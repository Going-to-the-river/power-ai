<template>
  <div>
    <back_map></back_map>
    <menu_left_simple></menu_left_simple>
    <menu_right></menu_right>
  </div>
</template>

<script>
  import back_map from "../back_map/back_map"
  import menu_left_simple from "../menu_left/menu_left_simple";
  import menu_right from "../menu_right/menu_right";

  export default {
    components:{
      back_map,
      menu_left_simple,
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
