<template>
  <div class="block-editor">
    <div class="com-select">
<!--      <treeBar></treeBar>-->
      <comPannel></comPannel>
    </div>
    <div class="block-content" @drop="drop_handler" @dragenter="drag_enter" @dragover.prevent @dragleave="drag_leave">
        <component :is="item.editor" v-for="(item,index) in com_list" :key="item.name"></component>

        <component  class="bbc" v-if="next_com" :is="next_com.editor" key="__next_com"></component>
    </div>
    <draggable
        :list="com_list"
        :disabled="false"
        class="list-group"
        ghost-class="ghost"
        :move="checkMove"
        @start="dragging = true"
        @end="dragging = false"
    >
      <component :is="item.editor" v-for="(item,index) in com_list" :key="index"></component>
    </draggable>
  </div>
</template>
<script>
import  treeBar from './treeBar.vue'
import  comPannel from './comPannel.vue'
import draggable from "vuedraggable";

export  default  {
  components:{
    treeBar,
    comPannel,
    draggable
  },
  data(){
    return {
      com_list:[
      ],
      next_com:{},
    }
  },
  methods:{
    checkMove(){

    },
     drop_handler(ev) {
      ev.preventDefault();
      // Get the id of the target and add the moved element to the target's DOM
      // var data = ev.dataTransfer.getData("text/plain");
      var data = ev.dataTransfer.getData('Text')
       this.com_list.push((JSON.parse(data)))
       this.next_com ={}
       window._drag_data ={}
    },
    drag_enter(ev){
       // console.log('enter')
      ev.preventDefault();
      if(window._drag_data){
        this.next_com = window._drag_data
      }
      // var data = ev.dataTransfer.getData('Text')
      //
      // if(data){
      //   debugger
      //   this.next_com = JSON.parse(data)
      // }

    },
    drag_leave(ev){
      this.next_com ={}
      ev.preventDefault();
    },

  }

}
</script>
<style scoped lang="scss">
.block-editor{
  display: flex;
  min-height: 500px;
}
.com-select{
  background-color: #f5f4f4;
  width: 200px;
}
.block-content{
  flex-grow: 1;
  background-color: white;
}
//.bbc{
//  pointer-events: none;
//}
</style>