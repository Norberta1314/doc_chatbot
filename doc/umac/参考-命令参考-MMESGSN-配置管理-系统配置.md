 系统配置 


背景知识 


介绍操作员在使用ZXUN uMAC产品进行网元全局配置部署及维护时，需要使用的命令。 




功能描述 


系统配置指网元全局配置，以及一些重要组件的配置。 




相关主题 



 

交换局配置
 

 

GSN节点与GTP版本映射配置
 

 

定时器配置
 

 

容量规划
 

 

MAP协议配置
 

 

N7配置
 

 

QoS配置
 

 

接入区域配置
 

 

SGSN对等PLMN配置
 

 

MME对等PLMN配置
 

 

Diameter配置
 

 

Gb接入配置
 

 

SGs口配置
 

 

MME IMSI鉴权配置
 

 

MME GUTI重分配配置
 

 

SGSN IMSI鉴权配置
 

 

DNS配置
 

 








父主题： [配置管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# GSN节点与GTP版本映射配置 
# GSN节点与GTP版本映射配置 


背景知识 


SGSN第一次与对端GSN节点进行消息交互，或与对端GSN节点交互过，后续再无业务交互，这两种情况下，SGSN向对端GSN节点发起业务请求时，SGSN未知对端GSN节点的GTP版本。此时，SGSN会先用GTPV1与对端GSN节点进行消息交互和Echo检测，如果对端没有正确响应，则再用GTPV0与对端GSN节点进行消息交互和Echo检测。 


如果SGSN提供GSN节点与GTP版本映射配置，明确对端GSN节点的GTP版本，则可以减少对接时GTP协商次数。 




功能描述 


配置GSN节点与GTP版本映射后，业务流程如下： 


MS发起PDP激活请求，SGSN获得PDP激活指向的GGSN地址后，根据GGSN地址查询GSN节点与GTP版本映射配置，得到GGSN的GTP版本，SGSN使用该GTP版本号向GGSN发送PDP激活请求，并继续后续PDP激活流程。 


MS携带激活的PDP上下文，发起局间路由更新或系统间切换请求时，SGSN新局向GGSN发起PDP上下文更新流程，新局SGSN根据GGSN地址查询GSN节点与GTP版本映射配置，得到GGSN的GTP版本，SGSN使用该GTP版本号向GGSN发送PDP更新请求，并继续后续PDP更新流程。 


SGSN间GTP请求消息的发送，例如Identification Request、SGSN Context Request等请求消息，根据指向的SGSN地址查询GSN节点与GTP版本映射配置，得到目标SGSN的GTP版本，SGSN使用该GTP版本号向目标SGSN发送GTP请求消息，并继续后续处理流程。 


SGSN和GGSN、目标SGSN定时进行Echo检测，SGSN根据GGSN/目标SGSN地址查询GSN节点与GTP版本映射配置，得到GTP版本，SGSN使用该GTP版本号发送Echo消息与对端GSN节点进行Echo检测。 


说明： 


GSN节点与GTP版本映射配置是可选的，如果不配置，在未知对端GSN节点的GTP版本时，SGSN仍使用GTP版本尝试机制与对端GSN节点进行消息交互和Echo检测。 




相关主题 



 

新增GSN节点与GTP版本映射配置(ADD GSN GTPVER)
 

 

修改GSN节点与GTP版本映射配置(SET GSN GTPVER)
 

 

删除GSN节点与GTP版本映射配置(DEL GSN GTPVER)
 

 

查询GSN节点与GTP版本映射配置(SHOW GSN GTPVER)
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增GSN节点与GTP版本映射配置(ADD GSN GTPVER) 
## 新增GSN节点与GTP版本映射配置(ADD GSN GTPVER) 


命令功能 


该命令用于配置GSN节点支持的GTP协议版本。在进行此项配置后，可以减少SGSN和各个GSN节点消息协商次数，优化处理流程。 


GSN节点指的是与本网元（SGSN）通过GTP协议交互的网元（比如邻接的GGSN、SGSN等）。 


GSN节点支持的GTP版本由运营商全局规划。 




注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
GSNADDR|GSN节点地址|参数可选性:必选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得（SHOW GPRS APN和、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
GTPVER|GTP版本|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:GTPV1。|表示对端GSN节点的GTP版本。取值含义：“GTPV0”：表示GTP版本0。“GTPV1”：表示GTP版本1。GTP：GTP是GPRS遂道协议，GTP协议包含控制面协议GTP-C（GTP Control Plane）和用户面协议GTP-U（GTP User Plane）两部分。Gn/Gp接口：Gn和Gp接口是指UMTS/GPRS骨干网中GSN（GPRS Support Node）节点之间的接口。Gn接口是同一个PLMN内GSN节点间的接口，Gp接口是不同的PLMN内GSN间的接口。GPRS网络中的GTP协议有两个版本：v0和v1。GTP v1版本顺从协议3GPP TS 29.060；GTP v0版本顺从协议3GPP TS 09.60。SGSN同时支持GTPv0和GTPv1：当SGSN收到对端GTP节点发送的GTP消息时，能够根据该消息是GTPv0或GTPv1自动回复对应类型的消息。当SGSN向对端GTP节点发送GTP消息时，它首先发送出GTPv1消息，如果没有收到成功响应，则默认为对端不支持v1版本，再以GTPv0的方式再发送一次消息。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


新增GSN节点与GTP版本映射配置，设置GSN节点IP地址为10.20.11.22，GTP版本为GTPV1。
ADD GSN GTPVER:GSNADDR=10.20.11.22,GTPVER=GTPV1; 








父主题： [GSN节点与GTP版本映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改GSN节点与GTP版本映射配置(SET GSN GTPVER) 
## 修改GSN节点与GTP版本映射配置(SET GSN GTPVER) 


命令功能 

该命令用于修改GSN节点支持的GTP协议版本。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
GSNADDR|GSN节点地址|参数可选性:必选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得（SHOW GPRS APN和、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
GTPVER|GTP版本|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|表示对端GSN节点的GTP版本。取值含义：“GTPV0”：表示GTP版本0。“GTPV1”：表示GTP版本1。GTP：GTP是GPRS遂道协议，GTP协议包含控制面协议GTP-C（GTP Control Plane）和用户面协议GTP-U（GTP User Plane）两部分。Gn/Gp接口：Gn和Gp接口是指UMTS/GPRS骨干网中GSN（GPRS Support Node）节点之间的接口。Gn接口是同一个PLMN内GSN节点间的接口，Gp接口是不同的PLMN内GSN间的接口。GPRS网络中的GTP协议有两个版本：v0和v1。GTP v1版本顺从协议3GPP TS 29.060；GTP v0版本顺从协议3GPP TS 09.60。SGSN同时支持GTPv0和GTPv1：当SGSN收到对端GTP节点发送的GTP消息时，能够根据该消息是GTPv0或GTPv1自动回复对应类型的消息。当SGSN向对端GTP节点发送GTP消息时，它首先发送出GTPv1消息，如果没有收到成功响应，则默认为对端不支持v1版本，再以GTPv0的方式再发送一次消息。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


修改GSN节点IP地址为10.20.11.22，GTP版本为GTPV1的GSN节点与GTP版本映射配置，将用户别名修改为zte。
SET GSN GTPVER:GSNADDR=10.20.11.22,GTPVER=GTPV1,NAME="zte"; 








父主题： [GSN节点与GTP版本映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除GSN节点与GTP版本映射配置(DEL GSN GTPVER) 
## 删除GSN节点与GTP版本映射配置(DEL GSN GTPVER) 


命令功能 

该命令用于删除GSN节点支持的GTP协议版本配置记录。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
GSNADDR|GSN节点地址|参数可选性:必选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得（SHOW GPRS APN和、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。






命令举例 


删除IP地址为10.20.11.22的GSN节点与GTP版本映射配置。
DEL GSN GTPVER:GSNADDR=10.20.11.22; 








父主题： [GSN节点与GTP版本映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询GSN节点与GTP版本映射配置(SHOW GSN GTPVER) 
## 查询GSN节点与GTP版本映射配置(SHOW GSN GTPVER) 


命令功能 

该命令用于查询GSN节点支持的GTP协议版本映射记录。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
GSNADDR|GSN节点地址|参数可选性:任选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得（SHOW GPRS APN和、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
GSNADDR|GSN节点地址|参数可选性:任选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得（SHOW GPRS APN和、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
GTPVER|GTP版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对端GSN节点的GTP版本。取值含义：“GTPV0”：表示GTP版本0。“GTPV1”：表示GTP版本1。GTP：GTP是GPRS遂道协议，GTP协议包含控制面协议GTP-C（GTP Control Plane）和用户面协议GTP-U（GTP User Plane）两部分。Gn/Gp接口：Gn和Gp接口是指UMTS/GPRS骨干网中GSN（GPRS Support Node）节点之间的接口。Gn接口是同一个PLMN内GSN节点间的接口，Gp接口是不同的PLMN内GSN间的接口。GPRS网络中的GTP协议有两个版本：v0和v1。GTP v1版本顺从协议3GPP TS 29.060；GTP v0版本顺从协议3GPP TS 09.60。SGSN同时支持GTPv0和GTPv1：当SGSN收到对端GTP节点发送的GTP消息时，能够根据该消息是GTPv0或GTPv1自动回复对应类型的消息。当SGSN向对端GTP节点发送GTP消息时，它首先发送出GTPv1消息，如果没有收到成功响应，则默认为对端不支持v1版本，再以GTPv0的方式再发送一次消息。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


查询所有GSN节点与GTP版本映射配置。
SHOW GSN GTPVER 


`

命令 (No.1): SHOW GSN GTPVER

操作维护         GSN节点地址   GTP版本   用户别名
-------------------------------------------------
复制 修改 删除   1.1.1.1       GTPV1     
-------------------------------------------------
记录数 1

命令执行成功（耗时 0.151 秒）。
` 








父主题： [GSN节点与GTP版本映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 定时器配置 
# 定时器配置 


背景知识 


在系统软件运行中，定时器用于以指定的时长自动触发业务执行相应的流程。 


系统中的定时器包括两种： 



 

预定义定时器
定时时长可以在运行过程中动态修改并实时生效，可以提高业务流程控制的灵活性。
 

 

时长固定的定时器
定时时长在软件实现中固定，在运行过程中不可动态修改，用于控制核心流程，以保证其稳定性。
 

 




功能描述 

            
            定时器管理维护网元模块/单元上的预定义定时器配置，主要是定时器到时时长参数。当网元维护操作中需要修改或查询模块/单元上预定义定时器的时候，需要使用以下命令，例如：网络优化，调整业务定时执行参数；数据恢复，将定时器配置恢复到初始值等。
        


相关主题 



 

修改预定义定时器(SET DEFPRETMR)
 

 

恢复预定义定时器(RESET DEFPRETMR)
 

 

查询预定义定时器(SHOW DEFPRETMR)
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改预定义定时器(SET DEFPRETMR) 
## 修改预定义定时器(SET DEFPRETMR) 


命令功能 

该命令用于修改网元的定时器配置。当网元维护中需调整某个业务定时器的时长时，使用该命令。调整设置成功后，可以通过[SHOW DEFPRETMR]查询确认网元定时器时长修改是否成功。
[所有定时器详细说明]




注意事项 


使用该命令，需输入“定时器标识”、“别名”，指定需修改的定时器，可通过[SHOW DEFPRETMR]获取。


修改业务的定时器时长将影响业务流程执行的频度，请谨慎使用。 




参数说明 


标识|名称|类型|说明
---|---|---|---
TIMER|定时器标识|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~2147483647。|定时器号，唯一标识一个定时器。
NAME|定时器名称|参数可选性:必须单选参数；参数类型:字符型；参数范围为:0~100个字符。|定时器的名称。
CURINTERVAL|当前的定时时长(ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|当前定时器时长，表示当前运行的定时器对应业务流程执行的周期。
NEWNAME|新定时器名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于用户重新自定义定时器的名称。






命令举例 


修改定时器标识为"40191"，当前时长为"36000ms"的预定义定时器。 


SET DEFPRETMR:TIMER=40191,CURINTERVAL=36000; 








父主题： [定时器配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 恢复预定义定时器(RESET DEFPRETMR) 
## 恢复预定义定时器(RESET DEFPRETMR) 


命令功能 

该命令用于恢复网元的定时器配置到初始值。当网元维护需要进行数据恢复时，可使用该命令。恢复设置成功后，可以通过[SHOW DEFPRETMR]查询确认网元定时器时长修改是否成功。
[所有定时器详细说明]




注意事项 


使用该命令，可以恢复所有的定时配置，也可以恢复指定定时器的配置。恢复指定定时器时长配置时需输入“定时器标识”参数，可通过[SHOW DEFPRETMR]获取。


修改业务的定时器时长将影响业务流程执行的频度，请谨慎使用。 




参数说明 


标识|名称|类型|说明
---|---|---|---
TIMER|定时器标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~2147483647。|定时器号，唯一标识一个定时器。






命令举例 


恢复全部预定义定时器。 


RESET DEFPRETMR; 








父主题： [定时器配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询预定义定时器(SHOW DEFPRETMR) 
## 查询预定义定时器(SHOW DEFPRETMR) 


命令功能 


该命令用于查询网元内预定义定时的配置： 


若查询全部预定义定时器配置信息，无需输入任何参数。 


若查询某条指定定时器的配置信息，需输入“定时器标识”、“别名”等参数。 


[所有定时器详细说明]




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TIMER|定时器标识|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~2147483647。|定时器号，唯一标识一个定时器。
NAME|定时器名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~100个字符。|定时器的名称。
MARCO|定时器宏名|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~32个字符。|定时器宏名，唯一标识一个定时器，给用户提供一个字符串助记符，以便更直观了解定时器所对应的业务流程的功能。
FLAG|修改标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于数据查询，表示查询结果是否包含修改的定时器，包括两种取值：未改变和已修改。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
TIMER|定时器标识|参数可选性:任选参数；参数类型:整数。|定时器号，唯一标识一个定时器。
NAME|定时器名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~1024个字符。|定时器的名称。
MARCO|定时器宏名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~1024个字符。|定时器宏名，唯一标识一个定时器，给用户提供一个字符串助记符，以便更直观了解定时器所对应的业务流程的功能。
DEFINTERVAL|缺省时长(ms)|参数可选性:任选参数；参数类型:整数。|缺省定时器时长，表示系统启动时数据库中初始加载的时长配置。
CURINTERVAL|当前时长(ms)|参数可选性:任选参数；参数类型:整数。|当前定时器时长，表示当前运行的定时器对应业务流程执行的周期。
FLAG|定时时长修改标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于数据查询，表示查询结果是否包含修改的定时器，包括两种取值：未改变和已修改。
LOWERLMTDUR|当前时长的下限值(ms)|参数可选性:任选参数；参数类型:整数。|定时器时长下限。
UPPERLMTDUR|当前时长的上限值(ms)|参数可选性:任选参数；参数类型:整数。|定时器时长上限。






命令举例 


查询定时器标识为"40191"的预定义定时器。 


SHOW DEFPRETMR:TIMER=40191; 


`

命令 (No.1): SHOW DEFPRETMR:TIMER=40191;

操作维护  定时器标识   定时器名称               定时器宏名               缺省时长(ms)   当前时长(ms)   定时时长修改标识   当前时长的下限值(ms)   当前时长的上限值(ms)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      40191        TIMER_CONNECTKEEPALIVE   TIMER_CONNECTKEEPALIVE   36000          36000          未改变             30000                  3600000
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.047 秒）。
` 








父主题： [定时器配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 容量规划 
# 容量规划 


背景知识 


容量规划主要用于配置系统处理能力相关的关键指标以及全局负荷分担策略。 




功能描述 


容量规划主要用于配置系统处理能力相关的关键指标以及全局负荷分担策略，包括以下4种配置功能： 



 

容量配置，包括单实例容量配置和全局容量配置，系统对这些已经有默认配置，一般情况不需要修改。
 

 

控制面负荷分担，用于配置控制面各USMP的负荷分担比例，支持缺省控制面负荷分担配置和人工设置各USMP模块的负荷分担比例两种配置方式。
 

 

Gb用户面负荷分担，用于设置参与用户面负荷分担的业务处理逻辑板号（2G USUP工作板号）和该逻辑板号对应的用户面IPV4或者IPV6地址。SGSN网元连接Gb接口时必须配置。
 

 

Iu用户面负荷分担，用于设置本网元所有参与Iu用户面负荷分担的USUP_3G模块编号和该USUP_3G模块的Iu口和Gn口用户面地址。SGSN网元连接Iu接口时必须配置。
 

 




相关主题 



 

容量配置
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 容量配置 
## 容量配置 


背景知识 


与系统处理能力相关的容量采用可配置的方式，便于根据运营商组网需要进行调整。 




功能描述 



 

若不配置则按默认值规划容量。
 

 

该项配置中的某些参数，需要license支持才有效，参见各参数的详细说明。
 

 

容量创建完成后，需要传送全部表数据到前台，并且整局重启之后才能生效。
 

 




相关主题 



 

设置容量规划(SET CAPACITY)
 

 

查询容量规划(SHOW CAPACITY)
 

 








父主题： [容量规划]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置容量规划(SET CAPACITY) 
### 设置容量规划(SET CAPACITY) 


命令功能 


该命令用于设置容量规划。 


该命令若不配置则按默认值规划容量，配置后传送全部表且前台重启后生效。 


创建MP的容量规划后，将全部表数据传送到前台，重启前台才能生效。 




注意事项 


承载/PDP下文个数 = SMP 附着用户数 * 激活:附着 


会话上下文个数 = 承载/PDP上下文个数÷APN平均建立的承载个数 


TFT队列的长度 = 承载/PDP上下文个数 * PMIP接入比例(%) ÷ 100 * 2 




参数说明 


标识|名称|类型|说明
---|---|---|---
SGMPMM|CMP附着用户数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~150000。|该参数用于配置单个CMP模块上的MM上下文容量。该参数同时适用于MME和SGSN网元。对于SGSN网元，表示GMM（GPRS Mobile Management，GPRS 移动性管理）上下文。对于MME网元，表示EMM（EPS Mobility Management，EPS移动性管理）上下文。对于COMBO网元，表示GMM上下文和EMM上下文的总和。
ACTATCHRATE|激活:附着|参数可选性:任选参数；参数类型:浮点|该参数用于配置单个CMP模块上的PDP上下文与MM上下文之间的容量比例关系。该参数同时适用于MME和SGSN网元。对于SGSN网元，表示PDP上下文与GMM上下文之间的容量比例关系。对于MME网元，表示PDP上下文与EMM上下文之间的容量比例关系。对于COMBO网元，表示PDP上下文与GMM上下文和EMM上下文的总和之间的容量比例关系。
LCSNUM|LCS资源容量(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数同时适用于MME和SGSN网元。该参数用于配置单个CMP模块上的LCS临时数据区的容量。LCS（Location Services，定位业务）是一种获取MS在移动通信系统中的位置，并对位置信息进行相应的转换、计算，提供出地理坐标值的业务。在获取手机用户的位置后，运营商就可以提供点播、信息定制、服务定制等丰富多样的、基于位置信息的服务。
SCCF|CMP CAMEL用户数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~150000。|该参数只适用于SGSN网元。该参数用于配置单个CMP模块上的CAMEL用户数。
SPMM|2G USUP MM上下文数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000000。|该参数只适用于SGSN网元。该参数用于配置单个USUP_GPRS模块上的GMM上下文容量。
UPPDP|USUP PDP上下文数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~500000。|该参数只适用于SGSN网元。该参数用于配置单个USUP_3G（用于处理3G用户的用户面数据）、USUP_GPRS（用于处理2G用户的用户面数据）和USUP_UP（用于处理2G用户和3G用户的用户面数据）模块上的PDP上下文容量。请注意USUP配置为1+1互备方式时，实际的单进程容量为本参数的一半，即互备的一对UP提供原来单个模块的容量。
UPPACKBUF|USUP报文缓存个数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:5000~60000。|该参数只适用于SGSN网元。该参数用于配置单个USUP_3G（用于处理3G用户的用户面数据）和USUP_GPRS（用于处理2G用户的用户面数据）模块的报文缓存个数。
LCSSGSN|SGSN支持LCS用户数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100000。|该参数只适用于SGSN网元。该参数用于配置单个CMP模块上的LCS用户数。
APNAVEBEAR|APN平均建立的承载个数|参数可选性:任选参数；参数类型:浮点|该参数只适用于MME网元。该参数用于配置控制面模块上单个用户每APN平均建立的承载个数。
PMIPRATE|PMIP接入比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数只适用于MME网元。该参数用于配置控制面模块上TFT上下文与PDP上下文的比例。
DIAMSESSION|Diameter会话容量(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:3000~20000。|该参数只适用于MME网元。该参数用于配置单个控制面模块上的Diameter会话上下文容量。
LCSMME|MME支持LCS用户数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100000。|该参数只适用于MME网元。该参数用于配置单个CMP模块上的LCS用户数。
PDPPDNDATA|平均每用户签约PDN/PDP连接数|参数可选性:任选参数；参数类型:浮点|对于SGSN网元，该参数用于配置平均每用户的PDP连接数。对于MME网元，该参数用于配置平均每用户签约的PDN连接数。
RESTOBAKCAP|容灾备份数据容量|参数可选性:任选参数；参数类型:整数；参数范围为:1~150000。|该参数只适用于MME网元。该参数用于配置单个CMP模块上备份的用于MME容灾的用户动态信息数。
BVC|BVC数(全局)|参数可选性:任选参数；参数类型:整数；参数范围为:1~120000。|该参数只针对SGSN网元生效。该参数用于配置全局支持的BVC上下文个数。
MAXCGNUM|最大CG服务器个数|参数可选性:任选参数；参数类型:整数；参数范围为:2~16。|该参数只针对SGSN网元生效。该参数用于配置全局支持的最大CG服务器个数。
S102DATANUM|S102数据区容量|参数可选性:任选参数；参数类型:整数；参数范围为:100~50000。|该参数适用于MME网元，MME网元需要支持S102接口时生效。该参数用于配置MME网元与1xCS-IWS之间的接口S102数据区的大小。
NBPDP|NB-IoT平均每用户承载数|参数可选性:任选参数；参数类型:浮点|该参数用于配置NB-IoT用户平均每用户的承载数目。该参数仅适用于MME。
NBAPNAVEBEAR|NB-IoT平均每APN承载数|参数可选性:任选参数；参数类型:浮点|该参数用于配置NB-IoT平均每APN的承载数目。该参数仅适用于MME。
NBPDNDATA|NB-IoT平均每用户签约PDN连接数|参数可选性:任选参数；参数类型:浮点|该参数用于配置NB-IoT用户平均每用户签约的PDN数目。该参数仅适用于MME。
UERADIOCAP|UE无线能力数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~95000。|该参数用于配置单个cmp模块上共享保存的ue无线能力数目。该参数仅适用于MME。
MCENUM|MCE容量(全局)|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于配置系统支持MCE的容量。
EMBMSNUM|EMBMS上下文数(单进程)|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|配置系统支持EMBMS会话的容量。
ROHCCAPIRATE|RoHC上下文比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数只适用于MME网元。该参数用于配置RoHC协商的上下文与承载上下文的比例。






命令举例 


设置CMP附着用户数（单进程）数为80000，CMP CAMEL用户数（单进程）为10000，USUP PDP上下文数（单进程）为500000，SGSN支持LCS用户数（单进程）为100000; 


SET CAPACITY:SGMPMM=80000,SCCF=10000,UPPDP=500000,LCSSGSN=100000; 








父主题： [容量配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询容量规划(SHOW CAPACITY) 
### 查询容量规划(SHOW CAPACITY) 


命令功能 


该命令用于查询容量规划。 




注意事项 


无。 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
SGMPMM|CMP附着用户数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数用于配置单个CMP模块上的MM上下文容量。该参数同时适用于MME和SGSN网元。对于SGSN网元，表示GMM（GPRS Mobile Management，GPRS 移动性管理）上下文。对于MME网元，表示EMM（EPS Mobility Management，EPS移动性管理）上下文。对于COMBO网元，表示GMM上下文和EMM上下文的总和。
ACTATCHRATE|激活:附着|参数可选性:任选参数；参数类型:浮点|该参数用于配置单个CMP模块上的PDP上下文与MM上下文之间的容量比例关系。该参数同时适用于MME和SGSN网元。对于SGSN网元，表示PDP上下文与GMM上下文之间的容量比例关系。对于MME网元，表示PDP上下文与EMM上下文之间的容量比例关系。对于COMBO网元，表示PDP上下文与GMM上下文和EMM上下文的总和之间的容量比例关系。
LCSNUM|LCS资源容量(单进程)|参数可选性:任选参数；参数类型:整数。|该参数同时适用于MME和SGSN网元。该参数用于配置单个CMP模块上的LCS临时数据区的容量。LCS（Location Services，定位业务）是一种获取MS在移动通信系统中的位置，并对位置信息进行相应的转换、计算，提供出地理坐标值的业务。在获取手机用户的位置后，运营商就可以提供点播、信息定制、服务定制等丰富多样的、基于位置信息的服务。
SCCF|CMP CAMEL用户数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数只适用于SGSN网元。该参数用于配置单个CMP模块上的CAMEL用户数。
SPMM|2G USUP MM上下文数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数只适用于SGSN网元。该参数用于配置单个USUP_GPRS模块上的GMM上下文容量。
UPPDP|USUP PDP上下文数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数只适用于SGSN网元。该参数用于配置单个USUP_3G（用于处理3G用户的用户面数据）、USUP_GPRS（用于处理2G用户的用户面数据）和USUP_UP（用于处理2G用户和3G用户的用户面数据）模块上的PDP上下文容量。请注意USUP配置为1+1互备方式时，实际的单进程容量为本参数的一半，即互备的一对UP提供原来单个模块的容量。
UPPACKBUF|USUP报文缓存个数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数只适用于SGSN网元。该参数用于配置单个USUP_3G（用于处理3G用户的用户面数据）和USUP_GPRS（用于处理2G用户的用户面数据）模块的报文缓存个数。
LCSSGSN|SGSN支持LCS用户数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数只适用于SGSN网元。该参数用于配置单个CMP模块上的LCS用户数。
APNAVEBEAR|APN平均建立的承载个数|参数可选性:任选参数；参数类型:浮点|该参数只适用于MME网元。该参数用于配置控制面模块上单个用户每APN平均建立的承载个数。
PMIPRATE|PMIP接入比例(%)|参数可选性:任选参数；参数类型:整数。|该参数只适用于MME网元。该参数用于配置控制面模块上TFT上下文与PDP上下文的比例。
DIAMSESSION|Diameter会话容量(单进程)|参数可选性:任选参数；参数类型:整数。|该参数只适用于MME网元。该参数用于配置单个控制面模块上的Diameter会话上下文容量。
LCSMME|MME支持LCS用户数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数只适用于MME网元。该参数用于配置单个CMP模块上的LCS用户数。
PDPPDNDATA|平均每用户签约PDN/PDP连接数|参数可选性:任选参数；参数类型:浮点|对于SGSN网元，该参数用于配置平均每用户的PDP连接数。对于MME网元，该参数用于配置平均每用户签约的PDN连接数。
S102DATANUM|S102数据区容量|参数可选性:任选参数；参数类型:整数。|该参数适用于MME网元，MME网元需要支持S102接口时生效。该参数用于配置MME网元与1xCS-IWS之间的接口S102数据区的大小。
RESTOBAKCAP|容灾备份数据容量|参数可选性:任选参数；参数类型:整数。|该参数只适用于MME网元。该参数用于配置单个CMP模块上备份的用于MME容灾的用户动态信息数。
BVC|BVC数(全局)|参数可选性:任选参数；参数类型:整数。|该参数只针对SGSN网元生效。该参数用于配置全局支持的BVC上下文个数。
MAXCGNUM|最大CG服务器个数|参数可选性:任选参数；参数类型:整数。|该参数只针对SGSN网元生效。该参数用于配置全局支持的最大CG服务器个数。
NBEMM|NB-IoT附着用户数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数用于配置单个CMP模块NB-IoT用户的EMM上下文容量。该参数仅适用于MME。
NBPDP|NB-IoT平均每用户承载数|参数可选性:任选参数；参数类型:浮点|该参数用于配置NB-IoT用户平均每用户的承载数目。该参数仅适用于MME。
NBAPNAVEBEAR|NB-IoT平均每APN承载数|参数可选性:任选参数；参数类型:浮点|该参数用于配置NB-IoT平均每APN的承载数目。该参数仅适用于MME。
NBPDNDATA|NB-IoT平均每用户签约PDN连接数|参数可选性:任选参数；参数类型:浮点|该参数用于配置NB-IoT用户平均每用户签约的PDN数目。该参数仅适用于MME。
UERADIOCAP|UE无线能力数(单进程)|参数可选性:任选参数；参数类型:整数。|该参数用于配置单个cmp模块上共享保存的ue无线能力数目。该参数仅适用于MME。
MCENUM|MCE容量(全局)|参数可选性:任选参数；参数类型:整数。|该参数用于配置系统支持MCE的容量。
EMBMSNUM|EMBMS上下文数(单进程)|参数可选性:任选参数；参数类型:整数。|配置系统支持EMBMS会话的容量。
ROHCCAPIRATE|RoHC上下文比例(%)|参数可选性:任选参数；参数类型:整数。|该参数只适用于MME网元。该参数用于配置RoHC协商的上下文与承载上下文的比例。






命令举例 


查询容量规划。 


SHOW CAPACITY; 


`

(No.1): SHOW CAPACITY

操作维护 CMP附着用户数(单进程) 激活:附着 LCS资源容量(单进程) CMP CAMEL用户数(单进程) 2G USUP MM上下文数(单进程) USUP PDP上下文数(单进程) USUP报文缓存个数(单进程) SGSN支持LCS用户数(单进程) APN平均建立的承载个数 PMIP接入比例(%) Diameter会话容量(单进程) MME支持LCS用户数(单进程) 平均每用户签约PDN/PDP连接数 S102数据区容量 容灾备份数据容量 BVC数(全局) 最大CG服务器个数 NB-IoT附着用户数(单进程) NB-IoT平均每用户承载数 NB-IoT平均每APN承载数 NB-IoT平均每用户签约PDN连接数 UE无线能力数(单进程) MCE容量(全局) EMBMS上下文数(全局) RoHC上下文比例(%) 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改     80000                 2         1                   80000                   1000000                    500000                   10000                    1                         1                     0               5000                     1                         7                          2000           80000            65000       2                400000                   1                      1                     1                             6000                 1             1                   0
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.025 秒）。



` 








父主题： [容量配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MAP协议配置 
# MAP协议配置 


背景知识 

            
            MAP（Mobile Application Part）是移动网络的应用层的信令系统，底层基于7号信令系统。在GPRS网络中，SGSN使用MAP协议的接口包括：SGSN与HLR之间的Gr口，SGSN和EIR之间的Gf口，SGSN和SMS-GMSC或SMS-IWMSC之间的Gd口。
        


功能描述 


MAP协议配置主要完成GT号码的MAP阶段配置，以及按IMSI的源GT号码功能相关配置。 


MAP协议配置包括以下2类配置： 


GT号码的MAP阶段配置，该配置支持根据GT号段配置MAP应用上下文的版本，该功能用于MAP应用上下文的版本协商。 


根据IMSI号段配置SGSN的源GT号码功能，该功能用于指定MAP消息中特定的源GT号码。 




相关主题 



 

多运营商配置
 

 

IMSI号段源GT配置
 

 

GT翻译号码MAP阶段配置
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 多运营商配置 
## 多运营商配置 


背景知识 


MAP协议是七号信令的应用层协议，使用SCCP作为信令传输协议。网元间采用MAP协议交互时，通过SCCP层的GT（Globe Title）地址翻译实现网元间寻址。SGSN给其他网元发送MAP信令时，需要填写信令消息的源GT地址和目的GT地址，源GT（主叫GT）地址是标识本局的GT号码，目的GT（被叫GT）地址是标识消息接收方的GT号码。发送消息时，SCCP层的GT翻译，可根据源GT和目的GT共同决定出局局向。 



                通常情况下，SGSN使用“本局移动数据“配置（命令为SET SGSNCFG或
                [SET COMBOCFG]
                ）中的SGSN号码作为源GT；也可以根据IMSI指定特定的源GT。
            




功能描述 


基于IMSI指定MAP信令消息的源GT功能，可以根据用户的IMSI，在发送MAP信令消息时，填写对应的源GT号码； 


本功能的配置方式为：首先在当前的“多运营商配置”中，配置运营商标识的源GT号码；然后在“IMSI号段源GT配置”中，配置IMSI号段对应的运营商标识；从而最终得到IMSI号段对应的源GT号码。该功能的启用同时需要开启系统软参（ID：65534）开关。 




相关主题 



 

新增运营网络标识(ADD NET NUMBER)
 

 

修改运营网络标识(SET NET NUMBER)
 

 

删除运营网络标识(DEL NET NUMBER)
 

 

查询运营网络标识(SHOW NET NUMBER)
 

 








父主题： [MAP协议配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增运营网络标识(ADD NET NUMBER) 
### 新增运营网络标识(ADD NET NUMBER) 


命令功能 


该命令用于增加“运营网络标识”指代的“运营网络号码”，后续可以通过[ADD IMSI2NETID]命令，根据“运营网络标识“来配置“运营网络号码”与用户的IMSI号码的对应关系。


“运营网络号码”为MAP信令中包含的源GT（Global Title，全局名）号码，供SGSN在基于MAP协议与其他网元通信时使用（例如SGSN根据IMSI寻址HLR）。 


MAP（Mobile Application Part，移动应用部分）协议是No.7号信令接口协议的一种，定义了为实现MS漫游功能而在各网络实体之间进行的信息交换方式。 


PS域中采用MAP协议的接口包括： 


Gr接口：SGSN与HLR之间的接口，用于交换有关MS位置信息及用户管理信息。
 

 
Gd接口：SGSN和SMC之间的接口，用来在SGSN和SMS-MSC之间交换短消息信息。
 

 
Gf接口：SGSN与EIR之间的接口，当SGSN需要检查国际移动设备识别码IMEI（International Mobile Equipment Identity，国际移动设备标识）的合法性时，需要通过Gf接口与EIR交换与IMEI有关的信息。
 

 


有关GT翻译的简介如下： 


No.7号信令网的信令消息都是通过MTP（Message Transfer Part，消息传递部分）进行传送的。在No.7号信令网中，MTP地址由信令点编码和信令网标识组成。 


信令消息的目的地址通常是由其他信息指出（例如MSC号、MDN号等），另外，地址还需要在国外网络中使用。这就有必要提供一种功能将这些信息翻译为MTP地址。这种转换过程就是GT翻译，是SCCP提供的功能之一。SCCP能够利用这些信息来得到SCCP消息的被叫部分地址，并且提供一个MTP可以进行寻址的地址。 


MAP使用SCCP作为其底层的信令传输协议。基于MAP协议进行通信的各网元间的消息，通过SCCP层的GT翻译进行寻址。MAP消息中需要包含源GT地址和目的GT地址。源GT地址是用于标识本局的GT号码。 




注意事项 


该命令适用于SGSN以及MME网元。 


该命令生效的前提：需要设置系统软件参数“SGSN支持基于IMSI指定MAP信令的源GT”为“是”，配置命令为[SET SOFTWARE PARAMETER]，其中“软件参数ID”为65543，“软件参数值”为1。




参数说明 


标识|名称|类型|说明
---|---|---|---
NETID|运营网络标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|该参数是用于标识运营网络号码的一个编号。该参数用于将“运营网络号码”与ADD IMSI2NETID命令中的“IMSI号段”进行关联。后续可以通过SHOW IMSI2NETID命令查询该“运营网络标识”是否与某个IMSI号段关联。
NETNUM|运营网络号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~16个字符。|该参数对应为MAP信令中包含的源GT号码，供SGSN在基于MAP协议与其他网元交互时使用。配置此参数时，可以使用SHOW GT命令查询其中的”被叫GT号码“，如果号码已经配置，可以直接使用”被叫GT号码“做为”运营网络号码“；否则需要使用ADD GT命令添加”被叫GT号码“。






命令举例 


新建一条运营网络标识记录，设置运营网络标识为100，运营网络号码为323232。
ADD NET NUMBER:NETID=100, NETNUM= "323232"; 








父主题： [多运营商配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改运营网络标识(SET NET NUMBER) 
### 修改运营网络标识(SET NET NUMBER) 


命令功能 

该命令用于修改“运营网络标识”指代的“运营网络号码”。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NETID|运营网络标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|该参数是用于标识运营网络号码的一个编号。该参数用于将“运营网络号码”与ADD IMSI2NETID命令中的“IMSI号段”进行关联。后续可以通过SHOW IMSI2NETID命令查询该“运营网络标识”是否与某个IMSI号段关联。
NETNUM|运营网络号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~16个字符。|该参数对应为MAP信令中包含的源GT号码，供SGSN在基于MAP协议与其他网元交互时使用。配置此参数时，可以使用SHOW GT命令查询其中的”被叫GT号码“，如果号码已经配置，可以直接使用”被叫GT号码“做为”运营网络号码“；否则需要使用ADD GT命令添加”被叫GT号码“。






命令举例 


修改运营网络标识为100的运营网络标识记录，将运营网络号码修改为99999999。
SET NET NUMBER:NETID=100, NETNUM= "99999999"; 








父主题： [多运营商配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除运营网络标识(DEL NET NUMBER) 
### 删除运营网络标识(DEL NET NUMBER) 


命令功能 

该命令用于删除“运营网络标识”。


注意事项 


在执行此命令之前，需要先通过[SHOW IMSI2NETID]命令查询该“运营网络标识”是否与某个IMSI号段关联，如果没有关联，则可执行此命令。


如果已经关联的话，则需要先通过[DEL IMSI2NETID]命令删除两者之间的关联，否则该命令无法执行。




参数说明 


标识|名称|类型|说明
---|---|---|---
NETID|运营网络标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|该参数是用于标识运营网络号码的一个编号。该参数用于将“运营网络号码”与ADD IMSI2NETID命令中的“IMSI号段”进行关联。后续可以通过SHOW IMSI2NETID命令查询该“运营网络标识”是否与某个IMSI号段关联。






命令举例 


删除运营网络标识为100的运营网络标识记录。
DEL NET NUMBER:NETID=100; 








父主题： [多运营商配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询运营网络标识(SHOW NET NUMBER) 
### 查询运营网络标识(SHOW NET NUMBER) 


命令功能 

该命令用于查询“运营网络标识”指代的“运营网络号码”。


注意事项 

如果还需要查询该“运营网络标识”关联的IMSI号段，可通过[SHOW IMSI2NETID]命令查询。


参数说明 


标识|名称|类型|说明
---|---|---|---
NETID|运营网络标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|该参数是用于标识运营网络号码的一个编号。该参数用于将“运营网络号码”与ADD IMSI2NETID命令中的“IMSI号段”进行关联。后续可以通过SHOW IMSI2NETID命令查询该“运营网络标识”是否与某个IMSI号段关联。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
NETID|运营网络标识|参数可选性:任选参数；参数类型:整数。|该参数是用于标识运营网络号码的一个编号。该参数用于将“运营网络号码”与ADD IMSI2NETID命令中的“IMSI号段”进行关联。后续可以通过SHOW IMSI2NETID命令查询该“运营网络标识”是否与某个IMSI号段关联。
NETNUM|运营网络号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~20个字符。|该参数对应为MAP信令中包含的源GT号码，供SGSN在基于MAP协议与其他网元交互时使用。配置此参数时，可以使用SHOW GT命令查询其中的”被叫GT号码“，如果号码已经配置，可以直接使用”被叫GT号码“做为”运营网络号码“；否则需要使用ADD GT命令添加”被叫GT号码“。






命令举例 


查询运营网络标识为100的运营网络标识记录。
SHOW NET NUMBER:NETID=100; 


`

命令 (No.1): SHOW NET NUMBER:NETID=100;

操作维护         运营网络标识   运营网络号码
--------------------------------------------
复制 修改 删除   100            323232
--------------------------------------------
记录数 1

命令执行成功（耗时 0.034 秒）。
` 








父主题： [多运营商配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## IMSI号段源GT配置 
## IMSI号段源GT配置 


背景知识 


MAP协议是七号信令的应用层协议，使用SCCP作为信令传输协议。网元间采用MAP协议交互时，通过SCCP层的GT（Globe Title）地址翻译实现网元间寻址。SGSN给其他网元发送MAP信令时，需要填写信令消息的源GT地址和目的GT地址，源GT（主叫GT）地址是标识本局的GT号码，目的GT（被叫GT）地址是标识消息接收方的GT号码。发送消息时，SCCP层的GT翻译，可根据源GT和目的GT共同决定出局局向。 



                通常情况下，SGSN使用“本局移动数据“配置（命令为SET SGSNCFG或
                [SET COMBOCFG]
                ）中的SGSN号码作为源GT；也可以根据IMSI指定特定的源GT。
            




功能描述 


基于IMSI指定MAP信令消息的源GT功能，可以根据用户的IMSI，在发送MAP信令消息时，填写对应的源GT号码； 


本功能的配置方式为：首先在“多运营商配置”中，配置运营商标识的源GT号码；然后在当前的“IMSI号段源GT配置”中，配置IMSI号段对应的运营商标识；从而最终得到IMSI号段对应的源GT号码。该功能的启用同时需要开启系统软参（ID：65534）开关。 




相关主题 



 

新增IMSI号段源GT(ADD IMSI2NETID)
 

 

修改IMSI号段源GT(SET IMSI2NETID)
 

 

删除IMSI号段源GT(DEL IMSI2NETID)
 

 

查询IMSI号段源GT(SHOW IMSI2NETID)
 

 








父主题： [MAP协议配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增IMSI号段源GT(ADD IMSI2NETID) 
### 新增IMSI号段源GT(ADD IMSI2NETID) 


命令功能 

该命令用于配置“IMSI号段”与“运营网络标识”的对应关系。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NETID|运营网络标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|该参数是用于标识运营网络号码的一个编号。该参数用于将通过ADD NET NUMBER命令配置“运营网络号码”与通过ADD IMSI2NETID命令中的“IMSI号段”进行关联。该参数的取值是通过ADD NET NUMBER命令配置的“运营网络标识”，可通过SHOW NET NUMBER命令查询。






命令举例 


新增一条IMSI号段源GT记录，设置IMSI号段为460001，运营网络标识为100。
ADD IMSI2NETID: IMSI="460001",NETID=100; 








父主题： [IMSI号段源GT配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改IMSI号段源GT(SET IMSI2NETID) 
### 修改IMSI号段源GT(SET IMSI2NETID) 


命令功能 

该命令用于修改“IMSI号段”与“运营网络标识”的对应关系。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NETID|运营网络标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|该参数是用于标识运营网络号码的一个编号。该参数用于将通过ADD NET NUMBER命令配置“运营网络号码”与通过ADD IMSI2NETID命令中的“IMSI号段”进行关联。该参数的取值是通过ADD NET NUMBER命令配置的“运营网络标识”，可通过SHOW NET NUMBER命令查询。






命令举例 


修改IMSI号段为46001的IMSI号段源GT记录，将运营网络标识修改为101。
SET IMSI2NETID: IMSI="46001",NETID=101; 








父主题： [IMSI号段源GT配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除IMSI号段源GT(DEL IMSI2NETID) 
### 删除IMSI号段源GT(DEL IMSI2NETID) 


命令功能 

该命令用于删除“IMSI号段”与“运营网络标识”的对应关系。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






命令举例 


删除IMSI号段为46001的IMSI号段源GT记录。
DEL IMSI2NETID: IMSI="46001"; 








父主题： [IMSI号段源GT配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询IMSI号段源GT(SHOW IMSI2NETID) 
### 查询IMSI号段源GT(SHOW IMSI2NETID) 


命令功能 

该命令用于查询“IMSI号段”与“运营网络标识”的对应关系。


注意事项 

如果还需要查询该“运营网络标识”指代的“运营网络号码”，可通过[SHOW NET NUMBER]命令查询。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NETID|运营网络标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|该参数是用于标识运营网络号码的一个编号。该参数用于将通过ADD NET NUMBER命令配置“运营网络号码”与通过ADD IMSI2NETID命令中的“IMSI号段”进行关联。该参数的取值是通过ADD NET NUMBER命令配置的“运营网络标识”，可通过SHOW NET NUMBER命令查询。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NETID|运营网络标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|该参数是用于标识运营网络号码的一个编号。该参数用于将通过ADD NET NUMBER命令配置“运营网络号码”与通过ADD IMSI2NETID命令中的“IMSI号段”进行关联。该参数的取值是通过ADD NET NUMBER命令配置的“运营网络标识”，可通过SHOW NET NUMBER命令查询。






命令举例 


查询所有的IMSI号段源GT记录。
SHOW IMSI2NETID; 


`

命令 (No.1): SHOW IMSI2NETID;

操作维护         IMSI号段   运营网络标识
----------------------------------------
复制 修改 删除   460001     100
----------------------------------------
记录数 1

命令执行成功（耗时 0.034 秒）。
` 








父主题： [IMSI号段源GT配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## GT翻译号码MAP阶段配置 
## GT翻译号码MAP阶段配置 


背景知识 


MAP协议中，应用上下文（AC）标识了每种特定的业务类型；出于兼容性的考虑，每个应用上下文都有版本信息，表示其支持的应用处理能力。SGSN在发送MAP消息前，根据消息的应用上下文和所需版本以及对端网元支持的应用上下文的最高版本，选择合适的应用上下文版本，用于消息发送。 


如果每次发送消息都需要两端协商，会导致局间信令的增加，所以为了减少发送方向上的MAP版本协商，可以预先设置目的局向上各应用上下文的缺省MAP版本。 




功能描述 



                “GT翻译号码MAP阶段配置”中，指定对端各网元能够支持的MAP应用上下文（AC）的版本（阶段），命令为
                [SET GT2ACMAP]
                。通常一个GT号码标识一个对接的MAP协议网元，对端网元的GT号码可以通过
                [SHOW GT]
                查询，通过配置其支持的应用上下文版本，可以得知对端网元的MAP协议的兼容性和处理能力。
            



                该配置也用于配置缺省的对端网元应用上下文版本，命令为：
                [SET DEFAULT ACMAP]
                ，如果对端网元的GT号码没有在
                [SET GT2ACMAP]
                中配置时，本网元使用缺省配置中的应用上下文版本作为对端网元的应用上下文版本。
            




相关主题 



 

设置系统缺省AC MAP阶段(SET DEFAULT ACMAP)
 

 

设置GT号码对应AC MAP阶段(SET GT2ACMAP)
 

 

删除GT号码对应AC MAP阶段(DEL GT2ACMAP)
 

 

查询GT号码对应AC MAP阶段(SHOW GT2ACMAP)
 

 








父主题： [MAP协议配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置系统缺省AC MAP阶段(SET DEFAULT ACMAP) 
### 设置系统缺省AC MAP阶段(SET DEFAULT ACMAP) 


命令功能 


该命令用于配置对端网元当前支持的缺省AC（Application Context，应用上下文）的MAP阶段。 


配置该命令后, 当本网元向对端网元发起特定的MAP请求时，首先根据对端网元的GT号码查询通过[SET GT2ACMAP]命令配置的数据，系统将根据MAP请求中的AC获取对应支持的MAP版本, 修改当前待发送MAP版本以适配对端网元, 从而减少本网元与对端网元进行MAP版本协商的次数，提高成功率的目的。


如果查询[SET GT2ACMAP]命令配置的数据，不能获取匹配的记录，则根据本命令配置的缺省数据修改当前待发送MAP版本以适配对端网元。




注意事项 

该命令适用于SGSN以及MME网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
AC|AC|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示AC（Application Context，应用上下文）的类型，包括以下内容：equipmentMngtContext 设备管理：对应操作为CheckIMEI，SGSN用于IMEI（International Mobile Equipment Identity，国际移动设备标识）检查。infoRetrievalContext 获取鉴权向量：对应操作为SendAuthenticationInfo，SGSN用于从HLR获取鉴权向量。shortMsgMO-RelayContext 短消息起呼：对应操作为mo-forwardSM，SGSN用于向SC（Short Message Center，短消息中心）提交短消息。mwdMngtContext 短消息提醒：对应操作为ReadyForSM，SGSN用于通知HLR用户可接收短消息。msPurgingContext Purge用户：对应操作为PurgeMS，SGSN用于向HLR发起Purge MS操作。gprsLocationUpdateContext GPRS位置更新：对应操作为UpdateGprsLocation，SGSN用于向HLR发起位置更新。gprsLocationInfoRetrievalContext 发送GPRS路由信息：对应操作为sendRoutingInfoForGprs，SGSN用于向HLR发起路由查询。failureReportContext 失败报告：对应操作为FailureReport，SGSN用于向HLR发起失败报告。locationSvcEnquiryContext 提供用户位置信息：对应操作为subscriberLocationReport，SGSN用于向GMLC（Gateway for Mobile Location Center，移动定位中心网关）上报用户位置信息。authenticationFailureReportContext 鉴权失败报告：对应操作为authenticationFailureReport，SGSN用于向HLR报告鉴权失败。mm-EventReportingContext 通知MM事件：对应操作为noteMM-Event，SGSN用于向HLR报告MM（Mobility Management，移动性管理）事件。
MAPVER|MAP阶段|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|本参数用于指示本网元的对端网元最高支持的功能版本。系统通过GT号码，获取到对端网元最高支持的功能版本，再根据协议规定和当前待发送的对话操作获得对端支持的应用上下文的版本。取值含义：Phase1，MAP phase1支持的版本信息。>Phase2，MAP phase2支持的版本信息。Phase2+，MAP phase2+支持的版本信息。Release99，MAP Release99支持的版本信息。R4，MAP Release4支持的版本信息






命令举例 


设置系统缺省AC MAP阶段，设置AC为设备管理，MAP阶段为invalid。
SET DEFAULT ACMAP:AC=equipmentMngtContext,MAPVER=invalid; 








父主题： [GT翻译号码MAP阶段配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置GT号码对应AC MAP阶段(SET GT2ACMAP) 
### 设置GT号码对应AC MAP阶段(SET GT2ACMAP) 


命令功能 


该命令用于根据对端网元的GT号码配置对端网元当前支持AC的MAP阶段。 


配置该命令后, 当本网元向对端网元发起特定的MAP请求时，首先根据对端网元的GT号码查询通过[SET GT2ACMAP]命令配置的数据，系统将根据MAP请求中的AC获取对应支持的MAP版本, 修改当前待发送MAP版本以适配对端网元, 从而减少本网元与对端网元进行MAP版本协商的次数，提高成功率的目的。




注意事项 


对于相同的GT号码，系统可以根据不同的AC配置不同的MAP阶段。 


如果查询[SET GT2ACMAP]命令配置的数据，不能获取匹配的记录，则根据[SET DEFAULT ACMAP]命令配置的缺省数据修改当前待发送MAP版本以适配对端网元。




参数说明 


标识|名称|类型|说明
---|---|---|---
GT|GT号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~20个字符。|该参数对应为MAP信令中包含的对端邻接局的GT号码，供SGSN在基于MAP协议与其他网元交互时使用。此参数的取值，可以使用SHOW GT命令查询其中的”被叫GT号码“，如果号码已经配置，可以直接使用”被叫GT号码“做为”GT号码“；否则需要使用ADD GT命令添加”被叫GT号码“。
AC|AC|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示AC（Application Context，应用上下文）的类型，包括以下内容：equipmentMngtContext 设备管理：对应操作为CheckIMEI，SGSN用于IMEI（International Mobile Equipment Identity，国际移动设备标识）检查。infoRetrievalContext 获取鉴权向量：对应操作为SendAuthenticationInfo，SGSN用于从HLR获取鉴权向量。shortMsgMO-RelayContext 短消息起呼：对应操作为mo-forwardSM，SGSN用于向SC（Short Message Center，短消息中心）提交短消息。mwdMngtContext 短消息提醒：对应操作为ReadyForSM，SGSN用于通知HLR用户可接收短消息。msPurgingContext Purge用户：对应操作为PurgeMS，SGSN用于向HLR发起Purge MS操作。gprsLocationUpdateContext GPRS位置更新：对应操作为UpdateGprsLocation，SGSN用于向HLR发起位置更新。gprsLocationInfoRetrievalContext 发送GPRS路由信息：对应操作为sendRoutingInfoForGprs，SGSN用于向HLR发起路由查询。failureReportContext 失败报告：对应操作为FailureReport，SGSN用于向HLR发起失败报告。locationSvcEnquiryContext 提供用户位置信息：对应操作为subscriberLocationReport，SGSN用于向GMLC（Gateway for Mobile Location Center，移动定位中心网关）上报用户位置信息。authenticationFailureReportContext 鉴权失败报告：对应操作为authenticationFailureReport，SGSN用于向HLR报告鉴权失败。mm-EventReportingContext 通知MM事件：对应操作为noteMM-Event，SGSN用于向HLR报告MM（Mobility Management，移动性管理）事件。
MAPVER|MAP阶段|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|本参数用于指示本网元的对端网元最高支持的功能版本。系统通过GT号码，获取到对端网元最高支持的功能版本，再根据协议规定和当前待发送的对话操作获得对端支持的应用上下文的版本。取值含义：Phase1，MAP phase1支持的版本信息。>Phase2，MAP phase2支持的版本信息。Phase2+，MAP phase2+支持的版本信息。Release99，MAP Release99支持的版本信息。R4，MAP Release4支持的版本信息






命令举例 


设置GT号码对应AC MAP阶段，设置GT号为55，AC为设备管理，MAP阶段为invalid。
SET GT2ACMAP:GT="55",AC="equipmentMngtContext",MAPVER="invalid"; 








父主题： [GT翻译号码MAP阶段配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除GT号码对应AC MAP阶段(DEL GT2ACMAP) 
### 删除GT号码对应AC MAP阶段(DEL GT2ACMAP) 


命令功能 

该命令用于删除GT号码对应的对端网元当前支持的AC的MAP阶段。


注意事项 

使用此删除命令时，GT号码对应的所有AC的MAP阶段都将被删除。


参数说明 


标识|名称|类型|说明
---|---|---|---
GT|GT号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~20个字符。|该参数对应为MAP信令中包含的对端邻接局的GT号码，供SGSN在基于MAP协议与其他网元交互时使用。此参数的取值，可以使用SHOW GT命令查询其中的”被叫GT号码“，如果号码已经配置，可以直接使用”被叫GT号码“做为”GT号码“；否则需要使用ADD GT命令添加”被叫GT号码“。






命令举例 


删除GT号码为55的对应AC MAP阶段。
DEL GT2ACMAP:GT="55"; 








父主题： [GT翻译号码MAP阶段配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询GT号码对应AC MAP阶段(SHOW GT2ACMAP) 
### 查询GT号码对应AC MAP阶段(SHOW GT2ACMAP) 


命令功能 

该命令用于显示GT号码对应的对端网元当前支持的AC的MAP阶段。


注意事项 

如果未输入GT号码，将显示所有的GT号码对应的AC的MAP阶段，包括通过[SET DEFAULT ACMAP]命令配置的缺省数据记录。


参数说明 


标识|名称|类型|说明
---|---|---|---
GT|GT号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~20个字符。|该参数对应为MAP信令中包含的对端邻接局的GT号码，供SGSN在基于MAP协议与其他网元交互时使用。此参数的取值，可以使用SHOW GT命令查询其中的”被叫GT号码“，如果号码已经配置，可以直接使用”被叫GT号码“做为”GT号码“；否则需要使用ADD GT命令添加”被叫GT号码“。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
GT|GT号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~20个字符。|该参数对应为MAP信令中包含的对端邻接局的GT号码，供SGSN在基于MAP协议与其他网元交互时使用。此参数的取值，可以使用SHOW GT命令查询其中的”被叫GT号码“，如果号码已经配置，可以直接使用”被叫GT号码“做为”GT号码“；否则需要使用ADD GT命令添加”被叫GT号码“。
AC13MAPVER|设备管理|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，支持MAP版本1；Phase2阶段，支持MAP版本1和2；Phase2+阶段，支持MAP版本1和2；Release99阶段，支持MAP版本1和2；R4阶段，支持MAP版本1和2。
AC14MAPVER|获取鉴权向量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，支持MAP版本1；Phase2阶段，支持MAP版本1和2；Phase2+阶段，支持MAP版本1和2；Release99阶段，支持MAP版本1、2和3；R4阶段，支持MAP版本1、2和3。
AC21MAPVER|短消息起呼|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，支持MAP版本1；Phase2阶段，支持MAP版本1和2；Phase2+阶段，支持MAP版本1、2和3；Release99阶段，支持MAP版本1、2和3；R4阶段，支持MAP版本1、2和3。
AC24MAPVER|短消息提醒|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，支持MAP版本1；Phase2阶段，支持MAP版本1和2；Phase2+阶段，支持MAP版本1、2和3；Release99阶段，支持MAP版本1、2和3；R4阶段，支持MAP版本1、2和3。
AC27MAPVER|Purge用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，不支持；Phase2阶段，支持MAP版本2；Phase2+阶段，支持MAP版本2和3；Release99阶段，支持MAP版本2和3；R4阶段，支持MAP版本2和3。
AC32MAPVER|GPRS位置更新|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，不支持；Phase2阶段，不支持；Phase2+阶段，支持MAP版本3；Release99阶段，支持MAP版本3；R4阶段，支持MAP版本3。
AC33MAPVER|发送GPRS路由信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，不支持；Phase2阶段，不支持；Phase2+阶段，支持MAP版本3；Release99阶段，支持MAP版本3；R4阶段，支持MAP版本3。
AC34MAPVER|失败报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，不支持；Phase2阶段，不支持；Phase2+阶段，支持MAP版本3；Release99阶段，支持MAP版本3；R4阶段，支持MAP版本3。
AC38MAPVER|提供用户位置信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，不支持；Phase2阶段，不支持；Phase2+阶段，支持MAP版本3；Release99阶段，支持MAP版本3；R4阶段，支持MAP版本3。
AC39MAPVER|鉴权失败报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，不支持；Phase2阶段，不支持；Phase2+阶段，不支持；Release99阶段，支持MAP版本3；R4阶段，支持MAP版本3。
AC42MAPVER|通知MM事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为执行SHOW GT2ACMAP命令后的输出参数。该AC在不同的阶段，支持的MAP版本情况如下：Phase1阶段，不支持；Phase2阶段，不支持；Phase2+阶段，不支持；Release99阶段，支持MAP版本3；R4阶段，支持MAP版本3。






命令举例 


查询所有GT号码对应AC MAP阶段。
SHOW GT2ACMAP:GT="55"; 


`

命令 (No.1): SHOW GT2ACMAP:GT="55";

操作维护    GT号码   设备管理   获取鉴权向量   短消息起呼   短消息提醒   Purge用户   GPRS位置更新   发送GPRS路由信息   失败报告   提供用户位置信息   鉴权失败报告   通知MM事件
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改 删除   55       Invalid    Invalid        Phase2       Invalid      Invalid     Invalid        Invalid            Invalid    Invalid            Invalid        Invalid
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.034 秒）。
` 








父主题： [GT翻译号码MAP阶段配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# N7配置 
# N7配置 


背景知识 

            
            七号信息系统（SS7, Signaling System Number 7）是一种被广泛应用于公共交换电话网和蜂窝通信网络等现代通信网络的共路信令系统。
        


功能描述 

            
            N7配置实现的是七号信令系统相关的编码计划配置。
        


相关主题 



 

编码计划配置
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 编码计划配置 
## 编码计划配置 


背景知识 


编码计划也叫编号计划，是指移动通信网络中，使用的各种用来识别身份的号码的格式、含义和范围。 


常见的编号计划有： 



 

ITU-T Recommendation E.164: "The international public telecommunication numbering plan".定义，号码结构为：CC+NDC+SN；CC=国家码；NDC=国内目的地码，即网路接入号；SN=客户号码，采用等长7位编号计划。
 

 

ITU-T Recommendation E.212: "The international identification plan for mobile terminals and mobile users".定义，号码结构为：MCC+MNC+MSIN；MCC=移动国家号码，由3位数字组成，唯一地识别移动客户所属的国家；MNC=移动网号，由2-3位数字组成，用于识别移动客户所归属的移动网。MSIN=移动客户识别码，采用等长11位数字构成。唯一地识别国内移动通信网中移动客户。
 

 


SSN是SCCP协议使用的子系统号（Sub System Number），用于识别一个节点中的各个SCCP用户，扩充了SCCP的寻址范围。不同的SCCP用户，一般固定分配不同的SSN。每个基于SCCP的上层用户，都分配有SSN。 




功能描述 

            
            编码计划配置主要实现两类配置，一类是移动号码类型的编码计划配置，用于配置特定号码类型的编码计划和地址种类；一类是子系统类型的编码计划配置，用于配置子系统描述ID，增加某种特定的子系统描述ID，其对应的系统使用的SSN值将改变，改变后的SSN值作为该子系统的编号。
一般情况下，不需要增加移动号码类型的编码计划配置；但需要增加常用的子系统描述ID，如SCCP、HLR、MSC、VLR、MAP、AUC、EIR、BSSAP、RANAP、SGSN、GGSN等。
        


相关主题 



 

新增编码计划（移动号码类型）(ADD MCPLAN)
 

 

修改编码计划（移动号码类型）(SET MCPLAN)
 

 

新增编码计划（子系统类型）(ADD SSNPLAN)
 

 

修改编码计划（子系统类型）(SET SSNPLAN)
 

 

删除编码计划(DEL MPLAN)
 

 

查询编码计划(SHOW MPLAN)
 

 








父主题： [N7配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增编码计划（移动号码类型）(ADD MCPLAN) 
### 新增编码计划（移动号码类型）(ADD MCPLAN) 


命令功能 

该命令用于新增移动号码类型的编码计划，即为某种特定的号码类型，配置其使用的编号计划和地址类型。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
CTYPE|移动号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|移动号码类型为枚举型参数，各个号码类型的含义如下：移动台ISDN号码（MSISDN）：MSISDN号码是指主叫客户为呼叫数字公用陆地蜂窝移动通信网中客户所需拨的号码。号码的结构为：CC+NDC+SN；CC=国家码；NDC=国内目的地码，即网路接入号；SN=客户号码，采用等长7位编号计划。国际移动客户识别码（IMSI）：为了在无线路径和整个GSM移动通信网上正确地识别某个移动客户，就必须给移动客户分配一个特定的识别码。这个识别码称为国际移动客户识别码（IMSI），用于移动通信网所有信令中。IMSI号码结构为：MCC+MNC+MSIN；MCC=移动国家号码，由3位数字组成，唯一地识别移动客户所属的国家；MNC=移动网号，由2-3位数字组成，用于识别移动客户所归属的移动网。MSIN=移动客户识别码，采用等长11位数字构成。唯一地识别国内移动通信网中移动客户。移动客户漫游号码（MSRN）：被叫客户所归属的HLR知道该客户目前是处于哪一个MSC/VLR业务区，为了提供给入口MSC/VLR（GMSC）一个用于选路由的临时号码，HLR请求被叫所在业务区的MSC/VLR给该被叫客户分配一个移动客户漫游号码（MSRN），并将此号码送至HLR，HLR收到后再发送给GMSC，GMSC根据此号码选路由，将呼叫接至被叫客户目前正在访问的MSC/VLR交换局。路由一旦建立，此号码就可立即释放。这种查询、呼叫选路由功能（即请求一个MSRN功能）是7号信令中移动应用部分（MAP）的一个程序，在GMSC—HLR—MSC/VLR间的7号信令网中进行传递。移动客户漫游号码（MSRN）结构是：CC+NDC+SN。临时移动客户识别码（TMSI）：为了对IMSI保密，MSC/VLR可给来访移动客户分配一个唯一的TMSI号码，即为一个由MSC自行分配的4字节的BCD编码，仅限在本MSC业务区内使用。全球小区识别码（CGI）：CGI是用来识别一个位置区内的小区，它是在位置区识别码 （LAI）后加上一个小区识别码（CI），其结构是：MCC+MNC+LAC+CI；CI是一个2字节BCD编码，由各MSC自定。基站识别码（BSIC）：BSIC是用于识别相邻国家的相邻基站的，为6bit编码，其结构是：NCC（3bit）+BCC（3bit）；NCC=国家色码，主要用来区分国界各侧的运营者。MSC号码：MSC号码在7号信令信息中使用，代表MSC的号码。结构是：CC+NDC+SN；可为其分配特定的号码。VLR号码：VLR号码在7号信令信息中使用，代表VLR的号码。结构是：CC+NDC+SN；可为其分配特定的号码。HLR号码：HLR号码在7号信令信息中使用，代表HLR的号码。结构是：CC+NDC+SN；可为其分配特定的号码。切换号码（HON）：HON是当进行移动交换局间切换时，为选择路由，由目标MSC（即切换要转移到的MSC）临时分配给移动客户的一个号码。此号码为MSRN号码的一部分。其他特殊号码（SPEC）：非上述号码类型的其他特殊号码。
PLAN|编码计划|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:PLMN。|编码计划为枚举型参数，列举了各种可能的编码计划，即号码的编码格式；移动网络中主要使用的有两种：电话编号计划（ISDN）即E.164编号计划；以及陆地移动编号计划（PLMN）即E.212编号计划。
ADDR|地址种类|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:INTL。|地址种类为枚举类型，列举了地址的不同属性。说明如下：INTL: 国际号码NAT: 国内有效号码NET: 网络号码USER: 用户号码ABBR: 小号码
ID|编码计划配置标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|用来标识当前的编码计划配置，移动号码类型的编号计划和子系统类型的编号计划采用统一的编号，不可重复。也可以不输入特定的标识，这样系统会直接分配一个默认的标识。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


新增移动号码类型的编码计划， 设置移动号码类型为移动用户ISDN号码，设置编码计划为电话编号计划，设置编码计划配置标识为1。 


ADD MCPLAN:CTYPE="ISDN",PLAN="ISDN",ID=1; 








父主题： [编码计划配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改编码计划（移动号码类型）(SET MCPLAN) 
### 修改编码计划（移动号码类型）(SET MCPLAN) 


命令功能 

该命令用于修改移动号码类型的编码计划，即针对已有的某种特定的号码类型，修改其使用的编号计划和地址类型。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
CTYPE|移动号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|移动号码类型为枚举型参数，各个号码类型的含义如下：移动台ISDN号码（MSISDN）：MSISDN号码是指主叫客户为呼叫数字公用陆地蜂窝移动通信网中客户所需拨的号码。号码的结构为：CC+NDC+SN；CC=国家码；NDC=国内目的地码，即网路接入号；SN=客户号码，采用等长7位编号计划。国际移动客户识别码（IMSI）：为了在无线路径和整个GSM移动通信网上正确地识别某个移动客户，就必须给移动客户分配一个特定的识别码。这个识别码称为国际移动客户识别码（IMSI），用于移动通信网所有信令中。IMSI号码结构为：MCC+MNC+MSIN；MCC=移动国家号码，由3位数字组成，唯一地识别移动客户所属的国家；MNC=移动网号，由2-3位数字组成，用于识别移动客户所归属的移动网。MSIN=移动客户识别码，采用等长11位数字构成。唯一地识别国内移动通信网中移动客户。移动客户漫游号码（MSRN）：被叫客户所归属的HLR知道该客户目前是处于哪一个MSC/VLR业务区，为了提供给入口MSC/VLR（GMSC）一个用于选路由的临时号码，HLR请求被叫所在业务区的MSC/VLR给该被叫客户分配一个移动客户漫游号码（MSRN），并将此号码送至HLR，HLR收到后再发送给GMSC，GMSC根据此号码选路由，将呼叫接至被叫客户目前正在访问的MSC/VLR交换局。路由一旦建立，此号码就可立即释放。这种查询、呼叫选路由功能（即请求一个MSRN功能）是7号信令中移动应用部分（MAP）的一个程序，在GMSC—HLR—MSC/VLR间的7号信令网中进行传递。移动客户漫游号码（MSRN）结构是：CC+NDC+SN。临时移动客户识别码（TMSI）：为了对IMSI保密，MSC/VLR可给来访移动客户分配一个唯一的TMSI号码，即为一个由MSC自行分配的4字节的BCD编码，仅限在本MSC业务区内使用。全球小区识别码（CGI）：CGI是用来识别一个位置区内的小区，它是在位置区识别码 （LAI）后加上一个小区识别码（CI），其结构是：MCC+MNC+LAC+CI；CI是一个2字节BCD编码，由各MSC自定。基站识别码（BSIC）：BSIC是用于识别相邻国家的相邻基站的，为6bit编码，其结构是：NCC（3bit）+BCC（3bit）；NCC=国家色码，主要用来区分国界各侧的运营者。MSC号码：MSC号码在7号信令信息中使用，代表MSC的号码。结构是：CC+NDC+SN；可为其分配特定的号码。VLR号码：VLR号码在7号信令信息中使用，代表VLR的号码。结构是：CC+NDC+SN；可为其分配特定的号码。HLR号码：HLR号码在7号信令信息中使用，代表HLR的号码。结构是：CC+NDC+SN；可为其分配特定的号码。切换号码（HON）：HON是当进行移动交换局间切换时，为选择路由，由目标MSC（即切换要转移到的MSC）临时分配给移动客户的一个号码。此号码为MSRN号码的一部分。其他特殊号码（SPEC）：非上述号码类型的其他特殊号码。
PLAN|编码计划|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编码计划为枚举型参数，列举了各种可能的编码计划，即号码的编码格式；移动网络中主要使用的有两种：电话编号计划（ISDN）即E.164编号计划；以及陆地移动编号计划（PLMN）即E.212编号计划。
ADDR|地址种类|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|地址种类为枚举类型，列举了地址的不同属性。说明如下：INTL: 国际号码NAT: 国内有效号码NET: 网络号码USER: 用户号码ABBR: 小号码
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


修改移动号码类型为移动用户ISDN号码的编码计划，修改编码计划为电话编号计划，修改址种类为国际号码。 


SET MCPLAN:CTYPE="ISDN",PLAN="ISDN",ADDR="INTL"; 








父主题： [编码计划配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增编码计划（子系统类型）(ADD SSNPLAN) 
### 新增编码计划（子系统类型）(ADD SSNPLAN) 


命令功能 

该命令用于新增子系统类型的编码计划。需要增加常用的子系统描述ID，如SCCP、HLR、MSC、VLR、MAP、AUC、EIR、BSSAP、RANAP、SGSN、GGSN等。增加后，可以通过[SHOW MPLAN]命令查询。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
SSN|子系统描述ID|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|子系统描述ID为枚举型参数，列举了SCCP的子系统号不同取值对应上层应用的名称。增加特定的子系统描述ID后，系统使用的SSN将发生改变，改变后的值由系统分配，见下。子系统描述ID 未配置使用的SSN 配置后使用的SSNSCCP      1  1    SPARE1    2  2    ISUP      3  3    OMAP      4  4    MAP       5  5    HLR       6  6    VLR       7  7    MSC       8  8    EIR       9  9    AUC       10 10   SPARE2    11 11   INAP      12 12   BSSOMAP   13 253 BSSAP     14 254 CSSP      15 146  CSCP      16 146  ISSP      17 12   ISCP      18 12   HSCP      19 147  RANAP     25 142 SGSN      26 149GGSN      27 150BSGSN     28 22 MSGSN     30 149 BVLR      31 21 MAPG      32 145  USSD      33 14
ID|编码计划配置标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|用来标识当前的编码计划配置，移动号码类型的编号计划和子系统类型的编号计划采用统一的编号，不可重复。也可以不输入特定的标识，这样系统会直接分配一个默认的标识。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


新增子系统类型的编码计划，设置子系统描述ID为SCCP，编码计划配置标识为13。 


ADD SSNPLAN:SSN="SCCP",ID=13; 








父主题： [编码计划配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改编码计划（子系统类型）(SET SSNPLAN) 
### 修改编码计划（子系统类型）(SET SSNPLAN) 


命令功能 

该命令用于修改子系统类型的编码计划。该修改命令只能修改用户别名。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
SSN|子系统描述ID|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|子系统描述ID为枚举型参数，列举了SCCP的子系统号不同取值对应上层应用的名称。增加特定的子系统描述ID后，系统使用的SSN将发生改变，改变后的值由系统分配，见下。子系统描述ID 未配置使用的SSN 配置后使用的SSNSCCP      1  1    SPARE1    2  2    ISUP      3  3    OMAP      4  4    MAP       5  5    HLR       6  6    VLR       7  7    MSC       8  8    EIR       9  9    AUC       10 10   SPARE2    11 11   INAP      12 12   BSSOMAP   13 253 BSSAP     14 254 CSSP      15 146  CSCP      16 146  ISSP      17 12   ISCP      18 12   HSCP      19 147  RANAP     25 142 SGSN      26 149GGSN      27 150BSGSN     28 22 MSGSN     30 149 BVLR      31 21 MAPG      32 145  USSD      33 14
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


修改子系统描述ID为SCCP的编码计划，设置用户别名为zte。 


SET SSNPLAN:SSN="SCCP",NAME="zte"; 








父主题： [编码计划配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除编码计划(DEL MPLAN) 
### 删除编码计划(DEL MPLAN) 


命令功能 

该命令用于删除编码计划。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
CATALOG|编码计划类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|编码计划类型为枚举型参数，用于选择当前命令是针对移动号码类型的配置项，还是针对子系统类型的配置项。
CTYPE|移动号码类型|参数可选性:必须单选参数；参数类型:枚举。参见枚举定义。|移动号码类型为枚举型参数，各个号码类型的含义如下：移动台ISDN号码（MSISDN）：MSISDN号码是指主叫客户为呼叫数字公用陆地蜂窝移动通信网中客户所需拨的号码。号码的结构为：CC+NDC+SN；CC=国家码；NDC=国内目的地码，即网路接入号；SN=客户号码，采用等长7位编号计划。国际移动客户识别码（IMSI）：为了在无线路径和整个GSM移动通信网上正确地识别某个移动客户，就必须给移动客户分配一个特定的识别码。这个识别码称为国际移动客户识别码（IMSI），用于移动通信网所有信令中。IMSI号码结构为：MCC+MNC+MSIN；MCC=移动国家号码，由3位数字组成，唯一地识别移动客户所属的国家；MNC=移动网号，由2-3位数字组成，用于识别移动客户所归属的移动网。MSIN=移动客户识别码，采用等长11位数字构成。唯一地识别国内移动通信网中移动客户。移动客户漫游号码（MSRN）：被叫客户所归属的HLR知道该客户目前是处于哪一个MSC/VLR业务区，为了提供给入口MSC/VLR（GMSC）一个用于选路由的临时号码，HLR请求被叫所在业务区的MSC/VLR给该被叫客户分配一个移动客户漫游号码（MSRN），并将此号码送至HLR，HLR收到后再发送给GMSC，GMSC根据此号码选路由，将呼叫接至被叫客户目前正在访问的MSC/VLR交换局。路由一旦建立，此号码就可立即释放。这种查询、呼叫选路由功能（即请求一个MSRN功能）是7号信令中移动应用部分（MAP）的一个程序，在GMSC—HLR—MSC/VLR间的7号信令网中进行传递。移动客户漫游号码（MSRN）结构是：CC+NDC+SN。临时移动客户识别码（TMSI）：为了对IMSI保密，MSC/VLR可给来访移动客户分配一个唯一的TMSI号码，即为一个由MSC自行分配的4字节的BCD编码，仅限在本MSC业务区内使用。全球小区识别码（CGI）：CGI是用来识别一个位置区内的小区，它是在位置区识别码 （LAI）后加上一个小区识别码（CI），其结构是：MCC+MNC+LAC+CI；CI是一个2字节BCD编码，由各MSC自定。基站识别码（BSIC）：BSIC是用于识别相邻国家的相邻基站的，为6bit编码，其结构是：NCC（3bit）+BCC（3bit）；NCC=国家色码，主要用来区分国界各侧的运营者。MSC号码：MSC号码在7号信令信息中使用，代表MSC的号码。结构是：CC+NDC+SN；可为其分配特定的号码。VLR号码：VLR号码在7号信令信息中使用，代表VLR的号码。结构是：CC+NDC+SN；可为其分配特定的号码。HLR号码：HLR号码在7号信令信息中使用，代表HLR的号码。结构是：CC+NDC+SN；可为其分配特定的号码。切换号码（HON）：HON是当进行移动交换局间切换时，为选择路由，由目标MSC（即切换要转移到的MSC）临时分配给移动客户的一个号码。此号码为MSRN号码的一部分。其他特殊号码（SPEC）：非上述号码类型的其他特殊号码。
SSN|子系统描述ID|参数可选性:必须单选参数；参数类型:枚举。参见枚举定义。|子系统描述ID为枚举型参数，列举了SCCP的子系统号不同取值对应上层应用的名称。增加特定的子系统描述ID后，系统使用的SSN将发生改变，改变后的值由系统分配，见下。子系统描述ID 未配置使用的SSN 配置后使用的SSNSCCP      1  1    SPARE1    2  2    ISUP      3  3    OMAP      4  4    MAP       5  5    HLR       6  6    VLR       7  7    MSC       8  8    EIR       9  9    AUC       10 10   SPARE2    11 11   INAP      12 12   BSSOMAP   13 253 BSSAP     14 254 CSSP      15 146  CSCP      16 146  ISSP      17 12   ISCP      18 12   HSCP      19 147  RANAP     25 142 SGSN      26 149GGSN      27 150BSGSN     28 22 MSGSN     30 149 BVLR      31 21 MAPG      32 145  USSD      33 14






命令举例 


删除编码计划类型为移动号码类型、移动号码类型为ISDN的编码计划。 


DEL MPLAN:CATALOG="MC",CTYPE="ISDN"; 








父主题： [编码计划配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询编码计划(SHOW MPLAN) 
### 查询编码计划(SHOW MPLAN) 


命令功能 

该命令用于查询编码计划，包括移动号码类型的编码计划和子系统类型的编码计划。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
ID|编码计划配置标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|用来标识当前的编码计划配置，移动号码类型的编号计划和子系统类型的编号计划采用统一的编号，不可重复。也可以不输入特定的标识，这样系统会直接分配一个默认的标识。
CATALOG|编码计划类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编码计划类型为枚举型参数，用于选择当前命令是针对移动号码类型的配置项，还是针对子系统类型的配置项。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|编码计划配置标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|用来标识当前的编码计划配置，移动号码类型的编号计划和子系统类型的编号计划采用统一的编号，不可重复。也可以不输入特定的标识，这样系统会直接分配一个默认的标识。
CATALOG|编码计划类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编码计划类型为枚举型参数，用于选择当前命令是针对移动号码类型的配置项，还是针对子系统类型的配置项。
CTYPE|移动号码类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|移动号码类型为枚举型参数，各个号码类型的含义如下：移动台ISDN号码（MSISDN）：MSISDN号码是指主叫客户为呼叫数字公用陆地蜂窝移动通信网中客户所需拨的号码。号码的结构为：CC+NDC+SN；CC=国家码；NDC=国内目的地码，即网路接入号；SN=客户号码，采用等长7位编号计划。国际移动客户识别码（IMSI）：为了在无线路径和整个GSM移动通信网上正确地识别某个移动客户，就必须给移动客户分配一个特定的识别码。这个识别码称为国际移动客户识别码（IMSI），用于移动通信网所有信令中。IMSI号码结构为：MCC+MNC+MSIN；MCC=移动国家号码，由3位数字组成，唯一地识别移动客户所属的国家；MNC=移动网号，由2-3位数字组成，用于识别移动客户所归属的移动网。MSIN=移动客户识别码，采用等长11位数字构成。唯一地识别国内移动通信网中移动客户。移动客户漫游号码（MSRN）：被叫客户所归属的HLR知道该客户目前是处于哪一个MSC/VLR业务区，为了提供给入口MSC/VLR（GMSC）一个用于选路由的临时号码，HLR请求被叫所在业务区的MSC/VLR给该被叫客户分配一个移动客户漫游号码（MSRN），并将此号码送至HLR，HLR收到后再发送给GMSC，GMSC根据此号码选路由，将呼叫接至被叫客户目前正在访问的MSC/VLR交换局。路由一旦建立，此号码就可立即释放。这种查询、呼叫选路由功能（即请求一个MSRN功能）是7号信令中移动应用部分（MAP）的一个程序，在GMSC—HLR—MSC/VLR间的7号信令网中进行传递。移动客户漫游号码（MSRN）结构是：CC+NDC+SN。临时移动客户识别码（TMSI）：为了对IMSI保密，MSC/VLR可给来访移动客户分配一个唯一的TMSI号码，即为一个由MSC自行分配的4字节的BCD编码，仅限在本MSC业务区内使用。全球小区识别码（CGI）：CGI是用来识别一个位置区内的小区，它是在位置区识别码 （LAI）后加上一个小区识别码（CI），其结构是：MCC+MNC+LAC+CI；CI是一个2字节BCD编码，由各MSC自定。基站识别码（BSIC）：BSIC是用于识别相邻国家的相邻基站的，为6bit编码，其结构是：NCC（3bit）+BCC（3bit）；NCC=国家色码，主要用来区分国界各侧的运营者。MSC号码：MSC号码在7号信令信息中使用，代表MSC的号码。结构是：CC+NDC+SN；可为其分配特定的号码。VLR号码：VLR号码在7号信令信息中使用，代表VLR的号码。结构是：CC+NDC+SN；可为其分配特定的号码。HLR号码：HLR号码在7号信令信息中使用，代表HLR的号码。结构是：CC+NDC+SN；可为其分配特定的号码。切换号码（HON）：HON是当进行移动交换局间切换时，为选择路由，由目标MSC（即切换要转移到的MSC）临时分配给移动客户的一个号码。此号码为MSRN号码的一部分。其他特殊号码（SPEC）：非上述号码类型的其他特殊号码。
SSN|子系统描述ID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|子系统描述ID为枚举型参数，列举了SCCP的子系统号不同取值对应上层应用的名称。增加特定的子系统描述ID后，系统使用的SSN将发生改变，改变后的值由系统分配，见下。子系统描述ID 未配置使用的SSN 配置后使用的SSNSCCP      1  1    SPARE1    2  2    ISUP      3  3    OMAP      4  4    MAP       5  5    HLR       6  6    VLR       7  7    MSC       8  8    EIR       9  9    AUC       10 10   SPARE2    11 11   INAP      12 12   BSSOMAP   13 253 BSSAP     14 254 CSSP      15 146  CSCP      16 146  ISSP      17 12   ISCP      18 12   HSCP      19 147  RANAP     25 142 SGSN      26 149GGSN      27 150BSGSN     28 22 MSGSN     30 149 BVLR      31 21 MAPG      32 145  USSD      33 14
PLAN|编码计划|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编码计划为枚举型参数，列举了各种可能的编码计划，即号码的编码格式；移动网络中主要使用的有两种：电话编号计划（ISDN）即E.164编号计划；以及陆地移动编号计划（PLMN）即E.212编号计划。
ADDR|地址种类|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|地址种类为枚举类型，列举了地址的不同属性。说明如下：INTL: 国际号码NAT: 国内有效号码NET: 网络号码USER: 用户号码ABBR: 小号码
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


查询编码计划为1的配置。 


SHOW MPLAN:ID=1; 


`

 命令 （No.1）: SHOW MPLAN:ID=1;

操作维护  编码计划配置标识   编码计划类型        移动号码类型           子系统描述ID   编码计划           地址种类       用户别名
---------------------------------------------------------------------------------------------------------------------------------
删除      1                  移动号码类型        移动用户ISDN号码                      电话编号计划       国际号码       MPLAN1
---------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.062 秒）。
` 








父主题： [编码计划配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# QoS配置 
# QoS配置 


背景知识 


SGSN对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


PDP上下文使用的QoS来源于UE请求的QoS，签约的QoS和SGSN上配置的QoS策略。 



 

请求QoS，指UE希望得到的QoS，UE在激活PDP上下文请求或修改PDP上下文请求消息中携带。
 

 

签约QoS，指能得到的QoS的上限，在HLR中签约确定。
 

 

SGSN上配置的QoS策略，包括默认QoS配置、分级服务配置、IMSI号段QoS上限配置、IMSI号段签约QoS提升配置、GGSN网段QoS版本上限配置、Smart QoS配置。
 

 


MME对每个承载上下文，需要提供QoS（Quality of Service，服务质量）。 


4G接入时，使用的是R8 QoS，而2G/3G接入时，使用的是Pre-R8 QoS。R8 QoS和Pre-R8 QoS参数形式完全不一样。R8 QoS中含有QCI（QoS Class Identifier，QoS等级标识）。QCI 是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。 


3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。 


QCI的取值为1-255，除了9个标准QCI，其他QCI称为扩展QCI，可以由运营商自定义。 


当具有2G/3G/4G能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup、从4G移动到2G/3G时，需要把R8 QoS转换为Pre R8 QoS。 




功能描述 


QoS配置中，SGSN和MME相关的配置说明如下： 



 

对于SGSN网元，配置SGSN本地的QoS策略控制，包括默认QoS配置、DSCP映射配置、PFI映射配置、分级服务配置、IMSI号段QoS上限配置、IMSI号段签约QoS提升配置、GGSN网段QoS版本上限配置、Smart QoS配置。
 

 

对于MME配置，只需要配置MME映射Pre-R8 QoS策略，包括PFI映射配置、QoS转换时的默认Pre-R8 QoS参数、QCI相关配置。
 

 




相关主题 



 

SGSN QoS配置
 

 

MME QoS配置
 

 

公共QoS配置
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGSN QoS配置 
## SGSN QoS配置 


背景知识 


SGSN对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


PDP上下文使用的QoS来源于UE请求的QoS、签约的QoS和SGSN上配置的QoS策略。 



 

请求QoS，指UE希望得到的QoS，UE在激活PDP上下文请求或修改PDP上下文请求消息中携带。
 

 

签约QoS，指能得到的QoS的上限，在HLR中签约确定。
 

 

SGSN上配置的QoS策略，包括默认QoS配置、分级服务配置、QoS模板配置、IMSI号段QoS上限配置、IMSI号段签约QoS提升配置、GGSN网段QoS版本上限配置、Smart QoS配置、DSCP映射配置和PFI映射配置，其中DSCP映射配置和PFI映射配置为公共QoS配置的内容。
 

 




功能描述 


对于SGSN网元，需要配置SGSN本地的QoS策略控制，以便提供QoS功能。SGSN QoS配置包括默认QoS配置、分级服务配置、QoS模板配置、IMSI号段QoS上限配置、IMSI号段签约QoS提升配置、GGSN网段QoS版本上限配置和Smart QoS配置。 




相关主题 



 

默认QoS配置
 

 

分级服务配置
 

 

QoS模板配置
 

 

IMSI号段QoS上限配置
 

 

IMSI号段签约QoS提升配置
 

 

Smart QoS配置
 

 

RAB指派流程QoS配置
 

 

RAU流程QoS重协商和通知UE配置
 

 








父主题： [QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 默认QoS配置 
### 默认QoS配置 


背景知识 


SGSN对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


PDP上下文使用的QoS来源于UE请求的QoS，签约的QoS和SGSN上配置的QoS策略。 



 

请求QoS，指UE希望得到的QoS，UE在激活PDP上下文请求或修改PDP上下文请求消息中携带。
 

 

签约QoS，指能得到的QoS的上限，在HLR中签约确定。
 

 

SGSN上配置的QoS策略，包括分级服务配置、IMSI号段QoS上限配置、IMSI号段签约QoS提升配置、GGSN网段QoS版本上限配置、Smart QoS配置。
 

 




功能描述 


在如下场景下，需要使用默认QoS配置： 



 

用户通过Iu口接入时，请求的QoS为0，SGSN取默认QoS配置中的值作为请求QoS。
 

 

SGSN从HLR中获取的用户签约的QoS中携带了非法值，SGSN使用默认QoS配置中的值修正。
 

 

UE请求的QoS中携带了非法值，SGSN使用默认QoS配置中的值修正。
 

 


“默认QoS配置”已经自动生成缺省记录，维护人员可以根据需要修改。 




相关主题 



 

设置默认QoS(SET QOS DEFAULT)
 

 

设置默认QoS的所有参数回到缺省值(RESET QOS DEFAULT)
 

 

查询默认QoS(SHOW QOS DEFAULT)
 

 








父主题： [SGSN QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置默认QOS(SET QOS DEFAULT) 
#### 设置默认QOS(SET QOS DEFAULT) 


命令功能 


该命令用于配置SGSN网元本地默认的QoS参数。 


该命令用于解决由于终端带上来的请求QoS参数不规范或者HLR中签约的QoS参数不合理，导致用户PDP激活失败或影响用户后续使用PS业务等问题。 


QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在MS的PDP上下文中。在MS激活PDP上下文的时候，SGSN需要与MS进行QoS参数协商，如果协商失败，SGSN将拒绝用户接入。 


QoS各参数的取值及含义具体请参见3GPP TS 3GPP TS 23.107（QoS协议）。 


在UMTS网络中，MS最终使用的QoS参数是通过各网元共同协商出来的，涉及到MS请求的QoS、HLR中签约的QoS、SGSN提供的默认QoS、SGSN自身的资源情况和周边网元的QoS能力等。 


协商过程中涉及到以下几种QoS： 


请求的QoS：是指用户发起激活PDP上下文请求时要求的QoS。 


签约的QoS：是指HLR中关于用户的QoS签约信息。在用户附着网络后，HLR就把用户签约QoS信息下发给SGSN。 


默认QoS：是指在SGSN本地配置的QoS，当MS通过Iu模式接入时，未携带请求QoS，SGSN使用本地配置的默认QoS做为MS的请求QoS；或者当MS的请求QoS参数或HLR中签约的QoS参数不合法时，SGSN使用本地配置的默认QoS的数值对非法值进行修正。 


协商的QoS：是指SGSN比较用户请求的QoS、HLR签约的QoS以及SGSN自身的QoS能力与RNC、GGSN共同协商得出的最后结果。 


该命令用于解决由于终端带上来的请求QoS参数不规范或者HLR中签约的QoS参数不合理，导致用户PDP激活失败或影响用户后续使用PS业务等问题。 




注意事项 


该命令只适用于SGSN网元。 


通常情况下，SGSN按正常的QoS协商流程来决定MS最后使用的QoS，当通过本地维护终端的“[ADD IMSI QOSLMT]”命令，将“是否强制使用默认QoS”选择为“是”时，将使用本命令配置的默认QoS做为用户的协商QoS。


除此之外，该命令还受到安全变量“是否支持基于IMSI号段和接入类型控制QoS”（ID为786447）的影响，当此安全变量设置为：[SET SOFTWARE PARAMETER] :PARAID=786447,PARAVALUE=1时，SGSN将使用通过[ADD QOSTPL]命令配置QoS参数来进行QoS协商。


缺省情况下，系统已有默认配置。 




参数说明 


标识|名称|类型|说明
---|---|---|---
RELIACLASS|可靠级|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数与业务数据单元错误率（SDU error ratio） 、残余位出错率（Residual bit error ratio）和发送错误数据（Delivery of erroneous SDUs）参数的取值相关，它们的相互取值对应关系，详见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
DELAYCLASS|延迟级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与业务类别（Traffic class） 和流量控制优先级（Traffic handling priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
PRECECLASS|优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与缺省分配/保持优先级（Allocation/Retention priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP 23107(R7)和3GPP 24008(R7)。
PEAK|峰值吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的最大链路比特率。取值含义见协议3GPP 24008(R7)。
MEAN|平均吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的链路比特率的平均值。取值含义见协议3GPP 24008(R7)。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为：“NotDetect”：“不检测”，表示根本不考虑差错检测就进行传送。“Deliver”：“发送”，表示将检测出有错的SDU（Service Data Unit，业务数据单元）标以差错指示后进行传送。“NotDeliver”："不发送"，表示将检测出有错的SDU标以差错指示后进行丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN是否按照要求顺序传送SDU，需要根据3GPP 23017(R7)协议而定。取值含义：“Order”：按顺序发送。“NotOrder”：不按顺序发送。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大业务数据单元长度，用于许可控制。取值含义见协议3GPP 24008(R7)。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：“Conversational”：会话类型“Streaming”：流类型“Interactive”：交互类型“Background”：背景类型业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口上行链路码的预留。取值含义见协议3GPP 24008(R7)。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口下行链路码的预留。取值含义见协议3GPP 24008(R7)。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指丢失或者检测出差错SDU的比例，用来配置L2的重发协议和L1的检错编码。取值含义见协议3GPP 24008(R7)。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指在传送SDU中未检测到的误码率，用来配置L1的信道编码和检错编码。取值含义见协议3GPP 24008(R7)。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数的含义指对不同媒体的SDU处理的优先权。对于同一个承载业务，它和参数“保证上行链路比特率”和“保证下行链路比特率“不能同时出现。取值含义：“1”：优先级1。“2”：优先级2。“3”：优先级3。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指不同的用户有不同的延迟容忍程度。UTRAN（UMTS Terrestrial Radio Access Network，UMTS陆地无线接入网）可根据这一参数来设定传送格式和ARQ（Automatic Repeat reQuest，自动重传请求）参数。取值含义见协议3GPP 24008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
ARP|缺省分配/保持优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数的含义指对分配和保持UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）承载的优先权。取值含义：“1”：优先级1“2”：优先级2“3”：优先级3
DSCPUL|缺省上行DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数的含义指缺省上行DSCP（Differentiated Services Code Point,差分服务编码点）。取值含义见协议3GPP 24008(R7)
DSCPDL|缺省下行DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数的含义指缺省下行DSCP。取值含义见协议3GPP 24008(R7)。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数只用于交互级业务（Interactive）。即当“业务类别”设置为“交互业务（Interactive）”时才需要设置该参数。取值含义：“NotOptimized”：非最优化信令。“Optimized”：最优化信令。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数说明SDU数据源的特征。取值含义：“UnKnown”：未知。“Speech”：语音。如果设置为“语音”，RAN、SGSN、GGSN和UE可根据经验得出统计复用增益，用于许可控制。






命令举例 


设置默认QoS，传输类别为“Conversational”，最大上行链路比特率为“5056 kbps”，最大下行链路比特率为“4544 kbps”，传输时延为“150 ms”，保证上行链路比特率为“2880 kbps”，保证下行链路比特率为“2624 kbps”：  


SET QOS DEFAULT:TRAFFCLASS="Conversational",MAXBITRATEUL="5056 kbps",MAXBITRATEDL="4544 kbps",SDUERRRATIO="1e-5",RESIDUALBER="1e-3",TRANSDELAY="150 ms",GUARBITRATEUL="2880 kbps",GUARBITRATEDL="2624 kbps"; 








父主题： [默认QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置默认QOS的所有参数回到缺省值(RESET QOS DEFAULT) 
#### 设置默认QOS的所有参数回到缺省值(RESET QOS DEFAULT) 


命令功能 


该命令用于设置SGSN本地配置的默认QoS的所有参数回到缺省值。 


当设置的QoS参数的数值异常或者需要重新设置默认值时，可以使用该命令。 




注意事项 

无。


命令举例 


设置默认QoS的所有参数回到缺省值： 


RESET QOS DEFAULT 








父主题： [默认QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询默认QOS(SHOW QOS DEFAULT) 
#### 查询默认QOS(SHOW QOS DEFAULT) 


命令功能 


该命令用于查询默认QoS各个参数的配置值。 




注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
RELIACLASS|可靠级|参数可选性:任选参数；参数类型:整数。|该参数与业务数据单元错误率（SDU error ratio） 、残余位出错率（Residual bit error ratio）和发送错误数据（Delivery of erroneous SDUs）参数的取值相关，它们的相互取值对应关系，详见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
DELAYCLASS|延迟级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与业务类别（Traffic class） 和流量控制优先级（Traffic handling priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
PRECECLASS|优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与缺省分配/保持优先级（Allocation/Retention priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP 23107(R7)和3GPP 24008(R7)。
PEAK|峰值吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的最大链路比特率。取值含义见协议3GPP 24008(R7)。
MEAN|平均吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的链路比特率的平均值。取值含义见协议3GPP 24008(R7)。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为：“NotDetect”：“不检测”，表示根本不考虑差错检测就进行传送。“Deliver”：“发送”，表示将检测出有错的SDU（Service Data Unit，业务数据单元）标以差错指示后进行传送。“NotDeliver”："不发送"，表示将检测出有错的SDU标以差错指示后进行丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN是否按照要求顺序传送SDU，需要根据3GPP 23017(R7)协议而定。取值含义：“Order”：按顺序发送。“NotOrder”：不按顺序发送。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大业务数据单元长度，用于许可控制。取值含义见协议3GPP 24008(R7)。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：“Conversational”：会话类型“Streaming”：流类型“Interactive”：交互类型“Background”：背景类型业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口上行链路码的预留。取值含义见协议3GPP 24008(R7)。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口下行链路码的预留。取值含义见协议3GPP 24008(R7)。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指丢失或者检测出差错SDU的比例，用来配置L2的重发协议和L1的检错编码。取值含义见协议3GPP 24008(R7)。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指在传送SDU中未检测到的误码率，用来配置L1的信道编码和检错编码。取值含义见协议3GPP 24008(R7)。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数。|该参数的含义指对不同媒体的SDU处理的优先权。对于同一个承载业务，它和参数“保证上行链路比特率”和“保证下行链路比特率“不能同时出现。取值含义：“1”：优先级1。“2”：优先级2。“3”：优先级3。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指不同的用户有不同的延迟容忍程度。UTRAN（UMTS Terrestrial Radio Access Network，UMTS陆地无线接入网）可根据这一参数来设定传送格式和ARQ（Automatic Repeat reQuest，自动重传请求）参数。取值含义见协议3GPP 24008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
ARP|缺省分配/保持优先级|参数可选性:任选参数；参数类型:整数。|该参数的含义指对分配和保持UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）承载的优先权。取值含义：“1”：优先级1“2”：优先级2“3”：优先级3
DSCPUL|缺省上行DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义指缺省上行DSCP（Differentiated Services Code Point,差分服务编码点）。取值含义见协议3GPP 24008(R7)
DSCPDL|缺省下行DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义指缺省下行DSCP。取值含义见协议3GPP 24008(R7)。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数只用于交互级业务（Interactive）。即当“业务类别”设置为“交互业务（Interactive）”时才需要设置该参数。取值含义：“NotOptimized”：非最优化信令。“Optimized”：最优化信令。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数说明SDU数据源的特征。取值含义：“UnKnown”：未知。“Speech”：语音。如果设置为“语音”，RAN、SGSN、GGSN和UE可根据经验得出统计复用增益，用于许可控制。






命令举例 


查询所有默认QoS：  


SHOW QOS DEFAULT 


`

命令 (No.1): SHOW QOS DEFAULT

操作维护  可靠级   延迟级    优先级       峰值吞吐量       平均吞吐量         发送错误数据   发送顺序       最大业务数据单元长度   业务类别   最大上行链路比特率      最大下行链路比特率      业务数据单元错误率   残余位出错率     流量控制优先级   传输时延         保证上行链路比特率      保证下行链路比特率      缺省分配/保持优先级   缺省上行DSCP   缺省下行DSCP   信令指示       源统计描述器
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      3        延迟级1   普通优先级   8000 字节/秒     最佳效果           不检测         不按顺序发送   1502 字节 (151)        交互类型   128 千比特/秒 (72)      128 千比特/秒 (72)      万分之一 (4)         千分之四 (4)     1                                                                                 2                     0              0              非最优化信令   
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.12 秒）。
` 








父主题： [默认QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 分级服务配置 
### 分级服务配置 


背景知识 


ARP（Allocation/Retention Priority，分配/保留优先级），指分配和保持承载资源的优先权。 


在核心网侧，根据ARP可以把用户分为3类：VIP用户、普通用户、低优先级用户，相应地ARP取值为1-3，用户的ARP在HLR中签约。 


在无线侧，根据APR确定无线承载资源的分配和保留优先级，包括4个参数： 



 

优先级（Priority Level）：反映了申请的无线资源的接纳优先级和抢占优先级。取值范围是1～15，1的优先级最高。
 

 

抢占能力（Pre-emption Capability）：在拥塞时是否可以抢占其他低优先级承载的无线资源。
 

 

被抢占特性（Pre-emption Vulnerability）：在拥塞时是否可以被其他高优先级承载抢占无线资源。
 

 

是否允许排队（Queuing Allowed）：在拥塞时是否允许排队。
 

 


THP（Traffic handling priority，业务处理优先级），指对不同用户数据报文处理的优先级，仅对业务类型为“交互类"的承载上的用户数据报文有效。 


在核心网侧，THP取值为1-3，而在无线侧，取值范围是1～15，1的优先级最高。 




功能描述 


分级服务配置包括以下内容： 



 


                        根据核心网侧的ARP、接入类型、承载的业务类别，映射无线侧的ARP，映射规则全网规划，配置命令为：
                        ADD QOS PIE
                        。
                    
 

 


                        根据核心网侧的THP，映射无线侧的THP，映射规则全网规划，配置命令为：
                        ADD THP
                        。
                    
 

 


                        根据ARP，限制PDP的最大上下行速率，配置命令为：
                        ADD QOS USERRATE
                        。
                    
 

 




相关主题 



 

PIE参数配置
 

 

用户级别与最大上下行速率配置
 

 

THP配置
 

 








父主题： [SGSN QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### PIE参数配置 
#### PIE参数配置 


背景知识 


PIE（Priority Information Element，优先级信息），指用户优先级信息。 


在核心网侧，根据ARP（Allocation/Retention Priority，分配/保留优先级）可以把用户分为3类：VIP用户、普通用户、低优先级用户，相应地ARP取值为1、2、3，用户的ARP在HLR中签约。 


在无线侧，根据APR确定无线承载资源的分配和保留优先级，包括4个参数： 



 

优先级（Priority Level）：反映了申请的无线资源的接纳优先级和抢占优先级。取值范围是1～15，1的优先级最高。
 

 

抢占能力（Pre-emption Capability）：在拥塞时是否可以抢占其他低优先级承载的无线资源。
 

 

被抢占特性（Pre-emption Vulnerability）：在拥塞时是否可以被其他高优先级承载抢占无线资源。
 

 

是否允许排队（Queuing Allowed）：在拥塞时是否允许排队。
 

 




功能描述 


“PIE参数配置”根据核心网侧的ARP、接入类型、承载的业务类别，映射无线侧的ARP。该映射关系需要全网规划。 


该配置在以下场景使用： 



 

Iu接入，在RAB指派时需要映射无线侧的ARP。
 

 

Gb接入，在PFC(Packet Flow Control，分组流控制)建立时需要映射无线侧的ARP。
 

 


说明： 


“PIE参数配置”已经自动生成缺省记录，维护人员可以根据全网规划修改。 




相关主题 



 

新增用户级别与PIE参数配置(ADD QOS PIE)
 

 

修改用户级别与PIE参数配置(SET QOS PIE)
 

 

删除用户级别与PIE参数配置(DEL QOS PIE)
 

 

查询用户级别与PIE参数配置(SHOW QOS PIE)
 

 

新增IMSI段用户级别与PIE参数配置(ADD QOS PIE IMSI)
 

 

修改IMSI段用户级别与PIE参数配置(SET QOS PIE IMSI)
 

 

删除IMSI段用户级别与PIE参数配置(DEL QOS PIE IMSI)
 

 

查询IMSI段用户级别与PIE参数配置(SHOW QOS PIE IMSI)
 

 








父主题： [分级服务配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增用户级别与PIE参数配置(ADD QOS PIE) 
##### 新增用户级别与PIE参数配置(ADD QOS PIE) 


命令功能 

该命令用于增加用户级别与PIE参数配置，支持Iu接入和Gb接入两种方式，并且每种方式只能配置3类用户。


注意事项 


当呼叫优先级类别（PRIOLEVEL）不输入时，自动取如下默认值： 


用户类别（USERCLASS）=1时，呼叫优先级类别（PRIOLEVEL）=2； 


用户类别（USERCLASS）=2时，呼叫优先级类别（PRIOLEVEL）=6； 


 用户类别（USERCLASS）=3时，呼叫优先级类别（PRIOLEVEL）=12； 




参数说明 


标识|名称|类型|说明
---|---|---|---
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
ACCTYPE|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:Iu Access。|该参数是用来区分用户UE的无线侧接入类型。取值含义：“Iu Access”：Iu接入，表示UE通过RNC接入SGSN。“Gb Access”：Gb接入，表示UE通过BSC接入SGSN。
TRAFFICCLASS|传输类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:Null。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：“Conversational”：会话类型，主要应用于实时语音及视频业务。“Streaming”：流类型，主要用于承载实时数据流。“Interactive”：交互类型。“Background”：背景类型。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
PRIOLEVEL|呼叫优先级类别|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数是用来定义呼叫优先级类别。该参数取值范围是1～15之间的整数，1的优先级最高，15的优先级最低。当不设置“呼叫优先级类别（PRIOLEVEL）”时，系统采用如下默认值：当“用户类别（USERCLASS）”设置为“1”时，“呼叫优先级类别（PRIOLEVEL）”为“2”；当“用户类别（USERCLASS）”设置为“2”时，“呼叫优先级类别（PRIOLEVEL）”、为“6“；当”用户类别（USERCLASS）“设置为3时，”呼叫优先级类别（PRIOLEVEL）“为“12”；
PC|是否可抢占其他呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数的含义为在拥塞时是否可以抢占其他低优先级承载的无线资源。取值含义：“YES”：可以抢占其他呼叫。“NO”：不可抢占其他呼叫。
PV|是否允许被其他呼叫抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数的含义为在拥塞时是否可以被其他高优先级承载抢占无线资源。取值含义：“YES”：允许被其他呼叫抢占。“NO”：不允许被其他呼叫抢占。
QA|是否允许排队|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数的含义为是否允许排队。取值含义：“YES”：允许排队。“NO”：不允许排队。






命令举例 


增加用户级别与PIE参数配置，用户类别“1"，接入类型为“Iu接入"，传输类型为“会话类"：  


ADD QoS PIE:USERCLASS=1,ACCTYPE="Iu Access",TRAFFICCLASS="Conversational Class"; 








父主题： [PIE参数配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改用户级别与PIE参数配置(SET QOS PIE) 
##### 修改用户级别与PIE参数配置(SET QOS PIE) 


命令功能 

该命令用于修改用户级别与PIE参数配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
ACCTYPE|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数是用来区分用户UE的无线侧接入类型。取值含义：“Iu Access”：Iu接入，表示UE通过RNC接入SGSN。“Gb Access”：Gb接入，表示UE通过BSC接入SGSN。
TRAFFICCLASS|传输类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：“Conversational”：会话类型，主要应用于实时语音及视频业务。“Streaming”：流类型，主要用于承载实时数据流。“Interactive”：交互类型。“Background”：背景类型。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
PRIOLEVEL|呼叫优先级类别|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数是用来定义呼叫优先级类别。该参数取值范围是1～15之间的整数，1的优先级最高，15的优先级最低。当不设置“呼叫优先级类别（PRIOLEVEL）”时，系统采用如下默认值：当“用户类别（USERCLASS）”设置为“1”时，“呼叫优先级类别（PRIOLEVEL）”为“2”；当“用户类别（USERCLASS）”设置为“2”时，“呼叫优先级类别（PRIOLEVEL）”、为“6“；当”用户类别（USERCLASS）“设置为3时，”呼叫优先级类别（PRIOLEVEL）“为“12”；
PC|是否可抢占其他呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为在拥塞时是否可以抢占其他低优先级承载的无线资源。取值含义：“YES”：可以抢占其他呼叫。“NO”：不可抢占其他呼叫。
PV|是否允许被其他呼叫抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为在拥塞时是否可以被其他高优先级承载抢占无线资源。取值含义：“YES”：允许被其他呼叫抢占。“NO”：不允许被其他呼叫抢占。
QA|是否允许排队|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为是否允许排队。取值含义：“YES”：允许排队。“NO”：不允许排队。






命令举例 


修改用户级别与PIE参数配置，用户类别“1"，接入类型为“Iu接入"，传输类型为“会话类"：  


SET QoS PIE:USERCLASS=1,ACCTYPE="Iu Access",TRAFFICCLASS="Conversational Class"; 








父主题： [PIE参数配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除用户级别与PIE参数配置(DEL QOS PIE) 
##### 删除用户级别与PIE参数配置(DEL QOS PIE) 


命令功能 

该命令用于删除用户级别与PIE参数配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
ACCTYPE|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数是用来区分用户UE的无线侧接入类型。取值含义：“Iu Access”：Iu接入，表示UE通过RNC接入SGSN。“Gb Access”：Gb接入，表示UE通过BSC接入SGSN。
TRAFFICCLASS|传输类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：“Conversational”：会话类型，主要应用于实时语音及视频业务。“Streaming”：流类型，主要用于承载实时数据流。“Interactive”：交互类型。“Background”：背景类型。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。






命令举例 


删除用户级别与PIE参数配置，用户类别“1"，接入类型为“Iu接入"，传输类型为“会话类"：  


DEL QoS PIE:USERCLASS=1,ACCTYPE="Iu Access",TRAFFICCLASS="Conversational Class"; 








父主题： [PIE参数配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询用户级别与PIE参数配置(SHOW QOS PIE) 
##### 查询用户级别与PIE参数配置(SHOW QOS PIE) 


命令功能 

该命令用于查询用户级别与PIE参数配置。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
USERCLASS|用户类别|参数可选性:任选参数；参数类型:整数。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
ACCTYPE|接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是用来区分用户UE的无线侧接入类型。取值含义：“Iu Access”：Iu接入，表示UE通过RNC接入SGSN。“Gb Access”：Gb接入，表示UE通过BSC接入SGSN。
TRAFFICCLASS|传输类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：“Conversational”：会话类型，主要应用于实时语音及视频业务。“Streaming”：流类型，主要用于承载实时数据流。“Interactive”：交互类型。“Background”：背景类型。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
PRIOLEVEL|呼叫优先级类别|参数可选性:任选参数；参数类型:整数。|该参数是用来定义呼叫优先级类别。该参数取值范围是1～15之间的整数，1的优先级最高，15的优先级最低。当不设置“呼叫优先级类别（PRIOLEVEL）”时，系统采用如下默认值：当“用户类别（USERCLASS）”设置为“1”时，“呼叫优先级类别（PRIOLEVEL）”为“2”；当“用户类别（USERCLASS）”设置为“2”时，“呼叫优先级类别（PRIOLEVEL）”、为“6“；当”用户类别（USERCLASS）“设置为3时，”呼叫优先级类别（PRIOLEVEL）“为“12”；
PC|是否可抢占其他呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为在拥塞时是否可以抢占其他低优先级承载的无线资源。取值含义：“YES”：可以抢占其他呼叫。“NO”：不可抢占其他呼叫。
PV|是否允许被其他呼叫抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为在拥塞时是否可以被其他高优先级承载抢占无线资源。取值含义：“YES”：允许被其他呼叫抢占。“NO”：不允许被其他呼叫抢占。
QA|是否允许排队|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为是否允许排队。取值含义：“YES”：允许排队。“NO”：不允许排队。






命令举例 


查询用户级别与PIE参数配置：  


SHOW QoS PIE 


`

命令 (No.1): SHOW QOS PIE

操作维护         用户类别   接入类型   传输类型   呼叫优先级类别   是否可抢占其他呼叫   是否允许被其他呼叫抢占   是否允许排队
-----------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1          Iu接入     会话类     2                可以抢占其他呼叫     不允许被其他呼叫抢占     允许排队
-----------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.055 秒）。
` 








父主题： [PIE参数配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增IMSI段用户级别与PIE参数配置(ADD QOS PIE IMSI) 
##### 新增IMSI段用户级别与PIE参数配置(ADD QOS PIE IMSI) 


命令功能 

该命令用于增加IMSI段用户级别与PIE参数配置，支持Iu接入和Gb接入两种方式，并且每种方式只能配置3类用户。


注意事项 


当呼叫优先级类别（PRIOLEVEL）不输入时，自动取如下默认值： 


用户类别（USERCLASS）=1时，呼叫优先级类别（PRIOLEVEL）=2； 


用户类别（USERCLASS）=2时，呼叫优先级类别（PRIOLEVEL）=6； 


 用户类别（USERCLASS）=3时，呼叫优先级类别（PRIOLEVEL）=12； 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
ACCTYPE|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:Iu Access。|该参数是用来区分用户UE的无线侧接入类型。取值含义：“Iu Access”：Iu接入，表示UE通过RNC接入SGSN。“Gb Access”：Gb接入，表示UE通过BSC接入SGSN。
TRAFFICCLASS|传输类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:Null。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：“Conversational”：会话类型，主要应用于实时语音及视频业务。“Streaming”：流类型，主要用于承载实时数据流。“Interactive”：交互类型。“Background”：背景类型。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
PRIOLEVEL|呼叫优先级类别|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数是用来定义呼叫优先级类别。该参数取值范围是1～15之间的整数，1的优先级最高，15的优先级最低。当不设置“呼叫优先级类别（PRIOLEVEL）”时，系统采用如下默认值：当“用户类别（USERCLASS）”设置为“1”时，“呼叫优先级类别（PRIOLEVEL）”为“2”；当“用户类别（USERCLASS）”设置为“2”时，“呼叫优先级类别（PRIOLEVEL）”、为“6“；当”用户类别（USERCLASS）“设置为3时，”呼叫优先级类别（PRIOLEVEL）“为“12”；
PC|是否可抢占其他呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数的含义为在拥塞时是否可以抢占其他低优先级承载的无线资源。取值含义：“YES”：可以抢占其他呼叫。“NO”：不可抢占其他呼叫。
PV|是否允许被其他呼叫抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数的含义为在拥塞时是否可以被其他高优先级承载抢占无线资源。取值含义：“YES”：允许被其他呼叫抢占。“NO”：不允许被其他呼叫抢占。
QA|是否允许排队|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数的含义为是否允许排队。取值含义：“YES”：允许排队。“NO”：不允许排队。






命令举例 


增加IMSI段用户级别与PIE参数配置，IMSI号段为“46001"，用户类别“1"，接入类型为“Iu接入"，传输类型为“会话类"：  


ADD QoS PIE IMSI:IMSI="46001",USERCLASS=1,ACCTYPE="Iu Access",TRAFFICCLASS="Conversational Class"; 








父主题： [PIE参数配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改IMSI段用户级别与PIE参数配置(SET QOS PIE IMSI) 
##### 修改IMSI段用户级别与PIE参数配置(SET QOS PIE IMSI) 


命令功能 

该命令用于修改IMSI段用户级别与PIE参数配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
ACCTYPE|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数是用来区分用户UE的无线侧接入类型。取值含义：“Iu Access”：Iu接入，表示UE通过RNC接入SGSN。“Gb Access”：Gb接入，表示UE通过BSC接入SGSN。
TRAFFICCLASS|传输类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：“Conversational”：会话类型，主要应用于实时语音及视频业务。“Streaming”：流类型，主要用于承载实时数据流。“Interactive”：交互类型。“Background”：背景类型。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
PRIOLEVEL|呼叫优先级类别|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数是用来定义呼叫优先级类别。该参数取值范围是1～15之间的整数，1的优先级最高，15的优先级最低。当不设置“呼叫优先级类别（PRIOLEVEL）”时，系统采用如下默认值：当“用户类别（USERCLASS）”设置为“1”时，“呼叫优先级类别（PRIOLEVEL）”为“2”；当“用户类别（USERCLASS）”设置为“2”时，“呼叫优先级类别（PRIOLEVEL）”、为“6“；当”用户类别（USERCLASS）“设置为3时，”呼叫优先级类别（PRIOLEVEL）“为“12”；
PC|是否可抢占其他呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为在拥塞时是否可以抢占其他低优先级承载的无线资源。取值含义：“YES”：可以抢占其他呼叫。“NO”：不可抢占其他呼叫。
PV|是否允许被其他呼叫抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为在拥塞时是否可以被其他高优先级承载抢占无线资源。取值含义：“YES”：允许被其他呼叫抢占。“NO”：不允许被其他呼叫抢占。
QA|是否允许排队|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为是否允许排队。取值含义：“YES”：允许排队。“NO”：不允许排队。






命令举例 


修改IMSI段用户级别与PIE参数配置，IMSI号段为“46001"，用户类别“1"，接入类型为“Iu接入"，传输类型为“会话类"：  


SET QoS PIE IMSI:IMSI="46001",USERCLASS=1,ACCTYPE="Iu Access",TRAFFICCLASS="Conversational Class"; 








父主题： [PIE参数配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除IMSI段用户级别与PIE参数配置(DEL QOS PIE IMSI) 
##### 删除IMSI段用户级别与PIE参数配置(DEL QOS PIE IMSI) 


命令功能 

该命令用于删除IMSI段用户级别与PIE参数配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
ACCTYPE|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数是用来区分用户UE的无线侧接入类型。取值含义：“Iu Access”：Iu接入，表示UE通过RNC接入SGSN。“Gb Access”：Gb接入，表示UE通过BSC接入SGSN。
TRAFFICCLASS|传输类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：“Conversational”：会话类型，主要应用于实时语音及视频业务。“Streaming”：流类型，主要用于承载实时数据流。“Interactive”：交互类型。“Background”：背景类型。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。






命令举例 


删除IMSI段用户级别与PIE参数配置，IMSI号段为“46001"，用户类别“1"，接入类型为“Iu接入"，传输类型为“会话类"：  


DEL QoS PIE IMSI:IMSI="46001",USERCLASS=1,ACCTYPE="Iu Access",TRAFFICCLASS="Conversational Class"; 








父主题： [PIE参数配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询IMSI段用户级别与PIE参数配置(SHOW QOS PIE IMSI) 
##### 查询IMSI段用户级别与PIE参数配置(SHOW QOS PIE IMSI) 


命令功能 

该命令用于查询IMSI段用户级别与PIE参数配置。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
USERCLASS|用户类别|参数可选性:任选参数；参数类型:整数。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
ACCTYPE|接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是用来区分用户UE的无线侧接入类型。取值含义：“Iu Access”：Iu接入，表示UE通过RNC接入SGSN。“Gb Access”：Gb接入，表示UE通过BSC接入SGSN。
TRAFFICCLASS|传输类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：“Conversational”：会话类型，主要应用于实时语音及视频业务。“Streaming”：流类型，主要用于承载实时数据流。“Interactive”：交互类型。“Background”：背景类型。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
PRIOLEVEL|呼叫优先级类别|参数可选性:任选参数；参数类型:整数。|该参数是用来定义呼叫优先级类别。该参数取值范围是1～15之间的整数，1的优先级最高，15的优先级最低。当不设置“呼叫优先级类别（PRIOLEVEL）”时，系统采用如下默认值：当“用户类别（USERCLASS）”设置为“1”时，“呼叫优先级类别（PRIOLEVEL）”为“2”；当“用户类别（USERCLASS）”设置为“2”时，“呼叫优先级类别（PRIOLEVEL）”、为“6“；当”用户类别（USERCLASS）“设置为3时，”呼叫优先级类别（PRIOLEVEL）“为“12”；
PC|是否可抢占其他呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为在拥塞时是否可以抢占其他低优先级承载的无线资源。取值含义：“YES”：可以抢占其他呼叫。“NO”：不可抢占其他呼叫。
PV|是否允许被其他呼叫抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为在拥塞时是否可以被其他高优先级承载抢占无线资源。取值含义：“YES”：允许被其他呼叫抢占。“NO”：不允许被其他呼叫抢占。
QA|是否允许排队|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为是否允许排队。取值含义：“YES”：允许排队。“NO”：不允许排队。






命令举例 


查询IMSI段用户级别与PIE参数配置：  


SHOW QoS PIE IMSI 


`

命令 (No.1): SHOW QOS PIE IMSI

操作维护         IMSI号段   用户类别   接入类型   传输类型   呼叫优先级类别   是否可抢占其他呼叫   是否允许被其他呼叫抢占   是否允许排队
----------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   46001      1          Iu接入     会话类     2                可以抢占其他呼叫     不允许被其他呼叫抢占     允许排队
----------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.055 秒）。
` 








父主题： [PIE参数配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 用户级别与最大上下行速率配置 
#### 用户级别与最大上下行速率配置 


背景知识 


在核心网侧，根据ARP（Allocation/Retention Priority，分配/保留优先级）可以把用户分为3类：VIP用户、普通用户、低优先级用户，相应地ARP取值为1、2、3，用户的ARP在HLR中签约。 


对于每一类用户，可以限制其最大上下行速率，特别是对低优先级用户。 


在激活、二次激活过程中，SGSN根据用户类别，限制PDP使用QoS中的MBR（Maximun Bit Rate，最大比特速率）和GBR（Guaranteed Bit Rate保证的比特速率）的值。 




功能描述 


为了避免单个用户对网络资源占用过多，可以根据用户类别需要限制最大上下行速率，特别是对低优先级用户设置最大上下行速率，保证高等级用户的服务质量。
配置用户级别与最大上下行速率后，对应等级用户的每个PDP的最大上下行速率都不会超过配置的速率。 




相关主题 



 

新增用户级别与最大上下行速率配置(ADD QOS USERRATE)
 

 

修改用户级别与最大上下行速率配置(SET QOS USERRATE)
 

 

删除用户级别与最大上下行速率配置(DEL QOS USERRATE)
 

 

查询用户级别与最大上下行速率配置(SHOW QOS USERRATE)
 

 








父主题： [分级服务配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增用户级别与最大上下行速率配置(ADD QOS USERRATE) 
##### 新增用户级别与最大上下行速率配置(ADD QOS USERRATE) 


命令功能 

该命令用于增加用户级别与最大上下行速率配置。


注意事项 

目前区分为三类用户，只能增加三条记录。


参数说明 


标识|名称|类型|说明
---|---|---|---
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:128 kbps。|该参数的含义是为了便于无线接口上行链路码的预留。取值含义见协议3GPP 24008(R7)。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:128 kbps。|该参数的含义是为了便于无线接口下行链路码的预留。取值含义见协议3GPP 24008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:128 kbps。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:128 kbps。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。






命令举例 


增加用户级别与最大上下行速率配置，用户类别“1"，最大上行链路比特率为“128 kbps"，最大下行链路比特率为“128 kbps"： 
ADD QoS USERRATE:USERCLASS=1,MAXBITRATEUL="128 kbps",MAXBITRATEDL="128 kbps"; 








父主题： [用户级别与最大上下行速率配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改用户级别与最大上下行速率配置(SET QOS USERRATE) 
##### 修改用户级别与最大上下行速率配置(SET QOS USERRATE) 


命令功能 

该命令用于修改用户级别与最大上下行速率配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口上行链路码的预留。取值含义见协议3GPP 24008(R7)。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口下行链路码的预留。取值含义见协议3GPP 24008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。






命令举例 


修改用户级别与最大上下行速率配置，用户类别“1"，最大上行链路比特率为“400 kbps"：
SET QoS USERRATE:USERCLASS=1,MAXBITRATEUL="400 kbps"; 








父主题： [用户级别与最大上下行速率配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除用户级别与最大上下行速率配置(DEL QOS USERRATE) 
##### 删除用户级别与最大上下行速率配置(DEL QOS USERRATE) 


命令功能 

该命令用于删除用户级别与最大上下行速率配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
USERCLASS|用户类别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。






命令举例 


删除用户级别与最大上下行速率配置，用户类别“1"： 
DEL QoS USERRATE:USERCLASS=1; 








父主题： [用户级别与最大上下行速率配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询用户级别与最大上下行速率配置(SHOW QOS USERRATE) 
##### 查询用户级别与最大上下行速率配置(SHOW QOS USERRATE) 


命令功能 

该命令用于查询用户级别与最大上下行速率配置。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
USERCLASS|用户类别|参数可选性:任选参数；参数类型:整数。|该参数用来表示用户签约的ARP级别，可以将用户分为三个级别：VIP用户（HighLevelUser）：ARP签约为1。普通用户（NormalUser）：ARP签约为2。低端用户（LowLevelUser）：ARP签约为3。其中1优先级最高，3优先级最低。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口上行链路码的预留。取值含义见协议3GPP 24008(R7)。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口下行链路码的预留。取值含义见协议3GPP 24008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。






命令举例 


查询用户级别与最大上下行速率配置：
SHOW QoS USERRATE 


`

命令 (No.2): SHOW QOS USERRATE

操作维护         用户类别   最大上行链路比特率      最大下行链路比特率      保证上行链路比特率      保证下行链路比特率
----------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1          128 千比特/秒 (72)      128 千比特/秒 (72)      128 千比特/秒 (72)      128 千比特/秒 (72)
----------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.051 秒）。
` 








父主题： [用户级别与最大上下行速率配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### THP配置 
#### THP配置 


背景知识 


THP（Traffic handling priority，业务处理优先级），指对不同用户数据报文处理的优先级，仅对业务类型为“交互类”的承载上的用户数据报文有效。 


在核心网侧，THP取值为1～3，而在无线侧，取值范围是1～15，1的优先级最高，15表示无优先级，一般不使用。 


在激活、二次激活、重定位流程中，SGSN通过和RNC的消息交互把用户的THP携带给RNC，由于核心网侧THP和无线侧THP的取值范围不同，SGSN需要把核心网侧的THP映射为无线侧的THP，映射规则全网统一规划。 




功能描述 


”THP配置“用于设置核心网侧THP和无线侧THP的映射关系。该映射关系需要全网规划。 


核心网侧THP的值1、2、3，都需要映射为无线侧的THP。无线测THP取值范围是1～15，但15表示无优先级，一般不使用，因此映射为无线侧的THP时，取值范围为1～14。 


说明： 


“THP配置”已经自动生成缺省记录，维护人员可以根据全网规划修改。 




相关主题 



 

新增THP配置(ADD THP)
 

 

修改THP配置(SET THP)
 

 

删除THP配置(DEL THP)
 

 

查询THP配置(SHOW THP)
 

 








父主题： [分级服务配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增THP配置(ADD THP) 
##### 新增THP配置(ADD THP) 


命令功能 


THP（Traffic Handling Priority，业务处理优先级）是QoS参数中的一种。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。 


THP表示系统对不同用户数据报文处理的优先级，仅对QoS业务类型为“交互类”的用户数据报文有效。 


在MS激活PDP上下文的时候，SGSN需要与MS进行QoS参数协商。如果在协商QoS为交互类的情况下，SGSN在后续发送RAB Assignment Request或Relocation Request消息给RNC时，SGSN根据协商QoS中THP映射出一个THP值带给RNC，让RNC合理分配资源。 


在核心网侧协商的QoS，对应的THP的取值范围为1~3，在无线侧SGSN带给RNC的THP，其取值范围是1～15，两种情况下，都是1的优先级最高。 


因为核心网侧的THP和无线侧的THP取值范围不同，系统需要把核心网侧的THP映射为无线侧的THP。使用此命令配置两者之间的映射关系，即将每个协商QoS中THP值配置对应一个由SGSN带给RNC的THP值。 




注意事项 


该命令只适用于SGSN网元。如果不配置该命令，THP的映射关系为系统默认值，具体情况如下： 


当协商QoS的THP值为1（Priority level 1）时，SGSN下发给RNC的THP值为1（highest）。 


当协商QoS的THP值为3（Priority level 3）时，SGSN下发给RNC的THP值为14（lowest）。 


当协商QoS的THP为2时，SGSN下发给RNC的THP值为2。 




参数说明 


标识|名称|类型|说明
---|---|---|---
PRIORITY|优先级别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数表示THP（Traffic Handling Priority，业务处理优先级），是QoS参数中的一种。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。THP表示系统对不同用户数据报文处理的优先级，仅对QoS业务类型为“交互类”的用户数据报文有效。该参数包括以下三个取值：THP值为1（Priority level 1）THP值为2（Priority level 2）THP值为3（Priority level 3）其中，1的优先级最高。
THP|THP值|参数可选性:必选参数；参数类型:整数；参数范围为:1~14。|SGSN在发送RAB Assignment Request或Relocation Request消息给RNC时，SGSN根据协商QoS中THP映射出一个THP值带给RNC，让RNC合理分配资源。此参数表示由协商QoS中THP的映射的THP。






命令举例 


新增THP映射配置，优先级别（即协商QoS中的THP值）为1，RAB参数中的THP值为1。 


ADD THP:PRIORITY=1,THP=1; 








父主题： [THP配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改THP配置(SET THP) 
##### 修改THP配置(SET THP) 


命令功能 

该命令用于修改THP映射配置。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
PRIORITY|优先级别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数表示THP（Traffic Handling Priority，业务处理优先级），是QoS参数中的一种。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。THP表示系统对不同用户数据报文处理的优先级，仅对QoS业务类型为“交互类”的用户数据报文有效。该参数包括以下三个取值：THP值为1（Priority level 1）THP值为2（Priority level 2）THP值为3（Priority level 3）其中，1的优先级最高。
THP|THP值|参数可选性:任选参数；参数类型:整数；参数范围为:1~14。|SGSN在发送RAB Assignment Request或Relocation Request消息给RNC时，SGSN根据协商QoS中THP映射出一个THP值带给RNC，让RNC合理分配资源。此参数表示由协商QoS中THP的映射的THP。






命令举例 


修改优先级别（即协商QoS中的THP值）为1的THP映射配置，将RAB参数中THP值修改为3。 


SET THP:PRIORITY=1,THP=3; 








父主题： [THP配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除THP配置(DEL THP) 
##### 删除THP配置(DEL THP) 


命令功能 

该命令用于删除THP映射配置。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
PRIORITY|优先级别|参数可选性:必选参数；参数类型:整数；参数范围为:1~3。|该参数表示THP（Traffic Handling Priority，业务处理优先级），是QoS参数中的一种。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。THP表示系统对不同用户数据报文处理的优先级，仅对QoS业务类型为“交互类”的用户数据报文有效。该参数包括以下三个取值：THP值为1（Priority level 1）THP值为2（Priority level 2）THP值为3（Priority level 3）其中，1的优先级最高。






命令举例 


删除优先级别（即协商QoS中的THP值）为1的THP映射配置。 


DEL THP:PRIORITY=1; 








父主题： [THP配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询THP配置(SHOW THP) 
##### 查询THP配置(SHOW THP) 


命令功能 


该命令用于查询THP映射配置。 


如果输入优先级别，表示查询该优先级别对应的THP映射配置。 


如果不输入查询参数，表示查询所有的THP映射配置。 




注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
PRIORITY|优先级别|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数表示THP（Traffic Handling Priority，业务处理优先级），是QoS参数中的一种。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。THP表示系统对不同用户数据报文处理的优先级，仅对QoS业务类型为“交互类”的用户数据报文有效。该参数包括以下三个取值：THP值为1（Priority level 1）THP值为2（Priority level 2）THP值为3（Priority level 3）其中，1的优先级最高。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
PRIORITY|优先级别|参数可选性:任选参数；参数类型:整数。|该参数表示THP（Traffic Handling Priority，业务处理优先级），是QoS参数中的一种。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。THP表示系统对不同用户数据报文处理的优先级，仅对QoS业务类型为“交互类”的用户数据报文有效。该参数包括以下三个取值：THP值为1（Priority level 1）THP值为2（Priority level 2）THP值为3（Priority level 3）其中，1的优先级最高。
THP|THP值|参数可选性:任选参数；参数类型:整数。|SGSN在发送RAB Assignment Request或Relocation Request消息给RNC时，SGSN根据协商QoS中THP映射出一个THP值带给RNC，让RNC合理分配资源。此参数表示由协商QoS中THP的映射的THP。






命令举例 


查询优先级别（即协商QoS中的THP值）为1的THP映射配置。 


SHOW THP:PRIORITY=1; 


`

命令 (No.1): SHOW THP:PRIORITY=1;

操作维护         优先级别   THP值
---------------------------------
复制 修改 删除   1          5
---------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [THP配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### QoS模板配置 
### QoS模板配置 


背景知识 


SGSN中，对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


PDP上下文使用的QoS可以根据UE请求QoS、签约QoS和SGSN策略得到。 



 

请求QoS：指UE希望得到的QoS，UE在激活PDP上下文请求或修改PDP上下文请求消息中携带。
 

 

签约QoS：指UE能得到的QoS的上限，在HLR中签约确定。
 

 

SGSN策略：SGSN网元配置的策略，根据UE的IMSI或IMSI号段、接入方式（Iu接入或Gb接入）、接入的RNC ID（Iu接入时），限制UE使用的QoS不能超过指定的QoS上限或直接使用本地指定的QoS。
 

 




功能描述 


在SGSN配置QoS策略的过程如下： 






配置QoS模板。由于多个IMSI号段使用的QoS策略可能相同，所以将QoS策略单独配置称为QoS模板。 







                        配置IMSI号段QoS上限配置（命令为：
                        [ADD IMSI QOSLMT]
                        ）。该配置中指定了IMSI号段和QoS模板号的关联关系。
                    








相关主题 



 

新增QoS模板配置(ADD QOSTPL)
 

 

修改QoS模板配置(SET QOSTPL)
 

 

删除QoS模板配置(DEL QOSTPL)
 

 

查询QoS模板配置(SHOW QOSTPL)
 

 








父主题： [SGSN QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增QOS模板配置(ADD QOSTPL) 
#### 新增QOS模板配置(ADD QOSTPL) 


命令功能 


该命令用于配置一个QoS模板，此模板定义了一组QoS参数的集合。 


配置此模板后，SGSN可以根据此模板定义的QoS参数来限制UE的QoS能力，详细内容参见[ADD IMSI QOSLMT]命令。




注意事项 


该命令只适用于SGSN网元。 


如果不配置该命令，系统采用默认的QoS模板。 




参数说明 


标识|名称|类型|说明
---|---|---|---
QOSID|QoS模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|ADD IMSI QOSLMT命令和SET IMSI QOSLMT DEFAULT命令中“IUQOS”和“GBQOS”这两个参数使用该标识来对应具体的QoS模板。
RELIACLASS|可靠级|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。默认值:3。|该参数与业务数据单元错误率（SDU error ratio）、残余位出错率（Residual bit error ratio）和发送错误数据（Delivery of erroneous SDUs）参数的取值相关，详见协议3GPP TS 24.008。
DELAYCLASS|延迟级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:Level 1。|该参数与业务类别（Traffic class）和流量控制优先级（Traffic handling priority）参数的取值相关，不同的取值有不同的对应关系，详见协议3GPP TS 24.008。
PRECECLASS|优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NORMAL。|该参数与缺省分配/保持优先级（Allocation/Retention priority）参数的取值相关，不同的取值有不同的对应关系，详见协议3GPP TS 24.008。
PEAK|峰值吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:8000 octet/s。|该参数的含义为SGSN可以处理的最大链路比特率，详见协议3GPP TS 24.008。
MEAN|平均吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BestEffort。|该参数的含义为SGSN可以处理的链路比特率的平均值，参见3GPP TS 24.008。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NotDetect。|该参数的含义详见协议3GPP TS 24.008，包括以下取值：“NotDetect”：“不检测”，表示根本不考虑差错检测就进行传送。“Deliver”：“发送”，表示将检测出有错的SDU（Service Data Unit，业务数据单元）标以差错指示后进行传送。“NotDeliver”："不发送"，表示将检测出有错的SDU标以差错指示后进行丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NotOrder。|该参数的含义为SGSN是否按照要求顺序传送SDU，需要根据3GPP TS 23.017(R7)协议而定。取值含义：“Order”：按顺序发送。“NotOrder”：不按顺序发送。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:1502 octets。|该参数的含义为最大SDU（Service Data Unit，业务数据单元）单元长度，用于许可控制。详见协议3GPP TS 24.008。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:Interactive。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:128 kbps。|该参数的含义是为了便于无线接口上行链路码的预留，详见协议3GPP TS 24.008。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:128 kbps。|该参数的含义是为了便于无线接口下行链路码的预留，详见协议3GPP TS 24.008。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:1e-4。|该参数的含义是指丢失或者检测出差错SDU的比例，用来配置L2的重发协议和L1的检错编码，详见协议3GPP TS 24.008。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:4e-3。|该参数的含义是指在传送SDU中未检测到的误码率，用来配置L1的信道编码和检错编码，详见协议3GPP TS 24.008。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数的含义指对不同媒体的SDU处理的优先权。对于同一个承载业务，它和参数“保证上行链路比特率”和“保证下行链路比特率“不能同时出现，详见协议3GPP TS 24.008。取值含义：“1”：优先级1。“2”：优先级2。“3”：优先级3。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指不同的用户有不同的延迟容忍程度。UTRAN（UMTS Terrestrial Radio Access Network，UMTS陆地无线接入网）可根据这一参数来设定传送格式和ARQ（Automatic Repeat reQuest，自动重传请求）参数。详见协议3GPP TS 24.008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配，详见协议3GPP TS 24.008。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配，详见协议3GPP TS 24.008。
ARP|缺省分配/保持优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。默认值:2。|该参数的含义指对分配和保持UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）承载的优先权，详见协议3GPP TS 24.008。取值含义：“1”：优先级1“2”：优先级2“3”：优先级31的优先级最高。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数只用于交互级业务（Interactive）。即当“业务类别”设置为“交互业务（Interactive）”时才需要设置该参数，详见协议3GPP TS 24.008。取值含义：“NotOptimized”：非最优化信令。“Optimized”：最优化信令，
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数说明SDU数据源的特征，详见协议3GPP TS 24.008。取值含义：“UnKnown”：未知。“Speech”：语音。如果设置为“语音”，RAN、SGSN、GGSN和UE可根据经验得出统计复用增益，用于许可控制。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


新增QOS模板配置，设置QoS模板标识为1，可靠级为3，延迟级为1级，优先级为普通优先级，流量控制优先级为2，其他参数使用默认值。 


ADD QOSTPL:QOSID=1,RELIACLASS=3,DELAYCLASS="Level 1",PRECECLASS="NORMAL",TRAFHANDPRIO=2; 








父主题： [QoS模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改QOS模板配置(SET QOSTPL) 
#### 修改QOS模板配置(SET QOSTPL) 


命令功能 

该命令用于根据指定的QoS模板修改其中定义的QoS参数。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
QOSID|QoS模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|ADD IMSI QOSLMT命令和SET IMSI QOSLMT DEFAULT命令中“IUQOS”和“GBQOS”这两个参数使用该标识来对应具体的QoS模板。
RELIACLASS|可靠级|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数与业务数据单元错误率（SDU error ratio）、残余位出错率（Residual bit error ratio）和发送错误数据（Delivery of erroneous SDUs）参数的取值相关，详见协议3GPP TS 24.008。
DELAYCLASS|延迟级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与业务类别（Traffic class）和流量控制优先级（Traffic handling priority）参数的取值相关，不同的取值有不同的对应关系，详见协议3GPP TS 24.008。
PRECECLASS|优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与缺省分配/保持优先级（Allocation/Retention priority）参数的取值相关，不同的取值有不同的对应关系，详见协议3GPP TS 24.008。
PEAK|峰值吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的最大链路比特率，详见协议3GPP TS 24.008。
MEAN|平均吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的链路比特率的平均值，参见3GPP TS 24.008。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义详见协议3GPP TS 24.008，包括以下取值：“NotDetect”：“不检测”，表示根本不考虑差错检测就进行传送。“Deliver”：“发送”，表示将检测出有错的SDU（Service Data Unit，业务数据单元）标以差错指示后进行传送。“NotDeliver”："不发送"，表示将检测出有错的SDU标以差错指示后进行丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN是否按照要求顺序传送SDU，需要根据3GPP TS 23.017(R7)协议而定。取值含义：“Order”：按顺序发送。“NotOrder”：不按顺序发送。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大SDU（Service Data Unit，业务数据单元）单元长度，用于许可控制。详见协议3GPP TS 24.008。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口上行链路码的预留，详见协议3GPP TS 24.008。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口下行链路码的预留，详见协议3GPP TS 24.008。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指丢失或者检测出差错SDU的比例，用来配置L2的重发协议和L1的检错编码，详见协议3GPP TS 24.008。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指在传送SDU中未检测到的误码率，用来配置L1的信道编码和检错编码，详见协议3GPP TS 24.008。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数的含义指对不同媒体的SDU处理的优先权。对于同一个承载业务，它和参数“保证上行链路比特率”和“保证下行链路比特率“不能同时出现，详见协议3GPP TS 24.008。取值含义：“1”：优先级1。“2”：优先级2。“3”：优先级3。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指不同的用户有不同的延迟容忍程度。UTRAN（UMTS Terrestrial Radio Access Network，UMTS陆地无线接入网）可根据这一参数来设定传送格式和ARQ（Automatic Repeat reQuest，自动重传请求）参数。详见协议3GPP TS 24.008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配，详见协议3GPP TS 24.008。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配，详见协议3GPP TS 24.008。
ARP|缺省分配/保持优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数的含义指对分配和保持UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）承载的优先权，详见协议3GPP TS 24.008。取值含义：“1”：优先级1“2”：优先级2“3”：优先级31的优先级最高。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数只用于交互级业务（Interactive）。即当“业务类别”设置为“交互业务（Interactive）”时才需要设置该参数，详见协议3GPP TS 24.008。取值含义：“NotOptimized”：非最优化信令。“Optimized”：最优化信令，
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数说明SDU数据源的特征，详见协议3GPP TS 24.008。取值含义：“UnKnown”：未知。“Speech”：语音。如果设置为“语音”，RAN、SGSN、GGSN和UE可根据经验得出统计复用增益，用于许可控制。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


修改QoS模板标识为1的QOS模板配置，将可靠级修改为3，延迟级修改为1级，优先级修改为普通优先级。 


SET QOSTPL:QOSID=1,RELIACLASS=3,DELAYCLASS="Level 1",PRECECLASS="NORMAL"; 








父主题： [QoS模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除QOS模板配置(DEL QOSTPL) 
#### 删除QOS模板配置(DEL QOSTPL) 


命令功能 

该命令用于删除指定的QoS模板。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
QOSID|QoS模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|ADD IMSI QOSLMT命令和SET IMSI QOSLMT DEFAULT命令中“IUQOS”和“GBQOS”这两个参数使用该标识来对应具体的QoS模板。






命令举例 


删除QoS模板标识为1的QOS模板配置。 


DEL QOSTPL:QOSID=1; 








父主题： [QoS模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询QOS模板配置(SHOW QOSTPL) 
#### 查询QOS模板配置(SHOW QOSTPL) 


命令功能 


该命令用于查询QoS模板中定义的QoS参数。 


如果输入QoS模板标识，表示查询该标识对应的QoS模板。 


如果不输入查询参数，表示查询所有的QoS模板。 




注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
QOSID|QoS模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|ADD IMSI QOSLMT命令和SET IMSI QOSLMT DEFAULT命令中“IUQOS”和“GBQOS”这两个参数使用该标识来对应具体的QoS模板。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
QOSID|QoS模板标识|参数可选性:任选参数；参数类型:整数。|ADD IMSI QOSLMT命令和SET IMSI QOSLMT DEFAULT命令中“IUQOS”和“GBQOS”这两个参数使用该标识来对应具体的QoS模板。
RELIACLASS|可靠级|参数可选性:任选参数；参数类型:整数。|该参数与业务数据单元错误率（SDU error ratio）、残余位出错率（Residual bit error ratio）和发送错误数据（Delivery of erroneous SDUs）参数的取值相关，详见协议3GPP TS 24.008。
DELAYCLASS|延迟级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与业务类别（Traffic class）和流量控制优先级（Traffic handling priority）参数的取值相关，不同的取值有不同的对应关系，详见协议3GPP TS 24.008。
PRECECLASS|优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与缺省分配/保持优先级（Allocation/Retention priority）参数的取值相关，不同的取值有不同的对应关系，详见协议3GPP TS 24.008。
PEAK|峰值吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的最大链路比特率，详见协议3GPP TS 24.008。
MEAN|平均吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的链路比特率的平均值，参见3GPP TS 24.008。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义详见协议3GPP TS 24.008，包括以下取值：“NotDetect”：“不检测”，表示根本不考虑差错检测就进行传送。“Deliver”：“发送”，表示将检测出有错的SDU（Service Data Unit，业务数据单元）标以差错指示后进行传送。“NotDeliver”："不发送"，表示将检测出有错的SDU标以差错指示后进行丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN是否按照要求顺序传送SDU，需要根据3GPP TS 23.017(R7)协议而定。取值含义：“Order”：按顺序发送。“NotOrder”：不按顺序发送。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大SDU（Service Data Unit，业务数据单元）单元长度，用于许可控制。详见协议3GPP TS 24.008。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。取值含义：会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口上行链路码的预留，详见协议3GPP TS 24.008。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口下行链路码的预留，详见协议3GPP TS 24.008。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指丢失或者检测出差错SDU的比例，用来配置L2的重发协议和L1的检错编码，详见协议3GPP TS 24.008。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指在传送SDU中未检测到的误码率，用来配置L1的信道编码和检错编码，详见协议3GPP TS 24.008。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数。|该参数的含义指对不同媒体的SDU处理的优先权。对于同一个承载业务，它和参数“保证上行链路比特率”和“保证下行链路比特率“不能同时出现，详见协议3GPP TS 24.008。取值含义：“1”：优先级1。“2”：优先级2。“3”：优先级3。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指不同的用户有不同的延迟容忍程度。UTRAN（UMTS Terrestrial Radio Access Network，UMTS陆地无线接入网）可根据这一参数来设定传送格式和ARQ（Automatic Repeat reQuest，自动重传请求）参数。详见协议3GPP TS 24.008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配，详见协议3GPP TS 24.008。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配，详见协议3GPP TS 24.008。
ARP|分配/保持优先级|参数可选性:任选参数；参数类型:整数。|该参数的含义指对分配和保持UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）承载的优先权，详见协议3GPP TS 24.008。取值含义：“1”：优先级1“2”：优先级2“3”：优先级31的优先级最高。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数只用于交互级业务（Interactive）。即当“业务类别”设置为“交互业务（Interactive）”时才需要设置该参数，详见协议3GPP TS 24.008。取值含义：“NotOptimized”：非最优化信令。“Optimized”：最优化信令，
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数说明SDU数据源的特征，详见协议3GPP TS 24.008。取值含义：“UnKnown”：未知。“Speech”：语音。如果设置为“语音”，RAN、SGSN、GGSN和UE可根据经验得出统计复用增益，用于许可控制。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


查询QoS模板标识为1的QOS模板配置。 


SHOW QOSTPL:QOSID=1; 


`

命令 (No.1): SHOW QOSTPL:QOSID=1;

操作维护         QoS模板标识   可靠级   延迟级    优先级       峰值吞吐量       平均吞吐量         发送错误数据   发送顺序       最大业务数据单元长度   业务类别   最大上行链路比特率      最大下行链路比特率      业务数据单元错误率   残余位出错率     流量控制优先级   传输时延         保证上行链路比特率      保证下行链路比特率      分配/保持优先级   信令指示       源统计描述器   用户别名
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1             3        延迟级1   普通优先级   8000 字节/秒     最佳效果           不检测         不按顺序发送   1502 字节 (151)        交互类型   128 千比特/秒 (72)      128 千比特/秒 (72)      万分之一 (4)         千分之四 (4)     2                                                                                 2                 非最优化信令                  
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.064 秒）。
` 








父主题： [QoS模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### IMSI号段QoS上限配置 
### IMSI号段QoS上限配置 


背景知识 


SGSN中，对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


PDP上下文使用的QoS可以根据UE请求QoS、签约QoS和SGSN策略得到。 



 

请求QoS：指UE希望得到的QoS，UE在激活PDP上下文请求或修改PDP上下文请求消息中携带。
 

 

签约QoS：指UE能得到的QoS的上限，在HLR中签约确定。
 

 

SGSN策略：SGSN网元配置的策略，根据UE的IMSI或IMSI号段、接入方式（Iu接入或Gb接入）、接入的RNC ID（Iu接入时），限制UE使用的QoS不能超过指定的QoS上限或直接使用本地指定的QoS。
 

 




功能描述 


根据UE的IMSI或IMSI号段、接入方式（Iu接入或Gb接入）、接入的RNC ID（Iu接入时），限制UE使用的QoS不能超过本地指定的QoS上限或直接使用本地指定的QoS： 



 

对漫游用户，限制其使用的QoS不能超过本地指定的QoS上限。
 

 

如果某个UE由于QoS原因不能使用数据业务，如不能上网，可以指定该用户使用本地指定QoS。
 

 


IMSI号段QoS上限配置流程如下： 







                        配置QoS模板，配置命令为
                        [ADD QOSTPL]
                        。
                    







                        设置IMSI号段QoS上限控制为：“支持基于IMSI号段和接入类型控制QoS”，配置命令为
                        [SET IMSI QOSLMT SPRT]
                        。
                    







                        配置IMSI号段QoS上限配置， 配置命令为：
                        [ADD IMSI QOSLMT]
                        。
                    







                        缺省IMSI号段上限配置已生成默认记录，可根据需要修改，命令为：
                        [SET IMSI QOSLMT DEFAULT]
                        。
                    






配置后，SGSN根据UE的IMSI或IMSI号段、接入方式（Iu接入或Gb接入）、接入的RNC ID（Iu接入时），限制UE的QoS上限。如果UE的IMSI或IMSI号段没有配置，则SGSN使用缺省IMSI号段QoS上限配置对用户进行限制。 




相关主题 



 

设置IMSI号段QoS上限控制(SET IMSI QOSLMT SPRT)
 

 

查询IMSI号段QoS上限控制(SHOW IMSI QOSLMT SPRT)
 

 

新增IMSI号段QoS上限配置(ADD IMSI QOSLMT)
 

 

修改IMSI号段QoS上限配置(SET IMSI QOSLMT)
 

 

删除IMSI号段QoS上限配置(DEL IMSI QOSLMT)
 

 

查询IMSI号段QoS上限配置(SHOW IMSI QOSLMT)
 

 

设置缺省IMSI号段QoS上限(SET IMSI QOSLMT DEFAULT)
 

 

查询缺省IMSI号段QoS上限(SHOW IMSI QOSLMT DEFAULT)
 

 








父主题： [SGSN QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置IMSI号段QoS上限控制(SET IMSI QOSLMT SPRT) 
#### 设置IMSI号段QoS上限控制(SET IMSI QOSLMT SPRT) 


命令功能 


该命令用于设置SGSN是否支持基于IMSI号段和接入类型控制QoS上限。 




注意事项 


此功能只适用于SGSN。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIRAT|是否支持基于IMSI号段和接入类型控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持基于IMSI号段和接入类型控制QoS上限。不支持：SGSN不支持基于IMSI号段和接入类型控制QoS上限。支持：SGSN支持基于IMSI号段和接入类型控制QoS上限。






命令举例 


设置SGSN支持基于IMSI号段接入类型控制QoS上限配置。 


SET IMSI QOSLMT SPRT:IMSIRAT="YES"; 








父主题： [IMSI号段QoS上限配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询IMSI号段QoS上限控制(SHOW IMSI QOSLMT SPRT) 
#### 查询IMSI号段QoS上限控制(SHOW IMSI QOSLMT SPRT) 


命令功能 


该命令用于查询SGSN是否支持基于IMSI号段和接入类型控制QoS上限。 




注意事项 


无 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIRAT|是否支持基于IMSI号段和接入类型控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持基于IMSI号段和接入类型控制QoS上限。不支持：SGSN不支持基于IMSI号段和接入类型控制QoS上限。支持：SGSN支持基于IMSI号段和接入类型控制QoS上限。






命令举例 


查询IMSI号段QoS上限控制信息。 


SHOW IMSI QOSLMT SPRT 


`

命令 (No.3): SHOW IMSI QOSLMT SPRT

操作维护 是否支持基于IMSI号段和接入类型控制 
--------------------------------------------
修改      支持 
--------------------------------------------
记录数 1

命令执行成功（耗时 0.063 秒）。
` 








父主题： [IMSI号段QoS上限配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增IMSI号段QOS上限配置(ADD IMSI QOSLMT) 
#### 新增IMSI号段QOS上限配置(ADD IMSI QOSLMT) 


命令功能 


该命令用于SGSN根据用户的IMSI号段、无线侧的接入类型和接入的RNC ID（无线侧为Iu接入时）来限制用户的QoS能力。目的是为了SGSN能够按照IMSI号段对本网用户和漫游用户的QoS进行单独配置，实现灵活的QoS控制策略的功能。 


在UMTS网络中，MS最终使用的QoS是通过各网元共同协商出来的，涉及到MS请求的QoS、HLR中签约的QoS、SGSN提供的默认QoS、SGSN自身对QoS的限制情况和周边网元的QoS能力等。 


协商过程中涉及到以下几种QoS： 


请求的QoS：是指用户发起激活PDP上下文请求时要求的QoS。 


签约的QoS：是指HLR中关于用户的QoS签约信息。在用户附着网络后，HLR就把用户签约QoS信息下发给SGSN。 


默认QoS：是指在SGSN本地配置的QoS，当终端通过Iu模式接入时，未携带请求QoS，SGSN使用本地配置的默认QoS作为用户的请求QoS；或者当终端的请求QoS参数或HLR中签约的QoS参数不合法时，SGSN使用本地配置的默认QoS的数值对非法值进行修正。 


协商的QoS：是指SGSN比较用户请求的QoS、HLR签约的QoS以及SGSN自身的QoS的限制情况与RNC、GGSN所支持QoS能力的共同协商得出的最后结果。 


如果将“是否强制使用默认QoS”配置为“是”，那么用户请求的QoS，签约的QoS都不参与QoS协商，SGSN直接使用本命令配置的“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS作为协商QoS； 


如果将”是否强制使用默认QoS配置为“否“，则SGSN需要使用用户请求的QoS和签约的QoS协商，但协商的QoS不能超过本命令配置的“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS能力的上限。 




注意事项 


该命令只适用于SGSN网元。 


使用此功能需要先开启软件参数，对应的软件参数为“SGSN是否支持基于IMSI号段和接入类型限制QoS”。配置命令为： [SET SOFTWARE PARAMETER] :PARAID=786447,PARAVALUE=1; 。


在配置此命令之前，需要通过[ADD QOSTPL]命令配置QoS模板。




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
RNCID|RNC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:4294967295。|如果需要基于每个RNC进行QoS策略控制，可以在该配置命令中配置具体的RNC ID，不需要则保持RNC ID为默认值4294967295即可。该参数是ADD RNC命令配置的“RNC”参数，可以根据SHOW RNC查询。
DFTQOSFLG|是否强制使用默认QoS|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|如果配置为"是"，那么用户请求的QoS，签约的QoS都不参与QoS协商，直接使用“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS作为协商QoS；如果配置为“否'，则需要使用用户请求的QoS和签约的QoS协商，但协商的QoS不能超过“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS。
IUQOS|Iu接入QoS模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。
GBQOS|Gb接入QoS模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


新增IMSI号段QOS上限配置，设置IMSI号段为46001，RNC标识为4294967295（不需要根据RNC来进行QoS策略控制），强制使用默认QoS，设置Iu接入QoS模板标识为2，Gb接入QoS模板标识为1。 


ADD IMSI QOSLMT:IMSI="46001",RNCID=4294967295,DFTQOSFLG="YES",IUQOS=2,GBQOS=1; 








父主题： [IMSI号段QoS上限配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改IMSI号段QOS上限配置(SET IMSI QOSLMT) 
#### 修改IMSI号段QOS上限配置(SET IMSI QOSLMT) 


命令功能 

该命令用于根据用户的IMSI号段和RNC ID（无线侧为Iu接入模式）来修改对应的QoS能力。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
RNCID|RNC标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|如果需要基于每个RNC进行QoS策略控制，可以在该配置命令中配置具体的RNC ID，不需要则保持RNC ID为默认值4294967295即可。该参数是ADD RNC命令配置的“RNC”参数，可以根据SHOW RNC查询。
DFTQOSFLG|是否强制使用默认QoS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果配置为"是"，那么用户请求的QoS，签约的QoS都不参与QoS协商，直接使用“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS作为协商QoS；如果配置为“否'，则需要使用用户请求的QoS和签约的QoS协商，但协商的QoS不能超过“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS。
IUQOS|Iu接入QoS模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。
GBQOS|Gb接入QoS模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


修改IMSI号段为46001，RNC标识为4294967295的IMSI号段QOS上限配置，将Iu接入QoS模板标识修改为2，Gb接入QoS模板标识修改为1。 


SET IMSI QOSLMT:IMSI="46001",RNCID=4294967295,IUQOS=2,GBQOS=1; 








父主题： [IMSI号段QoS上限配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除IMSI号段QOS上限配置(DEL IMSI QOSLMT) 
#### 删除IMSI号段QOS上限配置(DEL IMSI QOSLMT) 


命令功能 

该命令用于根据用户的IMSI号段和RNC ID（无线侧为Iu接入模式）来删除对应的QoS能力。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
RNCID|RNC标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|如果需要基于每个RNC进行QoS策略控制，可以在该配置命令中配置具体的RNC ID，不需要则保持RNC ID为默认值4294967295即可。该参数是ADD RNC命令配置的“RNC”参数，可以根据SHOW RNC查询。






命令举例 


删除IMSI号段为46001，RNC标识为4294967295的IMSI号段QOS上限配置。 


DEL IMSI QOSLMT:IMSI="46001",RNCID=4294967295; 








父主题： [IMSI号段QoS上限配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询IMSI号段QOS上限配置(SHOW IMSI QOSLMT) 
#### 查询IMSI号段QOS上限配置(SHOW IMSI QOSLMT) 


命令功能 


该命令用于根据用户的IMSI号段和RNC ID（无线侧为Iu接入模式）来查询对应的QoS能力。 


如果输入IMSI号段和RNC ID，表示查询该IMSI号段和RNC ID对应的QoS能力。 


如果不输入查询参数，表示查询所有配置的IMSI号段和RNC ID对应的QoS能力。 




注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
RNCID|RNC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|如果需要基于每个RNC进行QoS策略控制，可以在该配置命令中配置具体的RNC ID，不需要则保持RNC ID为默认值4294967295即可。该参数是ADD RNC命令配置的“RNC”参数，可以根据SHOW RNC查询。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
RNCID|RNC标识|参数可选性:任选参数；参数类型:整数。|如果需要基于每个RNC进行QoS策略控制，可以在该配置命令中配置具体的RNC ID，不需要则保持RNC ID为默认值4294967295即可。该参数是ADD RNC命令配置的“RNC”参数，可以根据SHOW RNC查询。
DFTQOSFLG|是否强制使用默认QoS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果配置为"是"，那么用户请求的QoS，签约的QoS都不参与QoS协商，直接使用“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS作为协商QoS；如果配置为“否'，则需要使用用户请求的QoS和签约的QoS协商，但协商的QoS不能超过“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS。
IUQOS|Iu接入QoS模板标识|参数可选性:任选参数；参数类型:整数。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。
GBQOS|Gb接入QoS模板标识|参数可选性:任选参数；参数类型:整数。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


查询所有的IMSI号段QOS上限配置。 


SHOW IMSI QOSLMT 


`

命令 (No.1): SHOW IMSI QOSLMT

操作维护         IMSI号段   RNC标识   是否强制使用默认QoS   Iu接入QoS模板标识   Gb接入QoS模板标识   用户别名
------------------------------------------------------------------------------------------------------------
复制 修改 删除   4600188    4294967295     否                    1                   1                   
------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。

` 








父主题： [IMSI号段QoS上限配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省IMSI号段QoS上限(SET IMSI QOSLMT DEFAULT) 
#### 设置缺省IMSI号段QoS上限(SET IMSI QOSLMT DEFAULT) 


命令功能 


该命令用于设置某个IMSI号段对应缺省的QoS能力。 


如果系统根据用户的IMSI号码、无线侧的接入类型及RNC ID（无线侧为Iu接入时），没有匹配到通过[ADD IMSI QOSLMT]命令设置的对应的“Iu接入QoS模板标识”或“Gb接入QoS模板标识”，
那么，会使用此命令设置的“QoS模板标识”。




注意事项 


该命令只适用于SGSN网元。 


使用此功能需要先开启软件参数，对应的软件参数为“SGSN是否支持基于IMSI号段和接入类型限制QoS”。配置命令为： [SET SOFTWARE PARAMETER] :PARAID=786447,PARAVALUE=1; 




参数说明 


标识|名称|类型|说明
---|---|---|---
DFTQOSFLG|是否强制使用默认QoS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果配置为"是"，那么用户请求的QoS，签约的QoS都不参与QoS协商，直接使用“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS作为协商QoS；如果配置为“否'，则需要使用用户请求的QoS和签约的QoS协商，但协商的QoS不能超过“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS。
IUQOS|Iu接入QoS模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。
GBQOS|Gb接入QoS模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。






命令举例 


设置缺省IMSI号段QOS上限配置，强制使用默认QoS，设置Iu接入QoS模板标识为2，Gb接入QoS模板标识为1。 


SET IMSI QOSLMT DEFAULT:DFTQOSFLG="YES",IUQOS=2,GBQOS=1; 








父主题： [IMSI号段QoS上限配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询缺省IMSI号段QOS上限(SHOW IMSI QOSLMT DEFAULT) 
#### 查询缺省IMSI号段QOS上限(SHOW IMSI QOSLMT DEFAULT) 


命令功能 

该命令用于查询缺省的IMSI号段对应的QoS能力。


注意事项 

该命令只适用于SGSN网元。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
DFTQOSFLG|是否强制使用默认QoS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果配置为"是"，那么用户请求的QoS，签约的QoS都不参与QoS协商，直接使用“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS作为协商QoS；如果配置为“否'，则需要使用用户请求的QoS和签约的QoS协商，但协商的QoS不能超过“Iu接入QoS模板标识”或“Gb接入QoS模板标识”对应的QoS。
IUQOS|Iu接入QoS模板标识|参数可选性:任选参数；参数类型:整数。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。
GBQOS|Gb接入QoS模板标识|参数可选性:任选参数；参数类型:整数。|此参数的取值是通过ADD QOSTPL命令设置的“QOSID”参数，可以根据SHOW QOSTPL查询。






命令举例 


查询缺省IMSI号段QOS上限配置。 


SHOW IMSI QOSLMT DEFAULT 


`

命令 (No.1): SHOW IMSI QOSLMT DEFAULT

操作维护  是否强制使用默认QoS   Iu接入QoS模板标识   Gb接入QoS模板标识
---------------------------------------------------------------------
修改      否                    1                   1
---------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.061 秒）。
` 








父主题： [IMSI号段QoS上限配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### IMSI号段签约QoS提升配置 
### IMSI号段签约QoS提升配置 


背景知识 


SGSN中，对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


PDP上下文使用的QoS可以根据UE请求QoS、签约QoS和SGSN策略得到。 



 

请求QoS：指UE希望得到的QoS，UE在激活PDP上下文请求或修改PDP上下文请求消息中携带。
 

 

签约QoS，指UE能得到的QoS的上限，在HLR中签约确定。
 

 

SGSN配置的QoS策略：有的HLR由于支持的协议版本较低，签约QoS中的MBR（Maximum Bit Rate，最大比特速率）的最大值只有16Mbps，有些数据卡用户，需要使用的MBR大于16Mbps。SGSN可以根据UE的IMSI或IMSI号段，提升签约QoS中的MBR，使UE使用的QoS中的MBR速率大于16Mbps。
 

 




功能描述 


在HLR签约的最大MBR不能满足UE使用的MBR需求时，使用IMSI号段签约QoS提升功能。通过SGSN上的配置可以根据UE的IMSI或IMSI号段号段和用户签约的MBR，提升用户签约的MBR，并把提升后的MBR作为用户签约MBR使用。 


IMSI号段签约QoS提升功能包括两个配置：QoS提升模板配置和IMSI号段QoS提升配置。 




相关主题 



 

QoS提升模板配置
 

 

IMSI号段QoS提升配置
 

 








父主题： [SGSN QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### QoS提升模板配置 
#### QoS提升模板配置 


背景知识 


SGSN中，对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


PDP上下文使用的QoS可以根据UE请求QoS、签约QoS和SGSN策略得到。 



 

请求QoS：指UE希望得到的QoS，UE在激活PDP上下文请求或修改PDP上下文请求消息中携带。
 

 

签约QoS：指能得到的QoS的上限，在HLR中签约确定。
 

 

SGSN配置的QoS策略：有的HLR由于支持的协议版本较低，签约QoS中的MBR的最大值只有16Mbps，而有些数据卡用户，需要使用的MBR大于16Mbps。通过SGSN上的配置，可以根据UE的IMSI或IMSI号段，提升签约QoS中的MBR，使UE使用的QoS中的MBR速率大于16Mbps。
 

 




功能描述 


在HLR签约的最大MBR不能满足UE使用的MBR需求时，使用IMSI号段签约QoS提升功能。SGSN可以根据UE的IMSI或IMSI号段号段和用户签约的MBR，提升用户签约的MBR，并把提升后的MBR作为用户签约MBR使用。 


IMSI号段签约QoS提升功能的配置过程如下： 







                        配置QoS提升模板，命令为
                        [ADD QOS UPGRADE TPL]
                        。由于多个IMSI或IMSI号段使用的提升签约QoS策略可能相同，为了避免重复配置数据，将QoS提升策略单独配置称为QoS提升模板。
                    







                        配置IMSI号段签约QoS提升配置，命令为：
                        [ADD IMSI UPGRADE QOS]
                        。在IMSI号段QoS提升配置中配置IMSI号段和对应的QoS提升策略模板号，实现IMSI号段和QoS提升策略的关联。
                    








相关主题 



 

新增QoS提升模板配置(ADD QOS UPGRADE TPL)
 

 

修改QoS提升模板配置(SET QOS UPGRADE TPL)
 

 

删除QoS提升模板配置(DEL QOS UPGRADE TPL)
 

 

查询QoS提升模板配置(SHOW QOS UPGRADE TPL)
 

 








父主题： [IMSI号段签约QoS提升配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增QoS提升模板配置(ADD QOS UPGRADE TPL) 
##### 新增QoS提升模板配置(ADD QOS UPGRADE TPL) 


命令功能 


该命令用于定义一个QoS提升模板，作用为提升用户签约QoS数据中的上/下行MBR（Maximum Bit Rate，最大比特率）。 


系统通过一个预先设定的QoS提升模板规定了用户的上/下行MBR范围及可以提升到对应的数值，后续可以将此QoS模板与用户的IMSI关联，SGSN可以根据用户的IMSI号码提升用户签约QoS数据中的上/下行MBR（具体命令参见[ADD IMSI UPGRADE QOS]。


具体提升过程详细描述如下（以上行MBR为例）：当用户的上/下行MBR在系统设置的范围之内时，可以提升到对应的数值（即通过本命令设置的“提升的最大比特率”）。 




注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|QoS模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|此参数表示QoS提升模板ID。该参数配置的数值，可用于ADD IMSI UPGRADE QOS命令中的“MAXUPBRTPL”参数和“MAXDNBRTPL”参数的取值。
MAXBRLOW|最大比特率下限|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|“最大比特率下限”和“最大比特率上限”决定了一个上/下行MBR范围。
MAXBRHIGH|最大比特率上限|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|“最大比特率下限”和“最大比特率上限”决定了一个上/下行MBR范围。
MAXBRMOD|提升的最大比特率|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|当用户的上/下行MBR在系统设置的范围之内时，可以提升到对应的数值。






命令举例 


新增QoS提升模板配置，设置QoS模板标识为1，最大比特率下限为1kbps，最大比特率上限为50kbps，提升的最大比特率为104kbps。 


ADD QOS UPGRADE TPL:TPLID=1,MAXBRLOW="1 kbps",MAXBRHIGH="50 kbps",MAXBRMOD="104 kbps"; 








父主题： [QoS提升模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改QoS提升模板配置(SET QOS UPGRADE TPL) 
##### 修改QoS提升模板配置(SET QOS UPGRADE TPL) 


命令功能 

该命令用于修改预先设定的QoS提升模板中规定的用户的上/下行MBR范围及可以提升到对应的数值。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|QoS模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|此参数表示QoS提升模板ID。该参数配置的数值，可用于ADD IMSI UPGRADE QOS命令中的“MAXUPBRTPL”参数和“MAXDNBRTPL”参数的取值。
MAXBRLOW|最大比特率下限|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|“最大比特率下限”和“最大比特率上限”决定了一个上/下行MBR范围。
MAXBRHIGH|最大比特率上限|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|“最大比特率下限”和“最大比特率上限”决定了一个上/下行MBR范围。
MAXBRMOD|提升的最大比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户的上/下行MBR在系统设置的范围之内时，可以提升到对应的数值。






命令举例 


修改QoS模板标识为1的QoS提升模板配置，修改最大比特率下限为1kbps，最大比特率上限为50kbps，提升的最大比特率为104kbps。 


SET QOS UPGRADE TPL:TPLID=1,MAXBRLOW="1 kbps",MAXBRHIGH="50 kbps",MAXBRMOD="104 kbps"; 








父主题： [QoS提升模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除QoS提升模板配置(DEL QOS UPGRADE TPL) 
##### 删除QoS提升模板配置(DEL QOS UPGRADE TPL) 


命令功能 

该命令用于删除QoS提升模板。


注意事项 


该命令只适用于SGSN网元。 


在执行此命令前，必须确认：对应的“QoS模板标识”没有被某个IMSI号段关联，即通过[SHOW IMSI UPGRADE QOS]命令查询不到对应的记录，否则，需要先通过命令删除此“QoS模板标识”与IMSI号段的关联，此命令才能执行成功。




参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|QoS模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|此参数表示QoS提升模板ID。该参数配置的数值，可用于ADD IMSI UPGRADE QOS命令中的“MAXUPBRTPL”参数和“MAXDNBRTPL”参数的取值。






命令举例 


删除QoS模板标识为1的QoS提升模板配置。 


DEL QOS UPGRADE TPL:TPLID=1; 








父主题： [QoS提升模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询QoS提升模板配置(SHOW QOS UPGRADE TPL) 
##### 查询QoS提升模板配置(SHOW QOS UPGRADE TPL) 


命令功能 


命令用于查询QoS提升模板。 


如果输入QoS模板标识，表示查询该标识对应的QoS模板。 


如果不输入查询参数，表示查询所有的QoS模板。 




注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|QoS模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|此参数表示QoS提升模板ID。该参数配置的数值，可用于ADD IMSI UPGRADE QOS命令中的“MAXUPBRTPL”参数和“MAXDNBRTPL”参数的取值。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|QoS模板标识|参数可选性:任选参数；参数类型:整数。|此参数表示QoS提升模板ID。该参数配置的数值，可用于ADD IMSI UPGRADE QOS命令中的“MAXUPBRTPL”参数和“MAXDNBRTPL”参数的取值。
MAXBRLOW|最大比特率下限|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|“最大比特率下限”和“最大比特率上限”决定了一个上/下行MBR范围。
MAXBRHIGH|最大比特率上限|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|“最大比特率下限”和“最大比特率上限”决定了一个上/下行MBR范围。
MAXBRMOD|提升的最大比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户的上/下行MBR在系统设置的范围之内时，可以提升到对应的数值。






命令举例 


查询所有的QoS提升模板配置。 


SHOW QOS UPGRADE TPL; 


`
 
命令 (No.1): SHOW QOS UPGRADE TPL

操作维护         QoS模板标识   最大比特率下限          最大比特率上限          提升的最大比特率
-----------------------------------------------------------------------------------------------
复制 修改 删除   1             13 千比特/秒 (13)       80 千比特/秒 (66)       408 千比特/秒 (107)
复制 修改 删除   2             44 千比特/秒 (44)       328 千比特/秒 (97)      2880 千比特/秒 (164)
-----------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.061 秒）。
` 








父主题： [QoS提升模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### IMSI号段QoS提升配置 
#### IMSI号段QoS提升配置 


背景知识 


SGSN中，对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


PDP上下文使用的QoS可以根据UE请求QoS、签约QoS和SGSN策略得到。 



 

请求QoS：指UE希望得到的QoS，UE在激活PDP上下文请求或修改PDP上下文请求消息中携带。
 

 

签约QoS：指能得到的QoS的上限，在HLR中签约确定。
 

 

SGSN配置的QoS策略：有的HLR由于支持的协议版本较低，签约QoS中的MBR的最大值只有16Mbps，而有些数据卡用户，需要使用的MBR大于16Mbps。通过SGSN上的配置，可以根据UE的IMSI或IMSI号段，提升签约QoS中的MBR，使UE使用的QoS中的MBR速率大于16Mbps。
 

 




功能描述 


在HLR签约的最大MBR不能满足UE使用的MBR需求时，使用IMSI号段签约QoS提升功能。SGSN可以根据UE的IMSI或IMSI号段号段和用户签约的MBR，提升用户签约的MBR，并把提升后的MBR作为用户签约MBR使用。 


IMSI号段签约QoS提升功能的配置过程如下： 







                        配置QoS提升模板，配置命令为
                        [ADD QOS UPGRADE TPL]
                        。由于多个IMSI或IMSI号段使用的提升签约QoS策略可能相同，为了避免重复配置数据，将QoS提升策略单独配置称为QoS提升模板。
                    







                        配置IMSI号段签约QoS提升配置， 配置命令为：
                        [ADD IMSI UPGRADE QOS]
                        。在IMSI号段QoS提升配置中配置IMSI号段和对应的QoS提升策略模板号，实现IMSI号段和QoS提升策略的关联。
                    








相关主题 



 

新增IMSI号段签约QoS提升配置(ADD IMSI UPGRADE QOS)
 

 

修改IMSI号段签约QoS提升配置(SET IMSI UPGRADE QOS)
 

 

删除IMSI号段签约QoS提升配置(DEL IMSI UPGRADE QOS)
 

 

查询IMSI号段签约QoS提升配置(SHOW IMSI UPGRADE QOS)
 

 








父主题： [IMSI号段签约QoS提升配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增IMSI号段签约QoS提升配置(ADD IMSI UPGRADE QOS) 
##### 新增IMSI号段签约QoS提升配置(ADD IMSI UPGRADE QOS) 


命令功能 


该命令用于SGSN支持根据用户的IMSI号段，提升用户签约QoS数据中的上/下行MBR。 


目的是为了SGSN能够按照IMSI号段对本网用户和漫游用户的QoS进行单独配置，实现灵活的QoS控制策略的功能（比如可以让漫游用户获得更高速率的本地上网业务）。 


用户签约的上行MBR在配置的该IMSI号段对应的某个上行MBR范围内时，SGSN对上行MBR进行提升处理。 


当用户签约的下行MBR在配置该IMSI号段对应某个下行MBR范围内时，SGSN对下行MBR进行提升处理。 




注意事项 


该命令只适用于SGSN网元。
 


配置该命令前确认已经通过[ADD QOS UPGRADE TPL]命令配置了QoS提升模板。


同一个IMSI号段可以配置多个上/下行MBR范围及对应的提升比特率，多个上行MBR范围不可有重叠；多个下行MBR范围不可有重叠。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
MAXUPBRTPL|最大上行比特率提升模板|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数的取值，是通过ADD QOS UPGRADE TPL命令设置的“TPLID”。
MAXDNBRTPL|最大下行比特率提升模板|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数的取值，是通过ADD QOS UPGRADE TPL命令设置的“TPLID”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


新增IMSI号段签约QoS提升配置，设置IMSI号段为46001，最大上行比特率提升模板为1，最大下行比特率提升模板为2。 


ADD IMSI UPGRADE QOS:IMSI="46001",MAXUPBRTPL=1,MAXDNBRTPL=2; 








父主题： [IMSI号段QoS提升配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改IMSI号段签约QoS提升配置(SET IMSI UPGRADE QOS) 
##### 修改IMSI号段签约QoS提升配置(SET IMSI UPGRADE QOS) 


命令功能 

该命令用于修改某个IMSI号段对应的QoS提升模板。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
MAXUPBRTPL|最大上行比特率提升模板|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数的取值，是通过ADD QOS UPGRADE TPL命令设置的“TPLID”。
MAXDNBRTPL|最大下行比特率提升模板|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数的取值，是通过ADD QOS UPGRADE TPL命令设置的“TPLID”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


修改IMSI号段为46001的IMSI号段签约QoS提升配置，将最大上行比特率提升模板修改为1，最大下行比特率提升模板修改为1。 


SET IMSI UPGRADE QOS:IMSI="46001",MAXUPBRTPL=1,MAXDNBRTPL=1,NAME="A"; 








父主题： [IMSI号段QoS提升配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除IMSI号段签约QoS提升配置(DEL IMSI UPGRADE QOS) 
##### 删除IMSI号段签约QoS提升配置(DEL IMSI UPGRADE QOS) 


命令功能 

该命令用于删除某个IMSI号段对应的QoS提升模板。


注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。






命令举例 


删除IMSI号段为46001的IMSI号段签约QoS提升配置。 


DEL IMSI UPGRADE QOS:IMSI="46001"; 








父主题： [IMSI号段QoS提升配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询IMSI号段签约QoS提升配置(SHOW IMSI UPGRADE QOS) 
##### 查询IMSI号段签约QoS提升配置(SHOW IMSI UPGRADE QOS) 


命令功能 


该命令用于查询IMSI号段对应的QoS提升模板。 


如果输入IMSI号段，表示查询该IMSI号段对应的签约QoS提升配置。 


如果不输入查询参数，表示查询所有配置的签约QoS提升配置。 




注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|该参数指示IMSI（International Mobile Subscriber Identity，国际移动用户标识）。该参数为是区别移动用户的标志，使用0～9的数字，且总长度不超过15位。
MAXUPBRTPL|最大上行比特率提升模板|参数可选性:任选参数；参数类型:字符型。|该参数的取值，是通过ADD QOS UPGRADE TPL命令设置的“TPLID”。
MAXDNBRTPL|最大下行比特率提升模板|参数可选性:任选参数；参数类型:字符型。|该参数的取值，是通过ADD QOS UPGRADE TPL命令设置的“TPLID”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


查询所有的IMSI号段签约QoS提升配置。 


SHOW IMSI UPGRADE QOS; 


`

命令 (No.1): SHOW IMSI UPGRADE QOS

操作维护         IMSI号段   最大上行比特率提升模板   最大下行比特率提升模板   用户别名
--------------------------------------------------------------------------------------
复制 修改 删除   46001      1                        2                        
--------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.031 秒）。
` 








父主题： [IMSI号段QoS提升配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Smart QoS配置 
### Smart QoS配置 


背景知识 


SGSN中，对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 


QoS参数在各个协议版本中不尽相同，在R6协议中，QoS的MBR和GBR最大值为16Mbps，在R7协议中，QoS的MBR和GBR最大值可达256Mbps。支持R6协议的终端，如果在HLR中签约了R7的QoS，UE在PDP激活或二次激活过程中，SGSN由于不知道终端支持的协议版本，有可能QoS协商的MBR或GBR最大值超过了16M，终端会在PDP激活成功之后，立刻去激活该PDP，原因值指示为QoS不接受（QoS not accepted）。 


为了提升激活成功率，SGSN需要根据UE的MBR和GBR的上限，确定下一次激活或二次激活过程中MBR和GBR的值。 




功能描述 


Smart QoS指SGSN记录UE不能接受的MBR和GBR的上限，在下次PDP激活或二次激活时，指定的MBR或GBR要比记录的UE的MBR和GBR的上限值要小，SGSN通过Smart QoS配置确定UE能接受的MRB和GBR的上限值。 



                Smart QoS功能需要通过开关控制，启用Smart QoS功能的配置命令为：
                [SET SMART QOS SPRT]
                。
            



                配置Smart QoS功能，配置命令为：
                [SET SMART QOS SPRT]
                。
            




相关主题 



 

设置是否支持Smart QoS功能(SET SMART QOS SPRT)
 

 

查询是否支持Smart QoS功能(SHOW SMART QOS SPRT)
 

 

新增Smart QoS配置(ADD SMART QOS)
 

 

删除Smart QoS配置(DEL SMART QOS)
 

 

查询Smart QoS配置(SHOW SMART QOS)
 

 








父主题： [SGSN QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置是否支持Smart QoS功能(SET SMART QOS SPRT) 
#### 设置是否支持Smart QoS功能(SET SMART QOS SPRT) 


命令功能 


该命令用于设置SGSN是否支持Smart QoS功能。 


QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在MS的PDP上下文中。在MS激活PDP上下文的时候，SGSN需要与MS进行QoS参数协商。如果协商失败，SGSN将拒绝用户接入。 


在UMTS网络中，MS最终使用的QoS参数是通过各网元共同协商出来的，涉及到MS请求的QoS、HLR中签约的QoS、SGSN提供的默认QoS、SGSN自身的资源情况和周边网元的QoS能力等。 


协商过程中涉及到以下几种QoS： 


请求的QoS：是指用户发起激活PDP上下文请求时要求的QoS。
 

 
签约的QoS：是指HLR中关于用户的QoS签约信息。在用户附着网络后，HLR就把用户签约QoS信息下发给SGSN。
 

 
协商的QoS：是指SGSN比较用户请求的QoS、HLR签约的QoS以及SGSN自身的QoS能力与RNC、GGSN共同协商得出的最后结果。
 

 


在UMTS网络的各种业务流程中（如MS发起的PDP激活流程、MS/SGSN/GGSN发起的PDP修改流程、RAU、Relocation流程等），SGSN负责将MS请求的QoS、HLR中签约的QoS、SGSN提供的默认QoS和SGSN自身的资源情况一起进行QoS协商，最终协商的结果为网络侧协商QoS，以供MS使用，如果MS不接受网络侧协商出的QoS，会主动发起PDP去激活流程，MS向SGSN发送deactivate pdp context reqMSst消息，携带原因值“QoS not accepted”。 


3GPP协议各个版本中定义的QoS参数的种类和对应的数值不尽相同。 


例如：在R6版本中，QoS的MBR（Maximum Bit Rate，最大比特率）和GBR（Guaranteed Bit Rate，保证比特率）的最大值为16Mbps，在R7版本中，QoS的MBR和GBR最大值为256Mbps。 


如果MS支持的QoS版本为R6，但签约的QoS版本为R7，在PDP激活或二次激活过程中，如果MS的MBR或GBR最大值超过了16M，则由于QoS协商不成功会导致接入失败。 


在此种情况下，为了让MS可以正常接入网络，SGSN可以根据MS支持的Qos参数的情况，设置一个MS可以接受的数值，以保证Qos协商成功。 


Smart Qos功能是指，当MS支持的QoS参数中的MBR与签约的QoS参数不匹配时，为了让用户正常使用网络，SGSN根据MS的MBR的上限值将MS签约的QoS参数中的MBR改写成特定的值，以保持Qos协商成功。 




注意事项 

该命令适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
ISSMARTQOS|是否支持Smart QoS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数表示SGSN是否支持Smart QoS功能。






命令举例 


设置支持Smart QoS功能。
SET SMART QOS SPRT:ISSMARTQOS="YES"; 








父主题： [Smart QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询是否支持Smart QoS功能(SHOW SMART QOS SPRT) 
#### 查询是否支持Smart QoS功能(SHOW SMART QOS SPRT) 


命令功能 

该命令用于查询SGSN是否支持Smart QoS功能。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
ISSMARTQOS|是否支持Smart QoS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数表示SGSN是否支持Smart QoS功能。






命令举例 


查询是否支持Smart QoS功能。
SHOW SMART QOS SPRT 


`

命令 (No.1): SHOW SMART QOS SPRT

操作维护  是否支持Smart QoS功能
-------------------------------
修改      支持
-------------------------------
记录数 1

命令执行成功（耗时 0.046 秒）。
` 








父主题： [Smart QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Smart QoS配置(ADD SMART QOS) 
#### 新增Smart QoS配置(ADD SMART QOS) 


命令功能 

此命令用于SGSN根据MS的可以接受的MBR的上限值来配置“最大上行链路比特率”与“最大下行链路比特率”，以保持Qos协商成功。


注意事项 


在设置本命令前，需要通过[SET SMART QOS SPRT]命令设置SGSN支持Smart QoS功能。


当将“QOS参数类型”设置为“最大上行链路比特率”时，需要设置对应的“最大上行链路比特率区间映射点”。 


当将“QOS参数类型”设置为“最大下行链路比特率”时，需要设置对应的“最大下行链路比特率区间映射点”。 




参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFICCLS|QOS参数类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|Qos参数类型选择“最大上行链路比特率”时，需配置最大上行链路比特率区间映射点。 Qos参数类型选择“最大下行链路比特率”时，需配置最大下行链路比特率区间映射点。
MAXBITRATEUL|最大上行链路比特率区间映射点|参数可选性:必须单选参数；参数类型:枚举。参见枚举定义。|用于和SGSN记录的UE支持的最大上行链路比特率进行比较以确定使用哪个最大上行比特率。
MAXBITRATEDL|最大下行链路比特率区间映射点|参数可选性:必须单选参数；参数类型:枚举。参见枚举定义。|用于和SGSN记录的UE支持的最大下行链路比特率进行比较以确定使用哪个最大下行比特率。






命令举例 


新增Smart QoS配置，设置QOS参数类型为最大上行链路比特率，设置最大上行链路比特率区间映射点为15kbps和35kbps。
ADD SMART QOS:TRAFFICCLS="MAXBITRATEUL",MAXBITRATEUL="15"&"35"; 








父主题： [Smart QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Smart QoS配置(DEL SMART QOS) 
#### 删除Smart QoS配置(DEL SMART QOS) 


命令功能 

该命令用于删除Smart QoS配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFICCLS|QOS参数类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|Qos参数类型选择“最大上行链路比特率”时，需配置最大上行链路比特率区间映射点。 Qos参数类型选择“最大下行链路比特率”时，需配置最大下行链路比特率区间映射点。






命令举例 


删除QOS参数类型为最大上行链路比特率的Smart QoS配置。
DEL SMART QOS:TRAFFICCLS="MAXBITRATEUL"; 








父主题： [Smart QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Smart QoS配置(SHOW SMART QOS) 
#### 查询Smart QoS配置(SHOW SMART QOS) 


命令功能 

该命令用于查询Smart QoS配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFICCLS|QOS参数类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Qos参数类型选择“最大上行链路比特率”时，需配置最大上行链路比特率区间映射点。 Qos参数类型选择“最大下行链路比特率”时，需配置最大下行链路比特率区间映射点。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFICCLS|QOS参数类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Qos参数类型选择“最大上行链路比特率”时，需配置最大上行链路比特率区间映射点。 Qos参数类型选择“最大下行链路比特率”时，需配置最大下行链路比特率区间映射点。
MAXBITRATE|最大链路比特率区间映射点|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于和SGSN记录的UE支持的最大链路比特率进行比较以确定使用哪个最大比特率，分上行和下行。Qos参数类型为“最大下行链路比特率”时，表示下行链路最大链路比特率区间映射点 。Qos参数类型为“最大上行链路比特率”时，表示上行链路最大链路比特率区间映射点 。






命令举例 


查询所有的Smart QoS配置。 


SHOW SMART QOS; 


`

命令 (No.1): SHOW SMART QOS

操作维护    QOS参数类型          最大链路比特率区间映射点
---------------------------------------------------------
复制 删除   最大上行链路比特率   15 千比特/秒 (15)
复制 删除   最大上行链路比特率   35 千比特/秒 (35)
---------------------------------------------------------
记录数 2

命令执行成功（耗时 0.043 秒）。
` 








父主题： [Smart QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### RAB指派流程QoS配置 
### RAB指派流程QoS配置 


背景知识 


根据23.060协议规定，在RAB指派流程中，如果RNC无法接受核心网下发的QoS，则RNC会向SGSN发送“RAB Assignment Response”消息，并携带类似“Requested Maximum Bit Rate not Available”的失败原因，SGSN在收到此类失败原因后，按照协议规定可以降低QoS参数重新发起RAB指派，QoS重新协商的细节协议未做规定。 




功能描述 


当SGSN下发RAB Assignment Request消息新建或修改某个RAB时，若RNC在响应消息RAB Assignment Response中指示RAB新建或修改失败，失败的原因为如下7个原因时，SGSN根据“RAB指派流程QoS配置”决定是否发起RAB重指派流程。 



 

如果RCN指示失败原因是"Requested Maximum Bit Rate not Available"，则SGSN根据“RAB指派流程QoS重协商-最大上行比特率降低跳数”和“RAB指派流程QoS重协商-最大下行比特率降低跳数”的配置值，决定是否降低协商QoS，重新向RNC发起RAB指派流程。
 

 

如果RCN指示失败原因是"Requested Maximum Bit Rate for UL not Available"或者"Requested Maximum Bit Rate for DL not Available"，则SGSN根据“RAB指派流程QoS重协商-最大上行比特率降低跳数”或者“RAB指派流程QoS重协商-最大下行比特率降低跳数”的配置值，决定是否降低协商QoS，重新向RNC发起RAB指派流程。
 

 

如果RCN指示失败原因是"Requested Guaranteed Bit Rate not Available"且用户协商QoS中的Traffic Class不是Interactive class和Background class，则SGSN根据“RAB指派流程QoS重协商-保证上行比特率降低跳数”和“RAB指派流程QoS重协商-保证下行比特率降低跳数”的配置值，决定是否降低协商QoS，重新向RNC发起RAB指派流程。
 

 

如果RNC指示失败原因是"Requested Guaranteed Bit Rate for UL not Available"或者"Requested Guaranteed Bit Rate for DL not Available"，且用户协商QoS中的Traffic Class不是Interactive class和Background class，则SGSN根据“RAB指派流程QoS重协商-保证上行比特率降低跳数”或者“RAB指派流程QoS重协商-保证下行比特率降低跳数”的配置值，决定是否降低协商QoS，重新向RNC发起RAB指派流程。
 

 

如果RNC指示失败原因是"Requested Transfer Delay not Achievable"且用户协商QoS中的Traffic Class不是Interactive class和Background class，则SGSN根据“RAB指派流程QoS重协商-传输延迟增高跳数”的配置值，决定是否降低协商QoS，重新向RNC发起RAB指派流程。
 

 


注意：“RAB指派流程QoS重协商最大次数”控制RAB指派过程中的QoS重新协商的最大次数，不区分RCN指示的失败原因；当配置为0时，表示SGSN不支持RAB指派过程中的QoS重新协商。 




相关主题 



 

设置RAB指派流程QoS(SET RAB QOS)
 

 

查询RAB指派流程QoS(SHOW RAB QOS)
 

 








父主题： [SGSN QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置RAB指派流程QoS(SET RAB QOS) 
#### 设置RAB指派流程QoS(SET RAB QOS) 


命令功能 


该命令用于设置RAB指派流程QoS配置。当需要根据RNC的响应消息RAB Assignment Response中指示的QoS相关的失败原因发起RAB重指派流程时，使用该命令。RAB指派流程QoS配置成功后，SGSN可以根据RAB指派流程QoS重协商各配置值并结合具体的QoS失败原因值，降低协商QoS，重新向RNC发起RAB指派流程。 




注意事项 


实际发起的RAB指派QoS重协商次数可能小于“RAB指派流程QoS重协商最大次数”的配置值，原因是：降低后的最大比特率不可小于保证比特率（注：若QoS中的Traffic Class是Interactive class或者Background class，则无此限制），且最大比特率不能降为0 bps；降低后的保证比特率最小值为0 bps；增大后传输延迟最大为4000 ms。当降低的QoS达到上限或者下限之后，则不再发起RAB重新指派。 




参数说明 


标识|名称|类型|说明
---|---|---|---
RENEGOMAX|RAB指派流程QoS重协商最大次数|参数可选性:任选参数；参数类型:整数；参数范围为:0~10。|在RAB指派流程中，如果RNC不支持网络侧下发的QoS参数，那么RAB指派流程QoS重协商最大次数控制核心网是否降低QoS参数等级，重新发起RAB指派流程，并限制最大重协商次数。0：不支持RAB指派过程中的QoS重协商。1~10：RAB指派过程中的QoS重协商的最大次数。
MAXBITUHOP|RAB指派流程QoS重协商-最大上行比特率降低跳数|参数可选性:任选参数；参数类型:整数；参数范围为:0~64。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对最大上行比特率降低跳数，一跳可能对应1kbps、8kbps、64kbps、100 kbps、1Mbps和2Mbps。0：不支持最大上行比特率的降低协商。1~64：每次降低Hop数。
MAXBITDHOP|RAB指派流程QoS重协商-最大下行比特率降低跳数|参数可选性:任选参数；参数类型:整数；参数范围为:0~64。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对最大下行比特率降低跳数，一跳可能对应1kbps、8kbps、64kbps、100 kbps、1Mbps和2Mbps。0：不支持最大下行比特率的降低协商。1~64：每次降低Hop数。
GUABITUHOP|RAB指派流程QoS重协商-保证上行比特率降低跳数|参数可选性:任选参数；参数类型:整数；参数范围为:0~64。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对保证上行比特率降低跳数，一跳可能对应1kbps、8kbps、64kbps、100 kbps、1Mbps和2Mbps。0：不支持保证上行比特率的降低协商。1~64：每次降低Hop数。
GUABITDHOP|RAB指派流程QoS重协商-保证下行比特率降低跳数|参数可选性:任选参数；参数类型:整数；参数范围为:0~64。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对保证下行比特率降低跳数，一跳可能对应1kbps、8kbps、64kbps、100 kbps、1Mbps和2Mbps。0：不支持保证下行比特率的降低协商。1~64：每次降低Hop数。
TNDELAYHOP|RAB指派流程QoS重协商-传输延迟增高跳数|参数可选性:任选参数；参数类型:整数；参数范围为:0~32。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对传输延迟增高跳数，一跳可能对应10ms、50ms和100ms。0：不支持传输延迟的增高协商。1~32：每次增高的Hop数。






命令举例 


设置RAB指派流程QoS重协商最大次数为5、最大上行比特率降低跳数为30。 


SET RAB QOS:RENEGOMAX=5,MAXBITUHOP=30; 








父主题： [RAB指派流程QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询RAB指派流程QoS(SHOW RAB QOS) 
#### 查询RAB指派流程QoS(SHOW RAB QOS) 


命令功能 


该命令用于查询RAB指派流程QoS配置。 




注意事项 


无 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
RENEGOMAX|RAB指派流程QoS重协商最大次数|参数可选性:任选参数；参数类型:整数。|在RAB指派流程中，如果RNC不支持网络侧下发的QoS参数，那么RAB指派流程QoS重协商最大次数控制核心网是否降低QoS参数等级，重新发起RAB指派流程，并限制最大重协商次数。0：不支持RAB指派过程中的QoS重协商。1~10：RAB指派过程中的QoS重协商的最大次数。
MAXBITUHOP|RAB指派流程QoS重协商-最大上行比特率降低跳数|参数可选性:任选参数；参数类型:整数。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对最大上行比特率降低跳数，一跳可能对应1kbps、8kbps、64kbps、100 kbps、1Mbps和2Mbps。0：不支持最大上行比特率的降低协商。1~64：每次降低Hop数。
MAXBITDHOP|RAB指派流程QoS重协商-最大下行比特率降低跳数|参数可选性:任选参数；参数类型:整数。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对最大下行比特率降低跳数，一跳可能对应1kbps、8kbps、64kbps、100 kbps、1Mbps和2Mbps。0：不支持最大下行比特率的降低协商。1~64：每次降低Hop数。
GUABITUHOP|RAB指派流程QoS重协商-保证上行比特率降低跳数|参数可选性:任选参数；参数类型:整数。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对保证上行比特率降低跳数，一跳可能对应1kbps、8kbps、64kbps、100 kbps、1Mbps和2Mbps。0：不支持保证上行比特率的降低协商。1~64：每次降低Hop数。
GUABITDHOP|RAB指派流程QoS重协商-保证下行比特率降低跳数|参数可选性:任选参数；参数类型:整数。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对保证下行比特率降低跳数，一跳可能对应1kbps、8kbps、64kbps、100 kbps、1Mbps和2Mbps。0：不支持保证下行比特率的降低协商。1~64：每次降低Hop数。
TNDELAYHOP|RAB指派流程QoS重协商-传输延迟增高跳数|参数可选性:任选参数；参数类型:整数。|在RAB指派流程中，如果网络侧发起QoS重协商，那么一次重协商过程，可能对传输延迟增高跳数，一跳可能对应10ms、50ms和100ms。0：不支持传输延迟的增高协商。1~32：每次增高的Hop数。






命令举例 


查询RAB指派流程QoS配置。 


SHOW RAB QOS 


`

命令 (No.6): SHOW RAB QOS

操作维护 RAB指派流程QoS重协商最大次数 RAB指派流程QoS重协商-最大上行比特率降低跳数  RAB指派流程QoS重协商-最大下行比特率降低跳数 RAB指派流程QoS重协商-保证上行比特率降低跳数   RAB指派流程QoS重协商-保证下行比特率降低跳数 RAB指派流程QoS重协商-传输延迟增高跳数 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      5                             30                                          0                                             0                                           0                                             0 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.048 秒）。
` 








父主题： [RAB指派流程QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### RAU流程QoS重协商和通知UE配置 
### RAU流程QoS重协商和通知UE配置 


背景知识 


用户在2G和3G间移动的RAU过程中，无论是局内还是局间RAU，由于接入方式发生改变，SGSN对2G接入和3G接入时QoS策略可能不同，因此SGSN需要在RAU过程中进行QoS重协商。 


RAU过程中SGSN能区分的只能是局内RAU，对局间RAU新局SGSN不知道UE上一次的接入方式，因此只要是局间Iu或Gb接入RAU都需要进行QoS重协商。 


用户在局间4G到3G的切换过程中，由于接入方式发生改变，3G接入和4G接入时的QoS可能不同，SGSN需要在切换后的首个RAU完成后进行QoS重协商。 


SGSN进行QoS重协商后QoS变化，通知UE新的QoS时，防止出现现网终端不兼容的情况，提供RAU过程QoS重协商后是否通知UE的配置。 




功能描述 


当SGSN执行2G和3G间的RAU流程时，需要进行QoS重协商，协商时机有两种： 



 

RAU过程中的协商。
 

 

滞后型的协商（包括RAU完成后和RAU后的首次业务请求过程中的协商）。
 

 


SGSN根据RAU流程QoS重协商和通知UE配置策略，确定是否进行QoS重协商和重协商的时机，确定QoS重协商后QoS变化是否通知UE。 


当SGSN执行局间4G到3G的切换流程时，需要进行QoS重协商，SGSN根据入局切换后的首个RAU完成后QoS重协商和通知UE配置策略，确定是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。 




相关主题 



 

设置RAU流程QoS重协商和通知UE(SET RAU QOS UE)
 

 

查询RAU流程QoS重协商和通知UE(SHOW RAU QOS UE)
 

 








父主题： [SGSN QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置RAU流程QoS重协商和通知UE(SET RAU QOS UE) 
#### 设置RAU流程QoS重协商和通知UE(SET RAU QOS UE) 


命令功能 


该命令用于设置RAU流程QoS重协商和通知UE配置。当SGSN需要在2G和3G间的RAU流程中进行QoS重协商，或在局间4G到3G的切换流程进行QoS重协商并通知UE时，使用该命令。RAU流程QoS重协商和通知UE配置成功后，SGSN可以根据QoS重协商和通知UE各配置值，确定是否进行QoS重协商、QoS重协商后QoS变化是否通知UE。 




注意事项 


无 




参数说明 


标识|名称|类型|说明
---|---|---|---
ITRAIUTOGB|局内Iu到Gb RAU过程QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在3G到2G的局内RAU过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITRAGBTOIU|局内Gb到Iu RAU过程QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在2G到3G的局内RAU过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITRAGBTOIUFST|局内Gb到Iu RAU后的首次业务请求过程中QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在2G到3G的局内RAU后的首次业务请求过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITERIU|局间Iu接入RAU过程QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在局间3G接入的RAU过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITERIUFST|局间Iu接入RAU后的首次业务请求过程中QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在局间3G接入RAU后的首次业务请求过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITERGB|局间Gb接入RAU过程QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在局间2G接入的RAU过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITERGBAFT|局间Gb接入RAU完成后QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在局间2G接入的RAU完成后，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
HOFST|入局切换后的首个RAU完成后QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在入局切换后的首个RAU完成后，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。






命令举例 


设置RAU流程QoS重协商和通知UE配置，其中，局内Iu到Gb RAU过程QoS重协商不通知UE，局内Gb到Iu RAU过程QoS重协商并通知UE。 


SET RAU QOS UE:ITRAIUTOGB="NEGOTIATION",ITRAGBTOIU="BOTH"; 








父主题： [RAU流程QoS重协商和通知UE配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询RAU流程QoS重协商和通知UE(SHOW RAU QOS UE) 
#### 查询RAU流程QoS重协商和通知UE(SHOW RAU QOS UE) 


命令功能 


该命令用于查询RAU流程QoS重协商和通知UE配置。 




注意事项 


无 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ITRAIUTOGB|局内Iu到Gb RAU过程QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在3G到2G的局内RAU过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITRAGBTOIU|局内Gb到Iu RAU过程QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在2G到3G的局内RAU过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITRAGBTOIUFST|局内Gb到Iu RAU后的首次业务请求过程中QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在2G到3G的局内RAU后的首次业务请求过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITERIU|局间Iu接入RAU过程QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在局间3G接入的RAU过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITERIUFST|局间Iu接入RAU后的首次业务请求过程中QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在局间3G接入RAU后的首次业务请求过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITERGB|局间Gb接入RAU过程QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在局间2G接入的RAU过程中，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
ITERGBAFT|局间Gb接入RAU完成后QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在局间2G接入的RAU完成后，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。
HOFST|入局切换后的首个RAU完成后QoS重协商和通知UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在入局切换后的首个RAU完成后，是否进行QoS重协商和QoS重协商后QoS变化是否通知UE。有如下三个选项：不协商：SGSN不进行QoS重协商。协商不通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化不通知UE。协商通知UE：SGSN进行QoS重协商，QoS重协商后QoS变化通知UE。






命令举例 


查询RAU流程QoS重协商和通知UE配置。 


SHOW RAU QOS UE 


`

命令 (No.8): SHOW RAU QOS UE

操作维护 局内Iu到Gb RAU过程QoS重协商和通知UE   局内Gb到Iu RAU过程QoS重协商和通知UE 局内Gb到Iu RAU后的首次业务请求过程中QoS重协商和通知UE 局间Iu接入RAU过程QoS重协商和通知UE   局间Iu接入RAU后的首次业务请求过程中QoS重协商和通知UE  局间Gb接入RAU过程QoS重协商和通知UE    局间Gb接入RAU完成后QoS重协商和通知UE   入局切换后的首个RAU完成后QoS重协商和通知UE 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      协商不通知                           协商通知                             协商不通知                                             不协商                               不协商                                              不协商                                不协商                               不协商 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.082 秒）。
` 








父主题： [RAU流程QoS重协商和通知UE配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## MME QoS配置 
## MME QoS配置 


背景知识 


MME对每个承载上下文，需要提供QoS，来保障承载的服务质量。 


4G接入时，终端使用的是R8 QoS，而2G/3G接入时，终端使用的是Pre-R8 QoS。R8 QoS和Pre-R8 QoS参数形式完全不一样。 



 

3GPP R8协议定义的QoS称为R8 QoS，R8协议引入了EPS网络，因此R8 QoS也称为EPS QoS，且R8 QoS中含有QCI（QoS Class Identifier，QoS等级标识）。
 

 

3GPP R8以前的协议定义的QoS称为Pre-R8 QoS。Pre-R8 QoS中无QCI参数。
 

 


QCI 是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。QCI的取值为1-255，除了9个标准QCI，其他QCI称为扩展QCI，可以由运营商自定义。 


当具有2G/3G/4G能力的UE，在4G附着、PDN连接建立、专有承载建立、从4G移动到2G/3G时，需要把R8 QoS转换为Pre R8 QoS。 




功能描述 


对于MME网元，只需要配置MME映射Pre-R8 QoS策略，MME QoS配置包括QoS转换时的默认Pre-R8 Qos参数配置、QCI相关配置和MME支持大于256Mbps速率控制配置。 




相关主题 



 

QoS转换时的默认Pre-R8 QoS参数
 

 

QCI相关配置
 

 

MME支持大于256Mbps速率控制配置
 

 

QoS控制策略配置
 

 

用户级QoS控制配置
 

 

会话级QoS控制配置
 

 

承载级QoS控制配置
 

 

默认承载ARP和QCI控制配置
 

 

缺省UE AMBR配置
 

 








父主题： [QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### QoS转换时的默认Pre-R8 QoS参数 
### QoS转换时的默认Pre-R8 QoS参数 


背景知识 


MME对每个承载上下文（Bearer Context），需要提供QoS（Quality of Service，服务质量）。 


4G接入时，使用的是R8 QoS，而2G/3G接入时，使用的是Pre-R8 QoS。 


R8 QoS和Pre-R8 QoS参数形式完全不一样。R8 QoS中含有QCI（QoS Class Identifier，QoS等级标识）。QCI 是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。 


QCI的取值为1-255，3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。除了9个标准QCI，其他QCI称为扩展QCI，可以由运营商自定义。 


当具有2G/3G/4G能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup、从4G移动到2G/3G时，需要把R8 QoS转换为Pre R8 QoS。 




功能描述 


在如下场景下，需要使用默认Pre-R8 QoS配置： 



 

具有2G/3G/4G能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup流程中建立承载，同时需要把Pre-R8 QoS带给UE，使UE后续移动到2G/3G后，可以直接使用Pre-R8 QoS作为承载上下文的QoS。
 

 

具有2G/3G/4G能力的UE，移动到2G/3G时，MME把R8 QoS映射为Pre-R8 QoS，传递给SGSN。
 

 


“QoS转换时的默认Pre-R8 QoS参数配置”已自动生成缺省记录了，可以根据客户的要求进行修改。 


说明： 


QCI相关配置中，已配置了QCI到Pre-R8 QoS映射，QoS转换时的默认Pre-R8 QoS参数配置一般不使用，只有QCI到Pre-R8 QoS映射没有时才使用QoS转换时的默认Pre-R8 QoS参数配置。 




相关主题 



 

设置QoS转换时的默认Pre-R8 QoS参数(SET PRER8 QOS DEFAULT)
 

 

设置QoS转换时的默认Pre-R8 QoS所有参数回到缺省值(RESET PRER8 QOS DEFAULT)
 

 

查询QoS转换时的默认Pre-R8 QoS参数(SHOW PRER8 QOS DEFAULT)
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置QoS转换时的默认Pre-R8 QoS参数(SET PRER8 QOS DEFAULT) 
#### 设置QoS转换时的默认Pre-R8 QoS参数(SET PRER8 QOS DEFAULT) 


命令功能 


该命令用于设置QOS转换时的默认Pre-R8 QOS参数。 


激活过程中如果UE具有UTRAN/GREAN能力时，网元根据该配置获取默认的Pre-R8 QOS参数带给手机。 




注意事项 

该命令不会被其他命令引用，配置时一般采取默认值。


参数说明 


标识|名称|类型|说明
---|---|---|---
RELIACLASS|可靠级|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数与业务数据单元错误率（SDU error ratio） 、残余位出错率（Residual bit error ratio）和发送错误数据（Delivery of erroneous SDUs）参数的取值相关，它们的相互取值对应关系，详见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
DELAYCLASS|延迟级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与业务类别（Traffic class） 和流量控制优先级（Traffic handling priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
PRECECLASS|优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与缺省分配/保持优先级（Allocation/Retention priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP 23107(R7)和3GPP 24008(R7)。
PEAK|峰值吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的最大链路比特率。取值含义见协议3GPP 24008(R7)。
MEAN|平均吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的链路比特率的平均值。取值含义见协议3GPP 24008(R7)。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为：“NotDetect”：“不检测”，表示根本不考虑差错检测就进行传送。“Deliver”：“发送”，表示将检测出有错的SDU（Service Data Unit，业务数据单元）标以差错指示后进行传送。“NotDeliver”："不发送"，表示将检测出有错的SDU标以差错指示后进行丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN是否按照要求顺序传送SDU，需要根据3GPP 23017(R7)协议而定。取值含义：“Order”：按顺序发送。“NotOrder”：不按顺序发送。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大业务数据单元长度，用于许可控制。取值含义见协议3GPP 24008(R7)。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：“Conversational”：会话类型“Streaming”：流类型“Interactive”：交互类型“Background”：背景类型
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口上行链路码的预留。取值含义见协议3GPP 24008(R7)。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口下行链路码的预留。取值含义见协议3GPP 24008(R7)。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指丢失或者检测出差错SDU的比例，用来配置L2的重发协议和L1的检错编码。取值含义见协议3GPP 24008(R7)。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指在传送SDU中未检测到的误码率，用来配置L1的信道编码和检错编码。取值含义见协议3GPP 24008(R7)。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数的含义指对不同媒体的SDU处理的优先权。对于同一个承载业务，它和参数“保证上行链路比特率”和“保证下行链路比特率“不能同时出现。取值含义：“1”：优先级1。“2”：优先级2。“3”：优先级3。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指不同的用户有不同的延迟容忍程度。UTRAN（UMTS Terrestrial Radio Access Network，UMTS陆地无线接入网）可根据这一参数来设定传送格式和ARQ（Automatic Repeat reQuest，自动重传请求）参数。取值含义见协议3GPP 24008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
ARP|缺省分配/保持优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数的含义指对分配和保持UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）承载的优先权。取值含义：“1”：优先级1“2”：优先级2“3”：优先级3
DSCPUL|缺省上行DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数的含义指缺省上行DSCP（Differentiated Services Code Point,差分服务编码点）。取值含义见协议3GPP 24008(R7)
DSCPDL|缺省下行DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数的含义指缺省下行DSCP。取值含义见协议3GPP 24008(R7)。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数只用于交互级业务（Interactive）。即当“业务类别”设置为“交互业务（Interactive）”时才需要设置该参数。取值含义：“NotOptimized”：非最优化信令。“Optimized”：最优化信令。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数说明SDU数据源的特征。取值含义：“UnKnown”：未知。“Speech”：语音。如果设置为“语音”，RAN、SGSN、GGSN和UE可根据经验得出统计复用增益，用于许可控制。






命令举例 


设置MME进行QoS转换时默认的Pre-R8 QoS参数，可靠级为“2”、延迟级为“1”、优先级为“normal”、峰值吞吐量为“16000 octet/s”、平均吞吐量为“500 octet/h”、发送错误数据为”NotDetect”、发送顺序为”ORDER”、最大业务数据单元配置范围为”50 octets”、业务列别为”Conversational”、最大上行链路比特率为”5 kbps”、最大下行链路比特率为”26 kbps”、业务数据单元错误率”1e-5”、残余位出错率”1e-3”、传输时延”850 ms”、保证上行链路比特率”5 kbps”、保证下行链路比特率”6 kbps”、缺省分配/保持优先级”2”、缺省上行DSCP为“2”、缺省下行DSCP “1”、源统计描述器”Speech“： 


SET PRER8 QoS DEFAULT:RELIACLASS=2,DELAYCLASS=Level 1,PRECECLASS=NORMAL,PEAK=16000 octet/s,MEAN=500 octet/h,DELIERRSDU=NotDetect,DELIORDER=ORDER,MAXSDUSIZE=50 octets,TRAFFCLASS=Conversational,MAXBITRATEUL=5 kbps,MAXBITRATEDL=26 kbps,SDUERRRATIO=1e-5,RESIDUALBER=1e-3,TRANSDELAY=850 ms,GUARBITRATEUL=5 kbps,GUARBITRATEDL=6 kbps,ARP=2,DSCPUL=2,DSCPDL=1,SRCSTADESCRIP=Speech; 








父主题： [QoS转换时的默认Pre-R8 QoS参数]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置QoS转换时的默认Pre-R8 QoS所有参数回到缺省值(RESET PRER8 QOS DEFAULT) 
#### 设置QoS转换时的默认Pre-R8 QoS所有参数回到缺省值(RESET PRER8 QOS DEFAULT) 


命令功能 

该命令用于设置QOS转换时的默认Pre-R8 QOS所有参数回到缺省值。


注意事项 

无。


命令举例 


设置QoS转换时的默认Pre-R8 QoS所有参数回到缺省值： 


RESET PRER8 QoS DEFAULT 








父主题： [QoS转换时的默认Pre-R8 QoS参数]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询QoS转换时的默认Pre-R8 QOS参数(SHOW PRER8 QOS DEFAULT) 
#### 查询QoS转换时的默认Pre-R8 QOS参数(SHOW PRER8 QOS DEFAULT) 


命令功能 

该命令用于查询QOS转换时的默认Pre-R8 QOS参数。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
RELIACLASS|可靠级|参数可选性:任选参数；参数类型:整数。|该参数与业务数据单元错误率（SDU error ratio） 、残余位出错率（Residual bit error ratio）和发送错误数据（Delivery of erroneous SDUs）参数的取值相关，它们的相互取值对应关系，详见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
DELAYCLASS|延迟级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与业务类别（Traffic class） 和流量控制优先级（Traffic handling priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP TS 23.107(R7)和3GPP TS 24.008(R7)。
PRECECLASS|优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数与缺省分配/保持优先级（Allocation/Retention priority）参数的取值相关，不同的取值有不同的对应关系，详细见协议：3GPP 23107(R7)和3GPP 24008(R7)。
PEAK|峰值吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的最大链路比特率。取值含义见协议3GPP 24008(R7)。
MEAN|平均吞吐量|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN可以处理的链路比特率的平均值。取值含义见协议3GPP 24008(R7)。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为：“NotDetect”：“不检测”，表示根本不考虑差错检测就进行传送。“Deliver”：“发送”，表示将检测出有错的SDU（Service Data Unit，业务数据单元）标以差错指示后进行传送。“NotDeliver”："不发送"，表示将检测出有错的SDU标以差错指示后进行丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SGSN是否按照要求顺序传送SDU，需要根据3GPP 23017(R7)协议而定。取值含义：“Order”：按顺序发送。“NotOrder”：不按顺序发送。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大业务数据单元长度，用于许可控制。取值含义见协议3GPP 24008(R7)。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：“Conversational”：会话类型“Streaming”：流类型“Interactive”：交互类型“Background”：背景类型
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口上行链路码的预留。取值含义见协议3GPP 24008(R7)。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是为了便于无线接口下行链路码的预留。取值含义见协议3GPP 24008(R7)。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指丢失或者检测出差错SDU的比例，用来配置L2的重发协议和L1的检错编码。取值含义见协议3GPP 24008(R7)。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义是指在传送SDU中未检测到的误码率，用来配置L1的信道编码和检错编码。取值含义见协议3GPP 24008(R7)。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数。|该参数的含义指对不同媒体的SDU处理的优先权。对于同一个承载业务，它和参数“保证上行链路比特率”和“保证下行链路比特率“不能同时出现。取值含义：“1”：优先级1。“2”：优先级2。“3”：优先级3。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指不同的用户有不同的延迟容忍程度。UTRAN（UMTS Terrestrial Radio Access Network，UMTS陆地无线接入网）可根据这一参数来设定传送格式和ARQ（Automatic Repeat reQuest，自动重传请求）参数。取值含义见协议3GPP 24008(R7)。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于上行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义指为了便于基于下行可用资源的许可控制和资源分配。见协议3GPP 24008(R7)。
ARP|缺省分配/保持优先级|参数可选性:任选参数；参数类型:整数。|该参数的含义指对分配和保持UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）承载的优先权。取值含义：“1”：优先级1“2”：优先级2“3”：优先级3
DSCPUL|缺省上行DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义指缺省上行DSCP（Differentiated Services Code Point,差分服务编码点）。取值含义见协议3GPP 24008(R7)
DSCPDL|缺省下行DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义指缺省下行DSCP。取值含义见协议3GPP 24008(R7)。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数只用于交互级业务（Interactive）。即当“业务类别”设置为“交互业务（Interactive）”时才需要设置该参数。取值含义：“NotOptimized”：非最优化信令。“Optimized”：最优化信令。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数说明SDU数据源的特征。取值含义：“UnKnown”：未知。“Speech”：语音。如果设置为“语音”，RAN、SGSN、GGSN和UE可根据经验得出统计复用增益，用于许可控制。






命令举例 


查询QoS转换时的默认Pre-R8 QoS参数： 


SHOW PRER8 QoS DEFAULT 


`

命令 (No.1): SHOW PRER8 QoS DEFAULT

操作维护  可靠级   延迟级    优先级       峰值吞吐量       平均吞吐量         发送错误数据   发送顺序       最大业务数据单元长度   业务类别   最大上行链路比特率      最大下行链路比特率      业务数据单元错误率   残余位出错率     流量控制优先级   传输时延         保证上行链路比特率      保证下行链路比特率      缺省分配/保持优先级   缺省上行DSCP   缺省下行DSCP   信令指示       源统计描述器
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      3        延迟级1   普通优先级   8000 字节/秒     最佳效果           不检测         不按顺序发送   1502 字节 (151)        交互类型   128 千比特/秒 (72)      128 千比特/秒 (72)      万分之一 (4)         千分之四 (4)     1                                                                                 2                     0              0              非最优化信令   
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.12 秒）。
` 








父主题： [QoS转换时的默认Pre-R8 QoS参数]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### QCI相关配置 
### QCI相关配置 


背景知识 


MME对每个承载上下文，需要提供QoS（Quality of Service，服务质量）。 


4G接入时，使用的是R8 QoS，而2G/3G接入时，使用的是Pre-R8 QoS。 


R8 QoS和Pre-R8 QoS参数形式完全不一样。 


R8 QoS中含有QCI（QoS Class Identifier，QoS等级标识）。QCI 是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。 


3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。 


QCI的取值为1-255，除了9个标准QCI，其他QCI称为扩展QCI，可以由运营商自定义。 


当具有2G/3G/4G能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup、从4G移动到2G/3G时，需要把R8 QoS转换为Pre R8 QoS。 




功能描述 


在如下场景下，需要使用QCI相关配置： 



 

具有2G/3G/4G能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup流程中建立承载，同时需要把Pre-R8 QoS带给UE，使UE后续移动到2G/3G后，可以直接使用Pre-R8 QoS作为承载上下文的QoS。
 

 

具有2G/3G/4G能力的UE，移动到2G/3G时，MME把R8 QoS映射为Pre-R8 QoS，传递给SGSN。
 

 




相关主题 



 

标准QCI到Pre-R8 QoS映射配置
 

 

扩展QCI到Pre-R8 QoS映射模板配置
 

 

扩展QCI配置
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 标准QCI到Pre-R8 QoS映射配置 
#### 标准QCI到Pre-R8 QoS映射配置 


背景知识 


用户接入4G网络时，使用的是R8 QoS， 接入2G/3G网络时，使用的是Pre-R8 QoS。 


R8 QoS和Pre-R8 QoS参数形式完全不一样。R8 QoS中含有QCI（QoS Class Identifier，QoS等级标识）。QCI 是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。 


3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。 


当具有2G/3G/4G能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup、从4G移动到2G或者3G时，MME需要把R8 QoS转换为Pre R8 QoS，把Pre-R8 QoS传递给UE，UE储存Pre-R8 QoS，使UE后续移动到2G/3G后，可以直接使用Pre-R8 QoS作为承载上下文的QoS。 




功能描述 


标准QCI到Pre-R8 QoS映射配置在以下场景使用。 



 

具有2G/3G/4G能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup流程中建立承载，承载QCI为标准QCI值，MME把Pre-R8 QoS传递给UE，UE储存Pre-R8 QoS，使UE后续移动到2G/3G后，可以直接使用Pre-R8 QoS作为承载上下文的QoS。
 

 

具有2G/3G/4G能力的UE，移动到2G/3G时，承载QCI为标准QCI值，MME把R8 QoS映射为Pre-R8 QoS，投递给SGSN。
 

 


说明： 


通常情况下，标准QCI到Pre-R8 QoS映射配置不需要配置，MME已生成默认值。可以根据客户的要求进行修改。 




相关主题 



 

设置标准QCI到Pre-R8 QoS映射配置(SET STANDARD QCI MAPPING)
 

 

设置标准QCI到Pre-R8 QoS映射回到缺省值(RESET DEFAULT STANDARD QCI MAPPING)
 

 

查询标准QCI到Pre-R8 QoS映射配置(SHOW STANDARD QCI MAPPING)
 

 

查询标准QCI到Pre-R8 QoS映射缺省配置(SHOW DEFAULT STANDARD QCI MAPPING)
 

 








父主题： [QCI相关配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 设置标准QCI到Pre-R8 QoS映射配置(SET STANDARD QCI MAPPING) 
##### 设置标准QCI到Pre-R8 QoS映射配置(SET STANDARD QCI MAPPING) 


命令功能 

该命令用于修改标准QCI到Pre-R8 QoS映射配置。当需要根据用户在4G网络的QoS中的不同QCI映射出不同的2G、3G网络的QoS时，使用该命令。标准QCI到Pre-R8 QoS映射配置成功后，MME可以根据用户的不同QCI，映射出不同的2G、3G网络的QoS。


注意事项 

标准QCI到Pre-R8 QoS映射配置在开局后就具有缺省值配置。


参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:1~9。|该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier）。QCI用于指示各EPS承载在确定分配和保留时的重要性。 每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，检测到的错误的数据是继续发送，还是丢弃。 取值含义： “不检测（NotDetect）”：不检测发送数据是否正确。“发送（Deliver）”：检测到错误的数据继续发送。“不发送（NotDeliver）”：检测到错误的数据直接丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按顺序传输数据包。取值含义：“按顺序发送（Order）”：承载数据传输时，按顺序传输数据包。“不按顺序发送（NotOrder）”：承载数据传输时，不按顺序传输数据包。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，能够支持的最大数据包的大小。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，承载的业务类型。取值含义：“会话类型（Conversational）”：承载数据传输时，承载的业务类型为会话类型。该类型业务保证数据顺序关系，并严格要求了低延时，适合语音类业务，例如VoIP业务。“流类型（Streaming）”：承载数据传输时，承载的业务类型为流类型。该类型业务保证数据顺序关系，常用于Video视频类业务。“交互类型（Interactive）”：承载数据传输时，承载的业务类型为交互类型。该业务类型保证业务内容的完整性，主要用于传统的Internet应用，例如web浏览。“背景类型（Background）”：承载数据传输时，承载的业务类型为背景类型。该业务类型数据保证业务内容完整性但没有时延要求，主要用于e-mail 下载、SMS、或者ftp下载等。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的业务数据单元错误率。该参数仅在TRAFFCLASS配置为“会话类型（Conversational）”时才生效。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时丢失的、错误的报文占全部报文数的百分比。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数用于指示各EPS承载在数据传输时的相对优先级。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的传输时延。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按最优化信令传输数据包。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。取值含义：“非最优化信令（NotOptimized）”：承载数据传输时，不按最优化信令传输数据包。“最优化信令（Optimized）”：按最优化信令传输数据包。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，数据传输源的类型。取值含义：“未知（UnKnown）”：承载数据传输时，数据传输源的种类为未知类型。“语音（Speech）”：承载数据传输时，数据传输源的种类为语音类型。






命令举例 


设置标准QCI到Pre-R8 QoS映射配置，设置QCI为"1"，其他参数使用系统默认值 。
SET STANDARD QCI MAPPING:QCI=1; 








父主题： [标准QCI到Pre-R8 QoS映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 设置标准QCI到Pre-R8 QoS映射回到缺省值(RESET DEFAULT STANDARD QCI MAPPING) 
##### 设置标准QCI到Pre-R8 QoS映射回到缺省值(RESET DEFAULT STANDARD QCI MAPPING) 


命令功能 

该命令用于将标准QCI到Pre-R8 QoS映射配置还原为缺省值。标准QCI到Pre-R8 QoS映射配置是根据用户在4G网络的QoS中的不同QCI映射出不同的2G、3G网络的QoS。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~9。|该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier）。QCI用于指示各EPS承载在确定分配和保留时的重要性。 每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。






命令举例 


将QCI值为"1"的标准QCI到Pre-R8 QoS映射配置数据还为缺省值。
RESET DEFAULT STANDARD QCI MAPPING:QCI=1; 








父主题： [标准QCI到Pre-R8 QoS映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询标准QCI到Pre-R8 QoS映射配置(SHOW STANDARD QCI MAPPING) 
##### 查询标准QCI到Pre-R8 QoS映射配置(SHOW STANDARD QCI MAPPING) 


命令功能 

该命令用于查询标准QCI到Pre-R8 QoS映射配置。标准QCI到Pre-R8 QoS映射配置是根据用户在4G网络的QoS中的不同QCI映射出不同的2G、3G网络的QoS。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~9。|该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier）。QCI用于指示各EPS承载在确定分配和保留时的重要性。 每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:必选参数；参数类型:整数。|该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier）。QCI用于指示各EPS承载在确定分配和保留时的重要性。 每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，检测到的错误的数据是继续发送，还是丢弃。 取值含义： “不检测（NotDetect）”：不检测发送数据是否正确。“发送（Deliver）”：检测到错误的数据继续发送。“不发送（NotDeliver）”：检测到错误的数据直接丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按顺序传输数据包。取值含义：“按顺序发送（Order）”：承载数据传输时，按顺序传输数据包。“不按顺序发送（NotOrder）”：承载数据传输时，不按顺序传输数据包。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，能够支持的最大数据包的大小。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，承载的业务类型。取值含义：“会话类型（Conversational）”：承载数据传输时，承载的业务类型为会话类型。该类型业务保证数据顺序关系，并严格要求了低延时，适合语音类业务，例如VoIP业务。“流类型（Streaming）”：承载数据传输时，承载的业务类型为流类型。该类型业务保证数据顺序关系，常用于Video视频类业务。“交互类型（Interactive）”：承载数据传输时，承载的业务类型为交互类型。该业务类型保证业务内容的完整性，主要用于传统的Internet应用，例如web浏览。“背景类型（Background）”：承载数据传输时，承载的业务类型为背景类型。该业务类型数据保证业务内容完整性但没有时延要求，主要用于e-mail 下载、SMS、或者ftp下载等。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的业务数据单元错误率。该参数仅在TRAFFCLASS配置为“会话类型（Conversational）”时才生效。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时丢失的、错误的报文占全部报文数的百分比。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数。|该参数用于指示各EPS承载在数据传输时的相对优先级。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的传输时延。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按最优化信令传输数据包。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。取值含义：“非最优化信令（NotOptimized）”：承载数据传输时，不按最优化信令传输数据包。“最优化信令（Optimized）：按最优化信令传输数据包。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，数据传输源的类型。取值含义：“未知（UnKnown）”：承载数据传输时，数据传输源的种类为未知类型。“语音（Speech）：承载数据传输时，数据传输源的种类为语音类型。






命令举例 


查询QCI值为"1"的标准QCI到Pre-R8 QoS映射配置。
SHOW STANDARD QCI MAPPING:QCI=1; 


`

命令 (No.1): SHOW STANDARD QCI MAPPING:QCI=1;

操作维护  QCI     发送错误数据   发送顺序       最大业务数据单元长度   业务类别   业务数据单元错误率   残余位出错率     流量控制优先级   传输时延         信令指示       源统计描述器
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      1       不检测         不按顺序发送   1500 字节 (150)        会话类型   百分之一 (1)         十万分之一 (7)                    100 毫秒 (10)                   语音
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.213 秒）。
` 








父主题： [标准QCI到Pre-R8 QoS映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询标准QCI到Pre-R8 QoS映射缺省配置(SHOW DEFAULT STANDARD QCI MAPPING) 
##### 查询标准QCI到Pre-R8 QoS映射缺省配置(SHOW DEFAULT STANDARD QCI MAPPING) 


命令功能 

该命令用于查询标准QCI到Pre-R8 QoS映射配置的缺省值。标准QCI到Pre-R8 QoS映射配置是根据用户在4G网络的QoS中的不同QCI映射出不同的2、3G网络的QoS。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~9。|该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier）。QCI用于指示各EPS承载在确定分配和保留时的重要性。 每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:必选参数；参数类型:整数。|该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier）。QCI用于指示各EPS承载在确定分配和保留时的重要性。 每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，检测到的错误的数据是继续发送，还是丢弃。 取值含义： “不检测（NotDetect）”：不检测发送数据是否正确。“发送（Deliver）”：检测到错误的数据继续发送。“不发送（NotDeliver）”：检测到错误的数据直接丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按顺序传输数据包。取值含义：“按顺序发送（Order）”：承载数据传输时，按顺序传输数据包。“不按顺序发送（NotOrder）”：承载数据传输时，不按顺序传输数据包。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，能够支持的最大数据包的大小。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，承载的业务类型。取值含义：“会话类型（Conversational）”：承载数据传输时，承载的业务类型为会话类型。该类型业务保证数据顺序关系，并严格要求了低延时，适合语音类业务，例如VoIP业务。“流类型（Streaming）”：承载数据传输时，承载的业务类型为流类型。该类型业务保证数据顺序关系，常用于Video视频类业务。“交互类型（Interactive）”：承载数据传输时，承载的业务类型为交互类型。该业务类型保证业务内容的完整性，主要用于传统的Internet应用，例如web浏览。“背景类型（Background）”：承载数据传输时，承载的业务类型为背景类型。该业务类型数据保证业务内容完整性但没有时延要求，主要用于e-mail 下载、SMS、或者ftp下载等。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的业务数据单元错误率。该参数仅在TRAFFCLASS配置为“会话类型（Conversational）”时才生效。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时丢失的、错误的报文占全部报文数的百分比。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数。|该参数用于指示各EPS承载在数据传输时的相对优先级。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的传输时延。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按最优化信令传输数据包。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。取值含义：“非最优化信令（NotOptimized）”：承载数据传输时，不按最优化信令传输数据包。“最优化信令（Optimized）：按最优化信令传输数据包。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，数据传输源的类型。取值含义：“未知（UnKnown）”：承载数据传输时，数据传输源的种类为未知类型。“语音（Speech）：承载数据传输时，数据传输源的种类为语音类型。






命令举例 


查询QCI值为"1"的标准QCI到Pre-R8 QoS映射缺省配置。
SHOW DEFAULT STANDARD QCI MAPPING:QCI=1; 


`

命令 (No.1): SHOW DEFAULT STANDARD QCI MAPPING:QCI=1;

QCI     发送错误数据   发送顺序       最大业务数据单元长度   业务类别   业务数据单元错误率   残余位出错率     流量控制优先级   传输时延         信令指示       源统计描述器
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1       不检测         不按顺序发送   1500 字节 (150)        会话类型   百分之一 (1)         十万分之一 (7)                    100 毫秒 (10)                   语音
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.157 秒）。
` 








父主题： [标准QCI到Pre-R8 QoS映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 扩展QCI到Pre-R8 QoS映射模板配置 
#### 扩展QCI到Pre-R8 QoS映射模板配置 


背景知识 


用户接入4G网络时，使用的是R8 QoS， 接入2G/3G网络时，使用的是Pre-R8 QoS。 


R8 QoS和Pre-R8 QoS参数形式完全不一样。 


R8 QoS中含有QCI（QoS Class Identifier，QoS等级标识）。QCI 是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。 


3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。 


QCI的取值为1-255，除了9个标准QCI，其他QCI称为扩展QCI，可以由运营商自定义。 


当具有2G/3G/4G接入能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup、从4G移动到2G/3G时，MME需要把R8 QoS转换为Pre R8 QoS，把Pre-R8 QoS传递给UE， UE储存Pre-R8 QoS，UE后续切换到2G/3G网络后，可以直接使用Pre-R8 QoS作为承载上下文的QoS。 




功能描述 



                如果启用扩展QCI，需要进行扩展QCI到Pre-R8 QoS映射配置，由于不同扩展QCI映射的Pre-R8 QoS可能相同，所以将映射后的Pre-R8 QoS单独配置称为扩展QCI到Pre-R8 QoS映射模板，在“扩展QCI配置”命令为（
                [ADD EXQCI]
                ）中配置扩展QCI和映射的Pre-R8 QoS关联关系，即配置其对应的扩展QCI到Pre-R8 QoS映射模板号。
            




相关主题 



 

设置缺省扩展QCI到Pre-R8 QoS映射模板(SET DEFAULT EXQCI TPL)
 

 

查询缺省扩展QCI到Pre-R8 QoS映射模板(SHOW DEFAULT EXQCI TPL)
 

 

新增扩展QCI到Pre-R8 QoS映射模板(ADD EXQCI TPL)
 

 

修改扩展QCI到Pre-R8 QoS映射模板(SET EXQCI TPL)
 

 

删除扩展QCI到Pre-R8 QoS映射模板(DEL EXQCI TPL)
 

 

查询扩展QCI到Pre-R8 QoS映射模板(SHOW EXQCI TPL)
 

 








父主题： [QCI相关配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 设置缺省扩展QCI到Pre-R8 QoS映射模板(SET DEFAULT EXQCI TPL) 
##### 设置缺省扩展QCI到Pre-R8 QoS映射模板(SET DEFAULT EXQCI TPL) 


命令功能 


该命令用于设置缺省扩展QCI到Pre-R8 QoS映射模板。当需要根据用户在LTE网络的QoS中的不同扩展QCI缺省映射出相同的2G、3G网络的QoS时，使用该命令。该命令配置成功后，MME可以将用户不同的扩展QCI值，缺省映射成2G、3G网络相同的QoS。 


不配置该命令时，MME使用系统中模板号为0的默认模板配置，该默认模板可以修改，但不能删除。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，检测到的错误的数据是继续发送，还是丢弃。取值含义：“不检测（NotDetect）”：不检测发送数据是否正确。“发送（Deliver）”：检测到的错误的数据继续发送。“不发送（NotDeliver）”：检测到的错误的数据直接丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按顺序传输数据包。取值含义：“按顺序发送（Order）”：承载数据传输时，按顺序传输数据包。“不按顺序发送（NotOrder）”：承载数据传输时，不按顺序传输数据包。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，能够支持的最大数据包的大小。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，承载的业务类型。取值含义：“会话类型（Conversational）”：承载数据传输时，承载的业务类型为会话类型。该业务类型的数据保证数据顺序关系，并严格要求了低延时，适合语音类业务，例如VoIP业务。“流类型（Streaming）”：承载数据传输时，承载的业务类型为流类型。该业务类型保证数据顺序关系，常用于Video视频类业务。“交互类型（Interactive）”：承载数据传输时，承载的业务类型为交互类型。该业务类型保证业务内容完整性，主要用于传统的Internet应用，例如web浏览。“背景类型（Background）”：承载数据传输时，承载的业务类型为背景类型。该业务类型数据保证业务内容完整性但没有时延要求，主要用于e-mail 下载、SMS或者ftp下载等。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的业务数据单元错误率。该参数仅在TRAFFCLASS配置为“会话类型（Conversational）”时才生效。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时丢失的、错误的报文占全部报文数的百分比。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数用于指示各EPS承载在数据传输时的相对优先级。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的传输时延。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按最优化信令传输数据包。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。取值含义：“非最优化信令（NotOptimized）”：承载数据传输时，不按最优化信令传输数据包。“最优化信令（Optimized）”：按最优化信令传输数据包。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，数据传输源的类型。取值含义：“未知（UnKnown）”：承载数据传输时，数据传输源的种类为未知类。“语音（Speech）”：承载数据传输时，数据传输源的种类为语音类。






命令举例 


按系统默认值设置缺省扩展QCI到Pre-R8 QoS映射模板。 


SET DEFAULT EXQCI TPL 








父主题： [扩展QCI到Pre-R8 QoS映射模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询缺省扩展QCI到Pre-R8 QoS映射模板(SHOW DEFAULT EXQCI TPL) 
##### 查询缺省扩展QCI到Pre-R8 QoS映射模板(SHOW DEFAULT EXQCI TPL) 


命令功能 

该命令用于查询缺省扩展QCI到Pre-R8 QoS映射模板。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，检测到的错误的数据是继续发送，还是丢弃。取值含义：“不检测（NotDetect）”：不检测发送数据是否正确。“发送（Deliver）”：检测到的错误的数据继续发送。“不发送（NotDeliver）”：检测到的错误的数据直接丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按顺序传输数据包。取值含义：“按顺序发送（Order）”：承载数据传输时，按顺序传输数据包。“不按顺序发送（NotOrder）”：承载数据传输时，不按顺序传输数据包。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，能够支持的最大数据包的大小。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，承载的业务类型。取值含义：“会话类型（Conversational）”：承载数据传输时，承载的业务类型为会话类型。该业务类型的数据保证数据顺序关系，并严格要求了低延时，适合语音类业务，例如VoIP业务。“流类型（Streaming）”：承载数据传输时，承载的业务类型为流类型。该业务类型保证数据顺序关系，常用于Video视频类业务。“交互类型（Interactive）”：承载数据传输时，承载的业务类型为交互类型。该业务类型保证业务内容完整性，主要用于传统的Internet应用，例如web浏览。“背景类型（Background）”：承载数据传输时，承载的业务类型为背景类型。该业务类型数据保证业务内容完整性但没有时延要求，主要用于e-mail 下载、SMS或者ftp下载等。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的业务数据单元错误率。该参数仅在TRAFFCLASS配置为“会话类型（Conversational）”时才生效。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时丢失的、错误的报文占全部报文数的百分比。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数。|该参数用于指示各EPS承载在数据传输时的相对优先级。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的传输时延。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按最优化信令传输数据包。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。取值含义：“非最优化信令（NotOptimized）”：承载数据传输时，不按最优化信令传输数据包。“最优化信令（Optimized）”：按最优化信令传输数据包。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，数据传输源的类型。取值含义：“未知（UnKnown）”：承载数据传输时，数据传输源的种类为未知类。“语音（Speech）”：承载数据传输时，数据传输源的种类为语音类。






命令举例 


查询缺省扩展QCI到Pre-R8 QoS映射模板。 


SHOW DEFAULT EXQCI TPL; 


`

命令 (No.1): SHOW DEFAULT EXQCI TPL

操作维护  发送错误数据   发送顺序       最大业务数据单元长度   业务类别   业务数据单元错误率   残余位出错率     流量控制优先级   传输时延         信令指示       源统计描述器
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      不检测         不按顺序发送   1502 字节 (151)        交互类型   万分之一 (4)         千分之四 (4)     1                150 毫秒 (15)    非最优化信令   
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.045 秒）。
` 








父主题： [扩展QCI到Pre-R8 QoS映射模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增扩展QCI到Pre-R8 QoS映射模板(ADD EXQCI TPL) 
##### 新增扩展QCI到Pre-R8 QoS映射模板(ADD EXQCI TPL) 


命令功能 

该命令用于新增扩展QCI到Pre-R8 QoS映射模板配置。当需要根据用户在LTE网络的QoS中的扩展QCI值映射出不同的2G、3G网络的QoS时，使用该命令。该命令配置成功后，可以在扩展QCI配置中新增扩展QCI值到该模板的映射。


注意事项 

该模板配置后，可以通过命令[ADD EXQCI]新增扩展QCI到该模板的映射。


参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|唯一标识一个扩展QCI到Pre-R8 QoS映射模板的ID。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NotDetect。|该参数用于指示承载数据传输时，检测到的错误的数据是继续发送，还是丢弃。取值含义：“不检测（NotDetect）”：不检测发送数据是否正确。“发送（Deliver）”：检测到的错误的数据继续发送。“不发送（NotDeliver）”：检测到的错误的数据直接丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NotOrder。|该参数用于指示承载数据传输时，是否按顺序传输数据包。取值含义：“按顺序发送（Order）”：承载数据传输时，按顺序传输数据包。“不按顺序发送（NotOrder）”：承载数据传输时，不按顺序传输数据包。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:1502 octets。|该参数用于指示承载数据传输时，能够支持的最大数据包的大小。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:Interactive。|该参数用于指示承载数据传输时，承载的业务类型。取值含义：“会话类型（Conversational）”：承载数据传输时，承载的业务类型为会话类型。该业务类型的数据保证数据顺序关系，并严格要求了低延时，适合语音类业务，例如VoIP业务。“流类型（Streaming）”：承载数据传输时，承载的业务类型为流类型。该业务类型保证数据顺序关系，常用于Video视频类业务。“交互类型（Interactive）”：承载数据传输时，承载的业务类型为交互类型。该业务类型保证业务内容完整性，主要用于传统的Internet应用，例如web浏览。“背景类型（Background）”：承载数据传输时，承载的业务类型为背景类型。该业务类型数据保证业务内容完整性但没有时延要求，主要用于e-mail 下载、SMS或者ftp下载等。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:1e-4。|该参数用于指示承载数据传输时的业务数据单元错误率。该参数仅在TRAFFCLASS配置为“会话类型（Conversational）”时才生效。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:4e-3。|该参数用于指示承载数据传输时丢失的、错误的报文占全部报文数的百分比。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数用于指示各EPS承载在数据传输时的相对优先级。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的传输时延。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按最优化信令传输数据包。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。取值含义：“非最优化信令（NotOptimized）”：承载数据传输时，不按最优化信令传输数据包。“最优化信令（Optimized）”：按最优化信令传输数据包。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，数据传输源的类型。取值含义：“未知（UnKnown）”：承载数据传输时，数据传输源的种类为未知类。“语音（Speech）”：承载数据传输时，数据传输源的种类为语音类。






命令举例 


新增扩展QCI到Pre-R8 QoS映射模板，设置模板标识为1，流量控制优先级为2，其他参数采用系统默认值。 


ADD EXQCI TPL:TPLID=1,TRAFHANDPRIO=2; 








父主题： [扩展QCI到Pre-R8 QoS映射模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改扩展QCI到Pre-R8 QoS映射模板(SET EXQCI TPL) 
##### 修改扩展QCI到Pre-R8 QoS映射模板(SET EXQCI TPL) 


命令功能 

该命令用于修改扩展QCI到Pre-R8 QoS映射模板配置属性。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|唯一标识一个扩展QCI到Pre-R8 QoS映射模板的ID。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，检测到的错误的数据是继续发送，还是丢弃。取值含义：“不检测（NotDetect）”：不检测发送数据是否正确。“发送（Deliver）”：检测到的错误的数据继续发送。“不发送（NotDeliver）”：检测到的错误的数据直接丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按顺序传输数据包。取值含义：“按顺序发送（Order）”：承载数据传输时，按顺序传输数据包。“不按顺序发送（NotOrder）”：承载数据传输时，不按顺序传输数据包。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，能够支持的最大数据包的大小。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，承载的业务类型。取值含义：“会话类型（Conversational）”：承载数据传输时，承载的业务类型为会话类型。该业务类型的数据保证数据顺序关系，并严格要求了低延时，适合语音类业务，例如VoIP业务。“流类型（Streaming）”：承载数据传输时，承载的业务类型为流类型。该业务类型保证数据顺序关系，常用于Video视频类业务。“交互类型（Interactive）”：承载数据传输时，承载的业务类型为交互类型。该业务类型保证业务内容完整性，主要用于传统的Internet应用，例如web浏览。“背景类型（Background）”：承载数据传输时，承载的业务类型为背景类型。该业务类型数据保证业务内容完整性但没有时延要求，主要用于e-mail 下载、SMS或者ftp下载等。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的业务数据单元错误率。该参数仅在TRAFFCLASS配置为“会话类型（Conversational）”时才生效。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时丢失的、错误的报文占全部报文数的百分比。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数用于指示各EPS承载在数据传输时的相对优先级。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的传输时延。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按最优化信令传输数据包。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。取值含义：“非最优化信令（NotOptimized）”：承载数据传输时，不按最优化信令传输数据包。“最优化信令（Optimized）”：按最优化信令传输数据包。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，数据传输源的类型。取值含义：“未知（UnKnown）”：承载数据传输时，数据传输源的种类为未知类。“语音（Speech）”：承载数据传输时，数据传输源的种类为语音类。






命令举例 


修改模板标识为1的扩展QCI到Pre-R8 QoS映射模板，将发送顺序修改为按顺序发送。 


SET EXQCI TPL:TPLID=1,DELIORDER="Order"; 








父主题： [扩展QCI到Pre-R8 QoS映射模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除扩展QCI到Pre-R8 QoS映射模板(DEL EXQCI TPL) 
##### 删除扩展QCI到Pre-R8 QoS映射模板(DEL EXQCI TPL) 


命令功能 

该命令用于删除扩展QCI到Pre-R8 QoS映射模板。


注意事项 

删除前，需要先删除映射模板关联的扩展QCI到Pre-R8 QoS的映射关系，删除命令为[DEL EXQCI]。


参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|唯一标识一个扩展QCI到Pre-R8 QoS映射模板的ID。






命令举例 


删除模板标识为1的扩展QCI到Pre-R8 QoS映射模板。 


DEL EXQCI TPL:TPLID=1; 








父主题： [扩展QCI到Pre-R8 QoS映射模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询扩展QCI到Pre-R8 QoS映射模板(SHOW EXQCI TPL) 
##### 查询扩展QCI到Pre-R8 QoS映射模板(SHOW EXQCI TPL) 


命令功能 

该命令用于查询扩展QCI到Pre-R8 QoS映射模板列表。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|唯一标识一个扩展QCI到Pre-R8 QoS映射模板的ID。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
TPLID|模板标识|参数可选性:任选参数；参数类型:整数。|唯一标识一个扩展QCI到Pre-R8 QoS映射模板的ID。
DELIERRSDU|发送错误数据|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，检测到的错误的数据是继续发送，还是丢弃。取值含义：“不检测（NotDetect）”：不检测发送数据是否正确。“发送（Deliver）”：检测到的错误的数据继续发送。“不发送（NotDeliver）”：检测到的错误的数据直接丢弃。
DELIORDER|发送顺序|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按顺序传输数据包。取值含义：“按顺序发送（Order）”：承载数据传输时，按顺序传输数据包。“不按顺序发送（NotOrder）”：承载数据传输时，不按顺序传输数据包。
MAXSDUSIZE|最大业务数据单元长度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，能够支持的最大数据包的大小。
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，承载的业务类型。取值含义：“会话类型（Conversational）”：承载数据传输时，承载的业务类型为会话类型。该业务类型的数据保证数据顺序关系，并严格要求了低延时，适合语音类业务，例如VoIP业务。“流类型（Streaming）”：承载数据传输时，承载的业务类型为流类型。该业务类型保证数据顺序关系，常用于Video视频类业务。“交互类型（Interactive）”：承载数据传输时，承载的业务类型为交互类型。该业务类型保证业务内容完整性，主要用于传统的Internet应用，例如web浏览。“背景类型（Background）”：承载数据传输时，承载的业务类型为背景类型。该业务类型数据保证业务内容完整性但没有时延要求，主要用于e-mail 下载、SMS或者ftp下载等。
SDUERRRATIO|业务数据单元错误率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的业务数据单元错误率。该参数仅在TRAFFCLASS配置为“会话类型（Conversational）”时才生效。
RESIDUALBER|残余位出错率|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时丢失的、错误的报文占全部报文数的百分比。
TRAFHANDPRIO|流量控制优先级|参数可选性:任选参数；参数类型:整数。|该参数用于指示各EPS承载在数据传输时的相对优先级。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。
TRANSDELAY|传输时延|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时的传输时延。
SIGNALIND|信令指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，是否按最优化信令传输数据包。该参数仅在TRAFFCLASS配置为“交互类型（Interactive）”时才生效。取值含义：“非最优化信令（NotOptimized）”：承载数据传输时，不按最优化信令传输数据包。“最优化信令（Optimized）”：按最优化信令传输数据包。
SRCSTADESCRIP|源统计描述器|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示承载数据传输时，数据传输源的类型。取值含义：“未知（UnKnown）”：承载数据传输时，数据传输源的种类为未知类。“语音（Speech）”：承载数据传输时，数据传输源的种类为语音类。






命令举例 


查询所有的扩展QCI到Pre-R8 QoS映射模板。 


SHOW EXQCI TPL; 


`

命令 (No.1): SHOW EXQCI TPL;

操作维护         模板标识   发送错误数据   发送顺序       最大业务数据单元长度   业务类别   业务数据单元错误率   残余位出错率     流量控制优先级   传输时延         信令指示       源统计描述器
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1          不检测         不按顺序发送   1502 字节 (151)        交互类型   万分之一 (4)         千分之四 (4)     1                                 非最优化信令   
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.033 秒）。
` 








父主题： [扩展QCI到Pre-R8 QoS映射模板配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 扩展QCI配置 
#### 扩展QCI配置 


背景知识 


用户接入4G网络时，使用的是R8 QoS， 接入2G/3G网络时，使用的是Pre-R8 QoS。 


R8 QoS和Pre-R8 QoS参数形式完全不一样。 


R8 QoS中含有QCI（QoS Class Identifier，QoS等级标识）。QCI 是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。 


3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。 


QCI的取值为1-255，除了9个标准QCI，其他QCI称为扩展QCI，可以由运营商自定义。 


当具有2G/3G/4G接入能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup、从4G移动到2G/3G时，MME需要把R8 QoS转换为Pre R8 QoS，把Pre-R8 QoS传递给UE， UE储存Pre-R8 QoS，UE后续切换到2G/3G网络后，可以直接使用Pre-R8 QoS作为承载上下文的QoS。 




功能描述 


在如下场景下，需要使用扩展QCI到Pre-R8 QoS映射配置： 



 

具有2G/3G/4G能力的UE，在4G Attach、PDN Connection Setup、Dedicated Bearer Setup流程中建立承载，承载QCI为扩展QCI值，MME把Pre-R8 QoS传递给UE，UE储存Pre-R8 QoS，使UE后续移动到2G/3G后，可以直接使用Pre-R8 QoS作为承载上下文的QoS。
 

 

具有2G/3G/4G能力的UE，移动到2G/3G时，承载QCI为扩展QCI值，MME把R8 QoS映射为Pre-R8 QoS，投递给SGSN。
 

 


扩展QCI到Pre-R8 QoS映射配置需要全网规划。 


配置扩展QCI到Pre-R8 QoS映射的过程如下： 







                        把支持扩展QCI的开关打开，配置命令为：
                        [SET EXQCI SPRT]
                        。
                    







                        配置扩展QCI到Pre-R8 QoS映射模板，配置命令为：
                        [ADD EXQCI TPL]
                        。
                    







                        配置扩展QCI到Pre-R8 QoS映射，配置命令为：
                        [ADD EXQCI]
                        。
                    








相关主题 



 

设置是否支持扩展QCI(SET EXQCI SPRT)
 

 

查询是否支持扩展QCI(SHOW EXQCI SPRT)
 

 

新增扩展QCI配置(ADD EXQCI)
 

 

修改扩展QCI配置(SET EXQCI)
 

 

删除扩展QCI配置(DEL EXQCI)
 

 

查询扩展QCI配置(SHOW EXQCI)
 

 








父主题： [QCI相关配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 设置是否支持扩展QCI(SET EXQCI SPRT) 
##### 设置是否支持扩展QCI(SET EXQCI SPRT) 


命令功能 

该命令用于设置MME是否支持扩展QCI。当运营商需要支持扩展QCI功能时，使用该命令。设置支持扩展QCI成功后，可以将QCI取值范围由原来的1~9扩展为1~255。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
EXQCI|是否支持扩展QCI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持扩展QCI功能。取值含义："NO"：MME不支持扩展QCI。"YES"：MME支持扩展QCI。






命令举例 


设置MME不支持扩展QCI。 


SET EXQCI SPRT:EXQCI="NO"; 








父主题： [扩展QCI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询是否支持扩展QCI(SHOW EXQCI SPRT) 
##### 查询是否支持扩展QCI(SHOW EXQCI SPRT) 


命令功能 

该命令用于查询MME是否支持扩展QCI。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
EXQCI|是否支持扩展QCI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持扩展QCI功能。取值含义："NO"：MME不支持扩展QCI。"YES"：MME支持扩展QCI。






命令举例 


查询MME是否支持扩展QCI。 


SHOW EXQCI SPRT; 


`

命令 (No.1): SHOW EXQCI SPRT;

操作维护  是否支持扩展QCI
-------------------------
修改      否
-------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [扩展QCI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增扩展QCI配置(ADD EXQCI) 
##### 新增扩展QCI配置(ADD EXQCI) 


命令功能 

该命令用于新增扩展QCI值到Pre-R8 QoS映射配置。当需要根据用户在LTE网络的QoS中的扩展QCI值映射出不同的2G、3G网络的QoS时，使用该命令。该命令配置成功后，MME可以根据用户的不同QCI值，映射出不同的2G、3G网络的QoS。


注意事项 



 
该配置生效需要开启“支持扩展QCI”，配置命令为SET EXQCI SPRT 。                
 

 
使用该命令前，需要配置扩展QCI到Pre-R8 QoS映射模板，配置命令为ADD EXQCI TPL 。 
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:10~255。|该参数用于指示服务质量类型。每个QCI值的具体说明，请参见3GPP TS 23.203协议，6.1.7.2节描述。
TPLID|模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数唯一标识一个扩展QCI到Pre-R8 QoS映射模板。






命令举例 


新增扩展QCI配置，QCI值为10，映射模板标识为1。 


ADD EXQCI:QCI=10,TPLID=1; 








父主题： [扩展QCI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改扩展QCI配置(SET EXQCI) 
##### 修改扩展QCI配置(SET EXQCI) 


命令功能 

该命令用于修改扩展QCI值到Pre-R8 QoS映射配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:10~255。|该参数用于指示服务质量类型。每个QCI值的具体说明，请参见3GPP TS 23.203协议，6.1.7.2节描述。
TPLID|模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数唯一标识一个扩展QCI到Pre-R8 QoS映射模板。






命令举例 


修改QCI值为10的扩展QCI配置属性，将模板标识修改为2。 


SET EXQCI:QCI=10,TPLID=2; 








父主题： [扩展QCI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除扩展QCI配置(DEL EXQCI) 
##### 删除扩展QCI配置(DEL EXQCI) 


命令功能 

该命令用于删除扩展QCI值到Pre-R8 QoS映射配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:10~255。|该参数用于指示服务质量类型。每个QCI值的具体说明，请参见3GPP TS 23.203协议，6.1.7.2节描述。






命令举例 


删除QCI值为10的扩展QCI配置。 


DEL EXQCI:QCI=10; 








父主题： [扩展QCI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询扩展QCI配置(SHOW EXQCI) 
##### 查询扩展QCI配置(SHOW EXQCI) 


命令功能 

该命令用于查询扩展QCI值到Pre-R8 QoS映射配置列表。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:10~255。|该参数用于指示服务质量类型。每个QCI值的具体说明，请参见3GPP TS 23.203协议，6.1.7.2节描述。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
QCI|QCI|参数可选性:必选参数；参数类型:整数。|该参数用于指示服务质量类型。每个QCI值的具体说明，请参见3GPP TS 23.203协议，6.1.7.2节描述。
TPLID|模板标识|参数可选性:任选参数；参数类型:整数。|该参数唯一标识一个扩展QCI到Pre-R8 QoS映射模板。






命令举例 


查询QCI值为10的扩展QCI配置信息。 


SHOW EXQCI; 


`

命令 (No.1): SHOW EXQCI

操作维护         QCI   模板标识   给UE的QCI
-------------------------------------------
复制 修改 删除   10    1          1
-------------------------------------------
记录数 1

命令执行成功（耗时 0.022 秒）。
` 








父主题： [扩展QCI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### MME支持大于256Mbps速率控制配置 
### MME支持大于256Mbps速率控制配置 


背景知识 


LTE支持最大20MHz的系统带宽，而LTE-A提出支持最大100MHz的系统带宽要求。为了达到LTE-A的这一要求，3GPP提出了CA（载波聚合，Carrier aggregation）技术。 


载波聚合技术将多个LTE载波聚合成LTE-A系统的传输载波，使系统带宽突破20MHz。 


载波聚合对MME的要求，MME在各个接口支持单用户的速率（包括MBR、GBR、APN-AMBR、UE-AMBR）大于256Mbps。 


本功能目前仅适用于MME网元，SGSN暂不支持此功能。 




功能描述 


“MME支持大于256Mbps速率控制配置”可以方便运营商根据邻接网元支持CA的能力，灵活的设置MME支持的各个接口是否支持超过256Mbps速率。 




相关主题 



 

设置MME支持大于256Mbps速率控制(SET MCAQOSCTL)
 

 

查询MME支持大于256Mbps速率控制(SHOW MCAQOSCTL)
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置MME支持大于256Mbps速率控制(SET MCAQOSCTL) 
#### 设置MME支持大于256Mbps速率控制(SET MCAQOSCTL) 


命令功能 


该命令用于设置MME各个接口是否支持超过256Mbps速率。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IFS11|S11接口是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给SAE-GW发送消息，如果消息中含有MBR/GBR/APN-AMBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR/APN-AMBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。
IFS10|S10接口是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给MME发送消息，如果消息中含有MBR/GBR/APN-AMBR/UE-AMBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR/APN-AMBR/UE-AMBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。
IFS1|S1接口是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给eNB发送消息，如果消息中含有MBR/GBR/UE-AMBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR/UE-AMBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。
IFNAS|NAS接口是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给UE发送消息，如果消息中EPS QoS中的MBR/GBR/APN-AMBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR/APN-AMBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。
IFPRER8|NAS接口Pre-R8 QoS是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给UE发送消息，如果消息中Pre-R8 QoS中的MBR/GBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。






命令举例 


设置MME支持大于256Mbps速率控制配置，S11接口是否支持CA为支持，S10接口是否支持CA为支持。 


SET MCAQOSCTL:IFS11="YES",IFS10="YES"; 








父主题： [MME支持大于256Mbps速率控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询MME支持大于256Mbps速率控制(SHOW MCAQOSCTL) 
#### 查询MME支持大于256Mbps速率控制(SHOW MCAQOSCTL) 


命令功能 


该命令用于查询MME各个接口是否支持超过256Mbps速率配置。 




注意事项 


无。 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
IFS11|S11接口是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给SAE-GW发送消息，如果消息中含有MBR/GBR/APN-AMBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR/APN-AMBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。
IFS10|S10接口是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给MME发送消息，如果消息中含有MBR/GBR/APN-AMBR/UE-AMBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR/APN-AMBR/UE-AMBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。
IFS1|S1接口是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给eNB发送消息，如果消息中含有MBR/GBR/UE-AMBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR/UE-AMBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。
IFNAS|NAS接口是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给UE发送消息，如果消息中EPS QoS中的MBR/GBR/APN-AMBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR/APN-AMBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。
IFPRER8|NAS接口Pre-R8 QoS是否支持CA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME给UE发送消息，如果消息中Pre-R8 QoS中的MBR/GBR，且其速率超过256Mbps，则根据该参数进行控制。取值含义：是：MME按其他网元携带的真实MBR/GBR处理。否：MME对超过256Mbps的速率，按256Mbps速率处理。






命令举例 


查询MME支持大于256Mbps速率控制配置。 


SHOW MCAQOSCTL 


`

命令 (No.1): SHOW MCAQOSCTL

操作维护  S11接口是否支持CA    S10接口是否支持CA   S1接口是否支持CA   NAS接口是否支持CA   NAS接口Pre-R8 QoS是否支持CA
---------------------------------------------------------------------------------------------------------------------
修改      不支持               不支持              不支持             不支持              不支持
---------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.133 秒）。
` 








父主题： [MME支持大于256Mbps速率控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### QoS控制策略配置 
### QoS控制策略配置 


背景知识 


运营商A的用户，如果签约的QoS比较高，当这些用户漫游到运营商B的网络后，运营商B如果要避免该用户占用过多的网络资源，需要通过MME进行本地QoS控制。 


MME对每个承载上下文，需要提供QoS来保障承载的服务质量。EPC网络QoS参数包括： 



 

QCI（QoS Class Identifier，QoS等级标识），QCI是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。QCI的取值为1-255，除了9个标准QCI，其他QCI称为扩展QCI，可以由运营商自定义。
 

 

ARP（Allocation and Retention Priority，分配保留优先级），用于在无线资源限制的情况下决定接受还是拒绝承载的建立或者修改请求，决定丢弃哪个承载。包含有优先级(priority level)、抢占能力标识(pre-emption capability)和被抢占能力标识(pre-emption vulnerability)。priority level具有1-15级别；pre-emption capability：标识该承载能否抢占具有更低优先级承载的资源；pre-emption vulnerability：标识该承载资源能否被具有更高优先级的承载抢占。
 

 

UE-AMBR（User Equipment-Aggregate Maximum Bit Rate，用户设备-累计最大比特率）：用来限制每个UE所有非GBR承载的汇聚最大速率。MME根据APN-AMBR和签约的UE-AMBR（取签约的UE-AMBR与各APN-AMBR之和的小值）计算得出UE-AMBR。
 

 

APN-AMBR（Access Point Name-Aggregate Maximum Bit Rate，接入点名称-累计最大比特率）：用来限制相同APN下所有非GBR承载的汇聚最大速率。
 

 

GBR（Guaranteed Bit Rate，保障速率）：GBR承载能够提供的保证比特率。
 

 

MBR（Maximum Bit Rate，最大比特速率）：GBR承载能够提供的最大比特率。
 

 




功能描述 


MME的QoS控制策略包括： 



 

全局是否支持用户QoS控制。
 

 

是否对用户所在的IMSI号段进行QoS控制，即是否建立进行QoS控制的用户黑白名单，如：对漫游用户进行QoS控制，对本地用户不进行QoS控制。
 

 

是否对用户使用的APN进行QCI控制，即是否建立进行QCI控制的APN黑白名单，如：对IMS APN不进行QCI控制，对其他普通APN进行QCI控制。
 

 

MME是否拒绝已控制的QoS被提升，以及拒绝时携带的拒绝原因。
 

 

MME是否拒绝高于本地QoS的承载的建立和修改，以及拒绝时携带的拒绝原因。
 

 




相关主题 



 

设置QoS控制策略(SET MME QOS POLICY)
 

 

查询QoS控制策略(SHOW MME QOS POLICY)
 

 

新增IMSI号段QoS控制策略(ADD IMSI QOS POLICY)
 

 

修改IMSI号段QoS控制策略(SET IMSI QOS POLICY)
 

 

删除IMSI号段QoS控制策略(DEL IMSI QOS POLICY)
 

 

查询IMSI号段QoS控制策略(SHOW IMSI QOS POLICY)
 

 

新增基于APN的QCI控制策略(ADD APN QCI POLICY)
 

 

修改基于APN的QCI控制策略(SET APN QCI POLICY)
 

 

删除基于APN的QCI控制策略(DEL APN QCI POLICY)
 

 

查询基于APN的QCI控制策略(SHOW APN QCI POLICY)
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置QoS控制策略(SET MME QOS POLICY) 
#### 设置QoS控制策略(SET MME QOS POLICY) 


命令功能 

该命令用于配置MME 是否支持用户QoS控制策略，包括用户是否支持QoS控制、是否控制QCI、是否拒绝已控制的QoS被提升以及拒绝原因、是否拒绝高于本地QoS的承载建立和修改以及拒绝原因。当需要MME进行用户QoS控制时，使用该命令。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
MMESUPQOSCTL|MME是否支持用户QoS控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持用户QoS控制。不支持：MME不支持用户QoS控制。支持：MME支持用户QoS控制。
USERDEFQOSCTL|用户默认QoS控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户默认QoS控制。不控制：用户默认不控制QoS。控制：用户默认控制QoS。
USERDEFQCICTL|用户默认QCI控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户默认QCI控制。不控制：用户默认不控制QCI。控制：用户默认控制QCI。
DEFREJPROQOSCON|MME默认拒绝已控制的QoS被提升|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起附着或PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，该参数用于在这种情况下设置MME默认是否拒绝已控制的QoS被提升。否：默认不拒绝已控制的QoS被提升。是：默认拒绝已控制的QoS被提升。
DEFREJEAMHLOCQOS|MME默认拒绝高于本地QoS的承载建立和修改|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当网络发起承载建立或承载更新请求时，请求中携带的承载级QoS参数高于本地QoS参数，该参数用于在这种情况下设置MME默认是否拒绝高于本地QoS的承载建立和修改。否：默认不拒绝高于本地QoS的承载建立和修改。是：默认拒绝高于本地QoS的承载建立和修改。
ATTREJCAU|附着拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起附着触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，如果MME拒绝已控制的QoS被提升，则需要使用此处配置的附着拒绝原因。
PDNCONREJCAU|PDN连接请求拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，如果MME拒绝已控制的QoS被提升，则需要使用此处配置的PDN连接请求拒绝原因。
UEREQBEAEAMREJCAU|UE请求承载资源建立和修改拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当UE请求承载资源建立和修改时，触发网络发起承载建立或承载更新请求，请求中携带的承载级QoS参数高于本地QoS参数，如果MME拒绝高于本地QoS的承载建立和修改，则需要使用此处配置的UE请求承载资源建立和修改拒绝原因。
BEAEAMREJCAU|承载建立和修改请求拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当网络发起承载建立或承载更新请求时，请求中携带的承载级QoS参数高于本地QoS参数，如果MME拒绝高于本地QoS的承载建立和修改，则需要使用此处配置的承载建立和修改请求拒绝原因。
DELSESSCAU|删除会话原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起附着或PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，如果MME拒绝已控制的QoS被提升，则需要使用此处配置的删除会话原因。
LOCALQOSLAYSUBQOS|本地QoS覆盖签约QoS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置本地QoS参数是否覆盖签约QoS参数。否：不覆盖，即从本地QoS和签约QoS两者中选择服务质量较低的QoS。是：覆盖，即忽略签约QoS。






命令举例 


设置QoS控制策略，MME是否支持用户QoS控制为不支持，用户默认QoS控制为控制。 


SET MME QOS POLICY:MMESUPQOSCTL="NO",USERDEFQOSCTL="YES"; 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询QoS控制策略(SHOW MME QOS POLICY) 
#### 查询QoS控制策略(SHOW MME QOS POLICY) 


命令功能 

该命令用于查询MME 是否支持用户QoS控制策略。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
MMESUPQOSCTL|MME是否支持用户QoS控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持用户QoS控制。不支持：MME不支持用户QoS控制。支持：MME支持用户QoS控制。
USERDEFQOSCTL|用户默认QoS控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户默认QoS控制。不控制：用户默认不控制QoS。控制：用户默认控制QoS。
USERDEFQCICTL|用户默认QCI控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户默认QCI控制。不控制：用户默认不控制QCI。控制：用户默认控制QCI。
DEFREJPROQOSCON|MME默认拒绝已控制的QoS被提升|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起附着或PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，该参数用于在这种情况下设置MME默认是否拒绝已控制的QoS被提升。否：默认不拒绝已控制的QoS被提升。是：默认拒绝已控制的QoS被提升。
DEFREJEAMHLOCQOS|MME默认拒绝高于本地QoS的承载建立和修改|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当网络发起承载建立或承载更新请求时，请求中携带的承载级QoS参数高于本地QoS参数，该参数用于在这种情况下设置MME默认是否拒绝高于本地QoS的承载建立和修改。否：默认不拒绝高于本地QoS的承载建立和修改。是：默认拒绝高于本地QoS的承载建立和修改。
ATTREJCAU|附着拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起附着触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，如果MME拒绝已控制的QoS被提升，则需要使用此处配置的附着拒绝原因。
PDNCONREJCAU|PDN连接请求拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，如果MME拒绝已控制的QoS被提升，则需要使用此处配置的PDN连接请求拒绝原因。
UEREQBEAEAMREJCAU|UE请求承载资源建立和修改拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当UE请求承载资源建立和修改时，触发网络发起承载建立或承载更新请求，请求中携带的承载级QoS参数高于本地QoS参数，如果MME拒绝高于本地QoS的承载建立和修改，则需要使用此处配置的UE请求承载资源建立和修改拒绝原因。
BEAEAMREJCAU|承载建立和修改请求拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当网络发起承载建立或承载更新请求时，请求中携带的承载级QoS参数高于本地QoS参数，如果MME拒绝高于本地QoS的承载建立和修改，则需要使用此处配置的承载建立和修改请求拒绝原因。
DELSESSCAU|删除会话原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起附着或PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，如果MME拒绝已控制的QoS被提升，则需要使用此处配置的删除会话原因。
LOCALQOSLAYSUBQOS|本地QoS覆盖签约QoS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置本地QoS参数是否覆盖签约QoS参数。否：不覆盖，即从本地QoS和签约QoS两者中选择服务质量较低的QoS。是：覆盖，即忽略签约QoS。






命令举例 


查询QoS控制策略。 


SHOW MME QOS POLICY; 


`

(No.9): SHOW MME QOS POLICY

操作维护 MME是否支持用户QoS控制 用户默认QoS控制 用户默认QCI控制 MME默认拒绝已控制的QoS被提升 MME默认拒绝高于本地QoS的承载建立和修改 附着拒绝原因 PDN连接请求拒绝原因 UE请求承载资源建立和修改拒绝原因 承载建立和修改请求拒绝原因 删除会话原因 本地QoS覆盖签约QoS 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改  不支持 不控制 不控制 否 否 EPS services not allowed in this PLMN service option not supported EPS QoS not accepted MME/SGSN refuses due to VPLMN Policy QoS parameter mismatch 否 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.088 秒）。
` 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增IMSI号段QoS控制策略(ADD IMSI QOS POLICY) 
#### 新增IMSI号段QoS控制策略(ADD IMSI QOS POLICY) 


命令功能 

该命令用于配置用户所在的IMSI号段的QoS控制策略，包括是否进行QoS控制、是否拒绝已控制的QoS被提升和是否拒绝高于本地QoS的承载建立。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置QoS控制策略的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。
USERDEFQOSCTL|是否QoS控制|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否对指定的用户IMSI号段进行QoS控制。不控制：对指定的用户IMSI号段不进行QoS控制。控制：对指定的用户IMSI号段进行QoS控制。
REJPROQOSCON|MME拒绝已控制的QoS被提升|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|当用户发起附着或PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，该参数用于在这种情况下设置MME基于用户IMSI号段是否拒绝已控制的QoS被提升。否：对指定的用户IMSI号段，不拒绝已控制的QoS被提升。是：对指定的用户IMSI号段，拒绝已控制的QoS被提升。
REJEAMHLOCQOS|MME拒绝高于本地QoS的承载建立和修改|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|当网络发起承载建立或承载更新请求时，请求中携带的承载级QoS参数高于本地QoS参数，该参数用于在这种情况下设置MME基于用户IMSI号段是否拒绝高于本地QoS的承载建立和修改。否：对指定的用户IMSI号段，不拒绝高于本地QoS的承载建立和修改。是：对指定的用户IMSI号段，拒绝高于本地QoS的承载建立和修改。






命令举例 


新增IMSI号段QoS控制策略，IMSI号段索引为1，是否QoS控制为控制。 


ADD IMSI QOS POLICY:IMSIIDX=1,USERDEFQOSCTL="YES"; 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改IMSI号段QoS控制策略(SET IMSI QOS POLICY) 
#### 修改IMSI号段QoS控制策略(SET IMSI QOS POLICY) 


命令功能 

该命令用于修改用户所在的IMSI号段的QoS控制策略进行QoS控制的配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置QoS控制策略的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。
USERDEFQOSCTL|是否QoS控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否对指定的用户IMSI号段进行QoS控制。不控制：对指定的用户IMSI号段不进行QoS控制。控制：对指定的用户IMSI号段进行QoS控制。
REJPROQOSCON|MME拒绝已控制的QoS被提升|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起附着或PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，该参数用于在这种情况下设置MME基于用户IMSI号段是否拒绝已控制的QoS被提升。否：对指定的用户IMSI号段，不拒绝已控制的QoS被提升。是：对指定的用户IMSI号段，拒绝已控制的QoS被提升。
REJEAMHLOCQOS|MME拒绝高于本地QoS的承载建立和修改|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当网络发起承载建立或承载更新请求时，请求中携带的承载级QoS参数高于本地QoS参数，该参数用于在这种情况下设置MME基于用户IMSI号段是否拒绝高于本地QoS的承载建立和修改。否：对指定的用户IMSI号段，不拒绝高于本地QoS的承载建立和修改。是：对指定的用户IMSI号段，拒绝高于本地QoS的承载建立和修改。






命令举例 


修改IMSI号段QoS控制策略，IMSI号段索引为1，是否QoS控制为控制。 


SET IMSI QOS POLICY:IMSIIDX=1,USERDEFQOSCTL="YES"; 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除IMSI号段QoS控制策略(DEL IMSI QOS POLICY) 
#### 删除IMSI号段QoS控制策略(DEL IMSI QOS POLICY) 


命令功能 

该命令用于删除用户所在的IMSI号段的QoS控制策略进行QoS控制的配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置QoS控制策略的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。






命令举例 


删除IMSI号段QoS控制策略，IMSI号段索引为1。 


DEL IMSI QOS POLICY:IMSIIDX=1; 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询IMSI号段QoS控制策略(SHOW IMSI QOS POLICY) 
#### 查询IMSI号段QoS控制策略(SHOW IMSI QOS POLICY) 


命令功能 

该命令用于查询用户所在的IMSI号段是否进行QoS控制的QoS控制策略。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置QoS控制策略的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数。|该参数用于配置QoS控制策略的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。
USERDEFQOSCTL|是否QoS控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否对指定的用户IMSI号段进行QoS控制。不控制：对指定的用户IMSI号段不进行QoS控制。控制：对指定的用户IMSI号段进行QoS控制。
REJPROQOSCON|MME拒绝已控制的QoS被提升|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当用户发起附着或PDN连接请求触发默认承载建立时，MME本地控制了用户签约的ARP/APN-AMBR/QCI后带给PCEF/PCRF，PCEF/PCRF又提升了已控制的ARP/APN-AMBR/QCI返回给MME，该参数用于在这种情况下设置MME基于用户IMSI号段是否拒绝已控制的QoS被提升。否：对指定的用户IMSI号段，不拒绝已控制的QoS被提升。是：对指定的用户IMSI号段，拒绝已控制的QoS被提升。
REJEAMHLOCQOS|MME拒绝高于本地QoS的承载建立和修改|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当网络发起承载建立或承载更新请求时，请求中携带的承载级QoS参数高于本地QoS参数，该参数用于在这种情况下设置MME基于用户IMSI号段是否拒绝高于本地QoS的承载建立和修改。否：对指定的用户IMSI号段，不拒绝高于本地QoS的承载建立和修改。是：对指定的用户IMSI号段，拒绝高于本地QoS的承载建立和修改。






命令举例 


查询IMSI号段QoS控制策略。 


SHOW IMSI QOS POLICY; 


`

命令 (No.21): SHOW IMSI QOS POLICY

操作维护         IMSI号段索引   是否QoS控制  MME拒绝已控制的QoS被提升 MME拒绝高于本地QoS的承载建立和修改 
----------------------------------------------------------------------------------------------------
复制 修改 删除   1              控制        否                       否
复制 修改 删除   2              不控制      否                       否
----------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.032 秒）。
` 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增基于APN的QCI控制策略(ADD APN QCI POLICY) 
#### 新增基于APN的QCI控制策略(ADD APN QCI POLICY) 


命令功能 

该命令用于配置用户使用的APN是否进行QCI控制。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置APN NI（Network Identifier），格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
QCICTL|是否QCI控制|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否对指定的用户APN进行QCI控制。不控制：对指定的用户APN，不进行QCI控制。控制：对指定的用户APN，进行QCI控制。






命令举例 


新增基于APN的QCI控制策略，APN名称为Label1Label2.Label3，是否QCI控制为不控制。 


ADD APN QCI POLICY:APN="Label1Label2.Label3",QCICTL="NO"; 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改基于APN的QCI控制策略(SET APN QCI POLICY) 
#### 修改基于APN的QCI控制策略(SET APN QCI POLICY) 


命令功能 

该命令用于修改用户使用的APN进行QCI控制的配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置APN NI（Network Identifier），格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
QCICTL|是否QCI控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否对指定的用户APN进行QCI控制。不控制：对指定的用户APN，不进行QCI控制。控制：对指定的用户APN，进行QCI控制。






命令举例 


修改基于APN的QCI控制策略，APN名称为Label1Label2.Label3，修改是否QCI控制为控制。 


SET APN QCI POLICY:APN="Label1Label2.Label3",QCICTL="YES";
 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除基于APN的QCI控制策略(DEL APN QCI POLICY) 
#### 删除基于APN的QCI控制策略(DEL APN QCI POLICY) 


命令功能 

该命令用于删除用户使用的APN进行QCI控制的配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置APN NI（Network Identifier），格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






命令举例 


删除基于APN的QCI控制策略，APN名称为Label1Label2.Label3。 


DEL APN QCI POLICY:APN="Label1Label2.Label3"; 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询基于APN的QCI控制策略(SHOW APN QCI POLICY) 
#### 查询基于APN的QCI控制策略(SHOW APN QCI POLICY) 


命令功能 

该命令用于查询用户使用的APN是否进行QCI控制。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置APN NI（Network Identifier），格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型。|该参数用于设置APN NI（Network Identifier），格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
QCICTL|是否QCI控制|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否对指定的用户APN进行QCI控制。不控制：对指定的用户APN，不进行QCI控制。控制：对指定的用户APN，进行QCI控制。






命令举例 


查询基于APN的QCI控制策略。 


SHOW APN QCI POLICY; 


`

命令 (No.21): SHOW APN QCI POLICY

操作维护        APN名称                 是否QCI控制 
--------------------------------------------------
复制 修改 删除  label1label2.label3     控制 
--------------------------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [QoS控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 用户级QoS控制配置 
### 用户级QoS控制配置 


背景知识 


运营商A的用户，如果签约的QoS比较高，当这些用户漫游到运营商B的网络后，运营商B如果要避免该用户占用过多的网络资源，需要通过MME进行本地QoS控制。 


EPC网络的QoS参数包括以下三个层级： 



 

用户级QoS参数：UE-AMBR。
 

 

会话级QoS参数：APN-AMBR。
 

 

承载级QoS参数：MBR和GBR（GBR承载）。
 

 


MME区分以上三个层级进行用户QoS控制，QoS参数说明参见“QoS控制策略配置”背景知识说明。 




功能描述 


用户级QoS控制配置，提供缺省的UE-AMBR上限配置和基于用户IMSI号段的UE-AMBR上限配置。 




相关主题 



 

设置缺省用户级QoS控制配置(SET DEFAULT SUBSRIBER LEVEL QOS)
 

 

设置缺省用户级QOS控制的所有参数回到缺省值(RESET DEFAULT SUBSRIBER LEVEL QOS)
 

 

查询缺省用户级QoS控制配置(SHOW DEFAULT SUBSRIBER LEVEL QOS)
 

 

新增用户级QoS控制配置(ADD SUBSRIBER LEVEL QOS)
 

 

修改用户级QoS控制配置(SET SUBSRIBER LEVEL QOS)
 

 

删除用户级QoS控制配置(DEL SUBSRIBER LEVEL QOS)
 

 

查询用户级QoS控制配置(SHOW SUBSRIBER LEVEL QOS)
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省用户级QoS控制配置(SET DEFAULT SUBSRIBER LEVEL QOS) 
#### 设置缺省用户级QoS控制配置(SET DEFAULT SUBSRIBER LEVEL QOS) 


命令功能 

该命令用于配置缺省上行UE累计最大比特率上限和缺省下行UE累计最大比特率上限。


注意事项 

如果该命令下的参数不配置，则不在用户级QOS控制配置IMSI号段内的用户，MME不进行UE-AMBR参数控制。


参数说明 


标识|名称|类型|说明
---|---|---|---
UEAMBRUL|上行UE累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置上行UE累计最大比特率上限。
UEAMBRDL|下行UE累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置下行UE累计最大比特率上限。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps






命令举例 


设置缺省用户级QoS控制配置，上行UE累计最大比特率为2Mbps，下行UE累计最大比特率为3Mbps，比特率单位为Mbps。 


SET DEFAULT SUBSRIBER LEVEL QOS:UEAMBRUL=2,UEAMBRDL=3,BITRATE="MBPS"; 








父主题： [用户级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省用户级QOS控制的所有参数回到缺省值(RESET DEFAULT SUBSRIBER LEVEL QOS) 
#### 设置缺省用户级QOS控制的所有参数回到缺省值(RESET DEFAULT SUBSRIBER LEVEL QOS) 


命令功能 

该命令用于设置缺省用户级QoS控制配置的所有参数回到缺省值。当设置的缺省用户级QoS参数的数值异常或者需要重新设置为缺省值时，可以使用该命令。


注意事项 

无。


命令举例 


设置缺省用户级QOS控制的所有参数回到缺省值。 


RESET DEFAULT SUBSRIBER LEVEL QOS; 








父主题： [用户级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询缺省用户级QoS控制配置(SHOW DEFAULT SUBSRIBER LEVEL QOS) 
#### 查询缺省用户级QoS控制配置(SHOW DEFAULT SUBSRIBER LEVEL QOS) 


命令功能 

该命令用于查询缺省上行UE累计最大比特率和缺省下行UE累计最大比特率。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
UEAMBRUL|上行UE累计最大比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置IMSI号段下的上行UE累计最大比特率上限。
UEAMBRDL|下行UE累计最大比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置IMSI号段下的下行UE累计最大比特率上限。






命令举例 


查询缺省用户级QoS控制配置。 


SHOW DEFAULT SUBSRIBER LEVEL QOS; 


`

命令 (No.15): SHOW DEFAULT SUBSRIBER LEVEL QOS

操作维护  上行UE累计最大比特率(Kbps)   下行UE累计最大比特率(Kbps)
-----------------------------------------------------------------
修改      2000                         3000
-----------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.04 秒）。
` 








父主题： [用户级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增用户级QoS控制配置(ADD SUBSRIBER LEVEL QOS) 
#### 新增用户级QoS控制配置(ADD SUBSRIBER LEVEL QOS) 


命令功能 

该命令用于配置基于IMSI号段的上行UE累计最大比特率上限和下行UE累计最大比特率上限。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置用户级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。
UEAMBRUL|上行UE累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置上行UE累计最大比特率上限。
UEAMBRDL|下行UE累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置下行UE累计最大比特率上限。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps






命令举例 


新增用户级QoS控制配置，IMSI号段索引为1，上行UE累计最大比特率为2Mbps，下行UE累计最大比特率为3Mbps，比特率单位为Mbps。 


ADD SUBSRIBER LEVEL QOS:IMSIIDX=1,UEAMBRUL=2,UEAMBRDL=3,BITRATE="MBPS"; 








父主题： [用户级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改用户级QoS控制配置(SET SUBSRIBER LEVEL QOS) 
#### 修改用户级QoS控制配置(SET SUBSRIBER LEVEL QOS) 


命令功能 

该命令用于修改基于IMSI号段的上行UE累计最大比特率上限和下行UE累计最大比特率上限。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置用户级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。
UEAMBRUL|上行UE累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置上行UE累计最大比特率上限。
UEAMBRDL|下行UE累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置下行UE累计最大比特率上限。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps






命令举例 


修改用户级QoS控制配置，IMSI号段索引为1，上行UE累计最大比特率为2Mbps，下行UE累计最大比特率为3Mbps，比特率单位为Mbps。 


SET SUBSRIBER LEVEL QOS:IMSIIDX=1,UEAMBRUL=2,UEAMBRDL=3,BITRATE="MBPS"; 








父主题： [用户级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除用户级QoS控制配置(DEL SUBSRIBER LEVEL QOS) 
#### 删除用户级QoS控制配置(DEL SUBSRIBER LEVEL QOS) 


命令功能 

该命令用于删除基于IMSI号段的上行UE累计最大比特率上限和下行UE累计最大比特率上限。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置用户级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。






命令举例 


删除用户级QoS控制配置，IMSI号段索引为1。 


DEL SUBSRIBER LEVEL QOS:IMSIIDX=1; 








父主题： [用户级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询用户级QoS控制配置(SHOW SUBSRIBER LEVEL QOS) 
#### 查询用户级QoS控制配置(SHOW SUBSRIBER LEVEL QOS) 


命令功能 

该命令用于查询基于IMSI号段的上行UE累计最大比特率上限和下行UE累计最大比特率上限。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置用户级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:必选参数；参数类型:整数。|该参数用于配置用户级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用。
UEAMBRUL|上行UE累计最大比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置IMSI号段下的上行UE累计最大比特率上限。
UEAMBRDL|下行UE累计最大比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置IMSI号段下的下行UE累计最大比特率上限。






命令举例 


查询用户级QoS控制配置。 


SHOW SUBSRIBER LEVEL QOS:IMSIIDX=1; 


`

命令 (No.16): SHOW SUBSRIBER LEVEL QOS:IMSIIDX=1;

操作维护         IMSI号段索引   上行UE累计最大比特率(Kbps)   下行UE累计最大比特率(Kbps)
---------------------------------------------------------------------------------------
复制 修改 删除   1              23000                            
---------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [用户级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 会话级QoS控制配置 
### 会话级QoS控制配置 


背景知识 


运营商A的用户，如果签约的QoS比较高，当这些用户漫游到运营商B的网络后，运营商B如果要避免该用户占用过多的网络资源，需要通过MME进行本地QoS控制。 


EPC网络的QoS参数包括以下三个层级： 



 

用户级QoS参数：UE-AMBR。
 

 

会话级QoS参数：APN-AMBR。
 

 

承载级QoS参数：MBR和GBR（GBR承载）。
 

 


MME区分以上三个层级进行用户QoS控制，QoS参数说明参见“QoS控制策略配置”背景知识说明。 




功能描述 


MME基于IMSI和APN NI两个维度进行会话级QoS控制： 



 

IMSI用来区分漫游和非漫游用户。
 

 

APN NI用来区分普通业务和特殊业务（如语音）。
 

 


会话级QoS控制配置，提供缺省的APN-AMBR上限配置和基于用户IMSI号段、APN NI及IMSI号段+APN NI的APN-AMBR上限配置。 




相关主题 



 

设置缺省会话级QoS控制配置(SET DEFAULT SESSION LEVEL QOS)
 

 

设置缺省会话级QOS控制的所有参数回到缺省值(RESET DEFAULT SESSION LEVEL QOS)
 

 

查询缺省会话级QoS控制配置(SHOW DEFAULT SESSION LEVEL QOS)
 

 

新增会话级QoS控制配置(ADD SESSION LEVEL QOS)
 

 

修改会话级QoS控制配置(SET SESSION LEVEL QOS)
 

 

删除会话级QoS控制配置(DEL SESSION LEVEL QOS)
 

 

查询会话级QoS控制配置(SHOW SESSION LEVEL QOS)
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省会话级QoS控制配置(SET DEFAULT SESSION LEVEL QOS) 
#### 设置缺省会话级QoS控制配置(SET DEFAULT SESSION LEVEL QOS) 


命令功能 

该命令用于配置缺省上行APN累计最大比特率和缺省下行APN累计最大比特率。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APNAMBRUL|上行APN累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置上行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
APNAMBRDL|下行APN累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置下行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps






命令举例 


设置缺省会话级QoS控制配置，上行APN累计最大比特率为2Mbps，下行APN累计最大比特率2Mbps，比特率单位为Mbps。 


SET DEFAULT SESSION LEVEL QOS:APNAMBRUL=2,APNAMBRDL=3,BITRATE="MBPS"; 








父主题： [会话级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省会话级QOS控制的所有参数回到缺省值(RESET DEFAULT SESSION LEVEL QOS) 
#### 设置缺省会话级QOS控制的所有参数回到缺省值(RESET DEFAULT SESSION LEVEL QOS) 


命令功能 

该命令用于设置缺省会话级QOS控制的缺省上行APN累计最大比特率和缺省下行APN累计最大比特率回到缺省值。


注意事项 

无。


命令举例 


设置缺省会话级QOS控制的所有参数回到缺省值。 


RESET DEFAULT SESSION LEVEL QOS; 








父主题： [会话级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询缺省会话级QoS控制配置(SHOW DEFAULT SESSION LEVEL QOS) 
#### 查询缺省会话级QoS控制配置(SHOW DEFAULT SESSION LEVEL QOS) 


命令功能 

该命令用于查询缺省上行APN累计最大比特率和缺省下行APN累计最大比特率。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNAMBRUL|上行APN累计最大比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置上行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
APNAMBRDL|下行APN累计最大比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置下行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。






命令举例 


查询缺省会话级QoS控制配置。 


SHOW DEFAULT SESSION LEVEL QOS; 


`

命令 (No.9): SHOW DEFAULT SESSION LEVEL QOS

操作维护  上行APN累计最大比特率(Kbps)   下行APN累计最大比特率(Kbps)
-------------------------------------------------------------------
修改      2048                          3008
-------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.047 秒）。
` 








父主题： [会话级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增会话级QoS控制配置(ADD SESSION LEVEL QOS) 
#### 新增会话级QoS控制配置(ADD SESSION LEVEL QOS) 


命令功能 

该命令用于新增基于用户IMSI号段或APN NI或IMSI号段+APN NI的上行APN累计最大比特率上限和下行APN累计最大比特率上限配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置会话级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNAMBRUL|上行APN累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置上行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
APNAMBRDL|下行APN累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置下行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps






命令举例 


新增会话级QoS控制配置，IMSI号段索引为1，APN名称为zte，上行APN累计最大比特率为2Mbps，下行APN累计最大比特率2Mbps，比特率单位为Mbps。 


ADD SESSION LEVEL QOS:IMSIIDX=1,APN="zte",APNAMBRUL=2,APNAMBRDL=3,BITRATE="MBPS"; 








父主题： [会话级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改会话级QoS控制配置(SET SESSION LEVEL QOS) 
#### 修改会话级QoS控制配置(SET SESSION LEVEL QOS) 


命令功能 

该命令用于修改基于用户IMSI号段或APN NI或IMSI号段+APN NI的上行APN累计最大比特率上限和下行APN累计最大比特率上限配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置会话级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNAMBRUL|上行APN累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置上行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
APNAMBRDL|下行APN累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置下行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps






命令举例 


修改会话级QoS控制配置，IMSI号段索引为1，APN名称为zte，上行APN累计最大比特率为2Mbps，下行APN累计最大比特率2Mbps，比特率单位为Mbps。 


SET SESSION LEVEL QOS:IMSIIDX=1,APN="zte",APNAMBRUL=2,APNAMBRDL=3,BITRATE="MBPS"; 








父主题： [会话级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除会话级QoS控制配置(DEL SESSION LEVEL QOS) 
#### 删除会话级QoS控制配置(DEL SESSION LEVEL QOS) 


命令功能 

该命令用于删除基于用户IMSI号段或APN NI或IMSI号段+APN NI的上行APN累计最大比特率上限和下行APN累计最大比特率上限配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置会话级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






命令举例 


删除会话级QoS控制配置，IMSI号段索引为1，APN名称为zte。 


DEL SESSION LEVEL QOS:IMSIIDX=1,APN="zte"; 








父主题： [会话级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询会话级QoS控制配置(SHOW SESSION LEVEL QOS) 
#### 查询会话级QoS控制配置(SHOW SESSION LEVEL QOS) 


命令功能 

该命令用于查询基于用户IMSI号段或APN NI或IMSI号段+APN NI的上行APN累计最大比特率上限和下行APN累计最大比特率上限配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置会话级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数。|该参数用于配置会话级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNAMBRUL|上行APN累计最大比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置上行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
APNAMBRDL|下行APN累计最大比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置下行APN累计最大比特率。3GPP NAS口协议24.301第 9.9.4.2.1节定义的APN-AMBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;256 Mbps到10Gbps，步长256 Mbps;如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。






命令举例 


查询会话级QoS控制配置，IMSI号段索引为1。 


SHOW SESSION LEVEL QOS:IMSIIDX=1; 


`

命令 (No.12): SHOW SESSION LEVEL QOS:IMSIIDX=1;

操作维护         IMSI号段索引   APN名称   上行APN累计最大比特率(Kbps)   下行APN累计最大比特率(Kbps)
---------------------------------------------------------------------------------------------------
复制 修改 删除   1              aaaa      1000                                  
---------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.037 秒）。
` 








父主题： [会话级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 承载级QoS控制配置 
### 承载级QoS控制配置 


背景知识 


某些地区（如A地）运营商的用户，如果签约的QoS比其他地区（如B地区）的用户等级高，当这些A地区的用户漫游到B地区后，B地区的运营商要避免A地区用户占用过多的网络资源，需要MME进行本地QoS控制。 


MME对每个承载上下文，需要提供QoS，来保障承载的服务质量。EPC网络QOS参数包括： 



 

QCI（QoS Class Identifier，QoS等级标识），QCI 是一个数量等级，代表eNodeB用于控制承载级别的包转发处理的特定参数，如承载的优先级、时延、误码率等。3GPP TS 23.203协议预定义了9个标准QCI（1-9），对每个标准QCI，协议定义了特定的优先级、时延、误码率等。QCI的取值为1-255，除了9个标准QCI，其他QCI称为扩展QCI，可以由运营商自定义。
 

 

ARP（分配保留优先级），用于在无线资源限制的情况下决定接受还是拒绝承载的建立或者修改请求，决定丢弃哪个承载。包含有优先级(priority level)、抢占能力标志(pre-emption capability)和被抢占能力(pre-emption vulnerability)。priority level具有1-15级别；pre-emption capability：该承载能否抢占具有更低优先级的资源标识；pre-emption vulnerability：该承载资源能否被具有更高优先级的承载抢占标识。
 

 

UE-AMBR（User Equipment-Aggregate Maximum Bit Rate，用户设备-累计最大比特率）：用来限制每个UE所有非GBR承载的汇聚最大速率的QoS参数。MME根据APN-AMBR和签约的UE-AMBR（取签约的UE-AMBR与各APN-AMBR之和的小值）计算UE-AMBR。
 

 

APN-AMBR（Access Point Name-Aggregate Maximum Bit Rate，接入点名称-累计最大比特率）用来限制相同APN下所有非GBR承载的汇聚最大速率的QoS参数。
 

 

GBR（Guaranteed Bit Rate，保障速率）：GBR承载能够提供的保证比特率。
 

 

MBR（Maximum Bit Rate，最大比特速率）：GBR承载能够提供的最大比特率。
 

 




功能描述 


MME基于IMSI，APN，QCI和ARP四个维度进行QoS控制： 



 

IMSI用来区分漫游和非漫游用户。
 

 

APN用来区分普通业务和特殊业务（如语音）。
 

 

QCI和ARP用来区分普通承载和特殊承载（IMS信令承载、IMS语音承载）。
 

 


承载级QoS控制配置，提供缺省的MBR和GBR上限配置和基于用户IMSI号段、APN NI、QCI和ARP的MBR和GBR上限配置，IMSI，APN，QCI和ARP四个维度的组合关系及优先级按照从高到低排序如下： 



 

1． IMSI+APN+QCI+ARP
 

 

2． IMSI+APN+QCI
 

 

3． IMSI+QCI+ARP
 

 

4． IMSI+APN
 

 

5． IMSI+QCI
 

 

6． IMSI+APN+ARP
 

 

7． IMSI+ARP
 

 

8． IMSI
 

 

9． APN+QCI+ARP
 

 

10． APN+QCI
 

 

11． QCI+ARP
 

 

12． APN
 

 

13． QCI
 

 

14． APN+ARP
 

 

15． ARP
 

 




相关主题 



 

设置缺省承载级QoS控制配置(SET DEFAULT BEARER LEVEL QOS)
 

 

设置缺省承载级QOS控制的所有参数回到缺省值(RESET DEFAULT BEARER LEVEL QOS)
 

 

查询缺省承载级QoS控制配置(SHOW DEFAULT BEARER LEVEL QOS)
 

 

新增承载级QoS控制配置(ADD BEARER LEVEL QOS)
 

 

修改承载级QoS控制配置(SET BEARER LEVEL QOS)
 

 

删除承载级QoS控制配置(DEL BEARER LEVEL QOS)
 

 

查询承载级QoS控制配置(SHOW BEARER LEVEL QOS)
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省承载级QoS控制配置(SET DEFAULT BEARER LEVEL QOS) 
#### 设置缺省承载级QoS控制配置(SET DEFAULT BEARER LEVEL QOS) 


命令功能 

该命令用于配置缺省最大上/下行链路比特率和缺省保证上/下行链路比特率上限。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置最大上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置最大下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置保证上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置保证下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps
BEARARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置ARP抢占能力。0：不抢占1：抢占
BEARARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|设置ARP优先级。
BEARARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置ARP被抢占能力。






命令举例 


设置最大上行链路比特率为2Mbps,最大下行链路比特率为3Mbps，保证上行链路比特率为4Mbps，保证下行链路比特率为5Mpbs，比特率单位为Mbps。 


SET DEFAULT BEARER LEVEL QOS:MAXBITRATEUL=2,MAXBITRATEDL=3,GUARBITRATEUL=4,GUARBITRATEDL=5,BITRATE="MBPS" 








父主题： [承载级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省承载级QOS控制的所有参数回到缺省值(RESET DEFAULT BEARER LEVEL QOS) 
#### 设置缺省承载级QOS控制的所有参数回到缺省值(RESET DEFAULT BEARER LEVEL QOS) 


命令功能 

该命令用于设置承载级QOS控制配置的所有参数回到缺省值。当设置的缺省承载级QoS参数的数值异常或者需要重新设置为缺省值时，可以使用该命令。


注意事项 

无。


命令举例 


设置缺省承载级QOS控制的所有参数回到缺省值。 


RESET DEFAULT BEARER LEVEL QOS 








父主题： [承载级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询缺省承载级QoS控制配置(SHOW DEFAULT BEARER LEVEL QOS) 
#### 查询缺省承载级QoS控制配置(SHOW DEFAULT BEARER LEVEL QOS) 


命令功能 

该命令用于查询缺省最大上/下行链路比特率和缺省保证上/下行链路比特率上限。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
MAXBITRATEUL|最大上行链路比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置最大上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
MAXBITRATEDL|最大下行链路比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置最大下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEUL|保证上行链路比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置保证上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEDL|保证下行链路比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置保证下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
BEARARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置ARP抢占能力。0：不抢占1：抢占
BEARARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数。|设置ARP优先级。
BEARARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置ARP被抢占能力。






命令举例 


查询缺省最大上/下行链路比特率和缺省保证上/下行链路比特率上限。 


SHOW DEFAULT BEARER LEVEL QOS 


`

命令 (No.5): SHOW DEFAULT BEARER LEVEL QOS

操作维护  最大上行链路比特率(Kbps)   最大下行链路比特率(Kbps)   保证上行链路比特率(Kbps)   保证下行链路比特率(Kbps)   ARP抢占能力   ARP优先级   ARP被抢占能力
-------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      2048                       3008                       4032                       5056                       抢占          1           被抢占
-------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.029 秒）。
` 








父主题： [承载级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增承载级QoS控制配置(ADD BEARER LEVEL QOS) 
#### 新增承载级QoS控制配置(ADD BEARER LEVEL QOS) 


命令功能 

该命令用于新增用户IMSI号段、APN NI、QCI和ARP一个或多个维度的上最大上/下行链路比特率保证上/下行链路比特率上限配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置承载级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置QoS分类标识。
ARP|ARP|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数用于设置分配保留优先级。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置最大上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置最大下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置保证上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置保证下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps
BEARARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置ARP抢占能力。0：不抢占1：抢占
BEARARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|设置ARP优先级。
BEARARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置ARP被抢占能力。






命令举例 


新增承载级QoS控制配置，IMSI号段索引为1，APN名称为zte，QCI为2，ARP为3，最大上行链路比特率为2Mbps,最大下行链路比特率为3Mbps，保证上行链路比特率为4Mbps，保证下行链路比特率为5Mpbs，比特率单位为Mbps。 


ADD BEARER LEVEL QOS:IMSIIDX=1,APN="apn",QCI=2,ARP=3,MAXBITRATEUL=2,MAXBITRATEDL=3,GUARBITRATEUL=4,GUARBITRATEDL=5,BITRATE="MBPS" 








父主题： [承载级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改承载级QoS控制配置(SET BEARER LEVEL QOS) 
#### 修改承载级QoS控制配置(SET BEARER LEVEL QOS) 


命令功能 

该命令用于修改用户IMSI号段、APN NI、QCI和ARP一个或多个维度的上最大上/下行链路比特率和保证上/下行链路比特率上限配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置承载级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置QoS分类标识。
ARP|ARP|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数用于设置分配保留优先级。
MAXBITRATEUL|最大上行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置最大上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
MAXBITRATEDL|最大下行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置最大下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEUL|保证上行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置保证上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEDL|保证下行链路比特率|参数可选性:任选参数；参数类型:整数；参数范围为:1~4000000000。|该参数用于设置保证下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
BITRATE|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:KBPS。|该参数用于设置比特率单位。有三个：KBPS：单位为KbpsMBPS：单位为MbpsGBPS：单位为Gbps
BEARARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置ARP抢占能力。0：不抢占1：抢占
BEARARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|设置ARP优先级。
BEARARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置ARP被抢占能力。






命令举例 


修改承载级QoS控制配置，IMSI号段索引为1，APN名称为zte，QCI为2，ARP为3，最大上行链路比特率为2Mbps,最大下行链路比特率为3Mbps，保证上行链路比特率为4Mbps，保证下行链路比特率为5Mpbs，比特率单位为Mbps。 


SET BEARER LEVEL QOS:IMSIIDX=1,APN="zte",QCI=2,ARP=3,MAXBITRATEUL=2,MAXBITRATEDL=3,GUARBITRATEUL=4,GUARBITRATEDL=5,BITRATE="MBPS" 








父主题： [承载级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除承载级QoS控制配置(DEL BEARER LEVEL QOS) 
#### 删除承载级QoS控制配置(DEL BEARER LEVEL QOS) 


命令功能 

该命令用于删除用户IMSI号段、APN NI、QCI和ARP一个或多个维度的上最大上/下行链路比特率和缺省保证上/下行链路比特率上限配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置承载级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置QoS分类标识。
ARP|ARP|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数用于设置分配保留优先级。






命令举例 


删除承载级QoS控制配置，IMSI号段索引为1，APN名称为zte，QCI为2，ARP为3。 


DEL BEARER LEVEL QOS:IMSIIDX=1,APN="zte",QCI=2,ARP=3 








父主题： [承载级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询承载级QoS控制配置(SHOW BEARER LEVEL QOS) 
#### 查询承载级QoS控制配置(SHOW BEARER LEVEL QOS) 


命令功能 

该命令用于查询用户IMSI号段、APN NI、QCI和ARP一个或多个维度的上最大上/下行链路比特率和缺省保证上/下行链路比特率上限配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置承载级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置QoS分类标识。
ARP|ARP|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数用于设置分配保留优先级。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数。|该参数用于配置承载级QoS控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
QCI|QCI|参数可选性:任选参数；参数类型:整数。|该参数用于设置QoS分类标识。
ARP|ARP|参数可选性:任选参数；参数类型:整数。|该参数用于设置分配保留优先级。
MAXBITRATEUL|最大上行链路比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置最大上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
MAXBITRATEDL|最大下行链路比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置最大下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEUL|保证上行链路比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置保证上行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
GUARBITRATEDL|保证下行链路比特率(Kbps)|参数可选性:任选参数；参数类型:整数。|该参数用于设置保证下行链路比特率上限。3GPP NAS口协议24.301第 9.9.4.3节定义的MBR是非连续的：1 kbps到63 kbps，步长1 kbps，例如：1 kbps，2 kbps，3 kbps，….，63kbps;64 kbps到 568 kbps，步长8 kbps，例如：64 kbps，72 kbps，80 kbps，…，568 kbps;576 kbps到8640 kbps，步长64 kbps，例如：576 kbps，640 kbps，704 kbps，…，8640 kbps;8700 kbps到16000 kbps，步长100 kbps，例如：8700 kbps，8800 kbps，8900 kbps，…，16000 kbps;17 Mbps到128 Mbps，步长1 Mbps，例如：17 Mbps，18 Mbps，19 Mbps，…，128 Mbps;130 Mbps 到256 Mbps，步长2 Mbps，例如：130 Mbps，132 Mbps，134 Mbps，…，256 Mbps;260 Mbps to 500 Mbps，步长4Mbps，例如：260 Mbps，264Mbps，268 Mbps，…，500 Mbps;510 Mbps to 1500 Mbps，步长10 Mbps，例如：510 Mbps，520 Mbps，530 Mbps，…，1500 Mbps1600 Mbps to 10 Gbps，步长100 Mbps，例如：1700 Mbps，1800 Mbps，1900 Mbps，…，10 Gbps如果用户输入如68 kbps，则MME会将该值强制修改为72 kbps，即对在协议定义区间值内的值进行向上取整。
BEARARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置ARP抢占能力。0：不抢占1：抢占
BEARARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数。|设置ARP优先级。
BEARARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置ARP被抢占能力。






命令举例 


查询承载级QoS控制配置,IMSI号段索引为1。 


SHOW BEARER LEVEL QOS:IMSIIDX=1 


`

命令 (No.7): SHOW BEARER LEVEL QOS:IMSIIDX=1

操作维护         IMSI号段索引   APN名称   QCI   ARP   最大上行链路比特率(Kbps)   最大下行链路比特率(Kbps)   保证上行链路比特率(Kbps)   保证下行链路比特率(Kbps)   ARP抢占能力   ARP优先级   ARP被抢占能力
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1              aaaa      1     1     11000                      12000                      13000                      14000                      抢占          1           被抢占
复制 修改 删除   1              zte       2     3     2                                                                                    
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.033 秒）。
` 








父主题： [承载级QoS控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 默认承载ARP和QCI控制配置 
### 默认承载ARP和QCI控制配置 


背景知识 


运营商A的用户，如果签约的QoS比较高，当这些用户漫游到运营商B的网络后，运营商B如果要避免该用户占用过多的网络资源，需要通过MME进行本地QoS控制。 


EPC网络用户签约的QoS参数包括APN-AMBR、QCI和ARP，QoS参数说明参见“QoS控制策略配置”背景知识说明。 




功能描述 


MME基于IMSI和APN两个维度进行QoS控制： 



 

IMSI用来区分漫游和非漫游用户。
 

 

APN用来区分普通业务和特殊业务（如语音）。
 

 


默认承载ARP和QCI控制配置，提供缺省的ARP和QCI控制配置和基于用户IMSI号段或APN NI的ARP和QCI控制配置。 




相关主题 



 

设置缺省默认承载ARP和QCI控制配置(SET DEFAULT BEARER ARP QCI)
 

 

设置缺省默认承载ARP和QCI控制的所有参数回到缺省值(RESET DEFAULT BEARER ARP QCI)
 

 

查询缺省默认承载ARP和QCI控制配置(SHOW DEFAULT BEARER ARP QCI)
 

 

新增默认承载ARP和QCI控制配置(ADD BEARER ARP QCI)
 

 

修改默认承载ARP和QCI控制配置(SET BEARER ARP QCI)
 

 

删除默认承载ARP和QCI控制配置(DEL BEARER ARP QCI)
 

 

查询默认承载ARP和QCI控制配置(SHOW BEARER ARP QCI)
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省默认承载ARP和QCI控制配置(SET DEFAULT BEARER ARP QCI) 
#### 设置缺省默认承载ARP和QCI控制配置(SET DEFAULT BEARER ARP QCI) 


命令功能 

该命令用于配置缺省默认承载的ARP和QCI控制。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
ARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数用于设置缺省分配保留优先级。
ARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP抢占能力。不能抢占：该承载不能抢占具有更低优先级承载的资源。抢占：该承载能抢占具有更低优先级承载的资源。
ARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP被抢占能力。不被抢占：该承载资源不能被具有更高优先级的承载抢占。被抢占：该承载资源能被具有更高优先级的承载抢占。
QCIMAP|QCI映射|参数可选性:任选参数；参数类型:复合参数|该参数用于设置缺省QoS分类标识映射。
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置缺省QoS分类标识，取值为[0,255]和65535。65535是该参数的通配值，未配置的QCI可以使用65535对应的映射QCI值。
MAPQCI|映射QCI|参数可选性:必选参数；参数类型:整数；参数范围为:5~255。|该参数用于设置缺省映射QoS分类标识。






命令举例 


设置缺省默认承载ARP和QCI控制配置，ARP优先级为1，ARP抢占能力为不能抢占，ARP被抢占能力为被抢占，QCI为112（映射QCI为5）和QCI为65535（映射QCI为100）。 


SET DEFAULT BEARER ARP QCI:ARPPRI=1,ARPPEC="NO",ARPPEV="YES",QCIMAP=112-5&65535-100; 








父主题： [默认承载ARP和QCI控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省默认承载ARP和QCI控制的所有参数回到缺省值(RESET DEFAULT BEARER ARP QCI) 
#### 设置缺省默认承载ARP和QCI控制的所有参数回到缺省值(RESET DEFAULT BEARER ARP QCI) 


命令功能 

该命令用于设置默认承载ARP和QCI控制配置的所有参数回到缺省值。当设置的缺省默认承载ARP和QCI参数的数值异常或者需要重新设置为缺省值时，可以使用该命令。


注意事项 

无。


命令举例 


设置默认承载ARP和QCI控制配置的所有参数回到缺省值。 


RESET DEFAULT BEARER ARP QCI; 








父主题： [默认承载ARP和QCI控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询缺省默认承载ARP和QCI控制配置(SHOW DEFAULT BEARER ARP QCI) 
#### 查询缺省默认承载ARP和QCI控制配置(SHOW DEFAULT BEARER ARP QCI) 


命令功能 

该命令用于查询缺省默认承载的ARP和QCI控制。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
ARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数。|该参数用于设置缺省分配保留优先级。
ARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP抢占能力。不能抢占：该承载不能抢占具有更低优先级承载的资源。抢占：该承载能抢占具有更低优先级承载的资源。
ARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP被抢占能力。不被抢占：该承载资源不能被具有更高优先级的承载抢占。被抢占：该承载资源能被具有更高优先级的承载抢占。
QCIMAP|QCI映射|参数可选性:任选参数；参数类型:字符型。|该参数用于设置缺省QoS分类标识映射。






命令举例 


查询缺省默认承载ARP和QCI控制配置。 


SHOW DEFAULT BEARER ARP QCI; 


`

命令 (No.6): SHOW DEFAULT BEARER ARP QCI

操作维护 ARP优先级 ARP抢占能力 ARP被抢占能力 QCI映射 
-----------------------------------------------------------
修改     1         不能抢占    被抢占        112-5&65535-100 
-----------------------------------------------------------
记录数 1

命令执行成功（耗时 0.036 秒）。
` 








父主题： [默认承载ARP和QCI控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增默认承载ARP和QCI控制配置(ADD BEARER ARP QCI) 
#### 新增默认承载ARP和QCI控制配置(ADD BEARER ARP QCI) 


命令功能 

该命令用于新增基于用户IMSI号段或APN NI或IMSI号段+APN NI的ARP和QCI控制配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置默认承载ARP和QCI控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数用于设置缺省分配保留优先级。
ARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP抢占能力。不能抢占：该承载不能抢占具有更低优先级承载的资源。抢占：该承载能抢占具有更低优先级承载的资源。
ARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP被抢占能力。不被抢占：该承载资源不能被具有更高优先级的承载抢占。被抢占：该承载资源能被具有更高优先级的承载抢占。
QCIMAP|QCI映射|参数可选性:任选参数；参数类型:复合参数|该参数用于设置缺省QoS分类标识映射。
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置缺省QoS分类标识，取值为[0,255]和65535。65535是该参数的通配值，未配置的QCI可以使用65535对应的映射QCI值。
MAPQCI|映射QCI|参数可选性:必选参数；参数类型:整数；参数范围为:5~255。|该参数用于设置缺省映射QoS分类标识。






命令举例 


新增默认承载ARP和QCI控制配置，IMSI号段索引为1，ARP优先级为1，QCI为100，映射QCI为5和QCI为255，映射QCI为255。 


ADD BEARER ARP QCI:IMSIIDX=1,ARPPRI=1,QCIMAP=100-5&255-255; 








父主题： [默认承载ARP和QCI控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改默认承载ARP和QCI控制配置(SET BEARER ARP QCI) 
#### 修改默认承载ARP和QCI控制配置(SET BEARER ARP QCI) 


命令功能 

该命令用于修改基于用户IMSI号段或APN NI或IMSI号段+APN NI的ARP和QCI控制配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置默认承载ARP和QCI控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数用于设置缺省分配保留优先级。
ARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP抢占能力。不能抢占：该承载不能抢占具有更低优先级承载的资源。抢占：该承载能抢占具有更低优先级承载的资源。
ARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP被抢占能力。不被抢占：该承载资源不能被具有更高优先级的承载抢占。被抢占：该承载资源能被具有更高优先级的承载抢占。
QCIMAP|QCI映射|参数可选性:任选参数；参数类型:复合参数|该参数用于设置缺省QoS分类标识映射。
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置缺省QoS分类标识，取值为[0,255]和65535。65535是该参数的通配值，未配置的QCI可以使用65535对应的映射QCI值。
MAPQCI|映射QCI|参数可选性:必选参数；参数类型:整数；参数范围为:5~255。|该参数用于设置缺省映射QoS分类标识。






命令举例 


修改默认承载ARP和QCI控制配置，IMSI号段索引为1，ARP抢占能力为抢占，ARP被抢占能力为被抢占。 


SET BEARER ARP QCI:IMSIIDX=1,ARPPEC="YES",ARPPEV="YES"; 








父主题： [默认承载ARP和QCI控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除默认承载ARP和QCI控制配置(DEL BEARER ARP QCI) 
#### 删除默认承载ARP和QCI控制配置(DEL BEARER ARP QCI) 


命令功能 

该命令用于删除基于用户IMSI号段或APN NI或IMSI号段+APN NI的ARP和QCI控制配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置默认承载ARP和QCI控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






命令举例 


删除默认承载ARP和QCI控制配置，IMSI号段索引为1。 


DEL BEARER ARP QCI:IMSIIDX=1; 








父主题： [默认承载ARP和QCI控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询默认承载ARP和QCI控制配置(SHOW BEARER ARP QCI) 
#### 查询默认承载ARP和QCI控制配置(SHOW BEARER ARP QCI) 


命令功能 

该命令用于查询基于用户IMSI号段或APN NI或IMSI号段+APN NI的ARP和QCI控制配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于配置默认承载ARP和QCI控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段索引|参数可选性:任选参数；参数类型:整数。|该参数用于配置默认承载ARP和QCI控制的用户IMSI号段索引，该索引可被分析器入口为“IMSI QoS控制分析”(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过IMSI号段进行QoS控制，则可不使用该参数。
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置APN NI即Network Identifier，格式为“Label1Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ARPPRI|ARP优先级|参数可选性:任选参数；参数类型:整数。|该参数用于设置缺省分配保留优先级。
ARPPEC|ARP抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP抢占能力。不能抢占：该承载不能抢占具有更低优先级承载的资源。抢占：该承载能抢占具有更低优先级承载的资源。
ARPPEV|ARP被抢占能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置默认承载的ARP被抢占能力。不被抢占：该承载资源不能被具有更高优先级的承载抢占。被抢占：该承载资源能被具有更高优先级的承载抢占。
QCIMAP|QCI映射|参数可选性:任选参数；参数类型:字符型。|该参数用于设置缺省QoS分类标识映射。






命令举例 


查询默认承载ARP和QCI控制配置。 


SHOW BEARER ARP QCI; 


`

命令 (No.6): SHOW BEARER ARP QCI

操作维护        IMSI号段索引  APN名称  ARP优先级  ARP抢占能力  ARP被抢占能力  QCI映射 
-------------------------------------------------------------------------------------------
复制 修改 删除  1                      1          抢占         被抢占         100-5&255-255 
-------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.036 秒）。
` 








父主题： [默认承载ARP和QCI控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 缺省UE AMBR配置 
### 缺省UE AMBR配置 


背景知识 


UE-AMBR，指UE的所有Non-GBR承载的集合对应的最大速率。MME计算UE-AMBR时，取该用户所有PDN连接的APN-AMBR之和与用户的签约UE-AMBR中的较小者。 




功能描述 


该功能用于设置缺省UE AMBR配置，当用户的签约UE-AMBR或者所有PDN连接的APN-AMBR之和为全零取值时，灵活设置MME下发给无线的非零取值的UE-AMBR。 




相关主题 



 

设置缺省UE AMBR配置(SET DEFAULT UE AMBR)
 

 

查询缺省UE AMBR配置(SHOW DEFAULT UE AMBR)
 

 








父主题： [MME QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置缺省UE AMBR配置(SET DEFAULT UE AMBR) 
#### 设置缺省UE AMBR配置(SET DEFAULT UE AMBR) 


命令功能 

该命令用于设置缺省UE AMBR配置。当用户签约UE-AMBR或者所有PDN连接的APN-AMBR之和为全零取值，运营商希望灵活设置MME下发给无线的非零取值的UE-AMBR时，使用该命令进行配置。


注意事项 

需要通过命令[SET SOFTWARE PARAMETER]打开软件参数“修正UE AMBR(786551)”开关，本配置才能够生效。


参数说明 


标识|名称|类型|说明
---|---|---|---
UEAMBRUL|上行UE累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:0~4000000000。|该参数用于设置缺省的上行UE累计最大比特率。
UEAMBRDL|下行UE累计最大比特率|参数可选性:任选参数；参数类型:整数；参数范围为:0~4000000000。|该参数用于设置缺省的下行UE累计最大比特率。
UNIT|比特率单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置比特率单位，包括：KBPS：单位为Kbps。MBPS：单位为Mbps。GBPS：单位为Gbps。






命令举例 


设置缺省UE AMBR配置，上行UE累计最大比特率为1Kbps，下行UE累计最大比特率为1Kbps，比特率单位为Kbps。 


SET DEFAULT UE AMBR:UEAMBRUL=1,UEAMBRDL=1,UNIT="KBPS"; 








父主题： [缺省UE AMBR配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询缺省UE AMBR配置(SHOW DEFAULT UE AMBR) 
#### 查询缺省UE AMBR配置(SHOW DEFAULT UE AMBR) 


命令功能 

该命令用于查询缺省UE AMBR配置。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
UEAMBRUL|上行UE累计最大比特率|参数可选性:任选参数；参数类型:整数。|该参数用于设置缺省的上行UE累计最大比特率。
UEAMBRDL|下行UE累计最大比特率|参数可选性:任选参数；参数类型:整数。|该参数用于设置缺省的下行UE累计最大比特率。
UNIT|比特率单位|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置比特率单位，包括：KBPS：单位为Kbps。MBPS：单位为Mbps。GBPS：单位为Gbps。






命令举例 


查询缺省UE AMBR配置。 


SHOW DEFAULT UE AMBR; 


`

命令 (No.9): SHOW DEFAULT UE AMBR

操作维护       上行UE累计最大比特率 下行UE累计最大比特率 比特率单位 
--------------------------------------------------------------------
修改           1                    1                    Kbps       
--------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.047 秒）。
` 








父主题： [缺省UE AMBR配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 公共QoS配置 
## 公共QoS配置 


背景知识 


QoS（Qualit of Service）也就是服务质量：是保证业务数据在网络中传输的质量和可靠性的度量。是在有限的网络环境(带宽)中为特定的业务数据流提供优质、可靠的服务。 



 

分类：将数据分为不同的类别，称为分类(classification)。
 

 

标记：将数据设置为不同的优先级称为标记(marking)。
 

 

管制：丢弃超出带宽，称为管制(Policing)。
 

 

整形：将超出的带宽缓存在内存中，等到下一秒再传递，称作整形(Shaping)。
 

 

拥塞管理：当网络发生拥塞后，数据需要被传递的，根据不同的QOS优先级保证高质量要求的数据有限被传递，QOS定义数据包传输的先后顺序。
 

 

拥塞避免：当网络发生拥塞后，超出的流量会采用流控方式，高优先级的数据优先保障通过，低优先级的数据被流控丢弃。
 

 


DSCP（Differentiated Services Code Point，差分服务代码点），IETF于1998年12月发布了Diff-Serv（Differentiated Service）的QoS分类标准。它在每个数据包IP头部的服务类别TOS（业务类型，Type of Service）标识字节中，利用已使用的6比特，通过编码值来区分优先级。DSCP 使用6个bit，取值范围为0~63。 


DSCP表示IP承载层的QoS，和承载网密切相关，各接口IP承载网的DSCP可以是独立规划。 


SGSN控制面和用户面各接口发送的IP报文的DSCP可以不同，方便用户根据DSCP实现不同的传输策略。各接口使用的DSCP值需要全网统一规划。 


PFC（Packet Flow Context，分组流上下文）是GPRS R99的一个特性，指SGSN通过为同一用户的具有相同或相近QoS的PDP分配相同的PFI（Packet Flow Identifier，分组流标识），实现具有相同或相近QoS的PDP共享相同的分组流上下文进行传输控制，仅用于2G接入。 


具体可参考协议3GPP TS 48.018。 


分配的PFI根据QoS映射，具体映射规则需全网规划。 




功能描述 


MME网元和SGSN网元都需要设置公共QoS配置，包括DSCP映射配置和PFI映射配置。 




相关主题 



 

DSCP映射配置
 

 

PFI映射配置
 

 








父主题： [QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### DSCP映射配置 
### DSCP映射配置 


背景知识 


DSCP（Differentiated Services Code Point，差分服务代码点），IETF于1998年12月发布了Diff-Serv（Differentiated Service）的QoS分类标准。它在每个数据包IP头部的服务类别TOS（业务类型，Type of Service）标识字节中，利用已使用的6比特，通过编码值来区分优先级。DSCP 使用6个bit，取值范围为0~63。 


DSCP表示IP承载层的QoS，和承载网密切相关，各接口IP承载网的DSCP可以是独立规划。 


SGSN控制面和用户面各接口发送的IP报文的DSCP可以不同，方便用户根据DSCP实现不同的传输策略。各接口使用的DSCP值需要全网统一规划。 




功能描述 


DSCP映射配置用于指定SGSN网元各接口的信令报文或用户数据报文的DSCP值。配置后，后续各个对应接口的信令报文或用户数据报文IP承载层的DSCP值就为此处配置的DSCP值。如果某个接口没有配置DSCP值，则DSCP值为0。 


“DSCP映射配置”仅用于SGSN网元，包括两部分内容： 



 


                        配置QoS与DSCP映射（命令为：
                        ADD QOS DSCP
                        ），可以配置Gn接口、Iu接口、Gb接口的用户数据报文的DSCP值。如果设置数据报文方向为上行链路，表示Gn接口的用户数据报文的DSCP值，如果设置数据报文方向为下行链路，表示Iu接口或Gb接口的用户数据报文的DSCP值。各个接口的用户数据报文的DSCP值还可以区分业务类别分别设置。
                    
 

 


                        配置信令DSCP（命令为：
                        SET SIG DSCP
                        ），可以配置Gb接口的NAS信令报文的DSCP值、Gb接口的承载信令报文的DSCP值、Gn接口的信令报文DSCP值和Ga接口、X1X2接口、X3接口的DSCP值。
                    
GB下行层三信令DSCP，应用于Gb接口投递的GMM、SM、SMS的NAS信令报文。GB下行承载信令DSCP，应用于Gb接口投递的LLC、BSSGP、IPNS的信令报文。
 

 




相关主题 



 

新增QoS与DSCP映射(ADD QOS DSCP)
 

 

删除QoS与DSCP映射(DEL QOS DSCP)
 

 

查询QoS与DSCP映射(SHOW QOS DSCP)
 

 

设置信令DSCP(SET SIG DSCP)
 

 

查询信令DSCP(SHOW SIG DSCP)
 

 








父主题： [公共QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增QOS与DSCP映射(ADD QOS DSCP) 
#### 新增QOS与DSCP映射(ADD QOS DSCP) 


命令功能 


此命令用于配置SGSN的Gn接口、Iu接口、Gb接口的用户面数据报文的DSCP值。 


SGSN的Gn接口、Iu接口、Gb接口的用户数据报文的DSCP值，可以通过此命令根据PDP的QoS映射得到，且各个PDP的DSCP值可以不一样。 


若当前流程做附着的GGSN与其他的DS区域（DiffServ Domain，区分服务域）联接时，需要根据事先的约定，对进入GGSN所属区域的报文IP头部的DSCP重新标记时，需要根据该命令的配置数据来执行。 


DiffServ（Differentiated Service，差分服务）是一种适用于骨干网络，可满足多种服务需求的IP QoS模型。骨干网承载服务主要由DiffServ功能实现，核心网承载服务主要由PS域QoS技术实现。 


在DiffServ模型中，将IP报文中的ToS（Type of Service，服务类型）字段重新定义，并称为DS（Differentiated Services，差分服务），用户通过标记分组数据报文的DS字段来申请不同层次的QoS服务。 


DS的前6位被称为DSCP（Differentiated Services Code Point，差分服务代码点），每一个DSCP编码值都被映射到一个已定义的PHB（Per-Hop Behaviors，每跳转发行为）标识码。网络节点根据IP报头中的DSCP，确定PHB。通过键入DSCP值，终端设备可对流量进行标识。 


DSCP总共分成了4类：CS (Class Selector，类选择器)、EF（Expedited Forwarding，加速转发）、AF（Assured Forwarding，确保转发类）和BE（Best Effort，尽力而为）。 


CS主要包括NC(Network Connection，网络连接)。 


NC、EF、AF、BE等都是RFC2474协议中定义的差异化服务类等级。NC是最高优先级服务，依次递减，BE为最低优先级服务类。 


NC（网络连接）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发类）的DSCP值最后一位为0，BE（尽力而为）的DSCP值为000000(0)。 


SGSN通过将IP报文中的DSCP字段与用户PDP上下文中的QoS进行映射可以使用户PDP上下文的QoS在IP网络传输中得到保证。 




注意事项 

该命令只适用于SGSN网元。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务。流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
DIRECTION|数据报文方向|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|上行链路是指MS到CN（Core Network，核心网）方向的链路；下行链路是指CN到MS方向的链路。取值含义：“UPLINK”：上行链路。“DOWNLINK”：下行链路。
QOSTYPE|QoS参数类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为需要映射的QoS的参数。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。本参数包括的选项为SGSN支持的需要映射的QoS的参数类型：“ARP”：缺省分配/保持优先级（Allocation/retention priority），该参数用于指示各UMTS承载在确定分配和保留时的相对重要性，该参数仅在Gn/Gp接口上传送，用于SGSN和GGSN之间的QoS协商，移动终端的QoS信元中不携带该参数。“MAXBITRATEUL”：最大上行链路比特率（Maximum bit rate for uplink）。“MAXBITRATEDL”：最大下行链路比特率（Maximum bit rate for downlink）。“GUARBITRATEUL”：保证上行链路比特率（Guaranteed bit rate for uplink）。“GUARBITRATEDL”：保证下行链路比特率（Guaranteed bit rate for downlink）。“TRANSDELAY”：传输时延（Transfer delay）。“SDUERRRATIO”：业务数据单元错误率（SDU error ratio）。“RESIDUALBER”：残余位错误率（Residual Bit Error Ratio）。选择“QoS参数类型”后，如果不设置该类型对应的各个“区间映射点”参数，则表示使用该QoS参数的全区间映射，表示将此QoS参数与DSCP的映射值划分为一个区间段，此种情况下，只需要设置一个DSCP值，区间的起止值分别为该QoS参数类型对应的各个“区间映射点”参数的最小值和最大值。选择“QoS参数类型”后，如果需要设置对应的各个“区间映射点”参数，可以设置一个或多个。输入的每个区间映射点代表一个区间段的终止值（最后一个区间段的终止值为该参数类型的最大值，不需要输入），如果设置了N个区间映射点，则表示将此QoS参数与DSCP的映射值划分为N+1个区间段，此种情况下，必须设置N+1个DSCP值。在设置了一个或多个“区间映射点”参数的情况下：第一区间段的起止值分别为：此“区间映射点”参数的最小值、选择的第一个“区间映射点“的值。第二区间段的起止值分别为：选择的第1个“区间映射点“紧接的下一个“区间映射点“的值、选择的第二个“区间映射点“的值。第N区间段的起止值分别为：选择的第N个“区间映射点“紧接的下一个“区间映射点“的值、此“区间映射点”参数的最大值。比如：选择“QoS参数类型”为“TRANSDELAY（传输时延）”，则分以下两种情况：如果没有设置“传输时延区间映射点”，则表示划分为一个区间段，此时只需要设置一个“DSCP值”，假设设置“DSCP值”为5，则区间起止值和DSCP值分别为：                  区  间           起始值            终止值           DSCP值               映射区间段1        10 ms(1)          3900 ms(62)       5（括号中，1和62表示“TRANSDELAY（传输时延）”对应的枚举值的编号。）表示10ms~4000ms均可以与数值为5的DSCP映射. 如果设置了4个“传输时延区间映射点”，分别为100ms、350ms、1200ms、3000ms，则表示划分为5个区间段，假设设置“DSCP值”分别为“15、25、35、45、55“，则映射区间被划分为5个区间段，区间段起止值和DSCP值分别为：                 区  间           起始值            终止值           DSCP值               映射区间段1        10 ms(1)          100 ms(10)        15               映射区间段2        110 ms(11)        350 ms(19)        25               映射区间段3        400 ms(20)        1200 ms(34)       35               映射区间段4        1300 ms(35)       3000 ms(52)       45               映射区间段5        3100 ms(53)       3900 ms(62)       55表示10ms~100ms映射到数值为15的PFI，110ms~350ms映射到数值为25的PFI，依次类推。
DSCP|DSCP值|参数可选性:必选参数；参数类型:整数；参数范围为:0~63。|该参数的含义为DSCP值，有关DSCP的内容请参见协议RFC2474。DSCP为6位二进制编码，本参数为十进制，取值范围为0~63之间的整数。DSCP总共分成了4类：CS (Class Selector，类选择器)、EF（Expedited Forwarding，加速转发）、AF（Assured Forwarding，确保转发类）和BE（Best Effort，尽力而为）。CS主要包括NC (Network Connection，网络连接)。NC、EF、AF、BE等都是RFC2474协议中定义的差异化服务类等级。NC是最高优先级服务，依次递减，BE为最低优先级服务类。NC（网络连接）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发类）的DSCP值最后一位为0，BE（尽力而为）的DSCP值为000000(0)。
ARP|ARP区间映射点|参数可选性:任意单选参数；参数类型:整数；参数范围为:1~2。|该参数的含义为ARP区间映射点。
MAXBITRATEUL|最大上行链路比特率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大上行链路比特率区间映射点。
MAXBITRATEDL|最大下行链路比特率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大下行链路比特率区间映射点。
GUARBITRATEUL|保证上行链路比特率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为保证上行链路比特率区间映射点。
GUARBITRATEDL|保证下行链路比特率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为保证下行链路比特率区间映射点。
TRANSDELAY|传输时延区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为传输时延区间映射点。
SDUERRRATIO|业务数据单元误码率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为SDU（Service Data Unit，业务数据单元）误码率区间映射点。
RESIDUALBER|残余误码率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为残余误码率区间映射点。






命令举例 


新增QOS与DSCP映射，设置业务类别为“Interactive”，数据报文方向为“UPLINK”，QoS参数类型为“ARP”，DSCP值为“1&2”，设置ARP区间映射点为“2”。 


ADD QOS DSCP: TRAFFCLASS=Interactive, DIRECTION=UPLINK, QOSTYPE=ARP,DSCP=1&2, ARP=2; 








父主题： [DSCP映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除QOS与DSCP映射(DEL QOS DSCP) 
#### 删除QOS与DSCP映射(DEL QOS DSCP) 


命令功能 

该命令用于根据QoS的业务类别和数据报文方向，删除QoS与DSCP映射。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务。流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
DIRECTION|数据报文方向|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|上行链路是指MS到CN（Core Network，核心网）方向的链路；下行链路是指CN到MS方向的链路。取值含义：“UPLINK”：上行链路。“DOWNLINK”：下行链路。






命令举例 


删除业务类别为“Interactive”，数据报文方向为“UPLINK” 


DEL QOS DSCP: TRAFFCLASS=Interactive, DIRECTION=UPLINK; 








父主题： [DSCP映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询QOS与DSCP映射(SHOW QOS DSCP) 
#### 查询QOS与DSCP映射(SHOW QOS DSCP) 


命令功能 

该命令用于根据QoS的业务类别或数据报文方向，查询QoS与DSCP映射。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务。流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
DIRECTION|数据报文方向|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|上行链路是指MS到CN（Core Network，核心网）方向的链路；下行链路是指CN到MS方向的链路。取值含义：“UPLINK”：上行链路。“DOWNLINK”：下行链路。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务。流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
DIRECTION|数据报文方向|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|上行链路是指MS到CN（Core Network，核心网）方向的链路；下行链路是指CN到MS方向的链路。取值含义：“UPLINK”：上行链路。“DOWNLINK”：下行链路。
QOSTYPE|QoS参数类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为需要映射的QoS的参数。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。本参数包括的选项为SGSN支持的需要映射的QoS的参数类型：“ARP”：缺省分配/保持优先级（Allocation/retention priority），该参数用于指示各UMTS承载在确定分配和保留时的相对重要性，该参数仅在Gn/Gp接口上传送，用于SGSN和GGSN之间的QoS协商，移动终端的QoS信元中不携带该参数。“MAXBITRATEUL”：最大上行链路比特率（Maximum bit rate for uplink）。“MAXBITRATEDL”：最大下行链路比特率（Maximum bit rate for downlink）。“GUARBITRATEUL”：保证上行链路比特率（Guaranteed bit rate for uplink）。“GUARBITRATEDL”：保证下行链路比特率（Guaranteed bit rate for downlink）。“TRANSDELAY”：传输时延（Transfer delay）。“SDUERRRATIO”：业务数据单元错误率（SDU error ratio）。“RESIDUALBER”：残余位错误率（Residual Bit Error Ratio）。选择“QoS参数类型”后，如果不设置该类型对应的各个“区间映射点”参数，则表示使用该QoS参数的全区间映射，表示将此QoS参数与DSCP的映射值划分为一个区间段，此种情况下，只需要设置一个DSCP值，区间的起止值分别为该QoS参数类型对应的各个“区间映射点”参数的最小值和最大值。选择“QoS参数类型”后，如果需要设置对应的各个“区间映射点”参数，可以设置一个或多个。输入的每个区间映射点代表一个区间段的终止值（最后一个区间段的终止值为该参数类型的最大值，不需要输入），如果设置了N个区间映射点，则表示将此QoS参数与DSCP的映射值划分为N+1个区间段，此种情况下，必须设置N+1个DSCP值。在设置了一个或多个“区间映射点”参数的情况下：第一区间段的起止值分别为：此“区间映射点”参数的最小值、选择的第一个“区间映射点“的值。第二区间段的起止值分别为：选择的第1个“区间映射点“紧接的下一个“区间映射点“的值、选择的第二个“区间映射点“的值。第N区间段的起止值分别为：选择的第N个“区间映射点“紧接的下一个“区间映射点“的值、此“区间映射点”参数的最大值。比如：选择“QoS参数类型”为“TRANSDELAY（传输时延）”，则分以下两种情况：如果没有设置“传输时延区间映射点”，则表示划分为一个区间段，此时只需要设置一个“DSCP值”，假设设置“DSCP值”为5，则区间起止值和DSCP值分别为：                  区  间           起始值            终止值           DSCP值               映射区间段1        10 ms(1)          3900 ms(62)       5（括号中，1和62表示“TRANSDELAY（传输时延）”对应的枚举值的编号。）表示10ms~4000ms均可以与数值为5的DSCP映射. 如果设置了4个“传输时延区间映射点”，分别为100ms、350ms、1200ms、3000ms，则表示划分为5个区间段，假设设置“DSCP值”分别为“15、25、35、45、55“，则映射区间被划分为5个区间段，区间段起止值和DSCP值分别为：                 区  间           起始值            终止值           DSCP值               映射区间段1        10 ms(1)          100 ms(10)        15               映射区间段2        110 ms(11)        350 ms(19)        25               映射区间段3        400 ms(20)        1200 ms(34)       35               映射区间段4        1300 ms(35)       3000 ms(52)       45               映射区间段5        3100 ms(53)       3900 ms(62)       55表示10ms~100ms映射到数值为15的PFI，110ms~350ms映射到数值为25的PFI，依次类推。
START|映射段段起始值|参数可选性:任选参数；参数类型:字符型；参数范围为:0~10个字符。|该参数的含义为映射段起始值。该参数在设置完“ADD QOS DSCP”命令后，由系统自动生成，无需设置”可通过“SHOW QOS DSCP ”命令进行查询
END|映射段段终止值|参数可选性:任选参数；参数类型:字符型；参数范围为:0~10个字符。|该参数的含义为映射段终止值。该参数在设置完“ADD QOS DSCP”命令后，由系统自动生成，无需设置”可通过“SHOW QOS DSCP ”命令进行查询
DSCP|DSCP值|参数可选性:任选参数；参数类型:整数。|该参数的含义为DSCP值，有关DSCP的内容请参见协议RFC2474。DSCP为6位二进制编码，本参数为十进制，取值范围为0~63之间的整数。DSCP总共分成了4类：CS (Class Selector，类选择器)、EF（Expedited Forwarding，加速转发）、AF（Assured Forwarding，确保转发类）和BE（Best Effort，尽力而为）。CS主要包括NC (Network Connection，网络连接)。NC、EF、AF、BE等都是RFC2474协议中定义的差异化服务类等级。NC是最高优先级服务，依次递减，BE为最低优先级服务类。NC（网络连接）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发类）的DSCP值最后一位为0，BE（尽力而为）的DSCP值为000000(0)。






命令举例 


查询所有的QOS与DSCP映射关系。 


SHOW QOS DSCP 


`

命令 (No.1): SHOW QOS DSCP

操作维护    业务类别   数据报文方向   QoS参数类型           映射段段起始值   映射段段终止值   DSCP值
----------------------------------------------------------------------------------------------------
复制 删除   流类型     上行链路       传输时延              10 ms            4000 ms          1
----------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [DSCP映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置信令DSCP(SET SIG DSCP) 
#### 设置信令DSCP(SET SIG DSCP) 


命令功能 


当全网规划某个接口的信令报文或用户数据报文使用某个指定DSCP数值时，通过该命令进行设置。后续各个对应接口的信令报文或用户数据报文IP承载层的DSCP值就为配置的DSCP值。 


使用此命令配置以下接口的DSCP值： 


GB下行层三信令DSCP，应用于Gb接口投递的GMM、SM、SMS的NAS信令报文。 


GB下行承载信令DSCP，应用于Gb接口投递的LLC、BSSGP、IPNS的信令报文。 


Gn接口的信令报文的DSCP值。 


Ga接口、X1/X2接口、X3接口的DSCP值。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
GBNASSIGDSCP|GB下行层三信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数的含义为Gb接口下行NAS（Non Access Stratum，非接入层）信令DSCP。
GBASSIGDSCP|GB下行承载信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数的含义为Gb下行承载信令DSCP。
GNGTPSIGDSCP|GTP信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数的含义为GTP信令DSCP。
GADSCP|Ga口信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数的含义为Ga口信令DSCP。
X1X2DSCP|X1X2口信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数的含义为X1X2口信令DSCP。
X3DSCP|X3口信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数的含义为X3口信令DSCP。
IWSS102DSCP|IWS S102口信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数的含义为IWS S102口信令DSCP。
S102DSCP|S102口信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数的含义为S102口信令DSCP。
DNSDSCP|DNS信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|本参数用于设置DNS接口DSCP标签值。
EMSDSCP|EMS+信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|本参数用于设置EMS+DSCP标签值






命令举例 


设置信令DSCP，设置GTP信令DSCP为“0”。 


SET SIG DSCP:GNGTPSIGDSCP=0; 








父主题： [DSCP映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询信令DSCP(SHOW SIG DSCP) 
#### 查询信令DSCP(SHOW SIG DSCP) 


命令功能 

该命令用于查询以下接口的DSCP值。
GB下行层三信令DSCP，应用于Gb接口投递的GMM、SM、SMS的NAS信令报文 


GB下行承载信令DSCP，应用于Gb接口投递的LLC、BSSGP、IPNS的信令报文 


Gn接口的信令报文的DSCP值 


Ga接口、X1/X2接口、X3接口的DSCP值 




注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
GBNASSIGDSCP|GB下行层三信令DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义为Gb接口下行NAS（Non Access Stratum，非接入层）信令DSCP。
GBASSIGDSCP|GB下行承载信令DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义为Gb下行承载信令DSCP。
GNGTPSIGDSCP|GTP信令DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义为GTP信令DSCP。
GADSCP|Ga口信令DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义为Ga口信令DSCP。
X1X2DSCP|X1X2口信令DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义为X1X2口信令DSCP。
X3DSCP|X3口信令DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义为X3口信令DSCP。
IWSS102DSCP|IWS S102口信令DSCP|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数的含义为IWS S102口信令DSCP。
S102DSCP|S102口信令DSCP|参数可选性:任选参数；参数类型:整数。|该参数的含义为S102口信令DSCP。
DNSDSCP|DNS信令DSCP|参数可选性:任选参数；参数类型:整数。|本参数用于设置DNS接口DSCP标签值。
EMSDSCP|EMS+信令DSCP|参数可选性:任选参数；参数类型:整数。|本参数用于设置EMS+DSCP标签值。






命令举例 


查询所有的信令DSCP。 


SHOW SIG DSCP 


`

命令 (No.1): SHOW SIG DSCP

操作维护       GB NAS-SIG DSCP GB AS-SIG DSCP GTP-SIG DSCP Ga SIG DSCP X1X2 SIG DSCP X3 SIG DSCP IWS S102 SIG DSCP S102 SIG DSCP DNS Signaling DSCP EMS+ Signaling DSCP 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           0               0              0            255         255           255         255               255           255                255                 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [DSCP映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### PFI映射配置 
### PFI映射配置 


背景知识 


PFC（Packet Flow Context，分组流上下文）是GPRS R99的一个特性，指SGSN通过为同一用户的具有相同或相近QoS的PDP分配相同的PFI（Packet Flow Identifier，分组流标识），实现具有相同或相近QoS的PDP共享相同的分组流上下文进行传输控制，仅用于2G接入。 


具体可参考协议3GPP TS 48.018。 


分配的PFI根据QoS映射，具体映射规则需全网规划。 




功能描述 


在如下场景下，需要使用PFI映射配置： 



 

2G/3G接入时，如果开启了PFC功能，在PDP激活、二次激活时，SGSN需要把PFI带给BSC和UE。
 

 

具有2G/3G/4G能力的UE，4G接入时，在Attach、PDN Connection Setup、Dedicated Bearer Setup流程中建立承载，MME需要把PFI传递给UE， UE移动到2G/3G网络后，能直接使用PFI。
 

 



                全网规划好了根据QoS映射PFI规则后，使用
                [ADD QOS PFI]
                配置。
            


说明： 


此处配置了PFI映射，则表示开启了PFC功能。 




相关主题 



 

新增QoS与PFI映射(ADD QOS PFI)
 

 

修改QoS与PFI映射(SET QOS PFI)
 

 

删除QoS与PFI映射(DEL QOS PFI)
 

 

查询QoS与PFI映射(SHOW QOS PFI)
 

 








父主题： [公共QoS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增QOS与PFI映射(ADD QOS PFI) 
#### 新增QOS与PFI映射(ADD QOS PFI) 


命令功能 


该命令用于新增MME和SGSN的QOS与PFI映射关系。 


MME在激活时如果UE有GERAN能力时，根据QOS读取该配置分配分组流标识PFI。PFI（Packet Flow Indentity）是指分组流标识--包含在QoS的上下文中。在用户和核心网交互中，用户激活后，核心网会根据PFI对同一用户中QOS需求相同的数据传输进行统一管理。一个用户不同类型的应用可以通过不同的会话来实现，即一个用户同时激活多个PDP上下文。这些PDP上下文，有可能具有相同的QOS需求，也有可能采用不同的QOS。 


PFC（Packet Flow Context，分组流上下文）是指SGSN通过为同一用户的具有相同或相近QoS的PDP分配相同的PFI（Packet Flow Identifier，分组流标识），实现数据流的捆绑传送，方便运营商对同一用户的不同QoS类别的PDP上下文区分处理。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
QOSTYPE|QoS参数类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为需要映射的QoS的参数。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。本参数包括的选项为SGSN支持的需要映射的QoS的参数类型：“MAXBITRATEUL”：最大上行链路比特率（Maximum bit rate for uplink）。“MAXBITRATEDL”：最大下行链路比特率（Maximum bit rate for downlink）。“GUARBITRATEUL”：保证上行链路比特率（Guaranteed bit rate for uplink）。“GUARBITRATEDL”：保证下行链路比特率（Guaranteed bit rate for downlink）。“TRANSDELAY”：传输时延（Transfer delay）。“SDUERRRATIO”：业务数据单元错误率（SDU error ratio）。“RESIDUALBER”：残余位错误率（Residual Bit Error Ratio）。选择“QoS参数类型”后，如果不设置该类型对应的各个“区间映射点”参数，则表示使用该QoS参数的全区间映射，表示将此QoS参数与PFI的映射值划分为一个区间段，此种情况下，只需要设置一个PFI值，区间的起止值分别为该QoS参数类型对应的各个“区间映射点”参数的最小值和最大值。选择“QoS参数类型”后，如果需要设置对应的各个“区间映射点”参数，可以设置一个或多个。输入的每个区间映射点代表一个区间段的终止值（最后一个区间段的终止值为该参数类型的最大值，不需要输入），如果设置了N个区间映射点，则表示将此QoS参数与PFI的映射值划分为N+1个区间段，此种情况下，必须设置N+1个PFI值。在设置了一个或多个“区间映射点”参数的情况下：第一区间段的起止值分别为：此“区间映射点”参数的最小值、选择的第一个“区间映射点“的值。第二区间段的起止值分别为：选择的第1个“区间映射点“紧接的下一个“区间映射点“的值、选择的第二个“区间映射点“的值。第N区间段的起止值分别为：选择的第N个“区间映射点“紧接的下一个“区间映射点“的值、此“区间映射点”参数的最大值。比如：选择“QoS参数类型”为“TRANSDELAY（传输时延）”，则分以下两种情况：如果没有设置“传输时延区间映射点”，则表示划分为一个区间段，此时只需要设置一个“PFI值”，假设设置“PFI值”为5，则区间起止值和PFI值分别为：                  区  间           起始值            终止值           PFI值               映射区间段1        10 ms(1)          3900 ms(62)       5表示10ms~4000ms均可以与数值为5的PFI映射. （括号中，1和62表示“TRANSDELAY（传输时延）”对应的枚举值的编号。）如果设置了4个“传输时延区间映射点”，分别为100ms、350ms、1200ms、3000ms，则表示划分为5个区间段，假设设置“PFI值”分别为“15、25、35、45、55“，则映射区间被划分为5个区间段，区间段起止值和PFI值分别为：                 区  间           起始值            终止值           PFI值               映射区间段1        10 ms(1)          100 ms(10)        15               映射区间段2        110 ms(11)        350 ms(19)        25               映射区间段3        400 ms(20)        1200 ms(34)       35               映射区间段4        1300 ms(35)       3000 ms(52)       45               映射区间段5        3100 ms(53)       3900 ms(62)       55表示10ms~100ms映射到数值为15的PFI，110ms~350ms映射到数值为25的PFI，依次类推。
PFI|PFI值|参数可选性:必选参数；参数类型:整数；参数范围为:8~127。|该参数的含义为PFI（Packet Flow Identifier，分组流标识）值。SGSN通过为同一用户的具有相同或相近QoS的PDP分配相同的PFI，实现数据流的捆绑传送，方便运营商对同一用户的不同QoS类别的PDP上下文区分处理。
MAXBITRATEUL|最大上行链路比特率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大上行链路比特率区间映射点。
MAXBITRATEDL|最大下行链路比特率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为最大下行链路比特率区间映射点。
GUARBITRATEUL|保证上行链路比特率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为保证上行链路比特率区间映射点。
GUARBITRATEDL|保证下行链路比特率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为保证下行链路比特率区间映射点。
TRANSDELAY|传输时延区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为传输时延区间映射点。
SDUERRRATIO|业务数据单元误码率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为业务数据单元误码率区间映射点。
RESIDUALBER|残余误码率区间映射点|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数的含义为残余误码率区间映射点。
TRAFHDLPRIO|流量控制优先级区间映射点|参数可选性:任意单选参数；参数类型:整数；参数范围为:1~2。|该参数的含义为流量控制优先级区间映射点。
PFTUNIT|分组流定时器的时间精度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NoExpire。|该参数表示分组流定时器的时长单位。取值含义：“2s”：表示分组流定时器的时长为2s的倍数。“1min”：表示分组流定时器的时长为1分钟的倍数。“6min”：表示分组流定时器的时长为6分钟的倍数。“500ms”：表示分组流定时器的时长是500ms的倍数。“Noexpire”：表示分组流定时器的时长没有限制。
PFTVALUE|分组流定时器时长|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。默认值:31。|该参数表示分组流定时器的时长取值。分组流定时器的时长由公式计算得出：分组流定时器的时长＝“本参数的取值”×“分组流定时器的时间精度”。






命令举例 


新增业务类别为"Conversational"、参数类型为"TRANSDELAY"、PFI与"TRANSDELAY"映射区间为PFI=12映射到10ms-90ms、PFI=14映射到90ms-150ms、PFI=55映射到150ms-950ms、PFI=56映射到950ms-2300ms、PFI=77映射到2300ms-3900ms的QOS与PFI映射： 


ADD QOS PFI:TRAFFCLASS="Conversational",QOSTYPE="TRANSDELAY",PFI=12&14&55&56&77,TRANSDELAY="90 ms"&"150 ms"&"950 ms"&"2300 ms"; 








父主题： [PFI映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改QOS与PFI映射(SET QOS PFI) 
#### 修改QOS与PFI映射(SET QOS PFI) 


命令功能 


该命令用于根据业务类别，修改QOS与PFI映射。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
PFTUNIT|分组流定时器的时间精度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示分组流定时器的时长单位。取值含义：“2s”：表示分组流定时器的时长为2s的倍数。“1min”：表示分组流定时器的时长为1分钟的倍数。“6min”：表示分组流定时器的时长为6分钟的倍数。“500ms”：表示分组流定时器的时长是500ms的倍数。“Noexpire”：表示分组流定时器的时长没有限制。
PFTVALUE|分组流定时器时长|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|该参数表示分组流定时器的时长取值。分组流定时器的时长由公式计算得出：分组流定时器的时长＝“本参数的取值”×“分组流定时器的时间精度”。






命令举例 


修改业务类别为Conversational的QOS与PFI映射，将分组流定时器的时间精度修改为6分钟，将分组流定时器时长修改为21秒： 


SET QOS PFI:TRAFFCLASS="Conversational",PFTUNIT="6min",PFTVALUE=21; 








父主题： [PFI映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除QOS与PFI映射(DEL QOS PFI) 
#### 删除QOS与PFI映射(DEL QOS PFI) 


命令功能 


该命令用于根据业务类别，删除QOS与PFI映射。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。






命令举例 


删除业务类别为Conversational的QOS与PFI映射： 


DEL QOS PFI:TRAFFCLASS="Conversational"; 








父主题： [PFI映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询QOS与PFI映射(SHOW QOS PFI) 
#### 查询QOS与PFI映射(SHOW QOS PFI) 


命令功能 


该命令用于根据业务类别，查询QOS与PFI映射。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
TRAFFCLASS|业务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为QoS的业务分类。取值含义：业务类型是QoS中用来标识用户业务的最主要参数，3GPP TS 23.107协议根据业务对时延的敏感程度将业务分成4类：会话类、流类、交互类和背景类。SGSN支持3GPP协议中定义的4类QoS级别的业务，可以为不同的用户提供不同优先级的业务。会话类主要应用于实时语音及视频业务流类主要用于承载实时数据流。交互类和背景类主要用于传统的Internet应用。相对于会话类和流类，它们对时延的敏感性低，背景类是对时延最不敏感的。两者的主要区别在于交互类主要用于交互式应用；而背景式主要用于后台流量。
QOSTYPE|QoS参数类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数的含义为需要映射的QoS的参数。QoS参数是一组为保证用户对业务质量的要求而定义的数据，包含在用户的PDP上下文中。本参数包括的选项为SGSN支持的需要映射的QoS的参数类型：“MAXBITRATEUL”：最大上行链路比特率（Maximum bit rate for uplink）。“MAXBITRATEDL”：最大下行链路比特率（Maximum bit rate for downlink）。“GUARBITRATEUL”：保证上行链路比特率（Guaranteed bit rate for uplink）。“GUARBITRATEDL”：保证下行链路比特率（Guaranteed bit rate for downlink）。“TRANSDELAY”：传输时延（Transfer delay）。“SDUERRRATIO”：业务数据单元错误率（SDU error ratio）。“RESIDUALBER”：残余位错误率（Residual Bit Error Ratio）。选择“QoS参数类型”后，如果不设置该类型对应的各个“区间映射点”参数，则表示使用该QoS参数的全区间映射，表示将此QoS参数与PFI的映射值划分为一个区间段，此种情况下，只需要设置一个PFI值，区间的起止值分别为该QoS参数类型对应的各个“区间映射点”参数的最小值和最大值。选择“QoS参数类型”后，如果需要设置对应的各个“区间映射点”参数，可以设置一个或多个。输入的每个区间映射点代表一个区间段的终止值（最后一个区间段的终止值为该参数类型的最大值，不需要输入），如果设置了N个区间映射点，则表示将此QoS参数与PFI的映射值划分为N+1个区间段，此种情况下，必须设置N+1个PFI值。在设置了一个或多个“区间映射点”参数的情况下：第一区间段的起止值分别为：此“区间映射点”参数的最小值、选择的第一个“区间映射点“的值。第二区间段的起止值分别为：选择的第1个“区间映射点“紧接的下一个“区间映射点“的值、选择的第二个“区间映射点“的值。第N区间段的起止值分别为：选择的第N个“区间映射点“紧接的下一个“区间映射点“的值、此“区间映射点”参数的最大值。比如：选择“QoS参数类型”为“TRANSDELAY（传输时延）”，则分以下两种情况：如果没有设置“传输时延区间映射点”，则表示划分为一个区间段，此时只需要设置一个“PFI值”，假设设置“PFI值”为5，则区间起止值和PFI值分别为：                  区  间           起始值            终止值           PFI值               映射区间段1        10 ms(1)          3900 ms(62)       5表示10ms~4000ms均可以与数值为5的PFI映射. （括号中，1和62表示“TRANSDELAY（传输时延）”对应的枚举值的编号。）如果设置了4个“传输时延区间映射点”，分别为100ms、350ms、1200ms、3000ms，则表示划分为5个区间段，假设设置“PFI值”分别为“15、25、35、45、55“，则映射区间被划分为5个区间段，区间段起止值和PFI值分别为：                 区  间           起始值            终止值           PFI值               映射区间段1        10 ms(1)          100 ms(10)        15               映射区间段2        110 ms(11)        350 ms(19)        25               映射区间段3        400 ms(20)        1200 ms(34)       35               映射区间段4        1300 ms(35)       3000 ms(52)       45               映射区间段5        3100 ms(53)       3900 ms(62)       55表示10ms~100ms映射到数值为15的PFI，110ms~350ms映射到数值为25的PFI，依次类推。
START|映射段段起始值|参数可选性:任选参数；参数类型:字符型；参数范围为:0~10个字符。|该参数的含义为映射段起始值。此参数为输出参数，在设置完ADD QOS PFI命令后，由系统自动生成，无需设置。可通过SHOW QOS PFI命令进行查询。
END|映射段段终止值|参数可选性:任选参数；参数类型:字符型；参数范围为:0~10个字符。|该参数的含义为映射段终止值。此参数为输出参数，在设置完ADD QOS PFI命令后，由系统自动生成，无需设置。可通过SHOW QOS PFI命令进行查询。
PFI|PFI值|参数可选性:任选参数；参数类型:整数。|该参数的含义为PFI（Packet Flow Identifier，分组流标识）值。SGSN通过为同一用户的具有相同或相近QoS的PDP分配相同的PFI，实现数据流的捆绑传送，方便运营商对同一用户的不同QoS类别的PDP上下文区分处理。
PFTUNIT|分组流定时器的时间精度|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示分组流定时器的时长单位。取值含义：“2s”：表示分组流定时器的时长为2s的倍数。“1min”：表示分组流定时器的时长为1分钟的倍数。“6min”：表示分组流定时器的时长为6分钟的倍数。“500ms”：表示分组流定时器的时长是500ms的倍数。“Noexpire”：表示分组流定时器的时长没有限制。
PFTVALUE|分组流定时器时长|参数可选性:任选参数；参数类型:整数。|该参数表示分组流定时器的时长取值。分组流定时器的时长由公式计算得出：分组流定时器的时长＝“本参数的取值”×“分组流定时器的时间精度”。






命令举例 


查询业务类别为Conversational的QOS与PFI映射： 


SHOW QOS PFI; 


`

命令 (No.1): SHOW QOS PFI

操作维护         业务类别   QoS参数类型          映射段段起始值   映射段段终止值   PFI值   分组流定时器的时间精度   分组流定时器时长
------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   流类型     传输时延             10 ms            4000 ms          8       NoExpire                 31
------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.044 秒）。
` 








父主题： [PFI映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SGSN对等PLMN配置 
# SGSN对等PLMN配置 


背景知识 


EPLMN即对等PLMN（Equivalent Public Land Mobile Network），运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，它们之间可以实现通信网络资源共享。 


配置EPLMN后，移动用户可以在运营商为他提供的不同PLMN之间驻留，允许移动用户选择其他通信网络的服务。 


移动用户可以有多个对等PLMN，但只有一个归属PLMN（HPLMN），移动用户通过IMSI号码提取归属PLMN。 


在多个网络同时为一个移动用户服务时，网络侧通过对等PLMN列表告诉RNC和UE：当前网络与归属PLMN 是等同的。业务流程如下： 



 

用户每次附着或路由更新时，当SGSN完成附着（Attach）或路由更新（RAU）流程时，就通过附着接受（Attach Accept）或路由更新接受（RAU Accept）消息把EPLMN列表信息下发给移动用户。
 

 

移动用户将网络侧下发的EPLMN列表加上当前网络的网络号保存在SIM卡中，下次附着或路由更新接受后刷新EPLMN列表。通过这个过程，移动用户实现通过查询保存的EPLMN列表来选择连接的网络资源。
 

 




功能描述 


如果不同运营商的网络资源之间或者同一运营商定义的不同PLMN之间需要实现通信网络资源共享。比如共有A、B两个PLMN网络。在B网络信号好的时候，原先登记在A网络的用户的手机可以根据保存在SIM卡上的EPLMN的信息自动重选B网络。此时，需要配置SGSN对等PLMN。 


注意事项： 


当SGSN需要为用户提供EPLMN列表时，应该根据软件参数“SGSN支持EPLMN组数”（ID：262151）和“SGSN对等PLMN配置”，决定是否向用户提供EPLMN列表，以及提供EPLMN的组数。（说明：软件参数取值为0，则不向用户提供EPLMN列表；取值为1，则最多向用户提供5组EPLMN列表；取值为2，则最多向用户提供15组EPLMN列表。） 


SGSN支持对整个网元配置默认的对等PLMN，也支持根据IMSI号段/路由区/位置区配置对等PLMN。配置项说明如下： 



 

根据IMSI号段/路由区/位置区配置对等PLMN。



                                配置对等PLMN Profile（
                                ADD SGSN PLMN PROFILE
                                ），该配置项把EPLMN列表组和PLMN Profile标识关联，方便被多种路由区/位置区和号码段的组合所引用。
                            



                                配置IMSI号段对等PLMN（
                                ADD SGSN IMSI RAI PLMN
                                ），该配置项对IMSI号段/路由区/位置区组合配置PLMN Profile标识。配置后，属于IMSI号段对等PLMN配置内的用户使用对等PLMN功能时，SGSN从此配置中获取EPLMN列表。
                            


 

 

配置默认对等PLMN

                        默认对等PLMN配置（
                        SET SGSN PLMN DEFAULT
                        }用于当不属于IMSI号段对等PLMN配置内的用户使用对等PLMN功能时，SGSN从此配置中获取EPLMN列表。
                    
 

 




相关主题 



 

默认对等PLMN配置
 

 

对等PLMN Profile配置
 

 

IMSI号段对等PLMN配置
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 默认对等PLMN配置 
## 默认对等PLMN配置 


背景知识 


EPLMN即对等PLMN（Equivalent Public Land Mobile Network），运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，它们之间可以实现通信网络资源共享。 


移动用户可以在运营商为他提供的不同EPLMN之间驻留，可以自己选择其他通信网络资源来提供服务。 


移动用户每次附着或路由更新时，SGSN通过附着接受或路由更新接受消息把EPLMN列表信息下发给移动用户。 




功能描述 



                当SGSN为移动用户提供EPLMN列表时，如果移动用户对应的IMSI号段已经在“IMSI号段对等PLMN配置（
                [ADD SGSN IMSI RAI PLMN]
                ）”中配置，则SGSN网元根据配置的列表下发EPLMN信息；如果移动用户IMSI号段不在已经配置的列表中，则SGSN根据“默认对等PLMN配置”获取EPLMN列表，下发给RNC和UE。
            


注意事项： 


SGSN根据软件参数“SGSN支持EPLMN组数”，决定向用户提供EPLMN的组数。 




相关主题 



 

设置默认对等PLMN(SET SGSN PLMN DEFAULT)
 

 

删除默认对等PLMN(DEL SGSN PLMN DEFAULT)
 

 

查询默认对等PLMN(SHOW SGSN PLMN DEFAULT)
 

 








父主题： [SGSN对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置默认对等PLMN(SET SGSN PLMN DEFAULT) 
### 设置默认对等PLMN(SET SGSN PLMN DEFAULT) 


命令功能 

该命令用于设置Gn/Gp SGSN网元的默认对等PLMN。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
PLMN|运营商|参数可选性:必选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。






命令举例 


设置默认对等PLMN，设置移动国家码为460，移动网号为001。
SET SGSN PLMN DEFAULT:PLMN="460"-"001"; 








父主题： [默认对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除默认对等PLMN(DEL SGSN PLMN DEFAULT) 
### 删除默认对等PLMN(DEL SGSN PLMN DEFAULT) 


命令功能 

该命令用于删除Gn/Gp SGSN网元的默认对等PLMN。


注意事项 

无。


命令举例 


删除所有的默认对等PLMN。
DEL SGSN PLMN DEFAULT 








父主题： [默认对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询默认对等PLMN(SHOW SGSN PLMN DEFAULT) 
### 查询默认对等PLMN(SHOW SGSN PLMN DEFAULT) 


命令功能 

该命令用于查询Gn/Gp SGSN网元的默认对等PLMN。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
PLMN|运营商|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。






命令举例 


查询所有的默认对等PLMN。
SHOW SGSN PLMN DEFAULT 


`

命令 (No.1): SHOW SGSN PLMN DEFAULT

操作维护  运营商
----------------
删除      460-001
----------------
记录数 1

命令执行成功（耗时 0.082 秒）。
` 








父主题： [默认对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 对等PLMN Profile配置 
## 对等PLMN Profile配置 


背景知识 


EPLMN即对等PLMN（Equivalent Public Land Mobile Network），运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，它们之间可以实现通信网络资源共享。 


ZXUN uMAC-SGSN产品支持配置全局默认的对等PLMN，也支持区分用户号段配置对等PLMN。 




功能描述 


区分用户号段/路由区/位置区配置对等PLMN时，由于用户号段＋路由区＋位置区的组合很多，为了提高配置效率，SGSN根据“对等PLMN Profile配置”把EPLMN列表组和PLMN Profile标识关联，用户号段＋路由区＋位置区的组合只需要引用相应的PLMN Profile标识。 


区分用户号码段对等PLMN功能的流程如下： 







                        配置对等PLMN Profile。配置命令为：
                        [ADD SGSN PLMN PROFILE]
                        。
                    







                        如果需要在PLMN Profile中增加运营商，使用命令：
                        [ADD SGSN PLMN]
                        。
                    







                        配置SGSN IMSI号段对等PLMN。参见
                        [ADD SGSN IMSI RAI PLMN]
                        。
                    






注意事项： 


SGSN根据软件参数“SGSN支持EPLMN组数”，决定向用户提供EPLMN的组数。 




相关主题 



 

增加PLMN(ADD SGSN PLMN)
 

 

删除PLMN(DEL SGSN PLMN)
 

 

新增对等PLMN Profile配置(ADD SGSN PLMN PROFILE)
 

 

修改对等PLMN Profile配置(SET SGSN PLMN PROFILE)
 

 

删除对等PLMN Profile配置(DEL SGSN PLMN PROFILE)
 

 

查询对等PLMN Profile配置(SHOW SGSN PLMN PROFILE)
 

 








父主题： [SGSN对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 增加PLMN(ADD SGSN PLMN) 
### 增加PLMN(ADD SGSN PLMN) 


命令功能 

该命令用于增加Gn/Gp SGSG网元的PLMN。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW SGSN IMSI RAI PLMN。
PLMN|运营商|参数可选性:必选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。






命令举例 


修改PLMN Profile标识为2的对等PLMN Profile配置，给它增加一个PLMN，该PLMN的移动国家码为460，移动网号为002。
ADD SGSN PLMN:PROFILEID=2,PLMN="460"-"002"; 








父主题： [对等PLMN Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除PLMN(DEL SGSN PLMN) 
### 删除PLMN(DEL SGSN PLMN) 


命令功能 

该命令用于删除Gn/Gp SGSG网元的PLMN。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW SGSN IMSI RAI PLMN。
PLMN|运营商|参数可选性:必选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。






命令举例 


修改PLMN Profile标识为2的对等PLMN Profile配置，将其中的移动国家码为460，移动网号为002的PLMN删除。
DEL SGSN PLMN:PROFILEID=2,PLMN="460"-"002"; 








父主题： [对等PLMN Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增对等PLMN Profile配置(ADD SGSN PLMN PROFILE) 
### 新增对等PLMN Profile配置(ADD SGSN PLMN PROFILE) 


命令功能 

该命令用于新增Gn/Gp SGSG网元的对等PLMN Profile配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW SGSN IMSI RAI PLMN。
PLMN|运营商|参数可选性:任选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


新增对等PLMN Profile配置，设置PLMN Profile标识为1，移动国家码为460，移动网号为003。
ADD SGSN PLMN PROFILE:PROFILEID=1,PLMN="460"-"003"; 








父主题： [对等PLMN Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改对等PLMN Profile配置(SET SGSN PLMN PROFILE) 
### 修改对等PLMN Profile配置(SET SGSN PLMN PROFILE) 


命令功能 

该命令用于修改Gn/Gp SGSG网元的对等PLMN Profile配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW SGSN IMSI RAI PLMN。
PLMN|运营商|参数可选性:任选参数；参数类型:复合参数|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|即MCC（Mobile Country Code）。MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位。例如，中国的“移动国家码”为“460”、美国的“移动国家码”为“310”等。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|即MNC（Mobile Network Code）。移动网号由2位或3位数字组成，它由本国电信主管部门在本国范围内统一分配。例如，“01”是中国联通的移动网号，“02”是中国移动的移动网号，“03”是中国电信的移动网号等。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


将PLMN Profile标识为1的对等PLMN Profile配置中的PLMN修改为“460-001”，其中的460是移动国家码，001是移动网号。
SET SGSN PLMN PROFILE:PROFILEID=1,PLMN="460"-"001"; 








父主题： [对等PLMN Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除对等PLMN Profile配置(DEL SGSN PLMN PROFILE) 
### 删除对等PLMN Profile配置(DEL SGSN PLMN PROFILE) 


命令功能 

该命令用于删除Gn/Gp SGSG网元的对等PLMN Profile配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW SGSN IMSI RAI PLMN。






命令举例 


删除PLMN Profile标识为1的所有PLMN。
DEL SGSN PLMN PROFILE:PROFILEID=1; 








父主题： [对等PLMN Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询对等PLMN Profile配置(SHOW SGSN PLMN PROFILE) 
### 查询对等PLMN Profile配置(SHOW SGSN PLMN PROFILE) 


命令功能 

该命令用于查询Gn/Gp SGSG网元的对等PLMN Profile配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW SGSN IMSI RAI PLMN。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|PLMN Profile标识|参数可选性:任选参数；参数类型:整数。|对等PLMN Profile的编号。这个标识供“IMSI号段对等PLMN配置”使用，“查询IMSI号段对等PLMN配置”的命令为：SHOW SGSN IMSI RAI PLMN。
PLMN|运营商|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


查询所有的对等PLMN Profile配置。
SHOW SGSN PLMN PROFILE; 


`

命令 (No.1): SHOW SGSN PLMN PROFILE;

操作维护         PLMN Profile标识   运营商    用户别名
------------------------------------------------------
复制 修改 删除   1                  460-003   
------------------------------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [对等PLMN Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## IMSI号段对等PLMN配置 
## IMSI号段对等PLMN配置 


背景知识 


EPLMN即对等PLMN（Equivalent Public Land Mobile Network），运营商可以在网络侧配置不同PLMN间的对等关系，这些PLMN处于一个平等的网络中，它们之间可以实现通信网络资源共享。 


ZXUN uMAC-SGSN产品支持配置全局默认的对等PLMN，也支持区分用户号段配置对等PLMN。 




功能描述 


当SGSN需要为用户提供EPLMN列表时，属于IMSI号段对等PLMN配置内的用户使用对等PLMN功能时，SGSN根据“IMSI号段对等PLMN配置”获取EPLMN列表。 


区分用户号码段对等PLMN功能的流程如下： 







                        配置对等PLMN Profile。参见
                        [ADD SGSN PLMN PROFILE]
                        。
                    







                        如果需要在PLMN Profile中增加运营商，使用命令：
                        [ADD SGSN PLMN]
                        。
                    







                        配置SGSN IMSI号段对等PLMN。配置命令为：
                        [ADD SGSN IMSI RAI PLMN]
                        。
                    






注意事项： 


SGSN根据软件参数“SGSN支持EPLMN组数”，决定向用户提供EPLMN的组数。 




相关主题 



 

新增SGSN IMSI对等PLMN配置(ADD SGSN IMSI RAI PLMN)
 

 

修改SGSN IMSI对等PLMN配置(SET SGSN IMSI RAI PLMN)
 

 

删除SGSN IMSI对等PLMN配置(DEL SGSN IMSI RAI PLMN)
 

 

查询SGSN IMSI对等PLMN配置(SHOW SGSN IMSI RAI PLMN)
 

 








父主题： [SGSN对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增SGSN IMSI对等PLMN配置(ADD SGSN IMSI RAI PLMN) 
### 新增SGSN IMSI对等PLMN配置(ADD SGSN IMSI RAI PLMN) 


命令功能 

该命令用于新增SGSN IMSI对等PLMN配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|表示该配置适用的IMSI号段。
ISALLRA|是否适用于所有路由区|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示该项配置是不是对所有的路由区都适用。是（YES）：该项配置适用于所有的位置区和路由区。否（NO）：该项配置不能适用于所有的位置区和路由区。适用的位置区名称或路由区名称需要输入，但是只能输入其中之一，两者不能同时输入。
LANAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此处的位置区名是SGSN已经配置的位置区名称。查询SGSN已经配置的位置区名的命令为：SHOW LAI。位置区用于表示用户所在的位置区信息，格式为MCC+MNC+LAC，更多的详细信息请参考24008–860协议10.5.1.3章节。
RANAME|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示该项配置适用于哪个路由区。此处的路由区名是SGSN已经配置的路由区名。查询SGSN已经配置的路由区名的命令为：SHOW RAI。路由区用于表示用户所在的路由区信息，格式为MCC+MNC+LAC+LAC cont'd+RAC，更多的详细信息请参考24008–860协议10.5.5.15章节。
PROFILEID|PLMN Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该项配置使用的对等PLMN Profile标识，该标识对应一组对等的PLMN。查询SGSN配置的对等PLMN Profile标识的命令为：SHOW SGSN PLMN PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


新增SGSN IMSI号段对等PLMN配置，设置IMSI号段为46001，适用于所有路由区，PLMN Profile标识为1。
ADD SGSN IMSI RAI PLMN:IMSI="46001",ISALLRA="YES",PROFILEID=1; 








父主题： [IMSI号段对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改SGSN IMSI对等PLMN配置(SET SGSN IMSI RAI PLMN) 
### 修改SGSN IMSI对等PLMN配置(SET SGSN IMSI RAI PLMN) 


命令功能 

该命令用于修改SGSN IMSI对等PLMN配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|表示该配置适用的IMSI号段。
ISALLRA|是否适用于所有路由区|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示该项配置是不是对所有的路由区都适用。是（YES）：该项配置适用于所有的位置区和路由区。否（NO）：该项配置不能适用于所有的位置区和路由区。适用的位置区名称或路由区名称需要输入，但是只能输入其中之一，两者不能同时输入。
LANAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此处的位置区名是SGSN已经配置的位置区名称。查询SGSN已经配置的位置区名的命令为：SHOW LAI。位置区用于表示用户所在的位置区信息，格式为MCC+MNC+LAC，更多的详细信息请参考24008–860协议10.5.1.3章节。
RANAME|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示该项配置适用于哪个路由区。此处的路由区名是SGSN已经配置的路由区名。查询SGSN已经配置的路由区名的命令为：SHOW RAI。路由区用于表示用户所在的路由区信息，格式为MCC+MNC+LAC+LAC cont'd+RAC，更多的详细信息请参考24008–860协议10.5.5.15章节。
PROFILEID|PLMN Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|该项配置使用的对等PLMN Profile标识，该标识对应一组对等的PLMN。查询SGSN配置的对等PLMN Profile标识的命令为：SHOW SGSN PLMN PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


修改IMSI号段为46001，适用于所有路由区的SGSN IMSI号段对等PLMN配置，将PLMN Profile标识修改为2。
SET SGSN IMSI RAI PLMN:IMSI="46001",ISALLRA="YES",PROFILEID=2; 








父主题： [IMSI号段对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除SGSN IMSI对等PLMN配置(DEL SGSN IMSI RAI PLMN) 
### 删除SGSN IMSI对等PLMN配置(DEL SGSN IMSI RAI PLMN) 


命令功能 

该命令用于删除SGSN IMSI对等PLMN配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|表示该配置适用的IMSI号段。
ISALLRA|是否适用于所有路由区|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示该项配置是不是对所有的路由区都适用。是（YES）：该项配置适用于所有的位置区和路由区。否（NO）：该项配置不能适用于所有的位置区和路由区。适用的位置区名称或路由区名称需要输入，但是只能输入其中之一，两者不能同时输入。
LANAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此处的位置区名是SGSN已经配置的位置区名称。查询SGSN已经配置的位置区名的命令为：SHOW LAI。位置区用于表示用户所在的位置区信息，格式为MCC+MNC+LAC，更多的详细信息请参考24008–860协议10.5.1.3章节。
RANAME|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示该项配置适用于哪个路由区。此处的路由区名是SGSN已经配置的路由区名。查询SGSN已经配置的路由区名的命令为：SHOW RAI。路由区用于表示用户所在的路由区信息，格式为MCC+MNC+LAC+LAC cont'd+RAC，更多的详细信息请参考24008–860协议10.5.5.15章节。






命令举例 


删除IMSI号段为46001，适用于所有路由区的SGSN IMSI号段对等PLMN配置。
DEL SGSN IMSI RAI PLMN:IMSI="46001",ISALLRA="YES"; 








父主题： [IMSI号段对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGSN IMSI对等PLMN配置(SHOW SGSN IMSI RAI PLMN) 
### 查询SGSN IMSI对等PLMN配置(SHOW SGSN IMSI RAI PLMN) 


命令功能 

该命令用于查询SGSN IMSI对等PLMN配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|表示该配置适用的IMSI号段。
LANAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此处的位置区名是SGSN已经配置的位置区名称。查询SGSN已经配置的位置区名的命令为：SHOW LAI。位置区用于表示用户所在的位置区信息，格式为MCC+MNC+LAC，更多的详细信息请参考24008–860协议10.5.1.3章节。
RANAME|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示该项配置适用于哪个路由区。此处的路由区名是SGSN已经配置的路由区名。查询SGSN已经配置的路由区名的命令为：SHOW RAI。路由区用于表示用户所在的路由区信息，格式为MCC+MNC+LAC+LAC cont'd+RAC，更多的详细信息请参考24008–860协议10.5.5.15章节。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|表示该配置适用的IMSI号段。
ISALLRA|是否适用于所有路由区|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示该项配置是不是对所有的路由区都适用。是（YES）：该项配置适用于所有的位置区和路由区。否（NO）：该项配置不能适用于所有的位置区和路由区。适用的位置区名称或路由区名称需要输入，但是只能输入其中之一，两者不能同时输入。
LANAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此处的位置区名是SGSN已经配置的位置区名称。查询SGSN已经配置的位置区名的命令为：SHOW LAI。位置区用于表示用户所在的位置区信息，格式为MCC+MNC+LAC，更多的详细信息请参考24008–860协议10.5.1.3章节。
RANAME|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示该项配置适用于哪个路由区。此处的路由区名是SGSN已经配置的路由区名。查询SGSN已经配置的路由区名的命令为：SHOW RAI。路由区用于表示用户所在的路由区信息，格式为MCC+MNC+LAC+LAC cont'd+RAC，更多的详细信息请参考24008–860协议10.5.5.15章节。
PROFILEID|PLMN Profile标识|参数可选性:任选参数；参数类型:整数。|该项配置使用的对等PLMN Profile标识，该标识对应一组对等的PLMN。查询SGSN配置的对等PLMN Profile标识的命令为：SHOW SGSN PLMN PROFILE。
PLMN|运营商PLMN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|即为PLMN（Public Land Mobile Network，公共陆地移动网络），由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






命令举例 


查询SGSN配置的所有的IMSI对等PLMN配置。
SHOW SGSN IMSI RAI PLMN; 


`

命令 (No.1): SHOW SGSN IMSI RAI PLMN;

操作维护         IMSI号段   是否适用于所有路由区   位置区名   路由区名   PLMN Profile标识   运营商PLMN   用户别名
-----------------------------------------------------------------------------------------------------------------
复制 修改 删除   46001      是                                           1                  460-003      
-----------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.074 秒）。
` 








父主题： [IMSI号段对等PLMN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# Diameter配置 
# Diameter配置 


背景知识 


MME与HSS、EIR和GMLC设备接口上之间采用Diameter基本协议。 


Diameter协议是IETF的AAA工作组确定的下一代AAA协议标准。Diameter协议包括基本协议（Diameter Base Protocol，RFC3588），NAS（网络接入服务）协议，EAP（可扩展鉴别）协议，MIP（移动IP）协议，CMS（密码消息语法）协议等。
Diameter基本协议为各种认证、授权和计费业务提供了安全、可靠、易于扩展的框架。其主要涉及性能协商、消息如何被发送、对等双方最终如何结束通信等方面，基本协议一般不单独使用，往往被扩展成新的应用来使用，所有应用和服务的基本功能都是在基础协议中实现，应用特定功能则是由扩展协议在基础协议的基础上扩展后实现的。 


Diameter基本协议中，消息体以AVP形式出现，一条消息相关的各种信息以一个个AVP（Attribute Value Pair）的形式封装起来。每个AVP都具有M、V、P标志和制造商ID，同时支持厂商自定义的AVP和命令。 



 

“M”比特，称为强制比特，指明对该AVP的支持是否是必需的。
 

 

“V”比特，称作制造商定义（Vendor-Specific）比特，指明在AVP头中是否出现可选的制造商ID字段。
 

 

“P”比特指明为保证端到端安全是否需要加密。
 

 


Diameter网络节点运行在TCP或者SCTP上，能够提供可靠传输和具有重传机制，由传输层来提供可靠性；同时能快速的检测出不可到达对等端的能力，并有很好的故障切换机制，当面MME只支持Diameter承载在SCTP协议。 




功能描述 


MME的Diameter配置，包括：Diameter协议栈基础配置、Diameter AVP Profile配置、Diameter连接路由配置、GMLC连接路由配置。 



 

Diameter协议栈基础配置：配置MME作为Diameter对等端时，MME的Prouduct Name、Firmware Version ID、TC时长、Diameter消息重传次数、等待DWA消息时长、Diameter链路恢复前DWR发送测试次数等信息。
 

 

Diameter AVP Profile配置：配置某个Diameter消息中的某个AVP是否携带，如携带时其中M、V、P标志和制造商ID的取值。
 

 

Diameter连接路由配置：配置到HSS网元的局向路由，到HSS或GMLC网元的Diameter路由组、路由和链路，路由组包含多个路由，路由包含多个链路，其中都可选择负荷分担与N+M主备模式。
 

 

GMLC连接路由配置：配置到GMLC网元的局向路由、局向路由关联“Diameter连接路由配置”中的Diameter路由组ID。
 

 


MME中配置对端HSS网元，需要配置HSS局向，Diameter局向路由，Diameter路由组、路由和链路。 


MME中配置对端EIR网元，需要配置EIR局向，Diameter局向路由，Diameter路由组、路由和链路。 


MME中配置对端GMLC网元，需要配置GMLC局向，GMLC局向路由，Diameter路由组、路由和链路。 




相关主题 



 

Diameter协议栈基本配置
 

 

Diameter AVP Profile配置
 

 

Diameter连接路由配置
 

 

Diameter GMLC配置
 

 

Diameter SMC配置
 

 

Support Feature管理
 

 

Diameter SCEF配置
 

 

Diameter消息控制配置
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Diameter协议栈基本配置 
## Diameter协议栈基本配置 


背景知识 


MME与HSS、EIR和GMLC网元使用Diameter协议连接，Diameter连接未建立时，MME定时发起Capabilities-Exchange-Request消息建立Diameter连接，消息中包括产品名称、固件版本号和MME支持的Diameter应用能力，对端网元收到消息后，判断本网元的Diameter应用能力是否和请求消息中一致，如一致则返回建立成功的响应消息。Diameter连接建立成功后，MME在链路上发送测试消息用于监测链路状态。 




功能描述 


“Diameter协议栈基本配置”用于设置MME网元Diameter链路的基本信息，包括“产品名称”，“固件版本号”，“Diameter链路建立尝试时间间隔”“Diameter消息重发时间间隔”等控制参数。 


“Diameter协议栈基本配置”MME网元已经设置了默认配置，一般情况不需要修改。 




相关主题 



 

设置Diameter协议栈基本配置(SET DIAMCFG)
 

 

查询Diameter协议栈基本配置(SHOW DIAMCFG)
 

 








父主题： [Diameter配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置Diameter协议栈基本配置(SET DIAMCFG) 
### 设置Diameter协议栈基本配置(SET DIAMCFG) 


命令功能 

该命令用于设置MME中Diameter协议栈的基本控制参数。当需要修改“产品名称”、“固件版本号”、“Diameter消息重发次数”等控制参数时，使用该命令，控制参数设置成功后，将会改变“产品名称”、“固件修订”、“Diameter消息重发次数”等信息。


注意事项 

建议使用默认值，一般情况下不修改。


参数说明 


标识|名称|类型|说明
---|---|---|---
PRODUCTNAME|产品名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|产品名称
FWVER|固件版本号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|固件版本号
AVPVALIDCHECK|是否做AVP有效性检查|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否对AVP的有效性进行检查
TP|连接恢复定时器(毫秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~1000。|该参数要“TPRETRYTIME”值不为0才有意义。表示控制连续多次心跳消息交互的定时器时长。
TPRETRYTIME|连接恢复尝试次数门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~5。|当一条Diameter连接的传输层由断到通后，需要经过连续多次成功的心跳消息交互才认为是Diameter连接状态正常，该参数用于控制具体的交互次数。
TB|流量控制定时器（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~60。|对外发送Diameter消息后，若对端返回DIAMETER_TOO_BUSY，则根据该参数的配置设定该路由忙的时间，后续发现该路由忙就选择其它正常路由，以此来达到流量控制的目的。
TN|不可达超时重传定时器（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~60。|对外发送Diameter消息后，若对端返回DIAMETER_UNABLE_TO_DELIVER（或DIAMETER_LOOP_DETECTED）错误码，则根据该参数的配置选择重选链路发送还是在该链路上重传。配置为0，则重新选择其它状态正常的链路进行发送消息。配置为非0，则在等待配置的时间后在原链路上重新发送消息。参数取值范围为[0,60]，单位为秒。
HOSTCASE|Hostname和realm是否区分大小写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Hostname和realm是否区分大小写






命令举例 


设置Diameter协议栈基本配置，产品名称为“uMAC(OMM)”，固件版本号为41020，需要对AVP的有效性进行检查。 


SET DIAMCFG:PRODUCTNAME="uMAC(OMM)",FWVER=41020,AVPVALIDCHECK="YES"; 








父主题： [Diameter协议栈基本配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询Diameter协议栈基本配置(SHOW DIAMCFG) 
### 查询Diameter协议栈基本配置(SHOW DIAMCFG) 


命令功能 

该命令用于查询MME中Diameter协议栈的基本控制参数，如“产品名称”、“固件版本号”、“Diameter消息重发次数”等。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
PRODUCTNAME|产品名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|产品名称
FWVER|固件版本号|参数可选性:任选参数；参数类型:整数。|固件版本号
AVPVALIDCHECK|是否做AVP有效性检查|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否对AVP的有效性进行检查
TP|连接恢复定时器(毫秒)|参数可选性:任选参数；参数类型:整数。|该参数要“TPRETRYTIME”值不为0才有意义。表示控制连续多次心跳消息交互的定时器时长。
TPRETRYTIME|连接恢复尝试次数门限|参数可选性:任选参数；参数类型:整数。|当一条Diameter连接的传输层由断到通后，需要经过连续多次成功的心跳消息交互才认为是Diameter连接状态正常，该参数用于控制具体的交互次数。
TB|流量控制定时器（秒）|参数可选性:任选参数；参数类型:整数。|对外发送Diameter消息后，若对端返回DIAMETER_TOO_BUSY，则根据该参数的配置设定该路由忙的时间，后续发现该路由忙就选择其它正常路由，以此来达到流量控制的目的。
TN|不可达超时重传定时器（秒）|参数可选性:任选参数；参数类型:整数。|对外发送Diameter消息后，若对端返回DIAMETER_UNABLE_TO_DELIVER（或DIAMETER_LOOP_DETECTED）错误码，则根据该参数的配置选择重选链路发送还是在该链路上重传。配置为0，则重新选择其它状态正常的链路进行发送消息。配置为非0，则在等待配置的时间后在原链路上重新发送消息。参数取值范围为[0,60]，单位为秒。
HOSTCASE|Hostname和realm是否区分大小写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Hostname和realm是否区分大小写






命令举例 


查询Diameter协议栈基本配置。 


SHOW DIAMCFG; 


`
 
命令 (No.1): SHOW DIAMCFG

操作维护  产品名称   固件版本号   是否做AVP有效性检查   连接恢复定时器(毫秒)   连接恢复尝试次数门限   流量控制定时器（秒）   不可达超时重传定时器（秒）   Hostname和realm是否区分大小写
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      ZTE-uMAC   41510        否                    100                    0                      0                      0                            不区分
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.054 秒）。
` 








父主题： [Diameter协议栈基本配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Diameter AVP Profile配置 
## Diameter AVP Profile配置 


背景知识 


Diameter协议由一个头以及跟随的一个或多个属性值对（AVP）组成。一个AVP包含一个头和用来封装特定协议的数据（例如，路由信息），以及认证、授权或计费信息，AVP头包括M、V、P标志和制造商ID。 



 

“M”比特，称为强制比特，指明对该AVP的支持是否是必需的。
 

 

“V”比特，称作制造商定义（Vendor-Specific）比特，指明在AVP头中是否出现可选的制造商ID字段。
 

 

“P”比特指明为保证端到端安全是否需要加密。
 

 




功能描述 


通过Diameter AVP Profile配置，可以编辑MME发送的Diameter消息，控制消息中的各个AVP字段是否携带，以及如携带时其中M、V、P标志和制造商ID的取值。 


MME到某个HSS、EIR或GMLC局向的Diameter的消息需要编辑时，在“Diameter 局向配置”、“Diameter EIR配置”和“Diameter GMLC局向配置”中为HSS、EIR或GMLC局向配置关联的AVP Profile ID，使用此ID可关联到本配置中的某个编辑策略。如果MME和其它网元对接时，不需要对Diameter消息进行编辑，配置AVP Profile ID默认值为0，则表示不采用Diameter编辑策略。 




相关主题 



 

新增Diameter AVP Profile配置(ADD DIM AVP PROFILE)
 

 

修改Diameter AVP Profile配置(SET DIM AVP PROFILE)
 

 

删除Diameter AVP Profile配置(DEL DIM AVP PROFILE)
 

 

查询Diameter AVP Profile配置(SHOW DIM AVP PROFILE)
 

 

设置默认Diameter AVP Profile配置(SET DEFAULT DIM AVP PROFILE)
 

 

清除默认Diameter AVP Profile配置(CLEAR DEFAULT DIM AVP PROFILE)
 

 

查询默认Diameter AVP Profile配置(SHOW DEFAULT DIM AVP PROFILE)
 

 








父主题： [Diameter配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增Diameter AVP Profile配置(ADD DIM AVP PROFILE) 
### 新增Diameter AVP Profile配置(ADD DIM AVP PROFILE) 


命令功能 

本命令用于增加Diameter AVP Profile配置。当需要控制某条Diameter消息中某AVP中“M,V,P”标记位或者控制该AVP是否携带时，使用该命令。Diameter AVP Profile配置成功后，可以实现Diameter基础协议消息，S6a和SLg口出向业务消息的AVP控制。


注意事项 



 
该命令需要加载支持该特性的安全变量，对应的安全变量项为“软件参数65560（是否支持Diameter AVP 控制功能）”。
 

 
配置的Profile需要被关联才能生效，其中Diameter基础协议消息在SET DIAMROUTE中被关联；DiameterS6a口业务消息需要在SET DIAMADJ中被关联；DiameterSLg口业务消息需要在SET DIAMGMLCADJ中被关联。
 

 
该AVP控制只对出向消息有效，而对入向消息无效。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|该参数用于指定一个Diameter AVP控制Profile标识号，需全局唯一。
AVPCODE1|AVP Code|参数可选性:必须单选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要被控制AVP的AVP 码，仅包含一些比较常用的需要被控制的AVP，各个AVP含义可以参见协议3GPP TS 29.272的7.3.1节。
AVPCODE2|AVP Code|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~65535。|该参数用于指定需要被控制AVP的AVP 码，手动输入，用于AVPCODE1中未包含的AVP，各个AVP含义可以参见协议3GPP TS 29.272。
MINDICATOR|M指示|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|M指示，强制比特，具体含义可以参见RFC3588的4.1节。
VINDICATOR|V指示|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|V指示，是否携带制造商标记，具体含义可以参见RFC3588的4.1节。
PINDICATOR|P指示|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|P指示，指明为保证端到端安全需要加密，具体含义可以参见RFC3588的4.1节。
VENDERID|Vender ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:10415。|Vender 标识，制造商标识，每一个设备厂家均被有自己的制造商标识。
COMMANDNAME|Command Name|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|命令码名称，该参数用于区分具体的消息，取值含义：Capabilities Exchange Request（CER）:能力协商请求Capabilities Exchange Answer（CEA）:能力协商响应Device Watchdog Request（DWR）:设备检测请求Device Watchdog Answer（DWA）:设备检测响应Disconnect Peer Request（DPR）:对端断开连接请求Disconnect Peer Answer（DPA）:对端断开连接响应Update Location Request（ULR）:位置更新请求Update Location Answer（ULA）:位置更新响应Cancel Location Request（CLR）:取消位置请求Cancel Location Answer（ULA）:取消位置响应Authentication Information Request（AIR）:鉴权信息请求Authentication Information Answer（AIA）:鉴权信息响应Insert Subscriber Data Request（IDR）:插入签约数据请求Insert Subscriber Answer（IDA）:插入签约数据响应Delete Subscriber Data Request（DSR）:删除签约数据请求Delete Subscriber Data  Answer（DSA）:删除签约数据响应Purge UE Request（PUR）:清除用户请求Purge UE Answer（PUA）清除用户响应Reset Request（RSR）:重启请求Reset Answer（RSA）重启响应Notify Request（NOR）:通知请求Notify Answer（NOA）通知响应Provide Location Request（PLR）:提供位置请求Provide Location Answer（PLA）提供位置响应Location Report Request（LRR）:位置报告请求Location Report Answer（LRA）位置报告响应
CARRYFLAG|是否携带|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于指示是否在消息中携带该AVP ，对于一个Group AVP，如果设置为不携带，则该Group AVP的子AVP也不会携带。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter AVP Profile的别名，便于识别和记忆。






命令举例 


新增Diameter AVP Profile配置，其中Profile标识为1、AVP Code为1032(RAT-TYPE)、携带M指示、V指示和P指示，名称为zte。
ADD DIM AVP PROFILE:PROFILEID=1,AVPCODE1="1032",MINDICATOR="YES",VINDICATOR="YES",PINDICATOR="YES",NAME="zte"; 








父主题： [Diameter AVP Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改Diameter AVP Profile配置(SET DIM AVP PROFILE) 
### 修改Diameter AVP Profile配置(SET DIM AVP PROFILE) 


命令功能 

本命令用于修改已有的Diameter AVP Profile配置。当需要改变现有的某消息某AVP中“M,V,P”标记位或者控制该AVP是否携带时，使用该命令。修改成功后，Diameter AVP控制策略将按照新的Profile定义的控制策略进行。


注意事项 



 
该命令需要加载支持该特性的安全变量，对应的安全变量项为“软件参数65560（是否支持Diameter AVP 控制功能）”。
 

 
配置的Profile需要被关联才能生效，其中Diameter基础协议消息在SET DIAMROUTE中被关联；DiameterS6a口业务消息需要在SET DIAMADJ中被关联；DiameterSLg口业务消息需要在SET DIAMGMLCADJ中被关联。
 

 
该AVP控制只对出向消息有效，而对入向消息无效。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|该参数用于指定一个Diameter AVP控制Profile标识号，需全局唯一。
COMMANDNAME|Command Name|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|命令码名称，该参数用于区分具体的消息，取值含义：Capabilities Exchange Request（CER）:能力协商请求Capabilities Exchange Answer（CEA）:能力协商响应Device Watchdog Request（DWR）:设备检测请求Device Watchdog Answer（DWA）:设备检测响应Disconnect Peer Request（DPR）:对端断开连接请求Disconnect Peer Answer（DPA）:对端断开连接响应Update Location Request（ULR）:位置更新请求Update Location Answer（ULA）:位置更新响应Cancel Location Request（CLR）:取消位置请求Cancel Location Answer（ULA）:取消位置响应Authentication Information Request（AIR）:鉴权信息请求Authentication Information Answer（AIA）:鉴权信息响应Insert Subscriber Data Request（IDR）:插入签约数据请求Insert Subscriber Answer（IDA）:插入签约数据响应Delete Subscriber Data Request（DSR）:删除签约数据请求Delete Subscriber Data  Answer（DSA）:删除签约数据响应Purge UE Request（PUR）:清除用户请求Purge UE Answer（PUA）清除用户响应Reset Request（RSR）:重启请求Reset Answer（RSA）重启响应Notify Request（NOR）:通知请求Notify Answer（NOA）通知响应Provide Location Request（PLR）:提供位置请求Provide Location Answer（PLA）提供位置响应Location Report Request（LRR）:位置报告请求Location Report Answer（LRA）位置报告响应
AVPCODE1|AVP Code|参数可选性:必须单选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要被控制AVP的AVP 码，仅包含一些比较常用的需要被控制的AVP，各个AVP含义可以参见协议3GPP TS 29.272的7.3.1节。
AVPCODE2|AVP Code|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~65535。|该参数用于指定需要被控制AVP的AVP 码，手动输入，用于AVPCODE1中未包含的AVP，各个AVP含义可以参见协议3GPP TS 29.272。
MINDICATOR|M指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|M指示，强制比特，具体含义可以参见RFC3588的4.1节。
VINDICATOR|V指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|V指示，是否携带制造商标记，具体含义可以参见RFC3588的4.1节。
PINDICATOR|P指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|P指示，指明为保证端到端安全需要加密，具体含义可以参见RFC3588的4.1节。
VENDERID|Vender ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|Vender 标识，制造商标识，每一个设备厂家均被有自己的制造商标识。
CARRYFLAG|是否携带|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否在消息中携带该AVP ，对于一个Group AVP，如果设置为不携带，则该Group AVP的子AVP也不会携带。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter AVP Profile的别名，便于识别和记忆。






命令举例 


修改Profile标识为1，命令名称为Capabilities-Exchange- Request，AVP Code为RAT-TYPE的Diameter AVP Profile配置数据、将M指示修改为不携带。
SET DIM AVP profile:profileID=1,COMMANDNAME="CER",AVPCODE1="1032",MINDICATOR="NO"; 








父主题： [Diameter AVP Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除Diameter AVP Profile配置(DEL DIM AVP PROFILE) 
### 删除Diameter AVP Profile配置(DEL DIM AVP PROFILE) 


命令功能 

本命令用于删除Diameter AVP Profile配置。当需要恢复为默认情况下某消息某AVP中“M,V,P”标记位或者控制该AVP是否携带时，使用该命令。删除成功后，该消息中的AVP 控制策略将按照默认的控制策略进行。


注意事项 

删除某Profile时，需要先删除Profile在[SET DIAMROUTE]（diameter基础协议消息），[SET DIAMADJ]（diameterS6a口业务消息），[SET DIAMGMLCADJ]（diameterSlg口业务消息）或[SET DIMMEG ANALYSIS]（diameter消息分析结果索引）中的关联关系。具体删除关联关系的方法为在上述四条命令中指定参数PROFILEID/AVPPROID的值为0即可。


参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|该参数用于指定一个Diameter AVP控制Profile标识号，需全局唯一。
AVPCODE1|AVP Code|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要被控制AVP的AVP 码，仅包含一些比较常用的需要被控制的AVP，各个AVP含义可以参见协议3GPP TS 29.272的7.3.1节。
AVPCODE2|AVP Code|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~65535。|该参数用于指定需要被控制AVP的AVP 码，手动输入，用于AVPCODE1中未包含的AVP，各个AVP含义可以参见协议3GPP TS 29.272。
COMMANDNAME|Command Name|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|命令码名称，该参数用于区分具体的消息，取值含义：Capabilities Exchange Request（CER）:能力协商请求Capabilities Exchange Answer（CEA）:能力协商响应Device Watchdog Request（DWR）:设备检测请求Device Watchdog Answer（DWA）:设备检测响应Disconnect Peer Request（DPR）:对端断开连接请求Disconnect Peer Answer（DPA）:对端断开连接响应Update Location Request（ULR）:位置更新请求Update Location Answer（ULA）:位置更新响应Cancel Location Request（CLR）:取消位置请求Cancel Location Answer（ULA）:取消位置响应Authentication Information Request（AIR）:鉴权信息请求Authentication Information Answer（AIA）:鉴权信息响应Insert Subscriber Data Request（IDR）:插入签约数据请求Insert Subscriber Answer（IDA）:插入签约数据响应Delete Subscriber Data Request（DSR）:删除签约数据请求Delete Subscriber Data  Answer（DSA）:删除签约数据响应Purge UE Request（PUR）:清除用户请求Purge UE Answer（PUA）清除用户响应Reset Request（RSR）:重启请求Reset Answer（RSA）重启响应Notify Request（NOR）:通知请求Notify Answer（NOA）通知响应Provide Location Request（PLR）:提供位置请求Provide Location Answer（PLA）提供位置响应Location Report Request（LRR）:位置报告请求Location Report Answer（LRA）位置报告响应






命令举例 


删除Profile标识为1的Diameter AVP Profile配置数据。
DEL DIM AVP PROFILE:PROFILEID=1; 








父主题： [Diameter AVP Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询Diameter AVP Profile配置(SHOW DIM AVP PROFILE) 
### 查询Diameter AVP Profile配置(SHOW DIM AVP PROFILE) 


命令功能 

本命令用于查询Diameter AVP Profile配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数用于指定一个Diameter AVP控制Profile标识号，需全局唯一。
AVPCODE1|AVP Code|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要被控制AVP的AVP 码，仅包含一些比较常用的需要被控制的AVP，各个AVP含义可以参见协议3GPP TS 29.272的7.3.1节。
AVPCODE2|AVP Code|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~65535。|该参数用于指定需要被控制AVP的AVP 码，手动输入，用于AVPCODE1中未包含的AVP，各个AVP含义可以参见协议3GPP TS 29.272。
COMMANDNAME|Command Name|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|命令码名称，该参数用于区分具体的消息，取值含义：Capabilities Exchange Request（CER）:能力协商请求Capabilities Exchange Answer（CEA）:能力协商响应Device Watchdog Request（DWR）:设备检测请求Device Watchdog Answer（DWA）:设备检测响应Disconnect Peer Request（DPR）:对端断开连接请求Disconnect Peer Answer（DPA）:对端断开连接响应Update Location Request（ULR）:位置更新请求Update Location Answer（ULA）:位置更新响应Cancel Location Request（CLR）:取消位置请求Cancel Location Answer（ULA）:取消位置响应Authentication Information Request（AIR）:鉴权信息请求Authentication Information Answer（AIA）:鉴权信息响应Insert Subscriber Data Request（IDR）:插入签约数据请求Insert Subscriber Answer（IDA）:插入签约数据响应Delete Subscriber Data Request（DSR）:删除签约数据请求Delete Subscriber Data  Answer（DSA）:删除签约数据响应Purge UE Request（PUR）:清除用户请求Purge UE Answer（PUA）清除用户响应Reset Request（RSR）:重启请求Reset Answer（RSA）重启响应Notify Request（NOR）:通知请求Notify Answer（NOA）通知响应Provide Location Request（PLR）:提供位置请求Provide Location Answer（PLA）提供位置响应Location Report Request（LRR）:位置报告请求Location Report Answer（LRA）位置报告响应






输出参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|Profile标识|参数可选性:任选参数；参数类型:整数。|该参数用于指定一个Diameter AVP控制Profile标识号，需全局唯一。
AVPCODE|AVP Code|参数可选性:任选参数；参数类型:整数。|AVP Code
MINDICATOR|M指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|M指示，强制比特，具体含义可以参见RFC3588的4.1节。
VINDICATOR|V指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|V指示，是否携带制造商标记，具体含义可以参见RFC3588的4.1节。
PINDICATOR|P指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|P指示，指明为保证端到端安全需要加密，具体含义可以参见RFC3588的4.1节。
VENDERID|Vender ID|参数可选性:任选参数；参数类型:整数。|Vender 标识，制造商标识，每一个设备厂家均被有自己的制造商标识。
COMMANDNAME|Command Name|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|命令码名称，该参数用于区分具体的消息，取值含义：Capabilities Exchange Request（CER）:能力协商请求Capabilities Exchange Answer（CEA）:能力协商响应Device Watchdog Request（DWR）:设备检测请求Device Watchdog Answer（DWA）:设备检测响应Disconnect Peer Request（DPR）:对端断开连接请求Disconnect Peer Answer（DPA）:对端断开连接响应Update Location Request（ULR）:位置更新请求Update Location Answer（ULA）:位置更新响应Cancel Location Request（CLR）:取消位置请求Cancel Location Answer（ULA）:取消位置响应Authentication Information Request（AIR）:鉴权信息请求Authentication Information Answer（AIA）:鉴权信息响应Insert Subscriber Data Request（IDR）:插入签约数据请求Insert Subscriber Answer（IDA）:插入签约数据响应Delete Subscriber Data Request（DSR）:删除签约数据请求Delete Subscriber Data  Answer（DSA）:删除签约数据响应Purge UE Request（PUR）:清除用户请求Purge UE Answer（PUA）清除用户响应Reset Request（RSR）:重启请求Reset Answer（RSA）重启响应Notify Request（NOR）:通知请求Notify Answer（NOA）通知响应Provide Location Request（PLR）:提供位置请求Provide Location Answer（PLA）提供位置响应Location Report Request（LRR）:位置报告请求Location Report Answer（LRA）位置报告响应
CARRYFLAG|是否携带|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否在消息中携带该AVP ，对于一个Group AVP，如果设置为不携带，则该Group AVP的子AVP也不会携带。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter AVP Profile的别名，便于识别和记忆。






命令举例 


查询所有的Diameter AVP Profile配置。
SHOW DIM AVP PROFILE; 


`

命令 (No.1): SHOW DIM AVP PROFILE

操作维护         Profile标识   AVP Code     M指示    V指示    P指示    Vender ID    Command Name                         是否携带   用户别名
--------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1             1032         携带     携带     携带     10415        Update-Location-Request              携带       
--------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。


` 








父主题： [Diameter AVP Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置默认Diameter AVP Profile配置(SET DEFAULT DIM AVP PROFILE) 
### 设置默认Diameter AVP Profile配置(SET DEFAULT DIM AVP PROFILE) 


命令功能 

设置默认Diameter AVP Profile配置


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|Profile标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|该参数用于指定一个默认的Diameter AVP控制Profile标识号。






命令举例 


设置默认Diameter AVP Profile配置，其中Profile标识为2
SET DEFAULT DIM AVP PROFILE:PROFILEID=2; 








父主题： [Diameter AVP Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 清除默认Diameter AVP Profile配置(CLEAR DEFAULT DIM AVP PROFILE) 
### 清除默认Diameter AVP Profile配置(CLEAR DEFAULT DIM AVP PROFILE) 


命令功能 

清除默认Diameter AVP Profile配置


注意事项 



 
该命令需要加载支持该特性的安全变量，对应的安全变量项为“软件参数65560（是否支持Diameter AVP 控制功能）”。
 

 
配置的Profile需要被关联才能生效，其中Diameter基础协议消息在SET DIAMROUTE中被关联；DiameterS6a口业务消息需要在SET DIAMADJ中被关联；DiameterSLg口业务消息需要在SET DIAMGMLCADJ中被关联。
 

 
该AVP控制只对出向消息有效，而对入向消息无效。
 

 




命令举例 


清除默认Diameter AVP profile
CLEAR DEFAULT DIM AVP PROFILE; 








父主题： [Diameter AVP Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询默认Diameter AVP Profile配置(SHOW DEFAULT DIM AVP PROFILE) 
### 查询默认Diameter AVP Profile配置(SHOW DEFAULT DIM AVP PROFILE) 


命令功能 

查询默认Diameter AVP Profile配置


注意事项 



 
该命令需要加载支持该特性的安全变量，对应的安全变量项为“软件参数65560（是否支持Diameter AVP 控制功能）”。
 

 
配置的Profile需要被关联才能生效，其中Diameter基础协议消息在SET DIAMROUTE中被关联；DiameterS6a口业务消息需要在SET DIAMADJ中被关联；DiameterSLg口业务消息需要在SET DIAMGMLCADJ中被关联。
 

 
该AVP控制只对出向消息有效，而对入向消息无效。
 

 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
PROFILEID|Profile标识|参数可选性:任选参数；参数类型:字符型。|该参数用于指定一个默认的Diameter AVP控制Profile标识号。






命令举例 


查询默认Diameter AVP Profile配置。
SHOW DEFAULT DIM AVP PROFILE; 


`

命令 (No.1): SHOW DEFAULT DIM AVP PROFILE

Profile标识 
--------------
N/A 
--------------
记录数 1

命令执行成功（耗时 0.012 秒）。
` 








父主题： [Diameter AVP Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Diameter连接路由配置 
## Diameter连接路由配置 


背景知识 


MME与HSS、EIR和GMLC网元之间的S6a口、S13口和Slg口均使用Diameter协议。 




功能描述 


MME向HSS发送消息时，获取路由过程如下： 







                        分析用户的IMSI号码，获取用户归属的HSS局向ID，对应的配置命令为：
                        [ADD MDNAL]
                        和
                        [ADD DIMOFC ANALYSIS]
                        。
                    







                        跟据HSS局向ID，获取到Diameter 局向路由，对应的配置命令：
                        [ADD DIAMADJ]
                        。
                    







                        根据Diameter局向路由ID查询到Diameter路由组， 对应的配置命令为：
                        [ADD DIAMADJROUTE]
                        。
                    







                        根据Diameter路由组ID查询到Diameter路由， 对应的配置命令为：
                        [ADD DIAMROUTEGROUP]
                        。
                    







                        根据Diameter路由ID查询到Diamete链路组， 对应的配置命令为：
                        [ADD DIAMROUTE]
                        。
                    







                        根据Diameter链路组ID查询到SCTP连接标识， 对应的配置命令为：
                        [ADD DIAMLINKGROUP]
                        。其中，SCTP连接标识已经在Diameter偶联中配置，对应的配置命令为：
                        [ADD SCTP]
                        。
                    







                MME向EIR发送消息，获取到EIR局向ID，对应的配置命令：
                [ADD DIAMEIR]
                ，后续处理同上2-6步骤。
            


MME向GMLC发送消息，获取路由过程如下： 







                        分析GMLC网元标识号码，获取用户归属的GMLC局向ID，对应的配置命令为：
                        [ADD MDNAL]
                        和
                        [ADD DIMGMLC ANALYSIS]
                        。
                    







                        根据GMLC局向ID，获取到Diameter GMLC局向路由，对应的配置命令：
                        [ADD DIAMGMLCADJ]
                        。
                    







                        根据Diameter GMLC局向路由ID查询到Diameter路由组， 对应的配置命令为：
                        [ADD DIAMGMLCROUTE]
                        。
                    






后续处理同上4-6步骤。 








相关主题 



 

Diameter连接配置
 

 

Diameter链路组配置
 

 

Diameter路由配置
 

 

Diameter路由组配置
 

 

Diameter局向路由配置
 

 

Diameter局向配置
 

 

Diameter EIR 配置
 

 








父主题： [Diameter配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter连接配置 
### Diameter连接配置 


背景知识 


Diameter连接承载在SCTP偶联上，一个Diameter连接对应一条SCTP偶联。偶联建立成功后，MME发出CER消息进行能力协商，收到CEA成功响应后Diameter链路建立成功 




功能描述 


通过Diameter连接配置，可配置MME网元的Diameter链路使用的SCTP偶联ID，以及此链路上对端网元的目的域名和目的主机名。 




相关主题 



 

新增Diameter连接配置(ADD DIAMCONN)
 

 

修改Diameter连接配置(SET DIAMCONN)
 

 

修改本端主机名和域名(SET HOST DOMAIN)
 

 

删除Diameter连接配置(DEL DIAMCONN)
 

 

查询Diameter连接配置(SHOW DIAMCONN)
 

 








父主题： [Diameter连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter连接配置(ADD DIAMCONN) 
#### 新增Diameter连接配置(ADD DIAMCONN) 


命令功能 

本命令用于增加一条Diameter连接数据配置。当两个网元之间需要使用Diameter协议进行通信时，要在两端配置Diameter连接路由数据，其中首先需要配置Diameter连接数据。Diameter连接数据配置成功后，两个网元之间Diameter层就通了，是使用Diameter协议交互的前提条件之一。


注意事项 



 
该命令需要引用某条SCTP链路，配置前，需要先配置SCTP链路，SCTP链路的配置参见ADD SCTP。
 

 
该Diameter连接数据中，本端的主机名和域名是默认生成的。如果默认生成的主机名和域名不为所期望的，可以通过SET HOST DOMAIN命令进行修改。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ADJNAME|对端节点主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|该参数指定某一条Diameter连接的对端主机名。当启用局向主机名时，业务消息会使用该命令中的主机名进行交互，局向主机名的查询参见SHOW DIAMADJROUTE。
ADJDOMAIN|对端节点域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数指定某一条Diameter连接的对端域名。当启用局向域名时，业务消息会使用该命令中的域名进行交互，局向域名的查询参见SHOW DIAMADJROUTE。
SCTPID|SCTP连接标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4112。|目前本设备中Diameter层均承载在SCTP协议之上，该参数用于指定该Diameter连接对应的SCTP标识，SCTP标识可以通过命令查询。
NAME|Diameter连接名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数指定了某Diameter连接的名称，便于识别和记忆。






命令举例 


新增Diameter连接，关联的SCTP链路为88，对端主机名为“hss98.zte.com.cn”，对端域名为"zte.com.cn"。
ADD DIAMCONN:ADJNAME="hss98.zte.com.cn",ADJDOMAIN="zte.com.cn",SCTPID=88; 








父主题： [Diameter连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter连接配置(SET DIAMCONN) 
#### 修改Diameter连接配置(SET DIAMCONN) 


命令功能 

本命令用于修改一条已存在的Diameter连接配置数据。当需要修改本端Diameter连接数据，例如，本端主机名和域名的配置时，使用该命令。修改成功后，可以改变本端主机名和域名为非默认值。


注意事项 

该命令需要引用某条SCTP链路，配置前，需要先配置SCTP链路，SCTP链路的配置参见[ADD SCTP]。


参数说明 


标识|名称|类型|说明
---|---|---|---
SCTPID|SCTP连接标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4112。|目前本设备中Diameter层均承载在SCTP协议之上，该参数用于指定该Diameter连接对应的SCTP标识，SCTP标识可以通过命令查询。
ADJNAME|对端节点主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|该参数指定某一条Diameter连接的对端主机名。当启用局向主机名时，业务消息会使用该命令中的主机名进行交互，局向主机名的查询参见SHOW DIAMADJROUTE。
ADJDOMAIN|对端节点域名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|该参数指定某一条Diameter连接的对端域名。当启用局向域名时，业务消息会使用该命令中的域名进行交互，局向域名的查询参见SHOW DIAMADJROUTE。
NAME|Diameter连接名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数指定了某Diameter连接的名称，便于识别和记忆。






命令举例 


修改关联SCTP为88的Diameter连接的本端主机名为"mme3.zte.com.cn"，本端域名为"zte.com.cn"。
SET DIAMCONN:SCTPID=88,HOSTNAME="mme3.zte.com.cn",HOSTDOMAIN="zte.com.cn"; 








父主题： [Diameter连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改本端主机名和域名(SET HOST DOMAIN) 
#### 修改本端主机名和域名(SET HOST DOMAIN) 


命令功能 

该命令用于修改本端主机名和域名。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
HOSTNAME|本端节点主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|本端节点主机名
HOSTDOMAIN|本端节点域名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|本端节点域名






命令举例 


修改关联SCTP为88的Diameter连接的本端节点主机名为"mme3.zte.com.cn"，本端节点域名为"zte.com.cn"。
SET HOST DOMAIN:HOSTNAME="mme3.zte.com.cn",HOSTDOMAIN="zte.com.cn"; 








父主题： [Diameter连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter连接配置(DEL DIAMCONN) 
#### 删除Diameter连接配置(DEL DIAMCONN) 


命令功能 

本命令用于删除一条已存在的Diameter连接配置数据。删除后，该链路即将断开，无法在该链路上收发Diameter消息。


注意事项 

删除前，需要先将该Diameter连接在Diameter链路组配置中去关联，Diameter链路组配置数据查询参见[SHOW DIAMLINKGROUP]。


参数说明 


标识|名称|类型|说明
---|---|---|---
SCTPID|SCTP连接标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4112。|目前本设备中Diameter层均承载在SCTP协议之上，该参数用于指定该Diameter连接对应的SCTP标识，SCTP标识可以通过命令查询。






命令举例 


删除关联SCTP为88的Diameter连接。
DEL DIAMCONN:SCTPID=88; 








父主题： [Diameter连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter连接配置(SHOW DIAMCONN) 
#### 查询Diameter连接配置(SHOW DIAMCONN) 


命令功能 

本命令用于显示所有已配置的Diameter连接配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
SCTPID|SCTP连接标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4112。|目前本设备中Diameter层均承载在SCTP协议之上，该参数用于指定该Diameter连接对应的SCTP标识，SCTP标识可以通过命令查询。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
SCTPID|SCTP连接标识|参数可选性:任选参数；参数类型:整数。|目前本设备中Diameter层均承载在SCTP协议之上，该参数用于指定该Diameter连接对应的SCTP标识，SCTP标识可以通过命令查询。
HOSTNAME|本端节点主机名|参数可选性:任选参数；参数类型:字符型。|该参数指定某一条Diameter连接的本端主机名，在新增Diameter连接时默认生成。如需要修改则使用修改命令：SET DIAMCONN。
HOSTDOMAIN|本端节点域名|参数可选性:任选参数；参数类型:字符型。|该参数指定某一条Diameter连接的本端域名，在新增Diameter连接时默认生成。如需要修改则使用修改命令：SET DIAMCONN。
ADJNAME|对端节点主机名|参数可选性:任选参数；参数类型:字符型。|该参数指定某一条Diameter连接的对端主机名。当启用局向主机名时，业务消息会使用该命令中的主机名进行交互，局向主机名的查询参见SHOW DIAMADJROUTE。
ADJDOMAIN|对端节点域名|参数可选性:任选参数；参数类型:字符型。|该参数指定某一条Diameter连接的对端域名。当启用局向域名时，业务消息会使用该命令中的域名进行交互，局向域名的查询参见SHOW DIAMADJROUTE。
NAME|Diameter连接名称|参数可选性:任选参数；参数类型:字符型。|该参数指定了某Diameter连接的名称，便于识别和记忆。






命令举例 


显示所有已配置的Diameter连接配置数据。
SHOW DIAMCONN 


`

命令 (No.1): SHOW DIAMCONN

操作维护         SCTP连接标识   本端节点主机名                                           本端节点域名                        对端节点主机名   对端节点域名   Diameter连接名称
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   5              mmec01.mmegi8000.mme.epc.mnc001.mcc460.3gppnetwork.org   epc.mnc001.mcc460.3gppnetwork.org                    zte.com.cn     5
复制 修改 删除   22             mmec01.mmegi8000.mme.epc.mnc001.mcc460.3gppnetwork.org   epc.mnc001.mcc460.3gppnetwork.org                    22             
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.033 秒）。


` 








父主题： [Diameter连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter链路组配置 
### Diameter链路组配置 


背景知识 


MME向HSS发送消息，路由逻辑是首先基于IMSI号码分析得到局向ID，局向ID得到局向路由，后面逻辑是局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路。在IMSI号码分析失败时，直接获取默认局向路由。 




功能描述 


通过Diameter链路组配置，可以配置MME中Diameter链路组包含哪些Diameter链路，其中模式可选择N+M主备或负荷分担，选为N+M主备模式时，主用链路个数N值可配。 




相关主题 



 

新增Diameter链路组配置(ADD DIAMLINKGROUP)
 

 

修改Diameter链路组配置(SET DIAMLINKGROUP)
 

 

删除Diameter链路组配置(DEL DIAMLINKGROUP)
 

 

查询Diameter链路组配置(SHOW DIAMLINKGROUP)
 

 








父主题： [Diameter连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter链路组配置(ADD DIAMLINKGROUP) 
#### 新增Diameter链路组配置(ADD DIAMLINKGROUP) 


命令功能 

该命令用于新增一个Diameter链路组，当需要将一条或多条Diameter连接添加到某Diameter链路组中时，使用该命令。新增Diameter链路组成功后，可以从逻辑上维护一组Diameter连接。


注意事项 



 
一个Diameter链路组最多包含16个Diameter链路。
 

 
配置Diameter链路组前，需要先配置Diameter连接数据，配置命令参见ADD DIAMCONN。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
LINKGRPID|Diameter链路组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter链路组标识号，需全局唯一。
SCTPLINKID|SCTP连接标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4112。|该参数用于指定本Diameter链路组包含的Diameter链路，1个Diameter链路组最多包含16个Diameter链路。
PARTAKEMODE|分担方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定本Diameter链路组中Diameter链路的分担方式，取值含义：N+M Backup: N+M 主备方式Load Partake: 负荷分担方式说明：如果只配置一条链路，则总是会选到该链路，使用N+M主备方式和负荷分担的方式效果是一样的。
MASTERNUM|主用链路个数（N）|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数配置原则如下：该参数只有当“分担方式”配置为N+M Backup才有效，该参数为可选参数，当未配置参数时，N默认为1。当N>1时，业务将会在该N个链路中进行轮选。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter链路组的别名，便于识别和记忆。






命令举例 


将SCTP连接标识为1的Diameter连接添加到ID为1的Diameter链路组中，采用N+M备份方式、主用链路个数为10。
ADD DIAMLINKGROUP:LINKGRPID=1,SCTPLINKID=1,PARTAKEMODE="BACKUP",MASTERNUM=10; 








父主题： [Diameter链路组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改DIAMETER链路组配置(SET DIAMLINKGROUP) 
#### 修改DIAMETER链路组配置(SET DIAMLINKGROUP) 


命令功能 

该命令用于修改一个已经存在的Diameter链路组，当需要修改本Diameter链路组中Diameter连接的构成或者改变本Diameter链路组内Diameter连接的分担方式和权重时，使用该命令。Diameter链路组为一组Diameter连接的集合，当一条或多条Diameter连接属于同一个Diameter链路组时，可以从逻辑上维护该组Diameter连接。


注意事项 



 
一个Diameter链路组最多包含16个Diameter链路。
 

 
配置Diameter链路组前，需要先配置Diameter连接数据，配置命令参见ADD DIAMCONN。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
LINKGRPID|Diameter链路组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter链路组标识号，需全局唯一。
SCTPLINKID|SCTP连接标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4112。|该参数用于指定本Diameter链路组包含的Diameter链路，1个Diameter链路组最多包含16个Diameter链路。
PARTAKEMODE|分担方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定本Diameter链路组中Diameter链路的分担方式，取值含义：N+M Backup: N+M 主备方式Load Partake: 负荷分担方式说明：如果只配置一条链路，则总是会选到该链路，使用N+M主备方式和负荷分担的方式效果是一样的。
MASTERNUM|主用链路个数（N）|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数配置原则如下：该参数只有当“分担方式”配置为N+M Backup才有效，该参数为可选参数，当未配置参数时，N默认为1。当N>1时，业务将会在该N个链路中进行轮选。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter链路组的别名，便于识别和记忆。






命令举例 


修改ID为1的Diameter链路组配置数据，将SCTP连接标识修改为1，备份方式修改为N+M、主用链路个数修改为10。
SET DIAMLINKGROUP:LINKGRPID=1,SCTPLINKID=1,PARTAKEMODE="BACKUP",MASTERNUM=10; 








父主题： [Diameter链路组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除DIAMETER链路组配置(DEL DIAMLINKGROUP) 
#### 删除DIAMETER链路组配置(DEL DIAMLINKGROUP) 


命令功能 

该命令用于删除一个已经存在的Diameter链路组。Diameter链路组为一组Diameter连接的集合，当一条或多条Diameter连接属于同一个Diameter链路组时，可以从逻辑上维护该组Diameter连接。


注意事项 

删除前，需要先将该Diameter链路组在Diameter路由配置中去关联，Diameter路由配置数据查询参见[SHOW DIAMROUTE]。


参数说明 


标识|名称|类型|说明
---|---|---|---
LINKGRPID|Diameter链路组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter链路组标识号，需全局唯一。






命令举例 


删除ID为1的Diameter链路组。
DEL DIAMLINKGROUP:LINKGRPID=1; 








父主题： [Diameter链路组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询DIAMETER链路组配置(SHOW DIAMLINKGROUP) 
#### 查询DIAMETER链路组配置(SHOW DIAMLINKGROUP) 


命令功能 

该命令用于查询Diameter链路组配置。Diameter链路组为一组Diameter连接的集合，当一条或多条Diameter连接属于同一个Diameter链路组时，可以从逻辑上维护该组Diameter连接。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
LINKGRPID|Diameter链路组ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter链路组标识号，需全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
LINKGRPID|Diameter链路组ID|参数可选性:任选参数；参数类型:整数。|该参数用于指定Diameter链路组标识号，需全局唯一。
PARTAKEMODE|分担方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定本Diameter链路组中Diameter链路的分担方式，取值含义：N+M Backup: N+M 主备方式Load Partake: 负荷分担方式说明：如果只配置一条链路，则总是会选到该链路，使用N+M主备方式和负荷分担的方式效果是一样的。
SCTPLINKID|SCTP连接标识|参数可选性:任选参数；参数类型:字符型。|该参数用于指定本Diameter链路组包含的Diameter链路，1个Diameter链路组最多包含16个Diameter链路。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型。|该Diameter链路组的别名，便于识别和记忆。
MASTERNUM|主用链路个数（N）|参数可选性:任选参数；参数类型:字符型。|该参数配置原则如下：该参数只有当“分担方式”配置为N+M Backup才有效，该参数为可选参数，当未配置参数时，N默认为1。当N>1时，业务将会在该N个链路中进行轮选。
BACKUPNUM|备用链路个数（M）|参数可选性:任选参数；参数类型:字符型。|备用链路个数（M）






命令举例 


查询所有的Diameter链路组配置数据。
SHOW DIAMLINKGROUP; 


`

命令 (No.1): SHOW DIAMLINKGROUP

操作维护         Diameter链路组ID   分担方式   SCTP连接标识   用户别名   主用链路个数（N）   备用链路个数（M）
--------------------------------------------------------------------------------------------------------------
复制 修改 删除   5                  负荷分担   5                         N/A                 N/A
复制 修改 删除   22                 负荷分担   22                        N/A                 N/A
--------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.033 秒）。


` 








父主题： [Diameter链路组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter路由配置 
### Diameter路由配置 


背景知识 


MME向HSS发送消息，路由逻辑是首先基于IMSI号码分析得到局向ID，局向ID得到局向路由，后面逻辑是局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路。在IMSI号码分析失败时，直接获取默认局向路由。 




功能描述 


通过Diameter路由配置，可以配置MME中Diameter路由包含哪些Diameter链路，其中模式可选择主备或负荷分担。 


配置Diameter链路建立是MME本端能力属性以及能力参数携带位置（内外层都携带、外层携带或内层携带）。 


配置Diameter链路的管理消息（CER/CEA、DWR/DWA等）中AVP编辑Profile ID，通过此Profile ID在“Diameter AVP Profile配置”中获得具体的AVP字段编辑策略。 




相关主题 



 

新增Diameter路由配置(ADD DIAMROUTE)
 

 

修改Diameter路由配置(SET DIAMROUTE)
 

 

删除Diameter路由配置(DEL DIAMROUTE)
 

 

查询Diameter路由配置(SHOW DIAMROUTE)
 

 








父主题： [Diameter连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter路由配置(ADD DIAMROUTE) 
#### 新增Diameter路由配置(ADD DIAMROUTE) 


命令功能 

该命令用于新增一个Diameter路由，当需要将一个或两个Diameter链路组添加到某Diameter路由中时，使用该命令。新增Diameter路由成功后，可以从逻辑上维护一组Diameter链路组。


注意事项 



 
一个Diameter路由中最多包含两个Diameter链路组。
 

 
配置Diameter路由前，需要先配置Diameter链路组数据，配置命令参见ADD DIAMLINKGROUP。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|Diameter路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter路由标识号，需全局唯一。
LINKGRPID|Diamerter链路组|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定本Diameter路由下关联的Diameter链路组集。一个Diameter路由下可以关联一至两个Diameter链路组。
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BACKUP。|该参数用于指定本Diameter路由中Diameter链路组的分担方式，取值含义：Master and Slave(Backup): 主备方式Partake: 负荷分担方式
ABILITY|路由协商本端能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:S6aS6d&S13S13&Slg&SGd。|只有当路由具有指定的能力时，才能进行相应业务。该参数指定了本端能力，取值如下：S6aS6d：HSS与MME之间接口，完成用户接入认证、插入用户签约数据、对用户接入PDN进行授权，与非3GPP系统互联时对用户的移动性管理消息的认证等功能。S13S13'：EIR与MME之间接口,完成用户接入认证。 SLg：MME与GMLC之间的接口，完成用户的定位业务。说明：网元之间通过能力协商过程得到最终路由的能力值。本端路由协商之后的能力可以通过命令SHOW DIMROUTE INFO查看。
LOCATION|携带位置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:ALL。|该参数指定了在能力协商过程中，本端路由能力值的携带位置。能力值可以通过Auth-Application-Id AVP（外层携带）或Vendor-Specific-Application-Id AVP（内层携带）来携带给对端，具体定义可以参见RFC3588的6.8节和6.9节。该参数取值可以为：内外层都携带（ALL）外层携带（External） 内层携带（Internal）说明：该参数为可选参数，当未配置该参数时，默认取值为内外层都携带（ALL）。
PROFILEID|Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。默认值:0。|该参数用于基础协议消息的AVP控制所用，AVP控制策略配置参见SHOW DIM AVP PROFILE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter路由的别名，便于识别和记忆。






命令举例 


新增一条Diameter路由数据，设置Diameter路由ID为1、Diamerter链路组为1，其他参数按默认配置。
ADD DIAMROUTE:ROUTEID=1,LINKGRPID=1; 








父主题： [Diameter路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter路由配置(SET DIAMROUTE) 
#### 修改Diameter路由配置(SET DIAMROUTE) 


命令功能 

该命令用于修改一个已经存在的Diameter路由，当需要修改本Diameter路由中Diameter链路组的构成或者改变本Diameter路由内Diameter链路组的分担方式和权重时，使用该命令。Diameter路由为一个或两个Diameter链路组的集合，当一个或两个Diameter链路组属于同一个Diameter路由时，可以从逻辑上维护该组Diameter链路组。


注意事项 



 
一个Diameter路由中最多包含两个Diameter链路组。
 

 
配置Diameter路由前，需要先配置Diameter链路组数据，配置命令参见ADD DIAMLINKGROUP。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|Diameter路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter路由标识号，需全局唯一。
LINKGRPID|Diamerter链路组|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定本Diameter路由下关联的Diameter链路组集。一个Diameter路由下可以关联一至两个Diameter链路组。
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定本Diameter路由中Diameter链路组的分担方式，取值含义：Master and Slave(Backup): 主备方式Partake: 负荷分担方式
ABILITY|路由协商本端能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|只有当路由具有指定的能力时，才能进行相应业务。该参数指定了本端能力，取值如下：S6aS6d：HSS与MME之间接口，完成用户接入认证、插入用户签约数据、对用户接入PDN进行授权，与非3GPP系统互联时对用户的移动性管理消息的认证等功能。S13S13'：EIR与MME之间接口,完成用户接入认证。 SLg：MME与GMLC之间的接口，完成用户的定位业务。说明：网元之间通过能力协商过程得到最终路由的能力值。本端路由协商之后的能力可以通过命令SHOW DIMROUTE INFO查看。
LOCATION|携带位置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指定了在能力协商过程中，本端路由能力值的携带位置。能力值可以通过Auth-Application-Id AVP（外层携带）或Vendor-Specific-Application-Id AVP（内层携带）来携带给对端，具体定义可以参见RFC3588的6.8节和6.9节。该参数取值可以为：内外层都携带（ALL）外层携带（External） 内层携带（Internal）说明：该参数为可选参数，当未配置该参数时，默认取值为内外层都携带（ALL）。
PROFILEID|Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于基础协议消息的AVP控制所用，AVP控制策略配置参见SHOW DIM AVP PROFILE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter路由的别名，便于识别和记忆。






命令举例 


修改路由ID为1的Diameter路由数据，将路由属性修改为负荷分担。
SET DIAMROUTE:ROUTEID=3,PROPERTY="PARTAKE"; 








父主题： [Diameter路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter路由配置(DEL DIAMROUTE) 
#### 删除Diameter路由配置(DEL DIAMROUTE) 


命令功能 

该命令用于删除一个已经存在的Diameter路由。Diameter路由为一个或两个Diameter链路组的集合，当一个或两个Diameter链路组属于同一个Diameter路由时，可以从逻辑上维护该组Diameter链路组。


注意事项 

删除前，需要先将该Diameter路由在Diameter路由组配置中去关联，Diameter路由组配置数据查询参见[SHOW DIAMROUTEGROUP]。


参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|Diameter路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter路由标识号，需全局唯一。






命令举例 


删除路由ID为1的Diameter路由数据。
DEL DIAMROUTE:ROUTEID=1; 








父主题： [Diameter路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter路由配置(SHOW DIAMROUTE) 
#### 查询Diameter路由配置(SHOW DIAMROUTE) 


命令功能 

该命令用于查询Diameter路由配置。Diameter路由为一个或两个Diameter链路组的集合，当一个或两个Diameter链路组属于同一个Diameter路由时，可以从逻辑上维护该组Diameter链路组。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|Diameter路由ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter路由标识号，需全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|Diameter路由ID|参数可选性:任选参数；参数类型:整数。|该参数用于指定Diameter路由标识号，需全局唯一。
LINKGRPID1|Diamerter链路组1|参数可选性:任选参数；参数类型:整数。|Diamerter链路组1
LINKGRPID2|Diamerter链路组2|参数可选性:任选参数；参数类型:整数。|Diamerter链路组2
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定本Diameter路由中Diameter链路组的分担方式，取值含义：Master and Slave(Backup): 主备方式Partake: 负荷分担方式
ABILITY|路由协商本端能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|只有当路由具有指定的能力时，才能进行相应业务。该参数指定了本端能力，取值如下：S6aS6d：HSS与MME之间接口，完成用户接入认证、插入用户签约数据、对用户接入PDN进行授权，与非3GPP系统互联时对用户的移动性管理消息的认证等功能。S13S13'：EIR与MME之间接口,完成用户接入认证。 SLg：MME与GMLC之间的接口，完成用户的定位业务。说明：网元之间通过能力协商过程得到最终路由的能力值。本端路由协商之后的能力可以通过命令SHOW DIMROUTE INFO查看。
LOCATION|携带位置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指定了在能力协商过程中，本端路由能力值的携带位置。能力值可以通过Auth-Application-Id AVP（外层携带）或Vendor-Specific-Application-Id AVP（内层携带）来携带给对端，具体定义可以参见RFC3588的6.8节和6.9节。该参数取值可以为：内外层都携带（ALL）外层携带（External） 内层携带（Internal）说明：该参数为可选参数，当未配置该参数时，默认取值为内外层都携带（ALL）。
PROFILEID|Profile标识|参数可选性:任选参数；参数类型:整数。|该参数用于基础协议消息的AVP控制所用，AVP控制策略配置参见SHOW DIM AVP PROFILE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型。|该Diameter路由的别名，便于识别和记忆。






命令举例 


查询所有的Diameter路由数据。
SHOW DIAMROUTE; 


`

命令 (No.1): SHOW DIAMROUTE

操作维护         Diameter路由ID   Diamerter链路组1   Diamerter链路组2   路由属性   路由协商本端能力           携带位置       Profile标识   用户别名
---------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   5                5                                     主备       S6a\S6d & S13\S13' & Slg   内外层都携带   0             
复制 修改 删除   22               22                                    主备       S6a\S6d & S13\S13' & Slg   内外层都携带   0             
---------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.035 秒）。


` 








父主题： [Diameter路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter路由组配置 
### Diameter路由组配置 


背景知识 


Diameter路由组为多个Diameter路由的集合，Diameter路由之间可选择主备或负荷分担，在向HSS、EIR或GMLC网元发送消息时，均会使用Diameter路由组。 




功能描述 


“Diameter路由组”配置MME网元路由组中的Diameter路由，一个路由组最多可以包含2个路由，如果配置了2个路由，路由间的模式可以选择主备或负荷分担。 


当路由间模式配置为主备时，当主用Diameter路由故障时，选择备用路由。当路由间模式配置为负荷分担时，MME采用轮选的方式选择可用的Diameter路由。 



                配置Diameter路由组前，需要先配置Diameter路由数据，配置命令为
                [ADD DIAMROUTE]
                。
            




相关主题 



 

新增Diameter路由组配置(ADD DIAMROUTEGROUP)
 

 

修改Diameter路由组配置(SET DIAMROUTEGROUP)
 

 

删除Diameter路由组配置(DEL DIAMROUTEGROUP)
 

 

查询Diameter路由组配置(SHOW DIAMROUTEGROUP)
 

 








父主题： [Diameter连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增DIAMETER路由组配置(ADD DIAMROUTEGROUP) 
#### 新增DIAMETER路由组配置(ADD DIAMROUTEGROUP) 


命令功能 

该命令用于新增一个Diameter路由组，当需要将一个或两个Diameter路由添加到某Diameter路由组中时，使用该命令。新增Diameter路由组成功后，可以从逻辑上维护一组Diameter路由。


注意事项 



 
一个Diameter路由组中最多包含两个Diameter路由。
 

 
配置Diameter路由组前，需要先配置Diameter路由数据，配置命令参见ADD DIAMROUTE。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter路由组标识号，需全局唯一。
ROUTEID|Diameter路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|Diamerter路由标识。该参数用于指定本Diameter路由组包含的Diameter路由，一个Diameter路由组中最多包含2个Diameter路由。
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BACKUP。|该参数用于指定本Diameter路由组中Diameter路由的分担方式，取值含义：Master and Slave（BACKUP）: 主备方式Partake（PARTAKE）: 负荷分担方式
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter路由组的别名，便于识别和记忆。






命令举例 


新增一条Diameter路由组数据，设置Diameter路由组ID为1、Diamerter路由ID为1，其他参数按默认配置。
ADD DIAMROUTEGROUP:ROUTEGRPID=1,ROUTEID=1; 








父主题： [Diameter路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改DIAMETER路由组配置(SET DIAMROUTEGROUP) 
#### 修改DIAMETER路由组配置(SET DIAMROUTEGROUP) 


命令功能 

该命令用于修改一个已经存在的Diameter路由组，当需要修改本Diameter路由组中Diameter路由的构成或者改变本Diameter路由组内Diameter路由的分担方式和权重时，使用该命令。Diameter路由组为一个或两个Diameter路由的集合，当一个或两个Diameter路由属于同一个Diameter路由组时，可以从逻辑上维护该组Diameter路由。


注意事项 



 
一个Diameter路由组中最多包含两个Diameter路由。
 

 
配置Diameter路由组前，需要先配置Diameter路由数据，配置命令参见ADD DIAMROUTE。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter路由组标识号，需全局唯一。
ROUTEID|Diameter路由ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|Diamerter路由标识。该参数用于指定本Diameter路由组包含的Diameter路由，一个Diameter路由组中最多包含2个Diameter路由。
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定本Diameter路由组中Diameter路由的分担方式，取值含义：Master and Slave（BACKUP）: 主备方式Partake（PARTAKE）: 负荷分担方式
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter路由组的别名，便于识别和记忆。






命令举例 


修改路由组ID为1的Diameter路由组数据，将路由组属性修改为负荷分担。
SET DIAMROUTEGROUP:ROUTEGRPID=1,PROPERTY="PARTAKE"; 








父主题： [Diameter路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除DIAMETER路由组配置(DEL DIAMROUTEGROUP) 
#### 删除DIAMETER路由组配置(DEL DIAMROUTEGROUP) 


命令功能 

该命令用于删除一个已经存在的Diameter路由组。Diameter路由组为一个或两个Diameter路由的集合，当一个或两个Diameter路由属于同一个Diameter路由组时，可以从逻辑上维护该组Diameter路由。


注意事项 

删除前，需要先将该Diameter路由组在Diameter局向路由配置中去关联，Diameter局向路由配置数据查询参见[SHOW DIAMADJROUTE]。


参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter路由组标识号，需全局唯一。






命令举例 


删除路由组ID为1的Diameter路由组数据。
DEL DIAMROUTEGROUP:ROUTEGRPID=1; 








父主题： [Diameter路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询DIAMETER路由组配置(SHOW DIAMROUTEGROUP) 
#### 查询DIAMETER路由组配置(SHOW DIAMROUTEGROUP) 


命令功能 

该命令用于查询Diameter路由组配置。Diameter路由组为一个或两个Diameter路由的集合，当一个或两个Diameter路由属于同一个Diameter路由组时，可以从逻辑上维护该组Diameter路由。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|Diameter路由组ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定Diameter路由组标识号，需全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|Diameter路由组ID|参数可选性:任选参数；参数类型:整数。|该参数用于指定Diameter路由组标识号，需全局唯一。
ROUTEID1|Diameter路由ID1|参数可选性:任选参数；参数类型:整数。|Diameter路由ID1
ROUTEID2|Diameter路由ID2|参数可选性:任选参数；参数类型:整数。|Diameter路由ID2
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定本Diameter路由组中Diameter路由的分担方式，取值含义：Master and Slave（BACKUP）: 主备方式Partake（PARTAKE）: 负荷分担方式
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型。|该Diameter路由组的别名，便于识别和记忆。






命令举例 


查询所有的Diameter路由组数据。
SHOW DIAMROUTEGROUP; 


`

命令 (No.1): SHOW DIAMROUTEGROUP;

操作维护         Diameter路由组ID   Diameter路由ID1   Diameter路由ID2   路由属性   用户别名
-------------------------------------------------------------------------------------------
复制 修改 删除   5                  5                                   主备       
复制 修改 删除   22                 22                                  主备       
-------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.035 秒）。

` 








父主题： [Diameter路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter局向路由配置 
### Diameter局向路由配置 


背景知识 


MME向HSS发送消息，路由逻辑是首先基于IMSI号码分析得到局向ID，局向ID得到局向路由，后面逻辑是局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路。在IMSI号码分析失败时，直接获取默认局向路由。 




功能描述 


通过Diameter局向路由配置，可以配置局向路由下包含的多个路由组，其中选择为主备或负荷分担模式。 


配置此局向路由是否为默认局向路由，MME中最大只能配置一个默认局向路由。 


配置在此局向路由发送消息时，消息的目的域名和目的主机名。 




相关主题 



 

新增Diameter局向路由配置(ADD DIAMADJROUTE)
 

 

修改Diameter局向路由配置(SET DIAMADJROUTE)
 

 

增加Diameter路由组信息（局向路由中）(ADD ROUTEGROUP LEVANDWGT)
 

 

修改Diameter路由组信息（局向路由中）(SET ROUTEGROUP LEVANDWGT)
 

 

删除Diameter路由组信息（局向路由中）(DEL ROUTEGROUP LEVANDWGT)
 

 

删除Diameter局向路由配置(DEL DIAMADJROUTE)
 

 

查询Diameter局向路由配置(SHOW DIAMADJROUTE)
 

 








父主题： [Diameter连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter局向路由配置(ADD DIAMADJROUTE) 
#### 新增Diameter局向路由配置(ADD DIAMADJROUTE) 


命令功能 

该命令用于新增一个Diameter局向路由，当需要将一个或多个Diameter路由组添加到某Diameter局向路由中时，使用该命令。新增Diameter局向路由成功后，可以从逻辑上维护一组Diameter路由组。


注意事项 



 
一个Diameter局向路由中最多包含16个Diameter路由组。
 

 
配置Diameter局向路由前，需要先配置Diameter路由组数据，配置命令参见ADD DIAMROUTEGROUP。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ADJROUTEID|局向路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指示Diameter局向路由标识号，需全局唯一。
ROUTEGROUP|Diameter路由组|参数可选性:必选参数；参数类型:复合参数|该参数用于指示本Diameter局向路由包含的Diameter路由组信息，由路由组ID、路由组优先级、路由组权重三个参数组成，其中路由组ID由命令ADD DIAMROUTEGROUP配置。1个Diameter局向路由中最多包含16个Diameter路由组。
DEFAULT|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数指示该局向路由是否作为默认局向路由。所谓默认局向路由，就是当没有配置指示局向路由用于寻址时，使用该默认局向路由进行寻址。
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。默认值:0。|该参数指示默认局向路由AVP Profile标识。
ADJREALM|是否启用局向域名|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数指示该局向路由是否启用局向域名。如果选择“是”，则业务消息中的主机名和域名使用本局向路由中的“域名”和“主机名”。如果选择“否”，则业务消息使用Diameter连接中配置的主机名和域名，Diameter连接配置数据查询参见SHOW DIAMCONN。
REALM|域名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|该参数指示本局向路由的域名，当配置启用局向域名时，必须配置。
HOSTNAME|主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|该参数指示本局向路由的主机名，当配置启用局向域名时，必须配置。
SUPFEATUREID|Feature ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。默认值:0。|该参数用于指示默认HSS局向路由关联的Support Feature模板。不同的局向路由可以指定不同的Support Feature模板。Support Feature模板的配置命令参见ADD SUPFEATURE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter局向路由的别名，便于识别和记忆。
ROUTEID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示本Diameter局向路由中diameter路由组的标识。
ROUTELEVEL|Diameter路由组级别|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|该参数用于指示Diameter局向路由中路由组的优先级别，数值越低优先级越高。
ROUTEWEIGHT|Diameter路由组权重|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指示Diameter局向路由中路由组的权重值。






命令举例 


新增一条Diameter局向路由数据，设置Diameter局向路由ID为2、diameter路由组ID为2，Diameter路由组级别1，Diameter路由组权重1，域名为test。 


ADD DIAMADJROUTE:ADJROUTEID=2,ROUTEGROUP=2-1-1,REALM="test"; 








父主题： [Diameter局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter局向路由配置(SET DIAMADJROUTE) 
#### 修改Diameter局向路由配置(SET DIAMADJROUTE) 


命令功能 

该命令用于修改一个已经存在的Diameter局向路由，当需要修改本Diameter局向路由中Diameter路由组的构成或者改变本Diameter局向路由内Diameter路由组的分担方式和权重时，使用该命令。Diameter局向路由为一个或多个Diameter路由组的集合，当一个或两个Diameter路由组属于同一个Diameter局向路由时，可以从逻辑上维护该组Diameter路由组。


注意事项 



 
一个Diameter局向路由中最多包含16个Diameter路由组。
 

 
配置Diameter局向路由前，需要先配置Diameter路由组数据，配置命令参见ADD DIAMROUTEGROUP。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ADJROUTEID|局向路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指示Diameter局向路由标识号，需全局唯一。
ROUTEGROUP|Diameter路由组|参数可选性:任选参数；参数类型:复合参数|该参数用于指示本Diameter局向路由包含的Diameter路由组信息，由路由组ID、路由组优先级、路由组权重三个参数组成，其中路由组ID由命令ADD DIAMROUTEGROUP配置。1个Diameter局向路由中最多包含16个Diameter路由组。
DEFAULT|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示该局向路由是否作为默认局向路由。所谓默认局向路由，就是当没有配置指示局向路由用于寻址时，使用该默认局向路由进行寻址。
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数指示默认局向路由AVP Profile标识。
ADJREALM|是否启用局向域名|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示该局向路由是否启用局向域名。如果选择“是”，则业务消息中的主机名和域名使用本局向路由中的“域名”和“主机名”。如果选择“否”，则业务消息使用Diameter连接中配置的主机名和域名，Diameter连接配置数据查询参见SHOW DIAMCONN。
REALM|域名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|该参数指示本局向路由的域名，当配置启用局向域名时，必须配置。
HOSTNAME|主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|该参数指示本局向路由的主机名，当配置启用局向域名时，必须配置。
SUPFEATUREID|Feature ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|该参数用于指示默认HSS局向路由关联的Support Feature模板。不同的局向路由可以指定不同的Support Feature模板。Support Feature模板的配置命令参见ADD SUPFEATURE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter局向路由的别名，便于识别和记忆。
ROUTEID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示本Diameter局向路由中diameter路由组的标识。
ROUTELEVEL|Diameter路由组级别|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|该参数用于指示Diameter局向路由中路由组的优先级别，数值越低优先级越高。
ROUTEWEIGHT|Diameter路由组权重|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指示Diameter局向路由中路由组的权重值。






命令举例 


修改局向路由ID为2的Diameter局向路由数据，将Diameter路由组的级别和权重修改为2。 


SET DIAMADJROUTE:ADJROUTEID=2,ROUTEGROUP=2-2-2; 








父主题： [Diameter局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 增加Diameter路由组信息（局向路由中）(ADD ROUTEGROUP LEVANDWGT) 
#### 增加Diameter路由组信息（局向路由中）(ADD ROUTEGROUP LEVANDWGT) 


命令功能 

该命令用于在已存在的局向路由中增加Diameter路由组信息，当需要将一个Diameter路由组添加到某个已存在的Diameter局向路由中时，使用该命令。


注意事项 

一个Diameter局向路由中最多包含16个Diameter路由组。


参数说明 


标识|名称|类型|说明
---|---|---|---
ADJROUTEID|局向路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指示Diameter局向路由标识号，需全局唯一。
ROUTEID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示本Diameter局向路由中diameter路由组的标识。
ROUTELEVEL|Diameter路由组级别|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|该参数用于指示Diameter局向路由中路由组的优先级别，数值越低优先级越高。
ROUTEWEIGHT|Diameter路由组权重|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指示Diameter局向路由中路由组的权重值。






命令举例 


在ID为2的Diameter局向路由中增加路由组信息，其中Diameter路由组ID为3，Diameter路由组级别3，diameter路由组权重3。 


ADD ROUTEGROUP LEVANDWGT:ADJROUTEID=2,ROUTEID=3,ROUTELEVEL=3,ROUTEWEIGHT=3; 








父主题： [Diameter局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter路由组信息（局向路由中）(SET ROUTEGROUP LEVANDWGT) 
#### 修改Diameter路由组信息（局向路由中）(SET ROUTEGROUP LEVANDWGT) 


命令功能 

该命令用于修改局向路由中已经存在的Diameter路由组信息，当需要修改某个Diameter路由组的优先级或者权重时，使用该命令。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
ADJROUTEID|局向路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指示Diameter局向路由标识号，需全局唯一。
ROUTEID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示本Diameter局向路由中diameter路由组的标识。
ROUTELEVEL|Diameter路由组级别|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数用于指示Diameter局向路由中路由组的优先级别，数值越低优先级越高。
ROUTEWEIGHT|Diameter路由组权重|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指示Diameter局向路由中路由组的权重值。






命令举例 


修改Diameter局向路由ID为2的路由组信息，将diameter路由组ID为3的级别和权重分别修改为4。 


SET ROUTEGROUP LEVANDWGT:ADJROUTEID=2,ROUTEID=3,ROUTELEVEL=4,ROUTEWEIGHT=4; 








父主题： [Diameter局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter路由组信息（局向路由中）(DEL ROUTEGROUP LEVANDWGT) 
#### 删除Diameter路由组信息（局向路由中）(DEL ROUTEGROUP LEVANDWGT) 


命令功能 

该命令用于从局向路由中删除已经存在的Diameter路由组，根据局向路由ID和Diameter路由组ID共同索引。当需要删除某个Diameter路由组时，使用该命令。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
ADJROUTEID|局向路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指示Diameter局向路由标识号，需全局唯一。
ROUTEID|Diameter路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示本Diameter局向路由中diameter路由组的标识。






命令举例 


删除局向路由中的Diameter路由组信息，其中Diameter局向路由ID为2，Diameter路由组ID为3。 


DEL ROUTEGROUP LEVANDWGT:ADJROUTEID=2,ROUTEID=3; 








父主题： [Diameter局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter局向路由配置(DEL DIAMADJROUTE) 
#### 删除Diameter局向路由配置(DEL DIAMADJROUTE) 


命令功能 

该命令用于删除一个已经存在的Diameter局向路由。Diameter局向路由为一个或多个Diameter路由组的集合，当一个或两个Diameter路由组属于同一个Diameter局向路由时，可以从逻辑上维护该组Diameter路由组。


注意事项 

删除前，需要先将该Diameter局向路由在Diameter局向配置中去关联，Diameter局向配置数据查询参见[SHOW DIAMADJ]。


参数说明 


标识|名称|类型|说明
---|---|---|---
ADJROUTEID|局向路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指示Diameter局向路由标识号，需全局唯一。






命令举例 


删除局向路由ID为1的Diameter局向路由数据。 


DEL DIAMADJROUTE:ADJROUTEID=1; 








父主题： [Diameter局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter局向路由配置(SHOW DIAMADJROUTE) 
#### 查询Diameter局向路由配置(SHOW DIAMADJROUTE) 


命令功能 

该命令用于查询Diameter局向路由配置。Diameter局向路由为一个或多个Diameter路由组的集合，当一个或两个Diameter路由组属于同一个Diameter局向路由时，可以从逻辑上维护该组Diameter路由组。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
ADJROUTEID|局向路由ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指示Diameter局向路由标识号，需全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ADJROUTEID|局向路由ID|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由标识号，需全局唯一。
DEFAULT|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示该局向路由是否作为默认局向路由。所谓默认局向路由，就是当没有配置指示局向路由用于寻址时，使用该默认局向路由进行寻址。
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数。|该参数指示默认局向路由AVP Profile标识。
ADJREALM|是否启用局向域名|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数指示该局向路由是否启用局向域名。如果选择“是”，则业务消息中的主机名和域名使用本局向路由中的“域名”和“主机名”。如果选择“否”，则业务消息使用Diameter连接中配置的主机名和域名，Diameter连接配置数据查询参见SHOW DIAMCONN。
REALM|域名|参数可选性:任选参数；参数类型:字符型。|该参数指示本局向路由的域名，当配置启用局向域名时，必须配置。
HOSTNAME|主机名|参数可选性:任选参数；参数类型:字符型。|该参数指示本局向路由的主机名，当配置启用局向域名时，必须配置。
SUPFEATUREID|Feature ID|参数可选性:任选参数；参数类型:整数。|该参数用于指示默认HSS局向路由关联的Support Feature模板。不同的局向路由可以指定不同的Support Feature模板。Support Feature模板的配置命令参见ADD SUPFEATURE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型。|该Diameter局向路由的别名，便于识别和记忆。
ROUTEID1|Diameter路由组ID1|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中diameter路由组1的标识。
ROUTELEVEL1|Diameter路由组级别1|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组1的优先级别，数值越低优先级越高。
ROUTEWEIGHT1|Diameter路由组权重1|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组1的权重值。
ROUTEID2|Diameter路由组ID2|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中diameter路由组2的标识。
ROUTELEVEL2|Diameter路由组级别2|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组2的优先级别，数值越低优先级越高。
ROUTEWEIGHT2|Diameter路由组权重2|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组2的权重值。
ROUTEID3|Diameter路由组ID3|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中diameter路由组3的标识。
ROUTELEVEL3|Diameter路由组级别3|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组3的优先级别，数值越低优先级越高。
ROUTEWEIGHT3|Diameter路由组权重3|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组3的权重值。
ROUTEID4|Diameter路由组ID4|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中diameter路由组4的标识。
ROUTELEVEL4|Diameter路由组级别4|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组4的优先级别，数值越低优先级越高。
ROUTEWEIGHT4|Diameter路由组权重4|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组4的权重值。
ROUTEID5|Diameter路由组ID5|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中diameter路由组5的标识。
ROUTELEVEL5|Diameter路由组级别5|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组5的优先级别，数值越低优先级越高。
ROUTEWEIGHT5|Diameter路由组权重5|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组5的权重值。
ROUTEID6|Diameter路由组ID6|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中diameter路由组6的标识。
ROUTELEVEL6|Diameter路由组级别6|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组6的优先级别，数值越低优先级越高。
ROUTEWEIGHT6|Diameter路由组权重6|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组6的权重值。
ROUTEID7|Diameter路由组ID7|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组7的标识。
ROUTELEVEL7|Diameter路由组级别7|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组7的优先级别，数值越低优先级越高。
ROUTEWEIGHT7|Diameter路由组权重7|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组7的权重值。
ROUTEID8|Diameter路由组ID8|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组8的标识。
ROUTELEVEL8|Diameter路由组级别8|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组8的优先级别，数值越低优先级越高。
ROUTEWEIGHT8|Diameter路由组权重8|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组8的权重值。
ROUTEID9|Diameter路由组ID9|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组9的标识。
ROUTELEVEL9|Diameter路由组级别9|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组9的优先级别，数值越低优先级越高。
ROUTEWEIGHT9|Diameter路由组权重9|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组9的权重值。
ROUTEID10|Diameter路由组ID10|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组10的标识。
ROUTELEVEL10|Diameter路由组级别10|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组10的优先级别，数值越低优先级越高。
ROUTEWEIGHT10|Diameter路由组权重10|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组10的权重值。
ROUTEID11|Diameter路由组ID11|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组11的标识。
ROUTELEVEL11|Diameter路由组级别11|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组11的优先级别，数值越低优先级越高。
ROUTEWEIGHT11|Diameter路由组权重11|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组11的权重值。
ROUTEID12|Diameter路由组ID12|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组12的标识。
ROUTELEVEL12|Diameter路由组级别12|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组12的优先级别，数值越低优先级越高。
ROUTEWEIGHT12|Diameter路由组权重12|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组12的权重值。
ROUTEID13|Diameter路由组ID13|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组13的标识。
ROUTELEVEL13|Diameter路由组级别13|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组13的优先级别，数值越低优先级越高。
ROUTEWEIGHT13|Diameter路由组权重13|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组13的权重值。
ROUTEID14|Diameter路由组ID14|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组14的标识。
ROUTELEVEL14|Diameter路由组级别14|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组14的优先级别，数值越低优先级越高。
ROUTEWEIGHT14|Diameter路由组权重14|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组14的权重值。
ROUTEID15|Diameter路由组ID15|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组15的标识。
ROUTELEVEL15|Diameter路由组级别15|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组15的优先级别，数值越低优先级越高。
ROUTEWEIGHT15|Diameter路由组权重15|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组15的权重值。
ROUTEID16|Diameter路由组ID16|参数可选性:任选参数；参数类型:整数。|该参数用于指示本Diameter局向路由中diameter路由组16的标识。
ROUTELEVEL16|Diameter路由组级别16|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组16的优先级别，数值越低优先级越高。
ROUTEWEIGHT16|Diameter路由组权重16|参数可选性:任选参数；参数类型:整数。|该参数用于指示Diameter局向路由中路由组16的权重值。






命令举例 


查询所有的Diameter局向路由数据。 


SHOW DIAMADJROUTE 


`

命令 (No.20): SHOW DIAMADJROUTE

操作维护         局向路由ID   是否默认局向路由   默认局向路由AVP Profile标识   是否启用局向域名   域名   主机名   Feature ID   用户别名   Diameter路由组ID1   Diameter路由组级别1   Diameter路由组权重1   Diameter路由组ID2   Diameter路由组级别2   Diameter路由组权重2   Diameter路由组ID3   Diameter路由组级别3   Diameter路由组权重3   Diameter路由组ID4   Diameter路由组级别4   Diameter路由组权重4   Diameter路由组ID5   Diameter路由组级别5   Diameter路由组权重5   Diameter路由组ID6   Diameter路由组级别6   Diameter路由组权重6   Diameter路由组ID7   Diameter路由组级别7   Diameter路由组权重7   Diameter路由组ID8   Diameter路由组级别8   Diameter路由组权重8   Diameter路由组ID9   Diameter路由组级别9   Diameter路由组权重9   Diameter路由组ID10   Diameter路由组级别10   Diameter路由组权重10   Diameter路由组ID11   Diameter路由组级别11   Diameter路由组权重11   Diameter路由组ID12   Diameter路由组级别12   Diameter路由组权重12   Diameter路由组ID13   Diameter路由组级别13   Diameter路由组权重13   Diameter路由组ID14   Diameter路由组级别14   Diameter路由组权重14   Diameter路由组ID15   Diameter路由组级别15   Diameter路由组权重15   Diameter路由组ID16   Diameter路由组级别16   Diameter路由组权重16
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   2            否                 0                             是                 test            0                       2                   2                     2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.053 秒）。

` 








父主题： [Diameter局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter局向配置 
### Diameter局向配置 


背景知识 


MME与HSS（Home Subscriber Server，归属用户服务器）网元之间的S6a接口使用Diameter协议，MME和HSS间可以直连发送消息，也可以通过DRA（Diameter Route Agent，路由代理节点）设备中转Diameter消息发送到HSS。 




功能描述 


“Diameter局向配置”为MME设置关联的Diameter局向路由，这些Diameter局向可能是HSS，也可能是DRA网元。 


配置后，MME在对用户的IMSI进行号码分析，得到Diameter局向后，通过此处设置的局向路由，向用户归属的HSS发送消息。 



                Diameter局向上的消息遵循3GPP协议版本（R8、R9或R10），如果需要对Diameter消息进行编辑，可以配置局向消息的AVP编辑Profile ID，通过此Profile ID在“Diameter AVP Profile配置（命令为：
                [ADD DIM AVP PROFILE]
                ）”中获得具体的AVP字段编辑策略，此处策略只能修改S6a的Diameter消息，如果要对Diameter链路管理消息（例如CER或DWR消息）进行编辑，需要在Diameter路由中配置，配置命令为
                [ADD DIAMROUTE]
                。
            



                配置Diameter局向前，需要先配置Diameter局向路由数据，配置命令为
                [ADD DIAMADJROUTE]
                。
            




相关主题 



 

新增Diameter局向配置(ADD DIAMADJ)
 

 

修改Diameter局向配置(SET DIAMADJ)
 

 

删除Diameter局向配置(DEL DIAMADJ)
 

 

查询Diameter局向配置(SHOW DIAMADJ)
 

 








父主题： [Diameter连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter局向配置(ADD DIAMADJ) 
#### 新增Diameter局向配置(ADD DIAMADJ) 


命令功能 

该命令用于新增一个Diameter局向，当需要将一个或多个Diameter局向路由添加到某Diameter局向中时，使用该命令。新增Diameter局向成功后，可以从逻辑上维护一组Diameter局向路由。


注意事项 



 
一个Diameter局向中最多包含两个Diameter局向路由。
 

 
配置Diameter局向前，需要先配置Diameter局向路由数据，配置命令参见ADD DIAMADJROUTE。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ADJID|Diameter局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向标识号，需全局唯一。
ADJROUTEID|Diameter局向路由|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|Diamerter局向路由标识。该参数用于指定本Diameter局向包含的Diameter局向路由，1个Diameter局向路由中最多包含2个Diameter路由组。其中分担方式为主备方式，且前一个路由组为主用，后一个为备用。
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。默认值:0。|该参数用于S6a口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
PROVERSION|协议版本号|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:R8。|该参数用于指定对端局向支持的协议版本号，取值如下：R8R9R10R11说明：对于有些字段只有高版本的协议才支持。如Update-Location-Request消息中的Active-APN字段在R9版本协议才支持。具体可以参见协议3GPP TS 29.272。
SUPFEATUREID|Feature ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。默认值:0。|该参数用于指示此HSS局向关联的Support Feature模板。不同的局向可以指定不同的Support Feature模板。Support Feature模板的配置命令参见ADD SUPFEATURE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter局向的别名，便于识别和记忆。






命令举例 


新增一条Diameter局向数据，设置Diameter局向ID为1、Diamerter局向路由ID为1，其他参数按默认配置。
ADD DIAMADJ:ADJID=1,ADJROUTEID=1; 








父主题： [Diameter局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter局向配置(SET DIAMADJ) 
#### 修改Diameter局向配置(SET DIAMADJ) 


命令功能 

该命令用于修改一个已经存在的Diameter局向，当需要修改该Diameter局向中Diameter局向路由的构成时，使用该命令。Diameter局向为一个或两个Diameter局向路由的集合，当一个或两个Diameter局向路由属于同一个Diameter局向时，可以从逻辑上维护该组Diameter局向路由。


注意事项 



 
一个Diameter局向中最多包含两个Diameter局向路由。
 

 
配置Diameter局向前，需要先配置Diameter局向路由数据，配置命令参见ADD DIAMADJROUTE。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ADJID|Diameter局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向标识号，需全局唯一。
ADJROUTEID|Diameter局向路由|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|Diamerter局向路由标识。该参数用于指定本Diameter局向包含的Diameter局向路由，1个Diameter局向路由中最多包含2个Diameter路由组。其中分担方式为主备方式，且前一个路由组为主用，后一个为备用。
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于S6a口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
PROVERSION|协议版本号|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定对端局向支持的协议版本号，取值如下：R8R9R10R11说明：对于有些字段只有高版本的协议才支持。如Update-Location-Request消息中的Active-APN字段在R9版本协议才支持。具体可以参见协议3GPP TS 29.272。
SUPFEATUREID|Feature ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|该参数用于指示此HSS局向关联的Support Feature模板。不同的局向可以指定不同的Support Feature模板。Support Feature模板的配置命令参见ADD SUPFEATURE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter局向的别名，便于识别和记忆。






命令举例 


修改局向ID为1的Diameter局向数据，将Diamerter局向路由ID修改为2。
SET DIAMADJ:ADJID=1,ADJROUTEID=2; 








父主题： [Diameter局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter局向配置(DEL DIAMADJ) 
#### 删除Diameter局向配置(DEL DIAMADJ) 


命令功能 

该命令用于删除一个已经存在的Diameter局向。Diameter局向为一个或两个Diameter局向路由的集合，当一个或两个Diameter局向路由属于同一个Diameter局向时，可以从逻辑上维护该组Diameter局向路由。


注意事项 

删除前，需要先将该Diameter局向在Diameter邻接局号码分析结果配置中去关联，Diameter邻接局号码分析结果配置数据查询参见[SHOW DIMOFC ANALYSIS]。


参数说明 


标识|名称|类型|说明
---|---|---|---
ADJID|Diameter局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向标识号，需全局唯一。






命令举例 


删除局向ID为1的Diameter局向数据。
DEL DIAMADJ:ADJID=1; 








父主题： [Diameter局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter局向配置(SHOW DIAMADJ) 
#### 查询Diameter局向配置(SHOW DIAMADJ) 


命令功能 

该命令用于查询Diameter局向配置。Diameter局向为一个或两个Diameter局向路由的集合，当一个或两个Diameter局向路由属于同一个Diameter局向时，可以从逻辑上维护该组Diameter局向路由。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
ADJID|Diameter局向号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向标识号，需全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ADJID|Diameter局向号|参数可选性:任选参数；参数类型:整数。|该参数用于指定Diameter局向标识号，需全局唯一。
ADJROUTEID1|Diameter局向路由1|参数可选性:任选参数；参数类型:整数。|Diameter局向路由1
ADJROUTEID2|Diameter局向路由2|参数可选性:任选参数；参数类型:整数。|Diameter局向路由2
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数。|该参数用于S6a口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
PROVERSION|协议版本号|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定对端局向支持的协议版本号，取值如下：R8R9R10R11说明：对于有些字段只有高版本的协议才支持。如Update-Location-Request消息中的Active-APN字段在R9版本协议才支持。具体可以参见协议3GPP TS 29.272。
SUPFEATUREID|Feature ID|参数可选性:任选参数；参数类型:整数。|该参数用于指示此HSS局向关联的Support Feature模板。不同的局向可以指定不同的Support Feature模板。Support Feature模板的配置命令参见ADD SUPFEATURE。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型。|该Diameter局向的别名，便于识别和记忆。






命令举例 


查询所有的Diameter局向数据。 


SHOW DIAMADJ; 


`

命令 (No.1): SHOW DIAMADJ

操作维护         Diameter局向号   Diameter局向路由1   Diameter局向路由2   AVP Profile标识   用户别名   协议版本号  Feature ID
-----------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   22               22                                      0                            R8          2
-----------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.033 秒）。


` 








父主题： [Diameter局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter EIR 配置 
### Diameter EIR 配置 


背景知识 


EIR即设备标识寄存器（Equipment Identity Register），MME与EIR网元之间的S13接口使用Diameter协议。 




功能描述 


通过Diameter EIR配置，可以为MME配置EIR网元的局向ID，MME最大支持配置一个EIR局向，MME向EIR发送消息时，根据配置的局向ID，获得关联的Diameter局向路由。 




相关主题 



 

新增Diameter EIR配置(ADD DIAMEIR)
 

 

删除Diameter EIR配置(DEL DIAMEIR)
 

 

查询Diameter EIR配置(SHOW DIAMEIR)
 

 








父主题： [Diameter连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter EIR配置(ADD DIAMEIR) 
#### 新增Diameter EIR配置(ADD DIAMEIR) 


命令功能 

该命令用于在网元侧创建Diameter EIR，当需要本端网元与EIR进行业务交互时，使用该命令。新增成功后，本端网元与EIR之间可以进行S13口业务。


注意事项 



 
本网元最多只能关联一个EIR。
 

 
配置EIR局向前，需要先配置Diameter局向数据，配置命令参见ADD DIAMADJ。
 

 


说明：可以将EIR局向看作是一个特殊的Diameter局向。 




参数说明 


标识|名称|类型|说明
---|---|---|---
GRPID|Diameter局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向标识号，需全局唯一，且该参数引用自Diameter 局向配置数据，可以使用命令SHOW DIAMADJ查看。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该Diameter EIR局向的别名，便于识别和记忆。






命令举例 


新增一条Diameter EIR数据，设置Diameter局向ID为1。
ADD DIAMEIR:GRPID=1; 








父主题： [Diameter EIR 配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter EIR配置(DEL DIAMEIR) 
#### 删除Diameter EIR配置(DEL DIAMEIR) 


命令功能 

该命令用于删除EIR配置。EIR是一个特殊的Diameter局向，与本网元进行S13口互通。


注意事项 

删除之后将无法进行S13口业务。


参数说明 


标识|名称|类型|说明
---|---|---|---
GRPID|Diameter局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向标识号，需全局唯一，且该参数引用自Diameter 局向配置数据，可以使用命令SHOW DIAMADJ查看。






命令举例 


删除Diameter局向ID为1的Diameter EIR配置数据。
DEL DIAMEIR:GRPID=1; 








父主题： [Diameter EIR 配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter EIR配置(SHOW DIAMEIR) 
#### 查询Diameter EIR配置(SHOW DIAMEIR) 


命令功能 

该命令用于查询EIR配置。EIR是一个特殊的Diameter局向，与本网元进行S13口互通。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
GRPID|Diameter局向ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向标识号，需全局唯一，且该参数引用自Diameter 局向配置数据，可以使用命令SHOW DIAMADJ查看。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
GRPID|Diameter局向ID|参数可选性:任选参数；参数类型:整数。|该参数用于指定Diameter局向标识号，需全局唯一，且该参数引用自Diameter 局向配置数据，可以使用命令SHOW DIAMADJ查看。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型。|该Diameter EIR局向的别名，便于识别和记忆。






命令举例 


查询所有的Diameter EIR配置数据。
SHOW DIAMEIR; 


`

命令 (No.1): SHOW DIAMEIR

操作维护    Diameter局向ID   用户别名
-------------------------------------
复制 删除   22               
-------------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。


` 








父主题： [Diameter EIR 配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Diameter GMLC配置 
## Diameter GMLC配置 


背景知识 


GMLC网元用于LTE网络中LCS定位功能，MME与GMLC网元之间的SLg接口使用Diameter协议。 




功能描述 


MME向GMLC发送消息，，获取路由过程如下： 







                        分析GMLC网元标识号码，获取用户归属的GMLC局向ID，对应的配置命令为：
                        [ADD MDNAL]
                        和
                        [ADD DIMGMLC ANALYSIS]
                        。
                    







                        根据GMLC局向ID，获取到Diameter GMLC局向路由，对应的配置命令：
                        [ADD DIAMGMLCADJ]
                        。
                    







                        根据Diameter GMLC局向路由ID查询到Diameter路由组， 对应的配置命令为：
                        [ADD DIAMGMLCROUTE]
                        。
                    







                        根据Diameter路由组ID查询到Diameter路由， 对应的配置命令为：
                        [ADD DIAMGMLCROUTE]
                        。
                    







                        根据Diameter路由ID查询到Diamete链路组， 对应的配置命令为：
                        [ADD DIAMROUTE]
                        。
                    







                        根据Diameter链路组ID查询到SCTP连接标识， 对应的配置命令为：
                        [ADD DIAMLINKGROUP]
                        。其中，SCTP连接标识已经在Diameter偶联中配置，对应的配置命令为：
                        [ADD SCTP]
                        。
                    








相关主题 



 

Diameter GMLC局向路由配置
 

 

Diameter GMLC局向配置
 

 








父主题： [Diameter配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter GMLC局向路由配置 
### Diameter GMLC局向路由配置 


背景知识 


MME向GMLC发送消息，路由逻辑是首先基于GMLC号码分析得到局向ID，局向ID得到局向路由，后面逻辑是局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路。 




功能描述 


通过Diameter GMLC局向路由配置，可以配置局向路由下包含的多个路由组，其中选择为主备或负荷分担模式。 


配置在此局向路由发送消息时，消息的目的域名和目的主机名。 


此配置中的路由组ID，在“Diameter路由组配置”中查找包含的Diameter路由。 




相关主题 



 

新增Diameter GMLC局向路由配置(ADD DIAMGMLCROUTE)
 

 

修改Diameter GMLC局向路由配置(SET DIAMGMLCROUTE)
 

 

删除Diameter GMLC局向路由配置(DEL DIAMGMLCROUTE)
 

 

查询Diameter GMLC局向路由配置(SHOW DIAMGMLCROUTE)
 

 








父主题： [Diameter GMLC配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter GMLC局向路由配置(ADD DIAMGMLCROUTE) 
#### 新增Diameter GMLC局向路由配置(ADD DIAMGMLCROUTE) 


命令功能 


该命令用于新增Diameter GMLC局向路由配置，当需要与GMLC对接时，使用该命令。Diameter GMLC局向路由配置完成后，可以进一步配置Diameter GMLC局向以完成GMLC号码分析配置。 


命令中的域名、主机名参数需要填写为对端GMLC的域名和主机名。 


在配置GMLC邻接局号码分析时需要先使用该命令。 




注意事项 



 
该命令执行前，需要先配置Diameter路由组。 配置命令参见ADD DIAMROUTEGROUP。
 

 
系统中最多只有一条默认Diameter GMLC局向路由；每个Diameter GMLC局向路由最多可以关联四个Diameter路由组

 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCROUTEID|局向路由标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter GMLC局向路由，该参数要求全局唯一。
ROUTEGROUP|Diameter路由组标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示该Diameter GMLC局向路由关联的路由组。执行SHOW DIAMROUTEGROUP命令查询已配置的Diameter路由组。一条Diameter GMLC局向路由最多关联四个Diameter路由组。
PROPERTY|路由属性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter GMLC局向路由的负荷分担属性。取值含义如下所示。“BACKUP”：该Diameter GMLC局向路由工作方式是主备方式 。“PARTAKE”：该Diameter GMLC局向路由工作方式是负荷分担方式。
DFTROUTE|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数表明该Diameter GMLC局向路由是否为默认。取值含义如下所示。“YES”：当GMLC号码分析匹配不到时可以选择该Diameter GMLC局向路由进行消息发送。“NO”：该Diameter GMLC局向路由非默认GMLC局向路由。 只能配置一条默认Diameter GMLC局向路由.
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。默认值:0。|该参数用于SLg口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
REALM|域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|配置的对端GMLC的域名。
HOSTNAME|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|配置的对端GMLC的主机名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的Diameter GMLC局向路由的别名。






命令举例 


增加Diameter GMLC局向路由：局向路由标识为“1”，路由组标识为“1”，路由属性为“负荷分担”，是否默认局向路由为“否”，GMLC域名为“A”，GMLC主机名为“A”，别名为“SS”。
ADD DIAMGMLCROUTE:GMLCROUTEID=1,ROUTEGROUP=1,PROPERTY="PARTAKE",REALM="A",HOSTNAME="A",NAME="SS"; 








父主题： [Diameter GMLC局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter GMLC局向路由配置(SET DIAMGMLCROUTE) 
#### 修改Diameter GMLC局向路由配置(SET DIAMGMLCROUTE) 


命令功能 

该命令用于修改Diameter GMLC局向路由配置。执行该命令，可以修改Diameter GMLC局向路由关联的路由组、局向路由的属性、对端GMLC的主机名、域名等信息。


注意事项 

一条Diameter GMLC局向路由最多可以关联四个Diameter路由组。


参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCROUTEID|局向路由标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter GMLC局向路由，该参数要求全局唯一。
ROUTEGROUP|Diameter路由组标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示该Diameter GMLC局向路由关联的路由组。执行SHOW DIAMROUTEGROUP命令查询已配置的Diameter路由组。一条Diameter GMLC局向路由最多关联四个Diameter路由组。
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter GMLC局向路由的负荷分担属性。取值含义如下所示。“BACKUP”：该Diameter GMLC局向路由工作方式是主备方式 。“PARTAKE”：该Diameter GMLC局向路由工作方式是负荷分担方式。
DFTROUTE|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter GMLC局向路由是否为默认。取值含义如下所示。“YES”：当GMLC号码分析匹配不到时可以选择该Diameter GMLC局向路由进行消息发送。“NO”：该Diameter GMLC局向路由非默认GMLC局向路由。 只能配置一条默认Diameter GMLC局向路由.
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于SLg口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
REALM|域名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|配置的对端GMLC的域名。
HOSTNAME|主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|配置的对端GMLC的主机名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的Diameter GMLC局向路由的别名。






命令举例 


修改局向路由标识为“1”的Diameter GMLC局向路由：关联的路由组标识为“1”，路由属性为“负荷分担”，是否默认局向路由为“否”，GMLC域名为“A”，GMLC主机名为“A”，别名为“SS”。
SET DIAMGMLCROUTE:GMLCROUTEID=1,ROUTEGROUP=1,PROPERTY="PARTAKE",REALM="A",HOSTNAME="A",NAME="SS"; 








父主题： [Diameter GMLC局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter GMLC局向路由配置(DEL DIAMGMLCROUTE) 
#### 删除Diameter GMLC局向路由配置(DEL DIAMGMLCROUTE) 


命令功能 

该命令用于删除Diameter GMLC局向路由配置。


注意事项 

删除Diameter GMLC局向路由前需要确保该局向路由没有被任何Diameter GMLC局向关联，查询命令参见[SHOW DIAMGMLCADJ]。


参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCROUTEID|局向路由标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter GMLC局向路由，该参数要求全局唯一。






命令举例 


删除局向路由标识为“1”的Diameter GMLC局向路由。
DEL DIAMGMLCROUTE:GMLCROUTEID=1; 








父主题： [Diameter GMLC局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter GMLC局向路由配置(SHOW DIAMGMLCROUTE) 
#### 查询Diameter GMLC局向路由配置(SHOW DIAMGMLCROUTE) 


命令功能 

该命令用于查询Diameter GMLC局向路由配置，使用该命令可以显示该Diameter GMLC局向路由所关联的路由组、路由属性、对端GMLC的主机名、域名等信息。


注意事项 



 
该命令不带参数，可查询所有的Diameter GMLC局向路由配置记录。

 

 
该命令也可根据Diameter GMLC局向路由标识查询与之匹配的记录

 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCROUTEID|局向路由标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter GMLC局向路由，该参数要求全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCROUTEID|局向路由标识|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条Diameter GMLC局向路由，该参数要求全局唯一。
ROUTEGROUP1|Diameter路由组标识1|参数可选性:任选参数；参数类型:整数。|配置的Diameter GMLC局向路由关联的路由组，路由组必须已经存在，一条Diameter GMLC局向路由最多关联四个路由组。
ROUTEGROUP2|Diameter路由组标识2|参数可选性:任选参数；参数类型:整数。|同“Diameter路由组标识1”说明。
ROUTEGROUP3|Diameter路由组标识3|参数可选性:任选参数；参数类型:整数。|同“Diameter路由组标识1”说明。
ROUTEGROUP4|Diameter路由组标识4|参数可选性:任选参数；参数类型:整数。|同“Diameter路由组标识1”说明。
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter GMLC局向路由的负荷分担属性。取值含义如下所示。“BACKUP”：该Diameter GMLC局向路由工作方式是主备方式 。“PARTAKE”：该Diameter GMLC局向路由工作方式是负荷分担方式。
DFTROUTE|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter GMLC局向路由是否为默认。取值含义如下所示。“YES”：当GMLC号码分析匹配不到时可以选择该Diameter GMLC局向路由进行消息发送。“NO”：该Diameter GMLC局向路由非默认GMLC局向路由。 只能配置一条默认Diameter GMLC局向路由.
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数。|该参数用于SLg口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
REALM|域名|参数可选性:任选参数；参数类型:字符型。|配置的对端GMLC的域名。
HOSTNAME|主机名|参数可选性:任选参数；参数类型:字符型。|配置的对端GMLC的主机名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|配置的Diameter GMLC局向路由的别名。






命令举例 


查询所有Diameter GMLC局向路由信息。
SHOW DIAMGMLCROUTE 


`
命令 (No.1): SHOW DIAMGMLCROUTE

操作维护         局向路由标识   Diameter路由组标识1   Diameter路由组标识2   Diameter路由组标识3   Diameter路由组标识4   路由属性   是否默认局向路由   域名         主机名   用户别名
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   5              5                                                                                       负荷分担   否                 zte.com.cn   gmlc     SS
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.035 秒）。


` 








父主题： [Diameter GMLC局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter GMLC局向配置 
### Diameter GMLC局向配置 


背景知识 


MME与GMLC（Gateway Mobile Location Center，网关移动位置中心）网元之间的Slg接口使用Diameter协议，MME也可以通过DRA设备中转Diameter消息发送到GMLC。DRA（Diameter Route Agent）路由代理节点，负责Diameter消息的转发。 




功能描述 


“Diameter GMLC局向配置”为MME设置关联的Diameter GMLC局向路由，这些Diameter局向可能是GMLC，也可能是DRA网元。 


配置后，MME对GMLC网元的号码进行分析，得到Diameter局向后，通过此处设置的局向路由，向GMLC发送消息。 



                Diameter局向上的消息遵循3GPP协议版本（R8、R9或R10），如果需要对Diameter消息进行编辑，可以配置局向消息的AVP编辑Profile ID，通过此Profile ID在“Diameter AVP Profile配置（命令为：
                [ADD DIM AVP PROFILE]
                ）”中获得具体的AVP字段编辑策略，此处策略只能修改Slg的Diameter消息，如果要对Diameter链路管理消息（例如CER或DWR消息）进行编辑，需要在Diameter路由中配置，配置命令为
                [ADD DIAMROUTE]
                。
            



                配置Diameter局向前，需要先配置Diameter GMLC局向路由数据，配置命令为
                [ADD DIAMGMLCROUTE]
                。
            




相关主题 



 

新增Diameter GMLC局向配置(ADD DIAMGMLCADJ)
 

 

修改Diameter GMLC局向配置(SET DIAMGMLCADJ)
 

 

删除Diameter GMLC局向配置(DEL DIAMGMLCADJ)
 

 

查询Diameter GMLC局向配置(SHOW DIAMGMLCADJ)
 

 








父主题： [Diameter GMLC配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter GMLC局向配置(ADD DIAMGMLCADJ) 
#### 新增Diameter GMLC局向配置(ADD DIAMGMLCADJ) 


命令功能 


该命令用于新增Diameter GMLC局向配置，当需要与GMLC对接时，使用该命令。Diameter GMLC局向配置完成后，可以进一步配置Diameter GMLC分析结果索引以完成GMLC号码分析配置。 


在配置GMLC邻接局号码分析时需要先执行该命令。 




注意事项 



 
该命令执行前，需要先配置Diameter GMLC局向路由标识。 配置命令见 ADD DIAMGMLCROUTE。
 

 
每个Diameter GMLC局向最多可以关联2个Diameter GMLC局向路由
 

 
查询与Diameter GMLC局向配置相关的GMLC号码分析配置，命令参见SHOW DIMGMLC ANALYSIS和SHOW MDNAL
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCADJID|局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter GMLC局向，该参数要求全局唯一。
GMLCROUTEID|Diameter GMLC局向路由标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示该Diameter GMLC局向关联的Diameter GMLC局向路由。需要先配置Diameter GMLC局向路由。 查询命令参见 SHOW DIAMGMLCROUTE。一条Diameter GMLC局向最多关联两个Diameter GMLC局向路由。
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。默认值:0。|该参数用于指示该Diameter GMLC局向关联的AVP Profile，AVP Profile用于控制Diameter消息中的某个AVP是否携带及AVP头中的相关标记位的值。默认值为”0“表明该Diameter GMLC局向不关联AVP Profile。如果要关联AVP Profile需要先配置AVP Profile。 配置命令参见 ADD DIM AVP PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的Diameter GMLC局向的别名。






命令举例 


增加Diameter GMLC局向：局向标识为“1”，关联的Diameter GMLC局向路由标识为“1”，关联的AVP Profile为“0”，别名为“SS”。
ADD DIAMGMLCADJ:GMLCADJID=1,GMLCROUTEID=1,NAME="SS"; 








父主题： [Diameter GMLC局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter GMLC局向配置(SET DIAMGMLCADJ) 
#### 修改Diameter GMLC局向配置(SET DIAMGMLCADJ) 


命令功能 

该命令用于修改Diameter GMLC局向配置，执行该命令，可以修改该Diameter GMLC局向关联的Diameter GMLC局向路由及关联的AVP Profile。


注意事项 

每个Diameter GMLC局向最多可以关联2个Diameter GMLC局向路由


参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCADJID|局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter GMLC局向，该参数要求全局唯一。
GMLCROUTEID|Diameter GMLC局向路由标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示该Diameter GMLC局向关联的Diameter GMLC局向路由。需要先配置Diameter GMLC局向路由。 查询命令参见 SHOW DIAMGMLCROUTE。一条Diameter GMLC局向最多关联两个Diameter GMLC局向路由。
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于指示该Diameter GMLC局向关联的AVP Profile，AVP Profile用于控制Diameter消息中的某个AVP是否携带及AVP头中的相关标记位的值。默认值为”0“表明该Diameter GMLC局向不关联AVP Profile。如果要关联AVP Profile需要先配置AVP Profile。 配置命令参见 ADD DIM AVP PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的Diameter GMLC局向的别名。






命令举例 


修改局向标识为“1”的Diameter GMLC局向：关联的Diameter GMLC局向路由标识为“1”，关联的AVP Profile为“0”，别名为“SS”。
SET DIAMGMLCADJ:GMLCADJID=1,GMLCROUTEID=1,AVPPROFILEID=0,NAME="SS"; 








父主题： [Diameter GMLC局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter GMLC局向配置(DEL DIAMGMLCADJ) 
#### 删除Diameter GMLC局向配置(DEL DIAMGMLCADJ) 


命令功能 

该命令用于删除Diameter GMLC局向配置。


注意事项 

删除Diameter GMLC局向时要确保该局向没有被Diameter GMLC号码分析结果索引所关联。参见[SHOW DIMGMLC ANALYSIS]。


参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCADJID|局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter GMLC局向，该参数要求全局唯一。






命令举例 


删除局向标识为“1”的Diameter GMLC局向。
DEL DIAMGMLCADJ:GMLCADJID=1; 








父主题： [Diameter GMLC局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter GMLC局向配置(SHOW DIAMGMLCADJ) 
#### 查询Diameter GMLC局向配置(SHOW DIAMGMLCADJ) 


命令功能 

该命令用于查询Diameter GMLC局向配置，使用该命令可以显示该Diameter GMLC局向关联的Diameter GMLC局向路由及AVP Profile信息。


注意事项 



 
该命令不带参数，可查询所有的Diameter GMLC局向配置记录。
 

 
该命令也可根据Diameter GMLC局向标识查询与之匹配的记录。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCADJID|局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter GMLC局向，该参数要求全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
GMLCADJID|局向标识|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条Diameter GMLC局向，该参数要求全局唯一。
GMLCROUTEID1|Diameter GMLC局向路由标识1|参数可选性:任选参数；参数类型:整数。|配置的Diameter GMLC局向关联的Diameter GMLC局向路由，Diameter GMLC局向路由必须已经存在。一条Diameter GMLC局向最多关联两个Diameter GMLC局向路由。Diameter GMLC局向路由标识2同此说明，不再详述。
GMLCROUTEID2|Diameter GMLC局向路由标识2|参数可选性:任选参数；参数类型:整数。|同“Diameter GMLC局向路由标识1”说明
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数。|该参数用于指示该Diameter GMLC局向关联的AVP Profile，AVP Profile用于控制Diameter消息中的某个AVP是否携带及AVP头中的相关标记位的值。默认值为”0“表明该Diameter GMLC局向不关联AVP Profile。如果要关联AVP Profile需要先配置AVP Profile。 配置命令参见 ADD DIM AVP PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|配置的Diameter GMLC局向的别名。






命令举例 


查询所有Diameter GMLC局向配置信息。
SHOW DIAMGMLCADJ; 


`
命令 (No.1): SHOW DIAMGMLCADJ

操作维护         局向标识   Diameter GMLC局向路由标识1   Diameter GMLC局向路由标识2   AVP Profile标识   用户别名
----------------------------------------------------------------------------------------------------------------
复制 修改 删除   5          5                                                         0                 SS
----------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。


` 








父主题： [Diameter GMLC局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Diameter SMC配置 
## Diameter SMC配置 


背景知识 


SMC网元用于LTE网络中LCS定位功能，MME与SMC网元之间的SLg接口使用Diameter协议。 




功能描述 


MME向SMC发送消息，，获取路由过程如下： 







                        分析SMC网元标识号码，获取用户归属的SMC局向ID，对应的配置命令为：
                        [ADD MDNAL]
                        和
                        [ADD DIMSMC ANALYSIS]
                        。
                    







                        根据SMC局向ID，获取到Diameter SMC局向路由，对应的配置命令：
                        [ADD DIAMSMCADJ]
                        。
                    







                        根据Diameter SMC局向路由ID查询到Diameter路由组， 对应的配置命令为：
                        [ADD DIAMSMCROUTE]
                        。
                    







                        根据Diameter路由组ID查询到Diameter路由， 对应的配置命令为：
                        [ADD DIAMSMCROUTE]
                        。
                    







                        根据Diameter路由ID查询到Diamete链路组， 对应的配置命令为：
                        [ADD DIAMROUTE]
                        。
                    







                        根据Diameter链路组ID查询到SCTP连接标识， 对应的配置命令为：
                        [ADD DIAMLINKGROUP]
                        。其中，SCTP连接标识已经在Diameter偶联中配置，对应的配置命令为：
                        [ADD SCTP]
                        。
                    








相关主题 



 

Diameter SMC局向路由配置
 

 

Diameter SMC局向配置
 

 








父主题： [Diameter配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter SMC局向路由配置 
### Diameter SMC局向路由配置 


背景知识 


MME向SMC发送消息，路由逻辑是首先基于SMC号码分析得到局向ID，局向ID得到局向路由，后面逻辑是局向路由-->Diameter路由组-->Diameter路由-->Diameter链路组-->Diameter链路。 




功能描述 


通过Diameter SMC局向路由配置，可以配置局向路由下包含的多个路由组，其中选择为主备或负荷分担模式。 


配置在此局向路由发送消息时，消息的目的域名和目的主机名。 


此配置中的路由组ID，在“Diameter路由组配置”中查找包含的Diameter路由。 




相关主题 



 

新增Diameter SMC局向路由配置(ADD DIAMSMCROUTE)
 

 

修改Diameter SMC局向路由配置(SET DIAMSMCROUTE)
 

 

删除Diameter SMC局向路由配置(DEL DIAMSMCROUTE)
 

 

查询Diameter SMC局向路由配置(SHOW DIAMSMCROUTE)
 

 








父主题： [Diameter SMC配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter SMC局向路由配置(ADD DIAMSMCROUTE) 
#### 新增Diameter SMC局向路由配置(ADD DIAMSMCROUTE) 


命令功能 


该命令用于新增Diameter SMC局向路由配置，当需要与SMC对接时，使用该命令。Diameter SMC局向路由配置完成后，可以进一步配置Diameter SMC局向以完成SMC号码分析配置。 


命令中的域名、主机名参数需要填写为对端SMC的域名和主机名。 


在配置SMC邻接局号码分析时需要先使用该命令。 




注意事项 



 
该命令执行前，需要先配置Diameter路由组。 配置命令参见ADD DIAMROUTEGROUP。
 

 
系统中最多只有一条默认Diameter SMC局向路由；每个Diameter SMC局向路由最多可以关联四个Diameter路由组

 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
SMCROUTEID|局向路由标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter SMC局向路由，该参数要求全局唯一。
ROUTEGROUP|Diameter路由组标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示该Diameter SMC局向路由关联的路由组。执行SHOW DIAMROUTEGROUP命令查询已配置的Diameter路由组。一条Diameter SMC局向路由最多关联四个Diameter路由组。
PROPERTY|路由属性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter SMC局向路由的负荷分担属性。取值含义如下所示。“BACKUP”：该Diameter SMC局向路由工作方式是主备方式 。“PARTAKE”：该Diameter SMC局向路由工作方式是负荷分担方式。
DFTROUTE|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数表明该Diameter SMC局向路由是否为默认。取值含义如下所示。“YES”：当SMC号码分析匹配不到时可以选择该Diameter SMC局向路由进行消息发送。“NO”：该Diameter SMC局向路由非默认SMC局向路由。 只能配置一条默认Diameter SMC局向路由.
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。默认值:0。|该参数用于SLg口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
REALM|域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|配置的对端SMC的域名。
HOSTNAME|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|配置的对端SMC的主机名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的Diameter SMC局向路由的别名。






命令举例 


增加Diameter SMC局向路由：局向路由标识为“1”，路由组标识为“1”，路由属性为“负荷分担”，是否默认局向路由为“否”，SMC域名为“A”，SMC主机名为“A”，别名为“SS”。 


ADD DIAMSMCROUTE:SMCROUTEID=1,ROUTEGROUP=1,PROPERTY="PARTAKE",REALM="A",HOSTNAME="A",NAME="SS"; 








父主题： [Diameter SMC局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter SMC局向路由配置(SET DIAMSMCROUTE) 
#### 修改Diameter SMC局向路由配置(SET DIAMSMCROUTE) 


命令功能 

该命令用于修改Diameter SMC局向路由配置。执行该命令，可以修改Diameter SMC局向路由关联的路由组、局向路由的属性、对端SMC的主机名、域名等信息。


注意事项 

一条Diameter SMC局向路由最多可以关联四个Diameter路由组。


参数说明 


标识|名称|类型|说明
---|---|---|---
SMCROUTEID|局向路由标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter SMC局向路由，该参数要求全局唯一。
ROUTEGROUP|Diameter路由组标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示该Diameter SMC局向路由关联的路由组。执行SHOW DIAMROUTEGROUP命令查询已配置的Diameter路由组。一条Diameter SMC局向路由最多关联四个Diameter路由组。
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter SMC局向路由的负荷分担属性。取值含义如下所示。“BACKUP”：该Diameter SMC局向路由工作方式是主备方式 。“PARTAKE”：该Diameter SMC局向路由工作方式是负荷分担方式。
DFTROUTE|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter SMC局向路由是否为默认。取值含义如下所示。“YES”：当SMC号码分析匹配不到时可以选择该Diameter SMC局向路由进行消息发送。“NO”：该Diameter SMC局向路由非默认SMC局向路由。 只能配置一条默认Diameter SMC局向路由.
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于SLg口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
REALM|域名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|配置的对端SMC的域名。
HOSTNAME|主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|配置的对端SMC的主机名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的Diameter SMC局向路由的别名。






命令举例 


修改局向路由标识为“1”的Diameter SMC局向路由：关联的路由组标识为“1”，路由属性为“负荷分担”，是否默认局向路由为“否”，SMC域名为“A”，SMC主机名为“A”，别名为“SS”。 


SET DIAMSMCROUTE:SMCROUTEID=1,ROUTEGROUP=1,PROPERTY="PARTAKE",REALM="A",HOSTNAME="A",NAME="SS"; 








父主题： [Diameter SMC局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter SMC局向路由配置(DEL DIAMSMCROUTE) 
#### 删除Diameter SMC局向路由配置(DEL DIAMSMCROUTE) 


命令功能 

该命令用于删除Diameter SMC局向路由配置。


注意事项 

删除Diameter SMC局向路由前需要确保该局向路由没有被任何Diameter SMC局向关联，查询命令参见[SHOW DIAMSMCADJ]。


参数说明 


标识|名称|类型|说明
---|---|---|---
SMCROUTEID|局向路由标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter SMC局向路由，该参数要求全局唯一。






命令举例 


删除局向路由标识为“1”的Diameter SMC局向路由。 


DEL DIAMSMCROUTE:SMCROUTEID=1; 








父主题： [Diameter SMC局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter SMC局向路由配置(SHOW DIAMSMCROUTE) 
#### 查询Diameter SMC局向路由配置(SHOW DIAMSMCROUTE) 


命令功能 

该命令用于查询Diameter SMC局向路由配置，使用该命令可以显示该Diameter SMC局向路由所关联的路由组、路由属性、对端SMC的主机名、域名等信息。


注意事项 



 
该命令不带参数，可查询所有的Diameter SMC局向路由配置记录。

 

 
该命令也可根据Diameter SMC局向路由标识查询与之匹配的记录

 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
SMCROUTEID|局向路由标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter SMC局向路由，该参数要求全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
SMCROUTEID|局向路由标识|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条Diameter SMC局向路由，该参数要求全局唯一。
ROUTEGROUP1|Diameter路由组标识1|参数可选性:任选参数；参数类型:整数。|配置的Diameter SMC局向路由关联的路由组，路由组必须已经存在，一条Diameter SMC局向路由最多关联四个路由组。
ROUTEGROUP2|Diameter路由组标识2|参数可选性:任选参数；参数类型:整数。|同“Diameter路由组标识1”说明。
ROUTEGROUP3|Diameter路由组标识3|参数可选性:任选参数；参数类型:整数。|同“Diameter路由组标识1”说明。
ROUTEGROUP4|Diameter路由组标识4|参数可选性:任选参数；参数类型:整数。|同“Diameter路由组标识1”说明。
PROPERTY|路由属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter SMC局向路由的负荷分担属性。取值含义如下所示。“BACKUP”：该Diameter SMC局向路由工作方式是主备方式 。“PARTAKE”：该Diameter SMC局向路由工作方式是负荷分担方式。
DFTROUTE|是否默认局向路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该Diameter SMC局向路由是否为默认。取值含义如下所示。“YES”：当SMC号码分析匹配不到时可以选择该Diameter SMC局向路由进行消息发送。“NO”：该Diameter SMC局向路由非默认SMC局向路由。 只能配置一条默认Diameter SMC局向路由.
AVPPROFILEID|默认局向路由AVP Profile标识|参数可选性:任选参数；参数类型:整数。|该参数用于SLg口消息的AVP控制所用，AVP控制策略查询参见SHOW DIM AVP PROFILE。
REALM|域名|参数可选性:任选参数；参数类型:字符型。|配置的对端SMC的域名。
HOSTNAME|主机名|参数可选性:任选参数；参数类型:字符型。|配置的对端SMC的主机名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|配置的Diameter SMC局向路由的别名。






命令举例 


查询所有Diameter SMC局向路由信息。 


SHOW DIAMSMCROUTE 


`
命令 (No.1): SHOW DIAMSMCROUTE

操作维护         局向路由标识   Diameter路由组标识1   Diameter路由组标识2   Diameter路由组标识3   Diameter路由组标识4   路由属性   是否默认局向路由   域名         主机名   用户别名
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   5              5                                                                                       负荷分担   否                 zte.com.cn   SMC     SS
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.035 秒）。


` 








父主题： [Diameter SMC局向路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### Diameter SMC局向配置 
### Diameter SMC局向配置 


背景知识 


MME与SMC（Gateway Mobile Location Center，网关移动位置中心）网元之间的Slg接口使用Diameter协议，MME也可以通过DRA设备中转Diameter消息发送到SMC。DRA（Diameter Route Agent）路由代理节点，负责Diameter消息的转发。 




功能描述 


“Diameter SMC局向配置”为MME设置关联的Diameter SMC局向路由，这些Diameter局向可能是SMC，也可能是DRA网元。 


配置后，MME对SMC网元的号码进行分析，得到Diameter局向后，通过此处设置的局向路由，向SMC发送消息。 



                Diameter局向上的消息遵循3GPP协议版本（R8、R9或R10），如果需要对Diameter消息进行编辑，可以配置局向消息的AVP编辑Profile ID，通过此Profile ID在“Diameter AVP Profile配置（命令为：
                [ADD DIM AVP PROFILE]
                ）”中获得具体的AVP字段编辑策略，此处策略只能修改Slg的Diameter消息，如果要对Diameter链路管理消息（例如CER或DWR消息）进行编辑，需要在Diameter路由中配置，配置命令为
                [ADD DIAMROUTE]
                。
            



                配置Diameter局向前，需要先配置Diameter SMC局向路由数据，配置命令为
                [ADD DIAMSMCROUTE]
                。
            




相关主题 



 

新增Diameter SMC局向配置(ADD DIAMSMCADJ)
 

 

修改Diameter SMC局向配置(SET DIAMSMCADJ)
 

 

删除Diameter SMC局向配置(DEL DIAMSMCADJ)
 

 

查询Diameter SMC局向配置(SHOW DIAMSMCADJ)
 

 








父主题： [Diameter SMC配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增Diameter SMC局向配置(ADD DIAMSMCADJ) 
#### 新增Diameter SMC局向配置(ADD DIAMSMCADJ) 


命令功能 


该命令用于新增Diameter SMC局向配置，当需要与SMC对接时，使用该命令。Diameter SMC局向配置完成后，可以进一步配置Diameter SMC分析结果索引以完成SMC号码分析配置。 


在配置SMC邻接局号码分析时需要先执行该命令。 




注意事项 



 
该命令执行前，需要先配置Diameter SMC局向路由标识。 配置命令见 ADD DIAMSMCROUTE。
 

 
每个Diameter SMC局向最多可以关联2个Diameter SMC局向路由
 

 
查询与Diameter SMC局向配置相关的SMC号码分析配置，命令参见SHOW DIMSMC ANALYSIS和SHOW MDNAL
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
SMCADJID|局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter SMC局向，该参数要求全局唯一。
SMCROUTEID|Diameter SMC局向路由标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示该Diameter SMC局向关联的Diameter SMC局向路由。需要先配置Diameter SMC局向路由。 查询命令参见 SHOW DIAMSMCROUTE。一条Diameter SMC局向最多关联两个Diameter SMC局向路由。
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。默认值:0。|该参数用于指示该Diameter SMC局向关联的AVP Profile，AVP Profile用于控制Diameter消息中的某个AVP是否携带及AVP头中的相关标记位的值。默认值为”0“表明该Diameter SMC局向不关联AVP Profile。如果要关联AVP Profile需要先配置AVP Profile。 配置命令参见 ADD DIM AVP PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的Diameter SMC局向的别名。






命令举例 


增加Diameter SMC局向：局向标识为“1”，关联的Diameter SMC局向路由标识为“1”，关联的AVP Profile为“0”，别名为“SS”。 


ADD DIAMSMCADJ:SMCADJID=1,SMCROUTEID=1,NAME="SS"; 








父主题： [Diameter SMC局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改Diameter SMC局向配置(SET DIAMSMCADJ) 
#### 修改Diameter SMC局向配置(SET DIAMSMCADJ) 


命令功能 

该命令用于修改Diameter SMC局向配置，执行该命令，可以修改该Diameter SMC局向关联的Diameter SMC局向路由及关联的AVP Profile。


注意事项 

每个Diameter SMC局向最多可以关联2个Diameter SMC局向路由


参数说明 


标识|名称|类型|说明
---|---|---|---
SMCADJID|局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter SMC局向，该参数要求全局唯一。
SMCROUTEID|Diameter SMC局向路由标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示该Diameter SMC局向关联的Diameter SMC局向路由。需要先配置Diameter SMC局向路由。 查询命令参见 SHOW DIAMSMCROUTE。一条Diameter SMC局向最多关联两个Diameter SMC局向路由。
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于指示该Diameter SMC局向关联的AVP Profile，AVP Profile用于控制Diameter消息中的某个AVP是否携带及AVP头中的相关标记位的值。默认值为”0“表明该Diameter SMC局向不关联AVP Profile。如果要关联AVP Profile需要先配置AVP Profile。 配置命令参见 ADD DIM AVP PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的Diameter SMC局向的别名。






命令举例 


修改局向标识为“1”的Diameter SMC局向：关联的Diameter SMC局向路由标识为“1”，关联的AVP Profile为“0”，别名为“SS”。 


SET DIAMSMCADJ:SMCADJID=1,SMCROUTEID=1,AVPPROFILEID=0,NAME="SS"; 








父主题： [Diameter SMC局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除Diameter SMC局向配置(DEL DIAMSMCADJ) 
#### 删除Diameter SMC局向配置(DEL DIAMSMCADJ) 


命令功能 

该命令用于删除Diameter SMC局向配置。


注意事项 

删除Diameter SMC局向时要确保该局向没有被Diameter SMC号码分析结果索引所关联。参见[SHOW DIMSMC ANALYSIS]。


参数说明 


标识|名称|类型|说明
---|---|---|---
SMCADJID|局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter SMC局向，该参数要求全局唯一。






命令举例 


删除局向标识为“1”的Diameter SMC局向。 


DEL DIAMSMCADJ:SMCADJID=1; 








父主题： [Diameter SMC局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询Diameter SMC局向配置(SHOW DIAMSMCADJ) 
#### 查询Diameter SMC局向配置(SHOW DIAMSMCADJ) 


命令功能 

该命令用于查询Diameter SMC局向配置，使用该命令可以显示该Diameter SMC局向关联的Diameter SMC局向路由及AVP Profile信息。


注意事项 



 
该命令不带参数，可查询所有的Diameter SMC局向配置记录。
 

 
该命令也可根据Diameter SMC局向标识查询与之匹配的记录。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
SMCADJID|局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于标识一条Diameter SMC局向，该参数要求全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
SMCADJID|局向标识|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条Diameter SMC局向，该参数要求全局唯一。
SMCROUTEID1|Diameter SMC局向路由标识1|参数可选性:任选参数；参数类型:整数。|配置的Diameter SMC局向关联的Diameter SMC局向路由，Diameter SMC局向路由必须已经存在。一条Diameter SMC局向最多关联两个Diameter SMC局向路由。Diameter SMC局向路由标识2同此说明，不再详述。
SMCROUTEID2|Diameter SMC局向路由标识2|参数可选性:任选参数；参数类型:整数。|同“Diameter SMC局向路由标识1”说明
AVPPROFILEID|AVP Profile标识|参数可选性:任选参数；参数类型:整数。|该参数用于指示该Diameter SMC局向关联的AVP Profile，AVP Profile用于控制Diameter消息中的某个AVP是否携带及AVP头中的相关标记位的值。默认值为”0“表明该Diameter SMC局向不关联AVP Profile。如果要关联AVP Profile需要先配置AVP Profile。 配置命令参见 ADD DIM AVP PROFILE。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|配置的Diameter SMC局向的别名。






命令举例 


查询所有Diameter SMC局向配置信息。 


SHOW DIAMSMCADJ; 


`
命令 (No.1): SHOW DIAMSMCADJ

操作维护         局向标识   Diameter SMC局向路由标识1   Diameter SMC局向路由标识2   AVP Profile标识   用户别名
----------------------------------------------------------------------------------------------------------------
复制 修改 删除   5          5                                                         0                 SS
----------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。


` 








父主题： [Diameter SMC局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Support Feature管理 
## Support Feature管理 


背景知识 


MME与HSS之间使用Diameter协议，在ULR/ULA、IDR/IDA等Diameter消息中，通过携带Support Feature字段，MME与HSS相互通知其所支持的Feature能力并进行能力协商。 




功能描述 



                通过Support Feature配置，可为MME配置多种Feature能力模板，基于用户IMSI优先级选择最高、其次是用户所在HSS局向，如无对应HSS局向则使用默认局向路由，MME可选择不同的Feature能力发送通知HSS。在
                [ADD DIAMADJ]
                、
                [ADD DIAMADJROUTE]
                和
                [ADD DIMMEG ANALYSIS]
                命令中选择配置的Feature能力模板。
            




相关主题 



 

新增Support Feature管理设置(ADD SUPFEATURE)
 

 

修改Support Feature管理设置(SET SUPFEATURE)
 

 

删除Support Feature管理设置(DEL SUPFEATURE)
 

 

查询Support Feature管理设置(SHOW SUPFEATURE)
 

 

查询全局Support Feature管理设置(SHOW GLOBAL SUPFEATURE)
 

 








父主题： [Diameter配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增Support Feature管理设置(ADD SUPFEATURE) 
### 新增Support Feature管理设置(ADD SUPFEATURE) 


命令功能 


本命令用于增加Support Feature模板配置。可以在MME中配置多个Support Feature模板，基于用户的IMSI或用户所在HSS局向ID选择不同的模板，实现不同用户在MME中具有不同的Support Feature能力。 




注意事项 


MME支持最大配置16个Feature模板。 




参数说明 


标识|名称|类型|说明
---|---|---|---
FEATUREID|Feature ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数用于指定一个Support Feature模板标识号，需全局唯一，此参数对应ADD DIAMADJ, ADD DIAMADJROUTE和ADD DIMMEG ANALYSIS命令中SUPFEATUREID或FEATID参数
SUPFEATURE|Support Feature|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Support Feature，取值含义：ODBALLAPN(Operator Determined Barring of all Packet Oriented Services)：该参数用于指示是否支持ODBALLAPN能力。ODBHPLMNAPN(Operator Determined Barring of Packet Oriented Services from access points that are within the HPLMN whilst the subscriber is roaming in a VPLMN):该参数用于设置是否支持漫游用户使用归属地APN业务禁止。ODBVPLMNAPN(Operator Determined Barring of Packet Oriented Services from access points that are within the roamed to VPLMN):该参数用于设置是否支持漫游用户使用拜访地APN业务禁止。RegSubs(Regional Subscription)：该参数用于指示是否支持Regional Subscription能力。Trace(TRACE)：该参数用于指示是否支持Trace能力。LCS-BasicSelfLoc(LCS-BasicSelfLocation)：该参数用于指示是否支持LCS- BasicSelfLocation能力。LCS-TransToThird(LCS-TransferToThirdParty)：该参数用于指示是否支持LCS-TransferToThirdParty能力。UE-Reach-Noti(UE-Reachability-Notification)：该参数用于指示是否支持UE-Reachability-Notification能力。T-ADSDataRetri(T-ADS Data Retrieval)：该参数用于指示是否支持T-ADS Data Retrieval能力。State/Loc-Retri(State/Location-Information-Retrieval)：该参数用于指示是否支持State/Location-Information-Retrieval能力。A-MSISDN(A-MSISDN)：该参数用于指示是否支持HSS签约数据包含A-MSISDN字段。
SUPFEATURE2|Support Feature 2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Support Feature 2，取值含义：SMS-IN-MME：该参数用于指示HSS MME是否支持SMS IN MME功能。P-CSCF Restoration：该参数用于设置是否支持当P-CSCF发生故障时，MME触发对IMS PDN重建或IMS PDN恢复Non-IP PDN Type APNs：该参数用于指示是否支持Non-IP PDN 类型的APNDedicated Core Networks：该参数用于指示HSS MME是否支持DCN功能。NR as Secondary RAT：该参数用于指示HSS 和MME是否支持NR as Secondary RAT功能。Communication Pattern：该参数用于是否支持Communication Pattern功能。






命令举例 


新增Support Feature管理设置，其中Feature ID为2，Support Feature为State/Loc-Retri。 


ADD SUPFEATURE:FEATUREID=2,SUPFEATURE="STALOC"; 








父主题： [Support Feature管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改Support Feature管理设置(SET SUPFEATURE) 
### 修改Support Feature管理设置(SET SUPFEATURE) 


命令功能 


本命令用于修改已有的Support Feature模板配置。当需要改变现有Support Feature模板中的能力，使用该命令。修改成功后，用户发送Diameter消息中将携带新的Support Feature能力。 




注意事项 

无


参数说明 


标识|名称|类型|说明
---|---|---|---
FEATUREID|Feature ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数用于指定一个Support Feature模板标识号，需全局唯一，此参数对应ADD DIAMADJ, ADD DIAMADJROUTE和ADD DIMMEG ANALYSIS命令中SUPFEATUREID或FEATID参数
SUPFEATURE|Support Feature|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Support Feature，取值含义：ODBALLAPN(Operator Determined Barring of all Packet Oriented Services)：该参数用于指示是否支持ODBALLAPN能力。ODBHPLMNAPN(Operator Determined Barring of Packet Oriented Services from access points that are within the HPLMN whilst the subscriber is roaming in a VPLMN):该参数用于设置是否支持漫游用户使用归属地APN业务禁止。ODBVPLMNAPN(Operator Determined Barring of Packet Oriented Services from access points that are within the roamed to VPLMN):该参数用于设置是否支持漫游用户使用拜访地APN业务禁止。RegSubs(Regional Subscription)：该参数用于指示是否支持Regional Subscription能力。Trace(TRACE)：该参数用于指示是否支持Trace能力。LCS-BasicSelfLoc(LCS-BasicSelfLocation)：该参数用于指示是否支持LCS- BasicSelfLocation能力。LCS-TransToThird(LCS-TransferToThirdParty)：该参数用于指示是否支持LCS-TransferToThirdParty能力。UE-Reach-Noti(UE-Reachability-Notification)：该参数用于指示是否支持UE-Reachability-Notification能力。T-ADSDataRetri(T-ADS Data Retrieval)：该参数用于指示是否支持T-ADS Data Retrieval能力。State/Loc-Retri(State/Location-Information-Retrieval)：该参数用于指示是否支持State/Location-Information-Retrieval能力。A-MSISDN(A-MSISDN)：该参数用于指示是否支持HSS签约数据包含A-MSISDN字段。
SUPFEATURE2|Support Feature 2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Support Feature 2，取值含义：SMS-IN-MME：该参数用于指示HSS MME是否支持SMS IN MME功能。P-CSCF Restoration：该参数用于设置是否支持当P-CSCF发生故障时，MME触发对IMS PDN重建或IMS PDN恢复Non-IP PDN Type APNs：该参数用于指示是否支持Non-IP PDN 类型的APNDedicated Core Networks：该参数用于指示HSS MME是否支持DCN功能。NR as Secondary RAT：该参数用于指示HSS 和MME是否支持NR as Secondary RAT功能。Communication Pattern：该参数用于是否支持Communication Pattern功能。






命令举例 


修改Feature ID为2的配置数据，将Support Feature修改为T-ADSDataRetri。 


SET SUPFEATURE:FEATUREID=2,SUPFEATURE="TADS"; 








父主题： [Support Feature管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除Support Feature管理设置(DEL SUPFEATURE) 
### 删除Support Feature管理设置(DEL SUPFEATURE) 


命令功能 


本命令用于删除已有的Support Feature模板配置。当某个Support Feature模板不再使用时，使用该命令。 




注意事项 


当需要删除某Support Feature模板，需确定此模板未在命令[ADD DIAMADJ], [ADD DIAMADJROUTE]和[ADD DIMMEG ANALYSIS]命令中被使用。




参数说明 


标识|名称|类型|说明
---|---|---|---
FEATUREID|Feature ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数用于指定一个Support Feature模板标识号，需全局唯一，此参数对应ADD DIAMADJ, ADD DIAMADJROUTE和ADD DIMMEG ANALYSIS命令中SUPFEATUREID或FEATID参数






命令举例 


删除Feature ID为2的配置数据。 


DEL SUPFEATURE:FEATUREID=2; 








父主题： [Support Feature管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询Support Feature管理设置(SHOW SUPFEATURE) 
### 查询Support Feature管理设置(SHOW SUPFEATURE) 


命令功能 


本命令用于显示已有的Support Feature模板配置。 




注意事项 

无


参数说明 


标识|名称|类型|说明
---|---|---|---
FEATUREID|Feature ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|该参数用于指定一个Support Feature模板标识号，需全局唯一，此参数对应ADD DIAMADJ, ADD DIAMADJROUTE和ADD DIMMEG ANALYSIS命令中SUPFEATUREID或FEATID参数






输出参数说明 


标识|名称|类型|说明
---|---|---|---
FEATUREID|Feature ID|参数可选性:任选参数；参数类型:整数。|该参数用于指定一个Support Feature模板标识号，需全局唯一，此参数对应ADD DIAMADJ, ADD DIAMADJROUTE和ADD DIMMEG ANALYSIS命令中SUPFEATUREID或FEATID参数
SUPFEATURE|Support Feature|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Support Feature，取值含义：ODBALLAPN(Operator Determined Barring of all Packet Oriented Services)：该参数用于指示是否支持ODBALLAPN能力。ODBHPLMNAPN(Operator Determined Barring of Packet Oriented Services from access points that are within the HPLMN whilst the subscriber is roaming in a VPLMN):该参数用于设置是否支持漫游用户使用归属地APN业务禁止。ODBVPLMNAPN(Operator Determined Barring of Packet Oriented Services from access points that are within the roamed to VPLMN):该参数用于设置是否支持漫游用户使用拜访地APN业务禁止。RegSubs(Regional Subscription)：该参数用于指示是否支持Regional Subscription能力。Trace(TRACE)：该参数用于指示是否支持Trace能力。LCS-BasicSelfLoc(LCS-BasicSelfLocation)：该参数用于指示是否支持LCS- BasicSelfLocation能力。LCS-TransToThird(LCS-TransferToThirdParty)：该参数用于指示是否支持LCS-TransferToThirdParty能力。UE-Reach-Noti(UE-Reachability-Notification)：该参数用于指示是否支持UE-Reachability-Notification能力。T-ADSDataRetri(T-ADS Data Retrieval)：该参数用于指示是否支持T-ADS Data Retrieval能力。State/Loc-Retri(State/Location-Information-Retrieval)：该参数用于指示是否支持State/Location-Information-Retrieval能力。A-MSISDN(A-MSISDN)：该参数用于指示是否支持HSS签约数据包含A-MSISDN字段。
SUPFEATURE2|Support Feature 2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Support Feature 2，取值含义：SMS-IN-MME：该参数用于指示HSS MME是否支持SMS IN MME功能。P-CSCF Restoration：该参数用于设置是否支持当P-CSCF发生故障时，MME触发对IMS PDN重建或IMS PDN恢复Non-IP PDN Type APNs：该参数用于指示是否支持Non-IP PDN 类型的APNDedicated Core Networks：该参数用于指示HSS MME是否支持DCN功能。NR as Secondary RAT：该参数用于指示HSS 和MME是否支持NR as Secondary RAT功能。Communication Pattern：该参数用于是否支持Communication Pattern功能。






命令举例 


查询所有的Support Feature管理设置 


SHOW SUPFEATURE; 


`

命令 (No.1): SHOW SUPFEATURE

操作维护         Feature ID   Support Feature   Support Feature 2
-----------------------------------------------------------------
复制 修改 删除   1            ODBALLAPN         Non-IP PDN Type APNs
-----------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.034 秒）。

` 








父主题： [Support Feature管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询全局Support Feature管理设置(SHOW GLOBAL SUPFEATURE) 
### 查询全局Support Feature管理设置(SHOW GLOBAL SUPFEATURE) 


命令功能 


本命令用于查询全局Support Feature。 




注意事项 

无


输出参数说明 


标识|名称|类型|说明
---|---|---|---
SUPFEATURE|Support Feature|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Support Feature，取值含义：ODBALLAPN(Operator Determined Barring of all Packet Oriented Services)：该参数用于指示是否支持ODBALLAPN能力。ODBHPLMNAPN(Operator Determined Barring of Packet Oriented Services from access points that are within the HPLMN whilst the subscriber is roaming in a VPLMN):该参数用于设置是否支持漫游用户使用归属地APN业务禁止。ODBVPLMNAPN(Operator Determined Barring of Packet Oriented Services from access points that are within the roamed to VPLMN):该参数用于设置是否支持漫游用户使用拜访地APN业务禁止。RegSubs(Regional Subscription)：该参数用于指示是否支持Regional Subscription能力。Trace(TRACE)：该参数用于指示是否支持Trace能力。LCS-BasicSelfLoc(LCS-BasicSelfLocation)：该参数用于指示是否支持LCS- BasicSelfLocation能力。LCS-TransToThird(LCS-TransferToThirdParty)：该参数用于指示是否支持LCS-TransferToThirdParty能力。UE-Reach-Noti(UE-Reachability-Notification)：该参数用于指示是否支持UE-Reachability-Notification能力。T-ADSDataRetri(T-ADS Data Retrieval)：该参数用于指示是否支持T-ADS Data Retrieval能力。State/Loc-Retri(State/Location-Information-Retrieval)：该参数用于指示是否支持State/Location-Information-Retrieval能力。
SUPFEATURE2|Support Feature 2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Support Feature 2，取值含义：SMS-IN-MME：该参数用于指示HSS MME是否支持SMS IN MME功能。P-CSCF Restoration：该参数用于设置是否支持当P-CSCF发生故障时，MME触发对IMS PDN重建或IMS PDN恢复。Non-IP PDN Type APNs：该参数用于指示是否支持Non-IP PDN 类型的APN。Dedicated Core Networks：该参数用于指示HSS MME是否支持DCN功能。NR as Secondary RAT：该参数用于指示HSS 和MME是否支持NR as Secondary RAT功能。Communication Pattern：该参数用于是否支持Communication Pattern功能。






命令举例 


查询全局Support Feature管理设置。 


SHOW GLOBAL SUPFEATURE; 


`
 
命令 (No.1): SHOW GLOBAL SUPFEATURE

Support Feature                                Support Feature 2
----------------------------------------------------------------
ODBALLAPN & T-ADSDataRetri & State/Loc-Retri   Null
----------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.072 秒）。
` 








父主题： [Support Feature管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Diameter SCEF配置 
## Diameter SCEF配置 


背景知识 

            
            MME支持对接SCEF网元，需要配置SCEF所属的Diameter局向链路信息。
        


功能描述 

            
            Diameter SCEF配置用于增加SCEF局向链路信息，包括SCEF的名称与ID。
        


相关主题 



 

新增Diameter SCEF配置(ADD DIASCEF)
 

 

修改Diameter SCEF配置(SET DIASCEF)
 

 

删除Diameter SCEF配置(DEL DIASCEF)
 

 

查询Diameter SCEF配置(SHOW DIASCEF)
 

 








父主题： [Diameter配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增Diameter SCEF配置(ADD DIASCEF) 
### 新增Diameter SCEF配置(ADD DIASCEF) 


命令功能 

该命令用于新增Diameter SCEF配置。当需要增加对接SCEF网元信息时，使用该命令。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
SCEFNAME|SCEF节点名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~150个字符。|该参数用于配置SCEF名称，字符长度的范围取值为[1, 150]。
ADJOFFICEID|邻接局编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于配置SCEF的ID，范围取值为[1, 4224]。






命令举例 


创建Diameter SCEF配置，SCEF名称为SCEF_1，邻接局ID为176。 


ADD DIASCEF:SCEFNAME=SCEF_1,ADJOFFICEID=176; 








父主题： [Diameter SCEF配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改Diameter SCEF配置(SET DIASCEF) 
### 修改Diameter SCEF配置(SET DIASCEF) 


命令功能 

该命令用于修改Diameter SCEF配置。当需要修改对接SCEF网元信息时，使用该命令。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
SCEFNAME|SCEF节点名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~150个字符。|该参数用于配置SCEF名称，字符长度的范围取值为[1, 150]。
ADJOFFICEID|邻接局编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|该参数用于配置SCEF的ID，范围取值为[1, 4224]。






命令举例 


修改Diameter SCEF配置，SCEF名称为SCEF_1，邻接局ID为176。 


SET DIASCEF:SCEFNAME=SCEF_1,ADJOFFICEID=176; 








父主题： [Diameter SCEF配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除Diameter SCEF配置(DEL DIASCEF) 
### 删除Diameter SCEF配置(DEL DIASCEF) 


命令功能 

该命令用于删除Diameter SCEF配置。当需要去除对接SCEF网元信息时，使用该命令。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
SCEFNAME|SCEF节点名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~150个字符。|该参数用于配置SCEF名称，字符长度的范围取值为[1, 150]。






命令举例 


删除SCEF名称为SCEF_1的Diameter SCEF配置。 


DEL DIASCEF:SCEFNAME=SCEF_1; 








父主题： [Diameter SCEF配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询Diameter SCEF配置(SHOW DIASCEF) 
### 查询Diameter SCEF配置(SHOW DIASCEF) 


命令功能 

该命令用于查询Diameter SCEF配置。当需要查询本局对接的SCEF网元信息时，使用该命令。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
SCEFNAME|SCEF节点名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~150个字符。|该参数用于配置SCEF名称，字符长度的范围取值为[1, 150]。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
SCEFNAME|SCEF节点名称|参数可选性:任选参数；参数类型:字符型。|该参数用于配置SCEF名称，字符长度的范围取值为[1, 150]。
ADJOFFICEID|邻接局编号|参数可选性:任选参数；参数类型:整数。|该参数用于配置SCEF的ID，范围取值为[1, 4224]。






命令举例 


查询SCEF名称为SCEF_1的Diameter SCEF配置。 


SHOW DIASCEF:SCEFNAME=SCEF_1; 


`

命令 (No.1): SHOW DIASCEF:SCEFNAME=SCEF_1;

操作维护                       SCEF名称             邻接局
---------------------------------------------------------------------
复制 修改 删除                  SCEF_1               176
---------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.06 秒）。

` 








父主题： [Diameter SCEF配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Diameter消息控制配置 
## Diameter消息控制配置 


背景知识 

            
            MME与HSS、EIR和GMLC网元使用Diameter协议连接，MME和对端网元进行业务消息交互时，本网元的Diameter消息以及消息内容需要和对端能力相匹配，保证网元对接成功以及业务处理正常。
        


功能描述 

            
            通过Diameter消息控制配置，可以对HSS、EIR、GMLC网元的消息以及消息内容进行控制，对发送到HSS的消息和消息参数进行灵活控制。包括：HSS消息ALR、CLA、PUR、IDA、DSA、RSA、NOR中是否携带Support Feature AVP。
        


相关主题 



 

设置HSS消息控制策略(SET HSS MSGCTL POLICY)
 

 

查询HSS消息控制策略(SHOW HSS MSGCTL POLICY)
 

 








父主题： [Diameter配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置HSS消息控制策略(SET HSS MSGCTL POLICY) 
### 设置HSS消息控制策略(SET HSS MSGCTL POLICY) 


命令功能 


该命令用于修改HSS的消息和消息参数携带策略。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
S6AMSGWITHSUPPFEAT|S6a接口消息携带Support Feature策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IDA。|根据此参数设置S6a接口IDA、AIR、CLA、NOR、DSA、PUR、RSA消息中是否携带Support Feature AVP参数。缺省值为1，默认IDA消息中携带Support Feature AVP参数。ULR默认携带Support Feature AVP参数。






命令举例 


设置HSS的消息和消息参数携带策略为AIR。 


SET  HSS MSGCTL POLICY:S6AMSGWITHSUPPFEAT=AIR; 








父主题： [Diameter消息控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询HSS消息控制策略(SHOW HSS MSGCTL POLICY) 
### 查询HSS消息控制策略(SHOW HSS MSGCTL POLICY) 


命令功能 


该命令用于查询HSS的消息和消息参数携带策略。 




注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
S6AMSGWITHSUPPFEAT|S6a接口消息携带Support Feature策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|根据此参数设置S6a接口IDA、AIR、CLA、NOR、DSA、PUR、RSA消息中是否携带Support Feature AVP参数。缺省值为1，默认IDA消息中携带Support Feature AVP参数。ULR默认携带Support Feature AVP参数。






命令举例 


查询当前HSS的消息和消息参数携带策略。 


SHOW HSS MSGCTL POLICY; 


`

命令 (No.1): SHOW HSS MSGCTL POLICY

S6a接口消息携带Support Feature策略    
---------------
Authentication-Information-Request            
---------------

命令执行成功（耗时 0.047 秒）。
 ` 








父主题： [Diameter消息控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# Gb接入配置 
# Gb接入配置 


背景知识 


Gb接口是移动通信网络中SGSN网元和BSC网元间接口，SGSN通过该接口与BSS系统、MS进行通信，以完成分组数据传送、移动性管理、会话管理的功能。 


该接口是GPRS组网的必选接口，目前的主要参考技术规范包括3GPP 48.016、3GPP 48.018。 




功能描述 


本模块主要包括网络业务实体的配置以及Gb口数据传输链路的配置。 


网络业务实体（NSE）用于管理BSC和SGSN之间的连接资源。从SGSN侧看来，一个网络业务实体就相当于一个BSC。配置一个NSE，可以对指定的BSC赋予不同的网元特性。根据组网需要，Gb口数据传输链路可以选择帧中继承载或IP承载。 



 

当选择帧中继承载时，需要配置“FR逻辑端口”、“FR永久虚连接”、“FR网络业务虚连接”。
 

 


                        当选择IP承载时，需要配置“本端IP端点”。如果
                        SET NSE
                        是“静态(Static)”，还要进一步配置“远端IP端点”和“IP网络业务虚连接”。
                    
 

 




相关主题 



 

网络业务实体配置
 

 

NSE保护路由区配置
 

 

本端IP端点配置
 

 

远端IP端点配置
 

 

IP网络业务虚连接配置
 

 

Gb口网络管理
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 网络业务实体配置 
## 网络业务实体配置 


背景知识 


要在BSC网元与SGSN网元之间完成通讯，必须建立相应的通讯链路，即网络业务虚连接（NSVC）。为了便于管理这些虚连接资源，比如进行负荷分担，需要配置相应的网络业务实体。一个网络业务实体用来管理一对BSC和SGSN之间的所有Gb口连接资源，比如NSVC和BVC（小区虚连接，3GPP 48.018协议标准未明确给出定义，但从上下文可以推断为BSSGP Virtual Connection），赋予或标明这些连接所具有的共性特征，进而便于系统在运行中对具有不同属性的网络业务实体下的业务采取不同的控制策略。 


与网络业务实体相关的协议标准可以参考3GPP 48.016和3GPP 48.018。 




功能描述 


当需要与BSC对接时，必须进行网络业务实体配置。 


功能用于增加、删除网络业务实体，修改或查询网络业务实体的相关属性。 


配置网络业务实体的流程如下： 







                        配置网络业务实体。假设标识为101的网络业务实体已经与BSC协商并且达成一致，则可以配置一个NSEI为101的网络业务实体。配置命令为：
                        [ADD NSE]
                        :NSEI=101;
                    








相关主题 



 

新增网络业务实体(ADD NSE)
 

 

修改网络业务实体(SET NSE)
 

 

删除网络业务实体(DEL NSE)
 

 

查询网络业务实体(SHOW NSE)
 

 








父主题： [Gb接入配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增网络业务实体(ADD NSE) 
### 新增网络业务实体(ADD NSE) 


命令功能 


该命令用于在SGSN上增加一个网络业务实体（NSE，Network service Entity）。 


NSE在3GPP TS 48.016中定义，BSC和SGSN之间的接口叫做Gb口，对应的协议栈叫做Gb口协议栈，NS层（网络业务实体层）是Gb口协议栈分层体系中的一个分层，NS层（网络业务实体层）屏蔽下层物理承载差异和细节，为上层用户提供逻辑链路通道。NSE（网络业务实体）是一个逻辑概念，就是用于管理，操作，维护这些逻辑链路通道的实体。 




注意事项 

SGSN最大支持8192个NSE。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
RAT|无线接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:GERAN。|该参数用于指示本NSE对应的BSC侧的无线接入类型，需要向BSC侧获取后选择。取值含义：GEARN：BSC侧无线接入类型为EDGE接入。NO RAT：BSC侧无线接入类型为传统GPRS接入。
FLEX|支持Flex功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指示本NSE是否支持Flex功能，需要和BSC侧协商，如果BSC侧进行了Flex组网，支持Flex，则SGSN上应该选中该NSE支持Flex，否则选择为不支持。取值含义：不支持(NO)：该NSE不支持Flex功能。支持(YES)：该NSE支持Flex功能。
PFC|支持PFC功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指示本网络业务实体是否支持PFC流程（Packet Flow Context Procedure），参考协议3GPP TS 48.018。如果本端NSE配置支持PFC流程，并且BSC侧的NSE也支持PFC流程（BSC通过BVC RESET消息中Feature bitmap信元里面的PFC bit比特位指示通知SGSN自己是否支持PFC流程），则SGSN才支持PFC流程。取值含义：不支持（NO）：该NSE不支持PFC功能。支持（YES）：该NSE支持PFC功能。
INR|支持NSE间重路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指示本网络业务实体是否支持INR功能（Inter-NSE re-routing，跨NSE重路由功能），参考协议3GPP TS 48.018。如果本端NSE配置支持INR功能，并且BSC侧的NSE也支持INR功能（BSC通过BVC RESET消息中Feature bitmap信元里面的INR bit指示通知SGSN自己是否支持INR功能），则SGSN才支持INR功能。取值含义：不支持(NO)：该NSE不支持NSE间重路由功能。支持(YES)：该NSE支持NSE间重路由功能。
PFC_FC|支持PFC流控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|是否支持向BSC发送FLOW-CONTROL-PFC-ACK消息。取值含义：是：支持向BSC发送FLOW-CONTROL-PFC-ACK消息。否：不支持向BSC发送FLOW-CONTROL-PFC-ACK消息。
BEARMODE|承载方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:IP。|该参数用于指示本NSE的承载网络类型。取值含义：IP：该NSE采用IP网络承载。
NSVCMODE|配置属性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE下的NSVC配置是采用动态配置还是静态配置。静态配置需要在SGSN侧和BSC侧，对对端IP端点和IP NSVC都采用静态配置方式。动态配置是指在SGSN上不需要配置BSC侧IP端点和NSVC，由BSC侧发起信令流程，来动态的建立IP NSVC。具体的信令流程参见协议3GPP TS 48.016。取值含义：静态(Static)：管理员静态配置远端端点和IP网络业务虚连接。动态(Dynamic)：通过信令过程动态配置远端端点和IP网络业务虚连接。
VPNID|VRF 标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。默认值:0。|该参数用于设置该NSE对应IP路由虚拟路由域，设置后，该NSE发往BSC的IP报文进行IP路由时，选择该VRF关联的路由域内路由，起到隔离路由域的作用。如果不需要隔离路由域，不需要关联某个IP路由虚拟路由域，则设置为0表示不关联。该参数仅对NSE承载采用IP承载时才有意义，FR承载时该参数无意义，配置为0即可。
NEWTLLIFG|是否携带NEW TLLI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|在SGSN新分配了P-TMSI后，是否以新分配的P-TMSI导出TLLI，在BSSGP层，“BSSGP DL-UNITDATA”消息的“TLLI (current)”信元中携带给BSC。取值含义：不携带（NO）：SGSN新分配了P-TMSI后，BSSGP层“BSSGP DL-UNITDATA”消息的“TLLI (current)”信元不填充为新分配的P-TMSI导出的新TLLI，还是填充为老的TLLI给BSC，且不携带“TLLI (old)”信元。携带（YES）：SGSN新分配了P-TMSI后，BSSGP层“BSSGP DL-UNITDATA”消息中的“TLLI (current)”信元填充为新分配的P-TMSI导出的新TLLI，同时将老的TLLI放在“TLLI (old)”信元中带给BSC。
T10TIMER|T10定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~3600。默认值:6。|用于填充CREATE-BSS-PFC消息中的T10信元(IE)，PFC排队定时器，BSS侧使用。目前未实现。
UTRANCCO|向UTRAN小区重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:PREFERENCE。|用于填充DL-UNITDATA消息中的Service UTRAN CCO信元(IE)，控制UE向UTRAN的切换顺序。
EUTRANCCO|向EUTRAN小区重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:PREFERENCE。|用于填充DL-UNITDATA消息中的Service UTRAN CCO信元(IE)，控制UE向E-UTRAN的切换顺序。
FCM_E|启用MS流控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|对本NSE下接入的用户，是否启用MS流控功能。MS流控功能参见3GPP TS 48.018协议，BSC通过FLOW-CONTROL-MS消息通知SGSN该MS在BSC上对应的桶大小、漏率大小，SGSN根据这两个参数来对下发给该MS的下行报文实施流控算法，对于不通过流控算法的下行帧暂不下发给BSC，避免报文在BSC堆积溢出丢弃。
FCM_R_SCALE|MS流控漏率缩放比|参数可选性:任选参数；参数类型:字符型；参数范围为:0~6个字符。默认值:1.00。|MS流控漏率，是MS流控算法实施的重要参数，由BSC通过FLOW-CONTROL-MS消息通知SGSN。SGSN为了灵活实施MS流控效果，对BSC上报的漏率参数可以进行调整，可以进行缩小或者放大，这样通过调整该参数，可以更加灵活的进行MS流控。该参数默认为1，表示原样使用BSC上报的漏率。配置小于1时，表示漏率缩小，配置大于1时，表示漏率放大。
FCM_B_SCALE|MS流控桶容量缩放比|参数可选性:任选参数；参数类型:字符型；参数范围为:0~6个字符。默认值:1.00。|MS流控桶容量，是MS流控算法实施的重要参数，由BSC通过FLOW-CONTROL-MS消息通知SGSN。SGSN为了灵活实施MS流控效果，对BSC上报的桶容量参数可以进行调整，可以进行缩小或者放大，这样通过调整该参数，可以更加灵活的进行MS流控。该参数默认为1，表示原样使用BSC上报的桶容量。配置小于1时，表示桶容量缩小，配置大于1时，表示桶容量放大。
NAME|NSE名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|本网络业务实体NSE的名称，由用户自行规划命名，便于记忆和识别。
SPRTRFSP|支持RFSP|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:OFF。|该参数用于设置BSC是否支持RFSP功能。不支持：BSC默认不支持RFSP。支持：BSC支持RFSP。
IFSPRTMOCN|支持MOCN功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:OFF。|该参数标识该NSE是否支持MOCN功能。不支持：NSE默认不支持MOCN。支持：NSE支持MOCN。






命令举例 


BSC和SGSN对接，新增加NSE。约定NSEI为1，采用IP方式承载，静态配置IP端点和NSVC，NSE名称为BSC_NanJing。
 ADD NSE:NSEI=1,BEARMODE="IP",NSVCMODE="Static",NAME="BSC_NanJing";
 








父主题： [网络业务实体配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改网络业务实体(SET NSE) 
### 修改网络业务实体(SET NSE) 


命令功能 


该命令用于修改已经配置在SGSN上的网络业务实体NSE的参数，如修改NSE名称，修改NSE支持Flex功能，修改NSE关联的IP路由虚拟域VRF标识等。 


基于设备维护的需要，NSE相关参数发生变更时，可以使用该命令，根据NSEI标识，修改对应NSE的参数。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
RAT|无线接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE对应的BSC侧的无线接入类型，需要向BSC侧获取后选择。取值含义：GEARN：BSC侧无线接入类型为EDGE接入。NO RAT：BSC侧无线接入类型为传统GPRS接入。
FLEX|支持Flex功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE是否支持Flex功能，需要和BSC侧协商，如果BSC侧进行了Flex组网，支持Flex，则SGSN上应该选中该NSE支持Flex，否则选择为不支持。取值含义：不支持(NO)：该NSE不支持Flex功能。支持(YES)：该NSE支持Flex功能。
PFC|支持PFC功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本网络业务实体是否支持PFC流程（Packet Flow Context Procedure），参考协议3GPP TS 48.018。如果本端NSE配置支持PFC流程，并且BSC侧的NSE也支持PFC流程（BSC通过BVC RESET消息中Feature bitmap信元里面的PFC bit比特位指示通知SGSN自己是否支持PFC流程），则SGSN才支持PFC流程。取值含义：不支持（NO）：该NSE不支持PFC功能。支持（YES）：该NSE支持PFC功能。
INR|支持NSE间重路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本网络业务实体是否支持INR功能（Inter-NSE re-routing，跨NSE重路由功能），参考协议3GPP TS 48.018。如果本端NSE配置支持INR功能，并且BSC侧的NSE也支持INR功能（BSC通过BVC RESET消息中Feature bitmap信元里面的INR bit指示通知SGSN自己是否支持INR功能），则SGSN才支持INR功能。取值含义：不支持(NO)：该NSE不支持NSE间重路由功能。支持(YES)：该NSE支持NSE间重路由功能。
PFC_FC|支持PFC流控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否支持向BSC发送FLOW-CONTROL-PFC-ACK消息。取值含义：是：支持向BSC发送FLOW-CONTROL-PFC-ACK消息。否：不支持向BSC发送FLOW-CONTROL-PFC-ACK消息。
BEARMODE|承载方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE的承载网络类型。取值含义：IP：该NSE采用IP网络承载。
NSVCMODE|配置属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE下的NSVC配置是采用动态配置还是静态配置。静态配置需要在SGSN侧和BSC侧，对对端IP端点和IP NSVC都采用静态配置方式。动态配置是指在SGSN上不需要配置BSC侧IP端点和NSVC，由BSC侧发起信令流程，来动态的建立IP NSVC。具体的信令流程参见协议3GPP TS 48.016。取值含义：静态(Static)：管理员静态配置远端端点和IP网络业务虚连接。动态(Dynamic)：通过信令过程动态配置远端端点和IP网络业务虚连接。
VPNID|VRF 标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|该参数用于设置该NSE对应IP路由虚拟路由域，设置后，该NSE发往BSC的IP报文进行IP路由时，选择该VRF关联的路由域内路由，起到隔离路由域的作用。如果不需要隔离路由域，不需要关联某个IP路由虚拟路由域，则设置为0表示不关联。该参数仅对NSE承载采用IP承载时才有意义，FR承载时该参数无意义，配置为0即可。
NEWTLLIFG|是否携带NEW TLLI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在SGSN新分配了P-TMSI后，是否以新分配的P-TMSI导出TLLI，在BSSGP层，“BSSGP DL-UNITDATA”消息的“TLLI (current)”信元中携带给BSC。取值含义：不携带（NO）：SGSN新分配了P-TMSI后，BSSGP层“BSSGP DL-UNITDATA”消息的“TLLI (current)”信元不填充为新分配的P-TMSI导出的新TLLI，还是填充为老的TLLI给BSC，且不携带“TLLI (old)”信元。携带（YES）：SGSN新分配了P-TMSI后，BSSGP层“BSSGP DL-UNITDATA”消息中的“TLLI (current)”信元填充为新分配的P-TMSI导出的新TLLI，同时将老的TLLI放在“TLLI (old)”信元中带给BSC。
T10TIMER|T10定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~3600。|用于填充CREATE-BSS-PFC消息中的T10信元(IE)，PFC排队定时器，BSS侧使用。目前未实现。
UTRANCCO|向UTRAN小区重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于填充DL-UNITDATA消息中的Service UTRAN CCO信元(IE)，控制UE向UTRAN的切换顺序。
EUTRANCCO|向EUTRAN小区重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于填充DL-UNITDATA消息中的Service UTRAN CCO信元(IE)，控制UE向E-UTRAN的切换顺序。
FCM_E|启用MS流控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|对本NSE下接入的用户，是否启用MS流控功能。MS流控功能参见3GPP TS 48.018协议，BSC通过FLOW-CONTROL-MS消息通知SGSN该MS在BSC上对应的桶大小、漏率大小，SGSN根据这两个参数来对下发给该MS的下行报文实施流控算法，对于不通过流控算法的下行帧暂不下发给BSC，避免报文在BSC堆积溢出丢弃。
FCM_R_SCALE|MS流控漏率缩放比|参数可选性:任选参数；参数类型:字符型；参数范围为:0~6个字符。|MS流控漏率，是MS流控算法实施的重要参数，由BSC通过FLOW-CONTROL-MS消息通知SGSN。SGSN为了灵活实施MS流控效果，对BSC上报的漏率参数可以进行调整，可以进行缩小或者放大，这样通过调整该参数，可以更加灵活的进行MS流控。该参数默认为1，表示原样使用BSC上报的漏率。配置小于1时，表示漏率缩小，配置大于1时，表示漏率放大。
FCM_B_SCALE|MS流控桶容量缩放比|参数可选性:任选参数；参数类型:字符型；参数范围为:0~6个字符。|MS流控桶容量，是MS流控算法实施的重要参数，由BSC通过FLOW-CONTROL-MS消息通知SGSN。SGSN为了灵活实施MS流控效果，对BSC上报的桶容量参数可以进行调整，可以进行缩小或者放大，这样通过调整该参数，可以更加灵活的进行MS流控。该参数默认为1，表示原样使用BSC上报的桶容量。配置小于1时，表示桶容量缩小，配置大于1时，表示桶容量放大。
NAME|NSE名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|本网络业务实体NSE的名称，由用户自行规划命名，便于记忆和识别。
SPRTRFSP|支持RFSP|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置BSC是否支持RFSP功能。不支持：BSC默认不支持RFSP。支持：BSC支持RFSP。
IFSPRTMOCN|支持MOCN功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识该NSE是否支持MOCN功能。不支持：NSE默认不支持MOCN。支持：NSE支持MOCN。






命令举例 


修改1号NSE为支持PFC功能。
 SET NSE:NSEI=1,PFC="YES";
 








父主题： [网络业务实体配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除网络业务实体(DEL NSE) 
### 删除网络业务实体(DEL NSE) 


命令功能 


该命令用于删除已经配置在SGSN上的网络业务实体NSE。 


基于设备维护的需要，不需要该NSE时，可以使用该命令，根据NSEI标识，删除对应的NSE。 


删除NSE前，如果是FR承载，需要先通过[DEL NSVC]命令删除该NSE下的NSVC配置。如果是IP承载，需要先通过[DEL IP NSVC]命令删除该NSE下的IP NSVC配置，通过[DEL REMOTE ENDPOINT]命令删除该NSE下的远端端点配置。




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。






命令举例 


删除1号NSE。
 DEL NSE:NSEI=1; 








父主题： [网络业务实体配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询网络业务实体(SHOW NSE) 
### 查询网络业务实体(SHOW NSE) 


命令功能 

该命令用于查询已经配置在SGSN上的网络业务实体NSE的详细参数信息。可以根据“NSE标识号”、“NSE名称”、“承载方式”条件进行查询。如果不输入任何参数，则表示查询所有网络业务实体配置信息。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
NAME|NSE名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|本网络业务实体NSE的名称，由用户自行规划命名，便于记忆和识别。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数。|NSE标识号，用于在SGSN上唯一标识一个网络业务实体NSE，在SGSN上取值唯一。取值和BSC侧协商，BSC侧和SGSN侧该取值需要保持一致。
RAT|无线接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE对应的BSC侧的无线接入类型，需要向BSC侧获取后选择。取值含义：GEARN：BSC侧无线接入类型为EDGE接入。NO RAT：BSC侧无线接入类型为传统GPRS接入。
FLEX|支持Flex功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE是否支持Flex功能，需要和BSC侧协商，如果BSC侧进行了Flex组网，支持Flex，则SGSN上应该选中该NSE支持Flex，否则选择为不支持。取值含义：不支持(NO)：该NSE不支持Flex功能。支持(YES)：该NSE支持Flex功能。
PFC|支持PFC功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本网络业务实体是否支持PFC流程（Packet Flow Context Procedure），参考协议3GPP TS 48.018。如果本端NSE配置支持PFC流程，并且BSC侧的NSE也支持PFC流程（BSC通过BVC RESET消息中Feature bitmap信元里面的PFC bit比特位指示通知SGSN自己是否支持PFC流程），则SGSN才支持PFC流程。取值含义：不支持（NO）：该NSE不支持PFC功能。支持（YES）：该NSE支持PFC功能。
INR|支持NSE间重路由|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本网络业务实体是否支持INR功能（Inter-NSE re-routing，跨NSE重路由功能），参考协议3GPP TS 48.018。如果本端NSE配置支持INR功能，并且BSC侧的NSE也支持INR功能（BSC通过BVC RESET消息中Feature bitmap信元里面的INR bit指示通知SGSN自己是否支持INR功能），则SGSN才支持INR功能。取值含义：不支持(NO)：该NSE不支持NSE间重路由功能。支持(YES)：该NSE支持NSE间重路由功能。
PFC_FC|支持PFC流控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否支持向BSC发送FLOW-CONTROL-PFC-ACK消息。取值含义：是：支持向BSC发送FLOW-CONTROL-PFC-ACK消息。否：不支持向BSC发送FLOW-CONTROL-PFC-ACK消息。
BEARMODE|承载方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE的承载网络类型。取值含义：IP：该NSE采用IP网络承载。
NSVCMODE|配置属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本NSE下的NSVC配置是采用动态配置还是静态配置。静态配置需要在SGSN侧和BSC侧，对对端IP端点和IP NSVC都采用静态配置方式。动态配置是指在SGSN上不需要配置BSC侧IP端点和NSVC，由BSC侧发起信令流程，来动态的建立IP NSVC。具体的信令流程参见协议3GPP TS 48.016。取值含义：静态(Static)：管理员静态配置远端端点和IP网络业务虚连接。动态(Dynamic)：通过信令过程动态配置远端端点和IP网络业务虚连接。
VPNID|VRF 标识|参数可选性:任选参数；参数类型:整数。|该参数用于设置该NSE对应IP路由虚拟路由域，设置后，该NSE发往BSC的IP报文进行IP路由时，选择该VRF关联的路由域内路由，起到隔离路由域的作用。如果不需要隔离路由域，不需要关联某个IP路由虚拟路由域，则设置为0表示不关联。该参数仅对NSE承载采用IP承载时才有意义，FR承载时该参数无意义，配置为0即可。
NEWTLLIFG|是否携带NEW TLLI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在SGSN新分配了P-TMSI后，是否以新分配的P-TMSI导出TLLI，在BSSGP层，“BSSGP DL-UNITDATA”消息的“TLLI (current)”信元中携带给BSC。取值含义：不携带（NO）：SGSN新分配了P-TMSI后，BSSGP层“BSSGP DL-UNITDATA”消息的“TLLI (current)”信元不填充为新分配的P-TMSI导出的新TLLI，还是填充为老的TLLI给BSC，且不携带“TLLI (old)”信元。携带（YES）：SGSN新分配了P-TMSI后，BSSGP层“BSSGP DL-UNITDATA”消息中的“TLLI (current)”信元填充为新分配的P-TMSI导出的新TLLI，同时将老的TLLI放在“TLLI (old)”信元中带给BSC。
T10TIMER|T10定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|用于填充CREATE-BSS-PFC消息中的T10信元(IE)，PFC排队定时器，BSS侧使用。目前未实现。
UTRANCCO|向UTRAN小区重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于填充DL-UNITDATA消息中的Service UTRAN CCO信元(IE)，控制UE向UTRAN的切换顺序。
EUTRANCCO|向EUTRAN小区重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于填充DL-UNITDATA消息中的Service UTRAN CCO信元(IE)，控制UE向E-UTRAN的切换顺序。
FCM_E|启用MS流控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|对本NSE下接入的用户，是否启用MS流控功能。MS流控功能参见3GPP TS 48.018协议，BSC通过FLOW-CONTROL-MS消息通知SGSN该MS在BSC上对应的桶大小、漏率大小，SGSN根据这两个参数来对下发给该MS的下行报文实施流控算法，对于不通过流控算法的下行帧暂不下发给BSC，避免报文在BSC堆积溢出丢弃。
FCM_R_SCALE|MS流控漏率缩放比|参数可选性:任选参数；参数类型:字符型。|MS流控漏率，是MS流控算法实施的重要参数，由BSC通过FLOW-CONTROL-MS消息通知SGSN。SGSN为了灵活实施MS流控效果，对BSC上报的漏率参数可以进行调整，可以进行缩小或者放大，这样通过调整该参数，可以更加灵活的进行MS流控。该参数默认为1，表示原样使用BSC上报的漏率。配置小于1时，表示漏率缩小，配置大于1时，表示漏率放大。
FCM_B_SCALE|MS流控桶容量缩放比|参数可选性:任选参数；参数类型:字符型。|MS流控桶容量，是MS流控算法实施的重要参数，由BSC通过FLOW-CONTROL-MS消息通知SGSN。SGSN为了灵活实施MS流控效果，对BSC上报的桶容量参数可以进行调整，可以进行缩小或者放大，这样通过调整该参数，可以更加灵活的进行MS流控。该参数默认为1，表示原样使用BSC上报的桶容量。配置小于1时，表示桶容量缩小，配置大于1时，表示桶容量放大。
NAME|NSE名称|参数可选性:任选参数；参数类型:字符型。|本网络业务实体NSE的名称，由用户自行规划命名，便于记忆和识别。
SPRTRFSP|支持RFSP|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置BSC是否支持RFSP功能。不支持：BSC默认不支持RFSP。支持：BSC支持RFSP。
IFSPRTMOCN|支持MOCN功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识该NSE是否支持MOCN功能。不支持：NSE默认不支持MOCN。支持：NSE支持MOCN。






命令举例 


查询1号NSE的详细参数信息。
   SHOW NSE:NSEI=1;
 


`                                                                                                                                                                                                               
                                                                                                                                                                                                                 
 命令 (No.1): SHOW NSE:NSEI=1;

操作维护         NSE标识号   无线接入类型   支持Flex功能   支持PFC功能   支持NSE间重路由   支持PFC流控   承载方式   配置属性   VRF 标识   是否携带NEW TLLI   T10定时器时长(秒)   向UTRAN小区重选         向EUTRAN小区重选          启用MS流控   MS流控漏率缩放比   MS流控桶容量缩放比   NSE名称          支持RFSP   支持MOCN功能
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1           GERAN          不支持         不支持        不支持            不支持        IP         静态       0          不携带             6                   优先向UTRAN小区重选     优先向E-UTRAN小区重选     否           1                  1                    BSC_NanJing      否         否   
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。

                                                                                                                                                                                    
` 








父主题： [网络业务实体配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## NSE保护路由区配置 
## NSE保护路由区配置 


背景知识 


网管配置操作中，路由区配置被异常删除时会导致系统业务如寻呼等出现异常。为避免该误操作，系统绑定了网络业务实体和路由区之间的关系。当该配置关系存在时，被绑定的路由区将不能被删除。该配置仅用于限制网管配置操作行为，避免关联的路由区被删除，不影响系统设备的实际运行。 




功能描述 


该命令用于新增网络业务实体NSE和路由区关联记录，避免该路由区在其他配置中被异常删除。 




相关主题 



 

设置NSE关联路由区(SET NSE RAI)
 

 

删除NSE关联路由区(DEL NSE RAI)
 

 

查询NSE关联路由区(SHOW NSE RAI)
 

 

查询未关联路由区的NSE(SHOW NSE NORAI)
 

 








父主题： [Gb接入配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置NSE关联路由区(SET NSE RAI) 
### 设置NSE关联路由区(SET NSE RAI) 


命令功能 


该命令用于新增NSE和路由区关联记录，即将路由区和NSE绑定，让路由区在数据库中被引用到，避免该路由区在其他配置中被异常删除。 




注意事项 

该配置不传前台，仅用于后台配置保护，防止Gb口在用的路由区被删除，配置的NSE与路由区并没有必然的绑定关系。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN内唯一的标识一个网络业务实体。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。
RANAME|路由区名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|路由区名称，在SGSN内唯一的标识一个路由区。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。






命令举例 


新增路由区名为RAC_NanJing的路由区和1号NSE关联。
 SET NSE RAI: NSEI=1,RANAME="RAC_NanJing";
 








父主题： [NSE保护路由区配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除NSE关联路由区(DEL NSE RAI) 
### 删除NSE关联路由区(DEL NSE RAI) 


命令功能 


该命令用于删除NSE和路由区关联记录。删除时按“NSEI”+“路由区名称”删除，其中，“NSEI”为必填，“路由区名称”可选，如果“路由区名称”不填写，则删除与该NSEI关联的所有路由区信息。 


删除NSE和路由区关联记录后，就可以正常删除路由区配置了。如果系统规划该路由区不再继续使用，需要删除该路由区，则先删除NSE和该路由区关联记录，再删除路由区配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN内唯一的标识一个网络业务实体。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。
RANAME|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|路由区名称，在SGSN内唯一的标识一个路由区。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。






命令举例 


删除路由区名为RAC_NanJing的路由区和1号NSE关联。
 DEL NSE RAI: NSEI=1,RANAME="RAC_NanJing";
 








父主题： [NSE保护路由区配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询NSE关联路由区(SHOW NSE RAI) 
### 查询NSE关联路由区(SHOW NSE RAI) 


命令功能 

该命令用于查询NSE和路由区关联记录信息。系统提供了按“NSE标识号”和“路由区名”两种查询方式，不填写则表示通配查询。执行命令后，系统将显示NSE和路由区关联记录信息。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN内唯一的标识一个网络业务实体。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。
RANAME|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|路由区名称，在SGSN内唯一的标识一个路由区。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN内唯一的标识一个网络业务实体。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。
RAIID|路由区标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|路由区标识，该路由区在SGSN内部的编号，在SGSN内部唯一的标识一个路由区。
RANAME|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|路由区名称，在SGSN内唯一的标识一个路由区。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。






命令举例 


查询和路由区名为RAC_NanJing的路由区和NSE建立关联的记录。
 SHOW NSE RAI:RANAME="RAC_NanJing";
 


`                                                                                                                                                                                                               
                                                                                                                                                                                                                 
命令 (No.1): SHOW NSE RAI:RANAME="RAC_NanJing";

操作维护    NSE标识号   路由区标识   路由区名
---------------------------------------------
修改 删除   1           1            rac_nanjing
---------------------------------------------
记录数 1

命令执行成功（耗时 0.063 秒）。

                                                                                                                                                                                      
` 








父主题： [NSE保护路由区配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询未关联路由区的NSE(SHOW NSE NORAI) 
### 查询未关联路由区的NSE(SHOW NSE NORAI) 


命令功能 

该命令用于查询所有未关联路由区的NSE记录。执行命令后，系统将把所有没有关联绑定RAI的NSE全部显示出来。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN内唯一的标识一个网络业务实体。在NSE保护路由区配置中，可以增加记录，让路由区和NSE绑定，在数据库中让路由区被引用，这样误操作删除路由区操作时，则不会被删除，起到保护路由区不被误删除的作用。
NSE|NSE名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|网络业务实体NSE的名称，在NSE保护路由区配置中，方便系统管理员区分记忆NSE和路由区的关联记录。






命令举例 


查询所有的未关联路由区的NSE记录。
   SHOW NSE NORAI;
 


`                                                                                                                                                                                                               
                                                                                                                                                                                                                 
命令 (No.1): SHOW NSE NORAI;

NSE标识号   NSE名称
-------------------
2           BSC_YangZhou
3           BSC_ShangHai
4           BSC_SuZhou
5           BSC_HangZhou
-------------------
记录数 4

命令执行成功（耗时 0.072 秒）。

                                                                                                                                                                                      
` 








父主题： [NSE保护路由区配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 本端IP端点配置 
## 本端IP端点配置 


背景知识 


要使SGSN能够与基于IP承载的BSC建立连接通路，SGSN必须提供本端IP端点。BSC可以根据该IP端点建立网络业务虚连接。 


本端端点不需要考虑IP承载是静态IP连接还是动态IP连接，它们被所有IP承载的BSC共享。 




功能描述 


当需要与IP承载的BSC对接时，必须进行本端IP端点配置，以提供IP承载方式下BSC和SGSN网元之间通讯及数据传输的通路。 


功能用于增加、删除、修改、显示本端IP端点。 


完整的本端IP端点配置包括以下配置项： 



 


                        配置网络业务实体，参见
                        ADD NSE
                        ，且其承载方式
                        ADD NSE
                        为“IP(IP)”，配置属性
                        ADD NSE
                        可为“静态(Static)”或“动态(Dynamic)”。
                    
 

 


                        配置本端IP端点。假设本端IP地址192.168.1.1及其上的UDP端口40000受IP传输网络支持并且可用。配置命令为：
                        ADD LOCAL ENDPOINT
                        :IPADDR="192.168.1.1",PORT=40000;
                    
 

 




相关主题 



 

新增本端IP端点(ADD LOCAL ENDPOINT)
 

 

修改本端IP端点(SET LOCAL ENDPOINT)
 

 

删除本端IP端点(DEL LOCAL ENDPOINT)
 

 

查询本端IP端点(SHOW LOCAL ENDPOINT)
 

 








父主题： [Gb接入配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增本端IP端点(ADD LOCAL ENDPOINT) 
### 新增本端IP端点(ADD LOCAL ENDPOINT) 


命令功能 


该命令用于增加一个本端IP端点。 


IP端点概念由3GPP TS 48.016协议引入，传统的BSC和SGSN之间的Gb口协议栈，物理承载是采用FR（帧中继）网络承载，引入IP端点后，实现了Gb口协议栈的物理承载IP化。IP端点由IP地址+UDP端口号组成。远端IP端点+本端IP端点构成一条IP NSVC（IP网络业务实体虚连接）通道，即使用<远端IP地址，远端UDP端口号，本端IP地址，本端UDP端口号>这样一个四元组就组成了一条IP NSVC（IP网络业务实体虚连接），对NS上层用户提供基于IP的网络业务虚连接通道。 



当SGSN和BSC对接，采用IP承载时，需要配置本端IP端点，后续才能使用该本端IP端点配置基于IP的网络业务虚连接通道。 




注意事项 

SGSN最多支持16个IPV4的本端IP端点和16个IPV6的本端IP端点。


参数说明 


标识|名称|类型|说明
---|---|---|---
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:必选参数；参数类型:整数；参数范围为:40000~40999。默认值:40000。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。
SIGWEIGHT|信令权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:100。|该参数用于设置该本端端点的信令权重，用于本端IP端点间的信令负荷分担。系统根据各个本端端点的信令权重，按信令权重比例，发送信令消息时按该比例选择本端端点。
DATAWEIGHT|数据权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:100。|该参数用于设置该本端端点的数据权重，用于本端IP端点间的数据负荷分担。系统根据各个本端端点的数据权重，按数据权重比例，发送数据消息时按该比例选择本端端点。
ENDPOINTID|本端IP端点标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|本端IP端点标识，用于在SGSN上唯一的标识一个本端IP端点。如果不配置，则系统自动为该本端IP端点生成一个不重复的标识号，也可以由管理员规划配置，不能重复。






命令举例 


新增一个本端IP端点，IP地址为192.168.1.1，UDP端口号为40000，信令权重100，数据权重100，IP端点标识设置为1。
 ADD LOCAL ENDPOINT:IPADDR="192.168.1.1",PORT=40000,SIGWEIGHT=100,DATAWEIGHT=100,ENDPOINTID=1;
 








父主题： [本端IP端点配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改本端IP端点(SET LOCAL ENDPOINT) 
### 修改本端IP端点(SET LOCAL ENDPOINT) 


命令功能 

该命令用于修改本端IP端点的一些参数，如数据权重、信令权重等。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:必选参数；参数类型:整数；参数范围为:40000~40999。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。
SIGWEIGHT|信令权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于设置该本端端点的信令权重，用于本端IP端点间的信令负荷分担。系统根据各个本端端点的信令权重，按信令权重比例，发送信令消息时按该比例选择本端端点。
DATAWEIGHT|数据权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于设置该本端端点的数据权重，用于本端IP端点间的数据负荷分担。系统根据各个本端端点的数据权重，按数据权重比例，发送数据消息时按该比例选择本端端点。






命令举例 


修改IP地址为192.168.1.1，UDP端口号为40000的本端IP端点，将信令权重修改为50，数据权重修改为50。
 SET LOCAL ENDPOINT:IPADDR="192.168.1.1",PORT=40000,SIGWEIGHT=50,DATAWEIGHT=50;
 








父主题： [本端IP端点配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除本端IP端点(DEL LOCAL ENDPOINT) 
### 删除本端IP端点(DEL LOCAL ENDPOINT) 


命令功能 


该命令用于删除一个本端IP端点，输入本端端点IP地址+本端IP端点UDP端口号，即可删除该本端端点。 


删除本端端点前，需要先通过[DEL IP NSVC]命令删除引用了该本端端点的IP NSVC配置




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:必选参数；参数类型:整数；参数范围为:40000~40999。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。






命令举例 


删除IP地址为192.168.1.1，UDP端口号为40000的本端IP端点。
 DEL LOCAL ENDPOINT: IPADDR =192.168.1.1, PORT =40000;
 








父主题： [本端IP端点配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询本端IP端点(SHOW LOCAL ENDPOINT) 
### 查询本端IP端点(SHOW LOCAL ENDPOINT) 


命令功能 

该命令用于查询所有的本端IP端点的详细信息。执行命令后系统将显示所有的本端IP端点的详细信息。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
ENDPOINTID|本端IP端点标识|参数可选性:任选参数；参数类型:整数。|本端IP端点标识，用于在SGSN上唯一的标识一个本端IP端点。如果不配置，则系统自动为该本端IP端点生成一个不重复的标识号，也可以由管理员规划配置，不能重复。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:任选参数；参数类型:整数。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。
SIGWEIGHT|信令权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置该本端端点的信令权重，用于本端IP端点间的信令负荷分担。系统根据各个本端端点的信令权重，按信令权重比例，发送信令消息时按该比例选择本端端点。
DATAWEIGHT|数据权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置该本端端点的数据权重，用于本端IP端点间的数据负荷分担。系统根据各个本端端点的数据权重，按数据权重比例，发送数据消息时按该比例选择本端端点。






命令举例 


查询所有本端IP端点。
   SHOW LOCAL ENDPOINT;
 


`                                                                                                                                                                                                               
                                                                                                                                                                                                                 
 命令 (No.1): SHOW LOCAL ENDPOINT;

操作维护         本端IP端点标识   IP地址        UDP端口      信令权重   数据权重
--------------------------------------------------------------------------------
复制 修改 删除   1                192.168.1.1   40000        100        100
复制 修改 删除   2                192.168.1.1   40002        100        100
--------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.042 秒）。

                                                                                                                                                                                     
` 








父主题： [本端IP端点配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 远端IP端点配置 
## 远端IP端点配置 


背景知识 


要使SGSN能够与基于IP承载的BSC建立静态的IP连接通路，需要向SGSN提供远端IP端点，即BSC上的本端IP端点。SGSN可以根据该IP端点主动建立网络业务虚连接。 




功能描述 


当需要与静态IP承载的BSC对接时，必须进行远端IP端点配置，以提供静态IP承载方式下BSC和SGSN网元之间通讯及数据传输的通路。 


功能用于增加、删除、修改、显示远端IP端点。 


配置远端IP端点的流程如下： 







                        配置网络业务实体，参见
                        [ADD NSE]
                        ，且其承载方式
                        [ADD NSE]
                        为“IP(IP)”，配置属性
                        [ADD NSE]
                        为“静态(Static)”。
                    







                        配置本端IP端点。假设标识为103的网络业务实体已经配置且和对端BSC协商并达成一致，远端IP地址192.168.2.1及其上的UDP端口40000已由BSC提供并且受IP传输网络支持并且可用。配置命令为：
                        [ADD REMOTE ENDPOINT]
                        :NSEI=103,IPADDR="192.168.2.1",PORT=40000;
                    








相关主题 



 

新增远端IP端点(ADD REMOTE ENDPOINT)
 

 

修改远端IP端点(SET REMOTE ENDPOINT)
 

 

删除远端IP端点(DEL REMOTE ENDPOINT)
 

 

查询远端IP端点(SHOW REMOTE ENDPOINT)
 

 








父主题： [Gb接入配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增远端IP端点(ADD REMOTE ENDPOINT) 
### 新增远端IP端点(ADD REMOTE ENDPOINT) 


命令功能 


该命令用于增加一个本端IP端点。 


IP端点概念由3GPP TS 48.016协议引入，传统的BSC和SGSN之间的Gb口协议栈，物理承载是采用FR（帧中继）网络承载，引入IP端点后，实现了Gb口协议栈的物理承载IP化。IP端点由IP地址+UDP端口号组成。远端IP端点+本端IP端点构成一条IP NSVC（IP网络业务实体虚连接）通道，即使用<远端IP地址，远端UDP端口号，本端IP地址，本端UDP端口号>这样一个四元组就组成了一条IP NSVC（IP网络业务实体虚连接），对NS上层用户提供基于IP的网络业务虚连接通道。 



当SGSN和BSC对接，采用IP承载时，需要配置本端IP端点，后续才能使用该本端IP端点配置基于IP的网络业务虚连接通道。 




注意事项 




SGSN对每个NSE最大支持配置16个远端IP端点，包括IPV4地址类型端点和IPV6地址类型端点总和。 




SGSN最大支持配置16384个远端IP端点，包括IPV4地址类型端点和IPV6地址类型端点总和。 








参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。
SIGWEIGHT|信令权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:100。|该参数用于设置该远端端点的信令权重，用于远端IP端点间的信令负荷分担。系统根据各个远端端点的信令权重，按信令权重比例，发送信令消息时按该比例选择远端端点。
DATAWEIGHT|数据权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:100。|该参数用于设置该远端端点的数据权重，用于远端IP端点间的数据负荷分担。系统根据各个远端端点的数据权重，按数据权重比例，发送数据消息时按该比例选择远端端点。
ENDPOINTID|远端IP端点标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~16384。|远端IP端点标识，用于在SGSN上唯一的标识一个远端IP端点。如果不配置，则系统自动为该远端IP端点生成一个不重复的标识号，也可以由管理员规划配置，不能重复。






命令举例 


在1号NSE下新增一个远端IP端点，IP地址为192.168.1.2，UDP端口号为40000，信令权重100，数据权重100，IP端点标识设置为10。
 ADD REMOTE ENDPOINT:NSEI=1,IPADDR="192.168.1.2",PORT=40000,ENDPOINTID=10;
 








父主题： [远端IP端点配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改远端IP端点(SET REMOTE ENDPOINT) 
### 修改远端IP端点(SET REMOTE ENDPOINT) 


命令功能 

该命令用于修改远端IP端点的一些参数，如数据权重、信令权重等。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。
SIGWEIGHT|信令权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于设置该远端端点的信令权重，用于远端IP端点间的信令负荷分担。系统根据各个远端端点的信令权重，按信令权重比例，发送信令消息时按该比例选择远端端点。
DATAWEIGHT|数据权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于设置该远端端点的数据权重，用于远端IP端点间的数据负荷分担。系统根据各个远端端点的数据权重，按数据权重比例，发送数据消息时按该比例选择远端端点。






命令举例 


修改1号NSE下的IP地址为192.168.1.2，UDP端口号为40000的远端IP端点，信令权重为50，数据权重为50。
 SET REMOTE ENDPOINT:NSEI=1,IPADDR="192.168.1.2",PORT=40000,SIGWEIGHT=50,DATAWEIGHT=50;
 








父主题： [远端IP端点配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除远端IP端点(DEL REMOTE ENDPOINT) 
### 删除远端IP端点(DEL REMOTE ENDPOINT) 


命令功能 


该命令用于删除某个NSE下的远端IP端点。设置需要删除的NSE标识号后，可根据IP地址、UDP端口号、和IP地址+UDP端口号三种条件进行删除。如果不输入任何参数，则表示删除此NSE下的所有远端IP端点配置信息。 


删除远端端点前，需要先通过[DEL IP NSVC]命令删除引用了该远端端点的IP NSVC配置。




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。






命令举例 


删除1号NSE下的IP地址为192.168.1.2，UDP端口号为40000的远端IP端点。
 DEL REMOTE ENDPOINT:NSEI=1,IPADDR="192.168.1.2",PORT=40000;
 








父主题： [远端IP端点配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询远端IP端点(SHOW REMOTE ENDPOINT) 
### 查询远端IP端点(SHOW REMOTE ENDPOINT) 


命令功能 

该命令用于查询远端IP端点的详细信息。可以根据NSE标识号、IP地址和UDP端口号三种条件方式进行查询。如果不输入任何参数，则显示所有的远端IP端点的详细信息。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ENDPOINTID|远端IP端点标识|参数可选性:任选参数；参数类型:整数。|远端IP端点标识，用于在SGSN上唯一的标识一个远端IP端点。如果不配置，则系统自动为该远端IP端点生成一个不重复的标识号，也可以由管理员规划配置，不能重复。
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的IP地址。
PORT|UDP端口|参数可选性:任选参数；参数类型:整数。|IP端点由IP地址+UDP端口号组成，该参数用于配置该IP端点对应的UDP端口号。
SIGWEIGHT|信令权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置该远端端点的信令权重，用于远端IP端点间的信令负荷分担。系统根据各个远端端点的信令权重，按信令权重比例，发送信令消息时按该比例选择远端端点。
DATAWEIGHT|数据权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置该远端端点的数据权重，用于远端IP端点间的数据负荷分担。系统根据各个远端端点的数据权重，按数据权重比例，发送数据消息时按该比例选择远端端点。
VPNID|VRF 标识|参数可选性:任选参数；参数类型:整数。|VRF标识，请参见ADD NSE。






命令举例 


查询1号NSE下的IP地址为192.168.1.2，UDP端口号为40000的远端IP端点的详细信息。
 SHOW REMOTE ENDPOINT:NSEI=1,IPADDR="192.168.1.2",PORT=40000;
 


`                                                                                                                                                                                                               
                                                                                                                                                                                                                 
 命令 (No.1): SHOW REMOTE ENDPOINT:NSEI=1,IPADDR="192.168.1.2",PORT=40000;

操作维护         远端IP端点标识   NSE标识号    IP地址        UDP端口      信令权重   数据权重   VRF 标识
--------------------------------------------------------------------------------------------------------
复制 修改 删除   10               1            192.168.1.2   40000        100        100        0
--------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.078 秒）。

                                                                                                                                                                                     
` 








父主题： [远端IP端点配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## IP网络业务虚连接配置 
## IP网络业务虚连接配置 


背景知识 


基于静态IP承载的网络业务虚连接（NSVC），与本端IP端点和远端IP端点关联后可以使用，它提供BSC和SGSN之间的链路级通路。 




功能描述 


当需要与静态IP承载的BSC对接时，必须进行IP网络业务虚连接配置。 


功能用于增加、删除、修改、查询静态IP网络业务虚连接。 


配置IP网络业务虚连接的流程如下： 







                        配置本端IP端点，参见
                        [ADD LOCAL ENDPOINT]
                        。
                    







                        配置远端IP端点，参见
                        [ADD REMOTE ENDPOINT]
                        。
                    







                        配置网络业务实体，参见
                        [ADD NSE]
                        。
                    







                        配置IP网络业务虚连接。假设网络业务实体标识为102的网络业务实体已经配置，标识号为1的本端IP端点和远端IP端点已经配置。配置命令为：
                        [ADD IP NSVC]
                        :NSEI=102,LIPPORTID=1,RIPPORTID=1;
                    







                注意：本端IP端点和远端IP端点的标识号分别在SGSN内唯一，可以在其配置命令参数中显式指定，也可以不指定而由系统自动分配。一个配置命令中可以同时提供多个本端IP端点和远端IP端点。当提供多个IP端点且连接方式
                [ADD IP NSVC]
                为“单一(SINGLE)”时，本端IP端点和远端IP端点的个数应该相同，它用来建立本端IP端点和远端IP端点之间一对一的连接。否则两者个数可以不同，用来建立本端IP端点和远端IP端点之间多对多的连接。
            




相关主题 



 

新增IP网络业务虚连接(ADD IP NSVC)
 

 

删除IP网络业务虚连接(DEL IP NSVC)
 

 

查询IP网络业务虚连接(SHOW IP NSVC)
 

 








父主题： [Gb接入配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增IP网络业务虚连接(ADD IP NSVC) 
### 新增IP网络业务虚连接(ADD IP NSVC) 


命令功能 


该命令用于当NSE采用IP承载时，在SGSN上增加IP网络业务虚拟连接IP NSVC配置。在IP承载时，通过配置IP NSVC，建立NS对等层之间的端到端的虚连接链路，使SGSN和BSC的NS对等层之间能够进行通信。 


IP NSVC由本端IP端点+远端IP端点组成，即由本端IP地址、本端UDP端口号、远端IP地址和远端UDP端口号组成。 


增加IP NSVC配置，系统提供了单一增加和枚举增加两种方式。 



 
单一增加是指配置相同个数的本端端点和远端端点，系统按顺序，对应顺序上的一个本端端点和一个远端端点组合成一条IP NSVC。
 

 
枚举增加是指配置的本端端点个数和远端端点个数可以相等也可以不相等，认为每个本端端点要和所有的远端端点组合生成多条IP
NSVC。把这些本端端点和远端端点自动完全组合，生成多条IP NSVC。
 

 




注意事项 




SGSN对每个NSE最大支持128条NSVC。 




SGSN最大支持40960条IP承载的NSVC。 








参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
LIPPORTID|本端IP端点标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|本端IP端点标识，请参见ADD LOCAL ENDPOINT。
RIPPORTID|远端IP端点标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~16384。|远端IP端点标识，请参见ADD REMOTE ENDPOINT。
MODE|连接方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:SINGLE。|增加IP NSVC配置，系统提供了单一增加和枚举增加两种方式。单一增加是指配置相同个数的本端端点和远端端点，系统按顺序，对应顺序上的一个本端端点和一个远端端点组合成一条IP NSVC。枚举增加是指配置的本端端点个数和远端端点个数可用相等也可用不相等，认为每个本端端点要和所有的远端端点组合生成多条IP NSVC。把这些本端端点和远端端点自动完全组合，生成多条IP NSVC。取值含义：单一（SINGLE）：系统采用单一方式增加IP NSVC。枚举（ENUMBERATE）：系统采用枚举组合方式增加IP NSVC。






命令举例 


在1号NSE下新增加IP网络业务虚连接，选择本端端点1和本端端点2，远端端点11和远端端点12，按单个方式增加。命令执行后，系统会生成2条IP NSVC，分别为<本端端点1，远端端点11>和<本端端点2，远端端点12>。
 ADD IP NSVC:NSEI=1,LIPPORTID=1&2,RIPPORTID=11&12,MODE="SINGLE";
 








父主题： [IP网络业务虚连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除IP网络业务虚连接(DEL IP NSVC) 
### 删除IP网络业务虚连接(DEL IP NSVC) 


命令功能 


该命令用于删除IP网络业务虚连接。可以按本端IP端点删除、按远端IP端点删除、按本端IP端点+远端IP端点三种方式删除，对应的参数不填写，就表示通配删除。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
LIPPORTID|本端IP端点标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|本端IP端点标识，请参见ADD LOCAL ENDPOINT。
RIPPORTID|远端IP端点标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~16384。|远端IP端点标识，请参见ADD REMOTE ENDPOINT。






命令举例 


需要删除1号NSE下本端端点为1，远端端点为11的这条IP NSVC配置。
 DEL IP NSVC:NSEI=1,LIPPORTID=1,RIPPORTID=11;
 








父主题： [IP网络业务虚连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询IP网络业务虚连接(SHOW IP NSVC) 
### 查询IP网络业务虚连接(SHOW IP NSVC) 


命令功能 

该命令用于查询IP网络业务虚连接的详细信息，可以按NSE查询、按本端IP端点查询、按远端IP端点查询三种方式，如果不输入任何参数，则删除所有的IP网络业务虚连接配置。执行命令后系统将显示查询的IP网络业务虚拟连接的详细信息。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
LIPPORTID|本端IP端点标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|本端IP端点标识，请参见ADD LOCAL ENDPOINT。
RIPPORTID|远端IP端点标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~16384。|远端IP端点标识，请参见ADD REMOTE ENDPOINT。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
NSVCID|IP网络业务虚连接ID|参数可选性:任选参数；参数类型:整数。|IP网络业务虚连接标识，在一个网络业务实体NSE下唯一的标识一条IP网络业务虚连接（IP NSVC，IP Network Service Virtual Connection）。
NSEI|NSE标识号|参数可选性:任选参数；参数类型:整数。|NSE标识号，在SGSN上唯一标识一个网络业务实体NSE。
LIPPORTID|本端IP端点标识|参数可选性:任选参数；参数类型:整数。|本端IP端点标识，请参见ADD LOCAL ENDPOINT。
LIPADDR|本端IP地址|参数可选性:任选参数；参数类型:字符型。|本端IP地址，请参见ADD LOCAL ENDPOINT。
LPORT|本端UDP端口|参数可选性:任选参数；参数类型:整数。|本端本端UDP端口，请参见ADD LOCAL ENDPOINT。
LSIGWEIGHT|本端信令权重|参数可选性:任选参数；参数类型:整数。|本端信令权重，请参见ADD LOCAL ENDPOINT。
LDATAWEIGHT|本端数据权重|参数可选性:任选参数；参数类型:整数。|本端数据权重，请参见ADD LOCAL ENDPOINT。
RIPPORTID|远端IP端点标识|参数可选性:任选参数；参数类型:整数。|远端IP端点标识，请参见ADD REMOTE ENDPOINT。
RIPADDR|远端IP地址|参数可选性:任选参数；参数类型:字符型。|远端IP地址，请参见ADD REMOTE ENDPOINT。
RPORT|远端UDP端口|参数可选性:任选参数；参数类型:整数。|远端UDP端口，请参见ADD REMOTE ENDPOINT。
RSIGWEIGHT|远端信令权重|参数可选性:任选参数；参数类型:整数。|远端信令权重，请参见ADD REMOTE ENDPOINT。
RDATAWEIGHT|远端数据权重|参数可选性:任选参数；参数类型:整数。|远端数据权重，请参见ADD REMOTE ENDPOINT。
VPNID|VRF 标识|参数可选性:任选参数；参数类型:整数。|VRF 标识，请参见ADD NSE。






命令举例 


查询1号NSE下本端端点为1，远端端点为11的这条IP NSVC配置信息。
SHOW IP NSVC:NSEI=1,LIPPORTID=1,RIPPORTID=11; 


`                                                                                                                                                                                                               
                                                                                                                                                                                                                 
命令 (No.1): SHOW IP NSVC:NSEI=1,LIPPORTID=1,RIPPORTID=11;

操作维护    IP网络业务虚连接ID   NSE标识号   本端IP端点标识   本端IP地址    本端UDP端口   本端信令权重   本端数据权重   远端IP端点标识   远端IP地址    远端UDP端口   远端信令权重   远端数据权重   VRF 标识
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 删除   1                    1           1                192.168.1.1   40000         100            100            11               192.168.1.2   40001         100            100            0
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.052 秒）。

                                                                                                                                                                                     
` 








父主题： [IP网络业务虚连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## Gb口网络管理 
## Gb口网络管理 


背景知识 


Gb口网络管理主要是指SGSN全局性的Gb口传输流量的的控制和管理。与Gb口网络管理相关的协议标准可以参考3GPP 48.018第10.4节。 




功能描述 


功能用于开启或关闭SGSN全局范围的Gb口流控开关。Gb口流控有三个级别：小区级别（BVC）、用户级别（MS）、分组流级别（PFC）。开启Gb口流控有助于减少过量的无效下行用户数据，减少上行LLC-DISCARDED消息，减轻BSC负荷，提升无线指标。 


目前SGSN设备仅支持用户级别的Gb口流控。其配置开关打开后，网络业务实体配置的基于MS的流控才能生效。开关关闭后所有网络业务实体配置的基于MS的流控功能都将被禁止。 




相关主题 



 

设置MS流控特性(SET BGPFCM)
 

 

查询MS流控特性(SHOW BGPFCM)
 

 








父主题： [Gb接入配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置MS流控特性(SET BGPFCM) 
### 设置MS流控特性(SET BGPFCM) 


命令功能 


该命令用于设置是否启用MS流控特性功能。当运营商需要在SGSN中配置MS流控特性时，使用该命令。配置成功后，SGSN能够根据BSC下发的流控参数进行控制或者不控制。功能开启时，SGSN支持根据BSC下发给SGSN的FLOW-CONTROL-MS中携带的流控参数，对用户的下行数据进行流量控制，超过速率的下行报文被丢弃。否则不进行控制，收到的下行报文全部发送给BSC。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
FCM_E|启用MS流控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数用于指示SGSN是否支持Flow-Control-MS功能。取值含义：是（YES）：支持MS流控，即SGSN支持根据BSC下发给SGSN的FLOW-CONTROL-MS中携带的流控参数，对用户的下行数据进行流量控制，超过速率的下行报文被丢弃。否（NO）：不支持MS流控，即SGSN不支持根据BSC下发给SGSN的FLOW-CONTROL-MS中携带的流控参数，不会对用户的下行数据进行流量控制。






命令举例 


关闭SGSN对MS流控的支持
SET BGPFCM:FCM_E="NO"; 








父主题： [Gb口网络管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MS流控特性(SHOW BGPFCM) 
### 查询MS流控特性(SHOW BGPFCM) 


命令功能 


查询是否启用MS流控特性功能，不带参数，查询结果以“YES”或“NO”的结果呈现。 




注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
FCM_E|启用MS流控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数用于指示SGSN是否支持Flow-Control-MS功能。取值含义：是（YES）：支持MS流控，即SGSN支持根据BSC下发给SGSN的FLOW-CONTROL-MS中携带的流控参数，对用户的下行数据进行流量控制，超过速率的下行报文被丢弃。否（NO）：不支持MS流控，即SGSN不支持根据BSC下发给SGSN的FLOW-CONTROL-MS中携带的流控参数，不会对用户的下行数据进行流量控制。






命令举例 


查询MS流控特性配置
SHOW BGPFCM; 


`

命令 (No.1): SHOW BGPFCM;

操作维护  启用MS流控
--------------------
修改      否
--------------------
记录数 1

命令执行成功（耗时 0.125 秒）。
` 








父主题： [Gb口网络管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SGs口配置 
# SGs口配置 


背景知识 

            
            随着移动通讯系统演进到EPS系统，为了运营商利用原有的2G和3G的基础设备提供语音、CS定位（LCS）等业务，引入了CSFB（CS fallback）功能，CSFB功能允许终端通过GERAN或者UTRAN接入到CS域。引入CSFB（CS fallback）功能后，系统需要和MSC/VLR通讯，因此增加SGs口的消息处理流程。SGs接口和GPRS/UMTS系统中的Gs接口的功能类似。
        


功能描述 


SGs接口用于EPS系统和CS域的移动性管理和寻呼。同时，用来传输MO-SMS（短信起呼业务）和MT-SMS（短信终呼业务），因而需要在EPS系统中设置SGs口的相关配置数据。 


配置SGs数据的大致流程如下： 







                        配置到MSC/VLR的SCTP连接。 配置命令参见
                        [ADD SCTP]
                        ;
                    







                        配置SGs连接。配置命令参见
                        [ADD SGSCONN]
                        ;
                    







                        配置SGs路由。配置命令参见
                        [ADD SGS ROUTE]
                        ;
                    







                        配置路由组。 配置命令参见
                        [ADD SGS ROUTE GROUP]
                        ;
                    







                        配置局向路由组。配置命令参见
                        [ADD SGS OFFICE ROUTE GROUP]
                        ;
                    








相关主题 



 

SGs基本配置
 

 

SGs连接路由配置
 

 

SGs与EMM拒绝原因映射配置
 

 

SGs口VLR POOL管理
 

 

基于IMSI的SGs口控制配置
 

 

基于APN的SGs口控制配置
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGs基本配置 
## SGs基本配置 


背景知识 

            
            随着移动通讯系统演进到EPS系统，为了运营商利用原有的2G和3G的基础设备提供语音、CS定位（LCS）等业务，引入了CSFB（CS fallback）功能，CSFB功能允许终端通过GERAN或者UTRAN接入到CS域。引入CSFB（CS fallback）功能后，系统需要和MSC/VLR通讯，因此增加SGs口的消息处理流程。SGs接口和GPRS/UMTS系统中的Gs接口的功能类似。为了确保SGs口消息发送的可靠性，3GPP TS 29.118协议中定义了消息重发的机制，SGs基本配置用于完成消息重发相关参数的配置。
        


功能描述 


本功能用于设置SGs口的4个重发计数器的取值，完成消息重发参数的配置。
其中Ns8是EPS Detach Request消息的重发计数器；Ns9是IMSI Detach Request消息的重发计数器；Ns10是Implicit IMSI Detach Request消息的重发计数器；Ns12是MME Reset消息的重发计数器。 


SGs基本配置的流程如下： 







                        启用SGs口支持开关。 配置命令参见
                        [SET SGSFLAG]
                        ;
                    







                        启用SGs口支持MME-Reset开关。 配置命令参见
                        [SET SOFTWARE PARAMETER]
                        ;
                    







                        配置SGs基本配置。 配置命令参见
                        [SET SGSDATA]
                        ;
                    








相关主题 



 

设置SGs基本参数配置(SET SGSDATA)
 

 

查询SGs基本参数配置(SHOW SGSDATA)
 

 








父主题： [SGs口配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置SGS基本参数配置(SET SGSDATA) 
### 设置SGS基本参数配置(SET SGSDATA) 


命令功能 


本命令用于设置SGs口的以下4个消息重发次数。 



 
Ns8：是显式EPS去附着请求消息重发次数。
 

 
Ns9：是显式IMSI显性去附着请求消息重发次数。
 

 
Ns10：是隐式IMSI去附着请求消息重发次数。
 

 
Ns12：是MME重启指示消息重发次数。
 

 


当需要配置MME与MSC/VLR对接参数时，执行该命令。 




注意事项 

建议使用默认值，一般情况下不修改


参数说明 


标识|名称|类型|说明
---|---|---|---
NS8|Ns8次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数表示显式EPS去附着请求重发次数。异常情况下，MME如果没有收到对端的EPS去附着响应时，MME需要重新发送EPS去附着请求，通过该参数控制MME最大发送EPS去附着请求的次数，该参数在3GPP TS 29.118中5.4.2.3描述。
NS9|Ns9次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数表示MME发送显式IMSI去附着请求重发次数。异常情况下，MME如果没有收到对端的显式IMSI去附着响应时，MME需要重新发送IMSI去附着请求，通过该参数控制MME在最大发送显式IMSI去附着请求的次数，该参数在3GPP TS 29.118 5.5.2.3中描述。
NS10|Ns10次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数表示隐式IMSI去附着请求重发次数。异常情况下，MME如果没有收到对端的IMSI隐式去附着响应时，MME需要重新发送IMSI隐式去附着请求，通过该参数控制MME在最大发送隐式IMSI去附着请求的次数，该参数在3GPP TS 29.118 5.6.2中描述。
NS12|Ns12次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数表示MME重启重发次数。异常情况下，MME如果没有收到对端的重启响应消息时，MME需要重新发送重启指示消息，通过该参数控制MME在最大发送重启指示消息的次数，该参数在3GPP TS 29.118 5.8.2.3中描述。






命令举例 


设置Ns8次数为1、Ns9次数为2、Ns10次数为3、Ns12次数为4。
SET SGSDATA:NS8=1,NS9=2,NS10=3,NS12=4; 








父主题： [SGs基本配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGS基本参数配置(SHOW SGSDATA) 
### 查询SGS基本参数配置(SHOW SGSDATA) 


命令功能 

该命令用于查询SGS基本参数配置，包括显式EPS去附着请求消息重发次数、显式IMSI显性去附着请求消息重发次数、隐式IMSI去附着请求消息重发次数和MME重启指示消息重发次数。


注意事项 

无


输出参数说明 


标识|名称|类型|说明
---|---|---|---
NS8|Ns8次数|参数可选性:任选参数；参数类型:整数。|该参数表示显式EPS去附着请求重发次数。异常情况下，MME如果没有收到对端的EPS去附着响应时，MME需要重新发送EPS去附着请求，通过该参数控制MME最大发送EPS去附着请求的次数，该参数在3GPP TS 29.118中5.4.2.3描述。
NS9|Ns9次数|参数可选性:任选参数；参数类型:整数。|该参数表示MME发送显式IMSI去附着请求重发次数。异常情况下，MME如果没有收到对端的显式IMSI去附着响应时，MME需要重新发送IMSI去附着请求，通过该参数控制MME在最大发送显式IMSI去附着请求的次数，该参数在3GPP TS 29.118 5.5.2.3中描述。
NS10|Ns10次数|参数可选性:任选参数；参数类型:整数。|该参数表示隐式IMSI去附着请求重发次数。异常情况下，MME如果没有收到对端的IMSI隐式去附着响应时，MME需要重新发送IMSI隐式去附着请求，通过该参数控制MME在最大发送隐式IMSI去附着请求的次数，该参数在3GPP TS 29.118 5.6.2中描述。
NS12|Ns12次数|参数可选性:任选参数；参数类型:整数。|该参数表示MME重启重发次数。异常情况下，MME如果没有收到对端的重启响应消息时，MME需要重新发送重启指示消息，通过该参数控制MME在最大发送重启指示消息的次数，该参数在3GPP TS 29.118 5.8.2.3中描述。






命令举例 


查询SGS基本参数配置，包括显式EPS去附着请求消息重发次数、显式IMSI显性去附着请求消息重发次数、隐式IMSI去附着请求消息重发次数和MME重启指示消息重发次数。
SHOW SGSDATA; 


`
命令 (No.1): SHOW SGSDATA

操作维护  Ns8次数   Ns9次数   Ns10次数   Ns12次数
-------------------------------------------------
修改      2         2         2          2
-------------------------------------------------
记录数 1

命令执行成功（耗时 0.033 秒）。
` 








父主题： [SGs基本配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGs连接路由配置 
## SGs连接路由配置 


背景知识 

            
            随着移动通讯系统演进到EPS系统，为了运营商利用原有的2G和3G的基础设备提供语音、CS定位（LCS）等业务，引入了CSFB（CS fallback）功能，CSFB功能允许终端通过GERAN或者UTRAN接入到CS域。引入CSFB（CS Fallback）功能后，系统需要和MSC/VLR通讯，因此增加SGs口的消息处理流程。SGs接口和GPRS/UMTS系统中的Gs接口的功能类似。SGs配置中包含SGs连接和SGs路由两部分，前者确定了MME和MSC/VLR间的连接关系，后者确定了MME到MSC/VLR的连接选择方式。
        


功能描述 


本功能用于配置MME到MSC/VLR局向的路由组以及路由的相关配置，可以达到灵活路由的目的。 


配置SGs口的连接路由数据的大致流程如下： 







                        配置到MSC/VLR的SCTP连接。 配置命令参见
                        [ADD SCTP]
                        ;
                    







                        配置SGs连接。配置命令参见
                        [ADD SGSCONN]
                        ;
                    







                        配置SGs路由。配置命令参见
                        [ADD SGS ROUTE]
                        ;
                    







                        配置路由组。 配置命令参见
                        [ADD SGS ROUTE GROUP]
                        ;
                    







                        配置局向路由组。配置命令参见
                        [ADD SGS OFFICE ROUTE GROUP]
                        ;
                    








相关主题 



 

SGs连接配置
 

 

SGs路由配置
 

 

SGs路由组配置
 

 

SGs局向路由组配置
 

 








父主题： [SGs口配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs连接配置 
### SGs连接配置 


背景知识 

            
            SGs连接配置用于确定MME和MSC/VLR的连接关系，被SGs路由配置所引用，另外SGs口采用SCTP连接作为底层通讯协议。
        


功能描述 


本功能用于设置SGs口连接所对应的SCTP连接，被SGs路由配置所引用。 


配置SGs口连接的流程如下： 






配置到MSC/VLR的SCTP连接; 







                        配置SGs连接。配置命令参见
                        [ADD SGSCONN]
                        ;
                    








相关主题 



 

新增SGs连接配置(ADD SGSCONN)
 

 

修改SGs连接配置(SET SGSCONN)
 

 

删除SGs连接配置(DEL SGSCONN)
 

 

查询SGs连接配置(SHOW SGSCONN)
 

 








父主题： [SGs连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增SGS连接配置(ADD SGSCONN) 
#### 新增SGS连接配置(ADD SGSCONN) 


命令功能 

该命令用于新增一条SGs连接，将其与SGs偶联相关联。执行该命令后，该SGs连接所关联的SGs 偶联才会发起底层SCTP建链。


注意事项 



 
执行该命令前通常需要先配置SGs偶联。
 

 
SGs连接与SGs偶联是一一对应的。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SGS连接编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2047。|该参数用于标识一条SGs连接，该标识要求全局唯一。
SCTPID|SCTP连接标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|目前MME同MSC/VLR交互的协议是承载在SCTP上的，该参数用于指示该SGs连接关联的SGs偶联。
NAME|SGS连接名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示配置的SGs连接别名。






命令举例 


新增SGs连接配置，设置SGs连接编号为1，其关联的SCTP连接标识为1。
ADD SGSCONN:ID=1,SCTPID=1,; 








父主题： [SGs连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改SGS连接配置(SET SGSCONN) 
#### 修改SGS连接配置(SET SGSCONN) 


命令功能 

该命令用于修改SGs连接配置。执行该命令可以修改SGs连接关联的SGs偶联。


注意事项 

SGs连接与SGs偶联是一一对应的。


参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SGS连接编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2047。|该参数用于标识一条SGs连接，该标识要求全局唯一。
SCTPID|SCTP连接标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|目前MME同MSC/VLR交互的协议是承载在SCTP上的，该参数用于指示该SGs连接关联的SGs偶联。
NAME|SGS连接名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示配置的SGs连接别名。






命令举例 


修改SGs连接编号为1的SGs连接配，将其关联的SCTP连接标识修改为1。
SET SGSCONN:ID=1,SCTPID=1; 








父主题： [SGs连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除SGS连接配置(DEL SGSCONN) 
#### 删除SGS连接配置(DEL SGSCONN) 


命令功能 

该命令用于删除SGs连接配置，执行该命令可以去除SGs连接与SGs偶联的关联关系。


注意事项 

执行该命令前需要先删除SGs路由，以确保删除的SGs连接没有被SGs路由关联。查询命令参见[SHOW SGS ROUTE]。


参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SGS连接编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2047。|该参数用于标识一条SGs连接，该标识要求全局唯一。






命令举例 


删除SGs连接编号为1的SGs连接配置。
DEL SGSCONN:ID=1; 








父主题： [SGs连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGS连接配置(SHOW SGSCONN) 
#### 查询SGS连接配置(SHOW SGSCONN) 


命令功能 

该命令用于查询SGs连接配置，主要查询该SGs连接关联的SGs偶联。


注意事项 



 
该命令不带参数，可查询所有的SGs连接配置记录。
 

 
该命令也可根据SGs连接编号查询与之匹配的记录。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SGS连接编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2047。|该参数用于标识一条SGs连接，该标识要求全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|SGS连接编号|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条SGs连接，该标识要求全局唯一。
SCTPID|SCTP连接标识|参数可选性:任选参数；参数类型:整数。|目前MME同MSC/VLR交互的协议是承载在SCTP上的，该参数用于指示该SGs连接关联的SGs偶联。
NAME|SGS连接名称|参数可选性:任选参数；参数类型:字符型。|该参数表示配置的SGs连接别名。






命令举例 


查询所有的SGs连接配置。
SHOW SGSCONN; 


`命令 (No.1): SHOW SGSCONN

操作维护         SGS连接编号   SCTP连接标识   SGS连接名称
---------------------------------------------------------
复制 修改 删除   6             6              
---------------------------------------------------------
记录数 1

命令执行成功（耗时 0.033 秒）。

` 








父主题： [SGs连接配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs路由配置 
### SGs路由配置 


背景知识 

            
            SGs路由用于确定MME到MSC/VLR的SGs连接的选择方式，系统支持备份和负荷分担两种选路方式，一般来说到一个MSC/VLR配置两条负荷分担的SGs连接即可。
        


功能描述 


本功能用于设置SGs口连接的选择方式，系统支持N+M备份和负荷分担两种选路方式。配置为N+M备份方式则在该路由中前N条可用的SGs连接中轮选出局链路；配置为负荷分担方式则在该路由中所有可用的SGs连接中轮选出局链路。 


配置SGs口路由的流程如下： 







                        配置到MSC/VLR的SCTP连接。 配置命令参见
                        [ADD SCTP]
                        ;
                    







                        配置SGs连接。 配置命令参见
                        [ADD SGSCONN]
                        ;
                    







                        配置SGs路由。 配置命令参见
                        [ADD SGS ROUTE]
                        ;
                    








相关主题 



 

新增SGs路由配置(ADD SGS ROUTE)
 

 

修改SGs路由配置(SET SGS ROUTE)
 

 

删除SGs路由配置(DEL SGS ROUTE)
 

 

查询SGs路由配置(SHOW SGS ROUTE)
 

 








父主题： [SGs连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增SGs路由配置(ADD SGS ROUTE) 
#### 新增SGs路由配置(ADD SGS ROUTE) 


命令功能 

该命令用于新增一条SGs路由，将其与SGs连接相关连。执行该命令后，可以将配置的SGs连接关联到该路由中。


注意事项 



 
该命令执行前，需要先配置SGs 连接。 配置命令参见ADD SGSCONN。
 

 
每个SGs路由最多可以关联8个SGs连接。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由，该参数是全局唯一的。
PARTAKEMODE|分担方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表明该SGs路由的负荷分担属性。取值含义如下所示。“BACKUP”：该SGs路由工作方式是N+M主备方式 。“PARTAKE”：该SGs路由工作方式是负荷分担方式。
CONNECTION|连接编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2047。|该参数用于指示该SGs路由关联的SGS连接编号，SGs连接配置参见SHOW SGSCONN。
MSTERNUM|主用连接编号个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~8。|该参数用于指示该SGs路由关联的SGs连接中主用连接的个数。只有当配置分担方式为N+M主备方式才可以配置该参数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置SGs路由的别名。






命令举例 


新增SGs路由配置，设置其标识为1，分担方式为N＋M备份，关联的SGs连接编号为1，主用连接编号个数为1。
ADD SGS ROUTE:ROUTEID=1,PARTAKEMODE="BACKUP",CONNECTION=1,MSTERNUM=1; 








父主题： [SGs路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改SGs路由配置(SET SGS ROUTE) 
#### 修改SGs路由配置(SET SGS ROUTE) 


命令功能 

该命令用于修改SGs路由配置，包括SGs路由关联的SGs连接、SGs路由的分担方式及主用连接的个数。


注意事项 

每个SGs路由最多可以关联8个SGs连接。


参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由，该参数是全局唯一的。
PARTAKEMODE|分担方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该SGs路由的负荷分担属性。取值含义如下所示。“BACKUP”：该SGs路由工作方式是N+M主备方式 。“PARTAKE”：该SGs路由工作方式是负荷分担方式。
CONNECTION|连接编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2047。|该参数用于指示该SGs路由关联的SGS连接编号，SGs连接配置参见SHOW SGSCONN。
MSTERNUM|主用连接编号个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~8。|该参数用于指示该SGs路由关联的SGs连接中主用连接的个数。只有当配置分担方式为N+M主备方式才可以配置该参数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置SGs路由的别名。






命令举例 


修改路由标识为1的SGs路由配置，将分担方式修改为负荷分担。
SET SGS ROUTE:ROUTEID=1,PARTAKEMODE="PARTAKE",CONNECTION=1; 








父主题： [SGs路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除SGs路由配置(DEL SGS ROUTE) 
#### 删除SGs路由配置(DEL SGS ROUTE) 


命令功能 

该命令用于删除SGs路由配置。执行该命令可以去除SGs路由与SGs连接的关联关系。


注意事项 

执行该命令前通常需要执行删除SGs路由组操作，以确保删除的SGs路由没有被SGs路由组关联。 查询命令参见[SHOW SGS ROUTE GROUP]。


参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由，该参数是全局唯一的。






命令举例 


删除路由标识为1的SGs路由配置。
DEL SGS ROUTE:ROUTEID=1; 








父主题： [SGs路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGs路由配置(SHOW SGS ROUTE) 
#### 查询SGs路由配置(SHOW SGS ROUTE) 


命令功能 

该命令用于查询SGs路由配置，主要查询该SGs路由关联的SGs连接、分担方式、主用连接个数等。


注意事项 



 
该命令不带参数，可查询所有的SGs路由配置记录。
 

 
该命令也可根据SGs路由标识查询与之匹配的记录
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|路由ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由，该参数是全局唯一的。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEID|路由ID|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条SGs路由，该参数是全局唯一的。
PARTAKEMODE|分担方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该SGs路由的负荷分担属性。取值含义如下所示。“BACKUP”：该SGs路由工作方式是N+M主备方式 。“PARTAKE”：该SGs路由工作方式是负荷分担方式。
CONNECTION|连接编号|参数可选性:任选参数；参数类型:字符型。|该参数用于指示该SGs路由关联的SGS连接编号，SGs连接配置参见SHOW SGSCONN。
MSTERNUM|主用连接编号个数|参数可选性:任选参数；参数类型:整数。|该参数用于指示该SGs路由关联的SGs连接中主用连接的个数。只有当配置分担方式为N+M主备方式才可以配置该参数。
BACKUPNUM|备用连接编号个数|参数可选性:任选参数；参数类型:整数。|该参数用于指示该SGs路由关联的SGs连接中备用连接的个数。只有当配置分担方式为N+M主备方式时该参数才有效。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|配置SGs路由的别名。






命令举例 


查询所有的SGs路由配置。
SHOW SGS ROUTE; 


`命令 (No.1): SHOW SGS ROUTE

操作维护         路由ID   分担方式   连接编号   主用连接编号个数   备用连接编号个数   用户别名
----------------------------------------------------------------------------------------------
复制 修改 删除   6        N+M备份    6          1                  0                  
----------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。

` 








父主题： [SGs路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs路由组配置 
### SGs路由组配置 


背景知识 

            
            为了达到灵活选择出局链路的目的，系统引入了SGs路由组的配置，用于配置SGs路由的选择方式。
        


功能描述 


本功能用于设置SGs口路由组中路由的选择方式，SGs路由组中可以包含多个SGs路由，各个SGs路由之间可以是N+M备份或者负荷分担的工作方式。 


配置SGs路由组的流程如下： 







                        配置到MSC/VLR的SCTP连接。 配置命令参见
                        [ADD SCTP]
                        ;
                    







                        配置SGs连接。 配置命令参见
                        [ADD SGSCONN]
                        ;
                    







                        配置SGs路由。 配置命令参见
                        [ADD SGS ROUTE]
                        ;
                    







                        配置SGs路由组。 配置命令参见
                        [ADD SGS ROUTE GROUP]
                        ;
                    








配置流程说明 



 


                        首先配置到MSC/VLR的SCTP连接。 配置命令为：
                        ADD SCTP
                        ;
                    
 

 


                        然后配置SGs连接。 配置命令为：
                        ADD SGSCONN
                        :ID=1,SCTPID=1,NAME="SGs1";
                    
 

 


                        然后配置路由。 配置命令为：
                        ADD SGS ROUTE
                        :ROUTEID=1,PARTAKEMODE="BACKUP",CONNECTION=1&2&3&4,MSTERNUM=2,NAME="SGs";
                    
 

 


                        然后配置路由组。 配置命令为：
                        ADD SGS ROUTE GROUP
                        :ROUTEGRPID=1,PARTAKEMODE="BACKUP",ROUTE=1&2&3&4,MSTERNUM=2,NAME="SGs";
                    
 

 




相关主题 



 

新增SGs路由组配置(ADD SGS ROUTE GROUP)
 

 

修改SGs路由组配置(SET SGS ROUTE GROUP)
 

 

删除SGs路由组配置(DEL SGS ROUTE GROUP)
 

 

查询SGs路由组配置(SHOW SGS ROUTE GROUP)
 

 








父主题： [SGs连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增SGs路由组配置(ADD SGS ROUTE GROUP) 
#### 新增SGs路由组配置(ADD SGS ROUTE GROUP) 


命令功能 

该命令用于新增一条SGs路由组，将其与SGs路由相关联。执行该命令后，可以将配置的SGs路由关联到该路由组中。


注意事项 



 
该命令执行前，需要先配置SGs 路由。 配置命令参见ADD SGS ROUTE。
 

 
每个SGs路由组最多可以关联8个SGs路由。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由组，该标识要求全局唯一。
PARTAKEMODE|分担方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表明该SGs路由组的负荷分担属性。取值含义如下所示。“BACKUP”：该SGs路由组工作方式是N+M主备方式 。“PARTAKE”：该SGs路由组工作方式是负荷分担方式。
ROUTE|路由ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于指示该SGs路由组关联的SGs路由，SGs路由配置参见SHOW SGS ROUTE。
MSTERNUM|主用路由个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~8。|该参数用于指示该SGs路由组关联的SGs路由中主用路由的个数。只有当配置分担方式为N+M主备方式才可以配置该参数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置SGs路由组的别名。






命令举例 


新增SGs路由组配置，设置路由组标识为1、关联的SGs路由标识为1，分担方式为N＋M备份，主用路由个数为1。
ADD SGS ROUTE GROUP:ROUTEGRPID=1,PARTAKEMODE="BACKUP",ROUTE=1,MSTERNUM=1,NAME="SS"; 








父主题： [SGs路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改SGs路由组配置(SET SGS ROUTE GROUP) 
#### 修改SGs路由组配置(SET SGS ROUTE GROUP) 


命令功能 

该命令用于修改SGs路由组配置，包括SGs路由组关联的SGs路由、SGs路由组的分担方式及主用路由的个数。


注意事项 

每个SGs路由组最多可以关联8个SGs路由。


参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由组，该标识要求全局唯一。
PARTAKEMODE|分担方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该SGs路由组的负荷分担属性。取值含义如下所示。“BACKUP”：该SGs路由组工作方式是N+M主备方式 。“PARTAKE”：该SGs路由组工作方式是负荷分担方式。
ROUTE|路由ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于指示该SGs路由组关联的SGs路由，SGs路由配置参见SHOW SGS ROUTE。
MSTERNUM|主用路由个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~8。|该参数用于指示该SGs路由组关联的SGs路由中主用路由的个数。只有当配置分担方式为N+M主备方式才可以配置该参数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置SGs路由组的别名。






命令举例 


修改路由组标识为1的SGs路由组配置，将分担方式修改为负荷分担。
SET SGS ROUTE GROUP:ROUTEGRPID=1,PARTAKEMODE="PARTAKE"; 








父主题： [SGs路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除SGs路由组配置(DEL SGS ROUTE GROUP) 
#### 删除SGs路由组配置(DEL SGS ROUTE GROUP) 


命令功能 

该命令用于删除SGs路由组配置。


注意事项 

执行该命令前通常需要执行删除SGs局向操作，以确保删除的SGs路由组没有被SGs局向路由组关联。 查询命令参见[SHOW SGS OFFICE ROUTE GROUP]。


参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由组，该标识要求全局唯一。






命令举例 


删除路由组标识为1的SGs路由组配置。
DEL SGS ROUTE GROUP:ROUTEGRPID=1; 








父主题： [SGs路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGs路由组配置(SHOW SGS ROUTE GROUP) 
#### 查询SGs路由组配置(SHOW SGS ROUTE GROUP) 


命令功能 

该命令用于查询SGs路由组配置，主要是SGs路由组关联的SGs路由、分担方式、主用路由个数等。


注意事项 



 
该命令不带参数，可查询所有的SGs路由组配置记录。
 

 
该命令也可根据SGs路由组标识查询与之匹配的记录。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|路由组ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于标识一条SGs路由组，该标识要求全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ROUTEGRPID|路由组ID|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条SGs路由组，该标识要求全局唯一。
PARTAKEMODE|分担方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表明该SGs路由组的负荷分担属性。取值含义如下所示。“BACKUP”：该SGs路由组工作方式是N+M主备方式 。“PARTAKE”：该SGs路由组工作方式是负荷分担方式。
ROUTE|路由ID|参数可选性:任选参数；参数类型:字符型。|该参数用于指示该SGs路由组关联的SGs路由，SGs路由配置参见SHOW SGS ROUTE。
MSTERNUM|主用路由个数|参数可选性:任选参数；参数类型:整数。|该参数用于指示该SGs路由组关联的SGs路由中主用路由的个数。只有当配置分担方式为N+M主备方式才可以配置该参数。
BACKUPNUM|备用路由个数|参数可选性:任选参数；参数类型:整数。|该参数用于指示该SGs路由组关联的SGs路由中备用路由的个数。只有当配置分担方式为N+M主备方式时该参数才有效。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|配置SGs路由组的别名。






命令举例 


查询所有的SGs路由组配置。
SHOW SGS ROUTE GROUP; 


`命令 (No.1): SHOW SGS ROUTE GROUP

操作维护         路由组ID   分担方式   路由ID   主用路由个数   备用路由个数   用户别名
--------------------------------------------------------------------------------------
复制 修改 删除   6          N+M备份    6        1              0              
--------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.09 秒）。

` 








父主题： [SGs路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs局向路由组配置 
### SGs局向路由组配置 


背景知识 

            
            SGs局向路由组配置用于确定出局到MSC/VLR局向的SGs路由组，从而获取到最终的出局SGs连接。
        


功能描述 


本功能用于设置到MSC/VLR局向的SGs路由组配置数据，SGs路由组可以分为直达路由和迂回路由两种，达到路由组备份的效果，系统优选使用直达路由组中的链路，当直达路由组中的链路均不可用时，选择迂回路由组中的链路出局。 


配置SGs局向路由组的流程如下： 







                        配置到MSC/VLR的SCTP连接。 配置命令参见
                        [ADD SCTP]
                        ;
                    







                        配置SGs连接。 配置命令参见
                        [ADD SGSCONN]
                        ;
                    







                        配置SGs路由。 配置命令参见
                        [ADD SGS ROUTE]
                        ;
                    







                        配置SGs路由组。 配置命令参见
                        [ADD SGS ROUTE GROUP]
                        ;
                    







                        配置SGs局向路由组。 配置命令参见
                        [ADD SGS OFFICE ROUTE GROUP]
                        ;
                    








配置流程说明 



 


                        首先配置到MSC/VLR的SCTP连接。 配置命令为：
                        ADD SCTP
                        ;
                    
 

 


                        然后配置SGs连接。 配置命令为：
                        ADD SGSCONN
                        :ID=1,SCTPID=1,NAME="SGs1";
                    
 

 


                        然后配置SGs路由。 配置命令为：
                        ADD SGS ROUTE
                        :ROUTEID=1,PARTAKEMODE="BACKUP",CONNECTION=1&2&3&4,MSTERNUM=2,NAME="SGs";
                    
 

 


                        然后配置路由组。 配置命令为：
                        ADD SGS ROUTE GROUP
                        :ROUTEGRPID=1,PARTAKEMODE="BACKUP",ROUTE=1&2&3&4,MSTERNUM=2,NAME="SGs";
                    
 

 


                        最后配置局向路由组。 配置命令为：
                        ADD SGS OFFICE ROUTE GROUP
                        :OFFICEID=1,ROUTEGRPID=1,BACKUPROUTEGRPID=2&3&4,NAME="SGs";
                    
 

 




相关主题 



 

新增SGs局向路由组配置(ADD SGS OFFICE ROUTE GROUP)
 

 

修改SGs局向路由组配置(SET SGS OFFICE ROUTE GROUP)
 

 

删除SGs局向路由组配置(DEL SGS OFFICE ROUTE GROUP)
 

 

查询SGs局向路由组配置(SHOW SGS OFFICE ROUTE GROUP)
 

 








父主题： [SGs连接路由配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增SGs局向路由组配置(ADD SGS OFFICE ROUTE GROUP) 
#### 新增SGs局向路由组配置(ADD SGS OFFICE ROUTE GROUP) 


命令功能 

该命令用于新增一条SGs局向路由组配置，将其与SGs路由组相关连。执行该命令后，可以将配置的SGs路由组关联到该SGs局向路由组中。


注意事项 



 
该命令执行前，需要先配置SGs 路由。 配置命令参见 ADD SGS ROUTE GROUP。
 

 
只有SGs局向路由组关联到MSC/VLR配置时才有意义， 配置命令参见ADD MSCVLR。
 

 
每个SGs局向路由组可以关联一个直达路由，但最多可以关联三个迂回路由。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
OFFICEID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于标识一个SGs局向，该参数要求全局唯一。
ROUTEGRPID|直达路由组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数表明该SGs局向关联的SGs直达路由组，一个SGs局向只能关联一个SGs直达路由组。需要先配置SGs路由组。查询命令参见SHOW SGS ROUTE GROUP。
BACKUPROUTEGRPID|迂回路由组ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数表明该SGs局向关联的SGs迂回路由组，一个SGs局向最多可以关联三个SGs迂回路由组。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的SGs局向的别名。






命令举例 


新增SGs局向路由组配置，设置SGs局向标识为1，关联的SGs直达路由组标识为1，SGs迂回路由组标识为0。
ADD SGS OFFICE ROUTE GROUP:OFFICEID=1,ROUTEGRPID=1,BACKUPROUTEGRPID=0; 








父主题： [SGs局向路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改SGs局向路由组配置(SET SGS OFFICE ROUTE GROUP) 
#### 修改SGs局向路由组配置(SET SGS OFFICE ROUTE GROUP) 


命令功能 

该命令用于修改SGs局向路由组配置，包括SGs局向关联的SGs直达路由组和迂回路由组。


注意事项 

每个SGs局向路由组可以关联一个直达路由，但最多可以关联三个迂回路由。


参数说明 


标识|名称|类型|说明
---|---|---|---
OFFICEID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于标识一个SGs局向，该参数要求全局唯一。
ROUTEGRPID|直达路由组ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数表明该SGs局向关联的SGs直达路由组，一个SGs局向只能关联一个SGs直达路由组。需要先配置SGs路由组。查询命令参见SHOW SGS ROUTE GROUP。
BACKUPROUTEGRPID|迂回路由组ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数表明该SGs局向关联的SGs迂回路由组，一个SGs局向最多可以关联三个SGs迂回路由组。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|配置的SGs局向的别名。






命令举例 


修改SGs局向标识为1的SGs局向路由组配置，将其关联的直达SGs路由组标识修改为1，关联的迂回SGs路由组标识修改为0。
SET SGS OFFICE ROUTE GROUP:OFFICEID=23,ROUTEGRPID=1,BACKUPROUTEGRPID=0; 








父主题： [SGs局向路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除SGs局向路由组配置(DEL SGS OFFICE ROUTE GROUP) 
#### 删除SGs局向路由组配置(DEL SGS OFFICE ROUTE GROUP) 


命令功能 

该命令用于删除SGs局向路由组配置，执行该命令可以去除SGs局向与SGs路由组的关联关系。


注意事项 


执行该命令前需要确保该SGs局向路由组没有被任何MSC/VLR配置关联，查询命令参见[SHOW MSCVLR]。


如果被删除的SGs局向路由已经与某VLR局向配置关联，需要先删除SGs局向路由与该VLR 局向之间的关联关系。 可以通过[SHOW VLROFFICE]命令查看VLR局向路由与VLR 局向之间的关联关系，通过[DEL VLROFFICE]命令删除。




参数说明 


标识|名称|类型|说明
---|---|---|---
OFFICEID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于标识一个SGs局向，该参数要求全局唯一。






命令举例 


删除局向标识为1的SGs局向路由组配置。
DEL SGS OFFICE ROUTE GROUP:OFFICEID=1; 








父主题： [SGs局向路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGs局向路由组配置(SHOW SGS OFFICE ROUTE GROUP) 
#### 查询SGs局向路由组配置(SHOW SGS OFFICE ROUTE GROUP) 


命令功能 

该命令用于查询SGs局向路由组配置，主要查询SGs局向关联的直达路由ID和迂回路由ID。


注意事项 



 
该命令不带参数，可查询所有的SGs局向路由配置记录。
 

 
该命令也可根据SGs局向路由标识查询与之匹配的记录。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
OFFICEID|局向ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于标识一个SGs局向，该参数要求全局唯一。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
OFFICEID|局向ID|参数可选性:任选参数；参数类型:整数。|该参数用于标识一个SGs局向，该参数要求全局唯一。
ROUTEGRPID|直达路由组ID|参数可选性:任选参数；参数类型:整数。|该参数表明该SGs局向关联的SGs直达路由组，一个SGs局向只能关联一个SGs直达路由组。需要先配置SGs路由组。查询命令参见SHOW SGS ROUTE GROUP。
BACKUPROUTEGRPID|迂回路由组ID|参数可选性:任选参数；参数类型:字符型。|该参数表明该SGs局向关联的SGs迂回路由组，一个SGs局向最多可以关联三个SGs迂回路由组。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|配置的SGs局向的别名。






命令举例 


查询所有SGs局向路由组配置。
SHOW SGS OFFICE ROUTE GROUP; 


`命令 (No.1): SHOW SGS OFFICE ROUTE GROUP

操作维护         局向ID   直达路由组ID   迂回路由组ID   用户别名
----------------------------------------------------------------
复制 修改 删除   6        6              0              
----------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.043 秒）。
` 








父主题： [SGs局向路由组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGs与EMM拒绝原因映射配置 
## SGs与EMM拒绝原因映射配置 


背景知识 


术语解释： 


EMM: EPS Mobility Management 


NAS: Non-access-Stratum 


背景介绍： 


随着移动通讯系统演进到EPS系统，为了运营商利用原有的2G和3G的基础设备提供语音、CS定位（LCS）等业务，引入了CSFB（CS fallback）功能，CSFB功能允许终端通过GERAN或者UTRAN接入到CS域。引入CSFB（CS Fallback）功能后，系统需要和MSC/VLR通讯，因此增加SGs口的消息处理流程。SGs接口和GPRS/UMTS系统中的Gs接口的功能类似。由于3GPP协议中并没有明确描述SGs口和EMM NAS失败原因之间的映射关系，因此引入了SGs和EMM拒绝原因的映射配置。 




功能描述 


本功能用于SGs口更新VLR位置信息失败后把SGs口失败原因映射为EPC的NAS失败原因，由于3GPP协议中并没有明确描述SGs口和EMM NAS失败原因之间的映射关系，因此系统默认生成了一套映射关系，对于有特殊映射要求的局点可以修改失败原因的映射关系。配置中SGs拒绝原因值是MSC/VLR位置信息更新失败的原因、EMM拒绝原因值为EPC的NAS失败原因。 


SGs与EMM拒绝原因映射配置的如下： 



                配置失败码映射关系，配置命令参见
                [SET SGS EMM]
                :SGSCAUSE;
            




相关主题 



 

设置SGs与EMM拒绝原因映射(SET SGS EMM)
 

 

查询SGs与EMM拒绝原因映射(SHOW SGS EMM)
 

 








父主题： [SGs口配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置SGs与EMM拒绝原因映射(SET SGS EMM) 
### 设置SGs与EMM拒绝原因映射(SET SGS EMM) 


命令功能 


设置SGs接口失败原因值与EMM NAS失败原因值之间的映射关系。当联合附着或者联合跟踪区更新时，MSC返回位置更新失败，导致联合附着或者联合跟踪区更新失败，运营商需要灵活设置附着接受或者跟踪区更新接受消息中的EMM Cause值时，使用该命令。命令执行成功后，联合附着或联合跟踪区更新时，MME发送位置更新请求消息给MSC，但MSC返回失败响应，MME依据MSC返回的失败原因，查找其对应的EMM NAS失败原因，并填写到附着或跟踪区更新接受消息中的EMM Cause IE中。 




注意事项 


使用该命令之前，需要MME支持SGs接口，配置命令为[SET SGSFLAG]:SGSFLAG="YES"。




参数说明 


标识|名称|类型|说明
---|---|---|---
SGSCAUSE|SGs拒绝原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|SGs口失败原因值列表，目前包括如下选项：IMSI在HLR中未知: 标准SGs口失败原因值，参看29.118协议。非法用户: 标准SGs口失败原因值，参看29.118协议。IMEI不接受: 标准SGs口失败原因值，参看29.118协议。非法设备: 标准SGs口失败原因值，参看29.118协议。PLMN不允许: 标准SGs口失败原因值，参看29.118协议。位置区不允许: 标准SGs口失败原因值，参看29.118协议。本位置区内漫游不允许: 标准SGs口失败原因值，参看29.118协议。位置区内无合适小区: 标准SGs口失败原因值，参看29.118协议。网络失败: 标准SGs口失败原因值，参看29.118协议。拥塞: 标准SGs口失败原因值，参看29.118协议。GSM鉴权不接受: 标准SGs口失败原因值，参看29.118协议。业务不支持: 标准SGs口失败原因值，参看29.118协议。请求的业务未签约: 标准SGs口失败原因值，参看29.118协议。选择的服务乱序: 标准SGs口失败原因值，参看29.118协议。消息语义不正确: 标准SGs口失败原因值，参看29.118协议。必选信息不正确: 标准SGs口失败原因值，参看29.118协议。消息类型不存在或未实现: 标准SGs口失败原因值，参看29.118协议。消息类型与协议状态不匹配: 标准SGs口失败原因值，参看29.118协议。IE不存在或未实现: 标准SGs口失败原因值，参看29.118协议。条件IE错误: 标准SGs口失败原因值，参看29.118协议。消息与协议状态不匹配: 标准SGs口失败原因值，参看29.118协议。未指定的协议错误: 标准SGs口失败原因值，参看29.118协议。SGs链路故障: 标准SGs口失败原因值，参看29.118协议。LAI解析失败: 标准SGs口失败原因值，参看29.118协议。其他原因: 其他SGs口失败原因值。超时: 用于设置MME等待SGs口响应超时所对应的EMM NAS原因值。
EMMCAUSE|EMM拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|需要设置的SGs失败原因值所对应的EMM拒绝原因值。下拉列表形式，目前包含如下选项:IMSI在HSS中未知:标准NAS口失败原因值，参看24.301协议。非法用户:标准NAS口失败原因值，参看24.301协议。IMEI不接受:标准NAS口失败原因值，参看24.301协议。非法设备:标准NAS口失败原因值，参看24.301协议。EPS业务和非EPS业务均不允许:标准NAS口失败原因值，参看24.301协议。PLMN不允许:标准NAS口失败原因值，参看24.301协议。跟踪区不允许:标准NAS口失败原因值，参看24.301协议。本跟踪区内漫游不允许:标准NAS口失败原因值，参看24.301协议。跟踪区内无合适小区:标准NAS口失败原因值，参看24.301协议。MSC临时不可达:标准NAS口失败原因值，参看24.301协议。网络失败:标准NAS口失败原因值，参看24.301协议。CS域不可用: 标准SGs口失败原因值，参看24.301协议。拥塞:标准NAS口失败原因值，参看24.301协议。消息语义不正确:标准NAS口失败原因值，参看24.301协议。必选信息不正确:标准NAS口失败原因值，参看24.301协议。消息类型不存在或未实现:标准NAS口失败原因值，参看24.301协议。消息类型与协议状态不匹配:标准NAS口失败原因值，参看24.301协议。IE不存在或未实现:标准NAS口失败原因值，参看24.301协议。条件IE错误:标准NAS口失败原因值，参看24.301协议。消息与协议状态不匹配:标准NAS口失败原因值，参看24.301协议。未指定的协议错误:标准NAS口失败原因值，参看24.301协议。






命令举例 


该命令设置SGs口失败原因值“IMSI Unknown in Hlr”，映射为EMM NAS原因值“IMSI Unknown in Hss”。 


命令执行成功后，联合附着或者联合跟踪区更新时，MME更新MSC失败，MSC返回更新失败原因为“IMSI Unknown in Hlr”，则附着或者跟踪区更新接受消息中，EMM Cause为“IMSI Unknown in Hss”。 


SET SGS EMM:SGSCAUSE="IMSIUnknownInHlr",EMMCAUSE="IMSIUnknownInHss"; 








父主题： [SGs与EMM拒绝原因映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGs与EMM拒绝原因映射(SHOW SGS EMM) 
### 查询SGs与EMM拒绝原因映射(SHOW SGS EMM) 


命令功能 


查询SGs接口失败原因值与EMM NAS失败原因值之间的映射关系。 




注意事项 


该配置生效，需要MME支持SGs接口。查询MME是否支持SGs接口配置命令为[SHOW SGSFLAG]。




参数说明 


标识|名称|类型|说明
---|---|---|---
SGSCAUSE|SGs拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGs口失败原因值列表，目前包括如下选项：IMSI在HLR中未知: 标准SGs口失败原因值，参看29.118协议。非法用户: 标准SGs口失败原因值，参看29.118协议。IMEI不接受: 标准SGs口失败原因值，参看29.118协议。非法设备: 标准SGs口失败原因值，参看29.118协议。PLMN不允许: 标准SGs口失败原因值，参看29.118协议。位置区不允许: 标准SGs口失败原因值，参看29.118协议。本位置区内漫游不允许: 标准SGs口失败原因值，参看29.118协议。位置区内无合适小区: 标准SGs口失败原因值，参看29.118协议。网络失败: 标准SGs口失败原因值，参看29.118协议。拥塞: 标准SGs口失败原因值，参看29.118协议。GSM鉴权不接受: 标准SGs口失败原因值，参看29.118协议。业务不支持: 标准SGs口失败原因值，参看29.118协议。请求的业务未签约: 标准SGs口失败原因值，参看29.118协议。选择的服务乱序: 标准SGs口失败原因值，参看29.118协议。消息语义不正确: 标准SGs口失败原因值，参看29.118协议。必选信息不正确: 标准SGs口失败原因值，参看29.118协议。消息类型不存在或未实现: 标准SGs口失败原因值，参看29.118协议。消息类型与协议状态不匹配: 标准SGs口失败原因值，参看29.118协议。IE不存在或未实现: 标准SGs口失败原因值，参看29.118协议。条件IE错误: 标准SGs口失败原因值，参看29.118协议。消息与协议状态不匹配: 标准SGs口失败原因值，参看29.118协议。未指定的协议错误: 标准SGs口失败原因值，参看29.118协议。SGs链路故障: 标准SGs口失败原因值，参看29.118协议。LAI解析失败: 标准SGs口失败原因值，参看29.118协议。其他原因: 其他SGs口失败原因值。超时: 用于设置MME等待SGs口响应超时所对应的EMM NAS原因值。
EMMCAUSE|EMM拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|需要设置的SGs失败原因值所对应的EMM拒绝原因值。下拉列表形式，目前包含如下选项:IMSI在HSS中未知:标准NAS口失败原因值，参看24.301协议。非法用户:标准NAS口失败原因值，参看24.301协议。IMEI不接受:标准NAS口失败原因值，参看24.301协议。非法设备:标准NAS口失败原因值，参看24.301协议。EPS业务和非EPS业务均不允许:标准NAS口失败原因值，参看24.301协议。PLMN不允许:标准NAS口失败原因值，参看24.301协议。跟踪区不允许:标准NAS口失败原因值，参看24.301协议。本跟踪区内漫游不允许:标准NAS口失败原因值，参看24.301协议。跟踪区内无合适小区:标准NAS口失败原因值，参看24.301协议。MSC临时不可达:标准NAS口失败原因值，参看24.301协议。网络失败:标准NAS口失败原因值，参看24.301协议。CS域不可用: 标准SGs口失败原因值，参看24.301协议。拥塞:标准NAS口失败原因值，参看24.301协议。消息语义不正确:标准NAS口失败原因值，参看24.301协议。必选信息不正确:标准NAS口失败原因值，参看24.301协议。消息类型不存在或未实现:标准NAS口失败原因值，参看24.301协议。消息类型与协议状态不匹配:标准NAS口失败原因值，参看24.301协议。IE不存在或未实现:标准NAS口失败原因值，参看24.301协议。条件IE错误:标准NAS口失败原因值，参看24.301协议。消息与协议状态不匹配:标准NAS口失败原因值，参看24.301协议。未指定的协议错误:标准NAS口失败原因值，参看24.301协议。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
SGSCAUSE|SGs拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGs口失败原因值列表，目前包括如下选项：IMSI在HLR中未知: 标准SGs口失败原因值，参看29.118协议。非法用户: 标准SGs口失败原因值，参看29.118协议。IMEI不接受: 标准SGs口失败原因值，参看29.118协议。非法设备: 标准SGs口失败原因值，参看29.118协议。PLMN不允许: 标准SGs口失败原因值，参看29.118协议。位置区不允许: 标准SGs口失败原因值，参看29.118协议。本位置区内漫游不允许: 标准SGs口失败原因值，参看29.118协议。位置区内无合适小区: 标准SGs口失败原因值，参看29.118协议。网络失败: 标准SGs口失败原因值，参看29.118协议。拥塞: 标准SGs口失败原因值，参看29.118协议。GSM鉴权不接受: 标准SGs口失败原因值，参看29.118协议。业务不支持: 标准SGs口失败原因值，参看29.118协议。请求的业务未签约: 标准SGs口失败原因值，参看29.118协议。选择的服务乱序: 标准SGs口失败原因值，参看29.118协议。消息语义不正确: 标准SGs口失败原因值，参看29.118协议。必选信息不正确: 标准SGs口失败原因值，参看29.118协议。消息类型不存在或未实现: 标准SGs口失败原因值，参看29.118协议。消息类型与协议状态不匹配: 标准SGs口失败原因值，参看29.118协议。IE不存在或未实现: 标准SGs口失败原因值，参看29.118协议。条件IE错误: 标准SGs口失败原因值，参看29.118协议。消息与协议状态不匹配: 标准SGs口失败原因值，参看29.118协议。未指定的协议错误: 标准SGs口失败原因值，参看29.118协议。SGs链路故障: 标准SGs口失败原因值，参看29.118协议。LAI解析失败: 标准SGs口失败原因值，参看29.118协议。其他原因: 其他SGs口失败原因值。超时: 用于设置MME等待SGs口响应超时所对应的EMM NAS原因值。
EMMCAUSE|EMM拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|需要设置的SGs失败原因值所对应的EMM拒绝原因值。下拉列表形式，目前包含如下选项:IMSI在HSS中未知:标准NAS口失败原因值，参看24.301协议。非法用户:标准NAS口失败原因值，参看24.301协议。IMEI不接受:标准NAS口失败原因值，参看24.301协议。非法设备:标准NAS口失败原因值，参看24.301协议。EPS业务和非EPS业务均不允许:标准NAS口失败原因值，参看24.301协议。PLMN不允许:标准NAS口失败原因值，参看24.301协议。跟踪区不允许:标准NAS口失败原因值，参看24.301协议。本跟踪区内漫游不允许:标准NAS口失败原因值，参看24.301协议。跟踪区内无合适小区:标准NAS口失败原因值，参看24.301协议。MSC临时不可达:标准NAS口失败原因值，参看24.301协议。网络失败:标准NAS口失败原因值，参看24.301协议。CS域不可用: 标准SGs口失败原因值，参看24.301协议。拥塞:标准NAS口失败原因值，参看24.301协议。消息语义不正确:标准NAS口失败原因值，参看24.301协议。必选信息不正确:标准NAS口失败原因值，参看24.301协议。消息类型不存在或未实现:标准NAS口失败原因值，参看24.301协议。消息类型与协议状态不匹配:标准NAS口失败原因值，参看24.301协议。IE不存在或未实现:标准NAS口失败原因值，参看24.301协议。条件IE错误:标准NAS口失败原因值，参看24.301协议。消息与协议状态不匹配:标准NAS口失败原因值，参看24.301协议。未指定的协议错误:标准NAS口失败原因值，参看24.301协议。






命令举例 


该命令查询SGs口失败原因值“IMSI Unknown in Hlr”所映射的EMM NAS原因值。 


SHOW SGS EMM:SGSCAUSE="IMSIUnknownInHlr"; 


`
命令 (No.1): SHOW SGS EMM:SGSCAUSE="IMSIUnknownInHlr";

操作维护  SGs拒绝原因值              EMM拒绝原因值
--------------------------------------------------
修改      IMSI在HLR中未知            IMSI在HSS中未知
--------------------------------------------------
记录数 1

命令执行成功（耗时 0.085 秒）。
` 








父主题： [SGs与EMM拒绝原因映射配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGs口VLR POOL管理 
## SGs口VLR POOL管理 


背景知识 

            
            支持CSFB功能后，MME与VLR之间能够互通。同时为了提高系统的容灾能力，MME可以与多个VLR同时连接，多个VLR组成一个POOL，在POOL内VLR相互备份，在某个VLR故障时，其他VLR可以继续为用户提供服务。
        


功能描述 


本功能用于配置LAI对应的VLR POOL，每个VLR POOL中包含的VLR局向，每个VLR局向在POOL内的优先级、权重及支持的NRI值。 


配置VLR POOL的相关配置命令如下： 







                        配置VLR局向，配置命令为
                        [ADD VLROFFICE]
                        。
                    







                        配置VLR POOL，配置命令为
                        [ADD VLRPOOL]
                        。
                    







                        配置LAI与VLR POOL对应关系，配置命令
                        [ADD LAIVLRPOOL]
                        。
                    








相关主题 



 

SGs口VLR局向配置
 

 

SGs口VLR POOL配置
 

 

SGs口VLR POOL NRI配置
 

 

SGs口选择VLR POOL配置
 

 








父主题： [SGs口配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs口VLR局向配置 
### SGs口VLR局向配置 


背景知识 


SGs接口是MME和MSC/VLR之间的接口，支持UE发起的联合类位置更新和CSFB功能。 


CSFB功能：移动通讯系统演进到EPS系统后，运营商为了利用原有的2G和3G的基础设备提供语音、CS定位（LCS）等业务，引入了CSFB（CS fallback）功能，CSFB功能允许终端通过GERAN或者UTRAN接入到CS域。 




功能描述 


MME支持SGs口时使用此配置管理VLR局向的名称、特征或者属性，并可以对VLR局向进行状态管理和业务负荷控制。 



                配置VLR局向之前，首先需要执行SGs局向路由组配置，配置命令参见
                [ADD SGS OFFICE ROUTE GROUP]
                。
            




相关主题 



 

新增SGs口VLR局向配置(ADD VLROFFICE)
 

 

修改SGs口VLR局向配置(SET VLROFFICE)
 

 

删除SGs口VLR局向配置(DEL VLROFFICE)
 

 

查询SGs口VLR局向配置(SHOW VLROFFICE)
 

 








父主题： [SGs口VLR POOL管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增SGs口VLR局向配置(ADD VLROFFICE) 
#### 新增SGs口VLR局向配置(ADD VLROFFICE) 


命令功能 


该命令用于新增SGs口的VLR局向配置。当运营商希望配置VLR局向的名称、特征或者属性时，使用此命令。通过该命令，MME可以获得此VLR局向的名称、特征或者属性，并可以对VLR局向进行状态管理和业务负荷控制。 




注意事项 


该命令执行前，需要先执行SGs局向路由组配置。 配置命令参见 [ADD SGS OFFICE ROUTE GROUP]。




参数说明 


标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指定SGs口VLR局向标识。
VLRNAME|VLR名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示SGs口VLR局向名称。
CSMOLR|是否支持CS-MO-LR功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:CS-MO-LR_UNKNOWN。|该参数用于指示SGs口VLR局向是否支持CS-MO-LR功能。CS的主叫发起的位置定位功能是指：LTE网络在进行联合附着时，核心网通知手机，它联合附着的MSC支持该功能。手机如果要发起主叫定位来定位自己所处的位置信息，可以通过CSFB方式回退到2G/3G网络进行定位。取值含义如下：未知（UNKNOWN）：不确定或者不关心VLR局向是否支持CS-MO-LR功能支持（Yes）：VLR局向支持CS-MO-LR功能不支持（No）：VLR局向不支持CS-MO-LR功能
ATTR|局向属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置VLR局向的属性：LUR携带TAI和ECGI：开关打开，MME发送给VLR的SGsAP-LOCATION-UPDATE-REQUEST消息中，将携带TAI和ECGI信元，否则不携带；RELEASE特定原因触发IMSI分离UE：开关打开，MME在CSFB的短消息流程中收到VLR的SGsAP-RELEASE-REQUEST消息携带原因是"IMSI unknown"或"IMSI detached for non-EPS services"时，MME将对UE发起IMSI分离，要求发起非EPS业务重新附着；否则不处理；支持SERVICE ABORT：开关打开，MME支持接收VLR的SGsAP-SERVICE-ABORT-REQUEST消息，中止当前的CSFB终呼业务；否则不处理；支持寻呼不携带LAI：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带LAI信元的情况下，对UE发起IMSI分离，待UE发起非EPS业务重新附着后，发送位置更新到VLR，由VLR重试寻呼；否则按普通SGs口寻呼消息处理，不触发IMSI分离；寻呼不携带TMSI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带TMSI信元的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI；寻呼携带错误LAI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中携带的LAI和MME保持的不一致的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI；寻呼不携带LAI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带LAI信元的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI。支持SRVCC：当“按SRVCC能力优选SGs口MSC”设置为“支持”时，使用本开关配置MSC/VLR是否同时支持SRVCC。MME在根据TA映射的LA选择SGs口MSC/VLR时，将优先选择支持SRVCC能力的MSC/VLR。配置后，当UE在进行IMS语音时，如果需要回落CS域进行CS业务，则采用SRVCC的方式，回落到UE已经通过SGs口注册的MSC/VLR。
SVHNAME|Sv口名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|当“局向属性”参数勾选了“支持SRVCC”时，使用该参数配置MSC/VLR在Sv口使用的名称（主机名或特定FQDN）。只有MSC/VLR在Sv口和SGs口使用不同的主机名时，才需要配置该参数。如果MSC/VLR在Sv口和SGs口使用相同的主机名，则仅需配置VLRNAME参数。
SGSCAUSE|MT短信用户不可达原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:UE_TU。|当该参数配置为UE temporarily unreachable，只有在NB用户收到的MT SMS的请求时，用户处于节电态MME才会回复该原因。






命令举例 


新增SGs口的VLR局向配置，其中VLR局向标识为1，VLR名称为vlr1，是否支持CS-MO-LR功能为支持，局向属性为支持寻呼不携带LAI。 


ADD VLROFFICE:VLROFFICEID=1,VLRNAME="vlr1",CSMOLR="CS-MO-LR_SUP",ATTR="NO_LAI"; 








父主题： [SGs口VLR局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改SGs口VLR局向配置(SET VLROFFICE) 
#### 修改SGs口VLR局向配置(SET VLROFFICE) 


命令功能 


该命令用于修改SGs口的VLR局向配置。 




注意事项 


无 




参数说明 


标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指定SGs口VLR局向标识。
VLRNAME|VLR名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示SGs口VLR局向名称。
CSMOLR|是否支持CS-MO-LR功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向是否支持CS-MO-LR功能。CS的主叫发起的位置定位功能是指：LTE网络在进行联合附着时，核心网通知手机，它联合附着的MSC支持该功能。手机如果要发起主叫定位来定位自己所处的位置信息，可以通过CSFB方式回退到2G/3G网络进行定位。取值含义如下：未知（UNKNOWN）：不确定或者不关心VLR局向是否支持CS-MO-LR功能支持（Yes）：VLR局向支持CS-MO-LR功能不支持（No）：VLR局向不支持CS-MO-LR功能
ATTR|局向属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置VLR局向的属性：LUR携带TAI和ECGI：开关打开，MME发送给VLR的SGsAP-LOCATION-UPDATE-REQUEST消息中，将携带TAI和ECGI信元，否则不携带；RELEASE特定原因触发IMSI分离UE：开关打开，MME在CSFB的短消息流程中收到VLR的SGsAP-RELEASE-REQUEST消息携带原因是"IMSI unknown"或"IMSI detached for non-EPS services"时，MME将对UE发起IMSI分离，要求发起非EPS业务重新附着；否则不处理；支持SERVICE ABORT：开关打开，MME支持接收VLR的SGsAP-SERVICE-ABORT-REQUEST消息，中止当前的CSFB终呼业务；否则不处理；支持寻呼不携带LAI：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带LAI信元的情况下，对UE发起IMSI分离，待UE发起非EPS业务重新附着后，发送位置更新到VLR，由VLR重试寻呼；否则按普通SGs口寻呼消息处理，不触发IMSI分离；寻呼不携带TMSI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带TMSI信元的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI；寻呼携带错误LAI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中携带的LAI和MME保持的不一致的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI；寻呼不携带LAI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带LAI信元的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI。支持SRVCC：当“按SRVCC能力优选SGs口MSC”设置为“支持”时，使用本开关配置MSC/VLR是否同时支持SRVCC。MME在根据TA映射的LA选择SGs口MSC/VLR时，将优先选择支持SRVCC能力的MSC/VLR。配置后，当UE在进行IMS语音时，如果需要回落CS域进行CS业务，则采用SRVCC的方式，回落到UE已经通过SGs口注册的MSC/VLR。
SVHNAME|Sv口名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|当“局向属性”参数勾选了“支持SRVCC”时，使用该参数配置MSC/VLR在Sv口使用的名称（主机名或特定FQDN）。只有MSC/VLR在Sv口和SGs口使用不同的主机名时，才需要配置该参数。如果MSC/VLR在Sv口和SGs口使用相同的主机名，则仅需配置VLRNAME参数。
SGSCAUSE|MT短信用户不可达原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当该参数配置为UE temporarily unreachable，只有在NB用户收到的MT SMS的请求时，用户处于节电态MME才会回复该原因。






命令举例 


修改VLR局向标识为1，VLR名称为vlr1的配置数据，将局向属性修改为支持SERVICE ABORT。 


SET VLROFFICE:VLROFFICEID=1,VLRNAME="vlr1",ATTR="SVRC_ABORT"; 








父主题： [SGs口VLR局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除SGs口VLR局向配置(DEL VLROFFICE) 
#### 删除SGs口VLR局向配置(DEL VLROFFICE) 


命令功能 


该命令用于删除VLR局向配置。 




注意事项 


如果被删除的VLR局向已经被某VLR POOL管理，需要先删除VLR局向与该VLR POOL之间的关联关系。 可以通过[SHOW VLRPOOL]命令查看VLR局向与VLR POOL之间的关联关系，通过[DEL VLRPOOL]命令删除。


如果被删除的VLR局向已经被MME特定VLR局向业务控制配置关联，需要先删除VLR局向与该VLR局向业务控制配置之间的关联关系。 可以通过[SHOW MOLVLR]命令查看VLR局向与VLR POOL之间的关联关系，通过[DEL MOLVLR]命令删除。




参数说明 


标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指定SGs口VLR局向标识。






命令举例 


删除VLR局向标识为1的配置数据。 


DEL VLROFFICE:VLROFFICEID=1; 








父主题： [SGs口VLR局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGs口VLR局向配置(SHOW VLROFFICE) 
#### 查询SGs口VLR局向配置(SHOW VLROFFICE) 


命令功能 


该命令用于查询VLR局向配置。 




注意事项 


无 




参数说明 


标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指定SGs口VLR局向标识。
VLRNAME|VLR名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示SGs口VLR局向名称。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数。|该参数用于指定SGs口VLR局向标识。
VLRNAME|VLR名称|参数可选性:任选参数；参数类型:字符型。|该参数用于指示SGs口VLR局向名称。
CSMOLR|是否支持CS-MO-LR功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向是否支持CS-MO-LR功能。CS的主叫发起的位置定位功能是指：LTE网络在进行联合附着时，核心网通知手机，它联合附着的MSC支持该功能。手机如果要发起主叫定位来定位自己所处的位置信息，可以通过CSFB方式回退到2G/3G网络进行定位。取值含义如下：未知（UNKNOWN）：不确定或者不关心VLR局向是否支持CS-MO-LR功能支持（Yes）：VLR局向支持CS-MO-LR功能不支持（No）：VLR局向不支持CS-MO-LR功能
ATTR|局向属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置VLR局向的属性：LUR携带TAI和ECGI：开关打开，MME发送给VLR的SGsAP-LOCATION-UPDATE-REQUEST消息中，将携带TAI和ECGI信元，否则不携带；RELEASE特定原因触发IMSI分离UE：开关打开，MME在CSFB的短消息流程中收到VLR的SGsAP-RELEASE-REQUEST消息携带原因是"IMSI unknown"或"IMSI detached for non-EPS services"时，MME将对UE发起IMSI分离，要求发起非EPS业务重新附着；否则不处理；支持SERVICE ABORT：开关打开，MME支持接收VLR的SGsAP-SERVICE-ABORT-REQUEST消息，中止当前的CSFB终呼业务；否则不处理；支持寻呼不携带LAI：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带LAI信元的情况下，对UE发起IMSI分离，待UE发起非EPS业务重新附着后，发送位置更新到VLR，由VLR重试寻呼；否则按普通SGs口寻呼消息处理，不触发IMSI分离；寻呼不携带TMSI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带TMSI信元的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI；寻呼携带错误LAI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中携带的LAI和MME保持的不一致的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI；寻呼不携带LAI时使用S-TMSI寻呼：开关打开，MME支持在收到VLR的SGsAP-PAGE-REQUEST中不携带LAI信元的情况下，对UE发起寻呼时，使用S-TMSI的用户标识，否则将使用IMSI。支持SRVCC：当“按SRVCC能力优选SGs口MSC”设置为“支持”时，使用本开关配置MSC/VLR是否同时支持SRVCC。MME在根据TA映射的LA选择SGs口MSC/VLR时，将优先选择支持SRVCC能力的MSC/VLR。配置后，当UE在进行IMS语音时，如果需要回落CS域进行CS业务，则采用SRVCC的方式，回落到UE已经通过SGs口注册的MSC/VLR。
SVHNAME|Sv口名称|参数可选性:任选参数；参数类型:字符型。|当“局向属性”参数勾选了“支持SRVCC”时，使用该参数配置MSC/VLR在Sv口使用的名称（主机名或特定FQDN）。只有MSC/VLR在Sv口和SGs口使用不同的主机名时，才需要配置该参数。如果MSC/VLR在Sv口和SGs口使用相同的主机名，则仅需配置VLRNAME参数。
SGSCAUSE|MT短信用户不可达原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当该参数配置为UE temporarily unreachable，只有在NB用户收到的MT SMS的请求时，用户处于节电态MME才会回复该原因。






命令举例 


查询所有的SGs口VLR局向配置。 


SHOW VLROFFICE; 


`

命令 (No.25): SHOW VLROFFICE

操作维护        VLR 局向标识  VLR名称  是否支持CS-MO-LR功能   局向属性            Sv口名称     MT短信用户不可达原因值
----------------------------------------------------------------------------------------------------------------------
复制 修改 删除  1             vlr1     支持                   支持SERVICE ABORT   sv1          用户临时不可达
----------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.051 秒）。


` 








父主题： [SGs口VLR局向配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs口VLR POOL配置 
### SGs口VLR POOL配置 


背景知识 


SGs接口是MME和MSC/VLR之间的接口，支持UE发起的联合类位置更新和CSFB功能。 


CSFB功能：移动通讯系统演进到EPS系统后，运营商为了利用原有的2G和3G的基础设备提供语音、CS定位（LCS）等业务，引入了CSFB（CS fallback）功能，CSFB功能允许终端通过GERAN或者UTRAN接入到CS域。 




功能描述 


SGs口VLR POOL配置用于管理多个VLR局向组成一个POOL的场景，配置各个VLR局向在POOL内的优先级和权重。 



                VLR局向标识需要通过命令
                [ADD VLROFFICE]
                进行配置。
            



                需要通过命令
                [SET SOFTWARE PARAMETER]
                打开移动管理参数“支持VLR POOL组网”开关，本配置才能够生效。
            




相关主题 



 

新增SGs口VLR POOL配置(ADD VLRPOOL)
 

 

修改SGs口VLR POOL配置(SET VLRPOOL)
 

 

删除SGs口VLR POOL配置(DEL VLRPOOL)
 

 

查询SGs口VLR POOL配置(SHOW VLRPOOL)
 

 








父主题： [SGs口VLR POOL管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增SGs口VLR POOL配置(ADD VLRPOOL) 
#### 新增SGs口VLR POOL配置(ADD VLRPOOL) 


命令功能 


该命令用于新增SGs口VLR POOL配置。当运营商希望多个VLR局组成一个POOL共同进行业务控制的时候，使用该命令。通过该命令，MME可以获得各个VLR局向在VLR POOL内的优先级和权重等信息。 




注意事项 


VLR局向标识需要通过命令[ADD VLROFFICE]进行配置。


一个VLR POOL最多支持32个VLR局向。 


需要通过命令[SET SOFTWARE PARAMETER]打开移动管理参数“支持VLR POOL组网”开关，本配置才能够生效。




参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定SGs口VLR POOL标识。
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示SGs口VLR局向标识。
VLRLEVEL|VLR级别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向在VLR POOL中的优先级别, 数值越低优先级越高。
VLRWEIGHT|VLR权重|参数可选性:必选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指示SGs口VLR局向在VLR POOL中的权重。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。






命令举例 


新增SGs口VLR POOL配置，其中VLR POOL标识为1，VLR局向标识为1，VLR级别为1级，VLR权重为100。 


ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=1,VLRLEVEL="LEVEL_1",VLRWEIGHT=100; 








父主题： [SGs口VLR POOL配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改SGs口VLR POOL配置(SET VLRPOOL) 
#### 修改SGs口VLR POOL配置(SET VLRPOOL) 


命令功能 


该命令用于修改SGs口VLR POOL配置中的VLR局向的优先级或者权重。 




注意事项 


无 




参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定SGs口VLR POOL标识。
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示SGs口VLR局向标识。
VLRLEVEL|VLR级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向在VLR POOL中的优先级别, 数值越低优先级越高。
VLRWEIGHT|VLR权重|参数可选性:任选参数；参数类型:整数；参数范围为:1~1000。|该参数用于指示SGs口VLR局向在VLR POOL中的权重。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。






命令举例 


修改VLR POOL标识为1，VLR局向标识为1的配置数据，将VLR权重修改为200。 


SET VLRPOOL:VLRPOOLID=1,VLROFFICEID=1,VLRWEIGHT=200; 








父主题： [SGs口VLR POOL配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除SGs口VLR POOL配置(DEL VLRPOOL) 
#### 删除SGs口VLR POOL配置(DEL VLRPOOL) 


命令功能 


该命令用于删除SGs口VLR POOL配置中的VLR局向配置信息。 




注意事项 


如果被删除的VLRPOOL已经被某LAI关联，需要先删除VLRPOOL与该LAI之间的关联关系。 可以通过[SHOW LAIVLRPOOL]命令查看VLRPOOL与LAI之间的关联关系，通过[DEL LAIVLRPOOL]命令删除。




参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定SGs口VLR POOL标识。
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示SGs口VLR局向标识。






命令举例 


删除VLR POOL标识为1，VLR局向标识为1的配置数据。 


DEL VLRPOOL:VLRPOOLID=1,VLROFFICEID=1; 








父主题： [SGs口VLR POOL配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGs口VLR POOL配置(SHOW VLRPOOL) 
#### 查询SGs口VLR POOL配置(SHOW VLRPOOL) 


命令功能 


该命令用于查询SGs口VLR POOL配置信息。 




注意事项 


无 




参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指定SGs口VLR POOL标识。
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示SGs口VLR局向标识。
VLRLEVEL|VLR级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向在VLR POOL中的优先级别, 数值越低优先级越高。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数。|该参数用于指定SGs口VLR POOL标识。
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数。|该参数用于指示SGs口VLR局向标识。
VLRLEVEL|VLR级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGs口VLR局向在VLR POOL中的优先级别, 数值越低优先级越高。
VLRWEIGHT|VLR权重|参数可选性:任选参数；参数类型:整数。|该参数用于指示SGs口VLR局向在VLR POOL中的权重。
IMSISTART|IMSI后三位起始值|参数可选性:任选参数；参数类型:整数。|该参数用于指示归属于此VLR局向的用户的IMSI后三位数值区间的起始值。
IMSIEND|IMSI后三位终止值|参数可选性:任选参数；参数类型:整数。|该参数用于指示归属于此VLR局向的用户的IMSI后三位数值区间的终止值。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|对此配置进行维护记录，起备注作用。






命令举例 


查询所有的SGs口VLR POOL配置 


SHOW VLRPOOL; 


`

命令 (No.31): SHOW VLRPOOL

操作维护      VLR POOL标识 VLR 局向标识 VLR级别   VLR权重 用户别名 
----------------------------------------------------------------------------
复制 修改 删除   1             1             1       200  
----------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 1.62 秒）。


` 








父主题： [SGs口VLR POOL配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs口VLR POOL NRI配置 
### SGs口VLR POOL NRI配置 


背景知识 

            
            NRI（Network Resource Identity，网络资源标识符），用于标识服务于一个特定MS/UE的MSC节点。NRI可以保证MS/UE每次发起业务均能路由到指定的MSC。一个NRI对应MSC池中的一个MSC。
        


功能描述 

            
            当UE在MME发起业务时，MME使用NRI选择MSC池中的指定MSC。
        


相关主题 



 

VLR POOL NRI长度配置
 

 

POOL内VLR NRI值配置
 

 








父主题： [SGs口VLR POOL管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### VLR POOL NRI长度配置 
#### VLR POOL NRI长度配置 


背景知识 

            
            TMSI的第14-23bit分配给NRI使用，NRI的长度可以占用其中的一个或者多个bit。
        


功能描述 

            
            NRI由运营商分配，MME需要配置NRI在TMSI中的长度，以便于从UE的信息中提取有效的NRI数值。
        


相关主题 



 

新增VLR POOL NRI长度配置(ADD POOLNRL LEN)
 

 

修改VLR POOL NRI长度配置(SET POOLNRL LEN)
 

 

删除VLR POOL NRI长度配置(DEL POOLNRL LEN)
 

 

查询VLR POOL NRI长度配置(SHOW POOLNRL LEN)
 

 








父主题： [SGs口VLR POOL NRI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增VLR POOL NRI长度配置(ADD POOLNRL LEN) 
##### 新增VLR POOL NRI长度配置(ADD POOLNRL LEN) 


命令功能 

该命令用于增加MSC/VLR POOl对应的NRI长度。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。
NRILENGTH|NRI长度|参数可选性:必选参数；参数类型:整数；参数范围为:1~10。|用于配置NRI的长度，便于提取有效的NRI数值。






命令举例 


新增MSC/VLR POOl对应的NRI长度，其中VLR POOL标识为1，对应的NRI长度为2。 


ADD POOLNRL LEN:VLRPOOLID=1,NRILENGTH=2; 








父主题： [VLR POOL NRI长度配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 修改VLR POOL NRI长度配置(SET POOLNRL LEN) 
##### 修改VLR POOL NRI长度配置(SET POOLNRL LEN) 


命令功能 

该命令用于修改MSC/VLR POOl对应的NRI长度。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。
NRILENGTH|NRI长度|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|用于配置NRI的长度，便于提取有效的NRI数值。






命令举例 


修改MSC/VLR POOl对应的NRI长度，其中VLR POOL标识为1，将其对应的NRI长度修改为3。 


SET POOLNRL LEN:VLRPOOLID=1,NRILENGTH=3; 








父主题： [VLR POOL NRI长度配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除VLR POOL NRI长度配置(DEL POOLNRL LEN) 
##### 删除VLR POOL NRI长度配置(DEL POOLNRL LEN) 


命令功能 

该命令用于删除MSC/VLR POOl对应的NRI长度。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。






命令举例 


删除标识为1的MSC/VLR POOl对应的NRI长度。 


DEL POOLNRL LEN:VLRPOOLID=1; 








父主题： [VLR POOL NRI长度配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询VLR POOL NRI长度配置(SHOW POOLNRL LEN) 
##### 查询VLR POOL NRI长度配置(SHOW POOLNRL LEN) 


命令功能 

该命令用于查询MSC/VLR POOl对应的NRI长度。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。
NRILENGTH|NRI长度|参数可选性:任选参数；参数类型:整数。|用于配置NRI的长度，便于提取有效的NRI数值。






命令举例 


查询标识为1的MSC/VLR POOl对应的NRI长度。 


SHOW POOLNRL LEN:VLRPOOLID=1; 


`

命令 (No.1): SHOW POOLNRL LEN:VLRPOOLID=1;

操作维护         VLR POOL标识   NRI长度
---------------------------------------
复制 修改 删除   1              4
---------------------------------------
记录数 1

命令执行成功（耗时 0.022 秒）。
` 








父主题： [VLR POOL NRI长度配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### POOL内VLR NRI值配置 
#### POOL内VLR NRI值配置 


背景知识 

            
            NRI由运营商规划分配，一个MSC/VLR可能分配一个或多个NRI数值，同一个MSC/VLR POOL下的不同MSC/VLR的NRI不能相同，不同MSC/VLR POOL下的MSC/VLR的NRI可以相同。
        


功能描述 

            
            根据运营商的规划，配置MSC/VLR POOL中的MSC/VLR使用的NRI数值，用于MME根据UE携带的NRI数值选择MSC/VLR。
        


相关主题 



 

新增POOL内VLR NRI值(ADD POOL VRLNRI)
 

 

删除POOL内VLR NRI值(DEL POOL VRLNRI)
 

 

查询POOL内VLR NRI值(SHOW POOL VRLNRI)
 

 








父主题： [SGs口VLR POOL NRI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 新增POOL内VLR NRI值(ADD POOL VRLNRI) 
##### 新增POOL内VLR NRI值(ADD POOL VRLNRI) 


命令功能 

该命令用于新增MSC/VLR POOL、POOL内的MSC/VLR局向标识和该局向对应的NRI数值。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|唯一标识一个MSC/VLR。该参数需要通过ADD VLROFFICE命令进行配置，可通过SHOW VLROFFICE命令进行查询。
NRI|NRI值|参数可选性:必选参数；参数类型:整数；参数范围为:0~1023。|运营商为MSC/VLR规划的NRI数值。






命令举例 


新增MSC/VLR POOL，其中MSC/VLR POOL标识为1，MSC/VLR局向标识为2，该MSC/VLR局向对应的NRI值为1。 


ADD POOL VRLNRI:VLRPOOLID=1,VLROFFICEID=2,NRI=1; 








父主题： [POOL内VLR NRI值配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 删除POOL内VLR NRI值(DEL POOL VRLNRI) 
##### 删除POOL内VLR NRI值(DEL POOL VRLNRI) 


命令功能 

该命令用于删除MSC/VLR POOL或POOL内的MSC/VLR局向。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|唯一标识一个MSC/VLR。该参数需要通过ADD VLROFFICE命令进行配置，可通过SHOW VLROFFICE命令进行查询。
NRI|NRI值|参数可选性:任选参数；参数类型:整数；参数范围为:0~1023。|运营商为MSC/VLR规划的NRI数值。






命令举例 


删除MSC/POOL内的MSC/VLR局向的NRI值，其中MSC/VLR POOL标识为1，MSC/VLR局向标识为2，该MSC/VLR局向对应的NRI值为1。 


DEL POOL VRLNRI:VLRPOOLID=1,VLROFFICEID=2,NRI=1; 








父主题： [POOL内VLR NRI值配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


##### 查询POOL内VLR NRI值(SHOW POOL VRLNRI) 
##### 查询POOL内VLR NRI值(SHOW POOL VRLNRI) 


命令功能 

该命令用于查询MSC/VLR POOL、POOL内的MSC/VLR局向标识和该局向对应的NRI数值。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|唯一标识一个MSC/VLR。该参数需要通过ADD VLROFFICE命令进行配置，可通过SHOW VLROFFICE命令进行查询。
NRI|NRI值|参数可选性:任选参数；参数类型:整数；参数范围为:0~1023。|运营商为MSC/VLR规划的NRI数值。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数。|唯一标识一个MSC/VLR POOL。该参数需要通过ADD VLRPOOL命令进行配置，可通过SHOW VLRPOOL命令进行查询。
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数。|唯一标识一个MSC/VLR。该参数需要通过ADD VLROFFICE命令进行配置，可通过SHOW VLROFFICE命令进行查询。
NRI|NRI值|参数可选性:任选参数；参数类型:整数。|运营商为MSC/VLR规划的NRI数值。






命令举例 


查询MSC/VLR POOL中的MSC/VLR局向对应的NRI值。 


SHOW POOL VRLNRI 


`

命令 (No.1): SHOW POOL VRLNRI

操作维护    VLR POOL标识   VLR局向标识   NRI值
----------------------------------------------
复制 删除   1              711           1
----------------------------------------------
记录数 1

命令执行成功（耗时 0.043 秒）。
` 








父主题： [POOL内VLR NRI值配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs口选择VLR POOL配置 
### SGs口选择VLR POOL配置 


背景知识 


SGs接口是MME和MSC/VLR之间的接口，支持UE发起的联合类位置更新和CSFB功能。 


CSFB功能：移动通讯系统演进到EPS系统后，运营商为了利用原有的2G和3G的基础设备提供语音、CS定位（LCS）等业务，引入了CSFB（CS fallback）功能，CSFB功能允许终端通过GERAN或者UTRAN接入到CS域。 




功能描述 


MME进行SGs口业务选择VLR时，需要根据VLR管理的位置区获得一个VLR。当多个VLR组成一个POOL共同管理一个位置区时，通过此配置获得一个VLR POOL标识，然后根据VLR POOL标识获得VLR POOL内的各个VLR局向的优先级和权重以及状态等信息，并选择一个可用的VLR局向进行业务。 



                位置区名需要通过命令
                [ADD LAI]
                进行配置。
            



                VLR POOL标识需要通过命令
                [ADD VLRPOOL]
                进行配置。
            



                需要通过命令
                [SET SOFTWARE PARAMETER]
                打开移动管理参数“支持VLR POOL组网”开关，本配置才能够生效。
            




相关主题 



 

新增SGs口选择VLR POOL配置(ADD LAIVLRPOOL)
 

 

修改SGs口选择VLR POOL配置(SET LAIVLRPOOL)
 

 

删除SGs口选择VLR POOL配置(DEL LAIVLRPOOL)
 

 

查询SGs口选择VLR POOL配置(SHOW LAIVLRPOOL)
 

 








父主题： [SGs口VLR POOL管理]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增SGs口选择VLR POOL配置(ADD LAIVLRPOOL) 
#### 新增SGs口选择VLR POOL配置(ADD LAIVLRPOOL) 


命令功能 


该命令用于新增SGs口选择VLR POOL配置。当运营商对VLR进行POOL组网时，根据LAI获得关联的VLR POOL时使用，使用此命令后，根据LAI可以获得管理此LAI的VLR POOL信息。 




注意事项 


位置区名需要通过命令[ADD LAI]进行配置。


VLR POOL标识需要通过命令[ADD VLRPOOL]进行配置。


需要通过命令[SET SOFTWARE PARAMETER]打开移动管理参数“支持VLR POOL组网”开关，本配置才能够生效。




参数说明 


标识|名称|类型|说明
---|---|---|---
LAINAME|位置区名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|该参数用于指定SGs口VLR POOL 管理的位置区名。
VLRPOOLID|VLR POOL标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示SGs口LAI关联的VLR POOL标识。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。






命令举例 


新增SGs口选择VLR POOL配置，其中位置区名为lai1，VLR POOL标识为1。 


ADD LAIVLRPOOL:LAINAME="lai1",VLRPOOLID=1; 








父主题： [SGs口选择VLR POOL配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 修改SGs口选择VLR POOL配置(SET LAIVLRPOOL) 
#### 修改SGs口选择VLR POOL配置(SET LAIVLRPOOL) 


命令功能 


该命令用于修改SGs口选择VLR POOL配置，当LAI与关联的VLR POOL关系发生变化时使用此命令。 




注意事项 


无 




参数说明 


标识|名称|类型|说明
---|---|---|---
LAINAME|位置区名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|该参数用于指定SGs口VLR POOL 管理的位置区名。
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于指示SGs口LAI关联的VLR POOL标识。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。






命令举例 


修改位置区名为lai1的配置数据，将VLR POOL标识修改为2。 


SET LAIVLRPOOL:LAINAME="lai1",VLRPOOLID=2; 








父主题： [SGs口选择VLR POOL配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除SGs口选择VLR POOL配置(DEL LAIVLRPOOL) 
#### 删除SGs口选择VLR POOL配置(DEL LAIVLRPOOL) 


命令功能 


该命令用于删除SGs口选择VLR POOL配置。 




注意事项 


无 




参数说明 


标识|名称|类型|说明
---|---|---|---
LAINAME|位置区名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|该参数用于指定SGs口VLR POOL 管理的位置区名。






命令举例 


删除位置区名为lai1的配置数据。 


DEL LAIVLRPOOL:LAINAME="lai1"; 








父主题： [SGs口选择VLR POOL配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGs口选择VLR POOL配置(SHOW LAIVLRPOOL) 
#### 查询SGs口选择VLR POOL配置(SHOW LAIVLRPOOL) 


命令功能 


该命令用于查询SGs口选择VLR POOL配置。 




注意事项 


无 




参数说明 


标识|名称|类型|说明
---|---|---|---
LAINAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|该参数用于指定SGs口VLR POOL 管理的位置区名。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
LAINAME|位置区名|参数可选性:任选参数；参数类型:字符型。|该参数用于指定SGs口VLR POOL 管理的位置区名。
VLRPOOLID|VLR POOL标识|参数可选性:任选参数；参数类型:整数。|该参数用于指示SGs口LAI关联的VLR POOL标识。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|对此配置进行维护记录，起备注作用。






命令举例 


查询所有的SGs口选择VLR POOL配置 


SHOW LAIVLRPOOL; 


`

命令 (No.37): SHOW LAIVLRPOOL

操作维护     位置区名 VLR POOL标识 用户别名 
---------------------------------------------------
复制 修改 删除  lai1     2  
---------------------------------------------------
记录数 1

命令执行成功（耗时 0.041 秒）。


` 








父主题： [SGs口选择VLR POOL配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 基于IMSI的SGs口控制配置 
## 基于IMSI的SGs口控制配置 


背景知识 


运营商在GERAN/UTRAN网络的基础上部署LTE网络，形成LTE网络热点覆盖，用户附着在LTE时，通过SGs接口收发短消息，无需回落。基于SGs接口实现短消息，即将用户的短消息在EPS网络和传统的电路域网络之间传递来提供短消息业务，不需要回落到目标电路域网络。 




功能描述 


基于SGs接口实现短消息特性中，最主要的接口是SGs接口，它是MME和MSC Server之间的接口，用来处理EPS和CS域之间的移动性管理和短消息业务寻呼流程。 


基于SGs接口实现短消息业务特性的移动性管理主要是通过SGs接口实现的，用户在附着/去附着网络，或者发生位置更新时，MME通过SGs接口跟MSC Server进行信息交互。 


基于IMSI的SGs口控制和基于APN的SGs口控制，这两个功能与“支持SGS口”的全局SGs口控制功能互斥，全局SGs口控制功能优先。即当SGs口开关配置“支持SGS口”开关打开，无论基于IMSI的SGs口控制和基于APN的SGs口控制功能开关是否打开，都执行全局SGs口控制功能；当SGs口开关配置“支持SGS口”开关关闭，才根据License“MME支持基于IMSI/APN的SGs口控制”以及基于IMSI的SGs口控制/基于APN的SGs口控制功能开关配置来决策是否开启这两个功能。 




相关主题 



 

SGs口IMSI控制策略配置
 

 

SGs口IMSI配置
 

 








父主题： [SGs口配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs口IMSI控制策略配置 
### SGs口IMSI控制策略配置 


背景知识 


3GPP TS 24.301协议定义了MME在attach/TAU accept消息中携带网络的语音业务能力指示。MME通过“Additional update result”参数指示网络对CSFB业务的支持能力。包括以下三种类型： 






no additional information：网络支持CSFB，终端可通过CSFB进行语音、SMS和其他业务。 






CS Fallback not preferred：网络不支持CSFB，终端不能进行CSFB业务。 






SMS only：网络仅支持CSFB SMS业务，终端在LTE仅能通过CSFB进行SMS业务，无法在LTE进行CSFB业务。 








功能描述 


该功能用于支持MME基于SGs接口根据用户的IMSI号码实现短消息业务，即将用户的短消息在EPS网络和传统的电路域网络之间传递来提供短消息业务，不需要回落到目标电路域网络。 


适用的场景：当运营商仅允许某些用户可以使用SGs接口来实现短消息业务时。 




相关主题 



 

设置SGs口IMSI控制策略(SET SGS IMSI CTRL POLICY)
 

 

查询SGs口IMSI控制策略(SHOW SGS IMSI CTRL POLICY)
 

 








父主题： [基于IMSI的SGs口控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 设置SGs口IMSI控制策略(SET SGS IMSI CTRL POLICY) 
#### 设置SGs口IMSI控制策略(SET SGS IMSI CTRL POLICY) 


命令功能 

该命令用于配置MME是否支持根据用户的IMSI号码通过SGs接口使用短消息业务。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
SGSIMSIFUN|MME支持SGs口IMSI功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持根据用户的IMSI号段选择SGs接口功能，当该参数设置为支持时，MME会根据配置的IMSI号段通过SGs接口到MSC/VLR进行注册流程，并且在MSC/VLR注册成功时，指示对应用户的“Additional update result”为“SMS ONLY”。该参数取值可以为：不支持：不支持SGs口IMSI功能支持：支持SGs口IMSI功能






命令举例 


设置MME支持SGs口IMSI功能为支持。 


SET SGS IMSI CTRL POLICY:SGSIMSIFUN="YES"; 








父主题： [SGs口IMSI控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGs口IMSI控制策略(SHOW SGS IMSI CTRL POLICY) 
#### 查询SGs口IMSI控制策略(SHOW SGS IMSI CTRL POLICY) 


命令功能 

该命令用于查询MME是否支持根据用户的IMSI号码通过SGs接口使用短消息业务。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
SGSIMSIFUN|MME支持SGs口IMSI功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持根据用户的IMSI号段选择SGs接口功能，当该参数设置为支持时，MME会根据配置的IMSI号段通过SGs接口到MSC/VLR进行注册流程，并且在MSC/VLR注册成功时，指示对应用户的“Additional update result”为“SMS ONLY”。该参数取值可以为：不支持：不支持SGs口IMSI功能支持：支持SGs口IMSI功能






命令举例 


查询SGs口IMSI段控制策略配置。 


SHOW SGS IMSI CTRL POLICY; 


`
命令 (No.1): SHOW SGS IMSI CTRL POLICY;

操作维护  MME支持SGs口IMSI功能
------------------------------
修改      支持
------------------------------
记录数 1

命令执行成功（耗时 0.033 秒）。
` 








父主题： [SGs口IMSI控制策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### SGs口IMSI配置 
### SGs口IMSI配置 


背景知识 

            
            SGs接口是MME和MSC Server之间的接口，用来处理EPS和CS域之间的移动性管理和短消息业务寻呼流程。
        


功能描述 


该功能用于支持MME基于SGs接口根据用户的IMSI号码实现短消息业务，即将用户的短消息在EPS网络和传统的电路域网络之间传递来提供短消息业务，不需要回落到目标电路域网络。 


当运营商仅允许某些用户可以使用SGs接口来实现短消息业务时，使用该功能来控制。 


注意：系统采用最短匹配原则，如果新增加的数据已经包含在已存在的数据中，则不允许配置；如果已存在的数据包含在新增加的数据中，则已存在的数据将会被覆盖删除，仅保留新增加的数据。举例说明如下： 






存在4600101，添加46001011,4600101123等等，新增的配置数据是4600101的子集，因此不添加新增的数据。 






存在4600388，4600399，添加46003，则系统删除4600388和4600399，增加46003配置数据。 








相关主题 



 

新增SGs口IMSI配置(ADD SGS IMSI)
 

 

删除SGs口IMSI配置(DEL SGS IMSI)
 

 

查询SGs口IMSI配置(SHOW SGS IMSI)
 

 








父主题： [基于IMSI的SGs口控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 新增SGs口IMSI配置(ADD SGS IMSI) 
#### 新增SGs口IMSI配置(ADD SGS IMSI) 


命令功能 

该命令用于配置允许通过SGs接口发送短消息的用户的IMSI号段。


注意事项 

无


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。






命令举例 


新增SGs口IMSI配置，IMSI号段为46001。 


ADD SGS IMSI:IMSI="46001"; 








父主题： [SGs口IMSI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 删除SGs口IMSI配置(DEL SGS IMSI) 
#### 删除SGs口IMSI配置(DEL SGS IMSI) 


命令功能 

该命令用于删除允许通过SGs接口发送短消息的用户的IMSI号段。


注意事项 

无


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。






命令举例 


删除IMSI号段为46001的SGs IMSI配置记录。 


DEL SGS IMSI:IMSI="46001"; 








父主题： [SGs口IMSI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


#### 查询SGs口IMSI配置(SHOW SGS IMSI) 
#### 查询SGs口IMSI配置(SHOW SGS IMSI) 


命令功能 

该命令用于查询允许通过SGs接口发送短消息的用户的IMSI号段。


注意事项 

无


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。






命令举例 


查询SGs口IMSI配置。 


SHOW SGS IMSI:IMSI="46001"; 


`
命令 (No.1): SHOW SGS IMSI:IMSI="46001";

操作维护    IMSI号段
--------------------
复制 删除   46001
--------------------
记录数 1

命令执行成功（耗时 0.033 秒）。
` 








父主题： [SGs口IMSI配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 基于APN的SGs口控制配置 
## 基于APN的SGs口控制配置 


背景知识 


当运营商对国际用户使用SGs口短信，国内用户不使用SGs口短信时，如果基于IMSI号段配置数据量大，则可以基于APN区分国内国际用户。 


基于IMSI的SGs口控制和基于APN的SGs口控制，这两个功能与“支持SGS口”的全局SGs口控制功能互斥，全局SGs口控制功能优先。即当SGs口开关配置“支持SGS口”开关打开，无论基于IMSI的SGs口控制和基于APN的SGs口控制功能开关是否打开，都执行全局SGs口控制功能；当SGs口开关配置“支持SGS口”开关关闭，才根据License“MME支持基于IMSI/APN的SGs口控制”以及基于IMSI的SGs口控制/基于APN的SGs口控制功能开关配置来决策是否开启这两个功能。 




功能描述 


MME基于APN配置是否支持SGs口，提供了默认配置和特定APN的配置，方便工程数据配置。“MME支持基于IMSI/APN的SGs口控制”License项为“支持”时，本功能才生效。 




相关主题 



 

设置基于APN的SGs口控制策略(SET DEFAULT APNSGSCTL)
 

 

查询基于APN的SGs口控制策略(SHOW DEFAULT APNSGSCTL)
 

 

新增基于APN的SGs口控制配置(ADD APNSGSCTL)
 

 

修改基于APN的SGs口控制配置(SET APNSGSCTL)
 

 

删除基于APN的SGs口控制配置(DEL APNSGSCTL)
 

 

查询基于APN的SGs口控制配置(SHOW APNSGSCTL)
 

 








父主题： [SGs口配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置基于APN的SGs口控制策略(SET DEFAULT APNSGSCTL) 
### 设置基于APN的SGs口控制策略(SET DEFAULT APNSGSCTL) 


命令功能 

该命令用于配置MME是否支持基于APN的SGs口控制，以及基于APN的SGs口控制的默认策略。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
SUPAPNSGSCTL|支持基于APN的SGs口控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于APN的SGs口控制。不支持：MME不支持基于APN的SGs口控制。支持：MME支持基于APN的SGs口控制。
APNDEFSUPSGS|默认支持SGs口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME基于APN是否默认支持SGs口。不支持：默认不支持SGs口。支持：默认支持SGs口。
SUPATTNOPDN|支持附着无PDN连接流程|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME基于APN的SGs口控制是否支持物联网终端的附着无PDN连接流程，如果支持，则MME使用签约的默认APN进行SGs口控制。不支持：MME基于APN的SGs口控制不支持附着无PDN连接流程。支持：MME基于APN的SGs口控制支持附着无PDN连接流程，并使用签约的默认APN进行SGs口控制。






命令举例 


设置基于APN的SGs口默认控制策略。 


SET DEFAULT APNSGSCTL:SUPAPNSGSCTL="YES",APNDEFSUPSGS="YES",SUPATTNOPDN="YES"; 








父主题： [基于APN的SGs口控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询基于APN的SGs口控制策略(SHOW DEFAULT APNSGSCTL) 
### 查询基于APN的SGs口控制策略(SHOW DEFAULT APNSGSCTL) 


命令功能 

该命令用于查询基于APN的SGs口控制策略。


注意事项 


无。 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
SUPAPNSGSCTL|支持基于APN的SGs口控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于APN的SGs口控制。不支持：MME不支持基于APN的SGs口控制。支持：MME支持基于APN的SGs口控制。
APNDEFSUPSGS|默认支持SGs口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME基于APN是否默认支持SGs口。不支持：默认不支持SGs口。支持：默认支持SGs口。
SUPATTNOPDN|支持附着无PDN连接流程|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME基于APN的SGs口控制是否支持物联网终端的附着无PDN连接流程，如果支持，则MME使用签约的默认APN进行SGs口控制。不支持：MME基于APN的SGs口控制不支持附着无PDN连接流程。支持：MME基于APN的SGs口控制支持附着无PDN连接流程，并使用签约的默认APN进行SGs口控制。






命令举例 


查询基于APN的SGs口默认控制策略。 


SHOW DEFAULT APNSGSCTL; 


`
命令 (No.1): SHOW DEFAULT APNSGSCTL

操作维护  支持基于APN的SGs口控制   默认支持SGs口   支持附着无PDN连接流程
------------------------------------------------------------------------
修改      支持                     支持            支持
------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 1.574 秒）。
` 








父主题： [基于APN的SGs口控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增基于APN的SGs口控制配置(ADD APNSGSCTL) 
### 新增基于APN的SGs口控制配置(ADD APNSGSCTL) 


命令功能 

该命令用于配置特定APN是否支持SGs口。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置基于用户会话APN是否开启SGs口短消息。APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。当“默认支持SGs口”设置为“不支持”时，这里配置支持SGs口及相应的APN；当“默认支持SGs口”设置为“支持”时，这里配置不支持SGs口及相应的APN。
SUPSGS|支持SGs口|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于用户会话APN是否支持SGs口。不支持：不支持SGs口。支持：支持SGs口。当“默认支持SGs口”设置为“不支持”时，这里配置支持SGs口及相应的APN；当“默认支持SGs口”设置为“支持”时，这里配置不支持SGs口及相应的APN。






命令举例 


新增基于APN的SGs口控制配置，APN名称为zte，对于此APN不支持SGs口。 


ADD APNSGSCTL:APN="zte",SUPSGS="NO"; 








父主题： [基于APN的SGs口控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改基于APN的SGs口控制配置(SET APNSGSCTL) 
### 修改基于APN的SGs口控制配置(SET APNSGSCTL) 


命令功能 

该命令用于修改特定APN是否支持SGs口的配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置基于用户会话APN是否开启SGs口短消息。APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。当“默认支持SGs口”设置为“不支持”时，这里配置支持SGs口及相应的APN；当“默认支持SGs口”设置为“支持”时，这里配置不支持SGs口及相应的APN。
SUPSGS|支持SGs口|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于用户会话APN是否支持SGs口。不支持：不支持SGs口。支持：支持SGs口。当“默认支持SGs口”设置为“不支持”时，这里配置支持SGs口及相应的APN；当“默认支持SGs口”设置为“支持”时，这里配置不支持SGs口及相应的APN。






命令举例 


修改基于APN的SGs口控制配置，APN名称为zte，对于此APN支持SGs口。 


SET APNSGSCTL:APN="zte",SUPSGS="YES"; 








父主题： [基于APN的SGs口控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除基于APN的SGs口控制配置(DEL APNSGSCTL) 
### 删除基于APN的SGs口控制配置(DEL APNSGSCTL) 


命令功能 

该命令用于删除特定APN是否支持SGs口的配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置基于用户会话APN是否开启SGs口短消息。APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。当“默认支持SGs口”设置为“不支持”时，这里配置支持SGs口及相应的APN；当“默认支持SGs口”设置为“支持”时，这里配置不支持SGs口及相应的APN。






命令举例 


删除名称为zte的APN所对应的SGs口控制配置。 


DEL APNSGSCTL:APN="zte"; 








父主题： [基于APN的SGs口控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询基于APN的SGs口控制配置(SHOW APNSGSCTL) 
### 查询基于APN的SGs口控制配置(SHOW APNSGSCTL) 


命令功能 

该命令用于查询特定APN是否支持SGs口。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置基于用户会话APN是否开启SGs口短消息。APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。当“默认支持SGs口”设置为“不支持”时，这里配置支持SGs口及相应的APN；当“默认支持SGs口”设置为“支持”时，这里配置不支持SGs口及相应的APN。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置基于用户会话APN是否开启SGs口短消息。APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。当“默认支持SGs口”设置为“不支持”时，这里配置支持SGs口及相应的APN；当“默认支持SGs口”设置为“支持”时，这里配置不支持SGs口及相应的APN。
SUPSGS|支持SGs口|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于用户会话APN是否支持SGs口。不支持：不支持SGs口。支持：支持SGs口。当“默认支持SGs口”设置为“不支持”时，这里配置支持SGs口及相应的APN；当“默认支持SGs口”设置为“支持”时，这里配置不支持SGs口及相应的APN。






命令举例 


查询基于APN的SGs口控制配置。 


SHOW APNSGSCTL; 


`
命令 (No.1): SHOW APNSGSCTL

操作维护         APN名称   支持SGs口
------------------------------------
复制 修改 删除   zte       不支持
------------------------------------
记录数 1

命令执行成功（耗时 0.088 秒）。
` 








父主题： [基于APN的SGs口控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MME IMSI鉴权配置 
# MME IMSI鉴权配置 


背景知识 


鉴权的作用，是防止未授权的PS业务使用，防止用户相关数据被窃听和篡改等威胁到用户和网络安全的行为。 


MME可以通过策略控制网络侧发起的鉴权场景和频度。MME能够针对全局设置策略控制，也能区分用户，即针对IMSI号段设置鉴权策略。 




功能描述 


MME根据不同的业务流程控制是否对用户鉴权，MME支持的可控制的流程包括IMSI附着、局内GUTI附着、RAT内局间附着、跨RAT局间附着、局内正常TAU、局内周期性TAU、RAT内局间TAU、跨RAT局间TAU、局内切换后TAU、RAT内局间切换后TAU、跨RAT局间切换后TAU、业务请求、Detach请求。用户在进行上述流程时，MME根据IMSI号段或者全局缺省IMSI号段配置选择对应的策略进行鉴权控制。流程如下： 





                    如果用户IMSI在"MME IMSI鉴权配置"（命令为
                    [ADD MME IMSI AUTH]
                    ）号段范围内，则按此处配置的鉴权策略进行控制。
                



                    如果没有用户IMSI对应的号段记录，则采用“默认MME IMSI鉴权配置”（命令为
                    [ADD MME IMSI AUTH]
                    ）中配置的缺省鉴权策略进行控制。
                






相关主题 



 

新增MME IMSI鉴权配置(ADD MME IMSI AUTH)
 

 

修改MME IMSI鉴权配置(SET MME IMSI AUTH)
 

 

删除MME IMSI鉴权配置(DEL MME IMSI AUTH)
 

 

查询MME IMSI鉴权配置(SHOW MME IMSI AUTH)
 

 

设置默认MME IMSI鉴权配置(SET MME IMSI AUTH DEFAULT)
 

 

查询默认MME IMSI鉴权配置(SHOW MME IMSI AUTH DEFAULT)
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增MME IMSI鉴权配置(ADD MME IMSI AUTH) 
## 新增MME IMSI鉴权配置(ADD MME IMSI AUTH) 


命令功能 


该命令用于MME新增基于IMSI号段和业务类型的鉴权策略。 


当运营商需要根据IMSI号段和业务类型设置不同的鉴权策略时使用该命令。 


当该命令配置成功后，MME针对不同IMSI号段的用户和不同的业务采取对应鉴权策略。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SERVICETYPE|业务类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|业务类型如下：IMSI附着：附着流程使用IMSI作为用户信息。局内GUTI附着：同一个MME内的附着流程使用GUTI作为用户信息。RAT内局间附着：不同的MME之间的附着流程。局内正常TAU：同一个MME内的正常的跟踪区更新流程。业务请求：业务请求流程。Detach请求：分离流程。跨RAT局间附着：SGSN到MME之间的附着流程。局内周期性TAU：同一个MME内的周期性的跟踪区更新流程。RAT内局间TAU：不同MME之间的跟踪区更新流程。跨RAT局间TAU：SGSN到MME之间的跟踪区更新流程。局内切换后TAU：同一个MME内的切换之后的跟踪区更新流程。RAT内局间切换后TAU：不同MME之间的切换之后的跟踪区更新流程。跨RAT局间切换后TAU：SGSN到MME的切换之后的跟踪区更新流程。5G到4G局间附着：基于N26接口，从AMF到MME的附着流程。5G到4G局间TAU：基于N26接口，从AMF到MME的跟踪区更新流程。5G到4G局间切换后TAU：基于N26接口，从AMF切换到MME之后的跟踪区更新流程。
AUTHTYPE|鉴权类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:System。|鉴权类型包括以下五种：系统判断：表示该IMSI号段的相应流程根据系统判断进行鉴权控制。具体如下：局内附着、局内TAU、局间HO之后的TAU在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。局间附着、局间TAU在以下场景会进行鉴权：老局为SGSN。老局SGSN返回P-TMSI Signature Mismatch。老局MME返回的鉴权失败。在Identification response指示了Request Accept，但是没有携带安全上下文。非关机类型的Detach在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。Initial UE形式上来的Detach。按频次鉴权：表示集中统计该IMSI号段所有用户的相应流程，当号段内的某个用户执行该流程时，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权；否则不进行鉴权。强制鉴权：表示该IMSI号段的相应流程每次都需要鉴权。强制不鉴权：表示该IMSI号段的相应流程每次都不需要鉴权。单用户频次鉴权：表示该IMSI号段的所有用户各自单独统计相应流程的次数，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要进行鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权，并将统计次数清零；否则不进行鉴权。
AUTHTIMES|鉴权周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:5。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的M。
AUTHSELNUM|鉴权选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:1。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的N。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|运营商可以根据自己的命名习惯来为鉴权配置定义一个名称。






命令举例 


新增一条IMSI号段为4600112345678，业务类型为IMSIATTACH，鉴权类型为强制鉴权，鉴权周期频次为3，名称为Auth1的配置。 


ADD MME IMSI AUTH:IMSI="4600112345678",SERVICETYPE="IMSIATTACH",AUTHTYPE="Force",AUTHTIMES=3,NAME="Auth1"; 








父主题： [MME IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改MME IMSI鉴权配置(SET MME IMSI AUTH) 
## 修改MME IMSI鉴权配置(SET MME IMSI AUTH) 


命令功能 


该命令用于修改MME IMSI鉴权配置。 


根据IMSI号段和流程类型定位到需要修改的鉴权策略。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SERVICETYPE|业务类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|业务类型如下：IMSI附着：附着流程使用IMSI作为用户信息。局内GUTI附着：同一个MME内的附着流程使用GUTI作为用户信息。RAT内局间附着：不同的MME之间的附着流程。局内正常TAU：同一个MME内的正常的跟踪区更新流程。业务请求：业务请求流程。Detach请求：分离流程。跨RAT局间附着：SGSN到MME之间的附着流程。局内周期性TAU：同一个MME内的周期性的跟踪区更新流程。RAT内局间TAU：不同MME之间的跟踪区更新流程。跨RAT局间TAU：SGSN到MME之间的跟踪区更新流程。局内切换后TAU：同一个MME内的切换之后的跟踪区更新流程。RAT内局间切换后TAU：不同MME之间的切换之后的跟踪区更新流程。跨RAT局间切换后TAU：SGSN到MME的切换之后的跟踪区更新流程。5G到4G局间附着：基于N26接口，从AMF到MME的附着流程。5G到4G局间TAU：基于N26接口，从AMF到MME的跟踪区更新流程。5G到4G局间切换后TAU：基于N26接口，从AMF切换到MME之后的跟踪区更新流程。
AUTHTYPE|鉴权类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|鉴权类型包括以下五种：系统判断：表示该IMSI号段的相应流程根据系统判断进行鉴权控制。具体如下：局内附着、局内TAU、局间HO之后的TAU在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。局间附着、局间TAU在以下场景会进行鉴权：老局为SGSN。老局SGSN返回P-TMSI Signature Mismatch。老局MME返回的鉴权失败。在Identification response指示了Request Accept，但是没有携带安全上下文。非关机类型的Detach在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。Initial UE形式上来的Detach。按频次鉴权：表示集中统计该IMSI号段所有用户的相应流程，当号段内的某个用户执行该流程时，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权；否则不进行鉴权。强制鉴权：表示该IMSI号段的相应流程每次都需要鉴权。强制不鉴权：表示该IMSI号段的相应流程每次都不需要鉴权。单用户频次鉴权：表示该IMSI号段的所有用户各自单独统计相应流程的次数，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要进行鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权，并将统计次数清零；否则不进行鉴权。
AUTHTIMES|鉴权周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的M。
AUTHSELNUM|鉴权选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的N。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|运营商可以根据自己的命名习惯来为鉴权配置定义一个名称。






命令举例 


修改一条IMSI号段为4600112345678，业务类型为IMSIATTACH，鉴权类型为系统判断，鉴权周期频次为2，名称为Auth2的配置。 


SET MME IMSI AUTH:IMSI="4600112345678",SERVICETYPE="IMSIATTACH",AUTHTYPE="System",AUTHTIMES=2,NAME="Auth2"; 








父主题： [MME IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除MME IMSI鉴权配置(DEL MME IMSI AUTH) 
## 删除MME IMSI鉴权配置(DEL MME IMSI AUTH) 


命令功能 


该命令用于根据IMSI号段删除MME IMSI鉴权配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|业务类型如下：IMSI附着：附着流程使用IMSI作为用户信息。局内GUTI附着：同一个MME内的附着流程使用GUTI作为用户信息。RAT内局间附着：不同的MME之间的附着流程。局内正常TAU：同一个MME内的正常的跟踪区更新流程。业务请求：业务请求流程。Detach请求：分离流程。跨RAT局间附着：SGSN到MME之间的附着流程。局内周期性TAU：同一个MME内的周期性的跟踪区更新流程。RAT内局间TAU：不同MME之间的跟踪区更新流程。跨RAT局间TAU：SGSN到MME之间的跟踪区更新流程。局内切换后TAU：同一个MME内的切换之后的跟踪区更新流程。RAT内局间切换后TAU：不同MME之间的切换之后的跟踪区更新流程。跨RAT局间切换后TAU：SGSN到MME的切换之后的跟踪区更新流程。5G到4G局间附着：基于N26接口，从AMF到MME的附着流程。5G到4G局间TAU：基于N26接口，从AMF到MME的跟踪区更新流程。5G到4G局间切换后TAU：基于N26接口，从AMF切换到MME之后的跟踪区更新流程。






命令举例 


删除一条IMSI号段为4600112345678，业务类型为IMSIATTACH的配置。 


DEL MME IMSI AUTH:IMSI="4600112345678",SERVICETYPE="IMSIATTACH"; 








父主题： [MME IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询MME IMSI鉴权配置(SHOW MME IMSI AUTH) 
## 查询MME IMSI鉴权配置(SHOW MME IMSI AUTH) 


命令功能 


该命令用于通过IMSI号段查询当前MME IMSI鉴权配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|业务类型如下：IMSI附着：附着流程使用IMSI作为用户信息。局内GUTI附着：同一个MME内的附着流程使用GUTI作为用户信息。RAT内局间附着：不同的MME之间的附着流程。局内正常TAU：同一个MME内的正常的跟踪区更新流程。业务请求：业务请求流程。Detach请求：分离流程。跨RAT局间附着：SGSN到MME之间的附着流程。局内周期性TAU：同一个MME内的周期性的跟踪区更新流程。RAT内局间TAU：不同MME之间的跟踪区更新流程。跨RAT局间TAU：SGSN到MME之间的跟踪区更新流程。局内切换后TAU：同一个MME内的切换之后的跟踪区更新流程。RAT内局间切换后TAU：不同MME之间的切换之后的跟踪区更新流程。跨RAT局间切换后TAU：SGSN到MME的切换之后的跟踪区更新流程。5G到4G局间附着：基于N26接口，从AMF到MME的附着流程。5G到4G局间TAU：基于N26接口，从AMF到MME的跟踪区更新流程。5G到4G局间切换后TAU：基于N26接口，从AMF切换到MME之后的跟踪区更新流程。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|业务类型如下：IMSI附着：附着流程使用IMSI作为用户信息。局内GUTI附着：同一个MME内的附着流程使用GUTI作为用户信息。RAT内局间附着：不同的MME之间的附着流程。局内正常TAU：同一个MME内的正常的跟踪区更新流程。业务请求：业务请求流程。Detach请求：分离流程。跨RAT局间附着：SGSN到MME之间的附着流程。局内周期性TAU：同一个MME内的周期性的跟踪区更新流程。RAT内局间TAU：不同MME之间的跟踪区更新流程。跨RAT局间TAU：SGSN到MME之间的跟踪区更新流程。局内切换后TAU：同一个MME内的切换之后的跟踪区更新流程。RAT内局间切换后TAU：不同MME之间的切换之后的跟踪区更新流程。跨RAT局间切换后TAU：SGSN到MME的切换之后的跟踪区更新流程。5G到4G局间附着：基于N26接口，从AMF到MME的附着流程。5G到4G局间TAU：基于N26接口，从AMF到MME的跟踪区更新流程。5G到4G局间切换后TAU：基于N26接口，从AMF切换到MME之后的跟踪区更新流程。
AUTHTYPE|鉴权类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|鉴权类型包括以下五种：系统判断：表示该IMSI号段的相应流程根据系统判断进行鉴权控制。具体如下：局内附着、局内TAU、局间HO之后的TAU在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。局间附着、局间TAU在以下场景会进行鉴权：老局为SGSN。老局SGSN返回P-TMSI Signature Mismatch。老局MME返回的鉴权失败。在Identification response指示了Request Accept，但是没有携带安全上下文。非关机类型的Detach在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。Initial UE形式上来的Detach。按频次鉴权：表示集中统计该IMSI号段所有用户的相应流程，当号段内的某个用户执行该流程时，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权；否则不进行鉴权。强制鉴权：表示该IMSI号段的相应流程每次都需要鉴权。强制不鉴权：表示该IMSI号段的相应流程每次都不需要鉴权。单用户频次鉴权：表示该IMSI号段的所有用户各自单独统计相应流程的次数，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要进行鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权，并将统计次数清零；否则不进行鉴权。
AUTHTIMES|鉴权周期频次|参数可选性:任选参数；参数类型:整数。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的M。
AUTHSELNUM|鉴权选中频次|参数可选性:任选参数；参数类型:整数。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的N。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|运营商可以根据自己的命名习惯来为鉴权配置定义一个名称。






命令举例 


查询IMSI号段为46001000001，业务类型为IMSIATTACH的鉴权配置。 


SHOW MME IMSI AUTH:IMSI="46001000001",SERVICETYPE="IMSIATTACH"; 


`

命令 (No.1): SHOW MME IMSI AUTH:IMSI="46001000001",SERVICETYPE="IMSIATTACH";

操作维护	     IMSI号段	   业务类型	    鉴权类型	     鉴权周期频次	鉴权选中频次   用户别名
---------------------------------------------------------------------------------------------------
复制 修改 删除   46001000001   IMSI附着     按频次鉴权       5              1              auth1
---------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.035 秒）。
` 








父主题： [MME IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置默认MME IMSI鉴权配置(SET MME IMSI AUTH DEFAULT) 
## 设置默认MME IMSI鉴权配置(SET MME IMSI AUTH DEFAULT) 


命令功能 


本命令用于设置与IMSI号段无关的MME全局的缺省鉴权策略配置，当用户的IMSI号码在配置条目中没有匹配项时适用此配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
SERVICETYPE|业务类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|业务类型如下：IMSI附着：附着流程使用IMSI作为用户信息。局内GUTI附着：同一个MME内的附着流程使用GUTI作为用户信息。RAT内局间附着：不同的MME之间的附着流程。局内正常TAU：同一个MME内的正常的跟踪区更新流程。业务请求：业务请求流程。Detach请求：分离流程。跨RAT局间附着：SGSN到MME之间的附着流程。局内周期性TAU：同一个MME内的周期性的跟踪区更新流程。RAT内局间TAU：不同MME之间的跟踪区更新流程。跨RAT局间TAU：SGSN到MME之间的跟踪区更新流程。局内切换后TAU：同一个MME内的切换之后的跟踪区更新流程。RAT内局间切换后TAU：不同MME之间的切换之后的跟踪区更新流程。跨RAT局间切换后TAU：SGSN到MME的切换之后的跟踪区更新流程。5G到4G局间附着：基于N26接口，从AMF到MME的附着流程。5G到4G局间TAU：基于N26接口，从AMF到MME的跟踪区更新流程。5G到4G局间切换后TAU：基于N26接口，从AMF切换到MME之后的跟踪区更新流程。
AUTHTYPE|鉴权类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|鉴权类型包括以下五种：系统判断：表示该IMSI号段的相应流程根据系统判断进行鉴权控制。具体如下：局内附着、局内TAU、局间HO之后的TAU在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。局间附着、局间TAU在以下场景会进行鉴权：老局为SGSN。老局SGSN返回P-TMSI Signature Mismatch。老局MME返回的鉴权失败。在Identification response指示了Request Accept，但是没有携带安全上下文。非关机类型的Detach在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。Initial UE形式上来的Detach。按频次鉴权：表示集中统计该IMSI号段所有用户的相应流程，当号段内的某个用户执行该流程时，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权；否则不进行鉴权。强制鉴权：表示该IMSI号段的相应流程每次都需要鉴权。强制不鉴权：表示该IMSI号段的相应流程每次都不需要鉴权。单用户频次鉴权：表示该IMSI号段的所有用户各自单独统计相应流程的次数，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要进行鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权，并将统计次数清零；否则不进行鉴权。
AUTHTIMES|鉴权周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的M。
AUTHSELNUM|鉴权选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的N。






命令举例 


设置默认MME IMSI鉴权配置，其中业务类型为局内TUDI附着，业务类型为系统判断，鉴权周期频次为200，鉴权选中频次100。 


SET MME IMSI AUTH DEFAULT:SERVICETYPE="GUTI",AUTHTYPE="System",AUTHTIMES=200,AUTHSELNUM=100; 








父主题： [MME IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询默认MME IMSI鉴权配置(SHOW MME IMSI AUTH DEFAULT) 
## 查询默认MME IMSI鉴权配置(SHOW MME IMSI AUTH DEFAULT) 


命令功能 


本命令用于显示与IMSI号段无关的MME全局的缺省鉴权策略配置，当用户的IMSI号码在配置条目中没有匹配项时适用此配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|业务类型如下：IMSI附着：附着流程使用IMSI作为用户信息。局内GUTI附着：同一个MME内的附着流程使用GUTI作为用户信息。RAT内局间附着：不同的MME之间的附着流程。局内正常TAU：同一个MME内的正常的跟踪区更新流程。业务请求：业务请求流程。Detach请求：分离流程。跨RAT局间附着：SGSN到MME之间的附着流程。局内周期性TAU：同一个MME内的周期性的跟踪区更新流程。RAT内局间TAU：不同MME之间的跟踪区更新流程。跨RAT局间TAU：SGSN到MME之间的跟踪区更新流程。局内切换后TAU：同一个MME内的切换之后的跟踪区更新流程。RAT内局间切换后TAU：不同MME之间的切换之后的跟踪区更新流程。跨RAT局间切换后TAU：SGSN到MME的切换之后的跟踪区更新流程。5G到4G局间附着：基于N26接口，从AMF到MME的附着流程。5G到4G局间TAU：基于N26接口，从AMF到MME的跟踪区更新流程。5G到4G局间切换后TAU：基于N26接口，从AMF切换到MME之后的跟踪区更新流程。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|业务类型如下：IMSI附着：附着流程使用IMSI作为用户信息。局内GUTI附着：同一个MME内的附着流程使用GUTI作为用户信息。RAT内局间附着：不同的MME之间的附着流程。局内正常TAU：同一个MME内的正常的跟踪区更新流程。业务请求：业务请求流程。Detach请求：分离流程。跨RAT局间附着：SGSN到MME之间的附着流程。局内周期性TAU：同一个MME内的周期性的跟踪区更新流程。RAT内局间TAU：不同MME之间的跟踪区更新流程。跨RAT局间TAU：SGSN到MME之间的跟踪区更新流程。局内切换后TAU：同一个MME内的切换之后的跟踪区更新流程。RAT内局间切换后TAU：不同MME之间的切换之后的跟踪区更新流程。跨RAT局间切换后TAU：SGSN到MME的切换之后的跟踪区更新流程。5G到4G局间附着：基于N26接口，从AMF到MME的附着流程。5G到4G局间TAU：基于N26接口，从AMF到MME的跟踪区更新流程。5G到4G局间切换后TAU：基于N26接口，从AMF切换到MME之后的跟踪区更新流程。
AUTHTYPE|鉴权类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|鉴权类型包括以下五种：系统判断：表示该IMSI号段的相应流程根据系统判断进行鉴权控制。具体如下：局内附着、局内TAU、局间HO之后的TAU在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。局间附着、局间TAU在以下场景会进行鉴权：老局为SGSN。老局SGSN返回P-TMSI Signature Mismatch。老局MME返回的鉴权失败。在Identification response指示了Request Accept，但是没有携带安全上下文。非关机类型的Detach在以下场景会进行鉴权：MAC码检查不通过。上行NAS消息没有安全上下文。上行NAS消息没有安全头。Initial UE形式上来的Detach。按频次鉴权：表示集中统计该IMSI号段所有用户的相应流程，当号段内的某个用户执行该流程时，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权；否则不进行鉴权。强制鉴权：表示该IMSI号段的相应流程每次都需要鉴权。强制不鉴权：表示该IMSI号段的相应流程每次都不需要鉴权。单用户频次鉴权：表示该IMSI号段的所有用户各自单独统计相应流程的次数，每隔M次可以进行鉴权时，选择其中的N次进行鉴权，达到M次后，统计次数清零；如果判断不需要进行鉴权，再根据鉴权类型为系统判断方式进行判断是否进行鉴权，如果要鉴权，则对用户进行鉴权，并将统计次数清零；否则不进行鉴权。
AUTHTIMES|鉴权周期频次|参数可选性:任选参数；参数类型:整数。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的M。
AUTHSELNUM|鉴权选中频次|参数可选性:任选参数；参数类型:整数。|按频次鉴权可以表示为一个分数N/M，每隔M次可以进行鉴权时，选择其中的N次进行鉴权。本参数就是其中的N。






命令举例 


查询默认MME IMSI鉴权配置 


SHOW MME IMSI AUTH DEFAULT 


`


操作维护 业务类型            鉴权类型   鉴权周期频次 鉴权选中频次 
---------------------------------------------------------------------------
修改      IMSI附着           强制鉴权   20           10
修改      局内GUTI附着       系统判断   5            1
修改      RAT内局间附着      系统判断   5            1
修改      局内正常TAU        系统判断   5            1
修改      业务请求           系统判断   5            1
修改      Detach请求         系统判断   5            1
修改      跨RAT局间附着      系统判断   5            1
修改      局内周期性TAU      系统判断   5            1
修改      RAT内局间TAU       系统判断   5            1
修改      跨RAT局间TAU       系统判断   5            1
修改      局内切换后TAU      系统判断   5            1
修改      RAT内局间切换后TAU 系统判断   5            1
修改      跨RAT局间切换后TAU 系统判断   5            1
---------------------------------------------------------------------------
记录数 13

命令执行成功（耗时 0.079 秒）。
` 








父主题： [MME IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MME GUTI重分配配置 
# MME GUTI重分配配置 


背景知识 


GUTI（Globally Unique Temporary Identity）是由MME为移动用户分配的全球唯一临时标识，由GUMMEI（Global Unique MME Identity）和M-TMSI（MME Temporal Mobile Subscriber Identity）两部分组成。 



 

GUMMEI用于标识MME，一个MME可以拥有多个GUMMEI。
 

 

M-TMSI用于在MME内部唯一标识一个移动用户。
 

 


MME选择一个本局支持的GUMMEI，并按自己的分配规则为移动用户分配M-TMSI，从而组成GUTI。 


MME通过在不同的时机给移动用户分配不同的GUTI，可以保护移动用户的通讯信息不被非法偷窥。 


【术语】 


周期TAU：TAU请求消息中EPS更新类型为周期更新的TAU流程。 


正常TAU：TAU请求消息中EPS更新类型为除周期更新之外的TAU流程。 




功能描述 


MME能根据需要对可选的GUTI重分配过程执行按比例的GUTI重分配。 


比例通过由两个整数组成的分数形式表示：比如比例为N/M，即表示每M次可选的GUTI重分配将会有N次被实际执行。 


比例值需要针对不同的业务流程分别配置，并且在同一业务流程中，针对MME全局或者指定的IMSI号段还可以设定不同的执行比例。 


【注意】 


有些GUTI重分配流程是必须的，比如一个移动用户首次接入本局的附着或者TAU流程。只有可选的GUTI重分配流程才能受到本功能的控制。 




相关主题 



 

设置MME GUTI重分配全局参数(SET MME GUTI REALLOC GLB)
 

 

查询MME GUTI重分配全局参数(SHOW MME GUTI REALLOC GLB)
 

 

设置MME GUTI重分配缺省配置(SET MME GUTI REALLOC DFT)
 

 

查询MME GUTI重分配缺省配置(SHOW MME GUTI REALLOC DFT)
 

 

新增MME GUTI重分配配置(ADD MME GUTI REALLOC)
 

 

修改MME GUTI重分配配置(SET MME GUTI REALLOC)
 

 

删除MME GUTI重分配配置(DEL MME GUTI REALLOC)
 

 

查询MME GUTI重分配配置(SHOW MME GUTI REALLOC)
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置MME GUTI重分配全局参数(SET MME GUTI REALLOC GLB) 
## 设置MME GUTI重分配全局参数(SET MME GUTI REALLOC GLB) 


命令功能 


该命令用于当网络运营商根据管理需要，修改GUTI按比例重分配功能全局开关为开启或关闭。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
FLAG|功能开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于打开或关闭MME全局GUTI按比例重分配功能。有两种选择：Close：关闭Open：开启






命令举例 


修改MME全局GUTI按比例重分配参数，打开全局GUTI按比例重分配功能开关。
SET MME GUTI REALLOC GLB:FLAG="OPEN"; 








父主题： [MME GUTI重分配配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询MME GUTI重分配全局参数(SHOW MME GUTI REALLOC GLB) 
## 查询MME GUTI重分配全局参数(SHOW MME GUTI REALLOC GLB) 


命令功能 


该命令用于查询是否开启了MME全局GUTI按比例重分配功能。 




注意事项 


无。 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
FLAG|功能开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于打开或关闭MME全局GUTI按比例重分配功能。有两种选择：Close：关闭Open：开启






命令举例 


查询是否开启了MME全局GUTI按比例重分配功能。
SHOW MME GUTI REALLOC GLB; 


`

命令 (No.1): SHOW MME GUTI REALLOC GLB

操作维护  功能开关
------------------
修改      关闭
------------------
记录数 1

命令执行成功（耗时 1.096 秒）。


` 








父主题： [MME GUTI重分配配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置MME GUTI重分配缺省配置(SET MME GUTI REALLOC DFT) 
## 设置MME GUTI重分配缺省配置(SET MME GUTI REALLOC DFT) 


命令功能 


该命令用于修改与IMSI号段无关的MME全局的GUTI按比例重分配配置，当用户的IMSI号码在配置条目中没有匹配项时适用此配置。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
ATTMODE|附着模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在附着流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
ATTCIRNUM|附着周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
ATTSELNUM|附着选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
NTAUMODE|正常TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在正常TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
NTAUCIRNUM|正常TAU周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
NTAUSELNUM|正常TAU选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
PTAUMODE|周期TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在周期TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
PTAUCIRNUM|周期TAU周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
PTAUSELNUM|周期TAU选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
OTHMODE|其他流程模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在其他流程（业务请求）中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
OTHCIRNUM|其他流程周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
OTHSELNUM|其他流程选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。






命令举例 


修改MME GUTI重分配缺省配置，设置附着模式为集中比按比例，附着周期频次为200，附着选中频次为180。
SET MME GUTI REALLOC DFT:ATTMODE="GROUPR",ATTCIRNUM=200,ATTSELNUM=180; 








父主题： [MME GUTI重分配配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询MME GUTI重分配缺省配置(SHOW MME GUTI REALLOC DFT) 
## 查询MME GUTI重分配缺省配置(SHOW MME GUTI REALLOC DFT) 


命令功能 


该命令用于显示与IMSI号段无关的MME全局的GUTI按比例重分配配置，当用户的IMSI号码在配置条目中没有匹配项时适用此配置。 




注意事项 


无。 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ATTMODE|附着模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在附着流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
ATTCIRNUM|附着周期频次|参数可选性:任选参数；参数类型:字符型。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
ATTSELNUM|附着选中频次|参数可选性:任选参数；参数类型:字符型。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
NTAUMODE|正常TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在正常TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
NTAUCIRNUM|正常TAU周期频次|参数可选性:任选参数；参数类型:字符型。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
NTAUSELNUM|正常TAU选中频次|参数可选性:任选参数；参数类型:字符型。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
PTAUMODE|周期TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在周期TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
PTAUCIRNUM|周期TAU周期频次|参数可选性:任选参数；参数类型:字符型。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
PTAUSELNUM|周期TAU选中频次|参数可选性:任选参数；参数类型:字符型。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
OTHMODE|其他流程模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在其他流程（业务请求）中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
OTHCIRNUM|其他流程周期频次|参数可选性:任选参数；参数类型:字符型。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
OTHSELNUM|其他流程选中频次|参数可选性:任选参数；参数类型:字符型。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。






命令举例 


查询MME GUTI重分配缺省配置。
SHOW MME GUTI REALLOC DFT; 


`

命令 (No.1): SHOW MME GUTI REALLOC DFT

操作维护  附着模式       附着周期频次   附着选中频次   正常TAU模式    正常TAU周期频次   正常TAU选中频次   周期TAU模式    周期TAU周期频次   周期TAU选中频次   其他流程模式   其他流程周期频次   其他流程选中频次
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      系统判断       100            20             系统判断       100               20                系统判断       100               20                系统判断       100                0
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.048 秒）。


` 








父主题： [MME GUTI重分配配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增MME GUTI重分配配置(ADD MME GUTI REALLOC) 
## 新增MME GUTI重分配配置(ADD MME GUTI REALLOC) 


命令功能 


该命令用于新增基于IMSI号段配置的MME GUTI按比例重分配策略。 


当运营商需要根据IMSI号段设置不同的GUTI按比例重分配策略时使用该命令。 


当该命令配置成功后，MME使用与IMSI号段和流程类型匹配的GUTI按比例重分配策略执行GUTI重分配流程。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段是IMSI号码中顶头的一串数字，来标识具有特定号码开头的一组用户。如46001表示IMSI以46001开头的所有用户。
ATTMODE|附着模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:SYSTEMD。|在附着流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
ATTCIRNUM|附着周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:100。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
ATTSELNUM|附着选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:20。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
NTAUMODE|正常TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:SYSTEMD。|在正常TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
NTAUCIRNUM|正常TAU周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:100。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
NTAUSELNUM|正常TAU选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:20。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
PTAUMODE|周期TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:SYSTEMD。|在周期TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
PTAUCIRNUM|周期TAU周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:100。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
PTAUSELNUM|周期TAU选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:20。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
OTHMODE|其他流程模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:GROUPR。|在其他流程（业务请求）中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
OTHCIRNUM|其他流程周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:100。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
OTHSELNUM|其他流程选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:0。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。






命令举例 


新增MME GUTI重分配配置，新增IMSI号段46001，附着模式为集中按比例，附着周期频次为200，附着选中频次为100，正常TAU模式为单用户按比例，正常TAU周期频次为100，正常TAU选中频次为20的记录。
ADD MME GUTI REALLOC:IMSI="46001",ATTMODE="GROUPR",ATTCIRNUM=200,ATTSELNUM=100,NTAUMODE="SINGLER",NTAUCIRNUM=100,NTAUSELNUM=20; 








父主题： [MME GUTI重分配配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改MME GUTI重分配配置(SET MME GUTI REALLOC) 
## 修改MME GUTI重分配配置(SET MME GUTI REALLOC) 


命令功能 


该命令用于修改基于IMSI号段配置的MME GUTI按比例重分配策略。 


根据IMSI号段定位到需要修改的GUTI按比例重分配策略。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段是IMSI号码中顶头的一串数字，来标识具有特定号码开头的一组用户。如46001表示IMSI以46001开头的所有用户。
ATTMODE|附着模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在附着流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
ATTCIRNUM|附着周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
ATTSELNUM|附着选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
NTAUMODE|正常TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在正常TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
NTAUCIRNUM|正常TAU周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
NTAUSELNUM|正常TAU选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
PTAUMODE|周期TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在周期TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
PTAUCIRNUM|周期TAU周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
PTAUSELNUM|周期TAU选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
OTHMODE|其他流程模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在其他流程（业务请求）中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
OTHCIRNUM|其他流程周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
OTHSELNUM|其他流程选中频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。






命令举例 


修改MME GUTI重分配配置，修改IMSI号段46001，附着模式为单用户按比例，附着周期频次为100，附着选中频次为80。
SET MME GUTI REALLOC:IMSI="46001",ATTMODE="SINGLER",ATTCIRNUM=100,ATTSELNUM=80; 








父主题： [MME GUTI重分配配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除MME GUTI重分配配置(DEL MME GUTI REALLOC) 
## 删除MME GUTI重分配配置(DEL MME GUTI REALLOC) 


命令功能 


该命令用于当网络运营商根据管理需要，删除基于某个IMSI号段MME GUTI按比例重分配策略的配置。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段是IMSI号码中顶头的一串数字，来标识具有特定号码开头的一组用户。如46001表示IMSI以46001开头的所有用户。






命令举例 


删除IMSI号段为46001的MME GUTI重分配配置。
DEL MME GUTI REALLOC:IMSI="46001"; 








父主题： [MME GUTI重分配配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询MME GUTI重分配配置(SHOW MME GUTI REALLOC) 
## 查询MME GUTI重分配配置(SHOW MME GUTI REALLOC) 


命令功能 


该命令用于通过IMSI号段查询当前MME GUTI按比例重分配配置。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI号段是IMSI号码中顶头的一串数字，来标识具有特定号码开头的一组用户。如46001表示IMSI以46001开头的所有用户。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|IMSI号段是IMSI号码中顶头的一串数字，来标识具有特定号码开头的一组用户。如46001表示IMSI以46001开头的所有用户。
ATTMODE|附着模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在附着流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
ATTCIRNUM|附着周期频次|参数可选性:任选参数；参数类型:字符型。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
ATTSELNUM|附着选中频次|参数可选性:任选参数；参数类型:字符型。|用于附着流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
NTAUMODE|正常TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在正常TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
NTAUCIRNUM|正常TAU周期频次|参数可选性:任选参数；参数类型:字符型。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
NTAUSELNUM|正常TAU选中频次|参数可选性:任选参数；参数类型:字符型。|用于正常TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
PTAUMODE|周期TAU模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在周期TAU流程中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
PTAUCIRNUM|周期TAU周期频次|参数可选性:任选参数；参数类型:字符型。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
PTAUSELNUM|周期TAU选中频次|参数可选性:任选参数；参数类型:字符型。|用于周期TAU流程。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。
OTHMODE|其他流程模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在其他流程（业务请求）中，可选的GUTI重分配是否采用按比例控制。有三种选择：系统判断：不按比例控制，由系统自行决定是否需要重分配。集中按比例：匹配号段的所有用户合并统计可GUTI重分配的次数，并在群组范围内分配GUTI重分配机会。单用户按比例：匹配号段的用户单独统计可GUTI重分配的次数和需要GUTI重分配的次数。
OTHCIRNUM|其他流程周期频次|参数可选性:任选参数；参数类型:字符型。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的M。
OTHSELNUM|其他流程选中频次|参数可选性:任选参数；参数类型:字符型。|用于其他流程（业务请求）。GUTI按比例重分配中的比例可以表示为一个分数N/M，每隔M次可以进行GUTI重分配时，选择其中的N次进行GUTI重分配。本参数就是其中的N。






命令举例 


查询当前MME GUTI按比例重分配配置。
SHOW MME GUTI REALLOC; 


`

命令 (No.1): SHOW MME GUTI REALLOC

操作维护         IMSI号段   附着模式       附着周期频次   附着选中频次   正常TAU模式    正常TAU周期频次   正常TAU选中频次   周期TAU模式    周期TAU周期频次   周期TAU选中频次   其他流程模式   其他流程周期频次   其他流程选中频次
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   46000      系统判断       100            20             系统判断       100               20                系统判断       100               20                集中按比例     100                0
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.061 秒）。
` 








父主题： [MME GUTI重分配配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SGSN IMSI鉴权配置 
# SGSN IMSI鉴权配置 


背景知识 


鉴权的作用，是防止未授权的PS业务使用，防止用户相关数据被窃听和篡改等威胁到用户和网络安全的行为。 


Gn/Gp SGSN可以通过策略控制网络侧发起的鉴权场景和频度。Gn/Gp SGSN能够针对全局设置策略控制，也能区分用户，即针对IMSI号段设置鉴权策略。 




功能描述 


Gn/Gp SGSN根据不同的业务流程控制是否对用户鉴权，Gn/Gp SGSN支持的可控制的流程包括附着、路由更新、业务请求、Gb口PDP激活、Gb口短消息始呼和Gb口短消息终呼呼。用户在进行上述流程时，Gn/Gp SGSN根据IMSI号段选择对应的策略进行鉴权控制。 


"SGSN IMSI鉴权配置" 设置用户IMSI号段的鉴权策略。 



                Gn/Gp SGSN的全局鉴权策略，通过“安全参数配置”（命令行
                [SET SECURITY PARAMETER]
                ）进行配置。
            




相关主题 



 

新增SGSN IMSI鉴权配置(ADD SGSN IMSI AUTH)
 

 

修改SGSN IMSI鉴权配置(SET SGSN IMSI AUTH)
 

 

删除SGSN IMSI鉴权配置(DEL SGSN IMSI AUTH)
 

 

查询SGSN IMSI鉴权配置(SHOW SGSN IMSI AUTH)
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增SGSN IMSI鉴权配置(ADD SGSN IMSI AUTH) 
## 新增SGSN IMSI鉴权配置(ADD SGSN IMSI AUTH) 


命令功能 


该命令用于新增Gn/Gp SGSN IMSI鉴权配置。当需要对某IMSI段单独进行鉴权控制时，使用该命令。该命令使用后，所配置IMSI段依照配置的鉴权控制方式，决定是否进行鉴权。 


如果Gn/Gp SGSN根据IMSI号段和流程类别没有查找到配置记录，则鉴权按照安全参数配置中安全变量来控制。 




注意事项 


鉴权类型为按频次鉴权时，如果不指定鉴权频次，默认值为2。 


鉴权类型不为按频次鉴权时，鉴权频次参数不允许配置。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于指定需要配置的进行鉴权控制的IMSI段，配置该IMSI段后，该项配置对应的鉴权控制策略对该IMSI段生效。
SERVICETYPE|业务类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要配置的进行鉴权控制的业务类型，配置该业务类型后，该项配置对应的鉴权控制策略对该IMSI段在该配置的业务类型下生效。取值含义：附着（Attach）：附着业务类型路由更新（RAU）：路由更新业务类型业务请求（Service Request）：业务请求业务类型GB接入PDP激活（PDP activation）：GB接入模式下的PDP激活业务类型GB接入短信息始呼（SMS MO）：GB接入模式下的短信息始呼GB接入短信息终呼（SMS MT）：GB接入模式下的短信息终呼局间切换后的RAU(RAU after inter-HO)：局间切换后发起的路由更新业务类型
AUTHTYPE|鉴权方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要配置的进行鉴权控制的鉴权方式，配置该业务类型后，该项配置对应的IMSI段在配置的业务类型下使用该参数对应的鉴权方式。取值含义：No_authentication（No_authentication）：强制不鉴权。Compelling_authentication（Compelling_authentication）：强制鉴权。System（System）：系统判定。by_frequency（by_frequency）：按频次鉴权
AUTHTIMES|鉴权频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于设置对IMSI段按频次进行鉴权控制时，需要鉴权的次数。该参数只有在配置了鉴权方式为按频次鉴权时才可以配置。如果配置次数为 N，则N次不鉴权，然后下一次鉴权。当配置频次为0时，每次都鉴权。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数可以配置为特定的描述，做为该项配置的备注。






命令举例 


新增IMSI鉴权配置，设置IMSI号段为46001的用户，在Attach流程中，设置鉴权方式为按频次鉴权，按鉴权频次为3进行鉴权。
ADD SGSN IMSI AUTH:IMSI="46001",SERVICETYPE="Attach",AUTHTYPE="by_frequency",AUTHTIMES=3; 








父主题： [SGSN IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改SGSN IMSI鉴权配置(SET SGSN IMSI AUTH) 
## 修改SGSN IMSI鉴权配置(SET SGSN IMSI AUTH) 


命令功能 


该命令用于修改Gn/Gp SGSN IMSI鉴权配置。根据IMSI 段、业务类型来修改鉴权类型、鉴权频次。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于指定需要配置的进行鉴权控制的IMSI段，配置该IMSI段后，该项配置对应的鉴权控制策略对该IMSI段生效。
SERVICETYPE|业务类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要配置的进行鉴权控制的业务类型，配置该业务类型后，该项配置对应的鉴权控制策略对该IMSI段在该配置的业务类型下生效。取值含义：附着（Attach）：附着业务类型路由更新（RAU）：路由更新业务类型业务请求（Service Request）：业务请求业务类型GB接入PDP激活（PDP activation）：GB接入模式下的PDP激活业务类型GB接入短信息始呼（SMS MO）：GB接入模式下的短信息始呼GB接入短信息终呼（SMS MT）：GB接入模式下的短信息终呼局间切换后的RAU(RAU after inter-HO)：局间切换后发起的路由更新业务类型
AUTHTYPE|鉴权方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要配置的进行鉴权控制的鉴权方式，配置该业务类型后，该项配置对应的IMSI段在配置的业务类型下使用该参数对应的鉴权方式。取值含义：No_authentication（No_authentication）：强制不鉴权。Compelling_authentication（Compelling_authentication）：强制鉴权。System（System）：系统判定。by_frequency（by_frequency）：按频次鉴权
AUTHTIMES|鉴权频次|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于设置对IMSI段按频次进行鉴权控制时，需要鉴权的次数。该参数只有在配置了鉴权方式为按频次鉴权时才可以配置。如果配置次数为 N，则N次不鉴权，然后下一次鉴权。当配置频次为0时，每次都鉴权。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数可以配置为特定的描述，做为该项配置的备注。






命令举例 


IMSI号段46001的用户，Attach流程时的鉴权类型为按频次鉴权，将配置的鉴权频次修改为5。
SET SGSN IMSI AUTH:IMSI="46001",SERVICETYPE="Attach",AUTHTYPE="by_frequency",AUTHTIMES=5; 








父主题： [SGSN IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除SGSN IMSI鉴权配置(DEL SGSN IMSI AUTH) 
## 删除SGSN IMSI鉴权配置(DEL SGSN IMSI AUTH) 


命令功能 


该命令用于删除Gn/Gp SGSN IMSI鉴权配置。根据IMSI 段、业务类型来删除，当不选择业务类型时，为删除IMSI段所关联的所有配置。删除该记录后，对该IMSI段的鉴权配置不再生效，该IMSI段对应用户的鉴权使用SGSN全局的鉴权配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于指定需要配置的进行鉴权控制的IMSI段，配置该IMSI段后，该项配置对应的鉴权控制策略对该IMSI段生效。
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要配置的进行鉴权控制的业务类型，配置该业务类型后，该项配置对应的鉴权控制策略对该IMSI段在该配置的业务类型下生效。取值含义：附着（Attach）：附着业务类型路由更新（RAU）：路由更新业务类型业务请求（Service Request）：业务请求业务类型GB接入PDP激活（PDP activation）：GB接入模式下的PDP激活业务类型GB接入短信息始呼（SMS MO）：GB接入模式下的短信息始呼GB接入短信息终呼（SMS MT）：GB接入模式下的短信息终呼局间切换后的RAU(RAU after inter-HO)：局间切换后发起的路由更新业务类型






命令举例 


删除IMSI号段46001的用户在Attach流程中的IMSI鉴权配置。
DEL SGSN IMSI AUTH:IMSI="46001",SERVICETYPE="Attach"; 








父主题： [SGSN IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询SGSN IMSI鉴权配置(SHOW SGSN IMSI AUTH) 
## 查询SGSN IMSI鉴权配置(SHOW SGSN IMSI AUTH) 


命令功能 


该命令用于查询Gn/Gp SGSN IMSI鉴权配置。该查询命令可以不填参数，为查询所有配置项。也可以带两个查询参数的一个或两个。这两个参数为 IMSI 段 和 业务类型，都能够查询到对应的配置项。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于指定需要配置的进行鉴权控制的IMSI段，配置该IMSI段后，该项配置对应的鉴权控制策略对该IMSI段生效。
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要配置的进行鉴权控制的业务类型，配置该业务类型后，该项配置对应的鉴权控制策略对该IMSI段在该配置的业务类型下生效。取值含义：附着（Attach）：附着业务类型路由更新（RAU）：路由更新业务类型业务请求（Service Request）：业务请求业务类型GB接入PDP激活（PDP activation）：GB接入模式下的PDP激活业务类型GB接入短信息始呼（SMS MO）：GB接入模式下的短信息始呼GB接入短信息终呼（SMS MT）：GB接入模式下的短信息终呼局间切换后的RAU(RAU after inter-HO)：局间切换后发起的路由更新业务类型






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|该参数用于指定需要配置的进行鉴权控制的IMSI段，配置该IMSI段后，该项配置对应的鉴权控制策略对该IMSI段生效。
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要配置的进行鉴权控制的业务类型，配置该业务类型后，该项配置对应的鉴权控制策略对该IMSI段在该配置的业务类型下生效。取值含义：附着（Attach）：附着业务类型路由更新（RAU）：路由更新业务类型业务请求（Service Request）：业务请求业务类型GB接入PDP激活（PDP activation）：GB接入模式下的PDP激活业务类型GB接入短信息始呼（SMS MO）：GB接入模式下的短信息始呼GB接入短信息终呼（SMS MT）：GB接入模式下的短信息终呼局间切换后的RAU(RAU after inter-HO)：局间切换后发起的路由更新业务类型
AUTHTYPE|鉴权方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定需要配置的进行鉴权控制的鉴权方式，配置该业务类型后，该项配置对应的IMSI段在配置的业务类型下使用该参数对应的鉴权方式。取值含义：No_authentication（No_authentication）：强制不鉴权。Compelling_authentication（Compelling_authentication）：强制鉴权。System（System）：系统判定。by_frequency（by_frequency）：按频次鉴权
AUTHTIMES|鉴权频次|参数可选性:任选参数；参数类型:整数。|该参数用于设置对IMSI段按频次进行鉴权控制时，需要鉴权的次数。该参数只有在配置了鉴权方式为按频次鉴权时才可以配置。如果配置次数为 N，则N次不鉴权，然后下一次鉴权。当配置频次为0时，每次都鉴权。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数可以配置为特定的描述，做为该项配置的备注。






命令举例 


查询IMSI号段46001用户的鉴权配置。
SHOW SGSN IMSI AUTH:IMSI="46001"; 


`

命令 (No.1): SHOW SGSN IMSI AUTH:IMSI="46001";

操作维护         IMSI号段   业务类型         鉴权方式     鉴权频次   用户别名
-----------------------------------------------------------------------------
复制 修改 删除   46001      附着             频次鉴权     3          
-----------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.051 秒）。


` 








父主题： [SGSN IMSI鉴权配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# DNS配置 
# DNS配置 


背景知识 

            
            在附着、RAU/TAU、切换、PDP激活/PDN连接等业务流程中，需要获取交互的SGSN、MME、GGSN、SGW或PGW的地址，如果这些地址没有在本网元配置，则需要查询DNS服务器，此时SGSN/MME需要内置DNS客户端功能。MME/SGSN通过DNS配置来完成内置DNS客户端功能的配置。
        


功能描述 

            
            DNS配置包含了和DNS服务器交互的DNS全局参数配置、DNS服务器配置、DNS服务器组配置、DNS Profile配置、DNS服务器状态监测机制配置。
        


相关主题 



 

DNS全局配置
 

 

DNS服务器配置
 

 

DNS服务器组配置
 

 

DNS Profile配置
 

 

DNS服务器链路状态检测配置
 

 

DNS TCP链路配置
 

 








父主题： [系统配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## DNS全局配置 
## DNS全局配置 


背景知识 

            
            DNS全局配置是针对MME/SGSN作为DNS客户端的全局参数配置，用于运营商根据实际的网络情况来调整MME/SGSN和DNS服务器之间的交互质量，参数主要包括：DNS UDP查询超时时长（秒）、DNS重发次数、TTL（分钟）、DNS查询方式、支持非权威服务器SOA记录缓存、非权威服务器SOA记录缓存抑制百分比 、TCP查询方式超时时长（秒）以及TCP保活时长（秒）。
            
 

DNS UDP查询超时时长（秒）：即MME/SGSN采用UDP连接查询DNS服务器，等待DNS服务器响应的时长。运营商可以根据网络时延情况，设置MME/SGSN等待DNS服务器响应的时长。
 

 

DNS UDP重发次数：MME/SGSN重发DNS消息（基于UDP连接）的次数。当运营商希望网络瞬断对业务无影响时，即不因为一次无响应就导致业务失败，则需要配置MME/SGSN的重发次数大于1。
 

 

TTL（分钟）：即DNS记录的生存时间，该参数决定了MME/SGSN和DNS服务器交互的频率，MME/SGSN中缓存的TTL取MME/SGSN配置的TTL和DNS服务器指定的TTL中较短的值。
 

 

DNS查询方式：指MME/SGSN基于何种连接方式向DNS服务器发起查询，包括UDP、TCP和UDP优先方式。
 

 

支持非权威服务器SOA记录缓存：该参数用来控制MME/SGSN是否保存DNS服务器返回的SOA记录。
 

 

非权威服务器SOA记录缓存抑制百分比：即当MME/SGSN支持非权威服务器SOA记录缓存时，缓存的SOA记录占总缓存记录的百分比。
 

 

TCP查询方式超时时长（秒）：即MME/SGSN采用TCP连接查询DNS服务器，等待DNS服务器响应的时长。运营商可以根据网络时延情况，设置MME/SGSN等待DNS服务器响应的时长。
 

 

TCP保活时长（秒）：即MME/SGSN向DNS服务器发送保活消息的间隔时长。
 

 




功能描述 

            
            全局配置的参数包括DNS UDP查询超时时长、DNS UDP重发次数、TTL、DNS查询方式、支持非权威服务器SOA记录缓存、非权威服务器SOA记录缓存抑制百分比 、TCP查询方式超时时长以及TCP保活时长。
        


相关主题 



 

设置DNS全局参数(SET DNS GLB)
 

 

查询DNS全局参数(SHOW DNS GLB)
 

 








父主题： [DNS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置DNS全局参数(SET DNS GLB) 
### 设置DNS全局参数(SET DNS GLB) 


命令功能 

该命令用于设置MME/SGSN作为DNS客户端的全局参数，包括DNS超时时长、重发次数、TTL。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
TIMEOUT|DNS UDP查询超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~8。|DNS 超时时长，用于设置MME/SGSN作为DNS客户端等待DNS服务器响应的时长，当等待时间超过设定的时长后，MME/SGSN视DNS服务器无响应。
MAXRET|DNS UDP重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该参数用于设置DNS重发次数，即MME/SGSN等待DNS服务器响应超时后的重发次数。若该值不为零，当MME/SGSN等待DNS服务器响应超时后，会重发消息。
TTL|TTL（分钟）|参数可选性:任选参数；参数类型:整数；参数范围为:1~34560。|该参数用于设置TTL，即DNS记录的生存时间，DNS域名解析记录在时长内有效，超时后MME/SGSN需要跟DNS服务器重新请求DNS域名解析记录。
MODE|DNS查询方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置DNS查询方式，分为如下三种：UDP（UDP）：UDP方式。TCP（TCP）：TCP方式UDP优先（UDPFIRST）：UDP优先方式
SUPPNONASOACACHE|支持非权威服务器SOA记录缓存|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持非权威服务器SOA记录缓存。
NASOACACHERESPERC|非权威服务器SOA记录缓存抑制百分比|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置非权威服务器SOA记录缓存抑制百分比，如果单模块已缓存域名总数（总数是指权威服务器域名缓存数+非权威服务器域名缓存数）占本模块Cahce缓存最大数的百分比>=（大于等于）配置的“非权威服务器SOA记录缓存抑制百分比”，则uMAC对来自非权威服务器的响应消息的SOA记录不再进行缓存，否则缓存。对权威服务器的SOA记录和非SOA记录缓存以及对非权威服务器的非SOA记录缓存，不受此配置影响。
DNSTCPTIMEOUT|TCP查询方式超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~30。|该参数用于设置采用TCP查询方式时，MME等待DNS服务器响应的超时时长。
TCPALIVETIME|TCP保活时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~7200。|该参数用于设置采用TCP查询方式时，MME和DNS服务器进行定时保活的时长。
SUPPADDITIONAL|支持Additional|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持接受DNS查询响应中的additional信息。
SUPPFASTAGING|支持加速老化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持快速老化功能。
FASTAGINGTHRESHOLD|快速老化门限(%)|参数可选性:任选参数；参数类型:整数；参数范围为:50~90。|该参数用于设置快速老化的门限值，使用百分比为单位。
SUPPPROTECTCACHE|支持保护缓存|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持缓存保护功能。当MME对接的所有DNS服务器都不可达时，MME会对CACHE中已经存在的功能进行保护，保证CACHE可用，直至有DNS服务器恢复正常可使用。不支持：当所有DNS服务器不可达时，MME不支持保护缓存功能。支持：当所有DNS服务器不可达时，MME支持保护缓存功能。
PROTECTTIMELEN|缓存保护时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:0~43200。|该参数用于设置缓存保护时长，单位为分钟。缓存保护时长，表示有DNS服务器恢复正常可使用后，延长保护CACHE的时间。






命令举例 


修改DNS全局参数DNS超时时长为3秒、TTL为10分钟。 


SET DNS GLB:TIMEOUT=3,TTL=10; 








父主题： [DNS全局配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS全局参数(SHOW DNS GLB) 
### 查询DNS全局参数(SHOW DNS GLB) 


命令功能 

该命令用于查询DNS客户端全局参数。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
TIMEOUT|DNS UDP查询超时时长(秒)|参数可选性:任选参数；参数类型:整数。|DNS 超时时长，用于设置MME/SGSN作为DNS客户端等待DNS服务器响应的时长，当等待时间超过设定的时长后，MME/SGSN视DNS服务器无响应。
MAXRET|DNS UDP重发次数|参数可选性:任选参数；参数类型:整数。|该参数用于设置DNS重发次数，即MME/SGSN等待DNS服务器响应超时后的重发次数。若该值不为零，当MME/SGSN等待DNS服务器响应超时后，会重发消息。
TTL|TTL（分钟）|参数可选性:任选参数；参数类型:整数。|该参数用于设置TTL，即DNS记录的生存时间，DNS域名解析记录在时长内有效，超时后MME/SGSN需要跟DNS服务器重新请求DNS域名解析记录。
MODE|DNS查询方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置DNS查询方式，分为如下三种：UDP（UDP）：UDP方式。TCP（TCP）：TCP方式UDP优先（UDPFIRST）：UDP优先方式
SUPPNONASOACACHE|支持非权威服务器SOA记录缓存|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持非权威服务器SOA记录缓存。
NASOACACHERESPERC|非权威服务器SOA记录缓存抑制百分比|参数可选性:任选参数；参数类型:整数。|该参数用于设置非权威服务器SOA记录缓存抑制百分比，如果单模块已缓存域名总数（总数是指权威服务器域名缓存数+非权威服务器域名缓存数）占本模块Cahce缓存最大数的百分比>=（大于等于）配置的“非权威服务器SOA记录缓存抑制百分比”，则uMAC对来自非权威服务器的响应消息的SOA记录不再进行缓存，否则缓存。对权威服务器的SOA记录和非SOA记录缓存以及对非权威服务器的非SOA记录缓存，不受此配置影响。
DNSTCPTIMEOUT|TCP查询方式超时时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置采用TCP查询方式时，MME等待DNS服务器响应的超时时长。
TCPALIVETIME|TCP保活时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置采用TCP查询方式时，MME和DNS服务器进行定时保活的时长。
SUPPADDITIONAL|支持Additional|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持接受DNS查询响应中的additional信息。
SUPPFASTAGING|支持加速老化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为输出参数，用于查询显示MME是否支持加速老化。
FASTAGINGTHRESHOLD|快速老化门限(%)|参数可选性:任选参数；参数类型:整数；参数范围为:50~90。|该参数为输出参数，用于查询显示配置的快速老化门限值。
SUPPPROTECTCACHE|支持保护缓存|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为输出参数，用于查询显示MME是否支持缓存保护功能。
PROTECTTIMELEN|缓存保护时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:0~43200。|该参数为输出参数，用于查询显示配置的缓存保护时长。






命令举例 


查询DNS全局参数。 


SHOW DNS GLB; 


`

命令 (No.43): SET DNS GLB:SUPPADDITIONAL="ON";


操作维护	DNS UDP查询超时时长(秒)	  DNS UDP重发次数	     TTL（分钟）	DNS查询方式	  支持非权威服务器SOA记录缓存	非权威服务器SOA记录缓存抑制百分比	TCP查询方式超时时长(秒)	 TCP保活时长(秒)	支持Additional	支持加速老化	快速老化门限(%)	 支持保护缓存	缓存保护时长(分钟)	
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改 	    2	                     3	                     15	            UDP	          不支持	                    80	                                6	                     2	                支持	        支持	        80	             不支持	        30	
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.063 秒）。

` 








父主题： [DNS全局配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## DNS服务器配置 
## DNS服务器配置 


背景知识 


SGSN/MME作为DNS客户端，可以跟多个DNS服务器相连接。一对客户端地址和服务器地址标识一个DNS服务器。 


SGSN/MME最多连接32个DNS服务器。 




功能描述 

            
            本功能主要用于配置DNS服务器的基本信息，包括DNS客户端地址、DNS服务器端地址、VRFID、DNS服务器编号以及名称。
        


相关主题 



 

新增DNS服务器配置(ADD DNS SERVER)
 

 

修改DNS服务器配置(SET DNS SERVER)
 

 

删除DNS服务器配置(DEL DNS SERVER)
 

 

查询DNS服务器配置(SHOW DNS SERVER)
 

 








父主题： [DNS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增DNS服务器配置(ADD DNS SERVER) 
### 新增DNS服务器配置(ADD DNS SERVER) 


命令功能 

该命令用于增加DNS服务器配置，包括配置DNS客户端和服务端地址、VRFID和服务器名称。


注意事项 

DNS服务器编号自动分配，通过查询DNS服务器命令可以查询所有DNS服务器对应的编号。


参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|DNS服务器的内部编号，自动分配，便于索引和进行分组配置。
SERVERIPADDR|DNS服务器IP地址|参数可选性:必选参数；参数类型:地址|DNS服务器地址，可以是IPV4地址也可以是IPV6地址。
CLIENTIPADDR|DNS客户端IP地址|参数可选性:必选参数；参数类型:地址|DNS客户端地址，和本配置中DNS服务器IP地址同类型,即DNS客户端IP地址和DNS服务器IP地址都是IPV4或都是IPV6地址。
VRFID|VRFID|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。默认值:0。|当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置VRF标识。是在VRF配置中已经配置的VRFID。
TCPNUM|TCP链路数量|参数可选性:任选参数；参数类型:整数；参数范围为:0~4。|如需使用TCP方式访问DNS服务器，必须要配置到该DNS服务器的链路，指明需要参与负荷分担的TCP链路条数，uMAC自动生成具体的TCP链路（参见SHOW TCPLINK STATE），建议尽量和部署的最大SMP的虚机数相同。
NAME|DNS服务器名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|DNS服务器名称。






命令举例 


新增DNS服务器配置，增加DNS服务器IP地址为172.16.12.101，DNS客户端IP地址为100.51.0.52，VRFID为202，DNS服务器名称为lte.zte.com.cn的配置。
ADD DNS SERVER:SERVERIPADDR="172.16.12.101",CLIENTIPADDR="100.51.0.52",VRFID=202,NAME="lte.zte.com.cn"; 








父主题： [DNS服务器配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改DNS服务器配置(SET DNS SERVER) 
### 修改DNS服务器配置(SET DNS SERVER) 


命令功能 

该命令用于修改DNS服务器配置，可以修改服务器IP地址、客户端IP地址和VRFID。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|DNS服务器的内部编号，自动分配，便于索引和进行分组配置。
SERVERIPADDR|DNS服务器IP地址|参数可选性:任选参数；参数类型:地址|DNS服务器地址，可以是IPV4地址也可以是IPV6地址。
CLIENTIPADDR|DNS客户端IP地址|参数可选性:任选参数；参数类型:地址|DNS客户端地址，和本配置中DNS服务器IP地址同类型,即DNS客户端IP地址和DNS服务器IP地址都是IPV4或都是IPV6地址。
VRFID|VRFID|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置VRF标识。是在VRF配置中已经配置的VRFID。
TCPNUM|TCP链路数量|参数可选性:任选参数；参数类型:整数；参数范围为:0~4。|如需使用TCP方式访问DNS服务器，必须要配置到该DNS服务器的链路，指明需要参与负荷分担的TCP链路条数，uMAC自动生成具体的TCP链路（参见SHOW TCPLINK STATE），建议尽量和部署的最大SMP的虚机数相同。
NAME|DNS服务器名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|DNS服务器名称。






命令举例 


修改DNS服务器配置，修改DNS服务器编号为1的DNS服务器IP地址为172.16.12.102。
SET DNS SERVER:ID=1,SERVERIPADDR="172.16.12.102"; 








父主题： [DNS服务器配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除DNS服务器配置(DEL DNS SERVER) 
### 删除DNS服务器配置(DEL DNS SERVER) 


命令功能 

该命令用于根据DNS服务器编号删除DNS服务器配置。


注意事项 

删除的服务器不能够被服务器组配置引用。


参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|DNS服务器的内部编号，自动分配，便于索引和进行分组配置。






命令举例 


删除DNS服务器配置，删除DNS服务器编号为8的配置。
DEL DNS SERVER:ID=8; 








父主题： [DNS服务器配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS服务器配置(SHOW DNS SERVER) 
### 查询DNS服务器配置(SHOW DNS SERVER) 


命令功能 

该命令用于查询DNS服务器配置


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|DNS服务器的内部编号，自动分配，便于索引和进行分组配置。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器编号|参数可选性:任选参数；参数类型:整数。|DNS服务器的内部编号，自动分配，便于索引和进行分组配置。
SERVERIPADDR|DNS服务器IP地址|参数可选性:任选参数；参数类型:地址|DNS服务器地址，可以是IPV4地址也可以是IPV6地址。
CLIENTIPADDR|DNS客户端IP地址|参数可选性:任选参数；参数类型:地址|DNS客户端地址，和本配置中DNS服务器IP地址同类型,即DNS客户端IP地址和DNS服务器IP地址都是IPV4或都是IPV6地址。
VRFID|VRFID|参数可选性:任选参数；参数类型:整数。|当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置VRF标识。是在VRF配置中已经配置的VRFID。
TCPNUM|TCP链路数量|参数可选性:任选参数；参数类型:整数。|如需使用TCP方式访问DNS服务器，必须要配置到该DNS服务器的链路，指明需要参与负荷分担的TCP链路条数，uMAC自动生成具体的TCP链路（参见SHOW TCPLINK STATE），建议尽量和部署的最大SMP的虚机数相同。
NAME|DNS服务器名称|参数可选性:任选参数；参数类型:字符型。|DNS服务器名称。






命令举例 


查询DNS服务器配置。
SHOW DNS SERVER; 


`

命令 (No.2): SHOW DNS SERVER

操作维护         DNS服务器编号   DNS服务器IP地址   DNS客户端IP地址   VRFID   TCP链路数量   DNS服务器名称
--------------------------------------------------------------------------------------------------------
复制 修改 删除   1               172.16.12.101     100.51.0.52       202     2             lte.zte.com.cn
--------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.047 秒）。
` 








父主题： [DNS服务器配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## DNS服务器组配置 
## DNS服务器组配置 


背景知识 


一个DNS服务器组包含一个或多个DNS服务器，多个DNS服务器之间的工作模式可以是负荷分担或主备。 



 

负荷分担时，需要根据各服务器的权重进行选择，权重值越大的DNS服务器被选择的概率越高。
 

 

主备时，排列在第一个的服务器是主用DNS服务器，其余都是备用DNS服务器。备用服务器依照排列顺序，优先级逐渐降低，优先级高的服务器可达时，选择高优先级的DNS服务器。主备时，权重值无效。
 

 


一个DNS服务器组中最多可以配置4个DNS服务器。系统最多配置8个DNS服务器组。 




功能描述 

            
            本功能配置DNS服务器组中关联的DNS服务器编号、权重、DNS服务器的选择模式以及DNS服务器组的名称。
        


相关主题 



 

新增DNS服务器组配置(ADD DNS SRVGRP)
 

 

修改DNS服务器组配置(SET DNS SRVGRP)
 

 

删除DNS服务器组配置(DEL DNS SRVGRP)
 

 

查询DNS服务器组配置(SHOW DNS SRVGRP)
 

 








父主题： [DNS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增DNS服务器组配置(ADD DNS SRVGRP) 
### 新增DNS服务器组配置(ADD DNS SRVGRP) 


命令功能 

该命令用于增加DNS服务器组配置，包括服务器选择模式、DNS服务器编号、DNS服务器权重。


注意事项 


DNS服务器组中的DNS服务器是已经在DNS服务器配置中配置的，且一个DNS服务器不能够在一个DNS服务器组中重复出现。 


DNS服务器组编号自动分配，通过查询DNS服务器组命令可以查询所有DNS服务器组对应的编号。 




参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器组号|参数可选性:任选参数；参数类型:整数；参数范围为:1~8。|DNS服务器组编号，系统自动分配，在DNS Profile配置中使用。
SELECTMODE|选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BACKUP。|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRVID|DNS服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|DNS服务器编号，通过ADD DNS SERVER配置时系统自动分配的。
WEIGHT|DNS服务器权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|DNS服务器在服务器组中的权重。当选择模式为负荷分担时有效。
SVRLST|DNS服务器列表|参数可选性:必选参数；参数类型:复合参数|DNS服务器组中的服务器列表，包括DNS服务器编号和该服务器的权重。每个服务器组最多可以配置4个DNS服务器。
NAME|DNS服务器组名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|服务器组名称，用于标识一个服务器组






命令举例 


新增DNS服务器组，增加DNS服务器组编号为3，选择模式为主备，DNS服务器列表包含服务器编号1和2的配置。
ADD DNS SRVGRP:ID=3,SELECTMODE="BACKUP",SVRLST=1-0&2-0,NAME="LTE DNS Group"; 








父主题： [DNS服务器组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改DNS服务器组配置(SET DNS SRVGRP) 
### 修改DNS服务器组配置(SET DNS SRVGRP) 


命令功能 

该命令用于修改服务器选择模式、DNS服务器编号、DNS服务器权重。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器组号|参数可选性:必选参数；参数类型:整数；参数范围为:1~8。|DNS服务器组编号，系统自动分配，在DNS Profile配置中使用。
SELECTMODE|选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRVID|DNS服务器ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|DNS服务器编号，通过ADD DNS SERVER配置时系统自动分配的。
WEIGHT|DNS服务器权重|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|DNS服务器在服务器组中的权重。当选择模式为负荷分担时有效。
SVRLST|DNS服务器列表|参数可选性:任选参数；参数类型:复合参数|DNS服务器组中的服务器列表，包括DNS服务器编号和该服务器的权重。每个服务器组最多可以配置4个DNS服务器。
NAME|DNS服务器组名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|服务器组名称，用于标识一个服务器组






命令举例 


修改DNS服务器组，修改DNS服务器组编号为1记录的选择模式为负荷分担，DNS服务器组名称为LTE DNS Group1。
SET DNS SRVGRP:ID=1,SELECTMODE="PARTAKE",NAME="LTE DNS Group1"; 








父主题： [DNS服务器组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除DNS服务器组配置(DEL DNS SRVGRP) 
### 删除DNS服务器组配置(DEL DNS SRVGRP) 


命令功能 

该命令用于根据DNS服务器组编号删除DNS服务器组的配置。


注意事项 

删除的服务器组不能够被服务器Profile配置引用。


参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器组号|参数可选性:必选参数；参数类型:整数；参数范围为:1~8。|DNS服务器组编号，系统自动分配，在DNS Profile配置中使用。






命令举例 


删除DNS服务器组，删除DNS服务器组编号为3的记录。
DEL DNS SRVGRP:ID=3; 








父主题： [DNS服务器组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS服务器组配置(SHOW DNS SRVGRP) 
### 查询DNS服务器组配置(SHOW DNS SRVGRP) 


命令功能 

该命令用于查询指定服务器组编号的组配置，若不输入编号则查询所有DNS服务器组的配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器组号|参数可选性:任选参数；参数类型:整数；参数范围为:1~8。|DNS服务器组编号，系统自动分配，在DNS Profile配置中使用。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|DNS服务器组号|参数可选性:任选参数；参数类型:整数。|DNS服务器组编号，系统自动分配，在DNS Profile配置中使用。
SELECTMODE|选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRV1ID|DNS服务器1ID|参数可选性:任选参数；参数类型:整数。|DNS服务器1编号，通过ADD DNS SERVER配置的值
WEIGHT1|DNS服务器1权重|参数可选性:任选参数；参数类型:整数。|DNS服务器1在服务器组中的权重。当选择模式为负荷分担时有效。
SRV2ID|DNS服务器2ID|参数可选性:任选参数；参数类型:整数。|DNS服务器2编号，通过ADD DNS SERVER配置的值
WEIGHT2|DNS服务器2权重|参数可选性:任选参数；参数类型:整数。|DNS服务器2在服务器组中的权重。当选择模式为负荷分担时有效。
SRV3ID|DNS服务器3ID|参数可选性:任选参数；参数类型:整数。|DNS服务器3编号，通过ADD DNS SERVER配置的值
WEIGHT3|DNS服务器3权重|参数可选性:任选参数；参数类型:整数。|DNS服务器3在服务器组中的权重。当选择模式为负荷分担时有效。
SRV4ID|DNS服务器4ID|参数可选性:任选参数；参数类型:整数。|DNS服务器4编号，通过ADD DNS SERVER配置的值
WEIGHT4|DNS服务器4权重|参数可选性:任选参数；参数类型:整数。|DNS服务器4在服务器组中的权重。当选择模式为负荷分担时有效。
NAME|DNS服务器组名称|参数可选性:任选参数；参数类型:字符型。|服务器组名称，用于标识一个服务器组






命令举例 


查询DNS服务器组配置，不输入参数查询所有DNS服务器组配置 


SHOW DNS SRVGRP; 


`

命令 (No.1): SHOW DNS SRVGRP

操作维护         DNS服务器组号   选择模式   DNS服务器1ID   DNS服务器1权重   DNS服务器2ID   DNS服务器2权重   DNS服务器3ID   DNS服务器3权重   DNS服务器4ID   DNS服务器4权重   DNS服务器组名称
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1               负荷分担   1              100              2              100              3              100              4              100              
复制 修改 删除   2               主备       5              0                6              0                7              0                8              0                
复制 修改 删除   3               主备       1              0                2              0                0              0                0              0                LTE DNS服务器组
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 3

命令执行成功（耗时 0.032 秒）。

` 








父主题： [DNS服务器组配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## DNS Profile配置 
## DNS Profile配置 


背景知识 


DNS Profile是进行DNS查询时选择DNS服务器的入口，包括EPC Profile和GPRS Profile。 



 

EPC Profile用于进行EPC查询时选择DNS服务器，GPRS Profile用于进行GPRS查询时选择DNS服务器。
 

 

一个DNS profile包含一个或多个DNS服务器组，最多四个DNS服务器组，多个DNS服务器组之间可以负荷分担或主备。
 

 

负荷分担时，则需要根据各服务器组的权重进行选择，权重值越大则被选择的概率越高。
 

 

主备时，则排列在第一个的服务器组是第一优先级的服务器组，依照排列顺序，优先级逐渐降低，优先级高的服务器组中有服务器可达时，则一定选择高优先级的服务器组。主备时，权重值无效。
 

 




功能描述 

            
            本功能主要配置DNS Profile的基本信息，包括Profile的类型、Profile中关联的服务器组编号、权重和服务器组的选择模式。
        


相关主题 



 

新增DNS Profile配置(ADD DNS PROFILE)
 

 

修改DNS Profile配置(SET DNS PROFILE)
 

 

删除DNS Profile配置(DEL DNS PROFILE)
 

 

查询DNS Profile配置(SHOW DNS PROFILE)
 

 








父主题： [DNS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增DNS Profile配置(ADD DNS PROFILE) 
### 新增DNS Profile配置(ADD DNS PROFILE) 


命令功能 

该命令用于增加DNS Profile配置，主要包括DNS Profile的类型、Profile中关联的DNS服务器组列表。


注意事项 

Profile中的服务器组是已经在服务器组配置中配置的，且一个服务器组不能够在一个Profile中重复出现。


参数说明 


标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性。
SELECTMODE|选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BACKUP。|Profile中多个服务器组的选择模式。选择模式为主备或负荷分担。
SRVGRPID|DNS服务器组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~8。|DNS服务器组编号，DNS服务器组编号通过ADD DNS SRVGRP配置
WEIGHT|DNS服务器组权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|DNS服务器组在本Profile中的权重，当选择模式为负荷分担时有效。
SVRGRPLST|DNS服务器组列表|参数可选性:必选参数；参数类型:复合参数|DNS Profile中的服务器组列表，包含DNS服务器组编号和DNS服务器组权重。每个DNS Profile最多可以配置8个服务器组。






命令举例 


新增DNS Profile配置，新增DNS Profile类型为GPRS,服务器组列表包含服务器组编号1和服务器组编号2，选择模式为主备的配置。 


ADD DNS PROFILE:TYPE="GPRS",SELECTMODE="BACKUP",SVRGRPLST=1-0&2-0; 








父主题： [DNS Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改DNS Profile配置(SET DNS PROFILE) 
### 修改DNS Profile配置(SET DNS PROFILE) 


命令功能 

该命令用于修改EPC Profile或GPRS Profile的配置。包括修改Profile关联的DNS服务器组、选择模式和服务器组的权重。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性。
SELECTMODE|选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Profile中多个服务器组的选择模式。选择模式为主备或负荷分担。
SRVGRPID|DNS服务器组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~8。|DNS服务器组编号，DNS服务器组编号通过ADD DNS SRVGRP配置
WEIGHT|DNS服务器组权重|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|DNS服务器组在本Profile中的权重，当选择模式为负荷分担时有效。
SVRGRPLST|DNS服务器组列表|参数可选性:任选参数；参数类型:复合参数|DNS Profile中的服务器组列表，包含DNS服务器组编号和DNS服务器组权重。每个DNS Profile最多可以配置8个服务器组。






命令举例 


修改DNS Profile配置，修改DNS Profile类型为GPRS的记录的选择模式为负荷分担，服务器组编号1和服务器组编号2的权重为100 


SET DNS PROFILE:TYPE="GPRS",SELECTMODE="PARTAKE",SVRGRPLST=1-100&2-100 








父主题： [DNS Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除DNS Profile配置(DEL DNS PROFILE) 
### 删除DNS Profile配置(DEL DNS PROFILE) 


命令功能 

该命令用于删除EPC Profile或GPRS Profile。


注意事项 

需要确认系统不需要该类DNS查询，一旦删除，则对应的DNS查询都将无法进行。


参数说明 


标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性。






命令举例 


删除DNS Profile配置，删除DNS Profile类型为GPRS的记录 


DEL DNS PROFILE:TYPE="GPRS"; 








父主题： [DNS Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS Profile配置(SHOW DNS PROFILE) 
### 查询DNS Profile配置(SHOW DNS PROFILE) 


命令功能 

该命令用于查询EPC Profile或GPRS Profile的配置，查看Profile关联的DNS服务器组、选择模式和DNS服务器组权重。


注意事项 


无。 




输出参数说明 


标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性。
SELECTMODE|选择模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Profile中多个服务器组的选择模式。选择模式为主备或负荷分担。
SRVGRP1ID|DNS服务器组1ID|参数可选性:任选参数；参数类型:整数。|DNS服务器组1编号，DNS服务器组编号通过ADD DNS SRVGRP配置
WEIGHT1|DNS服务器组1权重|参数可选性:任选参数；参数类型:整数。|DNS服务器组1在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRP2ID|DNS服务器组2ID|参数可选性:任选参数；参数类型:整数。|DNS服务器组2编号，DNS服务器组编号通过ADD DNS SRVGRP配置
WEIGHT2|DNS服务器组2权重|参数可选性:任选参数；参数类型:整数。|DNS服务器组2在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRP3ID|DNS服务器组3ID|参数可选性:任选参数；参数类型:整数。|DNS服务器组3编号，DNS服务器组编号通过ADD DNS SRVGRP配置
WEIGHT3|DNS服务器组3权重|参数可选性:任选参数；参数类型:整数。|DNS服务器组3在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRP4ID|DNS服务器组4ID|参数可选性:任选参数；参数类型:整数。|DNS服务器组4编号，DNS服务器组编号通过ADD DNS SRVGRP配置
WEIGHT4|DNS服务器组4权重|参数可选性:任选参数；参数类型:整数。|DNS服务器组4在本Profile中的权重，当选择模式为负荷分担时有效。






命令举例 


查询DNS Profile配置，不输入参数查询所有DNS Profile配置。 


SHOW DNS PROFILE; 


`

命令 (No.1): SHOW DNS PROFILE

操作维护         DNS Profile类型   选择模式   DNS服务器组1ID   DNS服务器组1权重   DNS服务器组2ID   DNS服务器组2权重   DNS服务器组3ID   DNS服务器组3权重   DNS服务器组4ID   DNS服务器组4权重
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   GPRS              主备       1                0                  0                0                  0                0                  0                0
复制 修改 删除   LTE               主备       2                0                  0                0                  0                0                  0                0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.068 秒）。
` 








父主题： [DNS Profile配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## DNS服务器链路状态检测配置 
## DNS服务器链路状态检测配置 


背景知识 


DNS服务器链路状态检测包括故障检测和故障恢复检测两方面功能。在本配置中故障检测周期即可用服务器检测周期，故障恢复检测周期即故障服务器握手周期。 



 

故障检测，是指对当前可用的DNS服务器进行定时检测，以便尽快了解其是否故障。
 

 

故障恢复检测，是指对当前处于不可用的DNS服务器进行定时检测，以确定其是否恢复可用。
 

 


DNS服务器检测方式分为三种类型。 



 

业务触发的检测，是指在业务查询连续失败多次的情况下，将服务器状态置为不可用。
 

 

标准协议方式的检测，是指按照DNS协议的要求在查询请求中明确指示是状态请求。
 

 

自定义查询的检测，是指通过在服务器端配置一个固定的业务不会使用的查询记录，客户端定时查询该记录，以确定服务器状态。
 

 




功能描述 

            
            本功能配置DNS服务器的检测方式、故障检测周期、故障恢复检测周期以及各检测模式下需要的参数。
        


相关主题 



 

设置DNS服务器链路状态检测配置(SET DNS SRVCHECK)
 

 

查询DNS服务器链路状态检测配置(SHOW DNS SRVCHECK)
 

 








父主题： [DNS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置DNS服务器状态检测配置(SET DNS SRVCHECK) 
### 设置DNS服务器状态检测配置(SET DNS SRVCHECK) 


命令功能 

该命令用于修改DNS服务器状态检测配置。


注意事项 

当配置DNS检测方式为标准协议方式时，需要通过调研或对接测试确认所有相连的DNS服务器都支持。


参数说明 


标识|名称|类型|说明
---|---|---|---
CHECKTYPE|检测方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|检测方式，分为如下四种：标准协议方式自定义查询组合模式
FLTCHKTIME|可用服务器检测周期（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:15~300。|状态可达的DNS服务器检测周期，即故障检测周期，当检测方式为标准协议或自定义查询时，必需配置。
RESENDNUM|重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|检测消息的响应超时时重发次数，当检测方式为标准协议或自定义查询时，必需配置。
TIMEOUT|握手超时时长（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|检测消息的响应超时时重发时长，当检测方式为标准协议或自定义查询时，必需配置。
RECOVERTIME|故障服务器握手周期（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:15~300。|状态不可达的DNS服务器的状态检测周期，即故障恢复周期，当检测方式为标准协议或自定义查询时，必需配置。
RECOVTIME|告警恢复时长（分钟）|参数可选性:任选参数；参数类型:整数；参数范围为:1~30。|检测方式为业务触发时，则故障发生时间和当前时间差大于等于本配置时，自动回复服务器为可用，即将告警进行恢复，后继业务可以选择该DNS Server。
QNAME|查询名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|检测方式为自定义查询方式时的查询字符串。当检查方式配置为“自定义查询”时，可以配置一个域名。当检查方式配置为“组合模式”时，可以配置五个域名。其他场景配置，不可配置本域名。
TCPPROTOCOLCHECK|支持TCP协议检测服务器状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否支持TCP协议方式的服务器状态检测。只有配置DNS支持TCP查询方式才能配置支持TCP协议方式的服务器状态检测。通过SHOW DNS GLB查看DNS查询方式。






命令举例 


修改DNS服务器UDP链路状态检测配置，修改检测方式为标准协议类型，可用服务器检测周期为150秒，重发次数为2次，支持TCP协议检测服务器状态。 


SET DNS SRVCHECK:CHECKTYPE="PROTOCAL",FLTCHKTIME=150,RESENDNUM=2,TCPPROTOCOLCHECK="ON"; 








父主题： [DNS服务器链路状态检测配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS服务器状态检测配置(SHOW DNS SRVCHECK) 
### 查询DNS服务器状态检测配置(SHOW DNS SRVCHECK) 


命令功能 

该命令用于查询DNS服务器状态检测配置。


注意事项 

无


输出参数说明 


标识|名称|类型|说明
---|---|---|---
CHECKTYPE|检测方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|检测方式，分为如下四种：标准协议方式自定义查询组合模式
FLTCHKTIME|可用服务器检测周期（秒）|参数可选性:任选参数；参数类型:整数。|状态可达的DNS服务器检测周期，即故障检测周期，当检测方式为标准协议或自定义查询时，必需配置。
RESENDNUM|重发次数|参数可选性:任选参数；参数类型:整数。|检测消息的响应超时时重发次数，当检测方式为标准协议或自定义查询时，必需配置。
TIMEOUT|握手超时时长（秒）|参数可选性:任选参数；参数类型:整数。|检测消息的响应超时时重发时长，当检测方式为标准协议或自定义查询时，必需配置。
RECOVERTIME|故障服务器握手周期（秒）|参数可选性:任选参数；参数类型:整数。|状态不可达的DNS服务器的状态检测周期，即故障恢复周期，当检测方式为标准协议或自定义查询时，必需配置。
RECOVTIME|告警恢复时长（分钟）|参数可选性:任选参数；参数类型:整数。|检测方式为业务触发时，则故障发生时间和当前时间差大于等于本配置时，自动回复服务器为可用，即将告警进行恢复，后继业务可以选择该DNS Server。
QNAME|查询名称|参数可选性:任选参数；参数类型:字符型。|检测方式为自定义查询方式时的查询字符串。当检查方式配置为“自定义查询”时，可以配置一个域名。当检查方式配置为“组合模式”时，可以配置五个域名。其他场景配置，不可配置本域名。
TCPPROTOCOLCHECK|支持TCP协议检测服务器状态|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否支持TCP协议方式的服务器状态检测。只有配置DNS支持TCP查询方式才能配置支持TCP协议方式的服务器状态检测。通过SHOW DNS GLB查看DNS查询方式。






命令举例 


查询DNS服务器状态检测配置，不输入参数查询所有查询DNS服务器状态检测配置。 


SHOW DNS SRVCHECK; 


`

命令 (No.1): SHOW DNS SRVCHECK

操作维护  检测方式       可用服务器检测周期（秒）   重发次数   握手超时时长（秒）   故障服务器握手周期（秒）   告警恢复时长（分钟）   查询名称  支持TCP协议检测服务器状态
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      业务触发       180                        3          2                    180                        10                               不支持                  
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.031 秒）。

` 








父主题： [DNS服务器链路状态检测配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## DNS TCP链路配置 
## DNS TCP链路配置 


背景知识 

            
            TCP协议是面向连接的协议，TCP连接由服务器地址、客户端地址、VRF和管理模块等信息组成。uMAC网元可以通过配置一条DNS TCP链路来管理和DNS服务器之间的TCP连接；其中TCP连接的基本信息如服务器地址、客户端地址、VRF通过DNS服务器配置获取。
        


功能描述 

            
            本功能用于配置DNS查询时所使用的DNS客户端与DNS服务器之间的TCP链路，通过DNS TCP链路编号将本局和DNS服务器关联起来
        


相关主题 



 

查询DNS TCP链路配置(SHOW DNS TCPLINK)
 

 








父主题： [DNS配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询DNS TCP链路配置(SHOW DNS TCPLINK) 
### 查询DNS TCP链路配置(SHOW DNS TCPLINK) 


命令功能 

该命令用于查询DNS客户端到DNS服务器的TCP链路，不输入参数查询所有记录。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
LINKID|DNS TCP链路编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|自定的TCP 链路的内部编号，便于内部索引，关联或查询。
SVRID|DNS服务器编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|DNS服务器的内部编号，在DNS服务器配置命令中配置，通过ADD DNS SERVER配置。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
LINKID|DNS TCP链路编号|参数可选性:任选参数；参数类型:整数。|自定的TCP 链路的内部编号，便于内部索引，关联或查询。
SVRID|DNS服务器编号|参数可选性:任选参数；参数类型:整数。|DNS服务器的内部编号，在DNS服务器配置命令中配置，通过ADD DNS SERVER配置。






命令举例 


查询DNS客户端到DNS服务器的所有TCP链路。 


SHOW DNS TCPLINK; 


`

命令 (No.3): SHOW DNS TCPLINK

DNS TCP链路编号   DNS服务器编号
-------------------------------
1                 1
17                17
-------------------------------
记录数 2

命令执行成功（耗时 0.022 秒）。
` 








父主题： [DNS TCP链路配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


