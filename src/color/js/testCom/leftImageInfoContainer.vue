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
let count =1
export  default  {
  props:['ctx'],
  data(){
    return {
      // com_list:[ ],
    }
  },
  methods:{
    open_drag(){
      cfg.pop_vue_com(leftImageInfoPannel,{},{shade:0,maxmin: true,offset:'rt',area:['500px','500px']})
    }
  }
}
</script>
