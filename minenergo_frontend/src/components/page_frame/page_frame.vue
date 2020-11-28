<template>
  <div>
    <router-view></router-view>

    <div class="menu top">
      <quick_access_line></quick_access_line>
    </div>

    <div class="menu bottom">
      <footer_line></footer_line>
    </div>

  </div>
</template>

<script>
  import quick_access_line from "./quick_access_line/quick_access_line";
  import footer_line from "./footer_line/footer_line";

  export default {
    components:{
      quick_access_line,
      footer_line,
    },
    data(){
      return{
      }
    },
  }
</script>


<style scoped>
  .menu{
    position: absolute;

    left: 0;
    width: 100%;
  }

  .menu.top{
    top: 0;
  }

  .menu.bottom{
    bottom: 0;
  }


</style>
