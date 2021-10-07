<template>
  <div>
    <blockEditor :prod="ctx.prod"></blockEditor>
  </div>
</template>
<script>
import blockEditor from './block_editor/blockEditor2.vue'
export  default  {
  components:{
    blockEditor
  },
  props:['ctx'],
}
</script>