<template>
  <div class="editor-float">
    <slot></slot>
    <div class="floater" v-if="canEdit">
      <div class="operations">
        <button @click="triggerEdit">编辑</button>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  props:{
    row:{},
    fields:{},
    fieldsGroup:{},
    canEdit:{
      default:true
    }
  },
  data(){
    return {}
  },
  methods:{
    async triggerEdit(){
      var fields_ctx = {
        heads:this.fields,
        row:this.row,
        save_fun:(vc)=>{vc.$emit('finish',vc.row)},
        ops:[
          {name:'save',label:'确定',editor:'com-btn',click_express:'scope.ps.vc.beforeSubmit().then(()=>{  if(scope.ps.vc.isValid()){ scope.ps.vc.ctx.save_fun(scope.ps.vc)}  })  '},
        ],
      }
      if(this.fieldsGroup){
        fields_ctx.fields_group = this.fieldsGroup
      }
      var resp = await cfg.pop_vue_com('com-form-one',fields_ctx)
      this.$emit('update:row',resp)
      this.$emit('change')
    }
  }
}
</script>
<style scoped lang="scss">
.editor-float{
  position: relative;
  .floater{
    position: absolute;
    top:0;
    left: 0;
    right: 0;
    bottom: 0;
    &:hover{
      background-color: rgba(0,0,0,.2);
      .operations{
        display: flex;
      }
    }
    .operations{
      display: none;
    }
  }
}

</style>
