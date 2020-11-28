<template>
  <div class="wrapper">
    <div class="main-header">
      Выбор региона
    </div>

    <div class="list">
      <div
        v-for="(location, idx) in locations"
        class="item"
        :class="{active:is_location_active[idx]}"
        @click="select_location(location)"
      >
        <span>
          <i class="map marker alternate icon"></i>
          {{location.title}}
        </span>
      </div>
    </div>

  </div>
</template>

<script>
  import utils from '../utils/utils'

  export default {
    data(){
      return{
        locations:this.$store.state.locations,
      }
    },
    computed:{
      is_location_active(){
        var list = []
        var current_location = this.$store.state.current_location

        if(current_location === null){
          for(var i = 0; i < this.locations.length; i++){
            list.push(false)
          }
        }else{
          for(var i = 0; i < this.locations.length; i++){
            let is_active = this.locations[i].id === this.$store.state.current_location.id
            list.push(is_active)
          }
        }

        return list
      },
    },
    methods:{
      select_location(location){
        this.$store.state.current_location = location

        utils.set_all_graphs_selected(this.locations, false)
        utils.set_location_graphs_selected(this.locations, location.id, true)
      }
    },
    created() {
      utils.set_all_graphs_selected(this.locations, false)

      var current_location = this.$store.state.current_location
      if (current_location !== null){
        var id = this.$store.state.current_location.id
        utils.set_location_graphs_selected(this.locations, id, true)
      }
    }

  }
</script>

<style scoped>

  .wrapper{
    position: absolute;

    left: 0;
    top: 45px;
    bottom: 45px;
    width: 300px;

    background-color: #fff;
    border: #333 1px solid;
    box-shadow: 0 0 10px #999;
  }

  .main-header{
    font-size: 20px;
    line-height: 30px;

    padding-left: 20px;


    border-bottom: #333 1px solid;
  }

  .list{
    display: flex;
    flex-direction: column;
    justify-content: left;

    margin: 10px 10px;

    font-size: 15px;
  }

  .list .item{
    display: flex;
    flex-direction: row;
    justify-content: left;

    padding: 5px 10px;

    border-radius: 5px;

    cursor: pointer;
  }

  .list .item:hover{
    background-color: #eee;
  }

  .list .item.active{
    background-color: #ddd;
  }

  .list .item.active:hover{
    background-color: #ccc;
  }

</style>
