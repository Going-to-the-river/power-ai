<template>
  <div class="wrapper">
    <div class="menu">
      <div class="item" style="font-size: 20px">
        Power AI
      </div>

      <div class="item" style="font-size: 15px">
        Advanced Energy Analytics
      </div>

      <div class="item" style="font-size: 15px; margin-left: 40px">
        Powered by "Going To The River" team
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

    border-top: var(--color-brown-light) 1px solid;
    background-color: #fff;

    font-size: 20px;
    color: var(--color-brown-dark);

    box-shadow: 0 0 10px #999;
  }

  .menu {
    display: flex;
    flex-direction: row;
    justify-content: center;
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

</style>
