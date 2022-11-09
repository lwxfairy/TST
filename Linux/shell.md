# shell

## 第1章 shell概念

shell的概述：shell是一个命令行解释器，塔接受应用程序/命令，然后调用操作系统内核

1. Linux提供的shell解析器有

   ```linux
   [lwxfairy@hadoop100 ~]# cat /etc/shells
   /bin/sh
   /bin/bash
   /usr/bin/sh
   /usr/bin/bash
   /bin/tcsh
   /bin/csh
   
   ```

2. bash和sh的关系

    ```linux
    [lwxfairy@hadoop100 bin]# ll | grep bash
    -rwxr-xr-x. 1 root root     964536 11月 25 2021 bash
    lrwxrwxrwx. 1 root root         10 11月  3 07:50 bashbug -> bashbug-64
    -rwxr-xr-x. 1 root root       6964 11月 25 2021 bashbug-64
    lrwxrwxrwx. 1 root root          4 11月  3 07:50 sh -> bash
    
    
    ```

3. Centos默认的解析器是bash

   ```linux
   [lwxfairy@hadoop100 bin]# echo $SHELL
   /bin/bash
   ```

   ***
## 第2章 Shell脚本入门

1. 脚本格式

   脚本以#!/bin/bash开头（指定解析器）

2. 第一个 Shell 脚本：helloworld.sh 

* 需求：创建一个 Shell 脚本，输出 helloworld 

* 案例实操

  ```linux
  [lwxfairy@hadoop101 shells]$ touch helloworld.sh
  [lwxfairy@hadoop101 shells]$ vim helloworld.sh
  ```

  ```shell
  # 在 helloworld.sh 中输入如下内容
  #!/bin/bash
  echo "helloworld"
  ```
3. 脚本的常用执行方式 
***
### 2.1 第一种
采用 bash 或 sh+脚本的相对路径或绝对路径（不用赋予脚本+x 权限)
* sh+脚本的相对路径

   ```linux
   [lwxfairy@hadoop101 shells]$ sh ./helloworld.sh
   Helloworld
   ```


* sh+脚本的绝对路径

  ```linux
  [lexfairy@hadoop101 shells]$ sh /home/lwxffairy/shells/helloworld.sh
  helloworld
  ```

* bash+脚本的相对路径

  ```linux
  [lwxfairy@hadoop101 shells]$ bash ./helloworld.sh
  Helloworld
  ```

* bash+脚本的绝对路径

  ```linux
  [lwxfairy@hadoop101 shells]$ bash /home/lwxfairy/shells/helloworld.sh
  Helloworld
  ```
***
### 2.2 第二种
采用输入脚本的绝对路径或相对路径执行脚本（必须具有可执行权限+x）

  1. 首先要赋予 helloworld.sh 脚本的+x 权限

  ```linux
  [lwxfairy@hadoop101 shells]$ chmod +x helloworld.sh
  
  ```

  2. 执行脚本
     * 相对路径
     

       ```linux
       [lwxfairy@hadoop101 shells]$ ./helloworld.sh
       Helloworld
       ```
     
     * 绝对路径

  	```linux
  	[lwxfairy@hadoop101 shells]$ /home/atguigu/shells/helloworld.sh
  	 Helloworld

注意：第一种执行方法，本质是 bash 解析器帮你执行脚本，所以脚本本身不需要执行 权限。第二种执行方法，本质是脚本需要自己执行，所以需要执行权限
***
### 2.3 第三种
在脚本的路径前加上“.”或者 sourc

   1. 有一下脚本
	```linux
	[lwxfairy@hadoop101 shells]$ cat test.sh
	#!/bin/bash
	A=5
	echo $A

2. 分别使用 sh，bash，./ 和 . 的方式来执行，结果如下：

```linux
[lwxfairy@hadoop101 shells]$ bash test.sh
[lwxfairy@hadoop101 shells]$ echo $A
[lwxfairy@hadoop101 shells]$ sh test.sh
[lwxfairy@hadoop101 shells]$ echo $A
[lwxfairy@hadoop101 shells]$ ./test.sh
[lwxfairy@hadoop101 shells]$ echo $A
[lwxfairy@hadoop101 shells]$ . test.sh
[lwxfairy@hadoop101 shells]$ echo $A
5
```

原因： 前两种方式都是在当前 shell 中打开一个子 shell 来执行脚本内容，当脚本内容结束，则 子 shell 关闭，回到父 shell 中。 第三种，也就是使用在脚本路径前加“.”或者 source 的方式，可以使脚本内容在当前 shell 里执行，而无需打开子 shell！这也是为什么我们每次要修改完/etc/profile 文件以后，需 要 source 一下的原因。 开子 shell 与不开子 shell 的区别就在于，环境变量的继承关系，如在子 shell 中设置的 当前变量，父 shell 是不可见的。（可用sourse替代bash和sh

bash/sh/绝对路径/相对路径：启动子shell进程(影响不到父shell，有些执行命令不生效)，

source：不启动子shell（无父子嵌套环境）(在当前同一环境下执行，即所有执行命令生效)）

***
测试：
```linux
[user1@VM-4-6-centos ~]$ mkdir scripts
[user1@VM-4-6-centos ~]$ cd scripts
[user1@VM-4-6-centos scripts]$ touch hello.sh
[user1@VM-4-6-centos scripts]$ vim  hello.sh
[user1@VM-4-6-centos scripts]$ ls
hello.sh
[user1@VM-4-6-centos scripts]$ bash hello.sh
hello world
[user1@VM-4-6-centos scripts]$ cd ~
[user1@VM-4-6-centos ~]$ bash scripts/hello.sh
hello world
[user1@VM-4-6-centos ~]$ bash /root/scripts/hello.sh
bash: /root/scripts/hello.sh: Permission denied
[user1@VM-4-6-centos ~]$ ^C
[user1@VM-4-6-centos ~]$ ./hello.sh
-bash: ./hello.sh: No such file or directory
[user1@VM-4-6-centos ~]$ Permission deniedPermission denied^C
[user1@VM-4-6-centos ~]$ bash /root/scripts/hello.sh
bash: /root/scripts/hello.sh: Permission denied
[user1@VM-4-6-centos ~]$ chmod +x scripts/hello.sh
[user1@VM-4-6-centos ~]$  /root/scripts/hello.sh
-bash: /root/scripts/hello.sh: Permission denied
[user1@VM-4-6-centos ~]$ ll scripts/
total 4
-rwxrwxr-x 1 user1 user1 32 Nov  3 20:09 hello.sh
[user1@VM-4-6-centos ~]$ scripts/hello.sh
hello world
[user1@VM-4-6-centos ~]$ hello.sh
-bash: hello.sh: command not found
[user1@VM-4-6-centos ~]$ cd scripts/
[user1@VM-4-6-centos scripts]$ ./hello.sh
hello world
[user1@VM-4-6-centos scripts]$ source hello.sh
hello world
[user1@VM-4-6-centos scripts]$ source /root/scripts/hello.sh
-bash: /root/scripts/hello.sh: Permission denied
[user1@VM-4-6-centos scripts]$ . hello.sh
hello world
[user1@VM-4-6-centos scripts]$ type source
source is a shell builtin
[user1@VM-4-6-centos scripts]$ 


```

![image-20221103203128066](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103203128066.png)

![image-20221103205547880](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103205547880.png)

### 2.4 子shell



```linux
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    24210 16205  0 20:56 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$  bash
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    24275 16205  0 20:56 pts/2    00:00:00 bash
user1    24330 24275  0 20:57 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$ ./hello.sh
hello world
[user1@VM-4-6-centos scripts]$ exit
exit
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    24497 16205  0 20:58 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$ 

```

![image-20221103210326438](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103210326438.png)

##第3章 变量

### 3.1 系统预定义变量

1. 常见系统变量
$HOME、$PWD、$SHELL、$USER 等

2. 案例实操
 * 查看系统变量的值

```linux
[lwxfairy@hadoop101 shells]$ echo $HOME
/home/lwxfairy
```

* 显示当前shell中所有变量 ：set

```linux
[lwxfairy@hadoop101 shells]$ set
BASH=/bin/bash
BASH_ALIASES=()
BASH_ARGC=()
BASH_ARGV=()
```
***
全局环境变量

除了printenv不用加$访问全局环境 ,其他都要加$访问全局环境变量

测试：

```linux
[user1@VM-4-6-centos scripts]$ env | less
[user1@VM-4-6-centos scripts]$ 
[user1@VM-4-6-centos scripts]$ printenv | less
[user1@VM-4-6-centos scripts]$ printenv $USER
[user1@VM-4-6-centos scripts]$ printenv USER
user1
[user1@VM-4-6-centos scripts]$ echo $HOME
/home/user1
[user1@VM-4-6-centos scripts]$ ls $HOME
scripts
[user1@VM-4-6-centos scripts]$ bash
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    27014 16205  0 21:13 pts/2    00:00:00 bash
user1    27053 27014  0 21:14 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$ echo $HOME
/home/user1
[user1@VM-4-6-centos scripts]$ exit
exit
[user1@VM-4-6-centos scripts]$ 

```

***

### 3.2 自定义变量
1. 基本语法

* 定义变量：变量名=变量值，注意，=号前后不能有空格

* 撤销变量：unset 变量名

* 声明静态变量：readonly 变量，注意：不能 unset

2. 变量定义规则
* 变量名称可以由字母、数字和下划线组成，但是不能以数字开头，环境变量名建 议大写

* 等号两侧不能有空格

* 在 bash 中，变量默认类型都是字符串类型，无法直接进行数值运算

* 变量的值如果有空格，需要使用双引号或单引号括起来
***
测试：
```linux
[user1@VM-4-6-centos scripts]$ a=2
[user1@VM-4-6-centos scripts]$ echo $a
2
[user1@VM-4-6-centos scripts]$ echo $my_var

[user1@VM-4-6-centos scripts]$ my_var=hello
[user1@VM-4-6-centos scripts]$ echo $my_var
hello
[user1@VM-4-6-centos scripts]$ my_var=study
[user1@VM-4-6-centos scripts]$ echo $my_var
study
[user1@VM-4-6-centos scripts]$ my_var = HELLO
-bash: my_var: command not found
[user1@VM-4-6-centos scripts]$ my_var=hello, world
-bash: world: command not found
[user1@VM-4-6-centos scripts]$ my_var="hello, world"
[user1@VM-4-6-centos scripts]$ echo $my_var
hello, world
[user1@VM-4-6-centos scripts]$ my_var='hello, world'
[user1@VM-4-6-centos scripts]$ echo $my_var
hello, world
[user1@VM-4-6-centos scripts]$ env | grep my_var
[user1@VM-4-6-centos scripts]$ set | grep my_var
my_var='hello, world'
[user1@VM-4-6-centos scripts]$ bash
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    28980 16205  0 21:25 pts/2    00:00:00 bash
user1    29023 28980  0 21:25 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$ echo $my_var

[user1@VM-4-6-centos scripts]$ exit
exit
[user1@VM-4-6-centos scripts]$ echo $my_var
hello, world

```

![image-20221103212904917](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103212904917.png)

提升为全局变量

```linux
[user1@VM-4-6-centos scripts]$ export my_var
[user1@VM-4-6-centos scripts]$ echo $my_var
hello, world
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    30156 16205  0 21:32 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$ bash
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    30175 16205  0 21:33 pts/2    00:00:00 bash
user1    30231 30175  0 21:33 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$ echo $my_var
hello, world
[user1@VM-4-6-centos scripts]$ my_var="hello linux"
[user1@VM-4-6-centos scripts]$ echo $my_var
hello linux
[user1@VM-4-6-centos scripts]$ exit
exit
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    30342 16205  0 21:33 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$ echo $my_var
hello, world
[user1@VM-4-6-centos scripts]$ bash
[user1@VM-4-6-centos scripts]$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user1    16205 16204  0 20:06 pts/2    00:00:00 -bash
user1    30512 16205  0 21:34 pts/2    00:00:00 bash
user1    30636 30512  0 21:35 pts/2    00:00:00 ps -f
[user1@VM-4-6-centos scripts]$ my_var="hello linux"
[user1@VM-4-6-centos scripts]$ export my_var
[user1@VM-4-6-centos scripts]$ echo $my_var
hello linux
[user1@VM-4-6-centos scripts]$ exit
exit
[user1@VM-4-6-centos scripts]$ echo $my_var
hello, world
[user1@VM-4-6-centos scripts]$ 

```

![image-20221103214450661](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103214450661.png)

在子shell中更改不会影响父shell，在父shell中声明变量，子shell中也能访问到

```linux
[user1@VM-4-6-centos scripts]$ echo $new_var

[user1@VM-4-6-centos scripts]$ new_var="hello linux"
[user1@VM-4-6-centos scripts]$ echo $new_var
hello linux
[user1@VM-4-6-centos scripts]$ vim hello.sh
[user1@VM-4-6-centos scripts]$ ./hello.sh
hello world
hello, world

[user1@VM-4-6-centos scripts]$ . hello.sh
hello world
hello, world
hello linux
[user1@VM-4-6-centos scripts]$ export new_var
[user1@VM-4-6-centos scripts]$ ./hello.sh
hello world
hello, world
hello linux
[user1@VM-4-6-centos scripts]$ 

```

![image-20221103215818093](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103215818093.png)


```linux
[user1@VM-4-6-centos scripts]$ echo $a
2
[user1@VM-4-6-centos scripts]$ a=1+5
[user1@VM-4-6-centos scripts]$ echo $a
1+5
[user1@VM-4-6-centos scripts]$ a=$((1+5))
[user1@VM-4-6-centos scripts]$ echo $a
6
[user1@VM-4-6-centos scripts]$ a=$[5+9]
[user1@VM-4-6-centos scripts]$ echo $a
14
[user1@VM-4-6-centos scripts]$ readonly b=5
[user1@VM-4-6-centos scripts]$ b=10
-bash: b: readonly variable
[user1@VM-4-6-centos scripts]$ echo $b
5
[user1@VM-4-6-centos scripts]$ set | less
[user1@VM-4-6-centos scripts]$ unset a
[user1@VM-4-6-centos scripts]$ set | less
[user1@VM-4-6-centos scripts]$ unset b
-bash: unset: b: cannot unset: readonly variable
[user1@VM-4-6-centos scripts]$ ![image-20221103221219549](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103221219549.png)
```

平常的命令一般放在根目录中的/bin或/sbin中
***
### 3.3 特殊变量

#### 3.3.1 $n

1. 基本语法

   $n （功能描述：n 为数字，$0 代表该脚本名称，$1-$9 代表第一到第九个参数，十以 上的参数，十以上的参数需要用大括号包含，如${10}）

2. 案例实操

单引号不会认为里面的$是变量的表示符，而是会把里面的内容原封不动的输出

```shell
#!/bin/bash
echo '======$n====='
echo script name: $0
echo 1st paramater: $1
echo 2nd paramater: $2
```

```linux
[user1@VM-4-6-centos scripts]$ vim paramater.sh
[user1@VM-4-6-centos scripts]$ ll
total 8
-rwxrwxr-x 1 user1 user1 103 Nov  3 22:36 hello.sh
-rw-rw-r-- 1 user1 user1 100 Nov  3 22:38 paramater.sh
[user1@VM-4-6-centos scripts]$ chmod +x paramater.sh
[user1@VM-4-6-centos scripts]$ ll
total 8
-rwxrwxr-x 1 user1 user1 103 Nov  3 22:36 hello.sh
-rwxrwxr-x 1 user1 user1 100 Nov  3 22:38 paramater.sh
[user1@VM-4-6-centos scripts]$ ./paramater.sh abc def
=====$n=====
script name: ./paramater.sh
1st paramater: abc
2nd paramater: def
[user1@VM-4-6-centos scripts]$ 

```
***
#### 3.3.2 $#

1. 基本语法

   $# （功能描述：获取所有输入参数个数，常用于循环,判断参数的个数是否正确以及 加强脚本的健壮性）

2. 案例实操

 ```shell
 #!/bin/bash
 echo '======$n====='
 echo script name: $0
 echo 1st paramater: $1
 echo 2nd paramater: $2
 echo '======$#====='
 echo paramater numbers: $#
 ```

```linux
[user1@VM-4-6-centos scripts]$ vim paramater.sh
[user1@VM-4-6-centos scripts]$ ./paramater.sh
=====$0=====
script name: ./paramater.sh
1st paramater:
2nd paramater:
======$#=====
paramater numbers: 0
[user1@VM-4-6-centos scripts]$ ./paramater.sh abc def
=====$0=====
script name: ./paramater.sh
1st paramater: abc
2nd paramater: def
======$#=====
paramater numbers: 2
[user1@VM-4-6-centos scripts]$ 

```
***
#### 3.3.3 $*  $@

1. 基本语法

 $* （功能描述：这个变量代表命令行中所有的参数，$*把所有的参数看成一个整体）
 $@ （功能描述：这个变量也代表命令行中所有的参数，不过$@把每个参数区分对待）

2. 案例实操
 ```shell
 #!/bin/bash
 echo '======$n====='
 echo script name: $0
 echo 1st paramater: $1
 echo 2nd paramater: $2
 echo '======$#====='
 echo paramater numbers: $#
 echo '======$*====='
 echo $*
 echo '======$@====='
 echo $@
 ```
```linux
[user1@VM-4-6-centos scripts]$ ./paramater.sh abc def
=====$0=====
script name: ./paramater.sh
1st paramater: abc
2nd paramater: def
======$#=====
paramater numbers: 2
=====$*======
abc def
=====$@=====
abc def
[user1@VM-4-6-centos scripts]$ 

```
***
#### 3.3.4 $?

1. 基本语法
 $？ （功能描述：最后一次执行的命令的返回状态。如果这个变量的值为 0，证明上一 个命令正确执行；如果这个变量的值为非 0（具体是哪个数，由命令自己来决定），则证明 上一个命令执行不正确了。

```linux
[user1@VM-4-6-centos scripts]$ echo $?
130

```
***
##第4章 运算符

1. 基本语法

   “$((运算式))” 或 “$[运算式]”

2. 案例实操

   ```linux
   [lwxfairy@hadoop101 shells]# S=$[(2+3)*4]
   [lwxfairy@hadoop101 shells]# echo $S
   ```
***
## 第五章 条件判断

1. 基本语法
 * test condition 

 * [ condition ]
    注意 condition 前后要有空格） 注意：条件非空即为 true，[ atguigu ]返回 true，[ ] 
2. 常用判断条件
*  两个整数之间比较
  -eq 等于（equal）  -ne 不等于（not equal） -lt 小于（less than） -le 小于等于（less equal） -gt 大于（greater than） -ge 大于等于（greater equal）
  注：如果是字符串之间的比较 ，用等号“=”判断相等；用“!=”判断不等。 
  
*  按照文件权限进行判断
 -r 有读的权限（read）
  -w 有写的权限（write）
  -x 有执行的权限（execute） 

*  按照文件类型进行判断 
 -e 文件存在（existence）
  -f 文件存在并且是一个常规的文件（file） 
  -d 文件存在并且是一个目录（directory
***
 #### expr
```linux
[user1@VM-4-6-centos scripts]$ a= 1+2
-bash: 1+2: command not found
[user1@VM-4-6-centos scripts]$ a=1+2
[user1@VM-4-6-centos scripts]$ echo $a
1+2
[user1@VM-4-6-centos scripts]$ 1+2
-bash: 1+2: command not found
[user1@VM-4-6-centos scripts]$ expr 1 + 2
3
[user1@VM-4-6-centos scripts]$ expr 5 - 2
3
[user1@VM-4-6-centos scripts]$ ecpr 5 * 2
-bash: ecpr: command not found
[user1@VM-4-6-centos scripts]$ expr 5 * 2
expr: syntax error
[user1@VM-4-6-centos scripts]$ echo $[5*2]
10
[user1@VM-4-6-centos scripts]$ a=$[6+8]
[user1@VM-4-6-centos scripts]$ echo $a
14
[user1@VM-4-6-centos scripts]$ a=expr 5 \* 2
-bash: 5: command not found
[user1@VM-4-6-centos scripts]$ a="expr 5 \* 2"
[user1@VM-4-6-centos scripts]$ echo $a
expr 5 \* 2
[user1@VM-4-6-centos scripts]$ a=$(expr 5 \* 4)
[user1@VM-4-6-centos scripts]$ echo $a
20
[user1@VM-4-6-centos scripts]$ a=`expr 5 \* 4`
[user1@VM-4-6-centos scripts]$ echo $a
20
[user1@VM-4-6-centos scripts]$ 

```

```linux
[user1@VM-4-6-centos scripts]$ s=$[(2+3)*5]
[user1@VM-4-6-centos scripts]$ echo $s
25

```

![image-20221103231417546](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103231417546.png)

***

编写脚本进行赋值运算

```shell
#!/bin/bash
sum=$[$1 + $2]
echo sum=$sum
```

```linux
[user1@VM-4-6-centos scripts]$ vim add.sh
[user1@VM-4-6-centos scripts]$ chmod +x add.sh
[user1@VM-4-6-centos scripts]$ ./add.sh 25 89
sum=114

```
***
测试：
ture -> 0

false -> 1

输出重定向：>

输入重定向：<

两者不能作为条件判断

```linux
[user1@VM-4-6-centos scripts]$ a=hello
[user1@VM-4-6-centos scripts]$ echo $a
hello
[user1@VM-4-6-centos scripts]$ test $a = hello
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ test $a = Hello
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ a=Hello
[user1@VM-4-6-centos scripts]$ test $a = Hello
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ $a = Hello ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ $a = hello]
-bash: [: missing `]'
[user1@VM-4-6-centos scripts]$ [ $a = hello ]
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ [ $a=hello ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ abddd ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [  ]
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ [ $a != hello ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ $a != Hello ]
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ [ 2 = 8 ]
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ [ 2 = 2]
-bash: [: missing `]'
[user1@VM-4-6-centos scripts]$ echo $?
2
[user1@VM-4-6-centos scripts]$ [ 2 = 2 ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ 2 -lt 8 ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ 2 -gt 8 ]
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ 

```

![image-20221103234454253](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103234454253.png)

![image-20221103234600033](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103234600033.png)

```linux
 [user1@VM-4-6-centos scripts]$ ls
add.sh  hello.sh  paramater.sh
[user1@VM-4-6-centos scripts]$ touch test
[user1@VM-4-6-centos scripts]$ ls
add.sh  hello.sh  paramater.sh  test
[user1@VM-4-6-centos scripts]$ ll
total 12
-rwxrwxr-x 1 user1 user1  41 Nov  3 23:08 add.sh
-rwxrwxr-x 1 user1 user1 103 Nov  3 22:36 hello.sh
-rwxrwxr-x 1 user1 user1 204 Nov  3 22:52 paramater.sh
-rw-rw-r-- 1 user1 user1   0 Nov  3 23:46 test
[user1@VM-4-6-centos scripts]$ [ -r hello.sh ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ -w hello.sh ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ -x hello.sh ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ -r test.sh ]
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ [ -x test.sh ]
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ [ -e /home/user1
-bash: [: missing `]'
[user1@VM-4-6-centos scripts]$ [ -e /home/user1 ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ ls /home/user1/
scripts
[user1@VM-4-6-centos scripts]$ [ -f add.sh ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ [ -d add.sh ]
[user1@VM-4-6-centos scripts]$ echo $?
1
[user1@VM-4-6-centos scripts]$ [ -d /home/user1 ]
[user1@VM-4-6-centos scripts]$ echo $?
0
[user1@VM-4-6-centos scripts]$ 
```
![image-20221104001146710](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104001146710.png)

```linux
[user1@VM-4-6-centos scripts]$ a=15
[user1@VM-4-6-centos scripts]$ [ $a -lt 20 ] && echo "$a < 20" || "$a >= 20"
15 < 20
[user1@VM-4-6-centos scripts]$ a=27
[user1@VM-4-6-centos scripts]$ [ $a -lt 20 ] && echo "$a < 20" || "$a >= 20"
-bash: 27 >= 20: command not found
[user1@VM-4-6-centos scripts]$ 

```

***

## 第6章 流程控制

### 6.1 条件判断

1. 基本语法

```shell
if [ 条件判断式 ];then
	程序
fi
```

```shell
if [ 条件判断式 ]
then
	程序
fi
```

2. 多分支

```shell
if [ 条件判断式 ]
then
	程序
elif [ 条件判断式 ]
then 
	程序
else
	程序
fi
```
注意事项：

* [ 条件判断式 ]，中括号和条件判断式之间必须有空格

* if 后要有空格
***
#### if
```shell
#!/bin/bash
if [ $1 = user1 ]
then 
	echo "welcome,user1"
fi
```

![image-20221104004137872](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104004137872.png)

-a为and ， -o为or

```linux
[user1@VM-4-6-centos scripts]$ if [ $a -gt 18 ] && [ $a -lt 35 ];then echo ok; fi
[user1@VM-4-6-centos scripts]$ echo $a
15
[user1@VM-4-6-centos scripts]$ a=25
[user1@VM-4-6-centos scripts]$ if [ $a -gt 18 ] && [ $a -lt 35 ];then echo ok; fi
ok
[user1@VM-4-6-centos scripts]$ a=20
[user1@VM-4-6-centos scripts]$ if [ $a -gt 18 ] && [ $a -lt 35 ];then echo ok; fi
ok
[user1@VM-4-6-centos scripts]$ 

```
***
#### if else 双分支

```shell
#!/bin/bash
if [ "$1"x = "user1"x1 ]
then 
	echo "welcome,user1"
fi

# 输入第二个参数，表示年龄，判断属于哪个年龄段
if [ $2 -lt 18 ]
then
	echo "未成年人"
else
	echo "成年人"
fi
```

```linux
[user1@VM-4-6-centos scripts]$ vim if_test.sh
[user1@VM-4-6-centos scripts]$ ./if_test.sh user1 15
未成年人
[user1@VM-4-6-centos scripts]$ ./if_test.sh user1 25
成年人
[user1@VM-4-6-centos scripts]$ 

```
***
####  if-elif-else-fi 多分支

```shell
#!/bin/bash
if [ "$1"x = "user1"x1 ]
then
		echo "welcome,user1"
fi

# 输入第二个参数，表示年龄，判断属于哪个年龄段
if [ $2 -lt 18 ] 
then
	echo "未成年人"
elif [ $2 -lt 35 ]
then
	echo "青年人"
elif [ $2 -lt 60 ]
then 
	echo "中年人"
else
	echo "老年人"
fi
```

```linux
[user1@VM-4-6-centos scripts]$ vim if_test.sh
[user1@VM-4-6-centos scripts]$ ./if_test.sh user1 15
未成年人
[user1@VM-4-6-centos scripts]$ ./if_test.sh user1 25
青年人
[user1@VM-4-6-centos scripts]$ ./if_test.sh user1 36
中年人
[user1@VM-4-6-centos scripts]$ ./if_test.sh user1 67
老年人
[user1@VM-4-6-centos scripts]$ 

```
***
### 6.2 case语句

1. 基本语法
```shell
case $变量名 in
"值1")
	如果变量的值等于值1.则执行程序1
;;
"值2")
	如果变量的值等于值2，则执行程序2
;;
	...省略其他分支
*）
	如果变量的值都不是以上的中，则执行此程序
;;
esac
```
注意事项：

 （1）case 行尾必须为单词“in”，每一个模式匹配必须以右括号“）”结束。 （2）双分号“;;”表示命令序列结束，相当于 java 中的 break。 

（3）最后的“*）”表示默认模式，相当于 java 中的 default。

2. 案例实操

```shell
#!/bin/bash

case $1 in
1)
	echo "one"
;;
2)
	echo "two"
;;
3)
	echo "three"
;;
*)
	echo "number else"
;;
esac
```

```linux
[user1@VM-4-6-centos scripts]$ vim case_test.sh
[user1@VM-4-6-centos scripts]$ chmod +x case_test.sh
[user1@VM-4-6-centos scripts]$ ./case_test.sh 2
two
[user1@VM-4-6-centos scripts]$ ./case_test.sh 3
three
[user1@VM-4-6-centos scripts]$ 

```
***
### 6.3 for循环

1. 基本语法
```shell
for ((初始值;循环控制条件;变量变化))
do
	程序
done
```
2. 案例实操
```shell
#!/bin/bash

for (( i=1; i <= $1; i++ ))
do 
	sum=$[ $sum + $i ]
done 
echo $sum
```

![image-20221104012005314](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104012005314.png)

双括号内能使用数学运算符

```linux
[user1@VM-4-6-centos scripts]$ vim sum_to.sh
[user1@VM-4-6-centos scripts]$ chmod +x sum_to.sh
[user1@VM-4-6-centos scripts]$ ./sum_to.sh 100
5050
[user1@VM-4-6-centos scripts]$ 
[user1@VM-4-6-centos scripts]$ a=3
[user1@VM-4-6-centos scripts]$ if (( $a > 2 )); then echo ok; else echo notok; fi
ok
[user1@VM-4-6-centos scripts]$ a=1
[user1@VM-4-6-centos scripts]$ if (( $a > 2 )); then echo ok; else echo notok; fi
notok
[user1@VM-4-6-centos scripts]$ 
```
***
3. 基本语法2

```shell
for 变量 in 值1 值2 值3 ...
do 
	程序
done
```
测试：
```linux
[user1@VM-4-6-centos scripts]$ for os in linux windows macos; do echo $os; done
linux
windows
macos
[user1@VM-4-6-centos scripts]$ for i in {1..100}; do sum=$[$sum+$i]; done; echo $sum
5050
[user1@VM-4-6-centos scripts]$ 

```
***
比较$*和$@区别 $*和$@都表示传递给函数或脚本的所有参数，不被双引号“”包含时，都以$1 $2 …$n 的形式输出所有参数

```shell
#!/bin/bash

echo '====$*====='
for para in $*
do 
	echo $para
done

echo '====$@===='
for para in $@
do 
	echo $para
done
```

```linux
[user1@VM-4-6-centos scripts]$ vim paramater_for_test.sh
[user1@VM-4-6-centos scripts]$ chmod +x paramater_for_test.sh
[user1@VM-4-6-centos scripts]$ ./paramater_for_test.sh  a b c d f
======$*========
a
b
c
d
f
======$@======
a
b
c
d
f
[user1@VM-4-6-centos scripts]$ 

```
***
当它们被双引号“”包含时，$*会将所有的参数作为一个整体，以“$1 $2 …$n”的形式输
出所有参数；$@会将各个参数分开，以“$1” “$2”…“$n”的形式输出所有参数

```shell
#!/bin/bash

echo '====$*======'
for para in "$*"
do 
	echo $para
done

echo '=====$@===='
for para in "$@"
do 
	echo $para
done
```


```linux
[user1@VM-4-6-centos scripts]$ vim  paramater_for_test.sh 
[user1@VM-4-6-centos scripts]$ ./paramater_for_test.sh  a b c d f
======$*========
a b c d f
======$@======
a
b
c
d
f
[user1@VM-4-6-centos scripts]$ 

```
***
###6.4 while循环

1. 基本语法
```shell
while [ 条件判断式 ]
do
	程序
done
```
```shell
#!/bin/bash

# 用for进行实现
for (( i=1; i<= $1; i++ ))
do
	sum=$[ $sum + $i ]
done
echo $sum

# 用while进行实现
a=1
while [ $a -le $1 ]
do 
	sum2=$[ $sum2 + $a ]
	a=$[$a + 1 ]
done
echo $sum2
```

```linux
[user1@VM-4-6-centos scripts]$ vim sum_to.sh
[user1@VM-4-6-centos scripts]$ ./sum_to.sh 100
5050
5050
[user1@VM-4-6-centos scripts]$ 
```
***
### let语法

```shell
#!/bin/bash

# 用for进行实现
for (( i=1; i<= $1; i++ ))
do
	sum=$[ $sum + $i ]
done
echo $sum

# 用while进行实现
a=1
while [ $a -le $1 ]
do 
#	sum2=$[ $sum2 + $a ]
#	a=$[$a + 1 ]
	let sum2+=a
	let a++
done
echo $sum2
```

```linux
[user1@VM-4-6-centos scripts]$ vim sum_to.sh
[user1@VM-4-6-centos scripts]$ ./sum_to.sh 100
5050
5050
[user1@VM-4-6-centos scripts]$ 

```

***

##第7章 read读取控制台输入

1. 基本语法
	
	read (选项) (参数) 
	
	①选项：
	
	 -p：指定读取值时的提示符； 
	
	-t：指定读取值时等待的时间（秒）如果-t 不加表示一直等待 
	
	②参数 
	
	变量：指定读取值的变量名
	
	```shell
	#!/bin/bash
	
	read -t 10 -p "请输入您的姓名：" name
	echo "welcome. $name"
	```

```linux
[user1@VM-4-6-centos scripts]$ vim read_test.sh
[user1@VM-4-6-centos scripts]$ chmod +x read_test.sh
[user1@VM-4-6-centos scripts]$ ./read_test.sh
请输入您的姓名：lwxfairy
welcome, lwxfairy
[user1@VM-4-6-centos scripts]$ ./read_test.sh
请输入您的姓名：welcome, 
[user1@VM-4-6-centos scripts]$ 

```

***

##第8章 函数

### 8.1 系统函数

#### 8.1.1 basename

1. 基本语法

   basename [string / pathname] [suffix] （功能描述：basename 命令会删掉所有的前 缀包括最后一个（‘/’）字符，然后将字符串显示出来。

    basename 可以理解为取路径里的文件名称

    选项： 

   suffix 为后缀，如果 suffix 被指定了，basename 会将 pathname 或 string 中的 suffix 去掉

![image-20221104021401401](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104021401401.png)




```shell
#!/bin/bash
filename="$1"_log_$(date +%s)
```

```linux
[user1@VM-4-6-centos scripts]$ date +%s
1667499211
[user1@VM-4-6-centos scripts]$ vim cmd_test.sh
[user1@VM-4-6-centos scripts]$ chmod +x cmd_test.sh
[user1@VM-4-6-centos scripts]$ ./cmd_test.sh lwxfairy
lwxfairy_log_1667499668
[user1@VM-4-6-centos scripts]$ basename /home/user1/paramater.sh
paramater.sh
[user1@VM-4-6-centos scripts]$ basename /home/uedf/safeeg
safeeg
[user1@VM-4-6-centos scripts]$ basename /home/user1/paramater.sh .sh
paramater
[user1@VM-4-6-centos scripts]$ 

```

![image-20221104022938858](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104022938858.png)

***

#### 8.1.2 dirname

1. 基本语法

   dirname 文件绝对路径 （功能描述：从给定的包含绝对路径的文件名中去除文件名 （非目录的部分），然后返回剩下的路径（目录的部分）） 

   dirname 可以理解为取文件路径的绝对路径名称

​	命令替换：$(  )

```linux
[user1@VM-4-6-centos scripts]$ dirname /home/scripts/parameter.sh
/home/scripts
[user1@VM-4-6-centos scripts]$ dirname ../scripts/parameter.sh
../scripts
[user1@VM-4-6-centos scripts]$ dirname ../scris/parater.sh
../scris
[user1@VM-4-6-centos scripts]$ 

```

![image-20221104023924992](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104023924992.png)

```linux
[user1@VM-4-6-centos scripts]$ vim paramater.sh
[user1@VM-4-6-centos scripts]$ ./paramater.sh
=====$0=====
script name: paramater
script path: /home/user1/scripts
1st paramater:
2nd paramater:
======$#=====
paramater numbers: 0
=====$*======

=====$@=====

[user1@VM-4-6-centos scripts]$ 

```
***

### 8.2 自定义函数

1. 基本语法

   [ function ] funname[()] 

   { 

   Action; 

   [return int;] 

   }
   
2. 经验技巧

   （1）必须在调用函数地方之前，先声明函数，shell 脚本是逐行运行。不会像其它语言一 样先编译。 

   （2）函数返回值，只能通过$?系统变量获得，可以显示加：return 返回，如果不加，将 以最后一条命令运行结果，作为返回值。return 后跟数值 n(0-255)

```shell
#!/bin/bash

function add(){
	s=$[$1 + $2]
	echo "和： "$s
}
read -p "请输入第一个整数： " a
read -p "请输入第二个整数： " b

add $a $b
```


```linux
[user1@VM-4-6-centos scripts]$ vim fun_test.sh
[user1@VM-4-6-centos scripts]$ chmod +x fun_test.sh
[user1@VM-4-6-centos scripts]$ ./fun_test.sh
请输入第一个整数：35
请输入第二个整数：45
和： 80
[user1@VM-4-6-centos scripts]$ 

```
```shell
#!/bin/bash

function add(){
	s=$[$1 +$2]
	echo $2
}
read -p "请输入第一个整数： " a
read -p "请输入第二个整数： " b

sum=$(add $a $b)
echo "和： "$sum
echo "和的平方： "$[$sum * $sum]
```
```linux
[user1@VM-4-6-centos scripts]$ vim fun_test.sh
[user1@VM-4-6-centos scripts]$ ./fun_test.sh
请输入第一个整数：156
请输入第二个整数：237
和: 393
和的平方：154449
[user1@VM-4-6-centos scripts]$ 

```

***

##第9章 正则表达式

正则表达式使用单个字符串来描述、匹配一系列符合某个语法规则的字符串。在很多文 本编辑器里，正则表达式通常被用来检索、替换那些符合某个模式的文本。在 Linux 中，grep， sed，awk 等文本处理工具都支持通过正则表达式进行模式匹配。

### 9.1 常规匹配

一串不包含特殊字符的正则表达式匹配它自己，例如： 

```linux
[lwxfairy@hadoop101 shells]$ cat /etc/passwd | grep atguigu 
```

就会匹配所有包含 atguigu 的行

***

### 9.2 常用特殊字符

1）特殊字符：^ 

^ 匹配一行的开头，例如：

```linux
 [lwxfairy@hadoop101 shells]$ cat /etc/passwd | grep ^a 
```

会匹配出所有以 a 开头的行

2）特殊字符：$

 $ 匹配一行的结束，例如 

```linux
[lwxfairy@hadoop101 shells]$ cat /etc/passwd | grep t$ 
```

会匹配出所有以 t 结尾的行 思考：^$ 匹配什么？ 

3）特殊字符：.

 . 匹配一个任意的字符，例如 

```lnux
[alwxfairy@hadoop101 shells]$ cat /etc/passwd | grep r..t 
```

会匹配包含 rabt,rbbt,rxdt,root 等的所有行 

4）特殊字符：* 

\* 不单独使用，他和上一个字符连用，表示匹配上一个字符 0 次或多次，例如

```linux
 [lwxfairy@hadoop101 shells]$ cat /etc/passwd | grep ro*t 
```

会匹配 rt, rot, root, rooot, roooot 等所有行

思考：.* 匹配什么？

 5）字符区间（中括号）：[ ]

 [ ] 表示匹配某个范围内的一个字符，例如 

[6,8]------匹配 6 或者 8

 [0-9]------匹配一个 0-9 的数字

 [0-9]\*------匹配任意长度的数字字符串 

[a-z]------匹配一个 a-z 之间的字符 

[a-z]* ------匹配任意长度的字母字符串 

[a-c, e-f]-匹配 a-c 或者 e-f 之间的任意字符

```linux
 [lwxfairy@hadoop101 shells]$ cat /etc/passwd | grep r[a,b,c]*t 
```

会匹配 rt,rat, rbt, rabt, rbact,rabccbaaacbt 等等所有行 

6）特殊字符：\

 \ 表示转义，并不会单独使用。由于所有特殊字符都有其特定匹配模式，当我们想匹配 某一特殊字符本身时（例如，我想找出所有包含 '$' 的行），就会碰到困难。此时我们就要 将转义字符和特殊字符连用，来表示特殊字符本身，例如

```linux
 [lwxfairy@hadoop101 shells]$ cat /etc/passwd | grep ‘a\$b’ 
```

就会匹配所有包含 a$b 的行。注意需要使用单引号将表达式引起来。

***
测试
```linux
[root@hadoop100 ~]# cat /etc/passwd |grep lwxfairy
lwxfairy:x:1000:1000:lwxfairy:/home/lwxfairy:/bin/bash
[root@hadoop100 ~]# cat /etc/passwd |grep 100
games:x:12:100:games:/usr/games:/sbin/nologin
lwxfairy:x:1000:1000:lwxfairy:/home/lwxfairy:/bin/bash
[root@hadoop100 ~]# cat /etc/passwd |grep ^lwxfairy$
[root@hadoop100 ~]# cat /etc/passwd |grep ^$
[root@hadoop100 ~]# vim daily-archive.sh
[root@hadoop100 ~]# cat daily-archive.sh | grep ^$











[root@hadoop100 ~]# cat daily-archive.sh | grep -n  ^$
6:
17:
20:
23:
27:
29:
32:
34:
45:
47:
48:
[root@hadoop100 ~]# cat /etc/passwd |grep r..t
root:x:0:0:root:/root:/bin/bash
operator:x:11:0:operator:/root:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
[root@hadoop100 ~]# cat /etc/passwd |grep r.t
operator:x:11:0:operator:/root:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
[root@hadoop100 ~]# cat /etc/passwd |grep r...t
rtkit:x:172:172:RealtimeKit:/proc:/sbin/nologin
unbound:x:991:986:Unbound DNS resolver:/etc/unbound:/sbin/nologin
[root@hadoop100 ~]# cat /etc/passwd |grep ^l.*bash$
lwxfairy:x:1000:1000:lwxfairy:/home/lwxfairy:/bin/bash
lihua:x:1001:1001::/home/lihua:/bin/bash
liming:x:1002:1001::/home/liming:/bin/bash
[root@hadoop100 ~]# cat /etc/passwd |grep ^l.*in$
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
libstoragemgmt:x:998:995:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
[root@hadoop100 ~]# cat /etc/passwd |grep ^l.*var.*in$
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
libstoragemgmt:x:998:995:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
[root@hadoop100 ~]# 

```



![image-20221104113610934](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104113610934.png)

![image-20221104113742211](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104113742211.png)

![image-20221104112407298](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104112407298.png)

```linux
[root@hadoop100 ~]# cat /etc/passwd |grep r[a,b]t
operator:x:11:0:operator:/root:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
[root@hadoop100 ~]# echo "ratbrddfd" |grep r[a,b]t
ratbrddfd
[root@hadoop100 ~]# echo "3558ratbrddfd" |grep r[a,b]t
3558ratbrddfd
[root@hadoop100 ~]# echo "3558ratbrddfd" |grep r[ab]t
3558ratbrddfd
[root@hadoop100 ~]# echo "3558ratbrdaaadfd" |grep r[ab]*t
3558ratbrdaaadfd
[root@hadoop100 ~]# echo "3558raaabbbtbrdaaadfd" |grep r[ab]*t
3558raaabbbtbrdaaadfd
[root@hadoop100 ~]# echo "3558raaabbbtbrdaaadfd" |grep r[a-z]*t
3558raaabbbtbrdaaadfd
[root@hadoop100 ~]# cat /etc/passwd |grep r[a-z]*t
root:x:0:0:root:/root:/bin/bash
operator:x:11:0:operator:/root:/sbin/nologin
libstoragemgmt:x:998:995:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
setroubleshoot:x:993:990::/var/lib/setroubleshoot:/sbin/nologin
rtkit:x:172:172:RealtimeKit:/proc:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin

```

![image-20221104113458646](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104113458646.png)

```linux
[root@hadoop100 ~]# cat daily-archive.sh 
f [ $# -ne 1 ]
then
        echo "参数个数错误！应该输入一个参数，作为归档目录名"
        exit
fi

# 从参数中获取目录名称
if [ -d $1 ]
then
        echo 
else
        echo
        echo "目录不存在!"
        echo 
        exit
fi

DIR_NAME=$(basename $1)
DIR_PATH=$(cd $(dirname $1); pwd)

# 获取当前日期
DATE=$(date +%y%m%d)

# 定义生成的归档文件名称
FALE=archive_${DIR_NAME}_$DATE.tar.gz
DEST=/home/archive/$FALE

# 开始归档目录文件

echo "开始归档..."
echo

tar -czf $DAST  $DIR_PATH/$DIR_NAME

if [ $? -eq 0 ]
then
        echo
        echo "归档成功!"
        echo "归档文件为：$DEST"
        echo
else
        echo "归档出现问题！"
        echo
fi

exit


[root@hadoop100 ~]# cat daily-archive.sh | grep '\$'
f [ $# -ne 1 ]
if [ -d $1 ]
DIR_NAME=$(basename $1)
DIR_PATH=$(cd $(dirname $1); pwd)
DATE=$(date +%y%m%d)
FALE=archive_${DIR_NAME}_$DATE.tar.gz
DEST=/home/archive/$FALE
tar -czf $DAST  $DIR_PATH/$DIR_NAME
if [ $? -eq 0 ]
        echo "归档文件为：$DEST"
[root@hadoop100 ~]# cat daily-archive.sh | grep '/\$'
DEST=/home/archive/$FALE
tar -czf $DAST  $DIR_PATH/$DIR_NAME

```

![image-20221104115549420](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104115549420.png)



手机号的正则表达式

```linux
[root@hadoop100 ~]# echo "18425686858" | grep -E ^1[34578][0-9]{9}$
18425686858

```

***

##第10章 文本处理工具

 ### 10.1 cut

cut 的工作就是“剪”，具体的说就是在文件中负责剪切数据用的。cut 命令从文件的每 一行剪切字节、字符和字段并将这些字节、字符和字段输出

1. 基本用法

   cut [选项参数] filename 说明：默认分隔符是制表符

2. 选项参数说明

​	

| 选项参数 | 功能                                           |
| -------- | ---------------------------------------------- |
| -f       | 列号，提取第几列                               |
| -d       | 分隔符，按照指定分隔符分割列，默认是制表符"\t" |
| -c       | 按字符进行切割 后加加n表示取第几列 比如 -c 1   |

***
3. 案例实操
   （1）数据准备
   
   ```linux
    [lwxfairy@hadoop101 shells]$ touch cut.txt [atguigu@hadoop101 shells]$ vim cut.txt dong shen guan zhen wo wo lai lai le le
   ```
   
   （2）切割 cut.txt 第一列 
   
   ```linux
   [lwxfairy@hadoop101 shells]$ cut -d " " -f 1 cut.txt dong guan wo lai le 
   ```
   
   （3）切割 cut.txt 第二、三列
   
   ```linux
    [lwxfairy@hadoop101 shells]$ cut -d " " -f 2,3 cut.txt shen zhen wo lai le
   ```
   
   （4）在 cut.txt 文件中切割出guan
   
   ```linux
    [lwxfairy@hadoop101 shells]$ cat cut.txt |grep guan | cut -d " " -f 1 guan
   ```
   
   
   
   （5）选取系统 PATH 变量值，第 2 个“：”开始后的所有路径： 

```linux
[lwxfairy@hadoop101 shells]$ echo $PATH /usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/atguigu/.local/bin:/ home/atguigu/bin
```
***
测试：
```linux
dong shen
guan zhen
wo wo
lai lai
le lei

```

```linux
[root@hadoop100 ~]# touch cut.txt
[root@hadoop100 ~]# vim cut.txt
[root@hadoop100 ~]# cat cut.txt
dong shen
guan zhen
wo   wo 
lai  lai
le   lei
[root@hadoop100 ~]# vim cut.txt
[root@hadoop100 ~]# cut -d " " -f 1 cut.txt
dong
guan
wo
lai
le
[root@hadoop100 ~]# cut -d " " -f 2,3 cut.txt
shen
zhen
wo 
lai
lei
[root@hadoop100 ~]# cat /etc/passwd |grep bash$
root:x:0:0:root:/root:/bin/bash
lwxfairy:x:1000:1000:lwxfairy:/home/lwxfairy:/bin/bash
lihua:x:1001:1001::/home/lihua:/bin/bash
liming:x:1002:1001::/home/liming:/bin/bash
xiaohong:x:1003:1002::/home/xiaohong:/bin/bash
xiaozhang:x:1004:1001::/home/xiaozhang:/bin/bash
[root@hadoop100 ~]# cat /etc/passwd |grep bash$ |cut -d ":" -f 1,6,7
root:/root:/bin/bash
lwxfairy:/home/lwxfairy:/bin/bash
lihua:/home/lihua:/bin/bash
liming:/home/liming:/bin/bash
xiaohong:/home/xiaohong:/bin/bash
xiaozhang:/home/xiaozhang:/bin/bash
[root@hadoop100 ~]# cat /etc/passwd |grep bash$ |cut -d ":" -f 1-4
root:x:0:0
lwxfairy:x:1000:1000
lihua:x:1001:1001
liming:x:1002:1001
xiaohong:x:1003:1002
xiaozhang:x:1004:1001
[root@hadoop100 ~]# cat /etc/passwd |grep bash$ |cut -d ":" -f 4-
0:root:/root:/bin/bash
1000:lwxfairy:/home/lwxfairy:/bin/bash
1001::/home/lihua:/bin/bash
1001::/home/liming:/bin/bash
1002::/home/xiaohong:/bin/bash
1001::/home/xiaozhang:/bin/bash
[root@hadoop100 ~]# cat /etc/passwd |grep bash$ |cut -d ":" -f -4
root:x:0:0
lwxfairy:x:1000:1000
lihua:x:1001:1001
liming:x:1002:1001
xiaohong:x:1003:1002
xiaozhang:x:1004:1001
[root@hadoop100 ~]# echo $PATH
/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:/root/bin
[root@hadoop100 ~]# echo $PATH | cut -d ":" -f 2-
/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:/root/bin
[root@hadoop100 ~]# echo $PATH | cut -d ":" -f 3-
/usr/bin:/usr/sbin:/bin:/sbin:/root/bin
[root@hadoop100 ~]# 

```

![image-20221104122806111](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104122806111.png)

#### 截取IP

```linux
[user1@VM-4-6-centos ~]$ ifconfig
cni0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet 10.42.0.1  netmask 255.255.255.0  broadcast 10.42.0.255
        inet6 fe80::c064:9aff:fe1b:1bd4  prefixlen 64  scopeid 0x20<link>
        ether c2:64:9a:1b:1b:d4  txqueuelen 1000  (Ethernet)
        RX packets 1811780  bytes 397655252 (379.2 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2076809  bytes 239551255 (228.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 0.0.0.0
        inet6 fe80::42:9ff:fe9b:ae1  prefixlen 64  scopeid 0x20<link>
        ether 02:42:09:9b:0a:e1  txqueuelen 0  (Ethernet)
        RX packets 31793  bytes 72963046 (69.5 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 18425  bytes 1640372 (1.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.4.6  netmask 255.255.252.0  broadcast 10.0.7.255
        inet6 fe80::5054:ff:fe54:701d  prefixlen 64  scopeid 0x20<link>
        ether 52:54:00:54:70:1d  txqueuelen 1000  (Ethernet)
        RX packets 817897  bytes 187593165 (178.9 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 787398  bytes 206203632 (196.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

flannel.1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet 10.42.0.0  netmask 255.255.255.255  broadcast 0.0.0.0
        inet6 fe80::8c3a:baff:fe25:bbff  prefixlen 64  scopeid 0x20<link>
        ether 8e:3a:ba:25:bb:ff  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 5 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1857661  bytes 577372060 (550.6 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1857661  bytes 577372060 (550.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth10c0b96f: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet6 fe80::60c5:c0ff:fe10:e18b  prefixlen 64  scopeid 0x20<link>
        ether 62:c5:c0:10:e1:8b  txqueuelen 0  (Ethernet)
        RX packets 13706  bytes 1019095 (995.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 12688  bytes 851426 (831.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth23e019ae: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet6 fe80::e06b:dcff:fe17:b807  prefixlen 64  scopeid 0x20<link>
        ether e2:6b:dc:17:b8:07  txqueuelen 0  (Ethernet)
        RX packets 196079  bytes 20836871 (19.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 193596  bytes 18360298 (17.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth89b12640: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet6 fe80::dc28:43ff:fe29:1fc1  prefixlen 64  scopeid 0x20<link>
        ether de:28:43:29:1f:c1  txqueuelen 0  (Ethernet)
        RX packets 1112489  bytes 354607728 (338.1 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1384073  bytes 176886442 (168.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth94d9e0cc: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet6 fe80::7493:f1ff:feab:787a  prefixlen 64  scopeid 0x20<link>
        ether 76:93:f1:ab:78:7a  txqueuelen 0  (Ethernet)
        RX packets 489584  bytes 46569562 (44.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 486777  bytes 43482727 (41.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

vethd899316: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::80b2:9fff:feb5:dca8  prefixlen 64  scopeid 0x20<link>
        ether 82:b2:9f:b5:dc:a8  txqueuelen 0  (Ethernet)
        RX packets 29039  bytes 66728026 (63.6 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 16964  bytes 1528869 (1.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

vethf65082ce: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet6 fe80::e014:b9ff:fe2b:1e2b  prefixlen 64  scopeid 0x20<link>
        ether e2:14:b9:2b:1e:2b  txqueuelen 0  (Ethernet)
        RX packets 8  bytes 612 (612.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 17  bytes 1226 (1.1 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

[user1@VM-4-6-centos ~]$ ifconfig ens33
ens33: error fetching interface information: Device not found
[user1@VM-4-6-centos ~]$ ifconfig cni0
cni0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1450
        inet 10.42.0.1  netmask 255.255.255.0  broadcast 10.42.0.255
        inet6 fe80::c064:9aff:fe1b:1bd4  prefixlen 64  scopeid 0x20<link>
        ether c2:64:9a:1b:1b:d4  txqueuelen 1000  (Ethernet)
        RX packets 1812443  bytes 397808499 (379.3 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2077573  bytes 239638280 (228.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

[user1@VM-4-6-centos ~]$ ifconfig cni0 | grep netmask
        inet 10.42.0.1  netmask 255.255.255.0  broadcast 10.42.0.255
[user1@VM-4-6-centos ~]$ ifconfig cni0 | grep netmask | cut -d " " -f 10
10.42.0.1
[user1@VM-4-6-centos ~]$ ifconfig | grep netmask | cut -d " " -f 10
10.42.0.1
172.17.0.1
10.0.4.6
10.42.0.0
127.0.0.1
[user1@VM-4-6-centos ~]$ 

```
***
###10.2 awk

一个强大的文本分析工具，把文件逐行的读入，以空格为默认分隔符将每行切片，切开 的部分再进行分析处理

1. 基本用法

   awk [选项参数] ‘/pattern1/{action1} /pattern2/{action2}...’ filename pattern：表示 awk 在数据中查找的内容，就是匹配模式 

   action：在找到匹配内容时所执行的一系列命令

2. 选项参数说明

   | 选项参数 | 功能                 |
   | -------- | -------------------- |
   | -F       | 指定输入文件分割符   |
   | -v       | 赋值一个用户定义变量 |

3. 案例实操

   （1）数据准备

   ```linux
    [lwxfairy@hadoop101 shells]$ sudo cp /etc/passwd ./ 
   ```

   passwd 数据的含义 用户名:密码(加密过后的):用户 id:组 id:注释:用户家目录:shell 解析器 

   （2）搜索 passwd 文件以 root 关键字开头的所有行，并输出该行的第 7 列。

   ```linux
    [lwxfairy@hadoop101 shells]$ awk -F : '/^root/{print $7}' passwd /bin/bash 
   ```

   （3）搜索 passwd 文件以 root 关键字开头的所有行，并输出该行的第 1 列和第 7 列， 中间以“，”号分割。 

   ```linux
   [lwxfairy@hadoop101 shells]$ awk -F : '/^root/{print $1","$7}' passwd root,/bin/bash
   ```

    注意：只有匹配了 pattern 的行才会执行 action。 

   （4）只显示/etc/passwd 的第一列和第七列，以逗号分割，且在所有行前面添加列名 user， shell 在最后一行添加"dahaige，/bin/zuishuai"。 

   ```linux
   [lwxfairy@hadoop101 shells]$ awk -F : 'BEGIN{print "user, shell"} {print $1","$7} END{print "dahaige,/bin/zuishuai"}' passwd user, shell root,/bin/bash bin,/sbin/nologin 。。。 atguigu,/bin/bash dahaige,/bin/zuishuai 
   ```
   注意：BEGIN 在所有数据读取行之前执行；END 在所有数据执行之后执行。
   
   （5）将 passwd 文件中的用户 id 增加数值 1 并输出 
   
   ```linux
   [lwxfairy@hadoop101 shells]$ awk -v i=1 -F : '{print $3+i}' passwd 1 2 3
   ```
   
   ***
   测试
```linux
[root@hadoop100 ~]# cat /etc/passwd | grep ^root | cut -d ":" -f 7
/bin/bash
[root@hadoop100 ~]# cat /etc/passwd | awk -F ":" '/^root/ {print $7}'
/bin/bash
[root@hadoop100 ~]# cat /etc/passwd | grep ^root | cut -d ":" -f 1,6,7
root:/root:/bin/bash
[root@hadoop100 ~]# cat /etc/passwd | awk -F ":" '/^root/ {print $1","$6","$7}'
root,/root,/bin/bash
[root@hadoop100 ~]# cat /etc/passwd | awk -F ":" 'BEGIN{print "user ,shell"}{print $1","$6","$7} END{print "end of file"}'
user ,shell
root,/root,/bin/bash
bin,/bin,/sbin/nologin
daemon,/sbin,/sbin/nologin
adm,/var/adm,/sbin/nologin
lp,/var/spool/lpd,/sbin/nologin
sync,/sbin,/bin/sync
shutdown,/sbin,/sbin/shutdown
halt,/sbin,/sbin/halt
mail,/var/spool/mail,/sbin/nologin
operator,/root,/sbin/nologin
games,/usr/games,/sbin/nologin
ftp,/var/ftp,/sbin/nologin
nobody,/,/sbin/nologin
systemd-network,/,/sbin/nologin
dbus,/,/sbin/nologin
polkitd,/,/sbin/nologin
libstoragemgmt,/var/run/lsm,/sbin/nologin
colord,/var/lib/colord,/sbin/nologin
rpc,/var/lib/rpcbind,/sbin/nologin
saned,/usr/share/sane,/sbin/nologin
gluster,/run/gluster,/sbin/nologin
saslauth,/run/saslauthd,/sbin/nologin
abrt,/etc/abrt,/sbin/nologin
setroubleshoot,/var/lib/setroubleshoot,/sbin/nologin
rtkit,/proc,/sbin/nologin
pulse,/var/run/pulse,/sbin/nologin
radvd,/,/sbin/nologin
chrony,/var/lib/chrony,/sbin/nologin
unbound,/etc/unbound,/sbin/nologin
qemu,/,/sbin/nologin
tss,/dev/null,/sbin/nologin
sssd,/,/sbin/nologin
usbmuxd,/,/sbin/nologin
geoclue,/var/lib/geoclue,/sbin/nologin
ntp,/etc/ntp,/sbin/nologin
gdm,/var/lib/gdm,/sbin/nologin
rpcuser,/var/lib/nfs,/sbin/nologin
nfsnobody,/var/lib/nfs,/sbin/nologin
gnome-initial-setup,/run/gnome-initial-setup/,/sbin/nologin
sshd,/var/empty/sshd,/sbin/nologin
avahi,/var/run/avahi-daemon,/sbin/nologin
postfix,/var/spool/postfix,/sbin/nologin
tcpdump,/,/sbin/nologin
lwxfairy,/home/lwxfairy,/bin/bash
lihua,/home/lihua,/bin/bash
liming,/home/liming,/bin/bash
xiaohong,/home/xiaohong,/bin/bash
xiaozhang,/home/xiaozhang,/bin/bash
end of file
[root@hadoop100 ~]# 
```

```linux
[root@hadoop100 ~]# cat /etc/passwd | awk -F ":" '{print $3}'
0
1
2
3
4
5
6
7
8
11
12
14
99
192
81
999
998
997
32
996
995
994
173
993
172
171
75
992
991
107
59
990
113
989
38
42
29
65534
988
74
70
89
72
1000
1001
1002
1003
1004
[root@hadoop100 ~]# cat /etc/passwd | awk -F ":" '{print $3+1}'
1
2
3
4
5
6
7
8
9
12
13
15
100
193
82
1000
999
998
33
997
996
995
174
994
173
172
76
993
992
108
60
991
114
990
39
43
30
65535
989
75
71
90
73
1001
1002
1003
1004
1005
[root@hadoop100 ~]# 
```

引入一个参数

```linux
[root@hadoop100 ~]# cat /etc/passwd | awk -v i=1 -F ":" '{print $3+i}'
1
2
3
4
5
6
7
8
9
12
13
15
100
193
82
1000
999
998
33
997
996
995
174
994
173
172
76
993
992
108
60
991
114
990
39
43
30
65535
989
75
71
90
73
1001
1002
1003
1004
1005
[root@hadoop100 ~]# 

```
***
4. awk的内置变量

  | 变量     | 说明                                   |
  | -------- | -------------------------------------- |
  | FILENAME | 文件名                                 |
  | NR       | 已读的记录数（行号）                   |
  | NF       | 浏览记录的域的个数（切割后，列的个数） |

5. 案例实操

   （1）统计 passwd 文件名，每行的行号，每行的列数 

   ```linux
   [lwxfairy@hadoop101 shells]$ awk -F : '{print "filename:" FILENAME ",linenum:" NR ",col:"NF}' passwd filename:passwd,linenum:1,col:7 filename:passwd,linenum:2,col:7 filename:passwd,linenum:3,col:7 ... 
   ```

   （2）查询 ifconfig 命令输出结果中的空行所在的行号 

   ```linux
   [lwxfairy@hadoop101 shells]$ ifconfig | awk '/^$/{print NR}' 9 18 26 
   ```

   （3）切割 IP

   ```linux
    [lwxfairy@hadoop101 shells]$ ifconfig ens33 | awk '/netmask/ {print $2}' 192.168.6.101
   ```
   ***
测试
```linux
[root@hadoop100 ~]#  awk -F ":" '{print "文件名："FILENAME " 行号: "NR " 列数："NF}' /etc/passwd
文件名：/etc/passwd 行号: 1 列数：7
文件名：/etc/passwd 行号: 2 列数：7
文件名：/etc/passwd 行号: 3 列数：7
文件名：/etc/passwd 行号: 4 列数：7
文件名：/etc/passwd 行号: 5 列数：7
文件名：/etc/passwd 行号: 6 列数：7
文件名：/etc/passwd 行号: 7 列数：7
文件名：/etc/passwd 行号: 8 列数：7
文件名：/etc/passwd 行号: 9 列数：7
文件名：/etc/passwd 行号: 10 列数：7
文件名：/etc/passwd 行号: 11 列数：7
文件名：/etc/passwd 行号: 12 列数：7
文件名：/etc/passwd 行号: 13 列数：7
文件名：/etc/passwd 行号: 14 列数：7
文件名：/etc/passwd 行号: 15 列数：7
文件名：/etc/passwd 行号: 16 列数：7
文件名：/etc/passwd 行号: 17 列数：7
文件名：/etc/passwd 行号: 18 列数：7
文件名：/etc/passwd 行号: 19 列数：7
文件名：/etc/passwd 行号: 20 列数：7
文件名：/etc/passwd 行号: 21 列数：7
文件名：/etc/passwd 行号: 22 列数：7
文件名：/etc/passwd 行号: 23 列数：7
文件名：/etc/passwd 行号: 24 列数：7
文件名：/etc/passwd 行号: 25 列数：7
文件名：/etc/passwd 行号: 26 列数：7
文件名：/etc/passwd 行号: 27 列数：7
文件名：/etc/passwd 行号: 28 列数：7
文件名：/etc/passwd 行号: 29 列数：7
文件名：/etc/passwd 行号: 30 列数：7
文件名：/etc/passwd 行号: 31 列数：7
文件名：/etc/passwd 行号: 32 列数：7
文件名：/etc/passwd 行号: 33 列数：7
文件名：/etc/passwd 行号: 34 列数：7
文件名：/etc/passwd 行号: 35 列数：7
文件名：/etc/passwd 行号: 36 列数：7
文件名：/etc/passwd 行号: 37 列数：7
文件名：/etc/passwd 行号: 38 列数：7
文件名：/etc/passwd 行号: 39 列数：7
文件名：/etc/passwd 行号: 40 列数：7
文件名：/etc/passwd 行号: 41 列数：7
文件名：/etc/passwd 行号: 42 列数：7
文件名：/etc/passwd 行号: 43 列数：7
文件名：/etc/passwd 行号: 44 列数：7
文件名：/etc/passwd 行号: 45 列数：7
文件名：/etc/passwd 行号: 46 列数：7
文件名：/etc/passwd 行号: 47 列数：7
文件名：/etc/passwd 行号: 48 列数：7
[root@hadoop100 ~]# 

```

```linux
[root@hadoop100 ~]# ifconfig | grep -n ^$
7:
16:
24:
[root@hadoop100 ~]# ifconfig | awk '/^$/ {print NR}'
7
16
24
[root@hadoop100 ~]# ifconfig | awk '/^$/ {print "空行:" NR}'
空行:8
空行:17
空行:25
[root@hadoop100 ~]# 

```

#### 切割ip

```linux
[user1@VM-4-6-centos ~]$ ifconfig cni0 |grep netmask |cut -d " " -f 10
10.42.0.1
[user1@VM-4-6-centos ~]$ ifconfig  |grep netmask |cut -d " " -f 10
10.42.0.1
172.17.0.1
10.0.4.6
10.42.0.0
127.0.0.1
[user1@VM-4-6-centos ~]$ ifconfig cni0 | awk '/netmask/ {print $2}'
10.42.0.1

```

##  第11章 综合应用案例

### 11.1 归档文件

实际生产应用中，往往需要对重要数据进行归档备份。 需求：实现一个每天对指定目录归档备份的脚本，输入一个目录名称（末尾不带/）， 将目录下所有文件按天归档保存，并将归档日期附加在归档文件名上，放在/root/archive 下。 这里用到了归档命令：tar 后面可以加上-c 选项表示归档，加上-z 选项表示同时进行压缩，得到的文件后缀名 为.tar.gz。 脚本实现如下：

```shell
#!/bin/bash

# 首先判断输入参数个数是否为1
if [ $# -ne 1 ]
then
        echo "参数个数错误！应该输入一个参数，作为归档目录名"
        exit
fi

# 从参数中获取目录名称
if [ -d $1 ]
then
        echo 
else
        echo
        echo "目录不存在!"
        echo 
        exit
fi

DIR_NAME=$(basename $1)
DIR_PATH=$(cd $(dirname $1); pwd)

# 获取当前日期
DATE=$(date +%y%m%d)

# 定义生成的归档文件名称
FALE=archive_${DIR_NAME}_$DATE.tar.gz
DEST=/home/archive/$FALE

# 开始归档目录文件

echo "开始归档..."
echo

tar -czf $DAST  $DIR_PATH/$DIR_NAME

if [ $? -eq 0 ]
then
        echo
        echo "归档成功!"
        echo "归档文件为：$DEST"
        echo
else
        echo "归档出现问题！"
        echo
fi

exit


```

linux cd 进入目录出现 no such file or directory的原因是把路径弄错了

1. 如果要进scripts目录，则直接cd scripts
2. 用正确路径 cd /home /yy/scripts 
3. 因为根目录下没有scripts，所以 cd /sctipts会遇到这个报错 

```linux
[user1@VM-4-6-centos ~]$ cd /scripts
-bash: cd: /scripts: No such file or directory
[user1@VM-4-6-centos ~]$ cd scripts
[user1@VM-4-6-centos scripts]$ ll
total 40
-rwxrwxr-x 1 user1 user1  41 Nov  3 23:08 add.sh
-rwxrwxr-x 1 user1 user1 111 Nov  4 01:11 case_test.sh
-rwxrwxr-x 1 user1 user1  58 Nov  4 02:19 cmd_test.sh
-rwxrwxr-x 1 user1 user1 208 Nov  4 02:59 fun_test.sh
-rwxrwxr-x 1 user1 user1 103 Nov  3 22:36 hello.sh
-rwxrwxr-x 1 user1 user1 290 Nov  4 01:03 if_test.sh
-rwxrwxr-x 1 user1 user1 135 Nov  4 01:44 paramater_for_test.sh
-rwxrwxr-x 1 user1 user1 262 Nov  4 02:39 paramater.sh
-rwxrwxr-x 1 user1 user1  81 Nov  4 02:09 read_test.sh
-rwxrwxr-x 1 user1 user1 227 Nov  4 01:57 sum_to.sh
-rw-rw-r-- 1 user1 user1   0 Nov  3 23:46 test
[user1@VM-4-6-centos scripts]$ 

```

![image-20221104105323741](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104105323741.png)

![image-20221104105357909](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104105357909.png)
***
### 11.2 发送消息
我们可以利用 Linux 自带的 mesg 和 write 工具，向其它用户发送消息。
需求：实现一个向某个用户快速发送消息的脚本，输入用户名作为第一个参数，后面直
接跟要发送的消息。脚本需要检测用户是否登录在系统中、是否打开消息功能，以及当前发
送消息是否为空。
脚本实现如下

```shell
#!/bin/bash

# 查看用户是否登录
login_user=$(who | grep -i -m 1 $1 |awk '{print $1}')

if [-z $login_user ]
then
        echo "$1 不在线！ "
        echo "脚本退出..."
        exit
fi

# 查看用户是否开启消息功能
is_allowed=$(who -T | grep -i -m 1 $1 | awk '{print $2}')

if [ $is_allowed != "+" ]
then
        echo "$1 没用开启消息功能"
        echo "脚本退出"
        exit
fi

# 确认是否有消息发送
if [ -z $2 ]
then
        echo "没有消息发送"
        echo "脚本退出"
        exit
fi

# 从参数中过去要发送的消息
whole_msg=$(echo $* | cut -d " " -f 2-)

# 获取用户登录的终端
user_terminal=$(who | grep -i -m 1 $1 | awk '{print $2}'

# 写入要发送的消息
echo $whole_msg | wirte $login_user $user_terminal

if [ $? !=0 ]
then
        echo "发送失败"
else
        echo "发送成功"
fi

exit
~                  
```

```linux
[user1@VM-4-6-centos ~]$ who
user1    pts/1        2022-11-04 19:48 (223.104.71.226)
root     pts/2        2022-11-04 19:29 (219.140.88.72)
[user1@VM-4-6-centos ~]$ mesg 
is y
[user1@VM-4-6-centos ~]$ who -T
user1    + pts/1        2022-11-04 19:48 (223.104.71.226)
root     + pts/2        2022-11-04 19:29 (219.140.88.72)
[user1@VM-4-6-centos ~]$ mesg n
[user1@VM-4-6-centos ~]$ who -t
[user1@VM-4-6-centos ~]$ who -T
user1    - pts/1        2022-11-04 19:48 (223.104.71.226)
root     + pts/2        2022-11-04 19:29 (219.140.88.72)
[user1@VM-4-6-centos ~]$ mesg y
[user1@VM-4-6-centos ~]$ who -T
user1    + pts/1        2022-11-04 19:48 (223.104.71.226)
root     + pts/2        2022-11-04 19:29 (219.140.88.72)
[user1@VM-4-6-centos ~]$ write root pts/2 
test

```

![image-20221104202415490](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221104202415490.png)
