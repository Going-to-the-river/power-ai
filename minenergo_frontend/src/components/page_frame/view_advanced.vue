<template>
  <div>
    <menu_left_advanced></menu_left_advanced>
    <menu_right :is_expert_mode="true"></menu_right>
  </div>
</template>

<script>
  import back_map from "../back_map/back_map"
  import menu_left_advanced from "../menu_left/menu_left_advanced";
  import menu_right from "../menu_right/menu_right";

  export default {
    components:{
      back_map,
      menu_left_advanced,
      menu_right
    },
    data(){
      return{
      }
    },
  }
</script>


<style scoped>
</style>
