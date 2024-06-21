 业务配置 
背景知识 
系统业务流程需要相关的配置来提高业务基本流程、网元选择、业务控制等方面稳定性和灵活性。 
功能描述 
本功能包括所有业务功能相关的配置。 
相关主题 
 
邻接局索引配置
 
 
RNC局向附加属性配置
 
 
偶联索引配置
 
 
基于GGSN IP功能控制配置
 
 
号码分析配置
 
 
业务地址查询
 
 
用户面地址配置
 
 
APN配置
 
 
MME IMSI号段LBO限制配置
 
 
SGSN IMSI号段LBO限制配置
 
 
3G扩展ARD策略配置
 
 
支持DT的GGSN IP配置
 
 
支持终端双栈的GGSN IP配置
 
 
不支持终端双栈的GGSN IP配置
 
 
Delivery Order控制配置
 
 
SGSN支持的Target ID配置
 
 
UE网络能力IE支持的版本
 
 
计费配置
 
 
GPRS地址解析配置
 
 
EPC地址解析配置
 
 
EPC地址解析优选子网段配置
 
 
PGW解析配置
 
 
MMEGI解析配置
 
 
MME RFSP策略配置
 
 
SGSN RFSP策略配置
 
 
MME基于IMSI号段IMEI检查配置
 
 
SGSN基于IMSI号段IMEI检查配置
 
 
SGSN ODB配置
 
 
漫游GGSN失败配置
 
 
漫游GGSN失败原因值映射配置
 
 
GGSN本地网段配置
 
 
MME ODB配置
 
 
SMS配置
 
 
跨RAT切换时映射配置
 
 
HeNB配置
 
 
基于号段选择S-GW配置
 
 
紧急呼叫配置
 
 
LCS配置
 
 
ESMLC组标识配置
 
 
MME控制开关配置
 
 
MME GMLC配置
 
 
支持定制CLR的HSS列表
 
 
Relay配置
 
 
LIPA配置
 
 
缺省SRVCC增强MSC Server配置
 
 
PGW局向特性配置
 
 
基于PGW IP控制配置
 
 
内置PGW的GGSN IP配置
 
 
优化切换到eHRPD的配置
 
 
MME非3GPP互操作配置
 
 
失败原因值映射配置
 
 
MPS配置
 
 
基于IMEI限制DT配置
 
 
SGSN消息参数配置
 
 
物联网业务配置
 
 
GGSN重选配置
 
 
rSRVCC配置
 
 
MME SMS业务配置
 
 
MME CS/PS协作配置
 
 
VoLTE业务控制策略配置
 
 
MME直接向UE获取IMSI配置
 
 
EPC PDN类型转换配置
 
 
MME头压缩配置
 
 
MME IMEI检查频次配置
 
 
NSA业务配置
 
 
SGSN IMEI检查频次配置
 
 
MME ePCO配置
 
 
基于PLMN的无线覆盖增强与CE mode B控制策略配置
 
 
5GC互操作基本配置
 
 
EMS PLUS管理
 
 
语音参数策略配置
 
 
PWS配置
 
 
语音中心用户限制配置
 
 
MME事件监控配置
 
 
无线连接异常释放策略配置
 
 
Gb口Rerouting配置
 
 
MME消息参数配置
 
 
父主题： [配置管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 邻接局索引配置 
# 邻接局索引配置 
背景知识 
信令系统是通信网的重要组成部分。No.7信令系统有四个功能级：信令数据链路级、信令链路功能级、信令网功能级以及用户部分。邻接局在信令网功能级中用于描述与本局相邻的信令点信息。 
功能描述 
本功能用于为本局新增、删除、查询、修改邻接局的配置信息。包括邻接信令点的信令点码、邻接信令点位于何种类型的信令网络、邻接信令点是否为信令转接点等信息。 
相关主题 
 
新增邻接局索引(ADD ADJOFCIDCFG)
 
 
修改邻接局索引(SET ADJOFCIDCFG)
 
 
删除邻接局索引(DEL ADJOFCIDCFG)
 
 
查询邻接局索引(SHOW ADJOFCIDCFG)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增邻接局索引(ADD ADJOFCIDCFG) 
## 新增邻接局索引(ADD ADJOFCIDCFG) 
命令功能 
新增邻接局索引
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OFCID|邻接局号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|本参数用于配置邻接局号。
OFCTYPE|邻接局类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|本参数用于设置邻接局的局向类别，包括：BSC、RNC、WNP-SRF、MSCSERVER、GMSCSERVER、SGSN、GGSN、HLR/HLRe、AUC、SMC、SCP/SCPe、GMLC等局向。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|本参数用于设置邻接局的别名。
命令举例 
新增邻接局索引
ADD ADJOFCIDCFG:OFCID=1,OFCTYPE="RNC",NAME="u1"; 
父主题： [邻接局索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改邻接局索引(SET ADJOFCIDCFG) 
## 修改邻接局索引(SET ADJOFCIDCFG) 
命令功能 
修改邻接局索引
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OFCID|邻接局号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|本参数用于配置邻接局号。
OFCTYPE|邻接局类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|本参数用于设置邻接局的局向类别，包括：BSC、RNC、WNP-SRF、MSCSERVER、GMSCSERVER、SGSN、GGSN、HLR/HLRe、AUC、SMC、SCP/SCPe、GMLC等局向。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|本参数用于设置邻接局的别名。
命令举例 
修改邻接局索引
SET ADJOFCIDCFG:OFCID=1,NAME="ua"; 
父主题： [邻接局索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除邻接局索引(DEL ADJOFCIDCFG) 
## 删除邻接局索引(DEL ADJOFCIDCFG) 
命令功能 
删除邻接局索引
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OFCID|邻接局号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|本参数用于配置邻接局号。
命令举例 
删除邻接局索引
DEL ADJOFCIDCFG:OFCID=1; 
父主题： [邻接局索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询邻接局索引(SHOW ADJOFCIDCFG) 
## 查询邻接局索引(SHOW ADJOFCIDCFG) 
命令功能 
查询邻接局索引
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OFCID|邻接局号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|本参数用于配置邻接局号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OFCID|邻接局号|参数可选性:任选参数；参数类型:整数。|本参数用于配置邻接局号。
OFCTYPE|邻接局类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|本参数用于设置邻接局的局向类别，包括：BSC、RNC、WNP-SRF、MSCSERVER、GMSCSERVER、SGSN、GGSN、HLR/HLRe、AUC、SMC、SCP/SCPe、GMLC等局向。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|本参数用于设置邻接局的别名。
命令举例 
查询邻接局索引。 
SHOW ADJOFCIDCFG:OFCID=2431; 
`
(No.4) : SHOW ADJOFCIDCFG:OFCID=2431;
-----------------NFS_MMESGSN_0----------------
邻接局号	邻接局类别	用户别名
2431    RNC局
记录数 1
命令执行成功（耗时 0.047 秒）。
 ` 
父主题： [邻接局索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# RNC局向附加属性配置 
# RNC局向附加属性配置 
背景知识 
无线网络子系统（RNS）由节点B（Node B）和无线网络控制器（RNC）组成，其中Node B负责在一个或多个小区与用户设备（UE）之间的无线传输和接收；而RNC则负责控制无线资源的使用和完整性；RNC与核心网（CN）之间通过Iu接口相连。Iu接口，无线网络层的信令协议为RANAP，底层信令协议为SCCP。 
E-UTRAN Service Handover参数用于控制用户从3G业务区切换到4G业务区。当用户开通签约此业务，RNC应尽可能让用户存在于3G业务区。 
功能描述 
对于SGSN来说，RNC也视为7号信令邻接局向统一管理，通过以下2个配置设置RNC局向的属性： 
                邻接局配置（命令为：
                [ADD ADJOFC]
                ）中设置与No.7信令相关的属性。
            
RNC局向附件属性配置中设置和上层应用相关的属性，例如，是否支持Flex功能等。 
另外，本配置中的另一个功能是配置RNC与RAI或LAI的关系，使得SGSN根据用户当前所在的RAI或LAI寻呼时，可以找到对应的用户所在的RNC。 
RNC的属性配置，需要和RNC侧协商一致。 
相关主题 
 
新增RNC局向附加属性(ADD RNC)
 
 
修改RNC局向附加属性(SET RNC)
 
 
删除RNC局向附加属性(DEL RNC)
 
 
查询RNC局向附加属性(SHOW RNC)
 
 
新增RNC局向寻呼区域(ADD RNC PAGING AREA)
 
 
删除RNC局向寻呼区域(DEL RNC PAGING AREA)
 
 
查询RNC局向寻呼区域(SHOW RNC PAGING AREA)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增RNC局向附加属性(ADD RNC) 
## 新增RNC局向附加属性(ADD RNC) 
命令功能 
该命令用于新增RNC局向附加属性。配置该命令中的RNC局向相关的属性，用于实现该RNC局向的对应功能实现，配置相应某一属性为支持则表明该RNC局向支持该项功能。属性之间相对独立，并无相关性。 
注意事项 
 
配置该命令需要首先配置RNC邻接局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号。
 
 
移动国家码、运营商码分别对应本SGSN所在国家的国家码及运营商的运营商码。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指定RNC局向所在国家的移动国家码，例如中国的移动国家码为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指定RNC局向所在运营商的PLMN编号。根据规划填写。例如，中国电信为03。
RNC|RNC标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|该参数用于指定RNC局向对应的RNC ID。
FLEX|支持Flex功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定该RNC是否支持FLEX功能。该参数设置与SET SGSNCFG中的“是否支持FLEX”参数，同时为支持时表明支持该RNC的FLEX功能。FLEX功能是指包括RNC、SGSN网元在内组成一个POOL（池），RNC接入多个SGSN，当前接入的SGSN出现故障或其它原因导致SGSN不可用时，RNC可以接入其它SGSN。这样就实现了用户接入SGSN的负载均衡、容灾等功能特性。取值含义：不支持（NO）：不支持FLEX功能支持（YES）：支持FLEX功能
RAT|RAT属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:UTRAN。|该参数用于指定无线接入类型。默认配置RNC的接入类型为UTRAN。取值含义：UTRAN（UTRAN）：UTRAN接入GERAN（GERAN）：GERAN接入
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定该RNC是否支持Direct Tunnel功能。当命令ADD GPRS APN中的参数“支持DT功能”设置为支持时，才支持该RNC接入用户建立DT方式承载。DT功能是指建立该DT类型承载后，上下行用户面数据不再通过SGSN，而是在GGSN、RNC间直接传输，绕过SGSN。DT功能要求RNC、SGSN、GGSN同时支持，才能真正完成DT类型承载的建立。取值含义：不支持（NO）：不支持Direct Tunnel功能支持（YES）：支持Direct Tunnel功能
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定该RNC是否支持终端双栈功能。此参数与命令ADD GPRS APN中的参数“支持终端双栈功能”同时设置为支持时，才支持该RNC接入用户建立双栈地址的PDP承载。终端双栈功能是指终端支持分配IP地址类型为IPV4或IPV6地址两种格式。取值含义：不支持（NO）：不支持终端双栈功能支持（YES）：支持终端双栈功能
SPRTFLOWSCH|支持多流调度功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定该RNC是否支持多流调度功能。多流程调度为RNC侧针对一卡双号，同等条件数据卡接入，即使同一用户的两张卡或不同用户两张卡，RNC都尽量分配在不同的载波上。要求核心网区分一卡双号的用户，并将双号用户用固定的ID捆绑并告知RNC，从而RNC针对一卡双号的用户分配相应的无线资源。该参数与命令SHOW SOFTWARE PARAMETER中的参数“SGSN是否支持RNC多流调度功能”同时都设置为支持时，才支持多流调度功能。启动该功能后，在用户进入READY状态时，SGSN通知RNC，用户支持多流程调度功能，且通知用户的ISDN号码。取值含义：不支持（NO）：不支持多流调度功能支持（YES）：支持多流调度功能
SNAFLAG|支持SNA功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定该RNC是否支持SNA功能。SNA功能指共享网络区域，RNC可以接入到不同的运营商的无线网络，当用户由该RNC接入到的SGSN，发现不允许该用户接入到本网时，SGSN发接入拒绝，拒绝原因表明用户不允许接入本网，RNC根据该原因向其它核心网接入。实际应用常为运营商租用其它运营商的无线网络的情况。取值含义：不支持（NO）：不支持SNA功能支持（YES）：支持SNA功能
DEQOSVER|是否降低QoS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于根据当前RNC附加属性配置中"是否降低 QoS版本 "的值来决定是否将版本降低到R6范围。当配置该参数为支持时，协商后QOS不高于R6版本。取值含义：不支持（NO）：不支持降低QoS版本支持（YES）：支持降低QoS版本
RABQOS|是否支持RAB QoS协商|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定该RNC是否支持RAB QoS协商。RAB QoS协商是指RNC根据RNC配置的QoS能力，与SGSN发送的RAB指派的承载能力的协商过程中，发现RAB指派时所带QoS，RNC并不支持QoS中的上下行速率等参数，那么允许RNC修改RAB参数，并在后续RAB指派响应消息中带给SGSN，来完成RAB的创建。当配置该参数为支持时，SGSN通知RNC，收到RAB指派时可以更改RAB参数。取值含义：不支持（NO）：不支持RAB QoS协商支持（YES）：支持RAB QoS协商
IUGTPUIPCAP|Iu GTPU IP能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:IPv4。|该参数用于指定该RNC支持的用户面IP地址能力，SGSN根据该参数跟GGSN分配用户用户面IP。比如配置为仅支持IPV4，那么在分配用户IP时，只分配IPV4的IP地址。取值含义：仅IPv4（IPv4）：仅支持IPv4仅IPv6（IPv6）：仅支持IPv6IPv4和IPv6（IPv4v6）：支持IPv4和IPv6
ASYMMETRYFLAG|是否强制RAB-AsymmetryIndicator为非双向对称|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指定该RNC强制RAB-AsymmetryIndicator为上下行速率是否为非双向对称速率。强制RAB-AsymmetryIndicator为非双向对称功能，是指强制要求上下行速率是不对称的。即使速率实际相同，那么上下行速率在指派时也要用两个不同字段表示。取值含义：否（NO）：不支持上下行速率为强制RAB-AsymmetryIndicator为非双向对称速率是（YES）：支持上下行速率为强制RAB-AsymmetryIndicator为非双向对称速率
EUTRANSERVHO|支持E-UTRAN Service Handover参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于配置当前RNC是否支持E-UTRAN Service Handover参数。支持：如果用户签约了E-UTRAN not allowed参数，SGSN发给RNC的RAB ASSIGNMENTREQUEST和RELOCATION REQUEST两个消息中会携带E-UTRAN Service Handover参数。不支持：无论用户是否签约了E-UTRAN not allowed参数，SGSN发给RNC的RAB ASSIGNMENTREQUEST和RELOCATION REQUEST两个消息中不会携带E-UTRAN Service Handover参数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数可以为某一有意义的名字，例如rnc_nanjing，表明是南京的RNC。
SPRTRFSP|支持RFSP|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:OFF。|该参数用于设置RNC是否支持RFSP功能。不支持：RNC默认不支持RFSP。支持：RNC支持RFSP。
命令举例 
新增RNC局向附加属性，设置RNC局向号为111，设置移动国家码为460，设置移动网号为001，设置RNC标识为1，设置RAT属性为UTRAN，其他参数使用系统默认配置。
ADD RNC:RNCOFFID=1,MCC="460",MNC="001",RNC=111,RAT="UTRAN"; 
父主题： [RNC局向附加属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改RNC局向附加属性(SET RNC) 
## 修改RNC局向附加属性(SET RNC) 
命令功能 
该命令用于修改RNC局向附加属性。这些属性在该命令中的参数中都有所体现。修改哪些属性取决于要求该RNC支持哪些功能。具体配置哪些附加属性由组网时，RNC的开局要求来决定。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指定RNC局向所在国家的移动国家码，例如中国的移动国家码为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指定RNC局向所在运营商的PLMN编号。根据规划填写。例如，中国电信为03。
RNC|RNC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于指定RNC局向对应的RNC ID。
FLEX|支持Flex功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持FLEX功能。该参数设置与SET SGSNCFG中的“是否支持FLEX”参数，同时为支持时表明支持该RNC的FLEX功能。FLEX功能是指包括RNC、SGSN网元在内组成一个POOL（池），RNC接入多个SGSN，当前接入的SGSN出现故障或其它原因导致SGSN不可用时，RNC可以接入其它SGSN。这样就实现了用户接入SGSN的负载均衡、容灾等功能特性。取值含义：不支持（NO）：不支持FLEX功能支持（YES）：支持FLEX功能
RAT|RAT属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定无线接入类型。默认配置RNC的接入类型为UTRAN。取值含义：UTRAN（UTRAN）：UTRAN接入GERAN（GERAN）：GERAN接入
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持Direct Tunnel功能。当命令ADD GPRS APN中的参数“支持DT功能”设置为支持时，才支持该RNC接入用户建立DT方式承载。DT功能是指建立该DT类型承载后，上下行用户面数据不再通过SGSN，而是在GGSN、RNC间直接传输，绕过SGSN。DT功能要求RNC、SGSN、GGSN同时支持，才能真正完成DT类型承载的建立。取值含义：不支持（NO）：不支持Direct Tunnel功能支持（YES）：支持Direct Tunnel功能
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持终端双栈功能。此参数与命令ADD GPRS APN中的参数“支持终端双栈功能”同时设置为支持时，才支持该RNC接入用户建立双栈地址的PDP承载。终端双栈功能是指终端支持分配IP地址类型为IPV4或IPV6地址两种格式。取值含义：不支持（NO）：不支持终端双栈功能支持（YES）：支持终端双栈功能
SPRTFLOWSCH|支持多流调度功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持多流调度功能。多流程调度为RNC侧针对一卡双号，同等条件数据卡接入，即使同一用户的两张卡或不同用户两张卡，RNC都尽量分配在不同的载波上。要求核心网区分一卡双号的用户，并将双号用户用固定的ID捆绑并告知RNC，从而RNC针对一卡双号的用户分配相应的无线资源。该参数与命令SHOW SOFTWARE PARAMETER中的参数“SGSN是否支持RNC多流调度功能”同时都设置为支持时，才支持多流调度功能。启动该功能后，在用户进入READY状态时，SGSN通知RNC，用户支持多流程调度功能，且通知用户的ISDN号码。取值含义：不支持（NO）：不支持多流调度功能支持（YES）：支持多流调度功能
SNAFLAG|支持SNA功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持SNA功能。SNA功能指共享网络区域，RNC可以接入到不同的运营商的无线网络，当用户由该RNC接入到的SGSN，发现不允许该用户接入到本网时，SGSN发接入拒绝，拒绝原因表明用户不允许接入本网，RNC根据该原因向其它核心网接入。实际应用常为运营商租用其它运营商的无线网络的情况。取值含义：不支持（NO）：不支持SNA功能支持（YES）：支持SNA功能
DEQOSVER|是否降低QoS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于根据当前RNC附加属性配置中"是否降低 QoS版本 "的值来决定是否将版本降低到R6范围。当配置该参数为支持时，协商后QOS不高于R6版本。取值含义：不支持（NO）：不支持降低QoS版本支持（YES）：支持降低QoS版本
RABQOS|是否支持RAB QoS协商|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持RAB QoS协商。RAB QoS协商是指RNC根据RNC配置的QoS能力，与SGSN发送的RAB指派的承载能力的协商过程中，发现RAB指派时所带QoS，RNC并不支持QoS中的上下行速率等参数，那么允许RNC修改RAB参数，并在后续RAB指派响应消息中带给SGSN，来完成RAB的创建。当配置该参数为支持时，SGSN通知RNC，收到RAB指派时可以更改RAB参数。取值含义：不支持（NO）：不支持RAB QoS协商支持（YES）：支持RAB QoS协商
IUGTPUIPCAP|Iu GTPU IP能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC支持的用户面IP地址能力，SGSN根据该参数跟GGSN分配用户用户面IP。比如配置为仅支持IPV4，那么在分配用户IP时，只分配IPV4的IP地址。取值含义：仅IPv4（IPv4）：仅支持IPv4仅IPv6（IPv6）：仅支持IPv6IPv4和IPv6（IPv4v6）：支持IPv4和IPv6
ASYMMETRYFLAG|是否强制RAB-AsymmetryIndicator为非双向对称|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC强制RAB-AsymmetryIndicator为上下行速率是否为非双向对称速率。强制RAB-AsymmetryIndicator为非双向对称功能，是指强制要求上下行速率是不对称的。即使速率实际相同，那么上下行速率在指派时也要用两个不同字段表示。取值含义：否（NO）：不支持上下行速率为强制RAB-AsymmetryIndicator为非双向对称速率是（YES）：支持上下行速率为强制RAB-AsymmetryIndicator为非双向对称速率
EUTRANSERVHO|支持E-UTRAN Service Handover参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当前RNC是否支持E-UTRAN Service Handover参数。支持：如果用户签约了E-UTRAN not allowed参数，SGSN发给RNC的RAB ASSIGNMENTREQUEST和RELOCATION REQUEST两个消息中会携带E-UTRAN Service Handover参数。不支持：无论用户是否签约了E-UTRAN not allowed参数，SGSN发给RNC的RAB ASSIGNMENTREQUEST和RELOCATION REQUEST两个消息中不会携带E-UTRAN Service Handover参数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数可以为某一有意义的名字，例如rnc_nanjing，表明是南京的RNC。
SPRTRFSP|支持RFSP|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置RNC是否支持RFSP功能。不支持：RNC默认不支持RFSP。支持：RNC支持RFSP。
命令举例 
修改RNC局向号为111的RNC局向附加属性，将RAT属性修改为GERAN。
SET RNC:RNCOFFID=111,RAT="GERAN"; 
父主题： [RNC局向附加属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除RNC局向附加属性(DEL RNC) 
## 删除RNC局向附加属性(DEL RNC) 
命令功能 
该命令用于删除RNC局向附加属性。当该局向也不需要配置，在组网中移除该RNC网元，才可以删除该RNC配置。删除本该配置后，该RNC网元无法再接入本SGSN。 
注意事项 
删除该RNC表明RNC从SGSN移除，相应的邻接局配置、局向对应的信令配置需要相应删除，避免SGSN存在无效配置数据。 
参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
命令举例 
删除RNC局向号为111的RNC局向附加属性。
DEL RNC:RNCOFFID=111; 
父主题： [RNC局向附加属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询RNC局向附加属性(SHOW RNC) 
## 查询RNC局向附加属性(SHOW RNC) 
命令功能 
该命令用于查询RNC局向附加属性。根据RNC ID来查询对应的配置项信息，当输入RNC ID参数时，查询的结果为所有RNC局向附加属性信息。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:任选参数；参数类型:整数。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|该参数用于指定RNC局向所在国家的移动国家码，例如中国的移动国家码为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|该参数用于指定RNC局向所在运营商的PLMN编号。根据规划填写。例如，中国电信为03。
RNC|RNC标识|参数可选性:任选参数；参数类型:整数。|该参数用于指定RNC局向对应的RNC ID。
FLEX|支持Flex功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持FLEX功能。该参数设置与SET SGSNCFG中的“是否支持FLEX”参数，同时为支持时表明支持该RNC的FLEX功能。FLEX功能是指包括RNC、SGSN网元在内组成一个POOL（池），RNC接入多个SGSN，当前接入的SGSN出现故障或其它原因导致SGSN不可用时，RNC可以接入其它SGSN。这样就实现了用户接入SGSN的负载均衡、容灾等功能特性。取值含义：不支持（NO）：不支持FLEX功能支持（YES）：支持FLEX功能
RAT|RAT属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定无线接入类型。默认配置RNC的接入类型为UTRAN。取值含义：UTRAN（UTRAN）：UTRAN接入GERAN（GERAN）：GERAN接入
DTSPRT|支持DT功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持Direct Tunnel功能。当命令ADD GPRS APN中的参数“支持DT功能”设置为支持时，才支持该RNC接入用户建立DT方式承载。DT功能是指建立该DT类型承载后，上下行用户面数据不再通过SGSN，而是在GGSN、RNC间直接传输，绕过SGSN。DT功能要求RNC、SGSN、GGSN同时支持，才能真正完成DT类型承载的建立。取值含义：不支持（NO）：不支持Direct Tunnel功能支持（YES）：支持Direct Tunnel功能
DUALSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持终端双栈功能。此参数与命令ADD GPRS APN中的参数“支持终端双栈功能”同时设置为支持时，才支持该RNC接入用户建立双栈地址的PDP承载。终端双栈功能是指终端支持分配IP地址类型为IPV4或IPV6地址两种格式。取值含义：不支持（NO）：不支持终端双栈功能支持（YES）：支持终端双栈功能
SPRTFLOWSCH|支持多流调度功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持多流调度功能。多流程调度为RNC侧针对一卡双号，同等条件数据卡接入，即使同一用户的两张卡或不同用户两张卡，RNC都尽量分配在不同的载波上。要求核心网区分一卡双号的用户，并将双号用户用固定的ID捆绑并告知RNC，从而RNC针对一卡双号的用户分配相应的无线资源。该参数与命令SHOW SOFTWARE PARAMETER中的参数“SGSN是否支持RNC多流调度功能”同时都设置为支持时，才支持多流调度功能。启动该功能后，在用户进入READY状态时，SGSN通知RNC，用户支持多流程调度功能，且通知用户的ISDN号码。取值含义：不支持（NO）：不支持多流调度功能支持（YES）：支持多流调度功能
SNAFLAG|支持SNA功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持SNA功能。SNA功能指共享网络区域，RNC可以接入到不同的运营商的无线网络，当用户由该RNC接入到的SGSN，发现不允许该用户接入到本网时，SGSN发接入拒绝，拒绝原因表明用户不允许接入本网，RNC根据该原因向其它核心网接入。实际应用常为运营商租用其它运营商的无线网络的情况。取值含义：不支持（NO）：不支持SNA功能支持（YES）：支持SNA功能
DEQOSVER|是否降低QoS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于根据当前RNC附加属性配置中"是否降低 QoS版本 "的值来决定是否将版本降低到R6范围。当配置该参数为支持时，协商后QOS不高于R6版本。取值含义：不支持（NO）：不支持降低QoS版本支持（YES）：支持降低QoS版本
RABQOS|是否支持RAB QoS协商|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC是否支持RAB QoS协商。RAB QoS协商是指RNC根据RNC配置的QoS能力，与SGSN发送的RAB指派的承载能力的协商过程中，发现RAB指派时所带QoS，RNC并不支持QoS中的上下行速率等参数，那么允许RNC修改RAB参数，并在后续RAB指派响应消息中带给SGSN，来完成RAB的创建。当配置该参数为支持时，SGSN通知RNC，收到RAB指派时可以更改RAB参数。取值含义：不支持（NO）：不支持RAB QoS协商支持（YES）：支持RAB QoS协商
IUGTPUIPCAP|Iu GTPU IP能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC支持的用户面IP地址能力，SGSN根据该参数跟GGSN分配用户用户面IP。比如配置为仅支持IPV4，那么在分配用户IP时，只分配IPV4的IP地址。取值含义：仅IPv4（IPv4）：仅支持IPv4仅IPv6（IPv6）：仅支持IPv6IPv4和IPv6（IPv4v6）：支持IPv4和IPv6
ASYMMETRYFLAG|是否强制RAB-AsymmetryIndicator为非双向对称|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定该RNC强制RAB-AsymmetryIndicator为上下行速率是否为非双向对称速率。强制RAB-AsymmetryIndicator为非双向对称功能，是指强制要求上下行速率是不对称的。即使速率实际相同，那么上下行速率在指派时也要用两个不同字段表示。取值含义：否（NO）：不支持上下行速率为强制RAB-AsymmetryIndicator为非双向对称速率是（YES）：支持上下行速率为强制RAB-AsymmetryIndicator为非双向对称速率
EUTRANSERVHO|支持E-UTRAN Service Handover参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当前RNC是否支持E-UTRAN Service Handover参数。支持：如果用户签约了E-UTRAN not allowed参数，SGSN发给RNC的RAB ASSIGNMENTREQUEST和RELOCATION REQUEST两个消息中会携带E-UTRAN Service Handover参数。不支持：无论用户是否签约了E-UTRAN not allowed参数，SGSN发给RNC的RAB ASSIGNMENTREQUEST和RELOCATION REQUEST两个消息中不会携带E-UTRAN Service Handover参数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数可以为某一有意义的名字，例如rnc_nanjing，表明是南京的RNC。
SPRTRFSP|支持RFSP|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置RNC是否支持RFSP功能。不支持：RNC默认不支持RFSP。支持：RNC支持RFSP。
命令举例 
查询RNC局向附加属性。 
SHOW RNC 
`
命令 (No.1): SHOW RNC
操作维护         RNC局向号   移动国家码   移动网号   RNC标识   支持Flex功能   RAT属性   支持DT功能   支持终端双栈功能   支持多流调度功能   支持SNA功能   是否降低QoS版本   是否支持RAB QoS协商   Iu GTPU IP能力   是否强制RAB-AsymmetryIndicator为非双向对称   支持E-UTRAN Service Handover参数   用户别名
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1           460          001        1         不支持         UTRAN     不支持       不支持             不支持             不支持        不降低            不支持                仅IPv4           否                                           否
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.056 秒）。
` 
父主题： [RNC局向附加属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增RNC局向寻呼区域(ADD RNC PAGING AREA) 
## 新增RNC局向寻呼区域(ADD RNC PAGING AREA) 
命令功能 
该命令用于新增RNC局向寻呼区域。寻呼区域决定了对该RNC无线信号覆盖下的用户进行寻呼时，在哪些位置区或路由区范围内进行寻呼。增加该配置时，根据实际组网要求的该RNC的实际覆盖范围的位置区或路由区来配置。 
注意事项 
 
配置该命令需要首先配置RNC，配置命令为： ADD RNC，该命令中的该参数RNCOFFID对应已配置的RNC配置中的RNCOFFID。
 
 
RNC寻呼区域要求，要么全是LAI，要么全是RAI。可以为RNC对应配置多个LAI，也可以为RNC对应配置多个RAI，但不能既有LAI，又有RAI。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
LAI|位置区名|参数可选性:必须单选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定该RNC下的LAI，可以配置多个LAI。对同一RNC，配置了LAI后不允许再对该RNC配置RAI。
RAI|路由区名|参数可选性:必须单选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定该RNC下的RAI，可以配置多个RAI。对同一RNC，配置了RAI后不允许再对该RNC配置LAI。
命令举例 
新增RNC局向寻呼区域，设置RNC局向号为1，位置区名为1。
ADD RNC PAGING AREA:RNCOFFID=1,LAI="1"; 
父主题： [RNC局向附加属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除RNC局向寻呼区域(DEL RNC PAGING AREA) 
## 删除RNC局向寻呼区域(DEL RNC PAGING AREA) 
命令功能 
该命令用于删除RNC局向寻呼区域。当RNC寻呼区域区域已不存在，或不需要在该区域进行寻呼时，可以删除该RNC的该寻呼区域。 
注意事项 
 
该删除命令必须在已配置的RNC寻呼区中有效记录，配置命令为：ADD RNC PAGING AREA。
 
 
位置区名和路由区名必须有且只有其中之一，且增加寻呼区域时为位置区，那么删除时只能删除该RNC的位置区，反之，增加的寻呼区域为路由区时，删除时只能删除路由区。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
LAI|位置区名|参数可选性:必须单选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定该RNC下的LAI，可以配置多个LAI。对同一RNC，配置了LAI后不允许再对该RNC配置RAI。
RAI|路由区名|参数可选性:必须单选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定该RNC下的RAI，可以配置多个RAI。对同一RNC，配置了RAI后不允许再对该RNC配置LAI。
命令举例 
删除RNC局向号为1，LAI为a的RNC局向寻呼区域。
DEL RNC PAGING AREA:RNCOFFID=1,LAI="a"; 
父主题： [RNC局向附加属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询RNC局向寻呼区域(SHOW RNC PAGING AREA) 
## 查询RNC局向寻呼区域(SHOW RNC PAGING AREA) 
命令功能 
该命令用于查询RNC局向寻呼区域。根据RNC ID参数查询某RNC的寻呼区域，如果不输入该参数，那么查询结果为所有配置的RNC的寻呼区域。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RNCOFFID|RNC局向号|参数可选性:任选参数；参数类型:整数。|该参数用于指定RNC局向ID。该局向ID，需要在邻接局中配置局向，配置命令为： ADD ADJOFC，RNCOFFID对应已配置的邻接局号 。
LAI|位置区名|参数可选性:任选参数；参数类型:字符型。|该参数用于指定该RNC下的LAI，可以配置多个LAI。对同一RNC，配置了LAI后不允许再对该RNC配置RAI。
RAI|路由区名|参数可选性:任选参数；参数类型:字符型。|该参数用于指定该RNC下的RAI，可以配置多个RAI。对同一RNC，配置了RAI后不允许再对该RNC配置LAI。
命令举例 
查询RNC局向1 的寻呼区域。
SHOW RNC PAGING AREA:RNCOFFID=1; 
`
命令 (No.1): SHOW RNC PAGING AREA:RNCOFFID=1;
操作维护    RNC局向号   位置区名   路由区名
-------------------------------------------
复制 删除   1           1          
-------------------------------------------
记录数 1
命令执行成功（耗时 0.049 秒）。
` 
父主题： [RNC局向附加属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 偶联索引配置 
# 偶联索引配置 
背景知识 
            
            在服务化架构下，信令和偶联配置在CommonS_SIG服务下，业务服务配置如果需要关联偶联，则需要配置偶联索引，且其偶联ID需要和CommonS_SIG服务下的SCTP偶联配置中的偶联ID相同。
        
功能描述 
            
            该功能用于配置则需要与业务关联的偶联的索引。
        
相关主题 
 
新增偶联索引(ADD SCTPIDCFG)
 
 
修改偶联索引(SET SCTPIDCFG)
 
 
删除偶联索引(DEL SCTPIDCFG)
 
 
查询偶联索引(SHOW SCTPIDCFG)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增偶联索引(ADD SCTPIDCFG) 
## 新增偶联索引(ADD SCTPIDCFG) 
命令功能 
该命令新增偶联索引，用于配置业务需要关联的SCTP偶联。其中，偶联ID、偶联协议协议类型，必须和CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的SCTP ID、Application Protocol Type相同。 
该命令的配置结果可以通过[SHOW SCTPIDCFG]命令进行查询。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SCTPID|偶联ID|参数可选性:必选参数；参数类型:整数。|该参数为SCTP偶联标识。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的SCTP ID相同。
TYPE|偶联协议类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数为偶联的归属上层协议类型。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的“Application Protocol Type”相同。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数为偶联的归属上层协议类型。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的“Application Protocol Type”相同。
命令举例 
新增偶联索引，其中偶联ID为10，偶联协议类型为S1AP。 
ADD SCTPIDCFG:SCTPID=10,TYPE="S1AP" 
父主题： [偶联索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改偶联索引(SET SCTPIDCFG) 
## 修改偶联索引(SET SCTPIDCFG) 
命令功能 
该命令修改偶联索引，用于修改业务需要关联的SCTP偶联的协议类型和用户别名。 
该命令的配置结果可以通过[SHOW SCTPIDCFG]命令进行查询。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SCTPID|偶联ID|参数可选性:必选参数；参数类型:整数。|该参数为SCTP偶联标识。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的SCTP ID相同。
TYPE|偶联协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为偶联的归属上层协议类型。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的“Application Protocol Type”相同。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数为偶联的归属上层协议类型。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的“Application Protocol Type”相同。
命令举例 
修改偶联索引，其中偶联ID为10，偶联协议类型为S1AP。 
SET SCTPIDCFG:SCTPID=10,TYPE="S1AP" 
父主题： [偶联索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除偶联索引(DEL SCTPIDCFG) 
## 删除偶联索引(DEL SCTPIDCFG) 
命令功能 
该命令用于删除偶联索引。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SCTPID|偶联ID|参数可选性:必选参数；参数类型:整数。|该参数为SCTP偶联标识。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的SCTP ID相同。
命令举例 
删除偶联索引，其中偶联ID为10。 
DEL SCTPIDCFG:SCTPID=10 
父主题： [偶联索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询偶联索引(SHOW SCTPIDCFG) 
## 查询偶联索引(SHOW SCTPIDCFG) 
命令功能 
该命令用于查询偶联索引。可以查询特定ID的偶联索引信息，也可以查询所有配置的偶联索引。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SCTPID|偶联ID|参数可选性:任选参数；参数类型:整数。|该参数为SCTP偶联标识。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的SCTP ID相同。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SCTPID|偶联ID|参数可选性:任选参数；参数类型:整数。|该参数为SCTP偶联标识。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的SCTP ID相同。
TYPE|偶联协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为偶联的归属上层协议类型。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的“Application Protocol Type”相同。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数为偶联的归属上层协议类型。该参数必须与CommonS_SIG服务的SCTP偶联配置ADD SCTP命令配置的“Application Protocol Type”相同。
命令举例 
查询偶联ID为10的偶联索引配置。 
SHOW SCTPIDCFG:SCTPID=10 
`
(No.2) : SHOW SCTPIDCFG:SCTPID=10
-----------------NFS_MMESGSN_0----------------
操作维护       偶联ID 偶联协议类型  用户别名 
-----------------------------------------------------
复制 修改 删除 10       S1AP                          
-----------------------------------------------------
记录数：1
执行成功开始时间:2020-08-11 19:11:24 耗时: 0.345 秒
` 
父主题： [偶联索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 基于GGSN IP功能控制配置 
# 基于GGSN IP功能控制配置 
背景知识 
            
            UBAS（User Behavior Analysis System，用户行为分析系统）支持基于小区进行用户业务行为的分析，为运营商提供进一步的精细化控制依据。例如，基于小区忙闲时的资源，运营商对用户业务等进行灵活控制。在不同的地区覆盖的小区内，用户访问业务的行为特点不同；在一些地区，由于用户可能访问一些为运营商带来低收益的业务（比如：P2P等），造成小区拥塞，为了保证用户对高优先级的业务体验，运营商需要对小区资源进行特殊的控制管理。
        
功能描述 
MS Info变换上报功能是，SGSN与无线侧Gb接口时，当用户的小区（CGI：Cell Global Identifier，全球小区标识）发生变化，SGSN向GGSN传递全球小区信息；SGSN与无线侧Iu接口时，当用户的服务区（SAI：Service Area Identity，服务区域标识）发生变化，SGSN向GGSN传递服务区信息（服务区和小区为一对多的关系），GGSN从SGSN获取小区或服务区信息，传递给UBAS用于分析。 
基于GGSN IP功能控制配置中设置支持MS Info变换上报的GGSN的IP地址，获得关联的GGSN是否支持MS Info变换上报，作为SGSN判断是否启用MS Info变换上报功能的依据。 
注意事项： 
SGSN支持MS Info变换上报功能受软件参数“是否支持MS Info Change Reporting功能”（ID：65551）控制，软件参数取值为0，则不支持上报；取值为1，则支持上报。 
相关主题 
 
新增GGSN IP功能(ADD GGSNIP FUNC)
 
 
删除GGSN IP功能(DEL GGSNIP FUNC)
 
 
查询GGSN IP功能(SHOW GGSNIP FUNC)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增GGSN IP功能(ADD GGSNIP FUNC) 
## 新增GGSN IP功能(ADD GGSNIP FUNC) 
命令功能 
基于GGSN IP功能控制配置是指：操作员通过此命令设置支持某功能的GGSN网元的IP地址，与SGSN交互的GGSN是否支持该功能，作为SGSN判断是否启用该功能的依据。当前只能配置一个功能，即是否支持MS Info变换上报功能。 
MS Info变换上报功能是指： 
无线侧为Gb接入模式，当MS的CGI（Cell Global Identifier，全球小区标识）发生变化时，SGSN向GGSN上报MS Info Change Notification Request消息，传递MS的CGI信息。 
无线侧为Iu接入模式，当MS的SAI（Service Area Identity，服务区域标识）发生变化时，SGSN向GGSN上报MS Info Change Notification Request消息，传递MS的SAI信息（服务区和小区为一对多的关系。） 
GGSN可以从SGSN获取到用户的当前位置信息，并将此信息传递给UBAS用于分析，UBAS基于小区对用户进行业务行为的分析，从而为运营商提供进一步精细化控制的依据。 
注意事项 
该功能只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN IP|参数可选性:必选参数；参数类型:地址|GGSN网元控制面IP地址。包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
FUNC|功能列表|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|支持的功能列表，目前只支持MS Info变化上报功能。
命令举例 
新增GGSN IP功能，其中IP地址为112.2.2.3，功能列表为支持MSInfo变化上报。 
ADD GGSNIP FUNC:IP="112.2.2.3",FUNC="MS_Info_Change_Report"; 
父主题： [基于GGSN IP功能控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除GGSN IP功能(DEL GGSNIP FUNC) 
## 删除GGSN IP功能(DEL GGSNIP FUNC) 
命令功能 
该命令用于删除基于GGSN IP的功能控制配置数据。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN IP|参数可选性:必选参数；参数类型:地址|GGSN网元控制面IP地址。包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
命令举例 
删除地址为112.2.2.3的GGSN IP功能。 
DEL GGSNIP FUNC:IP="112.2.2.3"; 
父主题： [基于GGSN IP功能控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询GGSN IP功能(SHOW GGSNIP FUNC) 
## 查询GGSN IP功能(SHOW GGSNIP FUNC) 
命令功能 
该命令用于查询与SGSN网元交互的GGSN网元的IP地址及其支持的功能列表。 
目前只支持MS Info变化上报功能。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN IP|参数可选性:任选参数；参数类型:地址|GGSN网元控制面IP地址。包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN IP|参数可选性:任选参数；参数类型:地址|GGSN网元控制面IP地址。包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
FUNC|功能列表|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持的功能列表，目前只支持MS Info变化上报功能。
命令举例 
查询GGSN IP对应的功能列表。 
SHOW GGSNIP FUNC; 
`
命令 (No.1): SHOW GGSNIP FUNC
操作维护    GGSN IP     功能列表
--------------------------------
复制 删除   112.2.2.3   支持MS Info变化上报功能
--------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [基于GGSN IP功能控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 号码分析配置 
# 号码分析配置 
背景知识 
号码分析是SGSN或MME在对外发送消息时，根据用户的IMSI，选择得到消息的目的网元局向。 
功能描述 
号码分析功能包含： 
 
分析IMSI号码，得到目的HSS局向号。
 
 
分析从HSS获得用户签约的GMLC网元号码，得到目的GMLC局向号。
 
 
分析IMSI号码，对IMSI号码进行转换，转换为ISDN（E.214）或者HLR（E.164）号码格式 ，位置更新时，SGSN 使用转换后的号码进行GT寻址，得到目的HLR局向号。
 
 
配置MME连接EIR网元的号码。
 
 
号码分析采用最长匹配的原则。（最长匹配如：配置有两条记录，记录A为460，记录B为46001，IMSI为460011234512345的用户将匹配到记录B）。 
相关主题 
 
移动号码分析结果索引
 
 
Diameter邻接局分析结果索引
 
 
Diameter GMLC分析结果索引配置
 
 
Diameter SMC分析结果索引配置
 
 
Diameter消息分析结果索引配置
 
 
TAI映射LAI配置
 
 
移动号码分析
 
 
EIR号码配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 移动号码分析结果索引 
## 移动号码分析结果索引 
背景知识 
用户进行附着或RAU业务需要向HLR发送消息时，SGSN根据用户IMSI号码进行号码分析，获得ISDN（E.214）或者HLR（E.164）号码 ，然后使用此号码进行GT翻译，得到目的HLR局向号。 
功能描述 
移动号码分析结果索引配置中，设置该索引对应的IMSI变换方式（ISDN或者HLR），并设置变换后的号码。 
                移动号码分析结果索引在移动号码分析配置
                [ADD MDNAL]
                中被引用。SGSN在用户进行附着和RAU等业务时，根据“移动号码分析”中的配置匹配号码分析结果索引。再根据此索引，在本配置项中获取IMSI变换后的号码，进行GT翻译，获取到用户对应的HLR局向号。
            
相关主题 
 
新增移动号码分析结果索引(ADD IROAM)
 
 
修改移动号码分析结果索引(SET IROAM)
 
 
删除移动号码分析结果索引(DEL IROAM)
 
 
查询移动号码分析结果索引(SHOW IROAM)
 
 
父主题： [号码分析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增移动号码分析结果索引(ADD IROAM) 
### 新增移动号码分析结果索引(ADD IROAM) 
命令功能 
该命令用于新增移动号码分析结果索引。当SGSN需要根据IMSI获得用户的ISDN号码或者HLR设备的号码，用于GT翻译得到HLR局向号时，使用该命令。命令执行成功后，提供一个号码分析结果索引，该索引指向一个ISDN号码或者HLR设备的号码，被用于GT翻译得到HLR局向号。 
注意事项 
该命令所配置的号码分析索引会被命令[ADD MDNAL] 引用。
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于指定一个移动号码分析结果索引值。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“IMSI号码分析”时，“号码分析结果索引”就会使用该参数配置的索引值。
TP|类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定移动号码分析得到号码的类型。取值含义：ISDN（ISDN）：用户的ISDN号码，E.214编码格式。当无法明确知道IMSI归属的HLR设备的号码时（例如：非本运营商的用户，无法根据IMSI明确知道其归属的运营商HLR设备的号码），号码类型选择“ISDN”。HLR（HLR）：HLR设备的号码，E.164编码格式。当明确知道IMSI归属的HLR设备的号码时，号码类型选择“HLR”。号码类型如何选择，由运营商根据实际组网决定。
RST|转换的结果|参数可选性:必选参数；参数类型:字符型；参数范围为:1~16个字符。|该参数用于指定移动号码分析后的结果，是一个ISDN（E.214）或者HLR（E.164）号码。该号码在命令ADD GT中与“被叫GT号码”参数相对应，起到对用户进行路由的作用。
EXFL|附加特性列表|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置此号段用户的附加特性。支持T-ADS查询(SUPPORT_TADS)：此号段的用户是否支持T-ADS（Terminating Access Domain Selection，终结接入域选择）查询功能。当SGSN向HLR上报位置更新消息时，会根据该配置报告自己是否支持T-ADS查询。T-ADS需要附加offeredCamel4CSIs(TADS_OFFERED)：此号段的用户在支持T-ADS查询时，是否需要附加Camel4CSI信息。当“支持T-ADS查询”开启，SGSN在向HLR上报位置更新消息时，会根据该配置报告自己是否附加Camel4CSI信息。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数可配置为特定含义的名称，用做备注。
命令举例 
新增移动号码分析结果索引，其中号码分析结果索引为1，类型为HLR，转换的结果是86139003，用户别名是test。 
ADD IROAM:IDX=1,TP="HLR",RST="86139003",NAME="test"; 
父主题： [移动号码分析结果索引]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改移动号码分析结果索引(SET IROAM) 
### 修改移动号码分析结果索引(SET IROAM) 
命令功能 
该命令用于修改移动号码分析结果索引。当需要修改IMSI对应的转换结果，或者IMSI对应的附加特性列表时，使用该命令。命令执行成功后，SGSN按照新的转换结果ISDN号码，通过GT翻译得到HLR局向号；或者获取到新的附加特性列表。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于指定一个移动号码分析结果索引值。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“IMSI号码分析”时，“号码分析结果索引”就会使用该参数配置的索引值。
RST|转换的结果|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|该参数用于指定移动号码分析后的结果，是一个ISDN（E.214）或者HLR（E.164）号码。该号码在命令ADD GT中与“被叫GT号码”参数相对应，起到对用户进行路由的作用。
EXFL|附加特性列表|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置此号段用户的附加特性。支持T-ADS查询(SUPPORT_TADS)：此号段的用户是否支持T-ADS（Terminating Access Domain Selection，终结接入域选择）查询功能。当SGSN向HLR上报位置更新消息时，会根据该配置报告自己是否支持T-ADS查询。T-ADS需要附加offeredCamel4CSIs(TADS_OFFERED)：此号段的用户在支持T-ADS查询时，是否需要附加Camel4CSI信息。当“支持T-ADS查询”开启，SGSN在向HLR上报位置更新消息时，会根据该配置报告自己是否附加Camel4CSI信息。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数可配置为特定含义的名称，用做备注。
命令举例 
修改移动号码分析结果索引，其中号码分析结果索引为1，将转换的结果修改为86139005。 
SET IROAM:IDX=1,RST="86139005"; 
父主题： [移动号码分析结果索引]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除移动号码分析结果索引(DEL IROAM) 
### 删除移动号码分析结果索引(DEL IROAM) 
命令功能 
该命令用于删除移动号码分析结果索引。命令执行成功后，SGSN无法获取该IMSI对应的ISDN号码，也无法通过GT翻译得到HLR局向号。 
注意事项 
如果要删除移动号码分析结果索引，必须先查询该索引是否已经被[ADD MDNAL]引用。如果该索引未被引用，则删除成功；如果该索引已经被引用，则删除失败，必须先删除[ADD MDNAL]引用过该索引的记录，再删除该索引。
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于指定一个移动号码分析结果索引值。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“IMSI号码分析”时，“号码分析结果索引”就会使用该参数配置的索引值。
命令举例 
删除移动号码分析结果索引，其中号码分析结果索引为1。 
DEL IROAM:IDX=1; 
父主题： [移动号码分析结果索引]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询移动号码分析结果索引(SHOW IROAM) 
### 查询移动号码分析结果索引(SHOW IROAM) 
命令功能 
该命令用于查询移动号码分析结果索引。通过号码分析结果索引进行查询；如果不带该参数，表明查询所有配置记录。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于指定一个移动号码分析结果索引值。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“IMSI号码分析”时，“号码分析结果索引”就会使用该参数配置的索引值。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数。|该参数用于指定一个移动号码分析结果索引值。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“IMSI号码分析”时，“号码分析结果索引”就会使用该参数配置的索引值。
TP|类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定移动号码分析得到号码的类型。取值含义：ISDN（ISDN）：用户的ISDN号码，E.214编码格式。当无法明确知道IMSI归属的HLR设备的号码时（例如：非本运营商的用户，无法根据IMSI明确知道其归属的运营商HLR设备的号码），号码类型选择“ISDN”。HLR（HLR）：HLR设备的号码，E.164编码格式。当明确知道IMSI归属的HLR设备的号码时，号码类型选择“HLR”。号码类型如何选择，由运营商根据实际组网决定。
RST|转换的结果|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|该参数用于指定移动号码分析后的结果，是一个ISDN（E.214）或者HLR（E.164）号码。该号码在命令ADD GT中与“被叫GT号码”参数相对应，起到对用户进行路由的作用。
EXFL|附加特性列表|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置此号段用户的附加特性。支持T-ADS查询(SUPPORT_TADS)：此号段的用户是否支持T-ADS（Terminating Access Domain Selection，终结接入域选择）查询功能。当SGSN向HLR上报位置更新消息时，会根据该配置报告自己是否支持T-ADS查询。T-ADS需要附加offeredCamel4CSIs(TADS_OFFERED)：此号段的用户在支持T-ADS查询时，是否需要附加Camel4CSI信息。当“支持T-ADS查询”开启，SGSN在向HLR上报位置更新消息时，会根据该配置报告自己是否附加Camel4CSI信息。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数可配置为特定含义的名称，用做备注。
命令举例 
查询已配置的移动号码分析结果索引。 
SHOW IROAM; 
`
命令 (No.1): SHOW IROAM
操作维护         号码分析结果索引   类型   转换的结果   附加特性列表                   用户别名
-----------------------------------------------------------------------------------------------
复制 修改 删除   1                  HLR    86139003     Null                           test
-----------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.059 秒）。
` 
父主题： [移动号码分析结果索引]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## Diameter邻接局分析结果索引 
## Diameter邻接局分析结果索引 
背景知识 
MME/SGSN进行附着和TAU等业务时，需要根据IMSI选择对应的HSS局向，向其发送消息。 
功能描述 
本配置用于配置“号码分析结果索引”对应的HSS“邻接局向编号”。 
 
                        在移动号码分析配置
                        ADD MDNAL
                        中，当“分析器入口”选择“Diameter邻接局分析”时，“号码分析结果索引”参数值引用本配置中的“号码分析结果索引”。
                    
 
 
                        “邻接局向编号”引用自Diameter局向配置
                        ADD DIAMADJ
                        中的“Diameter局向号”。
                    
 
 
                当MME/SGSN发起附着或者TAU业务时，MME/SGSN根据用户的IMSI在移动号码分析配置
                [ADD MDNAL]
                中匹配被分析号码，获取IMSI对应的Diameter邻接局分析结果索引，然后根据此索引，在本配置中查找对应的HSS局向号，然后向其发消息。
            
相关主题 
 
新增Diameter邻接局分析结果索引(ADD DIMOFC ANALYSIS)
 
 
修改Diameter邻接局分析结果索引(SET DIMOFC ANALYSIS)
 
 
删除Diameter邻接局分析结果索引(DEL DIMOFC ANALYSIS)
 
 
查询Diameter邻接局分析结果索引(SHOW DIMOFC ANALYSIS)
 
 
父主题： [号码分析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增Diameter邻接局分析结果索引(ADD DIMOFC ANALYSIS) 
### 新增Diameter邻接局分析结果索引(ADD DIMOFC ANALYSIS) 
命令功能 
该命令用于增加Diameter邻接局分析结果索引，以便被移动号码分析配置[ADD MDNAL]引用。
当需要增加移动号码分析[ADD MDNAL]中的“号码分析结果索引”和Diameter邻接局向的关联关系时，使用该命令。命令执行成功后，可以间接地实现移动号码段和Diameter邻接局的关联。
移动号码段和Diameter邻接局向关联关系的配置流程如下： 
使用本命令增加一个号码分析结果索引，并关联对应的Diameter邻接局。 
使用[ADD MDNAL]命令增加移动号码分析，分析入口选择Diameter邻接局分析，将被分析号码（移动号码段）与新增的号码分析结果索引关联，这样就间接实现了移动号码段和Diameter邻接局的关联。
注意事项 
 
号码分析结果索引对应的Diameter邻接局向，需要先在Diameter局向配置ADD DIAMADJ中配置。 
 
 
一个号码分析结果索引最多只能关联一个Diameter邻接局。 
 
 
一个Diameter邻接局可以关联多个号码分析结果索引。
 
 
只有当移动号码分析配置ADD MDNAL中“分析器入口”选择“Diameter邻接局分析”时，才能引用本配置中的“号码分析结果索引”。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数表示Diameter邻接局分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter邻接局分析”时，“号码分析结果索引”参数值引用本参数。
DIAMGRPID|邻接局编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数表示号码分析结果索引所关联的Diameter邻接局编号，引用自Diameter局向配置ADD DIAMADJ中的“Diameter局向号”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条Diameter邻接局分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
新增Diameter邻接局分析结果索引，其中号码分析结果索引为3，关联的邻接局编号为1，用户别名为test。 
ADD DIMOFC ANALYSIS:IDX=3,DIAMGRPID=1,NAME="test"; 
父主题： [Diameter邻接局分析结果索引]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改Diameter邻接局分析结果索引(SET DIMOFC ANALYSIS) 
### 修改Diameter邻接局分析结果索引(SET DIMOFC ANALYSIS) 
命令功能 
该命令用于修改已添加的号码分析结果索引对应的Diameter邻接局编号和/或用户别名。 
待修改的号码分析结果索引可通过[SHOW DIMOFC ANALYSIS]命令查询。
注意事项 
 
一个号码分析结果索引最多只能关联一个Diameter邻接局。 
 
 
一个Diameter邻接局可以关联多个号码分析结果索引。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数表示Diameter邻接局分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter邻接局分析”时，“号码分析结果索引”参数值引用本参数。
DIAMGRPID|邻接局编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|该参数表示号码分析结果索引所关联的Diameter邻接局编号，引用自Diameter局向配置ADD DIAMADJ中的“Diameter局向号”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条Diameter邻接局分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
修改Diameter邻接局分析结果索引对应的邻接局向号，其中号码分析结果索引为3，将其关联的新邻接局编号修改为2。 
SET DIMOFC ANALYSIS:IDX=3,DIAMGRPID=2; 
父主题： [Diameter邻接局分析结果索引]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除Diameter邻接局分析结果索引(DEL DIMOFC ANALYSIS) 
### 删除Diameter邻接局分析结果索引(DEL DIMOFC ANALYSIS) 
命令功能 
该命令用于删除已添加的Diameter邻接局分析结果索引。执行该命令后，号码分析结果索引和Diameter邻接局的关联关系就被断开，从而导致移动号码分析中的号段无法关联到Diameter邻接局上。 
注意事项 
如果Diameter邻接局分析结果索引已经被移动号码分析引用（查询命令参见[SHOW MDNAL]），该分析结果索引不能被删除。必须先删除移动号码分析表中与该Diameter邻接局分析结果索引对应的记录（删除命令参见[DEL MDNAL]），然后才能使用本命令删除邻接局分析结果索引。
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数表示Diameter邻接局分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter邻接局分析”时，“号码分析结果索引”参数值引用本参数。
命令举例 
删除号码分析结果索引为3的Diameter邻接局分析结果索引。 
DEL DIMOFC ANALYSIS:IDX=3; 
父主题： [Diameter邻接局分析结果索引]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询Diameter邻接局分析结果索引(SHOW DIMOFC ANALYSIS) 
### 查询Diameter邻接局分析结果索引(SHOW DIMOFC ANALYSIS) 
命令功能 
该命令用于查询Diameter邻接局分析结果索引。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|该参数表示Diameter邻接局分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter邻接局分析”时，“号码分析结果索引”参数值引用本参数。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数。|该参数表示Diameter邻接局分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter邻接局分析”时，“号码分析结果索引”参数值引用本参数。
DIAMGRPID|邻接局编号|参数可选性:任选参数；参数类型:整数。|该参数表示号码分析结果索引所关联的Diameter邻接局编号，引用自Diameter局向配置ADD DIAMADJ中的“Diameter局向号”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条Diameter邻接局分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
查询已配置的Diameter邻接局分析结果索引。 
SHOW DIMOFC ANALYSIS; 
`
命令 (No.1): SHOW DIMOFC ANALYSIS
操作维护         号码分析结果索引   邻接局编号   用户别名
---------------------------------------------------------
复制 修改 删除   3                  1           
---------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
 ` 
父主题： [Diameter邻接局分析结果索引]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## Diameter GMLC分析结果索引配置 
## Diameter GMLC分析结果索引配置 
背景知识 
MME/SGSN进行定位业务时，需要根据用户签约的GMLC号码选择对应的GMLC局向，向其发送消息。 
功能描述 
本配置用于设置“号码分析结果索引”对应的“Diameter GMLC局向标识”。 
 
                        在移动号码分析配置
                        ADD MDNAL
                        中，当“分析器入口”选择“GMLC邻接局分析”时，“号码分析结果索引”参数值引用本配置中的“号码分析结果索引”。
                    
 
 
                        “Diameter GMLC局向标识”引用自Diameter GMLC局向配置
                        ADD DIAMGMLCADJ
                        中的“局向标识”。
                    
 
 
                当MME/SGSN发起LCS定位业务时，MME/SGSN根据用户签约的GMLC号码在移动号码分析配置
                [ADD MDNAL]
                中匹配被分析号码，获取GMLC号码对应的Diameter GMLC邻接局分析结果索引，然后根据此索引，在本配置中查找对应的GMLC局向号，并向其发消息。
            
相关主题 
 
新增Diameter GMLC分析结果索引(ADD DIMGMLC ANALYSIS)
 
 
修改Diameter GMLC分析结果索引(SET DIMGMLC ANALYSIS)
 
 
删除Diameter GMLC分析结果索引(DEL DIMGMLC ANALYSIS)
 
 
查询Diameter GMLC分析结果索引(SHOW DIMGMLC ANALYSIS)
 
 
父主题： [号码分析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增Diameter GMLC分析结果索引(ADD DIMGMLC ANALYSIS) 
### 新增Diameter GMLC分析结果索引(ADD DIMGMLC ANALYSIS) 
命令功能 
该命令用于增加Diameter GMLC分析结果索引，以便被移动号码分析配置[ADD MDNAL]引用。
当需要增加移动号码分析[ADD MDNAL]中的“号码分析结果索引”和Diameter GMLC局向的关联关系时，使用该命令。命令执行成功后，可以间接地实现GMLC号码段和Diameter GMLC局向的关联。
GMLC号码段和Diameter GMLC局向关联关系的配置流程如下： 
使用本命令增加一个号码分析结果索引，并关联对应的Diameter GMLC邻接局。 
使用[ADD MDNAL]命令增加移动号码分析，分析入口选择GMLC邻接局分析，将被分析号码（GMLC号码段）与新增的号码分析结果索引关联，这样就间接实现了GMLC号码段到Diameter GMLC局向的关联。
注意事项 
 
号码分析结果索引对应的Diameter GMLC局向标识，需要先在Diameter GMLC局向配置 ADD DIAMGMLCADJ中配置。
 
 
一个号码分析结果索引最多只能关联一个Diameter GMLC局向。 
 
 
一个Diameter GMLC局向可以关联多个号码分析结果索引。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数表示Diameter GMLC局向分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“GMLC邻接局分析”时，“号码分析结果索引”参数值引用本参数。
DIAMGMLCID|Diameter GMLC局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数表示号码分析结果索引所关联的Diameter GMLC局向标识，引用自Diameter GMLC局向配置ADD DIAMGMLCADJ中的“局向标识”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条GMLC号码分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
新增Diameter GMLC分析结果索引，其中号码分析结果索引为1，GMLC局向标识为2，用户别名为test。 
ADD DIMGMLC ANALYSIS:IDX=1,DIAMGMLCID=2,NAME="test"; 
父主题： [Diameter GMLC分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改Diameter GMLC分析结果索引(SET DIMGMLC ANALYSIS) 
### 修改Diameter GMLC分析结果索引(SET DIMGMLC ANALYSIS) 
命令功能 
该命令用于修改已添加的号码分析结果索引对应的Diameter GMLC局向标识和/或用户别名。 
待修改的号码分析结果索引可通过[SHOW DIMGMLC ANALYSIS]命令查询。
注意事项 
 
一个号码分析结果索引最多只能关联一个Diameter GMLC局向。 
 
 
一个Diameter GMLC局向可以关联多个号码分析结果索引。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数表示Diameter GMLC局向分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“GMLC邻接局分析”时，“号码分析结果索引”参数值引用本参数。
DIAMGMLCID|Diameter GMLC局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数表示号码分析结果索引所关联的Diameter GMLC局向标识，引用自Diameter GMLC局向配置ADD DIAMGMLCADJ中的“局向标识”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条GMLC号码分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
修改Diameter GMLC分析结果索引对应的GMLC局向标识，其中号码分析结果索引为1，将其关联的GMLC局向标识修改为3，用户别名为test。 
SET DIMGMLC ANALYSIS:IDX=1,DIAMGMLCID=3,NAME="test"; 
父主题： [Diameter GMLC分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除Diameter GMLC分析结果索引(DEL DIMGMLC ANALYSIS) 
### 删除Diameter GMLC分析结果索引(DEL DIMGMLC ANALYSIS) 
命令功能 
该命令用于删除已添加的Diameter GMLC分析结果索引。执行该命令后，号码分析结果索引和Diameter GMLC局向的关联关系被断开，从而使得移动号码分析中的号码不再关联到Diameter GMLC局向上。 
注意事项 
如果Diameter GMLC分析结果索引已经被移动号码分析引用（查询命令参见[SHOW MDNAL]），该分析结果索引不能被删除。必须先删除移动号码分析表中与该diameter GMLC分析结果索引对应的记录（删除命令参见[DEL MDNAL]），然后才能使用本命令删除Diameter GMLC分析结果索引。
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数表示Diameter GMLC局向分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“GMLC邻接局分析”时，“号码分析结果索引”参数值引用本参数。
命令举例 
删除号码分析结果索引为1的Diameter GMLC分析结果索引配置。 
DEL DIMGMLC ANALYSIS:IDX=1; 
父主题： [Diameter GMLC分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询Diameter GMLC分析结果索引(SHOW DIMGMLC ANALYSIS) 
### 查询Diameter GMLC分析结果索引(SHOW DIMGMLC ANALYSIS) 
命令功能 
该命令用于查询Diameter GMLC分析结果索引。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|该参数表示Diameter GMLC局向分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“GMLC邻接局分析”时，“号码分析结果索引”参数值引用本参数。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数。|该参数表示Diameter GMLC局向分析结果索引，在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“GMLC邻接局分析”时，“号码分析结果索引”参数值引用本参数。
DIAMGMLCID|Diameter GMLC局向标识|参数可选性:任选参数；参数类型:整数。|该参数表示号码分析结果索引所关联的Diameter GMLC局向标识，引用自Diameter GMLC局向配置ADD DIAMGMLCADJ中的“局向标识”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示一条GMLC号码分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
查询号码分析结果索引为1的Diameter GMLC分析结果索引配置。 
SHOW DIMGMLC ANALYSIS:IDX=1; 
`
命令 (No.1):SHOW DIMGMLC ANALYSIS:IDX=1;
操作维护         号码分析结果索引   Diameter GMLC局向标识   用户别名
--------------------------------------------------------------------
复制 修改 删除   1                  1                       test
--------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
 ` 
父主题： [Diameter GMLC分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## Diameter SMC分析结果索引配置 
## Diameter SMC分析结果索引配置 
背景知识 
根据SMC网元号码分析得到SMC局向，MME进行定位业务时，根据SMC网元号码分析得到SMC局向，向SMC发送消息。 
功能描述 
根据“移动号码分析”配置中得到结果索引，得到SMC局向ID。 
                Diameter SMC分析结果索引中配置索引对应的SMC局向号。Diameter SMC分析结果索引在移动号码分析配置（
                [ADD MDNAL]
                ）中被引用。
            
                当MME发起LCS定位业务时，MME根据用户签约的SMC号码在移动号码分析配置（
                [ADD MDNAL]
                ）中匹配被分析号码，获取SMC号码对应的Diameter SMC分析结果索引，然后根据此索引，在“Diameter SMC分析结果索引”配置中查找到对应的SMC局向号。
            
相关主题 
 
新增Diameter SMC分析结果索引(ADD DIMSMC ANALYSIS)
 
 
修改Diameter SMC分析结果索引(SET DIMSMC ANALYSIS)
 
 
删除Diameter SMC分析结果索引(DEL DIMSMC ANALYSIS)
 
 
查询Diameter SMC分析结果索引(SHOW DIMSMC ANALYSIS)
 
 
父主题： [号码分析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增Diameter SMC分析结果索引(ADD DIMSMC ANALYSIS) 
### 新增Diameter SMC分析结果索引(ADD DIMSMC ANALYSIS) 
命令功能 
该命令用于增加Diameter SMC分析结果索引。当需要增加号码分析结果索引和Diameter SMC局向的关联关系时，使用该命令。新增成功后，可以间接地实现SMC号码段和Diameter SMC局向的关联。 
SMC号码段和Diameter SMC局向关联关系的配置流程如下： 
增加一个号码分析结果索引，并关联对应的Diameter SMC邻接局，配置命令参见[ADD DIMSMC ANALYSIS]。
增加移动号码分析，将号段与新增的号码分析结果索引关联，这样就间接实现了SMC号码段到Diameter SMC局向的关联。增加移动号码分析的命令参见[ADD MDNAL]。
注意事项 
 
配置前，需要在Diameter SMC局向配置中配置Diameter SMC局向。 配置命令参见 ADD DIAMSMCADJ。
 
 
一个号码分析结果索引最多只能关联一个Diameter SMC 局向。 
 
 
一个Diameter SMC 局向可以关联多个号码分析结果索引。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数表示Diameter SMC局向分析结果索引记录。
DIAMSMCID|Diameter SMC局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数表示号码分析结果索引所关联的Diameter SMC局向标识，其查询命令参见SHOW DIAMADJ。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条SMC号码分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
新增Diameter SMC分析结果索引，其中号码分析结果索引为1，SMC局向编号为1，用户别名为test。 
ADD DIMSMC ANALYSIS:IDX=1,DIAMSMCID=1,NAME="test"; 
父主题： [Diameter SMC分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改Diameter SMC分析结果索引(SET DIMSMC ANALYSIS) 
### 修改Diameter SMC分析结果索引(SET DIMSMC ANALYSIS) 
命令功能 
该命令用于修改Diameter SMC分析结果索引。 
待修改的号码分析结果索引可通过[SHOW DIMSMC ANALYSIS]命令查询。
注意事项 
 
一个号码分析结果索引最多只能关联到一个Diameter SMC 局向。 
 
 
一个Diameter SMC 局向可以关联到多个号码分析结果索引。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数表示Diameter SMC局向分析结果索引记录。
DIAMSMCID|Diameter SMC局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数表示号码分析结果索引所关联的Diameter SMC局向标识，其查询命令参见SHOW DIAMADJ。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条SMC号码分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
设置Diameter SMC分析结果索引，其中号码分析结果索引为1，将SMC 局向编号修改为2，用户别名为test。 
SET DIMSMC ANALYSIS:IDX=1,DIAMSMCID=2,NAME="test"; 
父主题： [Diameter SMC分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除Diameter SMC分析结果索引(DEL DIMSMC ANALYSIS) 
### 删除Diameter SMC分析结果索引(DEL DIMSMC ANALYSIS) 
命令功能 
该命令用于删除Diameter SMC分析结果索引。执行该命令后，号码分析结果索引和diameter SMC局向的关联关系被断开，从而使得移动号码分析中的号码不再关联到Diameter SMC局向上。
注意事项 
如果Diameter SMC分析结果索引已经被移动号码分析引用（查询命令参见[SHOW MDNAL]），该分析结果索引不能被删除。必须先删除移动号码分析表中与该diameter SMC分析结果索引对应的记录（其删除命令参见[DEL MDNAL]），然后才能删除SMC分析结果索引。
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该参数表示Diameter SMC局向分析结果索引记录。
命令举例 
删除号码分析结果索引为1的Diameter SMC分析结果索引配置。 
DEL DIMSMC ANALYSIS:IDX=1; 
父主题： [Diameter SMC分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询Diameter SMC分析结果索引(SHOW DIMSMC ANALYSIS) 
### 查询Diameter SMC分析结果索引(SHOW DIMSMC ANALYSIS) 
命令功能 
该命令用于查询Diameter SMC分析结果索引。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|该参数表示Diameter SMC局向分析结果索引记录。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数。|该参数表示Diameter SMC局向分析结果索引记录。
DIAMSMCID|Diameter SMC局向标识|参数可选性:任选参数；参数类型:整数。|该参数表示号码分析结果索引所关联的Diameter SMC局向标识，其查询命令参见SHOW DIAMADJ。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示一条SMC号码分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
查询号码分析结果索引为1的DiameterSMC分析结果索引配置。 
SHOW DIMSMC ANALYSIS:IDX=1; 
`
命令 (No.1):SHOW DIMSMC ANALYSIS:IDX=1;
操作维护         号码分析结果索引   Diameter SMC局向标识   用户别名
--------------------------------------------------------------------
复制 修改 删除   1                  1                       test
--------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
 ` 
父主题： [Diameter SMC分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## Diameter消息分析结果索引配置 
## Diameter消息分析结果索引配置 
背景知识 
MME/SGSN进行附着和TAU等业务时，需要发送Diameter的ULR消息到HSS，当有某些特殊需要（例如：控制Diameter消息中AVP头、控制AVP头中的标记位是否携带、实现不同用户具有不同的Support Feature能力等）时，可以在发消息至HSS前根据IMSI选择对应AVP编辑策略和Support Feature模板编辑ULR消息。 
功能描述 
本配置用于配置“号码分析结果索引”对应的“AVP Profile标识”和“Support Feature ID”。 
 
                        在移动号码分析配置
                        ADD MDNAL
                        中，当“分析器入口”选择“Diameter消息编辑策略分析”时，“号码分析结果索引”参数值引用本配置中的“号码分析结果索引”。
                    
 
 
                        “AVP Profile标识”引用自Diameter AVP Profile配置
                        ADD DIM AVP PROFILE
                        中的Profile标识参数。“Support Feature ID”引用自Support Feature配置
                        ADD SUPFEATURE
                        命令中的Feature ID参数。
                    
 
 
当MME/SGSN发起附着或者TAU时，MME/SGSN根据用户的IMSI在移动号码分析中匹配被分析号码，获取IMSI对应的Diameter消息分析结果索引，然后根据此索引，在本配置中查找对应的AVP编辑策略和Support Feature模板，编辑ULR消息。 
相关主题 
 
新增Diameter消息分析结果索引(ADD DIMMEG ANALYSIS)
 
 
修改Diameter消息分析结果索引(SET DIMMEG ANALYSIS)
 
 
删除Diameter消息分析结果索引(DEL DIMMEG ANALYSIS)
 
 
查询Diameter消息分析结果索引(SHOW DIMMEG ANALYSIS)
 
 
父主题： [号码分析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增Diameter消息分析结果索引(ADD DIMMEG ANALYSIS) 
### 新增Diameter消息分析结果索引(ADD DIMMEG ANALYSIS) 
命令功能 
该命令用于增加Diameter消息分析结果索引，以便被移动号码分析配置[ADD MDNAL]引用。
当需要增加消息分析结果索引和AVP编辑策略及Support Feature模板的关联关系时，使用该命令。命令执行成功后，可以间接地实现移动号码段和AVP编辑策略及Support Feature模板的关联。 
移动号码段和AVP编辑策略及Support Feature模板关联关系的配置流程如下： 
使用本命令增加一个Diameter消息分析结果索引，并关联对应的AVP编辑策略及Support Feature模板。 
使用[ADD MDNAL]命令增加移动号码分析，分析入口选择Diameter消息编辑策略分析，将被分析号码（移动号码段）与新增的Diameter消息分析结果索引关联，这样就间接实现了移动号码段和AVP编辑策略及Support Feature模板的关联。
注意事项 
 
Diameter消息分析结果索引对应的AVP编辑策略，需要先在Diameter AVP Profile配置ADD DIM AVP PROFILE中配置。
 
 
Diameter消息分析结果索引对应的Support Feature模板，需要先在Support Feature配置ADD SUPFEATURE中配置。 
 
 
AVP编辑策略ID和Support Feature模板ID要求至少有一个不为0。当AVP编辑策略ID或Support Feature模板ID为0时，表示此项无效，即不关联此项。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数为Diameter消息分析结果索引，全局唯一。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter消息编辑策略分析”时，“号码分析结果索引”参数值引用本参数。
AVPPROID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于指示AVP Profile编辑策略ID。此参数引用自ADD DIM AVP PROFILE命令中Profile标识参数，取值为0表示没有关联的AVP编辑策略。
FEATID|Support Feature ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|该参数用于指示Support Feature模板ID。此参数引用自Support Feature配置ADD SUPFEATURE命令中Feature ID参数，取值为0表示没有关联的Feature模板。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条Diameter消息分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
新增Diameter消息分析结果索引，其中号码分析结果索引为1，AVP Profile标识为2，Support Feature ID为3。 
ADD DIMMEG ANALYSIS:IDX=1,AVPPROID=2,FEATID=3; 
父主题： [Diameter消息分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改Diameter消息分析结果索引(SET DIMMEG ANALYSIS) 
### 修改Diameter消息分析结果索引(SET DIMMEG ANALYSIS) 
命令功能 
本命令用于修改已添加的Diameter消息分析结果索引对应的AVP编辑策略及Support Feature模板。 
待修改的Diameter消息分析结果索引可通过[SHOW DIMMEG ANALYSIS]命令查询。
注意事项 
 
Diameter消息分析结果索引对应的AVP编辑策略，需要先在Diameter AVP Profile配置ADD DIM AVP PROFILE中配置。
 
 
Diameter消息分析结果索引对应的Support Feature模板，需要先在Support Feature配置ADD SUPFEATURE中配置。
 
 
AVP编辑策略ID和Support Feature模板ID要求至少有一个不为0。不能将两个项都修改为０（如不需要关联AVP编辑策略和Support Feature模板中的任何一个，则可以通过删除命令DEL DIMMEG ANALYSIS实现）。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数为Diameter消息分析结果索引，全局唯一。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter消息编辑策略分析”时，“号码分析结果索引”参数值引用本参数。
AVPPROID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于指示AVP Profile编辑策略ID。此参数引用自ADD DIM AVP PROFILE命令中Profile标识参数，取值为0表示没有关联的AVP编辑策略。
FEATID|Support Feature ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|该参数用于指示Support Feature模板ID。此参数引用自Support Feature配置ADD SUPFEATURE命令中Feature ID参数，取值为0表示没有关联的Feature模板。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示一条Diameter消息分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
修改Diameter消息分析结果索引对应的AVP Profile标识和Support Feature ID，其中号码分析结果索引为1，将其关联的AVP Profile标识修改为4，Support Feature ID修改为5。 
SET DIMMEG ANALYSIS:IDX=1,AVPPROID=4,FEATID=5; 
父主题： [Diameter消息分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除Diameter消息分析结果索引(DEL DIMMEG ANALYSIS) 
### 删除Diameter消息分析结果索引(DEL DIMMEG ANALYSIS) 
命令功能 
本命令用于删除已添加的Diameter消息分析结果索引。执行该命令后，消息编辑策略分析结果索引和AVP修改策略及Support Feature模板的关联关系就被断开。 
注意事项 
如果Diameter消息编辑策略分析结果索引已经被移动号码分析引用（查询命令参见[SHOW MDNAL]），该分析结果索引不能被删除。必须先删除移动号码分析表中与该Diameter消息编辑策略分析结果索引对应的记录（删除命令参见[DEL MDNAL]），然后才能使用本命令删除Diameter消息编辑策略分析结果索引。
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数为Diameter消息分析结果索引，全局唯一。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter消息编辑策略分析”时，“号码分析结果索引”参数值引用本参数。
命令举例 
删除号码分析结果索引为1的配置数据。 
DEL DIMMEG ANALYSIS:IDX=1; 
父主题： [Diameter消息分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询Diameter消息分析结果索引(SHOW DIMMEG ANALYSIS) 
### 查询Diameter消息分析结果索引(SHOW DIMMEG ANALYSIS) 
命令功能 
本命令用于显示已添加的Diameter消息分析结果索引。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数为Diameter消息分析结果索引，全局唯一。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter消息编辑策略分析”时，“号码分析结果索引”参数值引用本参数。
AVPPROID|AVP Profile标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~16。|该参数用于指示AVP Profile编辑策略ID。此参数引用自ADD DIM AVP PROFILE命令中Profile标识参数，取值为0表示没有关联的AVP编辑策略。
FEATID|Support Feature ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|该参数用于指示Support Feature模板ID。此参数引用自Support Feature配置ADD SUPFEATURE命令中Feature ID参数，取值为0表示没有关联的Feature模板。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|号码分析结果索引|参数可选性:任选参数；参数类型:整数。|该参数为Diameter消息分析结果索引，全局唯一。在移动号码分析配置ADD MDNAL中，当“分析器入口”选择“Diameter消息编辑策略分析”时，“号码分析结果索引”参数值引用本参数。
AVPPROID|AVP Profile标识|参数可选性:任选参数；参数类型:整数。|该参数用于指示AVP Profile编辑策略ID。此参数引用自ADD DIM AVP PROFILE命令中Profile标识参数，取值为0表示没有关联的AVP编辑策略。
FEATID|Support Feature ID|参数可选性:任选参数；参数类型:整数。|该参数用于指示Support Feature模板ID。此参数引用自Support Feature配置ADD SUPFEATURE命令中Feature ID参数，取值为0表示没有关联的Feature模板。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示一条Diameter消息分析结果索引的名称，由数字和英文字母组成的字符串表示。
命令举例 
查询所有的Diameter消息分析结果索引。 
SHOW DIMMEG ANALYSIS; 
`
命令 (No.24): SHOW DIMMEG ANALYSIS
操作维护      号码分析结果索引 AVP Profile标识   Support Feature ID 用户别名 
-----------------------------------------------------------------------------------
复制 修改 删除    1                 1               4  
-----------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [Diameter消息分析结果索引配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## TAI映射LAI配置 
## TAI映射LAI配置 
背景知识 
EPC网络对用户的位置管理采用跟踪区TA（Tracking Area）， 跟踪区的划分由无线侧确定。 
MSC/VLR对用户的位置管理采用位置区LA（Location Area），位置区的划分由无线侧确定。 
一般一个跟踪区属于一个位置区管理，但是当多个运营商共享同样的LTE网络时，会存在一个TAI对应多个运营商不同的LAI；同一个运营商网络下，用户在大区间/省间漫游时，为了避免对拜访地MSC/VLR的资源占用，为用户选择归属地MSC/VLR，也会存在一个TAI对应多个不同归属地的LAI。 
功能描述 
当MME支持SGs接口时，需要配置TAI与LAI的映射关系。如果一个TAI对应多个LAI，可以灵活配置TAI映射LAI的策略，包括： 
 
基于号段和TAI映射LAI配置。
 
 
基于HSS主机名和TAI映射LAI配置。
 
 
“基于HSS主机名和TAI映射LAI配置”与“基于号段和TAI映射LAI配置”同时开启时，MME优先使用号段和TAI获取映射的LAI，如果获取LAI失败再使用HSS主机名和TAI获取映射的LAI。 
相关主题 
 
基于号段和TAI映射LAI配置
 
 
基于HSS主机名和TAI映射LAI配置
 
 
父主题： [号码分析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于号段和TAI映射LAI配置 
### 基于号段和TAI映射LAI配置 
背景知识 
EPC网络对用户的位置管理采用跟踪区TA（Tracking Area）， 跟踪区的划分由无线侧确定。 
MSC/VLR对用户的位置管理是采用位置区LA(Location Area)，位置区的划分由无线侧确定。 
一般一个跟踪区属于一个位置区管理，但是当多个运营商共享同样的LTE网络时，会存在一个TAI对应多个运营商不同的LAI。 
跟踪区标识TAI（Tracking Area Identity )由MCC、MNC、TAC（Tracking Area Code）组成，一般运营商对于TAC的编码方式都有明确的规定，需要提前确定TAC的分配和编码，在运营中较少改动。 
功能描述 
当MME支持SGs接口时，需要配置跟踪区与LAI的映射关系，如果一个TAI对应多个LAI，通过此配置来达到由IMSI/MSISDN+TAI确定LAI的目的。包括： 
 
基于号段和TAI映射LAI策略配置。
 
 
基于号段和TAI映射LAI配置。
 
 
该命令所配置的LAI映射键值索引用于代表一个IMSI/MSISDN或者IMSI/MSISDN号段。 
                该命令所配置的跟踪区标识需要先通过命令
                [ADD TA]
                进行配置。
            
                该命令所配置的位置区名需要先通过命令
                [ADD LAI]
                进行配置。
            
                需要通过命令
                [SET IMSITAITOLAI POLICY]
                打开“支持基于IMSI和TAI映射LAI”开关，基于IMSI和TAI映射LAI配置才能够生效；打开“支持基于MSISDN和TAI映射LAI”开关，基于MSISDN和TAI映射LAI配置才能够生效。
            
相关主题 
 
设置基于号段和TAI映射LAI策略配置(SET IMSITAITOLAI POLICY)
 
 
查询基于号段和TAI映射LAI策略配置(SHOW IMSITAITOLAI POLICY)
 
 
新增基于号段和TAI映射LAI配置(ADD IMSITAITOLAI)
 
 
修改基于号段和TAI映射LAI配置(SET IMSITAITOLAI)
 
 
删除基于号段和TAI映射LAI配置(DEL IMSITAITOLAI)
 
 
查询基于号段和TAI映射LAI配置(SHOW IMSITAITOLAI)
 
 
父主题： [TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置基于号段和TAI映射LAI策略配置(SET IMSITAITOLAI POLICY) 
#### 设置基于号段和TAI映射LAI策略配置(SET IMSITAITOLAI POLICY) 
命令功能 
该命令用于设置基于号段和TAI映射LAI策略配置，包括是否支持基于IMSI和TA映射LAI、是否支持基于MSISDN和TA映射LAI。当运营商希望根据不同的IMSI/MSISDN和TAI映射出不同的LAI时，执行该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPIMSITAITOLAI|支持基于IMSI和TAI映射LAI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于IMSI和TAI映射LAI。在联合附着、联合跟踪区更新等流程中，当MME需要发送Location Update Request（位置更新请求）消息到MSC/VLR时，如果期望基于IMSI号段灵活选择MSC/VLR，则需要开启该功能。
SUPMSISDNTAITOLAI|支持基于MSISDN和TAI映射LAI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于MSISDN和TAI映射LAI。在联合附着、联合跟踪区更新等流程中，当MME需要发送Location Update Request（位置更新请求）消息到MSC/VLR时，如果期望基于MSISDN号段灵活选择MSC/VLR，则需要开启该功能。
命令举例 
将"支持基于IMSI和TAI映射LAI"和"支持基于MSISDN和TAI映射LAI"修改为"是"。 
SET IMSITAITOLAI POLICY:SUPIMSITAITOLAI="YES",SUPMSISDNTAITOLAI="YES" 
父主题： [基于号段和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于号段和TAI映射LAI策略配置(SHOW IMSITAITOLAI POLICY) 
#### 查询基于号段和TAI映射LAI策略配置(SHOW IMSITAITOLAI POLICY) 
命令功能 
该命令用于查询基于号段和TAI映射LAI策略配置。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPIMSITAITOLAI|支持基于IMSI和TAI映射LAI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于IMSI和TAI映射LAI。在联合附着、联合跟踪区更新等流程中，当MME需要发送Location Update Request（位置更新请求）消息到MSC/VLR时，如果期望基于IMSI号段灵活选择MSC/VLR，则需要开启该功能。
SUPMSISDNTAITOLAI|支持基于MSISDN和TAI映射LAI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于MSISDN和TAI映射LAI。在联合附着、联合跟踪区更新等流程中，当MME需要发送Location Update Request（位置更新请求）消息到MSC/VLR时，如果期望基于MSISDN号段灵活选择MSC/VLR，则需要开启该功能。
命令举例 
查询基于号段和TAI映射LAI策略配置 
SHOW IMSITAITOLAI POLICY 
`
(No.1) : SHOW IMSITAITOLAI POLICY
-----------------uMAC_MME_V7master/NFS_MMESGSN_0----------------
操作维护       支持基于IMSI和TAI映射LAI 支持基于MSISDN和TAI映射LAI 
-------------------------------------------------------------------
修改           否                       否                         
-------------------------------------------------------------------
记录数：1
命令执行成功（耗时 0.042 秒）。
` 
父主题： [基于号段和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增基于号段和TAI映射LAI配置(ADD IMSITAITOLAI) 
#### 新增基于号段和TAI映射LAI配置(ADD IMSITAITOLAI) 
命令功能 
该命令用于新增一个基于号段和TAI映射LAI的配置。当运营商希望根据不同的IMSI/MSISDN和TAI映射出不同的LAI时，使用此命令。该命令使用后，MME提供一个基于IMSI/MSISDN的LAI映射键值索引，并根据此映射索引与TAI组合映射出不同的LAI。 
注意事项 
 
该命令所配置的号码分析索引会被命令ADD MDNAL 所引用。
 
 
该命令所配置的跟踪区标识需要通过命令ADD TA进行配置。
 
 
该命令所配置的位置区名需要通过命令ADD LAI进行配置。
 
 
需要通过命令SET IMSITAITOLAI POLICY打开“支持基于IMSI和TAI映射LAI”开关，基于IMSI和TAI映射LAI配置才能够生效；打开“支持基于MSISDN和TAI映射LAI”开关，基于MSISDN和TAI映射LAI配置才能够生效。
 
 
“支持基于IMSI和TAI映射LAI”与“支持基于MSISDN和TAI映射LAI”同时开启时，MME优先使用IMSI和TAI获取映射的LAI，如果获取LAI失败再使用MSISDN和TAI获取映射的LAI。
 
 
“支持基于HSS主机名和TAI映射LAI”与“支持基于IMSI和TAI映射LAI”/“支持基于MSISDN和TAI映射LAI”同时开启时，MME优先使用IMSI/MSISN和TAI获取映射的LAI，如果获取LAI失败再使用HSS主机名和TAI获取映射的LAI。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|LAI映射键值索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于指定一个IMSI或MSISDN号码分析的索引值，与命令ADD MDNAL 中分析器入口选为DAS_IMSI_LAI或DAS_MSISDN_LAI 时的“号码分析结果索引”参数相对应。
TAIID|跟踪区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于指定要进行映射的跟踪区标识。
LAINAME|位置区名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|该参数用于指定映射后的位置区名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。
命令举例 
新增基于号段和TAI映射LAI配置，其中LAI映射键值索引为1、跟踪区标识为1、位置区名为lai1。 
ADD IMSITAITOLAI:IDX=1,TAIID=1,LAINAME="lai1" 
父主题： [基于号段和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改基于号段和TAI映射LAI配置(SET IMSITAITOLAI) 
#### 修改基于号段和TAI映射LAI配置(SET IMSITAITOLAI) 
命令功能 
该命令用于修改基于号段和TAI映射LAI的配置。当映射关系发生变化时使用此命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|LAI映射键值索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于指定一个IMSI或MSISDN号码分析的索引值，与命令ADD MDNAL 中分析器入口选为DAS_IMSI_LAI或DAS_MSISDN_LAI 时的“号码分析结果索引”参数相对应。
TAIID|跟踪区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于指定要进行映射的跟踪区标识。
LAINAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定映射后的位置区名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。
命令举例 
修改LAI映射键值索引为1、跟踪区标识为1的配置数据，将位置区名修改为lai2。 
SET IMSITAITOLAI:IDX=1,TAIID=1,LAINAME="lai2" 
父主题： [基于号段和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除基于号段和TAI映射LAI配置(DEL IMSITAITOLAI) 
#### 删除基于号段和TAI映射LAI配置(DEL IMSITAITOLAI) 
命令功能 
该命令用于删除基于号段和TAI映射LAI的配置。当不需要此映射关系时使用此命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|LAI映射键值索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~3072。|该参数用于指定一个IMSI或MSISDN号码分析的索引值，与命令ADD MDNAL 中分析器入口选为DAS_IMSI_LAI或DAS_MSISDN_LAI 时的“号码分析结果索引”参数相对应。
TAIID|跟踪区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于指定要进行映射的跟踪区标识。
命令举例 
删除LAI映射键值索引为1、跟踪区标识为1的配置数据。 
DEL IMSITAITOLAI:IDX=1,TAIID=1 
父主题： [基于号段和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于号段和TAI映射LAI配置(SHOW IMSITAITOLAI) 
#### 查询基于号段和TAI映射LAI配置(SHOW IMSITAITOLAI) 
命令功能 
该命令用于查询基于号段和TAI映射LAI的配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|LAI映射键值索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于指定一个IMSI或MSISDN号码分析的索引值，与命令ADD MDNAL 中分析器入口选为DAS_IMSI_LAI或DAS_MSISDN_LAI 时的“号码分析结果索引”参数相对应。
TAIID|跟踪区标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于指定要进行映射的跟踪区标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IDX|LAI映射键值索引|参数可选性:任选参数；参数类型:整数。|该参数用于指定一个IMSI或MSISDN号码分析的索引值，与命令ADD MDNAL 中分析器入口选为DAS_IMSI_LAI或DAS_MSISDN_LAI 时的“号码分析结果索引”参数相对应。
TAIID|跟踪区标识|参数可选性:任选参数；参数类型:整数。|该参数用于指定要进行映射的跟踪区标识。
LAINAME|位置区名|参数可选性:任选参数；参数类型:字符型。|该参数用于指定映射后的位置区名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|对此配置进行维护记录，起备注作用。
命令举例 
查询所有基于号段和TAI映射LAI配置 
SHOW IMSITAITOLAI 
`
命令 (No.21): SHOW IMSITAITOLAI
操作维护     LAI映射键值索引   跟踪区标识 位置区名 用户别名 
-------------------------------------------------------------------
复制 修改 删除  1               1             lai2  
-------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.042 秒）。
` 
父主题： [基于号段和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于HSS主机名和TAI映射LAI配置 
### 基于HSS主机名和TAI映射LAI配置 
背景知识 
EPC网络对用户的位置管理采用跟踪区TA（Tracking Area）， 跟踪区的划分由无线侧确定。 
MSC/VLR对用户的位置管理采用位置区LA（Location Area），位置区的划分由无线侧确定。 
一般一个跟踪区属于一个位置区管理，但是当多个运营商共享同样的LTE网络时，会存在一个TAI对应多个运营商不同的LAI；同一个运营商网络下，用户在大区间/省间漫游时，为了避免对拜访地MSC/VLR的资源占用，为用户选择归属地MSC/VLR，也会存在一个TAI对应多个不同归属地的LAI。 
功能描述 
当MME支持SGs接口时，需要配置TAI与LAI的映射关系。如果一个TAI对应多个LAI，通过此配置来达到由HSS主机名和TAI确定LAI的目的，包括： 
 
基于HSS主机名和TAI映射LAI策略配置。
 
 
基于HSS主机名的LAI映射索引配置。
 
 
基于HSS主机名和TAI映射LAI配置。
 
 
相关主题 
 
设置基于HSS主机名和TAI映射LAI策略配置(SET HSSTAITOLAI POLICY)
 
 
查询基于HSS主机名和TAI映射LAI策略配置(SHOW HSSTAITOLAI POLICY)
 
 
新增基于HSS主机名和TAI映射LAI配置(ADD HSSTAITOLAI)
 
 
修改基于HSS主机名和TAI映射LAI配置(SET HSSTAITOLAI)
 
 
删除基于HSS主机名和TAI映射LAI配置(DEL HSSTAITOLAI)
 
 
查询基于HSS主机名和TAI映射LAI配置(SHOW HSSTAITOLAI)
 
 
新增基于HSS主机名的LAI映射索引配置(ADD HSSLAITOINDEX)
 
 
修改基于HSS主机名的LAI映射索引配置(SET HSSLAITOINDEX)
 
 
删除基于HSS主机名的LAI映射索引配置(DEL HSSLAITOINDEX)
 
 
查询基于HSS主机名的LAI映射索引配置(SHOW HSSLAITOINDEX)
 
 
父主题： [TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置基于HSS主机名和TAI映射LAI策略配置(SET HSSTAITOLAI POLICY) 
#### 设置基于HSS主机名和TAI映射LAI策略配置(SET HSSTAITOLAI POLICY) 
命令功能 
该命令用于设置基于HSS主机名和TAI映射LAI策略配置。当运营商希望根据不同的HSS主机名和TAI映射出不同的LAI时，使用该命令进行配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPHOSTTAITOLAI|支持基于HSS主机名和TAI映射LAI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于HSS主机名和TAI映射LAI。联合附着/联合跟踪区更新等流程中，当MME需要发送Location Update Request（位置更新请求）消息到MSC/VLR时，如果期望基于HSS主机名灵活选择MSC/VLR，则需要开启该功能。
命令举例 
设置基于HSS主机名和TAI映射LAI策略配置，支持基于HSS主机名和TAI映射LAI为不支持。 
SET HSSTAITOLAI POLICY:SUPHOSTTAITOLAI="NO" 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于HSS主机名和TAI映射LAI策略配置(SHOW HSSTAITOLAI POLICY) 
#### 查询基于HSS主机名和TAI映射LAI策略配置(SHOW HSSTAITOLAI POLICY) 
命令功能 
该命令用于查询基于HSS主机名和TAI映射LAI策略配置。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPHOSTTAITOLAI|支持基于HSS主机名和TAI映射LAI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于HSS主机名和TAI映射LAI。联合附着/联合跟踪区更新等流程中，当MME需要发送Location Update Request（位置更新请求）消息到MSC/VLR时，如果期望基于HSS主机名灵活选择MSC/VLR，则需要开启该功能。
命令举例 
查询基于HSS主机名和TAI映射LAI策略配置。 
SHOW HSSTAITOLAI POLICY 
`
命令 (No.12): SHOW HSSTAITOLAI POLICY;
操作维护       支持基于HSS主机名和TAI映射LAI 
------------------------------------------
 修改          不支持                       
------------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增基于HSS主机名和TAI映射LAI配置(ADD HSSTAITOLAI) 
#### 新增基于HSS主机名和TAI映射LAI配置(ADD HSSTAITOLAI) 
命令功能 
该命令用于新增基于HSS主机名和TAI映射LAI的配置。当运营商希望根据不同的HSS主机名和TAI映射出不同的LAI时，使用此命令进行配置。该命令使用后，MME提供一个基于HSS主机名的LAI映射键值索引，并根据此映射索引与TAI组合映射出不同的LAI。 
注意事项 
 
该命令所配置的LAI映射键值索引，会被命令ADD HSSLAITOINDEX引用。
 
 
该命令所配置的跟踪区标识需要通过命令ADD TA进行配置。
 
 
该命令所配置的位置区名需要通过命令ADD LAI进行配置。
 
 
需要通过命令SET HSSTAITOLAI POLICY打开“支持基于HSS主机名和TAI映射LAI”开关，本配置才能够生效。
 
 
“支持基于HSS主机名和TAI映射LAI”与“支持基于IMSI和TAI映射LAI”/“支持基于MSISDN和TAI映射LAI”同时开启时，MME优先使用IMSI/MSISN和TAI获取映射的LAI，如果获取LAI失败再使用HSS主机名和TAI获取映射的LAI。
 
 
最多可输入65535条记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
LAIMAPIDX|LAI映射键值索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置HSS主机名对应的LAI映射键值索引，与命令ADD HSSLAITOINDEX中的“LAI映射键值索引”参数相对应。
TAIID|跟踪区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置要进行映射的跟踪区标识。
LAINAME|位置区名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|该参数用于配置映射后的位置区名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于对当前配置进行维护记录，起备注作用。
命令举例 
新增基于HSS主机名和TAI映射LAI配置，LAI映射键值索引为1，跟踪区标识为1，位置区名为lai1。 
ADD HSSTAITOLAI:LAIMAPIDX=1,TAIID=1,LAINAME="lai1" 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改基于HSS主机名和TAI映射LAI配置(SET HSSTAITOLAI) 
#### 修改基于HSS主机名和TAI映射LAI配置(SET HSSTAITOLAI) 
命令功能 
该命令用于修改基于HSS主机名和TAI映射LAI配置。当映射关系发生变化时使用此命令。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
LAIMAPIDX|LAI映射键值索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置HSS主机名对应的LAI映射键值索引，与命令ADD HSSLAITOINDEX中的“LAI映射键值索引”参数相对应。
TAIID|跟踪区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置要进行映射的跟踪区标识。
LAINAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|该参数用于配置映射后的位置区名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于对当前配置进行维护记录，起备注作用。
命令举例 
修改基于HSS主机名和TAI映射LAI配置，LAI映射键值索引为1，跟踪区标识为1，位置区名为lai2。 
SET HSSTAITOLAI:LAIMAPIDX=1,TAIID=1,LAINAME="lai2" 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除基于HSS主机名和TAI映射LAI配置(DEL HSSTAITOLAI) 
#### 删除基于HSS主机名和TAI映射LAI配置(DEL HSSTAITOLAI) 
命令功能 
该命令用于删除基于HSS主机名和TAI映射LAI配置。当不需要此映射关系时使用此命令。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
LAIMAPIDX|LAI映射键值索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置HSS主机名对应的LAI映射键值索引，与命令ADD HSSLAITOINDEX中的“LAI映射键值索引”参数相对应。
TAIID|跟踪区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置要进行映射的跟踪区标识。
命令举例 
删除基于HSS主机名和TAI映射LAI配置，LAI映射键值索引为1，跟踪区标识为1。 
DEL HSSTAITOLAI:LAIMAPIDX=1,TAIID=1 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于HSS主机名和TAI映射LAI配置(SHOW HSSTAITOLAI) 
#### 查询基于HSS主机名和TAI映射LAI配置(SHOW HSSTAITOLAI) 
命令功能 
该命令用于查询基于HSS主机名和TAI映射LAI的配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
LAIMAPIDX|LAI映射键值索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置HSS主机名对应的LAI映射键值索引，与命令ADD HSSLAITOINDEX中的“LAI映射键值索引”参数相对应。
TAIID|跟踪区标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置要进行映射的跟踪区标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LAIMAPIDX|LAI映射键值索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置HSS主机名对应的LAI映射键值索引，与命令ADD HSSLAITOINDEX中的“LAI映射键值索引”参数相对应。
TAIID|跟踪区标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置要进行映射的跟踪区标识。
LAINAME|位置区名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|该参数用于配置映射后的位置区名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于对当前配置进行维护记录，起备注作用。
命令举例 
查询基于HSS主机名和TAI映射LAI配置，LAI映射键值索引为1，跟踪区标识为1。 
SHOW HSSTAITOLAI:LAIMAPIDX=1,TAIID=1 
`
命令 (No.12): SHOW HSSTAITOLAI:LAIMAPIDX=1,TAIID=1
操作维护       LAI映射键值索引 跟踪区标识 位置区名 用户别名 
--------------------------------------------------------
复制 修改 删除 1               1         lai1           
-------------------------------------------------------- 
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增基于HSS主机名的LAI映射索引配置(ADD HSSLAITOINDEX) 
#### 新增基于HSS主机名的LAI映射索引配置(ADD HSSLAITOINDEX) 
命令功能 
该命令用于新增基于HSS主机名的LAI映射索引配置，先将HSS主机名映射到一个索引，然后再和TAI组合映射得到LAI。当运营商希望根据不同的HSS主机名和TAI映射出不同的LAI时，使用此命令。 
注意事项 
 
该命令所配置的LAI映射键值索引需要通过命令ADD HSSTAITOLAI进行配置。
 
 
最多可输入1024条记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
HSSHOSTNAME|HSS主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于配置HSS主机名。
LAIMAPIDX|LAI映射键值索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置HSS主机名对应的LAI映射键值索引，该索引值在命令ADD HSSTAITOLAI中已配置。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于对当前配置进行维护记录，起备注作用。
命令举例 
新增基于HSS主机名的LAI映射索引配置，HSS主机名为host1，LAI映射键值索引为1，别名为test1。 
ADD HSSLAITOINDEX:HSSHOSTNAME="host1",LAIMAPIDX=1,NAME="test1" 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改基于HSS主机名的LAI映射索引配置(SET HSSLAITOINDEX) 
#### 修改基于HSS主机名的LAI映射索引配置(SET HSSLAITOINDEX) 
命令功能 
该命令用于修改基于HSS主机名的LAI映射索引配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
HSSHOSTNAME|HSS主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于配置HSS主机名。
LAIMAPIDX|LAI映射键值索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置HSS主机名对应的LAI映射键值索引，该索引值在命令ADD HSSTAITOLAI中已配置。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于对当前配置进行维护记录，起备注作用。
命令举例 
修改基于HSS主机名的LAI映射索引配置，HSS主机名为host1，LAI映射键值索引为2，别名为test2。 
SET HSSLAITOINDEX:HSSHOSTNAME="host1",LAIMAPIDX=2,NAME="test2" 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除基于HSS主机名的LAI映射索引配置(DEL HSSLAITOINDEX) 
#### 删除基于HSS主机名的LAI映射索引配置(DEL HSSLAITOINDEX) 
命令功能 
该命令用于删除基于HSS主机名的LAI映射索引配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
HSSHOSTNAME|HSS主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于配置HSS主机名。
命令举例 
删除基于HSS主机名的LAI映射索引配置，HSS主机名为host1。 
DEL HSSLAITOINDEX:HSSHOSTNAME="host1" 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于HSS主机名的LAI映射索引配置(SHOW HSSLAITOINDEX) 
#### 查询基于HSS主机名的LAI映射索引配置(SHOW HSSLAITOINDEX) 
命令功能 
该命令用于查询基于HSS主机名的LAI映射索引配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
HSSHOSTNAME|HSS主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于配置HSS主机名。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
HSSHOSTNAME|HSS主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于配置HSS主机名。
LAIMAPIDX|LAI映射键值索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置HSS主机名对应的LAI映射键值索引，该索引值在命令ADD HSSTAITOLAI中已配置。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于对当前配置进行维护记录，起备注作用。
命令举例 
查询基于HSS主机名的LAI映射索引配置，HSS主机名为host1。 
SHOW HSSLAITOINDEX:HSSHOSTNAME="host1" 
`
命令 (No.12): SHOW HSSLAITOINDEX:HSSHOSTNAME="host1"
操作维护       HSS主机名 LAI映射键值索引  用户别名 
------------------------------------------------
复制 修改 删除  host1     1               test1  
------------------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [基于HSS主机名和TAI映射LAI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 移动号码分析 
## 移动号码分析 
背景知识 
SGSN在提供Gn/Gp接口时，进行附着和RAU等业务，向HLR发送消息时，需要根据IMSI查询HLR的目的地址。 
SGSN在提供S3/S4接口时，进行附着和TAU等业务，向HSS发送消息时，需要根据IMSI查询Diameter局向。 
MME进行附着和TAU等业务，向HSS发送消息时，需要根据IMSI查询Diameter局向。 
MME进行定位业务，向GMLC发送消息时，需要根据GMLC网元号码查询GMLC局向。 
MME进行附着和TAU等业务，发送Diameter的ULR消息时，需要根据IMSI选择对应的AVP修改策略和Support Feature模块编辑ULR消息。 
MME进行联合附着和TAU等业务， 需要根据IMSI/MSISDN+TAI获取MSC/VLR的LAI信息。 
MME进行寻呼时，需要根据IMSI和其他因子获取寻呼策略。 
MME进行寻呼时，需要根据MSISDN和其他因子获取寻呼策略。 
MME进行寻呼时，需要根据IMEI和其他因子获取寻呼策略。 
功能描述 
移动号码分析中，配置被分析的IMSI、IMEI、MSISDN或者GMLC网元号码，并配置号码分析结果索引。此索引需要先在“移动号码分析结果索引”、“Diameter邻接局分析结果索引”、“Diameter GMLC分析结果索引配置”、“Diameter 消息编辑策略分析结果索引配置”、“基于号段和TAI映射LAI配置”和“MME寻呼策略因子配置”中进行配置。 
号码分析器是被分析号码的集合，根据被分析号码的业务类型，分为以下几类号码分析器入口。 
 
IMSI号码分析：用于SGSN分析IMSI号码或号段。
 
 
Diameter邻接局分析：用于MME/SGSN分析Diameter网元号码。
 
 
GMLC邻接局分析：用于MME分析GMLC网元号码。
 
 
Diameter消息编辑策略分析：用于MME分析用户使用的Diameter消息编辑策略。
 
 
IMSI LAI映射键值分析：用于MME基于IMSI号码或号段分析LAI号码。
 
 
MSISDN LAI映射键值分析：用于MME基于MSISDN号码或号段分析LAI号码。
 
 
IMSI寻呼策略分析：用于MME分析寻呼的IMSI号码或号段。
 
 
IMEI寻呼策略分析：用于MME分析寻呼的IMEI号码或号段。
 
 
MSISDN寻呼策略分析：用于MME分析寻呼的MSISDN号码或号段
 
 
相关主题 
 
新增移动号码分析(ADD MDNAL)
 
 
修改移动号码分析(SET MDNAL)
 
 
删除移动号码分析(DEL MDNAL)
 
 
查询移动号码分析(SHOW MDNAL)
 
 
查询移动号码归属域名信息(SHOW MDN2REALM)
 
 
父主题： [号码分析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增移动号码分析(ADD MDNAL) 
### 新增移动号码分析(ADD MDNAL) 
命令功能 
该命令用于新增移动号码分析。 
当SGSN需要分析IMSI，得到HLR局向；MME/SGSN需要分析IMSI，得到Diameter局向；MME需要分析GMLC网元号码，得到GMLC邻接局向；MME需要分析IMSI，得到Diameter消息编辑策略；MME需要分析IMSI/MSISDN+TAI，得到MSC/VLR的LAI信息；MME需要分析IMSI/IMEI/MSISDN，得到寻呼策略时，MME需要分析IMSI，得到QOS控制策略和QOS控制参数上限时，使用该命令。 
命令执行成功后，MME/SGSN就能根据移动号码，通过不同的分析器，得到不同的号码分析结果索引，最终得到HLR/Diamete/GMLC局向、Diameter消息编辑策略、MSC/VLR的LAI信息、寻呼策略、QOS控制策略和QOS控制参数上限。 
注意事项 
 
该命令需要将某移动号码段分析到HLR局向时，需要配置分析器入口为IMSI号码分析，并且配置命令ADD IROAM，得到号码分析结果索引。
 
 
该命令需要将某移动号码段分析到HSS局向时，需要配置分析器入口为Diameter邻接局分析，并且配置命令ADD DIMOFC ANALYSIS，得到号码分析结果索引。
 
 
该命令需要将某移动号码段分析到GMLC局向时，需要配置分析器入口为GMLC邻接局分析，并且配置命令ADD DIMGMLC ANALYSIS（该命令只适用于MME网元），得到号码分析结果索引。 
 
 
该命令需要将某移动号码段分析到Diameter消息编辑策略时，需要配置分析器入口为Diameter消息编辑策略分析，并且配置命令ADD DIMMEG ANALYSIS（该命令只适用于MME网元），得到号码分析结果索引。
 
 
该命令需要将某移动号码段（IMSI）分析到LAI映射键值时，需要配置分析器入口为IMSI LAI映射键值分析，并且配置命令ADD IMSITAITOLAI（该命令只适用于MME网元），得到号码分析结果索引。
 
 
该命令需要将某移动号码段（MSISDN）分析到LAI映射键值时，需要配置分析器入口为MSISDN LAI映射键值分析，并且配置命令ADD IMSITAITOLAI（该命令只适用于MME网元），得到号码分析结果索引。
 
 
该命令需要将某移动号码（IMSI）段分析到寻呼策略映射键值时，需要配置分析器入口为IMSI寻呼策略映射键值分析，并且配置命令ADD MME PAGING POLICY FACTOR（该命令只适用于MME网元），得到号码分析结果索引。由于基于用户号码的寻呼策略，用户的号码只使用IMSI或MSISDN中的一种，所以该分析器入口的号码分析结果索引与分析器入口“MSISDN寻呼策略分析”使用的号码分析结果索引不能重复。
 
 
该命令需要将某移动号码（MSISDN）段分析到寻呼策略映射键值时，需要配置分析器入口为MSISDN寻呼策略映射键值分析，并且配置命令ADD MME PAGING POLICY FACTOR（该命令只适用于MME网元），得到号码分析结果索引。由于基于用户号码的寻呼策略，用户的号码只使用IMSI或MSISDN中的一种，所以该分析器入口的号码分析结果索引与分析器入口“IMSI寻呼策略分析”使用的号码分析结果索引不能重复。
 
 
该命令需要将某IMEI号段分析到寻呼策略映射键值时，需要配置分析器入口为IMEI寻呼策略映射键值分析，并且配置命令ADD MME PAGING POLICY FACTOR（该命令只适用于MME网元），得到号码分析结果索引。
 
 
该命令需要将某IMSI号段分析到QOS控制策略映射键值时，需要配置分析器入口为IMSI QoS控制分析，并且配置命令ADD IMSI QOS POLICY或ADD SUBSRIBER LEVEL QOS或ADD SESSION LEVEL QOS或ADD BEARER LEVEL QOS（该命令只适用于MME网元），得到号码分析结果索引。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
DGT|被分析号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~20个字符。|该参数用于指定需要进行号码分析的IMSI、MSISDN、IMEI、或者GMLC网元号码。
ENTR|分析器入口|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定号码分析对应的分析器入口。不同的分析器入口对应了不同的分析类型。取值含义：IMSI号码分析（DAS_IMSI_ROAM）：IMSI号码分析，入口对应局向类型为HLR。Diameter邻接局分析（DAS_IMSI_DIAMETER）：入口对应局向类型为HSS局向。GMLC邻接局分析（DAS_GMLC）：入口对应局向类型为GMLC局向。SMC邻接局分析（DAS_SMC）：入口对应局向类型为SMC局向。Diameter消息编辑策略分析（DAS_DIAMETER_EDIT）：入口对应Diameter消息的AVP编辑策略和Support Feature模板。IMSI LAI映射健值分析（DAS_IMSI_LAI）：IMSI号码分析，对应LAI映射健值索引。MSISDN LAI映射健值分析（DAS_IMSI_LAI）：MSISDN号码分析，对应LAI映射健值索引。IMSI寻呼策略分析（DAS_IMSI_PGPOLICY）：IMSI号码分析，对应寻呼策略因子映射健值索引。IMEI寻呼策略分析（DAS_IMEI_PGPOLICY）：IMEI号码分析，对应寻呼策略因子映射健值索引。MSISDN寻呼策略分析（DAS_MSISDN_PGPOLICY）：MSISDN号码分析，对应寻呼策略因子映射健值索引。IMSI节电策略分析（DAS_IMSI_PSM）：IMSI号码分析，对应节电策略因子映射健值索引。IMSI QoS控制分析(DAS_IMSI_QOSCONTROL)：IMSI号码分析，对应QOS控制策略映射键值索引。
RST|号码分析结果索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定号码分析对应的号码分析结果索引。基于分析器入口的取值，索引值在“移动号码分析结果索引”、“Diameter邻接局分析结果索引”、“Diameter GMLC分析结果索引配置”、“Diameter 消息编辑策略分析结果索引配置”、“基于号段和TAI映射LAI配置”或”MME寻呼策略因子配置“中配置。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表明该配置的实际含义，配置特定名称做为备注。
命令举例 
新增移动号码分析，被分析号码是46003，分析器入口是Diameter邻接局分析，号码分析结果索引是3，用户别名是test。 
ADD MDNAL:DGT="46003",ENTR="DAS_IMSI_DIAMETER",RST=3,NAME="test"; 
父主题： [移动号码分析]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改移动号码分析(SET MDNAL) 
### 修改移动号码分析(SET MDNAL) 
命令功能 
该命令用于修改移动号码分析。根据被分析号码和分析器入口，修改号码分析结果索引。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
DGT|被分析号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~20个字符。|该参数用于指定需要进行号码分析的IMSI、MSISDN、IMEI、或者GMLC网元号码。
ENTR|分析器入口|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定号码分析对应的分析器入口。不同的分析器入口对应了不同的分析类型。取值含义：IMSI号码分析（DAS_IMSI_ROAM）：IMSI号码分析，入口对应局向类型为HLR。Diameter邻接局分析（DAS_IMSI_DIAMETER）：入口对应局向类型为HSS局向。GMLC邻接局分析（DAS_GMLC）：入口对应局向类型为GMLC局向。SMC邻接局分析（DAS_SMC）：入口对应局向类型为SMC局向。Diameter消息编辑策略分析（DAS_DIAMETER_EDIT）：入口对应Diameter消息的AVP编辑策略和Support Feature模板。IMSI LAI映射健值分析（DAS_IMSI_LAI）：IMSI号码分析，对应LAI映射健值索引。MSISDN LAI映射健值分析（DAS_IMSI_LAI）：MSISDN号码分析，对应LAI映射健值索引。IMSI寻呼策略分析（DAS_IMSI_PGPOLICY）：IMSI号码分析，对应寻呼策略因子映射健值索引。IMEI寻呼策略分析（DAS_IMEI_PGPOLICY）：IMEI号码分析，对应寻呼策略因子映射健值索引。MSISDN寻呼策略分析（DAS_MSISDN_PGPOLICY）：MSISDN号码分析，对应寻呼策略因子映射健值索引。IMSI节电策略分析（DAS_IMSI_PSM）：IMSI号码分析，对应节电策略因子映射健值索引。IMSI QoS控制分析(DAS_IMSI_QOSCONTROL)：IMSI号码分析，对应QOS控制策略映射键值索引。
RST|号码分析结果索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定号码分析对应的号码分析结果索引。基于分析器入口的取值，索引值在“移动号码分析结果索引”、“Diameter邻接局分析结果索引”、“Diameter GMLC分析结果索引配置”、“Diameter 消息编辑策略分析结果索引配置”、“基于号段和TAI映射LAI配置”或”MME寻呼策略因子配置“中配置。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表明该配置的实际含义，配置特定名称做为备注。
命令举例 
修改移动号码分析，被分析号码是46003，分析器入口是Diameter邻接局分析，将号码分析结果索引修改为2。 
SET MDNAL:DGT="46003",ENTR="DAS_IMSI_DIAMETER",RST=2; 
父主题： [移动号码分析]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除移动号码分析(DEL MDNAL) 
### 删除移动号码分析(DEL MDNAL) 
命令功能 
该命令用于删除移动号码分析。根据被分析号码和分析器入口进行删除。当不需要对该IMSI、MSISDN、IMEI、或者GMLC网元号码进行号码分析时，执行该删除命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
DGT|被分析号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~20个字符。|该参数用于指定需要进行号码分析的IMSI、MSISDN、IMEI、或者GMLC网元号码。
ENTR|分析器入口|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定号码分析对应的分析器入口。不同的分析器入口对应了不同的分析类型。取值含义：IMSI号码分析（DAS_IMSI_ROAM）：IMSI号码分析，入口对应局向类型为HLR。Diameter邻接局分析（DAS_IMSI_DIAMETER）：入口对应局向类型为HSS局向。GMLC邻接局分析（DAS_GMLC）：入口对应局向类型为GMLC局向。SMC邻接局分析（DAS_SMC）：入口对应局向类型为SMC局向。Diameter消息编辑策略分析（DAS_DIAMETER_EDIT）：入口对应Diameter消息的AVP编辑策略和Support Feature模板。IMSI LAI映射健值分析（DAS_IMSI_LAI）：IMSI号码分析，对应LAI映射健值索引。MSISDN LAI映射健值分析（DAS_IMSI_LAI）：MSISDN号码分析，对应LAI映射健值索引。IMSI寻呼策略分析（DAS_IMSI_PGPOLICY）：IMSI号码分析，对应寻呼策略因子映射健值索引。IMEI寻呼策略分析（DAS_IMEI_PGPOLICY）：IMEI号码分析，对应寻呼策略因子映射健值索引。MSISDN寻呼策略分析（DAS_MSISDN_PGPOLICY）：MSISDN号码分析，对应寻呼策略因子映射健值索引。IMSI节电策略分析（DAS_IMSI_PSM）：IMSI号码分析，对应节电策略因子映射健值索引。IMSI QoS控制分析(DAS_IMSI_QOSCONTROL)：IMSI号码分析，对应QOS控制策略映射键值索引。
命令举例 
删除移动号码分析，被分析号码是46003，分析器入口是Diameter邻接局分析。 
DEL MDNAL:DGT="46003",ENTR="DAS_IMSI_DIAMETER"; 
父主题： [移动号码分析]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询移动号码分析(SHOW MDNAL) 
### 查询移动号码分析(SHOW MDNAL) 
命令功能 
该命令用于查询移动号码分析。当查询命令不携带任何参数时，查询的结果为所有配置记录；当查询条件为被分析号码或分析器入口时，查询结果为对应的配置记录。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
DGT|被分析号码(通配%)|参数可选性:任选参数；参数类型:字符型；参数范围为:1~20个字符。|该参数用于指定需要进行号码分析的IMSI、MSISDN、IMEI、或者GMLC网元号码。可以使用通配符%，表示所有的号码。
ENTR|分析器入口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定号码分析对应的分析器入口。不同的分析器入口对应了不同的分析类型。取值含义：IMSI号码分析（DAS_IMSI_ROAM）：IMSI号码分析，入口对应局向类型为HLR。Diameter邻接局分析（DAS_IMSI_DIAMETER）：入口对应局向类型为HSS局向。GMLC邻接局分析（DAS_GMLC）：入口对应局向类型为GMLC局向。SMC邻接局分析（DAS_SMC）：入口对应局向类型为SMC局向。Diameter消息编辑策略分析（DAS_DIAMETER_EDIT）：入口对应Diameter消息的AVP编辑策略和Support Feature模板。IMSI LAI映射健值分析（DAS_IMSI_LAI）：IMSI号码分析，对应LAI映射健值索引。MSISDN LAI映射健值分析（DAS_IMSI_LAI）：MSISDN号码分析，对应LAI映射健值索引。IMSI寻呼策略分析（DAS_IMSI_PGPOLICY）：IMSI号码分析，对应寻呼策略因子映射健值索引。IMEI寻呼策略分析（DAS_IMEI_PGPOLICY）：IMEI号码分析，对应寻呼策略因子映射健值索引。MSISDN寻呼策略分析（DAS_MSISDN_PGPOLICY）：MSISDN号码分析，对应寻呼策略因子映射健值索引。IMSI节电策略分析（DAS_IMSI_PSM）：IMSI号码分析，对应节电策略因子映射健值索引。IMSI QoS控制分析(DAS_IMSI_QOSCONTROL)：IMSI号码分析，对应QOS控制策略映射键值索引。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DGT|被分析号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~20个字符。|该参数用于指定需要进行号码分析的IMSI、MSISDN、IMEI、或者GMLC网元号码。可以使用通配符%，表示所有的号码。
ENTR|分析器入口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定号码分析对应的分析器入口。不同的分析器入口对应了不同的分析类型。取值含义：IMSI号码分析（DAS_IMSI_ROAM）：IMSI号码分析，入口对应局向类型为HLR。Diameter邻接局分析（DAS_IMSI_DIAMETER）：入口对应局向类型为HSS局向。GMLC邻接局分析（DAS_GMLC）：入口对应局向类型为GMLC局向。SMC邻接局分析（DAS_SMC）：入口对应局向类型为SMC局向。Diameter消息编辑策略分析（DAS_DIAMETER_EDIT）：入口对应Diameter消息的AVP编辑策略和Support Feature模板。IMSI LAI映射健值分析（DAS_IMSI_LAI）：IMSI号码分析，对应LAI映射健值索引。MSISDN LAI映射健值分析（DAS_IMSI_LAI）：MSISDN号码分析，对应LAI映射健值索引。IMSI寻呼策略分析（DAS_IMSI_PGPOLICY）：IMSI号码分析，对应寻呼策略因子映射健值索引。IMEI寻呼策略分析（DAS_IMEI_PGPOLICY）：IMEI号码分析，对应寻呼策略因子映射健值索引。MSISDN寻呼策略分析（DAS_MSISDN_PGPOLICY）：MSISDN号码分析，对应寻呼策略因子映射健值索引。IMSI节电策略分析（DAS_IMSI_PSM）：IMSI号码分析，对应节电策略因子映射健值索引。IMSI QoS控制分析(DAS_IMSI_QOSCONTROL)：IMSI号码分析，对应QOS控制策略映射键值索引。
RST|号码分析结果索引|参数可选性:任选参数；参数类型:整数。|该参数用于指定号码分析对应的号码分析结果索引。基于分析器入口的取值，索引值在“移动号码分析结果索引”、“Diameter邻接局分析结果索引”、“Diameter GMLC分析结果索引配置”、“Diameter 消息编辑策略分析结果索引配置”、“基于号段和TAI映射LAI配置”或”MME寻呼策略因子配置“中配置。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表明该配置的实际含义，配置特定名称做为备注。
命令举例 
查询已配置的移动号码分析。 
SHOW MDNAL; 
`
命令 (No.1): SHOW MDNAL
操作维护         被分析号码   分析器入口           号码分析结果索引   用户别名
------------------------------------------------------------------------------
复制 修改 删除   46003        Diameter邻接局分析   3                  test
------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [移动号码分析]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询移动号码归属域名信息(SHOW MDN2REALM) 
### 查询移动号码归属域名信息(SHOW MDN2REALM) 
命令功能 
该命令用于查询移动号码归属域名信息。当需要查询移动号码对应的Diameter局向或者Diameter GMLC局向的域名信息时，使用该命令。 
命令执行成功后，如果配置了分析器入口为“Diameter邻接局分析”或者“GMLC邻接局分析”的数据，就能查询到该号码对应的Diameter局向或者GMLC局向的域名信息。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
DGT|被分析号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~20个字符。|该参数用于指定需要进行号码分析的IMSI、MSISDN、IMEI、或者GMLC网元号码。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DGT|被分析号码|参数可选性:任选参数；参数类型:字符型。|该参数用于指定需要进行号码分析的IMSI、MSISDN、IMEI、或者GMLC网元号码。
REALM|域名|参数可选性:任选参数；参数类型:字符型。|该参数用于表示Diameter局向或者Diameter GMLC局向的域名。
命令举例 
查询移动号码归属域名信息。 
SHOW MDN2REALM; 
`
命令 (No.1): SHOW MDN2REALM
被分析号码     域名
-------------------
4601100000     zte.com.cn
-------------------
记录数 1
命令执行成功（耗时 0.054 秒）。
` 
父主题： [移动号码分析]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## EIR号码配置 
## EIR号码配置 
背景知识 
EIR即设备标识寄存器（Equipment Identity Register）。 
如果启用EIR功能，则需要进行该配置。EIR功能启用后，手机用户发起业务，SGSN将其IMEI发送给EIR，EIR将收到的IMEI与配置的白名单、黑名单、灰名单进行比较，把结果返回给SGSN，由SGSN决定是否允许该移动台设备进入网络。 
功能描述 
EIR号码配置中设置SGSN连接的EIR网元编号，SGSN使用此号码作为目的地址向EIR发送Check IMEI消息。 
当支持Check IMEI功能，需要进行如下前提配置： 
 
                        通过
                        SET COMBOCFG
                        命令，在本局移动数据配置中选择支持Gf口。
                    
 
 
                        通过
                        SET SOFTWARE PARAMETER
                        :PARAID=262150,PARAVALUE=1;命令，将安全变量“SGSN 是否获取IMEI(SV)”设置为非0。
                    
 
 
相关主题 
 
新增EIR号码(ADD EIRNUM)
 
 
删除EIR号码(DEL EIRNUM)
 
 
查询EIR号码(SHOW EIRNUM)
 
 
父主题： [号码分析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增EIR号码(ADD EIRNUM) 
### 新增EIR号码(ADD EIRNUM) 
命令功能 
该命令用于新增EIR号码。EIR号码为EIR设备码，GT翻译该EIR号码，得到EIR局向。SGSN通过配置该EIR号码，起到向该设备路由的作用。 
注意事项 
 
该命令所配置的EIR号码在SGSN只能配置一条记录，这意味着，一个SGSN只能对应一个EIR局向。
 
 
该命令配置的EIR号码,会被命令ADD GT所引用。通过ADD GT命令，可将EIR号码翻译为EIR局向。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
NUM|EIR号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~16个字符。|该参数为EIR设备码，用于指定EIR局向对应的ISDN号码。该参数会被命令ADD GT所引用，用于进行GT翻译。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定一个特定的名称，可以是该设备所在地名，第几个局点等。该参数起到备注作用。
命令举例 
新增EIR号码，EIR号码为563，用户别名为sdf。 
ADD EIRNUM:NUM="563",NAME="sdf"; 
父主题： [EIR号码配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除EIR号码(DEL EIRNUM) 
### 删除EIR号码(DEL EIRNUM) 
命令功能 
该命令用于删除EIR号码。如果SGSN配置EIR局向，那么EIR号码的配置起到向该设备路由的功能，所以在有EIR局向配置的前提下不要去删除该EIR号码。 
注意事项 
由于EIR号码会被命令[ADD GT]所引用，因此在删除该EIR号码之前，需要先通过[DEL GT]命令删除引用该EIR号码的GT翻译配置。
参数说明 
标识|名称|类型|说明
---|---|---|---
NUM|EIR号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~16个字符。|该参数为EIR设备码，用于指定EIR局向对应的ISDN号码。该参数会被命令ADD GT所引用，用于进行GT翻译。
命令举例 
删除EIR号码为563的配置。 
DEL EIRNUM:NUM="563"; 
父主题： [EIR号码配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询EIR号码(SHOW EIRNUM) 
### 查询EIR号码(SHOW EIRNUM) 
命令功能 
该命令用于查询EIR号码。由于SGSN只允许配置一条EIRNUM记录，所以查询时不需要填写任何内容，直接查询，便得到当前配置的EIRNUM记录。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NUM|EIR号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~16个字符。|该参数为EIR设备码，用于指定EIR局向对应的ISDN号码。该参数会被命令ADD GT所引用，用于进行GT翻译。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NUM|EIR号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|该参数为EIR设备码，用于指定EIR局向对应的ISDN号码。该参数会被命令ADD GT所引用，用于进行GT翻译。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定一个特定的名称，可以是该设备所在地名，第几个局点等。该参数起到备注作用。
命令举例 
查询已配置的EIR号码。 
SHOW EIRNUM; 
`
命令 (No.1): SHOW EIRNUM
操作维护    EIR号码   用户别名
------------------------------
复制 删除   563       sdf
------------------------------
记录数 1
命令执行成功（耗时 0.052 秒）。
` 
父主题： [EIR号码配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 业务地址查询 
# 业务地址查询 
背景知识 
业务地址是MME或者SGSN网元对外通信的IP地址，包括GTPC地址，GTPU地址，Ga口地址，Gb口地址等，可以是IPV4，也可以是IPV6地址。 
功能描述 
业务地址查询支持查询网元配置的所有业务地址信息，如，GTPC地址，GTPU地址，Ga口地址等。查询结果包括业务地址、业务地址属性和业务地址的VRF编号。如果一个业务地址配置了多个VRF，将分为多个条目显示。 
相关主题 
 
查询地址属性配置(SHOW LOCALIP)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询地址属性配置(SHOW LOCALIP) 
## 查询地址属性配置(SHOW LOCALIP) 
命令功能 
该命令用于查询所有业务地址属性信息。当需要查询某些或所有业务地址属性时，使用该命令，执行成功后，将看到业务地址属性和业务地址关联的VRF标识。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|业务地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~39个字符。|业务IP地址，可以是IPv4或IPv6类型的地址。如果不输入时，系统默认查询所有业务地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|业务地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~45个字符。|业务IP地址，可以是IPv4或IPv6类型的地址。如果不输入时，系统默认查询所有业务地址。
TYPE|业务地址属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|业务地址属性，指示该地址的地址类型，其类型如下所示。Gn GTPU属性分为2G、3G的Gn口的GTPU地址属性，查询命令参见SHOW USUP SHARE LOAD和SHOW SGUPIP。Iu GTPU属性查询命令参见SHOW SGUPIP。IPNS属性查询命令参见SHOW LOCAL ENDPOINT。IP NSVC的查询命令参见SHOW IP NSVC。GTPC属性查询命令参见SHOW SIGIP GTPC。UBAS属性查询命令参见SHOW UBASCFG。Li属性查询命令参见SHOW LICFG。S102属性查询命令参见SHOW S102 LOCALADDR。IWS S102属性查询命令参见SHOW IWSLOCALIP。
VRF|VRF标识|参数可选性:任选参数；参数类型:整数。|VRF标识，指示该业务地址关联的VRF，与该地址相关的接口和路由需配置关联相应的VRF，本参数为显示项无需填写。查询命令参见SHOW VRFCFG。
命令举例 
查看所有的业务地址属性配置。 
SHOW LOCALIP; 
`
命令 (No.1): SHOW LOCALIP
业务地址                                  业务地址属性    VRF标识
-----------------------------------------------------------------
192.168.1.1                               IPNS            0
192.20.100.18                             UBAS            51
192.168.0.1                               GTP' SINGLEIP   0
192.168.0.1                               Gn GTPU         0
192.168.0.2                               Iu GTPU         0
0001:0000:0000:0000:0000:0000:0000:0002   Gn GTPU         0
0001:0000:0000:0000:0000:0000:0000:0003   Iu GTPU         0
192.168.11.122                            GTPC            0
10.44.20.5                                GTPC            0
-----------------------------------------------------------------
记录数 9
命令执行成功（耗时 0.033 秒）。
` 
父主题： [业务地址查询]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 用户面地址配置 
# 用户面地址配置 
背景知识 
SGSN支持媒体报文的转发，从RNC/BSC接收媒体报文，转发给GGSN；或者从GGSN接收报文，转发给RNC/BSC。 
功能描述 
该配置可用于设置SGSN与RNC交互媒体报文时采用的Iu口IP地址，以及与GGSN交互媒体报文时采用的Gn口的IP地址（按照无线接入类型，可分为2G Gn口和3G Gn口的IP地址）。 
相关主题 
 
新增用户面地址(ADD UPA)
 
 
删除用户面地址(DEL UPA)
 
 
查询用户面地址(SHOW UPA)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增用户面地址(ADD UPA) 
## 新增用户面地址(ADD UPA) 
命令功能 
该命令用于新增SGSN的用户面IP地址。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
INTERFACETYPE|接口类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示用户面IP地址的属性，取值含义为：Iu口：SGSN在Iu口上用户面的IP地址。2G Gn口：SGSN在用户通过2G方式接入时，Gn口上用户面的IP地址。3G Gn口：SGSN在用户通过3G方式接入时，Gn口上用户面的IP地址。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|该参数用于设置IP地址。
命令举例 
增加SGSN在Iu口的用户面IP地址，IP地址为1.1.1.1。 
ADD UPA:INTERFACETYPE="IU",IPADDR="1.1.1.1"; 
父主题： [用户面地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除用户面地址(DEL UPA) 
## 删除用户面地址(DEL UPA) 
命令功能 
该命令用于删除SGSN的用户面IP地址。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
INTERFACETYPE|接口类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示用户面IP地址的属性，取值含义为：Iu口：SGSN在Iu口上用户面的IP地址。2G Gn口：SGSN在用户通过2G方式接入时，Gn口上用户面的IP地址。3G Gn口：SGSN在用户通过3G方式接入时，Gn口上用户面的IP地址。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|该参数用于设置IP地址。
命令举例 
删除SGSN中Iu口的用户面IP地址，IP地址为1.1.1.1。 
DEL UPA:INTERFACETYPE="IU",IPADDR="1.1.1.1"; 
父主题： [用户面地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询用户面地址(SHOW UPA) 
## 查询用户面地址(SHOW UPA) 
命令功能 
该命令用于查询SGSN的用户面IP地址。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
INTERFACETYPE|接口类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示用户面IP地址的属性，取值含义为：Iu口：SGSN在Iu口上用户面的IP地址。2G Gn口：SGSN在用户通过2G方式接入时，Gn口上用户面的IP地址。3G Gn口：SGSN在用户通过3G方式接入时，Gn口上用户面的IP地址。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|该参数用于设置IP地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
INTERFACETYPE|接口类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示用户面IP地址的属性，取值含义为：Iu口：SGSN在Iu口上用户面的IP地址。2G Gn口：SGSN在用户通过2G方式接入时，Gn口上用户面的IP地址。3G Gn口：SGSN在用户通过3G方式接入时，Gn口上用户面的IP地址。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|该参数用于设置IP地址。
命令举例 
查询SGSN中Iu口的用户面IP地址。 
SHOW UPA:INTERFACETYPE="IU"; 
`
命令 (No.1):SHOW UPA:INTERFACETYPE="IU";
接口类型 IP地址 
-----------------
Iu口 1.1.1.1 
-----------------
记录数 1
命令执行成功（耗时 0.046 秒）。
` 
父主题： [用户面地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME IMSI号段LBO限制配置 
# MME IMSI号段LBO限制配置 
背景知识 
用户漫游时，有以下两种典型方式访问PDN（packet data network，分组数据网络）。 
 
Home Routed（归属地路由）：用户通过归属地网关接入PDN，即MME、SGW为拜访地的，PGW为归属地的。
 
 
LBO（Local Breakout，本地疏导）：用户通过拜访地网关接入PDN，即MME、SGW、PGW都为拜访地的。
 
 
不同漫游方式，涉及不同的计费策略等，根据运营商间的漫游协议确定。 
在PDN连接建立时，根据运营商漫游协议，选择访问PDN的方式。 
功能描述 
对漫游用户，如果漫游协议确定只能使用归属地路由方式访问PDN，则需要在MME中配置限制用户使用LBO方式访问PDN。 
                MME上配置限制用户使用LBO，需指定被限制用户的IMSI号段， 配置命令参见
                [ADD MME IMSI RESTRICT LBO]
                。
            
相关主题 
 
新增MME IMSI号段LBO限制配置(ADD MME IMSI RESTRICT LBO)
 
 
修改MME IMSI号段LBO限制配置(SET MME IMSI RESTRICT LBO)
 
 
删除MME IMSI号段LBO限制配置(DEL MME IMSI RESTRICT LBO)
 
 
查询MME IMSI号段LBO限制配置(SHOW MME IMSI RESTRICT LBO)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增MME IMSI号段LBO限制配置(ADD MME IMSI RESTRICT LBO) 
## 新增MME IMSI号段LBO限制配置(ADD MME IMSI RESTRICT LBO) 
命令功能 
该命令用于新增MME IMSI号段LBO限制配置。当需要新增LBO限制号段时使用该命令，使用该命令新增IMSI号段成功后，用户如果在限制号码则不允许选择VPLMN的P-GW。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数为必选参数，IMSI号段：1～15位的数字字符串，首位不能为0。该参数与其他号段配置参数之间不能有包含关系。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数为可选参数，参数类型:字符串数；参数范围为:0~50字节。
命令举例 
增加MME的IMSI号段LBO限制配置，IMSI号段为“46001”，用户别名为“test”。
ADD MME IMSI RESTRICT LBO:IMSI="46001",NAME="test"; 
父主题： [MME IMSI号段LBO限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改MME IMSI号段LBO限制配置(SET MME IMSI RESTRICT LBO) 
## 修改MME IMSI号段LBO限制配置(SET MME IMSI RESTRICT LBO) 
命令功能 
该命令用于修改MME IMSI号段LBO限制配置。当需要修改LBO限制号段配置时使用该命令，使用该命令修改IMSI号段LBO限制配置成功后，能修改该号段的用户别名 
只能修改该号段的用户别名 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数为必选参数，IMSI号段：1～15位的数字字符串，首位不能为0。该参数与其他号段配置参数之间不能有包含关系。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数为可选参数，参数类型:字符串数；参数范围为:0~50字节。
命令举例 
修改MME的IMSI号段LBO限制配置，IMSI号段为“46001”，用户别名为“zte1”。
SET MME IMSI RESTRICT LBO:IMSI="46001",NAME="zte1"; 
父主题： [MME IMSI号段LBO限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除MME IMSI号段LBO限制配置(DEL MME IMSI RESTRICT LBO) 
## 删除MME IMSI号段LBO限制配置(DEL MME IMSI RESTRICT LBO) 
命令功能 
该命令用于删除MME IMSI号段LBO限制配置。当需要删除LBO限制号段配置时使用该命令，使用该命令删除IMSI号段LBO限制配置成功后，能删除该IMSI号段LBO限制所有的配置 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数为必选参数，IMSI号段：1～15位的数字字符串，首位不能为0。该参数与其他号段配置参数之间不能有包含关系。
命令举例 
删除MME的IMSI号段LBO限制配置，IMSI号段为“46001“。
DEL MME IMSI RESTRICT LBO:IMSI="46001"; 
父主题： [MME IMSI号段LBO限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME IMSI号段LBO限制配置(SHOW MME IMSI RESTRICT LBO) 
## 查询MME IMSI号段LBO限制配置(SHOW MME IMSI RESTRICT LBO) 
命令功能 
该命令用于查询MME IMSI号段LBO限制配置，当需要查询LBO限制号段配置时使用该命令，使用该命令查询IMSI号段LBO限制配置成功后，能查询所有IMSI号段LBO限制配置 
输入单个号段查询单个IMSI号段下配置 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数为必选参数，IMSI号段：1～15位的数字字符串，首位不能为0。该参数与其他号段配置参数之间不能有包含关系。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数为必选参数，IMSI号段：1～15位的数字字符串，首位不能为0。该参数与其他号段配置参数之间不能有包含关系。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数为可选参数，参数类型:字符串数；参数范围为:0~50字节。
命令举例 
查询MME的IMSI号段LBO限制配置。
SHOW MME IMSI RESTRICT LBO; 
`
命令 (No.1): SHOW MME IMSI RESTRICT LBO
操作维护         IMSI号段   用户别名
------------------------------------
复制 修改 删除   46001      test
------------------------------------
记录数 1
命令执行成功（耗时 0.042 秒）。
` 
父主题： [MME IMSI号段LBO限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN IMSI号段LBO限制配置 
# SGSN IMSI号段LBO限制配置 
背景知识 
用户漫游时，有以下两种典型方式访问PDN（packet data network，分组数据网络）。 
 
Home Routed（归属地路由）：用户通过归属地网关接入PDN，即SGSN为拜访地的，GGSN为归属地的。
 
 
LBO（Local Breakout，本地疏导）：用户通过拜访地网关接入PDN，即SGSN、GGSN都为拜访地的。
 
 
不同漫游方式，涉及不同的计费策略等，根据运营商间的漫游协议确定。 
在PDN连接建立时，根据运营商漫游协议，选择访问PDN的方式。 
功能描述 
对漫游用户，如果漫游协议确定只能使用归属地路由方式访问PDN，则需要在SGSN中配置限制用户使用LBO方式访问PDN。 
                SGSN上配置限制用户使用LBO，需指定被限制用户的IMSI号段， 配置命令参见
                [ADD SGSN IMSI RESTRICT LBO]
                。
            
相关主题 
 
新增SGSN IMSI号段LBO限制配置(ADD SGSN IMSI RESTRICT LBO)
 
 
修改SGSN IMSI号段LBO限制配置(SET SGSN IMSI RESTRICT LBO)
 
 
删除SGSN IMSI号段LBO限制配置(DEL SGSN IMSI RESTRICT LBO)
 
 
查询SGSN IMSI号段LBO限制配置(SHOW SGSN IMSI RESTRICT LBO)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增SGSN IMSI号段LBO限制配置(ADD SGSN IMSI RESTRICT LBO) 
## 新增SGSN IMSI号段LBO限制配置(ADD SGSN IMSI RESTRICT LBO) 
命令功能 
 该命令用于设置漫游用户接入SGSN时，是否禁用LBO功能。 
当需要禁用漫游用户的LBO功能时，使用该命令。 
该命令执行成功后，该IMSI号段的用户不允许选择拜访地的P-GW进行用户数据报文的转发。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采用E.212编码方式。IMSI首位不能为0，且各IMSI号段不能存在包含的关系也不能有交集。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数为可选参数，参数类型:字符串数；参数范围为:0~50字节。
命令举例 
增加SGSN的IMSI号段LBO限制配置，IMSI号段为“46001”，用户别名为“test”。
ADD SGSN IMSI RESTRICT LBO:IMSI="46001",NAME="test"; 
父主题： [SGSN IMSI号段LBO限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改SGSN IMSI号段LBO限制配置(SET SGSN IMSI RESTRICT LBO) 
## 修改SGSN IMSI号段LBO限制配置(SET SGSN IMSI RESTRICT LBO) 
命令功能 
该命令用于修改SGSN IMSI号段LBO限制配置。当需要修改LBO限制号段配置时使用该命令，使用该命令修改IMSI号段LBO限制配置成功后，能修改该号段的用户别名。 
只能修改该号段的用户别名。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采用E.212编码方式。IMSI首位不能为0，且各IMSI号段不能存在包含的关系也不能有交集。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数为可选参数，参数类型:字符串数；参数范围为:0~50字节。
命令举例 
修改SGSN的IMSI号段LBO限制配置，IMSI号段为“46001”，用户别名为“zte1”。
SET SGSN IMSI RESTRICT LBO:IMSI="46001",NAME="zte1"; 
父主题： [SGSN IMSI号段LBO限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除SGSN IMSI号段LBO限制配置(DEL SGSN IMSI RESTRICT LBO) 
## 删除SGSN IMSI号段LBO限制配置(DEL SGSN IMSI RESTRICT LBO) 
命令功能 
该命令用于删除SGSN IMSI号段LBO限制配置。 
当需要删除LBO限制号段配置时使用该命令，使用该命令删除IMSI号段LBO限制配置成功后，该IMSI号段的用户如果已在HSS签约中开通LBO功能，则该IMSI号段的用户漫游进入本SGSN时，可选择拜访地的PGW进行用户数据报文的转发。  
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采用E.212编码方式。IMSI首位不能为0，且各IMSI号段不能存在包含的关系也不能有交集。
命令举例 
删除SGSN的IMSI号段LBO限制配置，IMSI号段为“46001“。
DEL SGSN IMSI RESTRICT LBO:IMSI="46001"; 
父主题： [SGSN IMSI号段LBO限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN IMSI号段LBO限制配置(SHOW SGSN IMSI RESTRICT LBO) 
## 查询SGSN IMSI号段LBO限制配置(SHOW SGSN IMSI RESTRICT LBO) 
命令功能 
该命令用于查询SGSN IMSI号段LBO限制配置，当需要查询哪些IMSI号段，用户被禁用LBO限制号段配置功能时使用该命令。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采用E.212编码方式。IMSI首位不能为0，且各IMSI号段不能存在包含的关系也不能有交集。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采用E.212编码方式。IMSI首位不能为0，且各IMSI号段不能存在包含的关系也不能有交集。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|此参数为可选参数，参数类型:字符串数；参数范围为:0~50字节。
命令举例 
查询SGSN的IMSI号段LBO限制配置。
 SHOW SGSN IMSI RESTRICT LBO; 
`
命令 (No.1): SHOW SGSN IMSI RESTRICT LBO
操作维护         IMSI号段   用户别名
------------------------------------
复制 修改 删除   46001      test
------------------------------------
记录数 1
命令执行成功（耗时 0.043 秒）。
` 
父主题： [SGSN IMSI号段LBO限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 3G扩展ARD策略配置 
# 3G扩展ARD策略配置 
背景知识 
标准ARD（Access Restriction Data，接入限制数据）功能，是指MS接入PS时，SGSN从HLR获取用户的签约信息，根据签约的ARD信息（即各种接入方式是否允许，包括：GERAN是否允许、UTRAN是否允许等），结合用户当前无线接入方式（Gb或者Iu）决定是否允许用户接入。 
本功能（3G扩展ARD策略）是一个类似标准ARD的功能，基于“3G扩展ARP策略配置”限制特定用户在3G中接入。与标准ARD不同的是，本功能不是在HLR签约，而是在SGSN本地配置。 
功能描述 
3G扩展ARD策略配置，主要用于限制未签署3G漫游协议号段的用户接入。其提供了一种灵活的限制用户3G接入的策略，根据IMSI号段及配置的APN（如果APN未配置，则仅根据IMSI号段）决定用户是否可以在UTRAN中接入，以及在不允许接入时的拒绝原因值。 
用户通过Iu口（UTRAN）发送Attach Request或者RAU Request消息，SGSN根据用户号码（IMSI）与“3G扩展ARD策略配置”的IMSI号段匹配，结合本配置的其它参数（控制策略、签约APN、拒绝原因）判断是否拒绝本次请求。如果拒绝，则在Attach Reject或者RAU Reject消息中携带配置的“拒绝原因”值。 
判断是否拒绝本次接入的策略如下： 
“控制策略”为“全部拒绝”时，拒绝本次接入； 
“控制策略”为“根据签约APN控制”时，判断用户签约的APN（从用户HLR签约参数中获取）是否与“3G扩展ARD策略配置”中的“签约APN”一致。 
 
如果不一致，则拒绝本次接入。
 
 
如果一致，则本检查通过，附着或者路由更新流程继续。
 
 
相关主题 
 
新增3G扩展ARD策略配置(ADD ARD POLICY)
 
 
修改3G扩展ARD策略配置(SET ARD POLICY)
 
 
删除3G扩展ARD策略配置(DEL ARD POLICY)
 
 
查询3G扩展ARD策略配置(SHOW ARD POLICY)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增3G扩展ARD策略配置(ADD ARD POLICY) 
## 新增3G扩展ARD策略配置(ADD ARD POLICY) 
命令功能 
该命令用于新增3G扩展ARD策略配置。 
当需要根据IMSI号段限制用户通过UTRAN接入SGSN时使用该命令。 
可以限制以下2种类型用户： 
 
控制该号段的用户全都不允许通过UTRAN接入到SGSN。
 
 
控制签约非*的APN与SGSN配置的APN相同的用户允许通过UTRAN接入到SGSN。
 
 
注意事项 
 
系统支持该项配置的最大记录数为：256。
 
 
该命令执行后，同步变化表即可生效。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|3G扩展ARD策略配置对应的IMSI号段。
CTRLPOLICY|控制策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:CONTROL BY APN。|该参数决定对该IMSI号段的控制策略。取值含义：根据签约APN控制（CONTROL BY APN）：比较用户签约在HLR的非*的APN跟SGSN配置的APN是否一致，来决定是否限制该号段的用户从UTRAN接入SGSN。如果一致，则允许从UTRAN接入SGSN；如果不一致，则不允许从UTRAN接入SGSN。全部拒绝（DENY）：该IMSI号段内的全部用户，都被限制从UTRAN接入SGSN。
APN|签约APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|当“控制策略”配置为“根据签约APN控制（CONTROL BY APN）”时起作用。如果用户在HLR上签约的APN跟此处配置的APN完全相同，则允许该用户从UTRAN接入SGSN，否则不允许该用户从UTRAN接入SGSN。
CAUSE|拒绝原因|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:GprsNotAllowed。|该参数在新增或者修改3G扩展ARD策略配置时用到。当用户因为该配置被拒绝接入SGSN时，给用户下发的拒绝原因使用该参数的值。取值含义：0x3-非法用户（IllegalMS）：手机接入SGSN时携带的ID非法，例如SGSN对手机鉴权失败时就会认为该用户携带的ID是非法的。0x6-非法设备（IllegalME）：手机的IMEI非法。0x7-GPRS业务不允许（GprsNotAllowed）：不允许该用户使用GPRS业务。0x8-GPRS业务和非GPRS业务均不允许（GaNGNotAllowed）：不允许该用户使用GPRS业务和非GPRS业务。0xB-PLMN不允许（PLMNNotAllowed）：不允许该用户在该PLMN中接入。0xC-位置区不允许（LANotAllowed）：不允许该用户在该位置区接入。0xD-本位置区内漫游不允许（RoamNotAllowed）：漫游用户不允许在该位置区接入。0xE-本PLMN内GPRS业务不允许（GprsNotAllowedInPlmn）：在该PLMN内不允许该用户使用GPRS业务。0xF-位置区内无合适小区（NoSuitCellInLA）：在该位置区中没有合适的小区。0x11-网络失败（NetWorkFailure）：网络侧发生 了失败。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
新增3G扩展ARD策略配置，IMSI号段为46001，控制策略为全部拒绝，拒绝原因为0x7-GPRS业务不允许，用户别名为0。 
ADD ARD POLICY:IMSI="46001",CTRLPOLICY="DENY",CAUSE="GprsNotAllowed",NAME="0"; 
父主题： [3G扩展ARD策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改3G扩展ARD策略配置(SET ARD POLICY) 
## 修改3G扩展ARD策略配置(SET ARD POLICY) 
命令功能 
该命令用于修改3G扩展ARD策略配置。 
当需要修改某个IMSI号段的3G扩展ARD策略配置中的“控制策略”、“签约APN”或者“拒绝原因”时使用该命令。 
注意事项 
该命令执行后，同步变化表即可生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|3G扩展ARD策略配置对应的IMSI号段。
CTRLPOLICY|控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数决定对该IMSI号段的控制策略。取值含义：根据签约APN控制（CONTROL BY APN）：比较用户签约在HLR的非*的APN跟SGSN配置的APN是否一致，来决定是否限制该号段的用户从UTRAN接入SGSN。如果一致，则允许从UTRAN接入SGSN；如果不一致，则不允许从UTRAN接入SGSN。全部拒绝（DENY）：该IMSI号段内的全部用户，都被限制从UTRAN接入SGSN。
APN|签约APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|当“控制策略”配置为“根据签约APN控制（CONTROL BY APN）”时起作用。如果用户在HLR上签约的APN跟此处配置的APN完全相同，则允许该用户从UTRAN接入SGSN，否则不允许该用户从UTRAN接入SGSN。
CAUSE|拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在新增或者修改3G扩展ARD策略配置时用到。当用户因为该配置被拒绝接入SGSN时，给用户下发的拒绝原因使用该参数的值。取值含义：0x3-非法用户（IllegalMS）：手机接入SGSN时携带的ID非法，例如SGSN对手机鉴权失败时就会认为该用户携带的ID是非法的。0x6-非法设备（IllegalME）：手机的IMEI非法。0x7-GPRS业务不允许（GprsNotAllowed）：不允许该用户使用GPRS业务。0x8-GPRS业务和非GPRS业务均不允许（GaNGNotAllowed）：不允许该用户使用GPRS业务和非GPRS业务。0xB-PLMN不允许（PLMNNotAllowed）：不允许该用户在该PLMN中接入。0xC-位置区不允许（LANotAllowed）：不允许该用户在该位置区接入。0xD-本位置区内漫游不允许（RoamNotAllowed）：漫游用户不允许在该位置区接入。0xE-本PLMN内GPRS业务不允许（GprsNotAllowedInPlmn）：在该PLMN内不允许该用户使用GPRS业务。0xF-位置区内无合适小区（NoSuitCellInLA）：在该位置区中没有合适的小区。0x11-网络失败（NetWorkFailure）：网络侧发生 了失败。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
修改IMSI号段为46001的3G扩展ARD策略配置，将控制策略修改为根据签约APN控制，签约APN为zte.com。 
SET ARD POLICY:IMSI="46001",CTRLPOLICY="CONTROL BY APN",APN="zte.com"; 
父主题： [3G扩展ARD策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除3G扩展ARD策略配置(DEL ARD POLICY) 
## 删除3G扩展ARD策略配置(DEL ARD POLICY) 
命令功能 
该命令用于删除3G扩展ARD策略配置。 
根据输入的IMSI号段删除一条配置。该配置没有关联其他的配置，可以直接删除。 
注意事项 
该命令执行后，同步变化表即可生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|3G扩展ARD策略配置对应的IMSI号段。
命令举例 
删除IMSI号段为46001的3G扩展ARD策略配置。 
DEL ARD POLICY:IMSI="46001"; 
父主题： [3G扩展ARD策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询3G扩展ARD策略配置(SHOW ARD POLICY) 
## 查询3G扩展ARD策略配置(SHOW ARD POLICY) 
命令功能 
该命令用于查询3G扩展ARD策略配置。 
根据输入的IMSI号段进行查询，查询结果显示该号段对应的3G扩展ARD策略配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|3G扩展ARD策略配置对应的IMSI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|3G扩展ARD策略配置对应的IMSI号段。
CTRLPOLICY|控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数决定对该IMSI号段的控制策略。取值含义：根据签约APN控制（CONTROL BY APN）：比较用户签约在HLR的非*的APN跟SGSN配置的APN是否一致，来决定是否限制该号段的用户从UTRAN接入SGSN。如果一致，则允许从UTRAN接入SGSN；如果不一致，则不允许从UTRAN接入SGSN。全部拒绝（DENY）：该IMSI号段内的全部用户，都被限制从UTRAN接入SGSN。
APN|签约APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|当“控制策略”配置为“根据签约APN控制（CONTROL BY APN）”时起作用。如果用户在HLR上签约的APN跟此处配置的APN完全相同，则允许该用户从UTRAN接入SGSN，否则不允许该用户从UTRAN接入SGSN。
CAUSE|拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在新增或者修改3G扩展ARD策略配置时用到。当用户因为该配置被拒绝接入SGSN时，给用户下发的拒绝原因使用该参数的值。取值含义：0x3-非法用户（IllegalMS）：手机接入SGSN时携带的ID非法，例如SGSN对手机鉴权失败时就会认为该用户携带的ID是非法的。0x6-非法设备（IllegalME）：手机的IMEI非法。0x7-GPRS业务不允许（GprsNotAllowed）：不允许该用户使用GPRS业务。0x8-GPRS业务和非GPRS业务均不允许（GaNGNotAllowed）：不允许该用户使用GPRS业务和非GPRS业务。0xB-PLMN不允许（PLMNNotAllowed）：不允许该用户在该PLMN中接入。0xC-位置区不允许（LANotAllowed）：不允许该用户在该位置区接入。0xD-本位置区内漫游不允许（RoamNotAllowed）：漫游用户不允许在该位置区接入。0xE-本PLMN内GPRS业务不允许（GprsNotAllowedInPlmn）：在该PLMN内不允许该用户使用GPRS业务。0xF-位置区内无合适小区（NoSuitCellInLA）：在该位置区中没有合适的小区。0x11-网络失败（NetWorkFailure）：网络侧发生 了失败。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
查询已配置的IMSI号段为46001的3G扩展ARD策略。 
SHOW ARD POLICY:IMSI="46001"; 
`
命令 (No.1): SHOW ARD POLICY:IMSI="46001";
操作维护         IMSI号段   控制策略          签约APN   拒绝原因                           用户别名
---------------------------------------------------------------------------------------------------
复制 修改 删除   46001      全部拒绝                    0x7-GPRS业务不允许                 0
---------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.073 秒）。
` 
父主题： [3G扩展ARD策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 支持DT的GGSN IP配置 
# 支持DT的GGSN IP配置 
背景知识 
DT（Direct Tunnel，直传隧道）是基于网络扁平化以及控制面用户面分离提出的。实现DT后，SGSN出Gn或Gp口时，用户面数据直接在RNC和GGSN之间传输，SGSN只负责PDP上下文的建立与删除，不负责用户面数据报文的转发。这样数据转发处理就减少了一个网元节点，减少了网络处理复杂度和时延，降低了网络成本，同时，SGSN在DT时，不建立用户面资源，节省了SGSN的部分投资。DT是Iu口接入模式下的一个可选功能，不适用Gb口接入的情况。 
DT功能涉及到SGSN和GGSN的配合： 
在具有DT能力的SGSN中，能配置每个RNC和GGSN是否支持直接用户面连接。SGSN处理控制面信令并决策何时建立直传隧道。 
在DT情况下，GGSN收到RNC的用户面ERROR INDICATION消息时，需要给SGSN发更新消息Update PDP Context Request，指示SGSN释放对应的RAB资源。 
功能描述 
具有DT能力的SGSN在出Gn或Gp口时，确定GGSN是否支持DT，有如下两种方式： 
                        本地根据APN进行配置，使用GPRS APN HOST配置（
                        [ADD GPRS APN]
                        ）或EPC APN HOST配置（
                        [ADD EPC APN]
                        ）或DNS解析类APN配置（
                        [ADD DNSAPNCHG]
                        ）。
                    
本地根据GGSN的IP地址配置。 
支持DT的GGSN IP配置用于方式2。 
配置支持DT功能的流程如下： 
                        RNC局向附加属性中配置支持DT功能，配置命令参见：
                        [ADD RNC]
                        。
                    
                        配置支持DT的GGSN地址，配置命令为：
                        [ADD DT IP]
                        。
                    
注意事项： 
 
SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。
 
 
软件参数“DT话单控制”（ID：786523），控制是否产生DT话单，该软件参数取值为0，则不产生无流量的DT话单（not generate no volume DT CDR）；取值为1，则产生DT话单（generate DT CDR）；取值为2，则不产生DT话单（not generagte DT CDR）。
 
 
软件参数“DT切换频次”（ID：786527），除SGSN首次建立DT外，控制SGSN建立DT的切换频次。该软件参数取值为0，则总是允许；取值为1-254，则第N+1次允许（allow once for every N+1 times）；取值为255，则总是不允许。
 
 
软件参数“CAMEL用户是否允许隧道直传”（ID：786546），控制CAMEL用户是否允许DT功能。该软件参数取值为0，则不允许CAMEL用户隧道直传；取值为1，则允许CAMEL用户隧道直传。
 
 
相关主题 
 
新增支持DT的GGSN地址配置(ADD DT IP)
 
 
删除支持DT的GGSN地址配置(DEL DT IP)
 
 
查询支持DT的GGSN地址配置(SHOW DT IP)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增支持DT的GGSN地址配置(ADD DT IP) 
## 新增支持DT的GGSN地址配置(ADD DT IP) 
命令功能 
该命令用于配置支持DT（Direct Tunnel，直传隧道）功能的GGSN的IP地址列表。 
在SGSN出Gn或Gp口时，使用扩展APN来解析GGSN IP地址情况下，如果通过[ADD EXAPN]命令，将参数“DT策略“设置为”根据支持DT的GGSN IP配置决策”，则SGSN需要将通过扩展APN解析出的GGSN IP地址与本命令配置的GGSN IP地址列表进行比较，如果解析出的GGSN IP地址在本命令配置的GGSN IP地址列表中，则表示SGSN通过扩展APN解析出的GGSN支持DT功能。
注意事项 
该命令需要加载支持该特性的License，对应的License项为“支持DT功能”,License ID为5003的项目的显示值为YES，表示此网元支持DT功能。本配置添加的GGSN地址，仅针对使用扩展APN有效，对非扩展APN无效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|GGSN与SGSN通信的Gn或Gp接口的信令面IP地址。
命令举例 
新增支持DT的GGSN配置，地址为10.43.146.1。 
ADD DT IP:IPADDR="10.43.146.1"; 
父主题： [支持DT的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除支持DT的GGSN地址配置(DEL DT IP) 
## 删除支持DT的GGSN地址配置(DEL DT IP) 
命令功能 
该命令用于将GGSN地址从支持DT功能的GGSN IP地址列表中删除。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|GGSN与SGSN通信的Gn或Gp接口的信令面IP地址。
命令举例 
删除地址为10.43.146.1的支持DT的GGSN配置。 
DEL DT IP:IPADDR="10.43.146.1"; 
父主题： [支持DT的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询支持DT的GGSN地址配置(SHOW DT IP) 
## 查询支持DT的GGSN地址配置(SHOW DT IP) 
命令功能 
该命令用于查询支持DT功能的GGSN IP地址列表。
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:任选参数；参数类型:地址|GGSN与SGSN通信的Gn或Gp接口的信令面IP地址。
命令举例 
查询支持DT的GGSN配置。 
SHOW DT IP; 
`
命令 (No.1): SHOW DT IP;
操作维护    GGSN IP地址
-----------------------
复制 删除   10.43.146.1
-----------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [支持DT的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 支持终端双栈的GGSN IP配置 
# 支持终端双栈的GGSN IP配置 
背景知识 
双栈，也叫双协议栈，即可以同时支持IPV4和IPV6协议。支持双栈的设备，既可以访问IPV4的网络资源，同时也可以访问IPV6的网络资源，而无需进行网络切换。 
手机终端接入互联网，必须要获得一个IP地址。以前的IP地址版本为IPV4，但是由于其可分配的IP地址资源越来越少，支持IPV6已成为网络设备商和手机产商的共识。同时分配了IPV4和IPV6地址的手机，既可以访问IPV4的互联网网络资源，也可以通过IPV6地址访问IPV6的网络资源。 
功能描述 
支持终端双栈功能的SGSN，确定GGSN是否支持终端双栈，有如下两种方式： 
                        本地根据APN进行配置，使用GPRS APN HOST配置（
                        [ADD GPRS APN]
                        ）；
                    
本地根据GGSN的IP地址配置； 
支持终端双栈的GGSN IP配置用于方式2。 
配置双栈功能的流程如下： 
                        SGSN终端双栈数据中配置支持终端双栈功能，配置命令参见：
                        [SET GNGP DUAL STACK]
                        。
                    
                        RNC局向附加属性中配置支持终端双栈功能，配置命令参见：
                        [ADD RNC]
                        。
                    
                        配置支持终端双栈的GGSN地址。配置命令为：
                        [ADD DUAL STACK IP]
                        。
                    
配置软件参数“计费消息是否携带终端双栈地址”，取值0：IPv4，1：IPv6，2：Ipv4v6。 
相关主题 
 
新增支持终端双栈的GGSN地址配置(ADD DUAL STACK IP)
 
 
删除支持终端双栈的GGSN地址配置(DEL DUAL STACK IP)
 
 
查询支持终端双栈的GGSN地址配置(SHOW DUAL STACK IP)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增支持终端双栈的GGSN地址配置(ADD DUAL STACK IP) 
## 新增支持终端双栈的GGSN地址配置(ADD DUAL STACK IP) 
命令功能 
该命令用于配置支持双栈功能的GGSN IP地址列表。 
双栈功能需要多个网元的配合才能实现，在RNC、SGSN和GGSN都支持双栈的情况下，MS才能启用双栈功能，具体情况如下： 
SGSN网元支持双栈：可通过[SET S4 DUAL STACK]命令设置SGSN网元支持双栈功能。
RNC网元支持双栈：可通过[ADD RNC]命令设置RNC支持双栈功能。
GGSN网元支持双栈：SGSN可通过两种DNS解析和本地配置两种方式来获取GGSN的IP地址，GGSN网元是否支持双栈分为两种情况： 
 
在SGSN使用ADD GPRS APN命令配置的本地数据获取GGSN IP地址情况下，如果通过ADD GPRS APN命令配置的参数“支持终端双栈功能”为“支持”，则表示此GGSN支持双栈功能。
 
 
在SGSN使用DNS对APN进行解析获取GGSN IP地址情况下， SGSN将解析出的GGSN IP地址与本命令配置的GGSN IP地址列表进行比较，如果解析出的GGSN IP地址在本命令配置的GGSN IP地址列表中，则表示此GGSN支持双栈功能。
 
 
注意事项 
该功能仅适用于SGSN网元。 
该功能受软件参数“计费消息是否携带终端双栈地址”（ID为393239）的影响，包括如下取值： 
取值为0，表示SGSN在CDR中填写MS的IPv4地址。 
取值为1，表示SGSN在CDR中填写MS的IPv6地址。 
取值为2，表示SGSN在CDR中填写MS的IPv4和IPv6地址。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|GGSN 用于与SGSN通信的Gn接口信令面IP地址
命令举例 
新增支持双栈的GGSN，地址为1.1.1.1。 
ADD DUAL STACK IP:IPADDR="1.1.1.1"; 
父主题： [支持终端双栈的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除支持终端双栈的GGSN地址配置(DEL DUAL STACK IP) 
## 删除支持终端双栈的GGSN地址配置(DEL DUAL STACK IP) 
命令功能 
该命令用于将GGSN地址从支持双栈功能的GGSN IP地址列表中删除。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|GGSN 用于与SGSN通信的Gn接口信令面IP地址
命令举例 
删除支持双栈的GGSN配置，地址为1.1.1.1。 
DEL DUAL STACK IP:IPADDR="1.1.1.1"; 
父主题： [支持终端双栈的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询支持终端双栈的GGSN地址配置(SHOW DUAL STACK IP) 
## 查询支持终端双栈的GGSN地址配置(SHOW DUAL STACK IP) 
命令功能 
该命令用于查询支持双栈功能的GGSN IP地址列表。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:任选参数；参数类型:地址|GGSN 用于与SGSN通信的Gn接口信令面IP地址
命令举例 
查询支持双栈的GGSN地址配置。 
SHOW DUAL STACK IP; 
`
命令 (No.1): SHOW DUAL STACK IP
操作维护    GGSN IP地址
-----------------------
复制 删除   1.1.1.1
-----------------------
记录数 1
命令执行成功（耗时 0.063 秒）。
` 
父主题： [支持终端双栈的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 不支持终端双栈的GGSN IP配置 
# 不支持终端双栈的GGSN IP配置 
背景知识 
双栈，也叫双协议栈，即可以同时支持IPV4和IPV6协议。支持双栈的设备，既可以访问IPV4的网络资源，同时也可以访问IPV6的网络资源，而无需进行网络切换。 
手机终端接入互联网，必须要获得一个IP地址。以前的IP地址版本为IPV4，但是由于其可分配的IP地址资源越来越少，支持IPV6已成为网络设备商和手机产商的共识。同时分配了IPV4和IPV6地址的手机，既可以访问IPV4的互联网网络资源，也可以通过IPV6地址访问IPV6的网络资源。 
功能描述 
支持终端双栈功能的SGSN，确定GGSN是否支持终端双栈，有如下两种方式： 
 
本地根据APN进行配置，使用“GPRS APN HOST配置”中命令进行配置。
 
 
本地根据GGSN的IP地址配置，使用“不支持终端双栈的GGSN IP配置”中命令进行配置。
 
 
配置双栈功能的流程如下： 
                        SGSN终端双栈数据中配置支持终端双栈功能，配置命令为：
                        [SET GNGP DUAL STACK]
                        。
                    
                        RNC局向附加属性中配置支持终端双栈功能，配置命令为：
                        [ADD RNC]
                        。
                    
                        配置GGSN支持终端双栈的默认策略。配置命令为：
                        [SET GNGP DUAL STACK]
                        。
                    
                        当默认策略为不支持时，需要配置支持终端双栈的GGSN地址。配置命令为：
                        [ADD DUAL STACK IP]
                        。
                    
                        当默认策略为支持时，需要配置不支持终端双栈的GGSN地址。配置命令为：
                        [ADD NOT DUAL STACK IP]
                        。
                    
                        使用命令
                        [SET SOFTWARE PARAMETER]
                        配置软件参数“计费消息是否携带终端双栈地址”（ID为393239），取值如下：
                    
 
0：IPv4
 
 
1：IPv6
 
 
2：Ipv4v6
 
 
相关主题 
 
新增不支持终端双栈的GGSN地址配置(ADD NOT DUAL STACK IP)
 
 
删除不支持终端双栈的GGSN地址配置(DEL NOT DUAL STACK IP)
 
 
查询不支持终端双栈的GGSN地址配置(SHOW NOT DUAL STACK IP)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增不支持终端双栈的GGSN地址配置(ADD NOT DUAL STACK IP) 
## 新增不支持终端双栈的GGSN地址配置(ADD NOT DUAL STACK IP) 
命令功能 
该命令用于配置不支持双栈功能的GGSN IP地址列表。 
双栈功能需要多个网元的配合才能实现，在RNC、SGSN和GGSN都支持双栈的情况下，MS才能启用双栈功能，具体情况如下： 
 
SGSN网元支持双栈：可通过SET GNGP DUAL STACK命令设置SGSN网元支持双栈功能。
 
 
RNC网元支持双栈：可通过ADD RNC命令设置RNC支持双栈功能。
 
 
GGSN网元支持双栈：SGSN可通过DNS解析和本地配置两种方式来获取GGSN的IP地址。
GGSN网元是否支持双栈分为两种情况：
在SGSN使用ADD GPRS APN命令配置的本地数据获取GGSN IP地址情况下，如果通过ADD GPRS APN命令配置的参数“支持终端双栈功能”为“支持”，则表示此GGSN支持双栈功能。
在SGSN使用DNS对APN进行解析获取GGSN IP地址情况下， SGSN将解析出的GGSN IP地址与本命令配置的GGSN IP地址列表进行比较，如果解析出的GGSN IP地址在本命令配置的GGSN IP地址列表中，则表示此GGSN不支持双栈功能。
 
 
注意事项 
该功能仅适用于SGSN网元。 
该功能受软件参数“计费消息是否携带终端双栈地址”（ID为393239）的影响，包括如下取值： 
 
取值为0，表示SGSN在CDR中填写MS的IPv4地址。
 
 
取值为1，表示SGSN在CDR中填写MS的IPv6地址。
 
 
取值为2，表示SGSN在CDR中填写MS的IPv4和IPv6地址。
 
 
使用命令[SET SOFTWARE PARAMETER]配置软件参数。
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|GGSN用于与SGSN通信的Gn接口信令面IP地址。
命令举例 
新增不支持双栈的GGSN，地址为1.1.1.1。 
ADD NOT DUAL STACK IP:IPADDR="1.1.1.1"; 
父主题： [不支持终端双栈的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除不支持终端双栈的GGSN地址配置(DEL NOT DUAL STACK IP) 
## 删除不支持终端双栈的GGSN地址配置(DEL NOT DUAL STACK IP) 
命令功能 
该命令用于将GGSN地址从不支持双栈功能的GGSN IP地址列表中删除。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|GGSN用于与SGSN通信的Gn接口信令面IP地址。
命令举例 
删除不支持双栈的GGSN配置，地址为1.1.1.1。 
DEL NOT DUAL STACK IP:IPADDR="1.1.1.1"; 
父主题： [不支持终端双栈的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询不支持终端双栈的GGSN地址配置(SHOW NOT DUAL STACK IP) 
## 查询不支持终端双栈的GGSN地址配置(SHOW NOT DUAL STACK IP) 
命令功能 
该命令用于查询不支持双栈功能的GGSN IP地址列表。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:任选参数；参数类型:地址|GGSN用于与SGSN通信的Gn接口信令面IP地址。
命令举例 
查询不支持双栈的GGSN地址配置。 
SHOW NOT DUAL STACK IP; 
`
命令 (No.1): SHOW NOT DUAL STACK IP
操作维护    GGSN IP地址
-----------------------
复制 删除   1.1.1.1
-----------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [不支持终端双栈的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# Delivery Order控制配置 
# Delivery Order控制配置 
背景知识 
Delivery Order指对用户面数据报文，是否应严格按sequence的顺序发送和接收。 
3GPP 23.107的第6.4.3.1 List of attributes章节中定义Delivery Order和PDP type相关，当PDP type为“IPv4”或“IPv6”时，Delivery Order应该设置为“No”。 
但现网有一些GGSN需要Delivery Order设置为“Yes”才能正常的处理业务数据，因此对这些GGSN，既使PDP type为“IPv4”或“IPv6”，在PDP激活过程中，SGSN也需要把使用的Delivery Order的值设置为“Yes”。 
功能描述 
如果现网有GGSN需要Delivery Order设置为“Yes”才能正常的处理业务数据，则需要进行Delivery Order控制配置。 
其配置流程如下： 
                        开启Delivery Order控制功能开关，配置命令为：
                        [SET DOSPRT]
                        :SPRT="YES";。
                    
                        在Delivery Order控制配置中，增加GGSN地址，配置命令参见
                        [ADD DO IP]
                        。当SGSN在激活PDP时，如果GGSN地址在配置的GGSN地址列表中，则最后协商的Delivery Order的值为“Yes”。
                    
相关主题 
 
设置Delivery Order开关配置(SET DOSPRT)
 
 
查询Delivery Order开关配置(SHOW DOSPRT)
 
 
新增GGSN IP配置(ADD DO IP)
 
 
删除GGSN IP配置(DEL DO IP)
 
 
查询GGSN IP配置(SHOW DO IP)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置Delivery order开关配置(SET DOSPRT) 
## 设置Delivery order开关配置(SET DOSPRT) 
命令功能 
此命令用于设置SGSN是否支持Delivery Order（发送次序）控制功能。 
Delivery Order控制功能是指SGSN与指定的GGSN网元处理用户面数据报文时，是否应严格按sequence的顺序发送和接收。 
注意事项 
该命令只适用于SGSN。 
如果设置SGSN支持Delivery order功能，则后续还需要通过[ADD DO IP]命令设置与SGSN通信的GGSN网元的IP地址。
参数说明 
标识|名称|类型|说明
---|---|---|---
SPRT|支持Delivery order控制|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数配置为“YES”：表示SGSN与指定GGSN（通过命令ADD DO IP设置的GGSN）的数据报文处理需要严格按照sequence的顺序发送和接收。该参数配置为“NO”时：表示SGSN与指定GGSN（通过命令ADD DO IP设置的GGSN）的数据报文处理不需要严格按照sequence的顺序发送和接收。
命令举例 
设置支持Delivery order控制。 
SET DOSPRT:SPRT="YES"; 
父主题： [Delivery Order控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询Delivery order开关配置(SHOW DOSPRT) 
## 查询Delivery order开关配置(SHOW DOSPRT) 
命令功能 
此命令用于查询SGSN是否支持Delivery Order（发送次序）控制功能。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SPRT|支持Delivery order控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数配置为“YES”：表示SGSN与指定GGSN（通过命令ADD DO IP设置的GGSN）的数据报文处理需要严格按照sequence的顺序发送和接收。该参数配置为“NO”时：表示SGSN与指定GGSN（通过命令ADD DO IP设置的GGSN）的数据报文处理不需要严格按照sequence的顺序发送和接收。
命令举例 
查询Delivery order开关配置。 
SHOW DOSPRT; 
`
命令 (No.1): SHOW DOSPRT;
操作维护  支持Delivery order控制
--------------------------------
修改      支持
--------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [Delivery Order控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增GGSN IP配置(ADD DO IP) 
## 新增GGSN IP配置(ADD DO IP) 
命令功能 
该命令用于新增与SGSN通信的GGSN的IP地址。 
增加该IP地址后，SGSN与使用该地址的GGSN处理用户面数据报文时，需要根据[SET DOSPRT]命令设定的结果来决定是否严格按照sequence的顺序发送和接收。
注意事项 
配置此命令前，已通过[SET DOSPRT]命令设置SGSN网元支持Delivery Order控制功能。
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|GGSN用于与SGSN进行信令面交互的IP地址。
命令举例 
新增GGSN IP地址，地址为1.1.1.1和2.2.2.2。 
ADD DO IP:IPADDR="1.1.1.1"&"1.1.1.2"; 
父主题： [Delivery Order控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除GGSN IP配置(DEL DO IP) 
## 删除GGSN IP配置(DEL DO IP) 
命令功能 
该命令用于删除与SGSN通信的GGSN的IP地址。 
删除该IP地址后，SGSN与使用该地址的GGSN处理用户面数据报文时，将不再根据[SET DOSPRT]命令设定的结果来决定是否严格按照sequence的顺序发送和接收。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|GGSN用于与SGSN进行信令面交互的IP地址。
命令举例 
删除GGSN IP地址，地址为1.1.1.1和2.2.2.2。 
DEL DO IP:IPADDR="1.1.1.1"&"1.1.1.2"; 
父主题： [Delivery Order控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询GGSN IP配置(SHOW DO IP) 
## 查询GGSN IP配置(SHOW DO IP) 
命令功能 
该命令用于查询与SGSN通信的GGSN的IP地址。 
会显示当前支持Delivery Order功能的GGSN的IP地址。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GGSN IP地址|参数可选性:任选参数；参数类型:地址|GGSN用于与SGSN进行信令面交互的IP地址。
命令举例 
查询GGSN IP配置。 
SHOW DO IP; 
`
命令 (No.1): SHOW DO IP;
操作维护    GGSN IP地址
-----------------------
复制 删除   1.1.1.1
复制 删除   1.1.1.2
-----------------------
记录数 2
命令执行成功（耗时 0.042 秒）。
` 
父主题： [Delivery Order控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN支持的Target ID配置 
# SGSN支持的Target ID配置 
背景知识 
在3GPP TS 29.060协议的V6.18.0之前版本Forward Relocation Request消息中的TargetID的结构和V6.18.0及之后版本不同，TargetID具体参见相应版本的3GPP TS 29.060协议的7.7.37节。 
用户从一个SGSN（称为原SGSN）切换到另一个SGSN（称为目标SGSN），原SGSN给目标SGSN发送前传重定位请求Forward Relocation Request消息时，需要根据目标SGSN支持的GTP版本来确定该消息中TargetID参数的结构。 
功能描述 
和本SGSN有切换关系的SGSN支持的GTP协议版本不同，且有的是V6.18.0之前的版本，有的是V6.18.0及之后的版本时，则在本配置中配置和本SGSN有切换关系的SGSN的IP地址以及其对应的GTP协议版本。 
当用户从本SGSN切出，本SGSN向目标SGSN发前传重定位请求消息Forward Relocation Request时，其中的TargetID参数结构的获取有以下两种方式。 
 
本配置中已配置目标SGSN IP地址时，根据目标SGSN的IP地址获取其支持的GTP协议版本号，然后再根据版本号确定消息中TargetID参数的结构。
 
 
本配置中没有配置目标SGSN IP地址时，则根据系统缺省的版本号进行填写；缺省版本号可以修改查询，系统初始化时是V6.18.0之前版本。
 
 
相关主题 
 
设置SGSN支持的缺省Target ID(SET DEFAULT TARGETID)
 
 
查询SGSN支持的缺省Target ID(SHOW DEFAULT TARGETID)
 
 
新增SGSN支持的Target ID配置(ADD TARGETID)
 
 
修改SGSN支持的Target ID配置(SET TARGETID)
 
 
删除SGSN支持的Target ID配置(DEL TARGETID)
 
 
查询SGSN支持的Target ID配置(SHOW TARGETID)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置SGSN支持的缺省Target ID(SET DEFAULT TARGETID) 
## 设置SGSN支持的缺省Target ID(SET DEFAULT TARGETID) 
命令功能 
当UE从本SGSN网元（源SGSN）切换到其它SGSN网元（目标SGSN）时，该命令用于设置目标SGSN网元支持的缺省Target ID版本。 
本SGSN网元先根据目标SGSN网元的IP地址查询根据[ADD TARGETID]命令配置的数据，如果匹配不到对应的记录，则使用本命令配置数据做为目标SGSN网元的缺省Target ID版本。
注意事项 
如果没有通过[ADD TARGETID]进行过相关设置，将使用该缺省设置
参数说明 
标识|名称|类型|说明
---|---|---|---
DFTGNGPFLAG|Target ID缺省版本|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|表示目标SGSN网元支持的缺省Target ID版本。
命令举例 
SET DEFAULT TARGETID:DFTGNGPFLAG="V6.18.0 Ago"; 
`
命令 (No.1): SET DEFAULT TARGETID:DFTGNGPFLAG="V6.18.0 Ago";
Target ID缺省版本 
-----------------------------
TS29.060 V6.18.0以前标准 
-----------------------------
记录数 1
命令执行成功（耗时 0.193 秒）。
` 
父主题： [SGSN支持的Target ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN支持的缺省Target ID(SHOW DEFAULT TARGETID) 
## 查询SGSN支持的缺省Target ID(SHOW DEFAULT TARGETID) 
命令功能 
该命令用于查询SGSN支持的缺省Target ID版本。 
注意事项 
如果没有通过[ADD TARGETID]进行过相关设置，将使用该缺省设置
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DFTGNGPFLAG|Target ID缺省版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示目标SGSN网元支持的缺省Target ID版本。
命令举例 
查询SGSN支持的缺省Target ID版本。
SHOW DEFAULT TARGETID; 
`
命令 (No.1): SHOW DEFAULT TARGETID;
操作维护  Target ID缺省版本
---------------------------
修改      TS29.060 V6.18.0以前标准
---------------------------
记录数 1
命令执行成功（耗时 0.091 秒）。
` 
父主题： [SGSN支持的Target ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增SGSN支持的Target ID配置(ADD TARGETID) 
## 新增SGSN支持的Target ID配置(ADD TARGETID) 
命令功能 
该命令用于新增目标 SGSN支持的Target ID版本。 
注意事项 
通过目标 SGSN的IP地址匹配Target ID版本。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|SGSN IP地址|参数可选性:必选参数；参数类型:地址|表示目标SGSN网元的GTP-C信令地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址。
GNGPFLAG|Target ID版本|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:V6.18.0 And Later。|GTP协议（3GPP TS29.060） V6.18.0及以后标准和之前的标准对Target ID定义的格式不同。该参数配置目标SGSN支持的3GPP TS29.060协议具体版本，取值包括：V6.18.0 And Later：TS29.060 V6.18.0及以后标准。V6.18.0 Ago：TS29.060 V6.18.0以前标准。配置后，SGSN网元根据配置的版本确定发送Forward Relocation Request消息时携带的Target ID格式。
命令举例 
新增SGSN支持的Target ID配置，SGSN地址为1.0.0.0，缺省版本为TS29.060 V6.18.0以前标准。
ADD TARGETID:IPADDR="1.0.0.0",GNGPFLAG=V6.18.0 Ago; 
`
命令 (No.1): ADD TARGETID:IPADDR="1.0.0.0",GNGPFLAG=V6.18.0 Ago;
SGSN IP地址   Target ID版本
---------------------------
1.0.0.0       TS29.060 V6.18.0以前标准
---------------------------
记录数 1
命令执行成功（耗时 0.172 秒）。
` 
父主题： [SGSN支持的Target ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改SGSN支持的Target ID配置(SET TARGETID) 
## 修改SGSN支持的Target ID配置(SET TARGETID) 
命令功能 
该命令用于修改目标SGSN支持的Target ID版本。 
注意事项 
通过目标 SGSN的IP地址匹配Target ID版本。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|SGSN IP地址|参数可选性:必选参数；参数类型:地址|表示目标SGSN网元的GTP-C信令地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址。
GNGPFLAG|Target ID版本|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|GTP协议（3GPP TS29.060） V6.18.0及以后标准和之前的标准对Target ID定义的格式不同。该参数配置目标SGSN支持的3GPP TS29.060协议具体版本，取值包括：V6.18.0 And Later：TS29.060 V6.18.0及以后标准。V6.18.0 Ago：TS29.060 V6.18.0以前标准。配置后，SGSN网元根据配置的版本确定发送Forward Relocation Request消息时携带的Target ID格式。
命令举例 
修改SGSN地址为1.0.0.0的Target ID版本为TS29.060 V6.18.0及以后标准。
SET TARGETID:IPADDR="1.0.0.0",GNGPFLAG="V6.18.0 And Later"; 
`
命令 (No.1): SET TARGETID:IPADDR="1.0.0.0",GNGPFLAG="V6.18.0 And Later";
SGSN IP地址   Target ID版本
---------------------------
1.0.0.0       TS29.060 V6.18.0及以后标准
---------------------------
记录数 1
命令执行成功（耗时 0.054 秒）。
` 
父主题： [SGSN支持的Target ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除SGSN支持的Target ID配置(DEL TARGETID) 
## 删除SGSN支持的Target ID配置(DEL TARGETID) 
命令功能 
该命令用于删除目标SGSN支持的Target ID版本。 
注意事项 
通过目标 SGSN的IP地址匹配Target ID版本。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|SGSN IP地址|参数可选性:必选参数；参数类型:地址|表示目标SGSN网元的GTP-C信令地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址。
命令举例 
删除SGSN地址为1.0.0.0的Target ID配置。
DEL TARGETID:IPADDR="1.0.0.0"; 
`
命令 (No.1): DEL TARGETID:IPADDR="1.0.0.0";
SGSN IP地址   Target ID版本
---------------------------
1.0.0.0       TS29.060 V6.18.0及以后标准
---------------------------
记录数 1
命令执行成功（耗时 0.092 秒）。
` 
父主题： [SGSN支持的Target ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN支持的Target ID配置(SHOW TARGETID) 
## 查询SGSN支持的Target ID配置(SHOW TARGETID) 
命令功能 
该命令用于查询目标SGSN支持的Target ID版本。 
注意事项 
通过目标 SGSN的IP地址匹配Target ID版本。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|SGSN IP地址|参数可选性:任选参数；参数类型:地址|表示目标SGSN网元的GTP-C信令地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|SGSN IP地址|参数可选性:任选参数；参数类型:地址|表示目标SGSN网元的GTP-C信令地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址。
GNGPFLAG|Target ID版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GTP协议（3GPP TS29.060） V6.18.0及以后标准和之前的标准对Target ID定义的格式不同。该参数配置目标SGSN支持的3GPP TS29.060协议具体版本，取值包括：V6.18.0 And Later：TS29.060 V6.18.0及以后标准。V6.18.0 Ago：TS29.060 V6.18.0以前标准。配置后，SGSN网元根据配置的版本确定发送Forward Relocation Request消息时携带的Target ID格式。
命令举例 
查询SGSN支持的Target ID配置。
SHOW TARGETID; 
`
命令 (No.1): SHOW TARGETID;
操作维护         SGSN IP地址   Target ID版本
--------------------------------------------
复制 修改 删除   1.0.0.0       TS29.060 V6.18.0及以后标准
--------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [SGSN支持的Target ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# UE网络能力IE支持的版本 
# UE网络能力IE支持的版本 
背景知识 
UE Network Capability是UE 4G相关的网络能力的IE，一般由UE在首条消息中携带给核心网，用于能力的协商和其他处理。在TS29.060中，局间消息（SGSN Context Rsp、Forward Relocation Req）中的MM上下文中在950版本之前是有UE Network Capability这个字段的，可是在950版本及之后将UE Network Capability放到了MM上下文外面了，并且在后面的版本中在原先UE Network Capability的位置增加了其他的IE，所以为了兼容版本差异需要配置对端网元的版本，本局根据对端网元的版本进行编码和解码。设置默认的版本是为了统一配置对端网元的GTPV1版本。 
功能描述 
UE网络能力配置包括： 
 
全局默认配置。
 
 
通过IP地址配置对端网元的UE网络能力。
 
 
相关主题 
 
设置UE网络能力IE支持的默认版本(SET DEFAULT UENETWORKCAPVERFG)
 
 
查询UE网络能力IE支持的默认版本(SHOW DEFAULT UENETWORKCAPVERFG)
 
 
新增UE网络能力IE支持的版本(ADD UENETWORKCAPVERFG)
 
 
修改UE网络能力IE支持的版本(SET UENETWORKCAPVERFG)
 
 
删除UE网络能力IE支持的版本(DEL UENETWORKCAPVERFG)
 
 
查询UE网络能力IE支持的版本(SHOW UENETWORKCAPVERFG)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置UE网络能力IE支持的默认版本(SET DEFAULT UENETWORKCAPVERFG) 
## 设置UE网络能力IE支持的默认版本(SET DEFAULT UENETWORKCAPVERFG) 
命令功能 
该命令用于设置UE网络能力IE支持的默认版本，按以下版本进行设置： 
 
TS29060 V9.5.0以前的版本。
 
 
TS29060 V9.5.0和之后的版本。
 
 
系统的默认配置为TS29.060 V9.5.0 Ago（V9.5.0 Ago）。 
注意事项 
[ADD UENETWORKCAPVERFG]是具体对端网元的单独配置，优先级高于默认配置，只有在没有单独配置时默认配置才会生效。
参数说明 
标识|名称|类型|说明
---|---|---|---
V950GTPV1VERSION|UE网络能力IE支持的默认版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置对端网元支持的缺省GTPV1版本。V9.5.0以前的版本：TS29060 V9.5.0以前的版本。V9.5.0和以后的版本：TS29060 V9.5.0和之后的版本。
命令举例 
设置UE网络能力IE支持的默认版本为V9.5.0 Ago。 
SET DEFAULT UENETWORKCAPVERFG:V950GTPV1VERSION="V9.5.0 Ago"; 
父主题： [UE网络能力IE支持的版本]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询UE网络能力IE支持的默认版本(SHOW DEFAULT UENETWORKCAPVERFG) 
## 查询UE网络能力IE支持的默认版本(SHOW DEFAULT UENETWORKCAPVERFG) 
命令功能 
该命令用于查询UE网络能力IE支持的默认版本。
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
V950GTPV1VERSION|UE网络能力IE支持的默认版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置对端网元支持的缺省GTPV1版本。V9.5.0以前的版本：TS29060 V9.5.0以前的版本。V9.5.0和以后的版本：TS29060 V9.5.0和之后的版本。
命令举例 
查询UE网络能力IE支持的默认版本。 
SHOW DEFAULT UENETWORKCAPVERFG; 
`
命令 (No.1): SHOW DEFAULT UENETWORKCAPVERFG;
操作维护                      UE网络能力IE支持的默认版本   
-----------------------------------------------------------
修改                            TS29.060 V9.5.0以前标准	               
-----------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [UE网络能力IE支持的版本]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增UE网络能力IE支持的版本(ADD UENETWORKCAPVERFG) 
## 新增UE网络能力IE支持的版本(ADD UENETWORKCAPVERFG) 
命令功能 
该命令用于新增UE网络能力IE支持的版本，按以下版本进行设置： 
 
TS29060 V9.5.0以前的版本。
 
 
TS29060 V9.5.0和之后的版本。
 
 
注意事项 
 
配置对端网元的版本后，也需要在对端网元上配置自身网元的版本，且版本要相同。
 
 
ADD UENETWORKCAPVERFG是具体对端网元的单独配置，优先级高于默认配置，只有在没有单独配置时默认配置才会生效。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端网元的IP|参数可选性:必选参数；参数类型:地址|对端网元的IP地址。
UENETWORKCAPVERFG|UE网络能力IE支持的版本|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:V9.5.0 Ago。|该参数用于设置对端网元支持的GTPV1版本，取值包括：V9.5.0以前的版本：TS29060 V9.5.0以前的版本。V9.5.0和以后的版本：TS29060 V9.5.0和之后的版本。
命令举例 
新增IP为10.43.150.10的UE网络能力IE支持的版本。 
ADD UENETWORKCAPVERFG:IP="10.43.150.10",UENETWORKCAPVERFG="V9.5.0 Ago"; 
父主题： [UE网络能力IE支持的版本]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改UE网络能力IE支持的版本(SET UENETWORKCAPVERFG) 
## 修改UE网络能力IE支持的版本(SET UENETWORKCAPVERFG) 
命令功能 
该命令用于修改UE网络能力IE支持的版本。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端网元的IP|参数可选性:必选参数；参数类型:地址|对端网元的IP地址。
UENETWORKCAPVERFG|UE网络能力IE支持的版本|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置对端网元支持的GTPV1版本，取值包括：V9.5.0以前的版本：TS29060 V9.5.0以前的版本。V9.5.0和以后的版本：TS29060 V9.5.0和之后的版本。
命令举例 
修改IP为10.43.150.10的UE网络能力IE支持的版本。 
SET UENETWORKCAPVERFG:IP="10.43.150.10",UENETWORKCAPVERFG="V9.5.0 Ago"; 
父主题： [UE网络能力IE支持的版本]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除UE网络能力IE支持的版本(DEL UENETWORKCAPVERFG) 
## 删除UE网络能力IE支持的版本(DEL UENETWORKCAPVERFG) 
命令功能 
该命令用于删除UE网络能力IE支持的版本。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端网元的IP|参数可选性:必选参数；参数类型:地址|对端网元的IP地址。
命令举例 
删除IP为10.43.150.10的UE网络能力IE支持的版本。 
DEL UENETWORKCAPVERFG:IP="10.43.150.10"; 
父主题： [UE网络能力IE支持的版本]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询UE网络能力IE支持的版本(SHOW UENETWORKCAPVERFG) 
## 查询UE网络能力IE支持的版本(SHOW UENETWORKCAPVERFG) 
命令功能 
该命令用于查询UE网络能力IE支持的版本。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端网元的IP|参数可选性:任选参数；参数类型:地址|对端网元的IP地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端网元的IP|参数可选性:任选参数；参数类型:地址|对端网元的IP地址。
UENETWORKCAPVERFG|UE网络能力IE支持的版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置对端网元支持的GTPV1版本，取值包括：V9.5.0以前的版本：TS29060 V9.5.0以前的版本。V9.5.0和以后的版本：TS29060 V9.5.0和之后的版本。
命令举例 
查询UE网络能力IE支持的版本。 
SHOW UENETWORKCAPVERFG:IP="10.43.150.10"; 
`
命令 (No.1): SHOW UENETWORKCAPVERFG:IP="10.43.150.10";
操作维护                      对端网元的IP               UE网络能力IE支持的版本   
--------------------------------------------------------------------------------
复制 修改 删除                10.43.150.10               TS29.060 V9.5.0以前标准	              
--------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [UE网络能力IE支持的版本]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# GPRS地址解析配置 
# GPRS地址解析配置 
背景知识 
用户发起附着/路由区更新请求或基站发起切换请求/RIM消息，SGSN收到请求后，根据逻辑名称DNS或本地解析得到目标局SGSN的地址，根据选择策略确定一个SGSN地址，最终SGSN通过选定的SGSN地址与目标局SGSN进行业务交互。 
本地解析目标局SGSN地址的逻辑名称共有三种方式，RNC，RAI，NRI；三种方式的逻辑名称组成如下： 
 
RNC标识具有固定格式“RNCIDxxxx.MNCyyy.MCCzzz.GPRS”；
 
 
RAI标识具有固定格式“RACxxxx.LACyyyy.MNCzzz.MCCwww.GPRS”；
 
 
NRI标识具有固定格式“nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs。
 
 
            术语：
            RIM：无线接入网络信息管理（Radio Access Network Information Management） 
DNS：域名服务器（Domain Name Server） 
RNC：无线网络控制器（Radio Network Controller），这里使用RNCID，即无线网络控制器标识。 
RAI：路由区标识（Routeing Area Identity） 
NRI：网络资源标识 （Network Resource Identifier） 
LAC：位置区域码（Location Area Code） 
RAC：路由区编码（Routing Area Code） 
MCC：移动国家号码（Mobile Country Code） 
MNC：移动网号（Mobile Network Code） 
功能描述 
GPRS地址解析配置，用于SGSN使用GPRS格式的逻辑名称本地解析得到目标局SGSN的IP地址。 
用户发起附着/路由区更新请求或基站发起切换请求/RIM消息，SGSN收到后，一般根据RAI组成的逻辑名称，本地解析得到目标局SGSN的IP地址；以下两种情况不同： 
 
如果切换请求或RIM消息中携带目标RNC，则SGSN根据目标RNC组成的逻辑名称，本地解析得到目标局SGSN的IP地址。
 
 
如果参与本次业务流程的两个SGSN局在SGSN POOL中，则SGSN根据NRI+RAC组成的逻辑名称，本地解析得到目标局SGSN的IP地址。
 
 
配置GPRS地址解析功能的流程如下： 
                        SGSN地址解析配置，配置命令为：
                        [ADD SGSNHOST]
                        。
                    
                        SGSN地址解析IP地址配置，是对已配置的SGSN的IP地址进行增加或删除，配置命令为：
                        [ADD SGSNHOST IPADDR]
                        或
                        [DEL SGSNHOST IPADDR]
                        。
                    
相关主题 
 
新增SGSN地址解析配置(ADD SGSNHOST)
 
 
修改SGSN地址解析配置(SET SGSNHOST)
 
 
增加SGSN地址解析IP地址(ADD SGSNHOST IPADDR)
 
 
删除SGSN地址解析IP地址(DEL SGSNHOST IPADDR)
 
 
删除SGSN地址解析配置(DEL SGSNHOST)
 
 
查询SGSN地址解析配置(SHOW SGSNHOST)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增SGSN地址解析配置(ADD SGSNHOST) 
## 新增SGSN地址解析配置(ADD SGSNHOST) 
命令功能 
该命令用于新增SGSN地址解析配置。当DNS服务器出现故障，或者测试局点进行测试而无需DNS服务器时，需要通过本地执行地址解析时，使用该命令。命令执行成功后，若SGSN配置本地解析优先于DNS地址解析，则SGSN优先执行本地地址解析，如果匹配成功，则不会进行DNS地址解析，匹配记录中的一个IP地址即作为目标地址；若SGSN配置DNS地址解析优先于本地地址解析，则SGSN优先执行DNS地址解析，如果DNS地址解析失败，则继续执行本地地址解析，匹配记录中的一个IP地址即作为目标地址。 
注意事项 
 
该命令和EPC HOST解析配置共用记录数，最大支持的记录数为4096。
 
 
SGSN地址解析优先级配置软参默认是0，即优先选择本地解析，解析失败才向DNS服务器去解析，如果希望改变优先级，可以调整软参SGSN地址解析优先级配置的设置。
 
 
SGSN设置本地地址解析优先DNS地址解析的配置命令为：SET SOFTWARE PARAMETER:PARAID=65592,PARAVALUE=0;
 
 
SGSN设置DNS地址解析优先本地地址解析的配置命令为：SET SOFTWARE PARAMETER:PARAID=65592,PARAVALUE=2;
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~42个字符。|逻辑名称指根据RAI或者RNCID等构成的对应的SGSN的域名，根据此域名可以解析得到SGSN的IP地址，具体格式如下：RNC标识具有固定格式“rncxxxx.mncyyy.mcczzz.gprs”，其中 xxxx 为 4 位数值表示的 RNC，不足4位的靠前补零；yyy、zzz为3位数值表示的MNC、MCC，不足3位的，靠前补零。x为十六进制数，y、z 为十进制数。 如：RNC ID为5、MNC为03、MCC460时，格式为：rnc0005.mnc003.mcc460.gprs。RAI标识具有固定形式“racxxxx.lacyyyy.mnczzz.mccwww.gprs”，其中xxxx、 yyyy分别为4位数值表示的RAC、LAC不足4位的靠前补零；zzz、www为3位数值表示的 MNC、MCC，不足3位的，靠前补零。x、y 为十六进制数，z、w 为十进制数。 如：RAC为5、LAC为3、MNC为3、MCC460时，格式为：rac0005.lac0003.mnc003.mcc460.gprs。NRI标识具有固定形式 “nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs”，其中 CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16 进位数字，Y、Z为10 进位数字，位数不足的，在前面补0。 如：NRI为5、RAC为5、LAC为3、MNC为03、MCC460时，格式为：nri0005.rac0005.lac0003.mnc003.mcc460.gprs
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|目标局IP地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址。IP地址既可以是IPv4地址，也可以是IPv6地址。
命令举例 
新增SGSN地址解析，逻辑名称为rac0002.lac0003.mnc004.mcc460.gprs，地址为1.0.0.2和2.0.0.2。 
ADD SGSNHOST:NAME="rac0002.lac0003.mnc004.mcc460.GPRS",IPADDR="1.0.0.2"&"2.0.0.2"; 
父主题： [GPRS地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改SGSN地址解析配置(SET SGSNHOST) 
## 修改SGSN地址解析配置(SET SGSNHOST) 
命令功能 
该命令用于修改SGSN地址解析配置。当SGSN地址解析配置发生变化时，使用该命令。命令执行成功后，若SGSN配置本地解析优先于DNS地址解析，则SGSN优先执行本地地址解析，如果匹配成功，则不会进行DNS地址解析，匹配记录中的一个IP地址即作为目标地址；若SGSN配置DNS地址解析优先于本地地址解析，则SGSN优先执行DNS地址解析，如果DNS地址解析失败，则继续执行本地地址解析，匹配记录中的一个IP地址即作为目标地址。 
注意事项 
 
该命令和EPC HOST解析配置共用记录数，最大支持的记录数为4096。
 
 
SGSN地址解析优先级配置软参默认是0，即优先选择本地解析，解析失败才向DNS服务器去解析，如果希望改变优先级，可以调整软参SGSN地址解析优先级配置的设置。
 
 
SGSN设置本地地址解析优先DNS地址解析的配置命令为：SET SOFTWARE PARAMETER :PARAID=65592,PARAVALUE=0;
 
 
SGSN设置DNS地址解析优先本地地址解析的配置命令为：SET SOFTWARE PARAMETER :PARAID=65592,PARAVALUE=2;
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~42个字符。|逻辑名称指根据RAI或者RNCID等构成的对应的SGSN的域名，根据此域名可以解析得到SGSN的IP地址，具体格式如下：RNC标识具有固定格式“rncxxxx.mncyyy.mcczzz.gprs”，其中 xxxx 为 4 位数值表示的 RNC，不足4位的靠前补零；yyy、zzz为3位数值表示的MNC、MCC，不足3位的，靠前补零。x为十六进制数，y、z 为十进制数。 如：RNC ID为5、MNC为03、MCC460时，格式为：rnc0005.mnc003.mcc460.gprs。RAI标识具有固定形式“racxxxx.lacyyyy.mnczzz.mccwww.gprs”，其中xxxx、 yyyy分别为4位数值表示的RAC、LAC不足4位的靠前补零；zzz、www为3位数值表示的 MNC、MCC，不足3位的，靠前补零。x、y 为十六进制数，z、w 为十进制数。 如：RAC为5、LAC为3、MNC为3、MCC460时，格式为：rac0005.lac0003.mnc003.mcc460.gprs。NRI标识具有固定形式 “nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs”，其中 CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16 进位数字，Y、Z为10 进位数字，位数不足的，在前面补0。 如：NRI为5、RAC为5、LAC为3、MNC为03、MCC460时，格式为：nri0005.rac0005.lac0003.mnc003.mcc460.gprs
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|目标局IP地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址。IP地址既可以是IPv4地址，也可以是IPv6地址。
命令举例 
将逻辑名称为rac0002.lac0003.mnc004.mcc460.gprs的SGSN地址解析的地址修改为1.0.0.23和2.0.0.23。 
SET SGSNHOST:NAME="rac0002.lac0003.mnc004.mcc460.GPRS",IPADDR="1.0.0.23"&"2.0.0.23"; 
父主题： [GPRS地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 增加SGSN地址解析IP地址(ADD SGSNHOST IPADDR) 
## 增加SGSN地址解析IP地址(ADD SGSNHOST IPADDR) 
命令功能 
该命令用于在SGSN地址解析中增加一个IP地址。当多个SGSN进行SGSN POOL组网的时候，在SGSN POOL内的用户移动到SGSN POOL内的SGSN进行接入的时候，会从老的SGSN获取用户信息，需要根据MS携带的OLD RAI解析出用户所在的SGSN。而同一个RAI被POOL内的多个SGSN管理，根据RAI解析出来的多个SGSN中选择一个SGSN作为Default SGSN，由为Default SGSN再进一步解析用户真正所在的SGSN。当更多的SGSN加入到SGSN POOL时，需要在对应的SGSN解析配置中增加IP地址时，使用该命令。增加IP地址成功后，SGSN能够根据本地解析选择新增加的SGSN作为Default SGSN，对POOL内的信令进行负荷分担，并由此SGSN去解析用户真正所在的SGSN IP。 
注意事项 
增加的SGSN IP建议为有效的IP地址，避免造成业务失败。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~42个字符。|逻辑名称指根据RAI或者RNCID等构成的对应的SGSN的域名，根据此域名可以解析得到SGSN的IP地址，具体格式如下：RNC标识具有固定格式“rncxxxx.mncyyy.mcczzz.gprs”，其中 xxxx 为 4 位数值表示的 RNC，不足4位的靠前补零；yyy、zzz为3位数值表示的MNC、MCC，不足3位的，靠前补零。x为十六进制数，y、z 为十进制数。 如：RNC ID为5、MNC为03、MCC460时，格式为：rnc0005.mnc003.mcc460.gprs。RAI标识具有固定形式“racxxxx.lacyyyy.mnczzz.mccwww.gprs”，其中xxxx、 yyyy分别为4位数值表示的RAC、LAC不足4位的靠前补零；zzz、www为3位数值表示的 MNC、MCC，不足3位的，靠前补零。x、y 为十六进制数，z、w 为十进制数。 如：RAC为5、LAC为3、MNC为3、MCC460时，格式为：rac0005.lac0003.mnc003.mcc460.gprs。NRI标识具有固定形式 “nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs”，其中 CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16 进位数字，Y、Z为10 进位数字，位数不足的，在前面补0。 如：NRI为5、RAC为5、LAC为3、MNC为03、MCC460时，格式为：nri0005.rac0005.lac0003.mnc003.mcc460.gprs
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|目标局IP地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址。IP地址既可以是IPv4地址，也可以是IPv6地址。
命令举例 
为逻辑名称为rac0002.lac0003.mnc004.mcc460.gprs的SGSN地址解析配置增加IP地址，地址为3.1.1.3。 
ADD SGSNHOST IPADDR:NAME="rac0002.lac0003.mnc004.mcc460.gprs",IPADDR="3.1.1.3"; 
父主题： [GPRS地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除SGSN地址解析IP地址(DEL SGSNHOST IPADDR) 
## 删除SGSN地址解析IP地址(DEL SGSNHOST IPADDR) 
命令功能 
该命令用于在SGSN地址解析中删除IP地址。当SGSN POOL中的某个SGSN退网，需要在对应的SGSN HOST解析配置中根据其管理的RAI构成的域名中删除相应的IP地址时，使用该命令。删除IP地址后，SGSN不会再解析到对应的SGSN IP地址。 
注意事项 
使用该命令不能删除最后一个IP地址，若强制使用，命令将执行失败。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~42个字符。|逻辑名称指根据RAI或者RNCID等构成的对应的SGSN的域名，根据此域名可以解析得到SGSN的IP地址，具体格式如下：RNC标识具有固定格式“rncxxxx.mncyyy.mcczzz.gprs”，其中 xxxx 为 4 位数值表示的 RNC，不足4位的靠前补零；yyy、zzz为3位数值表示的MNC、MCC，不足3位的，靠前补零。x为十六进制数，y、z 为十进制数。 如：RNC ID为5、MNC为03、MCC460时，格式为：rnc0005.mnc003.mcc460.gprs。RAI标识具有固定形式“racxxxx.lacyyyy.mnczzz.mccwww.gprs”，其中xxxx、 yyyy分别为4位数值表示的RAC、LAC不足4位的靠前补零；zzz、www为3位数值表示的 MNC、MCC，不足3位的，靠前补零。x、y 为十六进制数，z、w 为十进制数。 如：RAC为5、LAC为3、MNC为3、MCC460时，格式为：rac0005.lac0003.mnc003.mcc460.gprs。NRI标识具有固定形式 “nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs”，其中 CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16 进位数字，Y、Z为10 进位数字，位数不足的，在前面补0。 如：NRI为5、RAC为5、LAC为3、MNC为03、MCC460时，格式为：nri0005.rac0005.lac0003.mnc003.mcc460.gprs
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|目标局IP地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址。IP地址既可以是IPv4地址，也可以是IPv6地址。
命令举例 
将逻辑名称为rac0002.lac0003.mnc004.mcc460.gprs的SGSN地址解析中的3.1.1.3地址删除。 
DEL SGSNHOST IPADDR:NAME="rac0002.lac0003.mnc004.mcc460.gprs",IPADDR="3.1.1.3"; 
父主题： [GPRS地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除SGSN地址解析配置(DEL SGSNHOST) 
## 删除SGSN地址解析配置(DEL SGSNHOST) 
命令功能 
该命令用于删除SGSN地址解析配置。当不需要在SGSN中本地解析SGSN IP地址时、或者统一采用DNS服务器进行解析时，使用该命令。配置删除后，SGSN不会在本地解析得到对应的SGSN IP地址。 
注意事项 
使用该命令需要运营商运维人员确认不需要再SGSN上根据HOST解析SGSN地址，统一采用DNS服务器解析或者是一个测试配置测试完毕后要进行删除。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~42个字符。|逻辑名称指根据RAI或者RNCID等构成的对应的SGSN的域名，根据此域名可以解析得到SGSN的IP地址，具体格式如下：RNC标识具有固定格式“rncxxxx.mncyyy.mcczzz.gprs”，其中 xxxx 为 4 位数值表示的 RNC，不足4位的靠前补零；yyy、zzz为3位数值表示的MNC、MCC，不足3位的，靠前补零。x为十六进制数，y、z 为十进制数。 如：RNC ID为5、MNC为03、MCC460时，格式为：rnc0005.mnc003.mcc460.gprs。RAI标识具有固定形式“racxxxx.lacyyyy.mnczzz.mccwww.gprs”，其中xxxx、 yyyy分别为4位数值表示的RAC、LAC不足4位的靠前补零；zzz、www为3位数值表示的 MNC、MCC，不足3位的，靠前补零。x、y 为十六进制数，z、w 为十进制数。 如：RAC为5、LAC为3、MNC为3、MCC460时，格式为：rac0005.lac0003.mnc003.mcc460.gprs。NRI标识具有固定形式 “nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs”，其中 CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16 进位数字，Y、Z为10 进位数字，位数不足的，在前面补0。 如：NRI为5、RAC为5、LAC为3、MNC为03、MCC460时，格式为：nri0005.rac0005.lac0003.mnc003.mcc460.gprs
命令举例 
将逻辑名称为rac0002.lac0003.mnc004.mcc460.gprs的SGSN地址解析删除。 
DEL SGSNHOST:NAME="rac0002.lac0003.mnc004.mcc460.gprs"; 
父主题： [GPRS地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN地址解析配置(SHOW SGSNHOST) 
## 查询SGSN地址解析配置(SHOW SGSNHOST) 
命令功能 
该命令用于根据RAI/RNCID按照RAI/RNCID构成的SGSN域名格式查询SGSN地址解析配置，获得此域名对应的SGSN的IP地址列表。当需要查询SGSN本地配置的RAI/RNCID的地址解析配置时，使用该命令。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~42个字符。|逻辑名称指根据RAI或者RNCID等构成的对应的SGSN的域名，根据此域名可以解析得到SGSN的IP地址，具体格式如下：RNC标识具有固定格式“rncxxxx.mncyyy.mcczzz.gprs”，其中 xxxx 为 4 位数值表示的 RNC，不足4位的靠前补零；yyy、zzz为3位数值表示的MNC、MCC，不足3位的，靠前补零。x为十六进制数，y、z 为十进制数。 如：RNC ID为5、MNC为03、MCC460时，格式为：rnc0005.mnc003.mcc460.gprs。RAI标识具有固定形式“racxxxx.lacyyyy.mnczzz.mccwww.gprs”，其中xxxx、 yyyy分别为4位数值表示的RAC、LAC不足4位的靠前补零；zzz、www为3位数值表示的 MNC、MCC，不足3位的，靠前补零。x、y 为十六进制数，z、w 为十进制数。 如：RAC为5、LAC为3、MNC为3、MCC460时，格式为：rac0005.lac0003.mnc003.mcc460.gprs。NRI标识具有固定形式 “nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs”，其中 CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16 进位数字，Y、Z为10 进位数字，位数不足的，在前面补0。 如：NRI为5、RAC为5、LAC为3、MNC为03、MCC460时，格式为：nri0005.rac0005.lac0003.mnc003.mcc460.gprs
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|配置标识|参数可选性:任选参数；参数类型:整数。|输出参数，由系统自动生成。
NAME|逻辑名称|参数可选性:任选参数；参数类型:字符型。|逻辑名称指根据RAI或者RNCID等构成的对应的SGSN的域名，根据此域名可以解析得到SGSN的IP地址，具体格式如下：RNC标识具有固定格式“rncxxxx.mncyyy.mcczzz.gprs”，其中 xxxx 为 4 位数值表示的 RNC，不足4位的靠前补零；yyy、zzz为3位数值表示的MNC、MCC，不足3位的，靠前补零。x为十六进制数，y、z 为十进制数。 如：RNC ID为5、MNC为03、MCC460时，格式为：rnc0005.mnc003.mcc460.gprs。RAI标识具有固定形式“racxxxx.lacyyyy.mnczzz.mccwww.gprs”，其中xxxx、 yyyy分别为4位数值表示的RAC、LAC不足4位的靠前补零；zzz、www为3位数值表示的 MNC、MCC，不足3位的，靠前补零。x、y 为十六进制数，z、w 为十进制数。 如：RAC为5、LAC为3、MNC为3、MCC460时，格式为：rac0005.lac0003.mnc003.mcc460.gprs。NRI标识具有固定形式 “nriCCCC.racDDDD.lacEEEE.mncYYY.mccZZZ.gprs”，其中 CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16 进位数字，Y、Z为10 进位数字，位数不足的，在前面补0。 如：NRI为5、RAC为5、LAC为3、MNC为03、MCC460时，格式为：nri0005.rac0005.lac0003.mnc003.mcc460.gprs
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|被查询网元IP地址，可以是IPv4地址，也可以是IPv6地址。
命令举例 
查询逻辑名称为rac0002.lac0003.mnc004.mcc460.gprs的SGSN地址解析。 
SHOW SGSNHOST:NAME="rac0002.lac0003.mnc004.mcc460.gprs"; 
`
2016-09-06 08:25:24 命令 (No.1): SHOW SGSNHOST:NAME="rac0002.lac0003.mnc004.mcc460.gprs";
操作维护         配置标识   逻辑名称                             IP地址
-----------------------------------------------------------------------
复制 修改 删除   1          rac0002.lac0003.mnc004.mcc460.gprs   1.0.0.2
复制 修改 删除   1          rac0002.lac0003.mnc004.mcc460.gprs   2.0.0.2
-----------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.024 秒）。
` 
父主题： [GPRS地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# EPC地址解析配置 
# EPC地址解析配置 
背景知识 
 
SGW选择：
用户发起附着或跟踪区更新请求，或着eNodeB发起SGW改变的切换请求，MME收到请求后，根据逻辑名称DNS或本地解析得到SGW的地址，根据选择策略确定一个SGW地址，最终MME通过选定的SGW地址与SGW进行业务交互。
用户发起附着/路由区更新请求，或者RNC发起SGW改变的切换请求，SGSN收到请求后，发现用户驻留在EPC网络，则根据逻辑名称DNS或本地解析得到SGW的地址，根据选择策略确定一个SGW地址，最终SGSN通过选定的SGW地址与SGW进行业务交互。
 
 
目标MME选择：
用户发起附着/跟踪区更新请求或eNodeB发起切换请求/RIM消息，MME收到请求后，根据逻辑名称DNS或本地解析得到目标局MME的地址，根据选择策略确定一个MME地址，最终MME通过选定的MME地址与目标局MME进行业务交互。
用户发起附着/路由区更新请求或RNC发起切换请求/RIM消息，SGSN收到请求后，根据逻辑名称DNS或本地解析得到目标局MME的地址，根据选择策略确定一个MME地址，最终SGSN通过选定的MME地址与目标局MME进行业务交互。
 
 
目标SGSN选择：
用户发起附着/跟踪区更新请求或eNodeB发起切换请求/RIM消息，MME收到请求后，根据逻辑名称DNS或本地解析得到目标局SGSN的地址，根据选择策略确定一个SGSN地址，最终MME通过选定的SGSN地址与目标局SGSN进行业务交互。
用户发起附着/路由区更新请求或RNC发起切换请求/RIM消息，SGSN收到请求后，根据逻辑名称DNS或本地解析得到目标局SGSN的地址，根据选择策略确定一个SGSN地址，最终SGSN通过选定的SGSN地址与目标局SGSN进行业务交互。
 
 
目标MSC选择：
eNodeB根据UE测量报告发起IMS控制的VoIP 语音到CS域语音的SRVCC切换，MME收到请求后，根据逻辑名称DNS或本地解析得到目标局MSC的地址，根据选择策略确定一个MSC地址，最终MME通过选定的MSC地址与目标局MSC进行业务交互。
 
 
MME/SGSN本地解析SGW/SGSN/MME/MSC地址的逻辑名称共有七种方式，其各自的逻辑名称组成如下： 
 
TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”；
 
 
MME节点标识具有固定格式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”；
 
 
MME Pool标识具有固定格式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”；
 
 
EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”；
 
 
EPC RAI标识具有固定格式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”；
 
 
EPC NRI标识具有固定格式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”；
 
 
eNB标识具有固定格式“enb<XXXXXXX>.enb.epc.mnc<YYY>.mcc<ZZZ>.3gppnetwork.org”。
 
 
术语： 
TA：跟踪区域（Tracking Area） 
TAC：跟踪区编码（Tracking Area Code） 
MMEC：MME编码（MME Code） 
MMEGI：MME群组标识（MME Group Identity） 
RNC：无线网络控制器（Radio Network Controller），这里使用RNCID，即无线网络控制器标识。 
LAC：位置区域码（Location Area Code） 
RAC：路由区编码（Routing Area Code） 
eNB：演进的NodeB（evolved Node B），这里使用eNBID，即演进的NodeB标识。 
IMS：IP多媒体子系统（IP Multimedia Subsystem） 
MSC：移动交换中心（Mobile switching center） 
CS：电路域交换（Circuit Switched） 
VoIP：将模拟的声音讯号经过压缩与封包之后，以数据封包的形式在IP 网络的环境进行语音讯号的传输，通俗来说也就是互联网电话、网络电话或者简称IP电话的意思。（Voice over IP） 
SRVCC：单无线频率语音呼叫连续性（Single Radio Voice Call Continuity） 
RIM：无线接入网络信息管理（Radio Access Network Information Management） 
DNS：域名服务器（Domain Name Server） 
功能描述 
EPC地址解析配置，用于MME/SGSN使用EPC格式的逻辑名称本地解析得到目标局SGW/SGSN/MME/MSC的IP地址。 
 
SGW地址解析：
用户发起附着或跟踪区更新请求，或着eNodeB发起SGW改变的切换请求，MME收到后根据TAI和eNB标识组成的逻辑名称，本地解析得到SGW的IP地址。
用户发起附着/路由区更新请求，或者RNC发起SGW改变的切换请求，SGSN收到后根据RAI和RNC标识组成的逻辑名称，本地解析得到SGW的IP地址。
 
 
MME地址解析：
用户发起附着/跟踪区更新请求或eNodeB发起切换请求/RIM消息，MME收到后根据TAI/eNB/MME节点标识/MME Pool标识组成的逻辑名称，本地解析得到目标局MME的IP地址。
用户发起附着/路由区更新请求或RNC发起切换请求/RIM消息，SGSN收到后根据RNC/MME节点标识/eNB标识组成的逻辑名称，本地解析得到目标局MME的IP地址。
 
 
SGSN地址解析：
用户发起附着/跟踪区更新请求或eNodeB发起切换请求/RIM消息，MME收到后根据RAI标识组成的逻辑名称，本地解析得到目标局SGSN的IP地址。
用户发起附着/路由区更新请求或RNC发起切换请求/RIM消息，SGSN收到后根据RNC/RAI/NRI标识组成的逻辑名称，本地解析得到目标局SGSN的IP地址。
 
 
MSC地址解析：
eNodeB根据UE测量报告发起IMS控制的VoIP 语音到CS域语音的SRVCC切换，MME收到后根据RNC/RAI标识组成的逻辑名称，本地解析得到目标局MSC的IP地址。
 
 
配置EPC地址解析功能的流程如下： 
                        EPC地址解析配置，配置命令为：
                        [ADD EPCHOST]
                        。
                    
                        EPC地址解析IP地址配置，是对已配置的目标局SGW/SGSN/MME/MSC的IP地址进行增加或删除，配置命令为：
                        [ADD EPCHOST IPADDR]
                        或
                        [DEL EPCHOST IPADDR]
                        。
                    
相关主题 
 
设置EPC地址解析策略配置(SET EPCCFG)
 
 
查询EPC地址解析策略配置(SHOW EPCCFG)
 
 
新增EPC地址解析配置(ADD EPCHOST)
 
 
修改EPC地址解析配置(SET EPCHOST)
 
 
增加EPC地址解析IP地址(ADD EPCHOST IPADDR)
 
 
删除EPC地址解析IP地址(DEL EPCHOST IPADDR)
 
 
删除EPC地址解析配置(DEL EPCHOST)
 
 
查询EPC地址解析配置(SHOW EPCHOST)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置EPC地址解析策略(SET EPCCFG) 
## 设置EPC地址解析策略(SET EPCCFG) 
命令功能 
该命令用于设置EPC地址解析策略配置。当需要设置EPC地址解析的策略时，使用该命令进行配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPTACWILDRESOLVE|支持通配TAC的地址解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地解析SGW地址时，逻辑名称是否支持通配TAC。
命令举例 
设置EPC地址解析策略配置，支持通配TAC的地址解析设置为“YES”。 
SET EPCCFG:SUPTACWILDRESOLVE="YES"; 
父主题： [EPC地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询EPC地址解析策略(SHOW EPCCFG) 
## 查询EPC地址解析策略(SHOW EPCCFG) 
命令功能 
该命令用于查询EPC地址解析策略配置。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPTACWILDRESOLVE|支持通配TAC的地址解析|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地解析SGW地址时，逻辑名称是否支持通配TAC。
命令举例 
查询EPC地址解析策略配置。 
SHOW EPCCFG; 
`
命令 (No.1): SHOW EPCCFG
操作维护 支持通配TAC的地址解析 
-------------------------------
修改     不支持 
-------------------------------
记录数 1
命令执行成功（耗时 0.024 秒）。
` 
父主题： [EPC地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增EPC地址解析配置(ADD EPCHOST) 
## 新增EPC地址解析配置(ADD EPCHOST) 
命令功能 
该命令用于新增EPC FQDN地址解析配置。当DNS服务器出现故障，或者测试局点进行测试而无需DNS服务器时，MME/SGSN需要通过执行本地地址解析，查询SGW、SGSN或者其他MME网元地址时使用该命令。命令执行成功后，若MME/SGSN配置本地解析优先于DNS地址解析，则MME/SGSN优先执行本地地址解析，如果匹配成功，则不会进行DNS地址解析，匹配记录中的IP地址即作为被查询网元的IP地址；若MME/SGSN配置DNS地址解析优先于本地地址解析，则MME/SGSN优先执行DNS地址解析，如果DNS地址解析失败，则继续执行本地地址解析，匹配记录中的IP地址即作为被查询网元的IP地址。 
MME设置本地地址解析优先DNS地址解析的配置命令为：[SET SOFTWARE PARAMETER]:PARAID=65593,PARAVALUE=0;
MME设置DNS地址解析优先本地地址解析的配置命令为：[SET SOFTWARE PARAMETER]:PARAID=65593,PARAVALUE=2;
SGSN设置本地地址解析优先DNS地址解析的配置命令为：[SET SOFTWARE PARAMETER]:PARAID=65592,PARAVALUE=0;
SGSN设置DNS地址解析优先本地地址解析的配置命令为：[SET SOFTWARE PARAMETER]:PARAID=65592,PARAVALUE=2;
注意事项 
确定一个EPC FQDN地址解析记录，需要三个关键字：逻辑名称、业务类型和主机名。相同的逻辑名称，可以配置具有不同业务类型或者主机名的EPC FQDN地址解析记录。比如：[ADD EPCHOST]:NAME=tac-lb90.tac-hb02.tac.epc.mnc001.mcc460.3gppnetwork.org,SERVICE=x-3gpp-sgw,HOST=sgw53.zte.com,IPADDR=20.1.5.103,PROTOCOL="x-s5-gtp"&"x-s5-pmip"&"x-s8-gtp"&"x-s8-pmip";和[ADD EPCHOST]:NAME="tac-lb90.tac-hb02.tac.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="mme54.zte.com",IPADDR="20.1.5.103",PROTOCOL="x-s11"&"x-s10";。
如果配置了多个IP地址，且分属不同的子网段，则可以配置不同子网段具有不同的优先级，MME进行本地解析时，将会选择属于优先级最高子网网段的IP地址。配置子网优先级命令为：[ADD HOST SUBNET PRI]:NAME="tac-lb00.tac-hb52.tac.epc.mnc001.mcc460.3gppnetwork.org",SNPRI="20.1.5.0"-24-3;，其中"NAME"为EPC地址解析配置中的逻辑名称，"SNPRI"为配置的子网段、掩码长度以及优先级。
如果存在多个优先级相同的IP地址，则轮流选择这些IP地址作为目标地址。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.orgAMF逻辑名称AMF节点标识具有固定形式“ptXX.setYYY.regionZZ.amfi.5gc.mncWWW.mccVVV.3gppnetwork.org”，其中XX为2位数值表示的AMF Pointer、不足2位的，靠前补零。YYY为3位数值表示的AMF Set Id不足3位的，靠前补零。ZZ为2位数值表示的AMF Region Id不足2位的，靠前补零。WWW、VVV分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y、Z为十六进制数，W、V为十进制数。如：AMF Pointer为12、AMF Set为 1、AMF Region为48、MNC为12、MCC345时，格式为：pt12.set001.region48.amfi.5gc.mnc012.mcc345.3gppnetwork.org
SERVICE|支持服务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下几种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-amf: 目标局类型为AMF
HOST|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|网元的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|网元IP地址列表，列表中最多可以配置64个IP地址。IP地址既可以是IPv4地址，也可以是IPv6地址。
PROTOCOL|支持协议类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置被查询网元所支持的接口类型，目前支持如下类型：x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-s11(x-s11): S11接口x-gn(x-gn): Gn接口x-gp(x-gp): Gp接口x-s3(x-s3): S3接口x-s10(x-s10): S10接口，MME与MME之间的接口x-sv(x-sv): Sv接口，MME与MSC之间的接口，用于SRVCC切换x-s5-gtp+nc-nr：支持GTP协议网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议网络能力nr的S8接口。x-s11+nc-nr：网络能力nr的S11接口。x-n26(x-n26): N26接口
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|查询SGW或者PGW网元IP地址时，根据TAI FQDN或者RAI FQDN，查询得到多组EPC FQDN地址解析。此时，根据该参数从查询得到的多组EPC FQDN地址解析中，选择优先级最高的EPC FQDN地址解析。
NAPTRWEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:200。|查询SGW或者PGW网元IP地址时，根据TAI FQDN或者RAI FQDN，查询得到多组EPC FQDN地址解析。此时，首先根据优先级从查询得到的多组EPC FQDN地址解析中，选择优先级最高的EPC FQDN地址解析。若多组EPC FQDN地址解析都配置了最高优先级，则根据该参数在此多组EPC FQDN地址解析中按比例选择一组EPC FQDN地址解析。比如 ，第一组地址解析和第二组地址解析具有最高优先级，其负荷因子分别为2和3，那么在5次地址解析中，将会选择两次第一组地址解析和三次第二组地址解析。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NORMAL。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网SGW/MME/SGSN的选择。定义参见3GPP 29.272第7.3.202节。
命令举例 
新增EPC地址解析配置，逻辑名称是"mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org"，支持服务类别是"x-3gpp-mme"，主机名为"mme50.zte.com.cn"，IP地址为"131.1.17.159"，支持协议类型为"x-s10"、"x-gn"和"x-gp"。 
ADD EPCHOST:NAME="mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="mme50.zte.com.cn",IPADDR="131.1.17.159",PROTOCOL="x-gn"&"x-gp"&"x-s10"; 
父主题： [EPC地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改EPC地址解析配置(SET EPCHOST) 
## 修改EPC地址解析配置(SET EPCHOST) 
命令功能 
该命令用于修改特定EPC FQDN本地地址解析配置的IP地址、目标局所支持的接口类型。当目标地址发生改变，或者新增配置时目标局接口类型不满足现时需求时，使用该命令。命令执行成功后，MME/SGSN配置本地解析优先于DNS地址解析，则MME/SGSN优先执行本地地址解析，如果匹配成功，则不会进行DNS地址解析，匹配记录中的IP地址即作为目标地址；若MME/SGSN配置DNS地址解析优先于本地地址解析，则MME/SGSN优先执行DNS地址解析，如果DNS地址解析失败，则继续执行本地地址解析，匹配记录中的IP地址即作为目标地址。 
MME设置本地地址解析优先DNS地址解析的配置命令为：[SET SOFTWARE PARAMETER] :PARAID=65593,PARAVALUE=0;
MME设置DNS地址解析优先本地地址解析的配置命令为：[SET SOFTWARE PARAMETER] :PARAID=65593,PARAVALUE=2;
SGSN设置本地地址解析优先DNS地址解析的配置命令为：[SET SOFTWARE PARAMETER]:PARAID=65592,PARAVALUE=0;
SGSN设置DNS地址解析优先本地地址解析的配置命令为：[SET SOFTWARE PARAMETER]:PARAID=65592,PARAVALUE=2;
注意事项 
确定一个EPC FQDN地址解析记录，需要三个关键字：逻辑名称、业务类型和主机名。相同的逻辑名称，可以配置具有不同业务类型或者主机名的EPC FQDN地址解析记录。比如：[ADD EPCHOST]:NAME="tac-lb90.tac-hb02.tac.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="sgw53.zte.com",IPADDR="20.1.5.103",PROTOCOL="x-s5-gtp"&"x-s5-pmip"&"x-s8-gtp"&"x-s8-pmip";和[ADD EPCHOST]:NAME="tac-lb90.tac-hb02.tac.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="mme54.zte.com",IPADDR="20.1.5.103",PROTOCOL="x-s11"&"x-s10";。
如果配置了多个IP地址，且分属不同的子网段，则可以配置不同子网段具有不同的优先级，MME进行本地解析时，将会选择属于优先级最高子网网段的IP地址。配置子网优先级命令为：[ADD HOST SUBNET PRI]:NAME="tac-lb00.tac-hb52.tac.epc.mnc001.mcc460.3gppnetwork.org",SNPRI="20.1.5.0"-24-3;，其中"NAME"为EPC地址解析配置中的逻辑名称，"SNPRI"为配置的子网段、掩码长度以及优先级。
如果存在多个优先级相同的IP地址，则轮流选择这些IP地址作为目标地址。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.orgAMF逻辑名称AMF节点标识具有固定形式“ptXX.setYYY.regionZZ.amfi.5gc.mncWWW.mccVVV.3gppnetwork.org”，其中XX为2位数值表示的AMF Pointer、不足2位的，靠前补零。YYY为3位数值表示的AMF Set Id不足3位的，靠前补零。ZZ为2位数值表示的AMF Region Id不足2位的，靠前补零。WWW、VVV分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y、Z为十六进制数，W、V为十进制数。如：AMF Pointer为12、AMF Set为 1、AMF Region为48、MNC为12、MCC345时，格式为：pt12.set001.region48.amfi.5gc.mnc012.mcc345.3gppnetwork.org
SERVICE|支持服务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下几种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-amf: 目标局类型为AMF
HOST|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|网元的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|网元IP地址列表，列表中最多可以配置64个IP地址。IP地址既可以是IPv4地址，也可以是IPv6地址。
PROTOCOL|支持协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置被查询网元所支持的接口类型，目前支持如下类型：x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-s11(x-s11): S11接口x-gn(x-gn): Gn接口x-gp(x-gp): Gp接口x-s3(x-s3): S3接口x-s10(x-s10): S10接口，MME与MME之间的接口x-sv(x-sv): Sv接口，MME与MSC之间的接口，用于SRVCC切换x-s5-gtp+nc-nr：支持GTP协议网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议网络能力nr的S8接口。x-s11+nc-nr：网络能力nr的S11接口。x-n26(x-n26): N26接口
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|查询SGW或者PGW网元IP地址时，根据TAI FQDN或者RAI FQDN，查询得到多组EPC FQDN地址解析。此时，根据该参数从查询得到的多组EPC FQDN地址解析中，选择优先级最高的EPC FQDN地址解析。
NAPTRWEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|查询SGW或者PGW网元IP地址时，根据TAI FQDN或者RAI FQDN，查询得到多组EPC FQDN地址解析。此时，首先根据优先级从查询得到的多组EPC FQDN地址解析中，选择优先级最高的EPC FQDN地址解析。若多组EPC FQDN地址解析都配置了最高优先级，则根据该参数在此多组EPC FQDN地址解析中按比例选择一组EPC FQDN地址解析。比如 ，第一组地址解析和第二组地址解析具有最高优先级，其负荷因子分别为2和3，那么在5次地址解析中，将会选择两次第一组地址解析和三次第二组地址解析。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网SGW/MME/SGSN的选择。定义参见3GPP 29.272第7.3.202节。
命令举例 
修改逻辑名称是"mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org"，支持服务类别是"x-3gpp-mme"，主机名为"mme50.zte.com.cn"的EPC地址解析，将支持协议类型修改为"x-s10"和"x-gn"。 
SET EPCHOST:NAME="mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="mme50.zte.com.cn",PROTOCOL="x-gn"&"x-s10"; 
父主题： [EPC地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 增加EPC地址解析IP地址(ADD EPCHOST IPADDR) 
## 增加EPC地址解析IP地址(ADD EPCHOST IPADDR) 
命令功能 
该命令用于向特定EPC FQDN地址解析中增加一个IP地址。 
注意事项 
确定一个EPC FQDN地址解析记录，需要三个关键字：逻辑名称、业务类型和主机名。相同的逻辑名称，可以配置具有不同业务类型或者主机名的EPC FQDN地址解析记录。比如：[ADD EPCHOST]:NAME="tac-lb90.tac-hb02.tac.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="sgw53.zte.com",IPADDR="20.1.5.103",PROTOCOL="x-s5-gtp"&"x-s5-pmip"&"x-s8-gtp"&"x-s8-pmip";和[ADD EPCHOST]:NAME="tac-lb90.tac-hb02.tac.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="mme54.zte.com",IPADDR="20.1.5.103",PROTOCOL="x-s11"&"x-s10";。
如果配置了多个IP地址，且分属不同的子网段，则可以配置不同子网段具有不同的优先级，MME进行本地解析时，将会选择属于优先级最高子网网段的IP地址。配置子网优先级命令为：[ADD HOST SUBNET PRI]:NAME="tac-lb00.tac-hb52.tac.epc.mnc001.mcc460.3gppnetwork.org",SNPRI="20.1.5.0"-24-3;，其中"NAME"为EPC地址解析配置中的逻辑名称，"SNPRI"为配置的子网段、掩码长度以及优先级。
如果存在多个优先级相同的IP地址，则轮流选择这些IP地址作为目标地址。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.orgAMF逻辑名称AMF节点标识具有固定形式“ptXX.setYYY.regionZZ.amfi.5gc.mncWWW.mccVVV.3gppnetwork.org”，其中XX为2位数值表示的AMF Pointer、不足2位的，靠前补零。YYY为3位数值表示的AMF Set Id不足3位的，靠前补零。ZZ为2位数值表示的AMF Region Id不足2位的，靠前补零。WWW、VVV分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y、Z为十六进制数，W、V为十进制数。如：AMF Pointer为12、AMF Set为 1、AMF Region为48、MNC为12、MCC345时，格式为：pt12.set001.region48.amfi.5gc.mnc012.mcc345.3gppnetwork.org
SERVICE|支持服务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下几种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-amf: 目标局类型为AMF
HOST|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|网元的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|网元IP地址，可以是IPv4地址，也可以是IPv6地址。
命令举例 
增加EPC地址解析IP地址，逻辑名称为"mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org"，支持服务类别为"x-3gpp-mme"，主机名为"mme50.zte.com.cn"，新增的IP地址为"131.2.17.159"。 
ADD EPCHOST IPADDR:NAME="mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="mme50.zte.com.cn",IPADDR="131.2.17.159"; 
父主题： [EPC地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除EPC地址解析IP地址(DEL EPCHOST IPADDR) 
## 删除EPC地址解析IP地址(DEL EPCHOST IPADDR) 
命令功能 
该命令用于删除特定EPC FQDN地址解析配置中某一个IP地址。 
注意事项 
确定一个EPC FQDN地址解析记录，需要三个关键字：逻辑名称、业务类型和主机名。相同的逻辑名称，可以配置具有不同业务类型或者主机名的EPC FQDN地址解析记录。 
若特定EPC FQDN地址解析配置中只配置了一个IP地址，则不能使用该命令删除该IP地址。若强制执行，命令执行失败。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.orgAMF逻辑名称AMF节点标识具有固定形式“ptXX.setYYY.regionZZ.amfi.5gc.mncWWW.mccVVV.3gppnetwork.org”，其中XX为2位数值表示的AMF Pointer、不足2位的，靠前补零。YYY为3位数值表示的AMF Set Id不足3位的，靠前补零。ZZ为2位数值表示的AMF Region Id不足2位的，靠前补零。WWW、VVV分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y、Z为十六进制数，W、V为十进制数。如：AMF Pointer为12、AMF Set为 1、AMF Region为48、MNC为12、MCC345时，格式为：pt12.set001.region48.amfi.5gc.mnc012.mcc345.3gppnetwork.org
SERVICE|支持服务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下几种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-amf: 目标局类型为AMF
HOST|主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|网元的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|网元IP地址既可以是IPv4地址，也可以是IPv6地址。
命令举例 
删除EPC地址解析IP地址，其逻辑名称为"mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org"，支持服务类别为"x-3gpp-mme"，主机名为"mme50.zte.com.cn"，被删除的IP地址为"131.2.17.159"。 
DEL EPCHOST IPADDR:NAME="mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="mme50.zte.com.cn",IPADDR="131.2.17.159"; 
父主题： [EPC地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除EPC地址解析配置(DEL EPCHOST) 
## 删除EPC地址解析配置(DEL EPCHOST) 
命令功能 
该命令用于删除特定逻辑名称所对应的全部EPC地址解析配置，或者特定EPC地址解析配置。 
若要删除特定逻辑名称所对应的全部EPC地址解析配置，则只需要填写“逻辑名称”这个参数。命令执行成功后，MME/SGSN将无法通过本地地址解析，获取“逻辑名称”所对应的任何目标局IP地址。 
若要删除特定EPC地址解析配置，则需要填写“逻辑名称”、“支持服务类别”、“主机名”。命令执行成功后，MME/SGSN将无法通过本地地址解析，获取“逻辑名称”与“支持服务类别”所对应的目标局IP地址。 
注意事项 
确定一个特定EPC FQDN地址解析记录，需要三个关键字：逻辑名称、业务类型和主机名。相同的逻辑名称，可以配置具有不同业务类型或者主机名的EPC FQDN地址解析记录。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.orgAMF逻辑名称AMF节点标识具有固定形式“ptXX.setYYY.regionZZ.amfi.5gc.mncWWW.mccVVV.3gppnetwork.org”，其中XX为2位数值表示的AMF Pointer、不足2位的，靠前补零。YYY为3位数值表示的AMF Set Id不足3位的，靠前补零。ZZ为2位数值表示的AMF Region Id不足2位的，靠前补零。WWW、VVV分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y、Z为十六进制数，W、V为十进制数。如：AMF Pointer为12、AMF Set为 1、AMF Region为48、MNC为12、MCC345时，格式为：pt12.set001.region48.amfi.5gc.mnc012.mcc345.3gppnetwork.org
SERVICE|支持服务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下几种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-amf: 目标局类型为AMF
HOST|主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|网元的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
命令举例 
删除逻辑名称为mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org的EPC地址解析配置。 
DEL EPCHOST:NAME="mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org"; 
父主题： [EPC地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询EPC地址解析配置(SHOW EPCHOST) 
## 查询EPC地址解析配置(SHOW EPCHOST) 
命令功能 
该命令用于查询全部EPC地址解析配置、特定逻辑名称所对应的全部EPC地址解析配置、特定逻辑名称所对应的特定EPC地址解析配置。 
注意事项 
确定一个特定EPC FQDN地址解析记录，需要三个关键字：逻辑名称、业务类型和主机名。相同的逻辑名称，可以配置具有不同业务类型或者主机名的EPC FQDN地址解析记录。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.orgAMF逻辑名称AMF节点标识具有固定形式“ptXX.setYYY.regionZZ.amfi.5gc.mncWWW.mccVVV.3gppnetwork.org”，其中XX为2位数值表示的AMF Pointer、不足2位的，靠前补零。YYY为3位数值表示的AMF Set Id不足3位的，靠前补零。ZZ为2位数值表示的AMF Region Id不足2位的，靠前补零。WWW、VVV分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y、Z为十六进制数，W、V为十进制数。如：AMF Pointer为12、AMF Set为 1、AMF Region为48、MNC为12、MCC345时，格式为：pt12.set001.region48.amfi.5gc.mnc012.mcc345.3gppnetwork.org
SERVICE|支持服务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下几种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-amf: 目标局类型为AMF
HOST|主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|网元的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:任选参数；参数类型:字符型。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.orgAMF逻辑名称AMF节点标识具有固定形式“ptXX.setYYY.regionZZ.amfi.5gc.mncWWW.mccVVV.3gppnetwork.org”，其中XX为2位数值表示的AMF Pointer、不足2位的，靠前补零。YYY为3位数值表示的AMF Set Id不足3位的，靠前补零。ZZ为2位数值表示的AMF Region Id不足2位的，靠前补零。WWW、VVV分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y、Z为十六进制数，W、V为十进制数。如：AMF Pointer为12、AMF Set为 1、AMF Region为48、MNC为12、MCC345时，格式为：pt12.set001.region48.amfi.5gc.mnc012.mcc345.3gppnetwork.org
SERVICE|支持服务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下几种网元类型：x-3gpp-sgw: 目标局类型为SGWx-3gpp-mme: 目标局类型为MMEx-3gpp-sgsn: 目标局类型为SGSN，包括GnGp SGSN和S4 SGSNx-3gpp-msc: 目标局类型为MSCx-3gpp-amf: 目标局类型为AMF
HOST|主机名|参数可选性:任选参数；参数类型:字符型。|网元的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|网元IP地址，可以是IPv4地址，也可以是IPv6地址。
PROTOCOL|支持协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置被查询网元所支持的接口类型，目前支持如下类型：x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-s11(x-s11): S11接口x-gn(x-gn): Gn接口x-gp(x-gp): Gp接口x-s3(x-s3): S3接口x-s10(x-s10): S10接口，MME与MME之间的接口x-sv(x-sv): Sv接口，MME与MSC之间的接口，用于SRVCC切换x-s5-gtp+nc-nr：支持GTP协议网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议网络能力nr的S8接口。x-s11+nc-nr：网络能力nr的S11接口。x-n26(x-n26): N26接口
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数。|查询SGW或者PGW网元IP地址时，根据TAI FQDN或者RAI FQDN，查询得到多组EPC FQDN地址解析。此时，根据该参数从查询得到的多组EPC FQDN地址解析中，选择优先级最高的EPC FQDN地址解析。
NAPTRWEIGHT|权重|参数可选性:任选参数；参数类型:整数。|查询SGW或者PGW网元IP地址时，根据TAI FQDN或者RAI FQDN，查询得到多组EPC FQDN地址解析。此时，首先根据优先级从查询得到的多组EPC FQDN地址解析中，选择优先级最高的EPC FQDN地址解析。若多组EPC FQDN地址解析都配置了最高优先级，则根据该参数在此多组EPC FQDN地址解析中按比例选择一组EPC FQDN地址解析。比如 ，第一组地址解析和第二组地址解析具有最高优先级，其负荷因子分别为2和3，那么在5次地址解析中，将会选择两次第一组地址解析和三次第二组地址解析。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:字符型。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网SGW/MME/SGSN的选择。定义参见3GPP 29.272第7.3.202节。
命令举例 
查询已配置的EPC地址解析信息。 
SHOW EPCHOST; 
`
2017-02-20 13:42:10 命令 (No.1): SHOW EPCHOST
操作维护         逻辑名称                                                 支持服务类别   主机名             IP地址         支持协议类型          优先级   权重    用户使用类型
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org   x-3gpp-mme     mme50.zte.com.cn   131.1.17.159   x-gn & x-gp & x-s10   0        200     普通用户
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.085 秒）。
` 
父主题： [EPC地址解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# EPC地址解析优选子网段配置 
# EPC地址解析优选子网段配置 
背景知识 
            
            对EPC格式的TAI/eNB/MME节点标识/MME Pool标识RNC/RAI/NRI组成的逻辑名称，MME/SGSN通过DNS查询或本地HOST查询（
            [ADD EPCHOST]
            ），可以得到一组SGW/SGSN/MME/MSC列表。MME/SGSN根据SGW/SGSN/MME/MSC的优先级、权重等选择策略选出一个SGW/SGSN/MME/MSC的IP地址。
        
功能描述 
MME/SGSN给选出的SGW/SGSN/MME/MSC的每个IP地址赋值一个子网优先级，选择高优先级的SGW/SGSN/MME/MSC的IP地址。如果高优先级的IP地址既有IPv4地址，又有IPv6地址，则根据软件参数“与邻接网元交互时业务IP双栈优选的IP类型”确定是选择IPv4地址还是IPv6地址。如果高优先级的IP地址有多个，则随机选择一个。目的是为了更准确地获取到本次服务的SGW/SGSN/MME/MSC的IP地址。 
该配置支持基于TAI/eNB/MME节点标识/MME Pool标识RNC/RAI/NRI组成的逻辑名称，对SGW/SGSN/MME/MSC的IP地址按照优先级进行优选。 
优先级根据用户的需求设定，值越小，其优先级越高。 
配置EPC地址解析优选子网段功能的流程如下： 
                        EPC地址解析中配置，
                        [ADD EPCHOST]
                        。或在DNS上查询。
                    
                        EPC地址解析优选子网段配置，
                        [ADD HOST SUBNET PRI]
                        。
                    
相关主题 
 
新增EPC地址解析优选子网配置(ADD HOST SUBNET PRI)
 
 
修改EPC地址解析优选子网配置(SET HOST SUBNET PRI)
 
 
删除EPC地址解析优选子网配置(DEL HOST SUBNET PRI)
 
 
查询EPC地址解析优选子网配置(SHOW HOST SUBNET PRI)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增EPC地址解析优选子网配置(ADD HOST SUBNET PRI) 
## 新增EPC地址解析优选子网配置(ADD HOST SUBNET PRI) 
命令功能 
该命令用于MME/SGSN新增EPC地址解析优选子网配置。当特定EPC地址解析配置中，配置了分属不同网段的目标IP地址时，MME/SGSN可以使用该命令设置不同子网段的优先级。该命令执行成功后，MME/SGSN依据配置的子网段优先级，选择具有最高子网段优先级的目标IP地址。 
注意事项 
新增该配置之前，首先需要新增EPC地址解析配置，配置命令为：[ADD EPCHOST]:NAME="tac-lb90.tac-hb02.tac.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="mme18.zte.com",IPADDR="20.1.5.103",PROTOCOL="x-s11"&"x-s10";
若具有最高子网段优先级的子网段对应多个目标IP地址，或者多个子网段具有相同的最高优先级，则在这些具有相同优先级的目标地址中，轮选一个IP地址作为最终的目标IP地址。 
特定逻辑名称，最多可以包含10个子网段IP优先级配置。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.org
SNPRI|子网优先级|参数可选性:必选参数；参数类型:复合参数|该参数是以下三个参数的组合：IP、MASKLEN、PRI。用于指定子网地址、掩码长度和优先级。
IP|子网地址|参数可选性:必选参数；参数类型:地址|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN|掩码长度|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI|优先级|参数可选性:必选参数；参数类型:整数；参数范围为:1~16。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
命令举例 
新增EPC地址解析优选子网配置，其中逻辑名称为mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org，子网地址为45.1.234.4，掩码为22位，优先级为2。 
ADD HOST SUBNET PRI:NAME="mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org",SNPRI="45.1.234.4"-"22"-"2"; 
父主题： [EPC地址解析优选子网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改EPC地址解析优选子网配置(SET HOST SUBNET PRI) 
## 修改EPC地址解析优选子网配置(SET HOST SUBNET PRI) 
命令功能 
该命令用于MME/SGSN修改特定子网段优先级。当特定子网段优先级需要调整时，MME/SGSN使用该命令。该命令执行成功后，MME/SGSN依据配置的子网段优先级，选择具有最高子网段优先级的目标IP地址。 
注意事项 
若具有最高子网段优先级的子网段对应多个目标IP地址，或者多个子网段具有相同的最高优先级，则在这些具有相同优先级的目标地址中，轮选一个IP地址作为最终的目标IP地址。 
特定逻辑名称，最多可以包含10个子网段IP优先级配置。 
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.org
IP|子网地址|参数可选性:必选参数；参数类型:地址|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN|掩码长度|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
命令举例 
将名称为mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org，子网地址为45.1.234.4，掩码为24位的EPC地址解析优选子网配置中的优先级修改为1。 
SET HOST SUBNET PRI:NAME="mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org",IP="45.1.234.4",MASKLEN=24,PRI=1; 
父主题： [EPC地址解析优选子网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除EPC地址解析优选子网配置(DEL HOST SUBNET PRI) 
## 删除EPC地址解析优选子网配置(DEL HOST SUBNET PRI) 
命令功能 
该命令用于删除特定逻辑名称所对应的全部子网段优先级配置，或者删除特定逻辑名称所对应的某个特定子网段优先级配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.org
IP|子网地址|参数可选性:特殊任选参数；参数类型:地址|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN|掩码长度|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~128。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
命令举例 
删除逻辑名称为mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org的EPC地址解析优选子网配置。 
DEL HOST SUBNET PRI:NAME="mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org"; 
父主题： [EPC地址解析优选子网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询EPC地址解析优选子网配置(SHOW HOST SUBNET PRI) 
## 查询EPC地址解析优选子网配置(SHOW HOST SUBNET PRI) 
命令功能 
该命令用于查询特定逻辑名称所对应的全部子网段优先级配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.org
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|逻辑名称|参数可选性:任选参数；参数类型:字符型。|逻辑名称包括：TAI逻辑名称TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，y、z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点逻辑名称MME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgMME Pool逻辑名称MME Pool标识具有固定形式“mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：MMEGI为5、MNC为4、MCC460时，格式为：mmegi0005.mme.epc.mnc004.mcc460.3gppnetwork.orgEPC RAI逻辑名称EPC RAI标识具有固定形式“racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org”，其中XXXX、YYYY分别为4位数值表示的RAC、LAC不足4位的，靠前补零。ZZZ,WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数，Z、W为十进制数。如：RAC为2、LAC为3、MNC为4、MCC460时，格式为：rac0002.lac0003.rac.epc.mnc004.mcc460.3gppnetwork.orgEPC NRI逻辑名称EPC NRI标识具有固定形式“nri-sgsnCCCC.racDDDD.lacEEEE.rac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中CCCC、DDDD、EEEE为4为数值表示的NRI、RAC和LAC，YYY和ZZZ为3位数值表示的MNC和MCC，C、D、E为16进位数字，Y、Z为10进位数字，位数不足的，在前面补0。例如：nri-sgsn003A.rac123A.lac234B.rac.epc.mnc092.mcc167.3gppnetwork.orgEPC RNC逻辑名称EPC RNC标识具有固定格式“rncXXXX.rnc.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXX分别为4位数值表示的RNC，不足4位的，靠前补零。YYY,ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：RNCID 5、MNC为2、MCC460时，格式为：rnc0005.rnc.epc.mnc002.mcc460.3gppnetwork.orgeNB逻辑名称eNB标识具有固定格式“enbXXXXX.enb.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中XXXXX为eNBID。YYY、ZZZ 为3位数值表示的MNC、MCC，不足3位的，靠前补零。X为十六进制数，Y、Z为十进制数。如：GlobaleNodeB-ID为46000112345，则eNB-FQDN格式为：enb12345.enb.epc.mnc001.mcc460.3gppnetwork.org
IP1|子网地址1|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN1|掩码长度1|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI1|优先级1|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP2|子网地址2|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN2|掩码长度2|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI2|优先级2|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP3|子网地址3|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN3|掩码长度3|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI3|优先级3|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP4|子网地址4|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN4|掩码长度4|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI4|优先级4|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP5|子网地址5|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN5|掩码长度5|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI5|优先级5|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP6|子网地址6|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN6|掩码长度6|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI6|优先级6|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP7|子网地址7|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN7|掩码长度7|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI7|优先级7|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP8|子网地址8|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN8|掩码长度8|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI8|优先级8|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP9|子网地址9|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN9|掩码长度9|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI9|优先级9|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
IP10|子网地址10|参数可选性:任选参数；参数类型:字符型。|IPv4或者IPv6网络地址，比如10.24.0.0。
MASKLEN10|掩码长度10|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
PRI10|优先级10|参数可选性:任选参数；参数类型:整数。|IPv4或者IPv6网络地址中IP地址优先级。当EPC地址解析配置中，配置了多个IP地址时，MME/SGSN根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
命令举例 
查询EPC地址解析优选子网配置。 
SHOW HOST SUBNET PRI; 
`
命令 (No.1): SHOW HOST SUBNET PRI;
操作维护         逻辑名称                                                 子网地址1    掩码长度1   优先级1   子网地址2   掩码长度2   优先级2   子网地址3   掩码长度3   优先级3   子网地址4   掩码长度4   优先级4   子网地址5   掩码长度5   优先级5   子网地址6   掩码长度6   优先级6   子网地址7   掩码长度7   优先级7   子网地址8   掩码长度8   优先级8   子网地址9   掩码长度9   优先级9   子网地址10   掩码长度10   优先级10
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.org   45.1.234.4   22          2         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0     0           0         0.0.0.0      0            0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.053 秒）。
` 
父主题： [EPC地址解析优选子网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# PGW解析配置 
# PGW解析配置 
背景知识 
用户发起附着或PDN连接建立请求，MME/S4 SGSN收到请求后，先从HSS获取用户签约信息，然后MME/S4 SGSN进行PGW选择，MME/S4 SGSN根据FQDN解析到PGW列表和地址，根据选择策略确定一个PGW和其地址，最终MME/S4 SGSN通过选定的PGW地址与PGW进行业务交互。 
术语： 
FQDN：完全合格域名/全称域名(Fully Qualified Domain Name)。 
功能描述 
用户发起附着或PDN连接建立请求，MME/S4 SGSN收到后从HSS获取用户签约信息，如果HSS返回静态PGW ID（FQDN形式），则在MME/S4 SGSN选择PGW时使用该PGW ID；如果HSS返回动态PGW ID（FQDN形式），且签约数据指示允许用户切换到非3GPP网络，则在附着请求带切换指示的业务流程执行中，MME/S4 SGSN选择PGW时使用该PGW ID。 
MME/S4 SGSN使用HSS返回的PGW ID（FQDN形式）作为域名，本地配置对应的PGW地址、服务类别和协议类型。 
配置PGW解析功能的流程如下： 
                        PGW HOST配置，配置命令为：
                        [ADD EPC PGW]
                        。
                    
                        PGW HOST IP地址配置，是对已配置的PGW的IP地址进行增加或删除，配置命令为：
                        [ADD EPC PGW IPADDR]
                        或
                        [DEL EPC PGW IPADDR]
                        。
                    
相关主题 
 
新增PGW HOST配置(ADD EPC PGW)
 
 
修改PGW HOST配置(SET EPC PGW)
 
 
删除PGW HOST配置(DEL EPC PGW)
 
 
增加PGW HOST IP地址(ADD EPC PGW IPADDR)
 
 
删除PGW HOST IP地址(DEL EPC PGW IPADDR)
 
 
查询PGW HOST配置(SHOW EPC PGW)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增PGW HOST配置(ADD EPC PGW) 
## 新增PGW HOST配置(ADD EPC PGW) 
命令功能 
该命令用于对签约数据中的PGW ID（[ADD EPC PGW]命令中填写的PGW名称）进行解析。当MME/S4 SGSN需要对签约数据中的PGW ID进行解析时，使用该命令。该命令执行成功后，当用户进行附着时，MME/S4 SGSN根据用户IMSI到HSS上查找到该用户当前使用的APN未有签约的PGW IP地址，则MME/S4 SGSN根据PGW名称解析出PGW的IP地址。
注意事项 
 
如果用户的在HSS上同时签约了PGW地址和PGW ID，则MME/S4 SGSN优先选择签约的PGW地址。
 
 
运营商可以选择优先在本地进行地址解析，还是优先通过DNS服务器进行地址解析。当软件参数SET SOFTWARE PARAMETER中“软件参数ID”65539的“软件参数值”为0或1时，优先进行本地解析IP地址，本地解析成功后，将不再向DNS服务器发送解析地址请求。当软件参数SET SOFTWARE PARAMETER中“软件参数ID”65539的“软件参数值”为2或3时，优先向DNS服务器请求地址解析，DNS服务器解析成功后，将不再进行本地地址解析，如果DNS服务器故障或者没有配置该域名对应的解析地址，则会继续在本地解析地址。
 
 
如果配置了多个IP地址，且分属不同的子网段，则可以配置不同子网段具有不同的优先级，MME/S4 SGSN进行本地解析时，将会选择属于优先级最高子网段的IP地址。配置子网优先级命令为ADD HOST SUBNET PRI。
 
 
如果最高优先级的子网段中有多个IP地址，则MME/S4 SGSN轮流选择这些IP地址作为目标地址。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|固定格式为“YYYY.pgw.node.epc.mncZZZ.mccWWW.3gppnetwork.org ”，其中YYYY为用户签约的PGW ID。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。Y为字符串，Z、W为十进制数。如：PGW ID 为pc1.autopgw1、MNC为04、MCC460时，格式为：pc1.autopgw1.pgw.node.epc.mnc004.mcc460.3gppnetwork.org。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|配置PGW ID的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址，可配置小于等于64的任意个IP地址。
SERVICE|支持服务类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下网元类型。x-3gpp-pgw：目标局类型为PGWx-3gpp-ggsn：目标局类型为GGSN
PROTOCOL|支持协议类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-gn: 支持GTP协议的Gn接口x-gp: 支持GTP协议的Gp接口x-s5-gtp+nc-nr：支持GTP协议网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议网络能力nr的S8接口。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NORMAL。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网PGW的选择。定义参见3GPP 29.272第7.3.202节。
命令举例 
新增PGW HOST配置，PGW名称为gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org、IP地址为3.0.0.0和5.0.0.0、支持服务类别为x-3gpp-pgw、支持协议类型为x-s5-gtp。 
ADD EPC PGW:PGWNAME="gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org",IPADDR="3.0.0.0"&"5.0.0.0",SERVICE="x-3gpp-pgw",PROTOCOL="x-s5-gtp"; 
父主题： [PGW解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改PGW HOST配置(SET EPC PGW) 
## 修改PGW HOST配置(SET EPC PGW) 
命令功能 
该命令用于修改已经配置的PGW HOST解析的信息，可以修改IP地址、支持服务类别、支持协议类型。当PGW或GGSN网元的信息发生改变时需要使用该命令。该命令配置成功后，MME/S4 SGSN可以根据PGW的名称在本地解析出PGW IP地址。
注意事项 
 
如果修改后的地址是多个IP地址且分属不同的子网段，则可以配置不同子网段具有不同的优先级，MME/S4 SGSN进行本地解析时，将会选择属于优先级最高子网段的IP地址。配置子网优先级命令为ADD HOST SUBNET PRI。
 
 
如果最高优先级的子网段中有多个IP地址，则MME/S4 SGSN轮流选择这些IP地址作为目标地址。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|固定格式为“YYYY.pgw.node.epc.mncZZZ.mccWWW.3gppnetwork.org ”，其中YYYY为用户签约的PGW ID。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。Y为字符串，Z、W为十进制数。如：PGW ID 为pc1.autopgw1、MNC为04、MCC460时，格式为：pc1.autopgw1.pgw.node.epc.mnc004.mcc460.3gppnetwork.org。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|配置PGW ID的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持64个地址，可配置小于等于64的任意个IP地址。
SERVICE|支持服务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下网元类型。x-3gpp-pgw：目标局类型为PGWx-3gpp-ggsn：目标局类型为GGSN
PROTOCOL|支持协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-gn: 支持GTP协议的Gn接口x-gp: 支持GTP协议的Gp接口x-s5-gtp+nc-nr：支持GTP协议网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议网络能力nr的S8接口。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网PGW的选择。定义参见3GPP 29.272第7.3.202节。
命令举例 
修改PGW HOST配置，PGW名称为gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org的PGW HOST配置、IP地址修改为4.0.0.0。 
SET EPC PGW:PGWNAME="gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org",IPADDR="4.0.0.0"; 
父主题： [PGW解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除PGW HOST配置(DEL EPC PGW) 
## 删除PGW HOST配置(DEL EPC PGW) 
命令功能 
该命令用于删除PGW HOST配置。当需要删除PGW HOST配置时，使用该命令。使用该命令成功后，指定PGW名称的PGW HOST配置被删除。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|固定格式为“YYYY.pgw.node.epc.mncZZZ.mccWWW.3gppnetwork.org ”，其中YYYY为用户签约的PGW ID。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。Y为字符串，Z、W为十进制数。如：PGW ID 为pc1.autopgw1、MNC为04、MCC460时，格式为：pc1.autopgw1.pgw.node.epc.mnc004.mcc460.3gppnetwork.org。
命令举例 
删除PGW名称为gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org的PGW HOST配置。 
DEL EPC PGW:PGWNAME="gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org"; 
父主题： [PGW解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 增加PGW HOST IP地址(ADD EPC PGW IPADDR) 
## 增加PGW HOST IP地址(ADD EPC PGW IPADDR) 
命令功能 
该命令用于增加PGW HOST IP地址。当需要在EPC PGW解析信息中增加解析的地址时，使用该命令。使用该命令成功后，会为指定名称的PGW增加一个或多个IP地址。
注意事项 
 
如果配置了多个IP地址，且分属不同的子网段，则可以配置不同子网段具有不同的优先级，MME/S4 SGSN进行本地解析时，将会选择属于优先级最高子网段的IP地址。配置子网优先级命令为ADD HOST SUBNET PRI。
 
 
如果最高优先级的子网段中有多个IP地址，则MME/S4 SGSN轮流选择这些IP地址作为目标地址。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|固定格式为“YYYY.pgw.node.epc.mncZZZ.mccWWW.3gppnetwork.org ”，其中YYYY为用户签约的PGW ID。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。Y为字符串，Z、W为十进制数。如：PGW ID 为pc1.autopgw1、MNC为04、MCC460时，格式为：pc1.autopgw1.pgw.node.epc.mnc004.mcc460.3gppnetwork.org。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|配置PGW ID的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持10个地址，可配置小于等于10的任意个IP地址。
命令举例 
增加PGW HOST地址，PGW名称为gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org、IP地址为65.0.0.0和78.89.0.0。 
ADD EPC PGW IPADDR:PGWNAME="gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org",IPADDR="65.0.0.0"&"78.89.0.0"; 
父主题： [PGW解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除PGW HOST IP地址(DEL EPC PGW IPADDR) 
## 删除PGW HOST IP地址(DEL EPC PGW IPADDR) 
命令功能 
该命令用于删除PGW HOST IP地址。当需要对PGW HOST IP地址进行删除时，使用该命令。该命令成功后，指定名称的PGW HOST记录中一个或多个IP的地址被删除。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|固定格式为“YYYY.pgw.node.epc.mncZZZ.mccWWW.3gppnetwork.org ”，其中YYYY为用户签约的PGW ID。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。Y为字符串，Z、W为十进制数。如：PGW ID 为pc1.autopgw1、MNC为04、MCC460时，格式为：pc1.autopgw1.pgw.node.epc.mnc004.mcc460.3gppnetwork.org。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|配置PGW ID的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持10个地址，可配置小于等于10的任意个IP地址。
命令举例 
删除PGW名称为gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org、IP地址为65.0.0.0的PGW HOST配置。 
DEL EPC PGW IPADDR:PGWNAME="gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org",IPADDR="65.0.0.0"; 
父主题： [PGW解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询PGW HOST配置(SHOW EPC PGW) 
## 查询PGW HOST配置(SHOW EPC PGW) 
命令功能 
该命令用于查询PGW HOST配置。当需要查询PGW HOST的配置信息时，使用该命令。使用该命令成功后，可以得到PGW HOST的配置信息。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
PGWNAME|PGW名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|固定格式为“YYYY.pgw.node.epc.mncZZZ.mccWWW.3gppnetwork.org ”，其中YYYY为用户签约的PGW ID。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。Y为字符串，Z、W为十进制数。如：PGW ID 为pc1.autopgw1、MNC为04、MCC460时，格式为：pc1.autopgw1.pgw.node.epc.mnc004.mcc460.3gppnetwork.org。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PGWID|PGW标识|参数可选性:任选参数；参数类型:整数。|网管自动生成的记录号。
PGWNAME|PGW名称|参数可选性:任选参数；参数类型:字符型。|固定格式为“YYYY.pgw.node.epc.mncZZZ.mccWWW.3gppnetwork.org ”，其中YYYY为用户签约的PGW ID。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。Y为字符串，Z、W为十进制数。如：PGW ID 为pc1.autopgw1、MNC为04、MCC460时，格式为：pc1.autopgw1.pgw.node.epc.mnc004.mcc460.3gppnetwork.org。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|被查询PGW的IP地址，可以是IPv4地址，也可以是IPv6地址。
SERVICE|支持服务类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局类型，目前支持如下网元类型。x-3gpp-pgw：目标局类型为PGWx-3gpp-ggsn：目标局类型为GGSN
PROTOCOL|支持协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-gn: 支持GTP协议的Gn接口x-gp: 支持GTP协议的Gp接口x-s5-gtp+nc-nr：支持GTP协议网络能力nr的S5接口。x-s5-pmip+nc-nr：支持PMIP协议网络能力nr的S5接口。x-s8-gtp+nc-nr：支持GTP协议网络能力nr的S8接口。x-s8-pmip+nc-nr：支持PMIP协议网络能力nr的S8接口。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:字符型。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于专网PGW的选择。定义参见3GPP 29.272第7.3.202节。
命令举例 
查询已配置的PGW HOST。 
SHOW EPC PGW; 
`
2017-02-20 13:43:48 命令 (No.1): SHOW EPC PGW
操作维护         PGW标识   PGW名称                                          IP地址    支持服务类别   支持协议类型   用户使用类型
--------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1         gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org   3.0.0.0   x-3gpp-pgw     x-s5-gtp       普通用户
复制 修改 删除   1         gw1.pgw.node.epc.mnc001.mcc460.3gppnetwork.org   5.0.0.0   x-3gpp-pgw     x-s5-gtp       普通用户
--------------------------------------------------------------------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.096 秒）。
` 
父主题： [PGW解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MMEGI解析配置 
# MMEGI解析配置 
背景知识 
            
            专网用户需要接入专网MME，当专网功能DECOR（Dedicated Core Network）启用时，eNodeB先将用户接入公网MME，公网MME获取专网MME Group ID，携带专网MME Group ID通知eNodeB改向，eNodeB根据专网MME Group ID改向到专网MME。
        
功能描述 
            
            为了获得标识服务于特定UE usage type的专网MME Group ID，使用TAI FQDN和UE usage type本地查询专网MME Group ID。
        
相关主题 
 
新增MMEGI解析配置(ADD MMEGI RESOLVE)
 
 
修改MMEGI解析配置(SET MMEGI RESOLVE)
 
 
删除MMEGI解析配置(DEL MMEGI RESOLVE)
 
 
查询MMEGI解析配置(SHOW MMEGI RESOLVE)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增MMEGI解析配置(ADD MMEGI RESOLVE) 
## 新增MMEGI解析配置(ADD MMEGI RESOLVE) 
命令功能 
该命令用于根据TAI FQDN和用户使用类型配置专网MME Group ID，当需要部署DCN专网且DNS上未配置时，使用该命令。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
LGCNAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置TAI逻辑名称。TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org.
UEUSAGETYPE|用户使用类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。定义参见3GPP 29.272第7.3.202节。
MMEGI|MME Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置专网MME Group ID。
命令举例 
新增MMEGI解析配置。 
ADD MMEGI RESOLVE:LGCNAME="tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org",UEUSAGETYPE="DCN1",MMEGI=1; 
父主题： [MMEGI解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改MMEGI解析配置(SET MMEGI RESOLVE) 
## 修改MMEGI解析配置(SET MMEGI RESOLVE) 
命令功能 
该命令用于修改MMEGI解析配置，修改TAI FQDN、用户使用类型所对应的专网MME Group ID。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
LGCNAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置TAI逻辑名称。TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org.
UEUSAGETYPE|用户使用类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。定义参见3GPP 29.272第7.3.202节。
MMEGI|MME Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置专网MME Group ID。
命令举例 
修改MMEGI解析配置。 
SET MMEGI RESOLVE:LGCNAME="tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org",UEUSAGETYPE="DCN1",MMEGI=1; 
父主题： [MMEGI解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除MMEGI解析配置(DEL MMEGI RESOLVE) 
## 删除MMEGI解析配置(DEL MMEGI RESOLVE) 
命令功能 
该命令用于删除MMEGI解析配置，删除指定TAI FQDN所对应的专网MME Group ID。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
LGCNAME|逻辑名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置TAI逻辑名称。TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org.
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。定义参见3GPP 29.272第7.3.202节。
命令举例 
删除MMEGI解析配置。 
DEL MMEGI RESOLVE:LGCNAME="tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org"; 
父主题： [MMEGI解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MMEGI解析配置(SHOW MMEGI RESOLVE) 
## 查询MMEGI解析配置(SHOW MMEGI RESOLVE) 
命令功能 
该命令用于查询MMEGI解析配置，查询TAI FQDN、用户使用类型和专网MME Group ID的对应关系。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
LGCNAME|逻辑名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|该参数用于设置TAI逻辑名称。TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org.
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。定义参见3GPP 29.272第7.3.202节。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LGCNAME|逻辑名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置TAI逻辑名称。TA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”，其中WW为2位数值表示的TAC的低字节，不足2位的，靠前补零；XX为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数，Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org.
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:字符型。|该参数用于设置用户使用类型（例如：物联网用户、企业用户等，具体数值含义由运营商规划），UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。定义参见3GPP 29.272第7.3.202节。
MMEGI|MME Group ID|参数可选性:任选参数；参数类型:整数。|该参数用于设置专网MME Group ID。
命令举例 
查询MMEGI解析配置。 
SHOW MMEGI RESOLVE; 
`
2017-02-06 09:11:55 命令 (No.1): SHOW MMEGI RESOLVE
操作维护         逻辑名称                                                  用户使用类型        MME Group ID
-----------------------------------------------------------------------------------------------------------
复制 修改 删除   tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.org   专网用户使用类型1   1
-----------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.055 秒）。
` 
父主题： [MMEGI解析配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME RFSP策略配置 
# MME RFSP策略配置 
背景知识 
RFSP（RAT/Frequency Selection Priority，接入方式/频率选择优先级）是应用于无线侧的一个策略集合标识，在UE进行附着、业务请求、跟踪区更新等流程时，由MME在Initial Context Setup Request消息中携带使用的RFSP下发给eNodeB，全网规划，在eNodeB侧配置。 
eNodeB通过RFSP配置选择UE无线连接时使用的频率、频段等参数，RFSP取值范围为1-256。 
本功能涉及到以下几种RFSP： 
 
本地RFSP：本地RFSP是指SGSN网元本地配置的RFSP。
 
 
签约RFSP：是指HSS中关于UE的RFSP签约信息。在用户附着网络后，HSS就把UE的签约RFSP信息通过插入签约数据流程下发给MME。
 
 
使用的RFSP：是指MME根据本地的RFSP策略配置数据，比较本地RFSP和签约RFSP，从中选择一个做为下发给eNodeB的RFSP。
 
 
在下述场景下，可以使用RFSP策略： 
 
对不同用户，使用不同的频率频段，比如对漫游用户，使用FDD（Frequency Division Duplex，频分双工）频段，对其他用户，使用TDD（Time Division Duplex，时分双工）频段。
 
 
根据为UE提供语音业务的方式不同，使用不同的频率频段，比如对仅仅通过IMS VoPS方式提供语音的用户，优先接入LTE频段，对通过CSFB方式提供语音的用户，优先接入3G频段。
 
 
功能描述 
                MME首先根据两种情况匹配通过
                [ADD IMSI RFSP]
                命令配置的RFSP获取策略：
            
 
根据IMSI。
 
 
根据IMSI、UE's usage setting（UE使用设置）和Voice domain preference for E-UTRAN（E-UTRAN下语音域优先级）三个条件：
 
 
"UE's usage setting"和"Voice domain preference for E-UTRAN"是UE在Attach Request和TAU Request消息中携带发送给MME的。 
UE's usage setting，有下面两种方式： 
 
"Voice centric"：UE的现有状态必须能提供语音业务，如果不能提供语音业务，UE会重新选择新的RAT接入移动网络。
 
 
"Data centric"：UE的现有状态必须能提供数据业务，如果不能提供数据业务，UE会重新选择新的RAT接入移动网络。
 
 
Voice domain preference for E-UTRAN，有下面四种方式： 
 
CS Voice only：仅能通过CSFB方式提供语音业务，不能通过IMS VoPS方式提供语音业务。
 
 
IMS PS Voice only：仅能通过IMS VoPS方式提供语音业务，不能通过CSFB方式通过语音业务。
 
 
CS Voice preferred, IMS PS Voice as secondary：优先通过CSFB方式提供语音业务，在CSFB方式不能提供语音业务时，使用IMS VoPS方式提供语音业务。
 
 
IMS PS Voice preferred, CS Voice as secondary：优先通过IMS VoPS方式提供语音业务，在IMS VoPS方式不能提供语音业务时，使用CSFB方式提供语音业务。
 
 
                通过
                [ADD IMSI RFSP]
                命令配置的RFSP获取策略分为以下三种：
            
 
策略控制为“本地配置优先”，则MME使用本地配置的RFSP，发送给eNodeB。
 
 
策略控制为“签约优先”，则MME使用HSS下发的签约RFSP，发送给eNodeB。
 
 
策略控制为“签约与本地配置取小”，则MME使用本地配置的RFSP和HSS下发的签约RFSP中的较小值，发送给eNodeB。
 
 
                如果MME根据IMSI或根据IMSI、UE's usage setting（UE使用设置）和Voice domain preference for E-UTRAN（E-UTRAN下语音域优先级）不能匹配到对应的RFSP获取策略，则使用
                [SET DEFAULT RFSP]
                命令配置的缺省RFSP策略控制。
            
                通过
                [SET DEFAULT RFSP]
                命令配置的RFSP获取策略分为以下三种：
            
 
策略控制为“本地配置优先”，则MME使用本地配置的RFSP，发送给eNodeB。
 
 
策略控制为“签约优先”，则MME使用HSS下发的签约RFSP，发送给eNodeB。
 
 
策略控制为“签约与本地配置取小”，则MME使用本地配置的RFSP和HSS下发的签约RFSP中的较小值，发送给eNodeB。
 
 
说明： 
MME是否投递使用的RFSP给eNodeB，可以通过RFSP配置策略控制，如果MME获取的使用RFSP值为0，则表示不投递使用的RFSP给eNodeB。 
默认配置中MME不携带使用RFSP给eNodeB。 
相关主题 
 
设置MME缺省RFSP配置(SET DEFAULT RFSP)
 
 
查询MME缺省RFSP配置(SHOW DEFAULT RFSP)
 
 
新增基于IMSI的RFSP配置(ADD IMSI RFSP)
 
 
修改基于IMSI的RFSP配置(SET IMSI RFSP)
 
 
删除基于IMSI的RFSP配置(DEL IMSI RFSP)
 
 
查询基于IMSI的RFSP配置(SHOW IMSI RFSP)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置缺省RFSP配置(SET DEFAULT RFSP) 
## 设置缺省RFSP配置(SET DEFAULT RFSP) 
命令功能 
该命令用于设置缺省RFSP配置。当需要使用RFSP标识支持无线策略时，需要在MME中配置RFSP策略。 
注意事项 
选择使用“签约信息优先”或者“签约与本地配置取小”策略时，需要在HSS的用户签约信息中配置用户的RFSP参数。 
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICY|策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|RFSP使用策略。取值含义：LOCAL：本地配置优先，使用MME配置的本地RFSP索引值。SUBSCRIPT：签约信息优先，使用从HSS获取的用户签约信息中的RFSP索引值。SMALLER：使用本地配置及签约信息RFSP索引值中较小的RFSP索引值。
RFSP|RFSP索引值|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|RFSP索引值，由无线定义各RFSP索引值映射使用策略。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
设置缺省RFSP，策略控制为本地配置优先，RFSP索引值为0。 
SET DEFAULT RFSP:POLICY="LOCAL",RFSP=0; 
父主题： [MME RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询缺省RFSP配置(SHOW DEFAULT RFSP) 
## 查询缺省RFSP配置(SHOW DEFAULT RFSP) 
命令功能 
该命令用于查询缺省RFSP配置。无查询条件。显示缺省RFSP值。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
POLICY|策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|RFSP使用策略。取值含义：LOCAL：本地配置优先，使用MME配置的本地RFSP索引值。SUBSCRIPT：签约信息优先，使用从HSS获取的用户签约信息中的RFSP索引值。SMALLER：使用本地配置及签约信息RFSP索引值中较小的RFSP索引值。
RFSP|RFSP索引值|参数可选性:任选参数；参数类型:整数。|RFSP索引值，由无线定义各RFSP索引值映射使用策略。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询缺省RFSP配置。 
SHOW DEFAULT RFSP; 
`命令 (No.5): SHOW DEFAULT RFSP
操作维护   策略控制            RFSP索引值   用户别名
----------------------------------------------------
修改      本地配置优先         0            
----------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。` 
父主题： [MME RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增基于IMSI的RFSP配置(ADD IMSI RFSP) 
## 新增基于IMSI的RFSP配置(ADD IMSI RFSP) 
命令功能 
该命令用于新增基于IMSI或IMSI、UE使用设定、E-UTRAN语音优先策略的RFSP配置。当IMSI或IMSI、UE使用设定、E-UTRAN语音优先策略使用的RFSP策略不同于缺省RFSP策略时，根据IMSI或IMSI、UE使用设定、E-UTRAN语音优先策略选择不同的RFSP，则需要增加该IMSI的专有RFSP策略。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
USAGESET|UE使用设置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置。取值含义：VOICE：以语音业务为中心，UE主要并且优先用于语音通话，如手机。DATA：以数据业务为中心，UE主要并且优先用于数据传输，如上网数据卡。N/A：任意设定。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|E-UTRAN语音优先策略。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。N/A：任意设定。
POLICY|策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:LOCAL。|RFSP使用策略。取值含义：LOCAL：本地配置优先，使用MME配置的本地RFSP索引值。SUBSCRIPT：签约信息优先，使用从HSS获取的用户签约信息中的RFSP索引值。SMALLER：使用本地配置及签约信息RFSP索引值中较小的RFSP索引值。
RFSP|RFSP索引值|参数可选性:必选参数；参数类型:整数；参数范围为:0~256。|RFSP索引值，由无线定义各RFSP索引值映射使用策略。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
新增基于IMSI的RFSP配置，IMSI号段为46001，UE使用设置为语音中心，E-UTRAN语音优先策略为仅CS语音，策略控制为本地配置优先，RFSP索引值为1。 
ADD IMSI RFSP:IMSI="46001",USAGESET="VOICE",VOICEPREFER="CSVOICE",RFSP=1; 
父主题： [MME RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改基于IMSI的RFSP配置(SET IMSI RFSP) 
## 修改基于IMSI的RFSP配置(SET IMSI RFSP) 
命令功能 
该命令用于修改该IMSI的RFSP值。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
USAGESET|UE使用设置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置。取值含义：VOICE：以语音业务为中心，UE主要并且优先用于语音通话，如手机。DATA：以数据业务为中心，UE主要并且优先用于数据传输，如上网数据卡。N/A：任意设定。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|E-UTRAN语音优先策略。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。N/A：任意设定。
POLICY|策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|RFSP使用策略。取值含义：LOCAL：本地配置优先，使用MME配置的本地RFSP索引值。SUBSCRIPT：签约信息优先，使用从HSS获取的用户签约信息中的RFSP索引值。SMALLER：使用本地配置及签约信息RFSP索引值中较小的RFSP索引值。
RFSP|RFSP索引值|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|RFSP索引值，由无线定义各RFSP索引值映射使用策略。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
修改IMSI号段为46001，UE使用设置为语音中心，E-UTRAN语音优先策略为仅CS语音的RFSP配置，将RFSP索引值改为0。 
SET IMSI RFSP:IMSI="46001",USAGESET="VOICE",VOICEPREFER="CSVOICE",RFSP=0; 
父主题： [MME RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除基于IMSI的RFSP配置(DEL IMSI RFSP) 
## 删除基于IMSI的RFSP配置(DEL IMSI RFSP) 
命令功能 
该命令用于删除基于IMSI的RFSP配置。删除该IMSI的RFSP配置后，使用缺省RFSP策略。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
USAGESET|UE使用设置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置。取值含义：VOICE：以语音业务为中心，UE主要并且优先用于语音通话，如手机。DATA：以数据业务为中心，UE主要并且优先用于数据传输，如上网数据卡。N/A：任意设定。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|E-UTRAN语音优先策略。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。N/A：任意设定。
命令举例 
删除IMSI号段为46001，UE使用设置为语音中心，E-UTRAN语音优先策略为仅CS语音的RFSP配置。 
DEL IMSI RFSP:IMSI="46001",USAGESET="VOICE",VOICEPREFER="CSVOICE"; 
父主题： [MME RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询基于IMSI的RFSP配置(SHOW IMSI RFSP) 
## 查询基于IMSI的RFSP配置(SHOW IMSI RFSP) 
命令功能 
该命令用于查询基于IMSI的RFSP配置。可以使用IMSI来查询其RFSP值，或者不带参数查询所有IMSI的RFSP值。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
USAGESET|UE使用设置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置。取值含义：VOICE：以语音业务为中心，UE主要并且优先用于语音通话，如手机。DATA：以数据业务为中心，UE主要并且优先用于数据传输，如上网数据卡。N/A：任意设定。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|E-UTRAN语音优先策略。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。N/A：任意设定。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|该参数用于设置IMSI号段。
USAGESET|UE使用设置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置。取值含义：VOICE：以语音业务为中心，UE主要并且优先用于语音通话，如手机。DATA：以数据业务为中心，UE主要并且优先用于数据传输，如上网数据卡。N/A：任意设定。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|E-UTRAN语音优先策略。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。N/A：任意设定。
POLICY|策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|RFSP使用策略。取值含义：LOCAL：本地配置优先，使用MME配置的本地RFSP索引值。SUBSCRIPT：签约信息优先，使用从HSS获取的用户签约信息中的RFSP索引值。SMALLER：使用本地配置及签约信息RFSP索引值中较小的RFSP索引值。
RFSP|RFSP索引值|参数可选性:任选参数；参数类型:整数。|RFSP索引值，由无线定义各RFSP索引值映射使用策略。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询IMSI号段为46001的RFSP配置。 
SHOW IMSI RFSP:IMSI="46001"; 
`
命令 (No.3): SHOW IMSI RFSP:IMSI="46001";
操作维护         IMSI     UE使用设置   E-UTRAN语音优先策略    策略控制            RFSP索引值   用户别名
-------------------------------------------------------------------------------------------------------
复制 修改 删除   46001    语音中心     仅CS语音              本地配置优先         1            
-------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [MME RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN RFSP策略配置 
# SGSN RFSP策略配置 
背景知识 
RFSP（RAT/Frequency Selection Priority，接入方式/频率选择优先级）是应用于无线侧的一个策略集合标识。在UE进行附着、业务请求、路由区更新等流程时，由SGSN在Common ID、DIRECT TRANSFER、DL-UNITDATA、CREATE-BSS-PFC消息中携带使用的RFSP下发给RNC/BSC。该功能需要全网规划，在RNC和BSC侧配置。 
RNC/BSC通过RFSP配置选择UE无线连接时使用的频率、频段等参数，RFSP取值范围为1-256。 
本功能涉及到以下几种RFSP： 
 
本地RFSP：本地RFSP是指SGSN网元本地配置的RFSP。
 
 
使用的RFSP：是指SGSN根据本地的RFSP策略配置数据，确定最终下发给RNC/BSC的RFSP。
 
 
在下述场景下，可以使用RFSP策略： 
对不同用户，使用不同的频率频段，比如对漫游用户，使用FDD（Frequency Division Duplex，频分双工）频段，对其他用户，使用TDD（Time Division Duplex，时分双工）频段。 
功能描述 
SGSN通过ADD SGSN IMSI RFSP命令配置SGSN RFSP策略。 
如果SGSN根据根据IMSI不能匹配到对应的RFSP获取策略，则使用SET SGSN DEFAULT RFSP命令配置的缺省RFSP策略控制。 
说明：SGSN是否投递使用的RFSP给RNC/BSC，可以通过RFSP配置策略控制，如果SGSN获取的使用RFSP值为0，则表示不投递使用的RFSP给RNC/BSC。 
默认配置中SGSN不携带使用RFSP给RNC/BSC。 
相关主题 
 
设置SGSN默认RFSP策略(SET RFSP DEFPOLICY)
 
 
查询SGSN默认RFSP策略(SHOW RFSP DEFPOLICY)
 
 
新增SGSN基于IMSI号段的RFSP策略(ADD RFSP POLICY)
 
 
修改SGSN基于IMSI号段的RFSP策略(SET RFSP POLICY)
 
 
删除SGSN基于IMSI号段的RFSP策略(DEL RFSP POLICY)
 
 
查询SGSN基于IMSI号段的RFSP策略(SHOW RFSP POLICY)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置SGSN默认RFSP策略(SET RFSP DEFPOLICY) 
## 设置SGSN默认RFSP策略(SET RFSP DEFPOLICY) 
命令功能 
该命令用于设置SGSN 默认RFSP策略。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
LOCALRFSP|本地RFSP值|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|该参数用于设置本地RFSP值。
命令举例 
设置SGSN默认RFSP策略的本地RFSP值为1。 
SET RFSP DEFPOLICY:LOCALRFSP=1; 
父主题： [SGSN RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN默认RFSP策略(SHOW RFSP DEFPOLICY) 
## 查询SGSN默认RFSP策略(SHOW RFSP DEFPOLICY) 
命令功能 
该命令用于查询SGSN 默认RFSP策略。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LOCALRFSP|本地RFSP值|参数可选性:任选参数；参数类型:整数。|该参数用于设置本地RFSP值。
命令举例 
查询SGSN默认RFSP策略。 
SHOW RFSP DEFPOLICY; 
`命令 (No.11): SHOW RFSP DEFPOLICY
操作维护  本地RFSP值 
--------------------
修改      1 
--------------------
记录数 1
命令执行成功（耗时 0.057 秒）。` 
父主题： [SGSN RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增SGSN基于IMSI号段的RFSP策略(ADD RFSP POLICY) 
## 新增SGSN基于IMSI号段的RFSP策略(ADD RFSP POLICY) 
命令功能 
该命令用于新增SGSN基于IMSI号段的RFSP策略。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指示用户IMSI标识段。
LOCALRFSP|本地RFSP值|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。默认值:0。|该参数用于设置本地RFSP值。
ALIAS|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于描述别名。
命令举例 
新增SGSN基于IMSI号段为123的RFSP策略。 
ADD RFSP POLICY:IMSISEG="123"; 
父主题： [SGSN RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改SGSN基于IMSI号段的RFSP策略(SET RFSP POLICY) 
## 修改SGSN基于IMSI号段的RFSP策略(SET RFSP POLICY) 
命令功能 
该命令用于修改SGSN基于IMSI号段的RFSP策略。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指示用户IMSI标识段。
LOCALRFSP|本地RFSP值|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|该参数用于设置本地RFSP值。
ALIAS|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于描述别名。
命令举例 
修改SGSN基于IMSI号段为123, 本地RFSP值为1的RFSP策略。 
SET RFSP POLICY:IMSISEG="123",LOCALRFSP=1; 
父主题： [SGSN RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除SGSN基于IMSI号段的RFSP策略(DEL RFSP POLICY) 
## 删除SGSN基于IMSI号段的RFSP策略(DEL RFSP POLICY) 
命令功能 
该命令用于删除SGSN基于IMSI号段的RFSP策略。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指示用户IMSI标识段。
命令举例 
删除SGSN基于IMSI号段为123的RFSP策略。 
DEL RFSP POLICY:IMSISEG="123"; 
父主题： [SGSN RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN基于IMSI号段的RFSP策略(SHOW RFSP POLICY) 
## 查询SGSN基于IMSI号段的RFSP策略(SHOW RFSP POLICY) 
命令功能 
该命令用于查询SGSN基于IMSI号段的RFSP策略。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指示用户IMSI标识段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型。|该参数用于指示用户IMSI标识段。
LOCALRFSP|本地RFSP值|参数可选性:任选参数；参数类型:整数。|该参数用于设置本地RFSP值。
ALIAS|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数用于描述别名。
命令举例 
查询SGSN基于IMSI号段的RFSP策略。 
SHOW RFSP POLICY; 
`命令 (No.16): SHOW RFSP POLICY
操作维护        IMSI号段 本地RFSP值 用户别名 
------------------------------------------------
复制 修改 删除  123      1     
------------------------------------------------
记录数 1
命令执行成功（耗时 0.041 秒）。` 
父主题： [SGSN RFSP策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME基于IMSI号段IMEI检查配置 
# MME基于IMSI号段IMEI检查配置 
背景知识 
IMEI检查功能是指在UE Attach过程中，MME获取UE的IMEI（International Mobile Equipment Identity，国际移动设备标识）信息，并将其发送给EIR（Equipment Identity Register，设备标识寄存器）进行合法性检查的业务。MME收到EIR返回的检查结果后，根据EIR返回的结果（黑名单、白名单、灰名单）决定是否允许UE接入。 
通过IMEI检查功能，可以确认终端的合法性，从而禁止非法终端进入网络。 
MME网元支持基于用户的IMSI号段对其进行IMEI检查，此功能是对原IMEI检查功能的优化。 
通常情况下，MME会对所有用户进行IMEI检查，配置了“基于IMSI号段的IMEI检查”功能后，MME只需要对某些IMSI号段内的用户进行IMEI检查，这样可以减少MME与EIR之间的消息交互，降低EIR的负荷。 
本配置主要适用于部分运营商为了减少EIR信令负荷，只针对本网用户进行IMEI检查，不对漫游用户进行IMEI检查的场景。 
通常，一次IMEI检查的触发及处理过程如下： 
用户接入MME，MME向UE发送Identity Request消息，请求获取IMEI号码。 
UE向MME发送Identity Response消息，返回IMEI号码。 
MME向EIR发送IMEI Check Request消息，携带该UE的IMEI号码。 
EIR向MME发送IMEI Check Response消息，返回检查结果：黑名单（非法用户）、白名单（合法用户）、灰名单（合法但需关注的用户）。 
对于黑名单用户，MME拒绝接入；对于白名单用户，MME允许接入；对于灰名单用户，MME允许接入，且会通过告警通知（告警码：2114060544）上报该用户的本次接入事件。 
功能描述 
此功能只包含一个配置参数，即IMSI号段。 
配置生效后，MME只针对配置在IMSI号段内的用户，进行IMEI检查，对于不在配置号段内的用户则不进行IMEI检查。 
本功能配置前提条件如下： 
 
                        在移动管理中配置MME是否需要通过Identity Request消息向UE获取IMEI号码，通过
                        SET MOBILE MANAGEMENT
                        命令，将参数“MME获取IMEI(SV)”配置为”获取IMEI”（此参数有四个取值，只要不配置为“NONE”，其它三个取值均可）。
                    
 
 
                        在安全管理中设置MME是否需要进行IMEI检查，通过
                        SET SECURITY PARAMETER
                        命令，将参数“MME IMEI检查控制”配置为“需要“。
                    
 
 
                        配置MME支持s13接口（即MME与EIR之间的接口）：通过
                        SET COMBOCFG
                        命令，将参数“支持类型“设置为”S13“。
                    
 
 
                        通过
                        SHOW DIAMEIR
                        命令查看是否配置了MME到EIR之间的局向信息，如果没有配置的话，需要通过
                        ADD DIAMEIR
                        命令进行配置。
                    
 
 
                        配置软件参数，将MME支持基于IMSI号段进行IMEI检查配置为“支持”，命令为
                        SET SOFTWARE PARAMETER
                        :PARAID=262227,PARAVALUE=1;
                    
 
 
相关主题 
 
新增IMSI号段IMEI检查配置(ADD MME IMEI CHECK)
 
 
删除IMSI号段IMEI检查配置(DEL MME IMEI CHECK)
 
 
查询IMSI号段IMEI检查配置(SHOW MME IMEI CHECK)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增IMSI号段IMEI检查配置(ADD MME IMEI CHECK) 
## 新增IMSI号段IMEI检查配置(ADD MME IMEI CHECK) 
命令功能 
该命令用于MME网元新增基于IMSI号段进行IMEI检查配置。 
当需要对基于IMSI号段控制用户的IMEI检查时，使用该命令。 
该命令执行成功后，MME只对指定IMSI号段的用户向EIR发送ME Identity Check消息，等待EIR的IMEI检查响应确定该用户是否为合法用户、是否允许接入。 
注意事项 
如果需要进行IMEI检查，则需要通过Identity Request消息向UE获取到IMEI；MME侧移动管理中配置是否需要获取IMEI，配置命令为： 
[SET MOBILE MANAGEMENT]:MMEGETIMEI="Get IMEI";
是否进行IMEI检查，还需要进行如下相关配置： 
 
MME侧在安全管理中设置是否需要进行IMEI检查，配置命令为：SET SECURITY PARAMETER:MMECHECKIMEI="Need";
 
 
MME侧支持协议类型增加EIR网元的接口类型（s13口），配置命令为：SET COMBOCFG:SUPTYPE="SMS"&"Gs"&"Gf"&"Gb"&"Iu"&"Egprs"&"S13";
 
 
查看EIR局向配置是否存在，配置命令为：SHOW DIAMEIR
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI为国际移动用户识别码，由0～9的数字组成，总长度不超过15位，结构为MCC+MNC+MSIN。MCC：Mobile Country Code，移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，中国为460。MNC：Mobile Network Code，移动网络码，2~3位。MSIN：Mobile Subscriber Identification Number，移动用户识别号码，共有10位，结构为EF+M0M1M2M3+ABCD。其中的M0M1M2M3和MDN号码中的H0H1H2H3可存在对应关系，ABCD四位为自由分配。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
命令举例 
新增IMSI号段为46001的IMEI检查配置。 
ADD MME IMEI CHECK:IMSI="46001"; 
父主题： [MME基于IMSI号段IMEI检查配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除IMSI号段IMEI检查配置(DEL MME IMEI CHECK) 
## 删除IMSI号段IMEI检查配置(DEL MME IMEI CHECK) 
命令功能 
该命令用于删除基于IMSI号段IMEI检查配置。 
需要根据IMSI号段进行删除，否则命令执行失败并提示“必须输入IMSI号段(IMSI)参数的值”。 
删除指定IMSI号段的IMEI检查配置后，对于不在配置号段内的用户则不进行IMEI检查。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI为国际移动用户识别码，由0～9的数字组成，总长度不超过15位，结构为MCC+MNC+MSIN。MCC：Mobile Country Code，移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，中国为460。MNC：Mobile Network Code，移动网络码，2~3位。MSIN：Mobile Subscriber Identification Number，移动用户识别号码，共有10位，结构为EF+M0M1M2M3+ABCD。其中的M0M1M2M3和MDN号码中的H0H1H2H3可存在对应关系，ABCD四位为自由分配。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
命令举例 
删除IMSI号段为46001的IMEI检查配置。 
DEL MME IMEI CHECK:IMSI="46001"; 
父主题： [MME基于IMSI号段IMEI检查配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询IMSI号段IMEI检查配置(SHOW MME IMEI CHECK) 
## 查询IMSI号段IMEI检查配置(SHOW MME IMEI CHECK) 
命令功能 
该命令用于查询IMSI号段IMEI检查配置。 
查询条件包括： 
 
按指定IMSI号段查询，显示查询到的单条IMEI检查配置记录。
 
 
如果不指定IMSI号段，则显示全部IMEI检查配置记录。
 
 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI为国际移动用户识别码，由0～9的数字组成，总长度不超过15位，结构为MCC+MNC+MSIN。MCC：Mobile Country Code，移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，中国为460。MNC：Mobile Network Code，移动网络码，2~3位。MSIN：Mobile Subscriber Identification Number，移动用户识别号码，共有10位，结构为EF+M0M1M2M3+ABCD。其中的M0M1M2M3和MDN号码中的H0H1H2H3可存在对应关系，ABCD四位为自由分配。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI为国际移动用户识别码，由0～9的数字组成，总长度不超过15位，结构为MCC+MNC+MSIN。MCC：Mobile Country Code，移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，中国为460。MNC：Mobile Network Code，移动网络码，2~3位。MSIN：Mobile Subscriber Identification Number，移动用户识别号码，共有10位，结构为EF+M0M1M2M3+ABCD。其中的M0M1M2M3和MDN号码中的H0H1H2H3可存在对应关系，ABCD四位为自由分配。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
命令举例 
查询IMSI号段为46001的IMEI检查配置。 
SHOW MME IMEI CHECK:IMSI="46001"; 
`
命令 (No.1): SHOW MME IMEI CHECK:IMSI="46001";
操作维护    IMSI号段
--------------------
复制 删除   46001
--------------------
记录数 1
命令执行成功（耗时 0.042 秒）。
` 
父主题： [MME基于IMSI号段IMEI检查配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN基于IMSI号段IMEI检查配置 
# SGSN基于IMSI号段IMEI检查配置 
背景知识 
IMEI检查功能，是指在UE Attach过程中，SGSN获取UE的IMEI（International Mobile Equipment Identity，国际移动设备标识）信息，并将其发送给EIR（Equipment Identity Register，设备标识寄存器）进行合法性检查的业务。SGSN收到EIR返回的检查结果后，根据EIR返回的结果（黑名单、白名单、灰名单）决定是否允许UE接入。 
通过IMEI检查功能，可以确认终端的合法性，从而禁止非法终端进入网络。 
SGSN网元支持基于用户的IMSI号段对其进行IMEI检查，此功能是对原IMEI检查功能的优化。 
通常情况下，SGSN会对所有用户进行IMEI检查，配置了“基于IMSI号段的IMEI检查”功能后，SGSN只需要对某些IMSI号段内的用户进行IMEI检查，这样可以减少SGSN与EIR之间的消息交互，降低EIR的负荷。 
本配置主要适用于部分运营商为了减少EIR信令负荷，只针对本网用户进行IMEI检查，不对漫游用户进行IMEI检查的场景。 
通常，一次IMEI检查的触发及处理过程如下： 
用户接入SGSN，SGSN向UE发送Identity Request消息，请求获取IMEI号码。 
UE向SGSN发送Identity Response消息，返回IMEI号码。 
SGSN向EIR发送IMEI Check Request消息，携带该UE的IMEI号码。 
EIR向SGSN发送IMEI Check Response消息，返回检查结果：黑名单（非法用户）、白名单（合法用户）、灰名单（合法但需关注的用户）。 
对于黑名单用户，SGSN拒绝接入；对于白名单用户，SGSN允许接入；对于灰名单用户，SGSN允许接入，且会通过告警通知（告警码：2114060544）上报该用户的本次接入事件。 
功能描述 
此功能只包含一个配置参数，即IMSI号段。 
配置生效后，SGSN只针对配置在IMSI号段内的用户，进行IMEI检查，对于不在配置号段内的用户则不进行IMEI检查。 
本功能配置前提条件如下： 
 
                        配置软件参数“SGSN 是否获取IMEI(SV)”的值为非0，设置SGSN需要向UE获取IMEI号码，命令为
                        SET SOFTWARE PARAMETER
                        :PARAID=262150,PARAVALUE=1;。此软件参数有四个取值：0-不需要；1-获取IMEI；2-获取IMEISV；3-支持ADD功能。只要不配置为“0”，其它三个取值均可。
                    
 
 
                        配置软件参数“SGSN按流程检查IMEI”的值为非0，命令为
                        SET SOFTWARE PARAMETER
                        :PARAID=327819,PARAVALUE=1;。此软件参数按照流程控制是否检查IMEI，根据实际需要的流程配置不同的值。一共7个取值：0-不检查IMEI；1-附着时检查IMEI；2-局间RAU时检查IMEI；3-附着和局间RAU时检查IMEI；4-局内RAU时检查IMEI；5-附着和局内RAU时检查IMEI；6–RAU时检查IMEI；7-附着和RAU时检查IMEI。
                    
 
 
                        配置SGSN支持Gf接口（即SGSN与EIR之间的接口），通过
                        SET COMBOCFG
                        命令，将参数“支持类型“中的“Gf接口”选上。
                    
 
 
                        通过
                        SHOW EIRNUM
                        命令，查看是否配置了EIR号码，如果没有配置的话，需要通过
                        ADD EIRNUM
                        命令进行配置。
                    
 
 
                        配置软件参数“SGSN是否基于IMSI号段IMEI检查”的值为1（即“支持”），命令为
                        SET SOFTWARE PARAMETER
                        :PARAID=262232,PARAVALUE=1;。
                    
 
 
相关主题 
 
新增SGSN基于IMSI号段IMEI检查配置(ADD SGSN IMEI CHECK)
 
 
删除SGSN基于IMSI号段IMEI检查配置(DEL SGSN IMEI CHECK)
 
 
查询SGSN基于IMSI号段IMEI检查配置(SHOW SGSN IMEI CHECK)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增SGSN基于IMSI号段IMEI检查配置(ADD SGSN IMEI CHECK) 
## 新增SGSN基于IMSI号段IMEI检查配置(ADD SGSN IMEI CHECK) 
命令功能 
该命令用于新增SGSN基于IMSI号段IMEI检查配置。当需要基于IMSI号段控制用户的IMEI检查时，使用该命令。命令执行成功后，可以只针对特定的IMSI号段用户进行IMEI检查。 
IMEI是手机的唯一识别号码，用于识别手机的身份。IMSI是国际移动号码识别，识别当前用户的身份的，存储与SIM卡中，SIM卡可以插在不同的手机终端上。为了检查用户终端的合法性，需要进行IMEI检查。IMEI合法性主要检查用户是否处于黑名单、白名单和灰名单，然后限制用户是否允许接入SGSN。当只需要对特定IMSI号段，即特定号段用户检查手机终端的合法性时，要基于IMSI号段来检查。 
注意事项 
 
该命令最大支持的记录数为1024。
 
 
激活该特性，需要先将软件参数“SGSN是否基于IMSI号段IMEI检查”设置为“支持”，配置命令为：SET SOFTWARE PARAMETER:PARAID=262232,PARAVALUE=1;。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
命令举例 
新增SGSN基于IMSI号段46001的IMEI检查。 
ADD SGSN IMEI CHECK:IMSI="46001"; 
父主题： [SGSN基于IMSI号段IMEI检查配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除SGSN基于IMSI号段IMEI检查配置(DEL SGSN IMEI CHECK) 
## 删除SGSN基于IMSI号段IMEI检查配置(DEL SGSN IMEI CHECK) 
命令功能 
该命令用于删除SGSN基于IMSI号段IMEI检查配置。参数为IMSI号段。当不需要对特定IMSI号段用户进行IMEI检查控制时，使用该命令。开启IMSI号段检查IMEI功能并删除特定的号段后，SGSN对这部分号段的用户不会进行IMEI检查。 
注意事项 
使用前检查待删除的IMSI号段是否正确。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
命令举例 
删除SGSN基于IMSI号段46001的IMEI检查。 
DEL SGSN IMEI CHECK:IMSI="46001"; 
父主题： [SGSN基于IMSI号段IMEI检查配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN基于IMSI号段IMEI检查配置(SHOW SGSN IMEI CHECK) 
## 查询SGSN基于IMSI号段IMEI检查配置(SHOW SGSN IMEI CHECK) 
命令功能 
该命令用于查询SGSN基于IMSI号段IMEI检查配置，可以通过以下方式进行查询。 
 
按指定IMSI号段查询，显示查询到的单条IMEI检查配置记录。
 
 
不指定IMSI号段，显示全部IMEI检查配置记录。
 
 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
命令举例 
查询SGSN基于IMSI号段46001的IMEI检查配置。 
SHOW SGSN IMEI CHECK:IMSI="46001"; 
`
命令 (No.1): SHOW SGSN IMEI CHECK:IMSI="46001";
操作维护 IMSI号段 
--------------------
复制 删除  46001 
--------------------
记录数 1
命令执行成功（耗时 0.063 秒）。
` 
父主题： [SGSN基于IMSI号段IMEI检查配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN ODB配置 
# SGSN ODB配置 
背景知识 
支持ODB功能，运营商能够根据用户签约数据中的ODB参数，限制一些用户的业务和服务。 
功能描述 
通过SGSN ODB配置，可控制SGSN是否支持以下四种ODB业务。 
 
禁止用户出呼，不允许用户发送短信。
 
 
禁止用户进行PS业务。
 
 
禁止漫游用户通过HPLMN的接入点接入本网。（即漫游用户只能通过拜访地的GGSN接入）
 
 
禁止漫游用户通过VPLMN的接入点接入本网。（即漫游用户只能通过归属地的GGSN接入）
 
 
同时在HSS可对用户针对以上业务签约为支持或不支持。 
只有在SGSN与HLR签约同时支持情况下，ODB业务才会生效。 
相关主题 
 
设置SGSN ODB配置(SET SGSN ODB)
 
 
查询SGSN ODB配置(SHOW SGSN ODB)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置SGSN ODB配置(SET SGSN ODB) 
## 设置SGSN ODB配置(SET SGSN ODB) 
命令功能 
该命令用于设置SGSN支持的ODB（Operator Determined Barring，运营商闭锁）功能。 
ODB即运营商的限制，表示运营商能够通过本命令设置ODB参数，用于限制某些用户的业务和服务。 
本功能需要SGSN和HLR配合完成，要求HLR支持ODB签约信息，HLR能够根据签约数据决定是否触发ODB业务，以及向VLR发送用户的签约数据。 
本功能只有在SGSN与HLR签约同时支持情况下，对应的ODB业务才会生效。 
通过本命令，可控制SGSN是否支持以下四种ODB业务。 
禁止用户发送短消息。
 
 
禁止用户使用PS业务。
 
 
禁止漫游用户通过HPLMN的接入点接入本网络（即漫游用户只能通过拜访地的GGSN接入）。
 
 
禁止漫游用户通过VPLMN的接入点接入本网络（即漫游用户只能通过归属地的GGSN接入）。
 
 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
BAOC|所有呼出限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果用户在HLR中的签约ODB数据为限制所有呼出：当此参数配置为“是”时，SGSN限制用户不能发送短消息。当此参数配置为“否”时，SGSN不限制用户发送短消息。
BAOPS|所有PS业务限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果用户在HLR中的签约ODB为限制PS业务：当此参数配置为“否”时，系统允许用户附着到SGSN上使用PS业务。当此参数配置为“支持但允许接入”时，系统允许用户附着到SGSN但不能进行PS业务。当此参数配置为“支持且禁止接入”时，系统不允许用户附着到SGSN。
BOHPAP|VPLMN中禁止访问HPLMN APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果用户在HLR中的签约ODB为VPLMN中禁止访问HPLMN APN：VPLMN指漫游用户的拜访PLMN（即本SGSN网元所在的PLMN），HPLMN指漫游用户归属的PLMN。该参数表示是否禁止漫游用户通过HPLMN的GGSN网元激活。当此参数设置为“支持”时，表示漫游用户不能通过HPLMN中的GGSN激活。当此参数设置为“不支持”时，表示漫游用户可以通过HPLMN中的GGSN激活。
BOVPAP|VPLMN中禁止访问VPLMN APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果用户在HLR中的签约ODB为VPLMN中禁止访问VPLMN APN：VPLMN指漫游用户的拜访PLMN（即本SGSN网元所在的PLMN），HPLMN指漫游用户归属的PLMN。该参数表示是否禁止漫游用户通过VPLMN的GGSN网元激活。当此参数设置为“支持”时，表示漫游用户不能通过VPLMN中的GGSN激活。当此参数设置为“不支持”时，表示漫游用户可以通过VPLMN中的GGSN激活。
命令举例 
设置支持用户签约ODB业务：所有呼出限制，所有PS业务限制，VPLMN中禁止访问HPLMN APN，VPLMN中禁止访问VPLMN APN。 
SET SGSN ODB:BAOC="NO",BAOPS="YES_ACCESS",BOHPAP="YES",BOVPAP="YES"; 
父主题： [SGSN ODB配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN ODB配置(SHOW SGSN ODB) 
## 查询SGSN ODB配置(SHOW SGSN ODB) 
命令功能 
查询SGSN ODB配置，显示当前SGSN设置的ODB
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
BAOC|所有呼出限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果用户在HLR中的签约ODB数据为限制所有呼出：当此参数配置为“是”时，SGSN限制用户不能发送短消息。当此参数配置为“否”时，SGSN不限制用户发送短消息。
BAOPS|所有PS业务限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果用户在HLR中的签约ODB为限制PS业务：当此参数配置为“否”时，系统允许用户附着到SGSN上使用PS业务。当此参数配置为“支持但允许接入”时，系统允许用户附着到SGSN但不能进行PS业务。当此参数配置为“支持且禁止接入”时，系统不允许用户附着到SGSN。
BOHPAP|VPLMN中禁止访问HPLMN APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果用户在HLR中的签约ODB为VPLMN中禁止访问HPLMN APN：VPLMN指漫游用户的拜访PLMN（即本SGSN网元所在的PLMN），HPLMN指漫游用户归属的PLMN。该参数表示是否禁止漫游用户通过HPLMN的GGSN网元激活。当此参数设置为“支持”时，表示漫游用户不能通过HPLMN中的GGSN激活。当此参数设置为“不支持”时，表示漫游用户可以通过HPLMN中的GGSN激活。
BOVPAP|VPLMN中禁止访问VPLMN APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果用户在HLR中的签约ODB为VPLMN中禁止访问VPLMN APN：VPLMN指漫游用户的拜访PLMN（即本SGSN网元所在的PLMN），HPLMN指漫游用户归属的PLMN。该参数表示是否禁止漫游用户通过VPLMN的GGSN网元激活。当此参数设置为“支持”时，表示漫游用户不能通过VPLMN中的GGSN激活。当此参数设置为“不支持”时，表示漫游用户可以通过VPLMN中的GGSN激活。
命令举例 
此命令用于查询SGSN网元支持的ODB功能。 
SHOW SGSN ODB; 
`
命令 (No.1): SHOW SGSN ODB;
操作维护  所有呼出限制   所有PS业务限制   VPLMN中禁止访问HPLMN APN   VPLMN中禁止访问VPLMN APN
---------------------------------------------------------------------------------------------
修改      否             支持但允许接入   支持                       支持
---------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [SGSN ODB配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 漫游GGSN失败配置 
# 漫游GGSN失败配置 
背景知识 
            
            对于漫入用户采用Home-Routed方式激活PDP时，归属地GGSN在创建PDP失败后，给拜访地SGSN返回失败，携带了失败的GTP Cause，拜访地SGSN拒绝PDP激活，携带SM Cause，UE可以根据SM Cause采取合适的处理，SM Cause根据GTP Cause映射。
但是对同一失败场景，不同归属地GGSN返回的GTP Cause可能不同，从而导致UE的行为也不同，可能会导致一些UE的异常行为。因此拜访地SGSN对漫入用户的GTP Cause映射为SM Cause进行一些调整，可以调整一些UE的异常行为，利于UE业务体验提高和网络稳定。
        
功能描述 
            
            对于漫入用户采用Home-Routed方式激活PDP，但漫入用户的归属地GGSN无响应时，通过本功能设置给UE的SM Cause。
注：漫入用户的归属地GGSN的判断参考“
            [SHOW LOCAL GGSNIP]
            ”。
        
相关主题 
 
设置漫游GGSN失败原因(SET GTP FAIL CAUSE)
 
 
查询漫游GGSN失败原因(SHOW GTP FAIL CAUSE)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置漫游GGSN失败原因(SET GTP FAIL CAUSE) 
## 设置漫游GGSN失败原因(SET GTP FAIL CAUSE) 
命令功能 
设置漫游GGSN失败原因
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SWITCH|GTP原因映射开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关
SMCAUSENORSP|无响应时映射的SM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|无响应时映射的SM原因
命令举例 
设置漫游GGSN失败原因 
SET GTP FAIL CAUSE:SWITCH="NO",SMCAUSENORSP="SM_38"; 
父主题： [漫游GGSN失败配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询漫游GGSN失败原因(SHOW GTP FAIL CAUSE) 
## 查询漫游GGSN失败原因(SHOW GTP FAIL CAUSE) 
命令功能 
查询漫游GGSN失败原因
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SWITCH|GTP原因映射开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关
SMCAUSENORSP|无响应时映射的SM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|无响应时映射的SM原因
命令举例 
查询漫游GGSN失败原因 
SHOW GTP FAIL CAUSE; 
`
2019-05-30 12:54:41 命令 (No.8): SHOW GTP FAIL CAUSE
操作维护   GTP原因映射开关   无响应时映射的SM原因   
------------------------------------------------
修改       关                Network failure   
------------------------------------------------
记录数 1
命令执行成功（耗时 0.041 秒）。
` 
父主题： [漫游GGSN失败配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 漫游GGSN失败原因值映射配置 
# 漫游GGSN失败原因值映射配置 
背景知识 
            
            对于漫入用户采用Home-Routed方式激活PDP时，归属地GGSN在创建PDP失败后，给拜访地SGSN返回失败，携带了失败的GTP Cause，拜访地SGSN拒绝PDP激活，携带SM Cause，UE可以根据SM Cause采取合适的处理，SM Cause根据GTP Cause映射。
但是对同一失败场景，不同归属地GGSN返回的GTP Cause可能不同，从而导致UE的行为也不同，可能会导致一些UE的异常行为。因此拜访地SGSN对漫入用户的GTP Cause映射为SM Cause进行一些调整，可以调整一些UE的异常行为，利于UE业务体验提高和网络稳定。
        
功能描述 
            
            对于漫入用户采用Home-Routed方式激活PDP，但漫入用户的归属地GGSN返回失败响应时，通过本功能设置GTP Cause和SM Cause的映射，从而调整给UE的SM Cause。
注：漫入用户的归属地GGSN的判断参考“
            [SHOW LOCAL GGSNIP]
            ”。
        
相关主题 
 
新增漫游GGSN失败原因值映射(ADD GTPTOSM MAPPING)
 
 
删除漫游GGSN失败原因值映射(DEL GTPTOSM MAPPING)
 
 
查询漫游GGSN失败原因值映射(SHOW GTPTOSM MAPPING)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增漫游GGSN失败原因值映射(ADD GTPTOSM MAPPING) 
## 新增漫游GGSN失败原因值映射(ADD GTPTOSM MAPPING) 
命令功能 
新增漫游GGSN失败原因值映射
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FAILGTPCAUSE|GTP失败原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:GTP_204。|需要映射的失败的GTP Cause
MAPSMCAUSE|SM原因映射值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:SM_29。|被映射的SM Cause
命令举例 
新增漫游GGSN失败原因值映射 
ADD GTPTOSM MAPPING:FAILGTPCAUSE="GTP_204",MAPSMCAUSE="SM_29"; 
父主题： [漫游GGSN失败原因值映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除漫游GGSN失败原因值映射(DEL GTPTOSM MAPPING) 
## 删除漫游GGSN失败原因值映射(DEL GTPTOSM MAPPING) 
命令功能 
删除漫游GGSN失败原因值映射
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FAILGTPCAUSE|GTP失败原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|需要映射的失败的GTP Cause
命令举例 
删除漫游GGSN失败原因值映射  
DEL GTPTOSM MAPPING:FAILGTPCAUSE="GTP_204"; 
父主题： [漫游GGSN失败原因值映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询漫游GGSN失败原因值映射(SHOW GTPTOSM MAPPING) 
## 查询漫游GGSN失败原因值映射(SHOW GTPTOSM MAPPING) 
命令功能 
查询漫游GGSN失败原因值映射
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FAILGTPCAUSE|GTP失败原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|需要映射的失败的GTP Cause
MAPSMCAUSE|SM原因映射值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|被映射的SM Cause
命令举例 
查询漫游GGSN失败原因值映射 
SHOW GTPTOSM MAPPING; 
`
2019-05-30 13:03:13 命令 (No.14): SHOW GTPTOSM MAPPING;
操作维护     GTP失败原因值    SM原因映射值   
-----------------------------------------------------------------
复制 删除    System failure   User authentication failed   
-----------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [漫游GGSN失败原因值映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# GGSN本地网段配置 
# GGSN本地网段配置 
背景知识 
            
            对于漫入用户采用Home-Routed方式激活PDP时，归属地GGSN在创建PDP失败后，给拜访地SGSN返回失败，携带了失败的GTP Cause，拜访地SGSN拒绝PDP激活，携带SM Cause，UE可以根据SM Cause采取合适的处理，SM Cause根据GTP Cause映射。
但是对同一失败场景，不同归属地GGSN返回的GTP Cause可能不同，从而导致UE的行为也不同，可能会导致一些UE的异常行为。因此拜访地SGSN对漫入用户的GTP Cause映射为SM Cause进行一些调整，可以调整一些UE的异常行为，利于UE业务体验提高和网络稳定。
        
功能描述 
            
            本功能用于识别漫入用户的归属地GGSN。配置本地GGSN IP地址段后，不在本地GGSN IP地址段的GGSN，为漫入用户的归属地GGSN。
        
相关主题 
 
新增本地GGSN网段(ADD LOCAL GGSNIP)
 
 
删除本地GGSN网段(DEL LOCAL GGSNIP)
 
 
查询本地GGSN网段(SHOW LOCAL GGSNIP)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增本地GGSN网段(ADD LOCAL GGSNIP) 
## 新增本地GGSN网段(ADD LOCAL GGSNIP) 
命令功能 
新增本地GGSN网段
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN网段地址|参数可选性:必选参数；参数类型:地址|GGSN网段地址，和GGSN网段掩码一起确定GGSN网段
GGSNMASK|GGSN网段掩码|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|GGSN网段掩码
命令举例 
新增本地GGSN网段 
ADD LOCAL GGSNIP:GGSNIP="1.1.1.1",GGSNMASK=30; 
父主题： [GGSN本地网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除本地GGSN网段(DEL LOCAL GGSNIP) 
## 删除本地GGSN网段(DEL LOCAL GGSNIP) 
命令功能 
删除本地GGSN网段
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN网段地址|参数可选性:必选参数；参数类型:地址|GGSN网段地址，和GGSN网段掩码一起确定GGSN网段
GGSNMASK|GGSN网段掩码|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|GGSN网段掩码
命令举例 
删除本地GGSN网段 
DEL LOCAL GGSNIP:GGSNIP="1.1.1.1",GGSNMASK=30; 
父主题： [GGSN本地网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询本地GGSN网段(SHOW LOCAL GGSNIP) 
## 查询本地GGSN网段(SHOW LOCAL GGSNIP) 
命令功能 
查询本地GGSN网段
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN网段地址|参数可选性:任选参数；参数类型:地址|GGSN网段地址，和GGSN网段掩码一起确定GGSN网段
GGSNMASK|GGSN网段掩码|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|GGSN网段掩码
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN网段地址|参数可选性:任选参数；参数类型:地址|GGSN网段地址，和GGSN网段掩码一起确定GGSN网段
GGSNMASK|GGSN网段掩码|参数可选性:任选参数；参数类型:整数。|GGSN网段掩码
命令举例 
查询本地GGSN网段  
SHOW LOCAL GGSNIP; 
`
2019-05-30 12:49:12 命令 (No.5): SHOW LOCAL GGSNIP
操作维护     GGSN网段地址   GGSN网段掩码   
---------------------------------------
复制 删除    1.1.1.0        30   
---------------------------------------
记录数 1
命令执行成功（耗时 0.082 秒）。
` 
父主题： [GGSN本地网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME ODB配置 
# MME ODB配置 
背景知识 
支持ODB功能，运营商能够根据用户签约数据中的ODB参数，限制一些用户的业务和服务。 
功能描述 
通过MME ODB配置，MME控制是否禁止用户进行PS业务。
在MME支持禁止用户PS业务，并且在HSS上配置的用户签约数据中设置了禁止用户PS业务时，MME将禁止用户接入PS网络。 
相关主题 
 
设置MME ODB配置(SET MME ODB)
 
 
查询MME ODB配置(SHOW MME ODB)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置MME ODB配置(SET MME ODB) 
## 设置MME ODB配置(SET MME ODB) 
命令功能 
该命令用于设置MME ODB配置信息。当运营商需要控制接入用户的PS业务时，使用该命令。MME ODB配置成功后，如果用户在HSS中签约了ODB，则用户无法接入网络。
注意事项 
配置了该命令后，如果用户已经在网络注册，那么在HSS中修改用户签约ODB时，会触发用户去附着。
参数说明 
标识|名称|类型|说明
---|---|---|---
BAOPS|所有PS业务限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否所有PS业务都受限制，取值含义：否（NO）： MME不支持所有PS业务都受限制是（YES）：MME支持所有PS业务受限制
BOHPAP|漫游禁止访问HPLMN APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否允许漫游用户访问归属地网络信息。取值含义：否（NO）：允许访问是（YES）：禁止访问
BOVPAP|漫游禁止访问VPLMN APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否允许漫游用户访问漫游地网络信息。取值含义：否（NO）: 允许访问是（YES）: 禁止访问
命令举例 
增加MME ODB配置，设置为所有PS业务都受限制。 
SET MME ODB:BAOPS="YES"; 
父主题： [MME ODB配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME ODB配置(SHOW MME ODB) 
## 查询MME ODB配置(SHOW MME ODB) 
命令功能 
该命令用于查询MME ODB配置信息。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
BAOPS|所有PS业务限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否所有PS业务都受限制，取值含义：否（NO）： MME不支持所有PS业务都受限制是（YES）：MME支持所有PS业务受限制
BOHPAP|漫游禁止访问HPLMN APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否允许漫游用户访问归属地网络信息。取值含义：否（NO）：允许访问是（YES）：禁止访问
BOVPAP|漫游禁止访问VPLMN APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否允许漫游用户访问漫游地网络信息。取值含义：否（NO）: 允许访问是（YES）: 禁止访问
命令举例 
查询MME ODB配置。 
SHOW MME ODB; 
`
命令 (No.10): SHOW MME ODB
操作维护 所有PS业务限制 漫游禁止访问HPLMN APN 漫游禁止访问VPLMN APN 
------------------------------------------------------------------------
修改     是             否                    否 
------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.024 秒）。
` 
父主题： [MME ODB配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 跨RAT切换时映射配置 
# 跨RAT切换时映射配置 
背景知识 
跨RAT切换就是指运营商同时部署了多种无线制式的网络并支持用户在不同制式间进行数据业务切换。 
功能描述 
需要支持Pre-R8 3G网络和LTE网络间切换时，在SGSN上配置eNodeB ID到RNC ID的映射和TAI到RAI的映射，用户从Pre-R8 3G网络切换到LTE网络时，如果RNC给SGSN的切换请求中的切换目标是eNodeB ID和TAI，则SGSN根据跨RAT切换时映射配置将eNodeB ID转换为RNC ID和将TAI转换为RAI，SGSN给MME的切换请求中的切换目标是RNC ID和RAI。 
需要支持Pre-R8 3G网络和LTE网络间切换时，在MME上配置RNCID到eNodeB ID的映射和RAI到TAI的映射，用户从Pre-R8 3G网络切换到LTE网络时，SGSN给MME的切换请求中的切换目标是RNCID和RAI，MME根据跨RAT切换时映射配置将RNCID转换为eNodeBID和将RAI转换为TAI，得到真实的切换目标并执行切换流程。 
相关主题 
 
eNB和RNC之间的标识映射配置
 
 
TAI和RAI之间的映射配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## eNB和RNC之间的标识映射配置 
## eNB和RNC之间的标识映射配置 
背景知识 
当运营商同时部署了LTE网络和Pre-R8 3G网络且需要支持两者之间的切换时，需要进行eNB和RNC之间的标识映射配置。 
当UE移动到LTE覆盖（信号）优于UMTS覆盖（信号）的网络区域时，RNC可能会触发UE切换到eNodeB，以便为UE提供更好的服务。 
RNC发送重定位请求Relocation Required消息给SGSN，触发UTRAN到E-UTRAN跨RAT切换流程。 
SGSN收到RNC的重定位请求Relocation Required消息，消息中携带切换目标。 
 
如果切换目标是eNodeB ID和TAI，则需要在SGSN上配置eNodeB ID到RNC ID的映射。SGSN根据eNB和RNC之间的标识映射配置，将切换目标的eNodeB ID映射为RNC ID（真实eNodeB ID映射的虚拟值），SGSN给MME的前传重定位请求Forward Relocation Request消息中的切换目标携带映射的RNC ID。
 
 
如果切换目标是RNC，则不需要进行跨RAT切换流程。
 
 
MME收到SGSN的前传重定位请求Forward Relocation Request，消息中携带切换目标RNC ID。 
 
如果RNC ID值不等于eNodeB ID值，则需要在MME上配置RNC ID到eNodeB ID的映射。MME根据eNB和RNC之间的标识映射配置，将切换目标的RNC ID映射为eNodeB ID，MME在后继切换流程中与该eNodeB进行交互。
 
 
如果RNC ID值等于eNodeB ID值时，则不需要在MME上配置RNC ID到eNodeBID的映射。比如RNC ID值和eNodeB ID值均为100，则不需要进行RNC ID和eNodeB ID值之间的转换。
 
 
当UE移动到UMTS覆盖（信号）优于LTE覆盖（信号）的网络区域时，eNodeB可能会触发UE切换到RNC，以便为UE提供更好的服务。eNodeB发送Handover Required消息给MME，触发E-UTRAN到UTRAN跨RAT切换流程。由于消息的目标就是真实的RNC ID，因此，这种情况不需要特殊的配置。 
功能描述 
                在SGSN网元中，该功能需要软参“SGSN支持Target eNB-ID”打开的情况下才支持，通过命令：
                [SET SOFTWARE PARAMETER]
                :PARAID=786683,PARAVALUE=1;设置。
            
                在SGSN网元中，该功能需要与TAI和RAI的映射关系配置一起配合使用。通过命令：
                [ADD TAI RAI]
                设置。
            
                在MME网元中，该功能需要与TAI和RAI的映射关系配置一起配合使用。通过命令：
                [ADD TAI RAI]
                设置。
            
在MME和SGSN的Combo局中，只需要配置一次。 
相关主题 
 
新增eNB和RNC之间的标识映射配置(ADD ENB RNC)
 
 
修改eNB和RNC之间的标识映射配置(SET ENB RNC)
 
 
删除eNB和RNC之间的标识映射配置(DEL ENB RNC)
 
 
查询eNB和RNC之间的标识映射配置(SHOW ENB RNC)
 
 
父主题： [跨RAT切换时映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增eNB和RNC之间的标识映射配置(ADD ENB RNC) 
### 新增eNB和RNC之间的标识映射配置(ADD ENB RNC) 
命令功能 
该命令用于新增eNodeB ID和RNC ID之间的映射配置。 
 
需要在SGSN上配置eNodeB ID与RNC ID的映射关系，当UE从RNC切换到eNodeB的过程中，SGSN收到RNC的重定位请求Relocation Required消息，如果此消息中携带了切换目标是eNodeB ID和TAI，SGSN可以根据此命令配置的eNodeB ID与RNC ID的映射关系，获取eNodeB ID对应的RNC ID。如果不进行此配置或者删除此配置，当UE从RNC切换到eNodeB的过程中，SGSN将认为RNC ID等于eNodeB ID。
 
 
需要在MME上配置RNC ID与eNodeB ID的映射关系，当UE从RNC切换到eNodeB的过程中，MME收到SGSN发送的前传重定位请求Forward Relocation Request消息，此消息中携带了切换目标RNC ID，MME可以根据此命令配置的RNC ID和eNodeB ID的映射关系，获取RNC ID对应的目标eNodeB ID。如果不进行此配置或者删除此配置，当UE从RNC切换到eNodeB的过程中，MME将认为eNodeB ID等于RNC ID。
 
 
注意事项 
该功能适用于SGSN、MME和COMBO。 
对于SGSN需要软参“SGSN支持Target eNB-ID”打开的情况下才支持，通过命令：[SET SOFTWARE PARAMETER]:PARAID=786683,PARAVALUE=1;设置。
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
RNC|RNC标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|RNC ID，表示UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）网络基站在一个PLMN中的标识号。
ENB|eNodeB标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455 。|eNodeB ID，表示LTE（Long Term Evolution，长期演进）网络基站在一个PLMN中的标识号。
命令举例 
新增eNodeB ID和RNC ID之间的映射关系，当UE从UMTS网络切换到LTE网络时，设置移动国家码为“460”，移动网号为“02”，目标eNodeB ID为“10”，目标eNodeB ID对应的RNC ID为“1001”。 
ADD ENB RNC:MCC="460",MNC="02",RNC=1001,ENB=10; 
父主题： [eNB和RNC之间的标识映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改eNB和RNC之间的标识映射配置(SET ENB RNC) 
### 修改eNB和RNC之间的标识映射配置(SET ENB RNC) 
命令功能 
该命令用于修改eNodeB ID和RNC ID之间的映射配置。 
注意事项 
该功能适用于SGSN、MME和COMBO。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
RNC|RNC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|RNC ID，表示UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）网络基站在一个PLMN中的标识号。
ENB|eNodeB标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB ID，表示LTE（Long Term Evolution，长期演进）网络基站在一个PLMN中的标识号。
命令举例 
修改eNodeB ID和RNC ID之间的映射关系，当UE从UMTS网络切换到LTE网络时，修改移动国家码为“460”，移动网号为“02”，目标eNodeB ID为“5376”，目标eNodeB ID对应的RNC ID为“1010”。 
SET ENB RNC:MCC="460",MNC="03",RNC=1010,ENB=5376; 
父主题： [eNB和RNC之间的标识映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除eNB和RNC之间的标识映射配置(DEL ENB RNC) 
### 删除eNB和RNC之间的标识映射配置(DEL ENB RNC) 
命令功能 
该命令用于删除eNodeB ID和RNC ID之间的映射配置。 
注意事项 
该功能适用于SGSN、MME和COMBO。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
RNC|RNC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|RNC ID，表示UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）网络基站在一个PLMN中的标识号。
ENB|eNodeB标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB ID，表示LTE（Long Term Evolution，长期演进）网络基站在一个PLMN中的标识号。
命令举例 
删除eNodeB ID和RNC ID之间的映射关系，删除值为“1001”的RNC ID所对应的eNodeB ID，移动国家码为“460”，移动网号为“02”。 
DEL ENB RNC:MCC="460",MNC="02",RNC=1001; 
父主题： [eNB和RNC之间的标识映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询eNB和RNC之间的标识映射配置(SHOW ENB RNC) 
### 查询eNB和RNC之间的标识映射配置(SHOW ENB RNC) 
命令功能 
该命令用于查询eNodeB ID和RNC ID之间的映射配置。 
注意事项 
该功能适用于SGSN、MME和COMBO。 
如果不输入任何指定的查询参数，查询结果将返回已配置的所有RNC ID和eNodeB ID之间的映射关系。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
RNC|RNC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|RNC ID，表示UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）网络基站在一个PLMN中的标识号。
ENB|eNodeB标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB ID，表示LTE（Long Term Evolution，长期演进）网络基站在一个PLMN中的标识号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
RNC|RNC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|RNC ID，表示UMTS（Universal Mobile Telecommunication System，通用移动通讯系统）网络基站在一个PLMN中的标识号。
ENB|eNodeB标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB ID，表示LTE（Long Term Evolution，长期演进）网络基站在一个PLMN中的标识号。
命令举例 
查询已配置的所有eNodeB ID和RNC ID之间的映射关系。 
SHOW ENB RNC; 
`
命令 (No.1): SHOW ENB RNC;
移动国家码 移动网号 RNC标识 eNodeB标识 
------------------------------------------------
460           01         30          432 
460           01         1118      1118 
-------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.062 秒）。
` 
父主题： [eNB和RNC之间的标识映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## TAI和RAI之间的映射配置 
## TAI和RAI之间的映射配置 
背景知识 
在EPS网络中，TA（Tracking Area，跟踪区）由一个或多个小区（Cell）组成，跟踪区之间没有重叠区域。 
TAI（Tracking Area Identity，跟踪区标识）是EPS网络用于唯一标识一个跟踪区的编号。 
TAI由三部分组成，格式为：TAC（Tracking Area Code，跟踪区代码）＋MNC＋MCC。 
在3GPP Pre-R8网络中，RA（Routing Area，路由区）由运营商定义，包含一个或多个小区，可等同于一个LA（Location Area，位置区），或是一个位置区的子集（即几个路由区组成一个位置区）。 
RAI（Routing Area Identifier，路由区标识）由四部分组成，格式为：MCC＋MNC＋LAC（Location Area Code，位置区码）＋RAC（Routing Area Code，路由区域码）。 
当运营商同时部署了LTE网络和Pre-R8 3G网络且需要支持两者之间的切换时，需要进行TAI和RAI之间的标识映射配置。 
当UE移动到LTE覆盖（信号）优于UMTS覆盖（信号）的网络区域时，RNC可能会触发UE切换到eNodeB，以便为UE提供更好的服务。 
RNC发送重定位请求Relocation Required消息给SGSN，触发UTRAN到E-UTRAN跨RAT切换流程。 
SGSN收到RNC的重定位请求Relocation Required消息，消息中携带切换目标。 
 
如果切换目标是eNodeB ID和TAI，则需要在SGSN上配置TAI到RAI的映射。SGSN根据TAI和RAI之间的标识映射配置，将切换目标的TAI映射为RAI（真实TAI映射的虚拟值），SGSN给MME的前传重定位请求Forward Relocation Request消息中的切换目标携带映射的RAI。
 
 
如果切换目标是RNC，则不需要进行跨RAT切换流程。
 
 
MME收到SGSN的前传重定位请求Forward Relocation Request，消息中携带切换目标RNC ID和RAI。 
 
如果RAI值不等于TAI，则需要在MME上配置RAI到TAI的映射。MME根据RAI和TAI之间的标识映射配置，将切换目标的RAI映射为TAI，MME使用该TAI查找SGW，并在后继切换流程中使用这个TAI与该SGW进行交互。
 
 
如果RAI值等于TAI值时，则不需要在MME上配置RAI到TAI的映射。比如RAI值和TAI值均为100，则不需要进行RAI和TAI值之间的转换。
 
 
当UE移动到UMTS覆盖（信号）优于LTE覆盖（信号）的网络区域时，eNodeB可能会触发UE切换到RNC，以便为UE提供更好的服务。eNodeB发送Handover Required消息给MME，触发E-UTRAN到UTRAN跨RAT切换流程。由于消息的目标就是真实的RNC ID，因此，这种情况不需要特殊的配置。 
功能描述 
                在SGSN网元中，该功能需要软参“SGSN支持Target eNB-ID”打开的情况下才支持，通过命令：
                [SET SOFTWARE PARAMETER]
                :PARAID=786683,PARAVALUE=1;设置。
            
                在SGSN网元中，该功能需要和eNodeB ID到RNC ID的映射关系配置一起配合使用。通过命令：
                [ADD ENB RNC]
                设置。
            
                在MME网元中，该功能需要和eNodeB ID到RNC ID的映射关系配置一起配合使用。通过命令：
                [ADD ENB RNC]
                设置。
            
在MME和SGSN Combo局中，只需要配置一次。 
相关主题 
 
新增TAI和RAI之间的映射配置(ADD TAI RAI)
 
 
修改TAI和RAI之间的映射配置(SET TAI RAI)
 
 
删除TAI和RAI之间的映射配置(DEL TAI RAI)
 
 
查询TAI和RAI之间的映射配置(SHOW TAI RAI)
 
 
父主题： [跨RAT切换时映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增TAI和RAI之间的映射配置(ADD TAI RAI) 
### 新增TAI和RAI之间的映射配置(ADD TAI RAI) 
命令功能 
该命令用于配置TAI和RAI之间的映射关系。 
当运营商同时部署了LTE网络和UMTS网络，且支持用户在两个网络之间进行切换时，需要配置此功能。 
 
需要在SGSN上配置TAI与RAI的映射关系，当UE从RNC切换到eNodeB的过程中，SGSN收到RNC的重定位请求 Relocation Required消息，如果此消息中携带了切换目标是eNodeB ID和TAI，SGSN可以根据此命令配置TAI与RAI的映射关系，获取TAI对应的RAI。如果不进行此配置或者删除此配置，当UE从RNC切换到eNodeB的过程中，SGSN将认为RAI等于TAI。
 
 
需要在MME上配置TAI和RAI的映射关系，当UE从RNC切换到eNodeB的过程中，MME收到SGSN发送的前传重定位请求Forward Relocation Request消息，此消息中携带了RAI，MME可以根据此命令配置的RAI和TAI的映射关系，获取RAI对应的TAI，再根据TAI选择为UE服务的SGW。如果不进行此配置或者删除此配置，当UE从RNC切换到eNodeB的过程中，MME将认为TAI等于RAI。
 
 
注意事项 
该功能适用于SGSN、MME和COMBO。 
对于SGSN需要软参“SGSN支持Target eNB-ID”打开的情况下才支持，通过命令：[SET SOFTWARE PARAMETER]:PARAID=786683,PARAVALUE=1;设置。
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
LAC|位置区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|LAC（Location Area Code， 位置区域码）用于UMTS网络中，在相同MCC、MNC唯一标识一个LA（Location Area，位置区）的编号。LA是划分网络范围的基本属性。
RAC|路由区码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~2个字符。|RAC（Routing Area Code， 路由区码）用于UMTS网络中，在相同MCC、MNC和LAC下唯一标识一个RA（Routing Area，路由区）的编号。RA是移动用户位置的基本属性，一个LA下可以包含多个RA，一个RA只能属于一个LA。
TAC|跟踪区码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC（Tracking Area Code，跟踪区码）用于LTE网络中， 在相同MCC 和 MNC下 唯一标识TA（Tracking Area，跟踪区）的编号。
命令举例 
添加TAI和RAI的映射关系，当UE从UMTS网络切换到LTE网络时，设置移动国家码为“460”，移动网号为“02”，位置区域码为“1002”，RAC为“01”，该RAC对应的TAC为“0003”。 
ADD TAI RAI:MCC="460",MNC="02",LAC="1002",RAC="01",TAC="0003"; 
父主题： [TAI和RAI之间的映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改TAI和RAI之间的映射配置(SET TAI RAI) 
### 修改TAI和RAI之间的映射配置(SET TAI RAI) 
命令功能 
该命令用于修改TAI和RAI之间的映射配置。 
注意事项 
该功能适用于SGSN、MME和COMBO。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
LAC|位置区域码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|LAC（Location Area Code， 位置区域码）用于UMTS网络中，在相同MCC、MNC唯一标识一个LA（Location Area，位置区）的编号。LA是划分网络范围的基本属性。
RAC|路由区码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:2~2个字符。|RAC（Routing Area Code， 路由区码）用于UMTS网络中，在相同MCC、MNC和LAC下唯一标识一个RA（Routing Area，路由区）的编号。RA是移动用户位置的基本属性，一个LA下可以包含多个RA，一个RA只能属于一个LA。
TAC|跟踪区码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC（Tracking Area Code，跟踪区码）用于LTE网络中， 在相同MCC 和 MNC下 唯一标识TA（Tracking Area，跟踪区）的编号。
命令举例 
修改TAI和RAI的映射关系，移动国家码为“460”，移动网号为“02”，位置区域码为“1003”，RAC为“02”，将该RAC对应的TAC修改为“1005”。 
SET TAI RAI:MCC="460",MNC="02",LAC="1003",RAC="02",TAC="1005"; 
父主题： [TAI和RAI之间的映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除TAI和RAI之间的映射配置(DEL TAI RAI) 
### 删除TAI和RAI之间的映射配置(DEL TAI RAI) 
命令功能 
该命令用于删除TAI和RAI之间的映射配置。 
注意事项 
该功能适用于SGSN、MME和COMBO。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
LAC|位置区域码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|LAC（Location Area Code， 位置区域码）用于UMTS网络中，在相同MCC、MNC唯一标识一个LA（Location Area，位置区）的编号。LA是划分网络范围的基本属性。
RAC|路由区码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:2~2个字符。|RAC（Routing Area Code， 路由区码）用于UMTS网络中，在相同MCC、MNC和LAC下唯一标识一个RA（Routing Area，路由区）的编号。RA是移动用户位置的基本属性，一个LA下可以包含多个RA，一个RA只能属于一个LA。
TAC|跟踪区码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC（Tracking Area Code，跟踪区码）用于LTE网络中， 在相同MCC 和 MNC下 唯一标识TA（Tracking Area，跟踪区）的编号。
命令举例 
删除TAI和RAI的映射关系，移动国家码为“460”，移动网号为“02”，位置区域码为“1005”，RAC为“02”，将该RAC对应的TAC配置记录删除。 
DEL TAI RAI:MCC="460",MNC="02",LAC="1005",RAC="02"; 
父主题： [TAI和RAI之间的映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询TAI和RAI之间的映射配置(SHOW TAI RAI) 
### 查询TAI和RAI之间的映射配置(SHOW TAI RAI) 
命令功能 
该命令用于查询TAI和RAI之间的映射配置。 
如果不输入任何指定的查询参数，查询结果将显示已配置的所有TAI和RAI之间的映射关系。 
注意事项 
该功能适用于SGSN、MME和COMBO。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
LAC|位置区域码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|LAC（Location Area Code， 位置区域码）用于UMTS网络中，在相同MCC、MNC唯一标识一个LA（Location Area，位置区）的编号。LA是划分网络范围的基本属性。
RAC|路由区码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:2~2个字符。|RAC（Routing Area Code， 路由区码）用于UMTS网络中，在相同MCC、MNC和LAC下唯一标识一个RA（Routing Area，路由区）的编号。RA是移动用户位置的基本属性，一个LA下可以包含多个RA，一个RA只能属于一个LA。
TAC|跟踪区码(HEX)|参数可选性:任选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC（Tracking Area Code，跟踪区码）用于LTE网络中， 在相同MCC 和 MNC下 唯一标识TA（Tracking Area，跟踪区）的编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
LAC|位置区域码(HEX)|参数可选性:任选参数；参数类型:字符型。|LAC（Location Area Code， 位置区域码）用于UMTS网络中，在相同MCC、MNC唯一标识一个LA（Location Area，位置区）的编号。LA是划分网络范围的基本属性。
RAC|路由区码(HEX)|参数可选性:任选参数；参数类型:字符型。|RAC（Routing Area Code， 路由区码）用于UMTS网络中，在相同MCC、MNC和LAC下唯一标识一个RA（Routing Area，路由区）的编号。RA是移动用户位置的基本属性，一个LA下可以包含多个RA，一个RA只能属于一个LA。
TAC|跟踪区码(HEX)|参数可选性:任选参数；参数类型:字符型。|TAC（Tracking Area Code，跟踪区码）用于LTE网络中， 在相同MCC 和 MNC下 唯一标识TA（Tracking Area，跟踪区）的编号。
命令举例 
查询UMTS网络中的RAI和LTE网络中TAI之间的映射配置。 
SHOW TAI RAI; 
`
命令 (No.1): SHOW TAI RAI
移动国家码 移动网号 位置区域码(HEX) 路由区码(HEX) 跟踪区码(HEX) 
---------------------------------------------------------------------------
460           01         0001                 01                  0001 
---------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [TAI和RAI之间的映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# HeNB配置 
# HeNB配置 
背景知识 
HeNB家庭基站Home （e）Nodeb是一种小型、低功率蜂窝基站，主要用于家庭及办公室等室内场所，作为蜂窝网在室内无线信号覆盖的补充，为用户提供话音及数据服务。其外形通常和Wi-Fi AP类似，既可以单独使用，也可以集成在家庭网关中作为家庭网络的一部分 。 
CSG闭合用户群：一个家庭基站并不是为所有用户提供服务，而是只能为特定用户服务。因此，提出了闭合用户群的概念（Closed Subscriber Group，CSG），CSG指的是允许接入一个或多个特定小区的一组签约用户。这里的特定小区指的是Home （e）Nodeb所支持的小区。 
HeNB支持3种接入方式：闭合、开放和混合方式。 
闭合方式用于普通家庭，主要给家庭成员使用。只有HeNB关联的CSG的成员才能接入。 
开放方式用于火车站、飞机场、运动场，同普通的宏基站一样允许所有用户接入，主要用于增强运营商公共网络的覆盖和容量。 
混合方式用于商场，企业等，允许所有用户接入，但HeNB对CSG成员提供优先服务。这个场景可能在商场等环境使用，可以对内部员工提供优惠费率以及优先接入权；同时，也允许普通用户使用HeNB来接入，提高室内的无线覆盖范围。 
功能描述 
MME支持HeNB和CSG功能的配置,包括CSG配置和基于IMSI号段限制CSG漫游配置；CSG配置是CSG功能的基本参数配置，包括CSG用户容量、支持CSG的eNB数量等配置项。 
本功能需要License支持，对应的License项为“MME支持CSG功能”。 
相关主题 
 
CSG配置
 
 
基于IMSI号段限制CSG漫游配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## CSG配置 
## CSG配置 
背景知识 
HeNB家庭基站Home （e）Nodeb是一种小型、低功率蜂窝基站，主要用于家庭及办公室等室内场所作为蜂窝网在室内覆盖的补充，为用户提供话音及数据服务。外形通常和Wi-Fi AP类似，既可以单独使用，也可以集成在家庭网关中作为家庭网络的一部分 。 
CSG闭合用户群：一个家庭基站并不是为所有用户提供服务，而是只能为特定用户服务。因此，提出了闭合用户群的概念（Closed Subscriber Group，CSG），CSG指的是允许接入一个或多个特定小区的一组签约用户。这里的特定小区指的是Home （e）Nodeb所支持的小区。 
HeNB支持3种接入方式：闭合、开放和混合方式。 
闭合方式用于普通家庭主要给家庭成员使用。仅是HeNB关联的CSG的成员才能接入。 
开放模式用于火车站、飞机场、运动场，同普通的宏基站一样允许所有用户接入，主要用于增强运营商公共网络的覆盖和容量。 
混合模式用于商场，企业等，除了允许HeNB关联的CSG的成员接入，其它用户也允许接入。不过HeNB可以对成员提供优先服务。这个场景可能在商场等环境使用，可以对内部员工提供优惠费率以及优先接入权；同时，也允许普通用户使用HeNB来接入，提高室内的无线覆盖范围。 
功能描述 
CSG配置是CSG功能的基本参数配置，包括CSG用户容量（签约CSG的用户比例、用户平均签约CSG数目）、支持CSG的eNB数量、是否支持CSG信息更改上报（实时通知SGW/PGW用户CSG信息）以及各接口（S1、S11、Gn、S10）对CSG的支持情况等配置项。 
本功能需要License支持，对应的License项为“支持CSG功能”。 
相关主题 
 
设置CSG配置(SET CSGCFG)
 
 
查询CSG配置(SHOW CSGCFG)
 
 
父主题： [HeNB配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置CSG配置(SET CSGCFG) 
### 设置CSG配置(SET CSGCFG) 
命令功能 
该命令用于设置/修改CSG功能的相关参数，包括支持CSG功能接口列表（S1/S11/Gn/S10）、CSG用户容量（签约CSG的用户比例、用户平均签约CSG数目）、支持CSG的eNB数量、是否支持CSG信息更改上报（实时通知SGW/PGW用户CSG信息）、CSG寻呼是否携带CSG List、是否支持根据TAI查找HeNB-GW配置项。 
当MME网元支持CSG功能时，对CSG用户进行接入控制和移动管理时使用该命令配置基本参数指标。 
当配置成功后，MME根据配置参数情况进行以下各流程的CSG相关业务：Attach、TAU、ServiceRequest、S1切换和CSG用户身份更改流程。 
注意事项 
 
该命令需要加载支持该特性的License，对应的License项为“MME支持CSG功能“，配置命令为：SHOW UMAC LICENSE，License改变要求重启前台。
 
 
修改签约CSG用户比例、CSG用户平均签约CSG数目、支持CSG 的eNodeB数量这几个参数，传表后需要重启前台方可生效。
 
 
CSG成员身份改变流程中，需要配置MME执行CSG成员身份改变策略， 配置命令为：SHOW SOFTWARE PARAMETER，软参ID:65588；软参取值包括0、1、2，默认值为2。
取值含义如下：
0：不执行。对于临时用户和CSG签约数据改变，均不执行身份改变流程。
1：按协议要求执行。对于闭合模式下临时用户和混合模式下的临时用户和CSG签约数据改变执行身份改变流程。（协议要求）
2：均执行身份改变流程。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
INTERFACE|支持CSG的接口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持CSG的接口包括S1、S10、S11、Gn：S1接口：HeNB与MME之间的接口； S11接口：MME与SGW之间的接口； S10接口：MME之间的接口；Gn接口：SGSN与GGSN之间的接口。S1接口为HeNB与MME之间的接口，完成基本CSG接入控制功能。HeNB通知MME，用户接入的小区的CSG ID和接入模式。MME判断是否允许接入。MME判断出用户是否是CSG的成员用户后，或用户的CSG成员身份发生改变，均会通知HeNB，HeNB根据用户是否是成员用户可以提供不同的服务。S10接口为MME之间的接口，Gn接口为SGSN与GGSN之间的接口。S10/Gn接口完成局间CSG信息传递功能。MME会向用户以前所在的网元请求上下文信息。MME在切换时，需要判断用户在目的小区是否是CSG的成员用户，如允许切换需告知目的网元相关的CSG信息。S11接口为MME与SGW之间的接口，完成SGW/PGW相关CSG信息通知功能。MME通知SGW/PGW用户的CSG信息（UCI）。PGW可要求MME主动上报用户的CSG信息。
SSCSGRAT|签约CSG用户比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|用于计算签约CSG用户表容量。默认容量10%，最大容量100%。重启前台生效。
SSAVGCSG|CSG用户平均签约CSG数目|参数可选性:任选参数；参数类型:整数；参数范围为:1~50。|CSG用户平均签约CSG数目指每个CSG用户平均可以访问的CSG小区数量。默认容量10，最大容量50。重启前台生效。
CSGENBNUM|支持CSG的eNodeB数量|参数可选性:任选参数；参数类型:整数；参数范围为:1~25000。|配置此参数时，需根据本网元配置的支持eNodeB数量设置，配置命令为：SHOW CAPACITY。默认容量5000，最大容量为25000。重启前台生效。建议和HEB规划数量一致。
PGCSG|CSG寻呼消息携带CSG List|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|CSG寻呼时，MME是否携带用户签约CSG List（CSG小区列表）给eNB。是（YES)：寻呼消息中MME携带用户签约的CSG List给eNB。否（NO）：对CSG用户寻呼时MME不携带CSG List给eNB，默认采用此方式。
CSGCHGRPT|支持CSG更改上报|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|CSG信息更改后，MME网元是否会通知SGW CSG信息已更改。是（YES）：CSG信息更改后，MME网元通知SGW CSG信息更改，默认采用此方式。否（NO）：CSG信息更改后，MME网元不会通知SGW CSG信息更改。
TAIHO|支持根据TAI查找HeNB-GW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME是否支持根据TAI（跟踪区）查找HeNB-GW。是（YES）：支持根据TAI查找HeNB-GW。MME首先根据eNBID来查找目标eNB，如果查不到，而且目标eNB为HomeNB ID时，则使用TAI来查找支持该TAI的ENB即HeNB-GW，查找成功后，则需向该ENB（HeNB-GW）继续发送Handover Request消息。否（NO）：不支持根据TAI查找HeNB-GW。MME首先根据eNB/HomeNB ID来查找目标eNB/HomeNB，如果查不到，则流程失败。默认采用此方式。
命令举例 
设置CSG配置，其中支持CSG功能的接口是S1口，签约CSG用户比例为50%，CSG用户平均签约CSG数目30，支持CSG的eNodeB数量为500，CSG寻呼消息不携带CSG List，不支持CSG更改上报，不支持根据TAI查找HeNB-GW切换。 
SET CSGCFG:INTERFACE="S1",SSCSGRAT=50,SSAVGCSG=30,CSGENBNUM=500,PGCSG="NO",CSGCHGRPT="NO",TAIHO="NO"; 
父主题： [CSG配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询CSG配置(SHOW CSGCFG) 
### 查询CSG配置(SHOW CSGCFG) 
命令功能 
查看在[SET CSGCFG]中配置的各项参数，无需输入任何参数，查询结果显示如下信息：
 
支持CSG功能接口列表（S1/S11/Gn/S10）
 
 
CSG用户容量（签约CSG的用户比例、用户平均签约CSG数目）
 
 
支持CSG的eNB数量
 
 
是否支持CSG信息更改上报（实时通知SGW/PGW用户CSG信息）
 
 
CSG寻呼是否携带CSG List
 
 
是否支持根据TAI查找HeNB-GW配置项
 
 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
INTERFACE|支持CSG的接口|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|支持CSG的接口包括S1、S10、S11、Gn：S1接口：HeNB与MME之间的接口； S11接口：MME与SGW之间的接口； S10接口：MME之间的接口；Gn接口：SGSN与GGSN之间的接口。S1接口为HeNB与MME之间的接口，完成基本CSG接入控制功能。HeNB通知MME，用户接入的小区的CSG ID和接入模式。MME判断是否允许接入。MME判断出用户是否是CSG的成员用户后，或用户的CSG成员身份发生改变，均会通知HeNB，HeNB根据用户是否是成员用户可以提供不同的服务。S10接口为MME之间的接口，Gn接口为SGSN与GGSN之间的接口。S10/Gn接口完成局间CSG信息传递功能。MME会向用户以前所在的网元请求上下文信息。MME在切换时，需要判断用户在目的小区是否是CSG的成员用户，如允许切换需告知目的网元相关的CSG信息。S11接口为MME与SGW之间的接口，完成SGW/PGW相关CSG信息通知功能。MME通知SGW/PGW用户的CSG信息（UCI）。PGW可要求MME主动上报用户的CSG信息。
SSCSGRAT|签约CSG用户比例(%)|参数可选性:必选参数；参数类型:整数。|用于计算签约CSG用户表容量。默认容量10%，最大容量100%。重启前台生效。
SSAVGCSG|CSG用户平均签约CSG数目|参数可选性:必选参数；参数类型:整数。|CSG用户平均签约CSG数目指每个CSG用户平均可以访问的CSG小区数量。默认容量10，最大容量50。重启前台生效。
CSGENBNUM|支持CSG的eNodeB数量|参数可选性:必选参数；参数类型:整数。|配置此参数时，需根据本网元配置的支持eNodeB数量设置，配置命令为：SHOW CAPACITY。默认容量5000，最大容量为25000。重启前台生效。建议和HEB规划数量一致。
PGCSG|CSG寻呼消息携带CSG List|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|CSG寻呼时，MME是否携带用户签约CSG List（CSG小区列表）给eNB。是（YES)：寻呼消息中MME携带用户签约的CSG List给eNB。否（NO）：对CSG用户寻呼时MME不携带CSG List给eNB，默认采用此方式。
CSGCHGRPT|支持CSG更改上报|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|CSG信息更改后，MME网元是否会通知SGW CSG信息已更改。是（YES）：CSG信息更改后，MME网元通知SGW CSG信息更改，默认采用此方式。否（NO）：CSG信息更改后，MME网元不会通知SGW CSG信息更改。
TAIHO|支持根据TAI查找HeNB-GW|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|MME是否支持根据TAI（跟踪区）查找HeNB-GW。是（YES）：支持根据TAI查找HeNB-GW。MME首先根据eNBID来查找目标eNB，如果查不到，而且目标eNB为HomeNB ID时，则使用TAI来查找支持该TAI的ENB即HeNB-GW，查找成功后，则需向该ENB（HeNB-GW）继续发送Handover Request消息。否（NO）：不支持根据TAI查找HeNB-GW。MME首先根据eNB/HomeNB ID来查找目标eNB/HomeNB，如果查不到，则流程失败。默认采用此方式。
命令举例 
查询已配置的CSG信息。 
SHOW CSGCFG; 
`
命令 (No.1): SHOW CSGCFG;
支持CSG的接口   签约CSG用户比例(%)   CSG用户平均签约CSG数目   支持CSG的eNodeB数量   CSG寻呼消息携带CSG List   支持CSG更改上报   支持根据TAI查找HeNB-GW
------------------------------------------------------------------------------------------------------------------------------------------------------
S1              50                   30                       500                   否                        否                不支持
------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.052 秒）。
` 
父主题： [CSG配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于IMSI号段限制CSG漫游配置 
## 基于IMSI号段限制CSG漫游配置 
背景知识 
对于每个运营商来说用户的CSG签约是独立的，因此对于漫游用户携带的的CSG签约信息，拜访地的MME可以选择不使用(将该用户作为普通用户)。 
功能描述 
根据IMSI号段（MME可对IMSI号段进行最长匹配）限制漫游用户是否能使用CSG签约信息。配置为忽略CSG签约信息的用户被当做是普通用户。 
本功能需要License支持，对应的License项为“MME支持CSG功能”。 
相关主题 
 
新增基于IMSI号段限制CSG漫游配置(ADD IMSI CSG ROAM)
 
 
修改基于IMSI号段限制CSG漫游配置(SET IMSI CSG ROAM)
 
 
删除基于IMSI号段限制CSG漫游配置(DEL IMSI CSG ROAM)
 
 
查询基于IMSI号段限制CSG漫游配置(SHOW IMSI CSG ROAM)
 
 
父主题： [HeNB配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于IMSI号段限制CSG漫游配置(ADD IMSI CSG ROAM) 
### 新增基于IMSI号段限制CSG漫游配置(ADD IMSI CSG ROAM) 
命令功能 
该命令用于新增基于IMSI号段限制CSG漫游配置。 
基于IMSI号段的CSG限制策略包括： 
 
使用漫游用户的CSG签约信息
当配置此策略时，需要检查用户的CSG签约信息，根据用户签约的CSG信息来判断是否要限制。
 
 
忽略漫游用户的CSG签约信息
当配置此策略时，需要忽略该用户签约的CSG信息，直接按普通用户处理。
 
 
如果没有配置CSG限制策略，则按照使用签约的CSG策略处理，即根据用户签约的CSG信息处理。 
注意事项 
该命令需要加载支持该特性的License，对应的License项为“MME支持CSG功能”，配置命令为：[SHOW LICENSE]，License改变要求重启前台。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行CSG漫游限制的作用，而不需要将每个用户的完整号码都配置上。
LMTRES|CSG限制选项|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|对CSG漫游用户是否进行限制。使用签约的CSG（USE）：对于CSG小区接入的漫游用户，根据该用户签约CSG信息进行限制检查，若签约允许则允许用户接入，否则禁止用户接入。忽略签约的CSG（IGNORE）：禁止漫游用户从CSG小区接入。
命令举例 
新增基于IMSI号段限制CSG漫游配置，其中IMSI号段为46001，CSG限制选项为使用签约的CSG。 
ADD IMSI CSG ROAM:IMSI="46001",LMTRES="USE"; 
父主题： [基于IMSI号段限制CSG漫游配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于IMSI号段限制CSG漫游配置(SET IMSI CSG ROAM) 
### 修改基于IMSI号段限制CSG漫游配置(SET IMSI CSG ROAM) 
命令功能 
该命令用于修改IMSI号段的CSG限制策略。根据IMSI号段修改CSG限制为使用签约CSG还是忽略签约CSG。
注意事项 
所要修改的IMSI号段，必须是在[ADD IMSI CSG ROAM]中增加过的IMSI号段才能修改，否则会提示“要修改的IMSI号段（***）并不存在!”。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行CSG漫游限制的作用，而不需要将每个用户的完整号码都配置上。
LMTRES|CSG限制选项|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|对CSG漫游用户是否进行限制。使用签约的CSG（USE）：对于CSG小区接入的漫游用户，根据该用户签约CSG信息进行限制检查，若签约允许则允许用户接入，否则禁止用户接入。忽略签约的CSG（IGNORE）：禁止漫游用户从CSG小区接入。
命令举例 
修改号段为46001基于IMSI号段限制CSG漫游配置，将CSG限制选项修改为忽略签约的CSG。 
SET IMSI CSG ROAM:IMSI="46001",LMTRES="IGNORE"; 
父主题： [基于IMSI号段限制CSG漫游配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于IMSI号段限制CSG漫游配置(DEL IMSI CSG ROAM) 
### 删除基于IMSI号段限制CSG漫游配置(DEL IMSI CSG ROAM) 
命令功能 
该命令用于删除指定IMSI号段的CSG限制策略。 
注意事项 
所要删除的IMSI号段，必须是已配置过的IMSI号段才能修改，否则会提示“要删除的IMSI号段（***）并不存在！”。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行CSG漫游限制的作用，而不需要将每个用户的完整号码都配置上。
命令举例 
删除IMSI号段为46001的限制CSG漫游配置。 
DEL IMSI CSG ROAM:IMSI=46001; 
父主题： [基于IMSI号段限制CSG漫游配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于IMSI号段限制CSG漫游配置(SHOW IMSI CSG ROAM) 
### 查询基于IMSI号段限制CSG漫游配置(SHOW IMSI CSG ROAM) 
命令功能 
该命令用于查询IMSI号段限制CSG漫游配置信息，显示IMSI号段的CSG限制策略为使用签约的CSG还是忽略签约的CSG。 
 
可根据某个IMSI号段查询此IMSI号段的CSG限制策略。
 
 
不输入任何参数时，表示查询所有IMSI号段的CSG限制策略。
 
 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行CSG漫游限制的作用，而不需要将每个用户的完整号码都配置上。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI，International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行CSG漫游限制的作用，而不需要将每个用户的完整号码都配置上。
LMTRES|CSG限制选项|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|对CSG漫游用户是否进行限制。使用签约的CSG（USE）：对于CSG小区接入的漫游用户，根据该用户签约CSG信息进行限制检查，若签约允许则允许用户接入，否则禁止用户接入。忽略签约的CSG（IGNORE）：禁止漫游用户从CSG小区接入。
命令举例 
查询已配置的基于IMSI号段限制CSG漫游配置。 
SHOW IMSI CSG ROAM; 
`
命令 (No.1): SHOW IMSI CSG ROAM;
IMSI号段   CSG限制选项
----------------------
46001      使用签约的CSG
----------------------
记录数 1
命令执行成功（耗时 0.042 秒）。
` 
父主题： [基于IMSI号段限制CSG漫游配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 基于号段选择S-GW配置 
# 基于号段选择S-GW配置 
背景知识 
基于IMSI/MSISDN号码或号段进行S-GW选择是运营商的普遍需求。 
基于号段选择S-GW，可用于S-GW灵活选择，也用于对新入网或可能出故障的S-GW进行测试。其优点是： 
 
MME可以基于用户灵活选择S-GW，如：VIP用户需要接入特定的S-GW，享用特殊的网络资源。
 
 
满足一定的拨测场景，如：
场景一：运维人员需要测试新入网的S-GW，而DNS中没有该S-GW的配置数据，现网不方便在DNS上加入这个测试数据的场景，MME根据基于号段选择S-GW配置，能够将测试号码指向该S-GW进行拨测；
场景二：运维人员怀疑某个S-GW可能有问题或者故障，MME根据基于号段选择S-GW配置，能够将测试号码指向该S-GW进行拨测。
 
 
功能描述 
用户发起附着或跟踪区更新请求，或着eNodeB发起SGW改变的切换请求，MME收到请求后进行如下处理： 
MME根据MSISDN/IMSI号码及号段获得S-GW列表。 
MME根据S-GW列表中的每一个S-GW的主机名、service类型、protocol类型、优先级、权重因子，结合选择策略确定一个S-GW地址。 
配置基于号段选择S-GW功能的流程如下： 
                        配置“是否支持基于号段选择S-GW”为“支持”，配置命令为：
                        [SET SGW SELECTION SPRT]
                        :SELSGWFLAG="YES"。
                    
                        配置“基于号段选择S-GW方式”，配置命令为：
                        [SET SGW SELECTION MODE]
                        。
                    
                        配置“基于号段选择S-GW配置”，配置命令为：
                        [ADD SGW SELECTION]
                        。
                    
说明： 
如果“基于号段选择S-GW方式”配置为“支持基于号段本地解析地址”，则MME根据IMSI/MSISDN号码或号段获得本局配置的每个S-GW的主机名称、IP地址、支持协议类型、优先级和负荷因子，根据选择策略选出一个S-GW，这种方式推荐对新入网或可能出故障的S-GW进行测试时使用。 
如果“基于号段选择S-GW方式”配置为“不支持基于号段本地解析地址”，则MME根据IMSI/MSISDN号码或号段获得本局配置的S-GW主机名列表，与MME根据用户的TAI/eNB FQDN本地HOST或DNS查询到的S-GW列表取交集，对交集中的S-GW列表根据选择策略选出一个S-GW，这种方式推荐在商用而非测试情况下使用；如果交集为空，MME还可以控制号段选择失败后是否重选S-GW，配置为重选时，则MME根据用户的TAI/eNB FQDN本地HOST或DNS查询到的S-GW列表，根据选择策略选出一个S-GW，不再基于号码或号段选择S-GW。 
相关主题 
 
设置是否支持基于号段选择S-GW(SET SGW SELECTION SPRT)
 
 
查询是否支持基于号段选择S-GW(SHOW SGW SELECTION SPRT)
 
 
新增基于号段选择S-GW配置(ADD SGW SELECTION)
 
 
修改基于号段选择S-GW配置(SET SGW SELECTION)
 
 
增加S-GW地址(ADD SGW IPADDR)
 
 
删除S-GW地址(DEL SGW IPADDR)
 
 
删除基于号段选择S-GW配置(DEL SGW SELECTION)
 
 
查询基于号段选择S-GW配置(SHOW SGW SELECTION)
 
 
设置基于号段选择S-GW方式(SET SGW SELECTION MODE)
 
 
查询基于号段选择S-GW方式(SHOW SGW SELECTION MODE)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置是否支持基于号段选择S-GW(SET SGW SELECTION SPRT) 
## 设置是否支持基于号段选择S-GW(SET SGW SELECTION SPRT) 
命令功能 
该命令用于配置MME是否支持基于号段选择S-GW。当需要修改MME基于号段选择S-GW时，使用该命令。使用该命令成功后，能打开或者关闭基于号段选择S-GW功能。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SELSGWFLAG|是否支持基于号段选择S-GW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于号段选择S-GW。“不支持（NO）”：MME不支持MME基于号段选择S-GW。“支持（YES）”：MME支持MME基于号段选择S-GW。
命令举例 
设置MME支持基于号段选择S-GW。 
SET SGW SELECTION SPRT:SELSGWFLAG="YES"; 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询是否支持基于号段选择S-GW(SHOW SGW SELECTION SPRT) 
## 查询是否支持基于号段选择S-GW(SHOW SGW SELECTION SPRT) 
命令功能 
该命令用于查询MME是否支持基于号段选择S-GW。当需要查看MME是否支持基于号段选择S-GW时，使用该命令。使用该命令成功后，查询出基于号段选择S-GW的功能是开启还是关闭。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SELSGWFLAG|是否支持基于号段选择S-GW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于号段选择S-GW。“不支持（NO）”：MME不支持MME基于号段选择S-GW。“支持（YES）”：MME支持MME基于号段选择S-GW。
命令举例 
查看MME是否支持基于号段选择S-GW。 
SHOW SGW SELECTION SPRT; 
`
命令 (No.1): SHOW SGW SELECTION SPRT
操作维护  是否支持基于号段选择S-GW
----------------------------------
修改      不支持
----------------------------------
记录数 1
命令执行成功（耗时 0.136 秒）。
` 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增基于号段选择S-GW配置(ADD SGW SELECTION) 
## 新增基于号段选择S-GW配置(ADD SGW SELECTION) 
命令功能 
该命令用于新增基于号段选择S-GW配置。当需要新增基于号段选择S-GW配置时，使用该命令。使用该命令执行成功后，该IMSI号段的用户使用接入该配置的SGW。 
如果 "用户号码+号码类型"在[SET SGW SELECTION MODE]命令中设置为"支持基于号段本地解析地址"，则用户接入SGW时优先使用本命令配置的IP地址组中的地址，而支持的协议类型、优先级和负荷因子作为待选地址组的选择策略；否则使用主机名与DNS解析或者与EPC HOST解析的结果的交集数据作为待选地址组的选择策略。
注意事项 
 
 该命令必须在SET SGW SELECTION SPRT:SELSGWFLAG="YES";的情况下，配置信息才会生效。执行SHOW SGW SELECTION SPRT命令查询是否支持基于号段选择S-GW。
 
 
如果配置了多个IP地址，且分属不同的子网段，则可以配置不同子网段具有不同的优先级，MME进行解析时，将会选择属于优先级最高子网段的IP地址。配置子网优先级参考命令（ADD HOST SUBNET PRI）。
 
 
如果最高优先级的子网段中有多个IP地址，则轮流选择这些IP地址作为目标地址。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
SGWHOST|S-GW主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置SGW主机名称。
IPADDR|IP地址|参数可选性:特殊任选参数；参数类型:地址|该参数用于配置SGW的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持10个地址，可配置小于等于10的任意个IP地址。以下各IP地址同此说明，不再详述。
PROTOCOL|支持协议类型|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-s11(x-s11): 支持GTP协议的S11接口
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|优先级，数值越小代表优先级越高。优先级越高的SGW被选中的几率也越大。
NAPTRWEIGHT|负荷因子|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:200。|权重，数值越大权重越大，当优先级一样时，权重越大的SGW被选择使用的概率越大。
命令举例 
增加基于号段选择S-GW配置，其中用户号码为8613675138501、号码类型为MSISDN、SGW主机名是HostName。 
ADD SGW SELECTION:NUMBER="8613675138501",NUMTYPE="MSISDN",SGWHOST="HostName"; 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改基于号段选择S-GW配置(SET SGW SELECTION) 
## 修改基于号段选择S-GW配置(SET SGW SELECTION) 
命令功能 
该命令用于修改基于号段选择S-GW配置。当需要修改IP地址、支持协议类型、优先级和负荷因子时，使用该命令。使用该命令成功后，基于号段选择S-GW配置信息被修改。
注意事项 
 该命令必须在SET SGW SELECTION SPRT: SELSGWFLAG="YES";的情况下，配置信息才会生效。
 
 
如果配置了多个IP地址，且分属不同的子网段，则可以配置不同子网段具有不同的优先级，MME进行解析时，将会选择属于优先级最高子网段的IP地址。配置子网优先级参考命令（ADD HOST SUBNET PRI）。
 
 
如果最高优先级的子网段中有多个IP地址，则轮流选择这些IP地址作为目标地址。
 
 
如果"号码+号码类型"在SET SGW SELECTION MODE命令中设置为支持基于号段本地解析地址，则优先使用配置的IP地址，而支持的协议类型、优先级和负荷因子数据作为待选地址组的选择策略；否则使用SGW主机名与DNS解析或者与EPCHOST解析的结果的交集作为待选地址组的选择策略。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
SGWHOST|S-GW主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置SGW主机名称。
IPADDR|IP地址|参数可选性:任选参数；参数类型:地址|该参数用于配置SGW的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持10个地址，可配置小于等于10的任意个IP地址。以下各IP地址同此说明，不再详述。
PROTOCOL|支持协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-s11(x-s11): 支持GTP协议的S11接口
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|优先级，数值越小代表优先级越高。优先级越高的SGW被选中的几率也越大。
NAPTRWEIGHT|负荷因子|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|权重，数值越大权重越大，当优先级一样时，权重越大的SGW被选择使用的概率越大。
命令举例 
设置基于号段选择S-GW配置，其中用户号码为
8613675138501、号码类型为MSISDN、SGW主机名为HostName、IP地址为"1.2.3.4"、SGWHOST为HostName、支持的协议类型为x-s5-gtp。 
SET SGW SELECTION:NUMBER="8613675138501",NUMTYPE="MSISDN",SGWHOST="HostName",IPADDR="1.2.3.4",PROTOCOL="x-s5-gtp"; 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 增加S-GW地址(ADD SGW IPADDR) 
## 增加S-GW地址(ADD SGW IPADDR) 
命令功能 
该命令用于增加S-GW地址。当需要在SGW SELECTION记录中增加解析的地址时，使用该命令。 
使用该命令成功后，会为指定的号码+号码类型+SGW主机名增加一个SGW地址。 
注意事项 
 
 该命令必须在SET SGW SELECTION SPRT: SELSGWFLAG="YES";的情况下，配置信息才会生效。执行SHOW SGW SELECTION SPRT命令查询是否支持基于号段选择S-GW。
 
 
增加SGW IP地址配置，一次只能增加一个地址。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
SGWHOST|S-GW主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置SGW主机名称。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|该参数用于配置PGW或GGSN的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持10个地址，可配置小于等于10的任意个IP地址。以下各IP地址同此说明，不再详述。
命令举例 
增加S-GW地址，其中用户号码为8613675138501、号码类型为MSISDN、SGW主机名为HostName、新增的地址为"1.2.3.4"。 
ADD SGW IPADDR:NUMBER="8613675138501",NUMTYPE="MSISDN",SGWHOST="HostName",IPADDR="1.2.3.4"; 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除S-GW地址(DEL SGW IPADDR) 
## 删除S-GW地址(DEL SGW IPADDR) 
命令功能 
该命令用于删除S-GW地址。当需要删除SGW地址时，使用该命令。使用该命令成功后，会为指定的号码+号码类型+SGW 主机名删除一个SGW地址。
注意事项 
删除S-GW IP地址配置，一次只能删除一个地址。
参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
SGWHOST|S-GW主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置SGW主机名称。
IPADDR|IP地址|参数可选性:必选参数；参数类型:地址|该参数用于配置PGW或GGSN的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持10个地址，可配置小于等于10的任意个IP地址。以下各IP地址同此说明，不再详述。
命令举例 
删除S-GW地址，其中用户号码为8613675138501，号码类型为MSISDN、SGW主机名为HostName，删除的地址为"1.2.3.4"。 
DEL SGW IPADDR:NUMBER="8613675138501",NUMTYPE="MSISDN",SGWHOST="HostName",IPADDR="1.2.3.4"; 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除基于号段选择S-GW配置(DEL SGW SELECTION) 
## 删除基于号段选择S-GW配置(DEL SGW SELECTION) 
命令功能 
该命令用于删除基于号段选择S-GW配置。当需要删除基于号段选择S-GW配置记录时，使用该命令。该命令执行成功后，会删除指定号码+号码类型+SGW主机名的配置记录。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
SGWHOST|S-GW主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置SGW主机名称。
命令举例 
删除基于号段选择S-GW配置，其中用户号码为8613675138501、号码类型为MSISDN、SGW主机名为HostName。 
DEL SGW SELECTION:NUMBER="8613675138501",NUMTYPE="MSISDN",SGWHOST="HostName"; 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询基于号段选择S-GW配置(SHOW SGW SELECTION) 
## 查询基于号段选择S-GW配置(SHOW SGW SELECTION) 
命令功能 
该命令用于查询基于号段选择S-GW配置。当需要查看基于号段选择S-GW配置时，使用该命令。使用该命令成功后能查询基于号段选择S-GW配置的信息。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
SGWHOST|S-GW主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置SGW主机名称。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:任选参数；参数类型:字符型。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
SGWHOST|S-GW主机名|参数可选性:任选参数；参数类型:字符型。|该参数用于设置SGW主机名称。
IPADDR1|IP地址1|参数可选性:任选参数；参数类型:字符型。|该参数用于配置SGW的IP地址，可配置为IPv4地址或IPv6地址，IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持10个地址，可配置小于等于10的任意个IP地址。以下各IP地址同此说明，不再详述。
IPADDR2|IP地址2|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
IPADDR3|IP地址3|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
IPADDR4|IP地址4|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
IPADDR5|IP地址5|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
IPADDR6|IP地址6|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
IPADDR7|IP地址7|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
IPADDR8|IP地址8|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
IPADDR9|IP地址9|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
IPADDR10|IP地址10|参数可选性:任选参数；参数类型:字符型。|同参数IPADDR1描述。
PROTOCOL|支持协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置目标局所支持的接口类型，目前支持如下接口类型。x-s5-gtp: 支持GTP协议的S5接口x-s5-pmip: 支持PMIP协议的S5接口x-s8-gtp: 支持GTP协议的S8接口x-s8-pmip: 支持PMIP协议的S8接口x-s11(x-s11): 支持GTP协议的S11接口
NAPTRORDER|优先级|参数可选性:任选参数；参数类型:整数。|优先级，数值越小代表优先级越高。优先级越高的SGW被选中的几率也越大。
NAPTRWEIGHT|负荷因子|参数可选性:任选参数；参数类型:整数。|权重，数值越大权重越大，当优先级一样时，权重越大的SGW被选择使用的概率越大。
命令举例 
显示基于号段选择S-GW配置，其中用户号码为8613675138501、号码类型为MSISDN、SGW主机名为HostName。 
SHOW SGW SELECTION:NUMBER="8613675138501",NUMTYPE="MSISDN",SGWHOST="HostName"; 
`
命令 (No.1): SHOW SGW SELECTION:NUMBER="8613675138501",NUMTYPE="MSISDN",SGWHOST="HostName";
操作维护         用户号码        号码类型   S-GW主机名   IP地址1   IP地址2   IP地址3   IP地址4   IP地址5   IP地址6   IP地址7   IP地址8   IP地址9   IP地址10   支持协议类型   优先级   负荷因子
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   8613675138501   MSISDN     hostname     1.2.3.4   0.0.0.0   0.0.0.0   0.0.0.0   0.0.0.0   0.0.0.0   0.0.0.0   0.0.0.0   0.0.0.0   0.0.0.0    x-s5-gtp       0        200
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.064 秒）。
` 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置基于号段选择S-GW方式(SET SGW SELECTION MODE) 
## 设置基于号段选择S-GW方式(SET SGW SELECTION MODE) 
命令功能 
该命令用于设置基于号段选择S-GW方式。当需要设置基于号段选择S-GW方式时，使用该命令。使用该命令成功后，根据不同的配置产生不同的结果，各配置产生的结果说明如下。 
 
如果MME支持基于号段本地解析地址，则MME基于号段选择SGW失败后，不再进行重选。MME支持基于号段本地解析地址时，使用本地配置的地址、权重、优先级和协议作为选择策略；否则使用本地配置的SGW主机名与DNS解析或与EPC HOST解析结果的交集数据作为选择策略的来源。
 
 
在MME支持号段选择失败后重选S-GW且不支持基于号段本地解析地址的情况下，使用配置的SGW主机名与DNS解析或者与EPC HOST解析取交集的数据作为选择策略的来源，如果MME选择SGW失败，则MME在DNS或EPC HOST解析的结果中再次选择SGW。
 
 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
RESELSGW|号段选择失败后是否重选S-GW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于号段选择失败后重新选择S-GW。“否（NO）”：MME基于号段选择SGW失败后，不重选S-GW。“是（YES）”：MME基于号段选择SGW失败后，重选S-GW。
HOSTTRANS|是否支持基于号段本地解析地址|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于号段本地解析地址。“否（NO）”：MME不支持基于号段本地解析地址。“是（YES）”：MME支持基于号段本地解析地址。
命令举例 
设置基于号段选择S-GW方式，其中用户号码为8613675138501、号码类型为MSISDN、"号段选择失败后是否重选S-GW"为NO、"是否支持基于号段本地解析地址"为YES。 
SET SGW SELECTION MODE:NUMBER="8613675138501",NUMTYPE="MSISDN",RESELSGW="NO",HOSTTRANS="YES"; 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询基于号段选择S-GW方式(SHOW SGW SELECTION MODE) 
## 查询基于号段选择S-GW方式(SHOW SGW SELECTION MODE) 
命令功能 
该命令用于查询基于号段选择S-GW方式配置信息。当需要查看基于号段选择S-GW方式配置信息时，使用该命令。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NUMBER|用户号码|参数可选性:任选参数；参数类型:字符型。|IMSI号码前缀或MSISDN号码前缀
NUMTYPE|号码类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户号码类型。“MSISDN（MSISDN）”：MSISDN指主叫用户在呼叫GSM PLMN中的一个移动用户所需拨的号码MSISDN，作用等同于固定网PSTN号码，是在公共电话网交换网络编号计划中，唯一能识别移动用户的号码。“IMSI（IMSI）”：IMSI（International Mobile Subscriber Identity，国际移动用户标识）是核心网交换系统分配给移动用户的唯一的识别号，采取E.212编码方式。
RESELSGW|号段选择失败后是否重选S-GW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于号段选择失败后重新选择S-GW。“否（NO）”：MME基于号段选择SGW失败后，不重选S-GW。“是（YES）”：MME基于号段选择SGW失败后，重选S-GW。
HOSTTRANS|是否支持基于号段本地解析地址|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于号段本地解析地址。“否（NO）”：MME不支持基于号段本地解析地址。“是（YES）”：MME支持基于号段本地解析地址。
命令举例 
显示基于号段选择S-GW方式。 
SHOW SGW SELECTION MODE 
`
命令 (No.1): SHOW SGW SELECTION MODE
操作维护  用户号码        号码类型   号段选择失败后是否重选S-GW   是否支持基于号段本地解析地址
----------------------------------------------------------------------------------------------
修改      8613675138501   MSISDN     否                           是
----------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [基于号段选择S-GW配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 紧急呼叫配置 
# 紧急呼叫配置 
背景知识 
紧急呼叫（Emergency Call），所谓紧急呼叫是指用手机拨打911、110之类的报警或求救号码。 
在传统电路域网络中，紧急呼叫为网络的基本服务，随着网络发展电路域最终将被数据域完全替代。在EPC网络中，运营商通过IMS 为用户提供语音业务，同时也需要能提供紧急呼叫业务，EPC与IMS网络建立紧急会话来给用户提供紧急呼叫业务。为了给紧急呼叫提供端到端的保障，EPC网络需要为IMS紧急会话提供紧急承载，保证EPC承载的优先级和QoS。 
紧急呼叫建立的过程如下： 
 
UE注册在EPC网络中。
 
 
用户拨打紧急号码发起呼叫，UE发起紧急PDN连接请求，MME完成紧急PDN连接建立，将P-CSCF地址返回给UE。
 
 
UE获得P-CSCS地址后发起到IMS网络的注册。
 
 
UE完成注册后，发出Invite消息到IMS网络，IMS为UE发起专有承载的建立，建立成功将UE接续到紧用中心（emergency center），完成紧急呼叫建立。
 
 
功能描述 
如MME需支持紧急呼叫功能，需对本模块进行配置。 
本模块包含三部分，分别是紧急呼叫策略开关控制、紧急号码列表配置和紧急数据配置。 
紧急呼叫策略开关控制，对MME支持紧急呼叫功能的能力进行控制，包括： 
紧急呼叫策略开关控制 
对MME支持紧急呼叫功能的能力进行控制，包括： 
 
设置MME是否支持紧急呼叫功能。
 
 
设置MME是否支持无卡用户进行紧急呼叫功能。
 
 
设置用户进行紧急附着业务时，MME是否对其进行鉴权。
 
 
设置当用户鉴权失败时，MME是否继续让用户进行紧急呼叫。
 
 
设置MME是否支持受限用户（位置受限或欠费）进行紧急呼叫。
 
 
紧急号码列表 
MME在附着或TAU业务中通知UE，其当前所在TAI位置所对应的紧急号码列表，UE在拨打号码时通过与此列表比对，来判断当前拨打的是否为紧急呼叫。 
紧急数据配置 
配置紧急呼叫所使用承载的Qos信息，包括： 
 
APN，在未配置PGW标识时，使用此APN来获得指定PGW，此APN为全网规划，通过APN识别出当前承载被用于紧急呼叫。
 
 
紧急承载使用的QCI（QoS Class Identifier）。
 
 
紧急承载使用的AMBR（Aggregate Maximum Bit Rate）。
 
 
紧急承载使用的ARP（Allocation Retention Priority）。
 
 
PGW标识（PGW的FQDN域名或IP地址），MME向此PGW建立紧用承载。
 
 
相关主题 
 
控制开关配置
 
 
紧急数据配置
 
 
紧急号码列表配置
 
 
基于IMSI的紧急呼叫支持标识配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 控制开关配置 
## 控制开关配置 
背景知识 
在R10 3GPP 23.401协议中，对于MME支持紧急呼叫的功能，定义以下四种用户支持紧急呼叫： 
 
完全合法有效用户
 
 
鉴权合法用户（可能位置被限制）
 
 
具有IMSI的用户（可能鉴权失败、位置被限制）
 
 
任意用户（可能不具有IMSI、鉴权失败、位置被限制）
 
 
功能描述 
本模块可控制MME对于紧急呼叫功能的支持能力，包括有MME是否支持紧急呼叫、紧急附着是否鉴权，是否保留非紧急PDN连接等。 
相关主题 
 
设置紧急呼叫配置(SET EMERGENCYCFG)
 
 
查询紧急呼叫配置(SHOW EMERGENCYCFG)
 
 
父主题： [紧急呼叫配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置紧急呼叫配置(SET EMERGENCYCFG) 
### 设置紧急呼叫配置(SET EMERGENCYCFG) 
命令功能 
该命令用于紧急呼叫控制信息。当需要根据业务级别、用户级别、用户行为确定用户在LTE网络中发起紧急呼叫时，是否允许用户接入网络或继续使用紧急呼叫功能。 
在需要启用紧急呼叫功能时，需要按照控制策略执行该命令，设置相应的控制开关。 
若当前网络不支持紧急呼叫功能时，需要关闭紧急呼叫功能的控制开关。 
注意事项 
 
该命令传表后直接生效，无需重启单板。但是不建议反复修改，应在制定紧急呼叫控制策略后进行设置并保持不变，直至启用新的紧急呼叫策略。反复修改可能会对当前正在使用紧急呼叫业务的用户产生不良影响，如紧急呼叫被迫中断。
 
 
呼叫优先级需要安全变量262319的支持，查询使用命令SHOW SOFTWARE PARAMETER:PARAID=262319;
 
 
开启紧急呼叫控制开关，支持紧急呼叫功能，必须配置相应的紧急呼叫配置数据，参见命令ADD EMERGDATA。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICY|紧急呼叫策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|紧急呼叫控制策略，可以根据需要选择0项、1项或多项。选择其中某项，表示打开该项开关，未选择则表示关闭。取值含义：SPFLAG：支持紧急呼叫，包括紧急附着和紧急PDN连接。SPNOCARDUSER：支持无卡用户紧急呼叫。ATTACHAUTH：当紧急附着时进行鉴权。PAUTHFAIL：鉴权失败时，如果有紧急承载，则保留紧急承载；如果是紧急附着，则继续进行附着处理。PLIMITUSER：有紧急承载或紧急附着时检查用户接入受限、移动性受限等原因受限时，保留紧急承载或继续执行紧急附着。ATTACHCHKIMEI：紧急附着检查IMEI。GETIMEIATCHK：紧急附着IMEI检查中是否重新向UE获取IMEI。PCHKIMEIFAIL：IMEI检查失败保留紧急承载或继续紧急附着。RELPDNCON：正常附着用户发起紧急PDN连接时是否释放非紧急PDN连接。RPTIMSI：无卡用户紧急附着时，信令跟踪与失败观察是否上报由IMEI构造的IMSI。
PRIORITY|紧急呼叫寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于在空闲态下对具有紧急承载的用户进行寻呼时使用的优先级。取值含义：空：不使用PRIORITY，不修改已有的配置。PRIO_0~PRIO_14：优先级别，PRIO_0优先级最高，PRIO_14优先级最低。PRIO_15：寻呼时不携带优先级。
命令举例 
控制策略级别最低的设置，允许有卡用户（鉴权失败、IMEI检查失败、受限制都没有关系）和无卡用户拨打紧急电话。无线寻呼的优先级为7级。 
SET EMERGENCYCFG:POLICY="SPFLAG"&"SPNOCARDUSER"&"ATTACHAUTH"&"PAUTHFAIL"&"PLIMITUSER"&"ATTACHCHKIMEI"&"PCHKIMEIFAIL"&"RELPDNCON"&"RPTIMSI",PRIORITY="PRIO_7"; 
父主题： [控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询紧急呼叫配置(SHOW EMERGENCYCFG) 
### 查询紧急呼叫配置(SHOW EMERGENCYCFG) 
命令功能 
该命令用于查询紧急呼叫控制信息。紧急呼叫控制根据用户类型、行为来决定是否允许用户使用紧急呼叫功能。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
POLICY|紧急呼叫策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|紧急呼叫控制策略，可以根据需要选择0项、1项或多项。选择其中某项，表示打开该项开关，未选择则表示关闭。取值含义：SPFLAG：支持紧急呼叫，包括紧急附着和紧急PDN连接。SPNOCARDUSER：支持无卡用户紧急呼叫。ATTACHAUTH：当紧急附着时进行鉴权。PAUTHFAIL：鉴权失败时，如果有紧急承载，则保留紧急承载；如果是紧急附着，则继续进行附着处理。PLIMITUSER：有紧急承载或紧急附着时检查用户接入受限、移动性受限等原因受限时，保留紧急承载或继续执行紧急附着。ATTACHCHKIMEI：紧急附着检查IMEI。GETIMEIATCHK：紧急附着IMEI检查中是否重新向UE获取IMEI。PCHKIMEIFAIL：IMEI检查失败保留紧急承载或继续紧急附着。RELPDNCON：正常附着用户发起紧急PDN连接时是否释放非紧急PDN连接。RPTIMSI：无卡用户紧急附着时，信令跟踪与失败观察是否上报由IMEI构造的IMSI。
PRIORITY|紧急呼叫寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于在空闲态下对具有紧急承载的用户进行寻呼时使用的优先级。取值含义：空：不使用PRIORITY，不修改已有的配置。PRIO_0~PRIO_14：优先级别，PRIO_0优先级最高，PRIO_14优先级最低。PRIO_15：寻呼时不携带优先级。
命令举例 
查询紧急呼叫控制开关配置。 
SHOW EMERGENCYCFG； 
`
命令 (No.1): SHOW EMERGENCYCFG
操作维护  紧急呼叫策略                                                                                                                                                                                                               紧急呼叫寻呼优先级
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      支持紧急呼叫 & 支持无卡用户紧急呼叫 & 紧急附着鉴权 & 鉴权失败放行紧急呼叫 & 受限用户放行紧急呼叫 & 紧急附着检查IMEI & 紧急附着IMEI检查中向UE获取IMEI & IMEI检查失败放行紧急呼叫 & 释放非紧急PDN连接 & 上报IMEI构造的IMSI   优先级7
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 紧急数据配置 
## 紧急数据配置 
背景知识 
UE终端拨打紧急呼叫时，会向MME发起紧急PDN连接请求，MME使用本地配置的APN（紧急呼叫专用APN，全网统一规划）、Qos和PGW标识来建立PDN连接。 
功能描述 
当MME支持紧急呼叫功能时，需对本模块配置。 
本模块配置紧急呼叫所使用承载相关信息，对于不同PLMN的用户可配置不同的承载信息，承载相关信息如下： 
 
APN，在未配置PGW标识时，使用此APN来获得指定PGW，此APN为全网统一规划，通过APN识别出当前承载被用于紧急呼叫。
 
 
紧急承载使用的QCI（QoS Class Identifier）。
 
 
紧急承载使用的AMBR（Aggregate Maximum Bit Rate）。
 
 
紧急承载使用的ARP（Allocation Retention Priority）。
 
 
PGW标识（PGW的FQDN域名或IP地址），MME向此PGW建立紧用承载。
 
 
相关主题 
 
新增紧急数据配置(ADD EMERGDATA)
 
 
修改紧急数据配置(SET EMERGDATA)
 
 
删除紧急数据配置(DEL EMERGDATA)
 
 
查询紧急数据配置(SHOW EMERGDATA)
 
 
父主题： [紧急呼叫配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增紧急数据配置(ADD EMERGDATA) 
### 新增紧急数据配置(ADD EMERGDATA) 
命令功能 
该命令用于增加某个PLMN的紧急数据配置。当需要启用紧急呼叫功能时，必须配置该PLMN相关的紧急呼叫数据，以便根据这些配置创建相应的紧急PDN连接和紧急承载，为用户提供紧急呼叫服务。
注意事项 
 
需要支持紧急呼叫功能，该配置才有效。使用命令SET EMERGENCYCFG，并选择POLICY参数中的“SPFLAG”选项。
 
 
开启紧急呼叫功能，必须配置紧急呼叫数据。MME使用该配置而非用户签约信息创建紧急PDN连接和紧急承载。若缺少该配置，则无法提供紧急呼叫服务。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|运营商提供的网络服务接入点名称。
APNAMBR4UL|上行APNAMBR|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|APN的上行AMBR。
APNAMBR4DL|下行APNAMBR|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|APN的下行AMBR。
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:5~9。|QCI值，表示服务质量类型。取值含义：5：IMS 信令。6：缓存播放的视频，基于TCP的网络应用，优先级为6，略高。7：语音，实时视频，互动游戏。8：缓存播放的视频，基于TCP的网络应用，优先级为8。9：缓存播放的视频，基于TCP的网络应用，优先级为9，较低。
PRIOLEVEL|呼叫优先级类别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|资源分配与保持优先级。级别从1至15，数值越小，级别越高，优先分配网络资源并享有优质的网络服务。
PC|是否可抢占其他呼叫|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|当资源受限时，是否可抢占其他呼叫的资源。取值含义：是（YES）：可以抢占其他呼叫。当无空闲网络资源分配时，可以中断其他允许被抢占的呼叫，将其资源留作本呼叫使用。否（NO）：不可以抢占其他呼叫。当无空闲网络资源分配时，本呼叫不能中断其他呼叫并占用其资源。
PV|是否允许被其他呼叫抢占|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|当资源受限时，是否允许被其他呼叫抢占资源。取值含义：是（YES）：允许被其他呼叫抢占。当无空闲网络资源分配时，允许中断本呼叫而将资源让与优先级更高的呼叫使用。否（NO）：不允许被其他呼叫抢占。当无空闲网络资源分配时，不允许中断本呼叫而将资源让与其他呼叫使用。
IPADDR|PGW IP地址|参数可选性:任选参数；参数类型:地址|PGW的IP地址，字符串，合法的IPv4或IPv6格式。例如：“192.168.1.1”或“201::3456:7890”。
FQDN|FQDN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于查找紧急呼叫连接的PGW的FQDN，以“.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”结尾的字符串，最大长度100。
SUP5GSIWK|支持与5G互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:not supported。|支持与5G互操作。取值如下：不支持支持根据UE能力默认"不支持"。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
为PLMN为460-01的网络增加紧急数据配置，紧急APN为emergency，该APN的上行AMBR为152kpbs，下行AMBR为1024kbps，使用QCI为5，优先级为14，具有抢占能力，不允许被抢占，使用FQDN为“zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org”查找PGW，并将该条配置取名为emergency1。 
ADD EMERGDATA:PLMN="460"-"01",APN="emergency",APNAMBR4UL="512 kbps",APNAMBR4DL="1024 kbps",QCI=5,PRIOLEVEL="PRIO14",PC="YES",PV="NO",FQDN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",NAME="emergency1"; 
父主题： [紧急数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改紧急数据配置(SET EMERGDATA) 
### 修改紧急数据配置(SET EMERGDATA) 
命令功能 
该命令用于修改某个PLMN的紧急数据配置。当需要启用紧急呼叫功能时，必须配置该PLMN相关的紧急呼叫数据配置，以便根据这些配置创建相应的紧急PDN连接和紧急承载，为用户提供紧急呼叫服务。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~61个字符。|运营商提供的网络服务接入点名称。
APNAMBR4UL|上行APNAMBR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|APN的上行AMBR。
APNAMBR4DL|下行APNAMBR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|APN的下行AMBR。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:5~9。|QCI值，表示服务质量类型。取值含义：5：IMS 信令。6：缓存播放的视频，基于TCP的网络应用，优先级为6，略高。7：语音，实时视频，互动游戏。8：缓存播放的视频，基于TCP的网络应用，优先级为8。9：缓存播放的视频，基于TCP的网络应用，优先级为9，较低。
PRIOLEVEL|呼叫优先级类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|资源分配与保持优先级。级别从1至15，数值越小，级别越高，优先分配网络资源并享有优质的网络服务。
PC|是否可抢占其他呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当资源受限时，是否可抢占其他呼叫的资源。取值含义：是（YES）：可以抢占其他呼叫。当无空闲网络资源分配时，可以中断其他允许被抢占的呼叫，将其资源留作本呼叫使用。否（NO）：不可以抢占其他呼叫。当无空闲网络资源分配时，本呼叫不能中断其他呼叫并占用其资源。
PV|是否允许被其他呼叫抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当资源受限时，是否允许被其他呼叫抢占资源。取值含义：是（YES）：允许被其他呼叫抢占。当无空闲网络资源分配时，允许中断本呼叫而将资源让与优先级更高的呼叫使用。否（NO）：不允许被其他呼叫抢占。当无空闲网络资源分配时，不允许中断本呼叫而将资源让与其他呼叫使用。
IPADDR|PGW IP地址|参数可选性:任选参数；参数类型:地址|PGW的IP地址，字符串，合法的IPv4或IPv6格式。例如：“192.168.1.1”或“201::3456:7890”。
FQDN|FQDN|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。|用于查找紧急呼叫连接的PGW的FQDN，以“.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”结尾的字符串，最大长度100。
SUP5GSIWK|支持与5G互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持与5G互操作。取值如下：不支持支持根据UE能力默认"不支持"。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
修改PLMN为460-01的网络紧急数据配置，修改APN为emc，APN的上行AMBR改为1024kbps，下行AMBR为2048kbps，使用IP地址为“1:2:3:4:5:6:7:8”查找PGW，本条配置该名为emc。 
SET EMERGDATA:PLMN="460"-"01",APN="emc",APNAMBR4UL="1024 kbps",APNAMBR4DL="2048 kbps",IPADDR="1:2:3:4:5:6:7:8",NAME="emc"; 
父主题： [紧急数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除紧急数据配置(DEL EMERGDATA) 
### 删除紧急数据配置(DEL EMERGDATA) 
命令功能 
该命令用于删除某个PLMN使用的紧急数据配置。删除紧急数据配置后，该PLMN将无法提供紧急呼叫服务。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
命令举例 
删除PLMN为460-01的网络紧急数据配置。 
DEL EMERGDATA:PLMN="460"-"01"; 
父主题： [紧急数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询紧急数据配置(SHOW EMERGDATA) 
### 查询紧急数据配置(SHOW EMERGDATA) 
命令功能 
该命令用于查询紧急数据配置，包括PLMN、APN、AMBR、QCI、PGW地址或FQDN等信息。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|运营商提供的网络服务接入点名称。
APNAMBR4UL|上行APNAMBR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|APN的上行AMBR。
APNAMBR4DL|下行APNAMBR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|APN的下行AMBR。
QCI|QCI|参数可选性:任选参数；参数类型:整数。|QCI值，表示服务质量类型。取值含义：5：IMS 信令。6：缓存播放的视频，基于TCP的网络应用，优先级为6，略高。7：语音，实时视频，互动游戏。8：缓存播放的视频，基于TCP的网络应用，优先级为8。9：缓存播放的视频，基于TCP的网络应用，优先级为9，较低。
PRIOLEVEL|呼叫优先级类别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|资源分配与保持优先级。级别从1至15，数值越小，级别越高，优先分配网络资源并享有优质的网络服务。
PC|是否可抢占其他呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当资源受限时，是否可抢占其他呼叫的资源。取值含义：是（YES）：可以抢占其他呼叫。当无空闲网络资源分配时，可以中断其他允许被抢占的呼叫，将其资源留作本呼叫使用。否（NO）：不可以抢占其他呼叫。当无空闲网络资源分配时，本呼叫不能中断其他呼叫并占用其资源。
PV|是否允许被其他呼叫抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当资源受限时，是否允许被其他呼叫抢占资源。取值含义：是（YES）：允许被其他呼叫抢占。当无空闲网络资源分配时，允许中断本呼叫而将资源让与优先级更高的呼叫使用。否（NO）：不允许被其他呼叫抢占。当无空闲网络资源分配时，不允许中断本呼叫而将资源让与其他呼叫使用。
IPADDR|PGW IP地址|参数可选性:任选参数；参数类型:地址|PGW的IP地址，字符串，合法的IPv4或IPv6格式。例如：“192.168.1.1”或“201::3456:7890”。
FQDN|FQDN|参数可选性:任选参数；参数类型:字符型。|用于查找紧急呼叫连接的PGW的FQDN，以“.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”结尾的字符串，最大长度100。
SUP5GSIWK|支持与5G互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持与5G互操作。取值如下：不支持支持根据UE能力默认"不支持"。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询所有PLMN网络的紧急数据配置。 
SHOW EMERGDATA; 
`
命令 (No.1): SHOW EMERGDATA
操作维护    PLMN     APN名称     上行APNAMBR             下行APNAMBR             QCI   呼叫优先级类别   是否可抢占其他呼叫   是否允许被其他呼叫抢占   PGW IP地址   FQDN                                            支持与5G互操作         用户别名
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改   460-01   emergency   512 千比特/秒 (120)     1024 千比特/秒 (135)    5     优先级14         可以抢占其他呼叫     不允许被其他呼叫抢占                  zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org   不支持                 emergency1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [紧急数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 紧急号码列表配置 
## 紧急号码列表配置 
背景知识 
在附着/TAU业务中，MME通知UE终端其当前所在TAI支持的紧急号码，以便UE在拨打呼叫时判断是否为紧急呼叫。在不同的TAI下，可能其紧急号码不同。 
功能描述 
本模块配置多组紧急号码列表，以紧急号码列表ID为标识。每组号码列表中包含多个号码（比如110报警号码、119火警号码）。 
                在跟踪区配置
                [ADD TA]
                /
                [SET TA]
                命令中，为TA选择其对应的紧急号码列表ID后，
在附着或TAU业务流程中，如MME支持紧急呼叫功能，则MME在ATTACH ACCEPT或TAU ACCEPT消息中将UE当前所在TAI对应的紧急号码列表发送给UE终端，UE基于此号码列表判断拨打的号码是否为紧急号码；当MME不支持紧急呼叫功能时，ATTACH ACCEPT或TAU ACCEPT消息不携带此紧急号码列表。
            
相关主题 
 
新增紧急号码列表(ADD EMERGNUMLIST)
 
 
修改紧急号码列表(SET EMERGNUMLIST)
 
 
删除紧急号码列表(DEL EMERGNUMLIST)
 
 
查询紧急号码列表(SHOW EMERGNUMLIST)
 
 
父主题： [紧急呼叫配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增紧急号码列表(ADD EMERGNUMLIST) 
### 新增紧急号码列表(ADD EMERGNUMLIST) 
命令功能 
该命令用于增加紧急号码列表中的紧急号码。当需要提供紧急呼叫功能时，使用该命令。在设置紧急呼叫列表并关联到相应的TA后，当用户从该TA成功接入后，会将相应的紧急号码列表发送给UE。 
注意事项 
 
当紧急号码长度较大时会减少实际携带的号码数量。由于号码长度不同，而协议中携带的数据大小有限，因此并不能保证10个号码都能携带给UE。一般情况下足够使用，10个6位数的紧急号码没有问题。
 
 
需要与用户接入的TA进行关联。在创建或修改TA时，命令ADD TA或者SET TA中可以设置该TA关联使用的紧急号码列表。其中参数ADD TA即该TA使用的紧急号码列表ID。
 
 
需要支持紧急呼叫功能，紧急号码才会携带给UE。使用命令SET EMERGENCYCFG，并选择SET EMERGENCYCFG中的“SPFLAG”选项。
 
 
 设置传表后生效，无需重启单板。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
LISTID|紧急号码列表ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~50。|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。
NUMBER|紧急号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~20个字符。|紧急呼叫对应的紧急号码，例如：110、119、120。
TYPE|紧急号码类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
向紧急呼叫列表1中，添加一个紧急号码911，属于警用、急救、火警、海事、山地救援的类型。 
ADD EMERGNUMLIST:LISTID=1,NUMBER="911",TYPE="PC"& "AMB"& "FIRE"& "MG"& "MR"; 
父主题： [紧急号码列表配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改紧急号码列表(SET EMERGNUMLIST) 
### 修改紧急号码列表(SET EMERGNUMLIST) 
命令功能 
该命令用于修改紧急号码列表中的紧急号码。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
LISTID|紧急号码列表ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~50。|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。
NUMBER|紧急号码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~20个字符。|紧急呼叫对应的紧急号码，例如：110、119、120。
TYPE|紧急号码类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
修改紧急呼叫列表1中的紧急号码911，它属于警用和火警类型。 
SET EMERGNUMLIST:LISTID=1,NUMBER="911",TYPE="PC"&"FIRE"; 
父主题： [紧急号码列表配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除紧急号码列表(DEL EMERGNUMLIST) 
### 删除紧急号码列表(DEL EMERGNUMLIST) 
命令功能 
该命令用于从紧急号码列表中删除一个紧急号码。删除该号码之后，UE不再将此号码作为紧急呼叫使用，可能只会按照普通电话的要求建立连接。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
LISTID|紧急号码列表ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~50。|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。
NUMBER|紧急号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~20个字符。|紧急呼叫对应的紧急号码，例如：110、119、120。
命令举例 
将紧急号码列表1中的紧急号码911删除。 
DEL EMERGNUMLIST:LISTID=1,NUMBER="911"; 
父主题： [紧急号码列表配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询紧急号码列表(SHOW EMERGNUMLIST) 
### 查询紧急号码列表(SHOW EMERGNUMLIST) 
命令功能 
该命令用于显示紧急号码列表的紧急号码及其类型。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
LISTID|紧急号码列表ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~50。|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。
NUMBER|紧急号码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~20个字符。|紧急呼叫对应的紧急号码，例如：110、119、120。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LISTID|紧急号码列表ID|参数可选性:任选参数；参数类型:整数。|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。
NUMBER|紧急号码|参数可选性:任选参数；参数类型:字符型。|紧急呼叫对应的紧急号码，例如：110、119、120。
TYPE|紧急号码类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
显示紧急号码及其类型。 
SHOW EMERGNUMLIST; 
`
命令 (No.1): SHOW EMERGNUMLIST
操作维护         紧急号码列表ID   紧急号码   紧急号码类型                               用户别名
------------------------------------------------------------------------------------------------
复制 修改 删除   1                911        报警 & 救护 & 火警 & 海洋救援 & 山地救援   
------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.063 秒）。
` 
父主题： [紧急号码列表配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于IMSI的紧急呼叫支持标识配置 
## 基于IMSI的紧急呼叫支持标识配置 
背景知识 
MME能够支持基于终端用户的IMSI号段，来区分不同的用户下发不同的紧急承载标识（即携带紧急承载标识给终端），即可以根据不同的用户，配置不同的紧急呼叫策略。 
功能描述 
基于IMSI的紧急呼叫支持标识配置包括以下内容： 
 
可以支持根据用户终端的IMSI号段来决定是否启用紧急呼叫功能和下发默认的紧急呼叫策略。
 
 
可以支持根据用户终端的IMSI号段配置不同的紧急呼叫策略。
 
 
相关主题 
 
基于IMSI的紧急呼叫支持标识开关配置
 
 
基于IMSI的紧急呼叫支持标识策略配置
 
 
父主题： [紧急呼叫配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于IMSI的紧急呼叫支持标识开关配置 
### 基于IMSI的紧急呼叫支持标识开关配置 
背景知识 
            
            能够支持基于IMSI号段下发紧急承载标识，在开关打开和配置下发策略的时候携带紧急承载标识给终端。
        
功能描述 
            
            用于配置IMSI号段下发紧急承载标识控制开关和默认下发策略。
        
相关主题 
 
设置基于IMSI的紧急呼叫支持标识开关(SET EMERGIMSI SWITCH)
 
 
查询基于IMSI的紧急呼叫支持标识开关(SHOW EMERGIMSI SWITCH)
 
 
父主题： [基于IMSI的紧急呼叫支持标识配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置基于IMSI的紧急呼叫支持标识开关(SET EMERGIMSI SWITCH) 
#### 设置基于IMSI的紧急呼叫支持标识开关(SET EMERGIMSI SWITCH) 
命令功能 
该命令用于设置基于IMSI的紧急承载标识开关和默认策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPEMCBS|是否基于MNC/MCC下发紧急呼叫支持标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于用户终端的IMSI号段，来为不同的用户下发紧急呼叫支持标识。
DFTEMCBSPLY|基于MNC/MCC下发紧急呼叫支持标识默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在基于用户终端的IMSI号码开启紧急呼叫功能的情况下， 为用户下发的紧急呼叫策略是否为默认策略。
命令举例 
设置基于IMSI的紧急呼叫支持标识开关，把是否基于MNC/MCC下发紧急呼叫支持标识设置为不支持，把基于MNC/MCC下发紧急呼叫支持标识默认策略设置为不下发。 
SET EMERGIMSI SWITCH:SUPEMCBS="NSUP",DFTEMCBSPLY="NCAR"; 
父主题： [基于IMSI的紧急呼叫支持标识开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于IMSI的紧急呼叫支持标识开关(SHOW EMERGIMSI SWITCH) 
#### 查询基于IMSI的紧急呼叫支持标识开关(SHOW EMERGIMSI SWITCH) 
命令功能 
该命令用于查询基于IMSI的紧急承载标识开关和默认策略。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPEMCBS|是否基于MNC/MCC下发紧急呼叫支持标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于用户终端的IMSI号段，来为不同的用户下发紧急呼叫支持标识。
DFTEMCBSPLY|基于MNC/MCC下发紧急呼叫支持标识默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在基于用户终端的IMSI号码开启紧急呼叫功能的情况下， 为用户下发的紧急呼叫策略是否为默认策略。
命令举例 
查询基于IMSI的紧急呼叫支持标识开关。 
SHOW EMERGIMSI SWITCH 
`
命令 (No.31): SHOW EMERGIMSI SWITCH:
-----------------NFS_MMESGSN_0----------------
是否基于MNC/MCC下发紧急呼叫支持标识 基于MNC/MCC下发紧急呼叫支持标识默认策略
不支持 下发
----------------------------------
记录数：1
执行成功（耗时 0.027 秒）。
` 
父主题： [基于IMSI的紧急呼叫支持标识开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于IMSI的紧急呼叫支持标识策略配置 
### 基于IMSI的紧急呼叫支持标识策略配置 
背景知识 
MME能够支持基于终端用户的IMSI号段，来区分不同的用户下发不同的紧急承载标识（即携带紧急承载标识给终端），即可以根据不同的用户，配置不同的紧急呼叫策略。 
功能描述 
操作员配置基于终端用户的IMSI号段的紧急呼叫支持标识为下发，则MME会下发紧急承载标识给UE，表示该此IMSI号段的用户支持紧急呼叫功能。 
相关主题 
 
新增基于IMSI的紧急呼叫支持标识策略(ADD EMERGIMSI)
 
 
修改基于IMSI的紧急呼叫支持标识策略(SET EMERGIMSI)
 
 
删除基于IMSI的紧急呼叫支持标识策略(DEL EMERGIMSI)
 
 
查询基于IMSI的紧急呼叫支持标识策略(SHOW EMERGIMSI)
 
 
父主题： [基于IMSI的紧急呼叫支持标识配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增基于IMSI的紧急呼叫支持标识策略(ADD EMERGIMSI) 
#### 新增基于IMSI的紧急呼叫支持标识策略(ADD EMERGIMSI) 
命令功能 
该命令用于新增基于IMSI的紧急支持标识策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置与终端相同MNC/MCC，可以下发紧急呼叫支持标识的IMSI号段。
EMCBSPLY|基于MNC/MCC下发紧急呼叫支持标识策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置根据IMSI号段是否下发紧急呼叫支持标识策略。
命令举例 
新增基于IMSI号段为123的紧急呼叫支持标识策略。 
ADD EMERGIMSI:IMSI="123",EMCBSPLY="CAR"; 
父主题： [基于IMSI的紧急呼叫支持标识策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改基于IMSI的紧急呼叫支持标识策略(SET EMERGIMSI) 
#### 修改基于IMSI的紧急呼叫支持标识策略(SET EMERGIMSI) 
命令功能 
该命令用于修改基于IMSI的紧急呼叫支持标识策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置与终端相同MNC/MCC，可以下发紧急呼叫支持标识的IMSI号段。
EMCBSPLY|基于MNC/MCC下发紧急呼叫支持标识策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置根据IMSI号段是否下发紧急呼叫支持标识策略。
命令举例 
把IMSI号段为123的记录修改为基于MNC/MCC不下发紧急呼叫支持标识策略。 
SET EMERGIMSI:IMSI="123",EMCBSPLY="NCAR"; 
父主题： [基于IMSI的紧急呼叫支持标识策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除基于IMSI的紧急呼叫支持标识策略(DEL EMERGIMSI) 
#### 删除基于IMSI的紧急呼叫支持标识策略(DEL EMERGIMSI) 
命令功能 
该命令用于删除基于IMSI的紧急呼叫支持标识策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置与终端相同MNC/MCC，可以下发紧急呼叫支持标识的IMSI号段。
命令举例 
删除基于IMSI号段为123的紧急呼叫支持标识策略。 
DEL EMERGIMSI:IMSI="123"; 
父主题： [基于IMSI的紧急呼叫支持标识策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于IMSI的紧急呼叫支持标识策略(SHOW EMERGIMSI) 
#### 查询基于IMSI的紧急呼叫支持标识策略(SHOW EMERGIMSI) 
命令功能 
该命令用于查询基于IMSI的紧急呼叫支持标识策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置与终端相同MNC/MCC，可以下发紧急呼叫支持标识的IMSI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置与终端相同MNC/MCC，可以下发紧急呼叫支持标识的IMSI号段。
EMCBSPLY|基于MNC/MCC下发紧急呼叫支持标识策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置根据IMSI号段是否下发紧急呼叫支持标识策略。
命令举例 
查询基于IMSI号段为123的紧急呼叫支持标识策略。 
SHOW EMERGIMSI:IMSI="123"; 
`
命令 (No.1): SHOW EMERGIMSI:IMSI="123";
操作维护         IMSI号段   基于MNC/MCC下发紧急呼叫支持标识策略
---------------------------------------------------------------
复制 修改 删除   123        不下发
---------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.024 秒）。
` 
父主题： [基于IMSI的紧急呼叫支持标识策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# ESMLC组标识配置 
# ESMLC组标识配置 
背景知识 
E-SMLC（Evolved Serving Mobile Location Centre，演进服务移动定位中心）实现用户当前位置的计算。ESMLC ID作为ESMLC的一个标识，由运营商统一规划。MME通过ESMLC ID进行路由的选择。 
功能描述 
ESMLC组标识配置用于设置ESMLC组编号以及该ESMLC组包含哪些ESMLC。用于根据GMLC选择ESMLC。当在MME GMLC配置中配置了GMLC名称和ESMLC组标识的对应关系后，则此GMLC的MT定位选择的ESMLC来自于该ESMLC组。 
相关主题 
 
新增ESMLC组标识(ADD ESMLCGRPID)
 
 
修改ESMLC组标识(SET ESMLCGRPID)
 
 
删除ESMLC组标识(DEL ESMLCGRPID)
 
 
查询ESMLC组标识(SHOW ESMLCGRPID)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增E-SMLC组标识(ADD ESMLCGRPID) 
## 新增E-SMLC组标识(ADD ESMLCGRPID) 
命令功能 
该命令用于配置E-SMLC组的编号，以及该E-SMLC组所包含的E-SMLC。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCGRPID|E-SMLC组标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~100。|用于配置E-SMLC组标识。
ESMLCID|E-SMLC标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|用于增加或者删除E-SMLC组标识中包含的E-SMLC。
命令举例 
新增E-SMLC组标识配置，E-SMLC组标识为1，E-SMLC标识为1&2。 
ADD ESMLCGRPID:ESMLCGRPID=1,ESMLCID=1&2; 
父主题： [ESMLC组标识配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改E-SMLC组标识(SET ESMLCGRPID) 
## 修改E-SMLC组标识(SET ESMLCGRPID) 
命令功能 
该命令用于修改E-SMLC组包含的E-SMLC标识，可以删除某些E-SMLC，或者增加某些E-SMLC。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCGRPID|E-SMLC组标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~100。|用于配置E-SMLC组标识。
ESMLCID|E-SMLC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于增加或者删除E-SMLC组标识中包含的E-SMLC。
命令举例 
修改E-SMLC组标识配置，E-SMLC组标识为1，E-SMLC标识为1&2。 
SET ESMLCGRPID:ESMLCGRPID=1,ESMLCID=1&2; 
父主题： [ESMLC组标识配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除E-SMLC组标识(DEL ESMLCGRPID) 
## 删除E-SMLC组标识(DEL ESMLCGRPID) 
命令功能 
该命令用于删除E-SMLC组编号以及包含的E-SMLC标识。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCGRPID|E-SMLC组标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~100。|用于配置E-SMLC组标识。
命令举例 
删除E-SMLC组标识配置，E-SMLC组标识为1。 
DEL ESMLCGRPID:ESMLCGRPID=1; 
父主题： [ESMLC组标识配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询E-SMLC组标识(SHOW ESMLCGRPID) 
## 查询E-SMLC组标识(SHOW ESMLCGRPID) 
命令功能 
该命令用于查询E-SMLC组编号以及包含的E-SMLC标识。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCGRPID|E-SMLC组标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|用于配置E-SMLC组标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCGRPID|E-SMLC组标识|参数可选性:任选参数；参数类型:整数。|用于配置E-SMLC组标识。
ESMLCID|E-SMLC标识|参数可选性:任选参数；参数类型:整数。|用于增加或者删除E-SMLC组标识中包含的E-SMLC。
命令举例 
查询E-SMLC组标识配置，E-SMLC组标识为1。 
SHOW ESMLCGRPID:ESMLCGRPID=1; 
`
命令 (No.166): SHOW ESMLCGRPID:ESMLCGRPID=1;
操作维护        ESMLC组标识   ESMLC标识 
----------------------------------------
复制 修改 删除  1             1 
复制 修改 删除  1             2 
----------------------------------------
记录数 2
命令执行成功（耗时 0.073 秒）。
` 
父主题： [ESMLC组标识配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME控制开关配置 
# MME控制开关配置 
背景知识 
LCS业务存在各种各样的类别，除了协议规定的业务外，还有各种定制的业务。针对不同的场景和要求，MME可以控制相应的功能，以提高高效优质的定位业务和服务。 
功能描述 
用于控制MME对于定位功能的支持能力。 
相关主题 
 
设置MME控制开关配置(SET MMECTL)
 
 
查询MME控制开关配置(SHOW MMECTL)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置MME控制开关配置(SET MMECTL) 
## 设置MME控制开关配置(SET MMECTL) 
命令功能 
该命令用于设置MME支持的功能的开关状态。当需要支持相应的功能时，需要打开对应的开关。当设置为支持时，MME支持相应功能，反之，MME则不支持。 
注意事项 
该命令设置为支持时，必须在相应的License打开后方能有效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPDEFERMTPOSI|节电态用户延迟定位|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于设置MME是否支持NB用户在节电态下的延迟定位。
SUPESMLCBYGMLC|基于GMLC选择E-SMLC|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于设置MME是否支持基于GMLC选择E-SMLC。
命令举例 
设置根据GMLC选择E-SMLC开关，设置MME是否支持用户在节电态下的延迟定位为“支持”，基于GMLC选择E-SMLC为“支持”。 
SET MMECTL:SUPDEFERMTPOSI="YES",SUPESMLCBYGMLC="YES"; 
父主题： [MME控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME控制开关配置(SHOW MMECTL) 
## 查询MME控制开关配置(SHOW MMECTL) 
命令功能 
该命令用于查询MME相应功能的支持情况。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPDEFERMTPOSI|节电态用户延迟定位|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于设置MME是否支持NB用户在节电态下的延迟定位。
SUPESMLCBYGMLC|基于GMLC选择E-SMLC|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于设置MME是否支持基于GMLC选择E-SMLC。
命令举例 
查询根据GMLC选择E-SMLC开关。 
SHOW MMECTL; 
`
命令 (No.11): SHOW MMECTL
操作维护 节电态用户延迟定位 基于GMLC选择E-SMLC 
-------------------------------------------------
修改  不支持    不支持 
-------------------------------------------------
记录数 1
命令执行成功（耗时 0.057 秒）。
` 
父主题： [MME控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME GMLC配置 
# MME GMLC配置 
背景知识 
GMLC（Gateway Mobile Location Center，网关移动位置中心）是外部位置程序访问PLMN的第一个结点，它执行注册授权检查和从HLR/HSS请求路由信息。根据协议和运营商的要求，MME能够识别GMLC，同时允许某些GMLC接入到MME执行定位。 
功能描述 
“MME GMLC配置”用于设置MME允许接入的GMLC主机名称。配置后，MME收到定位业务的MT请求时，判断GMLC名称是否在配置的列表中，如果在，则允许GMLC接入MME执行定位操作，否则，MME拒绝该GMLC接入。 
相关主题 
 
新增MME GMLC(ADD MME GMLC)
 
 
修改MME GMLC(SET MME GMLC)
 
 
删除MME GMLC(DEL MME GMLC)
 
 
查询MME GMLC(SHOW MME GMLC)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增MME GMLC(ADD MME GMLC) 
## 新增MME GMLC(ADD MME GMLC) 
命令功能 
该命令用于新增MME允许接入的GMLC。当运营商允许某个GMLC接入本网络时，需要在此配置GMLC名称。没有在该命令中配置的GMLC将不能接入MME。对于允许接入的GMLC，可以根据GMLC来选择对应的E-SMLC组号。 
最多可以配置100个GMLC。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GMLCNAME|GMLC名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于标识允许接入MME的GMLC名称，长度最多不超过128个字符。
ESMLCGRPID|E-SMLC组标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。默认值:0。|用于设置允许接入的GMLC对应的E-SMLC组号。
命令举例 
新增MME允许接入的GMLC，GMLC名称为“abc.com”。 
ADD MME GMLC:GMLCNAME="abc.com"; 
父主题： [MME GMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改MME GMLC(SET MME GMLC) 
## 修改MME GMLC(SET MME GMLC) 
命令功能 
该命令用于修改MME允许接入GMLC对应的E-SMLC组号。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GMLCNAME|GMLC名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于标识允许接入MME的GMLC名称，长度最多不超过128个字符。
ESMLCGRPID|E-SMLC组标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|用于设置允许接入的GMLC对应的E-SMLC组号。
命令举例 
修改MME允许接入的GMLC，GMLC名称为“abc.com”，ESML组标识为1。 
SET MME GMLC:GMLCNAME="abc.com",ESMLCGRPID=1; 
父主题： [MME GMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除MME GMLC(DEL MME GMLC) 
## 删除MME GMLC(DEL MME GMLC) 
命令功能 
该命令用于删除MME允许接入的GMLC。被删除的GMLC将不能接入MME并发起定位业务请求。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GMLCNAME|GMLC名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于标识允许接入MME的GMLC名称，长度最多不超过128个字符。
命令举例 
删除MME允许接入的GMLC，GMLC名称为“abc.com”。 
DEL MME GMLC:GMLCNAME="abc.com"; 
父主题： [MME GMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME GMLC(SHOW MME GMLC) 
## 查询MME GMLC(SHOW MME GMLC) 
命令功能 
该命令用于查询MME允许接入的GMLC，以及允许接入的GMLC对应的E-SMLC组号。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GMLCNAME|GMLC名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|该参数用于标识允许接入MME的GMLC名称，长度最多不超过128个字符。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GMLCNAME|GMLC名称|参数可选性:任选参数；参数类型:字符型。|该参数用于标识允许接入MME的GMLC名称，长度最多不超过128个字符。
ESMLCGRPID|E-SMLC组标识|参数可选性:任选参数；参数类型:整数。|用于设置允许接入的GMLC对应的E-SMLC组号。
命令举例 
查询MME允许接入的GMLC。 
SHOW MME GMLC; 
`
命令 (No.17): SHOW MME GMLC
操作维护        GMLC名称  E-SMLC组标识 
---------------------------------------
复制 修改 删除  abc.com   1 
复制 修改 删除  def.com   0 
---------------------------------------
记录数 2
命令执行成功（耗时 0.037 秒）。
` 
父主题： [MME GMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 支持定制CLR的HSS列表 
# 支持定制CLR的HSS列表 
背景知识 
具有2G/3G/4G能力的UE，从LTE回落到2G/3G，UE给 SGSN发送RAU Request消息时，会携带Old RA。SGSN根据Old RA查找Old MME，然后向Old MME发送SGSN Context Request消息，请求UE的移动性管理上下文和承载上下文。Old MME在收到SGSN Context Request消息后，给SGSN返回SGSN Context Response消息，之后Old MME删除承载上下文，并通知SGW和PGW删除承载上下文。 
具体可以参考3GPP TS 23.401 D.3.5。 
然而，某些LTE终端没有按照协议实现，从LTE回落到2G/3G，给SGSN发送RAU Request消息时，没有携带old RA，导致SGSN无法查找Old MME，无法给Old MME发送SGSN Context Request消息。Old MME感知不到UE已经移动到2G/3G，无法删除承载上下文，也不会通知SGW和PGW删除承载上下文。 
为了解决上述问题，ZXUN HSS和ZXUN MME提供以下策略： 
UE从LTE回落到2G/3G，给SGSN发送RAU Request消息时，SGSN发送更新消息给HSS。ZXUN HSS收到消息后，给ZXUN MME发送定制的CLR（Cancel Location Request，取消位置请求）消息，取消类型为“初始附着”，ZXUN MME收到定制的CLR消息后，删除UE的承载上下文，同时通知SGW和PGW删除承载上下文。 
功能描述 
MME支持定制的CLR功能，需要在本端配置“支持定制CLR的HSS列表”。配置后，MME收到列表中的HSS发来的取消类型为“Initial-Attach-Indicator”的CLR消息后，MME删除用户的承载上下文（Bearer Context），同时通知SGW和PGW删除承载上下文。 
注意： 
MME支持定制的CLR功能，同时需要HSS也支持。 
相关主题 
 
新增支持定制CLR的HSS列表(ADD HSS CUSTOMIZED CLR)
 
 
删除支持定制CLR的HSS列表(DEL HSS CUSTOMIZED CLR)
 
 
查询支持定制CLR的HSS列表(SHOW HSS CUSTOMIZED CLR)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增支持定制CLR的HSS列表(ADD HSS CUSTOMIZED CLR) 
## 新增支持定制CLR的HSS列表(ADD HSS CUSTOMIZED CLR) 
命令功能 
新增支持定制CLR的HSS列表。 
该命令用于MME网元新增向本网元发送定制的Cancel Location Request消息的HSS配置。 
当UE移动到3G网络时，路由更新消息携带的RAI无效时，老的MME感知不到UE已经附着到3G网络。此时，需要HSS向老的MME局发送Cancel Location Request消息，需要配置特定的HSS时，使用该命令进行配置。 
该命令执行成功后，MME网元如果收到该HSS发送的Cancel Location 消息时将会进行特殊处理。 
注意事项 
当UE跨RAT RAU到SGSN后，在异常情况下，MME没有收到局间SGSN Context Request消息时，MME定制的HSS能发送一条Cancel Location Request消息给MME，使MME能够感知到UE已经移动到SGSN网络，从而释放LTE承载资源。 
参数说明 
标识|名称|类型|说明
---|---|---|---
HOSTNAME|HSS主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|定制该功能的HSS的主机名。
REALM|HSS域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|定制该功能的HSS的域名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数这里唯一标识了一个本端网元的定制HSS，用户可以方便地使用别名进行查询或者删除操作。
命令举例 
新增主机名为“hss26.zte.com.cn”、域名为“zte.com.cn”的HSS，作为MME的定制CLR消息的HSS，并设置别名为hss26。 
ADD HSS CUSTOMIZED CLR:HOSTNAME="hss26.zte.com.cn",REALM="zte.com.cn",NAME="hss26";
 
父主题： [支持定制CLR的HSS列表]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除支持定制CLR的HSS列表(DEL HSS CUSTOMIZED CLR) 
## 删除支持定制CLR的HSS列表(DEL HSS CUSTOMIZED CLR) 
命令功能 
删除支持定制CLR的HSS列表。 
该命令用于MME网元删除向本网元发送定制的Cancel Location Request消息的HSS配置。 
该命令执行成功后，MME网元如果收到该HSS发送的Cancel Location 消息时将不会特殊处理。 
注意事项 
删除某个定制CLR的HSS配置时，必须同时输入HSS的主机名和HSS的域名。 
参数说明 
标识|名称|类型|说明
---|---|---|---
HOSTNAME|HSS主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|定制该功能的HSS的主机名。
REALM|HSS域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|定制该功能的HSS的域名。
命令举例 
删除主机名为“hss26.zte.com.cn”、域名为“zte.com.cn”的HSS，不再作为MME的定制CLR消息的HSS。 
DEL HSS CUSTOMIZED CLR:HOSTNAME="hss26.zte.com.cn",REALM="zte.com.cn";
 
父主题： [支持定制CLR的HSS列表]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询支持定制CLR的HSS列表(SHOW HSS CUSTOMIZED CLR) 
## 查询支持定制CLR的HSS列表(SHOW HSS CUSTOMIZED CLR) 
命令功能 
查询支持定制CLR的HSS列表。 
该命令用于MME网元查询向本网元发送定制Cancel Location Request消息的HSS配置。 
该命令成功后，将查询出指定的域名或者主机名关联的HSS列表。默认不输入任何参数，可以查询到该MME网元所有定制的HSS。 
注意事项 
查询MME的所有定制CLR消息的HSS。可以输入HSS的主机名或者域名，表示指定查询该主机名或者域名是否为MME的定制HSS，也可以输入定制HSS记录的别名进行查询。 
参数说明 
标识|名称|类型|说明
---|---|---|---
HOSTNAME|HSS主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|定制该功能的HSS的主机名。
REALM|HSS域名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~128个字符。|定制该功能的HSS的域名。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
HOSTNAME|HSS主机名|参数可选性:任选参数；参数类型:字符型。|定制该功能的HSS的主机名。
REALM|HSS域名|参数可选性:任选参数；参数类型:字符型。|定制该功能的HSS的域名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数这里唯一标识了一个本端网元的定制HSS，用户可以方便地使用别名进行查询或者删除操作。
命令举例 
查询主机名为“hss26.zte.com.cn”、域名为“zte.com.cn”的HSS是否作为MME的定制CLR消息的HSS。 
SHOW HSS CUSTOMIZED CLR:HOSTNAME="hss26.zte.com.cn",REALM="zte.com.cn";
 
`
命令 (No.1): SHOW HSS CUSTOMIZED CLR:HOSTNAME="hss26.zte.com.cn",REALM="zte.com.cn";
操作维护    HSS主机名          HSS域名      用户别名
----------------------------------------------------
复制 删除   hss26.zte.com.cn   zte.com.cn   hss26
----------------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [支持定制CLR的HSS列表]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# Relay配置 
# Relay配置 
背景知识 
中继技术（Relay）作为LTE-Advanced系统的关键技术，它为小区带来更大的覆盖范围和系统容量。 
所谓中继技术，就是在下行方向，基站发给UE的信号不直接发给UE，而是先发给一个中继站，然后再由中继转发给UE；在上行方向，UE的上行信号也不直接发给基站，而是先发给一个中继站，然后再由中继站转发给基站。 
功能描述 
            
            中继的主要作用是扩大小区的覆盖面积和提高系统容量。Relay可以为小区中阴影衰落严重的地区以及通信信号覆盖死角提供服务信号，同时如果中继站放置在原有小区覆盖范围内，如一些热点地区和室内也可以起到提高系统容量的作用。
        
相关主题 
 
Relay控制开关配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## Relay控制开关配置 
## Relay控制开关配置 
背景知识 
中继技术（Relay）作为LTE-Advanced系统的关键技术，它为小区带来更大的覆盖范围和系统容量。 
所谓中继技术，就是在下行方向，基站发给UE的信号不直接发给UE，而是先发给一个中继站，然后再由中继转发给UE；在上行方向，UE的上行信号也不直接发给基站，而是先发给一个中继站，然后再由中继站转发给基站。 
功能描述 
Relay功能需要HSS和eNodeB配合实现，在运营商购买了Relay功能License情况下，其配置规则如下： 
 
当HSS和eNodeB都不支持Relay功能时，在MME中不打开Relay功能开关。
 
 
                        当HSS和eNodeB都支持Relay功能时，在MME中打开Relay功能开关，参见命令
                        SET RELAYCFG
                        。
                    
 
 
                        当eNodeB支持但是HSS不支持Relay功能时，而网络又需要Relay时，则在MME中开启Relay开关和本地控制开关，参见命令
                        SET RELAYCFG
                        。
                    
 
 
                        MME上Relay功能开关打开的情况下，运营商不期望对Relay节点PDN连接请求中的APN进行检查，则打开旁路APN检查工作开关，参见命令
                        SET RELAYCFG
                        。
                    
 
 
相关主题 
 
设置Relay控制开关(SET RELAYCFG)
 
 
查询Relay控制开关(SHOW RELAYCFG)
 
 
父主题： [Relay配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置Relay控制开关(SET RELAYCFG) 
### 设置Relay控制开关(SET RELAYCFG) 
命令功能 
本命令实现以下三种开关的设置： 
 
Relay功能开关：控制MME是否具有Relay节点管理能力。
 
 
本地控制Relay开关：控制MME是否不依赖HSS进行Relay节点管理。
 
 
旁路APN检查过程开关：控制MME是否对Relay节点的APN进行检查处理。
 
 
当运营商购买了Relay功能License时，各开关的配置规则如下：  
 
当HSS和eNodeB都不支持Relay功能时，在MME中不打开Relay功能开关。
 
 
当HSS和eNodeB都支持Relay功能时，在MME中打开Relay功能开关。
 
 
当eNodeB支持但是HSS不支持Relay功能时，而网络又需要Relay时，则在MME中开启Relay开关和本地控制开关。
 
 
MME上Relay功能开关打开的情况下，运营商不期望对Relay节点PDN连接请求中的APN进行检查，则打开旁路APN相关功能。
 
 
注意事项 
旁路APN检查过程开关打开时，MME不会对Relay节点的PDN连接请求进行APN更正、转换及Type检查等，避免因为Relay节点的APN不规范而附着失败。
参数说明 
标识|名称|类型|说明
---|---|---|---
RELAY|Relay控制开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Relay控制开关实现以下功能开关的设置：Relay功能开关：控制MME是否具有Relay节点管理能力。本地控制Relay开关：控制MME是否不依赖HSS进行Relay节点管理。旁路APN检查过程开关：控制MME是否对Relay节点的APN进行检查处理。
命令举例 
打开Relay功能开关。 
SET RELAYCFG:RELAY="SUPPORT_RELAY"; 
父主题： [Relay控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询Relay控制开关(SHOW RELAYCFG) 
### 查询Relay控制开关(SHOW RELAYCFG) 
命令功能 
查询Relay的功能开关、本地控制开关和旁路APN检查开关的状态。
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RELAY|Relay控制开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Relay控制开关实现以下功能开关的设置：Relay功能开关：控制MME是否具有Relay节点管理能力。本地控制Relay开关：控制MME是否不依赖HSS进行Relay节点管理。旁路APN检查过程开关：控制MME是否对Relay节点的APN进行检查处理。
命令举例 
查询Relay控制开关的设置状态。 
`
命令 (No.16): SHOW RELAYCFG
操作维护  Relay控制开关
-----------------------
修改      支持本地控制Relay
-----------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [Relay控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# LIPA配置 
# LIPA配置 
背景知识 
LIPA（Local IP Access，本地IP接入）技术最初是基于家庭基站（HeNB）网络提出的，其含义是用户的业务流数据直接从家庭基站接入到本地PDN网络，不经过运营商的PGW接入EPC网络，相对于运营商的EPC网络来说，这部分业务数据流直接从家庭基站分流出去了，从而减轻了EPC网络的负荷也降低了EPC网络的传输成本。 
功能描述 
当MME与不支持LIPA签约数据的HSS对接时，如果运营商需要MME为其APN没有签约LIPA属性的用户提供本地IP接入，则MME启用本地LIPA配置。LIPA配置提供本局LIPA控制策略和APN的LIPA属性配置。 
配置LIPA功能的流程如下： 
 
                        配置本局LIPA控制策略。配置命令为：
                        SET LOCAL LIPA CTRL
 
 
                        配置APN的LIPA属性。配置命令为：
                        ADD APN LIPA ATTR
 
 
相关主题 
 
本局LIPA控制策略配置
 
 
APN的LIPA属性配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 本局LIPA控制策略配置 
## 本局LIPA控制策略配置 
背景知识 
LIPA（Local IP Access，本地IP接入）技术最初是基于家庭基站（HeNB）网络提出的，其含义是用户的业务流数据直接从家庭基站接入到本地PDN网络，不经过运营商的PGW接入EPC网络，相对于运营商的EPC网络来说，这部分业务数据流直接从家庭基站分流出去了，从而减轻了EPC网络的负荷也降低了EPC网络的传输成本。 
功能描述 
当MME与不支持LIPA签约数据的HSS对接时，如果运营商需要MME为其APN没有签约LIPA属性的用户提供本地IP接入，则MME启用本局LIPA控制策略。本局LIPA控制策略包括： 
 
是否使用本局配置的LIPA属性。
 
 
漫游用户是否开启LIPA功能。
 
 
在切换中MME是否支持发起LIPA PDN去连接。
 
 
相关主题 
 
设置本局LIPA控制策略配置(SET LOCAL LIPA CTRL)
 
 
查询本局LIPA控制策略配置(SHOW LOCAL LIPA CTRL)
 
 
父主题： [LIPA配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置本局LIPA控制策略配置(SET LOCAL LIPA CTRL) 
### 设置本局LIPA控制策略配置(SET LOCAL LIPA CTRL) 
命令功能 
该命令用于设置本局LIPA控制策略。当MME与不支持LIPA签约数据的HSS对接时，如果运营商需要MME为其APN没有签约LIPA属性的用户提供本地IP接入，则需要MME开启本局LIPA属性配置时，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
LIPACTL|LIPA控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局LIPA控制策略，包含3个选项：使用本局配置的LIPA属性：MME与不支持LIPA签约数据的HSS对接时，MME要提供LIPA接入，此时开启使用本局配置的LIPA属性。开启使用本局配置的LIPA属性的条件下，本地用户即可使用本局“APN的LIPA属性配置”。若勾选该选项，则MME从本局配置获取LIPA属性；若不勾选该选项，则MME从HSS上获取签约的LIPA属性。漫游用户开启LIPA功能：开启使用本局配置的LIPA属性的条件下，漫游用户要使用本局“APN的LIPA属性配置”，必须开启此配置。若勾选该选项，则漫游用户从本局配置获取LIPA属性；若不勾选该选项，则漫游用户从HSS上获取签约的LIPA属性。在切换中MME支持发起LIPA PDN去连接：对于存在LIPA PDN连接的切换，eNodeB在发起切换前，先通过内部信令通知合设的L-GW（Local Gateway，本地网关）发起LIPA PDN去连接，连接释放后再通知MME进行切换。如果L-GW在切换前没有释放LIPA PDN连接，MME收到切换请求时，检查到存在LIPA PDN连接，若勾选该选项，则MME可以先发起LIPA PDN去连接，然后进行切换；若不勾选该选项，则切换失败。
命令举例 
设置LIPA控制策略为使用本局配置的LIPA属性。 
SET LOCAL LIPA CTRL:LIPACTL="LOCAL"; 
父主题： [本局LIPA控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询本局LIPA控制策略配置(SHOW LOCAL LIPA CTRL) 
### 查询本局LIPA控制策略配置(SHOW LOCAL LIPA CTRL) 
命令功能 
该命令用于查询本局LIPA控制策略配置，查询内容包括：是否使用本局配置的LIPA属性、漫游用户是否开启LIPA功能和在切换中MME是否支持发起LIPA PDN去连接 。 
注意事项 
无 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LIPACTL|LIPA控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局LIPA控制策略，包含3个选项：使用本局配置的LIPA属性：MME与不支持LIPA签约数据的HSS对接时，MME要提供LIPA接入，此时开启使用本局配置的LIPA属性。开启使用本局配置的LIPA属性的条件下，本地用户即可使用本局“APN的LIPA属性配置”。若勾选该选项，则MME从本局配置获取LIPA属性；若不勾选该选项，则MME从HSS上获取签约的LIPA属性。漫游用户开启LIPA功能：开启使用本局配置的LIPA属性的条件下，漫游用户要使用本局“APN的LIPA属性配置”，必须开启此配置。若勾选该选项，则漫游用户从本局配置获取LIPA属性；若不勾选该选项，则漫游用户从HSS上获取签约的LIPA属性。在切换中MME支持发起LIPA PDN去连接：对于存在LIPA PDN连接的切换，eNodeB在发起切换前，先通过内部信令通知合设的L-GW（Local Gateway，本地网关）发起LIPA PDN去连接，连接释放后再通知MME进行切换。如果L-GW在切换前没有释放LIPA PDN连接，MME收到切换请求时，检查到存在LIPA PDN连接，若勾选该选项，则MME可以先发起LIPA PDN去连接，然后进行切换；若不勾选该选项，则切换失败。
命令举例 
查询本局LIPA控制策略配置。 
SHOW LOCAL LIPA CTRL 
`
命令 (No.31): SHOW LOCAL LIPA CTRL
操作维护 LIPA控制策略 
----------------------------------
修改      使用本局配置的LIPA属性 
----------------------------------
记录数 1
命令执行成功（耗时 0.027 秒）。
` 
父主题： [本局LIPA控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## APN的LIPA属性配置 
## APN的LIPA属性配置 
背景知识 
3GPP TS 29.272协议上对APN的LIPA属性字段“LIPA-Permission”的定义： 
 
LIPA_PROHIBITED (0)：LIPA禁止，指示该APN禁止LIPA接入。
 
 
LIPA_ONLY (1)：LIPA签约，指示该APN只允许LIPA接入。
 
 
LIPA_CONDITIONAL (2)：LIPA条件签约，指示该APN允许非LIPA接入也允许LIPA接入。LIPA条件签约情况下，如果无线侧支持LIPA，则MME对用户进行LIPA接入；如果无线侧不支持LIPA，则MME通过PGW将用户接入EPC网络。
 
 
功能描述 
当MME与不支持LIPA签约数据的HSS对接时，如果运营商需要MME为其APN没有签约LIPA属性的用户提供本地IP接入，则MME要启用本局LIPA控制策略，使用APN的LIPA属性配置。 
相关主题 
 
新增APN的LIPA属性配置(ADD APN LIPA ATTR)
 
 
修改APN的LIPA属性配置(SET APN LIPA ATTR)
 
 
删除APN的LIPA属性配置(DEL APN LIPA ATTR)
 
 
查询APN的LIPA属性配置(SHOW APN LIPA ATTR)
 
 
父主题： [LIPA配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增APN的LIPA属性配置(ADD APN LIPA ATTR) 
### 新增APN的LIPA属性配置(ADD APN LIPA ATTR) 
命令功能 
该命令用于增加APN对应的LIPA属性配置。当MME与不支持LIPA签约数据的HSS对接时，如果运营商需要MME为其APN没有签约LIPA属性的用户提供本地IP接入，则需要本地配置APN对应的LIPA属性时，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
LIPAATTR|LIPA属性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PROHIBITED。|该参数用于设置本局对该APN的LIPA控制策略，取值含义：0：LIPA禁止。1：LIPA签约。2：LIPA条件签约。
命令举例 
新增APN的LIPA属性配置，其中APN名称zte，LIPA属性为LIPA签约。 
ADD APN LIPA ATTR:APN="zte",LIPAATTR="ONLY"; 
父主题： [APN的LIPA属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改APN的LIPA属性配置(SET APN LIPA ATTR) 
### 修改APN的LIPA属性配置(SET APN LIPA ATTR) 
命令功能 
该命令用于修改APN对应的LIPA属性配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
LIPAATTR|LIPA属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局对该APN的LIPA控制策略，取值含义：0：LIPA禁止。1：LIPA签约。2：LIPA条件签约。
命令举例 
修改APN名称为zte的LIPA属性配置，将该APN的LIPA属性修改为LIPA条件签约。 
SET APN LIPA ATTR:APN="zte",LIPAATTR="CONDITIONAL"; 
父主题： [APN的LIPA属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除APN的LIPA属性配置(DEL APN LIPA ATTR) 
### 删除APN的LIPA属性配置(DEL APN LIPA ATTR) 
命令功能 
该命令用于删除APN对应的LIPA属性配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
命令举例 
删除APN名称为zte的LIPA属性配置。 
DEL APN LIPA ATTR:APN="zte"; 
父主题： [APN的LIPA属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询APN的LIPA属性配置(SHOW APN LIPA ATTR) 
### 查询APN的LIPA属性配置(SHOW APN LIPA ATTR) 
命令功能 
该命令用于查询APN对应的LIPA属性配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型。|APN名称由Network Identifier（NI）组成，格式为“Label1.Label2.Label3”，可包含多个标签并且必须符合如下要求。不超过61个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
LIPAATTR|LIPA属性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局对该APN的LIPA控制策略，取值含义：0：LIPA禁止。1：LIPA签约。2：LIPA条件签约。
命令举例 
查询所有APN的LIPA属性配置。 
SHOW APN LIPA ATTR; 
`
命令 (No.34): SHOW APN LIPA ATTR
操作维护       APN名称  LIPA属性 
-----------------------------------------
复制 修改 删除    zte      LIPA条件签约 
-----------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [APN的LIPA属性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 缺省SRVCC增强MSC Server配置 
# 缺省SRVCC增强MSC Server配置 
背景知识 
LTE网络建设初期，其覆盖范围有限，当用户在使用LTE网络进行语音通话过程中，移动到LTE信号较弱，但GERAN/UTRAN网络信号覆盖较好的区域时，为了保证语音呼叫连续性（Voice Call Continuity，VCC），需要将话路由LTE切换到GERAN/UTRAN。目前能够在LTE和GERAN/UTRAN同时附着并收发数据的终端较少，LTE和2G/3G之间的业务连续性都基于Single Radio模式，即双模单待方式。3GPP TS 23.216 R9中提出了双模单待无线语音呼叫连续性（Single Radio Voice Call Continuity，SRVCC）技术。 
SVRCC业务流程中，MME通过以下过程获取MSC Server地址。 
1、通过eNodeB发送MME的切换请求消息（Handover Required）中携带的Target ID来构造FQDN（Fully Qualified Domain Name），通过解析FQDN查询到MSC Server的地址。 
2、如果FQDN解析失败，通过MME上配置的缺省MSC Server地址，完成SRVCC业务。 
功能描述 
“缺省SRVCC增强MSC Server配置”可以按PLMN进行缺省MSC Server配置，也可以不区分PLMN配置全局缺省的MSC Server。 
UE发起SRVCC切换时，MME首先根据UE的IMSI中归属PLMN信息查询基于PLMN的缺省MSC Server配置；如果没匹配到，再选择全局缺省的MSC Server配置。 
缺省MSC Server功能只有SRVCC业务需要使用，使用缺省MSC Server功能需要同时打开该功能的软参开关。同时，使用SRVCC功能需要打开SRVCC的License开关 
相关主题 
 
全局缺省SRVCC增强MSC Server配置
 
 
基于PLMN的缺省SRVCC增强MSC Server配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 全局缺省SRVCC增强MSC Server配置 
## 全局缺省SRVCC增强MSC Server配置 
背景知识 
SVRCC业务流程中，MME通过以下过程获取SRVCC增强MSC Server地址。 
通过eNodeB发送MME的切换请求消息（Handover Required）中携带的Target ID来构造FQDN（Fully Qualified Domain Name），通过解析FQDN查询到MSC Server的地址。 
如果FQDN解析失败，通过MME上配置的缺省MSC Server地址，完成SRVCC业务。 
功能描述 
“全局缺省SRVCC增强MSC Server配置”可以不区分PLMN配置全局缺省的MSC Server地址。 
在不需要区分PLMN，或者对应的PLMN没有配置缺省MSC Server的情况下，使用全局缺省MSC Server配置。 
相关主题 
 
设置全局缺省SRVCC增强MSC Server配置(SET GLOBAL DFTMSCS)
 
 
查询全局缺省SRVCC增强MSC Server配置(SHOW GLOBAL DFTMSCS)
 
 
删除全局缺省SRVCC增强MSC Server配置(DEL GLOBAL DFTMSCS)
 
 
父主题： [缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置全局缺省SRVCC增强MSC Server配置(SET GLOBAL DFTMSCS) 
### 设置全局缺省SRVCC增强MSC Server配置(SET GLOBAL DFTMSCS) 
命令功能 
该命令用于设置全局缺省MSC Server地址信息。 
MME本地配置的缺省MSC Server分为两种类型： 
基于PLMN的缺省MSC Server和全局缺省MSC Server。 
如果MME无法获取某个PLMN对应的缺省MSC Server的IP地址，则使用全局缺省MSC Server。 
注意事项 
该功能只适用于MME。 
该命令生效需要设置系统软参“MME支持系统缺省MSC Server”，对应的系统软参为有效。 配置命令为： [SET SOFTWARE PARAMETER]: PARAID=65642,PARAVALUE=1;
参数说明 
标识|名称|类型|说明
---|---|---|---
MSCSIP|缺省MSC Server地址|参数可选性:任选参数；参数类型:地址|表示全局缺省的MSC Server IP地址，包括IPv4或者IPv6地址。维护人员根据实际的IP地址个数配置，系统支持一个PLMN最多配置10个地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。
命令举例 
假设SRVCC业务中，MME通过eNode B发送的切换请求消息中携带的Target ID来构造域名解析UE的MSC Server enhanced for SRVCC的地址失败，则使用用户别名为"msc server"的全局缺省MSC Server， 地址为“129.0.0.1”。
SET GLOBAL DFTMSCS:MSCSIP="129.0.0.1",NAME="msc server"; 
父主题： [全局缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询全局缺省SRVCC增强MSC Server配置(SHOW GLOBAL DFTMSCS) 
### 查询全局缺省SRVCC增强MSC Server配置(SHOW GLOBAL DFTMSCS) 
命令功能 
该命令用于查询全局缺省MSC Server配置。 
该查询不需要输入任何参数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR1|缺省MSC Server地址1|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR2|缺省MSC Server地址2|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR3|缺省MSC Server地址3|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR4|缺省MSC Server地址4|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR5|缺省MSC Server地址5|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR6|缺省MSC Server地址6|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR7|缺省MSC Server地址7|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR8|缺省MSC Server地址8|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR9|缺省MSC Server地址9|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
IPADDR10|缺省MSC Server地址10|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址，用户根据实际的IP地址个数配置，系统按照添加配置先后顺序生成各IP地址，最多支持16个地址，可配置小于等于10的任意个IP地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。
命令举例 
查询SRVCC业务中，MME通过eNode B发送的切换请求消息中携带的Target ID来构造域名解析UE的MSC Server enhanced for SRVCC的地址失败时，使用的全局缺省MSC Server地址信息。
SHOW GLOBAL DFTMSCS; 
`
命令 (No.1): SHOW GLOBAL DFTMSCS
操作维护    缺省MSC Server地址1   缺省MSC Server地址2   缺省MSC Server地址3   缺省MSC Server地址4   缺省MSC Server地址5   缺省MSC Server地址6   缺省MSC Server地址7   缺省MSC Server地址8   缺省MSC Server地址9   缺省MSC Server地址10   用户别名
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改 删除   10.43.146.7           0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0                msc server
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.053 秒）。
` 
父主题： [全局缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除全局缺省SRVCC增强MSC Server配置(DEL GLOBAL DFTMSCS) 
### 删除全局缺省SRVCC增强MSC Server配置(DEL GLOBAL DFTMSCS) 
命令功能 
删除全局缺省SRVCC增强MSC Server配置
注意事项 
无。 
命令举例 
删除全局缺省MSC Server地址信息。
DEL GLOBAL DFTMSCS; 
父主题： [全局缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于PLMN的缺省SRVCC增强MSC Server配置 
## 基于PLMN的缺省SRVCC增强MSC Server配置 
背景知识 
SVRCC业务流程中，MME通过以下过程获取SRVCC增强MSC Server地址。 
通过eNodeB发送MME的切换请求消息（Handover Required）中携带的Target ID来构造FQDN（Fully Qualified Domain Name），通过解析FQDN查询到MSC Server的地址。 
如果FQDN解析失败，通过MME上配置的缺省MSC Server地址，完成SRVCC业务。 
功能描述 
“基于PLMN的缺省SRVCC增强MSC Server配置”可以按PLMN进行缺省MSC Server的IP地址配置，为不同的PLMN配置不同的缺省MSC Server地址。 
可以针对特定的漫游用户的PLMN，配置特定的缺省MSC Server；如果不配置，则使用全局缺省MSC Server配置。 
相关主题 
 
增加MSC Server IP地址(ADD PLMN DFTMSCS IP)
 
 
删除MSC Server IP地址(DEL PLMN DFTMSCS IP)
 
 
新增基于PLMN的缺省SRVCC增强MSC Server配置(ADD PLMN DFTMSCS)
 
 
修改基于PLMN的缺省SRVCC增强MSC Server配置(SET PLMN DFTMSCS)
 
 
删除基于PLMN的缺省SRVCC增强MSC Server配置(DEL PLMN DFTMSCS)
 
 
查询基于PLMN的缺省SRVCC增强MSC Server配置(SHOW PLMN DFTMSCS)
 
 
父主题： [缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 增加MSC Server IP地址(ADD PLMN DFTMSCS IP) 
### 增加MSC Server IP地址(ADD PLMN DFTMSCS IP) 
命令功能 
该命令用于根据RNC或者BSC所属的PLMN增加单个缺省MSC Server IP地址。 
执行该命令前，需要通过[ADD PLMN DFTMSCS]已经执行过设置基于指定PLMN的缺省MSC Server配置。如果后续还要为指定的PLMN增加对应的MSC Server，则需要通过此条命令配置。
该命令执行后，会将新增的MSC Server IP地址添加到该指定PLMN原来已有的地址IP列表中，如果原有地址数目已经达到10个，将无法新增。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|此参数为SHOW PLMN DFTMSCS命令的输出参数。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
MSCSIP|缺省MSC Server地址|参数可选性:必选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址。操作人员根据实际的IP地址个数配置，系统支持一个PLMN最多配置10个地址。
命令举例 
假设SRVCC切换目标的PLMN中MCC为“460”，MNC为“01”，增加其缺省MSC Server对应的的一条IP地址，IP地址为“129.0.0.1”。
ADD PLMN DFTMSCS IP:PLMN="460"-"01",MSCSIP="129.0.0.1"; 
父主题： [基于PLMN的缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除MSC Server IP地址(DEL PLMN DFTMSCS IP) 
### 删除MSC Server IP地址(DEL PLMN DFTMSCS IP) 
命令功能 
该命令用于根据RNC或者BSC所属的PLMN删除单个MSC Server IP缺省地址。 
该命令执行后，会将指定的MSC Server IP地址，从该PLMN原来已有的地址IP列表中删除。 
如果此地址为此PLMN对应的唯一地址，则无法删除。此时操作员可通过执行[DEL PLMN DFTMSCS]命令删除整条记录。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|此参数为SHOW PLMN DFTMSCS命令的输出参数。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
MSCSIP|缺省MSC Server地址|参数可选性:必选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址。操作人员根据实际的IP地址个数配置，系统支持一个PLMN最多配置10个地址。
命令举例 
假设SRVCC切换目标的PLMN中MCC为“460”，MNC为“01”，删除其缺省MSC Server对应的一条IP地址，IP地址为“129.0.0.1”。
DEL PLMN DFTMSCS IP:PLMN="460"-"01",MSCSIP="129.0.0.1"; 
父主题： [基于PLMN的缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于PLMN的缺省SRVCC增强MSC Server配置(ADD PLMN DFTMSCS) 
### 新增基于PLMN的缺省SRVCC增强MSC Server配置(ADD PLMN DFTMSCS) 
命令功能 
SRVCC（Single Radio Voice Call Continuity，双模单待无线语音呼叫连续性）为单语音呼叫持续。当用户在LTE网络进行语音业务并需要切换至GSM/UMTS网络时，为了保证不中断用户的语音业务，MME提供了SRVCC解决方案，使用户感知不到LTE和CS网络之间切换时的语音中断，解决了基于LTE网络的语音业务向GSM/UMTS网络的语音业务的无缝切换。 
进行语音业务的UE从LTE网络切换至GSM/UMTS的过程中，MME通过Sv接口向MSC发送PS to CS的切换请求，请求将语音承载切换到MSC。 
在SRVCC业务流程中，MME通过以下过程获取MSC Server地址。 
MME通过eNodeB发送的切换请求消息（Handover Required）中携带的Target ID（如RNC ID）来构造FQDN（Fully Qualified Domain Name，全称域名），MME通过解析FQDN查询到MSC Server的地址。 
如果MME不能通过解析FQDN查询到MSC Server的地址，则需要通过MME本地配置的缺省MSC Server，获取MSC Server地址，完成SRVCC业务。 
本地配置的缺省MSC Server分为两种类型： 
基于PLMN的缺省MSC Server和全局缺省MSC Server。 
如果MME无法获取某个PLMN对应的缺省MSC Server的IP地址，则使用全局缺省MSC Server。 
该命令用于为不同的PLMN配置不同的缺省MSC Server地址。 
可以针对特定的漫游用户的PLMN，配置特定的缺省MSC Server；如果不配置，则使用全局缺省MSC Server配置。 
注意事项 
该功能只适用于MME。 
该命令生效需要设置系统软参“MME支持系统缺省MSC Server”，对应的系统软件参数设置为支持。配置命令为： [SET SOFTWARE PARAMETER]: PARAID=65642,PARAVALUE=1;
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|此参数为SHOW PLMN DFTMSCS命令的输出参数。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
MSCSIP|缺省MSC Server地址|参数可选性:必选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址。操作人员根据实际的IP地址个数配置，系统支持一个PLMN最多配置10个地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。
命令举例 
假设SRVCC切换目标的PLMN的MCC为“460”，MNC为“01”，其缺省MSC Server的IP地址为“129.0.0.1”，Server名称为“msc server”。
ADD PLMN DFTMSCS:PLMN="460"-"01",MSCSIP="129.0.0.1",NAME="msc server"; 
父主题： [基于PLMN的缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于PLMN的缺省SRVCC增强MSC Server配置(SET PLMN DFTMSCS) 
### 修改基于PLMN的缺省SRVCC增强MSC Server配置(SET PLMN DFTMSCS) 
命令功能 
该命令用于根据RNC或者BSC所属的PLMN修改缺省MSC Server配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|此参数为SHOW PLMN DFTMSCS命令的输出参数。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
MSCSIP|缺省MSC Server地址|参数可选性:任选参数；参数类型:地址|配置缺省MSC Server的IP地址，包括IPv4或者IPv6地址。操作人员根据实际的IP地址个数配置，系统支持一个PLMN最多配置10个地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。
命令举例 
假设SRVCC切换目标的PLMN中MCC为“460”，MNC为“01”，将其缺省MSC Server的IP地址修改为“129.0.0.1”，Server名称修改为“msc server”。
SET PLMN DFTMSCS:PLMN="460"-"01",MSCSIP="129.0.0.1",NAME="msc server"; 
父主题： [基于PLMN的缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于PLMN的缺省SRVCC增强MSC Server配置(DEL PLMN DFTMSCS) 
### 删除基于PLMN的缺省SRVCC增强MSC Server配置(DEL PLMN DFTMSCS) 
命令功能 
该命令用于根据RNC或者BSC所属的PLMN删除其对应的缺省MSC Server配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|此参数为SHOW PLMN DFTMSCS命令的输出参数。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
命令举例 
假设SRVCC切换目标的PLMN中MCC为“460”，MNC为“01”，删除其缺省MSC Server的配置记录。
DEL PLMN DFTMSCS:PLMN="460"-"01"; 
父主题： [基于PLMN的缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于PLMN的缺省SRVCC增强MSC Server配置(SHOW PLMN DFTMSCS) 
### 查询基于PLMN的缺省SRVCC增强MSC Server配置(SHOW PLMN DFTMSCS) 
命令功能 
该命令用于根据RNC或者BSC所属的PLMN查询到对应的缺省MSC Server配置。 
如果不输入任何指定的查询参数，查询结果将显示已配置的所有RNC或者BSC的PLMN对应的缺省MSC Server配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|此参数为SHOW PLMN DFTMSCS命令的输出参数。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR1|缺省MSC Server地址1|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR2|缺省MSC Server地址2|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR3|缺省MSC Server地址3|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR4|缺省MSC Server地址4|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR5|缺省MSC Server地址5|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR6|缺省MSC Server地址6|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR7|缺省MSC Server地址7|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR8|缺省MSC Server地址8|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR9|缺省MSC Server地址9|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
IPADDR10|缺省MSC Server地址10|参数可选性:任选参数；参数类型:地址|此参数为SHOW PLMN DFTMSCS命令的输出参数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。
命令举例 
假设SRVCC切换目标的PLMN中MCC为“460”，MNC为“01”，显示其缺省MSC Server配置记录。
SHOW PLMN DFTMSCS:PLMN="460"-"01"; 
`
命令 (No.1): SHOW PLMN DFTMSCS:PLMN="460"-"01";
操作维护    PLMN     缺省MSC Server地址1   缺省MSC Server地址2   缺省MSC Server地址3   缺省MSC Server地址4   缺省MSC Server地址5   缺省MSC Server地址6   缺省MSC Server地址7   缺省MSC Server地址8   缺省MSC Server地址9   缺省MSC Server地址10   用户别名
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改   460-01   10.43.146.7           0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0               0.0.0.0                msc46001
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.077 秒）。
` 
父主题： [基于PLMN的缺省SRVCC增强MSC Server配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# PGW局向特性配置 
# PGW局向特性配置 
背景知识 
PGW局向特性用于设置MME向指定PLMN的PGW局向主动上报用户位置信息以及eNodeB ID，包括： 
 
MME根据PLMN，来设置是否主动向PGW上报用户位置信息ULI（User Location Information）。
 
 
MME根据PLMN，来设置MME主动向PGW上报ULI时，是否携带eNodeB ID给PGW。
 
 
功能描述 
在EPC网络中，3GPP规范要求MME网元和PGW网元之间进行交互的消息必须要符合3GPP29.274 GTPv2-C协议。 
随着协议本身的发展，不同的GTPv2-C版本之间可能存在一定的差异，导致不同PGW对GTPv2-C消息的支持能力不同（比如有些PGW可以识别并支持GTPv2-C消息中的某些字段，而有些PGW却不能）。因此，添加PGW局向特性，以增强MME与不同PGW之间交互的适应能力，提高MME的可服务性。 
相关主题 
 
设置MME主动上报ULI默认策略(SET MME RPT ULI DEFAULT POLICY)
 
 
查询MME主动上报ULI默认策略(SHOW MME RPT ULI DEFAULT POLICY)
 
 
新增PGW局向特性(ADD PGWCHAR)
 
 
修改PGW局向特性(SET PGWCHAR)
 
 
删除PGW局向特性(DEL PGWCHAR)
 
 
查询PGW局向特性(SHOW PGWCHAR)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置MME主动上报ULI默认策略(SET MME RPT ULI DEFAULT POLICY) 
## 设置MME主动上报ULI默认策略(SET MME RPT ULI DEFAULT POLICY) 
命令功能 
该命令用于设置MME是否支持主动向PGW上报（User Location Information，用户位置信息 ）的策略。 
注意事项 
 
如果要求全部用户都主动上报ULI，则将本命令配置为“在任何CRA信息未知情况下主动上报（Reporting for Any Situation of CRA Unknown）”，在“新增PGW局向特性”（对应命令ADD PGWCHAR）中不需要配置任何数据。
 
 
如果要求部分用户主动上报，则将本命令配置为“不主动上报时（No Initiatively Reporting）”，在“新增PGW局向特性”（对应命令ADD PGWCHAR）中进行相应的配置。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
DEFPOLICY|主动上报ULI默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在PGW未要求MME上报UE位置信息时，即在GTPv2-C消息中未向MME显式提供Change Reporting Action 字段，MME是否主动上报用户位置信息ULI（User Location Information）。
MMERPTENB|支持主动上报eNodeBID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME决策主动上报ULI时，是否携带eNodeBID给PGW。不支持：MME主动上报ULI时，不携带eNodeBID给PGW。支持：MME主动上报ULI时，携带eNodeBID给PGW。
命令举例 
修改主动上报ULI默认策略为No，命令如下： 
SET MME RPT ULI DEFAULT POLICY:DEFPOLICY="NO" 
父主题： [PGW局向特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME主动上报ULI默认策略(SHOW MME RPT ULI DEFAULT POLICY) 
## 查询MME主动上报ULI默认策略(SHOW MME RPT ULI DEFAULT POLICY) 
命令功能 
该命令用于查询MME是否支持主动向PGW上报（User Location Information，用户位置信息 ）的策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DEFPOLICY|主动上报ULI默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在PGW未要求MME上报UE位置信息时，即在GTPv2-C消息中未向MME显式提供Change Reporting Action 字段，MME是否主动上报用户位置信息ULI（User Location Information）。
MMERPTENB|支持主动上报eNodeBID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME决策主动上报ULI时，是否支持携带eNodeBID给PGW。不支持：MME主动上报ULI时，不携带eNodeBID给PGW。支持：MME主动上报ULI时，携带eNodeBID给PGW。
命令举例 
查询主动上报ULI默认策略。 
SHOW MME RPT ULI DEFAULT POLICY 
`
2019-09-02 12:32:50 命令 (No.4): SHOW MME RPT ULI DEFAULT POLICY
操作维护   主动上报ULI默认策略   支持主动上报eNodeBID   
-----------------------------------------------------------------------
修改       不主动上报            不支持   
-----------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.088 秒）。
` 
父主题： [PGW局向特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增PGW局向特性(ADD PGWCHAR) 
## 新增PGW局向特性(ADD PGWCHAR) 
命令功能 
该命令用于配置MME是否主动上报用户位置信息到指定的PGW局向。如果配置MME主动上报用户位置，则该命令执行成功后，PGW可以将接收到的用户位置信息转发给计费实体，以便计费实体执行不同的计费策略。 
注意事项 
目前MME仅支持根据PGW所在的移动网络（PLMN）确定PGW局向。 
PGW的局向特性目前仅包含MME是否主动上报用户位置信息功能。 
目前最多支持512条PGW局向特性配置记录。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|目标PGW所在PLMN的网号，由移动国家码MCC和移动网号MNC组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给指定局向PGW网元使用的移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给指定局向PGW网元使用的移动网号，如中国联通使用01（460-01）。
RISEREPULI|主动上报ULI|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|在PGW未要求MME上报UE位置信息时，即在GTPv2-C消息中未向MME显式提供Change Reporting Action  字段，MME是否主动上报用户位置信息ULI（User Location Information）。
MMEPLMNRPTENB|支持主动上报eNodeBID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置当MME决策主动上报ULI时，是否支持携带eNodeBID给PGW。不支持：MME主动上报ULI时，不携带eNodeBID给PGW。支持：MME主动上报ULI时，携带eNodeBID给PGW。
命令举例 
新增PGW局向特性配置，设置PGW的PLMN为"460"-"02"、MME不主动向该PGW局向上报用户位置信息，命令如下： 
ADD PGWCHAR:PLMN="460"-"02",RISEREPULI="NO" 
父主题： [PGW局向特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改PGW局向特性(SET PGWCHAR) 
## 修改PGW局向特性(SET PGWCHAR) 
命令功能 
该命令用于修改PGW局向特性配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|目标PGW所在PLMN的网号，由移动国家码MCC和移动网号MNC组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给指定局向PGW网元使用的移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给指定局向PGW网元使用的移动网号，如中国联通使用01（460-01）。
RISEREPULI|主动上报ULI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在PGW未要求MME上报UE位置信息时，即在GTPv2-C消息中未向MME显式提供Change Reporting Action  字段，MME是否主动上报用户位置信息ULI（User Location Information）。
MMEPLMNRPTENB|支持主动上报eNodeBID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME决策主动上报ULI时，是否支持携带eNodeBID给PGW。不支持：MME主动上报ULI时，不携带eNodeBID给PGW。支持：MME主动上报ULI时，携带eNodeBID给PGW。
命令举例 
修改PLMN为"460"-"02"的PGW局向特性配置，将主动上报ULI修改为MME不主动向该PGW局向上报用户位置信息，命令如下： 
SET PGWCHAR:PLMN="460"-"02",RISEREPULI="NO" 
父主题： [PGW局向特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除PGW局向特性(DEL PGWCHAR) 
## 删除PGW局向特性(DEL PGWCHAR) 
命令功能 
该命令用于删除PGW局向特性配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|目标PGW所在PLMN的网号，由移动国家码MCC和移动网号MNC组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给指定局向PGW网元使用的移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给指定局向PGW网元使用的移动网号，如中国联通使用01（460-01）。
命令举例 
删除PLMN为"460"-"02"的PGW局向特性配置，命令如下： 
DEL PGWCHAR:PLMN="460"-"02" 
父主题： [PGW局向特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询PGW局向特性(SHOW PGWCHAR) 
## 查询PGW局向特性(SHOW PGWCHAR) 
命令功能 
该命令用于查询PGW局向特性配置。当输入目标PGW所在移动网络的PLMN参数时，查询结果为指定PGW局向的特性参数配置，否则查询本局所有PGW局向特性参数配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|目标PGW所在PLMN的网号，由移动国家码MCC和移动网号MNC组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给指定局向PGW网元使用的移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给指定局向PGW网元使用的移动网号，如中国联通使用01（460-01）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|目标PGW所在PLMN的网号，由移动国家码MCC和移动网号MNC组成。
RISEREPULI|主动上报ULI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在PGW未要求MME上报UE位置信息时，即在GTPv2-C消息中未向MME显式提供Change Reporting Action  字段，MME是否主动上报用户位置信息ULI（User Location Information）。
MMEPLMNRPTENB|支持主动上报eNodeBID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME决策主动上报ULI时，是否支持携带eNodeBID给PGW。不支持：MME主动上报ULI时，不携带eNodeBID给PGW。支持：MME主动上报ULI时，携带eNodeBID给PGW。
命令举例 
查询所有PGW局向特性配置，命令如下： 
SHOW PGWCHAR 
`
命令 (No.2): SHOW PGWCHAR
操作维护 PLMN 主动上报ULI 
---------------------------------
复制 修改  000-390 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-391 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-392 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-393 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-394 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-395 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-396 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-397 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-398 在从GnGp SGSN切入无法获得CRA时主动上报 
复制 修改  000-399 在从GnGp SGSN切入无法获得CRA时主动上报 
---------------------------------
记录数 10
命令执行成功（耗时 0.159 秒）。
` 
父主题： [PGW局向特性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 基于PGW IP控制配置 
# 基于PGW IP控制配置 
背景知识 
            
            现网部署的PGW不一定都支持当用户位置改变时会上报消息。MME可以根据现网部署，来指示PGW上报用户位置改变消息。
        
功能描述 
            
            在MME上配置支持用户位置改变上报功能的PGW列表，指示PGW支持用户位置改变上报。MME可以根据PGW IP来指示某个PGW支持用户位置变化上报功能，支持按默认策略来上报用户位置变化功能。
        
相关主题 
 
设置PGW IP控制策略(SET PGWIP POLICY)
 
 
查询PGW IP控制策略(SHOW PGWIP POLICY)
 
 
新增PGW IP控制(ADD PGWIP FUNC)
 
 
修改PGW IP控制(SET PGWIP FUNC)
 
 
删除PGW IP控制(DEL PGWIP FUNC)
 
 
查询PGW IP控制(SHOW PGWIP FUNC)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置PGW IP控制策略(SET PGWIP POLICY) 
## 设置PGW IP控制策略(SET PGWIP POLICY) 
命令功能 
该命令用于设置MME是否支持基于配置的PGW IP指示PGW Change Reporting support Indication和支持位置变化上报的默认策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPLCRIONPGW|基于PGW指示支持位置变化上报|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|设置MME是否指示某个PGW支持用户位置变化上报功能。
DEFSUPLOCCHGRPT|支持位置变化上报默认策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|设置MME指示该PGW是否支持按默认策略来上报用户位置变化功能。
命令举例 
设置PGW IP控制策略，选择MME支持基于PGW指示支持位置变化上报和不支持位置变化上报的PGW IP列表  
SET PGWIP POLICY:SUPLCRIONPGW="SUPPORT",DEFSUPLOCCHGRPT="NOSUPPORT"; 
父主题： [基于PGW IP控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询PGW IP控制策略(SHOW PGWIP POLICY) 
## 查询PGW IP控制策略(SHOW PGWIP POLICY) 
命令功能 
该命令用于查询MME是否支持基于配置的PGW IP指示PGW Change Reporting support Indication和支持位置变化上报的默认策略。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPLCRIONPGW|基于PGW指示支持位置变化上报|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置MME是否指示某个PGW支持用户位置变化上报功能。
DEFSUPLOCCHGRPT|支持位置变化上报默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置MME指示该PGW是否支持按默认策略来上报用户位置变化功能。
命令举例 
查询PGW IP控制策略。 
SHOW PGWIP POLICY; 
`
2020-07-15 13:29:26 命令 (No.12): SHOW PGWIP POLICY
操作维护 基于PGW指示支持位置变化上报             支持位置变化上报默认策略 
-------------------------------------------------------------------------
修改      支持                                 不支持
-------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.02 秒）。
` 
父主题： [基于PGW IP控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增PGW IP控制(ADD PGWIP FUNC) 
## 新增PGW IP控制(ADD PGWIP FUNC) 
命令功能 
该命令用于新增支持或不支持位置改变上报的PGW网元控制面IP地址。
注意事项 
PGW IP包括接口地址和业务地址。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|PGW IP|参数可选性:必选参数；参数类型:地址|PGW网元控制面IP地址（包括接口地址和业务地址），包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
SUPLOCCHGRPT|支持位置变化上报|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置相应的PGW是否支持位置改变上报。
命令举例 
新增PGW IP控制，其中IP地址为112.2.2.3，位置变化上报为支持。 
ADD PGWIP FUNC:IP="112.2.2.3",SUPLOCCHGRPT="SUPPORT"; 
父主题： [基于PGW IP控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改PGW IP控制(SET PGWIP FUNC) 
## 修改PGW IP控制(SET PGWIP FUNC) 
命令功能 
该命令用于修改支持或不支持位置改变上报的PGW网元控制面IP地址。
注意事项 
PGW IP包括接口地址和业务地址。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|PGW IP|参数可选性:必选参数；参数类型:地址|PGW网元控制面IP地址（包括接口地址和业务地址），包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
SUPLOCCHGRPT|支持位置变化上报|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置相应的PGW是否支持位置改变上报。
命令举例 
修改PGW IP控制，其中IP地址为112.2.2.3，位置变化上报为不支持。 
SET PGWIP FUNC:IP="112.2.2.3",SUPLOCCHGRPT="NOSUPPORT"; 
父主题： [基于PGW IP控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除PGW IP控制(DEL PGWIP FUNC) 
## 删除PGW IP控制(DEL PGWIP FUNC) 
命令功能 
该命令用于删除支持或不支持位置改变上报的PGW网元控制面IP地址。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|PGW IP|参数可选性:必选参数；参数类型:地址|PGW网元控制面IP地址（包括接口地址和业务地址），包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
命令举例 
删除PGW IP控制，IP地址为112.2.2.3 
DEL PGWIP FUNC:IP=112.2.2.3; 
父主题： [基于PGW IP控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询PGW IP控制(SHOW PGWIP FUNC) 
## 查询PGW IP控制(SHOW PGWIP FUNC) 
命令功能 
该命令用于查询支持或不支持位置改变上报的PGW网元控制面IP地址。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|PGW IP|参数可选性:任选参数；参数类型:地址|PGW网元控制面IP地址（包括接口地址和业务地址），包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IP|PGW IP|参数可选性:必选参数；参数类型:地址|PGW网元控制面IP地址（包括接口地址和业务地址），包括IPv4和IPv6类型，其中，IPv6地址不支持缩写。
SUPLOCCHGRPT|支持位置变化上报|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置相应的PGW是否支持位置改变上报。
命令举例 
查询PGW IP控制。 
SHOW PGWIP FUNC; 
`
2020-07-15 11:03:52 命令 (No.11): SHOW PGWIP FUNC
操作维护        PGW IP      支持位置变化上报 
--------------------------------------------------
复制 修改 删除  112.2.2.3   不支持 
--------------------------------------------------
记录数 1
命令执行成功（耗时 0.019 秒）。
` 
父主题： [基于PGW IP控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 内置PGW的GGSN IP配置 
# 内置PGW的GGSN IP配置 
背景知识 
运营商要求支持LTE的多模终端从2G/3G网络切换到LTE网络时，MME可以选择与PGW合一的SGW或拓扑关系最邻近的SGW。在EPC网络中SGW和PGW合一设置或邻近设置的GW组网，是一种普遍且典型的组网方式，这种GW组网方式可减少数据传输时延，也能减少跨框、跨地域的业务流量，很多运营商都在使用这种GW组网。 
要实现上述要求，需要用户从2G/3G网络切换到LTE网络或重选到另一个SGSN覆盖区时，MME/SGSN Gn口发给新MME/SGSN的消息中带上PGW主机名。根据协议3GPP 29.060：SGSN Context Response 和 Forward Relocation Request消息中可以携带PGW主机名，MME/SGSN实现标准的PGW主机名传递，还不能解决所有现网环境下MME要选择与PGW合一的SGW或拓扑关系最邻近的SGW的问题，例如以下的现网环境： 
 
MME与不支持PGW FQDN IE传递的SGSN对接。
 
 
现网DNS是老设备，其上没有PGW主机名数据，通过SGSN解析内置PGW的GGSN IP地址时无法获取到PGW主机名。
 
 
SGSN与不支持PGW FQDN IE传递的MME对接。
 
 
为了解决以上MME不能选择与PGW合一的SGW或拓扑关系最邻近的SGW的问题，SGSN/MME提供本地配置“内置PGW的GGSN IP配置”。 
功能描述 
“内置PGW的GGSN IP配置”实现SGSN/MME通过GGSN IP地址获取到对应的PGW主机名。当SGSN执行地址解析没有获取到PGW主机名，或局间没有传递PGW主机名使SGSN/MME无法获得PGW主机名时，使用该配置。具体应用场景如下： 
 
发生局间切换或局间RAU/TAU，SGSN/MME老局发送Forward Relocation Request和SGSN Context Response消息时，支持LTE的多模终端根据“内置PGW的GGSN IP配置”获取GGSN IP地址对应的PGW主机名，携带出局。
 
 
发生局间切换或局间RAU/TAU，MME选择SGW时，如果支持拓扑选择，MME根据“内置PGW的GGSN IP配置”获取GGSN IP地址对应的PGW主机名，选择得到与PGW合一的SGW或拓扑关系最邻近的SGW。
 
 
配置根据GGSN IP地址获取PGW主机名功能的流程如下： 
 
                        配置“支持GGSN IP地址获取PGW主机名”为“支持”，配置命令为：
                        SET SUP PGW GGSNIP
                        。
                    
 
 
                        配置“内置PGW的GGSN IP配置”，配置命令为：
                        ADD IPTOPGW
                        。
                    
 
 
相关主题 
 
支持GGSN IP地址获取PGW主机名
 
 
内置PGW的GGSN IP配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 支持GGSN IP地址获取PGW主机名 
## 支持GGSN IP地址获取PGW主机名 
背景知识 
在EPC网络中，SGW和PGW合一设置或邻近设置的GW组网，是一种普遍且典型的组网方式，该组网方式可减少数据传输时延，也能减少跨框、跨地域的业务流量，目前很多运营商都在使用这种GW组网方式。同时，运营商要求MME在支持LTE的多模终端从2G/3G网络切换到LTE网络时，可以选择与PGW合一的SGW或拓扑关系最邻近的SGW。 
一般情况下，按照3GPP 29.060协议中的描述来实现标准的PGW主机名传递，就能满足现网中运营商的要求，但在特殊现网条件下，如对接的MME/SGSN不能传递PGW主机名时，则需要开启“支持GGSN IP地址获取PGW主机名”功能。开启该功能后，MME/SGSN可通过GGSN IP地址获取到PGW主机名。MME/SGSN将获取到的PGW主机名用于局间传送或根据获取的PGW主机名查找到与PGW合一的SGW或拓扑关系最邻近的SGW。 
功能描述 
“支持GGSN IP地址获取PGW主机名”配置是启用“内置PGW的GGSN IP配置”的开关。配置“支持GGSN IP地址获取PGW主机名”为“支持”，“内置PGW的GGSN IP配置”的配置数据才能生效。 
相关主题 
 
设置支持GGSN IP地址获取PGW主机名(SET SUP PGW GGSNIP)
 
 
查询支持GGSN IP地址获取PGW主机名(SHOW SUP PGW GGSNIP)
 
 
父主题： [内置PGW的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置支持GGSN IP地址获取PGW主机名(SET SUP PGW GGSNIP) 
### 设置支持GGSN IP地址获取PGW主机名(SET SUP PGW GGSNIP) 
命令功能 
该命令用于配置MME/SGSN是否支持根据GGSN IP地址获取PGW主机名。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
PGWBYGGSNIP|支持GGSN IP地址获取PGW主机名|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME/SGSN是否支持根据GGSN IP地址获取PGW主机名。不支持：MME/SGSN不支持根据GGSN IP地址获取PGW主机名。支持：MME/SGSN支持根据GGSN IP地址获取PGW主机名。
命令举例 
设置MME/SGSN支持根据GGSN IP地址获取PGW主机名。 
SET SUP PGW GGSNIP:PGWBYGGSNIP="YES"; 
父主题： [支持GGSN IP地址获取PGW主机名]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询支持GGSN IP地址获取PGW主机名(SHOW SUP PGW GGSNIP) 
### 查询支持GGSN IP地址获取PGW主机名(SHOW SUP PGW GGSNIP) 
命令功能 
该命令用于查询MME/SGSN是否支持根据GGSN IP地址获取PGW主机名。当需要查看MME/SGSN是否支持根据GGSN IP地址获取PGW主机名时，使用该命令。命令执行成功后，可查询到根据GGSN IP地址获取PGW主机名的功能是开启还是关闭。 
注意事项 
无 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PGWBYGGSNIP|支持GGSN IP地址获取PGW主机名|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME/SGSN是否支持根据GGSN IP地址获取PGW主机名。不支持：MME/SGSN不支持根据GGSN IP地址获取PGW主机名。支持：MME/SGSN支持根据GGSN IP地址获取PGW主机名。
命令举例 
查询MME/SGSN是否支持根据GGSN IP地址获取PGW主机名。 
SHOW SUP PGW GGSNIP 
`
命令 (No.6): SHOW SUP PGW GGSNIP
操作维护  支持GGSN IP地址获取PGW主机名
--------------------------------------
修改      支持                           
--------------------------------------
记录数 1
命令执行成功（耗时 0.048 秒）。
` 
父主题： [支持GGSN IP地址获取PGW主机名]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 内置PGW的GGSN IP配置 
## 内置PGW的GGSN IP配置 
背景知识 
运营商要求MME在支持LTE的多模终端从2G/3G网络切换到LTE网络时，可以选择与PGW合一的SGW或拓扑关系最邻近的SGW。要实现该要求，需要用户从2G/3G网络切换到LTE网络或重选到另一个SGSN覆盖区时，MME/SGSN通过Gn口发送给新MME/SGSN的消息中带上PGW主机名。根据3GPP 29.060协议中7.5.4节和7.5.6节的描述，SGSN Context Response和Forward Relocation Request消息中可以携带PGW主机名，MME/SGSN实现标准的PGW主机名传递。但在某些特殊现网条件下，仍不能解决MME选择与PGW合一的SGW或拓扑关系最邻近的SGW的问题，如以下的现网环境： 
 
MME与不支持PGW FQDN IE传递的SGSN对接。
 
 
SGSN与不支持PGW FQDN IE传递的MME对接。
 
 
现网DNS是老设备，没有PGW主机名数据，通过SGSN解析内置PGW的GGSN IP地址时无法获取到PGW主机名。
 
 
为了解决以上MME不能选择与PGW合一的SGW或拓扑关系最邻近的SGW的问题，SGSN/MME提供本地配置“内置PGW的GGSN IP配置”。 
功能描述 
“内置PGW的GGSN IP配置”实现SGSN/MME通过GGSN IP地址获取对应的PGW主机名。 
当SGSN执行地址解析没有获取到PGW主机名，或局间没有传递PGW主机名使SGSN/MME无法获取到PGW主机名时，使用该配置。具体应用场景如下： 
 
发生局间切换或局间RAU/TAU，SGSN/MME老局发送Forward Relocation Request或SGSN Context Response消息时，支持LTE的多模终端根据“内置PGW的GGSN IP配置”获取GGSN IP地址对应的PGW主机名，携带出局。
 
 
发生局间切换或局间RAU/TAU，MME选择SGW时，如果支持拓扑选择，MME根据“内置PGW的GGSN IP配置”获取GGSN IP地址对应的PGW主机名，选择得到与PGW合一的SGW或拓扑关系最邻近的SGW。
 
 
注：
 
                            只有在配置“支持GGSN IP地址获取PGW主机名”为“支持”（
                            SET SUP PGW GGSNIP
                            :PGWBYGGSNIP="YES";）的前提下，“内置PGW的GGSN IP配置”的配置数据才能生效。
                        
 
 
                            若要实现通过局间消息Forward Relocation Request和SGSN Context Response传递PGW主机名，需通过命令
                            SET SOFTWARE PARAMETER
                            :PARAID=786696,PARAVALUE=1;设置软件参数“支持携带PGW FQDN IE”值为1。
                        
 
 
相关主题 
 
新增内置PGW的GGSN IP(ADD IPTOPGW)
 
 
修改内置PGW的GGSN IP(SET IPTOPGW)
 
 
删除内置PGW的GGSN IP(DEL IPTOPGW)
 
 
查询内置PGW的GGSN IP(SHOW IPTOPGW)
 
 
父主题： [内置PGW的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增内置PGW的GGSN IP(ADD IPTOPGW) 
### 新增内置PGW的GGSN IP(ADD IPTOPGW) 
命令功能 
该命令用于新增GGSN IP地址和PGW主机名的对应关系。当发生局间切换或局间RAU/TAU，使用局间消息Forward Relocation Request和SGSN Context Response传递PGW主机名，或MME要选择得到与PGW合一的SGW或拓扑关系最邻近的SGW时，使用该命令。该命令执行成功后，MME/SGSN可以根据内置PGW的GGSN IP地址获取对应的PGW主机名。 
注意事项 
配置的GGSN IP地址对应内置PGW的GGSN的业务地址，非转发地址。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|内置PGW的GGSN与SGSN通信的Gn接口的业务IP地址。
PGWNAME|PGW主机名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|内置PGW的GGSN IP地址对应的PGW主机名。
命令举例 
新增内置PGW的GGSN IP配置，其中GGSN IP地址为10.43.107.126，PGW主机名为pgw.com。 
ADD IPTOPGW:GGSNIPADDR="10.43.107.126",PGWNAME="pgw.com"; 
父主题： [内置PGW的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改内置PGW的GGSN IP(SET IPTOPGW) 
### 修改内置PGW的GGSN IP(SET IPTOPGW) 
命令功能 
该命令用于修改GGSN IP地址和PGW主机名的对应关系配置。当需要修改GGSN IP地址对应的PGW主机名时，使用该命令。使用该命令成功后，GGSN IP地址和PGW主机名的对应关系配置信息被修改。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|内置PGW的GGSN与SGSN通信的Gn接口的业务IP地址。
PGWNAME|PGW主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~99个字符。|内置PGW的GGSN IP地址对应的PGW主机名。
命令举例 
将内置PGW的GGSN IP地址为10.43.107.126对应的PGW主机名修改为pgw.com.cn。 
SET IPTOPGW:GGSNIPADDR="10.43.107.126",PGWNAME="pgw.com.cn"; 
父主题： [内置PGW的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除内置PGW的GGSN IP(DEL IPTOPGW) 
### 删除内置PGW的GGSN IP(DEL IPTOPGW) 
命令功能 
该命令用于删除GGSN IP地址和PGW主机名的对应关系配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIPADDR|GGSN IP地址|参数可选性:必选参数；参数类型:地址|内置PGW的GGSN与SGSN通信的Gn接口的业务IP地址。
命令举例 
将内置PGW的GGSN IP为10.43.107.126的配置删除。 
DEL IPTOPGW:GGSNIPADDR="10.43.107.126"; 
父主题： [内置PGW的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询内置PGW的GGSN IP(SHOW IPTOPGW) 
### 查询内置PGW的GGSN IP(SHOW IPTOPGW) 
命令功能 
该命令用于查询GGSN IP地址和PGW主机名的对应关系配置。命令执行成功后，可查询到GGSN IP地址和PGW主机名的对应关系。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIPADDR|GGSN IP地址|参数可选性:任选参数；参数类型:地址|内置PGW的GGSN与SGSN通信的Gn接口的业务IP地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNIPADDR|GGSN IP地址|参数可选性:任选参数；参数类型:地址|内置PGW的GGSN与SGSN通信的Gn接口的业务IP地址。
PGWNAME|PGW主机名|参数可选性:任选参数；参数类型:字符型。|内置PGW的GGSN IP地址对应的PGW主机名。
命令举例 
查询所有内置PGW的GGSN IP与PGW主机名的对应关系。 
SHOW IPTOPGW; 
`
命令 (No.25): SHOW IPTOPGW
操作维护           GGSN IP地址        PGW主机名
---------------------------------------------------------------------------------
复制 修改 删除     10.43.107.126      pgw.com
---------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.051 秒）。
` 
父主题： [内置PGW的GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 优化切换到eHRPD的配置 
# 优化切换到eHRPD的配置 
背景知识 
LTE到eHRPD的优化切换，指UE在离开LTE前，先预注册到eHRPD，再切换到eHRPD，这样可以减少UE从LTE到eHRPD的切换时间以及UE的业务中断时间。 
LTE到eHRPD的优化切换有两个阶段： 
 
UE经过LTE预注册到eHRPD。
 
 
eNB发起切换流程。
 
 
eHRPD的无线接入网元为eAN，MME通过S101接口和eAN交互，在LTE到eHRPD的优化切换过程中，MME根据eNB提供的目标SectorID，结合本地配置的对应关系解析出eAN IP地址。 
为了尽可能减少LTE到eHRPD的优化切换对业务的影响，在优化切换过程中，可以建立从eNB到HSGW的数据前转隧道，把切换过程中没有成功投递给UE的数据报文前转到HSGW，由HSGW再投递给UE。 
功能描述 
支持从LTE到eHRPD的优化切换功能需要License支持，对应的License项为“MME支持优化切换到eHRPD功能License开关”。 
实现优化切换到eHRPD，MME需要增加如下配置。 
 
                        优化切换到eHRPD的策略配置：配置MME是否支持优化切换、eAN ID在SectorID中的位置、是否支持数据前转，参见：
                        SET OPTMHOPO
                        。
                    
 
 
                        获取eAN地址配置：配置eAN ID和eAN IP地址的对应关系，参见：
                        ADD EANIDTOIP
                        。
                    
 
 
相关主题 
 
优化切换到eHRPD的策略配置
 
 
获取eAN地址配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 优化切换到eHRPD的策略配置 
## 优化切换到eHRPD的策略配置 
背景知识 
优化切换是指3GPPTS23.402第9章描述的切换流程。 
LTE到eHRPD的优化切换，指UE在离开LTE前，先预注册到eHRPD，再切换到eHRPD，这样可以减少UE从LTE到eHRPD的切换时间以及UE的业务中断时间。 
LTE到eHRPD的优化切换有两个阶段： 
UE经过LTE预注册到eHRPD。 
eNB发起切换流程。 
eHRPD的无线接入网元为eAN，MME通过S101接口和eAN交互，在LTE到eHRPD的优化切换过程中，MME根据eNodeB提供的目标SectorID，结合本地配置的对应关系解析出eAN IP地址。 
为了尽可能减少LTE到eHRPD的优化切换对业务的影响，在优化切换过程中，可以建立从eNodeB到HSGW的数据前转隧道，把切换过程中没有成功投递给UE的数据报文前转到HSGW，由HSGW再投递给UE。 
由于从eHRPD非优化切换到LTE，只要很短的时间（几百毫秒），因此不需要进行eHRPD到LTE的优化切换。协议已停止了对eHRPD到LTE优化切换的标准化，3GPPTS23.402只定义了流程，但NAS接口协议没有定义具体的消息。因此MME对eHRPD到LTE优化切换是不需要支持的。 
功能描述 
                支持从LTE到eHRPD的优化切换功能需要License支持，通过命令
                [SHOW LICENSE]
                查看对应的License项“MME支持优化切换到eHRPD功能”。 只有该选项打开，才需要设置优化切换到eHRPD的策略。
            
本功能配置MME是否支持从LTE到eHRPD的优化切换功能、eAN ID在SectorID中的位置、是否支持数据前转。 
3GPP2协议C.S0024-B_v3.0_HRPD，定义了SectorID的各种格式，但没有说明小区信息如何填充，以及SectorID是否包含eAN ID。因此需要配置SectorID的起始和结束位置来确定eAN ID。 
相关主题 
 
设置优化切换到eHRPD的策略(SET OPTMHOPO)
 
 
查询优化切换到eHRPD的策略(SHOW OPTMHOPO)
 
 
父主题： [优化切换到eHRPD的配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置优化切换到eHRPD的策略(SET OPTMHOPO) 
### 设置优化切换到eHRPD的策略(SET OPTMHOPO) 
命令功能 
该命令用于设置LTE到eHRPD的优化切换功能的开关、eAN ID在Sector ID中的位置、是否支持数据前转。 
注意事项 
只有“MME支持优化切换到eHRPD功能"的License打开了，才能看到该配置。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IFOPTMHO|支持到eHRPD的优化切换|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本MME是否支持到eHRPD的优化切换：NO：不支持YES：支持
STARTSECTOR|Sector ID起始位|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|该参数用于指定SectorID的起始位，和SectorID的结束位一起确定解析eAN地址的eAN ID。注意：SectorID的最右边的BIT为第一个BIT，最左边的为最后一个BIT。
ENDSECTOR|Sector ID结束位|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|该参数用于指定SectorID的结束位，和SectorID的起始位一起确定解析eAN地址的eAN ID。注意：结束位不可以小于起始位，结束位和起始位之间不可以超过32个BIT。
IFDATAFWD|支持数据前转|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置LTE到eHRPD的优化切换过程是否支持数据前转：NO：不支持YES：支持
命令举例 
设置优化切换到eHRPD的策略，其中Sector ID起始位为74，Sector ID结束位为81。 
SET OPTMHOPO:STARTSECTOR=74,ENDSECTOR=81; 
父主题： [优化切换到eHRPD的策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询优化切换到eHRPD的策略(SHOW OPTMHOPO) 
### 查询优化切换到eHRPD的策略(SHOW OPTMHOPO) 
命令功能 
该命令用于查询LTE到eHRPD的优化切换功能的开关、eAN ID在Sector ID中的位置、是否支持数据前转。 
注意事项 
只有“MME支持优化切换到eHRPD功能"的License打开了，才能看到该配置。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IFOPTMHO|支持到eHRPD的优化切换|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本MME是否支持到eHRPD的优化切换：NO：不支持YES：支持
STARTSECTOR|Sector ID起始位|参数可选性:任选参数；参数类型:整数。|该参数用于指定SectorID的起始位，和SectorID的结束位一起确定解析eAN地址的eAN ID。注意：SectorID的最右边的BIT为第一个BIT，最左边的为最后一个BIT。
ENDSECTOR|Sector ID结束位|参数可选性:任选参数；参数类型:整数。|该参数用于指定SectorID的结束位，和SectorID的起始位一起确定解析eAN地址的eAN ID。注意：结束位不可以小于起始位，结束位和起始位之间不可以超过32个BIT。
IFDATAFWD|支持数据前转|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置LTE到eHRPD的优化切换过程是否支持数据前转：NO：不支持YES：支持
命令举例 
查询优化切换到eHRPD的策略。 
SHOW OPTMHOPO 
`
命令 (No.3): SHOW OPTMHOPO
操作维护 支持到eHRPD的优化切换  Sector ID起始位 Sector ID结束位   支持数据前转 
--------------------------------------------------------------------------------------
修改      不支持                  74                 81               支持 
--------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [优化切换到eHRPD的策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 获取eAN地址配置 
## 获取eAN地址配置 
背景知识 
在LTE到eHRPD的优化切换流程中，MME需要根据eAN ID（Cell ID）获取eAN的IP地址，这样MME和eAN才能通讯。 
                通过配置命令：
                [SET OPTMHOPO]
                设置Sector ID的起始和结束位置确定eAN ID，进而通过本配置设置eAN IP地址。
            
                通过查询命令：
                [SHOW OPTMHOPO]
                查询设置的Sector ID的起始和结束位置确定eAN ID。
            
功能描述 
支持从LTE到eHRPD的优化切换功能需要License支持，对应的License项为“MME支持优化切换到eHRPD功能”。只有“MME支持优化切换到eHRPD功能”License开关打开了，才需要进行获取eAN地址的配置。 
本功能配置eAN ID和eAN IP地址间的对应关系。 
                在设置获取eAN地址配置前，需先通过命令
                [SET OPTMHOPO]
                设置eAN ID在SectorID中的位置。
            
相关主题 
 
新增获取eAN地址(ADD EANIDTOIP)
 
 
修改获取eAN地址(SET EANIDTOIP)
 
 
删除获取eAN地址(DEL EANIDTOIP)
 
 
查询获取eAN地址(SHOW EANIDTOIP)
 
 
父主题： [优化切换到eHRPD的配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增获取eAN地址(ADD EANIDTOIP) 
### 新增获取eAN地址(ADD EANIDTOIP) 
命令功能 
该命令用于增加eAN ID（Cell ID）和eAN IP地址的对应关系。 
注意事项 
只有“MME支持优化切换到eHRPD功能”的License项打开了，才能看到该配置。 
同一个eAN ID（Cell ID）只能对应一个eAN IP地址，也即只能设置一条记录。 
参数说明 
标识|名称|类型|说明
---|---|---|---
EANORCELLID|eAN标识或小区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|eAN ID或eHRPD Cell ID。
EANIP|eAN地址|参数可选性:必选参数；参数类型:地址|eAN S101接口GTPC地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名，由用户自定义，便于记忆和识别。
命令举例 
新增获取eAN地址，其中eAN标识或小区标识为1，eAN地址为10.41.101.19。 
ADD EANIDTOIP:EANORCELLID=1,EANIP="10.41.101.19"; 
父主题： [获取eAN地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改获取eAN地址(SET EANIDTOIP) 
### 修改获取eAN地址(SET EANIDTOIP) 
命令功能 
该命令用于修改已存在的eAN ID（Cell ID）和eAN IP地址的对应关系。 
注意事项 
只有“MME支持优化切换到eHRPD功能”的License项打开了，才能看到该配置。 
只能修改通过命令[SHOW EANIDTOIP]查询到的记录，而且只能修改eAN地址和用户别名。
参数说明 
标识|名称|类型|说明
---|---|---|---
EANORCELLID|eAN标识或小区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|eAN ID或eHRPD Cell ID。
EANIP|eAN地址|参数可选性:任选参数；参数类型:地址|eAN S101接口GTPC地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名，由用户自定义，便于记忆和识别。
命令举例 
修改eAN标识或小区标识为1的配置数据，将eAN地址修改为10.41.101.20。 
SET EANIDTOIP:EANORCELLID=1,EANIP="10.41.101.20"; 
父主题： [获取eAN地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除获取eAN地址(DEL EANIDTOIP) 
### 删除获取eAN地址(DEL EANIDTOIP) 
命令功能 
该命令用于删除已存在的eAN ID（Cell ID）和eAN IP地址的对应关系。 
注意事项 
只有“MME支持优化切换到eHRPD功能”的License项打开了，才能看到该配置。 
只能删除通过命令[SHOW EANIDTOIP]查询到的记录。
参数说明 
标识|名称|类型|说明
---|---|---|---
EANORCELLID|eAN标识或小区标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|eAN ID或eHRPD Cell ID。
命令举例 
删除eAN标识或小区标识为1的配置数据。 
DEL EANIDTOIP:EANORCELLID=1; 
父主题： [获取eAN地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询获取eAN地址(SHOW EANIDTOIP) 
### 查询获取eAN地址(SHOW EANIDTOIP) 
命令功能 
该命令用于查询已配置的eAN ID（Cell ID）和eAN IP地址的对应关系。 
注意事项 
只有“MME支持优化切换到eHRPD功能”的License项打开了，才能看到该配置。 
参数说明 
标识|名称|类型|说明
---|---|---|---
EANORCELLID|eAN标识或小区标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|eAN ID或eHRPD Cell ID。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
EANORCELLID|eAN标识或小区标识|参数可选性:任选参数；参数类型:整数。|eAN ID或eHRPD Cell ID。
EANIP|eAN地址|参数可选性:任选参数；参数类型:地址|eAN S101接口GTPC地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户别名，由用户自定义，便于记忆和识别。
命令举例 
查询获取eAN地址。 
SHOW EANIDTOIP 
`
命令 (No.7): SHOW EANIDTOIP
操作维护       eAN标识或小区标识   eAN地址       用户别名 
--------------------------------------------------------------
复制 修改 删除    1                   10.41.101.20  
--------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.02 秒）。
` 
父主题： [获取eAN地址配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME非3GPP互操作配置 
# MME非3GPP互操作配置 
背景知识 
移动通讯技术的演进包括无线接入技术从2G/3G到LTE的演进，也包括移动核心网从电路域到分组域、再到EPC的演进，而EPC不仅支持传统的GSM、UMTS和LTE接入，也支持非3GPP接入技术，如WLAN、CDMA2000、WiMAX等。 
功能描述 
支持从LTE到eHRPD（evolved High Rate Packet Data，演进的高速分组数据）的优化切换功能”，实现优化切换到eHRPD，MME需要增加如下配置： 
 
通过SHOW UMAC LICENSE命令确认“MME支持优化切换到eHRPD功能“License开关为开启。
 
 
                        通过
                        SET OPTMHOPO
                        命令配置优化切换到eHRPD的策略。
                    
 
 
                        通过
                        ADD EANIDTOIP
                        命令配置eAN地址。
                    
 
 
相关主题 
 
WLAN互操作配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## WLAN互操作配置 
## WLAN互操作配置 
背景知识 
移动数据流量的爆炸式增长，推动移动运营商利用WLAN网络来增加覆盖范围并提高回程容量。WLAN网络作为互补手段，可以有效扩大覆盖范围，降低每比特数据交付成本，有效缓解3G/4G无线频谱的拥挤和昂贵回程资源的紧张，同时也是提升用户体验和忠诚度的有效的方法。 
WLAN作为移动运营商优选的异构网络来部署，一方面是因为移动终端中WLAN已经是标准配置；另一方面是因为WLAN的频谱免费开放、产业链成熟和部署灵活等优势。所以对于移动运营商来说，在热点地区部署WLAN网络作为移动蜂窝网络的有效补充，不但OPEX和CAPEX较低，而且还提高了网络服务质量和用户满意度。 
3GPP定义的WLAN与3GPP接入网络融合技术都是基于 EPC架构的。 
功能描述 
本功能用于控制用户移动到WLAN和3GPP移动蜂窝网络重叠区时，是否分流一些或全部业务到WLAN网络。 
当移动用户在WLAN和3GPP移动蜂窝网络重叠覆盖区内，可以向WLAN网络卸载分流一些业务，同时还可以保存一些蜂窝业务如VoIP。 
针对多接入分组数据网连接的网络架构，对来自不同网络的接入选择不同的分组数据网连接，但共用相同的分组数据网网关。 
相关主题 
 
无线辅助WLAN互操作控制开关配置
 
 
无线辅助WLAN互操作本地策略配置
 
 
父主题： [MME非3GPP互操作配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 无线辅助WLAN互操作控制开关配置 
### 无线辅助WLAN互操作控制开关配置 
背景知识 
RAN-assisted WLAN interworking是指eNodeB可以通过RRC信令中携带辅助参数来让UE卸载负荷到WLAN。 
RAN-assisted WLAN interworking功能对MME来说就是对WLAN offload acceptability的控制，MME可以通过WLAN offload acceptability指示UE不能够将负荷卸载到WLAN，也可以指示UE某个PDN连接负荷可以卸载到WLAN。为了能够灵活控制，MME可以将本地配置的WLAN offload acceptability下发给UE，也可以传递用户在HSS签约的WLAN offload acceptability给UE。 
功能描述 
本配置用于控制MME对RAN-assisted WLAN interworking功能的支持，参数主要包括：是否支持RAN辅助的WLAN互操作，是否支持基于RAN的WLAN互操作的本地控制，是否在WLAN offload acceptability变化时立即通知UE，本地默认的WLAN offload acceptability，以及当用户有签约且本地又有配置时是否本地优先。 
 
是否支持RAN辅助的WLAN互操作：这是功能总开关，只有在本功能开关打开时，MME才会根据本地配置或用户签约对WLAN offload acceptability进行控制。
 
 
是否支持基于RAN的WLAN互操作的本地控制：当选择不支持时，则MME只将用户签约的WLAN offload acceptability下发给UE。当支持本地控制时，则MME下发用户签约或本地配置的WLAN offload acceptability给UE。
 
 
MME是否支持WLAN负荷卸载能力变化的及时生效：当用户签约信息变化时，如果只是WLAN offload acceptability变化，为了下发这个信息会增加网络信令负荷，所以增加开关进行控制，由运营商根据网络情况确定是否有必要为此增加系统信令负荷。
 
 
默认E-UTRAN策略：指示终端在E-UTRAN接入时的WLAN offload acceptability，对所有用户生效。
 
 
默认UTRAN策略：指示终端在UTRAN接入时的WLAN offload acceptability，对所有用户生效。
 
 
本地默认优先：控制用户有签约的WLAN offload acceptability时，是使用MME配置的默认策略还是签约的。
 
 
相关主题 
 
设置无线辅助WLAN互操作控制开关(SET WLAN INTERWORKING CONTROL SWITCH)
 
 
查询无线辅助WLAN互操作控制开关(SHOW WLAN INTERWORKING CONTROL SWITCH)
 
 
父主题： [WLAN互操作配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置无线辅助WLAN互操作控制开关(SET WLAN INTERWORKING CONTROL SWITCH) 
#### 设置无线辅助WLAN互操作控制开关(SET WLAN INTERWORKING CONTROL SWITCH) 
命令功能 
该命令用于设置是否支持RAN辅助的WLAN互操作，是否支持本地策略，是否在WLAN负荷卸载能力变化时立即通知UE。当需要对EPC业务卸载到WLAN进行控制时，使用该命令。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPRANWLAN|MME是否支持RAN-assisted WLAN Interworking|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持RAN辅助的WLAN互操作。这是功能总开关，只有在本功能开关打开时，MME才会根据本地配置或用户签约对WLAN offload acceptability进行控制。不支持：MME不支持RAN辅助的WLAN互操作。支持：MME支持RAN辅助的WLAN互操作。
LOCWLANCTRLSUP|是否支持基于RAN的WLAN互操作的本地控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持RAN辅助的WLAN互操作的本地控制。本地控制通过ADD WLAN INTERWORKING LOCAL POLICY命令配置实现。不支持：MME不支持RAN辅助的WLAN互操作的本地控制，则MME只将用户签约的WLAN offload acceptability下发给UE。支持：MME支持RAN辅助的WLAN互操作的本地控制，则MME下发用户签约或本地配置的WLAN offload acceptability给UE。
INSTANTCHANGE|MME是否支持WLAN负荷卸载能力变化的及时生效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持WLAN offload acceptability变化的即时生效。当用户签约信息变化时，如果只是WLAN offload acceptability变化，为了下发这个信息会增加网络信令负荷，所以增加开关进行控制，由运营商根据网络情况确定是否有必要为此增加系统信令负荷。不支持：MME不支持WLAN offload acceptability变化的即时生效。支持：MME支持WLAN offload acceptability变化的即时生效。
DFTEUTRANPOLICY|默认E-UTRAN策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置E-UTRAN下默认的WLAN offload acceptability，对所有用户生效。不能卸载：UE在E-UTRAN接入时，不能卸载负荷到WLAN。能卸载：UE在E-UTRAN接入时，能卸载负荷到WLAN。
DFTUTRANPOLICY|默认UTRAN策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置UTRAN下默认的WLAN offload acceptability，对所有用户生效。不能卸载：UE在UTRAN接入时，不能卸载负荷到WLAN。能卸载：UE在UTRAN接入时，能卸载负荷到WLAN。
LOCALDFTPRIOR|本地默认优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置本地默认策略和签约同时存在时，给UE下发的能力参数（即WLAN offload acceptability）是签约的还是本地的默认策略。
命令举例 
设置无线辅助WLAN互操作控制开关，MME是否支持RAN-assisted WLAN Interworking为“是”。 
SET WLAN INTERWORKING CONTROL SWITCH:MMESUPRANWLAN="YES"; 
父主题： [无线辅助WLAN互操作控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询无线辅助WLAN互操作控制开关(SHOW WLAN INTERWORKING CONTROL SWITCH) 
#### 查询无线辅助WLAN互操作控制开关(SHOW WLAN INTERWORKING CONTROL SWITCH) 
命令功能 
该命令用于查询WLAN互操作控制开关。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPRANWLAN|MME是否支持RAN-assisted WLAN Interworking|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持RAN辅助的WLAN互操作。这是功能总开关，只有在本功能开关打开时，MME才会根据本地配置或用户签约对WLAN offload acceptability进行控制。不支持：MME不支持RAN辅助的WLAN互操作。支持：MME支持RAN辅助的WLAN互操作。
LOCWLANCTRLSUP|是否支持基于RAN的WLAN互操作的本地控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持RAN辅助的WLAN互操作的本地控制。本地控制通过ADD WLAN INTERWORKING LOCAL POLICY命令配置实现。不支持：MME不支持RAN辅助的WLAN互操作的本地控制，则MME只将用户签约的WLAN offload acceptability下发给UE。支持：MME支持RAN辅助的WLAN互操作的本地控制，则MME下发用户签约或本地配置的WLAN offload acceptability给UE。
INSTANTCHANGE|MME是否支持WLAN负荷卸载能力变化的及时生效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持WLAN offload acceptability变化的即时生效。当用户签约信息变化时，如果只是WLAN offload acceptability变化，为了下发这个信息会增加网络信令负荷，所以增加开关进行控制，由运营商根据网络情况确定是否有必要为此增加系统信令负荷。不支持：MME不支持WLAN offload acceptability变化的即时生效。支持：MME支持WLAN offload acceptability变化的即时生效。
DFTEUTRANPOLICY|默认E-UTRAN策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置E-UTRAN下默认的WLAN offload acceptability，对所有用户生效。不能卸载：UE在E-UTRAN接入时，不能卸载负荷到WLAN。能卸载：UE在E-UTRAN接入时，能卸载负荷到WLAN。
DFTUTRANPOLICY|默认UTRAN策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置UTRAN下默认的WLAN offload acceptability，对所有用户生效。不能卸载：UE在UTRAN接入时，不能卸载负荷到WLAN。能卸载：UE在UTRAN接入时，能卸载负荷到WLAN。
LOCALDFTPRIOR|本地默认优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置本地默认策略和签约同时存在时，给UE下发的能力参数（即WLAN offload acceptability）是签约的还是本地的默认策略。
命令举例 
查询无线辅助WLAN互操作控制开关。 
SHOW WLAN INTERWORKING CONTROL SWITCH 
`
2017-07-12 12:25:18 命令 (No.2): SHOW WLAN INTERWORKING CONTROL SWITCH
操作维护   MME是否支持RAN-assisted WLAN Interworking   是否支持基于RAN的WLAN互操作的本地控制   MME是否支持WLAN负荷卸载能力变化的及时生效   默认E-UTRAN策略   默认UTRAN策略   本地默认优先 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      否                                           否                                      否                                          不能卸载          不能卸载        签约的策略优先于本地默认策略 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.036 秒）。
` 
父主题： [无线辅助WLAN互操作控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 无线辅助WLAN互操作本地策略配置 
### 无线辅助WLAN互操作本地策略配置 
背景知识 
当HSS不支持WLAN负荷卸载功能签约时，或运营商想对漫游用户进行本地控制时，在MME上可根据用户号段和APN信息配置WLAN负荷卸载控制策略。 
功能描述 
            
            本功能主要用于配置本地WLAN负荷卸载能力控制策略，可以基于IMSI和APN进行配置。
        
相关主题 
 
新增无线辅助WLAN互操作本地策略(ADD WLAN INTERWORKING LOCAL POLICY)
 
 
修改无线辅助WLAN互操作本地策略(SET WLAN INTERWORKING LOCAL POLICY)
 
 
删除无线辅助WLAN互操作本地策略(DEL WLAN INTERWORKING LOCAL POLICY)
 
 
查询无线辅助WLAN互操作本地策略(SHOW WLAN INTERWORKING LOCAL POLICY)
 
 
父主题： [WLAN互操作配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增无线辅助WLAN互操作本地策略(ADD WLAN INTERWORKING LOCAL POLICY) 
#### 新增无线辅助WLAN互操作本地策略(ADD WLAN INTERWORKING LOCAL POLICY) 
命令功能 
该命令用于配置基于用户号段和APN的WLAN负荷卸载能力控制策略：是否本地策略优先，本地的E-UTRAN下能力指示和UTRAN下能力指示。当需要本地控制时使用该命令。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于配置用户IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于配置APN。
LOCALPRIOR|本地优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当本地策略和签约同时存在时，给UE下发的能力参数（即WLAN offload acceptability）是签约的还是本地策略的。
EUTRANPOLICY|E-UTRAN下的负荷卸载策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置E-UTRAN下的WLAN负荷卸载策略，即是否可以负荷卸载。当只配置了IMSI参数、未配置APN参数时，如果配置策略为不可以负荷卸载，则表示该号段用户的业务不可以卸载到WLAN。当只配置了APN参数、未配置IMSI参数时，该策略对使用该APN的所有用户生效。当同时配置了IMSI和APN参数时，该策略仅对使用该APN的指定号段用户生效。
UTRANPOLICY|UTRAN下的负荷卸载策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置UTRAN下的WLAN负荷卸载策略，即是否可以负荷卸载。当只配置了IMSI参数、未配置APN参数时，如果配置策略为不可以负荷卸载，则表示该号段用户的业务不可以卸载到WLAN。当只配置了APN参数、未配置IMSI参数时，该策略对使用该APN的所有用户生效。当同时配置了IMSI和APN参数时，该策略仅对使用该APN的指定号段用户生效。
命令举例 
新增无线辅助WLAN互操作本地策略。 
ADD WLAN INTERWORKING LOCAL POLICY:APN="zte",LOCALPRIOR="SUBPLYPRI",EUTRANPOLICY="YES",UTRANPOLICY="YES"; 
父主题： [无线辅助WLAN互操作本地策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改无线辅助WLAN互操作本地策略(SET WLAN INTERWORKING LOCAL POLICY) 
#### 修改无线辅助WLAN互操作本地策略(SET WLAN INTERWORKING LOCAL POLICY) 
命令功能 
该命令用于修改基于用户号段和APN的WLAN负荷卸载能力控制策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于配置用户IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于配置APN。
LOCALPRIOR|本地优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当本地策略和签约同时存在时，给UE下发的能力参数（即WLAN offload acceptability）是签约的还是本地策略的。
EUTRANPOLICY|E-UTRAN下的负荷卸载策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置E-UTRAN下的WLAN负荷卸载策略，即是否可以负荷卸载。当只配置了IMSI参数、未配置APN参数时，如果配置策略为不可以负荷卸载，则表示该号段用户的业务不可以卸载到WLAN。当只配置了APN参数、未配置IMSI参数时，该策略对使用该APN的所有用户生效。当同时配置了IMSI和APN参数时，该策略仅对使用该APN的指定号段用户生效。
UTRANPOLICY|UTRAN下的负荷卸载策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置UTRAN下的WLAN负荷卸载策略，即是否可以负荷卸载。当只配置了IMSI参数、未配置APN参数时，如果配置策略为不可以负荷卸载，则表示该号段用户的业务不可以卸载到WLAN。当只配置了APN参数、未配置IMSI参数时，该策略对使用该APN的所有用户生效。当同时配置了IMSI和APN参数时，该策略仅对使用该APN的指定号段用户生效。
命令举例 
修改无线辅助WLAN互操作本地策略。 
SET WLAN INTERWORKING LOCAL POLICY:APN="zte",LOCALPRIOR="LOCPLYPRI"; 
父主题： [无线辅助WLAN互操作本地策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除无线辅助WLAN互操作本地策略(DEL WLAN INTERWORKING LOCAL POLICY) 
#### 删除无线辅助WLAN互操作本地策略(DEL WLAN INTERWORKING LOCAL POLICY) 
命令功能 
该命令用于删除基于用户号段和APN的WLAN负荷卸载能力控制策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于配置用户IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于配置APN。
命令举例 
删除无线辅助WLAN互操作本地策略。 
DEL WLAN INTERWORKING LOCAL POLICY:APN="zte"; 
父主题： [无线辅助WLAN互操作本地策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询无线辅助WLAN互操作本地策略(SHOW WLAN INTERWORKING LOCAL POLICY) 
#### 查询无线辅助WLAN互操作本地策略(SHOW WLAN INTERWORKING LOCAL POLICY) 
命令功能 
该命令用于查询基于用户号段和APN的WLAN负荷卸载能力控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于配置用户IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于配置APN。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于配置用户IMSI号段。
APN|APN|参数可选性:任选参数；参数类型:字符型。|该参数用于配置APN。
LOCALPRIOR|本地优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当本地策略和签约同时存在时，给UE下发的能力参数（即WLAN offload acceptability）是签约的还是本地策略的。
EUTRANPOLICY|E-UTRAN下的负荷卸载策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置E-UTRAN下的WLAN负荷卸载策略，即是否可以负荷卸载。当只配置了IMSI参数、未配置APN参数时，如果配置策略为不可以负荷卸载，则表示该号段用户的业务不可以卸载到WLAN。当只配置了APN参数、未配置IMSI参数时，该策略对使用该APN的所有用户生效。当同时配置了IMSI和APN参数时，该策略仅对使用该APN的指定号段用户生效。
UTRANPOLICY|UTRAN下的负荷卸载策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置UTRAN下的WLAN负荷卸载策略，即是否可以负荷卸载。当只配置了IMSI参数、未配置APN参数时，如果配置策略为不可以负荷卸载，则表示该号段用户的业务不可以卸载到WLAN。当只配置了APN参数、未配置IMSI参数时，该策略对使用该APN的所有用户生效。当同时配置了IMSI和APN参数时，该策略仅对使用该APN的指定号段用户生效。
命令举例 
查询无线辅助WLAN互操作本地策略。 
SHOW WLAN INTERWORKING LOCAL POLICY 
`
2017-07-12 12:38:27 命令 (No.7): SHOW WLAN INTERWORKING LOCAL POLICY;
操作维护        IMSI   APN   本地优先                        E-UTRAN下的负荷卸载策略   UTRAN下的负荷卸载策略 
------------------------------------------------------------------------------------------------------------
复制 修改 删除         zte   本地策略优先于签约策略          支持                      支持 
------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [无线辅助WLAN互操作本地策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 失败原因值映射配置 
# 失败原因值映射配置 
背景知识 
用户在EPC网络下进行VoLTE语音呼叫，移动到3G网络覆盖时，可通过SRVCC切换功能切换到3G的CS网络，保证呼叫不中断。 
S1口为MME与eNodeB之间接口。 
Sv口为MME与MSC之间接口。 
功能描述 
            
            在SRVCC切换中，由于UE、eNodeB、MME或MSC网元原因，最终切换取消，MME发送给eNodeB或MSC网元切换取消消息，本功能模块可配置其中的原因值。
        
相关主题 
 
S1到Sv口切换取消原因映射配置
 
 
Sv到S1口切换失败原因映射配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## S1到Sv口切换取消原因映射配置 
## S1到Sv口切换取消原因映射配置 
背景知识 
用户在EPC网络下进行VoLTE语音呼叫，移动到3G网络覆盖区域时，可通过SRVCC切换功能切换到3G的CS网络，保证呼叫不中断。 
S1口为MME与eNodeB之间接口。 
Sv口为MME与MSC之间接口。 
功能描述 
            
            在SRVCC切换中，由于eNodeB触发切换取消或流程失败，MME将切换取消原因通知MSC。本功能模块可基于eNodeB上报的切换取消原因值或流程失败场景，映射得到Sv口的原因值，在发送给MSC的切换取消消息中携带。
        
相关主题 
 
设置S1到Sv口切换取消原因映射配置(SET SVHOFFCAUSE)
 
 
查询S1到Sv口切换取消原因映射配置(SHOW SVHOFFCAUSE)
 
 
父主题： [失败原因值映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置S1到Sv口切换取消原因映射配置(SET SVHOFFCAUSE) 
### 设置S1到Sv口切换取消原因映射配置(SET SVHOFFCAUSE) 
命令功能 
该命令用于设置S1口切换取消原因值或流程失败场景与Sv口切换取消的原因值的对应关系，MME发送Sv口切换取消消息时，基于S1口切换取消原因值或流程失败场景获得Sv口的原因值，在Sv口切换取消中携带。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
S1APCAUSE|S1AP切换取消原因|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示S1口切换取消原因或SRVCC切换失败场景。 枚举值：RNL:UnspecifiedRNL:TS1RELOCprep ExpiryRNL:Cell not availableRNL:Radio Connection With UE LostRNL:Failure in the Radio Interface Procedure流程冲突导致等待PS to CS Respond响应超时处理PS to CS Respond响应失败收到S1释放
GTPCAUSE|Sv切换取消原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示Sv口切换取消原因。 枚举值：UnspecifiedHandover/Relocation cancelled by source systemHandover /Relocation Failure with Target systemHandover/Relocation Target not allowedTarget Cell not availableNo Radio Resources Available in Target CellFailure in Radio Interface ProcedurePermanent session leg establishment errorTemporary session leg establishment error
命令举例 
设置S1口切换取消原因“RNL:Cell not available”与Sv口切换取消原因“Handover/Relocation Target not allowed ”对应。 
SET SVHOFFCAUSE:S1APCAUSE="CELLNOAVAIL",GTPCAUSE="HORELONOALLOW"; 
父主题： [S1到Sv口切换取消原因映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询S1到Sv口切换取消原因映射配置(SHOW SVHOFFCAUSE) 
### 查询S1到Sv口切换取消原因映射配置(SHOW SVHOFFCAUSE) 
命令功能 
该命令用于查询S1口切换取消原因值或流程失败场景与Sv口切换取消的原因值的对应关系。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
S1APCAUSE|S1AP切换取消原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示S1口切换取消原因或SRVCC切换失败场景。 枚举值：RNL:UnspecifiedRNL:TS1RELOCprep ExpiryRNL:Cell not availableRNL:Radio Connection With UE LostRNL:Failure in the Radio Interface Procedure流程冲突导致等待PS to CS Respond响应超时处理PS to CS Respond响应失败收到S1释放
输出参数说明 
标识|名称|类型|说明
---|---|---|---
S1APCAUSE|S1AP切换取消原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示S1口切换取消原因或SRVCC切换失败场景。 枚举值：RNL:UnspecifiedRNL:TS1RELOCprep ExpiryRNL:Cell not availableRNL:Radio Connection With UE LostRNL:Failure in the Radio Interface Procedure流程冲突导致等待PS to CS Respond响应超时处理PS to CS Respond响应失败收到S1释放
GTPCAUSE|Sv切换取消原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示Sv口切换取消原因。 枚举值：UnspecifiedHandover/Relocation cancelled by source systemHandover /Relocation Failure with Target systemHandover/Relocation Target not allowedTarget Cell not availableNo Radio Resources Available in Target CellFailure in Radio Interface ProcedurePermanent session leg establishment errorTemporary session leg establishment error
命令举例 
查询S1口切换取消原因“RNL:Cell not available”对应的Sv口切换取消原因值。 
SHOW SVHOFFCAUSE:S1APCAUSE="CELLNOAVAIL"; 
`
命令 (No.1): SHOW SVHOFFCAUSE:S1APCAUSE="CELLNOAVAIL";
操作维护  S1AP切换取消原因                               Sv切换取消原因
-----------------------------------------------------------------------
修改      RNL:Cell not available                         Handover/Relocation cancelled by source system
-----------------------------------------------------------------------
记录数 1
命令执行成功（耗时 18.37 秒）。
` 
父主题： [S1到Sv口切换取消原因映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## Sv到S1口切换失败原因映射配置 
## Sv到S1口切换失败原因映射配置 
背景知识 
用户在EPC网络下进行VoLTE语音呼叫，移动到3G网络覆盖区域时，可通过SRVCC切换功能切换到3G的CS网络，保证呼叫不中断。 
S1口为MME与eNodeB之间接口。 
Sv口为MME与MSC之间接口。 
功能描述 
            
            在SRVCC切换中，由于MSC触发切换取消或流程失败，MME将切换取消原因通知eNodeB。本功能模块可基于MSC上报的切换取消原因值或流程失败场景，映射得到S1口的原因值，在MME发送给eNodeB的切换取消消息中携带。
        
相关主题 
 
设置Sv到S1口切换失败原因映射配置(SET SVTOS1CAUSE)
 
 
查询Sv到S1口切换失败原因映射配置(SHOW SVTOS1CAUSE)
 
 
父主题： [失败原因值映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置Sv到S1口切换失败原因映射配置(SET SVTOS1CAUSE) 
### 设置Sv到S1口切换失败原因映射配置(SET SVTOS1CAUSE) 
命令功能 
该命令用于设置Sv口切换取消原因值或流程失败场景与S1口切换取消的原因值的对应关系。MME发送S1口切换取消消息时，基于Sv口切换取消原因值或流程失败场景获得S1口的原因值，在S1口切换取消消息中携带该原因值。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPCAUSE|Sv切换失败原因|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示Sv口切换取消原因。 枚举值：UnspecifiedHandover/Relocation cancelled by source systemHandover /Relocation Failure with Target systemHandover/Relocation Target not allowedTarget Cell not availableNo Radio Resources Available in Target CellFailure in Radio Interface ProcedurePermanent session leg establishment errorTemporary session leg establishment error流程冲突导致与CSFB流程冲突等待PS to CS Respond响应超时查找切换目标失败收到S1释放切换限制用户CSG信息无效CSGID无效
S1APCASUE|S1AP切换失败原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示S1口切换取消原因或SRVCC切换失败场景。 枚举值：RNL:UnspecifiedRNL: Release due to E-UTRAN Generated ReasonRNL: Handover Failure In Target EPC/eNB Or Target SystemRNL: Handover Target not allowedRNL: Cell not availableRNL: Unknown Target IDRNL: No Radio Resources Available in Target CellRNL: CS Fallback TriggeredRNL: Failure in the Radio Interface ProcedureRNL: Interaction with other procedureRNL: invalid CSG IdNAS: CSG Subscription ExpiryPC: Message not compatible with Receiver StatePC: Unspecified
命令举例 
设置Sv口切换取消原因“Handover/Relocation Target not allowed ”与S1口切换取消原因“RNL:Cell not available”对应。 
SET SVTOS1CAUSE:GTPCAUSE="HORELOCNOALLOW",S1APCASUE="CELLNOAVAIL"; 
父主题： [Sv到S1口切换失败原因映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询Sv到S1口切换失败原因映射配置(SHOW SVTOS1CAUSE) 
### 查询Sv到S1口切换失败原因映射配置(SHOW SVTOS1CAUSE) 
命令功能 
该命令用于查询Sv口切换取消原因值或流程失败场景与S1口切换取消的原因值的对应关系。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPCAUSE|Sv切换失败原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示Sv口切换取消原因。 枚举值：UnspecifiedHandover/Relocation cancelled by source systemHandover /Relocation Failure with Target systemHandover/Relocation Target not allowedTarget Cell not availableNo Radio Resources Available in Target CellFailure in Radio Interface ProcedurePermanent session leg establishment errorTemporary session leg establishment error流程冲突导致与CSFB流程冲突等待PS to CS Respond响应超时查找切换目标失败收到S1释放切换限制用户CSG信息无效CSGID无效
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GTPCAUSE|Sv切换失败原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示Sv口切换取消原因。 枚举值：UnspecifiedHandover/Relocation cancelled by source systemHandover /Relocation Failure with Target systemHandover/Relocation Target not allowedTarget Cell not availableNo Radio Resources Available in Target CellFailure in Radio Interface ProcedurePermanent session leg establishment errorTemporary session leg establishment error流程冲突导致与CSFB流程冲突等待PS to CS Respond响应超时查找切换目标失败收到S1释放切换限制用户CSG信息无效CSGID无效
S1APCASUE|S1AP切换失败原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示S1口切换取消原因或SRVCC切换失败场景。 枚举值：RNL:UnspecifiedRNL: Release due to E-UTRAN Generated ReasonRNL: Handover Failure In Target EPC/eNB Or Target SystemRNL: Handover Target not allowedRNL: Cell not availableRNL: Unknown Target IDRNL: No Radio Resources Available in Target CellRNL: CS Fallback TriggeredRNL: Failure in the Radio Interface ProcedureRNL: Interaction with other procedureRNL: invalid CSG IdNAS: CSG Subscription ExpiryPC: Message not compatible with Receiver StatePC: Unspecified
命令举例 
查询Sv口切换取消原因“Handover/Relocation Target not allowed ”所对应的S1口切换取消原因值。 
SHOW SVTOS1CAUSE:GTPCAUSE="HORELOCNOALLOW"; 
`
命令 (No.1): SHOW SVTOS1CAUSE:GTPCAUSE="HORELOCNOALLOW";
操作维护  Sv切换失败原因                                   S1AP切换失败原因
---------------------------------------------------------------------------
修改      Handover/Relocation Target not allowed           RNL: Handover Failure In Target EPC/eNB Or Target System
---------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 1.584 秒）。
` 
父主题： [Sv到S1口切换失败原因映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MPS配置 
# MPS配置 
背景知识 
MPS（Multimedia Priority Service）是一种端到端的多媒体优先级业务。MPS能够允许授权的“业务用户”在网络发生拥塞、会话建立受阻时，获取优先于其他用户的无线信道接入权利，能够优先发起、修改、保持、释放会话以及投递媒体报文。 
功能描述 
本功能模块可控制MME网元中MPS功能相关开关，例如是否启用MPS功能、是否检查MPS签约、MO CSFB高优先级判断方式等。 
同时可设置承载的ARP及VLR下发的eMLPP对应的寻呼优先级。 
相关主题 
 
MPS功能开关配置
 
 
ARP优先级到S1口寻呼优先级映射配置
 
 
eMLPP优先级到S1口寻呼优先级映射配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MPS功能开关配置 
## MPS功能开关配置 
背景知识 
MPS被应用于PS域以及IMS域的语音、视频和数据承载业务。所涉及到的包括特殊Access Class的USIM、HSS签约、EPS承载优先业务、IMS优先业务、CSFB优先业务、空口优先级接入等。 
功能描述 
本功能模块可控制MME是否启用MPS功能，以及启用MPS功能后，检查用户是否签约MPS业务，同时可配置拒绝无MPS权限的用户使用MPS业务使用的原因值。 
相关主题 
 
设置MPS功能开关(SET MPSCFG)
 
 
查询MPS功能开关(SHOW MPSCFG)
 
 
父主题： [MPS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置MPS功能开关(SET MPSCFG) 
### 设置MPS功能开关(SET MPSCFG) 
命令功能 
该命令用于设置MME是否启用MPS功能、设置MME是否检查用户MPS签约、设置MME判断MO CSFB是否为高优先级的方式、设置MME拒绝用户进行MPS业务时使用的原因值。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MPSFUNCSWITCH|是否支持MPS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否启用MPS功能。
MPSCHECKFAILSTYLE|是否允许非MPS高优先级用户进行高优先级接入|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置高优先级接入时是否检查用户MPS签约情况。是：用户采用高优先级方式接入，用户未签约MPS能力，则MME拒绝用户接入。否：即使用户未签约MPS能力，用户采用高优先级方式接时，MME也允许用户接入。
HIGHCSFBMO|高优先级CSFB起呼判断方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置如何判断MO CSFB为高优先级。MME可用以下两种方式判断。用户采用高优先级接入方式触发MO CSFB，同时用户签约了MPS能力，则MME认为为高优先级的MO CSFB。用户采用高优先级接入方式触发MO CSFB，或者用户签约了MPS能力，则MME认为为高优先级的MO CSFB。
CAUSE|拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置拒绝进行MPS业务时使用的原因值。
命令举例 
设置MPS功能开关，是否支持MPS功能为“不支持”，是否允许非MPS高优先级用户进行高优先级接入为“是”，高优先级CSFB起呼判断方式为“高优先级接入或签约MPS CS优先级”，拒绝原因值为“EPS业务不允许”。 
SET MPSCFG:MPSFUNCSWITCH="NO",MPSCHECKFAILSTYLE="YES",HIGHCSFBMO="HIGHPRIORITY_OR_MPSCS",CAUSE="EPSNOTALLOW"; 
父主题： [MPS功能开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询MPS功能开关(SHOW MPSCFG) 
### 查询MPS功能开关(SHOW MPSCFG) 
命令功能 
该命令用于查询MPS功能各项开关的应用情况。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MPSFUNCSWITCH|是否支持MPS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否启用MPS功能。
MPSCHECKFAILSTYLE|是否允许非MPS高优先级用户进行高优先级接入|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置高优先级接入时是否检查用户MPS签约情况。是：用户采用高优先级方式接入，用户未签约MPS能力，则MME拒绝用户接入。否：即使用户未签约MPS能力，用户采用高优先级方式接时，MME也允许用户接入。
HIGHCSFBMO|高优先级CSFB起呼判断方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置如何判断MO CSFB为高优先级。MME可用以下两种方式判断。用户采用高优先级接入方式触发MO CSFB，同时用户签约了MPS能力，则MME认为为高优先级的MO CSFB。用户采用高优先级接入方式触发MO CSFB，或者用户签约了MPS能力，则MME认为为高优先级的MO CSFB。
CAUSE|拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置拒绝进行MPS业务时使用的原因值。
命令举例 
查询MPS功能开关。 
SHOW MPSCFG; 
`
命令 (No.8): SHOW MPSCFG;
操作维护  是否支持MPS功能   是否允许非MPS高优先级用户进行高优先级接入   高优先级CSFB起呼判断方式         拒绝原因值
-------------------------------------------------------------------------------------------------------------------
修改      不支持            是                                          高优先级接入或签约MPS CS优先级   EPS业务不允许
-------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [MPS功能开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## ARP优先级到S1口寻呼优先级映射配置 
## ARP优先级到S1口寻呼优先级映射配置 
背景知识 
PGW网元对用户发起创建承载、更新承载或DDN请求时，会发送消息通知到MME网元。当用户为空闲态时，MME可按照ARP优先级寻呼方式对用户按寻呼优先级进行寻呼。 
MME的ARP优先级寻呼方式为：PGW需要创建/修改的承载、DDN请求恢复的承载中携带ARP优先级，MME根据该ARP来确定对应的寻呼优先级，在发送给eNodeB的寻呼消息中携带该寻呼优先级。eNodeB对寻呼优先级高的用户优先寻呼。 
功能描述 
本功能模块可配置ARP优先级对应的寻呼优先级，未配置的ARP则认为不支持MPS功能。 
相关主题 
 
新增ARP优先级到S1口寻呼优先级映射(ADD ARP S1PAGE PRI)
 
 
修改ARP优先级到S1口寻呼优先级映射(SET ARP S1PAGE PRI)
 
 
删除ARP优先级到S1口寻呼优先级映射(DEL ARP S1PAGE PRI)
 
 
查询ARP优先级到S1口寻呼优先级映射(SHOW ARP S1PAGE PRI)
 
 
父主题： [MPS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增ARP优先级到S1口寻呼优先级映射(ADD ARP S1PAGE PRI) 
### 新增ARP优先级到S1口寻呼优先级映射(ADD ARP S1PAGE PRI) 
命令功能 
该命令用于新增ARP优先级对应的寻呼优先级。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ARPPRIORITY|ARP优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置ARP优先级的取值。ARP优先级数值越小，代表优先级越高。
S1PAGEPRIORITY|S1寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置ARP优先级数值对应的寻呼优先级。寻呼优先级数值越小，代表优先级越高。PGW需要创建/修改的承载、DDN请求恢复的承载中携带ARP优先级，MME根据该ARP来确定对应的寻呼优先级，在发送给eNodeB的寻呼消息中携带该寻呼优先级。eNodeB对寻呼优先级高的用户优先寻呼。
命令举例 
新增ARP优先级到S1口寻呼优先级映射，ARP优先级为1，S1寻呼优先级为0。 
ADD ARP S1PAGE PRI:ARPPRIORITY=1,S1PAGEPRIORITY=0; 
父主题： [ARP优先级到S1口寻呼优先级映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改ARP优先级到S1口寻呼优先级映射(SET ARP S1PAGE PRI) 
### 修改ARP优先级到S1口寻呼优先级映射(SET ARP S1PAGE PRI) 
命令功能 
该命令用于设置ARP优先级对应的寻呼优先级。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ARPPRIORITY|ARP优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置ARP优先级的取值。ARP优先级数值越小，代表优先级越高。
S1PAGEPRIORITY|S1寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置ARP优先级数值对应的寻呼优先级。寻呼优先级数值越小，代表优先级越高。PGW需要创建/修改的承载、DDN请求恢复的承载中携带ARP优先级，MME根据该ARP来确定对应的寻呼优先级，在发送给eNodeB的寻呼消息中携带该寻呼优先级。eNodeB对寻呼优先级高的用户优先寻呼。
命令举例 
修改ARP优先级到S1口寻呼优先级映射，ARP优先级为1，S1寻呼优先级为0。 
SET ARP S1PAGE PRI:ARPPRIORITY=1,S1PAGEPRIORITY=0; 
父主题： [ARP优先级到S1口寻呼优先级映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除ARP优先级到S1口寻呼优先级映射(DEL ARP S1PAGE PRI) 
### 删除ARP优先级到S1口寻呼优先级映射(DEL ARP S1PAGE PRI) 
命令功能 
该命令用于删除ARP优先级记录，删除后则此ARP优先级不启用MPS功能，无对应的寻呼优先级。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ARPPRIORITY|ARP优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置ARP优先级的取值。ARP优先级数值越小，代表优先级越高。
命令举例 
删除ARP优先级到S1口寻呼优先级映射，ARP优先级为1的记录。 
DEL ARP S1PAGE PRI:ARPPRIORITY=1; 
父主题： [ARP优先级到S1口寻呼优先级映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询ARP优先级到S1口寻呼优先级映射(SHOW ARP S1PAGE PRI) 
### 查询ARP优先级到S1口寻呼优先级映射(SHOW ARP S1PAGE PRI) 
命令功能 
该命令用于查询ARP优先级对应的寻呼优先级。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ARPPRIORITY|ARP优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置ARP优先级的取值。ARP优先级数值越小，代表优先级越高。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ARPPRIORITY|ARP优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置ARP优先级的取值。ARP优先级数值越小，代表优先级越高。
S1PAGEPRIORITY|S1寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置ARP优先级数值对应的寻呼优先级。寻呼优先级数值越小，代表优先级越高。PGW需要创建/修改的承载、DDN请求恢复的承载中携带ARP优先级，MME根据该ARP来确定对应的寻呼优先级，在发送给eNodeB的寻呼消息中携带该寻呼优先级。eNodeB对寻呼优先级高的用户优先寻呼。
命令举例 
查询ARP优先级到S1口寻呼优先级映射。 
SHOW ARP S1PAGE PRI; 
`
命令 (No.1): SHOW ARP S1PAGE PRI
操作维护         ARP优先级   S1寻呼优先级
-----------------------------------------
复制 修改 删除   1           0
-----------------------------------------
记录数 1
命令执行成功（耗时 0.062 秒）。
` 
父主题： [ARP优先级到S1口寻呼优先级映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## eMLPP优先级到S1口寻呼优先级映射配置 
## eMLPP优先级到S1口寻呼优先级映射配置 
背景知识 
VLR对某些用户发起CSFB MT寻呼，并发送消息通知到MME。当用户处于空闲态时，MME可通过eMLPP优先级寻呼方式对用户按寻呼优先级进行寻呼。 
MME的eMLPP优先级寻呼方式为：MME基于VLR发送的消息中携带的eMLPP取值，来确定寻呼优先级，将此寻呼优先级在寻呼消息中携带给eNodeB。eNodeB对寻呼优先级高的用户优先寻呼。 
功能描述 
本功能模块可配置eMLPP对应的寻呼优先级，未配置的eMLPP则认为不支持MPS功能。 
相关主题 
 
新增eMLPP优先级到S1口寻呼优先级映射(ADD EMLPP S1PAGE PRI)
 
 
修改eMLPP优先级到S1口寻呼优先级映射(SET EMLPP S1PAGE PRI)
 
 
删除eMLPP优先级到S1口寻呼优先级映射(DEL EMLPP S1PAGE PRI)
 
 
查询eMLPP优先级到S1口寻呼优先级映射(SHOW EMLPP S1PAGE PRI)
 
 
父主题： [MPS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增eMLPP优先级到S1口寻呼优先级映射(ADD EMLPP S1PAGE PRI) 
### 新增eMLPP优先级到S1口寻呼优先级映射(ADD EMLPP S1PAGE PRI) 
命令功能 
该命令用于新增eMLPP对应的寻呼优先级。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
EMLPPPRIORITY|eMLPP优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置eMLPP的取值，数值越大表示优先级越高。
S1PAGEPRIORITY|S1寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置eMLPP取值对应的寻呼优先级。寻呼优先级数值越小，代表优先级越高。VLR发送给MME的寻呼消息中携带eMLPP时，MME根据eMLPP来确定对应的寻呼优先级，在发送给eNodeB的寻呼消息中携带该寻呼优先级。eNodeB对寻呼优先级高的用户优先寻呼。
命令举例 
新增eMLPP优先级到S1口寻呼优先级映射，eMLPP优先级为1，S1寻呼优先级为0。 
ADD EMLPP S1PAGE PRI:EMLPPPRIORITY=1,S1PAGEPRIORITY=0; 
父主题： [eMLPP优先级到S1口寻呼优先级映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改eMLPP优先级到S1口寻呼优先级映射(SET EMLPP S1PAGE PRI) 
### 修改eMLPP优先级到S1口寻呼优先级映射(SET EMLPP S1PAGE PRI) 
命令功能 
该命令用于设置eMLPP对应的寻呼优先级。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
EMLPPPRIORITY|eMLPP优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置eMLPP的取值，数值越大表示优先级越高。
S1PAGEPRIORITY|S1寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置eMLPP取值对应的寻呼优先级。寻呼优先级数值越小，代表优先级越高。VLR发送给MME的寻呼消息中携带eMLPP时，MME根据eMLPP来确定对应的寻呼优先级，在发送给eNodeB的寻呼消息中携带该寻呼优先级。eNodeB对寻呼优先级高的用户优先寻呼。
命令举例 
修改eMLPP优先级到S1口寻呼优先级映射，eMLPP优先级为1，S1寻呼优先级为0。 
SET EMLPP S1PAGE PRI:EMLPPPRIORITY=1,S1PAGEPRIORITY=0; 
父主题： [eMLPP优先级到S1口寻呼优先级映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除eMLPP优先级到S1口寻呼优先级映射(DEL EMLPP S1PAGE PRI) 
### 删除eMLPP优先级到S1口寻呼优先级映射(DEL EMLPP S1PAGE PRI) 
命令功能 
该命令用于删除eMLPP记录，删除后则此eMLPP不启用MPS功能，无对应的寻呼优先级。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
EMLPPPRIORITY|eMLPP优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置eMLPP的取值，数值越大表示优先级越高。
命令举例 
删除eMLPP优先级到S1口寻呼优先级映射，ARP优先级为1的记录。 
DEL EMLPP S1PAGE PRI:EMLPPPRIORITY=1; 
父主题： [eMLPP优先级到S1口寻呼优先级映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询eMLPP优先级到S1口寻呼优先级映射(SHOW EMLPP S1PAGE PRI) 
### 查询eMLPP优先级到S1口寻呼优先级映射(SHOW EMLPP S1PAGE PRI) 
命令功能 
该命令用于查询eMLPP对应的寻呼优先级。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
EMLPPPRIORITY|eMLPP优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置eMLPP的取值，数值越大表示优先级越高。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
EMLPPPRIORITY|eMLPP优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置eMLPP的取值，数值越大表示优先级越高。
S1PAGEPRIORITY|S1寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置eMLPP取值对应的寻呼优先级。寻呼优先级数值越小，代表优先级越高。VLR发送给MME的寻呼消息中携带eMLPP时，MME根据eMLPP来确定对应的寻呼优先级，在发送给eNodeB的寻呼消息中携带该寻呼优先级。eNodeB对寻呼优先级高的用户优先寻呼。
命令举例 
查询eMLPP优先级到S1口寻呼优先级映射。 
SHOW EMLPP S1PAGE PRI; 
`
命令 (No.1): SHOW EMLPP S1PAGE PRI
操作维护         eMLPP优先级   S1寻呼优先级
-------------------------------------------
复制 修改 删除   1             0
-------------------------------------------
记录数 1
命令执行成功（耗时 0.05 秒）。
` 
父主题： [eMLPP优先级到S1口寻呼优先级映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 基于IMEI限制DT配置 
# 基于IMEI限制DT配置 
背景知识 
 
在具有DT能力的SGSN中，能配置每个RNC和每个GGSN是否支持直接用户面连接。SGSN处理控制面信令并决策何时建立直传隧道。
 
 
在使用DT的情况下，GGSN收到RNC的用户面ERROR INDICATION消息时，需要给SGSN发更新消息Update PDP Context Request，指示SGSN释放对应的RAB资源。
 
 
在使用DT的情况下，RNC收到GGSN的用户面ERROR INDICATION消息时，需要给SGSN发RAB释放消息RAB Release Request，SGSN直接去激活PDP上下文。
 
 
功能描述 
通过IMEI，可以识别终端类型。有一些终端类型，业务请求和Iu释放极其频繁，对SGSN和GGSN负荷具有较大的影响，需要限制其建立DT。 
配置支持DT功能的流程如下： 
                        配置RNC支持DT，通过RNC局向附加属性中配置支持DT功能，配置命令参见：
                        [ADD RNC]
                        。
                    
配置GGSN支持DT，有如下两种方式： 
 
                                本地根据APN进行配置，使用GPRS APN HOST配置（
                                ADD GPRS APN
                                ）或EPC APN HOST配置（
                                ADD EPC APN
                                ）或DNS解析类APN配置（
                                ADD DNSAPNCHG
                                ）。
                            
 
 
                                本地根据GGSN的IP地址配置，配置命令为：
                                ADD DT IP
                                。
                            
 
 
                        如果需要根据终端类型限制DT，先明确终端类型对应的IMEI号段，通过基于IMEI号段限制DT功能，配置命令参见：
                        [ADD LIMIT DT IMEI]
                        。
                    
注意事项： 
 
SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。
 
 
软件参数“DT话单控制”（ID：786523），控制是否产生DT话单，该软件参数取值为0，则不产生无流量的DT话单（not generate no volume DT CDR）；取值为1，则产生DT话单（generate DT CDR）；取值为2，则不产生DT话单（not generagte DT CDR）。
 
 
软件参数“DT切换频次”（ID：786527），除SGSN首次建立DT外，控制SGSN建立DT的切换频次。该软件参数取值为0，则总是允许；取值为1-254，则第N+1次允许（allow once for every N+1 times）；取值为255，则总是不允许。
 
 
软件参数“CAMEL用户是否允许隧道直传”（ID：786546），控制CAMEL用户是否允许DT功能。该软件参数取值为0，则不允许CAMEL用户隧道直传；取值为1，则允许CAMEL用户隧道直传。
 
 
相关主题 
 
设置基于IMEI限制DT(SET DT LIMITATION BASED IMEI)
 
 
查询基于IMEI限制DT(SHOW DT LIMITATION BASED IMEI)
 
 
新增限制DT的IMEI号段(ADD LIMIT DT IMEI)
 
 
删除限制DT的IMEI号段(DEL LIMIT DT IMEI)
 
 
查询限制DT的IMEI号段(SHOW LIMIT DT IMEI)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置基于IMEI限制DT(SET DT LIMITATION BASED IMEI) 
## 设置基于IMEI限制DT(SET DT LIMITATION BASED IMEI) 
命令功能 
该命令用于设置基于IMEI号段限制DT功能的开关配置。当需要开启或关闭基于IMEI号段限制DT功能时使用该命令。使用该命令开启或关闭基于IMEI号段限制DT后，基于IMEI号段限制DT的功能生效或不生效。 
注意事项 
SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMEIDTCTRL|基于IMEI限制DT|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGSN是否支持基于IMEI限制DT。取值如下：不开启：SGSN不支持基于IMEI限制DT。开启：SGSN支持基于IMEI限制DT。
命令举例 
设置基于IMEI号段限制DT功能开启。 
SET DT LIMITATION BASED IMEI:IMEIDTCTRL="ENABLE"; 
父主题： [基于IMEI限制DT配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询基于IMEI限制DT(SHOW DT LIMITATION BASED IMEI) 
## 查询基于IMEI限制DT(SHOW DT LIMITATION BASED IMEI) 
命令功能 
该命令用于查询基于IMEI号段限制DT功能的开关配置。当需要查询基于IMEI号段限制DT功能的开关是否开启时使用该命令。 
注意事项 
SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMEIDTCTRL|基于IMEI限制DT|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示SGSN是否支持基于IMEI限制DT。取值如下：不开启：SGSN不支持基于IMEI限制DT。开启：SGSN支持基于IMEI限制DT。
命令举例 
查询基于IMEI号段限制DT功能是否开启。 
SHOW DT LIMITATION BASED IMEI; 
`
命令 (No.3): SHOW DT LIMITATION BASED IMEI
操作维护  基于IMEI限制DT
------------------------
修改      开启
------------------------
记录数 1
命令执行成功（耗时 0.102 秒）。
` 
父主题： [基于IMEI限制DT配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增限制DT的IMEI号段(ADD LIMIT DT IMEI) 
## 新增限制DT的IMEI号段(ADD LIMIT DT IMEI) 
命令功能 
该命令用于新增限制DT的IMEI号段配置。当需要新增限制DT的IMEI号段时使用该命令。使用该命令新增IMEI号段成功后，在该IMEI号段的用户不允许使用DT。 
注意事项 
SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~14个字符。|该参数用于指示IMEI（International Mobile station Equipment Identity，国际移动设备标识）。该参数是区别终端的标志，使用0～9的数字，且总长度不超过15位。
命令举例 
新增限制DT的IMEI号段配置，设置IMEI号段为8250。 
ADD LIMIT DT IMEI:IMEI="8250"; 
父主题： [基于IMEI限制DT配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除限制DT的IMEI号段(DEL LIMIT DT IMEI) 
## 删除限制DT的IMEI号段(DEL LIMIT DT IMEI) 
命令功能 
该命令用于删除限制DT的IMEI号段配置。当需要删除限制DT的IMEI号段配置时使用该命令。使用该命令删除IMEI号段成功后，被删除IMEI号段对应的用户也可以建立DT。 
注意事项 
SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~14个字符。|该参数用于指示IMEI（International Mobile station Equipment Identity，国际移动设备标识）。该参数是区别终端的标志，使用0～9的数字，且总长度不超过15位。
命令举例 
删除限制DT的IMEI号段配置，删除的IMEI号段为8250。 
DEL LIMIT DT IMEI:IMEI="8250"; 
父主题： [基于IMEI限制DT配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询限制DT的IMEI号段(SHOW LIMIT DT IMEI) 
## 查询限制DT的IMEI号段(SHOW LIMIT DT IMEI) 
命令功能 
该命令用于查询限制DT的IMEI号段配置。 
注意事项 
SGSN支持DT功能需要License支持，对应的License项为“支持DT功能”。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~14个字符。|该参数用于指示IMEI（International Mobile station Equipment Identity，国际移动设备标识）。该参数是区别终端的标志，使用0～9的数字，且总长度不超过15位。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:任选参数；参数类型:字符型。|该参数用于指示IMEI（International Mobile station Equipment Identity，国际移动设备标识）。该参数是区别终端的标志，使用0～9的数字，且总长度不超过15位。
命令举例 
查询限制DT的IMEI号段配置。 
SHOW LIMIT DT IMEI; 
`
命令 (No.5): SHOW LIMIT DT IMEI
操作维护    IMEI号段
--------------------
复制 删除   8250
--------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [基于IMEI限制DT配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN消息参数配置 
# SGSN消息参数配置 
背景知识 
SGSN中，对每个PDP上下文，需要提供QoS（Quality of Service，服务质量）。 
QoS参数在各个协议版本中不尽相同，各个协议版本的QoS差异如下： 
 
R99版本QoS：长度为11个字节，MBR和GBR的最大值为8.6Mbps。
 
 
R5版本QoS：长度为12个字节，相比较R99版本QoS版本，增加了Signaling Indicating和Source statistics descriptor字段。
 
 
R6版本QoS：长度为14个字节，相比较R5版本QoS，下行MBR和GBR最大值扩大到了16Mbps。
 
 
R7版本QoS：长度为16个字节，相比较R6版本QoS，上下行MBR和GBR最大速率可达256Mbps。
 
 
在PDP激活、二次激活过程中，SGSN投递给GGSN的QoS版本，不要超过GGSN支持的最高QoS版本。 
功能描述 
因为每个GGSN的处理能力不同，能够处理的参数能力不一致，以及每个GGSN支持的QoS版本不同，SGSN通过配置GGSN支持的QoS最高版本和支持的参数，避免在PDP激活、二次激活过程中，SGSN给GGSN发送的请求消息中携带的QoS版本超过GGSN支持的最高QoS版本以及是否携带相应的参数。 
                GGSN网段的Qos的版本上限和参数控制功能通过开关控制，启用该功能的配置命令为：
                [SET GGSN SEGMENT QOS VERSION CTRL]
                。
            
                配置GGSN网段支持的QoS版本上限和参数信息，配置命令为：
                [ADD GGSN SEGMENT QOS VERSION]
                。
            
相关主题 
 
设置消息参数控制开关(SET GGSN SEGMENT QOS VERSION CTRL)
 
 
查询消息参数控制开关(SHOW GGSN SEGMENT QOS VERSION CTRL)
 
 
设置GGSN网段缺省消息参数配置(SET GGSN SEGMENT DEFAULT PARA)
 
 
查询GGSN网段缺省消息参数配置(SHOW GGSN SEGMENT DEFAULT PARA)
 
 
新增GGSN网段消息参数(ADD GGSN SEGMENT QOS VERSION)
 
 
修改GGSN网段消息参数(SET GGSN SEGMENT QOS VERSION)
 
 
删除GGSN网段消息参数(DEL GGSN SEGMENT QOS VERSION)
 
 
查询GGSN网段消息参数(SHOW GGSN SEGMENT QOS VERSION)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置消息参数控制开关(SET GGSN SEGMENT QOS VERSION CTRL) 
## 设置消息参数控制开关(SET GGSN SEGMENT QOS VERSION CTRL) 
命令功能 
该命令用于配置是否根据GGSN支持的最高QoS版本对协商QoS版本和相关参数进行限制。 
在PDP激活、二次激活过程中，如果用户的协商QoS版本，超过了GGSN支持的最高QoS版本，会导致激活失败。为了避免后续流程会受到影响，SGSN通过此命令来限制协商QoS的版本，使其不要超过GGSN支持的最高QoS版本。同时不同的GGSN对参数的处理能力不一致，需要SGSN能够控制PDP激活和更新消息中的参数 
在此功能设置为开启的情况下，SGSN后续根据GGSN的IP地址设置对应QoS协商版本以及控制PDP激活和更新消息中的参数。 
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNSEGCTRL|消息参数控制|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示是否根据GGSN支持的最高QoS版本对协商QoS版本进行限制。
命令举例 
设置消息参数控制开关为开启。 
SET GGSN SEGMENT QOS VERSION CTRL:GGSNSEGCTRL=ENABLE; 
父主题： [SGSN消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询消息参数控制开关(SHOW GGSN SEGMENT QOS VERSION CTRL) 
## 查询消息参数控制开关(SHOW GGSN SEGMENT QOS VERSION CTRL) 
命令功能 
该命令用于查询SGSN是否支持根据GGSN支持的最高QoS版本对协商QoS版本和PDP激活和更新消息中的参数进行限制。
注意事项 
该命令只适用于SGSN网元。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GGSNSEGCTRL|消息参数控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示是否根据GGSN支持的最高QoS版本对协商QoS版本进行限制。
命令举例 
查询消息参数控制开关。 
SHOW GGSN SEGMENT QOS VERSION CTRL; 
`
命令 (No.1): SHOW GGSN SEGMENT QOS VERSION CTRL
操作维护  消息参数控制
----------------------
修改      不开启
----------------------
记录数 1
命令执行成功（耗时 0.066 秒）。
` 
父主题： [SGSN消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置GGSN网段缺省消息参数配置(SET GGSN SEGMENT DEFAULT PARA) 
## 设置GGSN网段缺省消息参数配置(SET GGSN SEGMENT DEFAULT PARA) 
命令功能 
该命令用于设置缺省GGSN网段是否支持最高QoS版本和PDP激活和更新消息中的参数。
注意事项 
该命令配置的参数如果是不携带，则在PDP激活更新消息中不会携带此参数；如果是携带，则消息中的参数受其他功能的控制。比如：IMEI设置为携带，但如果没有打开IMEI获取的功能，则消息中不会有IMEI参数。
参数说明 
标识|名称|类型|说明
---|---|---|---
QOSVER|QoS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示GGSN所支持的最高QoS版本。如果实际的QoS协商版本超过GGSN支持的最高QoS时，SGSN采用本参数的数值作为QoS协商版本，以保证SGSN发送给GGSN的Create PDP Context Request消息和Update PDP Context Request消息中的所携带的QoS参数版本不超过GGSN支持的最高QoS版本。如果实际的QoS协商版本没有超过GGSN支持的最高QoS时，则使用实际的QoS协商版本。
ATTR|消息参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|携带RAT type：关闭，表示PDP激活和更新消息中不携带RAT type。携带ULI：关闭，表示PDP激活和更新消息中不携带ULI。携带TZ：关闭，表示PDP激活和更新消息中不携带TZ。携带RAI：关闭，表示PDP激活和更新消息中不携带RAI。携带IMEI：关闭，表示PDP激活和更新消息中不携带IMEI。
命令举例 
设置GGSN网段缺省消息参数配置，QoS版本为R99，消息参数为携带RAT type 
SET GGSN SEGMENT DEFAULT PARA:QOSVER="R99",ATTR="RAT"; 
父主题： [SGSN消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询GGSN网段缺省消息参数配置(SHOW GGSN SEGMENT DEFAULT PARA) 
## 查询GGSN网段缺省消息参数配置(SHOW GGSN SEGMENT DEFAULT PARA) 
命令功能 
该命令用于查询缺省GGSN网段是否支持最高QoS版本和PDP激活和更新消息中的参数。
注意事项 
该命令只适用于SGSN网元。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
QOSVER|QoS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示GGSN所支持的最高QoS版本。如果实际的QoS协商版本超过GGSN支持的最高QoS时，SGSN采用本参数的数值作为QoS协商版本，以保证SGSN发送给GGSN的Create PDP Context Request消息和Update PDP Context Request消息中的所携带的QoS参数版本不超过GGSN支持的最高QoS版本。如果实际的QoS协商版本没有超过GGSN支持的最高QoS时，则使用实际的QoS协商版本。
ATTR|消息参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|携带RAT type：关闭，表示PDP激活和更新消息中不携带RAT type。携带ULI：关闭，表示PDP激活和更新消息中不携带ULI。携带TZ：关闭，表示PDP激活和更新消息中不携带TZ。携带RAI：关闭，表示PDP激活和更新消息中不携带RAI。携带IMEI：关闭，表示PDP激活和更新消息中不携带IMEI。
命令举例 
查询GGSN网段缺省消息参数配置。 
SHOW GGSN SEGMENT DEFAULT PARA; 
`
命令 (No.1): SHOW GGSN SEGMENT DEFAULT PARA
操作维护  QoS版本   消息参数
----------------------------
修改      R99版本   携带RAT type
----------------------------
记录数 1
命令执行成功（耗时 0.023 秒）。
` 
父主题： [SGSN消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增GGSN网段消息参数(ADD GGSN SEGMENT QOS VERSION) 
## 新增GGSN网段消息参数(ADD GGSN SEGMENT QOS VERSION) 
命令功能 
该命令用于配置某个GGSN网元支持的最高QoS版本和PDP激活和更新消息中携带的参数。 
在实际情况下，如果QoS协商版本超过GGSN支持的最高QoS时，SGSN采用本命令配置的数值作为QoS协商版本，以保证SGSN发送给GGSN的Create PDP Context Request消息和Update PDP Context Request消息中的所携带的QoS参数版本不超过GGSN支持的最高QoS版本。 
如果QoS协商版本没有超过GGSN支持的最高QoS时，则SGSN使用QoS协商版本。 
注意事项 
该命令只适用于SGSN网元。 
配置本命令，首先需要通过[SET GGSN SEGMENT QOS VERSION CTRL]命令，将“GGSNSEGCTRL”参数设置为"ENABLE"。
参数说明 
标识|名称|类型|说明
---|---|---|---
NETWORKADDR|GGSN网段地址|参数可选性:必选参数；参数类型:地址|GGSN的控制面地址。
NETWORKMASK|GGSN网段掩码|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|表示IP地址掩码的长度，比如24位或者32位等。
QOSVER|QoS版本|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|表示GGSN所支持的最高QoS版本。如果实际的QoS协商版本超过GGSN支持的最高QoS时，SGSN采用本参数的数值作为QoS协商版本，以保证SGSN发送给GGSN的Create PDP Context Request消息和Update PDP Context Request消息中的所携带的QoS参数版本不超过GGSN支持的最高QoS版本。如果实际的QoS协商版本没有超过GGSN支持的最高QoS时，则使用实际的QoS协商版本。
ATTR|消息参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:RAT&ULI&TZ&RAI&IMEI。|携带RAT type：关闭，表示PDP激活和更新消息中不携带RAT type。携带ULI：关闭，表示PDP激活和更新消息中不携带ULI。携带TZ：关闭，表示PDP激活和更新消息中不携带TZ。携带RAI：关闭，表示PDP激活和更新消息中不携带RAI。携带IMEI：关闭，表示PDP激活和更新消息中不携带IMEI。
命令举例 
新增GGSN网段消息参数，设置GGSN网段地址为10.44.36.0，设置GGSN网段掩码为24位，设置QoS版本为R6。 
ADD GGSN SEGMENT QOS VERSION:NETWORKADDR=10.44.36.0,NETWORKMASK=24,QOSVER=R6; 
父主题： [SGSN消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改GGSN网段消息参数(SET GGSN SEGMENT QOS VERSION) 
## 修改GGSN网段消息参数(SET GGSN SEGMENT QOS VERSION) 
命令功能 
该命令用于根据GGSN的IP地址修改其支持的最高QoS版本和PDP激活和更新消息中携带的参数。
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
NETWORKADDR|GGSN网段地址|参数可选性:必选参数；参数类型:地址|GGSN的控制面地址。
NETWORKMASK|GGSN网段掩码|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|表示IP地址掩码的长度，比如24位或者32位等。
QOSVER|QoS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示GGSN所支持的最高QoS版本。如果实际的QoS协商版本超过GGSN支持的最高QoS时，SGSN采用本参数的数值作为QoS协商版本，以保证SGSN发送给GGSN的Create PDP Context Request消息和Update PDP Context Request消息中的所携带的QoS参数版本不超过GGSN支持的最高QoS版本。如果实际的QoS协商版本没有超过GGSN支持的最高QoS时，则使用实际的QoS协商版本。
ATTR|消息参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|携带RAT type：关闭，表示PDP激活和更新消息中不携带RAT type。携带ULI：关闭，表示PDP激活和更新消息中不携带ULI。携带TZ：关闭，表示PDP激活和更新消息中不携带TZ。携带RAI：关闭，表示PDP激活和更新消息中不携带RAI。携带IMEI：关闭，表示PDP激活和更新消息中不携带IMEI。
命令举例 
修改GGSN网段地址为10.44.36.0，GGSN网段掩码为24位的GGSN网段消息参数，将QoS版本修改为R6。 
SET GGSN SEGMENT QOS VERSION:NETWORKADDR=10.44.36.0,NETWORKMASK=24,QOSVER=R6; 
父主题： [SGSN消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除GGSN网段消息参数(DEL GGSN SEGMENT QOS VERSION) 
## 删除GGSN网段消息参数(DEL GGSN SEGMENT QOS VERSION) 
命令功能 
该命令用于删除GGSN对应的最高QoS版本配置和PDP激活和更新消息中携带的参数。
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
NETWORKADDR|GGSN网段地址|参数可选性:必选参数；参数类型:地址|GGSN的控制面地址。
NETWORKMASK|GGSN网段掩码|参数可选性:必选参数；参数类型:整数；参数范围为:1~128。|表示IP地址掩码的长度，比如24位或者32位等。
命令举例 
删除GGSN网段地址为10.44.36.0，GGSN网段掩码为24位的GGSN网段消息参数。 
DEL GGSN SEGMENT QOS VERSION:NETWORKADDR="10.44.36.0",NETWORKMASK=24; 
父主题： [SGSN消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询GGSN网段消息参数(SHOW GGSN SEGMENT QOS VERSION) 
## 查询GGSN网段消息参数(SHOW GGSN SEGMENT QOS VERSION) 
命令功能 
该命令用于根据GGSN的IP地址查询其支持的最高QoS版本和PDP激活和更新消息中携带的参数。 
如果输入GGSN网段地址和GGSN网段掩码，表示查询该GGSN网段地址和GGSN网段掩码对应的支持最高QoS版本配置。 
如果不输入查询参数，表示查询所有配置的支持最高QoS版本配置。 
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
NETWORKADDR|GGSN网段地址|参数可选性:任选参数；参数类型:地址|GGSN的控制面地址。
NETWORKMASK|GGSN网段掩码|参数可选性:任选参数；参数类型:整数；参数范围为:1~128。|表示IP地址掩码的长度，比如24位或者32位等。
QOSVER|QoS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示GGSN所支持的最高QoS版本。如果实际的QoS协商版本超过GGSN支持的最高QoS时，SGSN采用本参数的数值作为QoS协商版本，以保证SGSN发送给GGSN的Create PDP Context Request消息和Update PDP Context Request消息中的所携带的QoS参数版本不超过GGSN支持的最高QoS版本。如果实际的QoS协商版本没有超过GGSN支持的最高QoS时，则使用实际的QoS协商版本。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NETWORKADDR|GGSN网段地址|参数可选性:任选参数；参数类型:地址|GGSN的控制面地址。
NETWORKMASK|GGSN网段掩码|参数可选性:任选参数；参数类型:整数。|表示IP地址掩码的长度，比如24位或者32位等。
QOSVER|QoS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|表示GGSN所支持的最高QoS版本。如果实际的QoS协商版本超过GGSN支持的最高QoS时，SGSN采用本参数的数值作为QoS协商版本，以保证SGSN发送给GGSN的Create PDP Context Request消息和Update PDP Context Request消息中的所携带的QoS参数版本不超过GGSN支持的最高QoS版本。如果实际的QoS协商版本没有超过GGSN支持的最高QoS时，则使用实际的QoS协商版本。
ATTR|消息参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|携带RAT type：关闭，表示PDP激活和更新消息中不携带RAT type。携带ULI：关闭，表示PDP激活和更新消息中不携带ULI。携带TZ：关闭，表示PDP激活和更新消息中不携带TZ。携带RAI：关闭，表示PDP激活和更新消息中不携带RAI。携带IMEI：关闭，表示PDP激活和更新消息中不携带IMEI。
命令举例 
查询所有的GGSN网段消息参数。 
SHOW GGSN SEGMENT QOS VERSION; 
`
命令 (No.1): SHOW GGSN SEGMENT QOS VERSION
操作维护         GGSN网段地址   GGSN网段掩码   QoS版本   消息参数
-----------------------------------------------------------------
复制 修改 删除   10.44.36.0     24             R6版本    Null
-----------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.025 秒）。
` 
父主题： [SGSN消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 物联网业务配置 
# 物联网业务配置 
背景知识 
            
            当MME支持物联网终端接入后，需要支持针对物联网用户的多种网络功能优化。
        
功能描述 
            
            MME物联网功能配置用于配置MME针对物联网用户的多种网络功能优化的开关。
        
相关主题 
 
设置MME物联网相关业务功能开关(SET MME IOT CFG)
 
 
查询MME物联网相关业务功能开关(SHOW MME IOT CFG)
 
 
节电配置
 
 
报文速率配置
 
 
低移动性策略配置
 
 
基于号段的CN辅助无线参数统计配置
 
 
MME专网配置
 
 
无PDN连接签约检查策略配置
 
 
NB跨RAT移动配置
 
 
NB DRX策略配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置MME物联网相关业务功能开关(SET MME IOT CFG) 
## 设置MME物联网相关业务功能开关(SET MME IOT CFG) 
命令功能 
该命令用于设置MME是否开启物联网相关业务功能。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CPSW|支持控制面优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持物联网小包数据控制面传输优化。当设置为支持后，MME将允许NB-IoT接入，并支持采用控制面优化方案来完成小包数据传输。
SUPPSM|支持PSM|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持PSM（Power Saving Mode，节电模式）功能。当设置为支持后，MME为请求PSM功能的UE分配PSM参数，可极大的提升UE待机时间，同时会导致下行数据/信令业务时延增加。
SUPEDRX|支持eDRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持eDRX（extended idle mode DRX，扩展DRX）功能。当设置为支持后，MME为请求eDRX功能的UE分配eDRX参数，可极大的提升UE待机时间，同时会导致下行数据/信令业务时延增加。
SUPHLCOM|支持HLCom|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持HLCom（Hign Latency Communication，高时延通信）功能。当设置为支持后，对于处于节电状态下的UE，MME通知SGW缓存下行报文，并在下一次用户面承载恢复后由SGW发送给UE。
UPSW|支持用户面优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持NB-IoT（Narrowband IoT，窄带物联网）用户面优化功能。当设置为支持后，MME允许UE以用户面优化模式接入核心网。
ERWOPDNSW|支持物联网终端短消息优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME支持物联网用户仅使用短消息时是否建PDN连接的全局开关。当设置为支持后，MME将允许UE附着时不建PDN连接。
SGNIPDNSW|支持Non-IP数据SGi口传输|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持物联网用户Non-IP数据通过SGi口传输。当设置为支持后，MME将允许UE建立到PGW的Non-IP类型的PDN连接，通过SGi口传输Non-IP的小包数据。
NBS1U|支持NB-IoT接入时采用S1-U承载进行数据传输|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME支持物联网用户采用NB-IoT接入时，能否建立S1-U承载进行数据传输。如果物联网用户采用WB接入，默认支持S1-U数据传输。
MMEASSRANPARA|MME是否支持CN辅助无线参数优化功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持CN辅助无线参数优化功能。不支持：MME不支持CN辅助无线参数优化功能。支持：MME支持CN辅助无线参数优化功能。
SUPLOWMOBILITY|支持低移动性(LM)|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME是否支持低移动性功能。如果参数设置为支持，则需要在“周期性TAU优化策略”配置中配置低移动性用户对应的号段以及该号段使用的周期性TAU优化策略，这样低移动性用户的周期性TAU才更合理。
MMESUPCPRELOC|MME支持UE CP模式下重定向|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持终端CP模式下重定向。不支持：MME不支持终端CP模式下重定向。支持：MME支持终端CP模式下重定向
SUPHLCOMSGWCHG|支持TAU流程SGW改变高延迟缓存数据转发|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置对于TAU流程SGW改变，且用户在原SGW有缓存数据的情况下，MME是否支持通过创建非直传隧道将缓存数据进行转发；开关打开后MME将根据当前的用户状态，创建用户面/控制面非直传隧道，向用户传输缓存数据
UERADCAPM|UE无线能力获取方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME获取UE无线能力的方式。不获取：MME不获取UE Radio Capability information。通过Connection Establishment Indication消息获取：MME通过Connection Establishment Indication消息不携带UE Radio Capability information。通过Downlink NAS Transport消息获取：MME通过Downlink NAS Transport消息携带UE Capability Info Request字段。
SUPEDT|支持EDT|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持NB Early Data Transmission（EDT）功能。不支持：MME不支持NB Early Data Transmission（EDT）功能。支持：MME支持NB Early Data Transmission（EDT）功能。
RDS11USGWALARMRVY|支持接收报文触发S11-U SGW告警恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME收到对端S11-U SGW的报文时，是否查找GSN告警节点表，发现该S11-U SGW节点在GSN告警节点表中，则恢复告警“S11-U SGW节点不可达”，并删除告警节点信息。不支持：MME不支持接收报文触发S11-U SGW告警恢复。支持：MME支持接收报文触发S11-U SGW告警恢复。
SPRUEDIFFERENTIATION|支持UE differentiation功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当SCEF和HSS支持签约的UE通信模式时，HSS分发UE通信模式参数到MME，MME可以根据此参数判断是否向无线发送UE Differentiation Information参数。MME通过此参数设置MME是否支持NB-IoT网络的UE differentiation功能。不支持（OFF）。支持（ON）。
SPRTSUBPTW|支持用户签约PTW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制是否支持用户签约PTW，默认不支持。修改影响：当该参数设置为是，则MME根据本地配置的PTW优先级策略，从UE请求的PTW、本地配置的PTW以及用户签约的PTW中选择优先级最高的PTW下发给UE。当该参数设置为否，则从UE请求的PTW和本地配置的PTW中选择优先级最高的PTW发给UE。数据来源：本端规划。默认值：否。配置原则：无。
IDRSUBPTWCHGPLY|IDR请求携带全部签约PTW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制当PTW签约变更时，HSS下发的IDR请求消息中，是否携带完整的PTW签约。修改影响：当该参数设置为是，MME认为IDR请求中携带的PTW签约数据是完整的PTW签约数据，MME覆盖本地保存的用户PTW签约数据。当该参数设置为否，MME认为IDR请求仅携带变化的PTW签约数据，MME仅修改IDR请求中携带的PTW签约数据。数据来源：本端规划。默认值：是。配置原则：无。
命令举例 
开启MME物联网相关业务功能，设置MME支持控制面优化、支持PSM、支持eDRX，支持HLCom。 
SET MME IOT CFG:CPSW="YES",SUPPSM="YES",SUPEDRX="YES",SUPHLCOM="YES",UPSW="YES",ERWOPDNSW="YES",SGNIPDNSW="YES"; 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME物联网相关业务功能开关(SHOW MME IOT CFG) 
## 查询MME物联网相关业务功能开关(SHOW MME IOT CFG) 
命令功能 
该命令用于查询MME是否开启了物联网相关业务功能。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CPSW|支持控制面优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持物联网小包数据控制面传输优化。当设置为支持后，MME将允许NB-IoT接入，并支持采用控制面优化方案来完成小包数据传输。
SUPPSM|支持PSM|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持PSM（Power Saving Mode，节电模式）功能。当设置为支持后，MME为请求PSM功能的UE分配PSM参数，可极大的提升UE待机时间，同时会导致下行数据/信令业务时延增加。
SUPEDRX|支持eDRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持eDRX（extended idle mode DRX，扩展DRX）功能。当设置为支持后，MME为请求eDRX功能的UE分配eDRX参数，可极大的提升UE待机时间，同时会导致下行数据/信令业务时延增加。
SUPHLCOM|支持HLCom|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持HLCom（Hign Latency Communication，高时延通信）功能。当设置为支持后，对于处于节电状态下的UE，MME通知SGW缓存下行报文，并在下一次用户面承载恢复后由SGW发送给UE。
UPSW|支持用户面优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持NB-IoT（Narrowband IoT，窄带物联网）用户面优化功能。当设置为支持后，MME允许UE以用户面优化模式接入核心网。
ERWOPDNSW|支持物联网终端短消息优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME支持物联网用户仅使用短消息时是否建PDN连接的全局开关。当设置为支持后，MME将允许UE附着时不建PDN连接。
SGNIPDNSW|支持Non-IP数据SGi口传输|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持物联网用户Non-IP数据通过SGi口传输。当设置为支持后，MME将允许UE建立到PGW的Non-IP类型的PDN连接，通过SGi口传输Non-IP的小包数据。
NBS1U|支持NB-IoT接入时采用S1-U承载进行数据传输|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME支持物联网用户采用NB-IoT接入时，能否建立S1-U承载进行数据传输。如果物联网用户采用WB接入，默认支持S1-U数据传输。
MMEASSRANPARA|MME是否支持CN辅助无线参数优化功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持CN辅助无线参数优化功能。不支持：MME不支持CN辅助无线参数优化功能。支持：MME支持CN辅助无线参数优化功能。
SUPLOWMOBILITY|支持低移动性(LM)|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME是否支持低移动性功能。如果参数设置为支持，则需要在“周期性TAU优化策略”配置中配置低移动性用户对应的号段以及该号段使用的周期性TAU优化策略，这样低移动性用户的周期性TAU才更合理。
MMESUPCPRELOC|MME支持UE CP模式下重定向|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持终端CP模式下重定向。不支持：MME不支持终端CP模式下重定向。支持：MME支持终端CP模式下重定向
SUPHLCOMSGWCHG|支持TAU流程SGW改变高延迟缓存数据转发|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置对于TAU流程SGW改变，且用户在原SGW有缓存数据的情况下，MME是否支持通过创建非直传隧道将缓存数据进行转发；开关打开后MME将根据当前的用户状态，创建用户面/控制面非直传隧道，向用户传输缓存数据
UERADCAPM|UE无线能力获取方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME获取UE无线能力的方式。不获取：MME不获取UE Radio Capability information。通过Connection Establishment Indication消息获取：MME通过Connection Establishment Indication消息不携带UE Radio Capability information。通过Downlink NAS Transport消息获取：MME通过Downlink NAS Transport消息携带UE Capability Info Request字段。
SUPEDT|支持EDT|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持NB Early Data Transmission（EDT）功能。不支持：MME不支持NB Early Data Transmission（EDT）功能。支持：MME支持NB Early Data Transmission（EDT）功能。
RDS11USGWALARMRVY|支持接收报文触发S11-U SGW告警恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME收到对端S11-U SGW的报文时，是否查找GSN告警节点表，发现该S11-U SGW节点在GSN告警节点表中，则恢复告警“S11-U SGW节点不可达”，并删除告警节点信息。不支持：MME不支持接收报文触发S11-U SGW告警恢复。支持：MME支持接收报文触发S11-U SGW告警恢复。
SPRUEDIFFERENTIATION|支持UE differentiation功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当SCEF和HSS支持签约的UE通信模式时，HSS分发UE通信模式参数到MME，MME可以根据此参数判断是否向无线发送UE Differentiation Information参数。MME通过此参数设置MME是否支持NB-IoT网络的UE differentiation功能。不支持（OFF）。支持（ON）。
SPRTSUBPTW|支持用户签约PTW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制是否支持用户签约PTW，默认不支持。修改影响：当该参数设置为是，则MME根据本地配置的PTW优先级策略，从UE请求的PTW、本地配置的PTW以及用户签约的PTW中选择优先级最高的PTW下发给UE。当该参数设置为否，则从UE请求的PTW和本地配置的PTW中选择优先级最高的PTW发给UE。数据来源：本端规划。默认值：否。配置原则：无。
IDRSUBPTWCHGPLY|IDR请求携带全部签约PTW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制当PTW签约变更时，HSS下发的IDR请求消息中，是否携带完整的PTW签约。修改影响：当该参数设置为是，MME认为IDR请求中携带的PTW签约数据是完整的PTW签约数据，MME覆盖本地保存的用户PTW签约数据。当该参数设置为否，MME认为IDR请求仅携带变化的PTW签约数据，MME仅修改IDR请求中携带的PTW签约数据。数据来源：本端规划。默认值：是。配置原则：无。
命令举例 
查询MME是否支持物联网相关业务功能。 
SHOW MME IOT CFG; 
`
命令 (No.1): SHOW MME IOT CFG
-----------------uMAC_MME_V7master/NFS_MMESGSN_0----------------
操作维护       支持控制面优化 支持PSM 支持eDRX 支持HLCom 支持用户面优化 支持物联网终端短消息优化 支持Non-IP数据SGi口传输 支持NB-IoT接入时采用S1-U承载进行数据传输 MME是否支持CN辅助无线参数优化功能 支持低移动性(LM) MME支持UE CP模式下重定向 支持TAU流程SGW改变高延迟缓存数据转发 UE无线能力获取方式                              支持EDT 支持接收报文触发S11-U SGW告警恢复 支持UE differentiation功能 支持用户签约PTW IDR请求携带全部签约PTW 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           不支持         不支持  不支持   不支持    不支持         不支持                   不支持                  不支持                                   不支持                            不支持           不支持                   不支持                               通过Connection Establishment Indication消息获取 不支持  不支持                            不支持                     否              是                     
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
命令执行成功（耗时 0.093 秒）。
` 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 节电配置 
## 节电配置 
背景知识 
传统4G网络应用中一般都是智能手机用户，在无数据传输情况下，通过释放空口连接进入空闲模式以节电，但为了应对随时可能触发的下行数据业务、语音业务等，终端在空闲模式下需要始终处于可寻呼状态，接收单元需要频繁开启，该状态仍然会导致大量的不必要的耗电，一般智能手机待机时间在几天以内。 
对于物联网终端，特别是无持续供电电源，或无法更换电池场景（比如：动物跟踪、恶劣条件下传感器设备等），其待机时间要求很高，一般以年为单位，普通终端几天的待机时间是无法满足物联网设备要求的。大部分物联网应用是小包数据传输，其传输间隔比较长并具有一定规律，可以容忍一定程度的延时通信（即高时延通信），因此可以根据实际业务部署情况来应用特定的节电技术以满足要求。 
物联网节电技术分为两种方式： 
 
PSM（Power Saving Mode，节电模式）：MME为UE分配活跃定时器。当UE进入空闲态后，活跃定时器启动，在此时间段内UE可以被寻呼，当活跃定时器超时则UE进入省电模式，彻底关闭无线信息接收单元，从而达到大幅提升待机时间的目的。
 
 
eDRX（extended Idle Mode DRX，演进的DRX）：UE进入空闲模式后，在现有的非连续接收基础上，进一步延长非连续接收间隔，从而达到大幅提升待机时间的目的。需要注意的是，当UE进入省电模式后，下行数据需要等到UE退出省电模式后才能发给UE，存在通信时延，对于不能容忍高时延通信的UE不能请求使用节电功能。
 
 
功能描述 
节电配置功能包括： 
 
配置缺省节电策略
此功能用于配置一个默认的节电策略，如果在节电策略因子配置中，没有可用的节电策略模板，则系统会使用此处配置的默认的节电策略。
 
 
配置节电策略模板
此功能用于配置一个节电策略模板，在节电策略因子配置中引用此处配置的策略模板。
 
 
配置节电策略因子
此功能用于根据用户的IMSI号段和APNNI为不同的用户配置不同的节点策略。
 
 
相关主题 
 
节电策略模板配置
 
 
节电策略因子配置
 
 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 节电策略模板配置 
### 节电策略模板配置 
背景知识 
传统4G网络应用中一般都是智能手机用户，在无数据传输情况下，通过释放空口连接进入空闲模式以节电，但为了应对随时可能触发的下行数据业务、语音业务等，终端在空闲模式下需要始终处于可寻呼状态，接收单元需要频繁开启，该状态仍然会导致大量的不必要的耗电，一般智能手机待机时间在几天以内。 
对于物联网终端，特别是无持续供电电源，或无法更换电池场景（比如：动物跟踪、恶劣条件下传感器设备等），其待机时间要求很高，一般以年为单位，普通终端几天的待机时间是无法满足物联网设备要求的。大部分物联网应用是小包数据传输，其传输间隔比较长并具有一定规律，可以容忍一定程度的延时通信（即高时延通信），因此可以根据实际业务部署情况来应用特定的节电技术以满足要求。 
功能描述 
节电技术分为两种： 
 
PSM：MME为UE分配活跃定时器。当UE进入空闲态后，活跃定时器启动，在此时间段内UE可以被寻呼，当活跃定时器超时则UE进入省电模式，彻底关闭无线信息接收单元，从而达到大幅提升待机时间的目的。
 
 
eDRX：UE进入空闲模式后，在现有的非连续接收基础上，进一步延长非连续接收间隔，从而达到大幅提升待机时间的目的。需要注意的是，当UE进入省电模式后，下行数据需要等到UE退出省电模式后才能发给UE，存在通信时延，对于不能容忍高时延通信的UE不能请求使用节电功能。
 
 
相关主题 
 
设置缺省节电策略(SET DEFAULT POWERSAVE POLICY)
 
 
查询缺省节电策略(SHOW DEFAULT POWERSAVE POLICY)
 
 
新增节电策略(ADD POWERSAVE POLICY)
 
 
修改节电策略(SET POWERSAVE POLICY)
 
 
删除节电策略(DEL POWERSAVE POLICY)
 
 
查询节电策略(SHOW POWERSAVE POLICY)
 
 
父主题： [节电配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置缺省节电策略(SET DEFAULT POWERSAVE POLICY) 
#### 设置缺省节电策略(SET DEFAULT POWERSAVE POLICY) 
命令功能 
该命令用于设置缺省的节电策略，当UE无匹配的节电策略因子配置时，将使用运营商配置的缺省的节电策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
AUTHPOLICY|UE同时请求PSM和eDRX时授权策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE同时请求两种节电（PSM和eDRX）技术时，是否均允许还是只能使用其中的一种。
HSFNSTARTTIME|H-SFN起始时间|参数可选性:任选参数；参数类型:日期|该参数用于MME计算H-SFN帧号时，确保和eNB使用相同的起始时间点。
SUPPORTPSM|支持PSM|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持PSM功能。
SUPPORTEDRX|支持eDRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持eDRX功能。
PSMATPRIO|Active Time优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配PSM节电参数值（Active Time）时优先参考的数据来源。UE请求的Active Time优先级和本地配置的Active Time优先级不能相同。
UEREQATPRIO|UE请求的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用UE在请求消息中携带的值。
LOCALATPRIO|本地配置的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用MME本地配置值。
HSSATPRIO|HSS签约的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用HSS签约值。
PSMATVALUE|Active Time(T3324)(s)|参数可选性:任选参数；参数类型:整数；参数范围为:0~11160。|该参数用于设置MME本地配置的Active Time（活跃定时器）。
PSMT3412PRIO|周期性更新时长优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配PSM节电参数值（周期性更新时长）时优先参考的数据来源。UE请求的周期性更新时长优先级、本地配置的周期性更新时长优先级和HSS签约的周期性更新时长优先级两两不能相同。
UEREQT3412PRIO|UE请求的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用UE在请求消息中携带的值。
LOCALT3412PRIO|本地配置的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用MME本地配置值。
HSST3412PRIO|HSS签约的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用HSS签约值。
PSMT3412|MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。|该参数用于设置MME本地配置的周期性跟踪区更新定时器时长值。当MME为UE分配PSM节电参数值（周期性更新时长）时，如果本地配置的周期性更新时长优先级为最高，则会使用该参数值。
PSMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~35712000。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=分配给UE的周期性跟踪区更新定时器(T3412)时长(秒)+ MME可达定时器相对T3412增量时长(秒)。
EDRXCYCPRIO|eDRX Cycle优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配eDRX节电参数值（eDRX Cycle Value）时优先参考的数据来源。
UEREQCYCPRIO|UE请求的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用UE在请求消息中携带的值。
LOCALCYCPRIO|本地配置的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用MME本地配置值。
HSSTCYCPRIO|HSS签约的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用HSS签约值。
EDRXCYCNBVALUE|NB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的NB-IoT接入制式的eDRX Cycle Value。
EDRXCYCWBVALUE|WB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的WB接入制式的eDRX Cycle Value。
EDRXPTWPRIO|eDRX PTW优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配eDRX节电参数值（eDRX PTW Value）时优先参考的数据来源。
UEREQPTWPRIO|UE请求的eDRX PTW优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用UE在请求消息中携带的值。
LOCALPTWPRIO|本地配置的eDRX PTW优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用MME本地配置值。
SUBPTWPRIO|用户签约的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:MEDIUM。|该参数用于设置在协商eDRX PTW值时，是否优先使用用户签约的PTW。修改影响：通过该参数调整签约PTW优先级，则后续在附着或者TAU过程中协商PTW参数时，可能会导致下发给UE的PTW数值存在变化。数据来源：本端规划。默认值：中。配置原则：本参数仅在MME支持用户签约PTW时有效。
EDRXPTWASSTYPE|PTW分配方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME为UE分配eDRX节电参数值（PTW）时的本地策略。包括两种方式：静态分配：总是为UE分配MME本地配置的一个固定值。基于寻呼策略动态分配：根据UE对应的寻呼策略（寻呼重发间隔及重发次数），将寻呼最大时长作为PTW（Power Saving Mode，节电模式）值。
EDRXNBPTWVALUE|NB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的NB-IoT接入制式的PTW值。
EDRXWBPTWVALUE|WB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的WB接入制式的PTW值。
EDRXPTWTVALUE|T Value(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|节电状态下的寻呼请求需要延迟到下一个PTW即将到达时触发，该参数用于设置PTW即将到达的提前时间量。
EDRXPTWENDTVALUE|eDRX PTW结束时间优化时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置PTW结束的提前时间量。从MME发送寻呼消息，到UE收到寻呼消息，这段时间内UE可能已经从PTW内到PTW外了，所以设置该参数可以保证UE收到寻呼响应时依然处于PTW内。
HLCOMBUFSUGTYPE|SGW扩展缓存报文数推荐方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当需要SGW缓存UE的下行报文时，建议SGW为该UE缓存的下行报文数。包括三种方式：不推荐：MME无建议值，由SGW根据自身策略设置。HSS签约：MME使用HSS签约的缓存报文数作为建议值，如果HSS未签约则无建议值。本地配置：MME使用本地配置的缓存报文数作为建议值。
HLCOMBUFSUGVAL|SGW扩展缓存报文数推荐值|参数可选性:任选参数；参数类型:整数；参数范围为:0~3200。|该参数用于设置MME本地配置的建议SGW缓存报文数。
命令举例 
设置缺省节电策略的T Value为20。 
SET DEFAULT POWERSAVE POLICY:EDRXPTWTVALUE=20; 
父主题： [节电策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询缺省节电策略(SHOW DEFAULT POWERSAVE POLICY) 
#### 查询缺省节电策略(SHOW DEFAULT POWERSAVE POLICY) 
命令功能 
该命令用于查询缺省的节电策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|节电策略模板编号|参数可选性:任选参数；参数类型:整数。|该参数用于设置节电策略编号。
AUTHPOLICY|UE同时请求PSM和eDRX时授权策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE同时请求两种节电（PSM和eDRX）技术时，是否均允许还是只能使用其中的一种。
HSFNSTARTTIME|H-SFN起始时间|参数可选性:任选参数；参数类型:日期|该参数用于MME计算H-SFN帧号时，确保和eNB使用相同的起始时间点。
SUPPORTPSM|支持PSM|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持PSM功能。
SUPPORTEDRX|支持eDRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持eDRX功能。
UEREQATPRIO|UE请求的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用UE在请求消息中携带的值。
LOCALATPRIO|本地配置的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用MME本地配置值。
HSSATPRIO|HSS签约的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用HSS签约值。
PSMATVALUE|Active Time(T3324)(s)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的Active Time（活跃定时器）。
UEREQT3412PRIO|UE请求的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用UE在请求消息中携带的值。
LOCALT3412PRIO|本地配置的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用MME本地配置值。
HSST3412PRIO|HSS签约的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用HSS签约值。
PSMT3412|MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的周期性跟踪区更新定时器时长值。当MME为UE分配PSM节电参数值（周期性更新时长）时，如果本地配置的周期性更新时长优先级为最高，则会使用该参数值。
PSMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=分配给UE的周期性跟踪区更新定时器(T3412)时长(秒)+ MME可达定时器相对T3412增量时长(秒)。
UEREQCYCPRIO|UE请求的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用UE在请求消息中携带的值。
LOCALCYCPRIO|本地配置的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用MME本地配置值。
HSSTCYCPRIO|HSS签约的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用HSS签约值。
EDRXCYCNBVALUE|NB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的NB-IoT接入制式的eDRX Cycle Value。
EDRXCYCWBVALUE|WB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的WB接入制式的eDRX Cycle Value。
UEREQPTWPRIO|UE请求的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用UE在请求消息中携带的值。
LOCALPTWPRIO|本地配置的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用MME本地配置值。
SUBPTWPRIO|用户签约的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用用户签约的PTW。修改影响：通过该参数调整签约PTW优先级，则后续在附着或者TAU过程中协商PTW参数时，可能会导致下发给UE的PTW数值存在变化。数据来源：本端规划。默认值：中。配置原则：本参数仅在MME支持用户签约PTW时有效。
EDRXPTWASSTYPE|PTW分配方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME为UE分配eDRX节电参数值（PTW）时的本地策略。包括两种方式：静态分配：总是为UE分配MME本地配置的一个固定值。基于寻呼策略动态分配：根据UE对应的寻呼策略（寻呼重发间隔及重发次数），将寻呼最大时长作为PTW（Power Saving Mode，节电模式）值。
EDRXNBPTWVALUE|NB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的NB-IoT接入制式的PTW值。
EDRXWBPTWVALUE|WB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的WB接入制式的PTW值。
EDRXPTWTVALUE|T Value(100ms)|参数可选性:任选参数；参数类型:整数。|节电状态下的寻呼请求需要延迟到下一个PTW即将到达时触发，该参数用于设置PTW即将到达的提前时间量。
EDRXPTWENDTVALUE|eDRX PTW结束时间优化时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于设置PTW结束的提前时间量。从MME发送寻呼消息，到UE收到寻呼消息，这段时间内UE可能已经从PTW内到PTW外了，所以设置该参数可以保证UE收到寻呼响应时依然处于PTW内。
HLCOMBUFSUGTYPE|SGW扩展缓存报文数推荐方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当需要SGW缓存UE的下行报文时，建议SGW为该UE缓存的下行报文数。包括三种方式：不推荐：MME无建议值，由SGW根据自身策略设置。HSS签约：MME使用HSS签约的缓存报文数作为建议值，如果HSS未签约则无建议值。本地配置：MME使用本地配置的缓存报文数作为建议值。
HLCOMBUFSUGVAL|SGW扩展缓存报文数推荐值|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的建议SGW缓存报文数。
命令举例 
查询缺省节电策略。 
SHOW DEFAULT POWERSAVE POLICY; 
`
命令 (No.32): SHOW DEFAULT POWERSAVE POLICY
操作维护       节电策略模板编号 UE同时请求PSM和eDRX时授权策略 H-SFN起始时间       支持PSM 支持eDRX UE请求的Active Time优先级 本地配置的Active Time优先级 HSS签约的Active Time优先级 Active Time(T3324)(s) UE请求的周期性更新时长优先级 本地配置的周期性更新时长优先级 HSS签约的周期性更新时长优先级 MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒) MME可达定时器相对T3412增量时长(秒) UE请求的eDRX Cycle优先级 本地配置的eDRX Cycle优先级 HSS签约的eDRX Cycle优先级 NB eDRX Cycle WB eDRX Cycle UE请求的eDRX PTW优先级 本地配置的eDRX PTW优先级 用户签约的eDRX PTW优先级 PTW分配方式 NB PTW Value WB PTW Value T Value(100ms) eDRX PTW结束时间优化时长(100ms) SGW扩展缓存报文数推荐方式 SGW扩展缓存报文数推荐值 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           1                PSM and eDRX                  1980-01-06 00:00:00 支持    支持     中                        低                          高                         300                   中                           低                             高                            86400                                              240                                中                       低                         高                        43.69分钟     655.36秒      高                     中                       低                       静态分配    40.96秒      20.48秒      10             10                              不推荐                    100                     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.069 秒）。
` 
父主题： [节电策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增节电策略(ADD POWERSAVE POLICY) 
#### 新增节电策略(ADD POWERSAVE POLICY) 
命令功能 
该命令用于增加节电策略，运营商可以根据物联网业务状况，根据特定的因子来自定义特定的节电策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|节电策略模板编号|参数可选性:必选参数；参数类型:整数；参数范围为:256~65535。|该参数用于设置节电策略编号。
POLICYNAME|节电策略模板名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于设置节电策略名称，便于理解本策略应用的业务种类。
AUTHPOLICY|UE同时请求PSM和eDRX时授权策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:PSM_EDRX。|该参数用于设置当UE同时请求两种节电（PSM和eDRX）技术时，是否均允许还是只能使用其中的一种。
SUPPORTPSM|支持PSM|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数设置当前策略是否支持PSM功能。
SUPPORTEDRX|支持eDRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数设置当前策略是否支持eDRX功能。
PSMATPRIO|Active Time优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配PSM节电参数值（Active Time）时优先参考的数据来源。
UEREQATPRIO|UE请求的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:MEDIUM。|该参数用于设置在协商Active Time值时，是否优先使用UE在请求消息中携带的值。
LOCALATPRIO|本地配置的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:LOW。|该参数用于设置在协商Active Time值时，是否优先使用MME本地配置值。
HSSATPRIO|HSS签约的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:HIGH。|该参数用于设置在协商Active Time值时，是否优先使用HSS签约值。
PSMATVALUE|Active Time(T3324)(s)|参数可选性:任选参数；参数类型:整数；参数范围为:0~11160。默认值:300。|该参数用于设置MME本地配置的Active Time（活跃定时器）。
PSMT3412PRIO|周期性更新时长优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配PSM节电参数值（周期性更新时长）时优先参考的数据来源。
UEREQT3412PRIO|UE请求的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:MEDIUM。|该参数用于设置在协商周期性更新时长值时，是否优先使用UE在请求消息中携带的值。
LOCALT3412PRIO|本地配置的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:LOW。|该参数用于设置在协商周期性更新时长值时，是否优先使用MME本地配置值。
HSST3412PRIO|HSS签约的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:HIGH。|该参数用于设置在协商周期性更新时长值时，是否优先使用HSS签约值。
PSMT3412|MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。默认值:86400。|该参数用于设置MME本地配置的周期性跟踪区更新定时器时长值。当MME为UE分配PSM节电参数值（周期性更新时长）时，如果本地配置的周期性更新时长优先级为最高，则会使用该参数值。
PSMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~35712000。默认值:240。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=分配给UE的周期性跟踪区更新定时器(T3412)时长(秒)+ MME可达定时器相对T3412增量时长(秒)。
EDRXCYCPRIO|eDRX Cycle优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配eDRX节电参数值（eDRX Cycle Value）时优先参考的数据来源。
UEREQCYCPRIO|UE请求的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:MEDIUM。|该参数用于设置在协商eDRX Cycle值时，是否优先使用UE在请求消息中携带的值。
LOCALCYCPRIO|本地配置的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:LOW。|该参数用于设置在协商eDRX Cycle值时，是否优先使用MME本地配置值。
HSSTCYCPRIO|HSS签约的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:HIGH。|该参数用于设置在协商eDRX Cycle值时，是否优先使用HSS签约值。
EDRXCYCNBVALUE|NB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:256。|该参数用于设置MME本地配置的NB-IoT接入制式的eDRX Cycle Value。
EDRXCYCWBVALUE|WB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:64。|该参数用于设置MME本地配置的WB接入制式的eDRX Cycle Value。
EDRXPTWPRIO|eDRX PTW优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配eDRX节电参数值（eDRX PTW Value）时优先参考的数据来源。
UEREQPTWPRIO|UE请求的eDRX PTW优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:。|该参数用于设置在协商eDRX PTW值时，是否优先使用UE在请求消息中携带的值。
LOCALPTWPRIO|本地配置的eDRX PTW优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:。|该参数用于设置在协商eDRX PTW值时，是否优先使用MME本地配置值。
SUBPTWPRIO|用户签约的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:MEDIUM。|该参数用于设置在协商eDRX PTW值时，是否优先使用用户签约的PTW。修改影响：通过该参数调整签约PTW优先级，则后续在附着或者TAU过程中协商PTW参数时，可能会导致下发给UE的PTW数值存在变化。数据来源：本端规划。默认值：中。配置原则：本参数仅在MME支持用户签约PTW时有效。
EDRXPTWASSTYPE|PTW分配方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:STATIC。|该参数用于设置MME为UE分配eDRX节电参数值（PTW）时的本地策略。包括两种方式：静态分配：总是为UE分配MME本地配置的一个固定值。基于寻呼策略动态分配：根据UE对应的寻呼策略（寻呼重发间隔及重发次数），将寻呼最大时长作为PTW（Power Saving Mode，节电模式）值。
EDRXNBPTWVALUE|NB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:16。|该参数用于设置MME静态配置的NB-IoT接入制式的PTW值。
EDRXWBPTWVALUE|WB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:16。|该参数用于设置MME静态配置的WB接入制式的PTW值。
EDRXPTWTVALUE|T Value(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。默认值:10。|节电状态下的寻呼请求需要延迟到下一个PTW即将到达时触发，该参数用于设置PTW即将到达的提前时间量。
EDRXPTWENDTVALUE|eDRX PTW结束时间优化时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。默认值:10。|该参数用于设置PTW结束的提前时间量。从MME发送寻呼消息，到UE收到寻呼消息，这段时间内UE可能已经从PTW内到PTW外了，所以设置该参数可以保证UE收到寻呼响应时依然处于PTW内。
HLCOMBUFSUGTYPE|SGW扩展缓存报文数推荐方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NOTSUGGEST。|该参数用于设置当需要SGW缓存UE的下行报文时，建议SGW为该UE缓存的下行报文数。包括三种方式：不推荐：MME无建议值，由SGW根据自身策略设置。HSS签约：MME使用HSS签约的缓存报文数作为建议值，如果HSS未签约则无建议值。本地配置：MME使用本地配置的缓存报文数作为建议值。
HLCOMBUFSUGVAL|SGW扩展缓存报文数推荐值|参数可选性:任选参数；参数类型:整数；参数范围为:0~3200。默认值:2。|该参数用于设置MME本地配置的建议SGW缓存报文数。
命令举例 
新增节电策略配置，节电策略模板编号为256，节电策略模板名称为policy_256。 
ADD POWERSAVE POLICY:POLICYID=256,POLICYNAME="policy_256"; 
父主题： [节电策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改节电策略(SET POWERSAVE POLICY) 
#### 修改节电策略(SET POWERSAVE POLICY) 
命令功能 
该命令用于修改自定义节电策略，运营商可以根据物联网业务状况，灵活调整自定义的节电策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|节电策略模板编号|参数可选性:必选参数；参数类型:整数；参数范围为:256~65535。|该参数用于设置节电策略编号。
POLICYNAME|节电策略模板名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|该参数用于设置节电策略名称，便于理解本策略应用的业务种类。
AUTHPOLICY|UE同时请求PSM和eDRX时授权策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE同时请求两种节电（PSM和eDRX）技术时，是否均允许还是只能使用其中的一种。
SUPPORTPSM|支持PSM|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持PSM功能。
SUPPORTEDRX|支持eDRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持eDRX功能。
PSMATPRIO|Active Time优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配PSM节电参数值（Active Time）时优先参考的数据来源。
UEREQATPRIO|UE请求的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用UE在请求消息中携带的值。
LOCALATPRIO|本地配置的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用MME本地配置值。
HSSATPRIO|HSS签约的Active Time优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用HSS签约值。
PSMATVALUE|Active Time(T3324)(s)|参数可选性:任选参数；参数类型:整数；参数范围为:0~11160。|该参数用于设置MME本地配置的Active Time（活跃定时器）。
PSMT3412PRIO|周期性更新时长优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配PSM节电参数值（周期性更新时长）时优先参考的数据来源。
UEREQT3412PRIO|UE请求的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用UE在请求消息中携带的值。
LOCALT3412PRIO|本地配置的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用MME本地配置值。
HSST3412PRIO|HSS签约的周期性更新时长优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用HSS签约值。
PSMT3412|MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。|该参数用于设置MME本地配置的周期性跟踪区更新定时器时长值。当MME为UE分配PSM节电参数值（周期性更新时长）时，如果本地配置的周期性更新时长优先级为最高，则会使用该参数值。
PSMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~35712000。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=分配给UE的周期性跟踪区更新定时器(T3412)时长(秒)+ MME可达定时器相对T3412增量时长(秒)。
EDRXCYCPRIO|eDRX Cycle优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配eDRX节电参数值（eDRX Cycle Value）时优先参考的数据来源。
UEREQCYCPRIO|UE请求的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用UE在请求消息中携带的值。
LOCALCYCPRIO|本地配置的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用MME本地配置值。
HSSTCYCPRIO|HSS签约的eDRX Cycle优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用HSS签约值。
EDRXCYCNBVALUE|NB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的NB-IoT接入制式的eDRX Cycle Value。
EDRXCYCWBVALUE|WB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的WB接入制式的eDRX Cycle Value。
EDRXPTWPRIO|eDRX PTW优先级|参数可选性:任选参数；参数类型:复合参数|该参数用于设置MME为UE分配eDRX节电参数值（eDRX PTW Value）时优先参考的数据来源。
UEREQPTWPRIO|UE请求的eDRX PTW优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用UE在请求消息中携带的值。
LOCALPTWPRIO|本地配置的eDRX PTW优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用MME本地配置值。
SUBPTWPRIO|用户签约的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:MEDIUM。|该参数用于设置在协商eDRX PTW值时，是否优先使用用户签约的PTW。修改影响：通过该参数调整签约PTW优先级，则后续在附着或者TAU过程中协商PTW参数时，可能会导致下发给UE的PTW数值存在变化。数据来源：本端规划。默认值：中。配置原则：本参数仅在MME支持用户签约PTW时有效。
EDRXPTWASSTYPE|PTW分配方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME为UE分配eDRX节电参数值（PTW）时的本地策略。包括两种方式：静态分配：总是为UE分配MME本地配置的一个固定值。基于寻呼策略动态分配：根据UE对应的寻呼策略（寻呼重发间隔及重发次数），将寻呼最大时长作为PTW（Power Saving Mode，节电模式）值。
EDRXNBPTWVALUE|NB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的NB-IoT接入制式的PTW值。
EDRXWBPTWVALUE|WB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的WB接入制式的PTW值。
EDRXPTWTVALUE|T Value(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|节电状态下的寻呼请求需要延迟到下一个PTW即将到达时触发，该参数用于设置PTW即将到达的提前时间量。
EDRXPTWENDTVALUE|eDRX PTW结束时间优化时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置PTW结束的提前时间量。从MME发送寻呼消息，到UE收到寻呼消息，这段时间内UE可能已经从PTW内到PTW外了，所以设置该参数可以保证UE收到寻呼响应时依然处于PTW内。
HLCOMBUFSUGTYPE|SGW扩展缓存报文数推荐方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当需要SGW缓存UE的下行报文时，建议SGW为该UE缓存的下行报文数。包括三种方式：不推荐：MME无建议值，由SGW根据自身策略设置。HSS签约：MME使用HSS签约的缓存报文数作为建议值，如果HSS未签约则无建议值。本地配置：MME使用本地配置的缓存报文数作为建议值。
HLCOMBUFSUGVAL|SGW扩展缓存报文数推荐值|参数可选性:任选参数；参数类型:整数；参数范围为:0~3200。|该参数用于设置MME本地配置的建议SGW缓存报文数。
命令举例 
修改节电策略模板编号为256的节电策略配置，T Value改为20。 
SET POWERSAVE POLICY:POLICYID=256,EDRXPTWTVALUE=20; 
父主题： [节电策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除节电策略(DEL POWERSAVE POLICY) 
#### 删除节电策略(DEL POWERSAVE POLICY) 
命令功能 
该命令用于删除自定义节电策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|节电策略模板编号|参数可选性:必选参数；参数类型:整数；参数范围为:256~65535。|该参数用于设置节电策略编号。
命令举例 
删除节电策略模板编号为256的节电策略配置。 
DEL POWERSAVE POLICY:POLICYID=256; 
父主题： [节电策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询节电策略(SHOW POWERSAVE POLICY) 
#### 查询节电策略(SHOW POWERSAVE POLICY) 
命令功能 
该命令用于查询自定义节电策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|节电策略模板编号|参数可选性:任选参数；参数类型:整数；参数范围为:256~65535。|该参数用于设置节电策略编号。
POLICYNAME|节电策略模板名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|该参数用于设置节电策略名称，便于理解本策略应用的业务种类。
AUTHPOLICY|UE同时请求PSM和eDRX时授权策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE同时请求两种节电（PSM和eDRX）技术时，是否均允许还是只能使用其中的一种。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|节电策略模板编号|参数可选性:任选参数；参数类型:整数。|该参数用于设置节电策略编号。
POLICYNAME|节电策略模板名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置节电策略名称，便于理解本策略应用的业务种类。
AUTHPOLICY|UE同时请求PSM和eDRX时授权策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE同时请求两种节电（PSM和eDRX）技术时，是否均允许还是只能使用其中的一种。
SUPPORTPSM|支持PSM|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持PSM功能。
SUPPORTEDRX|支持eDRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持eDRX功能。
UEREQATPRIO|UE请求的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用UE在请求消息中携带的值。
LOCALATPRIO|本地配置的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用MME本地配置值。
HSSATPRIO|HSS签约的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用HSS签约值。
PSMATVALUE|Active Time(T3324)(s)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的Active Time（活跃定时器）。
UEREQT3412PRIO|UE请求的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用UE在请求消息中携带的值。
LOCALT3412PRIO|本地配置的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商周期性更新时长值时，是否优先使用MME本地配置值。
HSST3412PRIO|HSS签约的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于协商周期性更新时长值时，是否优先使用HSS签约值。
PSMT3412|MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的周期性跟踪区更新定时器时长值。当MME为UE分配PSM节电参数值（周期性更新时长）时，如果本地配置的周期性更新时长优先级为最高，则会使用该参数值。
PSMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=分配给UE的周期性跟踪区更新定时器(T3412)时长(秒)+ MME可达定时器相对T3412增量时长(秒)。
UEREQCYCPRIO|UE请求的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用UE在请求消息中携带的值。
LOCALCYCPRIO|本地配置的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用MME本地配置值。
HSSTCYCPRIO|HSS签约的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用HSS签约值。
EDRXCYCNBVALUE|NB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的NB-IoT接入制式的eDRX Cycle Value。
EDRXCYCWBVALUE|WB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的WB接入制式的eDRX Cycle Value。
UEREQPTWPRIO|UE请求的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用UE在请求消息中携带的值。
LOCALPTWPRIO|本地配置的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用MME本地配置值。
SUBPTWPRIO|用户签约的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用用户签约的PTW。修改影响：通过该参数调整签约PTW优先级，则后续在附着或者TAU过程中协商PTW参数时，可能会导致下发给UE的PTW数值存在变化。数据来源：本端规划。默认值：中。配置原则：本参数仅在MME支持用户签约PTW时有效。
EDRXPTWASSTYPE|PTW分配方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME为UE分配eDRX节电参数值（PTW）时的本地策略。包括两种方式：静态分配：总是为UE分配MME本地配置的一个固定值。基于寻呼策略动态分配：根据UE对应的寻呼策略（寻呼重发间隔及重发次数），将寻呼最大时长作为PTW（Power Saving Mode，节电模式）值。
EDRXNBPTWVALUE|NB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的NB-IoT接入制式的PTW值。
EDRXWBPTWVALUE|WB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的WB接入制式的PTW值。
EDRXPTWTVALUE|T Value(100ms)|参数可选性:任选参数；参数类型:整数。|节电状态下的寻呼请求需要延迟到下一个PTW即将到达时触发，该参数用于设置PTW即将到达的提前时间量。
EDRXPTWENDTVALUE|eDRX PTW结束时间优化时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于设置PTW结束的提前时间量。从MME发送寻呼消息，到UE收到寻呼消息，这段时间内UE可能已经从PTW内到PTW外了，所以设置该参数可以保证UE收到寻呼响应时依然处于PTW内。
HLCOMBUFSUGTYPE|SGW扩展缓存报文数推荐方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当需要SGW缓存UE的下行报文时，建议SGW为该UE缓存的下行报文数。包括三种方式：不推荐：MME无建议值，由SGW根据自身策略设置。HSS签约：MME使用HSS签约的缓存报文数作为建议值，如果HSS未签约则无建议值。本地配置：MME使用本地配置的缓存报文数作为建议值。
HLCOMBUFSUGVAL|SGW扩展缓存报文数推荐值|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的建议SGW缓存报文数。
命令举例 
查询节电策略模板编号为256的节电策略配置。 
SHOW POWERSAVE POLICY:POLICYID=256; 
`
命令 (No.31): SHOW POWERSAVE POLICY:POLICYID=256;
操作维护       节电策略模板编号 节电策略模板名称 UE同时请求PSM和eDRX时授权策略 支持PSM 支持eDRX UE请求的Active Time优先级 本地配置的Active Time优先级 HSS签约的Active Time优先级 Active Time(T3324)(s) UE请求的周期性更新时长优先级 本地配置的周期性更新时长优先级 HSS签约的周期性更新时长优先级 MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒) MME可达定时器相对T3412增量时长(秒) UE请求的eDRX Cycle优先级 本地配置的eDRX Cycle优先级 HSS签约的eDRX Cycle优先级 NB eDRX Cycle WB eDRX Cycle UE请求的eDRX PTW优先级 本地配置的eDRX PTW优先级 用户签约的eDRX PTW优先级 PTW分配方式 NB PTW Value WB PTW Value T Value(100ms) eDRX PTW结束时间优化时长(100ms) SGW扩展缓存报文数推荐方式 SGW扩展缓存报文数推荐值 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 256              policy_256       PSM and eDRX                  支持    支持     中                        低                          高                         300                   中                           低                             高                            86400                                              240                                中                       低                         高                        43.69分钟     655.36秒      高                     低                       中                       静态分配    40.96秒      20.48秒      10             10                              不推荐                    2                       
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.071 秒）。
` 
父主题： [节电策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 节电策略因子配置 
### 节电策略因子配置 
背景知识 
传统4G网络应用中一般都是智能手机用户，在无数据传输情况下，通过释放空口连接进入空闲模式以节电，但为了应对随时可能触发的下行数据业务、语音业务等，终端在空闲模式下需要始终处于可寻呼状态，接收单元需要频繁开启，该状态仍然会导致大量的不必要的耗电，一般智能手机待机时间在几天以内。 
对于物联网终端，特别是无持续供电电源，或无法更换电池场景（比如：动物跟踪、恶劣条件下传感器设备等），其待机时间要求很高，一般以年为单位，普通终端几天的待机时间是无法满足物联网设备要求的。大部分物联网应用是小包数据传输，其传输间隔比较长并具有一定规律，可以容忍一定程度的延时通信（即高时延通信），因此可以根据实际业务部署情况来应用特定的节电技术以满足要求。 
功能描述 
MME节电策略因子配置，适用于运营商根据自身网络状况及业务发展需要，为不同用户，针对不同的物联网业务场景，提供灵活的节电策略。 
本配置中配置的是各种不同的策略因子到特定的节电策略的对应关系，这些因子包括：用户IMSI号段、业务类型（APN）。各因子的组合关系及优先级按照从高到低排序如下： 
IMSI号段+APN 
APN 
IMSI号段 
相关主题 
 
新增节电策略因子(ADD POWERSAVE POLICY FACTOR)
 
 
修改节电策略因子(SET POWERSAVE POLICY FACTOR)
 
 
删除节电策略因子(DEL POWERSAVE POLICY FACTOR)
 
 
查询节电策略因子(SHOW POWERSAVE POLICY FACTOR)
 
 
父主题： [节电配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增节电策略因子(ADD POWERSAVE POLICY FACTOR) 
#### 新增节电策略因子(ADD POWERSAVE POLICY FACTOR) 
命令功能 
该命令用于增加节电策略因子，运营商可以根据自身物联网业务状况，根据特定的因子关联特定的节电策略模板。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FACTORIMSI|用户号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于设置节电策略因子（IMSI号段），该索引可被分析器入口为IMSI节电策略映射键值分析的号码分析结果索引使用。如果不需要通过IMSI号段选择节电策略，则可不使用该参数，同时本参数和APNNI参数必须至少一个有效。
FACTORAPN|APNNI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置节电策略因子（APNNI）。在ADD/SET命令中，如果配置的节电策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的节电策略配置记录。同时本参数和用户号段索引参数必须至少一个有效。
POLICYID|节电策略模板编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置根据策略因子关联到的节电策略模板编号。
命令举例 
新增节电策略因子配置，APNNI为zte，节电策略模板编号为256。 
ADD POWERSAVE POLICY FACTOR:FACTORAPN="zte",POLICYID=256; 
父主题： [节电策略因子配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改节电策略因子(SET POWERSAVE POLICY FACTOR) 
#### 修改节电策略因子(SET POWERSAVE POLICY FACTOR) 
命令功能 
该命令用于修改节电策略因子，运营商可以根据自身物联网业务状况，灵活调整关联的节电策略模板。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FACTORIMSI|用户号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于设置节电策略因子（IMSI号段），该索引可被分析器入口为IMSI节电策略映射键值分析的号码分析结果索引使用。如果不需要通过IMSI号段选择节电策略，则可不使用该参数，同时本参数和APNNI参数必须至少一个有效。
FACTORAPN|APNNI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置节电策略因子（APNNI）。在ADD/SET命令中，如果配置的节电策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的节电策略配置记录。同时本参数和用户号段索引参数必须至少一个有效。
POLICYID|节电策略模板编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于配置根据策略因子关联到的节电策略模板编号。
命令举例 
修改APNNI为zte的节电策略因子配置，节电策略模板编号改为256。 
SET POWERSAVE POLICY FACTOR:FACTORAPN="zte",POLICYID=256; 
父主题： [节电策略因子配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除节电策略因子(DEL POWERSAVE POLICY FACTOR) 
#### 删除节电策略因子(DEL POWERSAVE POLICY FACTOR) 
命令功能 
该命令用于删除节电策略因子，运营商可以根据物联网业务状况，删除特定的节电策略因子与节电策略模板的关联关系。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FACTORIMSI|用户号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于设置节电策略因子（IMSI号段），该索引可被分析器入口为IMSI节电策略映射键值分析的号码分析结果索引使用。如果不需要通过IMSI号段选择节电策略，则可不使用该参数，同时本参数和APNNI参数必须至少一个有效。
FACTORAPN|APNNI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置节电策略因子（APNNI）。在ADD/SET命令中，如果配置的节电策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的节电策略配置记录。同时本参数和用户号段索引参数必须至少一个有效。
命令举例 
删除APNNI为zte的节电策略因子配置。 
DEL POWERSAVE POLICY FACTOR:FACTORAPN="zte"; 
父主题： [节电策略因子配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询节电策略因子(SHOW POWERSAVE POLICY FACTOR) 
#### 查询节电策略因子(SHOW POWERSAVE POLICY FACTOR) 
命令功能 
该命令用于查询节电策略因子对应的节电策略模板。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FACTORIMSI|用户号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~3072。|该参数用于设置节电策略因子（IMSI号段），该索引可被分析器入口为IMSI节电策略映射键值分析的号码分析结果索引使用。如果不需要通过IMSI号段选择节电策略，则可不使用该参数，同时本参数和APNNI参数必须至少一个有效。
FACTORAPN|APNNI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置节电策略因子（APNNI）。在ADD/SET命令中，如果配置的节电策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的节电策略配置记录。同时本参数和用户号段索引参数必须至少一个有效。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FACTORIMSI|用户号段索引|参数可选性:任选参数；参数类型:整数。|该参数用于设置节电策略因子（IMSI号段），该索引可被分析器入口为IMSI节电策略映射键值分析的号码分析结果索引使用。如果不需要通过IMSI号段选择节电策略，则可不使用该参数，同时本参数和APNNI参数必须至少一个有效。
FACTORAPN|APNNI|参数可选性:任选参数；参数类型:字符型。|该参数用于设置节电策略因子（APNNI）。在ADD/SET命令中，如果配置的节电策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的节电策略配置记录。同时本参数和用户号段索引参数必须至少一个有效。
POLICYID|节电策略模板编号|参数可选性:任选参数；参数类型:整数。|该参数用于配置根据策略因子关联到的节电策略模板编号。
POLICYNAME|节电策略模板名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置节电策略名称，便于理解本策略应用的业务种类。
AUTHPOLICY|UE同时请求PSM和eDRX时授权策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE同时请求两种节电（PSM和eDRX）技术时，是否均允许还是只能使用其中的一种。
SUPPORTPSM|支持PSM|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持PSM功能。
SUPPORTEDRX|支持eDRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置当前策略是否支持eDRX功能。
UEREQATPRIO|UE请求的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示在协商Active Time值时，是否优先使用UE在请求消息中携带的值。
LOCALATPRIO|本地配置的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示在协商Active Time值时，是否优先使用MME本地配置值。
HSSATPRIO|HSS签约的Active Time优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商Active Time值时，是否优先使用HSS签约值。
PSMATVALUE|Active Time(T3324)(s)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的Active Time。
UEREQT3412PRIO|UE请求的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示在协商周期性更新时长值时，是否优先使用UE在请求消息中携带的值。
LOCALT3412PRIO|本地配置的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示在协商周期性更新时长值时，是否优先使用MME本地配置值。
HSST3412PRIO|HSS签约的周期性更新时长优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示在协商周期性更新时长值时，是否优先使用HSS签约值。
PSMT3412|MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的周期性跟踪区更新定时器时长值。当MME为UE分配PSM节电参数值（周期性更新时长）时，如果本地配置的周期性更新时长优先级为最高，则会使用该参数值。
PSMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=分配给UE的周期性跟踪区更新定时器(T3412)时长(秒)+ MME可达定时器相对T3412增量时长(秒)。
UEREQCYCPRIO|UE请求的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示在协商eDRX Cycle值时，是否优先使用UE在请求消息中携带的值。
LOCALCYCPRIO|本地配置的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示在协商eDRX Cycle值时，是否优先使用MME本地配置值。
HSSTCYCPRIO|HSS签约的eDRX Cycle优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX Cycle值时，是否优先使用HSS签约值。
EDRXCYCNBVALUE|NB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的NB-IoT接入制式的eDRX Cycle Value。
EDRXCYCWBVALUE|WB eDRX Cycle|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME本地配置的WB接入制式的eDRX Cycle Value。
UEREQPTWPRIO|UE请求的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用UE在请求消息中携带的值。
LOCALPTWPRIO|本地配置的eDRX PTW优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置在协商eDRX PTW值时，是否优先使用MME本地配置值。
EDRXPTWASSTYPE|PTW分配方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于MME为UE分配eDRX节电参数值（PTW）时的本地策略。包括两种方式：静态分配：总是为UE分配MME本地配置的一个固定值。基于寻呼策略动态分配：根据UE对应的寻呼策略（寻呼重发间隔及重发次数），将寻呼最大时长作为PTW值。
EDRXNBPTWVALUE|NB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的NB-IoT接入制式的PTW值。
EDRXWBPTWVALUE|WB PTW Value|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME静态配置的WB接入制式的PTW值。
EDRXPTWTVALUE|T Value(100ms)|参数可选性:任选参数；参数类型:整数。|节电状态下的寻呼请求需要延迟到下一个PTW即将到达时触发，该参数用于设置PTW即将到达的提前时间量。
HLCOMBUFSUGTYPE|SGW扩展缓存报文数推荐方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当需要SGW缓存UE的下行报文时，建议SGW为该UE缓存的下行报文数。包括三种方式：不推荐：MME无建议值，由SGW根据自身策略设置。HSS签约：MME使用HSS签约的缓存报文数作为建议值，如果HSS未签约则无建议值。本地配置：MME使用本地配置的缓存报文数作为建议值。
HLCOMBUFSUGVAL|SGW扩展缓存报文数推荐值|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME本地配置的建议SGW缓存报文数。
命令举例 
查询APNNI为zte的节电策略因子配置。 
SHOW POWERSAVE POLICY FACTOR:FACTORAPN="zte"; 
`
2017-12-14 12:06:58 命令 (No.1): SHOW POWERSAVE POLICY FACTOR
操作维护         用户号段索引   APNNI   节电策略模板编号   节电策略模板名称   UE同时请求PSM和eDRX时授权策略   支持PSM   支持eDRX   UE请求的Active Time优先级   本地配置的Active Time优先级   Active Time(T3324)(s)   UE请求的周期性更新时长优先级   本地配置的周期性更新时长优先级   HSS签约的周期性更新时长优先级   MME本地配置的周期性跟踪区更新定时器(T3412)时长(秒)   MME可达定时器相对T3412增量时长(秒)   UE请求的eDRX Cycle优先级   本地配置的eDRX Cycle优先级   NB eDRX Cycle   WB eDRX Cycle   UE请求的eDRX PTW优先级   本地配置的eDRX PTW优先级   PTW分配方式            NB PTW Value   WB PTW Value   T Value(100ms)   SGW扩展缓存报文数推荐方式   SGW扩展缓存报文数推荐值
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1              1       256                A                  PSM and eDRX                    支持      支持       高                          低                            300                     中                             低                               高                              86400                                                240                                  高                         低                           43.68分钟       655.36秒        高                       低                         静态分配               40.96秒        20.48秒        10               不推荐                      100
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.057 秒）。
` 
父主题： [节电策略因子配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 报文速率配置 
## 报文速率配置 
背景知识 
NB-IoT，是由3GPP定义的基于蜂窝网络的窄带物联网技术，为低复杂度、低功耗、低速率物联网终端提供服务。 
功能描述 
虽然窄带物联网终端的数据传输速率极低，但物联网终端的量特别巨大，为避免网络拥塞，需要对物联网终端进行速率控制。 
速率控制包括针对拜访网络的“Serving PLMN Rate Control”及针对归属网络的“APN Rate Control”这两种控制方式，其中“APN Rate Control”对MME不可见，“Serving PLMN Rate Control”由MME控制。 
服务PLMN速率控制参数由MME设置，包括上行控制速率及下行控制速率，并通过NAS接口及S11接口消息分别通知到UE及PGW，UE执行上行速率控制，PGW执行下行速率控制。 
相关主题 
 
全局用户报文速率配置
 
 
基于IMSI号段用户报文速率配置
 
 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 全局用户报文速率配置 
### 全局用户报文速率配置 
背景知识 
虽然窄带物联网终端的数据传输速率极低，但物联网终端的量特别巨大，为避免网络拥塞，需要对物联网终端进行速率控制。 
速率控制包括针对拜访网络的“Serving PLMN Rate Control”及针对归属网络的“APN Rate Control”这两种控制方式，其中“APN Rate Control”对MME不可见，“Serving PLMN Rate Control”由MME控制。 
服务PLMN速率控制参数由MME设置，包括上行控制速率及下行控制速率，并通过NAS接口及S11接口消息分别通知到UE及PGW，UE执行上行速率控制，PGW执行下行速率控制。 
功能描述 
            
            全局用户报文速率配置，用于设置MME缺省的服务PLMN上下行速率控制参数。
        
相关主题 
 
设置全局用户报文速率(SET NBIOT DATARATE)
 
 
查询全局用户报文速率(SHOW NBIOT DATARATE)
 
 
父主题： [报文速率配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置全局用户报文速率(SET NBIOT DATARATE) 
#### 设置全局用户报文速率(SET NBIOT DATARATE) 
命令功能 
该命令用于配置缺省的用户报文速率参数，当UE无匹配的基于IMSI号段的用户报文速率配置时，将使用运营商配置的缺省的用户报文速率参数。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
UPNASDATARATE|上行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|每6分钟UE允许通过的上行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
DOWNNASDATARATE|下行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|每6分钟PGW允许通过的下行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
命令举例 
设置全局缺省的用户报文速率，其中上行NAS数据PDU速率为11，下行NAS数据PDU速率为22。 
SET NBIOT DATARATE:UPNASDATARATE=11,DOWNNASDATARATE=22; 
父主题： [全局用户报文速率配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询全局用户报文速率(SHOW NBIOT DATARATE) 
#### 查询全局用户报文速率(SHOW NBIOT DATARATE) 
命令功能 
该命令用于查询缺省的用户报文速率参数。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
UPNASDATARATE|上行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数。|每6分钟UE允许通过的上行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
DOWNNASDATARATE|下行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数。|每6分钟PGW允许通过的下行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
命令举例 
查询全局缺省的用户报文速率。 
SHOW NBIOT DATARATE; 
`
命令 (No.12): SHOW NBIOT DATARATE
操作维护  上行NAS数据PDU速率   下行NAS数据PDU速率
-------------------------------------------------
修改      11                   22
-------------------------------------------------
记录数 1
命令执行成功（耗时 0.043 秒）。
` 
父主题： [全局用户报文速率配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于IMSI号段用户报文速率配置 
### 基于IMSI号段用户报文速率配置 
背景知识 
虽然窄带物联网终端的数据传输速率极低，但物联网终端的量特别巨大，为避免网络拥塞，需要对物联网终端进行速率控制。 
速率控制包括针对拜访网络的“Serving PLMN Rate Control”及针对归属网络的“APN Rate Control”这两种控制方式，其中“APN Rate Control”对MME不可见，“Serving PLMN Rate Control”由MME控制。 
服务PLMN速率控制参数由MME设置，包括上行控制速率及下行控制速率，并通过NAS接口及S11接口消息分别通知到UE及PGW，UE执行上行速率控制，PGW执行下行速率控制。 
功能描述 
基于IMSI号段用户报文速率配置，用于运营商对不同用户灵活设置服务PLMN速率控制参数。 
相关主题 
 
新增基于IMSI号段用户报文速率(ADD IMSI NBIOT DATARATE)
 
 
修改基于IMSI号段用户报文速率(SET IMSI NBIOT DATARATE)
 
 
删除基于IMSI号段用户报文速率(DEL IMSI NBIOT DATARATE)
 
 
查询基于IMSI号段用户报文速率(SHOW IMSI NBIOT DATARATE)
 
 
父主题： [报文速率配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增基于IMSI号段用户报文速率(ADD IMSI NBIOT DATARATE) 
#### 新增基于IMSI号段用户报文速率(ADD IMSI NBIOT DATARATE) 
命令功能 
该命令用于增加基于IMSI号段的用户报文速率配置，运营商可以根据用户分类灵活控制。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
UPNASDATARATE|上行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|每6分钟UE允许通过的上行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
DOWNNASDATARATE|下行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|每6分钟PGW允许通过的下行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
命令举例 
新增基于IMSI号段的用户报文速率配置，其中IMSI号段为1234，上行NAS数据PDU速率为12，下行NAS数据PDU速率为34。 
ADD IMSI NBIOT DATARATE:IMSI="1234",UPNASDATARATE=12,DOWNNASDATARATE=34; 
父主题： [基于IMSI号段用户报文速率配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改基于IMSI号段用户报文速率(SET IMSI NBIOT DATARATE) 
#### 修改基于IMSI号段用户报文速率(SET IMSI NBIOT DATARATE) 
命令功能 
该命令用于修改基于IMSI号段的用户报文速率，运营商可以根据用户分类灵活控制。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
UPNASDATARATE|上行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|每6分钟UE允许通过的上行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
DOWNNASDATARATE|下行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|每6分钟PGW允许通过的下行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
命令举例 
修改基于IMSI号段的用户报文速率配置，其中IMSI号段为1234，上行NAS数据PDU速率为34，下行NAS数据PDU速率为12。 
SET IMSI NBIOT DATARATE:IMSI="1234",UPNASDATARATE=34,DOWNNASDATARATE=12; 
父主题： [基于IMSI号段用户报文速率配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除基于IMSI号段用户报文速率(DEL IMSI NBIOT DATARATE) 
#### 删除基于IMSI号段用户报文速率(DEL IMSI NBIOT DATARATE) 
命令功能 
该命令用于删除基于IMSI号段的用户报文速率配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
命令举例 
删除基于IMSI号段的用户报文速率配置，其中IMSI号段为1234。 
DEL IMSI NBIOT DATARATE:IMSI="1234"; 
父主题： [基于IMSI号段用户报文速率配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于IMSI号段用户报文速率(SHOW IMSI NBIOT DATARATE) 
#### 查询基于IMSI号段用户报文速率(SHOW IMSI NBIOT DATARATE) 
命令功能 
该命令用于查询IMSI号段对应的用户报文速率。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI是国际移动用户识别码（IMSI：International Mobile Subscriber Identification Number），是区别移动用户的标志，存储于SIM卡中，可用于区别移动用户的有效信息。IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。通过配置IMSI号段来达到对特定部分用户进行控制的作用，而不需要将每个用户的完整号码都配置上。
UPNASDATARATE|上行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数。|每6分钟UE允许通过的上行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
DOWNNASDATARATE|下行NAS数据PDU速率|参数可选性:任选参数；参数类型:整数。|每6分钟PGW允许通过的下行NAS Data PDU数目，0值表示对报文速率不控制，非0时最少不能低于10个。
命令举例 
查询所有基于IMSI号段的用户报文速率配置。 
SHOW IMSI NBIOT DATARATE; 
`
命令 (No.15): SHOW IMSI NBIOT DATARATE
操作维护         IMSI号段   上行NAS数据PDU速率   下行NAS数据PDU速率
-------------------------------------------------------------------
复制 修改 删除   1234       12                   34
-------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.072 秒）。
` 
父主题： [基于IMSI号段用户报文速率配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 低移动性策略配置 
## 低移动性策略配置 
背景知识 
物联网设备种类繁多，不同类设备有不同的特性，从移动性角度分，分为：低移动性的设备、一般移动性和高移动性设备，低移动性设备比如各种定点探测设备，家庭电器设备等，不同设备对网络资源的需求不同，为了最优化的利用网络资源，针对低移动性设备可以减少移动性管理过程。 
功能描述 
低移动性设备的移动性管理过程减少包括加长周期性TAU时长和缩小寻呼范围等。 
同时为了便于了解网络中低移动性设备的数量情况，增加低移动性设备的数量统计。 
相关主题 
 
低移动性识别及控制策略
 
 
周期性TAU优化策略
 
 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 低移动性识别及控制策略 
### 低移动性识别及控制策略 
背景知识 
移动性是指移动设备的物理位置发生改变的频度。 
移动设备种类繁多，从设备的移动性角度进行分类，可以分为三类：低移动性的设备、一般移动性的设备和高移动性设备。 
比如各种定点探测设备、家庭电器设备等可归为低移动性设备。 
功能描述 
该配置实现的功能如下： 
 
支持开启低移动设备识别功能。
开启低移动设备识别功能可以使运营商了解网络中低移动性设备的数量情况。
低移动性的设备终端，其特点是周期性TAU的时长比较长。当运营商需要确认移动网络中低移动性设备的数量时，可以根据这一特点将其与其他非低移动的设备终端进行区别，根据周期性TAU时长来标识终端是否为低移动性终端。
                        MME判断用户在HSS签约数据中的周期性TAU时长大于在本地配置的用户周期性TAU时长，用户周期性TAU时长是通过
                        SET LOWMOBILITY POLICY
                        命令配置的参数“本地默认周期性TAU时长（Local Default Periodic TAU Timer）”，则认为该移动终端是低移动性终端。
                    
 
 
支持灵活控制下发给UE的周期性TAU时长。
可以是全局、HSS签约或本地配置低移动性的周期性TAU时长。
 
 
使用本功能的前提条件是需要开启license：7102 支持 MME支持低移动性功能（MME support Low Mobility function ）。 
相关主题 
 
设置低移动性识别及控制策略(SET LOWMOBILITY POLICY)
 
 
查询低移动性识别及控制策略(SHOW LOWMOBILITY POLICY)
 
 
父主题： [低移动性策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置低移动性识别及控制策略(SET LOWMOBILITY POLICY) 
#### 设置低移动性识别及控制策略(SET LOWMOBILITY POLICY) 
命令功能 
该命令用于设置ZXUN uMAC是否开启低移动性终端的识别功能以及设置根据周期性TAU时长进行识别的控制策略。 
注意事项 
使用本功能的前提条件是需要开启license：7102 支持 MME支持低移动性功能（MME support Low Mobility function ）。 
参数说明 
标识|名称|类型|说明
---|---|---|---
DEFAULTT3412PRIO|默认周期性TAU时长控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置周期性TAU时长的取值策略。MME下发给UE的周期性TAU时长有以下两种选择策略：0：全局（Global），表示使用全局周期性TAU时长，该参数的取值来源为SHOW MOBILE MANAGEMENT命令中配置的参数“周期性跟踪区更新定时器T3412时长（Periodic TAU Timer T3412 Length）”。1：HSS签约（HSS signing），表示使用HSS签约数据中的周期性TAU时长（该参数的取值来源是ULA和IDA消息中 Subscription-Data AVP中的Subscribed-Periodic-RAU-TAU-Timer字段）。
LMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=周期性TAU定时器（T3412）时长（秒）+ MME可达定时器相对T3412增量时长（秒）。T3412 该定时器指示的是周期性RAU或TAU定时器。
命令举例 
设置低移动性识别及控制策略，其中默认周期性TAU时长控制策略为全局。 
SET LOWMOBILITY POLICY:DEFAULTT3412PRIO="GLOBAL"; 
父主题： [低移动性识别及控制策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询低移动性识别及控制策略(SHOW LOWMOBILITY POLICY) 
#### 查询低移动性识别及控制策略(SHOW LOWMOBILITY POLICY) 
命令功能 
该命令用于查询ZXUN uMAC是否开启了低移动性终端的识别功能，以及在开启此功能的情况下根据周期性TAU时长进行识别的策略。 
注意事项 
无 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DEFAULTT3412PRIO|默认周期性TAU时长控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置周期性TAU时长的取值策略。MME下发给UE的周期性TAU时长有以下两种选择策略：0：全局（Global），表示使用全局周期性TAU时长，该参数的取值来源为SHOW MOBILE MANAGEMENT命令中配置的参数“周期性跟踪区更新定时器T3412时长（Periodic TAU Timer T3412 Length）”。1：HSS签约（HSS signing），表示使用HSS签约数据中的周期性TAU时长（该参数的取值来源是ULA和IDA消息中 Subscription-Data AVP中的Subscribed-Periodic-RAU-TAU-Timer字段）。
LMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=周期性TAU定时器（T3412）时长（秒）+ MME可达定时器相对T3412增量时长（秒）。T3412 该定时器指示的是周期性RAU或TAU定时器。
命令举例 
查询低移动性识别及控制策略。 
SHOW LOWMOBILITY POLICY; 
`
命令 (No.1): SHOW LOWMOBILITY POLICY
操作维护  默认周期性TAU时长控制策略  MME可达定时器相对T3412增量时长(秒) 
----------------------------------------------------------------------------
修改      全局                       240 
----------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.052 秒）。
` 
父主题： [低移动性识别及控制策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 周期性TAU优化策略 
### 周期性TAU优化策略 
背景知识 
ZXUN uMAC支持运营商根据自身网络状况及业务发展需要，对漫游用户提供灵活的移动性管理策略控制。 
运营商可以对漫游用户设置本地的周期性TAU。 
功能描述 
本功能用于配置处于漫游状态的低移动性终端的TAU时长的下发策略。 
使用本功能的前提条件是需要开启license：7102 支持 MME支持低移动性功能（MME support Low Mobility function ）。 
当低移动性终端在附着或TAU流程时，如果ZXUN uMAC发现该终端为漫游用户且在HSS签约了周期性TAU时长，则根据终端的IMSI号段查询本功能配置的周期性TAU时长控制策略。 
 
                        如果可以查询到相关配置数据，则使用
                        ADD IMSI PERIODICTAU POLICY
                        命令中配置的“本地周期性TAU时长（Periodic TAU Timer(T3412) of MME Local Configuration）”做为低移动性终端的周期性TAU。
                    
 
 
                        如果查询不到到相关配置数据，则根据
                        SET LOWMOBILITY POLICY
                        命令配置的参数“默认周期性TAU时长控制策略”中的设置数据来确认低移动性终端的周期性TAU。
                    
 
 
相关主题 
 
新增周期性TAU优化策略(ADD IMSI PERIODICTAU POLICY)
 
 
修改周期性TAU优化策略(SET IMSI PERIODICTAU POLICY)
 
 
删除周期性TAU优化策略(DEL IMSI PERIODICTAU POLICY)
 
 
查询周期性TAU优化策略(SHOW IMSI PERIODICTAU POLICY)
 
 
父主题： [低移动性策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增周期性TAU优化策略(ADD IMSI PERIODICTAU POLICY) 
#### 新增周期性TAU优化策略(ADD IMSI PERIODICTAU POLICY) 
命令功能 
该命令用于增加指定号段周期性TAU优化策略，运营商可以根据自身物联网业务状况，根据IMSI配置自定义特定的周期性TAU优化策略。 
当低移动性终端在附着或TAU流程时，如果ZXUN uMAC发现该终端为漫游用户且在HSS签约了周期性TAU时长，则根据终端的IMSI号段查询本功能配置的周期性TAU时长控制策略。 
 
如果可以查询到相关配置数据，则使用ADD IMSI PERIODICTAU POLICY命令中配置的“本地周期性TAU时长（Periodic TAU Timer(T3412) of MME Local Configuration）”做为低移动性终端的周期性TAU。
 
 
如果查询不到到相关配置数据，则根据SET LOWMOBILITY POLICY命令配置的参数“默认周期性TAU时长控制策略”中的设置数据来确认低移动性终端的周期性TAU。
 
 
注意事项 
使用本功能的前提条件是需要开启license：7102 支持 MME支持低移动性功能（MME support Low Mobility function ）。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|用户号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置需要进行周期性TAU控制的用户IMSI号段。
T3412PRIO|周期性TAU时长控制策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于MME为UE分配周期性TAU时长时优先参考的数据来源。1：HSS签约，使用HSS签约数据中的周期性TAU时长。2：本地：使用ADD IMSI PERIODICTAU POLICY命令中配置的参数“本地周期性TAU时长（Periodic TAU Timer(T3412) of MME Local Configuration）”。
LOWMOBILITYT3412|本地周期性TAU时长（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。默认值:86400。|该参数用于配置本地低移动性周期性TAU时长。当ADD IMSI PERIODICTAU POLICY命令中的参数“Periodic TAU Policy”设置为“Local default”时，必须要设置该参数。
LMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。默认值:240。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=周期性TAU定时器（T3412）时长（秒）+ MME可达定时器相对T3412增量时长（秒）。T3412 该定时器指示的是周期性RAU或TAU定时器。
命令举例 
新增周期性TAU优化策略，其中用户号段为1234，周期性TAU时长控制策略为HSS签约。 
ADD IMSI PERIODICTAU POLICY:IMSI="1234",T3412PRIO="HSS"; 
父主题： [周期性TAU优化策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改周期性TAU优化策略(SET IMSI PERIODICTAU POLICY) 
#### 修改周期性TAU优化策略(SET IMSI PERIODICTAU POLICY) 
命令功能 
该命令用于修改指定号段的周期性TAU优化策略，运营商可以根据自身物联网业务状况，根据IMSI配置自定义特定的周期性TAU优化策略。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|用户号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置需要进行周期性TAU控制的用户IMSI号段。
T3412PRIO|周期性TAU时长控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于MME为UE分配周期性TAU时长时优先参考的数据来源。1：HSS签约，使用HSS签约数据中的周期性TAU时长。2：本地：使用ADD IMSI PERIODICTAU POLICY命令中配置的参数“本地周期性TAU时长（Periodic TAU Timer(T3412) of MME Local Configuration）”。
LOWMOBILITYT3412|本地周期性TAU时长（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。|该参数用于配置本地低移动性周期性TAU时长。当ADD IMSI PERIODICTAU POLICY命令中的参数“Periodic TAU Policy”设置为“Local default”时，必须要设置该参数。
LMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=周期性TAU定时器（T3412）时长（秒）+ MME可达定时器相对T3412增量时长（秒）。T3412 该定时器指示的是周期性RAU或TAU定时器。
命令举例 
修改周期性TAU优化策略，其中用户号段为1234，周期性TAU时长控制策略为HSS签约。 
SET IMSI PERIODICTAU POLICY:IMSI="1234",T3412PRIO="HSS"; 
父主题： [周期性TAU优化策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除周期性TAU优化策略(DEL IMSI PERIODICTAU POLICY) 
#### 删除周期性TAU优化策略(DEL IMSI PERIODICTAU POLICY) 
命令功能 
该命令用于删除指定号段的周期性TAU优化策略。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|用户号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置需要进行周期性TAU控制的用户IMSI号段。
命令举例 
删除周期性TAU优化策略，其中用户号段为1234。 
DEL IMSI PERIODICTAU POLICY:IMSI="1234"; 
父主题： [周期性TAU优化策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询周期性TAU优化策略(SHOW IMSI PERIODICTAU POLICY) 
#### 查询周期性TAU优化策略(SHOW IMSI PERIODICTAU POLICY) 
命令功能 
该命令用于查询指定号段周期性TAU优化策略，可以查询特定的策略，也可以查询所有策略。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|用户号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置需要进行周期性TAU控制的用户IMSI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|用户号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置需要进行周期性TAU控制的用户IMSI号段。
T3412PRIO|周期性TAU时长控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于MME为UE分配周期性TAU时长时优先参考的数据来源。1：HSS签约，使用HSS签约数据中的周期性TAU时长。2：本地：使用ADD IMSI PERIODICTAU POLICY命令中配置的参数“本地周期性TAU时长（Periodic TAU Timer(T3412) of MME Local Configuration）”。
LOWMOBILITYT3412|本地周期性TAU时长（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。|该参数用于配置本地低移动性周期性TAU时长。当ADD IMSI PERIODICTAU POLICY命令中的参数“Periodic TAU Policy”设置为“Local default”时，必须要设置该参数。
LMUNREACHABLE|MME可达定时器相对T3412增量时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。|该参数用于设置MME侧可达定时器时长。可达定时器时长(秒)=周期性TAU定时器（T3412）时长（秒）+ MME可达定时器相对T3412增量时长（秒）。T3412 该定时器指示的是周期性RAU或TAU定时器。
命令举例 
查询周期性TAU优化策略。 
SHOW IMSI PERIODICTAU POLICY; 
`
命令 (No.1): SHOW IMSI PERIODICTAU POLICY
用户号段 周期性TAU时长控制策略 本地周期性TAU时长（秒） MME可达定时器相对T3412增量时长(秒) 
-----------------------------------------------------------------------------------------------
1234     HSS签约               86400                   240 
-----------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [周期性TAU优化策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于号段的CN辅助无线参数统计配置 
## 基于号段的CN辅助无线参数统计配置 
背景知识 
NB-IoT物联网具有海量接入的特性，基于NB-IoT物联网技术接入EPC网络的MTC终端，其数量为亿级单位，是智能手机终端的数十甚至上百倍。如此海量的终端，在与无线建立RRC连接时，会占用大量的无线空口资源，导致无线资源紧张。 
海量接入的MTC终端同时会对网络信令负荷造成冲击，需要在无线侧减少终端的状态切换，从而减少网络对MTC终端的寻呼开销以及移动性管理过程，降低信令负荷。 
3GPP 23.401 协议在R12阶段引入的核心网辅助无线参数优化机制，就是为了减少MTC终端可能出现频繁Connected/Idle之间状态转换所带来的信令开销。该机制实现的功能是由核心网MME根据MTC终端的签约或统计信息，将MTC终端的Expected UE Behaviour相关信息告知eNodeB，eNodeB根据该信息来优化、设置MTC终端RRC连接释放定时器时长，从而决定MTC终端在没有数据传输时，什么时候来释放该MTC终端的RRC连接。 
功能描述 
CN辅助无线参数的获取方式有两种：一是根据MTC终端的签约信息获取；二是根据MME对用户行为的统计信息获取。协议规定如果是基于用户行为的统计信息获取，则需要支持按号段进行限制，即配置号段对应的MTC终端才支持按统计信息获取CN辅助无线参数。 
基于号段的CN辅助无线参数统计配置，适用于运营商根据自身网络状况及业务发展需要，针对不同类型的MTC终端，提供灵活的CN辅助无线参数统计策略。 
本配置中配置的是支持CN辅助无线参数统计功能的号段信息，只有号段已配置的MTC终端才会支持CN辅助无线参数本地统计功能。MTC终端号段类型包括：用户IMSI号段、业务类型（APN）。不同类型号段的组合关系及优先级按照从高到低排序如下： 
IMSI号段+APN 
APN 
IMSI号段 
相关主题 
 
新增基于号段的CN辅助无线参数统计(ADD CN ASS RAN PARA STATS)
 
 
修改基于号段的CN辅助无线参数统计(SET CN ASS RAN PARA STATS)
 
 
删除基于号段的CN辅助无线参数统计(DEL CN ASS RAN PARA STATS)
 
 
查询基于号段的CN辅助无线参数统计(SHOW CN ASS RAN PARA STATS)
 
 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于号段的CN辅助无线参数统计(ADD CN ASS RAN PARA STATS) 
### 新增基于号段的CN辅助无线参数统计(ADD CN ASS RAN PARA STATS) 
命令功能 
该命令用于增加基于号段的CN辅助无线参数统计功能。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置支持CN辅助无线参数统计功能的IMSI号段信息。
APN|APN NI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置支持CN辅助无线参数统计功能的APN信息。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出PGW；另一方面，APN标识了通过该PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了PGW所在的EPC分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
MMEASSRANPARAPLCY|CN辅助无线参数策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:SUBFIRST。|该参数用于指示MME获取CN辅助无线参数的策略。签约信息优先：优先从签约信息中获取CN辅助无线参数。统计信息优先：优先从统计信息中获取CN辅助无线参数。
命令举例 
新增基于号段的CN辅助无线参数统计，其中APN NI为“zte.com”，CN辅助无线参数策略为“签约信息优先”。 
ADD CN ASS RAN PARA STATS:APN="zte.com"; 
父主题： [基于号段的CN辅助无线参数统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于号段的CN辅助无线参数统计(SET CN ASS RAN PARA STATS) 
### 修改基于号段的CN辅助无线参数统计(SET CN ASS RAN PARA STATS) 
命令功能 
该命令用于修改基于号段的CN辅助无线参数统计功能。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置支持CN辅助无线参数统计功能的IMSI号段信息。
APN|APN NI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置支持CN辅助无线参数统计功能的APN信息。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出PGW；另一方面，APN标识了通过该PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了PGW所在的EPC分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
MMEASSRANPARAPLCY|CN辅助无线参数策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示MME获取CN辅助无线参数的策略。签约信息优先：优先从签约信息中获取CN辅助无线参数。统计信息优先：优先从统计信息中获取CN辅助无线参数。
命令举例 
修改基于号段的CN辅助无线参数统计，其中APN NI为“zte.com”，CN辅助无线参数策略为“统计信息优先”。 
SET CN ASS RAN PARA STATS:APN="zte.com",MMEASSRANPARAPLCY="STATSFIRST"; 
父主题： [基于号段的CN辅助无线参数统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于号段的CN辅助无线参数统计(DEL CN ASS RAN PARA STATS) 
### 删除基于号段的CN辅助无线参数统计(DEL CN ASS RAN PARA STATS) 
命令功能 
该命令用于删除基于号段的CN辅助无线参数统计功能。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置支持CN辅助无线参数统计功能的IMSI号段信息。
APN|APN NI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置支持CN辅助无线参数统计功能的APN信息。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出PGW；另一方面，APN标识了通过该PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了PGW所在的EPC分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
命令举例 
删除基于号段的CN辅助无线参数统计，其中APN NI为“zte.com”。 
DEL CN ASS RAN PARA STATS:APN="zte.com"; 
父主题： [基于号段的CN辅助无线参数统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于号段的CN辅助无线参数统计(SHOW CN ASS RAN PARA STATS) 
### 查询基于号段的CN辅助无线参数统计(SHOW CN ASS RAN PARA STATS) 
命令功能 
该命令用于查询基于号段的CN辅助无线参数统计功能。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置支持CN辅助无线参数统计功能的IMSI号段信息。
APN|APN NI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置支持CN辅助无线参数统计功能的APN信息。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出PGW；另一方面，APN标识了通过该PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了PGW所在的EPC分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|该参数用于设置支持CN辅助无线参数统计功能的IMSI号段信息。
APN|APN NI|参数可选性:任选参数；参数类型:字符型。|该参数用于设置支持CN辅助无线参数统计功能的APN信息。APN（Access Point Name，接入点名称）是分组核心网定义的网络标识。一方面，分组核心网通过APN标识出PGW；另一方面，APN标识了通过该PGW所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。根据3GPP TS 23.003协议的定义，APN名称由如下两部分组成：NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务，这部分是必须的。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户通过该PGW接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。OI（Operator Identifier，运营商标识），定义了PGW所在的EPC分组核心网，这部分是可选的。每个运营商都有一个缺省的APN运营商标识。此APN OI由IMSI可获取，形式为“MNCxxx.MCCyyy.gprs”。
MMEASSRANPARAPLCY|CN辅助无线参数策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示MME获取CN辅助无线参数的策略。签约信息优先：优先从签约信息中获取CN辅助无线参数。统计信息优先：优先从统计信息中获取CN辅助无线参数。
命令举例 
查询基于号段的CN辅助无线参数统计。 
SHOW CN ASS RAN PARA STATS; 
`
命令 (No.5): SHOW CN ASS RAN PARA STATS;
操作维护         IMSI号段   APN NI     CN辅助无线参数策略
---------------------------------------------------------
复制 修改 删除   111111     zte.com    签约信息优先
---------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [基于号段的CN辅助无线参数统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MME专网配置 
## MME专网配置 
背景知识 
专网用于为特定的用户提供特定的特性和功能，这类用户包括物联网用户、特定的企业用户或者独立行政区域用户等。物联网终端区别于人网终端，具有海量接入、低功耗等特性，具有专网服务的需求，在物联网应用快速发展的背景下，为物联网用户提供专网服务的需求越来越迫切。 
3GPP 23.401协议上定义了标准的专网功能DECOR（Dedicated Core Network）和eDECOR（Enhancements of Dedicated Core Network）。 
DECOR：特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网，公网MME需要将用户改向到其所属的专网MME下，完成附着、TAU、切换等。 
eDECOR：特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网且UE存储了默认专网标识、按PLMN存储了专网标识，UE提供DCN标识给eNodeB，eNodeB根据专网标识为用户选择专网MME，减少信令改向，MME及时识别专网标识改变并通知UE更新。 
功能描述 
MME专网配置包括MME DECOR配置、MME eDECOR配置、MME DECOR/eDECOR公共配置和专网MME权重配置。 
相关主题 
 
MME DECOR配置
 
 
MME eDECOR配置
 
 
MME DECOR/eDECOR公共配置
 
 
专网MME权重配置
 
 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME DECOR配置 
### MME DECOR配置 
背景知识 
3GPP 23.401协议上定义了标准的专网功能DECOR（Dedicated Core Network），表示特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网，公网MME需要将用户改向到其所属的专网MME下，完成附着、TAU、切换等。 
功能描述 
            
            MME DECOR配置提供了DECOR控制策略配置。
        
相关主题 
 
DECOR控制策略配置
 
 
父主题： [MME专网配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### DECOR控制策略配置 
#### DECOR控制策略配置 
背景知识 
3GPP 23.401协议上定义了标准的专网功能DECOR（Dedicated Core Network），即特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网，公网MME需要将用户改向到其所属的专网MME，完成附着、TAU、切换等。 
功能描述 
DECOR控制策略配置包括： 
 
MME是否支持DECOR。
 
 
漫游用户是否支持DECOR。
 
 
MME是否支持NAS改向。
 
 
MME是否拒绝专网用户接入。
 
 
拒绝时携带的Back-off Timer最小取值（秒）。
 
 
拒绝时携带的Back-off Timer最大取值（秒）。
 
 
相关主题 
 
设置DECOR控制策略(SET DECOR CONTROL POLICY)
 
 
查询DECOR控制策略(SHOW DECOR CONTROL POLICY)
 
 
父主题： [MME DECOR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置DECOR控制策略(SET DECOR CONTROL POLICY) 
##### 设置DECOR控制策略(SET DECOR CONTROL POLICY) 
命令功能 
该命令用于配置DECOR控制策略，包括设置以下内容： 
 
MME是否支持DECOR
 
 
漫游用户是否支持DECOR
 
 
MME是否支持NAS改向
 
 
MME是否拒绝专网用户接入
 
 
拒绝时携带的Back-off Timer取值
 
 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPDECOR|MME是否支持DECOR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持DECOR。
ROAMSUPDECOR|漫游用户是否支持DECOR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME对漫游用户是否支持DECOR，前提是“MME是否支持DECOR”设置为支持，否则不支持漫游用户的DECOR。
MMESUPNASREDI|MME是否支持NAS改向|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当专网用户接入公网MME时，该参数用于设置公网MME是否将专网用户改向到其所属的专网MME，公网MME发送Reroute NAS Request消息给eNodeB，通知其改向用户的附着、TAU请求到专网MME。前提是“MME是否支持DECOR”设置为支持，漫游用户需要“漫游用户是否支持DECOR”设置为支持。
MMEREJDUACC|MME是否拒绝专网用户接入|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当专网用户接入公网MME时，公网MME不支持将专网用户改向到其所属的专网MME时，该参数用于设置公网MME接受专网用户接入还是拒绝专网用户接入。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置拒绝时携带的Back-off Timer最小取值（秒）。当专网用户接入公网MME时，公网MME不支持将专网用户改向到其所属的专网MME，且公网MME拒绝专网用户接入，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置拒绝时携带的Back-off Timer最大取值（秒）。当专网用户接入公网MME时，公网MME不支持将专网用户改向到其所属的专网MME，且公网MME拒绝专网用户接入，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
命令举例 
设置DECOR控制策略，MME是否支持DECOR为不支持，漫游用户是否支持DECOR为不支持，MME是否支持NAS改向为不支持，MME是否拒绝专网用户接入为不支持，拒绝时携带的Back-off Timer最小取值（秒）为1，拒绝时携带的Back-off Timer最大取值（秒）为2。	 
SET DECOR CONTROL POLICY:MMESUPDECOR="NO",ROAMSUPDECOR="NO",MMESUPNASREDI="NO",MMEREJDUACC="NO",MINDELAY=1,MAXDELAY=2; 
父主题： [DECOR控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询DECOR控制策略(SHOW DECOR CONTROL POLICY) 
##### 查询DECOR控制策略(SHOW DECOR CONTROL POLICY) 
命令功能 
该命令用于查询DECOR控制策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPDECOR|MME是否支持DECOR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持DECOR。
ROAMSUPDECOR|漫游用户是否支持DECOR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME对漫游用户是否支持DECOR，前提是“MME是否支持DECOR”设置为支持，否则不支持漫游用户的DECOR。
MMESUPNASREDI|MME是否支持NAS改向|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当专网用户接入公网MME时，该参数用于设置公网MME是否将专网用户改向到其所属的专网MME，公网MME发送Reroute NAS Request消息给eNodeB，通知其改向用户的附着、TAU请求到专网MME。前提是“MME是否支持DECOR”设置为支持，漫游用户需要“漫游用户是否支持DECOR”设置为支持。
MMEREJDUACC|MME是否拒绝专网用户接入|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当专网用户接入公网MME时，公网MME不支持将专网用户改向到其所属的专网MME时，该参数用于设置公网MME接受专网用户接入还是拒绝专网用户接入。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于设置拒绝时携带的Back-off Timer最小取值（秒）。当专网用户接入公网MME时，公网MME不支持将专网用户改向到其所属的专网MME，且公网MME拒绝专网用户接入，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于设置拒绝时携带的Back-off Timer最大取值（秒）。当专网用户接入公网MME时，公网MME不支持将专网用户改向到其所属的专网MME，且公网MME拒绝专网用户接入，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
命令举例 
查询DECOR控制策略配置数据。 
SHOW DECOR CONTROL POLICY; 
`
命令 (No.10): SHOW DECOR CONTROL POLICY
操作维护 MME是否支持DECOR 漫游用户是否支持DECOR MME是否支持NAS改向 MME是否拒绝专网用户接入 拒绝时携带的Back-off Timer最小取值（秒） 拒绝时携带的Back-off Timer最大取值（秒） 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改     不支持           不支持                不支持             不拒绝                   1                                        2 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.107 秒）。
` 
父主题： [DECOR控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME eDECOR配置 
### MME eDECOR配置 
背景知识 
            
            3GPP 23.401协议上定义了标准的专网功能eDECOR（Enhancements of Dedicated Core Network），即UE辅助的专网选择，当特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网且UE存储了默认专网标识、按PLMN存储了专网标识，UE提供DCN标识给eNodeB，eNodeB根据专网标识为用户选择专网MME，减少信令改向，MME及时识别专网标识改变并通知UE更新。
        
功能描述 
            
            MME eDECOR配置提供了eDECOR控制策略配置。
        
相关主题 
 
eDECOR控制策略配置
 
 
DCN-ID配置
 
 
父主题： [MME专网配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### eDECOR控制策略配置 
#### eDECOR控制策略配置 
背景知识 
3GPP 23.401协议上定义了标准的专网功能eDECOR（Enhancements of Dedicated Core Network），即UE辅助的专网选择，当特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网且UE存储了默认专网标识、按PLMN存储了专网标识，UE提供DCN标识给eNodeB，eNodeB根据专网标识为用户选择专网MME，减少信令改向，MME及时识别专网标识改变并通知UE更新。 
功能描述 
eDECOR控制策略配置包括： 
 
MME是否支持eDECOR。
 
 
漫游用户是否支持eDECOR。
 
 
相关主题 
 
设置eDECOR控制策略(SET EDECOR CONTROL POLICY)
 
 
查询eDECOR控制策略(SHOW EDECOR CONTROL POLICY)
 
 
父主题： [MME eDECOR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置eDECOR控制策略(SET EDECOR CONTROL POLICY) 
##### 设置eDECOR控制策略(SET EDECOR CONTROL POLICY) 
命令功能 
该命令用于配置eDECOR控制策略，包括设置以下内容： 
 
MME是否支持eDECOR
 
 
漫游用户是否支持eDECOR
 
 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPEDECOR|MME是否支持eDECOR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持eDECOR。
ROAMSUPEDECOR|漫游用户是否支持eDECOR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME对漫游用户是否支持eDECOR，前提是“MME是否支持eDECOR”设置为支持，否则不支持漫游用户的eDECOR。
命令举例 
设置eDECOR控制策略，MME是否支持eDECOR为支持，漫游用户是否支持eDECOR为支持。	 
SET EDECOR CONTROL POLICY:MMESUPEDECOR="YES",ROAMSUPEDECOR="YES"; 
父主题： [eDECOR控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询eDECOR控制策略(SHOW EDECOR CONTROL POLICY) 
##### 查询eDECOR控制策略(SHOW EDECOR CONTROL POLICY) 
命令功能 
该命令用于查询eDECOR控制策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPEDECOR|MME是否支持eDECOR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持eDECOR。
ROAMSUPEDECOR|漫游用户是否支持eDECOR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME对漫游用户是否支持eDECOR，前提是“MME是否支持eDECOR”设置为支持，否则不支持漫游用户的eDECOR。
命令举例 
查询eDECOR控制策略的配置数据。 
SHOW EDECOR CONTROL POLICY; 
`
命令 (No.15): SHOW EDECOR CONTROL POLICY
操作维护 MME是否支持eDECOR 漫游用户是否支持eDECOR 
----------------------------------------------------
修改     支持              支持 
----------------------------------------------------
记录数 1
命令执行成功（耗时 0.067 秒）。
` 
父主题： [eDECOR控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### DCN-ID配置 
#### DCN-ID配置 
背景知识 
3GPP 23.401协议上定义了标准的专网功能eDECOR（Enhancements of Dedicated Core Network），即特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网且UE存储了默认专网标识、按PLMN存储了专网标识，UE提供DCN标识给eNodeB，eNodeB根据专网标识为用户选择专网MME，减少信令改向，MME及时识别专网标识改变并通知UE更新。 
一般DCN-ID会写入终端的芯片，但网络运营商也可以根据专网网络规划的改变更新终端保存的DCN-ID，服务PLMN指定DCN-ID给UE，并存储在UE每PLMN中。DCN-ID可以是标准的也可以是运营商确定的。 
功能描述 
DCN-ID配置用于运营商根据专网规划，配置本地DCN-ID。 
相关主题 
 
新增DCN-ID配置(ADD DCN IDENTITY)
 
 
修改DCN-ID配置(SET DCN IDENTITY)
 
 
删除DCN-ID配置(DEL DCN IDENTITY)
 
 
查询DCN-ID配置(SHOW DCN IDENTITY)
 
 
父主题： [MME eDECOR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 新增DCN-ID配置(ADD DCN IDENTITY) 
##### 新增DCN-ID配置(ADD DCN IDENTITY) 
命令功能 
该命令用于运营商根据专网规划配置本地DCN-ID。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
UEUSAGETYPE|用户使用类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型，UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。
DCNID|DCN标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~4095。默认值:0。|该参数用于设置专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定
命令举例 
新增DCN-ID配置，PLMN为460-01，用户使用类型为专网用户使用类型1，DCN标识为0。 
ADD DCN IDENTITY:PLMN="460"-"01",UEUSAGETYPE="DCN1",DCNID=0; 
父主题： [DCN-ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 修改DCN-ID配置(SET DCN IDENTITY) 
##### 修改DCN-ID配置(SET DCN IDENTITY) 
命令功能 
该命令用于当运营商专网规划改变时，修改本地DCN-ID配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
UEUSAGETYPE|用户使用类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型，UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。
DCNID|DCN标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4095。|该参数用于设置专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定
命令举例 
修改DCN-ID配置，PLMN为460-01，用户使用类型为专网用户使用类型1，DCN标识为1。 
SET DCN IDENTITY:PLMN="460"-"01",UEUSAGETYPE="DCN1",DCNID=1; 
父主题： [DCN-ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 删除DCN-ID配置(DEL DCN IDENTITY) 
##### 删除DCN-ID配置(DEL DCN IDENTITY) 
命令功能 
该命令用于当运营商专网规划改变时，删除本地DCN-ID配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
UEUSAGETYPE|用户使用类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型，UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。
命令举例 
删除DCN-ID配置，PLMN为460-01，用户使用类型为专网用户使用类型1。 
DEL DCN IDENTITY:PLMN="460"-"01",UEUSAGETYPE="DCN1"; 
父主题： [DCN-ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询DCN-ID配置(SHOW DCN IDENTITY) 
##### 查询DCN-ID配置(SHOW DCN IDENTITY) 
命令功能 
该命令用于查询DCN-ID配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型，UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
UEUSAGETYPE|用户使用类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户使用类型，UE Usage Type是专网用户的签约信息，标识了UE的使用特征，用于特定专网的选择。
DCNID|DCN标识|参数可选性:任选参数；参数类型:整数。|该参数用于设置专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定
命令举例 
查询DCN-ID的配置数据。 
SHOW DCN IDENTITY; 
`
命令 (No.6): SHOW DCN IDENTITY
操作维护       	PLMN	   用户使用类型	  DCN标识	
-------------------------------------------------------
复制 修改 删除 	460-01	专网用户使用类型1	0	
-------------------------------------------------------
记录数 1
命令执行成功（耗时 0.044 秒）。
` 
父主题： [DCN-ID配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME DECOR/eDECOR公共配置 
### MME DECOR/eDECOR公共配置 
背景知识 
3GPP 23.401协议上定义了标准的专网功能DECOR（Dedicated Core Network）和eDECOR（Enhancements of Dedicated Core Network）。 
DECOR：特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网，公网MME需要将用户改向到其所属的专网MME下，完成附着、TAU、切换等。 
eDECOR：特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网且UE存储了默认专网标识、按PLMN存储了专网标识，UE提供DCN标识给eNodeB，eNodeB根据专网标识为用户选择专网MME，减少信令改向，MME及时识别专网标识改变并通知UE更新。 
功能描述 
            
            MME DECOR/eDECOR公共配置包括DECOR/eDECOR公共控制策略配置。
        
相关主题 
 
DECOR/eDECOR公共控制策略配置
 
 
父主题： [MME专网配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### DECOR/eDECOR公共控制策略配置 
#### DECOR/eDECOR公共控制策略配置 
背景知识 
3GPP 23.401协议上定义了标准的专网功能DECOR（Dedicated Core Network）和eDECOR（Enhancements of Dedicated Core Network）。 
DECOR：特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网，公网MME需要将用户改向到其所属的专网MME下，完成附着、TAU、切换等。 
eDECOR：特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了专网且UE存储了默认专网标识、按PLMN存储了专网标识，UE提供DCN标识给eNodeB，eNodeB根据专网标识为用户选择专网MME，减少信令改向，MME及时识别专网标识改变并通知UE更新。 
每个专网包含多个核心网节点（包括MME/SGSN、SGW/PGW/PCRF），这些核心网节点可以组POOL，如物联网专网，一个MME容纳不了海量的终端，需要多个MME。网络除了要为专网用户选择专网的MME/SGSN接入，也要为专网用户选择专网的SGW/PGW为其服务。 
功能描述 
DECOR/eDECOR控制策略配置包括： 
 
用户默认专网支持。
 
 
MME是否支持选择专网的SGW/PGW。
 
 
MME选择专网SGW/PGW失败是否重选。
 
 
MME是否支持选择专网的目标MME/SGSN。
 
 
MME选择专网目标MME/SGSN失败是否重选。
 
 
相关主题 
 
设置DECOR/eDECOR公共控制策略(SET DECOR EDECOR CTRL POLICY)
 
 
查询DECOR/eDECOR公共控制策略(SHOW DECOR EDECOR CTRL POLICY)
 
 
新增IMSI号段DECOR/eDECOR公共控制策略(ADD IMSI DECOR EDECOR CTRL POLICY)
 
 
修改IMSI号段DECOR/eDECOR公共控制策略(SET IMSI DECOR EDECOR CTRL POLICY)
 
 
删除IMSI号段DECOR/eDECOR公共控制策略(DEL IMSI DECOR EDECOR CTRL POLICY)
 
 
查询IMSI号段DECOR/eDECOR公共控制策略(SHOW IMSI DECOR EDECOR CTRL POLICY)
 
 
父主题： [MME DECOR/eDECOR公共配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置DECOR/eDECOR公共控制策略(SET DECOR EDECOR CTRL POLICY) 
##### 设置DECOR/eDECOR公共控制策略(SET DECOR EDECOR CTRL POLICY) 
命令功能 
该命令用于配置DECOR/eDECOR公共控制策略，包括： 
 
用户默认专网支持。
 
 
MME是否支持选择专网的SGW/PGW。
 
 
MME选择专网SGW/PGW失败是否重选。
 
 
MME是否支持选择专网的目标MME/SGSN。
 
 
MME选择专网目标MME/SGSN失败是否重选。
 
 
MME是否支持DSR删除UE Usage Type。
 
 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
USERDEFDCNSUP|用户默认专网支持|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户默认专网支持，MME基于用户级控制是否支持专网，如果用户不在“IMSI号段DECOR/eDECOR公共控制策略”配置中，则使用该“用户默认专网支持”配置。
DCNGWSEL|MME是否支持选择专网的SGW/PGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|专网用户除了需要接入专网MME，根据运营商专网组网规化，也需要接入专网SGW/PGW或者接入公网SGW/PGW，该参数用于设置MME是否支持选择专网的SGW/PGW。
RESELGWFDCNFAIL|MME选择专网SGW/PGW失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|专网用户除了需要接入专网MME，根据运营商专网组网规化，也需要接入专网SGW/PGW或者接入公网SGW/PGW，如果MME选择专网SGW/PGW失败，则MME可以拒绝接入，也可以重新选择公网SGW/PGW使用户接入成功，该参数用于设置MME选择专网SGW/PGW失败是否重选。
DCNMMESGSNSEL|MME是否支持选择专网的目标MME/SGSN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户发生局间切换时，可能会在专网覆盖范围内移动，也可能从非专网区域移动到专网区域内，此时老局MME需要选择目标专网MME/SGSN，该参数用于设置MME是否支持选择专网的目标MME/SGSN。
RESELMSNFDCNFAIL|MME选择专网目标MME/SGSN失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户发生局间切换时，可能会在专网覆盖范围内移动，也可能从非专网区域移动到专网区域内，此时老局MME需要选择目标专网MME/SGSN，如果老局MME选择目标专网MME/SGSN失败，则老局MME可以拒绝切换，也可以重新选择目标公网MME/SGSN使用户切换成功，该参数用于设置MME选择专网目标MME/SGSN失败是否重选。
DSRDELUEUTYPE|MME是否支持DSR删除UE Usage Type|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持HSS在Delete Subscriber Data Request中删除UE Usage Type签约信息。
DEFAULTDCNFUN|MME是否支持默认DCN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持默认的专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定。
DCNAMFSEL|MME是否支持选择专网的目标AMF|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户发生4/5G切换时，可能会在专网覆盖范围内移动，也可能从非专网区域移动到专网区域内，此时老局MME需要选择专网的目标AMF，该参数用于设置MME是否支持选择专网的目标AMF。
RESELAMFFDCNFAIL|MME选择专网目标AMF失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户发生45G切换时，可能会在专网覆盖范围内移动，也可能从非专网区域移动到专网区域内，此时老局MME需要选择专网目标AMF。如果老局MME选择专网目标AMF失败，则老局MME可以：拒绝切换。重新选择目标公网AMF使用户切换成功。该参数用于设置MME选择专网目标AMF失败时，是否重新选择。
命令举例 
设置DECOR/eDECOR公共控制策略，用户默认专网支持为支持DECOR & 支持eDECOR，MME是否支持选择专网的SGW/PGW为支持，MME选择专网SGW/PGW失败是否重选为支持，MME是否支持选择专网的目标MME/SGSN为支持，MME选择专网目标MME/SGSN失败是否重选为支持，MME是否支持DSR删除UE Usage Type为支持。 
SET DECOR EDECOR CTRL POLICY:USERDEFDCNSUP="SUPDECOR"&"SUPEDECOR",DCNGWSEL="YES",RESELGWFDCNFAIL="YES",DCNMMESGSNSEL="YES",RESELMSNFDCNFAIL="YES" 
父主题： [DECOR/eDECOR公共控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询DECOR/eDECOR公共控制策略(SHOW DECOR EDECOR CTRL POLICY) 
##### 查询DECOR/eDECOR公共控制策略(SHOW DECOR EDECOR CTRL POLICY) 
命令功能 
该命令用于查询DECOR/eDECOR公共控制策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
USERDEFDCNSUP|用户默认专网支持|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户默认专网支持，MME基于用户级控制是否支持专网，如果用户不在“IMSI号段DECOR/eDECOR公共控制策略”配置中，则使用该“用户默认专网支持”配置。
DCNGWSEL|MME是否支持选择专网的SGW/PGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|专网用户除了需要接入专网MME，根据运营商专网组网规化，也需要接入专网SGW/PGW或者接入公网SGW/PGW，该参数用于设置MME是否支持选择专网的SGW/PGW。
RESELGWFDCNFAIL|MME选择专网SGW/PGW失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|专网用户除了需要接入专网MME，根据运营商专网组网规化，也需要接入专网SGW/PGW或者接入公网SGW/PGW，如果MME选择专网SGW/PGW失败，则MME可以拒绝接入，也可以重新选择公网SGW/PGW使用户接入成功，该参数用于设置MME选择专网SGW/PGW失败是否重选。
DCNMMESGSNSEL|MME是否支持选择专网的目标MME/SGSN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户发生局间切换时，可能会在专网覆盖范围内移动，也可能从非专网区域移动到专网区域内，此时老局MME需要选择目标专网MME/SGSN，该参数用于设置MME是否支持选择专网的目标MME/SGSN。
RESELMSNFDCNFAIL|MME选择专网目标MME/SGSN失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|专网用户除了需要接入专网MME，根据运营商专网组网规化，也需要接入专网SGW/PGW或者接入公网SGW/PGW，如果MME选择专网SGW/PGW失败，则MME可以拒绝接入，也可以重新选择公网SGW/PGW使用户接入成功，该参数用于设置MME选择专网SGW/PGW失败是否重选。
DSRDELUEUTYPE|MME是否支持DSR删除UE Usage Type|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持HSS在Delete Subscriber Data Request中删除UE Usage Type签约信息。
DEFAULTDCNFUN|MME是否支持默认DCN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持默认DCN（Dedicated Core Network，专用核心网）功能，当该功能开启时，如果非NB-IoT用户接入MME，MME会对该用户会发起重定向流程。不支持：不支持默认DCN功能支持：用支持默认DCN功能
DCNAMFSEL|MME是否支持选择专网的目标AMF|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户发生局间切换时，可能会在专网覆盖范围内移动，也可能从非专网区域移动到专网区域内，此时老局MME需要选择目标专网AMF，该参数用于设置MME是否支持选择专网的目标AMF。
RESELAMFFDCNFAIL|MME选择专网目标AMF失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|专网用户除了需要接入专网MME，根据运营商专网组网规化，也需要接入专网AMF或者接入公网AMF，如果MME选择专网AMF失败，则MME可以拒绝接入，也可以重新选择公网AMF使用户接入成功，该参数用于设置MME选择专网AMF失败是否重选。
命令举例 
查询DECOR/eDECOR公共控制策略的配置数据。 
SHOW DECOR EDECOR CTRL POLICY 
`
命令 (No.1): SHOW DECOR EDECOR CTRL POLICY
操作维护  用户默认专网支持   MME是否支持选择专网的SGW/PGW   MME选择专网SGW/PGW失败是否重选   MME是否支持选择专网的目标MME/SGSN   MME选择专网目标MME/SGSN失败是否重选   MME是否支持DSR删除UE Usage Type
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      Null               不支持                         不支持                           不支持                              不支持                                不支持
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.112 秒）。
` 
父主题： [DECOR/eDECOR公共控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 新增IMSI号段DECOR/eDECOR公共控制策略(ADD IMSI DECOR EDECOR CTRL POLICY) 
##### 新增IMSI号段DECOR/eDECOR公共控制策略(ADD IMSI DECOR EDECOR CTRL POLICY) 
命令功能 
该命令用于添加DECOR控制策略，即设置MME是否支持DECOR，当需要部署DECOR专网时，使用该命令。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
SUPDCN|是否支持专网|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户是否支持专网。不支持：用户不支持专网。支持DECOR：用户支持DECOR。支持eDECOR：用户支持eDECOR。
命令举例 
新增IMSI号段DECOR/eDECOR公共控制策略 IMSI为123，是否支持专网为支持DÉCOR。 
ADD IMSI DECOR EDECOR CTRL POLICY:IMSI="123",SUPDCN="SUPDECOR" 
父主题： [DECOR/eDECOR公共控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 修改IMSI号段DECOR/eDECOR公共控制策略(SET IMSI DECOR EDECOR CTRL POLICY) 
##### 修改IMSI号段DECOR/eDECOR公共控制策略(SET IMSI DECOR EDECOR CTRL POLICY) 
命令功能 
该命令用于修改DECOR控制策略，即设置MME是否支持DECOR，当需要部署DECOR专网时，使用该命令。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
SUPDCN|是否支持专网|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户是否支持专网。不支持：用户不支持专网。支持DECOR：用户支持DECOR。支持eDECOR：用户支持eDECOR。
命令举例 
修改IMSI号段DECOR/eDECOR公共控制策略 IMSI为123，是否支持专网为支持eDECOR。 
SET IMSI DECOR EDECOR CTRL POLICY:IMSI="123",SUPDCN="SUPEDECOR" 
父主题： [DECOR/eDECOR公共控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 删除IMSI号段DECOR/eDECOR公共控制策略(DEL IMSI DECOR EDECOR CTRL POLICY) 
##### 删除IMSI号段DECOR/eDECOR公共控制策略(DEL IMSI DECOR EDECOR CTRL POLICY) 
命令功能 
该命令用于删除DECOR控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|此参数表示IMSI的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
命令举例 
删除IMSI号段DECOR/eDECOR公共控制策略，IMSI为123。 
DEL IMSI DECOR EDECOR CTRL POLICY:IMSI="123" 
父主题： [DECOR/eDECOR公共控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询IMSI号段DECOR/eDECOR公共控制策略(SHOW IMSI DECOR EDECOR CTRL POLICY) 
##### 查询IMSI号段DECOR/eDECOR公共控制策略(SHOW IMSI DECOR EDECOR CTRL POLICY) 
命令功能 
该命令用于查询DECOR控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|此参数表示IMSI的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|此参数表示IMSI的前缀，总长度不超过15位的数字串，首位不能为0。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
SUPDCN|是否支持专网|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置用户是否支持专网。不支持：用户不支持专网。支持DECOR：用户支持DECOR。支持eDECOR：用户支持eDECOR。
命令举例 
查询IMSI号段DECOR/eDECOR公共控制策略的配置数据。 
SHOW IMSI DECOR EDECOR CTRL POLICY 
`
命令 (No.17): SHOW IMSI DECOR EDECOR CTRL POLICY
操作维护	         IMSI	是否支持专网	
------------------------------------
复制 修改 删除 	123	支持DECOR	
------------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [DECOR/eDECOR公共控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 专网MME权重配置 
### 专网MME权重配置 
背景知识 
当专网被使用，eNodeB负载均衡地选择在同一MME POOL内同一专网的多个MME，这些MME的PLMN和MMEGI相同。当一个MME服务于多个专网且一个专网由多个MME支持，为了获得支持同一专网的同一MME POOL内的多个MME间的负载均衡，根据这些MME中每个MME相对于其他MME在专网内的容量设置Weight Factor per DCN。在S1连接建立时MME提供每DCN（Dedicated Core Network）MME权重（Weight Factor per DCN）给eNodeB。 
功能描述 
专网MME权重配置每DCN（Dedicated Core Network）MME权重，MME在S1连接建立时提供给eNodeB。 
相关主题 
 
新增专网MME权重配置(ADD DCN MME WEIGHT)
 
 
修改专网MME权重配置(SET DCN MME WEIGHT)
 
 
删除专网MME权重配置(DEL DCN MME WEIGHT)
 
 
查询专网MME权重配置(SHOW DCN MME WEIGHT)
 
 
父主题： [MME专网配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增专网MME权重配置(ADD DCN MME WEIGHT) 
#### 新增专网MME权重配置(ADD DCN MME WEIGHT) 
命令功能 
该命令用于配置每DCN（Dedicated Core Network）MME权重，当需要部署DCN专网时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
DCNID|DCN标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~4095。默认值:0。|该参数用于设置专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定
MMEWEIGHT|MME权重|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。默认值:0。|该参数用于设置同一专网的同一MME POOL内的本MME相对于其他MME在专网内的容量。
命令举例 
新增专网MME权重配置 DCN标识为1，MME权重为1 
ADD DCN MME WEIGHT:DCNID=1,MMEWEIGHT=1; 
父主题： [专网MME权重配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改专网MME权重配置(SET DCN MME WEIGHT) 
#### 修改专网MME权重配置(SET DCN MME WEIGHT) 
命令功能 
当专网内MME容量发生改变时，使用该命令修改专网MME权重。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
DCNID|DCN标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~4095。|该参数用于设置专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定
MMEWEIGHT|MME权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于设置同一专网的同一MME POOL内的本MME相对于其他MME在专网内的容量。
命令举例 
修改专网MME权重配置 DCN标识为1，MME权重为2 
SET DCN MME WEIGHT:DCNID=1,MMEWEIGHT=2; 
父主题： [专网MME权重配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除专网MME权重配置(DEL DCN MME WEIGHT) 
#### 删除专网MME权重配置(DEL DCN MME WEIGHT) 
命令功能 
该命令用于删除专网MME权重。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
DCNID|DCN标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~4095。|该参数用于设置专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定
命令举例 
删除专网MME权重配置 DCN标识为1 
DEL DCN MME WEIGHT:DCNID=1; 
父主题： [专网MME权重配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询专网MME权重配置(SHOW DCN MME WEIGHT) 
#### 查询专网MME权重配置(SHOW DCN MME WEIGHT) 
命令功能 
该命令用于查询专网MME权重。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
DCNID|DCN标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4095。|该参数用于设置专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DCNID|DCN标识|参数可选性:任选参数；参数类型:整数。|该参数用于设置专网标识DCN-ID，此标识是运营专网规划确定的，由PLMN和专网用户使用类型确定
MMEWEIGHT|MME权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置同一专网的同一MME POOL内的本MME相对于其他MME在专网内的容量。
命令举例 
查询专网MME权重的配置数据。 
 SHOW DCN MME WEIGHT; 
`
命令 (No.25): SHOW DCN MME WEIGHT
操作维护	         DCN标识	MME权重	
----------------------------------
复制 修改 删除 	1	      1	
----------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [专网MME权重配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 无PDN连接签约检查策略配置 
## 无PDN连接签约检查策略配置 
背景知识 
完善NB-IoT功能，MME支持无PDN连接签约检查。 
功能描述 
无PDN连接签约检查策略配置包括： 
 
支持无PDN连接签约检查
 
 
签约PDN连接限制时是否PDN去连接
 
 
PDN连接拒绝原因
 
 
承载去激活原因
 
 
相关主题 
 
设置无PDN连接签约检查策略(SET WOPDN SUBCHK POLICY)
 
 
查询无PDN连接签约检查策略(SHOW WOPDN SUBCHK POLICY)
 
 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置无PDN连接签约检查策略(SET WOPDN SUBCHK POLICY) 
### 设置无PDN连接签约检查策略(SET WOPDN SUBCHK POLICY) 
命令功能 
该命令用于设置无PDN连接签约检查策略，包括： 
 
支持无PDN连接签约检查
 
 
签约PDN连接限制时是否PDN去连接
 
 
PDN连接拒绝原因
 
 
承载去激活原因
 
 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPWOPDNSUBCHK|支持无PDN连接签约检查|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持无PDN签约检查。开关打开后，MME对附着和PDN连接，检查是否签约了PDN连接限制，并且识别PDN连接限制签约信息的变更。
PDNDISCONSUBPDNRESTR|签约PDN连接限制时是否PDN去连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置签约PDN连接限制时，是否PDN去连接。
PDNCONREJCAUSE|PDN连接拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持无PDN连接签约检查，UE和MME都具备Without PDN能力，签约PDN连接限制，当UE发起PDN连接时，MME拒绝PDN连接。该参数用于设置PDN连接拒绝原因。
BEARDEACTCAUSE|承载去激活原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置签约PDN连接限制时PDN去连接，该参数用于设置PDN去连接时承载去激活原因。
命令举例 
设置无PDN连接签约检查策略。 
SET WOPDN SUBCHK POLICY:SUPWOPDNSUBCHK="NO",PDNDISCONSUBPDNRESTR="YES",PDNCONREJCAUSE="PDNCONREJCAU_33",BEARDEACTCAUSE="BEARDEACTCAUSE_36"; 
父主题： [无PDN连接签约检查策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询无PDN连接签约检查策略(SHOW WOPDN SUBCHK POLICY) 
### 查询无PDN连接签约检查策略(SHOW WOPDN SUBCHK POLICY) 
命令功能 
该命令用于查询无PDN连接签约检查策略。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPWOPDNSUBCHK|支持无PDN连接签约检查|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持无PDN签约检查。开关打开后，MME对附着和PDN连接，检查是否签约了PDN连接限制，并且识别PDN连接限制签约信息的变更。
PDNDISCONSUBPDNRESTR|签约PDN连接限制时是否PDN去连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置签约PDN连接限制时，是否PDN去连接。
PDNCONREJCAUSE|PDN连接拒绝原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持无PDN连接签约检查，UE和MME都具备Without PDN能力，签约PDN连接限制，当UE发起PDN连接时，MME拒绝PDN连接。该参数用于设置PDN连接拒绝原因。
BEARDEACTCAUSE|承载去激活原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置签约PDN连接限制时PDN去连接，该参数用于设置PDN去连接时承载去激活原因。
命令举例 
查询无PDN连接签约检查策略。 
SHOW WOPDN SUBCHK POLICY; 
`
2018-03-28 16:37:34 命令 (No.2): SHOW WOPDN SUBCHK POLICY;
操作维护  支持无PDN连接签约检查   签约PDN连接限制时是否PDN去连接   PDN连接拒绝原因                                                     承载去激活原因
-----------------------------------------------------------------------------------------------------------------------------------------------------
修改      不支持                  是                               requested service option not subscribed                             regular deactivation
-----------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.035 秒）。
` 
父主题： [无PDN连接签约检查策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## NB跨RAT移动配置 
## NB跨RAT移动配置 
背景知识 
顺从最新3GPP协议，满足运营商未来需求，支持UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT。 
功能描述 
当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME仅提供某一RAT类型（WB-E-UTRAN or NB-IoT）的TA list，并根据UE的签约信息或根据UE IMSI号段和APN本地配置的PDN连接连续性对每PDN连接进行处理。 
NB跨RAT移动配置提供NB跨RAT移动策略配置和基于UE IMSI号段和APN的NB跨RAT移动配置。 
相关主题 
 
设置NB跨RAT移动策略(SET NB RAT POLICY)
 
 
查询NB跨RAT移动策略(SHOW NB RAT POLICY)
 
 
新增NB跨RAT移动配置(ADD NB RAT)
 
 
修改NB跨RAT移动配置(SET NB RAT)
 
 
删除NB跨RAT移动配置(DEL NB RAT)
 
 
查询NB跨RAT移动配置(SHOW NB RAT)
 
 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置NB跨RAT移动策略(SET NB RAT POLICY) 
### 设置NB跨RAT移动策略(SET NB RAT POLICY) 
命令功能 
该命令用于设置是否支持NB跨RAT移动策略、PDN连接连续性控制优先级和默认PDN连接连续性。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPNBRATIDLEMV|支持NB跨RAT空闲态移动|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持NB跨RAT空闲态移动。不支持：MME不支持NB跨RAT空闲态移动。支持：MME支持NB跨RAT空闲态移动。
PDNPRIORITY|PDN连接连续性控制优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置PDN连接连续性控制优先级。HSS签约优先：当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME先从HSS获取签约的PDN-Connection-Continuity AVP，对相应的PDN连接进行处理；签约获取不到，再获取本地配置的PDN-Connection-Continuity。本地配置优先：当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME先从本地获取配置的PDN-Connection-Continuity，对相应的PDN连接进行处理；本地没有配置，再获取HSS签约的PDN-Connection-Continuity AVP。
DEFPDNCONTINUNITY|默认PDN连接连续性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME从本地配置获取PDN-Connection-Continuity AVP，根据该参数取值对相应的PDN连接进行处理：保留PDN连接：保留PDN连接PDN去连接携带Reactive指示：PDN去连接携带Reactive指示PDN去连接未携带Reactive指示：PDN去连接未携带Reactive指示
命令举例 
设置NB跨RAT移动策略，不支持NB跨RAT空闲态移动。 
SET NB RAT POLICY:SUPNBRATIDLEMV="NO"; 
父主题： [NB跨RAT移动配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询NB跨RAT移动策略(SHOW NB RAT POLICY) 
### 查询NB跨RAT移动策略(SHOW NB RAT POLICY) 
命令功能 
该命令用于查询NB跨RAT移动策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPNBRATIDLEMV|支持NB跨RAT空闲态移动|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持NB跨RAT空闲态移动。不支持：MME不支持NB跨RAT空闲态移动。支持：MME支持NB跨RAT空闲态移动。
PDNPRIORITY|PDN连接连续性控制优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置PDN连接连续性控制优先级。HSS签约优先：当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME先从HSS获取签约的PDN-Connection-Continuity AVP，对相应的PDN连接进行处理；签约获取不到，再获取本地配置的PDN-Connection-Continuity。本地配置优先：当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME先从本地获取配置的PDN-Connection-Continuity，对相应的PDN连接进行处理；本地没有配置，再获取HSS签约的PDN-Connection-Continuity AVP。
DEFPDNCONTINUNITY|默认PDN连接连续性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME从本地配置获取PDN-Connection-Continuity AVP，根据该参数取值对相应的PDN连接进行处理：保留PDN连接：保留PDN连接PDN去连接携带Reactive指示：PDN去连接携带Reactive指示PDN去连接未携带Reactive指示：PDN去连接未携带Reactive指示
命令举例 
查询NB跨RAT移动策略。 
SHOW NB RAT POLICY; 
`
命令 (No.1): SHOW NB RAT POLICY;;
操作维护                支持NB跨RAT空闲态移动               PDN连接连续性控制优先级                默认PDN连接连续性
-----------------------------------------------------------------------------------------------------------------------------------------
修改                    不支持                              HSS签约优先                            PDN去连接携带Reactive指示
-----------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [NB跨RAT移动配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增NB跨RAT移动配置(ADD NB RAT) 
### 新增NB跨RAT移动配置(ADD NB RAT) 
命令功能 
该命令用于新增UE IMSI号段和APN对应的PDN-Connection-Continuity AVP。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置用户IMSI号码或所属IMSI号段。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
PDNCONTINUNITY|PDN连接连续性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME从本地配置获取PDN-Connection-Continuity AVP，根据该参数取值对相应的PDN连接进行处理：保留PDN连接：保留PDN连接PDN去连接携带Reactive指示：PDN去连接携带Reactive指示PDN去连接未携带Reactive指示：PDN去连接未携带Reactive指示
命令举例 
新增NB跨RAT移动配置，IMSI为10010，保留PDN连接。 
ADD NB RAT:IMSI=10010,PDNCONTINUNITY="PDNCONN"; 
父主题： [NB跨RAT移动配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改NB跨RAT移动配置(SET NB RAT) 
### 修改NB跨RAT移动配置(SET NB RAT) 
命令功能 
该命令用于修改NB跨RAT移动配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置用户IMSI号码或所属IMSI号段。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
PDNCONTINUNITY|PDN连接连续性|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME从本地配置获取PDN-Connection-Continuity AVP，根据该参数取值对相应的PDN连接进行处理：保留PDN连接：保留PDN连接PDN去连接携带Reactive指示：PDN去连接携带Reactive指示PDN去连接未携带Reactive指示：PDN去连接未携带Reactive指示
命令举例 
设置NB跨RAT移动配置，IMSI为10010，保留PDN连接。 
SET NB RAT:IMSI=10010,PDNCONTINUNITY="PDNCONN"; 
父主题： [NB跨RAT移动配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除NB跨RAT移动配置(DEL NB RAT) 
### 删除NB跨RAT移动配置(DEL NB RAT) 
命令功能 
该命令用于删除NB跨RAT移动配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置用户IMSI号码或所属IMSI号段。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
命令举例 
删除NB跨RAT移动配置，IMSI为10010。 
DEL NB RAT:IMSI=10010; 
父主题： [NB跨RAT移动配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询NB跨RAT移动配置(SHOW NB RAT) 
### 查询NB跨RAT移动配置(SHOW NB RAT) 
命令功能 
该命令用于查询NB跨RAT移动配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置用户IMSI号码或所属IMSI号段。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置用户IMSI号码或所属IMSI号段。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
PDNCONTINUNITY|PDN连接连续性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE在空闲态跨RAT移动到NB-IoT或移出NB-IoT时，MME从本地配置获取PDN-Connection-Continuity AVP，根据该参数取值对相应的PDN连接进行处理：保留PDN连接：保留PDN连接PDN去连接携带Reactive指示：PDN去连接携带Reactive指示PDN去连接未携带Reactive指示：PDN去连接未携带Reactive指示
命令举例 
查询NB跨RAT移动配置，IMSI为10010 
SHOW NB RAT:IMSI=10010; 
`
命令 (No.1): SHOW NB RAT:IMSI=10010;
操作维护                       IMSI               APN名称                PDN连接连续性
------------------------------------------------------------------------------------------
复制 修改 删除                 10010                                      保留PDN连接
------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [NB跨RAT移动配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## NB DRX策略配置 
## NB DRX策略配置 
背景知识 
DRX（Discontinuous Reception，非连续接收），即UE不是任何时刻都在监听无线信道，而是在一个“睡眠”周期内，一直处于“睡眠”状态，不监听无线信道，在睡眠周期的某一个时刻才醒来，监听无线信道消息，这样能达到终端节电的目的。 
在2/3/4G，R15版本之前，核心网不参与DRX参数协商，完全由UE请求确定。到R16版本，协议规范NB-S1 Mode DRX协商机制，MME可以根据NB-IoT接入的UE请求的DRX参数，和本地的配置策略，协商调整NB DRX参数。 
NB-IoT终端对节电要求比较高，MME实现和UE之间NB-IoT specific DRX协商，在寻呼用户时携带协商的NB-IoT specific DRX，这样eNodeB将在UE苏醒时刻进行寻呼，精确寻呼，避免终端频繁苏醒。从而达到节电效果，增加电池寿命。 
MME提供了全局缺省的NB UE specific DRX协商策略配置和基于号段的NB UE specific DRX协商策略配置。如果配置了号段的NB UE specific DRX协商策略，则采用号段对应的NB UE specific DRX协商策略，否则采用全局缺省的NB DRX协商策略。 
功能描述 
NB UE specific DRX周期参数，依据协议规范，可以配置为32、64、128、256、512、1024六种取值，该参数值越大，UE节电效果越好，相应寻呼时延也越大。该参数值越小，UE频繁苏醒，相应寻呼时延越短，但节电效果越差。 
NB UE specific DRX协商策略，可以配置为以下四个策略： 
 
UE请求的DRX参数。
 
 
本地配置的DRX参数。
 
 
UE请求的DRX参数与本地配置的DRX参数，取最小值。
 
 
UE请求的DRX参数与本地配置的DRX参数，取最大值。
 
 
本节点用于配置MME的NB UE specific DRX协商策略，包括： 
 
基于IMSI号段配置NB UE specific DRX协商策略，MME针对不同IMSI号段用户，设置不同的NB UE specific DRX协商策略，满足不同号段用户的节电和寻呼时延需求。
 
 
配置缺省的NB UE specific DRX协商策略，MME根据IMSI号段没有匹配到NB UE specific DRX协商策略时，则使用缺省的NB UE specific DRX协商策略，满足用户的节电和寻呼时延需求。
 
 
相关主题 
 
设置缺省NB DRX策略(SET DEFAULT NBDRX POLICY)
 
 
查询缺省NB DRX策略(SHOW DEFAULT NBDRX POLICY)
 
 
新增基于号段的NB DRX策略配置(ADD NBDRX IMSISEG POLICY)
 
 
修改基于号段的NB DRX策略配置(SET NBDRX IMSISEG POLICY)
 
 
删除基于号段的NB DRX策略配置(DEL NBDRX IMSISEG POLICY)
 
 
查询基于号段的NB DRX策略配置(SHOW NBDRX IMSISEG POLICY)
 
 
父主题： [物联网业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置缺省NB DRX策略(SET DEFAULT NBDRX POLICY) 
### 设置缺省NB DRX策略(SET DEFAULT NBDRX POLICY) 
命令功能 
该命令用于设置缺省NB specific DRX策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
NBDRXSWITCH|支持NB-IOT UE Specific DRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关，该参数用于设置是否支持NB-IOT UE specific DRX。
NBDRXPERIOD|NB-IOT UE Specific DRX周期|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置缺省NB-IoT UE specific DRX周期值 。NB-IoT UE specific DRX周期参数，依据协议规范，可以配置为32、64、128、256、512、1024六种取值，该参数值越大，UE节电效果越好，相应寻呼时延也越大。该参数值越小，UE频繁苏醒，相应寻呼时延越短，但节电效果越差。
NBDRXPOLICY|NB-IOT UE Specific DRX协商策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置缺省NB UE specific DRX的协商策略，取值如下：UE：UE请求的DRX参数。本地配置：本地配置的DRX参数。UE与本地配置取最小值：UE请求的DRX参数与本地配置的DRX参数，取最小值。UE与本地配置取最大值：UE请求的DRX参数与本地配置的DRX参数，取最大值。
命令举例 
设置缺省NB specific DRX策略配置。不支持NB-IOT UE Specific DRX协商，NB-IOT UE Specific DRX周期为32，NB-IOT UE Specific DRX协商策略为UE。 
SET DEFAULT NBDRX POLICY:NBDRXSWITCH="NO",NBDRXPERIOD="P32",NBDRXPOLICY="UE"; 
父主题： [NB DRX策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询缺省NB DRX策略(SHOW DEFAULT NBDRX POLICY) 
### 查询缺省NB DRX策略(SHOW DEFAULT NBDRX POLICY) 
命令功能 
该命令用于查询缺省NB specific DRX策略配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NBDRXSWITCH|支持NB-IOT UE Specific DRX|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关，该参数用于设置是否支持NB-IOT UE specific DRX。
NBDRXPERIOD|NB-IOT UE Specific DRX周期|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置缺省NB-IoT UE specific DRX周期值 。NB-IoT UE specific DRX周期参数，依据协议规范，可以配置为32、64、128、256、512、1024六种取值，该参数值越大，UE节电效果越好，相应寻呼时延也越大。该参数值越小，UE频繁苏醒，相应寻呼时延越短，但节电效果越差。
NBDRXPOLICY|NB-IOT UE Specific DRX协商策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置缺省NB UE specific DRX的协商策略，取值如下：UE：UE请求的DRX参数。本地配置：本地配置的DRX参数。UE与本地配置取最小值：UE请求的DRX参数与本地配置的DRX参数，取最小值。UE与本地配置取最大值：UE请求的DRX参数与本地配置的DRX参数，取最大值。
命令举例 
查询缺省NB specific DRX策略配置。 
SHOW DEFAULT NBDRX POLICY; 
`
命令 (No.1): SHOW DEFAULT NBDRX POLICY;
操作维护                支持NB-IOT UE Specific DRX协商               NB-IOT UE Specific DRX周期                NB-IOT UE Specific DRX协商策略
-----------------------------------------------------------------------------------------------------------------------------------------------
修改                    不支持                                       32                                        UE
-----------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [NB DRX策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于IMSI号段的NB DRX策略(ADD NBDRX IMSISEG POLICY) 
### 新增基于IMSI号段的NB DRX策略(ADD NBDRX IMSISEG POLICY) 
命令功能 
该命令用于新增基于IMSI号段的NB DRX策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NBDRXPERIOD|NB-IOT UE Specific DRX周期|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:P32。|该参数用于设置基于号段的NB-IoT UE specific DRX周期值 。NB-IoT UE specific DRX周期参数，依据协议规范，可以配置为32、64、128、256、512、1024六种取值，该参数值越大，UE节电效果越好，相应寻呼时延也越大。该参数值越小，UE频繁苏醒，相应寻呼时延越短，但节电效果越差。
NBDRXPOLICY|NB-IOT UE Specific DRX协商策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:UE。|该参数用于设置基于号段的NB UE specific DRX的协商策略，取值如下：UE：UE请求的DRX参数。本地配置：本地配置的DRX参数。UE与本地配置取最小值：UE请求的DRX参数与本地配置的DRX参数，取最小值。UE与本地配置取最大值：UE请求的DRX参数与本地配置的DRX参数，取最大值。
命令举例 
新增基于IMSI号段的NB DRX策略。IMSI为460122，NB-IOT UE Specific DRX周期为32，NB-IOT UE Specific DRX协商策略为UE。 
ADD NBDRX IMSISEG POLICY:IMSI="460122",NBDRXPERIOD="P32",NBDRXPOLICY="UE"; 
父主题： [NB DRX策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于IMSI号段的NB DRX策略(SET NBDRX IMSISEG POLICY) 
### 修改基于IMSI号段的NB DRX策略(SET NBDRX IMSISEG POLICY) 
命令功能 
该命令用于修改基于IMSI号段的NB DRX策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NBDRXPERIOD|NB-IOT UE Specific DRX周期|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于号段的NB-IoT UE specific DRX周期值 。NB-IoT UE specific DRX周期参数，依据协议规范，可以配置为32、64、128、256、512、1024六种取值，该参数值越大，UE节电效果越好，相应寻呼时延也越大。该参数值越小，UE频繁苏醒，相应寻呼时延越短，但节电效果越差。
NBDRXPOLICY|NB-IOT UE Specific DRX协商策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于号段的NB UE specific DRX的协商策略，取值如下：UE：UE请求的DRX参数。本地配置：本地配置的DRX参数。UE与本地配置取最小值：UE请求的DRX参数与本地配置的DRX参数，取最小值。UE与本地配置取最大值：UE请求的DRX参数与本地配置的DRX参数，取最大值。
命令举例 
修改基于IMSI号段的NB DRX策略。IMSI为460122，NB-IOT UE Specific DRX周期为32，NB-IOT UE Specific DRX协商策略为UE。 
SET NBDRX IMSISEG POLICY:IMSI="460122",NBDRXPERIOD="P32",NBDRXPOLICY="UE"; 
父主题： [NB DRX策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于IMSI号段的NB DRX策略(DEL NBDRX IMSISEG POLICY) 
### 删除基于IMSI号段的NB DRX策略(DEL NBDRX IMSISEG POLICY) 
命令功能 
该命令用于删除基于IMSI号段的NB DRX策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
命令举例 
删除基于IMSI号段的NB DRX策略。IMSI为460122。 
DEL NBDRX IMSISEG POLICY:IMSI="460122"; 
父主题： [NB DRX策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于IMSI号段的NB DRX策略(SHOW NBDRX IMSISEG POLICY) 
### 查询基于IMSI号段的NB DRX策略(SHOW NBDRX IMSISEG POLICY) 
命令功能 
该命令用于查询基于IMSI号段的NB DRX策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|该参数表示IMSI（International Mobile Subscriber Identity，国际移动用户标识）的前缀，总长度不超过15位的数字串。IMSI由三部分组成，结构为MCC＋MNC＋MSIN。MCC（Mobile Country Code，移动国家码）标识移动用户所属的国家，MCC由ITU（International Telecommunications Union，国际电信联盟）管理，在世界范围里统一分配。MNC（Mobile Network Code，移动网络号）标识移动用户的归属PLMN（Public Land Mobile Network，公共陆地移动网），包含两位或三位数字，标识移动用户的归属的PLMN，MNC的长度与MCC的值有关，在单个MCC区域，一般不建议MNC采用两位和三位数字的混合方式。MSIN（Mobile Station Identification Number，移动台识别号码），标识一个PLMN内的移动用户。
NBDRXPERIOD|NB-IOT UE Specific DRX周期|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于号段的NB-IoT UE specific DRX周期值 。NB-IoT UE specific DRX周期参数，依据协议规范，可以配置为32、64、128、256、512、1024六种取值，该参数值越大，UE节电效果越好，相应寻呼时延也越大。该参数值越小，UE频繁苏醒，相应寻呼时延越短，但节电效果越差。
NBDRXPOLICY|NB-IOT UE Specific DRX协商策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于号段的NB UE specific DRX的协商策略，取值如下：UE：UE请求的DRX参数。本地配置：本地配置的DRX参数。UE与本地配置取最小值：UE请求的DRX参数与本地配置的DRX参数，取最小值。UE与本地配置取最大值：UE请求的DRX参数与本地配置的DRX参数，取最大值。
命令举例 
查询基于IMSI号段的NB DRX策略。 
SHOW NBDRX IMSISEG POLICY; 
`
命令 (No.1): SHOW NBDRX IMSISEG POLICY;
操作维护                IMSI号段               NB-IOT UE Specific DRX周期                NB-IOT UE Specific DRX协商策略
------------------------------------------------------------------------------------------------------------------------------------
修改                    460122                 32                                        UE
------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [NB DRX策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# GGSN重选配置 
# GGSN重选配置 
背景知识 
GGSN重选功能是指由于POOL组网架构内的某个GGSN发生拥塞、系统或链路问题的情况下导致PDN建立失败时，SGSN选择POOL内其他的GGSN继续尝试PDN建立，而不是等UE再次发起PDN建立请求。 
GGSN重选功能可以降低PDN建立的时延，提升用户感受度。 
功能描述 
本功能用于设置SGSN重新选择GGSN建立PDN连接的相关策略，包括： 
 
SGSN是否支持当PDN建立失败时，在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接。
 
 
SGSN是否支持在无响应消息的情况下，在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接。
 
 
对于漫游用户，SGSN是否支持在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接。
 
 
SGSN删除GGSN地址的方式。
 
 
SGSN是否支持根据Create PDP Context Response消息中携带的失败原因值在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接。
 
 
GGSN向SGSN返回Create PDP Context Response响应消息中携带的失败原因值。如果GGSN失败原因在配置的原因列表中，则进行GGSN重选；反之，则不进行GGSN重选。
 
 
SGSN重新选择GGSN建立PDN连接的最大次数。
 
 
相关主题 
 
设置GGSN重选策略(SET GGSN RESELECT)
 
 
查询GGSN重选策略(SHOW GGSN RESELECT)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置GGSN重选策略(SET GGSN RESELECT) 
## 设置GGSN重选策略(SET GGSN RESELECT) 
命令功能 
本命令用于设置SGSN重新选择GGSN建立PDN连接的相关策略，包括： 
 
SGSN是否支持当PDN建立失败时，在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接。
 
 
SGSN是否支持在无响应消息的情况下，在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接。
 
 
对于漫游用户，SGSN是否支持在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接。
 
 
SGSN删除GGSN地址的方式。
 
 
SGSN是否支持根据Create PDP Context Response消息中携带的失败原因值在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接。
 
 
GGSN向SGSN返回Create PDP Context Response响应消息中携带的失败原因值。如果GGSN失败原因在配置的原因列表中，则进行GGSN重选；反之，则不进行GGSN重选。
 
 
SGSN重新选择GGSN建立PDN连接的最大次数。
 
 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RESELBYFAIL|SGSN是否支持失败时重选GGSN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当GGSN向SGSN返回Create PDP Context Response响应消息，其中携带失败原因，表示PDP创建失败时，SGSN是否支持在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接，而不是等UE再次发起PDN建立请求。该参数包括两个选项：不支持（Not Support）：SGSN不支持在上述场景下，重新选择一个新的GGSN继续尝试建立PDN连接。支持（Support）：SGSN支持在上述场景下，重新选择一个新的GGSN继续尝试建立PDN连接。
RESELBYNORSP|SGSN是否支持无响应时重选GGSN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当GGSN超时未向SGSN返回Create PDP Context Response响应消息时，SGSN是否支持在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接，而不是等UE再次发起PDN建立请求。该参数包括两个选项：不支持（Not Support）：SGSN不支持在上述场景下，重新选择一个新的GGSN继续尝试建立PDN连接。支持（Support）：SGSN支持在上述场景下，重新选择一个新的GGSN继续尝试建立PDN连接。
ROAMURESEL|漫游用户是否重选GGSN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置如果是漫游用户，SGSN是否支持在以下两种情况下，从GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接，而不是等UE再次发起PDN建立请求。当GGSN向SGSN返回Create PDP Context Response响应消息，其中携带失败原因，表示PDP创建失败时。当GGSN超时未向SGSN返回Create PDP Context Response响应消息时。
ADDRDELMODE|GGSN重选地址删除方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN删除GGSN地址的方式。SGSN使用NAPTR（名称权威指针，Naming Authority Pointer）方式查询GGSN的IP地址时，如下两种情况下，以SGSN重选GGSN前，需要删除原来的GGSN地址。当GGSN向SGSN返回Create PDP Context Response响应消息，其中携带失败原因，表示PDP创建失败时。当GGSN超时未向SGSN返回Create PDP Context Response响应消息时。该参数包括两个选项：仅删除失败GGSN地址（Delete failed GGSN address only）：即该GGSN的一个地址。删除失败GGSN下所有地址（Delete all addresses for GGSN failed）：即该GGSN的所有地址。
IGNRESELCAUSE|忽略GGSN重选原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当GGSN向SGSN返回Create PDP Context Response响应消息，其中携带失败原因，表示PDP创建失败时，SGSN是否支持根据Create PDP Context Response消息中携带的失败原因值在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接，而不是等UE再次发起PDN建立请求。该参数包括两个选项：不忽略（Not Ignore）：即SGSN根据GGSN失败响应消息中携带的原因值确定是否进行GGSN重选，如果GGSN失败原因在参数“GGSN重选原因（GGSN Reselection Cause）”配置的原因列表中，则进行GGSN重选；反之，则不进行GGSN重选。忽略（Ignore）：即SGSN不根据GGSN失败响应携带的具体原因值确定是否进行GGSN重选，无论失败原因是什么都需要进行GGSN重选。
RESELCAUSE|GGSN重选原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数用于设置GGSN向SGSN返回Create PDP Context Response响应消息中携带的失败原因值。如果GGSN失败原因在本参数配置的原因列表中，则进行GGSN重选；反之，则不进行GGSN重选。该参数”忽略GGSN重选原因（Ignore GGSN Reselection Cause）配置为”不忽略（Not Ignore）“时，必须要设置本参数。
RESELNUM|GGSN重选次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该参数用于设置SGSN支持在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接的最大次数。如果当前重新选择的次数超过配置的次数，SGSN不会再进行重新选择，PDN连接建立失败。
命令举例 
设置GGSN重选策略，其中SGSN是否支持失败时重选GGSN设置为支持。 
SET GGSN RESELECT:RESELBYFAIL="YES",RESELNUM=1; 
父主题： [GGSN重选配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询GGSN重选策略(SHOW GGSN RESELECT) 
## 查询GGSN重选策略(SHOW GGSN RESELECT) 
命令功能 
该命令用于查询SGSN重新选择GGSN建立PDN连接的相关策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RESELBYFAIL|SGSN是否支持失败时重选GGSN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当GGSN向SGSN返回Create PDP Context Response响应消息，其中携带失败原因，表示PDP创建失败时，SGSN是否支持在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接，而不是等UE再次发起PDN建立请求。该参数包括两个选项：不支持（Not Support）：SGSN不支持在上述场景下，重新选择一个新的GGSN继续尝试建立PDN连接。支持（Support）：SGSN支持在上述场景下，重新选择一个新的GGSN继续尝试建立PDN连接。
RESELBYNORSP|SGSN是否支持无响应时重选GGSN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当GGSN超时未向SGSN返回Create PDP Context Response响应消息时，SGSN是否支持在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接，而不是等UE再次发起PDN建立请求。该参数包括两个选项：不支持（Not Support）：SGSN不支持在上述场景下，重新选择一个新的GGSN继续尝试建立PDN连接。支持（Support）：SGSN支持在上述场景下，重新选择一个新的GGSN继续尝试建立PDN连接。
ROAMURESEL|漫游用户是否重选GGSN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置如果是漫游用户，SGSN是否支持在以下两种情况下，从GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接，而不是等UE再次发起PDN建立请求。当GGSN向SGSN返回Create PDP Context Response响应消息，其中携带失败原因，表示PDP创建失败时。当GGSN超时未向SGSN返回Create PDP Context Response响应消息时。
ADDRDELMODE|GGSN重选地址删除方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN删除GGSN地址的方式。SGSN使用NAPTR（名称权威指针，Naming Authority Pointer）方式查询GGSN的IP地址时，如下两种情况下，以SGSN重选GGSN前，需要删除原来的GGSN地址。当GGSN向SGSN返回Create PDP Context Response响应消息，其中携带失败原因，表示PDP创建失败时。当GGSN超时未向SGSN返回Create PDP Context Response响应消息时。该参数包括两个选项：仅删除失败GGSN地址（Delete failed GGSN address only）：即该GGSN的一个地址。删除失败GGSN下所有地址（Delete all addresses for GGSN failed）：即该GGSN的所有地址。
IGNRESELCAUSE|忽略GGSN重选原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当GGSN向SGSN返回Create PDP Context Response响应消息，其中携带失败原因，表示PDP创建失败时，SGSN是否支持根据Create PDP Context Response消息中携带的失败原因值在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接，而不是等UE再次发起PDN建立请求。该参数包括两个选项：不忽略（Not Ignore）：即SGSN根据GGSN失败响应消息中携带的原因值确定是否进行GGSN重选，如果GGSN失败原因在参数“GGSN重选原因（GGSN Reselection Cause）”配置的原因列表中，则进行GGSN重选；反之，则不进行GGSN重选。忽略（Ignore）：即SGSN不根据GGSN失败响应携带的具体原因值确定是否进行GGSN重选，无论失败原因是什么都需要进行GGSN重选。
RESELCAUSE|GGSN重选原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数用于设置GGSN向SGSN返回Create PDP Context Response响应消息中携带的失败原因值。如果GGSN失败原因在本参数配置的原因列表中，则进行GGSN重选；反之，则不进行GGSN重选。该参数”忽略GGSN重选原因（Ignore GGSN Reselection Cause）配置为”不忽略（Not Ignore）“时，必须要设置本参数。
RESELNUM|GGSN重选次数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN支持在GGSN POOL中重新选择一个新的GGSN继续尝试建立PDN连接的最大次数。如果当前重新选择的次数超过配置的次数，SGSN不会再进行重新选择，PDN连接建立失败。
命令举例 
查询GGSN重选策略。 
SHOW GGSN RESELECT; 
`
命令 (No.1): SHOW GGSN RESELECT
操作维护 SGSN是否支持失败时重选GGSN SGSN是否支持无响应时重选GGSN 漫游用户是否重选GGSN GGSN重选地址删除方式 忽略GGSN重选原因 GGSN重选原因 GGSN重选次数 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改     不支持                     不支持                       否                   仅删除失败GGSN地址   忽略                          1 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.022 秒）。
` 
父主题： [GGSN重选配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# rSRVCC配置 
# rSRVCC配置 
背景知识 
SRVCC是3GPP提出的一种VoLTE语音业务连续性方案，主要是为了解决当单射频UE在LTE网络和2G/3G CS网络之间移动时，需要保证语音呼叫的连续性，即保证单射频UE在IMS控制的VoIP语音和CS域语音之间的平滑切换。但考虑到LTE网络在初期仅部署在热点、密集地区，小于2G/3G网络的覆盖，原有电路域语音业务不需要切换到LTE网络，因此SRVCC方案在提出时仅考虑了从E-UTRAN到UTRAN/GERAN的单向切换流程，并未给出从UTRAN/GERAN到E-UTRAN反方向的语言业务切换。 
随着LTE网络规模的不断发展，新业务的不断开发应用，为了使用户获得更好的业务体验，一旦用户发现有可连接的LTE网络，便需要从2G/3G网络切换到LTE网络；运营商也希望将业务转移到全新的网络，从而减少对传统网络的投入，加大LTE网络的部署。因此需要对SRVCC方案进行补充和完善，3GPP在R11版本中提出了反向SRVCC方案，即rSRVCC（Reverse SRVCC）。 
功能描述 
rSRVCC配置用于设置rSRVCC控制策略，即MME是否支持rSRVCC。 
相关主题 
 
设置rSRVCC控制策略(SET RSRVCC FLAG)
 
 
查询rSRVCC控制策略(SHOW RSRVCC FLAG)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置rSRVCC控制策略(SET RSRVCC FLAG) 
## 设置rSRVCC控制策略(SET RSRVCC FLAG) 
命令功能 
该命令用于配置rSRVCC控制策略，MME是否支持rSRVCC，当需要SGSN执行rSRVCC切换时，使用该命令。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPRSRVCC|MME是否支持rSRVCC|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持rSRVCC。不支持：MME不支持rSRVCC。支持：MME支持rSRVCC。
命令举例 
设置支持rSRVCC控制策略。 
SET RSRVCC FLAG:MMESUPRSRVCC="YES"; 
父主题： [rSRVCC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询rSRVCC控制策略(SHOW RSRVCC FLAG) 
## 查询rSRVCC控制策略(SHOW RSRVCC FLAG) 
命令功能 
该命令用于查询rSRVCC控制策略。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPRSRVCC|MME是否支持rSRVCC|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持rSRVCC。不支持：MME不支持rSRVCC。支持：MME支持rSRVCC。
命令举例 
查询rSRVCC控制策略。 
SHOW RSRVCC FLAG; 
`2016-11-10 12:00:03 命令 (No.1): SHOW RSRVCC FLAG
MME是否支持rSRVCC 
--------------------
支持 
--------------------
记录数 1
命令执行成功（耗时 0.032 秒）。` 
父主题： [rSRVCC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME SMS业务配置 
# MME SMS业务配置 
背景知识 
            
            UE注册到MME后，发送和接收短信有两种通道：通过MME和MSC以及SMSC或者通过MME和SMSC。
        
功能描述 
            
            SMS业务配置用于控制UE收发短信时是否从MME和SMSC的通道来完成。
        
相关主题 
 
设置SMS业务配置(SET SMS SERVICE)
 
 
查询SMS业务配置(SHOW SMS SERVICE)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置SMS业务配置(SET SMS SERVICE) 
## 设置SMS业务配置(SET SMS SERVICE) 
命令功能 
该命令用于设置MME是否支持SMS IN MME功能以及HSS注册时的需要携带的参数
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPSMSINMME|MME支持SMS IN MME功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置MME是否支持SMS IN MME的功能。注意：只有MME支持SMS IN MME的License打开，并且此开关打开时，MME才能支持SMS IN MME功能。
SMSONLY|UE指示SMS ONLY或者签约PS+SMS ONLY|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置当UE指示SMS ONLY或者UE签约了PS+SMS ONLY时，MME指示HSS的参数是SMS in MME Required还是SMS in MME Not Preferred
NONSMSONLY|UE未指示SMS ONLY并且无签约|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置当UE未指示SMS ONLY并且无UE签约数据时，MME指示HSS的参数是否是SMS in MME Not Preferred
命令举例 
设置SMS业务配置,将"MME支持SMS IN MME功能"设置为"支持"。 
SET SMS SERVICE:SUPSMSINMME="ON"; 
父主题： [MME SMS业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SMS业务配置(SHOW SMS SERVICE) 
## 查询SMS业务配置(SHOW SMS SERVICE) 
命令功能 
该命令用于查询MME是否支持SMS IN MME功能以及HSS注册时的需要携带的参数
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPSMSINMME|MME支持SMS IN MME功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置MME是否支持SMS IN MME的功能。注意：只有MME支持SMS IN MME的License打开，并且此开关打开时，MME才能支持SMS IN MME功能。
SMSONLY|UE指示SMS ONLY或者签约PS+SMS ONLY|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置当UE指示SMS ONLY或者UE签约了PS+SMS ONLY时，MME指示HSS的参数是SMS in MME Required还是SMS in MME Not Preferred
NONSMSONLY|UE未指示SMS ONLY并且无签约|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置当UE未指示SMS ONLY并且无UE签约数据时，MME指示HSS的参数是否是SMS in MME Not Preferred
命令举例 
查询SMS业务配置。 
SHOW SMS SERVICE; 
`
命令 (No.1): SHOW SMS SERVICE
操作维护  MME支持SMS IN MME功能  UE指示SMS ONLY或者签约PS+SMS ONLY   UE未指示SMS ONLY并且无签约
-----------------------------------------------------------------------------------------------
修改      支持                   SMS in MME Required                 SMS in MME Not Preferred   
-----------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.035 秒）。
` 
父主题： [MME SMS业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME CS/PS协作配置 
# MME CS/PS协作配置 
背景知识 
CS和PS协作，就是UE在CS域和PS域被同一运营商服务。 
在传统网络中，运营商总是会既部署自己的CS网络又部署自己的PS网络，并且UE在CS域和PS域总是被同一运营商服务。 
在共享网络中，多个运营商共享无线（MOCN），或者多个运营商共享无线和核心网（GWCN），为UE服务的运营商不止一个，当UE在CS和PS间来回移动或发起登记时，运营商希望尽可能保证UE登记在同一个运营商的CS域和PS域，避免跨PLMN的计费和用户管理等问题。 
在共享网络中，终端（其在2G/3G网络中不支持网络共享）回落到2G/3G网络使用CS域进行语音业务（即CSFB），或者终端进行语音呼叫时在LTE网络和2G/3G
CS网络之间移动（即SRVCC或者rSRVCC），MME/MSC和BSC/RNC协同，保证UE被同一运营商的CS域和PS域服务，完成CS/PS协作。 
功能描述 
            
            MME CS/PS协作配置用于设置CS/PS协作控制策略，即MME是否支持CS/PS协作。
        
相关主题 
 
设置CS/PS协作控制策略(SET CSPS COORDI)
 
 
查询CS/PS协作控制策略(SHOW CSPS COORDI)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置CS/PS协作控制策略(SET CSPS COORDI) 
## 设置CS/PS协作控制策略(SET CSPS COORDI) 
命令功能 
该命令用于配置MME的CS/PS协作控制策略，即MME是否支持CS/PS协作。当需要MME执行CS/PS协作时，使用该命令。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPCSPSCOORDI|MME是否支持CS/PS协作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持CS/PS协作。不支持：MME不支持CS/PS协作。支持：MME支持CS/PS协作。
命令举例 
设置MME支持CS/PS协作控制策略。 
SET CSPS COORDI:MMESUPCSPSCOORDI="YES"; 
父主题： [MME CS/PS协作配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询CS/PS协作控制策略(SHOW CSPS COORDI) 
## 查询CS/PS协作控制策略(SHOW CSPS COORDI) 
命令功能 
该命令用于查询MME的CS/PS协作控制策略。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPCSPSCOORDI|MME是否支持CS/PS协作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持CS/PS协作。不支持：MME不支持CS/PS协作。支持：MME支持CS/PS协作。
命令举例 
查询CS/PS协作控制策略。 
SHOW CSPS COORDI; 
`2017-03-02 11:13:50 命令 (No.1): SHOW CSPS COORDI
操作维护  MME是否支持CS/PS协作
------------------------------
修改      支持
------------------------------
记录数 1
命令执行成功（耗时 0.013 秒）。
` 
父主题： [MME CS/PS协作配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# VoLTE业务控制策略配置 
# VoLTE业务控制策略配置 
背景知识 
            
            随着VoLTE业务的开展，在各地运营过程中，可能存在不同的业务需求。
        
功能描述 
            
            本功能可以通过个性化配置来决定一些VoLTE的业务开展形式。如控制VoLTE用户在移动时接入当地还是原地域的网络。
        
相关主题 
 
设置VoLTE业务控制策略(SET VOLTECTRL)
 
 
查询VoLTE业务控制策略(SHOW VOLTECTRL)
 
 
漫游PLMN VoLTE接入方式配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置VoLTE业务控制策略(SET VOLTECTRL) 
## 设置VoLTE业务控制策略(SET VOLTECTRL) 
命令功能 
该命令用于配置VoLTE业务相关策略，主要是对接入控制策略进行配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IFIGNAPNOIREP|支持IMS APN忽略APN OI Replacement|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|出于运营需要，有时候对于VoLTE用户在区域间移动的情况，需要接入当地EPC网络。而如果此时HSS签约了UE级的APN-OI Replacement，VoLTE用户移动时，IMS APN被强制下插了APN-OI Replacement，会导致DNS解析后回到了原地域，不符合运营要求。因此通过配置来决定，是使用HSS签约的UE级的APN-OI Replacement来使VoLTE接入到原地域，还是忽略HSS签约的UE级的APN-OI Replacement，使用普通IMS APN FQDN进行DNS解析后接入到当地PGW：否：使用UE在HSS签约的APN OI Replacement进行DNS解析。网内用户支持：忽略网内用户在HSS签约的APN OI Replacement，使用普通IMS APN FQDN进行DNS解析，从而接入到当地PGW。网间用户支持：忽略网间用户在HSS签约的APN OI Replacement，使用普通IMS APN FQDN进行DNS解析，从而接入到当地PGW。所有用户都支持：忽略所有用户在HSS签约的APN OI Replacement，使用普通IMS APN FQDN进行DNS解析，从而接入到当地PGW。
TADSCHECKIMSPDN|是否支持T-ADS查询检查IMS PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当HSS请求T-ADS数据时，MME根据此参数综合判断用户当前是否存在IMS PDN连接以决策是否支持VoLTE能力。
VOLTEIMSIFUN|MME支持VoLTE漫游用户接入方式控制功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持漫游用户VoLTE业务策略控制功能。当打开本开关，则MME在用户发起VoLTE业务时，根据配置的策略选择S8HR方式还是REVAL方式。
命令举例 
此命令用于设置VoLTE业务控制策略配置。 
SET VOLTECTRL:IFIGNAPNOIREP="NO",TADSCHECKIMSPDN="NO",VOLTEIMSIFUN="NO"; 
父主题： [VoLTE业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询VoLTE业务控制策略(SHOW VOLTECTRL) 
## 查询VoLTE业务控制策略(SHOW VOLTECTRL) 
命令功能 
该命令用于查询VoLTE业务相关策略，包括接入控制策略。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IFIGNAPNOIREP|支持IMS APN忽略APN OI Replacement|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|出于运营需要，有时候对于VoLTE用户在区域间移动的情况，需要接入当地EPC网络。而如果此时HSS签约了UE级的APN-OI Replacement，VoLTE用户移动时，IMS APN被强制下插了APN-OI Replacement，会导致DNS解析后回到了原地域，不符合运营要求。因此通过配置来决定，是使用HSS签约的UE级的APN-OI Replacement来使VoLTE接入到原地域，还是忽略HSS签约的UE级的APN-OI Replacement，使用普通IMS APN FQDN进行DNS解析后接入到当地PGW：否：使用UE在HSS签约的APN OI Replacement进行DNS解析。网内用户支持：忽略网内用户在HSS签约的APN OI Replacement，使用普通IMS APN FQDN进行DNS解析，从而接入到当地PGW。网间用户支持：忽略网间用户在HSS签约的APN OI Replacement，使用普通IMS APN FQDN进行DNS解析，从而接入到当地PGW。所有用户都支持：忽略所有用户在HSS签约的APN OI Replacement，使用普通IMS APN FQDN进行DNS解析，从而接入到当地PGW。
TADSCHECKIMSPDN|是否支持T-ADS查询检查IMS PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当HSS请求T-ADS数据时，MME根据此参数综合判断用户当前是否存在IMS PDN连接以决策是否支持VoLTE能力。
VOLTEIMSIFUN|MME支持VoLTE漫游用户接入方式控制功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持漫游用户VoLTE业务策略控制功能。当打开本开关，则MME在用户发起VoLTE业务时，根据配置的策略选择S8HR方式还是REVAL方式。
命令举例 
此命令用于查询VoLTE业务控制策略。 
SHOW VOLTECTRL; 
`
2017-05-23 13:17:39 命令 (No.1): SHOW VOLTECTRL
支持IMS APN忽略APN OI Replacement      是否支持T-ADS查询检查IMS PDN连接      MME支持VoLTE漫游用户接入方式控制功能 
-----------------------------------------------------------------------------------------------------------------
否                                     不支持                                不支持 
-----------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [VoLTE业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 漫游PLMN VoLTE接入方式配置 
## 漫游PLMN VoLTE接入方式配置 
背景知识 
            
            VoLTE是基于IMS的语音业务。IMS由于支持多种接入和丰富的多媒体业务，成为全IP时代的核心网标准架构。VoLTE即Voice over LTE，它是一种IP数据传输技术，无需2G/3G网，全部业务承载于4G网络上，可实现数据与语音业务在同一网络下的统一。
        
功能描述 
            
            该功能用于控制漫游入用户的VoLTE业务的使用方式，如果配置为S8HR方式，则漫游入用户发起VoLTE业务时，MME选择用户归属的PGW以实现VoLTE业务；如果配置为REVAL方式，则漫游入用户发起VoLTE业务时，MME选择本地的PGW以实现VoLTE业务。
        
相关主题 
 
新增漫游PLMN VoLTE接入方式(ADD ROAM PLMN VOLTE POLICY)
 
 
修改漫游PLMN VoLTE接入方式(SET ROAM PLMN VOLTE POLICY)
 
 
删除漫游PLMN VoLTE接入方式(DEL ROAM PLMN VOLTE POLICY)
 
 
查询漫游PLMN VoLTE接入方式(SHOW ROAM PLMN VOLTE POLICY)
 
 
父主题： [VoLTE业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增漫游PLMN VoLTE接入方式(ADD ROAM PLMN VOLTE POLICY) 
### 新增漫游PLMN VoLTE接入方式(ADD ROAM PLMN VOLTE POLICY) 
命令功能 
该命令用于配置漫游PLMN VoLTE接入方式控制策略。当需要增加某些PLMN使用S8HR或者REVAL方式时，使用该命令。MME根据PLMN来判断，当用户归属的PLMN在配置列表中，则根据控制策略选择相应的方式。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
POLICYCTL|接入方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|用于控制漫游VoLTE用户选择策略，包括S8HR和REVAL两种方式。如果用户归属的PLMN在配置数据中，则MME根据配置来选择相应的方式。
命令举例 
增加基于PLMN的漫游PLMN VoLTE接入方式配置，其中PLMN为460-01，接入方式为S8HR。 
ADD ROAM PLMN VOLTE POLICY:PLMN="460"-"01",POLICYCTL="S8HR"; 
父主题： [漫游PLMN VoLTE接入方式配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改漫游PLMN VoLTE接入方式(SET ROAM PLMN VOLTE POLICY) 
### 修改漫游PLMN VoLTE接入方式(SET ROAM PLMN VOLTE POLICY) 
命令功能 
该命令用于修改漫游PLMN VoLTE的控制接入方式策略，当需要修改某些PLMN的控制策略时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
POLICYCTL|接入方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|用于控制漫游VoLTE用户选择策略，包括S8HR和REVAL两种方式。如果用户归属的PLMN在配置数据中，则MME根据配置来选择相应的方式。
命令举例 
修改基于PLMN的漫游PLMN VoLTE接入方式配置，其中PLMN为460-01，接入方式改为REVAL。 
SET ROAM PLMN VOLTE POLICY:PLMN="460"-"01",POLICYCTL="REVAL"; 
父主题： [漫游PLMN VoLTE接入方式配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除漫游PLMN VoLTE接入方式(DEL ROAM PLMN VOLTE POLICY) 
### 删除漫游PLMN VoLTE接入方式(DEL ROAM PLMN VOLTE POLICY) 
命令功能 
该命令用于删除漫游PLMN VoLTE的控制接入方式策略，当某些PLMN不需要进行控制时，使用该命令删除掉配置数据。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
命令举例 
删除基于PLMN的漫游PLMN VoLTE接入方式配置，其中PLMN为460-01。 
DEL ROAM PLMN VOLTE POLICY:PLMN="460"-"01"; 
父主题： [漫游PLMN VoLTE接入方式配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询漫游PLMN VoLTE接入方式(SHOW ROAM PLMN VOLTE POLICY) 
### 查询漫游PLMN VoLTE接入方式(SHOW ROAM PLMN VOLTE POLICY) 
命令功能 
该命令用于查询漫游PLMN VoLTE的控制接入方式策略，当需要查询某些PLMN使用的是何种策略时使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|PLMN（Public Land Mobile Network，公共陆地移动网络），是由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN = MCC + MNC，例如，46001是中国联通的PLMN，46002中国移动的PLMN，46003是中国电信的PLMN。
POLICYCTL|接入方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于控制漫游VoLTE用户选择策略，包括S8HR和REVAL两种方式。如果用户归属的PLMN在配置数据中，则MME根据配置来选择相应的方式。
命令举例 
显示基于PLMN的漫游PLMN VoLTE接入方式配置。 
SHOW ROAM PLMN VOLTE POLICY; 
`
命令 (No.1): SHOW ROAM PLMN VOLTE POLICY;
操作维护    PLMN    接入方式
------------------------------
复制 删除   460-01  REVAL
------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [漫游PLMN VoLTE接入方式配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME直接向UE获取IMSI配置 
# MME直接向UE获取IMSI配置 
背景知识 
UE在当前MME进行GUTI附着时，当前MME会首先向UE原来所在MME/SGSN发起Identification Request来获取IMSI；但在漫游的场景下，如果可以确定无法向某些PLMN的MME/SGSN发起这一查询，则可以跳过这一步骤，而直接向UE获取IMSI，以缩短附着时间。 
功能描述 
用于配置针对MME全局或针对某些PLMN的MME/SGSN，是否需要跳过局间ID请求步骤而直接向UE获取IMSI。配置前需要打开“MME支持直接向UE获取IMSI”的license开关。 
相关主题 
 
设置直接向UE获取IMSI的功能开关(SET MME UE ID REQ SW)
 
 
查询直接向UE获取IMSI的功能开关(SHOW MME UE ID REQ SW)
 
 
设置默认的直接向UE获取IMSI配置(SET MME DEFAULT ID REQ)
 
 
查询默认的直接向UE获取IMSI配置(SHOW MME DEFAULT ID REQ)
 
 
增加基于PLMN的直接向UE获取IMSI配置(ADD MME PLMN ID REQ)
 
 
修改基于PLMN的直接向UE获取IMSI配置(SET MME PLMN ID REQ)
 
 
删除基于PLMN的直接向UE获取IMSI配置(DEL MME PLMN ID REQ)
 
 
查询基于PLMN的直接向UE获取IMSI配置(SHOW MME PLMN ID REQ)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置直接向UE获取IMSI的功能开关(SET MME UE ID REQ SW) 
## 设置直接向UE获取IMSI的功能开关(SET MME UE ID REQ SW) 
命令功能 
该命令用于配置GUTI附着时，MME跳过局间ID请求，直接向UE获取IMSI的功能开关。
注意事项 
该配置为整个功能的开关。如果配置为不支持，则下面两组命令配置（即默认的直接向UE获取IMSI配置和针对特定PLMN的直接向UE获取IMSI配置）都不生效。
参数说明 
标识|名称|类型|说明
---|---|---|---
UECTRL|直接向UE获取IMSI的功能开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置MME是否支持直接向UE获取IMSI的功能开关。
命令举例 
打开MME向UE直接获取IMSI开关。 
SET MME UE ID REQ SW:UECTRL="YES"; 
父主题： [MME直接向UE获取IMSI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询直接向UE获取IMSI的功能开关(SHOW MME UE ID REQ SW) 
## 查询直接向UE获取IMSI的功能开关(SHOW MME UE ID REQ SW) 
命令功能 
该命令用于查询GUTI附着时，MME跳过局间ID请求，直接向UE获取IMSI的功能开关。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
UECTRL|直接向UE获取IMSI的功能开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置MME是否支持直接向UE获取IMSI的功能开关。
命令举例 
查询MME向UE直接获取IMSI的功能开关。 
SHOW MME UE ID REQ SW; 
`
命令 (No.2): SHOW MME UE ID REQ SW;
操作维护  直接向UE获取IMSI的功能开关
------------------------------------
修改      支持
------------------------------------
记录数 1
命令执行成功（耗时 0.15 秒）。
` 
父主题： [MME直接向UE获取IMSI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置默认的直接向UE获取IMSI配置(SET MME DEFAULT ID REQ) 
## 设置默认的直接向UE获取IMSI配置(SET MME DEFAULT ID REQ) 
命令功能 
该命令用于设置默认的直接向UE获取IMSI配置，配置针对其他非特定的PLMN，MME是否直接向UE获取IMSI。
注意事项 
对于未通过[ADD MME PLMN ID REQ]命令配置的其他PLMN，MME将使用此默认配置。
参数说明 
标识|名称|类型|说明
---|---|---|---
UECTRL|直接向UE获取IMSI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置默认针对其他非特定的PLMN，MME是否直接向UE获取IMSI。
命令举例 
设置默认的直接向UE获取IMSI配置。 
SET MME DEFAULT ID REQ:UECTRL="YES"; 
父主题： [MME直接向UE获取IMSI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询默认的直接向UE获取IMSI配置(SHOW MME DEFAULT ID REQ) 
## 查询默认的直接向UE获取IMSI配置(SHOW MME DEFAULT ID REQ) 
命令功能 
该命令用于查询默认的直接向UE获取IMSI配置。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
UECTRL|直接向UE获取IMSI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置默认针对其他非特定的PLMN，MME是否直接向UE获取IMSI。
命令举例 
查询默认的直接向UE获取IMSI配置。 
SHOW MME DEFAULT ID REQ; 
`
命令 (No.7): SHOW MME DEFAULT ID REQ;
操作维护  直接向UE获取IMSI
--------------------------
修改      是
--------------------------
记录数 1
命令执行成功（耗时 0.054 秒）。
` 
父主题： [MME直接向UE获取IMSI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 增加基于PLMN的直接向UE获取IMSI配置(ADD MME PLMN ID REQ) 
## 增加基于PLMN的直接向UE获取IMSI配置(ADD MME PLMN ID REQ) 
命令功能 
该命令用于增加某个PLMN的直接向UE获取IMSI配置，配置针对某个特定PLMN，MME是否直接向UE获取IMSI。
注意事项 
该配置为针对某个特定PLMN的配置，对于其他未通过此命令配置的PLMN，MME将采用默认的直接向UE获取IMSI配置。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联（ITU）统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
UECTRL|直接向UE获取IMSI|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|配置针对某个特定的PLMN，MME是否直接向UE获取IMSI。
命令举例 
新增特定PLMN的直接向UE获取IMSI配置，其中PLMN为"460"-"01"、向UE直接获取IMSI支持。 
ADD MME PLMN ID REQ:PLMN="460"-"01",UECTRL="YES"; 
父主题： [MME直接向UE获取IMSI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改基于PLMN的直接向UE获取IMSI配置(SET MME PLMN ID REQ) 
## 修改基于PLMN的直接向UE获取IMSI配置(SET MME PLMN ID REQ) 
命令功能 
该命令用于修改某个PLMN的直接向UE获取IMSI配置，配置针对某个特定PLMN，MME是否直接向UE获取IMSI。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联（ITU）统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
UECTRL|直接向UE获取IMSI|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|配置针对某个特定的PLMN，MME是否直接向UE获取IMSI。
命令举例 
修改特定PLMN的直接向UE获取IMSI配置，其中PLMN为"460"-"01"、向UE直接获取IMSI支持。 
SET MME PLMN ID REQ:PLMN="460"-"01",UECTRL="YES"; 
父主题： [MME直接向UE获取IMSI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除基于PLMN的直接向UE获取IMSI配置(DEL MME PLMN ID REQ) 
## 删除基于PLMN的直接向UE获取IMSI配置(DEL MME PLMN ID REQ) 
命令功能 
该命令用于删除某个PLMN的直接向UE获取IMSI配置。
注意事项 
删除该特定PLMN的配置后，针对该PLMN，MME将采用默认的直接向UE获取IMSI配置。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联（ITU）统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
命令举例 
删除PLMN为"460"-"01"的直接向UE获取IMSI配置。 
DEL MME PLMN ID REQ:PLMN="460"-"01"; 
父主题： [MME直接向UE获取IMSI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询基于PLMN的直接向UE获取IMSI配置(SHOW MME PLMN ID REQ) 
## 查询基于PLMN的直接向UE获取IMSI配置(SHOW MME PLMN ID REQ) 
命令功能 
该命令用于查询某个PLMN的直接向UE获取IMSI配置，即针对某个特定PLMN，MME是否直接向UE获取IMSI。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联（ITU）统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|由政府或政府所批准的经营者，为公众提供陆地移动通信业务目的而建立和经营的网络。PLMN码由MCC与MNC两部分组成，在本命令中使用"-"隔开，唯一识别某个国家或地区的一个移动通信网络。
UECTRL|直接向UE获取IMSI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置针对某个特定的PLMN，MME是否直接向UE获取IMSI。
命令举例 
查询PLMN为"460"-"01"的特定PLMN的直接向UE获取IMSI配置。 
SHOW MME PLMN ID REQ:PLMN="460"-"01"; 
`
命令 (No.9): SHOW MME PLMN ID REQ:PLMN="460"-"01";
操作维护    PLMN     直接向UE获取IMSI
-------------------------------------
复制 修改   460-01   是
-------------------------------------
记录数 1
命令执行成功（耗时 0.035 秒）。
` 
父主题： [MME直接向UE获取IMSI配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# EPC PDN类型转换配置 
# EPC PDN类型转换配置 
背景知识 
EPC系统，PGW默认支持IPv4v6双栈，MME也默认支持IPv4v6双栈。 
当漫游用户在拜访地附着或者发起UE请求PDN连接时，需要分配终端地址。如果漫游用户归属地特定的PGW不支持IPv4v6双栈，并且漫游用户签约错误（签约成IPv4v6双栈），UE请求的也是IPv4v6双栈，那么特定的PGW会返回失败，导致用户在拜访地接入失败。 
为了兼容这种特定的PGW不支持IPv4v6双栈，且用户签约错误（签约成IPv4v6双栈）的场景，可以通过拜访地MME的本地配置，灵活调整PDN Type，解决用户接入的问题，提高用户满意度，增加运营商收益。 
按照协议，PGW应该是支持双栈的，不支持双栈的PGW比较少，因此，本配置只针对此场景生效：UE请求的PDN类型是IPv4v6双栈，用户签约的PDN类型也是IPv4v6双栈时，可以通过“EPC PDN类型转换配置”，灵活配置PDN类型。 
功能描述 
EPC PDN类型转换配置包括： 
PDN类型转换默认策略配置。 
基于IMSI号段的PDN类型转换配置，即针对特定用户，可以配置特定的PDN类型。如：“PDN类型转换默认策略”支持IPv4v6双栈，特定的漫游用户可以配置不支持IPv4v6双栈。 
相关主题 
 
PDN类型转换默认策略配置
 
 
基于IMSI号段的PDN类型转换配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## PDN类型转换默认策略配置 
## PDN类型转换默认策略配置 
背景知识 
按照协议，PGW应该是支持双栈的，不支持双栈的PGW比较少。因此，提供PDN类型转换默认策略配置，以满足大部分场景。 
功能描述 
PDN类型转换默认策略配置，用于配置默认策略。 
相关主题 
 
设置PDN类型转换默认策略(SET PDN CONVERSION POLICY)
 
 
查询PDN类型转换默认策略(SHOW PDN CONVERSION POLICY)
 
 
父主题： [EPC PDN类型转换配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置PDN类型转换默认策略(SET PDN CONVERSION POLICY) 
### 设置PDN类型转换默认策略(SET PDN CONVERSION POLICY) 
命令功能 
该命令用于设置PDN类型转换默认策略。当IMSI在“基于IMSI号段的PDN类型转换配置”里没有匹配到，使用此处的默认策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PDNTYPE|PDN类型转换默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置PDN类型转换默认策略。取值含义如下：支持IPv4：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4。支持IPv6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv6。支持IPv4v6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4v6。
命令举例 
设置PDN类型转换默认策略支持IPv4v6。 
SET PDN CONVERSION POLICY:PDNTYPE="IPv4v6"; 
父主题： [PDN类型转换默认策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询PDN类型转换默认策略(SHOW PDN CONVERSION POLICY) 
### 查询PDN类型转换默认策略(SHOW PDN CONVERSION POLICY) 
命令功能 
该命令用于查询PDN类型转换默认策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PDNTYPE|PDN类型转换默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置PDN类型转换默认策略。取值含义如下：支持IPv4：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4。支持IPv6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv6。支持IPv4v6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4v6。
命令举例 
查询PDN类型转换默认策略。 
 SHOW PDN CONVERSION POLICY; 
`
命令 (No.1): SHOW PDN CONVERSION POLICY;
操作维护  PDN类型转换默认策略
-----------------------------
修改      支持IPv4v6
-----------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [PDN类型转换默认策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于IMSI号段的PDN类型转换配置 
## 基于IMSI号段的PDN类型转换配置 
背景知识 
按照协议，PGW应该是支持双栈的，不支持双栈的PGW比较少。但是也有一些漫游用户归属地特定的PGW不支持双栈。因此，可以通过基于IMSI号段的PDN类型转换配置，对这些漫游用户设置特定的PDN类型。 
功能描述 
基于IMSI号段的PDN类型转换配置，可以针对特定用户，配置特定的PDN类型。 
相关主题 
 
新增基于IMSI号段的PDN类型转换(ADD IMSI PDN CONVERSION)
 
 
修改基于IMSI号段的PDN类型转换(SET IMSI PDN CONVERSION)
 
 
删除基于IMSI号段的PDN类型转换(DEL IMSI PDN CONVERSION)
 
 
查询基于IMSI号段的PDN类型转换(SHOW IMSI PDN CONVERSION)
 
 
父主题： [EPC PDN类型转换配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于IMSI号段的PDN类型转换(ADD IMSI PDN CONVERSION) 
### 新增基于IMSI号段的PDN类型转换(ADD IMSI PDN CONVERSION) 
命令功能 
该命令用于设置基于IMSI号段的PDN类型转换。当需要为特定的IMSI号段设置特定的PDN类型时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
PDNTYPE|PDN类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于IMSI号段的PDN类型转换。取值含义如下：支持IPv4：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4。支持IPv6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv6。支持IPv4v6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4v6。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表明该配置的实际含义，配置特定名称作为备注。
命令举例 
新增基于IMSI号段的PDN类型转换，其中IMSI为“46012”、PDN类型为支持IPv4v6。 
ADD IMSI PDN CONVERSION:IMSI="46012",PDNTYPE="IPv4v6"; 
父主题： [基于IMSI号段的PDN类型转换配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于IMSI号段的PDN类型转换(SET IMSI PDN CONVERSION) 
### 修改基于IMSI号段的PDN类型转换(SET IMSI PDN CONVERSION) 
命令功能 
该命令用于修改基于IMSI号段的PDN类型转换。当需要修改特定IMSI号段对应的PDN类型时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
PDNTYPE|PDN类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于IMSI号段的PDN类型转换。取值含义如下：支持IPv4：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4。支持IPv6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv6。支持IPv4v6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4v6。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表明该配置的实际含义，配置特定名称作为备注。
命令举例 
修改IMSI为“46012”的PDN类型转换，将PDN类型修改为支持IPv4v6。 
SET IMSI PDN CONVERSION:IMSI="46012",PDNTYPE="IPv4v6"; 
父主题： [基于IMSI号段的PDN类型转换配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于IMSI号段的PDN类型转换(DEL IMSI PDN CONVERSION) 
### 删除基于IMSI号段的PDN类型转换(DEL IMSI PDN CONVERSION) 
命令功能 
该命令用于删除基于IMSI号段的PDN类型转换。当某个IMSI号段不再需要设置特定的PDN类型时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
命令举例 
删除IMSI为“46012”的PDN类型转换。 
DEL IMSI PDN CONVERSION:IMSI="46012"; 
父主题： [基于IMSI号段的PDN类型转换配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于IMSI号段的PDN类型转换(SHOW IMSI PDN CONVERSION) 
### 查询基于IMSI号段的PDN类型转换(SHOW IMSI PDN CONVERSION) 
命令功能 
该命令用于查询基于IMSI号段的PDN类型转换。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于设置IMSI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|该参数用于设置IMSI号段。
PDNTYPE|PDN类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于IMSI号段的PDN类型转换。取值含义如下：支持IPv4：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4。支持IPv6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv6。支持IPv4v6：用户请求的PDN类型是IPv4v6，用户在HSS签约的PDN类型也是IPv4v6，MME通过SGW带给PGW的PDN类型为IPv4v6。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表明该配置的实际含义，配置特定名称作为备注。
命令举例 
查询所有基于IMSI号段的PDN类型转换。 
SHOW IMSI PDN CONVERSION 
`
命令 (No.1): SHOW IMSI PDN CONVERSION;
操作维护         IMSI号段   PDN类型      用户别名
-------------------------------------------------
复制 修改 删除   46012      支持IPv4v6   
-------------------------------------------------
记录数 1
命令执行成功（耗时 0.054 秒）。
` 
父主题： [基于IMSI号段的PDN类型转换配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME头压缩配置 
# MME头压缩配置 
背景知识 
            
            Header Compression，即头压缩，是为了减少无线与核心网之间的流量的一种技术。通过头压缩，可以大大减少UE和MME之间的流量。
        
功能描述 
            
            本配置用于设置是否开启头压缩的功能。通过该配置开启了头压缩功能，MME与UE之间就可以使用头压缩的方式传递报文。
        
相关主题 
 
MME头压缩控制策略
 
 
MME头压缩属性
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MME头压缩控制策略 
## MME头压缩控制策略 
背景知识 
            
            Header Compression，即头压缩，是为了减少无线与核心网之间的流量的一种技术。通过头压缩，可以大大减少UE和MME之间的流量。
        
功能描述 
            
            本配置用于设置是否开启头压缩的功能。通过该配置开启了头压缩功能，MME与UE之间就可以使用头压缩的方式传递报文。
        
相关主题 
 
设置MME头压缩控制策略(SET MME HC FUNCION)
 
 
查询MME头压缩控制策略(SHOW MME HC FUNCION)
 
 
父主题： [MME头压缩配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置MME头压缩控制策略(SET MME HC FUNCION) 
### 设置MME头压缩控制策略(SET MME HC FUNCION) 
命令功能 
该命令用于设置MME是否支持头压缩功能。 
当MME需要支持头压缩功能时，需要使用该命令开启头压缩功能开关。 
在该命令执行成功后，MME与UE之间可以使用头压缩的方式传递报文。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
HCFUNCTION|支持头压缩功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持头压缩功能。此配置设置为“支持”，MME方能支持头压缩功能。
命令举例 
设置MME头压缩控制策略。 
SET MME HC FUNCION:HCFUNCTION="YES"; 
父主题： [MME头压缩控制策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询MME头压缩控制策略(SHOW MME HC FUNCION) 
### 查询MME头压缩控制策略(SHOW MME HC FUNCION) 
命令功能 
该命令用于查询MME是否支持头压缩功能。 
注意事项 
无 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
HCFUNCTION|支持头压缩功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持头压缩功能。此配置设置为“支持”，MME方能支持头压缩功能。
命令举例 
查询MME头压缩控制策略。 
SHOW MME HC FUNCION; 
`
命令 (No.1): SHOW MME HC FUNCION;
支持头压缩功能 
-----------------
支持 
-----------------
记录数 1
命令执行成功（耗时 0.029 秒）。
` 
父主题： [MME头压缩控制策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MME头压缩属性 
## MME头压缩属性 
背景知识 
MME支持头压缩，需要与UE协商多个属性。 
PROFILE：用于指示压缩使用哪个类型的算法。 
MAX_CID：最大支持的CID（Context Identifier，上下文标识）数值。 
功能描述 
            
            MME头压缩属性配置用于设置MME支持哪些PROFILE以及支持的MAX_CID。
        
相关主题 
 
设置MME头压缩属性(SET MME HC ATTRIBUTE)
 
 
查询MME头压缩属性(SHOW MME HC ATTRIBUTE)
 
 
父主题： [MME头压缩配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置MME头压缩属性(SET MME HC ATTRIBUTE) 
### 设置MME头压缩属性(SET MME HC ATTRIBUTE) 
命令功能 
该命令用于设置支持头压缩的相关属性参数。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
HCMAXCID|MAX_CID|参数可选性:任选参数；参数类型:整数；参数范围为:1~16383。|该参数用于设置MME与UE之间最大支持的CID（Context Identifier，上下文标识）数值。
HCPROFILE|头压缩PROFILE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME支持头压缩的RoHC PROFILE。PROFILE：用于指示压缩使用哪个类型的算法。
命令举例 
设置MME头压缩属性。 
SET MME HC ATTRIBUTE:HCMAXCID=1,HCPROFILE="UDP/IP"; 
父主题： [MME头压缩属性]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询MME头压缩属性(SHOW MME HC ATTRIBUTE) 
### 查询MME头压缩属性(SHOW MME HC ATTRIBUTE) 
命令功能 
该命令用于查询头压缩的相关属性参数。 
注意事项 
无 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
HCMAXCID|MAX_CID|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME与UE之间最大支持的CID（Context Identifier，上下文标识）数值。
HCPROFILE|头压缩PROFILE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME支持头压缩的RoHC PROFILE。PROFILE：用于指示压缩使用哪个类型的算法。
命令举例 
查询MME头压缩属性。 
SHOW MME HC ATTRIBUTE; 
`
命令 (No.1): SHOW MME HC ATTRIBUTE;
MAX_CID   头压缩PROFILE 
-----------------------
1         RoHC profile 0x0002 (UDP/IP)
-----------------------
记录数 1
命令执行成功（耗时 0.029 秒）。
` 
父主题： [MME头压缩属性]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME IMEI检查频次配置 
# MME IMEI检查频次配置 
背景知识 
IMEI检查功能是指在UE Attach过程中，MME获取UE的IMEI（International Mobile Equipment Identity，国际移动设备标识）信息，并将其发送给EIR（Equipment Identity Register，设备标识寄存器）进行合法性检查的业务。MME收到EIR返回的检查结果后，根据EIR返回的结果（黑名单、白名单、灰名单）决定是否允许UE接入。通过IMEI检查功能，可以确认终端的合法性，从而禁止非法终端进入网络。 
功能描述 
为了减轻EIR的负荷，在确保UE的有效性的前提下，可以通过减少IMEI检查的次数。 
本配置用于配置附着和TAU时的IMEI检查的频次，即附着或者TAU流程每执行N次，进行1次IMEI检查。 
相关主题 
 
设置MME IMEI检查频次(SET MME DEFAULT IMEI CHECK)
 
 
查询MME IMEI检查频次(SHOW MME DEFAULT IMEI CHECK)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置MME IMEI检查频次(SET MME DEFAULT IMEI CHECK) 
## 设置MME IMEI检查频次(SET MME DEFAULT IMEI CHECK) 
命令功能 
该命令用于设置MME按照业务类型进行IMEI检查，以及检查的频次。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SERVICETYPE|业务类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME附着/TAU业务时是否需要对UE终端进行IMEI检查。
CHECKTYPE|检查类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME附着/TAU业务是否进行IMEI检查。
FREQUENCY|检查周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置MME附着/TAU业务进行IMEI检查的频次，即当附着/TAU次数达到这个频次时，进行一次IMEI检查过程。
命令举例 
设置业务类型为“附着”和检查类型为“强制检查”的“检查周期频次”为3，命令如下： 
SET MME DEFAULT IMEI CHECK:SERVICETYPE="ATTACH",CHECKTYPE="FORCE",FREQUENCY=3; 
父主题： [MME IMEI检查频次配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME IMEI检查频次(SHOW MME DEFAULT IMEI CHECK) 
## 查询MME IMEI检查频次(SHOW MME DEFAULT IMEI CHECK) 
命令功能 
该命令用于查询MME按照业务类型进行IMEI检查，以及检查的频次。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME附着/TAU业务时是否需要对UE终端进行IMEI检查。
CHECKTYPE|检查类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME附着/TAU业务是否进行IMEI检查。
FREQUENCY|检查周期频次|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME附着/TAU业务进行IMEI检查的频次，即当附着/TAU次数达到这个频次时，进行一次IMEI检查过程。
命令举例 
查询MME IMEI检查频次 
SHOW MME DEFAULT IMEI CHECK; 
`
SHOW MME DEFAULT IMEI CHECK;
操作维护  业务类型  检查类型    检查周期频次 
--------------------------------------------
修改      附着      强制检查    1 
修改      局内TAU   强制检查    1 
修改      局间TAU   强制检查    1 
--------------------------------------------
记录数 3
命令执行成功（耗时 0.083 秒）。
` 
父主题： [MME IMEI检查频次配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# NSA业务配置 
# NSA业务配置 
背景知识 
同任何新网络建设一样，5G网络建设过程也是从热点到稍广覆盖、再到全网覆盖的过程。当用户移动到没有5G网络覆盖的地方，需要能够继续使用移动网络，所以网络侧和终端侧必须支持用户在5G网络与4G网络之间切换时的业务连续性，从而真正达到移动通信网络的目的：随时随地都能接入。 
5G网络的部署主要由RAN无线接入网（Radio Access Network，无线接入网）和核心网（Core Network）两部分组成。 
 
无线接入网主要由基站组成（LTE/NR），为用户提供无线接入功能。
 
 
核心网则主要为用户提供互联网接入服务和相应的管理功能等。
 
 
由于5G不仅是为移动宽带设计，它要面向eMBB（增强型移动宽带）、URLLC（超可靠低时延通信）和mMTC（大规模机器通信）三大应用场景，为了满足需求，3GPP在定义协议/标准的时候把无线接入网（5G NR）和核心网（5G Core）进行了拆分，各自都需要独立演进到5G。 
考虑到新建5G网络的巨大投资和建网周期，同时也为了保护运营商4G建网的既有投资和快速上线5G服务，3GPP定义了NSA(Non-Standalone，非独立部署)和SA(Standalone，独立部署)两种组网架构，供运营商根据自己情况灵活选择5G建网策略。虽然NSA标准相对于SA成熟较早，但SA架构相对NSA架构支持全场景eMBB、uRLLC、mMTC，支持切片等优点，所以很多运营商初期都选择NSA建网，实现5G部署先发，后期按需逐渐向SA演进，或者直接建设SA网络。 
5G NSA组网是一种过渡方案，主要以提升热点区域带宽为主要目标，依托4G基站和核心网工作，没有独立信令面，在5G发展初期，5G手机芯片同时支持SA和NSA。 
NSA和SA网络主要区别如下： 
性质 
 
NSA网络属于非独立组网。
 
 
SA网络属于独立组网。
 
 
网级互通 
 
在NSA组网下，5G与4G在接入网级互通，互连复杂。
 
 
在SA组网下，5G网络独立于4G网络，5G与4G仅在核心网级互通，互连简单。
 
 
核心网侧的区别 
 
NSA：新建5G基站，可以使用4G核心网或新建5G核心网。
 
 
SA：新建5G基站，新建5G核心网。
 
 
运营商的区别 
 
NSA（非独立组网）可以看做是5G初期的一种过渡方案，而SA（独立组网）才是5G的完全体。
 
 
由于NSA组网需要4G、5G公用核心网，不能支持5G低时延的特性。随着5G网络的建设，将逐渐转向SA组网，或采用SA/NSA混合组网的方式。
 
 
功能描述 
NSA业务配置支持MME和SGSN网络下NSA功能相关业务配置，包括： 
 
MME NSA业务配置。
 
 
SGSN NSA业务配置。
 
 
相关主题 
 
MME NSA业务配置
 
 
SGSN NSA业务配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MME NSA业务配置 
## MME NSA业务配置 
背景知识 
同任何新网络建设一样，5G网络建设过程也是从热点到稍广覆盖、再到全网覆盖的过程。当用户移动到没有5G网络覆盖的地方，需要能够继续使用移动网络，所以网络侧和终端侧必须支持用户在5G网络与4G网络之间切换时的业务连续性，从而真正达到移动通信网络的目的：随时随地都能接入。 
5G网络的部署主要由RAN无线接入网（Radio Access Network，无线接入网）和核心网（Core Network）两部分组成。 
 
无线接入网主要由基站组成（LTE/NR），为用户提供无线接入功能。
 
 
核心网则主要为用户提供互联网接入服务和相应的管理功能等。
 
 
由于5G不仅是为移动宽带设计，它要面向eMBB（增强型移动宽带）、URLLC（超可靠低时延通信）和mMTC（大规模机器通信）三大应用场景，为了满足需求，3GPP在定义协议/标准的时候把无线接入网（5G NR）和核心网（5G Core）进行了拆分，各自都需要独立演进到5G。 
考虑到新建5G网络的巨大投资和建网周期，同时也为了保护运营商4G建网的既有投资和快速上线5G服务，3GPP定义了NSA（Non-Standalone，非独立部署）和SA（Standalone，独立部署）两种组网架构，供运营商根据自己情况灵活选择5G建网策略。虽然NSA标准相对于SA成熟较早，但SA架构相对NSA架构支持全场景eMBB（Enhanced Mobile Broadband，增强移动宽带）、uRLLC（Ultra Reliable and Low Latency Communication，超高可靠低延迟通信）、mMTC（Massive Machine Type Communication，海量机器类通信），支持切片等优点，所以很多运营商初期都选择NSA建网，实现5G部署先发，后期按需逐渐向SA演进，或者直接建设SA网络。 
其中5G NSA部署方式为：通过DC（Dual Connectivity，双连接）方式，NR（5G基站）接入EPC。 
功能描述 
5G NSA组网是一种4G到5G网络的过渡方案，主要以提升热点区域带宽为主要目标，依托现有的LTE无线接入和核心网为移动性管理和覆盖，没有独立信令面。为实现NSA组网，MME需要增加相关的配置数据以支持NSA组网。 
相关主题 
 
MME NSA业务控制策略配置
 
 
MME DCNR限制策略配置
 
 
MME支持QoS速率扩展控制配置
 
 
MME IMSI号段上报NR用量策略配置
 
 
父主题： [NSA业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME NSA业务控制策略配置 
### MME NSA业务控制策略配置 
背景知识 
按照3GPP规划，5G标准分为NSA（Non-Standalone非独立部署）和SA（Standalone独立部署）两种。其中5G NSA组网是一种过渡方案，主要以提升热点区域带宽为主要目标，依托4G基站和核心网工作，没有独立信令面。 
为实现NSA组网，MME需要增加配置支持NSA。 
功能描述 
MME NSA(Non-Standalone)业务控制策略配置包括： 
是否支持NSA。 
是否支持DCNR(Dual connectivity with NR)限制。 
是否支持5G QoS速率扩展。 
是否支持选择NC-NR(Network Capability-New Radio)的SGW。 
是否支持选择NC-NR的PGW。 
选择NC-NR的SGW失败是否重选。 
选择NC-NR的PGW失败是否重选。 
是否支持SGW用量报告。 
是否支持PGW用量报告。 
相关主题 
 
设置MME NSA业务控制策略(SET NSA CONTROL POLICY)
 
 
查询MME NSA业务控制策略(SHOW NSA CONTROL POLICY)
 
 
父主题： [MME NSA业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置MME NSA业务控制策略(SET NSA CONTROL POLICY) 
#### 设置MME NSA业务控制策略(SET NSA CONTROL POLICY) 
命令功能 
该命令用于配置MME NSA业务控制策略。当MME需要支持NSA组网时，使用该命令。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPNSA|是否支持NSA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持NSA(Non-Standalone)。不支持：不支持NSA。支持：支持NSA。
SUPDCNRRESTRICT|是否支持DCNR限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持DCNR(Dual connectivity with NR)限制。不支持：不支持DCNR限制。支持：支持DCNR限制。
SUPQOSEXT|是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持5G QoS速率扩展。不支持：不支持5G QoS速率扩展。支持：支持5G QoS速率扩展。
SUPSELNCNRSGW|是否支持选择NC-NR的SGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持选择NC-NR的SGW。不支持：不支持选择NC-NR的SGW。支持：支持选择NC-NR的SGW。
SUPSELNCNRPGW|是否支持选择NC-NR的PGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持选择NC-NR的PGW。不支持：不支持选择NC-NR的PGW。支持：支持选择NC-NR的PGW。
RESELSGWNCNRFAIL|选择可达的NC-NR的SGW失败后的策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME选择不在不可达SGW（即SGW的黑名单）的NC-NR的SGW失败后，可以使用该参数设置后续处理策略。0：不重选不具有NC-NR能力的SGW。此时MME从具有NC-NR能力但在黑名单中的SGW中任选一个SGW。如果所有SGW都不具有NC-NR能力，则选择SGW失败。1：优选具有NC-NR能力的SGW。此时MME从具有NC-NR能力但在黑名单中的SGW中任选一个SGW。如果所有SGW都不具有NC-NR能力，则从不具有NC-NR能力的SGW中选择SGW。2：优选普通SGW。此时MME从不具有NC-NR能力的SGW中选择SGW。如果所有SGW（包括具有NC-NR能力和不具有NC-NR能力的SGW）都不可达，则随机选择一个SGW。
RESELPGWNCNRFAIL|选择可达的NC-NR的PGW失败后的策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME选择不在不可达PGW（即PGW的黑名单）的NC-NR的PGW失败后，可以使用该参数设置后续处理策略。0：不重选不具有NC-NR能力的PGW。此时MME从具有NC-NR能力但在黑名单中的PGW中任选一个PGW。如果所有PGW都不具有NC-NR能力，则选择PGW失败。1：优选具有NC-NR能力的PGW。此时MME从具有NC-NR能力但在黑名单中的PGW中任选一个PGW。如果所有PGW都不具有NC-NR能力，则从不具有NC-NR能力的PGW中选择PGW。
SUPSGWUSEDATARPT|是否支持SGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持SGW用量报告。不支持：不支持SGW用量报告。支持：支持SGW用量报告。
SUPPGWUSEDATARPT|是否支持PGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持PGW用量报告。不支持：不支持PGW用量报告。支持：支持PGW用量报告。
SUPUE5GSECCAPA|是否支持UE 5G安全能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持UE 5G安全能力。不支持：不支持UE 5G安全能力。支持：支支持UE 5G安全能力。
SGWFOURSTEPNCNROPTM|SGW四步查询时支持选择仅S11接口有nc-nr能力的nc-nr SGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME选择SGW时，如果需要四步查询，且DNS Server返回的SGW的Service Parameter中，S5和S8接口都没有携带nc-nr能力，仅有S11接口携带了nc-nr能力，MME通过该开关控制认为该SGW是否具有nc-nr能力。否：认为仅S11接口携带了nc-nr能力的SGW不具有NC-NR能力。是：认为仅S11接口携带了nc-nr能力的SGW具有NC-NR能力。
命令举例 
设置MME NSA业务控制策略 是否支持NSA为支持，是否支持DCNR限制为支持. 
SET NSA CONTROL POLICY:SUPNSA="YES",SUPDCNRRESTRICT="YES"; 
父主题： [MME NSA业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MME NSA业务控制策略(SHOW NSA CONTROL POLICY) 
#### 查询MME NSA业务控制策略(SHOW NSA CONTROL POLICY) 
命令功能 
该命令用于查询MME NSA业务控制策略。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPNSA|是否支持NSA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持NSA(Non-Standalone)。不支持：不支持NSA。支持：支持NSA。
SUPDCNRRESTRICT|是否支持DCNR限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持DCNR(Dual connectivity with NR)限制。不支持：不支持DCNR限制。支持：支持DCNR限制。
SUPQOSEXT|是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持5G QoS速率扩展。不支持：不支持5G QoS速率扩展。支持：支持5G QoS速率扩展。
SUPSELNCNRSGW|是否支持选择NC-NR的SGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持选择NC-NR的SGW。不支持：不支持选择NC-NR的SGW。支持：支持选择NC-NR的SGW。
SUPSELNCNRPGW|是否支持选择NC-NR的PGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持选择NC-NR的PGW。不支持：不支持选择NC-NR的PGW。支持：支持选择NC-NR的PGW。
RESELSGWNCNRFAIL|选择可达的NC-NR的SGW失败后的策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME选择不在不可达SGW（即SGW的黑名单）的NC-NR的SGW失败后，可以使用该参数设置后续处理策略。0：不重选不具有NC-NR能力的SGW。此时MME从具有NC-NR能力但在黑名单中的SGW中任选一个SGW。如果所有SGW都不具有NC-NR能力，则选择SGW失败。1：优选具有NC-NR能力的SGW。此时MME从具有NC-NR能力但在黑名单中的SGW中任选一个SGW。如果所有SGW都不具有NC-NR能力，则从不具有NC-NR能力的SGW中选择SGW。2：优选普通SGW。此时MME从不具有NC-NR能力的SGW中选择SGW。如果所有SGW（包括具有NC-NR能力和不具有NC-NR能力的SGW）都不可达，则随机选择一个SGW。
RESELPGWNCNRFAIL|选择可达的NC-NR的PGW失败后的策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME选择不在不可达PGW（即PGW的黑名单）的NC-NR的PGW失败后，可以使用该参数设置后续处理策略。0：不重选不具有NC-NR能力的PGW。此时MME从具有NC-NR能力但在黑名单中的PGW中任选一个PGW。如果所有PGW都不具有NC-NR能力，则选择PGW失败。1：优选具有NC-NR能力的PGW。此时MME从具有NC-NR能力但在黑名单中的PGW中任选一个PGW。如果所有PGW都不具有NC-NR能力，则从不具有NC-NR能力的PGW中选择PGW。
SUPSGWUSEDATARPT|是否支持SGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持SGW用量报告。不支持：不支持SGW用量报告。支持：支持SGW用量报告。
SUPPGWUSEDATARPT|是否支持PGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持PGW用量报告。不支持：不支持PGW用量报告。支持：支持PGW用量报告。
SUPUE5GSECCAPA|是否支持UE 5G安全能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持UE 5G安全能力。不支持：不支持UE 5G安全能力。支持：支支持UE 5G安全能力。
SGWFOURSTEPNCNROPTM|SGW四步查询时支持选择仅S11接口有nc-nr能力的nc-nr SGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME选择SGW时，如果需要四步查询，且DNS Server返回的SGW的Service Parameter中，S5和S8接口都没有携带nc-nr能力，仅有S11接口携带了nc-nr能力，MME通过该开关控制认为该SGW是否具有nc-nr能力。否：认为仅S11接口携带了nc-nr能力的SGW不具有NC-NR能力。是：认为仅S11接口携带了nc-nr能力的SGW具有NC-NR能力。
命令举例 
查询MME NSA业务控制策略。 
SHOW NSA CONTROL POLICY; 
`
命令 (No.25): SHOW NSA CONTROL POLICY
操作维护  是否支持NSA   是否支持DCNR限制   是否支持5G QoS速率扩展   是否支持选择NC-NR的SGW   是否支持选择NC-NR的PGW   选择NC-NR的SGW失败是否重选   选择NC-NR的PGW失败是否重选   是否支持SGW用量报告   是否支持PGW用量报告
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      支持          支持               不支持                   不支持                   不支持                   不重选                       不重选                       不支持                不支持
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.027 秒）。
` 
父主题： [MME NSA业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME DCNR限制策略配置 
### MME DCNR限制策略配置 
背景知识 
MME支持NSA(Non-Stand Alone)的时候，可以配置是否支持DCNR(Dual connectivity with NR)限制功能。 
功能描述 
MME DCNR(Dual connectivity with NR)限制策略配置包括： 
DCNR(Dual connectivity with NR)限制默认策略配置。 
IMSI号段DCNR(Dual connectivity with NR)限制策略配置。 
相关主题 
 
设置DCNR限制默认策略(SET DCNR RESTRICT DEFAULT POLICY)
 
 
查询DCNR限制默认策略(SHOW DCNR RESTRICT DEFAULT POLICY)
 
 
新增IMSI号段DCNR限制策略(ADD IMSI DCNR RESTRICT POLICY)
 
 
修改IMSI号段DCNR限制策略(SET IMSI DCNR RESTRICT POLICY)
 
 
删除IMSI号段DCNR限制策略(DEL IMSI DCNR RESTRICT POLICY)
 
 
查询IMSI号段DCNR限制策略(SHOW IMSI DCNR RESTRICT POLICY)
 
 
父主题： [MME NSA业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置DCNR限制默认策略(SET DCNR RESTRICT DEFAULT POLICY) 
#### 设置DCNR限制默认策略(SET DCNR RESTRICT DEFAULT POLICY) 
命令功能 
该命令用于配置DCNR限制默认策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
DFTDCNR|DCNR限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识DCNR限制策略优先级。本地策略：使用本地配置的DCNR限制策略。签约值：无论HSS是否支持DCNR，都使用签约策略。HSS支持时取签约值，不支持时本地策略：HSS支持DCNR时使用签约策略，HSS不支持DCNR时使用本地策略。
LOCALPOLICY|MME本地DCNR限制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识全局本地DCNR限制策略。不限制：不限制DCNR。限制：限制DCNR。
命令举例 
配置MME本地DCNR限制策略为不限制，DCNR限制策略优先级为HSS优先。 
SET DCNR RESTRICT DEFAULT POLICY:DFTDCNR="HSS",LOCALPOLICY="NO"; 
父主题： [MME DCNR限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询DCNR限制默认策略(SHOW DCNR RESTRICT DEFAULT POLICY) 
#### 查询DCNR限制默认策略(SHOW DCNR RESTRICT DEFAULT POLICY) 
命令功能 
该命令用于查询DCNR限制默认策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DFTDCNR|DCNR限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识DCNR限制策略优先级。本地策略：使用本地配置的DCNR限制策略。签约值：无论HSS是否支持DCNR，都使用签约策略。HSS支持时取签约值，不支持时本地策略：HSS支持DCNR时使用签约策略，HSS不支持DCNR时使用本地策略。
LOCALPOLICY|MME本地DCNR限制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识全局本地DCNR限制策略。不限制：不限制DCNR。限制：限制DCNR。
命令举例 
查询DCNR限制默认策略。 
SHOW DCNR RESTRICT DEFAULT POLICY; 
`
命令 (No.1): SHOW DCNR RESTRICT DEFAULT POLICY
操作维护   DCNR限制策略优先级                    DCNR限制策略优先级 
--------------------------------------------------------------------
修改       HSS支持时取签约值，不支持时本地策略    不限制
--------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [MME DCNR限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增IMSI号段DCNR限制策略(ADD IMSI DCNR RESTRICT POLICY) 
#### 新增IMSI号段DCNR限制策略(ADD IMSI DCNR RESTRICT POLICY) 
命令功能 
该命令用于配置IMSI号段对应的DCNR限制策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于MME配置需要使用DCNR限制策略的IMSI号段。
IMSIDCNRRESTRIC|DCNR限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识该IMSI号段的DCNR限制策略优先级。本地策略：使用本地配置的DCNR限制策略。签约值：无论HSS是否支持DCNR，都使用签约策略。HSS支持时取签约值，不支持时本地策略：HSS支持DCNR时使用签约策略，HSS不支持DCNR时使用本地策略。
IMSILOCALPOLICY|MME本地DCNR限制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识该IMSI号段的全局本地DCNR限制策略。不限制：不限制DCNR。限制：限制DCNR。
命令举例 
新增IMSI号段为460020012700100的MME本地DCNR限制策略为不限制，DCNR限制策略优先级HSS优先。 
ADD IMSI DCNR RESTRICT POLICY:IMSI="460020012700100",IMSIDCNRRESTRIC="HSS",IMSILOCALPOLICY="NO"; 
父主题： [MME DCNR限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改IMSI号段DCNR限制策略(SET IMSI DCNR RESTRICT POLICY) 
#### 修改IMSI号段DCNR限制策略(SET IMSI DCNR RESTRICT POLICY) 
命令功能 
该命令用于修改IMSI号段对应的DCNR限制策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于MME配置需要使用DCNR限制策略的IMSI号段。
IMSIDCNRRESTRIC|DCNR限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识该IMSI号段的DCNR限制策略优先级。本地策略：使用本地配置的DCNR限制策略。签约值：无论HSS是否支持DCNR，都使用签约策略。HSS支持时取签约值，不支持时本地策略：HSS支持DCNR时使用签约策略，HSS不支持DCNR时使用本地策略。
IMSILOCALPOLICY|MME本地DCNR限制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识该IMSI号段的全局本地DCNR限制策略。不限制：不限制DCNR。限制：限制DCNR。
命令举例 
设置IMSI号段为460020012700100的MME本地DCNR限制策略为不限制，DCNR限制策略优先级HSS优先。 
SET IMSI DCNR RESTRICT POLICY:IMSI="460020012700100",IMSIDCNRRESTRIC="HSS",IMSILOCALPOLICY="NO"; 
父主题： [MME DCNR限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除IMSI号段DCNR限制策略(DEL IMSI DCNR RESTRICT POLICY) 
#### 删除IMSI号段DCNR限制策略(DEL IMSI DCNR RESTRICT POLICY) 
命令功能 
该命令用于删除IMSI号段对应的DCNR限制策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于MME配置需要使用DCNR限制策略的IMSI号段。
命令举例 
删除IMSI号段为460020012700100的DCNR限制策略。 
DEL IMSI DCNR RESTRICT POLICY:IMSI="460020012700100"; 
父主题： [MME DCNR限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询IMSI号段DCNR限制策略(SHOW IMSI DCNR RESTRICT POLICY) 
#### 查询IMSI号段DCNR限制策略(SHOW IMSI DCNR RESTRICT POLICY) 
命令功能 
该命令用于查询IMSI号段对应的DCNR限制策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于MME配置需要使用DCNR限制策略的IMSI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于MME配置需要使用DCNR限制策略的IMSI号段。
IMSIDCNRRESTRIC|DCNR限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识该IMSI号段的DCNR限制策略优先级。本地策略：使用本地配置的DCNR限制策略。签约值：无论HSS是否支持DCNR，都使用签约策略。HSS支持时取签约值，不支持时本地策略：HSS支持DCNR时使用签约策略，HSS不支持DCNR时使用本地策略。
IMSILOCALPOLICY|MME本地DCNR限制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识该IMSI号段的全局本地DCNR限制策略。不限制：不限制DCNR。限制：限制DCNR。
命令举例 
查询IMSI号段为460020012700100的DCNR限制策略。 
SHOW IMSI DCNR RESTRICT POLICY:IMSI="460020012700100"; 
`
命令 (No.1): SHOW IMSI DCNR RESTRICT POLICY:IMSI="460020012700100";
操作维护         IMSI              DCNR限制策略优先级   MME本地DCNR限制策略 
---------------------------------------------------------------------------
复制 修改 删除   460020012700100   签约值               不限制
---------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.024 秒）。
` 
父主题： [MME DCNR限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME支持QoS速率扩展控制配置 
### MME支持QoS速率扩展控制配置 
背景知识 
5G用户要支持下行20Gbps和上行10Gbps的最大速率，需要设置MME支持NSA组网，并对QoS参数中的MBR(Maximum Bit Rate)、GBR(Guaranteed Bit Rate)、APN-AMBR、UE-AMBR进行扩展（为了将来易于扩展，统一扩展到4Tbps）。 
为了满足这个需求，MME在各个接口支持单用户的QoS速率扩展。如果不支持扩展，速率最大能达到10Gbps。 
功能描述 
MME支持QoS速率扩展控制配置包括： 
S11接口是否支持5G QoS速率扩展。 
S10接口是否支持5G QoS速率扩展。 
S1接口是否支持5G QoS速率扩展。 
NAS接口是否支持5G QoS速率扩展。 
相关主题 
 
设置MME支持QoS速率扩展控制(SET QOS RATE EXTCTRL)
 
 
查询MME支持QoS速率扩展控制(SHOW QOS RATE EXTCTRL)
 
 
父主题： [MME NSA业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置MME支持QoS速率扩展控制(SET QOS RATE EXTCTRL) 
#### 设置MME支持QoS速率扩展控制(SET QOS RATE EXTCTRL) 
命令功能 
该命令用于设置MME支持5G QoS速率扩展控制。当需要设置MME各接口是否支持5G QoS速率扩展时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
S11SUPQOSEXT|S11接口是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置S11接口是否支持5G QoS速率扩展。0-不支持1-支持
S10SUPQOSEXT|S10接口是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置S10接口是否支持5G QoS速率扩展。0-不支持1-支持
S1SUPQOSEXT|S1接口是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置S1接口是否支持5G QoS速率扩展。0-不支持1-支持
NASSUPQOSEXT|NAS接口是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置NAS接口是否支持5g QoS速率扩展。0-不支持1-支持
NASPRER8SUPQOSEXT|NAS接口Pre-R8 QoS是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置NAS接口Pre-R8 QoS是否支持5G QoS速率扩展。Pre-R8 QoS是用户接入2G/3G网络使用的参数。0-不支持1-支持
命令举例 
设置MME支持QoS速率扩展控制，S11接口是否支持5G QoS速率扩展为支持，S10接口是否支持5G QoS速率扩展为支持。 
SET QOS RATE EXTCTRL:S11SUPQOSEXT="YES",S10SUPQOSEXT="YES"; 
父主题： [MME支持QoS速率扩展控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MME支持QoS速率扩展控制(SHOW QOS RATE EXTCTRL) 
#### 查询MME支持QoS速率扩展控制(SHOW QOS RATE EXTCTRL) 
命令功能 
该命令用于查询MME是否支持5G QoS速率扩展控制。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
S11SUPQOSEXT|S11接口是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置S11接口是否支持5G QoS速率扩展。0-不支持1-支持
S10SUPQOSEXT|S10接口是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置S10接口是否支持5G QoS速率扩展。0-不支持1-支持
S1SUPQOSEXT|S1接口是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置S1接口是否支持5G QoS速率扩展。0-不支持1-支持
NASSUPQOSEXT|NAS接口是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置NAS接口是否支持5G QoS速率扩展。0-不支持1-支持
NASPRER8SUPQOSEXT|NAS接口Pre-R8 QoS是否支持5G QoS速率扩展|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置NAS接口Pre-R8 QoS是否支持5G QoS速率扩展。Pre-R8 QoS是用户接入2G/3G网络使用的参数。0-不支持1-支持
命令举例 
查询MME支持QoS速率扩展控制。 
SHOW QOS RATE EXTCTRL; 
`
命令 (No.2): SHOW QOS RATE EXTCTRL
操作维护  S11接口是否支持5G QoS速率扩展   S10接口是否支持5G QoS速率扩展   S1接口是否支持5G QoS速率扩展   NAS接口是否支持5G QoS速率扩展    NAS接口Pre-R8 QoS是否支持5G QoS速率扩展
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      支持                            支持                            不支持                         不支持                           不支持
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [MME支持QoS速率扩展控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME IMSI号段上报NR用量策略配置 
### MME IMSI号段上报NR用量策略配置 
背景知识 
根据3GPP协议，5G部署有两种方式： NSA（Non-Standalone非独立部署）和SA（Standalone独立部署）。其中5G NSA部署方式为：通过DC（Dual Connectivity双连接）方式，NR（5G基站）接入EPC。 
MME支持NSA时，eNodeB可以上报NR用量给MME，MME把NR用量再上报给SGW和/或PGW。 
功能描述 
MME IMSI号段上报NR用量策略配置包括：指定IMSI号段是否需上报NR用量给SGW和/或PGW。 
相关主题 
 
新增IMSI号段上报NR用量策略(ADD IMSI NR USAGE POLICY)
 
 
修改IMSI号段上报NR用量策略(SET IMSI NR USAGE POLICY)
 
 
删除IMSI号段上报NR用量策略(DEL IMSI NR USAGE POLICY)
 
 
查询IMSI号段上报NR用量策略(SHOW IMSI NR USAGE POLICY)
 
 
父主题： [MME NSA业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增IMSI号段上报NR用量策略(ADD IMSI NR USAGE POLICY) 
#### 新增IMSI号段上报NR用量策略(ADD IMSI NR USAGE POLICY) 
命令功能 
该命令用于新增IMSI号段上报NR用量策略。当需要根据IMSI号段设置上报NR用量策略时，使用该命令。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段，IMSI，国际移动用户识别码，储存在SIM卡中，区别移动用户的标志。
SUPSGWUSEDATARPT|是否支持SGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持SGW用量报告。不支持：移动网络不支持SGW用量报告。支持：移动网络支持SGW用量报告。
SUPPGWUSEDATARPT|是否支持PGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持PGW用量报告。不支持：移动网络不支持PGW用量报告。支持：移动网络支持PGW用量报告。
命令举例 
新增IMSI号段上报NR用量策略,IMSI号段为4601111，不支持SGW用量报告，支持PGW用量报告 
ADD IMSI NR USAGE POLICY:IMSI="4601111",SUPSGWUSEDATARPT="NO",SUPPGWUSEDATARPT="YES" 
父主题： [MME IMSI号段上报NR用量策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改IMSI号段上报NR用量策略(SET IMSI NR USAGE POLICY) 
#### 修改IMSI号段上报NR用量策略(SET IMSI NR USAGE POLICY) 
命令功能 
该命令用于修改IMSI号段上报NR用量策略。当需要修改已配置的根据IMSI号段设置上报NR用量策略时，使用该命令。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段，IMSI，国际移动用户识别码，储存在SIM卡中，区别移动用户的标志。
SUPSGWUSEDATARPT|是否支持SGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持SGW用量报告。不支持：移动网络不支持SGW用量报告。支持：移动网络支持SGW用量报告。
SUPPGWUSEDATARPT|是否支持PGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持PGW用量报告。不支持：移动网络不支持PGW用量报告。支持：移动网络支持PGW用量报告。
命令举例 
修改IMSI号段上报NR用量策略,IMSI号段为4601111，支持SGW用量报告，不支持PGW用量报告 
SET IMSI NR USAGE POLICY:IMSI="4601111",SUPSGWUSEDATARPT="YES",SUPPGWUSEDATARPT="NO" 
父主题： [MME IMSI号段上报NR用量策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除IMSI号段上报NR用量策略(DEL IMSI NR USAGE POLICY) 
#### 删除IMSI号段上报NR用量策略(DEL IMSI NR USAGE POLICY) 
命令功能 
该命令用于删除IMSI号段上报NR用量策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段，IMSI，国际移动用户识别码，储存在SIM卡中，区别移动用户的标志。
命令举例 
删除IMSI号段上报NR用量策略,IMSI号段为4601111。 
DEL IMSI NR USAGE POLICY:IMSI="4601111" 
父主题： [MME IMSI号段上报NR用量策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询IMSI号段上报NR用量策略(SHOW IMSI NR USAGE POLICY) 
#### 查询IMSI号段上报NR用量策略(SHOW IMSI NR USAGE POLICY) 
命令功能 
该命令用于查询IMSI号段上报NR用量策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段，IMSI，国际移动用户识别码，储存在SIM卡中，区别移动用户的标志。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段，IMSI，国际移动用户识别码，储存在SIM卡中，区别移动用户的标志。
SUPSGWUSEDATARPT|是否支持SGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持SGW用量报告。不支持：移动网络不支持SGW用量报告。支持：移动网络支持SGW用量报告。
SUPPGWUSEDATARPT|是否支持PGW用量报告|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持PGW用量报告。不支持：移动网络不支持PGW用量报告。支持：移动网络支持PGW用量报告。
命令举例 
查询IMSI号段上报NR用量策略。 
SHOW IMSI NR USAGE POLICY 
`
命令 (No.6): SHOW IMSI NR USAGE POLICY
操作维护       IMSI       是否支持SGW用量报告 是否支持PGW用量报告 
--------------------------------------------------------------------
复制 修改 删除    4601111   不支持             支持 
--------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.045 秒）。
` 
父主题： [MME IMSI号段上报NR用量策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## SGSN NSA业务配置 
## SGSN NSA业务配置 
背景知识 
同任何新网络建设一样，5G网络建设过程也是从热点到稍广覆盖、再到全网覆盖的过程。当用户移动到没有5G网络覆盖的地方，需要能够继续使用移动网络，所以网络侧和终端侧必须支持用户在5G网络与4G网络之间切换时的业务连续性，从而真正达到移动通信网络的目的：随时随地都能接入。 
5G网络的部署主要由RAN无线接入网（Radio Access Network，无线接入网）和核心网（Core Network）两部分组成。 
 
无线接入网主要由基站组成（LTE/NR），为用户提供无线接入功能。
 
 
核心网则主要为用户提供互联网接入服务和相应的管理功能等。
 
 
由于5G不仅是为移动宽带设计，它要面向eMBB（增强型移动宽带）、URLLC（超可靠低时延通信）和mMTC（大规模机器通信）三大应用场景，为了满足需求，3GPP在定义协议/标准的时候把无线接入网（5G NR）和核心网（5G Core）进行了拆分，各自都需要独立演进到5G。 
考虑到新建5G网络的巨大投资和建网周期，同时也为了保护运营商4G建网的既有投资和快速上线5G服务，3GPP定义了NSA（Non-Standalone，非独立部署）和SA（Standalone，独立部署）两种组网架构，供运营商根据自己情况灵活选择5G建网策略。虽然NSA标准相对于SA成熟较早，但SA架构相对NSA架构支持全场景eMBB（Enhanced Mobile Broadband，增强移动宽带）、uRLLC（Ultra Reliable and Low Latency Communication，超高可靠低延迟通信）、mMTC（Massive Machine Type Communication，海量机器类通信），支持切片等优点，所以很多运营商初期都选择NSA建网，实现5G部署先发，后期按需逐渐向SA演进，或者直接建设SA网络。 
其中5G NSA部署方式为：通过DC（Dual Connectivity，双连接）方式，NR（5G基站）接入EPC。 
功能描述 
5G NSA组网是一种4G到5G网络的过渡方案，主要以提升热点区域带宽为主要目标，依托现有的LTE无线接入和核心网为移动性管理和覆盖，没有独立信令面。为实现NSA组网，SGSN需要增加相关的配置数据以支持NSA组网。 
相关主题 
 
SGSN NSA业务控制策略配置
 
 
父主题： [NSA业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### SGSN NSA业务控制策略配置 
### SGSN NSA业务控制策略配置 
背景知识 
根据3GPP协议，5G部署有两种方式： NSA（Non-Standalone非独立部署）和SA（Standalone独立部署）。其中5G NSA部署方式为：通过DC（Dual Connectivity双连接）方式，NR（5G基站）接入EPC。 
功能描述 
SGSN NSA业务控制策略配置包括： 
SGSN是否支持NSA。 
SGSN是否支持选择NC-NR的PGW。 
SGSN选择NC-NR的PGW失败是否重选。 
相关主题 
 
设置SGSN NSA业务控制策略(SET SGSN NSA POLICY)
 
 
查询SGSN NSA业务控制策略(SHOW SGSN NSA POLICY)
 
 
父主题： [SGSN NSA业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置SGSN NSA业务控制策略(SET SGSN NSA POLICY) 
#### 设置SGSN NSA业务控制策略(SET SGSN NSA POLICY) 
命令功能 
该命令用于设置SGSN NSA业务控制策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNSUPNSA|SGSN是否支持NSA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持NSA。不支持：不支持NSA。支持：支持NSA。
SGSNSUPSELNCNRPGW|SGSN是否支持选择NC-NR的PGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持选择NC-NR的PGW。NC-NR（Network Capability-New Radio）的PGW是指具有支持NR这一网络能力的PGW。不支持：不支持选择NC-NR的PGW。支持：支持选择NC-NR的PGW。
SGSNRESELPGWNCNRFAIL|SGSN选择NC-NR的PGW失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGSN选择NC-NR的PGW失败后，可以根据该参数设置来决定是否重选。不重选：选择NC-NR的PGW失败后，不再重选NC-NR的PGW，而是选择普通的PGW。重选：选择NC-NR的PGW失败后，重选其他支持NC-NR的PGW。
命令举例 
设置SGSN NSA业务控制策略，SGSN支持NSA。 
SET SGSN NSA POLICY:SGSNSUPNSA="YES"; 
父主题： [SGSN NSA业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询SGSN NSA业务控制策略(SHOW SGSN NSA POLICY) 
#### 查询SGSN NSA业务控制策略(SHOW SGSN NSA POLICY) 
命令功能 
该命令用于查询SGSN NSA业务控制策略。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNSUPNSA|SGSN是否支持NSA/SGSN supports NSA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持NSA。不支持：不支持NSA。支持：支持NSA。
SGSNSUPSELNCNRPGW|SGSN是否支持选择NC-NR的PGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持选择NC-NR的PGW。NC-NR（Network Capability-New Radio）的PGW是指具有支持NR这一网络能力的PGW。不支持：不支持选择NC-NR的PGW。支持：支持选择NC-NR的PGW。
SGSNRESELPGWNCNRFAIL|SGSN选择NC-NR的PGW失败是否重选|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGSN选择NC-NR的PGW失败后，可以根据该参数设置来决定是否重选。不重选：选择NC-NR的PGW失败后，不再重选NC-NR的PGW，而是选择普通的PGW。重选：选择NC-NR的PGW失败后，重选其他支持NC-NR的PGW。
命令举例 
查询SGSN NSA业务控制策略。 
SHOW SGSN NSA POLICY; 
`
命令 (No.1): SHOW SGSN NSA POLICY;
操作维护                       SGSN是否支持NSA             SGSN是否支持选择NC-NR的PGW        SGSN选择NC-NR的PGW失败是否重选
------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除                     支持                               不支持                             重选
------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [SGSN NSA业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN IMEI检查频次配置 
# SGSN IMEI检查频次配置 
背景知识 
IMEI检查功能是指在UE Attach过程中，MME获取UE的IMEI（International Mobile Equipment Identity，国际移动设备标识）信息，并将其发送给EIR（Equipment Identity Register，设备标识寄存器）进行合法性检查的业务。SGSN收到EIR返回的检查结果后，根据EIR返回的结果（黑名单、白名单、灰名单）决定是否允许UE接入。通过IMEI检查功能，可以确认终端的合法性，从而禁止非法终端进入网络。 
功能描述 
为了减轻EIR的负荷，在确保UE的有效性的前提下，可以通过减少IMEI检查的次数 
本配置用于配置附着和RAU时的IMEI检查的频次，即附着或者RAU流程每执行N次，进行1次IMEI检查。 
相关主题 
 
设置SGSN IMEI检查频次(SET SGSN DEFAULT IMEI CHECK)
 
 
查询SGSN IMEI检查频次(SHOW SGSN DEFAULT IMEI CHECK)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置SGSN IMEI检查频次(SET SGSN DEFAULT IMEI CHECK) 
## 设置SGSN IMEI检查频次(SET SGSN DEFAULT IMEI CHECK) 
命令功能 
该命令用于设置SGSN按照业务类型进行IMEI检查，以及检查的频次。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SERVICETYPE|业务类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN附着/RAU业务时是否需要对UE终端进行IMEI检查。
CHECKTYPE|检查类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN附着/RAU业务是否进行IMEI检查。
FREQUENCY|检查周期频次|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置SGSN附着/RAU业务进行IMEI检查的频次，即当附着/RAU次数达到这个频次时，进行一次IMEI检查过程。
命令举例 
设置业务类型为“附着”和检查类型为“强制检查”的“检查周期频次”为3，命令如下： 
SET SGSN DEFAULT IMEI CHECK:SERVICETYPE="ATTACH",CHECKTYPE="FORCE",FREQUENCY=3; 
父主题： [SGSN IMEI检查频次配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN IMEI检查频次(SHOW SGSN DEFAULT IMEI CHECK) 
## 查询SGSN IMEI检查频次(SHOW SGSN DEFAULT IMEI CHECK) 
命令功能 
该命令用于设置SGSN按照业务类型进行IMEI检查，以及检查的频次。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SERVICETYPE|业务类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN附着/RAU业务时是否需要对UE终端进行IMEI检查。
CHECKTYPE|检查类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN附着/RAU业务是否进行IMEI检查。
FREQUENCY|检查周期频次|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN附着/RAU业务进行IMEI检查的频次，即当附着/RAU次数达到这个频次时，进行一次IMEI检查过程。
命令举例 
查询SGSN IMEI检查频次 
SHOW SGSN DEFAULT IMEI CHECK; 
`
SHOW SGSN DEFAULT IMEI CHECK;
操作维护  业务类型  检查类型    检查周期频次 
--------------------------------------------
修改      附着      强制检查    1 
修改      局内TAU   强制检查    1 
修改      局间TAU   强制检查    1 
--------------------------------------------
记录数 3
命令执行成功（耗时 0.083 秒）。
` 
父主题： [SGSN IMEI检查频次配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME ePCO配置 
# MME ePCO配置 
背景知识 
MME网元支持NB-IoT后，S1和GTP口消息的PCO字段增加了APN Rate Control（APN速率控制）的内容，此时PCO定义的长度存在容纳不下的可能性，因此提出了ePCO（Extended PCO）的概念，ePCO与PCO的区别在于ePCO支持携带更大长度的内容。 
功能描述 
MME ePCO配置用于设置ePCO控制策略。主要包括： 
1. MME是否支持ePCO。该配置决定了MME是否处理消息中携带的ePCO字段。 
2. MME是否支持承载级别的ePCO。该配置决定了MME是否处理消息中携带的承载级别的ePCO字段。 
3. 局间消息是否携带ePCO标识。该配置决定了当前MME网元是否携带ePCO标识给其他MME。 
相关主题 
 
设置ePCO控制策略(SET MME EPCO)
 
 
查询ePCO控制策略(SHOW MME EPCO)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置ePCO控制策略(SET MME EPCO) 
## 设置ePCO控制策略(SET MME EPCO) 
命令功能 
该命令用于配置ePCO控制策略：MME是否支持ePCO，当需要MME支持处理ePCO参数时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPEPCO|MME是否支持ePCO|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持ePCO。不支持：MME不支持ePCO。支持：MME支持ePCO。
SENDEPCOFG|MME是否支持在局间消息中携带ePCO标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持在局间消息中携带ePCO标识。不支持：MME不支持在局间消息中携带ePCO标识。支持：MME支持在局间消息中携带ePCO标识。
命令举例 
设置ePCO控制策略。 
SET MME EPCO:SUPEPCO="NO",SENDEPCOFG="YES"; 
父主题： [MME ePCO配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询ePCO控制策略(SHOW MME EPCO) 
## 查询ePCO控制策略(SHOW MME EPCO) 
命令功能 
该命令用于查询MME ePCO控制策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPEPCO|MME是否支持ePCO|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持ePCO。不支持：MME不支持ePCO。支持：MME支持ePCO。
SENDEPCOFG|MME是否支持在局间消息中携带ePCO标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持在局间消息中携带ePCO标识。不支持：MME不支持在局间消息中携带ePCO标识。支持：MME支持在局间消息中携带ePCO标识。
命令举例 
查询ePCO控制策略。 
SHOW MME EPCO; 
`
命令 (No.4): SHOW MME EPCO
操作维护  MME是否支持ePCO   MME是否支持在局间消息中携带ePCO标识
---------------------------------------------------------------
修改      不支持            支持
---------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.079 秒）。
` 
父主题： [MME ePCO配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 基于PLMN的无线覆盖增强与CE mode B控制策略配置 
# 基于PLMN的无线覆盖增强与CE mode B控制策略配置 
背景知识 
无线覆盖增强功能是指在物联网终端面对复杂环境下信号覆盖差异问题时，系统通过深度覆盖功能，以便保证地下车库/地下室/地下管道等信号难以到达的地方的信号覆盖。 
物联网（IoT，Internet of Things）是未来信息技术发展的重要组成部分，其主要特点是将物品通过通信技术与网络连接，从而实现人机互连，物物互连的智能化网络。协议3GPP R13针对此类物联网业务的特点，基于LTE进行演进，设计了专门用于物联网的eMTC（Enhanced Machine Type Communication）技术。eMTC的特点是广覆盖（相对于LTE 15dB的覆盖增强）、低成本、低功耗、支持海量连接。 
为了兼顾eMTC UE的覆盖深度和容量性能，3GPP协议引入了CE（Coverage Enhancement，覆盖增强等级）。 
 
对处于空闲态的终端，划分了4个不同的覆盖等级（CE Level0~3）。
 
 
对处于连接态的终端，划分了CE Mode A和CE Mode B两个覆盖模式。
 
 
空闲态的覆盖等级和连接态的覆盖模式之间有对应的映射关系，通过不同的覆盖等级的差异化管理可以大大节省开销。 
CE Mode B是eMTC终端支持无线覆盖增强的一种制式。详细的信元解释请参见3GPP TS 36.413 Ve.4.0中9.2.1.118章节。 
功能描述 
当用户终端处于无线覆盖增强时，会要求占用额外的资源（比如：无线和信令资源）。此功能用于阻止一些特殊的用户终端使用无线覆盖增强业务。 
相关主题 
 
无线覆盖增强与CE mode B控制开关
 
 
无线覆盖增强与CE mode B控制策略配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 无线覆盖增强与CE mode B控制开关 
## 无线覆盖增强与CE mode B控制开关 
背景知识 
当用户处于无线覆盖增强时，会要求占用额外的资源（比如：无线和信令资源）。此功能用于阻止一些特殊的终端使用无线覆盖增强业务。 
功能描述 
无线覆盖增强是指在物联网终端面对复杂环境下信号覆盖差异问题时，系统通过深度覆盖功能，以便保证地下车库/地下室/地下管道等信号难以到达的地方的信号覆盖。 
CE Mode B是eMTC终端支持无线覆盖增强的一种制式。 
相关主题 
 
设置无线覆盖增强与CE mode B控制开关(SET ECOVRESTRIC CTRL)
 
 
查询无线覆盖增强与CE mode B控制开关(SHOW ECOVRESTRIC CTRL)
 
 
父主题： [基于PLMN的无线覆盖增强与CE mode B控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置无线覆盖增强与CE mode B控制开关(SET ECOVRESTRIC CTRL) 
### 设置无线覆盖增强与CE mode B控制开关(SET ECOVRESTRIC CTRL) 
命令功能 
该命令用于设置MME是否支持无线覆盖增强功能和CE mode B控制功能。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ENHCOVCTRL|无线覆盖增强控制功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于设置MME是否支持无线覆盖增强限制功能。
CEMODEBCTRL|CE mode B控制功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于设置MME是否支持CE mode B限制功能。
命令举例 
设置不支持无线覆盖增强控制功能。 
SET ECOVRESTRIC CTRL:ENHCOVCTRL="NO"; 
父主题： [无线覆盖增强与CE mode B控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询无线覆盖增强与CE mode B控制开关(SHOW ECOVRESTRIC CTRL) 
### 查询无线覆盖增强与CE mode B控制开关(SHOW ECOVRESTRIC CTRL) 
命令功能 
该命令用于查询MME是否支持无线覆盖增强功能，是否支持CE mode B控制功能。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ENHCOVCTRL|无线覆盖增强控制功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于设置MME是否支持无线覆盖增强限制功能。
CEMODEBCTRL|CE mode B控制功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于设置MME是否支持CE mode B限制功能。
命令举例 
查询MME是否支持无线覆盖增强，是否支持CE mode B控制。 
SHOW ECOVRESTRIC CTRL; 
`
命令 (No.1): SHOW ECOVRESTRIC CTRL;
操作维护	无线覆盖增强控制功能	 CE mode B控制功能	
--------------------------------------------------
修改 	   不支持	             不支持	
--------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [无线覆盖增强与CE mode B控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 无线覆盖增强与CE mode B控制策略配置 
## 无线覆盖增强与CE mode B控制策略配置 
背景知识 
            
            无线覆盖增强限制是指UE在附着和TAU时，在消息中指示支持覆盖增强限制功能，MME根据HSS的签约和本地策略（根据PLMN配置），指示UE和eNB是否需要限制无线覆盖增强。
CE modeB是指在附着和TAU请求中，eNodeB通知MME UE支持CE mode B，MME根据UE's usage的类型以及本地的配置策略通知eNB 是否需要限制CE mode B方式。
        
功能描述 
            
            本配置用于配置某些或者全部PLMN的无线覆盖增强或CE ModeB控制策略的优先级别是使用HSS签约的限制策略还是使用本地配置限制策略，以及当优先级为本地配置时的限制策略。
        
相关主题 
 
设置默认无线覆盖增强与CE mode B控制策略(SET DEFAULT ECOVRESTRIC)
 
 
查询默认无线覆盖增强与CE mode B控制策略(SHOW DEFAULT ECOVRESTRIC)
 
 
新增无线覆盖增强与CE mode B控制策略(ADD PLMN ECOVRESTRIC)
 
 
修改无线覆盖增强与CE mode B控制策略(SET PLMN ECOVRESTRIC)
 
 
删除无线覆盖增强与CE mode B控制策略(DEL PLMN ECOVRESTRIC)
 
 
查询无线覆盖增强与CE mode B控制策略(SHOW PLMN ECOVRESTRIC)
 
 
父主题： [基于PLMN的无线覆盖增强与CE mode B控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置默认无线覆盖增强与CE mode B控制策略(SET DEFAULT ECOVRESTRIC) 
### 设置默认无线覆盖增强与CE mode B控制策略(SET DEFAULT ECOVRESTRIC) 
命令功能 
该命令用于设置默认无线覆盖增强与CE mode B控制策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ENHCOVPRIORITY|无线增强限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用户配置默认无线覆盖增强控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
ENHCOVLOCALPOLICY|无线增强限制本地控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地对于无线覆盖增强的控制策略。0：限制1：不限制
CEMODEBPRIORITY|CE mode B限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用户配置默认CE mode B控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
CEMODEBLOCALPOLICY|CE mode B限制本地控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地对于CE mode B的控制策略。0：限制1：不限制
命令举例 
设置默认无线增强限制策为HSS签约优先。 
SET DEFAULT ECOVRESTRIC:ENHCOVPRIORITY="HSSSUBSCRIPT"; 
父主题： [无线覆盖增强与CE mode B控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询默认无线覆盖增强与CE mode B控制策略(SHOW DEFAULT ECOVRESTRIC) 
### 查询默认无线覆盖增强与CE mode B控制策略(SHOW DEFAULT ECOVRESTRIC) 
命令功能 
该命令用于查询默认无线覆盖增强与CE mode B控制策略。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ENHCOVPRIORITY|无线增强限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用户配置默认无线覆盖增强控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
ENHCOVLOCALPOLICY|无线增强限制本地控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地对于无线覆盖增强的控制策略。0：限制1：不限制
CEMODEBPRIORITY|CE mode B限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用户配置默认CE mode B控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
CEMODEBLOCALPOLICY|CE mode B限制本地控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地对于CE mode B的控制策略。0：限制1：不限制
命令举例 
查询默认无线覆盖增强与CE mode B控制策略 
SHOW DEFAULT ECOVRESTRIC; 
`
命令 (No.1): SHOW DEFAULT ECOVRESTRIC;
操作维护     无线增强限制策略优先级     无线增强限制本地控制策略    CE mode B限制策略优先级       CE mode B限制本地控制策略 
---------------------------------------------------------------------------------------------------------------------------
修改         HSS签约优先                不限制                      HSS签约优先                   不限制 
---------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [无线覆盖增强与CE mode B控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增无线覆盖增强与CE mode B控制策略(ADD PLMN ECOVRESTRIC) 
### 新增无线覆盖增强与CE mode B控制策略(ADD PLMN ECOVRESTRIC) 
命令功能 
该命令用于新增无线覆盖增强与CE mode B控制策略。当需要增加一条新的无线覆盖增强与CE mode B控制策略时，通过本命令设置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|公共陆地移动(通信)网络。在某个国家或地区，某个运营商的某种制式的蜂窝移动通信网络被称为PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
ENHCOVPRIORITY|无线增强限制策略优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:HSSSUBSCRIPT。|该参数用户配置默认无线覆盖增强控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
ENHCOVLOCALPOLICY|无线增强限制本地控制策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置本地对于无线覆盖增强的控制策略。0：限制1：不限制
CEMODEBPRIORITY|CE mode B限制策略优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:HSSSUBSCRIPT。|该参数用户配置默认CE mode B控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
CEMODEBLOCALPOLICY|CE mode B限制本地控制策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置本地对于CE mode B的控制策略。0：限制1：不限制
命令举例 
新增一条无线覆盖增强与CE mode B控制策略，PLMN为"460"-"02"，无线增强限制策略为HHS签约优先，无线增强不限制本地控制，CE mode B限制策略优先级为HSS签约优先，CE mode B不限制本地控制 
ADD PLMN ECOVRESTRIC:PLMN="460"-"02",ENHCOVPRIORITY="HSSSUBSCRIPT",ENHCOVLOCALPOLICY="NO",CEMODEBPRIORITY="HSSSUBSCRIPT",CEMODEBLOCALPOLICY="NO"; 
父主题： [无线覆盖增强与CE mode B控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改无线覆盖增强与CE mode B控制策略(SET PLMN ECOVRESTRIC) 
### 修改无线覆盖增强与CE mode B控制策略(SET PLMN ECOVRESTRIC) 
命令功能 
该命令用于修改无线覆盖增强与CE mode B控制策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|公共陆地移动(通信)网络。在某个国家或地区，某个运营商的某种制式的蜂窝移动通信网络被称为PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
ENHCOVPRIORITY|无线增强限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用户配置默认无线覆盖增强控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
ENHCOVLOCALPOLICY|无线增强限制本地控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地对于无线覆盖增强的控制策略。0：限制1：不限制
CEMODEBPRIORITY|CE mode B限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用户配置默认CE mode B控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
CEMODEBLOCALPOLICY|CE mode B限制本地控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地对于CE mode B的控制策略。0：限制1：不限制
命令举例 
修改无线增强限制策略为本地配置优先。 
SET PLMN ECOVRESTRIC:PLMN="460"-"02",ENHCOVPRIORITY="LOCAL"; 
父主题： [无线覆盖增强与CE mode B控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除无线覆盖增强与CE mode B控制策略(DEL PLMN ECOVRESTRIC) 
### 删除无线覆盖增强与CE mode B控制策略(DEL PLMN ECOVRESTRIC) 
命令功能 
该命令用于删除无线覆盖增强与CE mode B控制策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|公共陆地移动(通信)网络。在某个国家或地区，某个运营商的某种制式的蜂窝移动通信网络被称为PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
命令举例 
删除PLMN为"460"-"02"的无线覆盖增强与CE mode B控制策略。 
DEL PLMN ECOVRESTRIC:PLMN="460"-"02"; 
父主题： [无线覆盖增强与CE mode B控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询无线覆盖增强与CE mode B控制策略(SHOW PLMN ECOVRESTRIC) 
### 查询无线覆盖增强与CE mode B控制策略(SHOW PLMN ECOVRESTRIC) 
命令功能 
该命令用于查询无线覆盖增强与CE mode B控制策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|公共陆地移动(通信)网络。在某个国家或地区，某个运营商的某种制式的蜂窝移动通信网络被称为PLMN。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|公共陆地移动(通信)网络。在某个国家或地区，某个运营商的某种制式的蜂窝移动通信网络被称为PLMN。
ENHCOVPRIORITY|无线增强限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用户配置默认无线覆盖增强控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
ENHCOVLOCALPOLICY|无线增强限制本地控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地对于无线覆盖增强的控制策略。0：限制1：不限制
CEMODEBPRIORITY|CE mode B限制策略优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用户配置默认CE mode B控制策略的优先级，包括HSS签约优先和本地配置优先两个选择。MME按照此配置使用相应的策略进行控制。0：HSS签约优先1：本地配置优先
CEMODEBLOCALPOLICY|CE mode B限制本地控制策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本地对于CE mode B的控制策略。0：限制1：不限制
命令举例 
查询无线覆盖增强与CE mode B控制策略 
SHOW PLMN ECOVRESTRIC; 
`
命令 (No.1): SHOW PLMN ECOVRESTRIC;
操作维护       PLMN        无线增强限制策略优先级    无线增强限制本地控制策略     CE mode B限制策略优先级      CE mode B限制本地控制策略 
------------------------------------------------------------------------------------------------------------------------------------------
复制 修改      460-01      本地配置优先              不限制                       本地配置优先                 不限制 
------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [无线覆盖增强与CE mode B控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 5GC互操作基本配置 
# 5GC互操作基本配置 
背景知识 
4G和5G互操作，指具有4G/5G能力的UE，在4G和5G间移动时（包括重新接入、重选、切换），能保证用户的会话连续性。 
根据MME和AMF间是否有N26接口，4G和5G互操作可分为： 
 
Interworking with N26：用户在4G和5G间移动时，在源系统和目标系统间可以交换移动性管理状态及会话管理状态。
 
 
Interworking without N26：用户在4G和5G间移动时，在源系统和目标系统间可以交换会话管理状态，但不交换移动性管理状态。
 
 
功能描述 
MME可以设置与5GC的互操作模式，选择AMF的策略等。 
相关主题 
 
设置5GC互操作基本配置(SET 5GC INTERWORKING)
 
 
查询5GC互操作基本配置(SHOW 5GC INTERWORKING)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置5GC互操作基本配置(SET 5GC INTERWORKING) 
## 设置5GC互操作基本配置(SET 5GC INTERWORKING) 
命令功能 
该命令用于设置5GC互操作基本配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MODE|互操作模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置互操作模式。
SUPWITHN26|支持N26互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持N26互操作。
SUPWITHOUTN26|支持无N26互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持无N26互操作。
SELECTCONVGCAMF|是否选择合一AMF|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否选择合一AMF&MME。
SUBEDIWK5GSINDPOLICY|签约的Interworking-5GS-Indicator处理策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置根据签约的Interworking-5GS-Indicator的决定是否允许与5GS互通的策略。0：根据签约值处理。如果Interworking-5GS-Indicator参数有值，按参数值决定。如果HSS没有携带该参数，则按Interworking-5GS-Indicator的值为NOT-SUBSCRIBED决定。1：无签约值时按允许处理。如果Interworking-5GS-Indicator参数有值，按参数值决定。如果HSS没有携带该参数，则按Interworking-5GS-Indicator的值为SUBSCRIBED决定。2：忽略签约值。无论HSS是否携带了Interworking-5GS-Indicator参数，都按Interworking-5GS-Indicator的值为SUBSCRIBED决定。
IFNTFAMF5GRESTRICT|MME是否基于签约限制信息通知AMF限制5GC接入|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否基于签约限制信息通知AMF限制5GC接入。0：否。收到AMF的Context Request消息，正常的给UE回成功响应消息。1：是。收到AMF的Context Request消息，检查签约的Core Network Type Restrictions和ARD信息，如果发现UE被限制接入5GC或当前RAT Type被限制接入，则给UE回失败响应消息，并指示失败原因值，AMF可以快速的拒绝用户注册。
PGWCSMFSELECTPOLICY|根据终端能力和签约信息选择融合的PGW-C+SMF策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME根据终端能力和签约信息选择融合的PGW-C+SMF的策略。0：终端能力和签约信息。如果UE Network Capability中的N1 mode值为1，并且MME根据终端的签约值和MME配置的本地策略，确定该终端使用的Core Network Type Restrictions不限制终端接入5GC网络，APN对应的Interworking-5GS-Indicator为允许终端与5GS Interworking，则MME选择融合的PGW-C+SMF。1：签约信息。如果MME根据终端的签约值和MME配置的本地策略，确定该终端使用的Core Network Type Restrictions不限制终端接入5GC网络，APN对应的Interworking-5GS-Indicator为允许终端与5GS Interworking，则MME选择融合的PGW-C+SMF。2：终端能力。如果UE Network Capability中的N1 mode值为1，则MME选择融合的PGW-C+SMF。3：终端能力或签约信息。如果UE Network Capability中的N1 mode值为1，或者根据签约值和本地策略，确定该用户使用的Core Network Type Restrictions不限制用户接入5GC以及APN对应的Interworking-5GS-Indicator为允许用户与5GS Interworking，则选择融合的PGW-C+SMF。4：不选择融合的PGW-C+SMF。对于终端能力或签约信息支持5G的用户，不选择融合的PGW-C+SMF。
PLYAFSELSMFFAIL|选择融合PGW-C+SMF失败后的策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME选择融合PGW-C+SMF失败后的处理策略。 0：不重选普通PGW。如果无融合PGW-C+SMF，则MME选择PGW失败；如果所有融合PGW-C+SMF均不可达，则MME从不可达的融合PGW-C+SMF中随机选择一个PGW。1：优选融合PGW-C+SMF。如果无融合PGW-C+SMF，则MME从普通PGW中选择PGW；如果所有融合PGW-C+SMF均不可达，则MME从不可达的融合PGW-C+SMF中随机选择一个PGW。2：优选普通PGW。如果无融合PGW-C+SMF，则MME从普通PGW中选择PGW；如果所有融合PGW-C+SMF均不可达，则MME从普通PGW中选择PGW。如果所有PGW（包括融合PGW-C+SMF和普通PGW）均不可达，则MME随机选择一个PGW。
IFSPRTAMFQUERY|是否支持AMF FQDN查询|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户从5G重接入到4G，MME需选择AMF，该参数用于设置查询AMF的方式,是否支持根据AMF FQDN查询AMF。0：否。直接按MME FQDN查询AMF。1：是。确定对端是AMF后，直接根据AMF instance FQDN解析AMF。
IFMMEQUERYAMFFAIL|AMF FQDN查询失败后是否再尝试MME FQDN查询|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置根据AMF FQDN查询AMF失败后是否再尝试根据MME FQDN查询AMF。0：否。直接认为AMF查询失败，不再根据MME FQDN查询AMF。1：是。确定对端是AMF，根据AMF instance FQDN解析AMF失败后，尝试根据MME FQDN查询AMF。
IFMMEENDCSON|MME是否支持EN-DC SON|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持EN-DC SON功能。0：否（No）。MME收到eNodeB或其他MME发送的消息时，如果消息中携带了EN-DC SON Configuration Transfer，则丢弃该消息。1：是（Yes）。MME收到eNodeB或其他MME发送的消息时，如果消息中携带了EN-DC SON Configuration Transfer，则透传该信息。
IFMMESPRT5GTRACE|MME是否支持5G Trace|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持5G相关接口的Trace功能。0：否（No）。MME给eNodeB发送消息携带Trace Activation信息时，即使签约信息或OMM本地设置了eNodeB的5G接口的Trace信息，也仅可携带first bit =S1-MME, second bit =X2, third bit =Uu，不会携带fourth bit =F1-C, fifth bit =E1。在N26接口中，MME不会处理Extended Trace Information信息。1：是（Yes）。MME给eNodeB发送消息携带Trace Activation信息时，如果签约信息或OMM本地设置了eNodeB的5G接口的Trace信息，则不仅可携带first bit =S1-MME, second bit =X2, third bit =Uu，也可携带fourth bit =F1-C, fifth bit =E1。在N26接口中，MME需处理Extended Trace Information信息。
IFMME5GFASTRETURN|MME是否支持5G的Return Preferred|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持5G的Return Preferred功能。0：否（No）。MME给eNodeB发送消息时，不会携带Last NG-RAN PLMN Identity信息给eNodeB。1：是（Yes）。MME在收到AMF的Return Preferred Indication后，给eNodeB发送切换限制列表信息时，携带Last NG-RAN PLMN Identity信息。
IFMME4GFASTRETURN|MME是否支持4G的Return Preferred|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持4G的Return Preferred功能。0：否（No）。MME给AMF发送Forward Relocation Request或Context Response消息时，不会携带Return Preferred Indication信息。1：是（Yes）。MME给AMF发送Forward Relocation Request或Context Response消息时，会携带Return Preferred Indication信息。
RSTRACCESSEPCONSCNR|MME是否基于核心网限制信息限制用户接入EPC|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否基于核心网限制信息限制用户接入EPC。0：否（No）。收到UE的Attach Request或TAU Request消息后，不判断最后使用的Core-Network-Restrictions中Access to EPC not allowed的值。1：是（Yes）。收到UE的Attach Request或TAU Request消息后，判断使用的Core-Network-Restrictions中Access to EPC not allowed的值，如果为“是”，则拒绝用户接入EPC。
REJCAUSE|限制用户接入EPC时拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME因为基于核心网限制信息限制用户接入EPC时，拒绝的原因值。
INDTUNNELINTSELOPT|MME是否支持非直传隧道接口选择优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当处于连接态下的用户从4G网络切换（Handover）到5G网络，或者从5G网络切换（Handover）到4G网络时，MME判断需要创建非直传隧道后，通过本参数控制是否在Create Indirect Tunnel Request请求消息中携带IDFUPF（Indirect Data Forwarding with UPF Indication）标记，后续SGW为非直传隧道选择网络接口时，需要参考该IDFUPF标记。0：否（No）1：是（Yes）
MMESUP5GCNRI|MME是否支持设置5GCNRI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制MME是否支持设置Create Session Request消息中的5GC NRI（ Network Resource Identifier，网络资源标识）和5GC NRS标记，5GC网络中的NRI是用来识别分配给移动终端的核心网络资源。包括以下选项，默认值为不支持。0：不支持。1：支持。当参数设置为"支持"时，MME根据终端用户的签约信息来设置Create Session Request消息中的5GC NRI和5GC NRS标记。
命令举例 
设置5GC互操作基本配置。 
SET 5GC INTERWORKING:MODE="WITHN26" 
父主题： [5GC互操作基本配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询5GC互操作基本配置(SHOW 5GC INTERWORKING) 
## 查询5GC互操作基本配置(SHOW 5GC INTERWORKING) 
命令功能 
该命令用于查询5GC互操作基本配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MODE|互操作模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置互操作模式。
SUPWITHN26|支持N26互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持N26互操作。
SUPWITHOUTN26|支持无N26互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持无N26互操作。
SELECTCONVGCAMF|是否选择合一AMF|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否选择合一AMF&MME。
SUBEDIWK5GSINDPOLICY|签约的Interworking-5GS-Indicator处理策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置根据签约的Interworking-5GS-Indicator的决定是否允许与5GS互通的策略。0：根据签约值处理。如果Interworking-5GS-Indicator参数有值，按参数值决定。如果HSS没有携带该参数，则按Interworking-5GS-Indicator的值为NOT-SUBSCRIBED决定。1：无签约值时按允许处理。如果Interworking-5GS-Indicator参数有值，按参数值决定。如果HSS没有携带该参数，则按Interworking-5GS-Indicator的值为SUBSCRIBED决定。2：忽略签约值。无论HSS是否携带了Interworking-5GS-Indicator参数，都按Interworking-5GS-Indicator的值为SUBSCRIBED决定。
IFNTFAMF5GRESTRICT|MME是否基于签约限制信息通知AMF限制5GC接入|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否基于签约限制信息通知AMF限制5GC接入。0：否。收到AMF的Context Request消息，正常的给UE回成功响应消息。1：是。收到AMF的Context Request消息，检查签约的Core Network Type Restrictions和ARD信息，如果发现UE被限制接入5GC或当前RAT Type被限制接入，则给UE回失败响应消息，并指示失败原因值，AMF可以快速的拒绝用户注册。
PGWCSMFSELECTPOLICY|根据终端能力和签约信息选择融合的PGW-C+SMF策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME根据终端能力和签约信息选择融合的PGW-C+SMF的策略。0：终端能力和签约信息。如果UE Network Capability中的N1 mode值为1，并且MME根据终端的签约值和MME配置的本地策略，确定该终端使用的Core Network Type Restrictions不限制终端接入5GC网络，APN对应的Interworking-5GS-Indicator为允许终端与5GS Interworking，则MME选择融合的PGW-C+SMF。1：签约信息。如果MME根据终端的签约值和MME配置的本地策略，确定该终端使用的Core Network Type Restrictions不限制终端接入5GC网络，APN对应的Interworking-5GS-Indicator为允许终端与5GS Interworking，则MME选择融合的PGW-C+SMF。2：终端能力。如果UE Network Capability中的N1 mode值为1，则MME选择融合的PGW-C+SMF。3：终端能力或签约信息。如果UE Network Capability中的N1 mode值为1，或者根据签约值和本地策略，确定该用户使用的Core Network Type Restrictions不限制用户接入5GC以及APN对应的Interworking-5GS-Indicator为允许用户与5GS Interworking，则选择融合的PGW-C+SMF。4：不选择融合的PGW-C+SMF。对于终端能力或签约信息支持5G的用户，不选择融合的PGW-C+SMF。
PLYAFSELSMFFAIL|选择融合PGW-C+SMF失败后的策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME选择融合PGW-C+SMF失败后的处理策略。 0：不重选普通PGW。如果无融合PGW-C+SMF，则MME选择PGW失败；如果所有融合PGW-C+SMF均不可达，则MME从不可达的融合PGW-C+SMF中随机选择一个PGW。1：优选融合PGW-C+SMF。如果无融合PGW-C+SMF，则MME从普通PGW中选择PGW；如果所有融合PGW-C+SMF均不可达，则MME从不可达的融合PGW-C+SMF中随机选择一个PGW。2：优选普通PGW。如果无融合PGW-C+SMF，则MME从普通PGW中选择PGW；如果所有融合PGW-C+SMF均不可达，则MME从普通PGW中选择PGW。如果所有PGW（包括融合PGW-C+SMF和普通PGW）均不可达，则MME随机选择一个PGW。
IFSPRTAMFQUERY|是否支持AMF FQDN查询|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户从5G重接入到4G，MME需选择AMF，该参数用于设置查询AMF的方式,是否支持根据AMF FQDN查询AMF。0：否。直接按MME FQDN查询AMF。1：是。确定对端是AMF后，直接根据AMF instance FQDN解析AMF。
IFMMEQUERYAMFFAIL|AMF FQDN查询失败后是否再尝试MME FQDN查询|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置根据AMF FQDN查询AMF失败后是否再尝试根据MME FQDN查询AMF。0：否。直接认为AMF查询失败，不再根据MME FQDN查询AMF。1：是。确定对端是AMF，根据AMF instance FQDN解析AMF失败后，尝试根据MME FQDN查询AMF。
IFMMEENDCSON|MME是否支持EN-DC SON|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持EN-DC SON功能。0：否（No）。MME收到eNodeB或其他MME发送的消息时，如果消息中携带了EN-DC SON Configuration Transfer，则丢弃该消息。1：是（Yes）。MME收到eNodeB或其他MME发送的消息时，如果消息中携带了EN-DC SON Configuration Transfer，则透传该信息。
IFMMESPRT5GTRACE|MME是否支持5G Trace|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持5G相关接口的Trace功能。0：否（No）。MME给eNodeB发送消息携带Trace Activation信息时，即使签约信息或OMM本地设置了eNodeB的5G接口的Trace信息，也仅可携带first bit =S1-MME, second bit =X2, third bit =Uu，不会携带fourth bit =F1-C, fifth bit =E1。在N26接口中，MME不会处理Extended Trace Information信息。1：是（Yes）。MME给eNodeB发送消息携带Trace Activation信息时，如果签约信息或OMM本地设置了eNodeB的5G接口的Trace信息，则不仅可携带first bit =S1-MME, second bit =X2, third bit =Uu，也可携带fourth bit =F1-C, fifth bit =E1。在N26接口中，MME需处理Extended Trace Information信息。
IFMME5GFASTRETURN|MME是否支持5G的Return Preferred|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持5G的Return Preferred功能。0：否（No）。MME给eNodeB发送消息时，不会携带Last NG-RAN PLMN Identity信息给eNodeB。1：是（Yes）。MME在收到AMF的Return Preferred Indication后，给eNodeB发送切换限制列表信息时，携带Last NG-RAN PLMN Identity信息。
IFMME4GFASTRETURN|MME是否支持4G的Return Preferred|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持4G的Return Preferred功能。0：否（No）。MME给AMF发送Forward Relocation Request或Context Response消息时，不会携带Return Preferred Indication信息。1：是（Yes）。MME给AMF发送Forward Relocation Request或Context Response消息时，会携带Return Preferred Indication信息。
RSTRACCESSEPCONSCNR|MME是否基于核心网限制信息限制用户接入EPC|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否基于核心网限制信息限制用户接入EPC。0：否（No）。收到UE的Attach Request或TAU Request消息后，不判断最后使用的Core-Network-Restrictions中Access to EPC not allowed的值。1：是（Yes）。收到UE的Attach Request或TAU Request消息后，判断使用的Core-Network-Restrictions中Access to EPC not allowed的值，如果为“是”，则拒绝用户接入EPC。
REJCAUSE|限制用户接入EPC时拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME因为基于核心网限制信息限制用户接入EPC时，拒绝的原因值。
INDTUNNELINTSELOPT|MME是否支持非直传隧道接口选择优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当处于连接态下的用户从4G网络切换（Handover）到5G网络，或者从5G网络切换（Handover）到4G网络时，MME判断需要创建非直传隧道后，通过本参数控制是否在Create Indirect Tunnel Request请求消息中携带IDFUPF（Indirect Data Forwarding with UPF Indication）标记，后续SGW为非直传隧道选择网络接口时，需要参考该IDFUPF标记。0：否（No）1：是（Yes）
MMESUP5GCNRI|MME是否支持设置5GCNRI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制MME是否支持设置Create Session Request消息中的5GC NRI（ Network Resource Identifier，网络资源标识）和5GC NRS标记，5GC网络中的NRI是用来识别分配给移动终端的核心网络资源。包括以下选项，默认值为不支持。0：不支持。1：支持。当参数设置为"支持"时，MME根据终端用户的签约信息来设置Create Session Request消息中的5GC NRI和5GC NRS标记。
命令举例 
查询5GC互操作基本配置。  
SHOW 5GC INTERWORKING 
`
(No.1) : SET 5GC INTERWORKING:PLYAFSELSMFFAIL="PGWSMF"
-----------------NFS_MMESGSN_0----------------
互操作模式 支持N26互操作   支持无N26互操作   是否选择合一AMF 签约的Interworking-5GS-Indicator处理策略 MME是否基于签约限制信息通知AMF限制5GC接入 根据终端能力和签约信息选择融合的PGW-C+SMF策略 选择融合PGW-C+SMF失败后的策略 是否支持AMF FQDN查询 AMF FQDN查询失败后是否再尝试MME FQDN查询 MME是否支持EN-DC SON MME是否支持5G Trace MME是否支持5G的Return Preferred MME是否支持4G的Return Preferred MME是否基于核心网限制信息限制用户接入EPC 限制用户接入EPC时拒绝原因值 MME是否支持非直传隧道接口选择优化 MME是否支持设置5GCNRI 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with N26   不支持N26互操作 不支持无N26互操作 是              根据签约值处理                           是                                        终端能力和签约信息                            优选融合PGW-C+SMF             否                   否                                       否                   否                  否                              否                              否                                       该跟踪区无合适小区          否                                否                    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-02 16:10:43 耗时: 0.192 秒
` 
父主题： [5GC互操作基本配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# EMS PLUS管理 
# EMS PLUS管理 
背景知识 
CHR，即Call History Record，是一种业务日志，用来分析业务执行状态，包括失败和成功的业务流程，以及一些关注的特定流程的记录。CHR可以用于故障定位，如用户投诉，KPI异常分析等；也可以用于运营商的精细化运维，如用户行为分析，网络业务运维分析等。 
EMSPlus，是面向用户的数据业务运营分析产品，立足于从用户的角度感知和分析网络信息和业务信息，通过对海量数据灵活地挖掘和分析，实现对业务流量、用户流量、日志查询、终端应用和用户回溯等全方位的可视化管理，构建可视、可管、可控的业务管道，为移动数据业务精细化运营提供全面支撑。 
MME/SGSN作为整个数据业务运营分析系统的一个组成部分，负责上报CHR记录给EMSPlus。 
功能描述 
EMS PLUS管理，用于配置MME/SGSN与EMSPlus之间的链路数据以及上报的业务日志类型，包括： 
 
EMS PLUS配置
 
 
EMS PLUS日志配置
 
 
相关主题 
 
EMS PLUS配置
 
 
EMS PLUS日志配置
 
 
EMS PLUS限速配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## EMS PLUS配置 
## EMS PLUS配置 
背景知识 
网元的通用日志分为3类，分别是业务日志，审计日志和运行日志。 
 
业务日志是指业务处理过程中产生的日志，如MME的失败日志。
 
 
审计日志是指操作和管理产生的日志，如OMM的操作日志。
 
 
运行日志记录系统运行状态事件及异常情况，如异常重启。
 
 
EMS+服务器为网元提供业务日志存储功能，业务统计功能，及日志查询功能。EMS+服务器和网元配套配置，为独立网元形态。 
功能描述 
该功能用于配置MME/SGSN与EMS+服务器之间连接的基础配置，包括EMS+服务器的地址，端口，以及链路检测参数等配置。 
相关主题 
 
设置EMS PLUS配置(SET EMSPLUS)
 
 
查询EMS PLUS配置(SHOW EMSPLUS)
 
 
父主题： [EMS PLUS管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置EMS PLUS配置(SET EMSPLUS) 
### 设置EMS PLUS配置(SET EMSPLUS) 
命令功能 
该命令用于配置MME/SGSN与EMS PLUS Server之间的基础配置，包括EMS+服务器的地址，端口，以及链路检测参数等配置。 
该命令的配置结果可以通过[SHOW EMSPLUS]命令进行查询。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SWITCH|是否开启EMS PLUS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示是否启用EMS PLUS服务器的功能。开：启用EMS PLUS服务器的功能。关：不启用EMS PLUS服务器的功能。
SVRIP|主用EMS PLUS服务端IP|参数可选性:任选参数；参数类型:地址|该参数用于设置EMS PLUS主用服务器的IP地址。
SVRPORT|主用EMS PLUS服务端端口号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置EMS PLUS主用服务器的端口号。
BAKSVRIP|备用EMS PLUS服务端IP|参数可选性:任选参数；参数类型:地址|该参数用于设置EMS PLUS备用服务器的IP地址。
BAKSVRPORT|备用EMS PLUS服务端端口号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置EMS PLUS备用服务器的端口号。
LOCALIP|MME/SGSN本端IP|参数可选性:任选参数；参数类型:地址|该参数用于设置MME/SGSN的本端IP地址。
VRFID|VRF ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|该参数用于设置VRFID。
CHECKINTERVAL|链路检测时间间隔(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~180。|该参数用于设置链路检测时间间隔(秒)，即每隔多长时间进行一次MME/SGSN与EMS PLUS服务器之间的链路检测。
CHECKNUM|链路检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置链路检测次数，连续检测失败的次数超过该参数配置的次数，则认为链路断开。
命令举例 
设置MME/SGSN开启EMS PLUS配置。 
SET EMSPLUS:SWITCH="ON" 
父主题： [EMS PLUS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询EMS PLUS配置(SHOW EMSPLUS) 
### 查询EMS PLUS配置(SHOW EMSPLUS) 
命令功能 
该命令用于查询MME/SGSN与EMS+服务器之间的基础配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SWITCH|是否开启EMS PLUS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示是否启用EMS PLUS服务器的功能。开：启用EMS PLUS服务器的功能。否：不启用EMS PLUS服务器的功能。
SVRIP|主用EMS PLUS服务端IP|参数可选性:任选参数；参数类型:地址|该参数用于设置EMS PLUS主用服务器的IP地址。
SVRPORT|主用EMS PLUS服务端端口号|参数可选性:任选参数；参数类型:整数。|该参数用于设置EMS PLUS主用服务器的端口号。
BAKSVRIP|备用EMS PLUS服务端IP|参数可选性:任选参数；参数类型:地址|该参数用于设置EMS PLUS备用服务器的IP地址。
BAKSVRPORT|备用EMS PLUS服务端端口号|参数可选性:任选参数；参数类型:整数。|该参数用于设置EMS PLUS备用服务器的端口号。
LOCALIP|MME/SGSN本端IP|参数可选性:任选参数；参数类型:地址|该参数用于设置MME/SGSN的本端IP地址。
VRFID|VRF ID|参数可选性:任选参数；参数类型:整数。|该参数用于设置VRFID。
CHECKINTERVAL|链路检测时间间隔(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置链路检测时间间隔(秒)，即每隔多长时间进行一次MME/SGSN与EMS PLUS服务器之间的链路检测。
CHECKNUM|链路检测次数|参数可选性:任选参数；参数类型:整数。|该参数用于设置链路检测次数，连续检测失败的次数超过该参数配置的次数，则认为链路断开。
命令举例 
查询EMS PLUS配置。 
SHOW EMSPLUS 
`
(No.1) : SHOW EMSPLUS:
-----------------NFS_MMESGSN_0----------------
操作维护       是否开启EMS PLUS功能 主用EMS PLUS服务端IP 主用EMS PLUS服务端端口号 备用PLUS服务端IP 备用EMS PLUS服务端端口号MME/SGSN本端IP VRF ID 链路检测时间间隔(秒) 链路检测次数 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           关闭                  0.0.0.0              0                        0.0.0.0          0                      0.0.0.0        0      5                     5              
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-08-11 16:41:56 耗时: 0.543 秒
` 
父主题： [EMS PLUS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## EMS PLUS日志配置 
## EMS PLUS日志配置 
背景知识 
在5GC网络中，支持使用EMS+作为独立的网管系统，为5GC网络中的各个网元提供业务日志功能、业务统计功能和日志查询功能。MME/SGSN需要支持与EMS+对接，向EMS+上报CHR，为EMS+的业务统计功能提供数据支撑。 
功能描述 
本功能用于控制MME/SGSN向EMS+是否上报日志，并且支持控制上报不同类型的日志。 
相关主题 
 
设置EMS PLUS日志配置(SET EMSPLUSLOG)
 
 
查询EMS PLUS日志配置(SHOW EMSPLUSLOG)
 
 
父主题： [EMS PLUS管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置EMS PLUS日志配置(SET EMSPLUSLOG) 
### 设置EMS PLUS日志配置(SET EMSPLUSLOG) 
命令功能 
该命令用于配置EMS PLUS上报日志的开关。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FUNCFLG|功能开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关：成功日志失败日志特殊日志
NETYPEFLG|网元类型开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|网元类型开关：NULLSGSNMME
LOGFUNCFLG|日志开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|日志功能开关：上报MM日志上报SM日志上报寻呼日志上报切换日志上报短信日志上报释放日志
SPECFAILLOGFLG|特殊日志开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|特殊失败日志开关：上报APN更正日志上报IMEI灰名单日志上报IMEI Unknown名单日志上报RIM成功日志上报RIM失败日志上报DNS查询成功日志上报DNS查询失败日志上报鉴权成功日志上报鉴权失败日志上报切换取消日志上报解码失败日志上报非替换类流程冲突且成功继续日志上报非替换类流程冲突且失败日志上报替换类流程冲突日志上报IMEI黑名单日志
INFOPOLICY|INFO字段携带策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置日志报文中INFO字段携带策略：正常携带：包含完整的INFO信息不携带：不携带INFO字段无调用链信息：携带INFO字段但内容不包含调用链信息默认正常携带。
ROAMLOGPLY|漫游用户日志上报策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置漫游用户日志上报策略：漫游用户上报正常日志：用于设置漫游用户是否上报正常日志。漫游用户上报特殊日志：用于设置漫游用户是否上报特殊日志。
命令举例 
设置EMS PLUS日志配置 
SET EMSPLUSLOG:FUNCFLG="SUCCESS"; 
父主题： [EMS PLUS日志配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询EMS PLUS日志配置(SHOW EMSPLUSLOG) 
### 查询EMS PLUS日志配置(SHOW EMSPLUSLOG) 
命令功能 
该命令用于查询EMS PLUS日志配置。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FUNCFLG|功能开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关：成功日志失败日志特殊日志
NETYPEFLG|网元类型开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|网元类型开关：NULLSGSNMME
LOGFUNCFLG|日志开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|日志功能开关：上报MM日志上报SM日志上报寻呼日志上报切换日志上报短信日志上报释放日志
SPECFAILLOGFLG|特殊日志开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|特殊失败日志开关：上报APN更正日志上报IMEI灰名单日志上报IMEI Unknown名单日志上报RIM成功日志上报RIM失败日志上报DNS查询成功日志上报DNS查询失败日志上报鉴权成功日志上报鉴权失败日志上报切换取消日志上报解码失败日志上报非替换类流程冲突且成功继续日志上报非替换类流程冲突且失败日志上报替换类流程冲突日志上报IMEI黑名单日志
INFOPOLICY|INFO字段携带策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置日志报文中INFO字段携带策略：正常携带：包含完整的INFO信息不携带：不携带INFO字段无调用链信息：携带INFO字段但内容不包含调用链信息默认正常携带。
ROAMLOGPLY|漫游用户日志上报策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置漫游用户日志上报策略：漫游用户上报正常日志：用于设置漫游用户是否上报正常日志。漫游用户上报特殊日志：用于设置漫游用户是否上报特殊日志。
命令举例 
查询EMS PLUS日志配置。 
SHOW EMSPLUSLOG; 
`
(No.1) : SHOW EMSPLUSLOG:
-----------------NFS_MMESGSN_0----------------
操作维护       功能开关 网元类型开关 日志开关                                              特殊日志开关 INFO字段携带策略 漫游用户日志上报策略                        
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           Null     Null         上报MM日志 & 上报SM日志 & 上报寻呼日志 & 上报切换日志 Null         正常携带         漫游用户上报正常日志 & 漫游用户上报特殊日志 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-05-17 20:43:18 耗时: 1.948秒
` 
父主题： [EMS PLUS日志配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## EMS PLUS限速配置 
## EMS PLUS限速配置 
背景知识 
CHR日志由用户流程触发，对CHR上报的速率进行限制，可以避免大量的CHR日志上报时占用系统过多的带宽/存储等资源，对系统造成异常影响。 
功能描述 
EMS PLUS限速配置用于对MME/SGSN的单SC中CHR上报的速率进行限制，包括如下配置： 
 
总上报速率：对单SC中所有CHR的上报速率进行限制。
 
 
失败CHR上报速率：对单SC中失败CHR的上报速率进行限制。
 
 
特殊CHR上报速率：对单SC中特殊CHR的上报速率进行限制。
 
 
相关主题 
 
设置EMS PLUS限速配置(SET EMSPLUS RATELIMIT)
 
 
查询EMS PLUS限速配置(SHOW EMSPLUS RATELIMIT)
 
 
父主题： [EMS PLUS管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置EMS PLUS限速配置(SET EMSPLUS RATELIMIT) 
### 设置EMS PLUS限速配置(SET EMSPLUS RATELIMIT) 
命令功能 
该命令用于设置EMS PLUS限速配置。当需要对MME/SGSN的单SC中CHR上报的速率进行限制时，使用该命令进行配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
TOTALRATE|总上报速率|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME/SGSN单SC中所有CHR的最大上报速率。默认值为2000（单位：事件数/每秒）。65535表示不限速。
FAILRATE|失败CHR上报速率|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME/SGSN单SC中失败CHR的最大上报速率。一般都在总上报速率的1/10以下。默认值为200（单位：事件数/每秒）。65535表示不限速。
SPECRATE|特殊CHR上报速率|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME/SGSN单SC中特殊CHR的最大上报速率。一般都在总上报速率的1/10以下。默认值为200（单位：事件数/每秒）。65535表示不限速。
命令举例 
设置EMS PLUS限速配置。 
SET EMSPLUS RATELIMIT:TOTALRATE=1000 
父主题： [EMS PLUS限速配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询EMS PLUS限速配置(SHOW EMSPLUS RATELIMIT) 
### 查询EMS PLUS限速配置(SHOW EMSPLUS RATELIMIT) 
命令功能 
该命令用于查询EMS PLUS限速配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TOTALRATE|总上报速率|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME/SGSN单SC中所有CHR的最大上报速率。默认值为2000（单位：事件数/每秒）。65535表示不限速。
FAILRATE|失败CHR上报速率|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME/SGSN单SC中失败CHR的最大上报速率。一般都在总上报速率的1/10以下。默认值为200（单位：事件数/每秒）。65535表示不限速。
SPECRATE|特殊CHR上报速率|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME/SGSN单SC中特殊CHR的最大上报速率。一般都在总上报速率的1/10以下。默认值为200（单位：事件数/每秒）。65535表示不限速。
命令举例 
查询EMS PLUS限速配置。。 
SHOW EMSPLUS RATELIMIT 
`
(No.1) : SHOW EMSPLUS RATELIMIT:
-----------------NFS_MMESGSN_0----------------
操作维护       总上报速率 失败CHR上报速率 特殊CHR上报速率 
----------------------------------------------------------
修改           1000       65535           65535           
----------------------------------------------------------
记录数：1
` 
父主题： [EMS PLUS限速配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 语音参数策略配置 
# 语音参数策略配置 
背景知识 
UE通过MME接入EPS网络后，如果需要进行语音呼叫，MME可通过两种方式来实现：IMS VoPS和CSFB。 
 
IMS VoPS能力用于指示UE是否可以进行IMS语音呼叫。
 
 
CSFB能力用于指示UE是否可以由EPS网络回落到目标GSM/UMTS电路域（CS）网络之后，再进行语音呼叫。
 
 
MME通知UE最终采用IMS VoPS或CSFB，还是IMS VoPS和CSFB都不支持，由UE能力和网络支持的语音能力共同确定，网络支持的语音能力由TA（无线能力）和IMSI（运营商策略）共同确定。 
 
UE能力：是指UE是否支持IMS VoPS或CSFB，MME根据UE在Attach/TAU请求中携带的“UE使用设置”和“E-UTRAN语音优先策略”，并结合“基于UE的语音参数策略配置”确定。
 
 
无线能力：是指无线侧是否支持IMS VoPS或CSFB。
 
 
运营商策略：是指用户归属的运营商（即PLMN）是否支持IMS VoPS或CSFB。
 
 
无线能力和运营商策略属于网络支持的语音能力，可以分开配置，也可以合一配置。 
 
当需要针对特定用户在特定区域采用特定的语音能力时，使用“基于IMSI和TA的语音参数策略配置”确定。
 
 
当无需针对特定运营商在特定区域采用特定的语音能力时，无线能力使用“基于TA的语音参数策略配置”确定，运营商策略使用“基于IMSI的语音参数策略配置”确定。
 
 
网络支持的语音能力，优先根据“基于IMSI和TA的语音参数策略配置”确定；若获取不到再根据“基于IMSI的语音参数策略配置”和“基于TA的语音参数策略配置”确定。 
如果UE能力、无线能力以及运营商策略三者有其一不支持IMS VoPS或CSFB，则MME通知UE不支持IMS VoPS或CSFB；如果这三者都支持IMS VoPS或CSFB，则MME通知UE支持IMS VoPS或CSFB。 
本功能目前仅适用于MME网元，SGSN暂不支持此功能。 
功能描述 
“语音参数策略配置”可以方便运营商灵活地根据UE能力、TA以及IMSI确定用户的语音能力，包括： 
 
基于UE的语音参数策略配置
 
 
基于TA的语音参数策略模板配置
 
 
基于IMSI的语音参数策略配置
 
 
基于IMSI和TA的语音参数策略配置
 
 
相关主题 
 
基于UE的语音参数策略配置
 
 
基于TA的语音参数策略模板配置
 
 
基于IMSI的语音参数策略配置
 
 
基于IMSI和TA的语音参数策略配置
 
 
基于IMEI的语音参数策略配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于UE的语音参数策略配置 
## 基于UE的语音参数策略配置 
背景知识 
UE通过MME接入EPS网络后，如果需要进行语音呼叫，MME可通过两种方式来实现：IMS VoPS和CSFB。 
 
IMS VoPS能力用于指示UE是否可以进行IMS语音呼叫。
 
 
CSFB能力用于指示UE是否可以由EPS网络回落到目标GSM/UMTS电路域（CS）网络之后，再进行语音呼叫。
 
 
MME通知UE最终采用IMS VoPS或CSFB，还是IMS VoPS和CSFB都不支持，由UE能力、无线能力以及运营商策略决定。 
 
UE能力：是指UE是否支持IMS VoPS或CSFB，MME根据UE在Attach/TAU请求中携带的“UE使用设置”和"E-UTRAN语音优先策略"，并结合“基于UE的语音参数策略配置”确定。
 
 
无线能力：是指无线侧是否支持IMS VoPS或CSFB，MME基于TA粒度确定无线侧是否支持，使用“基于TA的语音参数策略模板配置”确定。
 
 
运营商策略：是指用户归属的运营商（即PLMN）是否支持IMS VoPS或CSFB，使用“基于PLMN的语音参数策略配置”确定。
 
 
如果UE能力、无线能力以及运营商策略三者有其一不支持IMS VoPS或CSFB，则MME通知UE不支持IMS VoPS或CSFB；如果这三者都支持IMS VoPS或CSFB，则MME通知UE支持IMS VoPS或CSFB。 
本功能目前仅适用于MME网元，SGSN暂不支持此功能。 
功能描述 
“基于UE的语音参数策略配置”可以方便运营商灵活的根据不同UE的能力限制其语音能力。 
本功能在系统中的使用情况如下： 
                        在附着或者跟踪区更新流程中，UE在发给MME的Attach Request或TAU Request消息中携带UE能力，即消息中“Voice domain preference and UE's usage setting”字段（"UE's usage setting"对应
                        [ADD UE VOICE POLICY]
                        命令中配置的参数“UE使用设置”，"Voice domain preference"对应
                        [ADD UE VOICE POLICY]
                        命令中配置的参数"E-UTRAN语音优先策略"）。
                    
                        MME根据UE在Attach Request/TAU Request消息中携带的UE能力与通过
                        [ADD UE VOICE POLICY]
                        命令配置的参数“UE使用设置”及"E-UTRAN语音优先策略"进行匹配查找，如果MME找到对应配置记录，且UE所在的TA和UE归属的PLMN都支持IMS VoPS和CSFB，则在返回给UE的Attach/RAU Accept消息中携带对应配置记录的匹配数据：配置的参数“附加更新结果”（即为消息中需要携带的“CSFB能力”）和“IMS VoPS”（即为消息中需要携带的IMS VoPS能力）。
                    
                        如果MME没有通过
                        [ADD UE VOICE POLICY]
                        命令找到对应的配置记录，在返回给UE的Attach/RAU Accept消息中，携带系统默认配置的“附加更新结果”（即为消息中需要携带的“CSFB能力”）和“IMS VoPS”（即为消息中需要携带的IMS VoPS能力），系统默认配置的“附加更新结果”和“IMS VoPS”是通过
                        [SET DEFAULT VOICESET POLICY]
                        命令进行配置的，通常情况下，系统自动生成默认配置，无需操作人员执行。
                    
                如果运营商有没有特别的需要，则不需要通过
                [ADD UE VOICE POLICY]
                命令增加语音参数策略配置，只需要使用系统默认的语音参数策略配置即可，可通过
                [SHOW DEFAULT VOICESET POLICY]
                命令查询系统自动生成的默认记录。
            
应用此功能，有如下前提条件： 
 
                        在纯MME局（独立MME组网）或者Combo局（GnGp SGSN和MME网元合一组网）这两种情况下，需要通过
                        SET PACKET DOMAIN PARAMETER
                        命令，将参数“MME支持基于PS会话IMS语音”设置为“是”。
                    
 
 
                        通过
                        SHOW PLMN IMSVOPS NOSPRT
                        命令查询不支持IMS VoPS的PLMN，确认用户所属的PLMN不在查询结果中。
                    
 
 
相关主题 
 
设置缺省语音参数策略配置(SET DEFAULT VOICESET POLICY)
 
 
查询缺省语音参数策略配置(SHOW DEFAULT VOICESET POLICY)
 
 
新增基于UE的语音参数策略配置(ADD UE VOICE POLICY)
 
 
修改基于UE的语音参数策略配置(SET UE VOICE POLICY)
 
 
删除基于UE的语音参数策略配置(DEL UE VOICE POLICY)
 
 
查询基于UE的语音参数策略配置(SHOW UE VOICE POLICY)
 
 
父主题： [语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置缺省语音参数策略配置(SET DEFAULT VOICESET POLICY) 
### 设置缺省语音参数策略配置(SET DEFAULT VOICESET POLICY) 
命令功能 
该命令用于设置缺省语音参数策略配置。当系统没有配置其他语音参数策略，或者未找到符合该用户要求的语音参数策略配置时，使用缺省语音参数策略配置。 
注意事项 
该命令需要License支持CSFB或者SRVCC功能；或者开启IMS VoPS功能时有效，设置参数[SET PACKET DOMAIN PARAMETER#MMEIMSVOPS]为“Yes”。
参数说明 
标识|名称|类型|说明
---|---|---|---
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知向VLR更新位置区的附加更新结果。取值含义：NOADD：不携带附加更新结果。CSFBNOPRI：CSFB优先。SMSONLY：仅支持短信功能。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
设置缺省语音参数策略，其中无附加信息，不支持IMS VoPS。 
SET DEFAULT VOICESET POLICY:UPDATERESULT="NOADD",IMSVOPS="NOSPRT"; 
父主题： [基于UE的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询缺省语音参数策略配置(SHOW DEFAULT VOICESET POLICY) 
### 查询缺省语音参数策略配置(SHOW DEFAULT VOICESET POLICY) 
命令功能 
该命令用于显示缺省语音参数策略配置，包括附加信息更新结果、是否支持IMS语音业务。 
注意事项 
该命令需要License支持CSFB或者SRVCC功能；或者开启IMS VoPS功能时有效，设置参数[SET PACKET DOMAIN PARAMETER#MMEIMSVOPS]为“Yes”。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知向VLR更新位置区的附加更新结果。取值含义：NOADD：不携带附加更新结果。CSFBNOPRI：CSFB优先。SMSONLY：仅支持短信功能。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询缺省语音参数策略。 
SHOW DEFAULT VOICESET POLICY; 
`
命令 (No.1): SHOW DEFAULT VOICESET POLICY;
操作维护  附加更新结果        IMS VoPS   用户别名
-------------------------------------------------
修改      无附加信息          支持       
-------------------------------------------------
记录数 1
命令执行成功（耗时 0.062 秒）。
` 
父主题： [基于UE的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于UE的语音参数策略配置(ADD UE VOICE POLICY) 
### 新增基于UE的语音参数策略配置(ADD UE VOICE POLICY) 
命令功能 
该命令用于新增语音参数策略配置。当需要针对不同的语音中心或者数据中心的UE，以及当前E-UTRAN语音的优先策略时，可以配置不同的附加信息更新结果及IMS语音业务能力。 
注意事项 
 
该命令需要License支持CSFB或者SRVCC功能；或者开启IMS VoPS功能时有效，设置参数SET PACKET DOMAIN PARAMETER#MMEIMSVOPS为“Yes”。
 
 
基于不同的UE使用的配置以及E-UTRAN语音优先策略的组合可以配置不同的策略。每种组合只能配置一种，或者不配置。
 
 
如果UE使用的配置以及E-UTRAN语音优先策略的组合未配置，那么该组合实际使用策略使用缺省语音参数策略配置，参见命令SET DEFAULT VOICESET POLICY。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
USAGESET|UE使用设置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置，一般情况下移动电话以语音业务为中心，数据卡以数据业务为中心，网络可以根据UE的设置决定在特定环境下如何提供语音或者数据业务。取值含义：VOICE：以语音业务为中心。DATA：以数据业务为中心。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|E-UTRAN网络能够支持的语音业务类型，或者业务优先级别。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NOADD。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知向VLR更新位置区的附加更新结果。取值含义：NOADD：不携带附加更新结果。CSFBNOPRI：CSFB优先。SMSONLY：仅支持短信功能。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:SPRT。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
新增语音参数策略，其中UE使用语音中心，E-UTRAN语音优先策略为仅IMSVoPS语音，无附加信息的附加更新结果，支持IMS VoPS。 
ADD UE VOICE POLICY:USAGESET="VOICE",VOICEPREFER="IMSVoPSVOICE"; 
父主题： [基于UE的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于UE的语音参数策略配置(SET UE VOICE POLICY) 
### 修改基于UE的语音参数策略配置(SET UE VOICE POLICY) 
命令功能 
该命令用于修改语音参数策略配置。当需要针对不同的语音中心或者数据中心的UE，以及当前E-UTRAN语音的优先策略时，可以配置不同的附加信息更新结果及IMS语音业务能力。 
注意事项 
该命令需要License支持CSFB或者SRVCC功能；或者开启IMS VoPS功能时有效，设置参数[SET PACKET DOMAIN PARAMETER#MMEIMSVOPS]为“Yes”。
参数说明 
标识|名称|类型|说明
---|---|---|---
USAGESET|UE使用设置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置，一般情况下移动电话以语音业务为中心，数据卡以数据业务为中心，网络可以根据UE的设置决定在特定环境下如何提供语音或者数据业务。取值含义：VOICE：以语音业务为中心。DATA：以数据业务为中心。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|E-UTRAN网络能够支持的语音业务类型，或者业务优先级别。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知向VLR更新位置区的附加更新结果。取值含义：NOADD：不携带附加更新结果。CSFBNOPRI：CSFB优先。SMSONLY：仅支持短信功能。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
修改UE使用语音中心、E-UTRAN语音优先策略为仅IMSVoPS语音的语音参数策略，改为不支持IMS VoPS。 
SET UE VOICE POLICY:USAGESET="VOICE",VOICEPREFER="IMSVoPSVOICE"; 
父主题： [基于UE的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于UE的语音参数策略配置(DEL UE VOICE POLICY) 
### 删除基于UE的语音参数策略配置(DEL UE VOICE POLICY) 
命令功能 
该命令用于删除语音参数策略配置。 
删除后，如果UE使用设定以及E-UTRAN语音优先策略的组合无对应配置，那么使用策略使用缺省语音参数策略配置，参见命令[SET DEFAULT VOICESET POLICY]。
注意事项 
该命令需要License支持CSFB或者SRVCC功能；或者开启IMS VoPS功能时有效，设置参数[SET PACKET DOMAIN PARAMETER#MMEIMSVOPS]为“Yes”。
参数说明 
标识|名称|类型|说明
---|---|---|---
USAGESET|UE使用设置|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置，一般情况下移动电话以语音业务为中心，数据卡以数据业务为中心，网络可以根据UE的设置决定在特定环境下如何提供语音或者数据业务。取值含义：VOICE：以语音业务为中心。DATA：以数据业务为中心。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|E-UTRAN网络能够支持的语音业务类型，或者业务优先级别。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。
命令举例 
删除UE使用语音中心、E-UTRAN语音优先策略为仅IMS VoPS语音的语音参数策略。 
DEL UE VOICE POLICY:USAGESET="VOICE",VOICEPREFER="IMSVoPSVOICE"; 
父主题： [基于UE的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于UE的语音参数策略配置(SHOW UE VOICE POLICY) 
### 查询基于UE的语音参数策略配置(SHOW UE VOICE POLICY) 
命令功能 
该命令用于查询语音参数策略配置。包括UE使用设置、E-UTRAN的语音优先策略，以及相应的附加信息更新结果，是否支持IMS语音业务等信息。 
注意事项 
该命令需要License支持CSFB或者SRVCC功能；或者开启IMS VoPS功能时有效，设置参数[SET PACKET DOMAIN PARAMETER#MMEIMSVOPS]为“Yes”。
参数说明 
标识|名称|类型|说明
---|---|---|---
USAGESET|UE使用设置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置，一般情况下移动电话以语音业务为中心，数据卡以数据业务为中心，网络可以根据UE的设置决定在特定环境下如何提供语音或者数据业务。取值含义：VOICE：以语音业务为中心。DATA：以数据业务为中心。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|E-UTRAN网络能够支持的语音业务类型，或者业务优先级别。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
USAGESET|UE使用设置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|UE使用方式设置，一般情况下移动电话以语音业务为中心，数据卡以数据业务为中心，网络可以根据UE的设置决定在特定环境下如何提供语音或者数据业务。取值含义：VOICE：以语音业务为中心。DATA：以数据业务为中心。
VOICEPREFER|E-UTRAN语音优先策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|E-UTRAN网络能够支持的语音业务类型，或者业务优先级别。取值含义：CSVOICE：仅提供CS语音业务。IMSVoPSVOICE：仅提供IMS VoPS业务。CSVOICEPRI：CS语音业务作为首选，IMS VoPS业务作为第二选择。IMSVoPSVOICEPRI：IMS VoPS业务作为首选，CS语音业务作为第二选择。
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知向VLR更新位置区的附加更新结果。取值含义：NOADD：不携带附加更新结果。CSFBNOPRI：CSFB优先。SMSONLY：仅支持短信功能。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询已配置的语音参数策略。 
SHOW UE VOICE POLICY; 
`
命令 (No.1): SHOW UE VOICE POLICY;
操作维护         UE使用设置   E-UTRAN语音优先策略   附加更新结果        IMS VoPS   用户别名
-------------------------------------------------------------------------------------------
复制 修改 删除   语音中心     仅IMS VoPS语音        无附加信息          支持       
-------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [基于UE的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于TA的语音参数策略模板配置 
## 基于TA的语音参数策略模板配置 
背景知识 
UE通过MME接入EPS网络后，如果需要进行语音呼叫，MME可通过两种方式来实现：IMS VoPS和CSFB。 
 
IMS VoPS能力用于指示UE是否可以进行IMS语音呼叫。
 
 
CSFB能力用于指示UE是否可以由EPS网络回落到目标GSM/UMTS电路域（CS）网络之后，再进行语音呼叫。
 
 
MME通知UE最终采用IMS VoPS或CSFB，还是IMS VoPS和CSFB都不支持，由UE能力、无线能力以及运营商策略决定。 
 
UE能力：是指UE是否支持IMS VoPS或CSFB，MME根据UE在Attach/TAU请求中携带的“UE使用设置”和"E-UTRAN语音优先策略"，并结合“基于UE的语音参数策略配置”确定。
 
 
无线能力：是指无线侧是否支持IMS VoPS或CSFB，MME基于TA粒度确定无线侧是否支持，使用“基于TA的语音参数策略模板配置”确定。
 
 
运营商策略：是指用户归属的运营商（即PLMN）是否支持IMS VoPS或CSFB，使用“基于PLMN的语音参数策略配置”确定。
 
 
如果UE能力、无线能力以及运营商策略三者有其一不支持IMS VoPS或CSFB，则MME通知UE不支持IMS VoPS或CSFB；如果这三者都支持IMS VoPS或CSFB，则MME通知UE支持IMS VoPS或CSFB。 
本功能目前仅适用于MME网元，SGSN暂不支持此功能。 
功能描述 
“语音参数策略配置”可以方便运营商灵活的根据不同UE的能力限制其语音能力。 
本功能在系统中的使用情况如下： 
 
                        在附着或者跟踪区更新流程中，UE在发给MME的Attach Request或TAU Request消息中携带UE能力，即消息中“Voice domain preference and UE's usage setting”字段（"UE's usage setting"对应
                        ADD VOICESET POLICY
                        命令中配置的参数“UE使用设置”，"Voice domain preference"对应
                        ADD VOICESET POLICY
                        命令中配置的参数"E-UTRAN语音优先策略"）。
                    
 
 
                        MME根据UE在Attach Request/TAU Request消息中携带的UE能力与通过
                        ADD VOICESET POLICY
                        命令配置的参数“UE使用设置”及"E-UTRAN语音优先策略"进行匹配查找，如果MME找到对应配置记录，则在返回给UE的Attach/RAU Accept消息中携带对应配置记录的匹配数据：配置的参数“附加更新结果”（即为消息中需要携带的“CSFB能力”）和“IMS VoPS”（即为消息中需要携带的IMS VoPS能力）。
                    
 
 
                        如果MME没有通过
                        ADD VOICESET POLICY
                        命令找到对应的配置记录，在返回给UE的Attach/RAU Accept消息中，携带系统默认配置的“附加更新结果”（即为消息中需要携带的“CSFB能力”）和“IMS VoPS”（即为消息中需要携带的IMS VoPS能力），系统默认配置的“附加更新结果”和“IMS VoPS”是通过
                        SET DEFAULT VOICESET POLICY
                        命令进行配置的，通常情况下，系统自动生成默认配置，无需操作人员执行。
                    
 
 
                如果运营商有没有特别的需要，则不需要通过
                [ADD VOICESET POLICY]
                命令增加语音参数策略配置，只需要使用系统默认的语音参数策略配置即可，可通过
                [SHOW DEFAULT VOICESET POLICY]
                命令查询系统自动生成的默认记录。
            
应用此功能，有如下前提条件： 
 
                        在纯MME局（独立MME组网）或者Combo局（GnGp SGSN和MME网元合一组网）这两种情况下，需要通过
                        SET PACKET DOMAIN PARAMETER
                        命令，将参数“MME支持基于PS会话IMS语音”设置为“是”。
                    
 
 
                        通过
                        SHOW PLMN IMSVOPS NOSPRT
                        命令查询不支持IMS VoPS的PLMN，确认用户所属的PLMN不在查询结果中。
                    
 
 
相关主题 
 
设置缺省语音参数策略配置(SET DEFAULT TA VOICE POLICY)
 
 
查询缺省语音参数策略配置(SHOW DEFAULT TA VOICE POLICY)
 
 
新增基于TA的语音参数策略模板配置(ADD TA VOICESET POLICY TEMPLATE)
 
 
修改基于TA的语音参数策略模板配置(SET TA VOICESET POLICY TEMPLATE)
 
 
删除基于TA的语音参数策略模板配置(DEL TA VOICESET POLICY TEMPLATE)
 
 
查询基于TA的语音参数策略模板配置(SHOW TA VOICESET POLICY TEMPLATE)
 
 
父主题： [语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置缺省语音参数策略配置(SET DEFAULT TA VOICE POLICY) 
### 设置缺省语音参数策略配置(SET DEFAULT TA VOICE POLICY) 
命令功能 
该命令用于设置基于TA的缺省语音参数策略配置。当系统没有配置基于TA的语音参数策略时，使用该缺省语音参数策略配置。 
注意事项 
该命令需要License支持CSFB或者SRVCC功能；或者开启IMS VoPS功能时有效，设置参数[SET PACKET DOMAIN PARAMETER#MMEIMSVOPS]为“Yes”。
参数说明 
标识|名称|类型|说明
---|---|---|---
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附加更新结果。附加更新结果在Attach Accept消息及TAU Accept消息中携带给UE，把CSFB能力告知UE。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持IMS VoPS业务。IMS VoPS能力在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
设置缺省语音参数策略，其中无附加信息，不支持IMS VoPS。 
SET DEFAULT TA VOICE POLICY:UPDATERESULT="NOADD",IMSVOPS="NOSPRT"; 
父主题： [基于TA的语音参数策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询缺省语音参数策略配置(SHOW DEFAULT TA VOICE POLICY) 
### 查询缺省语音参数策略配置(SHOW DEFAULT TA VOICE POLICY) 
命令功能 
该命令用于显示基于TA的缺省语音参数策略配置，包括附加更新结果、是否支持IMS语音业务。 
注意事项 
该命令需要License支持CSFB或者SRVCC功能；或者开启IMS VoPS功能时有效，设置参数[SET PACKET DOMAIN PARAMETER#MMEIMSVOPS]为“Yes”。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附加更新结果。附加更新结果在Attach Accept消息及TAU Accept消息中携带给UE，把CSFB能力告知UE。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持IMS VoPS业务。IMS VoPS能力在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询缺省语音参数策略。 
SHOW DEFAULT TA VOICE POLICY; 
`
命令 (No.1): SHOW DEFAULT TA VOICE POLICY;
操作维护  附加更新结果        IMS VoPS   用户别名
-------------------------------------------------
修改      无附加信息          支持       
-------------------------------------------------
记录数 1
命令执行成功（耗时 0.062 秒）。
` 
父主题： [基于TA的语音参数策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于TA的语音参数策略模板配置(ADD TA VOICESET POLICY TEMPLATE) 
### 新增基于TA的语音参数策略模板配置(ADD TA VOICESET POLICY TEMPLATE) 
命令功能 
该命令用于新增语音参数策略模板配置。当需要针对不同的TA配置不同的语音参数策略时，进行语音参数策略模板的配置。配置后，还需要在跟踪区配置针对不同的TA配置语音参数策略模板标识。 
注意事项 
如果UE所在的跟踪区没有配置对应的语音参数策略模板标识，UE使用“全局语音参数策略配置”中设置的语音策略。 
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|策略模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数唯一标识一个语音参数策略模板。在命令ADD TA或者SET TA中被引用。
DFTUPTRSLT|附加更新结果|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NOADD。|该参数用于设置附加更新结果。附加更新结果在Attach Accept消息及TAU Accept消息中携带给UE，把CSFB能力告知UE。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
DFTIMSVOPS|IMS VoPS|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:SPRT。|该参数用于设置是否支持IMS VoPS业务。IMS VoPS能力在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|语音参数策略模板的别名，起备注作用。
命令举例 
新增语音参数策略模板配置，其中策略模板标识为1，缺省附加更新结果和缺省IMS VoPS都为缺省值，用户别名为alias。 
ADD TA VOICESET POLICY TEMPLATE:POLICYID=1,DFTUPTRSLT="SMSONLY",DFTIMSVOPS="SPRT",NAME="alias"; 
父主题： [基于TA的语音参数策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于TA的语音参数策略模板配置(SET TA VOICESET POLICY TEMPLATE) 
### 修改基于TA的语音参数策略模板配置(SET TA VOICESET POLICY TEMPLATE) 
命令功能 
该命令用于修改语音参数策略模板配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|策略模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数唯一标识一个语音参数策略模板。在命令ADD TA或者SET TA中被引用。
DFTUPTRSLT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附加更新结果。附加更新结果在Attach Accept消息及TAU Accept消息中携带给UE，把CSFB能力告知UE。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
DFTIMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持IMS VoPS业务。IMS VoPS能力在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|语音参数策略模板的别名，起备注作用。
命令举例 
修改语音参数策略模板配置，其中策略模板标识为1，缺省附加更新结果为仅SMS，缺省IMS VoPS为支持。 
SET TA VOICESET POLICY TEMPLATE:POLICYID=1,DFTUPTRSLT="SMSONLY",DFTIMSVOPS="SPRT"; 
父主题： [基于TA的语音参数策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于TA的语音参数策略模板配置(DEL TA VOICESET POLICY TEMPLATE) 
### 删除基于TA的语音参数策略模板配置(DEL TA VOICESET POLICY TEMPLATE) 
命令功能 
该命令用于删除语音参数策略模板配置。 
注意事项 
如果该策略模板标识已经被跟踪区配置关联使用，则不能删除。该策略模板标识是否被使用可通过命令[SHOW TA]查询。
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|策略模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数唯一标识一个语音参数策略模板。在命令ADD TA或者SET TA中被引用。
命令举例 
删除语音参数策略模板配置，其中策略模板标识为1。 
DEL TA VOICESET POLICY TEMPLATE:POLICYID=1; 
父主题： [基于TA的语音参数策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于TA的语音参数策略模板配置(SHOW TA VOICESET POLICY TEMPLATE) 
### 查询基于TA的语音参数策略模板配置(SHOW TA VOICESET POLICY TEMPLATE) 
命令功能 
该命令用于查询语音参数策略模板配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|策略模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数唯一标识一个语音参数策略模板。在命令ADD TA或者SET TA中被引用。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|策略模板标识|参数可选性:任选参数；参数类型:整数。|该参数唯一标识一个语音参数策略模板。在命令ADD TA或者SET TA中被引用。
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附加更新结果。附加更新结果在Attach Accept消息及TAU Accept消息中携带给UE，把CSFB能力告知UE。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持IMS VoPS业务。IMS VoPS能力在Attach Accept消息及TAU Accept消息中携带给UE，告知是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|语音参数策略模板的别名，起备注作用。
命令举例 
查询语音参数策略模板配置，策略模板标识为1。 
SHOW TA VOICESET POLICY TEMPLATE:POLICYID=1; 
`
2017-12-22 14:17:10 命令 (No.1): SHOW TA VOICESET POLICY TEMPLATE
操作维护         策略模板标识   附加更新结果        IMS VoPS   用户别名
-----------------------------------------------------------------------
复制 修改 删除   1              仅SMS               支持       alias
-----------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.042 秒）。
` 
父主题： [基于TA的语音参数策略模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于IMSI的语音参数策略配置 
## 基于IMSI的语音参数策略配置 
背景知识 
UE通过MME接入EPS网络后，如果需要进行语音呼叫，MME可通过两种方式来实现：IMS VoPS和CSFB。 
 
IMS VoPS能力用于指示UE是否可以进行IMS语音呼叫。
 
 
CSFB能力用于指示UE是否可以由EPS网络回落到目标GSM/UMTS电路域（CS）网络之后，再进行语音呼叫。
 
 
MME通知UE最终采用IMS VoPS或CSFB，还是IMS VoPS和CSFB都不支持，由UE能力、无线能力以及运营商策略决定。 
 
UE能力：是指UE是否支持IMS VoPS或CSFB，MME根据UE在Attach/TAU请求中携带的“UE使用设置”和"E-UTRAN语音优先策略"，并结合“基于UE的语音参数策略配置”确定。
 
 
无线能力：是指无线侧是否支持IMS VoPS或CSFB，MME基于TA粒度确定无线侧是否支持，使用“基于TA的语音参数策略模板配置”确定。
 
 
运营商策略：是指用户归属的运营商（即PLMN）是否支持IMS VoPS或CSFB，使用“基于PLMN的语音参数策略配置”确定。
 
 
如果UE能力、无线能力以及运营商策略三者有其一不支持IMS VoPS或CSFB，则MME通知UE不支持IMS VoPS或CSFB；如果这三者都支持IMS VoPS或CSFB，则MME通知UE支持IMS VoPS或CSFB。 
本功能目前仅适用于MME网元，SGSN暂不支持此功能。 
功能描述 
“基于PLMN的语音参数策略配置”可以方便运营商灵活的根据用户归属的PLMN确定其语音能力。 
                运营商如果不需要针对PLMN区分UE的语音能力，MME使用“基于PLMN的语音参数策略模板配置-缺省语音参数策略配置”中的配置。命令为：
                [SET DEFAULT PLMN VOICE POLICY]
                。
            
相关主题 
 
设置缺省语音参数策略配置(SET DEFAULT IMSI VOICE POLICY)
 
 
查询缺省语音参数策略配置(SHOW DEFAULT IMSI VOICE POLICY)
 
 
新增基于IMSI的语音参数策略配置(ADD IMSI VOICE POLICY)
 
 
修改基于IMSI的语音参数策略配置(SET IMSI VOICE POLICY)
 
 
删除基于IMSI的语音参数策略配置(DEL IMSI VOICE POLICY)
 
 
查询基于IMSI的语音参数策略配置(SHOW IMSI VOICE POLICY)
 
 
父主题： [语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置缺省语音参数策略配置(SET DEFAULT IMSI VOICE POLICY) 
### 设置缺省语音参数策略配置(SET DEFAULT IMSI VOICE POLICY) 
命令功能 
该命令用于设置基于IMSI的缺省语音参数策略配置。当系统没有配置基于IMSI的语音参数策略时，使用该缺省语音参数策略配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置MME默认附加更新结果。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数配置MME默认是否支持IMS VoPS业务。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
REFUSE|是否拒绝附着和PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否拒绝UE使用IMS APN发起附着或者PDN连接。
EMMCAUSE|EMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当拒绝UE使用IMS APN附着时的附着拒绝EMM原因值。
ESMCAUSE|ESM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当拒绝UE使用IMS APN附着或者PDN连接时的ESM拒绝原因值。
IMSAPNCHK|支持根据IMS APN签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据UE的IMS APN签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约IMS APN时，认为UE不具备IMS VoPS能力。
STNSRCHK|支持根据STN-SR签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据UE的STN-SR号码签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约STN-SR号码时，认为UE不具备IMS VoPS能力。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
设置缺省语音参数策略，其中无附加信息，不支持IMS VoPS。 
SET DEFAULT IMSI VOICE POLICY:UPDATERESULT="NOADD",IMSVOPS="NOSPRT"; 
父主题： [基于IMSI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询缺省语音参数策略配置(SHOW DEFAULT IMSI VOICE POLICY) 
### 查询缺省语音参数策略配置(SHOW DEFAULT IMSI VOICE POLICY) 
命令功能 
该命令用于显示基于IMSI的缺省语音参数策略配置，包括附加更新结果、是否支持IMS语音业务。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
UPDATERESULT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置MME默认附加更新结果。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数配置MME默认是否支持IMS VoPS业务。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
REFUSE|是否拒绝附着和PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否拒绝UE使用IMS APN发起附着或者PDN连接。
EMMCAUSE|EMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当拒绝UE使用IMS APN附着时的附着拒绝EMM原因值。
ESMCAUSE|ESM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当拒绝UE使用IMS APN附着或者PDN连接时的ESM拒绝原因值。
IMSAPNCHK|支持根据IMS APN签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据UE的IMS APN签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约IMS APN时，认为UE不具备IMS VoPS能力。
STNSRCHK|支持根据STN-SR签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据UE的STN-SR号码签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约STN-SR号码时，认为UE不具备IMS VoPS能力。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询缺省语音参数策略。 
SHOW DEFAULT IMSI VOICE POLICY; 
`
命令 (No.11): SHOW DEFAULT IMSI VOICE POLICY
操作维护  附加更新结果        IMS VoPS   用户别名
-------------------------------------------------
修改      无附加信息          不支持     abc
-------------------------------------------------
记录数 1
命令执行成功（耗时 0.029 秒）。
` 
父主题： [基于IMSI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于IMSI的语音参数策略配置(ADD IMSI VOICE POLICY) 
### 新增基于IMSI的语音参数策略配置(ADD IMSI VOICE POLICY) 
命令功能 
该命令用于新增基于IMSI的语音参数策略配置。当需要针对不同的IMSI段配置不同的语音参数策略时，使用该命令进行配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段
UPTRSLT|附加更新结果|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数是配置MME默认附加更新结果。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数配置MME默认是否支持IMS VoPS业务。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
REFUSE|是否拒绝附着和PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于配置是否拒绝UE使用IMS APN发起附着或者PDN连接。
EMMCAUSE|EMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:EF。|该参数用于配置当拒绝UE使用IMS APN附着时的附着拒绝EMM原因值。
ESMCAUSE|ESM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:ODB。|该参数用于配置当拒绝UE使用IMS APN附着或者PDN连接时的ESM拒绝原因值。
IMSAPNCHK|支持根据IMS APN签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于配置是否根据UE的IMS APN签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约IMS APN时，认为UE不具备IMS VoPS能力。
STNSRCHK|支持根据STN-SR签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于配置是否根据UE的STN-SR号码签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约STN-SR号码时，认为UE不具备IMS VoPS能力。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
新增基于IMSI的语音参数策略配置，其中IMSI为"46012"、附加更新结果为无附加信息、IMS VoPS为不支持。 
ADD IMSI VOICE POLICY:IMSI="46012",UPTRSLT="NOADD",IMSVOPS="NO"; 
父主题： [基于IMSI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于IMSI的语音参数策略配置(SET IMSI VOICE POLICY) 
### 修改基于IMSI的语音参数策略配置(SET IMSI VOICE POLICY) 
命令功能 
该命令用于修改基于IMSI的语音参数策略配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段
UPTRSLT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置MME默认附加更新结果。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数配置MME默认是否支持IMS VoPS业务。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
REFUSE|是否拒绝附着和PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否拒绝UE使用IMS APN发起附着或者PDN连接。
EMMCAUSE|EMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当拒绝UE使用IMS APN附着时的附着拒绝EMM原因值。
ESMCAUSE|ESM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当拒绝UE使用IMS APN附着或者PDN连接时的ESM拒绝原因值。
IMSAPNCHK|支持根据IMS APN签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据UE的IMS APN签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约IMS APN时，认为UE不具备IMS VoPS能力。
STNSRCHK|支持根据STN-SR签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据UE的STN-SR号码签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约STN-SR号码时，认为UE不具备IMS VoPS能力。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
修改IMSI为"46012"的语音参数策略配置，附加更新结果为无附加信息的配置数据，将IMS VoPS修改为支持。 
SET IMSI VOICE POLICY:IMSI="46012",UPTRSLT="NOADD",IMSVOPS="YES"; 
父主题： [基于IMSI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于IMSI的语音参数策略配置(DEL IMSI VOICE POLICY) 
### 删除基于IMSI的语音参数策略配置(DEL IMSI VOICE POLICY) 
命令功能 
该命令用于删除基于IMSI的语音参数策略模板配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段
命令举例 
删除IMSI为"46012"的配置数据。 
DEL IMSI VOICE POLICY:IMSI="46012"; 
父主题： [基于IMSI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于IMSI的语音参数策略配置(SHOW IMSI VOICE POLICY) 
### 查询基于IMSI的语音参数策略配置(SHOW IMSI VOICE POLICY) 
命令功能 
该命令用于查询基于IMSI的语音参数策略模板配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|IMSI号段
UPTRSLT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数是配置MME默认附加更新结果。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数配置MME默认是否支持IMS VoPS业务。当用户的IMSI未在“基于IMSI的语音参数策略”命令中配置时，才会使用本命令的该参数。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
REFUSE|是否拒绝附着和PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否拒绝UE使用IMS APN发起附着或者PDN连接。
EMMCAUSE|EMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当拒绝UE使用IMS APN附着时的附着拒绝EMM原因值。
ESMCAUSE|ESM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置当拒绝UE使用IMS APN附着或者PDN连接时的ESM拒绝原因值。
IMSAPNCHK|支持根据IMS APN签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据UE的IMS APN签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约IMS APN时，认为UE不具备IMS VoPS能力。
STNSRCHK|支持根据STN-SR签约决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据UE的STN-SR号码签约情况来决策其IMS VoPS能力。如果支持，则当UE没有签约STN-SR号码时，认为UE不具备IMS VoPS能力。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询所有基于IMSI的语音参数策略配置。 
SHOW IMSI VOICE POLICY 
`
命令 (No.9): SHOW IMSI VOICE POLICY
操作维护         IMSI   附加更新结果        IMS VoPS   用户别名
---------------------------------------------------------------
复制 修改 删除   11     仅SMS               支持       
---------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.023 秒）。
` 
父主题： [基于IMSI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于IMSI和TA的语音参数策略配置 
## 基于IMSI和TA的语音参数策略配置 
背景知识 
MME通知UE最终采用IMS VoPS或CSFB，还是IMS VoPS和CSFB都不支持，由UE能力和网络支持的语音能力共同确定，网络支持的语音能力由TA（无线能力）和IMSI（运营商策略）共同确定。 
 
无线能力：是指无线侧是否支持IMS VoPS或CSFB。
 
 
运营商策略：是指用户归属的运营商（即PLMN）是否支持IMS VoPS或CSFB。
 
 
当需要针对特定运营商在特定区域采用特定的语音能力时，使用“基于IMSI和TA的语音参数策略配置”确定网络支持的语音能力。 
本功能目前仅适用于MME网元，SGSN暂不支持此功能。 
功能描述 
“基于IMSI和TA的语音参数策略配置”可以方便运营商灵活的根据用户IMSI和TA确定其语音能力。 
相关主题 
 
新增基于IMSI和TA的语音参数策略配置(ADD IMSI TA VOICE POLICY)
 
 
修改基于IMSI和TA的语音参数策略配置(SET IMSI TA VOICE POLICY)
 
 
删除基于IMSI和TA的语音参数策略配置(DEL IMSI TA VOICE POLICY)
 
 
查询基于IMSI和TA的语音参数策略配置(SHOW IMSI TA VOICE POLICY)
 
 
父主题： [语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于IMSI和TA的语音参数策略配置(ADD IMSI TA VOICE POLICY) 
### 新增基于IMSI和TA的语音参数策略配置(ADD IMSI TA VOICE POLICY) 
命令功能 
该命令用于新增基于IMSI和TA的语音参数策略配置。当需要针对特定IMSI段+特定TA配置语音参数策略时，使用该命令进行配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
VOICEPLYAREAID|语音参数策略区域编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置语音参数策略区域编号。
UPTRSLT|附加更新结果|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附加更新结果。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
命令举例 
新增基于IMSI和TA的语音参数策略配置，其中IMSI为"46012"、语音参数策略区域编号为1和2、附加更新结果为无附加信息、IMS VoPS为不支持。 
ADD IMSI TA VOICE POLICY:IMSI="46012",VOICEPLYAREAID=1&2,UPTRSLT="NOADD",IMSVOPS="NO"; 
父主题： [基于IMSI和TA的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于IMSI和TA的语音参数策略配置(SET IMSI TA VOICE POLICY) 
### 修改基于IMSI和TA的语音参数策略配置(SET IMSI TA VOICE POLICY) 
命令功能 
该命令用于修改基于IMSI+TA的语音参数策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
VOICEPLYAREAID|语音参数策略区域编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置语音参数策略区域编号。
UPTRSLT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附加更新结果。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
命令举例 
修改IMSI为"46012"、语音参数策略区域编号为1和2的配置数据，附加更新结果为无附加信息的配置数据，将IMS VoPS修改为支持。 
SET IMSI TA VOICE POLICY:IMSI="46012",VOICEPLYAREAID=1&2,UPTRSLT="NOADD",IMSVOPS="YES"; 
父主题： [基于IMSI和TA的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于IMSI和TA的语音参数策略配置(DEL IMSI TA VOICE POLICY) 
### 删除基于IMSI和TA的语音参数策略配置(DEL IMSI TA VOICE POLICY) 
命令功能 
该命令用于删除基于IMSI+TA的语音参数策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
VOICEPLYAREAID|语音参数策略区域编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置语音参数策略区域编号。
命令举例 
删除IMSI为"46012"、语音参数策略区域编号为1和2的配置数据。 
DEL IMSI TA VOICE POLICY:IMSI="46012",VOICEPLYAREAID=1&2; 
父主题： [基于IMSI和TA的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于IMSI和TA的语音参数策略配置(SHOW IMSI TA VOICE POLICY) 
### 查询基于IMSI和TA的语音参数策略配置(SHOW IMSI TA VOICE POLICY) 
命令功能 
该命令用于查询基于IMSI+TA的语音参数策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
VOICEPLYAREAID|语音参数策略区域编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置语音参数策略区域编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于设置IMSI号段。
VOICEPLYAREAID|语音参数策略区域编号|参数可选性:任选参数；参数类型:整数。|该参数用于设置语音参数策略区域编号。
UPTRSLT|附加更新结果|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附加更新结果。取值含义：NOADD：不携带附加更新结果，表示MME支持CSFB。CSFBNOPRI：CSFB不优先，表示MME不支持CSFB。SMSONLY：仅支持短信功能，表示MME仅支持SGs口的短消息。
IMSVOPS|IMS VoPS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持IMS VoPS业务。取值含义：NOSPRT：不支持IMS VoPS业务。SPRT：支持IMS VoPS业务。
命令举例 
查询所有基于IMSI和TA的语音参数策略配置。 
SHOW IMSI TA VOICE POLICY 
`
命令 (No.1): SHOW IMSI TA VOICE POLICY;
操作维护         IMSI   语音参数策略区域编号   附加更新结果   IMS VoPS 
----------------------------------------------------------------------
复制 修改 删除   46012  1                      无附加信息     不支持 
复制 修改 删除   46012  2                      无附加信息     不支持 
----------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.127 秒）。
` 
父主题： [基于IMSI和TA的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于IMEI的语音参数策略配置 
## 基于IMEI的语音参数策略配置 
背景知识 
在LTE网络，本身只有分组交换（PS，Packet Switched）业务，没有电路交换（CS，Circuit Switched）业务，UE通过MME接入LTE网络后，如果需要进行语音呼叫，MME可通过两种方式来实现：IMS Based Voice/SRVCC（即VoLTE）和CSFB（Circuit Switched Fallback，电路域回落）。 
 
IMS VoPS能力用于指示UE是否可以进行IMS语音呼叫。
 
 
CSFB能力用于指示UE是否可以由EPS网络回落到目标GSM/UMTS电路域（CS）网络之后，再进行语音呼叫。
 
 
MME通知UE最终采用IMS VoPS或CSFB，还是IMS VoPS和CSFB都不支持，由UE能力、无线能力以及运营商策略决定。 
 
UE能力：是指UE是否支持IMS VoPS或CSFB，MME根据UE在Attach/TAU请求消息中携带的“UE使用设置”和"E-UTRAN语音优先策略"，并结合“基于UE的语音参数策略配置”确定。
 
 
无线能力：是指无线侧是否支持IMS VoPS或CSFB，MME基于TA粒度确定无线侧是否支持，使用“基于TA的语音参数策略模板配置”确定。
 
 
运营商策略：是指用户归属的运营商（即PLMN）是否支持IMS VoPS或CSFB，使用“基于PLMN的语音参数策略配置”确定。
 
 
无线能力和运营商策略属于网络支持的语音能力，可以分开配置，也可以合一配置。 
 
当需要针对特定用户在特定区域采用特定的语音能力时，使用“基于IMSI和TA的语音参数策略配置”确定。
 
 
当需要针对特定运营商在特定区域采用特定的语音能力时，无线能力使用“基于TA的语音参数策略配置”确定，运营商策略使用“基于IMSI的语音参数策略配置”和“基于IMEI的语音参数策略配置”确定。
 
 
网络支持的语音能力，优先根据“基于IMSI和TA的语音参数策略配置”确定；若获取不到再根据“基于IMSI的语音参数策略配置”、“基于IMEI的语音参数策略配置”和“基于TA的语音参数策略配置”确定。 
如果UE能力、无线能力以及运营商策略三者有其一不支持IMS VoPS或CSFB，则MME通知UE不支持IMS VoPS或CSFB；如果这三者都支持IMS VoPS或CSFB，则MME通知UE支持IMS VoPS或CSFB。 
本功能目前仅适用于MME网元，SGSN暂不支持此功能。 
功能描述 
本功能用于运营商灵活的根据终端用户的IMEI（International Mobile Equipment Identity，国际移动设备标识）中携带的SRVCC能力确定其语音能力。 
相关主题 
 
设置缺省语音参数策略配置(SET DEFAULT IMEI VOICE POLICY)
 
 
查询缺省语音参数策略配置(SHOW DEFAULT IMEI VOICE POLICY)
 
 
新增基于IMEI的语音参数策略配置(ADD IMEI VOICE POLICY)
 
 
修改基于IMEI的语音参数策略配置(SET IMEI VOICE POLICY)
 
 
删除基于IMEI的语音参数策略配置(DEL IMEI VOICE POLICY)
 
 
查询基于IMEI的语音参数策略配置(SHOW IMEI VOICE POLICY)
 
 
父主题： [语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置缺省语音参数策略配置(SET DEFAULT IMEI VOICE POLICY) 
### 设置缺省语音参数策略配置(SET DEFAULT IMEI VOICE POLICY) 
命令功能 
该命令用于设置基于IMEI的缺省语音参数策略配置。当系统没有配置基于IMEI的语音参数策略时，使用该缺省语音参数策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IFVOPSBASEDSRVCCCAPA|支持根据SRVCC能力决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制MME是否需要根据UE是否具备SRVCC能力来决策IMS VoPS（IMS Voice over PS session，基于PS会话的IMS语音）能力，并下发IMS VoPS能力给UE并且上报给HSS。该参数应用于开启VoLTE的场景。取值为0：MME决策UE的IMS VoPS能力时不会检查UE是否具备SRVCC能力。取值为1：MME决策UE的IMS VoPS能力时会检查UE的SRVCC能力，如果UE没有SRVCC能力，则确定UE不可使用IMS VoPS。如果UE有SRVCC能力，则下发IMS VoPS能力给UE并且上报给HSS。取值为2：MME决策UE的IMS VoPS能力时会检查UE的SRVCC能力：如果UE没有SRVCC能力，也没MS Network Capability，且为Voice center，则下发IMS VoPS能力给UE并且上报给HSS。如果UE没有SRVCC能力，但有MS Network Capability或为data center，则确定UE不可使用IMS VoPS。如果UE有SRVCC能力，则下发IMS VoPS能力给UE并且上报给HSS。
命令举例 
设置缺省语音参数策略，其中支持根据SRVCC能力决策IMS VoPS能力设置为根据SRVCC能力决策IMS VoPS能力。 
SET DEFAULT IMEI VOICE POLICY:IFVOPSBASEDSRVCCCAPA=BASE_ON_SRVCC; 
父主题： [基于IMEI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询缺省语音参数策略配置(SHOW DEFAULT IMEI VOICE POLICY) 
### 查询缺省语音参数策略配置(SHOW DEFAULT IMEI VOICE POLICY) 
命令功能 
该命令用于显示基于IMEI的缺省语音参数策略配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IFVOPSBASEDSRVCCCAPA|支持根据SRVCC能力决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制MME是否需要根据UE是否具备SRVCC能力来决策IMS VoPS（IMS Voice over PS session，基于PS会话的IMS语音）能力，并下发IMS VoPS能力给UE并且上报给HSS。该参数应用于开启VoLTE的场景。取值为0：MME决策UE的IMS VoPS能力时不会检查UE是否具备SRVCC能力。取值为1：MME决策UE的IMS VoPS能力时会检查UE的SRVCC能力，如果UE没有SRVCC能力，则确定UE不可使用IMS VoPS。如果UE有SRVCC能力，则下发IMS VoPS能力给UE并且上报给HSS。取值为2：MME决策UE的IMS VoPS能力时会检查UE的SRVCC能力：如果UE没有SRVCC能力，也没MS Network Capability，且为Voice center，则下发IMS VoPS能力给UE并且上报给HSS。如果UE没有SRVCC能力，但有MS Network Capability或为data center，则确定UE不可使用IMS VoPS。如果UE有SRVCC能力，则下发IMS VoPS能力给UE并且上报给HSS。
命令举例 
查询缺省语音参数策略配置。 
SHOW DEFAULT IMEI VOICE POLICY; 
`
命令 (No.1): SHOW DEFAULT IMEI VOICE POLICY;
操作维护  支持根据SRVCC能力决策IMS VoPS能力 
-------------------------------------------
修改      根据SRVCC能力决策IMS VoPS能力 
-------------------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [基于IMEI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于IMEI的语音参数策略配置(ADD IMEI VOICE POLICY) 
### 新增基于IMEI的语音参数策略配置(ADD IMEI VOICE POLICY) 
命令功能 
该命令用于新增基于IMEI的语音参数策略配置。当需要针对不同的IMEI段配置不同的语音参数策略时，使用该命令进行配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMEI号段。
IFVOPSBASEDSRVCCCAPA|支持根据SRVCC能力决策IMS VoPS能力|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于控制MME是否需要根据UE是否具备SRVCC能力来决策IMS VoPS（IMS Voice over PS session，基于PS会话的IMS语音）能力，并下发IMS VoPS能力给UE并且上报给HSS。该参数应用于开启VoLTE的场景。取值为0：MME决策UE的IMS VoPS能力时不会检查UE是否具备SRVCC能力。取值为1：MME决策UE的IMS VoPS能力时会检查UE的SRVCC能力，如果UE没有SRVCC能力，则确定UE不可使用IMS VoPS。如果UE有SRVCC能力，则下发IMS VoPS能力给UE并且上报给HSS。
命令举例 
新增基于IMEI的语音参数策略配置，其中IMEI为"864979040015257"、支持根据SRVCC能力决策IMS VoPS能力为根据SRVCC能力决策IMS VoPS能力。 
ADD IMEI VOICE POLICY:IMEI="864979040015257",IFVOPSBASEDSRVCCCAPA="BASE_ON_SRVCC"; 
父主题： [基于IMEI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于IMEI的语音参数策略配置(SET IMEI VOICE POLICY) 
### 修改基于IMEI的语音参数策略配置(SET IMEI VOICE POLICY) 
命令功能 
该命令用于修改基于IMEI的语音参数策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMEI号段。
IFVOPSBASEDSRVCCCAPA|支持根据SRVCC能力决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制MME是否需要根据UE是否具备SRVCC能力来决策IMS VoPS（IMS Voice over PS session，基于PS会话的IMS语音）能力，并下发IMS VoPS能力给UE并且上报给HSS。该参数应用于开启VoLTE的场景。取值为0：MME决策UE的IMS VoPS能力时不会检查UE是否具备SRVCC能力。取值为1：MME决策UE的IMS VoPS能力时会检查UE的SRVCC能力，如果UE没有SRVCC能力，则确定UE不可使用IMS VoPS。如果UE有SRVCC能力，则下发IMS VoPS能力给UE并且上报给HSS。
命令举例 
修改IMEI为"864979040015257"的语音参数策略配置，支持根据SRVCC能力决策IMS VoPS能力为不根据SRVCC能力决策IMS VoPS能力。 
SET IMEI VOICE POLICY:IMEI="864979040015257",IFVOPSBASEDSRVCCCAPA="NOT_BASE_ON_SRVCC"; 
父主题： [基于IMEI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于IMSI的语音参数策略配置(DEL IMEI VOICE POLICY) 
### 删除基于IMSI的语音参数策略配置(DEL IMEI VOICE POLICY) 
命令功能 
该命令用于删除基于IMEI的语音参数策略模板配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMEI号段。
命令举例 
删除IMEI为"864979040015257"的配置数据。 
DEL IMEI VOICE POLICY:IMEI="864979040015257"; 
父主题： [基于IMEI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于IMSI的语音参数策略配置(SHOW IMEI VOICE POLICY) 
### 查询基于IMSI的语音参数策略配置(SHOW IMEI VOICE POLICY) 
命令功能 
该命令用于查询基于IMEI的语音参数策略模板配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMEI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMEI|IMEI号段|参数可选性:任选参数；参数类型:字符型。|该参数用于设置IMEI号段。
IFVOPSBASEDSRVCCCAPA|支持根据SRVCC能力决策IMS VoPS能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制MME是否需要根据UE是否具备SRVCC能力来决策IMS VoPS（IMS Voice over PS session，基于PS会话的IMS语音）能力，并下发IMS VoPS能力给UE并且上报给HSS。该参数应用于开启VoLTE的场景。取值为0：MME决策UE的IMS VoPS能力时不会检查UE是否具备SRVCC能力。取值为1：MME决策UE的IMS VoPS能力时会检查UE的SRVCC能力，如果UE没有SRVCC能力，则确定UE不可使用IMS VoPS。如果UE有SRVCC能力，则下发IMS VoPS能力给UE并且上报给HSS。
命令举例 
查询基于IMEI的语音参数策略配置。 
SHOW IMEI VOICE POLICY 
`
命令 (No.1): SHOW IMEI VOICE POLICY;
操作维护           IMEI号段         支持根据SRVCC能力决策IMS VoPS能力 
--------------------------------------------------------------------
复制 修改 删除     864979040015257  不根据SRVCC能力决策IMS VoPS能力 
--------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.127 秒）。
` 
父主题： [基于IMEI的语音参数策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# PWS配置 
# PWS配置 
背景知识 
公众预警系统PWS（Public Warning System）是指在灾难或其他紧急情况下，系统生成预警信息，并通过各种通讯技术（广播、网络、电视等）进行通知，确保公众能够及时和准确接收灾难和其他紧急情况相关的预警、告警和危险信息。 
 
23G网络，BSC/RNC直接对接CBC，CBC直接下将预警信息下发给BSC/RNC。
 
 
4G LTE网络，MME对接CBC、CBC将预警信息下发给MME， MME将预警信息发送给eNodeB,eNodeB在小区中广播预警信息。
 
 
功能描述 
PWS配置包括以下内容： 
 
                        PWS控制策略配置：设置MME是否支持PWS功能以及是否支持Indication参数。命令参见：
                        SET PWS STRATEGY
                        。
                    
 
 
                        CBC局向配置：配置CBC局向以及关联的偶联ID。命令参见：
                        ADD CBC OFFICE
                        。
                    
 
 
相关主题 
 
PWS控制策略配置
 
 
CBC局向配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## PWS控制策略配置 
## PWS控制策略配置 
背景知识 
公众预警系统PWS（Public Warning System）是指在灾难或其他紧急情况下，系统生成预警信息，并通过各种通讯技术（广播、网络、电视等）进行通知，确保公众能够及时和准确接收灾难和其他紧急情况相关的预警、告警和危险信息。 
 
23G网络，BSC/RNC直接对接CBC，CBC直接下将预警信息下发给BSC/RNC。
 
 
4G LTE网络，MME对接CBC、CBC将预警信息下发给MME， MME将预警信息发送给eNodeB,eNodeB在小区中广播预警信息。
 
 
功能描述 
公众预警系统生成预警信息，并通过各种通讯技术（广播、网络、电视等），确保公众能够及时和准确接收灾难和其他紧急情况相关的预警、告警和危险信息。 
相关主题 
 
设置PWS控制策略配置(SET PWS STRATEGY)
 
 
查询PWS控制策略配置(SHOW PWS STRATEGY)
 
 
父主题： [PWS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置PWS控制策略配置(SET PWS STRATEGY) 
### 设置PWS控制策略配置(SET PWS STRATEGY) 
命令功能 
该命令用于配置和修改PWS控制策略。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
PWSFUNCFLAG|MME支持PWS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持PWS功能。当MMELicense支持PWS并且该参数配置为支持时，MME方支持PWS功能。
INDFLAG|MME支持Indication参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持Indication参数。当该参数配置为支持并且CBC在REQUEST携带此参数时，MME才会向CBC回复Indication信息。
PWSENBNUM|单次发送eNodeB数量|参数可选性:任选参数；参数类型:整数；参数范围为:1~500。|该参数用于设置100ms内MME发送PWS消息的eNodeB的数量。
命令举例 
修改PWS控制策略，MME不支持PWS功能，MME不支持Indication参数，单次发送eNodeB数量为23。 
SET PWS STRATEGY:PWSFUNCFLAG="NO",INDFLAG="NO",PWSENBNUM=23; 
父主题： [PWS控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询PWS控制策略配置(SHOW PWS STRATEGY) 
### 查询PWS控制策略配置(SHOW PWS STRATEGY) 
命令功能 
该命令用于查询PWS控制策略。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PWSFUNCFLAG|MME支持PWS功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持PWS功能。当MMELicense支持PWS并且该参数配置为支持时，MME方支持PWS功能。
INDFLAG|MME支持Indication参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持Indication参数。当该参数配置为支持并且CBC在REQUEST携带此参数时，MME才会向CBC回复Indication信息。
PWSENBNUM|单次发送eNodeB数量|参数可选性:任选参数；参数类型:整数。|该参数用于设置100ms内MME发送PWS消息的eNodeB的数量。
命令举例 
查询PWS控制策略。 
SHOW PWS STRATEGY; 
`
Command (No.6): SHOW PWS STRATEGY
维护  MME支持PWS功能 MME支持Indication参数 单次发送eNodeB数量 
--------------------------------------------------------------------------
修改  不支持         不支持                  200 
--------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [PWS控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## CBC局向配置 
## CBC局向配置 
背景知识 
            
            公众预警系统生成预警信息，并通过各种通讯技术（广播、网络、电视等），确保公众能够及时和准确接收灾难和其他紧急情况相关的预警、告警和危险信息。
        
功能描述 
            
            配置CBC局向以及CBC局向对应的SCTP偶联标识。
        
相关主题 
 
新增CBC局向配置(ADD CBC OFFICE)
 
 
修改CBC局向配置(SET CBC OFFICE)
 
 
删除CBC局向配置(DEL CBC OFFICE)
 
 
查询CBC局向配置(SHOW CBC OFFICE)
 
 
父主题： [PWS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增CBC局向配置(ADD CBC OFFICE) 
### 新增CBC局向配置(ADD CBC OFFICE) 
命令功能 
该命令用于增加CBC局向以及CBC局向对应的SCTP偶联标识。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
CBCID|CBC标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|CBC局向的标识，用于标识某个CBC。
SCTPID|SCTP连接标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4112。|SCTP连接标识，用于连接MME和CBC。标识可以通过命令SHOW SCTPIDCFG查询
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
新增CBC局信息，CBC标识为2，SCTP连接标识为21，用户别名为name21。 
ADD CBC OFFICE:CBCID="2",SCTPID="21",NAME="name21"; 
父主题： [CBC局向配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改CBC局向配置(SET CBC OFFICE) 
### 修改CBC局向配置(SET CBC OFFICE) 
命令功能 
该命令用于修改更新CBC局向对应的SCTP偶联标识。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
CBCID|CBC标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|CBC局向的标识，用于标识某个CBC。
SCTPID|SCTP连接标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4112。|SCTP连接标识，用于连接MME和CBC。标识可以通过命令SHOW SCTPIDCFG查询
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|记录该配置的注释信息，起备注作用。
命令举例 
修改CBC局信息，CBC标识为2，SCTP连接标识为21，用户别名为name21。 
SET CBC OFFICE:CBCID="2",SCTPID="21",NAME="name21"; 
父主题： [CBC局向配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除CBC局向配置(DEL CBC OFFICE) 
### 删除CBC局向配置(DEL CBC OFFICE) 
命令功能 
该命令用于删除MME配置的CBC局向信息。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
CBCID|CBC标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|CBC局向的标识，用于标识某个CBC。
命令举例 
删除CBC局信息，CBC标识为1。 
DEL CBC OFFICE:CBCID="1"; 
父主题： [CBC局向配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询CBC局向配置(SHOW CBC OFFICE) 
### 查询CBC局向配置(SHOW CBC OFFICE) 
命令功能 
该命令用于查询MME配置的CBC局向信息。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
CBCID|CBC标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|CBC局向的标识，用于标识某个CBC。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CBCID|CBC标识|参数可选性:任选参数；参数类型:整数。|CBC局向的标识，用于标识某个CBC。
SCTPID1|SCTP连接标识1|参数可选性:任选参数；参数类型:整数。|SCTP连接标识1，用于连接MME和CBC。
SCTPID2|SCTP连接标识2|参数可选性:任选参数；参数类型:整数。|SCTP连接标识2，用于连接MME和CBC。
SCTPID3|SCTP连接标识3|参数可选性:任选参数；参数类型:整数。|SCTP连接标识3，用于连接MME和CBC。
SCTPID4|SCTP连接标识4|参数可选性:必选参数；参数类型:整数。|SCTP连接标识4，用于连接MME和CBC。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|记录该配置的注释信息，起备注作用。
命令举例 
查询CBC局信息，CBC标识为2， 
SHOW CBC OFFICE:CBCID="2"; 
父主题： [CBC局向配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 语音中心用户限制配置 
# 语音中心用户限制配置 
背景知识 
功能描述 
本功能用于配置语音中心用户限制策略，包括是否支持语音中心用户限制，基于语音中心用户的语音偏好配置限制模板。 
相关主题 
 
语音中心用户限制策略配置
 
 
语音中心用户限制模板配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 语音中心用户限制策略配置 
## 语音中心用户限制策略配置 
背景知识 
功能描述 
本功能用于配置语音中心用户限制策略，比如是否启用语音中心用户限制。 
相关主题 
 
设置语音中心用户限制策略(SET VC USER RESTRICT POLICY)
 
 
查询语音中心用户限制策略(SHOW VC USER RESTRICT POLICY)
 
 
父主题： [语音中心用户限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置语音中心用户限制策略(SET VC USER RESTRICT POLICY) 
### 设置语音中心用户限制策略(SET VC USER RESTRICT POLICY) 
命令功能 
该命令用于修改语音中心用户限制策略。当运营商需要打开或者关闭语音中心用户按语音偏好设置限制策略时，使用该命令。 
注意事项 
最多可输入1024条记录。 
参数说明 
标识|名称|类型|说明
---|---|---|---
VCUSERLIMIT|启用语音中心用户限制功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制是否启用语音中心用户限制功能，启用后，语音中心用户可以按语音偏好设置限制策略。默认不启用。
命令举例 
将启用语音中心用户限制功能修改为"是"。 
SET VC USER RESTRICT POLICY:VCUSERLIMIT="YES"; 
父主题： [语音中心用户限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询语音中心用户限制策略(SHOW VC USER RESTRICT POLICY) 
### 查询语音中心用户限制策略(SHOW VC USER RESTRICT POLICY) 
命令功能 
该命令用于查询语音中心用户限制策略。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
VCUSERLIMIT|启用语音中心用户限制功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制是否启用语音中心用户限制功能，启用后，语音中心用户可以按语音偏好设置限制策略。默认不启用。
命令举例 
查询语音中心用户限制策略。 
SHOW VC USER RESTRICT POLICY; 
`
2021-12-28 14:53:28 命令 (No.1): SHOW VC USER RESTRICT POLICY
操作维护       启用语音中心用户限制功能 
----------------------------------------
修改           是                       
----------------------------------------
记录数：1
命令执行成功（耗时 1.235 秒）。
` 
父主题： [语音中心用户限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 语音中心用户限制模板配置 
## 语音中心用户限制模板配置 
背景知识 
功能描述 
本功能基于语音中心用户的语音域偏好，配置对应的限制策略，包括： 
 
仅CS语音时策略：是否放行普通用户、是否放行紧急用户、拒绝原因值。
 
 
仅IMS PS语音时策略：是否放行普通用户、是否放行紧急用户、拒绝原因值。
 
 
CS语音优先时策略：是否放行普通用户、是否放行紧急用户、拒绝原因值。
 
 
IMS PS语音优先时策略：是否放行普通用户、是否放行紧急用户、拒绝原因值。
 
 
相关主题 
 
新增语音中心用户限制模板(ADD VC USER RESTRICT POLICY PROFILE)
 
 
修改语音中心用户限制模板(SET VC USER RESTRICT POLICY PROFILE)
 
 
删除语音中心用户限制模板(DEL VC USER RESTRICT POLICY PROFILE)
 
 
查询语音中心用户限制模板(SHOW VC USER RESTRICT POLICY PROFILE)
 
 
父主题： [语音中心用户限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增语音中心用户限制模板(ADD VC USER RESTRICT POLICY PROFILE) 
### 新增语音中心用户限制模板(ADD VC USER RESTRICT POLICY PROFILE) 
命令功能 
该命令用于新增语音中心用户限制模板。当运营商需要按TA配置基于用户语音偏好限制语音中心用户时，需要增加该配置。 
当跟踪区关联了该限制模板后，语音中心用户在该跟踪区下接入时，根据限制模板中配置的用户语音偏好对应限制策略，决策用户放行或拒绝。 
注意事项 
 
传送配置表后，该命令方可生效。
 
 
最多可输入1024条记录。
 
 
ADD TA命令中的VCUSERLIMITPLYID和本配置中的POLICYID要一致。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|限制策略模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于设置语音中心用户限制策略模板标识，其他配置命令通过该标识关联对应的限制策略模板。
CSVOICEONLYPOLICY|仅CS语音限制用户策略|参数可选性:必选参数；参数类型:复合参数|该参数用于设置语音中心用户的语音偏好为仅CS语音时限制策略，包括是否放行仅CS语音普通用户、是否放行仅CS语音紧急用户以及拒绝原因值。
CSVONLYNORMAL|是否放行仅CS语音普通用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音偏好为仅CS语音的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为仅CS语音的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
CSVONLYEMC|是否放行仅CS语音紧急用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音中心且语音偏好为仅CS语音的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为仅CS语音的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
CSVONLYCAUSE|拒绝仅CS语音用户原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REJECTCAUSE_7。|该参数用于控制当拒绝语音中心且语音偏好为仅CS语音的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
IMSPSVOICEONLYPOLICY|仅IMS PS语音用户限制策略|参数可选性:必选参数；参数类型:复合参数|该参数用于设置语音中心用户的语音偏好为仅IMS PS语音时限制策略，包括是否放行仅IMS PS语音普通用户、是否放行仅IMS PS语音紧急用户以及拒绝原因值。
IMSPSVONLYNORMAL|是否放行仅IMS PS语音普通用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音偏好为仅IMS PS语音的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为仅IMS PS语音的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
IMSPSVONLYEMC|是否放行仅IMS PS语音紧急用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音中心且语音偏好为仅IMS PS语音的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为仅IMS PS语音的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
IMSPSVONLYCAUSE|拒绝仅IMS PS语音用户原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REJECTCAUSE_7。|该参数用于控制当拒绝语音中心且语音偏好为仅IMS PS语音的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
IMSPSVOICEVPREPOLICY|IMS PS语音优先用户限制策略|参数可选性:必选参数；参数类型:复合参数|该参数用于设置语音中心用户的语音偏好为IMS PS语音优先时限制策略，包括是否放行IMS PS语音优先普通用户、是否放行IMS PS语音优先紧急用户以及拒绝原因值。
IMSPSVPRENORMAL|是否放行IMS PS语音优先普通用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音偏好为IMS PS语音优先的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音中心，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
IMSPSVPREEMC|是否放行IMS PS语音优先紧急用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音中心且语音偏好为IMS PS语音优先的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为IMS PS语音优先的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
IMSPSVPRECAUSE|拒绝IMS PS语音优先用户原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REJECTCAUSE_7。|该参数用于控制当拒绝语音中心且语音偏好为IMS PS语音优先的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
CSVOICEVPREPOLICY|CS语音优先用户限制策略|参数可选性:必选参数；参数类型:复合参数|该参数用于设置语音中心用户语音偏好为CS语音优先时限制策略，包括是否放行CS语音优先普通用户、是否放行CS语音优先紧急用户以及拒绝原因值。
CSVPRENORMAL|是否放行CS语音优先普通用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音偏好为CS语音优先的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为CS语音优先的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
CSVPREEMC|是否放行CS语音优先紧急用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音中心且语音偏好为CS语音优先的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为CS语音优先的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
CSVPRECAUSE|拒绝CS语音优先用户原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REJECTCAUSE_7。|该参数用于控制当拒绝语音中心且语音偏好为CS语音优先的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
命令举例 
新增语音中心用户限制模板配置，限制策略模板标识为"1"，是否放行仅CS语音普通用户为"是"，是否放行仅CS语音紧急用户为"是"，拒绝仅CS语音用户原因值为"EPS服务不允许"，是否放行仅IMS PS语音普通用户为"是"，是否放行仅IMS PS语音紧急用户为"是"，拒绝仅IMS PS语音用户原因值为"EPS服务不允许"，是否放行IMS PS语音优先普通用户为"是"，是否放行IMS PS语音优先紧急用户为"是"，拒绝IMS PS语音优先用户原因值为"EPS服务不允许"，是否放行CS语音优先普通用户为"是"，是否放行CS语音优先紧急用户为"是"，拒绝CS语音优先用户原因值为"EPS服务不允许"。 
ADD VC USER RESTRICT POLICY PROFILE:POLICYID=1,CSVOICEONLYPOLICY="YES"-"YES"-"REJECTCAUSE_7",IMSPSVOICEONLYPOLICY="YES"-"YES"-"REJECTCAUSE_7",IMSPSVOICEVPREPOLICY="YES"-"YES"-"REJECTCAUSE_7",CSVOICEVPREPOLICY="YES"-"YES"-"REJECTCAUSE_7"; 
父主题： [语音中心用户限制模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改语音中心用户限制模板(SET VC USER RESTRICT POLICY PROFILE) 
### 修改语音中心用户限制模板(SET VC USER RESTRICT POLICY PROFILE) 
命令功能 
该命令用于修改指定语音中心用户限制模板配置。
注意事项 
该命令执行后传送配置表后方可生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|限制策略模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于设置语音中心用户限制策略模板标识，其他配置命令通过该标识关联对应的限制策略模板。
CSVOICEONLYPOLICY|仅CS语音限制用户策略|参数可选性:任选参数；参数类型:复合参数|该参数用于设置语音中心用户的语音偏好为仅CS语音时限制策略，包括是否放行仅CS语音普通用户、是否放行仅CS语音紧急用户以及拒绝原因值。
CSVONLYNORMAL|是否放行仅CS语音普通用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音偏好为仅CS语音的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为仅CS语音的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
CSVONLYEMC|是否放行仅CS语音紧急用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音中心且语音偏好为仅CS语音的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为仅CS语音的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
CSVONLYCAUSE|拒绝仅CS语音用户原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REJECTCAUSE_7。|该参数用于控制当拒绝语音中心且语音偏好为仅CS语音的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
IMSPSVOICEONLYPOLICY|仅IMS PS语音用户限制策略|参数可选性:任选参数；参数类型:复合参数|该参数用于设置语音中心用户的语音偏好为仅IMS PS语音时限制策略，包括是否放行仅IMS PS语音普通用户、是否放行仅IMS PS语音紧急用户以及拒绝原因值。
IMSPSVONLYNORMAL|是否放行仅IMS PS语音普通用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音偏好为仅IMS PS语音的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为仅IMS PS语音的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
IMSPSVONLYEMC|是否放行仅IMS PS语音紧急用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音中心且语音偏好为仅IMS PS语音的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为仅IMS PS语音的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
IMSPSVONLYCAUSE|拒绝仅IMS PS语音用户原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REJECTCAUSE_7。|该参数用于控制当拒绝语音中心且语音偏好为仅IMS PS语音的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
IMSPSVOICEVPREPOLICY|IMS PS语音优先用户限制策略|参数可选性:任选参数；参数类型:复合参数|该参数用于设置语音中心用户的语音偏好为IMS PS语音优先时限制策略，包括是否放行IMS PS语音优先普通用户、是否放行IMS PS语音优先紧急用户以及拒绝原因值。
IMSPSVPRENORMAL|是否放行IMS PS语音优先普通用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音偏好为IMS PS语音优先的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音中心，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
IMSPSVPREEMC|是否放行IMS PS语音优先紧急用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音中心且语音偏好为IMS PS语音优先的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为IMS PS语音优先的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
IMSPSVPRECAUSE|拒绝IMS PS语音优先用户原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REJECTCAUSE_7。|该参数用于控制当拒绝语音中心且语音偏好为IMS PS语音优先的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
CSVOICEVPREPOLICY|CS语音优先用户限制策略|参数可选性:任选参数；参数类型:复合参数|该参数用于设置语音中心用户语音偏好为CS语音优先时限制策略，包括是否放行CS语音优先普通用户、是否放行CS语音优先紧急用户以及拒绝原因值。
CSVPRENORMAL|是否放行CS语音优先普通用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音偏好为CS语音优先的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为CS语音优先的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
CSVPREEMC|是否放行CS语音优先紧急用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数用于控制对于语音中心且语音偏好为CS语音优先的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为CS语音优先的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
CSVPRECAUSE|拒绝CS语音优先用户原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:REJECTCAUSE_7。|该参数用于控制当拒绝语音中心且语音偏好为CS语音优先的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
命令举例 
修改语音中心用户限制模板配置，限制策略模板标识为"1"，是否放行仅CS语音普通用户为"是"，是否放行仅CS语音紧急用户为"是"，拒绝仅CS语音用户原因值为"EPS服务不允许"，是否放行仅IMS PS语音普通用户为"是"，是否放行仅IMS PS语音紧急用户为"是"，拒绝仅IMS PS语音用户原因值为"EPS服务不允许"，是否放行IMS PS语音优先普通用户为"是"，是否放行IMS PS语音优先紧急用户为"是"，拒绝IMS PS语音优先用户原因值为"EPS服务不允许"，是否放行CS语音优先普通用户为"是"，是否放行CS语音优先紧急用户为"是"，拒绝CS语音优先用户原因值为"EPS服务不允许"。 
SET VC USER RESTRICT POLICY PROFILE:POLICYID=1,CSVOICEONLYPOLICY="YES"-"YES"-"REJECTCAUSE_7",IMSPSVOICEONLYPOLICY="YES"-"YES"-"REJECTCAUSE_7",IMSPSVOICEVPREPOLICY="YES"-"YES"-"REJECTCAUSE_7",CSVOICEVPREPOLICY="YES"-"YES"-"REJECTCAUSE_7"; 
父主题： [语音中心用户限制模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除语音中心用户限制模板(DEL VC USER RESTRICT POLICY PROFILE) 
### 删除语音中心用户限制模板(DEL VC USER RESTRICT POLICY PROFILE) 
命令功能 
该命令用于删除指定语音中心用户限制模板。
注意事项 
该命令执行后传送配置表后方可生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|限制策略模板标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于设置语音中心用户限制策略模板标识，其他配置命令通过该标识关联对应的限制策略模板。
命令举例 
删除限制策略模板标识为"1"的语音中心用户限制模板配置。 
DEL VC USER RESTRICT POLICY PROFILE:POLICYID=1; 
父主题： [语音中心用户限制模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 本功能用于查询指定或者全部语音中心用户限制模板。(SHOW VC USER RESTRICT POLICY PROFILE) 
### 本功能用于查询指定或者全部语音中心用户限制模板。(SHOW VC USER RESTRICT POLICY PROFILE) 
命令功能 
该命令用于查询语音中心用户限制模板。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|限制策略模板标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|该参数用于设置语音中心用户限制策略模板标识，其他配置命令通过该标识关联对应的限制策略模板。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
POLICYID|限制策略模板标识|参数可选性:任选参数；参数类型:整数。|该参数用于设置语音中心用户限制策略模板标识，其他配置命令通过该标识关联对应的限制策略模板。
CSVONLYNORMAL|是否放行仅CS语音普通用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制对于语音偏好为仅CS语音的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为仅CS语音的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
CSVONLYEMC|是否放行仅CS语音紧急用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制对于语音中心且语音偏好为仅CS语音的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为仅CS语音的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
CSVONLYCAUSE|拒绝仅CS语音用户原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制当拒绝语音中心且语音偏好为仅CS语音的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
IMSPSVONLYNORMAL|是否放行仅IMS PS语音普通用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制对于语音偏好为仅IMS PS语音的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为仅IMS PS语音的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
IMSPSVONLYEMC|是否放行仅IMS PS语音紧急用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制对于语音中心且语音偏好为仅IMS PS语音的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为仅IMS PS语音的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
IMSPSVONLYCAUSE|拒绝仅IMS PS语音用户原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制当拒绝语音中心且语音偏好为仅IMS PS语音的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
IMSPSVPRENORMAL|是否放行IMS PS语音优先普通用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制对于语音偏好为IMS PS语音优先的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音中心，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
IMSPSVPREEMC|是否放行IMS PS语音优先紧急用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制对于语音中心且语音偏好为IMS PS语音优先的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为IMS PS语音优先的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
IMSPSVPRECAUSE|拒绝IMS PS语音优先用户原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制当拒绝语音中心且语音偏好为IMS PS语音优先的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
CSVPRENORMAL|是否放行CS语音优先普通用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制对于语音偏好为CS语音优先的语音中心非紧急用户是否放行，默认放行。当该参数打开后，对于语音偏好为CS语音优先的语音中心非紧急用户，触发的非紧急附着或者非紧急用户的TAU业务，直接拒绝。
CSVPREEMC|是否放行CS语音优先紧急用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制对于语音中心且语音偏好为CS语音优先的紧急用户是否放行，默认放行。当该参数打开后，对于语音中心且语音偏好为CS语音优先的紧急用户，触发的紧急附着或者紧急用户的TAU业务，直接拒绝。
CSVPRECAUSE|拒绝CS语音优先用户原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制当拒绝语音中心且语音偏好为CS语音优先的用户业务时，拒绝消息中携带的失败原因值，默认#7 (EPS services not allowed)。
命令举例 
查询限制策略模板标识为"1"的语音中心用户限制模板配置。 
SHOW VC USER RESTRICT POLICY PROFILE:POLICYID=1; 
`
2021-12-28 15:53:16 命令 (No.1): SHOW VC USER RESTRICT POLICY PROFILE:POLICYID=1
操作维护       限制策略模板标识 是否放行仅CS语音普通用户 是否放行仅CS语音紧急用户 拒绝仅CS语音用户原因值 是否放行仅IMS PS语音普通用户 是否放行仅IMS PS语音紧急用户 拒绝仅IMS PS语音用户原因值 是否放行IMS PS语音优先普通用户 是否放行IMS PS语音优先紧急用户 拒绝IMS PS语音优先用户原因值 是否放行CS语音优先普通用户 是否放行CS语音优先紧急用户 拒绝CS语音优先用户原因值 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1                是                       是                       EPS服务不允许          是                           是                           EPS服务不允许              是                             是                             EPS服务不允许                是                         是                         EPS服务不允许            
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
命令执行成功（耗时 2.177 秒）。
` 
父主题： [语音中心用户限制模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME事件监控配置 
# MME事件监控配置 
背景知识 
SCEF（Service Creation Environment Function，业务生成环境功能），是支持业务生成进程的功能集，其输出包括业务逻辑程序和业务数据，SCEF支持用户状态信息能力开放，SCEF通过HSS向MME/SGSN订阅UE状态信息，为某些特定物联网应用提供所需的用户状态信息，包括UE连接丢失、UE可达、UE位置、UE IMSI-IMEI(SV)关联改变、UE通信故障和DDN失败后UE可用等信息。 
T6a接口是MME（Mobility Management Entity）与SCEF之间的接口。T6a是3GPP定义的一个标准接口，主要用于MME通过SCEF向第三方应用开放NB-IoT（Narrow Band Internet of Things）终端的状态，比如UE连接丢失、UE可达、UE位置信息、UE通信失败、DDN（Digital Data Network）失败后可用等。 
UE的状态信息需要MME采集并上报。MME事件监控用于实现这些状态信息的监控及上报。监控的事件主要有： 
 
终端失去连接。
 
 
终端可及。
 
 
终端位置报告。
 
 
通讯失败。
 
 
DDN下行数据通知失败后可达。
 
 
功能描述 
本功能用于配置MME中的事件监控策略，包括MME是否支持或终止事件监控。 
 
MME支持事件监控功能后，MME会对HSS订阅的事件进行监控并及时上报给SCEF。
 
 
MME解除监控功能后，在HSS取消订阅事件后，MME终止监控。
 
 
相关主题 
 
MME事件监控策略配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MME事件监控策略配置 
## MME事件监控策略配置 
背景知识 
SCEF支持用户状态信息能力开放，通过HSS向MME/SGSN订阅UE状态信息，为某些特定物联网应用提供所需的用户状态信息，包括UE连接丢失、UE可达、UE位置、UE
IMSI-IMEI(SV)关联改变、UE通信故障和DDN失败后UE可用等信息。 
UE状态信息需要MME采集并上报。MME事件监控用于实现这些状态信息的监控及上报。监控的事件主要有： 
 
终端失去连接
 
 
终端可及
 
 
终端位置报告
 
 
通讯失败
 
 
DDN下行数据通知失败后可达
 
 
功能描述 
本功能用于配置MME中的事件监控策略，包括MME是否支持或终止事件监控。 
 
是否支持事件监控。设置为支持后，MME会对HSS订阅的事件进行监控并及时上报给SCEF。
 
 
是否支持解除监控事件。设置为支持后，在HSS取消订阅事件后，终止监控。
 
 
相关主题 
 
设置事件监控策略(SET MMEEVMONIPOLY)
 
 
查询事件监控策略(SHOW MMEEVMONIPOLY)
 
 
父主题： [MME事件监控配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置事件监控策略(SET MMEEVMONIPOLY) 
### 设置事件监控策略(SET MMEEVMONIPOLY) 
命令功能 
该命令用于设置MME是否支持事件监控及解除事件监控。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPMONIEV|MME是否支持事件监控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持监控事件。1，表示MME支持监控事件。0，表示MME不支持监控事件。
MMESUPDELMONIEV|MME是否支持删除监控事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持删除监控事件，即终止监控事件。1，表示MME支持终止监控事件。0，表示MME不支持终止监控事件。
命令举例 
设置MME监控事件策略，MME支持监控事件。 
SET MMEEVMONIPOLY:MMESUPMONIEV=1; 
父主题： [MME事件监控策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询事件监控策略(SHOW MMEEVMONIPOLY) 
### 查询事件监控策略(SHOW MMEEVMONIPOLY) 
命令功能 
该命令用于查询MME是否支持事件监控及解除事件监控。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPMONIEV|MME是否支持事件监控|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持监控事件。1，表示MME支持监控事件。0，表示MME不支持监控事件。
MMESUPDELMONIEV|MME是否支持删除监控事件|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持删除监控事件，即终止监控事件。1，表示MME支持终止监控事件。0，表示MME不支持终止监控事件。
命令举例 
查询MME事件监控策略。 
SHOW MMEEVMONIPOLY; 
`
命令 (No.1): SHOW MMEEVMONIPOLY;
操作维护                       MME支持监控事件             MME支持删除监控事件
---------------------------------------------------------------------------------------
复制 修改 删除                     支持                         不支持
---------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [MME事件监控策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 无线连接异常释放策略配置 
# 无线连接异常释放策略配置 
背景知识 
无线连接异常释放原因包括： 
 
Null
 
 
Radio Connection With UE Lost
 
 
User Inactivity
 
 
CS Fallback Triggered
 
 
Inter-RAT Redirection
 
 
UE Not Available for PS Service
 
 
Redirection towards 1xRTT
 
 
功能描述 
            
            通过设置无线连接异常释放原因和是否支持携带ARRL指示，来配置无线连接异常释放策略。
        
相关主题 
 
设置无线连接异常释放策略配置(SET RADIO LINK RELEASE POLICY)
 
 
查询无线连接异常释放策略配置(SHOW RADIO LINK RELEASE POLICY)
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 设置无线连接异常释放策略配置(SET RADIO LINK RELEASE POLICY) 
## 设置无线连接异常释放策略配置(SET RADIO LINK RELEASE POLICY) 
命令功能 
该命令用于设置无线连接异常释放策略配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ANLRADIORLSCAUSE|无线连接异常释放原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置表示无线连接异常释放的原因值，包括：NullRadio Connection With UE LostUser InactivityCS Fallback TriggeredInter-RAT RedirectionUE Not Available for PS ServiceRedirection towards 1xRTT
SUPCARRYARRL|支持携带ARRL指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持在Release Access Bearer Request消息中携带ARRL指示。
命令举例 
设置无线连接异常释放策略配，无线连接异常释放原因为RADIO，支持携带ARRL指示为不支持 
SET RADIO LINK RELEASE POLICY:ANLRADIORLSCAUSE="RADIO",SUPCARRYARRL="NOSUPPORT" 
父主题： [无线连接异常释放策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询无线连接异常释放策略配置(SHOW RADIO LINK RELEASE POLICY) 
## 查询无线连接异常释放策略配置(SHOW RADIO LINK RELEASE POLICY) 
命令功能 
该命令用于查询无线连接异常释放策略配置。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ANLRADIORLSCAUSE|无线连接异常释放原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置表示无线连接异常释放的原因值，包括：NullRadio Connection With UE LostUser InactivityCS Fallback TriggeredInter-RAT RedirectionUE Not Available for PS ServiceRedirection towards 1xRTT
SUPCARRYARRL|支持携带ARRL指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持在Release Access Bearer Request消息中携带ARRL指示。
命令举例 
查询无线连接异常释放策略配置。 
SHOW RADIO LINK RELEASE POLICY 
`
命令 (No.31): SHOW RADIO LINK RELEASE POLICY
-----------------NFS_MMESGSN_0----------------
无线连接异常释放原因    支持携带ARRL指示
Null                  不支持
记录数：1
执行成功（耗时 0.027 秒）。
` 
父主题： [无线连接异常释放策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# Gb口Rerouting配置 
# Gb口Rerouting配置 
背景知识 
网络共享时，对于不支持网络共享的UE，如果该UE选择了不合适的PLMN，会导致BSC（Base Station Controller）选择不合适的Initial SGSN，因此需Intial SGSN重定向用户到其他合适的SGSN。 
功能描述 
Gb口Rerouting策略配置包括Gb口Rerouting策略配置和IMSI号段Gb口Rerouting配置。 
相关主题 
 
Gb口Rerouting策略配置
 
 
IMSI号段Gb口Rerouting策略配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## Gb口Rerouting策略配置 
## Gb口Rerouting策略配置 
背景知识 
网络共享时，对于不支持网络共享的UE，如果该UE选择了不合适的PLMN，会导致BSC（Base Station Controller）选择不合适的Initial SGSN，因此需Intial SGSN重定向用户到其他合适的SGSN。 
功能描述 
Gb口Rerouting策略配置主要用于设置功能开关，包括以下功能： 
 
是否支持Gb口Rerouting策略。
 
 
是否支持根据IMSI号段控制Gb口Rerouting策略。
 
 
相关主题 
 
设置Gb口Rerouting策略配置(SET GB INTERFACE REROUTING POLICY)
 
 
查询Gb口Rerouting策略配置(SHOW GB INTERFACE REROUTING POLICY)
 
 
父主题： [Gb口Rerouting配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置Gb口Rerouting策略配置(SET GB INTERFACE REROUTING POLICY) 
### 设置Gb口Rerouting策略配置(SET GB INTERFACE REROUTING POLICY) 
命令功能 
该命令用于配置Gb口Rerouting策略。当SGSN需要支持Gb口Rerouting功能时，使用该命令。 
注意事项 
None.
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPGBROUTING|支持Gb口Rerouting|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持Gb口Rerouting功能。不支持：SGSN不支持Gb口Rerouting功能。支持：SGSN支持Gb口Rerouting功能。
SUPIMSIGBREROUTING|支持根据IMSI号段控制Gb口Rerouting|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持根据IMSI号段控制Gb口Rerouting。不支持：不支持根据IMSI号段控制Gb口Rerouting。支持：支持根据IMSI号段控制Gb口Rerouting。
REJECTCAUSE|拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置NAS层拒绝原因值。SGSN向BSC（Base Station Controller）发送Rerouting消息时，会携带重定向指示字段，该字段需要设置NAS层拒绝原因值。
命令举例 
设置Gb口Rerouting策略配置，支持Gb口Rerouting，不支持根据IMSI号段控制Gb口Rerouting，拒绝原因值设置为13。 
SET GB INTERFACE REROUTING POLICY:SUPGBROUTING=YES,SUPIMSIGBREROUTING=NO,REJECTCAUSE=REJECTCAUSE_13; 
父主题： [Gb口Rerouting策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询Gb口Rerouting策略配置(SHOW GB INTERFACE REROUTING POLICY) 
### 查询Gb口Rerouting策略配置(SHOW GB INTERFACE REROUTING POLICY) 
命令功能 
该命令用于查询Gb口Rerouting策略配置。 
注意事项 
None.
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPGBROUTING|支持Gb口Rerouting|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持Gb口Rerouting功能。不支持：SGSN不支持Gb口Rerouting功能。支持：SGSN支持Gb口Rerouting功能。
SUPIMSIGBREROUTING|支持根据IMSI号段控制Gb口Rerouting|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持根据IMSI号段控制Gb口Rerouting。不支持：不支持根据IMSI号段控制Gb口Rerouting。支持：支持根据IMSI号段控制Gb口Rerouting。
REJECTCAUSE|拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置NAS层拒绝原因值。SGSN向BSC（Base Station Controller）发送Rerouting消息时，会携带重定向指示字段，该字段需要设置NAS层拒绝原因值。
命令举例 
查询Gb口Rerouting策略配置 
SHOW GB INTERFACE REROUTING POLICY 
`
命令 (No.1): SHOW GB INTERFACE REROUTING POLICY;
操作维护          支持Gb口Rerouting      支持根据IMSI号段控制Gb口Rerouting                  拒绝原因值   
------------------------------------------------------------------------------------------------------------------------
复制 修改 删除         支持                          不支持                    roaming not allowed in this location area 
------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [Gb口Rerouting策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## IMSI号段Gb口Rerouting策略配置 
## IMSI号段Gb口Rerouting策略配置 
背景知识 
网络共享时，对于不支持网络共享的UE，如果该UE选择了不合适的PLMN，会导致BSC（Base Station Controller）选择不合适的Initial SGSN，因此需Intial SGSN重定向用户到其他合适的SGSN。 
功能描述 
当“支持根据IMSI号段控制Gb口Rerouting策略”功能设置为开启时，在配置的IMSI号段内的用户，可以进行Gb口Rerouting，即Initial SGSN可以把该用户重定向到其他SGSN。 
相关主题 
 
新增IMSI号段Gb口Rerouting策略(ADD IMSI GB INTERFACE REROUTING POLICY)
 
 
删除IMSI号段Gb口Rerouting策略(DEL IMSI GB INTERFACE REROUTING POLICY)
 
 
查询IMSI号段Gb口Rerouting策略(SHOW IMSI GB INTERFACE REROUTING POLICY)
 
 
父主题： [Gb口Rerouting配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增IMSI号段Gb口Rerouting策略(ADD IMSI GB INTERFACE REROUTING POLICY) 
### 新增IMSI号段Gb口Rerouting策略(ADD IMSI GB INTERFACE REROUTING POLICY) 
命令功能 
该命令用于新增IMSI号段Gb口Rerouting策略。当需要根据IMSI号段设置Gb口Rerouting时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置IMSI号段，在此号段内的用户，可以进行Gb口Rerouting，即SGSN可以把该用户重定向到其他SGSN。
命令举例 
新增IMSI号段Gb口Rerouting策略，其中IMSI为3547845195。 
ADD IMSI GB INTERFACE REROUTING POLICY:IMSI=3547845195; 
父主题： [IMSI号段Gb口Rerouting策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除IMSI号段Gb口Rerouting策略(DEL IMSI GB INTERFACE REROUTING POLICY) 
### 删除IMSI号段Gb口Rerouting策略(DEL IMSI GB INTERFACE REROUTING POLICY) 
命令功能 
该命令用于删除IMSI号段Gb口Rerouting策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于配置IMSI号段，在此号段内的用户，可以进行Gb口Rerouting，即SGSN可以把该用户重定向到其他SGSN。
命令举例 
删除IMSI为3547845195的Gb口Rerouting策略。 
DEL IMSI GB INTERFACE REROUTING POLICY:IMSI=3547845195; 
父主题： [IMSI号段Gb口Rerouting策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询IMSI号段Gb口Rerouting策略(SHOW IMSI GB INTERFACE REROUTING POLICY) 
### 查询IMSI号段Gb口Rerouting策略(SHOW IMSI GB INTERFACE REROUTING POLICY) 
命令功能 
该命令用于查询IMSI号段Gb口Rerouting策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于配置IMSI号段，在此号段内的用户，可以进行Gb口Rerouting，即SGSN可以把该用户重定向到其他SGSN。
命令举例 
查询IMSI号段Gb口Rerouting策略 
SHOW IMSI GB INTERFACE REROUTING POLICY; 
`
命令 (No.1): SHOW IMSI GB INTERFACE REROUTING POLICY;
操作维护                        IMSI
--------------------------------------------
复制 修改 删除               3547845195
--------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [IMSI号段Gb口Rerouting策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME消息参数配置 
# MME消息参数配置 
背景知识 
按照3GPP协议，核心网和终端之间的NAS消息按照协议标准进行设置， 核心网可以根据网络运行要求，对NAS消息中的参数进行控制。同时MME可以对其他接口（S6a、SGS、S11等接口）消息进行控制。 
功能描述 
为实现MME对网元各接口消息参数的灵活控制，在此节点下配置对应接口的消息参数控制策略。 
相关主题 
 
NAS消息参数配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## NAS消息参数配置 
## NAS消息参数配置 
背景知识 
按照3GPP协议，核心网和终端之间的NAS消息按照协议标准进行设置， 核心网可以根据网络运行要求，对NAS消息中的参数进行控制。 
功能描述 
为实现MME对NAS消息参数的灵活控制，在此节点下配置NAS消息参数的控制策略。 
相关主题 
 
T3402定时器策略配置
 
 
父主题： [MME消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### T3402定时器策略配置 
### T3402定时器策略配置 
背景知识 
T3402定时器用于控制UE Attach/TAU重试的时长，增加T3402的值会减少附着请求次数和TAU请求次数、提高附着成功率以及TAU的成功率。 
据3GPP规范24.008的10.5.7.3章节中定义的取值规则如下： 
 
当范围为2sec~60sec，间隔为2sec。
 
 
当范围为1min~31min，间隔为1min。
 
 
当范围为36min-186min，间隔为6min。
 
 
默认值：12min
 
 
网络侧MME在ATTACH ACCEPT、ATTACH REJECT 、TRACKING AREA UPDATE ACCEPT消息中将T3402定时器时长携带给UE。 
当核心网拥塞或容灾倒换时，为控制UE在T3402超时后集中附着对核心网造成冲击的影响，核心网对用户的T3402定时器时长进行离散设置，保障网络稳定运行。 
功能描述 
该功能用于提供对T3402定时器时长的策略控制，包括： 
 
附着拒绝消息中是否携带T3402时长
 
 
是否支持离散分配T3402时长
 
 
T3402时长最小值
 
 
T3402时长最大值
 
 
相关主题 
 
设置T3402定时器策略配置(SET T3402 POLICY CFG)
 
 
查询T3402定时器策略配置(SHOW T3402 POLICY CFG)
 
 
父主题： [NAS消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置T3402定时器策略配置(SET T3402 POLICY CFG) 
#### 设置T3402定时器策略配置(SET T3402 POLICY CFG) 
命令功能 
该命令用于设置T3402定时器时长的策略。当UE附着失败场景下，MME根据设置的策略控制UE重新发起附着请求的时间间隔。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
T3402INATTREJ|附着拒绝消息中是否携带T3402时长|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附着拒绝消息中是否携带T3402时长。
SUPPT3402RAND|是否支持离散分配T3402时长|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在attach accept、attach reject、TAU accept消息中携带T3404定时器时，是否支持离散分配T3402时长。该参数设置为“否”：不支持离散配置，T3402时长根据SHOW MOBILE MANAGEMENT命令的“UE附着/跟踪区更新重发定时器T3402时长 ”参数进行设置。该参数设置为“是”：必须设置“T3402时长最小值”和“T3402时长最大值”。
T3402MIN|T3402时长最小值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:2~11160。|该参数用于当T3402时长进行离散分配时，设置T3402时长范围的最小值 。
T3402MAX|T3402时长最大值 （秒）|参数可选性:任选参数；参数类型:整数；参数范围为:2~11160。|该参数用于当T3402时长进行离散分配时，设置T3402时长范围的最大值。
命令举例 
设置T3402定时器策略配置。附着拒绝消息中是否携带T3402时长设置是，是否支持离散分配T3402时长 T3402时长最小值（秒）设置是，T3402时长最小值（秒）设置400，T3402时长最大值 （秒）设置730。 
SET T3402 POLICY CFG:T3402INATTREJ="YES",SUPPT3402RAND="YES",T3402MIN=400,T3402MAX=730; 
父主题： [T3402定时器策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询T3402定时器策略配置(SHOW T3402 POLICY CFG) 
#### 查询T3402定时器策略配置(SHOW T3402 POLICY CFG) 
命令功能 
该命令用于查询T3402定时器时长的策略。当UE附着失败场景下，MME根据设置的策略控制UE重新发起附着请求的时间间隔。 
注意事项 
无 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
T3402INATTREJ|附着拒绝消息中是否携带T3402时长|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置附着拒绝消息中是否携带T3402时长。
SUPPT3402RAND|是否支持离散分配T3402时长|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在attach accept、attach reject、TAU accept消息中携带T3404定时器时，是否支持离散分配T3402时长。该参数设置为“否”：不支持离散配置，T3402时长根据SHOW MOBILE MANAGEMENT命令的“UE附着/跟踪区更新重发定时器T3402时长 ”参数进行设置。该参数设置为“是”：必须设置“T3402时长最小值”和“T3402时长最大值”。
T3402MIN|T3402时长最小值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于当T3402时长进行离散分配时，设置T3402时长范围的最小值 。
T3402MAX|T3402时长最大值 （秒）|参数可选性:任选参数；参数类型:整数。|该参数用于当T3402时长进行离散分配时，设置T3402时长范围的最大值。
命令举例 
查询T3402定时器策略配置。 
SHOW T3402 POLICY CFG; 
`
(No.1) : SHOW T3402 POLICY CFG:
-----------------NFS_MMESGSN_0----------------
操作维护       附着拒绝消息中是否携带T3402时长 是否支持离散分配T3402时长 T3402时长最小值（秒） T3402时长最大值 （秒） 
----------------------------------------------------------------------------------------------------------------------
修改           否                              否                        400                   730                    
----------------------------------------------------------------------------------------------------------------------
记录数：1
` 
父主题： [T3402定时器策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
