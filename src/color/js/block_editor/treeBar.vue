<template>
  <div>
    <el-tree
        :data="allcom"
        show-checkbox
        node-key="id"
        default-expand-all
        :expand-on-click-node="false">

       <span class="custom-tree-node" slot-scope="{ node, data }">
        <span>{{ node.label }}</span>
        <span>
          <el-button
              type="text"
              size="mini"
              @click="() => append(data)">
            添加
          </el-button>
          <el-button
              type="text"
              size="mini"
              @click="() => remove(node, data)">
            删除
          </el-button>
           <el-button
               type="text"
               size="mini"
               @click="() => edit(node, data)">
            编辑
          </el-button>
        </span>
       </span>

    </el-tree>
  </div>
</template>
<script>
let id = 1000;
export  default  {
  data(){
    return {
      allcom:[
        {
          id: 1,
          label: '一级 1',
        }
      ]
    }
  },
  methods:{
    append(data) {
      const newChild = { id: id++, label: 'testtest', children: [] };
      if (!data.children) {
        this.$set(data, 'children', []);
      }
      data.children.push(newChild);
    },

    remove(node, data) {
      const parent = node.parent;
      const children = parent.data.children || parent.data;
      const index = children.findIndex(d => d.id === data.id);
      children.splice(index, 1);
    },
    edit(node,data){
      alert('edit')
    },
  }
}
</script>