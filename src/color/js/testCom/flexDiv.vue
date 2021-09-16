<template>
  <div class="flex-div">
    <div>flex Dive {{name}}</div>
    <button @click="open_config">日</button>
    <draggable
        :list="com_list"
        :disabled="false"
        class="list-group"
        ghost-class="ghost"
        group="editor"
        @start="dragging = true"
        @end="dragging = false"
    >
      <componet :is="item.editor" v-for="item in com_list" :ctx="item" :key="item.index"></componet>
      <!--      <div-->
      <!--          class="list-group-item"-->
      <!--          v-for="element in list"-->
      <!--          :key="element.name"-->
      <!--      >-->
      <!--        {{ element.name }}-->
      <!--      </div>-->
    </draggable>
  </div>
</template>
<script>
import draggable from "vuedraggable"
let count = 1
export  default  {
  components:{
    draggable
  },
  data(){
    count +=1
    return {
      name:count,
      com_list:[]
    }
  },
  methods:{
    open_config(){
      alert('mimi')
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