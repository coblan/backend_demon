<template>
<!--  <div class="flex-div" @drop="drop_handler" @dragenter="drag_enter" @dragover.prevent @dragleave="drag_leave">-->
  <div>
    flex-div {{name}}
    <component :is="item.editor" v-for="item in com_list"></component>
    <component  class="fake-com" v-if="next_com" :is="next_com.editor" key="__next_com"></component>
  </div>
</template>
<script>
var count =1
export  default  {
  data(){
    count +=1
    return {
      com_list:[],
      next_com:{},
      name:count
    }
  },
  methods:{
    drop_handler(ev) {
      ev.preventDefault();
      var data = ev.dataTransfer.getData('Text')
      this.com_list.push((JSON.parse(data)))
      this.next_com ={}
      window._drag_data ={}
      ev.stopPropagation()
    },
    drag_enter(ev){
      console.log('enter')
      ev.preventDefault();
      // ev.stopPropagation()
      // if(window._drag_data){
      //   this.next_com = window._drag_data
      // }

    },
    drag_over(ev){
      ev.preventDefault();
      ev.stopPropagation()
      console.log('ff over')
    },
    drag_leave(ev){
      this.next_com ={}
      ev.preventDefault();
    },
  }
}
</script>
<style scoped lang="scss">
.flex-div{
  display: flex;
  border: 1px solid #e8e6e6;
  min-height: 50px;
}
//.fake-com{
//  pointer-events: none;
//}
</style>