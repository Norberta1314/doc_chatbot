 LCS配置 
背景知识 
移动位置业务是一种提供移动用户位置信息的业务，也叫定位业务(LCS)。它提供的位置信息可以被网络内部使用，也可以被第三方使用，其典型的应用包括： 
 
用于网络内部使用，如改善网络运行性能、网络维护、支持补充业务、支持移动智能业务等。
 
 
用于商用的增值业务。如根据用户当前位置给予向导服务。
 
 
MME用于紧急呼叫时确定起呼用户位置。
 
 
用于经批准的安全部门跟踪用户位置。
 
 
LCS涉及的实体包括LCS服务方、LCS客户方，以及被定位的目标用户。 
功能描述 
实现LCS功能，在SGSN网元上需要进行如下配置： 
 
SGSN GMLC配置：配置SGSN允许或限制接入的GMLC。 
 
SGSN VGMLC配置：配置SGSN网元用户进行注册时签约的VGMLC号码。 
 
实现LCS功能，在MME网元上需要进行如下配置： 
 
MME GMLC配置：配置MME允许接入的GMLC。 
 
MME VGMLC配置：配置MME网元用户进行注册时签约的VGMLC号码。 
 
ESMLC的配置：配置与MME相连的ESMLC路由。 
 
相关主题 
 
SGSN GMLC配置
 
 
SGSN VGMLC配置
 
 
MME VGMLC配置
 
 
E-SMLC配置
 
 
父主题： [业务配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN GMLC配置 
# SGSN GMLC配置 
背景知识 
            
            GMLC（Gateway Mobile Location Center，网关移动位置中心）是外部位置程序访问PLMN的第一个结点，它执行注册授权检查和从HLR/HSS请求路由信息。根据协议和运营商的要求，SGSN能够识别其他国家或者本国其他PLMN的GMLC号码，同时限制某些GMLC接入到SGSN执行定位。
        
功能描述 
            
            进行定位GMLC配置后，SGSN通过国家码或者GMLC的号码能够识别哪些GMLC允许接入SGSN执行定位操作，哪些GMLC不允许接入SGSN执行定位操作。
        
相关主题 
 
新增SGSN GMLC(ADD GMLC)
 
 
修改SGSN GMLC(SET GMLC)
 
 
删除SGSN GMLC(DEL GMLC)
 
 
查询SGSN GMLC(SHOW GMLC)
 
 
父主题： [LCS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增SGSN GMLC(ADD GMLC) 
## 新增SGSN GMLC(ADD GMLC) 
命令功能 
该命令用于在SGSN上新增一个受限制的GMLC。当运营商需要新增限制接入的GMLC时，使用该命令。该命令执行成功后，在SGSN上增加一个受限制的GMLC。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CC|国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~4个字符。|该参数代表某一国家或地区编码，如86代表中国。
NDC|国家目的码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~4个字符。|该参数代表某一类网络，如139代表移动。
ENABLE|允许标志|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否允许GMLC接入SGSN。取值含义："允许接入(YES)"：允许GMLC接入SGSN。"不允许接入(NO)"：不允许GMLC接入SGSN。
SELMODE|判断选择标志|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数表示根据GMLC前缀国家码或整个GMLC号码作为判断，允许/不允许该GMLC接入SGSN。取值含义："根据CC(CC)"：根据GMLC前缀国家码作为判断，允许/不允许该GMLC接入SGSN。"根据CC+NDC(CC+NDC)"：根据GMLC号码作为判断，允许/不允许该GMLC接入SGSN。
命令举例 
新增一个受限制的GMLC，国家码为"86"，国家目的码为"138"，允许标志为"YES",判断选择标志为“CC”。 
ADD GMLC:CC="86",NDC="138",ENABLE="YES",SELMODE="CC"; 
父主题： [SGSN GMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改SGSN GMLC(SET GMLC) 
## 修改SGSN GMLC(SET GMLC) 
命令功能 
该命令用于在SGSN上修改已配置GMLC的属性。当运营商需要修改已配置GMLC的属性时，使用该命令。该命令执行成功后，GMLC属性发生改变。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CC|国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~4个字符。|该参数代表某一国家或地区编码，如86代表中国。
NDC|国家目的码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~4个字符。|该参数代表某一类网络，如139代表移动。
ENABLE|允许标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否允许GMLC接入SGSN。取值含义："允许接入(YES)"：允许GMLC接入SGSN。"不允许接入(NO)"：不允许GMLC接入SGSN。
SELMODE|判断选择标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示根据GMLC前缀国家码或整个GMLC号码作为判断，允许/不允许该GMLC接入SGSN。取值含义："根据CC(CC)"：根据GMLC前缀国家码作为判断，允许/不允许该GMLC接入SGSN。"根据CC+NDC(CC+NDC)"：根据GMLC号码作为判断，允许/不允许该GMLC接入SGSN。
命令举例 
将国家码为"86"，国家目的码为"138"的GMLC判断选择标志修改为"CC+NDC"。 
SET GMLC:CC="86",NDC="138",ENABLE="YES",SELMODE="CC+NDC"; 
父主题： [SGSN GMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除SGSN GMLC(DEL GMLC) 
## 删除SGSN GMLC(DEL GMLC) 
命令功能 
该命令用于删除SGSN上的GMLC。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CC|国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~4个字符。|该参数代表某一国家或地区编码，如86代表中国。
NDC|国家目的码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~4个字符。|该参数代表某一类网络，如139代表移动。
命令举例 
删除国家码为"86"，国家目的码为"138"的GMLC。 
DEL GMLC:CC="86",NDC="138"; 
父主题： [SGSN GMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN GMLC(SHOW GMLC) 
## 查询SGSN GMLC(SHOW GMLC) 
命令功能 
该命令用于查询受限制的GMLC配置信息。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CC|国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~4个字符。|该参数代表某一国家或地区编码，如86代表中国。
NDC|国家目的码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~4个字符。|该参数代表某一类网络，如139代表移动。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CC|国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~4个字符。|该参数代表某一国家或地区编码，如86代表中国。
NDC|国家目的码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~4个字符。|该参数代表某一类网络，如139代表移动。
ENABLE|允许标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否允许GMLC接入SGSN。取值含义："允许接入(YES)"：允许GMLC接入SGSN。"不允许接入(NO)"：不允许GMLC接入SGSN。
SELMODE|判断选择标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示根据GMLC前缀国家码或整个GMLC号码作为判断，允许/不允许该GMLC接入SGSN。取值含义："根据CC(CC)"：根据GMLC前缀国家码作为判断，允许/不允许该GMLC接入SGSN。"根据CC+NDC(CC+NDC)"：根据GMLC号码作为判断，允许/不允许该GMLC接入SGSN。
命令举例 
查询GMLC配置信息。 
SHOW GMLC; 
`
命令 (No.1): SHOW GMLC
操作维护        国家码  国家目的码  允许标志    判断选择标志 
----------------------------------------------------------------
复制 修改 删除  460     01          不允许接入  根据CC 
复制 修改 删除  460     03          不允许接入  根据CC+NDC 
----------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.032 秒）。
` 
父主题： [SGSN GMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# SGSN VGMLC配置 
# SGSN VGMLC配置 
背景知识 
            
            VGMLC（Visited GMLC，拜访GMLC）是和SGSN直接相连的GMLC，定位消息通过VGMLC和SGSN进行通讯。当用户附着到网络时，SGSN给用户分配一个VGMLC的IP地址，该地址通过位置更新请求消息带给HLR。
        
功能描述 
            
            完成SGSN VGMLC配置后，SGSN可实现不同的用户使用不同的VGMLC，从而实现定位的VGMLC的负荷分担。VGMLC的IP地址是和SGSN实际相连的GMLC地址，由运营商统一规划。
        
相关主题 
 
新增SGSN VGMLC(ADD SGSN VGMLC)
 
 
修改SGSN VGMLC(SET SGSN VGMLC)
 
 
删除SGSN VGMLC(DEL SGSN VGMLC)
 
 
查询SGSN VGMLC(SHOW SGSN VGMLC)
 
 
父主题： [LCS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增SGSN VGMLC(ADD SGSN VGMLC) 
## 新增SGSN VGMLC(ADD SGSN VGMLC) 
命令功能 
该命令用于新增拜访移动定位中心地址。该地址为用户所在无线区域下归属的定位中心的地址，移动定位中心完成对区域下用户提供定位相关服务。新增该地址，表明SGSN支持所配置的VGMLC，允许该VGMLC通过本SGSN局，向本局用户进行定位业务。 
注意事项 
 
该命令所配置IP地址可以为IPV4类型，也可以为IPV6类型，依照地址长短来区分，配置时会对地址格式进行检查。
 
 
该命令支持ADD命令，也就意味着，SGSN支持多个VGMLC配置，在选择时采用轮选的方式，在配置的VGMLC列表中轮选出一个地址，带给HLR。
 
 
该命令所配的VGMLC地址轮选出来带给HLR。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:必选参数；参数类型:地址|该参数用于指定VGMLC对应的IP地址。地址类型为IPV4或IPV6，配置时会有地址格式的检查。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定一个特定的名称，可以设置成该设备所在地名或者局点等信息，主要起备注作用。
命令举例 
增加VGMLC地址为1.1.1.1。 
ADD SGSN VGMLC:VGMLCADDR="1.1.1.1"; 
父主题： [SGSN VGMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改SGSN VGMLC(SET SGSN VGMLC) 
## 修改SGSN VGMLC(SET SGSN VGMLC) 
命令功能 
根据VGMLC地址修改SGSN VGMLC。该命令由于只有两个参数，而VGMLC地址是必须字段，所以只能依据该字段修改用户别名。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:必选参数；参数类型:地址|该参数用于指定VGMLC对应的IP地址。地址类型为IPV4或IPV6，配置时会有地址格式的检查。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定一个特定的名称，可以设置成该设备所在地名或者局点等信息，主要起备注作用。
命令举例 
修改VGMLC地址为1.1.1.1。 
SET SGSN VGMLC:VGMLCADDR="1.1.1.1"; 
父主题： [SGSN VGMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除SGSN VGMLC(DEL SGSN VGMLC) 
## 删除SGSN VGMLC(DEL SGSN VGMLC) 
命令功能 
根据VGMLC地址删除SGSN VGMLC。当SGSN不再支持该VGMLC的定位业务时，执行该删除命令。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:必选参数；参数类型:地址|该参数用于指定VGMLC对应的IP地址。地址类型为IPV4或IPV6，配置时会有地址格式的检查。
命令举例 
删除VGMLC地址为1.1.1.1。 
DEL SGSN VGMLC:VGMLCADDR="1.1.1.1"; 
父主题： [SGSN VGMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询SGSN VGMLC(SHOW SGSN VGMLC) 
## 查询SGSN VGMLC(SHOW SGSN VGMLC) 
命令功能 
查询SGSN VGMLC，如果不带任何参数，则查询所有已配置的SGSN VGMLC信息，如果参数中填写VGMLC地址，则为查询该VGMLC。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:任选参数；参数类型:地址|该参数用于指定VGMLC对应的IP地址。地址类型为IPV4或IPV6，配置时会有地址格式的检查。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:任选参数；参数类型:地址|该参数用于指定VGMLC对应的IP地址。地址类型为IPV4或IPV6，配置时会有地址格式的检查。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数用于指定一个特定的名称，可以设置成该设备所在地名或者局点等信息，主要起备注作用。
命令举例 
查询所有的SGSN VGMLC地址。 
SHOW SGSN VGMLC; 
`
命令 (No.1): SHOW SGSN VGMLC
操作维护         VGMLC地址   用户别名
-------------------------------------
复制 修改 删除   1.1.1.1     
-------------------------------------
记录数 1
命令执行成功（耗时 0.062 秒）。
` 
父主题： [SGSN VGMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# MME VGMLC配置 
# MME VGMLC配置 
背景知识 
            
            VGMLC（Visited GMLC，拜访GMLC）是和MME直接相连的GMLC，定位消息通过VGMLC和MME进行通讯。当用户附着到网络时，MME给用户分配一个VGMLC的IP地址，该地址通过位置更新请求消息带给HSS。
        
功能描述 
            
            完成MME VGMLC配置后，MME可实现不同的用户使用不同的VGMLC，从而实现定位的VGMLC的负荷分担。VGMLC的IP地址是和MME实际相连的GMLC地址，由运营商统一规划。
        
相关主题 
 
新增MME VGMLC(ADD MME VGMLC)
 
 
修改MME VGMLC(SET MME VGMLC)
 
 
删除MME VGMLC(DEL MME VGMLC)
 
 
查询MME VGMLC(SHOW MME VGMLC)
 
 
父主题： [LCS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增MME VGMLC(ADD MME VGMLC) 
## 新增MME VGMLC(ADD MME VGMLC) 
命令功能 
该命令用于在MME上新增一个VGMLC地址。当运营商需要使用定位业务时，使用该命令。该命令执行成功后，当用户附着时，MME会分配一个VGMLC的IP地址给该用户。
注意事项 
 
该配置需要License的支持，对应的License项为“MME/SGSN支持LCS功能”。 
 
 
 该配置生效还需要当前MME支持的HSS协议版本号为R9以上，使用SHOW DIAMADJ命令查询协议版本号，使用SET DIAMADJ命令修改协议版本号。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:必选参数；参数类型:地址|VGMLC的地址，只能填写一个ipv4地址或者一个ipv6地址，不能为全0。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该条配置记录的名称，可以说明配置含义，便于理解。
命令举例 
新增一个VGMLC，地址为"192.168.0.1"，用户别名为"test"。 
ADD MME VGMLC:VGMLCADDR=192.168.0.1,NAME="test"; 
父主题： [MME VGMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改MME VGMLC(SET MME VGMLC) 
## 修改MME VGMLC(SET MME VGMLC) 
命令功能 
该命令用于在MME上修改已配置VGMLC的属性。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:必选参数；参数类型:地址|VGMLC的地址，只能填写一个ipv4地址或者一个ipv6地址，不能为全0。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该条配置记录的名称，可以说明配置含义，便于理解。
命令举例 
将VGMLC地址为"192.168.0.1"的用户别名修改为"test1"。 
SET MME VGMLC:VGMLCADDR=192.168.0.1,NAME="test1"; 
父主题： [MME VGMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除MME VGMLC(DEL MME VGMLC) 
## 删除MME VGMLC(DEL MME VGMLC) 
命令功能 
该命令用于删除MME上的VGMLC。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:必选参数；参数类型:地址|VGMLC的地址，只能填写一个ipv4地址或者一个ipv6地址，不能为全0。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。
命令举例 
删除地址为"192.168.0.1"的VGMLC。 
DEL MME VGMLC:VGMLCADDR=192.168.0.1; 
父主题： [MME VGMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询MME VGMLC(SHOW MME VGMLC) 
## 查询MME VGMLC(SHOW MME VGMLC) 
命令功能 
该命令用于查询已配置的VGMLC信息。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:任选参数；参数类型:地址|VGMLC的地址，只能填写一个ipv4地址或者一个ipv6地址，不能为全0。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
VGMLCADDR|VGMLC地址|参数可选性:任选参数；参数类型:地址|VGMLC的地址，只能填写一个ipv4地址或者一个ipv6地址，不能为全0。IP地址设置为IPv6类型地址时，需要license的支持，对应的license项为“IPv6功能”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该条配置记录的名称，可以说明配置含义，便于理解。
命令举例 
查询MME上已配置的VGMLC信息。 
SHOW MME VGMLC; 
`
命令 (No.1): SHOW MME VGMLC
操作维护         VGMLC地址                                 用户别名
-------------------------------------------------------------------
复制 修改 删除   192.0.1.165                               模拟VGMLC_liuyu1
复制 修改 删除   192.0.1.166                               
-------------------------------------------------------------------
记录数2
命令执行成功（耗时 0.064 秒）。
` 
父主题： [MME VGMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# E-SMLC配置 
# E-SMLC配置 
背景知识 
            
            E-SMLC（Evolved Serving Mobile Location Centre，演进服务移动定位中心）实现用户当前位置的计算。ESMLC ID作为ESMLC的一个标识，由运营商统一规划。MME通过ESMLC ID进行路由的选择。
        
功能描述 
            
            E-MSLC配置用于设置MME到E-SMLC的路由，实现MME与E-SMLC之间的路由选择和负荷分担。
        
相关主题 
 
新增E-SMLC(ADD ESMLC)
 
 
修改E-SMLC(SET ESMLC)
 
 
删除E-SMLC(DEL ESMLC)
 
 
查询E-SMLC(SHOW ESMLC)
 
 
父主题： [LCS配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 新增E-SMLC(ADD ESMLC) 
## 新增E-SMLC(ADD ESMLC) 
命令功能 
该命令用于在MME上新增一个E-SMLC 标识。 
E-SMLC是无线侧定位服务中使用的一个网元，当运营商需要投入定位业务时，使用该命令新增E-SMLC标识。 
命令执行成功后，MME和E-SMLC之间建立连接，定位服务可用。 
注意事项 
 
该命令需要先配置静态的SCTP，配置命令为 ADD SCTPIDCFG。
 
 
 一个E-SMLC可以关联1-16条SCTP。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCID|E-SMLC标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|E-SMLC网元标识，全局唯一。
SCTPID|SCTP标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4112。|SCTP标识，一个E-SMLC最多可使用16个SCTP与MME建立连接。新增SCTP命令为： ADD SCTPIDCFG。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|运营商可以根据自己的命名习惯来为E-SMLC定义一个名称。
命令举例 
新增一个E-SMLC，E-SMLC ID为"1"，关联SCTP有四条，ID分别为"1&2&3&4"，NAME为"E1"。 
ADD ESMLC:ESMLCID=1,SCTPID=1&2&3&4,NAME="E1"; 
父主题： [E-SMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 修改E-SMLC(SET ESMLC) 
## 修改E-SMLC(SET ESMLC) 
命令功能 
该命令用于在MME上设置已有E-SMLC的属性。 
当运营商需要设置已有E-SMLC的属性时候使用该命令。 
命令执行成功后，MME和E-SMLC之间关联属性发生改变。 
注意事项 
该命令中只有SCTP ID和用户别名可以修改。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCID|E-SMLC标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|E-SMLC网元标识，全局唯一。
SCTPID|SCTP标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4112。|SCTP标识，一个E-SMLC最多可使用16个SCTP与MME建立连接。新增SCTP命令为： ADD SCTPIDCFG。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|运营商可以根据自己的命名习惯来为E-SMLC定义一个名称。
命令举例 
将ID为"1"的E-SMLC关联的SCTP ID设置为"1&2"，NAME设置为"E2"。 
SET ESMLC:ESMLCID=1,SCTPID=1&2,NAME="E2"; 
父主题： [E-SMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 删除E-SMLC(DEL ESMLC) 
## 删除E-SMLC(DEL ESMLC) 
命令功能 
该命令用于根据E-SMLC标识删除MME上的E-SMLC。 
命令执行成功后，MME和E-SMLC之间解除关联关系。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCID|E-SMLC标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|E-SMLC网元标识，全局唯一。
命令举例 
删除ID为"1"的E-SMLC。 
DEL ESMLC:ESMLCID=1; 
父主题： [E-SMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询E-SMLC(SHOW ESMLC) 
## 查询E-SMLC(SHOW ESMLC) 
命令功能 
该命令用于查询当前可用的E-SMLC信息。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCID|E-SMLC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|E-SMLC网元标识，全局唯一。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ESMLCID|E-SMLC标识|参数可选性:任选参数；参数类型:整数。|E-SMLC网元标识，全局唯一。
SCTP1|SCTP标识1|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识1。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP2|SCTP标识2|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识2。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP3|SCTP标识3|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识3。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP4|SCTP标识4|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识4。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP5|SCTP标识5|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识5。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP6|SCTP标识6|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识6。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP7|SCTP标识7|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识7。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP8|SCTP标识8|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识8。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP9|SCTP标识9|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识9。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP10|SCTP标识10|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识10。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP11|SCTP标识11|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识11。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP12|SCTP标识12|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识12一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP13|SCTP标识13|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识13。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP14|SCTP标识14|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识14。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP15|SCTP标识15|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识15。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
SCTP16|SCTP标识16|参数可选性:任选参数；参数类型:字符型。|MME与E-SMLC连接的SCTP标识16。一个E-SMLC最多可使用16个SCTP与MME建立连接。每个SCTP都是同样的作用，没有任何区别。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|运营商可以根据自己的命名习惯来为E-SMLC定义一个名称。
命令举例 
查询ID为"1"的E-SMLC。 
SHOW ESMLC:ESMLCID=1; 
`
命令 (No.13): SHOW ESMLC:ESMLCID=1;
操作维护        E-SMLC标识  SCTP标识1  SCTP标识2  SCTP标识3  SCTP标识4  SCTP标识5  SCTP标识6  SCTP标识7  SCTP标识8  SCTP标识9  SCTP标识10  SCTP标识11  SCTP标识12  SCTP标识13  SCTP标识14  SCTP标识15  SCTP标识16  用户别名 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除  1           1          2          3          4                                                                                                                                                     E1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.023 秒）。
` 
父主题： [E-SMLC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
