动态管理 动态管理 

[](None)背景知识 


动态管理即动态数据管理，是设备维护中的一个重要组成模块，完成对网元某些关键资源（如信令链路、路由局向等）的状态查询和管理控制（如激活、去活、闭塞和解闭塞等），为整个系统的调试和系统管理提供了必要的技术手段。 




[](None)功能描述 


动态管理即动态数据管理，完成对网元某些关键资源的状态查询和管理控制,动态管理实现以下功能： 



 
静态查询：通过网管与网元进行交互，获取网元设备资源当前的动态信息。 

 
动态监视：网元对监视对象的动态数据实时监控，当动态数据发生变化时，网元将变更结果实时上报后台，网管实时呈现。 

 
动态操作：通过网管与网元进行交互，对网元动态资源进行各种操作如激活/去激活、闭塞/解闭塞、停止/启动等。 

 




[](None)相关主题 



 

GTP节点管理
 

 

RNC动态管理
 

 

eNodeB动态管理
 

 

MCE动态管理
 

 

GB口动态管理
 

 

负荷动态管理
 

 

用户动态管理
 

 

DNS相关
 

 

Diameter管理
 

 

SGs管理
 

 

计费管理
 

 

S102局向管理
 

 

KPI监控人工操作
 

 

用量和KPI查询
 

 

TCE跟踪管理
 

 

MME信令风暴抑制管理
 

 

SGSN信令风暴抑制管理
 

 

PGW拥塞管理
 

 

网元过负荷控制
 

 

ACL规则管理
 

 

EMS PLUS状态管理
 

 

调测信息采集
 

 

多进程查询
 

 












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## GTP节点管理 
## GTP节点管理 


[](None)背景知识 

            
            节点信息是指与本网元相连的周边网元的信息，包括GGSN/SGSN/MME/SGW。本网元没有周边的网元的配置信息，而且这些网元是否与本网元有交互都是动态的。
        


[](None)功能描述 

            
            由于与uMAC相连的周边网元信息是动态的，操作人员可以通过节点信息查询得到与本网元存在GTP消息交互的全部邻接GSN（GGSN/SGSN/MME/SGW）的信息。
        


[](None)相关主题 



 

显示全部可达节点(SHOW ALL REACHABLE NODES)
 

 

显示全部不可达节点(SHOW ALL UNREACHABLE NODES)
 

 

显示指定GTP节点(SHOW NODE)
 

 

删除不可达节点(DELETE UNREACHABLE NODE)
 

 

显示全部不可达SGW-PGW节点对(SHOW ALL UNREACHABLE GW NODES)
 

 

显示指定SGW-PGW节点对(SHOW GW NODES)
 

 

删除不可达SGW-PGW节点对(DELETE UNREACHABLE GW NODE)
 

 

查询S10口对端MME地址(SHOW S10 FAR ADDR)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 显示全部节点(SHOW ALL REACHABLE NODES) 
### 显示全部节点(SHOW ALL REACHABLE NODES) 


[](None)命令功能 

该命令用于查询与本网元存在GTP消息交互的全部邻接GSN网元（包括GGSN、SGSN、MME和SGW）的信息。


[](None)注意事项 

此功能适用于SGSN和MME网元。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
INDEX|节点序号|参数可选性:任选参数；参数类型:整数。|表示对端GSN网元的编号。
GSNTYPE|节点类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对端可达GSN网元的类型，包括：GGSN、SGSN、SGW、S11-U SGW、MME和MSC。
GSNSIGIP|对端节点信令GsnIP地址|参数可选性:任选参数；参数类型:字符型。|表示对端GSN网元的IP地址类型及地址信息。
VERSION|版本号|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对端GSN网元支持的GTP版本。取值含义如下：“GTPV0”：GTP版本0。“GTPV1”：GTP版本1。“GTPV2”：GTP版本2。
RECOVERY|重启次数|参数可选性:任选参数；参数类型:整数。|表示对端网元重启的次数。
PATHDELAYSTATUS|路径延迟检测状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|标识对端是否处于路径延迟检测状态。






[](None)命令举例 


查询与本网元相关的所有GSN节点信息。 


SHOW ALL REACHABLE NODES; 


`

命令 (No.1): SHOW ALL REACHABLE NODES

节点序号   节点类型       对端节点信令GsnIP地址   版本号   重启次数
-------------------------------------------------------------------
1          SGW            IPv4: 192.20.104.96     GTPV2    16
2          GGSN           IPv4: 192.20.104.196    GTPV1    15
-------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.04 秒）。
` 








父主题： [GTP节点管理](../../zh-CN/tree/N_130840043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 显示全部不可达节点(SHOW ALL UNREACHABLE NODES) 
### 显示全部不可达节点(SHOW ALL UNREACHABLE NODES) 


[](None)命令功能 

该命令用于查询全部不可达邻接GSN网元（包括GGSN、SGSN、SGW、MME和MSC）的信息。


[](None)注意事项 

此功能适用于SGSN和MME网元。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
INDEX|节点序号|参数可选性:任选参数；参数类型:整数。|表示对端GSN网元的编号。
GSNTYPE|节点类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对端不可达GSN网元的类型，包括：GGSN、SGSN、SGW、MME和MSC。
GSNSIGIP|对端节点信令GsnIP地址|参数可选性:任选参数；参数类型:字符型。|表示对端GSN网元的IP地址类型及地址信息。
VERSION|版本号|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对端GSN网元支持的GTP版本。取值含义如下：“GTPV0”：GTP版本0。“GTPV1”：GTP版本1。“GTPV2”：GTP版本2。






[](None)命令举例 


查询与本网元存在GTP消息交互的全部不可达邻接GTP节点（包括GGSN、SGSN、SGW、MME和MSC）的信息。 


SHOW ALL UNREACHABLE NODES; 


`

命令 (No.1): SHOW ALL UNREACHABLE NODES;

节点序号    节点类型          对端节点信令GsnIP地址   版本号   
-----------------------------------------------------------
1           Combo MME/SGSN    IPv4: 192.20.104.96     GTPV2   
2           Combo MME/SGSN    IPv4: 192.20.104.196    GTPV1   
-----------------------------------------------------------
记录数 2

命令执行成功（耗时 0.04 秒）。
` 








父主题： [GTP节点管理](../../zh-CN/tree/N_130840043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 显示路径或IP索引节点(SHOW NODE) 
### 显示路径或IP索引节点(SHOW NODE) 


[](None)命令功能 

此命令用于根据GSN网元的“路径索引”或IP地址查询与本网元存在GTP消息交互的特定邻接GSN网元（包括GGSN、SGSN、MME和SGW）的信息。


[](None)注意事项 


当“路径管理类型”设置为“路径索引”时，本网元根据路径索引号进行查询，路径索引号为[SHOW ALL REACHABLE NODES](1263000.html)命令显示的查询结果中的”节点序号“。


当“路径管理类型”设置为“IP索引”时，本网元按照对端网元的IP地址进行查询。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|路径管理类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PATH INDEX。|表示用于根据GSN网元的“路径索引”或IP地址查询与本网元存在GTP消息交互的特定邻接GSN网元（包括GGSN、SGSN、MME和SGW）的信息，取值含义如下：当“路径管理类型”设置为“路径索引”时，本网元根据路径索引号进行查询，路径索引号为SHOW ALL REACHABLE NODES命令显示的查询结果中的”节点序号“。当“路径管理类型”设置为“IP索引”时，本网元按照对端网元的IP地址进行查询。
INDEX|节点序号/IP地址|参数可选性:必选参数；参数类型:字符型。|表示对端GSN网元的编号或IP地址。当“路径管理类型”设置为“路径索引”时，此参数设置为对端GSN网元的编号，取值为SHOW ALL REACHABLE NODES命令显示的查询结果中的”节点序号“。当“路径管理类型”设置为“IP索引”时，此参数设置为对端网元的IP地址。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示本次操作的结果。
INDEX|节点序号|参数可选性:任选参数；参数类型:整数。|表示对端GSN网元的编号。
GSNTYPE|节点类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对端可达GSN网元的类型，包括：GGSN、SGSN、SGW、S11-U SGW、MME和MSC。
GSNSTATE|节点状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对端GSN网元的状态，分为可达和不可达两种状态。
GSNSIGIP|对端节点信令GsnIP地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|表示对端GSN网元的IP地址类型及地址信息。
VERSION|版本号|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对端GSN网元支持的GTP版本。取值含义如下：“GTPV0”：GTP版本0。“GTPV1”：GTP版本1。“GTPV2”：GTP版本2。
RECOVERY|重启次数|参数可选性:任选参数；参数类型:整数。|表示对端网元重启的次数。
PATHDELAYSTATUS|路径延迟检测状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|标识对端是否处于路径延迟检测状态。






[](None)命令举例 


查询路径索引为1的GSN节点信息。 


SHOW NODE:TYPE="PATH INDEX",INDEX="1"; 


`

命令 (No.1): SHOW NODE:TYPE="PATH INDEX",INDEX="1";

查询结果 
-----------
成功 
-----------
记录数 1

节点信息
节点序号     节点类型  节点状态  对端节点信令GsnIP地址   版本号   重启次数
-------------------------------------------------------------------------
1            SGW       可达      IPv4: 192.20.104.96     GTPV2    16
-------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [GTP节点管理](../../zh-CN/tree/N_130840043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除不可达节点(DELETE UNREACHABLE NODE) 
### 删除不可达节点(DELETE UNREACHABLE NODE) 


[](None)命令功能 


路由修改或配置错误等人为造成SGW/GGSN/MME/SGSN/MSC节点不可达，维护人员修改路由或配置后这些节点会立即修复，运营商希望人工查询到这类不可达节点并快速恢复这类告警的GTP节点。维护人员通过该命令删除这类不可达GTP节点，快速恢复这类告警的GTP节点。 




[](None)注意事项 

此功能适用于SGSN和MME网元。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GSNTYPE|节点类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|表示要删除的对端GSN网元的类型，包括：GGSN、SGSN、SGW、MME和MSC。
TYPE|节点删除类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:。|表示节点删除方式，有3种方式：删除该GTP节点类型的所有不可达节点。删除指定节点序号的不可达节点。删除指定IP地址的不可达节点。
INDEX|节点序号/IP地址|参数可选性:任选参数；参数类型:字符型。|表示要删除的对端GSN网元的编号，当“节点删除类型”设置为“删除指定节点序号的不可达节点”时，该参数需要设置节点序号；表示要删除的对端GSN网元的IP地址，当“节点删除类型”设置为“删除指定IP地址的不可达节点”时，该参数需要设置节点IP地址。






[](None)命令举例 


删除所有不可达节点。 


DELETE UNREACHABLE NODE:GSNTYPE="GGSN",TYPE="ALL_IDX"; 








父主题： [GTP节点管理](../../zh-CN/tree/N_130840043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 显示全部不可达SGW-PGW节点对(SHOW ALL UNREACHABLE GW NODES) 
### 显示全部不可达SGW-PGW节点对(SHOW ALL UNREACHABLE GW NODES) 


[](None)命令功能 

该命令用于查询全部不可达SGW-PGW节点对信息。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
INDEX|节点序号|参数可选性:任选参数；参数类型:整数。|表示对端SGW-PGW网元节点对的编号。
PGWIPADDR|PGW节点IP地址|参数可选性:任选参数；参数类型:字符型。|表示PGW网元的IP地址类型及地址信息。
SGWIPADDR|SGW节点IP地址|参数可选性:任选参数；参数类型:字符型。|表示SGW网元的IP地址类型及地址信息。






[](None)命令举例 


查询所有不可达SGW-PGW节点对信息。 


SHOW ALL UNREACHABLE GW NODES; 


`

命令 (No.1): SHOW ALL UNREACHABLE GW NODES;

节点序号   对端节点信令GsnIP地址   版本号   路径状态       重启次数
-------------------------------------------------------------------
1          IPv4: 192.20.104.96     GTPV2    路径稳定状态   16
2          IPv4: 192.20.104.196    GTPV1    路径稳定状态   15
-------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.04 秒）。
` 








父主题： [GTP节点管理](../../zh-CN/tree/N_130840043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 显示指定SGW-PGW节点对(SHOW GW NODES) 
### 显示指定SGW-PGW节点对(SHOW GW NODES) 


[](None)命令功能 


此命令用于根据SGW-PGW节点对的“路径索引”或SGW-PGW节点对IP地址或SGW、PGW其中一个IP地址查询特定SGW-PGW节点对的信息。 




[](None)注意事项 



 
当“路径管理类型”设置为“路径索引”时，本网元根据路径索引号进行查询，只可以查询不可达节点对，路径索引号为SHOW ALL UNREACHABLE GW NODES命令显示的查询结果中的“节点序号”。
 

 
当“路径管理类型”设置为“IP索引”时，本网元按照的SGW-PGW节点对IP地址或SGW、PGW其中一个IP地址进行查询，可以查询可达节点对，也可以查询不可达节点对。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|节点查询类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:。|表示节点查询方式，有4种方式：查询指定路径索引的不可达SGW-PGW节点对。查询指定IP地址的SGW-PGW节点对，该节点对的状态是可达或未知，因为MME只记录不可达SGW-PGW节点对。查询指定SGW对应的所有不可达SGW-PGW节点对。查询指定PGW对应的所有不可达SGW-PGW节点对。
INDEX|节点序号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4096。|表示指定的对端SGW-PGW网元节点对的编号。
PGWIPADDR|PGW节点IP地址|参数可选性:任选参数；参数类型:字符型。|表示指定PGW网元的IP地址类型及地址信息。
SGWIPADDR|SGW节点IP地址|参数可选性:任选参数；参数类型:字符型。|表示指定SGW网元的IP地址类型及地址信息。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
INDEX|节点序号|参数可选性:任选参数；参数类型:整数。|表示指定的对端SGW-PGW网元节点对的编号。
PGWIPADDR|PGW节点IP地址|参数可选性:任选参数；参数类型:字符型。|表示指定PGW网元的IP地址类型及地址信息。
SGWIPADDR|SGW节点IP地址|参数可选性:任选参数；参数类型:字符型。|表示指定SGW网元的IP地址类型及地址信息。
GWGSNSTATE|节点状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示指定的对端SGW-PGW网元节点对的状态，分为可达和未知两种状态






[](None)命令举例 


根据节点序号为537来查询SGW-PGW节点对。 


SHOW GW NODES:TYPE="SpecifyPathIndexUnreachableNode",INDEX=537; 


`

命令 (No.1): SHOW GW NODES:TYPE="SpecifyPathIndexUnreachableNode",INDEX=537;

节点序号   PGW节点IP地址                                   SGW节点IP地址    节点状态
-------------------------------------------------------------------------------------------
537       IPv6: 2017:0000:0000:0000:0000:0000:0000:0006   IPv4: 3.1.1.6    不可达
-------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.04 秒）。
` 








父主题： [GTP节点管理](../../zh-CN/tree/N_130840043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除不可达SGW-PGW节点对(DELETE UNREACHABLE GW NODE) 
### 删除不可达SGW-PGW节点对(DELETE UNREACHABLE GW NODE) 


[](None)命令功能 

该命令用于删除不可达的SGW-PGW节点对。SGW和PGW之间的链路会存在瞬断，如果希望人工查询到这类不可达的节点对并快速恢复这类不可达的节点对的告警时，维护人员通过该命令删除这类不可达SGW-PGW节点对，以便快速恢复这些不可达的节点对。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|节点删除类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:。|表示节点删除方式，有5种方式：删除所有不可达SGW-PGW节点对。删除指定路径索引的不可达SGW-PGW节点对。删除指定IP地址的不可达SGW-PGW节点对。删除指定SGW对应的所有不可达SGW-PGW节点对。删除指定PGW对应的所有不可达SGW-PGW节点对。
INDEX|节点序号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4096。|表示要删除的SGW-PGW节点对的编号，当“节点删除类型”设置为“指定不可达SGW-PGW节点对路径索引删除”时，该参数需要设置。
PGWIPADDR|PGW节点IP地址|参数可选性:任选参数；参数类型:字符型。|表示要删除的SGW-PGW节点对的PGW IP地址，当“节点删除类型”设置为“指定不可达SGW-PGW节点对IP索引删除”或“删除指定PGW对应的所有不可达SGW-PGW节点对”时，该参数需要设置。
SGWIPADDR|SGW节点IP地址|参数可选性:任选参数；参数类型:字符型。|表示要删除的SGW-PGW节点对的SGW IP地址，当“节点删除类型”设置为“指定不可达SGW-PGW节点对IP索引删除”或“删除指定SGW对应的所有不可达SGW-PGW节点对”时，该参数需要设置。






[](None)命令举例 


删除全部不可达SGW-PGW节点对。 


DELETE UNREACHABLE GW NODE:TYPE="AllUnreachableNode"; 








父主题： [GTP节点管理](../../zh-CN/tree/N_130840043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询S10口对端MME地址(SHOW S10 FAR ADDR) 
### 查询S10口对端MME地址(SHOW S10 FAR ADDR) 


[](None)命令功能 

查询S10口对端MME地址


[](None)注意事项 


无。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IPADDR|IP地址|参数可选性:任选参数；参数类型:字符型。|表示S10口对端MME地址






[](None)命令举例 


查询S10口对端MME地址。 


SHOW S10 FAR ADDR; 


`

命令 (No.1): SHOW S10 FAR ADDR

IP地址   
-------------------
192.20.104.96
-------------------
记录数 1

命令执行成功（耗时 0.04 秒）。
` 








父主题： [GTP节点管理](../../zh-CN/tree/N_130840043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## RNC动态管理 
## RNC动态管理 


[](None)背景知识 

            
            RNC（Radio Network Controller）无线网络控制器，用于提供移动性管理、呼叫处理、链接管理和切换机制，为核心网SGSN提供业务。
        


[](None)功能描述 

            
            RNC动态管理用于查询与本网元相连的RNC的信息，以及实现人工对RNC的操作，包括查询RNC的信息，对指定的RNC进行复位或者部分资源的复位。
        


[](None)相关主题 



 

显示RNC信息(SHOW RNCINFO)
 

 

复位RNC(RESET RNC)
 

 

复位RNC资源(RESET RNCRES)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 显示RNC信息(SHOW RNCINFO) 
### 显示RNC信息(SHOW RNCINFO) 


[](None)命令功能 

该命令用于查询Iu口所有已配置的RNC局向信息，包括RNC数目和RNC局向号。


[](None)注意事项 

此命令合适于SGSN网元。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RNCNUM|RNC数|参数可选性:任选参数；参数类型:整数。|此参数为执行SHOW RNCINFO 命令后的输出参数。表示当前SGSN已配置的RNC局向个数。目前SGSN最多支持配置4096个RNC。
RNCID|RNC局向号|参数可选性:任选参数；参数类型:字符型；参数范围为:1~5个字符。|该参数用于表示RNC局向号。该参数的取值是通过命令ADD RNC 配置的“RNC局向号”。






[](None)命令举例 


查询当前网管配置的所有RNC信息，查询结果示例如下：
SHOW RNCINFO; 


`

命令 (No.1): SHOW RNCINFO

RNC数 
--------
10 
--------
记录数 1

RNC INFO
RNC局向号 
------------
1 
12 
40 
119 
116 
121 
180 
218 
190 
33 
------------
记录数 10

命令执行成功（耗时 0.041 秒）。
` 








父主题： [RNC动态管理](../../zh-CN/tree/N_130840053.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 复位RNC(RESET RNC) 
### 复位RNC(RESET RNC) 


[](None)命令功能 

该命令用于复位一个指定的RNC局向。


[](None)注意事项 



 
此命令合适于SGSN网元。
 

 
复位指定的RNC局向前，需要确认该RNC局向已存在。 查询命令为： SHOW RNCINFO 。
 

 
该命令属于危险操作，将导致SGSN和RNC间的连接中断，用户无法正常使用数据业务。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RNCIDX|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于表示RNC局向号。该参数的取值是通过命令ADD RNC 配置的“RNC局向号”。






[](None)命令举例 


复位的RNC局向号为“1”。
RESET RNC:RNCIDX=1; 








父主题： [RNC动态管理](../../zh-CN/tree/N_130840053.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 复位RNC资源(RESET RNCRES) 
### 复位RNC资源(RESET RNCRES) 


[](None)命令功能 


该命令用于复位一个指定的RNC局向下的一个或多个IuScId（Iu Signalling Connection Identifier，Iu信令连接标识）资源。 


IuScId由RNC分配，唯一标识一个Iu信令连接。 




[](None)注意事项 



 
此命令合适于SGSN网元。
 

 
复位指定的RNC局向资源前，需要确认该RNC局向已存在。 查询命令为： SHOW RNCINFO 。
 

 
该命令属于危险操作，将导致SGSN和RNC间对应的Iu信令连接中断，用户无法正常使用数据业务。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RNCIDX|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于表示RNC局向号。该参数的取值是通过命令ADD RNC 配置的“RNC局向号”。
IUSCID|Iu信令连接标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于表示IuScId（Iu Signalling Connection Identifier，Iu信令连接标识）。该标识由RNC分配，唯一标识一个Iu连接，最多可配置250个。






[](None)命令举例 


复位RNC局向号为“1”，复位的Iu信令连接标识为“1”和“2”。
RESET RNCRES:RNCIDX=1,IUSCID="1"&"2"; 








父主题： [RNC动态管理](../../zh-CN/tree/N_130840053.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## eNodeB动态管理 
## eNodeB动态管理 


[](None)背景知识 

            
            为了查询与本网元相连的eNodeB的信息，以及实现人工对eNodeB的操作。
        


[](None)功能描述 

            
            eNodeB动态管理用于查询eNodeB的信息，对指定的eNodeB进行复位或者部分资源的复位。
        


[](None)相关主题 



 

S1连接释放(RELEASE S1)
 

 

复位部分S1连接(RESET PART S1)
 

 

复位eNodeB(RESET ENODEB)
 

 

查询单个eNodeB信息(SHOW ENODEB INFO)
 

 

查询全部eNodeB信息(SHOW ENODEBS INFO)
 

 

查询动态eNodeB数量(SHOW ENODEBS NUM)
 

 

查询所有动态TA的RAT类型(SHOW ALL TA RAT TYPE)
 

 

查询TAI相关的eNodeB信息(SHOW TAI ENODEBS INFO)
 

 

更新eNodeB的MME权重(UPDATE ENB MME WEIGHT)
 

 

通知单个eNodeB过负荷(NOTIFY SINGLE ENB OVERLOAD)
 

 

通知所有eNodeB过负荷(NOTIFY ALL ENB OVERLOAD)
 

 

停止单个eNodeB过负荷(STOP SINGLE ENB OVERLOAD)
 

 

停止所有eNodeB过负荷(STOP ALL ENB OVERLOAD)
 

 

增加允许跟踪Cell Traffic Trace消息的高优先级eNB(ADD CELLRPTENB)
 

 

删除允许跟踪Cell Traffic Trace消息的eNB(DEL CELLRPTENB)
 

 

查询允许跟踪Cell Traffic Trace消息的eNB(SHOW CELLRPTENB)
 

 

查询单个gNodeB信息(SHOW GNODEB INFO)
 

 

查询全部gNodeB信息(SHOW GNODEBS INFO)
 

 

查询TA下eNodeB数量(SHOW MME TALIST ENBNUM)
 

 

查询单个eNB邻接关系信息(SHOW SINGLE ENB NEIGHBOR INFO)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### S1连接释放(RELEASE S1) 
### S1连接释放(RELEASE S1) 


[](None)命令功能 


该命令用于释放一个S1连接。 


每个用户在线时都存在一条S1连接，在需要释放该S1连接时，使用该命令。 


该命令执行成功后，S1连接被释放，用户处于IDLE状态。 




[](None)注意事项 


该命令执行将会影响被释放了S1连接的用户的在线状态。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户携带的IMSI（非IMSI号段），IMSI（IMSI，International Mobile Subscriber Identification Number）是国际移动用户识别码，是区别移动用户的标志，可用于区别移动用户的有效信息。






[](None)命令举例 


释放IMSI为460010000000100对应的S1连接。 


RELEASE S1:IMSI="460010000000100"; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 复位部分S1连接(RESET PART S1) 
### 复位部分S1连接(RESET PART S1) 


[](None)命令功能 


该命令用于复位部分S1连接，实际复位S1连接的数量由命令中携带的参数决定。 


当运营商需要随机释放部分S1连接时使用该命令，需谨慎使用。 


命令执行成功后，指定数量的S1连接被释放。 




[](None)注意事项 


该命令执行将会影响被释放了S1连接的用户的在线状态。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
NUM|复位个数|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|设置复位S1连接的个数。






[](None)命令举例 


释放MCC为460，MNC为10，ENODEBID为1所对应的eNodeB下10条S1连接，这10条连接是随机选择的。 


RESET PART S1:MCC="460",MNC="10",ENODEBID=1,NUM=10; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 复位eNodeB(RESET ENODEB) 
### 复位eNodeB(RESET ENODEB) 


[](None)命令功能 


该命令用于复位指定的eNodeB，命令成功执行后MME会释放指定eNodeB上的所有S1连接。 


当运营商需要清理eNodeB上的所有S1连接时使用该命令。 


命令执行成功后，eNodeB上的所有S1连接被释放。 




[](None)注意事项 



 
复位指定的eNodeB前，需要确认该eNodeB局向是否已存在，查询命令为 SHOW ENODEBS INFO。
 

 
该命令会导致指定eNodeB上所有用户的PS业务中断。
 

 
该命令立即生效。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。






[](None)命令举例 


复位MCC为460，MNC为10，ENODEBID为1所对应的eNodeB。 


RESET ENODEB:MCC="460",MNC="10",ENODEBID=1; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询单个eNodeB信息(SHOW ENODEB INFO) 
### 查询单个eNodeB信息(SHOW ENODEB INFO) 


[](None)命令功能 


该命令用于根据MCC、MNC、eNodeB局向号三个参数查询本局归属下指定的单个eNodeB信息，包括：本端地址、本端端口、对端地址、对端端口等。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示命令执行结果。取值含义：“命令执行成功（耗时 * 秒）”：执行成功 “命令执行失败（耗时 * 秒），原因：命令发送超时。”：执行失败，并列出失败原因。
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型；参数范围为:0~5个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型；参数范围为:0~5个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
ENODEBNAME|eNodeB名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|eNodeB名称是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
TAC|跟踪区列表|参数可选性:任选参数；参数类型:字符型；参数范围为:0~20个字符。|eNodeB支持的TA列表，TA列表是一组TA的集合，一般是由运营商统一规划。
CSGNUM|CSG数量|参数可选性:任选参数；参数类型:字符型。|eNodeB支持的CSG个数，CSG也叫闭合用户群，一般是由运营商统一规划。
CSGLIST|CSG列表|参数可选性:任选参数；参数类型:字符型。|eNodeB支持的CSG列表，CSG列表是一组CSG的集合，一般是由运营商统一规划。
ASSOCID|偶联号|参数可选性:任选参数；参数类型:字符型。|指示eNodeB与MME之间建立局向时使用的偶联，一般是由运营商统一规划。
LOCALPORT|本地端口号|参数可选性:任选参数；参数类型:字符型。|eNodeB与MME之间建立SCTP链路时配置的本端端口号，一般是由运营商统一规划，动态偶联查询命令为： SHOW S1APSCTPSVR，静态偶联查询命令为：SHOW S1APSCTP。
PEERPORT|对端端口号|参数可选性:任选参数；参数类型:字符型。|设置eNodeB和MME建立SCTP链接时候所需的远端端口号。操作人员可以规划和分配此参数。使用SHOW S1APSCTPSVR命令来查询动态偶联。使用SHOW S1APSCTP命令查询静态偶联。
LOCALADDRLIST|本地IP地址列表|参数可选性:任选参数；参数类型:字符型。|eNodeB与MME之间建立SCTP链路时配置的本端IP地址列表，一般是由运营商统一规划，动态偶联查询命令为： SHOW S1APSCTPSVR，静态偶联查询命令为：SHOW S1APSCTP。
REMOTEADDRLIST|对端IP地址列表|参数可选性:任选参数；参数类型:字符型。|eNodeB与MME之间建立SCTP链路时配置的对端IP地址列表，一般是由运营商统一规划，动态偶联查询命令为： SHOW S1APSCTPSVR，静态偶联查询命令为：SHOW S1APSCTP。
QRYRESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示ENODEB查询不到。 取值含义：记录不存在
RAT|RAT类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示用户接入时，的PDP激活和更新消息中携带的RAT type。






[](None)命令举例 


查询MCC为460，MNC为11，ENODEBID为154对应eNodeB的相关信息。 


SHOW ENODEB INFO: MCC=460,MNC=11,ENODEBID=154; 


`

命令 (No.1): SHOW ENODEB INFO:MCC="460",MNC="11",ENODEBID=154;

移动国家码(MCC) 
------------------
460 
------------------
记录数 1

移动网号(MNC) 
----------------
11 
----------------
记录数 1

eNodeB局向号 
---------------
154 
---------------
记录数 1

eNodeB名称 
-------------
mme18test 
-------------
记录数 1

跟踪区列表 
-------------
460-11-0200 
460-11-0061 
454-00-0300 
232-10-0001 
460-11-0002 
460-03-0003 
454-00-0400 
460-11-0062 
460-03-0001 
460-11-0118 
460-16-0001 
460-03-0010 
232-10-0010 
-------------
记录数 13

CSG数量 
----------
0 
----------
记录数 1

CSG列表 
----------
  
----------
记录数 1

偶联号 
---------
59999 
---------
记录数 1

模块号 
---------
2 
---------
记录数 1

本地端口号 
-------------
1818 
-------------
记录数 1

对端端口号 
-------------
50001 
-------------
记录数 1

本地IP地址列表 
-----------------
IPv4: 200.18.1.18   
-----------------
记录数 1

对端IP地址列表 
-----------------
IPv4: 40.40.133.133   
-----------------
记录数 1

RAT TYPE 
---------
NB   
---------
记录数 1
命令执行成功（耗时 0.062 秒）。
` 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询全部eNodeB信息(SHOW ENODEBS INFO) 
### 查询全部eNodeB信息(SHOW ENODEBS INFO) 


[](None)命令功能 


该命令用于查询本局归属下全部eNodeB信息，包括：本端地址、本端端口、对端地址、对端端口等。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|查询类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于查询所有eNodeB信息时对eNodeB进行分类显示，具体取值由用户需求决定。 取值含义：COMMON_eNodeB：普通eNodeB。CSG_RELATION_eNodeB：关联了CSG的eNodeB，即建立局向时携带了CSG信息的eNodeB，且MME也支持CSG功能。ALL：所有eNodeB。
RAT|RAT类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示用户接入时，的PDP激活和更新消息中携带的RAT type。
EXFILE|是否导出到文件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|用于控制输出结果是否生成文件，默认为否。选项包括：否是






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:任选参数；参数类型:字符型。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
ASSOCID|偶联号|参数可选性:任选参数；参数类型:字符型。|指示eNodeB与MME之间建立局向时使用的偶联，一般是由运营商统一规划。
LOCALPORT|本地端口号|参数可选性:任选参数；参数类型:字符型。|eNodeB与MME之间建立SCTP链路时配置的本端端口号，一般是由运营商统一规划，动态偶联查询命令为： SHOW S1APSCTPSVR，静态偶联查询命令为：SHOW S1APSCTP。
PEERPORT|对端端口号|参数可选性:任选参数；参数类型:字符型。|设置eNodeB和MME建立SCTP链接时候所需的远端端口号。操作人员可以规划和分配此参数。使用SHOW S1APSCTPSVR命令来查询动态偶联。使用SHOW S1APSCTP命令查询静态偶联。
LOCALADDRLIST|本地IP地址列表|参数可选性:任选参数；参数类型:字符型。|eNodeB与MME之间建立SCTP链路时配置的本端IP地址列表，一般是由运营商统一规划，动态偶联查询命令为： SHOW S1APSCTPSVR，静态偶联查询命令为：SHOW S1APSCTP。
REMOTEADDRLIST|对端IP地址列表|参数可选性:任选参数；参数类型:字符型。|eNodeB与MME之间建立SCTP链路时配置的对端IP地址列表，一般是由运营商统一规划，动态偶联查询命令为： SHOW S1APSCTPSVR，静态偶联查询命令为：SHOW S1APSCTP。
QRYRESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示ENODEB查询不到。 取值含义：记录不存在
RAT|RAT类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示用户接入时，的PDP激活和更新消息中携带的RAT type。






[](None)命令举例 


查询本局归属下所有eNodeB的信息。 


SHOW ENODEBS INFO:TYPE="ALL"; 


`

命令 (No.1): SHOW ENODEBS INFO:TYPE="ALL";

移动国家码(MCC)   移动网号(MNC)   eNodeB局向号   模块号   偶联号   本地端口号   对端端口号   本地IP地址列表        对端IP地址列表       RAT TYPE
------------------------------------------------------------------------------------------------------------------------------------------------
460               11              154            2        59999    1818         50001        IPv4: 200.18.1.18     IPv4: 40.40.133.133  NB
454               00              138            2        59998    1819         50002        IPv4: 200.18.1.18     IPv4: 40.40.135.135  NB&WB
------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.197 秒）。
` 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询动态eNodeB数量(SHOW ENODEBS NUM) 
### 查询动态eNodeB数量(SHOW ENODEBS NUM) 


[](None)命令功能 


该命令用于查询本局归属下所有动态eNodeB的数量。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
COMENBNUM|普通的动态eNodeB数量|参数可选性:任选参数；参数类型:整数。|指示当前与MME建立局向的不支持CSG的eNodeB数量。
CSGENBNUM|CSG关联的动态eNodeB数量|参数可选性:任选参数；参数类型:整数。|指示当前与MME建立局向的支持CSG的eNodeB数量。






[](None)命令举例 


查询本局归属下eNodeB的个数。 


SHOW ENODEBS NUM; 


`

命令 (No.1): SHOW ENODEBS NUM

普通的动态eNodeB数量 
-----------------------
2 
-----------------------
记录数 1

CSG关联的动态eNodeB数量 
--------------------------
0 
--------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询所有动态TA的RAT类型(SHOW ALL TA RAT TYPE) 
### 查询所有动态TA的RAT类型(SHOW ALL TA RAT TYPE) 


[](None)命令功能 


该命令用于查询所有动态TA的无线接入类型情况。如果某个TA下的eNodeB的接入类型有混配，则说明规划有误，需要纠正。 




[](None)注意事项 


当出现某个TA下的eNodeB的无线接入类型有混配的情况时，可以进一步结合[SHOW TAI ENODEBS INFO](1263117.html)命令来查看该TA下具体每个eNodeB的无线接入类型。




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
TAC|跟踪区域码(TAC)(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC标识跟踪区的标识码。
WBENODEB|WB-E-UTRAN的eNodeB个数|参数可选性:任选参数；参数类型:整数。|当前跟踪区下，类型配置为WB-E-UTRAN的eNodeB的个数。
NBENODEB|NB-IoT的eNodeB个数|参数可选性:任选参数；参数类型:整数。|当前跟踪区下，类型配置为NB-IoT的eNodeB的个数。
QRYRESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于显示查询eNodeB相关信息时，命令的执行结果，表示命令执行成功或失败。






[](None)命令举例 


查询所有动态TA的RAT类型。 


SHOW ALL TA RAT TYPE; 


`

命令 (No.1): SHOW ALL TA RAT TYPE;

移动国家码(MCC)  移动网号(MNC)  跟踪区域码(TAC)(HEX)  WB-E-UTRAN的eNodeB个数  NB-IoT的eNodeB个数
------------------------------------------------------------------------------------------------
460              11             6001                  1                       0 
460              11             6002                  2                       0 
------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.042 秒）。
` 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询TAI相关的eNodeB信息(SHOW TAI ENODEBS INFO) 
### 查询TAI相关的eNodeB信息(SHOW TAI ENODEBS INFO) 


[](None)命令功能 


该命令用于根据TAI查询本局归属下与该TAI相关的eNodeB信息，包括MCC、MNC、eNodeB局向号。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TAID|跟踪区标识|参数可选性:必须单选参数；参数类型:整数；参数范围为:1~65535。|TA标识，该参数用于查找所有支持某个TA的eNodeB，TAID的配置命令为： ADD TA。
TAI|跟踪区标识TAI|参数可选性:必须单选参数；参数类型:复合参数|TAI跟踪区标识，由MCC，MNC和TAC组成。
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
TAC|跟踪区域码(TAC)(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC标识跟踪区的标识码。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示命令执行结果。取值含义：“命令执行成功（耗时 * 秒）”：执行成功 “命令执行失败（耗时 * 秒），原因：命令发送超时。”：执行失败，并列出失败原因。
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:任选参数；参数类型:字符型。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
RATTYPE|RAT类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|无线接入类型，此处广义区分为WB-E-UTRAN和NB-IoT两种类型。






[](None)命令举例 


查询TAI相关的eNodeB信息。 


SHOW TAI ENODEBS INFO:TAI="460"-"11"-"6001"; 


`

命令 (No.1): SHOW TAI ENODEBS INFO:TAI="460"-"11"-"6001";

移动国家码(MCC)  移动网号(MNC)  eNodeB局向号  RAT类型
----------------------------------------------------------------
460              11             190993        WB-E-UTRAN 
----------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 更新eNodeB的MME权重(UPDATE ENB MME WEIGHT) 
### 更新eNodeB的MME权重(UPDATE ENB MME WEIGHT) 


[](None)命令功能 


该命令用于修改MME的权重值时，通知eNodeB进行修改。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
MMEWEIGHT|MME权重|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|MME在POOL内的权重，数值越大，权重越大。当eNodeB向MME发s1 setup建链消息或者eNodeB配置更新消息时，eNodeB选择接入权重最大的MME。






[](None)命令举例 


通知指定eNodeB将MME权重值更新为80，该指定eNodeB的MCC为460、MNC为01、eNodeB ID为1。 


UPDATE ENB MME WEIGHT:MCC="460",MNC="01",ENODEBID=1,MMEWEIGHT=80; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 通知单个eNodeB过负荷(NOTIFY SINGLE ENB OVERLOAD) 
### 通知单个eNodeB过负荷(NOTIFY SINGLE ENB OVERLOAD) 


[](None)命令功能 

该命令用于通知单个eNodeB修改过负荷控制信息，包括Overload Action信元和Traffic Load Reduction Indication信元。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
ACT|Overload Action信元设置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME发送overload start消息时，消息中Overload Action IE所携带的值。取值含义： 拒绝非紧急情况终端发起数据传输的所有RRC连接建立拒绝信令传输的所有RRC连接建立仅允许紧急对话拒绝所有低优先级接入
TLRI|Traffic Load Reduction Indication信元设置|参数可选性:必选参数；参数类型:整数；参数范围为:0~99。|该参数用于设置MME发送overload start消息时，消息中Traffic Load Reduction Indication所携带的值。






[](None)命令举例 


通知指定eNodeB将Overload Action设置为“仅允许紧急对话”，Traffic Load Reduction Indication设置为50，该指定eNodeB的MCC为460、MNC为01、eNodeB ID为1。 


NOTIFY SINGLE ENB OVERLOAD:MCC="460",MNC="01",ENODEBID=1,ACT="Permit Emergency",TLRI=50; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 通知所有eNodeB过负荷(NOTIFY ALL ENB OVERLOAD) 
### 通知所有eNodeB过负荷(NOTIFY ALL ENB OVERLOAD) 


[](None)命令功能 

该命令用于通知所有eNodeB修改过负荷控制信息，包括Overload Action信元和Traffic Load Reduction Indication信元。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ACT|Overload Action信元设置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME发送overload start消息时，消息中Overload Action IE所携带的值。取值含义： 拒绝非紧急情况终端发起数据传输的所有RRC连接建立拒绝信令传输的所有RRC连接建立仅允许紧急对话拒绝所有低优先级接入
TLRI|Traffic Load Reduction Indication信元设置|参数可选性:必选参数；参数类型:整数；参数范围为:0~99。|该参数用于设置MME发送overload start消息时，消息中Traffic Load Reduction Indication所携带的值。






[](None)命令举例 


通知所有eNodeB将Overload Action设置为“仅允许紧急对话”，Traffic Load Reduction Indication设置为50。 


NOTIFY ALL ENB OVERLOAD:ACT="Permit Emergency",TLRI=50; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 停止单个eNodeB过负荷(STOP SINGLE ENB OVERLOAD) 
### 停止单个eNodeB过负荷(STOP SINGLE ENB OVERLOAD) 


[](None)命令功能 

该命令用于当MME已经不处于过负荷时，通知单个eNodeB停止过负荷控制。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。






[](None)命令举例 


通知指定eNodeB停止过负荷控制，该指定eNodeB的MCC为460、MNC为01、eNodeB ID为1。 


STOP SINGLE ENB OVERLOAD:MCC="460",MNC="01",ENODEBID=1; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 停止所有eNodeB过负荷(STOP ALL ENB OVERLOAD) 
### 停止所有eNodeB过负荷(STOP ALL ENB OVERLOAD) 


[](None)命令功能 

该命令用于当MME已经不处于过负荷时，通知所有eNodeB停止过负荷控制。


[](None)注意事项 


无。 




[](None)命令举例 


通知所有eNodeB停止过负荷控制。 


STOP ALL ENB OVERLOAD; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 增加允许跟踪Cell Traffic Trace消息的高优先级eNB(ADD CELLRPTENB) 
### 增加允许跟踪Cell Traffic Trace消息的高优先级eNB(ADD CELLRPTENB) 


[](None)命令功能 

该命令用于增加允许跟踪Cell Traffic Trace消息的高优先级eNB。


[](None)注意事项 


不能超过License限制的数量。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。






[](None)命令举例 


增加允许跟踪Cell Traffic Trace消息的高优先级eNB。 


ADD CELLRPTENB:MCC="445",MNC="123",ENODEBID=1; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除允许跟踪Cell Traffic Trace消息的eNB(DEL CELLRPTENB) 
### 删除允许跟踪Cell Traffic Trace消息的eNB(DEL CELLRPTENB) 


[](None)命令功能 

该命令用于删除允许跟踪Cell Traffic Trace消息的eNB。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。






[](None)命令举例 


删除允许跟踪Cell Traffic Trace消息的eNB。 


DEL CELLRPTENB:MCC="445",MNC="123",ENODEBID=1; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询允许跟踪Cell Traffic Trace消息的eNB(SHOW CELLRPTENB) 
### 查询允许跟踪Cell Traffic Trace消息的eNB(SHOW CELLRPTENB) 


[](None)命令功能 

该命令用于查询允许跟踪Cell Traffic Trace消息的eNB。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:特殊任选参数；参数类型:整数；参数范围为:1~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示命令执行结果。
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:任选参数；参数类型:字符型。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
FLAG|人工增加eNodeB|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于标识是否为人工增加的eNodeB。






[](None)命令举例 


查询允许跟踪Cell Traffic Trace消息的eNB。 


SHOW CELLRPTENB:MCC="445",MNC="123",ENODEBID=1; 


`

命令 (No.1): SHOW CELLRPTENB:MCC="445",MNC="123",ENODEBID=1;

操作结果	
-----------
成功	
-----------
记录数 1

信息
移动国家码(MCC)	移动网号(MNC)	eNodeB局向号	人工增加eNodeB	
---------------------------------------------------------------
445				123				1				是	
---------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.918 秒）。
` 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询单个gNodeB信息(SHOW GNODEB INFO) 
### 查询单个gNodeB信息(SHOW GNODEB INFO) 


[](None)命令功能 

网络支持EN-DC SON功能时，eNodeB会把与其连接的gNodeB信息上报给MME。eNodeB可能会根据gNode name查询gNode的IP地址，可以通过MME向该gNodeB连接的eNodeB查询。该命令用于根据MCC、MNC、gNodeB ID三个参数查询本局归属下指定的单个gNodeB信息，包括：连接的eNodeB。
注意：使用该命令，必须把“5GC互操作基本配置”下“MME是否支持EN-DC SON”设置为“是”。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GNODEBMCC|gNodeB MCC|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|gNodeB MCC
GNODEBMNC|gNodeB MNC|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|gNodeB MNC
GNODEBID|gNodeB ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|该参数标识gNodeB。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GNODEBMCC|gNodeB MCC|参数可选性:任选参数；参数类型:字符型；参数范围为:0~5个字符。|gNodeB MCC
GNODEBMNC|gNodeB MNC|参数可选性:任选参数；参数类型:字符型；参数范围为:0~5个字符。|gNodeB MNC
GNODEBID|gNodeB ID|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数标识gNodeB。
ENODEBMCC|eNodeB MCC|参数可选性:任选参数；参数类型:字符型；参数范围为:0~5个字符。|eNodeB MCC。
ENODEBMNC|eNodeB MNC|参数可选性:任选参数；参数类型:字符型；参数范围为:0~5个字符。|eNodeB MNC。
ENODEBID|eNodeB ID|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
QRYRESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示GNODEB查询不到的情况。 取值含义：1：功能不支持 2：记录不存在






[](None)命令举例 


查询单个gNodeB信息。 


SHOW GNODEB INFO:GNODEBMCC="460",GNODEBMNC="11",GNODEBID=152; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询全部gNodeB信息(SHOW GNODEBS INFO) 
### 查询全部gNodeB信息(SHOW GNODEBS INFO) 


[](None)命令功能 

网络支持EN-DC SON功能时，eNodeB会把与其连接的gNodeB信息上报给MME。eNodeB可能会根据gNode name查询gNode的IP地址，可以通过MME向该gNodeB连接的eNodeB查询。本命令用于查询本局eNodeB下所有gNodeB信息。
注意：使用该命令，必须把“5GC互操作基本配置”下“MME是否支持EN-DC SON”设置为“是”。


[](None)注意事项 


无。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GNODEBMCC|gNodeB MCC|参数可选性:任选参数；参数类型:字符型。|gNodeB MCC
GNODEBMNC|gNodeB MNC|参数可选性:任选参数；参数类型:字符型。|gNodeB MNC
GNODEBID|gNodeB ID|参数可选性:任选参数；参数类型:字符型。|该参数标识gNodeB。
ENODEBMCC|eNodeB MCC|参数可选性:任选参数；参数类型:字符型。|eNodeB MCC。
ENODEBMNC|eNodeB MNC|参数可选性:任选参数；参数类型:字符型。|eNodeB MNC。
ENODEBID|eNodeB ID|参数可选性:任选参数；参数类型:字符型。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
QRYRESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示GNODEB查询不到的情况。 取值含义：1：功能不支持 2：记录不存在






[](None)命令举例 


查询全部gNodeB信息。 


SHOW GNODEBS INFO; 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询TAList下eNodeB数量(SHOW MME TALIST ENBNUM) 
### 查询TAList下eNodeB数量(SHOW MME TALIST ENBNUM) 


[](None)命令功能 


该命令用于查询全局所有TA或TAList列表下每个TA分别对应的eNodeB数量。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
QUERYMODE|查询方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数表示查询跟踪区列表下站点的方式。0 - 表示查询全局每个TA对应的eNodeB站点数量。1 - 表示查询TA对应的eNodeB站点数量。
TA|跟踪区标识TA|参数可选性:任选参数；参数类型:复合参数|此参数表示查询的TA，根据TA查询eNodeB数量。
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
TAC|跟踪区域码(TAC)(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC标识跟踪区的标识码。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示命令执行结果。
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
TAC|跟踪区域码(TAC)(HEX)|参数可选性:任选参数；参数类型:字符型。|TAC标识跟踪区的标识码。
ENBNUM|跟踪区eNodeB数量|参数可选性:任选参数；参数类型:整数。|该参数用于表示跟踪区的eNodeB的具体数量。






[](None)命令举例 


查询TAList下eNodeB数量。 


SHOW MME TALIST ENBNUM; 


`

命令 (No.1) : SHOW MME TALIST ENBNUM:
-----------------uMAC_MME_V7master/NFS_MMESGSN_0----------------
移动国家码(MCC) 移动网号(MNC) 跟踪区域码(TAC)(HEX) 跟踪区eNodeB数量 
--------------------------------------------------------------------
460             11            007e                 0                
460             11            007f                 0                
460             11            0080                 0                
460             11            0081                 0                

记录数：4

命令执行成功（耗时 0.918 秒）。
` 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询单个eNB邻接关系信息(SHOW SINGLE ENB NEIGHBOR INFO) 
### 查询单个eNB邻接关系信息(SHOW SINGLE ENB NEIGHBOR INFO) 


[](None)命令功能 


该命令用于在MME上查询单个eNB的邻接eNB信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|本参数用于设置跟踪区的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号(MNC)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|本参数用于设置跟踪区的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
ENBID|eNB标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|本参数用于设置eNB ID，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个eNB，由运营商在PLMN内统一规划，以16进制数字编码。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|中心基站移动国家码|参数可选性:任选参数；参数类型:字符型。|本参数用于设置中心基站的Global eNodeB ID的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。
MNC|中心基站移动网络码|参数可选性:任选参数；参数类型:字符型。|本参数用于设置中心基站的Global eNodeB ID的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中基于MCC唯一标识一个运营商网络信息。
ENBID|中心eNB标识|参数可选性:任选参数；参数类型:整数。|本参数用于设置中心基站的eNB ID，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC）内，标识唯一的一个eNB，由运营商在PLMN内统一规划，以16进制数字编码。
NEIMCC|邻接基站移动国家码|参数可选性:任选参数；参数类型:字符型。|本参数用于设置邻接基站的Global eNodeB ID的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。
NEIMNC|邻接基站移动网号|参数可选性:任选参数；参数类型:字符型。|本参数用于设置邻接基站的Global eNodeB ID的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中基于MCC唯一标识一个运营商网络信息。
NEIENBID|邻接eNB标识|参数可选性:任选参数；参数类型:字符型。|本参数用于设置邻接基站的eNB ID，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个eNB，由运营商在PLMN内统一规划，以16进制数字编码。






[](None)命令举例 


查询MCC为460，MNC为11，ENBID为19001对应eNB的相关信息。 


SHOW SINGLE ENB NEIGHBOR INFO:MCC="420",MNC="11",ENBID=19001; 


`

命令 (No.1): SHOW SINGLE ENB NEIGHBOR INFO:MCC="420",MNC="11",ENBID=19001;
中心基站移动国家码   中心基站移动网络码   中心eNB标识 邻接基站移动国家码   邻接基站移动网号    邻接eNB标识
------------------------------------------------------------------------------------------------------------------------------------
420                  11                   19001       420                  02                  155
------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.062 秒）。
` 








父主题： [eNodeB动态管理](../../zh-CN/tree/N_130840063.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## MCE动态管理 
## MCE动态管理 


[](None)背景知识 

            
            MCE (Multi-cell/Multicast Coordination Entity)作为MBMS业务的一个实体，对于单个MBMS业务，MCE主要用于业务的调度，即选择合适的资源(包括频率、时间等参数)，进行多媒体广播多播单频网(MBSFN)传输；对于多个MBMS业务，MCE需要协调其相应的多个MBSFN传输，包括MBSFN区域的大小，无线资源的使用等等，以便能够合理地、高效地使用资源。
        


[](None)功能描述 

            
            MCE动态管理用于查询与本网元相连的MCE的信息，以及实现人工对MCE的操作。包括查询MCE的信息，对指定的MCE进行复位或者部分资源的复位。
        


[](None)相关主题 



 

复位MCE(Reset MCE)
 

 

复位部分MCE连接(RESET PART MCE)
 

 

查询所有MCE信息(SHOW MCES INFO)
 

 

查询全部MCE连接(SHOW ALL MCE LINKS)
 

 

查询单个MCE连接(SHOW MCE LINKS)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 复位MCE(RESET MCE) 
### 复位MCE(RESET MCE) 


[](None)命令功能 

复位MCE


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|
MCEID|MCE局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|






[](None)命令举例 


复位移动国家码为321，移动网号为111，MCE局向号为1对应的MCE。 


RESET MCE:MCC="321",MNC="111",MCEID=1; 








父主题： [MCE动态管理](../../zh-CN/tree/N_130840243.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 复位部分MCE连接(RESET PART MCE) 
### 复位部分MCE连接(RESET PART MCE) 


[](None)命令功能 


该命令用于复位指定模块上MCE部分连接，需要复位的连接数量由命令中携带的参数指定。 


该命令是由MME侧触发，由于丢失了部分业务交互信息，则需要初始化指定 MCE的部分连接；该命令执行成功后，指定MCE局向的部分连接被复位。 




[](None)注意事项 


复位指定的MCE部分连接前，需要确认该MCE局向是否已存在。 查询命令为： [SHOW MCES INFO](1263122.html)。




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|
MCEID|MCE局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|
NUMBER|个数|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数用于指示MCE和MME之间的信令连接数目。






[](None)命令举例 


复位移动国家码为321，移动网号为111，MCE局向号为1的MCE的5个连接。 


RESET PART MCE:MCC="321",MNC="111",MCEID=1,NUMBER=5; 








父主题： [MCE动态管理](../../zh-CN/tree/N_130840243.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询所有MCE信息(SHOW MCES INFO) 
### 查询所有MCE信息(SHOW MCES INFO) 


[](None)命令功能 


该命令用于查询M3口(MME和E-UTRAN的控制面接口)通过M3SETUP注册到本局MCE的局向信息。 




[](None)注意事项 


该命令属于动态查询，如果MCE注册到MME后，连接中断，则查询不到对应的MCE信息。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|MCC|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|MNC|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
MCEID|MCE号|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|MCE局向号，参考3GPP协议36.444。
ASSOCID|偶联号|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|该参数用于指示MME和MCE之间建立局向时使用的偶联，一般是由运营商统一规划。






[](None)命令举例 


查询所有MCE的局向关联信息。 


SHOW MCES INFO; 


`

命令 (No.1): SHOW MCES INFO

MCC   MNC   MCE号        模块号   偶联号
----------------------------------------
000   000   2147483659   2        11
----------------------------------------
记录数 1

命令执行成功（耗时 1.299 秒）。
` 








父主题： [MCE动态管理](../../zh-CN/tree/N_130840243.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询全部MCE连接(SHOW ALL MCE LINKS) 
### 查询全部MCE连接(SHOW ALL MCE LINKS) 


[](None)命令功能 


该命令用于查询系统当前全部的MCE连接。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示该命令的查询显示结果。
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
MCEID|MCE局向号|参数可选性:任选参数；参数类型:整数。|MCE局向号是MCE通过M3 Setup消息带给MME的，一般是由运营商统一规划。
TMGI|TMGI|参数可选性:任选参数；参数类型:字符型。|TMGI是eMBMS的会话标识，由BM-SC分配，与FLOWID组合，唯一对应一个BM-SC的会话。
FLOWID|FLOW ID|参数可选性:任选参数；参数类型:整数。|Flow ID是eMBMS的会话流标识，由BM-SC分配，与TMGI组合，唯一对应一个BM-SC的会话。






[](None)命令举例 


查询系统当前全部的MCE连接。 


SHOW ALL MCE LINKS; 


`

命令 (No.5): SHOW ALL MCE LINKS

移动国家码   移动网号   MCE局向号   TMGI            FLOW ID
-----------------------------------------------------------
460          110        60          460-14015-010   11
-----------------------------------------------------------
记录数 1

命令执行成功（耗时 1.547 秒）。
` 








父主题： [MCE动态管理](../../zh-CN/tree/N_130840243.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询单个MCE连接(SHOW MCE LINKS) 
### 查询单个MCE连接(SHOW MCE LINKS) 


[](None)命令功能 


该命令用于查询某个MCE连接。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
MCEID|MCE局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|MCE局向号，参考3GPP协议36.444。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示该命令的查询显示结果。
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
MCEID|MCE局向号|参数可选性:任选参数；参数类型:整数。|MCE局向号是MCE通过M3 Setup消息带给MME的，一般是由运营商统一规划。
TMGI|TMGI|参数可选性:任选参数；参数类型:字符型。|TMGI是eMBMS的会话标识，由BM-SC分配，与FLOWID组合，唯一对应一个BM-SC的会话。
FLOWID|FLOW ID|参数可选性:任选参数；参数类型:整数。|Flow ID是eMBMS的会话流标识，由BM-SC分配，与TMGI组合，唯一对应一个BM-SC的会话。






[](None)命令举例 


该查询MCC为460，MNC为110，MCE局向号为120的MCE连接的信息。 


SHOW MCE LINKS:MCC="460",MNC="110",MCEID=120; 


`

命令 (No.10): SHOW MCE LINKS:MCC="460",MNC="110",MCEID=120;

移动国家码   移动网号   MCE局向号    TMGI             FLOW ID
-------------------------------------------------------------
460          110        120          460110-273-477   12
-------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.056 秒）。
` 








父主题： [MCE动态管理](../../zh-CN/tree/N_130840243.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## GB口动态管理 
## GB口动态管理 


[](None)背景知识 

            
            BSC与SGSN之间的接口称为Gb口，是2G网络中无线侧和核心网连接的数据接口。
        


[](None)功能描述 

            
            Gb口动态管理用于查询与本网元相连的各Gb接口的信息，以及实现人工对Gb接口的操作，包括查询Gb口的信息，对指定的Gb口进行复位或者部分资源的复位。
        


[](None)相关主题 



 

查询BVC状态(SHOW BVCSTATE)
 

 

查询BVC统计信息(SHOW BVCSTATISTICS)
 

 

查询IPNSVC信息(SHOW IPNSVC INFO)
 

 

复位 BVC(RESET BVC)
 

 

查询IDLE状态NSE(SHOW IDLE NSE)
 

 

查询IDLE状态BVC(SHOW IDLE BVC)
 

 

查询全部NSE及路由区信息(SHOW ALL NSE RAI)
 

 

基于NSE/路由区/小区查询BVC信息(SHOW BVC BY POLICY)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询BVC状态(SHOW BVCSTATE) 
### 查询BVC状态(SHOW BVCSTATE) 


[](None)命令功能 


该命令用于查询PTP BVC的状态。可以按NSE进行查询，也可以查询全局（NSE ID不填写）；可以按BVC状态查询(闭塞状态或非闭塞状态)，也可以查询所有状态的BVC。 




[](None)注意事项 


按NSE为单位查询BVC信息，必须保证NSE已经配置。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
STATE|状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:ALL。|BVC状态，用于标识小区传输上行数据的能力。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSEI|NSEI|参数可选性:任选参数；参数类型:字符型。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
BVCI|BVCI|参数可选性:任选参数；参数类型:字符型。|BVCI（BSSGP Virtual Connection Identifier，BSSGP虚连接标识符）和NSEI一起用于标识一个2G的小区，此配置需要和BSC的配置完全匹配。每NSEI下最多创建1024个BVC，全局容量可配置，最多60000个。
CELLID|小区标识|参数可选性:任选参数；参数类型:字符型。|小区标识，用于唯一标识一个蜂窝数据小区。
BVCSTATE|BVC状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|BVC状态，用于标识小区传输上行数据的能力。
NSENAME|NSE名称|参数可选性:任选参数；参数类型:字符型。|NSE名称，是除了唯一标识NSE的NSEI之外的NSE别名，只有NSE标识号(NSEI)可以在SGSN上唯一标识一个网络业务实体NSE。






[](None)命令举例 


查询NSE标识号为100的所有PTP BVC的状态。 


SHOW BVCSTATE:NSEI=100;
 


`                                                                                                                                                                                                               

命令 (No.1): SHOW BVCSTATE:NSEI=100;

NSEI   BVCI   小区标识   BVC状态            NSE名称
---------------------------------------------------
100    1      257        解闭状态            
100    2      257        解闭状态            
---------------------------------------------------
记录数 2

命令执行成功（耗时 0.268 秒）。

                                                                                                                                                 
` 








父主题： [GB口动态管理](../../zh-CN/tree/N_130840073.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询BVC统计信息(SHOW BVCSTATISTICS) 
### 查询BVC统计信息(SHOW BVCSTATISTICS) 


[](None)命令功能 


该命令用于查询某个NSE下的PTP BVC的统计信息。包括NSE下创建的PTP BVC总数（BVC NUMBER）、闭塞的PTP BVC个数（BLOCK NUMBER）及其占PTP BVC总数的百分比、解闭的PTP BVC个数（UNBLOCK NUMBER）及其占PTP BVC总数的百分比。 




[](None)注意事项 


查询NSE ID 必须已经配置，请参见[SHOW NSE](1262303.html)。




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~10个字符。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
BVCNUM|BVC数|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|BVC统计信息 SHOW BVCSTATISTICS查询结果中，BVCNUM表示NSE下当前建立的PTP BVC总数。
BLOCKNUM|闭塞BVC数|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|BVC统计信息 SHOW BVCSTATISTICS查询结果中，BLOCKNUM表示NSE下当前处于闭塞状态的PTP BVC数量。
UNBLOCK|解闭BVC数|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|BVC统计信息 SHOW BVCSTATISTICS查询结果中，UNBLOCK表示NSE下当前处于解闭状态的PTP BVC数量。
NSENAME|NSE名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|NSE名称，是除了唯一标识NSE的NSEI之外的NSE别名，只有NSE标识号(NSEI)可以在SGSN上唯一标识一个网络业务实体NSE。






[](None)命令举例 


查询NSE标识号为100的PTP BVC统计信息。 


SHOW BVCSTATISTICS:NSEI=100;
 


`                                                                                                                                                                                                               

 命令 (No.1): SHOW BVCSTATISTICS:NSEI=100;

NSE标识   BVC数   闭塞BVC数   解闭BVC数   NSE名称
-------------------------------------------------
100       2       0(0%)       2(100%)      
-------------------------------------------------
记录数 1

命令执行成功（耗时 0.268 秒）。

                                                                                                                                               
` 








父主题： [GB口动态管理](../../zh-CN/tree/N_130840073.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询IPNSVC信息(SHOW IPNSVC INFO) 
### 查询IPNSVC信息(SHOW IPNSVC INFO) 


[](None)命令功能 


该命令用于查询某个IP承载NSE下配置的所有 NSVC的配置信息及状态。配置信息包括本端端点地址(IPV4 或IPV6)、本端端点端口、远端端点地址(IPV4 或IPV6)、远端端点端口、状态、对应远端端点的信令权值(0-255)、对应远端端点的数据权值(0-255)。 


配置信息含义： 



 
端点地址：IP端点由IP地址+UDP端口号组成，端点地址为IPV4或IPV6格式，用于配置该IP端点的IP地址。
 

 
端点端口：IP端点由IP地址+UDP端口号组成，端口号用于配置该IP端点对应的UDP端口号。
 

 
信令权重：IP端点的信令权重用于实现对端IP端点间的信令负荷分担。系统根据各个对端端点的信令权重，按信令权重比例，发送信令消息时按该比例选择对端端点，信令权重的配置范围为[0，255]。
 

 
数据权重：IP端点的数据权重用于实现对端IP端点间的数据负荷分担。系统根据各个对端端点的数据权重，按数据权重比例，发送数据时按该比例选择对端端点，数据权重的配置范围为[0，255]。
 

 


NSVC状态取值含义： 



 
Initial ：初始化状态。即链路刚刚建立的初始状态，还不具备传输信令的能力。
 

 
Alive ：激活状态。IP NSVC上的检活消息alive收到了应答alive-ack，状态迁移至激活，处于该状态的NSVC可以传输所有GbIP信令。
 

 
None_Operation ：无操作状态。该状态只存在于静态NSVC，即在检活最大重发次数内没有收到BSC侧的alive-ack，链路状态从alive迁移至无操作，处于该状态的NSVC不具备传输Gb口信令的能力。
 

 




[](None)注意事项 


如果输入NSEI没有配置过，则查询结果会提示：NSEI is not exist。 


如果输入NSEI是静态且没有静态NSVC链路配置，或者输入的NSEI是动态且尚没有建立动态NSVC链路，则查询结果中 Valid NSVC Number 为 0 。 


NSEI及NSVC配置模式必须和网络业务实体配置中保持完全一致。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
NSVCMODE|NSVC配置模式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:STATIC。|NSVC的配置模式。用于标识NSVC的配置方式及归属NSE的承载模式。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
CAUSE|返回原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于标识Gb口动态查询或动态操作命令返回的原因值。
NSEI|网络业务实体标识|参数可选性:任选参数；参数类型:整数。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
NSVCMODE|NSVC配置模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|NSVC的配置模式。用于标识NSVC的配置方式及归属NSE的承载模式。
NSVCNUM|有效NSVC个数|参数可选性:任选参数；参数类型:整数。|有效NSVC个数。该参数用于按NSE查询IP NSVC信息时标识NSE配置的IP NSVC条目数。
VPNID|NSEI所在VPN|参数可选性:任选参数；参数类型:整数。|该参数用于指定IP路由虚拟路由域，表示IP路由时选择该VRF关联的路由域内路由，起到隔离路由域的作用。
NSVCID|NSVC 标识|参数可选性:任选参数；参数类型:整数。|IP网络业务虚连接标识，在一个NSE内唯一的标识一条IP网络业务虚连接。
LIP|本端端点地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~64个字符。|IP端点由IP地址+UDP端口号组成，该参数用于标识该本端端点对应的IP地址，可以为IPV4或IPV6类型。
LPORT|本端端点端口|参数可选性:任选参数；参数类型:整数。|FR逻辑端口号用于在SGSN侧唯一标识一个BSC与SGSN的帧中继物理通道。逻辑端口号必须在1-960之间，且全局唯一。此配置需要和BSC的配置匹配。
RIP|远端端点地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~64个字符。|IP端点由IP地址+UDP端口号组成，该参数用于标识该远端端点对应的IP地址，可以为IPV4或IPV6类型。
RPORT|远端端点端口|参数可选性:任选参数；参数类型:整数。|IP端点由IP地址+UDP端口号组成，该参数用于标识该远端端点对应的UDP端口号。
STATUS|状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于标识 标识IP NSVC的是否可用状态或 BVC 的是否闭塞状态。
SIGWEIGHT|对应远端端点的信令权值|参数可选性:任选参数；参数类型:整数。|该参数用于设置IP本端端点的信令权重，用于本端\远端IP端点间的信令负荷分担。SGSN会根据各个远端端点的信令权重，按信令权重比例，发送信令消息时按该比例选择远端端点。若某NSE的两条IP NSVC 关联的两个远端端点的信令权重分别为66和33，那么如果有300个NS信令报文需要下发，两个端点对应的IP NSVC上传输的下行报文将按比例分配，分别为200个和100个。
DATAWEIGHT|NSVC对应远端端点的数据权值|参数可选性:任选参数；参数类型:整数。|该参数用于设置IP本端端点的数据权重，用于本端/远端IP端点间的数据负荷分担。SGSN会根据各个远端端点的数据权重，按数据权重比例，发送NS数据消息时按该比例选择远端端点。若某NSE的两条IP NSVC关联的两个远端端点的数据权重分别为100和25，那么如果有500个NS数据报文需要下发，两个端点对应的IP NSVC上传输的下行数据报文将按比例分配，分别为400个和100个。






[](None)命令举例 

根据NSE标识号为100，NSVC配置模式为静态配置模式，查询IPNSVC信息。 

SHOW IPNSVC INFO:NSEI=100,NSVCMODE="STATIC"; 

`                                                                                                                                                                                                               

命令 (No.1): SHOW IPNSVC INFO:NSEI=100,NSVCMODE="STATIC";

返回原因 
-----------
成功 
-----------
记录数 1

网络业务实体标识 
-------------------
100 
-------------------
记录数 1

NSVC配置模式 
---------------
静态配置 
---------------
记录数 1

有效NSVC个数 
---------------
2 
---------------
记录数 1

NSEI所在VPN 
--------------
0 
--------------
记录数 1

IPNSVC数组
NSVC 标识   本端端点地址          本端端点端口   远端端点地址        远端端点端口   状态     对应远端端点的信令权值   NSVC对应远端端点的数据权值
------------------------------------------------------------------------------------------------------------------------------------------------
1           IPv4: 30.1.136.107    40000          IPv4: 30.1.136.3    40000          激活     100                      100
2           IPv4: 30.1.136.107    40000          IPv4: 30.1.136.3    40001          激活     100                      100
------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.052 秒）。
                                                                                                                                                 
` 

  

。







父主题： [GB口动态管理](../../zh-CN/tree/N_130840073.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 复位 BVC(RESET BVC) 
### 复位 BVC(RESET BVC) 


[](None)命令功能 


该命令是用于当BSS和SGSN之间BVC 信息不匹配或设备异常时以及BVC的传输能力从0提升为非0时，BSS或SGSN可以发起BVC-RESET重新建立信令BVC或PTP BVC。SGSN使用该命令通过OMM手动复位一个信令BVC或者PTP BVC，以达到同步两端 GPRS BVC配置的目的。 



 
信令BVC：每个NSE有且只有一个信令BVC(BVCI为0)，即管控BVC，负责PTP BVC(BVCI非0)的创建、闭塞、解闭，该BVC只承载信令，不承载用户相关的信令；且不可以进行闭塞和解闭操作。
 

 
PTP BVC：每个NSE下可以有多个PTP BVC(BVCI非0)，即数据BVC，承载小区上用户信令，其创建、闭塞、解闭等操作必须通过信令BVC(BVCI为0来管控；可以进行闭塞和解闭操作。
 

 




[](None)注意事项 


手动复位的信令BVC或PTP BVC必须是已经在某个已配置的NSE下建立的BVC。 


执行命令，SGSN向对端BSC发送BVC-RESET消息，超时收不到BVC-RESET-ACK，重发，重发间隔为10s，最大重发次数为3次，即30s后收仍然不到BVC-RESET-ACK，命令执行失败：Result Failure; 30s内收到 正确的BVC-RESET-ACK，命令执行成功：Result Success 。 


如果复位的BVC为信令BVC(BVCI=0)，SGSN向对端BSC发送BVC-RESET消息, 对应NSE下所有已建立的PTP BVC将被闭塞，若30s内收到来自BSC的BVC-RESET-ACK，所有PTP BVC将被删除；若30s内未收到来自BSC的BVC-RESET-ACK，所有PTP BVC将保持闭塞状态。 


如果复位的BVC为PTP BVC(BVCI非0)，SGSN向对端BSC发送BVC-RESET消息,  该PTP BVC将被闭塞，若30s内收到来自BSC的BVC-RESET-ACK，该PTP BVC 执行RESET流程之后重新解闭并保持解闭状态；若30s内未收到来自BSC的BVC-RESET-ACK，该PTP BVC将保持闭塞状态。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
DLCICOMPLEX|DLCI复合体|参数可选性:必选参数；参数类型:复合参数|帧中继永久虚连接标识（FR PVC），由逻辑端口号和DLCI组成，用于在SGSN整局唯一标识一个帧中继永久虚连接。
BVCI|BVCI|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|BVCI（BSSGP Virtual Connection Identifier，BSSGP虚连接标识符）和NSEI一起用于标识一个2G的小区，此配置需要和BSC的配置完全匹配。每NSEI下最多创建1024个BVC，全局容量可配置，最多60000个。
NSEI|NSEI|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。






[](None)命令举例 


重置NSEI为109，BVCI为2的小区。 


RESET BVC:DLCICOMPLEX=109-2; 








父主题： [GB口动态管理](../../zh-CN/tree/N_130840073.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询IDLE态NSE(SHOW IDLE NSE) 
### 查询IDLE态NSE(SHOW IDLE NSE) 


[](None)命令功能 


该命令用于SGSN查询当前处于IDLE状态的NSE，把很久没有活动的NSE告诉维护操作人员，由他们决定是不是要对这些数据相关的设备做检查和删除处理。IDLE状态NSE，是闲置NSE，即在一定时间内NSE下的所有BVC上没有任何用户信令传输。 




[](None)注意事项 


当BVCI、BVC STATE参数显示为null时表明NSEI在前台不存在。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSEI|NSEI|参数可选性:任选参数；参数类型:字符型。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
TIMEELAPSED|闲置时长（时：分：秒）|参数可选性:任选参数；参数类型:字符型。|闲置时长用于记录NSE上没有任何用户信令及数据的时长。
NSENAME|NSE名称|参数可选性:任选参数；参数类型:字符型。|NSE名称，是除了唯一标识NSE的NSEI之外的NSE别名，只有NSE标识号(NSEI)可以在SGSN上唯一标识一个网络业务实体NSE。






[](None)命令举例 


查询SGSN处于IDLE态的所有NSE。 


 SHOW IDLE NSE; 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW IDLE NSE;

NSEI   闲置时长（时：分：秒）     NSE名称 
-------------------------------------------------------
11     197:16:27                  real_bsc_11
17     197:16:27                  Real_bsc_11_FR
21     197:16:27                  Real_BSC_21
-------------------------------------------------------
记录数 1

命令执行成功（耗时 0.172 秒）。
` 








父主题： [GB口动态管理](../../zh-CN/tree/N_130840073.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询IDLE态BVC(SHOW IDLE BVC) 
### 查询IDLE态BVC(SHOW IDLE BVC) 


[](None)命令功能 


该命令用于SGSN查询当前处于IDLE状态的BVC，把很久没有活动的BVC告诉维护操作人员，由他们决定是不是要对这些数据相关的设备做检查和删除处理。IDLE状态BVC，是闲置BVC，即在一定时间内BVC上没有任何用户信令传输。 




[](None)注意事项 


当BVCI、BVC STATE参数显示为null时表明NSEI在前台不存在。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSEI|NSEI|参数可选性:任选参数；参数类型:整数。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
BVCI|BVCI|参数可选性:任选参数；参数类型:整数。|BVCI（BSSGP Virtual Connection Identifier，BSSGP虚连接标识符）和NSEI一起用于标识一个2G的小区，此配置需要和BSC的配置完全匹配。每NSEI下最多创建1024个BVC，全局容量可配置，最多60000个。
CELLID|小区标识|参数可选性:任选参数；参数类型:整数。|小区标识，用于唯一标识一个蜂窝数据小区。
TIMEELAPSED|闲置时长（时：分：秒）|参数可选性:任选参数；参数类型:字符型。|闲置时长用于记录NSE上没有任何用户信令及数据的时长。
NSENAME|NSE名称|参数可选性:任选参数；参数类型:字符型。|NSE名称，是除了唯一标识NSE的NSEI之外的NSE别名，只有NSE标识号(NSEI)可以在SGSN上唯一标识一个网络业务实体NSE。






[](None)命令举例 


查询SGSN处于IDLE态的所有PTP BVC。 


SHOW IDLE BVC; 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW IDLE BVC;

NSEI    BVCI    小区标识   T闲置时长（时：分：秒）       NSE名称 
--------------------------------------------------------------------------
17      25      2          197:13:53                     Real_bsc_11_FR
--------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.226 秒）。                                                                   
` 








父主题： [GB口动态管理](../../zh-CN/tree/N_130840073.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询全部NSE及路由区信息(SHOW ALL NSE RAI) 
### 查询全部NSE及路由区信息(SHOW ALL NSE RAI) 


[](None)命令功能 


该命令用于查询SGSN全部NSE的基本配置信息即关联的路由区信息，不需要填写查询条件。 


查询结果包括： 



 
NSEI：网络业务实体标识。
 

 
NSE IDLE FLAG：NSE是否已经处于IDLE状态，请参见SHOW IDLE NSE。
 

 
Bearer Mode：NSE承载属性，“枚举值IP”或“FR”，请参见ADD NSE。
 

 
IPNS Config Mode：若NSE承载属性为“IP”，其NSVC的配置方式，枚举值静态“Static”或“动态Dynamic”，具体含义请参见SHOW NSE。
 

 
VRF ID：该NSE归属的VRF，具体含义请参见SHOW NSE。
 

 
Routing Area List：NSE的关联路由区列表，即NSE下已经建立的所有 PTP BV归属的路由区(RAI)列表。受OMM界面限制，目前最多显示8个RAI，若多于8个RAI，只显示前8个。
 

 
ALLRAFLAG：NSE关联路由区列表是否已经全部显示，枚举值“YES”或“NO”。
 

 




[](None)注意事项 


只有在NSE下创建有PTP BVC的前提下，才能由NSEI和小区标识（Global Cell Id）中的RAI生成关联。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于标识Gb口动态维护命令的操作结果。
NSEI|NSE标识|参数可选性:任选参数；参数类型:整数。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
IDLEFLAG|NSE是否空闲|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果NSE的所有小区在限制时长(TIMEELAPSED)内没有任何上行用户信令的传输SGSN将NSE置为IDLE态，并将IDLEFLAG置1。
BEARMODE|承载方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|NSE的承载模式。即Gb口SGSN和BSC之间的物理承载方式。取值含义：FR：FR帧中继承载。即Gb口SGSN和BSC之间物理连接为E1线，传输协议为帧中继。IP：IP承载。Gb口SGSN和BSC之间物理连接为网线，传输协议为UDP/IP。
NSVCMODE|IPNS配置方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|NSVC的配置模式。用于标识NSVC的配置方式及归属NSE的承载模式。取值含义：Invalid：无效。即NSVC归属的NSE为FR承载模式。Static：静态。即NSVC归属的NSE为IP承载，且为静态模式。Dynamic：动态。即NSVC归属的NSE为IP承载，且为动态配置模式。
VRF|VRF标识|参数可选性:任选参数；参数类型:整数。|等同于VPNID，用于指定IP路由虚拟路由域，表示IP路由时选择该VRF关联的路由域内路由，起到隔离路由域的作用。
RALIST|路由区列表|参数可选性:任选参数；参数类型:字符型。|NSE的关联路由区列表。该参数用于表示NSE下已经建立的所有 PTP BVC归属的路由区（RAI）列表。目前最多显示8个RAI，若多于8个RAI，只显示前8个。
ALLRAFLAG|已输出所有路由区|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于标识某个NSE关联的路由区列表是否已经全部显示。






[](None)命令举例 


查询全部NSE及路由区信息。 


 SHOW ALL NSE RAI 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW ALL NSE RAI

NSE标识   NSE是否空闲   承载方式   IPNS配置方式   VRF标识   路由区列表                    已输出所有路由区
----------------------------------------------------------------------------------------------------------
191       活跃          IP         静态           0                                       是
81        活跃          FR         无效           0         46016-0051-51                 是
1         活跃          IP         静态           0         460010-1102-02                是
2         活跃          IP         静态           0         460100-1101-02                是
100       活跃          IP         静态           0         46003-1071-01&46003-1071-02   是
400       活跃          IP         动态           0                                       是
----------------------------------------------------------------------------------------------------------
记录数 20

命令执行成功（耗时 0.052 秒）。                                                                                            
` 








父主题： [GB口动态管理](../../zh-CN/tree/N_130840073.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 基于NSE/路由区/小区查询BVC信息(SHOW BVC BY POLICY) 
### 基于NSE/路由区/小区查询BVC信息(SHOW BVC BY POLICY) 


[](None)命令功能 


该命令用于基于NSE/路由区/小区查询BVC信息。 




[](None)注意事项 


同组的NSE标识（NSEI）、路由区标识（RAI）、小区全局标识（CGI）必须单选，即只能输入且必须输入一个参数。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必须单选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
RAI|路由区标识|参数可选性:必须单选参数；参数类型:复合参数|该参数用于识别网络中的路由区。应该根据网络规划进行命名。
CGI|小区全局标识|参数可选性:必须单选参数；参数类型:复合参数|小区全球标识，能在全球范围内唯一标识一个移动小区，由MCC、MNC、LAC、CI组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
LAC|位置区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|位置区编码用于识别网络中的位置区。应该根据网络规划进行编码。
RAC|路由区码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~2个字符。|路由区编码用于识别网络中的路由区。应该根据网络规划进行编码。
CI|小区标识(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|小区标识用于识别一个2G蜂窝数据小区。应该根据网络规划进行命名。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于标识Gb口动态维护命令的操作结果。
NSEI|NSE标识|参数可选性:任选参数；参数类型:整数。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
BVCI|BVC标识|参数可选性:任选参数；参数类型:整数。|BVCI（BSSGP Virtual Connection Identifier，BSSGP虚连接标识符）和NSEI一起用于标识一个2G的小区，此配置需要和BSC的配置完全匹配。每NSEI下最多创建1024个BVC，全局容量可配置，最多60000个。
BVCSTATUS|BVC状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|BVC状态，用于标识小区传输上行数据的能力。
RAI|路由区标识|参数可选性:任选参数；参数类型:字符型。|该参数用于识别网络中的路由区。应该根据网络规划进行命名。
CI|小区标识(HEX)|参数可选性:任选参数；参数类型:字符型。|小区标识用于识别一个2G蜂窝数据小区。应该根据网络规划进行命名。






[](None)命令举例 


基于NSE标识为100查询BVC信息。 


SHOW BVC BY POLICY:NSEI=100; 


` 
                                                                                                                                                                                                               
命令 (No.1): SHOW BVC BY POLICY:NSEI=100;

NSE标识   BVC标识   BVC状态   路由区标识      小区标识(HEX)
-----------------------------------------------------------
100       1         活跃      46003-1071-01   0101
100       2         活跃      46003-1071-02   0101
-----------------------------------------------------------
记录数 2

命令执行成功（耗时 0.072 秒）。

                                                                                              
` 








父主题： [GB口动态管理](../../zh-CN/tree/N_130840073.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 负荷动态管理 
## 负荷动态管理 


[](None)背景知识 

            
            负荷动态管理是指人工控制和参与系统的负荷控制。
        


[](None)功能描述 

            
            负荷动态管理包括人工控制和管理当前的负荷。
        


[](None)相关主题 



 

SGSN负荷卸载请求(EXEC UNLOAD)
 

 

SGSN负荷卸载取消(CANCEL UNLOAD)
 

 

SGSN负荷卸载状态查询(SHOW UNLOADSTATE)
 

 

MME负荷重平衡请求(EXEC REBALANCE)
 

 

MME负荷重平衡取消(CANCEL REBALANCE)
 

 

MME负荷重平衡状态查询(SHOW REBALANCESTATE)
 

 

查询备用网元状态(SHOW BAKNE STATE)
 

 

调整备用网元状态(ADJUST BAKNE STATE)
 

 

MME负荷重平衡信息查询(SHOW MME REBALANCE PROC)
 

 

SGSN负荷卸载过程查询(SHOW SGSN UNLOAD PROC)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGSN负荷卸载请求(EXEC UNLOAD) 
### SGSN负荷卸载请求(EXEC UNLOAD) 


[](None)命令功能 


该命令用于启动负荷卸载功能。当POOL内某个SGSN负荷过高或者该SGSN需要进行升级操作时，可以使用负荷卸载功能将该局的用户迁移到其他SGSN。 



 
如果采用按SGSN卸载，表明是将该SGSN下的用户迁移到SGSN POOL内的其他SGSN。
 

 
如果采用按MSC卸载，表明是将该SGSN下选择了需卸载VLR的用户迁移到MSC POOL下的其他VLR。
 

 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ACT|卸载类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于选择需要进行的负荷卸载类型，系统支持卸载SGSN（SGSN）和卸载MSC（MSC）两种方式。如果选择卸载SGSN（SGSN），表明此次执行的负荷卸载是将该SGSN下的用户迁移到SGSN POOL内的其他SGSN。如果选择卸载MSC（MSC），表明此次执行的负荷卸载是将选择了该特定VLR的用户选择到MSC POOL的其他MSC。
SC|CMP实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|该参数为SC逻辑编号，可通过SHOW SCINFO命令查询。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
VLR|需要卸载的VLR号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~16个字符。|该配置在按MSC负荷卸载时生效。当执行MSC负荷卸载时，需要由CS侧提供该号码。
TYPE|SGSN卸载方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该配置在按SGSN负荷卸载时生效。执行按SGSN负荷卸载时，在不同的卸载方式下，系统对需要卸载的用户的判断以及卸载结束的判断会有差别。根据实际需要选择相应的卸载方式。按比例卸载SGSN，系统针对从支持FLEX的RAN接入且散落在需卸载的CMP实例的用户满足进行负荷卸载。当前在线用户比例小于FLEX配置中的重分配完成用户数门限时结束负荷卸载。按用户数卸载SGSN，系统针对从支持FLEX的RAN接入且散落在需卸载的CMP实例的用户进行负荷卸载。当统计到的卸载用户数大于FLEX配置中的重分配需卸载用户数时结束负荷卸载。按BSC/RNC负荷卸载配置卸载，系统针对从基于BSC/RNC负荷卸载配置中配置的BSC/RNC接入的用户进行负荷卸载。默认时当FLEX配置中的负荷卸载等待时间超时后结束负荷卸载。按RAI负荷卸载配置卸载，系统针对从基于RAI的负荷卸载配置中配置的RAI接入的用户进行负荷卸载。默认时当FLEX配置中的负荷卸载保护定时器超时后结束负荷卸载。按指定IMSI号段负荷卸载配置卸载，系统针对IMSI号码符合基于IMSI号段的负荷卸载配置的用户进行负荷卸载。默认时当FLEX配置中的负荷卸载保护定时器超时后结束负荷卸载。按指定MSISDN号段负荷卸载配置卸载，系统针对MSISDN号码符合基于MSISDN号段的负荷卸载配置的用户进行负荷卸载。默认时当FLEX配置中的负荷卸载保护定时器超时后结束负荷卸载。






[](None)命令举例 


执行按比例的SGSN负荷卸载。 


EXEC UNLOAD:ACT="SGSN",VM="ZTE_UMAC_55_CMP_1_L"-1,TYPE="BY_RATE" 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGSN负荷卸载取消(CANCEL UNLOAD) 
### SGSN负荷卸载取消(CANCEL UNLOAD) 


[](None)命令功能 


该命令用于手动终止负荷卸载。在负荷卸载过程中，通过查询负荷卸载情况决定可以结束负荷卸载时，可以使用该命令。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ACT|卸载取消类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于选择需要进行的取消负荷卸载类型，系统支持取消卸载SGSN（SGSN）和取消卸载MSC（MSC）两种方式。取消卸载SGSN（SGSN），表明此次取消的负荷卸载是将该SGSN下的用户迁移到SGSN POOL内的其他SGSN。取消卸载MSC（MSC），表明此次取消的负荷卸载是将选择了该特定VLR的用户选择到MSC POOL的其他MSC。






[](None)命令举例 


终止SGSN负荷卸载。 


CANCEL UNLOAD:ACT="SGSN" 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGSN负荷卸载状态查询(SHOW UNLOADSTATE) 
### SGSN负荷卸载状态查询(SHOW UNLOADSTATE) 


[](None)命令功能 


该命令用于查询系统的卸载情况，该命令不需要填写参数。在执行负荷卸载过程中，可以执行该命令查看当前在线用户比例，已卸载用户数等信息，以及时了解卸载状态，判断是否可以手动停止卸载。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|请求消息上报的类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|请求消息上报的类别。
RESPONSE_RESULT|请求消息返回的结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明当前命令执行是成功还是失败。
REJECT_CAUSE|拒绝请求操作的原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数提示当前命令执行失败的原因。正在卸载中，请求的实例或者VLR号码与当前正在卸载的有冲突。该原因出现在系统已经进行负荷卸载，再次执行该类型的负荷卸载时，填写的实例号与当前已经在卸载的实例号重复，或者填写的VLR号码与已经在卸载的VLR号码不一致的场景。卸载请求类型和当前卸载类型冲突。该原因出现在系统已经处于负荷卸载时，执行其他卸载方式的负荷卸载的场景。卸载取消时系统未处于卸载状态。该原因出现在当前系统没有出现负荷卸载状态，却执行了负荷卸载取消命令的场景。系统内部检查错误。该原因值出现在SGSN没有打开FLEX特性，却执行了负荷卸载的场景。请求参数非法。该原因值出现在执行按MSC方式负荷卸载时，却没有填写VLR号码的场景。系统忙。该原因值出现在系统在执行负荷卸载期间，处于内部消息分发时，收到网管执行的负荷卸载相关命令的场景。建议稍等片刻后再次操作。
SYSTEM_STATE|操作成功时的系统状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明当前命令执行成功时系统所处的状态。系统没有处于卸载状态，SGSN没有进行负荷卸载。正在卸载SGSN，系统进行按SGSN方式的负荷卸载。正在卸载MSC，系统进行按MSC方式的负荷卸载。SGSN卸载完成，系统完成按SGSN方式的负荷卸载。MSC卸载完成，系统完成按MSC方式的负荷卸载。
REPORT_RESULT|主动上报卸载结束的结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该字段暂不使用。
FAIL_CAUSE|卸载失败的原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该字段暂不使用。
USER_RATE|当前在线用户的比例（万分比）|参数可选性:任选参数；参数类型:整数。|参数表明当前在线用户数的比例。以当前卸载实例的在线用户数除以卸载开始时的在线用户数计算得到并转换成万分比。
MODULE_COUNT|本次上报的实例的数目|参数可选性:任选参数；参数类型:整数。|参数表明执行卸载的模块个数。
SC|CMP实例号|参数可选性:任选参数；参数类型:整数。|需要进行卸载的MP实例，不填写该数值时表示采用默认方式，默认方式为针对所有MP实例进行负荷卸载。按BSC/RNC、RAI、IMSI号段、MSISDN号段方式进行SGSN卸载时，只能针对所有MP实例进行卸载。按比例或按用户数进行SGSN卸载、以及按照MSC负荷卸载时，可以选择指定的MP实例进行卸载。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
MODULE_STATE|实例的状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数表明执行了卸载的各个实例的状态。系统处于正常状态，表明该实例已经结束负荷卸载。系统处于负荷重分配状态，表明该实例处于负荷卸载状态。系统处于未知状态，表明实例出现故障，状态未知。
USER_NUMBER|本模块的在线用户数|参数可选性:任选参数；参数类型:整数。|参数表明当前该模块的在线用户数目。统计非分离态的用户。
GS_USER|本模块的具有Gs口连接的用户数|参数可选性:任选参数；参数类型:整数。|参数表明当前该实例具有Gs口连接的用户数。
VLR_COUNT|正在处理卸载的MSC个数|参数可选性:任选参数；参数类型:整数。|参数表明进行MSC卸载时，卸载的MSC个数。
VLRCODE|VLR号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~16个字符。|参数表明进行MSC卸载时，卸载所针对的VLR号码。
UNLOADED|已卸载用户数|参数可选性:任选参数；参数类型:整数。|该参数累加此次负荷卸载过程已经卸载的用户数。满足卸载条件的用户触发附着流程或者RAU流程，SGSN在附着接受消息或者RAU接受消息分配包含NULL NRI的PTMSI及非广播路由区时，已卸载用户数加一。






[](None)命令举例 


查询当前卸载状态。 


SHOW UNLOADSTATE 


`

命令 (No.1): SHOW UNLOADSTATE

请求消息上报的类别 
---------------------
请求响应 
---------------------
记录数 1

请求消息返回的结果 
---------------------
处理了请求操作 
---------------------
记录数 1

操作成功时的系统状态 
-----------------------
正在卸载SGSN 
-----------------------
记录数 1

当前在线用户的比例（万分比） 
-------------------------------
10000 
-------------------------------
记录数 1

本次上报的实例的数目 
-----------------------
1 
-----------------------
记录数 1

已卸载用户数 
---------------
0 
---------------
记录数 1


CMP实例号   实例的状态             本模块的在线用户数   本模块的具有Gs口连接的用户数
---------------------------------------------------------------------------------
255      负荷卸载状态           5                    0
---------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。


` 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### MME负荷重平衡请求(EXEC REBALANCE) 
### MME负荷重平衡请求(EXEC REBALANCE) 


[](None)命令功能 


该命令用于启动负荷重平衡功能。当POOL内某个MME负荷过高或者该MME需要进行升级操作时，可以使用负荷重平衡功能将该局的用户迁移到其他MME。 



 
如果采用按保留用户千分比卸载，表明MME按照千分比计算保留多少用户，将其他用户迁移到POOL内的其他MME。
 

 
如果采用按卸载用户数卸载，表明是MME按照配置的用户个数将这些用户迁移到POOL内的其他MME。
 

 
如果采用按eNodeB列表卸载，表明MME按照配置的eNodeB列表将列表内用户迁移到POOL内的其他MME。
 

 
如果采用按IMSI号段卸载，表明MME按照配置的IMSI号段将该号段的用户迁移到POOL内的其他MME。
 

 
如果采用按MSISDN号段卸载，表明MME按照配置的MSISDN号段将该号段的用户迁移到POOL内的其他MME。
 

 
如果采用按SC实例号卸载，表明MME按照SC实例号将该SC实例号对应模块下的用户迁移到POOL内的其他MME。
 

 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ACT|卸载类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于选择需要进行的卸载类型。如果采用按保留用户千分比卸载，表明MME按照千分比计算保留多少用户，将其他用户迁移到POOL内的其他MME。如果采用按卸载用户数卸载，表明是MME按照配置的用户个数将这些用户迁移到POOL内的其他MME。如果采用按eNodeB列表卸载，表明MME按照配置的eNodeB列表将列表内用户迁移到POOL内的其他MME。如果采用按IMSI号段卸载，表明MME按照配置的IMSI号段将该号段的用户迁移到POOL内的其他MME。如果采用按MSISDN号段卸载，表明MME按照配置的MSISDN号段将该号段的用户迁移到POOL内的其他MME。如果采用按SC实例号卸载，表明MME按照SC实例号将该SC实例号对应模块下的用户迁移到POOL内的其他MME。
RATE|保留用户千分比|参数可选性:任选参数；参数类型:整数；参数范围为:0~999。|该配置在按保留用户千分比进行负荷重平衡时生效。
USERCNT|卸载用户数|参数可选性:任选参数；参数类型:整数。|该配置在按卸载用户数进行负荷重平衡时生效。
ENBIDS|eNodeB列表|参数可选性:任选参数；参数类型:复合参数|该配置在按eNodeB进行负荷重平衡时生效。
NUMSEG|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:5~15个字符。|该配置在按IMSI/MSISDN号段进行负荷重平衡时生效。
SC|CMP实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|该参数为SC逻辑编号，可通过SHOW SCINFO命令查询。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
STEP|负荷卸载步长|参数可选性:必选参数；参数类型:整数；参数范围为:1~100。默认值:5。|该参数控制MME网元全局负荷卸载第一阶段和第二阶段的卸载速率，设定MME网元全局被动卸载和主动卸载用户的步长，固定0.1秒卸载多少用户。卸载预处理期间（卸载第一阶段）：MME网元全局按照此卸载步长控制活动用户卸载速率。卸载预处理时间超时后（卸载第二阶段）：在MME卸载预处理时间超时之后，按照此步长控制全局扫描用户和活动用户的卸载速率。
PRELTIME|卸载预处理时间(分钟)|参数可选性:必选参数；参数类型:整数；参数范围为:1~1440。默认值:54。|该配置用于设定卸载预处理时间，在该时长内，MME等待用户主动卸载。单位：分钟
MCC|移动国家码(MCC)|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。






[](None)命令举例 


执行MME负荷重平衡。 


EXEC REBALANCE:ACT="BY_USERNUM",USERCNT=32,STEP=5,PRELTIME=54 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### MME负荷重平衡取消(CANCEL REBALANCE) 
### MME负荷重平衡取消(CANCEL REBALANCE) 


[](None)命令功能 


该命令用于手动终止负荷重平衡。在负荷重平衡过程中，通过查询负荷重平衡情况决定可以结束负荷重平衡时，可以使用该命令。 




[](None)注意事项 

无。


[](None)命令举例 


终止MME负荷重平衡。 


CANCEL REBALANCE 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### MME负荷重平衡状态查询(SHOW REBALANCESTATE) 
### MME负荷重平衡状态查询(SHOW REBALANCESTATE) 


[](None)命令功能 


该命令用于查询系统的重平衡情况，该命令不需要填写参数。在执行负荷重平衡过程中，可以执行该命令查看当前卸载的用户数等信息，以及时了解重平衡状态，判断是否可以手动停止负荷重平衡。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|请求消息上报的类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|请求消息上报的类别。
RESPONSE_RESULT|请求消息返回的结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明当前命令执行是成功还是失败。
REJECT_CAUSE|拒绝请求操作的原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数提示当前命令执行失败的原因。正在负荷重平衡中，请求的模块和正在负荷重平衡的模块有冲突。卸载取消时系统未处于卸载状态。系统内部检查错误。请求参数非法。系统忙。
SYSTEM_STATE|操作成功时的系统状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明当前命令执行成功时系统所处的状态。系统没有处于重平衡状态。正在进行MME重平衡。MME重平衡完成。
REPORT_RESULT|主动上报重平衡结束的结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该字段暂不使用。
FAIL_CAUSE|重平衡失败的原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该字段暂不使用。
UNLOADED_USER|卸载的用户数|参数可选性:任选参数；参数类型:整数。|该参数累加此次负荷卸载过程已经卸载的用户数。满足卸载条件的用户触发附着流程或者TAU流程，已卸载用户数加一。






[](None)命令举例 


查询MME负荷重平衡状态。 


SHOW REBALANCESTATE 


`

命令 (No.1): SHOW REBALANCESTATE

请求消息上报的类别 
---------------------
请求响应 
---------------------
记录数 1

请求消息返回的结果 
---------------------
处理了请求操作 
---------------------
记录数 1

操作成功时的系统状态 
-----------------------
系统没有处于重平衡状态 
-----------------------
记录数 1

命令执行成功（耗时 0.033 秒）。

` 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询备用网元状态(SHOW BAKNE STATE) 
### 查询备用网元状态(SHOW BAKNE STATE) 


[](None)命令功能 


该命令用于查询备用网元状态（工作态、非工作态）。 


POOL内两个异地的网元可以支持主备配置，其中主用、备用网元角色固定，备用网元仅在主用网元宕机时接替其工作，在主用网元恢复后退出服务。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
BAKSTATE|备用网元状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示本备用网元是否是工作状态。
MASTERSTATE|主用网元状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示对应的主用网元是否正常。






[](None)命令举例 


查询备用网元状态。 


SHOW BAKNE STATE 


`

命令 (No.1): SHOW BAKNE STATE

备用网元状态 主用网元状态 
---------------------------
非备用网元   正常 
---------------------------
记录数 1

命令执行成功（耗时 0.473 秒）。

` 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 调整备用网元状态(ADJUST BAKNE STATE) 
### 调整备用网元状态(ADJUST BAKNE STATE) 


[](None)命令功能 


该命令用于强制调整备用网元状态。 


POOL内两个异地的网元可以支持主备配置，其中主用、备用网元角色固定，备用网元仅在主用网元宕机时接替其工作，在主用网元恢复后退出服务。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ACTION|操作类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示管理人员操作行为。






[](None)命令举例 


调整备用网元状态。 


ADJUST BAKNE STATE:ACTION="CANCEL" 


`

命令 (No.1): ADJUST BAKNE STATE:ACTION="CANCEL"

操作结果 
-------------
非备用网元 
-------------
记录数 1

命令执行成功（耗时 3.998 秒）。

` 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### MME负荷重平衡信息查询(SHOW MME REBALANCE PROC) 
### MME负荷重平衡信息查询(SHOW MME REBALANCE PROC) 


[](None)命令功能 


该命令用于查询MME负荷重平衡的详细卸载情况。 


在执行负荷重平衡过程中，可以定时执行该命令查看当前卸载的详细信息，及时了解重平衡整个过程。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PERIODTIME|时间|参数可选性:任选参数；参数类型:字符型。|该参数表示当前负载重平衡周期时间。
UNLOADPHASE|卸载阶段|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示当前所处的负载重平衡阶段。
UNLOADUSERNUM|卸载初期用户数|参数可选性:任选参数；参数类型:整数。|该参数表示在当前周期内卸载的用户数。
REMAINUSERS|剩余用户数|参数可选性:任选参数；参数类型:整数。|该参数表示负载重平衡过程中，本局剩余的用户数。
PERIODSERVNUM|周期内用户活动次数|参数可选性:任选参数；参数类型:整数。|该参数表示在当前周期内用户主动接入的次数。
UESERVUNLOADNUM|UE触发卸载用户数|参数可选性:任选参数；参数类型:整数。|该参数表示在当前周期内UE主动接入触发卸载的用户数。
SCANUNLOADNUM|扫描卸载用户数|参数可选性:任选参数；参数类型:整数。|该参数表示在当前周期内扫描卸载的用户数。






[](None)命令举例 


查询MME负荷卸载详细信息。 


SHOW MME UNLOAD PROC 


`

命令 (No.1): SHOW MME UNLOAD PROC
时间                卸载阶段 卸载初期用户数 剩余用户数 周期内用户活动次数 UE触发卸载用户数 扫描卸载用户数 
----------------------------------------------------------------------------------------------------------      
2021-06-01 18:25:24 第一阶段 1000           1115       148                136              0              
2021-06-01 18:25:28 第一阶段 1000           1236       178                144              0              
----------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.063 秒）。
 ` 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGSN负荷卸载过程查询(SHOW SGSN UNLOAD PROC) 
### SGSN负荷卸载过程查询(SHOW SGSN UNLOAD PROC) 


[](None)命令功能 


该命令用于查询SGSN负荷卸载的详细卸载情况。 


在执行负荷卸载过程中，可以定时执行该命令查看当前卸载的详细信息，及时了解卸载整个过程。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PERIODTIME|时间|参数可选性:任选参数；参数类型:字符型。|该参数表示当前负载重平衡周期时间。
UNLOADPHASE|卸载阶段|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示当前所处的负载重平衡阶段。
UNLOADUSERNUM|卸载初期用户数|参数可选性:任选参数；参数类型:整数。|该参数表示在当前周期内卸载的用户数。
REMAINUSERS|剩余用户数|参数可选性:任选参数；参数类型:整数。|该参数表示负载重平衡过程中，本局剩余的用户数。
PERIODSERVNUM|周期内用户活动次数|参数可选性:任选参数；参数类型:整数。|该参数表示在当前周期内用户主动接入的次数。
UESERVUNLOADNUM|UE触发卸载用户数|参数可选性:任选参数；参数类型:整数。|该参数表示在当前周期内UE主动接入触发卸载的用户数。
SCANUNLOADNUM|扫描卸载用户数|参数可选性:任选参数；参数类型:整数。|该参数表示在当前周期内扫描卸载的用户数。






[](None)命令举例 


查询SGSN负荷卸载详细信息。 


SHOW SGSN UNLOAD PROC 


`

命令 (No.1): SHOW SGSN UNLOAD PROC
时间                卸载阶段 卸载初期用户数 剩余用户数 周期内用户活动次数 UE触发卸载用户数 扫描卸载用户数 
----------------------------------------------------------------------------------------------------------
2021-06-01 18:34:23 第一阶段 1000           997        216                160              0              
2021-06-01 18:34:27 第一阶段 1000           998        213                160              0              
----------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.063 秒）。
 ` 








父主题： [负荷动态管理](../../zh-CN/tree/N_130840093.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 用户动态管理 
## 用户动态管理 


[](None)背景知识 

            
            用户动态管理用于对用户的相关信息进行人工的控制。
        


[](None)功能描述 

            
            用户动态管理包括重分配PTMSI、重分配GUTI以及查询用户的相关信息。
        


[](None)相关主题 



 

查询用户群信息(SHOW IMSI RESGROUP)
 

 

查询模块上CMP群号(SHOW CMP GROUP)
 

 

查询模块上2G USUP群号(SHOW 2G UP GROUP)
 

 

查询模块上3G USUP群号(SHOW 3G UP GROUP)
 

 

基于号码查询用户CMP实例号(SHOW CMP MODULE)
 

 

Multi-SIM 查询(SHOW COMMON MSISDN)
 

 

删除LTE无线接入能力(DELETE LTE ACCESS)
 

 

分离移动用户(DETACH USER)
 

 

重分配P-TMSI(REALLOC PTMSI)
 

 

重分配GUTI(REALLOC GUTI)
 

 

删除PDP数据区(DELETE PDPCTX)
 

 

修改PDP(MODIFY PDP)
 

 

发送或删除无线接入能力(MOO RAC)
 

 

强制出GMM话单(REL MCDR)
 

 

强制出SM话单(REL SCDR)
 

 

上报数据(REPORT DATAVOL)
 

 

清除签约用户(PURGE SUBS)
 

 

删除EPS承载(DELETE EPS BEAR)
 

 

查询SGSN用户动态信息(SHOW SGSNUSERDYN)
 

 

查询SGSN用户动态简要信息(SHOW SGSNBRIEFUSERDYN)
 

 

查询SGSN用户签约信息(SHOW SGSNUSERSUB)
 

 

SGSN网投信息查询(SHOW SGSN COMPLAINT INFORMATION)
 

 

查询MME用户动态信息(SHOW MMEUSERDYN)
 

 

查询MME用户动态简要信息(SHOW MMEBRIEFUSERDYN)
 

 

查询MME用户签约信息(SHOW MMEUSERSUB)
 

 

MME网投信息查询(SHOW MME COMPLAINT INFORMATION)
 

 

GSN节点链路检测(GTP ECHO)
 

 

MME Multi-SIM 查询(SHOW MME COMMON MSISDN)
 

 

查询用户数据(SHOW USERDATA)
 

 

查询IMSI信息(SHOW GUTI IMSI)
 

 

查询备份用户信息(SHOW BAKDATAPOOL)
 

 

清空备份数据(CLEAR BAKDATA)
 

 

同步备份数据(SYN BAKDATA)
 

 

取消备份数据同步(CANCEL BAKDATA SYN)
 

 

用户卸载到指定MME(UNLOAD MME USER)
 

 

用户卸载到指定SGSN(UNLOAD SGSN USER)
 

 

查询MTC终端用户动态信息(SHOW MTC USER DYNAMIC INFO)
 

 

同步用户信息(CDB SYN)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询用户群信息(SHOW IMSI RESGROUP) 
### 查询用户群信息(SHOW IMSI RESGROUP) 


[](None)命令功能 


该命令用于查询用户相关群信息。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
CMPGROUP|CMP群|参数可选性:必选参数；参数类型:字符型。|用户归属的的CMP群号。
CMPSC|CMP实例号|参数可选性:必选参数；参数类型:字符型。|用户归属的的CMP实例号。
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
NETYPE|当前用户归属网元|参数可选性:必选参数；参数类型:字符型。|该参数用于Combo局时指示用户接入的网元类型。取值含义：SGSN：接入网元为SGSN。MME：接入网元为MME。
2GUPGROUP|2G UP群|参数可选性:必选参数；参数类型:字符型。|2G用户归属的的2G USUP群号。
2GUPSC|归属2G UP实例号|参数可选性:必选参数；参数类型:字符型。|2G用户归属的的2G USUP实例号。
3GUPGROUP|3G UP群|参数可选性:必选参数；参数类型:字符型。|3G用户归属的的2G USUP群号。
3GUPSC|归属3G UP实例号|参数可选性:必选参数；参数类型:字符型。|3G用户归属的的2G USUP实例号。






[](None)命令举例 


查询460119990020000用户相关群信息。 


SHOW IMSI RESGROUP:IMSI="460119990020000";
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW IMSI RESGROUP:IMSI="460119990020000";

CMP群   CMP模块   当前用户归属网元   2G USUP群   归属2G USUP模块号   3G USUP群   归属3G USUP模块号
------------------------------------------------------------------------------------------
600     2         SGSN               600       1025              600       1025
------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.055 秒）。
                                                                 
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询模块上CMP群号(SHOW CMP GROUP) 
### 查询模块上CMP群号(SHOW CMP GROUP) 


[](None)命令功能 


该命令用于查询CMP群分担所在的CMP模块。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65534。|实例号
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
CMPGROUP|CMP群号|参数可选性:必选参数；参数类型:整数。|该参数指示CMP模块关联的CMP群。
SC|实例号|参数可选性:必选参数；参数类型:整数。|实例号
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)命令举例 


查询CMP群分担所在的CMP模块。 


 SHOW CMP GROUP;
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW CMP GROUP

CMP群号   实例号
-------------------
0         1
1         1
...       ...
...       ...   
...       ...
8190      1
8191      1
-------------------
记录数 8192

命令执行成功（耗时 0.197 秒）。
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询模块上2G USUP群号(SHOW 2G UP GROUP) 
### 查询模块上2G USUP群号(SHOW 2G UP GROUP) 


[](None)命令功能 


该命令用于查询2G USUP群分担所在USUP模块。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65534。|实例号






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
2GUPGROUP|2G USUP群号|参数可选性:必选参数；参数类型:整数。|该参数指示2G USUP模块关联的2G USUP群。
SC|实例号|参数可选性:必选参数；参数类型:整数。|实例号






[](None)命令举例 


查询2G USUP群分担所在USUP模块。 


SHOW 2G UP GROUP;
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW 2G UP GROUP

2G USUP群号   实例号
-----------------------
0             1
1             1
...           ...
...           ...
...           ...
8190          1
8191          1
-----------------------
记录数 8192

命令执行成功（耗时 0.301 秒）。                                                                  
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询模块上3G USUP群号(SHOW 3G UP GROUP) 
### 查询模块上3G USUP群号(SHOW 3G UP GROUP) 


[](None)命令功能 


该命令用于查询3G USUP群分担所在USUP模块。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65534。|实例号






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
3GUPGROUP|3G USUP群号|参数可选性:必选参数；参数类型:整数。|该参数指示3G USUP模块关联的3G USUP群。
SC|实例号|参数可选性:必选参数；参数类型:整数。|实例号






[](None)命令举例 


查询3G USUP群分担所在USUP模块。 


SHOW 3G UP GROUP;
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW 3G UP GROUP

3G USUP群号   实例号
-----------------------
0             1
1             1
...           ...
...           ...
...           ...
8190          1
8191          1
-----------------------
记录数 8192

命令执行成功（耗时 0.304 秒）。                                                            
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 基于号码查询用户CMP实例号(SHOW CMP MODULE) 
### 基于号码查询用户CMP实例号(SHOW CMP MODULE) 


[](None)命令功能 


该命令用于查询用户分担所在的CMP实例号。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
MSID|IMSI/MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NETYPE|逻辑网元类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于Combo局时指示用户接入的网元类型。取值含义：SGSN：接入网元为SGSN。MME：接入网元为MME。
CMPSC|CMP逻辑编号|参数可选性:任选参数；参数类型:整数。|用户归属的的CMP实例号。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
MSISDN|MSISDN|参数可选性:任选参数；参数类型:字符型。|用户的MSISDN号码。MSISDN(MS international PSTN/ISDN Number)是移动用户号码，是主叫用户为呼叫移动通信网中用户所需拨号的号码。MSISDN号码最长是15位数字，由CC+NDC+SN三部分组成。CC是国家码，NDC是国家目的码，SN是用户号码。
IMEI|IMEI|参数可选性:任选参数；参数类型:字符型。|用户的IMEI号码。该参数用于指示IMEI（International Mobile station Equipment Identity，国际移动设备标识）。该参数是区别终端的标志，使用0～9的数字，且总长度不超过15。






[](None)命令举例 


查询460119990020000分担所在的CMP实例。 


SHOW CMP MODULE:TYPE="IMSI",MSID="460119990020000";
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW CMP MODULE:TYPE="IMSI",MSID="460119990020000";

逻辑网元类型   CMP实例号    IMSI              MSISDN          IMEI
------------------------------------------------------------------
SGSN           2            460119990020000   9919990020000   
------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.064 秒）。
                                                             
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Multi-SIM 查询(SHOW COMMON MSISDN) 
### Multi-SIM 查询(SHOW COMMON MSISDN) 


[](None)命令功能 


该命令用于查询公共MSISDN号码用户相关信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
COMMONMSISDN|共有MSISDN号码|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|命令查询所携带的COMMON MSISDN。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示命令执行的结果。取值含义：Success：操作结果成功。Failure：操作结果失败。
COMMONMSISDN|共有MSISDN号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|命令查询所携带的COMMON MSISDN。
IMSI|IMSI号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
INDIVIDUALMSISDN|私有MSISDN号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|该COMMON MSISDN关联的MSISDN号码。
IMEI|IMEISV|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|该COMMON MSISDN关联的IMEISV。
USERSTATE|用户状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该COMMON MSISDN关联的用户状态。
GRAYLISTSTATE|灰名单状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该COMMON MSISDN关联的用户灰名单状态。






[](None)命令举例 


SGSN查询COMMON MSISDN为"08613900000001"的相关用户信息； 


SHOW COMMON MSISDN:COMMONMSISDN="08613900000001"; 


`

命令 (No.15): SHOW COMMON MSISDN:COMMONMSISDN="08613900000001";

共有MSISDN号码 
-----------------
08613900000001 
-----------------
记录数 1

INFO
IMSI号码 私有MSISDN号码 IMEISV 用户状态 灰名单状态 
----------------------------------------------------------------------------------
460010000055000 861380055000  UMTS Connected 白名单 
----------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.051 秒）。
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除LTE无线接入能力(DELETE LTE ACCESS) 
### 删除LTE无线接入能力(DELETE LTE ACCESS) 


[](None)命令功能 


该命令用于删除单个用户的LTE无线接入能力。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|用户ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
MSID|IMSI/MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。






[](None)命令举例 


删除IMSI为460020011900100的用户的LTE无线接入能力。 


DELETE LTE ACCESS:TYPE=IMSI,MSID="460020011900100"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 分离移动用户(DETACH USER) 
### 分离移动用户(DETACH USER) 


[](None)命令功能 


该命令用于网络侧分离单个用户。当需要分离某个已附着用户时使用该命令。该命令执行成功后，用户会被分离。 


该命令只能通过输入用户的IMSI进行分离，并且分离方式分为3种：需要重附着（REQUEST）、不需要重附着（NOT REQUEST）、IMSI分离（IMSI DETACH）。该分离方式会通过分离请求消息（Detach Request）中的DetachType字段携带给终端，终端根据携带的分离方式判断是否需要重新附着。 


如果输入的用户不存在，该命令会执行失败。 




[](None)注意事项 



 
如果被分离用户存在激活的PDP，在进行网络侧分离时会同时触发PDP去活流程删除PDP上下文。
 

 
分离方式默认为“需要重附着（REQUEST）”
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
TYPE|分离方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REQUEST。|该参数用于指示分离方式。取值含义：REQUEST：需要重附着。NOT REQUEST：不需要重附着。IMSI DETACH：IMSI分离。






[](None)命令举例 


分离IMSI为460020011900100的用户，分离方式为“需要重附着”。 


DETACH USER:IMSI="460020011900100",TYPE=REQUEST; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 重分配P-TMSI(REALLOC PTMSI) 
### 重分配P-TMSI(REALLOC PTMSI) 


[](None)命令功能 


该命令用于重新分配一个新的PTMSI给用户，当需要强制给用户重新分配新的PTMSI时，使用该命令。 


PTMSI是分组域的临时移动用户识别码，用于临时识别一个用户的身份。使用户更安全，在用户接入SGSN发起附着流程后，SGSN会分配一个全新的PTMSI给用户，当用户RAI发生变化或者周期性路由区更新定时器到期后，终端会触发路由区更新流程，在更新流程结束时，SGSN也会给用户分配一个PTMSI。老的PTMSI就被释放，不能够再识别这个用户。当运维人员希望对某个用户的PTMSI进行重分配时候使用此流程进行强制分配。 


使用该命令后会触发“P-TMSI Reallocation Procedure”。 




[](None)注意事项 



 
用户必须已经在本SGSN中附着成功后，才可以进行此操作。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|用户ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
MSID|IMSI/MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。






[](None)命令举例 


重分配PTMSI，号码类型使用IMSI，号码为460020011900100。 


REALLOC PTMSI:TYPE=IMSI,MSID="460020011900100"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 重分配GUTI(REALLOC GUTI) 
### 重分配GUTI(REALLOC GUTI) 


[](None)命令功能 


该命令用于MME为用户重新分配GUTI。该命令执行成功后，MME会触发GUTI 重分配流程(GUTI Reallocation)，为用户分配一个新的GUTI。 


该命令可以通过输入用户的IMSI或MSISDN的方式进行GUTI重分配。 


如果输入的用户不存在，该命令会执行失败。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|用户ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
MSID|IMSI/MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。
BTALISTREALLOCTAG|是否重分配TA List|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指示是否重分配TA 列表。取值含义：是。否。






[](None)命令举例 


IMSI为460020011900100的用户进行GUTI重分配。 


REALLOC GUTI:TYPE=IMSI,MSID="460020011900100"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除PDP数据区(DELETE PDPCTX) 
### 删除PDP数据区(DELETE PDPCTX) 


[](None)命令功能 


该命令适用于以下两种情况： 


删除特定用户的某一个PDP上下文，此过程会删除SGSN上此用户的PDP上下文。
 

 
需要对某一个用户发起网络侧的去活流程，此过程不仅会删除SGSN上的PDP上下文，还将删除GGSN和MS上的PDP上下文。
 

 




[](None)注意事项 


该命令仅适用于SGSN网元。 


该命令属于危险操作，误操作将导致用户无法正常使用数据业务。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|删除类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:DELETE。|该参数用于指示删除类型。取值含义：DELETE：删除PDP。NETDEACT：网络侧去活。
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NSAPI|NSAPI|参数可选性:必选参数；参数类型:整数；参数范围为:5~15。|该参数用于指定删除的NSAPI（Network Service Access Point Identifier，网络层业务接入点标识），该标识和IMSI一起用于标示同一用户激活的不同PDP上下文。
TEARDOWN|TEARDOWN|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:TRUE。|该参数用于指示删除PDP上下文时，是否携带TEARDOWN标识，TEARDOWN标识的意义参考协议3GPP TS 29.060。根据3GPP 23.060协议，当删除的PDP上下文是某个用户的最后一个PDP上下文时，必须携带TEARDOWN标识，才可以强制删除。因此，在配置DELETE PDPCTX命令时，通常需要将参数“TEARDOWN”配置为“携带”，以保证此命令可以执行成功。取值含义：“TRUE”：删除与该PDP地址相关联的所有PDP上下文。“FALSE”：不删除与该PDP地址相关联的所有PDP上下文，只删除指定NSAPI的PDP上下文。






[](None)命令举例 


该示例命令是为了删除IMSI为“460020011900100”的用户NSAPI为5的PDP，而且删除消息携带TEARDOWN标识。 


DELETE PDPCTX:TYPE="DELETE",IMSI="460020011900100",NSAPI=5,TEARDOWN="TRUE"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改PDP(MODIFY PDP) 
### 修改PDP(MODIFY PDP) 


[](None)命令功能 


该命令用于修改特定用户的某一个PDP上下文对应的QoS参数。 


QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。 


在用户已经激活一个或多个PDP上下文情况下，当需要修改指定的某一个PDP上下文的QoS参数时，使用该命令。 




[](None)注意事项 


该命令仅适用于SGSN网元。 


该命令属于危险操作，误操作将影响用户的上网体验，甚至无法上网。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NSAPI|NSAPI|参数可选性:必选参数；参数类型:整数；参数范围为:5~15。|该参数用于指定删除的NSAPI（Network Service Access Point Identifier，网络层业务接入点标识），该标识和IMSI一起用于标示同一用户激活的不同PDP上下文。
TRUSTY|可靠级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数与业务数据单元错误率（SDU error ratio） 、残余位出错率（Residual bit error ratio）和发送错误数据（Delivery of erroneous SDUs）参数的取值相关，它们的相互取值对应关系，详见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
DELAY|延迟级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数与业务类别（Traffic class） 和流量控制优先级（Traffic handling priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
PRIORITY|优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数与缺省分配/保持优先级（Allocation/Retention priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP 23107(R7)和3GPP 24.008(R7)。
PEAK|峰值吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义为SGSN可以处理的最大链路比特率。取值含义见协议3GPP 24.008(R7)。
MEAN|平均吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义为SGSN可以处理的链路比特率的平均值。取值含义见协议3GPP 24.008(R7)。
MAXBITRATE4UL|上行链路最大比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义是为了便于无线接口上行链路码的预留。取值含义见协议3GPP 24.008(R7)。
MAXBITRATE4DL|下行链路最大比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义是为了便于无线接口下行链路码的预留。取值含义见协议3GPP 24.008(R7)。
TRAFPRIO|流量控制优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义指对不同媒体的SDU处理的优先权。对于同一个承载业务，它和参数“保证上行链路比特率”和“保证下行链路比特率“不能同时出现。取值含义：“1”：优先级1。“2”：优先级2。“3”：优先级3。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义是指在传送SDU中未检测到的信元误码率，用来配置L1的信道编码和检错编码。取值含义见协议3GPP 24.008(R7)。
TRANSDELAY|传输延迟|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义指不同的用户有不同的延迟容忍程度。UTRAN（UMTS Terrestrial Radio Access Network，UMTS陆地无线接入网）可根据这一参数来设定传送格式和ARQ（Automatic Repeat reQuest，自动重传请求）参数。取值含义见协议3GPP 24.008(R7)。
GUARBITRATE4UL|有保证的上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配。见协议3GPP 24.008(R7)。
GUARBITRATE4DL|有保证的下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配。见协议3GPP 24.008(R7)。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义为：“NotDetect”：“不检测”，表示根本不考虑差错检测就进行传送。“Deliver”：“发送”，表示将检测出有错的SDU（Service Data Unit，业务数据单元）标以差错指示后进行传送。“NotDeliver”："不发送"，表示将检测出有错的SDU标以差错指示后进行丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义为SGSN是否按照要求顺序传送SDU，需要根据3GPP 23017(R7)协议而定。取值含义：“Order”：按顺序发送。“NotOrder”：不按顺序发送。
TRAFCLASS|传输类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义为QoS的业务分类。取值含义：“Conversational”：会话类型“Streaming”：流类型“Interactive”：交互类型“Background”：背景类型业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
MAXSDUSIZE|最大SDU|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义为最大业务数据单元长度，用于许可控制。取值含义见协议3GPP 24.008(R7)。
SDUERRRATIO|SDU错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数的含义是指丢失或者检测出差错SDU（Service Data Unit，业务数据单元）的比例，用来配置L2的重发协议和L1的检错编码。取值含义见协议3GPP 24.008(R7)。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|该参数说明SDU数据源的特征。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NOT OPTIMIZED。|该参数只用于交互级业务（Interactive）。即当“业务类别”设置为“交互业务（Interactive）”时才需要设置该参数。取值含义：“NotOptimized”：非最优化信令。“Optimized”：最优化信令。






[](None)命令举例 


该示例命令为了将IMSI为460020011900100的用户NSAPI为5的PDP修改为如下参数： 


MODIFY PDP:IMSI="460020011900100",NSAPI=5,DELAY="1st Class",PRIORITY="1st Class",PEAK="_1000",MEAN="_100",MAXBITRATE4UL="1 kbps",MAXBITRATE4DL="1 kbps",TRAFPRIO="1",RESIDUALBER="5*10-2",TRANSDELAY="10 ms",GUARBITRATE4UL="1 kbps",GUARBITRATE4DL="1 kbps",DELIERRSDU="NO CHECK",DELIORDER="HAVE ORDER",TRAFCLASS="CONVERSATIONAL",MAXSDUSIZE="80 Bits"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 发送或删除无线接入能力(MOO RAC) 
### 发送或删除无线接入能力(MOO RAC) 


[](None)命令功能 


该命令用于向BSC发送特定用户的无线接入能力或者删除SGSN存储的特定用户的无线接入能力，一般用户首次接入SGSN或者无线接入能力发生变化的时候会同步无线接入能力给BSC。当BSC侧与SGSN侧不同步的时候，需要强制同步用户的无线接入能力给BSC时，使用该命令，或者强制删除SGSN本地存储的无线接入能力以便后续用户活跃发送信令给SGSN的时候，SGSN同步最新的无线接入能力给BSC时, 使用此命令。 


无线接入能力代表用户空口支持的特性，BSC可以根据此能力来对用户进行特性化处理。 




[](None)注意事项 



 
用户必须已经在本SGSN中附着成功后，才可以进行此操作。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|用户ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
ACTION|操作类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:SEND。|该参数用于指示用户的号码类型。 取值含义：SEND：操作类型为发送， 强制向BSC发送RA-CAPABILITY消息，同步用户的无线接入能力。DELETE：操作类型为删除，强制删除SGSN本地存储的用户的无线接入能力。
MSID|IMSI/MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。






[](None)命令举例 


向BSC发送IMSI号码为460020011900100的用户的无线接入能力。 


MOO RAC:TYPE=IMSI,ACTION=SEND,MSID="460020011900100"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 强制出GMM话单(REL MCDR) 
### 强制出GMM话单(REL MCDR) 


[](None)命令功能 


该命令可以立即生成某个用户M-CDR话单，上报给计费服务器。一般情况下，当用户分离或者移动到其他SGSN后或者位置改变达到一定次数后会触发M-CDR话单。如果要通过话单看用户当前的信息需要立即生成某个用户的M-CDR话单时，使用该命令。命令执行成功后，可以立刻上报M-CDR话单给CG。 




[](None)注意事项 


用户必须已经在本SGSN中附着成功后，才可以进行此操作。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






[](None)命令举例 


强制出MCDR话单，IMSI为"460020011900100" 


REL MCDR:IMSI="460020011900100" 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 强制出SM话单(REL SCDR) 
### 强制出SM话单(REL SCDR) 


[](None)命令功能 


SM（Session Management，会话管理）话单通常情况下是SGSN按计费时间门限或计费流量门限生成并上报给CG（Charging Gateway，计费网关）的，使用该命令可以立即生成某个用户指定PDP的SM话单，并上报给CG。  




[](None)注意事项 


该命令仅适用于SGSN网元。 


为了保证能够正常查看该命令上报的话单，请先确认SGSN网元是否可以与CG正常通信，有关SGSN与CG的对接配置，可以在命令终端查看“配置管理-〉业务配置-〉计费配置-〉Ga接口配置”下的各个命令。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NSAPI|NSAPI|参数可选性:必选参数；参数类型:整数；参数范围为:5~15。|该参数用于指定删除的NSAPI（Network Service Access Point Identifier，网络层业务接入点标识），该标识和IMSI一起用于标示同一用户激活的不同PDP上下文。






[](None)命令举例 


该命令用于强制出IMSI为"460020011900100"的用户NSAPI为5的PDP的会话管理话单。 


REL SCDR:IMSI="460020011900100",NSAPI=5; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 上报数据(REPORT DATAVOL) 
### 上报数据(REPORT DATAVOL) 


[](None)命令功能 


用户已经激活一个或多个PDP上下文，并且有下行数据流量时，当操作员需要查询某个用户的某个PDP没有成功下发的数据流量时，使用该命令。 


执行该命令后，SGSN将会给RNC发送一条Data Volume Report Request消息，用于查询某个用户指定RAB（Radio Access Bearer，无线接入承载）没有成功下发给终端的无线数据流量。 


当输入“IMSI”和“RAB ID”做为查询参数时，SGSN将查询指定RAB中没有成功下发的无线数据流量。
 

 
当只输入“IMSI”做为查询参数时，SGSN将查询此用户的所有RAB中没有成功下发的无线数据流量。
 

 




[](None)注意事项 

该命令仅适用于SGSN网元。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
VOLRPT|RAB ID|参数可选性:任选参数；参数类型:整数；参数范围为:5~15。默认值:"5"。|该参数用于表示RAB标识。SGSN侧的一个PDP上下文对应RNC侧的一个RAB。在SGSN侧，由NSAPI和IMSI一起用于唯一标识一个用户激活的不同PDP上下文；在RNC侧，由RAB ID和IMSI一起用于唯一标识一个用户激活的不同的RAB，一个RAB和一个PDP上下文是一一对应的。






[](None)命令举例 


该命令请求RNC上报IMSI为"460017700000080"的用户RABID为5的RAB没有成功下发到终端的无线数据流量。 


REPORT DATAVOL:IMSI="460017700000080",RABID="5"; 


`

命令 (No.1): REPORT DATAVOL:IMSI="460017700000080",VOLRPT=5;

IMSI 
-------
460017700000080 
-------
记录数 1

成功的RAB数目 
----------------
1 
----------------
记录数 1

成功的RAB
RABID DTVOLNUM UNSUCCDTVOL DTVOLREFFG DTVOLREF 
-------------------------------------------------------
5 DTVOLNUM0 100000 1 2 
5 DTVOLNUM0 1000 1 1 
-------------------------------------------------------
记录数 2

失败的RAB数目 
----------------
0 
----------------
记录数 1

命令执行成功（耗时 0.984 秒）。
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 清除签约用户(PURGE SUBS) 
### 清除签约用户(PURGE SUBS) 


[](None)命令功能 


该命令用于清除签约用户。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|删除类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
MSID|IMSI/MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。






[](None)命令举例 

清除IMSI为460029990020000的用户。 

PURGE SUBS:TYPE="IMSI",MSID="460029990020000";
 

` 
                                                                                                                                                                                                              
命令 (No.1): PURGE SUBS:TYPE="IMSI",MSID="460029990020000";

操作结果 
-----------
成功 
-----------
记录数 1

号码类型 
-----------
IMSI 
-----------
记录数 1

IMSI/MSISDN 
--------------
460029990020000 
--------------
记录数 1

命令执行成功（耗时 9.998 秒）。                                                          
` 

 "







父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除EPS承载(DELETE EPS BEAR) 
### 删除EPS承载(DELETE EPS BEAR) 


[](None)命令功能 

该命令用于MME删除用户EPS承载。当运营商需要手动删除EPC承载时使用该命令。该命令执行成功后,，如果删除类型是“本地删除”，则MME会释放承载资源，不通知PGW。如果删除类型是“网络侧删除承载”则MME向PGW发送delete bearer command消息。


[](None)注意事项 

如果删除的承载是该IMSI用户最后一条承载，MME将去附着用户。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
BEARID|承载ID|参数可选性:必选参数；参数类型:整数；参数范围为:5~15。|EPC承载的标识。
TYPE|删除类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示删除类型。取值含义：LOCAL：本地删除。NET：网络侧删除承载






[](None)命令举例 


删除用户EPS承载，IMSI为“460020000000100”、承载ID为“5”、删除类型为“本地删除“。 


DELETE EPS BEAR:IMSI="460020000000100",BEARID=5,TYPE="LOCAL" 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGSN用户动态信息(SHOW SGSNUSERDYN) 
### 查询SGSN用户动态信息(SHOW SGSNUSERDYN) 


[](None)命令功能 


该命令用于查询SGSN用户动态信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERIDTYPE|ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
USERID|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。
ITEM|查询选项|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:USERBASIC&USERDETAIL&PDPBASIC&PDPDETAIL。|查询选项，包括：USERBASIC：查询用户基本信息USERDETAIL：查询用户辅助信息PDPBASIC：查询用户PDP基本信息PDPDETAIL：查询用户PDP辅助信息默认输出以上所有信息。
EXFILE|是否导出到文件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|用于控制输出结果是否生成文件，默认为是。选项包括：否是






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RETCODE|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
RESULT|查询结果|参数可选性:任选参数；参数类型:字符型；参数范围为:0~640000个字符。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。






[](None)命令举例 

查询460119990020000的基本信息。 

SHOW SGSNUSERDYN:USERID="460119990020000",ITEM="USERBASIC";
 

` 
                                                                                                                                                                                                              
命令 (No.1): SHOW SGSNUSERDYN:USERID="460119990020000",ITEM="USERBASIC";

输出文件路径
---------------
当前命令执行的结果被另存为文件，请点击这个URL下载。
http://10.43.86.200:2323/combo_mmegngp_sgsn_200/server/tmp/udm_data/IMSI_460119990020000_20150818203412254.txt
---------------
记录数 1

命令执行成功（耗时 0.034 秒）。                                                                 
` 

 "







父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGSN用户动态简要信息(SHOW SGSNBRIEFUSERDYN) 
### 查询SGSN用户动态简要信息(SHOW SGSNBRIEFUSERDYN) 


[](None)命令功能 

查询SGSN用户动态简要信息


[](None)注意事项 


该命令可通过用户的IMSI号码或MSISDN号码，查询用户基本信息和用户激活PDP数据信息。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERIDTYPE|ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|可根据以下用户号码类型对用户信息进行查询：IMSI：IMSI号码类型MSISDN：MSISDN号码类型
USERID|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|根据已选择的ID类型，输入对应的用户号码。如果ID类型选择IMSI，此处输入IMSI号码。如果ID类型选择MSISDN，此处输入MSISDN号码。
ITEM|查询选项|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:USERBASIC&USERDETAIL&PDPBASIC&PDPDETAIL。|查询选项，包括：USERBASIC：查询用户基本信息USERDETAIL：查询用户辅助信息PDPBASIC：查询用户PDP基本信息PDPDETAIL：查询用户PDP辅助信息默认输出以上所有信息。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RETCODE|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
RESULT|查询结果|参数可选性:任选参数；参数类型:字符型。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。






[](None)命令举例 


查询SGSN用户动态简要信息，查询IMSI为4602121212122用户的动态信息。 


 SHOW SGSNBRIEFUSERDYN:USERIDTYPE="IMSI",USERID="4602121212122",ITEM="USERBASIC"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGSN用户签约信息(SHOW SGSNUSERSUB) 
### 查询SGSN用户签约信息(SHOW SGSNUSERSUB) 


[](None)命令功能 


该命令用于查询SGSN用户签约信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERIDTYPE|ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
USERID|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。
ITEM|查询选项|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:BASICSUB&USERCAMEL&PDPSUB。|查询选项，包括：BASICSUB：用户基本签约信息。USERCAMEL：用户CAMEL信息。PDPSUB：PDP签约信息。默认输出以上所有信息。
EXFILE|是否导出到文件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|用于控制输出结果是否生成文件，默认为是。选项包括：否是






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RETCODE|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
RESULT|查询结果|参数可选性:任选参数；参数类型:字符型；参数范围为:0~640000个字符。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。






[](None)命令举例 


查询460119990020000的基本签约信息。 


SHOW SGSNUSERSUB:USERID="460119990020000",ITEM="BASICSUB";
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW SGSNUSERSUB:USERID="460119990020000",ITEM="BASICSUB";

输出文件路径
---------------
当前命令执行的结果被另存为文件，请点击这个URL下载。
http://10.43.86.200:2323/combo_mmegngp_sgsn_200/server/tmp/udm_data/IMSI_460119990020000_20150818202812611.txt
---------------
记录数 1

命令执行成功（耗时 0.053 秒）。                                                                  
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGSN网投信息查询(SHOW SGSN COMPLAINT INFORMATION) 
### SGSN网投信息查询(SHOW SGSN COMPLAINT INFORMATION) 


[](None)命令功能 


该命令用于在满足各项安全规范的前提下，SGSN针对单个用户（比如,需要排查故障的某个用户）的、不包含通信内容（比如，短/彩信的内容、语音通话的内容等）的、实时历史信息的查询。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示命令执行的结果。取值含义：Success：操作结果成功。Failure：操作结果失败。
SGSNINFO|SGSN信息|参数可选性:任选参数；参数类型:字符型。|显示移动性相关参数，PDP会话参数，如果存在多个PDP，分别显示每一个PDP信息。






[](None)命令举例 


查询460119990022000的SGSN网投信息。 


SHOW SGSN COMPLAINT INFORMATION:IMSI="460119990022000";
 


` 

(No.1) : SHOW SGSN COMPLAINT INFORMATION:IMSI="460119990022000"
-----------------NFS_MMESGSN_0----------------
SGSN信息                                                         
----------------------------------------------------------------
MM Status:      PMM IDLE
CM Status:       
Current RAI:     460-11-2001-c1
RNC:             2431
RAT Restriction: /I-HSPA-Evolution Not Allowed/ 
PDP Information: 
  PDP[0]
    Slice Infomation: 
    APN: pc3.auto.local.mnc011.mcc460.gprs
    GGSN IPv4: 192.20.53.36 
    GGSN Name: pgw.auto1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
 
-------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-28 17:56:17 耗时: 0.916 秒                                                          
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME用户动态信息(SHOW MMEUSERDYN) 
### 查询MME用户动态信息(SHOW MMEUSERDYN) 


[](None)命令功能 


该命令用于查询MME用户动态信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERIDTYPE|ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
USERID|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。
ITEM|查询选项|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:USERBASIC&PDNCONN&EPSBEARER。|可查询到的用户信息，包括：USERBASIC：用户基本信息PDNCONN：PDN连接信息EPSBEARER：用户承载信息默认输出以上所有信息。
EXFILE|是否导出到文件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|用于控制输出结果是否生成文件，默认为是。选项包括：否是






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RETCODE|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
RESULT|查询结果|参数可选性:任选参数；参数类型:字符型；参数范围为:0~640000个字符。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。






[](None)命令举例 


查询MEE用户460119990023000的基本信息。 


SHOW MMEUSERDYN:USERID="460119990023000",ITEM="USERBASIC";
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW MMEUSERDYN:USERID="460119990023000",ITEM="USERBASIC";
-----------------NFS_MMESGSN_0----------------
结果
成功

命令结果的文件路径
af4a69ee430742be9c88787225d9eb26_IMSI_20200324163034418.txt
---------------
记录数 1

命令执行成功（耗时 0.094 秒）。                                                             
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME用户动态简要信息(SHOW MMEBRIEFUSERDYN) 
### 查询MME用户动态简要信息(SHOW MMEBRIEFUSERDYN) 


[](None)命令功能 

查询MME用户动态简要信息


[](None)注意事项 


该命令可通过用户的IMSI号码或MSISDN号码，查询到用户基本简要信息、PDN链接信息和用户承载信息。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERIDTYPE|ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|可根据以下用户号码类型对用户信息进行查询：IMSI：IMSI号码类型MSISDN：MSISDN号码类型
USERID|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|根据已选择的ID类型，输入对应的用户号码。如果ID类型选择IMSI，此处输入IMSI号码。如果ID类型选择MSISDN，此处输入MSISDN号码。
ITEM|查询选项|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:USERBASIC&PDNCONN&EPSBEARER。|可查询到的用户信息，包括：USERBASIC：用户基本信息PDNCONN：PDN连接信息EPSBEARER：用户承载信息默认输出以上所有信息。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RETCODE|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
RESULT|查询结果|参数可选性:任选参数；参数类型:字符型。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。






[](None)命令举例 


查询MME用户动态简要信息，查询IMSI为4602121212122用户的基本信息。 


SHOW MMEBRIEFUSERDYN:USERIDTYPE="IMSI",USERID="4602121212122",ITEM="USERBASIC"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME用户签约信息(SHOW MMEUSERSUB) 
### 查询MME用户签约信息(SHOW MMEUSERSUB) 


[](None)命令功能 


该命令用于查询MME用户签约信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERIDTYPE|ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
USERID|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|操作的用户的号码，号码类型取决于命令中的号码类型。
ITEM|查询选项|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:BASICSUB&EPSSUB。|可查询到的用户信息，包括：BASICSUB：用户基本签约信息。EPSSUB：EPS签约信息。默认输出以上所有信息。
EXFILE|是否导出到文件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|用于控制输出结果是否生成文件，默认为是。选项包括：否是






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RETCODE|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
RESULT|查询结果|参数可选性:任选参数；参数类型:字符型；参数范围为:0~640000个字符。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。






[](None)命令举例 


查询MME用户460119990023000的基本签约信息。 


SHOW MMEUSERSUB:USERIDTYPE="IMSI",USERID="460119990023000",ITEM=BASICSUB&EPSSUB;
 


` 
                                                                                                                                                                                                              
(No.1): SHOW MMEUSERSUB:USERIDTYPE="IMSI",USERID="460119990023000",ITEM=BASICSUB&EPSSUB;
-----------------NFS_MMESGSN_0----------------
结果
成功

命令结果的文件路径
53ae2b2ef64c415cba12278007f38cc5_IMSI_20200324162538417.txt
---------------
记录数 1

命令执行成功（耗时 0.094 秒）。                                                             
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### MME网投信息查询(SHOW MME COMPLAINT INFORMATION) 
### MME网投信息查询(SHOW MME COMPLAINT INFORMATION) 


[](None)命令功能 


该命令用于在满足各项安全规范的前提下，MME针对单个用户（比如,需要排查故障的某个用户）的、不包含通信内容（比如，短/彩信的内容、语音通话的内容等）的、实时历史信息的查询。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示命令执行的结果。取值含义：Success：操作结果成功。Failure：操作结果失败。
MMEINFO|MME信息|参数可选性:任选参数；参数类型:字符型。|显示移动性相关参数，PDN会话参数，如果存在多个PDN，分别显示每一个PDN信息。






[](None)命令举例 


查询MME用户460119990022000网投信息。 


SHOW MME COMPLAINT INFORMATION:IMSI="460119990022000";
 


` 
                                                      
(No.1) : SHOW MME COMPLAINT INFORMATION:IMSI="460119990022000"
-----------------NFS_MMESGSN_0----------------
MME信息                                                              
---------------------------------------------------------------------
EMM Status:      EMM-REGISTERED
CM Status:       ECM-CONNECTED
Current TAI:     460-11-6001
eNodeB:          460-11-190993
UE AMBR:         DL AMBR: 1024000 kbps    UL AMBR:1024000 kbps
RAT Restriction: no subscribed
PDN Information: 
  PDN[0]
    Slice Infomation: 
    APN: pc3.auto.local
    PGW IPv4: 192.20.53.36 
    PGW Name: pgw.auto1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org
 
---------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-28 16:47:55 耗时: 1.645 秒                                                           
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### GSN节点链路检测(GTP ECHO) 
### GSN节点链路检测(GTP ECHO) 


[](None)命令功能 


该命令用于对SGSN/MME与各个GSN节点之间的链路进行检测。 


使用该命令，SGSN/MME将向指定的GSN节点发送一条Echo消息，根据查询结果，了解该SGSN/MME与各个GSN节点之间的链路状态是否正常。 


对端的GSN节点类型包括SGSN、GGSN、MME、RNC、MSC、MBMS-GW（Multimedia Broadcast/Multicast Service Gateway，多媒体广播/组播业务网关）。 




[](None)注意事项 

该命令适用于SGSN/MME网元。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SRCIP|源地址|参数可选性:任选参数；参数类型:字符型。|本端SGSN/MME网元的控制面或用户面的IP地址，包括IPv4或者IPv6地址。SGSN网元的控制面地址可通过SHOW SIGIP GTPC命令查询获得。MME网元的控制面地址可通过SHOW MME GTPC命令查询获得。SGSN网元的用户面地址可通过SHOW SGUPIP 命令查询获得。如果不设置该参数，表示默认使用SGSN/MME网元的控制面地址。
DESIP|目的地址|参数可选性:必选参数；参数类型:字符型。|需要检测的对端GSN节点的IP地址，包括IPv4或者IPv6地址。
GTPPRO|GTP协议|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:GTPV1。|该参数用于指定本端SGSN/MME网元与对端网元的GTP协议版本。 取值含义：GTPV0：GTP版本0。GTPV1：GTP版本1。GTPV2：GTP版本2。GTP版本0和GTP版本1适用于Gn接口和Iu接口。GTP版本2适用于S11、S10、Sv、Sm和S3接口。
ITYPE|接口类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定对端网元的接口类型。 取值含义：Gn：SGSN与GPRS支持节点（GGSN或SGSN）之间的接口，设置为该接口时，“GTP协议”只能设置为“GTPV0”或“GTPV1”。Iu：SGSN与RNC之间的接口，设置为该接口时，“GTP协议”只能设置为“GTPV0”或“GTPV1”，“源地址”必须设置为用户面地址。S11：MME与SGW之间的接口，设置为该接口时，“GTP协议”只能设置为“GTPV2”，“源地址”必须是控制面的地址。S10：MME与MME之间的接口，设置为该接口时，“GTP协议”只能设置为“GTPV2”，“源地址”必须是控制面的地址。Sv：MME与MSC之间的接口，设置为该接口时，“GTP协议”只能设置为“GTPV2”，“源地址”必须是控制面的地址。Sm：MME与MBMS-GW的接口，设置为该接口时，“GTP协议”只能设置为“GTPV2”，“源地址”必须是控制面的地址。S3：MME与S4 SGSN之间的接口，设置为该接口时，“GTP协议”只能设置为“GTPV2”，“源地址”必须是控制面的地址。S11-U：MME与S11-U SGW之间的接口，设置为该接口时，“GTP协议”只能设置为“GTPV1”，“源地址”是MME GTPU地址。






[](None)命令举例 


使用GTP版本0的ECHO检测对端GSN节点（GGSN、SGSN）的链路状态，其中本端uMAC的Ip地址为192.168.0.1，对端GSN节点Ip地址为192.168.0.2。 


GTP ECHO:SRCIP="192.168.0.1",DESIP="192.168.0.2",GTPPRO="GTPV0",ITYPE="Gn"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### MME Multi-SIM 查询(SHOW MME COMMON MSISDN) 
### MME Multi-SIM 查询(SHOW MME COMMON MSISDN) 


[](None)命令功能 


该命令用于查询MME公共MSISDN号码用户相关信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
COMMONMSISDN|共有MSISDN号码|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|命令查询所携带的COMMON MSISDN。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示命令执行的结果。取值含义：Success：操作结果成功。Failure：操作结果失败。
COMMONMSISDN|共有MSISDN号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|命令查询所携带的COMMON MSISDN。
IMSI|IMSI号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
INDIVIDUALMSISDN|私有MSISDN号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|该COMMON MSISDN关联的MSISDN号码。
IMEI|IMEISV|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|该COMMON MSISDN关联的IMEISV。
USERSTATE|用户状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该COMMON MSISDN关联的用户状态。
GRAYLISTSTATE|灰名单状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该COMMON MSISDN关联的用户灰名单状态。






[](None)命令举例 


MME查询COMMON MSISDN为"08613900000001"的相关用户信息； 


SHOW MME COMMON MSISDN:COMMONMSISDN="08613900000001"; 


`

命令 (No.17): SHOW MME COMMON MSISDN:COMMONMSISDN="08613900000001";

共有MSISDN号码 
-----------------
08613900000001 
-----------------
记录数 1

INFO
IMSI号码 私有MSISDN号码 IMEISV 用户状态 灰名单状态 
----------------------------------------------------------------------------------
460010000055000 861380055000  ECM CONNECTED STATE 白名单 
----------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.157 秒）。
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询用户数据(SHOW USERDATA) 
### 查询用户数据(SHOW USERDATA) 


[](None)命令功能 


该命令用于根据用户的IMSI或者MSIDSN查询用户信息，查询结果包括用户网络类型、用户移动管理状态、实时计费标志、CSFB状态、APN状态（所使用的APN）、SGW名称和IP地址、PGW名称和IP地址。 




[](None)注意事项 


该命令适用于SGSN/MME网元，对于不同网元，命令输出结果有所不同。 


该命令只支持查询单个用户的信息，查询时，必须输入用户完整的IMSI号码或者MSIDSN号码。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERIDTYPE|ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
USERID|用户ID|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|该参数指定待查询的用户号码，如果“ID类型”为“IMSI”，则输入用户的IMSI号码，如果“ID类型”为“MSISDN”，则输入的用户的MSISDN号码。说明：输入的IMSI号或者MSISDN必须是用户完整的号码。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示命令执行的结果。取值含义：Success：操作结果成功。Failure：操作结果失败。
USERIDTYPE|ID类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示用户的号码类型。取值含义：IMSI：号码类型为IMSI。MSISDN：号码类型为MSISDN。
USERID|用户ID|参数可选性:任选参数；参数类型:字符型。|该参数指定待查询的用户号码，如果“ID类型”为“IMSI”，则输入用户的IMSI号码，如果“ID类型”为“MSISDN”，则输入的用户的MSISDN号码。说明：输入的IMSI号或者MSISDN必须是用户完整的号码。
NETTYPE|用户网络类型|参数可选性:任选参数；参数类型:字符型。|该参数指示该用户所处的网络类型。LTEUTRANGERANWLANCommon GPRS
MMSTATE|用户移动管理状态|参数可选性:任选参数；参数类型:字符型。|该参数指示该用户在网络中状态。MME网元中取值含义：12：已注册空闲态。13：已注册连接态。14：显式分离态。15：隐式分离态。SGSN网元中取值含义：1：2G注册Ready状态。2：2G注册Standy态。3：2G显式分离态。4：3G注册连接态。5：3G注册空闲态。6：3G显式分离态。7：隐式分离态。
CHARGFG|实时计费标志|参数可选性:任选参数；参数类型:字符型。|该参数指示用户签约的计费特性ID，根据此计费特性ID，可以在SGW与PGW中查找到用户使用的计费规则。
CSFBST|CSFB状态|参数可选性:任选参数；参数类型:字符型。|该参数指示用户是否联合注册到MSC。取值含义：0：未联合注册   SGs-NULL  。1：已注册在MSC  SGs-ASSOCIATED。
APNST|APN状态|参数可选性:任选参数；参数类型:字符型。|该参数指示MME/SGSN中用户使用的APN。
SGWIP|SGW IP地址|参数可选性:任选参数；参数类型:字符型。|该参数指示用户当前使用的SGW IP地址，可显示IPV4或IPV6地址。
SGWNM|SGW名称|参数可选性:任选参数；参数类型:字符型。|该参数指示用户当前使用的SGW的主机名。
PGWIP|PGW IP地址|参数可选性:任选参数；参数类型:字符型。|该参数指示用户当前使用的PGW IP地址，可显示IPV4或IPV6地址。
PGWNM|PGW名称|参数可选性:任选参数；参数类型:字符型。|该参数指示用户当前使用的PGW的主机名。
PGGSNIP|PGW/GGSN的Gn IP地址|参数可选性:任选参数；参数类型:字符型。|该参数指示用户当前使用的PGW或者GGSN Gn接口的IP地址，可显示IPV4或IPV6地址。
PGGSNNM|PGW/GGSN的名称|参数可选性:任选参数；参数类型:字符型。|该参数指示用户当前使用的PGW或者GGSN的主机名。






[](None)命令举例 


查询IMSI号为“460071000000909”的用户数据。 


SHOW USERDATA:USERIDTYPE="IMSI",USERID="460071000000909"; 


`

命令 (No.9): SHOW USERDATA:USERIDTYPE="IMSI",USERID="460071000000909";

ID类型 用户ID           用户网络类型   用户移动管理状态              实时计费标志     CSFB状态 APN状态                                         SGW IP地址         SGW名称  PGW IP地址              PGW名称 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
IMSI 460071000000909   LTE           EMM-REGISTERED; ECM-CONNECTED /Normal Billing/  NULL(0)     zte.com.apn.epc.mnc003.mcc460.3gppnetwork.org IPv4: 100.150.0.21  sgw      IPv4: 255.255.255.255   pgw 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 2.13 秒）。
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询IMSI信息(SHOW GUTI IMSI) 
### 查询IMSI信息(SHOW GUTI IMSI) 


[](None)命令功能 


该命令用于根据用户的GUTI查询用户IMSI信息。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GUTI|GUTI|参数可选性:必选参数；参数类型:字符型；参数范围为:20~20个字符。|该参数指示用户当前的GUTI(Globally Unique Temporary UE Identity)。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






[](None)命令举例 


查询64F011802115C00001FC的GUTI对应IMSI。 


SHOW GUTI IMSI:GUTI="64F011802115C00001FC";
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW GUTI IMSI:GUTI="64F011802115C00001FC";

结果 
-------
成功 
-------
记录数 1

IMSI 
-------
460119990023011 
-------
记录数 1

命令执行成功(耗时 0.058 秒).                                                            
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询备份用户信息(SHOW BAKDATAPOOL) 
### 查询备份用户信息(SHOW BAKDATAPOOL) 


[](None)命令功能 


该命令用于备份MME根据UE的IMSI，查询备份的用户动态位置信息。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
TA|跟踪区|参数可选性:任选参数；参数类型:字符型。|EPC网络中区域管理的最小单位。






[](None)命令举例 


备份MME上查询备份的460119990020000的动态位置信息。 


SHOW BAKDATAPOOL:IMSI="460119990020000";
 


` 
                                                                                                                                                                                                              
命令 (No.1): SHOW BAKDATAPOOL:IMSI="460119990020000";

结果 
-------
成功 
-------
记录数 1

跟踪区
----------------
460-11-8801 
460-11-8803 
460-11-8802 
----------------
记录数 3

命令执行成功（耗时 0.158 秒）。                                                            
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 清空备份数据(CLEAR BAKDATA) 
### 清空备份数据(CLEAR BAKDATA) 


[](None)命令功能 


该命令用于清除本MME保存的供MME容灾使用的所有备份信息。当修改了POOL内MME间的容灾备份关系，原有的备份数据不再有效时，可使用该命令清除原有的备份数据。 




[](None)注意事项 


该命令只适用于MME。 




[](None)命令举例 


清空备份数据。 


CLEAR BAKDATA; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 同步备份数据(SYN BAKDATA) 
### 同步备份数据(SYN BAKDATA) 


[](None)命令功能 


该命令用于将本MME的所有用户需要容灾备份的动态数据，立即同步备份到对应的备份节点，以供MME容灾使用。当修改了POOL内MME间的容灾备份关系，需要将数据快速同步到新的备份节点时，可使用该命令。 




[](None)注意事项 


该命令只适用于MME。 




[](None)命令举例 


同步备份数据。 


SYN BAKDATA; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 取消备份数据同步(CANCEL BAKDATA SYN) 
### 取消备份数据同步(CANCEL BAKDATA SYN) 


[](None)命令功能 


该命令用于终止正在进行的容灾备份数据同步操作。当发现正在进行的同步操作不再需要时，可使用该命令立即终止。 




[](None)注意事项 


该命令只适用于MME。 




[](None)命令举例 


取消备份数据同步。 


CANCEL BAKDATA SYN; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 用户卸载到指定MME(UNLOAD MME USER) 
### 用户卸载到指定MME(UNLOAD MME USER) 


[](None)命令功能 


该命令用于将用户卸载到指定MME。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
GUMMEI|GUMMEI|参数可选性:必选参数；参数类型:复合参数|GUMMEI（Globally Unique MME Identifier，全球唯一MME标识）由MCC（Mobile Country Code，移动国家码）、MNC（Mobile Network Code，移动网码）以及MMEI（MME Identifier，MME标识）组成。 MMEI由MMEGI（MME Group ID，MME组标识）和MMEC（MME Code，MME编码）组成，MMEGI长度为16比特，MMEC长度为8比特。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
MMEGID|MME组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|MME所在池组的标识，一般以32768开始。
MMEC|MME编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|用于在网络中标识MME的编号。






[](None)命令举例 


指定本局的一个用户卸载到另外一个MME。 


UNLOAD MME USER:IMSI="460119990020000",GUMMEI="460"-"02"-1-1; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 用户卸载到指定SGSN(UNLOAD SGSN USER) 
### 用户卸载到指定SGSN(UNLOAD SGSN USER) 


[](None)命令功能 


该命令用于将用户卸载到指定SGSN。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|IMSI由MCC、MNC、MSIN三部分组成。MCC：移动国家码，固定为3位十进制数字，用于唯一标识一个国家。MNC：移动网号，由2位或者3位十进制数字组成，用于标识移动用户的归属PLMN。MSIN：移动台标识号码，MSIN在PLMN内标识一个移动用户。不同的国家，采用的MNC位长不一定相同，可以是2位或者3位，但同一国家内，MNC的长度通常只有一种，或者2位，或者3位。
NRI|目标SGSN的NRI|参数可选性:必选参数；参数类型:整数；参数范围为:0~1023。|该参数表示目标SGSN的NRI。NRI（Network Resource Identifier，网络资源标识）用来识别不同的SGSN。NRI使用了PTMSI的一些固定的bit位。用户发起附着/路由区更新请求或基站发起切换请求/RIM消息，SGSN收到请求后，根据逻辑名称DNS或本地解析得到目标局SGSN的地址，根据选择策略确定一个SGSN地址，最终SGSN通过选定的SGSN地址与目标局SGSN进行业务交互。本地解析目标局SGSN地址的逻辑名称共有三种方式，RNC，RAI，NRI；三种方式的逻辑名称组成如下：RNC标识具有固定格式“RNCIDxxxx.MNCyyy.MCCzzz.GPRS”RAI标识具有固定格式“RACxxxx.LACyyyy.MNCzzz.MCCwww.GPRS”NRI标识具有固定格式“nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs。
RAI|目标SGSN的非广播路由区|参数可选性:必选参数；参数类型:复合参数|目标SGSN的非广播路由区是指，当前路由区不用广播给POOL内其他SGSN，只有目标SGSN知道。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
LAC|位置区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|LAC：位置区域码（Location Area Code），位置区编码用于识别网络中的位置区。根据网络规划进行编码。用于UMTS网络中，在相同MCC、MNC唯一标识一个LA（Location Area，位置区）的编号。LA是划分网络范围的基本属性。区域编码(Zone Code)被用来定义用户是否允许漫游的位置区域，用户可以签约一个或多个区域编码。位置区标识LAI是指UE在不更新VLR的情况下可以自由移动的区域。位置区标识LAI由MCC（移动国家码）+MNC（移动网号）+LAC（位置区域码，Location Area Code）组成。
RAC|路由区码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~2个字符。|路由区编码用于识别网络中的路由区。应该根据网络规划进行编码。RAC（Routing Area Code， 路由区码）用于UMTS网络中，在相同MCC、MNC和LAC下唯一标识一个RA（Routing Area，路由区）的编号。RA是移动用户位置的基本属性，一个LA下可以包含多个RA，一个RA只能属于一个LA。路由区RA是位置区的子集，GPRS网络是按路由区来进行用户的位置管理，用户在RA内移动不需要发起路由更新，跨RA移动时，会发起路由更新。一个位置区可以对应一个路由区，也可进一步划分为几个路由区。每个RA由一到多个小区组成，RA之间没有重叠区域。路由区标识RAI（Routing Area Identity )由LAI和RAC（Routing Area Code）组成，运营商对于RAC的编码方式有明确的规定，一旦分配，在运营中较少改动。






[](None)命令举例 


用户卸载到指定SGSN，IMSI为"460119990020000",目标SGSN的NRI为132，目标SGSN的非广播路由区中移动国家码为320，移动网号为30，位置区域码(HEX)为ADCF，路由区码(HEX)为AA。 


UNLOAD SGSN USER:IMSI="460119990020000",NRI=132,RAI="320"-"30"-"ADCF"-"AA""; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MTC用户动态信息(SHOW MTC USER DYNAMIC INFO) 
### 查询MTC用户动态信息(SHOW MTC USER DYNAMIC INFO) 


[](None)命令功能 


该命令用于查询MTC终端用户的动态信息。 


该命令可通过用户的IMSI号码，查询MTC终端用户的活动时长、空闲时长和切换间隔。 


可查询指定IMSI的MTC终端用户信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示命令执行的结果。取值含义：Success：查询成功。No Record：无记录。
HSSACTTIME|MTC终端活动周期(s)|参数可选性:任选参数；参数类型:整数。|该参数指示MTC终端处于活动态的周期。
HSSIDLETIME|MTC终端空闲周期(s)|参数可选性:任选参数；参数类型:整数。|该参数指示MTC终端处于空闲态的周期。
HOINTERVAL|MTC终端跨eNodeB之间切换的时间间隔(s)|参数可选性:任选参数；参数类型:整数。|该参数指示MTC终端在跨eNodeB之间切换的时间间隔。






[](None)命令举例 


SHOW MTC USER DYNAMIC INFO:IMSI="111111111111111";
 


` 
                                                                                                                                                                                                              
2017-01-14 14:26:40 命令 (No.12): SHOW MTC USER DYNAMIC INFO:IMSI="111111111111111";

MTC终端活动周期(s)   MTC终端空闲周期(s)   MTC终端跨eNodeB之间切换的时间间隔(s)
------------------------------------------------------------------------------
1                    1                    1
------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.038 秒）。                                                        
` 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 同步用户信息(CDB SYN) 
### 同步用户信息(CDB SYN) 


[](None)命令功能 

同步用户信息


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|用户的IMSI号码（非IMSI号段）。IMSI（International Mobile Subscriber Identity，国际移动用户标识）是区别移动用户的标志，可用于区别移动用户的有效信息。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






[](None)命令举例 


同步用户信息，IMSI为"460119990020000" 


CDB SYN:IMSI="460119990020000"; 








父主题： [用户动态管理](../../zh-CN/tree/N_130840103.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## DNS相关 
## DNS相关 


[](None)背景知识 

            
            DNS动态管理用于对DNS Cache和DNS查询的人工控制。
        


[](None)功能描述 

            
            DNS动态管理包括DNS查询、指定服务器DNS查询、查询DNS Cache中指定域名、清除DNS Cache中指定域名和清空DNS Cache所有内容。
        


[](None)相关主题 



 

DNS查询(DNS LOOKUP)
 

 

指定地址DNS查询(DNS SERVER LOOKUP)
 

 

查询DNS Cache中指定域名(SHOW DNSCACHE)
 

 

清除DNS Cache中指定域名(DEL DNSCACHE)
 

 

清空DNS Cache所有内容(CLEAR DNSCACHE)
 

 

查询DNS TCP链路状态(SHOW TCPLINK STATE)
 

 

查询DNS Cache使用率(SHOW DNSCACHE USAGE)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### DNS查询(DNS LOOKUP) 
### DNS查询(DNS LOOKUP) 


[](None)命令功能 


查询特定域名的资源记录，可根据以下信息进行查询。 



 
域名
 

 
查询方式
 

 
优先查询DNS CACHE
 

 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|此参数为查询的输入条件，表示对用户的IMSI号码进行处理的USMP的实例号，该IMSI号码为携带需要通过DNS进行解析的域名的用户号码。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
TIMEOUT|超时时长（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:2~20。默认值:15。|该参数用于设定SGSN/MME网元等待DNS服务器返回解析域名结果的时长，如果超过此时长，DNS还没有返回结果，表示查询失败。
SERVERGROUP|DNS查询方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定对域名进行解析的查询方式。 取值含义：GPRS查询：对域名进行A或AAAA或ANY的DNS查询。DNS查询时选择的DNS服务器为GPRS Profile中的服务器。EPC查询：对域名进行从S-NAPTR查询开始的一系列DNS查询。DNS查询时选择的DNS服务器为LTE Profile中的服务器。
DOMAINNAME|域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|SGSN/MME需要通过DNS进行解析的域名，以便根据域名获取对应的IP地址。
PRIOR|优先查询DNS CACHE|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:DNS_CACHE_PRIOR_YES。|该参数用于是否查询DNS CACHE中的结果。 DNS CACHE是SGSN/MME网元本地的一个数据表，用于保存DNS的历史解析结果，SGSN/MME可以先在DNS CACHE中查询需要解析的域名，如果查询不到结果，再将域名发送到DNS进行解析。 取值含义：“DNS_CACHE_PRIOR_YES”：优先查询DNS CACHE中保存的查询结果，如果查询不到，再到DNS服务器进行查询。“DNS_CACHE_PRIOR_NO”：不查询DNS CACHE中的结果，直接查询DNS服务器。
IPTYPE|IP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:V4V6。|该参数用于设置IP地址查询类型，有如下三种类型：V4V6: ANY查询V4: A查询V6: AAAA查询
SERVICE|服务类别|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下几种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-pgw：目标局类型为PGWx-3gpp-ggsn：目标局类型为GGSNx-3gpp-amf：目标局类型为AMF
PROTOCOL|协议类型|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置被查询网元所支持的接口类型，目前支持如下类型：x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-s11: S11接口x-s3: S3接口x-gn: Gn接口x-gp: Gp接口x-s10: S10接口，MME与MME之间的接口x-sv: Sv接口，MME与MSC之间的接口，用于SRVCC切换x-s11+nc-nr: 网络能力nr的S11接口x-s5-gtp+nc-nr：支持GTP协议（网络能力nr）的S5接口。x-s5-pmip+nc-nr：支持PMIP协议（网络能力nr）的S5接口。x-s8-gtp+nc-nr：支持GTP协议（网络能力nr）的S8接口。x-s8-pmip+nc-nr：支持PMIP协议（网络能力nr）的S8接口。x-n26：N26接口。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|






[](None)命令举例 


该示例命令在3号SC实例上采用GPRS查询方式，域名“zte.com.mnc001.mcc460.gpr”是否能够解析成功。 


DNS LOOKUP:SC=3,SERVERGROUP="GPRS",DOMAINNAME="zte.com.mnc001.mcc460.gprs"; 


`

命令 (No.9): DNS LOOKUP:SC=3,SERVERGROUP="GPRS",DOMAINNAME="zte.com.mnc001.mcc460.gprs";

域名 
-------
zte.com.mnc001.mcc460.gprs 
-------
记录数 1

DNS查询方式 
--------------
GPRS查询 
--------------
记录数 1

查询结果 
-----------
SUCCEED 
-----------
记录数 1

返回地址个数 
---------------
1 
---------------
记录数 1

地址 
-------
IPv4: 168.6.22.36  
-------
记录数 1

命令执行成功（耗时 6.282 秒）。
` 








父主题： [DNS相关](../../zh-CN/tree/N_130840166.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 指定地址DNS查询(DNS SERVER LOOKUP) 
### 指定地址DNS查询(DNS SERVER LOOKUP) 


[](None)命令功能 


查询指定的DNS服务器的资源记录，可根据以下信息进行服务器指定及进行查询。 



 
域名
 

 
查询方式
 

 
优先查询DNS CACHE
 

 
指定DNS服务器地址
 

 
DNS服务器地址
 

 
DNS客户端地址
 

 
VRFID
 

 




[](None)注意事项 


当指定的DNS服务器非本地配置的服务器时，不支持TCP查询模式。UDP优先模式可能影响查询结果，具体表现为：对于有截断响应的场景不再进行查询。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|此参数为查询的输入条件，表示对用户的IMSI号码进行处理的USMP的CMP实例号，该IMSI号码为携带需要通过DNS进行解析的域名的用户号码。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
TIMEOUT|超时时长（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:2~20。默认值:15。|该参数用于设定SGSN/MME网元等待DNS服务器返回解析域名结果的时长，如果超过此时长，DNS还没有返回结果，表示查询失败。
SERVERGROUP|DNS查询方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定对域名进行解析的查询方式。 取值含义：GPRS查询：对域名进行A或AAAA或ANY的DNS查询。DNS查询时选择的DNS服务器为GPRS Profile中的服务器。EPC查询：对域名进行从S-NAPTR查询开始的一系列DNS查询。DNS查询时选择的DNS服务器为LTE Profile中的服务器。
DOMAINNAME|域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|SGSN/MME需要通过DNS进行解析的域名，以便根据域名获取对应的IP地址。
PRIOR|优先查询DNS CACHE|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:DNS_CACHE_PRIOR_YES。|该参数用于是否查询DNS CACHE中的结果。 DNS CACHE是SGSN/MME网元本地的一个数据表，用于保存DNS的历史解析结果，SGSN/MME可以先在DNS CACHE中查询需要解析的域名，如果查询不到结果，再将域名发送到DNS进行解析。 取值含义：“DNS_CACHE_PRIOR_YES”：优先查询DNS CACHE中保存的查询结果，如果查询不到，再到DNS服务器进行查询。“DNS_CACHE_PRIOR_NO”：不查询DNS CACHE中的结果，直接查询DNS服务器。
SPECIFYDNS|指定DNS服务器地址|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|此参数为查询的输入条件，表示是否到指定的DNS服务器查询。
DNSSERVERADDR|DNS服务器地址|参数可选性:任选参数；参数类型:地址|此参数为查询的输入条件，表示指定查询的DNS服务器地址。 可以是IPV4地址或IPV6地址。 必须和DNS客户端地址类型保持一致。
DNSCLIENTADDR|DNS客户端地址|参数可选性:任选参数；参数类型:地址|此参数为查询的输入条件，表示指定查询的DNS客户端地址。 可以是IPV4地址或IPV6地址。必须和DNS服务器地址类型保持一致。
VRFID|VRFID|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|此参数为查询的输入条件，表示DNS服务器所在的网络VRFID。
IPTYPE|IP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:V4V6。|该参数用于设置IP地址查询类型，有如下三种类型：V4V6: ANY查询V4: A查询V6: AAAA查询
SERVICE|服务类别|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下四种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-pgw：目标局类型为PGWx-3gpp-ggsn：目标局类型为GGSNx-3gpp-amf：目标局类型为AMF
PROTOCOL|协议类型|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置被查询网元所支持的接口类型，目前支持如下类型：x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-s11: S11接口x-s3: S3接口x-gn: Gn接口x-gp: Gp接口x-s10: S10接口，MME与MME之间的接口x-sv: Sv接口，MME与MSC之间的接口，用于SRVCC切换x-s11+nc-nr: 网络能力nr的S11接口x-s5-gtp+nc-nr：支持GTP协议（网络能力nr）的S5接口。x-s5-pmip+nc-nr：支持PMIP协议（网络能力nr）的S5接口。x-s8-gtp+nc-nr：支持GTP协议（网络能力nr）的S8接口。x-s8-pmip+nc-nr：支持PMIP协议（网络能力nr）的S8接口。x-n26：N26接口。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|






[](None)命令举例 


查询3号SC实例且域名为“zte.com.cn”的DNS服务器信息。 


DNS SERVER LOOKUP:SC=3,SERVERGROUP="EPC",DOMAINNAME="zte.com.cn",SPECIFYDNS="YES",DNSSERVERADDR="1.3.2.4",DNSCLIENTADDR="1.3.2.5",VRFID=0;  


`

命令 (No.1): DNS SERVER LOOKUP:SC=3,SERVERGROUP="EPC",DOMAINNAME="zte.com.cn",SPECIFYDNS="YES",DNSSERVERADDR="1.3.2.4",DNSCLIENTADDR="1.3.2.5",VRFID=0;

域名 
-------
zte.com.cn 
-------
记录数 1

DNS查询方式 
--------------
EPC查询 
--------------
记录数 1

查询结果 
-----------
FAIL 
-----------
记录数 1

查询结果备注 
---------------
Timeout! 
---------------
记录数 1

命令执行成功（耗时 15.054 秒）。

` 








父主题： [DNS相关](../../zh-CN/tree/N_130840166.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS Cache中指定域名(SHOW DNSCACHE) 
### 查询DNS Cache中指定域名(SHOW DNSCACHE) 


[](None)命令功能 

该命令用于查询DNS Cache中指定域名，当需要根据域名从Cache中查询对应的资源记录时，使用该命令。查询DNS Cache的命令执行成功后，DNS根据查询的域名和查询类型从Cache中查询出对应的资源记录。


[](None)注意事项 


网元内各个模块独立维护本模块上的DNS cache，查询时需要指定具体的模块。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
APNNAME|域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~254个字符。|表示需要输入的APN（Access Point Name，接入点名称），是根据用户请求的APN和用户签约的APN，基于23.060协议的规则选择得到的APN作为DNS查询条件。
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65534。|单板逻辑地址中的CMP实例号，实例号必须是已存在的，可以使用 SHOW SCINFO 命令查询到。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SERVER|DNS服务器地址|参数可选性:任选参数；参数类型:字符型。|响应该资源记录的DNS服务器地址。
IPADDR1|IP地址|参数可选性:任选参数；参数类型:字符型。|IP地址
SERVER2|DNS服务器地址|参数可选性:任选参数；参数类型:字符型。|响应该资源记录的DNS服务器地址
PRIORITY|优先级|参数可选性:任选参数；参数类型:整数。|SRV记录中的优先级字段,决定SRV记录中主机名对应的权重值，用来作为对SRV记录进行优选时的依据
WEIGHT|权重|参数可选性:任选参数；参数类型:整数。|SRV记录中的权重字段。当SRV记录中的优先级字段相同时，根据协议要求，依据权重值对优先级字段相同的SRV记录进行优选
PORT|端口|参数可选性:任选参数；参数类型:整数。|SRV记录中的端口号，SRV记录中的主机名对应的主机提供的服务的端口号
TARGET|目标|参数可选性:任选参数；参数类型:字符型；参数范围为:0~512个字符。|SRV记录中的主机名
SERVER3|DNS服务器地址|参数可选性:任选参数；参数类型:字符型。|响应该资源记录的DNS服务器地址。
ORDER|次序|参数可选性:任选参数；参数类型:整数。|NAPTR记录中的次序字段，和NAPTR记录中的优选字段一起，作为对应NAPTR记录优选的依据。NAPTR相关的RFC协议有3401,3402,3403,3404,3405，其中关于NAPTR记录中的字段的描述请求参考RFC3403中描述。
PREFERENCE|优选|参数可选性:任选参数；参数类型:整数。|NAPTR记录中的优选字段和NAPTR记录中的次序字段一起，作为对应NAPTR记录优选的依据。NAPTR相关的RFC协议有3401,3402,3403,3404,3405，其中关于NAPTR记录中的字段的描述请求参考RFC3403中描述。
FLAG|标志|参数可选性:任选参数；参数类型:字符型。|NAPTR记录中的标志字段，控制标志，根据协议，该标志控制NAPTR记录的重写机制。NAPTR相关的RFC协议有3401,3402,3403,3404,3405，其中关于NAPTR记录中的字段的描述请求参考RFC3403中描述。
SERVICE|服务|参数可选性:任选参数；参数类型:字符型。|NAPTR记录中的服务字段，NAPTR相关的RFC协议有3401,3402,3403,3404,3405，其中关于NAPTR记录中的字段的描述请求参考RFC3403中描述。
REGEXP|正则表达式|参数可选性:任选参数；参数类型:字符型。|NAPTR记录中的正则表达式，NAPTR相关的RFC协议有3401,3402,3403,3404,3405，其中关于NAPTR记录中的字段的描述请求参考RFC3403中描述。
REPLACE|替换|参数可选性:任选参数；参数类型:字符型。|NAPTR记录中的替换字段，NAPTR相关的RFC协议有3401,3402,3403,3404,3405，其中关于NAPTR记录中的字段的描述请求参考RFC3403中描述。
RRTYPE|资源记录类型|参数可选性:任选参数；参数类型:字符型。|资源记录的类型，对应的字段描述参考RFC1035。
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。






[](None)命令举例 


查询DNS Cache中指定域名，域名为iuzte.com0029.mnc003.mcc460.gprs，SC实例号为10。 


SHOW DNSCACHE:APNNAME="iuzte.com0029.mnc003.mcc460.gprs",SC=10; 


`

 命令 (No.1): SHOW DNSCACHE:APNNAME="iuzte.com0029.mnc003.mcc460.gprs",SC=10;

查询结果       
---------------
域名不存在    
---------------
记录数 1

命令执行成功（耗时 0.092 秒）。
` 








父主题： [DNS相关](../../zh-CN/tree/N_130840166.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 清除DNS Cache中指定域名(DEL DNSCACHE) 
### 清除DNS Cache中指定域名(DEL DNSCACHE) 


[](None)命令功能 

该命令用于清除DNS Cache中指定域名和查询类型对应的资源记录，当需要根据域名和类型从Cache中清除对应的资源记录时，使用该命令。指定域名清除DNS Cache的命令执行成功后，[SHOW DNSCACHE](1405264.html)命令查看。


[](None)注意事项 


网元内各个CMP实例号独立维护本CMP实例号上的DNS Cache，清除时需要指定具体的CMP实例号。清除操作成功后，该域名对应的同类型的资源记录在DNS cache中被清除。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
APNNAME|域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~254个字符。|要查询的域名
MODULE|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65534。|单板逻辑地址中的CMP实例号，实例号必须是已存在的，可以使用SHOW SCINFO 命令查询到。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)命令举例 


清除DNS Cache中指定域名，域名为iuzte.com0029.mnc003.mcc460.gprs，SC实例号为10。 


DEL DNSCACHE:APNNAME="iuzte.com0029.mnc003.mcc460.gprs",SC=10; 








父主题： [DNS相关](../../zh-CN/tree/N_130840166.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 清空DNS Cache所有内容(CLEAR DNSCACHE) 
### 清空DNS Cache所有内容(CLEAR DNSCACHE) 


[](None)命令功能 

该命令用于清除DNS Cache中所有的资源记录，当需要从Cache中清除所有的资源记录时，使用该命令。清除DNS Cache所有资源记录的命令执行成功后，DNS Cache会被清空，使用[SHOW DNSCACHE](1405264.html)查询资源记录是否被清空。


[](None)注意事项 


网元内各个CMP实例号独立维护本CMP实例号上的DNS cache，清除时需要指定具体的CMP实例号。清除所有DNS cache命令完成后，该CMP实例号上的DNS  cache中所有的资源记录会被清空。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65534。|单板逻辑地址中的CMP实例号，CMP实例号必须是已存在的，可以使用SHOW SCINFO 命令查询到。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)命令举例 


清空DNS Cache所有内容。 


CLEAR DNSCACHE:SC=10; 








父主题： [DNS相关](../../zh-CN/tree/N_130840166.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS TCP链路状态(SHOW TCPLINK STATE) 
### 查询DNS TCP链路状态(SHOW TCPLINK STATE) 


[](None)命令功能 


该命令用于查询和DNS服务器通信的TCP链路。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SERVERID|DNS服务器编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|DNS服务器的内部编号，在DNS服务器配置命令中配置，通过ADD DNS SERVER配置。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。
NUM|链路个数|参数可选性:任选参数；参数类型:整数。|该DNS服务器下一共配置的TCP链路条数。
SERVERID|DNS服务器编号|参数可选性:任选参数；参数类型:整数。|DNS服务器的内部编号，在DNS服务器配置命令中配置，通过ADD DNS SERVER配置。
LINK|链路号|参数可选性:任选参数；参数类型:整数。|自定的TCP 链路的内部编号，便于内部索引，关联或查询。
SERVERADDR|DNS服务器IP地址|参数可选性:任选参数；参数类型:字符型。|DNS服务器地址，可以是IPV4地址也可以是IPV6地址。
CLIENTADDR|DNS客户端IP地址|参数可选性:任选参数；参数类型:字符型。|DNS客户端地址，和本配置中DNS服务器IP地址同类型,即DNS客户端IP地址和DNS服务器IP地址都是IPV4或都是IPV6地址。
PORT|源端口号|参数可选性:任选参数；参数类型:整数。|源端口号。
STATE|链路状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TCP链路状态，即是否已经激活成功。
SC|CMP实例号|参数可选性:任选参数；参数类型:整数。|指定管理链路的MP实例号，由系统自动分配，MP实例的类型必须为SMP。






[](None)命令举例 


查询服务1下的TCP 链路信息。 


命令 (No.1): SHOW TCPLINK STATE:SERVERID=1; 


`

2017-01-16 13:12:07 命令 (No.1): SHOW TCPLINK STATE:SERVERID=1

操作结果 
-----------
成功 
-----------
记录数 1

链路个数 
-----------
1 
-----------
记录数 1

信息
DNS服务器编号 链路号 DNS服务器IP地址 DNS客户端IP地址 源端口号 链路状态 CMP实例号 
---------------------------------------------------------------------------------
1             2      192.20.53.222   192.20.134.2    51026    激活     2               
---------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.546 秒）。
` 








父主题： [DNS相关](../../zh-CN/tree/N_130840166.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS Cache使用率(SHOW DNSCACHE USAGE) 
### 查询DNS Cache使用率(SHOW DNSCACHE USAGE) 


[](None)命令功能 

查询DNS Cache使用率


[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65534。|
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:整数。|单板逻辑地址中的CMP实例号，实例号必须是已存在的，可以使用 SHOW SCINFO 命令查询到。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
RESULT|操作结果|参数可选性:任选参数；参数类型:整数。|用于描述该命令的数据查询结果，结果包含的数据是根据新增的配置项所决定，具体以网管界面返回显示为准。






[](None)命令举例 


查询模块1的DNS Cache使用率 


SHOW DNSCACHE USAGE:SC=1; 


`

命令 (No.1): SHOW DNSCACHE USAGE:SC=1;

CMP实例号	操作结果
-------------------
1		    0
-------------------
记录数 1

命令执行成功（耗时 0.06 秒）。

` 








父主题： [DNS相关](../../zh-CN/tree/N_130840166.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Diameter管理 
## Diameter管理 


[](None)背景知识 

            
            Diameter管理用于人工查询和控制当前的Diameter的链路的状态。
        


[](None)功能描述 

            
            该功能包括查询Diameter链路状态、闭塞/解闭塞Diameter的链路。
        


[](None)相关主题 



 

Diameter连接状态开关(CHG DIMCONNSTATUS)
 

 

查询Diameter路由组(SHOW DIMROUTE INFO)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter连接状态开关(CHG DIMCONNSTATUS) 
### Diameter连接状态开关(CHG DIMCONNSTATUS) 


[](None)命令功能 

该命令用于手动开启或者关闭Diameter 链路。当Diameter链路建立成功之后，链路处于开启状态，如果不需要使用某条Diameter链路，可使用该命令手动闭塞Diameter链路。


[](None)注意事项 



 
执行该命令前，需要保证SCTP连接标识所标识的Diameter连接已存在，且已关联到某条Diameter路由中。Diameter路由、链路组及连接配置的查询命令分别参见 SHOW DIAMROUTE、SHOW DIAMLINKGROUP和SHOW DIAMCONN。
 

 
成功闭塞某条Diameter链路后，需重新开启该Diameter链路，该Diameter链路才会再次和对端通信。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|SCTP连接标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4112。|该参数表示待执行关闭或开启的Diameter链路标识。查询SCTP Link ID的命令参见SHOW SCTP。
TYPE|操作类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示本次操作的类型。该参数的类型为枚举型变量，取值如下：开启关闭






[](None)命令举例 


闭塞连接标识为1的Diameter链路。 


CHG DIMCONNSTATUS:ID=1,TYPE="close"; 








父主题： [Diameter管理](../../zh-CN/tree/N_13084022.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询Diameter路由组(SHOW DIMROUTE INFO) 
### 查询Diameter路由组(SHOW DIMROUTE INFO) 


[](None)命令功能 


该命令用于查询Diameter路由组及其所关联的Diameter路由、Diameter链路组、Diameter连接的状态等信息。 


其中Diameter路由组信息包括路由组的状态及路由属性；Diameter路由信息包括路由状态、路由协商本端能力及路由属性；Diameter链路组信息包括链路组状态及分担方式；Diameter链路信息包括链路状态信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数表示待查询的Diameter路由组标识。查询Diameter Route Group ID的命令参见SHOW DIAMROUTEGROUP。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示本次操作的结果。操作结果为枚举类型，取值如下：查询成功查询失败连接不存在（NOTEXIST）
DRGID|Diameter路由组ID|参数可选性:任选参数；参数类型:整数。|该参数表示待查询的Diameter路由组标识。查询Diameter Route Group ID的命令参见SHOW DIAMROUTEGROUP。
DRGS|Diameter路由组状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询到的Diameter路由组状态信息。Diameter路由组状态为枚举类型，取值如下：可用不可用
RP|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询到的该Diameter路由组的路由属性。路由属性其实就是分担方式，为枚举类型，取值如下：主备负荷分担
DRID|Diameter路由编号|参数可选性:任选参数；参数类型:整数。|该参数表示查询到的该Diameter路由组所关联的Diameter路由的编号。查询Diameter Route ID的命令参见SHOW DIAMROUTE。
DRS|Diameter路由状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询到的该Diameter路由组所关联的Diameter路由的状态信息。iameter路由状态为枚举类型，取值如下：可用（VALID）不可用（INVALID）
CN|路由协商本端能力|参数可选性:任选参数；参数类型:字符型。|该参数意思为路由协商支持的接口能力，取值如下：S6a\S6d：本网元支持和HSS连接。S13\S13'：本网元支持和EIR连接。Slg：本网元支持和GLMC连接。Slg：本网元支持和DRA连接。
LGID|链路组编号|参数可选性:任选参数；参数类型:整数。|该参数表示查询到的该Diameter路由组下所关联的Diameter链路组的编号。查询Link Group ID的命令参见SHOW DIAMLINKGROUP。
LGS|链路组状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询到的该Diameter路由组所关联的Diameter链路组的状态信息。Diameter链路组状态为枚举类型，取值如下：可用不可用
PM|分担方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询到的该Diameter路由组所关联的Diameter链路组的分担方式信息。分担方式为枚举类型，取值如下：主备负荷分担
DSID|Diameter偶联编号|参数可选性:任选参数；参数类型:整数。|该参数表示查询到的该Diameter路由组所关联的Diameter链路的编号。查询 SCTP Link ID的命令参见SHOW DIAMCONN。
DSS|Diameter偶联状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询到的该Diameter路由组所关联的Diameter链路的状态信息。Diameter链路状态为枚举类型，取值如下：可用不可用






[](None)命令举例 


查询Diameter路由组ID为1的路由组信息，包括该路由组及其所关联的Diameter路由、Diameter链路组、Diameter连接的状态等信息。 


SHOW DIMROUTE INFO:ID=1; 


`

命令 (No.1): SHOW DIMROUTE INFO:ID=1;

Diameter路由组信息
Diameter路由组ID   Diameter路由组状态   路由属性
------------------------------------------------
1                  可用                 主备
------------------------------------------------
记录数 1

Diameter路由信息
Diameter路由编号   Diameter路由状态   路由协商本端能力             路由属性
---------------------------------------------------------------------------
1                  可用               S6a\S6d&S13\S13'             主备
---------------------------------------------------------------------------
记录数 1

链路组信息
Diameter路由编号   链路组编号   链路组状态   分担方式
-----------------------------------------------------
1                  1            可用         负荷分担
-----------------------------------------------------
记录数 1

Diameter偶联信息
链路组编号   Diameter偶联编号   Diameter偶联状态
------------------------------------------------
1            1                  可用
------------------------------------------------
记录数 1

命令执行成功（耗时 0.078 秒）。
 ` 








父主题： [Diameter管理](../../zh-CN/tree/N_13084022.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGs管理 
## SGs管理 


[](None)背景知识 

            
            SGs管理用于人工查询和控制当前的SGs的链路的状态以及VLR局向状态、VLR POOL信息和VLR Name信息。
        


[](None)功能描述 

            
            该功能包括查询SGs链路状态、闭塞/解闭塞SGs的链路、查询VLR局向状态、VLR POOL信息和VLR Name信息。
        


[](None)相关主题 



 

查询SGs连接状态(SHOW SGSCONNSTATUS)
 

 

查询SGs路由状态(SHOW SGSROUTESTATUS)
 

 

查询SGs路由组状态(SHOW SGSROUTEGRPSTATUS)
 

 

查询VLR局向状态(SHOW VLROFFICESTATUS)
 

 

查询VLR POOL信息(SHOW VLRPOOLINFO)
 

 

查询VLR名称(SHOW VLRNAME)
 

 

VLR局向手动恢复(RESTORE VLR)
 

 

取消手动恢复VLR局向(CANCEL RESTORE VLR)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGs连接状态(SHOW SGSCONNSTATUS) 
### 查询SGs连接状态(SHOW SGSCONNSTATUS) 


[](None)命令功能 

该命令用于查询SGs连接状态。只有连接状态为开启才能正常进行SGs口业务。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NO|SGs连接编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2047。|该参数用于标识一条SGs连接，要求全局唯一。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NO|SGs连接编号|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条SGs连接，要求全局唯一。
STATUS|连接状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs连接状态取值为枚举类型：关闭状态（CLOSED）开启状态（OPEN）
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs连接查询结果。查询结果为枚举类型：查询成功（SUCCESS）查询失败（FAIL）连接不存在（NOTEXIST）
REASON|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs连接查询结果。查询结果为枚举类型：连接不存在（NOTEXIST）






[](None)命令举例 


查询SGS连接编号为118的SGs连接状态。 


SHOW SGSCONNSTATUS:NO=118; 


`

命令 (No.1): SHOW SGSCONNSTATUS:NO=118;

SGs连接编号   连接状态   查询结果
---------------------------------
118           开启状态   查询成功
---------------------------------
记录数 1

命令执行成功（耗时 0.041 秒）。
 ` 








父主题： [SGs管理](../../zh-CN/tree/N_1263_sgs_management_combo_gngp.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGs路由状态(SHOW SGSROUTESTATUS) 
### 查询SGs路由状态(SHOW SGSROUTESTATUS) 


[](None)命令功能 

该命令用于查询SGs路由状态。只有连接状态为开启才能正常进行SGs口业务。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NO|SGs路由ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由，要求全局唯一。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NO|SGs路由ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由，要求全局唯一。
STATUS|路由状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs路由状态。取值为枚举类型：关闭状态（CLOSED）开启状态（OPEN）
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs路由查询结果。查询结果为枚举类型：查询成功（SUCCESS）查询失败（FAIL）连接不存在（NOTEXIST）
REASON|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs路由查询结果。查询结果为枚举类型：连接不存在（NOTEXIST）






[](None)命令举例 


查询SGs路由ID为1的SGs路由状态。 


SHOW SGSROUTESTATUS:SGSRTID=1; 


`

命令 (No.1): SHOW SGSROUTESTATUS:SGSRTID=1;

SGs路由ID   路由状态   查询结果
-------------------------------
1           开启状态   查询成功
-------------------------------
记录数 1

命令执行成功（耗时 0.031 秒）。
 ` 








父主题： [SGs管理](../../zh-CN/tree/N_1263_sgs_management_combo_gngp.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGs路由组状态(SHOW SGSROUTEGRPSTATUS) 
### 查询SGs路由组状态(SHOW SGSROUTEGRPSTATUS) 


[](None)命令功能 

该命令用于查询SGs路由组状态。只有连接状态为开启才能正常进行SGs口业务。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NO|SGs路由组ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由组，要求全局唯一。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NO|SGs路由组ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由组，要求全局唯一。
STATUS|路由组状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs路由组状态。取值为枚举类型：关闭状态（CLOSED）开启状态（OPEN）
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs路由组查询结果。查询结果为枚举类型：查询成功（SUCCESS）查询失败（FAIL）连接不存在（NOTEXIST）
REASON|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示SGs路由组查询结果。查询结果为枚举类型：连接不存在（NOTEXIST）






[](None)命令举例 


查询SGs路由组ID为1的SGs路由组状态。 


SHOW SGSROUTEGRPSTATUS:SGSRTGRPID=1； 


`

命令 (No.1): SHOW SGSROUTEGRPSTATUS:SGSRTGRPID=1;

SGs路由组ID   路由组状态   查询结果
-----------------------------------
1             开启状态     查询成功
-----------------------------------
记录数 1

命令执行成功（耗时 0.041 秒）。
 ` 








父主题： [SGs管理](../../zh-CN/tree/N_1263_sgs_management_combo_gngp.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询VLR局向状态(SHOW VLROFFICESTATUS) 
### 查询VLR局向状态(SHOW VLROFFICESTATUS) 


[](None)命令功能 


该命令用于查询SGs口VLR局向状态。只有局向状态可达才能正常进行SGs口业务。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示特定的VLR局向标识






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示VLR局向状态查询结果。取值含义如下：SUCCESS：查询成功FAILURE：查询失败NOTEXIST：指定的局向不存在
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数。|该参数用于指示特定的VLR局向标识
VLROFFICEST|VLR局向状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向状态。取值含义如下：UNREACH：不可达REACH：可达UNKNOWN：未知






[](None)命令举例 


查询SGs口VLR局向状态。 


SHOW VLROFFICESTATUS; 


`

命令 (No.1): SHOW VLROFFICESTATUS;

VLR局向标识   VLR局向状态
---------------------------------
1             可达
---------------------------------
记录数 1

命令执行成功（耗时 0.041 秒）。
 ` 








父主题： [SGs管理](../../zh-CN/tree/N_1263_sgs_management_combo_gngp.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询VLR POOL信息(SHOW VLRPOOLINFO) 
### 查询VLR POOL信息(SHOW VLRPOOLINFO) 


[](None)命令功能 


该命令用于查询SGs口VLR POOL下各个VLR局向的优先级、权重和状态等信息。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定SGs口VLR POOL标识






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示查询VLRPOOL信息结果。取值含义如下：SUCCESS：查询成功FAILURE：查询失败NOTEXIST：指定的VLR POOL不存在NOTSUPPORT：不支持VLR POOL
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数。|该参数用于指定SGs口VLR POOL标识
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数。|该参数用于指示特定的VLR局向标识
VLRLEVEL|VLR级别|参数可选性:任选参数；参数类型:整数。|该参数用于指示SGs口VLR局向在VLR POOL中的优先级别, 数值越低优先级越高。
VLRWT|VLR权重|参数可选性:任选参数；参数类型:整数。|该参数用于指示SGs口VLR局向在VLR POOL中的权重。
VLROFFICEST|VLR局向状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向状态。取值含义如下：UNREACH：不可达REACH：可达UNKNOWN：未知
CSMOLR|支持CS-MO-LCS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向是否支持CS-MO-LR功能。CS的主叫发起的位置定位功能是指：LTE网络在进行联合附着时，核心网通知手机，它联合附着的MSC支持该功能。手机如果要发起主叫定位来定位自己所处的位置信息，可以通过CSFB方式回退到2G/3G网络进行定位。取值含义如下：未知（UNKNOWN）：不确定或者不关心VLR局向是否支持CS-MO-LR功能支持（SUPPORT）：VLR局向支持CS-MO-LR功能不支持（NOTSUPPORT）：VLR局向不支持CS-MO-LR功能
IMSISTART|IMSI后三位起始值|参数可选性:任选参数；参数类型:整数。|该参数用于指示归属于此VLR局向的用户的IMSI后三位数值区间的起始值。
IMSIEND|IMSI后三位终止值|参数可选性:任选参数；参数类型:整数。|该参数用于指示归属于此VLR局向的用户的IMSI后三位数值区间的终止值。






[](None)命令举例 


查询SGs口VLR POOL信息。 


SHOW VLRPOOLINFO:VLRPOOLID=1; 


`

命令 (No.2): SHOW VLRPOOLINFO:VLRPOOLID=1;

VLR POOL标识   VLR局向标识   VLR级别   VLR权重   VLR局向状态   支持CS-MO-LCS功能   IMSI后三位起始值   IMSI后三位终止值
----------------------------------------------------------------------------------------------------------------------
1              0             0         0         不可达        未知                111                222
----------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.723 秒）。
 ` 








父主题： [SGs管理](../../zh-CN/tree/N_1263_sgs_management_combo_gngp.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询VLR名称(SHOW VLRNAME) 
### 查询VLR名称(SHOW VLRNAME) 


[](None)命令功能 


该命令用于查询邻接VLR网元的VLR NAME。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|SGs连接编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2047。|该参数用于标识一条SGs连接。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询结果。
ID|SGs连接编号|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条SGs连接。
VLRNAME|VLR名称|参数可选性:任选参数；参数类型:字符型。|该参数用于标识VLR网元的名称。






[](None)命令举例 


查询SGs链路741对应的VLR名称。 


SHOW VLRNAME:ID=741; 


`

命令 (No.1): SHOW VLRNAME:ID=741;

SGs连接编号    VLR名称
----------------------
741            ZTE-VLR
----------------------
记录数 1

命令执行成功（耗时 0.041 秒）。
 ` 








父主题： [SGs管理](../../zh-CN/tree/N_1263_sgs_management_combo_gngp.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### VLR局向手动恢复(RESTORE VLR) 
### VLR局向手动恢复(RESTORE VLR) 


[](None)命令功能 


该命令用于VLR局向手动恢复。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指定SGs口VLR局向标识。






[](None)命令举例 


恢复VLR局向号为711的所有用户。 


RESTORE VLR:VLROFFICEID=711; 


`

命令 (No.1): RESTORE VLR:VLROFFICEID=711;

结果
---------
成功
---------
记录数 1

命令执行成功（耗时 0.078 秒）。
 ` 








父主题： [SGs管理](../../zh-CN/tree/N_1263_sgs_management_combo_gngp.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 取消手动恢复VLR局向(CANCEL RESTORE VLR) 
### 取消手动恢复VLR局向(CANCEL RESTORE VLR) 


[](None)命令功能 


该命令用于取消手动恢复VLR局向。 




[](None)注意事项 


当不输入局向号时，将取消所有处于手动卸载状态的局向。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指定SGs口VLR局向标识。






[](None)命令举例 


取消恢复VLR局向号为711的所有用户。 


CANCEL RESTORE VLR:VLROFFICEID=711; 


`

命令 (No.1): CANCEL RESTORE VLR:VLROFFICEID=711;
结果
---------
成功
---------
记录数 1

命令执行成功（耗时 0.078 秒）。
 ` 








父主题： [SGs管理](../../zh-CN/tree/N_1263_sgs_management_combo_gngp.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 计费管理 
## 计费管理 


[](None)背景知识 

            
            计费管理用于人工控制系统生成的话单。
        


[](None)功能描述 

            
            该功能包括保存MP缓冲区话单、回吐保存在硬盘的话单、停止回吐保存在硬盘的话单以及查询计费的信息。
        


[](None)相关主题 



 

保存MP缓冲区话单(SAVE CDR)
 

 

回吐MP已经保存在硬盘的话单(SEND CDR)
 

 

停止回吐MP已经保存在硬盘的话单(NO SEND CDR)
 

 

查询计费信息(SHOW BILLINFO)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 保存MP缓冲区话单(SAVE CDR) 
### 保存MP缓冲区话单(SAVE CDR) 


[](None)命令功能 

该命令用于保存MP话单内存缓冲区的话单到硬盘文件。仅当SGSN无法将话单发送到CG时，比如CG故障、SGSN和CG之间的通讯故障、SGSN突发产生大量话单、单板重启等，SGSN不能及时将这些话单传送给CG时，使用该命令。该命令执行成功后，当前MP模块临时保存在话单内存缓冲区的话单被保存到硬盘文件。


[](None)注意事项 



 
MP单板的主板才有可能产生需要保存的话单，备板不产生也不保存话单。
 

 
该命令仅对当前MP模块有效，如果需要整个单板都保存话单，需要对该单板的所有MP模块分别执行该命令。
 

 
执行该命令后，MP模块还有可能继续产生需要保存的话单。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数表示命令执行的MP实例号，查询命令参见 SHOW SCINFO。
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)命令举例 


命令2号CMP实例当前的主板立即保存内存缓冲区的话单到硬盘。 


SAVE CDR:SC=2; 








父主题： [计费管理](../../zh-CN/tree/N_130840203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 回吐MP已经保存在硬盘的话单(SEND CDR) 
### 回吐MP已经保存在硬盘的话单(SEND CDR) 


[](None)命令功能 

该命令用于发送保存在硬盘文件的话单。当且仅当当前MP模块使用过[NO SEND CDR](1263070.html)命令停止发送保存到文件的话单后，如果需要重新发送已经保存的话单，使用该命令。该命令执行成功后，本模块保存在硬盘文件上的话单继续发送到CG。


[](None)注意事项 



 
当前MP模块使用过NO SEND CDR命令停止发送话单后，必须使用本命令，才能继续发送保存的话单。
 

 
该命令仅对当前MP模块的主板或者备板有效，如果需要整个单板都发送保存的话单，需要对该单板的所有MP模块分别执行该命令，如果MP模块的主备板都要发送保存的话单，需要对模块的主备板都执行该命令。
说明：正常情况下，备板不保存话单，但是如果执行过主备倒换，原主板的话单文件就变成当前备板的话单文件，此时，需要对当前备板执行该命令。
 

 
该命令默认是发向MP主板的，如果FLAG不填写，则是向主板发送，如果发向备板，必须填写FLAG="SLAVE"。

 

 
备板不直接发送话单到CG，只能通过主板发送。

 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数表示命令执行的MP实例号，查询命令参见 SHOW SCINFO。
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
FLAG|主备属性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:MASTER。|该参数表示执行的模块的主备属性。其取值含义如下所示。MASTER： 主板






[](None)命令举例 


命令2号CMP实例当前的主板发送保存在文件的话单到CG。 


SEND CDR:SC=2,FLAG="MASTER"; 








父主题： [计费管理](../../zh-CN/tree/N_130840203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 停止回吐MP已经保存在硬盘的话单(NO SEND CDR) 
### 停止回吐MP已经保存在硬盘的话单(NO SEND CDR) 


[](None)命令功能 

该命令用于停止发送保存在硬盘文件的话单。当需要停止发送硬盘文件的话单，比如单板即将重启时，使用该命令。该命令执行成功后，本模块保存在硬盘文件上的话单不会再发送到CG。


[](None)注意事项 



 
当当前MP模块使用过该命令后，如果需要重新发送已经保存的话单，且单板没有重启，必须使用命令SEND CDR才能继续发送。执行SHOW BILLINFO命令，若查询结果中SENDFLAG字段值为‘No’时，表明使用过该命令。
 

 
该命令仅对当前MP模块的主板和备板有效，如果需要整个单板都停止发送保存的话单，需要对该单板的所有模块分别执行该命令，如果MP模块的主备板都要停止发送保存的话单，需要对模块的主备板都执行该命令。
说明：正常情况下，备板不保存话单，但是如果执行过主备倒换，原主板的话单文件就变成当前备板的话单文件，此时，需要对当前备板执行该命令。
 

 
该命令默认是发向主板的，如果FLAG不填写，则是向主板发送，如果发向备板，必须填写FLAG="SLAVE"。

 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数表示命令执行的MP实例号，查询命令参见 SHOW SCINFO。
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
FLAG|主备属性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:MASTER。|该参数表示执行的模块的主备属性。其取值含义如下所示。MASTER： 主板






[](None)命令举例 


命令2号CMP实例当前的主板停止发送保存在文件的话单到CG。 


NO SEND CDR:SC=2,FLAG="MASTER"; 








父主题： [计费管理](../../zh-CN/tree/N_130840203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询计费信息(SHOW BILLINFO) 
### 查询计费信息(SHOW BILLINFO) 


[](None)命令功能 

该命令用于查询MP模块的某个CG的状态信息。当需要查询CG状态或者保存的话单文件或者单板硬盘使用情况时，使用该命令。该命令执行成功后，本模块该CG的状态信息以及单板的话单文件信息被显示。


[](None)注意事项 



 
对于备板，返回的CG状态和Ga 链路状态是无意义的，因为CG的状态和Ga链路是MP的主板管理的，MP的备板不直接跟CG通讯。
 

 
该命令默认是发向主板的，如果FLAG不填写，则是向主板发送，如果需要查询备板的硬盘容量、话单文件数等信息，必须填写FLAG="SLAVE"。

 

 
SERVERID可以通过SHOW CGCFG获得。 

 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数表示命令执行的MP实例号，查询命令参见 SHOW SCINFO。
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
FLAG|主备属性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:MASTER。|该参数表示执行的模块的主备属性。其取值含义如下所示。MASTER： 主板
SERVERID|CG服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|CG服务器ID，查询命令参见SHOW CGCFG。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数表示命令执行的MP实例号，查询命令参见 SHOW SCINFO。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
FLAG|主备属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示执行的模块的主备属性。其取值含义如下所示。MASTER： 主板
RESULT|返回结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示执行命令的结果。其取值含义如下所示。SUCCESS：命令执行成功FAILURE：命令执行失败TIMEOUT：命令执行超时UNCONF：命令参数携带的CG服务器ID未配置，可通过SHOW CGCFG查询。
GALINK|Ga口链路状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询的Ga链路的状态，具体含义如下所示。CONNECT： 正常连接状态DISCONNECTED：链路断开INIT：初始状态，MP单板刚启动还未CG建链INVALID：无效状态
CGSTATUS|CG状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询的CG服务器的状态，如是否能接收话单，其取值含义如下所示。NORMAL：正常状态CGFULL：CG服务器硬盘满，CG不能正常接收话单INVALID：无效状态
AFILE|是否有A文件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示如果当前命令查询的CG服务器状态是否异常，该CG的话单是否正在保存，具体含义如下所示。NO：不存在A文件YES：存在A文件
SENDFLAG|发送话单标记是否有效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示当前命令查询的模块是否处理了NO SEND CDR命令。其取值含义如下所示。NO：未处理过该命令YES：处理过该命令
BNUM|B文件的个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~999999。|该参数表示当前命令查询的模块保存的话单文件个数，不包括损坏的话单文件。
ENUM|E文件的个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~999999。|该参数表示当前命令查询的模块保存的话单文件被损坏个数。
VOLUME|硬盘容量（M）|参数可选性:任选参数；参数类型:整数。|该参数表示当前命令查询的模块所在的单板的硬盘总容量。
FREEVOLUME|硬盘剩余可用容量（M）|参数可选性:任选参数；参数类型:整数。|该参数表示当前命令查询的模块所在的单板的硬盘剩余可以使用的容量。
EXISTLOCENCCDR|是否存在加密本地话单|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示当前命令查询的模块是否存在加密本地话单。






[](None)命令举例 


查询11号CMP实例当前的主板的计费相关信息。 


SHOW BILLINFO:SC=11,FLAG="MASTER",SERVERID=1; 


`

命令 (No.1):  SHOW BILLINFO:SC=11,FLAG="MASTER",SERVERID=1;

CMP实例号   主备属性   返回结果   Ga口链路状态   CG状态           是否有A文件   发送话单标记是否有效   B文件的个数   E文件的个数   硬盘容量（M）   硬盘剩余可用容量（M）   是否存在加密本地话单
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
11          主用       成功       连接           正常             否            是                     0             0             281604          266732                   是
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.049 秒）。
` 








父主题： [计费管理](../../zh-CN/tree/N_130840203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## S102局向管理 
## S102局向管理 


[](None)背景知识 


为支持用户从LTE网络回落到CDMA2000进行语音呼叫，MME通过IWS网元完成与MSC的互通。 


MME与IWS网元的接口为S102接口，一个IWS网元对于MME则是S102局向。为实现IWS网元的容灾，MME可连接多个IWS网元，MME与IWS网元之间连接是否正常，在MME内可维护此连接状态，表现为S102局向状态。 




[](None)功能描述 


本功能模块可查询MME与IWS网元之间连接是否正常， 一个IWS网元在MME中则为一个S102局向，当S102局向状态正常时，MME与此IWS网元连接正常。 


本模块分为查询单个S102局向状态和同时查询所有S102局向状态两种方式。 




[](None)相关主题 



 

查询S102局向状态(SHOW S102OFFICE STATUS)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询S102局向状态(SHOW S102OFFICE STATUS) 
### 查询S102局向状态(SHOW S102OFFICE STATUS) 


[](None)命令功能 

该命令用于查询S102局向状态。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示查询S102局向的方式。取值如下：所有连接：查询所有S102局向。指定连接：查询指定S102局向。
OFFICEID|S102局向ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一个S102局向。
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示查询结果。取值如下：成功。查询DB失败。指定局向ID不存在。
OFFICEID|S102局向ID|参数可选性:任选参数；参数类型:整数。|该参数用于标识一个S102局向。
STATUS|局向状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示S102局向状态。取值如下：OPEN：局向状态正常。CLOSE：局向状态故障。






[](None)命令举例 


查询3号CMP实例中所有S102局向的状态。 


SHOW S102OFFICE STATUS:TYPE="ALL",SC=3; 


`

命令 (No.1):SHOW S102OFFICE STATUS:TYPE="ALL",SC=3;

执行结果 
---------
成功
---------
记录数 1

S102局向ID  局向状态
---------------------------------
1 Open 
---------------------------------
记录数 1

命令执行成功（耗时 0.297 秒）。
 ` 








父主题： [S102局向管理](../../zh-CN/tree/N_130840205.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## KPI监控人工操作 
## KPI监控人工操作 


[](None)背景知识 


在KPI监控功能自动发现异常时，会进行告警。告警包含内容不多，有时需要人工帮助获取发生具体故障的KPI值，再次确认真正发生了故障。本命令即用于人工查询指定SC上的KPI异常记录。 




[](None)功能描述 


该功能可以人工查询指定SC上的用于KPI异常监控的记录。 




[](None)相关主题 



 

查询KPI监控人工操作(SHOW UP KPIPARAM)
 

 

查询CMP的模块的KPI参数(SHOW CMP KPIPARAM)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询KPI监控人工操作(SHOW UP KPIPARAM) 
### 查询KPI监控人工操作(SHOW UP KPIPARAM) 


[](None)命令功能 

查询KPI监控人工操作


[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|UP逻辑编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|该参数用于设置UP模块的逻辑编号。
COUNT|返回周期数|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。默认值:1。|该参数用于设置返回统计周期的数量。
ERR|只需错误记录|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:。|该参数用于设置查询状态是否只显示有异常的记录。是：表示该命令的执行结果只显示异常记录，如果无异常则不显示。否：表示无论是否异常，查询结果都会显示。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|UP逻辑编号|参数可选性:任选参数；参数类型:整数。|该参数用于设置UP模块的逻辑编号。
SEQ|序号|参数可选性:任选参数；参数类型:整数。|该参数用于显示标识统计的序号。
KPITYPE|KPI类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示使用的KPI类型。2G Attach(2GATTACH)：2G附着。3G Attach(3GATTACH)：3G附着。4G Attach(4GATTACH)：4G附着。2G PDP Active(2GPDPACTIVE)：2G PDP激活。3G PDP Active(3GPDPACTIVE)：3G PDP激活。
RATE|流量(Mbps)|参数可选性:任选参数；参数类型:整数。|该参数用于显示查询的UP模块的流量。
STATUS|状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于显示查询的UP模块是否被判断为异常。






[](None)命令举例 


查询KPI监控人工操作，UP逻辑编号为1，返回周期数为2，只需错误记录选择“否”。 


SHOW UP KPIPARAM:SC=1,COUNT=2,ERR="NO"; 


`

(No.1) : SHOW UP KPIPARAM:SC=1,COUNT=2,ERR="NO";
UP逻辑编号 序号 KPI类型 流量(Mbps) 状态 
---------------------------------------
2          2    2G流量  1          正常 
2          2    3G流量  10         正常 
2          3    2G流量  1          正常 
2          3    3G流量  10         正常 
---------------------------------------
记录数：4

命令执行成功（耗时 0.042 秒）。
` 








父主题： [KPI监控人工操作](../../zh-CN/tree/N_1269686.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询CMP的模块的KPI参数(SHOW CMP KPIPARAM) 
### 查询CMP的模块的KPI参数(SHOW CMP KPIPARAM) 


[](None)命令功能 

查询CMP的模块的KPI参数


[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP逻辑编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65534。默认值:1。|该参数用于设置CMP模块的逻辑编号。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
KPITYPE|KPI类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示使用的KPI类型。2G Attach(2GATTACH)：2G附着。3G Attach(3GATTACH)：3G附着。4G Attach(4GATTACH)：4G附着。2G PDP Active(2GPDPACTIVE)：2G PDP激活。3G PDP Active(3GPDPACTIVE)：3G PDP激活。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP逻辑编号|参数可选性:任选参数；参数类型:整数。|该参数用于设置CMP模块的逻辑编号。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
SEQ|序号|参数可选性:任选参数；参数类型:整数。|该参数用于显示输出结果的编号。
KPITYPE|KPI类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示使用的KPI类型。2G Attach(2GATTACH)：2G附着。3G Attach(3GATTACH)：3G附着。4G Attach(4GATTACH)：4G附着。2G PDP Active(2GPDPACTIVE)：2G PDP激活。3G PDP Active(3GPDPACTIVE)：3G PDP激活。
PARAM1|第1个KPI值|参数可选性:任选参数；参数类型:字符型。|该参数表示相应KPI类型的尝试次数。例如：当KPI类型选择为2G Attach，则该参数统计了2G附着的尝试次数。
PARAM2|第2个KPI值|参数可选性:任选参数；参数类型:字符型。|该参数表示相应KPI类型的成功次数。例如：当KPI类型选择为2G Attach，则该参数统计了2G附着的成功次数。






[](None)命令举例 


查询CMP模块KPI参数。CMP逻辑编号为1。 


SHOW CMP KPIPARAM:SC=1; 


`

命令 (No.9): SHOW CMP KPIPARAM:SC=2;

CMP逻辑编号   序号    KPI类型  第1个KPI值      第2个KPI值       
---------------------------------------------------------------------
1             1      2G Attach 0              16908290
---------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.047 秒）。
` 








父主题： [KPI监控人工操作](../../zh-CN/tree/N_1269686.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 用量和KPI查询 
## 用量和KPI查询 


[](None)背景知识 


虚拟化的网元可以根据系统负荷实时调整虚拟机个数，可以增加或删除一个或多个虚拟机。 


虚拟机缩扩容可以分为自动缩扩容和手动缩扩容。自动缩扩容即系统根据虚机负荷来判断是否进行缩扩容，并自动完成缩扩容；手动缩扩容即人工操作进行缩扩容。 


处理流量是IPB（转发控制面信令和媒体面报文）和USUP（处理SGSN 2G、3G上下行用户面报文）虚机的重要性能指标，IPB和USUP支持基于流量比例的缩扩容。IPB支持负荷分担备份冗余，USUP支持1+1互备冗余，通过闭塞/解闭塞操作，可以将报文交给其他虚机（IPB）或伙伴虚机（USUP）处理，从而对该虚机进行维护。 




[](None)功能描述 


虚拟机动态管理可以方便运营商根据当前系统负荷自动或手动对虚拟机个数进行增加或减少，以便提高系统资源利用率，达到节能减排目的。 


本功能主要包括以下内容： 



 


                        手动扩容：通过命令
                        INC SC
                        手动完成虚拟机的增加。
                    
 

 


                        手动缩容：通过命令
                        DEC SC
                        手动完成虚拟机的减少。
                    
 

 




[](None)相关主题 



 

查询UP流量(Show UP Traffic)
 

 

查询GnGp用户相关统计信息(SHOW USER STATS)
 

 

查询Gs用户相关统计信息(SHOW GS USER STATS)
 

 

查询MME用户相关统计信息(SHOW MMEUSER STATS)
 

 

查询SGs用户相关统计信息(SHOW SGS USER STATS)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询UP流量(Show UP Traffic) 
### 查询UP流量(Show UP Traffic) 


[](None)命令功能 


查询UP流量 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|UP实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|UP实例号。






[](None)命令举例 


用量和KPI查询。 


Show UP Traffic 


`

(No.1) : Show UP Traffic:
-----------------NFS_MMESGSN_0----------------
UP实例号 2G每秒报文个数（kpps） 3G每秒报文个数（kpps） 2G每秒字节数（Mbps） 3G每秒字节数（Mbps） 
-------------------------------------------------------------------------------------------------
1        0                      0                      0                    0                    
-------------------------------------------------------------------------------------------------
记录数：1
` 








父主题： [用量和KPI查询](../../zh-CN/tree/N_dm_mml_combo_gngp_vmmgr.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询用户相关统计信息(SHOW USER STATS) 
### 查询用户相关统计信息(SHOW USER STATS) 


[](None)命令功能 


该命令用于查询用户相关统计信息。 




[](None)注意事项 

返回的是SGSN用户的相关统计信息。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
QUERYTYPE|查询方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:。|该参数用于设置查询方式。取值含义：按网元查询。按模块查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:字符型。|用户归属的的CMP实例号。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
ATTUSER2G|附着用户数（2G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 2G附着用户数。
ATTUSER3G|附着用户数（3G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 3G附着用户数。
IDLEUSER2G|空闲用户数（2G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 2G空闲用户数。
IDLEUSER3G|空闲用户数（3G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 3G空闲用户数。
DETUSER2G|分离用户数（2G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 2G分离用户数。
DETUSER3G|分离用户数（3G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 3G分离用户数。
ACTUSER2G|激活用户数（2G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 2G激活用户数。
ACTUSER3G|激活用户数（3G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 3G激活用户数。
ACTPDP2G|激活PDP上下文数（2G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 2G激活PDP上下文数。
ACTPDP3G|激活PDP上下文数（3G）|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN 3G激活PDP上下文数。






[](None)命令举例 


按照网元来查询SGSN用户的统计信息。 


SHOW USER STATS:QUERYTYPE=BY_NE; 


`

命令 (No.1): SHOW USER STATS:QUERYTYPE=BY_NE;

模块号   附着用户数（2G）   附着用户数（3G）   空闲用户数（2G）   空闲用户数（3G）   分离用户数（2G）   分离用户数（3G）   激活用户数（2G）   激活用户数（3G）   激活PDP上下文数（2G）   激活PDP上下文数（3G）
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         0                  0                  0                  0                  0                  0                  0                  0                  0                       0
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.862 秒）。
` 








父主题： [用量和KPI查询](../../zh-CN/tree/N_dm_mml_combo_gngp_vmmgr.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询Gs用户相关统计信息(SHOW GS USER STATS) 
### 查询Gs用户相关统计信息(SHOW GS USER STATS) 


[](None)命令功能 


该命令用于查询用户相关统计信息。 




[](None)注意事项 

返回的是SGSN GS用户的统计信息。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
QUERYTYPE|查询方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:。|该参数用于设置查询方式。取值含义：按网元查询。按模块查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:字符型。|用户归属的的CMP实例号。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
USER_NUMBER|Gs用户数|参数可选性:任选参数；参数类型:整数。|统计得到的SGSN GS用户数。






[](None)命令举例 


按照网元来查询SGSN GS用户的统计信息。 


SHOW GS USER STATS:QUERYTYPE="BY_NE"; 


`

命令 (No.1): SHOW GS USER STATS:QUERYTYPE="BY_NE";

模块号 Gs用户数 
-----------------
  0 
-----------------
记录数 1

命令执行成功（耗时 0.109 秒）。
` 








父主题： [用量和KPI查询](../../zh-CN/tree/N_dm_mml_combo_gngp_vmmgr.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME用户相关统计信息(SHOW MMEUSER STATS) 
### 查询MME用户相关统计信息(SHOW MMEUSER STATS) 


[](None)命令功能 


该命令用于查询MME用户相关统计信息。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
QUERYTYPE|查询方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:。|该参数用于设置查询方式。取值含义：按网元查询。按模块查询。
USERTYPE|用户类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:LTE_NB-IOT。|该参数用于设置用户类型。取值含义：0：LTE用户和NB-IoT用户。1：LTE用户。2：NB-IoT用户。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:字符型。|用户归属的的CMP实例号。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
ATTUSER|附着用户数|参数可选性:任选参数；参数类型:整数。|统计得到的附着用户数。
IDLEUSER|空闲用户数|参数可选性:任选参数；参数类型:整数。|统计得到的空闲用户数。
BUSYUSER|连接用户数|参数可选性:任选参数；参数类型:整数。|统计得到的连接用户数。
DETUSER|分离用户数|参数可选性:任选参数；参数类型:整数。|统计得到的分离用户数。
IMPDETUSER|隐式分离用户|参数可选性:任选参数；参数类型:整数。|统计得到的隐式分离用户数。
MMUSER|MM上下文|参数可选性:任选参数；参数类型:整数。|统计得到的MM上下文数。
SESSIONNUM|会话上下文数|参数可选性:任选参数；参数类型:整数。|统计得到的会话上下文数。
PDPNUM|承载上下文|参数可选性:任选参数；参数类型:整数。|统计得到的承载上下文数。






[](None)命令举例 


按照网元来查询MME用户相关统计信息； 


SHOW MMEUSER STATS:QUERYTYPE=BY_NE; 


`

命令 (No.1): SHOW MMEUSER STATS:QUERYTYPE=BY_NE;

模块号   附着用户数   空闲用户数   连接用户数   分离用户数   隐式分离用户   MM上下文     会话上下文数   承载上下文
------------------------------------------------------------------------------------------------------------------
         1            0            1            0            0              1            1              1
------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.043 秒）。
` 








父主题： [用量和KPI查询](../../zh-CN/tree/N_dm_mml_combo_gngp_vmmgr.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGs用户相关统计信息(SHOW SGS USER STATS) 
### 查询SGs用户相关统计信息(SHOW SGS USER STATS) 


[](None)命令功能 

查询SGs用户相关统计信息


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
QUERYTYPE|查询方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:。|查询方式：按网元 按模块号 按VLR局向






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:整数。|用户的业务处理CMP实例号。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
VLR|VLR局向|参数可选性:任选参数；参数类型:整数。|VLR局向。
USER_NUMBER|SGs用户数|参数可选性:任选参数；参数类型:整数。|SGs用户数。






[](None)命令举例 


按照网元来查询SGs用户相关统计信息。 


SHOW SGS USER STATS; 


`

命令 (No.3): SHOW SGS USER STATS

SGs用户数	
-------------------
0	
-------------------
记录数 1

命令执行成功（耗时 0.058 秒）。
` 








父主题： [用量和KPI查询](../../zh-CN/tree/N_dm_mml_combo_gngp_vmmgr.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## TCE跟踪管理 
## TCE跟踪管理 


[](None)背景知识 

            
            TCE（Trace Collection Entity，跟踪采集实体）跟踪管理用于查询和删除通过OMC布控的Trace用户信息。
        


[](None)功能描述 

            
            TCE跟踪管理包括查询TCE信息和删除TCE信息。
        


[](None)相关主题 



 

查询TCE信息(SHOW TCE INFO)
 

 

删除TCE信息(DEL TCE INFO)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询TCE信息(SHOW TCE INFO) 
### 查询TCE信息(SHOW TCE INFO) 


[](None)命令功能 

该命令用于查询TCE信息。


[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NUMBERTYPE|号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|跟踪目标类型，支持IMSI、MSISDN、参考号和全部号码类型。
NUMBER|号码|参数可选性:任选参数；参数类型:字符型；参数范围为:6~15个字符。|跟踪目标值。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|命令操作类型。
NUMBER|号码|参数可选性:任选参数；参数类型:字符型。|跟踪目标值。
REFERENCE|参考号|参数可选性:任选参数；参数类型:字符型。|用于标识跟踪会话。
TRACEDEPTH|跟踪深度|参数可选性:任选参数；参数类型:整数。|跟踪的深度，根据深度的不同，要求上报的信息不同。
MSCSERVEREVENT|MSC Server跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要MSC Server网元跟踪的事件。
MGWEVENT|MGW跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要MGW网元跟踪的事件。
SGSNEVENT|SGSN跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要SGSN网元跟踪的事件。
GGSNEVENT|GGSN跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要GGSN网元跟踪的事件。
BMSCEVENT|BM-SC跟踪事件|参数可选性:任选参数；参数类型:字符型。|布控时需要BM-SC网元跟踪的事件。
MMEEVENT|MME跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要MME网元跟踪的事件。
PGWEVENT|PGW跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要PGW网元跟踪的事件
SGWEVENT|SGW跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要SGW网元跟踪的事件。
AMFEVENT|AMF跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要AMF网元跟踪的事件。
SMFEVENT|SMF跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要SMF网元跟踪的事件。
UPFEVENT|UPF跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要UPF网元跟踪的事件。
PCFEVENT|PCF跟踪事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要PCF网元跟踪的事件。
NETYPE|网元类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要跟踪的网元类型。
MSCSERVERINTERFACE|MSC Server接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要MSC Server网元跟踪的接口。
MGWINTERFACE|MGW接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要MGW网元跟踪的接口。
SGSNINTERFACE|SGSN接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要SGSN网元跟踪的接口。
GGSNINTERFACE|GGSN接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要GGSN网元跟踪的接口。
RNCINTERFACE|RNC接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要RNC网元跟踪的接口
BMSCINTERFACE|BM-SC接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要BM-SC网元跟踪的接口
MMEINTERFACE|MME接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要MME网元跟踪的接口。
SGWINTERFACE|SGW接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要SGW网元跟踪的接口。
PGWINTERFACE|PGW接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要PGW网元跟踪的接口。
ENBINTERFACE|eNB接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要eNodeB网元跟踪的接口。
HSSINTERFACE|HSS接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要HSS网元跟踪的接口。
EIRINTERFACE|EIR接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要EIR网元跟踪的接口。
AMFINTERFACE|AMF接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要AMF网元跟踪的接口。
PCFINTERFACE|PCF接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要PCF网元跟踪的接口。
SMFINTERFACE|SMF接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要SMF网元跟踪的接口。
UPFINTERFACE|UPF接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要UPF网元跟踪的接口。
NGINTERFACE|(Logical NG-RAN node) ng-eNB/gNB-CU-CP/gNB-CU-UP/gNB-DU接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|布控时需要gNodeB网元跟踪的接口。
IPADDRESS|IP地址|参数可选性:任选参数；参数类型:字符型。|布控时要求跟踪网元信息上报的目的地址。






[](None)命令举例 


根据IMSI查询用户的布控信息。 


SHOW TCE INFO:NUMBERTYPE="IMSI",NUMBER="460119990021002"; 








父主题： [TCE跟踪管理](../../zh-CN/tree/N_13084043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除TCE信息(DEL TCE INFO) 
### 删除TCE信息(DEL TCE INFO) 


[](None)命令功能 

该命令用于删除TCE信息。


[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NUMBERTYPE|号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|跟踪目标类型，支持IMSI、MSISDN、参考号和全部号码类型。
NUMBER|号码|参数可选性:任选参数；参数类型:字符型；参数范围为:6~15个字符。|跟踪目标值。






[](None)命令举例 


根据IMSI删除单个用户的布控信息。 


DEL TCE INFO:NUMBERTYPE="IMSI",NUMBER="460119990021002"; 








父主题： [TCE跟踪管理](../../zh-CN/tree/N_13084043.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## MME信令风暴抑制管理 
## MME信令风暴抑制管理 


[](None)背景知识 


信令风暴是由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。 


信令风暴抑制是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 


MME信令风暴抑制，具体包括附着请求信令风暴抑制、业务请求信令风暴抑制和PDN连接请求信令风暴抑制。 



                MME在各信令单位统计周期内统计各信令数，如果统计的信令数大于最大信令数，则MME将用户加入信令黑名单，并启动黑名单定时器。在信令黑名单定时器管理时间内，要么信令被拒绝或丢弃，要么FAKE APN PDN连接建立成功但用户用此连接无法上网。信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。MME信令风暴抑制配置参见
                [SET SIGSRESTRAIN](../mml/1260719.html)
                。
            




[](None)功能描述 


为了方便运营商对信令黑名单用户进行管理，“MME信令风暴抑制管理”提供以下功能： 



 


                        查询信令黑名单用户，命令参见
                        SHOW BLACK SUBSCRIBER
                        。
                    
 

 


                        查询单用户信令状态，命令参见
                        SHOW SUBSCRIBER SIGSTATUS
                        。
                    
 

 


                        用户移出信令黑名单功能，命令参见
                        MOVE SUBSCRIBER BLACK
                        。
                    
 

 




[](None)相关主题 



 

查询单用户信令状态(SHOW SUBSCRIBER SIGSTATUS)
 

 

用户移出信令黑名单(MOVE SUBSCRIBER BLACK)
 

 

查询信令黑名单用户(SHOW BLACK SUBSCRIBER)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询单用户信令状态(SHOW SUBSCRIBER SIGSTATUS) 
### 查询单用户信令状态(SHOW SUBSCRIBER SIGSTATUS) 


[](None)命令功能 


该命令用于查询某用户的信令状态是否在黑名单中。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|该参数用于表示输入的用户IMSI号码。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|执行结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示命令执行结果的详细信息。
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于表示输入的用户IMSI号码。
BLACK|是否黑名单|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示用户是否在信令黑名单。取值为0：用户不在信令黑名单。取值为1：用户在信令黑名单。
BLACKTYPE|黑名单标记|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示用户黑名单类型，包括附着请求信令黑名单、业务请求信令黑名单和PDN连接请求信令黑名单。该参数值为0时，表示用户不在信令黑名单。






[](None)命令举例 


查询IMSI为460013333333333的用户信令状态。 


SHOW SUBSCRIBER SIGSTATUS:IMSI="460013333333333"; 


`

命令 (No.2):  SHOW SUBSCRIBER SIGSTATUS:IMSI="460013333333333";

IMSI              是否黑名单                黑名单标识
-----------------------------------------------------------
460013333333333   是                        附着请求信令
-----------------------------------------------------------
记录数 1


命令执行成功（耗时 0.049 秒）。

` 








父主题： [MME信令风暴抑制管理](../../zh-CN/tree/N_13084039.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 用户移出信令黑名单(MOVE SUBSCRIBER BLACK) 
### 用户移出信令黑名单(MOVE SUBSCRIBER BLACK) 


[](None)命令功能 


该命令用于将某信令黑名单用户从黑名单中移出。当用户进入附着请求/业务请求/PDN连接请求信令黑名单，需要把该用户从黑名单中移出时，执行此命令。 




[](None)注意事项 


对于信令黑名单用户，当黑名单定时器超时后，用户自动从信令黑名单移除并能进行上网业务，但是对某单用户而言，运营商可以据实际需求执行此命令手动移除黑名单。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|该参数用于表示输入的用户IMSI号码。






[](None)命令举例 


把IMSI为460013333333333的用户移除信令黑名单。 


MOVE SUBSCRIBER BLACK:IMSI="460013333333333"; 








父主题： [MME信令风暴抑制管理](../../zh-CN/tree/N_13084039.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询信令黑名单用户(SHOW BLACK SUBSCRIBER) 
### 查询信令黑名单用户(SHOW BLACK SUBSCRIBER) 


[](None)命令功能 


该命令用于按业务模块查询信令黑名单用户或查询全局信令黑名单用户。 



 
按业务模块查询信令黑名单用户时，需要输入需要查询的业务模块号。
 

 
查询全局信令黑名单用户时，不需要输入业务模块号，直接执行查询命令。
 

 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|该参数用于表示用户IMSI在MME上的归属实例。通过SHOW SCINFO 查询。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RSTSC|CMP实例号|参数可选性:任选参数；参数类型:整数。|该参数用于表示查询的CMP实例。
RESULT|执行结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示命令执行结果的详细信息。
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于表示查询出的信令黑名单用户IMSI号码。
BLACKTYPE|黑名单标记|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示用户黑名单类型，包括附着请求信令黑名单、业务请求信令黑名单和PDN连接请求信令黑名单。该参数值为0时，表示用户不在信令黑名单。
SC|CMP实例号|参数可选性:任选参数；参数类型:整数。|该参数用于表示用户IMSI在MME上的归属实例。通过SHOW SCINFO 查询。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)命令举例 


查询2号模块的信令黑名单用户。 


SHOW BLACK SUBSCRIBER:MODULE=2; 


`

命令 (No.1): SHOW BLACK SUBSCRIBER:MODULE=2;

模块号    执行结果 
-------------------
2            成功 
-------------------
记录数 1

输出文件路径
---------------
当前命令执行的结果被另存为文件，请点击这个URL下载。
http://129.0.6.1:2323/combo_mmegngp_sgsn_25/server/tmp/cm/SHOW BLACK SUBSCRIBER_25-2014-07-01 11-25-23.zip
---------------
记录数 1

命令执行成功（耗时 14.5 秒）。

` 








父主题： [MME信令风暴抑制管理](../../zh-CN/tree/N_13084039.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGSN信令风暴抑制管理 
## SGSN信令风暴抑制管理 


[](None)背景知识 


信令风暴是由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。 


信令风暴抑制是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 


SGSN信令风暴抑制，具体包括附着请求信令风暴抑制、业务请求信令风暴抑制和PDP激活请求信令风暴抑制。 



                SGSN在各信令单位统计周期内统计各信令数，如果统计的信令数大于最大信令数，则SGSN将用户加入信令黑名单，并启动黑名单定时器。在信令黑名单定时器管理时间内，要么信令被拒绝或丢弃，要么网络以FAKE APN让终端建立成功但无法上网。信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。SGSN信令风暴抑制配置参见
                [SET SGSN SIGSRESTRAIN](../mml/1260869.html)
                。
            




[](None)功能描述 


为了方便运营商对信令黑名单用户进行管理，“SGSN信令风暴抑制管理”提供以下功能： 



 


                        查询信令黑名单用户，命令参见
                        SHOW SGSN BLACK SUBSCRIBER
                        。
                    
 

 


                        查询单用户信令状态，命令参见
                        SHOW SGSN SUBSCRIBER SIGSTATUS
                        。
                    
 

 


                        用户移出信令黑名单功能，命令参见
                        MOVE SGSN SUBSCRIBER BLACK
                        。
                    
 

 




[](None)相关主题 



 

查询单用户信令状态(SHOW SGSN SUBSCRIBER SIGSTATUS)
 

 

用户移出信令黑名单(MOVE SGSN SUBSCRIBER BLACK)
 

 

查询信令黑名单用户(SHOW SGSN BLACK SUBSCRIBER)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询单用户信令状态(SHOW SGSN SUBSCRIBER SIGSTATUS) 
### 查询单用户信令状态(SHOW SGSN SUBSCRIBER SIGSTATUS) 


[](None)命令功能 

该命令用于查询某用户的信令状态是否在黑名单中。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|该参数用于表示输入的用户IMSI号码。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|执行结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示命令执行结果的详细信息。
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于表示输入的用户IMSI号码。
BLACK|是否黑名单|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示用户是否在信令黑名单。取值为0：用户不在信令黑名单。取值为1：用户在信令黑名单。
BLACKTYPE|黑名单标记|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示用户黑名单类型，包括附着请求信令黑名单、业务请求信令黑名单和PDP激活请求信令黑名单。该参数值为0时，表示用户不在信令黑名单。






[](None)命令举例 


查询IMSI为460013333333333的用户信令状态。 


SHOW SGSN SUBSCRIBER SIGSTATUS:IMSI="460013333333333"; 


`

命令 (No.1):  SHOW SGSN SUBSCRIBER SIGSTATUS:IMSI="460013333333333";

IMSI              是否黑名单                黑名单标识
-----------------------------------------------------------
460013333333333   是                        附着请求信令
-----------------------------------------------------------
记录数 1

命令执行成功（耗时 0.049 秒）。

` 








父主题： [SGSN信令风暴抑制管理](../../zh-CN/tree/N_12631701.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 用户移出信令黑名单(MOVE SGSN SUBSCRIBER BLACK) 
### 用户移出信令黑名单(MOVE SGSN SUBSCRIBER BLACK) 


[](None)命令功能 

该命令用于将某信令黑名单用户从黑名单中移出。当用户进入附着请求/业务请求/PDP激活请求信令黑名单，需要把该用户从黑名单中移出时，执行此命令。


[](None)注意事项 

对于信令黑名单用户，当黑名单定时器超时后，用户自动从信令黑名单移除并能进行上网业务，但是对某单用户而言，运营商可以据实际需求执行此命令手动移除黑名单。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:6~15个字符。|该参数用于表示输入的用户IMSI号码。






[](None)命令举例 


把IMSI为460013333333333的用户移除信令黑名单。 


MOVE SGSN SUBSCRIBER BLACK:IMSI="460013333333333"; 








父主题： [SGSN信令风暴抑制管理](../../zh-CN/tree/N_12631701.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询信令黑名单用户(SHOW SGSN BLACK SUBSCRIBER) 
### 查询信令黑名单用户(SHOW SGSN BLACK SUBSCRIBER) 


[](None)命令功能 


该命令用于按业务模块查询信令黑名单用户或查询全局信令黑名单用户。
 



 
按业务模块查询信令黑名单用户时，需要输入需要查询的业务模块号。
 

 
查询全局信令黑名单用户时，不需要输入业务模块号，直接执行查询命令。
 

 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|该参数用于表示用户IMSI在SGSN上的归属实例。通过SHOW SCINFO 查询。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RSTSC|CMP实例号|参数可选性:任选参数；参数类型:整数。|该参数用于表示查询的CMP实例。
RESULT|执行结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示命令执行结果的详细信息。
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于表示查询出的信令黑名单用户IMSI号码。
BLACKTYPE|黑名单标记|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示用户黑名单类型，包括附着请求信令黑名单、业务请求信令黑名单和PDP激活请求信令黑名单，该参数值为0时，表示用户不在信令黑名单。
SC|CMP实例号|参数可选性:任选参数；参数类型:整数。|该参数用于表示用户IMSI在SGSN上的归属实例。通过SHOW SCINFO 查询。
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)命令举例 


查询2号模块的信令黑名单用户。 


SHOW SGSN BLACK SUBSCRIBER:SC=2; 


`

命令 (No.1): SHOW SGSN BLACK SUBSCRIBER:SC=2;

CMP实例号    执行结果 
---------------------
2            成功 
---------------------
记录数 1

输出文件路径
---------------
当前命令执行的结果被另存为文件，请点击这个URL下载。
http://129.0.6.1:2323/combo_mmegngp_sgsn_25/server/tmp/cm/SHOW SGSN BLACK SUBSCRIBER_25-2014-07-01 11-25-23.zip
---------------
记录数 1

命令执行成功（耗时 14.5 秒）。

` 








父主题： [SGSN信令风暴抑制管理](../../zh-CN/tree/N_12631701.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## PGW拥塞管理 
## PGW拥塞管理 


[](None)背景知识 


APN拥塞控制是PGW的拥塞控制的一种，即PGW基于APN进行拥塞控制，当达到APN拥塞控制门限时，PGW在一段时间内不容许在该APN下建立新PDN连接；该时间段内，MME选择其他的PGW为该APN服务。 


PGW拥塞功能需要PGW配合实现，在运营商购买了APN拥塞功能License情况下，PGW在创建会话失败中明确给出原因是拥塞"APN congestion"，并携带PGW Back-Off Time，MME在指定的时间内对该APN的会话不选择该PGW，包括附着、PDN连接建立。
在拥塞时长达到PGW Back-Off Time时，MME恢复选择该PGW。 




[](None)功能描述 


本功能只在MME网元有效。 


通过PGW拥塞管理可以查询APN拥塞状态，包括PGW地址、APN名称、拥塞发生时间以及拥塞时长等信息。 



                设置本局支持PGW拥塞控制后，MME才能处理PGW的APN拥塞，同时查询到APN拥塞信息，通过命令
                [SET SOFTWARE PARAMETER](../mml/1268001.html)
                :PARAID=786763,PARAVALUE=1;设置MME支持PGW拥塞控制。
            




[](None)相关主题 



 

APN拥塞状态查询(SHOW APN CONGESTION)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### APN拥塞状态查询(SHOW APN CONGESTION) 
### APN拥塞状态查询(SHOW APN CONGESTION) 


[](None)命令功能 

APN拥塞查询


[](None)注意事项 



 
设置本局支持PGW拥塞功能后，MME才能处理PGW的APN拥塞，才能够查询到PGW APN拥塞信息。 
 

 
本功能只在MME网元有效。 
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IP|PGW地址|参数可选性:任选参数；参数类型:地址|该参数表示发生APN拥塞的PGW地址
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数表示发生拥塞的APN名称






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于记录发生拥塞的APN名称
IP|PGW地址|参数可选性:任选参数；参数类型:地址|该参数表示发生APN拥塞的PGW地址
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数表示发生拥塞的APN名称
BACKOFFTIME|拥塞时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于记录拥塞的时长
CONGESTTIME|拥塞发生时间|参数可选性:任选参数；参数类型:字符型。|该参数用于记录发生拥塞的时刻






[](None)命令举例 


查询全部的APN拥塞状态： 


SHOW APN CONGESTION; 


`

命令 (No.1): SHOW APN CONGESTION

PGW地址        APN名称                                         拥塞时长(秒)   拥塞发生时间    
-------------------------------------------------------------------------------------------------
100.150.0.21   zte.com.apn.epc.mnc003.mcc460.3gppnetwork.org   10             2015-10-21 04:32:20
------------------------------------------------------------------------------------------------- 
记录数 1

命令执行成功（耗时 0.231 秒）。
` 








父主题： [PGW拥塞管理](../../zh-CN/tree/N_12696391.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 网元过负荷控制 
## 网元过负荷控制 


[](None)背景知识 


MME的周边网元（HSS、SGW、PGW等）发生过负荷后，可以通过接口消息中的特定的信元将过负荷信息通知给MME，由MME根据过负荷信息完成到这些发生过负荷的网元的业务控制和消息缩减。 




[](None)功能描述 


网元过负荷控制动态管理主要完成对MME收到的来自HSS、SGW或PGW的过负荷信息的查询。 




[](None)相关主题 



 

查询HSS过负荷信息(SHOW HSS OVERLOAD INFO)
 

 

查询SGW负荷信息(SHOW SGW LOAD INFO)
 

 

查询PGW负荷信息(SHOW PGW LOAD INFO)
 

 

查询SGW过负荷信息(SHOW SGW OVERLOAD INFO)
 

 

查询PGW过负荷信息(SHOW PGW OVERLOAD INFO)
 

 

查询SGSN自动过负荷信息(SHOW AUTO CNG INFO)
 

 

查询MME负荷信息(SHOW MMES1LOAD)
 

 

查询MME自动过负荷信息(SHOW MME AUTO CNG INFO)
 

 

查询S6a ALC局向负荷控制信息(SHOW S6A ALCOFC CNG INFO)
 

 

MME自动过负荷日志上报(START MME AUTO CNG LOGRPT)
 

 

停止MME自动过负荷日志上报(STOP MME AUTO CNG LOGRPT)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询HSS过负荷信息(SHOW HSS OVERLOAD INFO) 
### 查询HSS过负荷信息(SHOW HSS OVERLOAD INFO) 


[](None)命令功能 


该命令用于查询MME接收到的不同HSS返回的过负荷信息。过负荷信息包括HSS主机名/域、过负荷信息序列号、报告类型、有效时间和缩减比例。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
HOST|HSS主机名/域|参数可选性:任选参数；参数类型:字符型；参数范围为:0~129个字符。|用于设置需要查询过负荷信息的HSS主机名/域。如果不设置该参数，将查询所有记录的过负荷的HSS信息。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
HOST|HSS主机名/域|参数可选性:任选参数；参数类型:字符型；参数范围为:0~129个字符。|用于设置需要查询过负荷信息的HSS主机名/域。如果不设置该参数，将查询所有记录的过负荷的HSS信息。
SEQNO|过负荷报告序列号|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|过负荷报告的序列号，可用于标识最近的过负荷报告。
RPTTYPE|报告类型|参数可选性:任选参数；参数类型:整数。|报告类型指示报告的适用范围是主机还是域。
VALIDDURATION|有效时间(秒)|参数可选性:任选参数；参数类型:整数。|报告的有效时间，超过有效时间报告失效。
REDUCTION|缩减百分比|参数可选性:任选参数；参数类型:整数。|发生过负荷后，HSS要求MME对后继业务的缩减百分比。
INFORMTIME|通知时间|参数可选性:任选参数；参数类型:字符型。|接收到该过负荷报告的时间。






[](None)命令举例 


查询HSS过负荷信息。其中HSS主机名/域为"zte.com"。 


SHOW HSS OVERLOAD INFO:HOST="zte.com"; 


`

命令执行成功（耗时 0.612 秒）。
命令 (No.10): SHOW HSS OVERLOAD INFO:HOST="zte.com"

HSS主机名/域   过负荷报告序列号   报告类型   有效时间(秒)  缩减百分比   通知时间
-------------------------------------------------------------------------------
zte.com        0xffff0000ffff     1          2421       88           2016-2-22 14:06:58
-------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.066 秒）。
 ` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGW负荷信息(SHOW SGW LOAD INFO) 
### 查询SGW负荷信息(SHOW SGW LOAD INFO) 


[](None)命令功能 


用于查询MME接收到的不同SGW返回的动态负荷信息。负荷信息包括SGW主机名、负荷信息序列号、负荷值。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SGWNAME|SGW主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|用于设置需要查询负荷信息的SGW主机名。如果不设置该参数，将查询所有记录负荷信息的SGW。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SGWNAME|SGW主机名|参数可选性:任选参数；参数类型:字符型。|发送负荷信息的SGW主机名。
SN|负荷信息序列号|参数可选性:任选参数；参数类型:整数。|负荷信息的序列号，可用于标识最新的过负荷信息。
LOADMETRIC|SGW负荷值|参数可选性:任选参数；参数类型:整数。|SGW的网元级负荷值。






[](None)命令举例 


查询MME接收到的不同SGW返回的动态负荷信息。 


SHOW SGW LOAD INFO; 


`

命令 (No.26): SHOW SGW LOAD INFO

SGW主机名                                                负荷信息序列号   SGW负荷值
-----------------------------------------------------------------------------------
sgw.auto1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org   122              61
sgw.auto3.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org   322              71
-----------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.047 秒）。
 ` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询PGW负荷信息(SHOW PGW LOAD INFO) 
### 查询PGW负荷信息(SHOW PGW LOAD INFO) 


[](None)命令功能 


用于查询MME接收到的不同PGW返回的网元级或APN级的动态负荷信息。负荷信息包括PGW主机名和APN NI、负荷信息序列号、负荷值。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|用于设置需要查询负荷信息的PGW主机名。如果不设置该参数，将查询所有记录负荷信息的PGW。
APNNI|APN NI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|用于设置需要查询指定PGW的APN级负荷信息的APN NI。如果仅设置PGW Name不设置该参数，将查询PGW的所有节点级和APN级负荷信息。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW主机名|参数可选性:任选参数；参数类型:字符型。|发送负荷信息的PGW主机名。
APNNI|APNNI|参数可选性:任选参数；参数类型:字符型。|如果有该字段，表示该负荷信息针对该APN的APN级负荷信息。
SN|负荷信息序列号|参数可选性:任选参数；参数类型:整数。|负荷信息的序列号，可用于标识最新的过负荷信息。
LOADMETRIC|PGW网元级或APN级负荷值|参数可选性:任选参数；参数类型:整数。|PGW的网元级或者APN级的负荷值。
APNRC|APN的相对容量|参数可选性:任选参数；参数类型:整数。|PGW为该APN提供的相对容量。






[](None)命令举例 


查询MME接收到的不同PGW返回的动态负荷信息。 


SHOW PGW LOAD INFO; 


`

命令 (No.27): SHOW PGW LOAD INFO

PGW主机名                                                APNNI     负荷信息序列号   PGW网元级或APN级负荷值   APN的相对容量
--------------------------------------------------------------------------------------------------------------------------
pgw.auto1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org             2                33                       100
pgw.auto1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org   zte.com   3                33                       2
--------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.047 秒）。
 ` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGW过负荷信息(SHOW SGW OVERLOAD INFO) 
### 查询SGW过负荷信息(SHOW SGW OVERLOAD INFO) 


[](None)命令功能 


用于查询MME接收到的不同SGW返回的过负荷信息。过负荷信息包括SGW主机名、过负荷信息序列号、有效时间和缩减值。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SGWNAME|SGW主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|用于设置需要查询过负荷信息的SGW主机名；如果不设置该参数，将查询所有记录有过负荷信息的SGW。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SGWNAME|SGW主机名|参数可选性:任选参数；参数类型:字符型。|发送过负荷信息的SGW主机名。
SN|过负荷信息序列号|参数可选性:任选参数；参数类型:整数。|过负荷信息的序列号，可用于标识最新的过负荷信息。
PV|过负荷有效时间|参数可选性:任选参数；参数类型:字符型。|过负荷信息的有效时间，超过有效时间信息失效。
REDUCTION|过负荷信息缩减值|参数可选性:任选参数；参数类型:整数。|发生过负荷后，SGW要求MME对后继业务的缩减百分比。
INFORMTIME|通知时间|参数可选性:任选参数；参数类型:字符型。|接收到该过负荷信息的时间。






[](None)命令举例 


查询MME接收到的不同SGW返回的过负荷信息。 


SHOW SGW OVERLOAD INFO; 


`

命令 (No.1): SHOW SGW OVERLOAD INFO

SGW主机名                                                过负荷信息序列号   过负荷有效时间   过负荷信息缩减值   通知时间
------------------------------------------------------------------------------------------------------------------------
sgw.auto1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org   343                1(h)             22                 2000-1-2 19:02:08
------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.156 秒）。
 ` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询PGW过负荷信息(SHOW PGW OVERLOAD INFO) 
### 查询PGW过负荷信息(SHOW PGW OVERLOAD INFO) 


[](None)命令功能 


用于查询MME接收到的不同PGW返回的网元级或APN级的动态负荷信息。 


过负荷信息包括PGW主机名和APN NI、过负荷信息序列号、有效时间和缩减值。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|用于设置需要查询过负荷信息的PGW主机名。如果不设置该参数，将查询所有记录有过负荷信息的PGW。
APNNI|APN NI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|用于设置需要查询指定PGW的APN级过负荷信息的APN NI。如果仅设置PGW Name不设置该参数，将查询PGW的所有节点级和APN级过负荷信息。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW主机名|参数可选性:任选参数；参数类型:字符型。|发送过负荷信息的PGW主机名。
APNNI|APNNI|参数可选性:任选参数；参数类型:字符型。|如果有该字段，表示该过负荷信息针对该APN的APN级过负荷信息。
SN|过负荷信息序列号|参数可选性:任选参数；参数类型:整数。|过负荷信息的序列号，可用于标识最新的过负荷信息。
PV|过负荷有效时间|参数可选性:任选参数；参数类型:字符型。|过负荷信息的有效时间，超过有效时间信息失效。
REDUCTION|过负荷信息缩减值|参数可选性:任选参数；参数类型:整数。|发生过负荷后，PGW要求MME对后继业务的缩减百分比。
INFORMTIME|通知时间|参数可选性:任选参数；参数类型:字符型。|接收到该过负荷信息的时间。






[](None)命令举例 


查询MME接收到的不同PGW返回的过负荷信息。 


SHOW PGW OVERLOAD INFO; 


`

命令 (No.2): SHOW PGW OVERLOAD INFO

PGW主机名                                                APNNI            过负荷信息序列号   过负荷有效时间   过负荷信息缩减值   通知时间
-----------------------------------------------------------------------------------------------------------------------------------------
pgw.auto1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org   0123             25                 10(h)            20                 2000-1-2 19:39:09
pgw.auto1.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org   pc2.auto.local   25                 10(h)            20                 2000-1-2 19:41:45
-----------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.063 秒）。
 ` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGSN自动过负荷信息(SHOW AUTO CNG INFO) 
### 查询SGSN自动过负荷信息(SHOW AUTO CNG INFO) 


[](None)命令功能 


该命令用于查询SGSN自动过负荷信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65534。|CMP实例号。
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
HLRREQNUM|发出到HLR请求数|参数可选性:任选参数；参数类型:字符型。|发出到HLR请求数。
HLRREVNUM|由HLR接收的响应数|参数可选性:任选参数；参数类型:字符型。|由HLR接收的响应数。
CTLNUM|控制的业务数|参数可选性:任选参数；参数类型:字符型。|控制的业务数。






[](None)命令举例 


查询SGSN自动过负荷信息。 


SHOW AUTO CNG INFO:SC=1 


`

命令 (No.1): SHOW AUTO CNG INFO:SC=1

发出到HLR请求数  由HLR接收的响应数  控制的业务数 
------------------------------------------------
0                0                0 
0                0                0
0                0                0
0                0                0
0                0                0
0                0                0
0                0                0
0                0                0
0                0                0
0                0                0
------------------------------------------------
记录数 10

命令执行成功（耗时 0.063 秒）。
 ` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME负荷信息(SHOW MMES1LOAD) 
### 查询MME负荷信息(SHOW MMES1LOAD) 


[](None)命令功能 


该命令用于查询MME负荷情况，该负荷情况是MME向eNodeB发送overload start/stop的依据。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|查询类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|查询类型。
SC|CMP实例|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|CMP实例。
INTERPROCNO|内部进程号|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|操作结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|操作结果。
CPURATIO|CPU负荷(%)|参数可选性:任选参数；参数类型:整数。|CPU负荷(%)。
NASSIGRATE|NAS信令速率(每秒个)|参数可选性:任选参数；参数类型:整数。|NAS信令速率(每秒个。)






[](None)命令举例 


查询MME负荷情况。 


SHOW MMES1LOAD:TYPE="OVERALL" 


`

(No.93) : SHOW MMES1LOAD:TYPE="OVERALL"
-----------------NFS_MMESGSN_0----------------
操作结果
成功

CPU负荷(%) NAS信令速率(每秒个)
6   0

记录数 1

命令执行成功（耗时 0.024 秒）。
` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME自动过负荷信息(SHOW MME AUTO CNG INFO) 
### 查询MME自动过负荷信息(SHOW MME AUTO CNG INFO) 


[](None)命令功能 


该命令用于查询MME自动过负荷信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65534。|CMP实例号。
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
TYPE|局向类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:HSS&GW&MSCVLR。|该参数用于设置局向类型，根据此局向类型选择性的显示统一ALC（HSS/GW/MSC）控制详细信息。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
HLRSTARTTIME|周期开始时间|参数可选性:任选参数；参数类型:字符型。|该参数用于表示在流控期间，每个控制周期的开始时间。
HLRJUDGEPERIOD|评判周期|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前HSS局向自动负荷控制的评判周期。
HLRPERIODSERVNUM|周期内初始业务请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内， HSS局向接收到的初始附着、Inter TAU、跨RAT TAU业务请求数。
HLRCTLNUM|HSS拥塞控制请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，由于HSS局向拥塞控制的初始附着、Inter TAU、跨RAT TAU业务请求数。
HLRPERIODPASSRATE|周期通过速率|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内统一ALC HSS局向允许通过的业务速率（次/秒)。
HLRREQNUM|发出到HSS请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，MME向HSS局向发送的ALR\ULR\NOR请求次数。
HLRRESNUM|由HSS接收的成功响应数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，MME收到HSS局向成功响应次数。
HLRFAILRESNUM|接收HSS失败响应数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内， MME收到HSS失败响应次数。
GWSTARTTIME|周期开始时间|参数可选性:任选参数；参数类型:字符型。|该参数用于表示在流控期间，每个控制周期的开始时间。
GWJUDGEPERIOD|评判周期|参数可选性:任选参数；参数类型:字符型。|该参数用于表示GW局向自动负荷控制的评判周期。
GWPERIODSERVNUM|周期内初始业务请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，对应统一ALC HSS局向接收到的初始附着、Inter TAU、跨RAT TAU业务请求数。
GWCTLNUM|GW拥塞控制请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内由于GW局向拥塞控制的初始附着、Inter TAU、跨RAT TAU业务请求数。
GWPERIODPASSRATE|周期通过速率|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内统一ALC HSS局向允许通过的业务速率（次/秒)。
GWREQNUM|发出到GW请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，向GW局向发送的会话创建和承载修改请求次数。
GWRESNUM|由GW接收的成功响应数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，MME收到GW局向的成功响应次数
GWFAILRESNUM|由GW接收的失败响应数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内， MME收到GW失败响应次数。
MSCSTARTTIME|周期开始时间|参数可选性:任选参数；参数类型:字符型。|该参数用于表示在流控期间，每个控制周期的开始时间。
MSCJUDGEPERIOD|评判周期|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前统一ALC HSS局向自动负荷控制的评判周期。
MSCPERIODSERVNUM|周期内初始业务请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，对应统一ALC HSS局向接收到的初始附着、Inter TAU、跨RAT TAU业务请求数。
MSCCTLNUM|MSC/VLR拥塞控制请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内MME由于MSC/VLR局向拥塞而控制的初始附着、Inter TAU、跨RAT TAU业务请求数。MME系统运行时，会实时检测MSC/VLR局向是否拥塞。如果MSC/VLR局向发生拥塞，则MME控制初始附着、Inter TAU、跨RAT TAU业务请求数，从而降低MSC/VLR局向的负荷。
MSCPERIODPASSRATE|周期通过速率|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内统一ALC HSS局向允许通过的业务速率（次/秒)。
MSCREQNUM|发出到MSC请求数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，MSC/VLR局向发送的位置更新请求次数。在收到MSC/VLR响应和超时时，对该参数进行统计。
MSCRESNUM|由MSC接收的成功响应数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内，MME收到MSC/VLR局向成功响应次数。
MSCFAILRESNUM|由MSC接收的失败响应数|参数可选性:任选参数；参数类型:字符型。|该参数用于表示当前控制周期内， MME收到MSC/VLR失败响应次数。






[](None)命令举例 


查询MME自动过负荷信息。 


SHOW MME AUTO CNG INFO:SC=2 


`

命令 (No.1): SHOW MME AUTO CNG INFO:SC=2

发出到HHS请求数  由HSS接收的响应数  控制的业务数 
------------------------------------------------
0                0                  0 
0                0                  0
0                0                  0
0                0                  0
0                0                  0
0                0                  0
0                0                  0
0                0                  0
0                0                  0
0                0                  0
------------------------------------------------
记录数 10

命令执行成功（耗时 0.063 秒）。
 ` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询S6a ALC局向负荷控制信息(SHOW S6A ALCOFC CNG INFO) 
### 查询S6a ALC局向负荷控制信息(SHOW S6A ALCOFC CNG INFO) 


[](None)命令功能 


该命令用于查询S6a ALC局向负荷控制信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SC|CMP实例号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65534。|CMP实例号
INTERPROCNO|内部进程号|参数可选性:必选参数；参数类型:整数；参数范围为:0~16。|该参数为CMP内部业务进程编号，从1开始连续编号。CMP内部进程个数可以通过SHOW CMP PROCNUM命令查询。
HSSOFCIDX|HSS局向索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|HSS局向索引






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
OFCIDX|局向索引|参数可选性:任选参数；参数类型:整数。|该参数用于表示S6a ALC局向的索引。
OFCNAME|局向名称|参数可选性:任选参数；参数类型:字符型。|该参数用于表示S6a ALC局向的名称。
STARTTIME|周期开始时间|参数可选性:任选参数；参数类型:整数。|该参数用于表示控制周期的开始时间。粒度为5秒。
JUDGEPERIOD|评判周期|参数可选性:任选参数；参数类型:整数。|该参数用于表示当前S6a ALC局向自动负荷控制的评判周期。
DWPERIODSERVNUM|周期内初始业务请求数|参数可选性:任选参数；参数类型:整数。|该参数用于表示当前控制周期内，对应S6a ALC局向接收到的初始附着、Inter TAU、跨RAT TAU业务请求数。
DWHSSCTLNUM|HSS拥塞控制请求数|参数可选性:任选参数；参数类型:整数。|该参数用于表示当前控制周期内由于S6a ALC局向拥塞而控制的初始附着、Inter TAU、跨RAT TAU业务请求数。
PERIODPASSRATE|周期通过速率（次/秒）|参数可选性:任选参数；参数类型:整数。|该参数用于表示当前控制周期内S6a ALC局向允许通过的业务速率（次/秒)。
DWHSSREQNUM|发出到HSS请求数|参数可选性:任选参数；参数类型:整数。|该参数用于表示当前控制周期内，向S6a ALC局向发送的ALR、ULR、NOR请求次数。在收到HSS响应和超时时统计。
DWHSSRESNUM|由HSS接收的响应数|参数可选性:任选参数；参数类型:整数。|该参数用于表示当前控制周期内，对应S6a ALC局向收到HSS响应的ALA、ULA、NOA次数。在收到HSS响应时统计。
DWHSSFAILRESNUM|接收HSS失败响应数|参数可选性:任选参数；参数类型:整数。|该参数用于表示当前控制周期内， MME收到HSS失败响应次数。






[](None)命令举例 


查询S6a ALC局向负荷控制信息。 


SHOW S6A ALCOFC CNG INFO:SC=1,HSSOFCIDX=1 


`

命令 (No.1): SHOW S6A ALCOFC CNG INFO:SC=1,HSSOFCIDX=1

局向索引 局向名称                           周期开始时间        评判周期 周期内初始业务请求数 周期通过速率（次/秒） 发出到HSS请求数 由HSS接收的响应数 HSS拥塞控制请求数 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:56 25       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:51 24       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:46 24       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:41 24       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:36 23       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:31 23       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:26 23       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:21 22       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:16 22       0                    Uncontrolled          0               0                 0                 
1        2021.1.22.mnc321.mcc460.zte.com.cn 2021-01-26 18:54:11 22       0                    Uncontrolled          0               0                 0
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 10

命令执行成功（耗时 0.063 秒）。
 ` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### MME自动过负荷日志上报(START MME AUTO CNG LOGRPT) 
### MME自动过负荷日志上报(START MME AUTO CNG LOGRPT) 


[](None)命令功能 


该命令用于启动MME自动过负荷日志上报。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LOGTIME|日志上报时长（h）|参数可选性:任选参数；参数类型:整数。|此参数用于设置统一ALC、分局向ALC动态负荷控制日志上报的时长。系统收到动态命令时开始上报日志信息，超过设置的时长后，停止上报。存在动态负荷控制时和不存在动态负荷控制时都上报。






[](None)命令举例 


MME自动过负荷日志上报。 


START MME AUTO CNG LOGRPT:LOGTIME=2 


`
命令 (No.1): START MME AUTO CNG LOGRPT:LOGTIME=2

操作结果  
----------
成功     
----------
记录数：1

执行成功开始时间:2021-04-15 14:39:20 耗时: 2.075秒
` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 停止MME自动过负荷日志上报(STOP MME AUTO CNG LOGRPT) 
### 停止MME自动过负荷日志上报(STOP MME AUTO CNG LOGRPT) 


[](None)命令功能 


该命令用于停止MME自动过负荷日志上报。 




[](None)注意事项 

无。


[](None)命令举例 


停止MME自动过负荷日志上报。 


STOP MME AUTO CNG LOGRPT 


`
命令 (No.1): STOP MME AUTO CNG LOGRPT

操作结果  
----------
成功     
----------
记录数：1

执行成功开始时间:2021-04-15 14:39:20 耗时: 2.075秒
` 








父主题： [网元过负荷控制](../../zh-CN/tree/N_13084052.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## ACL规则管理 
## ACL规则管理 


[](None)背景知识 

            
            ACL规则包括IP地址、端口、VRF ID以及协议类型等关键信息。接口板基于ACL规则，将收到的消息分发给正确的处理单元。当ACL规则异常时，接口板无法将消息投递给正确处理单元，导致业务无法正常进行。
        


[](None)功能描述 

            
            当发现接口板ACL规则异常时，通过该节点下的动态命令，恢复ACL规则。
        


[](None)相关主题 



 

刷新GTPC ACL规则(SET GTPCACL)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 刷新GTPC ACL规则(SET GTPCACL) 
### 刷新GTPC ACL规则(SET GTPCACL) 


[](None)命令功能 

该命令用于刷新MME/SGSN的GTPC ACL规则，包括MME GTPC信令面地址、SGSN GTPC信令面地址以及MME Sv接口地址等GTPC地址的ACL规则。


[](None)注意事项 

无。


[](None)命令举例 


刷新GTPC ACL规则。 


SET GTPCACL 








父主题： [ACL规则管理](../../zh-CN/tree/N_13084054.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## EMS PLUS状态管理 
## EMS PLUS状态管理 


[](None)背景知识 


MME/SGSN和EMS+服务器对接，将业务日志发送给EMS+服务器。MME/SGSN会和EMS+服务器进行链路状态检活，维护MME/SGSN和EMS+服务器之间的链路状态。 




[](None)功能描述 


该节点用于查询MME/SGSN和EMS+服务器之间的链路状态，包括与主用EMS+服务器和备用EMS+服务器之间的链路状态。 




[](None)相关主题 



 

查询EMS PLUS链路状态(SHOW EMSPLUS LINK STATUS)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询EMS PLUS链路状态(SHOW EMSPLUS LINK STATUS) 
### 查询EMS PLUS链路状态(SHOW EMSPLUS LINK STATUS) 


[](None)命令功能 


该命令用于查询MME/SGSN和EMS+服务器之间的链路状态。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
LINK|链路|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示链路是主用或备用。
REMOTEIP|远端IP|参数可选性:任选参数；参数类型:字符型。|远端EMS+服务器的IP地址。
REMOTEPORT|远端端口号|参数可选性:任选参数；参数类型:整数。|远端EMS+服务器的端口号。
LOCALIP|本端IP|参数可选性:任选参数；参数类型:字符型。|本端与EMS+服务器对接的IP地址。
LOCALPORT|本端端口号|参数可选性:任选参数；参数类型:整数。|本端与EMS+服务器对接的端口号。
VRF|VRF ID|参数可选性:任选参数；参数类型:整数。|本端与EMS+服务器对接的地址关联的VRF。
STATUS|链路状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|主用或备用链路的状态。






[](None)命令举例 


查询EMS PLUS链路状态。 


SHOW EMSPLUS LINK STATUS; 


`

命令 (No.1): SHOW EMSPLUS LINK STATUS:
-----------------NFS_MMESGSN_0----------------
链路           远端IP                                        远端端口号  本端IP                                        本端端口号 VRF ID 链路状态   
--------------------------------------------------------------------------------------------------------------------------------------------------------
主用链路       IPv6: 0000:0000:0000:0000:0000:0000:0000:0000 0           IPv6: 0000:0000:0000:0000:0000:0000:0000:0000 16000      2      无效     
备用链路       IPv6: 0000:0000:0000:0000:0000:0000:0000:0000 0           IPv6: 0000:0000:0000:0000:0000:0000:0000:0000 16000      2      无效     
--------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.062 秒）。
` 








父主题： [EMS PLUS状态管理](../../zh-CN/tree/N_13084055.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


调测信息采集 调测信息采集 

[](None)背景知识 


在系统调试过程中，需要采集系统的运行信息，可提供给运维人员进行分析，达到监测系统是否正常的目的。 




[](None)功能描述 


使用本功能可以进行系统调测信息采集。 




[](None)相关主题 



 

查询本地数据库表(SHOW MMESGSN LOCAL DATABASE TABLE)
 

 

查询UDSF数据库表(SHOW MMESGSN UDSF DATABASE TABLE)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询本地数据库表(SHOW MMESGSN LOCAL DATABASE TABLE) 
### 查询本地数据库表(SHOW MMESGSN LOCAL DATABASE TABLE) 


[](None)命令功能 


该命令用于查询MME/SGSN本地数据库表情况。 




[](None)注意事项 

无


[](None)命令举例 


查询MME/SGSN本地数据库表情况。 


`

(No.1) : SHOW MMESGSN LOCAL DATABASE TABLE:
-----------------NFS_MMESGSN_0----------------
100%

输出文件路径
---------------
当前命令执行的结果被另存为文件，请点击这个URL下载：
342747db8f724f22be61a01bb07dcf4c_SHOW MMESGSN LOCAL DATABASE TABLE_1_2022-03-07 15-25-44.csv
---------------
开始时间:2022-03-07 15:25:45 耗时: 0.972秒 

` 








父主题： [调测信息采集](../../zh-CN/tree/N_13084056.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询UDSF数据库表(SHOW MMESGSN UDSF DATABASE TABLE) 
### 查询UDSF数据库表(SHOW MMESGSN UDSF DATABASE TABLE) 


[](None)命令功能 


该命令用于查询UDSF数据库表情况。 




[](None)注意事项 

无


[](None)命令举例 


查询UDSF数据库表情况。 


`

(No.2) : SHOW MMESGSN UDSF DATABASE TABLE:
-----------------NFS_MMESGSN_0----------------
输出文件路径
---------------
当前命令执行的结果被另存为文件，请点击这个URL下载：
f410371b486b466084a39bbab3854522_SHOW MMESGSN UDSF DATABASE TABLE_1_2022-03-07 15-26-19.csv
---------------

执行成功开始时间:2022-03-07 15:26:21 耗时: 0.454 秒
` 








父主题： [调测信息采集](../../zh-CN/tree/N_13084056.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 多进程查询 
## 多进程查询 


[](None)相关主题 



 

查询每CMP SC内业务进程个数(SHOW CMP PROCNUM)
 

 








父主题： [动态管理](../../zh-CN/tree/N_126033_operation_cm_mml_umacV4_dynamic.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询每CMP SC内业务进程个数(SHOW CMP PROCNUM) 
### 查询每CMP SC内业务进程个数(SHOW CMP PROCNUM) 


[](None)命令功能 


该命令用来查询每个CMP SC内部业务进程个数。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RESULT|查询结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|
PROCNUM|每个SC内部进程个数|参数可选性:任选参数；参数类型:整数。|






[](None)命令举例 


查询MME负荷情况。 


SHOW MMES1LOAD:TYPE="OVERALL" 


`

(No.93) : SHOW MMES1LOAD:TYPE="OVERALL"
-----------------NFS_MMESGSN_0----------------
操作结果
成功

CPU负荷(%) NAS信令速率(每秒个)
6   0

记录数 1

命令执行成功（耗时 0.024 秒）。
` 








父主题： [多进程查询](../../zh-CN/tree/N_13084057.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 大数据查询 
# 大数据查询 


[](None)背景知识 


在某些情况下，维护人员希望了解本网元相关的无线网元的相关信息或者本网元所有的用户相关信息。大数据查询功能针对此需求提供相应的查询命令。 




[](None)功能描述 


目前，ZXUN-uMAC产品支持的大数据查询功能包括：无线信息查询和用户信息查询。对于SGSN 网元，支持无线信息查询和用户信息查询。对于MME网元，仅支持无线信息查询。 


此类查询结果记录数较多，尤其是用户信息，一般超过50万，对于用户信息，系统直接将查询结果存为excel或者txt文件，并不是是直接显示。对于无线信息，如果查询出的记录较少，不大于2000条，则直接显示结果，查询结果大于2000条，则系统将查询结果保持为excel或者txt文件。 




[](None)相关主题 



 

导出用户信息
 

 

无线信息查询
 

 












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 导出用户信息 
## 导出用户信息 


[](None)背景知识 


在某些情况下，维护人员希望了解本网元相关的无线网元的相关信息或者本网元所有的用户相关信息。大数据查询功能针对此需求提供相应的查询命令。 




[](None)功能描述 


导出用户信息功能目前仅适用于SGSN网元，用于维护人员批量查询SGSN网元中2G/3G用户信息的需求，包括所有2G/3G用户的IMSI /MSISDN /RAI /CI等，查询结果保存为TXT或CSV格式的文件。 




[](None)相关主题 



 

导出用户信息(EXPORT USERINFO)
 

 

导出用户简要信息(EXPORT BRIEFUSERINFO)
 

 

停止导出用户信息(STOP USERINFO)
 

 








父主题： [大数据查询](../../zh-CN/tree/N_126050_operation_cm_mml_umacV4_bigdata.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 导出用户信息(EXPORT USERINFO) 
### 导出用户信息(EXPORT USERINFO) 


[](None)命令功能 


该命令用于查询SGSN/MME网元中所有2G/3G/4G用户的信息。查询结果包括：SCLogicNo、PLMN、IMSI、MSISDN、RAI、CI/SAC/TAC、TLLI/PTMSI/GUTI、用户状态、激活的PDP/承载数量、接入类型和IMEI。 


执行该命令后，系统将查询结果保存为excel或者txt文件。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
FORMAT|输出格式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:TXT。|该参数用于指定用户信息导出文件的格式，包括TXT和CSV两种输出格式。选择TXT输出时，仅输出一个文件；选择CSV格式输出时，按SC 实例产生文件。
FLAG|是否继续上次导出|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指示如果上一次导出过程被停止，是否选择继续导出。
USERTYPE|查询用户类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:2G&3G&4G。|该参数用于指定导出用户的接入类型，包括2G、3G、4G三种基本接入类型。支持单个或者组合用户接入类型选择。






[](None)命令举例 


导出用户信息。 


EXPORT USERINFO:USERTYPE=2G&3G&4G; 


`

命令 (No.8): EXPORT USERINFO:USERTYPE=2G&3G&4G;

操作结果 
---------
成功 
---------

文件输出URL
---------------
sftp://ems:*******@127.0.0.1:29029/Nfdata/combo23/vru_mmesgsn_dba/combo23/AMM/CMDBA/userinfo/20200109160509.zip
---------------

命令执行成功（耗时 elapsed 1.582 秒）。

` 








父主题： [导出用户信息](../../zh-CN/tree/N_130840038.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 导出用户简要信息(EXPORT BRIEFUSERINFO) 
### 导出用户简要信息(EXPORT BRIEFUSERINFO) 


[](None)命令功能 


该命令用于查询网元中所有2G/3G/4G用户的简要信息。 


执行该命令后，系统将查询结果保存为excel或者txt文件。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
FORMAT|输出格式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:TXT。|该参数用于指定用户信息导出文件的格式，包括TXT和CSV两种输出格式。选择TXT输出时，仅输出一个文件；选择CSV格式输出时，按模块产生文件。
FLAG|是否继续上次导出|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指示如果上一次导出过程被停止，是否选择继续导出。
USERTYPE|查询用户类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:2G&3G&4G。|该参数用于指定导出用户的接入类型，包括2G、3G、4G三种基本接入类型。支持单个或者组合用户接入类型选择。






[](None)命令举例 


导出用户简要信息。 


EXPORT BRIEFUSERINFO 


`

命令 (No.8): EXPORT BRIEFUSERINFO:USERTYPE="2G"&"3G"&"4G";

操作结果 
---------
成功 
---------
记录数 1

输出文件路径
---------------
当前命令执行的结果被另存为文件，请点击这个URL下载。
http://193.168.12.103:2323/combo_mmegngp_sgsn_105/server/tmp/ftp/userdata/20150929162751.zip
---------------
记录数 1

命令执行成功（耗时 elapsed 1.582 秒）。
` 








父主题： [导出用户信息](../../zh-CN/tree/N_130840038.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 停止导出用户信息(STOP USERINFO) 
### 停止导出用户信息(STOP USERINFO) 


[](None)命令功能 


该命令用于停止导出用户信息。当[EXPORT USERINFO](1263164.html)正在执行的时候，可以使用该命令，停止导出。




[](None)注意事项 


无 




[](None)命令举例 


停止导出用户信息。 


STOP USERINFO; 


`

命令 (No.4): STOP USERINFO;

记录数 0

命令执行成功（耗时 0.041 秒）。

` 








父主题： [导出用户信息](../../zh-CN/tree/N_130840038.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 无线信息查询 
## 无线信息查询 


[](None)背景知识 


在某些情况下，维护人员希望了解本网元相关的无线网元的相关信息或者本网元所有的用户相关信息。大数据查询功能针对此需求提供相应的查询命令。 




[](None)功能描述 


无线信息查询功能用于维护人员批量查询MME/SGSN关联的无线网元的无线相关信息，例如：2G BSC/3G RNC支持的路由区信息，4G eNodeB支持的跟踪区信息等。 


无线信息查询支持以下三种查询： 



 
查询BSC网元的无线信息。 

 
查询RNC网元的无线信息。 

 
查询eNodeB网元的无线信息。 

 




[](None)相关主题 



 

查询NSE信息(SHOW NSE INFO)
 

 

查询RNC信息(SHOW RNCALL INFO)
 

 

查询eNodeB信息(SHOW ENODEBALL INFO)
 

 

查询eNB邻接关系信息(SHOW ENB NEIGHBOR INFO)
 

 








父主题： [大数据查询](../../zh-CN/tree/N_126050_operation_cm_mml_umacV4_bigdata.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询NSE信息(SHOW NSE INFO) 
### 查询NSE信息(SHOW NSE INFO) 


[](None)命令功能 


该命令用于查询SGSN网元管理的NSE（BSC）关联的无线信息。查询结果包括：BVC信息、小区信息，路由区信息等。 




[](None)注意事项 


该命令仅适用于SGSN和Combo MME/GnGp SGSN网元。 




[](None)命令举例 


查询NSE信息。 


SHOW NSE INFO; 


`

(No.1) : SHOW NSE INFO:
-----------------NFS_MMESGSN_0----------------
命令结果的文件路径
---------------
请点击下面URL获取命令结果
a2ffb56ea0ec470db9c43d1ef15a908b_SHOW NSE INFO_1_2020-03-24 15-40-02.csv
---------------

` 








父主题： [无线信息查询](../../zh-CN/tree/N_130840039.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询RNC信息(SHOW RNCALL INFO) 
### 查询RNC信息(SHOW RNCALL INFO) 


[](None)命令功能 


该命令用于查询SGSN网元管理的RNC网元关联的无线信息。查询结果包括：RNC局向号、路由区信息等。 




[](None)注意事项 


该命令仅适用于SGSN和Combo MME/GnGp SGSN网元。 




[](None)命令举例 


查询RNC无线信息。 


SHOW RNCALL INFO; 


`

(No.2) : SHOW RNCALL INFO:
-----------------NFS_MMESGSN_0----------------
命令结果的文件路径
---------------
请点击下面URL获取命令结果
a2ffb56ea0ec470db9c43d1ef15a908b_SHOW RNCALL INFO_1_2020-03-24 15-41-33.csv
---------------

` 








父主题： [无线信息查询](../../zh-CN/tree/N_130840039.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询eNodeB信息(SHOW ENODEBALL INFO) 
### 查询eNodeB信息(SHOW ENODEBALL INFO) 


[](None)命令功能 


该命令用于查询MME网元管理的eNodeB网元关联的无线信息。查询结果包括：eNodeB局向号、eNodeB地址、跟踪区信息等。 




[](None)注意事项 


该命令仅适用于MME和Combo MME/GnGp SGSN网元。 




[](None)命令举例 


查询eNodeB信息。 


SHOW ENODEBALL INFO; 


`

(No.3) : SHOW ENODEBALL INFO:
-----------------NFS_MMESGSN_0----------------
命令结果的文件路径
---------------
请点击下面URL获取命令结果
a2ffb56ea0ec470db9c43d1ef15a908b_SHOW ENODEBALL INFO_1_2020-03-24 15-42-10.csv
---------------

` 








父主题： [无线信息查询](../../zh-CN/tree/N_130840039.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询eNB邻接关系信息(SHOW ENB NEIGHBOR INFO) 
### 查询eNB邻接关系信息(SHOW ENB NEIGHBOR INFO) 


[](None)命令功能 


该命令用于在MME上查询全部eNB的邻接eNB信息。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|中心基站移动国家码|参数可选性:任选参数；参数类型:字符型。|本参数用于设置中心基站的Global eNodeB ID的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。
MNC|中心基站移动网络码|参数可选性:任选参数；参数类型:字符型。|本参数用于设置中心基站的Global eNodeB ID的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中基于MCC唯一标识一个运营商网络信息。
BITLEN|eNB ID长度|参数可选性:任选参数；参数类型:整数。|参数作用：本参数用于显示中心eNB的eNB ID长度，取值范围为20BIT位。修改影响：无。数据来源：全网规划。默认值：无。配置原则：全网规划。
ENBID|中心eNB标识|参数可选性:任选参数；参数类型:整数。|本参数用于设置中心基站的eNB ID，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个eNB，由运营商在PLMN内统一规划，以16进制数字编码。
NEIMCC|邻接基站移动国家码|参数可选性:任选参数；参数类型:字符型。|本参数用于设置邻接基站的Global eNodeB ID的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。
NEIMNC|邻接基站移动网号|参数可选性:任选参数；参数类型:字符型。|本参数用于设置邻接基站的Global eNodeB ID的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中基于MCC唯一标识一个运营商网络信息。
NEIENBIDBITLEN|邻接eNB ID长度|参数可选性:任选参数；参数类型:整数。|参数作用：本参数用于显示邻接eNB的eNB ID长度，取值范围为20BIT位。修改影响：无。数据来源：全网规划。默认值：无。配置原则：全网规划。
NEIENBID|邻接eNB标识|参数可选性:任选参数；参数类型:字符型。|本参数用于设置邻接基站的eNB ID，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个eNB，由运营商在PLMN内统一规划，以16进制数字编码。






[](None)命令举例 


查询所有eNB邻接关系信息。 


SHOW ENB NEIGHBOR INFO; 


`

(No.3) : SHOW ENB NEIGHBOR INFO:
-----------------NFS_MMESGSN_0----------------
命令结果的文件路径
---------------
请点击下面URL获取命令结果
a2ffb56ea0ec470db9c43d1ef15a908b_SHOW ENB NEIGHBOR INFO_1_2020-03-24 15-42-10.csv
---------------

` 








父主题： [无线信息查询](../../zh-CN/tree/N_130840039.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 跟踪管理 
# 跟踪管理 


[](None)背景知识 


为了满足运营商支出于特定的目的，出于对特定目标对象的行为分析，AMF需要支持跟踪相关的信令消息。 




[](None)功能描述 


跟踪管理提供了根据配置跟踪特定用户的信令消息等功能，包括TRACE、管理MDT和信令MDT等功能。 




[](None)相关主题 



 

用户设备跟踪
 

 












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 用户设备跟踪 
## 用户设备跟踪 


[](None)背景知识 


出于特定的目的，出于对特定目标对象的行为分析，需要跟踪相关的信令消息 




[](None)功能描述 


跟踪管理提供了根据配置跟踪特定用户的信令消息等功能，包括TRACE、管理MDT和信令MDT等功能。 




[](None)相关主题 



 

激活用户设备跟踪任务(ACTIVATE TRACEJOB)
 

 

去激活用户设备跟踪任务(DEACTIVATE TRACEJOB)
 

 

查询用户设备跟踪任务(LIST TRACEJOB)
 

 

查询激活用户设备跟踪任务(LIST ACTIVATETRACEJOB)
 

 








父主题： [跟踪管理](../../zh-CN/tree/N_126070_operation_cm_mml_umacV4_trace.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 激活用户设备跟踪任务(ACTIVATE TRACEJOB) 
### 激活用户设备跟踪任务(ACTIVATE TRACEJOB) 


[](None)命令功能 

激活用户设备跟踪任务


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IOCINSTANCE|跟踪网元实例|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|该参数表示跟踪网元实例
LISTOFINTERFACES|跟踪接口|参数可选性:任选参数；参数类型:复合参数|该参数表示跟踪接口
NETYPE|网元类型|参数可选性:任选参数；参数类型:整数。|该参数表示网络类型
INTERFACE|接口|参数可选性:任选参数；参数类型:整数。|该参数表示接口
LISTOFNETYPES|跟踪网元类型|参数可选性:任选参数；参数类型:整数。|该参数表示跟踪网元类型
TRACEDEPTH|跟踪深度|参数可选性:必选参数；参数类型:整数。|该参数表示跟踪深度
TRACEREFERENCE|跟踪参考号|参数可选性:必选参数；参数类型:复合参数|该参数用于设置跟踪参考号
MCC|MCC|参数可选性:必选参数；参数类型:字符型；参数范围为:1~3个字符。|该参数表示跟踪参考号中的MCC
MNC|MNC|参数可选性:必选参数；参数类型:字符型；参数范围为:1~3个字符。|该参数表示跟踪参考号中的MNC
TRACEID|跟踪标识|参数可选性:必选参数；参数类型:整数。|该参数表示跟踪参考号中的ID
TRACETARGETTYPE|跟踪目标类型|参数可选性:必选参数；参数类型:整数。|该参数表示跟踪目标的号码类型，比如IMSI号码、ISDN号码等
TRACETARGETVALUES|跟踪目标值|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数表示被跟踪号码的信息
TRIGGERINGEVENT|跟踪触发事件|参数可选性:任选参数；参数类型:复合参数|该参数表示跟踪哪些事件
EVENT|事件|参数可选性:任选参数；参数类型:整数。|该参数表示跟踪事件
TRACECOLLECTIONENTITYADDRESS|TCE IP地址|参数可选性:任选参数；参数类型:地址|该参数表示TCE的IP地址
JOBTYPE|任务类型|参数可选性:任选参数；参数类型:整数。|该参数表示任务类型
AREASCOPETYPE|区域类型|参数可选性:任选参数；参数类型:整数。|该参数表示区域类型
AREASCOPEVALUE|区域值|参数可选性:任选参数；参数类型:字符型；参数范围为:0~20个字符。|该参数表示区域值
LISTOFMEASUREMENTS|测量列表|参数可选性:任选参数；参数类型:整数。|该参数表示测量列表信息
REPORTINGTRIGGER|上报触发器|参数可选性:任选参数；参数类型:整数。|该参数表示上报触发器
REPORTINTERVAL|上报间隔|参数可选性:任选参数；参数类型:整数。|该参数表示上报间隔
REPORTAMOUNT|上报次数|参数可选性:任选参数；参数类型:整数。|该参数表示上报次数
EVENTTHRESHOLD|事件阈值|参数可选性:任选参数；参数类型:复合参数|该参数表示事件阈值
LOGGINGINTERVAL|记录间隔|参数可选性:任选参数；参数类型:整数。|该参数表示记录间隔
LOGGINGDURATION|记录持续时间|参数可选性:任选参数；参数类型:整数。|该参数表示记录持续时间
ANONYMIZATIONOFMDTDATA|MDT数据匿名|参数可选性:任选参数；参数类型:整数。|该参数表示匿名MDT
MEASUREMENTPERIODLTE|LTE测量周期|参数可选性:任选参数；参数类型:整数。|该参数表示LTE测量周期
MEASUREMENTPERIODUMTS|UMTS测量周期|参数可选性:任选参数；参数类型:整数。|该参数表示UMTS测量周期
COLLECTIONPERIODRRMUMTS|UMTS RRM采集周期|参数可选性:任选参数；参数类型:整数。|该参数表示UMTS RRM采集周期
COLLECTIONPERIODRRMLTE|LTE RRM采集周期|参数可选性:任选参数；参数类型:整数。|该参数表示LTE RRM采集周期
POSITIONINGMETHOD|定位方法|参数可选性:任选参数；参数类型:整数。|该参数表示定位方法
MEASUREMENTQUANTITY|测量量|参数可选性:任选参数；参数类型:整数。|该参数表示测量量
PLMNTARGET|移动网络目标|参数可选性:任选参数；参数类型:字符型；参数范围为:0~10个字符。|该参数表示移动网络目标
OMCID|OMC ID|参数可选性:任选参数；参数类型:字符型；参数范围为:0~38个字符。|该参数表示OMC ID
MSCBSSTRACETYPE|MSC/BSS跟踪类型|参数可选性:任选参数；参数类型:复合参数|该参数表示MSC/BSS跟踪类型
MSCEVENT|MSC 触发事件|参数可选性:任选参数；参数类型:整数。|该参数表示MSC 触发事件
MSCRECORDTYPE|MSC记录类型|参数可选性:任选参数；参数类型:整数。|该参数表示MSC记录类型
BSSRECORDTYPE|BSS记录类型|参数可选性:任选参数；参数类型:整数。|该参数表示BSS记录类型
SGSNTRACETYPE|SGSN跟踪类型|参数可选性:任选参数；参数类型:复合参数|该参数表示SGSN跟踪类型
SGSNEVENT|SGSN触发事件|参数可选性:任选参数；参数类型:整数。|该参数表示SGSN触发事件
SGSNRECORDTYPE|SGSN记录类型|参数可选性:任选参数；参数类型:整数。|该参数表示SGSN记录类型
EVENTTHRESHOLDTYPE|事件阈值类型|参数可选性:任选参数；参数类型:整数。|该参数表示事件阈值类型
EVENTTHRESHOLDVALUE|事件阈值数值|参数可选性:任选参数；参数类型:整数；参数范围为:-32768~32767。|该参数表示事件阈值数值
SI|IMS业务级跟踪|参数可选性:任选参数；参数类型:字符型；参数范围为:0~2048个字符。|该参数表示IMS业务级跟踪
NETTYPE|网络类型|参数可选性:任选参数；参数类型:整数。默认值:1。|该参数表示网络类型
MBSFNAREALIST|MBSFN地区列表|参数可选性:任选参数；参数类型:复合参数|该参数表示MBSFN地区列表
MBSFNAREAID|MBSFN地区标识id|参数可选性:任选参数；参数类型:整数。|该参数表示MBSFN地区标识id
EARFCN|MBSFN地区载频|参数可选性:必选参数；参数类型:整数。|该参数表示MBSFN地区载频
PLMNLIST|PLMN列表|参数可选性:任选参数；参数类型:复合参数|该参数表示PLMN列表
MCC1|MCC|参数可选性:必选参数；参数类型:字符型；参数范围为:1~3个字符。|该参数表示MCC
MNC1|MNC|参数可选性:必选参数；参数类型:字符型；参数范围为:1~3个字符。|该参数表示MNC
M6PERIOD|M6上报间隔|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数表示M6上报周期
M7PERIOD|M7周期|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数表示M7周期
M6DELAYTHRESHOLD|M6时延门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数表示M6时延门限
WLANNAMELIST|WLAN名称列表|参数可选性:任选参数；参数类型:字符型；参数范围为:0~32个字符。|该参数表示WLAN名称列表
BTNAMELIST|BT名称列表|参数可选性:任选参数；参数类型:字符型；参数范围为:0~248个字符。|该参数表示设置BT名称列表
WLANCONFIG|WALN配置|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数表示设置WALN配置
BTCONFIG|BT配置|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数表示设置BT配置






[](None)命令举例 


激活用户设备跟踪任务 


ACTIVATE TRACEJOB:TRACEDEPTH=5,TRACEREFERENCE="321"-"111"-"1",TRACETARGETTYPE=3,TRACETARGETVALUES="1"; 








父主题： [用户设备跟踪](../../zh-CN/tree/N_12632021.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 去激活用户设备跟踪任务(DEACTIVATE TRACEJOB) 
### 去激活用户设备跟踪任务(DEACTIVATE TRACEJOB) 


[](None)命令功能 

去激活用户设备跟踪任务


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TRACEREFERENCE|跟踪参考号|参数可选性:必选参数；参数类型:复合参数|该参数用于设置跟踪参考号
MCC|MCC|参数可选性:必选参数；参数类型:字符型；参数范围为:1~3个字符。|该参数表示跟踪参考号中的MCC
MNC|MNC|参数可选性:必选参数；参数类型:字符型；参数范围为:1~3个字符。|该参数表示跟踪参考号中的MNC
TRACEID|跟踪标识|参数可选性:必选参数；参数类型:整数。|该参数表示跟踪参考号中的ID
TRACETARGETTYPE|跟踪目标类型|参数可选性:必选参数；参数类型:整数。|该参数表示跟踪目标的号码类型，比如IMSI号码、ISDN号码等
TRACETARGETVALUES|跟踪目标值|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数表示被跟踪号码的信息
NETTYPE|网络类型|参数可选性:任选参数；参数类型:整数。默认值:1。|该参数表示网络类型






[](None)命令举例 


去激活用户设备跟踪任务 


DEACTIVATE TRACEJOB:TRACEREFERENCE="321"-"111"-"1",TRACETARGETTYPE=1,TRACETARGETVALUES="1"; 








父主题： [用户设备跟踪](../../zh-CN/tree/N_12632021.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询用户设备跟踪任务(LIST TRACEJOB) 
### 查询用户设备跟踪任务(LIST TRACEJOB) 


[](None)命令功能 

查询用户设备跟踪任务


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TRACEREFERENCE|跟踪参考号|参数可选性:必选参数；参数类型:复合参数|该参数用于设置跟踪参考号
MCC|MCC|参数可选性:必选参数；参数类型:字符型；参数范围为:1~3个字符。|该参数表示跟踪参考号中的MCC
MNC|MNC|参数可选性:必选参数；参数类型:字符型；参数范围为:1~3个字符。|该参数表示跟踪参考号中的MNC
TRACEID|跟踪标识|参数可选性:必选参数；参数类型:整数。|该参数表示跟踪参考号中的ID
NETTYPE|网络类型|参数可选性:任选参数；参数类型:整数。默认值:1。|该参数表示网络类型






[](None)命令举例 


查询用户设备跟踪任务 


LIST TRACEJOB:TRACEREFERENCE="321"-"111"-"1"; 








父主题： [用户设备跟踪](../../zh-CN/tree/N_12632021.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询激活用户设备跟踪任务(LIST ACTIVATETRACEJOB) 
### 查询激活用户设备跟踪任务(LIST ACTIVATETRACEJOB) 


[](None)命令功能 

查询激活用户设备跟踪任务


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NETTYPE|网络类型|参数可选性:任选参数；参数类型:整数。默认值:1。|该参数表示网络类型






[](None)命令举例 


查询激活用户设备跟踪任务 


LIST ACTIVATETRACEJOB 








父主题： [用户设备跟踪](../../zh-CN/tree/N_12632021.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 直连接口管理 
# 直连接口管理 


[](None)背景知识 


在某些情况下，维护人员希望即时了解网元运行时的静态或动态信息，例如：MME的特有信息、用户信息、配置信息等，通过直连接口查询功能执行相应的查询命令以获取相关信息。 




[](None)功能描述 


本功能用于操作员查询本局的一些相关信息时使用。 


直连接口支持的查询功能包括： 



 

获取MME的特有信息。
 

 

获取配置数据。
 

 

获取单个用户信息。
 

 

获取eNodeB的连接信息。
 

 


对于信息量比较小的数据，操作员员可以在网管界面上直接查看。 


对于信息量比较大的数据，如：配置信息、eNodeB连接信息，系统会将查询结果存为excel或者txt文件，操作员可以通过下载文件的方式获取到相关内容。 




[](None)相关主题 



 

基本配置
 

 












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 基本配置 
## 基本配置 


[](None)背景知识 


在某些情况下，维护人员希望即时了解网元运行时的静态或动态信息，例如：MME的特有信息、用户信息、配置信息等，通过直连接口查询功能执行相应的查询命令以获取相关信息。 




[](None)功能描述 


本功能用于操作员查询本局的一些相关信息时使用。 


直连接口支持的查询功能包括： 



 

获取MME的特有信息。
 

 

获取配置数据。
 

 

获取单个用户信息。
 

 

获取eNodeB的连接信息。
 

 


对于信息量比较小的数据，操作员员可以在网管界面上直接查看。 


对于信息量比较大的数据，如：配置信息、eNodeB连接信息，系统会将查询结果存为excel或者txt文件，操作员可以通过下载文件的方式获取到相关内容。 




[](None)相关主题 



 

获取MME特有信息(GET MME INFO)
 

 

获取配置数据(GET ICMDATA)
 

 

获取单用户信息(GET USER INFO)
 

 

获取eNodeB连接信息(GET ENODEBS INFO)
 

 








父主题： [直连接口管理](../../zh-CN/tree/N_126012006.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 获取MME特有信息(GET MME INFO) 
### 获取MME特有信息(GET MME INFO) 


[](None)命令功能 

本命令用于获取MME的特有信息。


[](None)注意事项 

无。


[](None)命令举例 


获取MME特有信息。  


GET MME INFO; 


`

-----------------NFS_MMESGSN_0----------------
最大用户数 
--------------------
200000              
--------------------
记录数：1

全网唯一标识                               
-------------------------------------------------------
mmec22.mmegi8034.mme.epc.mnc011.mcc460.3gppnetwork.org 
-------------------------------------------------------
记录数：1
` 








父主题： [基本配置](../../zh-CN/tree/N_12601200611.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 获取配置数据(GET ICMDATA) 
### 获取配置数据(GET ICMDATA) 


[](None)命令功能 

本命令用于获取配置数据。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
TYPE|数据类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:ALL。|数据类型。






[](None)命令举例 


"获取配置数据。 

GET ICMDATA:TYPE="ALL"; 

`

-----------------NFS_MMESGSN_0----------------
文件路径 
-----------
sftp://ems:******@178.1.63.193:29029/Nfdata/UMAC193/vru-mmesgsn-oam-dba/UMAC193/AMM/CMDBA/getIcmdata/NE_1_CMDATA_2020_11_18_16_41_10_1605927927814.xml 
-----------
记录数 1

操作结果 
-----------
成功 
-----------
记录数 1
` 

"







父主题： [基本配置](../../zh-CN/tree/N_12601200611.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 获取单用户信息(GET USER INFO) 
### 获取单用户信息(GET USER INFO) 


[](None)命令功能 

本命令用于获取单用户信息。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IDTYPE|ID类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:。|ID类型。
USERID|用户ID|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|用户ID。






[](None)命令举例 


获取单用户信息。  


GET USER INFO:IDTYPE="IMSI",USERID="420111111111111"; 








父主题： [基本配置](../../zh-CN/tree/N_12601200611.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 获取eNodeB连接信息(GET ENODEBS INFO) 
### 获取eNodeB连接信息(GET ENODEBS INFO) 


[](None)命令功能 

本命令用于获取eNodeB连接信息。


[](None)注意事项 

无。


[](None)命令举例 


获取eNodeB连接信息。 


GET ENODEBS INFO; 








父主题： [基本配置](../../zh-CN/tree/N_12601200611.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


