# Pcf公共配置管理 
# Pcf公共配置管理 


[](None)背景知识 


部分配置需要被PCF网元的多个服务共同使用，为了避免重复配置，将这些配置作为公共配置列出。 




[](None)功能说明 


本功能用于管理可以被PCF网元的多个服务共同使用的配置。 




[](None)子主题： 






## 虚机服务信息 
## 虚机服务信息 


[](None)背景知识 


需要对PCF网元的每个虚机指定服务。 




[](None)功能说明 


本功能用于配置指定虚机上的服务信息。 




[](None)子主题： 






### 新增虚机服务信息(ADD VMSERVICEINFO) 
### 新增虚机服务信息(ADD VMSERVICEINFO) 


[](None)功能说明 

该命令用于增加在虚机上的服务信息。


[](None)注意事项 

无。 


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
index|标识|参数可选性: 必选参数类型: 字符串参数范围: 1-64|该参数用于唯一指定一个虚机服务配置记录的编号。
vm|虚机|参数可选性: 必选参数类型: 字符串参数范围: 1-64|该参数用于指定虚机的名称。可以通过执行SHOW VM命令查询虚机的名称。
servicefunction|服务功能|参数可选性: 必选参数类型: 字符串参数范围: 1-64|该参数表示在指定虚机上的服务功能。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
index|标识|参数可选性: 任选参数类型: 字符串参数范围: 1-64|该参数用于唯一指定一个虚机服务配置记录的编号。
vm|虚机|参数可选性: 任选参数类型: 字符串参数范围: 1-64|该参数表示根据指定标识查询到的虚机名称。
servicefunction|服务功能|参数可选性: 任选参数类型: 字符串参数范围: 1-64|该参数表示根据指定标识查询到的虚机上支持的服务功能名称。




[](None)命令举例 


`
增加一个虚机服务配置。在虚机"GSU0001"上增加"Npcf_SMPolicyControl_0"服务。
ADD VMSERVICEINFO:INDEX="1",VM="GSU0001",SERVICEFUNCTION="Npcf_SMPolicyControl_0"
` 


### 删除虚机服务信息(DEL VMSERVICEINFO) 
### 删除虚机服务信息(DEL VMSERVICEINFO) 


[](None)功能说明 

该命令用于删除指定的虚机服务信息。


[](None)注意事项 

无。 


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
index|标识|参数可选性: 必选参数类型: 字符串参数范围: 1-64|该参数用于唯一指定一个虚机服务配置记录的编号。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
index|标识|参数可选性: 任选参数类型: 字符串参数范围: 1-64|该参数用于唯一指定一个虚机服务配置记录的编号。




[](None)命令举例 


`
删除标识为1的虚机服务配置。
DEL VMSERVICEINFO:INDEX=1
` 


### 查询虚机服务信息(SHOW VMSERVICEINFO) 
### 查询虚机服务信息(SHOW VMSERVICEINFO) 


[](None)功能说明 

该命令用于查询指定或全部的虚机服务信息。


[](None)注意事项 

当需要查询指定的虚机服务信息时，必须输入标识参数；不指定标识时，表示查询全部的虚机服务信息。 


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
index|标识|参数可选性: 任选参数类型: 字符串参数范围: 1-64|该参数用于唯一指定一个虚机服务配置记录的编号。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
index|标识|参数可选性: 任选参数类型: 字符串参数范围: 1-64|该参数用于唯一指定一个虚机服务配置记录的编号。
vm|虚机|参数可选性: 任选参数类型: 字符串参数范围: 1-64|该参数表示根据指定标识查询到的虚机名称。
servicefunction|服务功能|参数可选性: 任选参数类型: 字符串参数范围: 1-64|该参数表示根据指定标识查询到的虚机上支持的服务功能名称。




[](None)命令举例 


`
查询标识为1的虚机服务配置信息。
SHOW VMSERVICEINFO:INDEX="1"

(No.5) : SHOW VMSERVICEINFO:
-----------------Npcf_SystemManagement_0----------------
操作维护       标识 虚机    服务功能               
---------------------------------------------------
复制 删除      1    GSU0001 Npcf_SMPolicyControl_0 
---------------------------------------------------
记录数：1
执行成功开始时间:2021-04-19 17:30:01 耗时: 1.269 秒

` 


# 专业维护 
# 专业维护 


[](None)背景知识 


为了方便对服务进行管理，RCP提供了专业维护功能。 




[](None)功能说明 


RCP提供专业维护方面的命令，包括内部统计查询，服务注册管理，容灾管理，CHR日志管理等命令。 

运维人员可以通过这些维护命令对当前服务进行相应功能操作。 




[](None)子主题： 






## Diameter信息管理 
## Diameter信息管理 


[](None)背景知识 


业务使用Diameter链路进行消息收发。 

为了了解Diameter链路的整体情况，需要提供相关的显示命令。 




[](None)功能说明 


RCP提供Diameter链路相关的如下信息的显示命令： 


 
Diameter维护模块的上电情况 

 
Diameter链路状态信息 

 
Diameter链路路由信息 

 
测试Diameter链路是否正常 

 
Diameter链路实例的信息 

 
Diameter链路所使用的承载层节点信息 

 
Diameter链路承载的配置和统计信息 

 
进行Diameter链路信息同步的节点信息 

 
各节点上Diameter链路信息同步库的情况 

 
指定节点上Diameter链路信息同步库的记录内容 

 
Diameter链路实例的详细信息 

 
链路维护模块上对同步库操作统计信息 

 
清除DAP的统计信息 

 
查看DIAMETER基础协议相关资源的使用情况 

 




[](None)子主题： 






### 查询Diameter系统状态(SHOW_DAPSYS) 
### 查询Diameter系统状态(SHOW_DAPSYS) 


[](None)功能说明 

该命令用于查询Diameter链路维护模块的上电信息。当链路全部断链时可以通过此命令查看链路维护模块是否处于主用正常态，如果不是则可以根据提供的信息判断是什么原因导致上电不正常。


[](None)注意事项 

无


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性: 必选参数类型: 字符串参数范围: 0-10000|Diameter链路维护模块的上电信息，可查询目前是否处于主用上电正常状态，以及是否发生过主备切换。




[](None)命令举例 


`
查询链路管理模块的上电情况。
SHOW_DAPSYS; 

(No.1) : SHOW_DAPSYS
-----------------Npcf_SystemManagement_0----------------
查询结果                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
0-master poweron 1-slave poweron 2-slave to master 3-master to slave 
4-check pcm status 5-get link info 6-slave normal 7-master normal 
current op (7) 
get dep status(4) 
  time (2021-03-24 13:57:50:296) 
   begintime(2021-03-24 13:57:50:296) 
  req times(2) 
   ack times(1) 
depsc status force enable(0) 
9  total num of link from depsc 
  time(2021-03-24 13:57:50:296) 
  current link 9  
  1 packs receive 
system state change record(4) 
  [0] state (0) time (2021-03-24 13:57:50:296) 
  [1] state (5) time (2021-03-24 13:57:50:296) 
  [2] state (4) time (2021-03-24 13:57:50:296) 
  [3] state (7) time (2021-03-24 13:57:50:296) 
 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1

` 


### 查询DIAMETER链路状态(SHOW DIMLNKSTAT) 
### 查询DIAMETER链路状态(SHOW DIMLNKSTAT) 


[](None)功能说明 

该命令用于查询所有Diameter链路的概要信息。维护人员在消息未正常收发、设备巡检等需要知道Diameter链路运行情况的场景下，使用该命令查询已经建链的Diameter链路号、链路状态、承载协议、链路角色。 


[](None)注意事项 


 
如果查询所有链路的状态信息，则不需要输入任何参数。 

 
如果查询某条链路的状态信息，则根据参数说明输入查询条件。 

 


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|参数作用：需要查询的Diameter链路的链路号，不输入时则查询所有链路信息。对于按Diameter链路配置生成的链路，此链路号通过ADD DIM RCPLINK定义后，才能进行有效查询。可通过执行SHOW DIM RCPLINK命令查询已配置的链路号。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，并且全局唯一。1~65535为静态链路的链路号，大于65535为动态链路的链路号。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|参数作用：需要查询的Diameter链路的链路号，不输入时则查询所有链路信息。对于按Diameter链路配置生成的链路，此链路号通过ADD DIM RCPLINK定义后，才能进行有效查询。可通过执行SHOW DIM RCPLINK命令查询已配置的链路号。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，并且全局唯一。1~65535为静态链路的链路号，大于65535为动态链路的链路号。
LINKSTATUS|链路状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-7|参数作用：该参数用于查看链路Diameter当前的状态。数据来源：根据链路实时变化。取值含义：Diameter链路的状态，包括：CONN_STATUS_ESTABLISHED（建链成功）：Diameter链路建链成功，能力协商成功，可用于Diameter消息传送。CONN_STATUS_UNSTABILE（链路断）：Diameter链路建链失败，不可用于Diameter消息传送。CONN_STATUS_REMOVED（逻辑移除）：Diameter链路在配置上已删除，处于拆除链路的状态，无法收发消息。CONN_STATUS_BLOCK_AVAILABLE（解闭塞）：Diameter链路处于从闭塞到解闭塞的过程中，无法收发消息。CONN_STATUS_BLOCK_UNAVAILABLE（闭塞）：Diameter链路已经闭塞，链路不可用，无法收发消息。CONN_STATUS_FAILOVER（失败替代）：Diameter链路处于不稳定的状态，收发消息会出现消息丢失的情况。CONN_STATUS_FAILBACK（失败倒回）：Diameter链路处于恢复到稳定的状态，可以正常收发消息。
SERVICEUSABLE|业务可用状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-7|参数作用：该参数用于指示该链路是否可以正常发送Diameter请求消息。数据来源：根据链路实时变化。配置原则：Diameter链路的业务可用状态包括：DEPLINK_STATUS_USABLE（可用）：该链路上可以发送Diameter请求消息。DEPLINK_STATUS_UNUSABLE（不可用）：该链路上不可以发送Diameter请求消息。
TRANSPORTPROTOCOL|承载协议|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 2-3|参数作用：该参数用于显示Diameter链路所用的承载协议。数据来源：与对端网元协商规划。配置原则：PROTOCOL_TYPE_TCP（TCP）：Diameter链路建立在TCP传输上，消息通过TCP链路传输。PROTOCOL_TYPE_SCTP（SCTP）：Diameter链路建立在SCTP偶联上，消息通过SCTP偶联传输。
LINKROLE|链路角色|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-3|参数作用：该参数用于显示Diameter链路的链路角色。数据来源：与对端网元协商规划。配置原则：指示该链路中本端是客户端还是服务端，包括：NODE_ROLE_SERVER（服务端）：本端是Diameter链路服务端，提供Diameter协议的服务。NODE_ROLE_CLIENT（客户端）：本端是Diameter链路客户端，可向服务端发送请求获取服务。NODE_ROLE_BOTH（既是服务端也是客户端）：本端既可以提供服务也可以发送请求获取服务。
RETCODE|结果|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于表示Diameter链路的查询结果。




[](None)命令举例 


`
查询Diameter链路的状态信息，链路号为1。
SHOW DIMLNKSTAT:LINKNO=1; 

(No.1) : SHOW DIMLNKSTAT:LINKNO=1
-----------------Npcf_SystemManagement_0----------------
链路号 链路状态 业务可用状态 承载协议 链路角色 
-----------------------------------------------
1      建链成功 可用         SCTP     服务端   
-----------------------------------------------
记录数：1

` 


### 查询DIAMETER路由信息(SHOW DIMRT) 
### 查询DIAMETER路由信息(SHOW DIMRT) 


[](None)功能说明 

该命令用于查询Diameter路由的详细信息，包括目的URI、支持的应用号、链路号、链路状态、路由优先级、路由类型、本地主机名、本地域名。当没有输入编号和应用标识时，则输出所有路由。


[](None)注意事项 

无


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ROUTENO|路由号|参数可选性: 任选参数类型: 数字|需要查询的Diameter路由号，不输入时查询所有Diameter路由信息。
SUPPORTAPPID|支持的应用标识|参数可选性: 任选参数类型: 数字|需要查询支持对应应用标识的路由，不输入时查询所有路由信息。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ROUTENO|路由号|参数可选性: 任选参数类型: 数字|链路号，1~32767为静态链路根据配置生成的路由，大于32767为动态链路根据配置生成的路由。
SUPPORTAPPID|支持的应用标识|参数可选性: 任选参数类型: 数字|显示该Diameter路由支持的应用。可选的应用有以下7种：COMMON：Diameter在线计费协议/离线计费协议。E4/Sp：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的签约消息的交互。Sp'：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的用量消息的交互。Rx：用于RCP和AF（Application Function，应用服务）的消息交互。Gx：用于RCP和PCEF（Policy and Charging Enforcement Function，策略与计费执行功能）的消息交互。Sy：用于RCP和OCS（Online Charging System，在线计费系统）的消息交互。Sd：用于RCP和TDF（Traffic Detection Function，业务检测功能）的消息交互。
DESTURI|目的URI|参数可选性: 任选参数类型: 字符串参数范围: 0-127|Diameter路由的目的URI。Diameter模块进行路由分析时，获取码流中Destination-Host AVP（没有则取Destination-Realm AVP）的内容，根据目的URI操作属性确定的匹配方式，与该参数进行匹配。如果二者匹配则选用本路由，否则不能使用本路由。目的URI必须符合FQDN格式要求。
LINKNO|链路号|参数可选性: 任选参数类型: 数字|Diameter路由关联的Diameter链路的编号。该参数引用DIAMETER链路配置（ADD DIM RCPLINK）中的链路号LINKNO。
ROUTEPRIORITY|优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于指定Diameter路由的优先级。当存在多条Diameter路由时，将依据优先级从高到低进行选路，如果出现未知优先级的Diameter路由需要查看系统是否运行正常。优先级有以下四种：低优先级（low）中优先级（nomal）高优先级（high）未知优先级（undefine）
ROUTELIFETIME|生命期(s)|参数可选性: 任选参数类型: 数字|生命期（此字段不再使用）
ROUTEORIGIN|路由类型|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于指定Diameter路由的来源，包括：静态（static）：来源于静态路由配置生成的路由，可通过SHOW DIM ROUTE命令查询。动态（dynamic）：来源于自动生成的路由，通过SHOW DIM ROUTE命令无法查到。未知（undefine）：来源不明。
LOCALHOST|本端主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|动态生成的Diameter路由对应Diameter链路的本端主机名，该参数引用DIAMETER链路配置（ADD DIM RCPLINK）中的本端主机名称LOCALHOSTNAME。静态配置生成的路由是路由条件中的条件值，该参数引用DIAMETER路由条件配置（ADD DIM ROUTECOND）中的条件值CONDITION。
LOCALREALM|本端域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|动态生成的Diameter路由的链路对应的本端域名，该参数引用DIAMETER链路配置（ADD DIM RCPLINK）中的本端主机名称LOCALREALMNAME。
SELFSVRNAME|服务名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|Diamete路由所在服务的服务名称。
RETCODE|结果|参数可选性: 任选参数类型: 枚举，参见枚举定义|Diameter路由的查询结果。




[](None)命令举例 


`
查询APPID为16777231的路由。
SHOW DIMRT:SUPPORTAPPID=16777231; 

(No.1) : SHOW DIMRT:SUPPORTAPPID=16777231
-----------------Npcf_SystemManagement_0----------------
结果 
-----
成功 
-----
记录数：1
路由号 支持的应用标识 目的URI    链路号 优先级   生命期(s) 路由类型 本端主机名 本端域名 服务名               
-------------------------------------------------------------------------------------------------------------
11     16777231       zte.com.cn 1      低优先级 0         静态                         Npcf_SMPolicyControl 
12     16777231       zte.com.cn 2      低优先级 0         静态                         Npcf_SMPolicyControl 
13     16777231       zte.com.cn 3      低优先级 0         静态                         Npcf_SMPolicyControl 
-------------------------------------------------------------------------------------------------------------
记录数：3

` 


### 测试DIAMETER链路状态(SHOW DIMLINKRESULT) 
### 测试DIAMETER链路状态(SHOW DIMLINKRESULT) 


[](None)功能说明 

该命令用于测试Diameter链路是否可用。本端会主动向对端发送一条DWR消息，收到对端回复的DWA消息即认为链路正常。


[](None)注意事项 

执行此命令前请先使用命令([SHOW DIMLNKSTAT](../mml/1137401.html))查询对应链路，并确认其为可用状态。


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 必选参数类型: 数字|需要测试的Diameter链路的链路号。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RETCODE|测试结果|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-12|Diameter链路的测试结果，包括：可达（success）：Diameter链路状态正常，发送DWR正常收到DWA。不可达(未收到dwa) （fail）：Diameter链路状态不正常，发送DWR没有收到DWA响应。未找到相应的链路 （not find link）：所要测试的链路不存在。时间间隔太短 （interval error）：前一次测试和本次测试之间间隔时间太短。参数错误（invalid param）：对于不支持心跳的链路进行测试。发送给DAP失败（send dap fail）：测试请求发往链路维护模块失败。动作不支持（not suppport action）：不支持对链路进行测试。缓冲区满（cache outbound）：在缓冲区的测试请求已满，无法接收新的测试请求。重复执行动作（duplite）：连续对同一链路进行测试。超时（timeout）：发往链路维护模块之后，一直没有反馈测试结果。链路处于断开状态（unstabile）：链路已经处于断链状态，无需进行测试。未找到相应的路由（not find route）：链路维护模块没有找到测试消息发往哪个SC。链路未被阻塞（unblocked）：Diameter链路处于未被阻塞的状态。
LINKNO|链路号|参数可选性: 任选参数类型: 数字|Diameter链路号，1~65535为静态链路的链路号，大于65535为动态链路的链路号。
LINKSTATUS|链路状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-7|Diameter链路的状态，包括：CONN_STATUS_ESTABLISHED（建链成功）：Diameter链路建链成功，能力协商成功，可用于Diameter消息传送。CONN_STATUS_UNSTABILE（链路断）：Diameter链路建链失败，不可用于Diameter消息传送。CONN_STATUS_REMOVED（逻辑移除）：Diameter链路在配置上已删除，处于拆除链路的状态，无法收发消息。CONN_STATUS_BLOCK_AVAILABLE（解闭塞）：Diameter链路处于从闭塞到解闭塞的过程中，无法收发消息。CONN_STATUS_BLOCK_UNAVAILABLE（闭塞）：Diameter链路已经闭塞，链路不可用，无法收发消息。CONN_STATUS_FAILOVER（失败替代）：Diameter链路处于不稳定的状态，收发消息会出现消息丢失的情况。CONN_STATUS_FAILBACK（失败倒回）：Diameter链路处于恢复到稳定的状态，可以正常收发消息。
TRANSPORTPROTOCOL|承载协议|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-3|Diameter链路所用的承载协议，包括：PROTOCOL_TYPE_TCP（TCP）：Diameter链路建立在TCP传输上，消息通过TCP链路传输。PROTOCOL_TYPE_SCTP（SCTP）：Diameter链路建立在SCTP偶联上，消息通过SCTP偶联传输。
LINKROLE|链路角色|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 2-3|Diameter链路的链路角色，指示该链路中本端是客户端还是服务端，包括：NODE_ROLE_SERVER（服务端）：本端是Diameter链路服务端，提供Diameter协议的服务。NODE_ROLE_CLIENT（客户端）：本端是Diameter链路客户端，可向服务端发送请求获取服务。NODE_ROLE_BOTH（既是服务端也是客户端）：本端既可以提供服务也可以发送请求获取服务。




[](None)命令举例 


`
测试Diameter链路1是否正常。
SHOW DIMLINKRESULT:LINKNO=1; 

(No.1) : SHOW DIMLINKRESULT:LINKNO=1
-----------------Npcf_SystemManagement_0----------------
链路号 
-------
1      
-------
记录数：1
链路角色 
---------
服务端   
---------
记录数：1
链路状态 
---------
建链成功 
---------
记录数：1
测试结果 
---------
可达     
---------
记录数：1
承载协议 
---------
SCTP     
---------
记录数：1

` 


### 查询DIAMETER链路实例信息(SHOW DIMINSTANCE) 
### 查询DIAMETER链路实例信息(SHOW DIMINSTANCE) 


[](None)功能说明 

该命令可查询所有Diameter链路的详细信息，包括链路的状态、链路对应的承载信息和链路的基本信息。当需要具体定位Diameter链路建链故障时，可使用本命令查询Diameter链路详细信息进行问题定位。


[](None)注意事项 

无


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|需要查询的Diameter链路的链路号，不输入时则查询所有链路信息。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|Diameter链路号，1~65535为静态链路的链路号，大于65535为动态链路的链路号。
LINKSTATUS|链路状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-7|Diameter链路的状态，包括：CONN_STATUS_ESTABLISHED（建链成功）：Diameter链路建链成功，能力协商成功，可用于Diameter消息传送。CONN_STATUS_UNSTABILE（链路断）：Diameter链路建链失败，不可用于Diameter消息传送。CONN_STATUS_REMOVED（逻辑移除）：Diameter链路在配置上已删除，处于拆除链路的状态，无法收发消息。CONN_STATUS_BLOCK_AVAILABLE（解闭塞）：Diameter链路处于从闭塞到解闭塞的过程中，无法收发消息。CONN_STATUS_BLOCK_UNAVAILABLE（闭塞）：Diameter链路已经闭塞，链路不可用，无法收发消息。CONN_STATUS_FAILOVER（失败替代）：Diameter链路处于不稳定的状态，收发消息会出现消息丢失的情况。CONN_STATUS_FAILBACK（失败倒回）：Diameter链路处于恢复到稳定的状态，可以正常收发消息。
TRANSPORTPROTOCOL|承载协议|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 2-3|Diameter链路所用的承载协议，包括：PROTOCOL_TYPE_TCP（TCP）：Diameter链路建立在TCP传输上，消息通过TCP链路传输。PROTOCOL_TYPE_SCTP（SCTP）：Diameter链路建立在SCTP偶联上，消息通过SCTP偶联传输。
TRANSPORTPROTOCOLID|承载协议ID|参数可选性: 任选参数类型: 数字|Diameter链路所用的承载链路对应的ID，用于指示Diameter链路建立在哪一条承载链路上。该参数引用DIAMETER链路配置（ADD DIM RCPLINK）中的字段SCTP/TCP承载链路。
LINKROLE|链路角色|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-3|Diameter链路的链路角色，指示该链路中本端是客户端还是服务端，包括：NODE_ROLE_SERVER（服务端）：本端是Diameter链路服务端，提供Diameter协议的服务。NODE_ROLE_CLIENT（客户端）：本端是Diameter链路客户端，可向服务端发送请求获取服务。NODE_ROLE_BOTH（既是服务端也是客户端）：本端既可以提供服务也可以发送请求获取服务。
LOCALHOST|本地主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|Diameter链路本端的主机名，本局在使用Diameter链路进行传输的组网中的标识名称。该参数引用DIAMETER链路配置（ADD DIM RCPLINK）中的的本端主机名称LOCALHOSTNAME。
LOCALREALM|本地域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|Diameter链路本端的域名，本局在使用Diameter链路进行传输的组网中的所处的区域范围的标识名称。该参数引用DIAMETER链路配置（ADD DIM RCPLINK）中的本端域名LOCALREALM。
REMOTEHOST|对端主机名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|Diameter链路对端的主机名，对端局在使用Diameter链路进行传输的组网中的标识名称。该参数引用DIAMETER链路配置（ADD DIM RCPLINK）中的对端主机名称DSTHOSTNAME。
REMOTEREALM|对端域名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|Diameter链路对端的域名，对端局在使用Diameter链路进行传输的组网中的所处的区域范围的标识名称。该参数引用DIAMETER链路配置（ADD DIM RCPLINK）中的对端域名DSTREALM。
LOCALIP|本端IP|参数可选性: 任选参数类型: 字符串参数范围: 0-160|此Diameter链路本端使用的IP地址，支持IPv4/IPv6建链。
LOCALPORT|本端端口|参数可选性: 任选参数类型: 数字参数范围: 0-65535|此Diameter链路本端使用的IP端口。
REMOTEIP|对端IP|参数可选性: 任选参数类型: 字符串参数范围: 0-160|此Diameter链路对端使用的IP地址，支持IPv4/IPv6建链。
REMOTEPORT|对端端口|参数可选性: 任选参数类型: 数字参数范围: 0-65535|此Diameter链路对端使用的IP端口。
APPID|应用ID|参数可选性: 任选参数类型: 字符串参数范围: 0-64|此Diameter链路所支持的应用能力ID。
RETCODE|结果|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|Diameter链路的查询结果。




[](None)命令举例 


`
查询1号链路实例的详细信息。
SHOW DIMINSTANCE:LINKNO=1; 

(No.1) : SHOW DIMINSTANCE:LINKNO=1
-----------------Npcf_SystemManagement_0----------------
链路号 链路状态 承载协议 承载协议ID 链路角色 本地主机名          本地域名        对端主机名           对端域名        本端IP    本端端口 对端IP    对端端口 应用ID     
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
1      建链成功 SCTP     1          服务端   rcp.hatt.zte.com.cn hatt.zte.com.cn pcef.hatt.zte.com.cn hatt.zte.com.cn 9.9.155.6 3890     9.9.155.4 3890     4294967295 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1

` 


### 查询DIAMETER SCTP节点(SHOW DIMSCTPNODE) 
### 查询DIAMETER SCTP节点(SHOW DIMSCTPNODE) 


[](None)功能说明 

该命令用于查询提供SCTP功能的SC实例的信息。当Diameter链路出现问题时，需要查看Diameter维护模块与SCTP偶联模块之间是否正常通信。可以使用该命令查询本NFS所有提供SCTP链路功能的SC实例，包括对应实例的VRU名称、SC逻辑号、COMMID以及实例节点的状态。


[](None)注意事项 

无


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
VRUNAME|VRU名称|参数可选性: 任选参数类型: 字符串参数范围: 1-64|SC实例对应的VRU名称，可用于确定其所在的容器。
SCLOGICNO|SC逻辑号|参数可选性: 任选参数类型: 数字|SC实例对应的SC逻辑号，可用于确定其所在的SC。
COMMID|CommID|参数可选性: 任选参数类型: 数字|SC实例的CommID，可用于查看Diameter链路维护模块发送消息的CommID是否包含SCTP功能。
NODESTATUS|节点状态|参数可选性: 任选参数类型: 枚举，参见枚举定义|SC实例的节点状态，可用于确认SC实例是否运行正常。normal（正常）：该SC实例运行正常。abnormal（不正常）：该SC实例运行不正常。
RETCODE|结果|参数可选性: 任选参数类型: 数字参数范围: 0-1|本NFS中提供SCTP功能的SC实例的查询结果。




[](None)命令举例 


`
查询本NFS中所有提供SCTP链路功能的SC实例。
SHOW DIMSCTPNODE; 

(No.1) : SHOW DIMSCTPNODE:
-----------------Npcf_SystemManagement_0----------------
VRU名称   SC逻辑号 CommID    节点状态 
--------------------------------------
vru-sig-0 1        100686849 1        
--------------------------------------
记录数：1

` 


### 查询DIAMETER承载信息(SHOW DIMTRANSINFO) 
### 查询DIAMETER承载信息(SHOW DIMTRANSINFO) 


[](None)功能说明 

该命令用于查询Diameter链路所使用承载的信息。当链路处于异常时或者维护人员需要查看链路上是否发生过异常，使用此命令查询Diameter链路对应的SCTP偶联的详细信息。包括承载的偶联ID、所在的VRU以及在此承载上交互的控制消息的统计。


[](None)注意事项 

无


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|需要查询的Diameter链路的链路号，不输入时则查询所有链路信息




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|Diameter链路号。
PROTOCOLID|SCTP偶联ID|参数可选性: 任选参数类型: 数字|承载Diameter链路消息的SCTP偶联号。
VRUNAME|VRU名称|参数可选性: 任选参数类型: 字符串参数范围: 0-64|偶联所在SCTP服务实例的VRU名称。
SNDSTARTREQTIMES|EV_SSM_StartReq发送次数|参数可选性: 任选参数类型: 数字|SCTP偶联的控制消息EV_SSM_StartReq的发送次数。EV_SSM_StartReq用于启动SCTP偶联。
SNDSTARTREQSUCCTIMES|EV_SSM_StartReq发送成功次数|参数可选性: 任选参数类型: 数字|SCTP偶联的控制消息EV_SSM_StartReq发送成功的次数。EV_SSM_StartReq用于启动SCTP偶联。
SNDSTATUSREQTIMES|EV_SSM_StatusReq发送次数|参数可选性: 任选参数类型: 数字|SCTP偶联的控制消息EV_SSM_StatusReq发送次数。EV_SSM_StatusReq用于查询SCTP偶联的状态。
SNDSTATUSREQSUCCTIMES|EV_SSM_StatusReq发送成功次数|参数可选性: 任选参数类型: 数字|SCTP偶联的控制消息EV_SSM_StatusReq发送成功的次数。EV_SSM_StatusReq用于查询SCTP偶联的状态。
SNDSTOPREQTIMES|EV_SSM_StopReq发送次数|参数可选性: 任选参数类型: 数字|SCTP偶联的控制消息EV_SSM_StopReq发送的次数。EV_SSM_StopReq用于停止SCTP偶联。
SNDSTOPREQSUCCTIMES|EV_SSM_StopReq发送成功次数|参数可选性: 任选参数类型: 数字|SCTP偶联的控制消息EV_SSM_StopReq发送成功的次数。EV_SSM_StopReq用于停止SCTP偶联。
RECVDATAINDEXTIMES|收到EV_SSM_DataIndEx次数|参数可选性: 任选参数类型: 数字|SCTP偶联收到数据消息EV_SSM_DataIndEx的次数。SCTP偶联会将链路上收到的EV_SSM_DataIndEx消息转发给Diameter链路维护模块。
RECVSTATUSACKTIMES|收到EV_SSM_StatusAck次数|参数可选性: 任选参数类型: 数字|SCTP偶联收到指示消息EV_SSM_StatusAck的次数。EV_SSM_StatusAck用于通知上层模块偶联当前的状态。
RECVINSINDTIMES|收到EV_SSM_InsInd次数|参数可选性: 任选参数类型: 数字|SCTP偶联收到指示消息EV_SSM_InsInd的次数。EV_SSM_InsInd用于指示偶联建立成功并将偶联参数通知上层模块。
RECVOOSINDTIMES|收到EV_SSM_OosInd次数|参数可选性: 任选参数类型: 数字|SCTP偶联收到指示消息EV_SSM_OosInd的次数。EV_SSM_OosInd用于偶联断链时通知上层模块。
RECVCGSTINDTIMES|收到EV_SSM_CgstInd次数|参数可选性: 任选参数类型: 数字|SCTP偶联收到指示消息EV_SSM_CgstInd的次数。EV_SSM_CgstInd用于指示偶联拥塞时通知上层模块。
RETCODE|结果|参数可选性: 任选参数类型: 数字参数范围: 0-1|Diameter链路的查询结果。




[](None)命令举例 


`
查询1号Diameter链路对应的承载情况。
SHOW DIMTRANSINFO:LINKNO=1; 

(No.1) : SHOW DIMTRANSINFO:LINKNO=1
-----------------Npcf_SystemManagement_0----------------
链路号 SCTP偶联ID VRU名称 EV_SSM_StartReq发送次数 EV_SSM_StartReq发送成功次数 EV_SSM_StatusReq发送次数 EV_SSM_StatusReq发送成功次数 EV_SSM_StopReq发送次数 EV_SSM_StopReq发送成功次数 收到EV_SSM_DataIndEx次数 收到EV_SSM_StatusAck次数 收到EV_SSM_InsInd次数 收到EV_SSM_OosInd次数 收到EV_SSM_CgstInd次数 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1      1                  180                     180                         68003                    0                            0                      0                          0                        68003                    10                    6                     0                      
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1

` 


### 查询DIAMETER链路详细信息(SHOW DIMINSTANCEDETAIL) 
### 查询DIAMETER链路详细信息(SHOW DIMINSTANCEDETAIL) 


[](None)功能说明 

该命令用于查询Diameter链路维护消息的配置和统计信息，包括Diameter链路当前状态、Diameter层的配置和基础消息的统计信息。
当Diameter链路出现故障时，使用该命令查询维护信息是否处理正常。
维护信息处理正常的情况下，Diameter链路建立时，通过CER/CEA消息进行能力协商；Diameter链路空闲时，通过心跳消息（DWR/DWA）定时检测链路是否正常。


[](None)注意事项 

无


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|需要查询的Diameter链路号，不输入时则查询所有Diameter链路信息。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|Diameter链路号。
LINKSTATUS|链路状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-7|Diameter链路状态。链路建立（1）：链路建链成功，该链路上可以发送Diameter请求消息。链路断链（2）：链路已断，该链路上无法接收和发送Diameter消息。链路FAILOVER（6）：链路出现不稳定状态，该链路上不可以发送Diameter请求消息。链路FAILBACK（7）：链路从不稳定状态恢复正常，该链路上不可以发送Diameter请求消息。
MOTHERLINKID|主链路号|参数可选性: 任选参数类型: 数字|动态链路是在静态链路基础上生成的链路，主链路号为其对应的静态链路的链路号。静态链路是通过网管配置的链路，没有主链路号（显示为无效值4294967295）。
HBSWITCH|心跳开关|参数可选性: 任选参数类型: 数字|每条链路均可通过该参数来开启或者关闭心跳机制，此开关开启本端定时检测链路状态。
HBCYCLE|心跳周期|参数可选性: 任选参数类型: 数字|“心跳开关”开启时，本端定时检测链路状态的时长。
HBTIMES|心跳次数|参数可选性: 任选参数类型: 数字|“心跳开关”开启时，本端连续若干心跳周期未收到对端的心跳消息DWR或者本端的心跳消息没有收到响应，需要关闭Diameter链路重新建链。心跳次数指示连续发生的心跳周期的个数。
CURHBTIME|当前心跳时间|参数可选性: 任选参数类型: 数字|指示当前一个心跳周期内，本端从当前时间开始等待多少秒发送DWR消息。
CURHBTIMES|当前心跳失败次数|参数可选性: 任选参数类型: 数字|当前已经发生的连续的心跳失败次数，即本端已发送心跳DWR没有收到响应的次数。失败次数超过链路配置的心跳次数，偶联和Diameter链路均会断链重建。
RCVCERTIMES|接收CER次数|参数可选性: 任选参数类型: 数字|本端接收到对端发送的能力协商请求CER次数。
SNDCEATIMES|发送CEA次数|参数可选性: 任选参数类型: 数字|本端发送给对端的能力协商响应CEA次数。
SNDCERTIMES|发送CER次数|参数可选性: 任选参数类型: 数字|本端发送给对端的能力协商请求CER次数。
RCVCEATIMES|接收CEA次数|参数可选性: 任选参数类型: 数字|本端接收到对端发送的能力协商响应CEA次数。
RCVDWRTIMES|接收DWR次数|参数可选性: 任选参数类型: 数字|本端接收到对端发送的心跳请求DWR次数。
SNDDWATIMES|发送DWA次数|参数可选性: 任选参数类型: 数字|本端发送给对端的心跳响应DWA次数。
SNDDWRTIMES|发送DWR次数|参数可选性: 任选参数类型: 数字|本端发送给对端的心跳请求DWR次数。
RCVDWATIMES|接收DWA次数|参数可选性: 任选参数类型: 数字|本端接收到对端发送的心跳响应DWA次数。
RETCODE|结果|参数可选性: 任选参数类型: 数字参数范围: 0-1|查询Diameter链路结果。




[](None)命令举例 


`
查询1号Diameter链路的Diameter详细信息。
SHOW DIMTRANSINFO:LINKNO=1; 

(No.1) : SHOW DIMINSTANCEDETAIL:LINKNO=1
-----------------Npcf_SystemManagement_0----------------
链路号 链路状态 主链路号   心跳开关 心跳周期 心跳次数 当前心跳时间 当前心跳失败次数 接收CER次数 发送CEA次数 发送CER次数 接收CEA次数 接收DWR次数 发送DWA次数 发送DWR次数 接收DWA次数 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1      建链成功 4294967295 0        30       0        0            0                0           0           0           4           150984      150984      55          53          
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1

` 


### 查询DIAMETER链路状态同步表操作次数(SHOW DIMUSYNCOP) 
### 查询DIAMETER链路状态同步表操作次数(SHOW DIMUSYNCOP) 


[](None)功能说明 

该命令用于查询Diameter维护模块变更Diameter同步记录的信息。当Diameter链路出现收发消息异常时，确认各同步节点数据是否一致，可使用该命令查询在链路管理节点上Diameter链路状态同步表的操作次数。


[](None)注意事项 

无


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
INSDATTIMES|插入数据次数|参数可选性: 任选参数类型: 数字|Diameter链路管理实例向同步库中的Diameter链路状态表中插入数据的次数。
INSDATSUCCTIMES|插入数据成功次数|参数可选性: 任选参数类型: 数字|Diameter链路管理实例向同步库中的Diameter链路状态表中插入数据的成功次数。
UPDDATTIMES|更新数据次数|参数可选性: 任选参数类型: 数字|更新同步库中的Diameter链路状态表中数据的次数。
UPDDATSUCCTIMES|更新数据成功次数|参数可选性: 任选参数类型: 数字|更新同步库中的Diameter链路状态表中数据的成功次数。
DELDATTIMES|删除数据次数|参数可选性: 任选参数类型: 数字|删除同步库中的Diameter链路状态表中数据的次数。
DELDATSUCCTIMES|删除数据成功次数|参数可选性: 任选参数类型: 数字|删除同步库中的Diameter链路状态表中数据的成功次数。
RETCODE|结果|参数可选性: 任选参数类型: 数字参数范围: 0-1|同步库的操作统计信息的查询结果。




[](None)命令举例 


`
查询在链路管理节点上数据处理的次数。
SHOW DIMUSYNCOP 

(No.1) : SHOW DIMUSYNCOP:
-----------------Npcf_SystemManagement_0----------------
删除数据成功次数 
-----------------
4                
-----------------
记录数：1
删除数据次数 
-------------
4            
-------------
记录数：1
插入数据成功次数 
-----------------
10795            
-----------------
记录数：1
插入数据次数 
-------------
10795        
-------------
记录数：1
结果 
-----
0    
-----
记录数：1
更新数据成功次数 
-----------------
128              
-----------------
记录数：1
更新数据次数 
-------------
128          
-------------
记录数：1

` 


### 清除DAP统计(CLEAR DAPSTAT) 
### 清除DAP统计(CLEAR DAPSTAT) 


[](None)功能说明 

该命令用于清除链路管理相关的所有统计信息，将统计信息全部清零。当维护人员想获取下一阶段的统计信息时，可以执行此命令。


[](None)注意事项 

无


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性: 任选参数类型: 数字|需要清除统计信息的Diameter链路的链路号，不输入时则清除所有链路的统计信息。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性: 任选参数类型: 字符串参数范围: 0-100|指示清除统计信息的结果。




[](None)命令举例 


`
清除所有链路管理的统计信息。
CLEAR DAPSTAT:

(No.1) : CLEAR DAPSTAT:
-----------------Npcf_SystemManagement_0----------------
操作结果                  
--------------------------
Clear Dap Statics Success 
--------------------------
记录数：1

` 


### 查询DAP资源的使用情况(SHOW_DAPDATA_STAT) 
### 查询DAP资源的使用情况(SHOW_DAPDATA_STAT) 


[](None)功能说明 

该命令用于查询DAP数据区的使用情况。当出现DIAMETER负荷容量告警时，可以执行该命令查询各DAP数据区的使用情况。


[](None)注意事项 

无


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SCNO|SC编号|参数可选性: 必选参数类型: 数字|该参数表示运行DAP数据区的SC实例的逻辑编号。
RESNAME|数据区名|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数表示统计的数据区对应的名称。
SUM|总数|参数可选性: 必选参数类型: 数字|该参数表示在对应SC上此数据区的总个数。
USAGE|占用数|参数可选性: 必选参数类型: 数字|该参数表示在对应SC上此数据区的当前使用个数。
PEAK|占用峰值|参数可选性: 必选参数类型: 数字|该参数表示在对应SC上此数据区上电以来最高的占用值。
PERCENT|占用百分比|参数可选性: 必选参数类型: 数字参数范围: 0-100|该参数表示在对应SC上此数据区使用个数占总个数的百分比。
RETCODE|结果|参数可选性: 任选参数类型: 数字参数范围: 0-1|该参数表示DAP资源使用情况的查询结果。




[](None)命令举例 


`
查询DAP数据区的使用情况。

(No.1) : SHOW_DAPDATA_STAT:
-----------------Npcf_SystemManagement_0----------------
SC编号 数据区名     总数 占用数 占用峰值 占用百分比 
----------------------------------------------------
1003   DAP_TRANS    1024 14     14       1          
1003   DAP_INSTANCE 1024 14     14       1          
1003   DAP_USYNC    2048 14     14       0          
----------------------------------------------------
记录数：3
结果 
-----
0    
-----
记录数：1

` 


# 操作维护 
# 操作维护 


[](None)背景知识 


平台提供的调试命令集合。 




[](None)功能说明 


该节点下面包括系统调测配置。 




[](None)子主题： 






## 系统调测 
## 系统调测 


[](None)背景知识 


对系统进行调试和信息收集，以判断运行状况。 




[](None)功能说明 


对系统进行调试和信息收集，包括调测信息收集等功能。 




[](None)子主题： 






### 调测信息收集 
### 调测信息收集 


[](None)背景知识 


在系统调试过程中，需要采集系统的运行信息，可提供给运维人员进行分析，达到监测系统是否正常的目的。 




[](None)功能说明 


本配置可以显示系统当前支持的所有模块，可针对模块名进行信息采集，也可以采集系统所有模块的信息，同时具备清除模块信息的功能。 




[](None)子主题： 






#### 查询含有Debug信息的模块列表(SHOW DEBUG MODULELIST) 
#### 查询含有Debug信息的模块列表(SHOW DEBUG MODULELIST) 


[](None)功能说明 

该命令用于查询其归属的NFS内含有调测信息的模块列表。当运维人员需要收集或者清除指定模块的调试信息时，可以执行该命令查询含有调测信息的模块名称。 


[](None)注意事项 

无。 


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MODULE_NAME|模块名|参数可选性: 必选参数类型: 字符串参数范围: 1-47|该参数用于表示支持统计信息的模块名称。
MODULE_INST|模块实例数|参数可选性: 必选参数类型: 数字参数范围: 0-4294967295|该参数用于表示支持统计信息的模块实例数。




[](None)命令举例 


`
查询某个NFS中含有调试统计信息的模块列表。
 SHOW DEBUG MODULELIST

------CommonS_TMSP_0--------
模块名         模块实例数
ROSNG_ADAPT    1
ROSNG_ARCH     1
记录数：2

执行成功耗时: 0.259 秒

` 


#### 清理模块内部统计信息(CLEAR DEBUG INFO) 
#### 清理模块内部统计信息(CLEAR DEBUG INFO) 


[](None)功能说明 

该命令用于清理其归属NFS内模块的调测信息。当需要获取新的调测信息前，先执行该命令。 


[](None)注意事项 

获取新的调测信息前可以先执行该命令，该命令返回的“失败数量”为非0则需要联系中兴通讯技术人员支持；为0则可获取新的调测信息。 


[](None)输入参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MODULE_NAME|模块名称|参数可选性: 任选参数类型: 字符串参数范围: 1-47|该参数用于表示需要清除调测信息的模块名称。该参数选项的含义是：默认为空：表示清除NFS内所有的调测信息。非空：表示清除指定模块的调测信息，可由SHOW DEBUG MODULELIST命令获取模块名称。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MODULE_NUMBER|模块实例数量|参数可选性: 必选参数类型: 数字参数范围: 0-4294967295|该参数用于表示清理的模块实例总数量。
SUCCESS_NUMBER|成功数量|参数可选性: 必选参数类型: 数字参数范围: 0-4294967295|该参数用于表示清理成功的模块实例数量。
FAILED_NUMBER|失败数量|参数可选性: 必选参数类型: 数字参数范围: 0-4294967295|该参数用于表示清理失败的模块实例数量。




[](None)命令举例 


`
清理名称为ROSNG_ADAPT的模块的调测信息。

CLEAR DEBUG INFO:MODULE_NAME="ROSNG_ADAPT"
` 


