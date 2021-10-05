<template>
  <div class="flex-div">
    <button @click="open_config" v-if="!parStore.vc.is_prod">flex Dive {{name}}</button>
    <draggable v-if="! parStore.vc.is_prod"
        :list="ctx.com_list"
        :disabled="false"
        class="list-group"
        ghost-class="ghost"
        group="flexPannel"
        @start="dragging = true"
        @end="dragging = false"
    >
      <componet :is="item.editor" v-for="item in ctx.com_list" :ctx="item" :key="item.index"></componet>
    </draggable>
    <div class="list-group" v-else>
      <componet :is="item.editor" v-for="item in ctx.com_list" :ctx="item" :key="item.index"></componet>
    </div>
  </div>
</template>
<script>
import draggable from "vuedraggable"
import flexPannel from "./flexPannel.vue";

export  default  {
  props:['ctx'],
  components:{
    draggable
  },

  data(){
    var parStore = ex.vueParStore(this)
    return {
      name:this.ctx.index,
      parStore:parStore,
    }
  },
  methods:{
    open_config(){
      debugger
      cfg.pop_vue_com(flexPannel,{genVc:this},{shade:0,maxmin: true,offset:'rt',area:['500px','500px']})
    }
  }
}
</script>
<style scoped lang="scss">
.flex-div{
  border: 1px solid #c9c8c8;
  .list-group{
    display: flex;
    flex-direction: row;
  }
}
</style>