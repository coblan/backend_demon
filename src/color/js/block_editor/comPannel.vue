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
let count =1
export  default  {
  data(){
    return {
      container_list:[
        {'editor':'block-flexDiv','label':'FlexDiv',},
      ],
      editor_list:[
        {'editor':'block-colorDiv','label':'colorDiv',row:{}}
      ]
    }
  },
  methods:{
    cloneDog(node){
      count +=1
      var node1= ex.copy(node)
      node1.index=count
      return node1
    }
  }
}
</script>
