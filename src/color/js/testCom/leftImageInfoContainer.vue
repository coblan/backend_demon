<template>
  <div>
    <button @click="open_drag">block-leftImageInfoContainer</button>
    <draggable
        class="dragArea list-group"
        :list="ctx.com_list"
        group="leftImageInfo"
    >
      <componet :is="item.editor" v-for="item in ctx.com_list" :ctx="item" :key="item.index"></componet>
    </draggable>
  </div>
</template>
<script>
import leftImageInfoPannel from "./leftImageInfoPannel.vue";
export  default  {
  props:['ctx'],
  data(){
    const childStore = new Vue()
    childStore.vc = this
    return {
      parStore:ex.vueParStore(this),
      childStore:childStore,
      // com_list:[ ],
    }
  },
  methods:{
    open_drag(){
      cfg.pop_vue_com(leftImageInfoPannel,{genVc:this,lay_row:this.ctx.lay_row},{shade:0,maxmin: true,offset:'rt',area:['500px','500px']})
    },
    save_row(row){
      ex.vueAssign(this.ctx.lay_row,row)
    },
    removeSelf(){
      this.parStore.vc.removeChildren(this.ctx.index)
    }
  }
}
</script>
