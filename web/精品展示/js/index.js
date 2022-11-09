$(function(){


    // 鼠标经过左侧的小li
    $(".left li").mouseover(function(){
            $(this).addClass("current").siblings().removeClass("current");
            // 得到当前小li的索引号
         var index=$(this).index();
        //让我们右侧的盒子相应索引号的图片显示出来就好
        // 让其与的图片（就是其他的兄弟）隐藏起来
        // 用链式编程
        $(".content div").eq(index).show().siblings().hide();

    });
})