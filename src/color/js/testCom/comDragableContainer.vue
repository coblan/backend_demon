<template>
  <div class="flex-div">
    <button @click="open_config" v-if="edit">{{title}}</button>
    <draggable v-if="edit"
               :list="comList"
               :disabled="false"
               class="list-group"
               :class="row.layout"
               ghost-class="ghost"
               :group="groupName"
               @start="dragging = true"
               @end="dragging = false"
    >
      <componet  :is="item.editor" v-for="item in comList" :ctx="item" :key="item.index"></componet>
    </draggable>
    <div class="list-group" :class="row.layout" v-else>
      <componet :is="item.editor" v-for="item in comList" :ctx="item" :key="item.index"></componet>
    </div>
  </div>
</template>
<script>
import draggable from "vuedraggable"
import flexPannel from "./flexPannel.vue";
import containerEditor from "./containerEditor.vue";
export  default  {
  props:{
    comList:{},
    groupName:{},
    title:{},
    comOptions:{},
    configHeads:{},
    row:{},
    openConfig:{},
    appendOps:{
      default:()=>[]
    },
  },
  components:{
    draggable
  },

  data(){
    // var parStore = ex.vueParStore(this)
    return {
      rootStore:ex.vueParStore(this,{name:'blockEditorStore'})
      // name:this.ctx.index,
      // parStore:parStore,
    }
  },
  computed:{
    edit(){
      return !this.rootStore.vc.is_prod
    }
  },
  methods:{
    open_config(){
      if(this.openConfig){
        this.openConfig.call(this.$parent)
      }else{
        cfg.pop_vue_com(containerEditor,{
              title:this.title,
              row:this.row,
              groupName:this.groupName,
              comOptions:this.comOptions,
              configHeads:this.configHeads,
              appendOps:this.appendOps,
              genVc:this},
            {shade:0,maxmin: true,offset:'rt',area:['300px','600px']})
      }

      // this.$emit('pop-config')
      // debugger
      // cfg.pop_vue_com(flexPannel,{genVc:this},{shade:0,maxmin: true,offset:'rt',area:['500px','500px']})
    },
    save_row(row){
      this.$emit('update:row',row)
    }
  }
}
</script>
<style scoped lang="scss">
.flex-div{
  border: 1px solid #c9c8c8;
  //.list-group{
  //  display: flex;
  //  flex-direction: row;
  //}
}
.list-group{
  &.flex-row{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
  &.flex-column{
    display: flex;
    flex-direction: column;
  }
}
</style>