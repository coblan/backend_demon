<template>
  <div class="block-editor">
    <div class="com-select">
<!--      <treeBar></treeBar>-->
      <comPannel></comPannel>
    </div>
    <div class="block-content" >

<!--        <flexDiv></flexDiv>-->

      <draggable
          :list="com_list"
          :disabled="false"
          class="list-group"
          ghost-class="ghost"
          group="container"
          @start="dragging = true"
          @end="dragging = false"
      >
        <componet :is="item.editor" v-for="item in com_list" :key="item.index"></componet>
      </draggable>
    </div>
  </div>
</template>
<script>
// import  treeBar from './treeBar.vue'
import  comPannel from './comPannel.vue'
import flexDiv from "../testCom/flexDiv.vue";

export  default  {
  components:{
    // treeBar,
    comPannel,
    // draggable,
    flexDiv
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