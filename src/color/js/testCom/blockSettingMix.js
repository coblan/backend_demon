export  default  {
    methods:{
        cloneNode(node){
            this.ctx.genVc.blockEditorStore.count +=1
            var node1= ex.copy(node)
            node1.index= this.ctx.genVc.blockEditorStore.count
            return node1
        }
    }
}