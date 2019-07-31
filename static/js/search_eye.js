$(function(){
    $('.analyse_btn').click(function () {
        var img_id = this.nextSibling.textContent;
        var success_a = this.nextSibling.nextSibling.nextSibling;
        success_a.setAttribute('hidden',true);
        var url = '/output_img/'+img_id+'/';
        doAanalyseBack(url,this);
        this.disabled=true;
        this.style.background='black';
        this.style.marginLeft='23px';
        this.style.color='#fff';
        this.value=("正在分析中，请稍后");
    })
    $('.img_del').click(function () {
        var result = confirm("确认删除该图像？");
        if (result == true) {
            var img_id = this.nextSibling.textContent;
            var url = '/delimg/'+img_id+'/';
            doDelBack(url);
            alert("删除成功!");
            location.reload();
        }
    })
})
function doAanalyseBack(url,obj) {
    $.ajax({
        async : true,
        cache : false,
        type : "get",
        url : url,// 请求的action路径
        dataType:"json",
        success : function(data){
            if(data['error'] == 1){
                obj.style.background='red'
                obj.style.marginLeft='45px';
                obj.value=("分析函数出错");
                res = document.getElementById('analyse_error');
                res.style.display="block";
                setTimeout("res.style.display=\"none\"",3000)
            }
            else{
                obj.disabled=false;
                obj.style.background='#09c762'
                obj.style.marginLeft='7px';
                obj.style.color='';
                obj.value=("重新分析");
                success_a = obj.nextSibling.nextSibling.nextSibling;
                success_a.removeAttribute('hidden');
                success_a.href='/output/'+data['imgid'];
                mes = document.getElementById('analyse_ok');
                mes.style.display="block";
                setTimeout("mes.style.display=\"none\"",2000)
            }
        },
        error : function(data) {// 请求失败处理函数
            console.log('函数出错')
        },
    });
}
function doDelBack(url) {
    $.ajax({
        async : false,
        cache : false,
        type : "get",
        url : url,// 请求的action路径
        dataType:"json",
        success : function(data){
        },
        error : function(data) {// 请求失败处理函数
            console.log('函数出错')
        },
    });
}
