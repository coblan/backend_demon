<template>
  <div>
    <div draggable="true" @dragstart="on_drag_start" id="no">com_test1</div>
  </div>
</template>
<script>
export  default  {
  methods:{
    on_drag_start(env){
       // env.dataTransfer.setData("Text",env.target.id);
      var com = {'editor':'block-flexDiv'}
      env.dataTransfer.setData("Text",JSON.stringify(com));
      window._drag_data = com
    }
  }
}
</script>
