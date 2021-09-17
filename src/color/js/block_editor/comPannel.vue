<template>
  <div>
    <draggable
        class="dragArea list-group"
        :list="container_list"
        :group="{ name: 'container', pull: 'clone', put: false }"
        :clone="cloneDog"
    >
      <div
          class="list-group-item"
          v-for="element in container_list"
          :key="element.editor"
          :ctx="element"
      >
        {{ element.label }}
      </div>
    </draggable>

    <draggable
        class="dragArea list-group"
        :list="editor_list"
        :group="{ name: 'editor', pull: 'clone', put: false }"
        :clone="cloneDog"
    >
      <div
          class="list-group-item"
          v-for="element in editor_list"
          :key="element.editor"
      >
        {{ element.label }}
      </div>
    </draggable>

  </div>
</template>
<script>
export  default  {
  data(){
    return {
      parStore:ex.vueParStore(this),
      container_list:[
        {'editor':'block-flexDiv','label':'FlexDiv','com_list':[]},
        {'editor':'block-leftImageInfoContainer','label':'block-leftImageInfoContainer',
          'com_list':[],'row':{}},
      ],
      editor_list:[]
    }
  },
  methods:{
    cloneDog(node){
      this.parStore.count +=1
      var node1= ex.copy(node)
      node1.index= this.parStore.count
      return node1
    },

  }
}
</script>
