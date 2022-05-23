<template>
  <div class="editor-tab">
    <editorViewer style="flex-grow: 10" :bus="bus"></editorViewer>
    <editorTree :bus="bus"></editorTree>
  </div>
</template>
<script>
import editorViewer from './editorViewer.vue'
import editorTree from './editorTree.vue'
export default {
  props:['tab_head','par_row'],
  components:{
    editorViewer,
    editorTree
  },
  data(){
    return {
      bus:{
        coms:[]
      }
    }

  },
  mounted(){
    this.bus.coms = JSON.parse(this.par_row.content)
  }
}
</script>
<style scoped lang="scss">
.editor-tab{
  height: 100%;
  width: 100%;
  overflow: auto;
  display: flex;

}
</style>