<template>
  <div>
    <button @click="is_prod = !is_prod">切换</button>
    <button @click="save_com_list">保存</button>
    <comDragableContainer
        :com-list="com_list"
        group-name="blockEditor"
        title="blockEditor"
        :com-options="com_options"
        :configHeads="config_heads"
        :row.sync="row"
        :append-ops="append_ops"
    >
    </comDragableContainer>
  </div>

</template>
<script>
import comDragableContainer from "../testCom/comDragableContainer.vue";

export  default  {
  components:{
    comDragableContainer
  },
  data(){
    var self = this

    var childStore = new Vue()
    childStore.vc = this
    childStore.name='blockEditorStore'
    return {
      row:{},
      is_prod:true,
      com_list:[ ],
      parStore:ex.vueParStore(this),
      childStore:childStore,
      // blockEditorStore:ex.vueAssign(this,{name:'blockEditorStore'}),
      com_options:[
        {'editor':'block-flexDiv','label':'FlexDiv','com_list':[],row:{} },
        {'editor':'block-leftImageInfoContainer','label':'block-leftImageInfoContainer',
          'com_list':[],row:{}},
        {'editor':'block-h2-title','label':'H2标题','com_list':[],row:{} },
      ],
      config_heads:[
        // {'name':'data_src','label':'数据源','editor':'com-field-linetext'},
      ],
      append_ops:[
        // {'editor':'com-btn','label':'获取数据','click_express':'var pp = ex.vueParStore(scope.vc,{name:"leftImageInfoContainer"});pp.vc.getData(scope.ps.vc.row)'},
      ]
      // com_list:[ ],
    }
  },
  mounted(){
    ex.director_call('get_test_com_list',{}).then(resp=>{

      if(resp){
        var bb = JSON.parse(resp)
        this.com_list =bb.com_list
        // this.childStore.count = bb.count
        ex.count = bb.count
      }
    })
  },
  methods:{
    save_com_list(){
      cfg.show_load()
      var bb = {com_list:this.com_list,count:ex.count}
      var post_data= JSON.stringify(bb)
      ex.director_call('save_test_com_list',{com_list:post_data}).then(resp=>{
        cfg.hide_load()
      })
    },
  }
}
</script>
