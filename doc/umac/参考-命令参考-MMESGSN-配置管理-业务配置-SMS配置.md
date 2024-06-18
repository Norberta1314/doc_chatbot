 SMS配置 


[](None)背景知识 

            
            GPRS附着的移动台，当其在GERAN/UTRAN PS覆盖下，可以在PS域进行点对点的短消息收发。仅仅GPRS附着而没有IMSI附着的移动台，只能在PS完成短消息业务，而同时GPRS附着和IMSI附着的移动台，则在CS域和PS域都可以完成短消息业务。
        


[](None)功能描述 

            
            “SMS配置”主要实现的是PS域短消息定制化功能的相关配置，普通的短消息业务并不需要进行本配置；定制化的功能包括：短消息中心地址修正功能，使用“短消息中心地址修正配置”；短消息中心地址黑名单功能，使用“短消息中心地址黑名单配置”；以及GPRS业务设置失败而引发的短消息通知功能，使用“GPRS业务失败错误码配置”和“短消息通知配置”，分别用来配置通知内容和通知策略。
        


[](None)相关主题 



 

短消息通知配置
 

 

GPRS错误码配置
 

 

SMSC地址修正规则配置
 

 

SMSC地址黑名单配置
 

 








父主题： [业务配置](../../zh-CN/tree/N_126085_operation_cm_mml_umacV4_cm_combo_gngp_service.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 短消息通知配置 
# 短消息通知配置 


[](None)背景知识 


MS（Mobile Station，移动台）在PS域实现点对点短消息业务时，SGSN通常只作为中间节点，负责短消息的传输，并不作为短消息实体产生短消息下发给用户。 


定制化的短消息功能是指，SGSN支持根据运营商的要求，主动构造短消息下发给用户，对用户使用的业务进行短消息通知。 




[](None)功能描述 


此功能是一种定制化的短消息功能，用于在以下两种情况中，由SGSN网元主动构造短消息（包括短消息内容和主叫号码）下发给用户： 



 

通知用户发生了局间RAU（Routing Area Update，路由区更新）。
 

 

通知用户终端设备中的APN配置错误。
 

 


本功能涉及到两项配置：包括“短消息通知配置”和“GPRS错误码配置”。 



 


                        “短消息通知配置”，用于配置该项功能的总开关（即
                        SET SMS NOTIFY
                        命令中的参数“是否支持发送失败原因”）、下发的短消息中的主叫号码和消息内容的编码方式。
                    
 

 

“GPRS错误码配置”，用于配置两种场景下的短消息通知开关，以及两种场景下短消息通知的文本内容。
 

 




[](None)相关主题 



 

设置短消息通知配置(SET SMS NOTIFY)
 

 

查询短消息通知配置(SHOW SMS NOTIFY)
 

 








父主题： [SMS配置](../../zh-CN/tree/N_1254470.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置短消息通知配置(SET SMS NOTIFY) 
## 设置短消息通知配置(SET SMS NOTIFY) 


[](None)命令功能 


该命令用于短消息通知配置。当需要通知用户发生了局间路由更新或通知用户终端设备中的APN配置错误时使用该命令。该命令配置成功后，当用户发生了局间路由更新或因为用户带上来的APN错误导致激活失败时，SGSN会查看该配置中的“是否发送失败原因”，如果设置为支持，并且“GPRS错误码”配置中的“失败原因是否启用”为启用时，则通过短信方式主动通知到用户，短信内容包括“GPRS错误码”配置中的“失败原因”，短信发送方号码为本配置中的“主叫号码”。  




[](None)注意事项 


是否通知用户局间路由更新或手机APN错误需要结合“短消息通知配置”和“GPRS错误码配置来决定”。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ENABLE|是否支持发送失败原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否支持发送失败原因，指的是当用户发生了局间路由更新或因为用户带上来的APN错误导致激活失败时，SGSN是否支持通过短信方式主动通知到用户。是（YES）：表示支持否（NO）：表示不支持
CODETYPE|编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编码方式，有三种选项：8-bit，UCS2 alpha，alphabet。
CALLNUM|主叫号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|短消息发送方号码。






[](None)命令举例 


设置短消息通知信息，其中不支持发送失败原因，编码方式为8-bit，主叫号码为861390511。 


SET SMS NOTIFY:ENABLE="NO",CODETYPE="8-bit",CALLNUM="861390511"; 








父主题： [短消息通知配置](../../zh-CN/tree/N_1254471.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询短消息通知配置(SHOW SMS NOTIFY) 
## 查询短消息通知配置(SHOW SMS NOTIFY) 


[](None)命令功能 


该命令用于查询短消息通知配置。 




[](None)注意事项 

无


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ENABLE|是否支持发送失败原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否支持发送失败原因，指的是当用户发生了局间路由更新或因为用户带上来的APN错误导致激活失败时，SGSN是否支持通过短信方式主动通知到用户。是（YES）：表示支持否（NO）：表示不支持
CODETYPE|编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编码方式，有三种选项：8-bit，UCS2 alpha，alphabet。
CALLNUM|主叫号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|短消息发送方号码。






[](None)命令举例 


查询已配置的短消息通知。 


SHOW SMS NOTIFY; 


`
命令 (No.1): SHOW SMS NOTIFY

操作维护 是否支持发送失败原因 编码方式 主叫号码 
------------------------------------------------------
修改  不支持 8-bit 861390511 
------------------------------------------------------
记录数 1

命令执行成功（耗时 0.031 秒）。
` 








父主题： [短消息通知配置](../../zh-CN/tree/N_1254471.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# GPRS错误码配置 
# GPRS错误码配置 


[](None)背景知识 


MS（Mobile Station，移动台）在PS域实现点对点短消息业务时，SGSN通常只作为中间节点，负责短消息的传输，并不作为短消息实体产生短消息下发给用户。 


定制化的短消息功能是指，SGSN支持根据运营商的要求，主动构造短消息下发给用户，对用户使用的业务进行短消息通知。 




[](None)功能描述 


此功能是一种定制化的短消息功能，用于在以下两种情况中，由SGSN网元主动构造短消息（包括短消息内容和主叫号码）下发给用户： 



 

通知用户发生了局间RAU（Routing Area Update，路由区更新）。
 

 

通知用户终端设备中的APN配置错误。
 

 


本功能涉及到两项配置：包括“短消息通知配置”和“GPRS错误码配置”。 



 


                        “短消息通知配置”，用于配置该项功能的总开关（即
                        SET SMS NOTIFY
                        命令中的参数“是否支持发送失败原因”）、下发的短消息中的主叫号码和消息内容的编码方式。
                    
 

 

“GPRS错误码配置”，用于配置两种场景下的短消息通知开关，以及两种场景下短消息通知的文本内容。
 

 




[](None)相关主题 



 

新增GPRS错误码配置(ADD SMS ERRCAUSS)
 

 

修改GPRS错误码配置(SET SMS ERRCAUSS)
 

 

删除GPRS错误码配置(DEL SMS ERRCAUSS)
 

 

查询GPRS错误码配置(SHOW SMS ERRCAUSS)
 

 








父主题： [SMS配置](../../zh-CN/tree/N_1254470.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增GPRS错误码配置(ADD SMS ERRCAUSS) 
## 新增GPRS错误码配置(ADD SMS ERRCAUSS) 


[](None)命令功能 


该命令用于新增GPRS错误码配置。当SGSN需要通知终端发生了局间路由更新，或通知终端进行APN检查并发现错误时使用该命令。该命令设置成功后，当终端发生了局间路由更新或终端带上来的APN错误导致终端激活失败时，如果“短消息通知配置”中的“是否发送失败原因”启用，则会根据本命令的配置信息，通过短信方式主动通知到终端，短信中的内容即为该配置中的失败原因信息。 




[](None)注意事项 


是否通知用户局间路由更新或手机APN错误需要结合“短消息通知配置”和“GPRS错误码配置来决定”。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
OMMERRCODE|失败原因错误码|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|失败原因错误码，包括APN错误和路由更新通知。
ENABLE|失败原因是否启用|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|当终端的APN配置错误导致用户激活失败或者局间路由更新时，设置是否通过短消息携带失败原因通知到用户。启用（ENABLE）：允许SGSN通过短消息方式发送失败原因给用户。不启用（DISABLE）：不允许SGSN通过短消息方式发送失败原因给用户。
ERRINFO|失败原因|参数可选性:必选参数；参数类型:字符型；参数范围为:1~140个字符。|根据APN错误或路由更新通知，设置对应的失败原因。当终端由于APN配置错误导致终端激活失败或者局间路由发生更新时，SGSN根据“失败原因”中设置的内容发送给终端。当“失败原因是否启用”设置为“启用”时，此设置才生效。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|备注作用，用户区分不同的失败原因。






[](None)命令举例 


新增GPRS错误码配置，其中失败原因错误码为APN错误，启用失败原因，失败原因是“您的APN设置错误”。 


ADD SMS ERRCAUSS:OMMERRCODE="APN Fail",ENABLE="ENABLE",ERRINFO="您的APN设置错误"; 








父主题： [GPRS错误码配置](../../zh-CN/tree/N_1254472.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改GPRS错误码配置(SET SMS ERRCAUSS) 
## 修改GPRS错误码配置(SET SMS ERRCAUSS) 


[](None)命令功能 


该命令用于修改GPRS错误码配置。当GPRS错误码配置信息发送变化时，可以使用此命令。可根据失败原因错误码来修改对应失败原因信息、用户别名以及是否启用此失败原因。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
OMMERRCODE|失败原因错误码|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|失败原因错误码，包括APN错误和路由更新通知。
ENABLE|失败原因是否启用|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当终端的APN配置错误导致用户激活失败或者局间路由更新时，设置是否通过短消息携带失败原因通知到用户。启用（ENABLE）：允许SGSN通过短消息方式发送失败原因给用户。不启用（DISABLE）：不允许SGSN通过短消息方式发送失败原因给用户。
ERRINFO|失败原因|参数可选性:任选参数；参数类型:字符型；参数范围为:0~140个字符。|根据APN错误或路由更新通知，设置对应的失败原因。当终端由于APN配置错误导致终端激活失败或者局间路由发生更新时，SGSN根据“失败原因”中设置的内容发送给终端。当“失败原因是否启用”设置为“启用”时，此设置才生效。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|备注作用，用户区分不同的失败原因。






[](None)命令举例 


修改错误码为APN错误的GPRS错误码配置，将用户别名修改为zte。 


SET SMS ERRCAUSS:OMMERRCODE="APN Fail",NAME="zte";  








父主题： [GPRS错误码配置](../../zh-CN/tree/N_1254472.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除GPRS错误码配置(DEL SMS ERRCAUSS) 
## 删除GPRS错误码配置(DEL SMS ERRCAUSS) 


[](None)命令功能 


该命令用于删除GPRS错误码配置。当此GPRS错误码不需要再使用时，可使用此命令。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
OMMERRCODE|失败原因错误码|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|失败原因错误码，包括APN错误和路由更新通知。






[](None)命令举例 


删除错误码为APN错误的GPRS错误码配置。 


DEL SMS ERRCAUSS:OMMERRCODE="APN Fail";  








父主题： [GPRS错误码配置](../../zh-CN/tree/N_1254472.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询GPRS错误码配置(SHOW SMS ERRCAUSS) 
## 查询GPRS错误码配置(SHOW SMS ERRCAUSS) 


[](None)命令功能 


该命令用于查询GPRS错误码配置。查询方式如下： 



 
不设置任何参数，则显示所有的GPRS错误码配置信息，包括APN错误码和路由更新通知的配置信息。
 

 
根据APN错误码查询，则显示APN错误码的配置信息。
 

 
根据路由更新通知查询，则显示路由更新通知的配置信息。
 

 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
OMMERRCODE|失败原因错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|失败原因错误码，包括APN错误和路由更新通知。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
OMMERRCODE|失败原因错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|失败原因错误码，包括APN错误和路由更新通知。
ENABLE|失败原因是否启用|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当终端的APN配置错误导致用户激活失败或者局间路由更新时，设置是否通过短消息携带失败原因通知到用户。启用（ENABLE）：允许SGSN通过短消息方式发送失败原因给用户。不启用（DISABLE）：不允许SGSN通过短消息方式发送失败原因给用户。
ERRINFO|失败原因|参数可选性:任选参数；参数类型:字符型；参数范围为:0~140个字符。|根据APN错误或路由更新通知，设置对应的失败原因。当终端由于APN配置错误导致终端激活失败或者局间路由发生更新时，SGSN根据“失败原因”中设置的内容发送给终端。当“失败原因是否启用”设置为“启用”时，此设置才生效。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|备注作用，用户区分不同的失败原因。






[](None)命令举例 


查询已配置的GPRS错误码配置。 


SHOW SMS ERRCAUSS;  


`
命令 (No.1): SHOW SMS ERRCAUSS

操作维护 失败原因错误码 失败原因是否启用 失败原因 用户别名 
---------------------------------------------------
复制 修改 删除  APN错误 启用 1  
---------------------------------------------------
记录数 2

命令执行成功（耗时 0.031 秒）。
` 








父主题： [GPRS错误码配置](../../zh-CN/tree/N_1254472.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SMSC地址修正规则配置 
# SMSC地址修正规则配置 


[](None)背景知识 


SMSC（Short Message Service Center，短消息中心）是在MS（Mobile Station，移动台）和短消息实体（短消息的提交者或者接收者，包括手机用户、自动台、人工台等用户）之间传递和保存短消息的功能实体。 


MS所连接的SMSC为E.164格式的号码，格式为：CC（Country Code，国家码）+NDC（National Destination Code，国内目的码）+SN（Subscriber Number，用户号码），SMSC号码在PLMN内可以唯一标识一个SMSC。 


MS发送短消息，向SGSN或MSC发送RP_MO_DATA消息，消息中需要携带SMSC号码，通过SMSC号码来标识请求的SMSC。 


SGSN根据MS携带的SMSC号码，将短消息路由到相应的MSC以及SMSC。如果SMSC号码错误，将导致短消息流程失败。 




[](None)功能描述 

            
            SMSC地址修正功能，是指SGSN根据用户的IMSI号段，在用户由于错误的设置了SMSC号码，而导致无法发送短消息的情况，对RP_MO_DATA消息中携带的SMSC号码进行修正，使短消息能够正常发送，从而降低了发送短消息的失败率。
        


[](None)相关主题 



 

新增SMSC地址修正规则配置(ADD SMSC MODIFY RULE)
 

 

修改SMSC地址修正规则配置(SET SMSC MODIFY RULE)
 

 

删除SMSC地址修正规则配置(DEL SMSC MODIFY RULE)
 

 

查询SMSC地址修正规则配置(SHOW SMSC MODIFY RULE)
 

 








父主题： [SMS配置](../../zh-CN/tree/N_1254470.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增SMSC地址修正规则配置(ADD SMSC MODIFY RULE) 
## 新增SMSC地址修正规则配置(ADD SMSC MODIFY RULE) 


[](None)命令功能 


该命令用于新增SMSC地址修正规则配置。如果PS数据卡设置的SMSC地址错误，则会导致短消息的发送失败，此时可以通过此命令来对SMCS地址进行修改，使短消息能够正常发送，从而降低了短消息的发送失败率。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
RULE|SMSC地址修正规则|参数可选性:必选参数；参数类型:复合参数|SMSC地址修正规则为复合参数，包括两个子参数：待修正的SMSC地址段修正后的SMSC地址
SRCSMSC|待修正的SMSC地址段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~38个字符。|待修正的短消息中心的GT号码地址。
MDFSMSC|修正后的SMSC地址|参数可选性:必选参数；参数类型:字符型；参数范围为:1~38个字符。|修正后的短消息中心的GT号码地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名。用户备注不同短消息中心地址的修正规则。






[](None)命令举例 


新增SMSC地址修正规则，其中IMSI号段为46001，待修正的SMSC地址段为8613800451500，修正后的SMSC地址段为8613800451550，用户别名为11。 


ADD SMSC MODIFY RULE:IMSI="46001",RULE="8613800451500"-"8613800451550",NAME="11";  








父主题： [SMSC地址修正规则配置](../../zh-CN/tree/N_1254473.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改SMSC地址修正规则配置(SET SMSC MODIFY RULE) 
## 修改SMSC地址修正规则配置(SET SMSC MODIFY RULE) 


[](None)命令功能 


该命令用于修改SMSC地址修正规则配置。当SMSC修正的地址发生变化时需要使用此命令。执行命令成功后，用户发送的短消息到修改后的SMSC地址。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SRCSMSC|待修正的SMSC地址段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~38个字符。|待修正的短消息中心的GT号码地址。
MDFSMSC|修正后的SMSC地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~38个字符。|修正后的短消息中心的GT号码地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名。用户备注不同短消息中心地址的修正规则。






[](None)命令举例 


修改SMSC地址修正规则，其中IMSI号段为46001，待修正的SMSC地址段为8613800451500，修正后的SMSC地址段为8613800451530。 


SET SMSC MODIFY RULE:IMSI="46001",SRCSMSC="8613800451500",MDFSMSC="8613800451530"; 








父主题： [SMSC地址修正规则配置](../../zh-CN/tree/N_1254473.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除SMSC地址修正规则配置(DEL SMSC MODIFY RULE) 
## 删除SMSC地址修正规则配置(DEL SMSC MODIFY RULE) 


[](None)命令功能 


该命令用于删除SMSC地址修正规则配置。删除后，该修正规则失效。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SRCSMSC|待修正的SMSC地址段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~38个字符。|待修正的短消息中心的GT号码地址。






[](None)命令举例 


删除SMSC地址修正规则，规则的IMSI号段为46001，待修正的SMSC地址段为8613800451500。 


DEL SMSC MODIFY RULE:IMSI="46001",SRCSMSC="8613800451500";  








父主题： [SMSC地址修正规则配置](../../zh-CN/tree/N_1254473.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询SMSC地址修正规则配置(SHOW SMSC MODIFY RULE) 
## 查询SMSC地址修正规则配置(SHOW SMSC MODIFY RULE) 


[](None)命令功能 


该命令用于查询SMSC地址修正规则配置。 




[](None)注意事项 

无


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SRCSMSC|待修正的SMSC地址段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~38个字符。|待修正的短消息中心的GT号码地址。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
SRCSMSC|待修正的SMSC地址段|参数可选性:任选参数；参数类型:字符型。|待修正的短消息中心的GT号码地址。
MDFSMSC|修正后的SMSC地址|参数可选性:任选参数；参数类型:字符型。|修正后的短消息中心的GT号码地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户别名。用户备注不同短消息中心地址的修正规则。






[](None)命令举例 


查询已配置的SMSC地址修正规则。 


SHOW SMSC MODIFY RULE;  


`
命令 (No.1): SHOW SMSC MODIFY RULE

操作维护 IMSI号段 待修正的SMSC地址段 修正后的SMSC地址 用户别名 
----------------------------------------------------------------------------
复制 修改 删除  46001 8613800451500 8613800451550 11 
----------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.031 秒）。
` 








父主题： [SMSC地址修正规则配置](../../zh-CN/tree/N_1254473.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SMSC地址黑名单配置 
# SMSC地址黑名单配置 


[](None)背景知识 


SMSC（Short Message Service Center，短消息中心）是在MS（Mobile Station，移动台）和短消息实体（短消息的提交者或者接收者，包括手机用户、自动台、人工台等用户）之间传递和保存短消息的功能实体。 


MS所连接的SMSC为E.164格式的号码，格式为：CC（Country Code，国家码）+NDC（National Destination Code，国内目的码）+SN（Subscriber Number，用户号码），SMSC号码在PLMN内可以唯一标识一个SMSC。 


MS发送短消息，向SGSN或MSC发送RP_MO_DATA消息，消息中需要携带SMSC号码，通过SMSC号码来标识请求的SMSC。 


SGSN根据MS携带的SMSC号码，将短消息路由到相应的MSC以及SMSC。如果SMSC号码错误，将导致短消息流程失败。 




[](None)功能描述 

            
            本功能支持将部分SMSC号码列入黑名单，使得用户发往该SMSC的短消息，都将被拒绝而无法发送。
        


[](None)相关主题 



 

新增SMSC地址黑名单配置(ADD SMSC BLACKLIST)
 

 

删除SMSC地址黑名单配置(DEL SMSC BLACKLIST)
 

 

查询SMSC地址黑名单配置(SHOW SMSC BLACKLIST)
 

 








父主题： [SMS配置](../../zh-CN/tree/N_1254470.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增SMSC地址黑名单配置(ADD SMSC BLACKLIST) 
## 新增SMSC地址黑名单配置(ADD SMSC BLACKLIST) 


[](None)命令功能 


该命令用于新增SMSC地址黑名单配置。当需要定制开发，不允许使用一些SMSC来发送SMS 时使用该命令。设置SMSC地址黑名单成功后，用户经过PS域发送到这些SMSC地址的短信会发送失败。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SMSCADDR|SMSC地址黑名单|参数可选性:必选参数；参数类型:字符型；参数范围为:1~38个字符。|列为黑名单的短消息中心的GT号码。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起备注作用，用于区分不同的SMSC黑名单地址。






[](None)命令举例 


新增SMSC地址黑名单配置，其中SMSC地址为861380045151，用户别名为11。 


ADD SMSC BLACKLIST:SMSCADDR="861380045151",NAME="11";  








父主题： [SMSC地址黑名单配置](../../zh-CN/tree/N_1254474.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除SMSC地址黑名单配置(DEL SMSC BLACKLIST) 
## 删除SMSC地址黑名单配置(DEL SMSC BLACKLIST) 


[](None)命令功能 


该命令用于删除SMSC地址黑名单配置，运营商需要从黑名单中去除该SMSC地址时使用，当删除后，用户经过PS域的短消息可以通过SGSN正常发送到这个SMSC上。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SMSCADDR|SMSC地址黑名单|参数可选性:必选参数；参数类型:字符型；参数范围为:1~38个字符。|列为黑名单的短消息中心的GT号码。






[](None)命令举例 


删除SMSC地址为861380045151的SMSC地址黑名单配置。 


DEL SMSC BLACKLIST:SMSCADDR="861380045151";  








父主题： [SMSC地址黑名单配置](../../zh-CN/tree/N_1254474.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询SMSC地址黑名单配置(SHOW SMSC BLACKLIST) 
## 查询SMSC地址黑名单配置(SHOW SMSC BLACKLIST) 


[](None)命令功能 


该命令用于查询SMSC地址黑名单配置列表信息。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SMSCADDR|SMSC地址黑名单|参数可选性:任选参数；参数类型:字符型；参数范围为:0~38个字符。|列为黑名单的短消息中心的GT号码。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SMSCADDR|SMSC地址黑名单|参数可选性:任选参数；参数类型:字符型。|列为黑名单的短消息中心的GT号码。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|起备注作用，用于区分不同的SMSC黑名单地址。






[](None)命令举例 


查询SMSC地址为861380045151的黑名单配置信息。 


SHOW SMSC BLACKLIST:SMSCADDR="861380045151";  


`
命令 (No.1): SHOW SMSC BLACKLIST

操作维护 SMSC地址黑名单 用户别名 
-------------------------------------
复制 删除  861380045151 11 
-------------------------------------
记录数 1

命令执行成功（耗时 0.016 秒）。
` 








父主题： [SMSC地址黑名单配置](../../zh-CN/tree/N_1254474.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


