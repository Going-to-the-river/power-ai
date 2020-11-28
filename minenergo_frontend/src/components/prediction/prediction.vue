<template>
  <div
    class="wrapper"
  >
    <div class="menu top">
      Интерактивное предсказание
    </div>

    <div class="content-container">

      <div class="list">
        <div
          v-for="(feature, idx) in features"
          class="item"
        >
          <graph :graph_id="feature.graph_id" :title="feature.title"></graph>

          <div style="display: flex; flex-direction: row; justify-content: space-around; align-items: center">
            <div style="font-size: 20px;">
              Задайте масштабирование (0 - 1000%)
            </div>
            <div class="ui input">
<!--              <input-->
<!--                type="number" min="0" max="1000" value="100"-->
<!--                @change="set_scale(feature, $event)"-->
<!--              >-->
              <input
                type="number" min="0" max="1000"
                v-model="feature.scale_percent"
                @change="set_scale(feature, $event)"
              >
            </div>
            <div style="font-size: 20px">
              %
            </div>

          </div>


        </div>
      </div>

      <div class="button-wrapper">
        <div
          class="ui big red button"
          @click="get_prediction"
        >
          Рассчитать
        </div>
      </div>

      <div class="prediction-wrapper">
        <div class="prediction">
          <graph
            v-if="is_prediction_ready"
            title="Предсказание"
            :graph_id="-1"
            :is_immutable="true"
            :immutable_datasets="make_immutable_datasets()"
          ></graph>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
  import graph from "../menu_right/graph";
  import Vue from "vue";
  import utils from "../utils/utils";

  export default {
    components:{
      graph
    },
    props:{
    },
    data(){
      return{
        features:this.$store.state.features,

        prediction_graph_data:this.$store.state.prediction_graph_data,
        baseline_graph_data:this.$store.state.baseline_graph_data,

        last_resolution:null,
        last_date:null,

        is_prediction_ready: false,
      }
    },
    methods:{
      set_scale(feature, event){
        var new_value = parseInt(event.target.value)

        new_value = new_value > 1000 ? 1000 : new_value;
        new_value = new_value < 0 ? 0 : new_value;

        feature.scale_percent = new_value
      },
      async get_prediction(){
        this.is_prediction_ready = false

        var data = {
          features: this.features,
        }
        await this.$store.dispatch('get_prediction', data)

        this.is_prediction_ready = true
      },
      make_immutable_datasets(){
        var ds = [
          {
            label:'Базовое предсказание',
            data:this.baseline_graph_data,
          },
          {
            label:'Интерактивное предсказание',
            data:this.prediction_graph_data,
            borderColor:'#f93',
            pointBackgroundColor:'#f93',
          }
        ]

        console.log(ds)

        return ds
      }
    },
    created() {
      this.last_resolution = this.$store.state.current_graph_resolution
      this.$store.state.current_graph_resolution = this.$store.state.GRAPH_RESOLUTIONS.DAY

      //~~~~~~~~~~~~~~~~~~~~~~~~~
      this.last_date = this.$store.state.current_graph_date

      var today = new Date()
      today.setHours(0,0,0,0)

      var new_date = new Date(today)
      new_date.setDate(new_date.getDate() - 15);

      this.$store.state.current_graph_date = new_date

      var features = this.features
      for(var i = 0; i < features.length; i++){
        var feature = features[i]

        Vue.set(feature, 'scale_percent', 100)
      }
    },
    beforeDestroy() {
      this.$store.state.current_graph_resolution = this.last_resolution
      this.$store.state.current_graph_date = this.last_date
    }
  }
</script>

<style scoped>
  .wrapper{
    position: absolute;

    display: flex;
    flex-direction: column;
    justify-content: space-between;

    right: 0;
    top: 45px;
    bottom: 45px;
    width: 100%;

    background-color: #fff;
    border: #333 1px solid;
    box-shadow: 0 0 10px #999;

    transition: width 0.5s;
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

  .menu{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    font-size: 20px;
    line-height: 30px;

    padding: 0 20px;
  }

  .menu.top{
    border-bottom: #333 1px solid;
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
  .content-container{
    display: flex;
    flex-direction: row;
    justify-content: space-around;

    height: calc(100% - 40px);
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
  .list{
    display: flex;
    flex-direction: column;
    justify-content: left;

    margin: 10px 10px;

    font-size: 15px;

    overflow-y: auto;
  }

  .list .item{
    display: flex;
    flex-direction: column;

    width: 600px;
    height: 400px;

    padding: 5px 10px;
    margin: 10px 0;

    border-radius: 5px;
    background-color: #f0f0f0;

    cursor: pointer;
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

  .button-wrapper{
    display: flex;
    flex-direction: column;
    justify-content: center;

    border-left: 3px solid #333;
    border-right: 3px solid #333;

    padding-left: 20px;
    padding-right: 18px;
  }

  .prediction-wrapper{
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .prediction{
    /*margin-right: 20px;*/

    width: 500px;
    height: 400px;
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/



</style>
