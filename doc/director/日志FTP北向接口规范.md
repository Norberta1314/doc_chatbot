# 日志FTP北向接口规范 
## 范围 
本规范定义了FTP日志北向接口，TECS Director向更高级别的vManager提供该接口。
本规范适用于TECS Director-vManager之间的交互设计。
## FTP日志北向接口规范 
### 日志北向对接方式 
TECS Director支持如下对接方式：
vManager 提供FTP服务，TECS Director作为FTP客户端按照一定的周期将日志文件上传到FTP服务器指定路径下。
### 日志北向配置 
日志北向对接支持界面自定义配置，具体配置的参数详解如下： 
开关： 打开或者关闭北向对接 
日志类型：可以选择操作日志、安全日志、运行日志一种或者多种上传到北向服务器 
发送周期：上传日志的周期，取值包含5分钟、10分钟、30分钟、60分钟、一天 
指定时间：当生成周期为1天的时候，每天执行上传动作的时间点 
日志备份语言：日志北向FTP文件的操作和安全日志的日志语言 
服务器类型：文件传输协议，支持FTP和SFTP 
服务器地址：FTP或者SFTP的服务器地址 
服务器端口：FTP或者SFTP的服务器端口 
用户名：FTP或者SFTP的服务器用户名 
密码：FTP或者SFTP的服务器密码 
路径：日志上传到服务器上的地址，是一个绝对路径，如果不填写就是登录到FTP服务器的默认路径 
### 日志文件传输协议 
支持使用FTP或SFTP协议传输文件。 
### 日志文件命名规则 
命名格式为 "logcategory_cloudName_subtype_time_num.zip"。 
logcategory：日志类型，取值为：OperationLog、SecurityLog、ProgramLog。 
cloudName：如果该日志文件是操作日志或者安全日志或者TECS Director的运行日志，cloudName取值为""，否则取值就是对接的云环境名称。 
subtype：如果该日志文件是操作日志或者安全日志，subtype取值为""，否则取值为enum（'Vim', 'HardwareLog', 'ContainerLog', 'ContainerAppLog'，'Director'） 
time：日志文件的日志的结束时间，是UTC时间格式。 
Num：日志文件的序号，如果一个周期内需要上传的日志量比较大，就会切割称多个文件，num即切割的文件序号。如果没有序号就是不需要切割。系统日志的考虑到日志量比较大，日志条目超过100000条就会另外生成新的文件。 
### 文件格式 
日志zip文件解压出来后是csv文件。 
数据第一行为字段名，每个字段以英文逗号“,”分隔。支持中文和英文，语言格式可以在【北向设置】中进行配置。 
第二行和下面几行是日志数据，每条记录占用一行，记录中的每个数据之间使用英文逗号“,”分隔。 
操作日志的字段有Log ID，App Module，Operation Name，Operation Resource，Resource Address，Level，Operation Result，User Name，Client Address，Operation Start Time，Operation End Time，Access Mode，Description Information，Detailed Information，Duration(S)，Fail Reason，Operation Object Type，Log Source，Project Name。字段说明如下：Log ID：日志标识App Module：日志模块Operation Name：操作名称，一般是操作的一个概述Operation Resource：操作对象Resource Address：操作对象地址，比如操作对象是虚机，就是虚机地址，一般操作日志不填写这个字段Level：日志级别，operlog_rank_normal表示普通，operlog_rank_notice表示注意，operlog_rank_important表示重要，operlog_rank_veryimportant表示非常重要Operation Result：操作结果，成功或者失败User Name：操作用户名Client Address：客户端地址Operation Start Time：操作开始时间，时间格式例如：2019-07-19T19:33:30+0800Operation End Time：操作结束时间，时间格式例如：2019-07-19T19:33:30+0800Access Mode：接入方式，取值WEB、SSHDescription Information：操作描述Detailed Information：操作详情Duration(S)：操作的持续时间，单位SFail Reason：操作失败的原因Operation Object Type：操作对象类型，可选Log Source：日志来源，如果来源是TECS Director上的，该字段不填，如果来源是provider的，字段填写为provider名称Project Name：租户信息，可选举例：字段：Log ID,App Module,Operation Name,Operation Resource,Resource Address,Level,Operation Result,User Name,Client Address,Operation Start Time,Operation End Time,Access Mode,Description Information,Detailed Information,Duration(S),Fail Reason,Operation Object Type,Log Source,Project Name举例1：161949535739937204,Log,Exportoperationlog,,,operlog_rank_notice,log_success,admin,10.68.21.166,2021-04-27T11:49:17+0000,2021-04-27T11:49:19+0000,WEB,Export operation log,,1.667,,,,举例2：161875667422617121,Intelligent Alarm,Create Alarm Related Action,,,operlog_rank_normal,log_success,admin,10.68.12.222,2021-04-18T22:37:52+0000,2021-04-18T22:37:52+0000,WEB,Create Alarm Related Action,,0.00,,Alarm Related Actions,, 
安全日志的字段有Log ID、Log Name、User Name、Level、Operation Time、Operation Result、Client Address、Access Mode、Detailed Information、Log Source、Project Name。字段说明如下：Log ID：日志标识Log Name：日志名称，一般是操作的一个概述User Name：操作用户名Level：日志级别，seclog_rank_normal、seclog_rank_notice、seclog_rank_important、seclog_rank_veryimportantOperation Time：操作时间，格式样例：2019-07-19T19:33:30+0800Operation Result：操作结果Client Address：客户端地址Access Mode：接入方式，取值WEB、SSHDetailed Information：日志详细信息Log Source：日志来源，如果来源是director上的，该字段不填，如果来源是provider的，字段填写为provider名称Project Name：租户信息，可选举例：字段：Log ID,Log Name,User Name,Level,Operation Time,Operation Result,Client Address,Access Mode,Detailed Information,Log Source,Project Name举例1：162424636697453808,Userlogin,admin,seclog_rank_normal,2021-06-21T11:32:46+0800,log_success,10.68.12.117,WEB,User login success,,举例2：162424596814784596,Session timeout,admin,seclog_rank_normal,2021-06-21T11:26:08+0800,log_success,10.68.21.166,WEB,"User name:admin,Login time:2021-06-21T10:04:59+08:00,Login duration:81 minutes,Idle duration:30 minutes,Last access time:2021-06-21T10:56:08+08:00",, 
系统日志的字段有index，HostName，time，LogCategory，Level, Log。字段说明如下：Index：序列号HostName：日志采集的来源主机名称time：日志入库的时间，时间格式为本地时间，时区是TECS Director服务器所在本地时间LogCategory：日志类型，SysLog_Iaas_ZTE_Director代表TECS Director日志、SysLog_Iaas_Pim代表硬件日志、SysLog_Paas_ZTE_Platform代表paas组件日志、SysLog_Paas_ZTE_OS代表pass平台的os日志、SysLog_Paas_Other_Application代表容器应用日志、以SysLog_Iaas_Other为开头的代表tecs的日志Level：日志级别，例如DEBUG、INFO、WARNNING、ERRORLog：日志原文举例：字段：index,HostName,time,LogCategory,Level,Log举例：1,paas-controller1,2021-06-08 13:23:23,SysLog_Iaas_ZTE_Director,INFO,"{""L"":""INFO"",""T"":""2021-06-08T21:22:55.854+0800"",""M"":""app cache are not ready, sleep 3s"",""module"":""appm-monitor""}" 
### 文件上传和生成周期 
文件上传周期：日志放入日志北向服务器的时间。在日志北向配置里面可以设置。 
文件生成周期：生成日志文件的周期。如果是操作日志和安全日志，文件生成周期就是文件上传周期；如果是系统日志，和日志量有关系，可能一个上传周期内会有多个文件生成。 
### 文件压缩 
文件压缩格式为zip文件。 
