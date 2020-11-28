<template>
  <div id="app" style="min-height: 100%">
    <router-view/>
  </div>
</template>

<script>

  export default {
  }
</script>

<style>

:root {
  --desktop-width: 1080px;
  --color-brown-light: #963;
  --color-brown-dark: #663300;
  --color-grey-light: #f0f0f0;
}

body{
  font-family: 'Roboto', sans-serif;
}



/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
.ui input{
  border-color: #963 !important;
  color: #630 !important;
}
.ui input::placeholder{
  color: #963 !important;
}

</style>
