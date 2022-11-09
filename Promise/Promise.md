					Promise

#  Promise

##1.1promise是什么

###1.1.1 理解 

1. 抽象表达: 

   * Promise 是一门新的技术(ES6 规范) 

   * Promise 是 JS 中进行异步编程的新解决方案 备注：旧方案是单纯使用回调函数 
2. 具体表达: 
   * 从语法上来说: Promise 是一个构造函数 
   * 从功能上来说: promise 对象用来封装一个异步操作并可以获取其成功/ 失败的结果值

***

### 1.1.2. promise 的状态改变

1. pending 变为 resolved

2. pending 变为 rejected 

   说明: 只有这 2 种, 且一个 promise 对象只能改变一次 无论变为成功还是失败, 都会有一个结果数据 成功的结果数据一般称为 value, 失败的结果数据一般称为 reason



***

### 1.1.3.promise的基本流程

### ![image-20221024171105721](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221024171105721.png)



***

##1.2 如果使用promise

### 1.2.1.API 

1. Promise 构造函数: Promise (excutor) {}

    (1) executor 函数: 执行器 (resolve, reject) => {} 

    (2) resolve 函数: 内部定义成功时我们调用的函数 value => {}

    (3) reject 函数: 内部定义失败时我们调用的函数 reason => {} 

   说明: executor 会在 Promise 内部立即同步调用,异步操作在执行器中执行 

2. Promise.prototype.then 方法: (onResolved, onRejected) => {} 

   (1) onResolved 函数: 成功的回调函数 (value) => {}

    (2) onRejected 函数: 失败的回调函数 (reason) => {} 

   说明: 指定用于得到成功 value 的成功回调和用于得到失败 reason 的失败回调 返回一个新的 promise 对象

3.   Promise.prototype.catch 方法: (onRejected) => {} 

   (1) onRejected 函数: 失败的回调函数 (reason) => {

​		说明: then()的语法糖, 相当于: then(undefined, onRejected)

​	4. Promise.resolve 方法: (value) => {} 

​		(1) value: 成功的数据或 promise 对象

 		说明: 返回一个成功/失败的 promise 对象

5. Promise.reject 方法: (reason) => {}

 		(1) reason: 失败的原因 

​		说明: 返回一个失败的 promise 对象

6. Promise.all 方法: (promises) => {}

 		(1) promises: 包含 n 个 promise 的数组 

​		说明: 返回一个新的 promise, 只有所有的 promise 都成功才成功, 只要有一个		失败了就 直接失败 

7.  Promise.race 方法: (promises) => {} 

​		(1) promises: 包含 n 个 promise 的数组 

​		说明: 返回一个新的 promise, 第一个		完成的 promise 的结果状态就是最		终的结果状态

***

### 1.2.2 promise的几个关键问题

 1. 如何改变 promise 的状态? 

    (1) resolve(value): 如果当前是 pending 就会变为 resolved

     (2) reject(reason): 如果当前是 pending 就会变为 rejected 

    (3) 抛出异常: 如果当前是 pending 就会变为 rejected 

 2. 一个 promise 指定多个成功/失败回调函数, 都会调用吗? 

    当 promise 改变为对应状态时都会调用 

 3. 改变 promise 状态和指定回调函数谁先谁后? 

    (1) 都有可能, 正常情况下是先指定回调再改变状态, 但也可以先改状态再指定回调 

    (2) 如何先改状态再指定回调?

     ① 在执行器中直接调用 resolve()/reject() 

    ② 延迟更长时间才调用 then() 

    (3) 什么时候才能得到数据? 

    ① 如果先指定的回调, 那当状态发生改变时, 回调函数就会调用, 得到数据

     ② 如果先改变的状态, 那当指定回调时, 回调函数就会调用, 得到数据 

 4. promise.then()返回的新 promise 的结果状态由什么决定?

    (1) 简单表达: 由 then()指定的回调函数执行的结果决定

    (2) 详细表达:

    ① 如果抛出异常, 新 promise 变为 rejected, reason 为抛出的异常 

    ② 如果返回的是非 promise 的任意值, 新 promise 变为 resolved, value 为返回的值 

    ③ 如果返回的是另一个新 promise, 此 promise 的结果就会成为新 promise 的结果 

 5. promise 如何串连多个操作任务? 

    (1) promise 的 then()返回一个新的 promise, 可以开成 then()的链式调用 

    (2) 通过 then 的链式调用串连多个同步/异步任务

 6. promise 异常传透?

     (1) 当使用 promise 的 then 链式调用时, 可以在最后指定失败的回调, 

     (2) 前面任何操作出了异常, 都会传到最后失败的回调中处理

  7. 中断 promise 链? 

     (1) 当使用 promise 的 then 链式调用时, 在中间中断, 不再调用后面的回调函数 

     (2) 办法: 在回调函数中返回一个 pendding 状态的 promise 对象

****

## 2.async与await

### 2.1. mdn 文档

 https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/await 

###2.2. async 函数 
1. 函数的返回值为 promise 对象

2.  promise 对象的结果由 async 函数执行的返回值决定 

###2.3. await 表达式

1. await 右侧的表达式一般为 promise 对象, 但也可以是其它的值 
1.  如果表达式是 promise 对象, await 返回的是 promise 成功的值
1.  如果表达式是其它值, 直接将此值作为 await 的返回值
###2.4. 注意
1. await 必须写在 async 函数中, 但 async 函数中可以没有 await 
1.  如果 await 的 promise 失败了, 就会抛出异常, 需要通过 try...catch 捕获处理






***

## promise-Ajax请求

```js
 //接口地址 https://api.apiopen.top/getJoke
        //获取元素对象
        //绑定元素
        // const btn =$('#btn');
        const btn=document.querySelector('#btn');
        btn.addEventListener('click',function(){
            //创建promise
            const p=new Promise((resolve,reject)=>{
                //1.创建对象
                const xhr =new XMLHttpRequest();
                //2.初始化
                xhr.open('GET','https://api.apiopen.top/getJoke');
                //3.发送
                xhr.send();
                //4.处理响应结果
                xhr.onreadystatechange==function(){
                    if(xhr.readyState===4)
                    {
                        if(xhr.status>=200&&xhr.status<=300){
                            //5.控制台输出响应体
                            resolve(xhr.response);
                        }else{
                            //6.控制台输出响应状态码
                            reject(xhr.status);
                        }
                    }
                }

            });

            //调用then方法
            p.then(value=>{
                console.log(value);
            },reason=>{
                console.log(reson);
            });
        });
```

##封装ajax请求

```js
  //封装一个函数sendAjax发送GET Ajax请求
        //参数 URL
        //返回结果 promise对象
        function sendAjax(url){
            return new Promise((resolve,reject)=>{
                const xhr=new XMLHttpRequest();
                xhr.open('GET',url);
                xhr.responseType='json';
                xhr.send();
                //处理响应结果
                xhr.onreadystatechange=function(){
                    if(xhr.readyState===4)
                    {
                        if(xhr.status>=200&&xhr.status<=300)
                        {
                            resolve(xhr.response);
                        }else{
                            reject(xhr.status);
                        }
                    }
                }
            });
        }
        sendAjax('url').then(value=>{
            console.log(value);
        },reason=>{
            console.log(reason)
        })
```

***

## promise -fs模块

```js
const fs=require('fs');
 //回调函数形式
// fs.readFile('./resource/content.tex',(err,data)=>{
//     //如果出错，则抛出错误
//     if(err) throw err;
//     //输出文件内容
//     console.log(data.toString());
// });

//promise形式
let p =new Promise((resolve , reject)=>{
    fs.readFile('./resource/content.txt',(err,data)=>{
    //如果出错
    if(err) reject(err);
    //如果成功
    resolve(data);
    });
    
});

//调用then
p.then(value=>{
    console.log(value.toString());
},reason=>{
    console.log(reson);
})
```

## 封装fs模块

```js
const { resolve } = require('path');

/*
封装一个函数mineReadFile 读取文件内容
参数：path 问价路径
返回：promise对象
*/
function mineReadFlie(path){
    return new Promise((reslove,reject)=>{
        //读取文件
        require('fs').readFile(path,(err,data)=>{
            //判断
            if(err) reject(err);
            //成功
            resolve(data);
        })
    });
}

mineReadFlie(path).then(value=>{
    console.log(value);
}, reason=>{
    console.log(reason);
});
```



***

## util-promise方法

```js
/*
util-promise方法

*/
//引入util模块
const util=require('util');
//引入fs模块
const fs=require('fs');
//返回一个新的函数
let mineReadFile=util.promisify(fs.readFile);

mineReadFile('./resource/content.txt').then(value=>{
    console.log(value);
},reason=>{
    console.log(reason);
});
```

***

## 中断promise

```js
  let p= new Prmmise((resolve,reject)=>{
            setTimeout(()=>{
                resolve('ok');
            },1000)
        });

        p.then(value=>{
            console.log(111);
            //有且只有一个方式
            return new Promise(()=>{});
        }).then(value=>{
            console.log(333);
        }).catch(reason=>{
            console.warn(reason);
        });
```

***

## async与await结合

```js
   //axios
          function sendAJAX(url){
            return new Promise((resolve, reject) => {
                const xhr = new XMLHttpRequest();
                xhr.responseType = 'json';
                xhr.open("GET", url);
                xhr.send();
                //处理结果
                xhr.onreadystatechange = function(){
                    if(xhr.readyState === 4){
                        //判断成功
                        if(xhr.status >= 200 && xhr.status < 300){
                            //成功的结果
                            resolve(xhr.response);
                        }else{
                            reject(xhr.status);
                        }
                    }
                }
            });
        }
 //段子接口地址 https://api.apiopen.top/getJoke
        let btn =document.querySelector('#btn');
        btn.addEventListener('click',async function(){
            //获取段子信息
            let duanzi =await sendAJAX('https://api.apiopen.top/getJoke');
            console.log(duanzi);
        })

```



```js
/* 
resource 1.html  2.html 3.html 问价内容
*/
const fs =require('fs');
const util=require('util');
const mineReadFile=util.promisify(fs.readFile);

//回调函数的方式
// fs.readFile('./resource/1.html', (err, data1) => {
//     if(err) throw err;
//     fs.readFile('./resource/2.html', (err, data2) => {
//         if(err) throw err;
//         fs.readFile('./resource/3.html', (err, data3) => {
//             if(err) throw err;
//             console.log(data1 + data2 + data3);
//         });
//     });
// });

async和await结合
async function main(){
    try{
        //读取第一个文件的内容
        let data1 =await mineReadFile('./resource/1.html');
        let data2 =await mineReadFile('./resource/2.html');
        let data3 =await mineReadFile('./resource/3.html');
    }catch(e){
        //异常
        console.log(e);
    } 
}
main();
```



## 自定义promise

```html
//实例化对象
        // let p=new Promise((resolve,reject)=>{
        //    // resolve('OK');
        //    //reject('error')
        //    //抛出异常
        //    //throw "error";
        //    //异步任务
        //    setTimeout(()=>{
        //     reject("error");
        //    },1000)
        // });
        
        // p.then(value=>{
        //     console.log(value);
        // },reason=>{
        //     console.log(reason);
        // });

        // p.then(value=>{
        //     alert(value);
        // },reason=>{
        //    alert(reason);
        // });

        //同步修改状态
        //实例化对象
        // let p=new Promise((reslove,reject)=>{
        //     resolve('ok');
        // });
        // //执行then方法
        // const res =p.then(value=>{
        //     //抛出异常
        //     throw "FAIL";
            
        // },reason=>{
        //     console.warn(reason);
        // })

        // console.log(res);

        //异步修改状态
         //实例化对象
         let p = new Promise((resolve, reject) => {
            setTimeout(() => {
                // resolve('OK');
                reject("Error");
            }, 1000)
        });

        // //执行 then 方法
        // const res = p.then(value => {
        //     // return 'oh Yeah';
        //     throw 'error';
        // }, reason=>{
        //     // console.warn(reason);
        //     throw 'error';
        // });

        // console.log(res);


        //值传递
        // p.then()
        // .then(value=>{
        //     console.log(222);
        // }).then(value => {
        //     console.log(333);
        // }).catch(reason => {
        //     console.warn(reason);
        // });

        // resolve方法
        // const a=Promise.resolve('ok');
        // const a1=Promise.resolve(new Promise((resolve,reject)=>{
        //     resolve('Success');
        // }));
        // const a2=Promise.resolve(Promise.resolve('oh yeah'));

        //reject方法
        // const a=Promise.reject('ok');
        // const a1=Promise.reject(new Promise((resolve,reject)=>{
        //     reject("error")
        // }));
        // const a2=Promise.reject(Promise.reject('oh yeah'));

        
        let p1=new promise((resolve,reject)=>{
            setTimeout(()=>{
                resolve('ok');
            },1000)
        })
        let p2=promise.resolve('success');
        let p3=promise.reject('error');
        //调用all方法
        // let result=promise.all([p1,p2,p3]);
        // console.log(result);

        // 调用race方法
        let result=promise.race([p1,p2,p3]);
        console.log(result);

```



```js
/*
自定义promise
*/
(function(window){

//声明构造函数
/* Promise 构造函数
    excutor：内部同步执行的函数(resolve，reject)=>{}
*/
function Promise(excutor){
    //添加属性
    this.PromiseState = 'pending';//状态值，初始状态为pending，成功了变为
    //resolved，失败了变为rejected
    this.PromiseResult = null;//用来保存成功value或失败reason属性
    //声明属性
    this.callbacks=[];//用来保存所有待调用的包含onResolved和onRejected回调函数的对象的数组
    // this.callback = {};  一个回调
    //保存实例对象的 this 的值
    const that = this;//  _this that
    /*
    异步处理成功后应该调用的函数
    value：将交给onResolved()的成功数据
    */
    //resolve 函数
    function resolve(data){
        // 状态只能改变一次
        //判断状态
        if(that.PromiseState !== 'pending') return;//如果当前不是pending，直接结束
        //1. 修改对象的状态 (promiseState)
        //立即更新状态，保存数据
        that.PromiseState = 'fulfilled';// resolved
        //2. 设置对象结果值 (promiseResult)
        that.PromiseResult = data;
        //调用成功的回调函数
        // if(self.callback.onResolved){
        //     self.callback.onResolved(data);
        // } 一个回调

        // 异步调用所有待处理的onResolved回调函数
        setTimeout(()=>{
            that.callbacks.forEach(item=>{

                item.onResolved(data);
            });
        });
        
    }
    //reject 函数
    function reject(data){
        //状态只能改变一次
        //判断状态
        if(that.PromiseState !== 'pending') return;
        //1. 修改对象的状态 (promiseState)
        that.PromiseState = 'rejected';// 
        //2. 设置对象结果值 (promiseResult)
        that.PromiseResult = data;
        //执行失败回调
        // if(self.callback.onResolved){
        //     self.callback.onResolved(data);
        // }
        // 异步调用所有待处理的onRejected回调函数
        setTimeout(()=>{
            that.callbacks.forEach(item=>{
                item.onRejected(data);
            });
        });  
    }
    try{
        //同步调用『执行器函数』
        executor(resolve, reject);
    }catch(e){
        //修改 promise 对象状态为『失败』
        reject(e);
    }
}

/*
为promise指定成功/失败的回调函数
函数返回值是一个新的promise对象

*/
//添加 then 方法
Promise.prototype.then = function(onResolved, onRejected){
    const that =this;
    //判断回调函数参数
    //如果onResolved/onRejected不是函数，可它指定一个默认的函数
    if(typeof onRejected !=='function'){
        onRejected= reason=>{
            throw reason;
        }
        //指定返回的promise为一个失败状态，结果值为reason，
    }
    if(typeof onResolved !=='function'){
        onResolved=value=>value;
        //指定返回的promise为一个成功状态，结果值为value
    }
    //返回一个新的promise对象
    return new Promise((resolve,reject)=>{

        // 封装函数
        function callback(type){
            //1.抛出异常===>返回的promise变为rejected
            try {
                //获取回调函数的执行结果
                let result =onResolved(that.PromiseResult);
                //判断
                // 2.返回一个新的promise===>得到新的promise的结果值作为返回promise的结果值
                if(result instanceof Promise){
                    //如果是Promise类型的对象
                    result.then(v=> {
                        resolve(v);
                    }, r=>{
                        reject(r);
                    })
                }else{
                    //3.返回一个一般指(undefined)===>将之歌值作为返回的promise的成功值
                    //结果的对象状态为成功
                    resolve(result);
                }
        
               } catch (e) {
                reject(e);
               }
        }
    //调用回调函数  PromiseState
    if(this.PromiseState === 'fulfilled'){ //当前promise已经成功了
        setTimeout(()=>{
            callback(onResolved);
        });
      
    }
    if(this.PromiseState === 'rejected'){//当前promise已经失败了
        setTimeout(()=>{
            callback(onRejected);
        });
       
    }
    //判断 pending 状态
    //当前promise还未确定
    //将onResolved和onRejected保存起来
    if(this.PromiseState === 'pending'){
        //保存回调函数
        this.callbacks.push({
            onResolved:function(){
               callback(onResolved);
            },
            onRejected:function(){
               callback(onRejected);
                }

            });
        }

    })
   
}

/*
为promise指定失败的回调函数
是then（null,onRejected)\
*/
//添加catch方法
Promise.prototype.catch=function(onRejected){
    return this.then(undefined,onRejected);
}

/*
返回一个指定了成功value的promise对象
*/
//添加resolve方法
Promise.resolve=function(value){
    //返回promise对象
    return new Promise((resolve,reject)=>{
        if(value instanceof Promise){
            value.then(v=>{
                resolve(v);
            } ,r=>{
                reject(r);
            })
        }else{
            //状态设置为成功
            resolve(value);
        }
    });
}

/*返回一个指定失败reason的promise对象 */
//添加reject方法
Promise.reject=function(reason){
    return new Promise((resolve,reject)=>{
        reject(reason);
    });
}

/*
返回一个promise 只有promise中所有promise对象都成功时，才最终成功，只要有一个失败就直接返回失败 
*/
//添加all方法
Promise.all=function(promises){
    //返回一个新的promise
    return new Promise((resolve,reject)=>{
        //声明变量
        //已成功的数量
        let count=0;
        //准备一个保存成功值的数组
        let arr=[];
        //遍历每个待处理的promise
        for(let i=0;i<=promises.length;i++){
            //promise中元素可能不是一个数组，需要用resolve包装一下
            promises[i].then(v=>{
                //得知对象的状态是成功
                //每个promise对象 都成功
                count++;
                //将当前promise对象成功的结果 ，存入到数组中去
                arr[i]=v;
                //判断 全部成功
                if(conut===promises.length){
                    //修改状态
                    // 将所有成功值的数组作为返回promise对象的成功结果值
                    resolve(arr);
                }
            },r=>{
                // 将所有失败值的数组作为返回promise对象的失败结果值
                reject(r);
            });
        }
    });
}

/*
返回一个promise，一旦某个promise解决或拒绝，返回的promise就会解决或拒绝
*/
//添加race方法
Promise.race=function(promises){
    return new Promise((resolve,reject)=>{
        //遍历所有promise
        for(let i=0;i<=promises.length;i++){
            promises[i].then(v=>{
                //只要有一个成功了，返回的Promise就成功了
                //修改返回对象的状态为【成功】
                resolve(v);
            },r=>{
                 //只要有一个一个了，返回的Promise就失败了
                //修改返回对象的状态为【失败】
                reject(r);
            })
        }
    });
}

//返回一个延迟指定时间才确定结果的promise对象
Promise.resolveDelay=function(value,time){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            if(value instanceof promise){
                //如果value是一个promise，取这个promise的结果值作为返回的promise的结果值
                value.then(resolve,reject)//如果成功调用resolve(vel)如果value失败了，调用reject(reason)
            }
            else{
                resolve(value)
            }
        },time);
    });
}

//返回一个延迟指定时间才失败的promise对象
Promise.rejectDelay=function(reason,time){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            reject(reason);
        },time);
    });
}

    //暴露构造函数
    window.Promise=Promise;

})(window)


```















