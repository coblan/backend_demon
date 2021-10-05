<template>
  <div>
    <draggable
        class="dragArea list-group"
        :list="comList"
        :group="{ name: groupName, pull: 'clone', put: false }"
        :clone="cloneNode"
    >
      <div
          class="list-group-item"
          v-for="element in comList"
          :key="element.editor"
      >
        {{ element.label }}
      </div>
    </draggable>
  </div>
</template>
<script>
import blockSettingMix from "./blockSettingMix.js";
export  default  {
  props:{
    comList:{

    },
    groupName:{

    }
  },
  data(){
    return {
    }
  },
  // mixins:[blockSettingMix],
  methods:{
    cloneNode(node){
      ex.count += 1
      // this.ctx.genVc.parStore.count +=1
      var node1= ex.copy(node)
      node1.index= ex.count //  this.ctx.genVc.parStore.count
      return node1
    }
  }
}
</script>
