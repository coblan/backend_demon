
var my_click = {
    // head: {fun:'xxx'}
    props:['rowData','field','index'],
    template:`<div class="com-table-color-color" style="display: inline-block">
    <span style="display: inline-block;width: 20px;height: 20px;margin: 2px;border-radius: 10px;" :style="{background:mycolor}"></span>
    </div>`,
    created:function(){
        // find head from parent table
        var table_par = this.$parent
        while (true){
            if (table_par.heads){
                break
            }
            table_par = table_par.$parent
            if(!table_par){
                break
            }
        }
        this.table_par = table_par
        this. head  = ex.findone(this.table_par.heads,{name:this.field})

        this.parStore = ex.vueParStore(this)
    },
    computed:{
        mycolor(){
            if(this.head.value_field){
                var value = this.rowData[this.head.value_field]
            }else{
                var value = this.rowData[this.field]
            }
            return value
            //if(this.rowData[this.field]){
            //    return this.rowData[this.field]
            //}else{
            //    return ''
            //}
        }
    },
}

Vue.component('com-table-color-color',my_click)
