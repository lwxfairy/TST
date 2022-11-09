$(function(){
    //点击发布按钮 动态创建一个li 放入文本框的内容和删除按钮，并且添加到ul中
    $(".btn").on("click" ,function(){
        var li=$("<li></li>");
        // 如果外围用了双分号，里面就要用单分号
        li.html($(".txt").val()+"<a href='javascipt:;'>删除</a>");
        $("ul").prepend(li);
        //添加元素不需要加分号
        li.slideDown();
        $(".txt").val("");
    })


    //点击删除按钮 可以删除当前的微博留言li
    // $("ul a").click(funciton(){
    //     //此时的click不给动态创建的a添加事件
    // })
    // on可以给动态创建的元素绑定事件
    $("ul").on("click","a",function(){
        $(this).parent().slideUp(function(){
            $(this).remove();
        })
    })
})