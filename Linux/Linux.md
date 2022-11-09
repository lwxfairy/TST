# Linux

返回图形化界面的快捷键为：ctrl+alt+f1

进入控制台界面的快捷键为：ctrl+alt+f2-f6

中文拼音切换快捷键：win+空格 

 tab键能自动补全

退出文件 : q

![image-20221031165114705](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031165114705.png)

按键u能回退编辑之前（撤销）

：w  是写入（保存）

![image-20221031165733356](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031165733356.png)

![image-20221031172045325](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031172045325.png)

复制(删除）光标当前的位置到一行最后的位置(快捷键）：y+$（d+$)

5yy：复制当前行至后面的五行

5dd：删除当前行至后面的五行

复制(删除）当前光标的位置与这一行光标之前的位置：y+^（d+^)

r : 修改当前光标的内容

shift+r：替换一串字符

移动到当前词头：b

整篇文档的开头：gg（shift+h）

整篇文档的最后一行：G

移动到指定行：数字+G

：set nu （显示行号）

：set nonu（不要行号）

插入模式

![image-20221031173403638](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031173403638.png)

o：回车换了一行

![image-20221031173754655](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031173754655.png)

![image-20221031185245211](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031185245211.png)



![image-20221031190956466](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031190956466.png)

粘贴：ctrl+shift+v



在window中输入ipconfig能查看当前所有网络的连接信息

ping用来检测两台机器是否能正常发送数据、是否能正常通信

ping + ip

###  网络配置 （静态）

虚拟机指定静态IP

![image-20221031204150672](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031204150672.png)

所有配置文件在etc目录下，

修改静态ip命令：vim /etc/sysconfig/network-scripts/ifcfg- ens33  

![image-20221031211227166](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031211227166.png)

![image-20221031211652376](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031211652376.png)

快捷模式：4+G  ，ww  ，dw ，i

![image-20221031212708457](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031212708457.png)

配置保存完之后，再进行当前网络服务的重启

service network restart

再到主机window中ping一下

![image-20221031213516351](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221031213516351.png)

5.2.4修改IP地址后可能会遇到的问题

(1)物理机能ping通虚拟机，但是虚拟机ping不通物理机一般都是因为物理机的防
火墙问题,把防火墙关闭就行
(2)虚拟机能Ping通物理机,但是虚拟机Ping不通外网，一般都是因为DNS的设置有问题
(3)虚拟机Ping www.baidu.com显示域名未知等信息，一般查看GATEWAY和DNS设置是否正确
(4)如果以上全部设置完还是不行，需要关闭NetworkManager服务
systemctl stop NetworkManager关闭
systemctl disable NetworkManager禁用
(5)如果检查发现systemctl status network有问题需要检查ifcfg-ens33



### 配置主机名

1. hostname：主机名

2. 查找文件：vim /etc/hostname

3. 修改主机  ：wq（保存）

4. 重启服务器

5. hostnamectl（与主机有关的信息与配置信息）

6. hostnamectl set-hostname 主机名  （简洁方式）

7. 用 vim /etc/hosts 命令打开文件，进行添加hostname与ip的对应关系
8. 在主机C:\Windows\System32\drivers\etc\hosts 中进行添加hostname与ip的对应关系![image-20221101085714224](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101085714224.png)



### 远程登录ssh

ssh root@hado0p100

### systemctl

查看服务的方法：/usr/lib/systemd/system

![image-20221101103433213](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101103433213.png)

重启网络服务：systemctl restart network

查看状态：systemctl status network

![image-20221101104125891](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101104125891.png)

![image-20221101104328371](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101104328371.png)

关闭network服务（上不了网了）

network与NetworkManager保留其中一个处于活跃状态即可

![image-20221101105318275](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101105318275.png)

重启服务：systemctl restart NetworkManager![image-20221101105414929](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101105414929.png)







![image-20221101110151663](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101110151663.png)

![image-20221101110336927](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101110336927.png)

![image-20221101110339724](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101110339724.png)

查看默认的启动级别：vim /etc/inittab

图形化界面（登录之后出入）：init 5

控制台界面： init 3

***



关闭（开启）服务：setup

![image-20221101113038533](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101113038533.png)

用命令行查看服务：chkconfig --list

![image-20221101113544112](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101113544112.png)

查看当前防火墙的状态：systemctl status firewalld

![image-20221101114156135](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101114156135.png)

关闭当前防火墙的状态：systmectl stop firewalld

开机自启动（enabled）![image-20221101114355485](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101114355485.png)

关闭开机自启动：systemctl disable firewalld.service

![image-20221101115028262](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101115028262.png)

开启自启动防火墙：systemctl enable firewalld.service

![image-20221101115714456](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101115714456.png)

查找所有的服务状态：systemctl list- unit- files

![image-20221101124437178](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101124437178.png)

### 关机

（默认一分钟之后关机）：shutdown

（取消之前指定好的关机命令）：shutdown -c

(三分钟之后关机)：shutdown 3

(15:00之后关机)：shutdown 15:00

关机之前linux执行 sync(将数据由内存同步到硬盘中)操作

![image-20221101125612417](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101125612417.png)

命令：-l  (信息全部在一行展示)

![image-20221101130609021](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101130609021.png)

### 3.常见基本命令(重要)

#### 3.1 man获得帮助信息

基本语法：man （命令或配置文件）(描述功能)

help 获取shell内置命令的帮助信息 

简洁化的命令：ls --help

![image-20221101142153280](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101142153280.png)

![image-20221101131008148](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101131008148.png)

![image-20221101131415095](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101131415095.png)

朝下翻页：空格/pg dn/f

朝上翻页：pg up/b

![image-20221101142400834](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101142400834.png)

查看当前的命令是内嵌命令还是外部命令：type cd

![image-20221101143229550](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101143229550.png)

***

### 4. 文件目录类

![image-20221101142928253](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101142928253.png)

![image-20221101143739587](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101143739587.png)

![image-20221101144426910](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101144426910.png)

![image-20221101143854781](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101143854781.png)

![image-20221101144915112](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101144915112.png)

![image-20221101145250961](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101145250961.png)

#### 4.2 mkdir创建文件

创建多层次目录: mkdir -p 

![image-20221101150259464](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101150259464.png)

rmdir： 删除目录

![image-20221101151000341](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101151000341.png)

***

touch创建空文件

![image-20221101151146800](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101151146800.png)

![image-20221101160712462](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101160712462.png)

删除文件：rm -f 文件名

![image-20221101161008108](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101161008108.png)

#### 4.5 cp复制文件

![image-20221101190043490](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101190043490.png)

\:原生命令

\cp：直接覆盖，不再提示

![image-20221101190602326](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101190602326.png)

***

rm：删除

![image-20221101190757447](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101190757447.png)

![image-20221101191145489](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101191145489.png)

***

mv：移动

![image-20221101191423671](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101191423671.png)

![image-20221101191329184](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221101191329184.png)

***

查看文件：cat

![image-20221102081316338](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102081316338.png)

![image-20221102081748179](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102081748179.png)

#### more

![=](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102081847686.png)

#### less

![image-20221102082405285](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102082405285.png)

#### echo

![image-20221102082742820](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102082742820.png)



#### 重定向

![image-20221102083332372](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102083332372.png)![image-20221102084451348](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102084451348.png)

输出环境变量：echo $(双击tab键)

![image-20221102084752447](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102084752447.png)

#### head显示文件头部内容

![image-20221102085202062](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102085202062.png)

#### tail输出文件尾部内容

![image-20221102085356430](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102085356430.png)

ctrl+s：暂停

#### ln软连接  (即类似指针)

![image-20221102085950693](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102085950693.png)

![image-20221102090434121](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102090434121.png)

![image-20221102090629675](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102090629675.png)

回退：cd -

![image-20221102090808556](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102090808556.png)

![image-20221102093028486](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102093028486.png)



![image-20221102093725339](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102093725339.png)

#### history

![image-20221102110710448](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102110710448.png)

删除历史命令：

```linux
:history -c
```

显示刚刚过去的十条命令：

```linux
: history 10
```

查看之前标号的历史命令：！(数字)

![image-20221102111635113](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102111635113.png)



#### 日期

![image-20221102111403745](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102111403745.png)

![image-20221102111425642](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102111425642.png)



![image-20221102111732954](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102111732954.png)

![image-20221102114106124](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102114106124.png)

![image-20221102114157844](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102114157844.png)

![image-20221102114445127](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102114445127.png)

1. 查看2022年的月份
2. 查看当前月与前后一个月
3. 把星期一放在第一个位置
4. 查看本年的月份

```linux
:cal 2022
:cal 3
:cal -m
:cla -y
```

***

### 用户管理命令

![image-20221102115145812](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102115145812.png)

![image-20221102115706157](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102115706157.png)

![image-20221102121143435](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102121143435.png)

![image-20221102121329470](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102121329470.png)

#### su

![image-20221102123416308](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102123416308.png)

#### sudo 设置普通用户具有root权限

![image-20221102123528953](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102123528953.png)

![image-20221102125411685](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102125411685.png)

##### userdel

![image-20221102125706501](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102125706501.png)

![image-20221102125927471](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102125927471.png)

:userdel -r

![image-20221102130354702](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102130354702.png)

![image-20221102130844651](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102130844651.png)

#### group

![image-20221102130900513](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102130900513.png)

![image-20221102131213464](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102131213464.png)

![image-20221102131420845](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102131420845.png)

![image-20221102131842508](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102131842508.png)

添加组

![image-20221102132637283](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102132637283.png)

1.将用户添加到新创建的组中

2. 修改原先的组名

![image-20221102132750500](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102132750500.png)

***



![image-20221102145041256](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102145041256.png)

  ##### 文件类型: ls /dev/

![image-20221102150125304](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102150125304.png)

1. 表示普通文件: - ![image-20221102145411109](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102145411109.png)

2. 目录文件夹：d ![image-20221102145459218](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102145459218.png)

3. 链接：l
4. 字符设备文件（鼠标、键盘）：c ![image-20221102150159777](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102150159777.png)
5. 块设备文件（硬盘）：b ![image-20221102150146113](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102150146113.png)

![image-20221102150919354](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102150919354.png)

![image-20221102150932451](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102150932451.png)

：ls -al (能显示隐藏文件)

![image-20221102151503077](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102151503077.png)

![image-20221102151735486](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102151735486.png)

![image-20221102151936934](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102151936934.png)

![image-20221102152053661](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102152053661.png)

#### chmod 改变权限

![image-20221102152325180](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102152325180.png)

![image-20221102152631922](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102152631922.png)

![image-20221102154134763](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102154134763.png)

![image-20221102154020424](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102154020424.png)

![image-20221102152949530](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102152949530.png)

![image-20221102153308898](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102153308898.png)

![image-20221102153526024](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102153526024.png)

![image-20221102155831680](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102155831680.png)

![image-20221102155936293](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102155936293.png)

![image-20221102160117160](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102160117160.png)

#### chown 

![image-20221102160227600](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102160227600.png)

![image-20221102160242581](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102160242581.png)

![image-20221102163540266](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102163540266.png)

### 用户权限的总结

```linux
[root@hadoop100 ~]# groupadd bigdata
[root@hadoop100 ~]# groupadd testing
[root@hadoop100 ~]# cat /etc/group
root:x:0:
bin:x:1:
daemon:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mem:x:8:
kmem:x:9:
wheel:x:10:
cdrom:x:11:
mail:x:12:postfix
man:x:15:
dialout:x:18:
floppy:x:19:
games:x:20:
tape:x:33:
video:x:39:
ftp:x:50:
lock:x:54:
audio:x:63:
nobody:x:99:
users:x:100:
utmp:x:22:
utempter:x:35:
input:x:999:
systemd-journal:x:190:
systemd-network:x:192:
dbus:x:81:
polkitd:x:998:
printadmin:x:997:
cgred:x:996:
libstoragemgmt:x:995:
colord:x:994:
rpc:x:32:
saned:x:993:
dip:x:40:
gluster:x:992:
ssh_keys:x:991:
saslauth:x:76:
abrt:x:173:
setroubleshoot:x:990:
rtkit:x:172:
pulse-access:x:989:
pulse-rt:x:988:
pulse:x:171:
radvd:x:75:
chrony:x:987:
unbound:x:986:
kvm:x:36:qemu
qemu:x:107:
tss:x:59:
libvirt:x:985:
sssd:x:984:
usbmuxd:x:113:
geoclue:x:983:
ntp:x:38:
gdm:x:42:
rpcuser:x:29:
nfsnobody:x:65534:
gnome-initial-setup:x:982:
sshd:x:74:
slocate:x:21:
avahi:x:70:
postdrop:x:90:
postfix:x:89:
stapusr:x:156:
stapsys:x:157:
stapdev:x:158:
tcpdump:x:72:
lwxfairy:x:1000:lwxfairy
bigdata:x:1001:
testing:x:1002:
[root@hadoop100 ~]# useradd -g bigdata lihua
[root@hadoop100 ~]# id lihua
uid=1001(lihua) gid=1001(bigdata) 组=1001(bigdata)
[root@hadoop100 ~]# useradd -g bigdata liming
[root@hadoop100 ~]# id liming
uid=1002(liming) gid=1001(bigdata) 组=1001(bigdata)
[root@hadoop100 ~]# useradd -g testing xiaohong
[root@hadoop100 ~]# id xiaohong
uid=1003(xiaohong) gid=1002(testing) 组=1002(testing)
[root@hadoop100 ~]# useradd -g testing xiaozhang 
[root@hadoop100 ~]# id xiaozhang 
uid=1004(xiaozhang) gid=1002(testing) 组=1002(testing)
[root@hadoop100 ~]# cd /home/
[root@hadoop100 home]# ls
dave  lihua  liming  lwxfairy  xiaohong  xiaozhang
[root@hadoop100 home]# su lihua
[lihua@hadoop100 home]$ cd ~
[lihua@hadoop100 ~]$ pwd
/home/lihua
[lihua@hadoop100 ~]$ vim import_codde
[lihua@hadoop100 ~]$ ll
总用量 4
-rw-r--r--. 1 lihua bigdata 12 11月  2 17:15 import_codde
[lihua@hadoop100 ~]$ exit
exit
[root@hadoop100 home]# su liming
[liming@hadoop100 home]$ cd ~
[liming@hadoop100 ~]$ cd ../lihua/
bash: cd: ../lihua/: 权限不够
[liming@hadoop100 ~]$ exit
exit
[root@hadoop100 home]# ls
dave  lihua  liming  lwxfairy  xiaohong  xiaozhang
[root@hadoop100 home]# ll
总用量 4
drwx------.  3 xiaohong      1004   78 11月  2 12:06 dave
drwx------.  5 lihua     bigdata   164 11月  2 17:18 lihua
drwx------.  5 liming    bigdata   128 11月  2 17:18 liming
drwx------. 15 lwxfairy  lwxfairy 4096 11月  2 15:21 lwxfairy
drwx------.  3 xiaohong  testing    78 11月  2 17:09 xiaohong
drwx------.  3 xiaozhang testing    78 11月  2 17:10 xiaozhang
[root@hadoop100 home]# chmod g+x lihua/
[root@hadoop100 home]# ll
总用量 4
drwx------.  3 xiaohong      1004   78 11月  2 12:06 dave
drwx--x---.  5 lihua     bigdata   164 11月  2 17:18 lihua
drwx------.  5 liming    bigdata   128 11月  2 17:18 liming
drwx------. 15 lwxfairy  lwxfairy 4096 11月  2 15:21 lwxfairy
drwx------.  3 xiaohong  testing    78 11月  2 17:09 xiaohong
drwx------.  3 xiaozhang testing    78 11月  2 17:10 xiaozhang
[root@hadoop100 home]# su liming
[liming@hadoop100 home]$ cd lihua/
[liming@hadoop100 lihua]$ ll
ls: 无法打开目录.: 权限不够
[liming@hadoop100 lihua]$ exit
exit
[root@hadoop100 home]# chmod g+r lihua/
[root@hadoop100 home]# ll
总用量 4
drwx------.  3 xiaohong      1004   78 11月  2 12:06 dave
drwxr-x---.  5 lihua     bigdata   164 11月  2 17:18 lihua
drwx------.  5 liming    bigdata   128 11月  2 17:18 liming
drwx------. 15 lwxfairy  lwxfairy 4096 11月  2 15:21 lwxfairy
drwx------.  3 xiaohong  testing    78 11月  2 17:09 xiaohong
drwx------.  3 xiaozhang testing    78 11月  2 17:10 xiaozhang
[root@hadoop100 home]# su liming 
[liming@hadoop100 home]$ cd lihua
[liming@hadoop100 lihua]$ ll
总用量 4
-rw-r--r--. 1 lihua bigdata 12 11月  2 17:15 import_codde
[liming@hadoop100 lihua]$ cat import_codde
hello world
[liming@hadoop100 lihua]$ vim import_codde 
[liming@hadoop100 lihua]$ exit
exit
[root@hadoop100 home]# su lihua
[lihua@hadoop100 home]$ cd ~
[lihua@hadoop100 ~]$ ll
总用量 4
-rw-r--r--. 1 lihua bigdata 12 11月  2 17:15 import_codde
[lihua@hadoop100 ~]$ chmod g+w import_codde 
[lihua@hadoop100 ~]$ exit
exit
[root@hadoop100 home]# su liming
[liming@hadoop100 home]$ cd lihua/
[liming@hadoop100 lihua]$ vim import_codde 
[liming@hadoop100 lihua]$ ll
总用量 4
-rw-rw-r--. 1 lihua bigdata 16 11月  2 17:50 import_codde
[liming@hadoop100 lihua]$ cat import_codde 
hello world
666
[liming@hadoop100 lihua]$ exit
exit
[root@hadoop100 home]# su xiaohong
[xiaohong@hadoop100 home]$ ll
总用量 4
drwx------.  3 xiaohong      1004   78 11月  2 12:06 dave
drwxr-x---.  5 lihua     bigdata   164 11月  2 17:18 lihua
drwx------.  5 liming    bigdata   144 11月  2 17:50 liming
drwx------. 15 lwxfairy  lwxfairy 4096 11月  2 15:21 lwxfairy
drwx------.  5 xiaohong  testing   107 11月  2 17:56 xiaohong
drwx------.  3 xiaozhang testing    78 11月  2 17:10 xiaozhang
[xiaohong@hadoop100 home]$ cd lihua
bash: cd: lihua: 权限不够
[xiaohong@hadoop100 home]$ exit
exit
[root@hadoop100 home]# chmod 755 lihua
[root@hadoop100 home]# ll
总用量 4
drwx------.  3 xiaohong      1004   78 11月  2 12:06 dave
drwxr-xr-x.  5 lihua     bigdata   164 11月  2 17:18 lihua
drwx------.  5 liming    bigdata   144 11月  2 17:50 liming
drwx------. 15 lwxfairy  lwxfairy 4096 11月  2 15:21 lwxfairy
drwx------.  5 xiaohong  testing   128 11月  2 17:57 xiaohong
drwx------.  3 xiaozhang testing    78 11月  2 17:10 xiaozhang
[root@hadoop100 home]# su xiaohong
[xiaohong@hadoop100 home]$ ll
总用量 4
drwx------.  3 xiaohong      1004   78 11月  2 12:06 dave
drwxr-xr-x.  5 lihua     bigdata   164 11月  2 17:18 lihua
drwx------.  5 liming    bigdata   144 11月  2 17:50 liming
drwx------. 15 lwxfairy  lwxfairy 4096 11月  2 15:21 lwxfairy
drwx------.  5 xiaohong  testing   128 11月  2 17:57 xiaohong
drwx------.  3 xiaozhang testing    78 11月  2 17:10 xiaozhang
[xiaohong@hadoop100 home]$ cd lihua
[xiaohong@hadoop100 lihua]$ ll
总用量 4
-rw-rw-r--. 1 lihua bigdata 16 11月  2 17:50 import_codde
[xiaohong@hadoop100 lihua]$ cat import_codde 
hello world
666
[xiaohong@hadoop100 lihua]$ vim import_codde 
[xiaohong@hadoop100 lihua]$ exit
exit
[root@hadoop100 home]# usermod -g bigdata xiaozhang 
[root@hadoop100 home]# id xiaozhang 
uid=1004(xiaozhang) gid=1001(bigdata) 组=1001(bigdata)
[root@hadoop100 home]# su xiaozhang 
[xiaozhang@hadoop100 home]$ cd lihua
[xiaozhang@hadoop100 lihua]$ vim import_codde 
[xiaozhang@hadoop100 lihua]$ cat import_codde 
hello world
666
study linux
[xiaozhang@hadoop100 lihua]$ 






```

创建组、添加成员

![image-20221102170749307](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102170749307.png)

![image-20221102170213856](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102170213856.png)

![image-20221102171401832](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102171401832.png)

同组人员 访问 查看 修改

![image-20221102171740900](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102171740900.png)

![image-20221102172456264](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102172456264.png)

![image-20221102173126660](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102173154835.png)

![image-20221102172953519](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102172953519.png)

![image-20221102175307978](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102175307978.png)

不同组人的 访问 查看  





![image-20221102180622964](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102180622964.png)

![image-20221102180745130](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102180745130.png)

![image-20221102175937158](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102175937158.png)

#### find查找

![image-20221102184929919](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102184929919.png)

``` linux

[root@hadoop100 ~]# find -name info
./.local/share/Trash/info
[root@hadoop100 ~]# touch 公共/info
[root@hadoop100 ~]# find -name info
./.local/share/Trash/info
./公共/info
[root@hadoop100 ~]# find /root -name info
/root/.local/share/Trash/info
/root/公共/info
[root@hadoop100 ~]# find /root/公共 -name info
/root/公共/info
[root@hadoop100 ~]# 
[root@hadoop100 ~]# find /root -name "*.cfg"
/root/anaconda-ks.cfg
/root/initial-setup-ks.cfg
/root/.config/yelp/yelp.cfg
/root/.local/share/telepathy/mission-control/accounts.cfg
/root/.local/share/telepathy/mission-control/accounts-goa.cfg
[root@hadoop100 ~]# find /home -user lwxfairy
/home/lwxfairy
/home/lwxfairy/.mozilla
/home/lwxfairy/.mozilla/extensions
[root@hadoop100 ~]# find /root/ -size +1.9k
find: Invalid argument `+1.9k' to -size

```

![image-20221102185746887](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102185746887.png)

#### locate

![image-20221102190144461](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102190144461.png)

```linux
[root@hadoop100 ~]# locate updatedb
```

```linux
[root@hadoop100 ~]# which ls
alias ls='ls --color=auto'
	/usr/bin/ls
[root@hadoop100 ~]# which locate
/usr/bin/locate
[root@hadoop100 ~]# which which
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
	/usr/bin/alias
	/usr/bin/which
[root@hadoop100 ~]# whereis locate
locate: /usr/bin/locate /usr/share/man/man1/locate.1.gz
[root@hadoop100 ~]# 

```

#### grep

![image-20221102190700296](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102190700296.png)

```linux
[root@hadoop100 ~]# grep -n boot initial-setup-ks.cfg 
3:xconfig  --startxonboot
12:# Run the Setup Agent on first boot
13:firstboot --enable
23:network  --bootproto=dhcp --device=ens33 --ipv6=auto --activate
31:# System bootloader configuration
32:bootloader --location=mbr --boot-drive=sda
37:part /boot --fstype="xfs" --ondisk=sda --size=1024
[root@hadoop100 ~]# 

```

![image-20221102191244179](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102191244179.png)

#### gzip/gunzip压缩

![image-20221102191438510](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102191438510.png)

```linux
[root@hadoop100 ~]# gzip xzhdx.txt
[root@hadoop100 ~]# ls
anaconda-ks.cfg       xzhdx.txt.gz  模板  图片  下载  桌面
initial-setup-ks.cfg  公共          视频  文档  音乐
[root@hadoop100 ~]# gunzip xzhdx.txt.gz
[root@hadoop100 ~]# ls
anaconda-ks.cfg       xzhdx.txt  模板  图片  下载  桌面
initial-setup-ks.cfg  公共       视频  文档  音乐
[root@hadoop100 ~]# ls -lh
总用量 12K
-rw-------. 1 root root 1.9K 10月 30 23:52 anaconda-ks.cfg
-rw-r--r--. 1 root root 1.9K 10月 30 23:59 initial-setup-ks.cfg
-rw-r--r--. 1 root root   25 11月  2 19:18 xzhdx.txt
drwxr-xr-x. 2 root root   18 11月  2 18:51 公共
drwxr-xr-x. 2 root root    6 10月 31 00:00 模板
drwxr-xr-x. 2 root root    6 10月 31 00:00 视频
drwxr-xr-x. 2 root root    6 10月 31 00:00 图片
drwxr-xr-x. 2 root root    6 10月 31 00:00 文档
drwxr-xr-x. 2 root root    6 10月 31 00:00 下载
drwxr-xr-x. 2 root root    6 10月 31 00:00 音乐
drwxr-xr-x. 2 root root   58 10月 31 19:15 桌面
[root@hadoop100 ~]
```

![image-20221102192148455](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102192148455.png)



![image-20221102192044305](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102192044305.png)

```linux
[root@hadoop100 ~]# zip -r myroot.zip /root

```

```linux
[root@hadoop100 ~]# ls -lh
总用量 51M
-rw-------. 1 root root 1.9K 10月 30 23:52 anaconda-ks.cfg
-rw-r--r--. 1 root root 1.9K 10月 30 23:59 initial-setup-ks.cfg
-rw-r--r--. 1 root root  51M 11月  2 19:24 myroot.zip
-rw-r--r--. 1 root root   25 11月  2 19:18 xzhdx.txt
drwxr-xr-x. 2 root root   18 11月  2 18:51 公共
drwxr-xr-x. 2 root root    6 10月 31 00:00 模板
drwxr-xr-x. 2 root root    6 10月 31 00:00 视频
drwxr-xr-x. 2 root root    6 10月 31 00:00 图片
drwxr-xr-x. 2 root root    6 10月 31 00:00 文档
drwxr-xr-x. 2 root root    6 10月 31 00:00 下载
drwxr-xr-x. 2 root root    6 10月 31 00:00 音乐
drwxr-xr-x. 2 root root   58 10月 31 19:15 桌面
[root@hadoop100 ~]# 

```

![image-20221102192649658](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102192649658.png)

![image-20221102192825602](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102192825602.png)

#### tar 打包

![image-20221102193016758](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102193016758.png)

```linux
[root@hadoop100 ~]# tar -zcvf temp.tar.gz initial-setup-ks.cfg  anaconda-ks.cfg  xzhdx.txt 
initial-setup-ks.cfg
anaconda-ks.cfg
xzhdx.txt
[root@hadoop100 ~]# ls -lh
总用量 16K
-rw-------. 1 root root 1.9K 10月 30 23:52 anaconda-ks.cfg
-rw-r--r--. 1 root root 1.9K 10月 30 23:59 initial-setup-ks.cfg
-rw-r--r--. 1 root root 1.3K 11月  2 19:32 temp.tar.gz
-rw-r--r--. 1 root root   25 11月  2 19:18 xzhdx.txt
drwxr-xr-x. 2 root root   18 11月  2 18:51 公共
drwxr-xr-x. 2 root root    6 10月 31 00:00 模板
drwxr-xr-x. 2 root root    6 10月 31 00:00 视频
drwxr-xr-x. 2 root root    6 10月 31 00:00 图片
drwxr-xr-x. 2 root root    6 10月 31 00:00 文档
drwxr-xr-x. 2 root root    6 10月 31 00:00 下载
drwxr-xr-x. 2 root root    6 10月 31 00:00 音乐
drwxr-xr-x. 2 root root   58 10月 31 19:15 桌面
[root@hadoop100 ~]# 

```

![image-20221102193408105](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102193408105.png)

解包

```linux
[root@hadoop100 ~]# tar -zxvf temp.tar.gz -C /tmp
initial-setup-ks.cfg
anaconda-ks.cfg
xzhdx.txt
```



![image-20221102193625377](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102193625377.png)

#### 磁盘

(未成功)安装tree：yum install tree

![image-20221102201727438](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102201727438.png)

```linux
[root@hadoop100 network-scripts]# du -sh
280K	
[root@hadoop100 network-scripts]# du --max-depth=1 -ah
4.0K	./ifcfg-lo
0	./ifdown
4.0K	./ifdown-bnep
8.0K	./ifdown-eth
4.0K	./ifdown-ippp
8.0K	./ifdown-ipv6
0	./ifdown-isdn
4.0K	./ifdown-post
4.0K	./ifdown-ppp
4.0K	./ifdown-routes
4.0K	./ifdown-sit
4.0K	./ifdown-tunnel
0	./ifup
16K	./ifup-aliases
4.0K	./ifup-bnep
16K	./ifup-eth
12K	./ifup-ippp
12K	./ifup-ipv6
0	./ifup-isdn
4.0K	./ifup-plip
4.0K	./ifup-plusb
8.0K	./ifup-post
8.0K	./ifup-ppp
4.0K	./ifup-routes
4.0K	./ifup-sit
4.0K	./ifup-tunnel
4.0K	./ifup-wireless
8.0K	./init.ipv6-global
24K	./network-functions
32K	./network-functions-ipv6
8.0K	./ifdown-ib
12K	./ifup-ib
4.0K	./ifdown-Team
4.0K	./ifdown-TeamPort
4.0K	./ifup-Team
4.0K	./ifup-TeamPort
12K	./.ifcfg-ens33.swp
12K	./.ifct-enss33.swp
4.0K	./ifcfg-ens33
280K	.
[root@hadoop100 network-scripts]# 

```

```linux
[root@hadoop100 network-scripts]# du -sh /
du: 无法访问"/proc/6390/task/6390/fd/3": 没有那个文件或目录
du: 无法访问"/proc/6390/task/6390/fdinfo/3": 没有那个文件或目录
du: 无法访问"/proc/6390/fd/4": 没有那个文件或目录
du: 无法访问"/proc/6390/fdinfo/4": 没有那个文件或目录
9.5G	/

```

![image-20221102203628702](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102203628702.png)



![image-20221102203647667](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102203647667.png)

 当前的磁盘占用信息

临时的文件系统基于内存的

共享内存：/dev/shm

devtmpfs（开机启动的时候创建的）

```linux
文件系统        容量  已用  可用 已用% 挂载点
devtmpfs        2.0G     0  2.0G    0% /dev
tmpfs           2.0G     0  2.0G    0% /dev/shm
tmpfs           2.0G   13M  2.0G    1% /run
tmpfs           2.0G     0  2.0G    0% /sys/fs/cgroup
/dev/sda3        15G  5.0G   11G   33% /
/dev/sda1      1014M  169M  846M   17% /boot
tmpfs           394M   20K  394M    1% /run/user/0
/dev/sr0        4.4G  4.4G     0  100% /run/media/root/CentOS 7 x86_64
[root@hadoop100 network-scripts]# free -h
              total        used        free      shared  buff/cache   available
Mem:           3.8G        923M        1.9G         21M        1.1G        2.6G
Swap:          4.0G          0B        4.0G

```

![image-20221102205245562](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102205245562.png)

![image-20221102210950355](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102210950355.png)

IDE -> hda/hdb

SATA/SCSI ->sda/sdb

```linux
[root@hadoop100 network-scripts]# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
├─sda2   8:2    0    4G  0 part [SWAP]
└─sda3   8:3    0   15G  0 part /
sr0     11:0    1  4.4G  0 rom  /run/media/root/CentOS 7 x86_64
[root@hadoop100 network-scripts]# ls /dev/ |grep sr0
sr0
[root@hadoop100 network-scripts]# ll /dev/ |grep sr0
lrwxrwxrwx. 1 root root           3 11月  2 16:02 cdrom -> sr0
brw-rw----+ 1 root cdrom    11,   0 11月  2 16:02 sr0
[root@hadoop100 network-scripts]# lsblk -f
NAME   FSTYPE  LABEL           UUID                                 MOUNTPOINT
sda                                                                 
├─sda1 xfs                     218a0d12-ef2c-40de-bd6e-f2c46a2bb8d9 /boot
├─sda2 swap                    cd54acb2-d66d-446a-962f-584f69cd3e43 [SWAP]
└─sda3 xfs                     33eed5a0-c497-4502-9564-2b307d95d7fd /
sr0    iso9660 CentOS 7 x86_64 2020-11-04-11-36-43-00               /run/media/r
[root@hadoop100 network-scripts]# 

```

![image-20221102212008758](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102212008758.png)

![image-20221102221742427](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221102221742427.png)



### 挂载点

```linux
[root@hadoop100 ~]# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
├─sda2   8:2    0    4G  0 part [SWAP]
└─sda3   8:3    0   15G  0 part /
sr0     11:0    1  4.4G  0 rom  /run/media/root/CentOS 7 x86_64
[root@hadoop100 ~]# ls /run/media/root/CentOS\ 7\ x86_64/
CentOS_BuildTag  GPL       LiveOS    RPM-GPG-KEY-CentOS-7
EFI              images    Packages  RPM-GPG-KEY-CentOS-Testing-7
EULA             isolinux  repodata  TRANS.TBL
[root@hadoop100 ~]# 

```

![image-20221103082512051](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103082512051.png)

```linux
[root@hadoop100 ~]# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
├─sda2   8:2    0    4G  0 part [SWAP]
└─sda3   8:3    0   15G  0 part /
sr0     11:0    1  4.4G  0 rom  
[root@hadoop100 ~]# ls /run/media/root/CentOS\ 7\ x86_64/
ls: 无法访问/run/media/root/CentOS 7 x86_64/: 没有那个文件或目录
[root@hadoop100 ~]# 


```

![image-20221103082645904](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103082645904.png)

#### 手动挂载：

![image-20221103083311801](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103083311801.png)

![image-20221103083943575](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103083943575.png)

![image-20221103084032835](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103084032835.png)

#### 开机自动挂载



![image-20221103084139836](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103084139836.png)

![image-20221103084653413](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103084653413.png)

![image-20221103084844428](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103084844428.png)

#### fdisk分区

![image-20221103085016357](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103085016357.png)

创建新硬盘（一直下一步）

![image-20221103085536291](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103085536291.png)

![image-20221103085712130](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103085712130.png)

添加了之后需要重新启动下：reboot

```linux
[root@hadoop100 ~]# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
├─sda2   8:2    0    4G  0 part [SWAP]
└─sda3   8:3    0   15G  0 part /
sdb      8:16   0   20G  0 disk 
sr0     11:0    1 1024M  0 rom  
[root@hadoop100 ~]# fdisk -l

磁盘 /dev/sdb：21.5 GB, 21474836480 字节，41943040 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


磁盘 /dev/sda：21.5 GB, 21474836480 字节，41943040 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0x000b62cb

   设备 Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    10487807     4194304   82  Linux swap / Solaris
/dev/sda3        10487808    41943039    15727616   83  Linux
[root@hadoop100 ~]# 

```

![image-20221103090613352](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103090613352.png)

```linux
[root@hadoop100 ~]# fdisk /dev/sdb
欢迎使用 fdisk (util-linux 2.23.2)。

更改将停留在内存中，直到您决定将更改写入磁盘。
使用写入命令前请三思。

Device does not contain a recognized partition table
使用磁盘标识符 0x621874f3 创建新的 DOS 磁盘标签。

命令(输入 m 获取帮助)：m
命令操作
   a   toggle a bootable flag
   b   edit bsd disklabel
   c   toggle the dos compatibility flag
   d   delete a partition
   g   create a new empty GPT partition table
   G   create an IRIX (SGI) partition table
   l   list known partition types
   m   print this menu
   n   add a new partition
   o   create a new empty DOS partition table
   p   print the partition table
   q   quit without saving changes
   s   create a new empty Sun disklabel
   t   change a partition's system id
   u   change display/entry units
   v   verify the partition table
   w   write table to disk and exit
   x   extra functionality (experts only)

命令(输入 m 获取帮助)：p

磁盘 /dev/sdb：21.5 GB, 21474836480 字节，41943040 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0x621874f3

   设备 Boot      Start         End      Blocks   Id  System

命令(输入 m 获取帮助)：n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p): p
分区号 (1-4，默认 1)：
起始 扇区 (2048-41943039，默认为 2048)：
将使用默认值 2048
Last 扇区, +扇区 or +size{K,M,G} (2048-41943039，默认为 41943039)：
将使用默认值 41943039
分区 1 已设置为 Linux 类型，大小设为 20 GiB

命令(输入 m 获取帮助)：p

磁盘 /dev/sdb：21.5 GB, 21474836480 字节，41943040 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0x621874f3

   设备 Boot      Start         End      Blocks   Id  System
/dev/sdb1            2048    41943039    20970496   83  Linux

命令(输入 m 获取帮助)：w
[root@hadoop100 ~]# lsblk -f
NAME   FSTYPE LABEL UUID                                 MOUNTPOINT
sda                                                      
├─sda1 xfs          218a0d12-ef2c-40de-bd6e-f2c46a2bb8d9 /boot
├─sda2 swap         cd54acb2-d66d-446a-962f-584f69cd3e43 [SWAP]
└─sda3 xfs          33eed5a0-c497-4502-9564-2b307d95d7fd /
sdb                                                      
└─sdb1                                                   
sr0         
```

![image-20221103091935270](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103091935270.png)

进行格式化与挂载：
```linux
[root@hadoop100 ~]# mkfs -t xfs /dev/sdb1
meta-data=/dev/sdb1              isize=512    agcount=4, agsize=1310656 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0, sparse=0
data     =                       bsize=4096   blocks=5242624, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
[root@hadoop100 ~]# lsblk -f
NAME   FSTYPE LABEL UUID                                 MOUNTPOINT
sda                                                      
├─sda1 xfs          218a0d12-ef2c-40de-bd6e-f2c46a2bb8d9 /boot
├─sda2 swap         cd54acb2-d66d-446a-962f-584f69cd3e43 [SWAP]
└─sda3 xfs          33eed5a0-c497-4502-9564-2b307d95d7fd /
sdb                                                      
└─sdb1 xfs          031bfdb3-658f-4352-a8c9-0d0aeed334c8 
sr0                                                      
[root@hadoop100 ~]# mount /dev/sdb1 /home/lwxfairy/
[root@hadoop100 ~]# lsblk -f
NAME   FSTYPE LABEL UUID                                 MOUNTPOINT
sda                                                      
├─sda1 xfs          218a0d12-ef2c-40de-bd6e-f2c46a2bb8d9 /boot
├─sda2 swap         cd54acb2-d66d-446a-962f-584f69cd3e43 [SWAP]
└─sda3 xfs          33eed5a0-c497-4502-9564-2b307d95d7fd /
sdb                                                      
└─sdb1 xfs          031bfdb3-658f-4352-a8c9-0d0aeed334c8 /home/lwxfair
sr0                                                      
[root@hadoop100 ~]# df -h
文件系统        容量  已用  可用 已用% 挂载点
devtmpfs        2.0G     0  2.0G    0% /dev
tmpfs           2.0G     0  2.0G    0% /dev/shm
tmpfs           2.0G   13M  2.0G    1% /run
tmpfs           2.0G     0  2.0G    0% /sys/fs/cgroup
/dev/sda3        15G  4.6G   11G   31% /
/dev/sda1      1014M  208M  807M   21% /boot
tmpfs           394M   40K  394M    1% /run/user/0
/dev/sdb1        20G   33M   20G    1% /home/lwxfairy
[root@hadoop100 ~]# ls
anaconda-ks.cfg       temp.tar.gz  公共  视频  文档  音乐
initial-setup-ks.cfg  xzhdx.txt    模板  图片  下载  桌面
[root@hadoop100 ~]# ll -h
总用量 16K
-rw-------. 1 root root 1.9K 10月 30 23:52 anaconda-ks.cfg
-rw-r--r--. 1 root root 1.9K 10月 30 23:59 initial-setup-ks.cfg
-rw-r--r--. 1 root root 1.3K 11月  2 19:32 temp.tar.gz
-rw-r--r--. 1 root root   25 11月  2 19:18 xzhdx.txt
drwxr-xr-x. 2 root root   18 11月  2 18:51 公共
drwxr-xr-x. 2 root root    6 10月 31 00:00 模板
drwxr-xr-x. 2 root root    6 10月 31 00:00 视频
drwxr-xr-x. 2 root root    6 10月 31 00:00 图片
drwxr-xr-x. 2 root root    6 10月 31 00:00 文档
drwxr-xr-x. 2 root root    6 10月 31 00:00 下载
drwxr-xr-x. 2 root root    6 10月 31 00:00 音乐
drwxr-xr-x. 2 root root   58 10月 31 19:15 桌面
[root@hadoop100 ~]# cp temp.tar.gz /home/lwxfairy 
[root@hadoop100 ~]# df -h
文件系统        容量  已用  可用 已用% 挂载点
devtmpfs        2.0G     0  2.0G    0% /dev
tmpfs           2.0G     0  2.0G    0% /dev/shm
tmpfs           2.0G   13M  2.0G    1% /run
tmpfs           2.0G     0  2.0G    0% /sys/fs/cgroup
/dev/sda3        15G  4.6G   11G   31% /
/dev/sda1      1014M  208M  807M   21% /boot
tmpfs           394M   44K  394M    1% /run/user/0
/dev/sdb1        20G   33M   20G    1% /home/lwxfairy
[root@hadoop100 ~]# umount /home/lwxfairy
[root@hadoop100 ~]# df -h
文件系统        容量  已用  可用 已用% 挂载点
devtmpfs        2.0G     0  2.0G    0% /dev
tmpfs           2.0G     0  2.0G    0% /dev/shm
tmpfs           2.0G   13M  2.0G    1% /run
tmpfs           2.0G     0  2.0G    0% /sys/fs/cgroup
/dev/sda3        15G  4.6G   11G   31% /
/dev/sda1      1014M  208M  807M   21% /boot
tmpfs           394M   52K  394M    1% /run/user/0
[root@hadoop100 ~]# lsblk -f
NAME   FSTYPE LABEL UUID                                 MOUNTPOINT
sda                                                      
├─sda1 xfs          218a0d12-ef2c-40de-bd6e-f2c46a2bb8d9 /boot
├─sda2 swap         cd54acb2-d66d-446a-962f-584f69cd3e43 [SWAP]
└─sda3 xfs          33eed5a0-c497-4502-9564-2b307d95d7fd /
sdb                                                      
└─sdb1 xfs          031bfdb3-658f-4352-a8c9-0d0aeed334c8 
sr0                                                      
[root@hadoop100 ~]# ll /home/lwxfairy
总用量 8
-rw-r--r--. 1 root     root     1851 11月  2 15:15 anaconda-ks.cfg
-rwx------. 1 lwxfairy root     1882 11月  2 15:16 initial-setup-ks.cfg
lrwxrwxrwx. 1 root     root       12 11月  2 10:51 myfolder -> /root/folder
drwxr-xr-x. 2 lwxfairy lwxfairy    6 11月  1 11:19 公共
drwxr-xr-x. 2 lwxfairy lwxfairy    6 11月  1 11:19 模板
drwxr-xr-x. 2 lwxfairy lwxfairy    6 11月  1 11:19 视频
drwxr-xr-x. 2 lwxfairy lwxfairy    6 11月  1 11:19 图片
drwxr-xr-x. 2 lwxfairy lwxfairy    6 11月  1 11:19 文档
drwxr-xr-x. 2 lwxfairy lwxfairy    6 11月  1 11:19 下载
drwxr-xr-x. 2 lwxfairy lwxfairy    6 11月  1 11:19 音乐
drwxr-xr-x. 2 lwxfairy lwxfairy    6 11月  1 11:19 桌面
[root@hadoop100 ~]# 

```

![image-20221103093252693](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103093252693.png)

![image-20221103093545203](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103093545203.png)

![image-20221103093654628](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103093654628.png)

***

### 系统管理

查看服务（守护进程，即守护后台服务）：

```linux
root@hadoop100 ~]# ls /usr/lib/systemd/system

```

#### ps查看当前系统进程状态

![image-20221103094744320](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103094744320.png)

![image-20221103095537477](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103095537477.png)

![image-20221103095801565](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103095801565.png)![image-20221103100348905](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103100348905.png)

![image-20221103100407204](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103100407204.png)

![image-20221103100813419](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103100813419.png)

![image-20221103101359160](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103101359160.png)

#### kill 终止进程

![image-20221103101805047](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103101805047.png)

kill后台守护进程（sshd）远程登录不进

即需要重新开启sshd：systemctl start sshd

查看当前的服务：systemctl status sshd

进程：1->sshd->远程登录->bash

***

（远程）:killall sshd (守护进程也关闭了，即全部都连接不上，需要到物理机上重启开启sshd)

```linux
[root@hadoop100 ~]# systemctl start sshd

```

![image-20221103103411761](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103103411761.png)

![image-20221103103602477](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103103602477.png)

安装pstree

```linux
[root@hadoop100 ~]# yum install pstree
```

如果安装不上可用...尝试

```linux
[root@hadoop100 ~]# yum -y install psmisc
```

#### top

![image-20221103104210959](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103104210959.png)

#### netstat

![image-20221103132514114](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103132514114.png)

#### crontab

![image-20221103133415203](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103133415203.png)![image-20221103133627981](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103133627981.png)

![image-20221103133747104](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103133747104.png)

![image-20221103133915882](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103133915882.png)

```linux
[root@hadoop100 ~]# crontab -e
no crontab for root - using an empty one
crontab: installing new crontab
[root@hadoop100 ~]# ls
anaconda-ks.cfg       temp.tar.gz  公共  视频  文档  音乐
initial-setup-ks.cfg  xzhdx.txt    模板  图片  下载  桌面
[root@hadoop100 ~]# cat hello
hello world
[root@hadoop100 ~]# tail -f hello
hello world
hello world

```

![image-20221103134613748](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103134613748.png)

***

### 软件包管理

![image-20221103134803980](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103134803980.png)

 ![image-20221103134952106](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103134952106.png)

```linux
[root@hadoop100 ~]# rpm -qa |grep firefox
firefox-91.13.0-1.el7.centos.x86_64
[root@hadoop100 ~]# rpm -qi firefox
Name        : firefox
Version     : 91.13.0
Release     : 1.el7.centos
Architecture: x86_64
Install Date: 2022年11月03日 星期四 07时52分03秒
Group       : Unspecified
Size        : 275922442
License     : MPLv1.1 or GPLv2+ or LGPLv2+
Signature   : RSA/SHA256, 2022年09月02日 星期五 03时20分22秒, Key ID 24c6a8a7f4a80eb5
Source RPM  : firefox-91.13.0-1.el7.centos.src.rpm
Build Date  : 2022年09月01日 星期四 23时29分49秒
Build Host  : x86-01.bsys.centos.org
Relocations : (not relocatable)
Packager    : CentOS BuildSystem <http://bugs.centos.org>
Vendor      : CentOS
URL         : https://www.mozilla.org/firefox/
Summary     : Mozilla Firefox Web browser
Description :
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.
[root@hadoop100 ~]# 

```



![image-20221103135407106](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103135407106.png)

![image-20221103135452357](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103135452357.png)

![image-20221103135648247](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103135648247.png)

查看安装包：

```linux
[root@hadoop100 ~]# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
├─sda2   8:2    0    4G  0 part [SWAP]
└─sda3   8:3    0   15G  0 part /
sdb      8:16   0   20G  0 disk 
└─sdb1   8:17   0   20G  0 part 
sr0     11:0    1  4.4G  0 rom  /run/media/root/CentOS 7 x86_64
[root@hadoop100 ~]# cd /run/media/root/CentOS\ 7\ x86_64/
[root@hadoop100 CentOS 7 x86_64]# ls
CentOS_BuildTag  GPL       LiveOS    RPM-GPG-KEY-CentOS-7
EFI              images    Packages  RPM-GPG-KEY-CentOS-Testing-7
EULA             isolinux  repodata  TRANS.TBL

```

![image-20221103140132878](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103140132878.png)

![image-20221103140331282](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103140331282.png)

#### yum

![image-20221103160414399](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103160414399.png)

![image-20221103160520791](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103160520791.png)

![image-20221103160716876](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103160716876.png)

```linux
[root@hadoop100 Packages]# yum list |grep firefoc
[root@hadoop100 Packages]# yum list |grep firefox
firefox.x86_64                            91.13.0-1.el7.centos         @updates 
firefox.i686                              91.13.0-1.el7.centos         updates  
[root@hadoop100 Packages]# 

```

![image-20221103161330147](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103161330147.png)

```linux
[root@hadoop100 Packages]# less /etc/yum.repos.d/CentOS-Base.repo
```



![image-20221103161530193](C:\Users\时笙\AppData\Roaming\Typora\typora-user-images\image-20221103161530193.png)

克隆虚拟机（IP地址与主机名不能改）



