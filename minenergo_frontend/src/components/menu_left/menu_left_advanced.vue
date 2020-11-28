<template>
  <div class="wrapper">
    <div class="main-header">
      Выбор региона
    </div>

    <div class="root list">
      <div
        v-for="(location, idx) in locations"
        class="item"
      >
        <div class="item-label">
          <span>
            <i class="map marker alternate icon"></i>
            {{location.title}}
          </span>

          <div v-if="location.is_expanded" class="clickable">
            <i
              class="caret up icon"
              @click="location.is_expanded = false"
            ></i>
          </div>
          <div v-else class="clickable">
            <i
              class="caret down icon"
              @click="location.is_expanded = true"
            ></i>
          </div>
        </div>

        <div
          v-if="location.is_expanded"
          class="list"
        >
          <div
            v-for="(graph, idx) in location.graphs"
            class="item"
          >
            <!--~~~~~~~~~~~~~~~START GRAPH LEAF~~~~~~~~~~~~~~~-->
            <div v-if="!graph.is_group">
              <div class="item-label">
                <span>
                  <i class="chart line icon"></i>
                  {{graph.title}}
                </span>

                <div v-if="graph.is_selected" class="clickable">
                  <i
                    class="check square icon"
                    @click="graph.is_selected = false"
                  ></i>
                </div>
                <div v-else class="clickable">
                  <i
                    class="stop icon"
                    @click="graph.is_selected = true"
                  ></i>
                </div>

              </div>
            </div>
            <!--~~~~~~~~~~~~~~~END GRAPH LEAF~~~~~~~~~~~~~~~-->
            <div v-else>
              <div class="item-label">
                <span>
                  <i class="folder icon"></i>
                  {{graph.title}}
                </span>
              </div>

              <div class="list">
                <div
                  v-for="(graph_v2, idx) in graph.children"
                  class="item"
                >
                  <!--~~~~~~~~~~~~~~~START GRAPH LEAF~~~~~~~~~~~~~~~-->
                  <div v-if="!graph_v2.is_group">
                    <div class="item-label">
                      <span>
                        <i class="chart line icon"></i>
                        {{graph_v2.title}}
                      </span>

                      <div v-if="graph_v2.is_selected" class="clickable">
                        <i
                          class="check square icon"
                          @click="graph_v2.is_selected = false"
                        ></i>
                      </div>
                      <div v-else class="clickable">
                        <i
                          class="stop icon"
                          @click="graph_v2.is_selected = true"
                        ></i>
                      </div>
                    </div>
                  </div>
                  <!--~~~~~~~~~~~~~~~END GRAPH LEAF~~~~~~~~~~~~~~~-->
                </div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
  import utils from '../utils/utils'

  export default {
    props:{
      is_expanded_by_default:{
        type:Boolean,
        default:true
      },
      is_selected_by_default:{
        type:Boolean,
        default:false
      }
    },
    data(){
      return{
        locations:this.$store.state.locations,
      }
    },
    created() {
      // utils.set_all_graphs_selected(this.locations, this.is_selected_by_default)
      utils.set_all_graphs_selected(this.locations, false)
      utils.set_location_graphs_selected(this.locations, 0, true)

      utils.set_all_graphs_expanded(this.locations, this.is_expanded_by_default)
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

    margin-left: 20px;

    font-size: 15px;
  }

  .root.list{
    margin-top: 10px;
    margin-left: 0px;

    height: calc(100% - 80px);
    overflow-y: auto;
  }

  .item .item-label{
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    padding: 5px 10px;

    border-radius: 5px;
  }

  .clickable{
    height: fit-content;

    padding-left: 4px;

    border-radius: 5px;

    cursor: pointer;
  }
  .clickable:hover{
    background-color: #ddd;
  }

</style>
