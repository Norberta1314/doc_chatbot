 增强功能 


背景知识 


3GPP协议中，规定了对不同的网络运营过程中可以根据实际情况配置不同的参数，以及运营商可以针对网络配置一些定制功能。 




功能说明 


增强功能提供了NAS原因值转换，特定VenderSpec以及消息参数的等配置。 




子主题： 






# NAS原因值映射 
# NAS原因值映射 


背景知识 


3GPP 协议规定多个NAS原因值，在实际的运营中，不同运营商可以根据实际情况，要求失败场景时和NAS原因值之间建立不同的映射关系。 




功能说明 


本功能用于根据运营商的实际需要配置失败场景到NAS的失败原因值，两者之间的映射关系。 




子主题： 






## Nausf 原因值映射配置 
## Nausf 原因值映射配置 


背景知识 


当网络侧NF之间进行交互时，如果应用程序发生错误，NF之间会通过HTTP层的HTTP状态码（HTTP status code）来指示错误原因，参见协议3GPP TS 29500 5.2.7章节。应用层还会通过应用层ProblemDetails结构数据中的Cause值来指示更详细的错误原因，参见协议3GPP TS 29571 5.2.4.1 Type: ProblemDetails。 

当终端发起移动性的流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因。并且终端根据Cause值，可以触发后续相应行为。 

在5GC的移动性管理中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议24501 Annex A: Cause values for 5GS mobility management。 

AMF与其他NF交互时，AMF需要把其他NF返回的失败原因转换为5GMM原因，发送给UE，以引导UE进行合理的后续行为。参考协议3GPP TS 29.524。 




功能说明 


当AMF和AUSF交互时，AMF使用AUSF返回的失败原因，通过配置转换为5GMM原因值通知UE。AUSF返回的失败原因包括HTTP层的HTTP状态码（HTTP status code）和应用层的错误码（Application error）。 




子主题： 






### 新增Nausf原因值映射配置(ADD AUSFCAUSEMAPPINGCFG) 
### 新增Nausf原因值映射配置(ADD AUSFCAUSEMAPPINGCFG) 


功能说明 

该命令用于新增Nausf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，映射出唯一的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息（AuthInformation Ack、EapSesssion Ack、AuthConfirm Ack等）中的状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息中的应用层详细错误原因。
ausfMMCause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|根据AUSF返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息（AuthInformation Ack、EapSesssion Ack、AuthConfirm Ack等）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息中的应用层详细错误原因。
ausfMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据AUSF返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
新增一个Nausf原因值映射配置，其中HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”，对应的5GMM Cause为“3 - Illegal UE”。
ADD AUSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",AUSFMMCAUSE="ILLEGALUE"
` 


### 修改Nausf原因值映射配置(SET AUSFCAUSEMAPPINGCFG) 
### 修改Nausf原因值映射配置(SET AUSFCAUSEMAPPINGCFG) 


功能说明 

该命令用于修改Nausf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，修改对应的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息（AuthInformation Ack、EapSesssion Ack、AuthConfirm Ack等）中的状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息中的应用层详细错误原因。
ausfMMCause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|根据AUSF返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息（AuthInformation Ack、EapSesssion Ack、AuthConfirm Ack等）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息中的应用层详细错误原因。
ausfMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据AUSF返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
修改一个Nausf原因值映射配置，将HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”对应的5GMM Cause修改为“5 - PEI not accepted”。
SET AUSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",AUSFMMCAUSE="PEINOTALLOWED"
` 


### 删除Nausf原因值映射配置(DEL AUSFCAUSEMAPPINGCFG) 
### 删除Nausf原因值映射配置(DEL AUSFCAUSEMAPPINGCFG) 


功能说明 

该命令用于删除Nausf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，删除对应的5GMM Cause。 


注意事项 

本配置存在默认记录。如果配置人员需要删除这些默认记录，那么AMF不保证后期映射原因值的合理性。当无法正确检索到原因值时，会统一使用“111 - Protocol error, unspecified” 。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息（AuthInformation Ack、EapSesssion Ack、AuthConfirm Ack等）中的状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息中的应用层详细错误原因。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息（AuthInformation Ack、EapSesssion Ack、AuthConfirm Ack等）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息中的应用层详细错误原因。
ausfMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据AUSF返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
删除一个Nausf原因值映射配置，将HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”对应的5GMM Cause映射配置删除。
DEL AUSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN"
` 


### 查询Nausf原因值映射配置(SHOW AUSFCAUSEMAPPINGCFG) 
### 查询Nausf原因值映射配置(SHOW AUSFCAUSEMAPPINGCFG) 


功能说明 

该命令用于查询Nausf原因值映射配置。支持单索引、全部查询等方式。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息（AuthInformation Ack、EapSesssion Ack、AuthConfirm Ack等）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息中的应用层详细错误原因。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息（AuthInformation Ack、EapSesssion Ack、AuthConfirm Ack等）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端AUSF返回给AMF的HTTP响应消息中的应用层详细错误原因。
ausfMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据AUSF返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
查询HTTP状态码为“403 Forbidden”对应的Nausf原因值映射配置。
SHOW AUSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_403"

(No.1) : SHOW AUSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_403"
-----------------Namf_Communication_0_A----------------
HTTP状态码           应用层错误码                       5GMM 原因值                                 计数归类 
403 Forbidden  SERVING_NETWORK_NOT_AUTHORIZED     11 - PLMN not allowed
403 Forbidden  AUTHENTICATION_REJECTED            15 - No suitable cells in tracking area
403 Forbidden  INVALID_HN_PUBLIC_KEY_IDENTIFIER   111 - Protocol error, unspecified
403 Forbidden  INVALID_SCHEME_OUTPUT              111 - Protocol error, unspecified

` 


## 基于SUPI号段的Nausf原因值映射配置 
## 基于SUPI号段的Nausf原因值映射配置 


背景知识 


当网络侧NF之间进行交互时，如果应用程序发生错误时，NF之间会通过HTTP层的HTTP状态码（HTTP status code）来指示错误原因，参见协议3GPP TS 29500 5.2.7章节。应用层还会通过应用层ProblemDetails结构数据中的Cause值来指示更详细的错误原因，参见协议3GPP TS 29571 5.2.4.1 Type: ProblemDetails。 

当终端发起移动性流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因。并且终端根据Cause值，可以触发后续相应行为。 

在5GC的移动性管理中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议3GPP TS 24501 Annex A: Cause values for 5GS mobility management。 

AMF与其他NF交互时，AMF需要把其他NF返回的失败原因转换为5GMM原因，发送给UE，以引导UE进行合理的后续行为。参见协议3GPP TS 29.524。 




功能说明 


该节点用于配置当AMF和AUSF交互时，AMF使用AUSF返回的失败原因，通过配置转换为5GMM原因通知UE。AUSF返回的失败原因包括HTTP层的HTTP状态码（HTTP status code）和应用层的错误码（Application error）。 

AMF支持按SUPI号段进行AUSF失败原因映射5GMM原因配置，以便灵活地针对不同SUPI号段提供差异化的映射配置，即“基于SUPI号段的Nausf原因值映射配置”。通过提供该配置，针对相同的AUSF返回的失败原因，AMF能够做不同的配置映射5GMM原因，可以灵活的引导不同号段的UE进行对应的合理行为。 

AMF优先使用基于SUPI号段的Nausf原因值映射配置，当没有匹配到基于SUPI号段的Nausf原因值映射数据时，AMF采用全局的Nausf原因值映射配置。 

基于SUPI号段的Nausf原因值映射配置，系统按最长匹配进行。匹配到最长号段后，这个号段的所有失败原因映射都应在最长号段下规划配置，不应该再到其他短号段下或者全局的原因映射下配置。不允许规划部分失败映射在长号段中配置，部分失败映射在短号段中或者全局配置的情形，如果配置到短号段中或者全局配置中，系统按匹配不到处理。 




子主题： 






### 新增基于SUPI号段的Nausf原因值映射配置(ADD AUSFCAUSEMAPPINGCFGBYSUPI) 
### 新增基于SUPI号段的Nausf原因值映射配置(ADD AUSFCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于新增基于SUPI号段的Nausf原因值映射配置。可通过“SUPI号段+HTTP状态码+应用层错误码”的组合，映射出唯一的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如：403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如：CONTEXT_NOT_FOUND，代表上下文不存在。
ausfMMCause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因。例如：Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如：403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如：CONTEXT_NOT_FOUND，代表上下文不存在。
ausfMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因。例如：Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
新增一个基于SUPI号段的Nausf原因值映射配置，其中，SUPI号段为“46011”，HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”，对应的5GMM Cause为“3 - Illegal UE”的映射配置。
ADD AUSFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",AUSFMMCAUSE="ILLEGALUE"
` 


### 修改基于SUPI号段的Nausf原因值映射配置(SET AUSFCAUSEMAPPINGCFGBYSUPI) 
### 修改基于SUPI号段的Nausf原因值映射配置(SET AUSFCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于修改基于SUPI号段的Nausf原因值映射配置。可通过“SUPI号段+HTTP状态码+应用层错误码”的组合，修改对应的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如：403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如：CONTEXT_NOT_FOUND，代表上下文不存在。
ausfMMCause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因。例如：Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如：403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如：CONTEXT_NOT_FOUND，代表上下文不存在。
ausfMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因。例如：Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
修改一个基于SUPI号段的Nausf原因值映射配置，其中，SUPI号段为“46011”，HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”，将对应的5GMM Cause修改为“5 - PEI not accepted”。
SET AUSFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",AUSFMMCAUSE="PEINOTALLOWED"
` 


### 删除基于SUPI号段的Nausf原因值映射配置(DEL AUSFCAUSEMAPPINGCFGBYSUPI) 
### 删除基于SUPI号段的Nausf原因值映射配置(DEL AUSFCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于删除基于SUPI号段的Nausf原因值映射配置。可通过“SUPI号段+HTTP状态码+应用层错误码”的组合，删除对应的5GMM Cause配置。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如：403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如：CONTEXT_NOT_FOUND，代表上下文不存在。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如：403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如：CONTEXT_NOT_FOUND，代表上下文不存在。
ausfMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因。例如：Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
删除一个基于SUPI号段的Nausf原因值映射配置，其中，SUPI号段为“46011”，HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”，删除其对应的5GMM Cause映射配置。
DEL AUSFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN"
` 


### 查询基于SUPI号段的Nausf原因值映射配置(SHOW AUSFCAUSEMAPPINGCFGBYSUPI) 
### 查询基于SUPI号段的Nausf原因值映射配置(SHOW AUSFCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于查询基于SUPI号段的Nausf原因值映射配置。支持单索引、全部查询等方式。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如：403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如：CONTEXT_NOT_FOUND，代表上下文不存在。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如：403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如：CONTEXT_NOT_FOUND，代表上下文不存在。
ausfMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因。例如：Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
查询基于SUPI号段的Nausf原因值映射配置。
SHOW AUSFCAUSEMAPPINGCFGBYSUPI

(No.4) : SHOW AUSFCAUSEMAPPINGCFGBYSUPI:
-----------------Namf_Communication_0----------------
SUPI号段    HTTP状态码                  应用层错误码                  5GMM 原因值          计数归类 
 46011      100 Continue           NF_CONSUMER_REDIRECT_ONE_TXN    3 - Illegal UE    
记录数：1
命令执行成功（耗时 0.031 秒）。

` 


## Nudm 原因值映射配置 
## Nudm 原因值映射配置 


背景知识 


当网络侧NF之间进行交互时，如果应用程序发生错误时，NF之间会通过ProblemDetails结构数据中的Cause值来传递错误原因，参见协议3GPP TS 23571 5.2.4.1 Type: ProblemDetails。 

当终端发起移动性的流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因。并且终端根据Cause值，可以触发后续相应行为。 

在5GC的移动性管理中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议24501 Annex A: Cause values for 5GS mobility management 




功能说明 


本功能用于在终端移动性流程中，将其他NF返回给AMF的失败ProblemDetails结构数据类型中Cause，映射到5G移动性管理的Cause，并与投递给终端。 




子主题： 






### 新增Nudm原因值映射配置(ADD UDMCAUSEMAPPINGCFG) 
### 新增Nudm原因值映射配置(ADD UDMCAUSEMAPPINGCFG) 


功能说明 

该命令用于新增当AMF和UDM交互时，AMF可以把UDM返回的失败原因（Cause）转换为5GC网络的移动性管理（Mobility Management）失败原因（Cause）。 

可通过“HTTP状态码+应用层错误码”的组合，映射出唯一的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AMF的HTTP状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AM的应用层详细错误原因
udmMMCause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|本参数用于配置AMF根据HTTP状态码和应用层错误码映射的5GC网络的移动性管理（Mobility Management）失败原因（Cause）。该原因值指示了为何来自UE的5GC网络的移动性管理请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AMF的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AM的应用层详细错误原因
udmMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置AMF根据HTTP状态码和应用层错误码映射的5GC网络的移动性管理（Mobility Management）失败原因（Cause）。该原因值指示了为何来自UE的5GC网络的移动性管理请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
新增一个HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”的5GMM Cause为“3 - Illegal UE”的映射配置。
ADD UDMCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",UDMMMCAUSE="ILLEGALUE"
` 


### 修改Nudm原因值映射配置(SET UDMCAUSEMAPPINGCFG) 
### 修改Nudm原因值映射配置(SET UDMCAUSEMAPPINGCFG) 


功能说明 

该命令用于修改UDM返回的失败原因（Cause）转换为5GC网络的移动性管理（Mobility Management）失败原因（Cause）配置数据。可通过“HTTP状态码+应用层错误码”的组合，修改5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AMF的HTTP状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AM的应用层详细错误原因
udmMMCause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|本参数用于配置AMF根据HTTP状态码和应用层错误码映射的5GC网络的移动性管理（Mobility Management）失败原因（Cause）。该原因值指示了为何来自UE的5GC网络的移动性管理请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AMF的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AM的应用层详细错误原因
udmMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置AMF根据HTTP状态码和应用层错误码映射的5GC网络的移动性管理（Mobility Management）失败原因（Cause）。该原因值指示了为何来自UE的5GC网络的移动性管理请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
将HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”的5GMM Cause修改为“5 - PEI not accepted”。
SET UDMCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",UDMMMCAUSE="PEINOTALLOWED"
` 


### 删除Nudm原因值映射配置(DEL UDMCAUSEMAPPINGCFG) 
### 删除Nudm原因值映射配置(DEL UDMCAUSEMAPPINGCFG) 


功能说明 

该命令用于删除UDM返回的失败原因（Cause）转换为5GC网络的移动性管理（Mobility Management）失败原因（Cause）配置数据。可通过“HTTP状态码+应用层错误码”的组合，删除5GMM Cause。 


注意事项 

本命令存在默认配置记录。如果操作人员需要删除这些默认配置记录，那么AMF无法保证后期映射原因值的合理性。 

当AMF无法正确检索到对应的原因值时，会统一使用111 - Protocol error, unspecified来表示Cause。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AMF的HTTP状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AM的应用层详细错误原因




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AMF的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AM的应用层详细错误原因
udmMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置AMF根据HTTP状态码和应用层错误码映射的5GC网络的移动性管理（Mobility Management）失败原因（Cause）。该原因值指示了为何来自UE的5GC网络的移动性管理请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
删除一个HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”的5GMM Cause的映射配置。
DEL UDMCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN"
` 


### 查询Nudm原因值映射配置(SHOW UDMCAUSEMAPPINGCFG) 
### 查询Nudm原因值映射配置(SHOW UDMCAUSEMAPPINGCFG) 


功能说明 

该命令用于查询UDM返回的失败原因（Cause）转换为5GC网络的移动性管理（Mobility Management）失败原因（Cause）配置数据。支持单索引、全部查询等方式。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AMF的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AM的应用层详细错误原因




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AMF的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置UDM返回给AM的应用层详细错误原因
udmMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|本参数用于配置AMF根据HTTP状态码和应用层错误码映射的5GC网络的移动性管理（Mobility Management）失败原因（Cause）。该原因值指示了为何来自UE的5GC网络的移动性管理请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
查询Nudm原因值映射配置数据。
SHOW UDMCAUSEMAPPINGCFG

(No.1) : SHOW UDMCAUSEMAPPINGCFG:
-----------------Namf_Communication_0_A----------------
HTTP状态码                              应用层错误码                             5GMM 原因值             计数归类 
403 Forbidden                          UNKNOWN_5GS_SUBSCRIPTION          27 - N1 mode not allowed

记录数：1

执行成功开始时间:2020-06-19 10:57:14 耗时: 0.732 秒

` 


## 基于SUPI号段的Nudm原因值映射配置 
## 基于SUPI号段的Nudm原因值映射配置 


背景知识 


当网络侧NF之间进行交互时，如果应用程序发生错误时，NF之间会通过HTTP层的HTTP状态码（HTTP status code）来指示错误原因，参见协议3GPP TS 29500 5.2.7章节。应用层还会通过应用层ProblemDetails结构数据中的Cause值来指示更详细的错误原因，参见协议3GPP TS 29571 5.2.4.1 Type: ProblemDetails。 

当终端发起移动性的流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因。并且终端根据Cause值，可以触发后续相应行为。 

在5GC的移动性管理中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议24501 Annex A: Cause values for 5GS mobility management 

AMF与其他NF交互时，AMF需要把其他NF返回的失败原因转换为5GMM原因，发送给UE，以引导UE进行合理的后续行为。参考协议3GPP TS 29.524 




功能说明 


该节点用于配置当AMF和UDM交互时，AMF使用UDM返回的失败原因，通过配置转换为5GMM原因通知UE。UDM返回的失败原因包括HTTP层的HTTP状态码（HTTP status code）和应用层的错误码（Application error）。 

AMF支持按SUPI号段进行UDM失败原因映射5GMM原因配置，以便灵活地针对不同SUPI号段提供差异化的映射配置，即“基于SUPI号段的Nudm原因值映射配置”。通过提供该配置，针对相同的UDM返回的失败原因，AMF能够做不同的配置映射5GMM原因，可以灵活的引导不同号段的UE进行对应的合理行为。 

AMF优先使用基于SUPI号段的Nudm原因值映射配置，当没有匹配到基于SUPI号段的Nudm原因值映射数据时，AMF采用全局的Nudm原因值映射配置。 

基于SUPI号段的Nudm原因值映射配置，系统按最长匹配进行。匹配到最长号段后，这个号段的所有失败原因映射都应在最长号段下规划配置，不应该再到其他短号段下或者全局的原因映射下配置，不允许规划部分失败映射在长号段中配置，部分失败映射在短号段中或者全局配置的情形，配置到短号段中或者全局配置中，系统按匹配不到处理。 




子主题： 






### 新增基于SUPI号段的Nudm原因值映射配置(ADD UDMCAUSEMAPPINGCFGBYSUPI) 
### 新增基于SUPI号段的Nudm原因值映射配置(ADD UDMCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于新增基于SUPI号段的Nudm原因值映射配置。可通过“SUPI号段+HTTP状态码+应用层错误码”的参数组合，映射出唯一的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如CONTEXT_NOT_FOUND，代表上下文不存在。
udmMMCause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因，例如Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如CONTEXT_NOT_FOUND，代表上下文不存在。
udmMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因，例如Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
新增一个SUPI号段为“46011”，HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”的5GMM Cause为“3 - Illegal UE”的映射配置。
ADD UDMCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",UDMMMCAUSE="ILLEGALUE"
` 


### 修改基于SUPI号段的Nudm原因值映射配置(SET UDMCAUSEMAPPINGCFGBYSUPI) 
### 修改基于SUPI号段的Nudm原因值映射配置(SET UDMCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于修改基于SUPI号段的Nudm原因值映射配置。可通过“SUPI号段+HTTP状态码+应用层错误码”的参数组合，修改5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如CONTEXT_NOT_FOUND，代表上下文不存在。
udmMMCause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因，例如Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如CONTEXT_NOT_FOUND，代表上下文不存在。
udmMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因，例如Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
将SUPI号段为“46011”，HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”的5GMM Cause修改为“5 - PEI not accepted”。
SET UDMCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",UDMMMCAUSE="PEINOTALLOWED"
` 


### 删除基于SUPI号段的Nudm原因值映射配置(DEL UDMCAUSEMAPPINGCFGBYSUPI) 
### 删除基于SUPI号段的Nudm原因值映射配置(DEL UDMCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于删除基于SUPI号段的Nudm原因值映射配置。可通过“SUPI号段+HTTP状态码+应用层错误码”的参数组合，删除5GMM Cause配置。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如CONTEXT_NOT_FOUND，代表上下文不存在。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如CONTEXT_NOT_FOUND，代表上下文不存在。
udmMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因，例如Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
删除一个SUPI号段为“46011”，HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”的5GMM Cause的映射配置。
DEL UDMCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN"
` 


### 查询基于SUPI号段的Nudm原因值映射配置(SHOW UDMCAUSEMAPPINGCFGBYSUPI) 
### 查询基于SUPI号段的Nudm原因值映射配置(SHOW UDMCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于查询基于SUPI号段的Nudm原因值映射配置。支持单索引、全部查询等方式。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如CONTEXT_NOT_FOUND，代表上下文不存在。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段，以便灵活地针对不同SUPI号段提供差异化的映射配置。
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的HTTP状态码。例如403 Forbidden，代表服务器收到请求，但是拒绝提供服务。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置对端返回的应用层详细错误原因。例如CONTEXT_NOT_FOUND，代表上下文不存在。
udmMMCause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于设置根据SUPI号段、HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了来自UE的5GMM请求被网络侧拒绝的原因，例如Implicitly de-registered，代表隐式去注册。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
查询基于SUPI号段的Nudm原因值映射配置。
SHOW UDMCAUSEMAPPINGCFGBYSUPI

(No.4) : SHOW UDMCAUSEMAPPINGCFGBYSUPI:
-----------------Namf_Communication_0----------------
SUPI号段   HTTP状态码       应用层错误码                        5GMM 原因值       计数归类 
 46011     100 Continue    NF_CONSUMER_REDIRECT_ONE_TXN       3 - Illegal UE    
记录数：1
命令执行成功（耗时 0.031 秒）

` 


## Nnssf 原因值映射配置 
## Nnssf 原因值映射配置 


背景知识 


当网络侧NF之间进行交互时，如果应用程序发生错误，NF之间会通过HTTP层的HTTP状态码（HTTP status code）来指示错误原因，参见协议3GPP TS 29500 5.2.7章节。应用层还会通过应用层ProblemDetails结构数据中的Cause值来指示更详细的错误原因，参见协议3GPP TS 29571 5.2.4.1 Type: ProblemDetails。 

当终端发起移动性的流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因。并且终端根据Cause值，可以触发后续相应行为。 

在5GC的移动性管理中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议24501 Annex A: Cause values for 5GS mobility management。 

AMF与其他NF交互时，AMF需要把其他NF返回的失败原因转换为5GMM原因，发送给UE，以引导UE进行合理的后续行为。参考协议3GPP TS 29.524。 




功能说明 


当AMF和NSSF交互时，AMF使用NSSF返回的失败原因，通过配置转换为5GMM原因值通知UE。NSSF返回的失败原因包括HTTP层的HTTP状态码（HTTP status code）和应用层的错误码（Application error）。 




子主题： 






### 新增Nnssf原因值映射配置(ADD NSSFCAUSEMAPPINGCFG) 
### 新增Nnssf原因值映射配置(ADD NSSFCAUSEMAPPINGCFG) 


功能说明 

该命令用于新增Nnssf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，映射出唯一的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的应用层详细错误原因。
nssfMMCause|5GMM Cause|参数可选性: 必选参数类型: 枚举，参见枚举定义|根据NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求等）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的应用层详细错误原因。
nssfMMCause|5GMM Cause|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求等）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
新增一个Nnssf原因值映射配置，其中HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”，对应的5GMM Cause为“3 - Illegal UE”。
ADD NSSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",NSSFMMCAUSE="ILLEGALUE"
` 


### 修改Nnssf原因值映射配置(SET NSSFCAUSEMAPPINGCFG) 
### 修改Nnssf原因值映射配置(SET NSSFCAUSEMAPPINGCFG) 


功能说明 

该命令用于修改Nnssf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，修改对应的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的应用层详细错误原因。
nssfMMCause|5GMM Cause|参数可选性: 必选参数类型: 枚举，参见枚举定义|根据NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求等）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的应用层详细错误原因。
nssfMMCause|5GMM Cause|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求等）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
修改一个Nnssf原因值映射配置，将HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”对应的5GMM Cause修改为“5 - PEI not accepted”。
SET NSSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",NSSFMMCAUSE="PEINOTALLOWED"
` 


### 删除Nnssf原因值映射配置(DEL NSSFCAUSEMAPPINGCFG) 
### 删除Nnssf原因值映射配置(DEL NSSFCAUSEMAPPINGCFG) 


功能说明 

该命令用于删除Nnssf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，删除对应的5GMM Cause。 


注意事项 

本配置存在默认记录。如果配置人员需要删除这些默认记录，那么AMF不保证后期映射原因值的合理性。当无法正确检索到原因值时，会统一使用111 - Protocol error, unspecified 。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的应用层详细错误原因。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的应用层详细错误原因。
nssfMMCause|5GMM Cause|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求等）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
删除一个Nnssf原因值映射配置，将HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”对应的5GMM Cause映射配置删除。
DEL NSSFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN"
` 


### 查询Nnssf原因值映射配置(SHOW NSSFCAUSEMAPPINGCFG) 
### 查询Nnssf原因值映射配置(SHOW NSSFCAUSEMAPPINGCFG) 


功能说明 

该命令用于查询Nnssf原因值映射配置。支持单索引、全部查询等方式。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的应用层详细错误原因。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的应用层详细错误原因。
nssfMMCause|5GMM Cause|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据NSSF返回给AMF的HTTP响应消息（切片选择响应Nnssf_NSSelection Ack）中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求等）会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
查询Nnssf原因值映射配置。
SHOW NSSFCAUSEMAPPINGCFG

(No.1) : SHOW NSSFCAUSEMAPPINGCFG:
-----------------Namf_Communication_0_A----------------
HTTP状态码                         应用层错误码            5GMM 原因值                        计数归类     
403 Forbidden                    SNSSAI_NOT_SUPPORTED   62 - No network slices available
Wait HTTP Response Timeout Not   Applicable             111 - Protocol error, unspecified
Any HTTP Status Code             Any Application Error  62 - No network slices available

` 


## Nsmf 原因值映射配置 
## Nsmf 原因值映射配置 


背景知识 


当网络侧NF之间进行交互时，如果应用程序发生错误，NF之间会通过HTTP层的HTTP状态码（HTTP status code）来指示错误原因，参见协议3GPP TS 29500 5.2.7章节。应用层还会通过应用层ProblemDetails结构数据中的Cause值来指示更详细的错误原因，参见协议3GPP TS 29571 5.2.4.1 Type: ProblemDetails。 

当终端发起移动性的流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因。并且终端根据Cause值，可以触发后续相应行为。 

在5GC的移动性管理中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议24501 Annex A: Cause values for 5GS mobility management。 

AMF与其他NF交互时，AMF需要把其他NF返回的失败原因转换为5GMM原因，发送给UE，以引导UE进行合理的后续行为。参考协议3GPP TS 29.524。 




功能说明 


当AMF和SMF交互时，AMF使用SMF返回的失败原因，通过配置转换为5GMM原因值通知UE。SMF返回的失败原因包括HTTP层的HTTP状态码（HTTP status code）和应用层的错误码（Application error）。 




子主题： 






### 新增Nsmf原因值映射配置(ADD SMFCAUSEMAPPINGCFG) 
### 新增Nsmf原因值映射配置(ADD SMFCAUSEMAPPINGCFG) 


功能说明 

该命令用于新增Nsmf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，映射出唯一的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端返回的HTTP状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端返回的应用层详细错误原因。
smfMMCause|5GMM Cause|参数可选性: 必选参数类型: 枚举，参见枚举定义|根据HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了为何来自UE的5GMM请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的应用层详细错误原因。
smfMMCause|5GMM Cause|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了为何来自UE的5GMM请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|




命令举例 


`
新增一个Nsmf原因值映射配置，其中HTTP状态码为“100 Continue”，应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”，对应的5GMM Cause为“3 - Illegal UE”。
ADD SMFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",SMFMMCAUSE="ILLEGALUE"
` 


### 修改Nsmf原因值映射配置(SET SMFCAUSEMAPPINGCFG) 
### 修改Nsmf原因值映射配置(SET SMFCAUSEMAPPINGCFG) 


功能说明 

该命令用于修改Nsmf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，修改对应的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端返回的HTTP状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端返回的应用层详细错误原因。
smfMMCause|5GMM Cause|参数可选性: 必选参数类型: 枚举，参见枚举定义|根据HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了为何来自UE的5GMM请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的应用层详细错误原因。
smfMMCause|5GMM Cause|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了为何来自UE的5GMM请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|




命令举例 


`
修改一个Nsmf原因值映射配置，将HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”对应的5GMM Cause修改为“5 - PEI not accepted”。
SET SMFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",SMFMMCAUSE="PEINOTALLOWED"
` 


### 删除Nsmf原因值映射配置(DEL SMFCAUSEMAPPINGCFG) 
### 删除Nsmf原因值映射配置(DEL SMFCAUSEMAPPINGCFG) 


功能说明 

该命令用于删除Nsmf原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，删除对应的5GMM Cause。 


注意事项 

本配置存在默认记录。如果配置人员需要删除这些默认记录，那么AMF不保证后期映射原因值的合理性。当无法正确检索到原因值时，会统一使用111 - Protocol error, unspecified 。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端返回的HTTP状态码。
applicationError|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|对端返回的应用层详细错误原因。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的应用层详细错误原因。
smfMMCause|5GMM Cause|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了为何来自UE的5GMM请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|




命令举例 


`
删除一个Nsmf原因值映射配置，将HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”对应的5GMM Cause映射配置删除。
DEL SMFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN"
` 


### 查询Nsmf原因值映射配置(SHOW SMFCAUSEMAPPINGCFG) 
### 查询Nsmf原因值映射配置(SHOW SMFCAUSEMAPPINGCFG) 


功能说明 

该命令用于查询Nsmf原因值映射配置。支持单索引、全部查询等方式。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的应用层详细错误原因。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpStatusCode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的HTTP状态码。
applicationError|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|对端返回的应用层详细错误原因。
smfMMCause|5GMM Cause|参数可选性: 任选参数类型: 枚举，参见枚举定义|根据HTTP状态码和应用层错误码映射成的5GMM原因值。该原因值指示了为何来自UE的5GMM请求会被网络侧拒绝。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|




命令举例 


`
 查询HTTP状态码为“200 OK”对应的所有Nsmf原因值。
SHOW SMFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_200"

(No.1) : SHOW SMFCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_200"
-----------------Namf_Communication_0_A----------------
HTTP状态码 应用层错误码                 5GMM Cause
200 OK    INSUFFICIENT_UP_RESOURCES    92 - Insufficient user-plane resources for the PDU session
记录数：1

` 


## Neir 原因值映射配置 
## Neir 原因值映射配置 


背景知识 


当网络侧NF之间进行交互时，如果应用程序发生错误，NF之间会通过HTTP层的HTTP状态码（HTTP status code）来指示错误原因，参见协议3GPP TS 29500 5.2.7章节。应用层还会通过应用层ProblemDetails结构数据中的Cause值来指示更详细的错误原因，参见协议3GPP TS 29571 5.2.4.1 Type: ProblemDetails。 

当终端发起移动性的流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因。并且终端根据Cause值，可以触发后续相应行为。 

在5GC的移动性管理中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议24501 Annex A: Cause values for 5GS mobility management。 

AMF与其他NF交互时，AMF需要把其他NF返回的失败原因转换为5GMM原因，发送给UE，以引导UE进行合理的后续行为。参考协议3GPP TS 29.524。 




功能说明 


本节点用于配置当AMF和5G-EIR交互时，AMF使用5G-EIR返回的失败原因，通过配置转换为5GMM原因通知UE。5G-EIR返回的失败原因包括HTTP层的HTTP状态码(HTTP status code)和应用层的错误码(Application error)。 




子主题： 






### 新增Neir原因值映射配置(ADD NEIRCAUSEMAPPINGCFG) 
### 新增Neir原因值映射配置(ADD NEIRCAUSEMAPPINGCFG) 


功能说明 

该命令用于新增Neir原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，映射出唯一的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的状态码。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
eirmmcause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：根据EIR返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的状态码。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的应用层详细错误原因。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
eirmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：根据EIR返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。




命令举例 


`
新增一个Neir原因值映射配置，其中HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”，对应的5GMM Cause为“3 - Illegal UE”。
ADD NEIRCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",EIRMMCAUSE="ILLEGALUE"
` 


### 修改Neir原因值映射配置(SET NEIRCAUSEMAPPINGCFG) 
### 修改Neir原因值映射配置(SET NEIRCAUSEMAPPINGCFG) 


功能说明 

该命令用于修改Neir原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，修改对应的5GMM Cause。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的状态码。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
eirmmcause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：根据EIR返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的状态码。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的应用层详细错误原因。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
eirmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：根据EIR返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。




命令举例 


`
修改一个Neir原因值映射配置，将HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”对应的5GMM Cause修改为“5 - PEI not accepted”。
SET NEIRCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN",EIRMMCAUSE="PEINOTALLOWED"
` 


### 删除Neir原因值映射配置(DEL NEIRCAUSEMAPPINGCFG) 
### 删除Neir原因值映射配置(DEL NEIRCAUSEMAPPINGCFG) 


功能说明 

该命令用于删除Neir原因值映射配置。可通过“HTTP状态码+应用层错误码”的组合，删除对应的5GMM Cause。 


注意事项 

本配置存在默认记录。如果配置人员需要删除这些默认记录，那么AMF不保证后期映射原因值的合理性。当无法正确检索到原因值时，会统一使用“111 - Protocol error, unspecified” 。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的状态码。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的状态码。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的应用层详细错误原因。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
eirmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：根据EIR返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。




命令举例 


`
删除一个Neir原因值映射配置，将HTTP状态码为“100 Continue”、应用层错误码为“NF_CONSUMER_REDIRECT_ONE_TXN”对应的5GMM Cause映射配置删除。
DEL NEIRCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_100",APPLICATIONERROR="NF_CONSUMER_REDIRECT_ONE_TXN"
` 


### 查询Neir原因值映射配置(SHOW NEIRCAUSEMAPPINGCFG) 
### 查询Neir原因值映射配置(SHOW NEIRCAUSEMAPPINGCFG) 


功能说明 

该命令用于查询Neir原因值映射配置。支持单索引、全部查询等方式。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的状态码。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的状态码。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置对端EIR返回给AMF的HTTP响应消息中的应用层详细错误原因。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
eirmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：根据EIR返回给AMF的HTTP响应消息中的状态码和应用层错误码映射对应的5GMM原因值。该原因值指示了为何来自UE的5GMM请求（注册请求或业务请求）会被网络侧拒绝。修改影响：修改此参数,影响AMF与EIR交互失败时（注册请求或业务请求）下发的5GMM 原因值。数据来源：本端规划 默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。




命令举例 


`
查询HTTP状态码为“ 404 Not Found”对应的Neir原因值映射配置。
SHOW NEIRCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_404"

(No.21) : SHOW NEIRCAUSEMAPPINGCFG:HTTPSTATUSCODE="HTTP_404"
-----------------Namf_Communication_0----------------
操作维护       HTTP状态码    应用层错误码            5GMM 原因值    计数归类 
-----------------------------------------------------------------------------
复制 修改      404 Not Found ERROR_EQUIPMENT_UNKNOWN 6 - Illegal ME          
-----------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-06-28 16:19:07 耗时: 0.143 秒

` 


## Nnrf原因值映射配置 
## Nnrf原因值映射配置 


背景知识 


当AMF要和网络侧的各种NF交互时，AMF需要先通过NRF发现网络侧NF。在这个过程中，如果应用程序发生错误，NRF会通过HTTP层的HTTP状态码（HTTP status code）来指示错误原因，参见协议3GPP TS 29500 5.2.7章节。除此之外，还会通过应用层ProblemDetails结构数据中的Cause值来指示更详细的错误原因，参见协议3GPP TS 29571 5.2.4.1 Type: ProblemDetails。 

AMF发现网络侧NF失败后，AMF需要将NRF返回的失败原因转换为5GC的MM（移动性管理）失败原因，再将其发送给UE，以引导终端根据失败原因（Cause值），执行合理的后续流程。 

当终端发起移动性的流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因（Cause值）。终端根据失败原因（Cause值），执行后续的相应流程。 

在5GC的移动性管理流程中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议24501 Annex A: Cause values for 5GS mobility management。 




功能说明 


当AMF通过NRF发现网络侧NF失败时，AMF需要根据NRF返回的失败原因，通过本功能的配置，转换为5GC的MM（移动性管理）失败原因，并将转换后的失败原因，发送给UE。 

NRF返回的失败原因包括HTTP层的HTTP状态码（HTTP status code）和应用层的错误码（Application error）。 




子主题： 






### 新增Nnrf原因值映射配置(ADD NNRFCAUSEMAPPINGCFG) 
### 新增Nnrf原因值映射配置(ADD NNRFCAUSEMAPPINGCFG) 


功能说明 

该命令用于新增Nnrf原因值映射配置。可通过“发现场景+HTTP状态码+应用层错误码”的三个条件，映射出唯一的5GMM Cause。 


注意事项 


 
本命令执行后立即生效。 

 
本命令最多支持配置512条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
disnfsituation|发现NF场景|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5G MM原因值。数据来源：本端规划。默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5G MM原因值。数据来源：本端规划。默认值：无。配置原则：无。
nrfmmcause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。
nrfmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。




命令举例 


`
新增一个Nnrf原因值映射配置，其中发现NF场景为“发现AUSF”，HTTP状态码为“通配”，应用层错误码为“通配”，对应的5GMM Cause为“111 - Protocol error, unspecified”。
ADD NNRFCAUSEMAPPINGCFG:DISNFSITUATION="DISCOVER_AUSF",HTTPSTATUSCODE="ANYHTTPSTATUS",APPLICATIONERROR="ANY_APPLICATION_ERR",NRFMMCAUSE="PROTOCOLERRUNSPEC"
` 


### 修改Nnrf原因值映射配置(SET NNRFCAUSEMAPPINGCFG) 
### 修改Nnrf原因值映射配置(SET NNRFCAUSEMAPPINGCFG) 


功能说明 

该命令用于修改Nnrf原因值映射配置。可通过“发现场景+HTTP状态码+应用层错误码”的组合，修改映射的5GMM Cause。 


注意事项 


 
本命令执行后立即生效。 

 
“发现场景+HTTP状态码+应用层错误码”对应记录需要已经通过ADD NNRFCAUSEMAPPINGCFG命令配置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
disnfsituation|发现NF场景|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5G MM原因值。数据来源：本端规划。默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5G MM原因值。数据来源：本端规划。默认值：无。配置原则：无。
nrfmmcause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。
nrfmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。




命令举例 


`
修改一个Nnrf原因值映射配置，其中发现NF场景为“发现AUSF”，HTTP状态码为“通配”，应用层错误码为“通配”，对应的5GMM Cause为“111 - Protocol error, unspecified”。
SET NNRFCAUSEMAPPINGCFG:DISNFSITUATION="DISCOVER_AUSF",HTTPSTATUSCODE="ANYHTTPSTATUS",APPLICATIONERROR="ANY_APPLICATION_ERR",NRFMMCAUSE="PROTOCOLERRUNSPEC"
` 


### 删除Nnrf原因值映射配置(DEL NNRFCAUSEMAPPINGCFG) 
### 删除Nnrf原因值映射配置(DEL NNRFCAUSEMAPPINGCFG) 


功能说明 

该命令用于删除Nnrf原因值映射配置。可通过“发现场景+HTTP状态码+应用层错误码”的组合，删除该配置记录。 


注意事项 


 
本命令执行后立即生效。 

 
“发现场景+HTTP状态码+应用层错误码”对应记录需要已经通过ADD NNRFCAUSEMAPPINGCFG命令配置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
disnfsituation|发现NF场景|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5G MM原因值。数据来源：本端规划。默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5G MM原因值。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。
nrfmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。




命令举例 


`
删除一个Nnrf原因值映射配置，将发现NF场景为“发现AUSF”，HTTP状态码为“通配”，应用层错误码为“通配”对应的5GMM Cause映射配置删除。
DEL NNRFCAUSEMAPPINGCFG:DISNFSITUATION="DISCOVER_AUSF",HTTPSTATUSCODE="ANYHTTPSTATUS",APPLICATIONERROR="ANY_APPLICATION_ERR"
` 


### 查询Nnrf原因值映射配置(SHOW NNRFCAUSEMAPPINGCFG) 
### 查询Nnrf原因值映射配置(SHOW NNRFCAUSEMAPPINGCFG) 


功能说明 

该命令用于查询Nnrf原因值映射配置。可通过输入“发现场景+HTTP状态码+应用层错误码”的参数组合，唯一查询该记录。也可以不输入某个查询参数，表示查询全部的配置数据。 


注意事项 

本命令执行后立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5G MM原因值。数据来源：本端规划。默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5G MM原因值。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。
nrfmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。




命令举例 


`
查询发现NF场景为“发现AUSF”对应的Nnrf原因值映射配置。
SHOW NNRFCAUSEMAPPINGCFG:DISNFSITUATION="DISCOVER_AUSF"

(No.1) : SHOW NNRFCAUSEMAPPINGCFG:DISNFSITUATION="DISCOVER_AUSF"
-----------------Namf_Communication_0_A----------------
发现NF场景   HTTP状态码        应用层错误码                     5GMM 原因值                                 计数归类 
发现AUSF     403 Forbidden   SERVING_NETWORK_NOT_AUTHORIZED     11 - PLMN not allowed
-------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-16 15:10:36 耗时: 0.137 秒

` 


## 基于SUPI号段的Nnrf原因值映射配置 
## 基于SUPI号段的Nnrf原因值映射配置 


背景知识 


当AMF要和网络侧的各种NF交互时，AMF需要先通过NRF发现网络侧NF。在这个过程中，如果应用程序发生错误，NRF会通过HTTP层的HTTP状态码（HTTP status code）来指示错误原因，参见协议3GPP TS 29500 5.2.7章节。除此之外，还会通过应用层ProblemDetails结构数据中的Cause值来指示更详细的错误原因，参见协议3GPP TS 29571 5.2.4.1 Type: ProblemDetails。 

AMF发现网络侧NF失败后，AMF需要将NRF返回的失败原因转换为5GC的MM（移动性管理）失败原因，再将其发送给UE，以引导终端根据失败原因（Cause值），执行合理的后续流程。 

当终端发起移动性的流程失败时，网络侧可以通过3GPP TS 24501中定义的移动性Cause值，通知终端失败原因（Cause值）。终端根据失败原因（Cause值），执行后续的相应流程。 

在5GC的移动性管理流程中，Cause是与终端身份、订阅选择、PLMN特定的网络故障和拥塞/认证失败、无效消息相关的错误原因，参见协议24501 Annex A: Cause values for 5GS mobility management。 




功能说明 


当AMF通过NRF发现网络侧NF失败时，AMF需要根据NRF返回的失败原因，通过本功能的配置，转换为5GC的MM（移动性管理）失败原因，并将转换后的失败原因，发送给UE。 

NRF返回的失败原因包括HTTP层的HTTP状态码（HTTP status code）和应用层的错误码（Application error）。 

AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。 

通过提供该配置功能，对NRF返回的相同的失败原因，AMF能够将其映射为不同的5G MM失败原因，可以灵活的引导不同SUPI号段的终端，执行相应的合理的后续流程。 




子主题： 






### 新增基于SUPI号段的Nnrf原因值映射配置(ADD NNRFCAUSEMAPPINGCFGBYSUPI) 
### 新增基于SUPI号段的Nnrf原因值映射配置(ADD NNRFCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于新增基于SUPI号段的Nnrf原因值映射配置。可通过“SUPI号段+发现场景+HTTP状态码+应用层错误码”的组合，映射出唯一的5GMM Cause。 


注意事项 


 
本命令执行后立即生效。 

 
针对每个发现场景，AMF优先使用基于SUPI号段的Nnrf原因值映射配置，当没有匹配到基于SUPI号段的Nnrf原因值映射数据时，AMF采用默认的Nnrf原因值映射配置（通过ADD NNRFCAUSEMAPPINGCFG）。 

 
针对每个发现场景，一旦规划了某个SUPI号段需要进行某种的Nnrf原因映射，则所有失败原因映射关系都应在该号段下配置完整，不应该再其他短号段下或者全局的失败原因映射下配置，即表示某个SUPI号段下的所有的失败原因，不允许在长号段中配置部分失败原因映射关系，同时又在短号段中或者全局配置中配置部分失败原因映射关系。 

 
本命令最多支持配置200000条记录条。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
disnfsituation|发现NF场景|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
nrfmmcause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。
nrfmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。




命令举例 


`
新增一个基于SUPI号段的Nnrf原因值映射配置，其中SUPI号段为“46011”，发现NF场景为“发现AUSF”，HTTP状态码为“通配”，应用层错误码为“通配”，对应的5GMM Cause为“111 - Protocol error, unspecified”。
ADD NNRFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",DISNFSITUATION="DISCOVER_AUSF",HTTPSTATUSCODE="ANYHTTPSTATUS",APPLICATIONERROR="ANY_APPLICATION_ERR",NRFMMCAUSE="PROTOCOLERRUNSPEC"
` 


### 修改基于SUPI号段的Nnrf原因值映射配置(SET NNRFCAUSEMAPPINGCFGBYSUPI) 
### 修改基于SUPI号段的Nnrf原因值映射配置(SET NNRFCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于修改基于SUPI号段的Nnrf原因值映射配置。可通过“SUPI号段+发现场景+HTTP状态码+应用层错误码”的组合，修改映射的5GMM Cause。 


注意事项 


 
本命令执行后立即生效。 

 
SUPI号段+发现场景+HTTP状态码+应用层错误码”对应记录需要已经通过ADD NNRFCAUSEMAPPINGCFGBYSUPI命令配置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
disnfsituation|发现NF场景|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
nrfmmcause|5GMM 原因值|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。
nrfmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。




命令举例 


`
修改一个基于SUPI号段的Nnrf原因值映射配置，其中SUPI号段为“46011”，发现NF场景为“发现AUSF”，HTTP状态码为“通配”，应用层错误码为“通配”，对应的5GMM Cause为“111 - Protocol error, unspecified”。
SET NNRFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",DISNFSITUATION="DISCOVER_AUSF",HTTPSTATUSCODE="ANYHTTPSTATUS",APPLICATIONERROR="ANY_APPLICATION_ERR",NRFMMCAUSE="PROTOCOLERRUNSPEC"
` 


### 删除基于SUPI号段的Nnrf原因值映射配置(DEL NNRFCAUSEMAPPINGCFGBYSUPI) 
### 删除基于SUPI号段的Nnrf原因值映射配置(DEL NNRFCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于删除基于SUPI号段的Nnrf原因值映射配置。可通过“SUPI号段+发现场景+HTTP状态码+应用层错误码”的组合，删除该配置记录。 


注意事项 


 
本命令执行后立即生效。 

 
SUPI号段+发现场景+HTTP状态码+应用层错误码”对应记录需要已经通过ADD NNRFCAUSEMAPPINGCFGBYSUPI命令配置。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
disnfsituation|发现NF场景|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
httpstatuscode|HTTP状态码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 必选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。
nrfmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。




命令举例 


`
删除一个基于SUPI号段的Nnrf原因值映射配置，将SUPI号段为“46011”，发现NF场景为“发现AUSF”，HTTP状态码为“通配”，应用层错误码为“通配”对应的5GMM Cause映射配置删除。
DEL NNRFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011",DISNFSITUATION="DISCOVER_AUSF",HTTPSTATUSCODE="ANYHTTPSTATUS",APPLICATIONERROR="ANY_APPLICATION_ERR"
` 


### 查询基于SUPI号段的Nnrf原因值映射配置(SHOW NNRFCAUSEMAPPINGCFGBYSUPI) 
### 查询基于SUPI号段的Nnrf原因值映射配置(SHOW NNRFCAUSEMAPPINGCFGBYSUPI) 


功能说明 

该命令用于查询基于SUPI号段的Nnrf原因值映射配置。可通过输入“SUPI号段+发现场景+HTTP状态码+应用层错误码”的参数组合，唯一查询该记录。也可以不输入某个查询参数，表示查询全部的配置数据。 


注意事项 

本命令执行后立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。修改影响：修改此参数，影响AMF与NRF交互失败时下发的5GMM原因值。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于设置终端的SUPI号段，AMF支持根据终端的SUPI号段来区分NRF失败原因映射到5G MM的失败原因，以便灵活地针对不同SUPI号段提供差异化的映射配置。
disnfsituation|发现NF场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置AMF通过NRF发现NF的场景，即AMF通过NRF发现的NF的类型，比如是发现SMF还是发现NSSF。
httpstatuscode|HTTP状态码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的HTTP状态码。
applicationerror|应用层错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置AMF向NRF发送发现NF的请求消息后，NRF返回的发现响应消息中携带的应用层详细错误码。
nrfmmcause|5GMM 原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：此参数用于配置根据NRF返回给AMF的发现响应消息中携带的HTTP状态码和应用层错误码，对应的5G MM原因值。该原因值指示了来自终端的5G MM请求（注册请求或业务请求）被网络侧拒绝的具体原因。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：此参数用于性能统计时归类使用。




命令举例 


`
查询基于SUPI号段的Nnrf原因值映射配置。
SHOW NNRFCAUSEMAPPINGCFGBYSUPI:SUPISEG="46011"

(No.4) : SHOW AUSFCAUSEMAPPINGCFGBYSUPI:
-----------------Namf_Communication_0----------------
SUPI号段    发现NF场景   HTTP状态码      应用层错误码                    5GMM 原因值          计数归类 
 46011      发现AUSF     100 Continue    NF_CONSUMER_REDIRECT_ONE_TXN    3 - Illegal UE    
记录数：1
命令执行成功（耗时 0.031 秒）。

` 


# VendorSpecial配置 
# VendorSpecial配置 


背景知识 


在3GPP 29.500协议中，允许设备商通过以厂商特定信元的方式对APIs接口进行扩展。 




功能说明 


VernderSpecail配置适用于中兴通讯的AMF和SMF之间配置相关的特定信元信息，以减少SMF需要到NRF才能发现AMF的过程。 




子主题： 






## AMF支持VendorSpec配置 
## AMF支持VendorSpec配置 


背景知识 


标准29500协议中，允许设备商通过以厂商特定信元的方式对APIs接口进行扩展（vendor-specific member elements）. 

IANA（Internet Assigned Number Authority，互联网号码分配机构）为每个厂商分配特定的编号（ "SMI Network Management Private Enterprise Codes"），如此可避免各个厂商冲突。 

具体参见TS 29500第“6.6.3 Vendor-specific extensions”章节。 




功能说明 


中兴通讯的AMF和SMF交互的时候，可以在SmContextCreateData消息中携带ZTE venderSpecific的 JSON objects（vendorSpecific-003902  ），其中包含了为SMF分配EBI、N1/N2消息传输时的URI。 

中兴通讯的SMF可通过解析此JSON object，在向调用AMF的Namf_Communication_N1N2 Transfer和Namf_Communication_EBIAssignment操作时，直接使用其中的URI，不必通过NRF发现这种方式获取，有效的减少了网络中的信令数，同时缩短了流程时间。 




子主题： 






### 修改 AMF支持VendorSpec配置(SET AMFSUPPORTVENDERSPEC) 
### 修改 AMF支持VendorSpec配置(SET AMFSUPPORTVENDERSPEC) 


功能说明 

该命令用于设置或修改AMF是否开启VenderSpec功能。  

当需要开启或关闭VenderSpec功能时，可使用此命令。  


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
amfSupVenderSpec|创建会话是否支持|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFNOTSUPTVENDERSPEC|该参数用于设置AMF会话创建时是否开启VendorSpec功能，携带VendorSpec参数。
updateSmSup|更新会话是否支持|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFNOTSUPTVENDERSPEC|该参数用于设置AMF会话更新时是否开启VendorSpec功能，携带VendorSpec参数。




命令举例 


`
设置或修改是否支持VENDERSPEC功能：创建会话支持，更新会话支持。
SET AMFSUPPORTVENDERSPEC:AMFSUPVENDERSPEC="AMFSUPTVENDERSPEC", UPDATESMSUP="AMFSUPTVENDERSPEC"
` 


### 查询 AMF支持VendorSpec配置(SHOW AMFSUPPORTVENDERSPEC) 
### 查询 AMF支持VendorSpec配置(SHOW AMFSUPPORTVENDERSPEC) 


功能说明 

该命令用于查询本AMF是否开启VenderSpec功能。  


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
amfSupVenderSpec|创建会话是否支持|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFNOTSUPTVENDERSPEC|该参数用于设置AMF会话创建时是否开启VendorSpec功能，携带VendorSpec参数。
updateSmSup|更新会话是否支持|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFNOTSUPTVENDERSPEC|该参数用于设置AMF会话更新时是否开启VendorSpec功能，携带VendorSpec参数。




命令举例 


`
查询AMFSUPPORTVENDERSPEC功能。 
SHOW AMFSUPPORTVENDERSPEC:

(No.1) : SHOW AMFSUPPORTVENDERSPEC:
-----------------Namf_Communication_0----------------
创建会话是否支持          更新会话是否支持
不支持VendorSpec            支持VendorSpec
记录数：1

` 


# 消息参数配置 
# 消息参数配置 


背景知识 


消息参数为移动网络中各个NF的业务实现的最小业务单元，每个参数都是各种功能实现的基础。在实际的使用中，需要根据网络的实际情况调整不同的参数，以配合其他NF和实现各种业务。 




功能说明 


本功能包括配置控制AMF和其他NF间某些消息参数的配置策略。 




子主题： 






## Namf消息参数配置 
## Namf消息参数配置 


背景知识 


AMF提供Namf接口，给其他NF使用。有时需要对某些消息参数进行控制处理。 




功能说明 


Namf消息参数配置提供retryafter参数配置。 




子主题： 






### retryAfter参数配置 
### retryAfter参数配置 


背景知识 


AMF收到N1N2MessageTransfer消息后，处理失败，需要给对端返回retryAfter字段。 




功能说明 


本功能用于设置AMF收到N1N2MessageTransfer消息后，处理失败，需要给对端返回retryAfter字段值。 

例如retryAfter时长为4秒，则对端在4秒之后，再次尝试发送N1N2MessageTransfer消息。 




子主题： 






#### 设置retryAfter参数配置(SET RETRYAFTER) 
#### 设置retryAfter参数配置(SET RETRYAFTER) 


功能说明 

该命令用于设置AMF收到N1N2MessageTransfer消息后，处理失败，需要给对端返回retryAfter时长值。 

例如retryAfter时长为4秒，则对端在4秒之后，再次尝试发送N1N2MessageTransfer消息。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
retryAfter|重试时长值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-20默认值: 4|AMF收到N1N2MessageTransfer消息后，处理失败，给对端返回的retryAfter时长，取值如下：0：不携带retryAfter时长。其他非0值：携带的retryAfter时长，单位：秒。




命令举例 


`
设置RETRYAFTER时长秒数为4秒。
SET RETRYAFTER:RETRYAFTER="4"
` 


#### 查询retryAfter参数配置(SHOW RETRYAFTER) 
#### 查询retryAfter参数配置(SHOW RETRYAFTER) 


功能说明 

该命令用于查询AMF收到N1N2MessageTransfer消息后，处理失败，需要给对端返回retryAfter时长值。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
retryAfter|重试时长值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-20默认值: 4|AMF收到N1N2MessageTransfer消息后，处理失败，给对端返回的retryAfter时长，取值如下：0：不携带retryAfter时长。其他非0值：携带的retryAfter时长，单位：秒。




命令举例 


`
查询RETRYAFTER配置。
SHOW RETRYAFTER:

SHOW RETRYAFTER:
-----------------Namf_Communication_0----------------
重试时长值（秒）
-----------------------------------------------------------------
             4
-----------------------------------------------------------------
记录数：1
执行成功耗时: 0.083 秒

` 


### DNN参数配置 
### DNN参数配置 


背景知识 


在跨AMF的注册更新和N2切换流程中，AMF间发送Namf_Communication_UEContextTransfer、Namf_Communication_CreateUEContext消息时，可以灵活配置DNN参数的携带策略。 




功能说明 


DNN参数配置中，可以分别设置本网用户、LBO漫游用户和HR漫游用户的DNN OI携带策略。 




子主题： 






#### 修改 DNN参数配置(SET DNNPARAMETERCFG) 
#### 修改 DNN参数配置(SET DNNPARAMETERCFG) 


功能说明 

该命令用于设置DNN参数配置。当AMF间发送Namf_Communication_UEContextTransfer、Namf_Communication_CreateUEContext消息时，可以配置DNN参数的携带策略，包括：DNN OI携带策略。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
localcarrydnnoi|本网用户携带DNN OI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYOI|参数作用：用于设置本网用户携带DNN OI。AMF间发送Namf_Communication_CreateUEContext Request和Namf_Communication_UEContextTransfer Response消息时，用户携带的DNN是否包含DNN OI。修改影响：如果设置为携带OI，则携带的DNN包含DNN OI；如果设置为不携带OI，则表示携带的DNN不包含DNN OI。数据来源：本端配置。默认值：不携带。配置原则：无。
lbocarrydnnoi|LBO漫游用户携带DNN OI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYOI|参数作用：用于设置LBO漫游用户携带DNN OI。AMF间发送Namf_Communication_CreateUEContext Request和Namf_Communication_UEContextTransfer Response消息时，用户携带的DNN是否包含DNN OI。修改影响：如果设置为携带OI，则携带的DNN包含DNN OI；如果设置为不携带OI，则表示携带的DNN不包含DNN OI。数据来源：本端配置。默认值：不携带。配置原则：无。
hrcarrydnnoi|HR漫游用户携带DNN OI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYOI|参数作用：用于设置HR漫游用户携带DNN OI。AMF间发送Namf_Communication_CreateUEContext Request和Namf_Communication_UEContextTransfer Response消息时，用户携带的DNN是否包含DNN OI。修改影响：如果设置为携带OI，则携带的DNN包含DNN OI；如果设置为不携带OI，则表示携带的DNN不包含DNN OI。数据来源：本端配置。默认值：携带。配置原则：无。




命令举例 


`
设置本网用户携带DNN OI为携带OI，设置LBO漫游用户携带DNN OI为携带OI，设置HR漫游用户携带DNN OI为携带OI：
SET DNNPARAMETERCFG:LOCALCARRYDNNOI="CARRYOI",LBOCARRYDNNOI="CARRYOI",HRCARRYDNNOI="CARRYOI"
` 


#### 查询 DNN参数配置(SHOW DNNPARAMETERCFG) 
#### 查询 DNN参数配置(SHOW DNNPARAMETERCFG) 


功能说明 

该命令用于查看DNN参数配置。  


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
localcarrydnnoi|本网用户携带DNN OI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYOI|参数作用：用于设置本网用户携带DNN OI。AMF间发送Namf_Communication_CreateUEContext Request和Namf_Communication_UEContextTransfer Response消息时，用户携带的DNN是否包含DNN OI。
lbocarrydnnoi|LBO漫游用户携带DNN OI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYOI|参数作用：用于设置LBO漫游用户携带DNN OI。AMF间发送Namf_Communication_CreateUEContext Request和Namf_Communication_UEContextTransfer Response消息时，用户携带的DNN是否包含DNN OI。
hrcarrydnnoi|HR漫游用户携带DNN OI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYOI|参数作用：用于设置HR漫游用户携带DNN OI。AMF间发送Namf_Communication_CreateUEContext Request和Namf_Communication_UEContextTransfer Response消息时，用户携带的DNN是否包含DNN OI。




命令举例 


`
该命令用于查看DNN参数配置。
SHOW DNNPARAMETERCFG:

(No.1) :  SHOW DNNPARAMETERCFG:
-----------------Namf_Communication_0----------------
操作维护       本网用户携带DNN OI LBO漫游用户携带DNN OI HR漫游用户携带DNN OI
--------------------------------------------------------------------------------
修改           携带               携带                  携带
--------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-07-21 11:01:27 耗时: 0.164 秒

` 


### N14接口参数配置 
### N14接口参数配置 


背景知识 


N14接口是AMF与AMF之间的接口。 

终端发生位置移动，从一个AMF的管理范围移动到另外一个AMF的管理范围，源AMF和目标AMF发生交互时，本AMF向其他AMF发送Namf_Communication_UEContextTransfer Request/Response、Namf_Communication_CreateUEContext Request/Response时，可以配置部分参数的携带策略。 




功能说明 


终端发生位置移动，从一个AMF的管理范围移动到另外一个AMF的管理范围，源AMF和目标AMF发生交互时，本AMF向其他AMF发送Namf_Communication_UEContextTransfer Request/Response、Namf_Communication_CreateUEContext Request/Response时，可以配置部分参数的携带策略。 




子主题： 






#### 设置N14接口参数配置(SET N14INTERFACEPARAMETERCFG) 
#### 设置N14接口参数配置(SET N14INTERFACEPARAMETERCFG) 


功能说明 

本命令用于设置N14接口参数配置。 

N14接口是AMF与AMF之间的接口。 


注意事项 

本命令执行后，结果立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ifservingplmn|创建UE上下文请求消息是否携带服务PLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYSERVINGPLMN|参数作用：该参数用于配置AMF在向其他AMF发送的Namf_Communication_CreateUEContext Request消息中servingNetwork参数的携带策略。修改影响：如果设置为携带，则AMF发出的Namf_Communication_CreateUEContext Request消息请求中会携带servingNetwork字段。数据来源：本端规划。默认值：不携带配置原则：无。
ifadditionsnssai|是否在PduSessionContext中携带additionalSnssai|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于配置当漫入用户在VPLMN内移动时，配置AMF在向其他AMF发送的Namf_Communication_UEContextTransfer Response/Namf_Communication_CreateUEContext Request消息中是否携带additionalSnssai参数。修改影响：如果设置为携带，则漫入用户在VPLMN内移动时，AMF在向其他AMF发送Namf_Communication_UEContextTransfer Response/Namf_Communication_CreateUEContext Request消息时，会携带additionalSnssai参数。数据来源：本端规划。默认值：不携带配置原则：无。
carryhnwpubkeyid|是否在UeContext中携带hNwPubKeyId|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置在跨AMF切换、跨AMF注册更新，或者AMF重选流程中，AMF之间传递的UeContext中是否携带hNwPubKeyId字段。修改影响：如果设置为携带，则在上述流程中，AMF之间传递的UeContext中携带hNwPubKeyId字段。数据来源：本端规划。默认值：不携带。配置原则：无。




命令举例 


`
设置AMF间发送N14接口消息时携带servingNetwork参数和additionSnssai参数。
SET N14INTERFACEPARAMETERCFG:IFSERVINGPLMN="CARRYSERVINGPLMN",IFADDITIONSNSSAI="CARRY",CARRYHNWPUBKEYID="NOTCARRY"
` 


#### 查询N14接口参数配置(SHOW N14INTERFACEPARAMETERCFG) 
#### 查询N14接口参数配置(SHOW N14INTERFACEPARAMETERCFG) 


功能说明 

该命令用于查询N14接口参数配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
ifservingplmn|创建UE上下文请求消息是否携带服务PLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYSERVINGPLMN|参数作用：该参数用于配置AMF在向其他AMF发送的Namf_Communication_CreateUEContext Request消息中servingNetwork参数的携带策略。
ifadditionsnssai|是否在PduSessionContext中携带additionalSnssai|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于配置当漫入用户在VPLMN内移动时，配置AMF在向其他AMF发送的Namf_Communication_UEContextTransfer Response/Namf_Communication_CreateUEContext Request消息中是否携带additionalSnssai参数。
carryhnwpubkeyid|是否在UeContext中携带hNwPubKeyId|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置在跨AMF切换、跨AMF注册更新，或者AMF重选流程中，AMF之间传递的UeContext中是否携带hNwPubKeyId字段。




命令举例 


`
该命令用于查询N14接口参数配置。
SHOW N14INTERFACEPARAMETERCFG

SHOW N14INTERFACEPARAMETERCFG:
-----------------Namf_Communication_0----------------------------------------------------------------------------------------------
操作维护      创建UE上下文请求消息是否携带服务PLMN    是否在PduSessionContext中携带additionalSnssai   是否在UeContext中携带hNwPubKeyId
-----------------------------------------------------------------------------------------------------------------------------------
修改          携带                                    携带                                            不携带
-----------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-05-05 10:15:48 耗时: 0.134 秒

` 


## N2消息参数配置 
## N2消息参数配置 


背景知识 


AMF在N2接口传递移动性管理相关的消息和信息。在某些特殊情况下，需要对某些消息参数进行控制处理。 




功能说明 


本功能用于配置UE AMBR等参数。 




子主题： 






### NAS透传消息参数配置 
### NAS透传消息参数配置 


背景知识 


本功能用于设置DNT(Downlink NasTransport)消息带给RAN侧的参数。 




功能说明 


本功能用于设置DNT(Downlink NasTransport)消息带给RAN侧的参数，比如：是否携带RFSP(Index to RAT/Frequency Selection Priority)给RAN。 




子主题： 






#### 修改NAS透传消息参数配置(SET DNTPARA) 
#### 修改NAS透传消息参数配置(SET DNTPARA) 


功能说明 

该命令用于设置DNT(Downlink NasTransport)消息带给RAN侧的参数，比如：是否携带RFSP(Index to RAT/Frequency Selection Priority)给RAN。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
takeRfsp|是否携带RFSP|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTAKERFSP|本参数用于设置DNT消息是否携带RFSP给RAN。




命令举例 


`
设置DNT参数，N2层携带RFSP。
SET DNTPARA:TAKERFSP=TAKERFSP
` 


#### 查询NAS透传消息参数配置(SHOW DNTPARA) 
#### 查询NAS透传消息参数配置(SHOW DNTPARA) 


功能说明 

该命令用于查询AMF在DNT消息中携带的参数，比如：是否携带RFSP给RAN。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
takeRfsp|是否携带RFSP|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTAKERFSP|本参数用于显示DNT消息是否携带RFSP给RAN。




命令举例 


`
查询AMF在DNT消息中携带的N2参数，比如：RFSP的携带情况。
SHOW DNTPARA

(No.1) : SHOW DNTPARA:
-----------------Namf_Communication_0----------------
是否携带RFSP   不携带RFSP
记录数：1

执行成功耗时: 0.258 秒

` 


### N2 Setup参数配置 
### N2 Setup参数配置 


背景知识 


AMF和RAN之间建立N2口连接，有些情形，如NG Setup失败，AMF需要携带相关参数给RAN。 




功能说明 


本功能用于设置AMF在N2口连接建立过程中需要带给RAN侧的参数，比如：NG Setup失败是否携带等待时长及等待的具体时长。 




子主题： 






#### 修改N2 Setup参数配置(SET N2SETUPPARACFG) 
#### 修改N2 Setup参数配置(SET N2SETUPPARACFG) 


功能说明 

该命令用于设置N2接口消息中的Setup参数，如NG Setup Failure消息是否携带等待时长及等待的具体时长。 

N2接口是NG-RAN（NG Radio Access Network）与AMF之间的信令面接口。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
timeToWaitFlg|NG Setup失败是否携带等待时长|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于控制AMF在给RAN回复的NG Setup Failure响应消息中是否携带等待时长。NG Setup Failure消息由AMF发送给无线侧，用于指示NG建立失败。修改影响：修改参数为是时，AMF在给RAN回复的NG Setup Failure响应消息中将携带等待时长。数据来源：本端配置。默认值：是。配置原则：无。
timeToWait|等待时长|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5默认值: V2S|参数作用：该参数用于设置AMF在给RAN回复的NG Setup Failure响应消息中携带的等待时长。NG Setup Failure消息由AMF发送给无线侧，用于指示NG建立失败。修改影响：修改本参数，且参数“NG Setup失败是否携带等待时长”为是时，NG Setup Failure响应消息中将携带对应的等待时长。数据来源：本端配置。默认值：2秒。配置原则：无。
maxnssainum|单PLMN下携带的最大切片数|参数可选性: 任选参数类型: 数字参数范围: 1-1024默认值: 64|参数作用：该参数用于控制N2接口的Setup流程中，AMF发送给RAN的NG Setup Response消息和AMF Configuration Update消息中的PLMN对应的Slice Support List中的最大切片数量。修改影响：修改本参数，AMF给RAN发送NG Setup Response消息和AMF Configuration Update消息中的PLMN对应的Slice Support List中的最大切片数量会修改为本参数配置的值。数据来源：本端配置。默认值：64。配置原则：无。




命令举例 


`
设置N2 Setup参数：NG Setup失败携带等待时长，等待时长为2秒，单PLMN下携带的最大切片数。
SET N2SETUPPARACFG:TIMETOWAITFLG="YES",TIMETOWAIT="V2S",MAXNSSAlNUM=64
` 


#### 查询N2 Setup参数配置(SHOW N2SETUPPARACFG) 
#### 查询N2 Setup参数配置(SHOW N2SETUPPARACFG) 


功能说明 

该命令用于查询N2接口消息中的Setup参数配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
timeToWaitFlg|NG Setup失败是否携带等待时长|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于控制AMF在给RAN回复的NG Setup Failure响应消息中是否携带等待时长。NG Setup Failure消息由AMF发送给无线侧，用于指示NG建立失败。
timeToWait|等待时长|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5默认值: V2S|参数作用：该参数用于设置AMF在给RAN回复的NG Setup Failure响应消息中携带的等待时长。NG Setup Failure消息由AMF发送给无线侧，用于指示NG建立失败。
maxnssainum|单PLMN下携带的最大切片数|参数可选性: 任选参数类型: 数字参数范围: 1-1024默认值: 64|参数作用：该参数用于控制N2接口的Setup流程中，AMF发送给RAN的NG Setup Response消息和AMF Configuration Update消息中的PLMN对应的Slice Support List中的最大切片数量。




命令举例 


`
查询N2 Setup参数。
SHOW N2SETUPPARACFG

(No.1) :SHOW N2SETUPPARACFG
-------Namf_Communication_0_A---------
NG Setup失败是否携带等待时长    等待时长    单PLMN下携带的最大切片数
----------------------------------------------------------------------------------
是                                             2秒           64           
--------------------------------------------------------------------------------
记录数：1
执行成功耗时: 0.087 秒

` 


### Masked IMEISV参数配置 
### Masked IMEISV参数配置 


背景知识 


38413 协议中描述，?INITIAL CONTEXT SETUP REQUEST和HANDOVER REQUEST中可以包含Masked IMEISV?IE，NG-RAN通过IMEISV进行特殊操作。 




功能说明 


本功能用于设置AMF 是否在?INITIAL CONTEXT SETUP REQUEST和HANDOVER REQUEST消息中携带Masked IMEISV。携带的前提是要配置获取IMEISV，必须先通过[SET AMFMOBCFG]命令设置“获取IMEISV”。具体为SET AMFMOBCFG:AMFGETIMEI="GETIMEISV" 




子主题： 






#### 设置Masked IMEISV参数配置(SET AMFMASKEDIMEISVCFG) 
#### 设置Masked IMEISV参数配置(SET AMFMASKEDIMEISVCFG) 


功能说明 

该命令用于设置AMF Masked IMEISV参数配置。当需要在N2消息中携带Masked IMEISV时，使用该命令进行配置。如果Masked IMEISV支持，NG-RAN可以通过IMSISV对终端进行管理， 对部分终端指定特殊的策略。 

包括是否携带如下参数：InitCtxSCarryIMEISV、HoCarryIMEISV。  


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
InitCtxSCarryIMEISV|INITIAL CONTEXT SETUP REQUEST中携带Masked IMEISV|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupMskImeiSv|该参数用于设置AMF通过向基站发送InitialContextSetupRequest时，是否携带masked imeisv。如设置为支持，则AMF发送的InitialContextSetupRequest消息携带masked imeisv，其值为IMEISV的SRN后4digit设置为1，其他位不变。
HoCarryIMEISV|HANDOVER  REQUEST中携带Masked IMEISV|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupMskImeiSv|该参数用于设置AMF通过向基站发送HandoverRequest时，是否携带masked imeisv。如设置为支持，则AMF发送的HandoverRequest消息携带masked imeisv，其值为IMEISV的SRN后4digit设置为1，其他位不变。




命令举例 


`
设置AMF在InitialContextSetupRequest和HandoverRequest消息中携带masked imeisv。
SET AMFMASKEDIMEISVCFG:INITCTXSCARRYIMEISV="SupMskImeiSv",HOCARRYIMEISV="SupMskImeiSv"
` 


#### 查询Masked IMEISV参数配置(SHOW AMFMASKEDIMEISVCFG) 
#### 查询Masked IMEISV参数配置(SHOW AMFMASKEDIMEISVCFG) 


功能说明 

该命令用于该命令用于查询Masked IMEISV参数配置。   


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
InitCtxSCarryIMEISV|INITIAL CONTEXT SETUP REQUEST中携带Masked IMEISV|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupMskImeiSv|该参数用于设置AMF通过向基站发送InitialContextSetupRequest时，是否携带masked imeisv。如设置为支持，则AMF发送的InitialContextSetupRequest消息携带masked imeisv，其值为IMEISV的SRN后4digit设置为1，其他位不变。
HoCarryIMEISV|HANDOVER  REQUEST中携带Masked IMEISV|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NotSupMskImeiSv|该参数用于设置AMF通过向基站发送HandoverRequest时，是否携带masked imeisv。如设置为支持，则AMF发送的HandoverRequest消息携带masked imeisv，其值为IMEISV的SRN后4digit设置为1，其他位不变。




命令举例 


`
查询当前AMF Masked IMEISV参数配置。
SHOW AMFMASKEDIMEISVCFG:

(No.1) : SHOW AMFMASKEDIMEISVCFG:
-----------------Namf_Communication_0----------------
INITIAL CONTEXT SETUP REQUEST中携带Masked IMEISV  HANDOVER  REQUEST中携带Masked IMEISV
不支持maskedImeisv 不支持maskedImeisv
记录数：1

执行成功耗时: 0.209 秒

` 


## Nnrf消息参数配置 
## Nnrf消息参数配置 


背景知识 


NRF通过Nnrf接口向其他NF提供多种服务(NFS，Network Function Service)，具体服务包括如下所定义的各种： 

Nnrf_NFManagement 


 
允许NF实例属性在所属PLMN的NRF上注册、更新、去注册。 

 
允许NRF实例在同一个PLMN中的另一个NRF中注册、更新或去注册其属性信息。也可以使用其他方式更新或去注册NRF Profile，例如，可以通过OA&M更新或去注册NRF Profile。 

 
允许NF订阅以收到新注册的NF实例和NFS的通知。 

 
允许检索当前NRF上已注册的NF实例列表或指定NF实例的属性。 

 

Nnrf_NFDiscovery 


 
允许NF实例通过查询本PLMN的NRF发现其他NF提供的NFS。 

 
允许PLMN内的NRF向其他PLMN（如某特定UE所在的PLMN）内的NRF重新发起发现请求。 

 

Nnrf_AccessToken 

NRF提供了Nnrf_AccessToken服务（用于OAuth2授权），遵循“Client Credentials”授权粒度，公开了一个“Token Endpoint”，其中，NF服务消费者可以请求Access Token Request服务。 

AMF使用NRF提供的Nnrf接口，向NRF注册AMF支持的能力信息，以及向NRF查询其他NF。AMF使用Nnrf接口时，有时需要对某些消息参数进行控制处理。 




功能说明 


Nnrf消息参数配置提供Nnrf接口中切片是否支持SD Range、allowednssais的切片最大数量、AMF支持的切片最大数量等配置。 




子主题： 






### NF注册参数配置 
### NF注册参数配置 


背景知识 


NRF通过Nnrf接口向其他NF提供多种服务(NFS，Network Function Service)，具体服务包括如下所定义的各种： 

Nnrf_NFManagement 


 
允许NF实例属性在所属PLMN的NRF上注册、更新、去注册。 

 
允许NRF实例在同一个PLMN中的另一个NRF中注册、更新或去注册其属性信息。也可以使用其他方式更新或去注册NRF Profile，例如，可以通过OA&M更新或去注册NRF Profile。 

 
允许NF订阅以收到新注册的NF实例和NFS的通知。 

 
允许检索当前NRF上已注册的NF实例列表或指定NF实例的属性。 

 

Nnrf_NFDiscovery 


 
允许NF实例通过查询本PLMN的NRF发现其他NF提供的NFS。 

 
允许PLMN内的NRF向其他PLMN（如某特定UE所在的PLMN）内的NRF重新发起发现请求。 

 

Nnrf_AccessToken 

NRF提供了Nnrf_AccessToken服务（用于OAuth2授权），遵循“Client Credentials”授权粒度，公开了一个“Token Endpoint”，其中，NF服务消费者可以请求Access Token Request服务。 

AMF使用NRF提供的Nnrf接口，向NRF注册AMF支持的能力信息，以及向NRF查询其他NF。AMF使用Nnrf接口时，有时需要对某些消息参数进行控制处理。 




功能说明 


NF注册参数配置提供Nnrf接口中切片是否支持SD Range、allowednssais的切片最大数量、AMF支持的切片最大数量等配置。 




子主题： 






#### 修改NF注册参数配置(SET NFREGPARACFG) 
#### 修改NF注册参数配置(SET NFREGPARACFG) 


功能说明 

该命令用于设置NF注册参数，如NRF注册或更新请求消息中携带的allowednssais的切片最大数、Nnrf接口中切片是否支持SD Range等。 

网络切片是一个完整的逻辑网络，包含一系列能够提供一定网络能力和网络特性的网络功能和相应资源。 

NSSAI就是指5G系统中一组S-NSSAI（Single Network Slice Selection Assistance Information）的集合，一个NSSAI最多包含8个S-NSSAI，每个S-NSSAI帮助网络选择特定的网络切片。 

S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息） 可用于标识网络切片，由SST（Slice/Service Type，切片/服务类型）和SD（Slice Differentiator，切片区分信息）组成。 


 
SST（Service/Slice Type）：业务或切片类型，如eMBB（Enhanced Mobile Broadband，增强移动宽带）、mMTC（Massive Machine Type Communication，海量机器类通信）、uRLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信），后续可以继续扩展。 

 
SD（Slice Differentiator，切片区分信息）：其它可以区分切片的信息，比如区域信息，租户信息等，用于进一步区分网络切片，便于选择所有符合所指示的SST的潜在多个网络切片实例 

 

通常情况下，SD是单个单个的，比如000001、000004、000005、000007。SD Range是指连续的多个SD，由start和end两个字段来定义。比如start为000000，end为000005，就代表了从000000到000005的5个SD。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ifsdrange|Nnrf接口中切片是否支持SD Range|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORTSDRANGE|参数作用：该参数用于控制当AMF给NRF发送NF注册或更新等消息时，消息中携带的切片信息，是否可以使用SD（Slice Differentiator，切片区分信息）Range来表达NSSAI。该参数也可以用于标识当AMF接收到NRF消息时，如果消息中包含SD Range，AMF是否可以处理。修改影响：修改参数为是时，影响如下。AMF给NRF发送NF注册或更新等消息时，会把SST相同的连续SD组成SD Range的形式，再发送给NRF。当AMF接收到NRF发送的消息时，可以处理消息中以SD Range形式表示的切片信息。数据来源：本端配置。默认值：否。配置原则：无。
maxallowednssaisnum|携带的授权切片的最大个数|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 8|参数作用：该参数用于控制当AMF给NRF发送NF注册或更新等消息时，每个服务携带的授权切片的最大个数。修改影响：修改该参数，AMF给NRF发送NF注册或更新等消息中，每个服务携带的授权切片的最大个数不会超过该参数的值。数据来源：本端配置。默认值：8。配置原则：无。
maxsnssaisnum|携带的AMF支持的切片的最大个数|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 1024|参数作用：该参数用于控制当AMF给NRF发送NF注册或更新等消息时，携带的AMF支持的切片的最大个数。修改影响：修改该参数，AMF给NRF发送NF注册或更新等消息中，携带的AMF支持的切片的最大个数不会超过该参数的值。数据来源：本端配置。默认值：1024。配置原则：无。




命令举例 


`
设置NRF注册参数：Nnrf接口中切片是否支持SD Range为不支持SD Range，携带的授权切片的最大个数为8个，携带的AMF支持的切片的最大个数为1024个。
SET NFREGPARACFG:IFSDRANGE="NOTSUPPORTSDRANGE",MAXAllOWEDNSSAISNUM=8,MAXSNSSAISNUM= 1024
` 


#### 查询NF注册参数配置(SHOW NFREGPARACFG) 
#### 查询NF注册参数配置(SHOW NFREGPARACFG) 


功能说明 

该命令用于查询NRF注册参数参数，如NRF注册或更新请求消息中携带的allowednssais的切片最大数、Nnrf接口中切片是否支持SD Range等。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
ifsdrange|Nnrf接口中切片是否支持SD Range|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORTSDRANGE|参数作用：该参数用于控制当AMF给NRF发送NF注册或更新等消息时，携带的切片信息，是否可以使用SD Range表达NSSAI。该参数也标识AMF接收到NRF消息时，如果包含SD Range，AMF是否可以处理。
maxallowednssaisnum|携带的授权切片的最大个数|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 8|参数作用：该参数用于控制当AMF给NRF发送NF注册或更新等消息时，携带的授权切片的最大个数。
maxsnssaisnum|携带的AMF支持的切片的最大个数|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 1024|参数作用：该参数用于控制当AMF给NRF发送NF注册或更新等消息时，携带的AMF支持的切片的最大个数。




命令举例 


`
查询NRF注册参数。
SHOW NFREGPARACFG

(No.1) :SHOW NFREGPARACFG
-----------------Namf_MP_0----------------
Nnrf接口中切片是否支持SD Range    携带的授权切片的最大个数    携带的AMF支持的切片的最大个数
--------------------------------------------------------------------------------------
不支持SD Range                    8                           1024   
--------------------------------------------------------------------------------------
记录数：1
执行成功耗时: 0.087 秒

` 


## Nnssf消息参数配置 
## Nnssf消息参数配置 


背景知识 


AMF使用NSSF提供的Nnssf接口，向NSSF获取切片可用性信息时，有时需要对某些消息参数进行控制处理。 




功能说明 


Nnssf消息参数配置提供AllowedNSSAIs的切片最大数、NSSAI是否使用SD Range等配置。 




子主题： 






### Nnssf接口可用性服务协议参数配置 
### Nnssf接口可用性服务协议参数配置 


背景知识 


AMF使用NSSF提供的Nnssf接口，向Nssf更新无线上报的切片可用性信息，以及向NSSF订阅切片可用性信息。AMF使用Nnssf接口时，有时需要对某些消息参数进行控制处理。 




功能说明 


Nnssf接口可用性服务协议参数配置提供单TA下支持的切片最大数量、EANAN选择配置。 




子主题： 






#### 设置Nnssf接口可用性服务参数配置(SET NSSFAVAILPARACFG) 
#### 设置Nnssf接口可用性服务参数配置(SET NSSFAVAILPARACFG) 


功能说明 

本命令用于设置Nnssf接口可用性服务参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
pertanssaisnum|单TA下支持的切片最大数量|参数可选性: 任选参数类型: 数字参数范围: 1-1024默认值: 8|参数作用：该参数标识AMF和NSSF的切片可用性服务，单TA下支持的切片最大数量。修改影响：修改后，影响AMF向NSSF发送订阅请求和更新请求消息中TA的最大个数。数据来源：本端规划。 默认值：8配置原则：根据运营商规划配置。
ifeanan|支持EANAN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数标识AMF是否支持EANAN（清空授权NSSAI可用性通知，Empty Authorized NSSAI Availability Notification）。修改影响：功能开启后，AMF向NSSF发送订阅请求和更新请求时，在Support Feature字段中携带EANAN。并且当NSSF返回空的切片可用性信息时，认为当前TA下无可用切片。数据来源：本端规划。 默认值：不支持。配置原则：根据运营商规划配置。




命令举例 


`
设置Nnssf接口可用性服务参数配置。
SET NSSFAVAILPARACFG:PERTANSSAISNum=8,IFEANAN="YES"
` 


#### 查询Nnssf接口可用性服务参数配置(SHOW NSSFAVAILPARACFG) 
#### 查询Nnssf接口可用性服务参数配置(SHOW NSSFAVAILPARACFG) 


功能说明 

本命令用于查询Nnssf接口可用性服务参数配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
pertanssaisnum|单TA下支持的切片最大数量|参数可选性: 任选参数类型: 数字参数范围: 1-1024默认值: 8|参数作用：该参数标识AMF和NSSF的切片可用性服务，单TA下支持的切片最大数量。修改影响：修改后，影响AMF向NSSF发送订阅请求和更新请求消息中TA的最大个数。数据来源：本端规划。 默认值：8配置原则：根据运营商规划配置。
ifeanan|支持EANAN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数标识AMF是否支持EANAN（清空授权NSSAI可用性通知，Empty Authorized NSSAI Availability Notification）。修改影响：功能开启后，AMF向NSSF发送订阅请求和更新请求时，在Support Feature字段中携带EANAN。并且当NSSF返回空的切片可用性信息时，认为当前TA下无可用切片。数据来源：本端规划。 默认值：不支持。配置原则：根据运营商规划配置。




命令举例 


`
查询Nnssf接口可用性服务参数配置。
SHOW NSSFAVAILPARACFG
` 


## SBI消息URI参数配置 
## SBI消息URI参数配置 


背景知识 


该功能用于设置SBI消息URI参数配置。当需要设置SBI消息中URI携带的参数时，使用该命令进行配置。 




功能说明 


本功能用于用于设置SBI消息中请求URI和回调URI的参数配置。
-  AMF向服务提供方NF发起服务请求操作，可以设置请求URI中的参数
-  AMF向服务提供方NF订阅服务通知，可以设置回调URI中的参数。 




子主题： 






### 设置SBI消息URI携带参数配置(SET SBIMSGURIPARACFG) 
### 设置SBI消息URI携带参数配置(SET SBIMSGURIPARACFG) 


功能说明 

设置SBI消息URI携带参数配置。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
reqUriHostConsMode|请求URI Host构造方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF在发送SBI消息，请求URI Host的构造方式，以及发送PCF AM POLICY建立的URL是根据新老版本决定是否在URI的最后带"/"。IP优先时，优先使用IP构造URI Host。FQDN优先时，优先使用FQDN构造URI Host。
cbUriHostConsMode|回调URI Host构造方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF在发送SBI消息，回调URI Host的构造方式。IP优先时，优先使用IP构造URI Host。FQDN优先时，优先使用FQDN构造URI Host。
AMPolicyURIForm|AM策略关联中URI格式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMPOLIURINEW|本参数用于设置PCF AM POLICY建立URL的构造方式。对新版本使用新版本的方式构造URL，最后不带"/"。对旧版本使用旧版本的方式构造URL，最后带"/"。




命令举例 


`
设置SBI消息URI携带参数配置。
SET SBIMSGURIPARACFG:REQURIHOSTCONSMODE="IPPRIORITY",CBURIHOSTCONSMODE="FQDNPRIORITY",AMPOLICYURIFORM="AMPOLIURINEW"
` 


### 查询SBI消息URI携带参数配置(SHOW SBIMSGURIPARACFG) 
### 查询SBI消息URI携带参数配置(SHOW SBIMSGURIPARACFG) 


功能说明 

该命令用于查询查询SBI消息URI携带参数配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
reqUriHostConsMode|请求URI Host构造方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF在发送SBI消息，请求URI Host的构造方式。IP优先时，优先使用IP构造URI Host。FQDN优先时，优先使用FQDN构造URI Host。
cbUriHostConsMode|回调URI Host构造方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF在发送SBI消息，回调URI Host的构造方式。IP优先时，优先使用IP构造URI Host。FQDN优先时，优先使用FQDN构造URI Host。
AMPolicyURIForm|AM策略关联中URI格式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMPOLIURINEW|本参数用于设置PCF AM POLICY建立URL的构造方式。对新版本使用新版本的方式构造URL，最后不带"/"。对旧版本使用旧版本的方式构造URL，最后带"/"。




命令举例 


`
查询SBI消息URI携带参数配置。
SHOW SBIMSGURIPARACFG:

SHOW SBIMSGURIPARACFG:
--------------------------------Namf_Communication_0-------------------------------
请求URI Host构造方式           回调URI Host构造方式            AM策略关联中URI格式
-----------------------------------------------------------------------------------------------
       优先使用IP地址                         优先使用FQDN                    按PCF支持V1.0.2构造
-----------------------------------------------------------------------------------------------
记录数：1
执行成功耗时: 0.083 秒

` 


# 流程冲突处理策略配置 
# 流程冲突处理策略配置 


背景知识 


UE、无线侧、网络侧可能都会触发与用户相关的流程，AMF在处理这些流程时，各个流程之间可能会产生冲突，对于不同的冲突场景，AMF需要采用不同的处理策略，以优化用户业务体验。 




功能说明 


本功能用于对一些流程冲突场景的处理策略进行调整。 




子主题： 






## 特定流程冲突处理策略配置 
## 特定流程冲突处理策略配置 


背景知识 


UE、无线侧、网络侧可能都会触发与用户相关的流程，AMF在处理这些流程时，各个流程之间可能会产生冲突，对于不同的冲突场景，AMF需要采用不同的处理策略，以优化用户业务体验。 




功能说明 


本功能用于设置一些特定流程的冲突处理策略，包括EBI分配流程冲突处理策略等。 




子主题： 






### 修改特定流程冲突处理策略配置(SET PROCCOLLISIONPOLICY) 
### 修改特定流程冲突处理策略配置(SET PROCCOLLISIONPOLICY) 


功能说明 

该命令用于修改特定流程冲突处理策略配置。 

UE、无线侧、网络侧可能都会触发与用户相关的流程，AMF在处理这些流程时，各个流程之间可能会产生冲突，对于不同的冲突场景，AMF需要采用不同的处理策略，以优化用户业务体验。 


注意事项 


 
本命令执行后，配置立即生效。 

 
本命令最多只能配置1条记录。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ebialloccollision|切换时收到SMF的EBI分配请求消息冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORMAL|参数作用：该参数用于配置当UE正处于切换流程时，如果此时AMF又收到SMF发送的EBI分配请求消息，AMF的处理策略，取值及含义如下：并行：保证SMF发送的EBI分配请求消息能够正常处理。AMF缓存EBI分配请求消息，等待当前流程结束之后再处理EBI请求，或者将EBI请求消息与当前进行处理的流程并行处理。拒绝：不处理SMF发送的EBI分配请求消息，AMF给SMF回送失败响应消息。根据当前正在进行流程，AMF在失败响应消息中携带TEMPORARY_REJECT_HANDOVER_ONGOING原因值给SMF。SMF待切换流程完成后，重新发送EBI分配请求消息给AMF。修改影响：无。数据来源：本端规划。默认值：并行。配置原则：无。
ebiallocregupdate|注册更新时收到SMF的EBI分配请求消息冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORMAL|参数作用：该参数用于配置当UE正处于注册更新流程时，如果此时AMF又收到SMF发送的EBI分配请求消息，AMF的处理策略，取值及含义如下：并行：保证SMF发送的EBI分配请求消息能够正常处理。AMF缓存EBI分配请求消息，等待当前流程结束之后再处理EBI请求，或者将EBI请求消息与当前进行处理的流程并行处理。拒绝：不处理SMF发送的EBI分配请求消息，AMF给SMF回送失败响应消息。根据当前正在进行流程，AMF在失败响应消息中携带TEMPORARY_REJECT_REGISTRATION_ONGOING原因值给SMF。SMF待注册流程完成后，重新发送EBI分配请求消息给AMF。修改影响：无。数据来源：本端规划。默认值：并行。配置原则：无。
n1n2transcollision|切换时收到SMF的PDU修改类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当UE正处于切换流程时，AMF又收到SMF发送的PDU修改类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF发送的N1N2MessageTransfer消息，待UE切换流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_HANDOVER_ONGOING原因值给SMF。SMF待切换完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
n1n2rlsconflictho|切换时收到SMF的PDU释放类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当UE正处于切换流程时，AMF又收到SMF发送的PDU释放类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF发送的N1N2MessageTransfer消息，待UE切换流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_HANDOVER_ONGOING原因值给SMF。SMF待切换完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
n1n2conflictregupt|注册更新时收到SMF的PDU修改类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当AMF正在处理注册更新流程时，又收到SMF发送的PDU修改类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF的N1N2MessageTransfer消息，待注册更新流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_REGISTRATION_ONGOING原因值给对端网元。SMF待注册更新完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
n1n2rlsconflictreg|注册更新时收到SMF的PDU释放类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当AMF正在处理注册更新流程时，又收到SMF发送的PDU释放类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF的N1N2MessageTransfer消息，待注册更新流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_REGISTRATION_ONGOING原因值给对端网元。SMF待注册更新完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
pduestandmob|切换时收到SMF的PDU建立类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当用户正在处理切换流程时，AMF又收到SMF发送的PDU建立类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF发送的N1N2MessageTransfer消息，待切换流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_HANDOVER_ONGOING原因值给对端网元。SMF待切换完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
pduestandregupt|注册更新时收到SMF的PDU建立类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当AMF正在处理注册更新流程时，又收到SMF发送的PDU建立类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF发送的N1N2MessageTransfer消息，待注册更新流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_REGISTRATION_ONGOING原因值给对端网元。SMF待注册更新完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
regConflictN1N2|处理N1N2MessageTransfer时收到注册更新冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUSPEND|参数作用：该参数用于配置，当AMF正在处理N1N2MessageTransfer时，又收到UE的注册更新请求消息，AMF的处理策略，取值及含义如下：挂起N1N2MessageTransfer流程：AMF不处理N1N2MessageTransfer，等待UE的注册更新完成后再恢复处理N1N2MessageTransfer流程。终止N1N2MessageTransfer流程：AMF发送N1N2Transfer Failure Notification给请求NF。修改影响：无。数据来源：本端规划。默认值：挂起N1N2MessageTransfer流程。配置原则：无。
SRSMPLY|业务请求时收到SMF的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置，当AMF正在处理业务请求流程时，又收到SMF的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF的N1N2MessageTransfer消息，待业务请求流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带合适的原因值，SMF待业务请求完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
MOBNONSMPLY|切换时收到非SMF触发的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|该参数用于配置，当AMF正在处理UE切换流程时，又收到非SMF发送的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：0-缓存：AMF缓存非SMF的N1N2MessageTransfer消息，待切换流程处理完成后，再处理非SMF的N1N2MessageTransfer消息。1-拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带合适的原因值，非SMF待切换完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
reguptnonsmply|注册更新时收到非SMF触发的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置，当AMF正在处理注册更新流程时，又收到非SMF的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存非SMF的N1N2MessageTransfer消息，待注册更新流程处理完成后，再处理非SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带合适的原因值，非SMF待注册更新完成后，重新发送N1N2MessageTransfer消息给AMF。修改影响：无。数据来源：本端规划。默认值：缓存。配置原则：无。
DURWAITREGUPD|切换之后等待注册更新时长|参数可选性: 任选参数类型: 数字参数范围: 0-10000默认值: 0|参数作用：在切换过程中，AMF又收到N1N2MessageTransfer消息，AMF缓存N1N2MessageTransfer消息时，如果发现切换的目标TA在之前为用户分配的TA List中时，该参数用于配置在切换完成后是否需等待注册更新，取值及含义如下：取值为0，表示不需等。取值为1-10000之间的数值：表示等待的毫秒数。修改影响：无。数据来源：本端规划。默认值：0。配置原则：无。
ifuectxtransfer|是否处理原因值UE上下文传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于标识AMF是否处理原因值“UE context transfer”，当UE处于inactive态时，AMF收到N1 Container后，会通过N2接口透传给NR（老的NR），eNodeB会发起对用户的寻呼流程，若此时UE已经移动到另外一个NR（新的NR）的覆盖范围内，老的NR无法处理该N2接口消息，老的NR会给AMF回复NAS消息未投递，其中携带UE context transfer原因值，并且通过Xn口通知其他eNodeB寻呼用户。用户在新的NR接入后，新的NR会发起Path Switch流程，AMF需要处理完Path Switch流程后，再向新的NR发送N2接口消息。取值及含义如下：否：AMF不处理原因值“UE context transfer”，会丢弃未投递的NAS-PDU。是：AMF处理原因值“UE context transfer”，会缓存未投递的NAS-PDU。修改影响：无。数据来源：本端规划。默认值：是。配置原则：无。
amfsuppcanceln2rel|AMF是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于配置当AMF收到SMF发送的PDU修改或删除类型的N1N2MessageTransfer消息，并给UE下发N1 SM信令，或给RAN下发N2 SM信令后，又收到RAN侧发起的N2 Release请求消息时，AMF是否支持取消用户无活动触发的N2释放流程，取值及含义如下：不支持：AMF不支持取消用户无活动触发的N2释放流程，并行处理PDU修改或删除流程和N2释放流程，或丢弃PDU修改或删除流程。支持：AMF支持取消用户无活动触发的N2释放流程，继续处理PDU修改或删除流程。修改影响：无。数据来源：本端规划。默认值：不支持。配置原则：无。
ransuppcanceln2rel|RAN是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于配置当AMF收到SMF发送的PDU修改或删除类型的N1N2MessageTransfer消息，并给UE下发N1 SM信令，或给RAN下发N2 SM信令后，又收到RAN侧发起的N2 Release请求消息时，RAN是否支持取消用户无活动触发的N2释放流程，取值及含义如下：不支持：RAN不支持取消用户无活动触发的N2释放流程，并行处理PDU修改或删除流程和N2释放流程，或丢弃PDU修改或删除流程。支持：RAN支持取消用户无活动触发的N2释放流程，继续处理PDU修改或删除流程。修改影响：无。数据来源：本端规划。默认值：不支持。配置原则：无。
canceln2relpendn1sm|AMF感知有下发的N1 SM信令时是否取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置当AMF收到SMF发送的PDU修改或删除类型的N1N2MessageTransfer消息，且AMF感知到已经为UE下发过N1 SM信令后，又收到RAN侧发起的N2 Release请求消息时，是否取消用户无活动触发的N2释放流程，取值及含义如下：否：AMF感知有下发的N1 SM信令时，不取消用户无活动触发的N2释放流程，并行处理PDU修改或删除流程和N2释放流程，或丢弃PDU修改或删除流程。是：AMF感知有下发的N1 SM信令时，取消用户无活动触发的N2释放流程，继续处理PDU修改或删除流程。修改影响：无。数据来源：本端规划。默认值：否。配置原则：无。
canceln2relpendn2sm|AMF感知有下发的N2 SM信令时是否取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置当AMF收到SMF发送的PDU修改或删除类型的N1N2MessageTransfer消息，且AMF感知到已经为RAN下发过N2 SM信令后，又收到RAN侧发起的N2 Release请求消息时，是否取消用户无活动触发的N2释放流程，取值及含义如下：否：AMF感知有下发的N2 SM信令时，不取消用户无活动触发的N2释放流程，并行处理PDU修改或删除流程和N2释放流程，或丢弃PDU修改或删除流程。是：AMF感知有下发的N2 SM信令时，取消用户无活动触发的N2释放流程，继续处理PDU修改或删除流程。修改影响：无。数据来源：本端规划。默认值：否。配置原则：无。




命令举例 


`
设置EBI分配与切换流程冲突处理策略为并行处理。
SET PROCCOLLISIONPOLICY:EBIALLOCCOLLISION="NORMAL"
` 


### 查询特定流程冲突处理策略配置(SHOW PROCCOLLISIONPOLICY) 
### 查询特定流程冲突处理策略配置(SHOW PROCCOLLISIONPOLICY) 


功能说明 

该命令用于查询流程特定冲突处理策略配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
ebialloccollision|切换时收到SMF的EBI分配请求消息冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORMAL|参数作用：该参数用于配置当UE正处于切换流程时，如果此时AMF又收到SMF发送的EBI分配请求消息，AMF的处理策略，取值及含义如下：并行：保证SMF发送的EBI分配请求消息能够正常处理。AMF缓存EBI分配请求消息，等待当前流程结束之后再处理EBI请求，或者将EBI请求消息与当前进行处理的流程并行处理。拒绝：不处理SMF发送的EBI分配请求消息，AMF给SMF回送失败响应消息。根据当前正在进行流程，AMF在失败响应消息中携带TEMPORARY_REJECT_HANDOVER_ONGOING原因值给SMF。SMF待切换流程完成后，重新发送EBI分配请求消息给AMF。
ebiallocregupdate|注册更新时收到SMF的EBI分配请求消息冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NORMAL|参数作用：该参数用于配置当UE正处于注册更新流程时，如果此时AMF又收到SMF发送的EBI分配请求消息，AMF的处理策略，取值及含义如下：并行：保证SMF发送的EBI分配请求消息能够正常处理。AMF缓存EBI分配请求消息，等待当前流程结束之后再处理EBI请求，或者将EBI请求消息与当前进行处理的流程并行处理。拒绝：不处理SMF发送的EBI分配请求消息，AMF给SMF回送失败响应消息。根据当前正在进行流程，AMF在失败响应消息中携带TEMPORARY_REJECT_REGISTRATION_ONGOING原因值给SMF。SMF待注册流程完成后，重新发送EBI分配请求消息给AMF。
n1n2transcollision|切换时收到SMF的PDU修改类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当UE正处于切换流程时，AMF又收到SMF发送的PDU修改类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF发送的N1N2MessageTransfer消息，待UE切换流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_HANDOVER_ONGOING原因值给SMF。SMF待切换完成后，重新发送N1N2MessageTransfer消息给AMF。
n1n2rlsconflictho|切换时收到SMF的PDU释放类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当UE正处于切换流程时，AMF又收到SMF发送的PDU释放类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF发送的N1N2MessageTransfer消息，待UE切换流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_HANDOVER_ONGOING原因值给SMF。SMF待切换完成后，重新发送N1N2MessageTransfer消息给AMF。
n1n2conflictregupt|注册更新时收到SMF的PDU修改类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当AMF正在处理注册更新流程时，又收到SMF发送的PDU修改类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF的N1N2MessageTransfer消息，待注册更新流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_REGISTRATION_ONGOING原因值给对端网元。SMF待注册更新完成后，重新发送N1N2MessageTransfer消息给AMF。
n1n2rlsconflictreg|注册更新时收到SMF的PDU释放类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当AMF正在处理注册更新流程时，又收到SMF发送的PDU释放类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF的N1N2MessageTransfer消息，待注册更新流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_REGISTRATION_ONGOING原因值给对端网元。SMF待注册更新完成后，重新发送N1N2MessageTransfer消息给AMF。
pduestandmob|切换时收到SMF的PDU建立类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当用户正在处理切换流程时，AMF又收到SMF发送的PDU建立类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF发送的N1N2MessageTransfer消息，待切换流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_HANDOVER_ONGOING原因值给对端网元。SMF待切换完成后，重新发送N1N2MessageTransfer消息给AMF。
pduestandregupt|注册更新时收到SMF的PDU建立类型的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置当AMF正在处理注册更新流程时，又收到SMF发送的PDU建立类型的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF发送的N1N2MessageTransfer消息，待注册更新流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带TEMPORARY_REJECT_REGISTRATION_ONGOING原因值给对端网元。SMF待注册更新完成后，重新发送N1N2MessageTransfer消息给AMF。
regConflictN1N2|处理N1N2MessageTransfer时收到注册更新冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUSPEND|参数作用：该参数用于配置，当AMF正在处理N1N2MessageTransfer时，又收到UE的注册更新请求消息，AMF的处理策略，取值及含义如下：挂起N1N2MessageTransfer流程：AMF不处理N1N2MessageTransfer，等待UE的注册更新完成后再恢复处理N1N2MessageTransfer流程。终止N1N2MessageTransfer流程：AMF发送N1N2Transfer Failure Notification给请求NF。
SRSMPLY|业务请求时收到SMF的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置，当AMF正在处理业务请求流程时，又收到SMF的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存SMF的N1N2MessageTransfer消息，待业务请求流程处理完成后，再处理SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带合适的原因值，SMF待业务请求完成后，重新发送N1N2MessageTransfer消息给AMF。
MOBNONSMPLY|切换时收到非SMF触发的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|该参数用于配置，当AMF正在处理UE切换流程时，又收到非SMF发送的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：0-缓存：AMF缓存非SMF的N1N2MessageTransfer消息，待切换流程处理完成后，再处理非SMF的N1N2MessageTransfer消息。1-拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带合适的原因值，非SMF待切换完成后，重新发送N1N2MessageTransfer消息给AMF。
reguptnonsmply|注册更新时收到非SMF触发的N1N2消息传输冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CACHE|参数作用：该参数用于配置，当AMF正在处理注册更新流程时，又收到非SMF的N1N2MessageTransfer消息，AMF的处理策略，取值及含义如下：缓存：AMF缓存非SMF的N1N2MessageTransfer消息，待注册更新流程处理完成后，再处理非SMF的N1N2MessageTransfer消息。拒绝：AMF不处理SMF发送的N1N2MessageTransfer消息，AMF给SMF回送失败响应消息。根据当前正在进行的流程，AMF在失败响应消息中携带合适的原因值，非SMF待注册更新完成后，重新发送N1N2MessageTransfer消息给AMF。
DURWAITREGUPD|切换之后等待注册更新时长|参数可选性: 任选参数类型: 数字参数范围: 0-10000默认值: 0|参数作用：在切换过程中，AMF又收到N1N2MessageTransfer消息，AMF缓存N1N2MessageTransfer消息时，如果发现切换的目标TA在之前为用户分配的TA List中时，该参数用于配置在切换完成后是否需等待注册更新，取值及含义如下：取值为0，表示不需等。取值为1-10000之间的数值：表示等待的毫秒数。
ifuectxtransfer|是否处理原因值UE上下文传输|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于标识AMF是否处理原因值“UE context transfer”，当UE处于inactive态时，AMF收到N1 Container后，会通过N2接口透传给NR（老的NR），eNodeB会发起对用户的寻呼流程，若此时UE已经移动到另外一个NR（新的NR）的覆盖范围内，老的NR无法处理该N2接口消息，老的NR会给AMF回复NAS消息未投递，其中携带UE context transfer原因值，并且通过Xn口通知其他eNodeB寻呼用户。用户在新的NR接入后，新的NR会发起Path Switch流程，AMF需要处理完Path Switch流程后，再向新的NR发送N2接口消息。取值及含义如下：否：AMF不处理原因值“UE context transfer”，会丢弃未投递的NAS-PDU。是：AMF处理原因值“UE context transfer”，会缓存未投递的NAS-PDU。
amfsuppcanceln2rel|AMF是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于配置当AMF收到SMF发送的PDU修改或删除类型的N1N2MessageTransfer消息，并给UE下发N1 SM信令，或给RAN下发N2 SM信令后，又收到RAN侧发起的N2 Release请求消息时，AMF是否支持取消用户无活动触发的N2释放流程，取值及含义如下：不支持：AMF不支持取消用户无活动触发的N2释放流程，并行处理PDU修改或删除流程和N2释放流程，或丢弃PDU修改或删除流程。支持：AMF支持取消用户无活动触发的N2释放流程，继续处理PDU修改或删除流程。修改影响：无。数据来源：本端规划。默认值：不支持。配置原则：无。
ransuppcanceln2rel|RAN是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于配置当AMF收到SMF发送的PDU修改或删除类型的N1N2MessageTransfer消息，并给UE下发N1 SM信令，或给RAN下发N2 SM信令后，又收到RAN侧发起的N2 Release请求消息时，RAN是否支持取消用户无活动触发的N2释放流程，取值及含义如下：不支持：RAN不支持取消用户无活动触发的N2释放流程，并行处理PDU修改或删除流程和N2释放流程，或丢弃PDU修改或删除流程。支持：RAN支持取消用户无活动触发的N2释放流程，继续处理PDU修改或删除流程。
canceln2relpendn1sm|AMF感知有下发的N1 SM信令时是否取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置当AMF收到SMF发送的PDU修改或删除类型的N1N2MessageTransfer消息，且AMF感知到已经为UE下发过N1 SM信令后，又收到RAN侧发起的N2 Release请求消息时，是否取消用户无活动触发的N2释放流程，取值及含义如下：否：AMF感知有下发的N1 SM信令时，不取消用户无活动触发的N2释放流程，并行处理PDU修改或删除流程和N2释放流程，或丢弃PDU修改或删除流程。是：AMF感知有下发的N1 SM信令时，取消用户无活动触发的N2释放流程，继续处理PDU修改或删除流程。
canceln2relpendn2sm|AMF感知有下发的N2 SM信令时是否取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置当AMF收到SMF发送的PDU修改或删除类型的N1N2MessageTransfer消息，且AMF感知到已经为RAN下发过N2 SM信令后，又收到RAN侧发起的N2 Release请求消息时，是否取消用户无活动触发的N2释放流程，取值及含义如下：否：AMF感知有下发的N2 SM信令时，不取消用户无活动触发的N2释放流程，并行处理PDU修改或删除流程和N2释放流程，或丢弃PDU修改或删除流程。是：AMF感知有下发的N2 SM信令时，取消用户无活动触发的N2释放流程，继续处理PDU修改或删除流程。




命令举例 


`
查询特定流程冲突处理策略配置情况。 
SHOW PROCCOLLISIONPOLICY

(No.1) : SHOW PROCCOLLISIONPOLICY:
-----------------Namf_Communication_0----------------
操作维护  切换时收到SMF的EBI分配请求消息冲突处理策略 注册更新时收到SMF的EBI分配请求消息冲突处理策略 切换时收到SMF的PDU修改类型的N1N2消息传输冲突处理策略 切换时收到SMF的PDU释放类型的N1N2消息传输冲突处理策略 注册更新时收到SMF的PDU修改类型的N1N2消息传输冲突处理策略 注册更新时收到SMF的PDU释放类型的N1N2消息传输冲突处理策略 切换时收到SMF的PDU建立类型的N1N2消息传输冲突处理策略 注册更新时收到SMF的PDU建立类型的N1N2消息传输冲突处理策略 处理N1N2MessageTransfer时收到注册更新冲突处理策略 业务请求时收到SMF的N1N2消息传输冲突处理策略 切换时收到非SMF触发的N1N2消息传输冲突处理策略 注册更新时收到非SMF触发的N1N2消息传输冲突处理策略 切换之后等待注册更新时长 是否处理原因值UE上下文传输 AMF是否支持取消用户无活动触发的N2释放流程 RAN是否支持取消用户无活动触发的N2释放流程 AMF感知有下发的N1 SM信令时是否取消用户无活动触发的N2释放流程 AMF感知有下发的N2 SM信令时是否取消用户无活动触发的N2释放流程
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      并行                                       并行                                           缓存                                                 缓存                                                 缓存                                                     缓存                                                     缓存                                                 缓存                                                     挂起N1N2MessageTransfer                           缓存                                        缓存                                          缓存                                              0                        是                         不支持                                    不支持                                    否                                                           否
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-10-08 10:16:48 耗时: 0.468 秒

` 


## 通用流程冲突处理策略配置 
## 通用流程冲突处理策略配置 


背景知识 


UE、无线侧、网络侧可能都会触发与用户相关的流程，AMF在处理这些流程时，各个流程之间可能会产生冲突，对于不同的冲突场景，AMF需要采用不同的处理策略，以优化用户业务体验。 




功能说明 


本功能用于设置通用的流程冲突处理策略，即AMF对于由新收到的消息触发的流程和AMF当前正在处理的流程，两者之间发生冲突时的处理策略。 




子主题： 






### 新增通用流程冲突处理策略配置(ADD GENERALCONFLICTPOLICY) 
### 新增通用流程冲突处理策略配置(ADD GENERALCONFLICTPOLICY) 


功能说明 

该命令用于新增一条流程冲突的处理策略配置。当需要改变AMF的流程冲突的处理策略时，使用该命令。 


注意事项 

本命令执行后，结果立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
newproc|新流程|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF新收到的消息触发的流程。 修改影响：此参数为配置组合关键字之一，不允许通过设置命令修改。 数据来源：本端规划。 默认值：无。配置原则： 无。
oldproc|老流程|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF当前正在处理的流程。 修改影响：此参数为配置组合关键字之一，不允许通过设置命令修改。 数据来源：本端规划。 默认值：无。配置原则： 无。
collpolicy|冲突处理策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-4|参数作用：该参数用于设置当AMF检测到新流程和老流程冲突时，处理该冲突使用的流程冲突策略。0：丢弃：丢弃新消息，继续处理老流程1：拒绝：拒绝新消息，继续处理老流程。2：并行处理：新流程和老流程同时并发处理。3：替换：终止老流程，处理新流程。4：缓存：缓存新消息，继续处理老流程，待老流程处理完成后再处理新流程。修改影响：修改此参数，影响新流程和老流程冲突时使用的冲突处理策略。数据来源：本端规划。默认值：无。配置原则：无。




命令举例 


`
新增一个新流程为“注册”，老流程为“PDU会话建立”的冲突策略为“替换”的通用流程冲突处理策略配置。
ADD GENERALCONFLICTPOLICY:NEWPROC="REGISTRATION",OLDPROC="UEPDUSESSIONESTABLISHMENT",COLLPOLICY="REPLACE"
` 


### 修改通用流程冲突处理策略配置(SET GENERALCONFLICTPOLICY) 
### 修改通用流程冲突处理策略配置(SET GENERALCONFLICTPOLICY) 


功能说明 

该命令用于修改一条流程冲突的处理策略配置, 即修改已配置的新流程和老流程所使用的冲突处理策略。 


注意事项 

本命令执行后，结果立即生效。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
newproc|新流程|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF新收到的消息触发的流程。 修改影响：此参数为配置组合关键字之一，不允许通过设置命令修改。 数据来源：本端规划。 默认值：无。配置原则： 无。
oldproc|老流程|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF当前正在处理的流程。 修改影响：此参数为配置组合关键字之一，不允许通过设置命令修改。 数据来源：本端规划。 默认值：无。配置原则： 无。
collpolicy|冲突处理策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-4|参数作用：该参数用于设置当AMF检测到新流程和老流程冲突时，处理该冲突使用的流程冲突策略。0：丢弃：丢弃新消息，继续处理老流程1：拒绝：拒绝新消息，继续处理老流程。2：并行处理：新流程和老流程同时并发处理。3：替换：终止老流程，处理新流程。4：缓存：缓存新消息，继续处理老流程，待老流程处理完成后再处理新流程。修改影响：修改此参数，影响新流程和老流程冲突时使用的冲突处理策略。数据来源：本端规划。默认值：无。配置原则：无。




命令举例 


`
将已配置的新流程为“注册，老流程为“PDU会话建立”的冲突策略修改为“并行处理”。
SET GENERALCONFLICTPOLICY:NEWPROC="REGISTRATION",OLDPROC="UEPDUSESSIONESTABLISHMENT",COLLPOLICY="CONCURRENT"
` 


### 删除通用流程冲突处理策略配置(DEL GENERALCONFLICTPOLICY) 
### 删除通用流程冲突处理策略配置(DEL GENERALCONFLICTPOLICY) 


功能说明 

该命令用于删除流程冲突的处理策略配置。 


注意事项 

本命令执行后，结果立即生效。 

只能同时使用"新流程"+"老流程"两个关键参数，进行逐条删除。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
newproc|新流程|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF新收到的消息触发的流程。 修改影响：此参数为配置组合关键字之一，不允许通过设置命令修改。 数据来源：本端规划。 默认值：无。配置原则： 无。
oldproc|老流程|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF当前正在处理的流程。 修改影响：此参数为配置组合关键字之一，不允许通过设置命令修改。 数据来源：本端规划。 默认值：无。配置原则： 无。




命令举例 


`
用唯一索引删除一个新流程为“注册”，老流程为“PDU会话建立”的通用流程冲突处理策略配置。
DEL GENERALCONFLICTPOLICY:NEWPROC="REGISTRATION",OLDPROC="UEPDUSESSIONESTABLISHMENT"
` 


### 查询通用流程冲突处理策略配置(SHOW GENERALCONFLICTPOLICY) 
### 查询通用流程冲突处理策略配置(SHOW GENERALCONFLICTPOLICY) 


功能说明 

该命令用于查询流程冲突的处理策略配置。 


注意事项 

本命令执行后，结果立即生效。 

支持单索引、全部查询等方式。 

如果不输入具体的"新流程"和"老流程"，则表示查询所有的通用流程冲突的处理策略配置。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
newproc|新流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF新收到的消息触发的流程。 修改影响：此参数为配置组合关键字之一，不允许通过设置命令修改。 数据来源：本端规划。 默认值：无。配置原则： 无。
oldproc|老流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF当前正在处理的流程。 修改影响：此参数为配置组合关键字之一，不允许通过设置命令修改。 数据来源：本端规划。 默认值：无。配置原则： 无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
newproc|新流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF新收到的消息触发的流程。
oldproc|老流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：本参数用于配置AMF当前正在处理的流程。
collpolicy|冲突处理策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4|参数作用：该参数用于设置通用的流程冲突处理策略，即AMF对于由新收到的消息触发的流程和AMF当前正在处理的流程，两者之间发生冲突时的处理策略。




命令举例 


`
查询全部通用流程冲突处理策略配置。
SHOW GENERALCONFLICTPOLICY

((No.4) : SHOW GENERALCONFLICTPOLICY:
-----------------Namf_Communication_0----------------
操作维护              新流程 老流程      冲突处理策略 
-----------------------------------------------
复制 修改 删除 注册   PDU会话建立        并行处理     
-----------------------------------------------
记录数：1
执行成功开始时间:2021-09-06 11:38:29 耗时: 0.17 秒

` 


# Communication定时器配置 
# Communication定时器配置 


背景知识 


本功能用于设置AMF注册、PDU建立、业务请求、切换等流程中，AMF等待SMF响应的定时器时长，包括如下定时器等。 


 
软参索引1对应的有名定时器：The length of AMF wait SMF rsp Timer 

 
软参索引2对应的有名定时器：The length of AMF wait UDM rsp Timer 

 
软参索引3对应的有名定时器：The length of AMF wait RAN rsp Timer 

 
软参索引4对应的有名定时器：The length of AMF wait UE rsp Timer 

 
软参索引5对应的有名定时器：The length of AMF wait all smf rsp Timer 

 
软参索引6对应的有名定时器：The length of AMF wait NRF discover Timer 

 
软参索引7对应的有名定时器：The length of AMF wait MT rsp Timer 

 
软参索引8对应的有名定时器：The length of AMF wait inter amf rsp Timer 

 
软参索引9对应的有名定时器：The length of AMF wait PCF rsp Timer 

 
软参索引10对应的有名定时器：The length of AMF wait NSSF rsp Timer 

 




功能说明 


本功能用于设置AMF注册、PDU建立、业务请求、切换等流程中，AMF等待SMF响应的定时器时长。 




子主题： 






## 修改AMF有名定时器时长配置(SET DEFPRETIMER) 
## 修改AMF有名定时器时长配置(SET DEFPRETIMER) 


功能说明 

该命令用于设置AMF有名定时器时长配置。 


注意事项 


 
本命令执行后，配置立即生效。 

 
系统的业务数据完成后，本命令中的各个定时器已经存在初始配置值，如果运营商没有特殊需求，无需修改，按初始配置值生效。 

 
所有定时器的时长单位都是毫秒（ms）。 

 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性: 必选参数类型: 数字|参数作用：该参数为有名定时器索引。修改影响：ID、参数名称、宏名定义三者是固定关系，在修改定时器参数值时，不要修改参数名称和宏名定义。数据来源：本端规划。默认值：无。配置原则：每个索引对应一个有名定时器，有不同的含义。索引1对应的内部定时器参数名称：AMF等待SMF更新SM Context响应时长，宏名定义：AMF_WAIT_SMF_UPDATE_RESP_TIMER。索引2对应的内部定时器参数名称：AMF等待UDM响应时长，宏名定义：AMF_WAIT_UDM_RESP_TIMER；该参数用于设置AMF向UDM发送请求消息（如UECM注册请求）后等待UDM响应的时长，单位为毫秒。索引3对应的内部定时器参数名称：AMF等待RAN响应时长，宏名定义：AMF_WAIT_RAN_RESP_TIMER；该参数用于设置AMF向RAN侧投递下行消息（如初始上下文建立请求）后等待RAN侧响应的时长，单位为毫秒。索引4对应的内部定时器参数名称：AMF等待UE响应时长，宏名定义：AMF_WAIT_UE_RESP_TIMER；该参数用于设置AMF向UE投递下行消息（如注册接受）后等待UE响应的时长，单位为毫秒。索引5对应的内部定时器参数名称：AMF等待SMF Context响应时长，宏名定义：AMF_WAIT_SMF_CTX_RESP_TIMER。索引6对应的内部定时器参数名称：AMF等待NRF发现时长，宏名定义：AMF_WAIT_NRF_DISCOVER_TIMER。索引8对应的内部定时器参数名称：AMF等待临局AMF响应时长，宏名定义：AMF_WAIT_INTER_AMF_RESP_TIMER；该参数用于设置5G到5G局间流程AMF向临局AMF发送除UE上下文创建请求外的其他请求消息（如UE Context Transfer请求）后等待临局AMF响应的时长，单位为毫秒。索引9对应的内部定时器参数名称：AMF等待PCF响应时长，宏名定义：AMF_WAIT_PCF_RESP_TIMER；该参数用于设置AMF向PCF发送请求消息（如AM策略关联建立请求）后等待PCF响应的时长，单位为毫秒。索引10对应的内部定时器参数名称：AMF等待NSSF响应时长，宏名定义：AMF_WAIT_NSSF_RESP_TIMER。索引11对应的内部定时器参数名称：AMF等待NRF access token响应时长，宏名定义：AMF_WAIT_NRF_ACCESSTOKEN_TIMER。索引12对应的内部定时器参数名称：AMF NRF Client在NRF注册及更新外的其它流程中等待HTTP响应时长，宏名定义：AMF_NRF_CLIENT_WAIT_HTTP_RESP_TIMER。索引13对应的内部定时器参数名称：AMF等待CREATE UE CONTEXT RSP时长，宏名定义：AMF_WAIT_CREATE_UE_CONTEXT_RESP_TIMER；该参数用于设置5G到5G局间切换流程源局AMF向目标局AMF发送Create UE Context请求消息后等待目标局AMF响应的时长，单位为毫秒。索引14对应的内部定时器参数名称：AMF等待RAN寻呼响应时长，宏名定义：AMF_WAIT_RAN_PAGING_RESP_TIMER。索引15对应的内部定时器参数名称：AMF等待DNS查询响应时长，宏名定义：AMF_WAIT_DNS_QUERY_RESP_TIMER。索引16对应的内部定时器参数名称：AMF等待SMSF响应时长，宏名定义：AMF_WAIT_SMSF_RESP_TIMER；该参数用于设置AMF向SMSF发送请求消息（如SMS Activate请求）后等待SMSF响应的时长，单位为毫秒。索引17对应的内部定时器参数名称：AMF等待AUSF响应时长，宏名定义：AMF_WAIT_AUSF_RESP_TIMER；该参数用于设置AMF向AUSF发送请求消息（如UE Authenticate请求）后等待AUSF响应的时长，单位为毫秒。索引18对应的内部定时器参数名称：AMF等待释放GNB老的NG连接响应时长，宏名定义：AMF_WAIT_REL_OLD_NG_CONNECT_RESP_TIMER。索引19对应的内部定时器参数名称：AMF等待释放SMF老的用户面连接响应时长，宏名定义：AMF_WAIT_DEACT_OLD_UP_CONNECT_RESP_TIMER。索引20对应的内部定时器参数名称：AMF等待CDB查询响应时长，宏名定义：AMF_WAIT_CDB_LOOKUP_RSP_TIMER；该参数用于设置AMF向CDB发送查询用户上下文请求消息后等待CDB响应的时长，单位为毫秒。索引21对应的内部定时器参数名称：AMF等待释放非直传隧道时长，宏名定义：AMF_WAIT_DEL_IND_FORWARD_TUN_TIMER。索引22对应的内部定时器参数名称：NF发现流控延迟时长(毫秒)，宏名定义：AMF_DISCOVERY_FlOW_CTRL_DELAY_TIMER。索引23对应的内部定时器参数名称：AMF NRF Client在NRF注册或更新流程中等待HTTP响应时长，宏名定义：AMF_NRF_CLIENT_WAIT_HTTP_RESP_TIMER_REGUPT。索引24对应的内部定时器参数名称：AMF等待Location Report时长，宏名定义：AMF_WAIT_LOCATION_REPORT_TIMER。索引25对应的内部定时器参数名称：PDU建立流程AMF等待N1N2MessageTransfe时长，宏名定义：AMF_WAIT_N1N2TRANSFER_TIMER。索引26对应的内部定时器参数名称：AMF等待UE的ConfigUpdateComplete时长，宏名定义：AMF_WAIT_UE_CONFIG_UPDATE_CMP_TIMER。索引27对应的内部定时器参数名称：AMF向批量RAN更新间隔时长，宏名定义：AMF_BATCH_RAN_UPDATE_INTERVAL_TIMER。索引28对应的内部定时器参数名称：AMF等待SMF创建SM Context响应时长，宏名定义：AMF_WAIT_SMF_CRT_RESP_TIMER。索引29对应的内部定时器参数名称：AMF等待SMF释放SM Context响应时长，宏名定义：AMF_WAIT_SMF_RLS_RESP_TIMER。索引30对应的内部定时器参数名称：PDU重复建立AMF等待SM context status notification时长，宏名定义：AMF_WAIT_SMCTXT_STATUS_NOTIFY_TIMER。索引31对应的内部定时器参数名称：收到NAS NON DELIVERY INDICATION时AMF等待切换完成时长，宏名定义：WAIT_HO_COMPLETE_TIMER_LENGTH。索引32对应的内部定时器参数名称：AMF等待Handover Notify消息时长，宏名定义：AMF_WAIT_HO_NOTIFY_TIMER。索引33对应的内部定时器参数名称：AMF等待Uplink RAN Status Transfer消息时长，宏名定义：AMF_WAIT_UPLINK_RAN_STATUS_TRANSFER_TIMER。索引34对应的内部定时器参数名称：AMF等待Release UE Context Response消息时长，宏名定义：AMF_WAIT_RELEASE_UE_CONTEXT_RESP_TIMER。索引35对应的内部定时器参数名称：AMF等待N2 Info Notify消息时长，宏名定义：AMF_WAIT_N2_INFO_NOTIFY_TIMER。索引36对应的内部定时器参数名称：AMF等待N2 Info Notify Ack消息时长，宏名定义：AMF_WAIT_N2_INFO_NOTIFY_ACK_TIMER。索引37对应的内部定时器参数名称：AMF等待Relocation Complete Notification消息时长，宏名定义：AMF_WAIT_FORWARD_RELOCATION_COMPLETE_TIMER。索引38对应的内部定时器参数名称：AMF等待Relocation Complete Ack消息时长，宏名定义：AMF_WAIT_FORWARD_RELOCATION_COMPLETE_ACK_TIMER。索引39对应的内部定时器参数名称：局间老局AMF等待 RegistrationStatusUpdate 消息时长，宏名定义：AMF_WAIT_REGISTRATION_STATUS_UPDATE_TIMER。索引40对应的内部定时器参数名称：AMF等待切换之后的注册更新消息时长，宏名定义：AMF_WAIT_REGISTRATION_AFTER_HO_TIMER。索引41对应的内部定时器参数名称：Namf_Communication服务等待Namf_EventExposure服务响应时长，宏名定义：AMF_WAIT_RESPONSE_FROM_EEX_TIMER。索引42对应的内部定时器参数名称：收到N1N2Transfer消息当前TA不在areaOfValidity时延迟发送Update SMContext request时长，宏名定义：AMF_DELAY_SEND_UPDATE_TIMER。索引43对应的内部定时器参数名称：AMF等待处理用量报告的切换流程的时长，宏名定义：AMF_WAIT_HO_PROCESS_USAGEREPORT_TIMER。索引44对应的内部定时器参数名称：AMF等待发送缓存的PDU SESSION RESOURCE SETUP REQUEST消息时长，宏名定义：AMF_WAIT_SEND_BUFFER_PDUSETUP_TIMER。索引45对应的内部定时器参数名称：Namf_Communication等待Namf_Location服务发送的Get LMF ID Response消息时长，宏名定义：AMF_WAIT_LOCATION_GET_LMFID_RESP_TIMER。索引46对应的内部定时器参数名称：AMF等待5G-EIR响应定时器时长，宏名定义：AMF_WAIT_EIR_RESP_TIMER。索引47对应的内部定时器参数名称：Namf_Communication等待Namf_Location服务发送的MOLR Response消息时长，宏名定义：AMF_WAIT_LOCATION_MOLR_RESP_TIMER。索引48对应的内部定时器参数名称：AMF等待UE发送的MOLR响应时长，宏名定义：AMF_WAIT_UE_MOLR_RESP_TIMER。索引49对应的内部定时器参数名称：Namf_Communication服务在切换流程中等待Namf_EventExposure服务响应时长，宏名定义：AMF_WAIT_RESPONSE_IN_HANDOVER_FROM_EEX_TIMER。索引50对应的内部定时器参数名称：4G到5G切换流程发生AMF重定向，初始AMF等待目标AMF的重定向UE上下文响应消息时长，宏名定义：AMF_WAIT_UECONTEXT_RELOCATED_DATA_RESP_TIMER。索引51对应的内部定时器参数名称：AMF等待Take Over通知SMF响应时长，宏名定义：AMF_WAIT_TAKEOVER_NOTIFY_SMF_RESP_TIMER。
VALUE|当前时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器的当前取值。修改影响：定时器的当前时长涉及多个网元之间的数据一致，不能随意修改，如果修改错误会导致网元间配合失败，流程失败。数据来源：本端规划。默认值：无。配置原则：无。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性: 任选参数类型: 数字|参数作用：该参数为有名定时器的索引。每个索引对应一个有名定时器，有不同的含义。索引1对应的内部定时器参数名称：AMF等待SMF更新SM Context响应时长，宏名定义：AMF_WAIT_SMF_UPDATE_RESP_TIMER。索引2对应的内部定时器参数名称：AMF等待UDM响应时长，宏名定义：AMF_WAIT_UDM_RESP_TIMER；该参数用于设置AMF向UDM发送请求消息（如UECM注册请求）后等待UDM响应的时长，单位为毫秒。索引3对应的内部定时器参数名称：AMF等待RAN响应时长，宏名定义：AMF_WAIT_RAN_RESP_TIMER；该参数用于设置AMF向RAN侧投递下行消息（如初始上下文建立请求）后等待RAN侧响应的时长，单位为毫秒。索引4对应的内部定时器参数名称：AMF等待UE响应时长，宏名定义：AMF_WAIT_UE_RESP_TIMER；该参数用于设置AMF向UE投递下行消息（如注册接受）后等待UE响应的时长，单位为毫秒。索引5对应的内部定时器参数名称：AMF等待SMF Context响应时长，宏名定义：AMF_WAIT_SMF_CTX_RESP_TIMER。索引6对应的内部定时器参数名称：AMF等待NRF发现时长，宏名定义：AMF_WAIT_NRF_DISCOVER_TIMER。索引8对应的内部定时器参数名称：AMF等待临局AMF响应时长，宏名定义：AMF_WAIT_INTER_AMF_RESP_TIMER；该参数用于设置5G到5G局间流程AMF向临局AMF发送除UE上下文创建请求外的其他请求消息（如UE Context Transfer请求）后等待临局AMF响应的时长，单位为毫秒。索引9对应的内部定时器参数名称：AMF等待PCF响应时长，宏名定义：AMF_WAIT_PCF_RESP_TIMER；该参数用于设置AMF向PCF发送请求消息（如AM策略关联建立请求）后等待PCF响应的时长，单位为毫秒。索引10对应的内部定时器参数名称：AMF等待NSSF响应时长，宏名定义：AMF_WAIT_NSSF_RESP_TIMER。索引11对应的内部定时器参数名称：AMF等待NRF access token响应时长，宏名定义：AMF_WAIT_NRF_ACCESSTOKEN_TIMER。索引12对应的内部定时器参数名称：AMF NRF Client在NRF注册及更新外的其它流程中等待HTTP响应时长，宏名定义：AMF_NRF_CLIENT_WAIT_HTTP_RESP_TIMER。索引13对应的内部定时器参数名称：AMF等待CREATE UE CONTEXT RSP时长，宏名定义：AMF_WAIT_CREATE_UE_CONTEXT_RESP_TIMER；该参数用于设置5G到5G局间切换流程源局AMF向目标局AMF发送Create UE Context请求消息后等待目标局AMF响应的时长，单位为毫秒。索引14对应的内部定时器参数名称：AMF等待RAN寻呼响应时长，宏名定义：AMF_WAIT_RAN_PAGING_RESP_TIMER。索引15对应的内部定时器参数名称：AMF等待DNS查询响应时长，宏名定义：AMF_WAIT_DNS_QUERY_RESP_TIMER。索引16对应的内部定时器参数名称：AMF等待SMSF响应时长，宏名定义：AMF_WAIT_SMSF_RESP_TIMER；该参数用于设置AMF向SMSF发送请求消息（如SMS Activate请求）后等待SMSF响应的时长，单位为毫秒。索引17对应的内部定时器参数名称：AMF等待AUSF响应时长，宏名定义：AMF_WAIT_AUSF_RESP_TIMER；该参数用于设置AMF向AUSF发送请求消息（如UE Authenticate请求）后等待AUSF响应的时长，单位为毫秒。索引18对应的内部定时器参数名称：AMF等待释放GNB老的NG连接响应时长，宏名定义：AMF_WAIT_REL_OLD_NG_CONNECT_RESP_TIMER。索引19对应的内部定时器参数名称：AMF等待释放SMF老的用户面连接响应时长，宏名定义：AMF_WAIT_DEACT_OLD_UP_CONNECT_RESP_TIMER。索引20对应的内部定时器参数名称：AMF等待CDB查询响应时长，宏名定义：AMF_WAIT_CDB_LOOKUP_RSP_TIMER；该参数用于设置AMF向CDB发送查询用户上下文请求消息后等待CDB响应的时长，单位为毫秒。索引21对应的内部定时器参数名称：AMF等待释放非直传隧道时长，宏名定义：AMF_WAIT_DEL_IND_FORWARD_TUN_TIMER。索引22对应的内部定时器参数名称：NF发现流控延迟时长(毫秒)，宏名定义：AMF_DISCOVERY_FlOW_CTRL_DELAY_TIMER。索引23对应的内部定时器参数名称：AMF NRF Client在NRF注册或更新流程中等待HTTP响应时长，宏名定义：AMF_NRF_CLIENT_WAIT_HTTP_RESP_TIMER_REGUPT。索引24对应的内部定时器参数名称：AMF等待Location Report时长，宏名定义：AMF_WAIT_LOCATION_REPORT_TIMER。索引25对应的内部定时器参数名称：PDU建立流程AMF等待N1N2MessageTransfe时长，宏名定义：AMF_WAIT_N1N2TRANSFER_TIMER。索引26对应的内部定时器参数名称：AMF等待UE的ConfigUpdateComplete时长，宏名定义：AMF_WAIT_UE_CONFIG_UPDATE_CMP_TIMER。索引27对应的内部定时器参数名称：AMF向批量RAN更新间隔时长，宏名定义：AMF_BATCH_RAN_UPDATE_INTERVAL_TIMER。索引28对应的内部定时器参数名称：AMF等待SMF创建SM Context响应时长，宏名定义：AMF_WAIT_SMF_CRT_RESP_TIMER。索引29对应的内部定时器参数名称：AMF等待SMF释放SM Context响应时长，宏名定义：AMF_WAIT_SMF_RLS_RESP_TIMER。索引30对应的内部定时器参数名称：PDU重复建立AMF等待SM context status notification时长，宏名定义：AMF_WAIT_SMCTXT_STATUS_NOTIFY_TIMER。索引31对应的内部定时器参数名称：收到NAS NON DELIVERY INDICATION时AMF等待切换完成时长，宏名定义：WAIT_HO_COMPLETE_TIMER_LENGTH。索引32对应的内部定时器参数名称：AMF等待Handover Notify消息时长，宏名定义：AMF_WAIT_HO_NOTIFY_TIMER。索引33对应的内部定时器参数名称：AMF等待Uplink RAN Status Transfer消息时长，宏名定义：AMF_WAIT_UPLINK_RAN_STATUS_TRANSFER_TIMER。索引34对应的内部定时器参数名称：AMF等待Release UE Context Response消息时长，宏名定义：AMF_WAIT_RELEASE_UE_CONTEXT_RESP_TIMER。索引35对应的内部定时器参数名称：AMF等待N2 Info Notify消息时长，宏名定义：AMF_WAIT_N2_INFO_NOTIFY_TIMER。索引36对应的内部定时器参数名称：AMF等待N2 Info Notify Ack消息时长，宏名定义：AMF_WAIT_N2_INFO_NOTIFY_ACK_TIMER。索引37对应的内部定时器参数名称：AMF等待Relocation Complete Notification消息时长，宏名定义：AMF_WAIT_FORWARD_RELOCATION_COMPLETE_TIMER。索引38对应的内部定时器参数名称：AMF等待Relocation Complete Ack消息时长，宏名定义：AMF_WAIT_FORWARD_RELOCATION_COMPLETE_ACK_TIMER。索引39对应的内部定时器参数名称：局间老局AMF等待 RegistrationStatusUpdate 消息时长，宏名定义：AMF_WAIT_REGISTRATION_STATUS_UPDATE_TIMER。索引40对应的内部定时器参数名称：AMF等待切换之后的注册更新消息时长，宏名定义：AMF_WAIT_REGISTRATION_AFTER_HO_TIMER。索引41对应的内部定时器参数名称：Namf_Communication服务等待Namf_EventExposure服务响应时长，宏名定义：AMF_WAIT_RESPONSE_FROM_EEX_TIMER。索引42对应的内部定时器参数名称：收到N1N2Transfer消息当前TA不在areaOfValidity时延迟发送Update SMContext request时长，宏名定义：AMF_DELAY_SEND_UPDATE_TIMER。索引43对应的内部定时器参数名称：AMF等待处理用量报告的切换流程的时长，宏名定义：AMF_WAIT_HO_PROCESS_USAGEREPORT_TIMER。索引44对应的内部定时器参数名称：AMF等待发送缓存的PDU SESSION RESOURCE SETUP REQUEST消息时长，宏名定义：AMF_WAIT_SEND_BUFFER_PDUSETUP_TIMER。索引45对应的内部定时器参数名称：Namf_Communication等待Namf_Location服务发送的Get LMF ID Response消息时长，宏名定义：AMF_WAIT_LOCATION_GET_LMFID_RESP_TIMER。索引46对应的内部定时器参数名称：AMF等待5G-EIR响应定时器时长，宏名定义：AMF_WAIT_EIR_RESP_TIMER。索引47对应的内部定时器参数名称：Namf_Communication等待Namf_Location服务发送的MOLR Response消息时长，宏名定义：AMF_WAIT_LOCATION_MOLR_RESP_TIMER。索引48对应的内部定时器参数名称：AMF等待UE发送的MOLR响应时长，宏名定义：AMF_WAIT_UE_MOLR_RESP_TIMER。索引49对应的内部定时器参数名称：Namf_Communication服务在切换流程中等待Namf_EventExposure服务响应时长，宏名定义：AMF_WAIT_RESPONSE_IN_HANDOVER_FROM_EEX_TIMER。索引50对应的内部定时器参数名称：4G到5G切换流程发生AMF重定向，初始AMF等待目标AMF的重定向UE上下文响应消息时长，宏名定义：AMF_WAIT_UECONTEXT_RELOCATED_DATA_RESP_TIMER。索引51对应的内部定时器参数名称：AMF等待Take Over通知SMF响应时长，宏名定义：AMF_WAIT_TAKEOVER_NOTIFY_SMF_RESP_TIMER。
VALUE|当前时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器当前取值。
DEFAULTVALUE|默认时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器默认取值。
MINVALUE|最小时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器最小值。
MAXVALUE|最大时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器最大值。
DESC|定时器名称|参数可选性: 任选参数类型: 字符串参数范围: 0-180|参数作用：本参数用于设置定时器的名称，代表每个定时器的含义。
MACRODEFINE|定时器宏名|参数可选性: 任选参数类型: 字符串参数范围: 0-180|参数作用：本参数用于设置定时器的宏名。




命令举例 


`
设置索引为1的有名定时器，取值为15s。
SET DEFPRETIMER:ID=1,VALUE=15000
` 


## 查询AMF有名定时器时长配置(SHOW DEFPRETIMER) 
## 查询AMF有名定时器时长配置(SHOW DEFPRETIMER) 


功能说明 

该命令用于查询AMF当前设置的有名定时器时长。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性: 任选参数类型: 数字|参数作用：该参数为有名定时器索引。修改影响：ID、参数名称、宏名定义三者是固定关系，在修改定时器参数值时，不要修改参数名称和宏名定义。数据来源：本端规划。默认值：无。配置原则：每个索引对应一个有名定时器，有不同的含义。索引1对应的内部定时器参数名称：AMF等待SMF更新SM Context响应时长，宏名定义：AMF_WAIT_SMF_UPDATE_RESP_TIMER。索引2对应的内部定时器参数名称：AMF等待UDM响应时长，宏名定义：AMF_WAIT_UDM_RESP_TIMER；该参数用于设置AMF向UDM发送请求消息（如UECM注册请求）后等待UDM响应的时长，单位为毫秒。索引3对应的内部定时器参数名称：AMF等待RAN响应时长，宏名定义：AMF_WAIT_RAN_RESP_TIMER；该参数用于设置AMF向RAN侧投递下行消息（如初始上下文建立请求）后等待RAN侧响应的时长，单位为毫秒。索引4对应的内部定时器参数名称：AMF等待UE响应时长，宏名定义：AMF_WAIT_UE_RESP_TIMER；该参数用于设置AMF向UE投递下行消息（如注册接受）后等待UE响应的时长，单位为毫秒。索引5对应的内部定时器参数名称：AMF等待SMF Context响应时长，宏名定义：AMF_WAIT_SMF_CTX_RESP_TIMER。索引6对应的内部定时器参数名称：AMF等待NRF发现时长，宏名定义：AMF_WAIT_NRF_DISCOVER_TIMER。索引8对应的内部定时器参数名称：AMF等待临局AMF响应时长，宏名定义：AMF_WAIT_INTER_AMF_RESP_TIMER；该参数用于设置5G到5G局间流程AMF向临局AMF发送除UE上下文创建请求外的其他请求消息（如UE Context Transfer请求）后等待临局AMF响应的时长，单位为毫秒。索引9对应的内部定时器参数名称：AMF等待PCF响应时长，宏名定义：AMF_WAIT_PCF_RESP_TIMER；该参数用于设置AMF向PCF发送请求消息（如AM策略关联建立请求）后等待PCF响应的时长，单位为毫秒。索引10对应的内部定时器参数名称：AMF等待NSSF响应时长，宏名定义：AMF_WAIT_NSSF_RESP_TIMER。索引11对应的内部定时器参数名称：AMF等待NRF access token响应时长，宏名定义：AMF_WAIT_NRF_ACCESSTOKEN_TIMER。索引12对应的内部定时器参数名称：AMF NRF Client在NRF注册及更新外的其它流程中等待HTTP响应时长，宏名定义：AMF_NRF_CLIENT_WAIT_HTTP_RESP_TIMER。索引13对应的内部定时器参数名称：AMF等待CREATE UE CONTEXT RSP时长，宏名定义：AMF_WAIT_CREATE_UE_CONTEXT_RESP_TIMER；该参数用于设置5G到5G局间切换流程源局AMF向目标局AMF发送Create UE Context请求消息后等待目标局AMF响应的时长，单位为毫秒。索引14对应的内部定时器参数名称：AMF等待RAN寻呼响应时长，宏名定义：AMF_WAIT_RAN_PAGING_RESP_TIMER。索引15对应的内部定时器参数名称：AMF等待DNS查询响应时长，宏名定义：AMF_WAIT_DNS_QUERY_RESP_TIMER。索引16对应的内部定时器参数名称：AMF等待SMSF响应时长，宏名定义：AMF_WAIT_SMSF_RESP_TIMER；该参数用于设置AMF向SMSF发送请求消息（如SMS Activate请求）后等待SMSF响应的时长，单位为毫秒。索引17对应的内部定时器参数名称：AMF等待AUSF响应时长，宏名定义：AMF_WAIT_AUSF_RESP_TIMER；该参数用于设置AMF向AUSF发送请求消息（如UE Authenticate请求）后等待AUSF响应的时长，单位为毫秒。索引18对应的内部定时器参数名称：AMF等待释放GNB老的NG连接响应时长，宏名定义：AMF_WAIT_REL_OLD_NG_CONNECT_RESP_TIMER。索引19对应的内部定时器参数名称：AMF等待释放SMF老的用户面连接响应时长，宏名定义：AMF_WAIT_DEACT_OLD_UP_CONNECT_RESP_TIMER。索引20对应的内部定时器参数名称：AMF等待CDB查询响应时长，宏名定义：AMF_WAIT_CDB_LOOKUP_RSP_TIMER；该参数用于设置AMF向CDB发送查询用户上下文请求消息后等待CDB响应的时长，单位为毫秒。索引21对应的内部定时器参数名称：AMF等待释放非直传隧道时长，宏名定义：AMF_WAIT_DEL_IND_FORWARD_TUN_TIMER。索引22对应的内部定时器参数名称：NF发现流控延迟时长(毫秒)，宏名定义：AMF_DISCOVERY_FlOW_CTRL_DELAY_TIMER。索引23对应的内部定时器参数名称：AMF NRF Client在NRF注册或更新流程中等待HTTP响应时长，宏名定义：AMF_NRF_CLIENT_WAIT_HTTP_RESP_TIMER_REGUPT。索引24对应的内部定时器参数名称：AMF等待Location Report时长，宏名定义：AMF_WAIT_LOCATION_REPORT_TIMER。索引25对应的内部定时器参数名称：PDU建立流程AMF等待N1N2MessageTransfe时长，宏名定义：AMF_WAIT_N1N2TRANSFER_TIMER。索引26对应的内部定时器参数名称：AMF等待UE的ConfigUpdateComplete时长，宏名定义：AMF_WAIT_UE_CONFIG_UPDATE_CMP_TIMER。索引27对应的内部定时器参数名称：AMF向批量RAN更新间隔时长，宏名定义：AMF_BATCH_RAN_UPDATE_INTERVAL_TIMER。索引28对应的内部定时器参数名称：AMF等待SMF创建SM Context响应时长，宏名定义：AMF_WAIT_SMF_CRT_RESP_TIMER。索引29对应的内部定时器参数名称：AMF等待SMF释放SM Context响应时长，宏名定义：AMF_WAIT_SMF_RLS_RESP_TIMER。索引30对应的内部定时器参数名称：PDU重复建立AMF等待SM context status notification时长，宏名定义：AMF_WAIT_SMCTXT_STATUS_NOTIFY_TIMER。索引31对应的内部定时器参数名称：收到NAS NON DELIVERY INDICATION时AMF等待切换完成时长，宏名定义：WAIT_HO_COMPLETE_TIMER_LENGTH。索引32对应的内部定时器参数名称：AMF等待Handover Notify消息时长，宏名定义：AMF_WAIT_HO_NOTIFY_TIMER。索引33对应的内部定时器参数名称：AMF等待Uplink RAN Status Transfer消息时长，宏名定义：AMF_WAIT_UPLINK_RAN_STATUS_TRANSFER_TIMER。索引34对应的内部定时器参数名称：AMF等待Release UE Context Response消息时长，宏名定义：AMF_WAIT_RELEASE_UE_CONTEXT_RESP_TIMER。索引35对应的内部定时器参数名称：AMF等待N2 Info Notify消息时长，宏名定义：AMF_WAIT_N2_INFO_NOTIFY_TIMER。索引36对应的内部定时器参数名称：AMF等待N2 Info Notify Ack消息时长，宏名定义：AMF_WAIT_N2_INFO_NOTIFY_ACK_TIMER。索引37对应的内部定时器参数名称：AMF等待Relocation Complete Notification消息时长，宏名定义：AMF_WAIT_FORWARD_RELOCATION_COMPLETE_TIMER。索引38对应的内部定时器参数名称：AMF等待Relocation Complete Ack消息时长，宏名定义：AMF_WAIT_FORWARD_RELOCATION_COMPLETE_ACK_TIMER。索引39对应的内部定时器参数名称：局间老局AMF等待 RegistrationStatusUpdate 消息时长，宏名定义：AMF_WAIT_REGISTRATION_STATUS_UPDATE_TIMER。索引40对应的内部定时器参数名称：AMF等待切换之后的注册更新消息时长，宏名定义：AMF_WAIT_REGISTRATION_AFTER_HO_TIMER。索引41对应的内部定时器参数名称：Namf_Communication服务等待Namf_EventExposure服务响应时长，宏名定义：AMF_WAIT_RESPONSE_FROM_EEX_TIMER。索引42对应的内部定时器参数名称：收到N1N2Transfer消息当前TA不在areaOfValidity时延迟发送Update SMContext request时长，宏名定义：AMF_DELAY_SEND_UPDATE_TIMER。索引43对应的内部定时器参数名称：AMF等待处理用量报告的切换流程的时长，宏名定义：AMF_WAIT_HO_PROCESS_USAGEREPORT_TIMER。索引44对应的内部定时器参数名称：AMF等待发送缓存的PDU SESSION RESOURCE SETUP REQUEST消息时长，宏名定义：AMF_WAIT_SEND_BUFFER_PDUSETUP_TIMER。索引45对应的内部定时器参数名称：Namf_Communication等待Namf_Location服务发送的Get LMF ID Response消息时长，宏名定义：AMF_WAIT_LOCATION_GET_LMFID_RESP_TIMER。索引46对应的内部定时器参数名称：AMF等待5G-EIR响应定时器时长，宏名定义：AMF_WAIT_EIR_RESP_TIMER。索引47对应的内部定时器参数名称：Namf_Communication等待Namf_Location服务发送的MOLR Response消息时长，宏名定义：AMF_WAIT_LOCATION_MOLR_RESP_TIMER。索引48对应的内部定时器参数名称：AMF等待UE发送的MOLR响应时长，宏名定义：AMF_WAIT_UE_MOLR_RESP_TIMER。索引49对应的内部定时器参数名称：Namf_Communication服务在切换流程中等待Namf_EventExposure服务响应时长，宏名定义：AMF_WAIT_RESPONSE_IN_HANDOVER_FROM_EEX_TIMER。索引50对应的内部定时器参数名称：4G到5G切换流程发生AMF重定向，初始AMF等待目标AMF的重定向UE上下文响应消息时长，宏名定义：AMF_WAIT_UECONTEXT_RELOCATED_DATA_RESP_TIMER。索引51对应的内部定时器参数名称：AMF等待Take Over通知SMF响应时长，宏名定义：AMF_WAIT_TAKEOVER_NOTIFY_SMF_RESP_TIMER。




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|ID|参数可选性: 任选参数类型: 数字|参数作用：该参数为有名定时器的索引。每个索引对应一个有名定时器，有不同的含义。索引1对应的内部定时器参数名称：AMF等待SMF更新SM Context响应时长，宏名定义：AMF_WAIT_SMF_UPDATE_RESP_TIMER。索引2对应的内部定时器参数名称：AMF等待UDM响应时长，宏名定义：AMF_WAIT_UDM_RESP_TIMER；该参数用于设置AMF向UDM发送请求消息（如UECM注册请求）后等待UDM响应的时长，单位为毫秒。索引3对应的内部定时器参数名称：AMF等待RAN响应时长，宏名定义：AMF_WAIT_RAN_RESP_TIMER；该参数用于设置AMF向RAN侧投递下行消息（如初始上下文建立请求）后等待RAN侧响应的时长，单位为毫秒。索引4对应的内部定时器参数名称：AMF等待UE响应时长，宏名定义：AMF_WAIT_UE_RESP_TIMER；该参数用于设置AMF向UE投递下行消息（如注册接受）后等待UE响应的时长，单位为毫秒。索引5对应的内部定时器参数名称：AMF等待SMF Context响应时长，宏名定义：AMF_WAIT_SMF_CTX_RESP_TIMER。索引6对应的内部定时器参数名称：AMF等待NRF发现时长，宏名定义：AMF_WAIT_NRF_DISCOVER_TIMER。索引8对应的内部定时器参数名称：AMF等待临局AMF响应时长，宏名定义：AMF_WAIT_INTER_AMF_RESP_TIMER；该参数用于设置5G到5G局间流程AMF向临局AMF发送除UE上下文创建请求外的其他请求消息（如UE Context Transfer请求）后等待临局AMF响应的时长，单位为毫秒。索引9对应的内部定时器参数名称：AMF等待PCF响应时长，宏名定义：AMF_WAIT_PCF_RESP_TIMER；该参数用于设置AMF向PCF发送请求消息（如AM策略关联建立请求）后等待PCF响应的时长，单位为毫秒。索引10对应的内部定时器参数名称：AMF等待NSSF响应时长，宏名定义：AMF_WAIT_NSSF_RESP_TIMER。索引11对应的内部定时器参数名称：AMF等待NRF access token响应时长，宏名定义：AMF_WAIT_NRF_ACCESSTOKEN_TIMER。索引12对应的内部定时器参数名称：AMF NRF Client在NRF注册及更新外的其它流程中等待HTTP响应时长，宏名定义：AMF_NRF_CLIENT_WAIT_HTTP_RESP_TIMER。索引13对应的内部定时器参数名称：AMF等待CREATE UE CONTEXT RSP时长，宏名定义：AMF_WAIT_CREATE_UE_CONTEXT_RESP_TIMER；该参数用于设置5G到5G局间切换流程源局AMF向目标局AMF发送Create UE Context请求消息后等待目标局AMF响应的时长，单位为毫秒。索引14对应的内部定时器参数名称：AMF等待RAN寻呼响应时长，宏名定义：AMF_WAIT_RAN_PAGING_RESP_TIMER。索引15对应的内部定时器参数名称：AMF等待DNS查询响应时长，宏名定义：AMF_WAIT_DNS_QUERY_RESP_TIMER。索引16对应的内部定时器参数名称：AMF等待SMSF响应时长，宏名定义：AMF_WAIT_SMSF_RESP_TIMER；该参数用于设置AMF向SMSF发送请求消息（如SMS Activate请求）后等待SMSF响应的时长，单位为毫秒。索引17对应的内部定时器参数名称：AMF等待AUSF响应时长，宏名定义：AMF_WAIT_AUSF_RESP_TIMER；该参数用于设置AMF向AUSF发送请求消息（如UE Authenticate请求）后等待AUSF响应的时长，单位为毫秒。索引18对应的内部定时器参数名称：AMF等待释放GNB老的NG连接响应时长，宏名定义：AMF_WAIT_REL_OLD_NG_CONNECT_RESP_TIMER。索引19对应的内部定时器参数名称：AMF等待释放SMF老的用户面连接响应时长，宏名定义：AMF_WAIT_DEACT_OLD_UP_CONNECT_RESP_TIMER。索引20对应的内部定时器参数名称：AMF等待CDB查询响应时长，宏名定义：AMF_WAIT_CDB_LOOKUP_RSP_TIMER；该参数用于设置AMF向CDB发送查询用户上下文请求消息后等待CDB响应的时长，单位为毫秒。索引21对应的内部定时器参数名称：AMF等待释放非直传隧道时长，宏名定义：AMF_WAIT_DEL_IND_FORWARD_TUN_TIMER。索引22对应的内部定时器参数名称：NF发现流控延迟时长(毫秒)，宏名定义：AMF_DISCOVERY_FlOW_CTRL_DELAY_TIMER。索引23对应的内部定时器参数名称：AMF NRF Client在NRF注册或更新流程中等待HTTP响应时长，宏名定义：AMF_NRF_CLIENT_WAIT_HTTP_RESP_TIMER_REGUPT。索引24对应的内部定时器参数名称：AMF等待Location Report时长，宏名定义：AMF_WAIT_LOCATION_REPORT_TIMER。索引25对应的内部定时器参数名称：PDU建立流程AMF等待N1N2MessageTransfe时长，宏名定义：AMF_WAIT_N1N2TRANSFER_TIMER。索引26对应的内部定时器参数名称：AMF等待UE的ConfigUpdateComplete时长，宏名定义：AMF_WAIT_UE_CONFIG_UPDATE_CMP_TIMER。索引27对应的内部定时器参数名称：AMF向批量RAN更新间隔时长，宏名定义：AMF_BATCH_RAN_UPDATE_INTERVAL_TIMER。索引28对应的内部定时器参数名称：AMF等待SMF创建SM Context响应时长，宏名定义：AMF_WAIT_SMF_CRT_RESP_TIMER。索引29对应的内部定时器参数名称：AMF等待SMF释放SM Context响应时长，宏名定义：AMF_WAIT_SMF_RLS_RESP_TIMER。索引30对应的内部定时器参数名称：PDU重复建立AMF等待SM context status notification时长，宏名定义：AMF_WAIT_SMCTXT_STATUS_NOTIFY_TIMER。索引31对应的内部定时器参数名称：收到NAS NON DELIVERY INDICATION时AMF等待切换完成时长，宏名定义：WAIT_HO_COMPLETE_TIMER_LENGTH。索引32对应的内部定时器参数名称：AMF等待Handover Notify消息时长，宏名定义：AMF_WAIT_HO_NOTIFY_TIMER。索引33对应的内部定时器参数名称：AMF等待Uplink RAN Status Transfer消息时长，宏名定义：AMF_WAIT_UPLINK_RAN_STATUS_TRANSFER_TIMER。索引34对应的内部定时器参数名称：AMF等待Release UE Context Response消息时长，宏名定义：AMF_WAIT_RELEASE_UE_CONTEXT_RESP_TIMER。索引35对应的内部定时器参数名称：AMF等待N2 Info Notify消息时长，宏名定义：AMF_WAIT_N2_INFO_NOTIFY_TIMER。索引36对应的内部定时器参数名称：AMF等待N2 Info Notify Ack消息时长，宏名定义：AMF_WAIT_N2_INFO_NOTIFY_ACK_TIMER。索引37对应的内部定时器参数名称：AMF等待Relocation Complete Notification消息时长，宏名定义：AMF_WAIT_FORWARD_RELOCATION_COMPLETE_TIMER。索引38对应的内部定时器参数名称：AMF等待Relocation Complete Ack消息时长，宏名定义：AMF_WAIT_FORWARD_RELOCATION_COMPLETE_ACK_TIMER。索引39对应的内部定时器参数名称：局间老局AMF等待 RegistrationStatusUpdate 消息时长，宏名定义：AMF_WAIT_REGISTRATION_STATUS_UPDATE_TIMER。索引40对应的内部定时器参数名称：AMF等待切换之后的注册更新消息时长，宏名定义：AMF_WAIT_REGISTRATION_AFTER_HO_TIMER。索引41对应的内部定时器参数名称：Namf_Communication服务等待Namf_EventExposure服务响应时长，宏名定义：AMF_WAIT_RESPONSE_FROM_EEX_TIMER。索引42对应的内部定时器参数名称：收到N1N2Transfer消息当前TA不在areaOfValidity时延迟发送Update SMContext request时长，宏名定义：AMF_DELAY_SEND_UPDATE_TIMER。索引43对应的内部定时器参数名称：AMF等待处理用量报告的切换流程的时长，宏名定义：AMF_WAIT_HO_PROCESS_USAGEREPORT_TIMER。索引44对应的内部定时器参数名称：AMF等待发送缓存的PDU SESSION RESOURCE SETUP REQUEST消息时长，宏名定义：AMF_WAIT_SEND_BUFFER_PDUSETUP_TIMER。索引45对应的内部定时器参数名称：Namf_Communication等待Namf_Location服务发送的Get LMF ID Response消息时长，宏名定义：AMF_WAIT_LOCATION_GET_LMFID_RESP_TIMER。索引46对应的内部定时器参数名称：AMF等待5G-EIR响应定时器时长，宏名定义：AMF_WAIT_EIR_RESP_TIMER。索引47对应的内部定时器参数名称：Namf_Communication等待Namf_Location服务发送的MOLR Response消息时长，宏名定义：AMF_WAIT_LOCATION_MOLR_RESP_TIMER。索引48对应的内部定时器参数名称：AMF等待UE发送的MOLR响应时长，宏名定义：AMF_WAIT_UE_MOLR_RESP_TIMER。索引49对应的内部定时器参数名称：Namf_Communication服务在切换流程中等待Namf_EventExposure服务响应时长，宏名定义：AMF_WAIT_RESPONSE_IN_HANDOVER_FROM_EEX_TIMER。索引50对应的内部定时器参数名称：4G到5G切换流程发生AMF重定向，初始AMF等待目标AMF的重定向UE上下文响应消息时长，宏名定义：AMF_WAIT_UECONTEXT_RELOCATED_DATA_RESP_TIMER。索引51对应的内部定时器参数名称：AMF等待Take Over通知SMF响应时长，宏名定义：AMF_WAIT_TAKEOVER_NOTIFY_SMF_RESP_TIMER。
VALUE|当前时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器当前取值。
DEFAULTVALUE|默认时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器默认取值。
MINVALUE|最小时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器最小值。
MAXVALUE|最大时长(ms)|参数可选性: 任选参数类型: 数字|参数作用：本参数用于设置定时器最大值。
DESC|定时器名称|参数可选性: 任选参数类型: 字符串参数范围: 0-180|参数作用：本参数用于设置定时器的名称，代表每个定时器的含义。
MACRODEFINE|定时器宏名|参数可选性: 任选参数类型: 字符串参数范围: 0-180|参数作用：本参数用于设置定时器的宏名。




命令举例 


`
查询索引1对应的有名定时器取值。
SHOW DEFPRETIMER

(No.1) : SHOW DEFPRETIMER:ID=1
-----------------Namf_Communication_0----------------
ID           当前时长(ms)          默认时长(ms)          最小时长(ms)           最大时长(ms)        定时器名称                              定时器宏名
1            10000                 10000                 1000                  20000              The length of AMF wait SMF rsp Timer   AMF_WAIT_SMF_RESP_TIMER
记录数：1
执行成功耗时: 0.129 秒

` 


# Communication软件参数配置 
# Communication软件参数配置 


背景知识 


本功能用于配置Namf_Communication这个NFS内部自定义的一些参数，包括非3GPP协议要求的或个别功能的开关。 




功能说明 


本功能用于配置Namf_Communication这个NFS内部自定义的一些参数，包括非3GPP协议要求的或个别功能的开关。 




子主题： 






## 新增Communication软件参数配置(ADD COMMU SOFTWARE PARAMETER) 
## 新增Communication软件参数配置(ADD COMMU SOFTWARE PARAMETER) 


功能说明 

该命令用于新增AMF的communication服务内部的一些功能参数，主要涉及非协议明确要求的、在IOT（Interoperability Test，互操作测试）过程中需要处理的第三方厂家的功能、中兴通讯根据自身产品的特点需要优化的功能。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|软参索引|参数可选性: 必选参数类型: 数字|该配置用于设置communication服务内部的一些功能参数，主要针对非协议明确要求的、异常厂家IOT、自厂家优化的功能或实现。参数1：针对网络侧触发的AN Release流程（参见TS 23502 4.2.6 AN Release章节），如果RAN在UE CONTEXT RELEASE COMPLETE消息中没有携带要去活N3隧道的PDU，则AMF根据此参数控制是否向SMF发送更新消息。参数2：用于控制局间切换或局间registration时，old AMF是否将该用户的订阅信息传递给目标AMF 或 target AMF。默认开启。主要用于异常家对接，对对方AMF不支持此功能时可关闭。参数3：用于控制局间切换或局间registration时，new AMF或targetAMF要不要接纳old AMF传递的订阅信息。参数4：用于控制是否跟踪RAN局向消息。参数5：用于控制PDU建立过程中，AMF是否获取当前PDU对应的S-NSSAI所对应的切片实例NSI。参数7： 用户从5G切换到4G EPS之后，AMF通过本参数控制是否立即删除用户上下文。参数8： 通过动态命令触发向NRF注册时，通过本软参可控制AMF是否先利用FQDN向DNS查询NRF地址。参数9： 当NRF地址采用FQDN方式配置时，该参数用于控制在进行DNS查询时，优先通过本地Cache查询，还是优先通过DNS Server查询。0表示优先本地Cache查询。1表示优先DNS Server查询。参数10：该软参用于控制S-NAPTR RR的优先级是否遵从3GPP。默认是。参数11：该软参用于控制是否支持跟踪Nas Container。默认是。参数12：在NF订阅策略配置为支持续订阅的情况下，AMF根据该参数设置（单位为分钟），来控制在NF订阅有效期到达前，提前多少分钟进行续订阅。参数13：该软参用于控制是否支持无SUPI时缓存上报用户信令。默认否。参数14：该软参用于控制是否支持回收共享表。默认是。参数16：保留软参。参数17：该软参用于控制是否支持无ISDN时缓存上报用户信令 。默认否。参数18：保留软参。参数20：该软参用于控制5G到4G的移动注册过程中是否使用next uplink nas count生成映射KASME。默认否。参数21：该软参用于控制注册请求followon标记置位时是否通知基站建UE上下文。默认是。参数22：该软参用于控制是否携带PLMN-ID参数向UDM获取签约数据。默认是。参数23：该软参用于控制S1 mode to N1 mode NAS transparent container是否包含5G UE Security capability。默认是。参数27：该软参用于控制是否强制使用初始上下文建立下发注册接受。默认否。参数28：该软参用于控制SBI接口中gNBValue的字段格式。默认gNBValue。参数29：本软参用于控制在检测到主备NRF都断链后，AMF是否清空本地发现缓存。设置为1，表示清空。参数30：该软参用于控制是否支持上下文健康检查。默认是。参数31：该软参用于控制是否支持NGAP转发表的健康检查 。默认是。参数32：该软参用于控制Forward relocation request消息中的UE NR security capability IE的长度。默认否。参数33：该软参用于控制是否限制全0的routingId。默认否。参数34：该软参用于控制无N26情况下是否对向UDM订阅ue-context-in-smf上下文。默认是。参数35：该软参用于控制是否支持AS安全修改。默认是。参数36：该软参用于控制Registration(unt)携带Uplink data Status是否进行active up conection操作。默认是。参数37：该软参用于控制是否对UE的安全能力参数进行检默认为90：Payload not  forwarded信息。默认否。参数39：该软参用于控制是否将EPS映射安全上下文中的NAS COUNT设置为5G NAS COUNT。默认是。参数40：该软参用于控制业务请求流程是否分配GUTI。默认否。参数41：该软参用于控制是否在当前5G安全上下文下行NAS COUNT基础上设置下行NAS COUNT。默认是。参数42：该软参用于控制业务请求是否先触发初始上下文建立。默认是。参数43：该软参用于控制 AMF与MME之间消息中的FTEID是否使用N26 AMF GTP-C interface。默认否。参数44：保留软参。参数45：该软参用于控制AMF进行NF订阅时是否携带PLMN-ID参数。默认是。参数46：本软参用于控制业务是否开启偶联状态检测功能。设置为1，表示开启偶联状态检测。参数47：该软参用于控制是否默认UE支持NEA0算法。默认是。参数48：该软参用于控制是否默认UE支持NEA1算法。默认是。参数49：该软参用于控制是否默认UE支持NEA2算法。默认是。参数50：该软参用于控制是否默认UE支持NEA3算法。默认是。参数51：该软参用于控制是否默认UE支持NIA0算法。默认是。参数52：该软参用于控制是否默认UE支持NIA1算法。默认是。参数53：该软参用于控制是否默认UE支持NIA2算法。默认是。参数54：该软参用于控制是否默认UE支持NIA3算法。默认是。参数55：该软参用于控制用户发生鉴权拒绝时是否上报通信失败。默认是。参数56：该软参用于控制用户发生注册拒绝时是否上报通信失败。默认是。参数57：该软参用于控制用户发生业务请求拒绝时是否上报通信失败。默认是。参数58：该软参用于控制用户发起网络侧去注册时是否上报通信失败。默认是。参数59：该软参用于控制初始上下文建立失败时是否上报通信失败。默认是。参数60：该软参用于控制初始注册时是否强制向UDM进行注册。默认是。参数61：该软参用于控制初始注册时是否强制向UDM获取签约数据。默认否。参数62：该软参用于控制发送SmContextUpdateData消息激活用户面是否携带ueLocation字段。默认否。参数63：该软参用于控制RAN发起的N2释放流程N2 Release command携带的原因值。默认携带N2Release请求中的原因值。参数64：该软参用于控制收到initial ue message是否要检查偶联有效性。默认是。参数65：该软参用于控制initial ue message偶联有效性检查失败是否要abort偶联。默认否。参数66：该软参用于控制网络侧没有获取到用户上下文时是否向UE要SUCI。默认是。参数67：该软参用于控制收到UE-CONTEXT标记时是否下发init context setup request消息。默认是。参数68：该软参用于控制偶联状态检测失败时是否删除偶联信息。默认是。参数69：该软参用于控制收到偶联断链时是否删除偶联信息。默认是。参数70：该软参用于控制MME消息中的GW FQDN是否需要去除top前缀保存。默认否。参数72：该软参用于控制SBI接口中的Snssai是否包含sd。默认否。参数73：该软参用于控制NGAP接口中的Snssai是否包含sd。默认否。参数74：该软参用于控制PCF发现时是否携带PLMN信息。默认否。参数75：该软参用于控制局间上下文响应中是否携带UE无线能力参数。默认是。参数76：本软参用于控制SC在重启时是否从Communication服务的Special SC加载局向相关表数据，默认否。参数77：本软参用于控制偶联表记录丢失是否终止该偶联，默认是。参数78：本软参用于控制从SC上是否删除老化的局向相关表记录，默认否。参数79：本软参用于控制收到SIG的偶联退服是否检验FRT表，默认是。参数80：该软参用于控制连接类消息amfngapid异常时给RAN发送释放命令还是是Error Indication。默认发送Error Indication。参数81：保留软参。参数82：该软参用于控制HTTP头中的ContentType multipart/related是否修正为小写字母 。默认否。参数84：该软参用于控制NULL scheme SUCI是否需要转换为BCD码。默认否。参数85：该软参用于控制没有签约UE AMBR时AMF是否携带本局默认UE AMBR 给MME。默认是。参数86：该软参用于控制是否在注册更新流程时的注册拒绝消息中携带T3502。默认否。参数87：该软参用于控制SBI消息中的NAS IE编码格式。默认包含IEI和长度部分。参数88：该软参用于控制切换时没有非直传隧道信息是否在HANDOVER COMMAND中构造PDU Session Resource Handover List。默认否。参数89：该软参用于控制非漫游场景下进行其他网元NRF发现时是否携带target plmn list。默认否。参数90：该软参用于控制鉴权返回二次同步失败时是否给UE发送鉴权拒绝。默认是。参数91：本软参用于控制接收主动负载重平衡启动动态命令时，是否处理动态命令，默认否。参数92：本软参用于控制是否支持5G SA默开时的特定T3502定时器，如果该软参开启，系统在鉴权过程触发5G SA默开、签约数据触发5G SA默开时, 注册拒绝携带特定的T3502定时器给UE， 默认否。参数93：该软参用于控制是否在未做完保的注册拒绝消息中携带T3502，如果关闭，注册拒绝未做完保时，不携带T3502，默认否。参数94：该软参用于控制Xn切换失败是否保持connect态。默认否。参数95：该软参用于控制是否检查NRF返回的NFID是否有效。默认否。参数96：该软参用于控制SCTP没有和gNB关联时是否终止偶联。默认是。参数97：该软参用于控制gNB记录缺失时是否终止偶联。默认是。参数98：该软参用于控制是否订阅SMF选择签约数据改变，默认是。参数99：该软参用于控制是否支持上下文请求携带CIoT Optimizations Support Indication，默认否。参数100：该软参用于控制是否支持互操作创建会话中携带切片信息，默认否。参数101：该软参用于控制是否给PCF携带时区，默认是。参数102：该软参用于控制是否支持组合SUPI号段限制接入和TA限制接入。默认否。参数103：该软参用于控制当paging超时时，是否将用户设置为不可达，默认否。参数105：该软参用于控制注册流程是否支持提前下发初始上下文建立。默认否。参数106：该软参用于控制局内移动I-SMF会话创建请求是否携带smfUri，默认携带。参数107：该软参用于控制局间移动I-SMF会话创建请求是否携带smfUri，默认携带。参数108：该软参用于控制是否把7-5GS服务不允许计数归类为用户原因。默认否。参数109：该软参用于控制是否把15-该TA没有合适小区计数归类为用户原因。默认否。参数110：该软参用于控制是否把111-协议失败，未指定计数归类为用户原因。默认否。参数111：保留软参。参数112：该软参用于控制全量备份场景信令跟踪是否上报接管通知消息，默认不上报。参数113：该软参用于控制是否按NFID清除缓存，默认是。参数114：该软参用于控制当寻呼的失败次数达到此软参时（等于或者大于），那么之后的寻呼，如果仍然失败，则不再统计寻呼的性能统计（包括全局和基于TA）。参数115：该软参用于控制5GS到EPS的切换是否需要通知SMF释放非直传隧道，默认是。参数116：该软参用于控制强制向RAN传递TCE信息。默认是。参数117：该软参用于控制选择NSSF时，是否支持NF级别的重选。默认否。参数118：该软参用于控制选择AUSF/UDM时，是否支持NF级别的重选。默认否。参数119：该软参用于控制选择AMF/SMF/PCF/SMSF/GMLC/LMF时，是否支持NF级别的重选。默认否。参数120：该软参用于控制是否把27-N1模式不允许计数归类为用户原因。默认否。参数121：该软参用于控制对ho required没有携带的pdu是否在流程最后是否给smf发update，默认是。参数122：该软参用于控制是否将业务请求接收消息码流填入到PDUSessionResourceSetupList中。默认否。参数123：该软参用于控制是否支持NF不可达发现查询信令上报，默认不上报。参数124：该软参用于控制，在SMF触发的paging过程中收到SMF发起的N1N2Transfer req，两次N1N2Transfer PDUID不同时，是缓存新的N1N2Transfer req还是依据优先级采取替换或者拒绝的策略，默认依据优先级。参数125：该软参用于控制Forward Relocation Request消息是否携带C-MSISDN 。默认否。参数126：该参数用于控制在X2口上报消息中的ServiceAreaList信元是否使用TAIList的格式来编码，默认不使用。参数128：该软参用于控制是否将注册接受消息码流填入到PDUSessionResourceSetupList中。默认否。参数129：该软参用于控制是否将SDM订阅请求中的callback设置为v2版本。默认否。参数130：该软参用于控制AMBR从bps转化为kbps时的取整方式。默认向下取整。参数131：该软参用于控制新注册的用户与PCF交互失败后是否后续不再与PCF交互。默认否。参数132：该软参用于控制是否支持TaCache表的老化处理。默认否。参数133：该软参用于控制TaCache表的老化时长。默认24小时。参数134：该软参用于控制业务DSL定时器选择开关。默认业务定制定时器。参数135：该软参用于控制是否支持NAS重放保护。默认否。参数136：该软参用于控制老局注册更新流程中是否通知SMF去活用户面。默认否。参数137：该软参用于控制是否支持小型化NSSF功能。默认否。参数138：保留软参。参数139：该软参用于控制GUTI分配方式。默认固定索引方式。参数140：该软参用于控制AMF收到PCF的PRA订阅后是否立即上报。默认立即上报。参数141：该软参用于控制在跨AMF注册流程中收到目标AMF Namf_Communication_RegistrationStatusUpdate Request消息且transferStatus信元值为“NOT_TRANSFERRED“时，源AMF回复Namf_Communication_RegistrationStatusUpdate响应时，响应消息中的regStatusTransferComplete字段取值是否为false。默认为false。参数142：该软参用于判断故障或判断恢复时，UE策略服务是否参与判断。缺省同”UE策略服务不参与判断“。当向PCF获取AM和UE策略的策略配置为UE策略不支持PCF交互时，此软参不起作用。参数143：该软参用于支持互操作的终端选择到非融合PGW-C+SMF时，在相同DNN相同切片情况下，是否支持选择同一个SMF，取值为：0-不支持，1-支持；默认0-不支持。参数144：该软参用于控制在不同PLMN网络下，发现SMF时，携带requester-plmn-list是否从本局支持的PLMN配置中获取。开关默认为否，从用户所在TA中获取。开关打开后，从本局支持的PLMN配置中获取。取值为：0-否，1-是；默认0-否。参数145：该软参用于控制AMF是否上报4/5G combo信令，默认上报。参数146：该软参用于控制是否支持过滤表容量告警上报。默认过滤。参数147：该软参控制注册流程创建UE策略后是否释放N2连接。取值为：0-否，1-是；默认0-否。参数148：该软参控制在短消息激活时是否携带Timezone信息。取值为：0-否，1-是；默认1-是。参数149：该软参控制是否检查SMF请求消息的地址。取值为：0-否，1-是；默认0-否。参数150：该软参控制5到4的Attach过程是否兼容5GS_TO_EPS_MOBILITY 原因值。取值为：0-否，1-是；默认1-是。参数151：该软参控制AMF已经携带smsfid发现smsf时是否还携带supi发现smsf，是否携带supi发现smsf还受网管配置SET NRFDISCSMSFPARACFG控制。取值为：0-否，1-是；默认0-否。参数152：该软参用于控制是否在AMF发给UE的注册拒绝消息中携带reject NSSAI。参数153：该参数用于控制AMF是否下发Redirection for Voice EPS Fallback指示给RAN，用于后续EPS Fallback时，RAN侧判断是否可以回落。取值为：0-否，1-是；默认1-是。参数154：该软参控制状态外收到UDM的原因值为初始注册或注册区域变更的去注册通知是否删除UE上下文。取值为：0-否，1-是；默认1-是。参数155：该参数用于控制AMF是否支持动态偶联详细信息检查。取值为：0-否，1-是；默认0-否。参数156：该参数用于设置动态偶联一致性检查失败时处理策略。取值为：0-更新对端地址信息，1-终止偶联；默认0-更新对端地址信息。参数157：该软参用于业务请求过程中rrc重建场景是否激活原先激活态pdu。取值为：0-否，1-是；默认0-否。参数158：该软参用于从SMF检索上下文失败导致5GS到EPS切换失败的原因值。取值为：0-255；默认7。参数160：该软参用于控制ISSU升级时Communication虚机升级步长，默认为1。参数161：该软参用于控制无用户使用后UE无线能力记录的Cache老化时间，默认10分钟。参数162：该软参用于控制是否在收到UDM触发的去注册后，立即发送SDM 去订阅消息，默认为1。参数163：该软参用于控制在使用NRFClient模式时，当NRF更新流程失败，并且响应码不是主备不可用的响应码，此时是否触发NRF重新注册。配置为“是”，表示触发重新注册，默认为“是”。参数164：该软参用于设置携带了selectedDnn参数时，selMode参数的携带策略。参数165：该软参用于控制UE-AMBR传递优化。默认优化。参数166：该软参用于控制5G切换4G时是否优选本合设局MME，默认为1。参数168：该软参用于控制是否支持性能统计定时上报，默认为支持。参数169：该软参用于控制注册拒绝消息中携带Rejected NSSAI的条件，当软参打开，仅nas原因值为62时携带；当软参关闭，不看原因值，均可以携带，默认为打开。参数170：该软参用于控制非漫游用户的DNN OI中PLMN来源，默认为SUPI。参数171：该软参用于控制是否支持忽略SMC过程，默认不支持。参数172：该软参用于控制SMF容灾IMS会话释放原因值。参数173：该参数用于指定卸载过程中，AMF网络侧去注册用户后，等待用户触发初始注册请求的时间，默认10s。参数174：该参数用于控制多PDU并行激活时延时发现SMF的时长，默认0ms,不延时。参数175：该参数用于收到N1N2Transfer消息出areaOfValidity区域时回N1N2MessageTransferRspData中的原因值,默认ATTEMPTING_TO_REACH_UE。参数176：该参数用于控制收到 PDU SESSION RESOURCE MODIFY RESPONSE消息后是否在SmContextUpdateData中强制携带UserLocation，取值为：0-否，1-是；默认是。参数178：该软参用于控制当5GMM Cause为91时用以替换的值，默认91，不替换。参数179：该软参用于控制v2版本的UplinkSMS中是否支持imeisv，取值为：0-否，1-是；默认是。参数185：该软参用于控制SmContextCreateData结构中hSmfUri, smfUri, additionalHsmfUri, additionalSmfUri信元的URI模式，详细参见29.502 CR0321。早期协议定义有歧义，会导致AMF发送给SMF的URI格式为“{apiRoot}/nsmf-pdusession/v1/”或者“{apiRoot}/nsmf-pdusession/v1/pdu-sessions/”。协议标准通过29.502 CR0321进行澄清，要求为“{apiRoot}/nsmf-pdusession/v1/”，AMF使用软参控制以便兼容对接现网版本。取值为：0-API URI，1-Resource URI；默认API URI。参数187：该软参用于控制AMF本地决策Allowed NSSAI为空时是否直接拒绝UE接入；取值为：0-否，1-是；默认0-否。参数188：该软参用于控制AMF本地决策Allowed NSSAI为空时，如果直接拒绝UE接入，应该携带的限制接入原因值；默认值为62-No network slices available。参数189：该软参用于控制用户注册时AMF是否强制不获取用户签约切片信息；默认否。参数190：该软参用于控制是否禁止用户建立多个紧急PDU；取值为：0-否，1-是；默认0-否。参数192：该软参用于是否统计业务请求流程无失败原因计数器时的请求数，用于控制版本间KPI波动过大，取值为：0-否，1-是；默认是。参数193：该软参用于控制一条5G Backup Data Notification消息最多包含的用户群数。参数194：该软参用于控制UE请求的S-NSSAI不在允许切片中是否拒绝PDU建立，取值为：0-否，1-是；默认是。参数195：该软参用于控制UE安全能力校验失败时的拒绝原因值，取值为：3-非法UE，6-非法ME，7-5G服务不允许，23-UE安全能力不匹配；默认6-非法ME。参数196：该软参用于控制AMF局间传递是否携带smssupport字段，取值为：0-否，1-是；默认否。参数197：该软参用于控制PCF UE策略创建请求消息是否携带有效的SupportedFeatures，取值为：0-否，1-是；默认否。参数198：该软参用于控制移动性流程是否支持基于preferred-locality发现I-SMF/V-SMF。参数199：该软参用于控制N11接口消息中servingNetwork的填写方式，取值为：0-TA中的PLMN；1-本局配置PLMN；默认0。参数201：该软参用于控制业务请求中AMF因底层链路问题向SMF发送失败时是否删除会话信息。默认是。参数202：该软参用于控制业务请求中与SMF交互无响应时是否删除会话信息。默认否。参数203：保留软参。参数204：保留软参。参数205：该软参用于控制Xn切换I-SMF插入发送SmContextCreateData是否携带AsmfId，默认否。参数206：是否限制NGAP BitRate IE值的大小。默认否。参数207：保留软参。参数208：保留软参。参数209：该软参用于控制收到基站NG Setup时检查所支持TA列表的策略。默认使用策略1。参数210：该软参用于控制SBI消息中Userlocation IE的timestamp格式。默认UTC时间。参数211：该参数用于控制移动性或切换流程I-SMF插入改变时是否携带SNSSAI给SMF，默认携带。参数212：该参数用于控制在非漫游场景下进行其他网元NRF发现的时候，是否携带requester plmn list。参数213：该参数用于控制在空闲态4到5注册更新时是否忽略到UDM获取切片及切片选择过程。参数214：该软参用于控制AMF内N2切换是否携带UE Time Zone给SMF。默认否。参数215：该软参用于控制AMF间N2切换是否携带UE Time Zone给SMF。默认否。参数216：该软参用于控制非Special SC在NRF发现后是否支持订阅。默认是。参数218：该软参用于流程冲突处理是否校验用户合法性。默认否。参数219：该软参用于控制限制接入带counter的SUPI号段优先。软参开启时，如果SUPI号段配置在SUPI号段接入限制中，且counter配置不为0，就以该配置数据为准。默认不开启。参数220：该软参用于控制当用户位置有效时是否在SmContextUpdateData中强制携带UserLocation，默认开启。参数222：该软参用于控制对于不在切换列表中的PDU是否去除UeContextCreateData消息中的N2SmInformation。参数223：该软参用于控制注册位置改变时是否通知SMF。参数224：该软参用于控制业务请求位置改变时是否通知SMF。参数225：保留软参。参数226：该软参用于控制是否支持回收异常信令管控表。参数227：保留软参。参数230：保留软参。参数232：该软参用于控制注册下发注册接受后被流程冲突抢占时是否强制同步用户上下文给cache/CDB。默认强制同步。参数234：该软参用于控制释放内部索引资源的阈值。参数235：该软参用于控制内部资源老化回收时长。参数238：保留软参。参数245：该参数用于控制NRFClient在处理UDM/AUSF/PCF的发现响应时，若对于NFProfile中携带号段小于软参设置值，则不进行发现缓存。默认值为2。参数246：该参数用于控制NRFClient在发现缓存老化时间的散列总时长，0默认为散列总时长为100秒，30~600为正常散列总时长，其他值认为不启用该功能。参数247：该参数用于控制重新GUTI分配结束后，是否在注册上下文中保留MTMSI资源已经被其他用户占用的老GUTI。默认不保留直接覆盖。参数248：该参数用于控制UDM/AUSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数251：该参数用于控制在NRF发现后触发NF状态订阅时，是否同时考虑采用IPv4及IPv6地址组成的nfStatusNotificationUri来查询当前是否存在对应的订阅记录，如果存在则不发起订阅。默认同时考虑。参数252：该参数用于控制在收到SMF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数253：该参数用于控制SMF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数254：该参数用于控制在收到PCF/SMSF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数255：该参数用于控制PCF/SMSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数256：该参数用于控制非UDM/AUSF/SMF/PCF/SMSF类型的其他NF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数257：该参数用于控制UDM/AUSF状态由不可用变为可用，并且按NFId触发续缓存时，是否根据缓存信息中识别出的同组UDM/AUSF信息，按NF组进行续缓存。参数258：该参数用于控制NRFClient在处理发现响应时，针对同一个NF号段相同时，是否展开号码树。参数259：该参数用于控制根据指定UDM/AUSF的NFId，进行关联同组其他NFId信息查询的方式，采用优先匹配或全表匹配。参数260：该参数用于控制在业务请求流程过程中是否并发处理initial context setup fail response。默认否。如果不并发处理，则会采用丢弃的处理策略。参数262：该参数用于控制在SMF通过N1N2Transfer请求发起的paging流程过程中，AMF又收到相同PDUID的N1N2Transfer请求，是否给SMF发送N1N2Transfer Fail Notify，取值为：0-否，1-是；默认否。参数269：该参数用于控制上行透传过程中收到N2释放的是否替换当前流程，取值为：0-否，1-是；默认否。参数270：该软参用于控制业务请求流程中ISMF删除或改变时收到SMF成功响应但未携带N2SmInfo是否通知ISMF释放。取值为：0 - 否；1 - 是； 默认是。参数272：该软参用于控制UDP截断转TCP场景下DNS性能统计是否统计查询尝试次数。取值为：0 - 否；1 - 是； 默认否。参数273：该软参用于控制局内切换收到Handover Notify是否更新sctp id。取值为：0 - 否；1 - 是； 默认否。参数274：该软参用于控制流程冲突对于未切换的PDU是否需要忽略通知SMF切换取消。取值为：0 - 否；1 - 是； 默认否。参数275：该软参用于控制是否优化处理局间切换时UeContextCreatedData消息的location字段。取值为：0 - 否；1 - 是； 默认否。参数276：该软参用于控制PDU会话建立流程等待N1N2Transfer消息超时的处理策略取值为：0 - 通知SMF和UE；1 - 仅通知SMF；2 - 仅通知UE；3 - 不通知SMF和UE； 默认通知SMF和UE。参数278：该软参用于控制发送NRF发现请求时选择SBIGW SC的方式。参数279：278号软参为1时，该软参用于控制最大可以使用的SBIGW SC数。参数285：该软参用于控制NFProfile中IP地址对应的端口使用默认端口还是服务对应端口 。取值为：0 - 使用服务对应端口；1 - 使用默认端口； 默认使用服务对应端口。参数287：该软参用于控制连接态收到N1N2Transfer消息不携带areaOfValidity是否丢弃消息中的N2信息，取值为：0-否，1-是；默认否。参数289：该软参用于控制收到N1N2Transfer消息出areaOfValidity区域时是否把N2 SM information投递给RAN，取值为：0-否，1-是；默认否。参数291：该软参用于控制当SMF故障时AMF扫描用户删除会话，用户连接态时是否分别通知UE和基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数292：该软参用于控制N1N2Transfer流程等待SMF更新响应时收到高优先级的消息是否直接替换，取值为：0-否，1-是；默认是。参数293：该软参用于控制收到PATH SWITCH REQUEST消息是否检查安全上下文，取值为：0-否，1-是；默认是。参数348：该软参用于控制AS检查失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数349：该软参用于控制NGAP连接一致性校验失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数352：该软参用于控制当收到SMF的创建响应找不到会话上下文时是否给SMF发送释放请求消息。取值为：0 - 否；1 - 是；默认否。参数355：该软参用于控制融合局AMF所有本局配置的GUAMI均不可用下发AMF Status Indication消息时，是否在Unavailable GUAMI List中携带GUMMEI映射的GUAMI。默认不携带。参数401：该软参用于控制AMF发送的NRF注册或更新请求携带的taiList的最大个数，修改软参值不会触发NRF更新。默认为512。参数402：该软参用于控制AMF发送的NRF注册或更新请求携带的taiRangeList的最大个数，修改软参值不会触发NRF更新。默认为12。参数403：该软参用于控制AMF发送的NRF注册或更新请求中携带的每个PLMN下tacRange最大个数，修改软参值不会触发NRF更新。默认为2048。参数404：该软参用于控制AMF发送的NRF注册或更新请求中携带的所有PLMN下总的tacRange最大个数，修改软参值不会触发NRF更新。默认为20000。参数406：该软参用于控制同步备份表异常挂死回收时长即当该用户的注册上下文不存在时，此上下文最长存在时长,单位分钟。默认为120分钟。参数407：该软参用于控制guti重分配后是否通知基站。参数408：该软参用于控制AMF发送的NRF注册或更新请求中是否携带n2InterfaceAmfInfo参数：0-否，1-是；默认否，修改软参值不会触发NRF更新。参数410：该软参用于控制4到5注册流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数411：该软参用于控制局内注册更新流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数412：该软参用于控制在X1口获取用户信息消息中的AMF上报信息是否强制携带上次使用的EPS PLMN标识。默认不强制携带，即参数可选。参数413：该软参用于控制初始注册结束是否强制保留N2连接。0-否，1-是；默认否。参数414：该软参用于控制4到5移动性注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数415：该软参用于控制5G系统内注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数416：该软参用于控制局内注册更新流程AMF是否向UDM注册。0-否，1-是；默认否。参数418：该软参用于控制发生guti冲突时是否purge老用户。0-否，1-是；默认否。参数419：该软参用于控制AMF收到RAN发送的Initial Ue Message消息时，AMF是否要检查局向TA表。0-否，1-是；默认是。参数420：该软参用于控制当gNB局向的TA记录丢失时，是否终止该gNB局向关联的所有SCTP偶联。0-否，1-是；默认是。参数421：该软参用于控制gNB局向表和gNB局向TA表异常挂死回收时长，单位分钟。默认为60分钟。参数422：该软参用于控制当发生guti冲突时是否放弃新用户流程。0-否，1-是；默认否。参数423：发生guti冲突且需要放弃新用户流程时的失败原因。默认为111。参数424：该软参用于控制是否启用SBI发送保序，中移路由测试的模式开启时该软参需要关闭。0-否，1-是；默认是。参数425：该软参用于控制SBI发送保序间隔。默认5秒。参数426：该软参用于控制AMF发送的NRF注册或更新请求携带的guami的最大个数，修改软参值不会触发NRF更新。默认为16。参数427：该软参用于控制AMF发送的NRF注册或更新请求携带的plmn-id的最大个数，修改软参值不会触发NRF更新。默认为32。参数430：该软参用于控制IP地址细分导致切换失败后是否释放N2连接。0-否，1-是；默认否。参数431：该软参用于控制注册更新或者切入流程，发生SUPI冲突查询到残留用户上下文时，是否需要通知I/V-SMF释放会话。默认需要通知。参数432：该软参用于控制用户信息入库失败时是否清除用户。默认为是。参数433：该软参用于控制用户信息入库失败时是否立即通知UE。默认为是。参数434：该软参用于控制二次鉴权routingId不变时重新发现AUSF。0-否，1-是；默认否。参数435：该软参用于控制同一流程中支持的最大鉴权次数。默认为3。参数436：该软参用于控制局内切换过程中收到上行的SM、SMS、LCS等消息时的处理方式。默认为2，即预处理阶段并行处理，执行阶段缓存处理。参数437：该软参用于控制AMF是否支持EPS回落增强功能。0-否，1-是；默认否。参数438：该软参用于控制AMF保持用户EPS回落状态时长。默认6秒。该参数仅在“AMF支持EPS回落增强”开启后有效。参数441：该软参用于控制是否删除不属于本SC管理的用户上下文。0-否，1-是；默认是。该参数仅在“是否支持上下文健康检查”开启后有效。参数443：该软参用于控制是否优化PDU级上行透传流程被冲突的处理机制.0-否，1-是；默认是。参数444：该软参用于控制紧急PDU建立失败是否使用配置原因值.0-否，1-是；默认是。参数445：紧急PDU建立失败的配置原因值；默认为90。参数446：该软参用于控制4到5注册是否使用从老局AMF获取到的SUPI。0-否，1-是；默认是。参数447：该软参用于控制AMF给UDM的Homogeneous Support of IMS Voice over PS Sessions指示是否考虑用户签约、漫游协议、无线能力信息。0-否，1-是；默认是。参数448：AMF收到gNB发起的部分重启消息，若消息中仅包含RAN UE NGAP ID，则N2连接异常。该软参用于判断AMF是否支持gNB部分重启消息中包含异常的N2连接信息。参数449：在448号参数置为1时，为了防止仅包含RAN UE NGAP ID的部分重启消息过多，对AMF造成冲击，该软参用于控制AMF单位时间内处理此类异常的部分重启消息数目。参数450：在RAN重启过程中，RAN侧先释放根据某个RAN UE NGAP ID建立的N2连接，此时AMF侧仍然保持该连接。之后，RAN根据同样的RAN UE NGAP ID再次请求与AMF建立N2连接，AMF此时会检测到RAN UE NGAP ID冲突。该软参用于判断此时AMF是否启动优化处理。参数451：该软参用于控制移动性流程（如注册、业务请求）被只携带N1容器的N1N2 Msg Transfer消息冲突场景，AS安全没有建立时是否需要拒绝N1N2 Msg Transfer消息。默认不拒绝。参数452：该软参用于控制初始注册流程下发注册接受后被移动性注册流程冲突的场景，AMF是否拒绝移动性注册并携带隐式分离的原因值。默认不拒绝，AMF终止处理初始注册，正常处理移动性注册。参数454：该软参用于控制UDM清除AM签约数据时是否需要去注册用户。默认去注册用户。参数455：该软参用于控制EAP鉴权失败为MAC 失败、同步失败、非5G失败时是否需要发送鉴权拒绝。默认发送鉴权拒绝。参数456：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的流程冲突处理机制。默认开启优化。参数457：该软参用于控制局间注册老局流程资源保护定时器内被注册流程冲突的场景，如果注册请求携带的GUTI是本局分配的，是否释放局间注册老局流程用户的PDU会话资源。默认不释放，流程冲突处理会向SMF更新PDU会话。参数458：该软参用于控制是否在鉴权完成之前启动异常信令管控。0-否，1-是；默认是。参数461：保留软参461。参数462：该软参用于控制5GS到EPS的切换流程中是否限制未请求切换的PDU建立非直传隧道。默认限制。参数463：该软参用于控制HANDOVER COMMAND消息是否限制携带未请求切换的PDU信息。默认限制。参数464：该软参用于控制PDU建立流程中，用户发生移动性流程时的冲突处理是否优化。默认是。参数465：该软参用于控制收到N2释放请求时是否检查amfN2apId，默认检查。参数468：该软参用于控制AMF通知基站释放老的N2连接时原因值，默认NAS “Normal release”。参数469：该软参用于控制5G到4G时AMF释放N2连接的原因值，默认NAS “Normal release”。参数470：该软参用于控制负荷重平衡时AMF主动释放N2连接的原因值，默认NAS “Normal release”。参数472：该软参用于控制是否删除不属于本SC管理的N11保序表记录。默认是。参数473：该软参用于控制A-SMF发现携带preferred-tai时是否忽略nrfSupportedFeatures。默认忽略。参数474：该软参用于控制用户在NAS拥塞控制backofftimer时间内再次发起上行业务时是否仍处理该消息。默认值否，不处理该上行消息。参数475：该软参用于控制是否删除不属于本SC管理的备份表记录。默认是。参数476：该软参用于控制Communication服务定时触发打包同步的时长。默认200ms。参数477：该软参用于控制Communication服务定量触发打包同步的用户个数。默认10个用户。参数478：该参数用于控制AMF是否开启动态偶联管理类消息打包功能。默认不开启。参数479：该软参用于控制用量上报表的老化时间，默认30秒。参数480：该软参用于控制NG Setup请求消息缓存时长，默认150毫秒。参数481：该软参用于控制AMF收到NG Setup请求消息后，是否释放该基站之前接入的用户N2连接，默认释放。该功能用于测试场景，商用场景不建议打开。参数482：该软参用于控制内部索引资源TEIDC老化回收的时长 ，默认2小时。参数483：该软参用于控制收到N2释放请求时检查n2apid失败是否发送Error Indication ，默认发送。参数484：该软参用于控制AMF是否支持连接态用户由于收到SMF的N1N2MessageTransfer触发I-SMF改变处理，默认是。参数486：该软参用于控制老局为初始注册态或attach时是否等待超时定时器，默认否。参数487：该软参用于控制从NRF接收PCF状态通知时，NF故障列表是否进行处理，默认是。参数488：该软参用于控制从NRF接收LMF状态通知时，NF故障列表是否进行处理，默认否。参数489：该软参用于控制局间附着和局间初始注册时，老局AMF等待UDM去注册通知消息的时长，默认10秒。参数491：该软参用于控制是否检查N2消息中的RAN UE NGAP ID，默认是。参数493：该软参用于控制Xn口切换被其它流程冲突掉是否通知源NG-RAN释放N2连接，默认否。参数494：该软参用于控制是否使用Forward Relocation Request消息中的Selected PLMN ID，默认是。参数496：该软参用于控制UE注册请求携带无效的注册类型时，AMF是否当做初始注册进行处理，默认是。参数497：该软参用于控制注册流程被N2释放流程冲突的场景，当N2释放流程被缓存时，注册流程是否继续投递下行消息，默认不投递。参数499：该软参用于控制5G到4G的切换流程被Context Request消息冲突替换时是否需要保留用户上下文，默认是。参数500：该软参用于控制优化N2释放和注册的冲突处理的方式，默认不优化。参数501：该软参用于控制AMF是否支持SUPI格式的正确性检查，SUPI中的MSIN每一位取值应为0-9的BCD码，不允许出现A-F。取值为：0-否，1-是；默认否。参数502：该软参用于控制PATH SWITCH REQUEST携带重复的PDU Session ID时AMF是否直接给RAN发送失败响应；默认否。参数503：该软参用于控制NGAP Class1消息无上下文是否释放连接，默认否。参数504：该软参用于控制NGAP Class2消息无上下文是否释放连接，默认否。参数505：该软参用于控制业务请求流程时是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认是。参数506：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数507：该软参用于控制网络侧去注册流程收到Error Indication是否终止通知UE。取值为：0-否，1-是；默认是。参数508：该软参用于控制是否支持对NGAP的连接进行一致性校验校验，默认是。参数509：该软参用于控制AMF是否收到成功响应后再标记UE-AMBR已发送，默认是。参数511：该软参用于控制连接态两条相同PDU的N1N2Transfer消息冲突时是否先回复失败响应，默认否。参数512：该软参用于控制收到PDU资源修改或释放的N1N2Transfer消息时如果AS安全未建立是否尝试透传N1信息，默认是。参数513：该软参用于控制初始注册当UE指示不支持S1能力时是否清除S1能力信息，默认否。参数514：该软参用于控制注册流程被相同注册请求冲突时，AMF在丢弃重复注册请求的同时是否释放老连接并更新新的连接信息，默认是。参数515：该软参用于控制注册流程收到N2修改UE上下文失败响应导致流程失败的原因值。默认为9。参数516：该软参用于控制初始guti注册时完保失败且老用户处于连接态是否丢弃新的注册请求。默认为否。参数517：该软参用于控制是否维持老版本lastseen ta的设置。默认为否。参数518：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时两个N1N2Transfer请求都没携带ARP时，是否拒绝新来的N1N2Transfer请求。取值为：0-否，1-是；默认是参数519：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时新的N1N2Transfer请求优先级更高时，是否采用替换的策略。取值为：0-否，1-是；默认是参数520：该软参用于控制用量上报表记录的老化扫描个数。取值范围为：1-3000；默认500参数521：该软参用于控制AMF是否对UE携带的IMEi进行格式检查，IMEI必须为14或15位BCD码，不允许出现A-F。取值为：0-否，1-是；默认是。参数522：当NF进入故障列表及告警的时间较长时，业务负担增加。该软参用于判断是否对故障NF启用老化机制。对于启用老化机制的NF,当到达规定时间（即老化时间）时，它将从故障列表中删除并且恢复告警。参数523：当不可达NF发现成功，恢复正常状态后，该软参用于判断此时AMF是否通知SBIGW更新NF状态。参数524：当第522号参数设置为1后，即故障NF启用老化机制，该软参生效。该软参用于控制对故障列表中仅NRF检测的记录，AMF触发不可达周期性发现的时间门限。参数525：该软参用于控制对于紧急PDU是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认否。参数526：该软参用于控制信令管控表扫描速率。取值范围为：1-1000；默认50。参数527：该软参用于控制注册流程在和SMF交互前被N1N2 Message Transfer消息冲突，交互后针对未发生交互会话的N1N2 Message Transfer请求消息，是否继续缓存，默认是。参数529：该软参用于控制紧邻PLMN的TAC放在TAC-low-byte还是放在TAC-high-byte。取值为：0 - 紧邻PLMN的TAC放在TAC-high-byte；1 - 紧邻PLMN的TAC放在TAC-low-byte；默认紧邻PLMN的TAC放在TAC-high-byte。参数530：该软参用于判断是否支持gNB在给AMF发送NG SETUP消息中的UE Retention字段功能，从而保持用户的N2逻辑连接。参数531：该软参用于控制发现AMF非本PLMN时，是否携带target-plmn-list和requester-plmn-list参数给NRF。取值为：0-否，1-是；默认是。参数532：该软参用于控制注册流程中，当注册完成后收到PDU建立请求是否缓存。取值为：0-否，1-是；默认是。参数533：该软参用于控制空闲态5G到4G移动性流程中，AMF是否需要判断N26 license和开关。取值为：0-否，1-是；默认是。参数534：该软参用于控制Handover Notify之后收到目标基站的N2释放是否修正通知源基站N2释放的原因值。取值为：0-否，1-是；默认否。参数535：该软参用于控制不可达主动发现恢复后是否通知SBIGW。取值为：0-否，1-是；默认是。参数536：该软参用于控制AMF收到Initial UE的业务请求时是否拒绝缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数537：该软参用于控制在业务请求过程中，当AMF收到Update/Create SM Response时是否释放缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数540：该软参用于控制LIG触发批量撤控请求时，AMF扫描删除布控记录的速率。默认每100毫秒扫描100条布控记录。参数541：该软参用于控制是否丢弃在会话建立过程中收到的相同PDU Session ID的会话建立请求消息。取值为：0-否，1-是；默认是。参数542：该软参用于控制HR漫游用户发送SmContextCreateData消息时是否携带HsmfId。取值为：0 - 否；1 - 是； 默认否。参数543：该软参用于控制重复的PDU会话激活预处理失败是否需要通知SMF删除会话。取值为：0 - 否；1 - 是； 默认是。参数544：当基于PLMN的AMF支持的SNSSAI和AMF支持的SNSSAI发生连续批量的配置变更时，基站会触发大量配置更新流程，易造成业务载荷过量。本软件参数用于控制延时通知基站触发配置更新流程的时长。参数545：该软参用于控制4G到5G的切换流程中获取不到Allowed NSSAI是否使用PDU会话的SNSSAI替代。取值为：0 - 否；1 - 是； 默认是。参数546：在DNS查询支持TCP方式的情况下，该软件参数用于判断AMF是否对DNS TCP链路信息进行周期性检查，例如检查链路对应的SC状态是否有效、链路个数是否正确等。取值为：0 - 否；1 - 是； 默认是。参数547：该软参用于控制局间切换新局I-SMF选择失败导致对应PDU会话切换失败时，是否通知SMF释放。取值为：0 - 否；1 - 是； 默认否。参数548：使用fake DNN发现SMF时本地发现模板id。取值范围为0-65535； 默认0。参数550：该软参用于控制PLMN改变后是否重新获取切片签约数据。取值为：0 - 否；1 - 是； 默认否。参数551：该软参用于控制是否优化注册过程中等待N2释放响应过程中与去注册冲突。取值为：0 - 否；1 - 是； 默认是。参数553：该软参用于控制收到用户相关的ERROR INDICATION消息指示NGAPID错误时是否触发UE CONTEXT RELEASE COMMAND消息。取值为：0 - 否；1 - 是； 默认否。参数554：该软参用于控制是否支持在UDM订阅请求中携带plmnId。取值为：0 - 否；1 - 是； 默认是。参数555：该软参用于控制当两个带有相同NasPdu字段的Initial UE业务请求冲突时，是否采用replace的策略。取值为：0 - 否；1 - 是； 默认是。参数556：该软参用于控制RAN配置更新消息缓存时长，默认150毫秒。参数558：该软参用于控制当老的PDU已经去活时相同DNN的多PDU会话是否选择同一个A-SMF。取值为：0 - 否；1 - 是； 默认是。参数560：该软参用于控制连接态业务请求过程中SMF故障检测后释放会话时是否通知基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数562：该软参用于控制AMF是否记录PDU会话的用户面状态。取值为：0 - 否；1 - 是； 默认否。参数563：该软参用于控制连接态时MT-LR定位是否向基站发送Location Reporting Control消息。取值为：0 - 否；1 - 是； 默认是。参数564：该软参用于控制业务请求过程中是否缓存N2容器类型是PDU资源修改的N1N2Transfer请求。取值为：0 - 否；1 - 是； 默认是。参数565：该软参用于控制局间未切换会话I/V-SMF改变/删除时AMF是否通知source I/V-SMF释放。取值为：0 - 否；1 - 是； 默认否。参数566：该软参用于控制当上行initial UE消息过负荷丢弃时是否发送N2释放消息。取值为：0 - 否；1 - 是； 默认否。参数568：该软参用于控制是否在注册过程中并行处理NAS未投递指示消息。取值为：0 - 否；1 - 是； 默认是。参数569：该软参用于控制当N2释放流程指示当前UE正在EPS回落时，是否丢弃PDU重建消息。取值为：0 - 否；1 - 是； 默认是。参数570：该软参用于控制无UDSF全量备份接管场景，是否支持通过扫描的方式发送打包的ZTE接管通知消息。该软件参数值设置为0：不支持。该软件参数值设置为1：支持。默认支持。参数571：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式发送打包的ZTE接管通知消息后，等待响应的超时时长。取值范围为1-60，默认1秒。参数572：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式每线程每秒至多可以发送的打包的ZTE接管通知消息数量。取值范围为1-200，默认2包每秒。参数575：该软参用于控制Xn切换流程发送的SmContextUpdateData是否携带变化的epsInterworkingInd。取值为：0 - 否；1 - 是； 默认是。参数577：该软参用于控制业务请求等移动性流程中，当SMF故障且AMF本地无对应TA缓存时，是否进行SMF发现。取值为：0 - 不发现；1 - 发现；默认不发现。参数578：该软参用于控制注册流程和SMF交互后是否继续缓存冲突的无法识别SMF是否改变的N1N2 Message Transfer的PDU修改或释放。取值为：0 - 否；1 - 是； 默认是。参数579：该软参用于控制全量备份场景，本局AMF是否将备份AMF加入本地检测列表，并在接管用户时检查备份AMF状态。默认检查备份局状态。参数580：该软参用于控制全量备份场景，本局AMF通过无线侧消息接管用户，并检查到备份AMF状态正常时，上行消息处理的方式。默认按全量容灾方式处理。参数581：该软参用于控制全量备份场景，本局AMF通过非无线侧消息接管用户，并检查到备份AMF状态正常时，下行消息处理的方式。默认按部分容灾方式处理。参数582：该软参用于控制5GS到EPS的切换流程中是否检查UE的S1 mode能力。取值为：0 - 否；1 - 是； 默认是。参数583：该软参用于控制当AMF收到SMF的N1N2MessageTransfer消息触发I-SMF改变是否回失败响应消息。取值为：0 - 否；1 - 是； 默认是。参数585：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为漫游PDU会话携带hplmnSnssai 。取值为：0 - 否；1 - 是；默认否。参数588：该软参用于控制是否支持强制向UDM获取及订阅ue-context-in-smf上下文。取值为：0 - 否；1 - 是；默认否。参数590：该软参用于控制当4到5切换重定向，目标局和MME都支持双栈时，目标局优选IP类型。取值为：0 - IPv4；1 - IPv6；默认IPv4。参数591：该软参用于控制Xn切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同Xn切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数592：该软参用于控制AMF内N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF内N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数593：该软参用于控制AMF间N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF间N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数594：该软参用于控制EPS到5GS的N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同EPS到5GS的N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数596：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为HR漫游PDU会话携带DTSSA特性 。取值为：0 - 否；1 - 是；默认是。参数597：该软参用于控制切换过程中收到切换完成的更新响应后再收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同之前的处理；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认保持之前的处理。参数598：该软参用于控制是否优化老局流程与上行透传消息的冲突策略。取值为：0 - 否；1 - 是；默认否。参数600：该软参用于控制AMF处理偶联退服消息的最大速率 ，超过的偶联退服消息将被延迟处理。取值为：0-10000（个/秒）；默认0（个/秒），表示不控制。参数601：该软参用于控制AMF进行偶联状态检测的最大速率。取值为：1-2000（个/秒）；默认10（个/秒）。参数602：该软参用于控制AMF进行偶联状态检测的超时时长。取值为：1-10秒；默认3秒。参数603：该软参用于控制接管用户更新SMF失败是否释放会话。取值为：0 - 否；1 - 是；默认是。参数604：该软参用于控制透传PDU SESSION RESOURCE RELEASE RESPONSE给SMF时是否需要等相应消息。取值为：0 - 否；1 - 是；默认是。参数605：该软参用于控制DNS性能统计UDP响应报文过长场景是否统计到UDP响应消息被截断计数器中。取值为：0 - 否；1 - 是；默认否。参数606：该软参用于控制当收到SBI口的失败响应消息而进行Nas原因值映射，若应用错误向配置转换失败，是否尝试继续匹配。取值为：0 - 否；1 - 是；默认否。参数607：该软参用于控制局间注册和TAU流程中old AMF用量上报是否受开关控制。取值为：0 - 否；1 - 是；默认是。参数608：该软参用于控制局间切换发现TargetAMF时携带切片的方式是否需要根据目标TA的PLMN决策。取值为：0 - 否；1 - 是；默认否。参数609：该软参用于控制因ISMF发送SmContextCreateData时是否需要更新SmContextStatusUri中的syn。取值为：0 - 否；1 - 是；默认是。参数610：该软参用于控制切换流程被N2释放流程冲突时是否优化UEContextReleaseCommand消息中原因值。取值为：0 - 否；1 - 是；默认否。参数614：该软参用于控制过负荷时是否要上报信令跟踪。取值为：0 - 否；1 - 是；默认否。参数615：该软参用于控制AMF向SMSF发起激活短消息时，携带GUAMI的方式。取值为：0 - 携带服务GUAMI；1 - 携带AMF的GUAMI列表；默认携带服务GUAMI。参数616：该软参用于控制是否强制获取短消息签约。取值为：0 - 否；1 - 是；默认否。参数617：该软参用于控制是否强制订阅短消息签约。取值为：0 - 否；1 - 是；默认否。参数618：该软参用于控制AMF切换入局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数619：该软参用于控制AMF收到流程外的UDM去注册通知，是否释放周边网元。取值为：0 - 否；1 - 是；默认否。参数620：该软参用于控制NAS未投递流程收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 并行处理；1 - 有MM层消息未投递时缓存处理；2 - 缓存处理；默认有MM层消息未投递时缓存处理。参数621：该软参用于控制SourceAMF收到N2InfoNotify前又收到UEContextReleaseRequest是否需要处理N2释放流程。取值为：0 - 否；1 - 是；默认是。参数622：该软参用于控制切换与其它流程冲突时是否强制将用户上下文同步给cache和CDB。取值为：0 - 否；1 - 是；默认否。参数623：该软参用于AMF进行PCF发现时，是否仅依据UE策略配置开关来决策是否要发现PCF UE策略服务。取值为：0 - 否；1 - 是；默认否。参数624：该软参用于控制5G内切换新局AMF或者互操作切换5G AMF在预处理阶段被流程冲突后是否强制删除PDU上下文。取值为：0 - 否；1 - 是；默认是。参数625：该软参用于控制业务请求过程中，ISMF插入、改变是否向LIG发送消息。取值为：0 - 否；1 - 是；默认否。参数626：该软参用于控制NRF注册或者更新时Service是否支持携带interPlmnFqdn参数。取值为：0 - 否；1 - 是；默认否。参数627：该软参用于控制局间初始UE消息注册请求完整性保护检查通过时，是否通过Namf_Communication_UEContextTransfer请求消息向老局AMF获取用户上下文。取值为：0 - 否；1 - 是；默认否。参数628：该软参用于控制在注册与签约变更流程中，当会话切片不在AllowedNssai中时，是否需要删除不在AllowedNssai中的会话或重建在AllowedNssai中的会话。取值为：0 - 否；1 - 是；默认是。参数629：该软参用于控制amf重定向流程是否支持重选。取值为：0 - 否；1 - 是；默认否。参数630：500号软参取值为1，该软参用于控制N2释放和注册的冲突删除UDM未登记用户的处理方式。参数631：该软参用于控制PCF更新失败是否清除策略上下文并通知PCF。<
VALUE|当前参数值|参数可选性: 必选参数类型: 数字|软件参数当前取值。
DEFAULTVALUE|默认参数值|参数可选性: 必选参数类型: 数字|软件参数默认取值。
MINVALUE|参数最小值|参数可选性: 必选参数类型: 数字|软件参数最小值
MAXVALUE|参数最大值|参数可选性: 必选参数类型: 数字|软件参数最大值
NAME|参数名称|参数可选性: 必选参数类型: 字符串参数范围: 0-180|软参的名称，代表每个软参的含义
REMARK|备注|参数可选性: 任选参数类型: 字符串参数范围: 0-180|参数取值的具体含义介绍




命令举例 


`
新增Communication软件参数配置，软参索引为99，当前参数值为1，默认参数值为1，参数最小值为0，参数最大值为1，参数名称为“保留软参99”。
ADD COMMU SOFTWARE PARAMETER:ID=99,VALUE=1,DEFAULTVALUE=1,MINVALUE=0,MAXVALUE=1,NAME="spareSoftwareParameter99"
` 


## 删除Communication软件参数配置(DEL COMMU SOFTWARE PARAMETER) 
## 删除Communication软件参数配置(DEL COMMU SOFTWARE PARAMETER) 


功能说明 

该命令用于删除AMF的communication服务内部的一些功能参数，主要涉及非协议明确要求的、在IOT（Interoperability Test，互操作测试）过程中需要处理的第三方厂家的功能、中兴通讯根据自身产品的特点需要优化的功能。 


注意事项 

本命令执行后立即生效。 

删除已有软参可能影响业务功能，需要在中兴通讯技术支持工程师的指导下进行操作，请勿擅自删除。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|软参索引|参数可选性: 必选参数类型: 数字|该配置用于设置communication服务内部的一些功能参数，主要针对非协议明确要求的、异常厂家IOT、自厂家优化的功能或实现。参数1：针对网络侧触发的AN Release流程（参见TS 23502 4.2.6 AN Release章节），如果RAN在UE CONTEXT RELEASE COMPLETE消息中没有携带要去活N3隧道的PDU，则AMF根据此参数控制是否向SMF发送更新消息。参数2：用于控制局间切换或局间registration时，old AMF是否将该用户的订阅信息传递给目标AMF 或 target AMF。默认开启。主要用于异常家对接，对对方AMF不支持此功能时可关闭。参数3：用于控制局间切换或局间registration时，new AMF或targetAMF要不要接纳old AMF传递的订阅信息。参数4：用于控制是否跟踪RAN局向消息。参数5：用于控制PDU建立过程中，AMF是否获取当前PDU对应的S-NSSAI所对应的切片实例NSI。参数7： 用户从5G切换到4G EPS之后，AMF通过本参数控制是否立即删除用户上下文。参数8： 通过动态命令触发向NRF注册时，通过本软参可控制AMF是否先利用FQDN向DNS查询NRF地址。参数9： 当NRF地址采用FQDN方式配置时，该参数用于控制在进行DNS查询时，优先通过本地Cache查询，还是优先通过DNS Server查询。0表示优先本地Cache查询。1表示优先DNS Server查询。参数10：该软参用于控制S-NAPTR RR的优先级是否遵从3GPP。默认是。参数11：该软参用于控制是否支持跟踪Nas Container。默认是。参数12：在NF订阅策略配置为支持续订阅的情况下，AMF根据该参数设置（单位为分钟），来控制在NF订阅有效期到达前，提前多少分钟进行续订阅。参数13：该软参用于控制是否支持无SUPI时缓存上报用户信令。默认否。参数14：该软参用于控制是否支持回收共享表。默认是。参数16：保留软参。参数17：该软参用于控制是否支持无ISDN时缓存上报用户信令 。默认否。参数18：保留软参。参数20：该软参用于控制5G到4G的移动注册过程中是否使用next uplink nas count生成映射KASME。默认否。参数21：该软参用于控制注册请求followon标记置位时是否通知基站建UE上下文。默认是。参数22：该软参用于控制是否携带PLMN-ID参数向UDM获取签约数据。默认是。参数23：该软参用于控制S1 mode to N1 mode NAS transparent container是否包含5G UE Security capability。默认是。参数27：该软参用于控制是否强制使用初始上下文建立下发注册接受。默认否。参数28：该软参用于控制SBI接口中gNBValue的字段格式。默认gNBValue。参数29：本软参用于控制在检测到主备NRF都断链后，AMF是否清空本地发现缓存。设置为1，表示清空。参数30：该软参用于控制是否支持上下文健康检查。默认是。参数31：该软参用于控制是否支持NGAP转发表的健康检查 。默认是。参数32：该软参用于控制Forward relocation request消息中的UE NR security capability IE的长度。默认否。参数33：该软参用于控制是否限制全0的routingId。默认否。参数34：该软参用于控制无N26情况下是否对向UDM订阅ue-context-in-smf上下文。默认是。参数35：该软参用于控制是否支持AS安全修改。默认是。参数36：该软参用于控制Registration(unt)携带Uplink data Status是否进行active up conection操作。默认是。参数37：该软参用于控制是否对UE的安全能力参数进行检默认为90：Payload not  forwarded信息。默认否。参数39：该软参用于控制是否将EPS映射安全上下文中的NAS COUNT设置为5G NAS COUNT。默认是。参数40：该软参用于控制业务请求流程是否分配GUTI。默认否。参数41：该软参用于控制是否在当前5G安全上下文下行NAS COUNT基础上设置下行NAS COUNT。默认是。参数42：该软参用于控制业务请求是否先触发初始上下文建立。默认是。参数43：该软参用于控制 AMF与MME之间消息中的FTEID是否使用N26 AMF GTP-C interface。默认否。参数44：保留软参。参数45：该软参用于控制AMF进行NF订阅时是否携带PLMN-ID参数。默认是。参数46：本软参用于控制业务是否开启偶联状态检测功能。设置为1，表示开启偶联状态检测。参数47：该软参用于控制是否默认UE支持NEA0算法。默认是。参数48：该软参用于控制是否默认UE支持NEA1算法。默认是。参数49：该软参用于控制是否默认UE支持NEA2算法。默认是。参数50：该软参用于控制是否默认UE支持NEA3算法。默认是。参数51：该软参用于控制是否默认UE支持NIA0算法。默认是。参数52：该软参用于控制是否默认UE支持NIA1算法。默认是。参数53：该软参用于控制是否默认UE支持NIA2算法。默认是。参数54：该软参用于控制是否默认UE支持NIA3算法。默认是。参数55：该软参用于控制用户发生鉴权拒绝时是否上报通信失败。默认是。参数56：该软参用于控制用户发生注册拒绝时是否上报通信失败。默认是。参数57：该软参用于控制用户发生业务请求拒绝时是否上报通信失败。默认是。参数58：该软参用于控制用户发起网络侧去注册时是否上报通信失败。默认是。参数59：该软参用于控制初始上下文建立失败时是否上报通信失败。默认是。参数60：该软参用于控制初始注册时是否强制向UDM进行注册。默认是。参数61：该软参用于控制初始注册时是否强制向UDM获取签约数据。默认否。参数62：该软参用于控制发送SmContextUpdateData消息激活用户面是否携带ueLocation字段。默认否。参数63：该软参用于控制RAN发起的N2释放流程N2 Release command携带的原因值。默认携带N2Release请求中的原因值。参数64：该软参用于控制收到initial ue message是否要检查偶联有效性。默认是。参数65：该软参用于控制initial ue message偶联有效性检查失败是否要abort偶联。默认否。参数66：该软参用于控制网络侧没有获取到用户上下文时是否向UE要SUCI。默认是。参数67：该软参用于控制收到UE-CONTEXT标记时是否下发init context setup request消息。默认是。参数68：该软参用于控制偶联状态检测失败时是否删除偶联信息。默认是。参数69：该软参用于控制收到偶联断链时是否删除偶联信息。默认是。参数70：该软参用于控制MME消息中的GW FQDN是否需要去除top前缀保存。默认否。参数72：该软参用于控制SBI接口中的Snssai是否包含sd。默认否。参数73：该软参用于控制NGAP接口中的Snssai是否包含sd。默认否。参数74：该软参用于控制PCF发现时是否携带PLMN信息。默认否。参数75：该软参用于控制局间上下文响应中是否携带UE无线能力参数。默认是。参数76：本软参用于控制SC在重启时是否从Communication服务的Special SC加载局向相关表数据，默认否。参数77：本软参用于控制偶联表记录丢失是否终止该偶联，默认是。参数78：本软参用于控制从SC上是否删除老化的局向相关表记录，默认否。参数79：本软参用于控制收到SIG的偶联退服是否检验FRT表，默认是。参数80：该软参用于控制连接类消息amfngapid异常时给RAN发送释放命令还是是Error Indication。默认发送Error Indication。参数81：保留软参。参数82：该软参用于控制HTTP头中的ContentType multipart/related是否修正为小写字母 。默认否。参数84：该软参用于控制NULL scheme SUCI是否需要转换为BCD码。默认否。参数85：该软参用于控制没有签约UE AMBR时AMF是否携带本局默认UE AMBR 给MME。默认是。参数86：该软参用于控制是否在注册更新流程时的注册拒绝消息中携带T3502。默认否。参数87：该软参用于控制SBI消息中的NAS IE编码格式。默认包含IEI和长度部分。参数88：该软参用于控制切换时没有非直传隧道信息是否在HANDOVER COMMAND中构造PDU Session Resource Handover List。默认否。参数89：该软参用于控制非漫游场景下进行其他网元NRF发现时是否携带target plmn list。默认否。参数90：该软参用于控制鉴权返回二次同步失败时是否给UE发送鉴权拒绝。默认是。参数91：本软参用于控制接收主动负载重平衡启动动态命令时，是否处理动态命令，默认否。参数92：本软参用于控制是否支持5G SA默开时的特定T3502定时器，如果该软参开启，系统在鉴权过程触发5G SA默开、签约数据触发5G SA默开时, 注册拒绝携带特定的T3502定时器给UE， 默认否。参数93：该软参用于控制是否在未做完保的注册拒绝消息中携带T3502，如果关闭，注册拒绝未做完保时，不携带T3502，默认否。参数94：该软参用于控制Xn切换失败是否保持connect态。默认否。参数95：该软参用于控制是否检查NRF返回的NFID是否有效。默认否。参数96：该软参用于控制SCTP没有和gNB关联时是否终止偶联。默认是。参数97：该软参用于控制gNB记录缺失时是否终止偶联。默认是。参数98：该软参用于控制是否订阅SMF选择签约数据改变，默认是。参数99：该软参用于控制是否支持上下文请求携带CIoT Optimizations Support Indication，默认否。参数100：该软参用于控制是否支持互操作创建会话中携带切片信息，默认否。参数101：该软参用于控制是否给PCF携带时区，默认是。参数102：该软参用于控制是否支持组合SUPI号段限制接入和TA限制接入。默认否。参数103：该软参用于控制当paging超时时，是否将用户设置为不可达，默认否。参数105：该软参用于控制注册流程是否支持提前下发初始上下文建立。默认否。参数106：该软参用于控制局内移动I-SMF会话创建请求是否携带smfUri，默认携带。参数107：该软参用于控制局间移动I-SMF会话创建请求是否携带smfUri，默认携带。参数108：该软参用于控制是否把7-5GS服务不允许计数归类为用户原因。默认否。参数109：该软参用于控制是否把15-该TA没有合适小区计数归类为用户原因。默认否。参数110：该软参用于控制是否把111-协议失败，未指定计数归类为用户原因。默认否。参数111：保留软参。参数112：该软参用于控制全量备份场景信令跟踪是否上报接管通知消息，默认不上报。参数113：该软参用于控制是否按NFID清除缓存，默认是。参数114：该软参用于控制当寻呼的失败次数达到此软参时（等于或者大于），那么之后的寻呼，如果仍然失败，则不再统计寻呼的性能统计（包括全局和基于TA）。参数115：该软参用于控制5GS到EPS的切换是否需要通知SMF释放非直传隧道，默认是。参数116：该软参用于控制强制向RAN传递TCE信息。默认是。参数117：该软参用于控制选择NSSF时，是否支持NF级别的重选。默认否。参数118：该软参用于控制选择AUSF/UDM时，是否支持NF级别的重选。默认否。参数119：该软参用于控制选择AMF/SMF/PCF/SMSF/GMLC/LMF时，是否支持NF级别的重选。默认否。参数120：该软参用于控制是否把27-N1模式不允许计数归类为用户原因。默认否。参数121：该软参用于控制对ho required没有携带的pdu是否在流程最后是否给smf发update，默认是。参数122：该软参用于控制是否将业务请求接收消息码流填入到PDUSessionResourceSetupList中。默认否。参数123：该软参用于控制是否支持NF不可达发现查询信令上报，默认不上报。参数124：该软参用于控制，在SMF触发的paging过程中收到SMF发起的N1N2Transfer req，两次N1N2Transfer PDUID不同时，是缓存新的N1N2Transfer req还是依据优先级采取替换或者拒绝的策略，默认依据优先级。参数125：该软参用于控制Forward Relocation Request消息是否携带C-MSISDN 。默认否。参数126：该参数用于控制在X2口上报消息中的ServiceAreaList信元是否使用TAIList的格式来编码，默认不使用。参数128：该软参用于控制是否将注册接受消息码流填入到PDUSessionResourceSetupList中。默认否。参数129：该软参用于控制是否将SDM订阅请求中的callback设置为v2版本。默认否。参数130：该软参用于控制AMBR从bps转化为kbps时的取整方式。默认向下取整。参数131：该软参用于控制新注册的用户与PCF交互失败后是否后续不再与PCF交互。默认否。参数132：该软参用于控制是否支持TaCache表的老化处理。默认否。参数133：该软参用于控制TaCache表的老化时长。默认24小时。参数134：该软参用于控制业务DSL定时器选择开关。默认业务定制定时器。参数135：该软参用于控制是否支持NAS重放保护。默认否。参数136：该软参用于控制老局注册更新流程中是否通知SMF去活用户面。默认否。参数137：该软参用于控制是否支持小型化NSSF功能。默认否。参数138：保留软参。参数139：该软参用于控制GUTI分配方式。默认固定索引方式。参数140：该软参用于控制AMF收到PCF的PRA订阅后是否立即上报。默认立即上报。参数141：该软参用于控制在跨AMF注册流程中收到目标AMF Namf_Communication_RegistrationStatusUpdate Request消息且transferStatus信元值为“NOT_TRANSFERRED“时，源AMF回复Namf_Communication_RegistrationStatusUpdate响应时，响应消息中的regStatusTransferComplete字段取值是否为false。默认为false。参数142：该软参用于判断故障或判断恢复时，UE策略服务是否参与判断。缺省同”UE策略服务不参与判断“。当向PCF获取AM和UE策略的策略配置为UE策略不支持PCF交互时，此软参不起作用。参数143：该软参用于支持互操作的终端选择到非融合PGW-C+SMF时，在相同DNN相同切片情况下，是否支持选择同一个SMF，取值为：0-不支持，1-支持；默认0-不支持。参数144：该软参用于控制在不同PLMN网络下，发现SMF时，携带requester-plmn-list是否从本局支持的PLMN配置中获取。开关默认为否，从用户所在TA中获取。开关打开后，从本局支持的PLMN配置中获取。取值为：0-否，1-是；默认0-否。参数145：该软参用于控制AMF是否上报4/5G combo信令，默认上报。参数146：该软参用于控制是否支持过滤表容量告警上报。默认过滤。参数147：该软参控制注册流程创建UE策略后是否释放N2连接。取值为：0-否，1-是；默认0-否。参数148：该软参控制在短消息激活时是否携带Timezone信息。取值为：0-否，1-是；默认1-是。参数149：该软参控制是否检查SMF请求消息的地址。取值为：0-否，1-是；默认0-否。参数150：该软参控制5到4的Attach过程是否兼容5GS_TO_EPS_MOBILITY 原因值。取值为：0-否，1-是；默认1-是。参数151：该软参控制AMF已经携带smsfid发现smsf时是否还携带supi发现smsf，是否携带supi发现smsf还受网管配置SET NRFDISCSMSFPARACFG控制。取值为：0-否，1-是；默认0-否。参数152：该软参用于控制是否在AMF发给UE的注册拒绝消息中携带reject NSSAI。参数153：该参数用于控制AMF是否下发Redirection for Voice EPS Fallback指示给RAN，用于后续EPS Fallback时，RAN侧判断是否可以回落。取值为：0-否，1-是；默认1-是。参数154：该软参控制状态外收到UDM的原因值为初始注册或注册区域变更的去注册通知是否删除UE上下文。取值为：0-否，1-是；默认1-是。参数155：该参数用于控制AMF是否支持动态偶联详细信息检查。取值为：0-否，1-是；默认0-否。参数156：该参数用于设置动态偶联一致性检查失败时处理策略。取值为：0-更新对端地址信息，1-终止偶联；默认0-更新对端地址信息。参数157：该软参用于业务请求过程中rrc重建场景是否激活原先激活态pdu。取值为：0-否，1-是；默认0-否。参数158：该软参用于从SMF检索上下文失败导致5GS到EPS切换失败的原因值。取值为：0-255；默认7。参数160：该软参用于控制ISSU升级时Communication虚机升级步长，默认为1。参数161：该软参用于控制无用户使用后UE无线能力记录的Cache老化时间，默认10分钟。参数162：该软参用于控制是否在收到UDM触发的去注册后，立即发送SDM 去订阅消息，默认为1。参数163：该软参用于控制在使用NRFClient模式时，当NRF更新流程失败，并且响应码不是主备不可用的响应码，此时是否触发NRF重新注册。配置为“是”，表示触发重新注册，默认为“是”。参数164：该软参用于设置携带了selectedDnn参数时，selMode参数的携带策略。参数165：该软参用于控制UE-AMBR传递优化。默认优化。参数166：该软参用于控制5G切换4G时是否优选本合设局MME，默认为1。参数168：该软参用于控制是否支持性能统计定时上报，默认为支持。参数169：该软参用于控制注册拒绝消息中携带Rejected NSSAI的条件，当软参打开，仅nas原因值为62时携带；当软参关闭，不看原因值，均可以携带，默认为打开。参数170：该软参用于控制非漫游用户的DNN OI中PLMN来源，默认为SUPI。参数171：该软参用于控制是否支持忽略SMC过程，默认不支持。参数172：该软参用于控制SMF容灾IMS会话释放原因值。参数173：该参数用于指定卸载过程中，AMF网络侧去注册用户后，等待用户触发初始注册请求的时间，默认10s。参数174：该参数用于控制多PDU并行激活时延时发现SMF的时长，默认0ms,不延时。参数175：该参数用于收到N1N2Transfer消息出areaOfValidity区域时回N1N2MessageTransferRspData中的原因值,默认ATTEMPTING_TO_REACH_UE。参数176：该参数用于控制收到 PDU SESSION RESOURCE MODIFY RESPONSE消息后是否在SmContextUpdateData中强制携带UserLocation，取值为：0-否，1-是；默认是。参数178：该软参用于控制当5GMM Cause为91时用以替换的值，默认91，不替换。参数179：该软参用于控制v2版本的UplinkSMS中是否支持imeisv，取值为：0-否，1-是；默认是。参数185：该软参用于控制SmContextCreateData结构中hSmfUri, smfUri, additionalHsmfUri, additionalSmfUri信元的URI模式，详细参见29.502 CR0321。早期协议定义有歧义，会导致AMF发送给SMF的URI格式为“{apiRoot}/nsmf-pdusession/v1/”或者“{apiRoot}/nsmf-pdusession/v1/pdu-sessions/”。协议标准通过29.502 CR0321进行澄清，要求为“{apiRoot}/nsmf-pdusession/v1/”，AMF使用软参控制以便兼容对接现网版本。取值为：0-API URI，1-Resource URI；默认API URI。参数187：该软参用于控制AMF本地决策Allowed NSSAI为空时是否直接拒绝UE接入；取值为：0-否，1-是；默认0-否。参数188：该软参用于控制AMF本地决策Allowed NSSAI为空时，如果直接拒绝UE接入，应该携带的限制接入原因值；默认值为62-No network slices available。参数189：该软参用于控制用户注册时AMF是否强制不获取用户签约切片信息；默认否。参数190：该软参用于控制是否禁止用户建立多个紧急PDU；取值为：0-否，1-是；默认0-否。参数192：该软参用于是否统计业务请求流程无失败原因计数器时的请求数，用于控制版本间KPI波动过大，取值为：0-否，1-是；默认是。参数193：该软参用于控制一条5G Backup Data Notification消息最多包含的用户群数。参数194：该软参用于控制UE请求的S-NSSAI不在允许切片中是否拒绝PDU建立，取值为：0-否，1-是；默认是。参数195：该软参用于控制UE安全能力校验失败时的拒绝原因值，取值为：3-非法UE，6-非法ME，7-5G服务不允许，23-UE安全能力不匹配；默认6-非法ME。参数196：该软参用于控制AMF局间传递是否携带smssupport字段，取值为：0-否，1-是；默认否。参数197：该软参用于控制PCF UE策略创建请求消息是否携带有效的SupportedFeatures，取值为：0-否，1-是；默认否。参数198：该软参用于控制移动性流程是否支持基于preferred-locality发现I-SMF/V-SMF。参数199：该软参用于控制N11接口消息中servingNetwork的填写方式，取值为：0-TA中的PLMN；1-本局配置PLMN；默认0。参数201：该软参用于控制业务请求中AMF因底层链路问题向SMF发送失败时是否删除会话信息。默认是。参数202：该软参用于控制业务请求中与SMF交互无响应时是否删除会话信息。默认否。参数203：保留软参。参数204：保留软参。参数205：该软参用于控制Xn切换I-SMF插入发送SmContextCreateData是否携带AsmfId，默认否。参数206：是否限制NGAP BitRate IE值的大小。默认否。参数207：保留软参。参数208：保留软参。参数209：该软参用于控制收到基站NG Setup时检查所支持TA列表的策略。默认使用策略1。参数210：该软参用于控制SBI消息中Userlocation IE的timestamp格式。默认UTC时间。参数211：该参数用于控制移动性或切换流程I-SMF插入改变时是否携带SNSSAI给SMF，默认携带。参数212：该参数用于控制在非漫游场景下进行其他网元NRF发现的时候，是否携带requester plmn list。参数213：该参数用于控制在空闲态4到5注册更新时是否忽略到UDM获取切片及切片选择过程。参数214：该软参用于控制AMF内N2切换是否携带UE Time Zone给SMF。默认否。参数215：该软参用于控制AMF间N2切换是否携带UE Time Zone给SMF。默认否。参数216：该软参用于控制非Special SC在NRF发现后是否支持订阅。默认是。参数218：该软参用于流程冲突处理是否校验用户合法性。默认否。参数219：该软参用于控制限制接入带counter的SUPI号段优先。软参开启时，如果SUPI号段配置在SUPI号段接入限制中，且counter配置不为0，就以该配置数据为准。默认不开启。参数220：该软参用于控制当用户位置有效时是否在SmContextUpdateData中强制携带UserLocation，默认开启。参数222：该软参用于控制对于不在切换列表中的PDU是否去除UeContextCreateData消息中的N2SmInformation。参数223：该软参用于控制注册位置改变时是否通知SMF。参数224：该软参用于控制业务请求位置改变时是否通知SMF。参数225：保留软参。参数226：该软参用于控制是否支持回收异常信令管控表。参数227：保留软参。参数230：保留软参。参数232：该软参用于控制注册下发注册接受后被流程冲突抢占时是否强制同步用户上下文给cache/CDB。默认强制同步。参数234：该软参用于控制释放内部索引资源的阈值。参数235：该软参用于控制内部资源老化回收时长。参数238：保留软参。参数245：该参数用于控制NRFClient在处理UDM/AUSF/PCF的发现响应时，若对于NFProfile中携带号段小于软参设置值，则不进行发现缓存。默认值为2。参数246：该参数用于控制NRFClient在发现缓存老化时间的散列总时长，0默认为散列总时长为100秒，30~600为正常散列总时长，其他值认为不启用该功能。参数247：该参数用于控制重新GUTI分配结束后，是否在注册上下文中保留MTMSI资源已经被其他用户占用的老GUTI。默认不保留直接覆盖。参数248：该参数用于控制UDM/AUSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数251：该参数用于控制在NRF发现后触发NF状态订阅时，是否同时考虑采用IPv4及IPv6地址组成的nfStatusNotificationUri来查询当前是否存在对应的订阅记录，如果存在则不发起订阅。默认同时考虑。参数252：该参数用于控制在收到SMF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数253：该参数用于控制SMF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数254：该参数用于控制在收到PCF/SMSF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数255：该参数用于控制PCF/SMSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数256：该参数用于控制非UDM/AUSF/SMF/PCF/SMSF类型的其他NF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数257：该参数用于控制UDM/AUSF状态由不可用变为可用，并且按NFId触发续缓存时，是否根据缓存信息中识别出的同组UDM/AUSF信息，按NF组进行续缓存。参数258：该参数用于控制NRFClient在处理发现响应时，针对同一个NF号段相同时，是否展开号码树。参数259：该参数用于控制根据指定UDM/AUSF的NFId，进行关联同组其他NFId信息查询的方式，采用优先匹配或全表匹配。参数260：该参数用于控制在业务请求流程过程中是否并发处理initial context setup fail response。默认否。如果不并发处理，则会采用丢弃的处理策略。参数262：该参数用于控制在SMF通过N1N2Transfer请求发起的paging流程过程中，AMF又收到相同PDUID的N1N2Transfer请求，是否给SMF发送N1N2Transfer Fail Notify，取值为：0-否，1-是；默认否。参数269：该参数用于控制上行透传过程中收到N2释放的是否替换当前流程，取值为：0-否，1-是；默认否。参数270：该软参用于控制业务请求流程中ISMF删除或改变时收到SMF成功响应但未携带N2SmInfo是否通知ISMF释放。取值为：0 - 否；1 - 是； 默认是。参数272：该软参用于控制UDP截断转TCP场景下DNS性能统计是否统计查询尝试次数。取值为：0 - 否；1 - 是； 默认否。参数273：该软参用于控制局内切换收到Handover Notify是否更新sctp id。取值为：0 - 否；1 - 是； 默认否。参数274：该软参用于控制流程冲突对于未切换的PDU是否需要忽略通知SMF切换取消。取值为：0 - 否；1 - 是； 默认否。参数275：该软参用于控制是否优化处理局间切换时UeContextCreatedData消息的location字段。取值为：0 - 否；1 - 是； 默认否。参数276：该软参用于控制PDU会话建立流程等待N1N2Transfer消息超时的处理策略取值为：0 - 通知SMF和UE；1 - 仅通知SMF；2 - 仅通知UE；3 - 不通知SMF和UE； 默认通知SMF和UE。参数278：该软参用于控制发送NRF发现请求时选择SBIGW SC的方式。参数279：278号软参为1时，该软参用于控制最大可以使用的SBIGW SC数。参数285：该软参用于控制NFProfile中IP地址对应的端口使用默认端口还是服务对应端口 。取值为：0 - 使用服务对应端口；1 - 使用默认端口； 默认使用服务对应端口。参数287：该软参用于控制连接态收到N1N2Transfer消息不携带areaOfValidity是否丢弃消息中的N2信息，取值为：0-否，1-是；默认否。参数289：该软参用于控制收到N1N2Transfer消息出areaOfValidity区域时是否把N2 SM information投递给RAN，取值为：0-否，1-是；默认否。参数291：该软参用于控制当SMF故障时AMF扫描用户删除会话，用户连接态时是否分别通知UE和基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数292：该软参用于控制N1N2Transfer流程等待SMF更新响应时收到高优先级的消息是否直接替换，取值为：0-否，1-是；默认是。参数293：该软参用于控制收到PATH SWITCH REQUEST消息是否检查安全上下文，取值为：0-否，1-是；默认是。参数348：该软参用于控制AS检查失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数349：该软参用于控制NGAP连接一致性校验失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数352：该软参用于控制当收到SMF的创建响应找不到会话上下文时是否给SMF发送释放请求消息。取值为：0 - 否；1 - 是；默认否。参数355：该软参用于控制融合局AMF所有本局配置的GUAMI均不可用下发AMF Status Indication消息时，是否在Unavailable GUAMI List中携带GUMMEI映射的GUAMI。默认不携带。参数401：该软参用于控制AMF发送的NRF注册或更新请求携带的taiList的最大个数，修改软参值不会触发NRF更新。默认为512。参数402：该软参用于控制AMF发送的NRF注册或更新请求携带的taiRangeList的最大个数，修改软参值不会触发NRF更新。默认为12。参数403：该软参用于控制AMF发送的NRF注册或更新请求中携带的每个PLMN下tacRange最大个数，修改软参值不会触发NRF更新。默认为2048。参数404：该软参用于控制AMF发送的NRF注册或更新请求中携带的所有PLMN下总的tacRange最大个数，修改软参值不会触发NRF更新。默认为20000。参数406：该软参用于控制同步备份表异常挂死回收时长即当该用户的注册上下文不存在时，此上下文最长存在时长,单位分钟。默认为120分钟。参数407：该软参用于控制guti重分配后是否通知基站。参数408：该软参用于控制AMF发送的NRF注册或更新请求中是否携带n2InterfaceAmfInfo参数：0-否，1-是；默认否，修改软参值不会触发NRF更新。参数410：该软参用于控制4到5注册流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数411：该软参用于控制局内注册更新流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数412：该软参用于控制在X1口获取用户信息消息中的AMF上报信息是否强制携带上次使用的EPS PLMN标识。默认不强制携带，即参数可选。参数413：该软参用于控制初始注册结束是否强制保留N2连接。0-否，1-是；默认否。参数414：该软参用于控制4到5移动性注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数415：该软参用于控制5G系统内注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数416：该软参用于控制局内注册更新流程AMF是否向UDM注册。0-否，1-是；默认否。参数418：该软参用于控制发生guti冲突时是否purge老用户。0-否，1-是；默认否。参数419：该软参用于控制AMF收到RAN发送的Initial Ue Message消息时，AMF是否要检查局向TA表。0-否，1-是；默认是。参数420：该软参用于控制当gNB局向的TA记录丢失时，是否终止该gNB局向关联的所有SCTP偶联。0-否，1-是；默认是。参数421：该软参用于控制gNB局向表和gNB局向TA表异常挂死回收时长，单位分钟。默认为60分钟。参数422：该软参用于控制当发生guti冲突时是否放弃新用户流程。0-否，1-是；默认否。参数423：发生guti冲突且需要放弃新用户流程时的失败原因。默认为111。参数424：该软参用于控制是否启用SBI发送保序，中移路由测试的模式开启时该软参需要关闭。0-否，1-是；默认是。参数425：该软参用于控制SBI发送保序间隔。默认5秒。参数426：该软参用于控制AMF发送的NRF注册或更新请求携带的guami的最大个数，修改软参值不会触发NRF更新。默认为16。参数427：该软参用于控制AMF发送的NRF注册或更新请求携带的plmn-id的最大个数，修改软参值不会触发NRF更新。默认为32。参数430：该软参用于控制IP地址细分导致切换失败后是否释放N2连接。0-否，1-是；默认否。参数431：该软参用于控制注册更新或者切入流程，发生SUPI冲突查询到残留用户上下文时，是否需要通知I/V-SMF释放会话。默认需要通知。参数432：该软参用于控制用户信息入库失败时是否清除用户。默认为是。参数433：该软参用于控制用户信息入库失败时是否立即通知UE。默认为是。参数434：该软参用于控制二次鉴权routingId不变时重新发现AUSF。0-否，1-是；默认否。参数435：该软参用于控制同一流程中支持的最大鉴权次数。默认为3。参数436：该软参用于控制局内切换过程中收到上行的SM、SMS、LCS等消息时的处理方式。默认为2，即预处理阶段并行处理，执行阶段缓存处理。参数437：该软参用于控制AMF是否支持EPS回落增强功能。0-否，1-是；默认否。参数438：该软参用于控制AMF保持用户EPS回落状态时长。默认6秒。该参数仅在“AMF支持EPS回落增强”开启后有效。参数441：该软参用于控制是否删除不属于本SC管理的用户上下文。0-否，1-是；默认是。该参数仅在“是否支持上下文健康检查”开启后有效。参数443：该软参用于控制是否优化PDU级上行透传流程被冲突的处理机制.0-否，1-是；默认是。参数444：该软参用于控制紧急PDU建立失败是否使用配置原因值.0-否，1-是；默认是。参数445：紧急PDU建立失败的配置原因值；默认为90。参数446：该软参用于控制4到5注册是否使用从老局AMF获取到的SUPI。0-否，1-是；默认是。参数447：该软参用于控制AMF给UDM的Homogeneous Support of IMS Voice over PS Sessions指示是否考虑用户签约、漫游协议、无线能力信息。0-否，1-是；默认是。参数448：AMF收到gNB发起的部分重启消息，若消息中仅包含RAN UE NGAP ID，则N2连接异常。该软参用于判断AMF是否支持gNB部分重启消息中包含异常的N2连接信息。参数449：在448号参数置为1时，为了防止仅包含RAN UE NGAP ID的部分重启消息过多，对AMF造成冲击，该软参用于控制AMF单位时间内处理此类异常的部分重启消息数目。参数450：在RAN重启过程中，RAN侧先释放根据某个RAN UE NGAP ID建立的N2连接，此时AMF侧仍然保持该连接。之后，RAN根据同样的RAN UE NGAP ID再次请求与AMF建立N2连接，AMF此时会检测到RAN UE NGAP ID冲突。该软参用于判断此时AMF是否启动优化处理。参数451：该软参用于控制移动性流程（如注册、业务请求）被只携带N1容器的N1N2 Msg Transfer消息冲突场景，AS安全没有建立时是否需要拒绝N1N2 Msg Transfer消息。默认不拒绝。参数452：该软参用于控制初始注册流程下发注册接受后被移动性注册流程冲突的场景，AMF是否拒绝移动性注册并携带隐式分离的原因值。默认不拒绝，AMF终止处理初始注册，正常处理移动性注册。参数454：该软参用于控制UDM清除AM签约数据时是否需要去注册用户。默认去注册用户。参数455：该软参用于控制EAP鉴权失败为MAC 失败、同步失败、非5G失败时是否需要发送鉴权拒绝。默认发送鉴权拒绝。参数456：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的流程冲突处理机制。默认开启优化。参数457：该软参用于控制局间注册老局流程资源保护定时器内被注册流程冲突的场景，如果注册请求携带的GUTI是本局分配的，是否释放局间注册老局流程用户的PDU会话资源。默认不释放，流程冲突处理会向SMF更新PDU会话。参数458：该软参用于控制是否在鉴权完成之前启动异常信令管控。0-否，1-是；默认是。参数461：保留软参461。参数462：该软参用于控制5GS到EPS的切换流程中是否限制未请求切换的PDU建立非直传隧道。默认限制。参数463：该软参用于控制HANDOVER COMMAND消息是否限制携带未请求切换的PDU信息。默认限制。参数464：该软参用于控制PDU建立流程中，用户发生移动性流程时的冲突处理是否优化。默认是。参数465：该软参用于控制收到N2释放请求时是否检查amfN2apId，默认检查。参数468：该软参用于控制AMF通知基站释放老的N2连接时原因值，默认NAS “Normal release”。参数469：该软参用于控制5G到4G时AMF释放N2连接的原因值，默认NAS “Normal release”。参数470：该软参用于控制负荷重平衡时AMF主动释放N2连接的原因值，默认NAS “Normal release”。参数472：该软参用于控制是否删除不属于本SC管理的N11保序表记录。默认是。参数473：该软参用于控制A-SMF发现携带preferred-tai时是否忽略nrfSupportedFeatures。默认忽略。参数474：该软参用于控制用户在NAS拥塞控制backofftimer时间内再次发起上行业务时是否仍处理该消息。默认值否，不处理该上行消息。参数475：该软参用于控制是否删除不属于本SC管理的备份表记录。默认是。参数476：该软参用于控制Communication服务定时触发打包同步的时长。默认200ms。参数477：该软参用于控制Communication服务定量触发打包同步的用户个数。默认10个用户。参数478：该参数用于控制AMF是否开启动态偶联管理类消息打包功能。默认不开启。参数479：该软参用于控制用量上报表的老化时间，默认30秒。参数480：该软参用于控制NG Setup请求消息缓存时长，默认150毫秒。参数481：该软参用于控制AMF收到NG Setup请求消息后，是否释放该基站之前接入的用户N2连接，默认释放。该功能用于测试场景，商用场景不建议打开。参数482：该软参用于控制内部索引资源TEIDC老化回收的时长 ，默认2小时。参数483：该软参用于控制收到N2释放请求时检查n2apid失败是否发送Error Indication ，默认发送。参数484：该软参用于控制AMF是否支持连接态用户由于收到SMF的N1N2MessageTransfer触发I-SMF改变处理，默认是。参数486：该软参用于控制老局为初始注册态或attach时是否等待超时定时器，默认否。参数487：该软参用于控制从NRF接收PCF状态通知时，NF故障列表是否进行处理，默认是。参数488：该软参用于控制从NRF接收LMF状态通知时，NF故障列表是否进行处理，默认否。参数489：该软参用于控制局间附着和局间初始注册时，老局AMF等待UDM去注册通知消息的时长，默认10秒。参数491：该软参用于控制是否检查N2消息中的RAN UE NGAP ID，默认是。参数493：该软参用于控制Xn口切换被其它流程冲突掉是否通知源NG-RAN释放N2连接，默认否。参数494：该软参用于控制是否使用Forward Relocation Request消息中的Selected PLMN ID，默认是。参数496：该软参用于控制UE注册请求携带无效的注册类型时，AMF是否当做初始注册进行处理，默认是。参数497：该软参用于控制注册流程被N2释放流程冲突的场景，当N2释放流程被缓存时，注册流程是否继续投递下行消息，默认不投递。参数499：该软参用于控制5G到4G的切换流程被Context Request消息冲突替换时是否需要保留用户上下文，默认是。参数500：该软参用于控制优化N2释放和注册的冲突处理的方式，默认不优化。参数501：该软参用于控制AMF是否支持SUPI格式的正确性检查，SUPI中的MSIN每一位取值应为0-9的BCD码，不允许出现A-F。取值为：0-否，1-是；默认否。参数502：该软参用于控制PATH SWITCH REQUEST携带重复的PDU Session ID时AMF是否直接给RAN发送失败响应；默认否。参数503：该软参用于控制NGAP Class1消息无上下文是否释放连接，默认否。参数504：该软参用于控制NGAP Class2消息无上下文是否释放连接，默认否。参数505：该软参用于控制业务请求流程时是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认是。参数506：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数507：该软参用于控制网络侧去注册流程收到Error Indication是否终止通知UE。取值为：0-否，1-是；默认是。参数508：该软参用于控制是否支持对NGAP的连接进行一致性校验校验，默认是。参数509：该软参用于控制AMF是否收到成功响应后再标记UE-AMBR已发送，默认是。参数511：该软参用于控制连接态两条相同PDU的N1N2Transfer消息冲突时是否先回复失败响应，默认否。参数512：该软参用于控制收到PDU资源修改或释放的N1N2Transfer消息时如果AS安全未建立是否尝试透传N1信息，默认是。参数513：该软参用于控制初始注册当UE指示不支持S1能力时是否清除S1能力信息，默认否。参数514：该软参用于控制注册流程被相同注册请求冲突时，AMF在丢弃重复注册请求的同时是否释放老连接并更新新的连接信息，默认是。参数515：该软参用于控制注册流程收到N2修改UE上下文失败响应导致流程失败的原因值。默认为9。参数516：该软参用于控制初始guti注册时完保失败且老用户处于连接态是否丢弃新的注册请求。默认为否。参数517：该软参用于控制是否维持老版本lastseen ta的设置。默认为否。参数518：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时两个N1N2Transfer请求都没携带ARP时，是否拒绝新来的N1N2Transfer请求。取值为：0-否，1-是；默认是参数519：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时新的N1N2Transfer请求优先级更高时，是否采用替换的策略。取值为：0-否，1-是；默认是参数520：该软参用于控制用量上报表记录的老化扫描个数。取值范围为：1-3000；默认500参数521：该软参用于控制AMF是否对UE携带的IMEi进行格式检查，IMEI必须为14或15位BCD码，不允许出现A-F。取值为：0-否，1-是；默认是。参数522：当NF进入故障列表及告警的时间较长时，业务负担增加。该软参用于判断是否对故障NF启用老化机制。对于启用老化机制的NF,当到达规定时间（即老化时间）时，它将从故障列表中删除并且恢复告警。参数523：当不可达NF发现成功，恢复正常状态后，该软参用于判断此时AMF是否通知SBIGW更新NF状态。参数524：当第522号参数设置为1后，即故障NF启用老化机制，该软参生效。该软参用于控制对故障列表中仅NRF检测的记录，AMF触发不可达周期性发现的时间门限。参数525：该软参用于控制对于紧急PDU是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认否。参数526：该软参用于控制信令管控表扫描速率。取值范围为：1-1000；默认50。参数527：该软参用于控制注册流程在和SMF交互前被N1N2 Message Transfer消息冲突，交互后针对未发生交互会话的N1N2 Message Transfer请求消息，是否继续缓存，默认是。参数529：该软参用于控制紧邻PLMN的TAC放在TAC-low-byte还是放在TAC-high-byte。取值为：0 - 紧邻PLMN的TAC放在TAC-high-byte；1 - 紧邻PLMN的TAC放在TAC-low-byte；默认紧邻PLMN的TAC放在TAC-high-byte。参数530：该软参用于判断是否支持gNB在给AMF发送NG SETUP消息中的UE Retention字段功能，从而保持用户的N2逻辑连接。参数531：该软参用于控制发现AMF非本PLMN时，是否携带target-plmn-list和requester-plmn-list参数给NRF。取值为：0-否，1-是；默认是。参数532：该软参用于控制注册流程中，当注册完成后收到PDU建立请求是否缓存。取值为：0-否，1-是；默认是。参数533：该软参用于控制空闲态5G到4G移动性流程中，AMF是否需要判断N26 license和开关。取值为：0-否，1-是；默认是。参数534：该软参用于控制Handover Notify之后收到目标基站的N2释放是否修正通知源基站N2释放的原因值。取值为：0-否，1-是；默认否。参数535：该软参用于控制不可达主动发现恢复后是否通知SBIGW。取值为：0-否，1-是；默认是。参数536：该软参用于控制AMF收到Initial UE的业务请求时是否拒绝缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数537：该软参用于控制在业务请求过程中，当AMF收到Update/Create SM Response时是否释放缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数540：该软参用于控制LIG触发批量撤控请求时，AMF扫描删除布控记录的速率。默认每100毫秒扫描100条布控记录。参数541：该软参用于控制是否丢弃在会话建立过程中收到的相同PDU Session ID的会话建立请求消息。取值为：0-否，1-是；默认是。参数542：该软参用于控制HR漫游用户发送SmContextCreateData消息时是否携带HsmfId。取值为：0 - 否；1 - 是； 默认否。参数543：该软参用于控制重复的PDU会话激活预处理失败是否需要通知SMF删除会话。取值为：0 - 否；1 - 是； 默认是。参数544：当基于PLMN的AMF支持的SNSSAI和AMF支持的SNSSAI发生连续批量的配置变更时，基站会触发大量配置更新流程，易造成业务载荷过量。本软件参数用于控制延时通知基站触发配置更新流程的时长。参数545：该软参用于控制4G到5G的切换流程中获取不到Allowed NSSAI是否使用PDU会话的SNSSAI替代。取值为：0 - 否；1 - 是； 默认是。参数546：在DNS查询支持TCP方式的情况下，该软件参数用于判断AMF是否对DNS TCP链路信息进行周期性检查，例如检查链路对应的SC状态是否有效、链路个数是否正确等。取值为：0 - 否；1 - 是； 默认是。参数547：该软参用于控制局间切换新局I-SMF选择失败导致对应PDU会话切换失败时，是否通知SMF释放。取值为：0 - 否；1 - 是； 默认否。参数548：使用fake DNN发现SMF时本地发现模板id。取值范围为0-65535； 默认0。参数550：该软参用于控制PLMN改变后是否重新获取切片签约数据。取值为：0 - 否；1 - 是； 默认否。参数551：该软参用于控制是否优化注册过程中等待N2释放响应过程中与去注册冲突。取值为：0 - 否；1 - 是； 默认是。参数553：该软参用于控制收到用户相关的ERROR INDICATION消息指示NGAPID错误时是否触发UE CONTEXT RELEASE COMMAND消息。取值为：0 - 否；1 - 是； 默认否。参数554：该软参用于控制是否支持在UDM订阅请求中携带plmnId。取值为：0 - 否；1 - 是； 默认是。参数555：该软参用于控制当两个带有相同NasPdu字段的Initial UE业务请求冲突时，是否采用replace的策略。取值为：0 - 否；1 - 是； 默认是。参数556：该软参用于控制RAN配置更新消息缓存时长，默认150毫秒。参数558：该软参用于控制当老的PDU已经去活时相同DNN的多PDU会话是否选择同一个A-SMF。取值为：0 - 否；1 - 是； 默认是。参数560：该软参用于控制连接态业务请求过程中SMF故障检测后释放会话时是否通知基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数562：该软参用于控制AMF是否记录PDU会话的用户面状态。取值为：0 - 否；1 - 是； 默认否。参数563：该软参用于控制连接态时MT-LR定位是否向基站发送Location Reporting Control消息。取值为：0 - 否；1 - 是； 默认是。参数564：该软参用于控制业务请求过程中是否缓存N2容器类型是PDU资源修改的N1N2Transfer请求。取值为：0 - 否；1 - 是； 默认是。参数565：该软参用于控制局间未切换会话I/V-SMF改变/删除时AMF是否通知source I/V-SMF释放。取值为：0 - 否；1 - 是； 默认否。参数566：该软参用于控制当上行initial UE消息过负荷丢弃时是否发送N2释放消息。取值为：0 - 否；1 - 是； 默认否。参数568：该软参用于控制是否在注册过程中并行处理NAS未投递指示消息。取值为：0 - 否；1 - 是； 默认是。参数569：该软参用于控制当N2释放流程指示当前UE正在EPS回落时，是否丢弃PDU重建消息。取值为：0 - 否；1 - 是； 默认是。参数570：该软参用于控制无UDSF全量备份接管场景，是否支持通过扫描的方式发送打包的ZTE接管通知消息。该软件参数值设置为0：不支持。该软件参数值设置为1：支持。默认支持。参数571：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式发送打包的ZTE接管通知消息后，等待响应的超时时长。取值范围为1-60，默认1秒。参数572：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式每线程每秒至多可以发送的打包的ZTE接管通知消息数量。取值范围为1-200，默认2包每秒。参数575：该软参用于控制Xn切换流程发送的SmContextUpdateData是否携带变化的epsInterworkingInd。取值为：0 - 否；1 - 是； 默认是。参数577：该软参用于控制业务请求等移动性流程中，当SMF故障且AMF本地无对应TA缓存时，是否进行SMF发现。取值为：0 - 不发现；1 - 发现；默认不发现。参数578：该软参用于控制注册流程和SMF交互后是否继续缓存冲突的无法识别SMF是否改变的N1N2 Message Transfer的PDU修改或释放。取值为：0 - 否；1 - 是； 默认是。参数579：该软参用于控制全量备份场景，本局AMF是否将备份AMF加入本地检测列表，并在接管用户时检查备份AMF状态。默认检查备份局状态。参数580：该软参用于控制全量备份场景，本局AMF通过无线侧消息接管用户，并检查到备份AMF状态正常时，上行消息处理的方式。默认按全量容灾方式处理。参数581：该软参用于控制全量备份场景，本局AMF通过非无线侧消息接管用户，并检查到备份AMF状态正常时，下行消息处理的方式。默认按部分容灾方式处理。参数582：该软参用于控制5GS到EPS的切换流程中是否检查UE的S1 mode能力。取值为：0 - 否；1 - 是； 默认是。参数583：该软参用于控制当AMF收到SMF的N1N2MessageTransfer消息触发I-SMF改变是否回失败响应消息。取值为：0 - 否；1 - 是； 默认是。参数585：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为漫游PDU会话携带hplmnSnssai 。取值为：0 - 否；1 - 是；默认否。参数588：该软参用于控制是否支持强制向UDM获取及订阅ue-context-in-smf上下文。取值为：0 - 否；1 - 是；默认否。参数590：该软参用于控制当4到5切换重定向，目标局和MME都支持双栈时，目标局优选IP类型。取值为：0 - IPv4；1 - IPv6；默认IPv4。参数591：该软参用于控制Xn切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同Xn切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数592：该软参用于控制AMF内N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF内N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数593：该软参用于控制AMF间N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF间N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数594：该软参用于控制EPS到5GS的N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同EPS到5GS的N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数596：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为HR漫游PDU会话携带DTSSA特性 。取值为：0 - 否；1 - 是；默认是。参数597：该软参用于控制切换过程中收到切换完成的更新响应后再收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同之前的处理；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认保持之前的处理。参数598：该软参用于控制是否优化老局流程与上行透传消息的冲突策略。取值为：0 - 否；1 - 是；默认否。参数600：该软参用于控制AMF处理偶联退服消息的最大速率 ，超过的偶联退服消息将被延迟处理。取值为：0-10000（个/秒）；默认0（个/秒），表示不控制。参数601：该软参用于控制AMF进行偶联状态检测的最大速率。取值为：1-2000（个/秒）；默认10（个/秒）。参数602：该软参用于控制AMF进行偶联状态检测的超时时长。取值为：1-10秒；默认3秒。参数603：该软参用于控制接管用户更新SMF失败是否释放会话。取值为：0 - 否；1 - 是；默认是。参数604：该软参用于控制透传PDU SESSION RESOURCE RELEASE RESPONSE给SMF时是否需要等相应消息。取值为：0 - 否；1 - 是；默认是。参数605：该软参用于控制DNS性能统计UDP响应报文过长场景是否统计到UDP响应消息被截断计数器中。取值为：0 - 否；1 - 是；默认否。参数606：该软参用于控制当收到SBI口的失败响应消息而进行Nas原因值映射，若应用错误向配置转换失败，是否尝试继续匹配。取值为：0 - 否；1 - 是；默认否。参数607：该软参用于控制局间注册和TAU流程中old AMF用量上报是否受开关控制。取值为：0 - 否；1 - 是；默认是。参数608：该软参用于控制局间切换发现TargetAMF时携带切片的方式是否需要根据目标TA的PLMN决策。取值为：0 - 否；1 - 是；默认否。参数609：该软参用于控制因ISMF发送SmContextCreateData时是否需要更新SmContextStatusUri中的syn。取值为：0 - 否；1 - 是；默认是。参数610：该软参用于控制切换流程被N2释放流程冲突时是否优化UEContextReleaseCommand消息中原因值。取值为：0 - 否；1 - 是；默认否。参数614：该软参用于控制过负荷时是否要上报信令跟踪。取值为：0 - 否；1 - 是；默认否。参数615：该软参用于控制AMF向SMSF发起激活短消息时，携带GUAMI的方式。取值为：0 - 携带服务GUAMI；1 - 携带AMF的GUAMI列表；默认携带服务GUAMI。参数616：该软参用于控制是否强制获取短消息签约。取值为：0 - 否；1 - 是；默认否。参数617：该软参用于控制是否强制订阅短消息签约。取值为：0 - 否；1 - 是；默认否。参数618：该软参用于控制AMF切换入局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数619：该软参用于控制AMF收到流程外的UDM去注册通知，是否释放周边网元。取值为：0 - 否；1 - 是；默认否。参数620：该软参用于控制NAS未投递流程收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 并行处理；1 - 有MM层消息未投递时缓存处理；2 - 缓存处理；默认有MM层消息未投递时缓存处理。参数621：该软参用于控制SourceAMF收到N2InfoNotify前又收到UEContextReleaseRequest是否需要处理N2释放流程。取值为：0 - 否；1 - 是；默认是。参数622：该软参用于控制切换与其它流程冲突时是否强制将用户上下文同步给cache和CDB。取值为：0 - 否；1 - 是；默认否。参数623：该软参用于AMF进行PCF发现时，是否仅依据UE策略配置开关来决策是否要发现PCF UE策略服务。取值为：0 - 否；1 - 是；默认否。参数624：该软参用于控制5G内切换新局AMF或者互操作切换5G AMF在预处理阶段被流程冲突后是否强制删除PDU上下文。取值为：0 - 否；1 - 是；默认是。参数625：该软参用于控制业务请求过程中，ISMF插入、改变是否向LIG发送消息。取值为：0 - 否；1 - 是；默认否。参数626：该软参用于控制NRF注册或者更新时Service是否支持携带interPlmnFqdn参数。取值为：0 - 否；1 - 是；默认否。参数627：该软参用于控制局间初始UE消息注册请求完整性保护检查通过时，是否通过Namf_Communication_UEContextTransfer请求消息向老局AMF获取用户上下文。取值为：0 - 否；1 - 是；默认否。参数628：该软参用于控制在注册与签约变更流程中，当会话切片不在AllowedNssai中时，是否需要删除不在AllowedNssai中的会话或重建在AllowedNssai中的会话。取值为：0 - 否；1 - 是；默认是。参数629：该软参用于控制amf重定向流程是否支持重选。取值为：0 - 否；1 - 是；默认否。参数630：500号软参取值为1，该软参用于控制N2释放和注册的冲突删除UDM未登记用户的处理方式。参数631：该软参用于控制PCF更新失败是否清除策略上下文并通知PCF。<




命令举例 


`
删除软参索引为99的Communication软件参数配置。
DEL COMMU SOFTWARE PARAMETER:ID=99
` 


## 设置Communication软件参数配置(SET COMMU SOFTWARE PARAMETER) 
## 设置Communication软件参数配置(SET COMMU SOFTWARE PARAMETER) 


功能说明 

该命令用于设置AMF的communication服务内部的一些功能参数，主要涉及非协议明确要求的、在IOT（Interoperability Test，互操作测试）过程中需要处理的第三方厂家的功能、中兴通讯根据自身产品的特点需要优化的功能。 


 
参数1：针对网络侧触发的AN Release流程（参见TS 23502 4.2.6 AN Release章节），如果RAN在UE CONTEXT RELEASE COMPLETE消息中没有携带要去活N3隧道的PDU，则AMF根据此参数控制是否向SMF发送更新消息。 

 
参数2：用于控制局间切换或局间registration时，old AMF是否将该用户的订阅信息传递给目标AMF 或 target AMF。默认开启。主要用于异常家对接，对对方AMF不支持此功能时可关闭。 

 
参数3：用于控制局间切换或局间registration时，new AMF或targetAMF要不要接纳old AMF传递的订阅信息。 

 
参数4：用于控制是否跟踪RAN局向消息。 

 
参数5：用于控制PDU建立过程中，AMF是否获取当前PDU对应的S-NSSAI所对应的切片实例NSI。 

 
参数7： 用户从5G切换到4G EPS之后，AMF通过本参数控制是否立即删除用户上下文。 

 
参数8： 通过动态命令触发向NRF注册时，通过本软参可控制AMF是否先利用FQDN向DNS查询NRF地址。 

 
参数9： 当NRF地址采用FQDN方式配置时，该参数用于控制在进行DNS查询时，优先通过本地Cache查询，还是优先通过DNS Server查询。0表示优先本地Cache查询。1表示优先DNS Server查询。 

 
参数10：该软参用于控制S-NAPTR RR的优先级是否遵从3GPP。默认是。 

 
参数11：该软参用于控制是否支持跟踪Nas Container。默认是。 

 
参数12：在NF订阅策略配置为支持续订阅的情况下，AMF根据该参数设置（单位为分钟），来控制在NF订阅有效期到达前，提前多少分钟进行续订阅。 

 
参数13：该软参用于控制是否支持无SUPI时缓存上报用户信令。默认否。 

 
参数14：该软参用于控制是否支持回收共享表。默认是。 

 
参数16：保留软参。 

 
参数17：该软参用于控制是否支持无ISDN时缓存上报用户信令 。默认否。 

 
参数18：保留软参。 

 
参数20：该软参用于控制5G到4G的移动注册过程中是否使用next uplink nas count生成映射KASME。默认否。 

 
参数21：该软参用于控制注册请求followon标记置位时是否通知基站建UE上下文。默认是。 

 
参数22：该软参用于控制是否携带PLMN-ID参数向UDM获取签约数据。默认是。 

 
参数23：该软参用于控制S1 mode to N1 mode NAS transparent container是否包含5G UE Security capability。默认是。 

 
参数27：该软参用于控制是否强制使用初始上下文建立下发注册接受。默认否。 

 
参数28：该软参用于控制SBI接口中gNBValue的字段格式。默认gNBValue。 

 
参数29：本软参用于控制在检测到主备NRF都断链后，AMF是否清空本地发现缓存。设置为1，表示清空。 

 
参数30：该软参用于控制是否支持上下文健康检查。默认是。 

 
参数31：该软参用于控制是否支持NGAP转发表的健康检查 。默认是。 

 
参数32：该软参用于控制Forward relocation request消息中的UE NR security capability IE的长度。默认否。 

 
参数33：该软参用于控制是否限制全0的routingId。默认否。 

 
参数34：该软参用于控制无N26情况下是否对向UDM订阅ue-context-in-smf上下文。默认是。 

 
参数35：该软参用于控制是否支持AS安全修改。默认是。 

 
参数36：该软参用于控制Registration(unt)携带Uplink data Status是否进行active up conection操作。默认是。 

 
参数37：该软参用于控制是否对UE的安全能力参数进行检默认为90：Payload not  forwarded信息。默认否。 

 
参数39：该软参用于控制是否将EPS映射安全上下文中的NAS COUNT设置为5G NAS COUNT。默认是。 

 
参数40：该软参用于控制业务请求流程是否分配GUTI。默认否。 

 
参数41：该软参用于控制是否在当前5G安全上下文下行NAS COUNT基础上设置下行NAS COUNT。默认是。 

 
参数42：该软参用于控制业务请求是否先触发初始上下文建立。默认是。 

 
参数43：该软参用于控制 AMF与MME之间消息中的FTEID是否使用N26 AMF GTP-C interface。默认否。 

 
参数44：保留软参。 

 
参数45：该软参用于控制AMF进行NF订阅时是否携带PLMN-ID参数。默认是。 

 
参数46：本软参用于控制业务是否开启偶联状态检测功能。设置为1，表示开启偶联状态检测。 

 
参数47：该软参用于控制是否默认UE支持NEA0算法。默认是。 

 
参数48：该软参用于控制是否默认UE支持NEA1算法。默认是。 

 
参数49：该软参用于控制是否默认UE支持NEA2算法。默认是。 
参数50：该软参用于控制是否默认UE支持NEA3算法。默认是。 

 
参数51：该软参用于控制是否默认UE支持NIA0算法。默认是。 

 
参数52：该软参用于控制是否默认UE支持NIA1算法。默认是。 

 
参数53：该软参用于控制是否默认UE支持NIA2算法。默认是。 

 
参数54：该软参用于控制是否默认UE支持NIA3算法。默认是。 

 
参数55：该软参用于控制用户发生鉴权拒绝时是否上报通信失败。默认是。 

 
参数56：该软参用于控制用户发生注册拒绝时是否上报通信失败。默认是。 

 
参数57：该软参用于控制用户发生业务请求拒绝时是否上报通信失败。默认是。 

 
参数58：该软参用于控制用户发起网络侧去注册时是否上报通信失败。默认是。 

 
参数59：该软参用于控制初始上下文建立失败时是否上报通信失败。默认是。 

 
参数60：该软参用于控制初始注册时是否强制向UDM进行注册。默认是。 

 
参数61：该软参用于控制初始注册时是否强制向UDM获取签约数据。默认否。 

 
参数62：该软参用于控制发送SmContextUpdateData消息激活用户面是否携带ueLocation字段。默认否。 

 
参数63：该软参用于控制RAN发起的N2释放流程N2 Release command携带的原因值。默认携带N2Release请求中的原因值。 

 
参数64：该软参用于控制收到initial ue message是否要检查偶联有效性。默认是。 

 
参数65：该软参用于控制initial ue message偶联有效性检查失败是否要abort偶联。默认否。 

 
参数66：该软参用于控制网络侧没有获取到用户上下文时是否向UE要SUCI。默认是。 

 
参数67：该软参用于控制收到UE-CONTEXT标记时是否下发init context setup request消息。默认是。 

 
参数68：该软参用于控制偶联状态检测失败时是否删除偶联信息。默认是。 

 
参数69：该软参用于控制收到偶联断链时是否删除偶联信息。默认是。 

 
参数70：该软参用于控制MME消息中的GW FQDN是否需要去除top前缀保存。默认否。 

 
参数72：该软参用于控制SBI接口中的Snssai是否包含sd。默认否。 

 
参数73：该软参用于控制NGAP接口中的Snssai是否包含sd。默认否。 

 
参数74：该软参用于控制PCF发现时是否携带PLMN信息。默认否。 

 
参数75：该软参用于控制局间上下文响应中是否携带UE无线能力参数。默认是。 

 
参数76：本软参用于控制SC在重启时是否从Communication服务的Special SC加载局向相关表数据，默认否。 

 
参数77：本软参用于控制偶联表记录丢失是否终止该偶联，默认是。 

 
参数78：本软参用于控制从SC上是否删除老化的局向相关表记录，默认否。 

 
参数79：本软参用于控制收到SIG的偶联退服是否检验FRT表，默认是。 

 
参数80：该软参用于控制连接类消息amfngapid异常时给RAN发送释放命令还是是Error Indication。默认发送Error Indication。 

 
参数81：保留软参。 

 
参数82：该软参用于控制HTTP头中的ContentType multipart/related是否修正为小写字母 。默认否。 

 
参数84：该软参用于控制NULL scheme SUCI是否需要转换为BCD码。默认否。 

 
参数85：该软参用于控制没有签约UE AMBR时AMF是否携带本局默认UE AMBR 给MME。默认是。 

 
参数86：该软参用于控制是否在注册更新流程时的注册拒绝消息中携带T3502。默认否。 

 
参数87：该软参用于控制SBI消息中的NAS IE编码格式。默认包含IEI和长度部分。 

 
参数88：该软参用于控制切换时没有非直传隧道信息是否在HANDOVER COMMAND中构造PDU Session Resource Handover List。默认否。 

 
参数89：该软参用于控制非漫游场景下进行其他网元NRF发现时是否携带target plmn list。默认否。 

 
参数90：该软参用于控制鉴权返回二次同步失败时是否给UE发送鉴权拒绝。默认是。 

 
参数91：本软参用于控制接收主动负载重平衡启动动态命令时，是否处理动态命令，默认否。 

 
参数92：本软参用于控制是否支持5G SA默开时的特定T3502定时器，如果该软参开启，系统在鉴权过程触发5G SA默开、签约数据触发5G SA默开时, 注册拒绝携带特定的T3502定时器给UE， 默认否。 

 
参数93：该软参用于控制是否在未做完保的注册拒绝消息中携带T3502，如果关闭，注册拒绝未做完保时，不携带T3502，默认否。 

 
参数94：该软参用于控制Xn切换失败是否保持connect态。默认否。 

 
参数95：该软参用于控制是否检查NRF返回的NFID是否有效。默认否。 

 
参数96：该软参用于控制SCTP没有和gNB关联时是否终止偶联。默认是。 

 
参数97：该软参用于控制gNB记录缺失时是否终止偶联。默认是。 

 
参数98：该软参用于控制是否订阅SMF选择签约数据改变，默认是。 

 
参数99：该软参用于控制是否支持上下文请求携带CIoT Optimizations Support Indication，默认否。 

 
参数100：该软参用于控制是否支持互操作创建会话中携带切片信息，默认否。 

 
参数101：该软参用于控制是否给PCF携带时区，默认是。 

 
参数102：该软参用于控制是否支持组合SUPI号段限制接入和TA限制接入。默认否。 

 
参数103：该软参用于控制当paging超时时，是否将用户设置为不可达，默认否。 

 
参数105：该软参用于控制注册流程是否支持提前下发初始上下文建立。默认否。 

 
参数106：该软参用于控制局内移动I-SMF会话创建请求是否携带smfUri，默认携带。 

 
参数107：该软参用于控制局间移动I-SMF会话创建请求是否携带smfUri，默认携带。 

 
参数108：该软参用于控制是否把7-5GS服务不允许计数归类为用户原因。默认否。 

 
参数109：该软参用于控制是否把15-该TA没有合适小区计数归类为用户原因。默认否。 

 
参数110：该软参用于控制是否把111-协议失败，未指定计数归类为用户原因。默认否。 

 
参数111：保留软参。 

 
参数112：该软参用于控制全量备份场景信令跟踪是否上报接管通知消息，默认不上报。 

 
参数113：该软参用于控制是否按NFID清除缓存，默认是。 

 
参数114：该软参用于控制当寻呼的失败次数达到此软参时（等于或者大于），那么之后的寻呼，如果仍然失败，则不再统计寻呼的性能统计（包括全局和基于TA）。 

 
参数115：该软参用于控制5GS到EPS的切换是否需要通知SMF释放非直传隧道，默认是。 

 
参数116：该软参用于控制强制向RAN传递TCE信息。默认是。 

 
参数117：该软参用于控制选择NSSF时，是否支持NF级别的重选。默认否。 

 
参数118：该软参用于控制选择AUSF/UDM时，是否支持NF级别的重选。默认否。 

 
参数119：该软参用于控制选择AMF/SMF/PCF/SMSF/GMLC/LMF时，是否支持NF级别的重选。默认否。 

 
参数120：该软参用于控制是否把27-N1模式不允许计数归类为用户原因。默认否。 

 
参数121：该软参用于控制对ho required没有携带的pdu是否在流程最后是否给smf发update，默认是。 

 
参数122：该软参用于控制是否将业务请求接收消息码流填入到PDUSessionResourceSetupList中。默认否。 

 
参数123：该软参用于控制是否支持NF不可达发现查询信令上报，默认不上报。 

 
参数124：该软参用于控制，在SMF触发的paging过程中收到SMF发起的N1N2Transfer req，两次N1N2Transfer PDUID不同时，是缓存新的N1N2Transfer req还是依据优先级采取替换或者拒绝的策略，默认依据优先级。 

 
参数125：该软参用于控制Forward Relocation Request消息是否携带C-MSISDN 。默认否。 

 
参数126：该参数用于控制在X2口上报消息中的ServiceAreaList信元是否使用TAIList的格式来编码，默认不使用。 

 
参数128：该软参用于控制是否将注册接受消息码流填入到PDUSessionResourceSetupList中。默认否。 

 
参数129：该软参用于控制是否将SDM订阅请求中的callback设置为v2版本。默认否。 

 
参数130：该软参用于控制AMBR从bps转化为kbps时的取整方式。默认向下取整。 

 
参数131：该软参用于控制新注册的用户与PCF交互失败后是否后续不再与PCF交互。默认否。 

 
参数132：该软参用于控制是否支持TaCache表的老化处理。默认否。 

 
参数133：该软参用于控制TaCache表的老化时长。默认24小时。 

 
参数134：该软参用于控制业务DSL定时器选择开关。默认业务定制定时器。 

 
参数135：该软参用于控制是否支持NAS重放保护。默认否。 

 
参数136：该软参用于控制老局注册更新流程中是否通知SMF去活用户面。默认否。 

 
参数137：该软参用于控制是否支持小型化NSSF功能。默认否。 

 
参数138：保留软参。 

 
参数139：该软参用于控制GUTI分配方式。默认固定索引方式。 

 
参数140：该软参用于控制AMF收到PCF的PRA订阅后是否立即上报。默认立即上报。 

 
参数141：该软参用于控制在跨AMF注册流程中收到目标AMF Namf_Communication_RegistrationStatusUpdate Request消息且transferStatus信元值为“NOT_TRANSFERRED“时，源AMF回复Namf_Communication_RegistrationStatusUpdate响应时，响应消息中的regStatusTransferComplete字段取值是否为false。默认为false。 

 
参数142：该软参用于判断故障或判断恢复时，UE策略服务是否参与判断。缺省同”UE策略服务不参与判断“。当向PCF获取AM和UE策略的策略配置为UE策略不支持PCF交互时，此软参不起作用。 

 
参数143：该软参用于支持互操作的终端选择到非融合PGW-C+SMF时，在相同DNN相同切片情况下，是否支持选择同一个SMF，取值为：0-不支持，1-支持；默认0-不支持。 

 
参数144：该软参用于控制在不同PLMN网络下，发现SMF时，携带requester-plmn-list是否从本局支持的PLMN配置中获取。开关默认为否，从用户所在TA中获取。开关打开后，从本局支持的PLMN配置中获取。取值为：0-否，1-是；默认0-否。 

 
参数145：该软参用于控制AMF是否上报4/5G combo信令，默认上报。 

 
参数146：该软参用于控制是否支持过滤表容量告警上报。默认过滤。 

 
参数147：该软参控制注册流程创建UE策略后是否释放N2连接。取值为：0-否，1-是；默认0-否。 

 
参数148：该软参控制在短消息激活时是否携带Timezone信息。取值为：0-否，1-是；默认1-是。 

 
参数149：该软参控制是否检查SMF请求消息的地址。取值为：0-否，1-是；默认0-否。 

 
参数150：该软参控制5到4的Attach过程是否兼容5GS_TO_EPS_MOBILITY 原因值。取值为：0-否，1-是；默认1-是。 

 
参数151：该软参控制AMF已经携带smsfid发现smsf时是否还携带supi发现smsf，是否携带supi发现smsf还受网管配置SET NRFDISCSMSFPARACFG控制。取值为：0-否，1-是；默认0-否。 

 
参数152：该软参用于控制是否在AMF发给UE的注册拒绝消息中携带reject NSSAI。 

 
参数153：该参数用于控制AMF是否下发Redirection for Voice EPS Fallback指示给RAN，用于后续EPS Fallback时，RAN侧判断是否可以回落。取值为：0-否，1-是；默认1-是。 

 
参数154：该软参控制状态外收到UDM的原因值为初始注册或注册区域变更的去注册通知是否删除UE上下文。取值为：0-否，1-是；默认1-是。 

 
参数155：该参数用于控制AMF是否支持动态偶联详细信息检查。取值为：0-否，1-是；默认0-否。 

 
参数156：该参数用于设置动态偶联一致性检查失败时处理策略。取值为：0-更新对端地址信息，1-终止偶联；默认0-更新对端地址信息。 

 
参数157：该软参用于业务请求过程中rrc重建场景是否激活原先激活态pdu。取值为：0-否，1-是；默认0-否。 

 
参数158：该软参用于从SMF检索上下文失败导致5GS到EPS切换失败的原因值。取值为：0-255；默认7。 

 
参数160：该软参用于控制ISSU升级时Communication虚机升级步长，默认为1。 

 
参数161：该软参用于控制无用户使用后UE无线能力记录的Cache老化时间，默认10分钟。 

 
参数162：该软参用于控制是否在收到UDM触发的去注册后，立即发送SDM 去订阅消息，默认为1。 

 
参数163：该软参用于控制在使用NRFClient模式时，当NRF更新流程失败，并且响应码不是主备不可用的响应码，此时是否触发NRF重新注册。配置为“是”，表示触发重新注册，默认为“是”。 

 
参数164：该软参用于设置携带了selectedDnn参数时，selMode参数的携带策略。 

 
参数165：该软参用于控制UE-AMBR传递优化。默认优化。 

 
参数166：该软参用于控制5G切换4G时是否优选本合设局MME，默认为1。 

 
参数168：该软参用于控制是否支持性能统计定时上报，默认为支持。 

 
参数169：该软参用于控制注册拒绝消息中携带Rejected NSSAI的条件，当软参打开，仅nas原因值为62时携带；当软参关闭，不看原因值，均可以携带，默认为打开。 

 
参数170：该软参用于控制非漫游用户的DNN OI中PLMN来源，默认为SUPI。 

 
参数171：该软参用于控制是否支持忽略SMC过程，默认不支持。 

 
参数172：该软参用于控制SMF容灾IMS会话释放原因值。 

 
参数173：该参数用于指定卸载过程中，AMF网络侧去注册用户后，等待用户触发初始注册请求的时间，默认10s。 

 
参数174：该参数用于控制多PDU并行激活时延时发现SMF的时长，默认0ms,不延时。 

 
参数175：该参数用于收到N1N2Transfer消息出areaOfValidity区域时回N1N2MessageTransferRspData中的原因值,默认ATTEMPTING_TO_REACH_UE。 

 
参数176：该参数用于控制收到 PDU SESSION RESOURCE MODIFY RESPONSE消息后是否在SmContextUpdateData中强制携带UserLocation，取值为：0-否，1-是；默认是。 

 
参数178：该软参用于控制当5GMM Cause为91时用以替换的值，默认91，不替换。 

 
参数179：该软参用于控制v2版本的UplinkSMS中是否支持imeisv，取值为：0-否，1-是；默认是。 

 
参数185：该软参用于控制SmContextCreateData结构中hSmfUri, smfUri, additionalHsmfUri, additionalSmfUri信元的URI模式，详细参见29.502 CR0321。早期协议定义有歧义，会导致AMF发送给SMF的URI格式为“{apiRoot}/nsmf-pdusession/v1/”或者“{apiRoot}/nsmf-pdusession/v1/pdu-sessions/”。协议标准通过29.502 CR0321进行澄清，要求为“{apiRoot}/nsmf-pdusession/v1/”，AMF使用软参控制以便兼容对接现网版本。取值为：0-API URI，1-Resource URI；默认API URI。 

 
参数187：该软参用于控制AMF本地决策Allowed NSSAI为空时是否直接拒绝UE接入；取值为：0-否，1-是；默认0-否。 

 
参数188：该软参用于控制AMF本地决策Allowed NSSAI为空时，如果直接拒绝UE接入，应该携带的限制接入原因值；默认值为62-No network slices available。 

 
参数189：该软参用于控制用户注册时AMF是否强制不获取用户签约切片信息；默认否。 

 
参数190：该软参用于控制是否禁止用户建立多个紧急PDU；取值为：0-否，1-是；默认0-否。 

 
参数192：该软参用于是否统计业务请求流程无失败原因计数器时的请求数，用于控制版本间KPI波动过大，取值为：0-否，1-是；默认是。 

 
参数193：该软参用于控制一条5G Backup Data Notification消息最多包含的用户群数。 

 
参数194：该软参用于控制UE请求的S-NSSAI不在允许切片中是否拒绝PDU建立，取值为：0-否，1-是；默认是。 

 
参数195：该软参用于控制UE安全能力校验失败时的拒绝原因值，取值为：3-非法UE，6-非法ME，7-5G服务不允许，23-UE安全能力不匹配；默认6-非法ME。 

 
参数196：该软参用于控制AMF局间传递是否携带smssupport字段，取值为：0-否，1-是；默认否。 

 
参数197：该软参用于控制PCF UE策略创建请求消息是否携带有效的SupportedFeatures，取值为：0-否，1-是；默认否。 

 
参数198：该软参用于控制移动性流程是否支持基于preferred-locality发现I-SMF/V-SMF。 

 
参数199：该软参用于控制N11接口消息中servingNetwork的填写方式，取值为：0-TA中的PLMN；1-本局配置PLMN；默认0。 

 
参数201：该软参用于控制业务请求中AMF因底层链路问题向SMF发送失败时是否删除会话信息。默认是。 

 
参数202：该软参用于控制业务请求中与SMF交互无响应时是否删除会话信息。默认否。 

 
参数203：保留软参。 

 
参数204：保留软参。 

 
参数205：该软参用于控制Xn切换I-SMF插入发送SmContextCreateData是否携带AsmfId，默认否。 

 
参数206：是否限制NGAP BitRate IE值的大小。默认否。 

 
参数207：保留软参。 

 
参数208：保留软参。 

 
参数209：该软参用于控制收到基站NG Setup时检查所支持TA列表的策略。默认使用策略1。 

 
参数210：该软参用于控制SBI消息中Userlocation IE的timestamp格式。默认UTC时间。 

 
参数211：该参数用于控制移动性或切换流程I-SMF插入改变时是否携带SNSSAI给SMF，默认携带。 

 
参数212：该参数用于控制在非漫游场景下进行其他网元NRF发现的时候，是否携带requester plmn list。 

 
参数213：该参数用于控制在空闲态4到5注册更新时是否忽略到UDM获取切片及切片选择过程。 

 
参数214：该软参用于控制AMF内N2切换是否携带UE Time Zone给SMF。默认否。 

 
参数215：该软参用于控制AMF间N2切换是否携带UE Time Zone给SMF。默认否。 

 
参数216：该软参用于控制非Special SC在NRF发现后是否支持订阅。默认是。 

 
参数218：该软参用于流程冲突处理是否校验用户合法性。默认否。 

 
参数219：该软参用于控制限制接入带counter的SUPI号段优先。软参开启时，如果SUPI号段配置在SUPI号段接入限制中，且counter配置不为0，就以该配置数据为准。默认不开启。 

 
参数220：该软参用于控制当用户位置有效时是否在SmContextUpdateData中强制携带UserLocation，默认开启。 

 
参数222：该软参用于控制对于不在切换列表中的PDU是否去除UeContextCreateData消息中的N2SmInformation。 

 
参数223：该软参用于控制注册位置改变时是否通知SMF。 

 
参数224：该软参用于控制业务请求位置改变时是否通知SMF。 

 
参数225：保留软参。 

 
参数226：该软参用于控制是否支持回收异常信令管控表。 

 
参数227：保留软参。 

 
参数230：保留软参。 

 
参数232：该软参用于控制注册下发注册接受后被流程冲突抢占时是否强制同步用户上下文给cache/CDB。默认强制同步。 

 
参数234：该软参用于控制释放内部索引资源的阈值。 

 
参数235：该软参用于控制内部资源老化回收时长。 

 
参数238：保留软参。 

 
参数245：该参数用于控制NRFClient在处理UDM/AUSF/PCF的发现响应时，若对于NFProfile中携带号段小于软参设置值，则不进行发现缓存。默认值为2。 

 
参数246：该参数用于控制NRFClient在发现缓存老化时间的散列总时长，0默认为散列总时长为100秒，30~600为正常散列总时长，其他值认为不启用该功能。 

 
参数247：该参数用于控制重新GUTI分配结束后，是否在注册上下文中保留MTMSI资源已经被其他用户占用的老GUTI。默认不保留直接覆盖。 

 
参数248：该参数用于控制UDM/AUSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。 

 
参数251：该参数用于控制在NRF发现后触发NF状态订阅时，是否同时考虑采用IPv4及IPv6地址组成的nfStatusNotificationUri来查询当前是否存在对应的订阅记录，如果存在则不发起订阅。默认同时考虑。 

 
参数252：该参数用于控制在收到SMF状态不可用的状态通知时，是否清除对应NF的发现缓存。 

 
参数253：该参数用于控制SMF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。 

 
参数254：该参数用于控制在收到PCF/SMSF状态不可用的状态通知时，是否清除对应NF的发现缓存。 

 
参数255：该参数用于控制PCF/SMSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。 

 
参数256：该参数用于控制非UDM/AUSF/SMF/PCF/SMSF类型的其他NF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。 

 
参数257：该参数用于控制UDM/AUSF状态由不可用变为可用，并且按NFId触发续缓存时，是否根据缓存信息中识别出的同组UDM/AUSF信息，按NF组进行续缓存。 

 
参数258：该参数用于控制NRFClient在处理发现响应时，针对同一个NF号段相同时，是否展开号码树。 

 
参数259：该参数用于控制根据指定UDM/AUSF的NFId，进行关联同组其他NFId信息查询的方式，采用优先匹配或全表匹配。 

 
参数260：该参数用于控制在业务请求流程过程中是否并发处理initial context setup fail response。默认否。如果不并发处理，则会采用丢弃的处理策略。 

 
参数262：该参数用于控制在SMF通过N1N2Transfer请求发起的paging流程过程中，AMF又收到相同PDUID的N1N2Transfer请求，是否给SMF发送N1N2Transfer Fail Notify，取值为：0-否，1-是；默认否。 

 
参数269：该参数用于控制上行透传过程中收到N2释放的是否替换当前流程，取值为：0-否，1-是；默认否。 

 
参数270：该软参用于控制业务请求流程中ISMF删除或改变时收到SMF成功响应但未携带N2SmInfo是否通知ISMF释放。取值为：0 - 否；1 - 是； 默认是。 

 
参数272：该软参用于控制UDP截断转TCP场景下DNS性能统计是否统计查询尝试次数。取值为：0 - 否；1 - 是； 默认否。 

 
参数273：该软参用于控制局内切换收到Handover Notify是否更新sctp id。取值为：0 - 否；1 - 是； 默认否。 

 
参数274：该软参用于控制流程冲突对于未切换的PDU是否需要忽略通知SMF切换取消。取值为：0 - 否；1 - 是； 默认否。 

 
参数275：该软参用于控制是否优化处理局间切换时UeContextCreatedData消息的location字段。取值为：0 - 否；1 - 是； 默认否。 

 
参数276：该软参用于控制PDU会话建立流程等待N1N2Transfer消息超时的处理策略取值为：0 - 通知SMF和UE；1 - 仅通知SMF；2 - 仅通知UE；3 - 不通知SMF和UE； 默认通知SMF和UE。 

 
参数278：该软参用于控制发送NRF发现请求时选择SBIGW SC的方式。 

 
参数279：278号软参为1时，该软参用于控制最大可以使用的SBIGW SC数。 

 
参数285：该软参用于控制NFProfile中IP地址对应的端口使用默认端口还是服务对应端口 。取值为：0 - 使用服务对应端口；1 - 使用默认端口； 默认使用服务对应端口。 

 
参数287：该软参用于控制连接态收到N1N2Transfer消息不携带areaOfValidity是否丢弃消息中的N2信息，取值为：0-否，1-是；默认否。 

 
参数289：该软参用于控制收到N1N2Transfer消息出areaOfValidity区域时是否把N2 SM information投递给RAN，取值为：0-否，1-是；默认否。 

 
参数291：该软参用于控制当SMF故障时AMF扫描用户删除会话，用户连接态时是否分别通知UE和基站PDU释放。取值为：0 - 否；1 - 是； 默认是。 

 
参数292：该软参用于控制N1N2Transfer流程等待SMF更新响应时收到高优先级的消息是否直接替换，取值为：0-否，1-是；默认是。 

 
参数293：该软参用于控制收到PATH SWITCH REQUEST消息是否检查安全上下文，取值为：0-否，1-是；默认是。 

 
参数338：该软参用于控制AMF指定卸载用户时，重定向是否强制nrf发现对端AMF。取值为：0 - 否，1 - 是；默认是。 

 
参数348：该软参用于控制AS检查失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。 

 
参数349：该软参用于控制NGAP连接一致性校验失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。 

 
参数352：该软参用于控制当收到SMF的创建响应找不到会话上下文时是否给SMF发送释放请求消息。取值为：0 - 否；1 - 是；默认否。 

 
参数355：该软参用于控制融合局AMF所有本局配置的GUAMI均不可用下发AMF Status Indication消息时，是否在Unavailable GUAMI List中携带GUMMEI映射的GUAMI。默认不携带。 

 
参数401：该软参用于控制AMF发送的NRF注册或更新请求携带的taiList的最大个数，修改软参值不会触发NRF更新。默认为512。 

 
参数402：该软参用于控制AMF发送的NRF注册或更新请求携带的taiRangeList的最大个数，修改软参值不会触发NRF更新。默认为12。 

 
参数403：该软参用于控制AMF发送的NRF注册或更新请求中携带的每个PLMN下tacRange最大个数，修改软参值不会触发NRF更新。默认为2048。 

 
参数404：该软参用于控制AMF发送的NRF注册或更新请求中携带的所有PLMN下总的tacRange最大个数，修改软参值不会触发NRF更新。默认为20000。 

 
参数406：该软参用于控制同步备份表异常挂死回收时长即当该用户的注册上下文不存在时，此上下文最长存在时长,单位分钟。默认为120分钟。 

 
参数407：该软参用于控制guti重分配后是否通知基站。 

 
参数408：该软参用于控制AMF发送的NRF注册或更新请求中是否携带n2InterfaceAmfInfo参数：0-否，1-是；默认否，修改软参值不会触发NRF更新。 

 
参数410：该软参用于控制4到5注册流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。 

 
参数411：该软参用于控制局内注册更新流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。 

 
参数412：该软参用于控制在X1口获取用户信息消息中的AMF上报信息是否强制携带上次使用的EPS PLMN标识。默认不强制携带，即参数可选。 

 
参数413：该软参用于控制初始注册结束是否强制保留N2连接。0-否，1-是；默认否。 

 
参数414：该软参用于控制4到5移动性注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。 

 
参数415：该软参用于控制5G系统内注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。 

 
参数416：该软参用于控制局内注册更新流程AMF是否向UDM注册。0-否，1-是；默认否。 

 
参数418：该软参用于控制发生guti冲突时是否purge老用户。0-否，1-是；默认否。 

 
参数419：该软参用于控制AMF收到RAN发送的Initial Ue Message消息时，AMF是否要检查局向TA表。0-否，1-是；默认是。 

 
参数420：该软参用于控制当gNB局向的TA记录丢失时，是否终止该gNB局向关联的所有SCTP偶联。0-否，1-是；默认是。 

 
参数421：该软参用于控制gNB局向表和gNB局向TA表异常挂死回收时长，单位分钟。默认为60分钟。 

 
参数422：该软参用于控制当发生guti冲突时是否放弃新用户流程。0-否，1-是；默认否。 

 
参数423：发生guti冲突且需要放弃新用户流程时的失败原因。默认为111。 

 
参数424：该软参用于控制是否启用SBI发送保序，中移路由测试的模式开启时该软参需要关闭。0-否，1-是；默认是。 

 
参数425：该软参用于控制SBI发送保序间隔。默认5秒。 

 
参数426：该软参用于控制AMF发送的NRF注册或更新请求携带的guami的最大个数，修改软参值不会触发NRF更新。默认为16。 

 
参数427：该软参用于控制AMF发送的NRF注册或更新请求携带的plmn-id的最大个数，修改软参值不会触发NRF更新。默认为32。 

 
参数430：该软参用于控制IP地址细分导致切换失败后是否释放N2连接。0-否，1-是；默认否。 

 
参数431：该软参用于控制注册更新或者切入流程，发生SUPI冲突查询到残留用户上下文时，是否需要通知I/V-SMF释放会话。默认需要通知。 

 
参数432：该软参用于控制用户信息入库失败时是否清除用户。默认为是。 

 
参数433：该软参用于控制用户信息入库失败时是否立即通知UE。默认为是。 

 
参数434：该软参用于控制二次鉴权routingId不变时重新发现AUSF。0-否，1-是；默认否。 

 
参数435：该软参用于控制同一流程中支持的最大鉴权次数。默认为3。 

 
参数436：该软参用于控制局内切换过程中收到上行的SM、SMS、LCS等消息时的处理方式。默认为2，即预处理阶段并行处理，执行阶段缓存处理。 

 
参数437：该软参用于控制AMF是否支持EPS回落增强功能。0-否，1-是；默认否。 

 
参数438：该软参用于控制AMF保持用户EPS回落状态时长。默认6秒。该参数仅在“AMF支持EPS回落增强”开启后有效。 

 
参数441：该软参用于控制是否删除不属于本SC管理的用户上下文。0-否，1-是；默认是。该参数仅在“是否支持上下文健康检查”开启后有效。 

 
参数443：该软参用于控制是否优化PDU级上行透传流程被冲突的处理机制.0-否，1-是；默认是。 

 
参数444：该软参用于控制紧急PDU建立失败是否使用配置原因值.0-否，1-是；默认是。 

 
参数445：紧急PDU建立失败的配置原因值；默认为90。 

 
参数446：该软参用于控制4到5注册是否使用从老局AMF获取到的SUPI。0-否，1-是；默认是。 

 
参数447：该软参用于控制AMF给UDM的Homogeneous Support of IMS Voice over PS Sessions指示是否考虑用户签约、漫游协议、无线能力信息。0-否，1-是；默认是。 

 
参数448：AMF收到gNB发起的部分重启消息，若消息中仅包含RAN UE NGAP ID，则N2连接异常。该软参用于判断AMF是否支持gNB部分重启消息中包含异常的N2连接信息。 

 
参数449：在448号参数置为1时，为了防止仅包含RAN UE NGAP ID的部分重启消息过多，对AMF造成冲击，该软参用于控制AMF单位时间内处理此类异常的部分重启消息数目。 

 
参数450：在RAN重启过程中，RAN侧先释放根据某个RAN UE NGAP ID建立的N2连接，此时AMF侧仍然保持该连接。之后，RAN根据同样的RAN UE NGAP ID再次请求与AMF建立N2连接，AMF此时会检测到RAN UE NGAP ID冲突。该软参用于判断此时AMF是否启动优化处理。 

 
参数451：该软参用于控制移动性流程（如注册、业务请求）被只携带N1容器的N1N2 Msg Transfer消息冲突场景，AS安全没有建立时是否需要拒绝N1N2 Msg Transfer消息。默认不拒绝。 

 
参数452：该软参用于控制初始注册流程下发注册接受后被移动性注册流程冲突的场景，AMF是否拒绝移动性注册并携带隐式分离的原因值。默认不拒绝，AMF终止处理初始注册，正常处理移动性注册。 

 
参数454：该软参用于控制UDM清除AM签约数据时是否需要去注册用户。默认去注册用户。 

 
参数455：该软参用于控制EAP鉴权失败为MAC 失败、同步失败、非5G失败时是否需要发送鉴权拒绝。默认发送鉴权拒绝。 

 
参数456：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的流程冲突处理机制。默认开启优化。 

 
参数457：该软参用于控制局间注册老局流程资源保护定时器内被注册流程冲突的场景，如果注册请求携带的GUTI是本局分配的，是否释放局间注册老局流程用户的PDU会话资源。默认不释放，流程冲突处理会向SMF更新PDU会话。 

 
参数458：该软参用于控制是否在鉴权完成之前启动异常信令管控。0-否，1-是；默认是。 

 
参数461：保留软参461。 

 
参数462：该软参用于控制5GS到EPS的切换流程中是否限制未请求切换的PDU建立非直传隧道。默认限制。 

 
参数463：该软参用于控制HANDOVER COMMAND消息是否限制携带未请求切换的PDU信息。默认限制。 

 
参数464：该软参用于控制PDU建立流程中，用户发生移动性流程时的冲突处理是否优化。默认是。 

 
参数465：该软参用于控制收到N2释放请求时是否检查amfN2apId，默认检查。 

 
参数468：该软参用于控制AMF通知基站释放老的N2连接时原因值，默认NAS “Normal release”。 

 
参数469：该软参用于控制5G到4G时AMF释放N2连接的原因值，默认NAS “Normal release”。 

 
参数470：该软参用于控制负荷重平衡时AMF主动释放N2连接的原因值，默认NAS “Normal release”。 

 
参数472：该软参用于控制是否删除不属于本SC管理的N11保序表记录。默认是。 

 
参数473：该软参用于控制A-SMF发现携带preferred-tai时是否忽略nrfSupportedFeatures。默认忽略。 

 
参数474：该软参用于控制用户在NAS拥塞控制backofftimer时间内再次发起上行业务时是否仍处理该消息。默认值否，不处理该上行消息。 

 
参数475：该软参用于控制是否删除不属于本SC管理的备份表记录。默认是。 

 
参数476：该软参用于控制Communication服务定时触发打包同步的时长。默认200ms。 

 
参数477：该软参用于控制Communication服务定量触发打包同步的用户个数。默认10个用户。 

 
参数478：该参数用于控制AMF是否开启动态偶联管理类消息打包功能。默认不开启。 

 
参数479：该软参用于控制用量上报表的老化时间，默认30秒。 

 
参数480：该软参用于控制NG Setup请求消息缓存时长，默认150毫秒。 

 
参数481：该软参用于控制AMF收到NG Setup请求消息后，是否释放该基站之前接入的用户N2连接，默认释放。该功能用于测试场景，商用场景不建议打开。 

 
参数482：该软参用于控制内部索引资源TEIDC老化回收的时长 ，默认2小时。 

 
参数483：该软参用于控制收到N2释放请求时检查n2apid失败是否发送Error Indication ，默认发送。 

 
参数484：该软参用于控制AMF是否支持连接态用户由于收到SMF的N1N2MessageTransfer触发I-SMF改变处理，默认是。 

 
参数486：该软参用于控制老局为初始注册态或attach时是否等待超时定时器，默认否。 

 
参数487：该软参用于控制从NRF接收PCF状态通知时，NF故障列表是否进行处理，默认是。 

 
参数488：该软参用于控制从NRF接收LMF状态通知时，NF故障列表是否进行处理，默认否。 

 
参数489：该软参用于控制局间附着和局间初始注册时，老局AMF等待UDM去注册通知消息的时长，默认10秒。 

 
参数491：该软参用于控制是否检查N2消息中的RAN UE NGAP ID，默认是。 

 
参数493：该软参用于控制Xn口切换被其它流程冲突掉是否通知源NG-RAN释放N2连接，默认否。 

 
参数494：该软参用于控制是否使用Forward Relocation Request消息中的Selected PLMN ID，默认是。 

 
参数496：该软参用于控制UE注册请求携带无效的注册类型时，AMF是否当做初始注册进行处理，默认是。 

 
参数497：该软参用于控制注册流程被N2释放流程冲突的场景，当N2释放流程被缓存时，注册流程是否继续投递下行消息，默认不投递。 

 
参数499：该软参用于控制5G到4G的切换流程被Context Request消息冲突替换时是否需要保留用户上下文，默认是。 

 
参数500：该软参用于控制优化N2释放和注册的冲突处理的方式，默认不优化。 

 
参数501：该软参用于控制AMF是否支持SUPI格式的正确性检查，SUPI中的MSIN每一位取值应为0-9的BCD码，不允许出现A-F。取值为：0-否，1-是；默认否。 

 
参数502：该软参用于控制PATH SWITCH REQUEST携带重复的PDU Session ID时AMF是否直接给RAN发送失败响应；默认否。 

 
参数503：该软参用于控制NGAP Class1消息无上下文是否释放连接，默认否。 

 
参数504：该软参用于控制NGAP Class2消息无上下文是否释放连接，默认否。 

 
参数505：该软参用于控制业务请求流程时是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认是。 

 
参数506：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。 

 
参数507：该软参用于控制网络侧去注册流程收到Error Indication是否终止通知UE。取值为：0-否，1-是；默认是。 

 
参数508：该软参用于控制是否支持对NGAP的连接进行一致性校验校验，默认是。 

 
参数509：该软参用于控制AMF是否收到成功响应后再标记UE-AMBR已发送，默认是。 

 
参数511：该软参用于控制连接态两条相同PDU的N1N2Transfer消息冲突时是否先回复失败响应，默认否。 

 
参数512：该软参用于控制收到PDU资源修改或释放的N1N2Transfer消息时如果AS安全未建立是否尝试透传N1信息，默认是。 

 
参数513：该软参用于控制初始注册当UE指示不支持S1能力时是否清除S1能力信息，默认否。 

 
参数514：该软参用于控制注册流程被相同注册请求冲突时，AMF在丢弃重复注册请求的同时是否释放老连接并更新新的连接信息，默认是。 

 
参数515：该软参用于控制注册流程收到N2修改UE上下文失败响应导致流程失败的原因值。默认为9。 

 
参数516：该软参用于控制初始guti注册时完保失败且老用户处于连接态是否丢弃新的注册请求。默认为否。 

 
参数517：该软参用于控制是否维持老版本lastseen ta的设置。默认为否。 

 
参数518：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时两个N1N2Transfer请求都没携带ARP时，是否拒绝新来的N1N2Transfer请求。取值为：0-否，1-是；默认是 

 
参数519：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时新的N1N2Transfer请求优先级更高时，是否采用替换的策略。取值为：0-否，1-是；默认是 

 
参数520：该软参用于控制用量上报表记录的老化扫描个数。取值范围为：1-3000；默认500 

 
参数521：该软参用于控制AMF是否对UE携带的IMEi进行格式检查，IMEI必须为14或15位BCD码，不允许出现A-F。取值为：0-否，1-是；默认是。 

 
参数522：当NF进入故障列表及告警的时间较长时，业务负担增加。该软参用于判断是否对故障NF启用老化机制。对于启用老化机制的NF,当到达规定时间（即老化时间）时，它将从故障列表中删除并且恢复告警。 

 
参数523：当不可达NF发现成功，恢复正常状态后，该软参用于判断此时AMF是否通知SBIGW更新NF状态。 

 
参数524：当第522号参数设置为1后，即故障NF启用老化机制，该软参生效。该软参用于控制对故障列表中仅NRF检测的记录，AMF触发不可达周期性发现的时间门限。 

 
参数525：该软参用于控制对于紧急PDU是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认否。 

 
参数526：该软参用于控制信令管控表扫描速率。取值范围为：1-1000；默认50。 

 
参数527：该软参用于控制注册流程在和SMF交互前被N1N2 Message Transfer消息冲突，交互后针对未发生交互会话的N1N2 Message Transfer请求消息，是否继续缓存，默认是。 

 
参数529：该软参用于控制紧邻PLMN的TAC放在TAC-low-byte还是放在TAC-high-byte。取值为：0 - 紧邻PLMN的TAC放在TAC-high-byte；1 - 紧邻PLMN的TAC放在TAC-low-byte；默认紧邻PLMN的TAC放在TAC-high-byte。 

 
参数530：该软参用于判断是否支持gNB在给AMF发送NG SETUP消息中的UE Retention字段功能，从而保持用户的N2逻辑连接。 

 
参数531：该软参用于控制发现AMF非本PLMN时，是否携带target-plmn-list和requester-plmn-list参数给NRF。取值为：0-否，1-是；默认是。 

 
参数532：该软参用于控制注册流程中，当注册完成后收到PDU建立请求是否缓存。取值为：0-否，1-是；默认是。 

 
参数533：该软参用于控制空闲态5G到4G移动性流程中，AMF是否需要判断N26 license和开关。取值为：0-否，1-是；默认是。 

 
参数534：该软参用于控制Handover Notify之后收到目标基站的N2释放是否修正通知源基站N2释放的原因值。取值为：0-否，1-是；默认否。 

 
参数535：该软参用于控制不可达主动发现恢复后是否通知SBIGW。取值为：0-否，1-是；默认是。 

 
参数536：该软参用于控制AMF收到Initial UE的业务请求时是否拒绝缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。 

 
参数537：该软参用于控制在业务请求过程中，当AMF收到Update/Create SM Response时是否释放缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。 

 
参数540：该软参用于控制LIG触发批量撤控请求时，AMF扫描删除布控记录的速率。默认每100毫秒扫描100条布控记录。 

 
参数541：该软参用于控制是否丢弃在会话建立过程中收到的相同PDU Session ID的会话建立请求消息。取值为：0-否，1-是；默认是。 

 
参数542：该软参用于控制HR漫游用户发送SmContextCreateData消息时是否携带HsmfId。取值为：0 - 否；1 - 是； 默认否。 

 
参数543：该软参用于控制重复的PDU会话激活预处理失败是否需要通知SMF删除会话。取值为：0 - 否；1 - 是； 默认是。 

 
参数544：当基于PLMN的AMF支持的SNSSAI和AMF支持的SNSSAI发生连续批量的配置变更时，基站会触发大量配置更新流程，易造成业务载荷过量。本软件参数用于控制延时通知基站触发配置更新流程的时长。 

 
参数545：该软参用于控制4G到5G的切换流程中获取不到Allowed NSSAI是否使用PDU会话的SNSSAI替代。取值为：0 - 否；1 - 是； 默认是。 

 
参数546：在DNS查询支持TCP方式的情况下，该软件参数用于判断AMF是否对DNS TCP链路信息进行周期性检查，例如检查链路对应的SC状态是否有效、链路个数是否正确等。取值为：0 - 否；1 - 是； 默认是。 

 
参数547：该软参用于控制局间切换新局I-SMF选择失败导致对应PDU会话切换失败时，是否通知SMF释放。取值为：0 - 否；1 - 是； 默认否。 

 
参数548：使用fake DNN发现SMF时本地发现模板id。取值范围为0-65535； 默认0。 

 
参数550：该软参用于控制PLMN改变后是否重新获取切片签约数据。取值为：0 - 否；1 - 是； 默认否。 

 
参数551：该软参用于控制是否优化注册过程中等待N2释放响应过程中与去注册冲突。取值为：0 - 否；1 - 是； 默认是。 

 
参数553：该软参用于控制收到用户相关的ERROR INDICATION消息指示NGAPID错误时是否触发UE CONTEXT RELEASE COMMAND消息。取值为：0 - 否；1 - 是； 默认否。 

 
参数554：该软参用于控制是否支持在UDM订阅请求中携带plmnId。取值为：0 - 否；1 - 是； 默认是。 

 
参数555：该软参用于控制当两个带有相同NasPdu字段的Initial UE业务请求冲突时，是否采用replace的策略。取值为：0 - 否；1 - 是； 默认是。 

 
参数556：该软参用于控制RAN配置更新消息缓存时长，默认150毫秒。 

 
参数558：该软参用于控制当老的PDU已经去活时相同DNN的多PDU会话是否选择同一个A-SMF。取值为：0 - 否；1 - 是； 默认是。 

 
参数560：该软参用于控制连接态业务请求过程中SMF故障检测后释放会话时是否通知基站PDU释放。取值为：0 - 否；1 - 是； 默认是。 

 
参数562：该软参用于控制AMF是否记录PDU会话的用户面状态。取值为：0 - 否；1 - 是； 默认否。 

 
参数563：该软参用于控制连接态时MT-LR定位是否向基站发送Location Reporting Control消息。取值为：0 - 否；1 - 是； 默认是。 

 
参数564：该软参用于控制业务请求过程中是否缓存N2容器类型是PDU资源修改的N1N2Transfer请求。取值为：0 - 否；1 - 是； 默认是。 

 
参数565：该软参用于控制局间未切换会话I/V-SMF改变/删除时AMF是否通知source I/V-SMF释放。取值为：0 - 否；1 - 是； 默认否。 

 
参数566：该软参用于控制当上行initial UE消息过负荷丢弃时是否发送N2释放消息。取值为：0 - 否；1 - 是； 默认否。 

 
参数568：该软参用于控制是否在注册过程中并行处理NAS未投递指示消息。取值为：0 - 否；1 - 是； 默认是。 

 
参数569：该软参用于控制当N2释放流程指示当前UE正在EPS回落时，是否丢弃PDU重建消息。取值为：0 - 否；1 - 是； 默认是。 

 
参数570：该软参用于控制无UDSF全量备份接管场景，是否支持通过扫描的方式发送打包的ZTE接管通知消息。该软件参数值设置为0：不支持。该软件参数值设置为1：支持。默认支持。 

 
参数571：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式发送打包的ZTE接管通知消息后，等待响应的超时时长。取值范围为1-60，默认1秒。 

 
参数572：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式每线程每秒至多可以发送的打包的ZTE接管通知消息数量。取值范围为1-200，默认2包每秒。 

 
参数575：该软参用于控制Xn切换流程发送的SmContextUpdateData是否携带变化的epsInterworkingInd。取值为：0 - 否；1 - 是； 默认是。 

 
参数577：该软参用于控制业务请求等移动性流程中，当SMF故障且AMF本地无对应TA缓存时，是否进行SMF发现。取值为：0 - 不发现；1 - 发现；默认不发现。 

 
参数578：该软参用于控制注册流程和SMF交互后是否继续缓存冲突的无法识别SMF是否改变的N1N2 Message Transfer的PDU修改或释放。取值为：0 - 否；1 - 是； 默认是。 

 
参数579：该软参用于控制全量备份场景，本局AMF是否将备份AMF加入本地检测列表，并在接管用户时检查备份AMF状态。默认检查备份局状态。 

 
参数580：该软参用于控制全量备份场景，本局AMF通过无线侧消息接管用户，并检查到备份AMF状态正常时，上行消息处理的方式。默认按全量容灾方式处理。 

 
参数581：该软参用于控制全量备份场景，本局AMF通过非无线侧消息接管用户，并检查到备份AMF状态正常时，下行消息处理的方式。默认按部分容灾方式处理。 

 
参数582：该软参用于控制5GS到EPS的切换流程中是否检查UE的S1 mode能力。取值为：0 - 否；1 - 是； 默认是。 

 
参数583：该软参用于控制当AMF收到SMF的N1N2MessageTransfer消息触发I-SMF改变是否回失败响应消息。取值为：0 - 否；1 - 是； 默认是。 

 
参数585：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为漫游PDU会话携带hplmnSnssai 。取值为：0 - 否；1 - 是；默认否。 

 
参数588：该软参用于控制是否支持强制向UDM获取及订阅ue-context-in-smf上下文。取值为：0 - 否；1 - 是；默认否。 

 
参数590：该软参用于控制当4到5切换重定向，目标局和MME都支持双栈时，目标局优选IP类型。取值为：0 - IPv4；1 - IPv6；默认IPv4。 

 
参数591：该软参用于控制Xn切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同Xn切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。 

 
参数592：该软参用于控制AMF内N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF内N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。 

 
参数593：该软参用于控制AMF间N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF间N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。 

 
参数594：该软参用于控制EPS到5GS的N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同EPS到5GS的N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。 

 
参数596：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为HR漫游PDU会话携带DTSSA特性 。取值为：0 - 否；1 - 是；默认是。 

 
参数597：该软参用于控制切换过程中收到切换完成的更新响应后再收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同之前的处理；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认保持之前的处理。 

 
参数598：该软参用于控制是否优化老局流程与上行透传消息的冲突策略。取值为：0 - 否；1 - 是；默认否。 

 
参数600：该软参用于控制AMF处理偶联退服消息的最大速率 ，超过的偶联退服消息将被延迟处理。取值为：0-10000（个/秒）；默认0（个/秒），表示不控制。 

 
参数601：该软参用于控制AMF进行偶联状态检测的最大速率。取值为：1-2000（个/秒）；默认10（个/秒）。 

 
参数602：该软参用于控制AMF进行偶联状态检测的超时时长。取值为：1-10秒；默认3秒。 

 
参数603：该软参用于控制接管用户更新SMF失败是否释放会话。取值为：0 - 否；1 - 是；默认是。 

 
参数604：该软参用于控制透传PDU SESSION RESOURCE RELEASE RESPONSE给SMF时是否需要等相应消息。取值为：0 - 否；1 - 是；默认是。 

 
参数605：该软参用于控制DNS性能统计UDP响应报文过长场景是否统计到UDP响应消息被截断计数器中。取值为：0 - 否；1 - 是；默认否。 

 
参数606：该软参用于控制当收到SBI口的失败响应消息而进行Nas原因值映射，若应用错误向配置转换失败，是否尝试继续匹配。取值为：0 - 否；1 - 是；默认否。 

 
参数607：该软参用于控制局间注册和TAU流程中old AMF用量上报是否受开关控制。取值为：0 - 否；1 - 是；默认是。 

 
参数608：该软参用于控制局间切换发现TargetAMF时携带切片的方式是否需要根据目标TA的PLMN决策。取值为：0 - 否；1 - 是；默认否。 

 
参数609：该软参用于控制因ISMF发送SmContextCreateData时是否需要更新SmContextStatusUri中的syn。取值为：0 - 否；1 - 是；默认是。 

 
参数610：该软参用于控制切换流程被N2释放流程冲突时是否优化UEContextReleaseCommand消息中原因值。取值为：0 - 否；1 - 是；默认否。 

 
参数614：该软参用于控制过负荷时是否要上报信令跟踪。取值为：0 - 否；1 - 是；默认否。 

 
参数615：该软参用于控制AMF向SMSF发起激活短消息时，携带GUAMI的方式。取值为：0 - 携带服务GUAMI；1 - 携带AMF的GUAMI列表；默认携带服务GUAMI。 

 
参数616：该软参用于控制是否强制获取短消息签约。取值为：0 - 否；1 - 是；默认否。 

 
参数617：该软参用于控制是否强制订阅短消息签约。取值为：0 - 否；1 - 是；默认否。 

 
参数618：该软参用于控制AMF切换入局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。 

 
参数619：该软参用于控制AMF收到流程外的UDM去注册通知，是否释放周边网元。取值为：0 - 否；1 - 是；默认否。 

 
参数620：该软参用于控制NAS未投递流程收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 并行处理；1 - 有MM层消息未投递时缓存处理；2 - 缓存处理；默认有MM层消息未投递时缓存处理。 

 
参数621：该软参用于控制SourceAMF收到N2InfoNotify前又收到UEContextReleaseRequest是否需要处理N2释放流程。取值为：0 - 否；1 - 是；默认是。 

 
参数622：该软参用于控制切换与其它流程冲突时是否强制将用户上下文同步给cache和CDB。取值为：0 - 否；1 - 是；默认否。 

 
参数623：该软参用于AMF进行PCF发现时，是否仅依据UE策略配置开关来决策是否要发现PCF UE策略服务。取值为：0 - 否；1 - 是；默认否。 

 
参数624：该软参用于控制5G内切换新局AMF或者互操作切换5G AMF在预处理阶段被流程冲突后是否强制删除PDU上下文。取值为：0 - 否；1 - 是；默认是。 

 
参数625：该软参用于控制业务请求过程中，ISMF插入、改变是否向LIG发送消息。取值为：0 - 否；1 - 是；默认否。 

 
参数626：该软参用于控制NRF注册或者更新时Service是否支持携带interPlmnFqdn参数。取值为：0 - 否；1 - 是；默认否。 

 
参数627：该软参用于控制局间初始UE消息注册请求完整性保护检查通过时，是否通过Namf_Communication_UEContextTransfer请求消息向老局AMF获取用户上下文。取值为：0 - 否；1 - 是；默认否。 

 
参数628：该软参用于控制在注册与签约变更流程中，当会话切片不在AllowedNssai中时，是否需要删除不在AllowedNssai中的会话或重建在AllowedNssai中的会话。取值为：0 - 否；1 - 是；默认是。 

 
参数629：该软参用于控制amf重定向流程是否支持重选。取值为：0 - 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|软参索引|参数可选性: 必选参数类型: 数字|该配置用于设置communication服务内部的一些功能参数，主要针对非协议明确要求的、异常厂家IOT、自厂家优化的功能或实现。参数1：针对网络侧触发的AN Release流程（参见TS 23502 4.2.6 AN Release章节），如果RAN在UE CONTEXT RELEASE COMPLETE消息中没有携带要去活N3隧道的PDU，则AMF根据此参数控制是否向SMF发送更新消息。参数2：用于控制局间切换或局间registration时，old AMF是否将该用户的订阅信息传递给目标AMF 或 target AMF。默认开启。主要用于异常家对接，对对方AMF不支持此功能时可关闭。参数3：用于控制局间切换或局间registration时，new AMF或targetAMF要不要接纳old AMF传递的订阅信息。参数4：用于控制是否跟踪RAN局向消息。参数5：用于控制PDU建立过程中，AMF是否获取当前PDU对应的S-NSSAI所对应的切片实例NSI。参数7： 用户从5G切换到4G EPS之后，AMF通过本参数控制是否立即删除用户上下文。参数8： 通过动态命令触发向NRF注册时，通过本软参可控制AMF是否先利用FQDN向DNS查询NRF地址。参数9： 当NRF地址采用FQDN方式配置时，该参数用于控制在进行DNS查询时，优先通过本地Cache查询，还是优先通过DNS Server查询。0表示优先本地Cache查询。1表示优先DNS Server查询。参数10：该软参用于控制S-NAPTR RR的优先级是否遵从3GPP。默认是。参数11：该软参用于控制是否支持跟踪Nas Container。默认是。参数12：在NF订阅策略配置为支持续订阅的情况下，AMF根据该参数设置（单位为分钟），来控制在NF订阅有效期到达前，提前多少分钟进行续订阅。参数13：该软参用于控制是否支持无SUPI时缓存上报用户信令。默认否。参数14：该软参用于控制是否支持回收共享表。默认是。参数16：保留软参。参数17：该软参用于控制是否支持无ISDN时缓存上报用户信令 。默认否。参数18：保留软参。参数20：该软参用于控制5G到4G的移动注册过程中是否使用next uplink nas count生成映射KASME。默认否。参数21：该软参用于控制注册请求followon标记置位时是否通知基站建UE上下文。默认是。参数22：该软参用于控制是否携带PLMN-ID参数向UDM获取签约数据。默认是。参数23：该软参用于控制S1 mode to N1 mode NAS transparent container是否包含5G UE Security capability。默认是。参数27：该软参用于控制是否强制使用初始上下文建立下发注册接受。默认否。参数28：该软参用于控制SBI接口中gNBValue的字段格式。默认gNBValue。参数29：本软参用于控制在检测到主备NRF都断链后，AMF是否清空本地发现缓存。设置为1，表示清空。参数30：该软参用于控制是否支持上下文健康检查。默认是。参数31：该软参用于控制是否支持NGAP转发表的健康检查 。默认是。参数32：该软参用于控制Forward relocation request消息中的UE NR security capability IE的长度。默认否。参数33：该软参用于控制是否限制全0的routingId。默认否。参数34：该软参用于控制无N26情况下是否对向UDM订阅ue-context-in-smf上下文。默认是。参数35：该软参用于控制是否支持AS安全修改。默认是。参数36：该软参用于控制Registration(unt)携带Uplink data Status是否进行active up conection操作。默认是。参数37：该软参用于控制是否对UE的安全能力参数进行检默认为90：Payload not  forwarded信息。默认否。参数39：该软参用于控制是否将EPS映射安全上下文中的NAS COUNT设置为5G NAS COUNT。默认是。参数40：该软参用于控制业务请求流程是否分配GUTI。默认否。参数41：该软参用于控制是否在当前5G安全上下文下行NAS COUNT基础上设置下行NAS COUNT。默认是。参数42：该软参用于控制业务请求是否先触发初始上下文建立。默认是。参数43：该软参用于控制 AMF与MME之间消息中的FTEID是否使用N26 AMF GTP-C interface。默认否。参数44：保留软参。参数45：该软参用于控制AMF进行NF订阅时是否携带PLMN-ID参数。默认是。参数46：本软参用于控制业务是否开启偶联状态检测功能。设置为1，表示开启偶联状态检测。参数47：该软参用于控制是否默认UE支持NEA0算法。默认是。参数48：该软参用于控制是否默认UE支持NEA1算法。默认是。参数49：该软参用于控制是否默认UE支持NEA2算法。默认是。参数50：该软参用于控制是否默认UE支持NEA3算法。默认是。参数51：该软参用于控制是否默认UE支持NIA0算法。默认是。参数52：该软参用于控制是否默认UE支持NIA1算法。默认是。参数53：该软参用于控制是否默认UE支持NIA2算法。默认是。参数54：该软参用于控制是否默认UE支持NIA3算法。默认是。参数55：该软参用于控制用户发生鉴权拒绝时是否上报通信失败。默认是。参数56：该软参用于控制用户发生注册拒绝时是否上报通信失败。默认是。参数57：该软参用于控制用户发生业务请求拒绝时是否上报通信失败。默认是。参数58：该软参用于控制用户发起网络侧去注册时是否上报通信失败。默认是。参数59：该软参用于控制初始上下文建立失败时是否上报通信失败。默认是。参数60：该软参用于控制初始注册时是否强制向UDM进行注册。默认是。参数61：该软参用于控制初始注册时是否强制向UDM获取签约数据。默认否。参数62：该软参用于控制发送SmContextUpdateData消息激活用户面是否携带ueLocation字段。默认否。参数63：该软参用于控制RAN发起的N2释放流程N2 Release command携带的原因值。默认携带N2Release请求中的原因值。参数64：该软参用于控制收到initial ue message是否要检查偶联有效性。默认是。参数65：该软参用于控制initial ue message偶联有效性检查失败是否要abort偶联。默认否。参数66：该软参用于控制网络侧没有获取到用户上下文时是否向UE要SUCI。默认是。参数67：该软参用于控制收到UE-CONTEXT标记时是否下发init context setup request消息。默认是。参数68：该软参用于控制偶联状态检测失败时是否删除偶联信息。默认是。参数69：该软参用于控制收到偶联断链时是否删除偶联信息。默认是。参数70：该软参用于控制MME消息中的GW FQDN是否需要去除top前缀保存。默认否。参数72：该软参用于控制SBI接口中的Snssai是否包含sd。默认否。参数73：该软参用于控制NGAP接口中的Snssai是否包含sd。默认否。参数74：该软参用于控制PCF发现时是否携带PLMN信息。默认否。参数75：该软参用于控制局间上下文响应中是否携带UE无线能力参数。默认是。参数76：本软参用于控制SC在重启时是否从Communication服务的Special SC加载局向相关表数据，默认否。参数77：本软参用于控制偶联表记录丢失是否终止该偶联，默认是。参数78：本软参用于控制从SC上是否删除老化的局向相关表记录，默认否。参数79：本软参用于控制收到SIG的偶联退服是否检验FRT表，默认是。参数80：该软参用于控制连接类消息amfngapid异常时给RAN发送释放命令还是是Error Indication。默认发送Error Indication。参数81：保留软参。参数82：该软参用于控制HTTP头中的ContentType multipart/related是否修正为小写字母 。默认否。参数84：该软参用于控制NULL scheme SUCI是否需要转换为BCD码。默认否。参数85：该软参用于控制没有签约UE AMBR时AMF是否携带本局默认UE AMBR 给MME。默认是。参数86：该软参用于控制是否在注册更新流程时的注册拒绝消息中携带T3502。默认否。参数87：该软参用于控制SBI消息中的NAS IE编码格式。默认包含IEI和长度部分。参数88：该软参用于控制切换时没有非直传隧道信息是否在HANDOVER COMMAND中构造PDU Session Resource Handover List。默认否。参数89：该软参用于控制非漫游场景下进行其他网元NRF发现时是否携带target plmn list。默认否。参数90：该软参用于控制鉴权返回二次同步失败时是否给UE发送鉴权拒绝。默认是。参数91：本软参用于控制接收主动负载重平衡启动动态命令时，是否处理动态命令，默认否。参数92：本软参用于控制是否支持5G SA默开时的特定T3502定时器，如果该软参开启，系统在鉴权过程触发5G SA默开、签约数据触发5G SA默开时, 注册拒绝携带特定的T3502定时器给UE， 默认否。参数93：该软参用于控制是否在未做完保的注册拒绝消息中携带T3502，如果关闭，注册拒绝未做完保时，不携带T3502，默认否。参数94：该软参用于控制Xn切换失败是否保持connect态。默认否。参数95：该软参用于控制是否检查NRF返回的NFID是否有效。默认否。参数96：该软参用于控制SCTP没有和gNB关联时是否终止偶联。默认是。参数97：该软参用于控制gNB记录缺失时是否终止偶联。默认是。参数98：该软参用于控制是否订阅SMF选择签约数据改变，默认是。参数99：该软参用于控制是否支持上下文请求携带CIoT Optimizations Support Indication，默认否。参数100：该软参用于控制是否支持互操作创建会话中携带切片信息，默认否。参数101：该软参用于控制是否给PCF携带时区，默认是。参数102：该软参用于控制是否支持组合SUPI号段限制接入和TA限制接入。默认否。参数103：该软参用于控制当paging超时时，是否将用户设置为不可达，默认否。参数105：该软参用于控制注册流程是否支持提前下发初始上下文建立。默认否。参数106：该软参用于控制局内移动I-SMF会话创建请求是否携带smfUri，默认携带。参数107：该软参用于控制局间移动I-SMF会话创建请求是否携带smfUri，默认携带。参数108：该软参用于控制是否把7-5GS服务不允许计数归类为用户原因。默认否。参数109：该软参用于控制是否把15-该TA没有合适小区计数归类为用户原因。默认否。参数110：该软参用于控制是否把111-协议失败，未指定计数归类为用户原因。默认否。参数111：保留软参。参数112：该软参用于控制全量备份场景信令跟踪是否上报接管通知消息，默认不上报。参数113：该软参用于控制是否按NFID清除缓存，默认是。参数114：该软参用于控制当寻呼的失败次数达到此软参时（等于或者大于），那么之后的寻呼，如果仍然失败，则不再统计寻呼的性能统计（包括全局和基于TA）。参数115：该软参用于控制5GS到EPS的切换是否需要通知SMF释放非直传隧道，默认是。参数116：该软参用于控制强制向RAN传递TCE信息。默认是。参数117：该软参用于控制选择NSSF时，是否支持NF级别的重选。默认否。参数118：该软参用于控制选择AUSF/UDM时，是否支持NF级别的重选。默认否。参数119：该软参用于控制选择AMF/SMF/PCF/SMSF/GMLC/LMF时，是否支持NF级别的重选。默认否。参数120：该软参用于控制是否把27-N1模式不允许计数归类为用户原因。默认否。参数121：该软参用于控制对ho required没有携带的pdu是否在流程最后是否给smf发update，默认是。参数122：该软参用于控制是否将业务请求接收消息码流填入到PDUSessionResourceSetupList中。默认否。参数123：该软参用于控制是否支持NF不可达发现查询信令上报，默认不上报。参数124：该软参用于控制，在SMF触发的paging过程中收到SMF发起的N1N2Transfer req，两次N1N2Transfer PDUID不同时，是缓存新的N1N2Transfer req还是依据优先级采取替换或者拒绝的策略，默认依据优先级。参数125：该软参用于控制Forward Relocation Request消息是否携带C-MSISDN 。默认否。参数126：该参数用于控制在X2口上报消息中的ServiceAreaList信元是否使用TAIList的格式来编码，默认不使用。参数128：该软参用于控制是否将注册接受消息码流填入到PDUSessionResourceSetupList中。默认否。参数129：该软参用于控制是否将SDM订阅请求中的callback设置为v2版本。默认否。参数130：该软参用于控制AMBR从bps转化为kbps时的取整方式。默认向下取整。参数131：该软参用于控制新注册的用户与PCF交互失败后是否后续不再与PCF交互。默认否。参数132：该软参用于控制是否支持TaCache表的老化处理。默认否。参数133：该软参用于控制TaCache表的老化时长。默认24小时。参数134：该软参用于控制业务DSL定时器选择开关。默认业务定制定时器。参数135：该软参用于控制是否支持NAS重放保护。默认否。参数136：该软参用于控制老局注册更新流程中是否通知SMF去活用户面。默认否。参数137：该软参用于控制是否支持小型化NSSF功能。默认否。参数138：保留软参。参数139：该软参用于控制GUTI分配方式。默认固定索引方式。参数140：该软参用于控制AMF收到PCF的PRA订阅后是否立即上报。默认立即上报。参数141：该软参用于控制在跨AMF注册流程中收到目标AMF Namf_Communication_RegistrationStatusUpdate Request消息且transferStatus信元值为“NOT_TRANSFERRED“时，源AMF回复Namf_Communication_RegistrationStatusUpdate响应时，响应消息中的regStatusTransferComplete字段取值是否为false。默认为false。参数142：该软参用于判断故障或判断恢复时，UE策略服务是否参与判断。缺省同”UE策略服务不参与判断“。当向PCF获取AM和UE策略的策略配置为UE策略不支持PCF交互时，此软参不起作用。参数143：该软参用于支持互操作的终端选择到非融合PGW-C+SMF时，在相同DNN相同切片情况下，是否支持选择同一个SMF，取值为：0-不支持，1-支持；默认0-不支持。参数144：该软参用于控制在不同PLMN网络下，发现SMF时，携带requester-plmn-list是否从本局支持的PLMN配置中获取。开关默认为否，从用户所在TA中获取。开关打开后，从本局支持的PLMN配置中获取。取值为：0-否，1-是；默认0-否。参数145：该软参用于控制AMF是否上报4/5G combo信令，默认上报。参数146：该软参用于控制是否支持过滤表容量告警上报。默认过滤。参数147：该软参控制注册流程创建UE策略后是否释放N2连接。取值为：0-否，1-是；默认0-否。参数148：该软参控制在短消息激活时是否携带Timezone信息。取值为：0-否，1-是；默认1-是。参数149：该软参控制是否检查SMF请求消息的地址。取值为：0-否，1-是；默认0-否。参数150：该软参控制5到4的Attach过程是否兼容5GS_TO_EPS_MOBILITY 原因值。取值为：0-否，1-是；默认1-是。参数151：该软参控制AMF已经携带smsfid发现smsf时是否还携带supi发现smsf，是否携带supi发现smsf还受网管配置SET NRFDISCSMSFPARACFG控制。取值为：0-否，1-是；默认0-否。参数152：该软参用于控制是否在AMF发给UE的注册拒绝消息中携带reject NSSAI。参数153：该参数用于控制AMF是否下发Redirection for Voice EPS Fallback指示给RAN，用于后续EPS Fallback时，RAN侧判断是否可以回落。取值为：0-否，1-是；默认1-是。参数154：该软参控制状态外收到UDM的原因值为初始注册或注册区域变更的去注册通知是否删除UE上下文。取值为：0-否，1-是；默认1-是。参数155：该参数用于控制AMF是否支持动态偶联详细信息检查。取值为：0-否，1-是；默认0-否。参数156：该参数用于设置动态偶联一致性检查失败时处理策略。取值为：0-更新对端地址信息，1-终止偶联；默认0-更新对端地址信息。参数157：该软参用于业务请求过程中rrc重建场景是否激活原先激活态pdu。取值为：0-否，1-是；默认0-否。参数158：该软参用于从SMF检索上下文失败导致5GS到EPS切换失败的原因值。取值为：0-255；默认7。参数160：该软参用于控制ISSU升级时Communication虚机升级步长，默认为1。参数161：该软参用于控制无用户使用后UE无线能力记录的Cache老化时间，默认10分钟。参数162：该软参用于控制是否在收到UDM触发的去注册后，立即发送SDM 去订阅消息，默认为1。参数163：该软参用于控制在使用NRFClient模式时，当NRF更新流程失败，并且响应码不是主备不可用的响应码，此时是否触发NRF重新注册。配置为“是”，表示触发重新注册，默认为“是”。参数164：该软参用于设置携带了selectedDnn参数时，selMode参数的携带策略。参数165：该软参用于控制UE-AMBR传递优化。默认优化。参数166：该软参用于控制5G切换4G时是否优选本合设局MME，默认为1。参数168：该软参用于控制是否支持性能统计定时上报，默认为支持。参数169：该软参用于控制注册拒绝消息中携带Rejected NSSAI的条件，当软参打开，仅nas原因值为62时携带；当软参关闭，不看原因值，均可以携带，默认为打开。参数170：该软参用于控制非漫游用户的DNN OI中PLMN来源，默认为SUPI。参数171：该软参用于控制是否支持忽略SMC过程，默认不支持。参数172：该软参用于控制SMF容灾IMS会话释放原因值。参数173：该参数用于指定卸载过程中，AMF网络侧去注册用户后，等待用户触发初始注册请求的时间，默认10s。参数174：该参数用于控制多PDU并行激活时延时发现SMF的时长，默认0ms,不延时。参数175：该参数用于收到N1N2Transfer消息出areaOfValidity区域时回N1N2MessageTransferRspData中的原因值,默认ATTEMPTING_TO_REACH_UE。参数176：该参数用于控制收到 PDU SESSION RESOURCE MODIFY RESPONSE消息后是否在SmContextUpdateData中强制携带UserLocation，取值为：0-否，1-是；默认是。参数178：该软参用于控制当5GMM Cause为91时用以替换的值，默认91，不替换。参数179：该软参用于控制v2版本的UplinkSMS中是否支持imeisv，取值为：0-否，1-是；默认是。参数185：该软参用于控制SmContextCreateData结构中hSmfUri, smfUri, additionalHsmfUri, additionalSmfUri信元的URI模式，详细参见29.502 CR0321。早期协议定义有歧义，会导致AMF发送给SMF的URI格式为“{apiRoot}/nsmf-pdusession/v1/”或者“{apiRoot}/nsmf-pdusession/v1/pdu-sessions/”。协议标准通过29.502 CR0321进行澄清，要求为“{apiRoot}/nsmf-pdusession/v1/”，AMF使用软参控制以便兼容对接现网版本。取值为：0-API URI，1-Resource URI；默认API URI。参数187：该软参用于控制AMF本地决策Allowed NSSAI为空时是否直接拒绝UE接入；取值为：0-否，1-是；默认0-否。参数188：该软参用于控制AMF本地决策Allowed NSSAI为空时，如果直接拒绝UE接入，应该携带的限制接入原因值；默认值为62-No network slices available。参数189：该软参用于控制用户注册时AMF是否强制不获取用户签约切片信息；默认否。参数190：该软参用于控制是否禁止用户建立多个紧急PDU；取值为：0-否，1-是；默认0-否。参数192：该软参用于是否统计业务请求流程无失败原因计数器时的请求数，用于控制版本间KPI波动过大，取值为：0-否，1-是；默认是。参数193：该软参用于控制一条5G Backup Data Notification消息最多包含的用户群数。参数194：该软参用于控制UE请求的S-NSSAI不在允许切片中是否拒绝PDU建立，取值为：0-否，1-是；默认是。参数195：该软参用于控制UE安全能力校验失败时的拒绝原因值，取值为：3-非法UE，6-非法ME，7-5G服务不允许，23-UE安全能力不匹配；默认6-非法ME。参数196：该软参用于控制AMF局间传递是否携带smssupport字段，取值为：0-否，1-是；默认否。参数197：该软参用于控制PCF UE策略创建请求消息是否携带有效的SupportedFeatures，取值为：0-否，1-是；默认否。参数198：该软参用于控制移动性流程是否支持基于preferred-locality发现I-SMF/V-SMF。参数199：该软参用于控制N11接口消息中servingNetwork的填写方式，取值为：0-TA中的PLMN；1-本局配置PLMN；默认0。参数201：该软参用于控制业务请求中AMF因底层链路问题向SMF发送失败时是否删除会话信息。默认是。参数202：该软参用于控制业务请求中与SMF交互无响应时是否删除会话信息。默认否。参数203：保留软参。参数204：保留软参。参数205：该软参用于控制Xn切换I-SMF插入发送SmContextCreateData是否携带AsmfId，默认否。参数206：是否限制NGAP BitRate IE值的大小。默认否。参数207：保留软参。参数208：保留软参。参数209：该软参用于控制收到基站NG Setup时检查所支持TA列表的策略。默认使用策略1。参数210：该软参用于控制SBI消息中Userlocation IE的timestamp格式。默认UTC时间。参数211：该参数用于控制移动性或切换流程I-SMF插入改变时是否携带SNSSAI给SMF，默认携带。参数212：该参数用于控制在非漫游场景下进行其他网元NRF发现的时候，是否携带requester plmn list。参数213：该参数用于控制在空闲态4到5注册更新时是否忽略到UDM获取切片及切片选择过程。参数214：该软参用于控制AMF内N2切换是否携带UE Time Zone给SMF。默认否。参数215：该软参用于控制AMF间N2切换是否携带UE Time Zone给SMF。默认否。参数216：该软参用于控制非Special SC在NRF发现后是否支持订阅。默认是。参数218：该软参用于流程冲突处理是否校验用户合法性。默认否。参数219：该软参用于控制限制接入带counter的SUPI号段优先。软参开启时，如果SUPI号段配置在SUPI号段接入限制中，且counter配置不为0，就以该配置数据为准。默认不开启。参数220：该软参用于控制当用户位置有效时是否在SmContextUpdateData中强制携带UserLocation，默认开启。参数222：该软参用于控制对于不在切换列表中的PDU是否去除UeContextCreateData消息中的N2SmInformation。参数223：该软参用于控制注册位置改变时是否通知SMF。参数224：该软参用于控制业务请求位置改变时是否通知SMF。参数225：保留软参。参数226：该软参用于控制是否支持回收异常信令管控表。参数227：保留软参。参数230：保留软参。参数232：该软参用于控制注册下发注册接受后被流程冲突抢占时是否强制同步用户上下文给cache/CDB。默认强制同步。参数234：该软参用于控制释放内部索引资源的阈值。参数235：该软参用于控制内部资源老化回收时长。参数238：保留软参。参数245：该参数用于控制NRFClient在处理UDM/AUSF/PCF的发现响应时，若对于NFProfile中携带号段小于软参设置值，则不进行发现缓存。默认值为2。参数246：该参数用于控制NRFClient在发现缓存老化时间的散列总时长，0默认为散列总时长为100秒，30~600为正常散列总时长，其他值认为不启用该功能。参数247：该参数用于控制重新GUTI分配结束后，是否在注册上下文中保留MTMSI资源已经被其他用户占用的老GUTI。默认不保留直接覆盖。参数248：该参数用于控制UDM/AUSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数251：该参数用于控制在NRF发现后触发NF状态订阅时，是否同时考虑采用IPv4及IPv6地址组成的nfStatusNotificationUri来查询当前是否存在对应的订阅记录，如果存在则不发起订阅。默认同时考虑。参数252：该参数用于控制在收到SMF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数253：该参数用于控制SMF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数254：该参数用于控制在收到PCF/SMSF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数255：该参数用于控制PCF/SMSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数256：该参数用于控制非UDM/AUSF/SMF/PCF/SMSF类型的其他NF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数257：该参数用于控制UDM/AUSF状态由不可用变为可用，并且按NFId触发续缓存时，是否根据缓存信息中识别出的同组UDM/AUSF信息，按NF组进行续缓存。参数258：该参数用于控制NRFClient在处理发现响应时，针对同一个NF号段相同时，是否展开号码树。参数259：该参数用于控制根据指定UDM/AUSF的NFId，进行关联同组其他NFId信息查询的方式，采用优先匹配或全表匹配。参数260：该参数用于控制在业务请求流程过程中是否并发处理initial context setup fail response。默认否。如果不并发处理，则会采用丢弃的处理策略。参数262：该参数用于控制在SMF通过N1N2Transfer请求发起的paging流程过程中，AMF又收到相同PDUID的N1N2Transfer请求，是否给SMF发送N1N2Transfer Fail Notify，取值为：0-否，1-是；默认否。参数269：该参数用于控制上行透传过程中收到N2释放的是否替换当前流程，取值为：0-否，1-是；默认否。参数270：该软参用于控制业务请求流程中ISMF删除或改变时收到SMF成功响应但未携带N2SmInfo是否通知ISMF释放。取值为：0 - 否；1 - 是； 默认是。参数272：该软参用于控制UDP截断转TCP场景下DNS性能统计是否统计查询尝试次数。取值为：0 - 否；1 - 是； 默认否。参数273：该软参用于控制局内切换收到Handover Notify是否更新sctp id。取值为：0 - 否；1 - 是； 默认否。参数274：该软参用于控制流程冲突对于未切换的PDU是否需要忽略通知SMF切换取消。取值为：0 - 否；1 - 是； 默认否。参数275：该软参用于控制是否优化处理局间切换时UeContextCreatedData消息的location字段。取值为：0 - 否；1 - 是； 默认否。参数276：该软参用于控制PDU会话建立流程等待N1N2Transfer消息超时的处理策略取值为：0 - 通知SMF和UE；1 - 仅通知SMF；2 - 仅通知UE；3 - 不通知SMF和UE； 默认通知SMF和UE。参数278：该软参用于控制发送NRF发现请求时选择SBIGW SC的方式。参数279：278号软参为1时，该软参用于控制最大可以使用的SBIGW SC数。参数285：该软参用于控制NFProfile中IP地址对应的端口使用默认端口还是服务对应端口 。取值为：0 - 使用服务对应端口；1 - 使用默认端口； 默认使用服务对应端口。参数287：该软参用于控制连接态收到N1N2Transfer消息不携带areaOfValidity是否丢弃消息中的N2信息，取值为：0-否，1-是；默认否。参数289：该软参用于控制收到N1N2Transfer消息出areaOfValidity区域时是否把N2 SM information投递给RAN，取值为：0-否，1-是；默认否。参数291：该软参用于控制当SMF故障时AMF扫描用户删除会话，用户连接态时是否分别通知UE和基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数292：该软参用于控制N1N2Transfer流程等待SMF更新响应时收到高优先级的消息是否直接替换，取值为：0-否，1-是；默认是。参数293：该软参用于控制收到PATH SWITCH REQUEST消息是否检查安全上下文，取值为：0-否，1-是；默认是。参数348：该软参用于控制AS检查失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数349：该软参用于控制NGAP连接一致性校验失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数352：该软参用于控制当收到SMF的创建响应找不到会话上下文时是否给SMF发送释放请求消息。取值为：0 - 否；1 - 是；默认否。参数355：该软参用于控制融合局AMF所有本局配置的GUAMI均不可用下发AMF Status Indication消息时，是否在Unavailable GUAMI List中携带GUMMEI映射的GUAMI。默认不携带。参数401：该软参用于控制AMF发送的NRF注册或更新请求携带的taiList的最大个数，修改软参值不会触发NRF更新。默认为512。参数402：该软参用于控制AMF发送的NRF注册或更新请求携带的taiRangeList的最大个数，修改软参值不会触发NRF更新。默认为12。参数403：该软参用于控制AMF发送的NRF注册或更新请求中携带的每个PLMN下tacRange最大个数，修改软参值不会触发NRF更新。默认为2048。参数404：该软参用于控制AMF发送的NRF注册或更新请求中携带的所有PLMN下总的tacRange最大个数，修改软参值不会触发NRF更新。默认为20000。参数406：该软参用于控制同步备份表异常挂死回收时长即当该用户的注册上下文不存在时，此上下文最长存在时长,单位分钟。默认为120分钟。参数407：该软参用于控制guti重分配后是否通知基站。参数408：该软参用于控制AMF发送的NRF注册或更新请求中是否携带n2InterfaceAmfInfo参数：0-否，1-是；默认否，修改软参值不会触发NRF更新。参数410：该软参用于控制4到5注册流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数411：该软参用于控制局内注册更新流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数412：该软参用于控制在X1口获取用户信息消息中的AMF上报信息是否强制携带上次使用的EPS PLMN标识。默认不强制携带，即参数可选。参数413：该软参用于控制初始注册结束是否强制保留N2连接。0-否，1-是；默认否。参数414：该软参用于控制4到5移动性注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数415：该软参用于控制5G系统内注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数416：该软参用于控制局内注册更新流程AMF是否向UDM注册。0-否，1-是；默认否。参数418：该软参用于控制发生guti冲突时是否purge老用户。0-否，1-是；默认否。参数419：该软参用于控制AMF收到RAN发送的Initial Ue Message消息时，AMF是否要检查局向TA表。0-否，1-是；默认是。参数420：该软参用于控制当gNB局向的TA记录丢失时，是否终止该gNB局向关联的所有SCTP偶联。0-否，1-是；默认是。参数421：该软参用于控制gNB局向表和gNB局向TA表异常挂死回收时长，单位分钟。默认为60分钟。参数422：该软参用于控制当发生guti冲突时是否放弃新用户流程。0-否，1-是；默认否。参数423：发生guti冲突且需要放弃新用户流程时的失败原因。默认为111。参数424：该软参用于控制是否启用SBI发送保序，中移路由测试的模式开启时该软参需要关闭。0-否，1-是；默认是。参数425：该软参用于控制SBI发送保序间隔。默认5秒。参数426：该软参用于控制AMF发送的NRF注册或更新请求携带的guami的最大个数，修改软参值不会触发NRF更新。默认为16。参数427：该软参用于控制AMF发送的NRF注册或更新请求携带的plmn-id的最大个数，修改软参值不会触发NRF更新。默认为32。参数430：该软参用于控制IP地址细分导致切换失败后是否释放N2连接。0-否，1-是；默认否。参数431：该软参用于控制注册更新或者切入流程，发生SUPI冲突查询到残留用户上下文时，是否需要通知I/V-SMF释放会话。默认需要通知。参数432：该软参用于控制用户信息入库失败时是否清除用户。默认为是。参数433：该软参用于控制用户信息入库失败时是否立即通知UE。默认为是。参数434：该软参用于控制二次鉴权routingId不变时重新发现AUSF。0-否，1-是；默认否。参数435：该软参用于控制同一流程中支持的最大鉴权次数。默认为3。参数436：该软参用于控制局内切换过程中收到上行的SM、SMS、LCS等消息时的处理方式。默认为2，即预处理阶段并行处理，执行阶段缓存处理。参数437：该软参用于控制AMF是否支持EPS回落增强功能。0-否，1-是；默认否。参数438：该软参用于控制AMF保持用户EPS回落状态时长。默认6秒。该参数仅在“AMF支持EPS回落增强”开启后有效。参数441：该软参用于控制是否删除不属于本SC管理的用户上下文。0-否，1-是；默认是。该参数仅在“是否支持上下文健康检查”开启后有效。参数443：该软参用于控制是否优化PDU级上行透传流程被冲突的处理机制.0-否，1-是；默认是。参数444：该软参用于控制紧急PDU建立失败是否使用配置原因值.0-否，1-是；默认是。参数445：紧急PDU建立失败的配置原因值；默认为90。参数446：该软参用于控制4到5注册是否使用从老局AMF获取到的SUPI。0-否，1-是；默认是。参数447：该软参用于控制AMF给UDM的Homogeneous Support of IMS Voice over PS Sessions指示是否考虑用户签约、漫游协议、无线能力信息。0-否，1-是；默认是。参数448：AMF收到gNB发起的部分重启消息，若消息中仅包含RAN UE NGAP ID，则N2连接异常。该软参用于判断AMF是否支持gNB部分重启消息中包含异常的N2连接信息。参数449：在448号参数置为1时，为了防止仅包含RAN UE NGAP ID的部分重启消息过多，对AMF造成冲击，该软参用于控制AMF单位时间内处理此类异常的部分重启消息数目。参数450：在RAN重启过程中，RAN侧先释放根据某个RAN UE NGAP ID建立的N2连接，此时AMF侧仍然保持该连接。之后，RAN根据同样的RAN UE NGAP ID再次请求与AMF建立N2连接，AMF此时会检测到RAN UE NGAP ID冲突。该软参用于判断此时AMF是否启动优化处理。参数451：该软参用于控制移动性流程（如注册、业务请求）被只携带N1容器的N1N2 Msg Transfer消息冲突场景，AS安全没有建立时是否需要拒绝N1N2 Msg Transfer消息。默认不拒绝。参数452：该软参用于控制初始注册流程下发注册接受后被移动性注册流程冲突的场景，AMF是否拒绝移动性注册并携带隐式分离的原因值。默认不拒绝，AMF终止处理初始注册，正常处理移动性注册。参数454：该软参用于控制UDM清除AM签约数据时是否需要去注册用户。默认去注册用户。参数455：该软参用于控制EAP鉴权失败为MAC 失败、同步失败、非5G失败时是否需要发送鉴权拒绝。默认发送鉴权拒绝。参数456：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的流程冲突处理机制。默认开启优化。参数457：该软参用于控制局间注册老局流程资源保护定时器内被注册流程冲突的场景，如果注册请求携带的GUTI是本局分配的，是否释放局间注册老局流程用户的PDU会话资源。默认不释放，流程冲突处理会向SMF更新PDU会话。参数458：该软参用于控制是否在鉴权完成之前启动异常信令管控。0-否，1-是；默认是。参数461：保留软参461。参数462：该软参用于控制5GS到EPS的切换流程中是否限制未请求切换的PDU建立非直传隧道。默认限制。参数463：该软参用于控制HANDOVER COMMAND消息是否限制携带未请求切换的PDU信息。默认限制。参数464：该软参用于控制PDU建立流程中，用户发生移动性流程时的冲突处理是否优化。默认是。参数465：该软参用于控制收到N2释放请求时是否检查amfN2apId，默认检查。参数468：该软参用于控制AMF通知基站释放老的N2连接时原因值，默认NAS “Normal release”。参数469：该软参用于控制5G到4G时AMF释放N2连接的原因值，默认NAS “Normal release”。参数470：该软参用于控制负荷重平衡时AMF主动释放N2连接的原因值，默认NAS “Normal release”。参数472：该软参用于控制是否删除不属于本SC管理的N11保序表记录。默认是。参数473：该软参用于控制A-SMF发现携带preferred-tai时是否忽略nrfSupportedFeatures。默认忽略。参数474：该软参用于控制用户在NAS拥塞控制backofftimer时间内再次发起上行业务时是否仍处理该消息。默认值否，不处理该上行消息。参数475：该软参用于控制是否删除不属于本SC管理的备份表记录。默认是。参数476：该软参用于控制Communication服务定时触发打包同步的时长。默认200ms。参数477：该软参用于控制Communication服务定量触发打包同步的用户个数。默认10个用户。参数478：该参数用于控制AMF是否开启动态偶联管理类消息打包功能。默认不开启。参数479：该软参用于控制用量上报表的老化时间，默认30秒。参数480：该软参用于控制NG Setup请求消息缓存时长，默认150毫秒。参数481：该软参用于控制AMF收到NG Setup请求消息后，是否释放该基站之前接入的用户N2连接，默认释放。该功能用于测试场景，商用场景不建议打开。参数482：该软参用于控制内部索引资源TEIDC老化回收的时长 ，默认2小时。参数483：该软参用于控制收到N2释放请求时检查n2apid失败是否发送Error Indication ，默认发送。参数484：该软参用于控制AMF是否支持连接态用户由于收到SMF的N1N2MessageTransfer触发I-SMF改变处理，默认是。参数486：该软参用于控制老局为初始注册态或attach时是否等待超时定时器，默认否。参数487：该软参用于控制从NRF接收PCF状态通知时，NF故障列表是否进行处理，默认是。参数488：该软参用于控制从NRF接收LMF状态通知时，NF故障列表是否进行处理，默认否。参数489：该软参用于控制局间附着和局间初始注册时，老局AMF等待UDM去注册通知消息的时长，默认10秒。参数491：该软参用于控制是否检查N2消息中的RAN UE NGAP ID，默认是。参数493：该软参用于控制Xn口切换被其它流程冲突掉是否通知源NG-RAN释放N2连接，默认否。参数494：该软参用于控制是否使用Forward Relocation Request消息中的Selected PLMN ID，默认是。参数496：该软参用于控制UE注册请求携带无效的注册类型时，AMF是否当做初始注册进行处理，默认是。参数497：该软参用于控制注册流程被N2释放流程冲突的场景，当N2释放流程被缓存时，注册流程是否继续投递下行消息，默认不投递。参数499：该软参用于控制5G到4G的切换流程被Context Request消息冲突替换时是否需要保留用户上下文，默认是。参数500：该软参用于控制优化N2释放和注册的冲突处理的方式，默认不优化。参数501：该软参用于控制AMF是否支持SUPI格式的正确性检查，SUPI中的MSIN每一位取值应为0-9的BCD码，不允许出现A-F。取值为：0-否，1-是；默认否。参数502：该软参用于控制PATH SWITCH REQUEST携带重复的PDU Session ID时AMF是否直接给RAN发送失败响应；默认否。参数503：该软参用于控制NGAP Class1消息无上下文是否释放连接，默认否。参数504：该软参用于控制NGAP Class2消息无上下文是否释放连接，默认否。参数505：该软参用于控制业务请求流程时是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认是。参数506：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数507：该软参用于控制网络侧去注册流程收到Error Indication是否终止通知UE。取值为：0-否，1-是；默认是。参数508：该软参用于控制是否支持对NGAP的连接进行一致性校验校验，默认是。参数509：该软参用于控制AMF是否收到成功响应后再标记UE-AMBR已发送，默认是。参数511：该软参用于控制连接态两条相同PDU的N1N2Transfer消息冲突时是否先回复失败响应，默认否。参数512：该软参用于控制收到PDU资源修改或释放的N1N2Transfer消息时如果AS安全未建立是否尝试透传N1信息，默认是。参数513：该软参用于控制初始注册当UE指示不支持S1能力时是否清除S1能力信息，默认否。参数514：该软参用于控制注册流程被相同注册请求冲突时，AMF在丢弃重复注册请求的同时是否释放老连接并更新新的连接信息，默认是。参数515：该软参用于控制注册流程收到N2修改UE上下文失败响应导致流程失败的原因值。默认为9。参数516：该软参用于控制初始guti注册时完保失败且老用户处于连接态是否丢弃新的注册请求。默认为否。参数517：该软参用于控制是否维持老版本lastseen ta的设置。默认为否。参数518：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时两个N1N2Transfer请求都没携带ARP时，是否拒绝新来的N1N2Transfer请求。取值为：0-否，1-是；默认是参数519：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时新的N1N2Transfer请求优先级更高时，是否采用替换的策略。取值为：0-否，1-是；默认是参数520：该软参用于控制用量上报表记录的老化扫描个数。取值范围为：1-3000；默认500参数521：该软参用于控制AMF是否对UE携带的IMEi进行格式检查，IMEI必须为14或15位BCD码，不允许出现A-F。取值为：0-否，1-是；默认是。参数522：当NF进入故障列表及告警的时间较长时，业务负担增加。该软参用于判断是否对故障NF启用老化机制。对于启用老化机制的NF,当到达规定时间（即老化时间）时，它将从故障列表中删除并且恢复告警。参数523：当不可达NF发现成功，恢复正常状态后，该软参用于判断此时AMF是否通知SBIGW更新NF状态。参数524：当第522号参数设置为1后，即故障NF启用老化机制，该软参生效。该软参用于控制对故障列表中仅NRF检测的记录，AMF触发不可达周期性发现的时间门限。参数525：该软参用于控制对于紧急PDU是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认否。参数526：该软参用于控制信令管控表扫描速率。取值范围为：1-1000；默认50。参数527：该软参用于控制注册流程在和SMF交互前被N1N2 Message Transfer消息冲突，交互后针对未发生交互会话的N1N2 Message Transfer请求消息，是否继续缓存，默认是。参数529：该软参用于控制紧邻PLMN的TAC放在TAC-low-byte还是放在TAC-high-byte。取值为：0 - 紧邻PLMN的TAC放在TAC-high-byte；1 - 紧邻PLMN的TAC放在TAC-low-byte；默认紧邻PLMN的TAC放在TAC-high-byte。参数530：该软参用于判断是否支持gNB在给AMF发送NG SETUP消息中的UE Retention字段功能，从而保持用户的N2逻辑连接。参数531：该软参用于控制发现AMF非本PLMN时，是否携带target-plmn-list和requester-plmn-list参数给NRF。取值为：0-否，1-是；默认是。参数532：该软参用于控制注册流程中，当注册完成后收到PDU建立请求是否缓存。取值为：0-否，1-是；默认是。参数533：该软参用于控制空闲态5G到4G移动性流程中，AMF是否需要判断N26 license和开关。取值为：0-否，1-是；默认是。参数534：该软参用于控制Handover Notify之后收到目标基站的N2释放是否修正通知源基站N2释放的原因值。取值为：0-否，1-是；默认否。参数535：该软参用于控制不可达主动发现恢复后是否通知SBIGW。取值为：0-否，1-是；默认是。参数536：该软参用于控制AMF收到Initial UE的业务请求时是否拒绝缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数537：该软参用于控制在业务请求过程中，当AMF收到Update/Create SM Response时是否释放缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数540：该软参用于控制LIG触发批量撤控请求时，AMF扫描删除布控记录的速率。默认每100毫秒扫描100条布控记录。参数541：该软参用于控制是否丢弃在会话建立过程中收到的相同PDU Session ID的会话建立请求消息。取值为：0-否，1-是；默认是。参数542：该软参用于控制HR漫游用户发送SmContextCreateData消息时是否携带HsmfId。取值为：0 - 否；1 - 是； 默认否。参数543：该软参用于控制重复的PDU会话激活预处理失败是否需要通知SMF删除会话。取值为：0 - 否；1 - 是； 默认是。参数544：当基于PLMN的AMF支持的SNSSAI和AMF支持的SNSSAI发生连续批量的配置变更时，基站会触发大量配置更新流程，易造成业务载荷过量。本软件参数用于控制延时通知基站触发配置更新流程的时长。参数545：该软参用于控制4G到5G的切换流程中获取不到Allowed NSSAI是否使用PDU会话的SNSSAI替代。取值为：0 - 否；1 - 是； 默认是。参数546：在DNS查询支持TCP方式的情况下，该软件参数用于判断AMF是否对DNS TCP链路信息进行周期性检查，例如检查链路对应的SC状态是否有效、链路个数是否正确等。取值为：0 - 否；1 - 是； 默认是。参数547：该软参用于控制局间切换新局I-SMF选择失败导致对应PDU会话切换失败时，是否通知SMF释放。取值为：0 - 否；1 - 是； 默认否。参数548：使用fake DNN发现SMF时本地发现模板id。取值范围为0-65535； 默认0。参数550：该软参用于控制PLMN改变后是否重新获取切片签约数据。取值为：0 - 否；1 - 是； 默认否。参数551：该软参用于控制是否优化注册过程中等待N2释放响应过程中与去注册冲突。取值为：0 - 否；1 - 是； 默认是。参数553：该软参用于控制收到用户相关的ERROR INDICATION消息指示NGAPID错误时是否触发UE CONTEXT RELEASE COMMAND消息。取值为：0 - 否；1 - 是； 默认否。参数554：该软参用于控制是否支持在UDM订阅请求中携带plmnId。取值为：0 - 否；1 - 是； 默认是。参数555：该软参用于控制当两个带有相同NasPdu字段的Initial UE业务请求冲突时，是否采用replace的策略。取值为：0 - 否；1 - 是； 默认是。参数556：该软参用于控制RAN配置更新消息缓存时长，默认150毫秒。参数558：该软参用于控制当老的PDU已经去活时相同DNN的多PDU会话是否选择同一个A-SMF。取值为：0 - 否；1 - 是； 默认是。参数560：该软参用于控制连接态业务请求过程中SMF故障检测后释放会话时是否通知基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数562：该软参用于控制AMF是否记录PDU会话的用户面状态。取值为：0 - 否；1 - 是； 默认否。参数563：该软参用于控制连接态时MT-LR定位是否向基站发送Location Reporting Control消息。取值为：0 - 否；1 - 是； 默认是。参数564：该软参用于控制业务请求过程中是否缓存N2容器类型是PDU资源修改的N1N2Transfer请求。取值为：0 - 否；1 - 是； 默认是。参数565：该软参用于控制局间未切换会话I/V-SMF改变/删除时AMF是否通知source I/V-SMF释放。取值为：0 - 否；1 - 是； 默认否。参数566：该软参用于控制当上行initial UE消息过负荷丢弃时是否发送N2释放消息。取值为：0 - 否；1 - 是； 默认否。参数568：该软参用于控制是否在注册过程中并行处理NAS未投递指示消息。取值为：0 - 否；1 - 是； 默认是。参数569：该软参用于控制当N2释放流程指示当前UE正在EPS回落时，是否丢弃PDU重建消息。取值为：0 - 否；1 - 是； 默认是。参数570：该软参用于控制无UDSF全量备份接管场景，是否支持通过扫描的方式发送打包的ZTE接管通知消息。该软件参数值设置为0：不支持。该软件参数值设置为1：支持。默认支持。参数571：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式发送打包的ZTE接管通知消息后，等待响应的超时时长。取值范围为1-60，默认1秒。参数572：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式每线程每秒至多可以发送的打包的ZTE接管通知消息数量。取值范围为1-200，默认2包每秒。参数575：该软参用于控制Xn切换流程发送的SmContextUpdateData是否携带变化的epsInterworkingInd。取值为：0 - 否；1 - 是； 默认是。参数577：该软参用于控制业务请求等移动性流程中，当SMF故障且AMF本地无对应TA缓存时，是否进行SMF发现。取值为：0 - 不发现；1 - 发现；默认不发现。参数578：该软参用于控制注册流程和SMF交互后是否继续缓存冲突的无法识别SMF是否改变的N1N2 Message Transfer的PDU修改或释放。取值为：0 - 否；1 - 是； 默认是。参数579：该软参用于控制全量备份场景，本局AMF是否将备份AMF加入本地检测列表，并在接管用户时检查备份AMF状态。默认检查备份局状态。参数580：该软参用于控制全量备份场景，本局AMF通过无线侧消息接管用户，并检查到备份AMF状态正常时，上行消息处理的方式。默认按全量容灾方式处理。参数581：该软参用于控制全量备份场景，本局AMF通过非无线侧消息接管用户，并检查到备份AMF状态正常时，下行消息处理的方式。默认按部分容灾方式处理。参数582：该软参用于控制5GS到EPS的切换流程中是否检查UE的S1 mode能力。取值为：0 - 否；1 - 是； 默认是。参数583：该软参用于控制当AMF收到SMF的N1N2MessageTransfer消息触发I-SMF改变是否回失败响应消息。取值为：0 - 否；1 - 是； 默认是。参数585：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为漫游PDU会话携带hplmnSnssai 。取值为：0 - 否；1 - 是；默认否。参数588：该软参用于控制是否支持强制向UDM获取及订阅ue-context-in-smf上下文。取值为：0 - 否；1 - 是；默认否。参数590：该软参用于控制当4到5切换重定向，目标局和MME都支持双栈时，目标局优选IP类型。取值为：0 - IPv4；1 - IPv6；默认IPv4。参数591：该软参用于控制Xn切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同Xn切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数592：该软参用于控制AMF内N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF内N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数593：该软参用于控制AMF间N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF间N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数594：该软参用于控制EPS到5GS的N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同EPS到5GS的N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数596：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为HR漫游PDU会话携带DTSSA特性 。取值为：0 - 否；1 - 是；默认是。参数597：该软参用于控制切换过程中收到切换完成的更新响应后再收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同之前的处理；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认保持之前的处理。参数598：该软参用于控制是否优化老局流程与上行透传消息的冲突策略。取值为：0 - 否；1 - 是；默认否。参数600：该软参用于控制AMF处理偶联退服消息的最大速率 ，超过的偶联退服消息将被延迟处理。取值为：0-10000（个/秒）；默认0（个/秒），表示不控制。参数601：该软参用于控制AMF进行偶联状态检测的最大速率。取值为：1-2000（个/秒）；默认10（个/秒）。参数602：该软参用于控制AMF进行偶联状态检测的超时时长。取值为：1-10秒；默认3秒。参数603：该软参用于控制接管用户更新SMF失败是否释放会话。取值为：0 - 否；1 - 是；默认是。参数604：该软参用于控制透传PDU SESSION RESOURCE RELEASE RESPONSE给SMF时是否需要等相应消息。取值为：0 - 否；1 - 是；默认是。参数605：该软参用于控制DNS性能统计UDP响应报文过长场景是否统计到UDP响应消息被截断计数器中。取值为：0 - 否；1 - 是；默认否。参数606：该软参用于控制当收到SBI口的失败响应消息而进行Nas原因值映射，若应用错误向配置转换失败，是否尝试继续匹配。取值为：0 - 否；1 - 是；默认否。参数607：该软参用于控制局间注册和TAU流程中old AMF用量上报是否受开关控制。取值为：0 - 否；1 - 是；默认是。参数608：该软参用于控制局间切换发现TargetAMF时携带切片的方式是否需要根据目标TA的PLMN决策。取值为：0 - 否；1 - 是；默认否。参数609：该软参用于控制因ISMF发送SmContextCreateData时是否需要更新SmContextStatusUri中的syn。取值为：0 - 否；1 - 是；默认是。参数610：该软参用于控制切换流程被N2释放流程冲突时是否优化UEContextReleaseCommand消息中原因值。取值为：0 - 否；1 - 是；默认否。参数614：该软参用于控制过负荷时是否要上报信令跟踪。取值为：0 - 否；1 - 是；默认否。参数615：该软参用于控制AMF向SMSF发起激活短消息时，携带GUAMI的方式。取值为：0 - 携带服务GUAMI；1 - 携带AMF的GUAMI列表；默认携带服务GUAMI。参数616：该软参用于控制是否强制获取短消息签约。取值为：0 - 否；1 - 是；默认否。参数617：该软参用于控制是否强制订阅短消息签约。取值为：0 - 否；1 - 是；默认否。参数618：该软参用于控制AMF切换入局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数619：该软参用于控制AMF收到流程外的UDM去注册通知，是否释放周边网元。取值为：0 - 否；1 - 是；默认否。参数620：该软参用于控制NAS未投递流程收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 并行处理；1 - 有MM层消息未投递时缓存处理；2 - 缓存处理；默认有MM层消息未投递时缓存处理。参数621：该软参用于控制SourceAMF收到N2InfoNotify前又收到UEContextReleaseRequest是否需要处理N2释放流程。取值为：0 - 否；1 - 是；默认是。参数622：该软参用于控制切换与其它流程冲突时是否强制将用户上下文同步给cache和CDB。取值为：0 - 否；1 - 是；默认否。参数623：该软参用于AMF进行PCF发现时，是否仅依据UE策略配置开关来决策是否要发现PCF UE策略服务。取值为：0 - 否；1 - 是；默认否。参数624：该软参用于控制5G内切换新局AMF或者互操作切换5G AMF在预处理阶段被流程冲突后是否强制删除PDU上下文。取值为：0 - 否；1 - 是；默认是。参数625：该软参用于控制业务请求过程中，ISMF插入、改变是否向LIG发送消息。取值为：0 - 否；1 - 是；默认否。参数626：该软参用于控制NRF注册或者更新时Service是否支持携带interPlmnFqdn参数。取值为：0 - 否；1 - 是；默认否。参数627：该软参用于控制局间初始UE消息注册请求完整性保护检查通过时，是否通过Namf_Communication_UEContextTransfer请求消息向老局AMF获取用户上下文。取值为：0 - 否；1 - 是；默认否。参数628：该软参用于控制在注册与签约变更流程中，当会话切片不在AllowedNssai中时，是否需要删除不在AllowedNssai中的会话或重建在AllowedNssai中的会话。取值为：0 - 否；1 - 是；默认是。参数629：该软参用于控制amf重定向流程是否支持重选。取值为：0 - 否；1 - 是；默认否。参数630：500号软参取值为1，该软参用于控制N2释放和注册的冲突删除UDM未登记用户的处理方式。参数631：该软参用于控制PCF更新失败是否清除策略上下文并通知PCF。<
VALUE|当前参数值|参数可选性: 任选参数类型: 数字|软件参数当前取值。
NAME|参数名称|参数可选性: 任选参数类型: 字符串参数范围: 0-180|软参的名称，代表每个软参的含义




命令举例 


`
设置Communication软件参数配置，软参索引为1，当前参数值为1。即针对网络侧触发的AN Release流程（参见TS 23502 "4.2.6 AN Release"章节），如果RAN在UE CONTEXT RELEASE COMPLETE消息中没有携带要去活N3隧道的PDU，AMF也会向SMF发送更新消息。
SET COMMU SOFTWARE PARAMETER:ID=1,VALUE=1
` 


## 查询Communication软件参数配置(SHOW COMMU SOFTWARE PARAMETER) 
## 查询Communication软件参数配置(SHOW COMMU SOFTWARE PARAMETER) 


功能说明 

该命令用于显示当前软件参数的设定值。 


注意事项 

无。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ID|软参索引|参数可选性: 任选参数类型: 数字|该配置用于设置communication服务内部的一些功能参数，主要针对非协议明确要求的、异常厂家IOT、自厂家优化的功能或实现。参数1：针对网络侧触发的AN Release流程（参见TS 23502 4.2.6 AN Release章节），如果RAN在UE CONTEXT RELEASE COMPLETE消息中没有携带要去活N3隧道的PDU，则AMF根据此参数控制是否向SMF发送更新消息。参数2：用于控制局间切换或局间registration时，old AMF是否将该用户的订阅信息传递给目标AMF 或 target AMF。默认开启。主要用于异常家对接，对对方AMF不支持此功能时可关闭。参数3：用于控制局间切换或局间registration时，new AMF或targetAMF要不要接纳old AMF传递的订阅信息。参数4：用于控制是否跟踪RAN局向消息。参数5：用于控制PDU建立过程中，AMF是否获取当前PDU对应的S-NSSAI所对应的切片实例NSI。参数7： 用户从5G切换到4G EPS之后，AMF通过本参数控制是否立即删除用户上下文。参数8： 通过动态命令触发向NRF注册时，通过本软参可控制AMF是否先利用FQDN向DNS查询NRF地址。参数9： 当NRF地址采用FQDN方式配置时，该参数用于控制在进行DNS查询时，优先通过本地Cache查询，还是优先通过DNS Server查询。0表示优先本地Cache查询。1表示优先DNS Server查询。参数10：该软参用于控制S-NAPTR RR的优先级是否遵从3GPP。默认是。参数11：该软参用于控制是否支持跟踪Nas Container。默认是。参数12：在NF订阅策略配置为支持续订阅的情况下，AMF根据该参数设置（单位为分钟），来控制在NF订阅有效期到达前，提前多少分钟进行续订阅。参数13：该软参用于控制是否支持无SUPI时缓存上报用户信令。默认否。参数14：该软参用于控制是否支持回收共享表。默认是。参数16：保留软参。参数17：该软参用于控制是否支持无ISDN时缓存上报用户信令 。默认否。参数18：保留软参。参数20：该软参用于控制5G到4G的移动注册过程中是否使用next uplink nas count生成映射KASME。默认否。参数21：该软参用于控制注册请求followon标记置位时是否通知基站建UE上下文。默认是。参数22：该软参用于控制是否携带PLMN-ID参数向UDM获取签约数据。默认是。参数23：该软参用于控制S1 mode to N1 mode NAS transparent container是否包含5G UE Security capability。默认是。参数27：该软参用于控制是否强制使用初始上下文建立下发注册接受。默认否。参数28：该软参用于控制SBI接口中gNBValue的字段格式。默认gNBValue。参数29：本软参用于控制在检测到主备NRF都断链后，AMF是否清空本地发现缓存。设置为1，表示清空。参数30：该软参用于控制是否支持上下文健康检查。默认是。参数31：该软参用于控制是否支持NGAP转发表的健康检查 。默认是。参数32：该软参用于控制Forward relocation request消息中的UE NR security capability IE的长度。默认否。参数33：该软参用于控制是否限制全0的routingId。默认否。参数34：该软参用于控制无N26情况下是否对向UDM订阅ue-context-in-smf上下文。默认是。参数35：该软参用于控制是否支持AS安全修改。默认是。参数36：该软参用于控制Registration(unt)携带Uplink data Status是否进行active up conection操作。默认是。参数37：该软参用于控制是否对UE的安全能力参数进行检默认为90：Payload not  forwarded信息。默认否。参数39：该软参用于控制是否将EPS映射安全上下文中的NAS COUNT设置为5G NAS COUNT。默认是。参数40：该软参用于控制业务请求流程是否分配GUTI。默认否。参数41：该软参用于控制是否在当前5G安全上下文下行NAS COUNT基础上设置下行NAS COUNT。默认是。参数42：该软参用于控制业务请求是否先触发初始上下文建立。默认是。参数43：该软参用于控制 AMF与MME之间消息中的FTEID是否使用N26 AMF GTP-C interface。默认否。参数44：保留软参。参数45：该软参用于控制AMF进行NF订阅时是否携带PLMN-ID参数。默认是。参数46：本软参用于控制业务是否开启偶联状态检测功能。设置为1，表示开启偶联状态检测。参数47：该软参用于控制是否默认UE支持NEA0算法。默认是。参数48：该软参用于控制是否默认UE支持NEA1算法。默认是。参数49：该软参用于控制是否默认UE支持NEA2算法。默认是。参数50：该软参用于控制是否默认UE支持NEA3算法。默认是。参数51：该软参用于控制是否默认UE支持NIA0算法。默认是。参数52：该软参用于控制是否默认UE支持NIA1算法。默认是。参数53：该软参用于控制是否默认UE支持NIA2算法。默认是。参数54：该软参用于控制是否默认UE支持NIA3算法。默认是。参数55：该软参用于控制用户发生鉴权拒绝时是否上报通信失败。默认是。参数56：该软参用于控制用户发生注册拒绝时是否上报通信失败。默认是。参数57：该软参用于控制用户发生业务请求拒绝时是否上报通信失败。默认是。参数58：该软参用于控制用户发起网络侧去注册时是否上报通信失败。默认是。参数59：该软参用于控制初始上下文建立失败时是否上报通信失败。默认是。参数60：该软参用于控制初始注册时是否强制向UDM进行注册。默认是。参数61：该软参用于控制初始注册时是否强制向UDM获取签约数据。默认否。参数62：该软参用于控制发送SmContextUpdateData消息激活用户面是否携带ueLocation字段。默认否。参数63：该软参用于控制RAN发起的N2释放流程N2 Release command携带的原因值。默认携带N2Release请求中的原因值。参数64：该软参用于控制收到initial ue message是否要检查偶联有效性。默认是。参数65：该软参用于控制initial ue message偶联有效性检查失败是否要abort偶联。默认否。参数66：该软参用于控制网络侧没有获取到用户上下文时是否向UE要SUCI。默认是。参数67：该软参用于控制收到UE-CONTEXT标记时是否下发init context setup request消息。默认是。参数68：该软参用于控制偶联状态检测失败时是否删除偶联信息。默认是。参数69：该软参用于控制收到偶联断链时是否删除偶联信息。默认是。参数70：该软参用于控制MME消息中的GW FQDN是否需要去除top前缀保存。默认否。参数72：该软参用于控制SBI接口中的Snssai是否包含sd。默认否。参数73：该软参用于控制NGAP接口中的Snssai是否包含sd。默认否。参数74：该软参用于控制PCF发现时是否携带PLMN信息。默认否。参数75：该软参用于控制局间上下文响应中是否携带UE无线能力参数。默认是。参数76：本软参用于控制SC在重启时是否从Communication服务的Special SC加载局向相关表数据，默认否。参数77：本软参用于控制偶联表记录丢失是否终止该偶联，默认是。参数78：本软参用于控制从SC上是否删除老化的局向相关表记录，默认否。参数79：本软参用于控制收到SIG的偶联退服是否检验FRT表，默认是。参数80：该软参用于控制连接类消息amfngapid异常时给RAN发送释放命令还是是Error Indication。默认发送Error Indication。参数81：保留软参。参数82：该软参用于控制HTTP头中的ContentType multipart/related是否修正为小写字母 。默认否。参数84：该软参用于控制NULL scheme SUCI是否需要转换为BCD码。默认否。参数85：该软参用于控制没有签约UE AMBR时AMF是否携带本局默认UE AMBR 给MME。默认是。参数86：该软参用于控制是否在注册更新流程时的注册拒绝消息中携带T3502。默认否。参数87：该软参用于控制SBI消息中的NAS IE编码格式。默认包含IEI和长度部分。参数88：该软参用于控制切换时没有非直传隧道信息是否在HANDOVER COMMAND中构造PDU Session Resource Handover List。默认否。参数89：该软参用于控制非漫游场景下进行其他网元NRF发现时是否携带target plmn list。默认否。参数90：该软参用于控制鉴权返回二次同步失败时是否给UE发送鉴权拒绝。默认是。参数91：本软参用于控制接收主动负载重平衡启动动态命令时，是否处理动态命令，默认否。参数92：本软参用于控制是否支持5G SA默开时的特定T3502定时器，如果该软参开启，系统在鉴权过程触发5G SA默开、签约数据触发5G SA默开时, 注册拒绝携带特定的T3502定时器给UE， 默认否。参数93：该软参用于控制是否在未做完保的注册拒绝消息中携带T3502，如果关闭，注册拒绝未做完保时，不携带T3502，默认否。参数94：该软参用于控制Xn切换失败是否保持connect态。默认否。参数95：该软参用于控制是否检查NRF返回的NFID是否有效。默认否。参数96：该软参用于控制SCTP没有和gNB关联时是否终止偶联。默认是。参数97：该软参用于控制gNB记录缺失时是否终止偶联。默认是。参数98：该软参用于控制是否订阅SMF选择签约数据改变，默认是。参数99：该软参用于控制是否支持上下文请求携带CIoT Optimizations Support Indication，默认否。参数100：该软参用于控制是否支持互操作创建会话中携带切片信息，默认否。参数101：该软参用于控制是否给PCF携带时区，默认是。参数102：该软参用于控制是否支持组合SUPI号段限制接入和TA限制接入。默认否。参数103：该软参用于控制当paging超时时，是否将用户设置为不可达，默认否。参数105：该软参用于控制注册流程是否支持提前下发初始上下文建立。默认否。参数106：该软参用于控制局内移动I-SMF会话创建请求是否携带smfUri，默认携带。参数107：该软参用于控制局间移动I-SMF会话创建请求是否携带smfUri，默认携带。参数108：该软参用于控制是否把7-5GS服务不允许计数归类为用户原因。默认否。参数109：该软参用于控制是否把15-该TA没有合适小区计数归类为用户原因。默认否。参数110：该软参用于控制是否把111-协议失败，未指定计数归类为用户原因。默认否。参数111：保留软参。参数112：该软参用于控制全量备份场景信令跟踪是否上报接管通知消息，默认不上报。参数113：该软参用于控制是否按NFID清除缓存，默认是。参数114：该软参用于控制当寻呼的失败次数达到此软参时（等于或者大于），那么之后的寻呼，如果仍然失败，则不再统计寻呼的性能统计（包括全局和基于TA）。参数115：该软参用于控制5GS到EPS的切换是否需要通知SMF释放非直传隧道，默认是。参数116：该软参用于控制强制向RAN传递TCE信息。默认是。参数117：该软参用于控制选择NSSF时，是否支持NF级别的重选。默认否。参数118：该软参用于控制选择AUSF/UDM时，是否支持NF级别的重选。默认否。参数119：该软参用于控制选择AMF/SMF/PCF/SMSF/GMLC/LMF时，是否支持NF级别的重选。默认否。参数120：该软参用于控制是否把27-N1模式不允许计数归类为用户原因。默认否。参数121：该软参用于控制对ho required没有携带的pdu是否在流程最后是否给smf发update，默认是。参数122：该软参用于控制是否将业务请求接收消息码流填入到PDUSessionResourceSetupList中。默认否。参数123：该软参用于控制是否支持NF不可达发现查询信令上报，默认不上报。参数124：该软参用于控制，在SMF触发的paging过程中收到SMF发起的N1N2Transfer req，两次N1N2Transfer PDUID不同时，是缓存新的N1N2Transfer req还是依据优先级采取替换或者拒绝的策略，默认依据优先级。参数125：该软参用于控制Forward Relocation Request消息是否携带C-MSISDN 。默认否。参数126：该参数用于控制在X2口上报消息中的ServiceAreaList信元是否使用TAIList的格式来编码，默认不使用。参数128：该软参用于控制是否将注册接受消息码流填入到PDUSessionResourceSetupList中。默认否。参数129：该软参用于控制是否将SDM订阅请求中的callback设置为v2版本。默认否。参数130：该软参用于控制AMBR从bps转化为kbps时的取整方式。默认向下取整。参数131：该软参用于控制新注册的用户与PCF交互失败后是否后续不再与PCF交互。默认否。参数132：该软参用于控制是否支持TaCache表的老化处理。默认否。参数133：该软参用于控制TaCache表的老化时长。默认24小时。参数134：该软参用于控制业务DSL定时器选择开关。默认业务定制定时器。参数135：该软参用于控制是否支持NAS重放保护。默认否。参数136：该软参用于控制老局注册更新流程中是否通知SMF去活用户面。默认否。参数137：该软参用于控制是否支持小型化NSSF功能。默认否。参数138：保留软参。参数139：该软参用于控制GUTI分配方式。默认固定索引方式。参数140：该软参用于控制AMF收到PCF的PRA订阅后是否立即上报。默认立即上报。参数141：该软参用于控制在跨AMF注册流程中收到目标AMF Namf_Communication_RegistrationStatusUpdate Request消息且transferStatus信元值为“NOT_TRANSFERRED“时，源AMF回复Namf_Communication_RegistrationStatusUpdate响应时，响应消息中的regStatusTransferComplete字段取值是否为false。默认为false。参数142：该软参用于判断故障或判断恢复时，UE策略服务是否参与判断。缺省同”UE策略服务不参与判断“。当向PCF获取AM和UE策略的策略配置为UE策略不支持PCF交互时，此软参不起作用。参数143：该软参用于支持互操作的终端选择到非融合PGW-C+SMF时，在相同DNN相同切片情况下，是否支持选择同一个SMF，取值为：0-不支持，1-支持；默认0-不支持。参数144：该软参用于控制在不同PLMN网络下，发现SMF时，携带requester-plmn-list是否从本局支持的PLMN配置中获取。开关默认为否，从用户所在TA中获取。开关打开后，从本局支持的PLMN配置中获取。取值为：0-否，1-是；默认0-否。参数145：该软参用于控制AMF是否上报4/5G combo信令，默认上报。参数146：该软参用于控制是否支持过滤表容量告警上报。默认过滤。参数147：该软参控制注册流程创建UE策略后是否释放N2连接。取值为：0-否，1-是；默认0-否。参数148：该软参控制在短消息激活时是否携带Timezone信息。取值为：0-否，1-是；默认1-是。参数149：该软参控制是否检查SMF请求消息的地址。取值为：0-否，1-是；默认0-否。参数150：该软参控制5到4的Attach过程是否兼容5GS_TO_EPS_MOBILITY 原因值。取值为：0-否，1-是；默认1-是。参数151：该软参控制AMF已经携带smsfid发现smsf时是否还携带supi发现smsf，是否携带supi发现smsf还受网管配置SET NRFDISCSMSFPARACFG控制。取值为：0-否，1-是；默认0-否。参数152：该软参用于控制是否在AMF发给UE的注册拒绝消息中携带reject NSSAI。参数153：该参数用于控制AMF是否下发Redirection for Voice EPS Fallback指示给RAN，用于后续EPS Fallback时，RAN侧判断是否可以回落。取值为：0-否，1-是；默认1-是。参数154：该软参控制状态外收到UDM的原因值为初始注册或注册区域变更的去注册通知是否删除UE上下文。取值为：0-否，1-是；默认1-是。参数155：该参数用于控制AMF是否支持动态偶联详细信息检查。取值为：0-否，1-是；默认0-否。参数156：该参数用于设置动态偶联一致性检查失败时处理策略。取值为：0-更新对端地址信息，1-终止偶联；默认0-更新对端地址信息。参数157：该软参用于业务请求过程中rrc重建场景是否激活原先激活态pdu。取值为：0-否，1-是；默认0-否。参数158：该软参用于从SMF检索上下文失败导致5GS到EPS切换失败的原因值。取值为：0-255；默认7。参数160：该软参用于控制ISSU升级时Communication虚机升级步长，默认为1。参数161：该软参用于控制无用户使用后UE无线能力记录的Cache老化时间，默认10分钟。参数162：该软参用于控制是否在收到UDM触发的去注册后，立即发送SDM 去订阅消息，默认为1。参数163：该软参用于控制在使用NRFClient模式时，当NRF更新流程失败，并且响应码不是主备不可用的响应码，此时是否触发NRF重新注册。配置为“是”，表示触发重新注册，默认为“是”。参数164：该软参用于设置携带了selectedDnn参数时，selMode参数的携带策略。参数165：该软参用于控制UE-AMBR传递优化。默认优化。参数166：该软参用于控制5G切换4G时是否优选本合设局MME，默认为1。参数168：该软参用于控制是否支持性能统计定时上报，默认为支持。参数169：该软参用于控制注册拒绝消息中携带Rejected NSSAI的条件，当软参打开，仅nas原因值为62时携带；当软参关闭，不看原因值，均可以携带，默认为打开。参数170：该软参用于控制非漫游用户的DNN OI中PLMN来源，默认为SUPI。参数171：该软参用于控制是否支持忽略SMC过程，默认不支持。参数172：该软参用于控制SMF容灾IMS会话释放原因值。参数173：该参数用于指定卸载过程中，AMF网络侧去注册用户后，等待用户触发初始注册请求的时间，默认10s。参数174：该参数用于控制多PDU并行激活时延时发现SMF的时长，默认0ms,不延时。参数175：该参数用于收到N1N2Transfer消息出areaOfValidity区域时回N1N2MessageTransferRspData中的原因值,默认ATTEMPTING_TO_REACH_UE。参数176：该参数用于控制收到 PDU SESSION RESOURCE MODIFY RESPONSE消息后是否在SmContextUpdateData中强制携带UserLocation，取值为：0-否，1-是；默认是。参数178：该软参用于控制当5GMM Cause为91时用以替换的值，默认91，不替换。参数179：该软参用于控制v2版本的UplinkSMS中是否支持imeisv，取值为：0-否，1-是；默认是。参数185：该软参用于控制SmContextCreateData结构中hSmfUri, smfUri, additionalHsmfUri, additionalSmfUri信元的URI模式，详细参见29.502 CR0321。早期协议定义有歧义，会导致AMF发送给SMF的URI格式为“{apiRoot}/nsmf-pdusession/v1/”或者“{apiRoot}/nsmf-pdusession/v1/pdu-sessions/”。协议标准通过29.502 CR0321进行澄清，要求为“{apiRoot}/nsmf-pdusession/v1/”，AMF使用软参控制以便兼容对接现网版本。取值为：0-API URI，1-Resource URI；默认API URI。参数187：该软参用于控制AMF本地决策Allowed NSSAI为空时是否直接拒绝UE接入；取值为：0-否，1-是；默认0-否。参数188：该软参用于控制AMF本地决策Allowed NSSAI为空时，如果直接拒绝UE接入，应该携带的限制接入原因值；默认值为62-No network slices available。参数189：该软参用于控制用户注册时AMF是否强制不获取用户签约切片信息；默认否。参数190：该软参用于控制是否禁止用户建立多个紧急PDU；取值为：0-否，1-是；默认0-否。参数192：该软参用于是否统计业务请求流程无失败原因计数器时的请求数，用于控制版本间KPI波动过大，取值为：0-否，1-是；默认是。参数193：该软参用于控制一条5G Backup Data Notification消息最多包含的用户群数。参数194：该软参用于控制UE请求的S-NSSAI不在允许切片中是否拒绝PDU建立，取值为：0-否，1-是；默认是。参数195：该软参用于控制UE安全能力校验失败时的拒绝原因值，取值为：3-非法UE，6-非法ME，7-5G服务不允许，23-UE安全能力不匹配；默认6-非法ME。参数196：该软参用于控制AMF局间传递是否携带smssupport字段，取值为：0-否，1-是；默认否。参数197：该软参用于控制PCF UE策略创建请求消息是否携带有效的SupportedFeatures，取值为：0-否，1-是；默认否。参数198：该软参用于控制移动性流程是否支持基于preferred-locality发现I-SMF/V-SMF。参数199：该软参用于控制N11接口消息中servingNetwork的填写方式，取值为：0-TA中的PLMN；1-本局配置PLMN；默认0。参数201：该软参用于控制业务请求中AMF因底层链路问题向SMF发送失败时是否删除会话信息。默认是。参数202：该软参用于控制业务请求中与SMF交互无响应时是否删除会话信息。默认否。参数203：保留软参。参数204：保留软参。参数205：该软参用于控制Xn切换I-SMF插入发送SmContextCreateData是否携带AsmfId，默认否。参数206：是否限制NGAP BitRate IE值的大小。默认否。参数207：保留软参。参数208：保留软参。参数209：该软参用于控制收到基站NG Setup时检查所支持TA列表的策略。默认使用策略1。参数210：该软参用于控制SBI消息中Userlocation IE的timestamp格式。默认UTC时间。参数211：该参数用于控制移动性或切换流程I-SMF插入改变时是否携带SNSSAI给SMF，默认携带。参数212：该参数用于控制在非漫游场景下进行其他网元NRF发现的时候，是否携带requester plmn list。参数213：该参数用于控制在空闲态4到5注册更新时是否忽略到UDM获取切片及切片选择过程。参数214：该软参用于控制AMF内N2切换是否携带UE Time Zone给SMF。默认否。参数215：该软参用于控制AMF间N2切换是否携带UE Time Zone给SMF。默认否。参数216：该软参用于控制非Special SC在NRF发现后是否支持订阅。默认是。参数218：该软参用于流程冲突处理是否校验用户合法性。默认否。参数219：该软参用于控制限制接入带counter的SUPI号段优先。软参开启时，如果SUPI号段配置在SUPI号段接入限制中，且counter配置不为0，就以该配置数据为准。默认不开启。参数220：该软参用于控制当用户位置有效时是否在SmContextUpdateData中强制携带UserLocation，默认开启。参数222：该软参用于控制对于不在切换列表中的PDU是否去除UeContextCreateData消息中的N2SmInformation。参数223：该软参用于控制注册位置改变时是否通知SMF。参数224：该软参用于控制业务请求位置改变时是否通知SMF。参数225：保留软参。参数226：该软参用于控制是否支持回收异常信令管控表。参数227：保留软参。参数230：保留软参。参数232：该软参用于控制注册下发注册接受后被流程冲突抢占时是否强制同步用户上下文给cache/CDB。默认强制同步。参数234：该软参用于控制释放内部索引资源的阈值。参数235：该软参用于控制内部资源老化回收时长。参数238：保留软参。参数245：该参数用于控制NRFClient在处理UDM/AUSF/PCF的发现响应时，若对于NFProfile中携带号段小于软参设置值，则不进行发现缓存。默认值为2。参数246：该参数用于控制NRFClient在发现缓存老化时间的散列总时长，0默认为散列总时长为100秒，30~600为正常散列总时长，其他值认为不启用该功能。参数247：该参数用于控制重新GUTI分配结束后，是否在注册上下文中保留MTMSI资源已经被其他用户占用的老GUTI。默认不保留直接覆盖。参数248：该参数用于控制UDM/AUSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数251：该参数用于控制在NRF发现后触发NF状态订阅时，是否同时考虑采用IPv4及IPv6地址组成的nfStatusNotificationUri来查询当前是否存在对应的订阅记录，如果存在则不发起订阅。默认同时考虑。参数252：该参数用于控制在收到SMF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数253：该参数用于控制SMF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数254：该参数用于控制在收到PCF/SMSF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数255：该参数用于控制PCF/SMSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数256：该参数用于控制非UDM/AUSF/SMF/PCF/SMSF类型的其他NF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数257：该参数用于控制UDM/AUSF状态由不可用变为可用，并且按NFId触发续缓存时，是否根据缓存信息中识别出的同组UDM/AUSF信息，按NF组进行续缓存。参数258：该参数用于控制NRFClient在处理发现响应时，针对同一个NF号段相同时，是否展开号码树。参数259：该参数用于控制根据指定UDM/AUSF的NFId，进行关联同组其他NFId信息查询的方式，采用优先匹配或全表匹配。参数260：该参数用于控制在业务请求流程过程中是否并发处理initial context setup fail response。默认否。如果不并发处理，则会采用丢弃的处理策略。参数262：该参数用于控制在SMF通过N1N2Transfer请求发起的paging流程过程中，AMF又收到相同PDUID的N1N2Transfer请求，是否给SMF发送N1N2Transfer Fail Notify，取值为：0-否，1-是；默认否。参数269：该参数用于控制上行透传过程中收到N2释放的是否替换当前流程，取值为：0-否，1-是；默认否。参数270：该软参用于控制业务请求流程中ISMF删除或改变时收到SMF成功响应但未携带N2SmInfo是否通知ISMF释放。取值为：0 - 否；1 - 是； 默认是。参数272：该软参用于控制UDP截断转TCP场景下DNS性能统计是否统计查询尝试次数。取值为：0 - 否；1 - 是； 默认否。参数273：该软参用于控制局内切换收到Handover Notify是否更新sctp id。取值为：0 - 否；1 - 是； 默认否。参数274：该软参用于控制流程冲突对于未切换的PDU是否需要忽略通知SMF切换取消。取值为：0 - 否；1 - 是； 默认否。参数275：该软参用于控制是否优化处理局间切换时UeContextCreatedData消息的location字段。取值为：0 - 否；1 - 是； 默认否。参数276：该软参用于控制PDU会话建立流程等待N1N2Transfer消息超时的处理策略取值为：0 - 通知SMF和UE；1 - 仅通知SMF；2 - 仅通知UE；3 - 不通知SMF和UE； 默认通知SMF和UE。参数278：该软参用于控制发送NRF发现请求时选择SBIGW SC的方式。参数279：278号软参为1时，该软参用于控制最大可以使用的SBIGW SC数。参数285：该软参用于控制NFProfile中IP地址对应的端口使用默认端口还是服务对应端口 。取值为：0 - 使用服务对应端口；1 - 使用默认端口； 默认使用服务对应端口。参数287：该软参用于控制连接态收到N1N2Transfer消息不携带areaOfValidity是否丢弃消息中的N2信息，取值为：0-否，1-是；默认否。参数289：该软参用于控制收到N1N2Transfer消息出areaOfValidity区域时是否把N2 SM information投递给RAN，取值为：0-否，1-是；默认否。参数291：该软参用于控制当SMF故障时AMF扫描用户删除会话，用户连接态时是否分别通知UE和基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数292：该软参用于控制N1N2Transfer流程等待SMF更新响应时收到高优先级的消息是否直接替换，取值为：0-否，1-是；默认是。参数293：该软参用于控制收到PATH SWITCH REQUEST消息是否检查安全上下文，取值为：0-否，1-是；默认是。参数348：该软参用于控制AS检查失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数349：该软参用于控制NGAP连接一致性校验失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数352：该软参用于控制当收到SMF的创建响应找不到会话上下文时是否给SMF发送释放请求消息。取值为：0 - 否；1 - 是；默认否。参数355：该软参用于控制融合局AMF所有本局配置的GUAMI均不可用下发AMF Status Indication消息时，是否在Unavailable GUAMI List中携带GUMMEI映射的GUAMI。默认不携带。参数401：该软参用于控制AMF发送的NRF注册或更新请求携带的taiList的最大个数，修改软参值不会触发NRF更新。默认为512。参数402：该软参用于控制AMF发送的NRF注册或更新请求携带的taiRangeList的最大个数，修改软参值不会触发NRF更新。默认为12。参数403：该软参用于控制AMF发送的NRF注册或更新请求中携带的每个PLMN下tacRange最大个数，修改软参值不会触发NRF更新。默认为2048。参数404：该软参用于控制AMF发送的NRF注册或更新请求中携带的所有PLMN下总的tacRange最大个数，修改软参值不会触发NRF更新。默认为20000。参数406：该软参用于控制同步备份表异常挂死回收时长即当该用户的注册上下文不存在时，此上下文最长存在时长,单位分钟。默认为120分钟。参数407：该软参用于控制guti重分配后是否通知基站。参数408：该软参用于控制AMF发送的NRF注册或更新请求中是否携带n2InterfaceAmfInfo参数：0-否，1-是；默认否，修改软参值不会触发NRF更新。参数410：该软参用于控制4到5注册流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数411：该软参用于控制局内注册更新流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数412：该软参用于控制在X1口获取用户信息消息中的AMF上报信息是否强制携带上次使用的EPS PLMN标识。默认不强制携带，即参数可选。参数413：该软参用于控制初始注册结束是否强制保留N2连接。0-否，1-是；默认否。参数414：该软参用于控制4到5移动性注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数415：该软参用于控制5G系统内注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数416：该软参用于控制局内注册更新流程AMF是否向UDM注册。0-否，1-是；默认否。参数418：该软参用于控制发生guti冲突时是否purge老用户。0-否，1-是；默认否。参数419：该软参用于控制AMF收到RAN发送的Initial Ue Message消息时，AMF是否要检查局向TA表。0-否，1-是；默认是。参数420：该软参用于控制当gNB局向的TA记录丢失时，是否终止该gNB局向关联的所有SCTP偶联。0-否，1-是；默认是。参数421：该软参用于控制gNB局向表和gNB局向TA表异常挂死回收时长，单位分钟。默认为60分钟。参数422：该软参用于控制当发生guti冲突时是否放弃新用户流程。0-否，1-是；默认否。参数423：发生guti冲突且需要放弃新用户流程时的失败原因。默认为111。参数424：该软参用于控制是否启用SBI发送保序，中移路由测试的模式开启时该软参需要关闭。0-否，1-是；默认是。参数425：该软参用于控制SBI发送保序间隔。默认5秒。参数426：该软参用于控制AMF发送的NRF注册或更新请求携带的guami的最大个数，修改软参值不会触发NRF更新。默认为16。参数427：该软参用于控制AMF发送的NRF注册或更新请求携带的plmn-id的最大个数，修改软参值不会触发NRF更新。默认为32。参数430：该软参用于控制IP地址细分导致切换失败后是否释放N2连接。0-否，1-是；默认否。参数431：该软参用于控制注册更新或者切入流程，发生SUPI冲突查询到残留用户上下文时，是否需要通知I/V-SMF释放会话。默认需要通知。参数432：该软参用于控制用户信息入库失败时是否清除用户。默认为是。参数433：该软参用于控制用户信息入库失败时是否立即通知UE。默认为是。参数434：该软参用于控制二次鉴权routingId不变时重新发现AUSF。0-否，1-是；默认否。参数435：该软参用于控制同一流程中支持的最大鉴权次数。默认为3。参数436：该软参用于控制局内切换过程中收到上行的SM、SMS、LCS等消息时的处理方式。默认为2，即预处理阶段并行处理，执行阶段缓存处理。参数437：该软参用于控制AMF是否支持EPS回落增强功能。0-否，1-是；默认否。参数438：该软参用于控制AMF保持用户EPS回落状态时长。默认6秒。该参数仅在“AMF支持EPS回落增强”开启后有效。参数441：该软参用于控制是否删除不属于本SC管理的用户上下文。0-否，1-是；默认是。该参数仅在“是否支持上下文健康检查”开启后有效。参数443：该软参用于控制是否优化PDU级上行透传流程被冲突的处理机制.0-否，1-是；默认是。参数444：该软参用于控制紧急PDU建立失败是否使用配置原因值.0-否，1-是；默认是。参数445：紧急PDU建立失败的配置原因值；默认为90。参数446：该软参用于控制4到5注册是否使用从老局AMF获取到的SUPI。0-否，1-是；默认是。参数447：该软参用于控制AMF给UDM的Homogeneous Support of IMS Voice over PS Sessions指示是否考虑用户签约、漫游协议、无线能力信息。0-否，1-是；默认是。参数448：AMF收到gNB发起的部分重启消息，若消息中仅包含RAN UE NGAP ID，则N2连接异常。该软参用于判断AMF是否支持gNB部分重启消息中包含异常的N2连接信息。参数449：在448号参数置为1时，为了防止仅包含RAN UE NGAP ID的部分重启消息过多，对AMF造成冲击，该软参用于控制AMF单位时间内处理此类异常的部分重启消息数目。参数450：在RAN重启过程中，RAN侧先释放根据某个RAN UE NGAP ID建立的N2连接，此时AMF侧仍然保持该连接。之后，RAN根据同样的RAN UE NGAP ID再次请求与AMF建立N2连接，AMF此时会检测到RAN UE NGAP ID冲突。该软参用于判断此时AMF是否启动优化处理。参数451：该软参用于控制移动性流程（如注册、业务请求）被只携带N1容器的N1N2 Msg Transfer消息冲突场景，AS安全没有建立时是否需要拒绝N1N2 Msg Transfer消息。默认不拒绝。参数452：该软参用于控制初始注册流程下发注册接受后被移动性注册流程冲突的场景，AMF是否拒绝移动性注册并携带隐式分离的原因值。默认不拒绝，AMF终止处理初始注册，正常处理移动性注册。参数454：该软参用于控制UDM清除AM签约数据时是否需要去注册用户。默认去注册用户。参数455：该软参用于控制EAP鉴权失败为MAC 失败、同步失败、非5G失败时是否需要发送鉴权拒绝。默认发送鉴权拒绝。参数456：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的流程冲突处理机制。默认开启优化。参数457：该软参用于控制局间注册老局流程资源保护定时器内被注册流程冲突的场景，如果注册请求携带的GUTI是本局分配的，是否释放局间注册老局流程用户的PDU会话资源。默认不释放，流程冲突处理会向SMF更新PDU会话。参数458：该软参用于控制是否在鉴权完成之前启动异常信令管控。0-否，1-是；默认是。参数461：保留软参461。参数462：该软参用于控制5GS到EPS的切换流程中是否限制未请求切换的PDU建立非直传隧道。默认限制。参数463：该软参用于控制HANDOVER COMMAND消息是否限制携带未请求切换的PDU信息。默认限制。参数464：该软参用于控制PDU建立流程中，用户发生移动性流程时的冲突处理是否优化。默认是。参数465：该软参用于控制收到N2释放请求时是否检查amfN2apId，默认检查。参数468：该软参用于控制AMF通知基站释放老的N2连接时原因值，默认NAS “Normal release”。参数469：该软参用于控制5G到4G时AMF释放N2连接的原因值，默认NAS “Normal release”。参数470：该软参用于控制负荷重平衡时AMF主动释放N2连接的原因值，默认NAS “Normal release”。参数472：该软参用于控制是否删除不属于本SC管理的N11保序表记录。默认是。参数473：该软参用于控制A-SMF发现携带preferred-tai时是否忽略nrfSupportedFeatures。默认忽略。参数474：该软参用于控制用户在NAS拥塞控制backofftimer时间内再次发起上行业务时是否仍处理该消息。默认值否，不处理该上行消息。参数475：该软参用于控制是否删除不属于本SC管理的备份表记录。默认是。参数476：该软参用于控制Communication服务定时触发打包同步的时长。默认200ms。参数477：该软参用于控制Communication服务定量触发打包同步的用户个数。默认10个用户。参数478：该参数用于控制AMF是否开启动态偶联管理类消息打包功能。默认不开启。参数479：该软参用于控制用量上报表的老化时间，默认30秒。参数480：该软参用于控制NG Setup请求消息缓存时长，默认150毫秒。参数481：该软参用于控制AMF收到NG Setup请求消息后，是否释放该基站之前接入的用户N2连接，默认释放。该功能用于测试场景，商用场景不建议打开。参数482：该软参用于控制内部索引资源TEIDC老化回收的时长 ，默认2小时。参数483：该软参用于控制收到N2释放请求时检查n2apid失败是否发送Error Indication ，默认发送。参数484：该软参用于控制AMF是否支持连接态用户由于收到SMF的N1N2MessageTransfer触发I-SMF改变处理，默认是。参数486：该软参用于控制老局为初始注册态或attach时是否等待超时定时器，默认否。参数487：该软参用于控制从NRF接收PCF状态通知时，NF故障列表是否进行处理，默认是。参数488：该软参用于控制从NRF接收LMF状态通知时，NF故障列表是否进行处理，默认否。参数489：该软参用于控制局间附着和局间初始注册时，老局AMF等待UDM去注册通知消息的时长，默认10秒。参数491：该软参用于控制是否检查N2消息中的RAN UE NGAP ID，默认是。参数493：该软参用于控制Xn口切换被其它流程冲突掉是否通知源NG-RAN释放N2连接，默认否。参数494：该软参用于控制是否使用Forward Relocation Request消息中的Selected PLMN ID，默认是。参数496：该软参用于控制UE注册请求携带无效的注册类型时，AMF是否当做初始注册进行处理，默认是。参数497：该软参用于控制注册流程被N2释放流程冲突的场景，当N2释放流程被缓存时，注册流程是否继续投递下行消息，默认不投递。参数499：该软参用于控制5G到4G的切换流程被Context Request消息冲突替换时是否需要保留用户上下文，默认是。参数500：该软参用于控制优化N2释放和注册的冲突处理的方式，默认不优化。参数501：该软参用于控制AMF是否支持SUPI格式的正确性检查，SUPI中的MSIN每一位取值应为0-9的BCD码，不允许出现A-F。取值为：0-否，1-是；默认否。参数502：该软参用于控制PATH SWITCH REQUEST携带重复的PDU Session ID时AMF是否直接给RAN发送失败响应；默认否。参数503：该软参用于控制NGAP Class1消息无上下文是否释放连接，默认否。参数504：该软参用于控制NGAP Class2消息无上下文是否释放连接，默认否。参数505：该软参用于控制业务请求流程时是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认是。参数506：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数507：该软参用于控制网络侧去注册流程收到Error Indication是否终止通知UE。取值为：0-否，1-是；默认是。参数508：该软参用于控制是否支持对NGAP的连接进行一致性校验校验，默认是。参数509：该软参用于控制AMF是否收到成功响应后再标记UE-AMBR已发送，默认是。参数511：该软参用于控制连接态两条相同PDU的N1N2Transfer消息冲突时是否先回复失败响应，默认否。参数512：该软参用于控制收到PDU资源修改或释放的N1N2Transfer消息时如果AS安全未建立是否尝试透传N1信息，默认是。参数513：该软参用于控制初始注册当UE指示不支持S1能力时是否清除S1能力信息，默认否。参数514：该软参用于控制注册流程被相同注册请求冲突时，AMF在丢弃重复注册请求的同时是否释放老连接并更新新的连接信息，默认是。参数515：该软参用于控制注册流程收到N2修改UE上下文失败响应导致流程失败的原因值。默认为9。参数516：该软参用于控制初始guti注册时完保失败且老用户处于连接态是否丢弃新的注册请求。默认为否。参数517：该软参用于控制是否维持老版本lastseen ta的设置。默认为否。参数518：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时两个N1N2Transfer请求都没携带ARP时，是否拒绝新来的N1N2Transfer请求。取值为：0-否，1-是；默认是参数519：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时新的N1N2Transfer请求优先级更高时，是否采用替换的策略。取值为：0-否，1-是；默认是参数520：该软参用于控制用量上报表记录的老化扫描个数。取值范围为：1-3000；默认500参数521：该软参用于控制AMF是否对UE携带的IMEi进行格式检查，IMEI必须为14或15位BCD码，不允许出现A-F。取值为：0-否，1-是；默认是。参数522：当NF进入故障列表及告警的时间较长时，业务负担增加。该软参用于判断是否对故障NF启用老化机制。对于启用老化机制的NF,当到达规定时间（即老化时间）时，它将从故障列表中删除并且恢复告警。参数523：当不可达NF发现成功，恢复正常状态后，该软参用于判断此时AMF是否通知SBIGW更新NF状态。参数524：当第522号参数设置为1后，即故障NF启用老化机制，该软参生效。该软参用于控制对故障列表中仅NRF检测的记录，AMF触发不可达周期性发现的时间门限。参数525：该软参用于控制对于紧急PDU是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认否。参数526：该软参用于控制信令管控表扫描速率。取值范围为：1-1000；默认50。参数527：该软参用于控制注册流程在和SMF交互前被N1N2 Message Transfer消息冲突，交互后针对未发生交互会话的N1N2 Message Transfer请求消息，是否继续缓存，默认是。参数529：该软参用于控制紧邻PLMN的TAC放在TAC-low-byte还是放在TAC-high-byte。取值为：0 - 紧邻PLMN的TAC放在TAC-high-byte；1 - 紧邻PLMN的TAC放在TAC-low-byte；默认紧邻PLMN的TAC放在TAC-high-byte。参数530：该软参用于判断是否支持gNB在给AMF发送NG SETUP消息中的UE Retention字段功能，从而保持用户的N2逻辑连接。参数531：该软参用于控制发现AMF非本PLMN时，是否携带target-plmn-list和requester-plmn-list参数给NRF。取值为：0-否，1-是；默认是。参数532：该软参用于控制注册流程中，当注册完成后收到PDU建立请求是否缓存。取值为：0-否，1-是；默认是。参数533：该软参用于控制空闲态5G到4G移动性流程中，AMF是否需要判断N26 license和开关。取值为：0-否，1-是；默认是。参数534：该软参用于控制Handover Notify之后收到目标基站的N2释放是否修正通知源基站N2释放的原因值。取值为：0-否，1-是；默认否。参数535：该软参用于控制不可达主动发现恢复后是否通知SBIGW。取值为：0-否，1-是；默认是。参数536：该软参用于控制AMF收到Initial UE的业务请求时是否拒绝缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数537：该软参用于控制在业务请求过程中，当AMF收到Update/Create SM Response时是否释放缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数540：该软参用于控制LIG触发批量撤控请求时，AMF扫描删除布控记录的速率。默认每100毫秒扫描100条布控记录。参数541：该软参用于控制是否丢弃在会话建立过程中收到的相同PDU Session ID的会话建立请求消息。取值为：0-否，1-是；默认是。参数542：该软参用于控制HR漫游用户发送SmContextCreateData消息时是否携带HsmfId。取值为：0 - 否；1 - 是； 默认否。参数543：该软参用于控制重复的PDU会话激活预处理失败是否需要通知SMF删除会话。取值为：0 - 否；1 - 是； 默认是。参数544：当基于PLMN的AMF支持的SNSSAI和AMF支持的SNSSAI发生连续批量的配置变更时，基站会触发大量配置更新流程，易造成业务载荷过量。本软件参数用于控制延时通知基站触发配置更新流程的时长。参数545：该软参用于控制4G到5G的切换流程中获取不到Allowed NSSAI是否使用PDU会话的SNSSAI替代。取值为：0 - 否；1 - 是； 默认是。参数546：在DNS查询支持TCP方式的情况下，该软件参数用于判断AMF是否对DNS TCP链路信息进行周期性检查，例如检查链路对应的SC状态是否有效、链路个数是否正确等。取值为：0 - 否；1 - 是； 默认是。参数547：该软参用于控制局间切换新局I-SMF选择失败导致对应PDU会话切换失败时，是否通知SMF释放。取值为：0 - 否；1 - 是； 默认否。参数548：使用fake DNN发现SMF时本地发现模板id。取值范围为0-65535； 默认0。参数550：该软参用于控制PLMN改变后是否重新获取切片签约数据。取值为：0 - 否；1 - 是； 默认否。参数551：该软参用于控制是否优化注册过程中等待N2释放响应过程中与去注册冲突。取值为：0 - 否；1 - 是； 默认是。参数553：该软参用于控制收到用户相关的ERROR INDICATION消息指示NGAPID错误时是否触发UE CONTEXT RELEASE COMMAND消息。取值为：0 - 否；1 - 是； 默认否。参数554：该软参用于控制是否支持在UDM订阅请求中携带plmnId。取值为：0 - 否；1 - 是； 默认是。参数555：该软参用于控制当两个带有相同NasPdu字段的Initial UE业务请求冲突时，是否采用replace的策略。取值为：0 - 否；1 - 是； 默认是。参数556：该软参用于控制RAN配置更新消息缓存时长，默认150毫秒。参数558：该软参用于控制当老的PDU已经去活时相同DNN的多PDU会话是否选择同一个A-SMF。取值为：0 - 否；1 - 是； 默认是。参数560：该软参用于控制连接态业务请求过程中SMF故障检测后释放会话时是否通知基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数562：该软参用于控制AMF是否记录PDU会话的用户面状态。取值为：0 - 否；1 - 是； 默认否。参数563：该软参用于控制连接态时MT-LR定位是否向基站发送Location Reporting Control消息。取值为：0 - 否；1 - 是； 默认是。参数564：该软参用于控制业务请求过程中是否缓存N2容器类型是PDU资源修改的N1N2Transfer请求。取值为：0 - 否；1 - 是； 默认是。参数565：该软参用于控制局间未切换会话I/V-SMF改变/删除时AMF是否通知source I/V-SMF释放。取值为：0 - 否；1 - 是； 默认否。参数566：该软参用于控制当上行initial UE消息过负荷丢弃时是否发送N2释放消息。取值为：0 - 否；1 - 是； 默认否。参数568：该软参用于控制是否在注册过程中并行处理NAS未投递指示消息。取值为：0 - 否；1 - 是； 默认是。参数569：该软参用于控制当N2释放流程指示当前UE正在EPS回落时，是否丢弃PDU重建消息。取值为：0 - 否；1 - 是； 默认是。参数570：该软参用于控制无UDSF全量备份接管场景，是否支持通过扫描的方式发送打包的ZTE接管通知消息。该软件参数值设置为0：不支持。该软件参数值设置为1：支持。默认支持。参数571：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式发送打包的ZTE接管通知消息后，等待响应的超时时长。取值范围为1-60，默认1秒。参数572：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式每线程每秒至多可以发送的打包的ZTE接管通知消息数量。取值范围为1-200，默认2包每秒。参数575：该软参用于控制Xn切换流程发送的SmContextUpdateData是否携带变化的epsInterworkingInd。取值为：0 - 否；1 - 是； 默认是。参数577：该软参用于控制业务请求等移动性流程中，当SMF故障且AMF本地无对应TA缓存时，是否进行SMF发现。取值为：0 - 不发现；1 - 发现；默认不发现。参数578：该软参用于控制注册流程和SMF交互后是否继续缓存冲突的无法识别SMF是否改变的N1N2 Message Transfer的PDU修改或释放。取值为：0 - 否；1 - 是； 默认是。参数579：该软参用于控制全量备份场景，本局AMF是否将备份AMF加入本地检测列表，并在接管用户时检查备份AMF状态。默认检查备份局状态。参数580：该软参用于控制全量备份场景，本局AMF通过无线侧消息接管用户，并检查到备份AMF状态正常时，上行消息处理的方式。默认按全量容灾方式处理。参数581：该软参用于控制全量备份场景，本局AMF通过非无线侧消息接管用户，并检查到备份AMF状态正常时，下行消息处理的方式。默认按部分容灾方式处理。参数582：该软参用于控制5GS到EPS的切换流程中是否检查UE的S1 mode能力。取值为：0 - 否；1 - 是； 默认是。参数583：该软参用于控制当AMF收到SMF的N1N2MessageTransfer消息触发I-SMF改变是否回失败响应消息。取值为：0 - 否；1 - 是； 默认是。参数585：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为漫游PDU会话携带hplmnSnssai 。取值为：0 - 否；1 - 是；默认否。参数588：该软参用于控制是否支持强制向UDM获取及订阅ue-context-in-smf上下文。取值为：0 - 否；1 - 是；默认否。参数590：该软参用于控制当4到5切换重定向，目标局和MME都支持双栈时，目标局优选IP类型。取值为：0 - IPv4；1 - IPv6；默认IPv4。参数591：该软参用于控制Xn切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同Xn切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数592：该软参用于控制AMF内N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF内N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数593：该软参用于控制AMF间N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF间N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数594：该软参用于控制EPS到5GS的N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同EPS到5GS的N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数596：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为HR漫游PDU会话携带DTSSA特性 。取值为：0 - 否；1 - 是；默认是。参数597：该软参用于控制切换过程中收到切换完成的更新响应后再收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同之前的处理；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认保持之前的处理。参数598：该软参用于控制是否优化老局流程与上行透传消息的冲突策略。取值为：0 - 否；1 - 是；默认否。参数600：该软参用于控制AMF处理偶联退服消息的最大速率 ，超过的偶联退服消息将被延迟处理。取值为：0-10000（个/秒）；默认0（个/秒），表示不控制。参数601：该软参用于控制AMF进行偶联状态检测的最大速率。取值为：1-2000（个/秒）；默认10（个/秒）。参数602：该软参用于控制AMF进行偶联状态检测的超时时长。取值为：1-10秒；默认3秒。参数603：该软参用于控制接管用户更新SMF失败是否释放会话。取值为：0 - 否；1 - 是；默认是。参数604：该软参用于控制透传PDU SESSION RESOURCE RELEASE RESPONSE给SMF时是否需要等相应消息。取值为：0 - 否；1 - 是；默认是。参数605：该软参用于控制DNS性能统计UDP响应报文过长场景是否统计到UDP响应消息被截断计数器中。取值为：0 - 否；1 - 是；默认否。参数606：该软参用于控制当收到SBI口的失败响应消息而进行Nas原因值映射，若应用错误向配置转换失败，是否尝试继续匹配。取值为：0 - 否；1 - 是；默认否。参数607：该软参用于控制局间注册和TAU流程中old AMF用量上报是否受开关控制。取值为：0 - 否；1 - 是；默认是。参数608：该软参用于控制局间切换发现TargetAMF时携带切片的方式是否需要根据目标TA的PLMN决策。取值为：0 - 否；1 - 是；默认否。参数609：该软参用于控制因ISMF发送SmContextCreateData时是否需要更新SmContextStatusUri中的syn。取值为：0 - 否；1 - 是；默认是。参数610：该软参用于控制切换流程被N2释放流程冲突时是否优化UEContextReleaseCommand消息中原因值。取值为：0 - 否；1 - 是；默认否。参数614：该软参用于控制过负荷时是否要上报信令跟踪。取值为：0 - 否；1 - 是；默认否。参数615：该软参用于控制AMF向SMSF发起激活短消息时，携带GUAMI的方式。取值为：0 - 携带服务GUAMI；1 - 携带AMF的GUAMI列表；默认携带服务GUAMI。参数616：该软参用于控制是否强制获取短消息签约。取值为：0 - 否；1 - 是；默认否。参数617：该软参用于控制是否强制订阅短消息签约。取值为：0 - 否；1 - 是；默认否。参数618：该软参用于控制AMF切换入局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数619：该软参用于控制AMF收到流程外的UDM去注册通知，是否释放周边网元。取值为：0 - 否；1 - 是；默认否。参数620：该软参用于控制NAS未投递流程收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 并行处理；1 - 有MM层消息未投递时缓存处理；2 - 缓存处理；默认有MM层消息未投递时缓存处理。参数621：该软参用于控制SourceAMF收到N2InfoNotify前又收到UEContextReleaseRequest是否需要处理N2释放流程。取值为：0 - 否；1 - 是；默认是。参数622：该软参用于控制切换与其它流程冲突时是否强制将用户上下文同步给cache和CDB。取值为：0 - 否；1 - 是；默认否。参数623：该软参用于AMF进行PCF发现时，是否仅依据UE策略配置开关来决策是否要发现PCF UE策略服务。取值为：0 - 否；1 - 是；默认否。参数624：该软参用于控制5G内切换新局AMF或者互操作切换5G AMF在预处理阶段被流程冲突后是否强制删除PDU上下文。取值为：0 - 否；1 - 是；默认是。参数625：该软参用于控制业务请求过程中，ISMF插入、改变是否向LIG发送消息。取值为：0 - 否；1 - 是；默认否。参数626：该软参用于控制NRF注册或者更新时Service是否支持携带interPlmnFqdn参数。取值为：0 - 否；1 - 是；默认否。参数627：该软参用于控制局间初始UE消息注册请求完整性保护检查通过时，是否通过Namf_Communication_UEContextTransfer请求消息向老局AMF获取用户上下文。取值为：0 - 否；1 - 是；默认否。参数628：该软参用于控制在注册与签约变更流程中，当会话切片不在AllowedNssai中时，是否需要删除不在AllowedNssai中的会话或重建在AllowedNssai中的会话。取值为：0 - 否；1 - 是；默认是。参数629：该软参用于控制amf重定向流程是否支持重选。取值为：0 - 否；1 - 是；默认否。参数630：500号软参取值为1，该软参用于控制N2释放和注册的冲突删除UDM未登记用户的处理方式。参数631：该软参用于控制PCF更新失败是否清除策略上下文并通知PCF。<




输出参数说明 


标识|名称|类型|说明
---|---|---|---
ID|软参索引|参数可选性: 任选参数类型: 数字|该配置用于设置communication服务内部的一些功能参数，主要针对非协议明确要求的、异常厂家IOT、自厂家优化的功能或实现。参数1：针对网络侧触发的AN Release流程（参见TS 23502 4.2.6 AN Release章节），如果RAN在UE CONTEXT RELEASE COMPLETE消息中没有携带要去活N3隧道的PDU，则AMF根据此参数控制是否向SMF发送更新消息。参数2：用于控制局间切换或局间registration时，old AMF是否将该用户的订阅信息传递给目标AMF 或 target AMF。默认开启。主要用于异常家对接，对对方AMF不支持此功能时可关闭。参数3：用于控制局间切换或局间registration时，new AMF或targetAMF要不要接纳old AMF传递的订阅信息。参数4：用于控制是否跟踪RAN局向消息。参数5：用于控制PDU建立过程中，AMF是否获取当前PDU对应的S-NSSAI所对应的切片实例NSI。参数7： 用户从5G切换到4G EPS之后，AMF通过本参数控制是否立即删除用户上下文。参数8： 通过动态命令触发向NRF注册时，通过本软参可控制AMF是否先利用FQDN向DNS查询NRF地址。参数9： 当NRF地址采用FQDN方式配置时，该参数用于控制在进行DNS查询时，优先通过本地Cache查询，还是优先通过DNS Server查询。0表示优先本地Cache查询。1表示优先DNS Server查询。参数10：该软参用于控制S-NAPTR RR的优先级是否遵从3GPP。默认是。参数11：该软参用于控制是否支持跟踪Nas Container。默认是。参数12：在NF订阅策略配置为支持续订阅的情况下，AMF根据该参数设置（单位为分钟），来控制在NF订阅有效期到达前，提前多少分钟进行续订阅。参数13：该软参用于控制是否支持无SUPI时缓存上报用户信令。默认否。参数14：该软参用于控制是否支持回收共享表。默认是。参数16：保留软参。参数17：该软参用于控制是否支持无ISDN时缓存上报用户信令 。默认否。参数18：保留软参。参数20：该软参用于控制5G到4G的移动注册过程中是否使用next uplink nas count生成映射KASME。默认否。参数21：该软参用于控制注册请求followon标记置位时是否通知基站建UE上下文。默认是。参数22：该软参用于控制是否携带PLMN-ID参数向UDM获取签约数据。默认是。参数23：该软参用于控制S1 mode to N1 mode NAS transparent container是否包含5G UE Security capability。默认是。参数27：该软参用于控制是否强制使用初始上下文建立下发注册接受。默认否。参数28：该软参用于控制SBI接口中gNBValue的字段格式。默认gNBValue。参数29：本软参用于控制在检测到主备NRF都断链后，AMF是否清空本地发现缓存。设置为1，表示清空。参数30：该软参用于控制是否支持上下文健康检查。默认是。参数31：该软参用于控制是否支持NGAP转发表的健康检查 。默认是。参数32：该软参用于控制Forward relocation request消息中的UE NR security capability IE的长度。默认否。参数33：该软参用于控制是否限制全0的routingId。默认否。参数34：该软参用于控制无N26情况下是否对向UDM订阅ue-context-in-smf上下文。默认是。参数35：该软参用于控制是否支持AS安全修改。默认是。参数36：该软参用于控制Registration(unt)携带Uplink data Status是否进行active up conection操作。默认是。参数37：该软参用于控制是否对UE的安全能力参数进行检默认为90：Payload not  forwarded信息。默认否。参数39：该软参用于控制是否将EPS映射安全上下文中的NAS COUNT设置为5G NAS COUNT。默认是。参数40：该软参用于控制业务请求流程是否分配GUTI。默认否。参数41：该软参用于控制是否在当前5G安全上下文下行NAS COUNT基础上设置下行NAS COUNT。默认是。参数42：该软参用于控制业务请求是否先触发初始上下文建立。默认是。参数43：该软参用于控制 AMF与MME之间消息中的FTEID是否使用N26 AMF GTP-C interface。默认否。参数44：保留软参。参数45：该软参用于控制AMF进行NF订阅时是否携带PLMN-ID参数。默认是。参数46：本软参用于控制业务是否开启偶联状态检测功能。设置为1，表示开启偶联状态检测。参数47：该软参用于控制是否默认UE支持NEA0算法。默认是。参数48：该软参用于控制是否默认UE支持NEA1算法。默认是。参数49：该软参用于控制是否默认UE支持NEA2算法。默认是。参数50：该软参用于控制是否默认UE支持NEA3算法。默认是。参数51：该软参用于控制是否默认UE支持NIA0算法。默认是。参数52：该软参用于控制是否默认UE支持NIA1算法。默认是。参数53：该软参用于控制是否默认UE支持NIA2算法。默认是。参数54：该软参用于控制是否默认UE支持NIA3算法。默认是。参数55：该软参用于控制用户发生鉴权拒绝时是否上报通信失败。默认是。参数56：该软参用于控制用户发生注册拒绝时是否上报通信失败。默认是。参数57：该软参用于控制用户发生业务请求拒绝时是否上报通信失败。默认是。参数58：该软参用于控制用户发起网络侧去注册时是否上报通信失败。默认是。参数59：该软参用于控制初始上下文建立失败时是否上报通信失败。默认是。参数60：该软参用于控制初始注册时是否强制向UDM进行注册。默认是。参数61：该软参用于控制初始注册时是否强制向UDM获取签约数据。默认否。参数62：该软参用于控制发送SmContextUpdateData消息激活用户面是否携带ueLocation字段。默认否。参数63：该软参用于控制RAN发起的N2释放流程N2 Release command携带的原因值。默认携带N2Release请求中的原因值。参数64：该软参用于控制收到initial ue message是否要检查偶联有效性。默认是。参数65：该软参用于控制initial ue message偶联有效性检查失败是否要abort偶联。默认否。参数66：该软参用于控制网络侧没有获取到用户上下文时是否向UE要SUCI。默认是。参数67：该软参用于控制收到UE-CONTEXT标记时是否下发init context setup request消息。默认是。参数68：该软参用于控制偶联状态检测失败时是否删除偶联信息。默认是。参数69：该软参用于控制收到偶联断链时是否删除偶联信息。默认是。参数70：该软参用于控制MME消息中的GW FQDN是否需要去除top前缀保存。默认否。参数72：该软参用于控制SBI接口中的Snssai是否包含sd。默认否。参数73：该软参用于控制NGAP接口中的Snssai是否包含sd。默认否。参数74：该软参用于控制PCF发现时是否携带PLMN信息。默认否。参数75：该软参用于控制局间上下文响应中是否携带UE无线能力参数。默认是。参数76：本软参用于控制SC在重启时是否从Communication服务的Special SC加载局向相关表数据，默认否。参数77：本软参用于控制偶联表记录丢失是否终止该偶联，默认是。参数78：本软参用于控制从SC上是否删除老化的局向相关表记录，默认否。参数79：本软参用于控制收到SIG的偶联退服是否检验FRT表，默认是。参数80：该软参用于控制连接类消息amfngapid异常时给RAN发送释放命令还是是Error Indication。默认发送Error Indication。参数81：保留软参。参数82：该软参用于控制HTTP头中的ContentType multipart/related是否修正为小写字母 。默认否。参数84：该软参用于控制NULL scheme SUCI是否需要转换为BCD码。默认否。参数85：该软参用于控制没有签约UE AMBR时AMF是否携带本局默认UE AMBR 给MME。默认是。参数86：该软参用于控制是否在注册更新流程时的注册拒绝消息中携带T3502。默认否。参数87：该软参用于控制SBI消息中的NAS IE编码格式。默认包含IEI和长度部分。参数88：该软参用于控制切换时没有非直传隧道信息是否在HANDOVER COMMAND中构造PDU Session Resource Handover List。默认否。参数89：该软参用于控制非漫游场景下进行其他网元NRF发现时是否携带target plmn list。默认否。参数90：该软参用于控制鉴权返回二次同步失败时是否给UE发送鉴权拒绝。默认是。参数91：本软参用于控制接收主动负载重平衡启动动态命令时，是否处理动态命令，默认否。参数92：本软参用于控制是否支持5G SA默开时的特定T3502定时器，如果该软参开启，系统在鉴权过程触发5G SA默开、签约数据触发5G SA默开时, 注册拒绝携带特定的T3502定时器给UE， 默认否。参数93：该软参用于控制是否在未做完保的注册拒绝消息中携带T3502，如果关闭，注册拒绝未做完保时，不携带T3502，默认否。参数94：该软参用于控制Xn切换失败是否保持connect态。默认否。参数95：该软参用于控制是否检查NRF返回的NFID是否有效。默认否。参数96：该软参用于控制SCTP没有和gNB关联时是否终止偶联。默认是。参数97：该软参用于控制gNB记录缺失时是否终止偶联。默认是。参数98：该软参用于控制是否订阅SMF选择签约数据改变，默认是。参数99：该软参用于控制是否支持上下文请求携带CIoT Optimizations Support Indication，默认否。参数100：该软参用于控制是否支持互操作创建会话中携带切片信息，默认否。参数101：该软参用于控制是否给PCF携带时区，默认是。参数102：该软参用于控制是否支持组合SUPI号段限制接入和TA限制接入。默认否。参数103：该软参用于控制当paging超时时，是否将用户设置为不可达，默认否。参数105：该软参用于控制注册流程是否支持提前下发初始上下文建立。默认否。参数106：该软参用于控制局内移动I-SMF会话创建请求是否携带smfUri，默认携带。参数107：该软参用于控制局间移动I-SMF会话创建请求是否携带smfUri，默认携带。参数108：该软参用于控制是否把7-5GS服务不允许计数归类为用户原因。默认否。参数109：该软参用于控制是否把15-该TA没有合适小区计数归类为用户原因。默认否。参数110：该软参用于控制是否把111-协议失败，未指定计数归类为用户原因。默认否。参数111：保留软参。参数112：该软参用于控制全量备份场景信令跟踪是否上报接管通知消息，默认不上报。参数113：该软参用于控制是否按NFID清除缓存，默认是。参数114：该软参用于控制当寻呼的失败次数达到此软参时（等于或者大于），那么之后的寻呼，如果仍然失败，则不再统计寻呼的性能统计（包括全局和基于TA）。参数115：该软参用于控制5GS到EPS的切换是否需要通知SMF释放非直传隧道，默认是。参数116：该软参用于控制强制向RAN传递TCE信息。默认是。参数117：该软参用于控制选择NSSF时，是否支持NF级别的重选。默认否。参数118：该软参用于控制选择AUSF/UDM时，是否支持NF级别的重选。默认否。参数119：该软参用于控制选择AMF/SMF/PCF/SMSF/GMLC/LMF时，是否支持NF级别的重选。默认否。参数120：该软参用于控制是否把27-N1模式不允许计数归类为用户原因。默认否。参数121：该软参用于控制对ho required没有携带的pdu是否在流程最后是否给smf发update，默认是。参数122：该软参用于控制是否将业务请求接收消息码流填入到PDUSessionResourceSetupList中。默认否。参数123：该软参用于控制是否支持NF不可达发现查询信令上报，默认不上报。参数124：该软参用于控制，在SMF触发的paging过程中收到SMF发起的N1N2Transfer req，两次N1N2Transfer PDUID不同时，是缓存新的N1N2Transfer req还是依据优先级采取替换或者拒绝的策略，默认依据优先级。参数125：该软参用于控制Forward Relocation Request消息是否携带C-MSISDN 。默认否。参数126：该参数用于控制在X2口上报消息中的ServiceAreaList信元是否使用TAIList的格式来编码，默认不使用。参数128：该软参用于控制是否将注册接受消息码流填入到PDUSessionResourceSetupList中。默认否。参数129：该软参用于控制是否将SDM订阅请求中的callback设置为v2版本。默认否。参数130：该软参用于控制AMBR从bps转化为kbps时的取整方式。默认向下取整。参数131：该软参用于控制新注册的用户与PCF交互失败后是否后续不再与PCF交互。默认否。参数132：该软参用于控制是否支持TaCache表的老化处理。默认否。参数133：该软参用于控制TaCache表的老化时长。默认24小时。参数134：该软参用于控制业务DSL定时器选择开关。默认业务定制定时器。参数135：该软参用于控制是否支持NAS重放保护。默认否。参数136：该软参用于控制老局注册更新流程中是否通知SMF去活用户面。默认否。参数137：该软参用于控制是否支持小型化NSSF功能。默认否。参数138：保留软参。参数139：该软参用于控制GUTI分配方式。默认固定索引方式。参数140：该软参用于控制AMF收到PCF的PRA订阅后是否立即上报。默认立即上报。参数141：该软参用于控制在跨AMF注册流程中收到目标AMF Namf_Communication_RegistrationStatusUpdate Request消息且transferStatus信元值为“NOT_TRANSFERRED“时，源AMF回复Namf_Communication_RegistrationStatusUpdate响应时，响应消息中的regStatusTransferComplete字段取值是否为false。默认为false。参数142：该软参用于判断故障或判断恢复时，UE策略服务是否参与判断。缺省同”UE策略服务不参与判断“。当向PCF获取AM和UE策略的策略配置为UE策略不支持PCF交互时，此软参不起作用。参数143：该软参用于支持互操作的终端选择到非融合PGW-C+SMF时，在相同DNN相同切片情况下，是否支持选择同一个SMF，取值为：0-不支持，1-支持；默认0-不支持。参数144：该软参用于控制在不同PLMN网络下，发现SMF时，携带requester-plmn-list是否从本局支持的PLMN配置中获取。开关默认为否，从用户所在TA中获取。开关打开后，从本局支持的PLMN配置中获取。取值为：0-否，1-是；默认0-否。参数145：该软参用于控制AMF是否上报4/5G combo信令，默认上报。参数146：该软参用于控制是否支持过滤表容量告警上报。默认过滤。参数147：该软参控制注册流程创建UE策略后是否释放N2连接。取值为：0-否，1-是；默认0-否。参数148：该软参控制在短消息激活时是否携带Timezone信息。取值为：0-否，1-是；默认1-是。参数149：该软参控制是否检查SMF请求消息的地址。取值为：0-否，1-是；默认0-否。参数150：该软参控制5到4的Attach过程是否兼容5GS_TO_EPS_MOBILITY 原因值。取值为：0-否，1-是；默认1-是。参数151：该软参控制AMF已经携带smsfid发现smsf时是否还携带supi发现smsf，是否携带supi发现smsf还受网管配置SET NRFDISCSMSFPARACFG控制。取值为：0-否，1-是；默认0-否。参数152：该软参用于控制是否在AMF发给UE的注册拒绝消息中携带reject NSSAI。参数153：该参数用于控制AMF是否下发Redirection for Voice EPS Fallback指示给RAN，用于后续EPS Fallback时，RAN侧判断是否可以回落。取值为：0-否，1-是；默认1-是。参数154：该软参控制状态外收到UDM的原因值为初始注册或注册区域变更的去注册通知是否删除UE上下文。取值为：0-否，1-是；默认1-是。参数155：该参数用于控制AMF是否支持动态偶联详细信息检查。取值为：0-否，1-是；默认0-否。参数156：该参数用于设置动态偶联一致性检查失败时处理策略。取值为：0-更新对端地址信息，1-终止偶联；默认0-更新对端地址信息。参数157：该软参用于业务请求过程中rrc重建场景是否激活原先激活态pdu。取值为：0-否，1-是；默认0-否。参数158：该软参用于从SMF检索上下文失败导致5GS到EPS切换失败的原因值。取值为：0-255；默认7。参数160：该软参用于控制ISSU升级时Communication虚机升级步长，默认为1。参数161：该软参用于控制无用户使用后UE无线能力记录的Cache老化时间，默认10分钟。参数162：该软参用于控制是否在收到UDM触发的去注册后，立即发送SDM 去订阅消息，默认为1。参数163：该软参用于控制在使用NRFClient模式时，当NRF更新流程失败，并且响应码不是主备不可用的响应码，此时是否触发NRF重新注册。配置为“是”，表示触发重新注册，默认为“是”。参数164：该软参用于设置携带了selectedDnn参数时，selMode参数的携带策略。参数165：该软参用于控制UE-AMBR传递优化。默认优化。参数166：该软参用于控制5G切换4G时是否优选本合设局MME，默认为1。参数168：该软参用于控制是否支持性能统计定时上报，默认为支持。参数169：该软参用于控制注册拒绝消息中携带Rejected NSSAI的条件，当软参打开，仅nas原因值为62时携带；当软参关闭，不看原因值，均可以携带，默认为打开。参数170：该软参用于控制非漫游用户的DNN OI中PLMN来源，默认为SUPI。参数171：该软参用于控制是否支持忽略SMC过程，默认不支持。参数172：该软参用于控制SMF容灾IMS会话释放原因值。参数173：该参数用于指定卸载过程中，AMF网络侧去注册用户后，等待用户触发初始注册请求的时间，默认10s。参数174：该参数用于控制多PDU并行激活时延时发现SMF的时长，默认0ms,不延时。参数175：该参数用于收到N1N2Transfer消息出areaOfValidity区域时回N1N2MessageTransferRspData中的原因值,默认ATTEMPTING_TO_REACH_UE。参数176：该参数用于控制收到 PDU SESSION RESOURCE MODIFY RESPONSE消息后是否在SmContextUpdateData中强制携带UserLocation，取值为：0-否，1-是；默认是。参数178：该软参用于控制当5GMM Cause为91时用以替换的值，默认91，不替换。参数179：该软参用于控制v2版本的UplinkSMS中是否支持imeisv，取值为：0-否，1-是；默认是。参数185：该软参用于控制SmContextCreateData结构中hSmfUri, smfUri, additionalHsmfUri, additionalSmfUri信元的URI模式，详细参见29.502 CR0321。早期协议定义有歧义，会导致AMF发送给SMF的URI格式为“{apiRoot}/nsmf-pdusession/v1/”或者“{apiRoot}/nsmf-pdusession/v1/pdu-sessions/”。协议标准通过29.502 CR0321进行澄清，要求为“{apiRoot}/nsmf-pdusession/v1/”，AMF使用软参控制以便兼容对接现网版本。取值为：0-API URI，1-Resource URI；默认API URI。参数187：该软参用于控制AMF本地决策Allowed NSSAI为空时是否直接拒绝UE接入；取值为：0-否，1-是；默认0-否。参数188：该软参用于控制AMF本地决策Allowed NSSAI为空时，如果直接拒绝UE接入，应该携带的限制接入原因值；默认值为62-No network slices available。参数189：该软参用于控制用户注册时AMF是否强制不获取用户签约切片信息；默认否。参数190：该软参用于控制是否禁止用户建立多个紧急PDU；取值为：0-否，1-是；默认0-否。参数192：该软参用于是否统计业务请求流程无失败原因计数器时的请求数，用于控制版本间KPI波动过大，取值为：0-否，1-是；默认是。参数193：该软参用于控制一条5G Backup Data Notification消息最多包含的用户群数。参数194：该软参用于控制UE请求的S-NSSAI不在允许切片中是否拒绝PDU建立，取值为：0-否，1-是；默认是。参数195：该软参用于控制UE安全能力校验失败时的拒绝原因值，取值为：3-非法UE，6-非法ME，7-5G服务不允许，23-UE安全能力不匹配；默认6-非法ME。参数196：该软参用于控制AMF局间传递是否携带smssupport字段，取值为：0-否，1-是；默认否。参数197：该软参用于控制PCF UE策略创建请求消息是否携带有效的SupportedFeatures，取值为：0-否，1-是；默认否。参数198：该软参用于控制移动性流程是否支持基于preferred-locality发现I-SMF/V-SMF。参数199：该软参用于控制N11接口消息中servingNetwork的填写方式，取值为：0-TA中的PLMN；1-本局配置PLMN；默认0。参数201：该软参用于控制业务请求中AMF因底层链路问题向SMF发送失败时是否删除会话信息。默认是。参数202：该软参用于控制业务请求中与SMF交互无响应时是否删除会话信息。默认否。参数203：保留软参。参数204：保留软参。参数205：该软参用于控制Xn切换I-SMF插入发送SmContextCreateData是否携带AsmfId，默认否。参数206：是否限制NGAP BitRate IE值的大小。默认否。参数207：保留软参。参数208：保留软参。参数209：该软参用于控制收到基站NG Setup时检查所支持TA列表的策略。默认使用策略1。参数210：该软参用于控制SBI消息中Userlocation IE的timestamp格式。默认UTC时间。参数211：该参数用于控制移动性或切换流程I-SMF插入改变时是否携带SNSSAI给SMF，默认携带。参数212：该参数用于控制在非漫游场景下进行其他网元NRF发现的时候，是否携带requester plmn list。参数213：该参数用于控制在空闲态4到5注册更新时是否忽略到UDM获取切片及切片选择过程。参数214：该软参用于控制AMF内N2切换是否携带UE Time Zone给SMF。默认否。参数215：该软参用于控制AMF间N2切换是否携带UE Time Zone给SMF。默认否。参数216：该软参用于控制非Special SC在NRF发现后是否支持订阅。默认是。参数218：该软参用于流程冲突处理是否校验用户合法性。默认否。参数219：该软参用于控制限制接入带counter的SUPI号段优先。软参开启时，如果SUPI号段配置在SUPI号段接入限制中，且counter配置不为0，就以该配置数据为准。默认不开启。参数220：该软参用于控制当用户位置有效时是否在SmContextUpdateData中强制携带UserLocation，默认开启。参数222：该软参用于控制对于不在切换列表中的PDU是否去除UeContextCreateData消息中的N2SmInformation。参数223：该软参用于控制注册位置改变时是否通知SMF。参数224：该软参用于控制业务请求位置改变时是否通知SMF。参数225：保留软参。参数226：该软参用于控制是否支持回收异常信令管控表。参数227：保留软参。参数230：保留软参。参数232：该软参用于控制注册下发注册接受后被流程冲突抢占时是否强制同步用户上下文给cache/CDB。默认强制同步。参数234：该软参用于控制释放内部索引资源的阈值。参数235：该软参用于控制内部资源老化回收时长。参数238：保留软参。参数245：该参数用于控制NRFClient在处理UDM/AUSF/PCF的发现响应时，若对于NFProfile中携带号段小于软参设置值，则不进行发现缓存。默认值为2。参数246：该参数用于控制NRFClient在发现缓存老化时间的散列总时长，0默认为散列总时长为100秒，30~600为正常散列总时长，其他值认为不启用该功能。参数247：该参数用于控制重新GUTI分配结束后，是否在注册上下文中保留MTMSI资源已经被其他用户占用的老GUTI。默认不保留直接覆盖。参数248：该参数用于控制UDM/AUSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数251：该参数用于控制在NRF发现后触发NF状态订阅时，是否同时考虑采用IPv4及IPv6地址组成的nfStatusNotificationUri来查询当前是否存在对应的订阅记录，如果存在则不发起订阅。默认同时考虑。参数252：该参数用于控制在收到SMF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数253：该参数用于控制SMF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数254：该参数用于控制在收到PCF/SMSF状态不可用的状态通知时，是否清除对应NF的发现缓存。参数255：该参数用于控制PCF/SMSF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数256：该参数用于控制非UDM/AUSF/SMF/PCF/SMSF类型的其他NF状态由不可用变为可用时，是按照NFId触发续缓存还是按照NFType触发续缓存。参数257：该参数用于控制UDM/AUSF状态由不可用变为可用，并且按NFId触发续缓存时，是否根据缓存信息中识别出的同组UDM/AUSF信息，按NF组进行续缓存。参数258：该参数用于控制NRFClient在处理发现响应时，针对同一个NF号段相同时，是否展开号码树。参数259：该参数用于控制根据指定UDM/AUSF的NFId，进行关联同组其他NFId信息查询的方式，采用优先匹配或全表匹配。参数260：该参数用于控制在业务请求流程过程中是否并发处理initial context setup fail response。默认否。如果不并发处理，则会采用丢弃的处理策略。参数262：该参数用于控制在SMF通过N1N2Transfer请求发起的paging流程过程中，AMF又收到相同PDUID的N1N2Transfer请求，是否给SMF发送N1N2Transfer Fail Notify，取值为：0-否，1-是；默认否。参数269：该参数用于控制上行透传过程中收到N2释放的是否替换当前流程，取值为：0-否，1-是；默认否。参数270：该软参用于控制业务请求流程中ISMF删除或改变时收到SMF成功响应但未携带N2SmInfo是否通知ISMF释放。取值为：0 - 否；1 - 是； 默认是。参数272：该软参用于控制UDP截断转TCP场景下DNS性能统计是否统计查询尝试次数。取值为：0 - 否；1 - 是； 默认否。参数273：该软参用于控制局内切换收到Handover Notify是否更新sctp id。取值为：0 - 否；1 - 是； 默认否。参数274：该软参用于控制流程冲突对于未切换的PDU是否需要忽略通知SMF切换取消。取值为：0 - 否；1 - 是； 默认否。参数275：该软参用于控制是否优化处理局间切换时UeContextCreatedData消息的location字段。取值为：0 - 否；1 - 是； 默认否。参数276：该软参用于控制PDU会话建立流程等待N1N2Transfer消息超时的处理策略取值为：0 - 通知SMF和UE；1 - 仅通知SMF；2 - 仅通知UE；3 - 不通知SMF和UE； 默认通知SMF和UE。参数278：该软参用于控制发送NRF发现请求时选择SBIGW SC的方式。参数279：278号软参为1时，该软参用于控制最大可以使用的SBIGW SC数。参数285：该软参用于控制NFProfile中IP地址对应的端口使用默认端口还是服务对应端口 。取值为：0 - 使用服务对应端口；1 - 使用默认端口； 默认使用服务对应端口。参数287：该软参用于控制连接态收到N1N2Transfer消息不携带areaOfValidity是否丢弃消息中的N2信息，取值为：0-否，1-是；默认否。参数289：该软参用于控制收到N1N2Transfer消息出areaOfValidity区域时是否把N2 SM information投递给RAN，取值为：0-否，1-是；默认否。参数291：该软参用于控制当SMF故障时AMF扫描用户删除会话，用户连接态时是否分别通知UE和基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数292：该软参用于控制N1N2Transfer流程等待SMF更新响应时收到高优先级的消息是否直接替换，取值为：0-否，1-是；默认是。参数293：该软参用于控制收到PATH SWITCH REQUEST消息是否检查安全上下文，取值为：0-否，1-是；默认是。参数348：该软参用于控制AS检查失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数349：该软参用于控制NGAP连接一致性校验失败是否将消息中的N2信息透传给SMF。取值为：0 - 否；1 - 是； 默认是。参数352：该软参用于控制当收到SMF的创建响应找不到会话上下文时是否给SMF发送释放请求消息。取值为：0 - 否；1 - 是；默认否。参数355：该软参用于控制融合局AMF所有本局配置的GUAMI均不可用下发AMF Status Indication消息时，是否在Unavailable GUAMI List中携带GUMMEI映射的GUAMI。默认不携带。参数401：该软参用于控制AMF发送的NRF注册或更新请求携带的taiList的最大个数，修改软参值不会触发NRF更新。默认为512。参数402：该软参用于控制AMF发送的NRF注册或更新请求携带的taiRangeList的最大个数，修改软参值不会触发NRF更新。默认为12。参数403：该软参用于控制AMF发送的NRF注册或更新请求中携带的每个PLMN下tacRange最大个数，修改软参值不会触发NRF更新。默认为2048。参数404：该软参用于控制AMF发送的NRF注册或更新请求中携带的所有PLMN下总的tacRange最大个数，修改软参值不会触发NRF更新。默认为20000。参数406：该软参用于控制同步备份表异常挂死回收时长即当该用户的注册上下文不存在时，此上下文最长存在时长,单位分钟。默认为120分钟。参数407：该软参用于控制guti重分配后是否通知基站。参数408：该软参用于控制AMF发送的NRF注册或更新请求中是否携带n2InterfaceAmfInfo参数：0-否，1-是；默认否，修改软参值不会触发NRF更新。参数410：该软参用于控制4到5注册流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数411：该软参用于控制局内注册更新流程AMF是否向UDM获取签约数据参数：0-否，1-是；默认否。参数412：该软参用于控制在X1口获取用户信息消息中的AMF上报信息是否强制携带上次使用的EPS PLMN标识。默认不强制携带，即参数可选。参数413：该软参用于控制初始注册结束是否强制保留N2连接。0-否，1-是；默认否。参数414：该软参用于控制4到5移动性注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数415：该软参用于控制5G系统内注册更新流程结束是否强制保留N2连接。0-否，1-是；默认否。参数416：该软参用于控制局内注册更新流程AMF是否向UDM注册。0-否，1-是；默认否。参数418：该软参用于控制发生guti冲突时是否purge老用户。0-否，1-是；默认否。参数419：该软参用于控制AMF收到RAN发送的Initial Ue Message消息时，AMF是否要检查局向TA表。0-否，1-是；默认是。参数420：该软参用于控制当gNB局向的TA记录丢失时，是否终止该gNB局向关联的所有SCTP偶联。0-否，1-是；默认是。参数421：该软参用于控制gNB局向表和gNB局向TA表异常挂死回收时长，单位分钟。默认为60分钟。参数422：该软参用于控制当发生guti冲突时是否放弃新用户流程。0-否，1-是；默认否。参数423：发生guti冲突且需要放弃新用户流程时的失败原因。默认为111。参数424：该软参用于控制是否启用SBI发送保序，中移路由测试的模式开启时该软参需要关闭。0-否，1-是；默认是。参数425：该软参用于控制SBI发送保序间隔。默认5秒。参数426：该软参用于控制AMF发送的NRF注册或更新请求携带的guami的最大个数，修改软参值不会触发NRF更新。默认为16。参数427：该软参用于控制AMF发送的NRF注册或更新请求携带的plmn-id的最大个数，修改软参值不会触发NRF更新。默认为32。参数430：该软参用于控制IP地址细分导致切换失败后是否释放N2连接。0-否，1-是；默认否。参数431：该软参用于控制注册更新或者切入流程，发生SUPI冲突查询到残留用户上下文时，是否需要通知I/V-SMF释放会话。默认需要通知。参数432：该软参用于控制用户信息入库失败时是否清除用户。默认为是。参数433：该软参用于控制用户信息入库失败时是否立即通知UE。默认为是。参数434：该软参用于控制二次鉴权routingId不变时重新发现AUSF。0-否，1-是；默认否。参数435：该软参用于控制同一流程中支持的最大鉴权次数。默认为3。参数436：该软参用于控制局内切换过程中收到上行的SM、SMS、LCS等消息时的处理方式。默认为2，即预处理阶段并行处理，执行阶段缓存处理。参数437：该软参用于控制AMF是否支持EPS回落增强功能。0-否，1-是；默认否。参数438：该软参用于控制AMF保持用户EPS回落状态时长。默认6秒。该参数仅在“AMF支持EPS回落增强”开启后有效。参数441：该软参用于控制是否删除不属于本SC管理的用户上下文。0-否，1-是；默认是。该参数仅在“是否支持上下文健康检查”开启后有效。参数443：该软参用于控制是否优化PDU级上行透传流程被冲突的处理机制.0-否，1-是；默认是。参数444：该软参用于控制紧急PDU建立失败是否使用配置原因值.0-否，1-是；默认是。参数445：紧急PDU建立失败的配置原因值；默认为90。参数446：该软参用于控制4到5注册是否使用从老局AMF获取到的SUPI。0-否，1-是；默认是。参数447：该软参用于控制AMF给UDM的Homogeneous Support of IMS Voice over PS Sessions指示是否考虑用户签约、漫游协议、无线能力信息。0-否，1-是；默认是。参数448：AMF收到gNB发起的部分重启消息，若消息中仅包含RAN UE NGAP ID，则N2连接异常。该软参用于判断AMF是否支持gNB部分重启消息中包含异常的N2连接信息。参数449：在448号参数置为1时，为了防止仅包含RAN UE NGAP ID的部分重启消息过多，对AMF造成冲击，该软参用于控制AMF单位时间内处理此类异常的部分重启消息数目。参数450：在RAN重启过程中，RAN侧先释放根据某个RAN UE NGAP ID建立的N2连接，此时AMF侧仍然保持该连接。之后，RAN根据同样的RAN UE NGAP ID再次请求与AMF建立N2连接，AMF此时会检测到RAN UE NGAP ID冲突。该软参用于判断此时AMF是否启动优化处理。参数451：该软参用于控制移动性流程（如注册、业务请求）被只携带N1容器的N1N2 Msg Transfer消息冲突场景，AS安全没有建立时是否需要拒绝N1N2 Msg Transfer消息。默认不拒绝。参数452：该软参用于控制初始注册流程下发注册接受后被移动性注册流程冲突的场景，AMF是否拒绝移动性注册并携带隐式分离的原因值。默认不拒绝，AMF终止处理初始注册，正常处理移动性注册。参数454：该软参用于控制UDM清除AM签约数据时是否需要去注册用户。默认去注册用户。参数455：该软参用于控制EAP鉴权失败为MAC 失败、同步失败、非5G失败时是否需要发送鉴权拒绝。默认发送鉴权拒绝。参数456：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的流程冲突处理机制。默认开启优化。参数457：该软参用于控制局间注册老局流程资源保护定时器内被注册流程冲突的场景，如果注册请求携带的GUTI是本局分配的，是否释放局间注册老局流程用户的PDU会话资源。默认不释放，流程冲突处理会向SMF更新PDU会话。参数458：该软参用于控制是否在鉴权完成之前启动异常信令管控。0-否，1-是；默认是。参数461：保留软参461。参数462：该软参用于控制5GS到EPS的切换流程中是否限制未请求切换的PDU建立非直传隧道。默认限制。参数463：该软参用于控制HANDOVER COMMAND消息是否限制携带未请求切换的PDU信息。默认限制。参数464：该软参用于控制PDU建立流程中，用户发生移动性流程时的冲突处理是否优化。默认是。参数465：该软参用于控制收到N2释放请求时是否检查amfN2apId，默认检查。参数468：该软参用于控制AMF通知基站释放老的N2连接时原因值，默认NAS “Normal release”。参数469：该软参用于控制5G到4G时AMF释放N2连接的原因值，默认NAS “Normal release”。参数470：该软参用于控制负荷重平衡时AMF主动释放N2连接的原因值，默认NAS “Normal release”。参数472：该软参用于控制是否删除不属于本SC管理的N11保序表记录。默认是。参数473：该软参用于控制A-SMF发现携带preferred-tai时是否忽略nrfSupportedFeatures。默认忽略。参数474：该软参用于控制用户在NAS拥塞控制backofftimer时间内再次发起上行业务时是否仍处理该消息。默认值否，不处理该上行消息。参数475：该软参用于控制是否删除不属于本SC管理的备份表记录。默认是。参数476：该软参用于控制Communication服务定时触发打包同步的时长。默认200ms。参数477：该软参用于控制Communication服务定量触发打包同步的用户个数。默认10个用户。参数478：该参数用于控制AMF是否开启动态偶联管理类消息打包功能。默认不开启。参数479：该软参用于控制用量上报表的老化时间，默认30秒。参数480：该软参用于控制NG Setup请求消息缓存时长，默认150毫秒。参数481：该软参用于控制AMF收到NG Setup请求消息后，是否释放该基站之前接入的用户N2连接，默认释放。该功能用于测试场景，商用场景不建议打开。参数482：该软参用于控制内部索引资源TEIDC老化回收的时长 ，默认2小时。参数483：该软参用于控制收到N2释放请求时检查n2apid失败是否发送Error Indication ，默认发送。参数484：该软参用于控制AMF是否支持连接态用户由于收到SMF的N1N2MessageTransfer触发I-SMF改变处理，默认是。参数486：该软参用于控制老局为初始注册态或attach时是否等待超时定时器，默认否。参数487：该软参用于控制从NRF接收PCF状态通知时，NF故障列表是否进行处理，默认是。参数488：该软参用于控制从NRF接收LMF状态通知时，NF故障列表是否进行处理，默认否。参数489：该软参用于控制局间附着和局间初始注册时，老局AMF等待UDM去注册通知消息的时长，默认10秒。参数491：该软参用于控制是否检查N2消息中的RAN UE NGAP ID，默认是。参数493：该软参用于控制Xn口切换被其它流程冲突掉是否通知源NG-RAN释放N2连接，默认否。参数494：该软参用于控制是否使用Forward Relocation Request消息中的Selected PLMN ID，默认是。参数496：该软参用于控制UE注册请求携带无效的注册类型时，AMF是否当做初始注册进行处理，默认是。参数497：该软参用于控制注册流程被N2释放流程冲突的场景，当N2释放流程被缓存时，注册流程是否继续投递下行消息，默认不投递。参数499：该软参用于控制5G到4G的切换流程被Context Request消息冲突替换时是否需要保留用户上下文，默认是。参数500：该软参用于控制优化N2释放和注册的冲突处理的方式，默认不优化。参数501：该软参用于控制AMF是否支持SUPI格式的正确性检查，SUPI中的MSIN每一位取值应为0-9的BCD码，不允许出现A-F。取值为：0-否，1-是；默认否。参数502：该软参用于控制PATH SWITCH REQUEST携带重复的PDU Session ID时AMF是否直接给RAN发送失败响应；默认否。参数503：该软参用于控制NGAP Class1消息无上下文是否释放连接，默认否。参数504：该软参用于控制NGAP Class2消息无上下文是否释放连接，默认否。参数505：该软参用于控制业务请求流程时是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认是。参数506：该软参用于控制AMF切换出局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数507：该软参用于控制网络侧去注册流程收到Error Indication是否终止通知UE。取值为：0-否，1-是；默认是。参数508：该软参用于控制是否支持对NGAP的连接进行一致性校验校验，默认是。参数509：该软参用于控制AMF是否收到成功响应后再标记UE-AMBR已发送，默认是。参数511：该软参用于控制连接态两条相同PDU的N1N2Transfer消息冲突时是否先回复失败响应，默认否。参数512：该软参用于控制收到PDU资源修改或释放的N1N2Transfer消息时如果AS安全未建立是否尝试透传N1信息，默认是。参数513：该软参用于控制初始注册当UE指示不支持S1能力时是否清除S1能力信息，默认否。参数514：该软参用于控制注册流程被相同注册请求冲突时，AMF在丢弃重复注册请求的同时是否释放老连接并更新新的连接信息，默认是。参数515：该软参用于控制注册流程收到N2修改UE上下文失败响应导致流程失败的原因值。默认为9。参数516：该软参用于控制初始guti注册时完保失败且老用户处于连接态是否丢弃新的注册请求。默认为否。参数517：该软参用于控制是否维持老版本lastseen ta的设置。默认为否。参数518：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时两个N1N2Transfer请求都没携带ARP时，是否拒绝新来的N1N2Transfer请求。取值为：0-否，1-是；默认是参数519：该软参用于控制当SMF发起的N1N2Transfer请求冲突另一个N1N2Transfer请求触发的paging，同时新的N1N2Transfer请求优先级更高时，是否采用替换的策略。取值为：0-否，1-是；默认是参数520：该软参用于控制用量上报表记录的老化扫描个数。取值范围为：1-3000；默认500参数521：该软参用于控制AMF是否对UE携带的IMEi进行格式检查，IMEI必须为14或15位BCD码，不允许出现A-F。取值为：0-否，1-是；默认是。参数522：当NF进入故障列表及告警的时间较长时，业务负担增加。该软参用于判断是否对故障NF启用老化机制。对于启用老化机制的NF,当到达规定时间（即老化时间）时，它将从故障列表中删除并且恢复告警。参数523：当不可达NF发现成功，恢复正常状态后，该软参用于判断此时AMF是否通知SBIGW更新NF状态。参数524：当第522号参数设置为1后，即故障NF启用老化机制，该软参生效。该软参用于控制对故障列表中仅NRF检测的记录，AMF触发不可达周期性发现的时间门限。参数525：该软参用于控制对于紧急PDU是否检查SMF上下文中字段的有效性。取值为：0-否，1-是；默认否。参数526：该软参用于控制信令管控表扫描速率。取值范围为：1-1000；默认50。参数527：该软参用于控制注册流程在和SMF交互前被N1N2 Message Transfer消息冲突，交互后针对未发生交互会话的N1N2 Message Transfer请求消息，是否继续缓存，默认是。参数529：该软参用于控制紧邻PLMN的TAC放在TAC-low-byte还是放在TAC-high-byte。取值为：0 - 紧邻PLMN的TAC放在TAC-high-byte；1 - 紧邻PLMN的TAC放在TAC-low-byte；默认紧邻PLMN的TAC放在TAC-high-byte。参数530：该软参用于判断是否支持gNB在给AMF发送NG SETUP消息中的UE Retention字段功能，从而保持用户的N2逻辑连接。参数531：该软参用于控制发现AMF非本PLMN时，是否携带target-plmn-list和requester-plmn-list参数给NRF。取值为：0-否，1-是；默认是。参数532：该软参用于控制注册流程中，当注册完成后收到PDU建立请求是否缓存。取值为：0-否，1-是；默认是。参数533：该软参用于控制空闲态5G到4G移动性流程中，AMF是否需要判断N26 license和开关。取值为：0-否，1-是；默认是。参数534：该软参用于控制Handover Notify之后收到目标基站的N2释放是否修正通知源基站N2释放的原因值。取值为：0-否，1-是；默认否。参数535：该软参用于控制不可达主动发现恢复后是否通知SBIGW。取值为：0-否，1-是；默认是。参数536：该软参用于控制AMF收到Initial UE的业务请求时是否拒绝缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数537：该软参用于控制在业务请求过程中，当AMF收到Update/Create SM Response时是否释放缓存中的N1N2Transfer Request消息。取值为：0-否，1-是；默认是。参数540：该软参用于控制LIG触发批量撤控请求时，AMF扫描删除布控记录的速率。默认每100毫秒扫描100条布控记录。参数541：该软参用于控制是否丢弃在会话建立过程中收到的相同PDU Session ID的会话建立请求消息。取值为：0-否，1-是；默认是。参数542：该软参用于控制HR漫游用户发送SmContextCreateData消息时是否携带HsmfId。取值为：0 - 否；1 - 是； 默认否。参数543：该软参用于控制重复的PDU会话激活预处理失败是否需要通知SMF删除会话。取值为：0 - 否；1 - 是； 默认是。参数544：当基于PLMN的AMF支持的SNSSAI和AMF支持的SNSSAI发生连续批量的配置变更时，基站会触发大量配置更新流程，易造成业务载荷过量。本软件参数用于控制延时通知基站触发配置更新流程的时长。参数545：该软参用于控制4G到5G的切换流程中获取不到Allowed NSSAI是否使用PDU会话的SNSSAI替代。取值为：0 - 否；1 - 是； 默认是。参数546：在DNS查询支持TCP方式的情况下，该软件参数用于判断AMF是否对DNS TCP链路信息进行周期性检查，例如检查链路对应的SC状态是否有效、链路个数是否正确等。取值为：0 - 否；1 - 是； 默认是。参数547：该软参用于控制局间切换新局I-SMF选择失败导致对应PDU会话切换失败时，是否通知SMF释放。取值为：0 - 否；1 - 是； 默认否。参数548：使用fake DNN发现SMF时本地发现模板id。取值范围为0-65535； 默认0。参数550：该软参用于控制PLMN改变后是否重新获取切片签约数据。取值为：0 - 否；1 - 是； 默认否。参数551：该软参用于控制是否优化注册过程中等待N2释放响应过程中与去注册冲突。取值为：0 - 否；1 - 是； 默认是。参数553：该软参用于控制收到用户相关的ERROR INDICATION消息指示NGAPID错误时是否触发UE CONTEXT RELEASE COMMAND消息。取值为：0 - 否；1 - 是； 默认否。参数554：该软参用于控制是否支持在UDM订阅请求中携带plmnId。取值为：0 - 否；1 - 是； 默认是。参数555：该软参用于控制当两个带有相同NasPdu字段的Initial UE业务请求冲突时，是否采用replace的策略。取值为：0 - 否；1 - 是； 默认是。参数556：该软参用于控制RAN配置更新消息缓存时长，默认150毫秒。参数558：该软参用于控制当老的PDU已经去活时相同DNN的多PDU会话是否选择同一个A-SMF。取值为：0 - 否；1 - 是； 默认是。参数560：该软参用于控制连接态业务请求过程中SMF故障检测后释放会话时是否通知基站PDU释放。取值为：0 - 否；1 - 是； 默认是。参数562：该软参用于控制AMF是否记录PDU会话的用户面状态。取值为：0 - 否；1 - 是； 默认否。参数563：该软参用于控制连接态时MT-LR定位是否向基站发送Location Reporting Control消息。取值为：0 - 否；1 - 是； 默认是。参数564：该软参用于控制业务请求过程中是否缓存N2容器类型是PDU资源修改的N1N2Transfer请求。取值为：0 - 否；1 - 是； 默认是。参数565：该软参用于控制局间未切换会话I/V-SMF改变/删除时AMF是否通知source I/V-SMF释放。取值为：0 - 否；1 - 是； 默认否。参数566：该软参用于控制当上行initial UE消息过负荷丢弃时是否发送N2释放消息。取值为：0 - 否；1 - 是； 默认否。参数568：该软参用于控制是否在注册过程中并行处理NAS未投递指示消息。取值为：0 - 否；1 - 是； 默认是。参数569：该软参用于控制当N2释放流程指示当前UE正在EPS回落时，是否丢弃PDU重建消息。取值为：0 - 否；1 - 是； 默认是。参数570：该软参用于控制无UDSF全量备份接管场景，是否支持通过扫描的方式发送打包的ZTE接管通知消息。该软件参数值设置为0：不支持。该软件参数值设置为1：支持。默认支持。参数571：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式发送打包的ZTE接管通知消息后，等待响应的超时时长。取值范围为1-60，默认1秒。参数572：该软参用于控制无UDSF全量备份接管场景，通过扫描的方式每线程每秒至多可以发送的打包的ZTE接管通知消息数量。取值范围为1-200，默认2包每秒。参数575：该软参用于控制Xn切换流程发送的SmContextUpdateData是否携带变化的epsInterworkingInd。取值为：0 - 否；1 - 是； 默认是。参数577：该软参用于控制业务请求等移动性流程中，当SMF故障且AMF本地无对应TA缓存时，是否进行SMF发现。取值为：0 - 不发现；1 - 发现；默认不发现。参数578：该软参用于控制注册流程和SMF交互后是否继续缓存冲突的无法识别SMF是否改变的N1N2 Message Transfer的PDU修改或释放。取值为：0 - 否；1 - 是； 默认是。参数579：该软参用于控制全量备份场景，本局AMF是否将备份AMF加入本地检测列表，并在接管用户时检查备份AMF状态。默认检查备份局状态。参数580：该软参用于控制全量备份场景，本局AMF通过无线侧消息接管用户，并检查到备份AMF状态正常时，上行消息处理的方式。默认按全量容灾方式处理。参数581：该软参用于控制全量备份场景，本局AMF通过非无线侧消息接管用户，并检查到备份AMF状态正常时，下行消息处理的方式。默认按部分容灾方式处理。参数582：该软参用于控制5GS到EPS的切换流程中是否检查UE的S1 mode能力。取值为：0 - 否；1 - 是； 默认是。参数583：该软参用于控制当AMF收到SMF的N1N2MessageTransfer消息触发I-SMF改变是否回失败响应消息。取值为：0 - 否；1 - 是； 默认是。参数585：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为漫游PDU会话携带hplmnSnssai 。取值为：0 - 否；1 - 是；默认否。参数588：该软参用于控制是否支持强制向UDM获取及订阅ue-context-in-smf上下文。取值为：0 - 否；1 - 是；默认否。参数590：该软参用于控制当4到5切换重定向，目标局和MME都支持双栈时，目标局优选IP类型。取值为：0 - IPv4；1 - IPv6；默认IPv4。参数591：该软参用于控制Xn切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同Xn切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数592：该软参用于控制AMF内N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF内N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数593：该软参用于控制AMF间N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同AMF间N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数594：该软参用于控制EPS到5GS的N2切换完成等注册更新时收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同EPS到5GS的N2切换；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认缓存处理。参数596：该软参用于控制AMF给SMF发送的SmContextCreateData中是否需要为HR漫游PDU会话携带DTSSA特性 。取值为：0 - 否；1 - 是；默认是。参数597：该软参用于控制切换过程中收到切换完成的更新响应后再收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 同之前的处理；1 - 拒绝处理；2 - 缓存处理；3 - 并行处理；默认保持之前的处理。参数598：该软参用于控制是否优化老局流程与上行透传消息的冲突策略。取值为：0 - 否；1 - 是；默认否。参数600：该软参用于控制AMF处理偶联退服消息的最大速率 ，超过的偶联退服消息将被延迟处理。取值为：0-10000（个/秒）；默认0（个/秒），表示不控制。参数601：该软参用于控制AMF进行偶联状态检测的最大速率。取值为：1-2000（个/秒）；默认10（个/秒）。参数602：该软参用于控制AMF进行偶联状态检测的超时时长。取值为：1-10秒；默认3秒。参数603：该软参用于控制接管用户更新SMF失败是否释放会话。取值为：0 - 否；1 - 是；默认是。参数604：该软参用于控制透传PDU SESSION RESOURCE RELEASE RESPONSE给SMF时是否需要等相应消息。取值为：0 - 否；1 - 是；默认是。参数605：该软参用于控制DNS性能统计UDP响应报文过长场景是否统计到UDP响应消息被截断计数器中。取值为：0 - 否；1 - 是；默认否。参数606：该软参用于控制当收到SBI口的失败响应消息而进行Nas原因值映射，若应用错误向配置转换失败，是否尝试继续匹配。取值为：0 - 否；1 - 是；默认否。参数607：该软参用于控制局间注册和TAU流程中old AMF用量上报是否受开关控制。取值为：0 - 否；1 - 是；默认是。参数608：该软参用于控制局间切换发现TargetAMF时携带切片的方式是否需要根据目标TA的PLMN决策。取值为：0 - 否；1 - 是；默认否。参数609：该软参用于控制因ISMF发送SmContextCreateData时是否需要更新SmContextStatusUri中的syn。取值为：0 - 否；1 - 是；默认是。参数610：该软参用于控制切换流程被N2释放流程冲突时是否优化UEContextReleaseCommand消息中原因值。取值为：0 - 否；1 - 是；默认否。参数614：该软参用于控制过负荷时是否要上报信令跟踪。取值为：0 - 否；1 - 是；默认否。参数615：该软参用于控制AMF向SMSF发起激活短消息时，携带GUAMI的方式。取值为：0 - 携带服务GUAMI；1 - 携带AMF的GUAMI列表；默认携带服务GUAMI。参数616：该软参用于控制是否强制获取短消息签约。取值为：0 - 否；1 - 是；默认否。参数617：该软参用于控制是否强制订阅短消息签约。取值为：0 - 否；1 - 是；默认否。参数618：该软参用于控制AMF切换入局时是否优化与注册更新或TAU的调度冲突处理机制。默认开启优化。参数619：该软参用于控制AMF收到流程外的UDM去注册通知，是否释放周边网元。取值为：0 - 否；1 - 是；默认否。参数620：该软参用于控制NAS未投递流程收到SMF的N1N2MessageTransfer消息处理策略。取值为：0 - 并行处理；1 - 有MM层消息未投递时缓存处理；2 - 缓存处理；默认有MM层消息未投递时缓存处理。参数621：该软参用于控制SourceAMF收到N2InfoNotify前又收到UEContextReleaseRequest是否需要处理N2释放流程。取值为：0 - 否；1 - 是；默认是。参数622：该软参用于控制切换与其它流程冲突时是否强制将用户上下文同步给cache和CDB。取值为：0 - 否；1 - 是；默认否。参数623：该软参用于AMF进行PCF发现时，是否仅依据UE策略配置开关来决策是否要发现PCF UE策略服务。取值为：0 - 否；1 - 是；默认否。参数624：该软参用于控制5G内切换新局AMF或者互操作切换5G AMF在预处理阶段被流程冲突后是否强制删除PDU上下文。取值为：0 - 否；1 - 是；默认是。参数625：该软参用于控制业务请求过程中，ISMF插入、改变是否向LIG发送消息。取值为：0 - 否；1 - 是；默认否。参数626：该软参用于控制NRF注册或者更新时Service是否支持携带interPlmnFqdn参数。取值为：0 - 否；1 - 是；默认否。参数627：该软参用于控制局间初始UE消息注册请求完整性保护检查通过时，是否通过Namf_Communication_UEContextTransfer请求消息向老局AMF获取用户上下文。取值为：0 - 否；1 - 是；默认否。参数628：该软参用于控制在注册与签约变更流程中，当会话切片不在AllowedNssai中时，是否需要删除不在AllowedNssai中的会话或重建在AllowedNssai中的会话。取值为：0 - 否；1 - 是；默认是。参数629：该软参用于控制amf重定向流程是否支持重选。取值为：0 - 否；1 - 是；默认否。参数630：500号软参取值为1，该软参用于控制N2释放和注册的冲突删除UDM未登记用户的处理方式。参数631：该软参用于控制PCF更新失败是否清除策略上下文并通知PCF。<
VALUE|当前参数值|参数可选性: 任选参数类型: 数字|软件参数当前取值。
DEFAULTVALUE|默认参数值|参数可选性: 任选参数类型: 数字|软件参数默认取值。
MINVALUE|参数最小值|参数可选性: 任选参数类型: 数字|软件参数最小值
MAXVALUE|参数最大值|参数可选性: 任选参数类型: 数字|软件参数最大值
NAME|参数名称|参数可选性: 任选参数类型: 字符串参数范围: 0-180|软参的名称，代表每个软参的含义
REMARK|备注|参数可选性: 任选参数类型: 字符串参数范围: 0-180|参数取值的具体含义介绍




命令举例 


`
查询软参索引为1的Communication软件参数配置数据。
SHOW COMMU SOFTWARE PARAMETER:

(No.1) : SHOW COMMU SOFTWARE PARAMETER:ID=1
-----------------Namf_Communication_0----------------
操作维护       软参索引 当前参数值 默认参数值 参数最小值 参数最大值 参数名称                                       备注           
----------------------------------------------------------------------------------------------------------------------------------
修改           1        1          1          0          1          UE Context Release流程不带PDUID是否需要更新SMF 0 - 否；1 - 是 
----------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-05-13 19:40:31 耗时: 0.129 秒

` 


# 一致性检查配置 
# 一致性检查配置 


背景知识 


中兴5GC AMF为了保证服务间数据一致性，内部实现用户数据定时一致性检查机制。 




功能说明 


本配置用于设置或修改数据一致性检查控制相关参数。 




子主题： 






## 修改数据一致性检查配置(SET DATACHECK) 
## 修改数据一致性检查配置(SET DATACHECK) 


功能说明 

该命令用于设置或修改数据一致性检查控制相关参数。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
scanRate|扫描速率(用户/秒)|参数可选性: 任选参数类型: 数字参数范围: 0-500默认值: 4|该参数用于设置一致性检查时，用户上下文的扫描速率，默认值为4（单位：用户/秒）。




命令举例 


`
设置数据一致性检查控制配置：扫描速率为4用户/秒。
SET DATACHECK:SCANRATE=4
` 


## 查询数据一致性检查配置(SHOW DATACHECK) 
## 查询数据一致性检查配置(SHOW DATACHECK) 


功能说明 

该命令用于查询数据一致性检查控制相关参数。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
scanRate|扫描速率(用户/秒)|参数可选性: 任选参数类型: 数字参数范围: 0-500默认值: 4|该参数用于设置一致性检查时，用户上下文的扫描速率，默认值为4（单位：用户/秒）。




命令举例 


`
查询数据一致性检查控制配置。 
SHOW DATACHECK:

(No.1) : SHOW DATACHECK:
-----------------Namf_Communication_0----------------
扫描速率(用户/秒)  
4         
记录数：1

` 


# 特定场景NAS原因配置 
# 特定场景NAS原因配置 


背景知识 


当AMF拒绝UE的请求时，可以下发NAS原因，UE根据NAS原因来进行后续行为。 

现网中，UE终端的种类繁多。对于UE下发的NAS原因，不同的UE终端可能会有不同的反应。在某些特定场景下，不同UE终端的反应差别可能更大。 

针对一些特定的场景，AMF提供了灵活的NAS原因配置。现网运行时，AMF可以根据现网对已有数据的统计来配置下发给UE的NAS原因值，从而更合理的引导UE的后续行为。 




功能说明 


该功能用于配置在一些特定场景下，AMF给UE发送的NAS原因值，以引导UE在这些特定场景下进行合理的后续行为。 




子主题： 






## 修改特定场景NAS原因配置(SET SPECIALNASCAUSECFG) 
## 修改特定场景NAS原因配置(SET SPECIALNASCAUSECFG) 


功能说明 

该命令用于配置在一些特定场景下，给UE发送的NAS原因值，以引导UE在这些特定场景下，进行合理的后续行为。 


注意事项 

给UE下发的原因值可以进行配置，但给所有UE下发的原因值都是统一的。 


输入参数说明 


标识|名称|类型|说明
---|---|---|---
situation|场景|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-100|该参数用于配置特定场景。有以下几种不同的场景：初始注册鉴权超时注册更新鉴权超时业务请求鉴权超时初始注册鉴权同步失败注册更新鉴权同步失败业务请求鉴权同步失败在AMF重分配注册流程中，等待Namf_Communication_N1MessageNotify响应失败在AMF重分配注册流程中，等待Namf_Communication_N1MessageNotify响应超时在Nnssf_NSSelection服务流程中，选择NSSF失败在Nnssf_NSSelection服务流程中，与NSSF交互失败场景一：向NSSF发送服务请求消息失败场景二：AMF反复重定向注册请求解码失败在AMF重分配注册流程中，发送Namf_Communication_N1MessageNotify消息失败非漫游用户在从Old AMF获取上下文失败时，发送给UE的拒绝原因值
NasMmCause|NAS移动性管理原因|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-200|该参数用于配置特定场景下，给UE发送的NAS原因值，以引导UE在这些特定场景下，进行合理的后续行为。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
修改场景为"INTREGAUTHTIMEOUT"时，AMF携带给UE的NAS Cause为"IMPLICITLYDEREG"。
SET SPECIALNASCAUSECFG:SITUATION="INTREGAUTHTIMEOUT",NASMMCAUSE="IMPLICITLYDEREG"
` 


## 查询特定场景NAS原因配置(SHOW SPECIALNASCAUSECFG) 
## 查询特定场景NAS原因配置(SHOW SPECIALNASCAUSECFG) 


功能说明 

该命令用于查询特定场景下，AMF发送给UE的NAS移动性管理原因值。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
situation|场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-100|该参数用于配置特定场景。有以下几种不同的场景：初始注册鉴权超时注册更新鉴权超时业务请求鉴权超时初始注册鉴权同步失败注册更新鉴权同步失败业务请求鉴权同步失败在AMF重分配注册流程中，等待Namf_Communication_N1MessageNotify响应失败在AMF重分配注册流程中，等待Namf_Communication_N1MessageNotify响应超时在Nnssf_NSSelection服务流程中，选择NSSF失败在Nnssf_NSSelection服务流程中，与NSSF交互失败场景一：向NSSF发送服务请求消息失败场景二：AMF反复重定向注册请求解码失败在AMF重分配注册流程中，发送Namf_Communication_N1MessageNotify消息失败非漫游用户在从Old AMF获取上下文失败时，发送给UE的拒绝原因值




输出参数说明 


标识|名称|类型|说明
---|---|---|---
situation|场景|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-100|该参数用于显示特定场景。有以下几种不同的场景：初始注册鉴权超时注册更新鉴权超时业务请求鉴权超时初始注册鉴权同步失败注册更新鉴权同步失败业务请求鉴权同步失败在AMF重分配注册流程中，等待Namf_Communication_N1MessageNotify响应失败在AMF重分配注册流程中，等待Namf_Communication_N1MessageNotify响应超时在Nnssf_NSSelection服务流程中，选择NSSF失败在Nnssf_NSSelection服务流程中，与NSSF交互失败场景一：向NSSF发送服务请求消息失败场景二：AMF反复重定向注册请求解码失败在AMF重分配注册流程中，发送Namf_Communication_N1MessageNotify消息失败非漫游用户在从Old AMF获取上下文失败时，发送给UE的拒绝原因值
NasMmCause|NAS移动性管理原因|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-200|该参数用于显示特定场景下，给UE发送的NAS原因值，以引导UE在这些特定场景下，进行合理的后续行为。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255|该参数用于性能统计时归类使用。




命令举例 


`
查询特定场景的NAS移动性管理原因值。 
SHOW SPECIALNASCAUSECFG:

 (No.1) : SHOW SPECIALNASCAUSECFG:SITUATION="INTREGAUTHTIMEOUT"
-----------------Namf_Communication_0_A----------------
场景                 NAS移动性管理原因                 计数归类 
初始注册鉴权超时     111 - Protocol error, unspecified 

记录数：1


` 


# gNB告警配置 
# gNB告警配置 


背景知识 


为了方便运维、监控gNB运行状态，AMF针对gNB发生某些事件时，会上报一些告警、通知。现网gNB数量庞大，AMF上报告警、通知需要考虑流控。现网还存在部分gNB，断链后长时间不恢复，AMF需要考虑老化恢复。所以，AMF提供了一些gNB告警相关的配置参数，现网运维人员，可以根据实际运行情况进行调整。 




功能说明 


本配置主要应用于是否上报相关通知及gNB断链告警长期无法恢复的场景。 




子主题： 






## gNB告警参数配置 
## gNB告警参数配置 


背景知识 


为了方便运维、监控gNB运行状态，AMF针对gNB发生某些事件时，会上报一些告警、通知。现网gNB数量庞大，AMF上报告警、通知需要考虑流控。现网还存在部分gNB，断链后长时间不恢复，AMF需要考虑老化恢复。所以，AMF提供了一些gNB告警相关的配置参数，现网运维人员，可以根据实际运行情况进行调整。 




功能说明 


本功能用于配置gNB告警参数，如是否上报偶联投入使用通知、是否上报偶联断链通知及gNB断链告警老化回收时长。 




子主题： 






### 修改gNB告警参数配置(SET GNB ALARMPARA) 
### 修改gNB告警参数配置(SET GNB ALARMPARA) 


功能说明 

该命令用于设置gNB告警参数配置，如是否上报偶联投入使用通知、是否上报偶联断链通知及gNB断链告警老化回收时长。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
ngaprptasisi|是否上报偶联投入使用通知|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否上报偶联投入使用通知，默认不上报。
ngaprptassoos|是否上报偶联断链通知|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否上报偶联断链通知，默认不上报。
gnbcallbackdura|gNB断链告警老化回收时长(小时)|参数可选性: 任选参数类型: 数字参数范围: 1-72默认值: 24|该参数用于设置gNB断链告警老化回收时长，取值范围：1-72小时，缺省为24小时。当gNB断链告警的持续时长超过配置的"gNB断链告警老化回收时长", AMF清除gNB断链告警。




命令举例 


`
设置gNB告警参数：不上报偶联投入使用通知，不上报偶联断链通知，gNB断链告警老化回收时长36小时。
SET GNB ALARMPARA:NGAPRPTASISI="NO",NGAPRPTASSOOS="NO",GNBCALLBACKDURA=36;
` 


### 查询gNB告警参数配置(SHOW GNB ALARMPARA) 
### 查询gNB告警参数配置(SHOW GNB ALARMPARA) 


功能说明 

该命令用于查询gNB告警参数配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
ngaprptasisi|是否上报偶联投入使用通知|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否上报偶联投入使用通知，默认不上报。
ngaprptassoos|是否上报偶联断链通知|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否上报偶联断链通知，默认不上报。
gnbcallbackdura|gNB断链告警老化回收时长(小时)|参数可选性: 任选参数类型: 数字参数范围: 1-72默认值: 24|该参数用于设置gNB断链告警老化回收时长，取值范围：1-72小时，缺省为24小时。当gNB断链告警的持续时长超过配置的"gNB断链告警老化回收时长", AMF清除gNB断链告警。




命令举例 


`
查询gNB告警参数。
SHOW GNB ALARMPARA

(No.1) : SHOW GNB ALARMPARA:
-----------------Namf_Communication_0_A----------------
是否上报偶联投入使用通知 是否上报偶联断链通知 gNB断链告警老化回收时长(小时) 
-----------------------------------------------------------------------
否                       否                   36                            
-----------------------------------------------------------------------
记录数：1

执行成功耗时: 0.17 秒

` 


# AMF负荷重平衡优化配置 
# AMF负荷重平衡优化配置 


背景知识 


AMF POOL区域是指UE在其间移动时，不需要改变UE对应的服务AMF的区域，一个AMF POOL区域内由一个或多个对等的AMF组成，AMF POOL区域所辖的物理区域是由多个TA（Tracking Area，跟踪区域）汇聚的，AMF区域内的每个gNB（Next Generation Node B，下一代基站）都与所有的AMF互联。 

AMF是以GUAMI为粒度的，GUAMI由PLMN+Region+Set+Point组成，一个AMF POOL内所有的AMF的GUAMI应该有相同的PLMN+Region+Set，只有Point不相同。 

AMF POOL功能主要包括三个部分： 


 
AMF负荷分担功能
AMF POOL区域内的所有AMF都有负荷分担功能，使用户可以较均衡的分布在各个AMF上，保证了AMF POOL内各个AMF上的负荷和其处理能力达到平衡。 

 
AMF负荷重平衡功能
当POOL内的某个AMF的业务量超负荷或者执行升级操作时，可以将此AMF的全部或部分特定用户迁移到同一个POOL内其他AMF，以减少该AMF下接入用户的数量，从而减少该AMF在这些场景下，对用户业务的影响。 

 
AMF容灾功能
当POOL内的某个AMF故障，或处于不可用状态进，POOL内其他AMF能够支持故障AMF下接入的用户正常使用数据业务。 

 




功能说明 


当AMF启动负荷重平衡功能时，会将全部用户或部分用户进行卸载，由于卸载初期，网络中活动用户较多，会频繁触发注册、业务请求等流程，当全部用户或者部分用户卸载后，会集中到新的AMF进行注册更新，会导致新的AMF的负荷瞬间冲高，造成拥塞。因此，需要对频繁活动用户的卸载过程进行控制。 

本功能用于配置操作员通过[ACTIVE REBALANC START]命令（Namf_Communication模式下）命令启动主动负载重平衡时，是否开启AMF负荷卸载优化功能。




子主题： 






## 修改负荷重平衡优化配置(SET LOADREBALANCOPT) 
## 修改负荷重平衡优化配置(SET LOADREBALANCOPT) 


功能说明 

该命令用于设置执行AMF主动负载重平衡时的优化配置。 

操作员通过本命令设置负荷卸载控制周期、周期令牌投放次数和允许卸载突发系数，然后进行负荷卸载，AMF根据这些设置的控制参数对负荷卸载过程进行速率控制。 


注意事项 

无。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
unloadopt|是否支持负荷卸载优化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|参数作用：此参数用于控制AMF是否支持负荷卸载优化功能。修改影响：开启之后，操作员通过ACTIVE REBALANC START命令（Namf_Communication模式下）命令启动负载主动重平衡时，AMF会根据控制参数对负荷卸载过程进行速率控制。数据来源：本端规划。默认值：1（支持）。配置原则：无。
controlperiod|负荷卸载控制周期(s)|参数可选性: 任选参数类型: 数字参数范围: 1-60|参数作用：此参数用于在AMF支持负荷卸载优化功能的场景下，设置负荷卸载速率控制的周期，用于指示一个负荷卸载控制周期的时间长度。负荷卸载优化功能的过程如下：负荷卸载通过令牌控制机制，即：卸载时AMF首先获取到令牌允许，然后再进行卸载。整个负荷卸载控制周期内令牌总量 = 负荷卸载步长 * 负荷卸载控制周期.（负荷卸载步长是通过ACTIVE REBALANC START命令配置的参数“卸载步长（UNLOADSTEP）”）。在整个负荷卸载控制周期内，根据“周期令牌投放次数”和“允许卸载突发系数”控制每次投放的令牌数量和投放时间间隔。令牌投放间隔 = 控制周期 / 周期令牌投放次数每次令牌投放数量 = 控制周期 * 卸载步长 / 周期令牌投放次数示例：控制周期为10秒，卸载步长为5个/秒。周期令牌投放次数为5次，允许卸载突发系数为2。那么：令牌投放间隔为10/5 = 2秒，每次令牌投放数量为：10*5*2/5 = 20，表示2秒内允许20个用户被卸载，直到所有令牌投放完毕。负荷卸载控制周期结束后，令牌数清0，下一个周期重新计算。修改影响：修改后，操作员通过ACTIVE REBALANC START命令（Namf_Communication模式下）命令启动负载主动重平衡时，AMF在周期内根据动态命令中设置的参数“卸载步长（UNLOADSTEP）”确定卸载令牌数，“卸载步长（UNLOADSTEP）”用于指示最高卸载速率。如果“负荷卸载控制周期”设置过小，会导致卸载时长会增加。负荷卸载控制周期内卸载令牌总数 = 卸载步长 * 负荷卸载控制周期。如果“负荷卸载控制周期”设置过大，会导致单位时间内卸载数量大，可能导致接管AMF产生流控。数据来源：本端规划。默认值：10。配置原则：无。
tokendelitimes|周期令牌投放次数|参数可选性: 任选参数类型: 数字参数范围: 1-600|参数作用：此参数用于在支持负荷卸载优化时，设置负荷控制周期内令牌投放次数，周期令牌投放次数用于指示一个负荷卸载控制周期内令牌桶补充的次数。修改影响：修改后，操作员通过ACTIVE REBALANC START命令（Namf_Communication模式下）命令启动负载主动重平衡时，AMF会根据配置的负荷卸载控制周期确定卸载令牌的投放周期，根据负荷卸载控制周期内卸载令牌总数确定单次令牌投放数量。令牌投放周期 = 负荷卸载控制周期 / 周期令牌投放次数。单次令牌投放数量 = 负荷卸载控制周期内卸载令牌总数 / 周期令牌投放次数。数据来源：本端规划。默认值：5（负荷控制周期/2）。配置原则：参数设置建议值：小于等于“负荷卸载控制周期”，令牌投放间隔控制在1~3秒。
burstcoefficient|允许卸载突发系数|参数可选性: 任选参数类型: 数字参数范围: 1-10|参数作用：此参数用于在支持负荷卸载优化时，设置负荷控制周期内允许用户突增的系数，允许卸载突发系数用于指示单次令牌投放的最高溢出倍数。修改影响：修改后，操作员通过ACTIVE REBALANC START命令（Namf_Communication模式下）命令启动负载主动重平衡时，用户突增导致单次令牌投放数量不足时，AMF会根据允许卸载突发系数扩大令牌投放数量，最大为单次令牌投放数量 * 允许卸载突发系数。1 - 表示每次令牌投放数*1 ；2 - 表示每次令牌投放数 *2；依次类推。数据来源：本端规划。默认值：1。配置原则：无。




命令举例 


`
设置执行AMF主动负载重平衡时支持负荷重平衡优化，负荷卸载控制周期为10秒，周期令牌投放次数为10次，允许卸载突发系数为3。
SET LOADREBALANCOPT:UNLOADOPT="SUPPORT",CONTROLPERIOD=10,TOKENDELITIMES=10,BURSTCOEFFICIENT=3
` 


## 查询负荷重平衡优化配置(SHOW LOADREBALANCOPT) 
## 查询负荷重平衡优化配置(SHOW LOADREBALANCOPT) 


功能说明 

该命令用于查询执行AMF主动负载重平衡时的优化配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
unloadopt|是否支持负荷卸载优化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|参数作用：此参数用于控制AMF是否支持负荷卸载优化功能。
controlperiod|负荷卸载控制周期(s)|参数可选性: 任选参数类型: 数字参数范围: 1-60|参数作用：此参数用于在AMF支持负荷卸载优化功能的场景下，设置负荷卸载速率控制的周期，用于指示一个负荷卸载控制周期的时间长度。
tokendelitimes|周期令牌投放次数|参数可选性: 任选参数类型: 数字参数范围: 1-600|参数作用：此参数用于在支持负荷卸载优化时，设置负荷控制周期内令牌投放次数，周期令牌投放次数用于指示一个负荷卸载控制周期内令牌桶补充的次数。
burstcoefficient|允许卸载突发系数|参数可选性: 任选参数类型: 数字参数范围: 1-10|参数作用：此参数用于在支持负荷卸载优化时，设置负荷控制周期内允许用户突增的系数，允许卸载突发系数用于指示单次令牌投放的最高溢出倍数。




命令举例 


`
查询负荷重平衡优化配置。
SHOW LOADREBALANCOPT:

(No.1) : SHOW LOADREBALANCOPT:
-----------------Namf_Communication_0----------------
操作维护    是否支持负荷卸载优化   负荷卸载控制周期(s)   周期令牌投放次数   允许卸载突发系数
------------------------------------------------------------------------------------------------------------
修改          支持                              10                             10                           3
------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-03-05 11:37:00 耗时: 0.128 秒

` 


# 会话异常处理策略配置 
# 会话异常处理策略配置 


背景知识 


非漫游或者漫游LBO场景下，用户在大区间/省间移动的过程中，为了保证业务连续性，会插入、改变或者删除I-SMF。 

在漫游HR场景下，用户在跨PLMN移动的过程中，也会插入、改变或者删除V-SMF。当AMF与SMF间交互异常时，可能导致PDU会话异常，最终导致终端长时间被叫业务不通， 影响用户体验。 

为了提升用户体验，AMF针对移动性流程（如切换流程、注册更新流程、业务请求流程等）提供会话异常处理策略配置，可以灵活设置AMF与SMF交互异常时的处理策略。 




功能说明 


会话异常处理策略配置包括：业务请求会话异常处理策略配置。 




子主题： 






## 业务请求会话异常处理策略配置 
## 业务请求会话异常处理策略配置 


背景知识 


非漫游或者漫游LBO场景下，用户在大区间/省间移动的过程中，为了保证业务连续性，会插入、改变或者删除I-SMF。 

在漫游HR场景下，用户在跨PLMN移动的过程中，也会插入、改变或者删除V-SMF。当AMF与SMF间交互异常时，可能导致PDU会话异常，最终导致终端长时间被叫业务不通， 影响用户体验。 

为了提升用户体验，AMF针对移动性流程（如切换流程、注册更新流程、业务请求流程等）提供会话异常处理策略配置，可以灵活设置AMF与SMF交互异常时的处理策略。 




功能说明 


该功能用于配置业务请求会话异常处理策略，用于灵活设置AMF与SMF交互异常时的处理策略。 




子主题： 






### 修改业务请求会话异常处理策略配置(SET SESSIONEXCEPTHANDLESR) 
### 修改业务请求会话异常处理策略配置(SET SESSIONEXCEPTHANDLESR) 


功能说明 

该命令用于修改业务请求会话异常处理策略配置。 

当AMF与SMF交互异常，需要灵活设置AMF的处理策略时，使用该命令进行配置。 


注意事项 

本命令执行后，结果立即生效。


输入参数说明 


标识|名称|类型|说明
---|---|---|---
supismfsesdetect|支持有I-SMF的语音会话状态检测|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于配置AMF在处理业务请求流程时，是否支持对有I-SMF的语音会话进行状态监测。修改影响：如果设置为支持，则AMF会对有I-SMF的语音会话进行状态监测，如果状态异常则删除会话相关信息。如果设置为不支持，则AMF不会对有I-SMF的语音会话进行状态监测。数据来源：本端规划。默认值：不支持。配置原则：无
supvsmfsesdetect|支持有V-SMF的语音会话状态检测|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于配置AMF在处理业务请求流程时，是否支持对有V-SMF的语音会话进行状态监测。修改影响：如果设置为支持，则AMF会对有V-SMF的语音会话进行状态监测，如果状态异常则删除会话相关信息。如果设置为不支持，则AMF不会对有V-SMF的语音会话进行状态监测。数据来源：本端规划。默认值：不支持。配置原则：无




命令举例 


`
设置业务请求会话异常处理策略配置。
SET SESSIONEXCEPTHANDLESR:SUPISMFSESDETECT="SUPPORT"
` 


### 查询业务请求会话异常处理策略配置(SHOW SESSIONEXCEPTHANDLESR) 
### 查询业务请求会话异常处理策略配置(SHOW SESSIONEXCEPTHANDLESR) 


功能说明 

该命令用于查询业务请求会话异常处理策略配置。 


注意事项 

无。


输出参数说明 


标识|名称|类型|说明
---|---|---|---
supismfsesdetect|支持有I-SMF的语音会话状态检测|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于配置AMF在处理业务请求流程时，是否支持对有I-SMF的语音会话进行状态监测。
supvsmfsesdetect|支持有V-SMF的语音会话状态检测|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|参数作用：该参数用于配置AMF在处理业务请求流程时，是否支持对有V-SMF的语音会话进行状态监测。




命令举例 


`
查询业务请求会话异常处理策略配置。 
SHOW SESSIONEXCEPTHANDLESR

(No.1) : SHOW SESSIONEXCEPTHANDLESR:
-----------------Namf_Communication_0----------------
操作维护    支持有I-SMF的语音会话状态检测          支持有V-SMF的语音会话状态检测
-------------------------------------------------------------------------------------------------
修改           支持                                                支持
-------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-07-08 10:16:48 耗时: 0.468 秒

` 


