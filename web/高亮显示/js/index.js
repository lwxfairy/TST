$(function(){
    //鼠标进入的时候，其他的livia噢前透明度为0.5
    $(".wrap li").hover(function(){
        $(this).siblings().stop().fadeTo(400,0.5);

    },function(){
 //鼠标离开。其他li透明度改为1
 //区分大小写，大小写写错了，会加载失败
 $(this).siblings().stop().fadeTo(400,1);

    })   
})