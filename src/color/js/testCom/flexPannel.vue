<template>
  <div>
    <draggable
        class="dragArea list-group"
        :list="com_list"
        :group="{ name: 'flexPannel', pull: 'clone', put: false }"
        :clone="cloneDog"
    >
      <div
          class="list-group-item"
          v-for="element in com_list"
          :key="element.editor"
      >
        {{ element.label }}
      </div>
    </draggable>
    <com-form-one :ctx="fields_ctx"></com-form-one>
  </div>
</template>
<script>

export  default  {
  props:['ctx'],
  data(){
    debugger
    return {
      com_list:[
        {'editor':'block-colorDiv','label':'colorDiv',row:{}}
      ],
      fields_ctx:{
        heads:[
          {'name':'data_src','label':'数据源','editor':'com-field-linetext'},
        ],
        row:{
          data_src:this.ctx.data_src,
        },
      }
    }
  },
  methods:{
    cloneDog(node){
      this.ctx.genVc.parStore.count +=1
      var node1= ex.copy(node)
      node1.index= this.ctx.genVc.parStore.count
      return node1
    }
  }
}
</script>
