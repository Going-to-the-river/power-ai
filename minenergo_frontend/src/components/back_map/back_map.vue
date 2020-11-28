<template>
  <div class="wrapper">
    <div class="rel-cont">

      <img
        src="../../../static/map_no_text.jpg"
        id="map_img"
      >

      <div class="abs-cont">
        <div class="rel-cont">
          <div
            v-for="(location, idx) in locations"
            class="floating-title"
            :class="{active:is_location_active[idx]}"
            :style="styles[idx]"
            @click="select_location(location)"
          >
            {{location.title}}
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
  import screen_width_mixin from "./screen_width_mixin";
  import utils from "../utils/utils";

  export default {
    mixins:[
      screen_width_mixin
    ],
    data(){
      return{
        locations:this.$store.state.locations,
      }
    },
    computed:{
      styles(){
        var list = []
        var locations = this.locations

        var w = this.screen_width - 600
        var h = w / 2

        for(var i = 0; i < locations.length; i++){
          var location = locations[i]
          var position = this.$store.state.location_position_by_id[location.id]

          var style = {
            left: (position.pos_x * w) + 'px',
            top: (position.pos_y * h) + 'px',
            fontSize: (15 * w / 1000) + 'px',
          }
          list.push(style)
        }
        return list
      },

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
      }
    },
    methods:{
      select_location(location){
        this.$store.state.current_location = location

        utils.set_all_graphs_selected(this.locations, false)
        utils.set_location_graphs_selected(this.locations, location.id, true)
      }
    }
  }
</script>

<style scoped>

  .wrapper{
    position: absolute;

    left: 300px;
    right: 300px;
    top: 145px;
    height: calc(100% - 145px);
  }

  #map_img{
    width: 100%;
  }

  /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
  .rel-cont{
    position: relative;
    width: 100%;
    height: 100%;
  }

  .abs-cont{
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
  }

  .floating-title{
    position: absolute;

    color: #fff;

    padding: 0px 5px;

    border-radius: 5px;

    cursor: pointer;
  }

  .floating-title:hover{
    background-color: rgba(255,255,255,0.3);
  }

  .floating-title.active{
    background-color: rgba(255,255,255,0.5);
  }

  .floating-title.active:hover{
    background-color: rgba(255,255,255,0.6);
  }

</style>
