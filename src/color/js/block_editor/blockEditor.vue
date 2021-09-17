<template>
  <div class="block-editor">
    <div class="com-select">
<!--      <treeBar></treeBar>-->
      <comPannel></comPannel>
    </div>
    <button @click="is_prod = !is_prod">切换</button>
    <button @click="save_com_list">保存</button>
    <div class="block-content" v-if="!is_prod">

      <draggable
          :list="com_list"
          :disabled="false"
          class="list-group"
          ghost-class="ghost"
          group="container"
          @start="dragging = true"
          @end="dragging = false"
      >
        <componet :is="item.editor" v-for="item in com_list" :key="item.index" :ctx="item"></componet>
      </draggable>
    </div>
    <div v-else>
        <componet :is="item.editor" v-for="item in com_list" :key="item.index" :ctx="item"></componet>
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
    var childStore = new Vue()
    childStore.vc = this
    childStore.count =1
    return {
      com_list:[],
      is_prod:false,
      childStore:childStore,
    }
  },
  mounted(){
    ex.director_call('get_test_com_list',{}).then(resp=>{
      if(resp){
        var bb = JSON.parse(resp)
        this.com_list =bb.com_list
        this.childStore.count = bb.count
      }
    })
  },
  methods:{
    save_com_list(){
      cfg.show_load()
      var bb = {com_list:this.com_list,count:this.childStore.count}
      var post_data= JSON.stringify(bb)
      ex.director_call('save_test_com_list',{com_list:post_data}).then(resp=>{
        cfg.hide_load()
      })
    },
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