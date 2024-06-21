 APN配置 


背景知识 


APN（Access Point Name），即“接入点名称”，是用户通过手机上网时必须配置的一个参数，它决定了用户的手机通过哪种接入方式来访问网络，在骨干网中用来标识要使用的外部PDN网络。APN由以下两部分组成： 



 

网络标识：这部分是必有的，它是由网络运营者分配给ISP（互联网服务提供商，Internet Service Provider）或公司的、与其固定Internet域名一样的一个标识。
 

 

运营商标识：这部分是可选的，其形式为“xxx.yyy.gprs”（如MNC.MCC.gprs）或”xxx.yyy.3gppnetwork.org”（ MNC.MCC. 3gppnetwork.org），用于标识归属网络。
 

 




功能描述 


APN网络标识通常作为用户签约数据存储在HSS/HLR中，用户在发起分组业务时也可向MME/SGSN提供APN。MME/SGSN根据APN通过DNS或本地域名解析得到PGW/GGSN的IP地址。 


该配置支持APN本地域名解析，支持基于用户级的APN扩展、更正和转换，也支持基于APN级的计费策略控制和DT控制。 




相关主题 



 

GPRS APN HOST配置
 

 

EPC APN HOST配置
 

 

GPRS扩展APN配置
 

 

EPC扩展APN配置
 

 

GPRS APN优选GGSN配置
 

 

EPC APN优选子网段配置
 

 

GPRS APN更正配置
 

 

EPC APN更正配置
 

 

EPC APN选择控制配置
 

 

APN PDP IDLE时长配置
 

 

LTE能力终端域名格式配置
 

 

签约APN DT前缀配置
 

 

转换APN配置
 

 

IMS APN配置
 

 

APN选择策略配置
 

 

专用APN配置
 

 








父主题： [业务配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# GPRS APN HOST配置 
# GPRS APN HOST配置 


背景知识 



                APN有2种格式：GPRS APN 和EPC APN，对支持LTE能力的用户终端，SGSN使用LTE能力终端域名格式配置（
                [SET EPC APN NAME CFG]
                ）选择EPC APN格式或GPRS APN格式进行地址解析，如果SGSN选择EPC APN格式进行地址解析，则使用EPC APN HOST配置（
                [ADD EPC APN]
                ），如果SGSN选择GPRS APN格式进行地址解析，则使用GPRS APN HOST配置；对不支持LTE能力的用户终端，SGSN选择GPRS APN格式进行地址解析，使用GPRS APN HOST配置。
            


SGSN从HSS/HLR或UE获取到APN，对支持LTE能力且选择GPRS APN格式的用户终端或不支持LTE能力的用户终端，根据GPRS格式的APN通过DNS或本地域名解析得到GGSN的IP地址。 




功能描述 


GPRS APN HOST配置包括以下内容： 



 

支持GPRS格式的APN域名本地解析，最多可以配置16个该APN对应的GGSN IP地址。
 

 


                        配置APN使用的计费模板标识，支持基于APN级的计费策略控制。基于APN级的计费策略控制使用APN计费模板配置（
                        ADD APNCTPL
                        ）。
                    
 

 

配置GGSN是否支持DT（Direct Tunnel，直传隧道）或根据签约APN信息决策是否支持DT，实现DT后，用户面数据直接在RNC和GGSN之间传输，SGSN只负责PDP上下文的建立与删除，不负责用户面数据报文的转发。
 

 

配置GGSN是否支持终端双栈，支持双栈的终端，网络为其同时分配了IPV4和IPV6地址，该终端既可以访问IPV4的网络资源，同时也可以访问IPV6的网络资源，而无需进行网络切换。
 

 

配置是否过滤S-CDR，基于APN屏蔽S-CDR话单（SGSN (IP-CAN bearer) generated – CDR），开启此功能后，SGSN对此APN不再输出S-CDR。
 

 


配置支持DT功能的流程如下： 







                        RNC局向附加属性中配置支持DT功能，
                        [ADD RNC]
                        。
                    







                        配置GGSN支持DT或配置根据签约APN信息决策是否支持DT，配置命令为：
                        [ADD GPRS APN]
                        。
                    







                        如果配置了根据签约APN信息决策是否支持DT，继续配置支持DT的APN前缀，检查用户签约APN DT前缀信息，配置命令参见
                        [SET APN DT PREFIX]
                        。
                    






注意事项： 



 

SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。
 

 

软件参数“DT话单控制”（ID：786523），控制是否产生DT话单，该软件参数取值为0，则不产生无流量的DT话单（not generate no volume DT CDR）；取值为1，则产生DT话单（generate DT CDR）；取值为2，则不产生DT话单（not generagte DT CDR）。
 

 

软件参数“DT切换频次”（ID：786527），除SGSN首次建立DT外，控制SGSN建立DT的切换频次。该软件参数取值为0，则总是允许；取值为1-254，则第N+1次允许（allow once for every N+1 times）；取值为255，则总是不允许。
 

 

软件参数“CAMEL用户是否允许隧道直传”（ID：786546），控制CAMEL用户是否允许DT功能。该软件参数取值为0，则不允许CAMEL用户隧道直传；取值为1，则允许CAMEL用户隧道直传。
 

 


配置双栈功能的流程如下： 







                        SGSN终端双栈数据中配置支持终端双栈功能，配置命令参见：
                        [SET GNGP DUAL STACK]
                        。
                    







                        RNC局向附加属性中配置支持终端双栈功能，配置命令参见：
                        [ADD RNC]
                        。
                    







                        配置GGSN支持终端双栈。配置命令为：
                        [ADD GPRS APN]
                        。
                    






配置软件参数“计费消息是否携带终端双栈地址”，取值0：IPv4，1：IPv6，2：Ipv4v6。 








相关主题 



 

新增GPRS APN HOST配置(ADD GPRS APN)
 

 

修改GPRS APN HOST配置(SET GPRS APN)
 

 

增加GPRS APN HOST地址(ADD GPRS APN IPADDR)
 

 

删除GPRS APN HOST地址(DEL GPRS APN IPADDR)
 

 

删除GPRS APN HOST配置(DEL GPRS APN)
 

 

查询GPRS APN HOST配置(SHOW GPRS APN)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增GPRS APN HOST配置(ADD GPRS APN) 
## 新增GPRS APN HOST配置(ADD GPRS APN) 


命令功能 


运营商首先需要知道MS将被允许通过GGSN接入到哪些PDN，一旦确定后，就应当规划连接到那些PDN的APN，并在SGSN上配置相应APN数据，以保证SGSN能够根据用户提供的APN信息，解析获取到对应的GGSN的IP地址，从而将MS接入相应的PDN。 


SGSN从HLR或MS获取到APN信息后，可以通过两种方式来获取对应的GGSN的IP地址，包括DNS解析和本地解析，使用本命令来配置SGSN本地解析APN数据。 


通过本命令，除了可以配置APN对应的GGSN IP地址，还可以配置以下内容： 


该APN对应的GGSN是否支持DT（Direct Tunnel，直传隧道）功能。 


该APN下接入的用户对应的计费模板。 


该APN下接入的用户否支持终端双栈。 


SGSN对该APN下接入的用户是否生成S-CDR（Serving GPRS Support Node -Call Detail Record，服务GPRS支持节点-呼叫详细记录）话单。 




注意事项 


该功能只适用于SGSN网元。 


该命令的配置数据受软件参数“SGSN地址解析优先级控制”（ID为65592）的影响，该软件参数包括如下选项： 


取值为“0”：表示SGSN获取GGSN控制面IP地址的优先级为：Host Local->DNS Cache->DNS Server 


取值为“1”：表示SGSN获取GGSN控制面IP地址的优先级为：Host Local->DNS Server 


取值为“2”：表示SGSN获取GGSN控制面IP地址的优先级为：DNS Cache->DNS Server->Host Local 


取值为“3”：表示SGSN获取GGSN控制面IP地址的优先级为：DNS Server->Host Local 


如果要通过本命令配置该APN下接入的用户对应的计费数据，需要先通过[ADD APNCTPL]命令配置该APN对应的计费模板。




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~82个字符。|APN由Network Identifier（NI）和Operator Identifier（OI）组成。NI部分具有格式“Label1.Label2.Label3”，可包含多个的标签；长度<=63；不以“rac”，“lac”，“sgsn”，“rnc”或者"."开头；不以“.gprs”结尾；不使用通配符“*”。OI部分具有格式“mnc<MNC>.mcc<MCC>.gprs” ，<MNC>和<MCC>都是三位0~9数字，不足三位的，靠前补零。NI和OI间以"."分隔。不区分大小写，SGSN完全以小写入库。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|配置GGSN的IP地址，包括IPv4或者IPv6地址，多实例。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，一个APN最多可以解析出64个地址，可配置小于等于64的任意个IP地址。
CTPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。默认值:0。|配置基于APN级的计费策略控制标识，该参数的值，是通过ADD APNCTPL命令设置的APN计费模板配置生成的计费模板标识,且这个APN计费模板配置命令是设置本配置的前提条件。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|SGSN根据使用的APN解析到的GGSN是否支持隧道直传(DT)。DT功能在PS域的RAN和GGSN间使用直传用户面隧道，不应用在Gb接入的情况。使用DT功能还需要：本局license支持Direct tunnel功能。SGSN配置关联的RNC(ADD RNC）支持DT功能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|终端UE支持双栈，为了支持其既可以访问IPV4的互联网网络资源，也可以通过IPV6地址访问IPV6的网络资源，SGSN配置关联的GGSN是否支持终端双栈功能。使用双栈功能还需要：本局license支持终端双栈功能。SGSN配置关联的RNC(ADD RNC）支持终端双栈功能。在SGSN上设置该参数，该参数用于设置目标GGSN是否支持终端双栈功能。“不支持（NO）”：对端GGSN不支持终端双栈功能。 “支持（YES）”：对端GGSN支持终端双栈功能。 “默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK
SCDRFLT|过滤S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|基于APN屏蔽S-CDR话单，过滤S-CDR选择是，SGSN通过此APN解析GGSN地址时，不再输出会话计费数据话单(S-CDR)；过滤S-CDR选择否，SGSN通过此APN解析GGSN地址时，输出会话计费数据话单(S-CDR)






命令举例 


新增GPRS APN HOST配置，APN名称为zte.com.mnc222.mcc333.gprs，IP地址为1.0.0.0和2.0.0.0，计费模板标识为1，不支持DT功能，不支持终端双栈功能，不过滤S-CDR。 


ADD GPRS APN:APN="zte.com.mnc222.mcc333.gprs",IPADDR="1.0.0.0"&"2.0.0.0",CTPLID=1; 








父主题： [GPRS APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改GPRS APN HOST配置(SET GPRS APN) 
## 修改GPRS APN HOST配置(SET GPRS APN) 


命令功能 


通过本命令，除了可以修改某个APN对应的GGSN IP地址，还可以修改以下内容： 


该APN对应的GGSN是否支持DT（Direct Tunnel，直传隧道）功能。 


该APN下接入的用户对应的计费模板。 


该APN下接入的用户否支持终端双栈。 


SGSN对该APN下接入的用户是否生成S-CDR（Serving GPRS Support Node -Call Detail Record，服务GPRS支持节点-呼叫详细记录）话单。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~82个字符。|APN由Network Identifier（NI）和Operator Identifier（OI）组成。NI部分具有格式“Label1.Label2.Label3”，可包含多个的标签；长度<=63；不以“rac”，“lac”，“sgsn”，“rnc”或者"."开头；不以“.gprs”结尾；不使用通配符“*”。OI部分具有格式“mnc<MNC>.mcc<MCC>.gprs” ，<MNC>和<MCC>都是三位0~9数字，不足三位的，靠前补零。NI和OI间以"."分隔。不区分大小写，SGSN完全以小写入库。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|配置GGSN的IP地址，包括IPv4或者IPv6地址，多实例。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，一个APN最多可以解析出64个地址，可配置小于等于64的任意个IP地址。
CTPLID|计费模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~31。|配置基于APN级的计费策略控制标识，该参数的值，是通过ADD APNCTPL命令设置的APN计费模板配置生成的计费模板标识,且这个APN计费模板配置命令是设置本配置的前提条件。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGSN根据使用的APN解析到的GGSN是否支持隧道直传(DT)。DT功能在PS域的RAN和GGSN间使用直传用户面隧道，不应用在Gb接入的情况。使用DT功能还需要：本局license支持Direct tunnel功能。SGSN配置关联的RNC(ADD RNC）支持DT功能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|终端UE支持双栈，为了支持其既可以访问IPV4的互联网网络资源，也可以通过IPV6地址访问IPV6的网络资源，SGSN配置关联的GGSN是否支持终端双栈功能。使用双栈功能还需要：本局license支持终端双栈功能。SGSN配置关联的RNC(ADD RNC）支持终端双栈功能。在SGSN上设置该参数，该参数用于设置目标GGSN是否支持终端双栈功能。“不支持（NO）”：对端GGSN不支持终端双栈功能。 “支持（YES）”：对端GGSN支持终端双栈功能。 “默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK
SCDRFLT|过滤S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|基于APN屏蔽S-CDR话单，过滤S-CDR选择是，SGSN通过此APN解析GGSN地址时，不再输出会话计费数据话单(S-CDR)；过滤S-CDR选择否，SGSN通过此APN解析GGSN地址时，输出会话计费数据话单(S-CDR)






命令举例 


修改APN名称为zte.com.mnc222.mcc333.gprs的GPRS APN HOST配置，IP地址为3.3.3.3和4.4.4.4，支持DT功能，支持终端双栈功能，过滤S-CDR。 


SET GPRS APN:APN="zte.com.mnc222.mcc333.gprs",IPADDR="3.3.3.3"&"4.4.4.4",DTSPRT="YES",DUALSTACKFLAG="YES",SCDRFLT="YES"; 








父主题： [GPRS APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 增加GPRS APN HOST地址(ADD GPRS APN IPADDR) 
## 增加GPRS APN HOST地址(ADD GPRS APN IPADDR) 


命令功能 


在已经通过[ADD GPRS APN]配置了某个APN对应的的GGSN的基础上，如果此APN还需要解析到其它GGSN时，需要通过本命令增加此APN对应的GGSN的IP地址。




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~82个字符。|APN由Network Identifier（NI）和Operator Identifier（OI）组成。NI部分具有格式“Label1.Label2.Label3”，可包含多个的标签；长度<=63；不以“rac”，“lac”，“sgsn”，“rnc”或者"."开头；不以“.gprs”结尾；不使用通配符“*”。OI部分具有格式“mnc<MNC>.mcc<MCC>.gprs” ，<MNC>和<MCC>都是三位0~9数字，不足三位的，靠前补零。NI和OI间以"."分隔。不区分大小写，SGSN完全以小写入库。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|配置GGSN的IP地址，包括IPv4或者IPv6地址，多实例。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，一个APN最多可以解析出64个地址，可配置小于等于64的任意个IP地址。






命令举例 


名称为zte.com.mnc222.mcc333.gprs的APN增加GPRS APN HOST地址，地址为5.5.5.5和6.6.6.6。 


ADD GPRS APN IPADDR:APN="zte.com.mnc222.mcc333.gprs",IPADDR="5.5.5.5"&"6.6.6.6"; 








父主题： [GPRS APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除GPRS APN HOST地址(DEL GPRS APN IPADDR) 
## 删除GPRS APN HOST地址(DEL GPRS APN IPADDR) 


命令功能 

该命令用于删除某个APN对应的GGSN IP地址。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~82个字符。|APN由Network Identifier（NI）和Operator Identifier（OI）组成。NI部分具有格式“Label1.Label2.Label3”，可包含多个的标签；长度<=63；不以“rac”，“lac”，“sgsn”，“rnc”或者"."开头；不以“.gprs”结尾；不使用通配符“*”。OI部分具有格式“mnc<MNC>.mcc<MCC>.gprs” ，<MNC>和<MCC>都是三位0~9数字，不足三位的，靠前补零。NI和OI间以"."分隔。不区分大小写，SGSN完全以小写入库。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|配置GGSN的IP地址，包括IPv4或者IPv6地址，多实例。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，一个APN最多可以解析出64个地址，可配置小于等于64的任意个IP地址。






命令举例 


删除GPRS APN HOST地址，APN名称为zte.com.mnc222.mcc333.gprs，地址为5.5.5.5。 


DEL GPRS APN IPADDR:APN="zte.com.mnc222.mcc333.gprs",IPADDR="5.5.5.5"; 








父主题： [GPRS APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除GPRS APN HOST配置(DEL GPRS APN) 
## 删除GPRS APN HOST配置(DEL GPRS APN) 


命令功能 

该命令用于删除某个APN对应的本地解析配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~82个字符。|APN由Network Identifier（NI）和Operator Identifier（OI）组成。NI部分具有格式“Label1.Label2.Label3”，可包含多个的标签；长度<=63；不以“rac”，“lac”，“sgsn”，“rnc”或者"."开头；不以“.gprs”结尾；不使用通配符“*”。OI部分具有格式“mnc<MNC>.mcc<MCC>.gprs” ，<MNC>和<MCC>都是三位0~9数字，不足三位的，靠前补零。NI和OI间以"."分隔。不区分大小写，SGSN完全以小写入库。






命令举例 


删除APN名称为zte.com.mnc222.mcc333.gprs的GPRS APN HOST配置。 


DEL GPRS APN:APN="zte.com.mnc222.mcc333.gprs"; 








父主题： [GPRS APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询GPRS APN HOST配置(SHOW GPRS APN) 
## 查询GPRS APN HOST配置(SHOW GPRS APN) 


命令功能 


该命令用于查询某个APN对应的本地解析配置数据。 


不输入APN名称，表示查询SGSN上所有APN对应的本地解析配置数据。 


输入指定的APN名称，表示查询该APN对应的本地解析配置数据。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~82个字符。|APN由Network Identifier（NI）和Operator Identifier（OI）组成。NI部分具有格式“Label1.Label2.Label3”，可包含多个的标签；长度<=63；不以“rac”，“lac”，“sgsn”，“rnc”或者"."开头；不以“.gprs”结尾；不使用通配符“*”。OI部分具有格式“mnc<MNC>.mcc<MCC>.gprs” ，<MNC>和<MCC>都是三位0~9数字，不足三位的，靠前补零。NI和OI间以"."分隔。不区分大小写，SGSN完全以小写入库。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNID|APN标识|参数可选性:任选参数；参数类型:整数。|系统自动生成的标识，不需要关注。
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|APN由Network Identifier（NI）和Operator Identifier（OI）组成。NI部分具有格式“Label1.Label2.Label3”，可包含多个的标签；长度<=63；不以“rac”，“lac”，“sgsn”，“rnc”或者"."开头；不以“.gprs”结尾；不使用通配符“*”。OI部分具有格式“mnc<MNC>.mcc<MCC>.gprs” ，<MNC>和<MCC>都是三位0~9数字，不足三位的，靠前补零。NI和OI间以"."分隔。不区分大小写，SGSN完全以小写入库。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|配置GGSN的控制面IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址，可配置小于等于64的任意个IP地址。
CTPLID|计费模板标识|参数可选性:任选参数；参数类型:整数。|配置基于APN级的计费策略控制标识，该参数的值，是通过ADD APNCTPL命令设置的APN计费模板配置生成的计费模板标识,且这个APN计费模板配置命令是设置本配置的前提条件。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGSN根据使用的APN解析到的GGSN是否支持隧道直传(DT)。DT功能在PS域的RAN和GGSN间使用直传用户面隧道，不应用在Gb接入的情况。使用DT功能还需要：本局license支持Direct tunnel功能。SGSN配置关联的RNC(ADD RNC）支持DT功能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|终端UE支持双栈，为了支持其既可以访问IPV4的互联网网络资源，也可以通过IPV6地址访问IPV6的网络资源，SGSN配置关联的GGSN是否支持终端双栈功能。使用双栈功能还需要：本局license支持终端双栈功能。SGSN配置关联的RNC(ADD RNC）支持终端双栈功能。在SGSN上设置该参数，该参数用于设置目标GGSN是否支持终端双栈功能。“不支持（NO）”：对端GGSN不支持终端双栈功能。 “支持（YES）”：对端GGSN支持终端双栈功能。 “默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK
SCDRFLT|过滤S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|基于APN屏蔽S-CDR话单，过滤S-CDR选择是，SGSN通过此APN解析GGSN地址时，不再输出会话计费数据话单(S-CDR)；过滤S-CDR选择否，SGSN通过此APN解析GGSN地址时，输出会话计费数据话单(S-CDR)






命令举例 


查询 GPRS APN HOST配置。 


SHOW GPRS APN; 


`

2016-09-06 11:39:11 命令 (No.1): SHOW GPRS APN

操作维护         APN标识   APN名称                      IP地址    计费模板标识   支持DT功能                      支持终端双栈功能   过滤S-CDR
---------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   2         zte.com.mnc222.mcc333.gprs   1.0.0.0   0              不支持                          不支持             否
复制 修改 删除   2         zte.com.mnc222.mcc333.gprs   2.0.0.0   0              不支持                          不支持             否
---------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.053 秒）。
` 








父主题： [GPRS APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# EPC APN HOST配置 
# EPC APN HOST配置 


背景知识 



                APN有2种格式：GPRS APN 和EPC APN，对支持LTE能力的用户终端，SGSN使用LTE能力终端域名格式配置 （
                [SET EPC APN NAME CFG]
                ）选择EPC APN格式或GPRS APN格式进行地址解析，如果SGSN选择EPC APN格式进行地址解析，则使用EPC APN HOST配置，如果SGSN选择GPRS APN格式进行地址解析，则使用GPRS APN HOST配置（
                [ADD GPRS APN]
                ），MME选择EPC APN格式进行地址解析，使用EPC APN HOST配置；对不支持LTE能力的用户终端，SGSN选择GPRS APN格式进行地址解析，使用GPRS APN HOST配置（
                [ADD GPRS APN]
                ），MME只支持具有LTE能力的用户终端，因此不使用GPRS APN HOST配置。
            


MME从HSS或UE获取到APN，对支持LTE能力的用户终端，根据EPC格式的APN通过DNS或本地域名解析得到PGW的IP地址。 


SGSN从HSS/HLR或UE获取到APN，对支持LTE能力且选择EPC APN格式的用户终端，根据EPC格式的APN通过DNS或本地域名解析得到GGSN的IP地址。 




功能描述 


EPC APN HOST配置包括以下内容： 



 

支持EPC格式的APN域名本地解析，最多可以配置10个该APN对应的PGW IP地址或GGSN IP地址。
 

 

配置GGSN是否支持DT（Direct Tunnel，直传隧道）或根据签约APN信息决策是否支持DT，实现DT后，用户面数据直接在RNC和GGSN之间传输，SGSN只负责PDP上下文的建立与删除，不负责用户面数据报文的转发。
 

 

配置GGSN是否支持终端双栈，支持双栈的终端，网络为其同时分配了IPV4和IPV6地址，该终端既可以访问IPV4的网络资源，同时也可以访问IPV6的网络资源，而无需进行网络切换。
 

 


配置支持DT功能的流程如下： 







                        RNC局向附加属性中配置支持DT功能，
                        [ADD RNC]
                        。
                    







                        配置GGSN支持DT或配置根据签约APN信息决策是否支持DT，配置命令为
                        [ADD EPC APN]
                        。
                    







                        如果配置了根据签约APN信息决策是否支持DT，继续配置支持DT的APN前缀，检查用户签约APN DT前缀信息，配置命令参见
                        [SET APN DT PREFIX]
                        。
                    






注意事项： 


SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。 


配置双栈功能的流程如下： 







                        SGSN终端双栈数据中配置支持终端双栈功能，配置命令参见：
                        [SET GNGP DUAL STACK]
                        。
                    







                        RNC局向附加属性中配置支持终端双栈功能，配置命令参见：
                        [ADD RNC]
                        。
                    







                        配置GGSN支持终端双栈。配置命令为
                        [ADD EPC APN]
                        。
                    






配置软件参数“计费消息是否携带终端双栈地址”，取值0：IPv4，1：IPv6，2：Ipv4v6。 






说明： 


EPC网络中eNodeB、MME和PGW，是一定支持DT和终端双栈，无需配置。 




相关主题 



 

新增EPC APN HOST配置(ADD EPC APN)
 

 

修改EPC APN HOST配置(SET EPC APN)
 

 

增加EPC APN HOST地址(ADD EPC APN IPADDR)
 

 

删除EPC APN HOST地址(DEL EPC APN IPADDR)
 

 

删除EPC APN HOST配置(DEL EPC APN)
 

 

查询EPC APN HOST配置(SHOW EPC APN)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增EPC APN HOST配置(ADD EPC APN) 
## 新增EPC APN HOST配置(ADD EPC APN) 


命令功能 


该命令用于新增EPC形式的APN本地域名解析信息，将EPC形式的APN解析成网络上可以识别的IP地址。 


当运营商需要本地解析IP地址时，使用该命令，APN本地域名解析配置成功后，可以根据EPC形式的APN在本地解析出IP地址。 




注意事项 



 
该命令中APN名称和主机名唯一确定一条记录，同一个APN名称可对应配置不同的主机名。
 

 
当需要解析PGW的IP地址时，参数中“支持服务类别”选择x-3gpp-pgw；当需要解析GGSN的IP地址时，参数中“支持服务类别”选择x-3gpp-ggsn。
 

 
运营商可以选择优先在本地进行地址解析，或者优先通过DNS服务器进行地址解析。当软件参数SET SOFTWARE PARAMETER 中“软件参数ID”65593的“软件参数值”为0或1时，优先进行本地解析IP地址，本地解析成功后，MME将不再向DNS服务器发送解析地址请求。当软件参数SET SOFTWARE PARAMETER 中“软件参数ID”65593的“软件参数值”为2或3时，MME优先向DNS服务器请求地址解析，DNS服务器解析成功后，将不再进行本地地址解析，如果DNS服务器故障或者没有配置该域名对应的解析地址，则会继续在本地解析地址。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过99个字符。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
HOST|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|目标局的主机名称，长度为1-100个字符，不区分大小写。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|PGW或GGSN的IP地址，可设置为IPv4或者IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址，可配置小于等于64的任意个IP地址。以下各IP地址同此说明，不再详述。
SERVICE|支持服务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下网元类型。x-3gpp-pgw：目标局类型为PGWx-3gpp-ggsn：目标局类型为GGSN
PROTOCOL|支持协议类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp：支持GTP协议（协议号为TS29274）的S5接口x-s5-pmip：支持PMIP协议（协议号为TS29274）的S5接口x-s8-gtp：支持GTP协议（协议号为TS29274）的S8接口x-s8-pmip：支持PMIP协议（协议号为TS29274）的S8接口x-gn(x-gn) ：支持GTP协议（协议号为TS29060）的Gn接口x-gp(x-gp) ：支持GTP协议（协议号为TS29060）的Gp接口x-s5-gtp+nc-nr：支持GTP协议（协议号为TS29274）网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议（协议号为TS29274）网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议（协议号为TS29274）网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议（协议号为TS29274）网络能力nr的S8接口。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|在SGSN上设置该参数，该参数用于设置目标GGSN是否支持DT（直传隧道）功能。“不支持（NO）”：对端GGSN不支持DT功能。 “支持（YES）”：对端GGSN支持DT功能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:DEFAULT。|在SGSN上设置该参数，该参数用于设置目标GGSN是否支持终端双栈功能。“不支持（NO）”：对端GGSN不支持终端双栈功能。 “支持（YES）”：对端GGSN支持终端双栈功能。 “默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|表示各个PGW网元的优先级，数值越小，优先级越高。在需要根据优先级和权重选择PGW时，优先选择优先级高的可用的PGW。
NAPTRWEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:200。|权重表示各个PGW网元的能力，数值越大，权重越高，PGW网元的能力越强。在需要根据优先级和权重选择PGW时，如果优先级相同，则权重值越高的可用的PGW，被选择使用的概率越大。PGW网元的能力，通常根据PGW的接入能力（支持的承载数）来确定。如果现场无特殊需求时，PGW支持的PDP承载数越大，PGW能力越强。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NORMAL。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网SGW/MME/SGSN的选择。定义参见3GPP 29.272第7.3.202节。






命令举例 


新增EPC APN HOST配置，APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，主机名为fg，IP地址为3.0.0.0和5.0.0.0，支持的服务类别有PGW和GGSN，支持的协议类型为"x-s5-gtp"，其余采用默认配置。 


ADD EPC APN:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",HOST="fg.epc.mnc222.mcc333.3gppnetwork.org",IPADDR="3.0.0.0"&"5.0.0.0",SERVICE="x-3gpp-pgw"&"x-3gpp-ggsn",PROTOCOL="x-s5-gtp"; 








父主题： [EPC APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改EPC APN HOST配置(SET EPC APN) 
## 修改EPC APN HOST配置(SET EPC APN) 


命令功能 


该命令用于修改已经配置的EPC形式的APN本地域名解析的信息，例如可以修改IP地址、支持服务类别、支持协议类型、支持DT功能、支持终端双栈功能、优先级、或者权重等信息。 


当PGW或GGSN网元的地址发生改变，或者GGSN网元DT功能发生改变时，使用该命令。当该命令配置成功后，可以根据EPC形式的APN在本地解析出IP地址。 




注意事项 


该命令中APN名称和主机名必须已事先通过[ADD EPC APN]配置。如果没有配置APN名称和主机名，该命令会执行失败。


可通过[SHOW EPC APN] 查询已经配置的EPC APN本地域名解析信息。




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过99个字符。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
HOST|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|目标局的主机名称，长度为1-100个字符，不区分大小写。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|PGW或GGSN的IP地址，可设置为IPv4或者IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址，可配置小于等于64的任意个IP地址。以下各IP地址同此说明，不再详述。
SERVICE|支持服务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下网元类型。x-3gpp-pgw：目标局类型为PGWx-3gpp-ggsn：目标局类型为GGSN
PROTOCOL|支持协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp：支持GTP协议（协议号为TS29274）的S5接口x-s5-pmip：支持PMIP协议（协议号为TS29274）的S5接口x-s8-gtp：支持GTP协议（协议号为TS29274）的S8接口x-s8-pmip：支持PMIP协议（协议号为TS29274）的S8接口x-gn(x-gn) ：支持GTP协议（协议号为TS29060）的Gn接口x-gp(x-gp) ：支持GTP协议（协议号为TS29060）的Gp接口x-s5-gtp+nc-nr：支持GTP协议（协议号为TS29274）网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议（协议号为TS29274）网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议（协议号为TS29274）网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议（协议号为TS29274）网络能力nr的S8接口。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在SGSN上设置该参数，该参数用于设置目标GGSN是否支持DT（直传隧道）功能。“不支持（NO）”：对端GGSN不支持DT功能。 “支持（YES）”：对端GGSN支持DT功能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在SGSN上设置该参数，该参数用于设置目标GGSN是否支持终端双栈功能。“不支持（NO）”：对端GGSN不支持终端双栈功能。 “支持（YES）”：对端GGSN支持终端双栈功能。 “默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|表示各个PGW网元的优先级，数值越小，优先级越高。在需要根据优先级和权重选择PGW时，优先选择优先级高的可用的PGW。
NAPTRWEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|权重表示各个PGW网元的能力，数值越大，权重越高，PGW网元的能力越强。在需要根据优先级和权重选择PGW时，如果优先级相同，则权重值越高的可用的PGW，被选择使用的概率越大。PGW网元的能力，通常根据PGW的接入能力（支持的承载数）来确定。如果现场无特殊需求时，PGW支持的PDP承载数越大，PGW能力越强。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网SGW/MME/SGSN的选择。定义参见3GPP 29.272第7.3.202节。






命令举例 


修改APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，名为fg.epc.mnc222.mcc333.3gppnetwork.org的EPC APN HOST配置，IP地址为3.0.0.0，优先级为1。 


SET EPC APN:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",HOST="fg.epc.mnc222.mcc333.3gppnetwork.org",IPADDR="3.0.0.0",NAPTRORDER=1; 








父主题： [EPC APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 增加EPC APN HOST地址(ADD EPC APN IPADDR) 
## 增加EPC APN HOST地址(ADD EPC APN IPADDR) 


命令功能 

该命令用于新增EPC形式的APN本地域名解析的地址信息。当需要在APN本地域名解析信息中增加解析的地址时，使用该命令。


注意事项 

该命令中APN名称和主机名必须已事先通过[ADD EPC APN]配置。如果没有配置APN名称和主机名，该命令会执行失败。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过99个字符。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
HOST|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|目标局的主机名称，长度为1-100个字符，不区分大小写。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|PGW或GGSN的IP地址，可设置为IPv4或者IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址，可配置小于等于64的任意个IP地址。以下各IP地址同此说明，不再详述。






命令举例 


为APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，名为fg的主机增加EPC APN HOST地址，地址为1.1.1.1和2.2.2.2。 


ADD EPC APN IPADDR:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",HOST="fg",IPADDR="1.1.1.1"&"2.2.2.2"; 








父主题： [EPC APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除EPC APN HOST地址(DEL EPC APN IPADDR) 
## 删除EPC APN HOST地址(DEL EPC APN IPADDR) 


命令功能 

该命令用于删除EPC形式的APN本地域名解析的地址信息。


注意事项 

该命令中APN名称和主机名必须已事先通过 [ADD EPC APN] 配置。如果没有配置APN名称和主机名，该命令会执行失败。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过99个字符。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
HOST|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|目标局的主机名称，长度为1-100个字符，不区分大小写。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|PGW或GGSN的IP地址，可设置为IPv4或者IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址，可配置小于等于64的任意个IP地址。以上各IP地址同此说明，不再详述。






命令举例 


为APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，名为fg的主机删除2.2.2.2的EPC APN HOST地址。 


DEL EPC APN IPADDR:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",HOST="fg",IPADDR="2.2.2.2"; 








父主题： [EPC APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除EPC APN HOST配置(DEL EPC APN) 
## 删除EPC APN HOST配置(DEL EPC APN) 


命令功能 

该命令用于删除EPC形式的APN本地域名解析配置。当运营商不需要本地解析APN名称时，使用该命令。


注意事项 

该命令可删除指定的APN名称的地址解析信息，也可以只删除指定的APN名称和指定的主机名对应的地址解析信息。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过99个字符。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
HOST|主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|目标局的主机名称，长度为1-100个字符，不区分大小写。






命令举例 


删除APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org的EPC APN HOST配置。 


DEL EPC APN:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org"; 








父主题： [EPC APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询EPC APN HOST配置(SHOW EPC APN) 
## 查询EPC APN HOST配置(SHOW EPC APN) 


命令功能 

该命令用于查询EPC形式的APN本地域名解析配置信息。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过99个字符。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
HOST|主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|目标局的主机名称，长度为1-100个字符，不区分大小写。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNID|APN标识|参数可选性:任选参数；参数类型:整数。|网管自动生成的记录号。
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过99个字符。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
HOST|主机名|参数可选性:任选参数；参数类型:字符型。|目标局的主机名称，长度为1-100个字符，不区分大小写。
IPADDR|IP地址|参数可选性:任选参数；参数类型:字符型。|IP地址
SERVICE|支持服务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下网元类型。x-3gpp-pgw：目标局类型为PGWx-3gpp-ggsn：目标局类型为GGSN
PROTOCOL|支持协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp：支持GTP协议（协议号为TS29274）的S5接口x-s5-pmip：支持PMIP协议（协议号为TS29274）的S5接口x-s8-gtp：支持GTP协议（协议号为TS29274）的S8接口x-s8-pmip：支持PMIP协议（协议号为TS29274）的S8接口x-gn(x-gn) ：支持GTP协议（协议号为TS29060）的Gn接口x-gp(x-gp) ：支持GTP协议（协议号为TS29060）的Gp接口x-s5-gtp+nc-nr：支持GTP协议（协议号为TS29274）网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议（协议号为TS29274）网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议（协议号为TS29274）网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议（协议号为TS29274）网络能力nr的S8接口。
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在SGSN上设置该参数，该参数用于设置目标GGSN是否支持DT（直传隧道）功能。“不支持（NO）”：对端GGSN不支持DT功能。 “支持（YES）”：对端GGSN支持DT功能。
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在SGSN上设置该参数，该参数用于设置目标GGSN是否支持终端双栈功能。“不支持（NO）”：对端GGSN不支持终端双栈功能。 “支持（YES）”：对端GGSN支持终端双栈功能。 “默认策略（DEFAULT）”：同GGSN支持终端双栈的默认策略。配置命令为：SET GNGP DUAL STACK
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数。|表示各个PGW网元的优先级，数值越小，优先级越高。在需要根据优先级和权重选择PGW时，优先选择优先级高的可用的PGW。
NAPTRWEIGHT|权重|参数可选性:任选参数；参数类型:整数。|权重表示各个PGW网元的能力，数值越大，权重越高，PGW网元的能力越强。在需要根据优先级和权重选择PGW时，如果优先级相同，则权重值越高的可用的PGW，被选择使用的概率越大。PGW网元的能力，通常根据PGW的接入能力（支持的承载数）来确定。如果现场无特殊需求时，PGW支持的PDP承载数越大，PGW能力越强。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:整数。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网SGW/MME/SGSN的选择。定义参见3GPP 29.272第7.3.202节。






命令举例 


查询EPC APN HOST配置。 


SHOW EPC APN; 


`

2017-02-20 13:45:27 命令 (No.1): SHOW EPC APN

操作维护         APN标识   APN名称                                         主机名                                 IP地址    支持服务类别               支持协议类型   支持DT功能                      支持终端双栈功能   优先级   权重    用户使用类型
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1         zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org   fg.epc.mnc222.mcc333.3gppnetwork.org   3.0.0.0   x-3gpp-pgw & x-3gpp-ggsn   x-s5-gtp       不支持                          不支持             0        200     普通用户
复制 修改 删除   1         zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org   fg.epc.mnc222.mcc333.3gppnetwork.org   5.0.0.0   x-3gpp-pgw & x-3gpp-ggsn   x-s5-gtp       不支持                          不支持             0        200     普通用户
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.097 秒）。
` 








父主题： [EPC APN HOST配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# GPRS扩展APN配置 
# GPRS扩展APN配置 


背景知识 


运营商在部署GGSN时，有可能需要考虑用户的号码和签约计费特性等，在APN NI中扩展这些用户信息，可以为运营商提供更准确的APN选择GGSN的策略。 




功能描述 


SGSN在进行GGSN选择时，对APN根据配置的扩展方法对APN NI进行扩展，然后用扩展后的APN NI来构造APN获取服务的GGSN。 


该配置支持多种APN扩展方式（包括：基于IMSI/MSISDN/IMEI号段、签约计费特性、以及两者的组合方式）、支持漫游用户拜访地接入时是否扩展、LTE能力终端是否扩展、本地HOST解析失败后是否使用非扩展APN解析和DT策略控制。 


注意事项： 



 

软件参数“PDP上下文中的APN是否保留扩展部分”（ID：786482），控制用户的APN扩展后，SGSN的PDP上下文中APN是否保留扩展部分，软件参数取值为1，则保留，相关的接口消息以及S-CDR（SGSN (IP-CAN bearer) generated – CDR）中的APN也包含扩展部分，性能统计等都使用扩展后的APN统计；取值为0，则不保留，相关接口消息、S-CDR和性能统计中都使用非扩展的APN。
 

 

软件参数“基于计费特性的APN扩展控制”（ID：786485），控制APN扩展需要根据计费特性扩展且签约混合计费特性时，对计费特性部分的扩展方式。软件参数取值为0，则按照优先级选择一种计费特性的名称扩展，优先级：Hot billing > Flat rate > Prepaid > Normal；取值为1，则使用计费特性字段有效位的二进制数扩展；取值为2，则使用计费特性字段十六进制数扩展。
 

 

软件参数“APN扩展号码类型”（ID：786565），控制APN扩展使用的号码类型，软件参数取值为0，则使用IMSI扩展APN；取值为1，则使用MSISDN扩展APN。
 

 




相关主题 



 

新增GPRS扩展APN配置(ADD EXAPN)
 

 

修改GPRS扩展APN配置(SET EXAPN)
 

 

删除GPRS扩展APN配置(DEL EXAPN)
 

 

查询GPRS扩展APN配置(SHOW EXAPN)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增GPRS扩展APN配置(ADD EXAPN) 
## 新增GPRS扩展APN配置(ADD EXAPN) 


命令功能 


根据3GPP TS 23.003协议的定义，APN名称由NI（Network Identifier，网络标识）和OI（Operator Identifier，运营商标识）两部分组成： 



 
OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。
 

 
NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。
 

 


它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。 


为了给SGSN提供更准确的APN，以供其选择更加合适的GGSN，可以对APN NI进行扩展，使其包括了更详细的信息，本命令用于设置APN NI的扩展方式，目的在于SGSN对扩展后的APN进行解析，得出对应的GGSN IP地址。 


本命令提供了多种扩展方式，包括：可根据MS的IMSI、IMEI、MSISDN或MS签约的计费特性对APN NI进行扩展。 


通过本命令还可以配置其他数据，包括： 



 
可根据MS的类型决定是否对APN NI进行扩展。
 

 
如果SGSN对扩展后的APN进行解析失败后，是否还需要对原APN进行解析。
 

 
在漫游用户通过拜访地的SGSN网元接入的情况下，SGSN是否支持对漫游用户的APN NI进行扩展。
 

 
对支持LTE能力的终端的APN NI中是否增加”.pgw”字段。判断SGSN是否支持DT功能。
 

 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|此参数为APN的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：长度小于63个字符。不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头。不能以“.gprs”结尾。不能使用通配符“*”。除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cn
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|此参数设置为MS的IMSI或MSISDN号段。IMSI（International Mobile Subscriber Identity，国际移动用户标识），由MCC+MNC+MSIN组成。MSISDN（Mobile Station International Subscriber Directory Number，移动台国际用户目录号），由CC+NDC+SN组成。SGSN根据软件参数“扩展APN的号码类型”（ID为786565）来获取APN NI的扩展方式的匹配条件：软件参数取值为“0”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+“IMSI号段”作为条件匹配APN NI的扩展方式。软件参数取值为“1”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+”MSISDN号段“作为条件查询APN NI的扩展方式。
EXUETYPE|扩展终端类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:For All。|该参数表示根据终端类型决定是否对APN NI扩展。设置为“全部扩展”：表示对所有的终端都可以进行APN NI扩展。设置为“仅支持LTE能力终端扩展”：只对支持LTE能力的MS进行APN NI扩展。设置为“仅不支持LTE能力终端扩展”：只对不支持LTE能力的接入的MS进行APN NI扩展。
EXMODE|扩展方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示对APN NI进行扩展的方式，包括六种方式：MSISDN扩展：表示使用MS的MSISDN号段对APN NI进行扩展（即在原APN NI后增加用户的MSISDN号段，最大扩展长度为15位）。IMSI扩展：表示使用MS的IMSI号码对APN NI进行扩展（即在原APN NI后增加用户的IMSI号段，最大扩展长度为15位）。签约计费特性扩展：表示根据MS签约的计费特性对APN NI进行扩展。MS签约热付费，在原APN NI后扩展“.hotbilling“；MS签约平率计费，在原APN NI后扩展”.flatrate”；MS签约预付费，在原APN NI后扩展”.preprid”；MS签约普通计费，在原APN NI后扩展”.normal“签约计费特性+IMSI：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMSI号段对APN NI进行扩展。签约计费特性+MSISDN：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的MSISDN号段对APN NI进行扩展。IMEI扩展：表示使用MS的IMEI号段对APN NI进行扩展（即在原APN NI后增加用户的IMEI号段，最大扩展长度为15位）。注意事项：当“扩展方式“设置为“签约计费特性扩展”时，不需要设置“APN扩展位”，设置为其他扩展方式时，都必须设置“APN扩展位”。
EXBITS|APN扩展位|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：EXBIT_F、EXBIT_T。用于指定APN扩展起始位和APN扩展终止位。
EXBIT_F|APN扩展起始位|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|当APN NI的扩展方式为对IMSI、MSISDN、IMEI号码扩展时，号码的起始扩展位。
EXBIT_T|APN扩展终止位|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|当APN NI的扩展方式为对IMSI、MSISDN、IMEI号码扩展时，号码的结束扩展位。例如：用户的MSISDN为13912345678，APN扩展起始位为4，APN扩展终止位为8，则将12345补充到原APN NI后。
APNCTRL|HOST解析失败后是否使用非扩展APN解析|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|当设置为“否”时：表示SGSN对扩展后的APN进行解析失败后，不再对原APN进行解析。当设置为“是”时：表示SGSN对扩展后的APN进行解析失败后，还会再次对扩展之前的原APN进行解析。
ROAMEXCTRL|漫游用户拜访地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|当设置为“否”时：表示在漫游用户通过拜访地的SGSN网元接入的情况下，SGSN将不对漫游用户的APN NI进行扩展。当设置为“是”时：表示在漫游用户通过拜访地的SGSN网元接入的情况下，SGSN支持对漫游用户的APN NI进行扩展。
HOMEEXCTRL|漫游用户归属地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|当设置为“否”时：表示漫游用户通过归属地的APN OI+NI选择GGSN网元接入的情况下，SGSN将不对漫游用户的APN NI进行扩展。当设置为“是”时：表示在漫游用户通过归属地的APN OI+NI选择GGSN网元接入的情况下，SGSN支持对漫游用户的APN NI进行扩展。
DTCTRL|DT策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:GGSNIP。|此参数做为判断SGSN是否支持DT功能的条件之一：当设置为“否”时：SGSN将根据MS的签约的APN信息决定是否支持DT功能。当设置为“是”时：SGSN将对扩展后的APN进行解析，根据得到GGSN的IP地址判断是否支持DT，如果解析出的GGSN的IP地址，可以通过SHOW DT IP命令的查询结果获得，表示SGSN支持DT功能。
EPCEXFLG|LTE能力终端是否扩展特殊字段|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|当设置为“是”时，表示对支持LTE能力的终端的APN NI中增加“.pgw”字段。当设置为“否”时，表示对支持LTE能力的终端的APN NI中不增加“.pgw”字段。
IFEXTBASEDCC|根据CC判断是否需进行APN扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置是否需根据CC判断进行APN扩展。否：APN是否需扩展不需基于用户签约CC值。是：APN是否扩展需基于用户签约CC值，对于特定CC值，不对该APN进行扩展。






命令举例 


新增GPRS扩展APN配置，APN名称为bbs，IMSI/MSISDN号段为434546，扩展终端类型为全部扩展，扩展方式为MSISDN扩展，APN扩展起始位为2，终止位为4。 


ADD EXAPN:APN="bbs",IMSI="434546",EXMODE="MSISDN",EXBITS=2-4; 








父主题： [GPRS扩展APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改GPRS扩展APN配置(SET EXAPN) 
## 修改GPRS扩展APN配置(SET EXAPN) 


命令功能 

该命令用于修改APN NI的扩展数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|此参数为APN的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：长度小于63个字符。不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头。不能以“.gprs”结尾。不能使用通配符“*”。除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cn
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|此参数设置为MS的IMSI或MSISDN号段。IMSI（International Mobile Subscriber Identity，国际移动用户标识），由MCC+MNC+MSIN组成。MSISDN（Mobile Station International Subscriber Directory Number，移动台国际用户目录号），由CC+NDC+SN组成。SGSN根据软件参数“扩展APN的号码类型”（ID为786565）来获取APN NI的扩展方式的匹配条件：软件参数取值为“0”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+“IMSI号段”作为条件匹配APN NI的扩展方式。软件参数取值为“1”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+”MSISDN号段“作为条件查询APN NI的扩展方式。
EXUETYPE|扩展终端类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示根据终端类型决定是否对APN NI扩展。设置为“全部扩展”：表示对所有的终端都可以进行APN NI扩展。设置为“仅支持LTE能力终端扩展”：只对支持LTE能力的MS进行APN NI扩展。设置为“仅不支持LTE能力终端扩展”：只对不支持LTE能力的接入的MS进行APN NI扩展。
EXMODE|扩展方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示对APN NI进行扩展的方式，包括六种方式：MSISDN扩展：表示使用MS的MSISDN号段对APN NI进行扩展（即在原APN NI后增加用户的MSISDN号段，最大扩展长度为15位）。IMSI扩展：表示使用MS的IMSI号码对APN NI进行扩展（即在原APN NI后增加用户的IMSI号段，最大扩展长度为15位）。签约计费特性扩展：表示根据MS签约的计费特性对APN NI进行扩展。MS签约热付费，在原APN NI后扩展“.hotbilling“；MS签约平率计费，在原APN NI后扩展”.flatrate”；MS签约预付费，在原APN NI后扩展”.preprid”；MS签约普通计费，在原APN NI后扩展”.normal“签约计费特性+IMSI：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMSI号段对APN NI进行扩展。签约计费特性+MSISDN：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的MSISDN号段对APN NI进行扩展。IMEI扩展：表示使用MS的IMEI号段对APN NI进行扩展（即在原APN NI后增加用户的IMEI号段，最大扩展长度为15位）。注意事项：当“扩展方式“设置为“签约计费特性扩展”时，不需要设置“APN扩展位”，设置为其他扩展方式时，都必须设置“APN扩展位”。
EXBITS|APN扩展位|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：EXBIT_F、EXBIT_T。用于指定APN扩展起始位和APN扩展终止位。
EXBIT_F|APN扩展起始位|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|当APN NI的扩展方式为对IMSI、MSISDN、IMEI号码扩展时，号码的起始扩展位。
EXBIT_T|APN扩展终止位|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|当APN NI的扩展方式为对IMSI、MSISDN、IMEI号码扩展时，号码的结束扩展位。例如：用户的MSISDN为13912345678，APN扩展起始位为4，APN扩展终止位为8，则将12345补充到原APN NI后。
APNCTRL|HOST解析失败后是否使用非扩展APN解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当设置为“否”时：表示SGSN对扩展后的APN进行解析失败后，不再对原APN进行解析。当设置为“是”时：表示SGSN对扩展后的APN进行解析失败后，还会再次对扩展之前的原APN进行解析。
ROAMEXCTRL|漫游用户拜访地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当设置为“否”时：表示在漫游用户通过拜访地的SGSN网元接入的情况下，SGSN将不对漫游用户的APN NI进行扩展。当设置为“是”时：表示在漫游用户通过拜访地的SGSN网元接入的情况下，SGSN支持对漫游用户的APN NI进行扩展。
HOMEEXCTRL|漫游用户归属地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当设置为“否”时：表示漫游用户通过归属地的APN OI+NI选择GGSN网元接入的情况下，SGSN将不对漫游用户的APN NI进行扩展。当设置为“是”时：表示在漫游用户通过归属地的APN OI+NI选择GGSN网元接入的情况下，SGSN支持对漫游用户的APN NI进行扩展。
DTCTRL|DT策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数做为判断SGSN是否支持DT功能的条件之一：当设置为“否”时：SGSN将根据MS的签约的APN信息决定是否支持DT功能。当设置为“是”时：SGSN将对扩展后的APN进行解析，根据得到GGSN的IP地址判断是否支持DT，如果解析出的GGSN的IP地址，可以通过SHOW DT IP命令的查询结果获得，表示SGSN支持DT功能。
EPCEXFLG|LTE能力终端是否扩展特殊字段|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当设置为“是”时，表示对支持LTE能力的终端的APN NI中增加“.pgw”字段。当设置为“否”时，表示对支持LTE能力的终端的APN NI中不增加“.pgw”字段。
IFEXTBASEDCC|根据CC判断是否需进行APN扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否需根据CC判断进行APN扩展。否：APN是否需扩展不需基于用户签约CC值。是：APN是否扩展需基于用户签约CC值，对于特定CC值，不对该APN进行扩展。






命令举例 


修改GPRS扩展APN配置，APN名称为bbs，IMSI/MSISDN号段为434546，将扩展方式修改为签约计费特性+IMSI扩展，APN扩展起始位修改为5，终止位修改为7。 


SET EXAPN:APN="bbs",IMSI="434546",EXMODE="CHARGE+IMSI",EXBITS=5-7; 








父主题： [GPRS扩展APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除GPRS扩展APN配置(DEL EXAPN) 
## 删除GPRS扩展APN配置(DEL EXAPN) 


命令功能 

该命令用于删除APN NI的扩展数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|此参数为APN的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：长度小于63个字符不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*” 除了数字、字母、“-”、和“.”不能输入其余字符示例：zte.com.cn
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|此参数设置为MS的IMSI或MSISDN号段。IMSI（International Mobile Subscriber Identity，国际移动用户标识），由MCC+MNC+MSIN组成。MSISDN（Mobile Station International Subscriber Directory Number，移动台国际用户目录号），由CC+NDC+SN组成。SGSN根据软件参数“扩展APN的号码类型”（ID为786565）来获取APN NI的扩展方式的匹配条件：软件参数取值为“0”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+“IMSI号段”作为条件匹配APN NI的扩展方式。软件参数取值为“1”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+”MSISDN号段“作为条件查询APN NI的扩展方式。






命令举例 


删除GPRS扩展APN配置，APN名称为bbs，IMSI/MSISDN号段为434546。 


DEL EXAPN:APN="bbs",IMSI="434546"; 








父主题： [GPRS扩展APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询GPRS扩展APN配置(SHOW EXAPN) 
## 查询GPRS扩展APN配置(SHOW EXAPN) 


命令功能 


该命令用于查询APN NI的扩展数据。 


不输入任何数据，表示查询当前所有APN NI扩展配置数据。 


输入指定的APN名称或IMSI/MSISDN号段表示查询对应的APN NI扩展配置数据。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|此参数为APN的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：长度小于63个字符。不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头。不能以“.gprs”结尾。不能使用通配符“*”。除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cn
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|此参数设置为MS的IMSI或MSISDN号段。IMSI（International Mobile Subscriber Identity，国际移动用户标识），由MCC+MNC+MSIN组成。MSISDN（Mobile Station International Subscriber Directory Number，移动台国际用户目录号），由CC+NDC+SN组成。SGSN根据软件参数“扩展APN的号码类型”（ID为786565）来获取APN NI的扩展方式的匹配条件：软件参数取值为“0”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+“IMSI号段”作为条件匹配APN NI的扩展方式。软件参数取值为“1”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+”MSISDN号段“作为条件查询APN NI的扩展方式。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
COMAPNID|扩展APN标识|参数可选性:任选参数；参数类型:整数。|该参数为输出参数，表示系统自动生成的标识。
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|此参数为APN的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：长度小于63个字符。不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头。不能以“.gprs”结尾。不能使用通配符“*”。除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cn
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型。|此参数设置为MS的IMSI或MSISDN号段。IMSI（International Mobile Subscriber Identity，国际移动用户标识），由MCC+MNC+MSIN组成。MSISDN（Mobile Station International Subscriber Directory Number，移动台国际用户目录号），由CC+NDC+SN组成。SGSN根据软件参数“扩展APN的号码类型”（ID为786565）来获取APN NI的扩展方式的匹配条件：软件参数取值为“0”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+“IMSI号段”作为条件匹配APN NI的扩展方式。软件参数取值为“1”：表示SGSN将使用ADD EXAPN命令设置的“APN名称“+”MSISDN号段“作为条件查询APN NI的扩展方式。
EXUETYPE|扩展终端类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示根据终端类型决定是否对APN NI扩展。设置为“全部扩展”：表示对所有的终端都可以进行APN NI扩展。设置为“仅支持LTE能力终端扩展”：只对支持LTE能力的MS进行APN NI扩展。设置为“仅不支持LTE能力终端扩展”：只对不支持LTE能力的接入的MS进行APN NI扩展。
EXMODE|扩展方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示对APN NI进行扩展的方式，包括六种方式：MSISDN扩展：表示使用MS的MSISDN号段对APN NI进行扩展（即在原APN NI后增加用户的MSISDN号段，最大扩展长度为15位）。IMSI扩展：表示使用MS的IMSI号码对APN NI进行扩展（即在原APN NI后增加用户的IMSI号段，最大扩展长度为15位）。签约计费特性扩展：表示根据MS签约的计费特性对APN NI进行扩展。MS签约热付费，在原APN NI后扩展“.hotbilling“；MS签约平率计费，在原APN NI后扩展”.flatrate”；MS签约预付费，在原APN NI后扩展”.preprid”；MS签约普通计费，在原APN NI后扩展”.normal“签约计费特性+IMSI：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMSI号段对APN NI进行扩展。签约计费特性+MSISDN：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的MSISDN号段对APN NI进行扩展。IMEI扩展：表示使用MS的IMEI号段对APN NI进行扩展（即在原APN NI后增加用户的IMEI号段，最大扩展长度为15位）。注意事项：当“扩展方式“设置为“签约计费特性扩展”时，不需要设置“APN扩展位”，设置为其他扩展方式时，都必须设置“APN扩展位”。
EXBIT_F|APN扩展起始位|参数可选性:任选参数；参数类型:整数。|当APN NI的扩展方式为对IMSI、MSISDN、IMEI号码扩展时，号码的起始扩展位。
EXBIT_T|APN扩展终止位|参数可选性:任选参数；参数类型:整数。|当APN NI的扩展方式为对IMSI、MSISDN、IMEI号码扩展时，号码的结束扩展位。例如：用户的MSISDN为13912345678，APN扩展起始位为4，APN扩展终止位为8，则将12345补充到原APN NI后。
APNCTRL|HOST解析失败后是否使用非扩展APN解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当设置为“否”时：表示SGSN对扩展后的APN进行解析失败后，不再对原APN进行解析。当设置为“是”时：表示SGSN对扩展后的APN进行解析失败后，还会再次对扩展之前的原APN进行解析。
ROAMEXCTRL|漫游用户拜访地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当设置为“否”时：表示在漫游用户通过拜访地的SGSN网元接入的情况下，SGSN将不对漫游用户的APN NI进行扩展。当设置为“是”时：表示在漫游用户通过拜访地的SGSN网元接入的情况下，SGSN支持对漫游用户的APN NI进行扩展。
HOMEEXCTRL|漫游用户归属地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当设置为“否”时：表示漫游用户通过归属地的APN OI+NI选择GGSN网元接入的情况下，SGSN将不对漫游用户的APN NI进行扩展。当设置为“是”时：表示在漫游用户通过归属地的APN OI+NI选择GGSN网元接入的情况下，SGSN支持对漫游用户的APN NI进行扩展。
DTCTRL|DT策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数做为判断SGSN是否支持DT功能的条件之一：当设置为“否”时：SGSN将根据MS的签约的APN信息决定是否支持DT功能。当设置为“是”时：SGSN将对扩展后的APN进行解析，根据得到GGSN的IP地址判断是否支持DT，如果解析出的GGSN的IP地址，可以通过SHOW DT IP命令的查询结果获得，表示SGSN支持DT功能。
EPCEXFLG|LTE能力终端是否扩展特殊字段|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当设置为“是”时，表示对支持LTE能力的终端的APN NI中增加“.pgw”字段。当设置为“否”时，表示对支持LTE能力的终端的APN NI中不增加“.pgw”字段。
IFEXTBASEDCC|根据CC判断是否需进行APN扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否需根据CC判断进行APN扩展。否：APN是否需扩展不需基于用户签约CC值。是：APN是否扩展需基于用户签约CC值，对于特定CC值，不对该APN进行扩展。






命令举例 


查询GPRS扩展APN配置。 


SHOW EXAPN; 


`

命令 (No.1): SHOW EXAPN

操作维护         扩展APN标识   APN名称   IMSI/MSISDN号段   扩展终端类型              扩展方式                  APN扩展起始位   APN扩展终止位   HOST解析失败后是否使用非扩展APN解析   漫游用户拜访地接入时是否扩展   DT策略                          LTE能力终端是否扩展特殊字段     根据CC判断是否需进行APN扩展
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1             bbs       434546            全部扩展                  MSISDN扩展                2               4               否                                    否                             根据支持DT的GGSN IP配置决策     否                              否
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.031 秒）。
` 








父主题： [GPRS扩展APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# EPC扩展APN配置 
# EPC扩展APN配置 


背景知识 


运营商在部署PGW时，有可能需要考虑用户的号码和签约计费特性等因素，在APN NI中扩展这些用户信息，可以为运营商提供更准确的APN选择PGW的策略。 




功能描述 


MME在进行PGW选择时，根据配置的扩展方法对APN NI进行扩展，然后用扩展后的APN NI来构造APN获取服务的PGW。 


该配置支持多种APN扩展方式（包括：基于IMSI/MSISDN/IMEI号段、签约计费特性、两者的组合方式、基于TA信息、以及无感分流标识扩展）；还可以控制漫游用户在拜访地接入时是否扩展、漫游用户在归属地接入时是否扩展、本地HOST解析失败后是否使用非扩展APN解析、扩展APN解析失败后是否使用非扩展APN解析、根据CC判断是否需进行APN扩展，以及基于CC+IMEI扩展解析失败后是否支持基于CC扩展。 


注意事项： 


软件参数“APN扩展号码类型”（ID：786565），控制APN扩展使用的号码类型，软件参数取值为0，则使用IMSI扩展APN；取值为1，则使用MSISDN扩展APN。 


“本地HOST解析失败后是否使用非扩展APN解析”和“扩展APN解析失败后是否使用非扩展APN解析”的使用场景： 



 

“本地HOST解析失败后是否使用非扩展APN解析”，用于设置当MME使用扩展APN在本地解析PGW地址失败后，是否使用非扩展APN继续尝试解析PGW地址。
 

 

“扩展APN解析失败后是否使用非扩展APN解析”，用于设置当MME使用扩展APN在本地解析PGW地址和通过DNS解析PGW地址都失败后，是否使用非扩展APN继续尝试解析PGW地址。
 

 


当软件参数“MME地址解析优先级”（ID：65593）取值为0（Host Local-DNS Cache-DNS Server）或者1（Host Local-DNS Server）时，有如下两种情况： 



 

如果“扩展APN解析失败后是否使用非扩展APN解析”设置为“是”，则根据该配置使用扩展APN在本地解析PGW地址和通过DNS解析PGW地址都失败后，再使用非扩展APN继续尝试解析PGW地址。
 

 

如果“扩展APN解析失败后是否使用非扩展APN解析”设置为“否”，则根据“本地HOST解析失败后是否使用非扩展APN解析”参数控制使用扩展APN解析失败后是否使用非扩展APN继续尝试解析。
 

 


当软件参数“MME地址解析优先级”（ID：65593）取值为2（DNS Cache-DNS Server-Host Local）或者3（DNS Server-Host Local）时，仅使用“本地HOST解析失败后是否使用非扩展APN解析”参数控制使用扩展APN解析失败后是否使用非扩展APN继续尝试解析。 




相关主题 



 

新增EPC扩展APN配置(ADD EPC EXAPN)
 

 

修改EPC扩展APN配置(SET EPC EXAPN)
 

 

删除EPC扩展APN配置(DEL EPC EXAPN)
 

 

查询EPC扩展APN配置(SHOW EPC EXAPN)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增EPC扩展APN配置(ADD EPC EXAPN) 
## 新增EPC扩展APN配置(ADD EPC EXAPN) 


命令功能 

该命令用于新增EPC扩展APN配置。当运营商希望通过用户号码段更准确的获取本次服务的PGW时，使用该命令，EPC扩展APN配置成功后，MME根据IMSI/MSISDN/IMEI号段、签约计费特性、两者的组合方式、TA信息、以及无感分流标识对APN NI进行扩展，然后通过扩展的APN获取到PGW的IP地址。


注意事项 



 
扩展后的APN NI总长度不得超过61个字符，否则只会截取前61个字符。
 

 
IMSI/MSISDN号段和APN名称必须至少配置其中一个。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|APN名称由Network Identifier（NI）组成，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|通过扩展的APN获取到PGW的IP地址的IMSI/MSISDN号段。
NUMBERTYPE|扩展方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置EPC扩展APN的扩展方式，取值含义：MSISDN扩展：MME使用MSISDN进行APN扩展。IMSI扩展：MME使用IMSI进行APN扩展。签约计费特性扩展：表示根据MS签约的计费特性对APN NI进行扩展。签约计费特性+IMSI扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMSI号段对APN NI进行扩展。签约计费特性+MSISDN扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的MSISDN号段对APNNI进行扩展。IMEI扩展：MME使用IMEI进行APN扩展。签约计费特性+IMEI扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMEI号段对APNNI进行扩展。TA信息扩展：MME使用TA信息进行APN扩展。无感分流标识扩展：MME使用无感分流标识进行APN扩展。注：“TA信息扩展”仅在License项“MME支持基于TA和APN解析PGW”打开时才生效。注：“无感分流标识扩展”仅在License项“MME支持无感分流功能”打开时才生效
EXBIT|APN扩展位|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：EXBEGIN、EXEND。用于指定APN扩展起始位和APN扩展终止位。
EXBEGIN|APN扩展起始位|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|针对IMSI或MSISDN扩展时，APN扩展的起始位。最小配置数值1，最大配置数值为15。
EXEND|APN扩展终止位|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|针对IMSI或MSISDN扩展时，APN扩展的终止位。最小配置数值1，最大配置数值为15，APN扩展终止位应大于等于扩展起始位。
APNCTRL|HOST解析失败后是否使用非扩展APN解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置当MME使用扩展APN在本地解析PGW的IP地址失败后，是否使用非扩展APN继续尝试解析PGW的IP地址，取值含义：是(YES) ： 使用非扩展APN进行解析否(NO) ：不使用非扩展APN进行解析
ROAMEXCTRL|漫游用户拜访地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置漫游用户从拜访地接入时，MME是否需要进行APN扩展，取值含义：是(YES) ：进行APN扩展否(NO) ：不进行APN扩展
HOMEEXCTRL|漫游用户归属地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置漫游用户在归属地接入时，MME是否需要进行APN扩展，取值含义：是(YES) ：进行APN扩展否(NO) ：不进行APN扩展
IFEXTBASEDCC|根据CC判断是否需进行APN扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置是否需根据CC判断进行APN扩展。否：APN是否需扩展不需基于用户签约CC值。是：APN是否扩展需基于用户签约CC值，对于特定CC值，不对该APN进行扩展。
NONEXTAFTEXTAPNFAIL|扩展APN解析失败后是否使用非扩展APN解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置当MME使用扩展APN在本地解析和通过DNS解析PGW的IP地址都失败后，是否使用非扩展APN继续尝试解析PGW的IP地址。
CCEXTAFTCCIMEIFAIL|基于CC+IMEI扩展解析失败后支持CC扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置当MME使用CC+IMEI扩展APN解析PGW的IP地址失败后，是否使用CC扩展APN继续尝试解析PGW的IP地址。
TAINFOFORMAT|TA信息扩展格式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:TAGROUP。|该参数用于使用TA信息扩展时设置TA扩展格式，取值含义：扩展TAC高位：扩展后APN-FQDN格式为tac-hb<TAC-high-byte>.APNNI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。扩展完整TAC：扩展后APN-FQDN格式为tac-lb<TAC-low-byte>.tac-hb<TAC-high-byte>.APNNI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。扩展TAI高位：扩展后APN-FQDN格式为tac-hb<TAC-high-byte>.mnc<TA-MNC>.mcc<TA-MCC>.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。扩展完整TAI：扩展后APN-FQDN格式为tac-lb<TAC-low-byte>.tac-hb<TAC-high-byte>.mnc<TA-MNC>.mcc<TA-MCC>.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。扩展TA组：扩展后APN-FQDN格式为TAGroupName.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。
RESELIFDEDPGWFAIL|选择无感分流专用PGW失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于设置基于无感分流标识扩展APN解析成功，选择无感分流专用PGW失败后，是否使用非扩展APN重选普通PGW。取值含义：否：不重选普通PGW。如果所有专用PGW均不可达，则MME从不可达的专用PGW中随机选择一个PGW。是：重选普通PGW。如果所有专用PGW均不可达，则MME使用非扩展APN重新选择普通PGW。






命令举例 


新增EPC扩展APN配置，APN名称为zte.com，IMSI号段前缀为46001，扩展方式为IMSI扩展，APN扩展位为2-4位，HOST解析失败后使用非扩展APN解析。 


ADD EPC EXAPN:APNNAME="zte.com",IMSI="46001",NUMBERTYPE="IMSI",EXBIT=2-4,APNCTRL="YES"; 








父主题： [EPC扩展APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改EPC扩展APN配置(SET EPC EXAPN) 
## 修改EPC扩展APN配置(SET EPC EXAPN) 


命令功能 

该命令用于修改EPC扩展APN配置。当需要修改APN扩展中IMSI/MSISDN号段、扩展方式、APN扩展位等信息时，使用该命令。EPC扩展APN配置修改成功后，MME根据IMSI/MSISDN/IMEI号段、签约计费特性、两者的组合方、TA信息、以及无感分流标识对APN NI进行扩展，然后通过扩展的APN获取到PGW的IP地址。


注意事项 



 
扩展后的APN NI总长度不得超过61个字符，否则只会截取前61个字符。
 

 
IMSI/MSISDN号段和APN名称必须至少配置其中一个。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|APN名称由Network Identifier（NI）组成，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|通过扩展的APN获取到PGW的IP地址的IMSI/MSISDN号段。
NUMBERTYPE|扩展方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置EPC扩展APN的扩展方式，取值含义：MSISDN扩展：MME使用MSISDN进行APN扩展。IMSI扩展：MME使用IMSI进行APN扩展。签约计费特性扩展：表示根据MS签约的计费特性对APN NI进行扩展。签约计费特性+IMSI扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMSI号段对APN NI进行扩展。签约计费特性+MSISDN扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的MSISDN号段对APNNI进行扩展。IMEI扩展：MME使用IMEI进行APN扩展。签约计费特性+IMEI扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMEI号段对APNNI进行扩展。TA信息扩展：MME使用TA信息进行APN扩展。无感分流标识扩展：MME使用无感分流标识进行APN扩展。注：“TA信息扩展”仅在License项“MME支持基于TA和APN解析PGW”打开时才生效。注：“无感分流标识扩展”仅在License项“MME支持无感分流功能”打开时才生效
EXBIT|APN扩展位|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：EXBEGIN、EXEND。用于指定APN扩展起始位和APN扩展终止位。
EXBEGIN|APN扩展起始位|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|针对IMSI或MSISDN扩展时，APN扩展的起始位。最小配置数值1，最大配置数值为15。
EXEND|APN扩展终止位|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|针对IMSI或MSISDN扩展时，APN扩展的终止位。最小配置数值1，最大配置数值为15，APN扩展终止位应大于等于扩展起始位。
APNCTRL|HOST解析失败后是否使用非扩展APN解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME使用扩展APN在本地解析PGW的IP地址失败后，是否使用非扩展APN继续尝试解析PGW的IP地址，取值含义：是(YES) ： 使用非扩展APN进行解析否(NO) ：不使用非扩展APN进行解析
ROAMEXCTRL|漫游用户拜访地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置漫游用户从拜访地接入时，MME是否需要进行APN扩展，取值含义：是(YES) ：进行APN扩展否(NO) ：不进行APN扩展
HOMEEXCTRL|漫游用户归属地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置漫游用户在归属地接入时，MME是否需要进行APN扩展，取值含义：是(YES) ：进行APN扩展否(NO) ：不进行APN扩展
IFEXTBASEDCC|根据CC判断是否需进行APN扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否需根据CC判断进行APN扩展。否：APN是否需扩展不需基于用户签约CC值。是：APN是否扩展需基于用户签约CC值，对于特定CC值，不对该APN进行扩展。
NONEXTAFTEXTAPNFAIL|扩展APN解析失败后是否使用非扩展APN解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME使用扩展APN在本地解析和通过DNS解析PGW的IP地址都失败后，是否使用非扩展APN继续尝试解析PGW的IP地址。
CCEXTAFTCCIMEIFAIL|基于CC+IMEI扩展解析失败后支持CC扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME使用CC+IMEI扩展APN解析PGW的IP地址失败后，是否使用CC扩展APN继续尝试解析PGW的IP地址。
TAINFOFORMAT|TA信息扩展格式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于使用TA信息扩展时设置TA扩展格式，取值含义：扩展TAC高位：扩展后APN-FQDN格式为tac-hb<TAC-high-byte>.APNNI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。扩展完整TAC：扩展后APN-FQDN格式为tac-lb<TAC-low-byte>.tac-hb<TAC-high-byte>.APNNI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。扩展TAI高位：扩展后APN-FQDN格式为tac-hb<TAC-high-byte>.mnc<TA-MNC>.mcc<TA-MCC>.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。扩展完整TAI：扩展后APN-FQDN格式为tac-lb<TAC-low-byte>.tac-hb<TAC-high-byte>.mnc<TA-MNC>.mcc<TA-MCC>.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。扩展TA组：扩展后APN-FQDN格式为TAGroupName.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。
RESELIFDEDPGWFAIL|选择无感分流专用PGW失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于无感分流标识扩展APN解析成功，选择无感分流专用PGW失败后，是否使用非扩展APN重选普通PGW。取值含义：否：不重选普通PGW。如果所有专用PGW均不可达，则MME从不可达的专用PGW中随机选择一个PGW。是：重选普通PGW。如果所有专用PGW均不可达，则MME使用非扩展APN重新选择普通PGW。






命令举例 


修改EPC扩展APN配置，APN名称为zte.com，IMSI/MSISDN号段为46001，将扩展方式修改为MSISDN扩展，APN扩展起始位修改为2，终止位修改为4，HOST解析失败后使用非扩展APN进行解析。 


SET EPC EXAPN:APNNAME="zte.com",IMSI="46001",NUMBERTYPE="MSISDN",EXBIT=2-4,APNCTRL="YES"; 








父主题： [EPC扩展APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除EPC扩展APN配置(DEL EPC EXAPN) 
## 删除EPC扩展APN配置(DEL EPC EXAPN) 


命令功能 

该命令用于删除EPC扩展APN配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|APN名称由Network Identifier（NI）组成，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|通过扩展的APN获取到PGW的IP地址的IMSI/MSISDN号段。






命令举例 


删除EPC扩展APN配置，APN名称为zte.com，IMSI号段前缀为46001。 


DEL EPC EXAPN:APNNAME="zte.com",IMSI="46001"; 








父主题： [EPC扩展APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询EPC扩展APN配置(SHOW EPC EXAPN) 
## 查询EPC扩展APN配置(SHOW EPC EXAPN) 


命令功能 

该命令用于查询EPC扩展APN配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|APN名称由Network Identifier（NI）组成，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|通过扩展的APN获取到PGW的IP地址的IMSI/MSISDN号段。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型。|APN名称由Network Identifier（NI）组成，格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IMSI|IMSI/MSISDN号段|参数可选性:任选参数；参数类型:字符型。|通过扩展的APN获取到PGW的IP地址的IMSI/MSISDN号段。
NUMBERTYPE|扩展方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置EPC扩展APN的扩展方式，取值含义：MSISDN扩展：MME使用MSISDN进行APN扩展。IMSI扩展：MME使用IMSI进行APN扩展。签约计费特性扩展：表示根据MS签约的计费特性对APN NI进行扩展。签约计费特性+IMSI扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMSI号段对APN NI进行扩展。签约计费特性+MSISDN扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的MSISDN号段对APNNI进行扩展。IMEI扩展：MME使用IMEI进行APN扩展。签约计费特性+IMEI扩展：根据MS签约的计费特性对APN NI进行扩展后，再根据MS的IMEI号段对APNNI进行扩展。TA信息扩展：MME使用TA信息进行APN扩展。无感分流标识扩展：MME使用无感分流标识进行APN扩展。注：“TA信息扩展”仅在License项“MME支持基于TA和APN解析PGW”打开时才生效。注：“无感分流标识扩展”仅在License项“MME支持无感分流功能”打开时才生效
EXBEGIN|APN扩展起始位|参数可选性:任选参数；参数类型:整数。|针对IMSI或MSISDN扩展时，APN扩展的起始位。最小配置数值1，最大配置数值为15。
EXEND|APN扩展终止位|参数可选性:任选参数；参数类型:整数。|针对IMSI或MSISDN扩展时，APN扩展的终止位。最小配置数值1，最大配置数值为15，APN扩展终止位应大于等于扩展起始位。
APNCTRL|HOST解析失败后是否使用非扩展APN解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME使用扩展APN在本地解析PGW的IP地址失败后，是否使用非扩展APN继续尝试解析PGW的IP地址，取值含义：是(YES) ： 使用非扩展APN进行解析否(NO) ：不使用非扩展APN进行解析
ROAMEXCTRL|漫游用户拜访地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置漫游用户从拜访地接入时，MME是否需要进行APN扩展，取值含义：是(YES) ：进行APN扩展否(NO) ：不进行APN扩展
HOMEEXCTRL|漫游用户归属地接入时是否扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置漫游用户在归属地接入时，MME是否需要进行APN扩展，取值含义：是(YES) ：进行APN扩展否(NO) ：不进行APN扩展
IFEXTBASEDCC|根据CC判断是否需进行APN扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否需根据CC判断进行APN扩展。否：APN是否需扩展不需基于用户签约CC值。是：APN是否扩展需基于用户签约CC值，对于特定CC值，不对该APN进行扩展。
NONEXTAFTEXTAPNFAIL|扩展APN解析失败后是否使用非扩展APN解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME使用扩展APN在本地解析和通过DNS解析PGW的IP地址都失败后，是否使用非扩展APN继续尝试解析PGW的IP地址。
CCEXTAFTCCIMEIFAIL|基于CC+IMEI扩展解析失败后支持CC扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME使用CC+IMEI扩展APN解析PGW的IP地址失败后，是否使用CC扩展APN继续尝试解析PGW的IP地址。
TAINFOFORMAT|TA信息扩展格式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于使用TA信息扩展时设置TA扩展格式，取值含义：扩展TAC高位：扩展后APN-FQDN格式为tac-hb<TAC-high-byte>.APNNI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。扩展完整TAC：扩展后APN-FQDN格式为tac-lb<TAC-low-byte>.tac-hb<TAC-high-byte>.APNNI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org。扩展TAI高位：扩展后APN-FQDN格式为tac-hb<TAC-high-byte>.mnc<TA-MNC>.mcc<TA-MCC>.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。扩展完整TAI：扩展后APN-FQDN格式为tac-lb<TAC-low-byte>.tac-hb<TAC-high-byte>.mnc<TA-MNC>.mcc<TA-MCC>.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。扩展TA组：扩展后APN-FQDN格式为TAGroupName.APNNI.apn.epc.mnc<IMSI-MNC>.mcc<IMSI-MCC>.3gppnetwork.org。
RESELIFDEDPGWFAIL|选择无感分流专用PGW失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于无感分流标识扩展APN解析成功，选择无感分流专用PGW失败后，是否使用非扩展APN重选普通PGW。取值含义：否：不重选普通PGW。如果所有专用PGW均不可达，则MME从不可达的专用PGW中随机选择一个PGW。是：重选普通PGW。如果所有专用PGW均不可达，则MME使用非扩展APN重新选择普通PGW。






命令举例 


查询EPC扩展APN配置。 


SHOW MME EXAPN; 


`

命令 (No.1): SHOW EPC EXAPN

操作维护          APN名称   IMSI/MSISDN号段   扩展方式     APN扩展起始位   APN扩展终止位   HOST解析失败后是否使用非扩展APN解析   漫游用户拜访地接入时是否扩展   漫游用户归属地接入时是否扩展   根据CC判断是否需进行APN扩展   扩展APN解析失败后是否使用非扩展APN解析   基于CC+IMEI扩展解析失败后支持CC扩展   TA信息扩展格式   选择无感分流专用PGW失败是否重选
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除    zte.com   460119999999999   MSISDN扩展   1               4               否                                    否                             否                             否                            否                                       否                                    扩展TAC高位      否   
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.051 秒）。
` 








父主题： [EPC扩展APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# GPRS APN优选GGSN配置 
# GPRS APN优选GGSN配置 


背景知识 


SGSN网元通过A/AAAA查询或者本地配置的Host查询得到GPRS APN对应的一组GGSN IP地址后，需要选择一个GGSN来提供本次业务。 




功能描述 


SGSN给查询到的每个GGSN的IP地址赋值一个优先级和权重，选择出高优先级的GGSN的IP地址，如果高优先级的IP地址是多个，再根据权重选出一个GGSN IP地址，目的是为了更准确地获取到本次服务的GGSN。 


该配置支持基于APN、位置区名称、路由区名称、或三者的任意组合方式，对GGSN的IP地址按照优先级和权重进行优选。 




相关主题 



 

新增GPRS APN优选GGSN配置(ADD GPRS APN GGSN PRI)
 

 

修改GPRS APN优选GGSN配置(SET GPRS APN GGSN PRI)
 

 

删除GPRS APN优选GGSN配置(DEL GPRS APN GGSN PRI)
 

 

查询GPRS APN优选GGSN配置(SHOW GPRS APN GGSN PRI)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增GPRS APN优选GGSN配置(ADD GPRS APN GGSN PRI) 
## 新增GPRS APN优选GGSN配置(ADD GPRS APN GGSN PRI) 


命令功能 


该命令用于配置如何为SGSN，根据APN解析的结果，从中选择一个最佳的GGSN。 


当一个APN通过SGSN本地配置或者DNS解析出多个GGSN IP地址时，SGSN为了更准确地获取到本次服务的GGSN，需要通过该命令来优选出一个最合适的GGSN。 




注意事项 


该功能只适用于SGSN网元。 


该命令的配置数据受软件参数“GGSN子网优先级选择方式”（ID为65566）的影响，该软件参数包括如下选项： 



 
当“GGSN子网优先级选择方式”设置为0，表示SGSN根据“APN名称”来匹配GGSN的优先级。
 

 
当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~82个字符。|APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*” 除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置某个APN的名称为“zte.com.cn.mnc011.mcc460.gprs”。
LAINAME|位置区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
SNPRI|配置优先级|参数可选性:必选参数；参数类型:复合参数|该参数是以下四个参数的组合：ADDR、LEN、PRI、WEIGHT。用于指定GGSN的IP地址、长度、优先级和权重。
ADDR|地址|参数可选性:必选参数；参数类型:字符型；参数范围为:1~39个字符。|由地址、长度、优先级和权重，四个维度来决定最终优选的GGSN的控制面IP地址。SGSN对APN进行解析后，可能得到多个GGSN IP地址，根据此命令配置的“地址”和“长度”与多个GGSN IP地址比较，如果匹配出多个IP地址，再根据对应的优先级和权重，来选择GGSN。
LEN|长度|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|表示IP地址的掩码长度。
PRI|优先级|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|表示GGSN控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT|权重|参数可选性:必选参数；参数类型:整数；参数范围为:0~100。|表示GGSN控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。






命令举例 


新增GPRS APN优选GGSN配置，APN名称为zte.com.mnc111.mcc222.gprs，其中地址为12.1.1.1/24的优先级为1，权重为22，地址为12.2.2.2/24的优先级为2，权重为23。 


ADD GPRS APN GGSN PRI:APN="zte.com.mnc111.mcc222.gprs",SNPRI="12.1.1.1"-24-1-22&"12.2.2.2"-24-2-23; 








父主题： [GPRS APN优选GGSN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改GPRS APN优选GGSN配置(SET GPRS APN GGSN PRI) 
## 修改GPRS APN优选GGSN配置(SET GPRS APN GGSN PRI) 


命令功能 

该命令用于修改APN的GGSN优选配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~82个字符。|APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*” 除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置某个APN的名称为“zte.com.cn.mnc011.mcc460.gprs”。
LAINAME|位置区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
ADDR|地址|参数可选性:必选参数；参数类型:字符型；参数范围为:1~39个字符。|由地址、长度、优先级和权重，四个维度来决定最终优选的GGSN的控制面IP地址。SGSN对APN进行解析后，可能得到多个GGSN IP地址，根据此命令配置的“地址”和“长度”与多个GGSN IP地址比较，如果匹配出多个IP地址，再根据对应的优先级和权重，来选择GGSN。
LEN|长度|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|表示IP地址的掩码长度。
PRI|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|表示GGSN控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|表示GGSN控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。






命令举例 


修改GPRS APN优选GGSN配置，APN名称为zte.com.mnc111.mcc222.gprs，其中地址为12.1.1.1/24的优先级为5，权重为32。 


SET GPRS APN GGSN PRI:APN="zte.com.mnc111.mcc222.gprs",ADDR="12.1.1.1",LEN=24,PRI=5,WEIGHT=32; 








父主题： [GPRS APN优选GGSN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除GPRS APN优选GGSN配置(DEL GPRS APN GGSN PRI) 
## 删除GPRS APN优选GGSN配置(DEL GPRS APN GGSN PRI) 


命令功能 

该命令用于删除APN的GGSN优选配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~82个字符。|APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*” 除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置某个APN的名称为“zte.com.cn.mnc011.mcc460.gprs”。
LAINAME|位置区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
SNPRI|配置优先级|参数可选性:任选参数；参数类型:复合参数|该参数是以下四个参数的组合：ADDR、LEN、PRI、WEIGHT。用于指定GGSN的IP地址、长度、优先级和权重。
ADDR|地址|参数可选性:必选参数；参数类型:字符型；参数范围为:1~39个字符。|由地址、长度、优先级和权重，四个维度来决定最终优选的GGSN的控制面IP地址。SGSN对APN进行解析后，可能得到多个GGSN IP地址，根据此命令配置的“地址”和“长度”与多个GGSN IP地址比较，如果匹配出多个IP地址，再根据对应的优先级和权重，来选择GGSN。
LEN|长度|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|表示IP地址的掩码长度。






命令举例 


删除APN名称为zte.com.mnc111.mcc222.gprs的GPRS APN优选GGSN配置。 


DEL GPRS APN GGSN PRI:APN="zte.com.mnc111.mcc222.gprs"; 








父主题： [GPRS APN优选GGSN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询GPRS APN优选GGSN配置(SHOW GPRS APN GGSN PRI) 
## 查询GPRS APN优选GGSN配置(SHOW GPRS APN GGSN PRI) 


命令功能 

该命令用于查询APN的GGSN优选配置。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~82个字符。|APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*” 除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置某个APN的名称为“zte.com.cn.mnc011.mcc460.gprs”。
LAINAME|位置区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*” 除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”，要求如下：<MNC>和<MCC>都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs例如：设置某个APN的名称为“zte.com.cn.mnc011.mcc460.gprs”。
LAINAME|位置区名称|参数可选性:任选参数；参数类型:字符型。|此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任选参数；参数类型:字符型。|此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
ADDR1|地址1|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN1|长度1|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI1|优先级1|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT1|权重1|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR2|地址2|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN2|长度2|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI2|优先级2|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT2|权重2|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR3|地址3|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN3|长度3|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI3|优先级3|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT3|权重3|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR4|地址4|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN4|长度4|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI4|优先级4|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT4|权重4|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR5|地址5|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN5|长度5|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI5|优先级5|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT5|权重5|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR6|地址6|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN6|长度6|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI6|优先级6|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT6|权重6|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR7|地址7|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN7|长度7|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI7|优先级7|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT7|权重7|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR8|地址8|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN8|长度8|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI8|优先级8|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT8|权重8|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR9|地址9|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN9|长度9|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI9|优先级9|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT9|权重9|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR10|地址10|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN10|长度10|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI10|优先级10|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT10|权重10|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR11|地址11|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN11|长度11|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI11|优先级11|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT11|权重11|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR12|地址12|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN12|长度12|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI12|优先级12|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT12|权重12|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR13|地址13|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN13|长度13|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI13|优先级13|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT13|权重13|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR14|地址14|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN14|长度14|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI14|优先级14|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT14|权重14|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR15|地址15|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN15|长度15|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI15|优先级15|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT15|权重15|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。
ADDR16|地址16|参数可选性:任选参数；参数类型:字符型。|此参数为输出参数，表示GGSN的控制面IP地址。
LEN16|长度16|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示IP地址的掩码长度。
PRI16|优先级16|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的优先级，数值越小，表示优先级越高。SGSN将优先选择优先级高的GGSN IP地址。
WEIGHT16|权重16|参数可选性:任选参数；参数类型:整数。|此参数为输出参数，表示GGSN 控制面IP地址的权重，数值越大，表示权重越高。如果多个GGSN IP地址对应的优先级相同，无法区分出最优GGSN，SGSN根据“权重”对GGSN进行选择。






命令举例 


查询GPRS APN优选GGSN配置。 


SHOW GPRS APN GGSN PRI; 


`

命令 (No.1): SHOW GPRS APN GGSN PRI

操作维护         APN名称                      位置区名称    路由区名称   地址1      长度1   优先级1   权重1   地址2      长度2   优先级2   权重2   地址3     长度3   优先级3   权重3   地址4     长度4   优先级4   权重4   地址5     长度5   优先级5   权重5   地址6     长度6   优先级6   权重6   地址7     长度7   优先级7   权重7   地址8     长度8   优先级8   权重8   地址9     长度9   优先级9   权重9   地址10    长度10   优先级10   权重10   地址11    长度11   优先级11   权重11   地址12    长度12   优先级12   权重12   地址13    长度13   优先级13   权重13   地址14    长度14   优先级14   权重14   地址15    长度15   优先级15   权重15   地址16    长度16   优先级16   权重16
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   zte.com.mnc111.mcc222.gprs                              12.1.1.1   24      1         22      12.2.2.2   24      2         23      0.0.0.0   0       0         0       0.0.0.0   0       0         0       0.0.0.0   0       0         0       0.0.0.0   0       0         0       0.0.0.0   0       0         0       0.0.0.0   0       0         0       0.0.0.0   0       0         0       0.0.0.0   0        0          0        0.0.0.0   0        0          0        0.0.0.0   0        0          0        0.0.0.0   0        0          0        0.0.0.0   0        0          0        0.0.0.0   0        0          0        0.0.0.0   0        0          0
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.054 秒）。
` 








父主题： [GPRS APN优选GGSN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# EPC APN优选子网段配置 
# EPC APN优选子网段配置 


背景知识 


MME/SGSN使用EPC形式的APN进行NAPTR（名称权威指针，Naming Authority Pointer）查询或本地HOST查询，可以得到一组PGW列表。MME/SGSN根据PGW的优先级、权重、拓扑关系、节点有效性等选择策略选出一个PGW。SGSN出Gn/Gp口时是与PGW内置的GGSN进行业务交互。 




功能描述 


MME/SGSN可以为选出的PGW的每个IP地址段，先赋值一个子网优先级，再选择高优先级的PGW的IP地址。如果高优先级的IP地址既有IPv4地址，又有IPv6地址，则根据软参“与非邻接网元交互时业务IP双栈优选的IP类型”（ID：786569），确定是选择IPv4地址还是IPv6地址。如果高优先级的IP地址有多个，则随机选择一个。目的是为了更准确地获取到本次服务的PGW。 


当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该配置支持基于APN、位置区名称、路由区名称、或三者的任意组合方式，对GGSN的IP地址按照优先级进行优选；当终端接入MME/SGSN，MME/SGSN分别出S11口/S4口通过SGW与PGW交互时，该配置支持基于APN对PGW的IP地址按照优先级进行优选。 




相关主题 



 

新增EPC APN优选子网段配置(ADD EPC APN SUBNET PRI)
 

 

修改EPC APN优选子网段配置(SET EPC APN SUBNET PRI)
 

 

删除EPC APN优选子网段配置(DEL EPC APN SUBNET PRI)
 

 

查询EPC APN优选子网段配置(SHOW EPC APN SUBNET PRI)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增EPC APN优选子网段配置(ADD EPC APN SUBNET PRI) 
## 新增EPC APN优选子网段配置(ADD EPC APN SUBNET PRI) 


命令功能 


该命令用于配置如何为MME/SGSN，根据APN解析的结果，从中选择一个最佳的PGW。 


当一个APN通过MME/SGSN本地配置或者DNS解析出多个PGW IP地址时，MME/SGSN为了更准确地获取到本次服务的PGW，需要通过该命令来优选出一个最合适的PGW。SGSN出Gn/Gp口时是与PGW内置的GGSN进行业务交互。 


当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该配置支持基于APN、位置区名称、路由区名称、或三者的任意组合方式，对GGSN的IP地址按照优先级进行优选；该命令的配置数据受软件参数“GGSN子网优先级选择方式”（ID为65566）的影响，可以根据“APN名称”、“APN名称”+“位置区名称”、“APN名称”+“路由区名称”来匹配GGSN的优先级。 


当终端接入MME/SGSN，MME/SGSN分别出S11口/S4口通过SGW与PGW交互时，MME/SGSN根据“APN”名称来匹配PGW的优先级。 




注意事项 


该功能适用于MME/SGSN网元。 


当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该命令的配置数据受软件参数“GGSN子网优先级选择方式”（ID为65566）的影响，该软件参数包括如下选项： 



 
当“GGSN子网优先级选择方式”设置为0，表示SGSN根据“APN名称”来匹配GGSN的优先级。
 

 
当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
 

 


当终端接入MME/SGSN，MME/SGSN分别出S11口/S4口通过SGW与PGW交互时，不受该软件参数的影响，MME/SGSN根据“APN名称”来匹配PGW的优先级。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过100个字符。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“SGSN”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
LAINAME|位置区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
SNPRI|子网优先级|参数可选性:必选参数；参数类型:复合参数|该参数是以下三个参数的组合：IP、MASKLEN、PRI。用于指定PGW的子网地址、掩码长度和优先级。
IP|子网地址|参数可选性:必选参数；参数类型:地址|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN|掩码长度|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI|优先级|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|数值越小，优先级越高。以下各优先级同此说明。






命令举例 


为APN名称为"zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org"增加优选子网段配置，其中地址段为“6.0.87.0”，掩码为23位，优先级为5。 


ADD EPC APN SUBNET PRI:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",SNPRI="6.0.87.0"-23-5; 








父主题： [EPC APN优选子网段配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改EPC APN优选子网段配置(SET EPC APN SUBNET PRI) 
## 修改EPC APN优选子网段配置(SET EPC APN SUBNET PRI) 


命令功能 


该命令用于修改EPC APN优选子网段配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过100个字符。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“SGSN”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
LAINAME|位置区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
IP|子网地址|参数可选性:必选参数；参数类型:地址|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN|掩码长度|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|数值越小，优先级越高。以下各优先级同此说明。






命令举例 


为APN名称为"zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org"修改优选子网段配置，其中地址段为“6.0.87.0”，掩码为23位，优先级为7。 


SET EPC APN SUBNET PRI:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",IP="6.0.87.0",MASKLEN=23,PRI=7; 








父主题： [EPC APN优选子网段配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除EPC APN优选子网段配置(DEL EPC APN SUBNET PRI) 
## 删除EPC APN优选子网段配置(DEL EPC APN SUBNET PRI) 


命令功能 


该命令用于删除EPC APN优选子网段配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过100个字符。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“SGSN”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
LAINAME|位置区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
SUBNET|子网段|参数可选性:任选参数；参数类型:复合参数|该参数是IP和MASKLEN两个参数的组合，用于指定PGW的子网地址和掩码长度。
IP|子网地址|参数可选性:必选参数；参数类型:地址|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN|掩码长度|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。






命令举例 


删除APN名称为"zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org"的优选子网段配置。 


DEL EPC APN SUBNET PRI:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org"; 








父主题： [EPC APN优选子网段配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询EPC APN优选子网段配置(SHOW EPC APN SUBNET PRI) 
## 查询EPC APN优选子网段配置(SHOW EPC APN SUBNET PRI) 


命令功能 


该命令用于查询EPC APN优选子网段配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过100个字符。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“SGSN”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
LAINAME|位置区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任意单选参数；参数类型:字符型；参数范围为:0~50个字符。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|APN名称由Network Identifier（NI）和Operator Identifier（OI）,加上插在二者之间的“apn.epc”组成，格式为“APN-NI.apn.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。APN协议规定最长不能超过100个字符。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“SGSN”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。 OI部分格式为“mnc<MNC>.mcc<MCC>.3gppnetwork.org”，MNC和MCC都是三位0~9的数字，不足三位的，靠前补零。
LAINAME|位置区名称|参数可选性:任选参数；参数类型:字符型。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD LAI命令设置的“位置区名”，可以通过SHOW LAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
RAINAME|路由区名称|参数可选性:任选参数；参数类型:字符型。|当具有EPC能力的终端接入SGSN，SGSN出Gn/Gp口与PGW内置的GGSN交互时，该参数可作为可选配置。此参数的取值，是通过ADD RAI命令设置的“路由区名称”，可以通过SHOW RAI命令查询获取。SGSN根据软件参数“GGSN子网优先级选择方式”（ID为65566）来获取GGSN IP地址匹配条件：当“GGSN子网优先级选择方式”设置为0，表示SGSN只根据“APN名称”来匹配GGSN的优先级。当“GGSN子网优先级选择方式”设置为1，表示SGSN根据“APN名称”+“位置区名称”或“路由区名称”来匹配GGSN的优先级。
IP1|子网地址1|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN1|掩码长度1|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI1|优先级1|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。
IP2|子网地址2|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN2|掩码长度2|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI2|优先级2|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。
IP3|子网地址3|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN3|掩码长度3|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI3|优先级3|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。
IP4|子网地址4|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN4|掩码长度4|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI4|优先级4|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明，不再详述。
IP5|子网地址5|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN5|掩码长度5|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI5|优先级5|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。
IP6|子网地址6|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN6|掩码长度6|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI6|优先级6|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。
IP7|子网地址7|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN7|掩码长度7|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI7|优先级7|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。
IP8|子网地址8|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN8|掩码长度8|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI8|优先级8|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。
IP9|子网地址9|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地+E43址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN9|掩码长度9|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI9|优先级9|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。
IP10|子网地址10|参数可选性:任选参数；参数类型:字符型。|配置PGW的IP地址，可设置为IPv4或者IPv6地址。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。以下各IP地址同此说明。
MASKLEN10|掩码长度10|参数可选性:任选参数；参数类型:整数。|IPv4格式的地址掩码长度为0-32，IPv6格式的地址掩码长度为0-128。以下各掩码长度同此说明。
PRI10|优先级10|参数可选性:任选参数；参数类型:整数。|数值越小，优先级越高。以下各优先级同此说明。






命令举例 


查询EPC APN优选子网段配置信息。 


SHOW EPC APN SUBNET PRI; 


`

命令 (No.2): SHOW EPC APN SUBNET PRI

操作维护         APN名称                                         位置区名称    路由区名称   子网地址1   掩码长度1   优先级1   子网地址2   掩码长度2   优先级2   子网地址3   掩码长度3   优先级3   子网地址4   掩码长度4   优先级4   子网地址5   掩码长度5   优先级5   子网地址6   掩码长度6   优先级6   子网地址7   掩码长度7   优先级7   子网地址8   掩码长度8   优先级8   子网地址9   掩码长度9   优先级9   子网地址10   掩码长度10   优先级10
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org                              6.0.87.0    23          5         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0      0            0
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.063 秒）。
` 








父主题： [EPC APN优选子网段配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# GPRS APN更正配置 
# GPRS APN更正配置 


背景知识 


当用户接入分组网络时，请求消息中如果没有携带APN或携带的APN不合法（无效的格式，或格式有效但是没有对应的GGSN），网络不能解析出对应的GGSN地址，导致接入失败。 




功能描述 


用户没有携带APN或者携带的APN不合法时，SGSN根据APN更正配置的策略更正为其他APN，用户使用更正后的APN激活PDP上下文访问数据业务和其他业务。 


GRPS形式的APN更正包括5种方式：“指定APN”、“更正为签约的第一个APN”、“APN模糊匹配”、“请求APN更正”和“首个APN签约wildcard时指定APN”。 


APN更正功能的配置流程如下： 







                        配置APN更正策略，命令为：
                        [SET APNMOD POLICY]
                        。
                    







                        配置APN控制更正策略，命令为：
                        [ADD APNCTRLMOD POLICY]
                        。
                    







                        配置基于IMSI号段的APN更正，命令为：
                        [ADD APN MODIFICATION]
                        。
                    








相关主题 



 

设置APN更正策略(SET APNMOD POLICY)
 

 

查询APN更正策略(SHOW APNMOD POLICY)
 

 

新增APN控制更正策略配置(ADD APNCTRLMOD POLICY)
 

 

修改APN控制更正策略配置(SET APNCTRLMOD POLICY)
 

 

删除APN控制更正策略配置(DEL APNCTRLMOD POLICY)
 

 

查询APN控制更正策略配置(SHOW APNCTRLMOD POLICY)
 

 

新增APN更正配置(ADD APN MODIFICATION)
 

 

修改APN更正配置(SET APN MODIFICATION)
 

 

删除APN更正配置(DEL APN MODIFICATION)
 

 

查询APN更正配置(SHOW APN MODIFICATION)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置APN更正策略(SET APNMOD POLICY) 
## 设置APN更正策略(SET APNMOD POLICY) 


命令功能 


该命令用于设置SGSN的APN更正策略，可以设置SGSN是否支持APN更正。 


当设置SGSN支持APN更正时，可以设置是否支持APN控制更正策略。 


当设置支持APN控制更正策略时，可以继续设置APN默认控制策略，以及APN控制不更正时的PDP激活拒绝原因值。 


APN更正功能是指，当UE发起的Activate PDP Context Request（激活请求）消息中没有携带APN或携带的APN不合法时，SGSN无法解析出正确的GGSN，导致接入失败。为了避免这种情况，SGSN支持对原来APN进行更正，以便获取GGSN的IP地址。 


APN控制更正策略是指，当SGSN支持APN更正的时候，可以根据APN控制是否进行更正。 




注意事项 


此功能只适用于SGSN。 


当“支持APN更正”设为“支持”，并且需要基于APN控制更正策略时，才需要配置 “支持APN控制更正策略”为“支持”；否则，“支持APN控制更正策略”默认配置为“不支持”。 


当“支持APN控制更正策略”设为“支持”时，才需要配置“APN默认控制策略”。 


当“支持APN控制更正策略”设为“支持”，且APN控制的更正策略为“不更正”时，SGSN发送的PDP激活拒绝消息中的原因值，才使用“APN控制不更正时PDP激活拒绝原因值”参数的配置值。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNMODIFY|支持APN更正|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置为“支持”：表示SGSN支持APN更正功能。设置为“不支持”：表示SGSN不支持APN更正功能。
SUPAPNCTLMODPLY|支持APN控制更正策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持基于APN控制更正策略。
APNDFTCTLPLY|APN默认控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于APN控制的默认更正策略。
PDPREJCAUSEVALUE|APN控制不更正时PDP激活拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当基于APN控制的更正策略为“不更正”时，该参数用于设置PDP激活拒绝消息中携带的原因值。






命令举例 


设置APN更正策略。 


SET APNMOD POLICY:APNMODIFY="YES"; 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询APN更正策略(SHOW APNMOD POLICY) 
## 查询APN更正策略(SHOW APNMOD POLICY) 


命令功能 

该命令用于查询SGSN的APN更正策略。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNMODIFY|支持APN更正|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置为“支持”：表示SGSN支持APN更正功能。设置为“不支持”：表示SGSN不支持APN更正功能。
SUPAPNCTLMODPLY|支持APN控制更正策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持基于APN控制更正策略。
APNDFTCTLPLY|APN默认控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于APN控制的默认更正策略。
PDPREJCAUSEVALUE|APN控制不更正时PDP激活拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当基于APN控制的更正策略为“不更正”时，该参数用于设置PDP激活拒绝消息中携带的原因值。






命令举例 


查询APN更正策略。 


SHOW APNMOD POLICY; 


`

命令 (No.1): SHOW APNMOD POLICY

操作维护  支持APN更正   支持APN控制更正策略   APN默认控制策略   APN控制不更正时PDP激活拒绝原因值
------------------------------------------------------------------------------------------------
修改      不支持        不支持                更正              requested service option not subscribed
------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.022 秒）。
` 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增APN控制更正策略配置(ADD APNCTRLMOD POLICY) 
## 新增APN控制更正策略配置(ADD APNCTRLMOD POLICY) 


命令功能 


该命令用于设置APN控制的更正策略。当需要基于特定的APN配置更正策略时，使用该命令。 




注意事项 

当[SET APNMOD POLICY]命令中的“支持APN更正”设为“支持”， “支持APN控制更正策略”设为“支持”，且特定APN的更正策略与[SET APNMOD POLICY]命令中的“APN默认控制策略”不一致时，才需要使用[ADD APNCTRLMOD POLICY]命令。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数用于设置APN NI（Network Identifier），格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过63个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNMODPLY|APN更正策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN控制的更正策略。






命令举例 


新增APN控制更正策略配置，其中APN为"zte"、APN更正策略为更正。 


ADD APNCTRLMOD POLICY:APN="zte",APNMODPLY="MODIFY"; 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改APN控制更正策略配置(SET APNCTRLMOD POLICY) 
## 修改APN控制更正策略配置(SET APNCTRLMOD POLICY) 


命令功能 


该命令用于修改APN控制更正策略。当需要修改基于APN控制的更正策略时，使用该命令。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数用于设置APN NI（Network Identifier），格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过63个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNMODPLY|APN更正策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN控制的更正策略。






命令举例 


修改APN为"zte"的APN控制更正策略，将APN更正策略修改为更正。 


SET APNCTRLMOD POLICY:APN="zte",APNMODPLY="MODIFY"; 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除APN控制更正策略配置(DEL APNCTRLMOD POLICY) 
## 删除APN控制更正策略配置(DEL APNCTRLMOD POLICY) 


命令功能 


该命令用于删除基于特定APN的控制更正策略。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数用于设置APN NI（Network Identifier），格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过63个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






命令举例 


删除APN为"zte"的APN控制更正策略。 


DEL APNCTRLMOD POLICY:APN="zte"; 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询APN控制更正策略配置(SHOW APNCTRLMOD POLICY) 
## 查询APN控制更正策略配置(SHOW APNCTRLMOD POLICY) 


命令功能 


该命令用于查询基于APN的控制更正策略。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数用于设置APN NI（Network Identifier），格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过63个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置APN NI（Network Identifier），格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过63个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNMODPLY|APN更正策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN控制的更正策略。






命令举例 


查询APN控制更正策略。 


SHOW APNCTRLMOD POLICY; 


`

命令 (No.1): SHOW APNCTRLMOD POLICY

操作维护         APN名称   APN更正策略
--------------------------------------
复制 修改 删除   zte       更正
--------------------------------------
记录数 1

命令执行成功（耗时 0.023 秒）。
` 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增APN更正配置(ADD APN MODIFICATION) 
## 新增APN更正配置(ADD APN MODIFICATION) 


命令功能 

此命令用于SGSN根据MS的IMSI号段来对不能正确解析的APN的NI部分进行修改，以便SGSN能够根据修改后的APN获取到GGSN的IP地址。


注意事项 


此功能只适用于SGSN。 


此命令的执行前提是，通过[SET APNMOD SPRT]命令，设置SGSN支持APN更正功能。




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
MODIFYMODE|更正APN方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:First APN Signed by HLR。|表示对APN进行更正的方式，包括以下4种：指定APN：“指定APN”表示使用ADD APN MODIFICATION命令配置的参数“APN”，设置为该选项，表示使用“指定APN”对原APN进行更正。该选项受软件参数“指定APN更正是否需要检查HLR签约信息”（ID为786483）的控制，如果此软件参数设置为“1”，SGSN在更正前，需要检查“指定APN”是否为MS在HLR中签约的APN，如果确为签约的APN，则将更正为指定APN”，如果不是HLR中签约的APN，则会导致PDP激活流程失败。如果此软件参数设置为“0”，SGSN直接使用“指定APN”对原APN进行更正。HLR签约的第一个APN：表示SGSN使用MS的HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。APN模糊匹配：SGSN首先检查“指定APN”是否为HLR签约APN，如果是，则将原APN更正为“指定APN”；如果不是，则使用HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。请求APN更正：表示SGSN首先检查用户请求的APN（即原APN）是否为HLR的签约APN。如果是，则使用该用户请求的APN，如果不是，则使用HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。
APN|APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为更正后的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
PDPTYPE|PDP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:IPv4。|表示PDP的类型，包括“IPv4”、“IPv6”、“IPv4v6”和“PPP”类型。
OPTION|是否检查APN签约有wildcard|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|是否检查用户签约的APN中包含有wildcard。0：不检查，SGSN执行APN更正。1：检查，SGSN检查用户签约的APN中有wildcard则进行APN更正，没有wildcard则不执行APN更正，PDP激活失败。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


新增APN更正配置，IMSI前缀为46001，更正APN方式为APN模糊匹配，APN名称为zte，PDP类型为IPv4。 


ADD APN MODIFICATION:IMSI="46001",MODIFYMODE="APN Fuzzy Match",APN="zte"; 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改APN更正配置(SET APN MODIFICATION) 
## 修改APN更正配置(SET APN MODIFICATION) 


命令功能 

该命令用于根据MS的IMSI号段来修改APN更正配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
MODIFYMODE|更正APN方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对APN进行更正的方式，包括以下4种：指定APN：“指定APN”表示使用ADD APN MODIFICATION命令配置的参数“APN”，设置为该选项，表示使用“指定APN”对原APN进行更正。该选项受软件参数“指定APN更正是否需要检查HLR签约信息”（ID为786483）的控制，如果此软件参数设置为“1”，SGSN在更正前，需要检查“指定APN”是否为MS在HLR中签约的APN，如果确为签约的APN，则将更正为指定APN”，如果不是HLR中签约的APN，则会导致PDP激活流程失败。如果此软件参数设置为“0”，SGSN直接使用“指定APN”对原APN进行更正。HLR签约的第一个APN：表示SGSN使用MS的HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。APN模糊匹配：SGSN首先检查“指定APN”是否为HLR签约APN，如果是，则将原APN更正为“指定APN”；如果不是，则使用HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。请求APN更正：表示SGSN首先检查用户请求的APN（即原APN）是否为HLR的签约APN。如果是，则使用该用户请求的APN，如果不是，则使用HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数为更正后的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
PDPTYPE|PDP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示PDP的类型，包括“IPv4”、“IPv6”、“IPv4v6”和“PPP”类型。
OPTION|是否检查APN签约有wildcard|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否检查用户签约的APN中包含有wildcard。0：不检查，SGSN执行APN更正。1：检查，SGSN检查用户签约的APN中有wildcard则进行APN更正，没有wildcard则不执行APN更正，PDP激活失败。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


修改IMSI前缀为46001的APN更正配置，更正APN方式为HLR签约的第一个APN。 


SET APN MODIFICATION:IMSI="46001",MODIFYMODE="First APN Signed by HLR"; 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除APN更正配置(DEL APN MODIFICATION) 
## 删除APN更正配置(DEL APN MODIFICATION) 


命令功能 

该命令用于根据MS的IMSI号段来删除APN更正配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






命令举例 


删除IMSI前缀为46001的APN更正配置。 


DEL APN MODIFICATION:IMSI="46001"; 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询APN更正配置(SHOW APN MODIFICATION) 
## 查询APN更正配置(SHOW APN MODIFICATION) 


命令功能 

该命令用于查询APN更正配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
MODIFYMODE|更正APN方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对APN进行更正的方式，包括以下4种：指定APN：“指定APN”表示使用ADD APN MODIFICATION命令配置的参数“APN”，设置为该选项，表示使用“指定APN”对原APN进行更正。该选项受软件参数“指定APN更正是否需要检查HLR签约信息”（ID为786483）的控制，如果此软件参数设置为“1”，SGSN在更正前，需要检查“指定APN”是否为MS在HLR中签约的APN，如果确为签约的APN，则将更正为指定APN”，如果不是HLR中签约的APN，则会导致PDP激活流程失败。如果此软件参数设置为“0”，SGSN直接使用“指定APN”对原APN进行更正。HLR签约的第一个APN：表示SGSN使用MS的HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。APN模糊匹配：SGSN首先检查“指定APN”是否为HLR签约APN，如果是，则将原APN更正为“指定APN”；如果不是，则使用HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。请求APN更正：表示SGSN首先检查用户请求的APN（即原APN）是否为HLR的签约APN。如果是，则使用该用户请求的APN，如果不是，则使用HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数为更正后的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
MODIFYMODE|更正APN方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示对APN进行更正的方式，包括以下4种：指定APN：“指定APN”表示使用ADD APN MODIFICATION命令配置的参数“APN”，设置为该选项，表示使用“指定APN”对原APN进行更正。该选项受软件参数“指定APN更正是否需要检查HLR签约信息”（ID为786483）的控制，如果此软件参数设置为“1”，SGSN在更正前，需要检查“指定APN”是否为MS在HLR中签约的APN，如果确为签约的APN，则将更正为指定APN”，如果不是HLR中签约的APN，则会导致PDP激活流程失败。如果此软件参数设置为“0”，SGSN直接使用“指定APN”对原APN进行更正。HLR签约的第一个APN：表示SGSN使用MS的HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。APN模糊匹配：SGSN首先检查“指定APN”是否为HLR签约APN，如果是，则将原APN更正为“指定APN”；如果不是，则使用HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。请求APN更正：表示SGSN首先检查用户请求的APN（即原APN）是否为HLR的签约APN。如果是，则使用该用户请求的APN，如果不是，则使用HLR签约信息中的第一个APN做为更正后APN，如果签约的第一个APN为“*”，则使用“指定APN”（即通过ADD APN MODIFICATION命令配置的参数“APN”）做为更正后的APN。
APN|APN|参数可选性:任选参数；参数类型:字符型。|该参数为更正后的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
PDPTYPE|PDP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示PDP的类型，包括“IPv4”、“IPv6”、“IPv4v6”和“PPP”类型。
OPTION|是否检查APN签约有wildcard|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否检查用户签约的APN中包含有wildcard。0：不检查，SGSN执行APN更正。1：检查，SGSN检查用户签约的APN中有wildcard则进行APN更正，没有wildcard则不执行APN更正，PDP激活失败。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


查询APN更正配置。 


SHOW APN MODIFICATION; 


`

命令 (No.1): SHOW APN MODIFICATION

操作维护         IMSI    更正APN方式          APN   PDP类型   用户别名
----------------------------------------------------------------------
复制 修改 删除   46001   APN模糊匹配          zte   IPv4      
----------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.035 秒）。
` 








父主题： [GPRS APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# EPC APN更正配置 
# EPC APN更正配置 


背景知识 


当用户接入分组网络时，请求消息中如果没有携带APN或携带的APN不合法（无效的格式，或格式有效但是没有对应的PGW），网络不能解析出对应的PGW地址，导致接入失败。 




功能描述 


用户没有携带APN或者携带的APN不合法时，MME根据APN更正配置的策略更正为其他APN，用户使用更正后的APN激活EPS承载上下文访问数据业务和其他业务。 


EPC形式的APN更正包括2种方式：“指定APN”和“HSS签约的默认APN”。 


APN更正功能的配置流程如下： 







                        配置本局是否支持APN更正功能，命令为：
                        [SET MME APNMOD POLICY]
                        。
                    







                        配置基于IMSI号段的APN更正，命令为：
                        [ADD MME APN MODIFICATION]
                        。
                    








相关主题 



 

设置EPC APN更正策略(SET MME APNMOD POLICY)
 

 

查询EPC APN更正策略(SHOW MME APNMOD POLICY)
 

 

新增EPC APN控制更正策略配置(ADD MME APN MODIFY POLICY)
 

 

修改EPC APN控制更正策略配置(SET MME APN MODIFY POLICY)
 

 

删除EPC APN控制更正策略配置(DEL MME APN MODIFY POLICY)
 

 

查询EPC APN控制更正策略配置(SHOW MME APN MODIFY POLICY)
 

 

新增EPC APN更正配置(ADD MME APN MODIFICATION)
 

 

修改EPC APN更正配置(SET MME APN MODIFICATION)
 

 

删除EPC APN更正配置(DEL MME APN MODIFICATION)
 

 

查询EPC APN更正配置(SHOW MME APN MODIFICATION)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置EPC APN更正策略(SET MME APNMOD POLICY) 
## 设置EPC APN更正策略(SET MME APNMOD POLICY) 


命令功能 


该命令用于设置本局是否支持EPC APN更正功能, 和更正APN方式为“指定APN（Specified APN）”时，MME是否需要检查用户是否签约了指定的APN。 


本局开启支持EPC APN更正功能后，如果用户在LTE网络激活时消息中没有携带APN或携带的APN不合法时，MME无法解析出正确的PGW，导致接入失败。为了避免这种情况，MME支持对原来APN进行更正，以便获取PGW的IP地址。 




注意事项 



 
设置本局支持EPC APN更正功能后，必须要存在EPC APN更正配置，才能对原来APN进行更正，使用更正后的APN进行PGW地址查询。 
 

 
如果本局是Combo局，该功能仅影响LTE网络的用户，对其他网络的用户不会产生影响。 
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNMODIFY|是否支持APN更正功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局是否支持EPC APN更正功能。取值含义：“不支持（No）”：本局不支持EPC APN更正功能。“支持（Yes）：本局支持EPC APN更正功能。
SPECAPNCHKSUB|指定APN更正时检查签约|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置更正APN方式为“指定APN（Specified APN）”时，MME是否需要检查用户是否签约了指定的APN，如果未签约，则MME拒绝该用户接入；如果签约，则MME使用指定的APN。取值含义：No：不检查Yes：检查
SUPEAPNCTLMODPLY|支持APN控制更正策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持APN控制更正策略。0-不支持。1-支持。
EAPNDFTCTLPLY|APN默认控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN控制的默认更正策略。0-不更正。1-更正。






命令举例 


设置EPC APN更正策略。 


SET MME APNMOD POLICY:APNMODIFY="YES"; 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询EPC APN更正策略(SHOW MME APNMOD POLICY) 
## 查询EPC APN更正策略(SHOW MME APNMOD POLICY) 


命令功能 

该命令用于查询本局是否支持EPC APN更正功能. 和更正APN方式为“指定APN（Specified APN）”时，MME是否需要检查用户是否签约了指定的APN。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNMODIFY|是否支持APN更正功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局是否支持EPC APN更正功能。取值含义：“不支持（No）”：本局不支持EPC APN更正功能。“支持（Yes）：本局支持EPC APN更正功能。
SPECAPNCHKSUB|指定APN更正时检查签约|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置更正APN方式为“指定APN（Specified APN）”时，MME是否需要检查用户是否签约了指定的APN，如果未签约，则MME拒绝该用户接入；如果签约，则MME使用指定的APN。取值含义：No：不检查Yes：检查
SUPEAPNCTLMODPLY|支持APN控制更正策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持APN控制更正策略。0-不支持。1-支持。
EAPNDFTCTLPLY|APN默认控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN控制的默认更正策略。0-不更正。1-更正。






命令举例 


查询EPC APN更正策略。 


SHOW MME APNMOD POLICY; 


`

命令 (No.1):SHOW MME APNMOD POLICY

操作维护  是否支持APN更正功能  指定APN更正时检查签约  支持APN控制更正策略  APN默认控制策略 
------------------------------------------------------------------------------------------
修改      不支持               不检查                 不支持               更正 
------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.044 秒）。
` 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增EPC APN控制更正策略配置(ADD MME APN MODIFY POLICY) 
## 新增EPC APN控制更正策略配置(ADD MME APN MODIFY POLICY) 


命令功能 


该命令用于设置EPC APN控制的更正策略。当需要基于特定的EPC APN配置更正策略时，使用该命令。 




注意事项 

当“支持APN更正”设为“支持”， “支持APN控制更正策略”设为“支持”，且特定APN的更正策略与“APN默认控制策略”不一致时，才需要配置“新增EPC APN控制更正策略配置”。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNMODPLY|APN更正策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN控制的更正策略。






命令举例 


新增EPC APN控制更正策略配置，其中APN名称为"zte"、APN更正策略为不更正。 


ADD MME APN MODIFY POLICY:APN="zte",APNMODPLY="NOTMODIFY"; 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改EPC APN控制更正策略配置(SET MME APN MODIFY POLICY) 
## 修改EPC APN控制更正策略配置(SET MME APN MODIFY POLICY) 


命令功能 


该命令用于修改EPC APN控制更正策略。当需要修改基于EPC APN控制的更正策略时，使用该命令。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNMODPLY|APN更正策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN控制的更正策略。






命令举例 


修改APN名称为"zte"的EPC APN控制更正策略配置，将APN更正策略修改为更正。 


SET MME APN MODIFY POLICY:APN="zte",APNMODPLY="MODIFY"; 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除EPC APN控制更正策略配置(DEL MME APN MODIFY POLICY) 
## 删除EPC APN控制更正策略配置(DEL MME APN MODIFY POLICY) 


命令功能 


该命令用于删除EPC APN控制更正策略。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






命令举例 


删除APN名称为"zte"的EPC APN控制更正策略配置。 


DEL MME APN MODIFY POLICY:APN="zte"; 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询EPC APN控制更正策略配置(SHOW MME APN MODIFY POLICY) 
## 查询EPC APN控制更正策略配置(SHOW MME APN MODIFY POLICY) 


命令功能 


该命令用于查询EPC APN控制更正策略。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
APNMODPLY|APN更正策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN控制的更正策略。






命令举例 


查询EPC APN控制更正策略配置。 


SHOW MME APN MODIFY POLICY; 


`
命令 (No.1): SHOW MME APN MODIFY POLICY

操作维护         APN名称  APN更正策略 
--------------------------------------
复制 修改 删除   zte      更正 
--------------------------------------
记录数 1

命令执行成功（耗时 0.052 秒）。
` 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增EPC APN更正配置(ADD MME APN MODIFICATION) 
## 新增EPC APN更正配置(ADD MME APN MODIFICATION) 


命令功能 

该命令用于MME根据MS的IMSI号段来对不能正确解析的APN的NI部分进行修改，以便MME能够根据修改后的APN获取到PGW的IP地址。


注意事项 


此功能只适用于MME。 


此命令的执行前提是，通过[SET MME APNMOD SPRT]命令，设置MME支持APN更正功能。




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
SUBWILDCHK|用户是否签约通配|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|如果在同一个号段内的用户，签约通配的用户和没有签约通配的用户使用不同的APN更正方式，则此参数需要分别设置为签约通配和没有签约通配；否则此参数设置为忽略。
MODIFYMODE|更正APN方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局支持EPC APN更正功能的APN更正方式。取值含义：“指定APN（Specified APN）”：设置为“指定APN”方式时，必须设置更正后的APN。IMSI用户在LTE网络激活时，请求消息中没有携带APN或携带的APN不合法时，MME支持对原来APN进行更正，用更正后的APN进行PGW地址查询。“HSS签约的默认APN（Default APN Signed by HSS）”：IMSI用户在LTE网络激活时，请求消息中没有携带APN或携带的APN不合法时，用HSS签约的默认APN进行PGW地址查询。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数为更正后的APN。该参数仅在更正APN方式为“指定APN（Specified APN）”时才有效。该参数为完整APN格式中的Network Identifier（NI）部分，不包括Operator Identifier（OI）部分。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符，不区分大小写。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
NIPAPN|Non-IP PDN类型的APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数为用户请求Non-IP类型的PDN时更正后的APN。该参数仅在更正APN方式为“指定APN（Specified APN）”时才有效，即通过命令ADD MME APN MODIFICATION将参数“更正APN方式（APN Modification Mode）”设置为“指定APN（Specified APN）。该参数为完整APN格式中的Network Identifier（NI）部分，不包括Operator Identifier（OI）部分。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符，不区分大小写。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数为EPC APN更正配置的别名，用于区分不同的EPC APN更正配置。






命令举例 


新增IMSI号段前缀为“46002”的EPC APN更正配置，用户是否签约通配为更正方式为“忽略”,“HSS签约的默认APN”，用户别名为“gg”。 


ADD MME APN MODIFICATION:IMSI="46002",SUBWILDCHK="IGNORE",MODIFYMODE="Default APN Signed by HSS",NAME="gg"; 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改EPC APN更正配置(SET MME APN MODIFICATION) 
## 修改EPC APN更正配置(SET MME APN MODIFICATION) 


命令功能 

该命令用于根据MS的IMSI号段来修改APN更正配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
SUBWILDCHK|用户是否签约通配|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|如果在同一个号段内的用户，签约通配的用户和没有签约通配的用户使用不同的APN更正方式，则此参数需要分别设置为签约通配和没有签约通配；否则此参数设置为忽略。
MODIFYMODE|更正APN方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局支持EPC APN更正功能的APN更正方式。取值含义：“指定APN（Specified APN）”：设置为“指定APN”方式时，必须设置更正后的APN。IMSI用户在LTE网络激活时，请求消息中没有携带APN或携带的APN不合法时，MME支持对原来APN进行更正，用更正后的APN进行PGW地址查询。“HSS签约的默认APN（Default APN Signed by HSS）”：IMSI用户在LTE网络激活时，请求消息中没有携带APN或携带的APN不合法时，用HSS签约的默认APN进行PGW地址查询。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数为更正后的APN。该参数仅在更正APN方式为“指定APN（Specified APN）”时才有效。该参数为完整APN格式中的Network Identifier（NI）部分，不包括Operator Identifier（OI）部分。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符，不区分大小写。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
NEWSUBWILDCHK|新的用户签约通配方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为参数“用户是否签约通配”的修改值，此参数取值为签约通配或没有签约通配；否则此参数设置为忽略。
NIPAPN|Non-IP PDN类型的APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数为用户请求Non-IP类型的PDN时更正后的APN。该参数仅在更正APN方式为“指定APN（Specified APN）”时才有效，即通过命令ADD MME APN MODIFICATION将参数“更正APN方式（APN Modification Mode）”设置为“指定APN（Specified APN）。该参数为完整APN格式中的Network Identifier（NI）部分，不包括Operator Identifier（OI）部分。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符，不区分大小写。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数为EPC APN更正配置的别名，用于区分不同的EPC APN更正配置。






命令举例 


修改IMSI号段前缀为“46002”,用户是否签约通配为更正方式为“忽略”的EPC APN更正配置，更正方式为“指定APN”，指定的APN名称为“zte.com”。 


SET MME APN MODIFICATION:IMSI="46002",SUBWILDCHK="IGNORE",MODIFYMODE="Specified APN",APN="zte.com"; 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除EPC APN更正配置(DEL MME APN MODIFICATION) 
## 删除EPC APN更正配置(DEL MME APN MODIFICATION) 


命令功能 

该命令用于根据MS的IMSI号段来删除APN更正配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
SUBWILDCHK|用户是否签约通配|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|如果在同一个号段内的用户，签约通配的用户和没有签约通配的用户使用不同的APN更正方式，则此参数需要分别设置为签约通配和没有签约通配；否则此参数设置为忽略。






命令举例 


删除IMSI号段前缀为“46002”,用户是否签约通配为更正方式为“忽略”的EPC APN更正配置。 


DEL MME APN MODIFICATION:IMSI="46002",SUBWILDCHK="IGNORE"; 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询EPC APN更正配置(SHOW MME APN MODIFICATION) 
## 查询EPC APN更正配置(SHOW MME APN MODIFICATION) 


命令功能 

该命令用于查询APN更正配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
SUBWILDCHK|用户是否签约通配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果在同一个号段内的用户，签约通配的用户和没有签约通配的用户使用不同的APN更正方式，则此参数需要分别设置为签约通配和没有签约通配；否则此参数设置为忽略。
MODIFYMODE|更正APN方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局支持EPC APN更正功能的APN更正方式。取值含义：“指定APN（Specified APN）”：设置为“指定APN”方式时，必须设置更正后的APN。IMSI用户在LTE网络激活时，请求消息中没有携带APN或携带的APN不合法时，MME支持对原来APN进行更正，用更正后的APN进行PGW地址查询。“HSS签约的默认APN（Default APN Signed by HSS）”：IMSI用户在LTE网络激活时，请求消息中没有携带APN或携带的APN不合法时，用HSS签约的默认APN进行PGW地址查询。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数为更正后的APN。该参数仅在更正APN方式为“指定APN（Specified APN）”时才有效。该参数为完整APN格式中的Network Identifier（NI）部分，不包括Operator Identifier（OI）部分。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符，不区分大小写。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
NIPAPN|Non-IP PDN类型的APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数为用户请求Non-IP类型的PDN时更正后的APN。该参数仅在更正APN方式为“指定APN（Specified APN）”时才有效，即通过命令ADD MME APN MODIFICATION将参数“更正APN方式（APN Modification Mode）”设置为“指定APN（Specified APN）。该参数为完整APN格式中的Network Identifier（NI）部分，不包括Operator Identifier（OI）部分。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符，不区分大小写。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
SUBWILDCHK|用户是否签约通配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果在同一个号段内的用户，签约通配的用户和没有签约通配的用户使用不同的APN更正方式，则此参数需要分别设置为签约通配和没有签约通配；否则此参数设置为忽略。
MODIFYMODE|更正APN方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局支持EPC APN更正功能的APN更正方式。取值含义：“指定APN（Specified APN）”：设置为“指定APN”方式时，必须设置更正后的APN。IMSI用户在LTE网络激活时，请求消息中没有携带APN或携带的APN不合法时，MME支持对原来APN进行更正，用更正后的APN进行PGW地址查询。“HSS签约的默认APN（Default APN Signed by HSS）”：IMSI用户在LTE网络激活时，请求消息中没有携带APN或携带的APN不合法时，用HSS签约的默认APN进行PGW地址查询。
APN|APN|参数可选性:任选参数；参数类型:字符型。|该参数为更正后的APN。该参数仅在更正APN方式为“指定APN（Specified APN）”时才有效。该参数为完整APN格式中的Network Identifier（NI）部分，不包括Operator Identifier（OI）部分。NI部分格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符，不区分大小写。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
NIPAPN|Non-IP PDN类型的APN|参数可选性:任选参数；参数类型:字符型。|该参数为用户请求Non-IP类型的PDN时更正后的APN。该参数仅在更正APN方式为“指定APN（Specified APN）”时才有效，即通过命令ADD MME APN MODIFICATION将参数“更正APN方式（APN Modification Mode）”设置为“指定APN（Specified APN）。该参数为完整APN格式中的Network Identifier（NI）部分，不包括Operator Identifier（OI）部分。NI部分格式为“Label1Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过61个字符，不区分大小写。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数为EPC APN更正配置的别名，用于区分不同的EPC APN更正配置。






命令举例 


查询全部的EPC APN更正配置。 


SHOW MME APN MODIFICATION; 


`

命令 (No.1): SHOW MME APN MODIFICATION

操作维护         IMSI    用户是否签约通配   更正APN方式        APN   Non-IP PDN类型的APN   用户别名
---------------------------------------------------------------------------------------------------
复制 修改 删除   46002   忽略               HSS签约的默认APN         zte.com               gg
---------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.022 秒）。
` 








父主题： [EPC APN更正配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# EPC APN选择控制配置 
# EPC APN选择控制配置 


背景知识 


用户发起附着和PDN连接流程时，进行APN选择。某些运营商要求，用户请求的APN、PDN类型与HSS签约信息匹配时，忽略签约通配。当请求的APN、PDN类型与HSS签约信息中的APN、PDN类型匹配时，才允许用户接入；不匹配时，拒绝用户接入。 


为了满足这种需求，MME提供EPC APN选择控制配置。当需要对请求的APN、PDN类型进行匹配控制时，使用本配置。 




功能描述 


EPC APN选择控制配置包括： 



 

设置EPC APN选择控制策略。
 

 

缺省EPC APN选择控制配置。
 

 

针对特定的IMSI号段、APN进行EPC APN选择控制配置。
 

 




相关主题 



 

设置EPC APN选择控制策略(SET EPC APN SELECT CFG)
 

 

查询EPC APN选择控制策略(SHOW EPC APN SELECT CFG)
 

 

设置缺省EPC APN选择控制(SET DEF EPC APN SELCTRL)
 

 

查询缺省EPC APN选择控制(SHOW DEF EPC APN SELCTRL)
 

 

新增EPC APN选择控制配置(ADD EPC APN SEL CTRL)
 

 

修改EPC APN选择控制配置(SET EPC APN SEL CTRL)
 

 

删除EPC APN选择控制配置(DEL EPC APN SEL CTRL)
 

 

查询EPC APN选择控制配置(SHOW EPC APN SEL CTRL)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置EPC APN选择控制策略(SET EPC APN SELECT CFG) 
## 设置EPC APN选择控制策略(SET EPC APN SELECT CFG) 


命令功能 


该命令用于设置EPC APN选择控制策略。当需要设置MME是否支持APN选择控制时，使用该命令。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
SUPAPNSELCTL|支持APN选择控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持APN选择控制。0-不支持1-支持






命令举例 


设置EPC APN选择控制策略，将支持APN选择控制修改为支持。 


SET EPC APN SELECT CFG:SUPAPNSELCTL="YES"; 








父主题： [EPC APN选择控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询EPC APN选择控制策略(SHOW EPC APN SELECT CFG) 
## 查询EPC APN选择控制策略(SHOW EPC APN SELECT CFG) 


命令功能 


该命令用于查询EPC APN选择控制策略。 




注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
SUPAPNSELCTL|支持APN选择控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持APN选择控制。0-不支持1-支持






命令举例 


查询EPC APN选择控制策略。 


SHOW EPC APN SELECT CFG; 


`
命令 (No.1): SHOW EPC APN SELECT CFG

操作维护 支持APN选择控制 
-------------------------
修改     支持 
-------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [EPC APN选择控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置缺省EPC APN选择控制(SET DEF EPC APN SELCTRL) 
## 设置缺省EPC APN选择控制(SET DEF EPC APN SELCTRL) 


命令功能 


该命令用于设置缺省EPC APN选择控制。当MME支持APN选择控制的时候，需要配置是否忽略签约通配时，使用该命令。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IGNWILDCARD|忽略签约通配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN选择控制时是否忽略签约通配。0-不忽略1-忽略
ATTAREJCAU|附着拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|APN选择，签约通配，且通配的PDN类型与请求的PDN类型一致，当配置为忽略签约通配，导致APN选择失败，附着拒绝时，该参数用于设置附着拒绝原因值。
PDNCONREJCAU|PDN连接拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|APN选择，签约通配，且通配的PDN类型与请求的PDN类型一致，当配置为忽略签约通配，导致APN选择失败，附着和PDN连接拒绝时，该参数用于设置PDN连接拒绝原因值。






命令举例 


设置缺省EPC APN选择控制,将忽略签约通配修改忽略，附着拒绝原因修改为Illegal UE，PDN连接拒绝原因修改为operator determined barring。 


SET DEF EPC APN SELCTRL:IGNWILDCARD="YES",ATTAREJCAU="ATTAREJCAU_3",PDNCONREJCAU="PDNCONREJCAU_8"; 








父主题： [EPC APN选择控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询缺省EPC APN选择控制(SHOW DEF EPC APN SELCTRL) 
## 查询缺省EPC APN选择控制(SHOW DEF EPC APN SELCTRL) 


命令功能 


该命令用于查询缺省EPC APN选择控制配置。 




注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
IGNWILDCARD|忽略签约通配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN选择控制时是否忽略签约通配。0-不忽略1-忽略
ATTAREJCAU|附着拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|APN选择，签约通配，且通配的PDN类型与请求的PDN类型一致，当配置为忽略签约通配，导致APN选择失败，附着拒绝时，该参数用于设置附着拒绝原因值。
PDNCONREJCAU|PDN连接拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|APN选择，签约通配，且通配的PDN类型与请求的PDN类型一致，当配置为忽略签约通配，导致APN选择失败，附着和PDN连接拒绝时，该参数用于设置PDN连接拒绝原因值。






命令举例 


查询缺省EPC APN选择控制。 


SHOW DEF EPC APN SELCTRL; 


`
命令 (No.1): SHOW DEF EPC APN SELCTRL

操作维护  忽略签约通配  附着拒绝原因  PDN连接拒绝原因 
-----------------------------------------------------------------
修改      忽略          Illegal UE    operator determined barring  
-----------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.034 秒）。
` 








父主题： [EPC APN选择控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增EPC APN选择控制配置(ADD EPC APN SEL CTRL) 
## 新增EPC APN选择控制配置(ADD EPC APN SEL CTRL) 


命令功能 


该命令用于新增基于用户IMSI号段或APN NI或IMSI号段+APN NI的EPC APN选择控制配置。当APN选择需要根据特定IMSI号段、APN设置是否忽略签约通配时，使用该命令。 




注意事项 


基于IMSI号段、APN的APN选择控制，可以从3个维度进行控制，优先级从高到低顺序为：IMSI号段+APN NI、APN NI、IMSI号段。 




参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IGNWILDCARD|忽略签约通配|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN选择控制时是否忽略签约通配。0-不忽略1-忽略






命令举例 


新增EPC APN选择控制配置，其中IMSI为46001、APN为"zte"、忽略签约通配为不忽略。 


ADD EPC APN SEL CTRL:IMSI="46001",APN="zte",IGNWILDCARD="NO"; 








父主题： [EPC APN选择控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改EPC APN选择控制配置(SET EPC APN SEL CTRL) 
## 修改EPC APN选择控制配置(SET EPC APN SEL CTRL) 


命令功能 


该命令用于修改基于用户IMSI号段或APN NI或IMSI号段+APN NI的EPC APN选择控制配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IGNWILDCARD|忽略签约通配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN选择控制时是否忽略签约通配。0-不忽略1-忽略






命令举例 


修改EPC APN选择控制配置，将忽略签约通配改为忽略。 


SET EPC APN SEL CTRL:IMSI="46001",APN="zte",IGNWILDCARD="YES"; 








父主题： [EPC APN选择控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除EPC APN选择控制配置(DEL EPC APN SEL CTRL) 
## 删除EPC APN选择控制配置(DEL EPC APN SEL CTRL) 


命令功能 


该命令用于删除基于用户IMSI号段或APN NI或IMSI号段+APN NI的EPC APN选择控制配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






命令举例 


删除EPC APN选择控制配置。 


DEL EPC APN SEL CTRL:IMSI="46001",APN="zte"; 








父主题： [EPC APN选择控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询EPC APN选择控制配置(SHOW EPC APN SEL CTRL) 
## 查询EPC APN选择控制配置(SHOW EPC APN SEL CTRL) 


命令功能 


该命令用于查询基于用户IMSI号段或APN NI或IMSI号段+APN NI的EPC APN选择控制配置。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IGNWILDCARD|忽略签约通配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN选择控制时是否忽略签约通配。0-不忽略1-忽略






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于设置IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
IGNWILDCARD|忽略签约通配|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置APN选择控制时是否忽略签约通配。0-不忽略1-忽略






命令举例 


查询EPC APN选择控制配置。 


SHOW EPC APN SEL CTRL; 


`
命令 (No.1): SHOW EPC APN SEL CTRL

操作维护        IMSI   APN  忽略签约通配 
---------------------------------------
复制 修改 删除  46001  zte  忽略 
---------------------------------------
记录数 1

命令执行成功（耗时 0.072 秒）。
` 








父主题： [EPC APN选择控制配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# APN PDP IDLE时长配置 
# APN PDP IDLE时长配置 


背景知识 

            
            随着用户数量的增多，为了节省网络资源，可以对不活跃用户去激活。
        


功能描述 

            
            该配置支持基于GPRS/EPC APN NI的PDP空闲时长配置。SGSN对PDP空闲时长大于等于该配置时长的用户，基于APN执行去激活。
        


相关主题 



 

新增APN PDP IDLE时长配置(ADD APN IDLE TIME)
 

 

修改APN PDP IDLE时长配置(SET APN IDLE TIME)
 

 

删除APN PDP IDLE时长配置(DEL APN IDLE TIME)
 

 

查询APN PDP IDLE时长配置(SHOW APN IDLE TIME)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增APN PDP IDLE时长配置(ADD APN IDLE TIME) 
## 新增APN PDP IDLE时长配置(ADD APN IDLE TIME) 


命令功能 


该命令用于配置某个APN下PDP空闲的MS的超时时长。 


当此类用户的PDP空闲时长超过本命令配置的数值时，SGSN会对此类用户进行去激活操作。 




注意事项 


此功能只适用于SGSN网元。 


默认值为60分钟。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为用户接入的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN/PGW；另一方面，APN标识了通过该GGSN/PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN/PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN/PGW所在的分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
IDLETIME|IDLE时长(分)|参数可选性:必选参数；参数类型:整数；参数范围为:1~14400。默认值:60。|表示接入某个APN下PDP空闲的MS的超时时长，当此类用户的PDP空闲时长超过本命令配置的数值时，SGSN会对此类用户进行去激活操作。默认值为60分钟。






命令举例 


新增APN PDP IDLE时长配置，APN名称为test.apn，IDLE时长为60分钟。 


ADD APN IDLE TIME:APN="test.apn",IDLETIME=60; 








父主题： [APN PDP IDLE时长配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改APN PDP IDLE时长配置(SET APN IDLE TIME) 
## 修改APN PDP IDLE时长配置(SET APN IDLE TIME) 


命令功能 

该命令用于修改某个APN下PDP空闲的MS的超时时长。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为用户接入的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN/PGW；另一方面，APN标识了通过该GGSN/PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN/PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN/PGW所在的分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
IDLETIME|IDLE时长(分)|参数可选性:必选参数；参数类型:整数；参数范围为:1~14400。|表示接入某个APN下PDP空闲的MS的超时时长，当此类用户的PDP空闲时长超过本命令配置的数值时，SGSN会对此类用户进行去激活操作。默认值为60分钟。






命令举例 


修改APN PDP IDLE时长配置，APN名称为test.apn，IDLE时长修改为57分钟。 


SET APN IDLE TIME:APN="test.apn",IDLETIME=57; 








父主题： [APN PDP IDLE时长配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除APN PDP IDLE时长配置(DEL APN IDLE TIME) 
## 删除APN PDP IDLE时长配置(DEL APN IDLE TIME) 


命令功能 


该命令用于删除某个APN下PDP空闲的MS的超时时长。 


该命令执行后，SGSN不再对该APN下的PDP空闲用户进行去活操作。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为用户接入的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN/PGW；另一方面，APN标识了通过该GGSN/PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN/PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN/PGW所在的分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。






命令举例 


删除名称为test.apn的APN PDP IDLE时长配置。 


DEL APN IDLE TIME:APN="test.apn"; 








父主题： [APN PDP IDLE时长配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询APN PDP IDLE时长配置(SHOW APN IDLE TIME) 
## 查询APN PDP IDLE时长配置(SHOW APN IDLE TIME) 


命令功能 

该命令用于根据APN来查询此APN下用户PDP空闲时长配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数为用户接入的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN/PGW；另一方面，APN标识了通过该GGSN/PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN/PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN/PGW所在的分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为用户接入的APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN/PGW；另一方面，APN标识了通过该GGSN/PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN/PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN/PGW所在的分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
IDLETIME|IDLE时长(分)|参数可选性:任选参数；参数类型:整数；参数范围为:1~14400。|表示接入某个APN下PDP空闲的MS的超时时长，当此类用户的PDP空闲时长超过本命令配置的数值时，SGSN会对此类用户进行去激活操作。默认值为60分钟。






命令举例 


查询APN PDP IDLE时长配置。 


SHOW APN IDLE TIME; 


`

命令 (No.1): SHOW APN IDLE TIME

操作维护         APN        IDLE时长(分)
----------------------------------------
复制 修改 删除   test.apn   60
----------------------------------------
记录数 1

命令执行成功（耗时 0.054 秒）。
` 








父主题： [APN PDP IDLE时长配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# LTE能力终端域名格式配置 
# LTE能力终端域名格式配置 


背景知识 



                APN有2种格式：GPRS APN 和EPC APN，对支持LTE能力的用户终端，SGSN使用LTE能力终端域名格式配置选择EPC APN格式或GPRS APN格式进行地址解析，如果SGSN选择EPC APN格式进行地址解析，则使用EPC APN HOST配置（
                [ADD EPC APN]
                ），如果SGSN选择GPRS APN格式进行地址解析，则使用GPRS APN HOST配置（
                [ADD GPRS APN]
                ）；对不支持LTE能力的用户终端，SGSN选择GPRS APN格式进行地址解析，使用GPRS APN HOST配置（
                [ADD GPRS APN]
                ）。
            




功能描述 


SGSN从HSS/HLR或UE获取到APN，对支持LTE能力的用户终端，根据LTE能力终端域名格式配置选择得到APN域名格式，根据EPC格式或GPRS APN格式的APN通过DNS或本地域名解析得到GGSN/PGW的IP地址。 


SGSN支持对整个网元配置LTE能力的用户终端使用的APN域名格式，也支持根据IMSI号段/IMEI号段配置LTE能力的用户终端使用的APN域名格式。配置项说明如下： 



 


                        对整个网元配置LTE能力的用户终端使用的APN域名格式，配置LTE能力域名格式为使用GPRS格式或使用EPC格式，配置命令为
                        SET EPC APN NAME CFG
                        。
                    
 

 

根据IMSI号段/IMEI号段配置LTE能力的用户终端使用的APN域名格式：
 

 


                        配置LTE能力域名格式为基于IMSI号段使用EPC格式或基于IMEI号段使用EPC格式，配置命令为
                        SET EPC APN NAME CFG
                        。
                    
 

 


                        配置支持EPC格式域名号段，配置命令为
                        ADD EPC NAME MSID SEG
                        。
                    
 

 




相关主题 



 

设置LTE能力域名格式(SET EPC APN NAME CFG)
 

 

查询LTE能力域名格式(SHOW EPC APN NAME CFG)
 

 

新增支持EPC格式域名号段(ADD EPC NAME MSID SEG)
 

 

删除支持EPC格式域名号段(DEL EPC NAME MSID SEG)
 

 

查询支持EPC格式域名号段(SHOW EPC NAME MSID SEG)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置LTE能力域名格式(SET EPC APN NAME CFG) 
## 设置LTE能力域名格式(SET EPC APN NAME CFG) 


命令功能 

该命令用于修改本局的LTE能力终端域名格式。当需要修改本局的LTE能力终端域名格式时，使用该命令。修改本局的LTE能力终端域名格式成功后，本局用户在与其他网元进行控制面信令交互时，信令中携带的APN可变成形式为：
“xxx.yyy.gprs”的GPRS APN格式，或者“xxx.yyy.3gppnetwork.org”的EPC APN的格式。


注意事项 



 
开局后，本局默认的LTE能力终端域名格式为GPRS格式。 
 

 
如果设置的LTE能力终端域名格式为按用户号段支持EPC格式，必须要配置用于支持EPC格式域名的号段。 
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNFORMAT|APN域名格式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:GPRS format。|该参数用于设置本局的LTE能力终端域名格式。 取值含义：“使用GPRS格式（GRPS format）”：本局所有用户给其他网元发送的APN将变成形式为“xxx.yyy.gprs”的GPRS APN格式。“使用EPC格式（EPC format）：本局所有用户给其他网元发送的APN为”xxx.yyy.3gppnetwork.org”的EPC APN的格式。“基于IMSI号段使用EPC格式（EPC format Depends on IMSI segment）：ADD EPC NAME MSID SEG命令设置的IMSI用户发送到其他网元的APN形式变为”xxx.yyy.3gppnetwork.org”的EPC APN的格式。“基于IMEI号段使用EPC格式（EPC format Depends on IMEI segment）：ADD EPC NAME MSID SEG命令设置的IMEI用户发送到其他网元的APN形式变为”xxx.yyy.3gppnetwork.org”的EPC APN的格式。






命令举例 


设置本局的LTE能力终端域名格式为“GPRS格式”。 


SET EPC APN NAME CFG:APNFORMAT="GPRS format"; 








父主题： [LTE能力终端域名格式配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询LTE能力域名格式(SHOW EPC APN NAME CFG) 
## 查询LTE能力域名格式(SHOW EPC APN NAME CFG) 


命令功能 

该命令用于查询本局支持的LTE能力终端域名格式。本局可以支持LTE能力终端域名格式为GPRS格式或者EPC格式。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNFORMAT|APN域名格式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局的LTE能力终端域名格式。 取值含义：“使用GPRS格式（GRPS format）”：本局所有用户给其他网元发送的APN将变成形式为“xxx.yyy.gprs”的GPRS APN格式。“使用EPC格式（EPC format）：本局所有用户给其他网元发送的APN为”xxx.yyy.3gppnetwork.org”的EPC APN的格式。“基于IMSI号段使用EPC格式（EPC format Depends on IMSI segment）：ADD EPC NAME MSID SEG命令设置的IMSI用户发送到其他网元的APN形式变为”xxx.yyy.3gppnetwork.org”的EPC APN的格式。“基于IMEI号段使用EPC格式（EPC format Depends on IMEI segment）：ADD EPC NAME MSID SEG命令设置的IMEI用户发送到其他网元的APN形式变为”xxx.yyy.3gppnetwork.org”的EPC APN的格式。






命令举例 


查询本局的LTE能力终端域名格式。 


SHOW EPC APN NAME CFG; 


`

命令 (No.1): SHOW EPC APN NAME CFG

操作维护  APN域名格式
---------------------
修改      使用GPRS格式
---------------------
记录数 1

命令执行成功（耗时 0.031 秒）。
` 








父主题： [LTE能力终端域名格式配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增支持EPC格式域名号段(ADD EPC NAME MSID SEG) 
## 新增支持EPC格式域名号段(ADD EPC NAME MSID SEG) 


命令功能 

该命令用于新增支持EPC格式域名的号段。当需要新增支持EPC格式域名的IMSI号段或者IMEI号段时，使用该命令。新增支持EPC格式域名的号段成功后，该IMSI或者IMEI号段的用户在与其他网元进行控制面信令交互时，信令中携带的APN格式变成形式为”xxx.yyy.3gppnetwork.org”的EPC APN的格式，其他用户将使用形式为“xxx.yyy.gprs”的GPRS APN格式。


注意事项 



 
如果新增了支持EPC格式域名的号段为IMSI号段，本局的LTE能力终端域名格式必须为基于IMSI号段使用EPC格式，否则新增的数据无法生效。 
 

 
如果新增了支持EPC格式域名的号段为IMEI号段，本局的LTE能力终端域名格式必须为基于IMEI号段使用EPC格式，否则新增的数据无法生效。 
 

 




参数说明 


标识|名称|类型|说明
---|---|---|---
SEGTYPE|号段类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置支持EPC格式域名的用户号段是为IMSI号段还是为IMEI号段。取值含义：“IMSI（IMSI）”：支持EPC APN格式域名的用户号段是为IMSI号段。“IMEI（IMEI）：支持EPC APN格式域名的用户号段是为 IMEI号段。
MSIDSEG|号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置支持EPC格式域名的用户号段。






命令举例 


新增本局支持EPC格式域名的用户号段，号段类型是“IMSI”，号段前缀是“460103”。 


ADD EPC NAME MSID SEG:SEGTYPE="IMSI",MSIDSEG="460103"; 








父主题： [LTE能力终端域名格式配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除支持EPC格式域名号段(DEL EPC NAME MSID SEG) 
## 删除支持EPC格式域名号段(DEL EPC NAME MSID SEG) 


命令功能 

该命令用于删除支持EPC格式域名的号段。当需要删除支持EPC格式域名的IMSI号段或者IMEI号段时。使用该命令，删除支持EPC格式域名的号段成功后，被删除号段的用户在与其他网元进行控制面信令交互时，信令中携带的APN格式将由EPC APN的格式，变成形式为“xxx.yyy.gprs”的GPRS APN格式。


注意事项 

该命令执行后，被删除号段的用户使用的APN将不再是EPC APN格式，将会变成默认的GPRS APN格式。


参数说明 


标识|名称|类型|说明
---|---|---|---
SEGTYPE|号段类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置支持EPC格式域名的用户号段是为IMSI号段还是为IMEI号段。取值含义：“IMSI（IMSI）”：支持EPC APN格式域名的用户号段是为IMSI号段。“IMEI（IMEI）：支持EPC APN格式域名的用户号段是为 IMEI号段。
MSIDSEG|号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置支持EPC格式域名的用户号段。






命令举例 


删除本局支持EPC格式域名的用户号段，号段类型为“IMSI”，号段前缀是“460103”。 


DEL EPC NAME MSID SEG:SEGTYPE="IMSI",MSIDSEG="460103"; 








父主题： [LTE能力终端域名格式配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询支持EPC格式域名号段(SHOW EPC NAME MSID SEG) 
## 查询支持EPC格式域名号段(SHOW EPC NAME MSID SEG) 


命令功能 

该命令用于查询本局支持EPC格式域名的用户IMSI或者IMEI号段。该IMSI或者IMEI号段的用户在与其他网元进行控制面信令交互时，信令中携带的APN变成形式为”xxx.yyy.3gppnetwork.org”的EPC APN的格式，其它用户将使用形式为“xxx.yyy.gprs”的GPRS APN格式。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
SEGTYPE|号段类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置支持EPC格式域名的用户号段是为IMSI号段还是为IMEI号段。取值含义：“IMSI（IMSI）”：支持EPC APN格式域名的用户号段是为IMSI号段。“IMEI（IMEI）：支持EPC APN格式域名的用户号段是为 IMEI号段。
MSIDSEG|号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置支持EPC格式域名的用户号段。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
SEGTYPE|号段类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置支持EPC格式域名的用户号段是为IMSI号段还是为IMEI号段。取值含义：“IMSI（IMSI）”：支持EPC APN格式域名的用户号段是为IMSI号段。“IMEI（IMEI）：支持EPC APN格式域名的用户号段是为 IMEI号段。
MSIDSEG|号段|参数可选性:任选参数；参数类型:字符型。|该参数用于设置支持EPC格式域名的用户号段。






命令举例 


查询本局支持EPC格式域名的用户号段。 


SHOW EPC NAME MSID SEG; 


`

命令 (No.1): SHOW EPC NAME MSID SEG;

操作维护    号段类型   号段
---------------------------
复制 删除   IMSI       460103
---------------------------
记录数 1

命令执行成功（耗时 0.052 秒）。
` 








父主题： [LTE能力终端域名格式配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 签约APN DT前缀配置 
# 签约APN DT前缀配置 


背景知识 


某些运营商部署的HLR/HSS在用户签约的APN中携带APN DT（Direct Tunnel，直传隧道）前缀信息，通过APN DT前缀，运营商可以实现基于APN控制是否支持DT。 




功能描述 


用户在激活流程中，SGSN在进行APN检查时，如果需要检查从HLR/HSS获取的签约上下文，则使用签约的APN与本局配置的支持DT的APN前缀进行比较，根据前缀是否相等，决定基于APN控制是否支持DT。 


配置支持DT功能的流程如下： 







                        RNC局向附加属性中配置支持DT功能，配置命令参见：
                        [ADD RNC]
                        。
                    







                        确定GGSN是否支持DT，有两种方式：配置支持DT的GGSN地址（
                        [ADD DT IP]
                        ）和本地根据APN进行配置，使用GPRS APN HOST配置（
                        [ADD GPRS APN]
                        ）或EPC APN HOST配置（
                        [ADD EPC APN]
                        ）或DNS解析类APN配置（
                        [ADD DNSAPNCHG]
                        ）。
                    







                        配置支持DT的APN前缀，检查用户签约APN DT前缀信息，配置命令为：
                        [SET APN DT PREFIX]
                        。
                    






注意事项： 



 

SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。
 

 

软件参数“DT话单控制”（ID：786523），控制是否产生DT话单，该软件参数取值为0，则不产生无流量的DT话单（not generate no volume DT CDR）；取值为1，则产生DT话单（generate DT CDR）；取值为2，则不产生DT话单（not generagte DT CDR）。
 

 

软件参数“DT切换频次”（ID：786527），除SGSN首次建立DT外，控制SGSN建立DT的切换频次。该软件参数取值为0，则总是允许；取值为1-254，则第N+1次允许（allow once for every N+1 times）；取值为255，则总是不允许。
 

 

软件参数“CAMEL用户是否允许隧道直传”（ID：786546），控制CAMEL用户是否允许DT功能。该软件参数取值为0，则不允许CAMEL用户隧道直传；取值为1，则允许CAMEL用户隧道直传。
 

 




相关主题 



 

设置签约APN DT前缀配置(SET APN DT PREFIX)
 

 

查询签约APN DT前缀配置(SHOW APN DT PREFIX)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置签约APN DT前缀配置(SET APN DT PREFIX) 
## 设置签约APN DT前缀配置(SET APN DT PREFIX) 


命令功能 


根据本命令的配置数据，SGSN可以基于MS的签约APN的NI部分的前缀决定此类用户是否支持DT功能。 


MS在PDP激活流程中，SGSN将使用HLR/HSS中签约的APN与本命令配置的APN NI部分的前缀进行比较，如果可以匹配，则表示SGSN对基于此APN接入的用户启用DT功能。 




注意事项 

此功能只适用于SGSN。


参数说明 


标识|名称|类型|说明
---|---|---|---
CHECKCTX|是否检查签约上下文|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置为“是”：表示SGSN使用MS签约的APN与本命令配置的APN NI部分的前缀进行比较，根据前缀是否相等，决定是否对此类用户开启DT功能。如果设置为“否”：则无需比较，表示SGSN对此类用户不启用DT功能。
APNPERFIX|APN前缀|参数可选性:任选参数；参数类型:字符型；参数范围为:0~20个字符。|表示APN NI部分的前缀。SGSN使用此参数与用户签约的APN的NI部分的前缀进行匹配，如果可以匹配，表示SGSN对基于此APN接入的用户启用DT功能。






命令举例 


设置签约APN DT前缀，检查签约上下文，APN前缀为zte。 


SET APN DT PREFIX:CHECKCTX="YES",APNPERFIX="zte"; 








父主题： [签约APN DT前缀配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询签约APN DT前缀配置(SHOW APN DT PREFIX) 
## 查询签约APN DT前缀配置(SHOW APN DT PREFIX) 


命令功能 

该命令用于查询SGSN根据MS的签约APN NI部分的前缀决定是否支持DT功能的配置数据。


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
CHECKCTX|是否检查签约上下文|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置为“是”：表示SGSN使用MS签约的APN与本命令配置的APN NI部分的前缀进行比较，根据前缀是否相等，决定是否对此类用户开启DT功能。如果设置为“否”：则无需比较，表示SGSN对此类用户不启用DT功能。
APNPERFIX|APN前缀|参数可选性:任选参数；参数类型:字符型。|表示APN NI部分的前缀。SGSN使用此参数与用户签约的APN的NI部分的前缀进行匹配，如果可以匹配，表示SGSN对基于此APN接入的用户启用DT功能。






命令举例 


查询签约APN DT前缀配置。 


SHOW APN DT PREFIX; 


`

命令 (No.1): SHOW APN DT PREFIX

操作维护  是否检查签约上下文   APN前缀
--------------------------------------
修改      是                   zte
--------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [签约APN DT前缀配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 转换APN配置 
# 转换APN配置 


背景知识 


APN转换：当用户携带的APN合法且是用户签约的APN时，根据IMSI、APN和PDP类型匹配判断是否需要进行APN转换，如果是，则将当前APN转换为配置指定的APN。 


SGSN能够根据IMSI 和终端请求的APN进行APN转换处理，然后根据转换后的APN来灵活选择不同的GGSN/PGW，转换后的APN对其他网元可见。 




功能描述 


SGSN进行APN有效性检查时，当用户携带的APN合法且是用户签约的APN时，根据IMSI、APN和PDP类型对APN NI进行转换，然后用转换后的APN NI来构造APN获取服务的GGSN/PGW。 


注意事项： 


软件参数“根据IMSI号段进行APN转换”（ID：786537），控制是否开启根据IMSI号段进行APN转换功能，软件参数取值为0，则不支持根据IMSI号段进行APN转换；取值为1，则支持根据IMSI号段进行APN转换。 




相关主题 



 

新增转换APN配置(ADD CONVERT APN)
 

 

修改转换APN配置(SET CONVERT APN)
 

 

删除转换APN配置(DEL CONVERT APN)
 

 

查询转换APN配置(SHOW CONVERT APN)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增转换APN配置(ADD CONVERT APN) 
## 新增转换APN配置(ADD CONVERT APN) 


命令功能 


该命令用于SGSN对MS请求的APN进行转换。 


当SGSN需要根据MS的IMSI号段、PDP类型和MS请求的APN这三个条件，灵活选择不同的GGSN/PGW时，使用该配置命令。 


当MS请求的APN合法且是MS的签约APN时，SGSN将请求APN的NI转换为此命令配置的APN NI，然后对转换后的APN NI进行解析，以便获取对应的GGSN/PGW的IP地址。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
REQPDPTYPE|终端请求PDP类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|表示MS的PDP类型，包括“IPv4”、“IPv6”、“IPv4v6”和“PPP”四种类型。
REQAPN|终端请求APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为MS请求APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
CNVTAPN|SGSN转换APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为SGSN对MS请求APN的NI部分进行转换后的APN NI。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


新增转换APN配置，IMSI号段为46001，终端请求PDP类型为IPv4，终端请求APN名称为zte.com，SGSN转换APN名称为zte1.com。 


ADD CONVERT APN:IMSI=46001,REQPDPTYPE="IPv4",REQAPN="zte.com",CNVTAPN="zte1.com"; 








父主题： [转换APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改转换APN配置(SET CONVERT APN) 
## 修改转换APN配置(SET CONVERT APN) 


命令功能 

该命令用于根据MS的IMSI号段、PDP类型和MS请求的APN这三个条件修改APN NI的转换配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
REQPDPTYPE|终端请求PDP类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|表示MS的PDP类型，包括“IPv4”、“IPv6”、“IPv4v6”和“PPP”四种类型。
REQAPN|终端请求APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为MS请求APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
CNVTAPN|SGSN转换APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数为SGSN对MS请求APN的NI部分进行转换后的APN NI。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


修改转换APN配置，将IMSI号段为46001，终端请求PDP类型为IPv4，终端请求APN的SGSN转换APN名称修改为zte2.com。 


SET CONVERT APN:IMSI="46001",REQPDPTYPE="IPv4",REQAPN="zte.com",CNVTAPN="zte2.com"; 








父主题： [转换APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除转换APN配置(DEL CONVERT APN) 
## 删除转换APN配置(DEL CONVERT APN) 


命令功能 

该命令用于根据MS的IMSI号段、PDP类型和MS请求的APN这三个条件删除APN NI的转换配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
REQPDPTYPE|终端请求PDP类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|表示MS的PDP类型，包括“IPv4”、“IPv6”、“IPv4v6”和“PPP”四种类型。
REQAPN|终端请求APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|该参数为MS请求APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。






命令举例 


将IMSI号段为46001，终端请求PDP类型为IPv4，终端请求APN的APN转换配置删除。 


DEL CONVERT APN:IMSI=46001,REQPDPTYPE="IPv4",REQAPN="zte.com"; 








父主题： [转换APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询转换APN配置(SHOW CONVERT APN) 
## 查询转换APN配置(SHOW CONVERT APN) 


命令功能 

该命令用于查询APN NI的转换配置数据。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
REQPDPTYPE|终端请求PDP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示MS的PDP类型，包括“IPv4”、“IPv6”、“IPv4v6”和“PPP”四种类型。
REQAPN|终端请求APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数为MS请求APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|此参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSINMCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
REQPDPTYPE|终端请求PDP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示MS的PDP类型，包括“IPv4”、“IPv6”、“IPv4v6”和“PPP”四种类型。
REQAPN|终端请求APN|参数可选性:任选参数；参数类型:字符型。|该参数为MS请求APN的NI部分。 APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出GGSN；另一方面，APN标识了通过该GGSN所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该GGSN接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了GGSN所在的GPRS分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
CNVTAPN|SGSN转换APN|参数可选性:任选参数；参数类型:字符型。|该参数为SGSN对MS请求APN的NI部分进行转换后的APN NI。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






命令举例 


查询APN转换配置。 


SHOW CONVERT APN; 


`

命令 (No.1): SHOW CONVERT APN

操作维护         IMSI号段   终端请求PDP类型   终端请求APN   SGSN转换APN   用户别名
----------------------------------------------------------------------------------
复制 修改 删除   46001      IPv4              zte.com       zte1.com      
----------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.051 秒）。
` 








父主题： [转换APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# IMS APN配置 
# IMS APN配置 


背景知识 


IMS APN是EPC网络支持VoLTE业务后引入的，运营商通常为移动用户分配特定的APN，该APN专用于连接IMS网络，使用IMS业务，此类APN 称为IMS APN。移动用户发起业务时，MME需要识别移动用户使用的APN或者签约的APN是否是IMS APN，从而针对该APN进行业务控制和性能统计等。 




功能描述 


“IMS APN配置”用于指定移动用户使用IMS业务、连接IMS网络专用的APN名称。MME根据该配置，识别移动用户使用的APN或者签约的APN是否是IMS APN。 


说明： 


IMS MME的计数器“IMS网络PDN连接请求次数”和“IMS网络PDN连接成功次数”仅针对此处配置的IMS APN统计。 




相关主题 



 

新增IMS APN配置(ADD IMS APN)
 

 

删除IMS APN配置(DEL IMS APN)
 

 

查询IMS APN配置(SHOW IMS APN)
 

 

新增基于PLMN的IMS APN配置(ADD PLMN IMS APN)
 

 

删除基于PLMN的IMS APN配置(DEL PLMN IMS APN)
 

 

查询基于PLMN的IMS APN配置(SHOW PLMN IMS APN)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增通用IMS APN配置(ADD IMS APN) 
## 新增通用IMS APN配置(ADD IMS APN) 


命令功能 


该命令用于新增IMS APN配置配置。 




注意事项 


 MME最多支持配置64个IMS APN。 


此处配置的APN仅需要配置APN NI。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|IMS APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|IMS APN是EPC网络支持VoLTE业务后引入的，运营商为移动用户分配特定的APN，该APN专用于移动用户连接IMS网络，使用IMS业务。






命令举例 


新增IMS APN配置，其中IMS APN名称为apn。 


ADD IMS APN:APNNAME="apn"; 








父主题： [IMS APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除通用IMS APN配置(DEL IMS APN) 
## 删除通用IMS APN配置(DEL IMS APN) 


命令功能 


该命令用于删除IMS APN配置。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|IMS APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|IMS APN是EPC网络支持VoLTE业务后引入的，运营商为移动用户分配特定的APN，该APN专用于移动用户连接IMS网络，使用IMS业务。






命令举例 


删除IMS APN配置，其中IMS APN名称为apn。 


DEL IMS APN:APNNAME="apn"; 








父主题： [IMS APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询通用IMS APN配置(SHOW IMS APN) 
## 查询通用IMS APN配置(SHOW IMS APN) 


命令功能 


该命令用于查询IMS APN配置。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|IMS APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|IMS APN是EPC网络支持VoLTE业务后引入的，运营商为移动用户分配特定的APN，该APN专用于移动用户连接IMS网络，使用IMS业务。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|IMS APN名称|参数可选性:任选参数；参数类型:字符型。|IMS APN是EPC网络支持VoLTE业务后引入的，运营商为移动用户分配特定的APN，该APN专用于移动用户连接IMS网络，使用IMS业务。






命令举例 


查询IMS APN配置。 


SHOW IMS APN; 


`

命令 (No.11): SHOW IMS APN

操作维护 IMS APN名称 
-----------------------
复制 删除  apn 
-----------------------
记录数 1

命令执行成功（耗时 0.062 秒）。


` 








父主题： [IMS APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增基于PLMN的IMS APN配置(ADD PLMN IMS APN) 
## 新增基于PLMN的IMS APN配置(ADD PLMN IMS APN) 


命令功能 


该命令用于新增基于PLMN的IMS APN配置。当需要根据PLMN来识别用户使用的APN是否是IMS APN时，使用该命令进行配置。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|IMS APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|IMS APN是EPC网络支持VoLTE业务后引入的，运营商为移动用户分配特定的APN，该APN专用于移动用户连接IMS网络，使用IMS业务。
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。






命令举例 


增加基于PLMN的IMS APN配置，其中IMS APN名称为zte，PLMN为460-01。 


ADD PLMN IMS APN:APNNAME="zte",PLMN="460"-"01"; 








父主题： [IMS APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除基于PLMN的IMS APN配置(DEL PLMN IMS APN) 
## 删除基于PLMN的IMS APN配置(DEL PLMN IMS APN) 


命令功能 


该命令用于删除PLMN配置了哪些IMS APN。当某些APN在某个PLMN下已经不是IMS APN时，使用该命令进行删除。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|IMS APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|IMS APN是EPC网络支持VoLTE业务后引入的，运营商为移动用户分配特定的APN，该APN专用于移动用户连接IMS网络，使用IMS业务。
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。






命令举例 


删除基于PLMN的IMS APN配置，其中IMS APN名称为zte，PLMN为460-01。 


DEL PLMN IMS APN:APNNAME="zte",PLMN="460"-"01"; 








父主题： [IMS APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询基于PLMN的IMS APN配置(SHOW PLMN IMS APN) 
## 查询基于PLMN的IMS APN配置(SHOW PLMN IMS APN) 


命令功能 


该命令用于查询PLMN下配置的IMS APN。当需要查询某个PLMN下配置了哪些IMS APN时，使用该命令进行查询。 




注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|IMS APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|IMS APN是EPC网络支持VoLTE业务后引入的，运营商为移动用户分配特定的APN，该APN专用于移动用户连接IMS网络，使用IMS业务。
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNNAME|IMS APN名称|参数可选性:任选参数；参数类型:字符型。|IMS APN是EPC网络支持VoLTE业务后引入的，运营商为移动用户分配特定的APN，该APN专用于移动用户连接IMS网络，使用IMS业务。
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。






命令举例 


显示基于PLMN的IMS APN配置。 


SHOW PLMN IMS APN; 


`

命令 (No.1): SHOW PLMN IMS APN;

操作维护    IMS APN名称   PLMN
------------------------------
复制 删除   zte           460-01
------------------------------
记录数 1

命令执行成功（耗时 0.047 秒）。
` 








父主题： [IMS APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# APN选择策略配置 
# APN选择策略配置 


背景知识 

            
            运营商的定制APN选择需求，区别于协议3GPP 23.060上描述的APN选择流程。运营商对签约通配APN的特定漫游用户和其他用户要实施不同的计费策略和业务控制，APN是业务接入点和计费关键字，APN对用户的计费策略和业务控制起决定作用，因此运营商希望SGSN区分这两类用户选择APN。
        


功能描述 

            
            SGSN提供配置区分签约通配APN的特定漫游用户和其他用户。对签约通配APN的特定漫游用户不忽略签约的通配APN，SGSN选择用户请求的APN。对其他用户，如果签约了通配APN，则忽略其签约的通配APN；如果用户请求了APN且该APN已签约，则SGSN选择用户请求的APN；如果用户未请求APN，则SGSN选择“APN更正配置”的APN（参见
            [ADD APN MODIFICATION]
            ）。
        


相关主题 



 

设置SGSN APN选择控制(SET SGSN APN POLICY CONTROL)
 

 

查询SGSN APN选择控制(SHOW SGSN APN POLICY CONTROL)
 

 

新增APN选择策略(ADD APN POLICY)
 

 

修改APN选择策略(SET APN POLICY)
 

 

删除APN选择策略(DEL APN POLICY)
 

 

查询APN选择策略(SHOW APN POLICY)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置SGSN APN选择控制(SET SGSN APN POLICY CONTROL) 
## 设置SGSN APN选择控制(SET SGSN APN POLICY CONTROL) 


命令功能 


该命令用于配置SGSN是否支持特定的APN选择、默认是否忽略签约的通配APN和本地QoS模板标识。 


当需要打开或者关闭SGSN特定APN选择功能、配置默认是否忽略签约的通配APN和本地QoS模板标识时，使用该命令。 




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
APNSELCTL|SGSN是否支持特定的APN选择|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识SGSN是否支持特定的APN选择。不支持（Not Support）：SGSN不支持特定的APN选择。支持（Support）：SGSN支持特定的APN选择。
IGNORECOMAPN|默认是否忽略签约的通配APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识默认是否忽略签约的通配APN。不忽略（Not Ignore）：默认不忽略签约的通配APN。忽略（Ignore）：默认忽略签约的通配APN。
REJNOSUBAPN|无匹配签约APN时是否拒绝|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识当打开忽略签约的通配功能开关后，若无匹配签约APN时，SGSN是否拒绝PDP激活。






命令举例 


设置SGSN APN选择控制，设置SGSN是否支持特定的APN选择为支持、默认是否忽略签约的通配APN为忽略。 


SET SGSN APN POLICY CONTROL:APNSELCTL="YES",IGNORECOMAPN="YES"; 








父主题： [APN选择策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询SGSN APN选择控制(SHOW SGSN APN POLICY CONTROL) 
## 查询SGSN APN选择控制(SHOW SGSN APN POLICY CONTROL) 


命令功能 


该命令用于查询SGSN是否支持特定的APN选择、默认是否忽略签约的通配APN和本地QoS模板标识。 


可以查询出SGSN特定APN选择功能是开启还是关闭、默认是否忽略签约的通配APN和本地QoS模板标识。 




注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
APNSELCTL|SGSN是否支持特定的APN选择|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识SGSN是否支持特定的APN选择。不支持（Not Support）：SGSN不支持特定的APN选择。支持（Support）：SGSN支持特定的APN选择。
IGNORECOMAPN|默认是否忽略签约的通配APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识默认是否忽略签约的通配APN。不忽略（Not Ignore）：默认不忽略签约的通配APN。忽略（Ignore）：默认忽略签约的通配APN。
REJNOSUBAPN|无匹配签约APN时是否拒绝|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识当打开忽略签约的通配功能开关后，若无匹配签约APN时，SGSN是否拒绝PDP激活。






命令举例 


查询SGSN APN选择控制。 


SHOW SGSN APN POLICY CONTROL; 


`

2018-03-29 10:53:59 命令 (No.1): SHOW SGSN APN POLICY CONTROL

操作维护  SGSN是否支持特定的APN选择   默认是否忽略签约的通配APN   无匹配签约APN时是否拒绝
-----------------------------------------------------------------------------------------
修改      不支持                      不忽略                      否
-----------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.023 秒）。
` 








父主题： [APN选择策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增APN选择策略(ADD APN POLICY) 
## 新增APN选择策略(ADD APN POLICY) 


命令功能 


该命令用于新增APN选择策略配置。 


如果该命令配置的IMSI号段“不忽略签约的通配APN”，则此号段对应的签约通配APN的用户是特定漫游用户，SGSN为此类用户选择用户请求的APN。 


如果该命令配置的IMSI号段“忽略签约的通配APN”，则此号段对应的用户是其他用户，如果用户请求了APN且该APN已签约，则SGSN选择用户请求的APN，如果用户未请求APN，则SGSN选择“APN更正配置”的APN（参见[ADD APN MODIFICATION]）。




注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
OPTION|是否忽略签约的通配APN|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数标识是否忽略签约的通配APN。不忽略（Not Ignore）：不忽略签约的通配APN。忽略（Ignore）：忽略签约的通配APN。
REJNOSUBAPN|无匹配签约APN时是否拒绝|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数标识当打开忽略签约的通配功能开关后，若无匹配签约APN时，SGSN是否拒绝PDP激活。






命令举例 


新增APN选择策略，IMSI为4600199999988，是否忽略签约的通配APN为不忽略。 


ADD APN POLICY:IMSI="4600199999988",OPTION="NO",REJNOSUBAPN="NO"; 








父主题： [APN选择策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改APN选择策略(SET APN POLICY) 
## 修改APN选择策略(SET APN POLICY) 


命令功能 

该命令用于修改APN选择策略配置。当需要修改用户号段是否忽略签约的通配APN时，使用该命令。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
OPTION|是否忽略签约的通配APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识是否忽略签约的通配APN。不忽略（Not Ignore）：不忽略签约的通配APN。忽略（Ignore）：忽略签约的通配APN。
REJNOSUBAPN|无匹配签约APN时是否拒绝|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识当打开忽略签约的通配功能开关后，若无匹配签约APN时，SGSN是否拒绝PDP激活。






命令举例 


修改APN选择策略。修改IMSI为4600199999988的APN选择策略，是否忽略签约的通配APN修改为不忽略。 


SET APN POLICY:IMSI="4600199999988",OPTION="NO"; 








父主题： [APN选择策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除APN选择策略(DEL APN POLICY) 
## 删除APN选择策略(DEL APN POLICY) 


命令功能 

该命令用于删除APN选择策略配置。当需要删除APN选择策略配置记录时，使用该命令。该命令执行成功后，会删除指定号码段的配置记录。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






命令举例 


删除IMSI为4600199999988的APN选择策略。 


DEL APN POLICY:IMSI="4600199999988"; 








父主题： [APN选择策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询APN选择策略(SHOW APN POLICY) 
## 查询APN选择策略(SHOW APN POLICY) 


命令功能 

该命令用于查询APN选择策略配置。可查询IMSI号段与是否忽略签约的通配APN的对应关系。


注意事项 

无。


参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
OPTION|是否忽略签约的通配APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识是否忽略签约的通配APN。不忽略（Not Ignore）：不忽略签约的通配APN。忽略（Ignore）：忽略签约的通配APN。
REJNOSUBAPN|无匹配签约APN时是否拒绝|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识当打开忽略签约的通配功能开关后，若无匹配签约APN时，SGSN是否拒绝PDP激活。






命令举例 


查询APN选择策略。 


SHOW APN POLICY; 


`

2018-03-29 10:57:15 命令 (No.4): SHOW APN POLICY;

操作维护         IMSI            是否忽略签约的通配APN   无匹配签约APN时是否拒绝
--------------------------------------------------------------------------------
复制 修改 删除   4600199999988   不忽略                  否
--------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.011 秒）。
` 








父主题： [APN选择策略配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 专用APN配置 
# 专用APN配置 


背景知识 


随着专网业务的不断拓展，为简化用户在终端UE界面上进行公网业务与专网业务之间切换的操作以及避免终端UE的功能限制，“用户公网业务与专网业务无感知切换及同时并存”的业务需求应运而生。



针对上述业务需求，网络侧可采用双APN无感分流方案，即：

1、当终端接入到4G网络后，终端只建立通用APN的PDN连接，MME基于本地配置的专用APN列表识别出有无感分流需求的用户，并为该类用户选择无感分流专用PGW。

2、专网业务到达， 在无感分流专用PGW和负责企业专网APN业务的PGW之间建立专用APN的PDN连接；无感分流专用PGW负责专用APN会话和通用APN会话之间的业务映射，屏蔽终端侧感知。 




功能描述 


“专用APN配置”用于MME本地配置专用APN列表以及无感分流关键字。 




相关主题 



 

新增专用APN配置(ADD DEDICATED APN)
 

 

修改专用APN配置(SET DEDICATED APN)
 

 

删除专用APN配置(DEL DEDICATED APN)
 

 

查询专用APN配置(SHOW DEDICATED APN)
 

 








父主题： [APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改专用APN配置(SET DEDICATED APN) 
## 修改专用APN配置(SET DEDICATED APN) 


命令功能 

该命令用于修改专用APN配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于MME本地配置专用APN，即专网业务对应的APN。APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求：不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ISTRANSPLITKEY|是否无感分流关键字|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置该APN是否为无感分流关键字。取值含义：否：该APN不是无感分流关键字。是：该APN是无感分流关键字。






命令举例 


修改专用APN配置，APN为"wugan"，是否无感分流关键字为“否”。 


SET DEDICATED APN:APN="wugan",ISTRANSPLITKEY="NO"; 








父主题： [专用APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除专用APN配置(DEL DEDICATED APN) 
## 删除专用APN配置(DEL DEDICATED APN) 


命令功能 

该命令用于删除专用APN配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于MME本地配置专用APN，即专网业务对应的APN。APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求：不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






命令举例 


删除专用APN配置，APN为"wugan"。 


DEL DEDICATED APN:APN="wugan"; 








父主题： [专用APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询专用APN配置(SHOW DEDICATED APN) 
## 查询专用APN配置(SHOW DEDICATED APN) 


命令功能 

该命令用于修改专用APN配置。


注意事项 


无。 




参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于MME本地配置专用APN，即专网业务对应的APN。APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求：不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。






输出参数说明 


标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于MME本地配置专用APN，即专网业务对应的APN。APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求：不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ISTRANSPLITKEY|是否无感分流关键字|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置该APN是否为无感分流关键字。取值含义：否：该APN不是无感分流关键字。是：该APN是无感分流关键字。






命令举例 


查询专用APN配置。 


SHOW DEDICATED APN; 


`

(No.1) : SHOW DEDICATED APN:
-----------------combo35/NFS_MMESGSN_0----------------
操作维护       APN    是否无感分流关键字 
-----------------------------------------------------------------                                     
复制 修改 删除 wugan  否                                         
-----------------------------------------------------------------
记录数：1

执行成功开始时间:2022-06-22 17:54:39 耗时: 2.531秒

` 








父主题： [专用APN配置]












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


