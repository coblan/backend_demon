<template>
  <div class="editor-tree">
    <div>
      <button @click="add">增加</button>
    </div>
    <div>
      <div v-for="ii in bus.coms">
        {{ii.label}}
      </div>
    </div>
  </div>
</template>
<script>
import ex from 'weblib/ex'
export default {
  props:{
    bus:{}
  },
  data(){
    return {
      coms_options:[]
    }
  },
  mounted(){
    this.getComponents()
  },
  methods:{
    async getComponents(){
      // var resp = await ex.director_get('uieditor/components/all')
      // this.coms_options=resp
      
      for(var k in cfg.uicoms){
        this.coms_options.push({value:cfg.uicoms[k],label:cfg.uicoms[k].label})
      }

    },
    async add(){

      var fields_ctx = {
        heads:[
          {name:'editor',label:'组件',editor:'com-field-select',options:this.coms_options,required:true},
          {name:'label',label:'名称',editor:'com-field-linetext',required:true},
        ],
        row:{},
        ops:[
          {name:'save',label:'确定',editor:'com-btn',click_express:'scope.ps.vc.beforeSubmit().then(()=>{  if(scope.ps.vc.isValid()){var vc= scope.ps.vc;vc.$emit("finish",vc.row)}  })  '},
        ],
      }
      var resp = await cfg.pop_vue_com('com-form-one',fields_ctx)
      this.bus.coms.push(
          {'editor':resp.editor,label:resp.label,bind:{} }
      )
    }
  }
}
</script>
<style scoped lang="scss">
.editor-tree{
  min-width: 150px;
}
</style>