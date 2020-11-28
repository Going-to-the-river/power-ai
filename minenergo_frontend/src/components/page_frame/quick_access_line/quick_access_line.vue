<template>
  <div class="wrapper">
    <div class="menu">
      <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~START BRANDING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
      <img
        src="/static/logo.png"
        style="height: 35px; width: 35px"
      >

      <div class="item" style="font-size: 30px">
        Power AI
      </div>
      <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END BRANDING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

      <div
        class="item link"
        :class="{active:$route.name === 'view_simple'}"
        @click="$router.push({name:'view_simple'})"
      >
        Простой
      </div>

      <div
        class="item link"
        :class="{active:$route.name === 'view_advanced'}"
        @click="$router.push({name:'view_advanced'})"
      >
        Продвинутый
      </div>

      <div
        class="item link"
        :class="{active:$route.name === 'view_prediction'}"
        @click="$router.push({name:'view_prediction'})"
      >
        Предсказание
      </div>

    </div>
  </div>
</template>

<script>

  export default {
    data(){
      return{
      }
    },
  }
</script>

<style scoped>
  .wrapper{
    height: 41px;
    line-height: 40px;

    border-bottom: var(--color-brown-light) 1px solid;
    background-color: #fff;

    font-size: 20px;
    color: var(--color-brown-dark);

    box-shadow: 0 0 10px #999;
  }

  .menu {
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;

    position: relative;

    max-width: var(--desktop-width);
    margin: auto;
  }

  .menu .item{
    padding: 0 10px;
    height: 100%;

    white-space: nowrap;

    line-height: 40px;

    position: relative;

    cursor: auto;
    user-select: auto;
  }

  .item.link{
    cursor: pointer;
  }
  .item.link:hover{
    background-color: #eee;
  }

  .item.link.active{
    background-color: #ddd;
  }

  .item.link.active:hover{
    background-color: #ccc;
  }


/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

  .link{
    color: #630;
    cursor: pointer;
  }

  .link:hover{
    color: #963;
  }

</style>
