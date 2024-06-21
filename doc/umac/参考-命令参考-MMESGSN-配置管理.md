 配置管理 
背景知识 
数据配置是指制作能够使通信设备正常运行的数据，并将这些数据设定到通信设备的操作。配置管理用于对全局的数据配置命令进行详细的描述。 
功能描述 
用来详细阐述ZXUN uMAC产品中与业务维护相关的配置命令。 
相关主题 
 
系统配置
 
 
业务配置
 
 
安全网关对接配置
 
 
高级配置
 
 
安全变量
 
 
DNS服务器配置
 
 
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 安全网关对接配置 
# 安全网关对接配置 
相关主题 
 
进入安全网关对接模式(ENTER ESTI)
 
 
退出安全网关对接模式(EXIT ESTI)
 
 
安全网关对接基础数据配置
 
 
安全网关对接CC配置
 
 
X3口报文过滤配置
 
 
父主题： [配置管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 进入安全网关对接模式(ENTER ESTI) 
## 进入安全网关对接模式(ENTER ESTI) 
命令功能 
进入安全网关对接模式
注意事项 
无。
命令举例 
进入安全网关对接模式 
ENTER ESTI 
父主题： [安全网关对接配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 退出安全网关对接模式(EXIT ESTI) 
## 退出安全网关对接模式(EXIT ESTI) 
命令功能 
退出安全网关对接模式
注意事项 
无。
命令举例 
退出安全网关对接模式 
EXIT ESTI 
父主题： [安全网关对接配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 安全网关对接基础数据配置 
## 安全网关对接基础数据配置 
相关主题 
 
设置安全网关对接基础数据(SET LICFG)
 
 
查询安全网关对接基础数据(SHOW LICFG)
 
 
查询安全网关对接实例号(SHOW LIMODULE)
 
 
父主题： [安全网关对接配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置安全网关对接基础数据(SET LICFG) 
### 设置安全网关对接基础数据(SET LICFG) 
命令功能 
该命令用于设置安全网关对接基础数据。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
LIFLAG|是否支持安全网关对接接口功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否支持安全网关对接接口功能
NENO|SGSN逻辑网元编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~1000。|SGSN逻辑网元编号
MMENENO|MME逻辑网元编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~1000。|MME逻辑网元编号
PWD|接入密码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~64个字符。|接入密码
NEIP|安全网关对接业务地址|参数可选性:任选参数；参数类型:地址|安全网关对接业务地址
VRF|安全网关对接VRF ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|安全网关对接VRF ID
NEX1X2PORT|安全网关对接本端X1X2端口号|参数可选性:任选参数；参数类型:整数；参数范围为:15000~15999。|安全网关对接本端X1X2端口号
LIGX1X2IP|安全网关X1X2地址|参数可选性:任选参数；参数类型:地址|安全网关X1X2地址
ENCRYPTION|用户号码简单加密|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否加密
COMBOMONIMS|合法安全网关对接布控记录数|参数可选性:任选参数；参数类型:整数；参数范围为:1~800000。|合法安全网关对接上下文数(全局)
SPRTLIVER|MME支持安全网关对接规范|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME支持安全网关对接规范
LIOLCTRL|启用安全网关对接接口流量控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|启用安全网关对接接口流量控制
CPENCRYPTION|控制面加密|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|控制面加密
CPENCRYPALGO|控制面加密算法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|控制面加密算法
CPENCRYPPWD|控制面加密密钥|参数可选性:任选参数；参数类型:字符型；参数范围为:16~16个字符。|该参数用于设置uMAC安全网关对接控制面加密的算法密钥，密钥为16位的十六进制数值。
命令举例 
设置安全网关对接基础数据，支持安全网关对接接口功能，SGSN逻辑网元编号为100，安全网关对接业务地址为1.1.1.1，安全网关对接本端X1X2端口号为15000，安全网关X1X2地址为2.2.2.2。 
SET LICFG:LIFLAG="YES",NENO=100,NEIP="1.1.1.1",NEX1X2PORT=15000,LIGX1X2IP="2.2.2.2"; 
父主题： [安全网关对接基础数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询安全网关对接基础数据(SHOW LICFG) 
### 查询安全网关对接基础数据(SHOW LICFG) 
命令功能 
该命令用于查询安全网关对接基础数据。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LIFLAG|是否支持安全网关对接接口功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否支持安全网关对接接口功能
NENO|SGSN逻辑网元编号|参数可选性:任选参数；参数类型:整数。|SGSN逻辑网元编号
MMENENO|MME逻辑网元编号|参数可选性:任选参数；参数类型:整数。|MME逻辑网元编号
NEIP|安全网关对接业务地址|参数可选性:任选参数；参数类型:地址|安全网关对接业务地址
VRF|安全网关对接VRF ID|参数可选性:任选参数；参数类型:整数。|安全网关对接VRF ID
NEX1X2PORT|安全网关对接本端X1X2端口号|参数可选性:任选参数；参数类型:整数。|安全网关对接本端X1X2端口号
LIGX1X2IP|安全网关X1X2地址|参数可选性:任选参数；参数类型:地址|安全网关X1X2地址
ENCRYPTION|用户号码简单加密|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否加密
MONIMS|合法安全网关对接布控记录数|参数可选性:任选参数；参数类型:整数。|合法安全网关对接上下文数(全局)
SPRTLIVER|MME支持安全网关对接规范|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME支持安全网关对接规范
LIOLCTRL|启用安全网关对接接口流量控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|启用安全网关对接接口流量控制
CPENCRYPTION|控制面加密|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|控制面加密
CPENCRYPALGO|控制面加密算法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|控制面加密算法
命令举例 
查询安全网关对接基础数据。 
SHOW LICFG; 
`
命令 (No.2): SHOW LICFG;
是否支持安全网关对接接口功能   SGSN逻辑网元编号   MME逻辑网元编号     安全网关对接业务地址   安全网关对接VRF ID   安全网关对接本端X1X2端口号   安全网关X1X2地址   用户号码简单加密   合法安全网关对接上下文数(全局)   MME支持安全网关对接规范    启用安全网关对接接口流量控制   控制面加密   控制面加密算法 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
支持安全网关对接               100                0                   1.1.1.1        0            15000                2.2.2.2        否                 60000                    支持ETSI规范       不启用                 否           AES256         
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.063 秒）。
` 
父主题： [安全网关对接基础数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询安全网关对接实例号(SHOW LIMODULE) 
### 查询安全网关对接实例号(SHOW LIMODULE) 
命令功能 
查询安全网关对接实例号
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MODULE|SC实例号|参数可选性:任选参数；参数类型:整数。|SC实例号
命令举例 
查询安全网关对接实例号。 
SHOW LIMODULE; 
`
命令 (No.6): SHOW LIMODULE
SC实例号 
-------------
25 
-------------
记录数 1
命令执行成功（耗时 0.768 秒）。
` 
父主题： [安全网关对接基础数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 安全网关对接CC配置 
## 安全网关对接CC配置 
相关主题 
 
设置安全网关对接CC配置(SET LICC)
 
 
查询安全网关对接CC配置(SHOW LICC)
 
 
父主题： [安全网关对接配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置安全网关对接CC配置(SET LICC) 
### 设置安全网关对接CC配置(SET LICC) 
命令功能 
该命令用于设置安全网关对接CC配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SVRSIGX3IP|对端 X3控制面地址|参数可选性:任选参数；参数类型:地址|对端 X3控制面地址
SVRMEDIAX3IP|对端 X3媒体面地址|参数可选性:任选参数；参数类型:地址|对端 X3媒体面地址
X3LINKCHECK|开启安全网关对接X3链路检测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|开启安全网关对接X3链路检测
X3LINKCHKNUM|安全网关对接X3链路检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:3~10。|安全网关对接X3链路检测次数
X3LINKCHKTIMER|安全网关对接X3链路检测间隔(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~3600。|安全网关对接X3链路检测间隔(秒)
NESIGX3PORT|安全网关对接本端控制面X3端口号|参数可选性:任选参数；参数类型:整数；参数范围为:15000~15999。|安全网关对接本端控制面X3端口号
NEMEDIAX3PORT|安全网关对接本端用户面X3端口号|参数可选性:任选参数；参数类型:整数；参数范围为:15000~15999。|安全网关对接本端用户面X3端口号
SVRSIGX3PORT|对端控制面X3端口号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|对端控制面X3端口号
SVRMEDIAX3PORT|对端用户面X3端口号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|对端用户面X3端口号
DX3VRFID|安全网关对接X3口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|安全网关对接X3口VRF标识
NEMEDIAX3IP|安全网关对接本端用户面X3口IP地址|参数可选性:任选参数；参数类型:地址|安全网关对接本端用户面X3口IP地址
UPENCRYPTION|用户面加密|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置uMAC安全网关对接是否支持用户面加密。
UPENCRYPALGO|用户面加密算法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置uMAC安全网关对接用户面加密的算法。
UPENCRYPKEY|用户面加密密钥|参数可选性:任选参数；参数类型:字符型；参数范围为:16~16个字符。|该参数用于设置uMAC安全网关对接用户面加密的算法密钥，密钥为16位的十六进制数值。
SQNGROUPNO|SQN组号|参数可选性:任选参数；参数类型:整数；参数范围为:2~4294967295。|该参数用于设置uMAC安全网关对接用户面加密的算法SQN组号。
命令举例 
设置安全网关对接CC配置，对端X3控制面地址为1.1.1.1，对端X3媒体面地址为2.2.2.2，开启安全网关对接X3链路检测。 
SET LICC:SVRSIGX3IP="1.1.1.1",SVRMEDIAX3IP="2.2.2.2",X3LINKCHECK="ON"; 
父主题： [安全网关对接CC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询安全网关对接CC配置(SHOW LICC) 
### 查询安全网关对接CC配置(SHOW LICC) 
命令功能 
该命令用于查询安全网关对接CC配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SVRSIGX3IP|对端 X3控制面地址|参数可选性:任选参数；参数类型:地址|对端 X3控制面地址
SVRMEDIAX3IP|对端 X3媒体面地址|参数可选性:任选参数；参数类型:地址|对端 X3媒体面地址
X3LINKCHECK|开启安全网关对接X3链路检测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|开启安全网关对接X3链路检测
X3LINKCHKNUM|安全网关对接X3链路检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:3~10。|安全网关对接X3链路检测次数
X3LINKCHKTIMER|安全网关对接X3链路检测间隔(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~3600。|安全网关对接X3链路检测间隔(秒)
NESIGX3PORT|安全网关对接本端控制面X3端口号|参数可选性:任选参数；参数类型:整数；参数范围为:15000~15999。|安全网关对接本端控制面X3端口号
NEMEDIAX3PORT|安全网关对接本端用户面X3端口号|参数可选性:任选参数；参数类型:整数；参数范围为:15000~15999。|安全网关对接本端用户面X3端口号
SVRSIGX3PORT|对端控制面X3端口号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|对端控制面X3端口号
SVRMEDIAX3PORT|对端用户面X3端口号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|对端用户面X3端口号
DX3VRFID|安全网关对接X3口VRF标识|参数可选性:任选参数；参数类型:整数。|安全网关对接X3口VRF标识
NEMEDIAX3IP|安全网关对接本端用户面X3口IP地址|参数可选性:任选参数；参数类型:地址|安全网关对接本端用户面X3口IP地址
UPENCRYPTION|用户面加密|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置uMAC安全网关对接是否支持用户面加密。
UPENCRYPALGO|用户面加密算法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置uMAC安全网关对接用户面加密的算法。
SQNGROUPNO|SQN组号|参数可选性:任选参数；参数类型:整数。|该参数用于设置uMAC安全网关对接用户面加密的算法SQN组号。
命令举例 
查询安全网关对接CC配置。 
SHOW LICC; 
`
命令 (No.32): SHOW LICC
操作维护       对端 X3控制面地址 对端 X3媒体面地址 开启安全网关对接X3链路检测 安全网关对接X3链路检测次数 安全网关对接X3链路检测间隔(秒) 安全网关对接本端控制面X3端口号 安全网关对接本端用户面X3端口号 对端控制面X3端口号 对端用户面X3端口号 安全网关对接X3口VRF标识 安全网关对接本端用户面X3口IP地址 用户面加密 用户面加密算法 SQN组号 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           1.1.1.1           2.2.2.2           开启                       3                          10                             15000                          15000                          0                  0                  0                       0.0.0.0                          否         AES256         0       
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
命令执行成功（耗时 0.069 秒）。
` 
父主题： [安全网关对接CC配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## X3口报文过滤配置 
## X3口报文过滤配置 
相关主题 
 
X3口报文过滤全局配置
 
 
X3口报文过滤规则配置
 
 
父主题： [安全网关对接配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### X3口报文过滤全局配置 
### X3口报文过滤全局配置 
相关主题 
 
设置X3口报文过滤全局参数(SET X3FILTERFG)
 
 
查询X3口报文过滤全局参数(SHOW X3FILTERFG)
 
 
父主题： [X3口报文过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置X3口报文过滤全局参数(SET X3FILTERFG) 
#### 设置X3口报文过滤全局参数(SET X3FILTERFG) 
命令功能 
设置X3口报文过滤全局参数
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
FILTERFG|过滤报文|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤报文
DEFPROC|报文默认处理方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|报文默认处理方式
命令举例 
设置X3口报文过滤全局参数 
SET X3FILTERFG:FILTERFG=YES,DEFPROC=FORWARD; 
父主题： [X3口报文过滤全局配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询X3口报文过滤全局参数(SHOW X3FILTERFG) 
#### 查询X3口报文过滤全局参数(SHOW X3FILTERFG) 
命令功能 
查询X3口报文过滤全局参数
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FILTERFG|过滤报文|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤报文
DEFPROC|报文默认处理方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|报文默认处理方式
命令举例 
查询X3口报文过滤全局参数 
SHOW X3FILTERFG; 
`
命令 (No.1): SHOW X3FILTERFG
操作维护       过滤报文 报文默认处理方式 
-----------------------------------------
修改           是       转发             
-----------------------------------------
记录数：1
命令执行成功（耗时 0.069 秒）。
` 
父主题： [X3口报文过滤全局配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### X3口报文过滤规则配置 
### X3口报文过滤规则配置 
相关主题 
 
新增X3口报文过滤规则(ADD X3FILTER RULE)
 
 
修改X3口报文过滤规则(SET X3FILTER RULE)
 
 
删除X3口报文过滤规则(DEL X3FILTER RULE)
 
 
查询X3口报文过滤规则(SHOW X3FILTER RULE)
 
 
父主题： [X3口报文过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增X3口报文过滤规则(ADD X3FILTER RULE) 
#### 新增X3口报文过滤规则(ADD X3FILTER RULE) 
命令功能 
新增X3口报文过滤规则
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|规则标识
PROTYPE|IP协议类型|参数可选性:必须单选参数；参数类型:枚举。参见枚举定义。|IP协议类型
PROVALUE|IP协议值|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~255。|IP协议值
DESTPORTBEGIN|远端起始端口号|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。|远端起始端口号
DESTPORTEND|远端结束端口号|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。|远端结束端口号
RESULT|报文处理方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:FORWARD。|报文处理方式
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名
命令举例 
新增X3口报文过滤规则 
ADD X3FILTER RULE:ID=1,PROVALUE=1; 
父主题： [X3口报文过滤规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改X3口报文过滤规则(SET X3FILTER RULE) 
#### 修改X3口报文过滤规则(SET X3FILTER RULE) 
命令功能 
修改X3口报文过滤规则
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|规则标识
DESTPORTBEGIN|远端起始端口号|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。|远端起始端口号
DESTPORTEND|远端结束端口号|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。|远端结束端口号
RESULT|报文处理方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|报文处理方式
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名
命令举例 
修改X3口报文过滤规则 
SET X3FILTER RULE:ID=1; 
父主题： [X3口报文过滤规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除X3口报文过滤规则(DEL X3FILTER RULE) 
#### 删除X3口报文过滤规则(DEL X3FILTER RULE) 
命令功能 
删除X3口报文过滤规则
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|规则标识
命令举例 
删除X3口报文过滤规则 
DEL X3FILTER RULE:ID=1; 
父主题： [X3口报文过滤规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询X3口报文过滤规则(SHOW X3FILTER RULE) 
#### 查询X3口报文过滤规则(SHOW X3FILTER RULE) 
命令功能 
查询X3口报文过滤规则
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|规则标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|规则标识
PROTYPE|IP协议类型|参数可选性:任意单选参数；参数类型:枚举。参见枚举定义。|IP协议类型
PROVALUE|IP协议值|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~255。|IP协议值
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|规则标识|参数可选性:任选参数；参数类型:整数。|规则标识
PROTYPE1|IP协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|IP协议类型
PROVALUE|IP协议值|参数可选性:任选参数；参数类型:整数。|IP协议值
DESTPORTBEGIN|远端起始端口号|参数可选性:任选参数；参数类型:整数。|远端起始端口号
DESTPORTEND|远端结束端口号|参数可选性:任选参数；参数类型:整数。|远端结束端口号
RESULT|报文处理方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|报文处理方式
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户别名
命令举例 
查询X3口报文过滤规则 
SHOW X3FILTER RULE:PROVALUE=5; 
`
命令 (No.1): SHOW X3FILTER RULE:PROVALUE=5;
操作维护       规则标识 IP协议类型 IP协议值 远端起始端口号 远端结束端口号 报文处理方式 用户别名 
------------------------------------------------------------------------------------------------
复制 修改 删除 1                   5                                      转发                  
------------------------------------------------------------------------------------------------
记录数：1
命令执行成功（耗时 0.069 秒）。
` 
父主题： [X3口报文过滤规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 高级配置 
# 高级配置 
背景知识 
系统提供了拥塞控制、GTP节点控制、容灾、监控、安全加固等配置项，通过配置这些内容，可以保障系统运行的安全性、稳定性。 
功能描述 
高级配置中提供了拥塞控制、GTP节点控制、容灾、监控、安全加固等配置项。 
相关主题 
 
拥塞和过负荷控制配置
 
 
软件参数配置
 
 
资源告警配置
 
 
话单存储空间使用率告警参数配置
 
 
性能管理专用配置
 
 
MCDR配置
 
 
CDR过滤配置
 
 
USUP报文缓存配置
 
 
TCP MSS协商配置
 
 
跟踪管理配置
 
 
SGSN黑名单配置
 
 
Pool内SGSN重选配置
 
 
GTP链路告警过滤配置
 
 
GTP节点管理保护配置
 
 
系统可用性配置
 
 
区内GSN网段配置
 
 
CSFB配置
 
 
IP和位置关联配置
 
 
话单存储空间配置
 
 
基于TAC的Gb加密算法配置
 
 
合法区域接入限制配置
 
 
eNodeB告警配置
 
 
EMS局向链路配置
 
 
GTP节点白名单配置
 
 
MME信令风暴抑制配置
 
 
SGSN信令风暴抑制配置
 
 
默认承载重建配置
 
 
容灾恢复配置
 
 
信令跟踪消息上报限制配置
 
 
MME失败原因细化配置
 
 
PGW重选配置
 
 
内部统计参数配置
 
 
GTP原因值与NAS原因值映射配置
 
 
KPI监控维护
 
 
内部资源监测配置
 
 
CDU租户配置
 
 
负荷卸载优化
 
 
GTP源端口策略配置
 
 
PDN连接拒绝Back-off策略配置
 
 
PDP激活拒绝Back-off策略配置
 
 
S1MME接口管理
 
 
HSS故障旁路配置
 
 
MME分级备份策略配置
 
 
父主题： [配置管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 拥塞和过负荷控制配置 
## 拥塞和过负荷控制配置 
背景知识 
            
            过负荷控制功能，通过限制本网元接入的业务量，降低本网元或者邻接网元的负荷，避免因负荷过高导致本网元或者邻接网元设备异常或崩溃。
        
功能描述 
SGSN/MME过负荷控制功能包括以下几个子功能： 
 
入向业务总量控制：
控制单位时间内允许通过的业务总量，业务总量的计算为各个单项业务的加权叠加。
 
 
入向单项业务控制。
控制单位时间内通过的各个单项业务量。
 
 
CPU拥塞控制
在MP上根据CPU拥塞情况对各类业务限制一定的通过率，保护MP CPU不会冲高。
 
 
出向单向业务控制
对于本系统发起的到其他网元（比如HSS、EIR）的业务，限制一定的业务量，保护对方网元不会被冲击。
 
 
信令拥塞控制。
对于信令处理MP按照信令链路拥塞情况，保护信令链路。
 
 
通知对方网元拥塞
对于SGSN/MME，协议（3Gpp TS 25.413和36.413）支持Iu、S1口 overload消息，可以告知对方网元本局拥塞情况， 接收overload消息的网元就会控制本方发送的信令。对于Iu口，SGSN和RNC可以互相通知；对于S1口，只有MME通知eNodeB。
 
 
SGSN过负荷控制包括：过负荷基本配置、SGSN过负荷参数配置、SGSN业务控制配置。 
MME过负荷控制包括：过负荷基本配置、MME过负荷参数配置、MME业务控制配置。 
默认配置情况下，SGSN和MME开启CPU负荷控制和信令拥塞控制，但不开启业务通过数控制。默认配置对本网元做了较好的保护，并对邻接网元做了基本保护，不建议修改默认配置。 
相关主题 
 
本网元拥塞和过负荷控制配置
 
 
HSS过负荷控制配置
 
 
SGW过负荷控制配置
 
 
PGW过负荷控制配置
 
 
基于APN拥塞控制配置
 
 
基于MTC用户的拥塞控制配置
 
 
基于RAT拥塞控制配置
 
 
控制面数据拥塞控制配置
 
 
MME拥塞控制管理
 
 
MME/SGSN网管过负荷控制参数配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 本网元拥塞和过负荷控制配置 
### 本网元拥塞和过负荷控制配置 
背景知识 
            
            过负荷控制功能，通过限制本网元接入的业务量，降低本网元或者邻接网元的负荷，避免因负荷过高导致本网元或者邻接网元设备异常或崩溃。
        
功能描述 
SGSN/MME过负荷控制功能包括以下几个子功能： 
 
入向业务总量控制：
控制单位时间内允许通过的业务总量，业务总量的计算为各个单项业务的加权叠加。
 
 
入向单项业务控制。
控制单位时间内通过的各个单项业务量。
 
 
CPU拥塞控制
在MP上根据CPU拥塞情况对各类业务限制一定的通过率，保护MP CPU不会冲高。
 
 
出向单向业务控制
对于本系统发起的到其他网元（比如HSS、EIR）的业务，限制一定的业务量，保护对方网元不会被冲击。
 
 
信令拥塞控制。
对于信令处理MP按照信令链路拥塞情况，保护信令链路。
 
 
通知对方网元拥塞
对于SGSN/MME，协议（3Gpp TS 25.413和36.413）支持Iu、S1口 overload消息，可以告知对方网元本局拥塞情况， 接收overload消息的网元就会控制本方发送的信令。对于Iu口，SGSN和RNC可以互相通知；对于S1口，只有MME通知eNodeB。
 
 
SGSN过负荷控制包括：过负荷基本配置、SGSN过负荷参数配置、SGSN业务控制配置。 
MME过负荷控制包括：过负荷基本配置、MME过负荷参数配置、MME业务控制配置。 
默认配置情况下，SGSN和MME开启CPU负荷控制和信令拥塞控制，但不开启业务通过数控制。默认配置对本网元做了较好的保护，并对邻接网元做了基本保护，不建议修改默认配置。 
相关主题 
 
过负荷基本参数配置
 
 
SGSN过负荷参数配置
 
 
MME过负荷参数配置
 
 
SGSN业务控制配置
 
 
MME业务控制配置
 
 
UE无关的网元消息控制配置
 
 
业务类型过负荷控制配置
 
 
MME过负荷寻呼优化配置
 
 
MME接口消息控制配置
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 过负荷基本参数配置 
#### 过负荷基本参数配置 
背景知识 
SGSN/MME网元对于CPU拥塞控制和信令拥塞控制，采用“自适应二分法”算法，主要涉及到以下几个概念： 
过载区 
过载区分为高过载区和低过载区，超过高拥塞门限（参数值可设置）的就是高过载区，高拥塞门限和拥塞门限之间为低过载区。业务处理负荷进入过载区后，进入过负荷状态，需要启动过负荷控制功能来减少业务通过量。高优先级业务在系统的业务处理负荷达到高过载区时会被丢弃。 
缓冲区 
缓冲区是过载区和正常负荷区之间的区域，是低于拥塞门限（参数值可设置），且高于（拥塞门限-缓冲区大小）的区间。缓冲区是负荷控制的目标区域，不增加也不减少业务通过量，业务处理负荷保持稳定。 
在信令局向拥塞控制、按RNC局拥塞控制时，要么拥塞要么不拥塞，没有缓冲区，拥塞控制目标区域是临界拥塞。 
正常负荷区 
正常负荷区就是低于（拥塞门限-缓冲区大小）的区间。正常业务处理负荷，不需进行过负荷控制。如果是由于进行了控制导致业务处理负荷进入了正常负荷区，需要增加业务通过量，来增加业务处理负荷直到进入缓冲区。 
业务控制周期 
每个控制周期内允许N个业务通过，后续的业务被控制。N就是业务允许通过数。周期越短，控制越平滑，但是CPU资源消耗也相应增大。业务控制周期可以通过参数设置。 
评判周期 
调整业务允许通过数和二分法的low、high的周期。评判周期越短，收敛速度也就越快，但CPU资源消耗也相应增大。配置是业务控制周期的倍数。评判周期可以通过参数设置。 
Low和High通过数 
即在评判周期使用的最低和最高的业务通过数，如果之前尚未启动流量控制，则前一周期业务通过数作为二分法的high通过数，最低保证通过数作为low通过数。Low和high通过数在进行负荷控制过程中在每个评判周期由系统自己进行设置，不可调整。 
功能描述 
“过负荷基本参数配置”用于设置SGSN/MME网元的负荷控制算法参数和CPU拥塞控制的参数。 
本配置项的各项参数都是经过验证为最优的，不建议修改。 
相关主题 
 
设置过负荷基本参数(SET OVERLOAD BASIC PARA)
 
 
查询过负荷基本参数(SHOW OVERLOAD BASIC PARA)
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置过负荷基本参数(SET OVERLOAD BASIC PARA) 
##### 设置过负荷基本参数(SET OVERLOAD BASIC PARA) 
命令功能 
该命令用于设置过负荷基本参数。当需要更改过负荷控制基本参数时，如开启或关闭CPU拥塞控制、更新CPU拥塞门限、更新业务控制周期或评判周期、设置业务被过负荷控制后是否需要回拒绝响应等场景下，使用该命令。“业务控制周期”、“评判周期/业务控制周期”设置成功后，会影响过负荷控制算法的计算粒度。若“是否开启CPU拥塞控制”设置为“是”，则SGSN或MME网元会根据设置的参数计算CPU是否拥塞，并在CPU拥塞时会根据“拒绝/丢弃策略”来决定是丢弃收到的消息还是回拒绝响应。
注意事项 
 
该命令中业务控制周期、评判周期的配置影响所有过负荷控制功能；拒绝/丢弃策略及CPU拥塞门限的相关配置只影响CPU拥塞控制。
 
 
当CPU使用率超过配置的CPU拥塞门限时，被认为负荷过重。在配置CPU拥塞门限时，如果配置过小，会浪费CPU的处理能力，如果配置过大，会存在CPU冲高的隐患，不能起到保护系统的作用。
 
 
配置中各项参数的默认值为验证后最优配置，非特殊要求不建议修改。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
CTRLTIMER|业务控制周期(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于配置过负荷控制算法时计算业务通过数的周期（时间段），单位是100毫秒。
JUDGETIMER|评判周期/业务控制周期|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于配置评判周期时长，即CPU拥塞控制（包括链路、局向拥塞控制）时，动态调整当前允许通过业务数的频率。说明：评判周期配置采用的是业务控制周期的倍数，即100毫秒的倍数。
CPUENABLE|是否开启CPU拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否启用CPU拥塞控制，即系统CPU使用率超过CPU拥塞门限时，是否控制业务通过数。取值含义：否: 关闭CPU拥塞控制。是: 开启CPU拥塞控制。
REJECT|拒绝/丢弃策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于CPU拥塞控制时，业务被拒绝后，是否需要给对端回拒绝响应。取值含义：丢弃: 业务被控制后直接丢弃消息，不需要回拒绝响应消息。拒绝: 业务被拒绝后，需要给对端回拒绝响应消息。
WARNTHRESHOLD|CPU拥塞预警门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于配置CPU拥塞预警门限。当系统CPU使用率超过该配置值时，表示系统有拥塞的可能趋势。此时系统会上报告警，提示采取应对措施，如计划扩容。特别的，当配置为0时，表示不上报该级别告警。
EMWARNTHRESHOLD|CPU拥塞紧急预警门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于配置CPU拥塞紧急预警门限。当系统CPU使用率超过该配置值时，表示系统就快要发生拥塞。此时系统会上报告警，提示采取应对措施，如紧急扩容。特别的，当配置为0时，表示不上报该级别告警。
THRESHOLD|CPU拥塞门限|参数可选性:任选参数；参数类型:整数；参数范围为:1~99。|该参数用于配置CPU拥塞门限。当系统CPU使用率超过该配置值时，表示系统已经开始拥塞。
HTHRESHOLD|CPU高拥塞门限|参数可选性:任选参数；参数类型:整数；参数范围为:2~100。|该参数用于配置CPU高拥塞门限。当系统CPU使用率超过该配置值时，表示系统已经严重拥塞。说明：CPU高拥塞门限值需要大于 CPU拥塞门限值。
BUFFER|缓冲区大小|参数可选性:任选参数；参数类型:整数；参数范围为:1~99。|该参数用于配置CPU缓冲区大小。缓冲区表示系统CPU使用率将要达到CPU拥塞门限值之前的一段区域，此时表示系统达到CPU正常负荷区内的最优使用率。说明：缓冲区大小值需要小于等于CPU拥塞门限值。
BACKOFFTIMESTART|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最小值。当用户发起业务，MME判断CPU使用率过高进入过负荷状态而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”和“拒绝时携带的Back-off Timer最小取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
BACKOFFTIMEEND|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最大值。当用户发起业务，MME判断CPU使用率过高进入过负荷状态而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”和“拒绝时携带的Back-off Timer最小取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
LOWBACKOFFTIMESTART|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最小值。当低优先级接入用户发起业务，MME判断CPU使用率过高进入过负荷状态而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最小取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
LOWBACKOFFTIMEEND|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最大值。当低优先级接入用户发起业务，MME判断CPU使用率过高进入过负荷状态而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最小取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
LASTTIME|业务过负荷告警持续时间（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:1~3600。|业务过负荷告警持续时间（秒）
命令举例 
设置过负荷基本参数，设置业务控制周期为1秒，评判周期为5秒（5个业务控制周期），开启CPU拥塞控制，采用拒绝策略，设置CPU拥塞门限为CPU使用率超过75%，CPU高拥塞门限为CPU使用率超过85%，缓冲区大小为10，即CPU使用率在65%~75%之间为缓冲区。
SET OVERLOAD BASIC PARA:CTRLTIMER=10,JUDGETIMER=5,CPUENABLE="YES",REJECT="Refuse",THRESHOLD=75,HTHRESHOLD=85,BUFFER=10 
父主题： [过负荷基本参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询过负荷基本参数(SHOW OVERLOAD BASIC PARA) 
##### 查询过负荷基本参数(SHOW OVERLOAD BASIC PARA) 
命令功能 
该命令用于查询当前过负荷控制相关的基本参数配置。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CTRLTIMER|业务控制周期(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置过负荷控制算法时计算业务通过数的周期（时间段），单位是100毫秒。
JUDGETIMER|评判周期/业务控制周期|参数可选性:任选参数；参数类型:整数。|该参数用于配置评判周期时长，即CPU拥塞控制（包括链路、局向拥塞控制）时，动态调整当前允许通过业务数的频率。说明：评判周期配置采用的是业务控制周期的倍数，即100毫秒的倍数。
CPUENABLE|是否开启CPU拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否启用CPU拥塞控制，即系统CPU使用率超过CPU拥塞门限时，是否控制业务通过数。取值含义：否: 关闭CPU拥塞控制。是: 开启CPU拥塞控制。
REJECT|拒绝/丢弃策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于CPU拥塞控制时，业务被拒绝后，是否需要给对端回拒绝响应。取值含义：丢弃: 业务被控制后直接丢弃消息，不需要回拒绝响应消息。拒绝: 业务被拒绝后，需要给对端回拒绝响应消息。
WARNTHRESHOLD|CPU拥塞预警门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于配置CPU拥塞预警门限。当系统CPU使用率超过该配置值时，表示系统有拥塞的可能趋势。此时系统会上报告警，提示采取应对措施，如计划扩容。特别的，当配置为0时，表示不上报该级别告警。
EMWARNTHRESHOLD|CPU拥塞紧急预警门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于配置CPU拥塞紧急预警门限。当系统CPU使用率超过该配置值时，表示系统就快要发生拥塞。此时系统会上报告警，提示采取应对措施，如紧急扩容。特别的，当配置为0时，表示不上报该级别告警。
THRESHOLD|CPU拥塞门限|参数可选性:任选参数；参数类型:整数。|该参数用于配置CPU拥塞门限。当系统CPU使用率超过该配置值时，表示系统已经开始拥塞。
HTHRESHOLD|CPU高拥塞门限|参数可选性:任选参数；参数类型:整数。|该参数用于配置CPU高拥塞门限。当系统CPU使用率超过该配置值时，表示系统已经严重拥塞。说明：CPU高拥塞门限值需要大于 CPU拥塞门限值。
BUFFER|缓冲区大小|参数可选性:任选参数；参数类型:整数。|该参数用于配置CPU缓冲区大小。缓冲区表示系统CPU使用率将要达到CPU拥塞门限值之前的一段区域，此时表示系统达到CPU正常负荷区内的最优使用率。说明：缓冲区大小值需要小于等于CPU拥塞门限值。
BACKOFFTIMESTART|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最小值。当用户发起业务，MME判断CPU使用率过高进入过负荷状态而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”和“拒绝时携带的Back-off Timer最小取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
BACKOFFTIMEEND|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最大值。当用户发起业务，MME判断CPU使用率过高进入过负荷状态而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”和“拒绝时携带的Back-off Timer最小取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
LOWBACKOFFTIMESTART|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最小值。当低优先级接入用户发起业务，MME判断CPU使用率过高进入过负荷状态而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最小取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
LOWBACKOFFTIMEEND|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最大值。当低优先级接入用户发起业务，MME判断CPU使用率过高进入过负荷状态而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最小取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
LASTTIME|业务过负荷告警持续时间（秒）|参数可选性:任选参数；参数类型:整数。|业务过负荷告警持续时间（秒）
命令举例 
查询过负荷基本参数配置。
SHOW OVERLOAD BASIC PARA 
`
(No.24) : SHOW OVERLOAD BASIC PARA
-----------------uMAC_MME_Combo_B5/NFS_MMESGSN_0----------------
操作维护       业务控制周期(100ms) 评判周期/业务控制周期 是否开启CPU拥塞控制 拒绝/丢弃策略 CPU拥塞预警门限 CPU拥塞紧急预警门限 CPU拥塞门限 CPU高拥塞门限 缓冲区大小 拒绝时携带的Back-off Timer最小取值（秒） 拒绝时携带的Back-off Timer最大取值（秒） 低优先级拒绝时携带的Back-off Timer最小取值（秒） 低优先级拒绝时携带的Back-off Timer最大取值（秒） 业务过负荷告警持续时间（秒） 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           10                  5                     是                  丢弃          0               0                   80          90            5          0                                        0                                        0                                                0                                                300                          
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-06 20:31:13 耗时: 1.652秒。
` 
父主题： [过负荷基本参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### SGSN过负荷参数配置 
#### SGSN过负荷参数配置 
背景知识 
根据协议3GPP TS 25.413的描述, SGSN在过负荷情况下，会向RNC发送Overload消息，通知RNC，本网元拥塞。 
功能描述 
“SGSN过负荷参数配置” 用于设置SGSN向RNC发送Overload消息的相关参数。 
修改参数，会影响SGSN网元向RNC发送Overload消息及根据Overload消息对Iu口下行业务进行控制的策略。 
相关主题 
 
设置SGSN通用过负荷参数(SET OVERLOAD PARA)
 
 
查询SGSN通用过负荷参数(SHOW OVERLOAD PARA)
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置SGSN通用过负荷参数(SET OVERLOAD PARA) 
##### 设置SGSN通用过负荷参数(SET OVERLOAD PARA) 
命令功能 
该命令用于设置SGSN网元的通用过负荷参数。当需要更改SGSN网元的过负荷参数时，如开启或关闭信令局向及窄带信令链路的拥塞控制、更新默认ERL拥塞门限及缓冲区大小、更新overload消息相关参数等场景下，使用该命令，其影响如下： 
 
拥塞控制开关相关参数设置成功后，会影响SGSN业务接口拥塞时，接收和发送报文的控制策略；
 
 
ERL相关参数设置成功后，会影响SGSN对窄带信令链路是否拥塞的判断。
 
 
overload相关参数设置成功后，会影响SGSN网元向RNC发送overlaod消息及根据overload消息对Iu口下行业务进行控制的策略。
 
 
ERL拥塞门限及缓冲区大小的配置也可以在“特定信令链路拥塞参数配置”中针对指定链路进行配置。 
注意事项 
 
该命令中除了“默认ERL拥塞”和“默认ERL门限缓冲区大小”配置外，其它配置对SGSN网元所有对应类型的信令局向生效。
 
 
“默认ERL拥塞门限”和“默认ERL缓冲区大小”的配置，对于未在“SGSN特定信令链路拥塞控制参数配置”中进行特定配置的信令链路生效。特定信令链路拥塞控制配置命令参见 ADD SGSN LINK OVERLOAD CONTROL PARA。
 
 
该命令中的参数建议采用默认配置，非特殊要求无需修改。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
OLSLOWLEVEL|开始发送overload时的最小拥塞级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置SGSN网元往RNC发送overload消息的最小拥塞级别，表示当SGSN处于何种拥塞程度才进行overload消息的发送。取值含义：低过载: SGSN处于低过载（CPU达到了低过载门限，但没有达到高过载门限）时就可以发送overload消息。高过载: SGSN处于高过载（CPU达到了高过载门限）时就可以发送overload消息。不发送: SGSN不主动发送overload消息。
OLSINTERVAL|每发送overload到RNC的报文间隔|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置当RNC拥塞时，每次累计收到该RNC的多少个报文后再发送一次overload消息到RNC，若无特殊要求，建议采用默认值。
OLIUDNCTRL|是否根据overload消息控制Iu口下行业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据RNC网元拥塞情况进行Iu口下行出向业务（寻呼、切换、短消息）的控制。
命令举例 
该命令用于设置SGSN通用过负荷参数配置，窄带信令链路开启拥塞控制，并且默认ERL拥塞门限为80%，默认ERL缓冲区配置为10，即ERL百分比在70%~80%之间为缓冲区。开始发送overload到RNC时的最小拥塞级别为高拥塞，发送overload到RNC的报文间隔是收到300个报文，并且开启根据overload消息控制Iu口下行业务。
SET OVERLOAD PARA:NO7CTRL="YES",ERL=80,BUFFER=10,OLSLOWLEVEL="Severely",OLSINTERVAL=300,OLIUDNCTRL="YES"; 
父主题： [SGSN过负荷参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询SGSN通用过负荷参数(SHOW OVERLOAD PARA) 
##### 查询SGSN通用过负荷参数(SHOW OVERLOAD PARA) 
命令功能 
该命令用于查询SGSN网元的通用过负荷参数。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OLSLOWLEVEL|开始发送overload时的最小拥塞级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置SGSN网元往RNC发送overload消息的最小拥塞级别，表示当SGSN处于何种拥塞程度才进行overload消息的发送。取值含义：低过载: SGSN处于低过载（CPU达到了低过载门限，但没有达到高过载门限）时就可以发送overload消息。高过载: SGSN处于高过载（CPU达到了高过载门限）时就可以发送overload消息。不发送: SGSN不主动发送overload消息。
OLSINTERVAL|每发送overload到RNC的报文间隔|参数可选性:任选参数；参数类型:整数。|该参数用于配置当RNC拥塞时，每次累计收到该RNC的多少个报文后再发送一次overload消息到RNC，若无特殊要求，建议采用默认值。
OLIUDNCTRL|是否根据overload消息控制Iu口下行业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否根据RNC网元拥塞情况进行Iu口下行出向业务（寻呼、切换、短消息）的控制。
命令举例 
该命令用于查询SGSN通用过负荷参数配置。
SHOW OVERLOAD PARA; 
`
命令 (No.1): SHOW OVERLOAD PARA
操作维护  窄带信令链路拥塞控制   默认ERL拥塞门限   默认ERL缓冲区大小   开始发送overload时的最小拥塞级别   每发送overload到RNC的报文间隔   是否根据overload消息控制Iu口下行业务
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      是                     80                10                  高过载                             300                             是
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [SGSN过负荷参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### MME过负荷参数配置 
#### MME过负荷参数配置 
背景知识 
按照协议3GPP TS 36.413, MME在拥塞情况下可以向eNodeB发送overload start消息，通知eNode减少向本MME发起业务；当MME解除拥塞，需要向已经发送overload start消息的eNodeB发送overload stop消息，通知eNodeB恢复正常业务。 
功能描述 
“MME过负荷参数配置”用于设置S1接口发送overload start消息的策略。 
本配置有默认值，建议用户采用默认配置。 
相关主题 
 
设置MME过负荷参数(SET MME OVERLOAD PARA)
 
 
查询MME过负荷参数(SHOW MME OVERLOAD PARA)
 
 
到GW的过负荷配置
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置MME过负荷参数(SET MME OVERLOAD PARA) 
##### 设置MME过负荷参数(SET MME OVERLOAD PARA) 
命令功能 
该命令用于设置MME网元的过负荷参数。当需要更改MME网元的过负荷参数时，例如更改更改S1口发送overload消息相关参数时，使用该命令。overload消息相关参数设置成功后，会影响MME网元S1口发送overload start消息的策略，及消息中Overload Action信元的设置。
注意事项 
 
overload消息发送相关参数的配置只对MME网元的S1口生效，并且在设置”S1口发送overload start的策略“为不发送时，“发送overload start的CPU低门限（%）”、“发送overload start的CPU高门限（%）”、“发送overload start的NAS信令速率低门限”、“发送overload start的NAS信令速率高门限”、“超过门限后，发送overload start消息的延时（秒）”、“低于门限后，发送overload stop/start消息的延时（秒）”、”低门限Overload Start消息中的Overload Action信元设置“、”高门限Overload Start消息中的Overload Action信元设置“、”低门限Traffic Load Reduction Indication信元设置“、“高门限Traffic Load Reduction Indication信元设置”、”发送overload start的eNodeB个数“等不生效。
 
 
该命令中的参数建议采用默认配置，非特殊要求无需修改。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
S1OLCTRL|S1口发送Overload Start的策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME网元S1口往eNodeB发送overload start消息的策略。取值含义：不发送: MME不主动发送overload start消息根据CPU负荷发送: MME根据CPU负荷发送overload start消息根据NAS信令速率发送: MME根据NAS信令速率发送overload start消息
CPULOWTHD|发送Overload Start的CPU低门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”时，当MME的CPU负荷超过该参数，MME则通过S1口往eNodeB发送overload start消息，overload start消息中“Overload Action信元”为配置的“低门限Overload Start消息中的Overload Action信元设置”，消息中“Traffic Load Reduction Indication信元”为配置的“低门限Traffic Load Reduction Indication信元设置”。
CPUHIGHTHD|发送Overload Start的CPU高门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”时，当MME的CPU负荷超过该参数，MME则通过S1口往eNodeB发送overload start消息，overload start消息中“Overload Action信元”为配置的“高门限Overload Start消息中的Overload Action信元设置”，消息中“Traffic Load Reduction Indication信元”为配置的“高门限Traffic Load Reduction Indication信元设置”。
NASLOWTHD|发送Overload Start的NAS信令速率低门限|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|该参数仅在“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”时，当MME接收的NAS信令速率超过该参数，MME则通过S1口往eNodeB发送overload start消息，overload start消息中“Overload Action信元”为配置的“低门限Overload Start消息中的Overload Action信元设置”，消息中“Traffic Load Reduction Indication信元”为配置的“低门限Traffic Load Reduction Indication信元设置”。
NASHIGHTHD|发送Overload Start的NAS信令速率高门限|参数可选性:任选参数；参数类型:整数；参数范围为:2~4294967295。|该参数仅在“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”时，当MME接收的NAS信令速率超过该参数，MME则通过S1口往eNodeB发送overload start消息，overload start消息中“Overload Action信元”为配置的“高门限Overload Start消息中的Overload Action信元设置”，消息中“Traffic Load Reduction Indication信元”为配置的“高门限Traffic Load Reduction Indication信元设置”。
OLSTARTDELAY|超过门限后，发送Overload Start消息的延时（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置当MME负荷高于门限时，发送overload start消息的延时时间。该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”，当MME的CPU负荷超过“发送Overload Start的CPU低门限（%）”或者“发送Overload Start的CPU高门限（%）”时，MME支持延时发送overload start消息。如果“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”，当MME接收的NAS信令速率超过“发送Overload Start的NAS信令速率低门限”或者“发送Overload Start的NAS信令速率高门限”时，MME支持延时发送overload start消息。
OLSTOPDELAY|低于门限后，发送Overload Stop/Start消息的延时（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置当MME负荷低于门限时，发送overload start或overload stop消息的延时时间。它仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”，当MME的CPU负荷低于“发送Overload Start的CPU低门限（%）”时，MME支持延时发送overload stop消息；当MME的CPU负荷低于“发送Overload Start的CPU高门限（%）”时，MME支持延时发送overload start消息。如果“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”，当MME接收的NAS信令速率超过“发送Overload Start的NAS信令速率低门限”时，MME支持延时发送overload stop消息；当MME接收的NAS信令速率低于“发送Overload Start的NAS信令速率高门限”时，MME支持延时发送overload start消息。
LOWTHDACT|低门限Overload Start消息中的Overload Action信元设置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于设置在MME负荷超过低门限情况下，MME发送overload start消息时，消息中Overload Action IE所携带的值。取值含义：拒绝非紧急情况终端发起数据传输的所有RRC连接建立拒绝信令传输的所有RRC连接建立仅允许紧急对话和移动被叫业务仅允许高优先级会话和移动被叫业务拒绝时延不敏感的访问仅允许高优先级会话、异常报告和移动被叫业务不接受来自CP CIoT的移动数据或时延不敏感访问说明：MME发给eNodeB的overload start消息中携带该参数，由eNodeB使用。RRC连接是为了建立UE和UTRAN之间的信令连接，由UE请求启动，为UE建立最初的信令连接。
HIGHTHDACT|高门限Overload Start消息中的Overload Action信元设置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于设置在MME负荷超过高门限情况下，MME发送overload start消息时，消息中Overload Action IE所携带的值。取值含义：拒绝非紧急情况终端发起数据传输的所有RRC连接建立拒绝信令传输的所有RRC连接建立仅允许紧急对话和移动被叫业务仅允许高优先级会话和移动被叫业务拒绝时延不敏感的访问仅允许高优先级会话、异常报告和移动被叫业务不接受来自CP CIoT的移动数据或时延不敏感访问说明：MME发给eNodeB的overload start消息中携带该参数，由eNodeB使用。RRC连接是为了建立UE和UTRAN之间的信令连接，由UE请求启动，为UE建立最初的信令连接。
LOWTHDTLRI|低门限Traffic Load Reduction Indication信元设置|参数可选性:任选参数；参数类型:整数；参数范围为:1~99。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于设置当MME负荷超过低门限情况下，MME发送overload start消息时，消息中Traffic Load Reduction Indication IE所携带的值。
HIGHTHDTLRI|高门限Traffic Load Reduction Indication信元设置|参数可选性:任选参数；参数类型:整数；参数范围为:1~99。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于设置当MME负荷超过高门限情况下，MME发送overload start消息时，消息中Traffic Load Reduction Indication IE所携带的值。
S1OLENBNUM|发送Overload Start的eNodeB个数|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于配置MME网元支持的已发送overload start消息，但未发送overload stop消息的最大eNodeB的个数。
命令举例 
该命令用于设置MME过负荷参数，S1口发送Overload Start的策略为"不发送"。
SET MME OVERLOAD PARA:S1OLCTRL="NOSEND"; 
父主题： [MME过负荷参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询MME过负荷参数(SHOW MME OVERLOAD PARA) 
##### 查询MME过负荷参数(SHOW MME OVERLOAD PARA) 
命令功能 
该命令用于查询MME网元当前过负荷参数的配置信息。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
S1OLCTRL|S1口发送Overload Start的策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME网元S1口往eNodeB发送overload start消息的策略。取值含义：不发送: MME不主动发送overload start消息根据CPU负荷发送: MME根据CPU负荷发送overload start消息根据NAS信令速率发送: MME根据NAS信令速率发送overload start消息
CPULOWTHD|发送Overload Start的CPU低门限（%）|参数可选性:任选参数；参数类型:整数。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”时，当MME的CPU负荷超过该参数，MME则通过S1口往eNodeB发送overload start消息，overload start消息中“Overload Action信元”为配置的“低门限Overload Start消息中的Overload Action信元设置”，消息中“Traffic Load Reduction Indication信元”为配置的“低门限Traffic Load Reduction Indication信元设置”。
CPUHIGHTHD|发送Overload Start的CPU高门限（%）|参数可选性:任选参数；参数类型:整数。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”时，当MME的CPU负荷超过该参数，MME则通过S1口往eNodeB发送overload start消息，overload start消息中“Overload Action信元”为配置的“高门限Overload Start消息中的Overload Action信元设置”，消息中“Traffic Load Reduction Indication信元”为配置的“高门限Traffic Load Reduction Indication信元设置”。
NASLOWTHD|发送Overload Start的NAS信令速率低门限|参数可选性:任选参数；参数类型:整数。|该参数仅在“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”时，当MME接收的NAS信令速率超过该参数，MME则通过S1口往eNodeB发送overload start消息，overload start消息中“Overload Action信元”为配置的“低门限Overload Start消息中的Overload Action信元设置”，消息中“Traffic Load Reduction Indication信元”为配置的“低门限Traffic Load Reduction Indication信元设置”。
NASHIGHTHD|发送Overload Start的NAS信令速率高门限|参数可选性:任选参数；参数类型:整数。|该参数仅在“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”时，当MME接收的NAS信令速率超过该参数，MME则通过S1口往eNodeB发送overload start消息，overload start消息中“Overload Action信元”为配置的“高门限Overload Start消息中的Overload Action信元设置”，消息中“Traffic Load Reduction Indication信元”为配置的“高门限Traffic Load Reduction Indication信元设置”。
OLSTARTDELAY|超过门限后，发送Overload Start消息的延时（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于配置当MME负荷高于门限时，发送overload start消息的延时时间。该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”，当MME的CPU负荷超过“发送Overload Start的CPU低门限（%）”或者“发送Overload Start的CPU高门限（%）”时，MME支持延时发送overload start消息。如果“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”，当MME接收的NAS信令速率超过“发送Overload Start的NAS信令速率低门限”或者“发送Overload Start的NAS信令速率高门限”时，MME支持延时发送overload start消息。
OLSTOPDELAY|低于门限后，发送Overload Stop/Start消息的延时（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于配置当MME负荷低于门限时，发送overload start或overload stop消息的延时时间。它仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。如果“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”，当MME的CPU负荷低于“发送Overload Start的CPU低门限（%）”时，MME支持延时发送overload stop消息；当MME的CPU负荷低于“发送Overload Start的CPU高门限（%）”时，MME支持延时发送overload start消息。如果“S1口发送Overload Start的策略”配置为“根据NAS信令速率发送”，当MME接收的NAS信令速率超过“发送Overload Start的NAS信令速率低门限”时，MME支持延时发送overload stop消息；当MME接收的NAS信令速率低于“发送Overload Start的NAS信令速率高门限”时，MME支持延时发送overload start消息。
LOWTHDACT|低门限Overload Start消息中的Overload Action信元设置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于设置在MME负荷超过低门限情况下，MME发送overload start消息时，消息中Overload Action IE所携带的值。取值含义：拒绝非紧急情况终端发起数据传输的所有RRC连接建立拒绝信令传输的所有RRC连接建立仅允许紧急对话和移动被叫业务仅允许高优先级会话和移动被叫业务拒绝时延不敏感的访问仅允许高优先级会话、异常报告和移动被叫业务不接受来自CP CIoT的移动数据或时延不敏感访问说明：MME发给eNodeB的overload start消息中携带该参数，由eNodeB使用。RRC连接是为了建立UE和UTRAN之间的信令连接，由UE请求启动，为UE建立最初的信令连接。
HIGHTHDACT|高门限Overload Start消息中的Overload Action信元设置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于设置在MME负荷超过高门限情况下，MME发送overload start消息时，消息中Overload Action IE所携带的值。取值含义：拒绝非紧急情况终端发起数据传输的所有RRC连接建立拒绝信令传输的所有RRC连接建立仅允许紧急对话和移动被叫业务仅允许高优先级会话和移动被叫业务拒绝时延不敏感的访问仅允许高优先级会话、异常报告和移动被叫业务不接受来自CP CIoT的移动数据或时延不敏感访问说明：MME发给eNodeB的overload start消息中携带该参数，由eNodeB使用。RRC连接是为了建立UE和UTRAN之间的信令连接，由UE请求启动，为UE建立最初的信令连接。
LOWTHDTLRI|低门限Traffic Load Reduction Indication信元设置|参数可选性:任选参数；参数类型:整数。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于设置当MME负荷超过低门限情况下，MME发送overload start消息时，消息中Traffic Load Reduction Indication IE所携带的值。
HIGHTHDTLRI|高门限Traffic Load Reduction Indication信元设置|参数可选性:任选参数；参数类型:整数。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于设置当MME负荷超过高门限情况下，MME发送overload start消息时，消息中Traffic Load Reduction Indication IE所携带的值。
S1OLENBNUM|发送Overload Start的eNodeB个数|参数可选性:任选参数；参数类型:整数。|该参数仅在“S1口发送Overload Start的策略”配置为“根据CPU负荷发送”或“根据NAS信令速率发送”时有效。该参数用于配置MME网元支持的已发送overload start消息，但未发送overload stop消息的最大eNodeB的个数。
命令举例 
该命令用于查询MME过负荷参数配置。
SHOW MME OVERLOAD PARA; 
`
(No.1) : SHOW MME OVERLOAD PARA:
-----------------NFS_MMESGSN_0----------------
操作维护       Sending Overload Start on S1 The Low Cpu Load Threshold of Sending Overload Start Msg(%) The High Cpu Load Threshold of Sending Overload Start Msg(%) The Low NAS Signalling Rate Threshold of Sending Overload Start Msg The High NAS Signalling Rate Threshold of Sending Overload Start Msg The Delay Time of Sending Overload Start Msg After Load Reach Threshold(seconds) The Delay Time of Sending Overload Stop/Start Msg After Load Under Threshold(seconds) Overload Action Value in Overload Start Msg for Low Threshold Overload Action Value in Overload Start Msg for High Threshold Traffic Load Reduction Indication Value for Low Threshold Traffic Load Reduction Indication Value for High Threshold Number of EnodeB for Sending Overload Start Msg 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           No Sending                   60                                                          70                                                           2147483648                                                           4294967295                                                            0                                                                                30                                                                              Reject RRC connection establishments for non-emergency MO DT  Reject RRC connection establishments for Signalling            1                                                         1                                                          128                                             
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功 耗时: 0.325 秒
` 
父主题： [MME过负荷参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 到GW的过负荷配置 
##### 到GW的过负荷配置 
背景知识 
MME支持S11接口的DDN Throttling。 
当MME业务量超过拥塞阈值时，MME在发给PGW的消息中携带OCI信元，通知PGW减少消息发送量。 
MME收到SGW和PGW的过载信息OCI后，有业务请求时(PDN创建、承载创建、其他业务上报等)，MME根据OCI要求的比例来减少选择拥塞SAE GW的次数，减少发送给SAE GW的请求消息数。 
功能描述 
在SGSN/MME网元处理的消息中，有一部分是与签约用户无关的管理类消息和中继消息，其中有些消息可能引起网元负荷冲高，因而需要加以负荷控制，每秒超过此门限的报文将要被丢弃。 
相关主题 
 
设置到GW的过负荷(SET MME OVERLOAD INFO TO GW)
 
 
查询到GW的过负荷(SHOW MME OVERLOAD INFO TO GW)
 
 
设置到GW的过负荷门限(SET MME OVERLOAD THRESHOLD INFO TO GW)
 
 
查询到GW的过负荷门限(SHOW MME OVERLOAD THRESHOLD INFO TO GW)
 
 
父主题： [MME过负荷参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置到GW的过负荷(SET MME OVERLOAD INFO TO GW) 
###### 设置到GW的过负荷(SET MME OVERLOAD INFO TO GW) 
命令功能 
该命令用于修改MME到SGW/PGW的过负荷配置信息，包括发送过负荷信息的CPU门限和过负荷信息发送周期。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
THRESHOLD|发送过负荷信息的CPU门限|参数可选性:任选参数；参数类型:整数；参数范围为:50~99。|MME开始发送过负荷信息的CPU门限。当MME检测到CPU达到配置门限后，即开始向SGW/PGW发送相应的过负荷信息。
PERIOD|过负荷信息发送周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~86400。|MME发送过负荷信息的周期。当MME始终处于过负荷时，需要周期性的发送过负荷信息。每次发送的过负荷信息的有效期与发送周期一致。
TOPGW|向PGW发送过负荷信息的控制开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME通过SGW向PGW发送过负荷信息的控制开关，可控制是否只向MME归属PLMN的PGW发送过负荷信息。该参数取值含义如下：不发送：不向任何PGW发送MME的过负荷信息。只有本PLMN的PGW发送：只向MME归属PLMN的PGW发送MME的过负荷信息。都发送：向MME归属PLMN的PGW和非MME归属PLMN的PGW都发送MME的过负荷信息。
GWOLIALG|过负荷控制信息参数生成方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME向PGW发送的过负荷信息参数生成方式，有固定算法和使用配置两种方式。当选择固定算法时，缩减比例通过如下公式获得：CPU小于50%，缩减比例为0；CPU在50%～60%之间，缩减比例=(5+0.5×(CPU-50))%；CPU在60%～70%之间，缩减比例=(10+1×(CPU-60))%；CPU在70%～90%之间，缩减比例=(20+4×(CPU-70))%；当选择使用配置时，参数由SET MME OVERLOAD THRESHOLD INFO TO GW配置。
命令举例 
修改MME到SGW/PGW的过负荷信息，其中发送过负荷信息的CPU门限为70、过负荷信息发送周期为600秒，过负荷控制信息参数生成方式为固定算法。 
SET MME OVERLOAD INFO TO GW:THRESHOLD=70,PERIOD=600,TOPGW="ALL",GWOLIALG="FIXEDALGORITHM" 
父主题： [到GW的过负荷配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询到GW的过负荷(SHOW MME OVERLOAD INFO TO GW) 
###### 查询到GW的过负荷(SHOW MME OVERLOAD INFO TO GW) 
命令功能 
该命令用于查询MME到SGW/PGW的过负荷配置信息。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
THRESHOLD|发送过负荷信息的CPU门限|参数可选性:任选参数；参数类型:整数。|MME开始发送过负荷信息的CPU门限。当MME检测到CPU达到配置门限后，即开始向SGW/PGW发送相应的过负荷信息。
PERIOD|过负荷信息发送周期(秒)|参数可选性:任选参数；参数类型:整数。|MME发送过负荷信息的周期。当MME始终处于过负荷时，需要周期性的发送过负荷信息。每次发送的过负荷信息的有效期与发送周期一致。
TOPGW|向PGW发送过负荷信息的控制开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|MME通过SGW向PGW发送过负荷信息的控制开关，可控制是否只向MME归属PLMN的PGW发送过负荷信息。该参数取值含义如下：不发送：不向任何PGW发送MME的过负荷信息。只有本PLMN的PGW发送：只向MME归属PLMN的PGW发送MME的过负荷信息。都发送：向MME归属PLMN的PGW和非MME归属PLMN的PGW都发送MME的过负荷信息。
GWOLIALG|过负荷控制信息参数生成方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME向PGW发送的过负荷信息参数生成方式，有固定算法和使用配置两种方式。当选择固定算法时，缩减比例通过如下公式获得：CPU小于50%，缩减比例为0；CPU在50%～60%之间，缩减比例=(5+0.5×(CPU-50))%；CPU在60%～70%之间，缩减比例=(10+1×(CPU-60))%；CPU在70%～90%之间，缩减比例=(20+4×(CPU-70))%；当选择使用配置时，参数由SET MME OVERLOAD THRESHOLD INFO TO GW配置。
命令举例 
查询MME到SGW/PGW的过负荷配置信息。 
SHOW MME OVERLOAD INFO TO GW 
`
命令 (No.4): SHOW MME OVERLOAD INFO TO GW
操作维护  发送过负荷信息的CPU门限   过负荷信息发送周期(秒)   向PGW发送过负荷信息的控制开关   过负荷控制信息参数生成方式
------------------------------------------------------------------------------------------------------------------------
修改      70                        600                      都发送                          固定算法
------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.033 秒）。
` 
父主题： [到GW的过负荷配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置到GW的过负荷门限(SET MME OVERLOAD THRESHOLD INFO TO GW) 
###### 设置到GW的过负荷门限(SET MME OVERLOAD THRESHOLD INFO TO GW) 
命令功能 
该命令用于修改到GW的过负荷门限。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
THRESHOLD|MME当前CPU负荷|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数仅在“过负荷控制信息参数生成方式”配置为“使用配置”时有效。本参数用来配置MME当前CPU负荷，分成以下几个等级：40~49（THRESHOLD_0）50~59（THRESHOLD_1）60~69（THRESHOLD_2）70~79（THRESHOLD_3）80~89（THRESHOLD_4）90~100（THRESHOLD_5）每个等级都有对应的“业务缩减比例(%)”和“业务缩减时长(秒)”配置。
METRIC|业务缩减比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数仅在“过负荷控制信息参数生成方式”配置为“使用配置”时有效，用来配置固定的业务缩减比例（%）。
PERIOD|业务缩减时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~86400。|该参数仅在“过负荷控制信息参数生成方式”配置为“使用配置”时有效，用来配置固定的业务缩减时长。
命令举例 
设置到GW的过负荷门限。 
SET MME OVERLOAD THRESHOLD INFO TO GW:THRESHOLD="THRESHOLD_0",METRIC=0,PERIOD =600 
父主题： [到GW的过负荷配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询到GW的过负荷门限(SHOW MME OVERLOAD THRESHOLD INFO TO GW) 
###### 查询到GW的过负荷门限(SHOW MME OVERLOAD THRESHOLD INFO TO GW) 
命令功能 
该命令用于查询到GW的过负荷门限。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
THRESHOLD|MME当前CPU负荷|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数仅在“过负荷控制信息参数生成方式”配置为“使用配置”时有效。本参数用来配置MME当前CPU负荷，分成以下几个等级：40~49（THRESHOLD_0）50~59（THRESHOLD_1）60~69（THRESHOLD_2）70~79（THRESHOLD_3）80~89（THRESHOLD_4）90~100（THRESHOLD_5）每个等级都有对应的“业务缩减比例(%)”和“业务缩减时长(秒)”配置。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
THRESHOLD|MME当前CPU负荷|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数仅在“过负荷控制信息参数生成方式”配置为“使用配置”时有效。本参数用来配置MME当前CPU负荷，分成以下几个等级：40~49（THRESHOLD_0）50~59（THRESHOLD_1）60~69（THRESHOLD_2）70~79（THRESHOLD_3）80~89（THRESHOLD_4）90~100（THRESHOLD_5）每个等级都有对应的“业务缩减比例(%)”和“业务缩减时长(秒)”配置。
METRIC|业务缩减比例(%)|参数可选性:任选参数；参数类型:整数。|该参数仅在“过负荷控制信息参数生成方式”配置为“使用配置”时有效，用来配置固定的业务缩减比例（%）。
PERIOD|业务缩减时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数仅在“过负荷控制信息参数生成方式”配置为“使用配置”时有效，用来配置固定的业务缩减时长。
命令举例 
查询到GW的过负荷门限。 
SHOW MME OVERLOAD THRESHOLD INFO TO GW; 
`
命令 (No.1): SHOW MME OVERLOAD THRESHOLD INFO TO GW:THRESHOLD="THRESHOLD_0";
操作维护	MME当前CPU负荷	业务缩减比例(%)	业务缩减时长(秒)	
-------------------------------------------------------------
修改 		40～49			10				600	
-------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.05 秒）。
` 
父主题： [到GW的过负荷配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### SGSN业务控制配置 
#### SGSN业务控制配置 
背景知识 
SGSN支持限制对端到本端的入向业务量，来控制自身的业务负荷；也支持限制本端到HLR、SMC的出向业务量，来控制对方的业务负荷。 
功能描述 
“SGSN业务控制配置”用于过负荷控制时，配置业务相关的参数。可以配置SGSN的入向、出向业务控制门限，高优先级业务类型，CPU拥塞控制业务保证通过数。 
相关主题 
 
SGSN通用业务控制配置
 
 
SGSN特定局向业务控制配置
 
 
SGSN自动业务控制策略配置
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### SGSN通用业务控制配置 
##### SGSN通用业务控制配置 
背景知识 
SGSN支持限制对端到本端的入向业务量，来控制自身的业务负荷，也支持限制本端到HLR、SMC的出向业务量，来控制对方的业务负荷。 
功能描述 
“SGSN通用业务控制配置”用于过负荷控制时，配置业务相关的通用参数。主要包括以下内容： 
 
配置哪些业务是高优先级业务，对于高优先级业务，仅在CPU处于高过载区时才进行控制。非高优先级业务只要在CPU拥塞时（高过载、或低过载、或非过载区但拥塞）时都会被控制。
 
 
配置MP实例保证每秒通过业务数，即MP CPU在拥塞情况下，每个MP实例保证通过一部分业务，目的是在拥塞时对业务进行“泄洪”。
 
 
配置MP实例每秒通过附着业务个数、MP实例每秒通过业务请求业务个数、MP实例每秒通过路由区更新业务个数、MP实例每秒通过切换业务个数、MP实例每秒通过激活业务个数和MP实例每秒通过短消息业务个数，用于入向业务单项控制。配置后，单位时间内，MP实例单项业务数量不能超过配置的该单项业务最大数。
 
 
配置各单项业务的权重和配置MP实例每秒通过业务最大个数，用于入向业务总量控制，各个单项业务每秒通过业务个数×业务权重之和，不能超过MP实例每秒通过业务最大个数。
 
 
                        配置MP实例默认每秒到HLR/SMC局向的最大业务，用于出向业务控制，针对HLR/SMC局向进行业务控制，保护对方网元。如果需要针对特定的HLR/SMC进行控制，可以通过
                        ADD SGSN OFFICE SERVICE MAXIMUM
                        命令配置。
                    
 
 
                        入向业务控制和出向业务控制，优先级高于CPU拥塞控制（CPU拥塞控制命令：
                        SET OVERLOAD BASIC PARA
                        ），配置入向、出向业务控制可以快速地降低系统负荷，设置的门限值需要根据实际话务模型设定(默认不控制)。
                    
 
 
相关主题 
 
设置通用业务控制(SET SERVICE CONTROL)
 
 
查询通用业务控制(SHOW SERVICE CONTROL)
 
 
父主题： [SGSN业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置通用业务控制(SET SERVICE CONTROL) 
###### 设置通用业务控制(SET SERVICE CONTROL) 
命令功能 
该命令用于设置SGSN网元过负荷控制相关的通用业务控制参数。当需要更改SGSN网元过负荷控制相关的通用业务控制参数时，如高优先业务配置、保证业务通过数配置、允许通过业务数配置、业务权重配置、入向业务控制对应的拒绝/丢弃策略、到HLR的鉴权及位置更新最大数目、到SMC的短消息最大数目等场景下，使用该命令。SGSN通用业务控制参数设置成功后，可以调整SGSN网元过负荷控制相关的通用业务控制参数。 
到HLR的鉴权及位置更新最大数目、到SMC的短消息最大数目也可以针对局向ID进行特定配置。 
注意事项 
 
该命令中拒绝/丢弃策略只对SGSN业务相关的入向业务控制有效。CPU拥塞控制也有对应的拒绝/丢弃策略，可以通过过负荷基本参数配置来设置，配置命令为： SET OVERLOAD BASIC PARA：REJECT="Discard";
 
 
高优先业务及每秒保证通过数配置只对CPU拥塞控制生效
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
HPRISVRI|高优先级业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置SGSN高优先级业务，高优先业务只在CPU高过载时才会控制，非高优先级业务只要在CPU拥塞时（高过载、或低过载、或非过载区但拥塞）时都会被控制。取值含义：附着(ATTACH)：Attach Request消息业务请求(SVRREQ)：Service Request消息PDP上下文激活(PDPACT)：Active PDP Context Request消息PDP上下文修改(PDPMOD)：Modify PDP Context Request消息短消息(SMS)：触发短消息流程的第一条CP-DATA消息寻呼(PAGING)：用户面触发的寻呼或CS寻呼流程的Paging Request消息路由区更新(RAU)：Routing Area Update Request消息切换(HO)：Handover Required消息Null(NULL)：不设置任何业务为高优先级说明：当不选择NULL时，业务可以选择多个，选择NULL时，不能选择任何业务。
ATTNUMG|附着|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置SGSN保证每秒通过的附着业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Attach Request消息数。说明：此处设置的个数针对单个MP实例。
SVRREQNUMG|业务请求|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置SGSN保证每秒通过的业务请求业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要说明：此处设置的个数针对单个MP实例。
PDPACTNUMG|PDP上下文激活|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置SGSN保证每秒通过的PDP上下文激活业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Active PDP Context Request消息数。说明：此处设置的个数针对单个MP实例。
PDPMODNUMG|PDP上下文修改|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置SGSN保证每秒通过的PDP上下文修改业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Modify PDP Context Request消息数。说明：此处设置的个数针对单个MP实例。
SMSNUMG|短消息|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置SGSN保证每秒通过的短消息业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的触发短消息流程的第一条CP-DATA消息数。说明：此处设置的个数针对单个MP实例。
PAGENUMG|寻呼|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置SGSN保证每秒通过的寻呼（包括用户面触发的寻呼和CS寻呼）业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Paging Request消息数。说明：此处设置的个数针对单个MP实例。
RUNUMG|路由区更新|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置SGSN保证每秒通过的路由区更新业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Routing Area Update Request消息数。说明：此处设置的个数针对单个MP实例。
HONUMG|切换|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置SGSN保证每秒通过的切换业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Handover Required消息数。说明：此处设置的个数针对单个MP实例。
SERVICENUMG|每实例每秒保证通过业务数|参数可选性:任选参数；参数类型:复合参数|该参数是以上ATTNUMG、SVRREQNUMG、PDPACTNUMG、PDPMODNUMG、SMSNUMG、PAGENUMG、RUNUMG、HONUMG各个参数的组合。用于设置SGSN保证每秒通过的各项业务数。
ATTNUM|每实例每秒通过附着业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的附着业务数，即每秒钟允许通过的Attach Request消息数。说明：此处设置的个数针对单个MP实例。
ATTWGT|附着业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置SGSN附着业务权重，即一个Attach Request消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
SVRREQNUM|每实例每秒通过业务请求业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的业务请求业务数，即每秒钟允许通过的Service Request消息数。说明：此处设置的个数针对单个MP实例。
SVRREQWGT|业务请求业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置SGSN业务请求业务权重，即一个Service Request消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
RUNUM|每实例每秒通过路由区更新业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的路由区更新业务数，即每秒钟允许通过的Routing Area Update Request消息数。说明：此处设置的个数针对单个MP实例。
RUWGT|路由区更新业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置SGSN路由区更新业务权重，即一个Routing Area Update Request消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
HONUM|每实例每秒通过切换业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的切换业务数，即每秒钟允许通过的Handover Required消息数。说明：此处设置的个数针对单个MP实例。
HOWGT|切换业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置SGSN切换业务权重，即一个Handover Required消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
ACTNUM|每实例每秒通过激活业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的PDP上下文激活业务数，即每秒钟允许通过的Active PDP Context Request消息数。说明：此处设置的个数针对单个MP实例。
ACTWGT|激活业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置SGSNPDP上下文激活业务权重，即一个Active PDP Context Request消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
SMSNUM|每实例每秒通过短消息业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的短消息业务数，即每秒钟允许通过的触发短消息流程的第一条CP-DATA消息数。说明：此处设置的个数针对单个MP实例。
SMSWGT|短消息业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置SGSN短消息业务权重，即一个触发短消息流程的第一条CP-DATA消息相当于多少个消息个数。说明：用于入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
ALLSVRNUM|每实例每秒通过业务最大个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于设置SGSN入向业务总量控制时，每个MP实例每秒钟允许通过的最大业务个数，即最大消息个数。说明：由各个业务加权之和计算的值与该设置值进行比较。
REJECT|拒绝/丢弃策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于SGSN入向业务控制情况下，业务被拒绝后，是否需要给对端回拒绝响应。丢弃: 业务被控制后直接丢弃消息，不需要回拒绝响应消息拒绝: 业务被拒绝后，需要给对端回拒绝响应消息
HLRAUTHNUM|每实例缺省每秒到HLR鉴权最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN出向业务控制时，每个MP实例每秒钟允许发送到单个HLR邻接局的鉴权消息的最大个数。
HLRLUNUM|每实例缺省每秒到HLR位置更新最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN出向业务控制时，每个MP实例每秒钟允许发送到单个HLR邻接局的位置更新消息的最大个数。
SMCSMSNUM|每实例缺省每秒到SMC短消息最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置SGSN出向业务控制时，每个MP实例每秒钟允许发送到单个SMC邻接局的短消息的最大个数。
命令举例 
该命令用于设置SGSN通用业务控制配置，高优先级业务为附着，附着业务保证每秒通过数为10个，MP实例每秒允许通过100个附着业务，附着业务权重为5，拒绝/丢弃策略为丢弃，MP实例缺省每秒到HLR鉴权最大数目为100个。
SET SERVICE CONTROL:HPRISVRI="ATTACH",SERVICENUMG="10"-"6"-"6"-"6"-"6"-"6"-"6"-"6",ATTNUM=100,ATTWGT=5,REJECT="Discard",HLRAUTHNUM=100; 
父主题： [SGSN通用业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询通用业务控制(SHOW SERVICE CONTROL) 
###### 查询通用业务控制(SHOW SERVICE CONTROL) 
命令功能 
该命令用于查询SGSN通用业务控制配置相关信息。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
HPRISVRI|高优先级业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置SGSN高优先级业务，高优先业务只在CPU高过载时才会控制，非高优先级业务只要在CPU拥塞时（高过载、或低过载、或非过载区但拥塞）时都会被控制。取值含义：附着(ATTACH)：Attach Request消息业务请求(SVRREQ)：Service Request消息PDP上下文激活(PDPACT)：Active PDP Context Request消息PDP上下文修改(PDPMOD)：Modify PDP Context Request消息短消息(SMS)：触发短消息流程的第一条CP-DATA消息寻呼(PAGING)：用户面触发的寻呼或CS寻呼流程的Paging Request消息路由区更新(RAU)：Routing Area Update Request消息切换(HO)：Handover Required消息Null(NULL)：不设置任何业务为高优先级说明：当不选择NULL时，业务可以选择多个，选择NULL时，不能选择任何业务。
ATTNUMG|每实例每秒保证通过业务数(附着)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN保证每秒通过的附着业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Attach Request消息数。说明：此处设置的个数针对单个MP实例。
SVRREQNUMG|每实例每秒保证通过业务数(业务请求)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN保证每秒通过的业务请求业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Service Request消息数。说明：此处设置的个数针对单个MP实例。
PDPACTNUMG|每实例每秒保证通过业务数(PDP上下文激活)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN保证每秒通过的PDP上下文激活业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Active PDP Context Request消息数。说明：此处设置的个数针对单个MP实例。
PDPMODNUMG|每实例每秒保证通过业务数(PDP上下文修改)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN保证每秒通过的PDP上下文修改业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Modify PDP Context Request消息数。说明：此处设置的个数针对单个MP实例。
SMSNUMG|每实例每秒保证通过业务数(短消息)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN保证每秒通过的短消息业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的触发短消息流程的第一条CP-DATA消息数。说明：此处设置的个数针对单个MP实例。
PAGENUMG|每实例每秒保证通过业务数(寻呼)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN保证每秒通过的寻呼（包括用户面触发的寻呼和CS寻呼）业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Paging Request消息数。说明：此处设置的个数针对单个MP实例。
RUNUMG|每实例每秒保证通过业务数(路由区更新)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN保证每秒通过的路由区更新业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Routing Area Update Request消息数。说明：此处设置的个数针对单个MP实例。
HONUMG|每实例每秒保证通过业务数(切换)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN保证每秒通过的切换业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Handover Required消息数。说明：此处设置的个数针对单个MP实例。
ATTNUM|每实例每秒通过附着业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的附着业务数，即每秒钟允许通过的Attach Request消息数。说明：此处设置的个数针对单个MP实例。
ATTWGT|附着业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN附着业务权重，即一个Attach Request消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
SVRREQNUM|每实例每秒通过业务请求业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的业务请求业务数，即每秒钟允许通过的Service Request消息数。说明：此处设置的个数针对单个MP实例。
SVRREQWGT|业务请求业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN业务请求业务权重，即一个Service Request消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
RUNUM|每实例每秒通过路由区更新业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的路由区更新业务数，即每秒钟允许通过的Routing Area Update Request消息数。说明：此处设置的个数针对单个MP实例。
RUWGT|路由区更新业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN路由区更新业务权重，即一个Routing Area Update Request消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
HONUM|每实例每秒通过切换业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的切换业务数，即每秒钟允许通过的Handover Required消息数。说明：此处设置的个数针对单个MP实例。
HOWGT|切换业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN切换业务权重，即一个Handover Required消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
ACTNUM|每实例每秒通过激活业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的PDP上下文激活业务数，即每秒钟允许通过的Active PDP Context Request消息数。说明：此处设置的个数针对单个MP实例。
ACTWGT|激活业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSNPDP上下文激活业务权重，即一个Active PDP Context Request消息相当于多少个消息个数。说明：用于SGSN入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
SMSNUM|每实例每秒通过短消息业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN入向业务控制时每秒钟允许通过的短消息业务数，即每秒钟允许通过的触发短消息流程的第一条CP-DATA消息数。说明：此处设置的个数针对单个MP实例。
SMSWGT|短消息业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN短消息业务权重，即一个触发短消息流程的第一条CP-DATA消息相当于多少个消息个数。说明：用于入向业务控制时总业务数的控制，每秒钟允许通过的总的消息数的控制。
ALLSVRNUM|每实例每秒通过业务最大个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN入向业务总量控制时，每个MP实例每秒钟允许通过的最大业务个数，即最大消息个数。说明：由各个业务加权之和计算的值与该设置值进行比较。
REJECT|拒绝/丢弃策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于SGSN入向业务控制情况下，业务被拒绝后，是否需要给对端回拒绝响应。丢弃: 业务被控制后直接丢弃消息，不需要回拒绝响应消息拒绝: 业务被拒绝后，需要给对端回拒绝响应消息
HLRAUTHNUM|每实例缺省每秒到HLR鉴权最大数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN出向业务控制时，每个MP实例每秒钟允许发送到单个HLR邻接局的鉴权消息的最大个数。
HLRLUNUM|每实例缺省每秒到HLR位置更新最大数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN出向业务控制时，每个MP实例每秒钟允许发送到单个HLR邻接局的位置更新消息的最大个数。
SMCSMSNUM|每实例缺省每秒到SMC短消息最大数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN出向业务控制时，每个MP实例每秒钟允许发送到单个SMC邻接局的短消息的最大个数。
命令举例 
该命令用于查询SGSN通用业务控制配置相关信息。
SHOW SERVICE CONTROL; 
`
命令 (No.1): SHOW SERVICE CONTROL
操作维护  高优先级业务   MP实例保证每秒通过业务数(附着)   MP实例保证每秒通过业务数(业务请求)   MP实例保证每秒通过业务数(PDP上下文激活)   MP实例保证每秒通过业务数(PDP上下文修改)   MP实例保证每秒通过业务数(短消息)   MP实例保证每秒通过业务数(寻呼)   MP实例保证每秒通过业务数(路由区更新)   MP实例保证每秒通过业务数(切换)   MP实例每秒通过附着业务个数   附着业务权重   MP实例每秒通过业务请求业务个数   业务请求业务权重   MP实例每秒通过路由区更新业务个数   路由区更新业务权重   MP实例每秒通过切换业务个数   切换业务权重   MP实例每秒通过激活业务个数   激活业务权重   MP实例每秒通过短消息业务个数   短消息业务权重   MP实例每秒通过业务最大个数   拒绝/丢弃策略   MP实例缺省每秒到HLR鉴权最大数目   MP实例缺省每秒到HLR位置更新最大数目   MP实例缺省每秒到SMC短消息最大数目
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      附着           10                                20                                    5                                          5                                          5                                   5                                 15                                      5                                 100                           5              65535                             6                  65535                               9                    65535                         15             65535                         4              65535                           2                4294967295                    丢弃            100                                65535                                  65535
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.043 秒）。
` 
父主题： [SGSN通用业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### SGSN特定局向业务控制配置 
##### SGSN特定局向业务控制配置 
背景知识 
SGSN支持支持限制本端到HLR、SMC的出向业务量，来控制对方的业务负荷。 
功能描述 
            
            本配置项针对特定的HLR、SMC局向设置出向业务控制，保护对方网元。如果该HLR、SMC局向没有配置特定局向业务控制时，采用
            [SET SGSN SERVICE CONTROL]
            命令中配置的默认HLR/SMC局向控制参数。
        
相关主题 
 
新增SGSN特定局向业务控制配置(ADD SGSN OFFICE SERVICE MAXIMUM)
 
 
修改SGSN特定局向业务控制配置(SET SGSN OFFICE SERVICE MAXIMUM)
 
 
删除SGSN特定局向业务控制配置(DEL SGSN OFFICE SERVICE MAXIMUM)
 
 
查询SGSN特定局向业务控制配置(SHOW SGSN OFFICE SERVICE MAXIMUM)
 
 
父主题： [SGSN业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 新增SGSN特定局向业务控制配置(ADD SGSN OFFICE SERVICE MAXIMUM) 
###### 新增SGSN特定局向业务控制配置(ADD SGSN OFFICE SERVICE MAXIMUM) 
命令功能 
该命令用于增加SGSN特定局向业务控制参数的配置。当需要针对SGSN特定局向进行允许的出向业务个数进行特殊设置时，使用该命令。成功后，发往该特定局向的业务数通过数将采用自身配置进行控制，通用业务控制中的相关参数对其无效。
注意事项 
 
该配置命令中允许个数若设置为65535，则表示不对其进行控制。
 
 
到HLR的鉴权和位置更新最大数的配置只有邻接局类型为HLR时才有效。到SMC的短消息最大数的配置只有邻接局类型为SMC时才有效。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定SGSN特定邻接局的局向号。SGSN特定邻接局需要在邻接局已经配置。查询命令参见SHOW ADJOFC。
HLRAUTHNUM|每进程每秒到HLR鉴权最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:65535。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该HLR的鉴权消息的最大个数。局向号对应的邻接局类型为HLR时该配置才有效。
HLRLUNUM|每进程每秒到HLR位置更新最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:65535。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该HLR的位置更新消息的最大个数。局向号对应的邻接局类型为HLR时该配置才有效。
SMCSMSNUM|每进程每秒到SMC短消息最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:65535。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该SMC的短消息的最大个数。局向号对应的邻接局类型为SMC时该配置才有效
命令举例 
该命令用于新增局向号为1的邻接局的业务控制配置，MP进程每秒到HLR鉴权最大数目为100，MP模块每秒到HLR位置更新最大数目为200，MP模块每秒到SMC短消息最大数目为65535（即不控制发送到SMC的短消息数）。
ADD SGSN OFFICE SERVICE MAXIMUM:ADJID=1,HLRAUTHNUM=100,HLRLUNUM=200,SMCSMSNUM=65535; 
父主题： [SGSN特定局向业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 修改SGSN特定局向业务控制配置(SET SGSN OFFICE SERVICE MAXIMUM) 
###### 修改SGSN特定局向业务控制配置(SET SGSN OFFICE SERVICE MAXIMUM) 
命令功能 
该命令用于修改SGSN特定局向业务控制参数的配置。当需要对已存在配置的SGSN特定局向业务控制参数进行修改时，使用该命令。
注意事项 
 
该配置命令中允许个数若设置为65535，则表示不对其进行控制。
 
 
到HLR的鉴权和位置更新最大数的配置只有邻接局类型为HLR时才有效。到SMC的短消息最大数的配置只有邻接局类型为SMC时才有效。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定SGSN特定邻接局的局向号。SGSN特定邻接局需要在邻接局已经配置。查询命令参见SHOW ADJOFC。
HLRAUTHNUM|每进程每秒到HLR鉴权最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该HLR的鉴权消息的最大个数。局向号对应的邻接局类型为HLR时该配置才有效。
HLRLUNUM|每进程每秒到HLR位置更新最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该HLR的位置更新消息的最大个数。局向号对应的邻接局类型为HLR时该配置才有效。
SMCSMSNUM|每进程每秒到SMC短消息最大数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该SMC的短消息的最大个数。局向号对应的邻接局类型为SMC时该配置才有效
命令举例 
该命令用于修改局向号为1的邻接局的业务控制配置，MP进程每秒到HLR鉴权最大数目改为200，MP模块每秒到HLR位置更新最大数目改为65535（即不控制发送到HLR的位置更新消息数）。
SET SGSN OFFICE SERVICE MAXIMUM:ADJID=1,HLRAUTHNUM=200,HLRLUNUM=65535; 
父主题： [SGSN特定局向业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 删除SGSN特定局向业务控制配置(DEL SGSN OFFICE SERVICE MAXIMUM) 
###### 删除SGSN特定局向业务控制配置(DEL SGSN OFFICE SERVICE MAXIMUM) 
命令功能 
该命令用于删除SGSN特定局向业务控制参数配置。当该特定邻接局不采用特定配置，而直接采用SGSN通用业务控制配置时，使用该命令。
注意事项 
该命令执行后，SGSN特定局向业务控制参数被删除，而特定局向号对应的SGSN邻接局将采用SGSN通用业务控制配置中的相应配置。
参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定SGSN特定邻接局的局向号。SGSN特定邻接局需要在邻接局已经配置。查询命令参见SHOW ADJOFC。
命令举例 
该命令用于删除局向号为1的SGSN邻接局的特定业务控制配置。
DEL SGSN OFFICE SERVICE MAXIMUM:ADJID=1; 
父主题： [SGSN特定局向业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询SGSN特定局向业务控制配置(SHOW SGSN OFFICE SERVICE MAXIMUM) 
###### 查询SGSN特定局向业务控制配置(SHOW SGSN OFFICE SERVICE MAXIMUM) 
命令功能 
该命令用于查询SGSN特定局向业务控制配置的相关信息。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|该参数用于指定SGSN特定邻接局的局向号。SGSN特定邻接局需要在邻接局已经配置。查询命令参见SHOW ADJOFC。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:任选参数；参数类型:整数。|该参数用于指定SGSN特定邻接局的局向号。SGSN特定邻接局需要在邻接局已经配置。查询命令参见SHOW ADJOFC。
HLRAUTHNUM|每进程每秒到HLR鉴权最大数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该HLR的鉴权消息的最大个数。局向号对应的邻接局类型为HLR时该配置才有效。
HLRLUNUM|每进程每秒到HLR位置更新最大数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该HLR的位置更新消息的最大个数。局向号对应的邻接局类型为HLR时该配置才有效。
SMCSMSNUM|每进程每秒到SMC短消息最大数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置指定SGSN特定邻接局在出向业务控制时，SGSN每个MP模块每秒钟允许发送到该SMC的短消息的最大个数。局向号对应的邻接局类型为SMC时该配置才有效
命令举例 
该命令用于查询局向号为1的SGSN邻接局的特定业务控制配置。
SHOW SGSN OFFICE SERVICE MAXIMUM:ADJID=1; 
`
命令 (No.1): SHOW SGSN OFFICE SERVICE MAXIMUM:ADJID=1;
操作维护         局向ID   MP进程每秒到HLR鉴权最大数目   MP进程每秒到HLR位置更新最大数目   MP进程每秒到SMC短消息最大数目
--------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1        100                            200                                65535
--------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.043 秒）。
` 
父主题： [SGSN特定局向业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### SGSN自动业务控制策略配置 
##### SGSN自动业务控制策略配置 
背景知识 
本功能根据业务成功率来评判当前系统中是否存在拥塞，通过限制接入的业务量，保证整个系统的业务正常。 
功能描述 
SGSN网元对接入业务（Attach/局间RAU/跨RAT RAU）进行自动拥塞控制，目的是为了保护HLR，在HLR的业务处理能力比较弱的情况下，SGSN需要根据HLR的业务处理能力来进行配置。 
相关主题 
 
设置SGSN自动业务控制策略(SET SGSN AUTO CNGCTL)
 
 
查询SGSN自动业务控制策略(SHOW SGSN AUTO CNGCTL)
 
 
父主题： [SGSN业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置SGSN自动业务控制策略(SET SGSN AUTO CNGCTL) 
###### 设置SGSN自动业务控制策略(SET SGSN AUTO CNGCTL) 
命令功能 
该命令用于设置自动业务控制功能策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
FLG|是否开启|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关。
STARTCAPS|触发拥塞的接入业务通过数量(单进程每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|只有在本进程，每秒的业务（Attach/局间RAU/跨RAT RAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
MAXCAPS|允许通过的接入业务最大数量(单进程每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|本进程每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的HLR业务成功率(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|一旦业务成功率降低（低于成功门限），且接入本进程的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
命令举例 
设置SGSN自动业务控制策略，其中是否开启设置为是，触发拥塞的接入业务通过数量(单进程每秒)为20，允许通过的接入业务最大数量(单进程每秒)为60，触发拥塞的HLR业务成功率(%)为85，接入业务控制步长为4，控制持续时间(分钟)为30。 
SET SGSN AUTO CNGCTL:FLG="YES",STARTCAPS=20,MAXCAPS=60,SUCCRATE=85,STEP=4,LASTTIME=30; 
父主题： [SGSN自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询SGSN自动业务控制策略(SHOW SGSN AUTO CNGCTL) 
###### 查询SGSN自动业务控制策略(SHOW SGSN AUTO CNGCTL) 
命令功能 
该命令用于查询自动业务控制功能策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FLG|是否开启|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关。
STARTCAPS|触发拥塞的接入业务通过数量(单进程每秒)|参数可选性:任选参数；参数类型:整数。|只有在本进程，每秒的业务（Attach/局间RAU/跨RAT RAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
MAXCAPS|允许通过的接入业务最大数量(单进程每秒)|参数可选性:任选参数；参数类型:整数。|本进程每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的HLR业务成功率(%)|参数可选性:任选参数；参数类型:整数。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数。|一旦业务成功率降低（低于成功门限），且接入本进程的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
命令举例 
查询SGSN自动业务控制策略。 
SHOW SGSN AUTO CNGCTL; 
`
命令 (No.1): SHOW SGSN AUTO CNGCTL
操作维护   是否开启   触发拥塞的接入业务通过数量(单进程每秒)   允许通过的接入业务最大数量(单进程每秒)   触发拥塞的HLR业务成功率(%)   接入业务控制步长   控制持续时间(分钟)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改       是         20                                       60                                       85                           4                  30 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [SGSN自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### MME业务控制配置 
#### MME业务控制配置 
背景知识 
MME支持限制对端到本端的入向业务量，来控制自身的业务负荷；也支持限制本端到HSS、VLR的出向业务量，来控制对方的业务负荷。 
功能描述 
“MME业务控制配置”配置 MME的入向、出向业务控制门限，高优先级业务类型，CPU拥塞控制业务保证通过数。 
相关主题 
 
MME通用业务控制配置
 
 
MME特定Diameter业务控制配置
 
 
MME特定VLR局向业务控制配置
 
 
MME自动业务控制策略配置
 
 
S6a ALC局向流控策略配置
 
 
S6a ALC局向IMSI号段配置
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### MME通用业务控制配置 
##### MME通用业务控制配置 
背景知识 
MME支持限制对端到本端的入向业务量，来控制自身的业务负荷；也支持限制本端到HSS、VLR的出向业务量，来控制对方的业务负荷。 
功能描述 
“MME通用业务控制配置”用于过负荷控制时，配置业务相关的参数。主要包括以下内容： 
配置哪些业务是高优先级业务，对于高优先级业务，仅在CPU处于高过载区时才进行控制。非高优先级业务只要在CPU拥塞时（高过载、或低过载、或非过载区但拥塞）时都会被控制。 
单位时间保证业务通过数，即使MP CPU再拥塞，每个MP实例也会保证通过一部分业务，目的是在拥塞时对业务进行“泄洪”。 
MP每实例通过业务最大数，用于入向业务单项控制，单位时间内MP实例单项业务不能超过该最大通过数。 
业务权重配置和MP实例每秒通过业务最大个数，用于入向业务总量控制，各个单项业务加权叠加，不能超过MP实例每秒通过业务最大个数。 
                MP实例默认每秒到Diameter局向的最大业务，用于出向针对Diameter局向的业务控制，保护对方网元。如果需要针对特定的Diameter局向进行控制，可以通过
                [ADD MME DIAMETER SERVICE MAXIMUM]
                命令配置。
            
                MP实例默认每秒到VLR局向的最大业务，用于出向针对VLR局向的业务控制，保护对方网元。如果需要针对特定的VLR局向进行控制，可以通过
                [ADD MOLVLR]
                命令配置。
            
                入向业务控制和出向业务控制，优先级高于CPU拥塞控制（CPU拥塞控制命令：
                [SET OVERLOAD BASIC PARA]
                ），配置入向、出向业务控制可以快速地降低系统负荷，设置的门限值需要根据实际话务模型设定（默认不控制）。
            
相关主题 
 
设置MME通用业务控制(SET MME SERVICE CONTROL)
 
 
查询MME通用业务控制(SHOW MME SERVICE CONTROL)
 
 
父主题： [MME业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置MME通用业务控制(SET MME SERVICE CONTROL) 
###### 设置MME通用业务控制(SET MME SERVICE CONTROL) 
命令功能 
该命令用于设置MME网元过负荷相关的通用业务控制参数。当需要更改MME通用业务控制参数时，如高优先业务配置、保证业务通过数配置、允许通过业务数配置、业务权重配置、入向业务控制对应的拒绝/丢弃策略、到Diameter局向的鉴权及位置更新最大数目等参数时，使用该命令。MME通用业务控制参数设置成功后，会影响MME网元CPU拥塞时的控制策略、入向业务控制时消息通过数的控制和拒绝/丢弃策略、及每秒发送鉴权和位置更新消息到Diameter局向的最大数目的控制。 
到Diameter局向的鉴权及位置更新最大数目也可以针对局向ID进行特定配置。 
注意事项 
 
该命令中拒绝/丢弃策略只对MME业务相关的入向业务控制有效。CPU拥塞控制对应的拒绝/丢弃策略通过过负荷基本参数配置来设置，配置命令为： SET OVERLOAD BASIC PARA：REJECT="Discard";。
 
 
高优先级业务配置只对CPU拥塞控制生效。
 
 
该命令中的参数建议采用默认配置，非特殊要求无需修改。
 
 
到VLR局向的位置更新以及起呼短消息最大数目也可以针对局向ID进行特定配置。
 
 
NBIOT流程未做特别区分，包含在各个流程中。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
HPRISVRI|高优先级业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME高优先级业务。高优先级业务仅在CPU拥塞并且CPU使用率处于高过载区才控制，相对于非高优先级业务，可以优先保证高优先级业务的放行。取值含义：附着(ATTACH)：Attach Request消息业务请求(SVRREQ)：Service Request消息PDN连接建立(PDNCONN)：PDN Connectivity Request消息专有承载建立(BEARERACT)：Create Bearer Request消息承载修改(BEARERMOD)：Update Bearer Request消息寻呼(PAGING)：下行数据通知触发寻呼的Downlink Data Notification消息或CS寻呼流程的Paging Request消息跟踪区更新(TAU)：TAU Request消息切换(HO)：无线侧或网络侧触发的切换业务涉及到的Handover Required、Path Switch Request消息Null(NULL)：不设置任何业务为高优先级，即只要CPU拥塞时就对所有业务进行控制
ATTNUMG|附着|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置MME保证每秒通过的附着业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Attach Request消息数。说明：此处设置的个数针对单个MP实例。
SVRREQNUMG|业务请求|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置MME保证每秒通过的业务请求业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Service Request消息数。说明：此处设置的个数针对单个MP实例。
PDNCONNNUMG|PDN连接建立|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置MME保证每秒通过的PDN连接建立业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的PDN Connectivity Request消息数。说明：此处设置的个数针对单个MP实例。
DEDIACTNUMG|专有承载建立|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置MME保证每秒通过的专有承载建立业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Create Bearer Request消息数。说明：此处设置的个数针对单个MP实例。
BEARMODNUMG|承载修改|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置MME保证每秒通过的承载修改业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Update Bearer Request消息数。说明：此处设置的个数针对单个MP实例。
PAGENUMG|寻呼|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置MME保证每秒通过的寻呼业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的下行数据通知触发寻呼的Downlink Data Notification或CS寻呼流程的Paging Request消息数。说明：此处设置的个数针对单个MP实例。
TUNUMG|跟踪区更新|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置MME保证每秒通过的跟踪区更新业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的TAU Request消息数。说明：此处设置的个数针对单个MP实例。
HONUMG|切换|参数可选性:任选参数；参数类型:整数；参数范围为:5~65535。|该参数用于设置MME保证每秒通过的切换业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的无线侧或网络侧触发的切换业务涉及到的Handover Required、Path Switch Request消息数。说明：此处设置的个数针对单个MP实例。
SERVICENUMG|每实例每秒保证通过业务数|参数可选性:任选参数；参数类型:复合参数|该参数是以上ATTNUMG、SVRREQNUMG、PDNCONNNUMG、DEDIACTNUMG、BEARMODNUMG、PAGENUMG、TUNUMG、HONUMG各个参数的组合。用于设置MME保证每秒通过的各项业务数。
ATTNUM|每实例每秒通过附着业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME入向业务控制时每秒钟允许通过的附着业务数，即每秒钟允许通过的Attach Request消息数。说明：此处设置的个数针对单个MP实例。
ATTWGT|附着业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置MME附着业务权重，即一个Attach Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
SVRREQNUM|每实例每秒通过业务请求业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME入向业务控制时每秒钟允许通过的业务请求业务数，即每秒钟允许通过的Service Request消息数。说明：此处设置的个数针对单个MP实例。
SVRREQWGT|业务请求业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置MME业务请求业务权重，即一个Service Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
TUNUM|每实例每秒通过跟踪区更新业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME入向业务控制时每秒钟允许通过的跟踪区更新业务数，即每秒钟允许通过的TAU Request消息数。说明：此处设置的个数针对单个MP实例。
TUWGT|跟踪区更新业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置MME跟踪区更新业务权重，即一个TAU Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
HONUM|每实例每秒通过切换业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME入向业务控制时每秒钟允许通过的切换业务数，即每秒钟允许通过的Handover Required、Path Switch Request及Forward Relocation Request消息数。说明：此处设置的个数针对单个MP实例。
HOWGT|切换业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置MME切换业务权重，即一个Handover Required或Path Switch Request或Forward Relocation Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
PDNCONNNUM|每实例每秒通过PDN连接业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME入向业务控制时每秒钟允许通过的PDN连接业务数，即每秒钟允许通过的PDN Connectivity Request消息数。说明：此处设置的个数针对单个MP实例。
PDNCWGT|PDN连接业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置MME PDN连接业务权重，即一个PDN Connectivity Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
DEDIACTNUM|每实例每秒通过专用承载激活业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME入向业务控制时每秒钟允许通过的专用承载激活业务数，即每秒钟允许通过的Create Bearer Request消息数。说明：此处设置的个数针对单个MP实例。
DEDIACTWGT|专用承载激活业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置MME专用承载激活业务权重，即一个Create Bearer Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
DNINFONUM|每实例每秒通过下行数据通知业务个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME入向业务控制时每秒钟允许通过的下行数据通知业务数，即每秒钟允许通过的Downlink Data Notification消息数。说明：此处设置的个数针对单个MP实例。
DNINFOWGT|下行数据通知业务权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|该参数用于设置MME下行数据通知业务权重，即一个Downlink Data Notification消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
ALLSVRNUM|每实例每秒通过业务最大个数|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于设置MME入向业务总量控制时，每个MP实例每秒钟允许通过的最大业务个数，即最大消息个数。说明：由各个业务加权之和计算的值与该设置值进行比较。
REJECT|拒绝/丢弃策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于MME入向业务控制情况下，业务被拒绝后，是否需要给对端回拒绝响应。丢弃: 业务被控制后直接丢弃消息，不需要回拒绝响应消息拒绝: 业务被拒绝后，需要给对端回拒绝响应消息
DIAMAUTHNUM|默认每实例每秒到Diameter局向最大鉴权业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME出向业务控制时，每个MP实例每秒钟允许发送到单个Diameter局向的鉴权消息的最大个数。
DIAMLUNUM|默认每实例每秒到Diameter局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME出向业务控制时，每个MP实例每秒钟允许发送到单个Diameter局向的位置更新消息的最大个数。
VLRLUNUM|默认每实例每秒到VLR局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME出向业务控制时，每个MP实例每秒钟允许发送到单个VLR局向的位置更新消息的最大个数。
VLRMOSMSNUM|默认每实例每秒到VLR局向最大起呼短消息业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于设置MME出向业务控制时，每个MP实例每秒钟允许发送到单个VLR局向的起呼短消息的最大个数。
BACKOFFTIMESTART|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端BackOff Time的最小值。该参数用于MME入向业务控制情况下，业务被拒绝时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
BACKOFFTIMEEND|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端BackOff Time的最大值。该参数用于MME入向业务控制情况下，业务被拒绝时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
命令举例 
该命令用于设置MME通用业务控制配置，高优先级业务为附着，附着业务保证每秒通过数为10个，MP实例每秒允许通过200个附着业务，附着业务权重为10，拒绝/丢弃策略为拒绝，MP实例缺省每秒到Diameter局向最大鉴权业务数目为156个。
SET MME SERVICE CONTROL:HPRISVRI="ATTACH",SERVICENUMG="10"-"6"-"6"-"6"-"6"-"6"-"6"-"6",ATTNUM=200,ATTWGT=10,REJECT="Refuse",DIAMAUTHNUM=156; 
父主题： [MME通用业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询MME通用业务控制(SHOW MME SERVICE CONTROL) 
###### 查询MME通用业务控制(SHOW MME SERVICE CONTROL) 
命令功能 
该命令用于查询MME通用业务控制配置相关信息。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
HPRISVRI|高优先级业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME高优先级业务。高优先级业务仅在CPU拥塞并且CPU使用率处于高过载区才控制，相对于非高优先级业务，可以优先保证高优先级业务的放行。取值含义：附着(ATTACH)：Attach Request消息业务请求(SVRREQ)：Service Request消息PDN连接建立(PDNCONN)：PDN Connectivity Request消息专有承载建立(BEARERACT)：Create Bearer Request消息承载修改(BEARERMOD)：Update Bearer Request消息寻呼(PAGING)：下行数据通知触发寻呼的Downlink Data Notification消息或CS寻呼流程的Paging Request消息跟踪区更新(TAU)：TAU Request消息切换(HO)：无线侧或网络侧触发的切换业务涉及到的Handover Required、Path Switch Request消息Null(NULL)：不设置任何业务为高优先级，即只要CPU拥塞时就对所有业务进行控制
ATTNUMG|每实例每秒保证通过业务数(附着)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME保证每秒通过的附着业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Attach Request消息数。说明：此处设置的个数针对单个MP实例。
SVRREQNUMG|每实例每秒保证通过业务数(业务请求)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME保证每秒通过的业务请求业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Service Request消息数。说明：此处设置的个数针对单个MP实例。
PDNCONNNUMG|每实例每秒保证通过业务数(PDN连接建立)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME保证每秒通过的PDN连接建立业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的PDN Connectivity Request消息数。说明：此处设置的个数针对单个MP实例。
DEDIACTNUMG|每实例每秒保证通过业务数(专有承载建立)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME保证每秒通过的专有承载建立业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Create Bearer Request消息数。说明：此处设置的个数针对单个MP实例。
BEARMODNUMG|每实例每秒保证通过业务数(承载修改)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME保证每秒通过的承载修改业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的Update Bearer Request消息数。说明：此处设置的个数针对单个MP实例。
PAGENUMG|每实例每秒保证通过业务数(寻呼)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME保证每秒通过的寻呼业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的下行数据通知触发寻呼的Downlink Data Notification或CS寻呼流程的Paging Request消息数。说明：此处设置的个数针对单个MP实例。
TUNUMG|每实例每秒保证通过业务数(跟踪区更新)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME保证每秒通过的跟踪区更新业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的TAU Request消息数。说明：此处设置的个数针对单个MP实例。
HONUMG|每实例每秒保证通过业务数(切换)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME保证每秒通过的切换业务数，即无论CPU拥塞程度如何，在进行过负荷控制时，仍然需要确保每秒至少通过的无线侧或网络侧触发的切换业务涉及到的Handover Required、Path Switch Request消息数。说明：此处设置的个数针对单个MP实例。
ATTNUM|每实例每秒通过附着业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME入向业务控制时每秒钟允许通过的附着业务数，即每秒钟允许通过的Attach Request消息数。说明：此处设置的个数针对单个MP实例。
ATTWGT|附着业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME附着业务权重，即一个Attach Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
SVRREQNUM|每实例每秒通过业务请求业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME入向业务控制时每秒钟允许通过的业务请求业务数，即每秒钟允许通过的Service Request消息数。说明：此处设置的个数针对单个MP实例。
SVRREQWGT|业务请求业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME业务请求业务权重，即一个Service Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
TUNUM|每实例每秒通过跟踪区更新业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME入向业务控制时每秒钟允许通过的跟踪区更新业务数，即每秒钟允许通过的TAU Request消息数。说明：此处设置的个数针对单个MP实例。
TUWGT|跟踪区更新业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME跟踪区更新业务权重，即一个TAU Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
HONUM|每实例每秒通过切换业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME入向业务控制时每秒钟允许通过的切换业务数，即每秒钟允许通过的Handover Required、Path Switch Request及Forward Relocation Request消息数。说明：此处设置的个数针对单个MP实例。
HOWGT|切换业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME切换业务权重，即一个Handover Required或Path Switch Request或Forward Relocation Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
PDNCONNNUM|每实例每秒通过PDN连接业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME入向业务控制时每秒钟允许通过的PDN连接业务数，即每秒钟允许通过的PDN Connectivity Request消息数。说明：此处设置的个数针对单个MP实例。
PDNCWGT|PDN连接业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME PDN连接业务权重，即一个PDN Connectivity Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
DEDIACTNUM|每实例每秒通过专用承载激活业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME入向业务控制时每秒钟允许通过的专用承载激活业务数，即每秒钟允许通过的Create Bearer Request消息数。说明：此处设置的个数针对单个MP实例。
DEDIACTWGT|专用承载激活业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME专用承载激活业务权重，即一个Create Bearer Request消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
DNINFONUM|每实例每秒通过下行数据通知业务个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME入向业务控制时每秒钟允许通过的下行数据通知业务数，即每秒钟允许通过的Downlink Data Notification消息数。说明：此处设置的个数针对单个MP实例。
DNINFOWGT|下行数据通知业务权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME下行数据通知业务权重，即一个Downlink Data Notification消息相当于多少个消息个数。说明：用于MME入向业务控制时总业务数的控制，每秒钟允许通过的总消息数。
ALLSVRNUM|每实例每秒通过业务最大个数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME入向业务总量控制时，每个MP实例每秒钟允许通过的最大业务个数，即最大消息个数。说明：由各个业务加权之和计算的值与该设置值进行比较。
REJECT|拒绝/丢弃策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于MME入向业务控制情况下，业务被拒绝后，是否需要给对端回拒绝响应。丢弃: 业务被控制后直接丢弃消息，不需要回拒绝响应消息拒绝: 业务被拒绝后，需要给对端回拒绝响应消息
DIAMAUTHNUM|默认每实例每秒到Diameter局向最大鉴权业务数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME出向业务控制时，每个MP实例每秒钟允许发送到单个Diameter局向的鉴权消息的最大个数。
DIAMLUNUM|默认每实例每秒到Diameter局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME出向业务控制时，每个MP实例每秒钟允许发送到单个Diameter局向的位置更新消息的最大个数。
VLRLUNUM|默认每实例每秒到VLR局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME出向业务控制时，每个MP实例每秒钟允许发送到单个VLR局向的位置更新消息的最大个数。
VLRMOSMSNUM|默认每实例每秒到VLR局向最大起呼短消息业务数目|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME出向业务控制时，每个MP实例每秒钟允许发送到单个VLR局向的起呼短消息的最大个数。
BACKOFFTIMESTART|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端BackOff Time的最小值。该参数用于MME入向业务控制情况下，业务被拒绝时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
BACKOFFTIMEEND|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端BackOff Time的最大值。该参数用于MME入向业务控制情况下，业务被拒绝时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。
命令举例 
该命令用于查询MME通用业务控制配置相关信息。 
SHOW MME SERVICE CONTROL; 
`
命令 (No.2): SHOW MME SERVICE CONTROL
操作维护  高优先级业务        每实例每秒保证通过业务数(附着)   每实例每秒保证通过业务数(业务请求)   每实例每秒保证通过业务数(PDN连接建立)   每实例每秒保证通过业务数(专有承载建立)   每实例每秒保证通过业务数(承载修改)   每实例每秒保证通过业务数(寻呼)   每实例每秒保证通过业务数(跟踪区更新)   每实例每秒保证通过业务数(切换)   每实例每秒通过附着业务个数   附着业务权重   每实例每秒通过业务请求业务个数   业务请求业务权重   每实例每秒通过跟踪区更新业务个数   跟踪区更新业务权重   每实例每秒通过切换业务个数   切换业务权重   每实例每秒通过PDN连接业务个数   PDN连接业务权重   每实例每秒通过专用承载激活业务个数   专用承载激活业务权重   每实例每秒通过下行数据通知业务个数   下行数据通知业务权重   每实例每秒通过业务最大个数   拒绝/丢弃策略   默认每实例每秒到Diameter局向最大鉴权业务数目   默认每实例每秒到Diameter局向最大位置更新业务数目   默认每实例每秒到VLR局向最大位置更新业务数目   默认每实例每秒到VLR局向最大起呼短消息业务数目   拒绝时携带的Back-off Timer最小取值（秒）   拒绝时携带的Back-off Timer最大取值（秒）
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      跟踪区更新 & 切换   11                               45                                   5                                       5                                        5                                    9                                50                                     5                                65535                        10             65535                            3                  65535                              6                    65535                        12             65535                           6                 65535                                3                      65535                                8                      4294967295                   丢弃            65535                                          65535                                              65535                                         65535                                           0                                          0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.036 秒）。
` 
父主题： [MME通用业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### MME特定Diameter业务控制配置 
##### MME特定Diameter业务控制配置 
背景知识 
MME支持控制本端发送到到特定Diameter协议类型的网元（比如HSS）的消息数，来避免对端网元因短时间收到大量消息冲击而出现过负荷的情况。 
功能描述 
                本配置项针对特定的Diameter局向设置出向业务控制，保护对方网元。如果该Diameter局向没有配置特定Diameter局向业务控制时，采用“
                [SET MME SERVICE CONTROL]
                ”命令中配置的默认Diameter局向控制参数。
            
相关主题 
 
新增MME特定Diameter业务控制(ADD MME DIAMETER SERVICE MAXIMUM)
 
 
修改MME特定Diameter业务控制(SET MME DIAMETER SERVICE MAXIMUM)
 
 
删除MME特定Diameter业务控制(DEL MME DIAMETER SERVICE MAXIMUM)
 
 
查询MME特定Diameter业务控制(SHOW MME DIAMETER SERVICE MAXIMUM)
 
 
父主题： [MME业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 新增MME特定Diameter业务控制(ADD MME DIAMETER SERVICE MAXIMUM) 
###### 新增MME特定Diameter业务控制(ADD MME DIAMETER SERVICE MAXIMUM) 
命令功能 
该命令用于增加MME特定Diameter业务控制配置。当过负荷控制对某个diameter局向不采用MME通用业务控制配置来控制业务，而是需要对该局向进行特殊配置来控制业务时，使用该命令。 
增加成功后，MME根据配置规则实现业务控制，主要包括控制MP进程每秒到Diameter局向最大鉴权业务数目和MP进程每秒到Diameter局向最大位置更新业务数目。 
注意事项 
 
该配置命令中MP进程每秒到Diameter局向最大鉴权业务数目或MP进程每秒到Diameter局向最大位置更新业务数目若设置为65535，则表示不对其进行控制。
 
 
配置该命令前，首先要新增diameter局向配置。配置命令参见ADD DIAMADJ。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向的局向ID。要求全局唯一。局向ID的查询命令参见SHOW DIAMADJ。
DIAMAUTHNUM|每进程每秒到Diameter局向最大鉴权业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:65535。|该参数用于限制MP进程每秒向Diameter局向发送的鉴权业务数。默认值为65535，表示不对其进行控制。
DIAMLUNUM|每进程每秒到Diameter局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:65535。|该参数用于限制MP进程每秒向Diameter局向发送的位置更新业务数。默认值为65535，表示不对其进行控制。
命令举例 
新增MME特定Diameter业务控制配置，局向ID为1，MP进程每秒到Diameter局向最大鉴权业务数目为100，MP进程每秒到Diameter局向最大位置更新业务数目为200。
ADD MME DIAMETER SERVICE MAXIMUM:ADJID=1,DIAMAUTHNUM=100,DIAMLUNUM=200； 
父主题： [MME特定Diameter业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 修改MME特定Diameter业务控制(SET MME DIAMETER SERVICE MAXIMUM) 
###### 修改MME特定Diameter业务控制(SET MME DIAMETER SERVICE MAXIMUM) 
命令功能 
该命令用于修改MME特定Diameter业务控制配置。当需要修改MP进程每秒到Diameter局向最大鉴权业务数目，或MP进程每秒到Diameter局向最大位置更新业务数目时，使用该命令。
注意事项 
该修改命令中MP进程每秒到Diameter局向最大鉴权业务数目或MP进程每秒到Diameter局向最大位置更新业务数目若设置为65535，则表示不对其进行控制。
参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向的局向ID。要求全局唯一。局向ID的查询命令参见SHOW DIAMADJ。
DIAMAUTHNUM|每进程每秒到Diameter局向最大鉴权业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于限制MP进程每秒向Diameter局向发送的鉴权业务数。默认值为65535，表示不对其进行控制。
DIAMLUNUM|每进程每秒到Diameter局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于限制MP进程每秒向Diameter局向发送的位置更新业务数。默认值为65535，表示不对其进行控制。
命令举例 
修改MMEDiameter局向ID为1下的业务控制配置，MP进程每秒到Diameter局向最大鉴权业务数目改为200，MP进程每秒到Diameter局向最大位置更新业务数目改为300。
SET MME DIAMETER SERVICE MAXIMUM:ADJID=1,DIAMAUTHNUM=200,DIAMLUNUM=300; 
父主题： [MME特定Diameter业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 删除MME特定Diameter业务控制(DEL MME DIAMETER SERVICE MAXIMUM) 
###### 删除MME特定Diameter业务控制(DEL MME DIAMETER SERVICE MAXIMUM) 
命令功能 
该命令用于删除MME特定Diameter业务控制配置。 
当该Diameter局向不采用特定配置，而直接采用MME通用业务控制配置中进行控制时，使用该命令。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向的局向ID。要求全局唯一。局向ID的查询命令参见SHOW DIAMADJ。
命令举例 
删除局向ID为1的MME特定Diameter业务控制配置。
DEL MME DIAMETER SERVICE MAXIMUM:ADJID=1; 
父主题： [MME特定Diameter业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询MME特定Diameter业务控制(SHOW MME DIAMETER SERVICE MAXIMUM) 
###### 查询MME特定Diameter业务控制(SHOW MME DIAMETER SERVICE MAXIMUM) 
命令功能 
该命令用于查询MME特定Diameter业务控制配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~4224。|该参数用于指定Diameter局向的局向ID。要求全局唯一。局向ID的查询命令参见SHOW DIAMADJ。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ADJID|局向ID|参数可选性:任选参数；参数类型:整数。|该参数用于指定Diameter局向的局向ID。要求全局唯一。局向ID的查询命令参见SHOW DIAMADJ。
DIAMAUTHNUM|每进程每秒到Diameter局向最大鉴权业务数目|参数可选性:任选参数；参数类型:整数。|该参数用于限制MP进程每秒向Diameter局向发送的鉴权业务数。默认值为65535，表示不对其进行控制。
DIAMLUNUM|每进程每秒到Diameter局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数。|该参数用于限制MP进程每秒向Diameter局向发送的位置更新业务数。默认值为65535，表示不对其进行控制。
命令举例 
查询局向ID为1的MME特定Diameter业务控制配置。
SHOW MME DIAMETER SERVICE MAXIMUM:ADJID=1; 
`
命令 (No.1): SHOW MME DIAMETER SERVICE MAXIMUM:ADJID=1;
操作维护         局向ID   MP进程每秒到Diameter局向最大鉴权业务数目   MP进程每秒到Diameter局向最大位置更新业务数目
-------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1        200                                          300
-------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
 ` 
父主题： [MME特定Diameter业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### MME特定VLR局向业务控制配置 
##### MME特定VLR局向业务控制配置 
背景知识 
过负荷控制是避免网元出现CPU或信令拥塞而采取的一种保护手段。 
本配置主要是控制到特定VLR网元发送的消息数来避免对端网元因短时间收到大量消息冲击而出现过负荷的情况。 
功能描述 
                本配置项针对特定的VLR局向设置出向业务控制，保护对端MSC/VLR网元，避免MSC/VLR短时间内收到来自MME的大量的位置更新或起呼短消息导致CPU负荷过高等。如果该VLR局向没有配置特定VLR局向业务控制时，采用“
                [SET MME SERVICE CONTROL]
                ”命令中配置的默认VLR局向控制参数。
            
相关主题 
 
新增MME特定VLR局向业务控制配置(ADD MOLVLR)
 
 
修改MME特定VLR局向业务控制配置(SET MOLVLR)
 
 
删除MME特定VLR局向业务控制配置(DEL MOLVLR)
 
 
查询MME特定VLR局向业务控制配置(SHOW MOLVLR)
 
 
父主题： [MME业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 新增MME特定VLR局向业务控制配置(ADD MOLVLR) 
###### 新增MME特定VLR局向业务控制配置(ADD MOLVLR) 
命令功能 
该命令用于增加MME特定VLR局向业务控制配置。当过负荷控制对某个VLR局向不采用MME通用业务控制配置来控制业务，而是需要对该局向进行特殊配置来控制业务时，使用该命令。 
该命令执行成功后，MME根据配置规则实现业务控制，主要包括控制MP进程每秒到VLR局向最大位置更新业务数目和MP进程每秒到VLR局向最大起呼短消息业务数目。 
注意事项 
该配置命令中MP进程每秒到VLR局向最大位置更新业务数目和MP进程每秒到VLR局向最大起呼短消息业务数目若设置为65535，则表示不对其进行控制。 
配置该命令前，首先要新增SGs口VLR局向配置。配置命令参见[ADD VLROFFICE]进行配置。
参数说明 
标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示特定的VLR局向标识。
VLRLUNUM|每进程每秒到VLR局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:65535。|该参数用于限制MP进程每秒向VLR局向发送的位置更新业务数。默认值为65535，表示不对其进行控制。
VLRMOSMSNUM|每进程每秒到VLR局向最大起呼短消息业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:65535。|该参数用于限制MP进程每秒向VLR局向发送的起呼短消息业务数。默认值为65535，表示不对其进行控制。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。
命令举例 
新增MME特定VLR局向业务控制配置，其中VLR局向标识为1，MP进程每秒到VLR局向最大位置更新业务数目为10000，MP进程每秒到VLR局向最大起呼短消息业务数目为10000。 
ADD MOLVLR:VLROFFICEID=1,VLRLUNUM=10000,VLRMOSMSNUM=10000; 
父主题： [MME特定VLR局向业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 修改MME特定VLR局向业务控制配置(SET MOLVLR) 
###### 修改MME特定VLR局向业务控制配置(SET MOLVLR) 
命令功能 
该命令用于修改MME特定VLR局向业务控制配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示特定的VLR局向标识。
VLRLUNUM|每进程每秒到VLR局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于限制MP进程每秒向VLR局向发送的位置更新业务数。默认值为65535，表示不对其进行控制。
VLRMOSMSNUM|每进程每秒到VLR局向最大起呼短消息业务数目|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于限制MP进程每秒向VLR局向发送的起呼短消息业务数。默认值为65535，表示不对其进行控制。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。
命令举例 
修改VLR局向标识为1的配置数据，将MP进程每秒到VLR局向最大位置更新业务数目修改为5000。 
SET MOLVLR:VLROFFICEID=1,VLRLUNUM=5000; 
父主题： [MME特定VLR局向业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 删除MME特定VLR局向业务控制配置(DEL MOLVLR) 
###### 删除MME特定VLR局向业务控制配置(DEL MOLVLR) 
命令功能 
该命令用于删除MME特定VLR局向业务控制配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示特定的VLR局向标识。
命令举例 
删除VLR局向标识为1的配置数据。 
DEL MOLVLR:VLROFFICEID=1; 
父主题： [MME特定VLR局向业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询MME特定VLR局向业务控制配置(SHOW MOLVLR) 
###### 查询MME特定VLR局向业务控制配置(SHOW MOLVLR) 
命令功能 
该命令用于查询MME特定VLR局向业务控制配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于指示特定的VLR局向标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
VLROFFICEID|VLR局向标识|参数可选性:任选参数；参数类型:整数。|该参数用于指示特定的VLR局向标识。
VLRLUNUM|每进程每秒到VLR局向最大位置更新业务数目|参数可选性:任选参数；参数类型:整数。|该参数用于限制MP进程每秒向VLR局向发送的位置更新业务数。默认值为65535，表示不对其进行控制。
VLRMOSMSNUM|每进程每秒到VLR局向最大起呼短消息业务数目|参数可选性:任选参数；参数类型:整数。|该参数用于限制MP进程每秒向VLR局向发送的起呼短消息业务数。默认值为65535，表示不对其进行控制。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|对此配置进行维护记录，起备注作用。
命令举例 
查询所有的MME特定VLR局向业务控制配置 
SHOW MOLVLR; 
`
命令 (No.74): SHOW MOLVLR
操作维护      VLR局向标识 MP进程每秒到VLR局向最大位置更新业务数目 MP进程每秒到VLR局向最大起呼短消息业务数目 用户别名 
-------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1             5000                                     10000  
-------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.04 秒）。
` 
父主题： [MME特定VLR局向业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### MME自动业务控制策略配置 
##### MME自动业务控制策略配置 
背景知识 
本功能根据业务成功率来评判当前系统中是否存在拥塞，通过限制接入的业务量，保证整个系统的业务正常。 
MME自动业务控制策略配置功能是指MME的周边网元（HSS\SGW\MSC等）存在过载风险时，MME根据周边网元返回的业务成功率的周期变化，判断周边网元的负荷拥塞情况，控制入向业务速率的方式来保护周边网元，通过调节Attach、Inter-MME TAU、跨RAT TAU流程的处理速率，控制向周边网元发往的请求数，从而保护周边网元的目的。 
功能描述 
此命令用于设置统一ALC（Auto Load Control）流控功能的相关参数。当由于系统升级、故障、业务大量涌入等情况导致S11、S6a、SGs接口出现拥塞时，可以通过开启此功能来保护周边网元。 
MME根据周边网元返回的业务成功率的周期变化，判断周边网元的负荷拥塞情况，通过调节Attach、Inter-MME TAU、跨RAT TAU等业务流程的处理速率，控制向周边网元发往的请求数，从而保护周边网元的目的。 
相关主题 
 
设置MME自动业务控制基本参数(SET MME AUTOCTL BASIC PARA)
 
 
查询MME自动业务控制基本参数(SHOW MME AUTOCTL BASIC PARA)
 
 
设置S6a统一ALC流控策略(SET MME AUTO CNGCTL)
 
 
查询S6a统一ALC流控策略(SHOW MME AUTO CNGCTL)
 
 
设置S11统一ALC流控策略(SET S11 ALCPLY)
 
 
查询S11统一ALC流控策略(SHOW S11 ALCPLY)
 
 
设置SGS统一ALC流控策略(SET SGS ALCPLY)
 
 
查询SGS统一ALC流控策略(SHOW SGS ALCPLY)
 
 
父主题： [MME业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置MME自动业务控制基本参数(SET MME AUTOCTL BASIC PARA) 
###### 设置MME自动业务控制基本参数(SET MME AUTOCTL BASIC PARA) 
命令功能 
该命令用于设置MME自动业务控制基本参数，包括: 控制周期、评判周期等，从而控制向周边网元发往的请求数，达到保护周边网元的目的。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CTRLTIMER|业务控制周期(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于配置MME自动业务控制控制算法时计算业务通过数的周期（时间段），单位是100毫秒。
JUDGETIMER|评判周期/业务控制周期|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于配置评判周期时长，即MME自动识别周边网元拥塞控制时，动态调整当前允许通过业务数的频率。说明：评判周期配置采用的是MME自动业务控制周期的倍数，即100毫秒的倍数。
ISLOG|拥塞控制时是否上报日志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制在统一ALC流控时是否上报日志。
HSSSUCCRATEWITHNOR|hss成功率统计包含NOR/NOA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于当计算HSS成功率时，是否包含NOR/NOA消息。
HSSSUCCRATEWITHPUR|hss成功率统计包含PUR/PUA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于当计算HSS成功率时，是否包含PUR/PUA消息。
SUCCRATENOCON|周边网元无过载成功率（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置周边网元无拥塞，系统流畅时，业务的成功率。周边网元（HSS、SGW、VLR）统一设置。
REDUCRATECLOSETOCON|临过载时向上步长缩减比例（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于当周边网元业务成功率高于配置门限，且低于“周边网元无拥塞成功率”时，同时系统临近过载，在向上增加放通率时，按照配置的步长和本参数设置的比例，设置实际增加的步长。
TOKENBKTRADIO|允许业务突发系数（%）|参数可选性:任选参数；参数类型:整数；参数范围为:100~500。|该参数用于当进行统一ALC动态流控时，在控制周期内S1口收到Attach/局间TAU/跨RAT TAU业务的突发系数。以百分比为单位。如：允许业务突发系数设置为150，控制周期内平均放通速率为20个/秒.控制周期内突发放通速率为= 20 × 150%= 30个/秒
命令举例 
设置MME自动业务控制基本参数，其中业务控制周期(100ms)为10，评判周期/业务控制周期为10，拥塞控制时是否上报日志为是，hss成功率统计包含NOR/NOA为是，hss成功率统计包含PUR/PUA为是，周边网元无过载成功率（%）为10，临过载时向上步长缩减比例（%）为10，允许业务突发系数（%）为100。 
SET MME AUTOCTL BASIC PARA:CTRLTIMER=10,JUDGETIMER=10,ISLOG="YES",HSSSUCCRATEWITHNOR="YES",HSSSUCCRATEWITHPUR="YES",SUCCRATENOCON=10,REDUCRATECLOSETOCON=10,TOKENBKTRADIO=100 
父主题： [MME自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询MME自动业务控制基本参数(SHOW MME AUTOCTL BASIC PARA) 
###### 查询MME自动业务控制基本参数(SHOW MME AUTOCTL BASIC PARA) 
命令功能 
该命令用于查询MME自动业务控制基本参数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CTRLTIMER|业务控制周期(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置MME自动业务控制控制算法时计算业务通过数的周期（时间段），单位是100毫秒。
JUDGETIMER|评判周期/业务控制周期|参数可选性:任选参数；参数类型:整数。|该参数用于配置评判周期时长，即MME自动识别周边网元拥塞控制时，动态调整当前允许通过业务数的频率。说明：评判周期配置采用的是MME自动业务控制周期的倍数，即100毫秒的倍数。
ISLOG|拥塞控制时是否上报日志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于控制在统一ALC流控时是否上报日志。
HSSSUCCRATEWITHNOR|hss成功率统计包含NOR/NOA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于当计算HSS成功率时，是否包含NOR/NOA消息。
HSSSUCCRATEWITHPUR|hss成功率统计包含PUR/PUA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于当计算HSS成功率时，是否包含PUR/PUA消息。
SUCCRATENOCON|周边网元无过载成功率（%）|参数可选性:任选参数；参数类型:整数。|该参数用于设置周边网元无拥塞，系统流畅时，业务的成功率。周边网元（HSS、SGW、VLR）统一设置。
REDUCRATECLOSETOCON|临过载时向上步长缩减比例（%）|参数可选性:任选参数；参数类型:整数。|该参数用于当周边网元业务成功率高于配置门限，且低于“周边网元无拥塞成功率”时，同时系统临近过载，在向上增加放通率时，按照配置的步长和本参数设置的比例，设置实际增加的步长。
TOKENBKTRADIO|允许业务突发系数（%）|参数可选性:任选参数；参数类型:整数。|该参数用于当进行统一ALC动态流控时，在控制周期内S1口收到Attach/局间TAU/跨RAT TAU业务的突发系数。以百分比为单位。如：允许业务突发系数设置为150，控制周期内平均放通速率为20个/秒.控制周期内突发放通速率为= 20 × 150%= 30个/秒
命令举例 
查询MME自动业务控制基本参数。 
SHOW MME AUTOCTL BASIC PARA 
`
命令 (No.1): SHOW MME AUTOCTL BASIC PARA
操作维护       业务控制周期(100ms) 评判周期/业务控制周期  拥塞控制时是否上报日志 hss成功率统计包含NOR/NOA hss成功率统计包含PUR/PUA 周边网元无过载成功率（%） 临过载时向上步长缩减比例（%） 允许业务突发系数（%） 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           10                  15           否                     是                       是                       95                        100                           100                        
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-15 14:39:20 耗时: 2.075秒
` 
父主题： [MME自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置S6a统一ALC流控策略(SET MME AUTO CNGCTL) 
###### 设置S6a统一ALC流控策略(SET MME AUTO CNGCTL) 
命令功能 
该命令用于设置S6a接口局向统一ALC业务流控策略。当运营商要求对S6a接口所有的HSS局向进行统一ALC流控时，使用此命令。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
FLG|是否开启|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关。
STARTCAPS|触发拥塞的接入业务通过数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，即使HSS成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:2~600。|本SC每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的业务成功率(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|一旦业务成功率降低（低于成功门限），且接入本SC的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
命令举例 
设置S6a统一ALC流控策略，其中是否开启设置为是，触发拥塞的接入业务通过数量(单SC每秒)为20，允许通过的接入业务最大数量(单SC每秒)为60，触发拥塞的HSS业务成功率(%)为85，接入业务控制步长为4，控制持续时间(分钟)为30。 
SET MME AUTO CNGCTL:FLG="YES",STARTCAPS=20,MAXCAPS=60,SUCCRATE=85,STEP=4,LASTTIME=30 
父主题： [MME自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询S6a统一ALC流控策略(SHOW MME AUTO CNGCTL) 
###### 查询S6a统一ALC流控策略(SHOW MME AUTO CNGCTL) 
命令功能 
该命令用于查询S6a口局向统一ALC业务流控策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FLG|是否开启|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关。
STARTCAPS|触发拥塞的接入业务通过数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，即使HSS成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|本SC每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的业务成功率(%)|参数可选性:任选参数；参数类型:整数。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数。|一旦业务成功率降低（低于成功门限），且接入本SC的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
命令举例 
查询S6a统一ALC流控策略。 
SHOW MME AUTO CNGCTL 
`
命令 (No.1): SHOW MME AUTO CNGCTL
操作维护   是否开启   触发拥塞的接入业务通过数量(单SC每秒)   初始限制的接入业务最大数量(单SC每秒) 允许通过的接入业务最大数量(单SC每秒)   触发拥塞的HSS业务成功率(%)   接入业务控制步长   控制持续时间(分钟)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改       是         20                                       50                                     60                                       85                           4                  30 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [MME自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置S11统一ALC流控策略(SET S11 ALCPLY) 
###### 设置S11统一ALC流控策略(SET S11 ALCPLY) 
命令功能 
根据此命令设置S11口局向统一ALC业务流控策略，当运营商要求对S11接口所有的SGW局向进行统一ALC流控时，使用此命令设置流控参数。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
FLG|是否开启|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关。 根据此参数设置是否支持S11接口的统一ALC流控。
STARTCAPS|触发拥塞的接入业务通过数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，即使成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:2~600。|本SC每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的业务成功率(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|一旦业务成功率降低（低于成功门限），且接入本SC的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
命令举例 
设置S11统一ALC流控策略，其中是否开启设置为是，触发拥塞的接入业务通过数量(单SC每秒)为20，允许通过的接入业务最大数量(单SC每秒)为60，触发拥塞的HSS业务成功率(%)为85，接入业务控制步长为4，控制持续时间(分钟)为30。 
SET S11 ALCPLY:FLG="YES",STARTCAPS=20,MAXCAPS=60,SUCCRATE=85,STEP=4,LASTTIME=30 
父主题： [MME自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询S11统一ALC流控策略(SHOW S11 ALCPLY) 
###### 查询S11统一ALC流控策略(SHOW S11 ALCPLY) 
命令功能 
根据此命令查询S11口局向统一ALC业务流控策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FLG|是否开启|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关。 根据此参数设置是否支持S11接口的统一ALC流控。
STARTCAPS|触发拥塞的接入业务通过数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，即使成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|本SC每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的业务成功率(%)|参数可选性:任选参数；参数类型:整数。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数。|一旦业务成功率降低（低于成功门限），且接入本SC的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
命令举例 
查询S11统一ALC流控策略。 
SHOW S11 ALCPLYL 
`
(No.4) : SHOW S11 ALCPLY:
-----------------NFS_MMESGSN_0----------------
操作维护       是否开启 触发拥塞的接入业务通过数量(单SC每秒) 初始限制的接入业务最大数量(单SC每秒) 允许通过的接入业务最大数量(单SC每秒) 触发拥塞的HSS业务成功率(%) 接入业务控制步长 控制持续时间(分钟) 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           是       20                                     50                                     60                                     85                         5                5                  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-11-26 14:54:27 耗时: 0.223 秒
` 
父主题： [MME自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置SGS统一ALC流控策略(SET SGS ALCPLY) 
###### 设置SGS统一ALC流控策略(SET SGS ALCPLY) 
命令功能 
根据此命令设置SGS口局向统一ALC业务流控策略，当运营商要求对SGS接口所有的SGW局向进行统一ALC流控时，使用此命令设置流控参数。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
FLG|是否开启|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关。 根据此参数设置是否支持SGS接口的统一ALC流控。
STARTCAPS|触发拥塞的接入业务通过数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在本SC，每秒的业务（联合Attach/联合TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在本SC，每秒的业务（联合Attach/联合TAU）数量超过配置的值时，即使成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:2~600。|本SC每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的业务成功率(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|一旦业务成功率降低（低于成功门限），且接入本SC的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
命令举例 
设置SGS统一ALC流控策略，其中是否开启设置为是，触发拥塞的接入业务通过数量(单SC每秒)为20，允许通过的接入业务最大数量(单SC每秒)为60，触发拥塞的HSS业务成功率(%)为85，接入业务控制步长为4，控制持续时间(分钟)为30。 
SET SGS ALCPLY:FLG="YES",STARTCAPS=20,MAXCAPS=60,SUCCRATE=85,STEP=4,LASTTIME=30 
父主题： [MME自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询SGS统一ALC流控策略(SHOW SGS ALCPLY) 
###### 查询SGS统一ALC流控策略(SHOW SGS ALCPLY) 
命令功能 
根据此命令查询SGS口局向统一ALC业务流控策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FLG|是否开启|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|功能开关。 根据此参数设置是否支持SGS接口的统一ALC流控。
STARTCAPS|触发拥塞的接入业务通过数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|只有在本SC，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，即使HSS成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单SC每秒)|参数可选性:任选参数；参数类型:整数。|本SC每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的业务成功率(%)|参数可选性:任选参数；参数类型:整数。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数。|一旦业务成功率降低（低于成功门限），且接入本SC的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
命令举例 
查询SGS统一ALC流控策略。 
SHOW SGS ALCPLY 
`
(No.5) : SHOW SGS ALCPLY:
-----------------NFS_MMESGSN_0----------------
操作维护       是否开启 触发拥塞的接入业务通过数量(单SC每秒) 初始限制的接入业务最大数量(单SC每秒) 允许通过的接入业务最大数量(单SC每秒) 触发拥塞的HSS业务成功率(%) 接入业务控制步长 控制持续时间(分钟) 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           是       20                                     50                                     60                                     85                         5                5                  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-11-26 14:54:48 耗时: 0.214 秒
` 
父主题： [MME自动业务控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### S6a ALC局向流控策略配置 
##### S6a ALC局向流控策略配置 
背景知识 
随着网络用户和业务不断增加，uMAC系统各周边接口和网元拥塞的可能性增加，另外，由于系统升级、系统故障、大型节假日、容灾等场景，会导致大量用户涌入MME，MME对周边网元HSS的消息量也会急剧增加，极易造成HSS的负荷拥塞。 
为了保证用户接通率、改善用户体验，防止HSS拥塞，需要周边HSS网元继续局向自动业务控制，保护周边网元。 
S6a接口局向自动业务控制功能是指MME的周边HSS网元存在过载风险时，MME能够基于周边HSS网元返回成功应答数的周期变化自动调节Attach、Inter TAU、Inter RAT Intra TAU流程的处理速率，从而控制向周边HSS网元发送的请求数，达到保护周边HSS网元的目的。 
功能描述 
本功能是根据业务成功率来评判当前系统中是否存在S6a接口网元拥塞，通过限制接入的业务量，保证MME和周边网元HSS的安全，保护HSS网元。 
此命令用于设置S6a接口ALC局向流控策略参数。系统对HSS网元进行分局向控制，根据配置将用户归属于具体的HSS ALC流控局向，针对具体的ALC局向进行分局向流控，从而保护对应的HSS网元免于拥塞。 
相关主题 
 
新增S6a ALC局向流控策略配置(ADD S6A ALCOFC POLICY)
 
 
修改S6a ALC局向流控策略配置(SET S6A ALCOFC POLICY)
 
 
删除S6a ALC局向流控策略配置(DEL S6A ALCOFC POLICY)
 
 
查询S6a ALC局向流控策略配置(SHOW S6A ALCOFC POLICY)
 
 
父主题： [MME业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 新增S6a ALC局向流控策略配置(ADD S6A ALCOFC POLICY) 
###### 新增S6a ALC局向流控策略配置(ADD S6A ALCOFC POLICY) 
命令功能 
此命令用于新增S6a接口ALC局向流控策略配置。在根据HOST解析转发的组网配置下，只有DRA对MME逻辑上可见，HSS目的实体对MME逻辑上不可见，所以需要用户手动配置，对自动业务控制的HSS局向进行区分，以保证准确的自动业务控制对象，避免错误控制。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OFCIDX|局向索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~10。|该参数用于设置S6a ALC局向索引。
OFCNAME|局向名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于设置S6a ALC局向名称。
OFCAUTOCTLSWITCH|局向流控开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置局向流控开关。
STARTCAPS|触发拥塞的接入业务通过数量(单进程每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。默认值:20。|只有在本进程，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单进程每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。默认值:50。|只有在本进程，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，即使HSS成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单进程每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:2~600。默认值:300。|本进程每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的HSS业务成功率(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。默认值:80。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:5。|一旦业务成功率降低（低于成功门限），且接入本进程的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:5。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
EXCLUDEERRCODE|被排除的S6a错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在计算S6a接口业务成功率时，HSS返回的部分错误码不是HSS原因造成的，应该不被统计。该参数标识具体的不是HSS原因的错误码。
命令举例 
新增S6a ALC局向流控策略配置，其中局向索引为1，局向名称为OFC_1。 
ADD S6A ALCOFC POLICY:OFCIDX=1,OFCNAME="OFC_1"; 
父主题： [S6a ALC局向流控策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 修改S6a ALC局向流控策略配置(SET S6A ALCOFC POLICY) 
###### 修改S6a ALC局向流控策略配置(SET S6A ALCOFC POLICY) 
命令功能 
此命令用于修改S6a接口ALC局向流控策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OFCIDX|局向索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~10。|该参数用于设置S6a ALC局向索引。
OFCNAME|局向名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~128个字符。|该参数用于设置S6a ALC局向名称。
OFCAUTOCTLSWITCH|局向流控开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置局向流控开关。
STARTCAPS|触发拥塞的接入业务通过数量(单进程每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在本进程，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单进程每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|只有在本进程，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，即使HSS成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单进程每秒)|参数可选性:任选参数；参数类型:整数；参数范围为:2~600。|本进程每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的HSS业务成功率(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|一旦业务成功率降低（低于成功门限），且接入本进程的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
EXCLUDEERRCODE|被排除的S6a错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在计算S6a接口业务成功率时，HSS返回的部分错误码不是HSS原因造成的，应该不被统计。该参数标识具体的不是HSS原因的错误码。
命令举例 
修改局向索引为1的S6a ALC局向流控策略配置，将局向流控开关修改为YES。 
SET S6A ALCOFC POLICY:OFCIDX=1,OFCAUTOCTLSWITCH="YES"; 
父主题： [S6a ALC局向流控策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 删除S6a ALC局向流控策略配置(DEL S6A ALCOFC POLICY) 
###### 删除S6a ALC局向流控策略配置(DEL S6A ALCOFC POLICY) 
命令功能 
此命令用于删除S6a接口ALC局向流控策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OFCIDX|局向索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~10。|该参数用于设置S6a ALC局向索引。
命令举例 
删除局向索引为1的S6a ALC局向流控策略配置。 
DEL S6A ALCOFC POLICY:OFCIDX=1; 
父主题： [S6a ALC局向流控策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询S6a ALC局向流控策略配置(SHOW S6A ALCOFC POLICY) 
###### 查询S6a ALC局向流控策略配置(SHOW S6A ALCOFC POLICY) 
命令功能 
此命令用于查询S6a接口ALC局向流控策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OFCIDX|局向索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该参数用于设置S6a ALC局向索引。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OFCIDX|局向索引|参数可选性:任选参数；参数类型:整数。|该参数用于设置S6a ALC局向索引。
OFCNAME|局向名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置S6a ALC局向名称。
OFCAUTOCTLSWITCH|局向流控开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置局向流控开关。
STARTCAPS|触发拥塞的接入业务通过数量(单进程每秒)|参数可选性:任选参数；参数类型:整数。|只有在本进程，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，才可能会触发本功能。即如果业务量过低是不被控制的。
LIMTCAPS|初始限制的接入业务最大数量(单进程每秒)|参数可选性:任选参数；参数类型:整数。|只有在本进程，每秒的业务（Attach/局间TAU/跨RAT TAU）数量超过配置的值时，即使HSS成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
MAXCAPS|允许通过的接入业务最大数量(单进程每秒)|参数可选性:任选参数；参数类型:整数。|本进程每秒最多允许通过的业务数量。
SUCCRATE|触发拥塞的HSS业务成功率(%)|参数可选性:任选参数；参数类型:整数。|只有在业务成功率低于本配置时，才可能会触发本功能，即业务如果是一直成功的，也不会被控制。
STEP|接入业务控制步长|参数可选性:任选参数；参数类型:整数。|一旦业务成功率降低（低于成功门限），且接入本进程的业务数也很高（高于业务门限），就会触发控制功能。 如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
LASTTIME|控制持续时间(分钟)|参数可选性:任选参数；参数类型:整数。|在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
EXCLUDEERRCODE|被排除的S6a错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在计算S6a接口业务成功率时，HSS返回的部分错误码不是HSS原因造成的，应该不被统计。该参数标识具体的不是HSS原因的错误码。
命令举例 
查询S6a ALC局向流控策略配置。 
SHOW S6A ALCOFC POLICY; 
`
命令 (No.5) : SHOW S6A ALCOFC POLICY:
-----------------uMAC_MME_V7master/NFS_MMESGSN_0----------------
操作维护       局向索引 局向名称 局向流控开关 触发拥塞的接入业务通过数量(单进程每秒) 初始限制的接入业务最大数量(单进程每秒) 允许通过的接入业务最大数量(单进程每秒) 触发拥塞的HSS业务成功率(%) 接入业务控制步长 控制持续时间(分钟) 被排除的S6a错误码                                                                                                                                               
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1        LAI001   否           20                                     50                                     300                                    80                         5                5                  DIAMETER_ERROR_USER_UNKNOWN (5001) & DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION (5420), without Error Diagnostic, or with Error Diagnostic of GPRS_DATA_SUBSCRIBED 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-02-24 10:42:50 耗时: 0.934秒
` 
父主题： [S6a ALC局向流控策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### S6a ALC局向IMSI号段配置 
##### S6a ALC局向IMSI号段配置 
背景知识 
随着网络用户和业务不断增加，uMAC系统各周边接口和网元拥塞的可能性增加，另外，由于系统升级、系统故障、大型节假日、容灾等场景，会导致大量用户涌入MME，MME对周边网元HSS的消息量也会急剧增加，极易造成HSS的负荷拥塞。 
为了保证用户接通率、改善用户体验，防止HSS拥塞，需要周边HSS网元继续局向自动业务控制，保护周边网元。 
S6a接口自动业务控制功能是指MME的周边HSS网元存在过载风险时，MME能够基于周边HSS网元返回成功应答数的周期变化自动调节Attach、Inter TAU、Inter RAT Intra TAU流程的处理速率，从而控制向周边HSS网元发送的请求数，达到保护周边HSS网元的目的。 
功能描述 
该命令用于设置S6a接口ALC局向关联的IMSI号段。MME在进行S6a ALC局向流控过程中，根据用户IMSI在此配置数据中查找，如果用户归属于一个ALC局向，那么MME根据具体ALC局向的业务成功率进行自动流控，保障周边网元指定的ALC局向的通畅。 
相关主题 
 
新增S6a ALC局向IMSI号段配置(ADD S6A ALCOFC IMSICFG)
 
 
修改S6a ALC局向IMSI号段配置(SET S6A ALCOFC IMSICFG)
 
 
删除S6a ALC局向IMSI号段配置(DEL S6A ALCOFC IMSICFG)
 
 
查询S6a ALC局向IMSI号段配置(SHOW S6A ALCOFC IMSICFG)
 
 
父主题： [MME业务控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 新增S6a ALC局向IMSI号段配置(ADD S6A ALCOFC IMSICFG) 
###### 新增S6a ALC局向IMSI号段配置(ADD S6A ALCOFC IMSICFG) 
命令功能 
该命令用于新增一个S6a接口ALC局向关联的IMSI号段。 
注意事项 
只有当"S6a ALC局向"配置表中“局向索引”对应的“局向流控开关”为“YES”时，本命令所配置的各个IMSI号段才进行流控。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
OFCIDX|局向索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~10。|该参数用于设置S6a ALC局向索引。
命令举例 
新增S6a ALC局向IMSI号段配置，其中IMSI为"46012"，局向索引为1。 
ADD S6A ALCOFC IMSICFG:IMSI="46012",OFCIDX=1; 
父主题： [S6a ALC局向IMSI号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 修改S6a ALC局向IMSI号段配置(SET S6A ALCOFC IMSICFG) 
###### 修改S6a ALC局向IMSI号段配置(SET S6A ALCOFC IMSICFG) 
命令功能 
该命令用于修改一个S6a接口ALC局向关联的IMSI号段。 
注意事项 
只有当"S6a ALC局向"配置表中“局向索引”对应的“局向流控开关”为“YES”时，本命令所配置的各个IMSI号段才进行流控。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
OFCIDX|局向索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该参数用于设置S6a ALC局向索引。
命令举例 
修改IMSI为"46012"的S6a ALC局向IMSI号段配置，将局向索引修改为2。 
SET S6A ALCOFC IMSICFG:IMSI="46012",OFCIDX=2; 
父主题： [S6a ALC局向IMSI号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 删除S6a ALC局向IMSI号段配置(DEL S6A ALCOFC IMSICFG) 
###### 删除S6a ALC局向IMSI号段配置(DEL S6A ALCOFC IMSICFG) 
命令功能 
该命令用于删除一个S6a接口ALC局向关联的IMSI号段。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
命令举例 
删除IMSI为"46012"的S6a ALC局向IMSI号段配置。 
DEL S6A ALCOFC IMSICFG:IMSI="46012"; 
父主题： [S6a ALC局向IMSI号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询S6a ALC局向IMSI号段配置(SHOW S6A ALCOFC IMSICFG) 
###### 查询S6a ALC局向IMSI号段配置(SHOW S6A ALCOFC IMSICFG) 
命令功能 
该命令用于查询S6a接口ALC局向关联的IMSI号段。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于设置IMSI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|该参数用于设置IMSI号段。
OFCIDX|局向索引|参数可选性:任选参数；参数类型:整数。|该参数用于设置S6a ALC局向索引。
命令举例 
查询S6a ALC局向IMSI号段配置。 
SHOW S6A  ALCOFC IMSICFG; 
`
命令 (No.1): SHOW S6A  ALCOFC IMSICFG
操作维护         IMSI   局向索引
--------------------------------
复制 修改 删除   46012  1
--------------------------------
记录数：1
命令执行成功（耗时 0.042 秒）。
` 
父主题： [S6a ALC局向IMSI号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### UE无关的网元消息控制配置 
#### UE无关的网元消息控制配置 
背景知识 
在SGSN/MME网元处理的消息中，有一部分是与签约用户无关的管理类消息和中继消息，如果这类消息过多，也会导致网元过负荷。 
功能描述 
在SGSN/MME网元处理的消息中，有一部分是与签约用户无关的管理类消息和中继消息，其中有些消息可能引起网元负荷冲高，因而需要加以负荷控制，每秒超过此门限的报文将被丢弃。 
相关主题 
 
设置UE无关的网元消息控制(SET UEINDMSG CTRL)
 
 
查询UE无关的网元消息控制(SHOW UEINDMSG CTRL)
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置UE无关的网元消息控制(SET UEINDMSG CTRL) 
##### 设置UE无关的网元消息控制(SET UEINDMSG CTRL) 
命令功能 
该命令用于设置UE无关的网元消息控制。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CFGTRANSNUM|每秒许可的入向配置传输消息数|参数可选性:任选参数；参数类型:整数；参数范围为:20~2000。|当进程内S1口或S10口在1秒内收到的eNB Configuration Transfer消息或Configuration Transfer Tunnel请求消息超过该门限时，多余的消息将被丢弃。S1口和S10口的消息独立计数。
命令举例 
将于UE无关的每秒许可的入向配置传输消息数设置为20。 
SET UEINDMSG CTRL:CFGTRANSNUM="20"; 
父主题： [UE无关的网元消息控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询UE无关的网元消息控制(SHOW UEINDMSG CTRL) 
##### 查询UE无关的网元消息控制(SHOW UEINDMSG CTRL) 
命令功能 
该命令用于查询UE无关的网元消息控制配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CFGTRANSNUM|每秒许可的入向配置传输消息数|参数可选性:任选参数；参数类型:整数。|当进程内S1口或S10口在1秒内收到的eNB Configuration Transfer消息或Configuration Transfer Tunnel请求消息超过该门限时，多余的消息将被丢弃。S1口和S10口的消息独立计数。
命令举例 
查询UE无关的网元消息控制。 
SHOW UEINDMSG CTRL; 
`
命令 (No.1): SHOW UEINDMSG CTRL
操作维护  每秒许可的入向配置传输消息数
--------------------------------------
修改      200
--------------------------------------
记录数 1
命令执行成功（耗时 0.064 秒）。
` 
父主题： [UE无关的网元消息控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 业务类型过负荷控制配置 
#### 业务类型过负荷控制配置 
背景知识 
过负荷控制功能指的是通过限制本网元接入的业务量，降低本网元或者邻接网元的负荷，避免因负荷过高导致本网元或者邻接网元设备异常或崩溃。 
由于语音业务的优先级高，在系统出现过负荷时，将语音相关业务（CSFB、VOLTE）作为高优先级业务，避免语音业务被限制。 
功能描述 
本功能用于在系统出现过负荷，将语音相关业务（CSFB、VOLTE）作为高优先级业务，避免语音业务被限制。 
相关主题 
 
设置业务类型过负荷控制(SET SERVICE TYPE OVERLOAD CONTROL)
 
 
查询业务类型过负荷控制(SHOW SERVICE TYPE OVERLOAD CONTROL)
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置业务类型过负荷控制(SET SERVICE TYPE OVERLOAD CONTROL) 
##### 设置业务类型过负荷控制(SET SERVICE TYPE OVERLOAD CONTROL) 
命令功能 
该命令用于设置是否开启过负荷时语音业务优先的功能。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPPORTVOICE|语音业务优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否开启过负荷时语音业务优先的功能。
命令举例 
开启过负荷时语音业务优先的功能。 
SET SERVICE TYPE OVERLOAD CONTROL:SUPPORTVOICE="ON"; 
父主题： [业务类型过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询业务类型过负荷控制(SHOW SERVICE TYPE OVERLOAD CONTROL) 
##### 查询业务类型过负荷控制(SHOW SERVICE TYPE OVERLOAD CONTROL) 
命令功能 
该命令用于查询是否开启过负荷时语音业务优先的功能。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPPORTVOICE|语音业务优先|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否开启过负荷时语音业务优先的功能。
命令举例 
查询是否开启过负荷时语音业务优先的功能。 
SHOW SERVICE TYPE OVERLOAD CONTROL; 
父主题： [业务类型过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### MME过负荷寻呼优化配置 
#### MME过负荷寻呼优化配置 
背景知识 
MME向每个被寻呼的eNodeB都要发送S1寻呼消息，寻呼的eNodeB个数越多，对MME的负荷冲击就越大。 
功能描述 
本功能用于当系统出现过负荷的情况下，MME通过优化寻呼使用的策略，减少寻呼次数和寻呼范围，达到减少系统负荷的目的。 
相关主题 
 
设置MME过负荷寻呼优化(SET MME OVERLOAD PAGING POLICY)
 
 
查询MME过负荷寻呼优化(SHOW MME OVERLOAD PAGING POLICY)
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置MME过负荷寻呼优化(SET MME OVERLOAD PAGING POLICY) 
##### 设置MME过负荷寻呼优化(SET MME OVERLOAD PAGING POLICY) 
命令功能 
该命令用于设置是否开启过负荷时优化寻呼过程的功能。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPPOLPAGINGOPTIMEZE|过负荷寻呼优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否开启过负荷时优化寻呼过程的功能。
OLPAGINGRANGE|过负荷时寻呼范围|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|
命令举例 
开启过负荷时优化寻呼过程的功能,寻呼范围为：最近活动eNB列表。 
SET MME OVERLOAD PAGING POLICY:SUPPOLPAGINGOPTIMEZE="ON",OLPAGINGRANGE="LASTACTENBLIST"; 
父主题： [MME过负荷寻呼优化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询MME过负荷寻呼优化(SHOW MME OVERLOAD PAGING POLICY) 
##### 查询MME过负荷寻呼优化(SHOW MME OVERLOAD PAGING POLICY) 
命令功能 
该命令用于查询是否开启过负荷时优化寻呼过程的功能。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPPOLPAGINGOPTIMEZE|过负荷寻呼优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否开启过负荷时优化寻呼过程的功能。
OLPAGINGRANGE|过负荷时寻呼范围|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|
命令举例 
查询是否开启过负荷时优化寻呼过程的功能。 
SHOW MME OVERLOAD PAGING POLICY; 
父主题： [MME过负荷寻呼优化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### MME接口消息控制配置 
#### MME接口消息控制配置 
背景知识 
MME通过限制各个逻辑接口的收发消息速率来避免本网元过负荷。 
功能描述 
MME支持控制各个逻辑接口的消息通过速率。 
相关主题 
 
设置MME接口消息控制配置(SET INTERFACE MSG OVERLOAD)
 
 
查询MME接口消息控制配置(SHOW INTERFACE MSG OVERLOAD)
 
 
父主题： [本网元拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置MME接口消息控制配置(SET INTERFACE MSG OVERLOAD) 
##### 设置MME接口消息控制配置(SET INTERFACE MSG OVERLOAD) 
命令功能 
本命令用于设置MME的各个逻辑接口的消息通过速率。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
S1RCV|S1接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S1接口的消息接收速率。
S1SND|S1接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S1接口的消息发送速率。
S6ARCV|S6a接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S6a接口的消息接收速率。
S6ASND|S6a接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S6a接口的消息发送速率。
S11RCV|S11接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S11接口的消息接收速率。
S11SND|S11接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S11接口的消息发送速率。
SGSRCV|SGs接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制SGs接口的消息接收速率。
SGSSND|SGs接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制SGs接口的消息发送速率。
SVRCV|Sv接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制Sv接口的消息接收速率。
SVSND|Sv接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制Sv接口的消息发送速率。
S10RCV|S10接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S10接口的消息接收速率。
S10SND|S10接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S10接口的消息发送速率。
GNRCV|Gn接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制Gn接口的消息接收速率。
GNSND|Gn接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制Gn接口的消息发送速率。
命令举例 
设置MME接口消息控制配置。 
SET INTERFACE MSG OVERLOAD:S1RCV=65535,S1SND=65535,S6ARCV=65535,S6ASND=65535,S11RCV=65535,S11SND=65535,SGSRCV=65535,SGSSND=65535,SVRCV=65535,SVSND=65535,S10RCV=65535,S10SND=65535,GNRCV=65535,GNSND=65535; 
父主题： [MME接口消息控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询MME接口消息控制配置(SHOW INTERFACE MSG OVERLOAD) 
##### 查询MME接口消息控制配置(SHOW INTERFACE MSG OVERLOAD) 
命令功能 
本命令用于查询MME的各个逻辑接口的消息通过速率。
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
S1RCV|S1接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S1接口的消息接收速率。
S1SND|S1接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S1接口的消息发送速率。
S6ARCV|S6a接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S6a接口的消息接收速率。
S6ASND|S6a接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S6a接口的消息发送速率。
S11RCV|S11接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S11接口的消息接收速率。
S11SND|S11接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S11接口的消息发送速率。
SGSRCV|SGs接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制SGs接口的消息接收速率。
SGSSND|SGs接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制SGs接口的消息发送速率。
SVRCV|Sv接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制Sv接口的消息接收速率。
SVSND|Sv接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制Sv接口的消息发送速率。
S10RCV|S10接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S10接口的消息接收速率。
S10SND|S10接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制S10接口的消息发送速率。
GNRCV|Gn接口接收速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制Gn接口的消息接收速率。
GNSND|Gn接口发送速率(条/秒/进程)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|控制Gn接口的消息发送速率。
命令举例 
查询MME接口消息控制配置。 
SHOW INTERFACE MSG OVERLOAD; 
`
2018-11-20 11:25:24 命令 (No.1): SHOW INTERFACE MSG OVERLOAD
操作维护  S1接口接收速率(条/秒/进程)   S1接口发送速率(条/秒/进程)   S6a接口接收速率(条/秒/进程)   S6a接口发送速率(条/秒/进程)   S11接口接收速率(条/秒/进程)   S11接口发送速率(条/秒/进程)   SGs接口接收速率(条/秒/进程)   SGs接口发送速率(条/秒/进程)   Sv接口接收速率(条/秒/进程)   Sv接口发送速率(条/秒/进程)   S10接口接收速率(条/秒/进程)   S10接口发送速率(条/秒/进程)   Gn接口接收速率(条/秒/进程)   Gn接口发送速率(条/秒/进程)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      65535                        65535                        65535                         65535                         65535                         65535                         65535                         65535                         65535                        65535                        65535                         65535                         65535                        65535
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.063 秒）。
` 
父主题： [MME接口消息控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### HSS过负荷控制配置 
### HSS过负荷控制配置 
背景知识 
            
            HSS过负荷控制，是指MME收到HSS通过Diameter协议扩展的OC-OLR AVP携带的控制比例和有效时间等详细过负荷信息，并根据该信息完成到该HSS的业务控制的功能。
        
功能描述 
            
            HSS过负荷控制配置用于配置HSS网元过负荷控制的开关和相关参数。
        
相关主题 
 
设置HSS过负荷控制(SET HSS OVERLOAD CONTROL)
 
 
查询HSS过负荷控制(SHOW HSS OVERLOAD CONTROL)
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置HSS过负荷控制(SET HSS OVERLOAD CONTROL) 
#### 设置HSS过负荷控制(SET HSS OVERLOAD CONTROL) 
命令功能 
该命令用于设置HSS网元的过负荷控制的开关以及拒绝时携带的Back-off Timer取值。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
OVERLOAD|支持HSS过负荷控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持HSS过负荷控制的开关。
MIN|拒绝时携带的Back-off Timer最小值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|配置HSS过负荷时，NAS拒绝消息中携带的Back-off Timer最小值。在用户4G接入，MME向HSS发送消息，收到HSS返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在"拒绝时携带的Back-off Timer最小取值（秒）”与"拒绝时携带的Back-off Timer最小取值（秒）”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。注：无论HSS过负荷控制License是否打开，该字段都会使用。
MAX|拒绝时携带的Back-off Timer最大值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|配置HSS过负荷时，NAS拒绝消息中携带的Back-off Timer最大值。在用户4G接入，MME向HSS发送消息，收到HSS返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在"拒绝时携带的Back-off Timer最小取值（秒）”与"拒绝时携带的Back-off Timer最小取值（秒）”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。注：无论HSS过负荷控制License是否打开，该字段都会使用。
命令举例 
设置支持HSS过负荷控制,支持HSS过负荷控制为不支持，拒绝时携带的Back-off Timer最小值为1800，拒绝时携带的Back-off Timer取值为3600。 
SET HSS OVERLOAD CONTROL:OVERLOAD="NO",MIN=1800,MAX=3600; 
父主题： [HSS过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询HSS过负荷控制(SHOW HSS OVERLOAD CONTROL) 
#### 查询HSS过负荷控制(SHOW HSS OVERLOAD CONTROL) 
命令功能 
该命令用于查询HSS网元的过负荷控制配置信息。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OVERLOAD|支持HSS过负荷控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持HSS过负荷控制的开关。
MIN|拒绝时携带的Back-off Timer最小值(秒)|参数可选性:任选参数；参数类型:整数。|配置HSS过负荷时，NAS拒绝消息中携带的Back-off Timer最小值。在用户4G接入，MME向HSS发送消息，收到HSS返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在"拒绝时携带的Back-off Timer最小取值（秒）”与"拒绝时携带的Back-off Timer最小取值（秒）”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。注：无论HSS过负荷控制License是否打开，该字段都会使用。
MAX|拒绝时携带的Back-off Timer最大值(秒)|参数可选性:任选参数；参数类型:整数。|配置HSS过负荷时，NAS拒绝消息中携带的Back-off Timer最大值。在用户4G接入，MME向HSS发送消息，收到HSS返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在"拒绝时携带的Back-off Timer最小取值（秒）”与"拒绝时携带的Back-off Timer最小取值（秒）”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。注：无论HSS过负荷控制License是否打开，该字段都会使用。
命令举例 
查询HSS过负荷控制信息。 
SHOW HSS OVERLOAD CONTROL; 
`
命令 (No.65): SHOW HSS OVERLOAD CONTROL
操作维护  支持HSS过负荷控制   拒绝时携带的Back-off Timer最小值(秒)   拒绝时携带的Back-off Timer最大值(秒)
---------------------------------------------------------------------------------------------------------
修改      支持                1                                      2
---------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.038 秒）。
` 
父主题： [HSS过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### SGW过负荷控制配置 
### SGW过负荷控制配置 
背景知识 
            
            GTP-C过负荷控制，即过负荷的GTP-C节点在发送的GTP-C消息中的携带包含有缩减比例的过负荷控制信息，接收消息的GTP-C节点根据收到的缩减比例，缩减到该发生过负荷的GTP-C节点的业务负荷。对于MME来说，SGW过负荷控制就是当SGW发生过负荷后，通知MME，由MME来缩减到SGW的业务负荷。
        
功能描述 
            
            SGW过负荷控制配置主要用于设置SGW过负荷控制的功能开关，以及SGW过负荷时给不同UE下发的NAS拒绝消息中携带的Back-off Timer的取值范围。
        
相关主题 
 
设置SGW过负荷控制(SET SGW OVERLOAD CONTROL)
 
 
查询SGW过负荷控制(SHOW SGW OVERLOAD CONTROL)
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置SGW过负荷控制(SET SGW OVERLOAD CONTROL) 
#### 设置SGW过负荷控制(SET SGW OVERLOAD CONTROL) 
命令功能 
该命令用于修改SGW过负荷控制，包括功能开关，以及SGW过负荷时NAS拒绝消息中携带的Back-off Timer的范围。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
OVERLOAD|支持SGW过负荷控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持SGW过负荷控制的开关。
MIN|拒绝时携带的Back-off Timer最小值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于配置SGW过负荷时，NAS拒绝消息中携带的Back-off Timer的最小值。在用户4G接入，MME向SGW发送消息，收到SGW返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最小值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。在PDN连接建立过程中，MME向SGW发送消息，收到SGW返回的过负荷信息，MME会给用户发送拒绝消息，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果为0，标识不携带Back-off Timer信息给UE。如果不是0，则MME在【MIN，MAX】范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAX|拒绝时携带的Back-off Timer最大值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于配置SGW过负荷时，NAS拒绝消息中携带的Back-off Timer的最大值。在用户4G接入，MME向SGW发送消息，收到SGW返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最小值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。在PDN连接建立过程中，MME向SGW发送消息，收到SGW返回的过负荷信息，MME会给用户发送拒绝消息，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果为0，标识不携带Back-off Timer信息给UE。如果不是0，则MME在【MIN，MAX】范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
设置支持SGW过负荷控制、拒绝时携带的Back-off Timer最小值为3600、拒绝时携带的Back-off Timer最大值为18000。 
SET SGW OVERLOAD CONTROL:OVERLOAD="YES",MIN=3600,MAX=18000; 
父主题： [SGW过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询SGW过负荷控制(SHOW SGW OVERLOAD CONTROL) 
#### 查询SGW过负荷控制(SHOW SGW OVERLOAD CONTROL) 
命令功能 
该命令用于查询SGW过负荷控制的配置信息。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OVERLOAD|支持SGW过负荷控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持SGW过负荷控制的开关。
MIN|拒绝时携带的Back-off Timer最小值(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于配置SGW过负荷时，NAS拒绝消息中携带的Back-off Timer的最小值。在用户4G接入，MME向SGW发送消息，收到SGW返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最小值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。在PDN连接建立过程中，MME向SGW发送消息，收到SGW返回的过负荷信息，MME会给用户发送拒绝消息，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果为0，标识不携带Back-off Timer信息给UE。如果不是0，则MME在【MIN，MAX】范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAX|拒绝时携带的Back-off Timer最大值(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于配置SGW过负荷时，NAS拒绝消息中携带的Back-off Timer的最大值。在用户4G接入，MME向SGW发送消息，收到SGW返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最小值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。在PDN连接建立过程中，MME向SGW发送消息，收到SGW返回的过负荷信息，MME会给用户发送拒绝消息，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果为0，标识不携带Back-off Timer信息给UE。如果不是0，则MME在【MIN，MAX】范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
查询SGW过负荷控制。 
SHOW SGW OVERLOAD CONTROL; 
`
命令 (No.1): SHOW SGW OVERLOAD CONTROL;
操作维护  支持SGW过负荷控制   拒绝时携带的Back-off Timer最小值   拒绝时携带的Back-off Timer最大值
-------------------------------------------------------------------------------------------------
修改      不支持              3600                               18000
-------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.041 秒）。
` 
父主题： [SGW过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### PGW过负荷控制配置 
### PGW过负荷控制配置 
背景知识 
GTP-C过负荷控制，即过负荷的GTP-C节点在发送的GTP-C消息中的携带包含有缩减比例的过负荷控制信息，接收消息的GTP-C节点根据收到的缩减比例，缩减到该发生过负荷的GTP-C节点的业务负荷。对于MME来说，PGW过负荷控制就是当PGW发生过负荷后，通知MME，由MME来缩减到PGW的业务负荷。同时，PGW也可以通过在创建会话响应消息中携带Back-off time来指示APN拥塞，MME可进行APN的拥塞控制。 
功能描述 
PGW过负荷控制配置主要用于设置PGW过负荷控制的功能开关、PGW返回Back-off time的APN拥塞控制功能的开关、以及PGW过负荷时给不同UE下发的NAS拒绝消息中携带的Back-off Timer的取值范围。 
相关主题 
 
设置PGW过负荷控制(SET PGW OVERLOAD CONTROL)
 
 
查询PGW过负荷控制(SHOW PGW OVERLOAD CONTROL)
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置PGW过负荷控制(SET PGW OVERLOAD CONTROL) 
#### 设置PGW过负荷控制(SET PGW OVERLOAD CONTROL) 
命令功能 
该命令用于修改PGW过负荷控制，包括过负荷控制功能开关，PGW返回Back-off time的APN拥塞控制功能开关，以及SGW过负荷时NAS拒绝消息中携带的Back-off Timer的范围。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
OVERLOAD|支持PGW过负荷控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持PGW过负荷控制的开关。
PGWBACKTIME|支持PGW Back-off time控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持PGW返回Back-off time的APN拥塞控制功能的开关。
MIN|拒绝时携带的Back-off Timer最小值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置配置PGW过负荷时，NAS拒绝消息中携带的Back-off Timer的最小值。在用户4G接入，MME向PGW发送消息，收到PGW返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最大值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。在PDN连接建立过程中，MME向PGW发送消息，收到PGW返回的过负荷信息，MME会给用户发送拒绝消息，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果为0，表示不携带Back-off Timer信息给UE。如果不是0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最大值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAX|拒绝时携带的Back-off Timer最大值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置配置PGW过负荷时，NAS拒绝消息中携带的Back-off Timer的最大值。在用户4G接入，MME向PGW发送消息，收到PGW返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最大值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。在PDN连接建立过程中，MME向PGW发送消息，收到PGW返回的过负荷信息，MME会给用户发送拒绝消息，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果为0，表示不携带Back-off Timer信息给UE。如果不是0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最大值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
设置支持PGW过负荷控制、支持PGW Back-off time控制、拒绝时携带的Back-off Timer最小值为3600、拒绝时携带的Back-off Timer最大值为18000。 
SET PGW OVERLOAD CONTROL:OVERLOAD="YES",PGWBACKTIME="YES",MIN=3600,MAX=18000; 
父主题： [PGW过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询PGW过负荷控制(SHOW PGW OVERLOAD CONTROL) 
#### 查询PGW过负荷控制(SHOW PGW OVERLOAD CONTROL) 
命令功能 
该命令用于查询PGW过负荷控制的配置信息。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OVERLOAD|支持PGW过负荷控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持PGW过负荷控制的开关。
PGWBACKTIME|支持PGW Back-off time控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持PGW返回Back-off time的APN拥塞控制功能的开关。
MIN|拒绝时携带的Back-off Timer取小值(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置配置PGW过负荷时，NAS拒绝消息中携带的Back-off Timer的最小值。在用户4G接入，MME向PGW发送消息，收到PGW返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最大值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。在PDN连接建立过程中，MME向PGW发送消息，收到PGW返回的过负荷信息，MME会给用户发送拒绝消息，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果为0，表示不携带Back-off Timer信息给UE。如果不是0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最大值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAX|拒绝时携带的Back-off Timer最大值(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置配置PGW过负荷时，NAS拒绝消息中携带的Back-off Timer的最大值。在用户4G接入，MME向PGW发送消息，收到PGW返回的过负荷信息，MME会给用户发送接入拒绝消息，原因值为#22（Congestion）时，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最大值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试接入。如果终端不支持#22或没有携带Back-off Timer，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。在PDN连接建立过程中，MME向PGW发送消息，收到PGW返回的过负荷信息，MME会给用户发送拒绝消息，消息中是否携带Back-off Timer及携带的值，通过本参数确定。如果为0，表示不携带Back-off Timer信息给UE。如果不是0，则MME在“拒绝时携带的Back-off Timer最小值(秒)”和“拒绝时携带的Back-off Timer最大值(秒)”范围取随机值，作为Back-off Timer的值，带给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
查询PGW过负荷控制。 
SHOW PGW OVERLOAD CONTROL; 
`
命令 (No.1): SHOW PGW OVERLOAD CONTROL;
操作维护  支持PGW过负荷控制   支持PGW Back-off time控制   拒绝时携带的Back-off Timer取小值   拒绝时携带的Back-off Timer取大值
-----------------------------------------------------------------------------------------------------------------------------
修改      不支持              不支持                      3600                               18000
-----------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.026 秒）。
` 
父主题： [PGW过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于APN拥塞控制配置 
### 基于APN拥塞控制配置 
背景知识 
LTE网络中，当用户发起的业务量过多时，可能导致PGW资源不够用而造成拥塞。此时如果MME不对业务量进行控制，那么PGW就有可能瘫痪。 
MME控制业务量的具体过程：当MME判断出已有过多业务建立时，MME可拒绝后续用户发起的业务，并通知这些用户延迟发起业务，这样可避免PGW瘫痪。 
功能描述 
本功能模块可实现以下功能： 
 
设置MME是否启用APN拥塞控制。
 
 
配置针对某些特定APN的拥塞控制策略。
 
 
相关主题 
 
基于APN拥塞控制开关
 
 
APN拥塞控制策略配置
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 基于APN拥塞控制开关 
#### 基于APN拥塞控制开关 
背景知识 
LTE网络中，当用户发起业务量过多，可能导致PGW资源不够用而造成拥塞。MME支持拥塞控制：当MME判断出已有过多业务建立，MME可拒绝后续用户发起的业务，并通知这些用户延迟发起业务，这样可避免PGW负荷过载。 
MME可针对特定的APN来进行拥塞控制，如果用户使用该特定的APN发起业务，那么此业务就会被MME拒绝，通知其延迟一段时间再使用此特定APN发起业务。 
功能描述 
本功能模块可设置MME是否启用基于APN进行拥塞控制。 
相关主题 
 
设置APN拥塞控制开关(SET APN CONGESTION SWITCH)
 
 
查询APN拥塞控制开关(SHOW APN CONGESTION SWITCH)
 
 
父主题： [基于APN拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置APN拥塞控制开关(SET APN CONGESTION SWITCH) 
##### 设置APN拥塞控制开关(SET APN CONGESTION SWITCH) 
命令功能 
该命令用于设置是否支持按APN进行拥塞控制。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ISSUPCONAPN|支持按APN拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否支持按APN进行拥塞控制。
NBUSELPACAPN|NB-IoT接入使用低接入优先级控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|基于APN拥塞控制下，该参数用于配置用户NB-IoT RAT接入时，是否使用低接入优先级拥塞控制参数进行拥塞控制。
命令举例 
开启按APN拥塞控制。 
SET APN CONGESTION SWITCH:ISSUPCONAPN="YES"; 
父主题： [基于APN拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询APN拥塞控制开关(SHOW APN CONGESTION SWITCH) 
##### 查询APN拥塞控制开关(SHOW APN CONGESTION SWITCH) 
命令功能 
该命令用于查询是否支持按APN进行拥塞控制。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ISSUPCONAPN|支持按APN拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否支持按APN进行拥塞控制。
NBUSELPACAPN|NB-IoT接入使用低接入优先级控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|基于APN拥塞控制下，该参数用于配置用户NB-IoT RAT接入时，是否使用低接入优先级拥塞控制参数进行拥塞控制。
命令举例 
查询APN拥塞控制开关。 
SHOW APN CONGESTION SWITCH; 
`
命令 (No.1): SHOW APN CONGESTION SWITCH
操作维护  支持按APN拥塞控制   NB-IoT接入使用低接入优先级控制
------------------------------------------------------------
修改      支持                不使用
------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.05 秒）。
` 
父主题： [基于APN拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### APN拥塞控制策略配置 
#### APN拥塞控制策略配置 
背景知识 
LTE网络中，当用户发起业务量过多，可能导致PGW资源不够用而造成拥塞。MME支持进行拥塞控制：当MME判断出已有过多业务建立，MME可拒绝后续用户发起的业务，并通知这些用户延迟发起业务，这样可避免PGW负荷过载。 
MME可针对特定的APN来进行拥塞控制，如果用户使用该特定的APN发起业务，那么此业务就会被MME拒绝，通知其延迟一段时间再使用此特定APN发起业务。 
功能描述 
本功能模块可设置MME支持对用户使用特定APN发起的业务进行拥塞控制，以及进行控制的策略、控制的门限和拒绝用户业务的比例。 
相关主题 
 
新增APN拥塞控制策略(ADD APN CONGESTION POLICY)
 
 
修改APN拥塞控制策略(SET APN CONGESTION POLICY)
 
 
删除APN拥塞控制策略(DEL APN CONGESTION POLICY)
 
 
查询APN拥塞控制策略(SHOW APN CONGESTION POLICY)
 
 
父主题： [基于APN拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 新增APN拥塞控制策略(ADD APN CONGESTION POLICY) 
##### 新增APN拥塞控制策略(ADD APN CONGESTION POLICY) 
命令功能 
该命令用于增加APN拥塞控制策略。每个APN最多可配置三种策略，三个策略分别是“承载建立数”、“承载建立速率”和“接收NAS MM信令速率”。 
注意事项 
当选择策略为“承载建立数”与“承载建立速率”时，配置的APN为APNNI+APNOI。当选择策略为“接收NAS MM信令速率”时，配置的APN为APNNI。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对APN进行拥塞控制的方式，可选择三种方式。“承载建立数”：当该APN对应的已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。“承载建立速率”：当该APN对应的建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。 “接收NAS MM信令速率”：当签约某APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。
PERIOD|NAS拥塞统计周期|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:SECOND。|该参数用于配置NAS拥塞统计周期，可以按秒、分钟进行控制。
MAXBEAR|最大建立承载数|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXRATE|最大建立承载速率（个/周期）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的最大建立承载速率，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/周期）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给终端Backoff Timer的最小值。当用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，Back-off Timer字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411，10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给终端Backoff Timer的最大值。当用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，Back-off Timer字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411，10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|当“拥塞控制类型”设置为“承载建立速率”或“接收NAS MM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，拒绝新接入业务的比例。
EMMREJECTCAUSE|EMM拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:19。|拒绝时可携带的原因值如下： 2:IMSI unknown in HSS  3:Illegal UE  5:IMEI not accepted  6:Illegal ME  7:EPS services not allowed  8:EPS services and non-EPS services not allowed  9:UE identity cannot be derived by the network  10:Implicitly detached  11:PLMN not allowed  12:Tracking Area not allowed  13:Roaming not allowed in this tracking area  14:EPS services not allowed in this PLMN  15:No Suitable Cells In tracking area  16:MSC temporarily not reachable  17:Network failure  18:CS domain not available  19:ESM failure  20:MAC failure  21:Synch failure  22:Congestion  23:UE security capabilities mismatch  24:Security mode rejected, unspecified  25:Not authorized for this CSG  26:Non-EPS authentication unacceptable  31:Redirection to 5GCN required  35:Requested service option not authorized in this PLMN  39:CS service temporarily not available  40:No EPS bearer context activated  42:Severe network failure  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified
ESMREJECTCAUSE|ESM拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。默认值:26。|拒绝时可携带的原因值如下： 8:Operator Determined Barring  26:Insufficient resources  27:Missing or unknown APN  28:Unknown PDN type  29:User authentication failed  30:Request rejected by Serving GW or PDN GW  31:Request rejected, unspecified  32:Service option not supported  33:Requested service option not subscribed  34:Service option temporarily out of order  35:PTI already in use  36:Regular deactivation  37:EPS QoS not accepted  38:Network failure  39:Reactivation requested  41:Semantic error in the TFT operation  42:Syntactical error in the TFT operation  43:Invalid EPS bearer identity  44:Semantic errors in packet filter(s)  45:Syntactical errors in packet filter(s)  47:PTI mismatch  49:Last PDN disconnection not allowed  50:PDN type IPv4 only allowed  51:PDN type IPv6 only allowed  57:PDN type IPv4v6 only allowed  58:PDN type non IP only allowed  52:PDN type non IP only allowed  53:ESM information not received  54:PDN connection does not exist  55:Multiple PDN connections for a given APN not allowed  56:Collision with network initiated request  59:Unsupported QCI value  60:Bearer handling not supported  65:Maximum number of EPS bearers reached  66:Requested APN not supported in current RAT and PLMN combination  68:PDN type Ethernet only allowed  81:Invalid PTI value  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified  112:APN restriction value incompatible with active EPS bearer context  113:Multiple accesses to a PDN connection not allowed
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|当“拥塞控制类型”设置为“承载建立数”或“承载建立速率”时，该参数用于指示使用这两种拥塞控制方式时，MME是否能够主动去活已建立的承载。
GUABEAR|可保障建立承载数|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的可保障建立承载数，超过此配置值时对低优先级接入业务进行限制。
GUARATE|可保障建立承载速率（个/周期）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的可保障建立承载速率，超过此配置值时对低优先级接入业务进行限制。
GUANASMM|可保障接收NAS MM信令速率（条/周期）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的可保障接收NAS MM信令速率，超过此配置值时对低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给低优先级接入用户Backoff Timer的最小值。当低优先级接入用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给低优先级接入用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级接入用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级接入用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。低优先级接入用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给低优先级接入终端Backoff Timer的最大值。当低优先级接入用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给低优先级接入用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级接入用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级接入用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。低优先级接入用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
命令举例 
新增APN拥塞控制策略配置。 
ADD APN CONGESTION POLICY:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",TYPE="BEARERNUM",MAXBEAR=2000,DEACTBEAR="YES",GUABEAR=0; 
父主题： [APN拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 修改APN拥塞控制策略(SET APN CONGESTION POLICY) 
##### 修改APN拥塞控制策略(SET APN CONGESTION POLICY) 
命令功能 
该命令用于修改APN拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对APN进行拥塞控制的方式，可选择三种方式。“承载建立数”：当该APN对应的已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。“承载建立速率”：当该APN对应的建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。 “接收NAS MM信令速率”：当签约某APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。
PERIOD|NAS拥塞统计周期|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置NAS拥塞统计周期，可以按秒、分钟进行控制。
MAXBEAR|最大建立承载数|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXRATE|最大建立承载速率（个/周期）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的最大建立承载速率，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/周期）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最小值。当用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，Back-off Timer字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411，10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最大值。当用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，Back-off Timer字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411，10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|当“拥塞控制类型”设置为“承载建立速率”或“接收NAS MM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，拒绝新接入业务的比例。
EMMREJECTCAUSE|EMM拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|拒绝时可携带的原因值如下： 2:IMSI unknown in HSS  3:Illegal UE  5:IMEI not accepted  6:Illegal ME  7:EPS services not allowed  8:EPS services and non-EPS services not allowed  9:UE identity cannot be derived by the network  10:Implicitly detached  11:PLMN not allowed  12:Tracking Area not allowed  13:Roaming not allowed in this tracking area  14:EPS services not allowed in this PLMN  15:No Suitable Cells In tracking area  16:MSC temporarily not reachable  17:Network failure  18:CS domain not available  19:ESM failure  20:MAC failure  21:Synch failure  22:Congestion  23:UE security capabilities mismatch  24:Security mode rejected, unspecified  25:Not authorized for this CSG  26:Non-EPS authentication unacceptable  31:Redirection to 5GCN required  35:Requested service option not authorized in this PLMN  39:CS service temporarily not available  40:No EPS bearer context activated  42:Severe network failure  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified
ESMREJECTCAUSE|ESM拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|拒绝时可携带的原因值如下： 8:Operator Determined Barring  26:Insufficient resources  27:Missing or unknown APN  28:Unknown PDN type  29:User authentication failed  30:Request rejected by Serving GW or PDN GW  31:Request rejected, unspecified  32:Service option not supported  33:Requested service option not subscribed  34:Service option temporarily out of order  35:PTI already in use  36:Regular deactivation  37:EPS QoS not accepted  38:Network failure  39:Reactivation requested  41:Semantic error in the TFT operation  42:Syntactical error in the TFT operation  43:Invalid EPS bearer identity  44:Semantic errors in packet filter(s)  45:Syntactical errors in packet filter(s)  47:PTI mismatch  49:Last PDN disconnection not allowed  50:PDN type IPv4 only allowed  51:PDN type IPv6 only allowed  57:PDN type IPv4v6 only allowed  58:PDN type non IP only allowed  52:PDN type non IP only allowed  53:ESM information not received  54:PDN connection does not exist  55:Multiple PDN connections for a given APN not allowed  56:Collision with network initiated request  59:Unsupported QCI value  60:Bearer handling not supported  65:Maximum number of EPS bearers reached  66:Requested APN not supported in current RAT and PLMN combination  68:PDN type Ethernet only allowed  81:Invalid PTI value  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified  112:APN restriction value incompatible with active EPS bearer context  113:Multiple accesses to a PDN connection not allowed
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“拥塞控制类型”设置为“承载建立数”或“承载建立速率”时，该参数用于指示使用这两种拥塞控制方式时，MME是否能够主动去活已建立的承载。
GUABEAR|可保障建立承载数|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的可保障建立承载数，超过此配置值时对低优先级接入业务进行限制。
GUARATE|可保障建立承载速率（个/周期）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的可保障建立承载速率，超过此配置值时对低优先级接入业务进行限制。
GUANASMM|可保障接收NAS MM信令速率（条/周期）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的可保障接收NAS MM信令速率，超过此配置值时对低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给低优先级接入用户Backoff Timer的最小值。当低优先级接入用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给低优先级接入用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级接入用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级接入用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。低优先级接入用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给低优先级接入终端Backoff Timer的最大值。当低优先级接入用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给低优先级接入用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级接入用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级接入用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。低优先级接入用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
命令举例 
修改APN拥塞控制策略配置。 
SET APN CONGESTION POLICY:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",TYPE="BEARERNUM",MAXBEAR=2000,MINDELAY=600,MAXDELAY=1800,DEACTBEAR="YES"; 
父主题： [APN拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 删除APN拥塞控制策略(DEL APN CONGESTION POLICY) 
##### 删除APN拥塞控制策略(DEL APN CONGESTION POLICY) 
命令功能 
该命令用于删除APN拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对APN进行拥塞控制的方式，可选择三种方式。“承载建立数”：当该APN对应的已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。“承载建立速率”：当该APN对应的建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。 “接收NAS MM信令速率”：当签约某APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。
命令举例 
删除APN拥塞控制策略配置，APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，拥塞控制类型为承载建立数。 
DEL APN CONGESTION POLICY:APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",TYPE="BEARERNUM"; 
父主题： [APN拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询APN拥塞控制策略(SHOW APN CONGESTION POLICY) 
##### 查询APN拥塞控制策略(SHOW APN CONGESTION POLICY) 
命令功能 
该命令用于查询APN拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对APN进行拥塞控制的方式，可选择三种方式。“承载建立数”：当该APN对应的已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。“承载建立速率”：当该APN对应的建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。 “接收NAS MM信令速率”：当签约某APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对APN进行拥塞控制的方式，可选择三种方式。“承载建立数”：当该APN对应的已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。“承载建立速率”：当该APN对应的建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。 “接收NAS MM信令速率”：当签约某APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。
PERIOD|NAS拥塞统计周期|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置NAS拥塞统计周期，可以按秒、分钟进行控制。
MAXBEAR|最大建立承载数|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXRATE|最大建立承载速率（个/周期）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的最大建立承载速率，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/周期）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最小值。当用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，Back-off Timer字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411，10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最大值。当用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，Back-off Timer字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411，10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立速率”或“接收NAS MM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，拒绝新接入业务的比例。
EMMREJECTCAUSE|EMM拒绝原因值|参数可选性:任选参数；参数类型:整数。|拒绝时可携带的原因值如下： 2:IMSI unknown in HSS  3:Illegal UE  5:IMEI not accepted  6:Illegal ME  7:EPS services not allowed  8:EPS services and non-EPS services not allowed  9:UE identity cannot be derived by the network  10:Implicitly detached  11:PLMN not allowed  12:Tracking Area not allowed  13:Roaming not allowed in this tracking area  14:EPS services not allowed in this PLMN  15:No Suitable Cells In tracking area  16:MSC temporarily not reachable  17:Network failure  18:CS domain not available  19:ESM failure  20:MAC failure  21:Synch failure  22:Congestion  23:UE security capabilities mismatch  24:Security mode rejected, unspecified  25:Not authorized for this CSG  26:Non-EPS authentication unacceptable  31:Redirection to 5GCN required  35:Requested service option not authorized in this PLMN  39:CS service temporarily not available  40:No EPS bearer context activated  42:Severe network failure  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified
ESMREJECTCAUSE|ESM拒绝原因值|参数可选性:任选参数；参数类型:整数。|拒绝时可携带的原因值如下： 8:Operator Determined Barring  26:Insufficient resources  27:Missing or unknown APN  28:Unknown PDN type  29:User authentication failed  30:Request rejected by Serving GW or PDN GW  31:Request rejected, unspecified  32:Service option not supported  33:Requested service option not subscribed  34:Service option temporarily out of order  35:PTI already in use  36:Regular deactivation  37:EPS QoS not accepted  38:Network failure  39:Reactivation requested  41:Semantic error in the TFT operation  42:Syntactical error in the TFT operation  43:Invalid EPS bearer identity  44:Semantic errors in packet filter(s)  45:Syntactical errors in packet filter(s)  47:PTI mismatch  49:Last PDN disconnection not allowed  50:PDN type IPv4 only allowed  51:PDN type IPv6 only allowed  57:PDN type IPv4v6 only allowed  58:PDN type non IP only allowed  52:PDN type non IP only allowed  53:ESM information not received  54:PDN connection does not exist  55:Multiple PDN connections for a given APN not allowed  56:Collision with network initiated request  59:Unsupported QCI value  60:Bearer handling not supported  65:Maximum number of EPS bearers reached  66:Requested APN not supported in current RAT and PLMN combination  68:PDN type Ethernet only allowed  81:Invalid PTI value  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified  112:APN restriction value incompatible with active EPS bearer context  113:Multiple accesses to a PDN connection not allowed
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“拥塞控制类型”设置为“承载建立数”或“承载建立速率”时，该参数用于指示使用这两种拥塞控制方式时，MME是否能够主动去活已建立的承载。
GUABEAR|可保障建立承载数|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的可保障建立承载数，超过此配置值时对低优先级接入业务进行限制。
GUARATE|可保障建立承载速率（个/周期）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的可保障建立承载速率，超过此配置值时对低优先级接入业务进行限制。
GUANASMM|可保障接收NAS MM信令速率（条/周期）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的可保障接收NAS MM信令速率，超过此配置值时对低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给低优先级接入用户Backoff Timer的最小值。当低优先级接入用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给低优先级接入用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级接入用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级接入用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。低优先级接入用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给低优先级接入终端Backoff Timer的最大值。当低优先级接入用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给低优先级接入用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级接入用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级接入用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。低优先级接入用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。
命令举例 
查询APN拥塞控制策略配置，APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，拥塞控制类型为承载建立数。 
SHOW APN CONGESTION POLICY:APN=""zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org"",TYPE=""BEARERNUM""; 
`
2016-12-14 16:43:33 命令 (No.5): SHOW APN CONGESTION POLICY:APN=""zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org"",TYPE=""BEARERNUM"";
操作维护         APN名称                                         拥塞控制类型         NAS拥塞统计周期   最大建立承载数   最大建立承载速率   最大接收NAS MM信令速率   拒绝时携带的Back-off Timer最小取值（秒）   拒绝时携带的Back-off Timer最大取值（秒）   拒绝比例(%)   是否主动去活承载   可保障建立承载数   可保障建立承载速率   可保障接收NAS MM信令速率   低优先级拒绝时携带的Back-off Timer最小取值（秒）   低优先级拒绝时携带的Back-off Timer最大取值（秒）
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org   承载建立数           秒                2000                                                         600                                        1800                                                     是                 0                                                                  600                                                1800
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.066 秒）。
` 
父主题： [APN拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于MTC用户的拥塞控制配置 
### 基于MTC用户的拥塞控制配置 
背景知识 
LTE网络中支持MTC类型用户。 
MTC（Machine Type Communication，机器类通信）是基于当前的LTE技术，并对LTE技术进行优化的一种物联网接入技术。 
MTC是M2M（Machine to Machine，机器对机器）技术的一个分支，其通过对LTE进行优化来支撑M2M终端的接入。 
M2M的另一个分支是采用全新的空口接入技术来支持M2M，俗称NB-IoT（Narrow Band Internet of Thing，窄带物联网）。 
MTC终端通常为单天线，其信号覆盖效果较差，MME可以协同eNodeB为MTC终端提供优化的寻呼，以提高寻呼成功率。 
由于MTC用户业务行为不可预期，可能出现特定类型MTC用户同时接入到同一个PGW，可能会造成PGW拥塞，影响其他用户正常接入。系统需要对MTC用户进行拥塞控制，当MME判断出特定类型MTC用户发起业务过快时，MME可拒绝后续此类用户发起的业务，并通知这些用户延迟发起业务，这样可避免PGW负荷过载。 
功能描述 
MME可针对某些特定类型的MTC用户来进行拥塞控制，当此类MTC用户发起业务过快时，MME可对此类用户发起的业务进行拒绝。 
MME提供了如下MTC用户的拥塞控制策略，分别从网元角度和APN角度对MTC用户进行拥塞控制，保障网络安全。 
 
基于MTC用户进行拥塞控制。
 
 
基于MTC用户的接入的APN进行拥塞控制。
 
 
相关主题 
 
基于MTC用户的MME网元拥塞控制配置
 
 
基于MTC用户的APN拥塞控制配置
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 基于MTC用户的MME网元拥塞控制配置 
#### 基于MTC用户的MME网元拥塞控制配置 
背景知识 
LTE网络中支持MTC类型用户。 
MTC（Machine Type Communication，机器类通信）是基于当前的LTE技术，并对LTE技术进行优化的一种物联网接入技术。 
MTC是M2M（Machine to Machine，机器对机器）技术的一个分支，其通过对LTE进行优化来支撑M2M终端的接入。 
M2M的另一个分支是采用全新的空口接入技术来支持M2M，俗称NB-IoT（Narrow Band Internet of Thing，窄带物联网）。 
MTC终端通常为单天线，其信号覆盖效果较差，MME可以协同eNodeB为MTC终端提供优化的寻呼，以提高寻呼成功率。 
由于MTC用户业务行为不可预期，可能出现特定类型MTC用户同时接入到同一个PGW，可能会造成PGW拥塞，影响其他用户正常接入。系统需要对MTC用户进行拥塞控制，当MME判断出特定类型MTC用户发起业务过快时，MME可拒绝后续此类用户发起的业务，并通知这些用户延迟发起业务，这样可避免PGW负荷过载。 
MME可针对某些特定类型的MTC用户来进行拥塞控制，当此类MTC用户发起业务过快时，MME可对此类用户发起的业务进行拒绝。 
功能描述 
基于MTC用户的MME网元拥塞控制功能包括： 
 
通过开关控制MME是否启用基于MTC用户来进行拥塞控制。
 
 
配置MME是否对特定MTC用户发起的业务进行拥塞控制。
 
 
相关主题 
 
基于MTC用户的MME网元拥塞控制开关
 
 
MTC用户的MME网元拥塞控制策略配置
 
 
父主题： [基于MTC用户的拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 基于MTC用户的MME网元拥塞控制开关 
##### 基于MTC用户的MME网元拥塞控制开关 
背景知识 
LTE网络中支持MTC类型用户，MTC用户业务行为不可预期，可能出现特定类型MTC用户同时接入MME，可能会造成MME拥塞，影响其他用户正常接入。系统需要对MTC用户进行拥塞控制，当MME判断出特定类型MTC用户发起业务过快时，MME可拒绝后续此类用户发起的业务，并通知这些用户延迟发起业务，这样可避免MME负荷过载。 
MME可针对某些特定类型的MTC用户来进行拥塞控制，当此类MTC用户发起业务过快时，MME可对此类用户发起的业务进行拒绝。 
功能描述 
本功能模块可设置是否启用对MTC用户进行拥塞控制。如果启用，那么当MTC用户发起业务过快时，可降低MME网元负荷。 
相关主题 
 
设置MTC用户的MME网元拥塞控制开关(SET MTCMME CONGESTION SWITCH)
 
 
查询MTC用户的MME网元拥塞控制开关(SHOW MTCMME CONGESTION SWITCH)
 
 
父主题： [基于MTC用户的MME网元拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置MTC用户的MME网元拥塞控制开关(SET MTCMME CONGESTION SWITCH) 
###### 设置MTC用户的MME网元拥塞控制开关(SET MTCMME CONGESTION SWITCH) 
命令功能 
该命令用于设置是否支持基于MTC用户的MME网元拥塞控制。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ISSUPCONMTCMME|支持MTC用户的MME网元拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否支持基于MTC用户的MME网元拥塞控制。
NBUSELPACMTC|NB-IoT接入使用低接入优先级控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|基于MTC用户的MME网元拥塞控制下，该参数用于配置用户NB-IoT RAT接入时，是否使用低接入优先级拥塞控制参数进行拥塞控制。
命令举例 
开启基于MTC用户的MME网元拥塞控制开关。 
SET MTCMME CONGESTION SWITCH:ISSUPCONMTCMME="YES"; 
父主题： [基于MTC用户的MME网元拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询MTC用户的MME网元拥塞控制开关(SHOW MTCMME CONGESTION SWITCH) 
###### 查询MTC用户的MME网元拥塞控制开关(SHOW MTCMME CONGESTION SWITCH) 
命令功能 
该命令用于查询是否支持基于MTC用户的MME网元拥塞控制。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ISSUPCONMTCMME|支持MTC用户的MME网元拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否支持基于MTC用户的MME网元拥塞控制。
NBUSELPACMTC|NB-IoT接入使用低接入优先级控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|基于MTC用户的MME网元拥塞控制下，该参数用于配置用户NB-IoT RAT接入时，是否使用低接入优先级拥塞控制参数进行拥塞控制。
命令举例 
查询基于MTC用户的MME网元拥塞控制开关。 
SHOW MTCMME CONGESTION SWITCH; 
`
命令 (No.1): SHOW MTCMME CONGESTION SWITCH
操作维护  支持MTC用户的MME网元拥塞控制   NB-IoT接入使用低接入优先级控制
-----------------------------------------------------------------------
修改      支持                           不使用
-----------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.068 秒）。
` 
父主题： [基于MTC用户的MME网元拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### MTC用户的MME网元拥塞控制策略配置 
##### MTC用户的MME网元拥塞控制策略配置 
背景知识 
LTE网络中支持MTC类型用户，MTC用户业务行为不可预期，可能出现特定类型MTC用户同时接入MME，可能会造成MME拥塞，影响其他用户正常接入。系统需要对MTC用户进行拥塞控制，当MME判断出特定类型MTC用户发起业务过快时，MME可拒绝后续此类用户发起的业务，并通知这些用户延迟发起业务，这样可避免MME负荷过载。 
MME可针对某些特定类型的MTC用户来进行拥塞控制，当此类MTC用户发起业务过快时，MME可对此类用户发起的业务进行拒绝。 
功能描述 
本功能模块可设置MME支持对某些特定MTC用户进行拥塞控制，以及进行控制的策略、控制的门限和拒绝用户业务的比例。 
相关主题 
 
新增MTC用户的MME网元拥塞控制策略(ADD MTCMME CONGESTION POLICY)
 
 
修改MTC用户的MME网元拥塞控制策略(SET MTCMME CONGESTION POLICY)
 
 
删除MTC用户的MME网元拥塞控制策略(DEL MTCMME CONGESTION POLICY)
 
 
查询MTC用户的MME网元拥塞控制策略(SHOW MTCMME CONGESTION POLICY)
 
 
父主题： [基于MTC用户的MME网元拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 新增MTC用户的MME网元拥塞控制策略(ADD MTCMME CONGESTION POLICY) 
###### 新增MTC用户的MME网元拥塞控制策略(ADD MTCMME CONGESTION POLICY) 
命令功能 
该命令用于新增MTC用户的MME网元拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:必选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示MTC Group Identifier的Group ID。
TYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对特定MTC Group Identifier进行拥塞控制的方式，可选择两种方式。“接收NAS MM信令速率”：当签约该MTC Group Identifier的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约该MTC Group Identifier的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给终端Backoff Timer的最小值。当MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给终端Backoff Timer的最大值。当MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。默认值:100。|该参数用于指示在进行拥塞控制时，拒绝新接入业务的比例。
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于指示在进行拥塞控制时，MME是否能够主动去活已建立的承载。
GUANASMM|可保障接收NAS MM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“接收NAS MM信令速率”拥塞控制方式时，可支持最大接收NAS MM信令速率，超过此门限时对于低优先级接入业务进行限制。
GUANASSM|可保障接收NAS SM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“接收NAS SM信令速率”拥塞控制方式时，可支持最大接收NAS SM信令速率，超过此门限时对于低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最小值。当低优先级MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果为0，表示不携带Back-off Timer信息给低优先级MTC用户。如果不是0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。低优先级MTC用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最大值。当低优先级MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。表示不携带Back-off Timer信息给低优先级MTC用户。如果不是0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。低优先级MTC用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
新增MTC用户的MME网元拥塞控制策略配置，MTC Group Identifier为"460"-"01"-123456，拥塞控制类型为接收NAS MM信令速率，最大接收NAS MM信令速率为2000，通知终端延时最小值为600秒，通知终端延时最大值为1800秒，拒绝比例为100%，支持主动去活承载，可保障接收NAS MM信令速率为2。 
ADD MTCMME CONGESTION POLICY:MTCGRPID="460"-"01"-123456,TYPE="NASMMRATE",MAXNASMM=2000,MINDELAY=600,MAXDELAY=1800,REJECTRATE=100,DEACTBEAR="YES",GUANASMM=2; 
父主题： [MTC用户的MME网元拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 修改MTC用户的MME网元拥塞控制策略(SET MTCMME CONGESTION POLICY) 
###### 修改MTC用户的MME网元拥塞控制策略(SET MTCMME CONGESTION POLICY) 
命令功能 
该命令用于修改MTC用户的MME网元拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:必选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示MTC Group Identifier的Group ID。
TYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对特定MTC Group Identifier进行拥塞控制的方式，可选择两种方式。“接收NAS MM信令速率”：当签约该MTC Group Identifier的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约该MTC Group Identifier的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最小值。当MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最大值。当MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于指示在进行拥塞控制时，拒绝新接入业务的比例。
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示在进行拥塞控制时，MME是否能够主动去活已建立的承载。
GUANASMM|可保障接收NAS MM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“接收NAS MM信令速率”拥塞控制方式时，可支持最大接收NAS MM信令速率，超过此门限时对于低优先级接入业务进行限制。
GUANASSM|可保障接收NAS SM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“接收NAS SM信令速率”拥塞控制方式时，可支持最大接收NAS SM信令速率，超过此门限时对于低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最小值。当低优先级MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果为0，表示不携带Back-off Timer信息给低优先级MTC用户。如果不是0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。低优先级MTC用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最大值。当低优先级MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。表示不携带Back-off Timer信息给低优先级MTC用户。如果不是0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。低优先级MTC用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
修改MTC用户的MME网元拥塞控制策略配置，MTC Group Identifier为"460"-"01"-123456，拥塞控制类型为接收NAS MM信令速率，最大接收NAS MM信令速率为2000，通知终端延时最小值为600秒，通知终端延时最大值为1800秒，拒绝比例为100%，支持主动去活承载。 
SET MTCMME CONGESTION POLICY:MTCGRPID="460"-"01"-123456,TYPE="NASMMRATE",MAXNASMM=2000,MINDELAY=600,MAXDELAY=1800,REJECTRATE=100,DEACTBEAR="YES"; 
父主题： [MTC用户的MME网元拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 删除MTC用户的MME网元拥塞控制策略(DEL MTCMME CONGESTION POLICY) 
###### 删除MTC用户的MME网元拥塞控制策略(DEL MTCMME CONGESTION POLICY) 
命令功能 
该命令用于删除MTC用户的MME网元拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:必选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示MTC Group Identifier的Group ID。
TYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对特定MTC Group Identifier进行拥塞控制的方式，可选择两种方式。“接收NAS MM信令速率”：当签约该MTC Group Identifier的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约该MTC Group Identifier的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
命令举例 
删除MTC用户的MME网元拥塞控制策略配置，MTC Group Identifier为"460"-"01"-123456，拥塞控制类型为接收NAS MM信令速率。 
DEL MTCMME CONGESTION POLICY:MTCGRPID="460"-"01"-123456,TYPE="NASMMRATE"; 
父主题： [MTC用户的MME网元拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询MTC用户的MME网元拥塞控制策略(SHOW MTCMME CONGESTION POLICY) 
###### 查询MTC用户的MME网元拥塞控制策略(SHOW MTCMME CONGESTION POLICY) 
命令功能 
该命令用于查询删除MTC用户的MME网元拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:任选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示MTC Group Identifier的Group ID。
TYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对特定MTC Group Identifier进行拥塞控制的方式，可选择两种方式。“接收NAS MM信令速率”：当签约该MTC Group Identifier的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约该MTC Group Identifier的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:任选参数；参数类型:字符型。|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
TYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对特定MTC Group Identifier进行拥塞控制的方式，可选择两种方式。“接收NAS MM信令速率”：当签约该MTC Group Identifier的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约该MTC Group Identifier的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最小值。当MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最大值。当MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数。|该参数用于指示在进行拥塞控制时，拒绝新接入业务的比例。
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示在进行拥塞控制时，MME是否能够主动去活已建立的承载。
GUANASMM|可保障接收NAS MM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数。|该参数用于指示当使用“接收NAS MM信令速率”拥塞控制方式时，可支持最大接收NAS MM信令速率，超过此门限时对于低优先级接入业务进行限制。
GUANASSM|可保障接收NAS SM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数。|该参数用于指示当使用“接收NAS SM信令速率”拥塞控制方式时，可支持最大接收NAS SM信令速率，超过此门限时对于低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最小值。当低优先级MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果为0，表示不携带Back-off Timer信息给低优先级MTC用户。如果不是0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。低优先级MTC用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最大值。当低优先级MTC用户发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。表示不携带Back-off Timer信息给低优先级MTC用户。如果不是0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。低优先级MTC用户PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
查询MTC用户的MME网元拥塞控制策略配置，MTC Group Identifier为"460"-"01"-123456，拥塞控制类型为接收NAS MM信令速率。 
SHOW MTCMME CONGESTION POLICY:MTCGRPID="460"-"01"-123456,TYPE="NASMMRATE"; 
`
命令 (No.1): SHOW MTCMME CONGESTION POLICY:MTCGRPID="460"-"01"-123456,TYPE="NASMMRATE";
操作维护         MTC Group Identifier   拥塞控制类型         最大接收NAS MM信令速率   最大接收NAS SM信令速率   拒绝时携带的Back-off Timer最小取值（秒）   拒绝时携带的Back-off Timer最大取值（秒）   拒绝比例(%)   是否主动去活承载   可保障接收NAS MM信令速率   可保障接收NAS SM信令速率   低优先级拒绝时携带的Back-off Timer最小取值（秒）   低优先级拒绝时携带的Back-off Timer最大取值（秒）
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   460-01-123456          接收NAS MM信令速率   2000                                              600                                        1800                                       100           是                 2                                                     600                                                1800
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.014 秒）。
` 
父主题： [MTC用户的MME网元拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 基于MTC用户的APN拥塞控制配置 
#### 基于MTC用户的APN拥塞控制配置 
背景知识 
LTE网络中支持MTC类型用户。 
MTC（Machine Type Communication，机器类通信）是基于当前的LTE技术，并对LTE技术进行优化的一种物联网接入技术。 
MTC是M2M（Machine to Machine，机器对机器）技术的一个分支，其通过对LTE进行优化来支撑M2M终端的接入。 
M2M的另一个分支是采用全新的空口接入技术来支持M2M，俗称NB-IoT（Narrow Band Internet of Thing，窄带物联网）。 
MTC终端通常为单天线，其信号覆盖效果较差，MME可以协同eNodeB为MTC终端提供优化的寻呼，以提高寻呼成功率。 
由于MTC用户业务行为不可预期，可能出现特定类型MTC用户同时接入到同一个PGW，可能会造成PGW拥塞，影响其他用户正常接入。系统需要对MTC用户进行拥塞控制，当MME判断出特定类型MTC用户发起业务过快时，MME可拒绝后续此类用户发起的业务，并通知这些用户延迟发起业务，这样可避免PGW负荷过载。 
MME可针对某些特定类型的MTC用户来进行拥塞控制，当此类MTC用户发起业务过快时，MME可对此类用户发起的业务进行拒绝。 
功能描述 
基于MTC用户的APN拥塞控制功能包括： 
 
通过开关控制MME是否启用基于MTC用户接入的APN来进行拥塞控制。
 
 
根据MTC用户接入的APN控制策略，来配置控制MME对特定MTC用户使用特定APN发起的业务进行拥塞控制。
 
 
相关主题 
 
基于MTC用户的APN拥塞控制开关
 
 
MTC用户的APN拥塞控制策略配置
 
 
父主题： [基于MTC用户的拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 基于MTC用户的APN拥塞控制开关 
##### 基于MTC用户的APN拥塞控制开关 
背景知识 
LTE网络中支持MTC类型用户，MTC用户业务行为不可预期，可能出现特定类型MTC用户同时接入到同一PGW，可能会造成PGW拥塞，影响其他用户正常接入。系统需要对MTC用户进行拥塞控制，当MME判断出特定类型MTC用户发起业务过快时，MME可拒绝后续此类用户发起的业务，并通知这些用户延迟发起业务，这样可避免PGW负荷过载。 
MME可针对某些特定类型的MTC用户来进行拥塞控制，当此类MTC用户发起业务过快时，MME可对此类用户发起的业务进行拒绝。 
功能描述 
本功能模块可设置MME是否启用基于MTC用户的APN拥塞控制。 
相关主题 
 
设置MTC用户的APN拥塞控制开关(SET MTCAPN CONGESTION SWITCH)
 
 
查询MTC用户的APN拥塞控制开关(SHOW MTCAPN CONGESTION SWITCH)
 
 
父主题： [基于MTC用户的APN拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 设置MTC用户的APN拥塞控制开关(SET MTCAPN CONGESTION SWITCH) 
###### 设置MTC用户的APN拥塞控制开关(SET MTCAPN CONGESTION SWITCH) 
命令功能 
该命令用于设置是否支持基于MTC用户的APN拥塞控制。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ISSUPCONMTCAPN|支持MTC用户的APN拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否支持基于MTC用户的APN拥塞控制。
NBUSELPACMTCAPN|NB-IoT接入使用低接入优先级控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|基于MTC用户的APN拥塞控制下，该参数用于配置用户NB-IoT RAT接入时，是否使用低接入优先级拥塞控制参数进行拥塞控制。
命令举例 
开启基于MTC用户的APN拥塞控制开关。 
SET MTCAPN CONGESTION SWITCH:ISSUPCONMTCAPN="YES"; 
父主题： [基于MTC用户的APN拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询MTC用户的APN拥塞控制开关(SHOW MTCAPN CONGESTION SWITCH) 
###### 查询MTC用户的APN拥塞控制开关(SHOW MTCAPN CONGESTION SWITCH) 
命令功能 
该命令用于查询是否支持基于MTC用户的APN拥塞控制。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ISSUPCONMTCAPN|支持MTC用户的APN拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否支持基于MTC用户的APN拥塞控制。
NBUSELPACMTCAPN|NB-IoT接入使用低接入优先级控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|基于MTC用户的APN拥塞控制下，该参数用于配置用户NB-IoT RAT接入时，是否使用低接入优先级拥塞控制参数进行拥塞控制。
命令举例 
查询基于MTC用户的APN拥塞控制开关。 
SHOW MTCAPN CONGESTION SWITCH; 
`
命令 (No.1): SHOW MTCAPN CONGESTION SWITCH
操作维护  支持MTC用户的APN拥塞控制   NB-IoT接入使用低接入优先级控制
-------------------------------------------------------------------
修改      支持                       不使用
-------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.074 秒）。
` 
父主题： [基于MTC用户的APN拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### MTC用户的APN拥塞控制策略配置 
##### MTC用户的APN拥塞控制策略配置 
背景知识 
LTE网络中，当MTC用户使用某APN发起业务量过多，占用PGW网元过多资源，将影响其他用户的业务，系统支持对MTC用户进行拥塞控制。当MME判断出MTC用户使用某APN已有过多业务建立，MME可拒绝后续MTC用户使用此APN发起的业务，并通知这些用户延迟发起业务，这样可避免占用过多PGW资源。 
功能描述 
本功能模块可设置MME支持对特定MTC用户使用特定APN发起的业务进行拥塞控制，进行控制的策略、控制的门限及拒绝用户业务的比例。 
相关主题 
 
新增MTC用户的APN拥塞控制策略(ADD MTCAPN CONGESTION POLICY)
 
 
修改MTC用户的APN拥塞控制策略(SET MTCAPN CONGESTION POLICY)
 
 
删除MTC用户的APN拥塞控制策略(DEL MTCAPN CONGESTION POLICY)
 
 
查询MTC用户的APN拥塞控制策略(SHOW MTCAPN CONGESTION POLICY)
 
 
父主题： [基于MTC用户的APN拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 新增MTC用户的APN拥塞控制策略(ADD MTCAPN CONGESTION POLICY) 
###### 新增MTC用户的APN拥塞控制策略(ADD MTCAPN CONGESTION POLICY) 
命令功能 
该命令用于新增MTC用户的APN拥塞控制策略，最多可配置三种策略，分别是“承载建立数”、“接收NAS MM信令速率”和“接收NAS SM信令速率”。 
注意事项 
当选择策略为“承载建立数”时，配置的APN为APNNI+APNOI。当选择策略为“接收NAS MM信令速率”和“接收NAS SM信令速率”时，配置的APN为APNNI。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:必选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示下发给MTC终端IMSI-Group identifier的Group ID。
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对MTC用户进行APN拥塞控制的方式，可选择三种方式。“承载建立数”：当签约了特定MTC Group Identifier的用户使用某APN已建立的承载数超过配置的最大建立承载数时，对其进行拥塞控制。“接收NAS MM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXBEAR|最大建立承载数|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给终端Backoff Timer的最小值。当MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给终端Backoff Timer的最大值。当MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|当“拥塞控制类型”设置为“接收NAS MM信令速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，拒绝新接入业务的比例。
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|当“拥塞控制类型”设置为承载建立数”时，该参数用于指示使用这种拥塞控制方式时，MME是否能够主动去活已建立的承载。
GUABEAR|可保障建立承载数|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“承载建立数”拥塞控制方式时，可支持建立的承载数，超过此门限时对于低优先级接入业务进行限制。
GUANASMM|可保障接收NAS MM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“接收NAS MM信令速率”拥塞控制方式时，可支持最大接收NAS MM信令速率，超过此门限时对于低优先级接入业务进行限制。
GUANASSM|可保障接收NAS SM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“接收NAS SM信令速率”拥塞控制方式时，可支持最大接收NAS SM信令速率，超过此门限时对于低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最小值。当低优先级MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，标识不携带Back-off Timer信息给低优先级MTC用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最大值。当低优先级MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，标识不携带Back-off Timer信息给低优先级MTC用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
新增MTC用户的APN拥塞控制策略配置，MTC Group Identifier为"460"-"01"-123456，APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，拥塞控制类型为接收NAS MM信令速率，最大接收NAS MM信令速率为2000，通知终端延时最小值为600秒，通知终端延时最大值为1800秒，拒绝比例为100%，支持主动去活承载。 
ADD MTCAPN CONGESTION POLICY:MTCGRPID="460"-"01"-123456,APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",TYPE="NASMMRATE",MAXNASMM=2000,REJECTRATE=100,DEACTBEAR="YES",GUANASMM=1000; 
父主题： [MTC用户的APN拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 修改MTC用户的APN拥塞控制策略(SET MTCAPN CONGESTION POLICY) 
###### 修改MTC用户的APN拥塞控制策略(SET MTCAPN CONGESTION POLICY) 
命令功能 
该命令用于修改MTC用户的APN拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:必选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示下发给MTC终端IMSI-Group identifier的Group ID。
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对MTC用户进行APN拥塞控制的方式，可选择三种方式。“承载建立数”：当签约了特定MTC Group Identifier的用户使用某APN已建立的承载数超过配置的最大建立承载数时，对其进行拥塞控制。“接收NAS MM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXBEAR|最大建立承载数|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最小值。当MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最大值。当MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|当“拥塞控制类型”设置为“接收NAS MM信令速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，拒绝新接入业务的比例。
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“拥塞控制类型”设置为承载建立数”时，该参数用于指示使用这种拥塞控制方式时，MME是否能够主动去活已建立的承载。
GUABEAR|可保障建立承载数|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“承载建立数”拥塞控制方式时，可支持建立的承载数，超过此门限时对于低优先级接入业务进行限制。
GUANASMM|可保障接收NAS MM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“接收NAS MM信令速率”拥塞控制方式时，可支持最大接收NAS MM信令速率，超过此门限时对于低优先级接入业务进行限制。
GUANASSM|可保障接收NAS SM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于指示当使用“接收NAS SM信令速率”拥塞控制方式时，可支持最大接收NAS SM信令速率，超过此门限时对于低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最小值。当低优先级MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，标识不携带Back-off Timer信息给低优先级MTC用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最大值。当低优先级MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，标识不携带Back-off Timer信息给低优先级MTC用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
修改MTC用户的APN拥塞控制策略配置，MTC Group Identifier为"460"-"01"-123456，APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，拥塞控制类型为接收NAS MM信令速率，最大接收NAS MM信令速率为2000，通知终端延时最小值为600秒，通知终端延时最大值为1800秒，拒绝比例为100%，支持主动去活承载。 
SET MTCAPN CONGESTION POLICY:MTCGRPID="460"-"01"-123456,APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",TYPE="NASMMRATE",MAXNASMM=2000,MINDELAY=600,MAXDELAY=1800,REJECTRATE=100,DEACTBEAR="YES"; 
父主题： [MTC用户的APN拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 删除MTC用户的APN拥塞控制策略(DEL MTCAPN CONGESTION POLICY) 
###### 删除MTC用户的APN拥塞控制策略(DEL MTCAPN CONGESTION POLICY) 
命令功能 
该命令用于删除MTC用户的APN拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:必选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示下发给MTC终端IMSI-Group identifier的Group ID。
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对MTC用户进行APN拥塞控制的方式，可选择三种方式。“承载建立数”：当签约了特定MTC Group Identifier的用户使用某APN已建立的承载数超过配置的最大建立承载数时，对其进行拥塞控制。“接收NAS MM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
命令举例 
删除MTC用户的APN拥塞控制策略配置，MTC Group Identifier为"460"-"01"-123456，APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，拥塞控制类型为接收NAS MM信令速率。 
DEL MTCAPN CONGESTION POLICY:MTCGRPID="460"-"01"-123456,APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",TYPE="NASMMRATE"; 
父主题： [MTC用户的APN拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
###### 查询MTC用户的APN拥塞控制策略(SHOW MTCAPN CONGESTION POLICY) 
###### 查询MTC用户的APN拥塞控制策略(SHOW MTCAPN CONGESTION POLICY) 
命令功能 
该命令用于查询MTC用户的APN拥塞控制策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:任选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示下发给MTC终端IMSI-Group identifier的Group ID。
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对MTC用户进行APN拥塞控制的方式，可选择三种方式。“承载建立数”：当签约了特定MTC Group Identifier的用户使用某APN已建立的承载数超过配置的最大建立承载数时，对其进行拥塞控制。“接收NAS MM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:0~99个字符。|该参数用于指示需进行拥塞控制的APN。
TYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示对MTC用户进行APN拥塞控制的方式，可选择三种方式。“承载建立数”：当签约了特定MTC Group Identifier的用户使用某APN已建立的承载数超过配置的最大建立承载数时，对其进行拥塞控制。“接收NAS MM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。 “接收NAS SM信令速率”：当签约特定MTC Group Identifier且签约特定APN的一类用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXBEAR|最大建立承载数|参数可选性:必须单选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
MINDELAY|拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最小值。当MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
MAXDELAY|拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最大值。当MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值（秒）”与“拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。终端在Backoff Timer时间内不再使用相同APN发起业务。MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
REJECTRATE|拒绝比例(%)|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS MM信令速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，拒绝新接入业务的比例。
DEACTBEAR|是否主动去活承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“拥塞控制类型”设置为承载建立数”时，该参数用于指示使用这种拥塞控制方式时，MME是否能够主动去活已建立的承载。
GUABEAR|可保障建立承载数|参数可选性:任选参数；参数类型:整数。|该参数用于指示当使用“承载建立数”拥塞控制方式时，可支持建立的承载数，超过此门限时对于低优先级接入业务进行限制。
GUANASMM|可保障接收NAS MM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示当使用“接收NAS MM信令速率”拥塞控制方式时，可支持最大接收NAS MM信令速率，超过此门限时对于低优先级接入业务进行限制。
GUANASSM|可保障接收NAS SM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示当使用“接收NAS SM信令速率”拥塞控制方式时，可支持最大接收NAS SM信令速率，超过此门限时对于低优先级接入业务进行限制。
LOWMIN|低优先级拒绝时携带的Back-off Timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最小值。当低优先级MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，标识不携带Back-off Timer信息给低优先级MTC用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
LOWMAX|低优先级拒绝时携带的Back-off Timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给低优先级MTC用户Backoff Timer的最大值。当低优先级MTC用户使用某APN发起业务，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，标识不携带Back-off Timer信息给低优先级MTC用户。如果本参数不为0，此字段取值在“低优先级拒绝时携带的Back-off Timer最小取值（秒）”与“低优先级拒绝时携带的Back-off Timer最大取值（秒）”的范围内随机选择。低优先级MTC用户在Backoff Timer时间内不再使用相同APN发起业务。低优先级MTC用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
查询MTC用户的APN拥塞控制策略配置，MTC Group Identifier为"460"-"01"-123456，APN名称为zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org，拥塞控制类型为接收NAS MM信令速率。 
SHOW MTCAPN CONGESTION POLICY:MTCGRPID="460"-"01"-123456,APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",TYPE="NASMMRATE"; 
`
命令 (No.1): SHOW MTCAPN CONGESTION POLICY:MTCGRPID="460"-"01"-123456,APN="zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org",TYPE="NASMMRATE";
操作维护         MTC Group Identifier   APN名称                                         拥塞控制类型         最大建立承载数   最大接收NAS MM信令速率   最大接收NAS SM信令速率   拒绝时携带的Back-off Timer最小取值（秒）   拒绝时携带的Back-off Timer最大取值（秒）   拒绝比例(%)   是否主动去活承载   可保障建立承载数   可保障接收NAS MM信令速率   可保障接收NAS SM信令速率   低优先级拒绝时携带的Back-off Timer最小取值（秒）   低优先级拒绝时携带的Back-off Timer最大取值（秒）
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   460-01-123456          zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org   接收NAS MM信令速率                    2000                                              600                                        1800                                       100           是                                    1000                                                  600                                                1800
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.028 秒）。
` 
父主题： [MTC用户的APN拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于RAT拥塞控制配置 
### 基于RAT拥塞控制配置 
背景知识 
当MME网元在业务过负荷的情况下，NB-IOT物联网用户的优先级应该低于人网用户，即MME需要优先满足人网用户的接入需求。 
功能描述 
本功能用来配置RAT拥塞控制开关和RAT（Radio Access Technology，无线接入技术）拥塞控制参数，比如分别设置NB-IOT和WB用户的承载建立数、承载建立速率、接收NAS MM信令速率、接收NAS SM信令速率。 
相关主题 
 
RAT拥塞控制开关
 
 
RAT拥塞控制策略配置
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### RAT拥塞控制开关 
#### RAT拥塞控制开关 
背景知识 
            
            NB-IoT用户有更低的拥塞控制门限，优先于普通移动用户被控制。网元可基于用户接入RAT类型进行NAS拥塞门限配置、拥塞判断和拥塞控制，如可控制NB-IoT RAT类型用户的附着请求消息和CPSR消息。当NB-IoT用户的拥塞门限低于普通移动用户的拥塞门限时，优先被控制。
        
功能描述 
            
            RAT拥塞控制开关用于配置MME是否支持RAT拥塞控制。
        
相关主题 
 
设置RAT拥塞控制开关(SET RAT CONGESTION SWITCH)
 
 
查询RAT拥塞控制开关(SHOW RAT CONGESTION SWITCH)
 
 
父主题： [基于RAT拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置RAT拥塞控制开关(SET RAT CONGESTION SWITCH) 
##### 设置RAT拥塞控制开关(SET RAT CONGESTION SWITCH) 
命令功能 
该命令用于设置基于用户接入类型的RAT拥塞控制功能是否开启。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPNBRATCON|支持RAT拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否支持基于用户接入类型RAT的拥塞控制。
命令举例 
设置不支持RAT拥塞控制。 
SET RAT CONGESTION SWITCH:SUPNBRATCON="NO"; 
父主题： [RAT拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询RAT拥塞控制开关(SHOW RAT CONGESTION SWITCH) 
##### 查询RAT拥塞控制开关(SHOW RAT CONGESTION SWITCH) 
命令功能 
该命令用于查询基于用户接入类型的RAT拥塞控制是否开启。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPNBRATCON|支持RAT拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否支持基于用户接入类型RAT的拥塞控制。
命令举例 
查询是否支持RAT拥塞控制。 
SHOW RAT CONGESTION SWITCH; 
`
命令 (No.1): SHOW RAT CONGESTION SWITCH
操作维护  支持RAT拥塞控制
-------------------------
修改      不支持
-------------------------
记录数 1
命令执行成功（耗时 0.063 秒）。
` 
父主题： [RAT拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### RAT拥塞控制策略配置 
#### RAT拥塞控制策略配置 
背景知识 
            
            NB-IoT用户有更低的拥塞控制门限，优先于大网用户被控制。网元可基于用户接入RAT类型进行NAS拥塞门限配置、拥塞判断和拥塞控制，如可控制NB-IoT RAT类型用户的附着请求消息和CPSR消息。当NB-IoT用户的拥塞门限低于大网用户的拥塞门限时，优先被控制。
        
功能描述 
            
            RAT拥塞控制策略配置用于设置MME基于用户接入RAT的业务进行拥塞控制，包括进行控制的策略、控制的门限和拒绝用户业务的比例。
        
相关主题 
 
新增RAT拥塞控制策略(ADD RAT CONGESTION POLICY)
 
 
修改RAT拥塞控制策略(SET RAT CONGESTION POLICY)
 
 
删除RAT拥塞控制策略(DEL RAT CONGESTION POLICY)
 
 
查询RAT拥塞控制策略(SHOW RAT CONGESTION POLICY)
 
 
父主题： [基于RAT拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 新增RAT拥塞控制策略(ADD RAT CONGESTION POLICY) 
##### 新增RAT拥塞控制策略(ADD RAT CONGESTION POLICY) 
命令功能 
该命令用于新增RAT拥塞控制策略配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ACCESSTYPE|无线接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置用户的无线接入类型，包括Wide Band和NB-IoT。
CTLTYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于RAT拥塞控制的方式，有4种控制方式供选择：承载建立数：当该无线接入类型下已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。承载建立速率：当该无线接入类型下建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。接收NAS MM信令速率：当该无线接入类型下的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。接收NAS SM信令速率：当该无线接入类型下的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXBEAR|最大建立承载数|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXRATE|最大建立承载速率（个/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的最大建立承载速率，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
CPUTHRESHOLD|CPU拥塞门限|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~99。|当“拥塞控制类型”设置为“CPU拥塞门限”时，该参数用于指示系统CPU占用率超过配置的CPU拥塞门限时，对该无线接入类型下的用户进行拥塞控制。
REJECTRATE|拒绝比例|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|当“拥塞控制类型”设置为“承载建立速率”或“接收NAS MM信令速率”或“接收NAS SM信令速率”时，该参数用于指示使用这三种拥塞控制方式时，拒绝新接入业务的比例。
BACKOFFTIMESTART|拒绝时携带的Back-off Timer最小取值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给终端Backoff Timer的最小值。当用户发起业务，系统判断由于达到RAT拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值(秒)”与“拒绝时携带的Back-off Timer最大取值(秒)”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
BACKOFFTIMEEND|拒绝时携带的Back-off Timer最大取值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于指示下发给终端Backoff Timer的最大值。当用户发起业务，系统判断由于达到RAT拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值(秒)”与“拒绝时携带的Back-off Timer最大取值(秒)”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
新增RAT拥塞控制策略配置。 
ADD RAT CONGESTION POLICY:ACCESSTYPE="NB-IOT",CTLTYPE="RATE_NAS_SM_SIG",MAXNASSM=12,REJECTRATE=3; 
父主题： [RAT拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 修改RAT拥塞控制策略(SET RAT CONGESTION POLICY) 
##### 修改RAT拥塞控制策略(SET RAT CONGESTION POLICY) 
命令功能 
该命令用于设置RAT拥塞控制策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ACCESSTYPE|无线接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置用户的无线接入类型，包括Wide Band和NB-IoT。
CTLTYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于RAT拥塞控制的方式，有4种控制方式供选择：承载建立数：当该无线接入类型下已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。承载建立速率：当该无线接入类型下建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。接收NAS MM信令速率：当该无线接入类型下的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。接收NAS SM信令速率：当该无线接入类型下的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXBEAR|最大建立承载数|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXRATE|最大建立承载速率（个/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的最大建立承载速率，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~4294967295。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
CPUTHRESHOLD|CPU拥塞门限|参数可选性:任意单选参数；参数类型:整数；参数范围为:0~99。|当“拥塞控制类型”设置为“CPU拥塞门限”时，该参数用于指示系统CPU占用率超过配置的CPU拥塞门限时，对该无线接入类型下的用户进行拥塞控制。
REJECTRATE|拒绝比例|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|当“拥塞控制类型”设置为“承载建立速率”或“接收NAS MM信令速率”或“接收NAS SM信令速率”时，该参数用于指示使用这三种拥塞控制方式时，拒绝新接入业务的比例。
BACKOFFTIMESTART|拒绝时携带的Back-off Timer最小取值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最小值。当用户发起业务，系统判断由于达到RAT拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值(秒)”与“拒绝时携带的Back-off Timer最大取值(秒)”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
BACKOFFTIMEEND|拒绝时携带的Back-off Timer最大取值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于指示下发给终端Backoff Timer的最大值。当用户发起业务，系统判断由于达到RAT拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值(秒)”与“拒绝时携带的Back-off Timer最大取值(秒)”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
设置RAT拥塞控制策略，最大接收NAS MM信令速率为100，拒绝时携带的Back-off Timer最小取值(秒)为50，拒绝时携带的Back-off Timer最大取值(秒)为100。 
SET RAT CONGESTION POLICY:ACCESSTYPE="NB-IOT",CTLTYPE="RATE_NAS_MM_SIG",MAXNASMM=100,BACKOFFTIMESTART=50,BACKOFFTIMEEND=100; 
父主题： [RAT拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 删除RAT拥塞控制策略(DEL RAT CONGESTION POLICY) 
##### 删除RAT拥塞控制策略(DEL RAT CONGESTION POLICY) 
命令功能 
该命令用于删除RAT拥塞控制策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ACCESSTYPE|无线接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置用户的无线接入类型，包括Wide Band和NB-IoT。
CTLTYPE|拥塞控制类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于RAT拥塞控制的方式，有4种控制方式供选择：承载建立数：当该无线接入类型下已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。承载建立速率：当该无线接入类型下建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。接收NAS MM信令速率：当该无线接入类型下的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。接收NAS SM信令速率：当该无线接入类型下的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
命令举例 
删除RAT拥塞控制策略。 
DEL RAT CONGESTION POLICY:ACCESSTYPE="NB-IOT",CTLTYPE="RATE_NAS_MM_SIG"; 
父主题： [RAT拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询RAT拥塞控制策略(SHOW RAT CONGESTION POLICY) 
##### 查询RAT拥塞控制策略(SHOW RAT CONGESTION POLICY) 
命令功能 
该命令用于查询RAT拥塞控制策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ACCESSTYPE|无线接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置用户的无线接入类型，包括Wide Band和NB-IoT。
CTLTYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于RAT拥塞控制的方式，有4种控制方式供选择：承载建立数：当该无线接入类型下已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。承载建立速率：当该无线接入类型下建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。接收NAS MM信令速率：当该无线接入类型下的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。接收NAS SM信令速率：当该无线接入类型下的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ACCESSTYPE|无线接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置用户的无线接入类型，包括Wide Band和NB-IoT。
CTLTYPE|拥塞控制类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置基于RAT拥塞控制的方式，有4种控制方式供选择：承载建立数：当该无线接入类型下已建立承载数超过配置的最大建立承载数时，对其进行拥塞控制 。承载建立速率：当该无线接入类型下建立承载速率超过配置的最大建立承载速率时，对其进行拥塞控制。接收NAS MM信令速率：当该无线接入类型下的用户发送NAS MM信令速率超过配置的最大接收NAS MM信令速率时，对其进行拥塞控制。接收NAS SM信令速率：当该无线接入类型下的用户发送NAS SM信令速率超过配置的最大接收NAS SM信令速率时，对其进行拥塞控制。
MAXBEAR|最大建立承载数|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立数”时，该参数用于指示可支持的最大建立承载数，超过此配置值时进行拥塞控制。
MAXRATE|最大建立承载速率（个/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立速率”时，该参数用于指示可支持的最大建立承载速率，超过此配置值时进行拥塞控制。
MAXNASMM|最大接收NAS MM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时进行拥塞控制。
MAXNASSM|最大接收NAS SM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时进行拥塞控制。
CPUTHRESHOLD|CPU拥塞门限|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“CPU拥塞门限”时，该参数用于指示系统CPU占用率超过配置的CPU拥塞门限时，对该无线接入类型下的用户进行拥塞控制。
REJECTRATE|拒绝比例|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“承载建立速率”或“接收NAS MM信令速率”或“接收NAS SM信令速率”时，该参数用于指示使用这三种拥塞控制方式时，拒绝新接入业务的比例。
BACKOFFTIMESTART|拒绝时携带的Back-off Timer最小取值(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最小值。当用户发起业务，系统判断由于达到RAT拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值(秒)”与“拒绝时携带的Back-off Timer最大取值(秒)”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
BACKOFFTIMEEND|拒绝时携带的Back-off Timer最大取值(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端Backoff Timer的最大值。当用户发起业务，系统判断由于达到RAT拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Backoff Timer。如果本参数为0，表示不携带Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Back-off Timer最小取值(秒)”与“拒绝时携带的Back-off Timer最大取值(秒)”的范围内随机选择。终端在Backoff Timer时间内不再发起业务。用户4G接入时，如果MME没有携带Back-off Timer给UE，则业务重试时长取决于终端行为，通常终端启动默认定时器3411， 10秒后发起业务重试；连续重试4次失败后，终端通常在12分钟后再重新尝试4G接入。PDN连接建立时，MME携带Back-off Timer给UE，指示UE在Back-off Timer超时后，再重新尝试PDN连接建立。
命令举例 
查询RAT拥塞控制策略。 
SHOW RAT CONGESTION POLICY; 
`
命令 (No.1): SHOW RAT CONGESTION POLICY
操作维护         无线接入类型   拥塞控制类型         最大建立承载数   最大建立承载速率   最大接收NAS MM信令速率   最大接收NAS SM信令速率   拒绝比例   拒绝时携带的Back-off Timer最小取值(秒)   拒绝时携带的Back-off Timer最大取值(秒)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   NB-IoT         接收NAS MM信令速率                                       4294967295                                        100        600                                      1800
复制 修改 删除   NB-IoT         承载建立数           1                                                                                                600                                      1800
复制 修改 删除   Wide Band      承载建立数           1                                                                                                600                                      1800
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 3
命令执行成功（耗时 0.092 秒）。
` 
父主题： [RAT拥塞控制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 控制面数据拥塞控制配置 
### 控制面数据拥塞控制配置 
背景知识 
控制面数据拥塞控制，属于3GPP协议标准的NAS拥塞控制；控制面数据拥塞可独立控制和识别，区别于人网和物网其他的拥塞控制，这样，各拥塞门限也可独立控制，例如人网拥塞门限可以设置高于物联网控制面数据拥塞门限，增加拥塞控制灵活度。 
功能描述 
MME控制面数据传送过负荷时，可以限制UE的控制面数据传输，通过下发UE新增的“Control Plane data back-off timer”T3448 来实施针对控制面数据传输的退让时间。 
相关主题 
 
控制面数据拥塞控制开关
 
 
控制面数据拥塞控制策略
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 控制面数据拥塞控制开关 
#### 控制面数据拥塞控制开关 
背景知识 
控制面数据拥塞控制，属于3GPP协议标准的NAS拥塞控制；控制面数据拥塞可独立控制和识别。 
功能描述 
控制面数据拥塞控制开关设置MME是否支持控制面数据拥塞控制，和当MME控制面数据拥塞时，是否支持控制面数据传送转用户面数据传送。 
相关主题 
 
设置控制面数据拥塞控制开关(SET CONTROL PLANE DATA CONGESTION SWITCH)
 
 
查询控制面数据拥塞控制开关(SHOW CONTROL PLANE DATA CONGESTION SWITCH)
 
 
父主题： [控制面数据拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置控制面数据拥塞控制开关(SET CONTROL PLANE DATA CONGESTION SWITCH) 
##### 设置控制面数据拥塞控制开关(SET CONTROL PLANE DATA CONGESTION SWITCH) 
命令功能 
该命令用于设置是否支持控制面数据拥塞控制。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPCPCONG|支持控制面数据拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持控制面数据拥塞控制。
SUPCGECPTOUP|支持拥塞时控制面数据转用户面数据传送|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME控制面数据拥塞时，是否支持控制面数据传送转用户面数据传送。
命令举例 
设置控制面数据拥塞控制开关，不支持控制面数据拥塞控制，不支持拥塞时控制面数据转用户面数据传送。 
SET CONTROL PLANE DATA CONGESTION SWITCH:SUPCPCONG="NO",SUPCGECPTOUP="NO"; 
父主题： [控制面数据拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询控制面数据拥塞控制开关(SHOW CONTROL PLANE DATA CONGESTION SWITCH) 
##### 查询控制面数据拥塞控制开关(SHOW CONTROL PLANE DATA CONGESTION SWITCH) 
命令功能 
该命令用于查询是否支持控制面数据拥塞控制。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPCPCONG|支持控制面数据拥塞控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持控制面数据拥塞控制。
SUPCGECPTOUP|支持拥塞时控制面数据转用户面数据传送|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当MME控制面数据拥塞时，是否支持控制面数据传送转用户面数据传送。
命令举例 
查询控制面数据拥塞控制开关。 
SHOW CONTROL PLANE DATA CONGESTION SWITCH 
`
命令 (No.1): SHOW CONTROL PLANE DATA CONGESTION SWITCH;
操作维护           支持控制面数据拥塞控制    支持拥塞时控制面数据转用户面数据传送   
--------------------------------------------------------------------------------
修改               不支持                    不支持                                               
--------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [控制面数据拥塞控制开关]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 控制面数据拥塞控制策略 
#### 控制面数据拥塞控制策略 
背景知识 
控制面数据拥塞控制，属于3GPP协议标准的NAS拥塞控制；控制面数据拥塞可独立控制和识别，区别于人网和物网其他的拥塞控制，这样，各拥塞门限也可独立控制，例如人网拥塞门限可以设置高于物联网控制面数据拥塞门限，增加拥塞控制灵活度。 
功能描述 
MME控制面数据传送过负荷时，可以限制UE的控制面数据传输，当MME最大接收CP业务请求信令速率大于设置门限时，通过下发UE新增的“Control Plane data back-off timer”T3448 来实施针对控制面数据传输的退让时间。 
相关主题 
 
设置控制面数据拥塞控制策略(SET CONTROL PLANE DATA CONGESTION POLICY)
 
 
查询控制面数据拥塞控制策略(SHOW CONTROL PLANE DATA CONGESTION POLICY)
 
 
父主题： [控制面数据拥塞控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置控制面数据拥塞控制策略(SET CONTROL PLANE DATA CONGESTION POLICY) 
##### 设置控制面数据拥塞控制策略(SET CONTROL PLANE DATA CONGESTION POLICY) 
命令功能 
该命令用于设置控制面数据拥塞策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MAXCPSERVREQ|最大接收CP业务请求信令速率（条/秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|该参数用于设置可支持的最大CP业务请求信令速率，超过此配置值时进行控制面数据拥塞控制。
CPBACKOFFTIMESTART|拒绝时携带的Control Plane data Back-off Timer最小取值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~11160。|该参数用于指示下发给终端发起Control Plane data Back-off Timer的最小值。当用户发起Control Plane Service Request，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Control Plane data Back- off Timer。如果本参数为0，表示不携带Control Plane data Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Control Plane data Back-off Timer最小取值(秒)”与“拒绝时携带的Control Plane data Back-off Timer最大取值(秒)”的范围内随机选择。终端在Control Plane data Back- off Timer时间内不再发起Control Plane Service Request。
CPBACKOFFTIMEEND|拒绝时携带的Control Plane data Back-off Timer最大取值(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~11160。|该参数用于指示下发给终端发起Control Plane data Back-off Timer的最大值。当用户发起Control Plane Service Request，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Control Plane data Back- off Timer。如果本参数为0，表示不携带Control Plane data Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Control Plane data Back-off Timer最小取值(秒)”与“拒绝时携带的Control Plane data Back-off Timer最大取值(秒)”的范围内随机选择。终端在Control Plane data Back- off Timer时间内不再发起Control Plane Service Request。
REJECTRATE|拒绝比例|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置拒绝新接入Control Plane Service Request的比例。
命令举例 
设置控制面数据拥塞控制策略，将最大接收CP业务请求信令速率设置为0，拒绝时携带的Control Plane data Back-off Timer最小取值设置为600s，最大取值设置为1800s，拒绝比例设置为100。 
SET CONTROL PLANE DATA CONGESTION POLICY:MAXCPSERVREQ=0,CPBACKOFFTIMESTART=600,CPBACKOFFTIMEEND=1800,REJECTRATE=100; 
父主题： [控制面数据拥塞控制策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询控制面数据拥塞控制策略(SHOW CONTROL PLANE DATA CONGESTION POLICY) 
##### 查询控制面数据拥塞控制策略(SHOW CONTROL PLANE DATA CONGESTION POLICY) 
命令功能 
该命令用于查询控制面数据拥塞策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MAXCPSERVREQ|最大接收CP业务请求信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|该参数用于设置可支持的最大CP业务请求信令速率，超过此配置值时进行控制面数据拥塞控制。
CPBACKOFFTIMESTART|拒绝时携带的Control Plane data Back-off Timer最小取值(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端发起Control Plane data Back-off Timer的最小值。当用户发起Control Plane Service Request，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Control Plane data Back- off Timer。如果本参数为0，表示不携带Control Plane data Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Control Plane data Back-off Timer最小取值(秒)”与“拒绝时携带的Control Plane data Back-off Timer最大取值(秒)”的范围内随机选择。终端在Control Plane data Back- off Timer时间内不再发起Control Plane Service Request。
CPBACKOFFTIMEEND|拒绝时携带的Control Plane data Back-off Timer最大取值(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给终端发起Control Plane data Back-off Timer的最大值。当用户发起Control Plane Service Request，系统判断由于达到拥塞控制条件而拒绝此业务时，通过本参数确定拒绝消息中是否携带Control Plane data Back- off Timer。如果本参数为0，表示不携带Control Plane data Back-off Timer信息给UE。如果本参数不为0，此字段取值在“拒绝时携带的Control Plane data Back-off Timer最小取值(秒)”与“拒绝时携带的Control Plane data Back-off Timer最大取值(秒)”的范围内随机选择。终端在Control Plane data Back- off Timer时间内不再发起Control Plane Service Request。
REJECTRATE|拒绝比例|参数可选性:任选参数；参数类型:整数。|该参数用于设置拒绝新接入Control Plane Service Request的比例。
命令举例 
查询控制面数据拥塞控制策略。 
SHOW CONTROL PLANE DATA CONGESTION POLICY 
`
命令 (No.1): SHOW CONTROL PLANE DATA CONGESTION POLICY;
操作维护           最大接收CP业务请求信令速率    拒绝时携带的Control Plane data Back-off Timer最小取值(秒)   拒绝时携带的Control Plane data Back-off Timer最大取值(秒)    拒绝比例
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改               0                               600                                                           1800                                                100                        
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [控制面数据拥塞控制策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME拥塞控制管理 
### MME拥塞控制管理 
背景知识 
拥塞控制是指在网络中，因为各种原因发生业务拥塞时，MME会对接入的业务和用户实施控制，以达到降低业务和整个网络的负荷，保证网元长期有效的正常运行的目的。 
MME拥塞控制区分用户和业务特性，包括： 
 
基于APN的拥塞控制。
 
 
基于MTC（Machine Type Communication，机器类通信）用户的拥塞控制。
 
 
基于RAT（Radio Access Technology，无线接入技术）拥塞控制。
 
 
功能描述 
MME的拥塞控制，可以对承载建立速率、MME接收NAS MM信令的速率和接收NAS SM信令速率设置对应的阈值，当达到阈值时，拥塞机制会起作用。为了方便运营商在商用局上部署拥塞控制，“MME拥塞控制管理”提供信令速率查询，用于根据当前的信令速率，来设置拥塞信令速率阈值： 
 
                        通过
                        SHOW APN CONGESTION
                        命令查询基于APN拥塞控制信令速率。
                    
 
 
查询SHOW MTC USER CONGESTION SIG RATE命令查询基于MTC用户拥塞控制信令速率。
 
 
通过SHOW MTC APN USER CONGESTION SIG RATE命令查询基于MTC用户的APN拥塞控制信令速率。
 
 
通过SHOW RAT CONGESTION SIG RATE命令查询基于RAT拥塞控制信令速率。
 
 
相关主题 
 
查询基于APN拥塞控制信令速率(SHOW APN SIGRATE)
 
 
查询基于MTC用户拥塞控制信令速率(SHOW MTC SIGRATE)
 
 
查询基于MTC用户的APN拥塞控制信令速率(SHOW MTCAPN SIGRATE)
 
 
查询基于RAT拥塞控制信令速率(SHOW RAT SIGRATE)
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于APN拥塞控制信令速率(SHOW APN SIGRATE) 
#### 查询基于APN拥塞控制信令速率(SHOW APN SIGRATE) 
命令功能 
查询基于APN拥塞控制信令速率
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数表示发生拥塞的APN名称。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数表示发生拥塞的APN名称。
CRBEARERRATE|建立承载速率（个/秒）|参数可选性:任选参数；参数类型:整数。|该参数表示建立承载速率(个/秒)。
RENASMMSIGRATE|接收NAS MM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|该参数用于表示接收NAS MM信令速率(个/秒)。
命令举例 
查询基于APN拥塞控制信令速率 
SHOW APN SIGRATE; 
`
命令 (No.1): SHOW APN SIGRATE
APN名称                                         建立承载速率（个/秒）   接收NAS MM信令速率（条/秒）
-------------------------------------------------------------------------------------------------
zte.com.apn.epc.mnc222.mcc333.3gppnetwork.org   12345                   12345
------------------------------------------------------------------------------------------------- 
记录数 1
命令执行成功（耗时 0.231 秒）。
` 
父主题： [MME拥塞控制管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于MTC用户拥塞控制信令速率(SHOW MTC SIGRATE) 
#### 查询基于MTC用户拥塞控制信令速率(SHOW MTC SIGRATE) 
命令功能 
查询基于MTC用户拥塞控制信令速率
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:任选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码(MCC)|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示下发给MTC终端IMSI-Group identifier的Group ID。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码(MCC)|参数可选性:任选参数；参数类型:字符型。|MCC标识移动用户所在国家，比如中国MCC为460。
MNC|移动网号(MNC)|参数可选性:任选参数；参数类型:字符型。|移动网号标识移动用户归属的PLMN网络编号，比如中国电信为03，中国移动为00、02。
GROUPID|Group ID|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给MTC终端IMSI-Group identifier的Group ID。
RENASMMSIGRATE|接收NAS MM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的可保障接收NAS MM信令速率，超过此配置值时对低优先级接入业务进行限制。
RENASSMSIGRATE|接收NAS SM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的可保障接收NAS SM信令速率，超过此配置值时对低优先级接入业务进行限制。
命令举例 
查询基于MTC用户拥塞控制信令速率。 
SHOW MTC SIGRATE; 
`
命令 (No.1): SHOW MTC SIGRATE;
移动国家码(MCC)   移动网号(MNC)   Group ID    接收NAS MM信令速率（条/秒）    接收NAS SM信令速率（条/秒）
-------------------------------------------------------------------------------------------------------
460               60              1           100                            100
-------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.041 秒）。
 ` 
父主题： [MME拥塞控制管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于MTC用户的APN拥塞控制信令速率(SHOW MTCAPN SIGRATE) 
#### 查询基于MTC用户的APN拥塞控制信令速率(SHOW MTCAPN SIGRATE) 
命令功能 
查询基于MTC用户的APN拥塞控制信令速率
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MTCGRPID|MTC Group Identifier|参数可选性:特殊任选参数；参数类型:复合参数|该参数用于指示进行拥塞控制的MTC用户的MTC Group Identifier，MTC Group Identifier由MCC、MNC及Group ID三部分组成。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~16777215。|该参数用于指示下发给MTC终端IMSI-Group identifier的Group ID。
APN|APN名称|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:1~99个字符。|该参数用于指示需进行拥塞控制的APN。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|该参数用于指示MTC Group Identifier的MCC。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|该参数用于指示MTC Group Identifier的MNC。
GROUPID|Group ID|参数可选性:任选参数；参数类型:整数。|该参数用于指示下发给MTC终端IMSI-Group identifier的Group ID。
APN|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于指示需进行拥塞控制的APN。
RENASMMSIGRATE|接收NAS MM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS MM信令速率”时，该参数用于指示可支持的可保障接收NAS MM信令速率，超过此配置值时对低优先级接入业务进行限制。
RENASSMSIGRATE|接收NAS SM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|当“拥塞控制类型”设置为“接收NAS SM信令速率”时，该参数用于指示可支持的可保障接收NAS SM信令速率，超过此配置值时对低优先级接入业务进行限制。
命令举例 
查询基于MTC用户的APN拥塞控制信令速率。 
SHOW MTCAPN SIGRATE; 
`
命令 (No.1): SHOW MTCAPN SIGRATE;
移动国家码(MCC)   移动网号(MNC)   Group ID    APN名称                                            接收NAS MM信令速率（条/秒）    接收NAS SM信令速率（条/秒）
-----------------------------------------------------------------------------------------------------------------------------------------------------------
460               60              1           zte.com.apn.epc.mnc003.mcc460.3gppnetwork.org      100                            100                        
-----------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.041 秒）。
 ` 
父主题： [MME拥塞控制管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询基于RAT拥塞控制信令速率(SHOW RAT SIGRATE) 
#### 查询基于RAT拥塞控制信令速率(SHOW RAT SIGRATE) 
命令功能 
查询基于RAT拥塞控制信令速率
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ACCESSTYPE|无线接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:ALL。|该参数用于表示查询的用户无线接入类型，包括Wide Band和NB-IoT。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ACCESSTYPE|无线接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于表示查询的用户无线接入类型，包括Wide Band和NB-IoT。
CRBEARERRATE|建立承载速率（个/秒）|参数可选性:任选参数；参数类型:整数。|该参数表示建立承载速率(个/秒)。
RENASMMSIGRATE|接收NAS MM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|该参数用于表示接收NAS MM信令速率(个/秒)。
RENASSMSIGRATE|接收NAS SM信令速率（条/秒）|参数可选性:任选参数；参数类型:整数。|该参数用于表示接收NAS SM信令速率(个/秒)。
命令举例 
查询基于RAT拥塞控制信令速率 
SHOW RAT SIGRATE; 
`
命令 (No.1): SHOW RAT SIGRATE
无线接入类型    建立承载速率（个/秒）   接收NAS MM信令速率（条/秒）   接收NAS SM信令速率（条/秒）
-------------------------------------------------------------------------------------------------
Wide Band       12345                   100                           100
------------------------------------------------------------------------------------------------- 
记录数 1
命令执行成功（耗时 0.231 秒）。
` 
父主题： [MME拥塞控制管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME/SGSN网管过负荷控制参数配置 
### MME/SGSN网管过负荷控制参数配置 
背景知识 
当业务处理单元发生过负荷的时候，为了优先保证用户的正常业务，需要对信令跟踪、失败观察等网管类的功能进行控制，停止向网管上报信令，把对应的系统消耗留出来给业务使用，达到优先保障业务正常运行的目的。 
功能描述 
本功能用于配置在网元发生过负荷的时候，控制业务进程单用户信令跟踪、全用户信令跟踪、接口信令跟踪以及失败观察等是否上报给网管。 
相关主题 
 
设置MME/SGSN网管过负荷控制参数(SET MMESGSNOMMCPUOLCFG)
 
 
查询MME/SGSN网管过负荷控制参数(SHOW MMESGSNOMMCPUOLCFG)
 
 
父主题： [拥塞和过负荷控制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置MME/SGSN网管过负荷控制参数(SET MMESGSNOMMCPUOLCFG) 
#### 设置MME/SGSN网管过负荷控制参数(SET MMESGSNOMMCPUOLCFG) 
命令功能 
该命令用于设置网管过负荷控制参数，包括全用户信令跟踪优先级、单用户信令跟踪优先级、接口信令跟踪优先级、全用户失败观察优先级、单用户失败观察优先级。在网元发生过负荷的时候，控制业务进程的单用户信令跟踪、全用户信令跟踪、接口信令跟踪这些信令是否上报给网管。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
OMMALLSIGCFG|全用户信令跟踪优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置全用户信令跟踪优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报全用户的信令跟踪给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对全用户信令跟踪进行控制，不再上报信令给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对全用户信令跟踪进行控制，不再上报信令给网管。
OMMSINGLESIGCFG|单用户信令跟踪优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置单用户信令跟踪优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报单用户的信令跟踪给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对单用户信令跟踪进行控制，不再上报信令给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对单用户信令跟踪进行控制，不再上报信令给网管。
OMMINTERFACESIGCFG|接口信令跟踪优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置全接口信令跟踪优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报接口的信令跟踪给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对接口信令跟踪进行控制，不再上报信令给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对接口信令跟踪进行控制，不再上报信令给网管。
OMMALLFAILCFG|全用户失败观察优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置全用户失败观察优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报全用户的失败观察给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对全用户失败观察进行控制，不再上报失败观察给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对全用户失败观察进行控制，不再上报失败观察给网管。
OMMSINGLEFAILCFG|单用户失败观察优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置单用户失败观察优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报单用户的失败观察给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对单用户失败观察进行控制，不再上报失败观察给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对单用户失败观察进行控制，不再上报失败观察给网管。
命令举例 
设置MME/SGSN网管过负荷控制参数。全用户信令跟踪优先级为优先级低，单用户信令跟踪优先级为优先级高，接口信令跟踪优先级为优先级低。 
SET MMESGSNOMMCPUOLCFG:OMMALLSIGCFG="LOW",OMMSINGLESIGCFG="HIGH",OMMINTERFACESIGCFG="LOW" 
父主题： [MME/SGSN网管过负荷控制参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MME/SGSN网管过负荷控制参数(SHOW MMESGSNOMMCPUOLCFG) 
#### 查询MME/SGSN网管过负荷控制参数(SHOW MMESGSNOMMCPUOLCFG) 
命令功能 
该命令用于查询网管过负荷控制配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OMMALLSIGCFG|全用户信令跟踪优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置全用户信令跟踪优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报全用户的信令跟踪给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对全用户信令跟踪进行控制，不再上报信令给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对全用户信令跟踪进行控制，不再上报信令给网管。
OMMSINGLESIGCFG|单用户信令跟踪优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置单用户信令跟踪优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报单用户的信令跟踪给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对单用户信令跟踪进行控制，不再上报信令给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对单用户信令跟踪进行控制，不再上报信令给网管。
OMMINTERFACESIGCFG|接口信令跟踪优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置全接口信令跟踪优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报接口的信令跟踪给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对接口信令跟踪进行控制，不再上报信令给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对接口信令跟踪进行控制，不再上报信令给网管。
OMMALLFAILCFG|全用户失败观察优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置全用户失败观察优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报全用户的失败观察给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对全用户失败观察进行控制，不再上报失败观察给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对全用户失败观察进行控制，不再上报失败观察给网管。
OMMSINGLEFAILCFG|单用户失败观察优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置单用户失败观察优先级，包括三个选项：不控制、低优先级和高优先级。设置参数为不控制，当MME/SGSN启用CPU过负荷控制功能，无论CPU是否处于过负荷，MME/SGSN都会上报单用户的失败观察给网管。设置参数为低优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载），则MME/SGSN都会对单用户失败观察进行控制，不再上报失败观察给网管。设置参数为高优先级，当MME/SGSN启用CPU过负荷控制功能，如果当前CPU的负荷等级处于一级过负荷（高过载），则MME/SGSN都会对单用户失败观察进行控制，不再上报失败观察给网管。
命令举例 
查询MME/SGSN网管过负荷控制参数。 
SHOW MMESGSNOMMCPUOLCFG 
`
命令 (No.1): SHOW MMESGSNOMMCPUOLCFG;
操作维护   全用户信令跟踪优先级为   单用户信令跟踪优先级   接口信令跟踪优先级  全用户失败观察优先级  单用户失败观察优先级
--------------------------------------------------------------------------------------------------------------------------------
修改       优先级低                优先级高              优先级低           优先级低             优先级低
--------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.06 秒）。
` 
父主题： [MME/SGSN网管过负荷控制参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 软件参数配置 
## 软件参数配置 
背景知识 
由于某些功能或者应用场景的需要，MME可以通过设置系统内部自定义的参数，对非协议要求的或一些特殊场景下使用的功能进行控制。 
功能描述 
软件参数配置功能提供了系统内部自定义参数的设置，对业务流程、系统控制、非协议要求的或个别功能进行简单灵活控制。 
相关主题 
 
增加软件参数配置(ADD SOFTWARE PARAMETER)
 
 
设置软件参数配置(SET SOFTWARE PARAMETER)
 
 
删除软件参数配置(DEL SOFTWARE PARAMETER)
 
 
查询软件参数配置(SHOW SOFTWARE PARAMETER)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 增加软件参数配置(ADD SOFTWARE PARAMETER) 
### 增加软件参数配置(ADD SOFTWARE PARAMETER) 
命令功能 
该命令用于增加软件参数配置。 
[所有软参详细说明]
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PARAID|软件参数ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置软件参数编号。
PARANAME|参数变量名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~40个字符。|本参数用于设置参数变量名。
DFTVALUE|参数缺省值|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置参数缺省值。
PARAVALUE|参数当前值|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置参数当前值。
MINVAL|参数最小值|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置参数最小值。
MAXVAL|参数最大值|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置参数最大值。
VALRANGE|参数范围|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|本参数用于设置参数范围。
NAME|参数名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~200个字符。|本参数用于设置参数名称。
REMARK|备注|参数可选性:任选参数；参数类型:字符型；参数范围为:0~4000个字符。|本参数用于设置备注说明。
命令举例 
增加软件参数，软件参数ID为9999，软件参数值为111，软参名为bCode，最小值为1，最大值为1000。 
ADD SOFTWARE PARAMETER:PARAID=9999,PARANAME="bCode",DFTVALUE=1,PARAVALUE=111,MINVAL=1,MAXVAL=1000,NAME="MME_para"; 
父主题： [软件参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置软件参数配置(SET SOFTWARE PARAMETER) 
### 设置软件参数配置(SET SOFTWARE PARAMETER) 
命令功能 
该命令用于设置系统内部自定义的参数，非协议要求的或个别功能的开关，比如是否启用资源异常回收控制开关。 
[所有软参详细说明]
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PARAID|软件参数ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置软件参数编号。
PARAVALUE|软件参数值|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置参数当前值。
命令举例 
设置软件参数，软件参数ID为786685，软件参数值为1。 
SET SOFTWARE PARAMETER:PARAID=786685,PARAVALUE=1; 
父主题： [软件参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除软件参数配置(DEL SOFTWARE PARAMETER) 
### 删除软件参数配置(DEL SOFTWARE PARAMETER) 
命令功能 
该命令用于删除软件参数配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PARAID|软件参数ID|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置软件参数编号。
命令举例 
删除软件参数，软件参数ID为9999。 
DEL SOFTWARE PARAMETER:PARAID=9999; 
父主题： [软件参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询软件参数配置(SHOW SOFTWARE PARAMETER) 
### 查询软件参数配置(SHOW SOFTWARE PARAMETER) 
命令功能 
该命令用于查询软件参数配置。 
[所有软参详细说明]
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PARAID|软件参数ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|本参数用于设置软件参数编号。
NAME|参数名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~200个字符。|本参数用于设置参数名称。
FLAG|修改标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|本参数用于设置软件参数的修改标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PARAID|软件参数ID|参数可选性:任选参数；参数类型:整数。|本参数用于设置软件参数编号。
DFTVALUE|参数缺省值|参数可选性:任选参数；参数类型:整数。|本参数用于设置参数缺省值。
PARAVALUE|参数当前值|参数可选性:任选参数；参数类型:整数。|本参数用于设置参数当前值。
MINVAL|参数最小值|参数可选性:任选参数；参数类型:整数。|本参数用于设置参数最小值。
MAXVAL|参数最大值|参数可选性:任选参数；参数类型:整数。|本参数用于设置参数最大值。
NAME|参数名称|参数可选性:任选参数；参数类型:字符型。|本参数用于设置参数名称。
REMARK|备注|参数可选性:任选参数；参数类型:字符型；参数范围为:0~4000个字符。|本参数用于设置备注说明。
命令举例 
查询软件参数配置，修改标识为“已修改”。 
SHOW SOFTWARE PARAMETER:FLAG="CHANGED"; 
`
命令 (No.1): SHOW SOFTWARE PARAMETER:FLAG="CHANGED";
操作维护  软件参数ID   参数缺省值   参数当前值   参数最小值   参数最大值   参数名称                                           备注
----------------------------------------------------------------------------------------------------------------------------------
修改      65672        1            0            0            1            支持使用正则节点名查询S11口的SGW                   0–不支持;1-支持
修改      65673        1            0            0            1            支持DNS ANY类型C-NAME查询                          0–不支持;1-支持
修改      65685        1            0            0            1            是否支持超长UE无线能力                             0-不支持;1-支持
修改      262356       1            0            0            1            支持Support Feature协商                            0-不支持;1-支持
修改      262448       1            0            0            1            ULR消息是否携带IMEISV                              0-否; 1-是
修改      262466       1            0            0            1            支持HSS返回5001失败统计到用户原因的EPS服务不允许   0-否;1-是
修改      262473       1            0            0            1            MME 网络侧分离时业务请求建承载                     0-否; 1-是
----------------------------------------------------------------------------------------------------------------------------------
记录数 7
命令执行成功（耗时 0.047 秒）。
` 
父主题： [软件参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 资源告警配置 
## 资源告警配置 
背景知识 
            
            为了保证网络的正常运行，本网元的注册用户数、在线用户数、PDP数量和动态资源达到一定的容量比例时，需要进行告警，以便运营商及时考虑扩容。
        
功能描述 
资源告警配置包括业务量拥塞统计配置和动态资源使用率告警参数配置。 
业务量拥塞统计配置用于设置X网元的注册用户数、在线用户数、PDP使用数量的不同告警级别门限和告警恢复门限。 
动态资源使用率告警参数配置设置本网元的动态表占用率告警门限和告警恢复门限。 
相关主题 
 
业务量拥塞统计配置
 
 
动态资源使用率告警参数配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 业务量拥塞统计配置 
### 业务量拥塞统计配置 
背景知识 
业务量拥塞统计配置是指当系统的各种资源（如用户数量或承载数量）将要到达了License容量的门限，进行提前预警，以便运营商及时采取扩容等措施，以免资源不足导致用户业务失败，对运营商造成损失。 
 
对于纯SGSN局，受License控制容量的资源项目包括PDP上下文、2G在线用户数、3G在线用户数、在线用户数、2G注册用户数、3G注册用户数、注册用户数。
 
 
对于纯MME局，受License控制容量的资源项目包括PDP上下文、在线用户数、注册用户数。
 
 
对于Combo局，受License控制容量的资源项目包括PDP上下文、2G在线用户数、3G在线用户数、LTE在线用户数、在线用户数、2G注册用户数、3G注册用户数、LTE注册用户数和注册用户数。
 
 
功能描述 
对应不同的局点类型，设置对应容量受License控制的告警类型，每种告警类型都可以设置四个不同级别的告警门限，每种告警类型都可以设置一个告警恢复门限。 
对于纯SGSN局，告警类型为包括PDP上下文过局容量数据库告警、2G在线用户数过局容量数据库告警、3G在线用户数过局容量数据库告警、在线用户数过局容量数据库告警、2G注册用户数过局容量数据库告警、3G注册用户数过局容量数据库告警、注册用户数过局容量数据库告警。 
 
SGSN根据当前统计的占用PDP数量和License容量的比例，判断是否需要上报告警以及上报几级告警，或恢复当前告警。
 
 
SGSN根据统计的各种类型的用户数及和对应的License容量的比例，判断是否需要上报告警以及上报几级告警，或恢复当前告警。
 
 
对于纯MME局，告警包括PDP上下文过局容量数据库告警、在线用户数过局容量数据库告警和注册用户数过局容量数据库告警。 
 
MME根据当前统计的占用PDP（承载）数量和PDP的License容量的比例，判断是否需要上报告警以及上报几级告警，或恢复当前告警。
 
 
MME根据统计的各种类型的用户数及对应的License容量的比例，判断是否需要上报告警以及上报几级告警，或恢复当前告警。
 
 
对于Combo局，告警包括PDP上下文过局容量数据库告警、2G在线用户数过局容量数据库告警、3G在线用户数过局容量数据库告警、LTE在线用户数过局容量数据库告警、在线用户数过局容量数据库告警、2G注册用户数过局容量数据库告警、3G注册用户数过局容量数据库告警、LTE注册用户数过局容量数据库告警和注册用户数过局容量数据库告警。 
 
Combo局根据当前统计的占用PDP（PDP和承载）数量和PDP的License容量的比例，判断是否需要上报告警以及上报几级告警，或恢复当前告警。
 
 
Combo根据统计的各种类型的用户数和对应的License容量的比例，判断是否需要上报告警以及上报几级告警，或恢复当前告警。
 
 
相关主题 
 
新增资源告警(ADD EQU)
 
 
修改资源告警(SET EQU)
 
 
删除资源告警(DEL EQU)
 
 
查询资源告警(SHOW EQU)
 
 
父主题： [资源告警配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增资源告警(ADD EQU) 
#### 新增资源告警(ADD EQU) 
命令功能 
该命令用于新增资源告警。该告警用于监控全局的用户资源，与license进行比较，进行提前预警，以便运营商及时采取扩容等措施，以免资源不足导致用户业务失败，对运营商造成损失。
注意事项 
该告警共分为4级，1级为最高，4级为最低，低级告警的门限值必须小于高级告警的门限值，告警阈值下限必须小于4级告警门限值。
参数说明 
标识|名称|类型|说明
---|---|---|---
EQUTYPE|告警类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|对应的用户资源告警类型，包括用户数、PDP数等。
HIGHTHRES1|一级告警上报门限|参数可选性:必选参数；参数类型:整数；参数范围为:0~100。|一级告警，用户资源数与对应license的比例高于该上限时，上报该告警。
HIGHTHRES2|二级告警上报门限|参数可选性:必选参数；参数类型:整数；参数范围为:0~100。|二级告警，用户资源数与对应license的比例高于该上限，且低于一级告警阈值上限时，上报该告警。
HIGHTHRES3|三级告警上报门限|参数可选性:必选参数；参数类型:整数；参数范围为:0~100。|三级告警，用户资源数与对应license的比例高于该上限，且低于二级告警阈值上限时，上报该告警。
HIGHTHRES4|四级告警上报门限|参数可选性:必选参数；参数类型:整数；参数范围为:0~100。|四级告警，用户资源数与对应license的比例高于该上限，且低于三级告警阈值上限时上报该告警。
LOWTHRES|告警恢复门限|参数可选性:必选参数；参数类型:整数；参数范围为:1~100。|对于已上报的告警，若用户资源数与对应license的比例低于该下限时，恢复告警。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于标识对应资源告警配置。
命令举例 
新增资源告警，告警类型为PDP上下文过局容量数据库告警（DB_PDP），一级告警阈值上限为9，二级告警阈值上限为8，三级告警阈值上限为7，四级告警阈值上限为6，告警阈值下限为5，用户别名为mm。 
ADD EQU:EQUTYPE="DB_PDP",HIGHTHRES1=9,HIGHTHRES2=8,HIGHTHRES3=7,HIGHTHRES4=6,LOWTHRES=5,NAME="mm"; 
父主题： [业务量拥塞统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改资源告警(SET EQU) 
#### 修改资源告警(SET EQU) 
命令功能 
该命令用于修改资源告警。可修改告警类型、4个级别的告警门限、告警阈值下限、以及用户别名。
注意事项 
该告警共分为4级，1级为最高，4级为最低，低级告警的门限值必须小于高级告警的门限值，告警阈值下限必须小于4级告警门限值。
参数说明 
标识|名称|类型|说明
---|---|---|---
EQUTYPE|告警类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|对应的用户资源告警类型，包括用户数、PDP数等。
HIGHTHRES1|一级告警上报门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|一级告警，用户资源数与对应license的比例高于该上限时，上报该告警。
HIGHTHRES2|二级告警上报门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|二级告警，用户资源数与对应license的比例高于该上限，且低于一级告警阈值上限时，上报该告警。
HIGHTHRES3|三级告警上报门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|三级告警，用户资源数与对应license的比例高于该上限且，低于二级告警阈值上限时，上报该告警。
HIGHTHRES4|四级告警上报门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|四级告警，用户资源数与对应license的比例高于该上限，且低于三级告警阈值上限时上报该告警。
LOWTHRES|告警恢复门限|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|对于已上报的告警，若用户资源数与对应license的比例低于该下限时，恢复告警。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于标识对应资源告警配置。
命令举例 
修改资源告警，告警类型为PDP上下文过局容量数据库告警（DB_PDP），一级告警阈值上限改为75，二级告警阈值上限改为45，三级告警阈值上限改为15，四级告警阈值上限改为10，告警阈值下限改为2，用户别名改为ippool。 
SET EQU:EQUTYPE="DB_PDP",HIGHTHRES1=75,HIGHTHRES2=45,HIGHTHRES3=15,HIGHTHRES4=10,LOWTHRES=2,NAME="ippool"; 
父主题： [业务量拥塞统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除资源告警(DEL EQU) 
#### 删除资源告警(DEL EQU) 
命令功能 
该命令用于删除资源告警。删除对应资源告警对业务不会造成影响，但是在用户资源超出license限制时将不会上报告警。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
EQUTYPE|告警类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|对应的用户资源告警类型，包括用户数、PDP数等。
命令举例 
删除告警类型为PDP上下文过局容量数据库告警（DB_PDP）的资源告警。 
DEL EQU:EQUTYPE="DB_PDP"; 
父主题： [业务量拥塞统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询资源告警(SHOW EQU) 
#### 查询资源告警(SHOW EQU) 
命令功能 
该命令用于查询资源告警。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
EQUTYPE|告警类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|对应的用户资源告警类型，包括用户数、PDP数等。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
EQUTYPE|告警类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|对应的用户资源告警类型，包括用户数、PDP数等。
HIGHTHRES1|一级告警上报门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|一级告警，用户资源数与对应license的比例高于该上限时，上报该告警。
HIGHTHRES2|二级告警上报门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|二级告警，用户资源数与对应license的比例高于该上限，且低于一级告警阈值上限时，上报该告警。
HIGHTHRES3|三级告警上报门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|三级告警，用户资源数与对应license的比例高于该上限且，低于二级告警阈值上限时，上报该告警。
HIGHTHRES4|四级告警上报门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|四级告警，用户资源数与对应license的比例高于该上限，且低于三级告警阈值上限时上报该告警。
LOWTHRES|告警恢复门限|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|对于已上报的告警，若用户资源数与对应license的比例低于该下限时，恢复告警。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于标识对应资源告警配置。
命令举例 
查询告警类型为PDP上下文过局容量数据库告警（DB_PDP）的资源告警。 
SHOW EQU:EQUTYPE="DB_PDP"; 
`
命令 (No.1): SHOW EQU:EQUTYPE="DB_PDP";
操作维护         告警类型                          一级告警上报门限   二级告警上报门限   三级告警上报门限   四级告警上报门限   告警恢复门限   用户别名
------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   PDP上下文过局容量数据库告警       95                 90                 80                 70                 65             
------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.098 秒）。
` 
父主题： [业务量拥塞统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 动态资源使用率告警参数配置 
### 动态资源使用率告警参数配置 
背景知识 
系统中有数据区、缓存、标识索引、表等不同类型的动态资源，为了监控这些动态资源的使用状况，系统提供了动态资源使用率告警（包括“表容量使用率过高告警”和“系统资源容量不足告警”），当动态资源占用率过高时上报告警，提醒运维人员及时采取扩容处理措施或者联系中兴通讯支持，以免资源不足导致用户业务失败，对运营商造成损失。 
功能描述 
本配置包括缺省动态资源使用率告警参数配置、特定动态资源使用率告警参数配置。 
相关主题 
 
缺省动态资源使用率告警参数配置
 
 
特定动态资源使用率告警参数配置
 
 
父主题： [资源告警配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 缺省动态资源使用率告警参数配置 
#### 缺省动态资源使用率告警参数配置 
背景知识 
系统中有数据区、缓存、表等不同类型的动态资源，为了监控这些动态资源的使用状况，系统提供了动态资源占用率告警（包括“表容量使用率过高告警”和“系统资源容量不足告警”），当动态资源占用率过高时上报告警，提醒运维人员及时采取扩容处理措施或者联系中兴通讯支持，以免资源不足导致用户业务失败，对运营商造成损失。 
系统对动态资源使用率告警参数提供了一条缺省的配置，正常场景下都使用这条缺省的动态资源使用率告警参数配置进行告警上报。 
为了防止外场某些特定动态资源占用率和其他动态资源差别较大，导致误报或者漏报告警，系统提供灵活配置，可以针对特定动态资源，配置特定的告警参数，来灵活上报告警。系统优先使用特定动态资源告警配置参数来进行告警上报，当对该动态资源没有配置特定动态资源告警参数时，系统再使用缺省的动态资源使用率进行告警上报。 
功能描述 
本节点用于配置缺省的动态资源使用率告警参数，参数包括“一级告警门限值”，“二级告警门限值”，“三级告警门限值”，“恢复告警门限值”。 
相关主题 
 
修改缺省动态资源使用率告警参数配置(SET DRA)
 
 
查询缺省动态资源使用率告警参数配置(SHOW DRA)
 
 
父主题： [动态资源使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 修改缺省动态资源使用率告警参数配置(SET DRA) 
##### 修改缺省动态资源使用率告警参数配置(SET DRA) 
命令功能 
该命令用于修改缺省动态资源使用率告警参数配置，参数包括各级告警门限和恢复门限。动态资源使用率达到某一级别门限后，将会上报对应的动态资源使用率告警。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
LEVEL1VALUE|一级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|动态资源使用率达到该门限后，将会上报对应的动态资源使用率一级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL2VALUE|二级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|动态资源使用率达到该门限后，将会上报对应的动态资源使用率二级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL3VALUE|三级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|动态资源使用率达到该门限后，将会上报对应的动态资源使用率三级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
RESTOREVALUE|恢复告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|在上报告警后，一旦动态资源使用率低于该告警恢复门限，将恢复告警。
命令举例 
修改缺省动态资源使用率告警参数配置，设置一级告警门限值为90%，二级告警门限值为80%，三级告警门限值为70%，恢复告警门限值为65%。 
SET DRA:LEVEL1VALUE=90,LEVEL2VALUE=80,LEVEL3VALUE=70,RESTOREVALUE=65 
相关命令 
[查询动态资源使用率告警参数]
父主题： [缺省动态资源使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询缺省动态资源使用率告警参数配置(SHOW DRA) 
##### 查询缺省动态资源使用率告警参数配置(SHOW DRA) 
命令功能 
该命令用于查询缺省动态资源使用率告警参数配置，参数包括各级告警门限和恢复门限。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LEVEL1VALUE|一级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|动态资源使用率达到该门限后，将会上报对应的动态资源使用率一级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL2VALUE|二级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|动态资源使用率达到该门限后，将会上报对应的动态资源使用率二级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL3VALUE|三级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|动态资源使用率达到该门限后，将会上报对应的动态资源使用率三级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
RESTOREVALUE|恢复告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|在上报告警后，一旦动态资源使用率低于该告警恢复门限，将恢复告警。
命令举例 
查询缺省动态资源使用率告警参数配置。 
SHOW DRA 
`
(No.29) : SHOW DRA
-----------------uMAC_MME_Combo_B5/NFS_MMESGSN_0----------------
操作维护       一级告警门限值(%) 二级告警门限值(%) 三级告警门限值(%) 恢复告警门限值(%) 
---------------------------------------------------------------------------------------
修改           90                80                70                65                
---------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-06 20:36:10 耗时: 1.347秒。
` 
父主题： [缺省动态资源使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 特定动态资源使用率告警参数配置 
#### 特定动态资源使用率告警参数配置 
背景知识 
系统中有数据区、缓存、表等不同类型的动态资源，为了监控这些动态资源的使用状况，系统提供了动态资源占用率告警（包括“表容量使用率过高告警”和“系统资源容量不足告警”），当动态资源占用率过高时上报告警，提醒运维人员及时采取扩容处理措施或者联系中兴通讯支持，以免资源不足导致用户业务失败，对运营商造成损失。 
系统对动态资源使用率告警参数提供了一条缺省的配置，正常场景下都使用这条缺省的动态资源使用率告警参数配置进行告警上报。 
为了防止外场某些特定动态资源占用率和其他动态资源差别较大，导致误报或者漏报告警，系统提供灵活配置，可以针对特定动态资源，配置特定的告警参数，来灵活上报告警。系统优先使用特定动态资源告警配置参数来进行告警上报，当对该动态资源没有配置特定动态资源告警参数时，系统再使用缺省的动态资源使用率进行告警上报。 
比如针对DNS缓存数据区，由于DNS缓存数据区本身就可以老化，如果在本地缓存查不到数据，还可以查DNS服务器，所以告警门限相对高于其他动态资源。这时可以使用资源名称为“DNSCacheDataArea”进行特定的告警参数配置。 
该配置需要在中兴通讯工程师的指导下进行。 
功能描述 
本节点用于配置系统特定动态资源使用率告警参数，参数包括“资源名称”，“一级告警门限值”，“二级告警门限值”，“三级告警门限值”，“恢复告警门限值”，即可以针对特定资源，配置不同的动态资源使用率告警参数。 
相关主题 
 
新增特定动态资源使用率告警参数配置(ADD SPECDRA)
 
 
修改特定动态资源使用率告警参数配置(SET SPECDRA)
 
 
删除特定动态资源使用率告警参数配置(DEL SPECDRA)
 
 
查询特定动态资源使用率告警参数配置(SHOW SPECDRA)
 
 
父主题： [动态资源使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 新增特定动态资源使用率告警参数配置(ADD SPECDRA) 
##### 新增特定动态资源使用率告警参数配置(ADD SPECDRA) 
命令功能 
该命令用于新增特定动态资源使用率告警参数配置，参数包括资源名称，各级告警门限和恢复门限。当该种动态资源使用率达到某一级别门限后，将会上报对应的动态资源使用率告警。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|资源名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于标识系统中各种数据区、缓存、标识索引、表等不同类型的动态资源名称。
LEVEL1VALUE|一级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。默认值:90。|该参数用于设置一级告警门限值。当该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率一级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL2VALUE|二级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。默认值:80。|该参数用于设置二级告警门限值。该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率二级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL3VALUE|三级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。默认值:70。|该参数用于设置三级告警门限值。该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率三级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
RESTOREVALUE|恢复告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。默认值:65。|该种资源在上报告警后，一旦该动态资源使用率低于该告警恢复门限，将恢复告警。
命令举例 
新增特定动态资源使用率告警参数配置，其中资源名称为“DNSCacheDataArea”，一级告警门限值为90%，二级告警门限值为80%，三级告警门限值为70%，恢复告警门限值为65%。 
ADD SPECDRA:NAME="DNSCacheDataArea",LEVEL1VALUE=90,LEVEL2VALUE=80,LEVEL3VALUE=70,RESTOREVALUE=65 
相关命令 
[修改特定动态资源使用率告警参数配置]
[删除特定动态资源使用率告警参数配置]
[查询特定动态资源使用率告警参数配置]
父主题： [特定动态资源使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 修改特定动态资源使用率告警参数配置(SET SPECDRA) 
##### 修改特定动态资源使用率告警参数配置(SET SPECDRA) 
命令功能 
该命令用于修改特定动态资源使用率告警参数配置，参数包括资源名称，各级告警门限和恢复门限。当该种动态资源使用率达到某一级别门限后，将会上报对应的动态资源使用率告警。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|资源名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于标识系统中各种数据区、缓存、标识索引、表等不同类型的动态资源名称。
LEVEL1VALUE|一级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置一级告警门限值。当该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率一级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL2VALUE|二级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置二级告警门限值。该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率二级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL3VALUE|三级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置三级告警门限值。该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率三级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
RESTOREVALUE|恢复告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该种资源在上报告警后，一旦该动态资源使用率低于该告警恢复门限，将恢复告警。
命令举例 
修改特定动态资源使用率告警参数配置，其中资源名称为“DNSCacheDataArea”，设置一级告警门限值为95%。 
SET SPECDRA:NAME="DNSCacheDataArea",LEVEL1VALUE=95 
相关命令 
[新增特定动态资源使用率告警参数配置]
[删除特定动态资源使用率告警参数配置]
[查询特定动态资源使用率告警参数配置]
父主题： [特定动态资源使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 删除特定动态资源使用率告警参数配置(DEL SPECDRA) 
##### 删除特定动态资源使用率告警参数配置(DEL SPECDRA) 
命令功能 
该命令用于删除特定动态资源使用率告警参数配置，参数包括资源名称，各级告警门限和恢复门限。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|资源名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于标识系统中各种数据区、缓存、标识索引、表等不同类型的动态资源名称。
命令举例 
删除特定动态资源使用率告警参数配置，其中资源名称为“DNSCacheDataArea”。 
DEL SPECDRA:NAME="DNSCacheDataArea" 
相关命令 
[新增特定动态资源使用率告警参数配置]
[修改特定动态资源使用率告警参数配置]
[查询特定动态资源使用率告警参数配置]
父主题： [特定动态资源使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询特定动态资源使用率告警参数配置(SHOW SPECDRA) 
##### 查询特定动态资源使用率告警参数配置(SHOW SPECDRA) 
命令功能 
该命令用于查询特定动态资源使用率告警参数配置。系统支持指定动态资源名称进行查询，也支持不指定资源名称进行通配查询。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|资源名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于标识系统中各种数据区、缓存、标识索引、表等不同类型的动态资源名称。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NAME|资源名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。|该参数用于标识系统中各种数据区、缓存、标识索引、表等不同类型的动态资源名称。
LEVEL1VALUE|一级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置一级告警门限值。当该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率一级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL2VALUE|二级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置二级告警门限值。该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率二级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
LEVEL3VALUE|三级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置三级告警门限值。该种动态资源使用率达到该门限后，将会上报对应的动态资源使用率三级告警。特别的，当配置为0时，表示不上报该级别告警，如果某一级别告警门限值配置为0，则比它级别低的告警门限都需要配置为0，比它低级别的告警也都不上报。
RESTOREVALUE|恢复告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该种资源在上报告警后，一旦该动态资源使用率低于该告警恢复门限，将恢复告警。
命令举例 
查询特定动态资源使用率告警参数配置。 
SHOW SPECDRA 
`
(No.32) : SHOW SPECDRA:
-----------------uMAC_MME_Combo_B5/NFS_MMESGSN_0----------------
操作维护       资源名称         一级告警门限值(%) 二级告警门限值(%) 三级告警门限值(%) 恢复告警门限值(%) 
--------------------------------------------------------------------------------------------------------
复制 修改 删除 DNSCacheDataArea 90                80                70                65                
--------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-06 20:39:05 耗时: 1.931秒。
` 
相关命令 
[新增特定动态资源使用率告警参数配置]
[修改特定动态资源使用率告警参数配置]
[删除特定动态资源使用率告警参数配置]
父主题： [特定动态资源使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 话单存储空间使用率告警参数配置 
## 话单存储空间使用率告警参数配置 
背景知识 
当CG服务器不通时，话单没法正常发送，系统对话单进行了本地缓存。 
本地存储空间有限，当CG服务器长时间不恢复，可能导致本地空间耗尽，新产生的话单没法继续缓存。因此，系统针对本地话单存储空间使用率进行告警上报，提醒运维人员及时处理，以免话单丢失，对运营商造成损失。 
系统可以针对本地话单存储空间使用率告警门限进行配置，告警门限参数包括“一级告警门限值”，“二级告警门限值”，“三级告警门限值”，缺省门限为80%、70%、50%。 
功能描述 
本节点用于配置话单存储空间使用率告警参数，参数包括“一级告警门限值“，二级告警门限值”，“三级告警门限值”。 
相关主题 
 
修改话单存储空间使用率告警参数配置(SET CDRDRA)
 
 
查询话单存储空间使用率告警参数配置(SHOW CDRDRA)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改话单存储空间使用率告警参数配置(SET CDRDRA) 
### 修改话单存储空间使用率告警参数配置(SET CDRDRA) 
命令功能 
该命令用于修改话单存储空间使用率告警参数配置，当需要修改话单存储空间使用率告警参数配置时，使用该命令进行修改配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
LEVEL1VALUE|一级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置一级告警门限值。话单存储空间使用率达到该门限后，将会上报“MP计费话单存储空间不足一级告警”。
LEVEL2VALUE|二级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置二级告警门限值。话单存储空间使用率达到该门限后，将会上报“MP计费话单存储空间不足二级告警”。
LEVEL3VALUE|三级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置三级告警门限值。话单存储空间使用率达到该门限后，将会上报“MP计费话单存储空间不足三级告警”。
命令举例 
修改话单存储空间使用率告警参数配置，设置一级告警门限值为80%，二级告警门限值为70%，三级告警门限值为50%。 
SET CDRDRA:LEVEL1VALUE=80,LEVEL2VALUE=70,LEVEL3VALUE=50 
相关命令 
[查询话单存储空间使用率告警参数配置]
父主题： [话单存储空间使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询话单存储空间使用率告警参数配置(SHOW CDRDRA) 
### 查询话单存储空间使用率告警参数配置(SHOW CDRDRA) 
命令功能 
该命令用于查询话单存储空间使用率告警参数配置，当需要查询话单存储空间使用率告警参数配置时，使用该命令进行查询。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LEVEL1VALUE|一级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置一级告警门限值。话单存储空间使用率达到该门限后，将会上报“MP计费话单存储空间不足一级告警”。
LEVEL2VALUE|二级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置二级告警门限值。话单存储空间使用率达到该门限后，将会上报“MP计费话单存储空间不足二级告警”。
LEVEL3VALUE|三级告警门限值(%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置三级告警门限值。话单存储空间使用率达到该门限后，将会上报“MP计费话单存储空间不足三级告警”。
命令举例 
查询话单存储空间使用率告警参数配置。 
SHOW CDRDRA 
`
(No.27) : SHOW CDRDRA
-----------------uMAC_MME_Combo_B5/NFS_MMESGSN_0----------------
操作维护       一级告警门限值(%) 二级告警门限值(%) 三级告警门限值(%) 
---------------------------------------------------------------------
修改           80                70                50                
---------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-06 20:34:17 耗时: 1.324秒。
` 
相关命令 
[修改话单存储空间使用率告警参数配置]
父主题： [话单存储空间使用率告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 性能管理专用配置 
## 性能管理专用配置 
背景知识 
性能统计分为无对象和有对象两个模式，对于分对象这种模式的性能统计，有些需要根据对象的格式来进行规整，便于系统使用正确的对象来匹配上报的性能数据。 
功能描述 
性能管理专用配置主要用于设置与性能统计相关的需要特殊配置的信息，包括GGSN的IP地址，IMSI号段、MME和SGW链路和ACL规则标识。配置后，可以根据GGSN IP地址或IMSI号段或链路号或ACL规则标识建立性能统计任务。 
相关主题 
 
GGSN IP配置
 
 
用户流程测量号段配置
 
 
用户号段统计配置
 
 
MME与SGW链路配置
 
 
EPC APN统计配置
 
 
eNodeB局向配置
 
 
组合条件配置
 
 
MME TA组配置
 
 
测量类型对象数配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### GGSN IP配置 
### GGSN IP配置 
背景知识 
网元的性能统计测量项，可以设置对象（比如，路由区、APN、号码段、GGSN IP等），通过区分对象的统计查看该对象下的统计数据，以达到更细致的数据分析目的。 
功能描述 
本命令功能用于设置待性能统计的GGSN IP信息，包括GGSN IP编号和用户别名。GGSN IP的用户别名在性能管理中可以与测量类型信息相关联，从而获取以GGSN IP为对象的性能统计数据。 
                在配置前，向运营商获取期望统计的GGSN IP地址列表，并通过
                [ADD GGSNIP]
                命令，将所有GGSN IP地址逐个配置。
            
                在操作员进行性能统计时，会使用到
                [ADD GGSNIP]
                命令配置的IMSI号段，操作如下：
            
在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。 
本命令功能用于设置待性能统计的GGSN IP地址信息，包括GGSN IP编号和用户别名。GGSN IP地址的用户别名在性能管理中可以与测量类型信息相关联，从而获取以GGSN IP地址为对象的性能统计数据。 
配置完成后，需要执行如下操作，系统才会以GGSN IP地址为对象进行性能统计： 
在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。 
在界面左侧的“测量类型树”中，右击“性能管理--SGSN测量--GGSN IP测量”目录下的“SGSN分GGSN IP的会话测量”，在弹出的快捷菜单中选择“新建测量任务”。 
在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。 
                        “测量类型信息”页签左侧列出的“对象名称”就是通过
                        [ADD GGSNIP]
                        命令设置的用户别名。勾选需要进行性能统计的GGSN IP地址，默认是全部勾选
                    
设置完成后，点击确定完成。 
该功能的具体实现流程如下： 
                        SGSN根据GGSN IP地址，匹配
                        [ADD GGSNIP]
                        命令的配置结果，以确定对应的GGSN IP地址。
                    
SGSN根据GGSN IP地址确定操作员是否建立了对应的性能统计任务，如果有，则将统计数据上报给OMM服务器。 
OMM服务器将分GGSN IP地址的、统计的性能统计数据上报给EMS。 
相关主题 
 
新增GGSN IP(ADD GGSNIP)
 
 
修改GGSN IP(SET GGSNIP)
 
 
删除GGSN IP(DEL GGSNIP)
 
 
查询GGSN IP(SHOW GGSNIP)
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增GGSN IP(ADD GGSNIP) 
#### 新增GGSN IP(ADD GGSNIP) 
命令功能 
此命令用于新增GGSN IP地址信息，包括编号和别名。 
当性能统计需要以GGSN IP地址为对象时，使用该命令设置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|GGSN IP编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2147483647。|该参数用于标识一条已配置GGSN IP地址的记录，该编号不能与已存在的编号相同。
IP|GGSN IP|参数可选性:必选参数；参数类型:地址|该参数用于配置GGSN IP地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~250个字符。|该参数为GGSN IP地址配置的别名，用于区分不同的GGSN IP地址配置。
命令举例 
新增一个GGSN IP，编号为1、GGSN IP为1.1.1.1、用户别名为A地址。 
ADD GGSNIP:ID=1,IP="1.1.1.1",NAME="A地址"; 
父主题： [GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改GGSN IP(SET GGSNIP) 
#### 修改GGSN IP(SET GGSNIP) 
命令功能 
此命令用于修改GGSN IP地址信息，包括别名。 
当性能统计使用的GGSN IP地址对象发生变化时，使用该命令修改。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN IP|参数可选性:必选参数；参数类型:地址|该参数用于配置GGSN IP地址。
NAME|用户别名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~250个字符。|该参数为GGSN IP地址配置的别名，用于区分不同的GGSN IP地址配置。
命令举例 
将GGSN IP 地址为1.1.1.1的用户别名修改为B地址。 
SET GGSNIP:IP="1.1.1.1",NAME="B地址"; 
父主题： [GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除GGSN IP(DEL GGSNIP) 
#### 删除GGSN IP(DEL GGSNIP) 
命令功能 
此命令用于删除GGSN IP地址信息。 
当性能统计中某个GGSN IP地址对象不再需要时，使用该命令删除。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN IP|参数可选性:必选参数；参数类型:地址|该参数用于配置GGSN IP地址。
命令举例 
删除一个GGSN性能统计IP，地址为1.1.1.1。 
DEL GGSNIP:IP="1.1.1.1"; 
父主题： [GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询GGSN IP(SHOW GGSNIP) 
#### 查询GGSN IP(SHOW GGSNIP) 
命令功能 
此命令用于查询已配置的GGSN IP地址信息。
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN IP|参数可选性:任选参数；参数类型:地址|该参数用于配置GGSN IP地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|GGSN IP编号|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条已配置GGSN IP地址的记录，该编号不能与已存在的编号相同。
IP|GGSN IP|参数可选性:任选参数；参数类型:地址|该参数用于配置GGSN IP地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数为GGSN IP地址配置的别名，用于区分不同的GGSN IP地址配置。
命令举例 
查询所有GGSN IP配置。 
SHOW GGSNIP; 
`
命令 (No.3): SHOW GGSNIP
操作维护         GGSN IP编号            GGSN IP       用户别名
--------------------------------------------------------------
复制 修改 删除   1                      10.43.12.12   
--------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.022 秒）。
` 
父主题： [GGSN IP配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 用户流程测量号段配置 
### 用户流程测量号段配置 
背景知识 
网元的性能统计测量项，可以设置对象（比如，路由区、APN、号码段、GGSN IP等），通过区分对象的统计查看该对象下的统计数据，以达到更细致的数据分析目的。 
功能描述 
本命令功能用于设置待性能统计的IMSI号段信息，包括IMSI编号和用户别名。IMSI号段的用户别名在性能管理中可以与测量类型信息相关联，从而获取以IMSI号段为对象的性能统计数据。 
                在配置前，需要向运营商获取期望统计的IMSI号段列表，并通过
                [ADD IMSINUM]
                命令，将所有IMSI号段逐个配置。
            
配置完成后，需要执行如下操作，系统才会以IMSI号段为对象进行性能统计： 
在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。 
在界面左侧的“测量类型树”中，右击“性能管理--SGSN测量--IMSI测量”目录下的“IMSI号段的单用户流程测量”，在弹出的快捷菜单中选择“新建测量任务”。 
在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。 
                        “测量类型信息”页签左侧列出的“对象名称”就是通过
                        [ADD IMSINUM]
                        命令设置的用户别名。勾选需要进行性能统计的IMSI号段，默认是全部勾选。
                    
设置完成后，点击确定完成。 
该功能的具体实现流程如下： 
                        SGSN根据用户IMSI，匹配
                        [ADD IMSINUM]
                        命令的配置结果，以确定对应的IMSI号段。
                    
SGSN根据IMSI号段确定操作员是否建立了对应的性能统计任务，如果有，则将统计数据上报给OMM服务器。 
OMM服务器将分IMSI号段的、统计的性能统计数据上报给EMS。 
相关主题 
 
新增IMSI号段(ADD IMSINUM)
 
 
修改IMSI号段(SET IMSINUM)
 
 
删除IMSI号段(DEL IMSINUM)
 
 
查询IMSI号段(SHOW IMSINUM)
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增IMSI号段(ADD IMSINUM) 
#### 新增IMSI号段(ADD IMSINUM) 
命令功能 
此命令用于新增IMSI号段信息，包括编号和别名。 
当性能统计需要以IMSI号段为对象时，使用该命令设置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|IMSI NUM编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数用于标识一条已配置IMSI号段的记录，该编号不能与已存在的编号相同。
NUM|IMSI NUM|参数可选性:必选参数；参数类型:整数；参数范围为:1~999999999999999。|该参数用于配置IMSI号段，该IMSI号段必须与性能统计期望的IMSI号段一致。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~250个字符。|该参数为IMSI号段配置的别名，用于区分不同的IMSI号段配置。
命令举例 
新增一个IMSI号段，IMSI编号为1，IMSI号段为460020012700100，用户别名为IMSI Number1。 
ADD IMSINUM:ID=1,NUM="460020012700100",NAME="IMSI Number1"; 
父主题： [用户流程测量号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改IMSI号段(SET IMSINUM) 
#### 修改IMSI号段(SET IMSINUM) 
命令功能 
此命令用于修改IMSI号段信息，包括别名。 
当性能统计使用的IMSI号段对象发生变化时，使用该命令修改。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
NUM|IMSI NUM|参数可选性:必选参数；参数类型:整数；参数范围为:1~999999999999999。|该参数用于配置IMSI号段，该IMSI号段必须与性能统计期望的IMSI号段一致。
NAME|用户别名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~250个字符。|该参数为IMSI号段配置的别名，用于区分不同的IMSI号段配置。
命令举例 
将IMSI号段为460020012700100的用户别名改为IMSINUM1。 
SET IMSINUM:NUM="460020012700100",NAME="IMSINUM1"; 
父主题： [用户流程测量号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除IMSI号段(DEL IMSINUM) 
#### 删除IMSI号段(DEL IMSINUM) 
命令功能 
此命令用于删除IMSI号段信息。 
当性能统计中某个IMSI号段对象不再需要时，使用该命令删除。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
NUM|IMSI NUM|参数可选性:必选参数；参数类型:整数；参数范围为:1~999999999999999。|该参数用于配置IMSI号段，该IMSI号段必须与性能统计期望的IMSI号段一致。
命令举例 
删除IMSI NUM为460020012700100的IMSI号段。 
DEL IMSINUM:NUM="460020012700100"; 
父主题： [用户流程测量号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询IMSI号段(SHOW IMSINUM) 
#### 查询IMSI号段(SHOW IMSINUM) 
命令功能 
此命令用于查询已配置的IMSI号段信息。
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
NUM|IMSI NUM|参数可选性:任选参数；参数类型:整数；参数范围为:1~999999999999999。|该参数用于配置IMSI号段，该IMSI号段必须与性能统计期望的IMSI号段一致。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|IMSI NUM编号|参数可选性:任选参数；参数类型:整数。|该参数用于标识一条已配置IMSI号段的记录，该编号不能与已存在的编号相同。
NUM|IMSI NUM|参数可选性:任选参数；参数类型:整数。|该参数用于配置IMSI号段，该IMSI号段必须与性能统计期望的IMSI号段一致。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数为IMSI号段配置的别名，用于区分不同的IMSI号段配置。
命令举例 
查询IMSI NUM为460020012700100的IMSI号段配置。 
SHOW IMSINUM:NUM="460020012700100"; 
`
命令 (No.5): SHOW IMSINUM:NUM="460020012700100";
操作维护         IMSI NUM编号           IMSI NUM               用户别名
-----------------------------------------------------------------------
复制 修改 删除   1                      460020012700100        IMSI Number1
-----------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [用户流程测量号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 用户号段统计配置 
### 用户号段统计配置 
背景知识 
运营商在运维的过程中，需要监控某些号段用户数。为了便于统计相关的数据，需要配置相关的IMSI或者MSISDN号码段。 
功能描述 
本命令功能用于设置待性能统计的号码段信息，包括IMSI和MSISDN。号码段的用户别名在性能管理中可以与测量类型信息相关联，从而获取以号码段为对象的性能统计数据。 
                在配置前，向运营商获取期望统计的号码段列表，并通过
                [ADD IMSI]
                或者
                [ADD MSISDN]
                命令，将所有号码段址逐个配置。
            
配置完成后，需要执行如下操作，系统才会以号码段为对象进行性能统计： 
在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。 
在界面左侧的“测量类型树”中，右击“性能管理--MME测量--号段测量”目录下的“IMSI段测量”或者"MSISDN段测量"，在弹出的快捷菜单中选择“新建测量任务”。 
在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。 
                        “测量类型信息”页签左侧列出的“对象名称”就是通过
                        [ADD IMSI]
                        或者
                        [ADD MSISDN]
                        命令设置的用户别名。勾选需要进行性能统计的号码段，默认是全部勾选。
                    
设置完成后，点击确定完成。 
该功能的具体实现流程如下： 
                        MME根据IMSI/MSISDN号码段，匹配
                        [ADD IMSI]
                        或者
                        [ADD MSISDN]
                        命令的配置结果，以确定对应的IMSI/MSISDN号段。
                    
MME根据IMSI/MSISDN号码段确定操作员是否建立了对应的性能统计任务，如果有，则将统计数据上报给OMM服务器。 
OMM服务器将分IMSI/MSISDN的统计的性能统计数据上报给EMS。 
相关主题 
 
新增IMSI号段(ADD IMSI)
 
 
修改IMSI号段(SET IMSI)
 
 
删除IMSI号段(DEL IMSI)
 
 
查询IMSI号段(SHOW IMSI)
 
 
新增MSISDN号段(ADD MSISDN)
 
 
修改MSISDN号段(SET MSISDN)
 
 
删除MSISDN号段(DEL MSISDN)
 
 
查询MSISDN号段(SHOW MSISDN)
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增IMSI号段(ADD IMSI) 
#### 新增IMSI号段(ADD IMSI) 
命令功能 
此命令用于配置需要进行统计的IMSI号段。当运营商需要统计相关IMSI号码段用户数的时候，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|IMSI编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|配置IMSI的号码编号。
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|配置待统计的IMSI号段。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。
命令举例 
新增待统计的IMSI号段信息，其中IMSI编号为12、IMSI号段为460020012700100、用户别名为IMSI Number1。 
ADD IMSI:ID=12,IMSI="460020012700100",NAME="IMSI Number1"; 
父主题： [用户号段统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改IMSI号段(SET IMSI) 
#### 修改IMSI号段(SET IMSI) 
命令功能 
此命令用于修改统计的IMSI号段。当运营商需要修改已经存在统计IMSI号码段用户数的时候，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|配置待统计的IMSI号段。
NAME|用户别名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|对此配置进行维护记录，起备注作用。
命令举例 
修改IMSI号段为460020012700100的配置数据，将该配置的用户别名为IMSI Number2。 
SET IMSI:IMSI="460020012700100",NAME="IMSI Number2"; 
父主题： [用户号段统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除IMSI号段(DEL IMSI) 
#### 删除IMSI号段(DEL IMSI) 
命令功能 
此命令用于删除已经配置的IMSI号段信息。当运营商需要取消已经配置了哪些IMSI号码段用户数的时候，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|配置待统计的IMSI号段。
命令举例 
删除IMSI号段为460020012700100的配置数据。 
DEL IMSI:IMSI="460020012700100"; 
父主题： [用户号段统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询IMSI号段(SHOW IMSI) 
#### 查询IMSI号段(SHOW IMSI) 
命令功能 
此命令用于查询已经配置的IMSI号段信息。当运营商需要查询配置了哪些IMSI号码段用户数的时候，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|配置待统计的IMSI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|IMSI编号|参数可选性:任选参数；参数类型:整数。|配置IMSI的号码编号。
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|配置待统计的IMSI号段。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|对此配置进行维护记录，起备注作用。
命令举例 
查询所有的IMSI号段。 
SHOW IMSI; 
`
命令 (No.7): SHOW IMSI
操作维护         IMSI编号   IMSI号段          用户别名
------------------------------------------------------
复制 修改 删除   12         460020012700100   IMSI Number1
------------------------------------------------------
记录数 1
命令执行成功（耗时 0.151 秒）。
命令执行成功（耗时 0.06 秒）。
` 
父主题： [用户号段统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增MSISDN号段(ADD MSISDN) 
#### 新增MSISDN号段(ADD MSISDN) 
命令功能 
此命令用于配置需要进行统计的MSISDN号段。当运营商需要统计相关MSISDN号码段用户数的时候，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|MSISDN编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|配置MSISDN的号码编号。
MSISDN|MSISDN号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|配置待统计的MSISDN号段。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|对此配置进行维护记录，起备注作用。
命令举例 
新增待统计的MSISDN号段信息，其中MSISDN编号为10、MSISDN号段为8613675138501、用户别名为MSISDN Number1。 
ADD MSISDN:ID=10,MSISDN="8613675138501",NAME="MSISDN Number1"; 
父主题： [用户号段统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改MSISDN号段(SET MSISDN) 
#### 修改MSISDN号段(SET MSISDN) 
命令功能 
此命令用于修改统计的MSISDN号段。当运营商需要修改已经存在统计MSISDN号码段用户数的时候，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
MSISDN|MSISDN号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|配置待统计的MSISDN号段。
NAME|用户别名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|对此配置进行维护记录，起备注作用。
命令举例 
修改MSISDN号段为8613675138501的配置数据，将该配置的用户别名为MSISDN Number2。 
SET MSISDN:MSISDN="8613675138501",NAME="MSISDN Number2"; 
父主题： [用户号段统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除MSISDN号段(DEL MSISDN) 
#### 删除MSISDN号段(DEL MSISDN) 
命令功能 
此命令用于删除已经配置了的MSISDN号段信息。当运营商需要取消已经配置了哪些MSISDN号码段用户数的时候，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
MSISDN|MSISDN号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|配置待统计的MSISDN号段。
命令举例 
删除MSISDN号段为8613675138501的配置数据。 
DEL MSISDN:MSISDN="8613675138501"; 
父主题： [用户号段统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MSISDN号段(SHOW MSISDN) 
#### 查询MSISDN号段(SHOW MSISDN) 
命令功能 
此命令用于查询已经配置的MSISDN号段信息。当运营商需要查询配置了哪些MSISDN号码段用户数的时候，使用该命令。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
MSISDN|MSISDN号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|配置待统计的MSISDN号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|MSISDN编号|参数可选性:任选参数；参数类型:整数。|配置MSISDN的号码编号。
MSISDN|MSISDN号段|参数可选性:任选参数；参数类型:字符型。|配置待统计的MSISDN号段。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|对此配置进行维护记录，起备注作用。
命令举例 
查询所有的MSISDN号段。 
SHOW MSISDN; 
`
命令 (No.9): SHOW MSISDN
操作维护         MSISDN编号   MSISDN号段      用户别名
------------------------------------------------------
复制 修改 删除   10           8613675138501   MSISDN Number1
------------------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [用户号段统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME与SGW链路配置 
### MME与SGW链路配置 
背景知识 
上级网管要求EMS上报有关S11接口的相关统计信息（基于CORBA接口），由于S11接口的相关统计信息是基于MME网元的控制面地址和SGW网元的控制面地址两个对象标识进行统计的，而建立性能统计任务只能基于一个对象标识。 
为了便于建立性能统计任务和过滤统计数据，通过本功能增加一个链路号，此链路号对应一个MME控制面地址和一个SGW控制面地址，用于唯一标识一对MME网元和SGW网元。 
功能描述 
                操作维护人员先根据将被统计的MME控制面地址（通过
                [ADD MMESGWLINK]
                命令设置的“源地址”）和SGW控制面地址（通过
                [ADD MMESGWLINK]
                命令设置的“目的地址”）配置链路号（通过
                [ADD MMESGWLINK]
                命令设置的“链路编号”），一个链路号中的源地址只能有一个，目的地址也只能有一个。
            
                在操作员进行性能统计时，会使用到
                [ADD MMESGWLINK]
                命令配置的“链路编号”，操作如下：
            
在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。 
在界面左侧的“测量类型树”中，右击“性能管理--MME测量--MME链路测量--MME用户链路测量”，在弹出的快捷菜单中选择“新建测量任务”。 
在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。 
                        在“测量类型信息”页签左侧的“对象名称”就是通过
                        [ADD MMESGWLINK]
                        命令设置的“链路编号”。
                    
此功能的实现流程如下： 
                        MME根据S11接口的交互消息获取MME控制面地址和SGW控制面地址，根据两个网元的地址，匹配
                        [ADD MMESGWLINK]
                        命令的配置结果，以确定对应的“链路编号”。
                    
MME根据“链路编号”（即“MME用户链路测量”中的“对象名称”）确定操作员是否建立了对应的性能统计任务，如果有，则将统计数据上报给OMM服务器。 
OMM服务器将S11接口的性能统计数据上报给EMS。 
EMS再通过CORBA接口将S11接口的性能统计数据上报给上级网管。 
相关主题 
 
新增MME与SGW链路(ADD MMESGWLINK)
 
 
修改MME与SGW链路(SET MMESGWLINK)
 
 
删除MME与SGW链路(DEL MMESGWLINK)
 
 
查询MME与SGW链路(SHOW MMESGWLINK)
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增MME与SGW链路(ADD MMESGWLINK) 
#### 新增MME与SGW链路(ADD MMESGWLINK) 
命令功能 
该命令用于增加一个链路编号。 
此链路编号对应一个MME控制面地址和一个SGW控制面地址，用于唯一标识一对MME网元和SGW网元。 
注意事项 
该命令只适用于MME网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|此参数对应一个MME控制面地址和一个SGW控制面地址，用于唯一标识一对MME网元和SGW网元。在操作员进行性能统计时，会使用到ADD MMESGWLINK命令配置的“链路编号”，操作如下：在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。在界面左侧的“测量类型树”中，右击“性能管理--MME测量--MME链路测量--MME用户链路测量”，在弹出的快捷菜单中选择“新建测量任务”。在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。在“测量类型信息”页签左侧的“对象名称”就是通过ADD MMESGWLINK命令设置的“链路编号”。
SRCADDR|MME地址|参数可选性:必选参数；参数类型:地址|该参数表示MME的控制面地址。该参数的取值是通过命令SET MME GTPC配置的“GTPC IPv4信令地址”，可通过SHOW SIGIP GTPC命令，从查询结果中获取。
DESTADDR|SGW地址|参数可选性:必选参数；参数类型:地址|该参数表示SGW的控制面地址。此参数需要根据运营商的规划数据获取。
TYPE|类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|此参数表示SGW链路的类型，区分S11口的控制面和用户面链路。S11-C：表示此链路是MME和SGW的控制面链路。S11-U：表示此链路是MME和SGW的用户面链路。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于补充此条配置命令的描述信息，以便于维护人员进行理解。
命令举例 
新增一条MME与SGW的链路，链路编号为1，源地址（MME控制面地址）为1.1.1.1，目的地址（SGW控制面地址）为2.2.2.2，类型为S11-C。 
ADD MMESGWLINK:LINKID=1,SRCADDR="1.1.1.1",DESTADDR="2.2.2.2",TYPE="S11-C"; 
父主题： [MME与SGW链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改MME与SGW链路(SET MMESGWLINK) 
#### 修改MME与SGW链路(SET MMESGWLINK) 
命令功能 
该命令用于修改链路对应的源地址（MME控制面地址）和目的地址（SGW控制面地址）。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|此参数对应一个MME控制面地址和一个SGW控制面地址，用于唯一标识一对MME网元和SGW网元。在操作员进行性能统计时，会使用到ADD MMESGWLINK命令配置的“链路编号”，操作如下：在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。在界面左侧的“测量类型树”中，右击“性能管理--MME测量--MME链路测量--MME用户链路测量”，在弹出的快捷菜单中选择“新建测量任务”。在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。在“测量类型信息”页签左侧的“对象名称”就是通过ADD MMESGWLINK命令设置的“链路编号”。
SRCADDR|MME地址|参数可选性:任选参数；参数类型:地址|该参数表示MME的控制面地址。该参数的取值是通过命令SET MME GTPC配置的“GTPC IPv4信令地址”，可通过SHOW SIGIP GTPC命令，从查询结果中获取。
DESTADDR|SGW地址|参数可选性:任选参数；参数类型:地址|该参数表示SGW的控制面地址。此参数需要根据运营商的规划数据获取。
TYPE|类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数表示SGW链路的类型，区分S11口的控制面和用户面链路。S11-C：表示此链路是MME和SGW的控制面链路。S11-U：表示此链路是MME和SGW的用户面链路。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于补充此条配置命令的描述信息，以便于维护人员进行理解。
命令举例 
修改一条链路编号为1的链路，将源地址修改为1.1.1.10。 
SET MMESGWLINK:LINKID=1,SRCADDR="1.1.1.10"; 
父主题： [MME与SGW链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除MME与SGW链路(DEL MMESGWLINK) 
#### 删除MME与SGW链路(DEL MMESGWLINK) 
命令功能 
该命令用于删除MME与SGW链路。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|此参数对应一个MME控制面地址和一个SGW控制面地址，用于唯一标识一对MME网元和SGW网元。在操作员进行性能统计时，会使用到ADD MMESGWLINK命令配置的“链路编号”，操作如下：在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。在界面左侧的“测量类型树”中，右击“性能管理--MME测量--MME链路测量--MME用户链路测量”，在弹出的快捷菜单中选择”新建测量任务“。在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。在“测量类型信息”页签左侧的“对象名称”就是通过ADD MMESGWLINK命令设置的”链路编号”。
命令举例 
删除一条链路编号为1的链路。 
DEL MMESGWLINK:LINKID=1; 
父主题： [MME与SGW链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MME与SGW链路(SHOW MMESGWLINK) 
#### 查询MME与SGW链路(SHOW MMESGWLINK) 
命令功能 
该命令用于查询MME与SGW链路。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|此参数对应一个MME控制面地址和一个SGW控制面地址，用于唯一标识一对MME网元和SGW网元。在操作员进行性能统计时，会使用到ADD MMESGWLINK命令配置的“链路编号”，操作如下：在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。在界面左侧的“测量类型树”中，右击“性能管理--MME测量--MME链路测量--MME用户链路测量”，在弹出的快捷菜单中选择”新建测量任务“。在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。在“测量类型信息”页签左侧的“对象名称”就是通过ADD MMESGWLINK命令设置的”链路编号”。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路编号|参数可选性:任选参数；参数类型:整数。|此参数对应一个MME控制面地址和一个SGW控制面地址，用于唯一标识一对MME网元和SGW网元。在操作员进行性能统计时，会使用到ADD MMESGWLINK命令配置的“链路编号”，操作如下：在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。在界面左侧的“测量类型树”中，右击“性能管理--MME测量--MME链路测量--MME用户链路测量”，在弹出的快捷菜单中选择”新建测量任务“。在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。在“测量类型信息”页签左侧的“对象名称”就是通过ADD MMESGWLINK命令设置的”链路编号”。
SRCADDR|MME地址|参数可选性:任选参数；参数类型:地址|该参数表示MME的控制面地址。该参数的取值是通过命令SET MME GTPC配置的“GTPC IPv4信令地址”，可通过SHOW SIGIP GTPC命令，从查询结果中获取。
DESTADDR|SGW地址|参数可选性:任选参数；参数类型:地址|该参数表示SGW的控制面地址。此参数需要根据运营商的规划数据获取。
TYPE|类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此参数表示SGW链路的类型，区分S11口的控制面和用户面链路。S11-C：表示此链路是MME和SGW的控制面链路。S11-U：表示此链路是MME和SGW的用户面链路。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数表示此条配置数据对应的记录标识，用于补充此条配置命令的描述信息，以便于维护人员进行理解。
命令举例 
查询链路编号为1的记录。 
SHOW MMESGWLINK:LINKID=1; 
`
命令 (No.12): SHOW MMESGWLINK:LINKID=1;
操作维护         链路编号   源地址    目的地址   类型    用户别名
-----------------------------------------------------------------
复制 修改 删除   1          1.1.1.1   2.2.2.2    S11-C   
-----------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.059 秒）。
` 
父主题： [MME与SGW链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### EPC APN统计配置 
### EPC APN统计配置 
背景知识 
当网络或设备出现故障时，运营商有可能会需要获取某个或某几个特定的APN的统计信息，用于进行故障定位、话务分析等。基于特定APN的统计前，必须先完成该APN的配置。目前，基于APN测量的统计项包括：承载激活流程统计、承载修改流程统计以及承载去激活流程统计。 
功能描述 
                “EPC APN统计配置”用于配置APN以及APN方式，该配置的APN作为性能测量对象。增加APN配置后，在性能管理的
                
MME测量
                     > APN测量
                     > 流量测量
                节点下，可进行基于APN的承载激活流程测量、基于APN的承载修改流程测量以及基于APN的承载去激活流程测量。
            
APN的方式包括FQDN和NI两种： 
 
配置为FQDN方式时，APN的填写格式为：APN NI.apn.epc.APN OI。
 
 
配置为NI方式时，APN的填写格式为：APN NI。
 
 
相关主题 
 
APN方式配置
 
 
APN配置
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### APN方式配置 
#### APN方式配置 
背景知识 
当网络或设备出现故障时，运营商有可能会需要获取某个或某几个特定APN的性能统计信息，用于进行故障定位、话务分析等操作。 
系统支持基于两种形式的APN格式进行统计，包括根据FQDN或NI进行性能数据统计。 
                操作员需要先通过
                [SET APN MODE]
                命令设置系统支持的APN统计格式，然后再通过
                [ADD APN STATIS]
                命令根据不同的格式设置APN的名称。
            
设置了相关数据之后，如果运营商想要查看某个APN的性能统计数据，系统可以针对某个APN提供相应的性能统计项目，供运营商进行查询。 
基于APN测量的性能统计项包括：“基于APN的承载激活流程测量”、“基于APN的承载修改流程测量”以及“基于APN的承载去激活流程测量”。 
                在操作员进行性能统计时，会使用到
                [ADD APN STATIS]
                命令配置的“APN名称”。
            
操作如下： 
在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。 
在界面左侧的“测量类型树”中，右击“性能管理--MME测量--APN测量--流程测量“，任意选择“基于APN的承载激活流程测量”、“基于APN的承载修改流程测量”以及“基于APN的承载去激活流程测量”三者之一，在弹出的快捷菜单中选择”新建测量任务“。 
在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。 
                        在“测量类型信息”页签左侧的“对象名称”就是通过
                        [ADD APN STATIS]
                        命令设置的”APN名称”。
                    
功能描述 
该命令用于配置基于APN进行性能统计时的测量方式，可以配置为根据NI或FQDN进行统计。 
相关主题 
 
设置APN方式配置(SET APN MODE)
 
 
查询APN方式配置(SHOW APN MODE)
 
 
父主题： [EPC APN统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 设置APN方式配置(SET APN MODE) 
##### 设置APN方式配置(SET APN MODE) 
命令功能 
该命令用于配置基于APN进行性能统计时的测量方式。 
在通过[ADD APN STATIS]命令配置需要进行性能统计的特定APN名称之前，必须先通过此命令配置系统支持的APN统计格式。目前支持两种格式：FQDN或NI。
FQDN（Fully Qualified Domain Name，全称域名）由NI和OI，加上插在二者之间的“apn.epc”组成，格式为“NI.apn.epc.OI”。 
协议规定FQDN最长不能超过100个字符。 
NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务。 
NI是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。 
APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下： 
 
不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头
> 
 
不能以“.gprs”结尾
 
 
不能使用通配符“*”
 
 
除了数字、字母、“-”、和“.”不能输入其余字符。
 
 
示例：zte.com.cn 
OI（Operator Identifier，运营商标识），每个运营商都有一个缺省的APN运营商标识。 
APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”（此处要求选用后面一种格式，即R8版本之后的形式），要求如下： 
MNC和MCC都是三位0~9的数字，如果不足三位，需要靠前用0补齐。 
除了数字、字母、“-”、和“.”不能输入其余字符。 
示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs 
注意事项 
该功能仅适用于MME网元。 
本命令的配置结果，会影响[ADD APN STATIS]E命令的配置数据。
 
如果本命令配置的格式为基于NI进行统计，则ADD APN STATISE命令中的APN名称需要为NI格式。
 
 
如果本命令配置的格式为基于FQDN进行统计，则ADD APN STATISE命令中的APN名称需要为FQDN格式。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
MODE|APN方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|操作员在基于APN进行性能统计时，支持两种方式：可以基于NI进行统计，也可以基于FQDN进行统计。
命令举例 
操作员在基于APN进行性能统计时，设置为基于APN-NI方式进行统计。 
SET APN MODE:MODE=NI; 
父主题： [APN方式配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询APN方式配置(SHOW APN MODE) 
##### 查询APN方式配置(SHOW APN MODE) 
命令功能 
该命令用于查询基于APN进行性能统计时的测量方式。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MODE|APN方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|操作员在基于APN进行性能统计时，支持两种方式：可以基于NI进行统计，也可以基于FQDN进行统计。
命令举例 
查询APN方式配置。 
SHOW APN MODE 
`
命令 (No.7): SHOW APN MODE;
操作维护 APN方式 
-------------------
修改      NI 
-------------------
记录数 1
命令执行成功（耗时 0.078 秒）。
` 
父主题： [APN方式配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### APN配置 
#### APN配置 
背景知识 
当网络或设备出现故障时，运营商有可能会需要获取某个或某几个特定APN的性能统计信息，用于进行故障定位、话务分析等操作。 
系统支持基于两种形式的APN格式进行统计，包括根据FQDN或NI进行性能数据统计。 
                操作员需要先通过
                [SET APN MODE]
                命令设置系统支持的APN统计格式，然后再通过
                [ADD APN STATIS]
                命令根据不同的格式设置APN的名称。
            
设置了相关数据之后，如果运营商想要查看某个APN的性能统计数据，系统可以针对某个APN提供相应的性能统计项目，供运营商进行查询。 
基于APN测量的性能统计项包括：“基于APN的承载激活流程测量”、“基于APN的承载修改流程测量”以及“基于APN的承载去激活流程测量”。 
                在操作员进行性能统计时，会使用到
                [ADD APN STATIS]
                命令配置的“APN名称”。
            
操作如下： 
在“本地维护终端”界面上，选择“系统菜单--应用管理--性能管理”，打开“性能管理”窗口。 
在界面左侧的“测量类型树”中，右击“性能管理--MME测量--APN测量--流程测量“，任意选择“基于APN的承载激活流程测量”、“基于APN的承载修改流程测量”以及“基于APN的承载去激活流程测量”三者之一，在弹出的快捷菜单中选择”新建测量任务“。 
在弹出的“新建测量任务”对话框中，选择“测量类型信息”页签。 
                        在“测量类型信息”页签左侧的“对象名称”就是通过
                        [ADD APN STATIS]
                        命令设置的”APN名称”。
                    
功能描述 
该命令用于配置基于APN进行性能统计的测量对象，即APN名称。 
相关主题 
 
新增APN配置(ADD APN STATIS)
 
 
删除APN配置(DEL APN STATIS)
 
 
查询APN配置(SHOW APN STATIS)
 
 
父主题： [EPC APN统计配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 新增APN配置(ADD APN STATIS) 
##### 新增APN配置(ADD APN STATIS) 
命令功能 
该命令用于配置基于APN进行性能统计的测量对象，即APN名称。 
注意事项 
该功能仅适用于MME网元。 
在通过本命令配置需要进行性能统计的特定APN名称之前，必须先通过[SET APN MODE]命令配置系统支持的APN统计格式。
 
如果SET APN MODE命令配置的格式为基于NI进行统计，则此参数的格式需要为NI。
 
 
如果SET APN MODE命令配置的格式为基于FQDN进行统计，则此参数的格式需要为FQDN。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|系统支持基于两种形式的APN格式进行性能统计，包括根据FQDN或NI进行性能数据统计。具体使用哪种方式进行统计，取决于SET APN MODE命令的配置结果。操作员需要先通过SET APN MODE命令设置系统支持的APN统计格式，然后再通过本命令根据不同的格式设置APN的名称。FQDN由NI和OI，加上插在二者之间的“apn.epc”组成，格式为“NI.apn.epc.OI”。协议规定FQDN最长不能超过100个字符。NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），每个运营商都有一个缺省的APN运营商标识。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”（此处要求选用后面一种格式），要求如下：MNC和MCC都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs
命令举例 
新增基于NI格式进行性能测量的APN名称，其中APN名称为'APN-NI.apn.epcmnc460.mcc01.3gppnetwork.org'。 
ADD APN STATIS:APNNAME="APN-NI.apn.epcmnc460.mcc01.3gppnetwork.org"; 
父主题： [APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 删除APN配置(DEL APN STATIS) 
##### 删除APN配置(DEL APN STATIS) 
命令功能 
该命令用于删除已经配置的基于APN进行性能统计的测量对象。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|系统支持基于两种形式的APN格式进行性能统计，包括根据FQDN或NI进行性能数据统计。具体使用哪种方式进行统计，取决于SET APN MODE命令的配置结果。操作员需要先通过SET APN MODE命令设置系统支持的APN统计格式，然后再通过本命令根据不同的格式设置APN的名称。FQDN由NI和OI，加上插在二者之间的“apn.epc”组成，格式为“NI.apn.epc.OI”。协议规定FQDN最长不能超过100个字符。NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），每个运营商都有一个缺省的APN运营商标识。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”（此处要求选用后面一种格式），要求如下：MNC和MCC都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs
命令举例 
已经配置的基于APN进行性能统计的测量对象，其中APN名称为'apn-ni.apn.epcmnc460.mcc01.3gppnetwork.org'的配置数据。 
DEL APN STATIS:APNNAME="apn-ni.apn.epcmnc460.mcc01.3gppnetwork.org"; 
父主题： [APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询APN配置(SHOW APN STATIS) 
##### 查询APN配置(SHOW APN STATIS) 
命令功能 
该命令用于查询已经配置的基于APN进行性能统计的测量对象。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~99个字符。|系统支持基于两种形式的APN格式进行性能统计，包括根据FQDN或NI进行性能数据统计。具体使用哪种方式进行统计，取决于SET APN MODE命令的配置结果。操作员需要先通过SET APN MODE命令设置系统支持的APN统计格式，然后再通过本命令根据不同的格式设置APN的名称。FQDN由NI和OI，加上插在二者之间的“apn.epc”组成，格式为“NI.apn.epc.OI”。协议规定FQDN最长不能超过100个字符。NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），每个运营商都有一个缺省的APN运营商标识。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”（此处要求选用后面一种格式），要求如下：MNC和MCC都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APNID|APN标识|参数可选性:任选参数；参数类型:整数。|APN标识用于标识一个APN。
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型。|系统支持基于两种形式的APN格式进行性能统计，包括根据FQDN或NI进行性能数据统计。具体使用哪种方式进行统计，取决于SET APN MODE命令的配置结果。操作员需要先通过SET APN MODE命令设置系统支持的APN统计格式，然后再通过本命令根据不同的格式设置APN的名称。FQDN由NI和OI，加上插在二者之间的“apn.epc”组成，格式为“NI.apn.epc.OI”。协议规定FQDN最长不能超过100个字符。NI（Network Identifier，网络标识），定义了通过分组核心网连接的外部网络和终端的可选请求业务。它是由网络运营商分配给ISP或企业的，与其固定Internet域名相同的一个标识。例如，定义移动用户接入某公司的企业网，则APN的网络标识可以规划为“zte.com”。APN名称的NI部分，配置格式：“Label1.Label2.....Labeln”，可包含多个标签，要求如下：不能以“.”、“rac”、“lac”、“sgsn”或者“rnc”开头不能以“.gprs”结尾不能使用通配符“*”除了数字、字母、“-”、和“.”不能输入其余字符。示例：zte.com.cnOI（Operator Identifier，运营商标识），每个运营商都有一个缺省的APN运营商标识。APN名称的OI部分，配置格式为“Label1.Label2.Label3”，包含3个标签，其中，R8版本之前的形式为：MNC<MNC>.MCC<MCC>.gprs，R8版本之后的形式为“MNC<MNC>.MCC<MCC>.3gppnetwork.org”（此处要求选用后面一种格式），要求如下：MNC和MCC都是三位0~9的数字，如果不足三位，需要靠前用0补齐。除了数字、字母、“-”、和“.”不能输入其余字符。示例：mnc001.mcc222.3gppnetwork.org，mnc011.mcc460.gprs
命令举例 
查询已经配置的基于APN进行性能统计的测量对象。 
SHOW APN STATIS; 
`
命令 (No.9): SHOW APN STATIS
操作维护  APN标识 APN名称 
------------------------------------------------------------------
复制 删除   1         apn-ni.apn.epcmnc460.mcc01.3gppnetwork.org 
------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.088 秒）。
` 
父主题： [APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### eNodeB局向配置 
### eNodeB局向配置 
背景知识 
当网络或设备出现故障时，运营商有可能会需要获取某个或某几个特定的eNodeB局向的统计信息，用于进行故障定位、话务分析等。基于特定eNodeB局向的统计前，必须先完成该特定eNodeB局向的配置。目前，基于eNodeB测量的统计项为：基于eNB局向的S1AP消息测量。 
功能描述 
                “eNodeB局向配置”用于配置eNodeB局向，该配置的eNodeB局向作为性能测量对象。增加eNodeB局向配置后，在性能管理的
                
MME测量
                     > 链路测量
                     > 接口消息测量
                     > 基于eNB局向的S1AP消息测量
                节点下，可进行基于eNodeB的S1AP消息测量统计。
            
eNodeB局向配置的内容包括：MCC、MNC、ENODEBID以及NAME，MCC+MNC+ENODEBID唯一确定一个eNodeB局向。 
相关主题 
 
新增eNodeB局向配置(ADD ENODEBOBJ)
 
 
修改eNodeB局向配置(SET ENODEBOBJ)
 
 
删除eNodeB局向配置(DEL ENODEBOBJ)
 
 
查询eNodeB局向配置(SHOW ENODEBOBJ)
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增eNodeB局向配置(ADD ENODEBOBJ) 
#### 新增eNodeB局向配置(ADD ENODEBOBJ) 
命令功能 
该命令用于配置eNodeB局向。当运营商要求能在性能管理中进行基于eNB局向的S1AP消息测量时，需要进行该配置。配置成功后，eNodeB局向作为S1AP消息的测量对象，在性能管理的MME测量 > 链路测量 > 接口消息测量 > 基于eNB局向的S1AP消息测量
路径下，可进行基于eNodeB的S1AP消息测量统计。
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，如中国大陆（不含港澳台地区）为460或461。移动国家码由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动网号。如中国移动使用02（460-02）。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。移动国家码+移动网号+eNodeB局向号（MNC+MCC+ENODEBID）唯一标识一个eNodeB局向。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户为eNodeB局向设置的别名，便用区别不同的eNodeB局向，无其他意义。
命令举例 
新增eNodeB局向配置，其中移动国家码为460、移动网号为01、eNodeB局向号为123456、用户别名为enb01。 
ADD ENODEBOBJ:MCC="460",MNC="01",ENODEBID=123456,NAME="enb01"; 
父主题： [eNodeB局向配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改eNodeB局向配置(SET ENODEBOBJ) 
#### 修改eNodeB局向配置(SET ENODEBOBJ) 
命令功能 
该命令用于修改eNodeB局向配置的别名。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，如中国大陆（不含港澳台地区）为460或461。移动国家码由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动网号。如中国移动使用02（460-02）。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。移动国家码+移动网号+eNodeB局向号（MNC+MCC+ENODEBID）唯一标识一个eNodeB局向。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户为eNodeB局向设置的别名，便用区别不同的eNodeB局向，无其他意义。
命令举例 
将移动国家码为460、移动网号为01、局向号为123456的eNodeB局向配置的用户别名修改为enb02。 
SET ENODEBOBJ:MCC="460",MNC="01",ENODEBID=123456,NAME="enb02"; 
父主题： [eNodeB局向配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除eNodeB局向配置(DEL ENODEBOBJ) 
#### 删除eNodeB局向配置(DEL ENODEBOBJ) 
命令功能 
该命令用于删除已存在的eNodeB局向配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，如中国大陆（不含港澳台地区）为460或461。移动国家码由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动网号。如中国移动使用02（460-02）。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。移动国家码+移动网号+eNodeB局向号（MNC+MCC+ENODEBID）唯一标识一个eNodeB局向。
命令举例 
删除移动国家码为460、移动网号为01、局向号为123456的eNodeB局向配置。 
DEL ENODEBOBJ:MCC="460",MNC="01",ENODEBID=123456; 
父主题： [eNodeB局向配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询eNodeB局向配置(SHOW ENODEBOBJ) 
#### 查询eNodeB局向配置(SHOW ENODEBOBJ) 
命令功能 
该命令用于查询已经配置的eNodeB测量对象。如果设置查询条件，则只查询出符合条件的配置；否则，查询所有配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，如中国大陆（不含港澳台地区）为460或461。移动国家码由ITU统一分配和管理。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动网号。如中国移动使用02（460-02）。
ENODEBID|eNodeB局向号|参数可选性:任选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。移动国家码+移动网号+eNodeB局向号（MNC+MCC+ENODEBID）唯一标识一个eNodeB局向。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|eNodeB局向编号|参数可选性:任选参数；参数类型:整数。|eNodeB局向编号用于唯一标识一条eNodeB局向配置记录，该参数在增加eNodeB局向配置成功后自动产生，可通过SHOW ENODEBOBJ命令查询。
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，如中国大陆（不含港澳台地区）为460或461。移动国家码由ITU统一分配和管理。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动网号。如中国移动使用02（460-02）。
ENODEBID|eNodeB局向号|参数可选性:任选参数；参数类型:整数。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。移动国家码+移动网号+eNodeB局向号（MNC+MCC+ENODEBID）唯一标识一个eNodeB局向。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户为eNodeB局向设置的别名，便用区别不同的eNodeB局向，无其他意义。
命令举例 
查询所有eNodeB局向配置。 
SHOW ENODEBOBJ; 
`
命令 (No.4): SHOW ENODEBOBJ
操作维护       eNodeB局向编号 移动国家码   移动网号   eNodeB局向号   用户别名 
--------------------------------------------------------------------------------------
复制 修改 删除    1                 460           01       123456       enb02 
--------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.092 秒）。
` 
父主题： [eNodeB局向配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 组合条件配置 
### 组合条件配置 
背景知识 
为了满足运营商对性能测量统计结果的不同要求，比如运营商希望在统计QCI的同时还关注TA，组合测量对象就随之应运而出了。 
所谓组合测量对象是指可以将已支持的测量对象组合为新的测量对象进行统计，如运营商希望统计QCI外还关注TA，那么配置QCI+TA的组合为测量对象就可满足要求。 
功能描述 
            
            组合条件配置的结果用于性能测量，每一个组合条件配置结果作为一个组合测量对象，应用于性能管理的
            
MME测量
                 > 组合条件测量
                 > 流程测量
            节点下的承载激活流程组合条件测量、承载修改流程组合条件测量、承载去激活流程组合条件测量、承载激活分网元组合条件测量以及承载修改分网元组合条件测量。
        
相关主题 
 
新增组合条件(ADD COMCOND)
 
 
修改组合条件(SET COMCOND)
 
 
删除组合条件(DEL COMCOND)
 
 
查询组合条件(SHOW COMCOND)
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增组合条件(ADD COMCOND) 
#### 新增组合条件(ADD COMCOND) 
命令功能 
该命令用于配置组合条件，每一个组合条件配置结果作为一个组合测量对象，应用于性能管理的MME测量 > 组合条件测量 > 流程测量
节点下的承载激活流程组合条件测量、承载修改流程组合条件测量、承载去激活流程组合条件测量、承载激活分网元组合条件测量以及承载修改分网元组合条件测量。
注意事项 
一种测量类型只能对应一种组合条件。比如，承载激活流程测量的组合一旦配置了TA+QCI的组合，那么就不能配置任何其他的组合。 
参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|用于组合统计的测量类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该测量类型与性能管理的MME测量 > 组合条件测量 > 流程测量节点下的承载激活流程组合条件测量、承载修改流程组合条件测量、承载去激活流程组合条件测量、承载激活分网元组合条件测量以及承载修改分网元组合条件测量相对应。
TAID|跟踪区标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|各TA在MME内部的唯一标识，在MME中一个TAID对应一个跟踪区TA。该参数关联ADD TA 命令配置的TAID。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~9。|流类标识 ，每个QCI对应一组QoS属性。
APNID|APN ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|APN的标识，该参数关联ADD APN STATIS命令配置结果中的“APN标识”。
NAME|测量对象描述|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|组合条件配置的名称，用于区别不同的组合条件配置。
命令举例 
新增组合条件配置，其中用于组合统计的测量类型为承载激活流程组合条件测量、跟踪区标识为1、测量对象描述为type_1。 
ADD COMCOND:TYPE="MOPTYPEID_MME_BEARACT",TAID=1,NAME="type_1"; 
父主题： [组合条件配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改组合条件(SET COMCOND) 
#### 修改组合条件(SET COMCOND) 
命令功能 
该命令用于修改已配置的组合条件，只能修改组合条件配置的测量对象描述。
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|用于组合统计的测量类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该测量类型与性能管理的MME测量 > 组合条件测量 > 流程测量节点下的承载激活流程组合条件测量、承载修改流程组合条件测量、承载去激活流程组合条件测量、承载激活分网元组合条件测量以及承载修改分网元组合条件测量相对应。
TAID|跟踪区标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|各TA在MME内部的唯一标识，在MME中一个TAID对应一个跟踪区TA。该参数关联ADD TA 命令配置的TAID。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~9。|流类标识 ，每个QCI对应一组QoS属性。
APNID|APN ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|APN的标识，该参数关联ADD APN STATIS命令配置结果中的“APN标识”。
NAME|测量对象描述|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|组合条件配置的名称，用于区别不同的组合条件配置。
命令举例 
修改用于组合统计的测量类型为承载激活流程组合条件测量，跟踪区标识为1的配置数据，将该配置的测量对象描述修改为type_2。 
SET COMCOND:TYPE="MOPTYPEID_MME_BEARACT",TAID=1,NAME="type_2"; 
父主题： [组合条件配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除组合条件(DEL COMCOND) 
#### 删除组合条件(DEL COMCOND) 
命令功能 
该命令用于删除已配置的组合条件。可根据测量对象ID进行删除也可根据测量类型进行删除。测量对象ID可通过[SHOW COMCOND]命令查询。
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
OBJECTID|测量对象ID|参数可选性:必须单选参数；参数类型:整数；参数范围为:1~100。|测量对象ID唯一标识一条组合条件配置，该参数在增加组合条件配置成功后自动产生，可通过SHOW COMCOND命令查询。
TYPE|用于组合统计的测量类型|参数可选性:必须单选参数；参数类型:枚举。参见枚举定义。|该测量类型与性能管理的MME测量 > 组合条件测量 > 流程测量节点下的承载激活流程组合条件测量、承载修改流程组合条件测量、承载去激活流程组合条件测量、承载激活分网元组合条件测量以及承载修改分网元组合条件测量相对应。
TAID|跟踪区标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|各TA在MME内部的唯一标识，在MME中一个TAID对应一个跟踪区TA。该参数关联ADD TA 命令配置的TAID。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:1~9。|流类标识 ，每个QCI对应一组QoS属性。
APNID|APN ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|APN的标识，该参数关联ADD APN STATIS命令配置结果中的“APN标识”。
命令举例 
删除测量对象ID为1的组合条件配置。 
DEL COMCOND:OBJECTID=1; 
父主题： [组合条件配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询组合条件(SHOW COMCOND) 
#### 查询组合条件(SHOW COMCOND) 
命令功能 
该命令用于查询已经配置的组合条件。如果设置查询条件，则只查询出符合条件的配置；否则，查询所有配置。 
注意事项 
无 
参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|用于组合统计的测量类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该测量类型与性能管理的MME测量 > 组合条件测量 > 流程测量节点下的承载激活流程组合条件测量、承载修改流程组合条件测量、承载去激活流程组合条件测量、承载激活分网元组合条件测量以及承载修改分网元组合条件测量相对应。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OBJECTID|测量对象ID|参数可选性:任选参数；参数类型:整数。|测量对象ID唯一标识一条组合条件配置，该参数在增加组合条件配置成功后自动产生，可通过SHOW COMCOND命令查询。
TYPE|用于组合统计的测量类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该测量类型与性能管理的MME测量 > 组合条件测量 > 流程测量节点下的承载激活流程组合条件测量、承载修改流程组合条件测量、承载去激活流程组合条件测量、承载激活分网元组合条件测量以及承载修改分网元组合条件测量相对应。
TAID|跟踪区标识|参数可选性:任选参数；参数类型:整数。|各TA在MME内部的唯一标识，在MME中一个TAID对应一个跟踪区TA。该参数关联ADD TA 命令配置的TAID。
QCI|QCI|参数可选性:任选参数；参数类型:整数。|流类标识 ，每个QCI对应一组QoS属性。
APNID|APN ID|参数可选性:任选参数；参数类型:整数。|APN的标识，该参数关联ADD APN STATIS命令配置结果中的“APN标识”。
NAME|测量对象描述|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|组合条件配置的名称，用于区别不同的组合条件配置。
命令举例 
查询所有的组合条件配置。 
SHOW COMCOND; 
`
命令 (No.17): SHOW COMCOND
操作维护       测量对象ID 用于组合统计的测量类型      跟踪区标识    地域编号    QCI   APN ID 测量对象描述 
--------------------------------------------------------------------------------------------------------------------
复制 修改 删除    1             承载激活流程组合条件测量  1            0        0   0         type_2 
--------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.062 秒）。
` 
父主题： [组合条件配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME TA组配置 
### MME TA组配置 
背景知识 
            
            目前网络采用的都是大区制，即一个MME/SGSN管理多个地市。在运维的过程中，为了监控网络运行情况，需要监控某些热点区域或者某个地市的指标数据。
        
功能描述 
            
            该功能用于满足大区制下的地市或者热点区域指标监控的要求，把某些TA归类为一个组，做为一个单元采集数据。
        
相关主题 
 
TA组编号配置
 
 
TA组资源配置
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### TA组编号配置 
#### TA组编号配置 
背景知识 
MME支持基于TA的性能统计，在运维中需要获取某些TA的合并数据，现有的基于TA的统计无法满足。因此MME需要根据配置把某个或者某些TA归类到一个组，即TA组，统计并呈现出对应TA组的性能统计数据。TA组是TA资源的集合。 
功能描述 
该功能用于对MME网元管理的TA组进行配置。包括TA组编号和别名 
相关主题 
 
新增TA组编号配置(ADD MMETAGROUPID)
 
 
修改TA组编号配置(SET MMETAGROUPID)
 
 
删除TA组编号配置(DEL MMETAGROUPID)
 
 
查询TA组编号配置(SHOW MMETAGROUPID)
 
 
父主题： [MME TA组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 新增TA组编号配置(ADD MMETAGROUPID) 
##### 新增TA组编号配置(ADD MMETAGROUPID) 
命令功能 
该命令用于配置MME网元管理的TA组的编号和别名。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于设置TA组的编号。
ALIAS|别名|参数可选性:任选参数；参数类型:字符型。|该参数用于设置TA组的别名，比如：南京雨花区、南京鼓楼区等。
命令举例 
新增TA组编号配置，其中TA组标识为1，别名为"yuhua"。 
ADD MMETAGROUPID:GROUPID=1,ALIAS="yuhua" 
父主题： [TA组编号配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 修改TA组编号配置(SET MMETAGROUPID) 
##### 修改TA组编号配置(SET MMETAGROUPID) 
命令功能 
该命令用于修改MME的TA组每个编号对应的别名。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于设置TA组的编号。
ALIAS|别名|参数可选性:任选参数；参数类型:字符型。|该参数用于设置TA组的别名，比如：南京雨花区、南京鼓楼区等。
命令举例 
修改TA组编号配置，其中TA组标识为1，别名修改为"YuhuaDistrict"。 
SET MMETAGROUPID:GROUPID=1,ALIAS="YuhuaDistrict" 
父主题： [TA组编号配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 删除TA组编号配置(DEL MMETAGROUPID) 
##### 删除TA组编号配置(DEL MMETAGROUPID) 
命令功能 
该命令用于删除MME网元配置的TA组。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于设置TA组的编号。
命令举例 
删除TA组标识为1的TA组编号配置。 
DEL MMETAGROUPID:GROUPID=1 
父主题： [TA组编号配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询TA组编号配置(SHOW MMETAGROUPID) 
##### 查询TA组编号配置(SHOW MMETAGROUPID) 
命令功能 
该命令用于查询MME网元配置的TA组的编号和别名。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于设置TA组的编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于设置TA组的编号。
ALIAS|别名|参数可选性:任选参数；参数类型:字符型。|该参数用于设置TA组的别名，比如：南京雨花区、南京鼓楼区等。
命令举例 
查询TA组编号配置。 
SHOW APN STATI 
`
(No.7) : SHOW MMETAGROUPID:
-----------------uMAC_MME_V7master/NFS_MMESGSN_0----------------
操作维护       TA组号 别名          
------------------------------------
复制 修改 删除 1      YuhuaDistrict 
------------------------------------
记录数：1
执行成功开始时间:2021-08-17 17:36:52 耗时: 1.578秒。
` 
父主题： [TA组编号配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### TA组资源配置 
#### TA组资源配置 
背景知识 
MME根据配置把某个或者某些TA归类到一个组，称为TA组，然后统计并呈现对应的性能统计数据。一个TA组中可以包含多个TA资源分段，一个TA资源分段只能归属于一个TA组。一个TA资源分段包括TA资源归属的TA组、TA资源段的MCC和MNC、起始值和终止值，不同的资源分段之间不能重叠交叉。 
功能描述 
该功能用于配置指定TA组下关联的TA资源分段信息，包括TA资源归属的TA组、TA资源段的MCC和MNC、起始值和终止值。 
一个TA组中只有配置了资源分段，这个TA组才有意义。 
相关主题 
 
新增TA组资源配置(ADD MMETAGRPRESOURSES)
 
 
删除TA组资源配置(DEL MMETAGRPRESOURSES)
 
 
查询TA组资源配置(SHOW MMETAGRPRESOURSES)
 
 
父主题： [MME TA组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 新增TA组资源配置(ADD MMETAGRPRESOURSES) 
##### 新增TA组资源配置(ADD MMETAGRPRESOURSES) 
命令功能 
该命令用于增加TA组关联的TA列表。当需要把某些TA归类为一个TA组的时候使用该配置。配置后，MME根据配置把某个或者某些TA按照一个组来使用。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于设置TA组的编号。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
TABEGIN|跟踪区码起始值|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|该参数用于指定资源段的起始TAC，TAC固定是4位十六进制字符。
TAEND|跟踪区码终止值|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|该参数用于指定资源段的终止TAC，TAC固定是4位十六进制字符。
命令举例 
新增TA组关联的TA列表，其中TA组标识为1，移动国家码为460，移动网号为11，跟踪区码范围为6001到7001。 
ADD MMETAGRPRESOURSES:GROUPID=1,MCC="460",MNC="11",TABEGIN="6001",TAEND="7001" 
父主题： [TA组资源配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 删除TA组资源配置(DEL MMETAGRPRESOURSES) 
##### 删除TA组资源配置(DEL MMETAGRPRESOURSES) 
命令功能 
该命令用于删除TA组关联的TA列表。可以根据TA组ID删除该TA组下的所有TA列表，或者根据TA组+MCC+MNC+跟踪区码起始值+跟踪区码终止值删除某一条记录。 
注意事项 
根据TA组+MCC+MNC+跟踪区码起始值+跟踪区码终止值删除某一条记录时，删除的记录需与[ADD MMETAGRPRESOURSES]命令中新增的记录对应。
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|该参数用于设置TA组的编号。
MCC|移动国家码|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
TABEGIN|跟踪区码起始值|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:4~4个字符。|该参数用于指定资源段的起始TAC，TAC固定是4位十六进制字符。
TAEND|跟踪区码终止值|参数可选性:特殊任选参数；参数类型:字符型；参数范围为:4~4个字符。|该参数用于指定资源段的终止TAC，TAC固定是4位十六进制字符。
命令举例 
删除TA组关联的TA列表，其中TA组标识为1。 
DEL MMETAGRPRESOURSES:GROUPID=1 
父主题： [TA组资源配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
##### 查询TA组资源配置(SHOW MMETAGRPRESOURSES) 
##### 查询TA组资源配置(SHOW MMETAGRPRESOURSES) 
命令功能 
该命令用于查询TA组关联的TA列表。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|该参数用于设置TA组的编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|TA组号|参数可选性:任选参数；参数类型:整数。|该参数用于设置TA组的编号。
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
TABEGIN|跟踪区码起始值|参数可选性:任选参数；参数类型:字符型。|该参数用于指定资源段的起始TAC，TAC固定是4位十六进制字符。
TAEND|跟踪区码终止值|参数可选性:任选参数；参数类型:字符型。|该参数用于指定资源段的终止TAC，TAC固定是4位十六进制字符。
命令举例 
该命令用于查询TA组关联的TA列表。 
SHOW MMETAGRPRESOURSES 
`
(No.13) : SHOW MMETAGRPRESOURSES:
-----------------NFS_MMESGSN_0----------------
操作维护       TA组号 移动国家码 移动网号 跟踪区码起始值 跟踪区码终止值 
------------------------------------------------------------------------
复制 删除      1      460        11       5001           5002           
复制 删除      2048   460        11       1001           2001           
复制 删除      1      460        11       6001           7001           
复制 删除      1      460        111      2222           2222           
------------------------------------------------------------------------
记录数：4
执行成功开始时间:2021-08-25 21:26:04 耗时: 0.81 秒
` 
父主题： [TA组资源配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 测量类型对象数配置 
### 测量类型对象数配置 
背景知识 
基于系统的支持能力，当前测量类型能够支持的对象数都是按照最大值来设置，但当所有测量类型支持的对象数过于庞大时，性能任务超过了系统的处理能力，可能会出现统计数据的延迟、错误和丢失等，因此要求当出现上述问题时，能够降低测量类型支持的对象数量。 
功能描述 
该配置用来控制系统支持的测量类型所对应的对象容量，可以针对不同的测量类型设置不同的对象容量。 
相关主题 
 
新增测量类型对象数配置(ADD POOBJNUMCFG)
 
 
修改测量类型对象数配置(SET POOBJNUMCFG)
 
 
删除测量类型对象数配置(DEL POOBJNUMCFG)
 
 
查询测量类型对象数配置(SHOW POOBJNUMCFG)
 
 
父主题： [性能管理专用配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增测量类型对象数配置(ADD POOBJNUMCFG) 
#### 新增测量类型对象数配置(ADD POOBJNUMCFG) 
命令功能 
该命令用于增加测量类型支持的最大对象数，当需要控制某个测量类型的对象数时，执行此命令。 
注意事项 
增加某个测量类型支持的对象数后，如果已经激活的任务对象数大于设置后的对象数，则自动根据设置后的对象数上报数据，超过的部分对象不再上报。 
参数说明 
标识|名称|类型|说明
---|---|---|---
POID|测量类型标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置测量类型标识。
CAPACITY|容量|参数可选性:必选参数；参数类型:整数；参数范围为:100~65535。|该参数用于配置PO ID标识的测量类型能够支持的对象数的最大值。
命令举例 
新增一条测量类型对象数配置，测量类型编号为44000、容量为300。 
ADD POOBJNUMCFG:POID=44000,CAPACITY=300 
父主题： [测量类型对象数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改测量类型对象数配置(SET POOBJNUMCFG) 
#### 修改测量类型对象数配置(SET POOBJNUMCFG) 
命令功能 
该命令用于修改测量类型支持的最大对象数，当某个测量类型的对象数需要减少或者增加时，执行此命令。 
注意事项 
设置某个测量类型支持的对象数后，如果已经激活的任务对象数大于设置后的对象数，则自动根据设置后的对象数上报数据，超过的部分对象不再上报。 
参数说明 
标识|名称|类型|说明
---|---|---|---
POID|测量类型标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置测量类型标识。
CAPACITY|容量|参数可选性:必选参数；参数类型:整数；参数范围为:100~65535。|该参数用于配置PO ID标识的测量类型能够支持的对象数的最大值。
命令举例 
修改一条测量类型对象数配置，测量类型编号为44000、容量为300。 
SET POOBJNUMCFG:POID=44000,CAPACITY=300 
父主题： [测量类型对象数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除测量类型对象数配置(DEL POOBJNUMCFG) 
#### 删除测量类型对象数配置(DEL POOBJNUMCFG) 
命令功能 
该命令用于删除测量类型支持的最大对象数，当某个测量类型的对象数不需要控制时，通过该命令来移除控制。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
POID|测量类型标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置测量类型标识。
命令举例 
删除一条测量类型对象数配置，测量类型编号为44000。 
DEL POOBJNUMCFG:POID=44000 
父主题： [测量类型对象数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询测量类型对象数配置(SHOW POOBJNUMCFG) 
#### 查询测量类型对象数配置(SHOW POOBJNUMCFG) 
命令功能 
该命令用于查询测量类型支持的最大对象数。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
POID|测量类型标识|参数可选性:任选参数；参数类型:整数。|该参数用于配置测量类型标识。
CAPACITY|容量|参数可选性:任选参数；参数类型:整数。|该参数用于配置PO ID标识的测量类型能够支持的对象数的最大值。
命令举例 
查询所有测量类型对象数配置。 
SHOW POOBJNUMCFG 
`
(No.1) : SHOW POOBJNUMCFG
-----------------NFS_MMESGSN_0----------------
操作维护       测量类型标识 容量 
---------------------------------
复制 修改 删除 44000        400  
---------------------------------
记录数：1
执行成功开始时间:2021-11-04 13:25:45 耗时: 0.798 秒
` 
父主题： [测量类型对象数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MCDR配置 
## MCDR配置 
背景知识 
M-CDR：即M-CDR话单（Mobility management generated - Charging Data Record）。M-CDR话单记录SGSN上附着用户的移动性管理相关的计费信息，主要包括话单类型、IMSI、话单序列号、用户当前的路由区以及路由区改变信息。 
用户成功附着或者局间路由更新以后，M-CDR话单打开，用户处于计费状态；M-CDR话单关闭的场景如下： 
移动用户分离。 
用户发起局间路由更新。 
任何异常释放。 
用户附着的时长达到一个阈值。 
局内路由更新，且路由区变化次数达到一个阈值。 
网管强制输出M-CDR话单。 
用户发起局内系统间切换。 
协议依据：3GPP TS 32.251 第5.2.3.2节。 
功能描述 
用户附着的时长达到一个阈值或者用户局内路由更新且路由区变化次数达到一个阈值时，M-CDR话单关闭，SGSN输出M-CDR话单，MCDR配置用于设置这两个阈值。 
注意事项： 
                如果配置了指定出话单时间和出话单原因（网管强制），命令为：
                [SET CDR TIME]
                。在该命令中设置的出话单时间到达时，SGSN也会输出M-CDR话单。
            
相关主题 
 
设置MCDR配置(SET MCDR)
 
 
查询MCDR配置(SHOW MCDR)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置MCDR配置(SET MCDR) 
### 设置MCDR配置(SET MCDR) 
命令功能 
该命令用于设置M-CDR配置。可以设置用户接入成功后，经过多长时间后出M-CDR话单。可以设置终端在本局内发生多少次路由区切换后出一份M-CDR话单。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
TIMELMT|M-CDR超时关闭时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:5~2880。|用户接入成功后，用户一直没有出M-CDR话单，需要设置在一段时间后出一份M-CDR话单，此参数即为设置这段时间的值。
MCLMT|移动性改变次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|用户在本局路由区会经常切换，当切换达到一定数量时，则会出一份M-CDR话单，此参数即为设置切换数量的值。
命令举例 
设置MCDR话单MCDR超时关闭时长为5分钟，移动性改变次数为1次。 
SET MCDR:TIMELMT=5,MCLMT=1;  
父主题： [MCDR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询MCDR配置(SHOW MCDR) 
### 查询MCDR配置(SHOW MCDR) 
命令功能 
查询M-CDR配置，显示所配置的M-CDR超时关闭时长和移动性改变次数信息。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TIMELMT|M-CDR超时关闭时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:5~2880。|用户接入成功后，用户一直没有出M-CDR话单，需要设置在一段时间后出一份M-CDR话单，此参数即为设置这段时间的值。
MCLMT|移动性改变次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|用户在本局路由区会经常切换，当切换达到一定数量时，则会出一份M-CDR话单，此参数即为设置切换数量的值。
命令举例 
显示MCDR配置。 
SHOW MCDR;  
`
命令 (No.1): SHOW MCDR
操作维护  M-CDR超时关闭时长(分钟)   移动性改变次数
--------------------------------------------------
修改      5                         1
--------------------------------------------------
记录数 1
命令执行成功（耗时 0.063 秒）。
` 
父主题： [MCDR配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## CDR过滤配置 
## CDR过滤配置 
背景知识 
CDR过滤是控制SGSN启用或关闭话单，对如下各话单分别进行控制，便于运营商根据本地计费策略灵活控制SGSN是否输出相应话单。 
M-CDR：M-CDR话单（Mobility management generated - Charging Data Record）。 
M-CDR话单记录的是，SGSN下的用户其移动性管理相关的计费信息，主要包括话单类型、服务的IMSI、话单序列号、用户当前的路由区以及路由区改变信息。 
SMS-SMO-CDR：短消息起呼话单（Short message Mobile Originated – CDR）。 
SMS-SMO-CDR话单记录的是，一条短消息在起呼方向经过SGSN传送相关的计费信息，主要包括话单类型、服务的IMSI、话单序列号、短消息服务中心的地址、短消息触发的位置区和路由区、短消息传送结果等。 
SMS-SMT-CDR：短消息终呼话单（Short message Mobile Terminated – CDR）。 
SMS-SMT-CDR话单记录的是，一条短消息在终呼方向经过SGSN传送相关的计费信息，主要包括话单类型、服务的IMSI、话单序列号、短消息服务中心的地址、短消息目的位置区和路由区、短消息传送结果等。 
LCS-MO-CDR：定位起呼话单（Location Service Mobile Originated – CDR）。 
LCS-MO-CDR话单记录的是，UE/MS发起一个定位请求经过SGSN传送相关的计费信息，主要包括话单类型、服务的IMSI、话单序列号、定位方式（Location Method）、定位QoS、定位优先级、定位原因、位置信息等。 
LCS-MT-CDR：定位终呼话单（Location Service Mobile Terminated – CDR）。 
LCS-MT-CDR话单记录的是，外部实体向UE发起定位请求经过SGSN传送相关的计费信息，主要包括话单类型、服务的IMSI、话单序列号、定位类型（Location Type）、定位QoS、定位优先级、定位原因、Location Estimate、位置信息等。 
LCS-NI-CDR：定位网络触发话单（Location Service Network Induced-CDR）。 
LCS-NI-CDR话单记录的是，网络触发的定位请求经过SGSN传送相关的计费信息，主要包括话单类型、服务的IMSI、话单序列号、定位QoS、定位优先级、定位原因、Location Estimate、位置信息等。 
以上各话单描述依据协议：3GPP TS 32.251 第5.2.3和6.1节。 
功能描述 
CDR过滤配置在以下场景使用。 
 
运营商根据本地计费策略不再需要SGSN输出M-CDR/SMS-SMO-CDR/SMS-SMT-CDR/LCS-MO-CDR/LCS-MT-CDR/LCS-NI-CDR话单，或运营商已关闭某话单后又需要SGSN启用该话单。
 
 
                        协议3GPP TS 32.251中M-CDR/SMS-SMO-CDR/SMS-SMT-CDR的话单中不要求输出SGSN的PLMN ID。当SGSN支持多PLMN ID（
                        ADD HPLMNCFG
                        ）时，如果运营商需要在话单中输出SGSN的PLMN ID，用于区分计费不同的PLMN或者通过话单了解用户分布情况，CDR过滤配置可以控制SGSN在M-CDR/SMS-SMO-CDR/SMS-SMT-CDR话单中是否输出PLMN ID。
                    
 
 
CDR过滤配置可以控制SGSN在SMS-SMT-CDR话单中是否输出发送者号码（Origination Number）。
 
 
相关主题 
 
设置CDR过滤配置(SET CDRFLT)
 
 
查询CDR过滤配置(SHOW CDRFLT)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置CDR过滤配置(SET CDRFLT) 
### 设置CDR过滤配置(SET CDRFLT) 
命令功能 
该命令用于设置CDR过滤配置，当需要过滤各类话单时使用该命令，包括M-CDR话单、SMS-SMO-CDR话单、过滤SMS-SMT-CDR话单、LCS-MO-CDR话单、LCS-MT-CDR话单、LCS-NI-CDR话单。将期望的话单配置为过滤后，SGSN将不再将该类话单上报至计费服务器，SGSN将直接丢弃被过滤的话单信息。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
MCDRFLT|过滤M-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤M-CDR（移动性话单），设置选项中YES表示过滤，NO表示不过滤。
SMOCDRFLT|过滤SMS-SMO-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤SMS-SMO-CDR（短消息起呼话单），设置选项中YES表示过滤，NO表示不过滤。
SMTCDRFLT|过滤SMS-SMT-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤SMS-SMT-CDR（短消息终呼话单），设置选项中YES表示过滤，NO表示不过滤。
LCSMOCDRFLT|过滤LCS-MO-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤LCS-MO-CDR（LCS起呼话单），设置选项中YES表示过滤，NO表示不过滤。
LCSMTCDRFLT|过滤LCS-MT-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤LCS-MT-CDR（LCS终呼话单），设置选项中YES表示过滤，NO表示不过滤。
LCSNICDRFLT|过滤LCS-NI-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤LCS-NI-CDR，设置选项中YES表示过滤，NO表示不过滤。
MCDRPLMNFLT|过滤M-CDR中PLMNID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤M-CDR中PLMN标识，设置选项中YES表示过滤，NO表示不过滤。
SMSCDRPLMNFLT|过滤SMS-CDR中PLMNID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤SMS-CDR中的PLMN标识，设置选项中YES表示过滤，NO表示不过滤。
NUMBERFLT|过滤短信终呼话单中发送者号码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤SMS-SMT-CDR中的短信发送方号码，设置选项中YES表示过滤，NO表示不过滤。
命令举例 
设置SGSN的话单过滤配置为MCDR不过滤，SMS-SMO-CDR话单不过滤，SMS-SMT-CDR话单不过滤，LCS-MO-CDR话单不过滤，LCS-MT-CDR话单不过滤，LCS-NI-CDR话单不过滤，M-CDR中PLMNID不过滤，SMS-CDR中PLMNID不过滤。 
SET CDRFLT:MCDRFLT="NO",SMOCDRFLT="NO",SMTCDRFLT="NO",LCSMOCDRFLT="NO",LCSMTCDRFLT="NO",LCSNICDRFLT="NO",MCDRPLMNFLT="NO",SMSCDRPLMNFLT="NO";  
父主题： [CDR过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询CDR过滤配置(SHOW CDRFLT) 
### 查询CDR过滤配置(SHOW CDRFLT) 
命令功能 
该命令用于查询CDR过滤配置信息，显示以下内容。 
 
显示可以被过滤话单的种类，并显示这些话单是否已经设置为过滤。
 
 
显示SMS-CDR话单中的PLMNID信息是否已经设置为被过滤。
 
 
显示短信终呼话单中短信发送方号码是否已经被设置为过滤。
 
 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MCDRFLT|过滤M-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤M-CDR（移动性话单），设置选项中YES表示过滤，NO表示不过滤。
SMOCDRFLT|过滤SMS-SMO-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤SMS-SMO-CDR（短消息起呼话单），设置选项中YES表示过滤，NO表示不过滤。
SMTCDRFLT|过滤SMS-SMT-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤SMS-SMT-CDR（短消息终呼话单），设置选项中YES表示过滤，NO表示不过滤。
LCSMOCDRFLT|过滤LCS-MO-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤LCS-MO-CDR（LCS起呼话单），设置选项中YES表示过滤，NO表示不过滤。
LCSMTCDRFLT|过滤LCS-MT-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤LCS-MT-CDR（LCS终呼话单），设置选项中YES表示过滤，NO表示不过滤。
LCSNICDRFLT|过滤LCS-NI-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤LCS-NI-CDR，设置选项中YES表示过滤，NO表示不过滤。
MCDRPLMNFLT|过滤M-CDR中PLMNID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤M-CDR中PLMN标识，设置选项中YES表示过滤，NO表示不过滤。
SMSCDRPLMNFLT|过滤SMS-CDR中PLMNID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤SMS-CDR中的PLMN标识，设置选项中YES表示过滤，NO表示不过滤。
NUMBERFLT|过滤短信终呼话单中发送者号码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|过滤SMS-SMT-CDR中的短信发送方号码，设置选项中YES表示过滤，NO表示不过滤。
命令举例 
显示CDR过滤配置信息。 
SHOW CDRFLT;  
`
命令 (No.1): SHOW CDRFLT
操作维护  过滤M-CDR   过滤SMS-SMO-CDR   过滤SMS-SMT-CDR   过滤LCS-MO-CDR   过滤LCS-MT-CDR   过滤LCS-NI-CDR   过滤M-CDR中PLMNID   过滤SMS-CDR中PLMNID   过滤短信终呼话单中发送者号码
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      否          否                否                否               否               否               否                  否                    是
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.062 秒）。
` 
父主题： [CDR过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## USUP报文缓存配置 
## USUP报文缓存配置 
背景知识 
SGSN USUP模块处理用户面报文时，由于下行的2、3G用户面数据会触发寻呼、上行2G SNDCP（Sub Network Dependent Convergence Protocol，子网相关会聚协议）重组，需要MME缓存用户面报文。 
功能描述 
SGSN USUP模块处理用户面报文时，由于下行2、3G用户面数据触发寻呼、上行2G SNDCP（Sub Network Dependent Convergence Protocol，子网相关会聚协议）重组，需要缓存用户面报文。 
USUP报文缓存配置用于配置2G USUP和3G USUP模块对每个PDP上下文最多缓存的报文个数。配置SGSN对2G用户上行数据包进行SNDCP重组时各个缓存大小、释放时长等参数。 
相关主题 
 
3G USUP报文缓存配置
 
 
2G USUP报文缓存配置
 
 
SNDCP重组配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 3G USUP报文缓存配置 
### 3G USUP报文缓存配置 
背景知识 
                每个USUP模块寻呼缓存报文数的总量有最大值限制，参见命令
                [SHOW CAPACITY]
                。单个USUP模块的所有PDP上下文缓存的报文个数相加，如果大于总量，则后续寻呼过程中的数据报文将无法缓存，只有等寻呼应答或超时后，对缓存进行释放才可以继续缓存。
            
缓存的报文个数越多，报文丢失概率就越小，但是因为总的缓存个数数目限制，同时缓存的PDP上下文数目就越小。 
功能描述 
“3G USUP报文缓存配置”配置下行3G用户面数据触发寻呼时，每个PDP上下文最多缓存的报文个数。 
本配置项默认参数经过测试和商用的验证，不建议修改。 
相关主题 
 
设置3G用户报文缓存配置(SET 3G USUP PACKBUF)
 
 
查询3G用户报文缓存配置(SHOW 3G USUP PACKBUF)
 
 
父主题： [USUP报文缓存配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置3G用户报文缓存配置(SET 3G USUP PACKBUF) 
#### 设置3G用户报文缓存配置(SET 3G USUP PACKBUF) 
命令功能 
该命令用于设置3G用户报文寻呼缓存配置。当需要设置每PDP上下文寻呼缓存下行数据包最大个数时，使用该命令，设置成功后，新接入的3G用户在寻呼过程中，每个PDP最大可以缓存的下行数据包个数将采用本配置的值。 
寻呼缓存指的是用户在寻呼过程中可以对此时下行的数据报文进行一定数量的缓存，当寻呼成功后再将缓存的报文下发给用户，保证了业务的连续性。 
注意事项 
 
每个用户面模块寻呼缓存报文数的总量有最大值限制，参见命令SHOW CAPACITY。单个用户面模块的所有PDP上下文缓存的报文个数相加，如果大于总量，则后续寻呼过程中的数据报文将无法缓存，只有等寻呼应答或超时后，对缓存进行释放才可以继续缓存。
 
 
每个用户面模块寻呼缓存报文数的总量一般采用默认值，若无特殊需要，无需修改。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PDPPACKBUF|每PDP缓存最大下行报文数|参数可选性:必选参数；参数类型:整数；参数范围为:0~70。|该参数用来设定寻呼缓存每PDP上下文能够缓存报文最大数量。若实际缓存报文数超过该配置值，则后续寻呼过程中的数据报文将无法缓存，只有等寻呼应答或超时后，对缓存进行释放才可以继续缓存。
命令举例 
设置3G用户报文缓存配置，每PDP缓存最大下行报文数为0，即不缓存。
SET 3G USUP PACKBUF:PDPPACKBUF=0; 
父主题： [3G USUP报文缓存配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询3G用户报文缓存配置(SHOW 3G USUP PACKBUF) 
#### 查询3G用户报文缓存配置(SHOW 3G USUP PACKBUF) 
命令功能 
该命令用于查询3G用户报文寻呼缓存配置。寻呼缓存作用是，在用户寻呼过程中可以对此时下行的数据报文进行一定数量的缓存，当寻呼成功后再将缓存的报文下发给用户，保证了业务的连续性。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PDPPACKBUF|每PDP缓存最大下行报文数|参数可选性:任选参数；参数类型:整数。|该参数用来设定寻呼缓存每PDP上下文能够缓存报文最大数量。若实际缓存报文数超过该配置值，则后续寻呼过程中的数据报文将无法缓存，只有等寻呼应答或超时后，对缓存进行释放才可以继续缓存。
命令举例 
查询3G用户报文缓存配置。
SHOW 3G USUP PACKBUF; 
`
命令 (No.1): SHOW 3G USUP PACKBUF;
操作维护  每PDP缓存最大下行报文数
---------------------------------
修改      5
---------------------------------
记录数 1
命令执行成功（耗时 0.053 秒）。
` 
父主题： [3G USUP报文缓存配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 2G USUP报文缓存配置 
### 2G USUP报文缓存配置 
背景知识 
                每个USUP模块寻呼缓存报文数的总量有最大值限制，参见命令
                [SHOW CAPACITY]
                。单个USUP模块的所有PDP上下文缓存的报文个数相加，如果大于总量，则后续寻呼过程中的数据报文将无法缓存，只有等寻呼应答或超时后，对缓存进行释放才可以继续缓存。
            
缓存的报文个数越多，报文丢失概率就越小，但是因为总的缓存个数数目限制，同时缓存的PDP上下文数目就越小。 
功能描述 
“2G USUP报文缓存配置”配置下行2G用户面数据触发寻呼时，每个PDP上下文最多缓存的报文个数。 
本配置项默认参数经过测试和商用的验证，不建议修改。 
相关主题 
 
设置2G用户报文缓存配置(SET 2G USUP PACKBUF)
 
 
查询2G用户报文缓存配置(SHOW 2G USUP PACKBUF)
 
 
父主题： [USUP报文缓存配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置2G用户报文缓存配置(SET 2G USUP PACKBUF) 
#### 设置2G用户报文缓存配置(SET 2G USUP PACKBUF) 
命令功能 
该命令用于设置2G用户报文寻呼缓存配置。当需要设置每PDP上下文寻呼缓存下行数据包最大个数时，使用该命令，设置成功后，新接入的2G用户在寻呼过程中，每个PDP最大可以缓存的下行数据包个数将采用本配置的值。 
寻呼缓存指的是用户在寻呼过程中可以对此时下行的数据报文进行一定数量的缓存，当寻呼成功后再将缓存的报文下发给用户，保证了业务的连续性。 
注意事项 
 
每个用户面模块寻呼缓存报文数的总量有最大值限制，参见命令SHOW CAPACITY。单个用户面模块的所有PDP上下文缓存的报文个数相加，如果大于总量，则后续寻呼过程中的数据报文将无法缓存，只有等寻呼应答或超时后，对缓存进行释放才可以继续缓存。
 
 
每个用户面模块寻呼缓存报文数的总量一般采用默认值，若无特殊需求，无需修改。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
USRPACKBUF|每PDP缓存最大下行报文数|参数可选性:必选参数；参数类型:整数；参数范围为:0~70。|该参数用来设定寻呼缓存每PDP上下文能够缓存报文最大数量。若实际缓存报文数超过该配置值，则后续寻呼过程中的数据报文将无法缓存，只有等寻呼应答或超时后，对缓存进行释放才可以继续缓存。
命令举例 
设置2G用户报文缓存配置，每PDP缓存最大下行报文数为0，即不缓存。
SET 2G USUP PACKBUF:USRPACKBUF=0; 
父主题： [2G USUP报文缓存配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询2G用户报文缓存配置(SHOW 2G USUP PACKBUF) 
#### 查询2G用户报文缓存配置(SHOW 2G USUP PACKBUF) 
命令功能 
该命令用于查询2G用户报文寻呼缓存配置。 
寻呼缓存作用是，在对用户寻呼过程中可以对此时下行的数据报文进行一定数量的缓存，当寻呼成功后再将缓存的报文下发给用户，保证了业务的连续性。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
USRPACKBUF|每PDP缓存最大下行报文数|参数可选性:任选参数；参数类型:整数；参数范围为:0~70。|该参数用来设定寻呼缓存每PDP上下文能够缓存报文最大数量。若实际缓存报文数超过该配置值，则后续寻呼过程中的数据报文将无法缓存，只有等寻呼应答或超时后，对缓存进行释放才可以继续缓存。
命令举例 
查询2G用户报文缓存配置。
SHOW 2G USUP PACKBUF; 
`
命令 (No.1): SHOW 2G USUP PACKBUF
操作维护  每PDP缓存最大下行报文数
---------------------------------
修改      5
---------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [2G USUP报文缓存配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### SNDCP重组配置 
### SNDCP重组配置 
背景知识 
SGSN和BSS之间通过Gb接口互通。 
Gb接口协议分为用户面和控制面两部分，用户面的协议栈由SNDCP（Subnetwork Dependant Convergence Protocol）、LLC（Logical Link Control）、BSSGP（Base Station Subsystem GPRS Protocol）、NS（Network Service）、L1组成。 
在用户平面中，SNDCP，LLC，BSSGP，NS互相配合，将GTP-U发送来的N-PDU（Network Packet Data Unit）传送到BSS/MS或将BSS/MS来的数据送到GTP-U。 
SNDCP层主要功能包括： 
 
不同协议的复用。
 
 
用户数据的压缩和解压缩。
 
 
协议控制信息（如TCP/IP头）的压缩和解压缩。
 
 
分段和重组。
 
 
SNDCP流程包括N-PDU缓冲、传输顺序管理、TCP/IP报头压缩、数据压缩、分片与重组、XID参数协商等流程。 
 
N-PDU缓冲
在N-PDU压缩、分片、传送到LLC协议层之前需要对其进行缓冲处理。
 
 
传输顺序管理
SNDCP协议保留在对端实体之间每个网络服务接入点标识的传输顺序管理。
 
 
TCP/IP报头压缩
TCP/IP报头压缩减小了无线接口上传输消息的大小，从而增加Gb接口的吞吐量。
 
 
数据压缩
整个N-PDU可以进行数据压缩，从而减少传输需要的无线资源，增加Gb接口的吞吐量。
 
 
分片与重组
分片流程由SNDCP实体执行，用于保证传输的N-PDU不超过最大长度。
重组流程即收集报文分片的过程，并将所有分片组装成同原报文完全一致的报文。
 
 
XID参数协商
对端SNDCP之间的XID参数协商流程用于保证最佳信息传递（数据压缩）。MS和SGSN都可以触发该流程。
 
 
功能描述 
“SNDCP重组配置”用于设置2G USUP模块对于2G上行用户面数据进行SNDCP重组时的缓存个数和重组超时时长。 
 
重组缓存个数多，则重组性能较好，但内存开销增大。
 
 
重组超时时长小，则缓存占用少，但对各个分片之间延迟要求就小，重组失败概率大。
 
 
本配置项有默认值，默认值经过测试和商用验证，不建议修改。 
相关主题 
 
设置SNDCP重组配置(SET SNDCP REASSEMBLE)
 
 
查询SNDCP重组配置(SHOW SNDCP REASSEMBLE)
 
 
父主题： [USUP报文缓存配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置SNDCP重组配置(SET SNDCP REASSEMBLE) 
#### 设置SNDCP重组配置(SET SNDCP REASSEMBLE) 
命令功能 
该命令用于修改SGSN网元中SNDCP（SubNetwork Dependent Convergence Protocol，子网会聚协议）重组功能的相关配置。对于Gb口数据报文，当需要修改单个用户面模块支持的最大缓存报文总数、分片报文的重组超时时长的时候，使用该命令。修改成功后，SNDCP分片重组将按照新配置的策略进行重组。
注意事项 
 
该命令采用系统默认配置，若无特殊要求，无需修改。
 
 
执行修改后，需重启SGSN服务器。
 
 
当Gb口SNDCP分片比例增多或网络传输速度低，重组分片等待的时间相应增加时，可以适当调整“SNDCP重组最大缓存数”和“SNDCP重组超时时间”为较大值。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
BUFFERNUM|SNDCP重组最大缓存个数|参数可选性:任选参数；参数类型:整数；参数范围为:3000~10000。|每用户面模块SNDCP重组最大缓存个数，取值越大容纳分片个数越多，即重组能力越强。当网络上报文延时较大时，建议使用较大值。
TIMEOUT|SNDCP重组超时时间(毫秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1000~6000。|SNDCP重组超时时间，时间越长则等待分片而重组失败的时间越长。当网络上报文延时较大时，建议使用较大值。
命令举例 
修改SNDCP重组配置，SNDCP重组最大缓存个数为4000，SNDCP重组超时时间（毫秒）为3000。 
SET SNDCP REASSEMBLE:BUFFERNUM=4000,TIMEOUT=3000; 
父主题： [SNDCP重组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询SNDCP重组配置(SHOW SNDCP REASSEMBLE) 
#### 查询SNDCP重组配置(SHOW SNDCP REASSEMBLE) 
命令功能 
该命令用于查询SNDCP重组功能的相关配置。对于Gb口数据报文，SNDCP分片需要重组，重组过程中需要对已接收的分片进行缓存，对缓存一定时长的报文则认为重组失败从而释放缓存。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
BUFFERNUM|SNDCP重组最大缓存个数|参数可选性:任选参数；参数类型:整数。|每用户面模块SNDCP重组最大缓存个数，取值越大容纳分片个数越多，即重组能力越强。当网络上报文延时较大时，建议使用较大值。
TIMEOUT|SNDCP重组超时时间(毫秒)|参数可选性:任选参数；参数类型:整数。|SNDCP重组超时时间，时间越长则等待分片而重组失败的时间越长。当网络上报文延时较大时，建议使用较大值。
命令举例 
查询SNDCP重组配置。 
SHOW SNDCP REASSEMBLE; 
`
命令 (No.1): SHOW SNDCP REASSEMBLE;
操作维护  SNDCP重组最大缓存个数   SNDCP重组超时时间(毫秒)
---------------------------------------------------------
修改      5000                    3000
---------------------------------------------------------
记录数 1
命令执行成功（耗时 0.085 秒）。
` 
父主题： [SNDCP重组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## TCP MSS协商配置 
## TCP MSS协商配置 
背景知识 
MSS: Maximum Segment Size 最大分段大小，是TCP协议里面的一个概念。 
为了达到最佳的传输效能，TCP协议在建立连接的时候通常要协商双方的MSS值，这个值TCP协议在实现的时候往往用MTU值代替（需要减去IP数据包包头的大小20Bytes和TCP数据段的包头20Bytes）所以一般MSS值为1460。 
TCP采用 SYN和SYN ACK报文来进行client和server段进行协商，包括采用MSS option来协商TCP层最大segment长度。 
通讯双方会根据双方提供的MSS值得最小值确定为这次连接的最大MSS值。 
TCP MSS相关描述请参见RFC879协议。 
分片报文会增加系统负担，而用户报文在传输时，需要封装在GTPU隧道中传递，GTPU隧道本身会为报文增加40个字节，导致原来不需分片的也可能进行分片。为了减少用户报文分片的概率，需要对用户的TCP报文（GTPU隧道中传递的报文），进行MSS字段修正，一般修正为1412（去掉GTPU V0头的长度48个字节）。 
功能描述 
TCP MSS修改功能，即是SGSN在传输用户TCP SYN报文时，如果发现用户传送的MSS值大于配置的MSS值时，将其修改为配置的MSS值。 
相关主题 
 
设置TCP MSS协商配置(SET TCP MSS)
 
 
查询TCP MSS协商配置(SHOW TCP MSS)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置TCP MSS协商配置(SET TCP MSS) 
### 设置TCP MSS协商配置(SET TCP MSS) 
命令功能 
该命令用于设置TCP MSS协商配置。当需要对用户TCP SYN报文携带的TCP MSS字段进行协商修改时，使用该命令。配置成功后，SGSN将对用户TCP SYN报文中的TCP MSS进行协商，从而限定后续用户TCP数据报文的长度，减少分片重组对系统的影响，提高传输效率或减少GTP承载封装引起的分片，从而提高系统的传输性能。
注意事项 
 
该功能默认启用，且该命令采用系统默认配置，若无特殊要求，无需修改。
 
 
如果TCP SYN报文首部不含TCP MSS选项则SGSN不参与协商修改。
 
 
如果配置TCP MSS较小，可能会引起网络中报文数增多，对系统吞吐量有一定影响。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
TCPMSS|最大IPv4报文段长度(字节)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1420。|IPv4报文TCP报文段长度，以字节数为单位，该长度不包括TCP首部长度。
IPV6TCPMSS|最大IPv6报文段长度(字节)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1400。|IPv6报文TCP报文段长度，以字节数为单位，该长度不包括TCP首部长度。
命令举例 
设置TCP MSS协商配置，最大IPv6报文TCP报文段长度（字节）为1000。
SET TCP MSS:IPV6TCPMSS=1000; 
父主题： [TCP MSS协商配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询TCP MSS协商配置(SHOW TCP MSS) 
### 查询TCP MSS协商配置(SHOW TCP MSS) 
命令功能 
该命令用于查询TCP MSS协商配置。 
TCP MSS协商的作用是通过TCP建链时的协商，保证后续TCP报文段长度不大于协商的长度，这样使IP报文可以按设置的长度在网络中进行传输，提高传输效率或减少GTP承载封装引起的分片，从而提高系统的传输性能。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TCPMSS|最大IPv4报文段长度(字节)|参数可选性:任选参数；参数类型:整数。|IPv4报文TCP报文段长度，以字节数为单位，该长度不包括TCP首部长度。
IPV6TCPMSS|最大IPv6报文段长度(字节)|参数可选性:任选参数；参数类型:整数。|IPv6报文TCP报文段长度，以字节数为单位，该长度不包括TCP首部长度。
命令举例 
查询TCP MSS协商配置。
SHOW TCP MSS; 
`
命令 (No.1): SHOW TCP MSS
操作维护  最大IPv4报文段长度(字节)   最大IPv6报文段长度(字节)
-------------------------------------------------------------
修改      1200                       1000
-------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.088 秒）。
` 
父主题： [TCP MSS协商配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 跟踪管理配置 
## 跟踪管理配置 
背景知识 
本功能是用于SGSN网元的用户面报文的跟踪功能。包含单用户跟踪功能和丢包跟踪功能。 
功能描述 
单用户跟踪功能即是在SGSN上跟踪指定用户当前传输的该用户的所有报文，并使用ZTE自定义格式发送到指定跟踪服务器上进行存储和解析。不同于信令中的数据跟踪，本功能跟踪的报文不可以在网管界面上直接呈现。本功能最多支持5个用户同时跟踪。 
丢包跟踪功能则能将SGSN由于各种异常导致的丢弃的报文进行跟踪，同单用户跟踪功能一样，使用自定义格式发送到指定服务器上进行存储和解析。 
相关主题 
 
跟踪服务器配置
 
 
丢包跟踪配置
 
 
单用户跟踪配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 跟踪服务器配置 
### 跟踪服务器配置 
背景知识 
跟踪服务器是在单用户跟踪功能和丢包跟踪功能中使用到的报文存储和解析用的服务器。 
功能描述 
配置跟踪服务器的IP地址（只能IPV4）和VRF。 
相关主题 
 
设置跟踪服务器配置(SET TRACE SERVER)
 
 
查询跟踪服务器配置(SHOW TRACE SERVER)
 
 
父主题： [跟踪管理配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置跟踪服务器配置(SET TRACE SERVER) 
#### 设置跟踪服务器配置(SET TRACE SERVER) 
命令功能 
该命令用于设置单用户跟踪或丢包跟踪时报文存储及解析的服务器相关信息。当需要设置跟踪服务器的IP地址和VRF信息时，使用该命令。跟踪服务器配置成功后，被跟踪的用户报文将发往该服务器。 
单用户跟踪、丢包跟踪功能用于定位用户面报文传输相关的问题，可以跟踪指定用户的所有数据报文，或所有用户在转发过程中被丢弃的数据报文，无需在交换机上进行镜像抓包。 
注意事项 
需要确保SGSN网元与所配置的服务器地址（包括VRF）对应的链路正常（即路由是通的）。VRF相关信息可以在Rosng配置管理中查看，命令如下：show running-config 
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|跟踪服务器地址|参数可选性:任选参数；参数类型:地址|该参数用于设置跟踪服务器IP地址。可以选择一台与SGSN网元路由相同的PC机作为跟踪服务器。包括IPv4或者IPv6地址。
VRF|VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于指定SGSN到跟踪服务器路由所归属的VRF的标识。VRF相关信息可以在Rosng配置管理中查看，命令如下：show running-config
命令举例 
该命令用于设置跟踪服务器IP地址为20.1.10.1，VRF标识为100。
SET TRACE SERVER:IPADDR="20.1.10.1",VRF=100; 
父主题： [跟踪服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询跟踪服务器配置(SHOW TRACE SERVER) 
#### 查询跟踪服务器配置(SHOW TRACE SERVER) 
命令功能 
该命令用于查询配置的跟踪服务器IP地址和VRF信息。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|跟踪服务器地址|参数可选性:任选参数；参数类型:地址|该参数用于设置跟踪服务器IP地址。可以选择一台与SGSN网元路由相同的PC机作为跟踪服务器。包括IPv4或者IPv6地址。
VRF|VRF标识|参数可选性:任选参数；参数类型:整数。|该参数用于指定SGSN到跟踪服务器路由所归属的VRF的标识。VRF相关信息可以在Rosng配置管理中查看，命令如下：show running-config
命令举例 
该命令用于查询跟踪服务器IP地址及VRF配置。
SHOW TRACE SERVER; 
`
命令 (No.1): SHOW TRACE SERVER
操作维护  跟踪服务器地址   VRF标识
----------------------------------
修改      20.1.10.1        100
----------------------------------
记录数 1
命令执行成功（耗时 0.056 秒）。
` 
父主题： [跟踪服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 丢包跟踪配置 
### 丢包跟踪配置 
背景知识 
丢包跟踪功能则能将SGSN由于各种异常导致的丢弃的报文进行跟踪，同单用户跟踪功能一样，使用自定义格式发送到指定服务器上进行存储和解析。 
功能描述 
可以配置开启或关闭丢包跟踪功能。 
                配置本功能时，必须配置对应的跟踪服务器，跟踪服务器配置命令为：
                [SET TRACE SERVER]
相关主题 
 
设置丢包跟踪配置(SET DROP PACKET TRACE)
 
 
查询丢包跟踪配置(SHOW DROP PACKET TRACE)
 
 
父主题： [跟踪管理配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置丢包跟踪配置(SET DROP PACKET TRACE) 
#### 设置丢包跟踪配置(SET DROP PACKET TRACE) 
命令功能 
该命令用于设置是否开启丢包跟踪功能。当需要开启或关闭丢包跟踪功能时，使用该命令。设置开启跟踪后，SGSN将对所有用户由于各种异常导致丢弃的用户报文进行跟踪，发送到跟踪服务器上进行存储和解析。
注意事项 
 
该配置项不区分用户，即对所有用户生效。
 
 
需要先进行跟踪服务器配置，才能对用户报文进行解析，配置命令参见SET TRACE SERVER。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
SPRT|是否开启丢包跟踪|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否开启丢包跟踪。取值含义：不开启：关闭丢包跟踪。开启：开启丢包跟踪。在需要对SGSN网元由于各种异常导致丢弃的用户数据报文进行跟踪分析时，开启丢包跟踪，默认情况下关闭丢包跟踪。
命令举例 
该命令用于设置为开启丢包跟踪。
SET DROP PACKET TRACE:SPRT="YES"; 
父主题： [丢包跟踪配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询丢包跟踪配置(SHOW DROP PACKET TRACE) 
#### 查询丢包跟踪配置(SHOW DROP PACKET TRACE) 
命令功能 
该命令用于查询当前丢包跟踪配置。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SPRT|是否开启丢包跟踪|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否开启丢包跟踪。取值含义：不开启：关闭丢包跟踪。开启：开启丢包跟踪。在需要对SGSN网元由于各种异常导致丢弃的用户数据报文进行跟踪分析时，开启丢包跟踪，默认情况下关闭丢包跟踪。
命令举例 
该命令用于查询丢包跟踪配置。
SHOW DROP PACKET TRACE; 
`
命令 (No.1): SHOW DROP PACKET TRACE;
操作维护  是否开启丢包跟踪
--------------------------
修改      开启
--------------------------
记录数 1
命令执行成功（耗时 0.081 秒）。
` 
父主题： [丢包跟踪配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 单用户跟踪配置 
### 单用户跟踪配置 
背景知识 
单用户跟踪功能即是在SGSN上跟踪指定用户当前传输的该用户的所有报文，并使用ZTE自定义格式发送到指定跟踪服务器上进行存储和解析。不同于信令中的数据跟踪，本功能跟踪的报文不可以在网管界面上直接呈现。本功能最多支持5个用户同时跟踪。 
功能描述 
配置跟踪的用户的IMSI号码，不支持按IMSI号段匹配。可以指定用户进行跟踪或不进行跟踪。 
                配置本功能时，必须配置对应的跟踪服务器，跟踪服务器配置命令为：
                [SET TRACE SERVER]
相关主题 
 
新增单用户跟踪配置(ADD SINGLE USER TRACE)
 
 
修改单用户跟踪配置(SET SINGLE USER TRACE)
 
 
删除单用户跟踪配置(DEL SINGLE USER TRACE)
 
 
查询单用户跟踪配置(SHOW SINGLE USER TRACE)
 
 
父主题： [跟踪管理配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增单用户跟踪配置(ADD SINGLE USER TRACE) 
#### 新增单用户跟踪配置(ADD SINGLE USER TRACE) 
命令功能 
该命令用于增加需要进行单用户跟踪的用户信息，并设置是否开启跟踪。当需要新增一个IMSI对应的用户进行单用户跟踪时，使用该命令。新增单用户跟踪，并设置开启跟踪后，可以跟踪指定用户当前传输的所有用户数据报文，发送到跟踪服务器上存储和解析。
注意事项 
 
该配置项最多支持同时存在5条记录。
 
 
需要先进行跟踪服务器配置，才能对用户报文进行解析，配置命令参见 SET TRACE SERVER。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指定用户对应的IMSI。
TRCFLG|是否开启跟踪|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于配置IMSI对应用户是否开启单用户跟踪。取值含义：不开启：关闭单用户跟踪。开启：开启单用户跟踪。在需要对某用户当前传输的所有报文进行跟踪分析时，可以开启单用户跟踪，默认情况下关闭单用户跟踪。
命令举例 
该命令用于新增单用户跟踪配置，IMSI为460090000000002，开启跟踪。
ADD SINGLE USER TRACE:IMSI="460090000000002",TRCFLG="YES"; 
父主题： [单用户跟踪配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改单用户跟踪配置(SET SINGLE USER TRACE) 
#### 修改单用户跟踪配置(SET SINGLE USER TRACE) 
命令功能 
该命令用于修改指定IMSI对应用户的单用户跟踪配置。当需要开启或关闭用户对应的单用户跟踪功能时，使用该命令。开启跟踪后，可以跟踪该用户当前传输的所有用户数据报文，发送到跟踪服务器上存储和解析。关闭跟踪后，该用户当前传输的报文将不再被跟踪。
注意事项 
指定IMSI对应的用户需要已经设置为单用户跟踪。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指定用户对应的IMSI。
TRCFLG|是否开启跟踪|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置IMSI对应用户是否开启单用户跟踪。取值含义：不开启：关闭单用户跟踪。开启：开启单用户跟踪。在需要对某用户当前传输的所有报文进行跟踪分析时，可以开启单用户跟踪，默认情况下关闭单用户跟踪。
命令举例 
该命令用于修改IMSI为460090000000002的用户，不进行跟踪。
SET SINGLE USER TRACE:IMSI="460090000000002",TRCFLG="NO"; 
父主题： [单用户跟踪配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除单用户跟踪配置(DEL SINGLE USER TRACE) 
#### 删除单用户跟踪配置(DEL SINGLE USER TRACE) 
命令功能 
该命令用于删除指定IMSI对应用户的单用户跟踪配置。当需要删除对应用户的单用户跟踪功能配置时，使用该命令。
注意事项 
指定IMSI对应的用户需要已经设置为单用户跟踪。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指定用户对应的IMSI。
命令举例 
该命令用于删除IMSI改为460090000000002的单用户跟踪配置。
DEL SINGLE USER TRACE:IMSI="460090000000002"; 
父主题： [单用户跟踪配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询单用户跟踪配置(SHOW SINGLE USER TRACE) 
#### 查询单用户跟踪配置(SHOW SINGLE USER TRACE) 
命令功能 
该命令用于查询当前配置的所有单用户跟踪配置信息，或查询指定IMSI的单用户跟踪配置信息。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于指定用户对应的IMSI。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于指定用户对应的IMSI。
TRCFLG|是否开启跟踪|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置IMSI对应用户是否开启单用户跟踪。取值含义：不开启：关闭单用户跟踪。开启：开启单用户跟踪。在需要对某用户当前传输的所有报文进行跟踪分析时，可以开启单用户跟踪，默认情况下关闭单用户跟踪。
命令举例 
该命令用于查询当前配置的单用户跟踪配置信息。
SHOW SINGLE USER TRACE; 
`
命令 (No.1): SHOW SINGLE USER TRACE
操作维护         IMSI              是否开启跟踪
-----------------------------------------------
复制 修改 删除   460090000000002   开启
-----------------------------------------------
记录数 1
命令执行成功（耗时 0.051 秒）。
` 
父主题： [单用户跟踪配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## SGSN黑名单配置 
## SGSN黑名单配置 
背景知识 
局间RAU（路由区位置更新）过程中，UE新注册的New SGSN需要向UE上一次注册的Old SGSN请求该用户的移动性管理上下文和PDP上下文。New SGSN给OldSGSN发送SGSN Context Request（SGSN上下文请求）消息，Old SGSN给New SGSN返回SGSN Context Response（SGSN上下文响应）消息，消息中携带移动性管理上下文和PDP上下文，New SGSN再给Old SGSN返回SGSN Context Acknowledge（SGSN上下文确认）消息。RAU流程的具体细节可以参考3GPP TS 23.060 6.9.1.2.2章节。 
局间RAU过程中，由于对端SGSN的实现缺陷、支持的协议版本不同或其他原因，对端SGSN没有按协议响应SGSN Context Response消息或不能正常处理SGSN Context Response消息中的PDP上下文信息，导致局间RAU失败。 
对这些不能按协议处理局间RAU的SGSN，设置为SGSN黑名单，本端SGSN通过控制和黑名单中的SGSN的局间RAU流程，提高局间RAU的成功率。 
功能描述 
通过SGSN黑名单配置，把不能按协议处理局间RAU的对端SGSN设置在SGSN黑名单里。SGSN和黑名单中的SGSN进行局间RAU流程时，控制是否向Old SGSN发送SGSN Context Request消息，控制Old SGSN在收到SGSN Context Request消息后，是否返回SGSN Context Response消息及在返回SGSN Context Response消息时是否携带PDP上下文信息。 
                配置SGSN黑名单的配置命令为：
                [ADD SGSN BLACKLIST]
                。
            
相关主题 
 
新增SGSN黑名单配置(ADD SGSN BLACKLIST)
 
 
修改SGSN黑名单配置(SET SGSN BLACKLIST)
 
 
删除SGSN黑名单配置(DEL SGSN BLACKLIST)
 
 
查询SGSN黑名单配置(SHOW SGSN BLACKLIST)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增SGSN黑名单配置(ADD SGSN BLACKLIST) 
### 新增SGSN黑名单配置(ADD SGSN BLACKLIST) 
命令功能 
该命令用于配置一个黑名单列表，将一些不按3GPP协议规范处理SGSN局间RAU（Routing Area Update，路由区位置更新）流程的对端SGSN网元的IP地址设置在此黑名单中。 
UE发生局间RAU流程时，如果New SGSN（目标SGSN）与Old SGSN（源SGSN）分别是我司与其他厂商的SGSN，由于局间RAU流程发生在两个不同厂商的SGSN网元，消息中的参数差异可能导致局间RAU流程发生失败，为了避免此种情况 ，通过该命令，对RAU流程中的信令交互进行修正，以提高局间RAU的成功率，具体处理情况如下： 
当本局SGSN做为局间RAU的New SGSN时，本局SGSN向Old SGSN发送SGSN Context Request消息，Old SGSN处理SGSN Context Request消息失败，导致局间RAU流程发生失败，通过本命令配置“New SGSN策略控制”为“不发送SGSN Context Request请求”，可以保证RAU成功。 
当本局SGSN做为局间RAU的Old SGSN，本局SGSN收到New SGSN发送的SGSN Context Request消息后，向New SGSN发送SGSN  Context Response消息，此响应消息中携带PDP上下文，如果New SGSN不能处理相关的PDP上下文，导致局间RAU流程发生失败，通过本命令配置“Old SGSN策略控制“为“SGSN  Context Response响应不携带PDP上下文”，可以保证RAU成功。 
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN IP地址|参数可选性:必选参数；参数类型:地址|与本SGSN网元对接的其它SGSN网元的控制面IP地址，包括IPv4或者IPv6地址。对端SGSN网元的IP地址可通过两种方式获取：该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
NEWSGSNCTRL|New SGSN策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NOSEND。|该参数用于在UE发生局间RAU过程中，本SGSN网元作为目标 SGSN的策略控制。取值含义：设置为“不限制（NONE）”时：表示当UE发生局间RAU时，本SGSN网元向源SGSN发送SGSN Context Request消息。 设置为“不发送SGSN Context Request请求（NOSEND）”时：表示当UE发生局间RAU时，本SGSN不向源SGSN发送SGSN Context Request消息。
OLDSGSNCTRL|Old SGSN策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NONE。|该参数用于UE发生局间RAU过程中，本SGSN网元作为源SGSN的策略控制。 取值含义：设置为“不限制（NONE）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，会发送SGSN Context Response消息给目标SGSN，且此响应消息中携带PDP上下文。 设置为“SGSN  Context Response响应不携带PDP上下文（NOPDP）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，会发送SGSN  Context Response消息给目标SGSN，此响应消息中不携带PDP上下文。设置为“不返回SGSN  Context Response消息（NOSEND）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，不会发送SGSN  Context Response消息给目标SGSN。
命令举例 
新增SGSN黑名单配置，SGSN IP地址为10.44.10.1，目标SGSN策略控制为不限制，源 SGSN策略控制为不限制。
ADD SGSN BLACKLIST:SGSNIP="10.44.10.1",NEWSGSNCTRL="NONE",OLDSGSNCTRL="NONE"; 
父主题： [SGSN黑名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改SGSN黑名单配置(SET SGSN BLACKLIST) 
### 修改SGSN黑名单配置(SET SGSN BLACKLIST) 
命令功能 
该命令用于修改本局SGSN与黑名单列表中的SGSN进行局间RAU流程时的处理策略。
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN IP地址|参数可选性:必选参数；参数类型:地址|与本SGSN网元对接的其它SGSN网元的控制面IP地址，包括IPv4或者IPv6地址。对端SGSN网元的IP地址可通过两种方式获取：该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
NEWSGSNCTRL|New SGSN策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于在UE发生局间RAU过程中，本SGSN网元作为目标 SGSN的策略控制。取值含义：设置为“不限制（NONE）”时：表示当UE发生局间RAU时，本SGSN网元向源SGSN发送SGSN Context Request消息。 设置为“不发送SGSN Context Request请求（NOSEND）”时：表示当UE发生局间RAU时，本SGSN不向源SGSN发送SGSN Context Request消息。
OLDSGSNCTRL|Old SGSN策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于UE发生局间RAU过程中，本SGSN网元作为源SGSN的策略控制。 取值含义：设置为“不限制（NONE）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，会发送SGSN Context Response消息给目标SGSN，且此响应消息中携带PDP上下文。 设置为“SGSN  Context Response响应不携带PDP上下文（NOPDP）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，会发送SGSN  Context Response消息给目标SGSN，此响应消息中不携带PDP上下文。设置为“不返回SGSN  Context Response消息（NOSEND）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，不会发送SGSN  Context Response消息给目标SGSN。
命令举例 
修改SGSN IP地址为10.44.10.1SGSN黑名单配置，目标SGSN策略控制改为不限制，源SGSN策略控制改为不限制。
SET SGSN BLACKLIST:SGSNIP="10.44.10.1",NEWSGSNCTRL="NONE",OLDSGSNCTRL="NONE"; 
父主题： [SGSN黑名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除SGSN黑名单配置(DEL SGSN BLACKLIST) 
### 删除SGSN黑名单配置(DEL SGSN BLACKLIST) 
命令功能 
该命令用于删除SGSN黑名单配置。
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN IP地址|参数可选性:必选参数；参数类型:地址|与本SGSN网元对接的其它SGSN网元的控制面IP地址，包括IPv4或者IPv6地址。对端SGSN网元的IP地址可通过两种方式获取：该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
命令举例 
删除SGSN IP地址为10.44.10.1SGSN黑名单配置。
DEL SGSN BLACKLIST:SGSNIP="10.44.10.1"; 
父主题： [SGSN黑名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询SGSN黑名单配置(SHOW SGSN BLACKLIST) 
### 查询SGSN黑名单配置(SHOW SGSN BLACKLIST) 
命令功能 
当不输入”SGSN IP地址“时，表示查询系统中配置的所有SGSN黑名单配置信息。
 
 
当输入”SGSN IP地址“时，表示查询本SGSN网元与此SGSN网元相关的黑名单配置信息。
 
 
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN IP地址|参数可选性:任选参数；参数类型:地址|与本SGSN网元对接的其它SGSN网元的控制面IP地址，包括IPv4或者IPv6地址。对端SGSN网元的IP地址可通过两种方式获取：该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN IP地址|参数可选性:任选参数；参数类型:字符型。|与本SGSN网元对接的其它SGSN网元的控制面IP地址，包括IPv4或者IPv6地址。对端SGSN网元的IP地址可通过两种方式获取：该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
NEWSGSNCTRL|New SGSN策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于在UE发生局间RAU过程中，本SGSN网元作为目标 SGSN的策略控制。取值含义：设置为“不限制（NONE）”时：表示当UE发生局间RAU时，本SGSN网元向源SGSN发送SGSN Context Request消息。 设置为“不发送SGSN Context Request请求（NOSEND）”时：表示当UE发生局间RAU时，本SGSN不向源SGSN发送SGSN Context Request消息。
OLDSGSNCTRL|Old SGSN策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于UE发生局间RAU过程中，本SGSN网元作为源SGSN的策略控制。 取值含义：设置为“不限制（NONE）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，会发送SGSN Context Response消息给目标SGSN，且此响应消息中携带PDP上下文。 设置为“SGSN  Context Response响应不携带PDP上下文（NOPDP）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，会发送SGSN  Context Response消息给目标SGSN，此响应消息中不携带PDP上下文。设置为“不返回SGSN  Context Response消息（NOSEND）”：表示当UE发生局间RAU时，本SGSN收到目标SGSN的SGSN Context Request消息后，不会发送SGSN  Context Response消息给目标SGSN。
命令举例 
查询SGSN黑名单配置。
SHOW SGSN BLACKLIST; 
`
命令 (No.1): SHOW SGSN BLACKLIST
操作维护   SGSN IP地址 New SGSN策略控制  Old SGSN策略控制 
---------------------------------------------------------------------------
复制 修改  131.1.3.159   不限制                     不限制 
---------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.189 秒）。
` 
父主题： [SGSN黑名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## Pool内SGSN重选配置 
## Pool内SGSN重选配置 
背景知识 
SGSN POOL组网下，某些特定厂商的SGSN作为源SGSN时，收到局间的GTP请求消息不回响应；需要目的SGSN将消息发送到POOL内的其他 SGSN，再由该SGSN转发至源SGSN； 
“POOL内SGSN地址重选功能”启用后，目标SGSN在特定的源SGSN不回响应消息的情况下，选择POOL内其他源SGSN重新发送局间的GTP请求消息。 
功能描述 
“POOL内SGSN重选配置”中配置的SGSN的GTP地址，用来检查该目的SGSN是否需要启用重选功能； 
当目标SGSN在发送消息时，查询到多个源SGSN地址，则判断前两个地址是否在在配置的上述地址列表中。如果在，则在向第一个地址发送请求消息无响应后，向第二个地址发起重试。 
相关主题 
 
新增Pool内SGSN重选配置(ADD RESEL SGSN ADDR)
 
 
删除Pool内SGSN重选配置(DEL RESEL SGSN ADDR)
 
 
查询Pool内SGSN重选配置(SHOW RESEL SGSN ADDR)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增Pool内SGSN重选配置(ADD RESEL SGSN ADDR) 
### 新增Pool内SGSN重选配置(ADD RESEL SGSN ADDR) 
命令功能 
一组SGSN可以构成一个SGSN池，即SGSN Pool。SGSN Pool组网是指：允许接入网侧连接同一个运营商的多个CN（Core Network，核心网）节点。 
在SGSN Pool组网下，多个SGSN之间形成负荷分担，可以在某一SGSN发生故障时实现容灾。另外，当用户在SGSN Pool内的SGSN上分布不均衡时，还可以通过手工方式将部分用户从一个SGSN迁移到另一个SGSN上，从而实现对SGSN Pool内这些SGSN的维护而不影响用户业务。 
在SGSN POOL组网下，UE发生局间RAU（Routing Area Update，路由区更新）流程时，当目标SGSN（New SGSN）为本SGSN网元，源SGSN（Old SGSN）为其他厂商的SGSN时，由于消息中的参数差异，源SGSN收到本SGSN网元发送的GTP请求消息后，可能不回响应，导致局间RAU失败。 
为了避免产生此种情况，通过此命令配置多个源SGSN IP地址，本SGSN网元解析到两个或两个以上的源SGSN地址时，将这些IP地址与本命令配置的IP地址进行匹配，如果能够匹配到两个IP地址，表示SGSN支持启用SGSN POOL内重选功能，如果匹配不到，表示此功能不生效。 
本SGSN向其中一个IP地址发送GTP请求消息无响应后，可以向第二个IP地址发起重试，以提高局间RAU成功率。 
注意事项 
该命令只适用于SGSN网元。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN GTP地址|参数可选性:必选参数；参数类型:地址|表示对端SGSN网元的IP地址，包括IPv4或者IPv6地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
命令举例 
新增Pool内SGSN重选配置，SGSN GTP地址为10.44.10.1。
ADD RESEL SGSN ADDR:SGSNIP="10.44.10.1"; 
父主题： [Pool内SGSN重选配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除Pool内SGSN重选配置(DEL RESEL SGSN ADDR) 
### 删除Pool内SGSN重选配置(DEL RESEL SGSN ADDR) 
命令功能 
该命令用于删除Pool内SGSN重选配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN GTP地址|参数可选性:必选参数；参数类型:地址|表示对端SGSN网元的IP地址，包括IPv4或者IPv6地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
命令举例 
删除SGSN GTP地址为10.44.10.1的Pool内SGSN重选配置。
DEL RESEL SGSN ADDR:SGSNIP="10.44.10.1"; 
父主题： [Pool内SGSN重选配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询Pool内SGSN重选配置(SHOW RESEL SGSN ADDR) 
### 查询Pool内SGSN重选配置(SHOW RESEL SGSN ADDR) 
命令功能 
该命令用于查询Pool内SGSN重选配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN GTP地址|参数可选性:任选参数；参数类型:地址|表示对端SGSN网元的IP地址，包括IPv4或者IPv6地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNIP|SGSN GTP地址|参数可选性:任选参数；参数类型:字符型。|表示对端SGSN网元的IP地址，包括IPv4或者IPv6地址。该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得（SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
命令举例 
查询Pool内SGSN重选配置。
SHOW RESEL SGSN ADDR"; 
`
命令 (No.1): SHOW RESEL SGSN ADDR
SGSN GTP地址 
---------------
1.2.3.1 
2.2.2.2 
32.2.2.2 
---------------
记录数 3
命令执行成功（耗时 0.147 秒）。
` 
父主题： [Pool内SGSN重选配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## GTP链路告警过滤配置 
## GTP链路告警过滤配置 
背景知识 
            
            对于现网中大量出现的GTP链路告警，维护人员认为，只有需要关注的GSN断链才需要告警，不需要关注的GSN断链不需要告警，所有SGSN都告警的方式是不可取的。通过配置过滤，对关注的对端GSN节点上报告警，其他不关注的则不上报告警。
        
功能描述 
对GTP链路告警进行过滤，关注重要的GSN节点是否发生故障。 
配置GTP链路告警过滤的流程如下： 
                        启用GTP链路告警过滤。 配置命令为：
                        [SET GTP ALARM FLAG]
                        :GTPALMFLAG="YES";
                    
                        配置GTP链路告警过滤。 配置命令为：
                        [ADD GTP ALARM NODE]
相关主题 
 
设置GTP链路告警过滤开关(SET GTP ALARM FLAG)
 
 
查询GTP链路告警过滤开关(SHOW GTP ALARM FLAG)
 
 
新增GTP链路告警对端节点地址(ADD GTP ALARM NODE)
 
 
删除GTP链路告警对端节点地址(DEL GTP ALARM NODE)
 
 
查询GTP链路告警对端节点地址(SHOW GTP ALARM NODE)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置GTP链路告警过滤开关(SET GTP ALARM FLAG) 
### 设置GTP链路告警过滤开关(SET GTP ALARM FLAG) 
命令功能 
该命令用于设置当运营商只需要关注部分GTP链路（对端网元为SGSN/MME）的告警信息时，SGSN/MME是否能将运营商不关注的对端SGSN/MME网元产生的GTP链路告警信息进行屏蔽，不会在本地维护终端的告警管理界面中显示出来。
注意事项 
系统的默认配置为不对GTP链路告警（由对端SGSN/MME网元产生的）进行屏蔽，即表示所有的GTP链路告警信息，都会在本地维护终端的告警管理界面中显示 。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPALMFLAG|GTP链路告警过滤开关|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本SGSN/MME网元是否能将运营商不关注的对端SGSN/MME网元产生的GTP链路告警信息进行屏蔽，不会在本地维护终端的告警管理界面中显示出来。 取值含义：设置为“不支持（NO）”：表示所有的GTP链路告警信息，都会在本地维护终端的告警管理界面中显示 。设置为“支持（YES）”：表示只有系统配置的对端SGSN/MME网元产生的GTP链路的告警信息才会在本地维护终端的告警管理界面中显示 。
命令举例 
设置GTP链路告警过滤开关为开。
SET GTP ALARM FLAG:GTPALMFLAG="YES"; 
父主题： [GTP链路告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询GTP链路告警过滤开关(SHOW GTP ALARM FLAG) 
### 查询GTP链路告警过滤开关(SHOW GTP ALARM FLAG) 
命令功能 
该命令用于查询本SGSN/MME网元是否支持对GTP链路告警（由对端SGSN/MME网元产生的）进行屏蔽。
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GTPALMFLAG|GTP链路告警过滤开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本SGSN/MME网元是否能将运营商不关注的对端SGSN/MME网元产生的GTP链路告警信息进行屏蔽，不会在本地维护终端的告警管理界面中显示出来。 取值含义：设置为“不支持（NO）”：表示所有的GTP链路告警信息，都会在本地维护终端的告警管理界面中显示 。设置为“支持（YES）”：表示只有系统配置的对端SGSN/MME网元产生的GTP链路的告警信息才会在本地维护终端的告警管理界面中显示 。
命令举例 
查询GTP链路告警过滤开关。
SHOW GTP ALARM FLAG; 
`
命令 (No.1): SHOW GTP ALARM FLAG
操作维护 GTP链路告警过滤开关 
-----------------------------
修改        不支持 
-----------------------------
记录数 1
命令执行成功（耗时 0.04 秒）。
` 
父主题： [GTP链路告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增GTP链路告警对端节点地址(ADD GTP ALARM NODE) 
### 新增GTP链路告警对端节点地址(ADD GTP ALARM NODE) 
命令功能 
该命令用于新增对端SGSN/MME网元的IP地址。 
通过此命令设置的对端SGSN/MME网元产生的GTP链路告警，才会显示在本地维护终端告警管理界面中。 
注意事项 
在执行本操作之前，需要执行[SET GTP ALARM FLAG]命令。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端节点IP地址|参数可选性:必选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。本端网元为SGSN的情况下，该地址包括如下两种情况：如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW GPRS APN、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得。SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
命令举例 
新增GTP链路告警对端节点地址，对端节点IP地址为1.1.1.1。
ADD GTP ALARM NODE:IP="1.1.1.1"; 
父主题： [GTP链路告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除GTP链路告警对端节点地址(DEL GTP ALARM NODE) 
### 删除GTP链路告警对端节点地址(DEL GTP ALARM NODE) 
命令功能 
该命令用于删除对端SGSN/MME网元的IP地址。 
执行此命令后，被删除的对端SGSN/MME网元产生的GTP链路告警将不会显示在本SGSN/MME网元本地维护终端告警管理界面中。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端节点IP地址|参数可选性:必选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。本端网元为SGSN的情况下，该地址包括如下两种情况：如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW GPRS APN、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得。SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
命令举例 
删除GTP链路告警对端节点地址，对端节点IP地址为1.1.1.1。
DEL GTP ALARM NODE:IP="1.1.1.1"; 
父主题： [GTP链路告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询GTP链路告警对端节点地址(SHOW GTP ALARM NODE) 
### 查询GTP链路告警对端节点地址(SHOW GTP ALARM NODE) 
命令功能 
该命令用于查询对端SGSN/MME网元的IP地址列表。 
查询结果中显示的SGSN/MME网元的IP地址，在其产生GTP链路告警时，对应的告警消息会显示在本SGSN/MME网元本地维护终端告警管理界面中。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端节点IP地址|参数可选性:任选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。本端网元为SGSN的情况下，该地址包括如下两种情况：如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW GPRS APN、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得。SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IP|对端节点IP地址|参数可选性:任选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。本端网元为SGSN的情况下，该地址包括如下两种情况：如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW GPRS APN、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得。SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。
命令举例 
查询GTP链路告警对端节点地址，对端节点IP地址为1.1.1.1。
SHOW GTP ALARM NODE:IP="1.1.1.1"; 
`
命令 (No.1): SHOW GTP ALARM NODE:IP="1.1.1.1";
记录数 0
命令执行成功（耗时 0.054 秒）。
` 
父主题： [GTP链路告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## GTP节点管理保护配置 
## GTP节点管理保护配置 
背景知识 
GTP节点管理是指，对与本网元（SGSN/MME）存在GTP消息/数据报文交互的GTP节点进行管理（比如，邻接的GGSN、SGSN、MME、SGW等），维护对端节点信息。 
GTP节点管理保护是指，对端节点网元由于处理不当，可能会在返回的GTP消息（非ECHO消息）中携带错误的Recovery值，比如GGSN创建PDP上下文失败、SGW创建会话失败，由于GGSN/SGW一些内部负荷分担机制，可能会在失败响应消息中携带错误的Recovery值；从而导致本网元（SGSN/MME）判断Recovery值改变，触发与该GTP节点存在关联的那些用户下线；此类问题，在要求其他网元正确处理的同时，本网元也需要采取一定的保护手段来规避这样的问题。 
功能描述 
当与本网元（SGSN/MME）存在GTP消息/数据报文交互的对端节点网元处理不当，在返回的GTP消息（非ECHO消息）中携带错误的Recovery值时，SGSN/MME为了保证用户业务正常，在对端网元不升级的情况下，根据“GTP节点管理保护配置”，对配置的GTP节点管理保护地址对应路径上的GTP消息（非ECHO消息）的Recovery值不做判断，直接忽略，只检查ECHO消息中的Recovery值。 
GTP节点管理保护配置的流程如下： 
                        启用GTP节点管理保护。配置命令为：
                        [SET GTP PROTECT FLAG]
                        。
                    
                        配置GTP节点管理保护的对端节点地址。配置命令为：
                        [ADD GTP PROTECT IP]
                        。
                    
相关主题 
 
设置是否支持节点管理保护配置(SET GTP PROTECT FLAG)
 
 
查询是否支持节点管理保护配置(SHOW GTP PROTECT FLAG)
 
 
新增GTP节点管理保护配置(ADD GTP PROTECT IP)
 
 
删除GTP节点管理保护配置(DEL GTP PROTECT IP)
 
 
查询GTP节点管理保护配置(SHOW GTP PROTECT IP)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置是否支持节点管理保护配置(SET GTP PROTECT FLAG) 
### 设置是否支持节点管理保护配置(SET GTP PROTECT FLAG) 
命令功能 
该命令用于设置SGSN/MME是否支持GTP节点管理保护功能。 
当SGSN/MME与其它基于GTP协议的网元（比如邻接的GGSN、SGSN、MME、SGW等）进行交互时，其它网元由于处理不当，可能会在返回给SGSN/MME的GTP消息（非Echo消息）中携带错误的Recovery值，导致用户业务失败。 
SGSN/MME可以通过是否支持GTP节点管理保护功能来避免此类问题的产生，当SGSN/MME支持GTP节点管理保护功能时，对其它网元返回的GTP消息（非Echo消息）中的Recovery值不进行处理，直接忽略。 
注意事项 
本功能适用于SGSN和MME网元。 
系统的默认配置为不支持GTP节点管理保护功能。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPPROTECT|是否支持节点管理异常保护|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本SGSN/MME是否支持GTP节点管理保护功能。取值含义： 设置为“不支持（NO）”：表示本SGSN/MME对其它GTP网元返回的GTP消息（非Echo消息）中的Recovery值进行处理，如果该值错误，会导致用户下线。 设置为“支持（YES）”：表示本SGSN/MME对其它网元返回的GTP消息（非ECHO消息）中的Recovery值不进行处理，直接忽略，以保证用户可以正常使用业务。
命令举例 
设置不支持节点管理保护。
SET GTP PROTECT FLAG:GTPPROTECT="NO"; 
父主题： [GTP节点管理保护配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询是否支持节点管理保护配置(SHOW GTP PROTECT FLAG) 
### 查询是否支持节点管理保护配置(SHOW GTP PROTECT FLAG) 
命令功能 
该命令用于查询uMAC是否支持节点管理保护功能
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GTPPROTECT|是否支持节点管理异常保护|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本SGSN/MME是否支持GTP节点管理保护功能。取值含义： 设置为“不支持（NO）”：表示本SGSN/MME对其它GTP网元返回的GTP消息（非Echo消息）中的Recovery值进行处理，如果该值错误，会导致用户下线。 设置为“支持（YES）”：表示本SGSN/MME对其它网元返回的GTP消息（非ECHO消息）中的Recovery值不进行处理，直接忽略，以保证用户可以正常使用业务。
命令举例 
查询是否支持节点管理保护配置。
SHOW GTP PROTECT FLAG; 
`
命令 (No.1): SHOW GTP PROTECT FLAG
操作维护 是否支持节点管理异常保护 
----------------------------------
修改       支持 
----------------------------------
记录数 1
命令执行成功（耗时 0.057 秒）。
` 
父主题： [GTP节点管理保护配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增GTP节点管理保护配置(ADD GTP PROTECT IP) 
### 新增GTP节点管理保护配置(ADD GTP PROTECT IP) 
命令功能 
该命令用于在SGSN/MME支持GTP节点管理保护功能的情况下，设置对端GTP网元的IP地址。 
通过此命令设置的对端GTP网元，在本SGSN/MME网元与其进行交互时，如果对端GTP网元发送给本SGSN/MME网元的GTP消息（非Echo消息）中携带错误的Recovery值，本SGSN/MME网元对此不进行处理，直接忽略，以避免导致用户下线，影响用户业务使用。 
注意事项 
在执行本命令前，需要执行[SET GTP PROTECT FLAG]命令。
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GTP节点地址|参数可选性:必选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。本端网元为SGSN的情况下，该地址包括如下两种情况：如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW GPRS APN、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得。SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。本端网元为MME的情况下，该地址包括如下两种情况：如果对端网元为SGW/PGW，该参数的取值可通过SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW EPC APN命令查询的是通过本地数据解析的SGW/PGW IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGW/PGW IP地址）。如果对端网元为MME，该参数的取值可通过SHOW EPCHOST或DNS LOOKUP命令的查询结果获得。SHOW EPCHOST命令查询的是通过本地数据解析的MME IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的MME IP地址）。
命令举例 
新增GTP节点管理保护，GTP节点地址为192.168.0.1。
ADD GTP PROTECT IP:IPADDR="192.168.0.1"; 
父主题： [GTP节点管理保护配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除GTP节点管理保护配置(DEL GTP PROTECT IP) 
### 删除GTP节点管理保护配置(DEL GTP PROTECT IP) 
命令功能 
该命令用于删除GTP节点管理保护配置。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GTP节点地址|参数可选性:必选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。本端网元为SGSN的情况下，该地址包括如下两种情况：如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW GPRS APN、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得。SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。本端网元为MME的情况下，该地址包括如下两种情况：如果对端网元为SGW/PGW，该参数的取值可通过SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW EPC APN命令查询的是通过本地数据解析的SGW/PGW IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGW/PGW IP地址）。如果对端网元为MME，该参数的取值可通过SHOW EPCHOST或DNS LOOKUP命令的查询结果获得。SHOW EPCHOST命令查询的是通过本地数据解析的MME IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的MME IP地址）。
命令举例 
删除GTP节点地址为192.168.0.1的GTP节点管理保护配置。
DEL GTP PROTECT IP:IPADDR="192.168.0.1"; 
父主题： [GTP节点管理保护配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询GTP节点管理保护配置(SHOW GTP PROTECT IP) 
### 查询GTP节点管理保护配置(SHOW GTP PROTECT IP) 
命令功能 
该命令用于查询GTP节点管理保护配置。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GTP节点地址|参数可选性:任选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。本端网元为SGSN的情况下，该地址包括如下两种情况：如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW GPRS APN、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得。SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。本端网元为MME的情况下，该地址包括如下两种情况：如果对端网元为SGW/PGW，该参数的取值可通过SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW EPC APN命令查询的是通过本地数据解析的SGW/PGW IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGW/PGW IP地址）。如果对端网元为MME，该参数的取值可通过SHOW EPCHOST或DNS LOOKUP命令的查询结果获得。SHOW EPCHOST命令查询的是通过本地数据解析的MME IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的MME IP地址）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPADDR|GTP节点地址|参数可选性:任选参数；参数类型:地址|GSN节点的IP地址，包括IPv4或者IPv6地址。本端网元为SGSN的情况下，该地址包括如下两种情况：如果对端网元为GGSN，该参数的取值可通过SHOW GPRS APN、SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW GPRS APN、SHOW EPC APN命令查询的是通过本地数据解析的GGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的GGSN IP地址）。如果对端网元为SGSN，该参数的取值可通过SHOW SGSNHOST或DNS LOOKUP命令的查询结果获得。SHOW SGSNHOST命令查询的是通过本地数据解析的SGSN IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGSN IP地址）。本端网元为MME的情况下，该地址包括如下两种情况：如果对端网元为SGW/PGW，该参数的取值可通过SHOW EPC APN或DNS LOOKUP命令的查询结果获得。SHOW EPC APN命令查询的是通过本地数据解析的SGW/PGW IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的SGW/PGW IP地址）。如果对端网元为MME，该参数的取值可通过SHOW EPCHOST或DNS LOOKUP命令的查询结果获得。SHOW EPCHOST命令查询的是通过本地数据解析的MME IP地址，DNS LOOKUP命令查询的是通过DNS解析获取的MME IP地址）。
命令举例 
查询GTP节点地址为192.168.0.1的GTP节点管理保护配置。
SHOW GTP PROTECT IP:IPADDR="192.168.0.1"; 
`
命令 (No.1): SHOW GTP PROTECT IP:IPADDR="192.168.0.1";
操作维护  GTP节点地址 
-----------------------
复制 删除  192.168.0.1 
-----------------------
记录数 1
命令执行成功（耗时 0.022 秒）。
` 
父主题： [GTP节点管理保护配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 系统可用性配置 
## 系统可用性配置 
背景知识 
系统可用性表征系统运行的稳定程度，是指除了特定维护操作（比如版本升级）外，系统正常运行时间与统计时长的百分比。可用性数值越高，系统稳定性越好。该功能是系统的一个可选项，系统提供了启用开关，可根据需要决定是否开启该功能。 
功能描述 
设置或查看系统可用性统计功能开关。 
相关主题 
 
修改系统可用性统计开关(SET SYSAVAILSTAT)
 
 
查询系统可用性统计开关(SHOW SYSAVAILSTAT)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置系统可用性统计开关(SET SYSAVAILSTAT) 
### 设置系统可用性统计开关(SET SYSAVAILSTAT) 
命令功能 
该命令用于打开或关闭系统可用性统计功能开关。 
系统可用性表征系统运行的稳定程度，是指除了特定维护操作（比如版本升级）外，系统正常运行时间与统计时长的百分比。可用性数值越高，系统稳定性越好。 
注意事项 
该开关值需根据网络规划确定，默认是关闭状态。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SAS|系统可用性统计|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|决定网元中是否启用系统可用性统计功能。ON：打开系统可用性统计功能。OFF：关闭系统可用性统计功能。
命令举例 
关闭系统可用性统计功能开关。 
SET SYSAVAILSTAT:SAS="OFF"; 
父主题： [系统可用性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询系统可用性统计开关(SHOW SYSAVAILSTAT) 
### 查询系统可用性统计开关(SHOW SYSAVAILSTAT) 
命令功能 
该命令用于查询系统可用性统计功能是否启动的开关状态。无输入参数。默认状态为关闭。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SAS|系统可用性统计|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|决定网元中是否启用系统可用性统计功能。ON：打开系统可用性统计功能。OFF：关闭系统可用性统计功能。
命令举例 
查询系统可用性统计开关。 
SHOW SYSAVAILSTAT; 
`
 命令 (No.1): SHOW SYSAVAILSTAT;
操作维护  系统可用性统计
------------------------
修改      关闭
------------------------
记录数 1
命令执行成功（耗时 0.042 秒）。
` 
父主题： [系统可用性配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 区内GSN网段配置 
## 区内GSN网段配置 
背景知识 
为满足运营商流量监控需求，SGSN网元支持通过GSN IP识别区域内/区域外流量并区分GTP-U（用户面）和GTP-C（控制面）进行流量统计。 
功能描述 
运营商希望针对某些GSN统计区域内的流量时，配置区内GSN网段，区内GSN网段是一组GSN IP地址段，流量统计时处于配置地址段内的为区内流量，否则为区外流量。对应的流量统计体现在“SGSN网元测量->SGSN区内区外GTP测量”这一性能统计测量项的计数器中。 
该功能默认不开启，如果开启需要将区内GGSN IP地址段配置全，否则区分区内/区外的流量统计可能不准确。 
相关主题 
 
新增区内GSN网段配置(ADD LOCAL GSN)
 
 
删除区内GSN网段配置(DEL LOCAL GSN)
 
 
查询区内GSN网段配置(SHOW LOCAL GSN)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增区内GSN网段配置(ADD LOCAL GSN) 
### 新增区内GSN网段配置(ADD LOCAL GSN) 
命令功能 
该命令用于新增区内GSN网段配置。当运营商需要对一组GSN（SGSN、GGSN）进行流量统计时，使用该命令。
注意事项 
该命令只适用于SGSN网元。
参数说明 
标识|名称|类型|说明
---|---|---|---
GSNIP|GSN网段地址|参数可选性:必选参数；参数类型:地址|配置省内GSN网段的IP地址(SGSN、GGSN的控制面和用户面地址。)，包括IPv4或者IPv6地址。
GSNMASK|GSN网段掩码|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|表示子网掩码的长度。IPv4地址掩码最大长度为32，IPv6地址掩码最大长度为128。
命令举例 
新增区内GSN网段配置，GSN网段地址为10.44.36.0，GSN网段掩码为24。 
ADD LOCAL GSN:GSNIP=10.44.36.0,GSNMASK=24; 
父主题： [区内GSN网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除区内GSN网段配置(DEL LOCAL GSN) 
### 删除区内GSN网段配置(DEL LOCAL GSN) 
命令功能 
该命令用于删除区内GSN网段配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GSNIP|GSN网段地址|参数可选性:必选参数；参数类型:地址|配置省内GSN网段的IP地址(SGSN、GGSN的控制面和用户面地址。)，包括IPv4或者IPv6地址。
GSNMASK|GSN网段掩码|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|表示子网掩码的长度。IPv4地址掩码最大长度为32，IPv6地址掩码最大长度为128。
命令举例 
删除GSN网段地址为10.44.36.0，GSN网段掩码为24的区内GSN网段配置。 
DEL LOCAL GSN:GSNIP="10.44.36.0",GSNMASK=24; 
父主题： [区内GSN网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询区内GSN网段配置(SHOW LOCAL GSN) 
### 查询区内GSN网段配置(SHOW LOCAL GSN) 
命令功能 
该命令用于查询区内GSN网段配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GSNIP|GSN网段地址|参数可选性:任选参数；参数类型:地址|配置省内GSN网段的IP地址(SGSN、GGSN的控制面和用户面地址。)，包括IPv4或者IPv6地址。
GSNMASK|GSN网段掩码|参数可选性:任选参数；参数类型:整数；参数范围为:0~128。|表示子网掩码的长度。IPv4地址掩码最大长度为32，IPv6地址掩码最大长度为128。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GSNIP|GSN网段地址|参数可选性:任选参数；参数类型:地址|配置省内GSN网段的IP地址(SGSN、GGSN的控制面和用户面地址。)，包括IPv4或者IPv6地址。
GSNMASK|GSN网段掩码|参数可选性:任选参数；参数类型:整数。|表示子网掩码的长度。IPv4地址掩码最大长度为32，IPv6地址掩码最大长度为128。
命令举例 
查询区内GSN网段配置。 
SHOW LOCAL GSN; 
`
命令 (No.1): SHOW LOCAL GSN
操作维护   GSN网段地址 GSN网段掩码 
------------------------------------------
复制 删除  10.44.36.0     24 
------------------------------------------
记录数 1
命令执行成功（耗时 0.034 秒）。
` 
父主题： [区内GSN网段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## CSFB配置 
## CSFB配置 
背景知识 
            
            CSFB（Circuit Switch Fallback，电路域回落）即CS回落，指触发终端从LTE网络回落到2/3G网络的CS（Circuit Switch，电路交换）域，以便进行语音业务。
        
功能描述 
在LTE网络中，切换和CSFB业务同时出现的概率比较大，为尽量保证CSFB业务的成功，通过本功能配置进行CSFB业务和切换业务的优先级，及配置和切换后各CSFB信令的重发处理配置策略。 
MME在发现切换和CSFB业务同时出现时，根据本功能配置的优先级决定是继续执行切换业务还是执行CSFB业务，根据本功能配置的重发处理策略配置决定策由切换导致发送失败的CSFB消息是否重发等。 
相关主题 
 
设置CSFB参数(SET CSFBCFG)
 
 
查询CSFB参数(SHOW CSFBCFG)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置CSFB参数(SET CSFBCFG) 
### 设置CSFB参数(SET CSFBCFG) 
命令功能 
该命令用于设置用户CSFB业务和切换业务发生冲突时MME的处理策略，比如优先处理CSFB还是优先处理切换业务。当本局存在用户CSFB业务和切换业务冲突场景时，使用该命令。命令执行成功后，当CSFB业务与切换业务冲突时，依据该配置策略处理切换和CSFB业务。 
由于CSFB和切换由不同的网元触发，因此存在冲突的可能性。典型场景，UE作为被叫，MSC发送SGs寻呼请求消息给MME，触发MT CSFB，而同时用户位置正在移动出源eNodeB，源eNodeB根据用户上报的测量报告，决策用户需要切出本eNodeB，触发切换业务，发送Handover Required消息给MME。这样对于MME而言，此时用户存在两种业务：MT CSFB和切换。为了减少由于冲突导致MT CSFB或者切换业务失败，MME需要根据该配置决策优先执行那种业务。 
注意事项 
 
使用该命令前，需要本局MME支持SGs接口，配置命令为：SET SGSFLAG:SGSFLAG="YES";。
 
 
使用该命令前，需要本局License中支持CSFB功能。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PRIORITY|切换优先于CSFB|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置切换业务是否优先于CSFB业务。否（NO）： CSFB业务优先于切换业务，当出现CSFB业务和切换业务冲突时，优先处理CSFB业务。是（YES）: 切换业务优先于CSFB业务，当出现CSFB业务和切换业务冲突时，优先处理切换业务，缓存CSFB业务。切换完成后，再执行CSFB业务。
STOPHO|终止切换准备阶段进行CSFB|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。否（NO）：当用户处于切换准备阶段，用户执行CSFB业务时，继续切换业务，切换业务完成后再进行CSFB业务。是（YES）：当用户处于切换准备阶段，用户执行CSFB业务时，终止切换业务，执行CSFB业务。
RETNOTITY|切换后重发CS业务通知|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。否（NO）:当用户作为被叫时，MME下发CS业务通知消息给UE，但eNodeB返回NAS未投递消息给MME，未投递原因为用户正在进行切换。MME终止用户被叫业务处理，处理切换业务。是（YES）:当用户作为被叫时，MME下发CS业务通知消息给UE，但eNodeB返回NAS未投递消息给MME，未投递原因为用户正在进行切换。MME暂停用户被叫业务处理，处理切换业务。切换成功后，根据该配置重新下发CS业务通知消息给UE。
RETMODIFY|切换后重发UE上下文修改请求|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。当MME发送UE Context Modify Request消息给eNodeB，携带CSFB业务指示，但eNodeB返回UE Context Modify Failure，原因为用户正在进行切换。MME暂停用户CSFB业务处理，处理切换业务。切换成功后，根据该配置决定是否重新下发UE Context Modify Request消息给eNodeB，携带CSFB业务指示。否(NO):执行CSFB业务时，当MME发送UE Context Modify Request消息给eNodeB，携带CSFB业务指示，但eNodeB返回UE Context Modify Failure，原因值指示用户正在进行切换，MME终止CSFB业务。是(YES):执行CSFB业务时，当MME发送UE Context Modify Request消息给eNodeB，携带CSFB业务指示，但eNodeB返回UE Context Modify Failure，原因值指示用户正在进行切换。MME暂停用户CSFB业务处理，处理切换业务。切换成功后，重新下发UE Context Modify Request消息给eNodeB，携带CSFB业务指示。
WTTAUTM|切换成功后等待TAU时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~10。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。当用户CSFB业务于切换业务冲突时，优先处理切换业务。由于切换后，用户有可能触发跟踪区更新业务，为了防止与CSFB业务冲突，MME在切换成功后，设置定时器等待用户跟踪区更新业务，定时器时长即为该参数值。
WTHOTM|等待切换初始消息的时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。用户被叫，MME下发CS业务通知给UE，但eNodeB返回NAS未投递，原因值指示用户正在进行切换；或者MME执行扩展业务请求，MME下发UE Context Modify Request消息给eNB，携带CSFB指示，但eNB返回UE Context Modify Failure，原因值指示正在切换。上述场景，MME暂停CSFB业务，处理切换业务，若此时切换还未通知到MME，则设置定时器等待eNB的切换请求，定时器时长即为该数值。
WTNASNDTM|等待NAS未投递消息时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”、并且“切换后重发CS业务通知”配置为“是(YES)”。当用户作为被叫时，MME下发CS业务通知消息给UE，但eNodeB返回NAS未投递消息给MME，未投递原因为用户正在进行切换。MME暂停用户被叫业务处理，处理切换业务。切换成功后，MME重新下发CS业务通知消息给UE。为了防止eNodeB返回NAS未投递，导致MME又重新处理切换与CSFB的冲突，陷入可能的切换-CSFB-切换-CSFB…无尽循环中，MME下发重新下发CS业务通知给UE后，设置定时器等待NAS未投递消息，定时器时长为该参数值。若MME在定时器超时前收到NAS未投递，原因值为正在进行切换，则终止CSFB业务。
RCONTEXT|UE上下文初始建立或修改失败时保留会话上下文|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|执行用户CSFB业务时，eNodeB返回Initial Context Setup Failure或者UE Context Modify Failure，MME依据该配置，决定是否删除用户上下文、是否下发业务拒绝消息给UE。 该参数取值及其含义如下：不保留(NOT_RESERVING): MME删除用户承载上下文，并下发业务拒绝消息给UE。拒绝并保留(REFUSE_RESERVE): MME不删除用户承载上下文，但下发业务拒绝消息给UE。保留(RESERVING): MME不删除用户承载上下文，也不下发业务拒绝消息给UE。
命令举例 
当用户CSFB业务和切换业务冲突时，设置CSFB业务优先于切换业务，并且UE上下文修改失败时不保留会话上下文。 
SET CSFBCFG:PRIORITY="NO",RCONTEXT="NOT_RESERVING"; 
父主题： [CSFB配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询CSFB参数(SHOW CSFBCFG) 
### 查询CSFB参数(SHOW CSFBCFG) 
命令功能 
该命令用于查询用户CSFB业务和切换业务发生冲突时MME的处理策略。 
注意事项 
MME配置的CSFB业务与切换业务冲突时处理策略，需要在本局MME支持SGs接口并且本局License中支持CSFB功能时才会生效。查询本局是否支持SGs功能的命令为：[SHOW SGSFLAG];，查询本局License的命令为：[SHOW LICENSE]。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PRIORITY|切换优先于CSFB|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置切换业务是否优先于CSFB业务。否（NO）： CSFB业务优先于切换业务，当出现CSFB业务和切换业务冲突时，优先处理CSFB业务。是（YES）: 切换业务优先于CSFB业务，当出现CSFB业务和切换业务冲突时，优先处理切换业务，缓存CSFB业务。切换完成后，再执行CSFB业务。
STOPHO|终止切换准备阶段进行CSFB|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。否（NO）：当用户处于切换准备阶段，用户执行CSFB业务时，继续切换业务，切换业务完成后再进行CSFB业务。是（YES）：当用户处于切换准备阶段，用户执行CSFB业务时，终止切换业务，执行CSFB业务。
RETNOTITY|切换后重发CS业务通知|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。否（NO）:当用户作为被叫时，MME下发CS业务通知消息给UE，但eNodeB返回NAS未投递消息给MME，未投递原因为用户正在进行切换。MME终止用户被叫业务处理，处理切换业务。是（YES）:当用户作为被叫时，MME下发CS业务通知消息给UE，但eNodeB返回NAS未投递消息给MME，未投递原因为用户正在进行切换。MME暂停用户被叫业务处理，处理切换业务。切换成功后，根据该配置重新下发CS业务通知消息给UE。
RETMODIFY|切换后重发UE上下文修改请求|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。当MME发送UE Context Modify Request消息给eNodeB，携带CSFB业务指示，但eNodeB返回UE Context Modify Failure，原因为用户正在进行切换。MME暂停用户CSFB业务处理，处理切换业务。切换成功后，根据该配置决定是否重新下发UE Context Modify Request消息给eNodeB，携带CSFB业务指示。否(NO):执行CSFB业务时，当MME发送UE Context Modify Request消息给eNodeB，携带CSFB业务指示，但eNodeB返回UE Context Modify Failure，原因值指示用户正在进行切换，MME终止CSFB业务。是(YES):执行CSFB业务时，当MME发送UE Context Modify Request消息给eNodeB，携带CSFB业务指示，但eNodeB返回UE Context Modify Failure，原因值指示用户正在进行切换。MME暂停用户CSFB业务处理，处理切换业务。切换成功后，重新下发UE Context Modify Request消息给eNodeB，携带CSFB业务指示。
WTTAUTM|切换成功后等待TAU时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。当用户CSFB业务于切换业务冲突时，优先处理切换业务。由于切换后，用户有可能触发跟踪区更新业务，为了防止与CSFB业务冲突，MME在切换成功后，设置定时器等待用户跟踪区更新业务，定时器时长即为该参数值。
WTHOTM|等待切换初始消息的时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”。用户被叫，MME下发CS业务通知给UE，但eNodeB返回NAS未投递，原因值指示用户正在进行切换；或者MME执行扩展业务请求，MME下发UE Context Modify Request消息给eNB，携带CSFB指示，但eNB返回UE Context Modify Failure，原因值指示正在切换。上述场景，MME暂停CSFB业务，处理切换业务，若此时切换还未通知到MME，则设置定时器等待eNB的切换请求，定时器时长即为该数值。
WTNASNDTM|等待NAS未投递消息时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数生效，需要“切换优先于CSFB”配置为“是(YES)”、并且“切换后重发CS业务通知”配置为“是(YES)”。当用户作为被叫时，MME下发CS业务通知消息给UE，但eNodeB返回NAS未投递消息给MME，未投递原因为用户正在进行切换。MME暂停用户被叫业务处理，处理切换业务。切换成功后，MME重新下发CS业务通知消息给UE。为了防止eNodeB返回NAS未投递，导致MME又重新处理切换与CSFB的冲突，陷入可能的切换-CSFB-切换-CSFB…无尽循环中，MME下发重新下发CS业务通知给UE后，设置定时器等待NAS未投递消息，定时器时长为该参数值。若MME在定时器超时前收到NAS未投递，原因值为正在进行切换，则终止CSFB业务。
RCONTEXT|UE上下文初始建立或修改失败时保留会话上下文|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|执行用户CSFB业务时，eNodeB返回Initial Context Setup Failure或者UE Context Modify Failure，MME依据该配置，决定是否删除用户上下文、是否下发业务拒绝消息给UE。 该参数取值及其含义如下：不保留(NOT_RESERVING): MME删除用户承载上下文，并下发业务拒绝消息给UE。拒绝并保留(REFUSE_RESERVE): MME不删除用户承载上下文，但下发业务拒绝消息给UE。保留(RESERVING): MME不删除用户承载上下文，也不下发业务拒绝消息给UE。
命令举例 
查询CSFB业务与切换业务发生冲突时，MME的处理策略。 
SHOW CSFBCFG; 
`
命令 (No.1): SHOW CSFBCFG;
操作维护  切换优先于CSFB   终止切换准备阶段进行CSFB   切换后重发CS业务通知   切换后重发UE上下文修改请求   切换成功后等待TAU时长(秒)   等待切换初始消息的时长(秒)   等待NAS未投递消息时长(秒)   UE上下文初始建立或修改失败时保留会话上下文
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      是               是                         是                     是                           0                           1                            2                           不保留
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.068 秒）。
` 
父主题： [CSFB配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## IP和位置关联配置 
## IP和位置关联配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
“IP和位置关联配置”用于设置IP和位置关联功能策略、具体的RA编组或TA编组、省内用户的IMSI号段。 
用户IP和位置关联功能策略包括： 
 
用户IP和位置关联功能开启或关闭时，SGSN/MME是否强制UE下线。
 
 
用户进入非RA编组或非TA编组时，SGSN/MME是否强制UE下线。
 
 
位置IP关联功能是否去连接紧急呼叫，即在位置IP关联功能开启需分离UE时/位置IP关联功能关闭需分离UE时/TA编组发生变化需分离UE时，是否去连接紧急呼叫会话。
 
 
SGSN/MME强制UE下线方式。
 
 
位置IP关联功能是否限制国际漫游用户访问数据业务及限制时给UE的拒绝原因值。
 
 
位置IP关联功能是否限制国内漫游用户访问数据业务及限制时给UE的拒绝原因值。
 
 
位置IP关联RA编组或TA编组，配置具体的RA编组或TA编组。 
如果需要限制在RA编组内或TA编组内的国内漫游用户访问数据业务，则需要配置省内用户的IMSI号段，识别出国内漫游用户。 
注：
“IP和位置关联配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
相关主题 
 
SGSN IP和位置关联配置
 
 
RA编组规则配置
 
 
位置IP关联RA编组配置
 
 
MME IP和位置关联配置
 
 
TA编组规则配置
 
 
位置IP关联TA编组配置
 
 
位置IP关联5G TA编组配置
 
 
控制开关配置
 
 
区域编组配置
 
 
省内用户IMSI号段配置
 
 
基于数据APN的IP地址细分配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### SGSN IP和位置关联配置 
### SGSN IP和位置关联配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
本功能模块主要实现2G/3G用户IP和位置关联功能策略，包括： 
 
用户IP和位置关联功能开启或关闭时，SGSN是否强制UE下线。
 
 
用户进入非RA编组时，SGSN是否强制UE下线。
 
 
SGSN强制UE下线方式。
 
 
位置IP关联功能是否限制国际漫游用户及限制时给UE的拒绝原因值。
 
 
位置IP关联功能是否限制国内漫游用户及限制时给UE的拒绝原因值。
 
 
注：
“SGSN IP和位置关联配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
相关主题 
 
设置SGSN IP地址和位置关联配置(SET SGSNIPLOC)
 
 
查询SGSN IP地址和位置关联配置(SHOW SGSNIPLOC)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置SGSN IP地址和位置关联配置(SET SGSNIPLOC) 
#### 设置SGSN IP地址和位置关联配置(SET SGSNIPLOC) 
命令功能 
本命令用于设置2G/3G用户IP和位置关联功能策略，包括： 
 
用户IP和位置关联功能开启时，SGSN是否强制UE下线。
 
 
用户IP和位置关联功能关闭时，SGSN是否强制UE下线。
 
 
SGSN强制UE下线方式。
 
 
用户进入非RA编组时，SGSN是否强制UE下线。
 
 
注意事项 
设置开启IP和位置关联功能时，需要一并把IP和位置关联功能的策略也确定好 
参数说明 
标识|名称|类型|说明
---|---|---|---
DETACH|功能开启时SGSN是否强制UE下线|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGSN是否支持用户IP地址和位置关联功能开启时是否分离UE：是：支持。否：不支持。
DETACHFUNCOFF|功能关闭时SGSN是否强制UE下线|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能关闭时，SGSN是否强制UE下线。是：SGSN对所有在RA编组内的UE进行强制下线。否：UE不下线。
UEOFFMETHOD|强制UE下线方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置UE下线方式：分离UE。去激活PDP。
NONRADEACT|进入非RA编组位置时SGSN是否去激活PDP|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|进入非RA编组位置时SGSN是否去激活PDP： 是：去激活PDP。否：不去激活PDP。
命令举例 
设置SGSN IP地址和位置关联功能的策略。其中功能开启时SGSN是否强制UE下线为“否”，功能关闭时SGSN是否强制UE下线为“是”，强制UE下线方式为“分离UE”，进入非RA编组位置时SGSN是否去激活PDP“是”。 
SET SGSNIPLOC:DETACH="NO",DETACHFUNCOFF="YES",UEOFFMETHOD="DETACH_UE",NONRADEACT="YES"; 
父主题： [SGSN IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询SGSN IP地址和位置关联配置(SHOW SGSNIPLOC) 
#### 查询SGSN IP地址和位置关联配置(SHOW SGSNIPLOC) 
命令功能 
该命令用于查询IP和位置关联功能的策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DETACH|功能开启时SGSN是否强制UE下线|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SGSN是否支持用户IP地址和位置关联功能开启时是否分离UE：是：支持。否：不支持。
DETACHFUNCOFF|功能关闭时SGSN是否强制UE下线|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能关闭时，SGSN是否强制UE下线。是：SGSN对所有在RA编组内的UE进行强制下线。否：UE不下线。
UEOFFMETHOD|强制UE下线方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置UE下线方式：分离UE。去激活PDP。
NONRADEACT|进入非RA编组位置时SGSN是否去激活PDP|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|进入非RA编组位置时SGSN是否去激活PDP： 是：去激活PDP。否：不去激活PDP。
命令举例 
查询SGSN IP地址和位置关联功能的策略。 
SHOW SGSNIPLOC; 
`
命令 (No.1): SHOW SGSNIPLOC
操作维护   功能开启时SGSN是否强制UE下线   功能关闭时SGSN是否强制UE下线   强制UE下线方式   进入非RA编组位置时SGSN是否去激活PDP 
-----------------------------------------------------------------------------------------------------------------------------
修改       否                             是                             分离UE           是 
-----------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.313 秒）。
` 
父主题： [SGSN IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### RA编组规则配置 
### RA编组规则配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
本功能模块实现2G/3G用户在RA编组中，关联的IP和位置关联功能策略，包括： 
 
RA编组是否支持用户IP地址和位置关联开关。
 
 
位置IP关联功能是否限制国际漫游用户访问数据业务及限制时给UE的拒绝原因值。
 
 
位置IP关联功能是否限制国内漫游用户访问数据业务及限制时给UE的拒绝原因值。
 
 
注：
“RA编组规则配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
相关主题 
 
新增RA编组规则配置(ADD RAGROUP RULE)
 
 
修改RA编组规则配置(SET RAGROUP RULE)
 
 
删除RA编组规则配置(DEL RAGROUP RULE)
 
 
查询RA编组规则配置(SHOW RAGROUP RULE)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增RA编组规则配置(ADD RAGROUP RULE) 
#### 新增RA编组规则配置(ADD RAGROUP RULE) 
命令功能 
该命令用于增加位置IP关联功能的RA编组策略。 
注意事项 
设置开启IP和位置关联功能时，需要一并把IP和位置关联功能的策略也确定好 
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|RA编组规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联功能的RA编组策略标识，用于区分不同的位置IP关联功能的RA编组策略。
RAGROUPIPLOC|RA编组是否支持用户IP地址和位置关联|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该位置IP关联RA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，SGSN才需要对该位置IP关联RA编组下的移动用户启用IP位置关联功能。
IMPACTINTERROAM|SGSN位置IP关联功能是否限制国际漫游用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|位置IP关联功能开启，如果国际漫游用户在TA编组内：是：拒绝PDP激活。否：不拒绝PDP激活。
IMPACTINTRAROAM|SGSN位置IP关联功能是否限制国内漫游用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:SAMENOTROAM。|位置IP关联功能开启时，SGSN是否限制在RA编组内的国内漫游用户访问数据网络。限制接入：限制其访问数据网络，拒绝用户注册，拒绝原因值取自参数“SGSN由于位置IP关联功能拒绝国内漫游用户接入的原因值”。同位置IP关联功能没有开启时处理：等同于位置IP功能没有开启时一样处理。同非漫游用户处理：等同于非漫游用户时一样处理。
SLMTINTERCAUSE|SGSN由于位置IP关联功能拒绝国际漫游用户接入的原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NoSuitCellInLA。|位置IP关联功能开启且参数“SGSN位置IP关联功能是否限制国际漫游用户”设置为“限制”时，SGSN会拒绝注册在其RA编组内的国际漫游用户，拒绝原因值由该参数指定。
SLMTINTRACAUSE|SGSN由于位置IP关联功能拒绝国内漫游用户接入的原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NoSuitCellInLA。|位置IP关联功能开启且参数“SGSN位置IP关联功能限制国内漫游用户”设置为“限制”时，SGSN会拒绝注册在其RA编组内的国内漫游用户，拒绝原因值由该参数指定。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联功能的RA编组策略。 该参数不被其他命令引用，无其他意义。
命令举例 
新增位置IP关联功能的RA编组策略配置，其中RA编组规则标识为“1”，RA编组是否支持用户IP地址和位置关联为“是”，SGSN位置IP关联功能是否限制国际漫游用户为“是”，SGSN位置IP关联功能是否限制国内漫游用户为“是”，SGSN由于位置IP关联功能拒绝国际漫游用户接入的原因值为“PLMN不允许”，SGSN由于位置IP关联功能拒绝国内漫游用户接入的原因值为“PLMN不允许”，用户别名为“area1”。 
ADD RAGROUP RULE:RULEID=1,RAGROUPIPLOC="YES",IMPACTINTERROAM="YES",IMPACTINTRAROAM="LIMITACCESS",SLMTINTERCAUSE="PLMNNotAllowed",SLMTINTRACAUSE="PLMNNotAllowed",NAME="area1"; 
父主题： [RA编组规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改RA编组规则配置(SET RAGROUP RULE) 
#### 修改RA编组规则配置(SET RAGROUP RULE) 
命令功能 
该命令用于修改位置IP关联功能的RA编组策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|RA编组规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联功能的RA编组策略标识，用于区分不同的位置IP关联功能的RA编组策略。
RAGROUPIPLOC|RA编组是否支持用户IP地址和位置关联|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该位置IP关联RA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，SGSN才需要对该位置IP关联RA编组下的移动用户启用IP位置关联功能。
IMPACTINTERROAM|SGSN位置IP关联功能是否限制国际漫游用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启，如果国际漫游用户在TA编组内：是：拒绝PDP激活。否：不拒绝PDP激活。
IMPACTINTRAROAM|SGSN位置IP关联功能是否限制国内漫游用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启时，SGSN是否限制在RA编组内的国内漫游用户访问数据网络。限制接入：限制其访问数据网络，拒绝用户注册，拒绝原因值取自参数“SGSN由于位置IP关联功能拒绝国内漫游用户接入的原因值”。同位置IP关联功能没有开启时处理：等同于位置IP功能没有开启时一样处理。同非漫游用户处理：等同于非漫游用户时一样处理。
SLMTINTERCAUSE|SGSN由于位置IP关联功能拒绝国际漫游用户接入的原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启且参数“SGSN位置IP关联功能是否限制国际漫游用户”设置为“限制”时，SGSN会拒绝注册在其RA编组内的国际漫游用户，拒绝原因值由该参数指定。
SLMTINTRACAUSE|SGSN由于位置IP关联功能拒绝国内漫游用户接入的原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启且参数“SGSN位置IP关联功能限制国内漫游用户”设置为“限制”时，SGSN会拒绝注册在其RA编组内的国内漫游用户，拒绝原因值由该参数指定。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联功能的RA编组策略。 该参数不被其他命令引用，无其他意义。
命令举例 
修改位置IP关联功能的RA编组策略配置，其中RA编组规则标识为“1”，RA编组是否支持用户IP地址和位置关联为“否”。 
SET RAGROUP RULE:RULEID=1,RAGROUPIPLOC="NO"; 
父主题： [RA编组规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除RA编组规则配置(DEL RAGROUP RULE) 
#### 删除RA编组规则配置(DEL RAGROUP RULE) 
命令功能 
该命令用于删除位置IP关联功能的RA编组策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|RA编组规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联功能的RA编组策略标识，用于区分不同的位置IP关联功能的RA编组策略。
命令举例 
删除位置IP关联功能的RA编组策略配置，其中RA编组规则标识为“1”。 
DEL RAGROUP RULE:RULEID=1; 
父主题： [RA编组规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询RA编组规则配置(SHOW RAGROUP RULE) 
#### 查询RA编组规则配置(SHOW RAGROUP RULE) 
命令功能 
该命令用于查询已配置位置IP关联功能的RA编组策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|RA编组规则标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|位置IP关联功能的RA编组策略标识，用于区分不同的位置IP关联功能的RA编组策略。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|RA编组规则标识|参数可选性:任选参数；参数类型:整数。|位置IP关联功能的RA编组策略标识，用于区分不同的位置IP关联功能的RA编组策略。
RAGROUPIPLOC|RA编组是否支持用户IP地址和位置关联|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该位置IP关联RA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，SGSN才需要对该位置IP关联RA编组下的移动用户启用IP位置关联功能。
IMPACTINTERROAM|SGSN位置IP关联功能是否限制国际漫游用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启，如果国际漫游用户在TA编组内：是：拒绝PDP激活。否：不拒绝PDP激活。
IMPACTINTRAROAM|SGSN位置IP关联功能是否限制国内漫游用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启时，SGSN是否限制在RA编组内的国内漫游用户访问数据网络。限制接入：限制其访问数据网络，拒绝用户注册，拒绝原因值取自参数“SGSN由于位置IP关联功能拒绝国内漫游用户接入的原因值”。同位置IP关联功能没有开启时处理：等同于位置IP功能没有开启时一样处理。同非漫游用户处理：等同于非漫游用户时一样处理。
SLMTINTERCAUSE|SGSN由于位置IP关联功能拒绝国际漫游用户接入的原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启且参数“SGSN位置IP关联功能是否限制国际漫游用户”设置为“限制”时，SGSN会拒绝注册在其RA编组内的国际漫游用户，拒绝原因值由该参数指定。
SLMTINTRACAUSE|SGSN由于位置IP关联功能拒绝国内漫游用户接入的原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启且参数“SGSN位置IP关联功能限制国内漫游用户”设置为“限制”时，SGSN会拒绝注册在其RA编组内的国内漫游用户，拒绝原因值由该参数指定。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户自定义别名，便于记忆和识别各位置IP关联功能的RA编组策略。 该参数不被其他命令引用，无其他意义。
命令举例 
查询位置IP关联功能的RA编组策略配置，查询所有已配置的位置IP关联功能的RA编组策略。 
SHOW RAGROUP RULE; 
`
命令 (No.1): SHOW RAGROUP RULE;
操作维护         RA编组规则标识   RA编组是否支持用户IP地址和位置关联   SGSN位置IP关联功能是否限制国际漫游用户   SGSN位置IP关联功能是否限制国内漫游用户   SGSN由于位置IP关联功能拒绝国际漫游用户接入的原因值   SGSN由于位置IP关联功能拒绝国内漫游用户接入的原因值   用户别名
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1                否                                   是                                       限制接入                                 PLMN不允许                                           PLMN不允许                                           area1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.052 秒）。
` 
父主题： [RA编组规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 位置IP关联RA编组配置 
### 位置IP关联RA编组配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
通过配置RA编组，把同一个区（县）下的RA编为同一个位置IP关联功能的RA编组。一个RA编组与一个IP地址池一一对应，因此，UE在位置IP关联RA编组内移动时，不需要为UE的会话重新分配IP。 
注：
“位置IP关联RA编组配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
相关主题 
 
新增位置IP关联RA编组配置(ADD RAGROUP)
 
 
修改位置IP关联RA编组配置(SET RAGROUP)
 
 
删除位置IP关联RA编组配置(DEL RAGROUP)
 
 
查询位置IP关联RA编组配置(SHOW RAGROUP)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增位置IP关联RA编组配置(ADD RAGROUP) 
#### 新增位置IP关联RA编组配置(ADD RAGROUP) 
命令功能 
该命令用于增加位置IP关联功能的RA编组，一般同一个区（县）下的RA/LA编为同一个位置IP关联功能的RA编组。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联RA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联RA编组编号，一般一个区（县）对应一个位置IP关联RA编组编号
NAME|编组别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联RA编组。 该参数不被其他命令引用，无其他意义。
RULEID|RA编组规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该位置IP关联RA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，SGSN才需要对该位置IP关联RA编组下的移动用户启用IP位置关联功能。
LAI|位置区|参数可选性:必须单选参数；参数类型:复合参数|该参数用于指示网络规划的位置区信息，包括移动国家码、移动网号与位置区域码。
LAMCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
LAMNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
LALAC|位置区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|跟踪区域码，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个跟踪区。EPC系统中的基本的位置信息，运营商规划而定。
RAI|路由区|参数可选性:必须单选参数；参数类型:复合参数|该参数用于指示网络规划的路由区信息，包括移动国家码、移动网号、位置区域码和路由区码。
RAMCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
RAMNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
RALAC|位置区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|跟踪区域码，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个跟踪区。EPC系统中的基本的位置信息，运营商规划而定。
RAC|路由区码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~2个字符。|路由区编码用于识别网络中的路由区。应该根据网络规划进行编码。
命令举例 
新增位置IP关联RA编组配置，其中位置IP关联RA编组编号为1，编组别名为group1，位置区为"460"-"01"-"1A2D"，RA编组规则标识为1。 
ADD RAGROUP:GROUPID=1,NAME="group1",LAI="460"-"01"-"1A2D",RULEID=1; 
父主题： [位置IP关联RA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改位置IP关联RA编组配置(SET RAGROUP) 
#### 修改位置IP关联RA编组配置(SET RAGROUP) 
命令功能 
该命令用于修改位置IP关联功能的RA编组，一般在同一个区（县）下的RA/LA发生改变时使用。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联RA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联RA编组编号，一般一个区（县）对应一个位置IP关联RA编组编号
NAME|编组别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联RA编组。 该参数不被其他命令引用，无其他意义。
RULEID|RA编组规则标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|该位置IP关联RA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，SGSN才需要对该位置IP关联RA编组下的移动用户启用IP位置关联功能。
命令举例 
修改位置IP关联RA编组配置，其中位置IP关联RA编组编号为1，RA编组规则标识为1。 
SET RAGROUP:GROUPID=1,RULEID=1; 
父主题： [位置IP关联RA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除位置IP关联RA编组配置(DEL RAGROUP) 
#### 删除位置IP关联RA编组配置(DEL RAGROUP) 
命令功能 
该命令用于删除位置IP关联功能的RA编组。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联RA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联RA编组编号，一般一个区（县）对应一个位置IP关联RA编组编号
LAI|位置区|参数可选性:任意单选参数；参数类型:复合参数|该参数用于指示网络规划的位置区信息，包括移动国家码、移动网号与位置区域码。
LAMCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
LAMNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
LALAC|位置区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|跟踪区域码，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个跟踪区。EPC系统中的基本的位置信息，运营商规划而定。
RAI|路由区|参数可选性:任意单选参数；参数类型:复合参数|该参数用于指示网络规划的路由区信息，包括移动国家码、移动网号、位置区域码和路由区码。
RAMCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码，MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，例如中国为460。
RAMNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络码，共2位，由国际电联(ITU)统一分配和管理，在一个移动国家码内是唯一标识一个移动网络，比如中国移动TD系统使用00，中国联通GSM系统使用01。
RALAC|位置区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|跟踪区域码，在同一个PLMN（公共陆地移动网络 PLMN=MCC+MNC ）内，标识唯一的一个跟踪区。EPC系统中的基本的位置信息，运营商规划而定。
RAC|路由区码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:2~2个字符。|路由区编码用于识别网络中的路由区。应该根据网络规划进行编码。
命令举例 
删除位置IP关联RA编组配置，其中位置IP关联RA编组编号为1，位置区为"460"-"01"-"1A2D"。 
DEL RAGROUP:GROUPID=1,LAI="460"-"01"-"1A2D"; 
父主题： [位置IP关联RA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询位置IP关联RA编组配置(SHOW RAGROUP) 
#### 查询位置IP关联RA编组配置(SHOW RAGROUP) 
命令功能 
该命令用于查询已配置位置IP关联功能的RA编组。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联RA编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|位置IP关联RA编组编号，一般一个区（县）对应一个位置IP关联RA编组编号
AREATYPE|区域类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|标识是路由区还是位置区。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联RA编组编号|参数可选性:任选参数；参数类型:整数。|位置IP关联RA编组编号，一般一个区（县）对应一个位置IP关联RA编组编号
NAME|编组别名|参数可选性:任选参数；参数类型:字符型。|用户自定义别名，便于记忆和识别各位置IP关联RA编组。 该参数不被其他命令引用，无其他意义。
RULEID|RA编组规则标识|参数可选性:任选参数；参数类型:整数。|该位置IP关联RA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，SGSN才需要对该位置IP关联RA编组下的移动用户启用IP位置关联功能。
LAI|位置区|参数可选性:任选参数；参数类型:字符型。|该参数用于指示网络规划的位置区信息，包括移动国家码、移动网号与位置区域码。
RAI|路由区|参数可选性:任选参数；参数类型:字符型。|该参数用于指示网络规划的路由区信息，包括移动国家码、移动网号、位置区域码和路由区码。
命令举例 
查询位置IP关联RA编组配置，其中位置IP关联RA编组编号为1，区域类型为位置区。 
SHOW RAGROUP:GROUPID=1,AREATYPE="LAI"; 
`
命令 (No.17): SHOW RAGROUP:AREATYPE="LAI";
操作维护         位置IP关联RA编组编号   编组别名   RA编组规则标识   位置区        路由区
----------------------------------------------------------------------------------------
复制 修改 删除   1                      group1     1                460-01-1A2D   
----------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.052 秒）。
` 
父主题： [位置IP关联RA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME IP和位置关联配置 
### MME IP和位置关联配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
本功能模块主要实现LTE用户IP和位置关联功能策略，包括： 
 
用户IP和位置关联功能开启时，MME是否分离UE。
 
 
用户IP和位置关联功能关闭时，MME是否分离UE。
 
 
用户进入非TA编组时，MME是否分离UE。
 
 
位置IP关联功能是否去连接紧急呼叫，即在位置IP关联功能开启需分离UE时/位置IP关联功能关闭需分离UE时/TA编组发生变化需分离UE时，是否去连接紧急呼叫会话。
 
 
MME分离UE的方式。
 
 
位置IP关联功能是否限制国际漫游用户访问数据业务及限制时给UE的拒绝原因值。
 
 
位置IP关联功能是否限制国内漫游用户访问数据业务及限制时给UE的拒绝原因值。
 
 
注：
“MME IP和位置关联配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
相关主题 
 
设置MME IP地址和位置关联配置(SET MMEIPLOC)
 
 
查询MME IP地址和位置关联配置(SHOW MMEIPLOC)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置MME IP地址和位置关联配置(SET MMEIPLOC) 
#### 设置MME IP地址和位置关联配置(SET MMEIPLOC) 
命令功能 
本命令用于设置LTE用户IP和位置关联功能策略，包括： 
 
功能开启时MME是否分离UE。
 
 
功能关闭时MME是否分离UE。
 
 
UE进入非TA编组位置时，MME是否分离UE。
 
 
位置IP关联功能开启或TA编组发生变化时，是否去连接紧急呼叫。
 
 
位置IP关联功能开启或TA编组发生变化时，是否去连接IMS呼叫。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。 
注意事项 
设置开启IP和位置关联功能时，需要一并把IP和位置关联功能的策略也确定好。 
参数说明 
标识|名称|类型|说明
---|---|---|---
DETACH|功能开启时MME是否分离UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能开启时，MME是否分离UE。是：对所有在TA编组内的UE，MME强制分离UE。否：不分离用户。
DETACHFUNCOFF|功能关闭时MME是否分离UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能关闭时，MME是否强制分离UE。是：对所有在TA编组内的UE，MME强制分离UE。否：不分离用户。
NONTADETACH|进入非TA编组位置时MME是否分离UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|UE进入非TA编组位置时，MME是否分离UE。是：MME强制分离UE。否：不分离用户。
IMPACTEMERGFUN|位置IP关联功能是否去连接紧急呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能开启或TA编组发生变化时，是否去连接紧急呼叫会话。是：去连接紧急呼叫会话。否：不去连接紧急呼叫会话。
IFOFFIMSSESS|位置IP关联功能是否去连接IMS PDN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能开启或TA编组发生变化时，是否去连接IMS呼叫。是：去连接IMS呼叫。否：不去连接IMS呼叫
SUPIMSDELAYDIS|支持IMS呼叫跨区延时下线|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持IMS PDN跨区延时下线，用户跨区移动时IMS PDN不去连接情况下，等用户通话结束后，立即释放IMS PDN连接并重建连接。不支持：MME不支持IMS PDN跨区延时下线。支持：MME支持IMS PDN跨区延时下线。
IFPRIVATETA|在私有字段携带TA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识MME作为New MME/AMF时，是否携带TA给Old AMF/MME，或者MME作为Old MME/AMF时，是否携带TA给New AMF/MME，便于New MME/AMF或Old AMF/MME在开启终端的物理位置和终端的IP地址关联功能时，不会误删PDU Session。
命令举例 
设置MME IP地址和位置关联功能的策略。其中功能开启时MME是否分离UE为“否”，功能关闭时MME是否分离UE为“是”，进入非TA编组位置时MME是否分离UE为“否”，位置IP关联功能是否去连接紧急呼叫为“是”，位置IP关联功能是否去连接IMS会话为“是”。 
SET MMEIPLOC:DETACH="NO",DETACHFUNCOFF="YES",NONTADETACH="NO",IMPACTEMERGFUN="YES",IFOFFIMSSESS="YES"; 
父主题： [MME IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MME IP地址和位置关联配置(SHOW MMEIPLOC) 
#### 查询MME IP地址和位置关联配置(SHOW MMEIPLOC) 
命令功能 
该命令用于查询IP和位置关联功能的策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DETACH|功能开启时MME是否分离UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能开启时，MME是否分离UE。是：对所有在TA编组内的UE，MME强制分离UE。否：不分离用户。
DETACHFUNCOFF|功能关闭时MME是否分离UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能关闭时，MME是否强制分离UE。是：对所有在TA编组内的UE，MME强制分离UE。否：不分离用户。
NONTADETACH|进入非TA编组位置时MME是否分离UE|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|UE进入非TA编组位置时，MME是否分离UE。是：MME强制分离UE。否：不分离用户。
IMPACTEMERGFUN|位置IP关联功能是否去连接紧急呼叫|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能开启或TA编组发生变化时，是否去连接紧急呼叫会话。是：去连接紧急呼叫会话。否：不去连接紧急呼叫会话。
IFOFFIMSSESS|位置IP关联功能是否去连接IMS PDN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用户IP地址和位置关联功能开启或TA编组发生变化时，是否去连接IMS呼叫。是：去连接IMS呼叫。否：不去连接IMS呼叫
SUPIMSDELAYDIS|支持IMS呼叫跨区延时下线|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持IMS PDN跨区延时下线，用户跨区移动时IMS PDN不去连接情况下，等用户通话结束后，立即释放IMS PDN连接并重建连接。不支持：MME不支持IMS PDN跨区延时下线。支持：MME支持IMS PDN跨区延时下线。
IFPRIVATETA|在私有字段携带TA|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识MME作为New MME/AMF时，是否携带TA给Old AMF/MME，或者MME作为Old MME/AMF时，是否携带TA给New AMF/MME，便于New MME/AMF或Old AMF/MME在开启终端的物理位置和终端的IP地址关联功能时，不会误删PDU Session。
命令举例 
查询MME IP地址和位置关联功能的策略。 
SHOW MMEIPLOC; 
`
命令 (No.1): SHOW MMEIPLOC
功能开启时MME是否分离UE   功能关闭时MME是否分离UE   进入非TA编组位置时MME是否分离UE   位置IP关联功能是否去连接紧急呼叫   位置IP关联功能是否去连接IMS呼叫   支持IMS PDN跨区延时下线   在私有字段携带TA
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
是                        是                        是                                否                                 是                                不支持                    是                                
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.097 秒）。
` 
父主题： [MME IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### TA编组规则配置 
### TA编组规则配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
本功能模块实现LTE用户在TA编组中，关联的IP和位置关联功能策略，包括： 
 
TA编组是否支持用户IP地址和位置关联开关。
 
 
位置IP关联功能是否限制国际漫游用户访问数据业务及限制时给UE的拒绝原因值。
 
 
位置IP关联功能是否限制国内漫游用户访问数据业务及限制时给UE的拒绝原因值。
 
 
注：
“TA编组规则配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
相关主题 
 
新增TA编组规则配置(ADD TAGROUP RULE)
 
 
修改TA编组规则配置(SET TAGROUP RULE)
 
 
删除TA编组规则配置(DEL TAGROUP RULE)
 
 
查询TA编组规则配置(SHOW TAGROUP RULE)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增TA编组规则配置(ADD TAGROUP RULE) 
#### 新增TA编组规则配置(ADD TAGROUP RULE) 
命令功能 
该命令用于增加位置IP关联功能的TA编组策略。 
注意事项 
设置开启IP和位置关联功能时，需要一并把IP和位置关联功能的策略也确定好。 
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|TA编组规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联功能的TA编组策略标识，用于区分不同的位置IP关联功能的TA编组策略。
TAGROUPIPLOC|TA编组是否支持用户IP地址和位置关联|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该位置IP关联TA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，MME才需要对该位置IP关联TA编组下的移动用户启用IP位置关联功能。
IMPACTINTERROAM|MME位置IP关联功能是否限制国际漫游用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|位置IP关联功能开启，如果国际漫游用户在TA编组内：是：拒绝PDN连接建立。否：不拒绝PDN连接建立。
IMPACTINTRAROAM|MME位置IP关联功能是否限制国内漫游用户|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:SAMENOTROAM。|位置IP关联功能开启时，MME是否限制在TA编组内的国内漫游用户访问数据网络。限制接入：限制其访问数据网络，拒绝用户注册，拒绝原因值取自参数“MME由于位置IP关联功能拒绝国内漫游用户接入的原因值”。同位置IP关联功能没有开启时处理：等同于位置IP功能没有开启时一样处理。同非漫游用户处理：等同于非漫游用户时一样处理。
MLMTINTERCAUSE|MME由于位置IP关联功能拒绝国际漫游用户接入的原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NoCellInTA。|位置IP关联功能开启且参数“MME位置IP关联功能是否限制国际漫游用户”设置为“限制”时，MME会拒绝注册在其TA编组内的国际漫游用户，拒绝原因值由该参数指定。
MLMTINTRACAUSE|MME由于位置IP关联功能拒绝国内漫游用户接入的原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NoCellInTA。|位置IP关联功能开启且参数“MME位置IP关联功能限制国内漫游用户”设置为“限制”时，MME会拒绝注册在其TA编组内的国内漫游用户，拒绝原因值由该参数指定。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联功能的TA编组策略。 该参数不被其他命令引用，无其他意义。
命令举例 
新增位置IP关联功能的TA编组策略配置，其中TA编组规则标识为“1”，TA编组是否支持用户IP地址和位置关联为“是”，MME位置IP关联功能是否限制国际漫游用户为“是”，MME位置IP关联功能是否限制国内漫游用户为“是”，MME由于位置IP关联功能拒绝国际漫游用户接入的原因值为“PLMN不允许”，MME由于位置IP关联功能拒绝国内漫游用户接入的原因值为“PLMN不允许”，用户别名为“area1”。 
ADD TAGROUP RULE:RULEID=1,TAGROUPIPLOC="YES",IMPACTINTERROAM="YES",IMPACTINTRAROAM="LIMITACCESS",MLMTINTERCAUSE="PLMNNotAllowed",MLMTINTRACAUSE="PLMNNotAllowed",NAME="aera1"; 
父主题： [TA编组规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改TA编组规则配置(SET TAGROUP RULE) 
#### 修改TA编组规则配置(SET TAGROUP RULE) 
命令功能 
该命令用于修改位置IP关联功能的TA编组策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|TA编组规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联功能的TA编组策略标识，用于区分不同的位置IP关联功能的TA编组策略。
TAGROUPIPLOC|TA编组是否支持用户IP地址和位置关联|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该位置IP关联TA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，MME才需要对该位置IP关联TA编组下的移动用户启用IP位置关联功能。
IMPACTINTERROAM|MME位置IP关联功能是否限制国际漫游用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启，如果国际漫游用户在TA编组内：是：拒绝PDN连接建立。否：不拒绝PDN连接建立。
IMPACTINTRAROAM|MME位置IP关联功能是否限制国内漫游用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启时，MME是否限制在TA编组内的国内漫游用户访问数据网络。限制接入：限制其访问数据网络，拒绝用户注册，拒绝原因值取自参数“MME由于位置IP关联功能拒绝国内漫游用户接入的原因值”。同位置IP关联功能没有开启时处理：等同于位置IP功能没有开启时一样处理。同非漫游用户处理：等同于非漫游用户时一样处理。
MLMTINTERCAUSE|MME由于位置IP关联功能拒绝国际漫游用户接入的原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启且参数“MME位置IP关联功能是否限制国际漫游用户”设置为“限制”时，MME会拒绝注册在其TA编组内的国际漫游用户，拒绝原因值由该参数指定。
MLMTINTRACAUSE|MME由于位置IP关联功能拒绝国内漫游用户接入的原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启且参数“MME位置IP关联功能限制国内漫游用户”设置为“限制”时，MME会拒绝注册在其TA编组内的国内漫游用户，拒绝原因值由该参数指定。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联功能的TA编组策略。 该参数不被其他命令引用，无其他意义。
命令举例 
修改位置IP关联功能的TA编组策略配置，其中TA编组规则标识为“1”，TA编组是否支持用户IP地址和位置关联为“否”。 
SET TAGROUP RULE:RULEID=1,TAGROUPIPLOC="NO"; 
父主题： [TA编组规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除TA编组规则配置(DEL TAGROUP RULE) 
#### 删除TA编组规则配置(DEL TAGROUP RULE) 
命令功能 
该命令用于删除位置IP关联功能的TA编组策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|TA编组规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联功能的TA编组策略标识，用于区分不同的位置IP关联功能的TA编组策略。
命令举例 
删除位置IP关联功能的TA编组策略配置，其中TA编组规则标识为“1”。 
DEL TAGROUP RULE:RULEID=1; 
父主题： [TA编组规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询TA编组规则配置(SHOW TAGROUP RULE) 
#### 查询TA编组规则配置(SHOW TAGROUP RULE) 
命令功能 
该命令用于查询已配置位置IP关联功能的TA编组策略。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|TA编组规则标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|位置IP关联功能的TA编组策略标识，用于区分不同的位置IP关联功能的TA编组策略。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|TA编组规则标识|参数可选性:任选参数；参数类型:整数。|位置IP关联功能的TA编组策略标识，用于区分不同的位置IP关联功能的TA编组策略。
TAGROUPIPLOC|TA编组是否支持用户IP地址和位置关联|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该位置IP关联TA编组是否启用位置IP关联功能。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，MME才需要对该位置IP关联TA编组下的移动用户启用IP位置关联功能。
IMPACTINTERROAM|MME位置IP关联功能是否限制国际漫游用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启，如果国际漫游用户在TA编组内：是：拒绝PDN连接建立。否：不拒绝PDN连接建立。
IMPACTINTRAROAM|MME位置IP关联功能是否限制国内漫游用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启时，MME是否限制在TA编组内的国内漫游用户访问数据网络。限制接入：限制其访问数据网络，拒绝用户注册，拒绝原因值取自参数“MME由于位置IP关联功能拒绝国内漫游用户接入的原因值”。同位置IP关联功能没有开启时处理：等同于位置IP功能没有开启时一样处理。同非漫游用户处理：等同于非漫游用户时一样处理。
MLMTINTERCAUSE|MME由于位置IP关联功能拒绝国际漫游用户接入的原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启且参数“MME位置IP关联功能是否限制国际漫游用户”设置为“限制”时，MME会拒绝注册在其TA编组内的国际漫游用户，拒绝原因值由该参数指定。
MLMTINTRACAUSE|MME由于位置IP关联功能拒绝国内漫游用户接入的原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|位置IP关联功能开启且参数“MME位置IP关联功能限制国内漫游用户”设置为“限制”时，MME会拒绝注册在其TA编组内的国内漫游用户，拒绝原因值由该参数指定。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户自定义别名，便于记忆和识别各位置IP关联功能的TA编组策略。 该参数不被其他命令引用，无其他意义。
命令举例 
查询位置IP关联功能的TA编组策略配置，查询所有已配置的位置IP关联功能的TA编组策略。 
SHOW TAGROUP RULE; 
`
命令 (No.1): SHOW TAGROUP RULE
操作维护         TA编组规则标识   TA编组是否支持用户IP地址和位置关联   MME位置IP关联功能是否限制国际漫游用户   MME位置IP关联功能是否限制国内漫游用户   MME由于位置IP关联功能拒绝国际漫游用户接入的原因值   MME由于位置IP关联功能拒绝国内漫游用户接入的原因值   用户别名
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1                是                                   是                                      限制接入                                PLMN不允许                                          PLMN不允许                                          aera1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.039 秒）。
` 
父主题： [TA编组规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 位置IP关联TA编组配置 
### 位置IP关联TA编组配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
通过配置TA编组，把同一个区（县）下的TA编为同一个位置IP关联的TA编组。一个TA编组与一个IP地址池一一对应，因此，UE在位置IP关联TA编组内移动时，不需要为UE的会话重新分配IP。 
注：
“位置IP关联TA编组配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
相关主题 
 
新增位置IP关联TA编组配置(ADD TAGROUP)
 
 
修改位置IP关联TA编组配置(SET TAGROUP)
 
 
删除位置IP关联TA编组配置(DEL TAGROUP)
 
 
查询位置IP关联TA编组配置(SHOW TAGROUP)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增位置IP关联TA编组配置(ADD TAGROUP) 
#### 新增位置IP关联TA编组配置(ADD TAGROUP) 
命令功能 
该命令用于增加位置IP关联的TA编组，一般同一个区（县）下的TA编为同一个位置IP关联的TA编组。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联TA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联TA编组编号，一般一个区（县）对应一个位置IP关联TA编组编号。
NAME|编组别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联TA编组。 该参数不被其他命令引用，无其他意义。
RULEID|TA编组规则标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|该位置IP关联TA编组是否启用位置IP关联。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，MME才需要对该位置IP关联TA编组下的移动用户启用IP位置关联功能。
TAI|跟踪区|参数可选性:必选参数；参数类型:复合参数|EPC网络对用户的位置管理采用跟踪区TA（Tracking Area）， 跟踪区的划分由无线侧确定。一个位置区可以对应一个跟踪区，也可进一步划分为几个跟踪区。每个跟踪区由一到多个小区组成，跟踪区之间没有重叠区域。跟踪区标识TAI（Tracking Area Identity )由MCC、MNC、TAC（Tracking Area Code）组成，一般运营商对于TAC的编码方式都有明确的规定，需要提前确定TAC的分配和编码，在运营中较少改动。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动”在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
TAC|跟踪区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC用于LTE网络中，在相同MCC和MNC下唯一标识TA（Tracking Area，跟踪区）的编号。
命令举例 
新增位置IP关联TA编组配置，其中位置IP关联TA编组编号为1，编组别名为group1，跟踪区为460-01-1ADC和460-01-1ADE，TA编组规则标识为1。 
ADD TAGROUP:GROUPID=1,NAME="group1",RULEID=1,TAI="460"-"01"-"1ADC"&"460"-"01"-"1ADE"; 
父主题： [位置IP关联TA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改位置IP关联TA编组配置(SET TAGROUP) 
#### 修改位置IP关联TA编组配置(SET TAGROUP) 
命令功能 
该命令用于修改位置IP关联的TA编组，一般在同一个区（县）下的TA发生改变时使用。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联TA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联TA编组编号，一般一个区（县）对应一个位置IP关联TA编组编号。
NAME|编组别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联TA编组。 该参数不被其他命令引用，无其他意义。
RULEID|TA编组规则标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|该位置IP关联TA编组是否启用位置IP关联。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，MME才需要对该位置IP关联TA编组下的移动用户启用IP位置关联功能。
命令举例 
修改位置IP关联TA编组配置，其中位置IP关联TA编组编号为1，TA编组规则标识为1。 
SET TAGROUP:GROUPID=1,RULEID=1; 
父主题： [位置IP关联TA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除位置IP关联TA编组配置(DEL TAGROUP) 
#### 删除位置IP关联TA编组配置(DEL TAGROUP) 
命令功能 
该命令用于删除位置IP关联的TA编组。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联TA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联TA编组编号，一般一个区（县）对应一个位置IP关联TA编组编号。
TAI|跟踪区|参数可选性:任选参数；参数类型:复合参数|EPC网络对用户的位置管理采用跟踪区TA（Tracking Area）， 跟踪区的划分由无线侧确定。一个位置区可以对应一个跟踪区，也可进一步划分为几个跟踪区。每个跟踪区由一到多个小区组成，跟踪区之间没有重叠区域。跟踪区标识TAI（Tracking Area Identity )由MCC、MNC、TAC（Tracking Area Code）组成，一般运营商对于TAC的编码方式都有明确的规定，需要提前确定TAC的分配和编码，在运营中较少改动。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动”在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
TAC|跟踪区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:4~4个字符。|TAC用于LTE网络中，在相同MCC和MNC下唯一标识TA（Tracking Area，跟踪区）的编号。
命令举例 
删除位置IP关联TA编组配置，其中位置IP关联TA编组编号为1，跟踪区为"460"-"01"-"1ADC"。 
DEL TAGROUP:GROUPID=1,TAI="460"-"01"-"1ADC"; 
父主题： [位置IP关联TA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询位置IP关联TA编组配置(SHOW TAGROUP) 
#### 查询位置IP关联TA编组配置(SHOW TAGROUP) 
命令功能 
该命令用于查询已配置位置IP关联的TA编组。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联TA编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|位置IP关联TA编组编号，一般一个区（县）对应一个位置IP关联TA编组编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GROUPID|位置IP关联TA编组编号|参数可选性:任选参数；参数类型:整数。|位置IP关联TA编组编号，一般一个区（县）对应一个位置IP关联TA编组编号。
NAME|编组别名|参数可选性:任选参数；参数类型:字符型。|用户自定义别名，便于记忆和识别各位置IP关联TA编组。 该参数不被其他命令引用，无其他意义。
RULEID|TA编组规则标识|参数可选性:任选参数；参数类型:整数。|该位置IP关联TA编组是否启用位置IP关联。只有在“支持用户IP地址和位置关联功能”License设置为“支持”，且该参数也设置为“支持”时，MME才需要对该位置IP关联TA编组下的移动用户启用IP位置关联功能。
TAI|跟踪区|参数可选性:任选参数；参数类型:字符型。|EPC网络对用户的位置管理采用跟踪区TA（Tracking Area）， 跟踪区的划分由无线侧确定。一个位置区可以对应一个跟踪区，也可进一步划分为几个跟踪区。每个跟踪区由一到多个小区组成，跟踪区之间没有重叠区域。跟踪区标识TAI（Tracking Area Identity )由MCC、MNC、TAC（Tracking Area Code）组成，一般运营商对于TAC的编码方式都有明确的规定，需要提前确定TAC的分配和编码，在运营中较少改动。
命令举例 
查询位置IP关联TA编组配置，其中位置IP关联TA编组编号为1。 
SHOW TAGROUP:GROUPID=1; 
`
命令 (No.10): SHOW TAGROUP:GROUPID=1;
操作维护         位置IP关联TA编组编号   编组别名   TA编组规则标识   跟踪区
--------------------------------------------------------------------------
复制 修改 删除   1                      group1     1                460-01-1ADC
复制 修改 删除   1                      group1     1                460-01-1ADE
--------------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.08 秒）。
` 
父主题： [位置IP关联TA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 位置IP关联5G TA编组配置 
### 位置IP关联5G TA编组配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
5G用户接入的每一个特定区域称为一个TA编组。
 
 
不同的TA编组，有不同的IP地址段。
 
 
功能描述 
5G TA编组配置，可以设置具体的5G TA区域和其对应的IP位置关联策略。 
注：
“位置IP关联5G TA编组配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
相关主题 
 
新增位置IP关联5G TA编组配置(ADD 5GTAGROUP)
 
 
修改位置IP关联5G TA编组配置(SET 5GTAGROUP)
 
 
删除位置IP关联5G TA编组配置(DEL 5GTAGROUP)
 
 
查询位置IP关联5G TA编组配置(SHOW 5GTAGROUP)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增位置IP关联5G TA编组配置(ADD 5GTAGROUP) 
#### 新增位置IP关联5G TA编组配置(ADD 5GTAGROUP) 
命令功能 
该命令用于增加位置IP关联的5G TA编组，一般同一个区（县）下的TA编为同一个位置IP关联的TA编组。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
TAGRPID5G|5G TA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联5G TA编组编号，一般一个区（县）对应一个位置IP关联5G TA编组编号。
TA5G|5G跟踪区|参数可选性:必选参数；参数类型:复合参数|5GC网络对用户的位置管理采用5G跟踪区（5G TA，5G Tracking Area），5G跟踪区的划分由无线侧确定。每个5G跟踪区由一到多个小区组成，5G跟踪区之间没有重叠区域。5G跟踪区标识5G TAI（5G Tracking Area Identity )由MCC、MNC、TAC（Tracking Area Code）组成，一般运营商对于TAC的编码方式都有明确的规定，需要提前确定TAC的分配和编码，在运营中较少改动。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动”在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
TAC|跟踪区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:6~6个字符。|TAC用于5GC网络中，在相同MCC和MNC下唯一标识5G TA（5G Tracking Area，5G 跟踪区）的编号。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指示用户名称。
命令举例 
新增位置IP关联5G TA编组配置，其中位置IP关联5G TA编组编号为1，编组别名为group1，跟踪区为460-01-005001。 
ADD 5GTAGROUP:TAGRPID5G=1,TA5G="460"-"01"-"005001",NAME="group1"; 
父主题： [位置IP关联5G TA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改位置IP关联5G TA编组配置(SET 5GTAGROUP) 
#### 修改位置IP关联5G TA编组配置(SET 5GTAGROUP) 
命令功能 
该命令用于修改位置IP关联的5G TA编组，一般在同一个区（县）下的5G TA发生改变时使用。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
TAGRPID5G|5G TA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联5G TA编组编号，一般一个区（县）对应一个位置IP关联5G TA编组编号。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指示用户名称。
命令举例 
修改位置IP关联5G TA编组配置，其中位置IP关联5G TA编组编号为1，编组别名为group11。 
SET 5GTAGROUP:TAGRPID5G=1,NAME="group11"; 
父主题： [位置IP关联5G TA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除位置IP关联5G TA编组配置(DEL 5GTAGROUP) 
#### 删除位置IP关联5G TA编组配置(DEL 5GTAGROUP) 
命令功能 
该命令用于删除位置IP关联的5G TA编组。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
TAGRPID5G|5G TA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联5G TA编组编号，一般一个区（县）对应一个位置IP关联5G TA编组编号。
TA5G|5G跟踪区|参数可选性:任选参数；参数类型:复合参数|5GC网络对用户的位置管理采用5G跟踪区（5G TA，5G Tracking Area），5G跟踪区的划分由无线侧确定。每个5G跟踪区由一到多个小区组成，5G跟踪区之间没有重叠区域。5G跟踪区标识5G TAI（5G Tracking Area Identity )由MCC、MNC、TAC（Tracking Area Code）组成，一般运营商对于TAC的编码方式都有明确的规定，需要提前确定TAC的分配和编码，在运营中较少改动。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|MCC（Mobile Country Code，移动国家码），用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|MNC（Mobile Network Code，移动网络号），用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动”在中国运营的GSN网络的MNC为01。MCC和MNC标识唯一的一个PLMN, 标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
TAC|跟踪区域码(HEX)|参数可选性:必选参数；参数类型:字符型；参数范围为:6~6个字符。|TAC用于5GC网络中，在相同MCC和MNC下唯一标识5G TA（5G Tracking Area，5G 跟踪区）的编号。
命令举例 
删除位置IP关联5G TA编组配置，其中位置IP关联5G TA编组编号为1。 
DEL 5GTAGROUP:TAGRPID5G=1; 
父主题： [位置IP关联5G TA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询位置IP关联5G TA编组配置(SHOW 5GTAGROUP) 
#### 查询位置IP关联5G TA编组配置(SHOW 5GTAGROUP) 
命令功能 
该命令用于查询已配置位置IP关联的5G TA编组。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
TAGRPID5G|5G TA编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|位置IP关联5G TA编组编号，一般一个区（县）对应一个位置IP关联5G TA编组编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TAGRPID5G|5G TA编组编号|参数可选性:必选参数；参数类型:整数。|位置IP关联5G TA编组编号，一般一个区（县）对应一个位置IP关联5G TA编组编号。
TA5G|5G跟踪区|参数可选性:必选参数；参数类型:字符型。|5GC网络对用户的位置管理采用5G跟踪区（5G TA，5G Tracking Area），5G跟踪区的划分由无线侧确定。每个5G跟踪区由一到多个小区组成，5G跟踪区之间没有重叠区域。5G跟踪区标识5G TAI（5G Tracking Area Identity )由MCC、MNC、TAC（Tracking Area Code）组成，一般运营商对于TAC的编码方式都有明确的规定，需要提前确定TAC的分配和编码，在运营中较少改动。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数用于指示用户名称。
命令举例 
查询位置IP关联5G TA编组配置，其中位置IP关联5G TA编组编号为1。 
SHOW 5GTAGROUP:TAGRPID5G=1; 
`
命令 (No.10): SHOW 5GTAGROUP:TAGRPID5G=1;
操作维护         位置IP关联5G TA编组编号   5G跟踪区             用户别名 
---------------------------------------------------------------------------
复制 修改 删除   1                         460-01-1ADCBB        group1     
复制 修改 删除   1                         460-01-1ADEBE        group1     
---------------------------------------------------------------------------
记录数 2
命令执行成功（耗时 0.08 秒）。
` 
父主题： [位置IP关联5G TA编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 控制开关配置 
### 控制开关配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
一个RA/TA编组与一个IP地址池一一对应，UE在位置IP关联的RA编组内或者TA编组内移动时，不需要为UE的会话重新分配IP；当用户所在编组发生变化，则需要为UE的会话重新分配IP。 
该命令用于开关配置，判断当UE在同一区域RA和TA编组之间移动时，是否为UE的会话重新分配IP。 
相关主题 
 
设置控制开关配置(SET IPLOC SWITCHCFG)
 
 
查询控制开关配置(SHOW IPLOC SWITCHCFG)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置控制开关配置(SET IPLOC SWITCHCFG) 
#### 设置控制开关配置(SET IPLOC SWITCHCFG) 
命令功能 
该命令用于设置“是否支持IP地址细分优化功能”。 
当UE在同一区域RA和TA编组之间移动时，如果不需要为UE的会话重新分配IP，使用该命令。 
注意事项 
该命令只适用于COMBO网元 
。
参数说明 
标识|名称|类型|说明
---|---|---|---
IPLOCRELATEOPTFLAG|是否支持IP地址细分优化功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE在同一区域RA和TA编组之间移动时，是否为UE的会话重新分配IP。取值含义：否：当UE在同一区域RA和TA编组之间移动时，需要为UE的会话重新分配IP。是：当UE在同一区域RA和TA编组之间移动时，不需要为UE的会话重新分配IP。
命令举例 
设置控制开关，设置“是否支持IP地址细分优化功能”为“是”。 
SET IPLOC SWITCHCFG:IPLOCRELATEOPTFLAG="YES"; 
父主题： [控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询控制开关配置(SHOW IPLOC SWITCHCFG) 
#### 查询控制开关配置(SHOW IPLOC SWITCHCFG) 
命令功能 
该命令用于查询“是否支持IP地址细分优化功能”。 
注意事项 
该命令只适用于COMBO网元 
。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IPLOCRELATEOPTFLAG|是否支持IP地址细分优化功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置当UE在同一区域RA和TA编组之间移动时，是否为UE的会话重新分配IP。取值含义：否：当UE在同一区域RA和TA编组之间移动时，需要为UE的会话重新分配IP。是：当UE在同一区域RA和TA编组之间移动时，不需要为UE的会话重新分配IP。
命令举例 
查询控制开关配置。 
SHOW IPLOC SWITCHCFG 
`
命令 (No.4): SHOW IPLOC SWITCHCFG
操作维护  是否支持IP地址细分优化功能
------------------------------------
修改      是
------------------------------------
记录数 1
命令执行成功（耗时 0.022 秒）。
` 
父主题： [控制开关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 区域编组配置 
### 区域编组配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
通过区域编组配置，可以将同一个区域内的RA编组和TA编组关联在一起。 
                当UE在同一区域编组内不同的RA编组和TA编组之间移动时，根据控制开关配置（
                [SET IPLOC SWITCHCFG]
                ），判断是否需要为UE的会话重新分配IP。
            
相关主题 
 
新增区域编组配置(ADD AREAGROUP)
 
 
修改区域编组配置(SET AREAGROUP)
 
 
删除区域编组配置(DEL AREAGROUP)
 
 
查询区域编组配置(SHOW AREAGROUP)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增区域编组配置(ADD AREAGROUP) 
#### 新增区域编组配置(ADD AREAGROUP) 
命令功能 
 该命令用于新增区域编组配置。 
当需要配置同一区域的位置IP关联RA编组和位置IP关联TA编组时，使用该命令。 
该命令执行成功后，同一区域的位置IP关联RA编组和位置IP关联TA编组会被关联配置。 
注意事项 
该命令的参数“位置IP关联RA编组编号”为网管配置的位置IP关联RA编组编号。通过SHOW RAGROUP命令可查询到“位置IP关联RA编组编号”。
 
 
该命令的参数“位置IP关联TA编组编号”为网管配置的位置IP关联TA编组编号。通过SHOW TAGROUP命令可查询到“位置IP关联TA编组编号”。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAGROUPID|位置IP关联区域编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|位置IP关联区域编组编号，一般一个区（县）对应一个位置IP关联区域编组编号。
RAGROUPID|位置IP关联RA编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|位置IP关联RA编组编号，一般一个区（县）对应一个位置IP关联RA编组编号，关联ADD RAGROUP中的位置IP关联RA编组编号。默认值0为无效值。
TAGROUPID|位置IP关联TA编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联TA编组编号，一般一个区（县）对应一个位置IP关联TA编组编号，关联ADD TAGROUP中的位置IP关联TA编组编号。默认值0为无效值。
TAGRPID5G|位置IP关联5G TA编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|位置IP关联5G TA编组编号，一般一个区（县）对应一个位置IP关联5G TA编组编号，关联ADD 5GTAGROUP中的位置IP关联5G TA编组编号。默认值0为无效值。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联区域编组。 该参数不被其他命令引用，无其他意义。
命令举例 
新增区域编组配置，其中位置IP关联RA编组编号为1，位置IP关联TA编组编号为1。 
ADD AREAGROUP:RAGROUPID=1,TAGROUPID=1; 
父主题： [区域编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改区域编组配置(SET AREAGROUP) 
#### 修改区域编组配置(SET AREAGROUP) 
命令功能 
该命令用于修改区域编组配置。 
当需要修改位置IP关联RA编组编号和位置IP关联TA编组编号时使用该命令。 
该命令执行成功后，能修改区域编组的位置IP关联RA编组编号和者位置IP关联TA编组编号。 
注意事项 
该命令的参数“位置IP关联RA编组编号”为网管配置的位置IP关联RA编组编号。通过SHOW RAGROUP命令可查询到“位置IP关联RA编组编号”。
 
 
该命令的参数“位置IP关联TA编组编号”为网管配置的位置IP关联TA编组编号。通过SHOW TAGROUP命令可查询到“位置IP关联TA编组编号”。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAGROUPID|位置IP关联区域编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联区域编组编号，一般一个区（县）对应一个位置IP关联区域编组编号。
RAGROUPID|位置IP关联RA编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|位置IP关联RA编组编号，一般一个区（县）对应一个位置IP关联RA编组编号，关联ADD RAGROUP中的位置IP关联RA编组编号。默认值0为无效值。
TAGROUPID|位置IP关联TA编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|位置IP关联TA编组编号，一般一个区（县）对应一个位置IP关联TA编组编号，关联ADD TAGROUP中的位置IP关联TA编组编号。默认值0为无效值。
TAGRPID5G|位置IP关联5G TA编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|位置IP关联5G TA编组编号，一般一个区（县）对应一个位置IP关联5G TA编组编号，关联ADD 5GTAGROUP中的位置IP关联5G TA编组编号。默认值0为无效值。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义别名，便于记忆和识别各位置IP关联区域编组。 该参数不被其他命令引用，无其他意义。
命令举例 
修改位置IP关联区域编组编号为1的配置数据，将位置IP关联TA编组编号修改为2。 
SET AREAGROUP:AREAGROUPID=1,TAGROUPID=2; 
父主题： [区域编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除区域编组配置(DEL AREAGROUP) 
#### 删除区域编组配置(DEL AREAGROUP) 
命令功能 
该命令用于删除区域编组配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAGROUPID|位置IP关联区域编组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~256。|位置IP关联区域编组编号，一般一个区（县）对应一个位置IP关联区域编组编号。
命令举例 
删除位置IP关联区域编组编号为1的配置数据。 
DEL AREAGROUP:AREAGROUPID=1; 
父主题： [区域编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询区域编组配置(SHOW AREAGROUP) 
#### 查询区域编组配置(SHOW AREAGROUP) 
命令功能 
该命令用于查询区域编组配置。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAGROUPID|位置IP关联区域编组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~256。|位置IP关联区域编组编号，一般一个区（县）对应一个位置IP关联区域编组编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
AREAGROUPID|位置IP关联区域编组编号|参数可选性:任选参数；参数类型:整数。|位置IP关联区域编组编号，一般一个区（县）对应一个位置IP关联区域编组编号。
RAGROUPID|位置IP关联RA编组编号|参数可选性:任选参数；参数类型:整数。|位置IP关联RA编组编号，一般一个区（县）对应一个位置IP关联RA编组编号，关联ADD RAGROUP中的位置IP关联RA编组编号。默认值0为无效值。
TAGROUPID|位置IP关联TA编组编号|参数可选性:任选参数；参数类型:整数。|位置IP关联TA编组编号，一般一个区（县）对应一个位置IP关联TA编组编号，关联ADD TAGROUP中的位置IP关联TA编组编号。默认值0为无效值。
TAGRPID5G|位置IP关联5G TA编组编号|参数可选性:任选参数；参数类型:整数。|位置IP关联5G TA编组编号，一般一个区（县）对应一个位置IP关联5G TA编组编号，关联ADD 5GTAGROUP中的位置IP关联5G TA编组编号。默认值0为无效值。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户自定义别名，便于记忆和识别各位置IP关联区域编组。 该参数不被其他命令引用，无其他意义。
命令举例 
查询所有区域编组配置。 
SHOW AREAGROUP 
`
命令 (No.21): SHOW AREAGROUP
操作维护         位置IP关联区域编组编号   位置IP关联RA编组编号   位置IP关联TA编组编号   位置IP关联5G TA编组编号   用户别名
--------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1                        1                      2                      2                      
--------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.043 秒）。
` 
父主题： [区域编组配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 省内用户IMSI号段配置 
### 省内用户IMSI号段配置 
背景知识 
为实现对特定区域（细化到区县）的移动用户使用移动互联网数据业务的管理，需要针对在特定时间、特定区域内的移动用户，分配特定的IP地址段内的IP地址。 
通过对特定的IP地址段内的IP地址进行管理，从而实现对特定区域内移动用户的管理。 
注：
 
2G/3G用户接入的每一个特定区域称为一个RA编组。
 
 
LTE用户接入的每一个特定区域称为一个TA编组。
 
 
功能描述 
如果SGSN/MME需要限制在RA编组内或TA编组内的国内漫游用户访问数据业务，则需要配置省内用户的IMSI号段，识别出国内漫游用户。如果国内用户IMSI不在省内IMSI号段内，则认为该用户是国内漫游用户。 
注：
“省内用户IMSI号段配置”功能需要License的支持，对应的License项为“支持用户IP地址和位置关联功能”。 
如果省内用户IMSI号段配置为空，则认为所有用户都是非省内用户。 
相关主题 
 
新增省内用户IMSI号段配置(ADD PROVINCE IMSI)
 
 
修改省内用户IMSI号段配置(SET PROVINCE IMSI)
 
 
删除省内用户IMSI号段配置(DEL PROVINCE IMSI)
 
 
查询省内用户IMSI号段配置(SHOW PROVINCE IMSI)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增省内用户IMSI号段配置(ADD PROVINCE IMSI) 
#### 新增省内用户IMSI号段配置(ADD PROVINCE IMSI) 
命令功能 
该命令用于配置省内用户IMSI号段。如果国内用户的IMSI不在省内IMSI号段内，则认为该用户是国内漫游用户。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指定省内用户的IMSI号段。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定省内用户IMSI号段的别名。
命令举例 
新增省内用户IMSI号段，其中IMSI号段为4600112345，用户别名为name1。 
ADD PROVINCE IMSI:IMSISEG="4600112345",NAME="name1"; 
父主题： [省内用户IMSI号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改省内用户IMSI号段配置(SET PROVINCE IMSI) 
#### 修改省内用户IMSI号段配置(SET PROVINCE IMSI) 
命令功能 
该命令用于修改省内用户IMSI号段，IMSI号段不能修改，只能修改用户别名。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指定省内用户的IMSI号段。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数用于指定省内用户IMSI号段的别名。
命令举例 
修改省内用户IMSI号段，将IMSI号段4600112345的用户别名改为test1。 
SET PROVINCE IMSI:IMSISEG="4600112345",NAME="test1"; 
父主题： [省内用户IMSI号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除省内用户IMSI号段配置(DEL PROVINCE IMSI) 
#### 删除省内用户IMSI号段配置(DEL PROVINCE IMSI) 
命令功能 
该命令用于删除省内用户IMSI号段。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数用于指定省内用户的IMSI号段。
命令举例 
删除省内用户IMSI号段，IMSI号段为4600112345。 
DEL PROVINCE IMSI:IMSISEG="4600112345"; 
父主题： [省内用户IMSI号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询省内用户IMSI号段配置(SHOW PROVINCE IMSI) 
#### 查询省内用户IMSI号段配置(SHOW PROVINCE IMSI) 
命令功能 
该命令用于查询已配置的省内用户IMSI号段。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数用于指定省内用户的IMSI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:任选参数；参数类型:字符型。|该参数用于指定省内用户的IMSI号段。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|该参数用于指定省内用户IMSI号段的别名。
命令举例 
查询省内用户IMSI号段。 
SHOW PROVINCE IMSI; 
`
命令 (No.1): SHOW PROVINCE IMSI
操作维护         IMSI号段     用户别名
--------------------------------------
复制 修改 删除   4600112345   test1
--------------------------------------
记录数 1
命令执行成功（耗时 0.063 秒）。
` 
父主题： [省内用户IMSI号段配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 基于数据APN的IP地址细分配置 
### 基于数据APN的IP地址细分配置 
背景知识 
运营商需要对终端用户进行管理：包括基于终端用户所在的TA及分组来为其分配IP地址，便于在网络侧，可以分析终端用户IP地址和终端用户位置的关联关系。 
基于终端用户的IP地址，可以知道终端用户目前所在的位置。在网关或防火墙侧，根据终端用户的IP地址进行管理操作，相当于根据终端用户的位置进行管理操作。 
运营商除了根据整个网元的粒度来对终端用户IP地址和位置的关联关系进行管理，还需要基于APN的粒度来对终端用户的IP地址和位置关联关系进行管理。 
MME已经支持基于IMS APN的IP地址和用户位置关联关系的管理，通过此功能，可以支持基于数据APN的粒度，对终端用户的IP地址和位置的关联关系进行管理。 
功能描述 
基于数据APN的IP地址细分配置，提供数据APN IP地址细分策略和数据APN IP地址细分配置。 
数据APN IP地址细分策略包括： 
 
MME支持基于数据APN的IP地址细分。
 
 
默认基于数据APN是否去PDN连接的设置。
 
 
数据APN IP地址细分配置包括：数据APN名称和对应的数据APN是否去PDN连接。 
相关主题 
 
设置数据APN IP地址细分策略(SET APN SUBDIVISION POLICY)
 
 
查询数据APN IP地址细分策略(SHOW APN SUBDIVISION POLICY)
 
 
新增数据APN IP地址细分配置(ADD APN SUBDIVISION)
 
 
修改数据APN IP地址细分配置(SET APN SUBDIVISION)
 
 
删除数据APN IP地址细分配置(DEL APN SUBDIVISION)
 
 
查询数据APN IP地址细分配置(SHOW APN SUBDIVISION)
 
 
父主题： [IP和位置关联配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置数据APN IP地址细分策略(SET APN SUBDIVISION POLICY) 
#### 设置数据APN IP地址细分策略(SET APN SUBDIVISION POLICY) 
命令功能 
该命令用于设置数据APN IP地址细分策略，包括MME支持基于数据APN的IP地址细分和默认基于数据APN是否去PDN连接的设置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPDAPNIPSUB|MME支持基于数据APN的IP地址细分|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于数据APN的IP地址细分。不支持：MME不支持基于数据APN的IP地址细分。支持：MME支持基于数据APN的IP地址细分。
DEFAPNDISC|默认基于数据APN是否去PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持基于数据APN的IP地址细分时，该参数用于设置MME默认基于数据APN是否去PDN连接。
命令举例 
设置数据APN IP地址细分策略。 
SET APN SUBDIVISION POLICY:MMESUPDAPNIPSUB="NO",DEFAPNDISC="YES"; 
父主题： [基于数据APN的IP地址细分配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询数据APN IP地址细分策略(SHOW APN SUBDIVISION POLICY) 
#### 查询数据APN IP地址细分策略(SHOW APN SUBDIVISION POLICY) 
命令功能 
该命令用于查询APN IP地址细分策略。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMESUPDAPNIPSUB|MME支持基于数据APN的IP地址细分|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持基于数据APN的IP地址细分。不支持：MME不支持基于数据APN的IP地址细分。支持：MME支持基于数据APN的IP地址细分。
DEFAPNDISC|默认基于数据APN是否去PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持基于数据APN的IP地址细分时，该参数用于设置MME默认基于数据APN是否去PDN连接。
命令举例 
查询数据APN IP地址细分策略。 
SHOW APN SUBDIVISION POLICY; 
`
命令 (No.7): SHOW APN SUBDIVISION POLICY
操作维护  MME支持基于数据APN的IP地址细分   默认基于数据APN是否去PDN连接
-----------------------------------------------------------------------
修改      不支持                           是
-----------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.056 秒）。
` 
父主题： [基于数据APN的IP地址细分配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增数据APN IP地址细分配置(ADD APN SUBDIVISION) 
#### 新增数据APN IP地址细分配置(ADD APN SUBDIVISION) 
命令功能 
 该命令用于新增数据APN名称和对应的数据APN是否去PDN连接的配置。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|当配置参数“默认基于数据APN是否去PDN连接（Default Disconnect PDN based on Data APN）”的设置值与APN粒度下的位置IP关联配置不同时，需要配置相应的数据APN。
APNDISC|APN是否去PDN连接|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|支持基于数据APN的IP地址细分时，该参数用于设置MME对特定数据APN是否去PDN连接。注意：此参数的设置值一般要求与配置参数“默认基于数据APN是否去PDN连接（Default Disconnect PDN based on Data APN）”的设置值不同。
命令举例 
新增数据APN IP地址细分配置，其中APN名称为zte.com，APN是否去PDN连接为否。 
ADD APN SUBDIVISION:APN="zte.com",APNDISC="NO"; 
父主题： [基于数据APN的IP地址细分配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改数据APN IP地址细分配置(SET APN SUBDIVISION) 
#### 修改数据APN IP地址细分配置(SET APN SUBDIVISION) 
命令功能 
该命令用于修改数据APN IP地址细分配置数据。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|当配置参数“默认基于数据APN是否去PDN连接（Default Disconnect PDN based on Data APN）”的设置值与APN粒度下的位置IP关联配置不同时，需要配置相应的数据APN。
APNDISC|APN是否去PDN连接|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|支持基于数据APN的IP地址细分时，该参数用于设置MME对特定数据APN是否去PDN连接。注意：此参数的设置值一般要求与配置参数“默认基于数据APN是否去PDN连接（Default Disconnect PDN based on Data APN）”的设置值不同。
命令举例 
修改数据APN IP地址细分配置。 
SET APN SUBDIVISION:APN="zte.com",APNDISC="YES"; 
父主题： [基于数据APN的IP地址细分配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除数据APN IP地址细分配置(DEL APN SUBDIVISION) 
#### 删除数据APN IP地址细分配置(DEL APN SUBDIVISION) 
命令功能 
该命令用于删除数据APN IP地址细分配置数据。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~62个字符。|当配置参数“默认基于数据APN是否去PDN连接（Default Disconnect PDN based on Data APN）”的设置值与APN粒度下的位置IP关联配置不同时，需要配置相应的数据APN。
命令举例 
删除APN名称为"zte.com"的数据APN IP地址细分配置记录。 
DEL APN SUBDIVISION:APN="zte.com"; 
父主题： [基于数据APN的IP地址细分配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询数据APN IP地址细分配置(SHOW APN SUBDIVISION) 
#### 查询数据APN IP地址细分配置(SHOW APN SUBDIVISION) 
命令功能 
该命令用于查询数据APN IP地址细分配置数据。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|当配置参数“默认基于数据APN是否去PDN连接（Default Disconnect PDN based on Data APN）”的设置值与APN粒度下的位置IP关联配置不同时，需要配置相应的数据APN。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|当配置参数“默认基于数据APN是否去PDN连接（Default Disconnect PDN based on Data APN）”的设置值与APN粒度下的位置IP关联配置不同时，需要配置相应的数据APN。
APNDISC|APN是否去PDN连接|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|支持基于数据APN的IP地址细分时，该参数用于设置MME对特定数据APN是否去PDN连接。注意：此参数的设置值一般要求与配置参数“默认基于数据APN是否去PDN连接（Default Disconnect PDN based on Data APN）”的设置值不同。
命令举例 
查询数据APN IP地址细分配置。 
SHOW APN SUBDIVISION; 
`
命令 (No.1): SHOW APN SUBDIVISION
APN名称                                         APN是否去PDN连接
----------------------------------------------------------------
zte.com                                         是
----------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.087 秒）。
` 
父主题： [基于数据APN的IP地址细分配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 话单存储空间配置 
## 话单存储空间配置 
背景知识 
当系统运行时，用户业务会持续产生话单，系统存储磁盘的占用空间会不断增加，最终导致磁盘可用空间不足，从而导致系统故障，可能的故障包括：配置数据存盘失败或者版本加载失败等。 
因此需要通过控制磁盘的剩余空间大小的方法对话单存储进行控制。当磁盘剩余空间少于配置的门限值并且系统还需要进行在本地存储话单的时候，则会丢弃掉新生成的话单文件（即不保存新产生的话单文件），此过程会一直持续，直到磁盘剩余空间高于停止门限为止。 
功能描述 
该配置用于控制磁盘的剩余空间大小，避免存储过多的话单造成磁盘空间不足导致配置数据存盘或者版本加载失败，当磁盘剩余空间少于配置门限值并且需要进行话单本地存储的时候，则丢弃掉新生成的话单文件。为了保证不频繁的启停话单丢弃操作，对于之前启动了话单丢弃操作，并且磁盘剩余空间未恢复到停止丢弃门限的情况下会继续保持话单丢弃操作，直到磁盘剩余空间高于停止门限为止。其中门限配置的是开始丢弃话单的磁盘剩余空间百分比以及停止丢弃话单的磁盘剩余空间百分比。 
相关主题 
 
设置话单存储空间(SET BILLSPACE)
 
 
查询话单存储空间(SHOW BILLSPACE)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置话单存储空间(SET BILLSPACE) 
### 设置话单存储空间(SET BILLSPACE) 
命令功能 
该命令用于设置话单存储空间配置，配置用于控制磁盘的剩余空间大小，避免存储过多的话单造成磁盘空间不足导致配置数据存盘或者版本加载失败。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
DISCARD|丢弃话单的磁盘剩余空间(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|磁盘剩余空间少于配置的“丢弃话单的磁盘剩余空间”门限值并且需要进行话单本地存储的时候，则开始丢弃掉新生成的话单文件。
STORE|存储话单的磁盘剩余空间(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~30。|磁盘剩余空间多于配置的“存储话单的磁盘剩余空间”门限值并且需要进行话单本地存储的时候，则停止丢弃掉新生成的话单文件。
命令举例 
设置话单存储空间配置，丢弃话单的磁盘剩余空间(%)为5存储话单的磁盘剩余空间(%)为6。 
SET BILLSPACE:DISCARD=5,STORE=6; 
父主题： [话单存储空间配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询话单存储空间(SHOW BILLSPACE) 
### 查询话单存储空间(SHOW BILLSPACE) 
命令功能 
该命令用于查询话单存储空间配置。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DISCARD|丢弃话单的磁盘剩余空间(%)|参数可选性:任选参数；参数类型:整数。|磁盘剩余空间少于配置的“丢弃话单的磁盘剩余空间”门限值并且需要进行话单本地存储的时候，则开始丢弃掉新生成的话单文件。
STORE|存储话单的磁盘剩余空间(%)|参数可选性:任选参数；参数类型:整数。|磁盘剩余空间多于配置的“存储话单的磁盘剩余空间”门限值并且需要进行话单本地存储的时候，则停止丢弃掉新生成的话单文件。
命令举例 
查询话单存储空间配置。 
SHOW BILLSPACE; 
`
命令 (No.3): SHOW BILLSPACE
操作维护  丢弃话单的磁盘剩余空间(%)   存储话单的磁盘剩余空间(%)
---------------------------------------------------------------
修改      5                           6
---------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.023 秒）。
` 
父主题： [话单存储空间配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 基于TAC的Gb加密算法配置 
## 基于TAC的Gb加密算法配置 
背景知识 
            
            Gb接入加密：对于SGSN Gb接入，当MS发起附着和路由更新请求时，SGSN确认网络侧LLC加密开关已经打开，则根据手机支持的GPRS加密算法和SGSN支持的GPRS加密算法取交集，确定最终使用的GPRS加密算法。Gb口的信令和数据就使用密文进行交互，保证用户接入的安全性。
        
功能描述 
一般情况下，启用Gb接入加密时，对所有用户采用同一种加密算法。但如果需要根据终端类型配置不同的加密算法时，可以通过设置“基于TAC的Gb加密算法”实现。 
IMEI中的TAC为类型分配代码，共8个十进制数值，其中前两位代表不同的分配机构，后面6位区分不同的机器类型。不同的手机型号对应不同的TAC，因此根据TAC就可以配置不同手机型号支持的GPRS加密算法。 
相关主题 
 
新增基于TAC的Gb加密算法配置(ADD TAC GEA)
 
 
修改基于TAC的Gb加密算法配置(SET TAC GEA)
 
 
删除基于TAC的Gb加密算法配置(DEL TAC GEA)
 
 
查询基于TAC的Gb加密算法配置(SHOW TAC GEA)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增基于TAC的Gb加密算法配置(ADD TAC GEA) 
### 新增基于TAC的Gb加密算法配置(ADD TAC GEA) 
命令功能 
该命令用于新增基于TAC的Gb加密算法配置。当运营商需要根据终端类型设置不同的Gb加密算法时，使用此命令。 
注意事项 
本功能受安全变量“支持基于IMEI配置Gb加密算法”控制。该安全变量属于“安全相关配置”，可以通过命令[SHOW SECURITY PARAMETER]查看。
参数说明 
标识|名称|类型|说明
---|---|---|---
TAC|类型分配码|参数可选性:必选参数；参数类型:字符型；参数范围为:8~8个字符。|IMEI中的类型分配码。TAC采用8个十进制数值表示，前两位代表不同的分配机构，后6位区分不同的机器类型。不同的手机型号TAC不同。
GEA1|GPRS加密算法1|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法1（GEA1）。
PRIORGEA1|GPRS加密算法1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:2。|GPRS加密算法1的优先级。
GEA2|GPRS加密算法2|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法2（GEA2）。
PRIORGEA2|GPRS加密算法2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:3。|GPRS加密算法2的优先级。
GEA3|GPRS加密算法3|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法3（GEA3）。
PRIORGEA3|GPRS加密算法3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:1。|GPRS加密算法3的优先级。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
新增基于TAC的Gb加密算法配置，类型分配码为46012665，支持GPRS加密算法1，支持GPRS加密算法2，支持GPRS加密算法3。 
ADD TAC GEA:TAC="46012665",GEA1="ON",GEA2="ON",GEA3="ON";
 
父主题： [基于TAC的Gb加密算法配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改基于TAC的Gb加密算法配置(SET TAC GEA) 
### 修改基于TAC的Gb加密算法配置(SET TAC GEA) 
命令功能 
该命令用于修改基于TAC的Gb加密算法配置。可以修改该TAC对Gb加密算法1、算法2、算法3的支持情况。 
注意事项 
本功能受安全变量“支持基于IMEI配置Gb加密算法”控制。该安全变量属于“安全相关配置”，可以通过命令[SHOW SECURITY PARAMETER]查看。
参数说明 
标识|名称|类型|说明
---|---|---|---
TAC|类型分配码|参数可选性:必选参数；参数类型:字符型；参数范围为:8~8个字符。|IMEI中的类型分配码。TAC采用8个十进制数值表示，前两位代表不同的分配机构，后6位区分不同的机器类型。不同的手机型号TAC不同。
GEA1|GPRS加密算法1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法1（GEA1）。
PRIORGEA1|GPRS加密算法1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法1的优先级。
GEA2|GPRS加密算法2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法2（GEA2）。
PRIORGEA2|GPRS加密算法2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法2的优先级。
GEA3|GPRS加密算法3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法3（GEA3）。
PRIORGEA3|GPRS加密算法3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法3的优先级。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
修改基于TAC的Gb加密算法配置，类型分配码为46012665，支持GPRS加密算法1，支持GPRS加密算法2，不支持GPRS加密算法3。 
SET TAC GEA:TAC="46012665",GEA1="ON",GEA2="ON",GEA3="OFF";
 
父主题： [基于TAC的Gb加密算法配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除基于TAC的Gb加密算法配置(DEL TAC GEA) 
### 删除基于TAC的Gb加密算法配置(DEL TAC GEA) 
命令功能 
该命令用于删除基于TAC的Gb加密算法配置。删除后，此TAC对应的加密算法不再生效，系统采用全局的Gb加密算法（查询命令为：[SHOW GPRS ENCRYPTION]）。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
TAC|类型分配码|参数可选性:必选参数；参数类型:字符型；参数范围为:8~8个字符。|IMEI中的类型分配码。TAC采用8个十进制数值表示，前两位代表不同的分配机构，后6位区分不同的机器类型。不同的手机型号TAC不同。
命令举例 
删除基于TAC的Gb加密算法配置，类型分配码为46012665记录。
 
DEL TAC GEA:TAC="46012665";
 
父主题： [基于TAC的Gb加密算法配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询基于TAC的Gb加密算法配置(SHOW TAC GEA) 
### 查询基于TAC的Gb加密算法配置(SHOW TAC GEA) 
命令功能 
该命令用于查询SGSN网元已配置的基于TAC的Gb加密算法。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
TAC|类型分配码|参数可选性:任选参数；参数类型:字符型；参数范围为:8~8个字符。|IMEI中的类型分配码。TAC采用8个十进制数值表示，前两位代表不同的分配机构，后6位区分不同的机器类型。不同的手机型号TAC不同。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TAC|类型分配码|参数可选性:任选参数；参数类型:字符型。|IMEI中的类型分配码。TAC采用8个十进制数值表示，前两位代表不同的分配机构，后6位区分不同的机器类型。不同的手机型号TAC不同。
GEA1|GPRS加密算法1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法1（GEA1）。
PRIORGEA1|GPRS加密算法1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法1的优先级。
GEA2|GPRS加密算法2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法2（GEA2）。
PRIORGEA2|GPRS加密算法2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法2的优先级。
GEA3|GPRS加密算法3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法3（GEA3）。
PRIORGEA3|GPRS加密算法3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法3的优先级。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
查询已经配置的基于TAC的Gb加密算法配置信息 
SHOW TAC GEA; 
`
命令 (No.1): SHOW TAC GEA
操作维护         类型分配码   GPRS加密算法1   GPRS加密算法2   GPRS加密算法3   用户别名
--------------------------------------------------------------------------------------
复制 修改 删除   46012665     支持            支持            支持            
--------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.023 秒）。
` 
父主题： [基于TAC的Gb加密算法配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 合法区域接入限制配置 
## 合法区域接入限制配置 
背景知识 
为实现对特定区域的特定移动用户使用移动互联网数据业务的管理，需要针对在特定区域内的特定移动用户，设置特定的接入策略。 
功能描述 
合法区域接入限制配置用于查询功能开关、设置管理策略等。 
相关主题 
 
接入限制策略配置
 
 
本地GGSN配置
 
 
接入限制目标GGSN配置
 
 
查询接入限制开关(SHOW ISMCCGXFLAG)
 
 
接入限制区域配置
 
 
接入限制规则配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 接入限制策略配置 
### 接入限制策略配置 
背景知识 
            
            为实现对特定区域的特定移动用户使用特定移动互联网数据业务的管理，需要针对在特定时间，特定区域内的特定移动用户或用户接入的特定业务，设置特定的接入策略。
        
功能描述 
            
            接入限制区域配置用于设置特定时间范围、特定移动用户范围等。
        
相关主题 
 
设置接入限制策略(SET CNLAR POLICY)
 
 
查询接入限制策略(SHOW CNLAR POLICY)
 
 
父主题： [合法区域接入限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置接入限制策略(SET CNLAR POLICY) 
#### 设置接入限制策略(SET CNLAR POLICY) 
命令功能 
设置接入限制策略。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
POLICY|策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|策略
DRAU|路由更新时是否分离受限用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|路由更新时是否分离受限用户
命令举例 
设置接入限制策略，策略为PASS，路由更新时是否分离受限用户为NO。 
SET CNLAR POLICY:POLICY="PASS",DRAU="NO"; 
父主题： [接入限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询接入限制策略(SHOW CNLAR POLICY) 
#### 查询接入限制策略(SHOW CNLAR POLICY) 
命令功能 
查询接入限制策略。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
POLICY|策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|策略
DRAU|路由更新时是否分离受限用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|路由更新时是否分离受限用户
命令举例 
查询接入限制策略。 
SHOW CNLAR POLICY 
`
(No.1) : SHOW CNLAR POLICY:
-----------------NFS_MMESGSN_0----------------
操作维护       策略 路由更新时是否分离受限用户 
---------------------------------------------------------
修改           不管控 否                                                
---------------------------------------------------------
记录数：1
执行成功 开始时间:2020-08-10 14:43:42 耗时: 0.335 秒
` 
父主题： [接入限制策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 本地GGSN配置 
### 本地GGSN配置 
背景知识 
            
            为实现对特定区域的特定移动用户使用移动互联网数据业务的管理，需要针对在特定时间，特定区域内的特定移动用户，设置特定的接入策略。
        
功能描述 
            
            本地GGSN配置用于设置把本地GGSN，特定时间、特定区域的特定移动用户的PDP激活，在接入策略为“转本地GGSN”时，使用本地GGSN激活PDP。
        
相关主题 
 
新增本地GGSN配置(ADD CNLAR LGGSN)
 
 
删除本地GGSN配置(DEL CNLAR LGGSN)
 
 
查询本地GGSN配置(SHOW CNLAR LGGSN)
 
 
父主题： [合法区域接入限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增本地GGSN配置(ADD CNLAR LGGSN) 
#### 新增本地GGSN配置(ADD CNLAR LGGSN) 
命令功能 
新增本地GGSN配置
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN地址|参数可选性:必选参数；参数类型:地址|GGSN地址
MASK|掩码|参数可选性:必选参数；参数类型:整数；参数范围为:0~128。|掩码
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名
命令举例 
新增本地GGSN配置，IP为0:0:0:0:0:0:0:10，掩码为0，用户别名为example。 
ADD CNLAR LGGSN:IP="0:0:0:0:0:0:0:10",MASK=0,NAME="example"; 
父主题： [本地GGSN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除本地GGSN配置(DEL CNLAR LGGSN) 
#### 删除本地GGSN配置(DEL CNLAR LGGSN) 
命令功能 
删除本地GGSN配置
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN地址|参数可选性:必选参数；参数类型:地址|GGSN地址
命令举例 
删除本地GGSN配置，IP为0:0:0:0:0:0:0:10。 
DEL CNLAR LGGSN:IP="0:0:0:0:0:0:0:10"; 
父主题： [本地GGSN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询本地GGSN配置(SHOW CNLAR LGGSN) 
#### 查询本地GGSN配置(SHOW CNLAR LGGSN) 
命令功能 
查询本地GGSN配置
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN地址|参数可选性:任选参数；参数类型:地址|GGSN地址
MASK|掩码|参数可选性:任选参数；参数类型:整数。|掩码
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户别名
命令举例 
查询本地GGSN配置。 
SHOW CNLAR LGGSN 
`
(No.1) : SHOW CNLAR LGGSN:
-----------------NFS_MMESGSN_0----------------
操作维护       GGSN地址 掩码 用户别名 
----------------------------------------------------------------------------
复制  删除     0:0:0:0:0:0:0:10 0 example                                                 
----------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2020-08-10 14:43:42 耗时: 0.335 秒
` 
父主题： [本地GGSN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 接入限制目标GGSN配置 
### 接入限制目标GGSN配置 
背景知识 
            
            为实现对特定区域的特定移动用户使用移动互联网数据业务的管理，需要针对在特定时间，特定区域内的特定移动用户，设置特定的接入策略。
        
功能描述 
            
            接入限制区域配置用于设置特定时间范围、特定移动用户范围等。
        
相关主题 
 
新增接入限制目标GGSN配置(ADD CNLAR DGGSN)
 
 
删除接入限制目标GGSN配置(DEL CNLAR DGGSN)
 
 
查询接入限制目标GGSN配置(SHOW CNLAR DGGSN)
 
 
父主题： [合法区域接入限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增接入限制目标GGSN配置(ADD CNLAR DGGSN) 
#### 新增接入限制目标GGSN配置(ADD CNLAR DGGSN) 
命令功能 
新增管控目标GGSN配置
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN地址|参数可选性:必选参数；参数类型:地址|GGSN地址
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名
命令举例 
新增管控目标GGSN配置 
ADD CNLAR DGGSN:IP="0:0:0:0:0:0:0:10",NAME=""; 
父主题： [接入限制目标GGSN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除接入限制目标GGSN配置(DEL CNLAR DGGSN) 
#### 删除接入限制目标GGSN配置(DEL CNLAR DGGSN) 
命令功能 
删除管控目标GGSN配置
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN地址|参数可选性:必选参数；参数类型:地址|GGSN地址
命令举例 
删除管控目标GGSN配置 
DEL CNLAR DGGSN:IP="0:0:0:0:0:0:0:10"; 
父主题： [接入限制目标GGSN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询接入限制目标GGSN配置(SHOW CNLAR DGGSN) 
#### 查询接入限制目标GGSN配置(SHOW CNLAR DGGSN) 
命令功能 
查询管控目标GGSN配置
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GGSN地址|参数可选性:任选参数；参数类型:地址|GGSN地址
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户别名
命令举例 
SHOW CNLAR DGGSN 
`
(No.1) : SHOW CNLAR DGGSN:
-----------------NFS_MMESGSN_0----------------
操作维护       GGSN地址 用户别名 
---------------------------------------------------------
复制 删除      0:0:0:0:0:0:0:10                                                  
---------------------------------------------------------
记录数：1
执行成功 开始时间:2020-08-10 14:43:42 耗时: 0.335 秒
` 
父主题： [接入限制目标GGSN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询接入限制开关(SHOW ISMCCGXFLAG) 
### 查询接入限制开关(SHOW ISMCCGXFLAG) 
命令功能 
本参命令用于查询接入限制开关。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RETCODE|执行结果码|参数可选性:任选参数；参数类型:整数。|执行结果码
FLAG|Gx口开关状态标记|参数可选性:任选参数；参数类型:整数。|Gx口开关状态标记
RESULT|执行结果|参数可选性:任选参数；参数类型:字符型。|执行结果
命令举例 
查询接入限制开关。 
SHOW ISMCCGXFLAG 
`
(No.1) : SHOW ISMCCGXFLAG:
-----------------NFS_MMESGSN_0----------------
Gx口开关状态标记 
------------------
0                 
------------------
记录数：1
执行结果 
-------
Pass   
-------
记录数：1
执行结果码
------------
0           
------------
记录数：1
执行成功 开始时间:2020-08-10 14:43:42 耗时: 0.335 秒
` 
父主题： [合法区域接入限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 接入限制区域配置 
### 接入限制区域配置 
背景知识 
            
            为实现对特定区域的特定移动用户使用移动互联网数据业务的管理，需要针对在特定区域内的特定移动用户，设置特定的接入策略。
        
功能描述 
            
            接入限制区域配置用于设置需要管理的特定区域。
        
相关主题 
 
新增接入限制区域配置(ADD SMCCSCA)
 
 
新增接入限制区域位置项配置(ADD SMCCSCAITEM)
 
 
修改接入限制区域配置(SET SMCCSCA)
 
 
删除接入限制区域配置(DEL SMCCSCA)
 
 
查询接入限制区域配置(SHOW ISMCCSCA)
 
 
父主题： [合法区域接入限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增接入限制区域配置(ADD SMCCSCA) 
#### 新增接入限制区域配置(ADD SMCCSCA) 
命令功能 
新增接入限制区域
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAID|区域索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|区域索引
AREANAME|区域名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|区域名称
AREADESCRP|区域描述|参数可选性:任选参数；参数类型:字符型；参数范围为:0~200个字符。|区域描述
NETTYPE|区域归属网络类型|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|区域归属网络类型
FLAG|对象追加标记|参数可选性:必选参数；参数类型:整数；参数范围为:0~1。|对象追加标记
AREAITEMS|区域位置项列表|参数可选性:必选参数；参数类型:复合参数|区域位置项列表
ITEMID|位置项编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|位置项编号
ITEMNAME|位置项名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|位置项名称
ITEMTYPE|位置项标识类型|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|位置项标识类型
ITEMVALUE|位置项标识值|参数可选性:必选参数；参数类型:字符型；参数范围为:1~200个字符。|位置项标识值
ITEMNETTYPE|归属网络类型|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|归属网络类型
命令举例 
新增接入限制区域 
ADD SMCCSCA:AREAID=1,AREANAME="1",AREADESCRP="0",NETTYPE=2,FLAG=0,AREAITEMS=1-"1"-3-"1.1.1.1"-2; 
父主题： [接入限制区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增接入限制区域位置项配置(ADD SMCCSCAITEM) 
#### 新增接入限制区域位置项配置(ADD SMCCSCAITEM) 
命令功能 
增加接入限制区域位置项
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAID|区域索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|区域索引
FLAG|对象追加标记|参数可选性:必选参数；参数类型:整数；参数范围为:0~1。|对象追加标记
AREAITEMS|区域位置项列表|参数可选性:必选参数；参数类型:复合参数|区域位置项列表
ITEMID|位置项编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|位置项编号
ITEMNAME|位置项名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|位置项名称
ITEMTYPE|位置项标识类型|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|位置项标识类型
ITEMVALUE|位置项标识值|参数可选性:必选参数；参数类型:字符型；参数范围为:1~200个字符。|位置项标识值
ITEMNETTYPE|归属网络类型|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|归属网络类型
命令举例 
增加接入限制区域位置项 
ADD SMCCSCAITEM:AREAID=1,FLAG=0,AREAITEMS="1"-""-"2"-"4"-"3"; 
父主题： [接入限制区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改接入限制区域配置(SET SMCCSCA) 
#### 修改接入限制区域配置(SET SMCCSCA) 
命令功能 
修改接入限制区域
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAID|区域索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|区域索引
AREANAME|区域名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|区域名称
AREADESCRP|区域描述|参数可选性:任选参数；参数类型:字符型；参数范围为:0~200个字符。|区域描述
NETTYPE|区域归属网络类型|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|区域归属网络类型
命令举例 
修改接入限制区域 
SET SMCCSCA:AREAID=1,AREANAME="AREA_1",NETTYPE=2; 
父主题： [接入限制区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除接入限制区域配置(DEL SMCCSCA) 
#### 删除接入限制区域配置(DEL SMCCSCA) 
命令功能 
删除接入限制区域
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAID|区域索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|区域索引
命令举例 
删除接入限制区域 
DEL SMCCSCA:AREAID="1"; 
父主题： [接入限制区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询接入限制区域配置(SHOW ISMCCSCA) 
#### 查询接入限制区域配置(SHOW ISMCCSCA) 
命令功能 
查询接入限制区域
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
AREAID|区域索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|区域索引
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RETCODE|执行结果码|参数可选性:任选参数；参数类型:整数。|执行结果码
RESULT|执行结果|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|执行结果
命令举例 
查询接入限制区域。 
SHOW ISMCCSCA 
`
(No.1) : SHOW ISMCCSCA:AREAID="1":
-----------------NFS_MMESGSN_0----------------
执行结果                                                                                                                                    
--------------------------------------------------------------------------------------------------------------------------------------------
sftp://ems:********@10.228.62.189:29029/Nfdata/uMAC_MME_B11/vru-mmesgsn-oam-dba/uMAC_MME_B11/AMM/CMDBA/emsent/smcc/sca-query-result.xml 
--------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行结果码 
-----------
0          
-----------
记录数：1
执行成功 开始时间:2020-08-10 14:43:42 耗时: 0.335 秒
` 
父主题： [接入限制区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 接入限制规则配置 
### 接入限制规则配置 
背景知识 
            
            为实现对特定区域的特定移动用户使用特定移动互联网数据业务的管理，需要针对在特定时间，特定区域内的特定移动用户或用户接入的特定业务，设置特定的接入策略。
        
功能描述 
            
            接入限制区域配置用于设置特定时间范围、特定移动用户范围等。
        
相关主题 
 
新增接入限制规则配置(ADD SMCCSCR)
 
 
新增接入限制规则位置项配置(ADD SMCCSCRITEM)
 
 
修改接入限制规则配置(SET SMCCSCR)
 
 
删除接入限制规则配置(DEL SMCCSCR)
 
 
查询接入限制规则配置(SHOW ISMCCSCR)
 
 
设置接入限制规则状态配置(SET SMCCSCROPSTAT)
 
 
父主题： [合法区域接入限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增接入限制规则配置(ADD SMCCSCR) 
#### 新增接入限制规则配置(ADD SMCCSCR) 
命令功能 
新增接入限制规则
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|规则索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|规则索引
RULENAME|规则名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|规则名称
RULEDESCRP|规则描述|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|规则描述
CREATOR|创建人|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|创建人
CREATETIME|创建时间|参数可选性:必选参数；参数类型:整数；参数范围为:0~562949953421311。|创建时间
AREAIDS|管控区域索引列表|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|管控区域索引列表
USERGRPIDS|管控用户群索引列表|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|管控用户群索引列表
NETTYPE|归属网络类型|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|归属网络类型
STARTTIME|管控规则开始时间|参数可选性:任选参数；参数类型:整数；参数范围为:0~9223372036854775807。|接入限制规则开始时间
ENDTIME|管控规则结束时间|参数可选性:任选参数；参数类型:整数；参数范围为:0~9223372036854775807。|接入限制规则结束时间
FLAG|对象追加标记|参数可选性:必选参数；参数类型:整数；参数范围为:0~1。|对象追加标记
SERVITEMS|业务项列表|参数可选性:必选参数；参数类型:复合参数|业务项列表
SERVNO|业务类型编号|参数可选性:必选参数；参数类型:整数；参数范围为:0~32768。|业务类型编号
SERVVALUE|业务类型值|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|业务类型值
SERVNETTYPE|归属网络类型|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|归属网络类型
SERVFLAG|业务管控标记|参数可选性:必选参数；参数类型:整数；参数范围为:0~1。|业务管控标记
命令举例 
新增接入限制规则。 
ADD SMCCSCR:RULEID=1,RULENAME="RULE_1",RULEDESCRP="RULE_1",CREATOR="SMCC",CREATETIME=12300,AREAIDS=1,USERGRPIDS=1,NETTYPE=2,STARTTIME=350000,ENDTIME=4600000,FLAG=0,SERVITEMS=4-"4"-2-0; 
父主题： [接入限制规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增接入限制规则位置项配置(ADD SMCCSCRITEM) 
#### 新增接入限制规则位置项配置(ADD SMCCSCRITEM) 
命令功能 
增加接入限制规则业务项
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|规则索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|规则索引
FLAG|对象追加标记|参数可选性:必选参数；参数类型:整数；参数范围为:0~1。|对象追加标记
SERVITEMS|业务项列表|参数可选性:必选参数；参数类型:复合参数|业务项列表
SERVNO|业务类型编号|参数可选性:必选参数；参数类型:整数；参数范围为:0~32768。|业务类型编号
SERVVALUE|业务类型值|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|业务类型值
SERVNETTYPE|归属网络类型|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|归属网络类型
SERVFLAG|业务管控标记|参数可选性:必选参数；参数类型:整数；参数范围为:0~1。|业务管控标记
命令举例 
增加接入限制规则业务项 
ADD SMCCSCRITEM:RULEID=1,FLAG=0,SERVITEMS="0"-"1"-"1"-"0"&"0"-"1"-"1"-"0"; 
父主题： [接入限制规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改接入限制规则配置(SET SMCCSCR) 
#### 修改接入限制规则配置(SET SMCCSCR) 
命令功能 
修改接入限制规则
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|规则索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|规则索引
RULENAME|规则名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|规则名称
RULEDESCRP|规则描述|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|规则描述
CREATOR|创建人|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|创建人
AREAIDS|管控区域索引列表|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|管控区域索引列表
USERGRPIDS|管控用户群索引列表|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|管控用户群索引列表
NETTYPE|归属网络类型|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|归属网络类型
STARTTIME|管控规则开始时间|参数可选性:任选参数；参数类型:整数；参数范围为:0~9223372036854775807。|接入限制规则开始时间
ENDTIME|管控规则结束时间|参数可选性:任选参数；参数类型:整数；参数范围为:0~9223372036854775807。|接入限制规则结束时间
命令举例 
修改接入限制规则 
SET SMCCSCR:RULEID=1,AREAIDS=1,USERGRPIDS=1,NETTYPE=2; 
父主题： [接入限制规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除接入限制规则配置(DEL SMCCSCR) 
#### 删除接入限制规则配置(DEL SMCCSCR) 
命令功能 
删除接入限制规则
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|规则索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|规则索引
命令举例 
删除接入限制规则 
DEL SMCCSCR:RULEID="1"; 
父主题： [接入限制规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询接入限制规则配置(SHOW ISMCCSCR) 
#### 查询接入限制规则配置(SHOW ISMCCSCR) 
命令功能 
查询接入限制规则
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|规则索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|规则索引
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RETCODE|执行结果码|参数可选性:任选参数；参数类型:整数。|执行结果码
RESULT|执行结果|参数可选性:任选参数；参数类型:字符型；参数范围为:0~500个字符。|执行结果
命令举例 
查询接入限制规则。 
SHOW ISMCCSCR 
`
(No.1) : SHOW ISMCCSCR:RULEID="1":
-----------------NFS_MMESGSN_0----------------
执行结果 
---------
无数据   
---------
记录数：1
执行结果码 
-----------
2          
-----------
记录数：1
执行成功开始时间:2021-01-05 16:06:57 耗时: 0.777 秒
` 
父主题： [接入限制规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置接入限制规则状态配置(SET SMCCSCROPSTAT) 
#### 设置接入限制规则状态配置(SET SMCCSCROPSTAT) 
命令功能 
设置接入限制规则状态
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RULEID|规则索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|规则索引
OPSTATUS|规则操作状态|参数可选性:必选参数；参数类型:整数；参数范围为:0~1。|规则操作状态
命令举例 
设置接入限制规则状态 
SET SMCCSCROPSTAT:RULEID=1,OPSTATUS=0; 
父主题： [接入限制规则配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## eNodeB告警配置 
## eNodeB告警配置 
背景知识 
正常情况下，eNodeB局向链路断链时，MME上报eNodeB断链告警，告警码为：2114322696。当网络中存在一些异常情况时，需要进行一些特殊处理： 
 
对于少量不稳定的eNodeB，可能会长期处于断链状态无法恢复，如果这些eNodeB不需要关注，则可以通过告警过滤配置屏蔽这些eNodeB的断链告警。
 
 
如果eNodeB断链时间太长造成告警一直无法恢复时，需要设定这些告警达到一定时间即恢复。
 
 
功能描述 
eNodeB告警配置包括： 
 
eNodeB断链告警过滤配置：主要应用于屏蔽eNodeB断链告警的场景。
 
 
eNodeB告警参数配置：主要应用于eNodeB断链告警长期无法恢复的场景。
 
 
相关主题 
 
eNodeB告警参数配置
 
 
eNodeB断链告警过滤配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### eNodeB告警参数配置 
### eNodeB告警参数配置 
背景知识 
正常情况下，eNodeB局向链路断链时，MME上报eNodeB断链告警，告警码为：2114322696。 
当网络中存在一些异常情况，如果eNodeB断链时间太长造成告警一直无法恢复时，需要设定这些告警达到一定时间即恢复。 
功能描述 
当eNodeB局向链路断链持续时长超过配置的“eNodeB断链老化回收时长”时，MME恢复eNodeB断链告警。 
相关主题 
 
设置eNodeB告警参数配置(SET ENODEB ALARM PARA)
 
 
查询eNodeB告警参数配置(SHOW ENODEB ALARM PARA)
 
 
父主题： [eNodeB告警配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置eNodeB告警参数配置(SET ENODEB ALARM PARA) 
#### 设置eNodeB告警参数配置(SET ENODEB ALARM PARA) 
命令功能 
该命令用于设置eNodeB告警参数，主要包括"eNodeB断链老化回收时长"，"TAList下eNodeB到达门限告警方式"，"TAList下eNodeB到达门限告警上报周期"，"TAList下eNodeB数量告警门限"，"一级告警阈值"，"二级告警阈值"。该命令执行成功后，MME将对断链告警持续时长超过这个时长的eNodeB进行告警恢复。 
注意事项 
该配置针对所有的eNodeB生效。配置后，所有eNodeB的断链告警持续时间达到这个时长时，告警会被恢复。 
参数说明 
标识|名称|类型|说明
---|---|---|---
CBDUR|eNodeB断链老化回收时长(小时)|参数可选性:任选参数；参数类型:整数；参数范围为:12~48。|当eNodeB断链告警的持续时长超过配置的"eNodeB断链老化回收时长", MME恢复eNodeB断链告警。参数范围为:12-48小时，缺省为24小时。
TAENBOUTALMMODE|TAList下eNodeB到达门限告警方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在寻呼UE时，寻呼TAList下eNodeB站点数量到达最大门限后是否上报告警。0：不上报（No）1：上报（Yes）
TAENBOUTALMPERIOD|TAList下eNodeB到达门限告警上报周期（小时）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置MME在寻呼TAList下eNodeB站点数量到达最大门限后，告警循环上报的时间间隔。时长设置范围:1～255，单位：小时。默认值：24小时。
TAENBTHRESHOLD|TAList下eNodeB数量告警门限|参数可选性:任选参数；参数类型:整数；参数范围为:100~2000。|该参数用于设置TA或TALIST下eNodeB站点数量告警的最大门限。eNodeB站点数量达到此门限后会上报告警。
ALMTHRESHOLD|一级告警阈值（%）|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于设置TA或TALIST下eNodeB站点数量到达告警门限的一级告警阈值。eNodeB站点数量达到此门限后会上报一级告警。
ALMTHRESHOLD2|二级告警阈值（%）|参数可选性:任选参数；参数类型:整数；参数范围为:1~99。|该参数用于设置TA或TALIST下eNodeB站点数量到达告警门限的二级告警阈值。eNodeB站点数量达到此门限后会上报二级告警。
命令举例 
修改eNodeB告警参数配置，将eNodeB断链老化回收时长改为30小时。 
SET ENODEB ALARM PARA:CBDUR=30; 
父主题： [eNodeB告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询eNodeB告警参数配置(SHOW ENODEB ALARM PARA) 
#### 查询eNodeB告警参数配置(SHOW ENODEB ALARM PARA) 
命令功能 
该命令用于查询eNodeB告警参数，主要包括"eNodeB断链老化回收时长"，"TAList下eNodeB到达门限告警方式"，"TAList下eNodeB到达门限告警上报周期"，"TAList下eNodeB数量告警门限"，"一级告警阈值"，"二级告警阈值"。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CBDUR|eNodeB断链老化回收时长(小时)|参数可选性:任选参数；参数类型:整数。|当eNodeB断链告警的持续时长超过配置的"eNodeB断链老化回收时长", MME恢复eNodeB断链告警。参数范围为:12-48小时，缺省为24小时。
TAENBOUTALMMODE|TAList下eNodeB到达门限告警方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在寻呼UE时，寻呼TAList下eNodeB站点数量到达最大门限后是否上报告警。0：不上报（No）1：上报（Yes）
TAENBOUTALMPERIOD|TAList下eNodeB到达门限告警上报周期（小时）|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME在寻呼TAList下eNodeB站点数量到达最大门限后，告警循环上报的时间间隔。时长设置范围:1～255，单位：小时。默认值：24小时。
TAENBTHRESHOLD|TAList下eNodeB数量告警门限|参数可选性:任选参数；参数类型:整数。|该参数用于设置TA或TALIST下eNodeB站点数量告警的最大门限。eNodeB站点数量达到此门限后会上报告警。
ALMTHRESHOLD|一级告警阈值（%）|参数可选性:任选参数；参数类型:整数。|该参数用于设置TA或TALIST下eNodeB站点数量到达告警门限的一级告警阈值。eNodeB站点数量达到此门限后会上报一级告警。
ALMTHRESHOLD2|二级告警阈值（%）|参数可选性:任选参数；参数类型:整数。|该参数用于设置TA或TALIST下eNodeB站点数量到达告警门限的二级告警阈值。eNodeB站点数量达到此门限后会上报二级告警。
命令举例 
查询eNodeB告警参数配置。 
SHOW ENODEB ALARM PARA 
`
命令 (No.1): SHOW ENODEB ALARM PARA
操作维护   eNodeB断链老化回收时长(小时)    TAList下eNodeB到达门限告警方式    TAList下eNodeB到达门限告警上报周期（小时）   TAList下eNodeB数量告警门限    一级告警阈值（%）   二级告警阈值（%）
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改       30                              不上报                            24                                           1024                          90                  80
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
父主题： [eNodeB告警参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### eNodeB断链告警过滤配置 
### eNodeB断链告警过滤配置 
背景知识 
正常情况下，eNodeB局向链路断链时，MME网元上报eNodeB断链告警，告警码为：2114322696。但网络中可能存在少量不稳定的eNodeB长期处于断链状态，导致告警始终无法恢复，如果这些eNodeB不需要关注，MME提供屏蔽该eNodeB断链告警的功能。 
功能描述 
在“eNodeB断链告警过滤配置”中指定的eNodeB，MME检测到该eNodeB局向链路断链时，不会上报eNodeB断链告警。 
相关主题 
 
新增eNodeB断链告警过滤配置(ADD ENODEB ALARM FILTER)
 
 
修改eNodeB断链告警过滤配置(SET ENODEB ALARM FILTER)
 
 
删除eNodeB断链告警过滤配置(DEL ENODEB ALARM FILTER)
 
 
查询eNodeB断链告警过滤配置(SHOW ENODEB ALARM FILTER)
 
 
父主题： [eNodeB告警配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增eNodeB断链告警过滤配置(ADD ENODEB ALARM FILTER) 
#### 新增eNodeB断链告警过滤配置(ADD ENODEB ALARM FILTER) 
命令功能 
网络中可能存在少量不稳定的eNodeB长期处于断链状态，导致告警始终无法恢复，如果这些eNodeB不需要关注，MME支持通过命令屏蔽eNodeB断链告警的功能。 
该命令用于新增不上报局向断链告警的eNodeB信息，主要包括移动国家码、移动网号和eNodeB局向号。 
注意事项 
该命令最多可以配置1000个支持告警过滤功能的eNodeB。 
eNodeB被配置之后，当该eNodeB局向断链时，MME不会上报断链告警。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号用来唯一识别不同的移动网络，由ITU统一分配和管理。比如中国电信为03，中国移动为00和02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|eNode局向的别名。
命令举例 
新增eNodeB断链告警过滤配置，其中移动国家码为460，移动网号为01，eNodeB局向号为1000，用户别名为name1。 
ADD ENODEB ALARM FILTER:MCC="460",MNC="01",ENODEBID=1000,NAME="name1"; 
父主题： [eNodeB断链告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改eNodeB断链告警过滤配置(SET ENODEB ALARM FILTER) 
#### 修改eNodeB断链告警过滤配置(SET ENODEB ALARM FILTER) 
命令功能 
该命令用于修改不上报局向断链告警的eNodeB信息，只能修改该eNodeB的用户别名。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号用来唯一识别不同的移动网络，由ITU统一分配和管理。比如中国电信为03，中国移动为00和02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|eNode局向的别名。
命令举例 
修改eNodeB断链告警过滤配置，将用户别名改为name2。 
SET ENODEB ALARM FILTER:MCC="460",MNC="01",ENODEBID=1000,NAME="name2"; 
父主题： [eNodeB断链告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除eNodeB断链告警过滤配置(DEL ENODEB ALARM FILTER) 
#### 删除eNodeB断链告警过滤配置(DEL ENODEB ALARM FILTER) 
命令功能 
该命令用于删除不上报局向断链告警的eNodeB信息。删除成功后，该eNodeB和MME断链时，MME上报断链告警。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。如中国为460。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号用来唯一识别不同的移动网络，由ITU统一分配和管理。比如中国电信为03，中国移动为00和02。
ENODEBID|eNodeB局向号|参数可选性:必选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
命令举例 
删除eNodeB断链告警过滤配置，其中移动国家码为460，移动网号为01，eNodeB局向号为1000。 
DEL ENODEB ALARM FILTER:MCC="460",MNC="01",ENODEBID=1000; 
父主题： [eNodeB断链告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询eNodeB断链告警过滤配置(SHOW ENODEB ALARM FILTER) 
#### 查询eNodeB断链告警过滤配置(SHOW ENODEB ALARM FILTER) 
命令功能 
该命令用于查询MME已配置的不需要上报局向断链告警的eNodeB信息。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。如中国为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网号用来唯一识别不同的移动网络，由ITU统一分配和管理。比如中国电信为03，中国移动为00和02。
ENODEBID|eNodeB局向号|参数可选性:任选参数；参数类型:整数；参数范围为:0~268435455。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|eNode局向的别名。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。如中国为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|移动网号用来唯一识别不同的移动网络，由ITU统一分配和管理。比如中国电信为03，中国移动为00和02。
ENODEBID|eNodeB局向号|参数可选性:任选参数；参数类型:整数。|eNodeB局向号是eNodeB通过S1 Setup消息带给MME的，一般是由运营商统一规划。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|eNode局向的别名。
命令举例 
查询eNodeB断链告警过滤配置。 
SHOW ENODEB ALARM FILTER:MCC="460"; 
`
命令 (No.1): SHOW ENODEB ALARM FILTER:MCC="460";
操作维护         移动国家码   移动网号   eNodeB局向号   用户别名
----------------------------------------------------------------
复制 修改 删除   460          01         1000           name1
----------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.052 秒）。
` 
父主题： [eNodeB断链告警过滤配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## EMS局向链路配置 
## EMS局向链路配置 
背景知识 
GTP协议并无链路、局向的概念，GTP的邻接网元是动态发现的，但为了满足EMS上将MME/SGSN与邻接的SGW/GGSN的节点图形化显示在网管界面上，同时也显示各个网元之间的连接关系，于是增加了GTP链路以及局向的概念。 
配置了网元间的GTP链路及局向后，EM才能绘制网元间的拓扑（Topo）关系。MME对应的一个邻接网元就是一个局向，MME到一个邻接网元可以包含多条链路。 
功能描述 
EMS局向链路配置功能包括配置GTP链路和局向，详细功能如下： 
 
用于在EM上进行核心网链路图渲染。
 
 
用于显示各个网元之间的拓扑（Topo）关系。
 
 
GTP链路使用的是对端网元的IP地址，同一网元可能有多个IP地址，配置GTP链路时，MME就需要配置多条GTP链路并关联到同一个局向下。 
相关主题 
 
GTP链路配置
 
 
GTP局向链路配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### GTP链路配置 
### GTP链路配置 
背景知识 
GTP协议并无链路、局向的概念，GTP的邻接网元是动态发现的，但为了满足EMS上将MME/SGSN与邻接的SGW/GGSN的节点图形化显示出来，同时也显示网元间的连接关系，于是增加了GTP链路以及局向的概念。配置了网元间的GTP链路及局向后，EMS才能绘制网元间的Topo关系。到一个邻接网元是一个局向，一个局向可以包含多条链路。 
功能描述 
GTP链路、局向用于EMS的进行核心网链路图渲染，区别网元Topo关系。GTP链路是使用的是对端网元的IP地址，同一网元可能有多个地址，就需要配置多条GTP链路并关联到同一个局向下。 
相关主题 
 
新增GTP链路(ADD GTPIP)
 
 
修改GTP链路(SET GTPIP)
 
 
删除GTP链路(DEL GTPIP)
 
 
查询GTP链路(SHOW GTPIP)
 
 
父主题： [EMS局向链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增GTP链路(ADD GTPIP) 
#### 新增GTP链路(ADD GTPIP) 
命令功能 
该命令用于新增GTP链路配置。主要是配置链路号和 GTP IP地址信息。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~8192。|GTP链路的标识号。
IP|IP地址|参数可选性:必选参数；参数类型:地址|对应的对端网元（GTP节点）的IP地址，IPV4或IPV6格式,地址，且不同链路的IP地址不能重复。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
新增GTP链路，增加链路号为1，对应IP地址为129.1.1.5的GTP链路。 
ADD GTPIP:LINKID=1,IP="129.1.1.5"; 
父主题： [GTP链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改GTP链路(SET GTPIP) 
#### 修改GTP链路(SET GTPIP) 
命令功能 
该命令用于修改GTP链路配置。主要是修改对应链路号的 GTP IP地址信息。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~8192。|GTP链路的标识号。
IP|IP地址|参数可选性:任选参数；参数类型:地址|对应的对端网元（GTP节点）的IP地址，IPV4或IPV6格式,地址，且不同链路的IP地址不能重复。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
修改GTP链路，修改1号GTP链路的IP地址为129.1.1.6。  
SET GTPIP:LINKID=1,IP="129.1.1.6"; 
父主题： [GTP链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除GTP链路(DEL GTPIP) 
#### 删除GTP链路(DEL GTPIP) 
命令功能 
该命令用于删除GTP链路配置。主要是删除链路号和其对应的IP地址信息。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~8192。|GTP链路的标识号。
命令举例 
删除GTP链路，删除1号GTP链路配置。 
DEL GTPIP:LINKID=1; 
父主题： [GTP链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询GTP链路(SHOW GTPIP) 
#### 查询GTP链路(SHOW GTPIP) 
命令功能 
该命令用于查询GTP链路配置。主要是查询链路号和 GTP IP地址信息。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~8192。|GTP链路的标识号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
LINKID|链路号|参数可选性:任选参数；参数类型:整数。|GTP链路的标识号。
IP|IP地址|参数可选性:任选参数；参数类型:地址|对应的对端网元（GTP节点）的IP地址，IPV4或IPV6格式,地址，且不同链路的IP地址不能重复。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
查询已经配置GTP链路信息。 
SHOW GTPIP; 
`
命令 (No.8): SHOW GTPIP
操作维护 链路号 IP地址 别名 
--------------------------------------------
复制 修改 删除  1 1.1.1.1  
--------------------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [GTP链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### GTP局向链路配置 
### GTP局向链路配置 
背景知识 
GTP协议并无链路、局向的概念，GTP的邻接网元是动态发现的，但为了满足EMS上将MME/SGSN与邻接的SGW/GGSN的节点图形化显示出来，同时也显示网元间的连接关系，于是增加了GTP链路以及局向的概念。配置了网元间的GTP链路及局向后，EMS才能绘制网元间的Topo关系。到一个邻接网元是一个局向，一个局向可以包含多条链路。 
功能描述 
GTP链路、局向用于EMS的进行核心网链路图渲染，区别网元Topo关系。GTP链路是使用的是对端网元的IP地址，同一网元可能有多个地址，就需要配置多条GTP链路并关联到同一个局向下。 
相关主题 
 
新增GTP局向链路(ADD GTP OFFICE)
 
 
删除GTP局向链路(DEL GTP OFFICE)
 
 
查询GTP局向链路(SHOW GTP OFFICE)
 
 
父主题： [EMS局向链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增GTP局向链路(ADD GTP OFFICE) 
#### 新增GTP局向链路(ADD GTP OFFICE) 
命令功能 
该命令用于新增GTP局向链路配置。主要是配置 GTP局和GTP链路之关的对应关系。 
注意事项 
本命令配置的GTP链路ID必须已经在GTP链路配置命令中提前配置。 
参数说明 
标识|名称|类型|说明
---|---|---|---
OFFICEIDID|局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~8192。|GTP局向编号，用来标识局向用。
LINKID|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~8192。|GTP局向下的链路号，链路号通过ADD GTPIP配置，通过关联链路号，找到该到链路号对应的IP地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
新增GTP局向链接醘配置，局向号为1，链路号为1。 
ADD GTP OFFICE:OFFICEIDID=1,LINKID=1; 
父主题： [GTP局向链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除GTP局向链路(DEL GTP OFFICE) 
#### 删除GTP局向链路(DEL GTP OFFICE) 
命令功能 
该命令用于删除GTP局向链路配置。主要是删除 GTP局和GTP链路之关的对应关系。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
OFFICEIDID|局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~8192。|GTP局向编号，用来标识局向用。
LINKID|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~8192。|GTP局向下的链路号，链路号通过ADD GTPIP配置，通过关联链路号，找到该到链路号对应的IP地址。
命令举例 
删除GTP局向链接醘配置，删除局向号为1，链路号为1记录。 
DEL GTP OFFICE:OFFICEIDID=1,LINKID=1; 
父主题： [GTP局向链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询GTP局向链路(SHOW GTP OFFICE) 
#### 查询GTP局向链路(SHOW GTP OFFICE) 
命令功能 
该命令用于查询GTP局向链路配置。主要是查询 GTP局和GTP链路之关的对应关系。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
OFFICEIDID|局向号|参数可选性:任选参数；参数类型:整数；参数范围为:1~8192。|GTP局向编号，用来标识局向用。
LINKID|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~8192。|GTP局向下的链路号，链路号通过ADD GTPIP配置，通过关联链路号，找到该到链路号对应的IP地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OFFICEIDID|局向号|参数可选性:任选参数；参数类型:整数。|GTP局向编号，用来标识局向用。
LINKID|链路号|参数可选性:任选参数；参数类型:整数。|GTP局向下的链路号，链路号通过ADD GTPIP配置，通过关联链路号，找到该到链路号对应的IP地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。
命令举例 
查询已经配置GTP局向配置信息 
SHOW GTP OFFICE; 
`
命令 (No.1): SHOW GTP OFFICE
操作维护    局向号       链路号       别名
------------------------------------------
复制 删除   1            1            
------------------------------------------
记录数 1
命令执行成功（耗时 0.085 秒）。
` 
父主题： [GTP局向链路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## GTP节点白名单配置 
## GTP节点白名单配置 
相关主题 
 
设置是否支持GTP节点白名单(SET GTP WHITE NODE SPRT)
 
 
查询是否支持GTP节点白名单(SHOW GTP WHITE NODE SPRT)
 
 
新增GTP节点白名单(ADD GTP WHITE NODE)
 
 
删除GTP节点白名单(DEL GTP WHITE NODE)
 
 
查询GTP节点白名单(SHOW GTP WHITE NODE)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置是否支持GTP节点白名单(SET GTP WHITE NODE SPRT) 
### 设置是否支持GTP节点白名单(SET GTP WHITE NODE SPRT) 
命令功能 
该命令用于配置MME/SGSN是否支持GTP节点白名单功能。 
在某些运营商的组网环境中，有部分型号陈旧的网元设备不支持响应Echo消息，在这类GTP节点不支持响应Echo消息的情况下，运营商仍希望MME/SGSN视这类GTP节点为可达节点时，需要开启此功能。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPGTPNWL|是否支持GTP节点白名单|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME/SGSN是否支持GTP节点白名单功能。不支持（OFF）：MME/SGSN不支持GTP节点白名单。支持（ON）：MME/SGSNE支持GTP节点白名单。
命令举例 
配置MME/SGSN是否支持GTP节点白名单功能。 
SET GTP WHITE NODE SPRT:SUPGTPNWL=ON; 
父主题： [GTP节点白名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询是否支持GTP节点白名单(SHOW GTP WHITE NODE SPRT) 
### 查询是否支持GTP节点白名单(SHOW GTP WHITE NODE SPRT) 
命令功能 
该命令用于查询MME/SGSN是否支持GTP节点白名单功能。可以查询出此功能处于开启还是关闭状态。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPGTPNWL|是否支持GTP节点白名单|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME/SGSN是否支持GTP节点白名单功能。不支持（OFF）：MME/SGSN不支持GTP节点白名单。支持（ON）：MME/SGSNE支持GTP节点白名单。
命令举例 
查询是否支持GTP节点白名单。 
SHOW GTP WHITE NODE SPRT; 
`
命令 (No.2): SHOW GTP WHITE NODE SPRT;
操作维护  是否支持GTP节点白名单
-------------------------------
修改      支持
-------------------------------
记录数 1
命令执行成功（耗时 0.043 秒）。
` 
父主题： [GTP节点白名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增GTP节点白名单(ADD GTP WHITE NODE) 
### 新增GTP节点白名单(ADD GTP WHITE NODE) 
命令功能 
该命令用于将不支持响应Echo消息的GTP节点增加到白名单中。 
加入白名单后，虽然此类GTP节点不支持响应Echo消息，MME/SGSN仍将此类GTP节点视为可达节点。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GTP白名单节点IP地址|参数可选性:必选参数；参数类型:地址|该参数用于设置GTP白名单节点的IP地址，该地址为本地解析或DNS解析获取到的GGSN、SGSN、SGW、MME或MSC地址，可以是IPv4或者IPv6地址。
命令举例 
将不支持响应Echo消息的GTP节点，IP地址为192.168.1.1增加到白名单中。 
ADD GTP WHITE NODE:IP=192.168.1.1; 
父主题： [GTP节点白名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除GTP节点白名单(DEL GTP WHITE NODE) 
### 删除GTP节点白名单(DEL GTP WHITE NODE) 
命令功能 
该命令用于将不支持响应Echo消息的GTP节点从白名单中删除。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GTP白名单节点IP地址|参数可选性:必选参数；参数类型:地址|该参数用于设置GTP白名单节点的IP地址，该地址为本地解析或DNS解析获取到的GGSN、SGSN、SGW、MME或MSC地址，可以是IPv4或者IPv6地址。
命令举例 
将不支持响应Echo消息的GTP节点，IP地址为192.168.1.1，从白名单中删除。 
DEL GTP WHITE NODE:IP=192.168.1.1; 
父主题： [GTP节点白名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询GTP节点白名单(SHOW GTP WHITE NODE) 
### 查询GTP节点白名单(SHOW GTP WHITE NODE) 
命令功能 
该命令用于查询当前白名单中配置的所有GTP节点。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GTP白名单节点IP地址|参数可选性:任选参数；参数类型:地址|该参数用于设置GTP白名单节点的IP地址，该地址为本地解析或DNS解析获取到的GGSN、SGSN、SGW、MME或MSC地址，可以是IPv4或者IPv6地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IP|GTP白名单节点IP地址|参数可选性:任选参数；参数类型:地址|该参数用于设置GTP白名单节点的IP地址，该地址为本地解析或DNS解析获取到的GGSN、SGSN、SGW、MME或MSC地址，可以是IPv4或者IPv6地址。
命令举例 
查询GTP节点白名单配置。 
SHOW GTP WHITE NODE; 
`
命令 (No.29): SHOW GTP WHITE NODE
操作维护    GTP白名单节点IP地址
-------------------------------
复制 删除   1.1.1.1
-------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [GTP节点白名单配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MME信令风暴抑制配置 
## MME信令风暴抑制配置 
背景知识 
信令风暴是由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。 
信令风暴抑制是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
功能描述 
MME信令风暴抑制是用户级的且针对三种终端信令，包括附着请求信令、业务请求信令和PDN连接请求信令。 
 
附着请求信令风暴抑制。
MME在附着请求信令单位统计周期内统计附着请求信令数。如果统计的附着请求信令数大于附着请求最大信令数，则MME将用户加入附着请求信令黑名单管理，并启动黑名单定时器。在附着请求信令黑名单定时器管理时间内，要么附着信令被拒绝或丢弃，要么FAKE APN PDN连接建立成功但用户用此连接无法上网。附着请求信令黑名单定时器超时后，用户从附着信令黑名单移除，可以正常附着并上网。
 
 
业务请求信令风暴抑制。
MME在业务请求信令单位统计周期内统计业务请求信令数。如果统计的业务请求信令数大于业务请求最大信令数，则MME将用户加入业务请求信令黑名单管理，并启动黑名单定时器。在业务请求信令黑名单定时器管理时间内，业务请求信令被拒绝，终端继续发起业务请求MME会分离用户，并对后续的附着直接丢弃。业务请求信令黑名单超时后，用户从业务请求信令黑名单移除，可以正常上网。
 
 
PDN连接请求信令风暴抑制。
MME在PDN连接请求信令单位统计周期内统计PDN连接请求信令数。如果统计的PDN连接请求信令数大于PDN连接请求最大信令数，则MME将用户加入PDN连接请求信令黑名单管理，并启动黑名单定时器。在PDN连接请求信令黑名单定时器管理时间内，PDN连接请求信令被拒绝，终端继续发起PDN连接请求，FAKE APN PDN连接建立成功但用户用此连接无法上网。终端继续再发起PDN连接请求，MME会分离用户并对后续的附着直接丢弃。PDN连接请求信令黑名单超时后，用户从PDN连接请求信令黑名单移除，可以正常建立PDN连接并上网。
 
 
“MME信令风暴抑制配置”为以上MME信令风暴抑制管理提供信令统计周期、最大信令数、拒绝原因值、黑名单定时器时长以及FAKE APN名称的配置信息。 
相关主题 
 
设置MME是否支持信令风暴抑制配置(SET SIGSRESTRAIN FLAG)
 
 
查询MME是否支持信令风暴抑制配置(SHOW SIGSRESTRAIN FLAG)
 
 
设置MME信令风暴抑制配置(SET SIGSRESTRAIN)
 
 
删除MME信令风暴抑制Fake APN(DEL SIGSRESTRAIN FAKE APN)
 
 
查询MME信令风暴抑制配置(SHOW SIGSRESTRAIN)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置MME是否支持信令风暴抑制配置(SET SIGSRESTRAIN FLAG) 
### 设置MME是否支持信令风暴抑制配置(SET SIGSRESTRAIN FLAG) 
命令功能 
设置MME是否支持信令风暴抑制配置。 
注意事项 
未打开MME信令风暴抑制本开关，“MME信令风暴抑制配置信息”不会生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FLAG|MME支持信令风暴抑制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于打开或者关闭MME支持信令风暴抑制开关。
命令举例 
打开MME信令风暴抑制配置开关。 
SET SIGSRESTRAIN FLAG:FLAG="YES" 
父主题： [MME信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询MME是否支持信令风暴抑制配置(SHOW SIGSRESTRAIN FLAG) 
### 查询MME是否支持信令风暴抑制配置(SHOW SIGSRESTRAIN FLAG) 
命令功能 
查询MME是否支持信令风暴抑制配置。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FLAG|MME支持信令风暴抑制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于打开或者关闭MME支持信令风暴抑制开关。
命令举例 
查询MME信令风暴配置开关状态。 
SHOW SIGSRESTRAIN FLAG; 
`
命令 (No.1): SHOW SIGSRESTRAIN FLAG
操作维护  MME支持信令风暴抑制
-----------------------------
修改      支持
-----------------------------
记录数 1
命令执行成功（耗时 0.026 秒）。
` 
父主题： [MME信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置MME信令风暴抑制配置(SET SIGSRESTRAIN) 
### 设置MME信令风暴抑制配置(SET SIGSRESTRAIN) 
命令功能 
该命令用于设置MME信令风暴抑制功能。当智能终端网络信令短时频繁成功或终端网络信令连续失败，造成MME收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，MME需要进行信令风暴抑制管理时，使用该命令。MME信令风暴抑制配置成功后，MME可以根据MME信令风暴抑制各配置值，采取一定的措施，减少网络侧要处理的信令，化解信令风暴，避免网络拥塞，确保网络设备安全运行，有力保障不在信令黑名单中的用户使用数据业务和其他业务的成功率。 
注意事项 
MME信令风暴抑制受License开关“MME支持信令风暴抑制”控制，启用此功能，需要打开此License开关。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ATTSTATISPERD|附着请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME统计附着请求信令的统计周期。
ATTMAXSIGNUM|附着请求最大信令数|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME附着请求信令的统计周期内允许的附着请求最大信令数。
ATTREJCAUSE|附着拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置MME将用户加入附着请求信令黑名单时，给用户终端下发附着拒绝携带的拒绝原因值。附着拒绝时可携带的原因值如下： 2:IMSI unknown in HSS  3:Illegal UE  5:IMEI not accepted  6:Illegal ME  7:EPS services not allowed  8:EPS services and non-EPS services not allowed  9:UE identity cannot be derived by the network  10:Implicitly detached  11:PLMN not allowed  12:Tracking Area not allowed  13:Roaming not allowed in this tracking area  14:EPS services not allowed in this PLMN  15:No Suitable Cells In tracking area  16:MSC temporarily not reachable  17:Network failure  18:CS domain not available  19:ESM failure  20:MAC failure  21:Synch failure  22:Congestion  23:UE security capabilities mismatch  24:Security mode rejected, unspecified  25:Not authorized for this CSG  26:Non-EPS authentication unacceptable  31:Redirection to 5GCN required  35:Requested service option not authorized in this PLMN  39:CS service temporarily not available  40:No EPS bearer context activated  42:Severe network failure  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified
ATTBLACKLISTDUR|附着请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME将用户加入附着请求信令黑名单时，启动的附着请求黑名单定时器的时长。
SERVSTATISPERD|业务请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME统计业务请求信令的统计周期。
SERVMAXSIGNUM|业务请求最大信令数|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME业务请求信令的统计周期内允许的业务请求最大信令数。
SERVREJCAUSE|业务请求拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置MME将用户加入业务请求信令黑名单时，给用户终端下发业务拒绝携带的拒绝原因值。业务请求拒绝时可携带的原因值如下： 2:IMSI unknown in HSS  3:Illegal UE  5:IMEI not accepted  6:Illegal ME  7:EPS services not allowed  8:EPS services and non-EPS services not allowed  9:UE identity cannot be derived by the network  10:Implicitly detached  11:PLMN not allowed  12:Tracking Area not allowed  13:Roaming not allowed in this tracking area  14:EPS services not allowed in this PLMN  15:No Suitable Cells In tracking area  16:MSC temporarily not reachable  17:Network failure  18:CS domain not available  19:ESM failure  20:MAC failure  21:Synch failure  22:Congestion  23:UE security capabilities mismatch  24:Security mode rejected, unspecified  25:Not authorized for this CSG  26:Non-EPS authentication unacceptable  31:Redirection to 5GCN required  35:Requested service option not authorized in this PLMN  39:CS service temporarily not available  40:No EPS bearer context activated  42:Severe network failure  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified
SERVBLACKLISTDUR|业务请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME将用户加入业务请求信令黑名单时，启动的业务请求黑名单定时器的时长。
PDNSTATISPERD|PDN连接请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME统计PDN连接请求信令的统计周期。
PDNMAXSIGNUM|PDN连接请求最大信令数|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME PDN连接请求信令的统计周期内允许的PDN连接请求最大信令数。
PDNREJCAUSE|PDN连接拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置MME将用户加入PDN连接请求信令黑名单时，给用户终端下发PDN连接建立拒绝携带的拒绝原因值。PDN连接拒绝时可携带的原因值如下。 8:Operator Determined Barring  26:Insufficient resources  27:Missing or unknown APN  28:Unknown PDN type  29:User authentication failed  30:Request rejected by Serving GW or PDN GW  31:Request rejected, unspecified  32:Service option not supported  33:Requested service option not subscribed  34:Service option temporarily out of order  35:PTI already in use  36:Regular deactivation  37:EPS QoS not accepted  38:Network failure  39:Reactivation requested  41:Semantic error in the TFT operation  42:Syntactical error in the TFT operation  43:Invalid EPS bearer identity  44:Semantic errors in packet filter(s)  45:Syntactical errors in packet filter(s)  47:PTI mismatch  49:Last PDN disconnection not allowed  50:PDN type IPv4 only allowed  51:PDN type IPv6 only allowed  57:PDN type IPv4v6 only allowed  58:PDN type non IP only allowed  52:PDN type non IP only allowed  53:ESM information not received  54:PDN connection does not exist  55:Multiple PDN connections for a given APN not allowed  56:Collision with network initiated request  59:Unsupported QCI value  60:Bearer handling not supported  65:Maximum number of EPS bearers reached  66:Requested APN not supported in current RAT and PLMN combination  68:PDN type Ethernet only allowed  81:Invalid PTI value  95:Semantically incorrect message  96:Invalid mandatory information  97:Message type non-existent or not implemented  98:Message type not compatible with the protocol state  99:Information element non-existent or not implemented  100:Conditional IE error  101:Message not compatible with the protocol state  111:Protocol error, unspecified  112:APN restriction value incompatible with active EPS bearer context  113:Multiple accesses to a PDN connection not allowed
PDNBLACKLISTDUR|PDN连接请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置MME将用户加入PDN连接请求信令黑名单时，启动的PDN连接请求黑名单定时器的时长。
FAKEAPN|FAKE APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置FAKE APN名称，FAKE APN名称是MME在用户附着请求信令或PDN连接请求信令黑名单定时器管理时间内，终端发起附着请求或PDN连接请求，MME建立FAKE APN PDN连接时使用的，FAKE APN PDN连接可成功建立，FAKE APN PDN连接可成功建立，但用户通过此PDN连接无法上网。
命令举例 
设置MME信令风暴抑制配置。设置附着请求信令统计周期为100秒，附着请求最大信令数为2000，附着拒绝原因值为7，附着请求黑名单定时器时长3600秒；业务请求信令统计周期为200秒，业务请求最大信令数为1000，业务拒绝原因值为7，业务请求黑名单定时器时长3600秒；PDN连接请求信令统计周期为300秒，PDN连接请求最大信令数为100，PDN连接拒绝原因值为7，PDN连接请求黑名单定时器时长3600秒，FAKE APN名称为fake。 
SET SIGSRESTRAIN:ATTSTATISPERD=100,ATTMAXSIGNUM=2000,ATTREJCAUSE=7,ATTBLACKLISTDUR=3600,SERVSTATISPERD=200,SERVMAXSIGNUM=1000,SERVREJCAUSE=7,SERVBLACKLISTDUR=3600,PDNSTATISPERD=300,PDNMAXSIGNUM=100,PDNREJCAUSE=7,PDNBLACKLISTDUR=3600,FAKEAPN="fake"; 
父主题： [MME信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除MME信令风暴抑制Fake APN(DEL SIGSRESTRAIN FAKE APN) 
### 删除MME信令风暴抑制Fake APN(DEL SIGSRESTRAIN FAKE APN) 
命令功能 
该命令用于删除MME信令风暴抑制配置中已配置的Fake APN。
注意事项 
无。 
命令举例 
删除MME信令风暴抑制配置中已配置的Fake APN。 
DEL SIGSRESTRAIN FAKE APN; 
父主题： [MME信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询MME信令风暴抑制配置(SHOW SIGSRESTRAIN) 
### 查询MME信令风暴抑制配置(SHOW SIGSRESTRAIN) 
命令功能 
该命令用于查询MME信令风暴抑制配置信息，包括附着请求、业务请求和PDN连接请求三种信令的信令统计周期、最大信令数、拒绝原因值、黑名单定时器时长以及FAKE APN名称。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ATTSTATISPERD|附着请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME统计附着请求信令的统计周期。
ATTMAXSIGNUM|附着请求最大信令数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME附着请求信令的统计周期内允许的附着请求最大信令数。
ATTREJCAUSE|附着拒绝原因值|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME将用户加入附着请求信令黑名单时，给用户终端下发附着拒绝携带的拒绝原因值。
ATTBLACKLISTDUR|附着请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME将用户加入附着请求信令黑名单时，启动的附着请求黑名单定时器的时长。
SERVSTATISPERD|业务请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME统计业务请求信令的统计周期。
SERVMAXSIGNUM|业务请求最大信令数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME业务请求信令的统计周期内允许的业务请求最大信令数。
SERVREJCAUSE|业务请求拒绝原因值|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME将用户加入业务请求信令黑名单时，给用户终端下发业务拒绝携带的拒绝原因值。
SERVBLACKLISTDUR|业务请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME将用户加入业务请求信令黑名单时，启动的业务请求黑名单定时器的时长。
PDNSTATISPERD|PDN连接请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME统计PDN连接请求信令的统计周期。
PDNMAXSIGNUM|PDN连接请求最大信令数|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME PDN连接请求信令的统计周期内允许的PDN连接请求最大信令数。
PDNREJCAUSE|PDN连接拒绝原因值|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME将用户加入PDN连接请求信令黑名单时，给用户终端下发PDN连接建立拒绝携带的拒绝原因值。
PDNBLACKLISTDUR|PDN连接请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME将用户加入PDN连接请求信令黑名单时，启动的PDN连接请求黑名单定时器的时长。
FAKEAPN|FAKE APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置FAKE APN名称，FAKE APN名称是MME在用户附着请求信令或PDN连接请求信令黑名单定时器管理时间内，终端发起附着请求或PDN连接请求，MME建立FAKE APN PDN连接时使用的，FAKE APN PDN连接可成功建立，FAKE APN PDN连接可成功建立，但用户通过此PDN连接无法上网。
命令举例 
查询MME信令风暴配置。 
SHOW SIGSRESTRAIN; 
`
命令 (No.1): SHOW SIGSRESTRAIN
操作维护  附着请求信令统计周期(秒)   附着请求最大信令数   附着拒绝原因值   附着请求黑名单定时器时长(秒)   业务请求信令统计周期(秒)   业务请求最大信令数   业务请求拒绝原因值   业务请求黑名单定时器时长(秒)   PDN连接请求信令统计周期(秒)   PDN连接请求最大信令数   PDN连接拒绝原因值   PDN连接请求黑名单定时器时长(秒)   FAKE APN名称
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      600                        20                   7                300                            600                        40                   7                    300                            600                           100                     55                  300                               
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.076 秒）。
` 
父主题： [MME信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## SGSN信令风暴抑制配置 
## SGSN信令风暴抑制配置 
背景知识 
信令风暴是由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。 
信令风暴抑制是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
功能描述 
SGSN信令风暴抑制是用户级的且针对三种终端信令，包括附着请求信令、业务请求信令和PDP激活请求信令。 
 
附着请求信令风暴抑制。
SGSN在附着请求信令单位统计周期内统计附着请求信令数。如果统计的附着请求信令数大于附着请求最大信令数，则SGSN将用户加入附着请求信令黑名单管理，并启动黑名单定时器。在附着请求信令黑名单定时器管理时间内，要么附着信令被拒绝或丢弃，要么FAKE APN PDP激活建立成功但用户用此连接无法上网。附着请求信令黑名单定时器超时后，用户从附着信令黑名单移除，可以正常附着并上网。
 
 
业务请求信令风暴抑制。
SGSN在业务请求信令单位统计周期内统计业务请求信令数。如果统计的业务请求信令数大于业务请求最大信令数，则SGSN将用户加入业务请求信令黑名单管理，并启动黑名单定时器。在业务请求信令黑名单定时器管理时间内，业务请求信令被拒绝，终端继续发起业务请求SGSN会分离用户，并对后续的附着直接丢弃。业务请求信令黑名单超时后，用户从业务请求信令黑名单移除，可以正常上网。
 
 
PDP激活请求信令风暴抑制。
SGSN在PDP激活请求信令单位统计周期内统计PDP激活请求信令数。如果统计的PDP激活请求信令数大于PDP激活请求最大信令数，则SGSN将用户加入PDP激活请求信令黑名单管理，并启动黑名单定时器。在PDP激活请求信令黑名单定时器管理时间内，PDP激活请求信令被拒绝，终端继续发起PDP激活请求，FAKE APN PDP激活建立成功但用户用此连接无法上网。终端继续再发起PDP激活请求，SGSN会分离用户并对后续的附着直接丢弃。PDP激活请求信令黑名单超时后，用户从PDP激活请求信令黑名单移除，可以正常建立PDP激活并上网。
 
 
“SGSN信令风暴抑制配置”为以上SGSN信令风暴抑制管理提供信令统计周期、最大信令数、拒绝原因值、黑名单定时器时长以及FAKE APN名称的配置信息。 
相关主题 
 
设置SGSN是否支持信令风暴抑制配置(SET SGSN SIGSRESTRAIN FLAG)
 
 
查询SGSN是否支持信令风暴抑制配置(SHOW SGSN SIGSRESTRAIN FLAG)
 
 
设置SGSN信令风暴抑制配置(SET SGSN SIGSRESTRAIN)
 
 
删除SGSN信令风暴抑制Fake APN(DEL SGSN SIGSRESTRAIN FAKE APN)
 
 
查询SGSN信令风暴抑制配置(SHOW SGSN SIGSRESTRAIN)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置SGSN是否支持信令风暴抑制配置(SET SGSN SIGSRESTRAIN FLAG) 
### 设置SGSN是否支持信令风暴抑制配置(SET SGSN SIGSRESTRAIN FLAG) 
命令功能 
该命令用于设置SGSN信令风暴抑制开关。当智能终端网络信令短时频繁成功或终端网络信令连续失败，造成SGSN收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，SGSN需要进行信令风暴抑制管理时，使用该命令。启用本功能后，SGSN信令风暴抑制配置成功后，SGSN可以根据SGSN信令风暴抑制各配置值，采取一定的措施，减少网络侧要处理的信令，化解信令风暴，避免网络拥塞，确保网络设备安全运行。
注意事项 
未打开SGSN信令风暴抑制本开关，“SGSN信令风暴抑制配置信息”不会生效。
参数说明 
标识|名称|类型|说明
---|---|---|---
FLAG|SGSN支持信令风暴抑制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持信令风暴抑制。
命令举例 
打开SGSN信令风暴抑制配置开关。 
SET SGSN SIGSRESTRAIN FLAG:FLAG="ON"; 
父主题： [SGSN信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询SGSN是否支持信令风暴抑制配置(SHOW SGSN SIGSRESTRAIN FLAG) 
### 查询SGSN是否支持信令风暴抑制配置(SHOW SGSN SIGSRESTRAIN FLAG) 
命令功能 
该命令用于查询SGSN信令风暴抑制配置开关状态。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FLAG|SGSN支持信令风暴抑制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持信令风暴抑制。
命令举例 
查询SGSN信令风暴配置开关状态。 
SHOW SGSN SIGSRESTRAIN FLAG; 
`
命令 (No.8): SHOW SGSN SIGSRESTRAIN FLAG
操作维护  SGSN支持信令风暴抑制
------------------------------
修改      支持
------------------------------
记录数 1
命令执行成功（耗时 0.022 秒）。
` 
父主题： [SGSN信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置SGSN信令风暴抑制配置(SET SGSN SIGSRESTRAIN) 
### 设置SGSN信令风暴抑制配置(SET SGSN SIGSRESTRAIN) 
命令功能 
该命令用于设置SGSN信令风暴抑制功能。当智能终端网络信令短时频繁成功或终端网络信令连续失败，造成SGSN收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，SGSN需要进行信令风暴抑制管理时，使用该命令。SGSN信令风暴抑制配置成功后，SGSN可以根据SGSN信令风暴抑制各配置值，采取一定的措施，减少网络侧要处理的信令，化解信令风暴，避免网络拥塞，确保网络设备安全运行，有力保障不在信令黑名单中的用户使用数据业务和其他业务的成功率。
注意事项 
SGSN信令风暴抑制受License开关“SGSN支持信令风暴抑制”控制，启用此功能，需要打开此License开关。
参数说明 
标识|名称|类型|说明
---|---|---|---
ATTSTATISPERD|附着请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN统计附着请求信令的统计周期。
ATTMAXSIGNUM|附着请求最大信令数|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN附着请求信令的统计周期内允许的附着请求最大信令数。
ATTREJCAUSE|附着拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置SGSN将用户加入附着请求信令黑名单时，给用户终端下发附着拒绝携带的拒绝原因值。附着拒绝时可携带的原因值如下：2:IMSI unknown in HLR 3:Illegal MS 5:IMEI not accepted 6:Illegal ME 7:GPRS services not allowed 8:GPRS services and non-GPRS services not allowed 9:MS identity cannot be derived by the network10:Implicitly detached 11:PLMN not allowed 12:Location Area not allowed 13:Roaming not allowed in this location area 14:GPRS services not allowed in this PLMN 15:No Suitable Cells In Location Area 16:MSC temporarily not reachable 17:Network failure20:MAC failure 21:Synch failure 22:Congestion 23:GSM authentication unacceptable 25:Not authorized for this CSG 28:SMS provided via GPRS in this routing area40:No PDP context activated 95:Semantically incorrect message 96:Invalid mandatory information 97:Message type non-existent or not implemented 98:Message type not compatible with the protocol state 99:Information element non-existent or not implemented 100:Conditional IE error 101:Message not compatible with the protocol state 111:Protocol error, unspecified
ATTBLACKLISTDUR|附着请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN将用户加入附着请求信令黑名单时，启动的附着请求黑名单定时器的时长。
SERVSTATISPERD|业务请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN统计业务请求信令的统计周期。
SERVMAXSIGNUM|业务请求最大信令数|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN业务请求信令的统计周期内允许的业务请求最大信令数。
SERVREJCAUSE|业务请求拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置SGSN将用户加入业务请求信令黑名单时，给用户终端下发业务拒绝携带的拒绝原因值。业务请求拒绝时可携带的原因值如下：2:IMSI unknown in HLR 3:Illegal MS 5:IMEI not accepted 6:Illegal ME 7:GPRS services not allowed 8:GPRS services and non-GPRS services not allowed 9:MS identity cannot be derived by the network10:Implicitly detached 11:PLMN not allowed 12:Location Area not allowed 13:Roaming not allowed in this location area 14:GPRS services not allowed in this PLMN 15:No Suitable Cells In Location Area 16:MSC temporarily not reachable 17:Network failure20:MAC failure 21:Synch failure 22:Congestion 23:GSM authentication unacceptable 25:Not authorized for this CSG 28:SMS provided via GPRS in this routing area40:No PDP context activated 95:Semantically incorrect message 96:Invalid mandatory information 97:Message type non-existent or not implemented 98:Message type not compatible with the protocol state 99:Information element non-existent or not implemented 100:Conditional IE error 101:Message not compatible with the protocol state 111:Protocol error, unspecified
SERVBLACKLISTDUR|业务请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN将用户加入业务请求信令黑名单时，启动的业务请求黑名单定时器的时长。
PDPSTATISPERD|PDP激活请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN统计PDP激活请求信令的统计周期。
PDPMAXSIGNUM|PDP激活请求最大信令数|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN PDP激活请求信令的统计周期内允许的PDP激活请求最大信令数。
PDPREJCAUSE|PDP激活拒绝原因值|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置SGSN将用户加入PDP激活请求信令黑名单时，给用户终端下发PDP激活拒绝携带的拒绝原因值。PDN连接拒绝时可携带的原因值如下。8:Operator Determined Barring 24:MBMS bearer capabilities insufficient for the service25:LLC or SNDCP failure(A/Gb mode only)26:Insufficient resources 27:Missing or unknown APN 28:Unknown PDP address or PDP type 29:User authentication failed 30:Activation rejected by GGSN, Serving GW or PDN GW 31:Activation rejected, unspecified32:Service option not supported 33:Requested service option not subscribed 34:Service option temporarily out of order 35:NSAPI already used (not sent)36:Regular deactivation 37:QoS not accepted38:Network failure 39:Reactivation requested 40:Feature not supported41:Semantic error in the TFT operation 42:Syntactical error in the TFT operation 43:Unknown PDP context 44:Semantic errors in packet filter(s) 45:Syntactical errors in packet filter(s) 46:PDP context without TFT already activated47:Multicast group membership time-out48:Request rejected, BCM violation50:PDP type IPv4 only allowed51:PDP type IPv6 only allowed 57:PDP type IPv4v6 only allowed 58:PDP type non IP only allowed 52:Single address bearers only allowed56:Collision with network initiated request60:Bearer handling not supported65:Maximum number of PDP contexts reached 66:Requested APN not supported in current RAT and PLMN combination 81:Invalid transaction identifier value95:Semantically incorrect message 96:Invalid mandatory information 97:Message type non-existent or not implemented 98:Message type not compatible with the protocol state 99:Information element non-existent or not implemented 100:Conditional IE error 101:Message not compatible with the protocol state 111:Protocol error, unspecified 112:APN restriction value incompatible with active PDP context 113:Multiple accesses to a PDN connection not allowed
PDPBLACKLISTDUR|PDP激活请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置SGSN将用户加入PDP激活请求信令黑名单时，启动的PDP激活请求黑名单定时器的时长。
FAKEAPN|FAKE APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于设置FAKE APN名称，FAKE APN名称是SGSN在用户PDP激活请求信令黑名单定时器管理时间内，终端发起PDP激活请求，SGSN建立FAKE APN PDP时使用的，FAKE APN PDP可成功建立，但用户通过此PDP无法上网。
命令举例 
设置SGSN信令风暴抑制配置的FAKE APN名称为zte。 
SET SGSN SIGSRESTRAIN:FAKEAPN="zte"; 
父主题： [SGSN信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除SGSN信令风暴抑制Fake APN(DEL SGSN SIGSRESTRAIN FAKE APN) 
### 删除SGSN信令风暴抑制Fake APN(DEL SGSN SIGSRESTRAIN FAKE APN) 
命令功能 
该命令用于删除SGSN信令风暴抑制配置中已配置的Fake APN。
注意事项 
无。
命令举例 
删除SGSN信令风暴抑制配置中已配置的Fake APN。 
DEL SGSN SIGSRESTRAIN FAKE APN; 
父主题： [SGSN信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询SGSN信令风暴抑制配置(SHOW SGSN SIGSRESTRAIN) 
### 查询SGSN信令风暴抑制配置(SHOW SGSN SIGSRESTRAIN) 
命令功能 
该命令用于查询SGSN信令风暴抑制配置信息，包括附着请求、业务请求和PDP激活请求三种信令的信令统计周期、最大信令数、拒绝原因值、黑名单定时器时长以及FAKE APN名称。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ATTSTATISPERD|附着请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN统计附着请求信令的统计周期。
ATTMAXSIGNUM|附着请求最大信令数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN附着请求信令的统计周期内允许的附着请求最大信令数。
ATTREJCAUSE|附着拒绝原因值|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN将用户加入附着请求信令黑名单时，给用户终端下发附着拒绝携带的拒绝原因值。附着拒绝时可携带的原因值如下：2:IMSI unknown in HLR 3:Illegal MS 5:IMEI not accepted 6:Illegal ME 7:GPRS services not allowed 8:GPRS services and non-GPRS services not allowed 9:MS identity cannot be derived by the network10:Implicitly detached 11:PLMN not allowed 12:Location Area not allowed 13:Roaming not allowed in this location area 14:GPRS services not allowed in this PLMN 15:No Suitable Cells In Location Area 16:MSC temporarily not reachable 17:Network failure20:MAC failure 21:Synch failure 22:Congestion 23:GSM authentication unacceptable 25:Not authorized for this CSG 28:SMS provided via GPRS in this routing area40:No PDP context activated 95:Semantically incorrect message 96:Invalid mandatory information 97:Message type non-existent or not implemented 98:Message type not compatible with the protocol state 99:Information element non-existent or not implemented 100:Conditional IE error 101:Message not compatible with the protocol state 111:Protocol error, unspecified
ATTBLACKLISTDUR|附着请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN将用户加入附着请求信令黑名单时，启动的附着请求黑名单定时器的时长。
SERVSTATISPERD|业务请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN统计业务请求信令的统计周期。
SERVMAXSIGNUM|业务请求最大信令数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN业务请求信令的统计周期内允许的业务请求最大信令数。
SERVREJCAUSE|业务请求拒绝原因值|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN将用户加入业务请求信令黑名单时，给用户终端下发业务拒绝携带的拒绝原因值。业务请求拒绝时可携带的原因值如下：2:IMSI unknown in HLR 3:Illegal MS 5:IMEI not accepted 6:Illegal ME 7:GPRS services not allowed 8:GPRS services and non-GPRS services not allowed 9:MS identity cannot be derived by the network10:Implicitly detached 11:PLMN not allowed 12:Location Area not allowed 13:Roaming not allowed in this location area 14:GPRS services not allowed in this PLMN 15:No Suitable Cells In Location Area 16:MSC temporarily not reachable 17:Network failure20:MAC failure 21:Synch failure 22:Congestion 23:GSM authentication unacceptable 25:Not authorized for this CSG 28:SMS provided via GPRS in this routing area40:No PDP context activated 95:Semantically incorrect message 96:Invalid mandatory information 97:Message type non-existent or not implemented 98:Message type not compatible with the protocol state 99:Information element non-existent or not implemented 100:Conditional IE error 101:Message not compatible with the protocol state 111:Protocol error, unspecified
SERVBLACKLISTDUR|业务请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN将用户加入业务请求信令黑名单时，启动的业务请求黑名单定时器的时长。
PDPSTATISPERD|PDP激活请求信令统计周期(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN统计PDP激活请求信令的统计周期。
PDPMAXSIGNUM|PDP激活请求最大信令数|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN PDP激活请求信令的统计周期内允许的PDP激活请求最大信令数。
PDPREJCAUSE|PDP激活拒绝原因值|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN将用户加入PDP激活请求信令黑名单时，给用户终端下发PDP激活拒绝携带的拒绝原因值。PDN连接拒绝时可携带的原因值如下。8:Operator Determined Barring 24:MBMS bearer capabilities insufficient for the service25:LLC or SNDCP failure(A/Gb mode only)26:Insufficient resources 27:Missing or unknown APN 28:Unknown PDP address or PDP type 29:User authentication failed 30:Activation rejected by GGSN, Serving GW or PDN GW 31:Activation rejected, unspecified32:Service option not supported 33:Requested service option not subscribed 34:Service option temporarily out of order 35:NSAPI already used (not sent)36:Regular deactivation 37:QoS not accepted38:Network failure 39:Reactivation requested 40:Feature not supported41:Semantic error in the TFT operation 42:Syntactical error in the TFT operation 43:Unknown PDP context 44:Semantic errors in packet filter(s) 45:Syntactical errors in packet filter(s) 46:PDP context without TFT already activated47:Multicast group membership time-out48:Request rejected, BCM violation50:PDP type IPv4 only allowed51:PDP type IPv6 only allowed 57:PDP type IPv4v6 only allowed 58:PDP type non IP only allowed 52:Single address bearers only allowed56:Collision with network initiated request60:Bearer handling not supported65:Maximum number of PDP contexts reached 66:Requested APN not supported in current RAT and PLMN combination 81:Invalid transaction identifier value95:Semantically incorrect message 96:Invalid mandatory information 97:Message type non-existent or not implemented 98:Message type not compatible with the protocol state 99:Information element non-existent or not implemented 100:Conditional IE error 101:Message not compatible with the protocol state 111:Protocol error, unspecified 112:APN restriction value incompatible with active PDP context 113:Multiple accesses to a PDN connection not allowed
PDPBLACKLISTDUR|PDP激活请求黑名单定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于设置SGSN将用户加入PDP激活请求信令黑名单时，启动的PDP激活请求黑名单定时器的时长。
FAKEAPN|FAKE APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于设置FAKE APN名称，FAKE APN名称是SGSN在用户PDP激活请求信令黑名单定时器管理时间内，终端发起PDP激活请求，SGSN建立FAKE APN PDP时使用的，FAKE APN PDP可成功建立，但用户通过此PDP无法上网。
命令举例 
查询SGSN信令风暴抑制配置。 
SHOW SGSN SIGSRESTRAIN; 
`
命令 (No.10): SHOW SGSN SIGSRESTRAIN
操作维护  附着请求信令统计周期(秒)   附着请求最大信令数   附着拒绝原因值   附着请求黑名单定时器时长(秒)   业务请求信令统计周期(秒)   业务请求最大信令数   业务请求拒绝原因值   业务请求黑名单定时器时长(秒)   PDP激活请求信令统计周期(秒)   PDP激活请求最大信令数   PDP激活拒绝原因值   PDP激活请求黑名单定时器时长(秒)   FAKE APN名称
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      720                        15                   7                1200                           720                        30                   7                    1200                           720                           10                      31                  200                               zte
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [SGSN信令风暴抑制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 默认承载重建配置 
## 默认承载重建配置 
背景知识 
EPC网络，如果对于省间漫游用户采用Local Breakout方式，即采用拜访地的PGW接入拜访地的PDN网络情况下，当用户从不同区域移动时，由于PGW是业务的锚定点，用户的承载连接通道仍然采用之前接入区域的PGW，而SGW却是本地的，造成了承载资源的浪费。如果用户的业务是IMS业务，会造成语音的时延增加。 
为了节省承载资源，降低业务时延，在用户跨区域移动时，在尽量减少对用户业务影响的情况下，可以对用户的默认承载重建，新建的默认承载使用本地PGW。 
功能描述 
“默认承载重建配置”用于设置MME是否支持重建默认承载以及重建默认承载的策略。配置后，用户在跨区域移动时，会发生SGW改变的TAU或Handover，MME检测在以下条件满足时，重建默认承载。 
 
                        MME支持默认承载重建。对应命令为：
                        SET DEFAULT BEARER REBUILD
                        。
                    
 
 
                        MME检测到用户连接的SGW和PGW是跨区域的。对应命令为：
                        SET DEFAULT BEARER REBUILD
                        。
                    
 
 
                        用户的默认承载对应的APN在MME上配置需要重建默认承载的APN列表内，且当前时间在该APN的默认承载重建功能的生效时间内，且用户进入空闲态时长不小于该APN的默认承载重建功能要求的用户进入空闲态时长。对应命令为：
                        ADD REBUILD BEARER APN
                        。
                    
 
 
相关主题 
 
默认承载重建策略配置
 
 
需重建默认承载的APN配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 默认承载重建策略配置 
### 默认承载重建策略配置 
背景知识 
EPC网络，如果对于省间漫游用户采用Local Breakout方式，即采用拜访地的PGW接入拜访地的PDN网络情况下，当用户从不同区域移动时，由于PGW是业务的锚定点，用户的承载连接通道仍然采用之前接入区域的PGW，而SGW却是本地的，造成了承载资源的浪费。如果用户的业务是IMS业务，会造成语音的时延增加。 
为了节省承载资源，降低业务时延，在用户跨区域移动时，在尽量减少对用户业务影响的情况下，可以对用户的默认承载重建，新建的默认承载使用本地PGW。 
功能描述 
“默认承载重建策略配置”用于设置MME是否支持重建默认承载、MME检测用户的SGW和PGW是否合设的依据、功能生效时存量用户是否重建默认承载。具体包括以下设置： 
 
MME是否支持默认承载重建功能。如果设置为支持，MME才会启用默认承载重建功能。
 
 
设置MME检测用户的SGW和PGW是否合设的依据。当用户的SGW和PGW非合设时，MME发起默认承载的重建过程。
 
 
功能生效时存量用户是否重建默认承载。如果设置为支持，则MME在功能生效后，把存量用户符合重建条件的默认承载也重建。
 
 
相关主题 
 
设置默认承载重建策略配置(SET DEFAULT BEARER REBUILD)
 
 
查询默认承载重建策略配置(SHOW DEFAULT BEARER REBUILD)
 
 
父主题： [默认承载重建配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置默认承载重建策略配置(SET DEFAULT BEARER REBUILD) 
#### 设置默认承载重建策略配置(SET DEFAULT BEARER REBUILD) 
命令功能 
该命令用于配置用户发生SGW改变后，MME为用户重建默认承载的策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RESETBEAR|支持默认承载重建|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定MME是否支持默认承载重建功能。配置为支持后，当用户发生SGW改变流程后，MME根据配置的策略判断是否需要对该用户重建默认承载。
SAMELABELNUM|SGW和PGW合一时FQDN相同的Label数|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|该参数用于MME判断用户连接的SGW和PGW是否合一。用户发生SGW改变的TAU或者Handover流程后，如果SGW和PGW是合一的，则MME不需要对该用户重建默认承载。MME根据SGW和PGW的FQDN判断SGW和PGW是否合一。FQDN由一个或多个Label组成，每个Label由长度和一串字符串组成，字符串是字母和数字的组合。如果SGW和PGW的FQDN从后往前，相同的Label个数大于等于“SGW和PGW合一时FQDN相同的Label数”，则MME认为SGW和PGW是合一的，否则认为SGW和PGW不是合一的。
IFRESETREGUSER|功能生效时存量用户重建默认承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识当功能开关从关到开，或功能生效时间发生改变时，对存量用户是否需重建默认承载。
命令举例 
设置默认承载重建策略配置，其中支持默认承载重建为“是”，SGW和PGW合一时FQDN相同的Label数为10，功能生效时存量用户重建默认承载为“是”。 
SET DEFAULT BEARER REBUILD:RESETBEAR="YES",SAMELABELNUM=10,IFRESETREGUSER="YES"; 
父主题： [默认承载重建策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询默认承载重建策略配置(SHOW DEFAULT BEARER REBUILD) 
#### 查询默认承载重建策略配置(SHOW DEFAULT BEARER REBUILD) 
命令功能 
该命令用于查询SGW改变时，MME为用户重建默认承载策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RESETBEAR|支持默认承载重建|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定MME是否支持默认承载重建功能。配置为支持后，当用户发生SGW改变流程后，MME根据配置的策略判断是否需要对该用户重建默认承载。
SAMELABELNUM|SGW和PGW合一时FQDN相同的Label数|参数可选性:任选参数；参数类型:整数。|该参数用于MME判断用户连接的SGW和PGW是否合一。用户发生SGW改变的TAU或者Handover流程后，如果SGW和PGW是合一的，则MME不需要对该用户重建默认承载。MME根据SGW和PGW的FQDN判断SGW和PGW是否合一。FQDN由一个或多个Label组成，每个Label由长度和一串字符串组成，字符串是字母和数字的组合。如果SGW和PGW的FQDN从后往前，相同的Label个数大于等于“SGW和PGW合一时FQDN相同的Label数”，则MME认为SGW和PGW是合一的，否则认为SGW和PGW不是合一的。
IFRESETREGUSER|功能生效时存量用户重建默认承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识当功能开关从关到开，或功能生效时间发生改变时，对存量用户是否需重建默认承载。
命令举例 
查询默认承载重建策略配置。 
SHOW DEFAULT BEARER REBUILD; 
`
(No.2) : SHOW DEFAULT BEARER REBUILD
-----------------uMAC_MME_V7master/NFS_MMESGSN_0----------------
操作维护       支持默认承载重建 SGW和PGW合一时FQDN相同的Label数 功能生效时存量用户重建默认承载 
-----------------------------------------------------------------------------------------------
修改           是               10                              是                             
-----------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-10 18:33:20 耗时: 0.922秒。
` 
父主题： [默认承载重建策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 需重建默认承载的APN配置 
### 需重建默认承载的APN配置 
背景知识 
EPC网络，如果对于省间漫游用户采用Local Breakout方式，即采用拜访地的PGW接入拜访地的PDN网络情况下，当用户从不同区域移动时，由于PGW是业务的锚定点，用户的承载连接通道仍然采用之前接入区域的PGW，而SGW却是本地的，造成了承载资源的浪费。如果用户的业务是IMS业务，会造成语音的时延增加。 
为了节省承载资源，降低业务时延，在用户跨区域移动时，在尽量减少对用户业务影响的情况下，可以对用户的默认承载重建，新建的默认承载使用本地PGW。 
功能描述 
“需重建默认承载的APN配置”用于在MME上指定APN，以及指定该APN的默认承载重建生效时间以及用户进入空闲态时长等条件。具体包括以下设置： 
 
设置支持默认承载重建功能的APN。只有设置AN，MME才会启用默认承载重建功能。
 
 
设置指定APN支持默认承载重建功能启用的时间段。只有在设置的时间段内，MME才会启用默认承载重建功能。
 
 
设置指定APN用户处于“ECM-IDLE”的时长阈值，达到阈值时才对用户重建默认承载。
 
 
如果“需重建默认承载的APN配置”中没有配置任何一个APN，表示对所有APN都不启用默认承载重建功能。 
相关主题 
 
新增需重建默认承载的APN配置(ADD REBUILD BEARER APN)
 
 
修改需重建默认承载的APN配置(SET REBUILD BEARER APN)
 
 
删除需重建默认承载的APN配置(DEL REBUILD BEARER APN)
 
 
查询需重建默认承载的APN配置(SHOW REBUILD BEARER APN)
 
 
父主题： [默认承载重建配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增需重建默认承载的APN配置(ADD REBUILD BEARER APN) 
#### 新增需重建默认承载的APN配置(ADD REBUILD BEARER APN) 
命令功能 
该命令用于配置需重建默认承载的APN，以及该APN默认承载重建策略。配置后，针对使用该APN的用户，在发生SGW改变的流程后，MME判断是否需要对该用户重建默认承载。 
注意事项 
此处配置的APN不能和“紧急数据配置”中的APN重复，“紧急数据配置”中的APN可以通过命令[SHOW EMERGDATA]查询。
参数说明 
标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于配置在MME支持SGW改变时的默认承载重建功能时，需要重建默认承载的APN名称。用户使用的APN必须在此处配置后，MME才会对该用户进行默认承载重建。
IFREBUILDBASEDCC|是否根据CC判断默认承载重建|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否根据CC（计费特性）判断默认承载重建。是：该APN是否重建默认承载需要基于用户签约CC值判断，对于特定CC值，重建默认承载；非特定CC值，不重建默认承载。否：该APN是否重建默认承载不需要基于用户签约CC值判断。
STARTTIME|起始时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定MME支持SGW改变时的默认承载重建时，功能生效的起始时间。
ENDTIME|结束时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定MME支持SGW改变时的默认承载重建时，功能生效的结束时间。
IDLEDURATION|空闲态时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~43200。|该参数用于用户在发生SGW改变的TAU或者Handover流程后，用户处于“ECM-IDLE”的时长达到该参数设置的时长，MME可以对该用户重建默认承载。如果为0，表示只要用户一进入空闲态，则可以立刻重建默认承载。
IMMIREBUILD|默认承载立即重建|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数标识只要SGW改变，不存在其他延迟重建的条件（主要是正在通话的语音默认承载的延迟释放）时，是否立刻重建默认承载，不需用户进入空闲态。
命令举例 
新增需重建默认承载的APN配置，其中APN名称为test.com。 
ADD REBUILD BEARER APN:APNNAME="test.com" 
父主题： [需重建默认承载的APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改需重建默认承载的APN配置(SET REBUILD BEARER APN) 
#### 修改需重建默认承载的APN配置(SET REBUILD BEARER APN) 
命令功能 
该命令用于修改需重建默认承载的APN的重建策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于配置在MME支持SGW改变时的默认承载重建功能时，需要重建默认承载的APN名称。用户使用的APN必须在此处配置后，MME才会对该用户进行默认承载重建。
IFREBUILDBASEDCC|是否根据CC判断默认承载重建|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否根据CC（计费特性）判断默认承载重建。是：该APN是否重建默认承载需要基于用户签约CC值判断，对于特定CC值，重建默认承载；非特定CC值，不重建默认承载。否：该APN是否重建默认承载不需要基于用户签约CC值判断。
STARTTIME|起始时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定MME支持SGW改变时的默认承载重建时，功能生效的起始时间。
ENDTIME|结束时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定MME支持SGW改变时的默认承载重建时，功能生效的结束时间。
IDLEDURATION|空闲态时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~43200。|该参数用于用户在发生SGW改变的TAU或者Handover流程后，用户处于“ECM-IDLE”的时长达到该参数设置的时长，MME可以对该用户重建默认承载。如果为0，表示只要用户一进入空闲态，则可以立刻重建默认承载。
IMMIREBUILD|默认承载立即重建|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数标识只要SGW改变，不存在其他延迟重建的条件（主要是正在通话的语音默认承载的延迟释放）时，是否立刻重建默认承载，不需用户进入空闲态。
命令举例 
修改需重建默认承载的APN配置，APN名称为test.com，是否根据CC判断默认承载重建选择是。 
SET REBUILD BEARER APN:APNNAME="test.com",IFREBUILDBASEDCC="YES" 
父主题： [需重建默认承载的APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除需重建默认承载的APN配置(DEL REBUILD BEARER APN) 
#### 删除需重建默认承载的APN配置(DEL REBUILD BEARER APN) 
命令功能 
该命令用于删除需重建默认承载的APN。APN删除后，对使用该APN的用户，MME不会进行默认承载重建。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~61个字符。|该参数用于配置在MME支持SGW改变时的默认承载重建功能时，需要重建默认承载的APN名称。用户使用的APN必须在此处配置后，MME才会对该用户进行默认承载重建。
命令举例 
删除需重建默认承载的APN配置，其中APN名称为test.com。 
DEL REBUILD BEARER APN:APNNAME="test.com" 
父主题： [需重建默认承载的APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询需重建默认承载的APN配置(SHOW REBUILD BEARER APN) 
#### 查询需重建默认承载的APN配置(SHOW REBUILD BEARER APN) 
命令功能 
该命令用于查询MME网元已经配置的的需要重建默认承载的APN，以及该APN默认承载重建策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于配置在MME支持SGW改变时的默认承载重建功能时，需要重建默认承载的APN名称。用户使用的APN必须在此处配置后，MME才会对该用户进行默认承载重建。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APNNAME|APN名称|参数可选性:任选参数；参数类型:字符型。|该参数用于配置在MME支持SGW改变时的默认承载重建功能时，需要重建默认承载的APN名称。用户使用的APN必须在此处配置后，MME才会对该用户进行默认承载重建。
IFREBUILDBASEDCC|是否根据CC判断默认承载重建|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否根据CC（计费特性）判断默认承载重建。是：该APN是否重建默认承载需要基于用户签约CC值判断，对于特定CC值，重建默认承载；非特定CC值，不重建默认承载。否：该APN是否重建默认承载不需要基于用户签约CC值判断。
STARTTIME|起始时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定MME支持SGW改变时的默认承载重建时，功能生效的起始时间。
ENDTIME|结束时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定MME支持SGW改变时的默认承载重建时，功能生效的结束时间。
IDLEDURATION|空闲态时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于用户在发生SGW改变的TAU或者Handover流程后，用户处于“ECM-IDLE”的时长达到该参数设置的时长，MME可以对该用户重建默认承载。如果为0，表示只要用户一进入空闲态，则可以立刻重建默认承载。
IMMIREBUILD|默认承载立即重建|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识只要SGW改变，不存在其他延迟重建的条件（主要是正在通话的语音默认承载的延迟释放）时，是否立刻重建默认承载，不需用户进入空闲态。
命令举例 
查询需重建默认承载的APN配置。 
SHOW REBUILD BEARER APN 
`
(No.7) : SHOW REBUILD BEARER APN:
-----------------uMAC_MME_V7master/NFS_MMESGSN_0----------------
操作维护       APN名称  是否根据CC判断默认承载重建 起始时间 结束时间 空闲态时长(秒) 默认承载立即重建 
-----------------------------------------------------------------------------------------------------
复制 修改 删除 test.com 否                         00:00    00:00    0              否               
-----------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-10 18:36:18 耗时: 1.045秒
` 
父主题： [需重建默认承载的APN配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 容灾恢复配置 
## 容灾恢复配置 
背景知识 
容灾恢复是当MME、SGW、PGW或者P-CSCF、MSC/VLR发生故障后，MME通过指示UE重新附着、重建PDN连接或IMSI重新附着的方式，实现相关的业务恢复。这对于需要保持UE实时在线的VoLTE以及CSFB业务来说，尤为重要。 
对于MME容灾恢复，MME支持以下功能： 
 
POOL内全部MME之间支持在线用户IMSI和TA list信息备份。
 
 
在收到SGW发送的DDN（Downlink Data Notification，下行数据通知）消息后，备用MME以IMSI方式寻呼用户，触发用户重新附着。
 
 
对于SGW容灾恢复，MME支持以下功能： 
 
支持通过Echo消息或者Recovery信元检测SGW故障。
 
 
检测到SGW故障后，针对故障设备上的用户采用指示用户重新附着或重选SGW的方式进行业务恢复。
 
 
在此期间，空闲态用户主动触发上行业务时，返回拒绝并指示UE重新附着。
 
 
对于PGW容灾恢复，MME支持以下功能： 
 
支持通过SGW发送的PGW Restart Notification消息感知PGW故障。
 
 
检测到PGW故障后，针对故障设备上的用户：
若该用户所有PDN连接对应的PGW均故障，则MME通过发送分离请求、或者IMSI寻呼、或者业务请求拒绝和TAU拒绝来指示用户重新附着。
若用户仅IMS PDN连接对应的PGW故障，则MME指示用户重建IMS PDN连接。
 
 
对于P-CSCF容灾恢复，MME支持以下功能： 
 
根据HSS的P-CSCF恢复指示，触发UE的IMS PDN重建，在PDN重建过程中由PGW为UE分配新的P-CSCF地址。
 
 
MSC/VLR容灾恢复，MME支持以下功能： 
 
检测到MSC/VLR故障后，针对故障设备上的用户发送IMSI分离请求指示用户进行IMSI重新附着。
 
 
功能描述 
            
            “容灾恢复配置”用来配置容灾恢复的全局参数，包括容灾恢复的功能开关、恢复速率、备份节点、备份速率、恢复方式等。
        
相关主题 
 
设置容灾恢复配置(SET SERVRSTOCFG)
 
 
查询容灾恢复配置(SHOW SERVRSTOCFG)
 
 
POOL内其他MME及其备份MME配置
 
 
MME支持用户全量数据备份容灾恢复策略配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置容灾恢复配置(SET SERVRSTOCFG) 
### 设置容灾恢复配置(SET SERVRSTOCFG) 
命令功能 
该命令用于设置容灾恢复的功能开关、恢复速率、备份节点、备份速率等基本参数。 
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
SGWRSTOFLAG|支持SGW容灾恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持当SGW故障或重启后对受影响用户进行业务恢复。
PGWRSTOFLAG|支持PGW容灾恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持当PGW故障或重启后对受影响用户进行业务恢复。
MMERSTOFLAG|支持MME容灾恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持当MME故障或重启后对受影响用户进行业务恢复。
PCSCFRSTOFLAG|支持P-CSCF容灾恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持P-CSCF故障后根据HSS的指示对受影响用户进行业务恢复。
PGWTRIGSGWRSTO|支持PGW触发的SGW恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持SGW故障后根据PGW的指示对受影响用户进行业务恢复。
RSTOSCANRATE|容灾恢复扫描速率(用户数/扫描周期/模块)|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|在MME支持SGW和PGW容灾恢复以及MSC/VLR容灾恢复的情况下，MME会扫描UE上下文来判断UE是否需要恢复。该参数用于配置每模块每扫描周期扫描的用户数。
RSTORATE|容灾业务恢复速率(用户数/扫描周期/模块)|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|在MME支持SGW和PGW容灾恢复以及MSC/VLR容灾恢复的情况下，MME扫描UE上下文判断UE是否需要恢复。该参数用于配置每模块每扫描周期业务恢复的用户数。
GWRSTOPGAREA|GW容灾恢复时寻呼范围|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置SGW和PGW容灾恢复时，MME寻呼UE时的寻呼范围。取值如下：系统判断：使用用户当前配置的数据业务寻呼的首次寻呼范围。eNB：基于最近一次活动eNB寻呼。eNB Set：基于最近活动eNB列表寻呼。TA：基于最近一次活动TA寻呼。TA Set：基于最近活动TA列表寻呼。TA List：在TA LIST范围内寻呼。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“GW容灾恢复时寻呼范围”为“基于最近活动eNB列表寻呼”时，该参数用于设置使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
BAKMMEIP|备份MME的MME IP地址|参数可选性:任选参数；参数类型:地址|该参数用于配置用来备份用户动态信息数据的备份MME的IP地址。
BAKRATE|数据备份消息发送频率(毫秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~5000。|该参数用于配置每模块发送数据备份消息的间隔，即消息发送频度。
BAKSIZE|数据备份消息包大小(KB)|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数用于配置数据备份消息中包含的最大字节数。
SGWRELOCTIME|采用SGW重选方式的故障恢复时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:0~60。|该参数用于配置采用SGW重选方式进行故障恢复的SGW故障时长。
BAKAGINGTIME|备份数据老化时长(小时)|参数可选性:任选参数；参数类型:整数；参数范围为:10~240。|该参数用于配置MME保存的备份数据的老化时长，超过老化时长而没有更新的备份数据将被删除。
VLRDETCTIME|VLR局向故障恢复检测时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~60。|该参数用于配置VLR局向故障恢复检测时长，故障时长超过该检测时长的VLR局向，MME将触发注册在该VLR局向上的用户IMSI重新附着来实现SGs口恢复。
命令举例 
设置容灾恢复配置，设置MME支持MME容灾恢复，容灾恢复扫描速率为每模块每扫描周期40个用户，容灾业务恢复速率为每模块每扫描周期5个用户，备份MME的IP地址为“10.10.10.10”，数据备份消息发送频率为1000毫秒，数据备份消息包大小为4KB。 
SET SERVRSTOCFG:MMERSTOFLAG="YES",RSTOSCANRATE=40,RSTORATE=5,BAKMMEIP="10.10.10.10",BAKRATE=1000,BAKSIZE=4; 
父主题： [容灾恢复配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询容灾恢复配置(SHOW SERVRSTOCFG) 
### 查询容灾恢复配置(SHOW SERVRSTOCFG) 
命令功能 
该命令用于查询容灾恢复的功能开关、恢复速率、备份节点、备份速率等基本参数。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SGWRSTOFLAG|支持SGW容灾恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持当SGW故障或重启后对受影响用户进行业务恢复。
PGWRSTOFLAG|支持PGW容灾恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持当PGW故障或重启后对受影响用户进行业务恢复。
MMERSTOFLAG|支持MME容灾恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持当MME故障或重启后对受影响用户进行业务恢复。
PCSCFRSTOFLAG|支持P-CSCF容灾恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持P-CSCF故障后根据HSS的指示对受影响用户进行业务恢复。
PGWTRIGSGWRSTO|支持PGW触发的SGW恢复|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持SGW故障后根据PGW的指示对受影响用户进行业务恢复。
RSTOSCANRATE|容灾恢复扫描速率(用户数/扫描周期/模块)|参数可选性:任选参数；参数类型:整数。|在MME支持SGW和PGW容灾恢复以及MSC/VLR容灾恢复的情况下，MME扫描UE上下文判断UE是否需要恢复。该参数用于配置每模块每扫描周期内扫描的用户数。扫描周期通过命令SHOW SOFTWARE PARAMETER:PARAID=786499进行查询。
RSTORATE|容灾业务恢复速率(用户数/扫描周期/模块)|参数可选性:任选参数；参数类型:整数。|在MME支持SGW和PGW容灾恢复以及MSC/VLR容灾恢复的情况下，MME扫描UE上下文判断UE是否需要恢复。该参数用于配置每模块每扫描周期业务恢复的用户数。
GWRSTOPGAREA|GW容灾恢复时寻呼范围|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置SGW和PGW容灾恢复时，MME寻呼UE时的寻呼范围。取值如下：系统判断：使用用户当前配置的数据业务寻呼的首次寻呼范围。eNB：基于最近一次活动eNB寻呼。eNB Set：基于最近活动eNB列表寻呼。TA：基于最近一次活动TA寻呼。TA Set：基于最近活动TA列表寻呼。TA List：在TA LIST范围内寻呼。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“GW容灾恢复时寻呼范围”为“基于最近活动eNB列表寻呼”时，该参数用于设置使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
BAKMMEIP|备份MME的MME IP地址|参数可选性:任选参数；参数类型:地址|该参数用于配置用来备份用户动态信息数据的备份MME的IP地址。
BAKRATE|数据备份消息发送频率(毫秒)|参数可选性:任选参数；参数类型:整数。|该参数用于配置每模块发送数据备份消息的间隔，即消息发送频度。
BAKSIZE|数据备份消息包大小(KB)|参数可选性:任选参数；参数类型:整数。|该参数用于配置数据备份消息中包含的最大字节数。
SGWRELOCTIME|采用SGW重选方式的故障恢复时长(分钟)|参数可选性:任选参数；参数类型:整数。|该参数用于配置采用SGW重选方式进行故障恢复的SGW故障时长。如果配置为0表示不采用SGW重选方式进行故障恢复。
BAKAGINGTIME|备份数据老化时长(小时)|参数可选性:任选参数；参数类型:整数。|该参数用于配置MME保存的备份数据的老化时长，超过老化时长而没有更新的备份数据将被删除。
VLRDETCTIME|VLR局向故障恢复检测时长(分钟)|参数可选性:任选参数；参数类型:整数。|该参数用于配置VLR局向故障恢复检测时长，故障时长超过该检测时长的VLR局向，MME将触发注册在该VLR局向上的用户IMSI重新附着来实现SGs口恢复。
命令举例 
查询容灾恢复配置。 
SHOW SERVRSTOCFG; 
`命令 (No.1): SHOW SERVRSTOCFG
操作维护  支持SGW容灾恢复   支持PGW容灾恢复   支持MME容灾恢复   支持P-CSCF容灾恢复   支持PGW触发的SGW恢复   容灾恢复扫描速率(用户数/扫描周期/模块)   容灾业务恢复速率(用户数/扫描周期/模块)   GW容灾恢复时寻呼范围   备份MME的MME IP地址   数据备份消息发送频率(毫秒)   数据备份消息包大小(KB)   采用SGW重选方式的故障恢复时长(分钟)   备份数据老化时长(小时)   VLR局向故障恢复检测时长(分钟)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      不支持            不支持            不支持            不支持               不支持                 40                                       5                                        系统判断                                     1000                         4                        0                                     48                       10
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.063 秒）。` 
父主题： [容灾恢复配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### POOL内其他MME及其备份MME配置 
### POOL内其他MME及其备份MME配置 
背景知识 
            
            MME故障容灾时，需要在POOL内的MME之间，进行用户动态信息的备份。通常情况下，采用链式备份的方式，即例如MME1备份MME2，MME2备份MME3，MME3备份MME1。在进行数据备份或查询时，就需要知道MME间的备份关系。
        
功能描述 
本配置用来配置POOL内的所有其他MME节点及其对应的备份节点，以便在容灾恢复时可以： 
 
根据故障节点信息，向其对应的备份节点获取备份数据。
 
 
查询POOL内所有备份节点获取备份数据。
 
 
相关主题 
 
新增POOL内其他MME及其备份MME(ADD POOLBAKMMECFG)
 
 
修改POOL内其他MME及其备份MME(SET POOLBAKMMECFG)
 
 
删除POOL内其他MME及其备份MME(DEL POOLBAKMMECFG)
 
 
查询POOL内其他MME及其备份MME(SHOW POOLBAKMMECFG)
 
 
父主题： [容灾恢复配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增POOL内其他MME及其备份MME(ADD POOLBAKMMECFG) 
#### 新增POOL内其他MME及其备份MME(ADD POOLBAKMMECFG) 
命令功能 
该命令用于新增本MME所在POOL内的其他MME的GTPC地址，以及其他MME对应的备份MME的GTPC地址。
注意事项 
执行该命令时，需要保证MME故障容灾的License功能开关打开，对应的License项为“MME支持MME容灾故障恢复功能 ”。
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEIP|MME的GTPC地址|参数可选性:必选参数；参数类型:地址|该参数用于配置本MME所在的POOL内的其他MME的GTPC地址。
BAKMMEIP|备份MME的GTPC地址|参数可选性:必选参数；参数类型:地址|该参数用于配置该MME（即为参数“MME的GTPC地址”所对应的MME）在POOL内的对应的备份MME的GTPC地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名。
命令举例 
新增本MME所在POOL内的其他MME的GTPC地址为1.1.1.1，该其他MME对应的备份MME的GTPC地址为2.2.2.2。 
ADD POOLBAKMMECFG:MMEIP="1.1.1.1",BAKMMEIP="2.2.2.2"; 
父主题： [POOL内其他MME及其备份MME配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改POOL内其他MME及其备份MME(SET POOLBAKMMECFG) 
#### 修改POOL内其他MME及其备份MME(SET POOLBAKMMECFG) 
命令功能 
该命令用于修改本MME所在POOL内的其他MME的GTPC地址，以及其他MME对应的备份MME的GTPC地址。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEIP|MME的GTPC地址|参数可选性:必选参数；参数类型:地址|该参数用于配置本MME所在的POOL内的其他MME的GTPC地址。
BAKMMEIP|备份MME的GTPC地址|参数可选性:任选参数；参数类型:地址|该参数用于配置该MME（即为参数“MME的GTPC地址”所对应的MME）在POOL内的对应的备份MME的GTPC地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名。
命令举例 
本MME所在POOL内的其他MME的GTPC地址为1.1.1.1，将该其他MME对应的备份MME的GTPC地址改为3.3.3.3。 
SET POOLBAKMMECFG:MMEIP="1.1.1.1",BAKMMEIP="3.3.3.3"; 
父主题： [POOL内其他MME及其备份MME配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除POOL内其他MME及其备份MME(DEL POOLBAKMMECFG) 
#### 删除POOL内其他MME及其备份MME(DEL POOLBAKMMECFG) 
命令功能 
该命令用于删除本MME所在POOL内的其他MME的GTPC地址，以及其他MME对应的备份MME的GTPC地址。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEIP|MME的GTPC地址|参数可选性:必选参数；参数类型:地址|该参数用于配置本MME所在的POOL内的其他MME的GTPC地址。
命令举例 
删除本MME所在POOL内的其他MME信息，该其他MME的GTPC地址为1.1.1.1。 
DEL POOLBAKMMECFG:MMEIP="1.1.1.1"; 
父主题： [POOL内其他MME及其备份MME配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询POOL内其他MME及其备份MME(SHOW POOLBAKMMECFG) 
#### 查询POOL内其他MME及其备份MME(SHOW POOLBAKMMECFG) 
命令功能 
该命令用于查询本MME所在POOL内的其他MME的GTPC地址，以及其他MME对应的备份MME的GTPC地址。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEIP|MME的GTPC地址|参数可选性:任选参数；参数类型:地址|该参数用于配置本MME所在的POOL内的其他MME的GTPC地址。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMEIP|MME的GTPC地址|参数可选性:任选参数；参数类型:地址|该参数用于配置本MME所在的POOL内的其他MME的GTPC地址。
BAKMMEIP|备份MME的GTPC地址|参数可选性:任选参数；参数类型:地址|该参数用于配置该MME（即为参数“MME的GTPC地址”所对应的MME）在POOL内的对应的备份MME的GTPC地址。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用户别名。
命令举例 
查询本MME所在POOL内的其他MME及其备份MME的GTPC地址。 
SHOW POOLBAKMMECFG; 
`
命令 (No.1): SHOW POOLBAKMMECFG
操作维护         MME的GTPC地址   备份MME的GTPC地址   用户别名
-------------------------------------------------------------
复制 修改 删除   1.1.1.1         2.2.2.2             
-------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.142 秒）。
` 
父主题： [POOL内其他MME及其备份MME配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME支持用户全量数据备份容灾恢复策略配置 
### MME支持用户全量数据备份容灾恢复策略配置 
背景知识 
MME支持用户全量数据备份容灾时，MME会把用户的全量数据备份到另一个MME。当MME故障后，其他MME可以从故障MME的备份MME恢复用户全量数据。其他MME从备份MME恢复用户全量数据后，可以让用户不必重新附着、PDN连接建立等，即可使用户继续使用各种业务。 
功能描述 
该配置设置MME支持用户全量数据备份容灾时的各种策略，包括功能开关等。 
相关主题 
 
设置MME支持用户全量数据备份容灾恢复策略配置(SET CMPBACKUPRESTOPLY)
 
 
查询MME支持用户全量数据备份容灾恢复策略配置(SHOW CMPBACKUPRESTOPLY)
 
 
父主题： [容灾恢复配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置MME支持用户全量数据备份容灾恢复策略配置(SET CMPBACKUPRESTOPLY) 
#### 设置MME支持用户全量数据备份容灾恢复策略配置(SET CMPBACKUPRESTOPLY) 
命令功能 
该命令用于修改MME支持用户全量数据备份容灾恢复策略配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
IFSPRTCMPBACKUP|MME支持用户全量数据备份容灾|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识MME是否支持用户全量数据备份容灾功能。该参数设置为开启，则MME会把用户的全量数据备份到另一个MME。当MME故障后，其他MME可以从备份MME恢复用户全量数据，用户不必重新附着即可继续业务。
命令举例 
设置MME支持用户全量数据备份容灾恢复策略配置，MME支持用户全量数据备份容灾为否。 
SET CMPBACKUPRESTOPLY:IFSPRTCMPBACKUP="NO" 
父主题： [MME支持用户全量数据备份容灾恢复策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MME支持用户全量数据备份容灾恢复策略配置(SHOW CMPBACKUPRESTOPLY) 
#### 查询MME支持用户全量数据备份容灾恢复策略配置(SHOW CMPBACKUPRESTOPLY) 
命令功能 
该命令用于查询MME支持用户全量数据备份容灾恢复策略配置。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IFSPRTCMPBACKUP|MME支持用户全量数据备份容灾|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识MME是否支持用户全量数据备份容灾功能。该参数设置为开启，则MME会把用户的全量数据备份到另一个MME。当MME故障后，其他MME可以从备份MME恢复用户全量数据，用户不必重新附着即可继续业务。
命令举例 
查询MME支持用户全量数据备份容灾恢复策略配置。 
SHOW CMPBACKUPRESTOPLY 
`
命令 (No.1): SHOW CMPBACKUPRESTOPLY
操作维护       MME支持用户全量数据备份容灾 
-------------------------------------------
修改           是                          
-------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [MME支持用户全量数据备份容灾恢复策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 信令跟踪消息上报限制配置 
## 信令跟踪消息上报限制配置 
背景知识 
由于信令跟踪消息上报都需要通过OMP，最终上报给OMM。如果上报的消息不进行限制将会导致OMP的CPU持续冲高，影响OMP的正常功能甚至导致OMP宕机。 
功能描述 
配置需要被限制的信令跟踪类型，允许通过的信令数量，CPU门限等。 
相关主题 
 
设置信令跟踪消息上报限制(SET ST RESTRICTION)
 
 
查询信令跟踪消息上报限制(SHOW ST RESTRICTION)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置信令跟踪消息上报限制(SET ST RESTRICTION) 
### 设置信令跟踪消息上报限制(SET ST RESTRICTION) 
命令功能 
该命令用于修改信令跟踪消息上报限制的配置
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SERVICE|被限制的信令跟踪类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|被限制的信令跟踪类型：可选择STS跟踪，CTS跟踪
MODE|限制方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|限制的信令上报的方式：可选择根据CPU占用限制，根据上报数目限制
命令举例 
修改被限制的信令跟踪类型为STS，命令如下： 
SET ST RESTRICTION:SERVICE="STS"; 
父主题： [信令跟踪消息上报限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询信令跟踪消息上报限制(SHOW ST RESTRICTION) 
### 查询信令跟踪消息上报限制(SHOW ST RESTRICTION) 
命令功能 
该命令用于查询信令跟踪消息上报限制的配置
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SERVICE|被限制的信令跟踪类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|被限制的信令跟踪类型：可选择STS跟踪，CTS跟踪
MODE|限制方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|限制的信令上报的方式：可选择根据CPU占用限制，根据上报数目限制
命令举例 
查询信令跟踪消息上报限制，命令如下： 
SHOW ST RESTRICTION; 
父主题： [信令跟踪消息上报限制配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MME失败原因细化配置 
## MME失败原因细化配置 
背景知识 
UE收到MME返回的拒绝消息后，会根据其中携带的EMM Cause完成相应的处理；不同的EMM Cause对于UE的影响不同；在某些特定场景下，需要携带特定的EMM Cause，以控制其对UE的影响。 
功能描述 
本功能用于配置特定失败场景下，MME返回给UE的拒绝消息中，携带的EMM Cause。 
相关主题 
 
设置特定场景失败原因值(SET SPEC REJ CAUSE)
 
 
查询特定场景失败原因值(SHOW SPEC REJ CAUSE)
 
 
设置特定场景切换失败原因值(SET MME HANDOVER FAILCAUSE MAP)
 
 
查询特定场景切换失败原因值(SHOW MME HANDOVER FAILCAUSE MAP)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置特定场景失败原因值(SET SPEC REJ CAUSE) 
### 设置特定场景失败原因值(SET SPEC REJ CAUSE) 
命令功能 
设置特定场景失败原因值
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SITUATION|场景|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|特定的失败场景。
CAUSE|拒绝原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该场景下，MME返回给UE的拒绝消息中携带的EMM Cause。
命令举例 
设置TAU鉴权超时后，返回给UE的TAU Reject消息中携带的EMM Cause为10 Implicitly detached。 
SET SPEC REJ CAUSE:SITUATION="TAU_AUTH_TIMEOUT",CAUSE="10_RejectCause"; 
父主题： [MME失败原因细化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询特定场景失败原因值(SHOW SPEC REJ CAUSE) 
### 查询特定场景失败原因值(SHOW SPEC REJ CAUSE) 
命令功能 
查询特定场景失败原因值
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SITUATION|场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|特定的失败场景。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SITUATION|场景|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|特定的失败场景。
CAUSE|拒绝原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该场景下，MME返回给UE的拒绝消息中携带的EMM Cause。
命令举例 
查询当前特定场景的失败原因值配置。 
SHOW SPEC REJ CAUSE; 
`
命令 (No.1): SHOW SPEC REJ CAUSE
操作维护  场景                       拒绝原因值
-----------------------------------------------
修改      附着时鉴权超时             Network failure
修改      跟踪区更新时鉴权超时       Network failure
修改      业务请求时鉴权超时         Network failure
修改      附着时鉴权同步失败         Network failure
修改      跟踪区更新时鉴权同步失败   Network failure
修改      业务请求时鉴权同步失败     Network failure
-----------------------------------------------
记录数 6
命令执行成功（耗时 0.053 秒）。
` 
父主题： [MME失败原因细化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置特定场景切换失败原因值(SET MME HANDOVER FAILCAUSE MAP) 
### 设置特定场景切换失败原因值(SET MME HANDOVER FAILCAUSE MAP) 
命令功能 
该命令用于设置特定场景切换失败原因值。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SITUATION|场景|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|特定的切换失败场景。
S1APCAUSE|拒绝原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|在切换失败时，给eNodeB的S1AP拒绝原因值。
命令举例 
设置目标eNB返回原因值为“Cell not available”的切换失败”的场景的切换失败原因值为“Cell not available”。 
SET MME HANDOVER FAILCAUSE MAP:SITUATION="CellNotValid",S1APCAUSE="CellNotValid"; 
父主题： [MME失败原因细化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询特定场景切换失败原因值(SHOW MME HANDOVER FAILCAUSE MAP) 
### 查询特定场景切换失败原因值(SHOW MME HANDOVER FAILCAUSE MAP) 
命令功能 
该命令用于查询特定场景切换失败原因值。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SITUATION|场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|特定的切换失败场景。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SITUATION|场景|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|特定的切换失败场景。
S1APCAUSE|拒绝原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|在切换失败时，给eNodeB的S1AP拒绝原因值。
命令举例 
查询切换失败原因值配置。 
SHOW MME HANDOVER FAILCAUSE MAP; 
`
命令 (No.1): SHOW MME HANDOVER FAILCAUSE MAP
操作维护  场景                                                                                             拒绝原因值
---------------------------------------------------------------------------------------------------------------------
修改      SGW返回失败响应                                                                                  Handover Failure In Target EPC/eNB Or Target System
修改      等待SGW响应超时                                                                                  Handover Failure In Target EPC/eNB Or Target System
修改      目标eNB返回原因值为"Unspecified"的切换失败                                                       Unspecified
修改      目标eNB返回原因值为"Handover Failure In Target EPC/eNB Or Target System"的切换失败               Handover Failure In Target EPC/eNB Or Target System
修改      目标eNB返回原因值为"Handover Target not allowed"的切换失败                                       Handover Target not allowed
修改      目标eNB返回原因值为"Cell not available"的切换失败                                                Cell not available
修改      目标eNB返回原因值为"Unknown Target ID"的切换失败                                                 Unknown Target ID
修改      目标eNB返回原因值为"No radio resources available in target cell"的切换失败                       No radio resources available in target cell
修改      目标eNB返回原因值为"Radio resources not available"的切换失败                                     Radio resources not available
修改      目标eNB返回原因值为"Failure in the Radio Interface Procedure"的切换失败                          Failure in the Radio Interface Procedure
修改      目标eNB返回原因值为"Encryption and/or integrity protection algorithms not supported"的切换失败   Encryption and/or integrity protection algorithms not supported
修改      目标eNB返回原因值为"Invalid CSG Id"的切换失败                                                    Invalid CSG Id
修改      等待Target eNB切换响应超时                                                                       Handover Failure In Target EPC/eNB Or Target System
修改      等待Target MME/SGSN切换响应超时                                                                  Handover Failure In Target EPC/eNB Or Target System
修改      Target MME/SGSN返回切换失败响应                                                                  Handover Failure In Target EPC/eNB Or Target System
---------------------------------------------------------------------------------------------------------------------
记录数 15
命令执行成功（耗时 0.053 秒）。
` 
父主题： [MME失败原因细化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## PGW重选配置 
## PGW重选配置 
背景知识 
PGW重选是指因为PGW的某些原因而导致PDN建立失败时，MME选择其他的PGW继续尝试PDN建立，而不是等UE再次发起PDN建立请求，MME重选PGW可以降低PDN建立的时延，提升用户感受度。 
功能描述 
                在运营商购买了PGW重选功能License情况下，可以通过命令
                [SET SOFTWARE PARAMETER]
                :PARAID=786762,PARAVALUE=1;打开PGW重选功能。打开后，通过本功能可以设置或查询重选PGW的PGW失败原因。
            
相关主题 
 
设置PGW重选原因值(SET RESELECTION CAUSE)
 
 
查询PGW重选原因值(SHOW RESELECTION CAUSE)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置PGW重选原因值(SET RESELECTION CAUSE) 
### 设置PGW重选原因值(SET RESELECTION CAUSE) 
命令功能 
设置本局支持PGW重选功能后，必须要存在PGW重选原因配置，才能对相应原因的会话建立失败进行PGW重选，使用重选后的PGW继续会话创建。 
当MME开启了PGW重选功能后，需要设置PGW重选原因值。 
注意事项 
如果本局是Combo局，该功能仅影响LTE网络的用户，对其他网络的用户不会产生影响。  
参数说明 
标识|名称|类型|说明
---|---|---|---
CAUSELIST|原因列表|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局支持重选的会话创建失败原因列表。无默认值取值含义：System failure：PGW系统失败。No resources available：PGW没有资源可用了。Remote peer not responding：PGW无响应。APN Congestion ：PGW发生APN拥塞。
命令举例 
设置PGW重选原因值：原因值列表为"PGW系统失败"。 
SET RESELECTION CAUSE:CAUSELIST="SYS_FAIL"; 
父主题： [PGW重选配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询PGW重选原因值(SHOW RESELECTION CAUSE) 
### 查询PGW重选原因值(SHOW RESELECTION CAUSE) 
命令功能 
查询PGW重选原因值
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CAUSELIST|原因列表|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局支持重选的会话创建失败原因列表。无默认值取值含义：System failure：PGW系统失败。No resources available：PGW没有资源可用了。Remote peer not responding：PGW无响应。APN Congestion ：PGW发生APN拥塞。
命令举例 
查询PGW重选原因值： 
SHOW RESELECTION CAUSE; 
`
命令 (No.1): SHOW RESELECTION CAUSE
操作维护  原因列表
------------------
修改      System failure(72)
------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
父主题： [PGW重选配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 内部统计参数配置 
## 内部统计参数配置 
背景知识 
业务前台有大量的内部统计，用于开发维护人员更详细的知悉系统运行状况、性能话务情况等，但是这些内部统计的采集获取很不方便。 
开启内部统计上报后，前台会将内部统计数据周期性的上报给后台网管，后台网管保存在硬盘目录，供开发维护人员查询分析，这样就方便更好的监控了解系统运行状况、性能话务情况等。 
功能描述 
本功能用于配置内部统计上报参数，主要是内部统计上报周期和是否开启内部统计开关。 
相关主题 
 
设置内部统计参数(SET INNER STAT PARAM)
 
 
查询内部统计参数(SHOW INNER STAT PARAM)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置内部统计参数(SET INNER STAT PARAM) 
### 设置内部统计参数(SET INNER STAT PARAM) 
命令功能 
设置内部统计参数。用于设置是否开启内部统计上报，及内部统计上报周期。开启内部统计上报后，前台会将内部统计数据周期性的上报给后台网管，后台网管保存在硬盘目录，供开发维护人员查询分析，方便更好的监控了解系统运行状况、性能话务情况。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PERIOD|内部统计周期(分钟)|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示内部统计上报周期。
ENABLE|启用内部统计|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否支持内部统计上报。
命令举例 
设置内部统计参数，内部统计周期为30分钟，启用内部统计为是。 
SET INNER STAT PARAM:PERIOD="30MIN",ENABLE="YES"; 
父主题： [内部统计参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询内部统计参数(SHOW INNER STAT PARAM) 
### 查询内部统计参数(SHOW INNER STAT PARAM) 
命令功能 
查询内部统计参数。用于查询是否开启内部统计上报，及内部统计上报周期。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PERIOD|内部统计周期(分钟)|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示内部统计上报周期。
ENABLE|启用内部统计|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示是否支持内部统计上报。
命令举例 
查询内部统计参数。 
SHOW INNER STAT PARAM; 
`
2016-09-28 17:10:37 命令 (No.1): SHOW INNER STAT PARAM
操作维护  内部统计周期(分钟)   启用内部统计
-------------------------------------------
修改      30                   是
-------------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [内部统计参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## GTP原因值与NAS原因值映射配置 
## GTP原因值与NAS原因值映射配置 
背景知识 
            
            3GPP TS 29.274协议规定的GTP原因值与NAS原因值的映射存在一对多的映射关系，不同客户可能倾向不同的映射关系，需要系统支持客户根据实际需要配置GTP到NAS的失败原因值映射关系。
        
功能描述 
MME发起会话管理流程，SGW处理失败时，给MME返回的应答消息中携带GTP失败原因值，MME根据配置将GTP失败原因值映射成NASESM失败原因值发送给UE。 
GTP原因值对应的NAS原因值取值范围原则上根据协议要求进行限定，但考虑到系统兼容，部分GTP原因值对应的NAS原因值取值范围除协议要求值外还增加了系统兼容值。 
相关主题 
 
设置GTP原因值与NAS原因值映射(SET GTP NAS CAUSE MAPPING)
 
 
查询GTP原因值与NAS原因值映射(SHOW GTP NAS CAUSE MAPPING)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置GTP原因值与NAS原因值映射(SET GTP NAS CAUSE MAPPING) 
### 设置GTP原因值与NAS原因值映射(SET GTP NAS CAUSE MAPPING) 
命令功能 
该命令用于修改GTP原因值与NAS原因值映射关系。当需要修改GTP原因值与NAS原因值映射关系时，使用该命令。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPCAUSE|GTP原因值|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP原因值。
PROCEDURE|适用流程|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP原因值映射NAS原因值适用的流程。如果GTP原因值为“#64 "Context not found"”时，协议规定非3GPP到3GPP的初始PDN连接请求流程，与非3GPP到3GPP的初始PDN连接请求外其他流程映射的原因值不同。对于其他GTP原因值，映射NAS原因值不区分场景。
NASCAUSE|NAS原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP原因值对应的NAS原因值。
命令举例 
设置GTP原因值与NAS原因值映射，GTP原因值为GTPCAUSE_64，适用流程为PROCEDURE_1，NAS原因值设置为NASCAUSE_54。 
SET GTP NAS CAUSE MAPPING:GTPCAUSE="GTPCAUSE_64",PROCEDURE="PROCEDURE_1",NASCAUSE="NASCAUSE_54"; 
父主题： [GTP原因值与NAS原因值映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询GTP原因值与NAS原因值映射(SHOW GTP NAS CAUSE MAPPING) 
### 查询GTP原因值与NAS原因值映射(SHOW GTP NAS CAUSE MAPPING) 
命令功能 
该命令用于查询配置的GTP原因值与NAS原因值映射关系。
注意事项 
无
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPCAUSE|GTP原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP原因值。
PROCEDURE|适用流程|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP原因值映射NAS原因值适用的流程。如果GTP原因值为“#64 "Context not found"”时，协议规定非3GPP到3GPP的初始PDN连接请求流程，与非3GPP到3GPP的初始PDN连接请求外其他流程映射的原因值不同。对于其他GTP原因值，映射NAS原因值不区分场景。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GTPCAUSE|GTP原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP原因值。
PROCEDURE|适用流程|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP原因值映射NAS原因值适用的流程。如果GTP原因值为“#64 "Context not found"”时，协议规定非3GPP到3GPP的初始PDN连接请求流程，与非3GPP到3GPP的初始PDN连接请求外其他流程映射的原因值不同。对于其他GTP原因值，映射NAS原因值不区分场景。
NASCAUSE|NAS原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP原因值对应的NAS原因值。
命令举例 
查询GTP原因值与NAS原因值映射。 
SHOW GTP NAS CAUSE MAPPING:GTPCAUSE="GTPCAUSE_64",PROCEDURE="PROCEDURE_1"; 
`
命令 (No.1):SHOW GTP NAS CAUSE MAPPING:GTPCAUSE="GTPCAUSE_64",PROCEDURE="PROCEDURE_1";
操作维护   GTP原因值              适用流程                                NAS原因值 
-----------------------------------------------------------------------------------------------------------------
修改      64 Context not found  仅适用非3GPP到3GPP的初始PDN连接请求流程  54 PDN connection does not exist 
-----------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.021 秒）。
` 
父主题： [GTP原因值与NAS原因值映射配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## KPI监控维护 
## KPI监控维护 
背景知识 
本功能开启时，持续监控业务各项KPI，在判断出某模块KPI异常时，上报告警或自动采取措施恢复业务。 
功能描述 
配置KPI监控维护功能的全局参数，如是否开启本功能，检测周期参数等。 
配置KPI监控维护功能的策略，如附着流程的KPI策略，采用的维护动作。 
相关主题 
 
KPI监控维护全局参数
 
 
KPI监控维护策略配置
 
 
UP KPI监控维护策略
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### KPI监控维护全局参数 
### KPI监控维护全局参数 
背景知识 
本功能开启时，持续监控业务各项KPI，在判断出某模块KPI异常时，上报告警或自动采取措施恢复业务。 
功能描述 
配置KPI监控维护功能的全局参数，如是否开启本功能，检测周期和次数、冷却周期、最大闭塞模块个数。 
相关主题 
 
设置KPI监控维护全局参数(SET KPIMONCFG)
 
 
查询KPI监控维护全局参数(SHOW KPIMONCFG)
 
 
父主题： [KPI监控维护]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置KPI监控维护全局参数(SET KPIMONCFG) 
#### 设置KPI监控维护全局参数(SET KPIMONCFG) 
命令功能 
设置KPI监控维护功能的全局参数配置，包括是否开启本功能、检测周期和次数等参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
FLAG|KPI监控维护开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置是否启用KPI监控维护功能。
PERIOD|检测周期(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|配置监控KPI的检测周期。
COLTIME|检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|配置连续几次检测到异常才执行维护动作。
COOLING|冷却周期(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~60。|在执行一次维护动作动作后，必须等待冷却周期后才能继续执行下一次维护动作。
命令举例 
设置KPI监控维护功能的全局参数配置，KPI监控维护开关是开启，检测周期是4，检测次数是2，冷却周期(分钟)是12。 
SET KPIMONCFG:FLAG="ON",PERIOD=4,COLTIME=2,COOLING=12; 
父主题： [KPI监控维护全局参数]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询KPI监控维护全局参数(SHOW KPIMONCFG) 
#### 查询KPI监控维护全局参数(SHOW KPIMONCFG) 
命令功能 
查询当前KPI监控维护功能的全局参数配置。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FLAG|KPI监控维护开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置是否启用KPI监控维护功能。
PERIOD|检测周期(分钟)|参数可选性:任选参数；参数类型:整数。|配置监控KPI的检测周期。
COLTIME|检测次数|参数可选性:任选参数；参数类型:整数。|配置连续几次检测到异常才执行维护动作。
COOLING|冷却周期(分钟)|参数可选性:任选参数；参数类型:整数。|在执行一次维护动作动作后，必须等待冷却周期后才能继续执行下一次维护动作。
命令举例 
查询当前KPI监控维护功能的全局参数配置。 
SHOW KPIMONCFG; 
`
2018-10-23 11:30:05 命令 (No.1): SHOW KPIMONCFG
操作维护  KPI监控维护开关   检测周期(分钟)   检测次数   冷却周期(分钟)
----------------------------------------------------------------------
修改      开启              4                2          12            
----------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.022 秒）。
` 
父主题： [KPI监控维护全局参数]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### KPI监控维护策略配置 
### KPI监控维护策略配置 
背景知识 
本功能开启时，持续监控业务各项KPI，在判断出某模块KPI异常时，上报告警或自动采取措施恢复业务。 
功能描述 
配置KPI监控维护功能的策略，如附着流程的KPI策略，采用的维护动作。 
相关主题 
 
设置KPI监控维护策略(SET KPIMONPOLICY)
 
 
查询KPI监控维护策略(SHOW KPIMONPOLICY)
 
 
父主题： [KPI监控维护]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置KPI监控维护策略(SET KPIMONPOLICY) 
#### 设置KPI监控维护策略(SET KPIMONPOLICY) 
命令功能 
设置KPI监控维护功能的策略配置，如附着流程的KPI策略。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
KPITYPE|KPI类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|使用的KPI类型。
RATE|维护动作执行的过滤条件(最低业务次数)|参数可选性:任选参数；参数类型:整数；参数范围为:1~5000。|配置维护动作执行的过滤条件，必须要大于最低的条件才能启动功能，对业务KPI来说，就是指最低的业务发起次数/分钟/模块。
PERCENT|维护执行过滤条件(KPI低于门限%)|参数可选性:任选参数；参数类型:整数；参数范围为:1~50。|配置维护执行过滤条件（KPI低于门限%），必须要小于该的条件才能启动功能，对业务KPI来说，就是指成功率门限。
ACTION|维护动作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置维护执行的动作，默认只告警。
命令举例 
设置KPI监控维护功能的策略配置，KPI类型选择2G Attach，维护动作执行的过滤条件是50，维护执行过滤条件是10，维护动作是不启用。 
SET KPIMONPOLICY:KPITYPE="2G_ATTACH",RATE=50,PERCENT=10,ACTION="NO_ACTION"; 
父主题： [KPI监控维护策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询KPI监控维护策略(SHOW KPIMONPOLICY) 
#### 查询KPI监控维护策略(SHOW KPIMONPOLICY) 
命令功能 
查询当前KPI监控维护功能的策略配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
KPITYPE|KPI类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|使用的KPI类型。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
KPITYPE|KPI类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|使用的KPI类型。
RATE|维护动作执行的过滤条件(最低业务次数)|参数可选性:任选参数；参数类型:整数。|配置维护动作执行的过滤条件，必须要大于最低的条件才能启动功能，对业务KPI来说，就是指最低的业务发起次数/分钟/模块。
PERCENT|维护执行过滤条件(KPI低于门限%)|参数可选性:任选参数；参数类型:整数。|配置维护执行过滤条件（KPI低于门限%），必须要小于该的条件才能启动功能，对业务KPI来说，就是指成功率门限。
ACTION|维护动作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|配置维护执行的动作，默认只告警。
命令举例 
查询当前KPI监控维护功能的策略配置。 
SHOW KPIMONPOLICY; 
`
2018-10-23 11:19:26 命令 (No.1): SHOW KPIMONPOLICY
操作维护  KPI类型         维护动作执行的过滤条件(最低业务次数)   维护执行过滤条件(KPI低于门限%)   维护动作
----------------------------------------------------------------------------------------------------------
修改      2G Attach       50                                     10                               不启用
修改      3G Attach       600                                    50                               告警
修改      4G Attach       5000                                   50                               告警并重启模块
修改      2G PDN Active   60                                     20                               告警
修改      3G PDN Active   40                                     20                               告警并重启模块
----------------------------------------------------------------------------------------------------------
记录数 5
命令执行成功（耗时 0.041 秒）。
` 
父主题： [KPI监控维护策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### UP KPI监控维护策略 
### UP KPI监控维护策略 
背景知识 
本功能开启时，MME会持续监控UP的流量指标，在MME判断出某个UP模块流量异常时，会上报告警或自动采取措施，以避免影响业务。 
功能描述 
本功能用于配置UP 流量监控维护功能的策略，如2G的流量策略。 
相关主题 
 
设置UP KPI监控维护策略(SET UPKPIMONPOLICY)
 
 
查询UP KPI监控维护策略(SHOW UPKPIMONPOLICY)
 
 
父主题： [KPI监控维护]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置UP KPI监控维护策略(SET UPKPIMONPOLICY) 
#### 设置UP KPI监控维护策略(SET UPKPIMONPOLICY) 
命令功能 
本命令用于修改UP KPI监控维护功能的策略配置，如2G用户的流量策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
KPITYPE|KPI类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|本参数用于配置监控的KPI类型。2G：监控网络的2G数据流量3G：监控网络的3G数据流量
MINRATE|告警的最低流量(Mbps)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|本参数用于配置MME上报告警的最小流量阈值，至少有其中一个UP模块超过了本参数配置的流量值，MME才会上报告警。
DIFPERCENT|差异门限|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|本参数用于配置差异门限，即当前流程和均值流程的差异的比例，如果当前某个UP模块的流量比均值小，且超过该比例，MME为认为数据流量为异常。
命令举例 
设置UP KPI监控维护策略，KPI类型选择2G流量，告警的最低流量为5Mbps，差异门限为50。 
SET UPKPIMONPOLICY:KPITYPE="2G",MINRATE=5,DIFPERCENT=50; 
父主题： [UP KPI监控维护策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询UP KPI监控维护策略(SHOW UPKPIMONPOLICY) 
#### 查询UP KPI监控维护策略(SHOW UPKPIMONPOLICY) 
命令功能 
本命令用于查询当前UP KPI监控维护功能的策略。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
KPITYPE|KPI类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|本参数用于配置监控的KPI类型。2G：监控网络的2G数据流量3G：监控网络的3G数据流量
输出参数说明 
标识|名称|类型|说明
---|---|---|---
KPITYPE|KPI类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|本参数用于配置监控的KPI类型。2G：监控网络的2G数据流量3G：监控网络的3G数据流量
MINRATE|告警的最低流量(Mbps)|参数可选性:任选参数；参数类型:整数。|本参数用于配置MME上报告警的最小流量阈值，至少有其中一个UP模块超过了本参数配置的流量值，MME才会上报告警。
DIFPERCENT|差异门限|参数可选性:任选参数；参数类型:整数。|本参数用于配置差异门限，即当前流程和均值流程的差异的比例，如果当前某个UP模块的流量比均值小，且超过该比例，MME为认为数据流量为异常。
命令举例 
查询UP KPI监控维护策略。 
SHOW UPKPIMONPOLICY; 
`
命令 (No.1):  SHOW UPKPIMONPOLICY
KPI类型   告警的最低流量(Mbps)  差异门限
----------------------------------------
2G流量    5                     50
----------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [UP KPI监控维护策略]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 内部资源监测配置 
## 内部资源监测配置 
背景知识 
MME/SGSN系统中有各种数据区、缓存、标识索引等类型的临时资源，这种资源的生命周期是临时分配的，在使用时才申请，使用完毕后就会释放掉，正常情况下这种类型的资源可以重复循环使用。 
但是在某些异常场景下，可能导致临时资源未被正确释放，资源会长期残留。久而久之，系统资源会被最终耗尽，导致系统无资源可用。 
所以，MME/SGSN系统提供了自愈机制，来解决该问题。MME/SGSN对系统中的临时资源进行定时扫描监测，对于长时间处于占用状态没有正常释放的临时资源，或者处于不健康状态下的资源，系统予以回收再利用。 
功能描述 
本节点用于配置MME/SGSN内部资源监测功能，可以对Buffer资源和索引资源进行监测。 
相关主题 
 
设置内部资源监测配置(SET MME INNERRESCMONI)
 
 
查询内部资源监测配置(SHOW MME INNERRESCMONI)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置内部资源监测配置(SET MME INNERRESCMONI) 
### 设置内部资源监测配置(SET MME INNERRESCMONI) 
命令功能 
该命令用于设置MME/SGSN内部资源监测配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|内部资源ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|内部资源的唯一标识。
NAME|内部资源名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~64个字符。|内部资源的名称。
SUPPMONITOR|内部资源是否支持监测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持回收内部资源。
AGETIME|内部资源监测老化时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|该参数用于设置内部资源的老化回收时长。
命令举例 
将ID为1的内部资源的监测老化时长修改为60分钟。 
SET MME INNERRESCMONI:ID=1,AGETIME=60; 
父主题： [内部资源监测配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询内部资源监测配置(SHOW MME INNERRESCMONI) 
### 查询内部资源监测配置(SHOW MME INNERRESCMONI) 
命令功能 
该命令用于查询MME/SGSN内部资源监测配置。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|内部资源ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|内部资源的唯一标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|内部资源ID|参数可选性:任选参数；参数类型:整数。|内部资源的唯一标识。
NAME|内部资源名称|参数可选性:任选参数；参数类型:字符型。|内部资源的名称。
SUPPMONITOR|内部资源是否支持监测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置是否支持回收内部资源。
AGETIME|内部资源监测老化时长(分钟)|参数可选性:任选参数；参数类型:整数。|该参数用于设置内部资源的老化回收时长。
命令举例 
查询ID为1的内部资源是否支持监测以及监测老化时长。 
SHOW MME INNERRESCMONI:ID=1;  
`
(No.1) : SHOW MME INNERRESCMONI:ID=1
-----------------NFS_MMESGSN_0----------------
操作维护  内部资源ID 内部资源名称 内部资源是否支持监测 内部资源监测老化时长（分钟）
-----------------------------------------------------------------------------------
修改      1          MME_Buffer   支持                  60
-----------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-11-10 17:09:40 耗时: 0.241 秒
` 
父主题： [内部资源监测配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## CDU租户配置 
## CDU租户配置 
背景知识 
租户（Tenant）是指使用系统或计算资源的用户。不同租户的数据访问和数据存储都是隔离的，从而保证数据的安全。 
功能描述 
本功能用于设置MME/SGSN使用的CDU租户ID，默认情况下租户ID为1，必须和实际CDU上配置的租户ID保持一致。 
相关主题 
 
设置CDU租户配置(SET CDUTENANTID)
 
 
查询CDU租户配置(SHOW CDUTENANTID)
 
 
POOL内其他MME的CDU租户配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置CDU租户配置(SET CDUTENANTID) 
### 设置CDU租户配置(SET CDUTENANTID) 
命令功能 
设置当前MME/SGSN使用的CDU租户ID。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
CDUTENANTID|CDU租户ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置CDU租户ID。
命令举例 
设置当前MME/SGSN使用的CDU租户ID为22。 
SET CDUTENANTID:CDUTENANTID=22; 
父主题： [CDU租户配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询CDU租户配置(SHOW CDUTENANTID) 
### 查询CDU租户配置(SHOW CDUTENANTID) 
命令功能 
查询当前MME/SGSN使用的CDU租户ID。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CDUTENANTID|CDU租户ID|参数可选性:任选参数；参数类型:整数。|该参数用于设置CDU租户ID。
命令举例 
查询当前MME/SGSN使用的CDU租户ID。 
SHOW CDUTENANTID; 
`
命令 (No.27): SHOW CDUTENANTID
CDU租户ID    
---------------
1            
---------------
命令执行成功（耗时 0.047 秒）。
 ` 
父主题： [CDU租户配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### POOL内其他MME的CDU租户配置 
### POOL内其他MME的CDU租户配置 
背景知识 
MME实现了计算和存储分离，数据存储在CDU单元。不同MME局向使用不同的CDU租户，实现数据隔离。 
MME支持用户全量数据备份容灾时，MME的CDU会把用户的全量数据备份到MME POOL内另一个MME的CDU。当MME故障后，其他MME可以从备份MME的CDU恢复用户全量数据，可以让用户不必重新附着即可继续业务。 
MME从其他MME的CDU恢复用户全量数据，需要配置其他MME的CDU租户信息。 
功能描述 
对于MME支持用户全量数据的容灾恢复时，MME POOL中每个MME需配置每个MME使用的CDU租户信息。 
相关主题 
 
新增POOL内其他MME的CDU租户配置(ADD POOLCDUTENANTID)
 
 
修改POOL内其他MME的CDU租户配置(SET POOLCDUTENANTID)
 
 
删除POOL内其他MME的CDU租户配置(DEL POOLCDUTENANTID)
 
 
查询POOL内其他MME的CDU租户配置(SHOW POOLCDUTENANTID)
 
 
父主题： [CDU租户配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增POOL内其他MME的CDU租户配置(ADD POOLCDUTENANTID) 
#### 新增POOL内其他MME的CDU租户配置(ADD POOLCDUTENANTID) 
命令功能 
该命令用于新增POOL内其他MME的CDU租户。对MME POOL中其他MME，或MME POOL中新增了MME时，通过本命令增加其CDU租户信息。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEC|MME编号|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|该参数用于在网络中标识MME的编号。
CDUTENANTID|CDU租户ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置CDU租户ID。
NAME|别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|别名。自定义名称，命名应方便维护人员理解和记忆。
命令举例 
新增POOL内其他MME的CDU租户配置，MME编号为1，CDU租户ID为1，别名为test。 
ADD POOLCDUTENANTID:MMEC=1,CDUTENANTID=1,NAME="test" 
父主题： [POOL内其他MME的CDU租户配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改POOL内其他MME的CDU租户配置(SET POOLCDUTENANTID) 
#### 修改POOL内其他MME的CDU租户配置(SET POOLCDUTENANTID) 
命令功能 
该命令用于修改POOL内其他MME的CDU租户配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEC|MME编号|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|该参数用于在网络中标识MME的编号。
CDUTENANTID|CDU租户ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置CDU租户ID。
NAME|别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|别名。自定义名称，命名应方便维护人员理解和记忆。
命令举例 
修改POOL内其他MME的CDU租户配置，MME编号为1，CDU租户ID为1，别名为test。 
SET POOLCDUTENANTID:MMEC=1,CDUTENANTID=1,NAME="test" 
父主题： [POOL内其他MME的CDU租户配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除POOL内其他MME的CDU租户配置(DEL POOLCDUTENANTID) 
#### 删除POOL内其他MME的CDU租户配置(DEL POOLCDUTENANTID) 
命令功能 
该命令用于删除POOL内其他MME的CDU租户配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEC|MME编号|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|该参数用于在网络中标识MME的编号。
命令举例 
删除POOL内其他MME的CDU租户配置，MME编号为1。 
DEL POOLCDUTENANTID:MMEC=1 
父主题： [POOL内其他MME的CDU租户配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询POOL内其他MME的CDU租户配置(SHOW POOLCDUTENANTID) 
#### 查询POOL内其他MME的CDU租户配置(SHOW POOLCDUTENANTID) 
命令功能 
该命令用于查询POOL内其他MME的CDU租户配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEC|MME编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于在网络中标识MME的编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMEC|MME编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于在网络中标识MME的编号。
CDUTENANTID|CDU租户ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于设置CDU租户ID。
NAME|别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|别名。自定义名称，命名应方便维护人员理解和记忆。
命令举例 
查询POOL内其他MME的CDU租户配置，MME编号为1。 
SHOW POOLCDUTENANTID:MMEC=1 
`
命令 (No.15): SHOW POOLCDUTENANTID:MMEC=1
操作维护       MME编号 CDU租户ID 别名 
--------------------------------------
复制 修改      1       1         test  
--------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [POOL内其他MME的CDU租户配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 负荷卸载优化 
## 负荷卸载优化 
背景知识 
Pool功能最初是在2G/3G时代引入的。移动网络支持Pool功能后，一个RAN节点连接到多个SGSN节点，由RAN实现节点选择和路由功能。SGSN在分配新P-TMSI给用户时，包含了本SGSN节点的标识NRI，用户通过RAN节点接入到SGSN时，RAN从P-TMSI/TLLI中分离出NRI，根据NRI将信令消息路由到正确的SGSN节点上。 
                对于SGSN POOL内节点的负荷重分配，将某个SGSN节点上的用户迁移到其他SGSN上时，可通过网管命令
                [EXEC UNLOAD]
                对SGSN进行负荷卸载。通过触发用户发起附着或路由更新过程，分配NULL NRI给用户，从而在用户的下一次路由更新过程中将用户迁移到其他可用的SGSN局。
            
对于EPS网络来说，由于在网络设计之初就考虑的对Pool的必然支持，所以对Pool功能的支持又有了进一步的优化和增强。MME负荷卸载方式如下： 
 
eNodeB与MME建立动态偶联，通过S1消息获取GUMMEI和权重，无需静态配置。
 
 
通过特殊原因值的S1释放即可立即触发。
 
 
UE通过不携带MME节点信息给eNodeB的方式，指示eNodeB重选。
 
 
当启动负荷卸载时，由于卸载初期，网络中频繁活动用户较多，用户主动上线，核心网在业务流程结束后，对用户发起负荷卸载，这时用户会集中接入到新局，会导致新局负荷瞬间冲高，造成拥塞。因此，需要对频繁活动用户卸载过程进行控制。 
功能描述 
该节点用于配置负荷卸载过程中的卸载控制参数，包括： 
 
                        SGSN负荷卸载优化配置，通过命令
                        SET SGSN UNLOAD OPT
                        进行配置。
                    
 
 
                        MME负荷卸载优化配置，通过命令
                        SET MME UNLOAD OPT
                        进行配置
                    
 
 
相关主题 
 
MME卸载优化配置
 
 
SGSN卸载优化配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME卸载优化配置 
### MME卸载优化配置 
背景知识 
MME Pool区域是指UE在其间移动不需要改变服务MME的区域，一个MME Pool区域内有一个或多个对等的MME，MME池区是由多个TA汇聚，Pool区域内的每个eNB都与所有的MME互联。 
MME Pool的主要优点在于： 
 
UE在MME Pool内移动时，通常不需要切换MME节点，可以有效减少系统间的信令交互。
 
 
可以有效实现MME网元级的容灾和负荷分担。
 
 
MME Pool的功能主要包括三部分： 
 
MME Pool负荷分担功能，使用户可以较均衡的分布在各个MME上，保证了在MME Pool内各个MME上的负荷和处理能力的一致性。
 
 
MME负荷重平衡功能，通过将某个MME的全部或部分特定用户迁移到Pool内其他MME的方式，以减少该MME下用户的数量，从而减少该MME升级或其它情况下对用户业务的影响。
 
 
MME容灾功能，当Pool内某MME不可用后，Pool内其他MME能够支持故障MME下用户发起的业务。
 
 
当启动负荷卸载时，卸载初期，由于网络中频繁活动用户较多，触发ATTACH\TAU\Service req等业务，用户完成卸载后，集中到新局进行TAU，会导致新局负荷瞬间冲高，造成拥塞。因此，需要对频繁活动用户卸载过程进行控制。 
功能描述 
本功能用于对MME进行负荷卸载前，进行MME负荷卸载优化配置，设置负荷卸载控制周期、每周期令牌投放次数、允许卸载突发系数，然后进行负荷卸载，根据控制参数对负荷卸载过程进行速率控制。 
相关主题 
 
设置MME卸载优化配置(SET MME UNLOAD OPT)
 
 
查询MME卸载优化配置(SHOW MME UNLOAD OPT)
 
 
父主题： [负荷卸载优化]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置MME卸载优化配置(SET MME UNLOAD OPT) 
#### 设置MME卸载优化配置(SET MME UNLOAD OPT) 
命令功能 
该命令用于设置MME卸载优化配置中的各个控制参数，当需要对MME进行负荷卸载时，使用此命令。配置成功后，可对MME负荷卸载过程的速率进行控制。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
MMEUNLOADOPT|支持负荷卸载优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持负荷卸载优化功能。
MMECTLPERIOD|负荷卸载控制周期（s）|参数可选性:任选参数；参数类型:整数；参数范围为:1~60。|该参数用于在MME支持负荷卸载优化时，设置负荷卸载速率控制的周期。在控制周期内根据卸载速率提供固定的卸载令牌数。周期结束后，相应令牌数清0。默认值为10秒。
MMETOKENPERIOD|周期令牌投放次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~600。|该参数用于在MME支持负荷卸载优化时，设置负荷控制周期内令牌投放次数。默认值为10。令牌投放数量的计算方法为：控制周期内令牌总数*（负荷卸载控制周期/每周期令牌投放次数）控制周期内令牌总数的计算方法为: 负荷卸载步长 * 负荷卸载控制周期
MMETOKENBKTTIMES|允许卸载突发系数|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该参数用于在MME支持负荷卸载优化时，设置负荷控制周期内允许用户突增的系数。默认值为1。用户突增时，固定令牌投放周期投放的令牌不够用，此时需增加令牌投放，最大投放数量为单次投放的令牌数*允许卸载突发系数。
命令举例 
设置MME卸载优化配置，支持负荷卸载优化设置为支持。 
SET MME UNLOAD OPT:MMEUNLOADOPT="SUPPORT" 
父主题： [MME卸载优化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MME卸载优化配置(SHOW MME UNLOAD OPT) 
#### 查询MME卸载优化配置(SHOW MME UNLOAD OPT) 
命令功能 
该命令用于查询MME卸载优化配置中的各个控制参数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
MMEUNLOADOPT|支持负荷卸载优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持负荷卸载优化功能。
MMECTLPERIOD|负荷卸载控制周期（s）|参数可选性:任选参数；参数类型:整数。|该参数用于在MME支持负荷卸载优化时，设置负荷卸载速率控制的周期。在控制周期内根据卸载速率提供固定的卸载令牌数。周期结束后，相应令牌数清0。默认值为10秒。
MMETOKENPERIOD|周期令牌投放次数|参数可选性:任选参数；参数类型:整数。|该参数用于在MME支持负荷卸载优化时，设置负荷控制周期内令牌投放次数。默认值为10。令牌投放数量的计算方法为：控制周期内令牌总数*（负荷卸载控制周期/每周期令牌投放次数）控制周期内令牌总数的计算方法为: 负荷卸载步长 * 负荷卸载控制周期
MMETOKENBKTTIMES|允许卸载突发系数|参数可选性:任选参数；参数类型:整数。|该参数用于在MME支持负荷卸载优化时，设置负荷控制周期内允许用户突增的系数。默认值为1。用户突增时，固定令牌投放周期投放的令牌不够用，此时需增加令牌投放，最大投放数量为单次投放的令牌数*允许卸载突发系数。
命令举例 
查询MME卸载优化配置。 
SHOW MME UNLOAD OPT 
`
命令 (No.1): SHOW MME UNLOAD OPT
操作维护 支持负荷卸载优化    负荷卸载控制周期（s）    周期令牌投放次数    允许卸载突发系数 
--------------------------------------------------------------------------------------------
修改     支持                  10                      10                   3  
--------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.024 秒）。
` 
父主题： [MME卸载优化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### SGSN卸载优化配置 
### SGSN卸载优化配置 
背景知识 
RNC/BSC（Radio Network Controller/Base Station Controller，无线网络控制器/基站控制器）在启用Iu-Gb Flex功能的情况下，SGSN分配新PTMSI给用户时，包含了本SGSN节点的NRI。用户通过RNC/BSC接入到SGSN时，RNC/BSC从PTMSI中分离出NRI，根据NRI将信令消息路由到正确的SGSN节点。 
当需要对POOL内SGSN节点的负荷进行重分配，即将某个SGSN节点上的用户迁移到其他SGSN上时，可对SGSN进行负荷卸载。SGSN的负荷卸载过程，即触发用户发起附着或路由更新过程，分配NULL NRI给用户，从而在用户下一次进行路由更新时能将用户迁移到其他可用的SGSN。 
当启动负荷卸载时，卸载初期，由于网络中频繁活动用户较多，触发ATTACH\RAU\Service req等业务，分配NULL NRI给用户后，用户集中到新局进行RAU，会导致新局负荷瞬间冲高，造成拥塞。因此，需要对频繁活动用户卸载过程进行控制。 
功能描述 
本功能用于对SGSN进行负荷卸载前，进行SGSN负荷卸载优化配置，设置负荷卸载控制周期、周期令牌投放次数、允许卸载突发系数，然后进行负荷卸载，根据控制参数对负荷卸载过程进行速率控制。 
相关主题 
 
设置SGSN卸载优化配置(SET SGSN UNLOAD OPT)
 
 
查询SGSN卸载优化配置(SHOW SGSN UNLOAD OPT)
 
 
父主题： [负荷卸载优化]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置SGSN卸载优化配置(SET SGSN UNLOAD OPT) 
#### 设置SGSN卸载优化配置(SET SGSN UNLOAD OPT) 
命令功能 
该命令用于设置SGSN卸载优化配置中的各个控制参数，当需要对SGSN进行负荷卸载时，使用此命令。配置成功后，可对SGSN负荷卸载过程的速率进行控制。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNUNLOADOPT|支持负荷卸载优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持负荷卸载优化功能。
SGSNCTLPERIOD|负荷卸载控制周期（s）|参数可选性:任选参数；参数类型:整数；参数范围为:1~60。|该参数用于在SGSN支持负荷卸载优化时，设置负荷卸载速率控制的周期。在控制周期内根据卸载速率提供固定的卸载令牌数。周期结束后，相应令牌数清0。默认值为10秒。
SGSNTOKENPERIOD|周期令牌投放次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~600。|该参数用于在SGSN支持负荷卸载优化时，设置负荷控制周期内令牌投放次数。默认值为10。令牌投放数量的计算方法为：控制周期内令牌总数*（负荷卸载控制周期/每周期令牌投放次数）控制周期内令牌总数的计算方法为: 负荷卸载步长 * 负荷卸载控制周期
SGSNTOKENBKTTIMES|允许卸载突发系数|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该参数用于在SGSN支持负荷卸载优化时，设置负荷控制周期内允许用户突增的系数。默认值为1。用户突增时，固定令牌投放周期投放的令牌不够用，此时需增加令牌投放，最大投放数量为单次投放的令牌数*允许卸载突发系数。
命令举例 
设置SGSN卸载优化配置，支持负荷卸载优化设置为支持。 
SET SGSN UNLOAD OPT:SGSNUNLOADOPT="SUPPORT" 
父主题： [SGSN卸载优化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询SGSN卸载优化配置(SHOW SGSN UNLOAD OPT) 
#### 查询SGSN卸载优化配置(SHOW SGSN UNLOAD OPT) 
命令功能 
该命令用于查询SGSN卸载优化配置中的各个控制参数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SGSNUNLOADOPT|支持负荷卸载优化|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持负荷卸载优化功能。
SGSNCTLPERIOD|负荷卸载控制周期（s）|参数可选性:任选参数；参数类型:整数。|该参数用于在SGSN支持负荷卸载优化时，设置负荷卸载速率控制的周期。在控制周期内根据卸载速率提供固定的卸载令牌数。周期结束后，相应令牌数清0。默认值为10秒。
SGSNTOKENPERIOD|周期令牌投放次数|参数可选性:任选参数；参数类型:整数。|该参数用于在SGSN支持负荷卸载优化时，设置负荷控制周期内令牌投放次数。默认值为10。令牌投放数量的计算方法为：控制周期内令牌总数*（负荷卸载控制周期/每周期令牌投放次数）控制周期内令牌总数的计算方法为: 负荷卸载步长 * 负荷卸载控制周期
SGSNTOKENBKTTIMES|允许卸载突发系数|参数可选性:任选参数；参数类型:整数。|该参数用于在SGSN支持负荷卸载优化时，设置负荷控制周期内允许用户突增的系数。默认值为1。用户突增时，固定令牌投放周期投放的令牌不够用，此时需增加令牌投放，最大投放数量为单次投放的令牌数*允许卸载突发系数。
命令举例 
查询SGSN卸载优化配置。 
SHOW SGSN UNLOAD OPT 
`
命令 (No.1): SHOW SGSN UNLOAD OPT
操作维护 支持负荷卸载优化    负荷卸载控制周期（s）    周期令牌投放次数    允许卸载突发系数 
--------------------------------------------------------------------------------------------
修改     支持                  10                      10                   3  
--------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.024 秒）。
` 
父主题： [SGSN卸载优化配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## GTP源端口策略配置 
## GTP源端口策略配置 
相关主题 
 
设置GTP源端口默认策略(SET DEFAULT GTP SRCPORT)
 
 
查询GTP源端口默认策略(SHOW DEFAULT GTP SRCPORT)
 
 
新增GTP源端口策略(ADD GTP SRCPORT)
 
 
修改GTP源端口策略(SET GTP SRCPORT)
 
 
删除GTP源端口策略(DEL GTP SRCPORT)
 
 
查询GTP源端口策略(SHOW GTP SRCPORT)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置GTP源端口默认策略(SET DEFAULT GTP SRCPORT) 
### 设置GTP源端口默认策略(SET DEFAULT GTP SRCPORT) 
命令功能 
该命令用于设置MME/SGSN在发送请求消息时，源端口号使用知名端口号还是非知名端口号。该配置适用于本局发送的所有GTP请求消息。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPSRCPORTTYPE|GTP源端口默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP请求IP报文中源端口的默认类型。非知名端口知名端口
命令举例 
设置GTP源端口默认策略为知名端口。 
SET DEFAULT GTP SRCPORT:GTPSRCPORTTYPE="KNOWN"; 
父主题： [GTP源端口策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询GTP源端口默认策略(SHOW DEFAULT GTP SRCPORT) 
### 查询GTP源端口默认策略(SHOW DEFAULT GTP SRCPORT) 
命令功能 
该命令用于查询GTP源端口默认策略，即GTP请求消息中源端口号默认使用知名端口号还是非知名端口号。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GTPSRCPORTTYPE|GTP源端口默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP请求IP报文中源端口的默认类型。非知名端口知名端口
命令举例 
查询GTP源端口默认策略。 
SHOW DEFAULT GTP SRCPORT; 
`
命令 (No.1): SHOW DEFAULT GTP SRCPORT
GTP源端口默认策略 
---------------------------------
知名端口 
---------------------------------
记录数 1
命令执行成功（耗时 0.091 秒）。
` 
父主题： [GTP源端口策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增GTP源端口策略(ADD GTP SRCPORT) 
### 新增GTP源端口策略(ADD GTP SRCPORT) 
命令功能 
该命令用于新增GTP源端口策略，当MME/SGSN向指定GTP节点发送GTP请求消息时，指定GTP节点源端口号使用知名端口号还是非知名端口号。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPIPADDR|GTP节点IP地址|参数可选性:必选参数；参数类型:地址|周边GTP协议网元（SGW、MME、GGSN等）的控制面IP地址。IP地址包括IPv4和IPv6类型。
GTPSRCPORTTYPE|GTP源端口策略|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:UNKNOWN。|该参数用于设置GTP请求IP报文中源端口的类型。非知名端口知名端口
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户为GTP源端口策略设置的别名，便用区别不同的GTP源端口策略，无其他意义。
命令举例 
增加GTP源端口策略，GTP节点IP地址为10.20.11.22，GTP源端口策略为知名端口。 
ADD GTP SRCPORT:GTPIPADDR="10.20.11.22",GTPSRCPORTTYPE="KNOWN"; 
父主题： [GTP源端口策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改GTP源端口策略(SET GTP SRCPORT) 
### 修改GTP源端口策略(SET GTP SRCPORT) 
命令功能 
该命令用于修改GTP源端口策略，当MME/SGSN向指定GTP节点发送GTP请求消息时，修改指定GTP节点源端口号使用知名端口号还是非知名端口号。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPIPADDR|GTP节点IP地址|参数可选性:必选参数；参数类型:地址|周边GTP协议网元（SGW、MME、GGSN等）的控制面IP地址。IP地址包括IPv4和IPv6类型。
GTPSRCPORTTYPE|GTP源端口策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP请求IP报文中源端口的类型。非知名端口知名端口
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户为GTP源端口策略设置的别名，便用区别不同的GTP源端口策略，无其他意义。
命令举例 
修改GTP源端口策略，GTP节点IP地址为10.20.11.22，GTP源端口策略为知名端口。 
SET GTP SRCPORT:GTPIPADDR="10.20.11.22",GTPSRCPORTTYPE="KNOWN"; 
父主题： [GTP源端口策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除GTP源端口策略(DEL GTP SRCPORT) 
### 删除GTP源端口策略(DEL GTP SRCPORT) 
命令功能 
该命令用于删除指定GTP节点的源端口号策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPIPADDR|GTP节点IP地址|参数可选性:必选参数；参数类型:地址|周边GTP协议网元（SGW、MME、GGSN等）的控制面IP地址。IP地址包括IPv4和IPv6类型。
命令举例 
删除GTP源端口策略，GTP节点IP地址为10.20.11.22。 
DEL GTP SRCPORT:GTPIPADDR="10.20.11.22"; 
父主题： [GTP源端口策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询GTP源端口策略(SHOW GTP SRCPORT) 
### 查询GTP源端口策略(SHOW GTP SRCPORT) 
命令功能 
该命令用于查询指定GTP节点源端口号策略配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
GTPIPADDR|GTP节点IP地址|参数可选性:任选参数；参数类型:地址|周边GTP协议网元（SGW、MME、GGSN等）的控制面IP地址。IP地址包括IPv4和IPv6类型。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GTPIPADDR|GTP节点IP地址|参数可选性:任选参数；参数类型:地址|周边GTP协议网元（SGW、MME、GGSN等）的控制面IP地址。IP地址包括IPv4和IPv6类型。
GTPSRCPORTTYPE|GTP源端口策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置GTP请求IP报文中源端口的类型。非知名端口知名端口
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户为GTP源端口策略设置的别名，便用区别不同的GTP源端口策略，无其他意义。
命令举例 
查询GTP源端口策略。 
SHOW GTP SRCPORT; 
`
命令 (No.1): SHOW GTP SRCPORT
GTP节点IP地址   GTP源端口策略   用户别名
----------------------------------------
10.20.11.22     知名端口 
----------------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [GTP源端口策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## PDN连接拒绝Back-off策略配置 
## PDN连接拒绝Back-off策略配置 
背景知识 
UE发起附着或者PDN连接请求，由于非拥塞控制被拒绝时，通过携带Back-off timer满足不同场景下的需求： 
 
MME由于APN未签约的原因拒绝PDN连接建立，通过在PDN connectivity reject消息中携带Back-off timer触发UE侧的T3396时器，UE无需重启，在定时器超时后即会使用该APN再次接入网络，可以提升用户的业务体验。
 
 
MME由于其他原因拒绝PDN连接建立，通过在PDN connectivity reject消息中携带Back-off timer通知用户延迟发起业务，可以避免对系统的影响。
 
 
功能描述 
“PDN连接拒绝Back-off策略配置”包括： 
 
拒绝PDN连接建立时，Back-off策略的缺省配置。
 
 
基于APN/ESM原因灵活配置PDN connectivity reject消息中是否携带Back-off timer，以及Back-off timer取值。
 
 
相关主题 
 
设置缺省PDN连接拒绝Back-off策略配置(SET DEFAULT PDN REJ BACKOFF)
 
 
查询缺省PDN连接拒绝Back-off策略配置(SHOW DEFAULT PDN REJ BACKOFF)
 
 
新增PDN连接拒绝Back-off策略配置(ADD PDN REJ BACKOFF)
 
 
修改PDN连接拒绝Back-off策略配置(SET PDN REJ BACKOFF)
 
 
删除PDN连接拒绝Back-off策略配置(DEL PDN REJ BACKOFF)
 
 
查询PDN连接拒绝Back-off策略配置(SHOW PDN REJ BACKOFF)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置缺省PDN连接拒绝Back-off策略配置(SET DEFAULT PDN REJ BACKOFF) 
### 设置缺省PDN连接拒绝Back-off策略配置(SET DEFAULT PDN REJ BACKOFF) 
命令功能 
该命令用于设置拒绝PDN连接建立时，Back-off策略的缺省配置。当附着或者PDN连接被拒绝，拒绝原因是非拥塞控制时，需要配置MME在PDN connectivity reject消息中是否携带Back-off timer时，使用该命令进行配置。 
注意事项 
附着或者PDN连接由于拥塞控制被拒绝时，PDN connectivity reject消息中Back-off timer的携带不受本命令控制。 
“Back-off timer最小取值（秒）”和“Back-off timer最大取值（秒）”可以配置为不同或相同。 
 
取值不同时，MME在取值范围内取随机值下发Back-off timer给终端。
 
 
取值相同时，MME取配置的固定值下发Back-off timer给终端。取固定值下发时会导致用户在同一时间集中发起PDN连接重试，对网络会造成冲击。因此，建议无特殊要求不要将最小值和最大值配置为相同。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPPDNREJBACKOFFPLY|支持PDN连接拒绝Back-off策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持PDN连接拒绝Back-off策略控制。
CARRYBACKOFF|携带Back-off timer|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在PDN connectivity reject消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最小取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最大取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
该命令用于设置缺省PDN连接拒绝Back-off策略配置，其中支持PDN连接拒绝Back-off策略控制，APN未签约时不携带Back-off timer。 
SET DEFAULT PDN REJ BACKOFF:SUPPDNREJBACKOFFPLY="YES",CARRYBACKOFF="NO"; 
父主题： [PDN连接拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询缺省PDN连接拒绝Back-off策略配置(SHOW DEFAULT PDN REJ BACKOFF) 
### 查询缺省PDN连接拒绝Back-off策略配置(SHOW DEFAULT PDN REJ BACKOFF) 
命令功能 
该命令用于查询拒绝PDN连接建立时，Back-off策略的缺省配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPPDNREJBACKOFFPLY|支持PDN连接拒绝Back-off策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持PDN连接拒绝Back-off策略控制。
CARRYBACKOFF|携带Back-off timer|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在PDN connectivity reject消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于设置下发给终端的Back-off timer的最小取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于设置下发给终端的Back-off timer的最大取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
该命令用于查询缺省PDN连接拒绝Back-off策略配置。 
SHOW DEFAULT PDN REJ BACKOFF; 
`
(No.8) : SHOW DEFAULT PDN REJ BACKOFF:
-----------------combo26/NFS_MMESGSN_0----------------
操作维护       支持PDN连接拒绝Back-off策略控制 APN未签约时携带Back-off timer Back-off timer最小取值（秒） Back-off timer最大取值（秒） 
---------------------------------------------------------------------------------------------------------------------------------------
修改           是                              是                            100                          200                          
---------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-10-20 15:34:34 耗时: 1.026秒
` 
父主题： [PDN连接拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增PDN连接拒绝Back-off策略配置(ADD PDN REJ BACKOFF) 
### 新增PDN连接拒绝Back-off策略配置(ADD PDN REJ BACKOFF) 
命令功能 
该命令用于新增拒绝PDN连接建立时，Back-off策略的配置。当附着或者PDN连接由于非拥塞控制被拒绝，需要根据APN/ESM原因灵活配置MME在PDN connectivity reject消息中是否携带Back-off timer时，使用该命令进行配置。 
注意事项 
附着或者PDN连接请求由于拥塞控制被拒绝时，PDN connectivity reject消息中Back-off timer的携带不受本命令控制。 
可以基于APN和ESM原因2个维度进行配置，优先级从高到低顺序为：APN+ESM原因、APN、ESM原因。 
最多配置1024条记录。 
“Back-off timer最小取值（秒）”和“Back-off timer最大取值（秒）”可以配置为不同或相同。 
 
取值不同时MME在取值范围内取随机值下发Back-off timer给终端。
 
 
取值相同时MME取配置的固定值下发Back-off timer给终端。取固定值下发时会导致用户在同一时间集中发起PDN连接重试，对网络会造成冲击。因此，建议无特殊要求不要将最小值和最大值配置为相同。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ESMCAUSE|ESM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:ALLCAUSE。|ESM原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDN type29: user authentication or authorization failed30: request rejected by Serving GW or PDN GW31: request rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: PTI already in use38: network failure53: ESM information not received55: multiple PDN connections for a given APN not allowed66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
CARRYBACKOFF|携带Back-off timer|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在PDN connectivity reject消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最小取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最大取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
新增PDN连接拒绝Back-off策略配置，APN名称为zte，ESM原因为ALL CAUSE，APN未签约时不携带Back-off timer。 
ADD PDN REJ BACKOFF:APN="zte",ESMCAUSE="ALLCAUSE",CARRYBACKOFF="NO"; 
父主题： [PDN连接拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改PDN连接拒绝Back-off策略配置(SET PDN REJ BACKOFF) 
### 修改PDN连接拒绝Back-off策略配置(SET PDN REJ BACKOFF) 
命令功能 
该命令用于修改拒绝PDN连接建立时，Back-off策略的配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ESMCAUSE|ESM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ESM原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDN type29: user authentication or authorization failed30: request rejected by Serving GW or PDN GW31: request rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: PTI already in use38: network failure53: ESM information not received55: multiple PDN connections for a given APN not allowed66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
CARRYBACKOFF|携带Back-off timer|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在PDN connectivity reject消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置下发给终端的Back-off timer的最小取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置下发给终端的Back-off timer的最大取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
修改“APN名称为zte，ESM原因为ALL CAUSE”的PDN连接拒绝Back-off策略配置记录，将APN未签约时携带Back-off timer修改为“是”。 
SET PDN REJ BACKOFF:APN="zte",ESMCAUSE="ALLCAUSE",CARRYBACKOFF="YES"; 
父主题： [PDN连接拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除MME PDN连接拒绝Back-off策略配置(DEL PDN REJ BACKOFF) 
### 删除MME PDN连接拒绝Back-off策略配置(DEL PDN REJ BACKOFF) 
命令功能 
该命令用于删除拒绝PDN连接建立时，Back-off策略的配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ESMCAUSE|ESM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ESM原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDN type29: user authentication or authorization failed30: request rejected by Serving GW or PDN GW31: request rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: PTI already in use38: network failure53: ESM information not received55: multiple PDN connections for a given APN not allowed66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
命令举例 
删除“APN名称为zte，ESM原因为ALL CAUSE”的PDN连接拒绝Back-off策略配置记录。 
DEL PDN REJ BACKOFF:APN="zte",ESMCAUSE="ALLCAUSE"; 
父主题： [PDN连接拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询MME PDN连接拒绝Back-off策略配置(SHOW PDN REJ BACKOFF) 
### 查询MME PDN连接拒绝Back-off策略配置(SHOW PDN REJ BACKOFF) 
命令功能 
该命令用于查询拒绝PDN连接建立时，Back-off策略的配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ESMCAUSE|ESM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ESM原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDN type29: user authentication or authorization failed30: request rejected by Serving GW or PDN GW31: request rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: PTI already in use38: network failure53: ESM information not received55: multiple PDN connections for a given APN not allowed66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~62个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
ESMCAUSE|ESM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ESM原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDN type29: user authentication or authorization failed30: request rejected by Serving GW or PDN GW31: request rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: PTI already in use38: network failure53: ESM information not received55: multiple PDN connections for a given APN not allowed66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
CARRYBACKOFF|携带Back-off timer|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME在PDN connectivity reject消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置下发给终端的Back-off timer的最小取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置下发给终端的Back-off timer的最大取值。当PDN连接建立由于APN未签约被拒绝需要在PDN connectivity reject消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择，终端在Back-off timer时间内不再使用相同APN发起业务。配置的Back-off timer单位为秒，MME需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
查询PDN连接拒绝Back-off策略配置。 
SHOW PDN REJ BACKOFF; 
`
(No.9) : SHOW PDN REJ BACKOFF:
-----------------combo26/NFS_MMESGSN_0----------------
操作维护       APN名称 ESM原因                APN未签约时携带Back-off timer Back-off timer最小取值（秒） Back-off timer最大取值（秒） 
--------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 zte     ALL cause              否                            0                            0                                                    
--------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-10-20 15:34:55 耗时: 1.165秒
` 
父主题： [PDN连接拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## PDP激活拒绝Back-off策略配置 
## PDP激活拒绝Back-off策略配置 
背景知识 
UE发起PDP激活请求，通过携带Back-off timer满足不同场景下的需求： 
 
SGSN由于APN未签约拒绝PDP激活，通过在PDP激活拒绝消息中携带Back-off timer触发UE侧的T3396时器，UE无需重启在定时器超时后即会使用该APN再次接入网络，可以提升用户的业务体验。
 
 
SGSN由于其他原因拒绝PDP激活，通过在PDP激活拒绝消息中携带Back-off timer通知用户延迟发起业务，可以避免对系统的影响。
 
 
功能描述 
“PDP激活拒绝Back-off策略配置”包括： 
 
拒绝PDP激活时，Back-off策略的缺省配置。
 
 
基于APN/SM原因灵活配置PDP激活拒绝消息中是否携带Back-off timer以及Back-off timer取值。
 
 
相关主题 
 
设置缺省PDP激活拒绝Back-off策略配置(SET DEFAULT PDP REJ BACKOFF)
 
 
查询缺省PDP激活拒绝Back-off策略配置(SHOW DEFAULT PDP REJ BACKOFF)
 
 
新增PDP激活拒绝Back-off策略配置(ADD PDP REJ BACKOFF)
 
 
修改PDP激活拒绝Back-off策略配置(SET PDP REJ BACKOFF)
 
 
删除PDP激活拒绝Back-off策略配置(DEL PDP REJ BACKOFF)
 
 
查询PDP激活拒绝Back-off策略配置(SHOW PDP REJ BACKOFF)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置缺省PDP激活拒绝Back-off策略配置(SET DEFAULT PDP REJ BACKOFF) 
### 设置缺省PDP激活拒绝Back-off策略配置(SET DEFAULT PDP REJ BACKOFF) 
命令功能 
该命令用于设置拒绝PDP激活时，Back-off策略的缺省配置。当PDP激活被拒绝，需要配置SGSN在PDP激活拒绝消息中是否携带Back-off timer时，使用该命令进行配置。 
注意事项 
Back-off timer最小取值（秒）”和“Back-off timer最大取值（秒）”可以配置为不同或相同。 
 
取值不同时SGSN在取值范围内取随机值下发Back-off timer给终端。
 
 
取值相同时SGSN取配置的固定值下发Back-off timer给终端。取固定值下发时会导致用户在同一时间集中发起PDP激活重试，对网络会造成冲击。因此，建议无特殊要求不要将最小值和最大值配置为相同。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
SUPPDPREJBACKOFFPLY|支持PDP连接拒绝Back-off策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持PDP激活拒绝Back-off策略控制。
CARRYBACKOFF|携带Back-off timer|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在PDP激活拒绝消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最小取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最大取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
该命令用于设置缺省PDP激活拒绝Back-off策略配置，其中支持PDP连接拒绝Back-off策略控制，不携带Back-off timer。 
SET DEFAULT PDP REJ BACKOFF:SUPPDPREJBACKOFFPLY="YES",CARRYBACKOFF="NO"; 
父主题： [PDP激活拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询缺省PDP激活拒绝Back-off策略配置(SHOW DEFAULT PDP REJ BACKOFF) 
### 查询缺省PDP激活拒绝Back-off策略配置(SHOW DEFAULT PDP REJ BACKOFF) 
命令功能 
该命令用于查询拒绝PDP激活时，Back-off策略的配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPPDPREJBACKOFFPLY|支持PDP连接拒绝Back-off策略控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持PDP激活拒绝Back-off策略控制。
CARRYBACKOFF|携带Back-off timer|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在PDP激活拒绝消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于设置下发给终端的Back-off timer的最小取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数。|该参数用于设置下发给终端的Back-off timer的最大取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
该命令用于查询缺省PDP激活拒绝Back-off策略配置。 
SHOW DEFAULT PDP REJ BACKOFF; 
`
(No.10) : SHOW DEFAULT PDP REJ BACKOFF:
-----------------combo26/NFS_MMESGSN_0----------------
操作维护       支持PDP连接拒绝Back-off策略控制 携带Back-off timer Back-off timer最小取值（秒） Back-off timer最大取值（秒） 
----------------------------------------------------------------------------------------------------------------------------
修改           否                              否                 0                            0                            
----------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-10-20 15:35:13 耗时: 1.077秒
` 
父主题： [PDP激活拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增PDP激活拒绝Back-off策略配置(ADD PDP REJ BACKOFF) 
### 新增PDP激活拒绝Back-off策略配置(ADD PDP REJ BACKOFF) 
命令功能 
该命令用于新增拒绝PDP激活时，Back-off策略的配置。当PDP激活被拒绝，需要根据APN/SM原因灵活配置SGSN在PDP激活拒绝消息中是否携带Back-off timer时，使用该命令进行配置。 
注意事项 
“Back-off timer最小取值（秒）”和“Back-off timer最大取值（秒）”可以配置为不同或相同。 
 
取值不同时SGSN在取值范围内取随机值下发Back-off timer给终端。
 
 
取值相同时SGSN取配置的固定值下发Back-off timer给终端。取固定值下发时会导致用户在同一时间集中发起PDP激活重试，对网络会造成冲击。因此，建议无特殊要求不要将最小值和最大值配置为相同。
 
 
可以基于APN和SM原因2个维度进行配置，优先级从高到低顺序为：APN+SM原因、APN、SM原因。 
最多配置1024条记录。 
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
SMCAUSE|SM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:ALLCAUSE。|SM 原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDP address or PDP type29: user authentication failed30: activation rejected by GGSN, Serving GW or PDN GW31: activation rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: NSAPI already used66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
CARRYBACKOFF|携带Back-off timer|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在PDP激活拒绝消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最小取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最大取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
新增PDP激活拒绝Back-off策略配置，APN名称为apn1，SM原因为insufficient resources，携带Back-off timer。 
ADD PDP REJ BACKOFF:APN="apn1",SMCAUSE="INRESOURCES",CARRYBACKOFF="YES"; 
父主题： [PDP激活拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改PDP激活拒绝Back-off策略配置(SET PDP REJ BACKOFF) 
### 修改PDP激活拒绝Back-off策略配置(SET PDP REJ BACKOFF) 
命令功能 
该命令用于修改拒绝PDP激活时，Back-off策略的配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
SMCAUSE|SM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SM 原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDP address or PDP type29: user authentication failed30: activation rejected by GGSN, Serving GW or PDN GW31: activation rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: NSAPI already used66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
CARRYBACKOFF|携带Back-off timer|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在PDP激活拒绝消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最小取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。默认值:0。|该参数用于设置下发给终端的Back-off timer的最大取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
修改“APN名称为apn1，SM原因为insufficient resources”的PDP激活拒绝Back-off策略配置，携带Back-off timer修改为“否”。 
SET PDP REJ BACKOFF:APN="apn1",SMCAUSE="INRESOURCES",CARRYBACKOFF="NO"; 
父主题： [PDP激活拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除PDP激活拒绝Back-off策略配置(DEL PDP REJ BACKOFF) 
### 删除PDP激活拒绝Back-off策略配置(DEL PDP REJ BACKOFF) 
命令功能 
该命令用于删除拒绝PDP激活时，Back-off策略的配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
SMCAUSE|SM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SM 原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDP address or PDP type29: user authentication failed30: activation rejected by GGSN, Serving GW or PDN GW31: activation rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: NSAPI already used66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
命令举例 
删除“APN名称为apn1，SM原因为insufficient resources”的PDP激活拒绝Back-off策略配置。 
DEL PDP REJ BACKOFF:APN="apn1",SMCAUSE="INRESOURCES"; 
父主题： [PDP激活拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询PDP激活拒绝Back-off策略配置(SHOW PDP REJ BACKOFF) 
### 查询PDP激活拒绝Back-off策略配置(SHOW PDP REJ BACKOFF) 
命令功能 
该命令用于查询拒绝PDP激活时，Back-off策略的配置。 
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
SMCAUSE|SM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SM 原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDP address or PDP type29: user authentication failed30: activation rejected by GGSN, Serving GW or PDN GW31: activation rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: NSAPI already used66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
输出参数说明 
标识|名称|类型|说明
---|---|---|---
APN|APN名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|该参数用于设置APN NI即Network Identifier，格式为“Label1.Label2.Label3”，可包含多个的标签并且必须符合如下要求。不超过62个字符。不以“rac”、“lac”、“sgsn”或者“rnc”开头。不以“.gprs”结尾。不使用通配符“*”。
SMCAUSE|SM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|SM 原因0: ALL cause8: operator determined barring26: insufficient resources27: missing or unknown APN28: unknown PDP address or PDP type29: user authentication failed30: activation rejected by GGSN, Serving GW or PDN GW31: activation rejected, unspecified32: service option not supported33: requested service option not subscribed34: service option temporarily out of order35: NSAPI already used66: requested APN not supported in current RAT and PLMN combination95:Semantically incorrect message96:Invalid mandatory information97:Message type non-existent or not implemented98:Message type not compatible with the protocol state99:Information element non-existent or not implemented100:Conditional IE error101:Message not compatible with the protocol state111:Protocol error, unspecified112: APN restriction value incompatible with active EPS bearer context113: Multiple accesses to a PDN connection not allowed
CARRYBACKOFF|携带Back-off timer|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN在PDP激活拒绝消息中是否携带Back-off timer。
MINBACKOFF|Back-off timer最小取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置下发给终端的Back-off timer的最小取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
MAXBACKOFF|Back-off timer最大取值（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:0~1116000。|该参数用于设置下发给终端的Back-off timer的最大取值。当需要在PDP激活拒绝消息中携带Back-off timer时，此字段取值在Back-off timer最小取值与Back-off timer最大取值的范围内随机选择。配置的Back-off timer单位为秒，SGSN需要将配置取值转换为3GPP协议24.008定义的格式，转化原则如下：1-62秒，转换后Unit字段取值011（2秒）。例如： 30秒，转换后内容为Unit=011，Timer value=01111。63-930秒，转换后Unit字段取值100（30秒）。例如：500秒，转换后内容为Unit=100，Timer value=10001。931-1860秒，转换后Unit字段取值101（1分钟）。例如：1000秒，转换后内容为Unit=101，Timer value=10001。1861-18600秒，转换后Unit字段取值000（10分钟）。例如：5000秒，转换后内容为Unit=000，Timer value=01001。18601-111600秒，转换后Unit字段取值001（1小时）。例如：18000秒，转换后内容为Unit=001，Timer value=00101。111601-1116000秒，转换后Unit字段取值010（10小时）。例如：300000秒，转换后内容为Unit=010，Timer value=01001。
命令举例 
查询PDP激活拒绝Back-off策略配置。 
SHOW PDP REJ BACKOFF; 
`
(No.11) : SHOW PDP REJ BACKOFF:
-----------------combo26/NFS_MMESGSN_0----------------
操作维护       APN名称 SM原因                 携带Back-off timer Back-off timer最小取值（秒） Back-off timer最大取值（秒） 
---------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 apn1    insufficient resources 是                 1                            62                                               
---------------------------------------------------------------------------------------------------------------------------
记录数：2
执行成功开始时间:2021-10-20 15:35:28 耗时: 1.142秒
` 
父主题： [PDP激活拒绝Back-off策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## S1MME接口管理 
## S1MME接口管理 
背景知识 
当MME对接的i5GC故障或者MME自身故障时，需要闭塞本局MME，基站将UE消息转发给另外一套MME，达到触发容灾的目的。 
功能描述 
本功能用于管理S1MME 偶联，可以将偶联设置为闭塞，解闭塞。 
相关主题 
 
配置S1MME接口管理状态(SET S1MMEMANAGECFG)
 
 
查询S1MME接口管理状态(SHOW S1MMEMANAGECFG)
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## HSS故障旁路配置 
## HSS故障旁路配置 
背景知识 
HSS存储了用户的签约数据，当用户接入4G时，MME从HSS获取签约数据。如果用户归属的HSS均故障，初始接入、跨制式（RAT）互操作、跨AMF/MME移动等移动性管理流程中，MME会由于无法从HSS获取到用户的签约信息，导致这些业务流程失败，从而影响数据、语音业务。 
为了保证用户所属HSS故障时用户基本的通信业务需求，可以通过本地配置用户签约数据。当检测到用户所属HSS故障时，直接使用本地配置的签约数据，继续用户业务流程。 
功能描述 
本配置用于配置HSS故障后旁路配置，包括旁路策略配置、本地用户最小签约配置。 
相关主题 
 
HSS故障旁路策略配置
 
 
EPS签约QoS模板配置
 
 
APN签约模板配置
 
 
HSS故障本地签约数据配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### HSS故障旁路策略配置 
### HSS故障旁路策略配置 
背景知识 
HSS存储了用户的签约数据，当用户接入4G时，MME从HSS获取签约数据。如果用户归属的HSS均故障，初始接入、跨制式（RAT）互操作、跨AMF/MME移动等移动性管理流程中，MME会由于无法从HSS获取到用户的签约信息，导致这些业务流程失败，从而影响数据、语音业务。 
为了保证用户所属HSS故障时用户基本的通信业务需求，可以通过本地配置用户签约数据。当检测到用户所属HSS故障时，直接使用本地配置的签约数据，继续用户业务流程。 
功能描述 
            
            本功能用于配置HSS故障时的旁路策略，包括设置MME是否支持HSS故障时旁路用户、UE触发的附着\跟踪区更新\业务请求流程是否触发HSS恢复探测等。
        
相关主题 
 
设置HSS故障旁路策略配置(SET HSSBPPLYCFG)
 
 
查询HSS故障旁路策略配置(SHOW HSSBPPLYCFG)
 
 
父主题： [HSS故障旁路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置HSS故障旁路策略配置(SET HSSBPPLYCFG) 
#### 设置HSS故障旁路策略配置(SET HSSBPPLYCFG) 
命令功能 
该命令用于设置HSS故障旁路策略配置，包括设置MME是否支持HSS故障时旁路用户、DRA返回的错误响应中指示HSS故障的错误码等。
注意事项 
该功能配置后立即生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SPRTHSSFAULTBP|支持HSS故障旁路用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于控制MME是否支持当HSS故障时旁路用户。修改影响：当参数打开后，若MME检测到用户所述HSS故障，且用户存在有效的安全上下文，则设置用户进入旁路状态。旁路状态的用户触发业务时，业务流程跳过鉴权以及HSS交互过程，若用户无有效签约上下文，则使用本地配置的签约上下文。数据来源：本端规划。默认值：否。配置原则：无。
ERRCODE|指示HSS故障错误码|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于在DRA组网模式下，MME收到DRA失败响应且失败码为本参数配置的错误码时，表示用户归属的HSS已经故障。常用错误码如下：3002：DIAMETER_UNABLE_TO_DELIVER3003：DIAMETER_REALM_NOT_SERVED5003：DIAMETER_AUTHORIZATION_REJECTED5012：DIAMETER_UNABLE_TO_COMPLY修改影响：无。数据来源：全网规划。默认值：3002。配置原则：无。
SCANHSSSPEED|HSS恢复探测扫描步长|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|参数作用：该参数用于控制每SC每秒触发恢复探测的用户个数。修改影响：该参数设置过大，有可能会影响正常用户业务。数据来源：本端规划。默认值：10。配置原则：无。
SCANINTERVAL|HSS恢复探测时间间隔(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~600。|参数作用：本参数用于控制针对同一个处于旁路状态的用户，连续两次触发HSS恢复探测的最小时间间隔，单位为秒。修改影响：该参数设置过小，会导致在HSS未恢复时单个用户发送多个探测消息，增加了系统的负荷。数据来源：本端规划。默认值：60(秒)。配置原则：无。
命令举例 
设置HSS故障旁路策略配置，支持HSS故障旁路用户为否，指示HSS故障错误码为666，HSS恢复探测扫描步长为30，HSS恢复探测时间间隔(秒)为50。 
SET HSSBPPLYCFG:SPRTHSSFAULTBP="NO",ERRCODE=666,SCANHSSSPEED=30,SCANINTERVAL=50 
父主题： [HSS故障旁路策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询HSS故障旁路策略配置(SHOW HSSBPPLYCFG) 
#### 查询HSS故障旁路策略配置(SHOW HSSBPPLYCFG) 
命令功能 
该命令用于查询HSS故障旁路策略配置。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SPRTHSSFAULTBP|支持HSS故障旁路用户|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于控制MME是否支持当HSS故障时旁路用户。修改影响：当参数打开后，若MME检测到用户所述HSS故障，且用户存在有效的安全上下文，则设置用户进入旁路状态。旁路状态的用户触发业务时，业务流程跳过鉴权以及HSS交互过程，若用户无有效签约上下文，则使用本地配置的签约上下文。数据来源：本端规划。默认值：否。配置原则：无。
ERRCODE|指示HSS故障错误码|参数可选性:任选参数；参数类型:整数。|参数作用：本参数用于在DRA组网模式下，MME收到DRA失败响应且失败码为本参数配置的错误码时，表示用户归属的HSS已经故障。常用错误码如下：3002：DIAMETER_UNABLE_TO_DELIVER3003：DIAMETER_REALM_NOT_SERVED5003：DIAMETER_AUTHORIZATION_REJECTED5012：DIAMETER_UNABLE_TO_COMPLY修改影响：无。数据来源：全网规划。默认值：3002。配置原则：无。
SCANHSSSPEED|HSS恢复探测扫描步长|参数可选性:任选参数；参数类型:整数。|参数作用：该参数用于控制每SC每秒触发恢复探测的用户个数。修改影响：该参数设置过大，有可能会影响正常用户业务。数据来源：本端规划。默认值：10。配置原则：无。
SCANINTERVAL|HSS恢复探测时间间隔(秒)|参数可选性:任选参数；参数类型:整数。|参数作用：本参数用于控制针对同一个处于旁路状态的用户，连续两次触发HSS恢复探测的最小时间间隔，单位为秒。修改影响：该参数设置过小，会导致在HSS未恢复时单个用户发送多个探测消息，增加了系统的负荷。数据来源：本端规划。默认值：60(秒)。配置原则：无。
命令举例 
查询HSS故障旁路策略配置。 
SHOW HSSBPPLYCFG 
`
(No.153) : SHOW HSSBPPLYCFG:
-----------------uMAC_Combo_14/NFS_MMESGSN_0----------------
操作维护       支持HSS故障旁路用户    指示HSS故障错误码    HSS恢复探测扫描步长    HSS恢复探测时间间隔(秒)
------------------------------------------------------------------------------------------------------------------------------------
修改           不支持                  666                 20                     60                                              
------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-05-09 11:05:08 耗时: 1.965秒
` 
父主题： [HSS故障旁路策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### EPS签约QoS模板配置 
### EPS签约QoS模板配置 
背景知识 
为了保证用户所属HSS故障时用户基本的通信业务需求，可以通过本地配置用户签约数据。当检测到用户所属HSS故障时，直接使用本地配置的签约数据，继续用户业务流程。 
功能描述 
本功能用于配置EPS签约QoS模板。 
相关主题 
 
新增EPS签约QoS模板配置(ADD EPSSUBQOSPROCFG)
 
 
修改EPS签约QoS模板配置(SET EPSSUBQOSPROCFG)
 
 
删除EPS签约QoS模板配置(DEL EPSSUBQOSPROCFG)
 
 
查询EPS签约QoS模板配置(SHOW EPSSUBQOSPROCFG)
 
 
父主题： [HSS故障旁路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增EPS签约QoS模板配置(ADD EPSSUBQOSPROCFG) 
#### 新增EPS签约QoS模板配置(ADD EPSSUBQOSPROCFG) 
命令功能 
该命令用于新增EPS签约QoS模板。
注意事项 
 
配置完成，且传送变化表或者全部表后生效。
 
 
最多支持配置2048个记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|EPS签约QoS模板ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
QCI|服务质量业务类别标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|参数作用：该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier，QCI）。QCI用于指示各EPS承载在确定分配和保留时的重要性。每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
ARP|分配保留优先级|参数可选性:必选参数；参数类型:复合参数|参数作用：该参数用于配置分配保留优先级，是一个复合参数，由PRILEVEL、PREEMPCAP、PREEMPVUL三个参数组合而成，是对这三个参数的组合说明。修改影响：无。数据来源：全网规划。默认值：0。配置原则：无。
PRILEVEL|优先级|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|参数作用：该参数用于设置分配保留优先级参数中的优先级。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
PREEMPCAP|抢占能力标识|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置分配保留优先级参数中的抢占能力标识，用于标识在系统拥塞时是否可以抢占其他低优先级承载的无线资源。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
PREEMPVUL|被抢占能力标识|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置分配保留优先级参数中的被抢占能力标识。用于标识在系统拥塞时是否可以被其他高优先级承载抢占无线资源。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
命令举例 
新增EPS签约QoS模板配置，EPS签约QoS模板ID为1，服务质量业务类别标识为255，优先级为2，抢占能力标识为启用，被抢占能力标识为禁用。 
ADD EPSSUBQOSPROCFG:PROID=1,QCI=255,ARP="2"-"ENABLE"-"DISABLE" 
父主题： [EPS签约QoS模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改EPS签约QoS模板配置(SET EPSSUBQOSPROCFG) 
#### 修改EPS签约QoS模板配置(SET EPSSUBQOSPROCFG) 
命令功能 
该命令用于修改指定EPS签约QoS模板中的签约信息。
注意事项 
配置完成，且传送变化表或者全部表后生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|EPS签约QoS模板ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
QCI|服务质量业务类别标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|参数作用：该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier，QCI）。QCI用于指示各EPS承载在确定分配和保留时的重要性。每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
ARP|分配保留优先级|参数可选性:任选参数；参数类型:复合参数|参数作用：该参数用于配置分配保留优先级，是一个复合参数，由PRILEVEL、PREEMPCAP、PREEMPVUL三个参数组合而成，是对这三个参数的组合说明。修改影响：无。数据来源：全网规划。默认值：0。配置原则：无。
PRILEVEL|优先级|参数可选性:必选参数；参数类型:整数；参数范围为:1~15。|参数作用：该参数用于设置分配保留优先级参数中的优先级。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
PREEMPCAP|抢占能力标识|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置分配保留优先级参数中的抢占能力标识，用于标识在系统拥塞时是否可以抢占其他低优先级承载的无线资源。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
PREEMPVUL|被抢占能力标识|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置分配保留优先级参数中的被抢占能力标识。用于标识在系统拥塞时是否可以被其他高优先级承载抢占无线资源。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
命令举例 
修改EPS签约QoS模板配置，EPS签约QoS模板ID为1，服务质量业务类别标识为123，优先级为5，抢占能力标识为启用，被抢占能力标识为禁用。 
SET EPSSUBQOSPROCFG:PROID=1,QCI=123,ARP="5"-"ENABLE"-"DISABLE" 
父主题： [EPS签约QoS模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除EPS签约QoS模板配置(DEL EPSSUBQOSPROCFG) 
#### 删除EPS签约QoS模板配置(DEL EPSSUBQOSPROCFG) 
命令功能 
该命令用于删除指定EPS签约QoS模板。
注意事项 
配置完成，且传送变化表或者全部表后生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|EPS签约QoS模板ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~2048。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
命令举例 
删除EPS签约QoS模板配置，EPS签约QoS模板ID为1。 
DEL EPSSUBQOSPROCFG:PROID=1 
父主题： [EPS签约QoS模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询EPS签约QoS模板配置(SHOW EPSSUBQOSPROCFG) 
#### 查询EPS签约QoS模板配置(SHOW EPSSUBQOSPROCFG) 
命令功能 
该命令用于查询EPS签约QoS模板配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|EPS签约QoS模板ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~2048。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|EPS签约QoS模板ID|参数可选性:必选参数；参数类型:整数。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
QCI|服务质量业务类别标识|参数可选性:必选参数；参数类型:整数。|参数作用：该参数为用户QoS属性中的QoS业务类别标识（QoS Class Identifier，QCI）。QCI用于指示各EPS承载在确定分配和保留时的重要性。每个QCI值的具体说明，参见3GPP TS 23.203协议，6.1.7.2节描述。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
PRILEVEL|优先级|参数可选性:必选参数；参数类型:整数。|参数作用：该参数用于设置分配保留优先级参数中的优先级。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
PREEMPCAP|抢占能力标识|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置分配保留优先级参数中的抢占能力标识，用于标识在系统拥塞时是否可以抢占其他低优先级承载的无线资源。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
PREEMPVUL|被抢占能力标识|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置分配保留优先级参数中的被抢占能力标识。用于标识在系统拥塞时是否可以被其他高优先级承载抢占无线资源。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
命令举例 
查询EPS签约QoS模板配置，EPS签约QoS模板ID为1。 
SHOW EPSSUBQOSPROCFG:PROID=1 
`
(No.156) : SHOW EPSSUBQOSPROCFG:PROID=1
-----------------uMAC_Combo_14/NFS_MMESGSN_0----------------
操作维护       EPS签约QoS模板ID    服务质量业务类别标识    优先级    抢占能力标识    被抢占能力标识
--------------------------------------------------------------------------------------------------------------
复制 修改 删除 1          255                  5              启用                启用                  
--------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-05-09 11:06:07 耗时: 3.544秒
` 
父主题： [EPS签约QoS模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### APN签约模板配置 
### APN签约模板配置 
背景知识 
为了保证用户所属HSS故障时用户基本的通信业务需求，可以通过本地配置用户签约数据。当检测到用户所属HSS故障时，直接使用本地配置的签约数据，继续用户业务流程。 
功能描述 
本功能用于配置签约APN模板配置。 
当APN需要关联配置EPS签约QoS时，则需要通过"新增EPS签约QoS模板配置"，配置对应的EPS签约QoS模板。 
相关主题 
 
新增APN签约模板配置(ADD APNSUBPROCFG)
 
 
修改APN签约模板配置(SET APNSUBPROCFG)
 
 
删除APN签约模板配置(DEL APNSUBPROCFG)
 
 
查询APN签约模板配置(SHOW APNSUBPROCFG)
 
 
父主题： [HSS故障旁路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增APN签约模板配置(ADD APNSUBPROCFG) 
#### 新增APN签约模板配置(ADD APNSUBPROCFG) 
命令功能 
该命令用于新增APN签约模板，或者在已有的签约APN模板中新增签约APN。
注意事项 
 
配置完成，且传送变化表或者全部表后生效。
 
 
最多支持配置4096个记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|APN签约模板ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
APN|APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|参数作用：该参数用于配置签约的APN名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：大小写不敏感，若配置的APN名称中包含大写字母，则传送到前台时自动转为小写。
CNTXID|上下文标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|参数作用：该参数用于配置APN对应的上下文标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：同一个模板中，上下文标识唯一。
PDNTYPE|PDN类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置APN对应的PDN类型，包括IPv4和IPv6。修改影响：无。数据来源：全网规划。默认值：0-IPv4。配置原则：无。
DFTAPNFG|是否默认APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|参数作用：该参数用于控制APN是否为用户默认签约APN。修改影响：当该参数设置为是，则该APN为用户默认签约APN。当用户激活PDN时，若未携带请求的APN，则使用该默认APN。数据来源：全网规划。默认值：0-否。配置原则：无。
EPSSUBQOSPROID|EPS签约QoS模板ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~2048。默认值:0。|参数作用：该参数用于配置用户EPS签约QoS模板标识。修改影响：当该参数设置为0，则表示未配置EPS签约QoS。数据来源：本端规划。默认值：0。配置原则：无。
VPLMNDYNADDR|是否允许拜访网络动态地址|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|参数作用：该参数用于控制该APN是否允许使用拜访地网络中的网关。修改影响：当该参数设置为否时，则用户漫游地接入新建PDN会话时，不允许该PDN会话使用漫游地网络的网关。数据来源：全网规划。默认值：0-否。配置原则：无。
CHARGCH|3GPP计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置本APN对应的计费特性。修改影响：当该参数设置为0，表示该APN未签约计费特性。若该参数设置为非0，则表示配置了一个或者多个计费特性，各计费特性说明如下：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。自定义计费：按照运营商自定义的计费策略进行计费。数据来源：全网规划。默认值：0-无计费特性。配置原则：无。
APNAMBR|APN AMBR|参数可选性:任选参数；参数类型:复合参数|参数作用：该参数用于配置该APN对应的APN AMBR。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
ULAMBR|上行APN AMBR|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。默认值:4294967295。|参数作用：该参数用于配置该APN对应的上行AMBR。本参数和"上行APN AMBR单位"结合，得到最终该APN对应的上行AMBR。修改影响：若参数设置为4294967295，则表示该APN未配置签约的上行APN AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
ULAPNAMBRUNIT|上行APN AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:bps。|参数作用：该参数用于配置上行APN AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps。配置原则：无。
DLAMBR|下行APN AMBR|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。默认值:4294967295。|参数作用：该参数用于配置该APN对应的下行AMBR。本参数和"下行APN AMBR单位"结合，得到最终该APN对应的下行AMBR。修改影响：若参数设置为4294967295，则表示该APN未配置签约的下行APN AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
DLAPNAMBRUNIT|下行APN AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:bps。|参数作用：该参数用于配置下行APN AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps。配置原则：无。
APNOI|APN OI替换|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。默认值:。|参数作用：该参数用于配置该APN对应的APN OI替换。APN OI替换包含用户级和APN级，用于在选择PGW时构造FQDN。修改影响：无。数据来源：全网规划。默认值：无。配置原则：大小写不敏感，若配置的APN OI替换中包含大写字母，则传送到前台时自动转为小写。
EPSIWK|是否允许5G系统互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|参数作用：该参数用于控制该APN是否允许4/5G互操作。修改影响：当参数设置为是，则使用该APN创建的PDN会话可以在4/5G间切换。数据来源：全网规划。默认值：0-否。配置原则：无。
命令举例 
新增APN签约模板配置，APN签约模板ID为1，APN为APN1，PDN类型为IPv4和IPv6。 
ADD APNSUBPROCFG:PROID=1,APN="APN1",CNTXID=2,PDNTYPE="IPv4AndIPv6" 
父主题： [APN签约模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改APN签约模板配置(SET APNSUBPROCFG) 
#### 修改APN签约模板配置(SET APNSUBPROCFG) 
命令功能 
该命令用于修改指定APN签约模板中指定APN的签约信息。
注意事项 
配置完成，且传送变化表或者全部表后生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|APN签约模板ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
APN|APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|参数作用：该参数用于配置签约的APN名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：大小写不敏感，若配置的APN名称中包含大写字母，则传送到前台时自动转为小写。
CNTXID|上下文标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|参数作用：该参数用于配置APN对应的上下文标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：同一个模板中，上下文标识唯一。
PDNTYPE|PDN类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置APN对应的PDN类型，包括IPv4和IPv6。修改影响：无。数据来源：全网规划。默认值：0-IPv4。配置原则：无。
DFTAPNFG|是否默认APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于控制APN是否为用户默认签约APN。修改影响：当该参数设置为是，则该APN为用户默认签约APN。当用户激活PDN时，若未携带请求的APN，则使用该默认APN。数据来源：全网规划。默认值：0-否。配置原则：无。
EPSSUBQOSPROID|EPS签约QoS模板ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~2048。|参数作用：该参数用于配置用户EPS签约QoS模板标识。修改影响：当该参数设置为0，则表示未配置EPS签约QoS。数据来源：本端规划。默认值：0。配置原则：无。
VPLMNDYNADDR|是否允许拜访网络动态地址|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于控制该APN是否允许使用拜访地网络中的网关。修改影响：当该参数设置为否时，则用户漫游地接入新建PDN会话时，不允许该PDN会话使用漫游地网络的网关。数据来源：全网规划。默认值：0-否。配置原则：无。
CHARGCH|3GPP计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置本APN对应的计费特性。修改影响：当该参数设置为0，表示该APN未签约计费特性。若该参数设置为非0，则表示配置了一个或者多个计费特性，各计费特性说明如下：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。自定义计费：按照运营商自定义的计费策略进行计费。数据来源：全网规划。默认值：0-无计费特性。配置原则：无。
APNAMBR|APN AMBR|参数可选性:任选参数；参数类型:复合参数|参数作用：该参数用于配置该APN对应的APN AMBR。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
ULAMBR|上行APN AMBR|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于配置该APN对应的上行AMBR。本参数和"上行APN AMBR单位"结合，得到最终该APN对应的上行AMBR。修改影响：若参数设置为4294967295，则表示该APN未配置签约的上行APN AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
ULAPNAMBRUNIT|上行APN AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置上行APN AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps。配置原则：无。
DLAMBR|下行APN AMBR|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于配置该APN对应的下行AMBR。本参数和"下行APN AMBR单位"结合，得到最终该APN对应的下行AMBR。修改影响：若参数设置为4294967295，则表示该APN未配置签约的下行APN AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
DLAPNAMBRUNIT|下行APN AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置下行APN AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps。配置原则：无。
APNOI|APN OI替换|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。|参数作用：该参数用于配置该APN对应的APN OI替换。APN OI替换包含用户级和APN级，用于在选择PGW时构造FQDN。修改影响：无。数据来源：全网规划。默认值：无。配置原则：大小写不敏感，若配置的APN OI替换中包含大写字母，则传送到前台时自动转为小写。
EPSIWK|是否允许5G系统互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于控制该APN是否允许4/5G互操作。修改影响：当参数设置为是，则使用该APN创建的PDN会话可以在4/5G间切换。数据来源：全网规划。默认值：0-否。配置原则：无。
命令举例 
修改APN签约模板配置，将APN签约模板ID为1，APN为APN1的PDN类型修改为IPv4。 
SET APNSUBPROCFG:PROID=1,APN="APN1",PDNTYPE="IPv4" 
父主题： [APN签约模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除APN签约模板配置(DEL APNSUBPROCFG) 
#### 删除APN签约模板配置(DEL APNSUBPROCFG) 
命令功能 
该命令用于删除指定APN签约模板中的指定APN。
注意事项 
配置完成，且传送变化表或者全部表后生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|APN签约模板ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
APN|APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|参数作用：该参数用于配置签约的APN名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：大小写不敏感，若配置的APN名称中包含大写字母，则传送到前台时自动转为小写。
命令举例 
删除APN签约模板配置，将APN签约模板ID为1，APN为APN1的数据删除。 
DEL APNSUBPROCFG:PROID=1,APN="APN1" 
父主题： [APN签约模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询APN签约模板配置(SHOW APNSUBPROCFG) 
#### 查询APN签约模板配置(SHOW APNSUBPROCFG) 
命令功能 
该命令用于查询APN签约模板配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|APN签约模板ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~1024。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
APN|APN|参数可选性:任选参数；参数类型:字符型；参数范围为:1~100个字符。|参数作用：该参数用于配置签约的APN名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：大小写不敏感，若配置的APN名称中包含大写字母，则传送到前台时自动转为小写。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PROID|APN签约模板ID|参数可选性:必选参数；参数类型:整数。|参数作用：该参数用于配置EPS签约QoS模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
APN|APN|参数可选性:必选参数；参数类型:字符型。|参数作用：该参数用于配置签约的APN名称。修改影响：无。数据来源：全网规划。默认值：无。配置原则：大小写不敏感，若配置的APN名称中包含大写字母，则传送到前台时自动转为小写。
CNTXID|上下文标识|参数可选性:必选参数；参数类型:整数。|参数作用：该参数用于配置APN对应的上下文标识。修改影响：无。数据来源：本端规划。默认值：无。配置原则：同一个模板中，上下文标识唯一。
PDNTYPE|PDN类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置APN对应的PDN类型，包括IPv4和IPv6。修改影响：无。数据来源：全网规划。默认值：0-IPv4。配置原则：无。
DFTAPNFG|是否默认APN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于控制APN是否为用户默认签约APN。修改影响：当该参数设置为是，则该APN为用户默认签约APN。当用户激活PDN时，若未携带请求的APN，则使用该默认APN。数据来源：全网规划。默认值：0-否。配置原则：无。
EPSSUBQOSPROID|EPS签约QoS模板ID|参数可选性:任选参数；参数类型:整数。|参数作用：该参数用于配置用户EPS签约QoS模板标识。修改影响：当该参数设置为0，则表示未配置EPS签约QoS。数据来源：本端规划。默认值：0。配置原则：无。
VPLMNDYNADDR|是否允许拜访网络动态地址|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于控制该APN是否允许使用拜访地网络中的网关。修改影响：当该参数设置为否时，则用户漫游地接入新建PDN会话时，不允许该PDN会话使用漫游地网络的网关。数据来源：全网规划。默认值：0-否。配置原则：无。
CHARGCH|3GPP计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置本APN对应的计费特性。修改影响：当该参数设置为0，表示该APN未签约计费特性。若该参数设置为非0，则表示配置了一个或者多个计费特性，各计费特性说明如下：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。自定义计费：按照运营商自定义的计费策略进行计费。数据来源：全网规划。默认值：0-无计费特性。配置原则：无。
ULAMBR|上行APN AMBR|参数可选性:必选参数；参数类型:整数。|参数作用：该参数用于配置该APN对应的上行AMBR。本参数和"上行APN AMBR单位"结合，得到最终该APN对应的上行AMBR。修改影响：若参数设置为4294967295，则表示该APN未配置签约的上行APN AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
ULAPNAMBRUNIT|上行APN AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置上行APN AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps。配置原则：无。
DLAMBR|下行APN AMBR|参数可选性:必选参数；参数类型:整数。|参数作用：该参数用于配置该APN对应的下行AMBR。本参数和"下行APN AMBR单位"结合，得到最终该APN对应的下行AMBR。修改影响：若参数设置为4294967295，则表示该APN未配置签约的下行APN AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
DLAPNAMBRUNIT|下行APN AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置下行APN AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps。配置原则：无。
APNOI|APN OI替换|参数可选性:任选参数；参数类型:字符型。|参数作用：该参数用于配置该APN对应的APN OI替换。APN OI替换包含用户级和APN级，用于在选择PGW时构造FQDN。修改影响：无。数据来源：全网规划。默认值：无。配置原则：大小写不敏感，若配置的APN OI替换中包含大写字母，则传送到前台时自动转为小写。
EPSIWK|是否允许5G系统互操作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于控制该APN是否允许4/5G互操作。修改影响：当参数设置为是，则使用该APN创建的PDN会话可以在4/5G间切换。数据来源：全网规划。默认值：0-否。配置原则：无。
命令举例 
查询APN签约模板配置APN签约模板ID为1的数据。 
SHOW APNSUBPROCFG:PROID=1 
`
(No.144) : SHOW APNSUBPROCFG:PROID=1
-----------------uMAC_Combo_14/NFS_MMESGSN_0----------------
操作维护       APN签约模板ID    APN    上下文标识    PDN类型    是否默认APN    EPS签约QoS模板ID    是否允许拜访网络动态地址    3GPP计费特性    APN AMBR    上行APN AMBR    上行APN AMBR单位    下行APN AMBR    下行APN AMBR单位    APN OI替换    是否允许5G系统互操作
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1          apn1 1                  IPv4和IPv6 否                  0                             否                                    Null                          4294967295       bps                  4294967295         bps                    qwe1               否                               
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-05-09 10:18:32 耗时: 4.474秒
` 
父主题： [APN签约模板配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### HSS故障本地签约数据配置 
### HSS故障本地签约数据配置 
背景知识 
为了保证用户所属HSS故障时用户基本的通信业务需求，可以通过本地配置用户签约数据。当检测到用户所属HSS故障时，直接使用本地配置的签约数据，继续用户业务流程。 
功能描述 
本功能用于按号段进行本地签约基本数据配置。 
当需要关联配置签约APN时，则需要通过"新增APN签约模板配置"，配置对应的APN签约模板。 
相关主题 
 
新增HSS故障本地签约数据配置(ADD HSSFAULTLOCALSUBCFG)
 
 
修改HSS故障本地签约数据配置(SET HSSFAULTLOCALSUBCFG)
 
 
删除HSS故障本地签约数据配置(DEL HSSFAULTLOCALSUBCFG)
 
 
查询HSS故障本地签约数据配置(SHOW HSSFAULTLOCALSUBCFG)
 
 
父主题： [HSS故障旁路配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增HSS故障本地签约数据配置(ADD HSSFAULTLOCALSUBCFG) 
#### 新增HSS故障本地签约数据配置(ADD HSSFAULTLOCALSUBCFG) 
命令功能 
该命令用于新增指定IMSI号段对应的本地签约数据。
注意事项 
 
配置完成，且传送变化表或者全部表后生效。
 
 
最多支持配置2048个记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|参数作用：该参数用于配置用户的IMSI号段，该号段下用户本地签约配置遵循本配置记录。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
UEAMBR|UE AMBR|参数可选性:任选参数；参数类型:复合参数|参数作用：该参数用于配置用户签约的UE AMBR。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
ULUEAMBR|上行UE AMBR|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。默认值:4294967295。|参数作用：该参数用于配置上行UE AMBR。本参数和"上行UE AMBR单位"结合，得到最终的上行UE AMBR。修改影响：当参数设置为4294967295，表示用户未配置签约上行UE AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
ULUEAMBRUNIT|上行UE AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:bps。|参数作用：该参数用于配置上行UE AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps(bps)。配置原则：无。
DLUEAMBR|下行UE AMBR|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。默认值:4294967295。|参数作用：该参数用于配置下行UE AMBR。本参数和"下行UE AMBR单位"结合，得到最终的下行UE AMBR。修改影响：当参数设置为4294967295，表示用户未配置签约下行UE AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
DLUEAMBRUNIT|下行UE AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:bps。|参数作用：该参数用于配置下行UE AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps(bps)。配置原则：无。
RFSPINDEX|RFSP索引|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。默认值:0。|参数作用：该参数用于配置用户签约的频率选择优先级标识。修改影响：若设置为0，表示未签约频率选择优先级标识。数据来源：全网规划。默认值：0。配置原则：无。
UEUSGTYPE|UE使用类型|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:0。|参数作用：该参数用于配置用户签约的UE使用类型。修改影响：若参数设置为0，则表示未签约UE使用类型。数据来源：全网规划。默认值：0。配置原则：无。
ODBPACKETSR|运营商闭锁分组业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NoBarring。|参数作用：该参数用于配置用户签约运营商闭锁分组业务。修改影响：无。数据来源：全网规划。默认值：0-无运营商闭锁(No ODB)。配置原则：无。
NAC|网络接入模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:PacketAndCircuit。|参数作用：该参数用于配置用户网络接入模式。修改影响：若该参数设置为1，即支持用户接入分组网络，则用户无法触发CS回落。数据来源：全网规划。默认值：0-分组和电路(Packet and Circuit)。配置原则：无。
CHARGCH|3GPP计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用户配置用户级签约计费特性。修改影响：当该参数设置为0，则表示未配置用户级签约计费特性。若该参数设置为非0，则表示配置了一个或者多个计费特性，各计费特性说明如下：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。自定义计费：按照运营商自定义的计费策略进行计费。数据来源：全网规划。默认值：0-无计费特性(Null)。配置原则：无。
RELAYNDIND|中继节点指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NotRelayNode。|参数作用：该参数用于配置用户是否是中继节点。修改影响：无。数据来源：全网规划。默认值：0-非中继节点(Not Relay Node)。配置原则：无。
SUBAPNPROID|APN签约模板ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~1024。默认值:0。|参数作用：该参数用于配置用户签约的APN模板标识。修改影响：若该参数配置为0，则表示用户未配置签约APN。数据来源：本端规划。默认值：0。配置原则：无。
命令举例 
新增HSS故障本地签约数据配置，IMSI号段为999，上行UE AMBR为4294967295，上行UE AMBR单位为bps，下行UE AMBR为4294967295，下行UE AMBR单位为bps。 
ADD HSSFAULTLOCALSUBCFG:IMSISEG="999",UEAMBR="4294967295"-"bps"-"4294967295"-"bps" 
父主题： [HSS故障本地签约数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 修改HSS故障本地签约数据配置(SET HSSFAULTLOCALSUBCFG) 
#### 修改HSS故障本地签约数据配置(SET HSSFAULTLOCALSUBCFG) 
命令功能 
该命令用于修改HSS故障本地签约数据配置。
注意事项 
配置完成，且传送变化表或者全部表后生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|参数作用：该参数用于配置用户的IMSI号段，该号段下用户本地签约配置遵循本配置记录。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
UEAMBR|UE AMBR|参数可选性:任选参数；参数类型:复合参数|参数作用：该参数用于配置用户签约的UE AMBR。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
ULUEAMBR|上行UE AMBR|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于配置上行UE AMBR。本参数和"上行UE AMBR单位"结合，得到最终的上行UE AMBR。修改影响：当参数设置为4294967295，表示用户未配置签约上行UE AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
ULUEAMBRUNIT|上行UE AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置上行UE AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps(bps)。配置原则：无。
DLUEAMBR|下行UE AMBR|参数可选性:必选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于配置下行UE AMBR。本参数和"下行UE AMBR单位"结合，得到最终的下行UE AMBR。修改影响：当参数设置为4294967295，表示用户未配置签约下行UE AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
DLUEAMBRUNIT|下行UE AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置下行UE AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps(bps)。配置原则：无。
RFSPINDEX|RFSP索引|参数可选性:任选参数；参数类型:整数；参数范围为:0~256。|参数作用：该参数用于配置用户签约的频率选择优先级标识。修改影响：若设置为0，表示未签约频率选择优先级标识。数据来源：全网规划。默认值：0。配置原则：无。
UEUSGTYPE|UE使用类型|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|参数作用：该参数用于配置用户签约的UE使用类型。修改影响：若参数设置为0，则表示未签约UE使用类型。数据来源：全网规划。默认值：0。配置原则：无。
ODBPACKETSR|运营商闭锁分组业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置用户签约运营商闭锁分组业务。修改影响：无。数据来源：全网规划。默认值：0-无运营商闭锁(No ODB)。配置原则：无。
NAC|网络接入模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置用户网络接入模式。修改影响：若该参数设置为1，即支持用户接入分组网络，则用户无法触发CS回落。数据来源：全网规划。默认值：0-分组和电路(Packet and Circuit)。配置原则：无。
CHARGCH|3GPP计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用户配置用户级签约计费特性。修改影响：当该参数设置为0，则表示未配置用户级签约计费特性。若该参数设置为非0，则表示配置了一个或者多个计费特性，各计费特性说明如下：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。自定义计费：按照运营商自定义的计费策略进行计费。数据来源：全网规划。默认值：0-无计费特性(Null)。配置原则：无。
RELAYNDIND|中继节点指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置用户是否是中继节点。修改影响：无。数据来源：全网规划。默认值：0-非中继节点(Not Relay Node)。配置原则：无。
SUBAPNPROID|APN签约模板ID|参数可选性:任选参数；参数类型:整数；参数范围为:0~1024。|参数作用：该参数用于配置用户签约的APN模板标识。修改影响：若该参数配置为0，则表示用户未配置签约APN。数据来源：本端规划。默认值：0。配置原则：无。
命令举例 
修改HSS故障本地签约数据配置，IMSI号段为999，上行UE AMBR为128，上行UE AMBR单位为kbps，下行UE AMBR为256，下行UE AMBR单位为kbps。 
SET HSSFAULTLOCALSUBCFG:IMSISEG="999",UEAMBR="128"-"Kbps"-"256"-"Kbps" 
父主题： [HSS故障本地签约数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除HSS故障本地签约数据配置(DEL HSSFAULTLOCALSUBCFG) 
#### 删除HSS故障本地签约数据配置(DEL HSSFAULTLOCALSUBCFG) 
命令功能 
该命令用于删除HSS故障本地签约数据配置。
注意事项 
配置完成，且传送变化表或者全部表后生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|参数作用：该参数用于配置用户的IMSI号段，该号段下用户本地签约配置遵循本配置记录。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
命令举例 
删除HSS故障本地签约数据配置，IMSI号段为999。 
DEL HSSFAULTLOCALSUBCFG:IMSISEG="999" 
父主题： [HSS故障本地签约数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除HSS故障本地签约数据配置(SHOW HSSFAULTLOCALSUBCFG) 
#### 删除HSS故障本地签约数据配置(SHOW HSSFAULTLOCALSUBCFG) 
命令功能 
该命令用于查询HSS故障本地签约数据配置。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|参数作用：该参数用于配置用户的IMSI号段，该号段下用户本地签约配置遵循本配置记录。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSISEG|IMSI号段|参数可选性:必选参数；参数类型:字符型。|参数作用：该参数用于配置用户的IMSI号段，该号段下用户本地签约配置遵循本配置记录。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
ULUEAMBR|上行UE AMBR|参数可选性:必选参数；参数类型:整数。|参数作用：该参数用于配置上行UE AMBR。本参数和"上行UE AMBR单位"结合，得到最终的上行UE AMBR。修改影响：当参数设置为4294967295，表示用户未配置签约上行UE AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
ULUEAMBRUNIT|上行UE AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置上行UE AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps(bps)。配置原则：无。
DLUEAMBR|下行UE AMBR|参数可选性:必选参数；参数类型:整数。|参数作用：该参数用于配置下行UE AMBR。本参数和"下行UE AMBR单位"结合，得到最终的下行UE AMBR。修改影响：当参数设置为4294967295，表示用户未配置签约下行UE AMBR。数据来源：全网规划。默认值：4294967295 。配置原则：无。
DLUEAMBRUNIT|下行UE AMBR单位|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置下行UE AMBR的单位。修改影响：无。数据来源：全网规划。默认值：0-bps(bps)。配置原则：无。
RFSPINDEX|RFSP索引|参数可选性:任选参数；参数类型:整数。|参数作用：该参数用于配置用户签约的频率选择优先级标识。修改影响：若设置为0，表示未签约频率选择优先级标识。数据来源：全网规划。默认值：0。配置原则：无。
UEUSGTYPE|UE使用类型|参数可选性:任选参数；参数类型:整数。|参数作用：该参数用于配置用户签约的UE使用类型。修改影响：若参数设置为0，则表示未签约UE使用类型。数据来源：全网规划。默认值：0。配置原则：无。
ODBPACKETSR|运营商闭锁分组业务|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置用户签约运营商闭锁分组业务。修改影响：无。数据来源：全网规划。默认值：0-无运营商闭锁(No ODB)。配置原则：无。
NAC|网络接入模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置用户网络接入模式。修改影响：若该参数设置为1，即支持用户接入分组网络，则用户无法触发CS回落。数据来源：全网规划。默认值：0-分组和电路(Packet and Circuit)。配置原则：无。
CHARGCH|3GPP计费特性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用户配置用户级签约计费特性。修改影响：当该参数设置为0，则表示未配置用户级签约计费特性。若该参数设置为非0，则表示配置了一个或者多个计费特性，各计费特性说明如下：热计费：具有普通计费的所有功能，只是话单产生速度比普通话单更快。平率计费：即统一费率计费，用户按照指定周期（例如按月）支付费用，且每个周期（例如每月）费用固定。预付费计费：用户在获取某种服务之前需要预先支付一定的费用，如果费用不足以支付某项服务的花销，该项服务将会被强制中止。普通计费：基于用户使用业务的数据流量或时间长度来进行计费，不区分数据的业务种类。自定义计费：按照运营商自定义的计费策略进行计费。数据来源：全网规划。默认值：0-无计费特性(Null)。配置原则：无。
RELAYNDIND|中继节点指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置用户是否是中继节点。修改影响：无。数据来源：全网规划。默认值：0-非中继节点(Not Relay Node)。配置原则：无。
SUBAPNPROID|APN签约模板ID|参数可选性:任选参数；参数类型:整数。|参数作用：该参数用于配置用户签约的APN模板标识。修改影响：若该参数配置为0，则表示用户未配置签约APN。数据来源：本端规划。默认值：0。配置原则：无。
命令举例 
查询HSS故障本地签约数据配置，IMSI号段为999。 
SHOW HSSFAULTLOCALSUBCFG:IMSISEG="999" 
`
(No.152) : SHOW HSSFAULTLOCALSUBCFG:IMSISEG="999"
-----------------uMAC_Combo_14/NFS_MMESGSN_0----------------
操作维护       IMSI号段    上行UE AMBR    上行UE AMBR单位    下行UE AMBR    下行UE AMBR单位    RFSP索引    UE使用类型    运营商闭锁分组业务    网络接入模式    3GPP计费特性    中继节点指示    APN签约模板ID
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 999          4294967295      bps                 4294967295        bps                   0          0             无运营商闭锁          分组和电路  Null                          非中继节点       0                           
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-05-09 11:04:59 耗时: 3.837秒
` 
父主题： [HSS故障本地签约数据配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## MME分级备份策略配置 
## MME分级备份策略配置 
背景知识 
备份功能是指将本MME的用户数据同步到备份MME，一旦本MME发生故障，备份MME可以使用已经同步的用户数据快速接管用户，恢复用户业务。 
功能描述 
分级备份功能是指MME可以配置一些策略，对用户进行区别，将部分用户的数据，同步到备份MME，而其它用户的数据不会被同步，在本MME发生故障时，这些用户可以更快的恢复业务。 
分级备份策略是指MME支持通过SUPI号、GPSI号段、DNN和切片信息等策略来指定将数据同步到备份MME的用户。 
分级备份策略是指MME支持通过APN号、MSISDN号段、IMSI号段指定将数据同步到备份MME的用户。 
各个策略区别出的用户之间可能有重叠，用户生效的优先级顺序如下，即最先生效的为根据APN指定的用户，最后生效的为根据IMSI/MSISDN号段指定的用户。 
APN 
IMSI/MSISDN 
相关主题 
 
MME分级备份全局策略配置
 
 
MSISDN号段分级备份配置
 
 
IMSI号段分级备份配置
 
 
APN分级备份配置
 
 
父主题： [高级配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MME分级备份全局策略配置 
### MME分级备份全局策略配置 
背景知识 
分级备份功能是指MME可以配置一些策略，对用户进行区别，将筛选出来的部分用户的数据，同步到备份MME，而其它用户的数据不会被同步，在本MME发生故障时，这些用户可以更快的恢复业务。 
分级备份策略是指MME支持通过MSISDN号、IMSI号段、APN等策略来指定将数据同步到备份MME的用户。 
功能描述 
用于设置MME是否开启分级备份功能，以及变化速率等全局配置。 
相关主题 
 
设置分级备份全局策略配置(SET MMEPOLYDRCFG)
 
 
查询分级备份全局策略配置(SHOW MMEPOLYDRCFG)
 
 
父主题： [MME分级备份策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置分级备份全局策略配置(SET MMEPOLYDRCFG) 
#### 设置分级备份全局策略配置(SET MMEPOLYDRCFG) 
命令功能 
设置是否开启各种分级备份功能，以及变化速率等全局配置。 
注意事项 
 
通过此命令，开启MME分级备份功能后，MME将会根据配置对用户进行分级备份，后续MME会通过扫描的方式修改用户分级备份策略，这个过程所需要的时间是通过本命令配置的参数“分级配置变化生效时间”。生效时间需要在中兴通讯技术支持的指导下修改，避免生效时间设置过短，导致扫描太快，影响系统性能。
 
 
此命令可以配置1条记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
FUNC|分级备份功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置MME是否开启分级备份功能以及开启MME分级部分功能后，采用的备份策略。备份策略可以是MME仅备份IMS用户或者MME根据不同的条件来区别备份哪些用户。
TIME|分级配置变化生效时间（s）|参数可选性:任选参数；参数类型:整数；参数范围为:120~3600。|参数作用：该参数用于配置开启MME分级备份功能后，MME通过扫描的方式修改用户分级备份策略所需要的时间。MME是按SC的粒度来计算扫描速度的，各个SC（Service Component，服务组件）各自计算相应的扫描速度。生效时间需要在中兴通讯技术支持的指导下修改，避免生效时间设置过短，导致扫描太快，影响系统性能。
命令举例 
设置分级备份全局策略配置，分级备份功能为关闭，分级配置变化生效时间为600s。 
SET MMEPOLYDRCFG:FUNC="Close",TIME="600" 
父主题： [MME分级备份全局策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询分级备份全局策略配置(SHOW MMEPOLYDRCFG) 
#### 查询分级备份全局策略配置(SHOW  MMEPOLYDRCFG) 
命令功能 
查询已配置的全局分级备份策略。 
注意事项 
此命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
FUNC|分级备份功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于配置MME是否开启分级备份功能以及开启MME分级部分功能后，采用的备份策略。备份策略可以是MME仅备份IMS用户或者MME根据不同的条件来区别备份哪些用户。
TIME|分级配置变化生效时间（s）|参数可选性:任选参数；参数类型:整数；参数范围为:|参数作用：该参数用于配置开启MME分级备份功能后，MME通过扫描的方式修改用户分级备份策略所需要的时间。MME是按SC的粒度来计算扫描速度的，各个SC（Service Component，服务组件）各自计算相应的扫描速度。生效时间需要在中兴通讯技术支持的指导下修改，避免生效时间设置过短，导致扫描太快，影响系统性能。
命令举例 
查询分级备份全局策略配置。 
SHOW MMEPOLYDRCFG; 
`命令 (No.1): SHOW MMEPOLYDRCFG
操作维护       分级备份功能    分级配置变化生效时间（s） 
-----------------------------------------------------
修改           Close          600                               
-----------------------------------------------------
记录数：1
命令执行成功（耗时 0.063 秒）。` 
父主题： [MME分级备份全局策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### MSISDN号段分级备份配置 
### MSISDN号段分级备份配置 
背景知识 
此命令用于配置在MME开启分级备份功能的情况下，MME支持根据MSISDN号段来配置分级备份策略，即配置了某个MSISDN号段，MME就会将此MSISDN号段用户的数据，同步到备份MME。 
功能描述 
可以增加、删除查看MSISDN号段配置。 
相关主题 
 
新增MSISDN号段分级备份配置(ADD CONDISDN)
 
 
删除MSISDN号段分级备份配置(DEL CONDISDN)
 
 
查询MSISDN号段分级备份配置(SHOW CONDISDN)
 
 
父主题： [MME分级备份策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增MSISDN号段分级备份配置(ADD CONDISDN) 
#### 新增MSISDN号段分级备份配置(ADD CONDISDN) 
命令功能 
此命令用于配置在MME开启分级备份功能的情况下，MME支持根据MSISDN号段来配置分级备份策略，即配置了某个MSISDN号段，MME就会将此MSISDN号段用户的数据，同步到备份MME。 
注意事项 
 
此命令生效的前提条件是通过SET MMEPOLYDRCFG命令，将参数“分级备份功能（FUNC）”配置为“MME按条件备份用户（Backup User Conditionally）”。
 
 
此命令配置的号段按最长匹配原则进行匹配，建议配置的号段尽量长度一致，如果不一致会影响查询性能。
 
 
通过SET MMEPOLYDRCFG命令开启MME分级备份功能后，MME将会根据配置进行用户数据的同步，这个过程所需要的时间是通过SET MMEPOLYDRCFG命令配置的参数“分级配置变化生效时间（TIME）”控制的。生效时间需要在中兴通讯技术支持的指导下修改，避免生效时间设置过短，导致扫描太快，影响系统性能。
 
 
此命令最多可以配置4096条记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|参数作用：该参数用于配置指定MSISDN号段分级备份策略的编号。
MSISDN|MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:5~15个字符。|本参数用于配置MSISDN号段。
命令举例 
新增MSISDN号段分级备份配置，ID为1，MSISDN为8613675138501。 
ADD CONDISDN:ID=1,MSISDN="8613675138501"; 
父主题： [MSISDN号段分级备份配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除MSISDN号段分级备份配置(DEL CONDISDN) 
#### 删除MSISDN号段分级备份配置(DEL CONDISDN) 
命令功能 
删除已配置的ISDN号段。 
注意事项 
此命令执行后立即生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|参数作用：该参数用于配置指定MSISDN号段分级备份策略的编号。
命令举例 
删除MSISDN号段分级备份配置，ID为1。 
DEL CONDIMSI:ID=1; 
父主题： [MSISDN号段分级备份配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询MSISDN号段分级备份配置(SHOW CONDISDN) 
#### 查询MSISDN号段分级备份配置(SHOW CONDISDN) 
命令功能 
查询已配置的ISDN号段。 
注意事项 
此命令执行后立即生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|参数作用：该参数用于配置指定MSISDN号段分级备份策略的编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|参数作用：该参数用于配置指定MSISDN号段分级备份策略的编号。
MSISDN|MSISDN|参数可选性:必选参数；参数类型:字符型。|本参数用于配置MSISDN号段。
命令举例 
查询MSISDN号段分级备份配置，ID为1。 
SHOW CONDISDN:ID=1; 
`
命令 (No.12): SHOW CONDISDN:ID=1;
操作维护       ID MSISDN            
--------------------------------
复制 删除      1  8613675138501 
--------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [MSISDN号段分级备份配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### IMSI号段分级备份配置 
### IMSI号段分级备份配置 
背景知识 
此命令用于配置在MME开启分级备份功能的情况下，MME支持根据IMSI号段来配置分级备份策略，即配置了某个IMSI号段，MME就会将此IMSI号段用户的数据，同步到备份MME。 
功能描述 
可以增加、删除查看已经配置的IMSI号段。 
相关主题 
 
新增IMSI号段分级备份配置(ADD CONDIMSI)
 
 
删除IMSI号段分级备份配置(DEL CONDIMSI)
 
 
查询IMSI号段分级备份配置(SHOW CONDIMSI)
 
 
父主题： [MME分级备份策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增IMSI号段分级备份配置(ADD CONDIMSI) 
#### 新增IMSI号段分级备份配置(ADD CONDIMSI) 
命令功能 
此命令用于配置在MME开启分级备份功能的情况下，MME支持根据IMSI号段来配置分级备份策略，即配置了某个IMSI号段，MME就会将此IMSI号段用户的数据，同步到备份MME。 
注意事项 
 
此命令生效的前提条件是通过SET MMEPOLYDRCFG命令，将参数“分级备份功能（FUNC）”配置为“MME按条件备份用户（Backup User Conditionally）”。
 
 
此命令配置的号段按最长匹配原则进行匹配，建议配置的号段尽量长度一致，如果不一致会影响查询性能。
 
 
通过SET MMEPOLYDRCFG命令开启MME分级备份功能后，MME将会根据配置进行用户数据的同步，这个过程所需要的时间是通过SET MMEPOLYDRCFG命令配置的参数“分级配置变化生效时间（TIME）”控制的。生效时间需要在中兴通讯技术支持的指导下修改，避免生效时间设置过短，导致扫描太快，影响系统性能。
 
 
此命令最多可以配置4096条记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|参数作用：该参数用于配置指定IMSI号段分级备份策略的编号。
IMSI|IMSI|参数可选性:必选参数；参数类型:字符型；参数范围为:5~15个字符。|本参数用于配置IMSI号段。
命令举例 
新增IMSI号段分级备份配置，ID为1，IMSI为460020012700100。 
ADD CONDIMSI:ID=1,IMSI="460020012700100"; 
父主题： [IMSI号段分级备份配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除IMSI号段分级备份配置(DEL CONDIMSI) 
#### 删除IMSI号段分级备份配置(DEL CONDIMSI) 
命令功能 
此命令用于删除已配置的IMSI号段。 
注意事项 
此命令执行后立即生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|参数作用：该参数用于配置指定IMSI号段分级备份策略的编号。
命令举例 
删除IMSI号段分级备份配置，ID为1。 
DEL CONDIMSI:ID=1; 
父主题： [IMSI号段分级备份配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询IMSI号段分级备份配置(SHOW CONDIMSI) 
#### 查询IMSI号段分级备份配置(SHOW CONDIMSI) 
命令功能 
此命令用于查询已配置的IMSI号段。 
注意事项 
此命令执行后立即生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|参数作用：该参数用于配置指定IMSI号段分级备份策略的编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|参数作用：该参数用于配置指定IMSI号段分级备份策略的编号。
IMSI|IMSI|参数可选性:任选参数；参数类型:字符型。|本参数用于配置IMSI号段。
命令举例 
查询IMSI号段分级备份配置，ID为1。 
SHOW CONDIMSI:ID=1; 
`
命令 (No.12): SHOW CONDIMSI:ID=1;
操作维护       ID IMSI            
----------------------------------
复制 删除      1  460020012700100 
----------------------------------
记录数 1
命令执行成功（耗时 0.037 秒）。
` 
父主题： [IMSI号段分级备份配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### APN分级备份配置 
### APN分级备份配置 
背景知识 
该功能用于配置指定APN的分级备份策略，配置了某个APN，当用户签约的APN中包含配置的APN时，MME就会将此类用户的数据，同步到备份AMF。 
功能描述 
本功能主要用于增加、删除和查询指定APN配置的分级备份策略。 
相关主题 
 
新增APN分级备份配置(ADD CONDAPN)
 
 
删除APN分级备份配置(DEL CONDAPN)
 
 
查询APN分级备份配置(SHOW CONDAPN)
 
 
父主题： [MME分级备份策略配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 新增APN分级备份配置(ADD CONDAPN) 
#### 新增APN分级备份配置(ADD CONDAPN) 
命令功能 
MME支持配置指定APN的分级备份策略，即配置了某个APN，当用户签约的APN中包含配置的APN时，MME就会将此类用户的数据，同步到备份MME。 
注意事项 
 
此命令执行后立即生效。
 
 
此命令生效的前提条件是通过SET MMEPOLYDRCFG命令，将参数“分级备份功能（FUNC）”配置为“MME按条件备份用户（Backup User Conditionally）”。
 
 
通过SET MMEPOLYDRCFG命令开启MME分级备份功能后，MME将会根据配置进行用户数据的同步，这个过程所需要的时间是通过SET MMEPOLYDRCFG命令配置的参数“分级配置变化生效时间（TIME）”控制的。生效时间需要在中兴通讯技术支持的指导下修改，避免生效时间设置过短，导致扫描太快，影响系统性能。
 
 
此命令配置的APN为NI部分。
 
 
此命令最多可以配置1024条记录。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于配置指定APN分级备份策略的编号。
APN|APN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~99个字符。|本参数用于配置分级备份策略的APN，只需配置NI部分。
命令举例 
新增APN分级备份配置，ID为1，APN为ims。 
ADD CONDAPN:ID=1,APN="ims"; 
父主题： [APN分级备份配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 删除APN分级备份配置(DEL CONDAPN) 
#### 删除APN分级备份配置(DEL CONDAPN) 
命令功能 
删除已配置的APN。 
注意事项 
此命令执行后，结果立即生效。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~1024。|该参数用于配置指定APN分级备份策略的编号。
命令举例 
删除APN分级备份配置，ID为1。 
DEL CONDAPN:ID=1; 
父主题： [APN分级备份配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# 安全变量 
# 安全变量 
背景知识 
系统运行过程中，需要设置安全相关的变量参数，以保障系统运行过程功能中灵活控制，保障系统安全。 
功能描述 
安全变量的配置功能范围包括：鉴权参数、短消息参数、移动性管理参数、系统控制参数、LLC相关参数、分组域参数、GTP参数等配置。 
相关主题 
 
短消息参数配置
 
 
移动管理参数配置
 
 
系统控制参数配置
 
 
分组域参数配置
 
 
LLC相关配置
 
 
安全相关配置
 
 
GTP参数配置
 
 
父主题： [配置管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 短消息参数配置 
## 短消息参数配置 
背景知识 
SGSN在处理短消息业务的过程中，为保障短消息业务成功，需要增加相关的短消息控制参数，来控制短消息是否进行分包，消息重发以及消息参数携带等。 
功能描述 
短消息参数配置主要完成的功能如下： 
 
控制短消息分包长度。
 
 
设置下行短消息重发次数。
 
 
控制GPRS的起呼短信是否携带IMSI
 
 
相关主题 
 
设置短消息参数(SET SMS PARAMETER)
 
 
查询短消息参数(SHOW SMS PARAMETER)
 
 
父主题： [安全变量]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置短消息参数(SET SMS PARAMETER) 
### 设置短消息参数(SET SMS PARAMETER) 
命令功能 
该命令用于设置短消息参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
SMSPACKET|短消息分包长度|参数可选性:任选参数；参数类型:整数；参数范围为:1~200。|该安全变量用于设置短消息分包长度。29002协议规定，向短消息中心发送ForwardSMS Request消息时，根据终端发送短消息包长度和安全变量配置的短消息分包长度进行比较。如果超出设置的短消息分包长度，那么先向短消息中心发送map open request对话，对话建立后，再发送ForwardSMS Request消息给短消息中心。
DLSMSRETRIES|下行短消息重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~3。|该安全变量用于设置下行短消息重发次数。在SGSN处理短消息起呼和短消息终呼时，在SGSN下发CPDATA REQUEST消息给UE时，设置等待CPDATA ACK定时器，等待UE回 CPDATA ACK消息，定时器超时后，根据此安全变量判断是否重新发送CPDATA REQUEST。如果下发CPDATA REQUEST次数小于安全变量的设置的次数，那么重新下发CPDATA REQUEST，重新设置等待定时器。等待UE的响应。如果下发CPDATA REQUEST次数大于安全变量的设置的次数，那么通知短消息中心短消息发送失败。
GPRSSMSMO|GPRS的起呼短信是否携带IMSI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置GPRS的起呼短信是否携带IMSI。短消息起呼过程中，SGSN向短消息中心发送ForwardSMS Request消息时，根据此安全变量判断短消息消息中是否携带IMSI内容：不携带：ForwardSMS Request消息中不携带IMSI内容。携带：ForwardSMS Request消息中携带IMSI内容。
命令举例 
设置短消息参数，短消息分包长度为1，下行短消息重发次数为1。 
SET SMS PARAMETER:SMSPACKET=1,DLSMSRETRIES=1; 
父主题： [短消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询短消息参数(SHOW SMS PARAMETER) 
### 查询短消息参数(SHOW SMS PARAMETER) 
命令功能 
该命令用于查询短消息参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SMSPACKET|短消息分包长度|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置短消息分包长度。29002协议规定，向短消息中心发送ForwardSMS Request消息时，根据终端发送短消息包长度和安全变量配置的短消息分包长度进行比较。如果超出设置的短消息分包长度，那么先向短消息中心发送map open request对话，对话建立后，再发送ForwardSMS Request消息给短消息中心。
DLSMSRETRIES|下行短消息重发次数|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置下行短消息重发次数。在SGSN处理短消息起呼和短消息终呼时，在SGSN下发CPDATA REQUEST消息给UE时，设置等待CPDATA ACK定时器，等待UE回 CPDATA ACK消息，定时器超时后，根据此安全变量判断是否重新发送CPDATA REQUEST。如果下发CPDATA REQUEST次数小于安全变量的设置的次数，那么重新下发CPDATA REQUEST，重新设置等待定时器。等待UE的响应。如果下发CPDATA REQUEST次数大于安全变量的设置的次数，那么通知短消息中心短消息发送失败。
GPRSSMSMO|GPRS的起呼短信是否携带IMSI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置GPRS的起呼短信是否携带IMSI。短消息起呼过程中，SGSN向短消息中心发送ForwardSMS Request消息时，根据此安全变量判断短消息消息中是否携带IMSI内容：不携带：ForwardSMS Request消息中不携带IMSI内容。携带：ForwardSMS Request消息中携带IMSI内容。
命令举例 
查询短消息参数。 
SHOW SMS PARAMETER 
`
2017-01-04 09:15:38 命令 (No.1): SHOW SMS PARAMETER
操作维护  短消息分包长度   下行短消息重发次数   GPRS的起呼短信是否携带IMSI
--------------------------------------------------------------------------
修改      120              2                    不携带
--------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.138 秒）。
` 
父主题： [短消息参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 移动管理参数配置 
## 移动管理参数配置 
背景知识 
在SGSN/MME网元中，移动性管理模块主要负责移动性管理（MM）子层协议的功能，包括用户的连接管理、接入控制、移动性管理、以及NAS层安全等。 
SGSN的移动性管理模块（GMM）主要负责处理协议（3GPP-24008-950 “4.7 Elementary mobility management procedures for GPRS services"）要求的流程，具体包括：Attach流程，Detach流程，RAU流程，Service Request流程。Identification流程，P-TMSI Reallocation流程，鉴权流程，以及GMM information流程。 
MME的移动性管理模块（EMM）主要负责处理协议（3GPP-24008-950 “11.2 Timers of mobility management "/3GPP-24301-950 “5 Elementary procedures for EPS mobility management"）要求的流程，具体包括：Attach流程、Detach流程、TAU流程、Service Request流程、Paging触发流程、LTE UE接入鉴权流程等。 
功能描述 
本命令用来设置SGSN/MME移动性管理相关的参数。包括协议（3GPP-24008-950 “11.2 Timers of mobility management "/3GPP-24301-950 “10.2 Timers of EPS mobility management"）规定的由SGSN/MME下发给UE的相关定时器时长，SGSN/MME自身的相关定时器时长以及是否支持Iu延迟释放，EPLMN组数等其它一些重要的移动性管理参数。 
相关主题 
 
设置移动管理参数(SET MOBILE MANAGEMENT)
 
 
查询移动管理参数(SHOW MOBILE MANAGEMENT)
 
 
父主题： [安全变量]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置移动管理参数(SET MOBILE MANAGEMENT) 
### 设置移动管理参数(SET MOBILE MANAGEMENT) 
命令功能 
本命令用于设置移动管理参数。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
RTUPDATEPERIOD|路由周期性更新定时器(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:60~11160。|该定时器用于设置指示MS发起周期性路由更新的时间间隔。SGSN通过attach accept消息或者routing area update accept消息携带Periodic RA update timer字段，将该时长传递给MS，MS收到后将此时长作为MS周期性路由更新时长。Iu模式时，MS从PMM-CONNECTED变为PMM-IDLE mode时，该定时器重置并被启动，当MS重新进入PMM-CONNECTED时停止。A/Gb模式时，当MS进入Standby状态时，该定时器重置并被启动，当MS进入READY态时，定时器停止。当定时器超时时，MS发起周期性路由更新。
READYTIMER|Ready定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:30~11160。|该定时器用于设置READY定时器的时长。SGSN通过attach accept消息或者routing area update accept消息携带Negotiated READY timer value字段，将该时长传递给MS，MS收到后将此时长作为Ready状态变为Standby状态的时长。在MS侧，当MS发起上行信令或数据包时定时器启动。定时器超时时进入Standby状态，定时器停止（复位）。在SGSN侧，当接收到上行信令或数据包时定时器启动。定时器超时时进入Standby状态，定时器停止（复位）。
STANDBYTIMER|SGSN可达定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:120~24000。|该定时器用于SGSN侧，当进入READY state或PMM-CONNECTED状态时，可达定时器停止。当返回到STANDBY或PMM-IDLE状态时，可达定时器被重置并且启动。当可达定时器超时时，SGSN会将MS置为隐式分离状态。可达定时器应该比MS使用的路由周期性更新定时器(T3312)时长略长点。
SGSNUNREACHABLETIMER|SGSN MM上下文删除定时器时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:120~1440。|该安全变量是系统内部定义的，按照23.060协议的说明，上下文处于分离状态后，可以立即删除，也可以保留一段时间。具体时长取决于实际需要。作为一种实际应用的选择，SGSN可以在MS隐式或者显式分离后立即删除MS的MM上下文和PDP上下文；或者SGSN也可以将已经分离的MS的MM和PDP上下文以及鉴权三重组保留一段时间（根据该变量设置），这样可以在随后的GPRS附着中使用而不需要访问HLR。当MS隐式或者显式分离时，定时器启动，定时器超时时将MS的MM上下文删除，定时器停止（复位）。
FORSWITCHFORIURELEASE|Iu延迟释放|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果手机在附着或者路由更新请求消息中携带FOR=0，那么依靠此安全变量决定附着成功或者路由更新成功后是否立即释放Iu连接。支持：附着成功或者路由更新成功后，SGSN支持Iu连接延迟释放。不支持：附着成功或者路由更新成功后，立即释放Iu连接。
NASRESENDCOUNT|移动性管理NAS消息重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:0~10。|该安全变量用于设置MME重发NAS请求消息的次数，这些消息包括：AUTHENTICATION REQUEST，DETACH REQUEST，GUTI REALLOCATION COMMAND，IDENTITY REQUEST，SECURITY MODE COMMAND。按照24.301协议的说明，MME在发送NAS请求消息给UE的时候，会启动定时器，定时器超时前未收到UE的响应消息，定时器超时会重发该请求消息，该安全变量用于控制重发的次数。
TAUTIMER|周期性跟踪区更新定时器T3412时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~35712000。|该安全变量用于设置周期性跟踪区更新定时器T3412时长。T3412是UE控制发起周期性跟踪区更新的定时器。按照24.301协议的说明，MME在ATTACH ACCEPT或者 TRACKING AREA UPDATE ACCEPT消息中将T3412的时长带给UE，用于控制UE发起周期性跟踪区更新的时间间隔。
REACHTIMER|MME可达定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:300~35712240。|该安全变量用于设置可达定时器时长。该定时器要比周期性跟踪区更新定时器T3412大，进入空闲态时，如果在移动可达定时器时长内，UE都没有发起周期性路由更新，说明UE已经不在该MME控制范围内，即UE不可达。可达定时器在UE进入空闲态时启动，在UE进入连接态时停止；如果该定时器超时而一直没有收到用户的任何消息，将清空PPF标志并启动隐式分离定时器。
IMPDETACHTIMER|MME隐式分离定时器时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~35712240。|该安全变量用于设置隐式分离定时器时长。隐式分离就是MME本地删除UE的移动性管理上下文、会话和承载上下文，不通知UE。可达定时器超时后隐式分离定时器启动，用户进入连接态时停止；如果该定时器超时而一直没有收到用户的任何消息，MME将UE隐式分离。
MMEUNREACHABLETIMER|MME MM上下文删除定时器时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:1~4320。|该安全变量用于设置UE分离或隐式分离之后到删除移动性管理上下文之间的时长。按照23.401协议的说明，上下文处于分离状态后，可以立即删除，也可以保留一段时间。具体时长取决于实际需要。作为一种实际应用的选择，MME可以在UE隐式或者显式分离后立即删除移动性管理上下文、会话和承载上下文。或者MME也可以将已经分离的用户的移动性管理上下文保留一段时间（根据该变量设置），这样可以在随后的EPS附着中使用而不需要访问HSS。
T3402|UE附着/跟踪区更新重发定时器T3402时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:30~11160。|该安全变量用于控制UE附着/跟踪区更新重发定时器T3402的时长。T3402在UE尝试附着或者跟踪区更新失败5次后启动，超时后再次尝试附着或者跟踪区更新。该定时器保证UE在接入失败之后能够继续尝试接入。MME通过 ATTACH ACCEPT、TRACKING AREA UPDATE ACCEPT或者ATTACH REJECT消息将T3402下发给UE。
MMEGETIMEI|MME 获取IMEI(SV)|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME是否需要在附着流程或者跟踪区更新流程中向UE获取IMEI/IMEISV，取值含义如下：不需要：表示MME不需要获取UE的IMEI或者IMEISV。获取IMEI：表示MME需要向UE获取IMEI。获取IMEISV：表示MME需要向UE获取IMEISV。支持ADD功能：表示MME支持ADD(Automatic Device Detection)功能。
LIMITLTEUSERACCESS|MME支持LTE用户接入限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量是ARD（Access Restriction Data）功能开关，主要是通过对UE的HSS基本信息中ARD参数的设置，实现S1口是否允许该UE附着或者跟踪区更新到EUTRAN网络。
LTEUSERACCESSCAUSE|LTE用户接入EUTRAN网络失败原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制UE因为ARD（Access Restriction Data）功能被限制接入EUTRAN网络，MME在S1口下发附着拒绝或者跟踪区更新拒绝消息时携带的原因值。可供选择的原因值有：“PLMN not allowed"，“Tracking Area not allowed"，“Roaming not allowed in this tracking area"，“EPS services not allowed in this PLMN"，“No Suitable Cells In tracking area"，“Severe network failure"，“Protocol error, unspecified"。
MMELIMITZONESWITCH|MME支持区域码限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量与“MME IMSI号段区域编码配置"ADD MME IMSI TAIZC配合使用，用于控制是否支持漫游限制功能，可以对不同的IMSI号段的同一个区域码设置不同的路由区。MME在用户接入时，根据从HSS获取到的用户签约的区域编码、IMSI号码、当前接入的跟踪区查询“MME IMSI号段区域编码配置"ADD MME IMSI TAIZC，确定是否允许用户接入。如果接入MME的用户号段不在MME IMSI号段区域编码配置中，MME根据跟踪区域码配置中的区域判断是否限制接入。
MMEEPLMNLISTNUM|支持EPLMN组数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME下发给UE的Attach Accept/TAU Accept消息中EPLMN组数。值含义如下：若变量值为“不支持"，则Attach Accept/TAU Accept消息中不带有EPLMN参数。若变量值为“支持5组"，则Attach Accept/TAU Accept消息中最多携带5组EPLMN。若变量值为“支持15组"，则Attach Accept/TAU Accept消息中最多携带15组EPLMN。
MMEZONECODELIMIT|由于区域编码限制用户接入拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制当用户IMSI号段不在区域限制的允许列表中的时候，MME拒绝用户的原因值。具体的原因值有：“IMSI unknown in HSS"，“Illegal UE"， “Illegal ME"，“EPS services not allowed"，“EPS services and non-EPS services not allowed"，“PLMN not allowed"，“Track Area not allowed"，“Roaming not allowed in this tracking area"，“EPS services not allowed in this PLMN"，“No suitable cells in tracking area"，“Not authorized for this CSG"
MMEDETACHCAUSE|MME网络侧分离携带的分离原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制网络侧发起的分离流程时，如果分离类型为“re-attach not required"时，MME是否在分离请求消息中携带EMM Cause信元及携带的具体的EMM Cause。EMM Cause具体的值有：“IMSI unknown in HSS"，“Illegal UE"，“Illegal ME"，“EPS services not allowed"，“EPS services and non-EPS services not allowed"，“PLMN not allowed"，“Track Area not allowed"，“Roaming not allowed in this tracking area"，“EPS services not allowed in this PLMN"，“No suitable cells in tracking area"，“Not authorized for this CSG"。
LMTNBUSRACS|MME支持NB用户接入限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于配置NB用户接入，MME是否要根据用户签约数据，进行ARD限制。
LMTNBUSRACSCAUSE|NB用户接入EUTRAN网络失败原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|NB用户接入，MME根据用户签约数据，进行ARD限制，拒绝NB接入的原因值。可供选择的原因值有：“PLMN not allowed"，“Tracking Area not allowed"，“Roaming not allowed in this tracking area"，“EPS services not allowed in this PLMN"，“No Suitable Cells In tracking area"。
T3412|是否支持小于系统缺省值的T3412值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|T3412为周期性跟踪区更新定时器，该定时器由MME下发给UE后，UE会按该定时器规定的时长定时发起跟踪区更新流程，该定时器的系统缺省取值为54分钟。如果因为操作员在配置时误修改或者其他情况使得T3412定时器的时长修改为非系统缺省值，可能会导致整网的UE行为异常。比如如果这个定时器的时长配置的很短，会导致整网的UE频繁向网络发起海量跟踪区更新消息而将网络冲击瘫痪。该安全变量用于控制MME是否支持小于系统缺省值的T3412值，系统默认不支持小于系统缺省值的T3412值。当该开关开启时（设置为支持），MME允许T3412值小于系统缺省值的T3412值（54分钟）。当该开关关闭时（设置为不支持），MME对小于系统缺省值的T3412值（54分钟），会修正为系统缺省值的T3412值（54分钟），即不允许T3412值小于系统缺省值的T3412值（54分钟）。如果在实际场景中，确实有小于系统缺省取值的使用场景，经过数据规划论证后，再开启该配置开关。
命令举例 
[MME]：设置移动管理参数，移动管理NAS消息重发次数为1，周期性跟踪区更新定时器T3412时长（秒）为10，MME可达定时器时长（秒）为2100，MME隐式分离定时器时长（秒）为1000。 
[MME] SET MOBILE MANAGEMENT:NASRESENDCOUNT=1,TAUTIMER=10,REACHTIMER=2100,IMPDETACHTIMER=1000; 
[GnGp SGSN：设置移动管理参数，路由周期性更新定时器（秒）为60，Ready定时器时长（秒）为30，SGSN不可达定时器时长（秒）为2700，SGSN MM上下文删除定时时长（分钟）为1000，Iu延迟释放为支持。 
[GnGp SGSN] SET MOBILE MANAGEMENT:RTUPDATEPERIOD=60,READYTIMER=30,STANDBYTIMER=2700,SGSNUNREACHABLETIMER=1000,FORSWITCHFORIURELEASE="YES"; 
父主题： [移动管理参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询移动管理参数(SHOW MOBILE MANAGEMENT) 
### 查询移动管理参数(SHOW MOBILE MANAGEMENT) 
命令功能 
本命令用于查询移动管理参数。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
RTUPDATEPERIOD|路由周期性更新定时器(秒)|参数可选性:任选参数；参数类型:整数。|该定时器用于设置指示MS发起周期性路由更新的时间间隔。SGSN通过attach accept消息或者routing area update accept消息携带Periodic RA update timer字段，将该时长传递给MS，MS收到后将此时长作为MS周期性路由更新时长。Iu模式时，MS从PMM-CONNECTED变为PMM-IDLE mode时，该定时器重置并被启动，当MS重新进入PMM-CONNECTED时停止。A/Gb模式时，当MS进入Standby状态时，该定时器重置并被启动，当MS进入READY态时，定时器停止。当定时器超时时，MS发起周期性路由更新。
READYTIMER|Ready定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该定时器用于设置READY定时器的时长。SGSN通过attach accept消息或者routing area update accept消息携带Negotiated READY timer value字段，将该时长传递给MS，MS收到后将此时长作为Ready状态变为Standby状态的时长。在MS侧，当MS发起上行信令或数据包时定时器启动。定时器超时时进入Standby状态，定时器停止（复位）。在SGSN侧，当接收到上行信令或数据包时定时器启动。定时器超时时进入Standby状态，定时器停止（复位）。
STANDBYTIMER|SGSN可达定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该定时器用于SGSN侧，当进入READY state或PMM-CONNECTED状态时，可达定时器停止。当返回到STANDBY或PMM-IDLE状态时，可达定时器被重置并且启动。当可达定时器超时时，SGSN会将MS置为隐式分离状态。可达定时器应该比MS使用的路由周期性更新定时器(T3312)时长略长点。
SGSNUNREACHABLETIMER|SGSN MM上下文删除定时器时长(分钟)|参数可选性:任选参数；参数类型:整数。|该安全变量是系统内部定义的，按照23.060协议的说明，上下文处于分离状态后，可以立即删除，也可以保留一段时间。具体时长取决于实际需要。作为一种实际应用的选择，SGSN可以在MS隐式或者显式分离后立即删除MS的MM上下文和PDP上下文；或者SGSN也可以将已经分离的MS的MM和PDP上下文以及鉴权三重组保留一段时间（根据该变量设置），这样可以在随后的GPRS附着中使用而不需要访问HLR。当MS隐式或者显式分离时，定时器启动，定时器超时时将MS的MM上下文删除，定时器停止（复位）。
FORSWITCHFORIURELEASE|Iu延迟释放|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|如果手机在附着或者路由更新请求消息中携带FOR=0，那么依靠此安全变量决定附着成功或者路由更新成功后是否立即释放Iu连接。支持：附着成功或者路由更新成功后，SGSN支持Iu连接延迟释放。不支持：附着成功或者路由更新成功后，立即释放Iu连接。
NASRESENDCOUNT|移动性管理NAS消息重发次数|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置MME重发NAS请求消息的次数，这些消息包括：AUTHENTICATION REQUEST，DETACH REQUEST，GUTI REALLOCATION COMMAND，IDENTITY REQUEST，SECURITY MODE COMMAND。按照24.301协议的说明，MME在发送NAS请求消息给UE的时候，会启动定时器，定时器超时前未收到UE的响应消息，定时器超时会重发该请求消息，该安全变量用于控制重发的次数。
TAUTIMER|周期性跟踪区更新定时器T3412时长(秒)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置周期性跟踪区更新定时器T3412时长。T3412是UE控制发起周期性跟踪区更新的定时器。按照24.301协议的说明，MME在ATTACH ACCEPT或者 TRACKING AREA UPDATE ACCEPT消息中将T3412的时长带给UE，用于控制UE发起周期性跟踪区更新的时间间隔。
REACHTIMER|MME可达定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置可达定时器时长。该定时器要比周期性跟踪区更新定时器T3412大，进入空闲态时，如果在移动可达定时器时长内，UE都没有发起周期性路由更新，说明UE已经不在该MME控制范围内，即UE不可达。可达定时器在UE进入空闲态时启动，在UE进入连接态时停止；如果该定时器超时而一直没有收到用户的任何消息，将清空PPF标志并启动隐式分离定时器。
IMPDETACHTIMER|MME隐式分离定时器时长(秒)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置隐式分离定时器时长。隐式分离就是MME本地删除UE的移动性管理上下文、会话和承载上下文，不通知UE。可达定时器超时后隐式分离定时器启动，用户进入连接态时停止；如果该定时器超时而一直没有收到用户的任何消息，MME将UE隐式分离。
MMEUNREACHABLETIMER|MME MM上下文删除定时器时长(分钟)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置UE分离或隐式分离之后到删除移动性管理上下文之间的时长。按照23.401协议的说明，上下文处于分离状态后，可以立即删除，也可以保留一段时间。具体时长取决于实际需要。作为一种实际应用的选择，MME可以在UE隐式或者显式分离后立即删除移动性管理上下文、会话和承载上下文。或者MME也可以将已经分离的用户的移动性管理上下文保留一段时间（根据该变量设置），这样可以在随后的EPS附着中使用而不需要访问HSS。
T3402|UE附着/跟踪区更新重发定时器T3402时长(秒)|参数可选性:任选参数；参数类型:整数。|该安全变量用于控制UE附着/跟踪区更新重发定时器T3402的时长。T3402在UE尝试附着或者跟踪区更新失败5次后启动，超时后再次尝试附着或者跟踪区更新。该定时器保证UE在接入失败之后能够继续尝试接入。MME通过 ATTACH ACCEPT、TRACKING AREA UPDATE ACCEPT或者ATTACH REJECT消息将T3402下发给UE。
MMEGETIMEI|MME 获取IMEI(SV)|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME是否需要在附着流程或者跟踪区更新流程中向UE获取IMEI/IMEISV，取值含义如下：不需要：表示MME不需要获取UE的IMEI或者IMEISV。获取IMEI：表示MME需要向UE获取IMEI。获取IMEISV：表示MME需要向UE获取IMEISV。支持ADD功能：表示MME支持ADD(Automatic Device Detection)功能。
LIMITLTEUSERACCESS|MME支持LTE用户接入限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量是ARD（Access Restriction Data）功能开关，主要是通过对UE的HSS基本信息中ARD参数的设置，实现S1口是否允许该UE附着或者跟踪区更新到EUTRAN网络。
LTEUSERACCESSCAUSE|LTE用户接入EUTRAN网络失败原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制UE因为ARD（Access Restriction Data）功能被限制接入EUTRAN网络，MME在S1口下发附着拒绝或者跟踪区更新拒绝消息时携带的原因值。可供选择的原因值有：“PLMN not allowed"，“Tracking Area not allowed"，“Roaming not allowed in this tracking area"，“EPS services not allowed in this PLMN"，“No Suitable Cells In tracking area"，“Severe network failure"，“Protocol error, unspecified"。
MMELIMITZONESWITCH|MME支持区域码限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量与“MME IMSI号段区域编码配置"ADD MME IMSI TAIZC配合使用，用于控制是否支持漫游限制功能，可以对不同的IMSI号段的同一个区域码设置不同的路由区。MME在用户接入时，根据从HSS获取到的用户签约的区域编码、IMSI号码、当前接入的跟踪区查询“MME IMSI号段区域编码配置"ADD MME IMSI TAIZC，确定是否允许用户接入。如果接入MME的用户号段不在MME IMSI号段区域编码配置中，MME根据跟踪区域码配置中的区域判断是否限制接入。
MMEEPLMNLISTNUM|支持EPLMN组数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME下发给UE的Attach Accept/TAU Accept消息中EPLMN组数。值含义如下：若变量值为“不支持"，则Attach Accept/TAU Accept消息中不带有EPLMN参数。若变量值为“支持5组"，则Attach Accept/TAU Accept消息中最多携带5组EPLMN。若变量值为“支持15组"，则Attach Accept/TAU Accept消息中最多携带15组EPLMN。
MMEZONECODELIMIT|由于区域编码限制用户接入拒绝原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制当用户IMSI号段不在区域限制的允许列表中的时候，MME拒绝用户的原因值。具体的原因值有：“IMSI unknown in HSS"，“Illegal UE"， “Illegal ME"，“EPS services not allowed"，“EPS services and non-EPS services not allowed"，“PLMN not allowed"，“Track Area not allowed"，“Roaming not allowed in this tracking area"，“EPS services not allowed in this PLMN"，“No suitable cells in tracking area"，“Not authorized for this CSG"
MMEDETACHCAUSE|MME发起的分离携带的分离原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制网络侧发起的分离流程时，如果分离类型为“re-attach not required"时，MME是否在分离请求消息中携带EMM Cause信元及携带的具体的EMM Cause。EMM Cause具体的值有：“IMSI unknown in HSS"，“Illegal UE"，“Illegal ME"，“EPS services not allowed"，“EPS services and non-EPS services not allowed"，“PLMN not allowed"，“Track Area not allowed"，“Roaming not allowed in this tracking area"，“EPS services not allowed in this PLMN"，“No suitable cells in tracking area"，“Not authorized for this CSG"。
LMTNBUSRACS|MME支持NB用户接入限制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于配置NB用户接入，MME是否要根据用户签约数据，进行ARD限制。
LMTNBUSRACSCAUSE|NB用户接入EUTRAN网络失败原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|NB用户接入，MME根据用户签约数据，进行ARD限制，拒绝NB接入的原因值。可供选择的原因值有：“PLMN not allowed"，“Tracking Area not allowed"，“Roaming not allowed in this tracking area"，“EPS services not allowed in this PLMN"，“No Suitable Cells In tracking area"。
T3412|是否支持小于系统缺省值的T3412值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|T3412为周期性跟踪区更新定时器，该定时器由MME下发给UE后，UE会按该定时器规定的时长定时发起跟踪区更新流程，该定时器的系统缺省取值为54分钟。如果因为操作员在配置时误修改或者其他情况使得T3412定时器的时长修改为非系统缺省值，可能会导致整网的UE行为异常。比如如果这个定时器的时长配置的很短，会导致整网的UE频繁向网络发起海量跟踪区更新消息而将网络冲击瘫痪。该安全变量用于控制MME是否支持小于系统缺省值的T3412值，系统默认不支持小于系统缺省值的T3412值。当该开关开启时（设置为支持），MME允许T3412值小于系统缺省值的T3412值（54分钟）。当该开关关闭时（设置为不支持），MME对小于系统缺省值的T3412值（54分钟），会修正为系统缺省值的T3412值（54分钟），即不允许T3412值小于系统缺省值的T3412值（54分钟）。如果在实际场景中，确实有小于系统缺省取值的使用场景，经过数据规划论证后，再开启该配置开关。
命令举例 
该命令用来查询移动管理参数 
SHOW MOBILE MANAGEMENT; 
`
(No.1) : SHOW MOBILE MANAGEMENT:
-----------------NFS_MMESGSN_0----------------
操作维护       路由周期性更新定时器(秒) Ready定时器时长(秒) SGSN可达定时器时长(秒) SGSN MM上下文删除定时器时长(分钟) Iu延迟释放 移动性管理NAS消息重发次数 周期性跟踪区更新定时器T3412时长(秒) MME可达定时器时长(秒) MME隐式分离定时器时长(秒) MME MM上下文删除定时器时长(分钟) UE附着/跟踪区更新重发定时器T3402时长(秒) MME 获取IMEI(SV) MME支持LTE用户接入限制 LTE用户接入EUTRAN网络失败原因      MME支持区域码限制 支持EPLMN组数 由于区域编码限制用户接入拒绝原因值 MME发起的分离携带的分离原因值 MME支持NB用户接入限制 NB用户接入EUTRAN网络失败原因值     是否支持小于系统缺省值的T3412值     
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           3240                     44                  3480                   1440                              不支持     4                         3240                                3480                  3480                      1440                             720                                      不需要           不支持                 No Suitable Cells In tracking area 不支持            不支持        Tracking Area not allowed          EPS services not allowed      不支持                No Suitable Cells In tracking area 不支持 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-03-30 15:46:07 耗时: 1.438秒
` 
父主题： [移动管理参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 系统控制参数配置 
## 系统控制参数配置 
背景知识 
MME支持Last UE Activity Time功能是MME位置上报功能的一个子功能，是为了让HSS获知UE最后活动的时间。 
功能描述 
该配置用于设置SGSN/MME的系统级控制参数，包括：的TM包尺寸和MME是否支持Last UE Activity Time功能。 
相关主题 
 
设置系统控制参数(SET SYSTEM CONTROL)
 
 
查询系统控制参数(SHOW SYSTEM CONTROL)
 
 
父主题： [安全变量]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置系统控制参数(SET SYSTEM CONTROL) 
### 设置系统控制参数(SET SYSTEM CONTROL) 
命令功能 
该命令用于设置系统控制参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
TMSIZE|TM包尺寸(B)|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MAP对话的包长度。SGSN向其他网元（如：HLR、SGSN等）发起MAP对话时，根据此安全变量限制对话的包长度。如果对话的包长度超过了安全变量设置的长度，那么在发起MAP对话时，将进行分包发送。保证每包的长度不超过此安全变量规定的长度。
LATR|是否支持Last UE Activity Time功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME是否支持Last UE Activity Time功能。MME支持该功能时，MME可以通过在IDA（Insert Subscriber Data Answer）消息中携带Last UE Activity Time字段告知HSS UE最后活动的时间。取值含义如下：是：表示支持Last UE Activity Time功能，即MME在接收到HSS发送的IDR（Insert Subscriber Data Request）消息后，给HSS回IDA消息时携带Last UE Activity Time字段。否：表示不支持Last UE Activity Time功能，即MME在接收到HSS发送的IDR消息后，给HSS回IDA消息时不携带Last UE Activity Time字段。
命令举例 
设置系统控制参数，TM包尺寸（B）为150 byte。 
SET SYSTEM CONTROL:TMSIZE=150 Byte; 
父主题： [系统控制参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询系统控制参数(SHOW SYSTEM CONTROL) 
### 查询系统控制参数(SHOW SYSTEM CONTROL) 
命令功能 
该命令用于查询系统控制参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TMSIZE|TM包尺寸(B)|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MAP对话的包长度。SGSN向其他网元（如：HLR、SGSN等）发起MAP对话时，根据此安全变量限制对话的包长度。如果对话的包长度超过了安全变量设置的长度，那么在发起MAP对话时，将进行分包发送。保证每包的长度不超过此安全变量规定的长度。
LATR|是否支持Last UE Activity Time功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME是否支持Last UE Activity Time功能。MME支持该功能时，MME可以通过在IDA（Insert Subscriber Data Answer）消息中携带Last UE Activity Time字段告知HSS UE最后活动的时间。取值含义如下：是：表示支持Last UE Activity Time功能，即MME在接收到HSS发送的IDR（Insert Subscriber Data Request）消息后，给HSS回IDA消息时携带Last UE Activity Time字段。否：表示不支持Last UE Activity Time功能，即MME在接收到HSS发送的IDR消息后，给HSS回IDA消息时不携带Last UE Activity Time字段。
命令举例 
查询系统控制参数。 
SHOW SYSTEM CONTROL; 
`
操作维护 TM包尺寸(B) 是否支持Last UE Activity Time功能 
---------------------------------------------------------
修改      2000       否 
---------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [系统控制参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 分组域参数配置 
## 分组域参数配置 
背景知识 
            
            无。
        
功能描述 
            
            分组域参数配置主要提供会话管理和切换相关的安全变量参数配置。
        
相关主题 
 
设置分组域参数(SET PACKET DOMAIN PARAMETER)
 
 
查询分组域参数(SHOW PACKET DOMAIN PARAMETER)
 
 
父主题： [安全变量]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置分组域参数(SET PACKET DOMAIN PARAMETER) 
### 设置分组域参数(SET PACKET DOMAIN PARAMETER) 
命令功能 
该命令用于设置分组域参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
OVERLOADINLCS|MME/SGSN支持Override参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制在LCS（LoCation Services，定位业务）功能开启（通过命令SHOW LICENSE查看受控项标识为7011的LICENSE）的情况下，由H-GMLC(Home Gateway Mobile Location Centre, 归属地网关移动位置中心，参见3GPP 23.271协议6.3.3章节)发起的MR-LR流程(正常立即定位流程，参见3GPP 23.271协议9.1.6章节)中，SGSN是否保存LCS客户端携带的Override权限标记。Override权限：表示2/3G用户在LCS业务中的优先级权限(参见3GPP 23.271协议9.5.1章节，Privacy Override Indicator (POI)的描述)。该安全变量有如下取值：NO：表示不保存Override权限标记。无论LCS客户端是任何类型，系统都必须先进行私密性检查(由H-GMLC发起，详见3GPP 23.271协议 9.1.1 章节(step5))，私密性检查通过后才可以发起定位。YES：保存Override权限标记，根据POI的取值做如下处理：1：LCS客户端类型为紧急定位（emergency Services）或合法性定位（lawfulIntercept Services）两者之一时，系统对LCS客户端立即进行定位而不需要进行私密性检查；0：无论LCS客户端是任何类型，系统都必须先进行私密性检查(由H-GMLC发起，详见3GPP 23.271协议 9.1.1 章节(step5))，私密性检查通过后才可以发起定位。
SERVICEHO|业务切换指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 25413 章节9.1.3 RAB ASSIGNMENT REQUEST、9.1.10 RELOCATION REQUEST或9.1.81 RANAP ENHANCED RELOCATION INFORMATION REQUEST消息中Service Handover IE的取值。当SGSN之间切换时，SGSN需要根据该安全变量设置IE Service Handover的取值，Service Handover用于RAB指派消息中使用，从非接入层看来，当前的RAB是应该切换到GSM，还是不应该切换到GSM，还是如果有问题则不切换到GSM。Service Handover有如下三个取值：Switch  to GSM：应该切换至GSM。Should not switch  to GSM：不应该切换至GSM。Error Rab should not switch  to GSM：有问题的RAB将不切换至GSM。
RABQUE|RAB排队|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 25413 章节9.2.1.3 RAB Parameters IE中Allocation/Retention Priority IE下Queuing Allowed IE的取值。当SGSN请求无线侧建立承载分配资源时，SGSN需要根据该安全变量设置IE Queuing Allowed的取值，Queuing Allowed用于指示是否将待建的RAB放入RAB队列中。Queuing Allowed有如下两个取值：queuing not allowed：本RAB建立不允许放入RAB资源分配队列。queuing allowed：本RAB建立允许放入RAB资源分配队列。
RABPREEMPT|RAB抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 25413 章节9.2.1.3 RAB Parameters IE中Allocation/Retention Priority IE下Pre-emption Capability IE的取值。当SGSN请求无线侧建立承载分配资源时，SGSN需要根据该安全变量设置IE Pre-emption Capability的取值， Pre-emption Capability用于指示是否支持RAB抢占。RAB抢占是指在RAB创建过程中，在无线侧资源紧张的情况下，本RAB是否可以抢占其他低优先级的RAB占用的资源。Pre-emption Capability有如下两个取值：shall not trigger pre-emption：本RAB建立不要触发抢占流程。may trigger pre-emption：本RAB建立可以触发抢占流程。
RABPRMPTEVUL|RAB被抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 25413 章节9.2.1.3 RAB Parameters IE中Allocation/Retention Priority IE下Pre-emption Vulnerability的取值。当SGSN请求无线侧建立承载分配资源时，SGSN需要根据该安全变量设置Pre-emption Vulnerability的取值， Pre-emption Vulnerability用于指示是否支持RAB被抢占。RAB被抢占是指在无线侧资源紧张的情况下，本RAB占用的资源是否可以被其他高优先级的RAB抢占。Pre-emption Capability有如下两个取值：not pre-emptable：本RAB不允许执行被抢占流程。pre-emptable：本RAB可以执行被抢占流程。
MMESMNASRESEND|会话管理NAS消息重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:0~10。|该安全变量用于设置协议3GPP 24301会话管理流程中MME重发NAS消息的次数。设置该安全变量后，当MME发送NAS请求消息时，在超过设置时间（由各个定时器决定）的情况下，如果没有收到UE的应答消息，MME将重新发送该NAS请求消息（重发该消息的最大次数不能超过本安全变量设置的次数）。如果在重发次数达到本安全变量设置的次数时，但是仍然没有收到UE的应答消息，MME将停止发送该NAS消息，流程将会失败。不同的NAS请求消息的超时时长是由不同的定时器决定的，具体对应关系如下：ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST消息：使用定时器标识为201651的MME ESM承载激活定时器（T3485)，该定时器的取值可以通过SET DEFPRETMR:TIMER=201651,CURINTERVAL=n;命令设置，可以通过SHOW DEFPRETMR:TIMER=201651;命令查询。ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST消息：使用定时器同ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST消息的定时器。MODIFY EPS BEARER CONTEXT REQUEST消息：使用定时器标识为201652的MME ESM承载修改定时器（T3486)，该定时器的取值可以通过SET DEFPRETMR:TIMER=201652,CURINTERVAL=n;命令设置，可以通过SHOW DEFPRETMR:TIMER=201652;命令查询。DEACTIVATE EPS BEARER CONTEXT REQUEST消息：使用定时器标识为201653的MME ESM承载去活定时器（T3495)，该定时器的取值可以通过SET DEFPRETMR:TIMER=201653,CURINTERVAL=n;命令设置，可以通过SHOW DEFPRETMR:TIMER=201653;MR命令查询。
MMEESMINFORESEND|ESM Information Request消息重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:0~10。|该安全变量用于设置ATTACH或者PDN连接流程中，MME重发ESM INFORMATION REQUEST的次数。设置该安全变量后，当MME发送ESM INFORMATION REQUEST消息时，在超过设置时间（通过定时器决定）后，如果没有收到UE回送的应答消息ESM INFORMATION RESPONSE，MME将重新发送该消息（重发该消息的最大次数不能超过本安全变量设置的次数）。如果在重发次数达到本安全变量设置的次数时，但是仍然没有收到UE的应答消息，MME将停止发送ESM INFORMATION REQUEST请求消息，该流程将会失败。ESM INFORMATION REQUEST消息的超时时长是通过定时器201654设置的。通过SET DEFPRETMR:TIMER=201654,CURINTERVAL=n;命令设置该定时器的取值，可以通过SHOW DEFPRETMR:TIMER=201654命令查询。
ARPHIGHPRIORITY|ARP高优先级权重值|参数可选性:任选参数；参数类型:整数；参数范围为:1~14。|该安全变量用于实现协议3GPP 23401附录Annex E (normative)描述的功能，设置EPS bearer ARP和Pre-Rel-8 ARP之间转换EPS bearer ARP的高优先级映射阈值。ARP（Allocation and Retention Priority)是用来指示在承载建立和修改流程中，如果资源紧张，该流程是继续还是拒绝。流程中的网元应优先保证高优先级ARP（值越小，优先级越高）的承载资源分配。当MME和Gn/Gp SGSN互连，用户在2G/3G和LTE之间移动时，MME需要把EPS承载和PDP上下文进行一对一的映射，主要是其中的EPS QoS和Pre-R8 QoS进行一对一的映射，需要把Pre-R8 QoS携带给具有UTRAN/GERAN能力的UE。该安全变量和安全变量“ARP中优先级权重值”两者配合完成ARP的映射。EPS bearer ARP到Pre-Rel-8 ARP映射规则是这样的：1~ARP高优先级权重值 映射为 1。ARP高优先级权重值+1~ARP中优先级权重值 映射为 2。 ARP中优先级权重值+1~15 映射为 3。 Pre-Rel-8 ARP到EPS bearer ARP映射规则是这样的：1 映射为 1。2 映射为 ARP高优先级权重值+1。 3 映射为 ARP中优先级权重值+1。 该安全变量的取值要小于安全变量“ARP中优先级权重值”的取值。
ARPMEDPRIORITY|ARP中优先级权重值|参数可选性:任选参数；参数类型:整数；参数范围为:2~15。|该安全变量用于实现协议3GPP 23401附录Annex E (normative)描述的功能，设置EPS bearer ARP和Pre-Rel-8 ARP之间转换EPS bearer ARP的中优先级映射阈值。当MME和Gn/Gp SGSN互连，用户在2G/3G和LTE之间移动时，MME需要把EPS 承载和PDP上下文进行一对一的映射，主要是其中的EPS QoS和Pre-R8 QoS进行一对一的映射，需要把Pre-R8 QoS携带给具有UTRAN/GERAN能力的UE 。该安全变量和安全变量ARP高优先级权重值配合完成ARP的映射。EPS bearer ARP到Pre-Rel-8 ARP映射规则是这样的：1：ARP高优先级权重值 映射为 1。ARP高优先级权重值+1：ARP中优先级权重值 映射为 2。 ARP中优先级权重值+1：15 映射为 3。 Pre-Rel-8 ARP到EPS bearer ARP映射规则是这样的：1 映射为 1。2 映射为 ARP高优先级权重值+1。 3 映射为 ARP中优先级权重值+1。 该安全变量的取值要大于安全变量“ARP高优先级权重值”的取值。
ERABPREEMPT|支持E-RAB抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 36413 章节9.2.1.60 Allocation and Retention Priority IE Pre-emption Capability的取值。当MME和Gn/Gp SGSN互连，用户从2G/3G到LTE移动时，MME需要根据该安全变量设置IE Pre-emption Capability的取值， Pre-emption Capability用于指示是否支持E-RAB抢占。E-RAB抢占是指在E-RAB创建过程中，在无线侧资源紧张的情况下，本E-RAB是否可以抢占其他低优先级的E-RAB占用的资源。Pre-emption Capability有如下两个取值：shall not trigger pre-emption：本E-RAB建立不要触发抢占流程。may trigger pre-emption：本E-RAB建立可以触发抢占流程。
ERABPREEMPTVUL|支持E-RAB被抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 36413 章节9.2.1.60 Allocation and Retention Priority IE Pre-emption Vulnerability的取值。当MME和Gn/Gp SGSN互连，用户从2G/3G到LTE移动时，MME需要根据该安全变量设置Pre-emption Vulnerability的取值， Pre-emption Vulnerability用于指示是否支持E-RAB被抢占。E-RAB被抢占是指在无线侧资源紧张的情况下，本E-RAB占用的资源是否可以被其他高优先级的E-RAB抢占。Pre-emption Capability有如下两个取值：not pre-emptable：本E-RAB不允许执行被抢占流程pre-emptable：本E-RAB可以执行被抢占流程。
S5S8PROTOCOL|选择S5/S8接口协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于MME在选择SGW或者PGW时，SGW或者PGW的S5/S8接口是基于GTP协议还是基于PMIP协议。根据SGW和PGW支持的协议类型进行设置。该安全变量包括如下两种选项：GTP：选择GTP协议类型。通常情况选择GTP协议。PMIP：选择PMIP协议类型。PMIP协议一般用于3GPP 23402定义的和非3GPP互通的流程。
TOPOLOGY|Gateway选择是否考虑拓扑关系|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME在选择SGW或者PGW时，是否考虑协议3GPP 29.303 4.3.2章节描述SGW和PGW的拓扑关系。该安全变量包括如下两种选项：YES:MME将优先选择拓扑关系最接近的一对SGW和PGW。NO:MME在选择SGW和PGW时，不考虑两者之间的拓扑关系。
MMEUNDIRECTFWD|切换中MME支持非直接数据前转|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于实现协议3GPP 23401 5.5.1.2章节和5.5.2章节S1切换过程中非直接数据前转隧道建立功能。该变量有如下两种取值：NO:MME在切换过程中将不执行创建非直接数据前转隧道的过程。YES:MME将根据情况执行创建非直接数据前转隧道的过程。分如下情况：MME不改变的S1切换，如果满足如下条件：源eNodeB的Handover Required消息和目标eNodeB的Handover Request Acknowledge消息都指示源eNodeB和目标eNodeB之间没有直接数据前转连接，则MME创建非直接数据前转隧道。MME改变的S1切换，在目标MME，如果满足如下条件：源MME的Forward Relocation Request消息和目标eNodeB的Handover Request Acknowledge消息都指示源eNodeB和目标eNodeB之间没有直接数据前转连接，而且切换过程中重新选择了另外的SGW，则MME创建非直接数据前转隧道。MME改变的S1切换，在源MME，如果满足如下条件：源eNodeB的Handover Required消息和目标MME的 Forward Relocation Response消息都指示源eNodeB和目标eNodeB之间没有直接数据前转连接，则MME创建非直接数据前转隧道。
MMEIMSVOPS|MME支持基于PS会话IMS语音|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在Attach和TAU流程中，MME发送Attach Accept或TAU Accept消息时，消息中会携带一个“基于PS会话的IMS语音（IMS voice over PS Session）”指示（IMS voice over PS Session Supported Indication）给UE，该安全变量用于控制IMS voice over PS Session的取值，有如下两种：是(YES)：如果该安全变量设置为是，表示网络支持基于PS会话的IMS语音。否(NO)：如果该安全变量设置为否，表示网络不支持基于PS会话的IMS语音。具体可参考3GPP TS 23.401的4.3.5.8章节。
DEACGBR|寻呼失败时去活GBR承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|网络侧发起业务请求过程，寻呼失败时，MME根据此安全变量的配置值来判断是否要对GBR承载进行去活，该安全变量有如下两种配置值：去活(YES)：表示MME此时需要去活GBR承载。不去活(NO)：表示MME此时不要去活GBR承载。具体可参考3GPP TS 23.401的5.3.4.3章节。
DATAFORWARD|切换中SGSN是否支持数据前转|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于实现协议3GPP 23060 6.9.2.2章节Serving RNS Relocation Procedures中数据前转隧道建立功能。该安全变量有如下两种取值：不支持：SGSN在切换过程中将不执行创建数据前转隧道的过程。支持：SGSN在切换过程中执行创建数据前转隧道的过程。
QosNegotiation|Gn口GTP消息指示支持QOS协商|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 29060 章节7.7.48 Common Flags中No QoS negotiation bit field的取值。当SGSN进行Update  PDP Context procedure流程时，需要根据该安全变量的值设置SGSN发送给GGSN的Update PDP Context Request消息中Common Flags中的No QoS negotiation bit，用于向GGSN指示QoS重协商在本次更新流程中是否支持。该安全变量有如下两个取值：是：表示SGSN支持QoS协商。否：表示SGSN不支持QoS协商。
QosUpgrade|Gn口GTP消息指示支持QOS提升|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 29060 章节7.7.48 Common Flags中Upgrade QoS Supported bit field的取值。当SGSN进行Create PDP Context procedure或Update  PDP Context procedure流程时，需要根据该安全变量的值设置SGSN发送给GGSN的Update PDP Context Request消息中Common Flags中的Upgrade QoS Supported bit，用于向GGSN指示QoS提升在本次流程中是否支持。该安全变量有如下两个取值：是：表示SGSN支持QoS提升。否：表示SGSN不支持QoS提升。
FQDNRESOLVESGW|使用TAI-FQDN或eNB-FQDN解析SGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME在选择SGW时，构造SGW的FQDN的方法，有如下两种选项：TAI-FQDN：根据TAI构造FQDN，参见协议3GPP 23003 19.4.2.3章节。eNB-FQDN：根据eNodeB构造FQDN，参见协议3GPP 23003 19.4.2.10章节。
APNFLTSCDR|支持按照APN过滤S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制SGSN是否支持按照APN屏蔽S-CDR话单功能。该安全变量有如下取值：否：表示SGSN不支持按照APN屏蔽S-CDR话单功能。是：表示SGSN支持按照APN屏蔽S-CDR话单功能。
IMSIFLTCDR|支持按照IMSI号段过滤CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制SGSN是否支持根据IMSI过滤MCDR话单功能。该安全变量有如下取值：否：表示SGSN不支持根据IMSI是否过滤MCDR话单功能。是：表示SGSN支持根据IMSI是否过滤MCDR话单功能。
MMESUPLCS|MME支持紧急定位参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME是否支持4G用户紧急LCS（LoCation Services，定位业务）功能。该安全变量有如下取值：NO：表示MME不支持4G用户紧急LCS功能。YES：表示MME支持4G用户紧急LCS功能，区分如下情况：用户局间切入，等待源MME的切换完成确认消息超时，MME发送定位位置信息报告到定位中心（GMLC)；用户局间切入，收到源MME的前转切换完成确认消息，MME发送定位位置信息报告到定位中心（GMLC)；用户发起紧急附着完成后，MME向计算中心（E-SMLC）发送定位请求；用户发起紧急PDN连接请求成功后，MME向计算中心（E-SMLC）发送定位请求。
PLMNCHGSCDR|PLMN改变时是否产生S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制SGSN是否支持PLMN改变触发S-CDR话单功能。该安全变量有如下两个取值：不产生S-CDR：表示SGSN不支持PLMN改变触发S-CDR话单功能。2G间局内RAU产生S-CDR：表示SGSN只支持2G局内RAU流程，PLMN改变时触发S-CDR话单功能。
S5S8IPTYPE|SGW S5S8口组网配置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME在选择PGW时，根据SGW的S5/S8接口地址类型选择对应的PGW的S5/S8接口地址类型，有如下四种选项：IPv4：选择IPv4类型的PGW地址。IPv6：选择IPv6类型的PGW地址。IPv4v6：选择IPv4v6双栈类型的PGW地址。S11：选择跟本MME的S11接口地址类型相同的PGW地址，可通过命令SHOW MME GTPC查询本MME的S11接口地址类型。
命令举例 
[MME]：设置分组域参数，会话管理NAS消息重发次数为1，ESM信息请求消息重发次数为1，ARP高优先级权重值为1，ARP中优先级权重值为2。 
[MME]SET PACKET DOMAIN PARAMETER:MMESMNASRESEND=1,MMEESMINFORESEND=1,ARPHIGHPRIORITY=1,ARPMEDPRIORITY=2; 
[GnGp SGSN]：设置分组域参数，LCS中override权限取值为是，业务切换指示为应切换至GSM，RAB排队为是，RAB抢占为是。 
[GnGp SGSN]SET PACKET DOMAIN PARAMETER:OVERLOADINLCS="YES",SERVICEHO="Switch to GSM",RABQUE="YES",RABPREEMPT="YES"; 
父主题： [分组域参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询分组域参数(SHOW PACKET DOMAIN PARAMETER) 
### 查询分组域参数(SHOW PACKET DOMAIN PARAMETER) 
命令功能 
该命令用于查询分组域参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
OVERLOADINLCS|MME/SGSN支持Override参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制在LCS（LoCation Services，定位业务）功能开启（通过命令SHOW LICENSE查看受控项标识为7011的LICENSE）的情况下，由H-GMLC(Home Gateway Mobile Location Centre, 归属地网关移动位置中心，参见3GPP 23.271协议6.3.3章节)发起的MR-LR流程(正常立即定位流程，参见3GPP 23.271协议9.1.6章节)中，SGSN是否保存LCS客户端携带的Override权限标记。Override权限：表示2/3G用户在LCS业务中的优先级权限(参见3GPP 23.271协议9.5.1章节，Privacy Override Indicator (POI)的描述)。该安全变量有如下取值：NO：表示不保存Override权限标记。无论LCS客户端是任何类型，系统都必须先进行私密性检查(由H-GMLC发起，详见3GPP 23.271协议 9.1.1 章节(step5))，私密性检查通过后才可以发起定位。YES：保存Override权限标记，根据POI的取值做如下处理：1：LCS客户端类型为紧急定位（emergency Services）或合法性定位（lawfulIntercept Services）两者之一时，系统对LCS客户端立即进行定位而不需要进行私密性检查；0：无论LCS客户端是任何类型，系统都必须先进行私密性检查(由H-GMLC发起，详见3GPP 23.271协议 9.1.1 章节(step5))，私密性检查通过后才可以发起定位。
SERVICEHO|业务切换指示|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 25413 章节9.1.3 RAB ASSIGNMENT REQUEST、9.1.10 RELOCATION REQUEST或9.1.81 RANAP ENHANCED RELOCATION INFORMATION REQUEST消息中Service Handover IE的取值。当SGSN之间切换时，SGSN需要根据该安全变量设置IE Service Handover的取值，Service Handover用于RAB指派消息中使用，从非接入层看来，当前的RAB是应该切换到GSM，还是不应该切换到GSM，还是如果有问题则不切换到GSM。Service Handover有如下三个取值：Switch  to GSM：应该切换至GSM。Should not switch  to GSM：不应该切换至GSM。Error Rab should not switch  to GSM：有问题的RAB将不切换至GSM。
RABQUE|RAB排队|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 25413 章节9.2.1.3 RAB Parameters IE中Allocation/Retention Priority IE下Queuing Allowed IE的取值。当SGSN请求无线侧建立承载分配资源时，SGSN需要根据该安全变量设置IE Queuing Allowed的取值，Queuing Allowed用于指示是否将待建的RAB放入RAB队列中。Queuing Allowed有如下两个取值：queuing not allowed：本RAB建立不允许放入RAB资源分配队列。queuing allowed：本RAB建立允许放入RAB资源分配队列。
RABPREEMPT|RAB抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 25413 章节9.2.1.3 RAB Parameters IE中Allocation/Retention Priority IE下Pre-emption Capability IE的取值。当SGSN请求无线侧建立承载分配资源时，SGSN需要根据该安全变量设置IE Pre-emption Capability的取值， Pre-emption Capability用于指示是否支持RAB抢占。RAB抢占是指在RAB创建过程中，在无线侧资源紧张的情况下，本RAB是否可以抢占其他低优先级的RAB占用的资源。Pre-emption Capability有如下两个取值：shall not trigger pre-emption：本RAB建立不要触发抢占流程。may trigger pre-emption：本RAB建立可以触发抢占流程。
RABPRMPTEVUL|RAB被抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 25413 章节9.2.1.3 RAB Parameters IE中Allocation/Retention Priority IE下Pre-emption Vulnerability的取值。当SGSN请求无线侧建立承载分配资源时，SGSN需要根据该安全变量设置Pre-emption Vulnerability的取值， Pre-emption Vulnerability用于指示是否支持RAB被抢占。RAB被抢占是指在无线侧资源紧张的情况下，本RAB占用的资源是否可以被其他高优先级的RAB抢占。Pre-emption Capability有如下两个取值：not pre-emptable：本RAB不允许执行被抢占流程。pre-emptable：本RAB可以执行被抢占流程。
MMESMNASRESEND|会话管理NAS消息重发次数|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置协议3GPP 24301会话管理流程中MME重发NAS消息的次数。设置该安全变量后，当MME发送NAS请求消息时，在超过设置时间（由各个定时器决定）的情况下，如果没有收到UE的应答消息，MME将重新发送该NAS请求消息（重发该消息的最大次数不能超过本安全变量设置的次数）。如果在重发次数达到本安全变量设置的次数时，但是仍然没有收到UE的应答消息，MME将停止发送该NAS消息，流程将会失败。不同的NAS请求消息的超时时长是由不同的定时器决定的，具体对应关系如下：ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST消息：使用定时器标识为201651的MME ESM承载激活定时器（T3485)，该定时器的取值可以通过SET DEFPRETMR:TIMER=201651,CURINTERVAL=n;命令设置，可以通过SHOW DEFPRETMR:TIMER=201651;命令查询。ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST消息：使用定时器同ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST消息的定时器。MODIFY EPS BEARER CONTEXT REQUEST消息：使用定时器标识为201652的MME ESM承载修改定时器（T3486)，该定时器的取值可以通过SET DEFPRETMR:TIMER=201652,CURINTERVAL=n;命令设置，可以通过SHOW DEFPRETMR:TIMER=201652;命令查询。DEACTIVATE EPS BEARER CONTEXT REQUEST消息：使用定时器标识为201653的MME ESM承载去活定时器（T3495)，该定时器的取值可以通过SET DEFPRETMR:TIMER=201653,CURINTERVAL=n;命令设置，可以通过SHOW DEFPRETMR:TIMER=201653;MR命令查询。
MMEESMINFORESEND|ESM Information Request消息重发次数|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置ATTACH或者PDN连接流程中，MME重发ESM INFORMATION REQUEST的次数。设置该安全变量后，当MME发送ESM INFORMATION REQUEST消息时，在超过设置时间（通过定时器决定）后，如果没有收到UE回送的应答消息ESM INFORMATION RESPONSE，MME将重新发送该消息（重发该消息的最大次数不能超过本安全变量设置的次数）。如果在重发次数达到本安全变量设置的次数时，但是仍然没有收到UE的应答消息，MME将停止发送ESM INFORMATION REQUEST请求消息，该流程将会失败。ESM INFORMATION REQUEST消息的超时时长是通过定时器201654设置的。通过SET DEFPRETMR:TIMER=201654,CURINTERVAL=n;命令设置该定时器的取值，可以通过SHOW DEFPRETMR:TIMER=201654命令查询。
ARPHIGHPRIORITY|ARP高优先级权重值|参数可选性:任选参数；参数类型:整数。|该安全变量用于实现协议3GPP 23401附录Annex E (normative)描述的功能，设置EPS bearer ARP和Pre-Rel-8 ARP之间转换EPS bearer ARP的高优先级映射阈值。ARP（Allocation and Retention Priority)是用来指示在承载建立和修改流程中，如果资源紧张，该流程是继续还是拒绝。流程中的网元应优先保证高优先级ARP（值越小，优先级越高）的承载资源分配。当MME和Gn/Gp SGSN互连，用户在2G/3G和LTE之间移动时，MME需要把EPS承载和PDP上下文进行一对一的映射，主要是其中的EPS QoS和Pre-R8 QoS进行一对一的映射，需要把Pre-R8 QoS携带给具有UTRAN/GERAN能力的UE。该安全变量和安全变量“ARP中优先级权重值”两者配合完成ARP的映射。EPS bearer ARP到Pre-Rel-8 ARP映射规则是这样的：1~ARP高优先级权重值 映射为 1。ARP高优先级权重值+1~ARP中优先级权重值 映射为 2。 ARP中优先级权重值+1~15 映射为 3。 Pre-Rel-8 ARP到EPS bearer ARP映射规则是这样的：1 映射为 1。2 映射为 ARP高优先级权重值+1。 3 映射为 ARP中优先级权重值+1。 该安全变量的取值要小于安全变量“ARP中优先级权重值”的取值。
ARPMEDPRIORITY|ARP中优先级权重值|参数可选性:任选参数；参数类型:整数。|该安全变量用于实现协议3GPP 23401附录Annex E (normative)描述的功能，设置EPS bearer ARP和Pre-Rel-8 ARP之间转换EPS bearer ARP的中优先级映射阈值。当MME和Gn/Gp SGSN互连，用户在2G/3G和LTE之间移动时，MME需要把EPS 承载和PDP上下文进行一对一的映射，主要是其中的EPS QoS和Pre-R8 QoS进行一对一的映射，需要把Pre-R8 QoS携带给具有UTRAN/GERAN能力的UE 。该安全变量和安全变量ARP高优先级权重值配合完成ARP的映射。EPS bearer ARP到Pre-Rel-8 ARP映射规则是这样的：1：ARP高优先级权重值 映射为 1。ARP高优先级权重值+1：ARP中优先级权重值 映射为 2。 ARP中优先级权重值+1：15 映射为 3。 Pre-Rel-8 ARP到EPS bearer ARP映射规则是这样的：1 映射为 1。2 映射为 ARP高优先级权重值+1。 3 映射为 ARP中优先级权重值+1。 该安全变量的取值要大于安全变量“ARP高优先级权重值”的取值。
ERABPREEMPT|支持E-RAB抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 36413 章节9.2.1.60 Allocation and Retention Priority IE Pre-emption Capability的取值。当MME和Gn/Gp SGSN互连，用户从2G/3G到LTE移动时，MME需要根据该安全变量设置IE Pre-emption Capability的取值， Pre-emption Capability用于指示是否支持E-RAB抢占。E-RAB抢占是指在E-RAB创建过程中，在无线侧资源紧张的情况下，本E-RAB是否可以抢占其他低优先级的E-RAB占用的资源。Pre-emption Capability有如下两个取值：shall not trigger pre-emption：本E-RAB建立不要触发抢占流程。may trigger pre-emption：本E-RAB建立可以触发抢占流程。
ERABPREEMPTVUL|支持E-RAB被抢占|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 36413 章节9.2.1.60 Allocation and Retention Priority IE Pre-emption Vulnerability的取值。当MME和Gn/Gp SGSN互连，用户从2G/3G到LTE移动时，MME需要根据该安全变量设置Pre-emption Vulnerability的取值， Pre-emption Vulnerability用于指示是否支持E-RAB被抢占。E-RAB被抢占是指在无线侧资源紧张的情况下，本E-RAB占用的资源是否可以被其他高优先级的E-RAB抢占。Pre-emption Capability有如下两个取值：not pre-emptable：本E-RAB不允许执行被抢占流程pre-emptable：本E-RAB可以执行被抢占流程。
S5S8PROTOCOL|选择S5/S8接口协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于MME在选择SGW或者PGW时，SGW或者PGW的S5/S8接口是基于GTP协议还是基于PMIP协议。根据SGW和PGW支持的协议类型进行设置。该安全变量包括如下两种选项：GTP：选择GTP协议类型。通常情况选择GTP协议。PMIP：选择PMIP协议类型。PMIP协议一般用于3GPP 23402定义的和非3GPP互通的流程。
TOPOLOGY|Gateway选择是否考虑拓扑关系|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME在选择SGW或者PGW时，是否考虑协议3GPP 29.303 4.3.2章节描述SGW和PGW的拓扑关系。该安全变量包括如下两种选项：YES:MME将优先选择拓扑关系最接近的一对SGW和PGW。NO:MME在选择SGW和PGW时，不考虑两者之间的拓扑关系。
MMEUNDIRECTFWD|切换中MME支持非直接数据前转|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于实现协议3GPP 23401 5.5.1.2章节和5.5.2章节S1切换过程中非直接数据前转隧道建立功能。该变量有如下两种取值：NO:MME在切换过程中将不执行创建非直接数据前转隧道的过程。YES:MME将根据情况执行创建非直接数据前转隧道的过程。分如下情况：MME不改变的S1切换，如果满足如下条件：源eNodeB的Handover Required消息和目标eNodeB的Handover Request Acknowledge消息都指示源eNodeB和目标eNodeB之间没有直接数据前转连接，则MME创建非直接数据前转隧道。MME改变的S1切换，在目标MME，如果满足如下条件：源MME的Forward Relocation Request消息和目标eNodeB的Handover Request Acknowledge消息都指示源eNodeB和目标eNodeB之间没有直接数据前转连接，而且切换过程中重新选择了另外的SGW，则MME创建非直接数据前转隧道。MME改变的S1切换，在源MME，如果满足如下条件：源eNodeB的Handover Required消息和目标MME的 Forward Relocation Response消息都指示源eNodeB和目标eNodeB之间没有直接数据前转连接，则MME创建非直接数据前转隧道。
MMEIMSVOPS|MME支持基于PS会话IMS语音|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|在Attach和TAU流程中，MME发送Attach Accept或TAU Accept消息时，消息中会携带一个“基于PS会话的IMS语音（IMS voice over PS Session）”指示（IMS voice over PS Session Supported Indication）给UE，该安全变量用于控制IMS voice over PS Session的取值，有如下两种：是(YES)：如果该安全变量设置为是，表示网络支持基于PS会话的IMS语音。否(NO)：如果该安全变量设置为否，表示网络不支持基于PS会话的IMS语音。具体可参考3GPP TS 23.401的4.3.5.8章节。
DEACGBR|寻呼失败时去活GBR承载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|网络侧发起业务请求过程，寻呼失败时，MME根据此安全变量的配置值来判断是否要对GBR承载进行去活，该安全变量有如下两种配置值：去活(YES)：表示MME此时需要去活GBR承载。不去活(NO)：表示MME此时不要去活GBR承载。具体可参考3GPP TS 23.401的5.3.4.3章节。
DATAFORWARD|切换中SGSN是否支持数据前转|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于实现协议3GPP 23060 6.9.2.2章节Serving RNS Relocation Procedures中数据前转隧道建立功能。该安全变量有如下两种取值：不支持：SGSN在切换过程中将不执行创建数据前转隧道的过程。支持：SGSN在切换过程中执行创建数据前转隧道的过程。
QosNegotiation|Gn口GTP消息指示支持QOS协商|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 29060 章节7.7.48 Common Flags中No QoS negotiation bit field的取值。当SGSN进行Update  PDP Context procedure流程时，需要根据该安全变量的值设置SGSN发送给GGSN的Update PDP Context Request消息中Common Flags中的No QoS negotiation bit，用于向GGSN指示QoS重协商在本次更新流程中是否支持。该安全变量有如下两个取值：是：表示SGSN支持QoS协商。否：表示SGSN不支持QoS协商。
QosUpgrade|Gn口GTP消息指示支持QOS提升|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制协议3GPP 29060 章节7.7.48 Common Flags中Upgrade QoS Supported bit field的取值。当SGSN进行Create PDP Context procedure或Update  PDP Context procedure流程时，需要根据该安全变量的值设置SGSN发送给GGSN的Update PDP Context Request消息中Common Flags中的Upgrade QoS Supported bit，用于向GGSN指示QoS提升在本次流程中是否支持。该安全变量有如下两个取值：是：表示SGSN支持QoS提升。否：表示SGSN不支持QoS提升。
FQDNRESOLVESGW|使用TAI-FQDN或eNB-FQDN解析SGW|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME在选择SGW时，构造SGW的FQDN的方法，有如下两种选项：TAI-FQDN：根据TAI构造FQDN，参见协议3GPP 23003 19.4.2.3章节。eNB-FQDN：根据eNodeB构造FQDN，参见协议3GPP 23003 19.4.2.10章节。
APNFLTSCDR|支持按照APN过滤S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制SGSN是否支持按照APN屏蔽S-CDR话单功能。该安全变量有如下取值：否：表示SGSN不支持按照APN屏蔽S-CDR话单功能。是：表示SGSN支持按照APN屏蔽S-CDR话单功能。
IMSIFLTCDR|支持按照IMSI号段过滤CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制SGSN是否支持根据IMSI过滤MCDR话单功能。该安全变量有如下取值：否：表示SGSN不支持根据IMSI是否过滤MCDR话单功能。是：表示SGSN支持根据IMSI是否过滤MCDR话单功能。
MMESUPLCS|MME支持紧急定位参数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME是否支持4G用户紧急LCS（LoCation Services，定位业务）功能。该安全变量有如下取值：NO：表示MME不支持4G用户紧急LCS功能。YES：表示MME支持4G用户紧急LCS功能，区分如下情况：用户局间切入，等待源MME的切换完成确认消息超时，MME发送定位位置信息报告到定位中心（GMLC)；用户局间切入，收到源MME的前转切换完成确认消息，MME发送定位位置信息报告到定位中心（GMLC)；用户发起紧急附着完成后，MME向计算中心（E-SMLC）发送定位请求；用户发起紧急PDN连接请求成功后，MME向计算中心（E-SMLC）发送定位请求。
PLMNCHGSCDR|PLMN改变时是否产生S-CDR|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制SGSN是否支持PLMN改变触发S-CDR话单功能。该安全变量有如下两个取值：不产生S-CDR：表示SGSN不支持PLMN改变触发S-CDR话单功能。2G间局内RAU产生S-CDR：表示SGSN只支持2G局内RAU流程，PLMN改变时触发S-CDR话单功能。
S5S8IPTYPE|SGW S5S8口组网配置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于控制MME在选择PGW时，根据SGW的S5/S8接口地址类型选择对应的PGW的S5/S8接口地址类型，有如下四种选项：IPv4：选择IPv4类型的PGW地址。IPv6：选择IPv6类型的PGW地址。IPv4v6：选择IPv4v6双栈类型的PGW地址。S11：选择跟本MME的S11接口地址类型相同的PGW地址，可通过命令SHOW MME GTPC查询本MME的S11接口地址类型。
命令举例 
查询分组域参数。 
SHOW PACKET DOMAIN PARAMETER; 
`
命令 (No.4): SHOW PACKET DOMAIN PARAMETER
操作维护  MME/SGSN支持Override参数   业务切换指示               RAB排队   RAB抢占   RAB被抢占   会话管理NAS消息重发次数   ESM Information Request消息重发次数   ARP高优先级权重值   ARP中优先级权重值   支持E-RAB抢占   支持E-RAB被抢占   选择S5/S8接口协议类型   Gateway选择是否考虑拓扑关系   切换中MME支持非直接数据前转   MME支持基于PS会话IMS语音   寻呼失败时去活GBR承载   切换中SGSN是否支持数据前转   Gn口GTP消息指示支持QOS协商   Gn口GTP消息指示支持QOS提升   使用TAI-FQDN或eNB-FQDN解析SGW   支持按照APN过滤S-CDR   支持按照IMSI号段过滤CDR   MME支持紧急定位参数   PLMN改变时是否产生S-CDR   SGW S5S8口组网配置
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      否                         应该切换至GSM              否        否        否          4                         2                                     5                   10                  否              否                GTP                     否                            需要                          否                         去活                    支持                         是                           否                           TAI-FQDN解析SGW                 否                     否                        否                    不产生S-CDR               同S11口
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.059 秒）。
` 
父主题： [分组域参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## LLC相关配置 
## LLC相关配置 
背景知识 
协议栈中的逻辑链路控制（LLC Logical Link Control）层协议，类似于国际标准化组织7层参考模型中的第2层（数据链路层）。 
LLC层是针对GSM和EDGE无线接入技术的手机侧协议栈，如果是3G的无线环境，例如WCDMA等，则没有LLC层。相应的功能由RRC层实体替代。 
LLC主要作用是在移动台MS和GPRS业务支持节点SGSN的层3的实体之间传送信息。LLC提供通过逻辑连接在MS和SGSN的对等实体之间的消息传送，在实际的GPRS手机协议栈体系结构中，LLC层位于GPRS移动性管理协议层GMM。 
LLC 层的基本功能如下: 
 
提供用数据链路连接标识符DLCI（Data LinkConnection Identifier）区分一个或多个逻辑连接。
 
 
支持证实模式和非证实模式数据传输。
 
 
允许MS和SGSN之间进行XID ( ExchangeIdentification) 协商，选用合适的XID进行数据传输。
 
 
对通过逻辑链路传送帧顺序进行控制。
 
 
逻辑链路流量控制，对逻辑链路上的传送信息、信息格式和操作错误的检测。
 
 
对检测到的信息传送、信息格式和操作错误的恢复,报告不可恢复的错误。
 
 
加密用户数据。
 
 
功能描述 
LLC相关配置提供了LLC分组消息数据单元的生存周期、LLC SAPI3、LLC SAPI5、LLC SAPI9、LLC SAPI11等参数的配置，控制LLC在消息分发和处理时，对数据区释放、消息重传、缓存等进行安全、稳定的传输。 
相关主题 
 
LLC参数配置
 
 
LLC SAPI3参数配置
 
 
LLC SAPI5参数配置
 
 
LLC SAPI9参数配置
 
 
LLC SAPI11参数配置
 
 
父主题： [安全变量]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### LLC参数配置 
### LLC参数配置 
背景知识 
协议栈中的逻辑链路控制（LLC Logical Link Control）层协议，类似于国际标准化组织7层参考模型中的第2层（数据链路层）。 
LLC主要作用是在移动台MS和GPRS业务支持节点SGSN的层3的实体之间传送信息。LLC提供通过逻辑连接在MS和SGSN的对等实体之间的消息传送，在实际的GPRS手机协议栈体系结构中，LLC层位于GPRS移动性管理协议层GMM。 
功能描述 
用于设置LLC分组消息数据单元的生存周期，当为某个LLC消息数据单元分配数据区时开始计时，超过该配置时间则将分配的数据区释放 
相关主题 
 
设置LLC参数(SET LLC PARAMETER)
 
 
查询LLC参数(SHOW LLC PARAMETER)
 
 
父主题： [LLC相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置LLC参数(SET LLC PARAMETER) 
#### 设置LLC参数(SET LLC PARAMETER) 
命令功能 
该命令用于设置LLC参数。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
PDULIFE|LLC PDU生存期(10毫秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该安全变量用于设置LLC分组消息数据单元的生存周期，单位为10ms。当为某个LLC消息数据单元分配数据区时开始计时，超过该配置时间则将分配的数据区释放。
命令举例 
设置LLC参数，LLC PDU生存期（毫秒）为1。 
SET LLC PARAMETER:PDULIFE=1; 
父主题： [LLC参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询LLC参数(SHOW LLC PARAMETER) 
#### 查询LLC参数(SHOW LLC PARAMETER) 
命令功能 
该命令用于查询LLC参数。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PDULIFE|LLC PDU生存期(10毫秒)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置LLC分组消息数据单元的生存周期，单位为10ms。当为某个LLC消息数据单元分配数据区时开始计时，超过该配置时间则将分配的数据区释放。
命令举例 
查询LLC参数。 
SHOW LLC PARAMETER; 
`
操作维护  LLC PDU生存期(10毫秒) 
-------------------------------
修改      36863 
-------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [LLC参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### LLC SAPI3参数配置 
### LLC SAPI3参数配置 
背景知识 
协议栈中的逻辑链路控制（LLC Logical Link Control）层协议，类似于国际标准化组织7层参考模型中的第2层（数据链路层）。 
LLC主要作用是在移动台MS和GPRS业务支持节点SGSN的层3的实体之间传送信息。LLC提供通过逻辑连接在MS和SGSN的对等实体之间的消息传送，在实际的GPRS手机协议栈体系结构中，LLC层位于GPRS移动性管理协议层GMM。 
功能描述 
LLC SAPI3参数配置提供LLC SAPI3参数的配置，控制消息超时重传时间，重传的最大次数、帧消息域码流的最大字节数、缓冲区大小等处理。 
相关主题 
 
设置LLC SAPI3参数(SET LLC SAPI3 PARAMETER)
 
 
查询LLC SAPI3参数(SHOW LLC SAPI3 PARAMETER)
 
 
父主题： [LLC相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置LLC SAPI3参数(SET LLC SAPI3 PARAMETER) 
#### 设置LLC SAPI3参数(SET LLC SAPI3 PARAMETER) 
命令功能 
该命令用于设置LLC SAPI3参数。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SAPI3TIMER|SAPI3超时重传时间(0.1秒)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~4095。|该安全变量用于设置SAPI3消息超时重传时间，单位为0.1s。当发送SAPI3消息后，等待该配置时间，如果没有收到响应则发起重传。
SAPI3RETRIES|SAPI3超时重传最大次数（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该安全变量用于设置SAPI3消息超时重传的最大次数，该值不能超过15。当消息重传次数超过该配置值后，消息不再重传。
SAPI3SIZE|SAPI3I帧信息域最大长度(字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:140~1520。|该安全变量用于设置SAPI3 I帧消息域码流的最大字节数。
SAPI3UUI|SAPI3U帧，UI帧信息域最大长度(字节)|参数可选性:任选参数；参数类型:整数；参数范围为:140~1520。|该安全变量用于设置SAPI3 U帧/UI帧消息域码流的最大字节数。
SAPI3DLBUF|SAPI3下行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:0~24320。|该安全变量用于设置SAPI3下行I帧消息缓冲区大小，以16字节为单位。
SAPI3ULBUF|SAPI3上行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:0~24320。|该安全变量用于设置SAPI3上行I帧消息缓冲区大小，以16字节为单位。
SAPI3DLWINDOW|SAPI3下行窗口大小（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该安全变量用于设置SAPI3消息下行窗口大小。
SAPI3ULWINDOW|SAPI3上行窗口大小（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该安全变量用于设置SAPI3消息上行窗口大小。
命令举例 
设置LLC SAPI3参数，SAPI3超时重传时间（0.1秒）为50，SAPI3超时重传最大次数为3，SAPI3I帧信息域最大长度（字节）为1503，SAPI3U帧，UI帧信息域最大长度（字节）为500，SAPI3下行I帧缓冲区大小（16字节）为1250，SAPI3上行I帧缓冲区大小（16字节）为1250，SAPI3下行窗口大小为16，SAPI3上行窗口大小为16。 
SET LLC SAPI3 PARAMETER:SAPI3TIMER=50,SAPI3RETRIES=3,SAPI3SIZE=1053,SAPI3UUI=500,SAPI3DLBUF=1520,SAPI3ULBUF=1520,SAPI3DLWINDOW=16,SAPI3ULWINDOW=16; 
父主题： [LLC SAPI3参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询LLC SAPI3参数(SHOW LLC SAPI3 PARAMETER) 
#### 查询LLC SAPI3参数(SHOW LLC SAPI3 PARAMETER) 
命令功能 
该命令用于查询LLC SAPI3参数。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SAPI3TIMER|SAPI3超时重传时间(0.1秒)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI3消息超时重传时间，单位为0.1s。当发送SAPI3消息后，等待该配置时间，如果没有收到响应则发起重传。
SAPI3RETRIES|SAPI3超时重传最大次数（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI3消息超时重传的最大次数，该值不能超过15。当消息重传次数超过该配置值后，消息不再重传。
SAPI3SIZE|SAPI3I帧信息域最大长度(字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI3 I帧消息域码流的最大字节数。
SAPI3UUI|SAPI3U帧，UI帧信息域最大长度(字节)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI3 U帧/UI帧消息域码流的最大字节数。
SAPI3DLBUF|SAPI3下行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI3下行I帧消息缓冲区大小，以16字节为单位。
SAPI3ULBUF|SAPI3上行I帧缓冲区大小(16字节（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI3上行I帧消息缓冲区大小，以16字节为单位。
SAPI3DLWINDOW|SAPI3下行窗口大小（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI3消息下行窗口大小。
SAPI3ULWINDOW|SAPI3上行窗口大小（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI3消息上行窗口大小。
命令举例 
查询LLC SAPI3参数。 
SHOW LLC SAPI3 PARAMETER; 
`
操作维护  SAPI3超时重传时间(0.1秒)（保留）   SAPI3超时重传最大次数（保留）  SAPI3I帧信息域最大长度(字节)（保留） SAPI3U帧，UI帧信息域最大长度(字节) SAPI3下行I帧缓冲区大小(16字节)（保留） SAPI3上行I帧缓冲区大小(16字节（保留） SAPI3下行窗口大小（保留）    SAPI3上行窗口大小（保留） 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      50                                 3                              1503                                 500                                 1520                                   1520                                  16                          16 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [LLC SAPI3参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### LLC SAPI5参数配置 
### LLC SAPI5参数配置 
背景知识 
协议栈中的逻辑链路控制（LLC Logical Link Control）层协议，类似于国际标准化组织7层参考模型中的第2层（数据链路层）。 
LLC主要作用是在移动台MS和GPRS业务支持节点SGSN的层3的实体之间传送信息。LLC提供通过逻辑连接在MS和SGSN的对等实体之间的消息传送，在实际的GPRS手机协议栈体系结构中，LLC层位于GPRS移动性管理协议层GMM。 
功能描述 
LLC SAP5参数配置提供LLC SAPI5参数的配置，控制消息超时重传时间，重传的最大次数、帧消息域码流的最大字节数、缓冲区大小等处理。 
相关主题 
 
设置LLC SAPI5参数(SET LLC SAPI5 PARAMETER)
 
 
查询LLC SAPI5参数(SHOW LLC SAPI5 PARAMETER)
 
 
父主题： [LLC相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置LLC SAPI5参数(SET LLC SAPI5 PARAMETER) 
#### 设置LLC SAPI5参数(SET LLC SAPI5 PARAMETER) 
命令功能 
该命令用于设置LLC SAPI5参数。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SAPI5TIMER|SAPI5超时重传时间(0.1秒)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~4095。|该安全变量用于设置SAPI5消息超时重传时间，单位为0.1s。当发送SAPI5消息后，等待该配置时间，如果没有收到响应则发起重传。
SAPI5RETRIES|SAPI5超时重传最大次数（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该安全变量用于设置SAPI5消息超时重传的最大次数，该值不能超过15。当消息重传次数超过该配置值后，消息不再重传。
SAPI5SIZE|SAPI5I帧信息域最大长度(字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:140~1520。|该安全变量用于设置SAPI5 I帧消息域码流的最大字节数。
SAPI5UUI|SAPI5U帧，UI帧信息域最大长度(字节)|参数可选性:任选参数；参数类型:整数；参数范围为:140~1520。|该安全变量用于设置SAPI5 U帧/UI帧消息域码流的最大字节数。
SAPI5DLBUF|SAPI5下行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:0~24320。|该安全变量用于设置SAPI5下行I帧消息缓冲区大小，以16字节为单位。
SAPI5ULBUF|SAPI5上行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:0~24320。|该安全变量用于设置SAPI5上行I帧消息缓冲区大小，以16字节为单位。
SAPI5DLWINDOW|SAPI5下行窗口大小（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该安全变量用于设置SAPI5消息下行窗口大小。
SAPI5ULWINDOW|SAPI5上行窗口大小（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该安全变量用于设置SAPI5消息上行窗口大小。
命令举例 
设置LLC SAPI5参数，SAPI5超时重传时间（0.1秒）为100，SAPI5超时重传最大次数为3，SAPI5I帧信息域最大长度（字节）为1503，SAPI5U帧，UI帧信息域最大长度（字节）为500，SAPI5下行I帧缓冲区大小（16字节）为760，SAPI5上行I帧缓冲区大小（16字节）为760，SAPI5下行窗口大小为8，SAPI5上行窗口大小为8。 
SET LLC SAPI5 PARAMETER:SAPI5TIMER=100,SAPI5RETRIES=3,SAPI5SIZE=1503,SAPI5UUI=500,SAPI5DLBUF=760,SAPI5ULBUF=760,SAPI5DLWINDOW=8,SAPI5ULWINDOW=8; 
父主题： [LLC SAPI5参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询LLC SAPI5参数(SHOW LLC SAPI5 PARAMETER) 
#### 查询LLC SAPI5参数(SHOW LLC SAPI5 PARAMETER) 
命令功能 
该命令用于查询LLC SAPI5参数。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SAPI5TIMER|SAPI5超时重传时间(0.1秒)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI5消息超时重传时间，单位为0.1s。当发送SAPI5消息后，等待该配置时间，如果没有收到响应则发起重传。
SAPI5RETRIES|SAPI5超时重传最大次数（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI5消息超时重传的最大次数，该值不能超过15。当消息重传次数超过该配置值后，消息不再重传。
SAPI5SIZE|SAPI5I帧信息域最大长度(字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI5 I帧消息域码流的最大字节数。
SAPI5UUI|SAPI5U帧，UI帧信息域最大长度(字节)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI5 U帧/UI帧消息域码流的最大字节数。
SAPI5DLBUF|SAPI5下行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI5下行I帧消息缓冲区大小，以16字节为单位。
SAPI5ULBUF|SAPI5上行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI5上行I帧消息缓冲区大小，以16字节为单位。
SAPI5DLWINDOW|SAPI5下行窗口大小（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI5消息下行窗口大小。
SAPI5ULWINDOW|SAPI5上行窗口大小（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI5消息上行窗口大小。
命令举例 
查询LLC SAPI5参数。 
SHOW LLC SAPI5 PARAMETER; 
`
操作维护  SAPI5超时重传时间(0.1秒)（保留）    SAPI5超时重传最大次数（保留）  SAPI5I帧信息域最大长度(字节)（保留）   SAPI5U帧，UI帧信息域最大长度(字节)   SAPI5下行I帧缓冲区大小(16字节)（保留）   SAPI5上行I帧缓冲区大小(16字节)（保留）  SAPI5下行窗口大小（保留）  SAPI5上行窗口大小（保留） 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      100                                 3                               1503                                   500                                  760                                     760                                      8                         8 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [LLC SAPI5参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### LLC SAPI9参数配置 
### LLC SAPI9参数配置 
背景知识 
协议栈中的逻辑链路控制（LLC Logical Link Control）层协议，类似于国际标准化组织7层参考模型中的第2层（数据链路层）。 
LLC主要作用是在移动台MS和GPRS业务支持节点SGSN的层3的实体之间传送信息。LLC提供通过逻辑连接在MS和SGSN的对等实体之间的消息传送，在实际的GPRS手机协议栈体系结构中，LLC层位于GPRS移动性管理协议层GMM。 
功能描述 
LLC SAP9参数配置提供LLC SAPI9参数的配置，控制消息超时重传时间，重传的最大次数、帧消息域码流的最大字节数、缓冲区大小等处理。 
相关主题 
 
设置LLC SAPI9参数(SET LLC SAPI9 PARAMETER)
 
 
查询LLC SAPI9参数(SHOW LLC SAPI9 PARAMETER)
 
 
父主题： [LLC相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置LLC SAPI9参数(SET LLC SAPI9 PARAMETER) 
#### 设置LLC SAPI9参数(SET LLC SAPI9 PARAMETER) 
命令功能 
该命令用于设置LLC SAPI9参数。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SAPI9TIMER|SAPI9超时重传时间(0.1秒)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~4095。|该安全变量用于设置SAPI9消息超时重传时间，单位为0.1s。当发送SAPI9消息后，等待该配置时间，如果没有收到响应则发起重传。
SAPI9RETRIES|SAPI9超时重传最大次数（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该安全变量用于设置SAPI9消息超时重传的最大次数，该值不能超过15。当消息重传次数超过该配置值后，消息不再重传。
SAPI9SIZE|SAPI9I帧信息域最大长度(字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:140~1520。|该安全变量用于设置SAPI9 I帧消息域码流的最大字节数。
SAPI9UUI|SAPI9U帧，UI帧信息域最大长度(字节)|参数可选性:任选参数；参数类型:整数；参数范围为:140~1520。|该安全变量用于设置SAPI9 U帧/UI帧消息域码流的最大字节数。
SAPI9DLBUF|SAPI9下行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:0~24320。|该安全变量用于设置SAPI9下行I帧消息缓冲区大小，以16字节为单位。
SAPI9ULBUF|SAPI9上行I帧缓冲区大小(16字节（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:0~24320。|该安全变量用于设置SAPI9上行I帧消息缓冲区大小，以16字节为单位。
SAPI9DLWINDOW|SAPI9下行窗口大小（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该安全变量用于设置SAPI9消息下行窗口大小。
SAPI9ULWINDOW|SAPI9上行窗口大小（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该安全变量用于设置SAPI9消息上行窗口大小。
命令举例 
设置LLC SAPI9参数，SAPI9超时重传时间（0.1秒）为200，SAPI9超时重传最大次数为3，SAPI9I帧信息域最大长度(字节）为1503，SAPI9U帧，UI帧信息域最大长度（字节）为500，SAPI9下行I帧缓冲区大小（16字节）为380，SAPI9上行I帧缓冲区大小（16字节）为380，SAPI9下行窗口大小为4，SAPI9上行窗口大小为4。 
SET LLC SAPI9 PARAMETER:SAPI9TIMER=200,SAPI9RETRIES=3,SAPI9SIZE=1503,SAPI9UUI=500,SAPI9DLBUF=380,SAPI9ULBUF=380,SAPI9DLWINDOW=4,SAPI9ULWINDOW=4; 
父主题： [LLC SAPI9参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询LLC SAPI9参数(SHOW LLC SAPI9 PARAMETER) 
#### 查询LLC SAPI9参数(SHOW LLC SAPI9 PARAMETER) 
命令功能 
该命令用于查询LLC SAPI9参数。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SAPI9TIMER|SAPI9超时重传时间(0.1秒)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI9消息超时重传时间，单位为0.1s。当发送SAPI9消息后，等待该配置时间，如果没有收到响应则发起重传。
SAPI9RETRIES|SAPI9超时重传最大次数（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI9消息超时重传的最大次数，该值不能超过15。当消息重传次数超过该配置值后，消息不再重传。
SAPI9SIZE|SAPI9I帧信息域最大长度(字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI9 I帧消息域码流的最大字节数。
SAPI9UUI|SAPI9U帧，UI帧信息域最大长度(字节)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI9 U帧/UI帧消息域码流的最大字节数。
SAPI9DLBUF|SAPI9下行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI9下行I帧消息缓冲区大小，以16字节为单位。
SAPI9ULBUF|SAPI9上行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI9上行I帧消息缓冲区大小，以16字节为单位。
SAPI9DLWINDOW|SAPI9下行窗口大小（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI9消息下行窗口大小。
SAPI9ULWINDOW|SAPI9上行窗口大小（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI9消息上行窗口大小。
命令举例 
查询LLC SAPI9参数。 
SHOW LLC SAPI9 PARAMETER; 
`
操作维护   SAPI9超时重传时间(0.1秒)（保留）  SAPI9超时重传最大次数（保留）  SAPI9I帧信息域最大长度(字节)（保留） SAPI9U帧，UI帧信息域最大长度(字节)   SAPI9下行I帧缓冲区大小(16字节)（保留）  SAPI9上行I帧缓冲区大小(16字节)（保留）  SAPI9下行窗口大小（保留）   SAPI9上行窗口大小（保留） 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改       200                               3                              1503                                  500                                 380                                     380                                      4                          4 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [LLC SAPI9参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### LLC SAPI11参数配置 
### LLC SAPI11参数配置 
背景知识 
协议栈中的逻辑链路控制（LLC Logical Link Control）层协议，类似于国际标准化组织7层参考模型中的第2层（数据链路层）。 
LLC主要作用是在移动台MS和GPRS业务支持节点SGSN的层3的实体之间传送信息。LLC提供通过逻辑连接在MS和SGSN的对等实体之间的消息传送，在实际的GPRS手机协议栈体系结构中，LLC层位于GPRS移动性管理协议层GMM。 
功能描述 
LLC SAPI11参数配置提供LLC SAPI11参数的配置，控制消息超时重传时间，重传的最大次数、帧消息域码流的最大字节数、缓冲区大小等处理。 
相关主题 
 
设置LLC SAPI11参数(SET LLC SAPI11 PARAMETER)
 
 
查询LLC SAPI11参数(SHOW LLC SAPI11 PARAMETER)
 
 
父主题： [LLC相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置LLC SAPI11参数(SET LLC SAPI11 PARAMETER) 
#### 设置LLC SAPI11参数(SET LLC SAPI11 PARAMETER) 
命令功能 
该命令用于设置LLC SAPI11参数。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SAPI11TIMER|SAPI11超时重传时间(0.1秒)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~4095。|该安全变量用于设置SAPI11消息超时重传时间，单位为0.1s。当发送SAPI11消息后，等待该配置时间，如果没有收到响应则发起重传。
SAPI11RETRIES|SAPI11超时重传最大次数（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~15。|该安全变量用于设置SAPI11消息超时重传的最大次数，该值不能超过15。当消息重传次数超过该配置值后，消息不再重传。
SAPI11SIZE|SAPI11I帧信息域最大长度(字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:140~1520。|该安全变量用于设置SAPI11 I帧消息域码流的最大字节数。
SAPI11UUI|SAPI11U帧，UI帧信息域最大长度(字节)|参数可选性:任选参数；参数类型:整数；参数范围为:140~1520。|该安全变量用于设置SAPI11 U帧/UI帧消息域码流的最大字节数。
SAPI11DLBUF|SAPI11下行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:0~24320。|该安全变量用于设置SAPI11下行I帧消息缓冲区大小，以16字节为单位。
SAPI11ULBUF|SAPI11上行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:0~24320。|该安全变量用于设置SAPI11上行I帧消息缓冲区大小，以16字节为单位。
SAPI11DLWINDOW|SAPI11下行窗口大小（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该安全变量用于设置SAPI11消息下行窗口大小。
SAPI11ULWINDOW|SAPI11上行窗口大小（保留）|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该安全变量用于设置SAPI11消息上行窗口大小。
命令举例 
设置LLC SAPI11参数，SAPI11超时重传时间（0.1秒）为400，SAPI11超时重传最大次数为3，SAPI11I帧信息域最大长度（字节）为1503，SAPI11U帧，UI帧信息域最大长度（字节）为500，SAPI11下行I帧缓冲区大小（16字节）为190，SAPI11上行I帧缓冲区大小（16字节）为190，SAPI11下行窗口大小为2，SAPI11上行窗口大小为2。 
SET LLC SAPI11 PARAMETER:SAPI11TIMER=400,SAPI11RETRIES=3,SAPI11SIZE=1503,SAPI11UUI=500,SAPI11DLBUF=190,SAPI11ULBUF=190,SAPI11DLWINDOW=2,SAPI11ULWINDOW=2; 
父主题： [LLC SAPI11参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询LLC SAPI11参数(SHOW LLC SAPI11 PARAMETER) 
#### 查询LLC SAPI11参数(SHOW LLC SAPI11 PARAMETER) 
命令功能 
该命令用于查询LLC SAPI11参数。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SAPI11TIMER|SAPI11超时重传时间(0.1秒)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI11消息超时重传时间，单位为0.1s。当发送SAPI11消息后，等待该配置时间，如果没有收到响应则发起重传。
SAPI11RETRIES|SAPI11超时重传最大次数（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI11消息超时重传的最大次数，该值不能超过15。当消息重传次数超过该配置值后，消息不再重传。
SAPI11SIZE|SAPI11I帧信息域最大长度(字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI11 I帧消息域码流的最大字节数。
SAPI11UUI|SAPI11U帧，UI帧信息域最大长度(字节)|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI11 U帧/UI帧消息域码流的最大字节数。
SAPI11DLBUF|SAPI11下行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI11下行I帧消息缓冲区大小，以16字节为单位。
SAPI11ULBUF|SAPI11上行I帧缓冲区大小(16字节)（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI11上行I帧消息缓冲区大小，以16字节为单位。
SAPI11DLWINDOW|SAPI11下行窗口大小（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI11消息下行窗口大小。
SAPI11ULWINDOW|SAPI11上行窗口大小（保留）|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SAPI11消息上行窗口大小。
命令举例 
查询LLC SAPI11参数。 
SHOW LLC SAPI11 PARAMETER; 
`
操作维护  SAPI11超时重传时间(0.1秒)（保留） SAPI11超时重传最大次数（保留） SAPI11I帧信息域最大长度(字节)（保留）  SAPI11U帧，UI帧信息域最大长度(字节)     SAPI11下行I帧缓冲区大小(16字节)（保留）  SAPI11上行I帧缓冲区大小(16字节)（保留）   SAPI11下行窗口大小（保留） SAPI11上行窗口大小（保留） 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      400                               3                               1503                                  500                                     190                                       190                                      2                           2 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [LLC SAPI11参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 安全相关配置 
## 安全相关配置 
背景知识 
移动通信是我们现代生活中不可缺少的一部分，大家对通信中的信息安全也提出了更高的要求。 
移动通讯的安全措施发展分为以下几个阶段： 
 
第一代模拟移动通信系统（1G）只能进行语音通话，几乎没有采取安全措施，它采用简单的电子序列号作为确认手段。安全性比较低。
 
 
第二代移动通信（2G）增加接收数据功能，主要有时分多址（TDMA）的GSM系统、DAMPS系统及基于码分多址（TDMA）的CDMA系统，它们都是基于私钥密码体制，这种密钥被窃取的难度大，安全性得到大幅提升。但身份认证及加密算法存在着许多隐患。
 
 
第三代移动通信技术（3G）,相对于第一代模拟技术和第二代GSM、CDMA等技术而言，提供语音和数据业务，对安全性要求提高，采用对称密钥实现数据加密、数据源认证、数据完整性保护来进行安全保护。
 
 
LTE网络数据业务快速发展，对数据安全要求更高，为了避免攻击者在空中接口上伪造和重发来窃取安全信息，分析LTE中密钥体系和安全性架构，在对安全模式命令进行研究的基础上，LTE实行加密和完整性保护的实现方案，并通过基于AES核心算法仿真实现。安全机制将为分组业务提供更可靠的安全保证。 
功能描述 
安全相关的配置中提供了如下和安全相关的功能配置： 
 
配置安全参数。
 
 
配置UMTS AS加密控制参数。
 
 
配置EPC NAS加密控制参数。
 
 
配置UMTS AS完整性保护参数。
 
 
配置EPC NAS完整性保护参数。
 
 
配置GPRS加密参数。
 
 
相关主题 
 
安全参数配置
 
 
UMTS AS加密控制参数配置
 
 
EPC NAS加密控制参数配置
 
 
UMTS AS完整性保护参数配置
 
 
EPC NAS完整性保护参数配置
 
 
GPRS加密参数配置
 
 
父主题： [安全变量]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 安全参数配置 
### 安全参数配置 
背景知识 
对于移动性管理相关的流程，MME/SGSN会根据协议（3GPP-23401-950 “5.3.10 Security Function”/3GPP-23060-900 “6.8 Security Function”）的要求对用户进行鉴权、加密和IMEI检查。运营商也可以配置自己的鉴权、加密和IMEI检查策略。 
功能描述 
当运营商需要配置自己的鉴权、加密和IMEI检查策略时需要使用该配置。该配置可以实现如下功能： 
 
控制MME/SGSN每次向HSS/HLR请求的鉴权向量组数。
 
 
控制MME是否需要对用户进行IMEI检查。
 
 
控制MME获取用户的IMEI/IMEISV失败时，或者对用户进行IMEI检查失败时，MME的处理方式。
 
 
控制SGSN对于移动性管理流程（附着/路由区更新/去附着/业务请求/Gb口短消息呼出/Gb口短消息呼入/Gb口激活PDP/Gb口去活PDP）的鉴权和加密策略。
 
 
控制SGSN是否支持基于IMEI配置Gb口的加密算法。
 
 
控制SGSN不支持用户的GPRS加密算法时，是否拒绝用户接入。
 
 
相关主题 
 
设置安全参数(SET SECURITY PARAMETER)
 
 
查询安全参数(SHOW SECURITY PARAMETER)
 
 
父主题： [安全相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置安全参数(SET SECURITY PARAMETER) 
#### 设置安全参数(SET SECURITY PARAMETER) 
命令功能 
该命令用于设置安全参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
AUTHSEG|SGSN允许sendAuthInfo操作分段|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持SGSN允许sendAuthInfo操作分段，取值含义如下：不支持：表示SGSN不允许sendAuthInfo操作分段。支持：表示SGSN允许sendAuthInfo操作分段。
AUTHNUM|SGSN鉴权组数|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该安全变量用于设置SGSN向HLR获取鉴权向量的组数，取值范围为1~5。
AUTHONATTACH|SGSN附着时鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN附着时鉴权的类型，取值含义如下：不鉴权：表示用户附着时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户附着时SGSN每次都会对用户进行鉴权。系统判断：表示用户附着时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。按频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
AUTHONRAUPDT|SGSN路由更新时鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN路由更新时鉴权的类型，取值含义如下：不鉴权：表示用户路由更新时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户路由更新时SGSN每次都会对用户进行鉴权。系统判断：表示用户路由更新时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。按频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
SGSNAUTHONDETACH|SGSN去附着时鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN去附着时鉴权的类型，取值含义如下：不鉴权：表示用户去附着时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户去附着时SGSN每次都会对用户进行鉴权。系统判断：表示用户去附着时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。
AUTHSMSOUT|GnGp SGSN Gb口短消息呼出鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置GnGp SGSN Gb口短消息呼出鉴权的类型，取值含义如下：不鉴权：表示用户Gb口短消息呼出时GnGp SGSN始终不会对用户进行鉴权。强制鉴权：表示用户Gb口短消息呼出时GnGp SGSN每次都会对用户进行鉴权。系统判断：表示用户Gb口短消息呼出时GnGp SGSN是否对用户进行鉴权取决于UE和GnGp SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
AUTHSMSIN|GnGp SGSN Gb口短消息呼入鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置GnGp SGSN Gb口短消息呼入鉴权的类型，取值含义如下：不鉴权：表示用户Gb口短消息呼入时GnGp SGSN始终不会对用户进行鉴权。强制鉴权：表示用户Gb口短消息呼入时GnGp SGSN每次都会对用户进行鉴权。系统判断：表示用户Gb口短消息呼入时GnGp SGSN是否对用户进行鉴权取决于UE和GnGp SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
AUTHONACTPDP|SGSN Gb口激活PDP鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN Gb口激活PDP鉴权的类型，取值含义如下：不鉴权：表示用户Gb口激活PDP时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户Gb口激活PDP时SGSN每次都会对用户进行鉴权。系统判断：表示用户Gb口激活PDP时SGSN是否对用户进行鉴权取决于UE和GnGp SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
AUTHONDEACTPDP|SGSN Gb口去活PDP鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN Gb口去活PDP鉴权的类型，取值含义如下：不鉴权：表示用户Gb口去活PDP时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户Gb口去活PDP时SGSN每次都会对用户进行鉴权。系统判断：表示用户Gb口去活PDP时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。
SGSNAUTHONSVC|SGSN业务请求时鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN业务请求时鉴权的类型，取值含义如下：不鉴权：表示业务请求时SGSN始终不会对用户进行鉴权。强制鉴权：表示业务请求时SGSN每次都会对用户进行鉴权。系统判断：表示业务请求时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。按频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
REJATTACHIFNOGEA|SGSN不支持手机GPRS加密算法拒绝接入|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN不支持手机GPRS加密算法是否拒绝接入，取值含义如下：否：表示SGSN不支持手机GPRS加密算法时不拒绝接入。是：表示SGSN不支持手机GPRS加密算法时拒绝接入。
EUTRANAuthNum|MME请求的E-UTRAN鉴权组数|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该安全变量用于设置MME每次向HSS请求鉴权向量（Number of requested E-UTRAN vectors）时，期望HSS返回的鉴权向量组数。建议使用系统默认值5。该值的大小会决定MME向HSS请求鉴权向量的频率。例如，该值设置为1，则MME每次要对用户进行鉴权时，都会向HSS请求鉴权向量，这会增加MME和HSS之间的信令交互。
MMECHECKIMEI|MME IMEI检查控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置用户发起ATTACH/TAU流程时，MME是否需要对用户进行IMEI检查，以便判定终端是否合法。当设置为“需要”时，需要同时新增如下配置：配置MME获取IMEI/IMEISV的方式：例如，执行命令SET MOBILE MANAGEMENT:MMEGETIMEI="Get IMEI";配置MME支持S13接口：例如，执行命令SET COMBOCFG:SUPTYPE="S13";配置MME对接的EIR网元的局向：例如，执行命令ADD DIAMEIR:GRPID=1;配置对指定类型的ATTACH/TAU流程进行IMEI检查（对应软件参数ID为327820）：例如，执行命令SET SOFTWARE PARAMETER:PARAID=327820,PARAVALUE=1;
MMEFAILIMEI|MME IMEI获取或检查失败处理控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置当MME获取用户的IMEI/IMEISV失败时，或者检查用户的IMEI失败时，MME是继续执行当前流程还是终止当前流程。
SGSNINTERRAUAUTH|SGSN局间切换后的RAU鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN局间切换后的RAU鉴权的类型，取值含义如下：不鉴权：表示局间切换后的RAU时SGSN始终不会对用户进行鉴权。强制鉴权：表示局间切换后的RAU时SGSN每次都会对用户进行鉴权。系统判断：表示局间切换后的RAU时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。
GEABASEDONIMEI|是否支持基于IMEI配置Gb加密算法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持基于IMEI配置Gb加密算法，取值含义如下：不支持：表示SGSN不支持基于IMEI配置Gb加密算法。支持：表示SGSN支持基于IMEI配置Gb加密算法。
命令举例 
[MME]:设置安全变量，MME IMSI附着时鉴权控制为系统判断，MME IMSI附着时鉴权控制频次为2，MME局内GUTI附着时鉴权控制为系统判断，MME局内GUTI附着时鉴权控制频次为2，MME局间附着时鉴权控制为系统判断，MME局间附着时鉴权控制频次为2，MME EPC TAU时鉴权为系统判断，MME EPC TAU时鉴权频次为2，MME业务请求时鉴权为系统判断，MME业务请求时鉴权频次为2，MME Detach时鉴权为强制不健全，MME Detach时鉴权频次为2，MME请求的E-UTRAN鉴权组数为1。
[GnGp SGSN]：设置安全变量，SGSN允许sendAuthInfo操作分段为支持，SGSN鉴权组数为1，SGSN Attach时鉴权为按照频次鉴权，SGSN路由更新时鉴权为按照频次鉴权，SGSN Detach时鉴权为不鉴权，GnGp SGSN Gb口短消息呼出鉴权为系统判断，GnGp SGSN Gb口短消息呼入鉴权为系统判断，SGSN Gb口激活PDP鉴权为强制鉴权，SGSN Gb口去活PDP鉴权为系统判断，SGSN业务请求时鉴权为系统判断，SGSN不支持手机GPRS加密算法拒绝接入为是。 
[MME]SET SECURITY PARAMETER:IMSIATTACHAUTH="System define",IMSIATTACHAUTHNUM=2,INTRAGUTIATTACH="System define",INTRAGUTIATTACHNUM=2,INTERATTACHAUTH="System define",INTERATTACHAUTHNUM=2,AUTHONTAUPDT="System define",AUTHONTAUPDTNUM=2,MMEAUTHONSVC="System define",MMEAUTHONSVCNUM=2,MMEAUTHONDETACH="Forcenot",MMEAUTHONDETACHNUM=2,EUTRANAUTHNUM=1;
[GnGp SGSN]SET SECURITY PARAMETER:AUTHSEG="Support",AUTHNUM=1,AUTHONATTACH="Authentication according to frequency",AUTHONRAUPDT="Authentication according to frequency",SGSNAUTHONDETACH="No authentication",AUTHSMSOUT="System define",AUTHSMSIN="System define",AUTHONACTPDP="Compelling authentication",AUTHONDEACTPDP="System define",SGSNAUTHONSVC="System define",REJATTACHIFNOGEA="YES"; 
父主题： [安全参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询安全参数(SHOW SECURITY PARAMETER) 
#### 查询安全参数(SHOW SECURITY PARAMETER) 
命令功能 
该命令用于查询安全参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
AUTHSEG|SGSN允许sendAuthInfo操作分段|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持SGSN允许sendAuthInfo操作分段，取值含义如下：不支持：表示SGSN不允许sendAuthInfo操作分段。支持：表示SGSN允许sendAuthInfo操作分段。
AUTHNUM|SGSN鉴权组数|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置SGSN向HLR获取鉴权向量的组数，取值范围为1~5。
AUTHONATTACH|SGSN附着时鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN附着时鉴权的类型，取值含义如下：不鉴权：表示用户附着时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户附着时SGSN每次都会对用户进行鉴权。系统判断：表示用户附着时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。按频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
AUTHONRAUPDT|SGSN路由更新时鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN路由更新时鉴权的类型，取值含义如下：不鉴权：表示用户路由更新时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户路由更新时SGSN每次都会对用户进行鉴权。系统判断：表示用户路由更新时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。按频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
SGSNAUTHONDETACH|SGSN去附着时鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN去附着时鉴权的类型，取值含义如下：不鉴权：表示用户去附着时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户去附着时SGSN每次都会对用户进行鉴权。系统判断：表示用户去附着时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。
AUTHSMSOUT|GnGp SGSN Gb口短消息呼出鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置GnGp SGSN Gb口短消息呼出鉴权的类型，取值含义如下：不鉴权：表示用户Gb口短消息呼出时GnGp SGSN始终不会对用户进行鉴权。强制鉴权：表示用户Gb口短消息呼出时GnGp SGSN每次都会对用户进行鉴权。系统判断：表示用户Gb口短消息呼出时GnGp SGSN是否对用户进行鉴权取决于UE和GnGp SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
AUTHSMSIN|GnGp SGSN Gb口短消息呼入鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置GnGp SGSN Gb口短消息呼入鉴权的类型，取值含义如下：不鉴权：表示用户Gb口短消息呼入时GnGp SGSN始终不会对用户进行鉴权。强制鉴权：表示用户Gb口短消息呼入时GnGp SGSN每次都会对用户进行鉴权。系统判断：表示用户Gb口短消息呼入时GnGp SGSN是否对用户进行鉴权取决于UE和GnGp SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
AUTHONACTPDP|SGSN Gb口激活PDP鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN Gb口激活PDP鉴权的类型，取值含义如下：不鉴权：表示用户Gb口激活PDP时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户Gb口激活PDP时SGSN每次都会对用户进行鉴权。系统判断：表示用户Gb口激活PDP时SGSN是否对用户进行鉴权取决于UE和GnGp SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
AUTHONDEACTPDP|SGSN Gb口去活PDP鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN Gb口去活PDP鉴权的类型，取值含义如下：不鉴权：表示用户Gb口去活PDP时SGSN始终不会对用户进行鉴权。强制鉴权：表示用户Gb口去活PDP时SGSN每次都会对用户进行鉴权。系统判断：表示用户Gb口去活PDP时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。
SGSNAUTHONSVC|SGSN业务请求时鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN业务请求时鉴权的类型，取值含义如下：不鉴权：表示业务请求时SGSN始终不会对用户进行鉴权。强制鉴权：表示业务请求时SGSN每次都会对用户进行鉴权。系统判断：表示业务请求时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。按频次鉴权：SGSN检查UE和SGSN之间的安全上下文是否破坏：如果破坏，则SGSN对本用户本业务类型流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。如果没有破坏，SGSN进一步检查：该用户本业务类型流程未鉴权累计次数是否达到IMSI号段配置的鉴权频次数。如果没有达到，则SGSN对该用户的本流程未鉴权累计次数加1，在本业务类型流程中SGSN对UE不进行鉴权。如果达到，则SGSN对该用户的本流程未鉴权累计次数清除成0，在本业务类型流程中SGSN对UE进行鉴权。
REJATTACHIFNOGEA|SGSN不支持手机GPRS加密算法拒绝接入|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN不支持手机GPRS加密算法是否拒绝接入，取值含义如下：否：表示SGSN不支持手机GPRS加密算法时不拒绝接入。是：表示SGSN不支持手机GPRS加密算法时拒绝接入。
EUTRANAuthNum|MME请求的E-UTRAN鉴权组数|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置MME每次向HSS请求鉴权向量（Number of requested E-UTRAN vectors）时，期望HSS返回的鉴权向量组数。建议使用系统默认值5。该值的大小会决定MME向HSS请求鉴权向量的频率。例如，该值设置为1，则MME每次要对用户进行鉴权时，都会向HSS请求鉴权向量，这会增加MME和HSS之间的信令交互。
MMECHECKIMEI|MME IMEI检查控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置用户发起ATTACH/TAU流程时，MME是否需要对用户进行IMEI检查，以便判定终端是否合法。当设置为“需要”时，需要同时新增如下配置：配置MME获取IMEI/IMEISV的方式：例如，执行命令SET MOBILE MANAGEMENT:MMEGETIMEI="Get IMEI";配置MME支持S13接口：例如，执行命令SET COMBOCFG:SUPTYPE="S13";配置MME对接的EIR网元的局向：例如，执行命令ADD DIAMEIR:GRPID=1;配置对指定类型的ATTACH/TAU流程进行IMEI检查（对应软件参数ID为327820）：例如，执行命令SET SOFTWARE PARAMETER:PARAID=327820,PARAVALUE=1;
MMEFAILIMEI|MME IMEI获取或检查失败处理控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置当MME获取用户的IMEI/IMEISV失败时，或者检查用户的IMEI失败时，MME是继续执行当前流程还是终止当前流程。
SGSNINTERRAUAUTH|SGSN局间切换后的RAU鉴权|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置SGSN局间切换后的RAU鉴权的类型，取值含义如下：不鉴权：表示局间切换后的RAU时SGSN始终不会对用户进行鉴权。强制鉴权：表示局间切换后的RAU时SGSN每次都会对用户进行鉴权。系统判断：表示局间切换后的RAU时SGSN是否对用户进行鉴权取决于UE和SGSN之间的安全上下文是否被破坏，如果被破坏，则重新发起鉴权流程，以建立新的安全上下文。如：UE和GnGp SGSN的P-TMSI Signature不同步，CKSN检查失败等等，如果安全上下文被破坏，则对用户进行鉴权，否则，默认不鉴权。
GEABASEDONIMEI|是否支持基于IMEI配置Gb加密算法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持基于IMEI配置Gb加密算法，取值含义如下：不支持：表示SGSN不支持基于IMEI配置Gb加密算法。支持：表示SGSN支持基于IMEI配置Gb加密算法。
命令举例 
查询安全参数。 
SHOW SECURITY PARAMETER; 
`
命令 (No.1): SHOW SECURITY PARAMETER
操作维护  SGSN允许sendAuthInfo操作分段   SGSN鉴权组数   SGSN附着时鉴权   SGSN路由更新时鉴权   SGSN去附着时鉴权   GnGp SGSN Gb口短消息呼出鉴权   GnGp SGSN Gb口短消息呼入鉴权   SGSN Gb口激活PDP鉴权   SGSN Gb口去活PDP鉴权   SGSN业务请求时鉴权   SGSN不支持手机GPRS加密算法拒绝接入   MME请求的E-UTRAN鉴权组数   MME IMEI检查控制   MME IMEI获取或检查失败处理控制   SGSN局间切换后的RAU鉴权   是否支持基于IMEI配置Gb加密算法
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      支持                           5              强制鉴权         系统判断             不鉴权             强制鉴权                       强制鉴权                       不鉴权                 不鉴权                 系统判断             否                                   5                          不需要             流程继续                         不鉴权                    不支持
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.093 秒）。
` 
父主题： [安全参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### UMTS AS加密控制参数配置 
### UMTS AS加密控制参数配置 
背景知识 
当终端接入UMTS网络时，为了保证用户信令和数据的安全，网络需要对用户信令和数据进行加密。 
UMTS AS的加密是一项可选的功能，运营商可以根据自身网络的需求来决定是否开启该功能。 
功能描述 
该配置用于设置是否对UMTS AS信令进行加密。 
在支持UMTS AS信令加密的情况下，可配置支持多种加密算法。SGSN通过Security Mode Command命令将支持的加密算法携带给RNC，由RNC选择具体的加密算法。 
相关主题 
 
设置UMTS AS加密控制参数(SET ENCRYCTRL)
 
 
查询UMTS AS加密控制参数(SHOW ENCRYCTRL)
 
 
父主题： [安全相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置UMTS AS加密控制参数(SET ENCRYCTRL) 
#### 设置UMTS AS加密控制参数(SET ENCRYCTRL) 
命令功能 
该命令用于设置加密控制参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ENCRYPTION|加密控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持加密控制，取值含义如下：不支持：表示不支持UMTS AS加密。支持：表示支持UMTS AS加密，将支持的所有加密算法通过Security Mode Command带给RNC。
ENCRYALGO|支持无加密算法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持无加密算法，取值含义如下：不支持：表示不支持无加密算法。支持：表示支持无加密算法。
ENCRYALGO1|支持加密算法1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法1，取值含义如下：不支持：表示不支持加密算法1。支持：表示支持加密算法1。
ENCRYALGO2|支持加密算法2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法2，取值含义如下：不支持：表示不支持加密算法2。支持：表示支持加密算法2。
ENCRYALGO3|支持加密算法3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法3，取值含义如下：不支持：表示不支持加密算法3。支持：表示支持加密算法3。
ENCRYALGO4|支持加密算法4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法4，取值含义如下：不支持：表示不支持加密算法4。支持：表示支持加密算法4。
ENCRYALGO5|支持加密算法5|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法5，取值含义如下：不支持：表示不支持加密算法5。支持：表示支持加密算法5。
ENCRYALGO6|支持加密算法6|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法6，取值含义如下：不支持：表示不支持加密算法6。支持：表示支持加密算法6。
ENCRYALGO7|支持加密算法7|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法7，取值含义如下：不支持：表示不支持加密算法7。支持：表示支持加密算法7。
ENCRYALGO8|支持加密算法8|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法8，取值含义如下：不支持：表示不支持加密算法8。支持：表示支持加密算法8。
ENCRYALGO9|支持加密算法9|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法9，取值含义如下：不支持：表示不支持加密算法9。支持：表示支持加密算法9。
ENCRYALGO10|支持加密算法10|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法10，取值含义如下：不支持：表示不支持加密算法10。支持：表示支持加密算法10。
ENCRYALGO11|支持加密算法11|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法11，取值含义如下：不支持：表示不支持加密算法11。支持：表示支持加密算法11。
ENCRYALGO12|支持加密算法12|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法12，取值含义如下：不支持：表示不支持加密算法12。支持：表示支持加密算法12。
ENCRYALGO13|支持加密算法13|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法13，取值含义如下：不支持：表示不支持加密算法13。支持：表示支持加密算法13。
ENCRYALGO14|支持加密算法14|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法14，取值含义如下：不支持：表示不支持加密算法14。支持：表示支持加密算法14。
ENCRYALGO15|支持加密算法15|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法15，取值含义如下：不支持：表示不支持加密算法15。支持：表示支持加密算法15。
命令举例 
设置加密控制参数，加密控制为支持，支持无加密算法为支持，支持加密算法1为支持，支持加密算法2为支持。 
SET ENCRYCTRL:ENCRYPTION="Support",ENCRYALGO="Support",ENCRYALGO1="Support",ENCRYALGO2="Support"; 
父主题： [UMTS AS加密控制参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询UMTS AS加密控制参数(SHOW ENCRYCTRL) 
#### 查询UMTS AS加密控制参数(SHOW ENCRYCTRL) 
命令功能 
该命令用于查询加密控制参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ENCRYPTION|加密控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持加密控制，取值含义如下：不支持：表示不支持UMTS AS加密。支持：表示支持UMTS AS加密，将支持的所有加密算法通过Security Mode Command带给RNC。
ENCRYALGO|支持无加密算法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持无加密算法，取值含义如下：不支持：表示不支持无加密算法。支持：表示支持无加密算法。
ENCRYALGO1|支持加密算法1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法1，取值含义如下：不支持：表示不支持加密算法1。支持：表示支持加密算法1。
ENCRYALGO2|支持加密算法2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法2，取值含义如下：不支持：表示不支持加密算法2。支持：表示支持加密算法2。
ENCRYALGO3|支持加密算法3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法3，取值含义如下：不支持：表示不支持加密算法3。支持：表示支持加密算法3。
ENCRYALGO4|支持加密算法4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法4，取值含义如下：不支持：表示不支持加密算法4。支持：表示支持加密算法4。
ENCRYALGO5|支持加密算法5|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法5，取值含义如下：不支持：表示不支持加密算法5。支持：表示支持加密算法5。
ENCRYALGO6|支持加密算法6|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法6，取值含义如下：不支持：表示不支持加密算法6。支持：表示支持加密算法6。
ENCRYALGO7|支持加密算法7|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法7，取值含义如下：不支持：表示不支持加密算法7。支持：表示支持加密算法7。
ENCRYALGO8|支持加密算法8|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法8，取值含义如下：不支持：表示不支持加密算法8。支持：表示支持加密算法8。
ENCRYALGO9|支持加密算法9|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法9，取值含义如下：不支持：表示不支持加密算法9。支持：表示支持加密算法9。
ENCRYALGO10|支持加密算法10|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法10，取值含义如下：不支持：表示不支持加密算法10。支持：表示支持加密算法10。
ENCRYALGO11|支持加密算法11|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法11，取值含义如下：不支持：表示不支持加密算法11。支持：表示支持加密算法11。
ENCRYALGO12|支持加密算法12|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法12，取值含义如下：不支持：表示不支持加密算法12。支持：表示支持加密算法12。
ENCRYALGO13|支持加密算法13|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法13，取值含义如下：不支持：表示不支持加密算法13。支持：表示支持加密算法13。
ENCRYALGO14|支持加密算法14|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法14，取值含义如下：不支持：表示不支持加密算法14。支持：表示支持加密算法14。
ENCRYALGO15|支持加密算法15|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“加密控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持加密算法15，取值含义如下：不支持：表示不支持加密算法15。支持：表示支持加密算法15。
命令举例 
查询加密控制参数。 
SHOW ENCRYCTRL; 
`
操作维护  加密控制  支持无加密算法  支持加密算法1   支持加密算法2   支持加密算法3  支持加密算法4   支持加密算法5  支持加密算法6   支持加密算法7  支持加密算法8  支持加密算法9  支持加密算法10  支持加密算法11  支持加密算法12  支持加密算法13   支持加密算法14   支持加密算法15 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      支持      支持            不支持          不支持          不支持         不支持           不支持        不支持          不支持         不支持         不支持         不支持          不支持          不支持          不支持            不支持          不支持 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [UMTS AS加密控制参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### EPC NAS加密控制参数配置 
### EPC NAS加密控制参数配置 
背景知识 
一般认为，只有放在运营商机房的网元才可完全信任。由于eNodeB处于一个不完全信任区域，为了确保eNodeB和MME之间的NAS信令不会被非法窃听，因此需要对NAS信令进行加密。 
NAS信令的加密是一项可选的功能，运营商可以根据自身网络的需求来决定是否开启该功能。 
功能描述 
该配置用于设置是否对EPC NAS信令进行加密。 
在支持NAS信令加密的情况下，可配置支持多种加密算法和相应算法的优先级，优先级取值越小表示优先级越高。 
MME选择加密算法时，在UE和MME同时支持的加密算法中，选择优先级最高的。如果两种加密算法的优先级相同，则按照EEA0、EEA1、EEA2、EEA3的顺序，优先选择排在前面的加密算法。比如：EEA0和EEA1的优先级相同，则选择EEA0作为加密算法。 
对于加密算法的优先级，建议采用系统默认值。 
相关主题 
 
设置EPC NAS加密控制参数(SET NAS ENCRYCTRL)
 
 
查询EPC NAS加密控制参数(SHOW NAS ENCRYCTRL)
 
 
父主题： [安全相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置EPC NAS加密控制参数(SET NAS ENCRYCTRL) 
#### 设置EPC NAS加密控制参数(SET NAS ENCRYCTRL) 
命令功能 
该命令用于设置EPC NAS加密控制参数。
注意事项 
MME目前支持的算法为NAS加密算法0~NAS加密算法3，按照协议要求其他的加密算法暂时是保留的。
参数说明 
标识|名称|类型|说明
---|---|---|---
ENCRYPTION|NAS加密控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持NAS加密，取值含义如下：不加密：表示不支持NAS加密，直接选择算法EEA0，即空算法。加密：表示支持NAS加密，加密算法根据设置从EEA0~EEA3中选择。
EEA0|EEA0|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“EPC加密”参数设置为“加密”时，该安全变量用于设置MME是否支持NAS加密算法EEA0，取值含义如下：不支持：表示不支持NAS加密算法EEA0。支持：表示支持NAS加密算法EEA0。
EEA1|EEA1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“EPC加密”参数设置为“加密”时，该安全变量用于设置MME是否支持NAS加密算法EEA1，取值含义如下：不支持：表示不支持NAS加密算法EEA1。支持：表示支持NAS加密算法EEA1。
EEA2|EEA2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“EPC加密”参数设置为“加密”时，该安全变量用于设置MME是否支持NAS加密算法EEA2，取值含义如下：不支持：表示不支持NAS加密算法EEA2。支持：表示支持NAS加密算法EEA2。
EEA3|EEA3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“EPC加密”参数设置为“加密”时，该安全变量用于设置MME是否支持NAS加密算法EEA3，取值含义如下：不支持：表示不支持NAS加密算法EEA3。支持：表示支持NAS加密算法EEA3。
PRIORENCRY0|EEA0优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS加密算法EEA0的优先级；取值越小表示EEA0算法的优先级越高。
PRIORENCRY1|EEA1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS加密算法EEA1的优先级；取值越小表示EEA1算法的优先级越高。
PRIORENCRY2|EEA2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS加密算法EEA2的优先级；取值越小表示EEA2算法的优先级越高。
PRIORENCRY3|EEA3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS加密算法EEA3的优先级；取值越小表示EEA3算法的优先级越高。
命令举例 
设置EPC NAS加密控制参数，EPC加密为加密，EEA0为支持，EEA1为支持，EEA0优先级为1，EEA1优先级为2。 
SET NAS ENCRYCTRL:ENCRYPTION="Encrypt",EEA0="Support",EEA1="Support",PRIORENCRY0="1",PRIORENCRY1="2"; 
父主题： [EPC NAS加密控制参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询EPC NAS加密控制参数(SHOW NAS ENCRYCTRL) 
#### 查询EPC NAS加密控制参数(SHOW NAS ENCRYCTRL) 
命令功能 
该命令用于查询EPC NAS加密控制参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ENCRYPTION|NAS加密控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持NAS加密，取值含义如下：不加密：表示不支持NAS加密，直接选择算法EEA0，即空算法。加密：表示支持NAS加密，加密算法根据设置从EEA0~EEA3中选择。
EEA0|EEA0|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“EPC加密”参数设置为“加密”时，该安全变量用于设置MME是否支持NAS加密算法EEA0，取值含义如下：不支持：表示不支持NAS加密算法EEA0。支持：表示支持NAS加密算法EEA0。
EEA1|EEA1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“EPC加密”参数设置为“加密”时，该安全变量用于设置MME是否支持NAS加密算法EEA1，取值含义如下：不支持：表示不支持NAS加密算法EEA1。支持：表示支持NAS加密算法EEA1。
EEA2|EEA2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“EPC加密”参数设置为“加密”时，该安全变量用于设置MME是否支持NAS加密算法EEA2，取值含义如下：不支持：表示不支持NAS加密算法EEA2。支持：表示支持NAS加密算法EEA2。
EEA3|EEA3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“EPC加密”参数设置为“加密”时，该安全变量用于设置MME是否支持NAS加密算法EEA3，取值含义如下：不支持：表示不支持NAS加密算法EEA3。支持：表示支持NAS加密算法EEA3。
PRIORENCRY0|EEA0优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS加密算法EEA0的优先级；取值越小表示EEA0算法的优先级越高。
PRIORENCRY1|EEA1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS加密算法EEA1的优先级；取值越小表示EEA1算法的优先级越高。
PRIORENCRY2|EEA2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS加密算法EEA2的优先级；取值越小表示EEA2算法的优先级越高。
PRIORENCRY3|EEA3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS加密算法EEA3的优先级；取值越小表示EEA3算法的优先级越高。
命令举例 
查询EPC NAS加密控制参数。 
SHOW NAS ENCRYCTRL; 
`
操作维护 NAS加密控制   EEA0   EEA1   EEA2   EEA3    EEA0优先级  EEA1优先级   EEA2优先级   EEA3优先级 
-------------------------------------------------------------------------------------------------------------
修改      加密         支持   支持   支持   不支持   0           1            2           3 
-------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [EPC NAS加密控制参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### UMTS AS完整性保护参数配置 
### UMTS AS完整性保护参数配置 
背景知识 
当终端接入UMTS网络时，为了保证用户信令和数据不被非法篡改，网络需要对用户信令和数据进行完整性保护。 
UMTS AS的完整性保护是一项可选的功能，运营商可以根据自身网络的需求来决定是否开启该功能。 
功能描述 
该配置用于设置是否支持UMTS AS完整性保护。 
在支持UMTS AS完整性保护的情况下，可配置支持多种完整性保护算法。SGSN通过Security Mode Command命令将支持的完整性保护算法携带给RNC，由RNC选择具体的完整性保护算法。 
相关主题 
 
设置UMTS AS完整性保护参数(SET INTEGCTRL)
 
 
查询UMTS AS完整性保护参数(SHOW INTEGCTRL)
 
 
父主题： [安全相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置UMTS AS完整性保护参数(SET INTEGCTRL) 
#### 设置UMTS AS完整性保护参数(SET INTEGCTRL) 
命令功能 
该命令用于设置完整性保护参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
INTEGCTRL|支持完整性控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持UMTS AS完整性保护，取值含义如下：不支持：表示不支持UMTS AS完整性保护。支持：表示支持UMTS AS完整性保护。
INTEGALGO1|支持完整性保护算法1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法1，取值含义如下：不支持：表示不支持完整性保护算法1。支持：表示支持完整性保护算法1。
INTEGALGO2|支持完整性保护算法2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法2，取值含义如下：不支持：表示不支持完整性保护算法2。支持：表示支持完整性保护算法2。
INTEGALGO3|支持完整性保护算法3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法3，取值含义如下：不支持：表示不支持完整性保护算法3。支持：表示支持完整性保护算法3。
INTEGALGO4|支持完整性保护算法4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法4，取值含义如下：不支持：表示不支持完整性保护算法4。支持：表示支持完整性保护算法4。
INTEGALGO5|支持完整性保护算法5|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法5，取值含义如下：不支持：表示不支持完整性保护算法5。支持：表示支持完整性保护算法5。
INTEGALGO6|支持完整性保护算法6|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法6，取值含义如下：不支持：表示不支持完整性保护算法6。支持：表示支持完整性保护算法6。
INTEGALGO7|支持完整性保护算法7|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法7，取值含义如下：不支持：表示不支持完整性保护算法7。支持：表示支持完整性保护算法7。
INTEGALGO8|支持完整性保护算法8|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法8，取值含义如下：不支持：表示不支持完整性保护算法8。支持：表示支持完整性保护算法8。
INTEGALGO9|支持完整性保护算法9|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法9，取值含义如下：不支持：表示不支持完整性保护算法9。支持：表示支持完整性保护算法9。
INTEGALGO10|支持完整性保护算法10|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法10，取值含义如下：不支持：表示不支持完整性保护算法10。支持：表示支持完整性保护算法10。
INTEGALGO11|支持完整性保护算法11|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法11，取值含义如下：不支持：表示不支持完整性保护算法11。支持：表示支持完整性保护算法11。
INTEGALGO12|支持完整性保护算法12|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法12，取值含义如下：不支持：表示不支持完整性保护算法12。支持：表示支持完整性保护算法12。
INTEGALGO13|支持完整性保护算法13|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法13，取值含义如下：不支持：表示不支持完整性保护算法13。支持：表示支持完整性保护算法13。
INTEGALGO14|支持完整性保护算法14|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法14，取值含义如下：不支持：表示不支持完整性保护算法14。支持：表示支持完整性保护算法14。
INTEGALGO15|支持完整性保护算法15|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法15，取值含义如下：不支持：表示不支持完整性保护算法15。支持：表示支持完整性保护算法15。
INTEGALGO16|支持完整性保护算法16|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法16，取值含义如下：不支持：表示不支持完整性保护算法16。支持：表示支持完整性保护算法16。
命令举例 
设置完整性保护参数，支持完整性控制为支持，支持完整性保护算法1为支持，支持完整性保护算法2为支持，支持完整性保护算法3为支持。 
SET INTEGCTRL:INTEGCTRL="Support",INTEGALGO1="Support",INTEGALGO2="Support",INTEGALGO3="Support"; 
父主题： [UMTS AS完整性保护参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询UMTS AS完整性保护参数(SHOW INTEGCTRL) 
#### 查询UMTS AS完整性保护参数(SHOW INTEGCTRL) 
命令功能 
该命令用于查询完整性保护参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
INTEGCTRL|支持完整性控制|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置是否支持UMTS AS完整性保护，取值含义如下：不支持：表示不支持UMTS AS完整性保护。支持：表示支持UMTS AS完整性保护。
INTEGALGO1|支持完整性保护算法1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法1，取值含义如下：不支持：表示不支持完整性保护算法1。支持：表示支持完整性保护算法1。
INTEGALGO2|支持完整性保护算法2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法2，取值含义如下：不支持：表示不支持完整性保护算法2。支持：表示支持完整性保护算法2。
INTEGALGO3|支持完整性保护算法3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法3，取值含义如下：不支持：表示不支持完整性保护算法3。支持：表示支持完整性保护算法3。
INTEGALGO4|支持完整性保护算法4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法4，取值含义如下：不支持：表示不支持完整性保护算法4。支持：表示支持完整性保护算法4。
INTEGALGO5|支持完整性保护算法5|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法5，取值含义如下：不支持：表示不支持完整性保护算法5。支持：表示支持完整性保护算法5。
INTEGALGO6|支持完整性保护算法6|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法6，取值含义如下：不支持：表示不支持完整性保护算法6。支持：表示支持完整性保护算法6。
INTEGALGO7|支持完整性保护算法7|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法7，取值含义如下：不支持：表示不支持完整性保护算法7。支持：表示支持完整性保护算法7。
INTEGALGO8|支持完整性保护算法8|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法8，取值含义如下：不支持：表示不支持完整性保护算法8。支持：表示支持完整性保护算法8。
INTEGALGO9|支持完整性保护算法9|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法9，取值含义如下：不支持：表示不支持完整性保护算法9。支持：表示支持完整性保护算法9。
INTEGALGO10|支持完整性保护算法10|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法10，取值含义如下：不支持：表示不支持完整性保护算法10。支持：表示支持完整性保护算法10。
INTEGALGO11|支持完整性保护算法11|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法11，取值含义如下：不支持：表示不支持完整性保护算法11。支持：表示支持完整性保护算法11。
INTEGALGO12|支持完整性保护算法12|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法12，取值含义如下：不支持：表示不支持完整性保护算法12。支持：表示支持完整性保护算法12。
INTEGALGO13|支持完整性保护算法13|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法13，取值含义如下：不支持：表示不支持完整性保护算法13。支持：表示支持完整性保护算法13。
INTEGALGO14|支持完整性保护算法14|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法14，取值含义如下：不支持：表示不支持完整性保护算法14。支持：表示支持完整性保护算法14。
INTEGALGO15|支持完整性保护算法15|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法15，取值含义如下：不支持：表示不支持完整性保护算法15。支持：表示支持完整性保护算法15。
INTEGALGO16|支持完整性保护算法16|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当“支持完整性控制”参数设置为“支持”时，该安全变量用于设置SGSN是否支持完整性保护算法16，取值含义如下：不支持：表示不支持完整性保护算法16。支持：表示支持完整性保护算法16。
命令举例 
查询完整性保护参数。 
SHOW INTEGCTRL; 
`
操作维护 支持完整性控制   支持完整性保护算法1    支持完整性保护算法2   支持完整性保护算法3   支持完整性保护算法4   支持完整性保护算法5  支持完整性保护算法6   支持完整性保护算法7   支持完整性保护算法8   支持完整性保护算法9   支持完整性保护算法10   支持完整性保护算法11   支持完整性保护算法12  支持完整性保护算法13  支持完整性保护算法14   支持完整性保护算法15  支持完整性保护算法16 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改     支持             支持                   不支持                不支持                 不支持               不支持               不支持                不支持                 不支持               不支持                不支持                  不支持                不支持                 不支持               不支持                 不支持                不支持 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [UMTS AS完整性保护参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### EPC NAS完整性保护参数配置 
### EPC NAS完整性保护参数配置 
背景知识 
一般认为，只有放在运营商机房的网元才可完全信任。由于eNodeB处于一个不完全信任区域，为了确保eNodeB和MME之间的NAS信令不会被非法篡改，因此需要对NAS信令进行完整性保护。 
                NAS信令的完整性是MME系统安全的基本保障，所以完整性保护功能应该一直开启。但是为了满足运营商的个性化需求，MME可通过
                [SET SOFTWARE PARAMETER]
                命令将软件参数ID为327761的软件参数值设置为0来关闭对NAS信令的完整性保护。
            
功能描述 
该命令用于设置EPC NAS信令完整性保护的算法。 
                在软件参数ID为327761的软件参数值设置为1的情况下（该值通过
                [SET SOFTWARE PARAMETER]
                命令设置），可配置支持多种完整性保护算法和相应算法的优先级，优先级取值越小表示优先级越高。
            
MME选择完整性保护算法时，在UE和MME同时支持的完整性保护算法中，选择优先级最高的。如果两种完整性保护算法的优先级相同，则按照EIA1、EIA2、EIA3的顺序，优先选择排在前面的加密算法。比如：EIA1和EIA2的优先级相同，则选择EIA1作为完整性保护算法。 
对于完整性保护算法的优先级，建议采用系统默认值。 
相关主题 
 
设置EPC NAS完整性保护参数(SET NAS INTEGCTRL)
 
 
查询EPC NAS完整性保护参数(SHOW NAS INTEGCTRL)
 
 
父主题： [安全相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置EPC NAS完整性保护参数(SET NAS INTEGCTRL) 
#### 设置EPC NAS完整性保护参数(SET NAS INTEGCTRL) 
命令功能 
该命令用于设置EPC NAS完整性保护参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
INTEGALGO1|EIA1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME是否支持NAS完整性保护算法EIA1（EIA1是基于SNOW 3G的完整性保护算法），取值含义如下：不支持：表示不支持NAS完整性保护算法EIA1。支持：表示支持NAS完整性保护算法EIA1。
INTEGALGO2|EIA2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME是否支持NAS完整性保护算法EIA2（EIA2是基于AES的完整性保护算法），取值含义如下：不支持：表示不支持NAS完整性保护算法EIA2。支持：表示支持NAS完整性保护算法EIA2。
INTEGALGO3|EIA3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME是否支持NAS完整性保护算法EIA3（EIA3是基于ZUC的完整性保护算法），取值含义如下：不支持：表示不支持NAS完整性保护算法EIA3。支持：表示支持NAS完整性保护算法EIA3。
PRIORINTEG1|EIA1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS完整性保护算法EIA1的优先级；取值越小表示EIA1算法的优先级越高。
PRIORINTEG2|EIA2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS完整性保护算法EIA2的优先级；取值越小表示EIA2算法的优先级越高。
PRIORINTEG3|EIA3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS完整性保护算法EIA3的优先级；取值越小表示EIA3算法的优先级越高。
命令举例 
设置EPC NAS完整性保护参数，EIA1为不支持，EIA2为支持，EIA3为不支持，EIA1优先级为0，EIA2优先级为1，EIA3优先级为2。 
SET NAS INTEGCTRL:INTEGALGO1="Not support",INTEGALGO2="Support",INTEGALGO3="Not support",PRIORINTEG1="0",PRIORINTEG2="1",PRIORINTEG3="2"; 
父主题： [EPC NAS完整性保护参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询EPC NAS完整性保护参数(SHOW NAS INTEGCTRL) 
#### 查询EPC NAS完整性保护参数(SHOW NAS INTEGCTRL) 
命令功能 
该命令用于查询EPC NAS完整性保护参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
INTEGALGO1|EIA1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME是否支持NAS完整性保护算法EIA1（EIA1是基于SNOW 3G的完整性保护算法），取值含义如下：不支持：表示不支持NAS完整性保护算法EIA1。支持：表示支持NAS完整性保护算法EIA1。
INTEGALGO2|EIA2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME是否支持NAS完整性保护算法EIA2（EIA2是基于AES的完整性保护算法），取值含义如下：不支持：表示不支持NAS完整性保护算法EIA2。支持：表示支持NAS完整性保护算法EIA2。
INTEGALGO3|EIA3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME是否支持NAS完整性保护算法EIA3（EIA3是基于ZUC的完整性保护算法），取值含义如下：不支持：表示不支持NAS完整性保护算法EIA3。支持：表示支持NAS完整性保护算法EIA3。
PRIORINTEG1|EIA1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS完整性保护算法EIA1的优先级；取值越小表示EIA1算法的优先级越高。
PRIORINTEG2|EIA2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS完整性保护算法EIA2的优先级；取值越小表示EIA2算法的优先级越高。
PRIORINTEG3|EIA3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME支持的NAS完整性保护算法EIA3的优先级；取值越小表示EIA3算法的优先级越高。
命令举例 
查询EPC NAS完整性保护参数。 
SHOW NAS INTEGCTRL; 
`
操作维护  EIA1   EIA2   EIA3    EIA1优先级  EIA2优先级  EIA3优先级 
-------------------------------------------------------------------------
修改      支持   支持   不支持   0          1           2 
-------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [EPC NAS完整性保护参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### GPRS加密参数配置 
### GPRS加密参数配置 
背景知识 
当终端接入GPRS网络时，为了保证用户信令和数据的安全，网络需要对用户信令和数据进行加密。 
功能描述 
该配置用于设置对GPRS信令进行加密所使用的加密算法和对应算法的优先级。 
可以配置支持多种加密算法和相应算法的优先级，优先级取值越小表示优先级越高。 
SGSN选择加密算法时，在MS和SGSN同时支持的加密算法中，选择优先级最高的。如果两种加密算法的优先级相同，则按照GEA3、GEA2、GEA1的顺序，优先选择排在前面的加密算法。比如：GEA2和GEA1的优先级相同，则选择GEA2作为加密算法。 
对于加密算法的优先级，建议采用系统默认值。 
相关主题 
 
设置GPRS加密参数(SET GPRS ENCRYPTION)
 
 
查询GPRS加密参数(SHOW GPRS ENCRYPTION)
 
 
父主题： [安全相关配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 设置GPRS加密参数(SET GPRS ENCRYPTION) 
#### 设置GPRS加密参数(SET GPRS ENCRYPTION) 
命令功能 
该命令用于设置GPRS加密参数。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
GEA1|GEA1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法1（GEA1）。
GEA2|GEA2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法2（GEA2）。
GEA3|GEA3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法3（GEA3）。
PRIORGEA1|GPRS加密算法1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:。|GPRS加密算法1的优先级。
PRIORGEA2|GPRS加密算法2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:。|GPRS加密算法2的优先级。
PRIORGEA3|GPRS加密算法3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:。|GPRS加密算法3的优先级。
命令举例 
设置GPRS加密参数，GEA1为支持，GEA2为不支持，GEA3为不支持。 
SET GPRS ENCRYPTION:GEA1="Support",GEA2="Not support",GEA3="Not support"; 
父主题： [GPRS加密参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
#### 查询GPRS加密参数(SHOW GPRS ENCRYPTION) 
#### 查询GPRS加密参数(SHOW GPRS ENCRYPTION) 
命令功能 
该命令用于查询GPRS加密参数。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
GEA1|GEA1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法1（GEA1）。
GEA2|GEA2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法2（GEA2）。
GEA3|GEA3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|TAC是否支持GPRS加密算法3（GEA3）。
PRIORGEA1|GPRS加密算法1优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法1的优先级。
PRIORGEA2|GPRS加密算法2优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法2的优先级。
PRIORGEA3|GPRS加密算法3优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|GPRS加密算法3的优先级。
命令举例 
查询GPRS加密参数。 
SHOW GPRS ENCRYPTION; 
`
操作维护 GEA1     GEA2    GEA3     GPRS加密算法1优先级  GPRS加密算法2优先级   GPRS加密算法3优先级 
----------------------------------------------------------------------------------------------------
修改     不支持   不支持  不支持   2                    3                     1 
----------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [GPRS加密参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## GTP参数配置 
## GTP参数配置 
背景知识 
            
            根据协议29060描述，GTP协议承载在UDP/IP之上，由于UDP是无连接的不可靠传输协议，所以协议要求GTP本身要实现重发机制。
        
功能描述 
GTP参数配置是用来设置GTPC的信令消息的发送次数（包括首次发送和后续重发）， 是否主动发起ECHO消息，以及ECHO消息的发送次数（包括首次发送和后续重发）。 
这里的GTP信令消息是指除了路径管理类消息之外的GTPC消息。 
相关主题 
 
设置GTP参数(SET GTP PARAMETER)
 
 
查询GTP参数(SHOW GTP PARAMETER)
 
 
父主题： [安全变量]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置GTP参数(SET GTP PARAMETER) 
### 设置GTP参数(SET GTP PARAMETER) 
命令功能 
该命令用于设置GTP参数。
注意事项 
无。
参数说明 
标识|名称|类型|说明
---|---|---|---
SMSENDCOUNT|GTP会话管理信令发送次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该安全变量用于设置GTP会话管理信令消息发送次数（包括首次发送和后续重发）。默认值为5。在SGW没有响应的情况下，MME会重发GTP会话管理信令消息，当重发达到最大次数，仍然没有收到对端Response消息，则停止发送，流程失败或选择其他SGW重新尝试。该参数仅对S11接口的GTP会话管理信令消息有效。
ECHOREQ|主动发送ECHO消息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME是否主动发送Echo Request消息。如果设置为否，则本端MME不会主动发送Echo Request消息，但对于收到的Echo Request消息仍会回Echo Response响应消息。如果设置为是，则本端MME会主动发送Echo Request消息。
ECHORESENDCOUNT|ECHO信令发送次数|参数可选性:任选参数；参数类型:整数；参数范围为:3~30。|该参数用于设置Echo Request消息尝试次数（包括首次发送和后续重发），对应于协议29060中的N3-REQUESTS计数器。当对端不回Echo Response消息时，MME会重发Echo Request消息。 当重发达到最大次数，仍然没有收到对端Echo Response消息，则停止发送，认为对端链路故障或对端网元发生故障。
MMSENDCOUNT|GTP移动性管理信令发送次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|该安全变量用于设置GTP移动性管理信令消息发送次数（包括首次发送和后续重发）。默认值为5。在对端MME/SGSN没有响应的情况下，MME会重发GTP移动性管理信令消息，重发达到最大次数，仍然没有收到对端Response消息时，停止发送。对除了S11接口之外的S10、Gn/Gp、Sv等接口的GTP移动性管理信令消息有效。
IFDELAYDETECT|SGW不回Echo响应时是否延迟回收用户资源|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于标识在SGW连续多次不回Echo响应的情况下，MME是否会在继续检测SGW一段时间后，才确定是否回收或恢复相关用户资源。0-否：不继续检测。确定回收或恢复相关用户资源。1-是：继续检测。确定不回收或恢复相关用户资源。继续检测的时间为“延迟检测Echo发送次数”与Echo发送时间间隔的乘积。
DELAYECHONUM|延迟检测Echo发送次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于标识在SGW连续多次不回Echo响应的情况下，MME若继续检测SGW，通过向SGW发送Echo Request消息进行检测的次数。
命令举例 
设置GTP参数，GTP信令发送次数为3，主动发送ECHO消息为YES，ECHO信令发送次数为6。 
SET GTP PARAMETER:RESENDCOUNT=3,SGSNECHO="YES",ECHORESENDCOUNT=6 
父主题： [GTP参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询GTP参数(SHOW GTP PARAMETER) 
### 查询GTP参数(SHOW GTP PARAMETER) 
命令功能 
该命令用于查询GTP参数。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SMSENDCOUNT|GTP会话管理信令发送次数|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置GTP会话管理信令消息发送次数（包括首次发送和后续重发）。默认值为5。在SGW没有响应的情况下，MME会重发GTP会话管理信令消息，当重发达到最大次数，仍然没有收到对端Response消息，则停止发送，流程失败或选择其他SGW重新尝试。该参数仅对S11接口的GTP会话管理信令消息有效。
ECHOREQ|主动发送ECHO消息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该安全变量用于设置MME是否主动发送Echo Request消息。如果设置为否，则本端MME不会主动发送Echo Request消息，但对于收到的Echo Request消息仍会回Echo Response响应消息。如果设置为是，则本端MME会主动发送Echo Request消息。
ECHORESENDCOUNT|ECHO信令发送次数|参数可选性:任选参数；参数类型:整数。|该参数用于设置Echo Request消息尝试次数（包括首次发送和后续重发），对应于协议29060中的N3-REQUESTS计数器。当对端不回Echo Response消息时，MME会重发Echo Request消息。 当重发达到最大次数，仍然没有收到对端Echo Response消息，则停止发送，认为对端链路故障或对端网元发生故障。
MMSENDCOUNT|GTP移动性管理信令发送次数|参数可选性:任选参数；参数类型:整数。|该安全变量用于设置GTP移动性管理信令消息发送次数（包括首次发送和后续重发）。默认值为5。在对端MME/SGSN没有响应的情况下，MME会重发GTP移动性管理信令消息，重发达到最大次数，仍然没有收到对端Response消息时，停止发送。对除了S11接口之外的S10、Gn/Gp、Sv等接口的GTP移动性管理信令消息有效。
IFDELAYDETECT|SGW不回Echo响应时是否延迟回收用户资源|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于标识在SGW连续多次不回Echo响应的情况下，MME是否会在继续检测SGW一段时间后，才确定是否回收或恢复相关用户资源。0-否：不继续检测。确定回收或恢复相关用户资源。1-是：继续检测。确定不回收或恢复相关用户资源。继续检测的时间为“延迟检测Echo发送次数”与Echo发送时间间隔的乘积。
DELAYECHONUM|延迟检测Echo发送次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|该参数用于标识在SGW连续多次不回Echo响应的情况下，MME若继续检测SGW，通过向SGW发送Echo Request消息进行检测的次数。
命令举例 
查询GTP参数。 
SHOW GTP PARAMETER 
`
操作维护 GTP会话管理信令发送次数 主动发送ECHO消息 ECHO信令发送次数 GTP移动性管理信令发送次数 SGW不回Echo响应时是否延迟回收用户资源 延迟检测Echo发送次数
-------------------------------------------------------------------------------------------------------------------------------------------------------
修改     5                       是               5                5                         是                                    12
-------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.047 秒）。
` 
父主题： [GTP参数配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
# DNS服务器配置 
# DNS服务器配置 
背景知识 
在附着、RAU/TAU、切换、PDP激活/PDN连接等业务流程中，ZXUN uMAC需要获取与之交互的SGSN、MME、GGSN、SGW或PGW的地址。如果这些地址没有在本网元配置，则需要发送消息到DNS服务器进行查询，获取对应的地址，此时SGSN/MME需要具有DNS客户端的功能，作为DNS客户端，与DNS服务器进行交互。 
DNS服务器用于提供根据域名解析IP地址的功能，通常DNS服务器为运行DNS服务器软件的一台网络服务器。 
功能描述 
在ZXUN uMAC，配置DNS（Domain Name System）服务器相关数据，可以提供DNS服务器运行需要的ZONE、视图、ACL和资源记录的功能。 
相关主题 
 
DNS服务器节点配置
 
 
DNS基础配置
 
 
DNS ACL配置
 
 
DNS视图配置
 
 
DNS区域配置
 
 
资源记录配置
 
 
进入DNS模式(ENTER DNS)
 
 
退出DNS模式(EXIT DNS)
 
 
备份DNS服务器数据(BACKUP DNS)
 
 
恢复DNS服务器数据(RESTORE DNS)
 
 
刷新DNS服务器数据到本地数据库(REFRESH LOCALDNS)
 
 
同步DNS服务器配置(SYN DNS)
 
 
强制退出DNS模式(EXIT DNS FORCE)
 
 
重新加载DNS服务器(RELOAD DNS)
 
 
查询DNS服务器版本(SHOW DNS SERVER VERSION)
 
 
查询DNS服务器主从状态(SHOW DNS SERVER STATE)
 
 
父主题： [配置管理]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## DNS服务器节点配置 
## DNS服务器节点配置 
背景知识 
DNS服务器是运行DNS软件，提供DNS服务的一组网络服务器，为保证可靠性通常DNS服务器以主备方式运行。 
功能描述 
用于配置DNS服务器的IP等基本信息。对DNS服务器操作时从本配置获取DNS服务器的IP等基本信息后发起对应的下载和上传请求。本配置为基础配置，删除前请确认。 
相关主题 
 
新增DNS服务器节点(ADD DNS)
 
 
修改DNS服务器节点(SET DNS)
 
 
删除DNS服务器节点(DEL DNS)
 
 
查询DNS服务器节点(SHOW DNS)
 
 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增DNS服务器节点(ADD DNS) 
### 新增DNS服务器节点(ADD DNS) 
命令功能 
该命令用于增加DNS服务器节点。当用户需要管理DNS服务器配置数据时，为接入DNS服务器需要使用该命令配置DNS服务器节点，配置成功后，可以通过[SHOW DNS]查看当前已经配置的DNS服务器节点。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|服务器编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|用于指示被操作的DNS服务器编号。
CONNTYPE|连接方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:SSH。|用于指示被操作的DNS服务器连接方式，支持2种接入方式：SSH或者TELNET。
IP|DNS服务器IP地址|参数可选性:必选参数；参数类型:地址|用于描述被操作DNS服务器的管理口IP地址，通过该IP网管接入DNS服务器。
CONNPORT|连接端口|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。默认值:22。|用于指示被操作的DNS服务器接入端口，SSH连接方式对应的连接端口默认是22，TELNET连接方式对应的连接端口默认是23。
PWD|ROOT密码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|用于描述被操作DNS服务器ROOT用户的密码。
FTPTYPE|FTP/SFTP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:SFTP。|用于描述该DNS服务器开放的FTP/SFTP服务类型，一般使用SFTP服务。
PORT|FTP端口|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。默认值:22。|用于描述该DNS服务器开放的FTP/SFTP服务端口，默认为22。
PATH|路径|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。默认值:/etc。|用于描述该DNS服务器开放的FTP/SFTP服务的根路径。
FTPUSER|FTP/SFTP服务器用户名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|用于描述该DNS服务器开放的FTP/SFTP服务的用户名。
FTPPWD|FTP/SFTP服务器密码|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|用于描述该DNS服务器开放的FTP/SFTP服务的密码。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用于描述DNS服务器的用户别名。
命令举例 
增加DNS服务器节点，指定服务器编号为1，连接方式为SSH，DNS服务器管理口IP为10.42.184.198，连接端口为22，ROOT密码为root123，FTP/SFTP服务器用户名为root，FTP/SFTP服务器密码为root123。  
ADD DNS:ID=1,CONNTYPE="SSH",IP="10.42.184.198",CONNPORT="22",PWD="root123",FTPUSER="root",FTPPWD="root123"; 
父主题： [DNS服务器节点配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改DNS服务器节点(SET DNS) 
### 修改DNS服务器节点(SET DNS) 
命令功能 
该命令用于修改DNS服务器节点。当用户需要修改DNS服务器的基本信息时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|服务器编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|用于指示被操作的DNS服务器编号。
CONNTYPE|连接方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于指示被操作的DNS服务器连接方式，支持2种接入方式：SSH或者TELNET。
IP|DNS服务器IP地址|参数可选性:任选参数；参数类型:地址|用于描述被操作DNS服务器的管理口IP地址，通过该IP网管接入DNS服务器。
CONNPORT|连接端口|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|用于指示被操作的DNS服务器接入端口，SSH连接方式对应的连接端口默认是22，TELNET连接方式对应的连接端口默认是23。
PWD|ROOT密码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用于描述被操作DNS服务器ROOT用户的密码。
FTPTYPE|FTP/SFTP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该DNS服务器开放的FTP/SFTP服务类型，一般使用SFTP服务。
PORT|FTP端口|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|用于描述该DNS服务器开放的FTP/SFTP服务端口，默认为22。
PATH|路径|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于描述该DNS服务器开放的FTP/SFTP服务的根路径。
FTPUSER|FTP/SFTP服务器用户名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用于描述该DNS服务器开放的FTP/SFTP服务的用户名。
FTPPWD|FTP/SFTP服务器密码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用于描述该DNS服务器开放的FTP/SFTP服务的密码。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用于描述DNS服务器的用户别名。
命令举例 
修改DNS服务器节点，指定服务器编号为1，服务器管理口IP为10.42.184.198，ROOT密码为"root123"。  
SET DNS:ID=1,IP="10.42.184.198",PWD="root123"; 
父主题： [DNS服务器节点配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除DNS服务器节点(DEL DNS) 
### 删除DNS服务器节点(DEL DNS) 
命令功能 
该命令用于删除DNS服务器节点。当用户不再需要管理该DNS服务器时，使用该命令删除该DNS服务器节点。 
注意事项 
删除DNS服务器点将连带删除网管为此节点保存的配置数据，删除前请务必确认。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|服务器编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|用于指示被操作的DNS服务器编号。
命令举例 
删除DNS服务器节点，指定服务器编号为1。  
DEL DNS:ID=1; 
父主题： [DNS服务器节点配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询DNS服务器节点(SHOW DNS) 
### 查询DNS服务器节点(SHOW DNS) 
命令功能 
该命令用于查询DNS服务器节点。当用户需要查看已经配置的DNS服务器节点时使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|服务器编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|用于指示被操作的DNS服务器编号。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ID|服务器编号|参数可选性:任选参数；参数类型:整数。|用于指示被操作的DNS服务器编号。
CONNTYPE|连接方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于指示被操作的DNS服务器连接方式，支持2种接入方式：SSH或者TELNET。
IP|DNS服务器IP地址|参数可选性:任选参数；参数类型:地址|用于描述被操作DNS服务器的管理口IP地址，通过该IP网管接入DNS服务器。
CONNPORT|连接端口|参数可选性:任选参数；参数类型:整数。|用于指示被操作的DNS服务器接入端口，SSH连接方式对应的连接端口默认是22，TELNET连接方式对应的连接端口默认是23。
FTPTYPE|FTP/SFTP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于描述该DNS服务器开放的FTP/SFTP服务类型，一般使用SFTP服务。
PORT|FTP端口|参数可选性:任选参数；参数类型:整数。|用于描述该DNS服务器开放的FTP/SFTP服务端口，默认为22。
PATH|路径|参数可选性:任选参数；参数类型:字符型。|用于描述该DNS服务器开放的FTP/SFTP服务的根路径。
FTPUSER|FTP/SFTP服务器用户名|参数可选性:任选参数；参数类型:字符型。|用于描述该DNS服务器开放的FTP/SFTP服务的用户名。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型。|用于描述DNS服务器的用户别名。
命令举例 
查询全部DNS服务器节点。  
SHOW DNS; 
`
命令 (No.17): SHOW DNS
操作维护         服务器编号   连接方式   DNS服务器IP地址   连接端口   FTP/SFTP类型   FTP端口   路径    FTP/SFTP服务器用户名   用户别名
---------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1            SSH        10.42.184.198      22         SFTP           22        /etc/   root                   
---------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.021 秒）。
` 
父主题： [DNS服务器节点配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## DNS基础配置 
## DNS基础配置 
背景知识 
DNS服务器的全局选项保存在named.conf配置文件中，包括了DNS进程运行的最重要的设置信息，如DNS监听端口，是否允许转发等。 
功能描述 
用于配置DNS服务器的全局选项参数，包括允许查询的源地址，允许通知，监听接口，转发列表，递归查询，递归查询请求并发最大客户端，性能统计文件路径等。 
相关主题 
 
设置DNS基础配置(SET NAMEDCFG)
 
 
查询DNS基础配置(SHOW NAMEDCFG)
 
 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 设置DNS基础配置(SET NAMEDCFG) 
### 设置DNS基础配置(SET NAMEDCFG) 
命令功能 
该命令用于设置DNS基础配置。当用户需要设置DNS全局选项时，使用该命令。 
注意事项 
本命令设置的全局选项非常重要，请确认后修改。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ALLOWQUERY|允许查询的源地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~45个字符。|用来设定哪个主机可以进行普通的查询。该选项也能在DNS区域中设定，这样全局选项中的选项就不起作用了。默认的是允许所有主机进行查询。
NOTIFY|允许通知|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否允许通知。有下面取值：yes：默认值，当一个授权的服务器修改了一个域后，DNS NOTIFY 信息被发送出去。此信息将会发给列在域NS 记录上的服务器和任何列在also-notify 选项中的服务器。no：不会发出任何报文。Notify 选项也可能设定在DNS区域中，这样就替代了本处的设置。
LISTENON|监听接口|参数可选性:任选参数；参数类型:字符型；参数范围为:0~1000个字符。|DNS监听端口，服务器用来接收和发送DNS 协议数据的UDP/TCP端口号。默认为53。
FORWARD|转发|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此选项只有当转发器列表中有内容的时候才有意义。FIRST：默认情况下，使服务器先查询设置的转发器列表，如果没有得到回答，服务器就会自己寻找答案。ONLY：服务器只会把请求转发到其它服务器上去。
FORWARDERS|转发器|参数可选性:任选参数；参数类型:字符型；参数范围为:0~45个字符。|设定转发使用的IP地址。默认的列表是空的(不转发)。转发也可以设置在每个区域上，这样全局选项中的转发设置就不会起作用。用户可以将多个区域都转发到服务器上，或者对不同的区域使用forward only 或first的不同方式，也可以不转发。
RECURSION|递归查询|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|本参数用于设置是否递归查询，包括下面取值：YES：允许递归查询。此时如果一个DNS询问要求递归，那么服务器将会做所有能够回答查询请求的工作。NO：不允许查询。此时如果服务器不知道答案，将会返回一个推荐响应。默认值是YES。
RECURSIVECLIENTS|递归查询请求并发最大客户端|参数可选性:任选参数；参数类型:整数；参数范围为:0~1000000。|服务器同时执行的递归查询的最大数量。默认值1000，该选项值必须根据DNS服务器实际内存大小调整。
STATISTICSFILE|性能统计文件路径|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|性能统计文件路径，当使用rndc stats命令的时候，服务器会将统计信息保存到该文件路径下。如果没有指定，默认为named.stats在服务器程序的当前目录中。
命令举例 
修改DNS基础配置，指定递归查询为"YES"。  
SET NAMEDCFG:RECURSION="YES"; 
父主题： [DNS基础配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询DNS基础配置(SHOW NAMEDCFG) 
### 查询DNS基础配置(SHOW NAMEDCFG) 
命令功能 
该命令用于查询DNS基础配置。当用户需要查看当前DNS基础配置使用该命令。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ALLOWQUERY|允许查询的源地址|参数可选性:任选参数；参数类型:字符型。|用来设定哪个主机可以进行普通的查询。该选项也能在DNS区域中设定，这样全局选项中的选项就不起作用了。默认的是允许所有主机进行查询。
NOTIFY|允许通知|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否允许通知。有下面取值：yes：默认值，当一个授权的服务器修改了一个域后，DNS NOTIFY 信息被发送出去。此信息将会发给列在域NS 记录上的服务器和任何列在also-notify 选项中的服务器。no：不会发出任何报文。Notify 选项也可能设定在DNS区域中，这样就替代了本处的设置。
LISTENON|监听接口|参数可选性:任选参数；参数类型:字符型。|DNS监听端口，服务器用来接收和发送DNS 协议数据的UDP/TCP端口号。默认为53。
FORWARD|转发|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|此选项只有当转发器列表中有内容的时候才有意义。FIRST：默认情况下，使服务器先查询设置的转发器列表，如果没有得到回答，服务器就会自己寻找答案。ONLY：服务器只会把请求转发到其它服务器上去。
FORWARDERS|转发器|参数可选性:任选参数；参数类型:字符型。|设定转发使用的IP地址。默认的列表是空的(不转发)。转发也可以设置在每个区域上，这样全局选项中的转发设置就不会起作用。用户可以将多个区域都转发到服务器上，或者对不同的区域使用forward only 或first的不同方式，也可以不转发。
RECURSION|递归查询|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|本参数用于设置是否递归查询，包括下面取值：YES：允许递归查询。此时如果一个DNS询问要求递归，那么服务器将会做所有能够回答查询请求的工作。NO：不允许查询。此时如果服务器不知道答案，将会返回一个推荐响应。默认值是YES。
RECURSIVECLIENTS|递归查询请求并发最大客户端|参数可选性:任选参数；参数类型:整数。|服务器同时执行的递归查询的最大数量。默认值1000，该选项值必须根据DNS服务器实际内存大小调整。
STATISTICSFILE|性能统计文件路径|参数可选性:任选参数；参数类型:字符型。|性能统计文件路径，当使用rndc stats命令的时候，服务器会将统计信息保存到该文件路径下。如果没有指定，默认为named.stats在服务器程序的当前目录中。
命令举例 
查询当前DNS基础配置。  
SHOW NAMEDCFG; 
`
命令 (No.1): SHOW NAMEDCFG
允许查询的源地址   允许通知   监听接口             转发    转发器                          递归查询   递归查询请求并发最大客户端   性能统计文件路径
---------------------------------------------------------------------------------------------------------------------------------------------------
any;                          port  53  { any; }   only    221.177.173.1; 221.177.173.5;   yes        100000                       /var/log/named_stats.log
---------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.038 秒）。
` 
父主题： [DNS基础配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## DNS ACL配置 
## DNS ACL配置 
背景知识 
访问控制列表（Access Control List, ACL）就是一个被命名的地址匹配列表。使用访问控制列表可以使配置简单而清晰，一次定义之后可以在多处使用，从而不会使配置文件因为大量的IP地址而变得混乱。 
功能描述 
用于配置ACL的名称及其地址列表。 
相关主题 
 
新增DNS ACL配置(ADD DNSACL)
 
 
修改DNS ACL配置(SET DNSACL)
 
 
删除DNS ACL配置(DEL DNSACL)
 
 
查询DNS ACL配置(SHOW DNSACL)
 
 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增DNS ACL配置(ADD DNSACL) 
### 新增DNS ACL配置(ADD DNSACL) 
命令功能 
该命令用于增加ACL。当用户需要增加ACL时，使用该命令。配置成功后，可以通过[SHOW DNSACL]查看当前已经配置的DNS ACL。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ACL|ACL名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|ACL名称，用于唯一标识一条ACL。
MATCHLIST|地址列表|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|地址匹配列表，包括多个IP地址、网段或者ACL。引用ACL时不能是该ACL自身。
命令举例 
增加ACL，指定ACL名称为our-nets，地址匹配列表为网段"169.254.0.0/16"和网段"192.0.2.0/24"。  
ADD DNSACL:ACL="our-nets" ,MATCHLIST="169.254.0.0/16"&"192.0.2.0/24"; 
父主题： [DNS ACL配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改DNS ACL配置(SET DNSACL) 
### 修改DNS ACL配置(SET DNSACL) 
命令功能 
该命令用于修改ACL。当用户需要修改DNS ACL的地址列表时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ACL|ACL名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|ACL名称，用于唯一标识一条ACL。
MATCHLIST|地址列表|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|地址匹配列表，包括多个IP地址、网段或者ACL。引用ACL时不能是该ACL自身。
命令举例 
修改名称为"our-nets"的ACL，指定地址匹配列表为网段"169.254.0.0/16"。 
SET DNSACL:ACL="our-nets" ,MATCHLIST="169.254.0.0/16"; 
父主题： [DNS ACL配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除DNS ACL配置(DEL DNSACL) 
### 删除DNS ACL配置(DEL DNSACL) 
命令功能 
该命令用于删除ACL。当用户不再需要某个ACL时，使用该命令删除该ACL。 
注意事项 
删除ACL前，请先检查该ACL不再被DNS VIEW或者ZONE引用。查询DNS视图命令为[SHOW DNSVIEW]，查询DNS区域命令。
参数说明 
标识|名称|类型|说明
---|---|---|---
ACL|ACL名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|ACL名称，用于唯一标识一条ACL。
命令举例 
删除名称为"our-nets"的ACL。 
DEL DNSACL:ACL="our-nets"; 
父主题： [DNS ACL配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询DNS ACL配置(SHOW DNSACL) 
### 查询DNS ACL配置(SHOW DNSACL) 
命令功能 
该命令用于查询ACL。当用户需要查看已经配置的ACL时使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ACL|ACL名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|ACL名称，用于唯一标识一条ACL。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ACL|ACL名称|参数可选性:任选参数；参数类型:字符型。|ACL名称，用于唯一标识一条ACL。
MATCHLIST|地址列表|参数可选性:任选参数；参数类型:字符型；参数范围为:0~1000个字符。|地址匹配列表，包括多个IP地址、网段或者ACL。引用ACL时不能是该ACL自身。
命令举例 
查询全部DNS ACL。 
SHOW DNSACL; 
`
命令 (No.1): SHOW DNSACL;
ACL名称    地址列表
-------------------
our-nets   169.254.0.0/16;192.0.2.0/24;
-------------------
记录数 1
命令执行成功（耗时 0.02 秒）。
` 
父主题： [DNS ACL配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## DNS视图配置 
## DNS视图配置 
背景知识 
DNS视图允许名称服务器根据询问者的不同有区别的回答DNS查询，当运行拆分DNS设置而不需要运行多个服务器时特别有用。每个DNS视图定义了一个将会在用户的子集中见到的DNS名称空间。 
功能描述 
用于配置DNS视图的基本参数，包括视图名称和匹配的源地址信息。 
相关主题 
 
新增DNS视图配置(ADD DNSVIEW)
 
 
修改DNS视图配置(SET DNSVIEW)
 
 
删除DNS视图配置(DEL DNSVIEW)
 
 
查询DNS视图配置(SHOW DNSVIEW)
 
 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增DNS视图配置(ADD DNSVIEW) 
### 新增DNS视图配置(ADD DNSVIEW) 
命令功能 
该命令用于增加DNS视图。当用户需要增加DNS视图时，使用该命令。配置成功后，可以通过[SHOW DNSVIEW]查看当前已经配置的DNS视图。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
VIEW|视图名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|DNS视图名称，唯一标识一个DNS视图。
MATCHCLIENTS|匹配源地址|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|DNS视图匹配的源地址，可以是网段，ACL或者IP地址，包括4个预定义的ACL：any：所有地址none：所有地址都不允许localhost：本机localnets：本地网络
命令举例 
增加DNS视图，指定视图名称为"internal"，匹配源地址为"10.0.0.0/8"。  
ADD DNSVIEW:VIEW="internal",MATCHCLIENTS="10.0.0.0/8"; 
父主题： [DNS视图配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改DNS视图配置(SET DNSVIEW) 
### 修改DNS视图配置(SET DNSVIEW) 
命令功能 
该命令用于修改DNS视图。当用户需要修改DNS视图的匹配源地址时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
VIEW|视图名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|DNS视图名称，唯一标识一个DNS视图。
MATCHCLIENTS|匹配源地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图匹配的源地址，可以是网段，ACL或者IP地址，包括4个预定义的ACL：any：所有地址none：所有地址都不允许localhost：本机localnets：本地网络
命令举例 
修改名称为"internal"的DNS视图，匹配源地址为"10.0.0.0/8"。  
SET DNSVIEW:VIEW="internal",MATCHCLIENTS="10.0.0.0/8"; 
父主题： [DNS视图配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除DNS视图配置(DEL DNSVIEW) 
### 删除DNS视图配置(DEL DNSVIEW) 
命令功能 
该命令用于删除DNS视图。当用户不再需要某个DNS视图时，使用该命令删除该视图。 
注意事项 
删除DNS视图前，请先清除该视图下的区域。 
参数说明 
标识|名称|类型|说明
---|---|---|---
VIEW|视图名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|DNS视图名称，唯一标识一个DNS视图。
命令举例 
删除名称为"internal"的DNS视图。  
DEL DNSVIEW:VIEW="internal"; 
父主题： [DNS视图配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询DNS视图配置(SHOW DNSVIEW) 
### 查询DNS视图配置(SHOW DNSVIEW) 
命令功能 
该命令用于查询DNS视图。当用户需要查看已经配置的DNS视图时使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图名称，唯一标识一个DNS视图。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型。|DNS视图名称，唯一标识一个DNS视图。
MATCHCLIENTS|匹配源地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~1000个字符。|DNS视图匹配的源地址，可以是网段，ACL或者IP地址，包括4个预定义的ACL：any：所有地址none：所有地址都不允许localhost：本机localnets：本地网络
命令举例 
查询全部DNS视图。 
SHOW DNSVIEW; 
`
命令 (No.1): SHOW DNSVIEW
视图名称   匹配源地址
---------------------
internal   10.0.0.0/8;
---------------------
记录数 1
命令执行成功（耗时 0.039 秒）。
` 
父主题： [DNS视图配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## DNS区域配置 
## DNS区域配置 
背景知识 
DNS整个的域名空间可以被分成多个区域（zone）。区域开始于一个顶级域名，一直到一个子域名或是其它域名的开始。区域通常表示管理界限的划分，是DNS树状结构上的一个标识的点。一个区域包含了那些相邻的域名树结构的部分，并具有此部分的全部信息，并且它是真正授权的。区域包含了这个节点下的所有域名，但不包括其它域里已经指定的。 
SOA：起始授权机构（Start Of Authority，SOA）的资源记录，描述了域名的管理员、电子邮件地址，和一些时间参数。 
功能描述 
用于配置DNS区域的基本信息，包括区域名称、所在视图名称、区域类型、区域资源记录存储的文件名称等信息。 
相关主题 
 
新增DNS区域配置(ADD DNSZONE)
 
 
修改DNS区域配置(SET DNSZONE)
 
 
删除DNS区域配置(DEL DNSZONE)
 
 
查询DNS区域配置(SHOW DNSZONE)
 
 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增DNS区域配置(ADD DNSZONE) 
### 新增DNS区域配置(ADD DNSZONE) 
命令功能 
该命令用于增加DNS区域。当用户需要增加DNS区域时，使用该命令。配置成功后，可以通过[SHOW DNSZONE]查看当前已经配置的DNS区域。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|区域名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图名称，用于标识DNS区域所在的视图。
TYPE|类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|区域类型，用于标识DNS区域文件的类型。MASTER：服务器有一个主域（也称为控制域）的配置文件拷贝，能够为之提供授权解析服务。SLAVE：辅域（也可以叫次级域）是主域的复制。STUB：子根域与辅域类似,除了只复制主域的NS 记录而不是整个域。根域不是DNS的一个标准部分，它们是DNS 运行的特有性质。FORWARD：“转发域”，用于对该域单独设置转发方式。forward类型的域语句包括一个转发语句和转发列表，都应用于在域内的由域名给出的查询。HINT：表示根类型区域，用来指定初始的根名字服务器集合。在DNS服务器启动时，DNS服务器使用根提示信息来找到一个根名字服务器并从后者获取最近的根名字服务器名单。
FILE|文件名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于标识区域数据所在的文件名称。
FORWARDERS|转发器|参数可选性:任选参数；参数类型:字符型；参数范围为:0~45个字符。|转发器列表，用来代替全局的转发器列表。
SOADOMAINNAME|SOA域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|用于标识起始授权机构（Start Of Authority，SOA）的域名。
SOA|主服务器名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|用于标识SOA域名解析使用的服务器。
POSTMASTER|域名管理者的电子邮件地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于标识SOA域名管理者的电子邮件地址。
SERIALNO|序列号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|用于标识区域信息变化的序列号。每次域名信息变化该项数值需要增大。
REFRESHTIME|刷新时间(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~65535。默认值:3600。|刷新间隔，备用DNS服务器隔一定时间会查询主DNS服务器中的序列号是否增加，即域文件是否有变化。
RETRYTIME|重试时间(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~65535。默认值:600。|重试时间，表示如果备用服务器无法连上主服务器，过多久再重试。
EXPIRETIME|过期时间(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~4294967295。默认值:86400。|过期时间，当备用DNS服务器无法联系上主DNS服务器时，备用DNS服务器可以在多长时间内认为其缓存是有效的，并供用户查询。
MINIMUMTIME|最小TTL(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~3000000。默认值:3600。|用于表示缓存DNS服务器可以缓存记录多长时间。
命令举例 
增加DNS区域，指定区域名称为"129.16.172.in-addr.arpa"，区域类型为MASTER，文件保存在"named.172.16.129.txt"。  
ADD DNSZONE:ZONE="129.16.172.in-addr.arpa",TYPE="MASTER",FILE="named.172.16.129.txt",SOADOMAINNAME="soa1",SOA="host1"; 
父主题： [DNS区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 修改DNS区域配置(SET DNSZONE) 
### 修改DNS区域配置(SET DNSZONE) 
命令功能 
该命令用于修改DNS区域。当用户需要修改DNS区域的类型，存储文件或者其他参数时，使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|区域名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图名称，用于标识DNS区域所在的视图。
FORWARDERS|转发器|参数可选性:任选参数；参数类型:字符型；参数范围为:0~45个字符。|转发器列表，用来代替全局的转发器列表。
SOADOMAINNAME|SOA域名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于标识起始授权机构（Start Of Authority，SOA）的域名。
SOA|主服务器名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于标识SOA域名解析使用的服务器。
POSTMASTER|域名管理者的电子邮件地址|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于标识SOA域名管理者的电子邮件地址。
SERIALNO|序列号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|用于标识区域信息变化的序列号。每次域名信息变化该项数值需要增大。
REFRESHTIME|刷新时间(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~65535。|刷新间隔，备用DNS服务器隔一定时间会查询主DNS服务器中的序列号是否增加，即域文件是否有变化。
RETRYTIME|重试时间(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~65535。|重试时间，表示如果备用服务器无法连上主服务器，过多久再重试。
EXPIRETIME|过期时间(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~4294967295。|过期时间，当备用DNS服务器无法联系上主DNS服务器时，备用DNS服务器可以在多长时间内认为其缓存是有效的，并供用户查询。
MINIMUMTIME|最小TTL(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:100~3000000。|用于表示缓存DNS服务器可以缓存记录多长时间。
命令举例 
修改名称为"129.16.172.in-addr.arpa"的DNS区域，区域类型为SLAVE。  
SET DNSZONE:ZONE="129.16.172.in-addr.arpa",TYPE="SLAVE"; 
父主题： [DNS区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除DNS区域配置(DEL DNSZONE) 
### 删除DNS区域配置(DEL DNSZONE) 
命令功能 
该命令用于删除DNS区域。当用户不再需要某个DNS区域时，使用该命令删除该区域。 
注意事项 
删除DNS区域前，请先清除该区域下的资源记录。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|区域名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~63个字符。|DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图名称，用于标识DNS区域所在的视图。
命令举例 
删除名称为"129.16.172.in-addr.arpa"的DNS区域。  
DEL DNSZONE:ZONE="129.16.172.in-addr.arpa"; 
父主题： [DNS区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询DNS区域配置(SHOW DNSZONE) 
### 查询DNS区域配置(SHOW DNSZONE) 
命令功能 
该命令用于查询DNS区域。当用户需要查看已经配置的DNS区域时使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|区域名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图名称，用于标识DNS区域所在的视图。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|区域名称|参数可选性:任选参数；参数类型:字符型。|DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型。|DNS视图名称，用于标识DNS区域所在的视图。
TYPE|类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|区域类型，用于标识DNS区域文件的类型。MASTER：服务器有一个主域（也称为控制域）的配置文件拷贝，能够为之提供授权解析服务。SLAVE：辅域（也可以叫次级域）是主域的复制。STUB：子根域与辅域类似,除了只复制主域的NS 记录而不是整个域。根域不是DNS的一个标准部分，它们是DNS 运行的特有性质。FORWARD：“转发域”，用于对该域单独设置转发方式。forward类型的域语句包括一个转发语句和转发列表，都应用于在域内的由域名给出的查询。HINT：表示根类型区域，用来指定初始的根名字服务器集合。在DNS服务器启动时，DNS服务器使用根提示信息来找到一个根名字服务器并从后者获取最近的根名字服务器名单。
FILE|文件名称|参数可选性:任选参数；参数类型:字符型。|用于标识区域数据所在的文件名称。
FORWARDERS|转发器|参数可选性:任选参数；参数类型:字符型。|转发器列表，用来代替全局的转发器列表。
SOADOMAINNAME|SOA域名|参数可选性:任选参数；参数类型:字符型。|用于标识起始授权机构（Start Of Authority，SOA）的域名。
SOA|主服务器名称|参数可选性:任选参数；参数类型:字符型。|用于标识SOA域名解析使用的服务器。
POSTMASTER|域名管理者的电子邮件地址|参数可选性:任选参数；参数类型:字符型。|用于标识SOA域名管理者的电子邮件地址。
SERIALNO|序列号|参数可选性:任选参数；参数类型:整数。|用于标识区域信息变化的序列号。每次域名信息变化该项数值需要增大。
REFRESHTIME|刷新时间(秒)|参数可选性:任选参数；参数类型:整数。|刷新间隔，备用DNS服务器隔一定时间会查询主DNS服务器中的序列号是否增加，即域文件是否有变化。
RETRYTIME|重试时间(秒)|参数可选性:任选参数；参数类型:整数。|重试时间，表示如果备用服务器无法连上主服务器，过多久再重试。
EXPIRETIME|过期时间(秒)|参数可选性:任选参数；参数类型:整数。|过期时间，当备用DNS服务器无法联系上主DNS服务器时，备用DNS服务器可以在多长时间内认为其缓存是有效的，并供用户查询。
MINIMUMTIME|最小TTL(秒)|参数可选性:任选参数；参数类型:整数。|用于表示缓存DNS服务器可以缓存记录多长时间。
命令举例 
查询全部DNS区域。  
SHOW DNSZONE; 
`
命令 (No.1): SHOW DNSZONE
区域名称                                           视图名称   类型      文件名称                    转发器   SOA域名   主服务器名称                        域名管理者的电子邮件地址                 序列号       刷新时间(秒)   重试时间(秒)   过期时间(秒)   最小TTL(秒)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
.                                                             hint      named.cache                                                                                                                                                                           
0.0.127.in-addr.arpa                                          master    named.127.0.0                        @         localhost.                          postmaster.localhost.                    2010111601   10800          3600           604800         86400
170.177.221.in-addr.arpa                                      master    named.221.177.170                    @         localhost.                          postmaster.localhost.                    2010111601   10800          3600           604800         86400
cdbxboss.hn.mnc000.mcc460.gprs                                master    VPN11.cmnet                          @         hndns01bzx.hn.mnc000.mcc460.gprs.   root.hndns01bzx.hn.mnc000.mcc460.gprs.   1            3600           900            3600000        3600
cdbxboss.hn.mnc002.mcc460.gprs                                master    VPN11.cmnet                          @         hndns01bzx.hn.mnc000.mcc460.gprs.   root.hndns01bzx.hn.mnc000.mcc460.gprs.   1            3600           900            3600000        3600
zzszf.hn.mnc007.mcc460.gprs                                   master    VPN11.cmnet                          @         hndns01bzx.hn.mnc000.mcc460.gprs.   root.hndns01bzx.hn.mnc000.mcc460.gprs.   1            3600           900            3600000        3600
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 5
命令执行成功（耗时 0.159 秒）。
` 
父主题： [DNS区域配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 资源记录配置 
## 资源记录配置 
背景知识 
DNS server內的每一个DNS区域都有自己的文件（zone file），ZONE文件由多个记录組成，每一个记录称为资源记录（Resource Record，RR）。当在设置DNS名称解析、反向解析及其他的管理目的时，需要使用不同类型的RR。 
目前支持的资源记录类型包括： 
 
域名服务器记录（NS记录）：用来指定某域名由哪个DNS服务器来进行解析。 
 
主机记录（A记录）：A记录是用于名称解析的重要记录，它将特定的主机名映射到对应主机的IP地址上。 
 
IPv6主机记录（AAAA记录）: 与A记录对应，用于将特定的主机名映射到一个主机的IPv6地址。 
 
服务位置记录（SRV记录）: 用于定义提供特定服务的服务器的位置，如主机，端口等。 
 
NAPTR记录：用来通过正则表达式方式去映射一个域名。 
 
功能描述 
用于配置各种DNS资源记录。 
相关主题 
 
新增DNS服务器资源记录(ADD RR)
 
 
删除DNS服务器资源记录(DEL RR)
 
 
查询DNS服务器资源记录(SHOW RR)
 
 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 新增DNS服务器资源记录(ADD RR) 
### 新增DNS服务器资源记录(ADD RR) 
命令功能 
该命令用于增加DNS资源记录。当用户需要增加DNS资源记录时，使用该命令。配置成功后，可以通过[SHOW RR]查看当前已经配置的DNS资源记录。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|ZONE名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|用于标识资源记录所在的DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图名称，用于标识DNS区域所在的视图。
DOMAIN|域名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|用于描述资源记录的域名称。
TYPE|类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|资源记录的类型，需要根据不同场景使用。目前支持的资源记录类型包括：域名服务器记录（NS记录）：用来指定某域名由哪个DNS服务器来进行解析。主机记录（A记录）：A记录是用于名称解析的重要记录，它将特定的主机名映射到对应主机的IP地址上。IPv6主机记录（AAAA记录）：与A记录对应，用于将特定的主机名映射到一个主机的IPv6地址。服务位置记录（SRV记录）：用于定义提供特定服务的服务器的位置，如主机，端口等。NAPTR记录：用来通过正则表达式方式去映射一个域名。
IP|IP地址|参数可选性:任选参数；参数类型:地址|用于描述域名对应的IP地址，本参数仅用于类型为A或者AAAA的资源记录。
ORDER|Order|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|用于给出处理顺序，按照oder从小到大的顺序对记录搜索，搜索到匹配的记录后，就停止搜索order值更大的记录。本参数仅用于类型为NAPTR的资源记录。
PREF|Preference|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|用于给出在同一个order下各记录的偏好（或权重），值越小偏好越高，pref和order的不同之处在于，order具有唯一性，用户只可以处理某一个order值，而pref表达的是偏好，用户可以对多个不同pref进行综合考虑。本参数仅用于类型为NAPTR的资源记录。
FLAGS|Flags|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Flags为[A-Z0-9]中的一个字符，表达映射关系及记录本身的含义，目前有S”,“A”标志，“S”和“A”是终结标志，即下一步不需要再进行NAPTR查询，“A”表示下一步进行A，AAAA或者A6查询，“S”表示下一步进行SRV查询，如果flags为空（即什么字符也没有），表示用户需要根据本次输出，再进行一次NAPTR查询。本参数仅用于类型为NAPTR的资源记录。
SERVICE|Service|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于给出新目标（即映射后的新域名或URI）上的服务，以及和该服务交互所使用的协议，其形式为[protocol]*(“+” service)，如果flags中的标志为终结标志时，protocol就必须填写。本参数仅用于类型为NAPTR的资源记录。
REPLACEMENT|Replacement|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|在FLAG为空时使用，用于指定再进行一次NAPTR查询时的域名。
PRIORITY|优先级|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|用于给出处理的顺序，按照priority从小到大的顺序对记录搜索，搜索到匹配的记录后，就停止搜索priority值更大的记录，对于拥有相同priority的记录将通过weight再次选择。本参数仅用于类型为SRV的资源记录。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|用于对于拥有相同priority的多条记录，weight给出了选择某条记录的几率，值越大，被选中的概率就越大，合理的取值范围为0-65535。本参数仅用于类型为SRV的资源记录。
PORT|端口|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|用于描述目标机器提供对应服务的端口。本参数仅用于类型为SRV的资源记录。
TARGET|目标|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于描述目标机器的域名。本参数仅用于类型为SRV或者NS的资源记录。
命令举例 
增加DNS资源记录，指定视图名称为"zte"，区域为"hb.node.epc.mnc000.mcc460.3gppnetwork.org"，资源记录类型为"A"，域名为"wh.hb.node.epc.mnc000.mcc460.3gppnetwork.org."，IP地址为"223.103.20.96"。  
ADD RR:ZONE="hb.node.epc.mnc000.mcc460.3gppnetwork.org", VIEWNAME="zte",TYPE=A,DOMAIN="wh.hb.node.epc.mnc000.mcc460.3gppnetwork.org.", IP="223.103.20.96"; 
父主题： [资源记录配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 删除DNS服务器资源记录(DEL RR) 
### 删除DNS服务器资源记录(DEL RR) 
命令功能 
该命令用于删除DNS资源记录。当用户不再需要某条DNS资源记录时，使用该命令删除该资源记录。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|ZONE名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|用于标识资源记录所在的DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图名称，用于标识DNS区域所在的视图。
DOMAIN|域名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~100个字符。|用于描述资源记录的域名称。
TYPE|类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|资源记录的类型，需要根据不同场景使用。目前支持的资源记录类型包括：域名服务器记录（NS记录）：用来指定某域名由哪个DNS服务器来进行解析。主机记录（A记录）：A记录是用于名称解析的重要记录，它将特定的主机名映射到对应主机的IP地址上。IPv6主机记录（AAAA记录）：与A记录对应，用于将特定的主机名映射到一个主机的IPv6地址。服务位置记录（SRV记录）：用于定义提供特定服务的服务器的位置，如主机，端口等。NAPTR记录：用来通过正则表达式方式去映射一个域名。
IP|IP地址|参数可选性:任选参数；参数类型:地址|用于描述域名对应的IP地址，本参数仅用于类型为A或者AAAA的资源记录。
SERVICE|Service|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|用于给出新目标（即映射后的新域名或URI）上的服务，以及和该服务交互所使用的协议，其形式为[protocol]*(“+” service)，如果flags中的标志为终结标志时，protocol就必须填写。本参数仅用于类型为NAPTR的资源记录。
REPLACEMENT|Replacement|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|在FLAG为空时使用，用于指定再进行一次NAPTR查询时的域名。
TARGET|目标|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于描述目标机器的域名。本参数仅用于类型为SRV或者NS的资源记录。
命令举例 
删除一条资源记录，其视图名称为"zte"，区域为"hb.node.epc.mnc000.mcc460.3gppnetwork.org"，资源记录类型为"A"，域名为"wh.hb.node.epc.mnc000.mcc460.3gppnetwork.org."。  
DEL RR:ZONE="hb.node.epc.mnc000.mcc460.3gppnetwork.org", VIEWNAME="zte",TYPE=A,DOMAIN="wh.hb.node.epc.mnc000.mcc460.3gppnetwork.org."; 
父主题： [资源记录配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
### 查询DNS服务器资源记录(SHOW RR) 
### 查询DNS服务器资源记录(SHOW RR) 
命令功能 
该命令用于查询DNS资源记录。当用户需要查看已经配置的DNS资源记录时使用该命令。 
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|ZONE名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于标识资源记录所在的DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|DNS视图名称，用于标识DNS区域所在的视图。
DOMAIN|域名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|用于描述资源记录的域名称。
TYPE|类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|资源记录的类型，需要根据不同场景使用。目前支持的资源记录类型包括：域名服务器记录（NS记录）：用来指定某域名由哪个DNS服务器来进行解析。主机记录（A记录）：A记录是用于名称解析的重要记录，它将特定的主机名映射到对应主机的IP地址上。IPv6主机记录（AAAA记录）：与A记录对应，用于将特定的主机名映射到一个主机的IPv6地址。服务位置记录（SRV记录）：用于定义提供特定服务的服务器的位置，如主机，端口等。NAPTR记录：用来通过正则表达式方式去映射一个域名。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ZONE|ZONE名称|参数可选性:任选参数；参数类型:字符型。|用于标识资源记录所在的DNS区域名称，如果未划分不同视图，则唯一标识一个DNS区域；否则，DNS区域与DNS视图一起唯一确定一个DNS区域。
VIEW|视图名称|参数可选性:任选参数；参数类型:字符型。|DNS视图名称，用于标识DNS区域所在的视图。
DOMAIN|域名称|参数可选性:任选参数；参数类型:字符型。|用于描述资源记录的域名称。
TYPE|类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|资源记录的类型，需要根据不同场景使用。目前支持的资源记录类型包括：域名服务器记录（NS记录）：用来指定某域名由哪个DNS服务器来进行解析。主机记录（A记录）：A记录是用于名称解析的重要记录，它将特定的主机名映射到对应主机的IP地址上。IPv6主机记录（AAAA记录）：与A记录对应，用于将特定的主机名映射到一个主机的IPv6地址。服务位置记录（SRV记录）：用于定义提供特定服务的服务器的位置，如主机，端口等。NAPTR记录：用来通过正则表达式方式去映射一个域名。
IP|IP地址|参数可选性:任选参数；参数类型:地址|用于描述域名对应的IP地址，本参数仅用于类型为A或者AAAA的资源记录。
ORDER|Order|参数可选性:任选参数；参数类型:整数。|用于给出处理顺序，按照oder从小到大的顺序对记录搜索，搜索到匹配的记录后，就停止搜索order值更大的记录。本参数仅用于类型为NAPTR的资源记录。
PREF|Preference|参数可选性:任选参数；参数类型:整数。|用于给出在同一个order下各记录的偏好（或权重），值越小偏好越高，pref和order的不同之处在于，order具有唯一性，用户只可以处理某一个order值，而pref表达的是偏好，用户可以对多个不同pref进行综合考虑。本参数仅用于类型为NAPTR的资源记录。
FLAGS|Flags|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|Flags为[A-Z0-9]中的一个字符，表达映射关系及记录本身的含义，目前有S”,“A”标志，“S”和“A”是终结标志，即下一步不需要再进行NAPTR查询，“A”表示下一步进行A，AAAA或者A6查询，“S”表示下一步进行SRV查询，如果flags为空（即什么字符也没有），表示用户需要根据本次输出，再进行一次NAPTR查询。本参数仅用于类型为NAPTR的资源记录。
SERVICE|Service|参数可选性:任选参数；参数类型:字符型。|用于给出新目标（即映射后的新域名或URI）上的服务，以及和该服务交互所使用的协议，其形式为[protocol]*(“+” service)，如果flags中的标志为终结标志时，protocol就必须填写。本参数仅用于类型为NAPTR的资源记录。
REPLACEMENT|Replacement|参数可选性:任选参数；参数类型:字符型。|在FLAG为空时使用，用于指定再进行一次NAPTR查询时的域名。
PRIORITY|优先级|参数可选性:任选参数；参数类型:整数。|用于给出处理的顺序，按照priority从小到大的顺序对记录搜索，搜索到匹配的记录后，就停止搜索priority值更大的记录，对于拥有相同priority的记录将通过weight再次选择。本参数仅用于类型为SRV的资源记录。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数。|用于对于拥有相同priority的多条记录，weight给出了选择某条记录的几率，值越大，被选中的概率就越大，合理的取值范围为0-65535。本参数仅用于类型为SRV的资源记录。
PORT|端口|参数可选性:任选参数；参数类型:整数。|用于描述目标机器提供对应服务的端口。本参数仅用于类型为SRV的资源记录。
TARGET|目标|参数可选性:任选参数；参数类型:字符型。|用于描述目标机器的域名。本参数仅用于类型为SRV或者NS的资源记录。
命令举例 
查询全部类型为NAPTR的DNS资源记录。  
SHOW RR:TYPE="NAPTR"; 
`
命令 (No.1): SHOW RR:TYPE="NAPTR";
ZONE名称                                           视图名称   域名称              类型    IP地址   Order   Preference   Flags   Service                              正则表达式   Replacement                                                               优先级   权重    端口    目标
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tac.epc.mnc000.mcc460.3gppnetwork.org                         tac-lb00.tac-hb73   NAPTR            100     10           S       x-3gpp-sgw:x-s5-gtp:x-s8-gtp:x-s11                sgw-list-3.cs.hn.node.epc.mnc000.mcc460.3gppnetwork.org.                                           
tac.epc.mnc000.mcc460.3gppnetwork.org                         tac-lb0E.tac-hb74   NAPTR            100     10           A       x-3gpp-mme:x-s10                                  topoff.mme-s10.mmecF4.mmegi0343.mme.epc.mnc000.mcc460.3gppnetwork.org.                             
tac.epc.mnc000.mcc460.3gppnetwork.org                         tac-lb85.tac-hb74   NAPTR            100     10           A       x-3gpp-mme:x-s10                                  topoff.mme-s10.mmecE6.mmegi0342.mme.epc.mnc000.mcc460.3gppnetwork.org.                             
tac.epc.mnc000.mcc460.3gppnetwork.org                         tac-lb85.tac-hb74   NAPTR            100     10           A       x-3gpp-mme:x-s10                                  topoff.mme-s10.mmecE8.mmegi0342.mme.epc.mnc000.mcc460.3gppnetwork.org.                             
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 4
命令执行成功（耗时 1.15 秒）。
` 
父主题： [资源记录配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 进入DNS模式(ENTER DNS) 
## 进入DNS模式(ENTER DNS) 
命令功能 
该命令用于进入DNS模式，当需要进行DNS服务器配置时，使用该命令。 
命令执行成功后，配置模式切换为DNS模式，在该模式下可以执行DNS的数据配置，后续ZXUN uMAC作为DNS客户端从DNS服务器获取相关的配置数据，用此刷新本地网管的配置数据。 
注意事项 
执行DNS服务器配置命令，需要先进入DNS模式。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|服务器编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|用于表示被操作的DNS服务器编号。
命令举例 
进入DNS模式，DNS服务器编号为1。 
ENTER DNS:ID=1; 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 退出DNS模式(EXIT DNS) 
## 退出DNS模式(EXIT DNS) 
命令功能 
该命令用于退出当前DNS模式，当操作员不再需要配置DNS相关数据时，使用该命令。 
命令执行成功后，配置模式由DNS模式切换到普通模式。 
注意事项 
该命令在用户需要退出DNS配置模式，返回普通模式时候使用。 
命令举例 
退出DNS模式。 
EXIT DNS; 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 备份DNS服务器数据(BACKUP DNS) 
## 备份DNS服务器数据(BACKUP DNS) 
命令功能 
该命令用于对指定的DNS服务器进行备份。
注意事项 
 
备份操作时，输出的备份文件可以存储在本地磁盘和FTP/SFTP服务器上。
 
 
备份操作完成对指定的DNS服务器DNS配置文件的备份，最终输出一个zip压缩格式的备份文件。
 
 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|服务器编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|用于表示被操作的DNS服务器编号。
OUTPUTTYPE|备份输出类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:DISK。|该参数用于设置备份文件的保存位置：FTP_OR_SFTP：备份文件保存到FTP/SFTP服务器上。DISK：备份文件保存到本地磁盘上。
OUTPUTPATH|备份输出路径|参数可选性:必选参数；参数类型:字符型；参数范围为:1~255个字符。|对于输出到服务器磁盘（备份输出类型：DISK），为服务器磁盘的绝对目录。对于输出到FTP/SFTP服务器（备份输出类型：FTP_OR_SFTP），则为URL格式的FTP/SFTP服务器目录，例如：ftp://10.0.0.35/backup/。
FILENAME|备份文件名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~128个字符。|不需要添加文件扩展名，系统会自动添加扩展名（.zip），若不输入则系统默认为：<DNS服务器编号>_<DNS服务器IP地址>_<DNS服务器用户别名>_<时间戳>。
USERNAME|FTP/SFTP用户名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|对于输出到FTP/SFTP服务器（备份输出类型：FTP_OR_SFTP），则输入FTP/SFTP服务器的用户名。
PASSWORD|FTP/SFTP用户密码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|对于输出到FTP/SFTP服务器（备份输出类型：FTP_OR_SFTP），则输入FTP/SFTP服务器的用户密码。
命令举例 
备份DNS服务器数据，DNS服务器编号是1，备份输出路径是/home，备份文件名称是backbind1.zip。 
BACKUP DNS:ID=1,OUTPUTPATH="/home",FILENAME="backbind1.zip"; 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 恢复DNS服务器数据(RESTORE DNS) 
## 恢复DNS服务器数据(RESTORE DNS) 
命令功能 
该命令用于对指定的备份文件进行恢复。
注意事项 
无。 
参数说明 
标识|名称|类型|说明
---|---|---|---
ID|服务器编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~255。|用于表示被操作的DNS服务器编号。
FILENAME|服务器备份文件全路径|参数可选性:必选参数；参数类型:字符型；参数范围为:1~128个字符。|对于服务器磁盘（备份输入类型：DISK），则备份文件来自服务器磁盘；对于FTP/SFTP服务器（备份输入类型：FTP_OR_SFTP），则来自FTP/SFTP服务器，例如：ftp://10.0.0.35/backup/comm_all.zip。
INPUTTYPE|备份输入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:DISK。|备份文件来源:FTP_OR_SFTP：备份文件来源于FTP/SFTP服务器。DISK：备份文件来源于本地磁盘。
USERNAME|FTP/SFTP用户名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|对于输出到FTP/SFTP服务器（备份输出类型：FTP_OR_SFTP），则输入FTP/SFTP服务器的用户名。
PASSWORD|FTP/SFTP用户密码|参数可选性:任选参数；参数类型:字符型；参数范围为:1~50个字符。|对于输出到FTP/SFTP服务器（备份输出类型：FTP_OR_SFTP），则输入FTP/SFTP服务器的用户密码。
命令举例 
恢复DNS服务器数据，DNS服务器编号为1，服务器备份文件全路径为/home/backbind1.zip。 
RESTORE DNS:ID=1,FILENAME="/home/backbind1.zip"; 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 刷新DNS服务器数据到本地数据库(REFRESH LOCALDNS) 
## 刷新DNS服务器数据到本地数据库(REFRESH LOCALDNS) 
命令功能 
该命令用于强制更新OMM网管的DNS配置数据，当ZXUN uMAC需要从DNS服务器重新下载配置数据时，使用该命令。 
命令执行成功后，OMM网管从DNS服务器下载配置数据并刷新本地的网管配置数据。 
注意事项 
当配置DNS服务器数据后未同步到DNS服务器即退出后，下次进入DNS模式网管配置数据将会保留。如果用户需要重新以DNS服务器配置为准进行配置，需要执行刷新DNS服务器数据到本地数据库命令。 
命令举例 
刷新DNS服务器数据到本地数据库命令。 
REFRESH LOCALDNS; 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 同步DNS服务器配置(SYN DNS) 
## 同步DNS服务器配置(SYN DNS) 
命令功能 
该命令用于将本地OMM网管保存的DNS服务器配置数据同步到DNS服务器，当需要将本地OMM网管配置的DNS数据上传到DNS服务器时，使用该命令。 
命令执行成功后，DNS服务器的配置数据文件将被刷新。 
注意事项 
用户在退出DNS模式前需要先使用该命令，否则用户配置的数据不会上传到DNS服务器生效。下次进入DNS配置模式时，将会重新加载DNS服务器上的数据，即网管上原来的配置数据将会被覆盖。 
命令举例 
同步网管DNS配置数据到DNS服务器。 
SYN DNS; 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 强制退出DNS模式(EXIT DNS FORCE) 
## 强制退出DNS模式(EXIT DNS FORCE) 
命令功能 
该命令用于强制退出DNS模式，当某个操作员使用DNS模式后没有退出而其他操作员需要配置DNS服务器数据时，使用该命令。 
命令执行成功后，配置模式将由DNS模式切换到普通模式。 
注意事项 
该命令仅允许ADMIN用户执行。 
命令举例 
强制退出DNS模式。 
EXIT DNS FORCE; 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 重新加载DNS服务器(RELOAD DNS) 
## 重新加载DNS服务器(RELOAD DNS) 
命令功能 
该命令用于重新加载DNS服务器的配置数据，当操作员在本地OMM网管修改DNS数据并且同步到DNS服务器，使配置数据生效时，使用该命令。 
命令执行成功后，DNS服务器重新加载配置文件，本地OMM网管的修改的数据生效。 
注意事项 
该命令将配置更改正式生效，执行前请检查数据正确性。 
命令举例 
重新加载DNS服务器配置文件。 
RELOAD DNS; 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询DNS服务器版本(SHOW DNS SERVER VERSION) 
## 查询DNS服务器版本(SHOW DNS SERVER VERSION) 
命令功能 
该命令用于查询当前DNS服务器的版本。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
VERSION|版本信息|参数可选性:任选参数；参数类型:字符型；参数范围为:0~10240个字符。|DNS服务器版本的详细信息。
命令举例 
查询DNS服务器版本。  
SHOW DNS SERVER VERSION; 
`
命令 (No.1): SHOW DNS SERVER VERSION
版本信息 
-----------
V5.17.10.B2 
-----------
记录数 1
命令执行成功（耗时 0.306 秒）。
` 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
## 查询DNS服务器主从状态(SHOW DNS SERVER STATE) 
## 查询DNS服务器主从状态(SHOW DNS SERVER STATE) 
命令功能 
该命令用于查询DNS服务器的主从状态。
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ISLEADER|是否为主节点|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|DNS服务器主从状态。是：主节点。否：从节点。
命令举例 
查询DNS服务器主从状态。  
SHOW DNS SERVER STATE; 
`
命令 (No.1): SHOW DNS SERVER STATE
是否为主节点 
---------------
否 
---------------
记录数 1
命令执行成功（耗时 0.235 秒）。
` 
父主题： [DNS服务器配置]
Copyright © ZTE Corporation. All right reserved. 
PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 
