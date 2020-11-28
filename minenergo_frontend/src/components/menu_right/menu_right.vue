<template>
  <div
    class="wrapper"
    :class="{expanded: is_expanded}"
  >
    <div class="menu top">
      {{title}}

      <div v-if="is_fully_expanded" class="view-options">
        <div
          class="item"
          :class="{active:view_option === VIEW_OPTIONS.THREE_LINES}"
          @click="view_option = VIEW_OPTIONS.THREE_LINES"
        >
          <div style="height: 30px; overflow: hidden;">
            <i class="ui th big icon" style="margin-top: 3px"></i>
          </div>
        </div>

        <div
          class="item"
          :class="{active:view_option === VIEW_OPTIONS.TWO_LINES}"
          @click="view_option = VIEW_OPTIONS.TWO_LINES"
        >
          <i class="ui th large icon"></i>
        </div>

        <div
          class="item"
          :class="{active:view_option === VIEW_OPTIONS.ONE_LINE}"
          @click="view_option = VIEW_OPTIONS.ONE_LINE"
        >
          <i class="ui large stop icon"></i>
        </div>
      </div>

      <div v-if="!is_expert_mode">
        <i
          v-if="!is_expanded"
          class="expand arrows alternate icon"
          @click="set_expanded(true)"
        ></i>
        <i
          v-else
          class="compress icon"
          @click="set_expanded(false)"
        ></i>
      </div>


    </div>

    <div class="graphs">
      <div
        v-for="(graph, idx) in selected_graphs_list"
        :key="graph.id"
        class="graph"
        :class="graph_view_class"
      >
        <graph :graph_id="graph.id" :title="graph.title" :ylab="graph.ylab"></graph>
      </div>
    </div>

    <div class="menu bottom">


      <div class="view-options">
        <div v-if="is_fully_expanded" style="padding-right: 10px">
          Разрешение графиков:
        </div>

        <div
          v-for="(resolution) in $store.state.GRAPH_RESOLUTIONS"
          class="item v2"
          :class="{active: $store.state.current_graph_resolution.name === resolution.name}"
          @click="select_resolution(resolution)"
        >
          {{resolution.title}}
        </div>
      </div>

      <div v-if="is_fully_expanded" class="view-options">
        <div style="padding-right: 10px">
          Навигация по времени:
        </div>

        <div class="ui icon buttons">
          <div class="ui button" @click="add_to_current_graph_date(-10000)">
            <i class="angle double left icon"></i>
          </div>
          <div class="ui button" @click="add_to_current_graph_date(-100)">
            <i class="angle left icon"></i>
            x100
          </div>
          <div class="ui button" @click="add_to_current_graph_date(-10)">
            <i class="angle left icon"></i>
            x10
          </div>
          <div class="ui button" @click="add_to_current_graph_date(-1)">
            <i class="angle left icon"></i>
            x1
          </div>
          <div class="ui button" @click="add_to_current_graph_date(1)">
            x1
            <i class="angle right icon"></i>
          </div>
          <div class="ui button" @click="add_to_current_graph_date(10)">
            x10
            <i class="angle right icon"></i>
          </div>
          <div class="ui button" @click="add_to_current_graph_date(100)">
            x100
            <i class="angle right icon"></i>
          </div>
          <div class="ui button" @click="add_to_current_graph_date(10000)">
            <i class="angle double right icon"></i>
          </div>
        </div>

      </div>


    </div>

  </div>
</template>

<script>
  import graph from "./graph";
  import Vue from "vue";
  import utils from "../utils/utils";

  var VIEW_OPTIONS = {
    ONE_LINE:1,
    TWO_LINES:2,
    THREE_LINES:3
  }

  export default {
    components:{
      graph
    },
    props:{
      is_expert_mode:{
        type:Boolean,
        default:false
      },
    },
    data(){
      return{
        locations:this.$store.state.locations,

        is_expanded:false,
        is_fully_expanded:false,

        VIEW_OPTIONS:VIEW_OPTIONS,
        view_option:VIEW_OPTIONS.TWO_LINES
      }
    },
    computed:{
      title(){
        var current_location = this.$store.state.current_location

        if(this.is_expert_mode){
          return 'Сравнение показателей'
        }

        if (current_location === null){
          return 'Ничего не выбрано'
        }else {
          return current_location.title
        }
      },
      graph_view_class(){
        if(this.is_expanded){
          if(this.view_option === VIEW_OPTIONS.ONE_LINE){
            return {one_line:true}
          }else if(this.view_option === VIEW_OPTIONS.TWO_LINES){
            return {two_lines:true}
          }else{
            return {three_lines:true}
          }
        }else {
          return {collapsed:true}
        }
      },
      selected_graphs_list(){
        var list = []

        //~~~~~~~~~~~~~~~~start locations~~~~~~~~~~~~~~~~~~~~
        for(var i = 0; i < this.locations.length; i++){
          var location = this.locations[i]

          //~~~~~~~~~~~~~~~~start graphs~~~~~~~~~~~~~~~~~~~~
          var graphs = location.graphs
          for(var j = 0; j < graphs.length; j++){
            var graph = graphs[j]

            if(!graph.is_group){
              if(graph.is_selected){
                list.push(graph)
              }
            }else{
              //~~~~~~~~~~~~~~~~start graphs lvl 2~~~~~~~~~~~~~~~~~~~~
              var graphs_v2 = graph.children
              for(var k = 0; k < graphs_v2.length; k++){
                var graph_v2 = graphs_v2[k]

                if(!graph_v2.is_group){
                  if(graph_v2.is_selected){
                    list.push(graph_v2)
                  }
                }
              }
              //~~~~~~~~~~~~~~~~end graphs lvl 2~~~~~~~~~~~~~~~~~~~~
            }
          }
          //~~~~~~~~~~~~~~~~end graphs~~~~~~~~~~~~~~~~~~~~
        }
        //~~~~~~~~~~~~~~~~end locations~~~~~~~~~~~~~~~~~~~~

        return list
      },
    },
    methods:{
      select_resolution(resolution){
        this.$store.state.current_graph_resolution = resolution
      },
      set_expanded(is_expand){
        if(is_expand){
          this.is_expanded = true
          setTimeout(() => {
            this.is_fully_expanded = true
          }, 500)
        }else{
          this.is_expanded = false
          this.is_fully_expanded = false
        }
      },
      add_to_current_graph_date(value){
        var resolution =  this.$store.state.current_graph_resolution.name

        if (resolution === 'day'){
          value *= 1
        }else if(resolution === 'month'){
          value *= 30
        }else{
          value *= 365
        }

        var date_min = new Date('2000.01.01')
        var date_max = new Date()

        var new_date = new Date(this.$store.state.current_graph_date)
        new_date.setDate(new_date.getDate() + value);

        if(new_date.getTime() > date_max.getTime()){
          this.$store.state.current_graph_date = date_max
          return
        }
        if(new_date.getTime() < date_min.getTime()){
          this.$store.state.current_graph_date = date_min
          return
        }

        this.$store.state.current_graph_date = new_date
      }
    },
    created() {
      if(this.is_expert_mode){
        this.is_expanded = true
        this.is_fully_expanded = true
      }
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
    width: 300px;

    background-color: #fff;
    border: #333 1px solid;
    box-shadow: 0 0 10px #999;

    transition: width 0.5s;
  }

  .wrapper.expanded{
    width: calc(100%  - 305px);
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

  .menu.bottom{
    border-top: #333 1px solid;
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
  .view-options{
    display: flex;
    flex-direction: row;
  }

  .view-options .item{
    color: #666;

    cursor: pointer;
  }

  .view-options .item:hover{
    background-color: #ddd;
  }

  .view-options .item.active{
    color: #000;
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~*/
  .view-options .item.v2{
    padding: 0 10px;
  }

  .view-options .item.v2:hover{
    background-color: #ddd;
  }
  .view-options .item.v2.active{
    background-color: #d0d0d0;
  }
  .view-options .item.v2.active:hover{
    background-color: #c0c0c0;
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

  .graphs{
    display: flex;
    flex-direction: row;
    justify-content: left;
    flex-wrap: wrap;

    margin: 5px;

    font-size: 15px;

    height: calc(100% - 80px);
    overflow-y: auto;
  }

  .graph{
    margin: 10px;
  }

  .graph.collapsed{
    width: calc(100% - 20px);
    height: calc(33vh - 67px);
  }

  .graph.one_line{
    width: calc(100% - 20px);
    height: calc(100vh - 250px);
  }

  .graph.two_lines{
    width: calc(50% - 20px);
    height: calc(50vh - 125px);
  }

  .graph.three_lines{
    width: calc(33% - 20px);
    height: calc(33vh - 83px);
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/



</style>
