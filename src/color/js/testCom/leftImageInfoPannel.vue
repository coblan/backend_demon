<template>
  <div>
    <draggable
        class="dragArea list-group"
        :list="com_list"
        :group="{ name: 'leftImageInfo', pull: 'clone', put: false }"
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
let count =1
export  default  {
  props:['ctx'],
  data(){
    return {
      com_list:[
        {'editor':'block-leftImageInfo','label':'block-leftImageInfo',},
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
      count +=1
      var node1= ex.copy(node)
      node1.index=count
      return node1
    }
  }
}
</script>
