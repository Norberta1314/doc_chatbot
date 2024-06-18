 交换局配置 


[](None)背景知识 

            
            移动网络中，逻辑网元实体，通常也称为交换局。
        


[](None)功能描述 

            
            交换局配置，主要完成本网元的全局属性配置，以及邻接网元与本网元互通对接时需要的邻接网元属性配置。
        


[](None)相关主题 



 

全局数据配置
 

 

SGSN全局寻呼策略配置
 

 

MME全局寻呼策略配置
 

 

MME寻呼策略配置
 

 

MME寻呼策略因子配置
 

 

SGSN其他HPLMN配置
 

 

MME其他HPLMN配置
 

 

本局支持的其他GUMMEI配置
 

 

3位MNC运营商信息配置
 

 

信令面参数配置
 

 

本局移动数据
 

 

FLEX配置
 

 

用户地址号段属性配置
 

 

RAB指派失败统计控制配置
 

 

MME终端双栈数据配置
 

 

SGSN终端双栈数据配置
 

 

VRF配置
 

 

SGs口开关配置
 

 

拒绝原因更正配置
 

 

下行数据通知延迟配置
 

 

Gn GTPU IP能力配置
 

 

MME GTPU地址配置
 

 

NITZ配置
 

 








父主题： [系统配置](../../zh-CN/tree/N_126066_operation_cm_mml_umacV4_cm_combo_gngp_system.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 全局数据配置 
# 全局数据配置 


[](None)背景知识 


移动网络中，逻辑网元实体，通常也称为交换局。 




[](None)功能描述 


本功能主要完成本网元的全局属性配置。 




[](None)相关主题 



 

设置S6a错误码到EMM原因值的转换(SET DIAMERR EMM)
 

 

查询S6a错误码到EMM原因值的转换(SHOW DIAMERR EMM)
 

 

设置MAP错误码到GMM原因值的映射(SET MAPERR GMM)
 

 

查询MAP错误码到GMM原因值的映射(SHOW MAPERR GMM)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置S6a错误码到EMM原因值的转换(SET DIAMERR EMM) 
## 设置S6a错误码到EMM原因值的转换(SET DIAMERR EMM) 


[](None)命令功能 


该命令用于查询S6a错误到NAS EMM失败原因值的映射。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
DIAMERR|S6a错误码|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|需要映射的S6a错误码列表，具有如下列表选项：DIAMETER_ERROR_USER_UNKNOWN (5001)：标准DIAMETER错误码，参考29.272 协议的“7.4.3.1 DIAMETER_ERROR_USER_UNKNOWN(5001)”章节。DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION (5420), without Error Diagnostic, or with Error Diagnostic of GPRS_DATA_SUBSCRIBED：DIAMETER返回错误码“DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION”，且没有携带错误诊断或者携带错误诊断指示用户签约GPRS数据。DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION (5420), with Error Diagnostic of NO_GPRS_DATA_SUBSCRIBED：DIAMETER返回错误码“DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION”，且携带错误诊断指示用户没有签约GPRS数据。DIAMETER_ERROR_RAT_NOT_ALLOWED (5421)：标准DIAMETER错误码，参考29.272协议的“7.4.3.3 DIAMETER_ERROR_RAT_NOT_ALLOWED (5421)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic unenumerated or without Error Diagnostic：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_AUTHORIZATION_REJECTED (5003)：标准DIAMETER错误码，参考29.272 协议的“5.2.3.1.3 Detailed behaviour of the HSS”章节。DIAMETER_UNABLE_TO_COMPLY (5012)：标准DIAMETER错误码，参考29.272协议。DIAMETER_INVALID_AVP_VALUE (5004)：标准DIAMETER错误码，参考29.272协议。DIAMETER_ERROR_EQUIPMENT_UNKNOWN (5422)：标准DIAMETER错误码，参考29.272 协议的“7.4.3.5 DIAMETER_ERROR_EQUIPMENT_UNKNOWN (5422)”章节。OTHER_DIAMETER_ERROR：HSS返回响应消息中其他DIAMETER错误码。MME gets HSS unsuccessfully：MME无法解析用户所在的HSS局向。HSS time out：MME等待HSS响应超时。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_HPLMN_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_VPLMN_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_ALL_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE (4181)：标准DIAMETER错误码，参考29.272 协议的“7.4.4.1 DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE(4181)”章节。DIAMETER_UNABLE_TO_DELIVER (3002)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_REALM_NOT_SERVED (3003)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_AVP_UNSUPPORTED (5001)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_MISSING_AVP (5005)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_RESOURCES_EXCEEDED (5006)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_AVP_OCCURS_TOO_MANY_TIMES (5009)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_TOO_BUSY (3004)：标准DIAMETER错误码，参考RFC 3588协议。HSS Overload：由于HSS过负荷导致MME无法发送消息到HSS，参考RFC 7683协议。Packet only subscription for Combined TAU/LAU：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.2。Roaming restricted due to unsupported feature in ULA：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.2。HSS office unreachable：HSS局向不可达。
EMMCAUSE|EMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|EMM NAS失败原因值列表：IMSI unknown in HSSIllegal UEIllegal MEEPS services not allowedEPS services and non-EPS services not allowedPLMN not allowedTracking Area not allowedRoaming not allowed in this tracking areaEPS services not allowed in this PLMNNo Suitable Cells In tracking areaNetwork failureCS domain not availableESM failureCongestionSevere network failureProtocol error, unspecified
EXEMMCAUSE|是否携带扩展EMM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME附着拒绝或TAU拒绝消息中，是否携带扩展EMM原因字段。E-UTRAN允许E-UTRAN不允许不携带






[](None)命令举例 


配置S6a错误码“USER_UNKONW”映射为EMM NAS原因值“IMSI unknow in HSS”。 


配置成功后，用户附着、跟踪区更新、业务请求或者扩展业务请求时，MME向HSS请求鉴权向量或者更新HSS，HSS返回失败响应，错误码为“User Unknown”，导致整个业务失败，MME需要下发拒绝消息给UE，携带失败原因值为“IMSI unknown in HSS”。 


SET DIAMERR EMM:DIAMERR="USER_UNKNOWN",EMMCAUSE="IMSIUnknownInHSS"; 








父主题： [全局数据配置](../../zh-CN/tree/N_1254211.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询S6a错误码到EMM原因值的转换(SHOW DIAMERR EMM) 
## 查询S6a错误码到EMM原因值的转换(SHOW DIAMERR EMM) 


[](None)命令功能 


该命令用于查询S6a错误到NAS EMM失败原因值的映射。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
DIAMERR|S6a错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|需要映射的S6a错误码列表，具有如下列表选项：DIAMETER_ERROR_USER_UNKNOWN (5001)：标准DIAMETER错误码，参考29.272 协议的“7.4.3.1 DIAMETER_ERROR_USER_UNKNOWN(5001)”章节。DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION (5420), without Error Diagnostic, or with Error Diagnostic of GPRS_DATA_SUBSCRIBED：DIAMETER返回错误码“DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION”，且没有携带错误诊断或者携带错误诊断指示用户签约GPRS数据。DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION (5420), with Error Diagnostic of NO_GPRS_DATA_SUBSCRIBED：DIAMETER返回错误码“DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION”，且携带错误诊断指示用户没有签约GPRS数据。DIAMETER_ERROR_RAT_NOT_ALLOWED (5421)：标准DIAMETER错误码，参考29.272协议的“7.4.3.3 DIAMETER_ERROR_RAT_NOT_ALLOWED (5421)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic unenumerated or without Error Diagnostic：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_AUTHORIZATION_REJECTED (5003)：标准DIAMETER错误码，参考29.272 协议的“5.2.3.1.3 Detailed behaviour of the HSS”章节。DIAMETER_UNABLE_TO_COMPLY (5012)：标准DIAMETER错误码，参考29.272协议。DIAMETER_INVALID_AVP_VALUE (5004)：标准DIAMETER错误码，参考29.272协议。DIAMETER_ERROR_EQUIPMENT_UNKNOWN (5422)：标准DIAMETER错误码，参考29.272 协议的“7.4.3.5 DIAMETER_ERROR_EQUIPMENT_UNKNOWN (5422)”章节。OTHER_DIAMETER_ERROR：HSS返回响应消息中其他DIAMETER错误码。MME gets HSS unsuccessfully：MME无法解析用户所在的HSS局向。HSS time out：MME等待HSS响应超时。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_HPLMN_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_VPLMN_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_ALL_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE (4181)：标准DIAMETER错误码，参考29.272 协议的“7.4.4.1 DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE(4181)”章节。DIAMETER_UNABLE_TO_DELIVER (3002)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_REALM_NOT_SERVED (3003)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_AVP_UNSUPPORTED (5001)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_MISSING_AVP (5005)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_RESOURCES_EXCEEDED (5006)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_AVP_OCCURS_TOO_MANY_TIMES (5009)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_TOO_BUSY (3004)：标准DIAMETER错误码，参考RFC 3588协议。HSS Overload：由于HSS过负荷导致MME无法发送消息到HSS，参考RFC 7683协议。Packet only subscription for Combined TAU/LAU：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.2。Roaming restricted due to unsupported feature in ULA：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.2。HSS office unreachable：HSS局向不可达。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
DIAMERR|S6a错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|需要映射的S6a错误码列表，具有如下列表选项：DIAMETER_ERROR_USER_UNKNOWN (5001)：标准DIAMETER错误码，参考29.272 协议的“7.4.3.1 DIAMETER_ERROR_USER_UNKNOWN(5001)”章节。DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION (5420), without Error Diagnostic, or with Error Diagnostic of GPRS_DATA_SUBSCRIBED：DIAMETER返回错误码“DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION”，且没有携带错误诊断或者携带错误诊断指示用户签约GPRS数据。DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION (5420), with Error Diagnostic of NO_GPRS_DATA_SUBSCRIBED：DIAMETER返回错误码“DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION”，且携带错误诊断指示用户没有签约GPRS数据。DIAMETER_ERROR_RAT_NOT_ALLOWED (5421)：标准DIAMETER错误码，参考29.272协议的“7.4.3.3 DIAMETER_ERROR_RAT_NOT_ALLOWED (5421)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic unenumerated or without Error Diagnostic：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_AUTHORIZATION_REJECTED (5003)：标准DIAMETER错误码，参考29.272 协议的“5.2.3.1.3 Detailed behaviour of the HSS”章节。DIAMETER_UNABLE_TO_COMPLY (5012)：标准DIAMETER错误码，参考29.272协议。DIAMETER_INVALID_AVP_VALUE (5004)：标准DIAMETER错误码，参考29.272协议。DIAMETER_ERROR_EQUIPMENT_UNKNOWN (5422)：标准DIAMETER错误码，参考29.272 协议的“7.4.3.5 DIAMETER_ERROR_EQUIPMENT_UNKNOWN (5422)”章节。OTHER_DIAMETER_ERROR：HSS返回响应消息中其他DIAMETER错误码。MME gets HSS unsuccessfully：MME无法解析用户所在的HSS局向。HSS time out：MME等待HSS响应超时。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_HPLMN_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_VPLMN_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004), with Error Diagnostic of ODB_ALL_APN：标准DIAMETER错误码，参考29.272 协议的“7.4.3.4 DIAMETER_ERROR_ROAMING_NOT_ALLOWED (5004)”章节。DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE (4181)：标准DIAMETER错误码，参考29.272 协议的“7.4.4.1 DIAMETER_AUTHENTICATION_DATA_UNAVAILABLE(4181)”章节。DIAMETER_UNABLE_TO_DELIVER (3002)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_REALM_NOT_SERVED (3003)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_AVP_UNSUPPORTED (5001)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_MISSING_AVP (5005)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_RESOURCES_EXCEEDED (5006)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_AVP_OCCURS_TOO_MANY_TIMES (5009)：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.1。DIAMETER_TOO_BUSY (3004)：标准DIAMETER错误码，参考RFC 3588协议。HSS Overload：由于HSS过负荷导致MME无法发送消息到HSS，参考RFC 7683协议。Packet only subscription for Combined TAU/LAU：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.2。Roaming restricted due to unsupported feature in ULA：标准DIAMETER错误码，参考29.272 协议的“8 User identity to HSS resolution”章节，Table A.2。HSS office unreachable：HSS局向不可达。
EMMCAUSE|EMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|EMM NAS失败原因值列表：IMSI unknown in HSSIllegal UEIllegal MEEPS services not allowedEPS services and non-EPS services not allowedPLMN not allowedTracking Area not allowedRoaming not allowed in this tracking areaEPS services not allowed in this PLMNNo Suitable Cells In tracking areaNetwork failureCS domain not availableESM failureCongestionSevere network failureProtocol error, unspecified
EXEMMCAUSE|是否携带扩展EMM原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME附着拒绝或TAU拒绝消息中，是否携带扩展EMM原因字段。E-UTRAN允许E-UTRAN不允许不携带






[](None)命令举例 


查询S6a错误码“User Unknown”对应的EMM NAS失败原因值。 


SHOW DIAMERR EMM:DIAMERR="USER_UNKNOWN"; 


`
命令 (No.1): SHOW DIAMERR EMM:DIAMERR="USER_UNKNOWN";

操作维护  Diameter错误码                    EMM原因值                                         是否携带扩展EMM原因
-----------------------------------------------------------------------------------------------------------------
修改      DIAMETER_ERROR_USER_UNKNOWN       EPS services and non-EPS services not allowed     不携带
-----------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.063 秒）。


` 


MME可以查询全部的映射关系，查询命令为[SHOW DIAMERR EMM](1260261.html)。








父主题： [全局数据配置](../../zh-CN/tree/N_1254211.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置MAP错误码到GMM原因值的映射(SET MAPERR GMM) 
## 设置MAP错误码到GMM原因值的映射(SET MAPERR GMM) 


[](None)命令功能 


该命令用于在SGSN上配置MAP失败类型和GMM失败原因值的映射关系。配置后，MS发起Attach或者RAU流程时，如果HLR向SGSN返回MAP失败，SGSN根据该命令配置的映射关系表基于HLR返回的MAP失败类型给MS返回对应的GMM失败原因值。 




[](None)注意事项 


若SGSN上已经配置了“拒绝原因更正配置”，对应的查询命令为：[SHOW CAUSE CORRECT](1260248.html)，在MS进行Attach或者RAU流程时，如果HLR向SGSN返回MAP失败，SGSN返回给MS的拒绝消息中携带的是更正后的拒绝原因值。




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MAPERR|MAP错误码|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数标识MAP错误原因，包括如下选项：Unknown subscriber：MAP响应消息携带的user error为“unknown subscriber”，无附加诊断信息。Unknown subscriber (no GPRS subscription)：MAP响应消息携带的user error为“unknown subscriber”，附加诊断信息为“Gprs or EPS Subscription Unknown”。Unknown subscriber (IMSI unknown)：MAP响应消息携带的user error为“unknown subscriber”，附加诊断信息为“Imsi Unknown”。Roaming not allowed (PLMN not allowed)：MAP响应消息携带的user error为“roaming not allowed”，附加诊断信息为“PLMN Not Allowed”。Roaming not allowed (Operator determined barring)：MAP响应消息携带的user error为“roaming not allowed”，附加诊断信息为“Operator Determined Barring”。Unknown equipment：MAP响应消息携带的user error为“unknown equipment”。System Failure：MAP响应消息携带的user error为“system Failure”。Unexpected data value：MAP响应消息携带的user error为“unexpected data value”。Data missing：MAP响应消息携带的user error为“data missing”。Other user errors：MAP响应消息携带的user error为其他错误。MAP procedure error or provider error：MAP响应消息携带provider error，或者MAP处理错误。Unknown HLR：HLR未知，无法获取有效的HLR。
GMMCAUSE|GMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识GMM拒绝原因值，在SGSN网元，可以根据实际需要配置MAP错误类型和GMM拒绝原因值的映射关系。GMM拒绝原因值在3GPP24.008协议10.5.5.14节中定义，目前包含如下选项：IMSI unknown in HLRIllegal MSIllegal MEGPRS services not allowedGPRS services and non-GPRS services not allowedMS identity cannot be derived by the networkImplicitly detachedPLMN not allowedLocation Area not allowedRoaming not allowed in this location areaGPRS services not allowed in this PLMNNo Suitable Cells In Location AreaNetwork failureCongestion






[](None)命令举例 


设置MAP错误码到GMM原因值的映射，MAP错误码为MAP procedure error or provider error，GMM原因值为IMSI unknown in HLR。 


SET MAPERR GMM:MAPERR="MAPPROC_PROVIDER_ERR",GMMCAUSE="IMSI_UNKNOWN_INHLR"; 








父主题： [全局数据配置](../../zh-CN/tree/N_1254211.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询MAP错误码到GMM原因值的映射(SHOW MAPERR GMM) 
## 查询MAP错误码到GMM原因值的映射(SHOW MAPERR GMM) 


[](None)命令功能 


该命令用于查询MAP错误到NAS GMM失败原因值的映射。 




[](None)注意事项 


若SGSN上已经配置了“拒绝原因更正配置”，对应的查询命令为：[SHOW CAUSE CORRECT](1260248.html)，在MS进行Attach或者RAU流程时，如果HLR向SGSN返回MAP失败，SGSN返回给MS的拒绝消息中携带的是更正后的拒绝原因值。




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MAPERR|MAP错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识MAP错误原因，包括如下选项：Unknown subscriber：MAP响应消息携带的user error为“unknown subscriber”，无附加诊断信息。Unknown subscriber (no GPRS subscription)：MAP响应消息携带的user error为“unknown subscriber”，附加诊断信息为“Gprs or EPS Subscription Unknown”。Unknown subscriber (IMSI unknown)：MAP响应消息携带的user error为“unknown subscriber”，附加诊断信息为“Imsi Unknown”。Roaming not allowed (PLMN not allowed)：MAP响应消息携带的user error为“roaming not allowed”，附加诊断信息为“PLMN Not Allowed”。Roaming not allowed (Operator determined barring)：MAP响应消息携带的user error为“roaming not allowed”，附加诊断信息为“Operator Determined Barring”。Unknown equipment：MAP响应消息携带的user error为“unknown equipment”。System Failure：MAP响应消息携带的user error为“system Failure”。Unexpected data value：MAP响应消息携带的user error为“unexpected data value”。Data missing：MAP响应消息携带的user error为“data missing”。Other user errors：MAP响应消息携带的user error为其他错误。MAP procedure error or provider error：MAP响应消息携带provider error，或者MAP处理错误。Unknown HLR：HLR未知，无法获取有效的HLR。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MAPERR|MAP错误码|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识MAP错误原因，包括如下选项：Unknown subscriber：MAP响应消息携带的user error为“unknown subscriber”，无附加诊断信息。Unknown subscriber (no GPRS subscription)：MAP响应消息携带的user error为“unknown subscriber”，附加诊断信息为“Gprs or EPS Subscription Unknown”。Unknown subscriber (IMSI unknown)：MAP响应消息携带的user error为“unknown subscriber”，附加诊断信息为“Imsi Unknown”。Roaming not allowed (PLMN not allowed)：MAP响应消息携带的user error为“roaming not allowed”，附加诊断信息为“PLMN Not Allowed”。Roaming not allowed (Operator determined barring)：MAP响应消息携带的user error为“roaming not allowed”，附加诊断信息为“Operator Determined Barring”。Unknown equipment：MAP响应消息携带的user error为“unknown equipment”。System Failure：MAP响应消息携带的user error为“system Failure”。Unexpected data value：MAP响应消息携带的user error为“unexpected data value”。Data missing：MAP响应消息携带的user error为“data missing”。Other user errors：MAP响应消息携带的user error为其他错误。MAP procedure error or provider error：MAP响应消息携带provider error，或者MAP处理错误。Unknown HLR：HLR未知，无法获取有效的HLR。
GMMCAUSE|GMM原因值|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数标识GMM拒绝原因值，在SGSN网元，可以根据实际需要配置MAP错误类型和GMM拒绝原因值的映射关系。GMM拒绝原因值在3GPP24.008协议10.5.5.14节中定义，目前包含如下选项：IMSI unknown in HLRIllegal MSIllegal MEGPRS services not allowedGPRS services and non-GPRS services not allowedMS identity cannot be derived by the networkImplicitly detachedPLMN not allowedLocation Area not allowedRoaming not allowed in this location areaGPRS services not allowed in this PLMNNo Suitable Cells In Location AreaNetwork failureCongestion






[](None)命令举例 


查询MAP失败原因到GMM原因值的映射。 


SHOW MAPERR GMM 


`

命令 (No.10): SHOW MAPERR GMM

操作维护  MAP错误码                                           GMM原因值
-----------------------------------------------------------------------
修改      MAP procedure error or provider error               Network failure
修改      Unknown subscriber (IMSI unknown)                   GPRS services and non-GPRS services not allowed
修改      Unknown subscriber (no GPRS subscription)           GPRS services not allowed
修改      Roaming not allowed (PLMN not allowed)              GPRS services not allowed in this PLMN
修改      Roaming not allowed (Operator determined barring)   GPRS services not allowed in this PLMN
修改      Unknown subscriber                                  GPRS services not allowed
修改      Unknown equipment                                   GPRS services not allowed
修改      Unknown HLR                                         GPRS services not allowed in this PLMN
修改      Other user errors                                   Network failure
修改      System Failure                                      Network failure
修改      Unexpected data value                               Network failure
修改      Data missing                                        Network failure
-----------------------------------------------------------------------
记录数 12

命令执行成功（耗时 0.119 秒）。
` 








父主题： [全局数据配置](../../zh-CN/tree/N_1254211.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SGSN全局寻呼策略配置 
# SGSN全局寻呼策略配置 


[](None)背景知识 


终端接入网络后，不发生语音或者数据业务时，为了省电，可以进入空闲状态，空闲状态下，SGSN与基站之间，基站与终端之间的无线侧连接被释放。处于空闲状态的终端无法接收下行数据，如果SGSN需要向空闲状态的终端发送下行数据，SGSN需要在特定区域内（比如，路由区）广播寻呼消息，终端侦听到寻呼消息后通过消息流程（比如，业务请求、路由更新等）重新建立无线侧连接。终端进入连接状态，SGSN即可进行下行数据的发送。 


SGSN通过广播方式发送寻呼消息时，需要向特定区域内的所有RNC/BSC发送寻呼消息，再由RNC/BSC通过其管理的NodeB/BTS在空口广播寻呼消息。如果SGSN发送寻呼消息的区域范围内NodeB/BTS较多时，寻呼的消息量较大。 




[](None)功能描述 


SGSN全局寻呼策略配置，用于指导SGSN按照特定的策略发送寻呼消息，通过灵活的寻呼策略配置，适应不同的网络状况并提高寻呼成功率。 


本配置有缺省配置，默认不需要调整。如果需要调整，建议联系中兴核心网专家，否则可能引起网络信令负荷波动或者寻呼成功率下降。 




[](None)相关主题 



 

设置SGSN全局寻呼策略(SET SGSN PAGING POLICY)
 

 

查询SGSN全局寻呼策略(SHOW SGSN PAGING POLICY)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置SGSN全局寻呼策略(SET SGSN PAGING POLICY) 
## 设置SGSN全局寻呼策略(SET SGSN PAGING POLICY) 


[](None)命令功能 

该命令用于设置SGSN全局寻呼策略，当需要调整本局在全局范围内寻呼所采用的策略（包括寻呼次数，寻呼超时时长，寻呼方式等参数）时，使用该命令。该命令执行成功后，寻呼策略生效。该寻呼策略是全局性的，也就说该命令生效后，本SGSN局的寻呼都会依照当前执行的命令进行寻呼。


[](None)注意事项 



 
该命令为全局性的，配置内容影响到对所有RNC/BSC下用户寻呼。
 

 
寻呼间隔跟 N、M 是两种不同的寻呼寻制方式，且N、M方式优先级高于寻呼间隔方式，如果配置N不为 0，那么寻呼间隔只能配置为 0，这个后台配置时就会有配置限制。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PGINTERVAL|寻呼间隔时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:0~186。|该参数用于指定寻呼失败时，该用户下次进行寻呼时的下发限制。用户寻呼失败时记录当前时间点，下次对该用户进行寻呼时，以当前时间跟上次记录的寻呼失败时间点取时间差，如果时间差小于配置的该参数“寻呼间隔时间”，那么本次寻呼不允许下发（不允许下发时不更新寻呼失败时间点）。直到收到寻呼，当前时间减去上次寻呼失败时间大于配置该“寻呼间隔时间”时，才允许时间下发。
NMTYPE|N+M方式|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：N，M。用于指定N次触发寻呼不到用户后，后面的M次寻呼触发将不发起寻呼.
PGN|N|参数可选性:任选参数；参数类型:整数；参数范围为:0~127。|该参数用于指定寻呼时允许次数。SGSN通过该参数指定允许连续失败的寻呼次数。寻呼失败时，对该用户记录寻呼失败次数加1，当失败次数累加到N次后，开始拒绝下发寻呼。中间寻呼成功时，该累加出的失败次数清零。
PGM|M|参数可选性:任选参数；参数类型:整数；参数范围为:1~127。|该参数用于指定寻呼时不允许寻呼次数。SGSN通过该参数指定连续失败次数达到N次时，开始拒绝寻呼，同时寻呼拒绝次数M开始累加。累加到M次后，开始允许寻呼。
PGTIMES|寻呼次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~5。|该参数用于指定本次寻呼的重发次数，寻呼寻呼超时时，允许在配置的该寻呼次数内进行超时重发。
IMSIPAGING|是否尝试IMSI寻呼|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于是否允许IMSI寻呼，IMSI寻呼表明最后一次（重发最后一次，或寻呼次数为 1时的当前寻呼），采用IMSI寻呼，寻呼用户标识不带PTMSI，只带IMSI，且寻呼区域使用参数“PS域IMSI寻呼区域”配置的寻呼区域。取值含义：不支持（NO）：不支持IMSI寻呼支持（YES）：支持IMSI寻呼
IMSIPGAREA|PS域IMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定IMSI寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
OTHERITFPG|是否在其它接口寻呼|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定是否允许OTHER寻呼，用户在已配置的寻呼次数下寻呼都失败时，最后再以不同于当前接入类型的方式进行最后一次寻呼，比如当前用户2G接入，OTHER寻呼为3G寻呼，反之，3G接入时，OTHER寻呼为2G寻呼。取值含义：不支持（NO）：不支持OTHER寻呼支持（YES）：支持OTHER寻呼
PGVALIDDURATION|边界寻呼有效时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:30~7200。|该参数用于指定存在边界区寻呼时，边界区的时间有效性。最新更新的三次位置区域中，如果有大于配置的该“边界寻呼有效时长”时，边界区域不能用于进行寻呼。
GBPG1|Gb接入PTMSI寻呼区域1|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：GBPGDURATION1，GBPTMSIPGAREA1。用于指定第一次2G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
GBPGDURATION1|Gb接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第一次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA1|Gb接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第一次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
GBPG2|Gb接入PTMSI寻呼区域2|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：GBPGDURATION2，GBPTMSIPGAREA2。用于指定第二次2G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
GBPGDURATION2|Gb接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第二次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA2|Gb接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第二次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
GBPG3|Gb接入PTMSI寻呼区域3|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：GBPGDURATION3，GBPTMSIPGAREA3。用于指定第三次2G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
GBPGDURATION3|Gb接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第三次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA3|Gb接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第三次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
GBPG4|Gb接入PTMSI寻呼区域4|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：GBPGDURATION4，GBPTMSIPGAREA4。用于指定第四次2G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
GBPGDURATION4|Gb接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第四次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA4|Gb接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第四次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
GBPG5|Gb接入PTMSI寻呼区域5|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：GBPGDURATION5，GBPTMSIPGAREA5。用于指定第五次2G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
GBPGDURATION5|Gb接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第五次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA5|Gb接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第五次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPG1|Iu接入PTMSI寻呼区域1|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：IUPGDURATION1，IUPTMSIPGAREA1。用于指定第一次3G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
IUPGDURATION1|Iu接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第一次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA1|Iu接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第一次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPG2|Iu接入PTMSI寻呼区域2|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：IUPGDURATION2，IUPTMSIPGAREA2。用于指定第二次3G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
IUPGDURATION2|Iu接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第二次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA2|Iu接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第二次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPG3|Iu接入PTMSI寻呼区域3|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：IUPGDURATION3，IUPTMSIPGAREA3。用于指定第三次3G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
IUPGDURATION3|Iu接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第三次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA3|Iu接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第三次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPG4|Iu接入PTMSI寻呼区域4|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：IUPGDURATION4，IUPTMSIPGAREA4。用于指定第四次3G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
IUPGDURATION4|Iu接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第四次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA4|Iu接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第四次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPG5|Iu接入PTMSI寻呼区域5|参数可选性:任选参数；参数类型:复合参数|该参数是以下两个参数的组合：IUPGDURATION5，IUPTMSIPGAREA5。用于指定第五次3G寻呼时，寻呼超时定时器的时长和寻呼时所采用的寻呼区域
IUPGDURATION5|Iu接入PTMSI寻呼超时时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:0~25。|该参数用于指定第五次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA5|Iu接入PTMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第五次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。






[](None)命令举例 


设置全局寻策略，其中寻呼间隔为 1、寻呼限制N：1和M：1、寻呼次数为5、支持IMSI寻呼、IMSI寻呼区域为SGSN、寻呼区域有效时长为30S、GB口第一次寻呼，寻呼定时器为1S，寻呼方式为SGSN 全局寻呼、GB口第二次寻呼，寻呼定时器为2S，寻呼方式为RAI寻呼、GB口第三次寻呼，寻呼定时器为3S，寻呼方式为BVC寻呼、GB口第四次寻呼，寻呼定时器为4S，寻呼方式为LAI寻呼、GB口第五次寻呼，寻呼定时器为5S，寻呼方式为边界寻呼、IU口第一次寻呼，寻呼定时器为1S，寻呼方式为SGSN 全局寻呼、IU口第二次寻呼，寻呼定时器为2S，寻呼方式为RAI寻呼、IU口第三次寻呼，寻呼定时器为3S，寻呼方式为LAI寻呼、IU口第四次寻呼，寻呼定时器为4S，寻呼方式为边界寻呼、IU口第五次寻呼，寻呼定时器为5S，寻呼方式为SGSN 全局寻呼。
SET SGSN PAGING POLICY:PGINTERVAL=0,NMTYPE=1-1,PGTIMES=5,IMSIPAGING="YES",IMSIPGAREA="SGSN",PGVALIDDURATION=30,GBPG1=1-"SGSN",GBPG2=2-"RAI",GBPG3=3-"BVC",GBPG4=4-"LAI",GBPG5=5-"BoundaryPaging",IUPG1=1-"SGSN",IUPG2=2-"RAI",IUPG3=3-"LAI",IUPG4=4-"BoundaryPaging",IUPG5=5-"SGSN"; 








父主题： [SGSN全局寻呼策略配置](../../zh-CN/tree/N_1254212.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询SGSN全局寻呼策略(SHOW SGSN PAGING POLICY) 
## 查询SGSN全局寻呼策略(SHOW SGSN PAGING POLICY) 


[](None)命令功能 

该命令用于查询SGSN全局寻呼策略。该查询命令不带参数，查询结果为所配置的全局寻呼策略，只有一条记录。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PGINTERVAL|寻呼间隔时间(分钟)|参数可选性:任选参数；参数类型:整数。|该参数用于指定寻呼失败时，该用户下次进行寻呼时的下发限制。用户寻呼失败时记录当前时间点，下次对该用户进行寻呼时，以当前时间跟上次记录的寻呼失败时间点取时间差，如果时间差小于配置的该参数“寻呼间隔时间”，那么本次寻呼不允许下发（不允许下发时不更新寻呼失败时间点）。直到收到寻呼，当前时间减去上次寻呼失败时间大于配置该“寻呼间隔时间”时，才允许时间下发。
PGN|N|参数可选性:任选参数；参数类型:整数。|该参数用于指定寻呼时允许次数。SGSN通过该参数指定允许连续失败的寻呼次数。寻呼失败时，对该用户记录寻呼失败次数加1，当失败次数累加到N次后，开始拒绝下发寻呼。中间寻呼成功时，该累加出的失败次数清零。
PGM|M|参数可选性:任选参数；参数类型:整数。|该参数用于指定寻呼时不允许寻呼次数。SGSN通过该参数指定连续失败次数达到N次时，开始拒绝寻呼，同时寻呼拒绝次数M开始累加。累加到M次后，开始允许寻呼。
PGTIMES|寻呼次数|参数可选性:任选参数；参数类型:整数。|该参数用于指定本次寻呼的重发次数，寻呼寻呼超时时，允许在配置的该寻呼次数内进行超时重发。
IMSIPAGING|是否尝试IMSI寻呼|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于是否允许IMSI寻呼，IMSI寻呼表明最后一次（重发最后一次，或寻呼次数为 1时的当前寻呼），采用IMSI寻呼，寻呼用户标识不带PTMSI，只带IMSI，且寻呼区域使用参数“PS域IMSI寻呼区域”配置的寻呼区域。取值含义：不支持（NO）：不支持IMSI寻呼支持（YES）：支持IMSI寻呼
IMSIPGAREA|PS域IMSI寻呼区域|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定IMSI寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
OTHERITFPG|是否在其它接口寻呼|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定是否允许OTHER寻呼，用户在已配置的寻呼次数下寻呼都失败时，最后再以不同于当前接入类型的方式进行最后一次寻呼，比如当前用户2G接入，OTHER寻呼为3G寻呼，反之，3G接入时，OTHER寻呼为2G寻呼。取值含义：不支持（NO）：不支持OTHER寻呼支持（YES）：支持OTHER寻呼
PGVALIDDURATION|边界寻呼有效时长(秒)|参数可选性:任选参数；参数类型:整数。|该参数用于指定存在边界区寻呼时，边界区的时间有效性。最新更新的三次位置区域中，如果有大于配置的该“边界寻呼有效时长”时，边界区域不能用于进行寻呼。
GBPGDURATION1|Gb接入PTMSI寻呼超时时长(秒)1|参数可选性:任选参数；参数类型:整数。|该参数用于指定第一次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA1|Gb接入PTMSI寻呼区域1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第一次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
GBPGDURATION2|Gb接入PTMSI寻呼超时时长(秒)2|参数可选性:任选参数；参数类型:整数。|该参数用于指定第二次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA2|Gb接入PTMSI寻呼区域2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第二次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
GBPGDURATION3|Gb接入PTMSI寻呼超时时长(秒)3|参数可选性:任选参数；参数类型:整数。|该参数用于指定第三次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA3|Gb接入PTMSI寻呼区域3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第三次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
GBPGDURATION4|Gb接入PTMSI寻呼超时时长(秒)4|参数可选性:任选参数；参数类型:整数。|该参数用于指定第四次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA4|Gb接入PTMSI寻呼区域4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第四次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
GBPGDURATION5|Gb接入PTMSI寻呼超时时长(秒)5|参数可选性:任选参数；参数类型:整数。|该参数用于指定第五次2G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
GBPTMSIPGAREA5|Gb接入PTMSI寻呼区域5|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第五次2G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。BVC（BVC）：寻呼区域是用户所在的BVC对应小区。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPGDURATION1|Iu接入PTMSI寻呼超时时长(秒)1|参数可选性:任选参数；参数类型:整数。|该参数用于指定第一次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA1|Iu接入PTMSI寻呼区域1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第一次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPGDURATION2|Iu接入PTMSI寻呼超时时长(秒)2|参数可选性:任选参数；参数类型:整数。|该参数用于指定第二次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA2|Iu接入PTMSI寻呼区域2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第二次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPGDURATION3|Iu接入PTMSI寻呼超时时长(秒)3|参数可选性:任选参数；参数类型:整数。|该参数用于指定第三次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA3|Iu接入PTMSI寻呼区域3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第三次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPGDURATION4|Iu接入PTMSI寻呼超时时长(秒)4|参数可选性:任选参数；参数类型:整数。|该参数用于指定第四次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA4|Iu接入PTMSI寻呼区域4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第四次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。
IUPGDURATION5|Iu接入PTMSI寻呼超时时长(秒)5|参数可选性:任选参数；参数类型:整数。|该参数用于指定第五次3G寻呼时，寻呼超时定时器的时长。如果寻呼超时，且当前超时次数不大于配置的“寻呼次数”，就会进行寻呼重发。否则，寻呼失败。
IUPTMSIPGAREA5|Iu接入PTMSI寻呼区域5|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定第五次3G寻呼时所采用的寻呼区域。取值含义：SGSN（SGSN）：寻呼区域是SGSN下所有RNC或NSE。RAI（RAI）：寻呼区域是用户所在的RAI。LAI（LAI）：寻呼区域是用户所在的LAI。边界寻呼（BoundaryPaging）：寻呼区域是用户所在的最新的位置区域，最多为3个最新位置区。






[](None)命令举例 


查询SGSN全局寻呼策略。
SHOW SGSN PAGING POLICY; 


`

命令 (No.1): SHOW SGSN PAGING POLICY

操作维护  寻呼间隔时间(分钟)   N     M     寻呼次数   是否尝试IMSI寻呼   PS域IMSI寻呼区域   是否在其它接口寻呼   边界寻呼有效时长(秒)   Gb接入PTMSI寻呼超时时长(秒)1   Gb接入PTMSI寻呼区域1   Gb接入PTMSI寻呼超时时长(秒)2   Gb接入PTMSI寻呼区域2   Gb接入PTMSI寻呼超时时长(秒)3   Gb接入PTMSI寻呼区域3   Gb接入PTMSI寻呼超时时长(秒)4   Gb接入PTMSI寻呼区域4   Gb接入PTMSI寻呼超时时长(秒)5   Gb接入PTMSI寻呼区域5   Iu接入PTMSI寻呼超时时长(秒)1   Iu接入PTMSI寻呼区域1   Iu接入PTMSI寻呼超时时长(秒)2   Iu接入PTMSI寻呼区域2   Iu接入PTMSI寻呼超时时长(秒)3   Iu接入PTMSI寻呼区域3   Iu接入PTMSI寻呼超时时长(秒)4   Iu接入PTMSI寻呼区域4   Iu接入PTMSI寻呼超时时长(秒)5   Iu接入PTMSI寻呼区域5
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      0                    1     1     5          支持               SGSN               不支持               30                     1                              SGSN                   2                              RAI                    3                              BVC                    4                              LAI                    5                              边界寻呼               1                              SGSN                   2                              RAI                    3                              LAI                    4                              边界寻呼               5                              SGSN
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.043 秒）。
` 








父主题： [SGSN全局寻呼策略配置](../../zh-CN/tree/N_1254212.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MME全局寻呼策略配置 
# MME全局寻呼策略配置 


[](None)背景知识 


终端接入网络后，不发生语音或者数据业务时，为了省电，可以进入空闲状态，空闲状态下，MME与基站之间，基站与终端之间的无线侧连接被释放。处于空闲状态的终端无法接收下行数据，如果MME需要向空闲状态的终端发送下行数据，MME需要在特定区域内（比如，跟踪区列表）广播寻呼消息，终端侦听到寻呼消息后通过消息流程（比如，业务请求、跟踪区更新等）重新建立无线侧连接。终端进入连接状态，MME即可进行下行数据的发送。 


MME通过广播方式发送寻呼消息时，需要向特定区域内的所有eNodeB发送寻呼消息，再由eNodeB在空口广播寻呼消息。如果MME发送寻呼消息的区域范围内eNodeB较多时，寻呼的消息量较大。 




[](None)功能描述 


MME全局寻呼策略配置，用于指导MME按照特定的策略发送寻呼消息，通过灵活的寻呼策略配置，适应不同的网络状况并提高寻呼成功率，同时可以设置邻接eNB寻呼策略。 


本配置有缺省配置，默认不需要调整。如果需要调整，建议联系中兴核心网专家，否则可能引起网络信令负荷波动或者寻呼成功率下降。 




[](None)相关主题 



 

设置数据业务全局寻呼策略(SET MME GLOBAL PS PAGING POLICY)
 

 

修改数据业务全局寻呼策略(MOD MME GLOBAL PS PAGING POLICY)
 

 

查询数据业务全局寻呼策略(SHOW MME GLOBAL PS PAGING POLICY)
 

 

设置CS语音业务全局寻呼策略(SET MME GLOBAL CS PAGING POLICY)
 

 

查询CS语音业务全局寻呼策略(SHOW MME GLOBAL CS PAGING POLICY)
 

 

设置短信业务全局寻呼策略(SET MME GLOBAL SMS PAGING POLICY)
 

 

修改短信业务全局寻呼策略(MOD MME GLOBAL SMS PAGING POLICY)
 

 

查询短信业务全局寻呼策略(SHOW MME GLOBAL SMS PAGING POLICY)
 

 

设置IDR业务全局寻呼策略(SET MME GLOBAL IDR PAGING POLICY)
 

 

修改IDR业务全局寻呼策略(MOD MME GLOBAL IDR PAGING POLICY)
 

 

查询IDR业务全局寻呼策略(SHOW MME GLOBAL IDR PAGING POLICY)
 

 

设置NB-IoT业务全局寻呼策略(SET MME GLOBAL NBIOT PAGING POLICY)
 

 

修改NB-IoT业务全局寻呼策略(MOD MME GLOBAL NBIOT PAGING POLICY)
 

 

查询NB-IoT业务全局寻呼策略(SHOW MME GLOBAL NBIOT PAGING POLICY)
 

 

修改邻接eNB寻呼策略(SET NEIGHBOR ENB PAGING POLICY)
 

 

查询邻接eNB寻呼策略(SHOW NEIGHBOR ENB PAGING POLICY)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置数据业务全局寻呼策略(SET MME GLOBAL PS PAGING POLICY) 
## 设置数据业务全局寻呼策略(SET MME GLOBAL PS PAGING POLICY) 


[](None)命令功能 


该命令用于配置MME数据业务全局寻呼策略。系统存在默认的寻呼策略配置，当运营商根据自身网络状况，需要修改寻呼策略时，可以通过该命令配置。修改成功后，后续寻呼业务将根据该策略执行。 


配置每种寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，需要打开“MME支持策略寻呼功能”License项。 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，不需要配置 “寻呼策略”参数项；选择“自定义寻呼”时，必须配置“寻呼策略”参数项。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值。
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼GUTI在周边TALIST范围寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:50。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:N/A。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。
IOTPAGEEN|物联网寻呼增强|参数可选性:任选参数；参数类型:复合参数|该参数用于设置物联网寻呼增强的三个参数。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”配置为“精准寻呼”时，该参数用于配置使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


设置如下的数据业务全局寻呼策略： 



 
GUTI(在TA LIST范围)寻呼次数：2次
 

 
IMSI(在TA LIST范围)寻呼次数：1次
 

 


配置成功后，MME后续执行寻呼业务时，依次执行基于GUTI(在TA LIST范围)寻呼策略2次、IMSI(在TA LIST范围)寻呼策略1次。 


SET MME GLOBAL PS PAGING POLICY:PAGETYPE="USER",PAGEPOLICY="GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"IMSITALIST"-50-"PRIO_255"-"RECENBLIST"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改数据业务全局寻呼策略(MOD MME GLOBAL PS PAGING POLICY) 
## 修改数据业务全局寻呼策略(MOD MME GLOBAL PS PAGING POLICY) 


[](None)命令功能 


该命令用于修改MME数据业务全局寻呼策略中某次寻呼的方式、寻呼间隔及优先级。需要指定修改全局策略中第几次寻呼。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGEINDEX|寻呼次序|参数可选性:必选参数；参数类型:整数；参数范围为:1~20。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼GUTI在周边TALIST范围寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。






[](None)命令举例 


修改数据业务全局寻呼策略，其中寻呼次序为1，寻呼方式为“最近活动eNB列表或邻接eNB列表寻呼”。 


MOD MME GLOBAL PS PAGING POLICY:PAGEINDEX=1,PAGESTYLE="LASTENBLIST"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询数据业务全局寻呼策略(SHOW MME GLOBAL PS PAGING POLICY) 
## 查询数据业务全局寻呼策略(SHOW MME GLOBAL PS PAGING POLICY) 


[](None)命令功能 


该命令用于查询MME数据业务全局寻呼策略。 




[](None)注意事项 


无 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGETYPES|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼GUTI在周边TALIST范围寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。






[](None)命令举例 


查询MME数据业务全局寻呼策略。 


SHOW MME GLOBAL PS PAGING POLICY; 


`
命令 (No.1): SHOW MME GLOBAL PS PAGING POLICY;

寻呼类型     寻呼次序   寻呼方式                寻呼时长(100ms)   寻呼优先级   eNB列表类型        携带寻呼无线能力   携带寻呼推荐小区信息   携带寻呼覆盖增强级别
------------------------------------------------------------------------------------------------------------------------------------------------------------------
自定义寻呼   1          最近活动eNB列表寻呼     50                N/A          最近活动eNB列表    不携带             不携带                 不携带
自定义寻呼   2          GUTI在TA LIST范围寻呼   50                N/A          最近活动eNB列表    不携带             不携带                 不携带
自定义寻呼   3          IMSI在TA LIST范围寻呼   50                N/A          最近活动eNB列表    不携带             不携带                 不携带
------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 3

命令执行成功（耗时 0.041 秒）。
` 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置CS语音业务全局寻呼策略(SET MME GLOBAL CS PAGING POLICY) 
## 设置CS语音业务全局寻呼策略(SET MME GLOBAL CS PAGING POLICY) 


[](None)命令功能 


该命令用于配置MME语音业务全局寻呼策略。系统存在默认的寻呼策略配置，当运营商根据自身网络状况，需要修改寻呼策略时，可以通过该命令配置。修改成功后，后续寻呼业务将根据该策略执行。 


ZXUN uMAC-MME目前所支持的语音业务寻呼策略的寻呼范围如下： 



 
在TA LIST范围内寻呼
 

 
在MME全局范围内寻呼
 

 


配置寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


MME根据寻呼策略中设定的寻呼范围进行寻呼。语音寻呼只尝试一次，重发由MSC控制。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:50。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。






[](None)命令举例 


设置全局的语音寻呼策略，其中寻呼方式为“GUTI在TA LIST范围寻呼”。 


SET MME GLOBAL CS PAGING POLICY:PAGEPOLICY="GUTITALIST"-50-"PRIO_255"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询CS语音业务全局寻呼策略(SHOW MME GLOBAL CS PAGING POLICY) 
## 查询CS语音业务全局寻呼策略(SHOW MME GLOBAL CS PAGING POLICY) 


[](None)命令功能 


该命令用于查询MME语音业务全局寻呼策略。 




[](None)注意事项 


无 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。






[](None)命令举例 


查询语音业务全局寻呼策略。 


SHOW MME GLOBAL CS PAGING POLICY; 


`
命令 (No.1): SHOW MME GLOBAL CS PAGING POLICY

寻呼次序   寻呼方式                寻呼时长(100ms)   寻呼优先级
---------------------------------------------------------------
1          GUTI在TA LIST范围寻呼   50                N/A
---------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.028 秒）。
` 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置短信业务全局寻呼策略(SET MME GLOBAL SMS PAGING POLICY) 
## 设置短信业务全局寻呼策略(SET MME GLOBAL SMS PAGING POLICY) 


[](None)命令功能 


该命令用于配置MME短信业务全局寻呼策略。系统存在默认的寻呼策略配置，当运营商根据自身网络状况，需要修改寻呼策略时，可以通过该命令配置。修改成功后，后续寻呼业务将根据该策略执行。 


配置寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，需要打开“MME支持策略寻呼功能”License项。 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，不需要配置 “寻呼策略”参数项；选择“自定义寻呼”时，必须配置“寻呼策略”参数项。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:50。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:N/A。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”配置为“精准寻呼”时，该参数用于配置使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


设置全局的短信寻呼策略，其中寻呼类型为自定义寻呼，寻呼方式为“最近一次活动eNodeB寻呼”。 


SET MME GLOBAL SMS PAGING POLICY:PAGETYPE="USER",PAGEPOLICY="LASTENB"-50-"PRIO_255"-"RECENBLIST"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改短信业务全局寻呼策略(MOD MME GLOBAL SMS PAGING POLICY) 
## 修改短信业务全局寻呼策略(MOD MME GLOBAL SMS PAGING POLICY) 


[](None)命令功能 


该命令用于修改MME短信业务全局寻呼策略中某次寻呼的方式、寻呼间隔及优先级。需要指定修改全局策略中第几次寻呼。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGEINDEX|寻呼次序|参数可选性:必选参数；参数类型:整数；参数范围为:1~20。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。






[](None)命令举例 


修改短信业务全局寻呼策略，其中寻呼次序为1，寻呼方式为“最近一次活动TA寻呼”。 


MOD MME GLOBAL SMS PAGING POLICY:PAGEINDEX=1,PAGESTYLE="LASTTA"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询短信业务全局寻呼策略(SHOW MME GLOBAL SMS PAGING POLICY) 
## 查询短信业务全局寻呼策略(SHOW MME GLOBAL SMS PAGING POLICY) 


[](None)命令功能 


该命令用于查询MME短信业务全局寻呼策略。 




[](None)注意事项 


无 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGETYPES|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。






[](None)命令举例 


查询短信业务全局寻呼策略。 


SHOW MME GLOBAL SMS PAGING POLICY; 


`
命令 (No.1): SHOW MME GLOBAL SMS PAGING POLICY

寻呼类型    寻呼次序  寻呼方式                寻呼时长(100ms)  寻呼优先级    eNB列表类型
-------------------------------------------------------------------------------------------
自定义寻呼  1         GUTI在TA LIST范围寻呼   50               N/A          最近活动eNB列表
-------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.044 秒）。
` 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置IDR业务全局寻呼策略(SET MME GLOBAL IDR PAGING POLICY) 
## 设置IDR业务全局寻呼策略(SET MME GLOBAL IDR PAGING POLICY) 


[](None)命令功能 


该命令用于配置MME IDR业务全局寻呼策略。系统存在默认的寻呼策略配置，当运营商根据自身网络状况，需要修改寻呼策略时，可以通过该命令配置。修改成功后，后续寻呼业务将根据该策略执行。 


配置每次寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，需要打开“MME支持策略寻呼功能”License项。 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，不需要配置 “寻呼策略”参数项；选择“自定义寻呼”时，必须配置“寻呼策略”参数项。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:50。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:N/A。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”配置为“精准寻呼”时，该参数用于配置使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


设置如下的IDR业务全局寻呼策略： 



 
GUTI(在TA LIST范围)寻呼次数：2次
 

 
IMSI(在TA LIST范围)寻呼次数：1次
 

 


配置成功后，MME后续执行寻呼业务时，依次执行基于GUTI(在TA LIST范围)寻呼策略2次、IMSI(在TA LIST范围)寻呼策略1次。 


SET MME GLOBAL IDR PAGING POLICY:PAGETYPE="USER",PAGEPOLICY="GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"IMSITALIST"-50-"PRIO_255"-"RECENBLIST"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改IDR业务全局寻呼策略(MOD MME GLOBAL IDR PAGING POLICY) 
## 修改IDR业务全局寻呼策略(MOD MME GLOBAL IDR PAGING POLICY) 


[](None)命令功能 


该命令用于修改MME IDR业务全局寻呼策略中某次寻呼的方式、寻呼间隔及优先级。需要指定修改全局策略中第几次寻呼。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGEINDEX|寻呼次序|参数可选性:必选参数；参数类型:整数；参数范围为:1~20。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。






[](None)命令举例 


修改IDR业务全局寻呼策略，其中寻呼次序为1，寻呼方式为“GUTI在TA LIST范围寻呼”。 


MOD MME GLOBAL IDR PAGING POLICY:PAGEINDEX=1,PAGESTYLE="GUTITALIST"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询IDR业务全局寻呼策略(SHOW MME GLOBAL IDR PAGING POLICY) 
## 查询IDR业务全局寻呼策略(SHOW MME GLOBAL IDR PAGING POLICY) 


[](None)命令功能 


该命令用于查询MME IDR业务全局寻呼策略。 




[](None)注意事项 


无 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGETYPES|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。






[](None)命令举例 


查询IDR业务全局寻呼策略。 


SHOW MME GLOBAL IDR PAGING POLICY; 


`
命令 (No.1): SHOW MME GLOBAL IDR PAGING POLICY

寻呼类型    寻呼次序   寻呼方式                寻呼时长(100ms) 寻呼优先级   eNB列表类型
-----------------------------------------------------------------------------------------
自定义寻呼  1          GUTI在TA LIST范围寻呼   50              N/A          最近活动eNB列表
自定义寻呼  2          GUTI在TA LIST范围寻呼   50              N/A          最近活动eNB列表 
自定义寻呼  3          IMSI在TA LIST范围寻呼   50              N/A          最近活动eNB列表 
-----------------------------------------------------------------------------------------
记录数 3

命令执行成功（耗时 0.037 秒）。
` 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置NB-IoT业务全局寻呼策略(SET MME GLOBAL NBIOT PAGING POLICY) 
## 设置NB-IoT业务全局寻呼策略(SET MME GLOBAL NBIOT PAGING POLICY) 


[](None)命令功能 


该命令用于配置NB-IoT业务全局寻呼策略。系统存在默认的寻呼策略配置，当运营商根据自身网络状况，需要修改寻呼策略时，可以通过该命令配置。修改成功后，后续寻呼业务将根据该策略执行。 


配置每种寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，需要打开“MME支持策略寻呼功能”License项。 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，不需要配置 “寻呼策略”参数项；选择“自定义寻呼”时，必须配置“寻呼策略”参数项。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值。
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:120。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:N/A。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。
IOTPAGEEN|物联网寻呼增强|参数可选性:任选参数；参数类型:复合参数|该参数用于设置物联网寻呼增强的三个参数。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”配置为“精准寻呼”时，该参数用于配置使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


设置如下的NB-IoT全局寻呼策略： 



 
GUTI(在TA LIST范围)寻呼次数：2次
 

 
IMSI(在TA LIST范围)寻呼次数：1次
 

 


配置成功后，MME后续执行寻呼业务时，依次执行基于GUTI(在TA LIST范围)寻呼策略2次、IMSI(在TA LIST范围)寻呼策略1次。 


SET MME GLOBAL NBIOT PAGING POLICY:PAGETYPE="USER",PAGEPOLICY="GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"IMSITALIST"-50-"PRIO_255"-"RECENBLIST"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改NB-IoT业务全局寻呼策略(MOD MME GLOBAL NBIOT PAGING POLICY) 
## 修改NB-IoT业务全局寻呼策略(MOD MME GLOBAL NBIOT PAGING POLICY) 


[](None)命令功能 


该命令用于修改MME NB-IoT业务全局寻呼策略中某次寻呼的方式、寻呼间隔及优先级。需要指定修改全局策略中第几次寻呼。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGEINDEX|寻呼次序|参数可选性:必选参数；参数类型:整数；参数范围为:1~20。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。






[](None)命令举例 


修改NB-IoT业务全局寻呼策略，其中寻呼次序为1，寻呼方式为“最近活动eNB列表或邻接eNB列表寻呼”。 


MOD MME GLOBAL NBIOT PAGING POLICY:PAGEINDEX=1,PAGESTYLE="LASTENBLIST"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询NB-IoT业务全局寻呼策略(SHOW MME GLOBAL NBIOT PAGING POLICY) 
## 查询NB-IoT业务全局寻呼策略(SHOW MME GLOBAL NBIOT PAGING POLICY) 


[](None)命令功能 


该命令用于查询NB-IoT业务全局寻呼策略。 




[](None)注意事项 


无 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PAGETYPES|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数用于配置MME使用最近活动eNB列表中的eNB寻呼，还是使用邻接eNB列表中的eNB寻呼。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。






[](None)命令举例 


查询NB-IoT业务全局寻呼策略。 


SHOW MME GLOBAL NBIOT PAGING POLICY; 


`
命令 (No.14): SHOW MME GLOBAL NBIOT PAGING POLICY

寻呼类型     寻呼次序   寻呼方式                寻呼时长(100ms)   寻呼优先级   eNB列表类型              携带寻呼无线能力   携带寻呼推荐小区信息   携带寻呼覆盖增强级别
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
自定义寻呼   1          GUTI在TA LIST范围寻呼   50                N/A          最近活动eNB列表          不携带             不携带                 不携带
自定义寻呼   2          GUTI在TA LIST范围寻呼   50                N/A          最近活动eNB列表          不携带             不携带                 不携带
自定义寻呼   3          IMSI在TA LIST范围寻呼   50                N/A          最近活动eNB列表          不携带             不携带                 不携带
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 3

命令执行成功（耗时 0.045 秒）。
` 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改邻接eNB寻呼策略(SET NEIGHBOR ENB PAGING POLICY) 
## 修改邻接eNB寻呼策略(SET NEIGHBOR ENB PAGING POLICY) 


[](None)命令功能 


该命令用于设置邻接eNB寻呼功能策略。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SUPNEIENBPAGING|支持邻接eNB寻呼功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持邻接eNB寻呼功能。
LOWMOBCHECK|仅低移动性下开启邻接eNB寻呼|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否仅支持对低移动性用户开启邻接eNB列表寻呼功能 。
ENBSTICKDURA|eNB粘性时长（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:1~3600。|该参数用于配置，在MME执行低移动性检查时，UE在一个eNB下驻留的时间阈值。UE在一个eNB下驻留的时间超过该参数配置的数值，才允许MME对其使用邻接eNB寻呼。
SONNEIENB|SON学习开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持eNodeB Configuration Transfer流程中学习邻接eNodeB关系的能力。
X2NEIENB|X2学习开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持X2-based Handover流程中学习邻接eNodeB关系的能力。
S1NEIENB|S1学习开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持S1-based Handover流程中学习邻接eNodeB关系的能力。
NEIENBEXPIRE|邻接eNodeB老化时间（分钟）|参数可选性:任选参数；参数类型:整数；参数范围为:0~129600。|该参数用于配置邻接eNodeB的老化时间。当超过老化时间，相邻eNodeB之间的关系记录将被删除。如果参数值为0，表示MME不执行老化检查。
LEARNTIME|学习eNodeB邻接关系保护时间（分钟）|参数可选性:任选参数；参数类型:整数；参数范围为:0~10080。|该参数用于配置MME获取eNodeB邻接关系的时间。在该时间段内，MME不允许使用邻接eNB寻呼功能。






[](None)命令举例 


修改邻接eNB寻呼策略，修改为不支持邻接eNB寻呼功能。 


SET NEIGHBOR ENB PAGING POLICY:SUPNEIENBPAGING="NO"; 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询邻接eNB寻呼策略(SHOW NEIGHBOR ENB PAGING POLICY) 
## 查询邻接eNB寻呼策略(SHOW NEIGHBOR ENB PAGING POLICY) 


[](None)命令功能 


该命令用于查询邻接eNB寻呼策略配置。 




[](None)注意事项 


无 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SUPNEIENBPAGING|支持邻接eNB寻呼功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持邻接eNB寻呼功能。
LOWMOBCHECK|仅低移动性下开启邻接eNB寻呼|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否仅支持对低移动性用户开启邻接eNB列表寻呼功能 。
ENBSTICKDURA|eNB粘性时长（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:1~3600。|该参数用于配置，在MME执行低移动性检查时，UE在一个eNB下驻留的时间阈值。UE在一个eNB下驻留的时间超过该参数配置的数值，才允许MME对其使用邻接eNB寻呼。
SONNEIENB|SON学习开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持eNodeB Configuration Transfer流程中学习邻接eNodeB关系的能力。
X2NEIENB|X2学习开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持X2-based Handover流程中学习邻接eNodeB关系的能力。
S1NEIENB|S1学习开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置MME是否支持S1-based Handover流程中学习邻接eNodeB关系的能力。
NEIENBEXPIRE|邻接eNodeB老化时间（分钟）|参数可选性:任选参数；参数类型:整数；参数范围为:0~129600。|该参数用于配置邻接eNodeB的老化时间。当超过老化时间，相邻eNodeB之间的关系记录将被删除。如果参数值为0，表示MME不执行老化检查。
LEARNTIME|学习eNodeB邻接关系保护时间（分钟）|参数可选性:任选参数；参数类型:整数；参数范围为:0~10080。|该参数用于配置MME获取eNodeB邻接关系的时间。在该时间段内，MME不允许使用邻接eNB寻呼功能。






[](None)命令举例 


查询邻接eNB寻呼策略。 


SHOW NEIGHBOR ENB PAGING POLICY; 


`
(No.2) : SHOW NEIGHBOR ENB PAGING POLICY
-----------------uMAC_MME_V7master/NFS_MMESGSN_0----------------
操作维护       支持邻接eNB寻呼功能 仅低移动性下开启邻接eNB寻呼 eNB粘性时长（秒） SON学习开关 X2学习开关 S1学习开关 邻接eNodeB老化时间（分钟） 学习eNodeB邻接关系保护时间（分钟） 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           否                  是                          600               是          是         是         21600                      3600                       
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1

执行成功开始时间:2021-11-24 15:00:48 耗时: 1.076秒
` 








父主题： [MME全局寻呼策略配置](../../zh-CN/tree/N_12522121.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MME寻呼策略配置 
# MME寻呼策略配置 


[](None)背景知识 


终端接入网络后，不发生语音或者数据业务时，为了省电，可以进入空闲状态，空闲状态下，MME与基站之间，基站与终端之间的无线侧连接被释放。处于空闲状态的终端无法接收下行数据，如果MME需要向空闲状态的终端发送下行数据，MME需要在特定区域内（比如，跟踪区列表）广播寻呼消息，终端侦听到寻呼消息后通过消息流程（比如，业务请求、跟踪区更新等）重新建立无线侧连接。终端进入连接状态，MME即可进行下行数据的发送。 


MME通过广播方式发送寻呼消息时，需要向特定区域内的所有eNodeB发送寻呼消息，再由eNodeB在空口广播寻呼消息。如果MME发送寻呼消息的区域范围内eNodeB较多时，寻呼的消息量较大。 




[](None)功能描述 


MME寻呼策略配置，适用于运营商根据自身网络状况及业务发展需要，为不同的特定的用户和终端，针对不同的业务场景，提供特定的寻呼策略，满足不同的寻呼量和寻呼时延的限制要求，提高寻呼成功率。 


本配置中增加的数据、语音、短信的寻呼策略，将由“寻呼策略因子配置”所引用，作为系统根据特定因子匹配的寻呼策略。如果匹配不到特定的寻呼策略，将使用全局寻呼策略。 




[](None)相关主题 



 

新增数据业务寻呼策略(ADD MME PS PAGING POLICY)
 

 

修改数据业务寻呼策略(SET MME PS PAGING POLICY)
 

 

删除数据业务寻呼策略(DEL MME PS PAGING POLICY)
 

 

查询数据业务寻呼策略(SHOW MME PS PAGING POLICY)
 

 

新增CS语音业务寻呼策略(ADD MME CS PAGING POLICY)
 

 

修改CS语音业务寻呼策略(SET MME CS PAGING POLICY)
 

 

删除CS语音业务寻呼策略(DEL MME CS PAGING POLICY)
 

 

查询CS语音业务寻呼策略(SHOW MME CS PAGING POLICY)
 

 

新增短信业务寻呼策略(ADD MME SMS PAGING POLICY)
 

 

修改短信业务寻呼策略(SET MME SMS PAGING POLICY)
 

 

删除短信业务寻呼策略(DEL MME SMS PAGING POLICY)
 

 

查询短信业务寻呼策略(SHOW MME SMS PAGING POLICY)
 

 

新增IDR业务寻呼策略(ADD MME IDR PAGING POLICY)
 

 

修改IDR业务寻呼策略(SET MME IDR PAGING POLICY)
 

 

删除IDR业务寻呼策略(DEL MME IDR PAGING POLICY)
 

 

查询IDR业务寻呼策略(SHOW MME IDR PAGING POLICY)
 

 

新增NB-IoT业务寻呼策略(ADD MME NBIOT PAGING POLICY)
 

 

修改NB-IoT业务寻呼策略(SET MME NBIOT PAGING POLICY)
 

 

删除NB-IoT业务寻呼策略(DEL MME NBIOT PAGING POLICY)
 

 

查询NB-IoT业务寻呼策略(SHOW MME NBIOT PAGING POLICY)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增数据业务寻呼策略(ADD MME PS PAGING POLICY) 
## 新增数据业务寻呼策略(ADD MME PS PAGING POLICY) 


[](None)命令功能 


该命令用于增加MME数据业务寻呼策略。如果运营商根据自身网络状况，需要根据特定的因子，配置特定的寻呼策略时，可以通过该命令增加数据业务寻呼策略。 


配置每次寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，需要打开“MME支持策略寻呼功能”License项。 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，不需要配置 “寻呼策略”参数项；选择“自定义寻呼”时，必须配置“寻呼策略”参数项。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:USER。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼GUTI在周边TALIST范围寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:50。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:N/A。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
IOTPAGEEN|物联网寻呼增强|参数可选性:任选参数；参数类型:复合参数|该参数用于设置物联网寻呼增强的三个参数。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”为“精准寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


新增数据业务寻呼策略。 


ADD MME PS PAGING POLICY:ID=51,PAGETYPE="USER",PAGEPOLICY="GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"IMSITALIST"-50-"PRIO_255"-"RECENBLIST"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改数据业务寻呼策略(SET MME PS PAGING POLICY) 
## 修改数据业务寻呼策略(SET MME PS PAGING POLICY) 


[](None)命令功能 


该命令用于修改MME数据业务寻呼策略中某次寻呼的方式、寻呼间隔及优先级。需要指定修改的策略编号及其中第几次寻呼。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼GUTI在周边TALIST范围寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”为“精准寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


修改数据业务寻呼策略。 


SET MME PS PAGING POLICY:ID=51,PAGEINDEX=2,PAGESTYLE="IMSIMME",PAGETIME=50,PAGEPRIO="PRIO_255"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除数据业务寻呼策略(DEL MME PS PAGING POLICY) 
## 删除数据业务寻呼策略(DEL MME PS PAGING POLICY) 


[](None)命令功能 


该命令用于删除MME数据业务寻呼策略。需要指定删除的策略编号。 




[](None)注意事项 


如果该寻呼策略已经被寻呼因子策略配置使用，则不能删除。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)命令举例 


删除数据业务寻呼策略，寻呼策略编号是51。 


DEL MME PS PAGING POLICY:ID=51; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询数据业务寻呼策略(SHOW MME PS PAGING POLICY) 
## 查询数据业务寻呼策略(SHOW MME PS PAGING POLICY) 


[](None)命令功能 


该命令用于查询MME数据业务寻呼策略。可以指定查询的策略编号。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼GUTI在周边TALIST范围寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。






[](None)命令举例 


查询数据业务寻呼策略。 


SHOW MME PS PAGING POLICY; 


`

命令 (No.1): SHOW MME PS PAGING POLICY

操作维护         寻呼策略编号   寻呼类型     寻呼次序   寻呼方式                寻呼时长(100ms)   寻呼优先级   eNB列表类型      携带寻呼无线能力   携带寻呼推荐小区信息   携带寻呼覆盖增强级别
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   112            自定义寻呼   1          用户当前CSG寻呼         50                N/A          最近活动eNB列表  携带               不携带                 不携带
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 1.498 秒）。
` 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增CS语音业务寻呼策略(ADD MME CS PAGING POLICY) 
## 新增CS语音业务寻呼策略(ADD MME CS PAGING POLICY) 


[](None)命令功能 


该命令用于增加MME语音业务寻呼策略。如果运营商根据自身网络状况，需要根据特定的因子，配置特定的寻呼策略时，可以通过该命令增加语音业务寻呼策略。 


配置寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


MME根据寻呼策略中设定的寻呼范围进行寻呼。语音寻呼只尝试一次，重发由MSC控制。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGEPOLICY|寻呼策略|参数可选性:必选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:50。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。






[](None)命令举例 


新增语音业务寻呼策略，寻呼策略编号是101，寻呼范围为GUTI在TA LIST范围寻呼。 


ADD MME CS PAGING POLICY:ID=101,PAGEPOLICY="GUTITALIST"-50-"PRIO_255"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改CS语音业务寻呼策略(SET MME CS PAGING POLICY) 
## 修改CS语音业务寻呼策略(SET MME CS PAGING POLICY) 


[](None)命令功能 


该命令用于修改MME语音业务寻呼策略中的寻呼方式、寻呼间隔及优先级。需要指定修改的策略编号。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。






[](None)命令举例 


修改语音业务寻呼策略。 


SET MME CS PAGING POLICY:ID=101,PAGESTYLE="GUTITALIST",PAGETIME=50,PAGEPRIO="PRIO_255"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除CS语音业务寻呼策略(DEL MME CS PAGING POLICY) 
## 删除CS语音业务寻呼策略(DEL MME CS PAGING POLICY) 


[](None)命令功能 


该命令用于删除MME语音业务寻呼策略。需要指定删除的策略编号。 




[](None)注意事项 


如果该寻呼策略已经被寻呼因子策略配置使用，则不能删除。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)命令举例 


删除语音业务寻呼策略，寻呼策略编号是101。 


DEL MME CS PAGING POLICY:ID=101; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询CS语音业务寻呼策略(SHOW MME CS PAGING POLICY) 
## 查询CS语音业务寻呼策略(SHOW MME CS PAGING POLICY) 


[](None)命令功能 


该命令用于查询MME语音业务寻呼策略。可以指定查询的策略编号。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略编号。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。






[](None)命令举例 


查询语音业务寻呼策略。 


SHOW MME CS PAGING POLICY; 


`

命令 (No.1): SHOW MME CS PAGING POLICY

操作维护         寻呼策略编号   寻呼次序   寻呼方式                寻呼时长(100ms)   寻呼优先级
-----------------------------------------------------------------------------------------------
复制 修改 删除   101            1          GUTI在TA LIST范围寻呼   50                N/A
-----------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.023 秒）。
` 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增短信业务寻呼策略(ADD MME SMS PAGING POLICY) 
## 新增短信业务寻呼策略(ADD MME SMS PAGING POLICY) 


[](None)命令功能 


该命令用于新增MME短信业务寻呼策略。如果运营商根据自身网络状况，需要根据特定的因子，配置特定的寻呼策略时，可以通过该命令增加短信业务寻呼策略。 


配置寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，需要打开“MME支持策略寻呼功能”License项。 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，不需要配置 “寻呼策略”参数项；选择“自定义寻呼”时，必须配置“寻呼策略”参数项。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:USER。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:50。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:N/A。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”为“精准寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


新增短信业务寻呼策略，寻呼策略编号是201。 


ADD MME SMS PAGING POLICY:ID=201,PAGETYPE="USER",PAGEPOLICY="LASTENB"-50-"PRIO_255"-"RECENBLIST"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改短信业务寻呼策略(SET MME SMS PAGING POLICY) 
## 修改短信业务寻呼策略(SET MME SMS PAGING POLICY) 


[](None)命令功能 


该命令用于修改MME短信业务寻呼策略中某次寻呼的方式、寻呼间隔及优先级。需要指定修改的策略编号及其中第几次寻呼。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”为“精准寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


修改短信业务寻呼策略，寻呼策略编号是201。 


SET MME SMS PAGING POLICY:ID=201,PAGEINDEX=1,PAGESTYLE="LASTENB",PAGETIME=50,PAGEPRIO="PRIO_255"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除短信业务寻呼策略(DEL MME SMS PAGING POLICY) 
## 删除短信业务寻呼策略(DEL MME SMS PAGING POLICY) 


[](None)命令功能 


该命令用于删除MME短信业务寻呼策略。需要指定删除的策略编号。 




[](None)注意事项 


如果该寻呼策略已经被寻呼因子策略配置使用，则不能删除。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)命令举例 


删除短信业务寻呼策略，寻呼策略编号是201。 


DEL MME SMS PAGING POLICY:ID=201; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询短信业务寻呼策略(SHOW MME SMS PAGING POLICY) 
## 查询短信业务寻呼策略(SHOW MME SMS PAGING POLICY) 


[](None)命令功能 


该命令用于查询MME短信业务寻呼策略。可以指定查询的策略编号。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


查询短信业务寻呼策略。 


SHOW MME SMS PAGING POLICY; 


`

命令 (No.1): SHOW MME SMS PAGING POLICY

操作维护         寻呼策略编号   寻呼类型     寻呼次序    寻呼方式               寻呼时长(100ms)   寻呼优先级   eNB列表类型 
-----------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   201            自定义寻呼   1           最近一次活动eNB寻呼    50                N/A          最近活动eNB列表
-----------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.021 秒）。
` 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增IDR业务寻呼策略(ADD MME IDR PAGING POLICY) 
## 新增IDR业务寻呼策略(ADD MME IDR PAGING POLICY) 


[](None)命令功能 


该命令用于增加MME IDR业务寻呼策略。如果运营商根据自身网络状况，需要根据特定的因子，配置特定的寻呼策略时，可以通过该命令增加数据业务寻呼策略。 


配置每次寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，需要打开“MME支持策略寻呼功能”License项。 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，不需要配置 “寻呼策略”参数项；选择“自定义寻呼”时，必须配置“寻呼策略”参数项。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:USER。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:50。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:N/A。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”为“精准寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


新增IDR业务寻呼策略。 


ADD MME IDR PAGING POLICY:ID=301,PAGETYPE="USER",PAGEPOLICY="GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"IMSITALIST"-50-"PRIO_255"-"RECENBLIST"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改IDR业务寻呼策略(SET MME IDR PAGING POLICY) 
## 修改IDR业务寻呼策略(SET MME IDR PAGING POLICY) 


[](None)命令功能 


该命令用于修改MME IDR业务寻呼策略中某次寻呼的方式、寻呼间隔及优先级。需要指定修改的策略编号及其中第几次寻呼。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”为“精准寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


修改IDR业务寻呼策略。 


SET MME IDR PAGING POLICY:ID=301,PAGEINDEX=2,PAGESTYLE="IMSIMME",PAGETIME=50,PAGEPRIO="PRIO_255"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除IDR业务寻呼策略(DEL MME IDR PAGING POLICY) 
## 删除IDR业务寻呼策略(DEL MME IDR PAGING POLICY) 


[](None)命令功能 


该命令用于删除MME IDR业务寻呼策略。需要指定删除的策略编号。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)命令举例 


删除IDR业务寻呼策略，寻呼策略编号是301。 


DEL MME IDR PAGING POLICY:ID=301; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询IDR业务寻呼策略(SHOW MME IDR PAGING POLICY) 
## 查询IDR业务寻呼策略(SHOW MME IDR PAGING POLICY) 


[](None)命令功能 


该命令用于查询MME IDR业务寻呼策略。可以指定查询的策略编号。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


查询IDR业务寻呼策略。 


SHOW MME IDR PAGING POLICY; 


`

命令 (No.1): SHOW MME IDR PAGING POLICY

操作维护         寻呼策略编号   寻呼类型    寻呼次序   寻呼方式                寻呼时长(100ms)   寻呼优先级   eNB列表类型 
--------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   301            自定义寻呼  1          GUTI在TA LIST范围寻呼   50                N/A          最近活动eNB列表
复制 修改 删除   301            自定义寻呼  2          IMSI在MME全局范围寻呼   50                N/A          最近活动eNB列表
--------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.037 秒）。
` 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增NB-IoT业务寻呼策略(ADD MME NBIOT PAGING POLICY) 
## 新增NB-IoT业务寻呼策略(ADD MME NBIOT PAGING POLICY) 


[](None)命令功能 


该命令用于增加NB-IoT业务寻呼策略。如果运营商根据自身网络状况，需要根据特定的因子，配置特定的寻呼策略时，可以通过该命令增加数据业务寻呼策略。 


配置每次寻呼方式的同时，可设置寻呼间隔及采用的寻呼优先级。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，需要打开“MME支持策略寻呼功能”License项。 


寻呼类型设置为“精准寻呼”或者“智能寻呼”时，不需要配置 “寻呼策略”参数项；选择“自定义寻呼”时，必须配置“寻呼策略”参数项。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:USER。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置寻呼使用的寻呼方式、寻呼间隔时长、及寻呼消息携带的优先级取值
PAGESTYLE|寻呼方式|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:必选参数；参数类型:整数；参数范围为:10~1200。默认值:120。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:PRIO_255。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:N/A。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
IOTPAGEEN|物联网寻呼增强|参数可选性:任选参数；参数类型:复合参数|该参数用于设置物联网寻呼增强的三个参数。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”为“精准寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


新增NB-IoT业务寻呼策略。 


ADD MME NBIOT PAGING POLICY:ID=51,PAGETYPE="USER",PAGEPOLICY="GUTITALIST"-50-"PRIO_255"-"RECENBLIST"&"IMSITALIST"-50-"PRIO_255"-"RECENBLIST"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改NB-IoT业务寻呼策略(SET MME NBIOT PAGING POLICY) 
## 修改NB-IoT业务寻呼策略(SET MME NBIOT PAGING POLICY) 


[](None)命令功能 


该命令用于修改NB-IoT业务寻呼策略中某次寻呼的方式、寻呼间隔及优先级。需要指定修改的策略编号及其中第几次寻呼。 


系统提供“精准寻呼”和“智能寻呼”两个寻呼模板，选择“精准寻呼”或者“智能寻呼”时，MME自动生成相应的寻呼策略。其中“精准寻呼”的寻呼次序为先eNB，然后eNB列表，最后是TALIST； “智能寻呼”的寻呼次序为先TA，然后TALIST。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:10~1200。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。
ACCENBLISTTYPE|精准寻呼时eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼类型”为“精准寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。






[](None)命令举例 


修改NB-IoT业务寻呼策略。 


SET MME NBIOT PAGING POLICY:ID=51,PAGEINDEX=2,PAGESTYLE="IMSIMME",PAGETIME=50,PAGEPRIO="PRIO_255"; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除NB-IoT业务寻呼策略(DEL MME NBIOT PAGING POLICY) 
## 删除NB-IoT业务寻呼策略(DEL MME NBIOT PAGING POLICY) 


[](None)命令功能 


该命令用于删除NB-IoT业务寻呼策略。需要指定删除的策略编号。 




[](None)注意事项 


如果该寻呼策略已经被寻呼因子策略配置使用，则不能删除。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)命令举例 


删除NB-IoT业务寻呼策略，寻呼策略编号是51。 


DEL MME NBIOT PAGING POLICY:ID=51; 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询NB-IoT业务寻呼策略(SHOW MME NBIOT PAGING POLICY) 
## 查询NB-IoT业务寻呼策略(SHOW MME NBIOT PAGING POLICY) 


[](None)命令功能 


该命令用于查询NB-IoT业务寻呼策略。可以指定查询的策略编号。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置寻呼策略编号。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ID|寻呼策略编号|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略编号。
PAGETYPE|寻呼类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼策略的类型，包括精准寻呼、智能寻呼、自定义寻呼。当选择精准寻呼或者智能寻呼时，MME自动生成相应的寻呼策略。
PAGEINDEX|寻呼次序|参数可选性:任选参数；参数类型:整数。|该参数用于标识进行的第几次寻呼。
PAGESTYLE|寻呼方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼采用的方式，可选择的寻呼方式如下：使用当前CSG寻呼使用用户CSG List寻呼基于最近一次活动eNB寻呼基于最近活动eNB列表寻呼基于最近一次活动TA寻呼基于最近活动TA列表寻呼在TA LIST范围内的GUTI寻呼在MME全局范围内的GUTI寻呼在TA LIST范围内的IMSI寻呼在MME全局范围内的IMSI寻呼
PAGETIME|寻呼时长(100ms)|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼间隔时长。
PAGEPRIO|寻呼优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置寻呼消息中携带优先级的取值，取值范围如下：0：PriorLevel11：PriorLevel22：PriorLevel33：PriorLevel44：PriorLevel55：PriorLevel66：PriorLevel77：PriorLevel8255：N/A当取值为N/A(255)时表示寻呼请求消息中不携带寻呼优先级字段。
ENBLISTTYPE|eNB列表类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|当参数“寻呼方式”为“基于最近活动eNB列表或邻接eNB列表寻呼”时，该参数标识使用最近活动eNB列表寻呼，还是使用邻接eNB列表寻呼。
PAGERADIOCAP|携带寻呼无线能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Paging Radio Capability信元。eNB可根据MME下发的Paging Radio Capability识别UE的相关特性完成寻呼。
PAGECELL|携带寻呼推荐小区信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data For Recommended Cells信元。eNB可根据MME下发的Recommended Cells在指定的小区内完成精确寻呼。
PAGECELLLEVEL|携带寻呼覆盖增强级别|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置寻呼时，是否携带Assistance Data for CE capable UEs信元。eNB可根据MME下发的UE之前所在小区的覆盖等级，完成覆盖增强寻呼。






[](None)命令举例 


查询NB-IoT业务寻呼策略。 


SHOW MME NBIOT PAGING POLICY; 


`

命令 (No.16): SHOW MME NBIOT PAGING POLICY;

操作维护         寻呼策略编号   寻呼类型     寻呼次序   寻呼方式                寻呼时长(100ms)   寻呼优先级   eNB列表类型         携带寻呼无线能力   携带寻呼推荐小区信息   携带寻呼覆盖增强级别
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   111            智能寻呼     1          最近一次活动TA寻呼      50                N/A          最近活动eNB列表     不携带             不携带                 不携带
复制 修改 删除   111            智能寻呼     2          最近活动TA列表寻呼      50                N/A          最近活动eNB列表     不携带             不携带                 不携带
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.023 秒）。
` 








父主题： [MME寻呼策略配置](../../zh-CN/tree/N_12522122.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MME寻呼策略因子配置 
# MME寻呼策略因子配置 


[](None)背景知识 


终端接入网络后，不发生语音或者数据业务时，为了省电，可以进入空闲状态，空闲状态下，MME与基站之间，基站与终端之间的无线侧连接被释放。处于空闲状态的终端无法接收下行数据，如果MME需要向空闲状态的终端发送下行数据，MME需要在特定区域内（比如，跟踪区列表）广播寻呼消息，终端侦听到寻呼消息后通过消息流程（比如，业务请求、跟踪区更新等）重新建立无线侧连接。终端进入连接状态，MME即可进行下行数据的发送。 


MME通过广播方式发送寻呼消息时，需要向特定区域内的所有eNodeB发送寻呼消息，再由eNodeB在空口广播寻呼消息。如果MME发送寻呼消息的区域范围内eNodeB较多时，寻呼的消息量较大。 




[](None)功能描述 


MME寻呼策略因子配置，适用于运营商根据自身网络状况及业务发展需要，为不同的特定的用户和终端，针对不同的业务场景，提供特定的寻呼策略，满足不同的寻呼量和寻呼时延的限制要求，提高寻呼成功率。 


本配置中配置的是各种不同的策略因子到特定的数据、语音、短信的寻呼策略的对应关系，这些因子包括：用户号段（MSISDN/IMSI）、终端类型（IMEI）、当前位置（TA）以及仅适用于专有承载建立和修改相关寻呼的当前APN和当前承载的QCI及寻呼策略指示位（PPI）。各种因子的组合关系及优先级按照从高到低排序如下： 






IMSI/MSIDN+IMEI+TA+APN+QCI+PPI 






IMSI/MSIDN+IMEI+TA+APN+QCI 






IMSI/MSIDN+IMEI+TA 






IMSI/MSIDN+IMEI+APN+QCI+PPI 






IMSI/MSIDN+IMEI+APN+QCI 






IMSI/MSIDN+IMEI+APN+PPI 






IMSI/MSIDN+IMEI+QCI+PPI 






IMSI/MSIDN+IMEI+APN 






IMSI/MSIDN+IMEI+QCI 






IMSI/MSIDN+IMEI+PPI 






IMSI/MSIDN+IMEI 






IMSI/MSIDN+TA 






IMSI/MSIDN+APN+QCI+PPI 






IMSI/MSIDN+APN+QCI 






IMSI/MSIDN+APN+PPI 






IMSI/MSIDN+QCI+PPI 






IMSI/MSIDN+APN 






IMSI/MSIDN+QCI 






IMSI/MSIDN+PPI 






IMSI/MSIDN 






IMEI+TA 






IMEI+APN+QCI+PPI 






IMEI+APN+QCI 






IMEI+APN+PPI 






IMEI+QCI+PPI 






IMEI+APN 






IMEI+QCI 






IMEI+PPI 






IMEI 






TA 






APN+QCI+PPI 






APN+QCI 






APN+PPI 






QCI+PPI 






APN 






QCI 






PPI 








[](None)相关主题 



 

新增MME寻呼策略因子(ADD MME PAGING POLICY FACTOR)
 

 

修改MME寻呼策略因子(SET MME PAGING POLICY FACTOR)
 

 

删除MME寻呼策略因子(DEL MME PAGING POLICY FACTOR)
 

 

查询MME寻呼策略因子(SHOW MME PAGING POLICY FACTOR)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增MME寻呼策略因子(ADD MME PAGING POLICY FACTOR) 
## 新增MME寻呼策略因子(ADD MME PAGING POLICY FACTOR) 


[](None)命令功能 


该命令用于新增MME寻呼策略因子配置。配置的是各种不同的策略因子到特定的数据、语音、短信的寻呼策略的对应关系，这些因子包括：用户号段（MSISDN/IMSI）、终端类型（IMEI）、当前位置（TA）以及仅适用于专有承载建立和修改相关寻呼的当前APN、当前承载的QCI及当前承载的PPI。可以使用一种或几种因子来选择寻呼策略，配置是只需要输入需要的因子即可；各种因子的组合关系及优先级（由高到低）如下： 




IMSI/MSIDN+IMEI+TA+APN+QCI+PPI 




IMSI/MSIDN+IMEI+TA+APN+QCI 




IMSI/MSIDN+IMEI+TA 




IMSI/MSIDN+IMEI+APN+QCI+PPI 




IMSI/MSIDN+IMEI+APN+QCI  




IMSI/MSIDN+IMEI+APN+PPI 




IMSI/MSIDN+IMEI+QCI+PPI 




IMSI/MSIDN+IMEI+APN 




IMSI/MSIDN+IMEI+QCI 




IMSI/MSIDN+IMEI+PPI 




IMSI/MSIDN+IMEI 




IMSI/MSIDN+TA 




IMSI/MSIDN+APN+QCI+PPI 




IMSI/MSIDN+APN+QCI  




IMSI/MSIDN+APN+PPI 




IMSI/MSIDN+QCI+PPI 




IMSI/MSIDN+APN 




IMSI/MSIDN+QCI 




IMSI/MSIDN+PPI 




IMSI/MSIDN 




IMEI+TA 




IMEI+APN+QCI+PPI 




IMEI+APN+QCI  




IMEI+APN+PPI 




IMEI+QCI+PPI 




IMEI+APN 




IMEI+QCI 




IMEI+PPI 




IMEI 




TA 




APN+QCI+PPI 




APN+QCI  




APN+PPI 




QCI+PPI 




APN 




QCI 




PPI 








[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERNUMIDX|IMSI/MSISDN号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:0~3072。默认值:0。|该参数用于配置寻呼策略的用户号段因子，该索引可被分析器入口为IMSI寻呼策略映射键值分析(配置命令ADD MDNAL)或MSISDN寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
IMEIIDX|IMEI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:0~3072。默认值:0。|该参数用于配置寻呼策略的终端类型因子，该索引可被分析器入口为IMEI寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
TAID|跟踪区标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|该参数用于配置寻呼策略的用户位置因子，该索引使用跟踪区配置（配置命令ADD TA）中已有配置的TAID参数；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。默认值:0。|该参数用于配置寻呼策略的QCI因子；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
APNNI|APNNI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。默认值:。|该参数用于配置寻呼策略的APNNI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的寻呼策略配置记录。
PPI|PPI|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。默认值:0。|该参数用于配置寻呼策略的PPI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过PPI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种PPI因子的寻呼策略配置记录。
PGPOLICYTYPE|寻呼策略类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置根据策略因子得到的寻呼策略的类型，是CS、PS、SMS、IDR还是NBIOT。
PGPOLICYID|策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置根据策略因子得到的寻呼策略编号。
PGPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置根据策略因子得到的寻呼策略。寻呼策略分为CS、PS、SMS、IDR和NB-IoT五种，由具体的策略编号标识。CS寻呼策略编号使用寻呼策略配置（配置命令ADD MME CS PAGING POLICY）中已有配置的语音业务寻呼策略的ID参数。PS寻呼策略编号使用寻呼策略配置（配置命令ADD MME PS PAGING POLICY）中已有配置的数据业务寻呼策略的ID参数。SMS寻呼策略编号使用寻呼策略配置（配置命令ADD MME SMS PAGING POLICY）中已有配置的短信业务寻呼策略的ID参数。IDR寻呼策略编号使用寻呼策略配置（配置命令ADD MME IDR PAGING POLICY）中已有配置的IDR业务寻呼策略的ID参数。NB-IoT寻呼策略编号使用寻呼策略配置（配置命令ADD MME NBIOT PAGING POLICY）中已有配置的NB-IoT业务寻呼策略的ID参数。






[](None)命令举例 


新增MME寻呼策略因子，IMSI/MSISDN号段索引为1，IMEI号段索引为1，寻呼策略类型为PS，策略编号为51。 


ADD MME PAGING POLICY FACTOR:USERNUMIDX=1,IMEIIDX=1,PGPOLICY="PS"-51; 








父主题： [MME寻呼策略因子配置](../../zh-CN/tree/N_12607041.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改MME寻呼策略因子(SET MME PAGING POLICY FACTOR) 
## 修改MME寻呼策略因子(SET MME PAGING POLICY FACTOR) 


[](None)命令功能 


该命令用于修改MME寻呼策略因子配置。需要指定特定的因子，修改指定记录的寻呼策略编号。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERNUMIDX|IMSI/MSISDN号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:0~3072。|该参数用于配置寻呼策略的用户号段因子，该索引可被分析器入口为IMSI寻呼策略映射键值分析(配置命令ADD MDNAL)或MSISDN寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
IMEIIDX|IMEI号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:0~3072。|该参数用于配置寻呼策略的终端类型因子，该索引可被分析器入口为IMEI寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
TAID|跟踪区标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置寻呼策略的用户位置因子，该索引使用跟踪区配置（配置命令ADD TA）中已有配置的TAID参数；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|该参数用于配置寻呼策略的QCI因子；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
APNNI|APNNI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于配置寻呼策略的APNNI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的寻呼策略配置记录。
PPI|PPI|参数可选性:必选参数；参数类型:整数；参数范围为:0~63。|该参数用于配置寻呼策略的PPI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过PPI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种PPI因子的寻呼策略配置记录。
PGPOLICYTYPE|寻呼策略类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于配置根据策略因子得到的寻呼策略的类型，是CS、PS、SMS、IDR还是NBIOT。
PGPOLICYID|策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:51~1024。|该参数用于配置根据策略因子得到的寻呼策略编号。
PGPOLICY|寻呼策略|参数可选性:任选参数；参数类型:复合参数|该参数用于配置根据策略因子得到的寻呼策略。寻呼策略分为CS、PS、SMS、IDR和NB-IoT五种，由具体的策略编号标识。CS寻呼策略编号使用寻呼策略配置（配置命令ADD MME CS PAGING POLICY）中已有配置的语音业务寻呼策略的ID参数。PS寻呼策略编号使用寻呼策略配置（配置命令ADD MME PS PAGING POLICY）中已有配置的数据业务寻呼策略的ID参数。SMS寻呼策略编号使用寻呼策略配置（配置命令ADD MME SMS PAGING POLICY）中已有配置的短信业务寻呼策略的ID参数。IDR寻呼策略编号使用寻呼策略配置（配置命令ADD MME IDR PAGING POLICY）中已有配置的IDR业务寻呼策略的ID参数。NB-IoT寻呼策略编号使用寻呼策略配置（配置命令ADD MME NBIOT PAGING POLICY）中已有配置的NB-IoT业务寻呼策略的ID参数。






[](None)命令举例 


修改MME寻呼策略因子，IMSI/MSISDN号段索引为1，IMEI号段索引为1，跟踪区标识为0，QCI为0，PPI为0，将寻呼策略修改为“编号为101的CS寻呼”。 


SET MME PAGING POLICY FACTOR:USERNUMIDX=1,IMEIIDX=1,TAID=0,QCI=0,PPI=0,PGPOLICY="CS"-101; 








父主题： [MME寻呼策略因子配置](../../zh-CN/tree/N_12607041.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除MME寻呼策略因子(DEL MME PAGING POLICY FACTOR) 
## 删除MME寻呼策略因子(DEL MME PAGING POLICY FACTOR) 


[](None)命令功能 


该命令用于删除MME寻呼策略因子配置。需要指定特定的因子，删除指定记录。如果该记录的USERNUMIDX或IMEIIDX已经被号码分析使用，则不能删除。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERNUMIDX|IMSI/MSISDN号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:0~3072。|该参数用于配置寻呼策略的用户号段因子，该索引可被分析器入口为IMSI寻呼策略映射键值分析(配置命令ADD MDNAL)或MSISDN寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
IMEIIDX|IMEI号段索引|参数可选性:必选参数；参数类型:整数；参数范围为:0~3072。|该参数用于配置寻呼策略的终端类型因子，该索引可被分析器入口为IMEI寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
TAID|跟踪区标识|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置寻呼策略的用户位置因子，该索引使用跟踪区配置（配置命令ADD TA）中已有配置的TAID参数；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
QCI|QCI|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|该参数用于配置寻呼策略的QCI因子；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
APNNI|APNNI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于配置寻呼策略的APNNI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的寻呼策略配置记录。
PPI|PPI|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数用于配置寻呼策略的PPI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过PPI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种PPI因子的寻呼策略配置记录。






[](None)命令举例 


删除MME寻呼策略因子，IMSI/MSISDN号段索引为1，IMEI号段索引为1，跟踪区标识为0，QCI为0，PPI为0的记录。 


DEL MME PAGING POLICY FACTOR:USERNUMIDX=1,IMEIIDX=1,TAID=0,QCI=0,PPI=0; 








父主题： [MME寻呼策略因子配置](../../zh-CN/tree/N_12607041.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询MME寻呼策略因子(SHOW MME PAGING POLICY FACTOR) 
## 查询MME寻呼策略因子(SHOW MME PAGING POLICY FACTOR) 


[](None)命令功能 


该命令用于查询MME寻呼策略因子配置。可以指定特定的因子，查询对应的寻呼策略。如果不指定某个特定因子，则表示对该因子进行通配查询。 




[](None)注意事项 


无 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERNUMIDX|IMSI/MSISDN号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:0~3072。|该参数用于配置寻呼策略的用户号段因子，该索引可被分析器入口为IMSI寻呼策略映射键值分析(配置命令ADD MDNAL)或MSISDN寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
IMEIIDX|IMEI号段索引|参数可选性:任选参数；参数类型:整数；参数范围为:0~3072。|该参数用于配置寻呼策略的终端类型因子，该索引可被分析器入口为IMEI寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
TAID|跟踪区标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|该参数用于配置寻呼策略的用户位置因子，该索引使用跟踪区配置（配置命令ADD TA）中已有配置的TAID参数；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
QCI|QCI|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于配置寻呼策略的QCI因子；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
APNNI|APNNI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~61个字符。|该参数用于配置寻呼策略的APNNI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的寻呼策略配置记录。
PPI|PPI|参数可选性:任选参数；参数类型:整数；参数范围为:0~63。|该参数用于配置寻呼策略的PPI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过PPI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种PPI因子的寻呼策略配置记录。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
USERNUMIDX|IMSI/MSISDN号段索引|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略的用户号段因子，该索引可被分析器入口为IMSI寻呼策略映射键值分析(配置命令ADD MDNAL)或MSISDN寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
IMEIIDX|IMEI号段索引|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略的终端类型因子，该索引可被分析器入口为IMEI寻呼策略映射键值分析(配置命令ADD MDNAL)的号码分析结果索引使用；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
TAID|跟踪区标识|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略的用户位置因子，该索引使用跟踪区配置（配置命令ADD TA）中已有配置的TAID参数；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
QCI|QCI|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略的QCI因子；如果不需要通过当前因子选择寻呼策略，则可不使用该参数。
APNNI|APNNI|参数可选性:任选参数；参数类型:字符型。|该参数用于配置寻呼策略的APNNI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过APNNI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种APNNI因子的寻呼策略配置记录。
PPI|PPI|参数可选性:任选参数；参数类型:整数。|该参数用于配置寻呼策略的PPI因子。在ADD/SET命令中，如果配置的寻呼策略不需要通过PPI因子进行选择，则可不使用该参数；在SHOW命令中，如果不使用该参数，表示通配查询各种PPI因子的寻呼策略配置记录。
PGPOLICY|寻呼策略|参数可选性:任选参数；参数类型:字符型。|该参数用于配置根据策略因子得到的寻呼策略。寻呼策略分为CS、PS、SMS、IDR和NB-IoT五种，由具体的策略编号标识。CS寻呼策略编号使用寻呼策略配置（配置命令ADD MME CS PAGING POLICY）中已有配置的语音业务寻呼策略的ID参数。PS寻呼策略编号使用寻呼策略配置（配置命令ADD MME PS PAGING POLICY）中已有配置的数据业务寻呼策略的ID参数。SMS寻呼策略编号使用寻呼策略配置（配置命令ADD MME SMS PAGING POLICY）中已有配置的短信业务寻呼策略的ID参数。IDR寻呼策略编号使用寻呼策略配置（配置命令ADD MME IDR PAGING POLICY）中已有配置的IDR业务寻呼策略的ID参数。NB-IoT寻呼策略编号使用寻呼策略配置（配置命令ADD MME NBIOT PAGING POLICY）中已有配置的NB-IoT业务寻呼策略的ID参数。






[](None)命令举例 


查询MME寻呼策略因子。 


SHOW MME PAGING POLICY FACTOR 


`

命令 (No.1): SHOW MME PAGING POLICY FACTOR

操作维护         IMSI/MSISDN号段索引   IMEI号段索引   跟踪区标识   QCI     APNNI   PPI     寻呼策略
---------------------------------------------------------------------------------------------------
复制 修改 删除   1                     1              0            0               0       PS-51
复制 修改 删除   2                     2              0            0               0       PS-51&CS-101&SMS-201
---------------------------------------------------------------------------------------------------
记录数 2

命令执行成功（耗时 0.027 秒）。
` 








父主题： [MME寻呼策略因子配置](../../zh-CN/tree/N_12607041.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SGSN其他HPLMN配置 
# SGSN其他HPLMN配置 


[](None)背景知识 


HPLMN（Home Public Land Mobile Network，本地公用陆地移动网络） ，是UE归属的PLMN，也就是说，UE的IMSI号中包含的MCC和MNC与HPLMN上的MCC和MNC是一致的。 


运营商可以配置多个PLMN，UE的IMSI号码根据PLMN的不同，MCC和MNC也不同。 




[](None)功能描述 



                SGSN支持多PLMN，“本局移动数据”中配置的PLMN（MCC+MNC）和“SGSN其他HPLMN配置控制“（命令为：
                [ADD HPLMNCFG](../mml/1260105.html)
                ）中配置的PLMN一起组成了SGSN支持的全部SGSN HPLMN列表。SGSN HPLMN列表用于本SGSN判断接入用户是否属于漫游用户，判断规则如下。
            




若从接入用户IMSI中提取的PLMN在全部SGSN HPLMN列表范围内，那么该用户在计费、漫游管理上将被当作本局归属用户处理。 


若从接入用户IMSI中提取的移动国家码MCC与全部SGSN HPLMN列表中配置的某个移动国家码匹配，那么该用户在计费、漫游管理上将被当作国内漫游用户处理，否则该用户在计费、漫游管理上将被当作国际漫游用户处理。 






[](None)相关主题 



 

新增本局SGSN其他HPLMN配置(ADD HPLMNCFG)
 

 

修改本局SGSN其他HPLMN配置(SET HPLMNCFG)
 

 

删除本局SGSN其他HPLMN配置(DEL HPLMNCFG)
 

 

查询本局SGSN其他HPLMN配置(SHOW HPLMNCFG)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增本局其他HPLMN配置(ADD HPLMNCFG) 
## 新增本局其他HPLMN配置(ADD HPLMNCFG) 


[](None)命令功能 


该命令用于新增本局SGSN的其他HPLMN配置。当需要本局SGSN同时服务于两个或两个以上的PLMN时，使用该命令。该命令配置成功后，增加的多个PLMN和“移动数据配置”中的配置的PLMN构成了全部SGSN HPLMN列表，这些HPLMN列表下的用户在计费、漫游管理上以本局归属用户的方式进行管理。 




若从接入用户IMSI中提取的PLMN在全部SGSN HPLMN列表范围内，那么该用户被当作本局归属用户处理。 


若从接入用户IMSI中提取的移动国家码MCC与全部SGSN HPLMN列表中配置的某个移动国家码匹配，那么该用户在计费、漫游管理上将被当作国内漫游用户处理，否则该用户在计费、漫游管理上将被当作国际漫游用户处理。 






[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动网号，如中国移动使用02（460-02）。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






[](None)命令举例 


增加本局SGSN其他HPLMN配置，设置移动国家码为460，移动网号为001。 


ADD HPLMNCFG:MCC="460",MNC="001"; 








父主题： [SGSN其他HPLMN配置](../../zh-CN/tree/N_1254213.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改本局其他HPLMN配置(SET HPLMNCFG) 
## 修改本局其他HPLMN配置(SET HPLMNCFG) 


[](None)命令功能 

该命令用于修改本局SGSN其他HPLMN配置。当需要修改本SGSN服务的其他HPLMN信息，包括MCC、MNC或该PLMN的别名时，使用该命令。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动网号，如中国移动使用02（460-02）。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






[](None)命令举例 


修改移动国家码为460，移动网号为001的本局SGSN其他HPLMN配置，将用户别名修改为hhh。 


SET HPLMNCFG:MCC="460",MNC="001",NAME="hhh"; 








父主题： [SGSN其他HPLMN配置](../../zh-CN/tree/N_1254213.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除本局其他HPLMN配置(DEL HPLMNCFG) 
## 删除本局其他HPLMN配置(DEL HPLMNCFG) 


[](None)命令功能 

该命令用于删除本局SGSN其他HPLMN配置。当本SGSN不需要为指定PLMN服务时，可以通过此命令删除。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动网号，如中国移动使用02（460-02）。






[](None)命令举例 


删除移动国家码为460，移动网号为001的本局SGSN其他HPLMN配置。 


DEL HPLMNCFG:MCC="460",MNC="001"; 








父主题： [SGSN其他HPLMN配置](../../zh-CN/tree/N_1254213.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询本局其他HPLMN配置(SHOW HPLMNCFG) 
## 查询本局其他HPLMN配置(SHOW HPLMNCFG) 


[](None)命令功能 

该命令用于查询本局SGSN其他HPLMN配置，显示本SGSN服务的其他HPLMN信息列表，包括MCC、MNC或PLMN的别名。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动网号，如中国移动使用02（460-02）。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的其他移动网号，如中国移动使用02（460-02）。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






[](None)命令举例 


查询所有的本局SGSN其他HPLMN配置。 


SHOW HPLMNCFG; 


`

命令 (No.1): SHOW HPLMNCFG

操作维护         移动国家码   移动网号   用户别名
-------------------------------------------------
复制 修改 删除   460          001        
-------------------------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [SGSN其他HPLMN配置](../../zh-CN/tree/N_1254213.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MME其他HPLMN配置 
# MME其他HPLMN配置 


[](None)背景知识 


HPLMN（Home Public Land Mobile Network，本地公用陆地移动网络） ，是UE归属的PLMN，也就是说，UE的IMSI号中包含的MCC和MNC与HPLMN上的MCC和MNC是一致的。 


运营商可以配置多个PLMN，UE的IMSI号码根据PLMN的不同，MCC和MNC也不同。 




[](None)功能描述 



                MME支持多PLMN，“本局移动数据”中配置的PLMN（MCC+MNC）和“MME其他HPLMN配置控制“（命令为：
                [ADD MME HPLMNCFG](../mml/1260235.html)
                ）中配置的PLMN一起组成了MME支持的全部MME HPLMN列表。MME HPLMN列表用于本MME判断接入用户是否属于漫游用户，判断规则如下。
            




若从接入用户IMSI中提取的PLMN在全部MME HPLMN列表范围内，那么该用户在漫游管理上将被当作本局归属用户处理。 


若从接入用户IMSI中提取的移动国家码MCC与全部MME HPLMN列表中配置的某个移动国家码匹配，那么该用户在漫游管理上将被当作国内漫游用户处理，否则该用户被当作国际漫游用户处理。 






[](None)相关主题 



 

新增本局MME其他HPLMN配置(ADD MME HPLMNCFG)
 

 

修改本局MME其他HPLMN配置(SET MME HPLMNCFG)
 

 

删除本局MME其他HPLMN配置(DEL MME HPLMNCFG)
 

 

查询本局MME其他HPLMN配置(SHOW MME HPLMNCFG)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增本局MME其他HPLMN配置(ADD MME HPLMNCFG) 
## 新增本局MME其他HPLMN配置(ADD MME HPLMNCFG) 


[](None)命令功能 


该命令用于新增本局MME其他HPLMN配置。当需要本局MME同时服务于两个或两个以上的PLMN时，使用该命令。该命令配置成功后，增加的多个PLMN和“移动数据配置”中的配置的PLMN构成了全部MME HPLMN列表。 




若从接入用户IMSI中提取的PLMN在全部MME HPLMN列表范围内，那么该用户在漫游管理上将被当作本局归属用户处理。 


若从接入用户IMSI中提取的移动国家码MCC与全部MME HPLMN列表中配置的某个移动国家码匹配，那么该用户在漫游管理上将被当作国内漫游用户处理，否则该用户被当作国际漫游用户处理。 






[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动网号，如中国移动使用02（460-02）。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






[](None)命令举例 


新增MME其他HPLMN配置,移动国家码460, 移动网号02 用户别名460-02。 


ADD MME HPLMNCFG:MCC="460",MNC="02",NAME="460-02";
 








父主题： [MME其他HPLMN配置](../../zh-CN/tree/N_12602351.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改本局MME其他HPLMN配置(SET MME HPLMNCFG) 
## 修改本局MME其他HPLMN配置(SET MME HPLMNCFG) 


[](None)命令功能 


该命令用于修改本局MME其他HPLMN配置。当需要修改本MME服务的其他HPLMN信息，包括MCC、MNC或该PLMN的别名时，使用该命令。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动网号，如中国移动使用02（460-02）。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






[](None)命令举例 


修改MME其他HPLMN配置,移动国家码460, 移动网号02的用户别名为460-02 


SET MME HPLMNCFG:MCC="460",MNC="02",NAME="46002";
 








父主题： [MME其他HPLMN配置](../../zh-CN/tree/N_12602351.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除本局MME其他HPLMN配置(DEL MME HPLMNCFG) 
## 删除本局MME其他HPLMN配置(DEL MME HPLMNCFG) 


[](None)命令功能 


该命令用于删除本局MME其他HPLMN配置。当本MME不需要为指定PLMN服务时，可以通过此命令删除。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动网号，如中国移动使用02（460-02）。






[](None)命令举例 


删除MME其他HPLMN配置,移动国家码460, 移动网号02 记录 


DEL MME HPLMNCFG:MCC="460",MNC="02";
 








父主题： [MME其他HPLMN配置](../../zh-CN/tree/N_12602351.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询本局MME其他HPLMN配置(SHOW MME HPLMNCFG) 
## 查询本局MME其他HPLMN配置(SHOW MME HPLMNCFG) 


[](None)命令功能 


该命令用于查询本局MME其他HPLMN配置，显示本MME服务的其他HPLMN信息列表，包括MCC、MNC或PLMN的别名。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动网号，如中国移动使用02（460-02）。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的其他移动网号，如中国移动使用02（460-02）。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|起注释作用，对此项命令配置并没有影响。当新增或修改此配置时，如果配置人员有需要特别说明的内容，可以填写在此处。






[](None)命令举例 


查询已经配置的MME其他HPLMN信息 


SHOW MME HPLMNCFG; 


`

命令 (No.1): SHOW MME HPLMNCFG

操作维护         移动国家码   移动网号   用户别名
-------------------------------------------------
复制 修改 删除   460          02         46002
-------------------------------------------------
记录数 1

命令执行成功（耗时 0.024 秒）。
` 








父主题： [MME其他HPLMN配置](../../zh-CN/tree/N_12602351.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 本局支持的其他GUMMEI配置 
# 本局支持的其他GUMMEI配置 


[](None)背景知识 


GUMMEI（Globally Unique MME Identifier，全球唯一MME标识），由MCC（Mobile Country Code，移动国家码）、MNC（Mobile Network Code，移动网码）以及MMEI（MME Identifier，MME标识）组成。 


MMEI由MMEGI（MME Group ID，MME组标识）和MMEC（MME Code，MME编码）组成；MMEGI长度为16比特，MMEC长度为8比特。 


一个MME实体，一般只需要一个GUMMEI。运营商出于运维和组网的特殊要求，也可以为一个MME实体分配多个GUMMEI。 




[](None)功能描述 



                “本局移动数据”配置（配置命令：SET MMECFG 或
                [SET COMBOCFG](../mml/1260006.html)
                ）中，进行本局的GUMMEI配置；在此基础上，“本局支持的其他GUMMEI配置”可提供本局其他GUMMEI的配置功能。
            


运营商规划GUMMEI时，应保证MMEC在MME POOL内唯一。 




[](None)相关主题 



 

新增本局其他GUMMEI配置(ADD GUMMEI)
 

 

修改本局其他GUMMEI配置(SET GUMMEI)
 

 

删除本局其他GUMMEI配置(DEL GUMMEI)
 

 

查询本局其他GUMMEI配置(SHOW GUMMEI)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增本局其他GUMMEI配置(ADD GUMMEI) 
## 新增本局其他GUMMEI配置(ADD GUMMEI) 


[](None)命令功能 


该命令用于新增本局支持的其他GUMMEI配置，如果运营商需要给其他运营商设定网络共享时，根据规划追加该配置。其中PLMN编号必须包含在本局移动数据配置的PLMN或本局其它HPLMN中。配置追加后，新追加的GUMMEI所对应的用户被认为是本局用户。 




[](None)注意事项 


查询本局移动数据配置命令：SHOW MMECFG或[SHOW COMBOCFG](1260007.html)


查询本局其他PLMN配置命令：[SHOW HPLMNCFG](1260108.html)




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GUMMEI|GUMMEI标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|GUMMEI（Globally Unique MME Identifier，全球唯一MME标识）由MCC（Mobile Country Code，移动国家码）、MNC（Mobile Network Code，移动网码）以及MMEI（MME Identifier，MME标识）组成。MMEI由MMEGI（MME Group ID，MME组标识）和MMEC（MME Code，MME编码）组成，MMEGI长度为16比特，MMEC长度为8比特。
USERLABEL|用户别名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|用户别名，由用户自定义，便于记忆和识别。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
PLMN|PLMN编号|参数可选性:必选参数；参数类型:复合参数|公共陆地移动（通信）网络。在某个国家或地区，某个运营商的某种制式的蜂窝移动通信网络被称为PLMN。
MMEGID|MME组ID|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|MME组ID，同一组的MME使用同一MME组ID。
MMEC|MME编号|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|MME编号,同一组内的MME使用MME编号来区分彼此。






[](None)命令举例 


配置本局其他GUMMEI，设置用户别名为1，移动国家码为460，移动网号为01，MME组ID为1，MME编号为1。
ADD GUMMEI:USERLABEL="1",PLMN="460"-"01",MMEGID=1,MMEC=1; 








父主题： [本局支持的其他GUMMEI配置](../../zh-CN/tree/N_12542131.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改本局其他GUMMEI配置(SET GUMMEI) 
## 修改本局其他GUMMEI配置(SET GUMMEI) 


[](None)命令功能 


该命令用于修改本局支持的其他GUMMEI配置，通过输入GUMMEI标识来修改该GUMMEI对应的参数。可以修改PLMN编号（PLMN编号必须包含在本局移动数据配置的PLMN或本局其它HPLMN中）、MME组ID、MME编号和用户别名。 




[](None)注意事项 


查询本局移动数据配置命令：SHOW MMECFG或[SHOW COMBOCFG](1260007.html)


查询本局其他PLMN配置命令：[SHOW HPLMNCFG](1260108.html)




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GUMMEI|GUMMEI标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|GUMMEI（Globally Unique MME Identifier，全球唯一MME标识）由MCC（Mobile Country Code，移动国家码）、MNC（Mobile Network Code，移动网码）以及MMEI（MME Identifier，MME标识）组成。MMEI由MMEGI（MME Group ID，MME组标识）和MMEC（MME Code，MME编码）组成，MMEGI长度为16比特，MMEC长度为8比特。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户别名，由用户自定义，便于记忆和识别。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|移动国家码用来唯一识别移动用户所属的国家，由ITU统一分配和管理。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|移动网络编码是不同移动网络的代码，用户以此区分不同的移动网络。
PLMN|PLMN编号|参数可选性:任选参数；参数类型:复合参数|公共陆地移动（通信）网络。在某个国家或地区，某个运营商的某种制式的蜂窝移动通信网络被称为PLMN。
MMEGID|MME组ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|MME组ID，同一组的MME使用同一MME组ID。
MMEC|MME编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|MME编号,同一组内的MME使用MME编号来区分彼此。






[](None)命令举例 


修改GUMMEI标识为1的PLMN数据，修改为46011。
SET GUMMEI:GUMMEI=1,PLMN="460"-"11"; 








父主题： [本局支持的其他GUMMEI配置](../../zh-CN/tree/N_12542131.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除本局其他GUMMEI配置(DEL GUMMEI) 
## 删除本局其他GUMMEI配置(DEL GUMMEI) 


[](None)命令功能 


该命令用于删除本局支持的其他GUMMEI配置，通过输入GUMMEI标识来删除该GUMMEI的配置。删除的GUMMEI所对应的用户被认为不是本局用户。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GUMMEI|GUMMEI标识|参数可选性:必选参数；参数类型:整数；参数范围为:1~32。|GUMMEI（Globally Unique MME Identifier，全球唯一MME标识）由MCC（Mobile Country Code，移动国家码）、MNC（Mobile Network Code，移动网码）以及MMEI（MME Identifier，MME标识）组成。MMEI由MMEGI（MME Group ID，MME组标识）和MMEC（MME Code，MME编码）组成，MMEGI长度为16比特，MMEC长度为8比特。






[](None)命令举例 


删除GUMMEI标识为1的本局其他GUMMEI配置。
DEL GUMMEI:GUMMEI=1; 








父主题： [本局支持的其他GUMMEI配置](../../zh-CN/tree/N_12542131.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询本局其他GUMMEI配置(SHOW GUMMEI) 
## 查询本局其他GUMMEI配置(SHOW GUMMEI) 


[](None)命令功能 


该命令用于查询本局支持的其他GUMMEI配置，可输入指定GUMMEI标识查询该GUMMEI的配置，如果不输入参数则查询全部GUMMEI的配置。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GUMMEI|GUMMEI标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~32。|GUMMEI（Globally Unique MME Identifier，全球唯一MME标识）由MCC（Mobile Country Code，移动国家码）、MNC（Mobile Network Code，移动网码）以及MMEI（MME Identifier，MME标识）组成。MMEI由MMEGI（MME Group ID，MME组标识）和MMEC（MME Code，MME编码）组成，MMEGI长度为16比特，MMEC长度为8比特。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GUMMEI|GUMMEI标识|参数可选性:任选参数；参数类型:整数。|GUMMEI（Globally Unique MME Identifier，全球唯一MME标识）由MCC（Mobile Country Code，移动国家码）、MNC（Mobile Network Code，移动网码）以及MMEI（MME Identifier，MME标识）组成。MMEI由MMEGI（MME Group ID，MME组标识）和MMEC（MME Code，MME编码）组成，MMEGI长度为16比特，MMEC长度为8比特。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型。|用户别名，由用户自定义，便于记忆和识别。
PLMN|PLMN编号|参数可选性:任选参数；参数类型:字符型。|公共陆地移动（通信）网络。在某个国家或地区，某个运营商的某种制式的蜂窝移动通信网络被称为PLMN。
MMEGID|MME组ID|参数可选性:任选参数；参数类型:字符型。|MME组ID，同一组的MME使用同一MME组ID。
MMEC|MME编号|参数可选性:任选参数；参数类型:字符型。|MME编号,同一组内的MME使用MME编号来区分彼此。






[](None)命令举例 


查询所有的本局其他GUMMEI配置。
SHOW GUMMEI; 


`

命令 (No.1): SHOW GUMMEI;

操作维护         GUMMEI标识   用户别名   PLMN编号     MME组ID   MME编号
-----------------------------------------------------------------------
复制 修改 删除   1            1			 "460"-"01"   1         1         
-----------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.043 秒）。
` 








父主题： [本局支持的其他GUMMEI配置](../../zh-CN/tree/N_12542131.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 3位MNC运营商信息配置 
# 3位MNC运营商信息配置 


[](None)背景知识 


IMSI由MCC、MNC、MSIN三部分组成。 


MCC：移动国家码，固定为3位十进制数字，用于唯一标识一个国家。 


MNC：移动网号，由2位或者3位十进制数字组成，用于标识移动用户的归属PLMN。 


MSIN：移动台标识号码，MSIN在PLMN内标识一个移动用户。 


不同的国家，采用的MNC位长不一定相同，可以是2位或者3位，但同一国家内，MNC的长度通常只有一种，或者2位，或者3位。 




[](None)功能描述 


SGSN/MME从用户的IMSI号码中解析MNC时，需要根据本配置判断IMSI中的MNC是2位还是3位；如果IMSI中的MCC和3位MNC能够匹配到配置记录，则认为用户归属的PLMN使用3位的MNC；如果匹配不到，则认为用户归属的PLMN使用2位的MNC。 


大多数的PLMN都采用了2位的MNC。这里需要配置所有归属和漫游用户中，使用3位MNC的MCC和MNC记录。 




[](None)相关主题 



 

新增3位MNC运营商信息配置(ADD 3 MNC OPERATOR)
 

 

修改3位MNC运营商信息配置(SET 3 MNC OPERATOR)
 

 

删除3位MNC运营商信息配置(DEL 3 MNC OPERATOR)
 

 

查询3位MNC运营商信息配置(SHOW 3 MNC OPERATOR)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增3位MNC运营商信息配置(ADD 3 MNC OPERATOR) 
## 新增3位MNC运营商信息配置(ADD 3 MNC OPERATOR) 


[](None)命令功能 


该命令用于配置MCC（Mobile Country Code，移动国家码）和3位MNC（Mobile Network Code，移动网络号）对应的运营商信息配置。 


MNC和MCC共同组成PLMN（Public Land Mobile Network，公共陆地移动网），PLMN被包含在用户的IMSI（International Mobile Subscriber Identity，国际移动用户标识）之中。 


按照3GPP规范，MNC的位数不是固定的，可能是2位，也可能是3位。因此，SGSN/MME网元将无法从IMSI中获取到MNC从而判断出用户归属的PLMN。为了能够从IMSI中提取到MNC和MCC，需要通过本命令配置MCC和3位MNC的对应关系。 


如果一个MCC有对应的3位MNC，需要通过本命令配置MCC和3位MNC的对应关系；如果一个MCC所对应的全部MNC都是3位的，那么配置时只需要输入MCC就可以了，MNC不需要输入。 


SGSN/MME从用户的IMSI号码中解析MNC时，需要根据本命令的配置结果判断IMSI中的MNC是2位还是3位；如果IMSI中的MCC和3位MNC能够匹配到配置记录，则认为用户归属的PLMN使用3位的MNC；如果匹配不到，则认为用户归属的PLMN使用2位的MNC。 




[](None)注意事项 

该命令适用于SGSN/MME网元。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数表示MCC（Mobile Country Code，移动国家码），固定为3位十进制数字，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数表示3位的MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。
NAME|运营商名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~255个字符。|表示运营商的名称。






[](None)命令举例 


新增3位MNC运营商信息配置，设置移动国家码为460，设置移动网号为003，设置运营商名称为TEL。
ADD 3 MNC OPERATOR:MCC="460",MNC="003",NAME="TEL"; 








父主题： [3位MNC运营商信息配置](../../zh-CN/tree/N_1254215.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改3位MNC运营商信息配置(SET 3 MNC OPERATOR) 
## 修改3位MNC运营商信息配置(SET 3 MNC OPERATOR) 


[](None)命令功能 

该命令用于修改MCC和3位MNC对应的运营商信息配置。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数表示MCC（Mobile Country Code，移动国家码），固定为3位十进制数字，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数表示3位的MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。
NAME|运营商名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|表示运营商的名称。






[](None)命令举例 


修改移动国家码为460的3位MNC运营商信息配置，将运营商名称修改为NTE。
SET 3 MNC OPERATOR:MCC="460",MNC="003",NAME="NTE"; 








父主题： [3位MNC运营商信息配置](../../zh-CN/tree/N_1254215.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除3位MNC运营商信息配置(DEL 3 MNC OPERATOR) 
## 删除3位MNC运营商信息配置(DEL 3 MNC OPERATOR) 


[](None)命令功能 

该命令用于删除MCC和3位MNC对应的运营商信息配置。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数表示MCC（Mobile Country Code，移动国家码），固定为3位十进制数字，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数表示3位的MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。
NAME|运营商名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|表示运营商的名称。






[](None)命令举例 


删除3位MNC运营商信息配置。
DEL 3 MNC OPERATOR:MCC="460",MNC="111"; 








父主题： [3位MNC运营商信息配置](../../zh-CN/tree/N_1254215.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询3位MNC运营商信息配置(SHOW 3 MNC OPERATOR) 
## 查询3位MNC运营商信息配置(SHOW 3 MNC OPERATOR) 


[](None)命令功能 

该命令用于查询MCC和3位MNC对应的运营商信息配置。


[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数表示MCC（Mobile Country Code，移动国家码），固定为3位十进制数字，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|该参数表示3位的MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。
NAME|运营商名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|表示运营商的名称。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MCC|移动国家码|参数可选性:任选参数；参数类型:字符型。|该参数表示MCC（Mobile Country Code，移动国家码），固定为3位十进制数字，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
MNC|移动网号|参数可选性:任选参数；参数类型:字符型。|该参数表示3位的MNC（Mobile Network Code，移动网络号），某个国家或地区可能有多个移动网络，移动网号用于唯一标识某个国家或地区的一个移动网络。
NAME|运营商名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|表示运营商的名称。






[](None)命令举例 


查询所有的3位MNC运营商信息配置。
SHOW 3 MNC OPERATOR 


`

命令 (No.1): SHOW 3 MNC OPERATOR

操作维护         移动国家码   移动网号   运营商名称
---------------------------------------------------
复制 修改 删除   302          656        Tbay Mobility , Canada
复制 修改 删除   310                     United States
复制 修改 删除   311                     United States
复制 修改 删除   316                     United States
复制 修改 删除   334                     Mexico
复制 修改 删除   338                     Jamaica
复制 修改 删除   342                     Barbados
复制 修改 删除   344                     Antigua and Barbuda
复制 修改 删除   346                     Cayman Islands
复制 修改 删除   348                     British Virgin Islands
复制 修改 删除   365                     Anguilla
复制 修改 删除   374          130        Digicel Trinidad and Tobago Ltd., Trinidad and Tobago
复制 修改 删除   374          140        LaqTel Ltd., Trinidad and Tobago
复制 修改 删除   376                     Turks and Caicos Islands
复制 修改 删除   460          003        NTE
复制 修改 删除   708                     Honduras
复制 修改 删除   714          020        Telefonica Moviles Panamo S.A., Panama
复制 修改 删除   722                     Argentina
复制 修改 删除   732                     Colombia
复制 修改 删除   750                     Falkland Islands (Malvinas)
---------------------------------------------------
记录数 20

命令执行成功（耗时 0.054 秒）。
` 








父主题： [3位MNC运营商信息配置](../../zh-CN/tree/N_1254215.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 信令面参数配置 
# 信令面参数配置 


[](None)背景知识 


SGSN/MME与其他网元（比如，邻接的GGSN、SGSN、MME、SGW等）基于GTP协议进行消息交互时，比如SGSN创建PDP上下文时和GGSN的交互，MME创建会话时和SGW的交互，本网元SGSN/MME要提供交互的GTPC IPv4/IPv6信令地址。 




[](None)功能描述 


当SGSN/MME与其他网元基于GTP协议进行消息交互时，根据“信令面参数配置”提供本网元交互的GTPC IPv4/IPv6信令地址。 


“信令面参数配置”包含如下2个子节点配置： 



 


                        GTPC信令地址配置，
                        SET SIGIP GTPC
                        ，设置SGSN GTPC信令地址。
                    
 

 


                        MME GTPC信令地址配置，
                        SET MME GTPC
                        ，设置MME GTPC信令地址。
                    
 

 


注意事项： 






信令面参数配置的SGSN/MME网元的GTPC信令地址，同时需要在协议栈的Loopback环回口上配置。 






信令面参数配置了SGSN/MME网元的GTPC IPv6信令地址时，需要License支持才能生效，对应SGSN/MME的License项为“IPv6功能”。 








[](None)相关主题 



 

GTPC信令地址配置
 

 

MME GTPC信令地址配置
 

 

MME Sx信令地址配置
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## GTPC信令地址配置 
## GTPC信令地址配置 


[](None)背景知识 


SGSN与其他网元（比如，邻接的GGSN、SGSN、MME等）基于GTP协议进行消息交互时，比如SGSN创建PDP上下文时和GGSN的交互，本网元SGSN要提供交互的GTPC IPv4/IPv6信令地址。 




[](None)功能描述 


当SGSN与其他网元基于GTP协议进行消息交互时，根据“GTPC信令地址配置”提供本网元交互的GTPC IPv4/IPv6信令地址。 



                GTPC信令地址配置的流程是，设置GTPC信令地址，配置命令为：
                [SET SIGIP GTPC](../mml/1260093.html)
                。
            


注意事项： 



 

GTPC信令地址配置的SGSN网元的GTPC信令地址，同时需要在协议栈的Loopback环回口上配置。
 

 

GTPC信令地址配置了SGSN网元的GTPC IPv6信令地址时，需要License支持才能生效，对应SGSN的License项为“IPv6功能”。
 

 




[](None)相关主题 



 

设置GTPC信令地址(SET SIGIP GTPC)
 

 

查询GTPC信令地址(SHOW SIGIP GTPC)
 

 








父主题： [信令面参数配置](../../zh-CN/tree/N_1254216.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置GTPC信令地址(SET SIGIP GTPC) 
### 设置GTPC信令地址(SET SIGIP GTPC) 


[](None)命令功能 


该命令用于设置SGSN网元的GTPC信令地址。当需要设定或者修改GTPC地址时使用该命令，使用该命令。 


该地址为SGSN与其他网元（包括SGSN、MME等）基于GTP协议交互时的信令地址。 


该地址同时需要在协议栈[IPSTACK](../mml/1404255.html)的环回（Loopback）接口上配置，可通过
[SHOW IP INTERFACE LOOPBACK](../mml/1404144.html)或[SHOW IPV6 INTERFACE LOOPBACK](../mml/1404155.html)命令查询当前系统中配置环回接口。


当该地址配置为GTPC地址后，不能再配置为GTPU地址。 




[](None)注意事项 

该命令仅适用于SGSN网元。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IPADDR|GTPC IPv4信令地址|参数可选性:任选参数；参数类型:地址|IPv4格式的SGSN网元的GTPC信令地址。可通过协议栈中的SHOW IP INTERFACE LOOPBACK命令查询当前系统中配置IPv4环回接口。
IPV6ADDR|GTPC IPv6信令地址|参数可选性:任选参数；参数类型:地址|IPv6格式的SGSN网元的GTPC信令地址。可通过协议栈中的SHOW IPV6 INTERFACE LOOPBACK命令查询当前系统中配置IPv6环回接口。






[](None)命令举例 


设置SGSN GTPC IPv4信令地址为10.44.20.5。
SET SIGIP GTPC:IPADDR="10.44.20.5"; 


`

命令 (No.1): SET SIGIP GTPC:IPADDR="10.44.20.5";

GTPC IPv4信令地址   GTPC IPv6信令地址
-------------------------------------
10.44.20.5          
-------------------------------------
记录数 1

命令执行成功（耗时 4.964 秒）。
` 








父主题： [GTPC信令地址配置](../../zh-CN/tree/N_1254201.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询GTPC信令地址(SHOW SIGIP GTPC) 
### 查询GTPC信令地址(SHOW SIGIP GTPC) 


[](None)命令功能 

该命令用于查询SGSN网元的GTPC地址。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IPADDR|GTPC IPv4信令地址|参数可选性:任选参数；参数类型:地址|IPv4格式的SGSN网元的GTPC信令地址。可通过协议栈中的SHOW IP INTERFACE LOOPBACK命令查询当前系统中配置IPv4环回接口。
IPV6ADDR|GTPC IPv6信令地址|参数可选性:任选参数；参数类型:地址|IPv6格式的SGSN网元的GTPC信令地址。可通过协议栈中的SHOW IPV6 INTERFACE LOOPBACK命令查询当前系统中配置IPv6环回接口。






[](None)命令举例 


查询SGSN GTPC信令地址。
SHOW SIGIP GTPC; 


`

命令 (No.1): SHOW SIGIP GTPC

操作维护  GTPC IPv4信令地址   GTPC IPv6信令地址
-----------------------------------------------
修改      10.44.20.5          
-----------------------------------------------
记录数 1

命令执行成功（耗时 0.041 秒）。
` 








父主题： [GTPC信令地址配置](../../zh-CN/tree/N_1254201.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## MME GTPC信令地址配置 
## MME GTPC信令地址配置 


[](None)背景知识 


MME与其他网元（比如，邻接的SGSN、MME、SGW等）基于GTP协议进行消息交互时，比如MME创建会话时和SGW的交互，本网元MME要提供交互的GTPC IPv4/IPv6信令地址。 




[](None)功能描述 


当MME与其他网元基于GTP协议进行消息交互时，根据“MME GTPC信令地址配置”提供本网元交互的GTPC IPv4/IPv6信令地址。 


注意事项： 






MME GTPC信令地址配置的MME网元的GTPC信令地址，同时需要在协议栈的Loopback环回口上配置。 






MME GTPC信令地址配置了MME网元的GTPC IPv6信令地址时，需要License支持才能生效，对应MME的License项为“IPv6功能”。 








[](None)相关主题 



 

设置MME GTPC信令地址(SET MME GTPC)
 

 

查询MME GTPC信令地址(SHOW MME GTPC)
 

 








父主题： [信令面参数配置](../../zh-CN/tree/N_1254216.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置MME GTPC信令地址(SET MME GTPC) 
### 设置MME GTPC信令地址(SET MME GTPC) 


[](None)命令功能 


当需要设定或者修改GTPC地址时使用该命令，使用该命令，设置GTPC信令地址后，输入的地址设定或更新GTPC信令地址。 


该地址为MME与其他网元（包括SGSN、MME、S-GW等）基于GTP协议交互时的信令地址，该地址同时需要在协议栈的Loopback环回口上配置，当该地址配置为GTPC地址后，不能再配置为GTPU地址。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IPADDR|GTPC IPv4信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME的IPv4信令地址，用户根据实际网络规划配置，只能配置一个IPv4地址。IPv4和IPv6地址可以同时配置，也可以只配置其中一个。IPv6地址需要license的支持，对应的license项为“IPv6功能”。
IPV6ADDR|GTPC IPv6信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME的IPv6信令地址，用户根据实际网络规划配置，只能配置一个IPv6地址。IPv6和IPv4地址可以同时配置，也可以只配置其中一个。IPv6地址需要license的支持，对应的license项为“IPv6功能”。






[](None)命令举例 


设置MME网元的GTPC的IP地址为192.168.11.122。
SET MME GTPC:IPADDR="192.168.11.122"; 








父主题： [MME GTPC信令地址配置](../../zh-CN/tree/N_1254208.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME GTPC信令地址(SHOW MME GTPC) 
### 查询MME GTPC信令地址(SHOW MME GTPC) 


[](None)命令功能 

该命令用于查询GTPC信令地址。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IPADDR|GTPC IPv4信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME的IPv4信令地址，用户根据实际网络规划配置，只能配置一个IPv4地址。IPv4和IPv6地址可以同时配置，也可以只配置其中一个。IPv6地址需要license的支持，对应的license项为“IPv6功能”。
IPV6ADDR|GTPC IPv6信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME的IPv6信令地址，用户根据实际网络规划配置，只能配置一个IPv6地址。IPv6和IPv4地址可以同时配置，也可以只配置其中一个。IPv6地址需要license的支持，对应的license项为“IPv6功能”。






[](None)命令举例 


查询MME网元的GTPC信令地址。
SHOW MME GTPC 


`

命令 (No.1): SHOW MME GTPC

操作维护  GTPC IPv4信令地址   GTPC IPv6信令地址
-----------------------------------------------
修改      192.168.11.122      
-----------------------------------------------
记录数 1

命令执行成功（耗时 0.085 秒）。
` 








父主题： [MME GTPC信令地址配置](../../zh-CN/tree/N_1254208.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## MME Sx信令地址配置 
## MME Sx信令地址配置 


[](None)背景知识 



 

SRVCC（Single Radio Voice Call Continuity，双模单待无线语音呼叫连续性）为单语音呼叫持续。当用户在LTE网络进行语音业务并需要切换至GSM/UMTS网络时，为了保证不中断用户的语音业务，MME提供了SRVCC解决方案，使用户感知不到LTE和CS网络之间切换时的语音中断，解决了基于LTE网络的语音业务向GSM/UMTS网络的语音业务的无缝切换。
进行语音业务的UE从LTE网络切换至GSM/UMTS的过程中，MME通过Sv接口向MSC发送PS to CS的切换请求，请求将语音承载切换到MSC。
 

 

中继技术（Relay）在R10中被引入到3GPP家族，作为LTE-Advanced系统的关键技术，它为小区带来更大的覆盖范围和系统容量。
所谓中继技术，就是在下行方向，基站发给UE的信号不直接发给UE，而是先发给一个中继站，然后再由中继转发给UE；在上行方向，UE的上行信号也不直接发给基站，而是先发给一个中继站，然后再由中继站转发给基站。
 

 




[](None)功能描述 


MME使用GTPv2协议与周边其他网元互联，不同的接口可以使用相同的或不同的信令地址，本配置支持Sv接口、S11（RN）接口配置独立的GTPv2信令地址。 



 

Sv接口:
MME与MSC基于GTP协议进行SRVCC消息交互时，MME需要提供本网元和MSC交互的GTPC IPv4/IPv6信令地址。

                        MME和MSC之间的Sv接口的GTP-C地址，通过
                        SET MME SX GTPC
                        命令设置，地址类型可以是IPV4或者IPV6。
                    

                        MME网元上，Sv接口的信令地址只有在“SRVCC功能”License开启时才需要配置。“SRVCC功能”License未开启时，MME其他接口的GTP地址通过
                        SET MME GTPC
                        命令配置。
                    
 

 

S11（RN）接口:
MME与内置SGW功能的DeNB（Donor eNodeB）基于GTP协议进行RN S11口消息交互时，MME需要提供本网元和DeNB交互的GTPC IPv4/IPv6信令地址。

                        MME和DeNB之间的S11（RN）接口的GTP-C地址，通过
                        SET MME SX GTPC
                        命令设置，地址类型可以是IPV4或者IPV6。
                    
MME网元上，S11（RN）接口的信令地址只有在“Relay功能”License开启时才需要配置。
 

 




[](None)相关主题 



 

设置MME Sx信令地址配置(SET MME SX GTPC)
 

 

查询MME Sx信令地址配置(SHOW MME SX GTPC)
 

 








父主题： [信令面参数配置](../../zh-CN/tree/N_1254216.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置MME Sx信令地址配置(SET MME SX GTPC) 
### 设置MME Sx信令地址配置(SET MME SX GTPC) 


[](None)命令功能 


该命令用于设置或者修改MME Sv接口、S11（RN）接口的GTPC信令地址。 


Sv接口用于MME和MSC进行信令交互，当MME网元启用SRVCC功能时，需要配置Sv接口的GTPC信令地址。 


S11（RN）接口用于MME和DeNB（Donor eNodeB）进行信令交互，当MME网元启用Relay功能时，需要配置S11（RN）接口的GTPC信令地址。 




[](None)注意事项 


Sv接口信令地址:  



 
“SRVCC功能”License开启时，MME网元必须配置Sv接口信令地址。 

 
Sv信令地址需要在协议栈的Loopback环回口上配置。 

 
Sv信令地址需要配置IPv6信令地址时，需要License支持才能生效，对应License项为“IPv6功能”。 

 
Sv信令地址可以和MME GTPC信令地址相同。 

 
MME和SGSN合一局，Sv信令地址不能和SGSN网元的 GTP-U地址相同。 

 


S11（RN）接口信令地址:  



 
“Relay功能”License开启且S1口地址和MME GTPC地址不在同一网段时，MME网元需要配置S11（RN）接口信令地址。 

 
S11（RN）信令地址需要配置IPv6信令地址时，需要License支持才能生效，对应License项为“IPv6功能”。 

 
S11（RN）信令地址可以和MME GTPC信令地址相同。
 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SVIPADDR|Sv IPv4信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME Sv接口IPv4信令地址，用户根据实际网络规划配置，Sv接口最多只能配置一个IPv4地址。说明：MME Sv接口支持同时配置IPv4信令地址和IPv6信令地址，也可以只配置IPv4信令地址，但不能只配置IPv6信令地址。
SVIPV6ADDR|Sv IPv6信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME Sv接口IPv6信令地址，用户根据实际网络规划配置，最多只能配置一个IPv6地址。说明：MME Sv接口支持同时配置IPv4信令地址和IPv6信令地址，也可以只配置IPv4信令地址，但不能只配置IPv6信令地址。IPv6信令地址生效需要license的支持，对应的license项为“IPv6功能”。
S11RNIPADDR|S11(RN) IPv4信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME S11（RN）接口IPv4信令地址，用户根据实际网络规划配置，最多只能配置一个IPv4地址。IPv6和IPv4地址可以同时配置，也可以只配置IPv4地址。
S11RNIPV6ADDR|S11(RN) IPv6信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME S11（RN）接口IPv6信令地址，用户根据实际网络规划配置，最多只能配置一个IPv6地址。IPv6和IPv4地址可以同时配置，也可以只配置IPv6地址。IPv6地址需要license的支持，对应的license项为“IPv6功能”。
S101IPADDR|S101 IPv4信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME S101接口IPv4信令地址，用户根据实际网络规划配置，最多只能配置一个IPv4地址。说明：MME S101接口支持同时配置IPv4信令地址和IPv6信令地址，也可以只配置IPv4信令地址，但不能只配置IPv6信令地址。
S101IPV6ADDR|S101 IPv6信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME S101接口IPv6信令地址，用户根据实际网络规划配置，最多只能配置一个IPv6地址。说明：MME S101接口支持同时配置IPv4信令地址和IPv6信令地址，也可以只配置IPv4信令地址，但不能只配置IPv6信令地址。IPv6信令地址生效需要license的支持，对应的license项为“IPv6功能”。






[](None)命令举例 


设置Sv信令地址为192.168.11.122。 


SET MME SX GTPC:SVIPADDR="192.168.11.122"; 








父主题： [MME Sx信令地址配置](../../zh-CN/tree/N_125064102.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME Sx信令地址配置(SHOW MME SX GTPC) 
### 查询MME Sx信令地址配置(SHOW MME SX GTPC) 


[](None)命令功能 


该命令用于查询MME Sv接口、S11（RN）接口GTPC信令地址。 




[](None)注意事项 


无。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SVIPADDR|Sv IPv4信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME Sv接口IPv4信令地址，用户根据实际网络规划配置，Sv接口最多只能配置一个IPv4地址。说明：MME Sv接口支持同时配置IPv4信令地址和IPv6信令地址，也可以只配置IPv4信令地址，但不能只配置IPv6信令地址。
SVIPV6ADDR|Sv IPv6信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME Sv接口IPv6信令地址，用户根据实际网络规划配置，最多只能配置一个IPv6地址。说明：MME Sv接口支持同时配置IPv4信令地址和IPv6信令地址，也可以只配置IPv4信令地址，但不能只配置IPv6信令地址。IPv6信令地址生效需要license的支持，对应的license项为“IPv6功能”。
S11RNIPADDR|S11(RN) IPv4信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME S11（RN）接口IPv4信令地址，用户根据实际网络规划配置，最多只能配置一个IPv4地址。IPv6和IPv4地址可以同时配置，也可以只配置IPv4地址。
S11RNIPV6ADDR|S11(RN) IPv6信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME S11（RN）接口IPv6信令地址，用户根据实际网络规划配置，最多只能配置一个IPv6地址。IPv6和IPv4地址可以同时配置，也可以只配置IPv6地址。IPv6地址需要license的支持，对应的license项为“IPv6功能”。
S101IPADDR|S101 IPv4信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME S101接口IPv4信令地址，用户根据实际网络规划配置，最多只能配置一个IPv4地址。说明：MME S101接口支持同时配置IPv4信令地址和IPv6信令地址，也可以只配置IPv4信令地址，但不能只配置IPv6信令地址。
S101IPV6ADDR|S101 IPv6信令地址|参数可选性:任选参数；参数类型:地址|该参数用于配置MME S101接口IPv6信令地址，用户根据实际网络规划配置，最多只能配置一个IPv6地址。说明：MME S101接口支持同时配置IPv4信令地址和IPv6信令地址，也可以只配置IPv4信令地址，但不能只配置IPv6信令地址。IPv6信令地址生效需要license的支持，对应的license项为“IPv6功能”。






[](None)命令举例 


查询Sx信令地址。 


SHOW MME SX GTPC 


`

命令 (No.16): SHOW MME SX GTPC

操作维护  Sv IPv4信令地址    Sv IPv6信令地址    S11(RN) IPv4信令地址   S11(RN) IPv6信令地址
------------------------------------------------------------------------------------------
修改      192.168.11.122                        192.168.11.123
------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.041 秒）。
` 








父主题： [MME Sx信令地址配置](../../zh-CN/tree/N_125064102.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 本局移动数据 
# 本局移动数据 


[](None)背景知识 

            
            SGSN网元术语解释：
            Iu-Gb Flex功能：启用Iu-Gb Flex功能后，一个RAN节点能够连接到多个SGSN节点。 


NRI：NRI是SGSN的节点标识。在启用Iu-Gb Flex功能后，SGSN在分配新PTMSI给用户时，包含了本SGSN节点的标识NRI，用户通过RAN节点接入到SGSN时，RAN从用户的PTMSI/TLLI中分离出NRI，根据NRI将信令消息路由到正确的SGSN节点上。NRI使用PTMSI的23比特到14比特，长度在0到10比特间可配置。 


            MME网元术语解释：
            MME权重：MME组成MME POOL时，eNodeB和池内的所有MME相连；池内各个MME配置的权重因子，都会下发给eNodeB；eNodeB发送消息时，根据存储的各个MME的权重因子，按比例分发消息，实现了MME的负荷分担。 


GUMMEI：全局唯一MME标识，由移动国家码MCC、移动网码MNC以及MME标识MMEI组成；MMEI由MME组标识MMEGI和MME编码MMEC组成。 




[](None)功能描述 

            
            “本局移动数据配置”用来配置移动性管理相关的本局全局参数配置：
            MME网元包括：GUMMEI、MME权重、位置信息上报、MOCN、MME缺省APN、支持接口类型等配置； 


SGSN网元：包括：PLMN、FLEX、NRI、SGSN缺省APN、支持接口类型、全局核心网标识、Camel版本、LCS版本、PS用户面配置等； 


MME和SGSN合一局：包括上述SGSN和MME的各项参数配置。 




[](None)相关主题 



 

设置Combo本局移动数据(SET COMBOCFG)
 

 

查询Combo本局移动数据(SHOW COMBOCFG)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置Combo本局移动数据(SET COMBOCFG) 
## 设置Combo本局移动数据(SET COMBOCFG) 


[](None)命令功能 


该命令用于设置Combo本局移动数据。当运营商新开combo局或者修改combo局移动数据配置时使用该命令。该命令执行成功后,该combo局移动数据配置将修改，具体修改项见命令参数。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MMEGROUPID|MME组ID|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|MME所在池组的标识，一般以32768开始。
MMENAME|MME节点名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~150个字符。|MME节点的名称。
CC|国家号|参数可选性:任选参数；参数类型:字符型；参数范围为:0~4个字符。|国际标准分配的国家号，如中国为86。
NDC|国家目的码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~4个字符。|数字移动业务接入号，如139。
MCC|SGSN移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|SGSN移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的移动网号。如中国移动使用02（460-02）。
MMCC|MME移动国家码|参数可选性:任选参数；参数类型:字符型；参数范围为:3~3个字符。|按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动国家码，如中国大陆（不含港澳台地区）为460或461。
MMNC|MME移动网号|参数可选性:任选参数；参数类型:字符型；参数范围为:2~3个字符。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动网号。如中国移动使用02（460-02）。
GSNCODE|SGSN号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|用于在网络中标识SGSN的号码。
MMECODE|MME编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|用于在网络中标识MME的编号。
MMENUMBER|MME号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|用于在网络中标识MME的号码。
IPV4APN|SGSN缺省IPv4 APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|如果2G、3G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv4类型地址连接PDN时，通过此缺省IPv4 APN接入。
IPV6APN|SGSN缺省IPv6 APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|如果2G、3G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv6类型地址连接PDN时，通过此缺省IPv6 APN接入。
IPV4V6APN|SGSN缺省IPv4IPv6 APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|如果2G、3G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv4v6双栈类型地址连接PDN时，通过此缺省IPv4v6 APN接入。
PPPAPN|SGSN缺省PPP APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|如果2G、3G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用PPP类型（即点对点类型）地址连接PDN时，通过此缺省PPP APN接入。
PREINT|国际长途字冠|参数可选性:任选参数；参数类型:字符型；参数范围为:0~4个字符。|本局用户拨打国际长途电话时，在电话号码前加的前缀。如中国的国际长途字冠为00。
SUPTYPE|支持类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局支持的接口类型，可以多选。取值含义：短消息SMS：SGSN与SMS-GMSC、SMS-IWMSC之间的接口，采用Gd接口协议，协议标准为3GPP TS29.060。Gs接口。：Gn/Gp SGSN与MSCS之间的接口，采用BSSAP+协议，协议标准为3GPP TS29.018。Gf接口：Gn/Gp SGSN与EIR之间的接口，采用MAP协议，协议标准为3GPP TS29.002。Gb接口：Gn/Gp SGSN与BSC之间的接口，采用BSSGP协议，协议标准为GSM 08.18。Iu接口：Gn/Gp SGSN与RNC之间的接口，采用RANAP协议，协议标准为3GPP TS25.413。Egprs增强型GPRS：BSC和BTS之间的接口，采用 Abis 协议，协议标准为3GPP TS3GPP TS 08.58 。S13：MME与EIR之间的接口，采用Diemeter协议。
CAMELVER|支持的Camel类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局是否支持移动智能网。取值含义：不支持：本局不支持移动智能网。camelCamel3 Camel3：本局支持camel3版本的移动智能网。Camel4： 本局支持camel4版本移动智能网。
UPVER|PS用户面版本|参数可选性:任选参数；参数类型:整数；参数范围为:1~16。|该参数用于设置CN发送给RNC的用户面版本信息。用户面版本的详细内容参见协议25.413  9.2.1.18节。
UPMODE|PS用户面模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置PS用户面模式，包括透明模式和预定义SDU大小模式。不同版本支持的模式有所不同，详细内容参见协议25.413  9.2.1.18节。取值含义：透明模式：SGSN除了传输数据之外不提供任何特殊功能。支持预定义SDU大小的模式：SGSN除了传输数据之外还提供一定的控制功能。
LCSVER|本局支持的LCS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME/SGSN支持的LCS版本，需要license的支持，对应的license项为“MME/SGSN支持LCS功能”。取值含义：不支持：本局不支持LCS。支持R99：本局支持协议版本为R99的LCS功能。支持支持R4及最高更高版本：本局支持协议版本为R4及以上的版本的LCS功能。
FLEXEN|支持Flex功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持POOL功能。取值含义：不支持：SGSN不支持pool功能。支持：SGSN支持pool功能。超容，SGSN支持pool功能下，可以分配的PTMSI增加到原来的4倍。
NRILEN|NRI的长度|参数可选性:任选参数；参数类型:整数；参数范围为:0~8。|当SGSN支持POOL功能时，需要配置该参数。NRI是网络资源标识，包含在PTMSI中，用于在SGSN POOL内唯一标识一个SGSN节点。NRI的长度由运营商规划。
CNID|全局核心网标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4096。|本combo局在全局网络中标识。
MMEWEIGHT|MME权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于设置MME在POOL内的权重，数值越大，权重越大。MME通过S1 Setup响应消息或者MME CONFIGURATION UPDATE消息携带此参数通知eNodeB，便于eNodeB进行POOL内的MME选择。
OPERATOR|运营商名称|参数可选性:任选参数；参数类型:字符型；参数范围为:0~100个字符。|运营商名称，按照实际填写。
MMEULICHGRPT|支持用户位置信息变化上报配置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持4G用户位置信息变化，即位置区变换后将相应小区和跟踪区信息通知PGW。取值含义：不支持：MME不支持用户位置信息变化上报到PGW。支持：MME支持用户位置信息变化上报到PGW。
MMESHARETYPE|MME支持MOCN功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持多个不同运营商的核心网共享一套无线接入网络。取值含义：不支持：MME不支持多个不同运营商的核心网共享一套无线接入网络支持：MME支持多个不同运营商的核心网共享一套无线接入网络
MMEIPV4APN|MME缺省IPv4 APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|如果4G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv4类型地址连接PDN时，通过此缺省IPv4 APN接入。
MMEIPV6APN|MME缺省IPv6 APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|如果4G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv6类型地址连接PDN时，通过此缺省IPv6 APN接入。
MMEIPV4V6APN|MME缺省IPv4IPv6 APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|如果4G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv4v6双栈类型地址连接PDN时，通过此缺省IPv4v6 APN接入。
ALLOCNRIFLG|不支持Flex功能时是否为UE分配NRI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN不支持Flex功能时，如果配置了NRI长度，为UE分配PTMSI是否携带NRI。取值含义：NO：PTMSI不携带NOULTRA：不使用超容方式分配PTMS，PTMS携带NRI。  ULTRA：使用超容方式PTMSI， PTMSI携带NRI。
MMENIPAPN|MME缺省Non-IP APN|参数可选性:任选参数；参数类型:字符型；参数范围为:0~63个字符。|此参数用于配置缺省Non-IP APN。如果物联网用户在HSS上没有签约Non-IP PDN类型的APN，在终端附着时也没有填写APN，则用户选择使用Non-IP类型PDN时，通过此缺省Non-IP APN接入。
MMEENBULICHGRPT|支持基于eNodeBID位置变化上报|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持4G用户接入的eNodeBID变化时将新的eNodeBID通知PGW。不支持：MME不支持将用户接入的eNodeBID变化上报到PGW。支持：MME支持将用户接入的eNodeBID变化上报到PGW。






[](None)命令举例 


设置Combo本局移动数据，设置MME组ID为32769，设置MME节点名称为zte，设置移动国家码为460，设置移动网号为001，设置MME编号为123，其他参数使用默认配置。 


SET COMBOCFG:MMEGROUPID=32769,MMENAME="zte",MMECODE=123,MCC="460",MNC="001"; 








父主题： [本局移动数据](../../zh-CN/tree/N_1254217.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询Combo本局移动数据(SHOW COMBOCFG) 
## 查询Combo本局移动数据(SHOW COMBOCFG) 


[](None)命令功能 


该命令用于查询Combo本局移动数据。通过该命令查询该局移动性相关的数据，如MMECODE、MMEGROUPID。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MMEGROUPID|MME组ID|参数可选性:任选参数；参数类型:整数。|MME所在池组的标识，一般以32768开始。
MMENAME|MME节点名称|参数可选性:任选参数；参数类型:字符型。|MME节点的名称。
CC|国家号|参数可选性:任选参数；参数类型:字符型。|国际标准分配的国家号，如中国为86。
NDC|国家目的码|参数可选性:任选参数；参数类型:字符型。|数字移动业务接入号，如139。
MCC|SGSN移动国家码|参数可选性:任选参数；参数类型:字符型。|按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的移动国家码，如中国大陆（不含港澳台地区）为460或461。
MNC|SGSN移动网号|参数可选性:任选参数；参数类型:字符型。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本SGSN网元使用的移动网号。如中国移动使用02（460-02）。
MMCC|MME移动国家码|参数可选性:任选参数；参数类型:字符型。|按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动国家码，如中国大陆（不含港澳台地区）为460或461。
MMNC|MME移动网号|参数可选性:任选参数；参数类型:字符型。|由运营商所在国官方机构按国际电信联盟ITU-T E.212建议分配给本MME网元使用的移动网号。如中国移动使用02（460-02）。
GSNCODE|SGSN号码|参数可选性:任选参数；参数类型:字符型。|用于在网络中标识SGSN的号码。
MMECODE|MME编号|参数可选性:任选参数；参数类型:整数。|用于在网络中标识MME的编号。
MMENUMBER|MME号码|参数可选性:任选参数；参数类型:字符型；参数范围为:0~16个字符。|用于在网络中标识MME的号码。
IPV4APN|SGSN缺省IPv4 APN|参数可选性:任选参数；参数类型:字符型。|如果2G、3G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv4类型地址连接PDN时，通过此缺省IPv4 APN接入。
IPV6APN|SGSN缺省IPv6 APN|参数可选性:任选参数；参数类型:字符型。|如果2G、3G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv6类型地址连接PDN时，通过此缺省IPv6 APN接入。
IPV4V6APN|SGSN缺省IPv4IPv6 APN|参数可选性:任选参数；参数类型:字符型。|如果2G、3G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv4v6双栈类型地址连接PDN时，通过此缺省IPv4v6 APN接入。
PPPAPN|SGSN缺省PPP APN|参数可选性:任选参数；参数类型:字符型。|如果2G、3G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用PPP类型（即点对点类型）地址连接PDN时，通过此缺省PPP APN接入。
PREINT|国际长途字冠|参数可选性:任选参数；参数类型:字符型。|本局用户拨打国际长途电话时，在电话号码前加的前缀。如中国的国际长途字冠为00。
SUPTYPE|支持类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局支持的接口类型，可以多选。取值含义：短消息SMS：SGSN与SMS-GMSC、SMS-IWMSC之间的接口，采用Gd接口协议，协议标准为3GPP TS29.060。Gs接口。：Gn/Gp SGSN与MSCS之间的接口，采用BSSAP+协议，协议标准为3GPP TS29.018。Gf接口：Gn/Gp SGSN与EIR之间的接口，采用MAP协议，协议标准为3GPP TS29.002。Gb接口：Gn/Gp SGSN与BSC之间的接口，采用BSSGP协议，协议标准为GSM 08.18。Iu接口：Gn/Gp SGSN与RNC之间的接口，采用RANAP协议，协议标准为3GPP TS25.413。Egprs增强型GPRS：BSC和BTS之间的接口，采用 Abis 协议，协议标准为3GPP TS3GPP TS 08.58 。S13：MME与EIR之间的接口，采用Diemeter协议。
CAMELVER|支持的Camel类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置本局是否支持移动智能网。取值含义：不支持：本局不支持移动智能网。camelCamel3 Camel3：本局支持camel3版本的移动智能网。Camel4： 本局支持camel4版本移动智能网。
UPVER|PS用户面版本|参数可选性:任选参数；参数类型:整数。|该参数用于设置CN发送给RNC的用户面版本信息。用户面版本的详细内容参见协议25.413  9.2.1.18节。
UPMODE|PS用户面模式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置PS用户面模式，包括透明模式和预定义SDU大小模式。不同版本支持的模式有所不同，详细内容参见协议25.413  9.2.1.18节。取值含义：透明模式：SGSN除了传输数据之外不提供任何特殊功能。支持预定义SDU大小的模式：SGSN除了传输数据之外还提供一定的控制功能。
LCSVER|本局支持的LCS版本|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME/SGSN支持的LCS版本，需要license的支持，对应的license项为“MME/SGSN支持LCS功能”。取值含义：不支持：本局不支持LCS。支持R99：本局支持协议版本为R99的LCS功能。支持支持R4及最高更高版本：本局支持协议版本为R4及以上的版本的LCS功能。
FLEXEN|支持Flex功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持POOL功能。取值含义：不支持：SGSN不支持pool功能。支持：SGSN支持pool功能。超容，SGSN支持pool功能下，可以分配的PTMSI增加到原来的4倍。
NRILEN|NRI的长度|参数可选性:任选参数；参数类型:整数。|当SGSN支持POOL功能时，需要配置该参数。NRI是网络资源标识，包含在PTMSI中，用于在SGSN POOL内唯一标识一个SGSN节点。NRI的长度由运营商规划。
CNID|全局核心网标识|参数可选性:任选参数；参数类型:整数。|本combo局在全局网络中标识。
MMEWEIGHT|MME权重|参数可选性:任选参数；参数类型:整数。|该参数用于设置MME在POOL内的权重，数值越大，权重越大。MME通过S1 Setup响应消息或者MME CONFIGURATION UPDATE消息携带此参数通知eNodeB，便于eNodeB进行POOL内的MME选择。
OPERATOR|运营商名称|参数可选性:任选参数；参数类型:字符型。|运营商名称，按照实际填写。
MMEULICHGRPT|支持用户位置信息变化上报配置|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持4G用户位置信息变化，即位置区变换后将相应小区和跟踪区信息通知PGW。取值含义：不支持：MME不支持用户位置信息变化上报到PGW。支持：MME支持用户位置信息变化上报到PGW。
MMESHARETYPE|MME支持MOCN功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持多个不同运营商的核心网共享一套无线接入网络。取值含义：不支持：MME不支持多个不同运营商的核心网共享一套无线接入网络支持：MME支持多个不同运营商的核心网共享一套无线接入网络
MMEIPV4APN|MME缺省IPv4 APN|参数可选性:任选参数；参数类型:字符型。|如果4G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv4类型地址连接PDN时，通过此缺省IPv4 APN接入。
MMEIPV6APN|MME缺省IPv6 APN|参数可选性:任选参数；参数类型:字符型。|如果4G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv6类型地址连接PDN时，通过此缺省IPv6 APN接入。
MMEIPV4V6APN|MME缺省IPv4IPv6 APN|参数可选性:任选参数；参数类型:字符型。|如果4G用户在HSS上没有签约APN，在终端附着时也没有填写APN，则用户选择使用IPv4v6双栈类型地址连接PDN时，通过此缺省IPv4v6 APN接入。
ALLOCNRIFLG|不支持Flex功能时是否为UE分配NRI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN不支持Flex功能时，如果配置了NRI长度，为UE分配PTMSI是否携带NRI。取值含义：NO：PTMSI不携带NOULTRA：不使用超容方式分配PTMS，PTMS携带NRI。  ULTRA：使用超容方式PTMSI， PTMSI携带NRI。
MMENIPAPN|MME缺省Non-IP APN|参数可选性:任选参数；参数类型:字符型。|此参数用于配置缺省Non-IP APN。如果物联网用户在HSS上没有签约Non-IP PDN类型的APN，在终端附着时也没有填写APN，则用户选择使用Non-IP类型PDN时，通过此缺省Non-IP APN接入。
MMEENBULICHGRPT|支持基于eNodeBID位置变化上报|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置MME是否支持4G用户接入的eNodeBID变化时将新的eNodeBID通知PGW。不支持：MME不支持将用户接入的eNodeBID变化上报到PGW。支持：MME支持将用户接入的eNodeBID变化上报到PGW。






[](None)命令举例 


查询Combo本局移动数据。 


SHOW COMBOCFG; 


`

(No.1) : SHOW COMBOCFG:
-----------------umac_160----------------
操作维护       MME组ID MME节点名称 国家号 国家目的码 SGSN移动国家码 SGSN移动网号 MME移动国家码 MME移动网号 SGSN号码  MME编号 MME号码   SGSN缺省IPv4 APN  SGSN缺省IPv6 APN  SGSN缺省IPv4IPv6 APN SGSN缺省PPP APN   国际长途字冠 支持类型                                            支持的Camel类型 PS用户面版本 PS用户面模式 本局支持的LCS版本 支持Flex功能 NRI的长度 全局核心网标识 MME权重 运营商名称 支持用户位置信息变化上报配置 MME支持MOCN功能 MME缺省IPv4 APN   MME缺省IPv6 APN   MME缺省IPv4IPv6 APN 不支持Flex功能时是否为UE分配NRI MME缺省Non-IP APN  支持基于eNodeBID位置变化上报 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           33120   ZTEMME      86     132        460            11           460           11          861311600 160     861351600 mipv4.zte.company mipv6.zte.company mipv4v6.zte.company  mipv4.zte.company 0            短消息&Gs 接口&Gf 接口&Gb 接口&Iu 接口&增强GPRS&S13 支持CAMEL3      1            透明模式     不支持            支持         6         160            1                  支持                         不支持          mipv4.zte.company mipv6.zte.company mipv4v6.zte.company 不分配                          mnonip.zte.company 不支持                       
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-08-10 15:58:46 耗时: 0.193 秒
` 








父主题： [本局移动数据](../../zh-CN/tree/N_1254217.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# FLEX配置 
# FLEX配置 


[](None)背景知识 


移动网络在Flex功能引入之前，一个RNC/BSC只能对应一个SGSN节点；引入Iu-Gb Flex功能后，一个RNC/BSC支持连接到多个SGSN节点；NRI（Network Resource Identifier，网络资源标识）用来识别不同的SGSN。NRI使用了PTMSI的一些固定的bit位。 


RNC/BSC在启用Iu-Gb Flex功能的情况下，SGSN分配新PTMSI给用户时，包含了本SGSN节点的NRI，用户通过RNC/BSC节点接入到SGSN时，RNC/BSC从PTMSI中分离出NRI，根据NRI将信令消息路由到正确的SGSN节点。 


当需要对POOL内SGSN节点的负荷进行重分配，将某个SGSN节点上的用户迁移到其他SGSN上时，可通过网管命令对SGSN进行负荷卸载。SGSN的负荷卸载过程，实现原理是触发用户发起附着或路由更新过程，分配NULL NRI给用户，从而在用户的下一次路由更新过程中能将用户迁移到其他可用的SGSN局。 




[](None)功能描述 


FLEX配置中包括SGSN节点标识NRI的配置和SGSN负荷卸载的相关配置。 



                当需要减少SGSN中的用户负荷，使用负荷卸载功能时，可以在动态管理中执行
                [EXEC UNLOAD](../mml/1263022.html)
                命令请求负荷卸载。卸载的方式包括：
            



 


                        按比例卸载，卸载指定比例的SGSN用户。命令为：
                        SET FLEX
                        :USRSTHD=10
                    
 

 


                        按数量卸载，卸载指定数目的SGSN用户。命令为：
                        SET FLEX
                        :UNLOADNUM=10
                    
 

 


                        基于BSC/RNC的负荷卸载，卸载位于指定BSC/RNC的SGSN用户。命令为：
                        ADD UNLOADBSCRNC

 

 


                        基于RAI的负荷卸载，卸载位于指定RAI的SGSN用户。命令为：
                        ADD UNLOADRAI

 

 


                        基于IMSI号段的负荷卸载，卸载指定IMSI号段的SGSN用户。命令为：
                        ADD UNLOADNUM

 

 


                        基于MSISDN号段的负荷卸载，卸载指定MSISDN号段的SGSN用户。命令为：
                        ADD UNLOADMSISDN

 

 



                使用FLEX功能，需要在移动局配置中开启，命令为SET SGSNCFG或
                [SET COMBOCFG](../mml/1260006.html)
                。
            




[](None)相关主题 



 

NRI配置
 

 

基于BSC/RNC的负荷卸载配置
 

 

基于IMSI号段的负荷卸载配置
 

 

基于RAI的负荷卸载配置
 

 

基于MSISDN号段的负荷卸载配置
 

 

指定SGSN卸载配置
 

 

网元主备参数配置
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## NRI配置 
## NRI配置 


[](None)背景知识 


Iu-Gb Flex功能：支持一个RNC/BSC支持连接到多个SGSN节点，通过NRI（Network Resource Identifier，网络资源标识）用来识别不同的SGSN。 


NRI：NRI使用P-TMSI的第23bit-14bit的全部或者连续的一部分bit作，长度可以为0～10bit，如果长度为0表示不启用FLEX功能。NRI不为0，SGSN给用户分配P-TMSI时，包含本SGSN的NRI，RNC/BSC根据用户的P-TMSI中的NRI选择对应的SGSN节点。 


NULL NRI：如果启用负荷卸载功能，则需要配置NULL NRI，RNC/BSC判断是NULL NRI，重新选择SGSN节点。NULL NRI与池内其他SGSN的NRI编号不重复。 




[](None)功能描述 


NRI配置中，包括以下3部分内容： 


1、FLEX属性配置，用于局间消息最大转发跳数配置，以及负荷重分配时使用的相关参数配置； 


2、本SGSN NRI 编号配置，NRI的编号取值，一般由运营商统一规划，保证POOL内不重复，并且取值范围不超过本局移动配置中配置的NRI长度，也不能等于NULL NRI； 


3、SGSN NULL NRI配置，NULL NRI值一般由运营商提供，用于负荷卸载状态下填充到为用户分配的PTIMSI中；POOL池中同一个PLMN下所有的NULL NRI可以相同。 




[](None)相关主题 



 

设置FLEX配置(SET FLEX)
 

 

查询FLEX配置(SHOW FLEX)
 

 

新增FLEX NRI配置(ADD FLEX NRI)
 

 

修改FLEX NRI配置(SET FLEX NRI)
 

 

删除FLEX NRI配置(DEL FLEX NRI)
 

 

查询FLEX NRI配置(SHOW FLEX NRI)
 

 

设置FLEX NULLNRI配置(SET FLEX NULLNRI)
 

 

删除FLEX NULLNRI配置(DEL FLEX NULLNRI)
 

 

查询FLEX NULLNRI配置(SHOW FLEX NULLNRI)
 

 








父主题： [FLEX配置](../../zh-CN/tree/N_1254218.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置FLEX配置(SET FLEX) 
### 设置FLEX配置(SET FLEX) 


[](None)命令功能 


该命令用于修改FLEX功能相关的配置，在SGSN支持FLEX特性时需要检查该项配置是否合理。可以修改以下内容: 



 
最大跳数。该配置用于该SGSN作为default SGSN收到Identification Request/ SGSN
Context Request消息，需要将该消息转发给POOL内其他SGSN时，填写的Hop Counter字段的数值，默认为10。
 

 
重分配周期路由更新时长。该配置用于在SGSN负荷卸载状态时，SGSN在附着接受或路由更新接受消息中，分配给需卸载用户的周期性路由更新定时器的时长，默认为4秒。
 

 
强制分离定时器时长。该配置用于控制负荷卸载第一阶段的时长，该定时器超时后进入负荷卸载第二阶段，SGSN主动对需卸载的用户发起网络侧分离，默认为60分钟。
 

 
重分配完成用户数门限。该配置用于按比例方式进行的SGSN负荷卸载，当在线用户比例已经低于该配置时，结束负荷卸载，默认为100‰。
 

 
负荷卸载等待时间。该配置用于负荷卸载，当该定时器超时后，强制结束负荷卸载，默认为120分钟。
 

 
重分配需卸载用户数。该配置用于按用户数方式进行的SGSN负荷卸载，SGSN统计到的已卸载用户数大于该配置时，结束负荷卸载，默认为10000。
 

 
负荷卸载步长。该配置用于控制负荷卸载进入第二阶段时，各个USMP每秒处理已接入该SGSN且符合卸载条件的在线用户的数目，默认为35。
 

 




[](None)注意事项 

负荷卸载等待定时器需要大于强制分离定时器时长。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MAXHOP|最大跳数|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|POOL内SGSN转发Identification Request或SGSN Context Request消息时，可能出现无限次转发的情况。为解决该问题，3GPP协议在这两条消息中引入了HOP Counter字段，当该字段等于零时，SGSN将不再转发这两条消息。当需要转发Identification Request或SGSN Context Request消息，而且消息中没有携带该字段时，使用该配置项-1填充；当前需要转发Identification Request或SGSN Context Request消息，且消息中携带了Hop Counter字段，将Hop Counter数值-1填充。
RAUTIMER|重分配周期路由更新时长(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:2~62。|该配置用于在负荷卸载的时候，在附着流程或者是路由更新流程，SGSN给需要卸载的终端下发附着接受消息或者是路由更新接受消息时，消息中的周期性路由更新定时器时长这一字段使用该项配置的数值填写。
DETACHTIME|强制分离定时器时长(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1440。|该配置用于控制负荷卸载第一阶段的时长，在该阶段，收到预期发生迁移的用户所发起的附着或RAU请求消息，为其分配包含NULL-NRI的PTMSI及很短的周期性RAU时长。
USRSTHD|重分配完成用户数门限(‰)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1000。|该配置在按比例方式的SGSN卸载时生效。作为卸载结束条件，当前用户数小于该门限值时，完成卸载。
ENDTIMER|负荷卸载等待时间(分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1440。|该配置用于控制整个负荷卸载的时长，当该定时器超时而卸载仍未结束时，无条件停止卸载。
UNLOADNUM|重分配需卸载用户数|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|该配置用于按用户数方式的SGSN卸载。当已卸载用户数大于该门限值时，完成卸载。
SCANSTEP|负荷卸载步长|参数可选性:任选参数；参数类型:整数；参数范围为:10~100。|该参数用于控制负荷卸载第一阶段和第二阶段的卸载速率，即：USMP每秒处理接入该SGSN且符合卸载条件的用户的数目。卸载预处理期间（卸载第一阶段）：SGSN按照此卸载步长控制活动用户卸载速率。卸载预处理时间超时后（卸载第二阶段）：SGSN在卸载预处理时间超时之后，按照此步长控制扫描用户卸载和活动用户接入卸载速率。






[](None)命令举例 


按默认值设置FLEX配置。
SET FLEX; 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询FLEX配置(SHOW FLEX) 
### 查询FLEX配置(SHOW FLEX) 


[](None)命令功能 


该命令用于查询FLEX功能相关的配置，执行该命令不需要填写参数。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MAXHOP|最大跳数|参数可选性:任选参数；参数类型:整数。|POOL内SGSN转发Identification Request或SGSN Context Request消息时，可能出现无限次转发的情况。为解决该问题，3GPP协议在这两条消息中引入了HOP Counter字段，当该字段等于零时，SGSN将不再转发这两条消息。当需要转发Identification Request或SGSN Context Request消息，而且消息中没有携带该字段时，使用该配置项-1填充；当前需要转发Identification Request或SGSN Context Request消息，且消息中携带了Hop Counter字段，将Hop Counter数值-1填充。
RAUTIMER|重分配周期路由更新时长(秒)|参数可选性:任选参数；参数类型:整数。|该配置用于在负荷卸载的时候，在附着流程或者是路由更新流程，SGSN给需要卸载的终端下发附着接受消息或者是路由更新接受消息时，消息中的周期性路由更新定时器时长这一字段使用该项配置的数值填写。
DETACHTIME|强制分离定时器时长(分钟)|参数可选性:任选参数；参数类型:整数。|该配置用于控制负荷卸载第一阶段的时长，在该阶段，收到预期发生迁移的用户所发起的附着或RAU请求消息，为其分配包含NULL-NRI的PTMSI及很短的周期性RAU时长。
USRSTHD|重分配完成用户数门限(‰)|参数可选性:任选参数；参数类型:整数。|该配置在按比例方式的SGSN卸载时生效。作为卸载结束条件，当前用户数小于该门限值时，完成卸载。
ENDTIMER|负荷卸载等待时间(分钟)|参数可选性:任选参数；参数类型:整数。|该配置用于控制整个负荷卸载的时长，当该定时器超时而卸载仍未结束时，无条件停止卸载。
UNLOADNUM|重分配需卸载用户数|参数可选性:任选参数；参数类型:整数。|该配置用于按用户数方式的SGSN卸载。当已卸载用户数大于该门限值时，完成卸载。
SCANSTEP|负荷卸载步长|参数可选性:任选参数；参数类型:整数。|该参数用于控制负荷卸载第一阶段和第二阶段的卸载速率，即：USMP每秒处理接入该SGSN且符合卸载条件的用户的数目。卸载预处理期间（卸载第一阶段）：SGSN按照此卸载步长控制活动用户卸载速率。卸载预处理时间超时后（卸载第二阶段）：SGSN在卸载预处理时间超时之后，按照此步长控制扫描用户卸载和活动用户接入卸载速率。






[](None)命令举例 


查询FLEX配置。
SHOW FLEX; 


`

命令 (No.1): SHOW FLEX

操作维护  最大跳数   重分配周期路由更新时长(秒)   强制分离定时器时长(分钟)   重分配完成用户数门限(‰)   负荷卸载等待时间(分钟)   重分配需卸载用户数   负荷卸载步长
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      10         4                            60                         100                        120                      10000                35
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.127 秒）。
` 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增FLEX NRI配置(ADD FLEX NRI) 
### 新增FLEX NRI配置(ADD FLEX NRI) 


[](None)命令功能 


该命令用于配置POOL内本SGSN所使用的NRI值，该NRI值需要统一规划，保证在POOL内唯一。 




[](None)注意事项 


新增NRI配置后需要重启整局。 


NRI值非0时，NRI的长度必须配置，可通过[SHOW COMBOCFG](1260007.html)命令查询本局移动数据的NRI长度。NRI的值不能大于NRI bit位长度数的最大值。




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NRI|NRI值|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|NRI（网络资源标识，Net Resource Identify）在POOL内唯一。NRI用于POOL组网时，无线侧选择SGSN，以及发生POOL内的跨局流程时，新局查找老局。当PS网络使用POOL组网时，SGSN会在附着流程或是路由更新流程给终端分配包含本局NRI的PTMSI。在RNC或BSC侧需要配置该NRI与对应SGSN的关联关系。后续终端使用该PTMSI发起流程，RNC或BSC可以根据PTMSI中的NRI值，将消息投递到正确的SGSN。
NAME|用户别名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|NRI的别名，起备注作用，命名时以方便记忆为原则。






[](None)命令举例 


新增FLEX NRI配置，设置NRI值为2，NRI别名为2。
ADD FLEX NRI:NRI=2,NAME="2"; 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改FLEX NRI配置(SET FLEX NRI) 
### 修改FLEX NRI配置(SET FLEX NRI) 


[](None)命令功能 


该命令用于修改指定NRI的用户别名，当NRI的用户别名的含义不够清晰时可以使用此命令修改。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NRI|NRI值|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|NRI（网络资源标识，Net Resource Identify）在POOL内唯一。NRI用于POOL组网时，无线侧选择SGSN，以及发生POOL内的跨局流程时，新局查找老局。当PS网络使用POOL组网时，SGSN会在附着流程或是路由更新流程给终端分配包含本局NRI的PTMSI。在RNC或BSC侧需要配置该NRI与对应SGSN的关联关系。后续终端使用该PTMSI发起流程，RNC或BSC可以根据PTMSI中的NRI值，将消息投递到正确的SGSN。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|NRI的别名，起备注作用，命名时以方便记忆为原则。






[](None)命令举例 


将NRI值为2的用户别名修改为NRI2。
SET FLEX NRI:NRI=2,NAME="NRI2"; 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除FLEX NRI配置(DEL FLEX NRI) 
### 删除FLEX NRI配置(DEL FLEX NRI) 


[](None)命令功能 


该命令用于删除指定的NRI配置。根据规划分配给该SGSN使用的NRI值发生变化时可以使用此命令，删除NRI配置后需要重启整局。 




[](None)注意事项 

删除NRI配置后需要重启整局。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NRI|NRI值|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|NRI（网络资源标识，Net Resource Identify）在POOL内唯一。NRI用于POOL组网时，无线侧选择SGSN，以及发生POOL内的跨局流程时，新局查找老局。当PS网络使用POOL组网时，SGSN会在附着流程或是路由更新流程给终端分配包含本局NRI的PTMSI。在RNC或BSC侧需要配置该NRI与对应SGSN的关联关系。后续终端使用该PTMSI发起流程，RNC或BSC可以根据PTMSI中的NRI值，将消息投递到正确的SGSN。






[](None)命令举例 


删除NRI值为2的FLEX NRI配置。
DEL FLEX NRI:NRI=2; 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询FLEX NRI配置(SHOW FLEX NRI) 
### 查询FLEX NRI配置(SHOW FLEX NRI) 


[](None)命令功能 


该命令用于查询FLEX NRI配置。需要查看特定的NRI是否是NULL NRI时，可以在命令中填写NRI的值或者是NRI用户别名。按默认选项执行该命令时，可以显示本局配置的所有NRI是否是NULL NRI。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NRI|NRI值|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|NRI（网络资源标识，Net Resource Identify）在POOL内唯一。NRI用于POOL组网时，无线侧选择SGSN，以及发生POOL内的跨局流程时，新局查找老局。当PS网络使用POOL组网时，SGSN会在附着流程或是路由更新流程给终端分配包含本局NRI的PTMSI。在RNC或BSC侧需要配置该NRI与对应SGSN的关联关系。后续终端使用该PTMSI发起流程，RNC或BSC可以根据PTMSI中的NRI值，将消息投递到正确的SGSN。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|NRI的别名，起备注作用，命名时以方便记忆为原则。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NRI|NRI值|参数可选性:任选参数；参数类型:整数。|NRI（网络资源标识，Net Resource Identify）在POOL内唯一。NRI用于POOL组网时，无线侧选择SGSN，以及发生POOL内的跨局流程时，新局查找老局。当PS网络使用POOL组网时，SGSN会在附着流程或是路由更新流程给终端分配包含本局NRI的PTMSI。在RNC或BSC侧需要配置该NRI与对应SGSN的关联关系。后续终端使用该PTMSI发起流程，RNC或BSC可以根据PTMSI中的NRI值，将消息投递到正确的SGSN。
NULLNRI|NULL NRI标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为输出参数，无须操作人员设置，用于系统内部处理。仅用于表示当前查询的NRI信息是否为SHOW FLEX NULLNRI命令中的“NRI”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|NRI的别名，起备注作用，命名时以方便记忆为原则。






[](None)命令举例 


查询FLEX NRI配置。
SHOW FLEX NRI; 


`

命令 (No.1): SHOW FLEX NRI;

操作维护         NRI值   NULL NRI标志   用户别名
------------------------------------------------
复制 修改 删除   2       FALSE          NRI2
------------------------------------------------
记录数 1

命令执行成功（耗时 0.104 秒）。
` 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置FLEX NULLNRI配置(SET FLEX NULLNRI) 
### 设置FLEX NULLNRI配置(SET FLEX NULLNRI) 


[](None)命令功能 


该命令用于设置NULL NRI值，该值需要统一规划，保证POOL内各个SGSN使用相同的NULL NRI。NULL NRI是在SGSN处于负荷卸载过程中使用的NRI。 


当SGSN进行负荷卸载时，SGSN会给需要卸载的终端分配包含该NULL NRI的PTMSI。由于在无线侧没有配置该NULL NRI与SGSN的归属关系，当终端使用该PTMSI发起后续流程时，RAN会随机选择POOL内的SGSN，从而可以达到负荷卸载功能将用户迁移到其他SGSN的目的。 




[](None)注意事项 

NULL-NRI的值需要统一规划，要求POOL内的各个SGSN使用相同的NULL-NRI取值，并且不能与NRI的值相同。RAN侧没有配置该NULL-NRI与POOL内SGSN的归属关系。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NRI|NRI值|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|NRI（网络资源标识，Net Resource Identify）在POOL内唯一。NRI用于POOL组网时，无线侧选择SGSN，以及发生POOL内的跨局流程时，新局查找老局。当PS网络使用POOL组网时，SGSN会在附着流程或是路由更新流程给终端分配包含本局NRI的PTMSI。在RNC或BSC侧需要配置该NRI与对应SGSN的关联关系。后续终端使用该PTMSI发起流程，RNC或BSC可以根据PTMSI中的NRI值，将消息投递到正确的SGSN。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|NULL NRI的别名，起备注作用，命名时以方便记忆为原则。






[](None)命令举例 


设置FLEX NULLNRI配置，设置NRI值为1。
SET FLEX NULLNRI:NRI=1; 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除FLEX NULLNRI配置(DEL FLEX NULLNRI) 
### 删除FLEX NULLNRI配置(DEL FLEX NULLNRI) 


[](None)命令功能 


该命令用于删除NULL-NRI配置。规划的NULL NRI值发生变化时，可以使用该命令删除原有的配置。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NRI|NRI值|参数可选性:必选参数；参数类型:整数；参数范围为:0~255。|NRI（网络资源标识，Net Resource Identify）在POOL内唯一。NRI用于POOL组网时，无线侧选择SGSN，以及发生POOL内的跨局流程时，新局查找老局。当PS网络使用POOL组网时，SGSN会在附着流程或是路由更新流程给终端分配包含本局NRI的PTMSI。在RNC或BSC侧需要配置该NRI与对应SGSN的关联关系。后续终端使用该PTMSI发起流程，RNC或BSC可以根据PTMSI中的NRI值，将消息投递到正确的SGSN。






[](None)命令举例 


删除NRI值为1的FLEX NULLNRI配置。
DEL FLEX NULLNRI:NRI=1; 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询FLEX NULLNRI配置(SHOW FLEX NULLNRI) 
### 查询FLEX NULLNRI配置(SHOW FLEX NULLNRI) 


[](None)命令功能 


该命令用于查询NULL-NRI配置。该命令不需要输入参数，执行后可以看到本局配置的NULL NRI的取值及NRI用户别名。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NRI|NRI值|参数可选性:任选参数；参数类型:整数。|NRI（网络资源标识，Net Resource Identify）在POOL内唯一。NRI用于POOL组网时，无线侧选择SGSN，以及发生POOL内的跨局流程时，新局查找老局。当PS网络使用POOL组网时，SGSN会在附着流程或是路由更新流程给终端分配包含本局NRI的PTMSI。在RNC或BSC侧需要配置该NRI与对应SGSN的关联关系。后续终端使用该PTMSI发起流程，RNC或BSC可以根据PTMSI中的NRI值，将消息投递到正确的SGSN。
NULLNRI|NULL NRI标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为输出参数，无须操作人员设置，用于系统内部处理。仅用于表示当前查询的NRI信息是否为SHOW FLEX NULLNRI命令中的“NRI”。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|NULL NRI的别名，起备注作用，命名时以方便记忆为原则。






[](None)命令举例 


查询所有的FLEX NULLNRI配置。
SHOW FLEX NULLNRI; 


`

命令 (No.1): SHOW FLEX NULLNRI

操作维护    NRI值   NULL NRI标志   用户别名
-------------------------------------------
修改 删除   1       TRUE           
-------------------------------------------
记录数 1

命令执行成功（耗时 0.043 秒）。
` 








父主题： [NRI配置](../../zh-CN/tree/N_1254203.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 基于BSC/RNC的负荷卸载配置 
## 基于BSC/RNC的负荷卸载配置 


[](None)背景知识 

            
            SGSN的负荷卸载，可支持针对在指定的BSC/RNC下的SGSN用户进行卸载；可应用于该BSC/RNC升级前，对其所辖用户的迁移；同时也是分批卸载的一种方式。
        


[](None)功能描述 


基于BSC/RNC的负荷卸载配置用于指定需要进行负荷卸载的NSE ID/RNC ID。 



                执行动态管理中请求负荷卸载命令
                [EXEC UNLOAD](../mml/1263022.html)
                时，如果SGSN卸载方式参数设置为按指定BSC/RNC卸载，则将使用本配置中配置的NSE ID/RNC ID作为指定的BSC/RNC的标识。
            




[](None)相关主题 



 

新增基于BSC/RNC的负荷卸载配置(ADD UNLOADBSCRNC)
 

 

删除基于BSC/RNC的负荷卸载配置(DEL UNLOADBSCRNC)
 

 

删除全部基于BSC/RNC的负荷卸载配置(DEL UNLOADBSCRNC ALL)
 

 

查询基于BSC/RNC的负荷卸载配置(SHOW UNLOADBSCRNC)
 

 








父主题： [FLEX配置](../../zh-CN/tree/N_1254218.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增基于BSC/RNC的负荷卸载配置(ADD UNLOADBSCRNC) 
### 新增基于BSC/RNC的负荷卸载配置(ADD UNLOADBSCRNC) 


[](None)命令功能 


该命令用于新增基于BSC/RNC的负荷卸载配置，在执行按BSC/RNC的负荷卸载时需要使用该配置。当SGSN执行按BSC/RNC的负荷卸载时，SGSN判断只有从该配置项中的BSC/RNC接入的终端才满足负荷卸载条件，才会在附着流程或者路由更新流程为其分配包含NULL NRI的PTMSI以及重分配周期性路由更新定时器时长。 




[](None)注意事项 

NSE标识及RNC标识只能二选一。相应的NSE或者RNC必须支持FLEX属性。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSE|NSE标识|参数可选性:必须单选参数；参数类型:整数；参数范围为:1~65535。|一个BSC物理实体虚拟成一个或者多个NSE，无线侧统一规划给每个NSE分配NSE标识。该配置命令中NSE标识不能与RNC标识同时设置。
RNC|RNC标识|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~65535。|无线侧统一规划给每个RNC分配RNC标识。该配置命令中RNC标识不能与NSE标识同时设置。






[](None)命令举例 


新增NSE标识为1的基于BSC/RNC的负荷卸载配置。
ADD UNLOADBSCRNC:NSE=1; 








父主题： [基于BSC/RNC的负荷卸载配置](../../zh-CN/tree/N_12605254.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除基于BSC/RNC的负荷卸载配置(DEL UNLOADBSCRNC) 
### 删除基于BSC/RNC的负荷卸载配置(DEL UNLOADBSCRNC) 


[](None)命令功能 


该命令用于删除某一条基于BSC/RNC的负荷卸载配置。特定的BSC或者RNC不再需要负荷卸载时，可以使用该命令从配置表中删除。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSE|NSE标识|参数可选性:必须单选参数；参数类型:整数；参数范围为:1~65535。|一个BSC物理实体虚拟成一个或者多个NSE，无线侧统一规划给每个NSE分配NSE标识。该配置命令中NSE标识不能与RNC标识同时设置。
RNC|RNC标识|参数可选性:必须单选参数；参数类型:整数；参数范围为:0~65535。|无线侧统一规划给每个RNC分配RNC标识。该配置命令中RNC标识不能与NSE标识同时设置。






[](None)命令举例 


删除NSE标识为1基于BSC/RNC的负荷卸载配置。
DEL UNLOADBSCRNC:NSE=1; 








父主题： [基于BSC/RNC的负荷卸载配置](../../zh-CN/tree/N_12605254.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除全部基于BSC/RNC的负荷卸载配置(DEL UNLOADBSCRNC ALL) 
### 删除全部基于BSC/RNC的负荷卸载配置(DEL UNLOADBSCRNC ALL) 


[](None)命令功能 


该命令用于删除全部基于BSC/RNC的负荷卸载配置。配置表中的所有BSC及RNC都不再需要负荷卸载时，可以使用该命令便捷删除。 




[](None)注意事项 

无。


[](None)命令举例 


删除全部基于BSC/RNC的负荷卸载配置。
DEL UNLOADBSCRNC ALL; 








父主题： [基于BSC/RNC的负荷卸载配置](../../zh-CN/tree/N_12605254.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询基于BSC/RNC的负荷卸载配置(SHOW UNLOADBSCRNC) 
### 查询基于BSC/RNC的负荷卸载配置(SHOW UNLOADBSCRNC) 


[](None)命令功能 


该命令用于查询基于BSC/RNC的负荷卸载配置。可根据单个NSE标识或者RNC标识，查看对应的BSC或者RNC是否在BSC/RNC负荷卸载配置表中；可按照默认命令查看所有在BSC/RNC负荷卸载配置表中的NSE标识及RNC标识。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSE|NSE标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|一个BSC物理实体虚拟成一个或者多个NSE，无线侧统一规划给每个NSE分配NSE标识。该配置命令中NSE标识不能与RNC标识同时设置。
RNC|RNC标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|无线侧统一规划给每个RNC分配RNC标识。该配置命令中RNC标识不能与NSE标识同时设置。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
NSE|NSE标识|参数可选性:任选参数；参数类型:整数。|一个BSC物理实体虚拟成一个或者多个NSE，无线侧统一规划给每个NSE分配NSE标识。该配置命令中NSE标识不能与RNC标识同时设置。
RNC|RNC标识|参数可选性:任选参数；参数类型:整数。|无线侧统一规划给每个RNC分配RNC标识。该配置命令中RNC标识不能与NSE标识同时设置。






[](None)命令举例 


查询基于BSC/RNC的负荷卸载配置。
SHOW UNLOADBSCRNC; 


`

命令 (No.1): SHOW UNLOADBSCRNC

操作维护    NSE标识   RNC标识
-----------------------------
复制 删除   1         
-----------------------------
记录数 1

命令执行成功（耗时 0.063 秒）。
` 








父主题： [基于BSC/RNC的负荷卸载配置](../../zh-CN/tree/N_12605254.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 基于IMSI号段的负荷卸载配置 
## 基于IMSI号段的负荷卸载配置 


[](None)背景知识 

            
            SGSN的负荷卸载，可支持针对指定的IMSI号段的SGSN用户进行卸载；从而满足运营商出于管理目的，对指定号段的用户重分配；同时也是分批卸载的一种方式。
        


[](None)功能描述 


基于IMSI号段的负荷卸载配置用于指定需要进行负荷卸载的IMSI号段。 



                执行动态管理中请求负荷卸载命令
                [EXEC UNLOAD](../mml/1263022.html)
                时，如果SGSN卸载方式参数设置为按指定IMSI号段卸载，则将使用本配置中配置的IMSI号段作为指定的IMSI号段。
            




[](None)相关主题 



 

新增基于IMSI号段的负荷卸载配置(ADD UNLOADNUM)
 

 

删除基于IMSI号段的负荷卸载配置(DEL UNLOADNUM)
 

 

删除全部基于IMSI号段的负荷卸载配置(DEL UNLOADNUM ALL)
 

 

查询基于IMSI号段的负荷卸载配置(SHOW UNLOADNUM)
 

 








父主题： [FLEX配置](../../zh-CN/tree/N_1254218.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增基于IMSI号段的负荷卸载配置(ADD UNLOADNUM) 
### 新增基于IMSI号段的负荷卸载配置(ADD UNLOADNUM) 


[](None)命令功能 


该命令用于新增基于IMSI的负荷卸载配置。当SGSN执行按IMSI号段的负荷卸载时，只有IMSI号码处于该配置的号段内的终端才满足负荷卸载条件，SGSN才会在附着流程或者路由更新流程为其分配包含NULL NRI的PTMSI以及重分配周期性路由更新定时器时长。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI(Internation Mobile Subscriber Identity)是全球唯一的国际移动用户识别码。IMSI共有15位，由MCC+MNC+MSIN三部分组成。MCC是移动国家码，共三位，由ITU统一分配;MNC是移动网络码，两位或者三位，由各个国家分配；MSIN是移动用户识别号码，由各运行商自由分配。根据需要卸载的IMSI范围，在该项配置中填写长度在1到15的IMSI号段。






[](None)命令举例 


新增基于IMSI的负荷卸载配置，设置IMSI号段为46001。
ADD UNLOADNUM:IMSI="46001"; 








父主题： [基于IMSI号段的负荷卸载配置](../../zh-CN/tree/N_12605304.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除基于IMSI号段的负荷卸载配置(DEL UNLOADNUM) 
### 删除基于IMSI号段的负荷卸载配置(DEL UNLOADNUM) 


[](None)命令功能 


该命令用于删除一条特定的基于IMSI号段的负荷卸载配配置。当需要卸载的IMSI号段发生变更时，可以使用该命令删除已有的配置。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI(Internation Mobile Subscriber Identity)是全球唯一的国际移动用户识别码。IMSI共有15位，由MCC+MNC+MSIN三部分组成。MCC是移动国家码，共三位，由ITU统一分配;MNC是移动网络码，两位或者三位，由各个国家分配；MSIN是移动用户识别号码，由各运行商自由分配。根据需要卸载的IMSI范围，在该项配置中填写长度在1到15的IMSI号段。






[](None)命令举例 


删除基于IMSI号段为46001的负荷卸载配配置。
DEL UNLOADNUM:IMSI="46001"; 








父主题： [基于IMSI号段的负荷卸载配置](../../zh-CN/tree/N_12605304.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除全部基于IMSI号段的负荷卸载配置(DEL UNLOADNUM ALL) 
### 删除全部基于IMSI号段的负荷卸载配置(DEL UNLOADNUM ALL) 


[](None)命令功能 


该命令用于删除全部基于IMSI号段的负荷卸载配配置。需要卸载的IMSI号段发生变更，配置的IMSI号段条目较多时可以使用该命令便捷删除。 




[](None)注意事项 

无。


[](None)命令举例 


删除全部基于IMSI号段的负荷卸载配配置。
DEL UNLOADNUM ALL; 








父主题： [基于IMSI号段的负荷卸载配置](../../zh-CN/tree/N_12605304.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询基于IMSI号段的负荷卸载配置(SHOW UNLOADNUM) 
### 查询基于IMSI号段的负荷卸载配置(SHOW UNLOADNUM) 


[](None)命令功能 


该命令用于查询基于IMSI号段的负荷卸载配配置。可根据特定的IMSI号段来查看该号段是否在基于IMSI号段的负荷卸载配置中；可按默认方式执行该命令来查看基于IMSI号段的负荷卸载配置中的所有IMSI号段。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|IMSI(Internation Mobile Subscriber Identity)是全球唯一的国际移动用户识别码。IMSI共有15位，由MCC+MNC+MSIN三部分组成。MCC是移动国家码，共三位，由ITU统一分配;MNC是移动网络码，两位或者三位，由各个国家分配；MSIN是移动用户识别号码，由各运行商自由分配。根据需要卸载的IMSI范围，在该项配置中填写长度在1到15的IMSI号段。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型。|IMSI(Internation Mobile Subscriber Identity)是全球唯一的国际移动用户识别码。IMSI共有15位，由MCC+MNC+MSIN三部分组成。MCC是移动国家码，共三位，由ITU统一分配;MNC是移动网络码，两位或者三位，由各个国家分配；MSIN是移动用户识别号码，由各运行商自由分配。根据需要卸载的IMSI范围，在该项配置中填写长度在1到15的IMSI号段。






[](None)命令举例 


查询基于IMSI号段为46001的负荷卸载配配置。
SHOW UNLOADNUM:IMSI="46001"; 


`

命令 (No.1): SHOW UNLOADNUM:IMSI="46001";

操作维护    IMSI号段
--------------------
复制 删除   46001
--------------------
记录数 1

命令执行成功（耗时 0.052 秒）。
` 








父主题： [基于IMSI号段的负荷卸载配置](../../zh-CN/tree/N_12605304.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 基于RAI的负荷卸载配置 
## 基于RAI的负荷卸载配置 


[](None)背景知识 

            
            SGSN的负荷卸载，可支持针对在指定RAI下的SGSN用户进行卸载；从而满足运营商出于管理目的，对指定位置的用户重分配；同时也是分批卸载的一种方式。
        


[](None)功能描述 


基于RAI的负荷卸载配置用于指定需要进行负荷卸载的RAI编号。最大支持256个RAI。 



                执行动态管理中请求负荷卸载命令
                [EXEC UNLOAD](../mml/1263022.html)
                时，如果SGSN卸载方式参数设置为按指定路由区卸载，则将使用本配置中配置的RAI作为指定的路由区标识。
            




[](None)相关主题 



 

新增基于RAI的负荷卸载配置(ADD UNLOADRAI)
 

 

删除基于RAI的负荷卸载配置(DEL UNLOADRAI)
 

 

删除全部基于RAI的负荷卸载配置(DEL UNLOADRAI ALL)
 

 

查询基于RAI的负荷卸载配置(SHOW UNLOADRAI)
 

 








父主题： [FLEX配置](../../zh-CN/tree/N_1254218.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增基于RAI的负荷卸载配置(ADD UNLOADRAI) 
### 新增基于RAI的负荷卸载配置(ADD UNLOADRAI) 


[](None)命令功能 


该命令用于新增基于RAI的负荷卸载配置。当SGSN执行按RAI的负荷卸载时，只有从该配置的RAI接入的终端才满足负荷卸载条件，SGSN才会在附着流程或者路由更新流程为其分配包含NULL NRI的PTMSI以及重分配周期性路由更新定时器时长。 




[](None)注意事项 


使用[SHOW RAI](1262238.html)命令检查该路由区在本SGSN已经配置，且支持FLEX属性。




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAI|路由区名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|路由区名称，系统给每个路由区指定了名称，系统内部根据该名称关联对应的路由区。






[](None)命令举例 


新增基于RAI的负荷卸载配置，设置路由区名为rai1。
ADD UNLOADRAI:RAI="rai1"; 








父主题： [基于RAI的负荷卸载配置](../../zh-CN/tree/N_12605354.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除基于RAI的负荷卸载配置(DEL UNLOADRAI) 
### 删除基于RAI的负荷卸载配置(DEL UNLOADRAI) 


[](None)命令功能 


该命令用于删除一条基于RAI号段的负荷卸载配配置。当需要卸载的RAI发生变更时，可以使用该命令删除已有的配置。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAI|路由区名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~50个字符。|路由区名称，系统给每个路由区指定了名称，系统内部根据该名称关联对应的路由区。






[](None)命令举例 


删除路由区名为rai1的基于RAI号段的负荷卸载配配置。
DEL UNLOADRAI:RAI="rai1"; 








父主题： [基于RAI的负荷卸载配置](../../zh-CN/tree/N_12605354.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除全部基于RAI的负荷卸载配置(DEL UNLOADRAI ALL) 
### 删除全部基于RAI的负荷卸载配置(DEL UNLOADRAI ALL) 


[](None)命令功能 


该命令用于删除全部基于RAI号段的负荷卸载配配置。需要卸载的RAI发生变更，配置的RAI条目较多时可以使用该命令便捷删除。 




[](None)注意事项 

无。


[](None)命令举例 


删除全部基于RAI号段的负荷卸载配配置。
DEL UNLOADRAI ALL; 








父主题： [基于RAI的负荷卸载配置](../../zh-CN/tree/N_12605354.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询基于RAI的负荷卸载配置(SHOW UNLOADRAI) 
### 查询基于RAI的负荷卸载配置(SHOW UNLOADRAI) 


[](None)命令功能 


该命令用于查询基于RAI号段的负荷卸载配配置。可根据特定的RAI用以查看该号段是否在基于RAI的负荷卸载配置中；可按默认方式执行该命令来查看基于RAI的负荷卸载配置中的所有RAI。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAI|路由区名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|路由区名称，系统给每个路由区指定了名称，系统内部根据该名称关联对应的路由区。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAI|路由区名|参数可选性:任选参数；参数类型:字符型。|路由区名称，系统给每个路由区指定了名称，系统内部根据该名称关联对应的路由区。






[](None)命令举例 


查询基于RAI号段的负荷卸载配配置。
SHOW UNLOADRAI; 


`

命令 (No.1): SHOW UNLOADRAI

操作维护    路由区名
--------------------
复制 删除   rai1
--------------------
记录数 1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [基于RAI的负荷卸载配置](../../zh-CN/tree/N_12605354.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 基于MSISDN号段的负荷卸载配置 
## 基于MSISDN号段的负荷卸载配置 


[](None)背景知识 

            
            SGSN的负荷卸载，可支持针对指定的MSISDN号段的SGSN用户进行卸载；从而满足运营商出于管理目的，对指定号段的用户重分配；同时也是分批卸载的一种方式。
        


[](None)功能描述 


基于MSISDN号段的负荷卸载配置用于指定需要进行负荷卸载的MSISDN号段。 



                执行动态管理中请求负荷卸载命令
                [EXEC UNLOAD](../mml/1263022.html)
                时，如果SGSN卸载方式参数设置为按指定MSISDN号段卸载，则将使用本配置中配置的MSISDN号段作为指定的MSISDN号段。
            




[](None)相关主题 



 

新增基于MSISDN号段的负荷卸载配置(ADD UNLOADMSISDN)
 

 

删除基于MSISDN号段的负荷卸载配置(DEL UNLOADMSISDN)
 

 

删除全部基于MSISDN号段的负荷卸载配置(DEL UNLOADMSISDN ALL)
 

 

查询基于MSISDN号段的负荷卸载配置(SHOW UNLOADMSISDN)
 

 








父主题： [FLEX配置](../../zh-CN/tree/N_1254218.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增基于MSISDN号段的负荷卸载配置(ADD UNLOADMSISDN) 
### 新增基于MSISDN号段的负荷卸载配置(ADD UNLOADMSISDN) 


[](None)命令功能 


新增基于MSISDN号段的负荷卸载配置。当SGSN执行按MSISDN号段的负荷卸载时，只有MSISDN处于该配置的号段内的终端才满足负荷卸载条件，SGSN才会在附着流程或者路由更新流程为其分配包含NULL NRI的PTMSI以及重分配周期性路由更新定时器时长。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MSISDN|MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|MSISDN(MS international PSTN/ISDN Number)是移动用户号码，是主叫用户为呼叫移动通信网中用户所需拨号的号码。MSISDN号码最长是15位数字，由CC+NDC+SN三部分组成。CC是国家码，NDC是国家目的码，SN是用户号码。根据需要卸载的MSISDN范围，在该项配置中填写长度在1到15的MSISDN号段。






[](None)命令举例 


新增MSISDN号段为8613675138的负荷卸载配置。
ADD UNLOADMSISDN:MSISDN="8613675138"; 








父主题： [基于MSISDN号段的负荷卸载配置](../../zh-CN/tree/N_12605794.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除基于MSISDN号段的负荷卸载配置(DEL UNLOADMSISDN) 
### 删除基于MSISDN号段的负荷卸载配置(DEL UNLOADMSISDN) 


[](None)命令功能 


删除一条基于MSISDN号段的负荷卸载配置。当需要卸载的MSISDN号段发生变更时，可以使用该命令删除已有的配置。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MSISDN|MSISDN|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|MSISDN(MS international PSTN/ISDN Number)是移动用户号码，是主叫用户为呼叫移动通信网中用户所需拨号的号码。MSISDN号码最长是15位数字，由CC+NDC+SN三部分组成。CC是国家码，NDC是国家目的码，SN是用户号码。根据需要卸载的MSISDN范围，在该项配置中填写长度在1到15的MSISDN号段。






[](None)命令举例 


删除MSISDN号段为8613675138的负荷卸载配置。
DEL UNLOADMSISDN:MSISDN="8613675138"; 








父主题： [基于MSISDN号段的负荷卸载配置](../../zh-CN/tree/N_12605794.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除全部基于MSISDN号段的负荷卸载配置(DEL UNLOADMSISDN ALL) 
### 删除全部基于MSISDN号段的负荷卸载配置(DEL UNLOADMSISDN ALL) 


[](None)命令功能 


删除全部基于MSISDN号段的负荷卸载配置。需要卸载的MSISDN号段发生变更，配置的MSISDN号段条目较多时可以使用该命令便捷删除。 




[](None)注意事项 


无。 




[](None)命令举例 


删除所有的基于MSISDN号段的负荷卸载配置。
DEL UNLOADMSISDN ALL; 








父主题： [基于MSISDN号段的负荷卸载配置](../../zh-CN/tree/N_12605794.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询基于MSISDN号段的负荷卸载配置(SHOW UNLOADMSISDN) 
### 查询基于MSISDN号段的负荷卸载配置(SHOW UNLOADMSISDN) 


[](None)命令功能 


查询基于MSISDN号段的负荷卸载配置。可根据特定的MSISDN号段来查看该号段是否在基于MSISDN号段的负荷卸载配置中；可按默认方式执行该命令来查看基于MSISDN号段的负荷卸载配置中的所有MSISDN号段。 




[](None)注意事项 


无。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MSISDN|MSISDN|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|MSISDN(MS international PSTN/ISDN Number)是移动用户号码，是主叫用户为呼叫移动通信网中用户所需拨号的号码。MSISDN号码最长是15位数字，由CC+NDC+SN三部分组成。CC是国家码，NDC是国家目的码，SN是用户号码。根据需要卸载的MSISDN范围，在该项配置中填写长度在1到15的MSISDN号段。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MSISDN|MSISDN|参数可选性:任选参数；参数类型:字符型。|MSISDN(MS international PSTN/ISDN Number)是移动用户号码，是主叫用户为呼叫移动通信网中用户所需拨号的号码。MSISDN号码最长是15位数字，由CC+NDC+SN三部分组成。CC是国家码，NDC是国家目的码，SN是用户号码。根据需要卸载的MSISDN范围，在该项配置中填写长度在1到15的MSISDN号段。






[](None)命令举例 


查询基于MSISDN号段的负荷卸载配置。
SHOW UNLOADMSISDN; 


`

命令 (No.1): SHOW UNLOADMSISDN;

操作维护    MSISDN
------------------
复制 删除   8613675138
------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [基于MSISDN号段的负荷卸载配置](../../zh-CN/tree/N_12605794.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 指定SGSN卸载配置 
## 指定SGSN卸载配置 


[](None)背景知识 


POOL内的负荷重平衡，是通过对高负荷的SGSN进行卸载来实现用户迁移的。但普通的卸载并不指定目标SGSN，所以实际上被卸载的用户将按照RAN侧配置的POOL内各个SGSN的权重，迁移到POOL内的各个SGSN，这样重平衡的时间就会较长。如果在卸载时，将低负荷的SGSN指定为卸载的目标，那么用户就会迁移到指定的SGSN，从而缩短POOL内负荷重平衡的时间。 




[](None)功能描述 


指定SGSN卸载配置用来配置SGSN负荷卸载，是否需要指定目标SGSN，以及指定目标SGSN的NRI； 



                执行指定SGSN负荷卸载，需要首先进行本项配置，然后再执行SGSN负荷卸载请求操作
                [EXEC UNLOAD](../mml/1263022.html)
                ，这样负荷将卸载到指定的SGSN。
            




[](None)相关主题 



 

设置指定SGSN卸载配置(SET APPOINTSGSN)
 

 

查询指定SGSN卸载配置(SHOW APPOINTSGSN)
 

 








父主题： [FLEX配置](../../zh-CN/tree/N_1254218.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置指定SGSN卸载配置(SET APPOINTSGSN) 
### 设置指定SGSN卸载配置(SET APPOINTSGSN) 


[](None)命令功能 


该命令用于配置指定SGSN卸载开关，及目标SGSN的NRI。 


执行指定SGSN负荷卸载，需要首先打开指定SGSN卸载开关，配置目标SGSN的NRI；然后再执行SGSN负荷卸载请求操作[EXEC UNLOAD](1263022.html)，这样负荷将卸载到指定的SGSN。




[](None)注意事项 


该命令的参数“指定NRI”不能与FLEX NRI重复。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ISSPECNRI|是否指定SGSN卸载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否启用指定SGSN卸载功能。默认该功能关闭，表示不指定特定的SGSN。
SPECNRI|指定NRI|参数可选性:任选参数；参数类型:整数；参数范围为:0~1023。|目标SGSN的NRI。






[](None)命令举例 


修改指定SGSN卸载配置，关闭指定SGSN卸载开关，目标SGSN的NRI为“1”。 


SET APPOINTSGSN:ISSPECNRI="NO",SPECNRI=1; 








父主题： [指定SGSN卸载配置](../../zh-CN/tree/N_12605364.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询指定SGSN卸载配置(SHOW APPOINTSGSN) 
### 查询指定SGSN卸载配置(SHOW APPOINTSGSN) 


[](None)命令功能 


该命令用于查询已配置的指定SGSN卸载开关，及目标SGSN的NRI。 




[](None)注意事项 


无。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ISSPECNRI|是否指定SGSN卸载|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|是否启用指定SGSN卸载功能。默认该功能关闭，表示不指定特定的SGSN。
SPECNRI|指定NRI|参数可选性:任选参数；参数类型:整数。|目标SGSN的NRI。






[](None)命令举例 


查询指定SGSN卸载配置。 


SHOW APPOINTSGSN;  


`

命令 (No.6): SHOW APPOINTSGSN;

操作维护  是否指定SGSN卸载   指定NRI
------------------------------------
修改      否                 1
------------------------------------
记录数 1

命令执行成功（耗时 0.03 秒）。


` 








父主题： [指定SGSN卸载配置](../../zh-CN/tree/N_12605364.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 网元主备参数配置 
## 网元主备参数配置 


[](None)背景知识 

            
            POOL内两个异地的网元可以支持主备配置，其中主用、备用网元角色固定，备用网元仅在主用网元宕机时接替其工作，在主用网元恢复后退出服务。所以，备用网元需要实时检测主用网元的状态。
        


[](None)功能描述 

            
            无。
        


[](None)相关主题 



 

设置网元主备参数(SET NE BACKUP PARA)
 

 

查询网元主备参数(SHOW NE BACKUP PARA)
 

 








父主题： [FLEX配置](../../zh-CN/tree/N_1254218.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置网元主备参数(SET NE BACKUP PARA) 
### 设置网元主备参数(SET NE BACKUP PARA) 


[](None)命令功能 

设置网元主用、备用角色，以及备用网元检测主用网元的参数。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
BACKUPFLAG|是否备用网元|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用来配置本网元是否是备用网元。如果不是备用网元，不需要配置下面其他参数。
MASETERIP|主用网元IP地址|参数可选性:任选参数；参数类型:地址|当本网元为备用网元时，该参数用来配置主用网元的IP地址。
MASTERVRF|主用网元VRF|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|当本网元为备用网元时，该参数用来配置主用网元IP的 VRF。
TIMEOUT|检测超时时间(100ms)|参数可选性:任选参数；参数类型:整数；参数范围为:1~6000。|当本网元为备用网元时，该参数用来配置向主用网元检测的超时时长。
REPEATTIME|检测确认次数|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|当本网元为备用网元时，该参数用来配置向主用网元检测的超时次数。






[](None)命令举例 


设置网元主备参数。是否备用网元为是。 


SET NE BACKUP PARA:BACKUPFLAG="YES"; 








父主题： [网元主备参数配置](../../zh-CN/tree/N_12608633.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询网元主备参数(SHOW NE BACKUP PARA) 
### 查询网元主备参数(SHOW NE BACKUP PARA) 


[](None)命令功能 

查询网元主用、备用角色，以及备用网元检测主用网元的参数。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
BACKUPFLAG|是否备用网元|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用来配置本网元是否是备用网元。如果不是备用网元，不需要配置下面其他参数。
MASETERIP|主用网元IP地址|参数可选性:任选参数；参数类型:地址|当本网元为备用网元时，该参数用来配置主用网元的IP地址。
MASTERVRF|主用网元VRF|参数可选性:任选参数；参数类型:整数。|当本网元为备用网元时，该参数用来配置主用网元IP的 VRF。
TIMEOUT|检测超时时间(100ms)|参数可选性:任选参数；参数类型:整数。|当本网元为备用网元时，该参数用来配置向主用网元检测的超时时长。
REPEATTIME|检测确认次数|参数可选性:任选参数；参数类型:整数。|当本网元为备用网元时，该参数用来配置向主用网元检测的超时次数。






[](None)命令举例 


是否备用网元。 


SHOW NE BACKUP PARA; 


`
命令 (No.17): SHOW NE BACKUP PARA

操作维护 是否备用网元 主用网元IP地址 主用网元VRF 检测超时时间(100ms) 检测确认次数 
-----------------------------------------------------------------------------
修改     是           0.0.0.0        0           0                   0
-----------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.033 秒）。
` 








父主题： [网元主备参数配置](../../zh-CN/tree/N_12608633.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 用户地址号段属性配置 
# 用户地址号段属性配置 


[](None)背景知识 

            
            运营商分配的用户标识IMSI和MSISDN具备一定的规律性，不同的号码段，往往代表某一类用户，比如用户的归属地等。系统可以配置特定号段的用户属性和权限，实现相关的业务处理和功能。
        


[](None)功能描述 


“用户地址号段属性配置”主要包括“漫游用户统计功能”和“IMSI限制附着用户数和PDP上下文数功能”的相关配置。 


对于漫游用户统计功能，配置流程如下： 



                1、开启漫游用户统计功能：
                [SET ROAMER STATCTR](../mml/1260115.html)




                2、配置本地用户地址号段属性：
                [ADD LOCAL NUMSEG](../mml/1260120.html)





[](None)相关主题 



 

漫游用户统计功能控制配置
 

 

本地用户地址号段属性配置
 

 

IMSI限制附着用户数和PDP上下文数配置
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 漫游用户统计功能控制配置 
## 漫游用户统计功能控制配置 


[](None)背景知识 

            
            漫游用户统计功能是指SGSN根据配置的本地IMSI号段或本地MSISDN号段，判断用户是否为漫游用户，实现对漫游用户的统计功能。
        


[](None)功能描述 



                “漫游用户统计功能控制配置”用来设置SGSN是否支持“漫游用户统计功能”。如果配置为支持，通过
                [ADD LOCAL NUMSEG](../mml/1260120.html)
                命令增加本地IMSI号段或者本地ISDN号段。
            


漫游用户统计功能涉及的性能统计项包括“SGSN附着的本地用户数(基于本地用户地址号段配置)”、“SGSN附着的漫游用户数(基于本地用户地址号段配置)”、“SGSN激活会话的本地用户数(基于本地用户地址号段配置)”、“SGSN激活会话的漫游用户数(基于本地用户地址号段配置)”等。 




[](None)相关主题 



 

设置漫游用户统计功能控制配置(SET ROAMER STATCTR)
 

 

查询漫游用户统计功能控制配置(SHOW ROAMER STATCTR)
 

 








父主题： [用户地址号段属性配置](../../zh-CN/tree/N_1254219.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置漫游用户统计功能控制配置(SET ROAMER STATCTR) 
### 设置漫游用户统计功能控制配置(SET ROAMER STATCTR) 


[](None)命令功能 

该命令用于设置SGSN是否支持漫游用户统计功能。当运营商要求实现对漫游用户个数进行统计时，使用该命令。该命令设置为“YES”成功后，当用户接入到SGSN时，SGSN判断该IMSI/MSISDN用户是否在命令[ADD LOCAL NUMSEG](1260120.html) 配置的本地IMSI/MSISDN号段，如果不在本地IMSI/MSISDN号段，则该判断IMSI/MSISDN用户为漫游用户，将该用户统计到漫游用户中。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SUPTYPE|是否支持漫游用户统计|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持漫游用户统计。NO：不支持YES：支持






[](None)命令举例 


设置SGSN支持漫游用户统计功能。
SET ROAMER STATCTR:SUPTYPE="YES"; 








父主题： [漫游用户统计功能控制配置](../../zh-CN/tree/N_12601154.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询漫游用户统计功能控制配置(SHOW ROAMER STATCTR) 
### 查询漫游用户统计功能控制配置(SHOW ROAMER STATCTR) 


[](None)命令功能 

该命令用于查询是否支持漫游用户统计功能。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SUPTYPE|是否支持漫游用户统计|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置SGSN是否支持漫游用户统计。NO：不支持YES：支持






[](None)命令举例 


查询是否支持漫游用户统计;
SHOW ROAMER STATCTR; 


`

命令 (No.1): SHOW ROAMER STATCTR

操作维护  是否支持漫游用户统计
------------------------------
修改      不支持
------------------------------
记录数 1

命令执行成功（耗时 0.032 秒）。
` 








父主题： [漫游用户统计功能控制配置](../../zh-CN/tree/N_12601154.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 本地用户地址号段属性配置 
## 本地用户地址号段属性配置 


[](None)背景知识 

            
            漫游用户统计功能是指SGSN根据配置的本地IMSI号段或本地MSISDN号段，判断用户是否为漫游用户，实现对漫游用户的统计功能。
        


[](None)功能描述 


“本地用户地址号段属性配置”用来设置本地用户的IMSI号段或者MSISDN号段，SGSN通过匹配此列表，作为判断用户是否是漫游用户的依据。 


注意事项： 



                该配置生效的前提是已通过
                [SET ROAMER STATCTR](../mml/1260115.html)
                命令设置了支持漫游用户统计功能。
            




[](None)相关主题 



 

新增本地用户地址号段属性配置(ADD LOCAL NUMSEG)
 

 

修改本地用户地址号段属性配置(SET LOCAL NUMSEG)
 

 

删除本地用户地址号段属性配置(DEL LOCAL NUMSEG)
 

 

查询本地用户地址号段属性配置(SHOW LOCAL NUMSEG)
 

 








父主题： [用户地址号段属性配置](../../zh-CN/tree/N_1254219.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增本地用户地址号段属性配置(ADD LOCAL NUMSEG) 
### 新增本地用户地址号段属性配置(ADD LOCAL NUMSEG) 


[](None)命令功能 

该命令用于新增本地用户地址号段属性配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ADDRNUMSEG|地址号段|参数可选性:必选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于配置本地用户号段，字段长度范围为5-15。
NUMSEGTYPE|号段类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:IMSI。|该参数用于配置本地地址号段的类型，可以是IMSI号段和MSISDN号段。






[](None)命令举例 


增加一个值为“46001”的IMSI号段；
ADD LOCAL NUMSEG:ADDRNUMSEG="46001",NUMSEGTYPE="IMSI"; 








父主题： [本地用户地址号段属性配置](../../zh-CN/tree/N_12601204.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改本地用户地址号段属性配置(SET LOCAL NUMSEG) 
### 修改本地用户地址号段属性配置(SET LOCAL NUMSEG) 


[](None)命令功能 

该命令用于修改本地用户地址号段属性配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ADDRNUMSEG|地址号段|参数可选性:必选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于配置本地用户号段，字段长度范围为5-15。
NUMSEGTYPE|号段类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置本地地址号段的类型，可以是IMSI号段和MSISDN号段。






[](None)命令举例 


将“46001”号段类型由IMSI修改为MSISDN；
SET LOCAL NUMSEG:ADDRNUMSEG="46001",NUMSEGTYPE="MSISDN"; 








父主题： [本地用户地址号段属性配置](../../zh-CN/tree/N_12601204.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除本地用户地址号段属性配置(DEL LOCAL NUMSEG) 
### 删除本地用户地址号段属性配置(DEL LOCAL NUMSEG) 


[](None)命令功能 

该命令用于删除本地用户地址号段属性配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ADDRNUMSEG|地址号段|参数可选性:必选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于配置本地用户号段，字段长度范围为5-15。
NUMSEGTYPE|号段类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置本地地址号段的类型，可以是IMSI号段和MSISDN号段。






[](None)命令举例 


将“46001”号段配置删除；
DEL LOCAL NUMSEG:ADDRNUMSEG="46001",NUMSEGTYPE="MSISDN"; 








父主题： [本地用户地址号段属性配置](../../zh-CN/tree/N_12601204.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询本地用户地址号段属性配置(SHOW LOCAL NUMSEG) 
### 查询本地用户地址号段属性配置(SHOW LOCAL NUMSEG) 


[](None)命令功能 

该命令用于查询本地用户地址号段属性配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ADDRNUMSEG|地址号段|参数可选性:任选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于配置本地用户号段，字段长度范围为5-15。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
ADDRNUMSEG|地址号段|参数可选性:任选参数；参数类型:字符型；参数范围为:5~15个字符。|该参数用于配置本地用户号段，字段长度范围为5-15。
SEGTYPE|号段类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数为输出参数，用于表示本地地址号段的类型，可能是IMSI号段或MSISDN号段。






[](None)命令举例 


查询指定的号段“46001”具体配置信息;
SHOW LOCAL NUMSEG:ADDRNUMSEG="46001"; 


`

命令 (No.1): SHOW LOCAL NUMSEG:ADDRNUMSEG="46001";

操作维护         地址号段   号段类型
------------------------------------
复制 修改 删除   46001      IMSI号段
------------------------------------
记录数 1

命令执行成功（耗时 0.033 秒）。
` 








父主题： [本地用户地址号段属性配置](../../zh-CN/tree/N_12601204.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## IMSI限制附着用户数和PDP上下文数配置 
## IMSI限制附着用户数和PDP上下文数配置 


[](None)背景知识 

            
            IMSI限制附着用户数和PDP上下文数功能，用于运营商对某些IMSI号段，设置该号段允许接入SGSN的最大附着用户数和最大PDP上下文数目。
        


[](None)功能描述 


“IMSI限制附着用户数和PDP上下文数配置”配置流程如下： 







                        设置“IMSI限制附着用户数和PDP上下文数功能”开关，配置命令为
                        [SET IMSICTRL USERPDP SPRT](../mml/1260263.html)








                        配置特定的IMSI号段及其对应的允许接入的附着用户数和允许接入的PDP上下文数。命令为：
                        [ADD IMSICTRL USERPDP](../mml/1260266.html)







SGSN最大支持配置100个IMSI号段。 


如果IMSI号段的附着用户数或PDP上下文数达到相应限制，SGSN将拒绝该号段的用户附着或拒绝用户PDP激活。 




[](None)相关主题 



 

设置是否支持IMSI号段附着激活数(SET IMSICTRL USERPDP SPRT)
 

 

查询是否支持IMSI号段附着激活数(SHOW IMSICTRL USERPDP SPRT)
 

 

新增IMSI号段附着激活数配置(ADD IMSICTRL USERPDP)
 

 

修改IMSI号段附着激活数配置(SET IMSICTRL USERPDP)
 

 

删除IMSI号段附着激活数配置(DEL IMSICTRL USERPDP)
 

 

查询IMSI号段附着激活数配置(SHOW IMSICTRL USERPDP)
 

 








父主题： [用户地址号段属性配置](../../zh-CN/tree/N_1254219.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置是否支持IMSI号段附着激活数(SET IMSICTRL USERPDP SPRT) 
### 设置是否支持IMSI号段附着激活数(SET IMSICTRL USERPDP SPRT) 


[](None)命令功能 

该命令用于设置SGSN是否支持根据MS的IMSI号段，对此号段允许的最大附着用户数和PDP上下文数进行限制。


[](None)注意事项 

该命令只适用于SGSN网元。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSICTRL|是否支持IMSI号段限制附着激活数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置为“是”：表示SGSN支持根据MS的IMSI号段，对附着用户数和PDP上下文数进行限制。设置为“否”：表示SGSN不支持根据MS的IMSI号段，对附着用户数和PDP上下文数进行限制。






[](None)命令举例 


设置支持IMSI号段附着激活数。
SET IMSICTRL USERPDP SPRT:IMSICTRL="YES"; 








父主题： [IMSI限制附着用户数和PDP上下文数配置](../../zh-CN/tree/N_12602634.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询是否支持IMSI号段附着激活数(SHOW IMSICTRL USERPDP SPRT) 
### 查询是否支持IMSI号段附着激活数(SHOW IMSICTRL USERPDP SPRT) 


[](None)命令功能 

该命令用于查询SGSN是否支持根据MS的IMSI号段，对此号段允许的最大附着用户数和PDP上下文数进行限制。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSICTRL|是否支持IMSI号段限制附着激活数|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置为“是”：表示SGSN支持根据MS的IMSI号段，对附着用户数和PDP上下文数进行限制。设置为“否”：表示SGSN不支持根据MS的IMSI号段，对附着用户数和PDP上下文数进行限制。






[](None)命令举例 


查询是否支持IMSI号段附着激活数。
SHOW IMSICTRL USERPDP SPRT; 


`

命令 (No.1): SHOW IMSICTRL USERPDP SPRT

操作维护  是否支持IMSI号段限制附着激活数
----------------------------------------
修改      不支持
----------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [IMSI限制附着用户数和PDP上下文数配置](../../zh-CN/tree/N_12602634.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增IMSI号段附着激活数配置(ADD IMSICTRL USERPDP) 
### 新增IMSI号段附着激活数配置(ADD IMSICTRL USERPDP) 


[](None)命令功能 


该命令用于在SGSN支持根据MS的IMSI号段对附着用户数和PDP上下文数进行限制的情况下，设置某个IMSI号段中允许的最大附着用户数和最大PDP上下文数。 


对于特定的IMSI号段，当达到本命令设置的“允许接入的附着用户数”和“允许接入的PDP上下文数”后，SGSN无法再继续附着和激活用户。 




[](None)注意事项 


该命令只适用于SGSN网元。 


此命令的前提条件为设置[SET IMSICTRL USERPDP SPRT](1260263.html) :IMSICTRL="YES"。




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示的IMSI号段。如果设置了多条记录，则各条记录中的IMSI号段不能相互包含或重合。首位不能为0。
MMNUMCFG|允许接入的附着用户数|参数可选性:任选参数；参数类型:整数；参数范围为:0~15000000。默认值:10000。|该参数用于配置特定IMSI号段允许的最大附着用户数。
PDPNUMCFG|允许接入的PDP上下文数|参数可选性:任选参数；参数类型:整数；参数范围为:0~30000000。默认值:20000。|该参数用于配置特定IMSI号段允许的最大PDP上下文数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






[](None)命令举例 


新增IMSI号段附着激活数配置，设置IMSI号段为46001，设置允许接入的附着用户数为10000，设置允许接入的PDP上下文数为200000。
ADD IMSICTRL USERPDP:IMSI="46001",MMNUMCFG=10000,PDPNUMCFG=200000; 








父主题： [IMSI限制附着用户数和PDP上下文数配置](../../zh-CN/tree/N_12602634.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改IMSI号段附着激活数配置(SET IMSICTRL USERPDP) 
### 修改IMSI号段附着激活数配置(SET IMSICTRL USERPDP) 


[](None)命令功能 

该命令用于修改某个IMSI号段中，允许的最大附着用户数和最大PDP上下文数。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示的IMSI号段。如果设置了多条记录，则各条记录中的IMSI号段不能相互包含或重合。首位不能为0。
MMNUMCFG|允许接入的附着用户数|参数可选性:任选参数；参数类型:整数；参数范围为:0~15000000。|该参数用于配置特定IMSI号段允许的最大附着用户数。
PDPNUMCFG|允许接入的PDP上下文数|参数可选性:任选参数；参数类型:整数；参数范围为:0~30000000。|该参数用于配置特定IMSI号段允许的最大PDP上下文数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






[](None)命令举例 


修改IMSI号段为46001的IMSI号段附着激活数配置，将允许接入的附着用户数修改为20000，将允许接入的PDP上下文数修改为300000。
SET IMSICTRL USERPDP:IMSI="46001",MMNUMCFG=20000,PDPNUMCFG=300000; 








父主题： [IMSI限制附着用户数和PDP上下文数配置](../../zh-CN/tree/N_12602634.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除IMSI号段附着激活数配置(DEL IMSICTRL USERPDP) 
### 删除IMSI号段附着激活数配置(DEL IMSICTRL USERPDP) 


[](None)命令功能 

该命令用于取消对某个IMSI号段允许的最大附着用户数和最大PDP上下文数进行限制的功能。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|该参数表示的IMSI号段。如果设置了多条记录，则各条记录中的IMSI号段不能相互包含或重合。首位不能为0。






[](None)命令举例 


删除IMSI号段为46001的IMSI号段附着激活数配置。
DEL IMSICTRL USERPDP:IMSI="46001"; 








父主题： [IMSI限制附着用户数和PDP上下文数配置](../../zh-CN/tree/N_12602634.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询IMSI号段附着激活数配置(SHOW IMSICTRL USERPDP) 
### 查询IMSI号段附着激活数配置(SHOW IMSICTRL USERPDP) 


[](None)命令功能 

该命令用于根据IMSI号段查询，当前系统中设置的此IMSI号段允许的最大附着用户数和最大PDP上下文数。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数表示的IMSI号段。如果设置了多条记录，则各条记录中的IMSI号段不能相互包含或重合。首位不能为0。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSICTRLID|限制标识|参数可选性:任选参数；参数类型:整数。|该参数为输出参数，在执行ADD IMSICTRL USERPDP命令后，由系统自动生成，无需设置，可通过SHOW IMSICTRL USERPDP 命令进行查询。
IMSI|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:0~15个字符。|该参数表示的IMSI号段。如果设置了多条记录，则各条记录中的IMSI号段不能相互包含或重合。首位不能为0。
MMNUMCFG|允许接入的附着用户数|参数可选性:任选参数；参数类型:整数。|该参数用于配置特定IMSI号段允许的最大附着用户数。
PDPNUMCFG|允许接入的PDP上下文数|参数可选性:任选参数；参数类型:整数。|该参数用于配置特定IMSI号段允许的最大PDP上下文数。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该参数表示此条配置数据对应的记录标识，用于增加配置命令的描述信息，以便于维护人员进行理解。






[](None)命令举例 


查询IMSI号段附着激活数配置。
SHOW IMSICTRL USERPDP:IMSI="46001"; 


`
命令 (No.1): SHOW IMSICTRL USERPDP:IMSI="46001";

操作维护         限制标识   IMSI号段   允许接入的附着用户数   允许接入的PDP上下文数   用户别名
----------------------------------------------------------------------------------------------
复制 修改 删除   1          46001      10000                  200000                  
----------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.045 秒）。
` 








父主题： [IMSI限制附着用户数和PDP上下文数配置](../../zh-CN/tree/N_12602634.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# RAB指派失败统计控制配置 
# RAB指派失败统计控制配置 


[](None)背景知识 


根据23.060协议规定，终端用户在3G进行激活过程中，会向RNC要求进行RAB指派，RNC可能由于某些原因无法RAB指派成功，会向终端用户返回RAB指派失败。 


RAB（无线接入承载，Radio Access Bearer）用于指明接入层提供给非接入层的用于用户设备和核心网络间用户数据传输的服务。 




[](None)功能描述 


当终端用户在3G接入后，发起PDP激活流程，RAB指派过程失败的时候，根据RNC返回的失败原因值进行控制是否将此次失败上报到性能统计。 


此功能基于RNC局向进行控制。 




[](None)相关主题 



 

新增RAB指派失败统计控制(ADD RAB FAIL CONTROL)
 

 

修改RAB指派失败统计控制(SET RAB FAIL CONTROL)
 

 

删除RAB指派失败统计控制(DEL RAB FAIL CONTROL)
 

 

查询RAB指派失败统计控制(SHOW RAB FAIL CONTROL)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增RAB指派失败统计控制(ADD RAB FAIL CONTROL) 
## 新增RAB指派失败统计控制(ADD RAB FAIL CONTROL) 


[](None)命令功能 

新增RAB指派失败统计控制。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RNCID|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于配置RNC局向ID。RNC局向ID是通过ADD ADJOFC命令配置的，此命令中的RNCOFFID对应已配置的RNC局向ID 。
IFALLEPTTMR|是否对超时之外的所有失败原因生效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于配置是否将超时之外的所有失败原因导致的失败情况都上报到性能统计中。
IFTIMEROUT|是否对RAB 指派超时生效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|该参数用于配置是否将RAB指派超时这种情况上报到性能统计中。
FAILCAUSE|失败原因列表|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于配置将哪些失败原因上报到性能统计中。






[](None)命令举例 


新增RAB指派失败统计控制。 


ADD RAB FAIL CONTROL:RNCID=1,IFALLEPTTMR=NO,IFTIMEROUT=NO,FAILCAUSE="1"; 








父主题： [RAB指派失败统计控制配置](../../zh-CN/tree/N_1251220.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改RAB指派失败统计控制(SET RAB FAIL CONTROL) 
## 修改RAB指派失败统计控制(SET RAB FAIL CONTROL) 


[](None)命令功能 

修改RAB指派失败统计控制。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RNCID|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于配置RNC局向ID。RNC局向ID是通过ADD ADJOFC命令配置的，此命令中的RNCOFFID对应已配置的RNC局向ID 。
IFALLEPTTMR|是否对超时之外的所有失败原因生效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否将超时之外的所有失败原因导致的失败情况都上报到性能统计中。
IFTIMEROUT|是否对RAB 指派超时生效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否将RAB指派超时这种情况上报到性能统计中。
FAILCAUSE|失败原因列表|参数可选性:任选参数；参数类型:整数；参数范围为:1~255。|该参数用于配置将哪些失败原因上报到性能统计中。






[](None)命令举例 


修改RAB指派失败统计控制。 


SET RAB FAIL CONTROL:RNCID=1,IFALLEPTTMR=NO,IFTIMEROUT=NO,FAILCAUSE="1"; 








父主题： [RAB指派失败统计控制配置](../../zh-CN/tree/N_1251220.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除RAB指派失败统计控制(DEL RAB FAIL CONTROL) 
## 删除RAB指派失败统计控制(DEL RAB FAIL CONTROL) 


[](None)命令功能 

删除RAB指派失败统计控制。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RNCID|RNC局向号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4096。|该参数用于配置RNC局向ID。RNC局向ID是通过ADD ADJOFC命令配置的，此命令中的RNCOFFID对应已配置的RNC局向ID 。






[](None)命令举例 


删除RAB指派失败统计控制。 


DEL RAB FAIL CONTROL:RNCID=1; 








父主题： [RAB指派失败统计控制配置](../../zh-CN/tree/N_1251220.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询RAB指派失败统计控制(SHOW RAB FAIL CONTROL) 
## 查询RAB指派失败统计控制(SHOW RAB FAIL CONTROL) 


[](None)命令功能 

查询RAB指派失败统计控制。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RNCID|RNC局向号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4096。|该参数用于配置RNC局向ID。RNC局向ID是通过ADD ADJOFC命令配置的，此命令中的RNCOFFID对应已配置的RNC局向ID 。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RNCID|RNC局向号|参数可选性:任选参数；参数类型:整数。|该参数用于配置RNC局向ID。RNC局向ID是通过ADD ADJOFC命令配置的，此命令中的RNCOFFID对应已配置的RNC局向ID 。
IFALLEPTTMR|是否对超时之外的所有失败原因生效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否将超时之外的所有失败原因导致的失败情况都上报到性能统计中。
IFTIMEROUT|是否对RAB 指派超时生效|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于配置是否将RAB指派超时这种情况上报到性能统计中。
FAILCAUSE|失败原因列表|参数可选性:任选参数；参数类型:字符型。|该参数用于配置将哪些失败原因上报到性能统计中。






[](None)命令举例 


查询RAB指派失败统计控制。 


SHOW RAB FAIL CONTROL 


`

(No.1) : SHOW RAB FAIL CONTROL:
-----------------NFS_MMESGSN_0----------------
操作维护       RNC局向号 是否对超时之外的所有失败原因生效 是否对RAB 指派超时生效 失败原因列表 
----------------------------------------------------------------------------------------------
复制 修改 删除 1         否                               是                     1            
----------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-07 15:56:25 耗时: 1.941 秒
` 








父主题： [RAB指派失败统计控制配置](../../zh-CN/tree/N_1251220.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MME终端双栈数据配置 
# MME终端双栈数据配置 


[](None)背景知识 


终端双栈功能是指UE注册到EPC网络后，UE发起PDN连接建立请求，指示申请IPv4v6双栈地址，PGW可以根据策略判断为用户同时分配IPv4和IPv6地址。SGW将PGW分配的IPv4v6双栈地址携带给MME，MME发送给UE。通过双栈功能，UE可以通过激活一个承载获取IPv4和IPv6地址和转发IPv4和IPv6报文，不需要激活两个承载分别获取IPv4和IPv6地址。 


UE激活双栈PDN连接后，可以同时访问IPv4的PDN和IPv6的PDN。 




[](None)功能描述 


终端双栈功能是全网规划的，需要各网元支持，MME、PGW、SGW默认支持双栈功能，符合以下两个条件时，可以开通终端双栈功能。 



 

PGW支持终端双栈，且同时连接IPv4 PDN和IPv6 PDN。
 

 

MME连接的SGSN都支持终端双栈。
 

 


"MME终端双栈数据配置"用于MME判断网络侧对UE双栈的支持情况，如网络侧不支持终端双栈，MME根据此处的配置选择给UE分配的单栈地址类型。包括以下2个设置：本MME连接的SGSN是否都支持终端双栈和优选PDN类型。 


在以下2种情况下，MME判断为网络侧不支持终端双栈，MME根据配置的“优选PDN类型”指定为UE分配的单栈地址类型。 



 

UE请求终端双栈地址，但UE在HSS的签约只允许为UE分配IPv4和IPv6单栈地址。
 

 

UE请求终端双栈地址，UE在HSS的签约也允许终端双栈地址，但MME连接的SGSN不都支持终端双栈。
 

 


说明： 


HSS中可以签约允许的地址类型有4种：IPv4v6（终端双栈）、IPv4（终端单栈）、IPv6（终端单栈）、IPv4或IPv6（终端单栈，允许IPv4或IPv6）。UE请求双栈地址，但只签约了终端单栈，则只能使用终端单栈。 




[](None)相关主题 



 

设置MME终端双栈数据(SET MME DUAL STACK)
 

 

查询MME终端双栈数据(SHOW MME DUAL STACK)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置终端双栈数据(SET MME DUAL STACK) 
## 设置终端双栈数据(SET MME DUAL STACK) 


[](None)命令功能 


该命令用于设置终端支持IP双栈功能，使用该命令成功后，用户申请PDN连接时，UE会支持终端双栈能力。 


在HSS上签约双栈功能后，还需要在MME上配置命令[SET MME DUAL STACK](1260190.html)中的MMEDUALSTACK参数为YES才能实现终端双栈功能。 




[](None)注意事项 

如果用户在HSS上签约了单栈功能，则不需要进行该项配置。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MMEPDNTYPE|优选PDN类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置具有双栈功能的用户接入PDN时，优先选择使用的IP地址类型。取值含义：“优选IPv4”：用户接入PDN时，优先选择使用IPv4类型的地址接入。 “优选IPv6”：用户接入PDN时，优先选择使用IPv6类型的地址接入。 如果用户在HSS签约了单栈类型的地址，则用户使用签约的地址类型接入PDN。
MMEDUALSTACK|UE切换的所有SGSN支持终端双栈|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置UE在不同网络间切换时，所有源SGSN和目的SGSN是否支持终端双栈功能。取值含义：“否NO”：不支持“是YES”：支持






[](None)命令举例 


设置双栈数据，设置优选PDN类型为IPv4，UE切换的所有SGSN支持终端双栈。
SET MME DUAL STACK:MMEPDNTYPE="IPv4",MMEDUALSTACK="YES"; 








父主题： [MME终端双栈数据配置](../../zh-CN/tree/N_12542091.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询终端双栈数据(SHOW MME DUAL STACK) 
## 查询终端双栈数据(SHOW MME DUAL STACK) 


[](None)命令功能 

该命令用于查询终端双栈数据。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
MMEPDNTYPE|优选PDN类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置具有双栈功能的用户接入PDN时，优先选择使用的IP地址类型。取值含义：“优选IPv4”：用户接入PDN时，优先选择使用IPv4类型的地址接入。 “优选IPv6”：用户接入PDN时，优先选择使用IPv6类型的地址接入。 如果用户在HSS签约了单栈类型的地址，则用户使用签约的地址类型接入PDN。
MMEDUALSTACK|UE切换的所有SGSN支持终端双栈|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置UE在不同网络间切换时，所有源SGSN和目的SGSN是否支持终端双栈功能。取值含义：“否NO”：不支持“是YES”：支持






[](None)命令举例 


查询终端双栈数据。
SHOW MME DUAL STACK; 


`

命令 (No.1): SHOW MME DUAL STACK

操作维护  优选PDN类型   UE切换的所有SGSN支持终端双栈
----------------------------------------------------
修改      优选IPv4      是
----------------------------------------------------
记录数 1

命令执行成功（耗时 0.042 秒）。
` 








父主题： [MME终端双栈数据配置](../../zh-CN/tree/N_12542091.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SGSN终端双栈数据配置 
# SGSN终端双栈数据配置 


[](None)背景知识 


终端双栈功能是指UE通过激活一个承载同时获取IPv4和IPv6地址，发送IPv4和IPv6报文，从而同时访问IPv4的PDN和IPv6的PDN。启用终端双栈后，UE不需要激活两个承载分别获取IPv4和IPv6地址。 


流程如下：UE注册到GPRS网络后，发起激活请求，指示申请IPv4和IPv6双栈地址，SGSN如果判断可以支持终端双栈(SGSN支持双栈，用户签约允许双栈，且与SGSN连接的SGSN都支持双栈，三个条件同时满足则SGSN认为支持终端双栈），则向GGSN发起请求，GGSN根据配置的策略判断可以为UE同时分配IPv4和IPv6地址。GGSN将分配的IPv4v6双栈地址携带给SGSN，SGSN发送给UE。 




[](None)功能描述 


终端双栈功能是全网规划的，需要各网元支持，SGSN、GGSN都需要支持双栈功能，开通终端双栈功能，需要满足以下三个条件。 



 

GGSN支持终端双栈，且同时连接IPv4 PDN和IPv6 PDN。
 

 

SGSN支持终端双栈。
 

 

SGSN连接的SGSN都支持终端双栈。
 

 


“SGSN终端双栈数据配置”用于SGSN判断网络侧对UE双栈的支持情况，如网络侧不支持终端双栈，SGSN根据此处的配置选择给UE分配的单栈地址类型。包括以下3个设置：SGSN是否支持终端双栈功能；本SGSN连接的SGSN是否都支持终端双栈；优选PDN类型。 


在以下2种情况下，SGSN判断为不支持终端双栈，SGSN根据配置的“优选PDN类型”指定为UE分配的单栈地址类型。 



 

UE请求终端双栈地址，但UE在HLR上的签约只允许为UE分配IPv4或IPv6单栈地址。
 

 

UE请求终端双栈地址，UE在HLR上的签约也允许终端双栈地址，但SGSN连接的SGSN不都支持终端双栈。
 

 


说明： 


HLR/HSS中可以签约允许的地址类型有4种：IPv4v6（终端双栈）、IPv4（终端单栈）、IPv6（终端单栈）、IPv4或IPv6（终端单栈，允许IPv4或IPv6）。UE请求双栈地址，但只签约了终端单栈，则只能使用终端单栈。 




[](None)相关主题 



 

设置SGSN终端双栈数据(SET GNGP DUAL STACK)
 

 

查询SGSN终端双栈数据(SHOW GNGP DUAL STACK)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置终端双栈数据(SET GNGP DUAL STACK) 
## 设置终端双栈数据(SET GNGP DUAL STACK) 


[](None)命令功能 


该命令用于配置以下内容： 



 
本SGSN网元是否支持终端双栈功能。
 

 
当UE切换时，与本SGSN网元连接的所有目的SGSN网元是否支持终端双栈功能。
 

 
与本SGSN网元连接的GGSN网元支持终端双栈功能默认策略。
 

 
在SGSN网元判断UE不支持双栈功能时，为UE指示单栈的PDP类型，包括IPv4和IPv6两种类型。
 

 




[](None)注意事项 

该命令只适用于SGSN网元。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SGSNSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本SGSN网元是否支持终端双栈功能。
SGSNPDNTYPE|优选PDP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于在SGSN网元判断UE不支持双栈功能时，为UE指示PDP类型，包括IPv4和IPv6两种类型。在以下2种情况下，当SGSN判断UE不支持终端双栈功能时，会根据配置的“优选PDN类型”指定为UE分配的单栈地址类型。UE请求双栈地址，但UE在HLR上的签约数据只允许为UE分配IPv4或IPv6单栈地址。UE请求双栈地址，UE在HLR上的签约数据也允许为UE分配双栈地址，但UE切换时，本SGSN网元连接的目的SGSN不支持终端双栈功能。
SGSNDUALSTACK|UE切换的所有SGSN支持终端双栈|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示UE切换时，与本SGSN网元连接的所有目的SGSN网元是否支持终端双栈功能。
ALLAPNDUALSTACK|APN支持终端双栈默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示APN支持终端双栈功能的默认策略






[](None)命令举例 


设置双栈数据，设置支持终端双栈功能，设置优选PDN类型为IPv4，UE切换的所有SGSN支持终端双栈。 


SET GNGP DUAL STACK:SGSNSTACKFLAG="YES",SGSNPDNTYPE="IPv4",SGSNDUALSTACK="YES",ALLAPNDUALSTACK="YES"; 








父主题： [SGSN终端双栈数据配置](../../zh-CN/tree/N_1254209.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询终端双栈数据(SHOW GNGP DUAL STACK) 
## 查询终端双栈数据(SHOW GNGP DUAL STACK) 


[](None)命令功能 


该命令用于查询以下内容： 


本SGSN网元是否支持终端双栈功能。 


当UE切换时，与本SGSN网元连接的所有目的SGSN网元是否支持终端双栈功能。 


在SGSN网元判断UE不支持双栈功能时，为UE指示单栈的PDP类型，包括IPv4和IPv6两种类型。 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SGSNSTACKFLAG|支持终端双栈功能|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示本SGSN网元是否支持终端双栈功能。
SGSNPDNTYPE|优选PDP类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于在SGSN网元判断UE不支持双栈功能时，为UE指示PDP类型，包括IPv4和IPv6两种类型。在以下2种情况下，当SGSN判断UE不支持终端双栈功能时，会根据配置的“优选PDN类型”指定为UE分配的单栈地址类型。UE请求双栈地址，但UE在HLR上的签约数据只允许为UE分配IPv4或IPv6单栈地址。UE请求双栈地址，UE在HLR上的签约数据也允许为UE分配双栈地址，但UE切换时，本SGSN网元连接的目的SGSN不支持终端双栈功能。
SGSNDUALSTACK|UE切换的所有SGSN支持终端双栈|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示UE切换时，与本SGSN网元连接的所有目的SGSN网元是否支持终端双栈功能。
ALLAPNDUALSTACK|APN支持终端双栈默认策略|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示APN支持终端双栈功能的默认策略






[](None)命令举例 


查询终端双栈数据。 


SHOW GNGP DUAL STACK; 


`

命令 (No.3): SHOW GNGP DUAL STACK

操作维护  支持终端双栈功能   优选PDP类型   UE切换的所有SGSN支持终端双栈   APN支持终端双栈默认策略
-----------------------------------------------------------------------------------------------
修改      支持               优选IPv4      是                             是
-----------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.066 秒）。

` 








父主题： [SGSN终端双栈数据配置](../../zh-CN/tree/N_1254209.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# VRF配置 
# VRF配置 


[](None)背景知识 


通过VRF（VPN Routing and Forward instance）可以将路由设备划分成多个彼此独立的虚拟路由器。该虚拟路由器含有： 



 

一张独立的路由表，包括了独立的地址空间。
 

 

一组归属于本VRF的接口集合。
 

 

一组只用于本VRF的路由协议。
 

 




[](None)功能描述 


如果需要对SGSN/MME 接入的各个业务网络进行隔离，比如无线eNodeB网络和EPC核心网的信令/数据在不同的路由域进行传输，则可以对相应的业务接口、路由设置不同的VRF。 



 

当不需要隔离不同接口（比如S3口、S11口）的业务网络，让接口信令/数据在相同的虚拟路由域内传输时，配置相同的VRF。
 

 

当需要隔离不同接口（比如S3口、S11口）的业务网络，让接口信令/数据在不同的虚拟路由域内传输时，配置不同的VRF。
 

 



                本配置中各业务接口的VRFID配置命令参见
                [VRF](../mml/1404115.html)
                ，并且以下配置需关联该VRF。
            



 


                        该业务接口所在的物理接口、子接口、聚合口或者隧道接口需要关联该VRF，配置命令参见
                        ADD IP FORWARDING VRF
                        。
                    
 

 


                        该业务接口的静态路由或者动态路由需要关联该VRF。静态路由配置命令参见
                        ADD IP ROUTE
                        ；动态路由配置命令参见
                        ROUTE OSPF
                        。
                    
 

 




[](None)相关主题 



 

设置VRF配置(SET VRFCFG)
 

 

查询VRF配置(SHOW VRFCFG)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置VRF配置(SET VRFCFG) 
## 设置VRF配置(SET VRFCFG) 


[](None)命令功能 


该命令用于设置各业务接口关联的VRF， 当需要隔离不同接口（比如S3口、S11口）的业务网络让某接口的信令/数据在不同的虚拟路由域内传输时，使用该命令。当某业务接口VRF设置成功后，该业务接口的信令/数据就被限定在该VRF关联的路由域内传输，起到隔离路由域的作用。 




[](None)注意事项 



 
该配置需结合实际组网情况进行配置，如果不配置，系统默认配置都是0，即所有业务接口都默认处于同一路由域。
 

 
配置前，需要先新增一个VRF及配置该业务接口所在物理接口、子接口或虚接口与VRF关联。配置流程如下。

新增VRF配置，命令参见VRF。

如果该业务接口已关联其它VRF(不含默认的0)，需要先删除关联的路由及接口地址然后再跟原来的VRF解关联，才能关联新的VRF，并配置接口地址和添加相关的路由。


 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
S3VRF|S3口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|S3口的VRF标识，表示S3口的信令/数据被限定在该VRF关联的路由域内传输。
S10VRF|S10口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|S10口的VRF标识，表示S10口的信令/数据被限定在该VRF关联的路由域内传输。
S11VRF|S11口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|S11口的VRF标识，表示S11口的信令/数据被限定在该VRF关联的路由域内传输。
GNVRF|Gn-C口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|Gn口控制面VRF ID，取值0时表示不配置VRF，其他值表示配置为相应的VRF。
IUVRF|Iu口用户面VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|Iu口的VRF标识，表示Iu口的信令/数据被限定在该VRF关联的路由域内传输。
SVVRF|Sv口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|Sv口的VRF标识，表示Sv口的信令/数据被限定在该VRF关联的路由域内传输。
SMVRF|Sm口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|Sm口的VRF标识，表示Sm口的信令/数据被限定在该VRF关联的路由域内传输。
S11RNVRF|S11(RN)口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|S11（RN）口的VRF标识，表示S11（RN）口的信令/数据被限定在该VRF关联的路由域内传输。
S101VRF|S101口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|S101口的VRF标识，表示S101口的信令/数据被限定在该VRF关联的路由域内传输。
S102VRF|S102口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|S102口的VRF标识，表示S102口的信令/数据被限定在该VRF关联的路由域内传输。
IWSS102VRF|IWS S102口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|IWS S102口VRF标识，表示IWS S102口的信令/数据被限定在该VRF关联的路由域内传输。
S11UVRF|S11-U口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|S11-U口的VRF标识，表示S11-U口的数据被限定在该VRF关联的路由域内传输。
GNUVRF|Gn-U口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|Gn口用户面VRF ID，取值0时表示不配置VRF，其他值表示配置为相应的VRF。
N26VRF|N26口VRF标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~254。|N26口用户面VRF ID，取值0时表示不配置VRF，其他值表示配置为相应的VRF。






[](None)命令举例 


设置S11接口的VRF标识为11。 


SET VRFCFG:S11VRF=11 








父主题： [VRF配置](../../zh-CN/tree/N_12522224.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询VRF配置(SHOW VRFCFG) 
## 查询VRF配置(SHOW VRFCFG) 


[](None)命令功能 


该命令用于查询各业务接口关联的VRF。 




[](None)注意事项 


无。 




[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
S3VRF|S3口VRF标识|参数可选性:任选参数；参数类型:整数。|S3口的VRF标识，表示S3口的信令/数据被限定在该VRF关联的路由域内传输。
S10VRF|S10口VRF标识|参数可选性:任选参数；参数类型:整数。|S10口的VRF标识，表示S10口的信令/数据被限定在该VRF关联的路由域内传输。
S11VRF|S11口VRF标识|参数可选性:任选参数；参数类型:整数。|S11口的VRF标识，表示S11口的信令/数据被限定在该VRF关联的路由域内传输。
GNVRF|Gn-C口VRF标识|参数可选性:任选参数；参数类型:整数。|Gn口控制面VRF ID，取值0时表示不配置VRF，其他值表示配置为相应的VRF。
IUVRF|Iu口用户面VRF标识|参数可选性:任选参数；参数类型:整数。|Iu口的VRF标识，表示Iu口的信令/数据被限定在该VRF关联的路由域内传输。
SVVRF|Sv口VRF标识|参数可选性:任选参数；参数类型:整数。|Sv口的VRF标识，表示Sv口的信令/数据被限定在该VRF关联的路由域内传输。
SMVRF|Sm口VRF标识|参数可选性:任选参数；参数类型:整数。|Sm口的VRF标识，表示Sm口的信令/数据被限定在该VRF关联的路由域内传输。
S11RNVRF|S11(RN)口VRF标识|参数可选性:任选参数；参数类型:整数。|S11（RN）口的VRF标识，表示S11（RN）口的信令/数据被限定在该VRF关联的路由域内传输。
S101VRF|S101口VRF标识|参数可选性:任选参数；参数类型:整数。|S101口的VRF标识，表示S101口的信令/数据被限定在该VRF关联的路由域内传输。
S102VRF|S102口VRF标识|参数可选性:任选参数；参数类型:整数。|S102口的VRF标识，表示S102口的信令/数据被限定在该VRF关联的路由域内传输。
IWSS102VRF|IWS S102口VRF标识|参数可选性:任选参数；参数类型:整数。|IWS S102口VRF标识，表示IWS S102口的信令/数据被限定在该VRF关联的路由域内传输。
S11UVRF|S11-U口VRF标识|参数可选性:任选参数；参数类型:整数。|S11-U口的VRF标识，表示S11-U口的数据被限定在该VRF关联的路由域内传输。
GNUVRF|Gn-U口VRF标识|参数可选性:任选参数；参数类型:整数。|Gn口用户面VRF ID，取值0时表示不配置VRF，其他值表示配置为相应的VRF。
N26VRF|N26口VRF标识|参数可选性:任选参数；参数类型:整数。|N26口用户面VRF ID，取值0时表示不配置VRF，其他值表示配置为相应的VRF。






[](None)命令举例 


查询VRF配置。 


SHOW VRFCFG 


`

命令 (No.1): SHOW VRFCFG

操作维护  S3口VRF标识   S10口VRF标识   S11口VRF标识   Gn-C口VRF标识   Iu口用户面VRF标识   Sv口VRF标识   Sm口VRF标识   S11(RN)口VRF标识   S101口VRF标识   S102口VRF标识   IWS S102口VRF标识   S11-U口VRF标识   Gn-U口VRF标识    N26口VRF标识
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      0             0              11             0               0                   0             0             0                  0               0               0                   0                0            0
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.091 秒）。
` 








父主题： [VRF配置](../../zh-CN/tree/N_12522224.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# SGs口开关配置 
# SGs口开关配置 


[](None)背景知识 


SGs口为MME与MSC/VLR之间的接口，承载在SCTP协议上。 


SGs口用于实现以下功能： 



 

UE发起联合类的附着或者跟踪区更新，MME通过SGs口向MSC/VLR发起位置更新流程。
 

 

CSFB（CS Fallback，CS语音回落）业务中，UE通过SGs口从LTE网络回落到2/3G网络进行语音或者短信的起呼或终呼。
 

 




[](None)功能描述 


SGs口开关配置用于控制MME是否支持SGs接口，设置为支持后，MME可以和MSC/VLR进行消息交互。 




[](None)相关主题 



 

设置SGs口开关(SET SGSFLAG)
 

 

查询SGs口开关(SHOW SGSFLAG)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置SGS口开关(SET SGSFLAG) 
## 设置SGS口开关(SET SGSFLAG) 


[](None)命令功能 


该命令用于设置是否开启SGs接口功能。当在SGs口需要支持语音回落（voice fallback），短消息等业务时，需要使用该命令开启SGs接口功能开关。执行成功后，MME可以在SGs口正常收发业务消息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SGSFLAG|支持SGS口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示是否支持SGs接口功能开关。该参数的类型为枚举型变量，取值为：是：表明支持SGs口功能。否：表明不支持SGs口功能。






[](None)命令举例 


开启SGs接口功能。
SET SGSFLAG:SGSFLAG="YES"; 








父主题： [SGs口开关配置](../../zh-CN/tree/N_12512234.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询SGS口开关(SHOW SGSFLAG) 
## 查询SGS口开关(SHOW SGSFLAG) 


[](None)命令功能 


该命令用于查询SGS接口功能。 



 
查询到SGs接口功能开启时表明当前MME在SGs口能正常收发业务消息。
 

 
查询到SGs接口功能关闭时表明当前MME在SGs口不能正常收发业务消息。
 

 




[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SGSFLAG|支持SGS口|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数表示是否支持SGs接口功能开关。该参数的类型为枚举型变量，取值为：是：表明支持SGs口功能。否：表明不支持SGs口功能。






[](None)命令举例 


查询SGS接口功能。
SHOW SGSFLAG; 


`

命令 (No.1): SHOW SGSFLAG

操作维护  支持SGS口
-------------------
修改      是
-------------------
记录数 1

命令执行成功（耗时 0.031 秒）。
` 








父主题： [SGs口开关配置](../../zh-CN/tree/N_12512234.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 拒绝原因更正配置 
# 拒绝原因更正配置 


[](None)背景知识 


2G/3G网络中，UE向网络发起附着（Attach）、RAU或业务请求（Service Request）时，如果SGSN拒绝UE接入，会在拒绝消息（Attach Reject、RAU Reject、Service Reject）中携带拒绝原因，按照3GPP的24.008协议，UE对于SGSN下发的不同拒绝原因进行不同的处理。 




[](None)功能描述 


对SGSN下发给UE的Attach Reject、RAU Reject或Service Reject消息，如果运营商希望修改消息中默认的拒绝原因，可以通过“拒绝原因更正配置”，对Iu接口或者Gb接口分别设置拒绝原因值。配置后，SGSN根据设置下发拒绝原因。 


拒绝原因修正后，SGSN在上报性能统计使用修改后的原因值 




[](None)相关主题 



 

新增拒绝原因更正配置(ADD CAUSE CORRECT)
 

 

修改拒绝原因更正配置(SET CAUSE CORRECT)
 

 

删除拒绝原因更正配置(DEL CAUSE CORRECT)
 

 

查询拒绝原因更正配置(SHOW CAUSE CORRECT)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增拒绝原因更正配置(ADD CAUSE CORRECT) 
## 新增拒绝原因更正配置(ADD CAUSE CORRECT) 


[](None)命令功能 


该命令用于新增拒绝原因更正配置。拒绝原因更正配置用于调整附着或者路由区更新被拒绝时下发给用户的原因值，以便与缺省情况不一样。不同的运营商对不同场景产生的失败期望的拒绝原因值不一样，需要提供给运营商进行灵活配置。当运营商需要调整限制用户接入的拒绝原因值时，使用该命令。配置成功后，SGSN下发附着拒绝的原因值会被调整。 




[](None)注意事项 


此命令属于危险命令，不合适的原因值可能会导致终端必现开关机才可以重新接入。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAT|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示拒绝原因更正配置生效的接入类型。 取值含义：Iu：只对Iu接入用户生效。Gb：只对Gb接入用户生效。
CAUSE|更正前原因|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示更正前的原因值，具体原因值含义参考3GPP TS24.008 协议中的GMM Cause 相应的描述。
CAUSECORRECT|更正后原因|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示更正后的原因值，具体原因值含义参考3GPP TS24.008 协议中的GMM Cause相应的描述。






[](None)命令举例 


新增拒绝原因更正配置，设置接入类型为Iu，更正前原因为Illegal MS，更正后原因为MS identity cannot be derived by the network。
ADD CAUSE CORRECT:RAT="Iu",CAUSE="Illegal MS",CAUSECORRECT="MS identity cannot be derived by the network"; 








父主题： [拒绝原因更正配置](../../zh-CN/tree/N_1254224.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改拒绝原因更正配置(SET CAUSE CORRECT) 
## 修改拒绝原因更正配置(SET CAUSE CORRECT) 


[](None)命令功能 


该命令用于修改拒绝原因更正配置。拒绝原因更正配置用于调整附着或者路由区更新被拒绝时下发给用户的原因值，以便与缺省情况不一样。不同的运营商对不同场景产生的失败期望的拒绝原因值不一样，需要提供给运营商进行灵活配置。当当前原因值不满足运营商期望时，使用该命令。配置成功后，SGSN下发附着拒绝的原因值会被调整。 




[](None)注意事项 


此命令属于危险命令，不合适的原因值可能会导致终端必现开关机才可以重新接入。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAT|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示拒绝原因更正配置生效的接入类型。 取值含义：Iu：只对Iu接入用户生效。Gb：只对Gb接入用户生效。
CAUSE|更正前原因|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示更正前的原因值，具体原因值含义参考3GPP TS24.008 协议中的GMM Cause 相应的描述。
CAUSECORRECT|更正后原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示更正后的原因值，具体原因值含义参考3GPP TS24.008 协议中的GMM Cause相应的描述。






[](None)命令举例 


修改接入类型为Iu，更正前原因为Illegal MS的拒绝原因更正配置，将更正后原因修改为MS identity cannot be derived by the network。
SET CAUSE CORRECT:RAT="Iu",CAUSE="Illegal MS",CAUSECORRECT="MS identity cannot be derived by the network"; 








父主题： [拒绝原因更正配置](../../zh-CN/tree/N_1254224.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除拒绝原因更正配置(DEL CAUSE CORRECT) 
## 删除拒绝原因更正配置(DEL CAUSE CORRECT) 


[](None)命令功能 


该命令用于删除拒绝原因更正配置。删除命令区分用户的无线接入类型，并需要提供缺省原因值。当运营商需要删除针对特定的绝原因值，使用系统缺省的原因值时进行调整时，使用该命令。配置成功后，SGSN下发附着拒绝的原因值会被调整，使用缺省的原因值进行下发。 




[](None)注意事项 


此命令属于危险命令，不合适的原因值可能会导致终端必现开关机才可以重新接入。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAT|接入类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示拒绝原因更正配置生效的接入类型。 取值含义：Iu：只对Iu接入用户生效。Gb：只对Gb接入用户生效。
CAUSE|更正前原因|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于指示更正前的原因值，具体原因值含义参考3GPP TS24.008 协议中的GMM Cause 相应的描述。






[](None)命令举例 


删除接入类型为Iu，更正前原因为Illegal MS的拒绝原因更正配置。
DEL CAUSE CORRECT:RAT="Iu",CAUSE="Illegal MS"; 








父主题： [拒绝原因更正配置](../../zh-CN/tree/N_1254224.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询拒绝原因更正配置(SHOW CAUSE CORRECT) 
## 查询拒绝原因更正配置(SHOW CAUSE CORRECT) 


[](None)命令功能 


该命令用于查询所有的拒绝原因更正配置，没有参数，查询结果当前的所有的拒绝原因更正配置信息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAT|接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示拒绝原因更正配置生效的接入类型。 取值含义：Iu：只对Iu接入用户生效。Gb：只对Gb接入用户生效。
CAUSE|更正前原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示更正前的原因值，具体原因值含义参考3GPP TS24.008 协议中的GMM Cause 相应的描述。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
RAT|接入类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示拒绝原因更正配置生效的接入类型。 取值含义：Iu：只对Iu接入用户生效。Gb：只对Gb接入用户生效。
CAUSE|更正前原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示更正前的原因值，具体原因值含义参考3GPP TS24.008 协议中的GMM Cause 相应的描述。
CAUSECORRECT|更正后原因|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指示更正后的原因值，具体原因值含义参考3GPP TS24.008 协议中的GMM Cause相应的描述。






[](None)命令举例 


查询所有的拒绝原因更正配置。
SHOW CAUSE CORRECT; 


`

命令 (No.1): SHOW CAUSE CORRECT

操作维护         接入类型   更正前原因                                        更正后原因
----------------------------------------------------------------------------------------
复制 修改 删除   Iu         Illegal MS                                        MS identity cannot be derived by the network
----------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.062 秒）。
` 








父主题： [拒绝原因更正配置](../../zh-CN/tree/N_1254224.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# 下行数据通知延迟配置 
# 下行数据通知延迟配置 


[](None)背景知识 


当SGW接收到发给处于ECM-IDLE状态的UE下行数据时，SGW发送下行数据通知消息（DDN，Downlink Data Notification）给MME，由MME对用户进行寻呼。如果SGW发给MME的DDN消息过于频繁，会引起MME负荷过高。 




[](None)功能描述 


MME为了避免因为接收大量的SGW下发的DDN消息，导致负荷过高，可以通过“下行数据通知延迟配置”设置DDN消息的速率阈值及延迟时间，当SGW下发的DDN消息速率超过此阈值时，MME在发送给SGW的Downlink Data Notification ACK消息中携带延迟时间，通知SGW延迟下发DDN消息。 




[](None)相关主题 



 

设置下行数据通知延迟配置(SET DDN DELAY)
 

 

查询下行数据通知延迟配置(SHOW DDN DELAY)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置下行数据通知延迟配置(SET DDN DELAY) 
## 设置下行数据通知延迟配置(SET DDN DELAY) 


[](None)命令功能 


该命令用于设置下行数据通知延迟配置。当需要延时发送下行数据通知时使用该命令，下行数据通知延时配置后，MME计算出下行数据通知延迟值，通知SGW延时发送下行数据通知消息。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
DDNRATETHD|DDN消息速率阈值(次/分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|MME判断发送DDN消息的一个条件，速率值大于阈值时才会去判断是否发送DDN延迟值到SGW。
DDNDELAYCALMTHD|DDN延迟值计算方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数配置DDN延迟值计算方式。取值含义：“DDN消息接收速率(RATE)”：速率方式，DDN延迟值=“DDN消息速率达到阈值时延迟时长”+（“下行数据通知消息接收速率”-“DDN消息速率阈值”）*“DDN速率增加时延迟时长增大比率”“DDN消息平均处理时长”：时长方式，DDN延迟值=下行数据通知消息平均处理时长（MME自行计算)+“DDN延迟保护时长”下行数据通知消息接收速率=MME收到DDN消息个数/接收时长（分钟）
DDNDELAYTIME|DDN消息速率达到阈值时延迟时长(50ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于计算DDN延迟值，延迟值计算方式为“DDN消息接收速率(RATE)”。MME计算出“下行数据通知消息接收速率”大于“DDN消息速率阈值”，DDN延迟值=“DDN消息速率达到阈值时延迟时长”+（“下行数据通知消息接收速率”-“DDN消息速率阈值”）*“DDN速率增加时延迟时长增大比率”。
DDNDELAYRATE|DDN速率增加时延迟时长增大比率(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1000。|该参数用于计算DDN延迟值，延迟值计算方式为“DDN消息接收速率(RATE)”。MME计算出“下行数据通知消息接收速率”大于“DDN消息速率阈值”，DDN延迟值=“DDN消息速率达到阈值时延迟时长”+（“下行数据通知消息接收速率”-“DDN消息速率阈值”）*“DDN速率增加时延迟时长增大比率”。
DDNDELAYPROTECT|DDN消息延迟保护时长(50ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于计算DDN延迟值，延迟值计算方式为“DDN消息平均处理时长”。MME计算出““下行数据通知消息接收速率”大于“DDN消息速率阈值”，DDN延迟值=下行数据通知消息平均处理时长（MME自行计算)+“DDN消息延迟保护时长”。
DDNDELAYCORRECT|DDN延迟值修正时长(50ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于计算MME发送到SGW的D值。为了避免在极短的时间内给不同的SGW相同的D值，在延迟值计算方式为“DDN消息平均处理时长”时，MME会对延迟值做出相应的处理。计算的延迟值为N，配置的“DDN延迟值修正时长”值为M，则在N-M和N+M之间随机取一个值作为最终发送给SGW的 D值（如果N-M小于或等于0，则取1，如果N+M大于255，则取255）。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该条记录的配置名称，可以说明配置含义，便于理解。






[](None)命令举例 


设置DDN消息速率阈值为60次/分钟、DDN延迟值计算方式为RATE。
SET DDN DELAY:DDNRATETHD=60,DDNDELAYCALMTHD="RATE"; 








父主题： [下行数据通知延迟配置](../../zh-CN/tree/N_12602804.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询下行数据通知延迟配置(SHOW DDN DELAY) 
## 查询下行数据通知延迟配置(SHOW DDN DELAY) 


[](None)命令功能 

该命令用于查询下行数据通知延迟配置。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
DDNRATETHD|DDN消息速率阈值(次/分钟)|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|MME判断发送DDN消息的一个条件，速率值大于阈值时才会去判断是否发送DDN延迟值到SGW。
DDNDELAYCALMTHD|DDN延迟值计算方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数配置DDN延迟值计算方式。取值含义：“DDN消息接收速率(RATE)”：速率方式，DDN延迟值=“DDN消息速率达到阈值时延迟时长”+（“下行数据通知消息接收速率”-“DDN消息速率阈值”）*“DDN速率增加时延迟时长增大比率”“DDN消息平均处理时长”：时长方式，DDN延迟值=下行数据通知消息平均处理时长（MME自行计算)+“DDN延迟保护时长”下行数据通知消息接收速率=MME收到DDN消息个数/接收时长（分钟）
DDNDELAYTIME|DDN消息速率达到阈值时延迟时长(50ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于计算DDN延迟值，延迟值计算方式为“DDN消息接收速率(RATE)”。MME计算出“下行数据通知消息接收速率”大于“DDN消息速率阈值”，DDN延迟值=“DDN消息速率达到阈值时延迟时长”+（“下行数据通知消息接收速率”-“DDN消息速率阈值”）*“DDN速率增加时延迟时长增大比率”。
DDNDELAYRATE|DDN速率增加时延迟时长增大比率(%)|参数可选性:任选参数；参数类型:整数；参数范围为:0~1000。|该参数用于计算DDN延迟值，延迟值计算方式为“DDN消息接收速率(RATE)”。MME计算出“下行数据通知消息接收速率”大于“DDN消息速率阈值”，DDN延迟值=“DDN消息速率达到阈值时延迟时长”+（“下行数据通知消息接收速率”-“DDN消息速率阈值”）*“DDN速率增加时延迟时长增大比率”。
DDNDELAYPROTECT|DDN消息延迟保护时长(50ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于计算DDN延迟值，延迟值计算方式为“DDN消息平均处理时长”。MME计算出““下行数据通知消息接收速率”大于“DDN消息速率阈值”，DDN延迟值=下行数据通知消息平均处理时长（MME自行计算)+“DDN消息延迟保护时长”。
DDNDELAYCORRECT|DDN延迟值修正时长(50ms)|参数可选性:任选参数；参数类型:整数；参数范围为:0~255。|该参数用于计算MME发送到SGW的D值。为了避免在极短的时间内给不同的SGW相同的D值，在延迟值计算方式为“DDN消息平均处理时长”时，MME会对延迟值做出相应的处理。计算的延迟值为N，配置的“DDN延迟值修正时长”值为M，则在N-M和N+M之间随机取一个值作为最终发送给SGW的 D值（如果N-M小于或等于0，则取1，如果N+M大于255，则取255）。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|该条记录的配置名称，可以说明配置含义，便于理解。






[](None)命令举例 


查询下行数据通知延迟配置。
SHOW DDN DELAY; 


`

命令 (No.1): SHOW DDN DELAY

操作维护  DDN消息速率阈值(次/分钟)   DDN延迟值计算方式   DDN消息速率达到阈值时延迟时长(50ms)   DDN速率增加时延迟时长增大比率(%)   DDN消息延迟保护时长(50ms)   DDN延迟值修正时长(50ms)   用户别名
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改      60                         DDN消息接收速率     20                                    10                                 10                          40                        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.044 秒）。
` 








父主题： [下行数据通知延迟配置](../../zh-CN/tree/N_12602804.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# Gn GTPU IP能力配置 
# Gn GTPU IP能力配置 


[](None)背景知识 


SGSN与GGSN之间Gn接口使用GTP协议，分为控制面（GTP-C）与用户面（GTP-U）。GTP协议承载在IP上，SGSN和GGSN可以支持IPV4、IPV6或双栈地址，支持双栈即同时支持IPV4和IPV6地址。 




[](None)功能描述 


"Gn GTPU IP能力配置"用于在SGSN上设置对端GGSN的用户面IP地址类型，如果支持双栈功能，必须配置此项。配置前，需要确定对端GGSN支持IPV4和IPV6的能力。 


配置后，如果GGSN支持双栈，SGSN在PDP激活流程中，收到GGSN的Create PDP Context Response消息中携带的GGSN的GTP-C（IPV4和IPV6两个地址）和GTP-U（IPV4和IPV6两个地址），SGSN通过本配置匹配GGSN的GTP-C地址，获取对端GGSN的用户面地址能力，从而SGSN采用和对端相同的能力进行IP地址类型选择。 




[](None)相关主题 



 

新增Gn GTPU IP能力配置(ADD GN GTPU IP CAPA)
 

 

修改Gn GTPU IP能力配置(SET GN GTPU IP CAPA)
 

 

删除Gn GTPU IP能力配置(DEL GN GTPU IP CAPA)
 

 

查询Gn GTPU IP能力配置(SHOW GN GTPU IP CAPA)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 新增Gn GTPU IP能力配置(ADD GN GTPU IP CAPA) 
## 新增Gn GTPU IP能力配置(ADD GN GTPU IP CAPA) 


[](None)命令功能 


该命令用于新增Gn GTPU IP支持IPv4或IPv6的能力配置。从而根据对端GGSN用户面对IPv4、IPv6协议栈的支持情况，本局SGSN根据该配置对用户面地址IP协议栈类型做出相应的决策。当需要配置Gn口支持IPv6或支持IPv4/IPv6双栈时，使用该命令。配置支持的能力成功后，SGSN就可以支持Gn口这种能力的控制面和用户面业务。 


在支持双栈情况下，Gn口本端用户面地址和Gn口对端地址使用相同的IP地址类型。 




[](None)注意事项 



 
该命令需要加载支持该特性的License，对应的License项为“IPv6功能”。
 

 
该命令配置前需要知道Gn口对端GGSN的支持IPv4/IPv6的能力，本端SGSN的能力取决于对端。
 

 
如果本端和对端支持IPv4和IPv6，则本端优先选择IPv6。
 

 
如果本端仅支持IPv4而不支持IPv6，而本配置配为对端支持“仅IPv6”，用户面则按丢包处理。如果需要配置本端支持IPv6，相关的设置包括GTPC信令地址配置SET SIGIP GTPC、用户面负荷分担、接口配置、及相关路由等协议栈配置。

 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN GTPC IP地址|参数可选性:必选参数；参数类型:字符型；参数范围为:1~39个字符。|该参数用于配置对端GGSN的GTPC IP地址。
GNGTPUIPCAP|Gn GTPU IP能力|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:GTPC。|该参数用于指定对端Gn口GTPU IP具体能力。取值含义如下：同GTPC IP(GTPC)：IP能力同GGSN GTPC IP地址类型对应的能力，如果配为IPv4地址则为IPv4，如果配为IPv6地址则为IPv6。仅IPv4(IPV4)：IP能力为IPv4。仅IPv6(IPV6)：IP能力为IPv6。IPv4和IPv6(IPV4V6)：IP能力为IPv4和IPv6。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义的新增规则的名称。






[](None)命令举例 


新增Gn GTPU IP能力配置，设置GGSN GTPC IP地址为20.1.7.100，Gn GTPU IP能力为同GTPC IP。
ADD GN GTPU IP CAPA:GGSNIP="20.1.7.100",GNGTPUIPCAP="GTPC"; 








父主题： [Gn GTPU IP能力配置](../../zh-CN/tree/N_12605205.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 修改Gn GTPU IP能力配置(SET GN GTPU IP CAPA) 
## 修改Gn GTPU IP能力配置(SET GN GTPU IP CAPA) 


[](None)命令功能 

该命令用于修改Gn GTPU IP能力配置。Gn GTPU IP能力指的是对端GGSN用户面对IPv4、IPv6支持情况，本端根据该配置对用户面地址IP类型做出相应的决策。


[](None)注意事项 



 
该命令配置前需要知道Gn口对端GGSN的支持IPv4/IPv6的能力，本端SGSN的能力取决于对端。
 

 
如果本端和对端支持IPv4和IPv6，则本端优先选择IPv6。
 

 
如果本端仅支持IPv4而不支持IPv6，而本配置配为对端支持“仅IPv6”，用户面则按丢包处理。如果需要配置本端支持IPv6，相关的设置包括GTPC信令地址配置SET SIGIP GTPC、用户面负荷分担、接口配置、及相关路由等协议栈配置。

 

 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN GTPC IP地址|参数可选性:必选参数；参数类型:字符型；参数范围为:1~39个字符。|该参数用于配置对端GGSN的GTPC IP地址。
GNGTPUIPCAP|Gn GTPU IP能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定对端Gn口GTPU IP具体能力。取值含义如下：同GTPC IP(GTPC)：IP能力同GGSN GTPC IP地址类型对应的能力，如果配为IPv4地址则为IPv4，如果配为IPv6地址则为IPv6。仅IPv4(IPV4)：IP能力为IPv4。仅IPv6(IPV6)：IP能力为IPv6。IPv4和IPv6(IPV4V6)：IP能力为IPv4和IPv6。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|用户自定义的新增规则的名称。






[](None)命令举例 


修改GGSN GTPC IP地址为20.1.7.100的Gn GTPU IP能力配置，将Gn GTPU IP能力修改为IPV4。
SET GN GTPU IP CAPA:GGSNIP="20.1.7.100",GNGTPUIPCAP="IPV4"; 








父主题： [Gn GTPU IP能力配置](../../zh-CN/tree/N_12605205.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 删除Gn GTPU IP能力配置(DEL GN GTPU IP CAPA) 
## 删除Gn GTPU IP能力配置(DEL GN GTPU IP CAPA) 


[](None)命令功能 

该命令用于删除Gn GTPU IP能力配置。Gn GTPU IP能力指的是对端GGSN用户面对IPv4、IPv6支持情况，本端根据该配置对用户面地址IP类型做出相应的决策。


[](None)注意事项 

删除Gn GTPU IP能力配置后，本端则不根据对端用户面地址IP类型做出相应的决策。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN GTPC IP地址|参数可选性:必选参数；参数类型:字符型；参数范围为:1~39个字符。|该参数用于配置对端GGSN的GTPC IP地址。






[](None)命令举例 


删除GGSN GTPC IP地址为20.1.7.100的Gn GTPU IP能力配置。
DEL GN GTPU IP CAPA:GGSNIP="20.1.7.100"; 








父主题： [Gn GTPU IP能力配置](../../zh-CN/tree/N_12605205.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询Gn GTPU IP能力配置(SHOW GN GTPU IP CAPA) 
## 查询Gn GTPU IP能力配置(SHOW GN GTPU IP CAPA) 


[](None)命令功能 

该命令用于查询Gn GTPU IP能力配置。Gn GTPU IP能力指的是对端GGSN用户面对IPv4、IPv6支持情况，本端根据该配置对用户面地址IP类型做出相应的决策。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN GTPC IP地址|参数可选性:任选参数；参数类型:字符型；参数范围为:1~39个字符。|该参数用于配置对端GGSN的GTPC IP地址。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
GGSNIP|GGSN GTPC IP地址|参数可选性:任选参数；参数类型:字符型。|该参数用于配置对端GGSN的GTPC IP地址。
GNGTPUIPCAP|Gn GTPU IP能力|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于指定对端Gn口GTPU IP具体能力。取值含义如下：同GTPC IP(GTPC)：IP能力同GGSN GTPC IP地址类型对应的能力，如果配为IPv4地址则为IPv4，如果配为IPv6地址则为IPv6。仅IPv4(IPV4)：IP能力为IPv4。仅IPv6(IPV6)：IP能力为IPv6。IPv4和IPv6(IPV4V6)：IP能力为IPv4和IPv6。
USERLABEL|用户别名|参数可选性:任选参数；参数类型:字符型。|用户自定义的新增规则的名称。






[](None)命令举例 


查询所有的Gn GTPU IP能力配置，或填入参数地址根据地址查询能力。
SHOW GN GTPU IP CAPA; 


`

命令 (No.1): SHOW GN GTPU IP CAPA

操作维护         GGSN GTPC IP地址   Gn GTPU IP能力   用户别名
-------------------------------------------------------------
复制 修改 删除   20.1.7.100         同GTPC IP        
-------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.04 秒）。
` 








父主题： [Gn GTPU IP能力配置](../../zh-CN/tree/N_12605205.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# MME GTPU地址配置 
# MME GTPU地址配置 


[](None)背景知识 


NB-IoT，即窄带物联网，是为低复杂度、低功耗、低速率物联网终端提供服务的3GPP无线接入技术的蜂窝网络。 


为支持此类应用，网络侧需要做到：当MME支持NB-IoT接入时，为了提高小包数据的传输效率，降低系统信令消耗，MME可采用控制面优化方案，即将小包数据封装在NAS消息中在UE和MME之间传递。而MME和SGW之间，是通过建立S11-U隧道来实现小包数据传递。 




[](None)功能描述 


MME GTPU地址配置用于配置MME和SGW之间的S11-U隧道的MME本端的GTP-U的IP地址。 




[](None)相关主题 



 

设置MME GTPU地址(SET MME GTPU IP)
 

 

查询MME GTPU地址(SHOW MME GTPU IP)
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 设置MME GTPU地址(SET MME GTPU IP) 
## 设置MME GTPU地址(SET MME GTPU IP) 


[](None)命令功能 


该命令用于修改MME的GTP-U的IP地址。当MME和SGW之间需要建立S11-U隧道传输小包数据时，使用该命令设定或者修改MME的GTPU地址。 


该地址为MME与SGW基于GTP-U协议交互时的地址，该地址同时需要在协议栈的Loopback环回口上配置。 




[](None)注意事项 

None


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
S11UIPADDR|GTPU IPv4地址|参数可选性:任选参数；参数类型:地址|该参数用于设置MME的GTP-U IPv4地址。
S11UIPV6ADDR|GTPU IPv6地址|参数可选性:任选参数；参数类型:地址|该参数用于设置MME的GTP-U IPv6地址。






[](None)命令举例 


设置MME的GTP-U IPv4地址为"10.44.25.5"。 


SET MME GTPU IP:S11UIPADDR="10.44.25.5"; 








父主题： [MME GTPU地址配置](../../zh-CN/tree/N_12605533.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 查询MME GTPU地址(SHOW MME GTPU IP) 
## 查询MME GTPU地址(SHOW MME GTPU IP) 


[](None)命令功能 

该命令用于查询MME的GTP-U的IP地址。


[](None)注意事项 

None


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
S11UIPADDR|GTPU IPv4地址|参数可选性:任选参数；参数类型:地址|该参数用于设置MME的GTP-U IPv4地址。
S11UIPV6ADDR|GTPU IPv6地址|参数可选性:任选参数；参数类型:地址|该参数用于设置MME的GTP-U IPv6地址。






[](None)命令举例 


查询MME的GTP-U的IP地址。 


SHOW MME GTPU IP; 


`

命令 (No.3): SHOW MME GTPU IP

操作维护  GTPU IPv4地址   GTPU IPv6地址
---------------------------------------
修改      10.44.25.5      
---------------------------------------
记录数 1

命令执行成功（耗时 0.043 秒）。
` 








父主题： [MME GTPU地址配置](../../zh-CN/tree/N_12605533.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


# NITZ配置 
# NITZ配置 


[](None)背景知识 


NITZ（Network Identity and Time Zone），即网络标识和时区，网络侧可以将网络标识（包括网络长标识和网络短标识）和时区信息（如时区、时间、夏令时）传递给UE，UE可以根据网络侧下发的信息进行自动更新。 



 

当用户在2/3G网络下接入时，由SGSN给UE下发网络标识和时区。
 

 

当用户在4G网络下接入时，由MME给UE下发网络标识和时区。
 

 




[](None)功能描述 


本功能节点用于配置网络标识和时区，及下发网络标识和时区的策略。 




[](None)相关主题 



 

MME全局NITZ配置
 

 

MME基于IMSI号段的NITZ发送策略配置
 

 

SGSN全局NITZ配置
 

 

SGSN基于IMSI号段的NITZ发送策略配置
 

 

基于PLMN的NI配置
 

 








父主题： [交换局配置](../../zh-CN/tree/N_1254210.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## MME全局NITZ配置 
## MME全局NITZ配置 


[](None)背景知识 


网络标识和时区NITZ（Network Identity and Time Zone）是一种通过无线网络向UE提供本地日期和时间、时区、夏时制偏移，以及网络提供商身份信息的方法，通常应用于移动电话自动更新系统时间。 


多时区业务是指随着用户的移动，根据位置信息与时区/夏令时的映射关系，MME完成以下功能： 



 

MME会将用户当前位置的时区和夏令时信息传递给UE，UE会刷新自己的系统时间。
 

 

MME会将用户当前位置时区和夏令时信息上报给用户承载连接网关SGW，以实现基于位置时区的差异化计费。
 

 




[](None)功能描述 


本功能用于设置MME全局网络标识和时区，MME根据配置的策略控制向UE发送NI和TZ。 




[](None)相关主题 



 

设置MME全局NITZ配置(SET MME NITZ)
 

 

查询MME全局NITZ配置(SHOW MME NITZ)
 

 








父主题： [NITZ配置](../../zh-CN/tree/N_1260931.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置MME全局NITZ配置(SET MME NITZ) 
### 设置MME全局NITZ配置(SET MME NITZ) 


[](None)命令功能 

该命令用于设置MME全局网络标识和时区。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置MME是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下场景:  IMSI附着:  用户发起IMSI附着时，MME下发网络标识给UE。局内GUTI附着:  用户发起局内GUTI附着时，MME下发网络标识给UE。RAT内局间GUTI附着:  用户发起RAT内局间GUTI附着时，MME下发网络标识给UE。RAT间局间GUTI附着:  用户发起RAT间局间GUTI附着时，MME下发网络标识给UE。周期TAU:  用户发起周期TAU时，MME下发网络标识给UE。局内TAU:  用户发起局内TAU时，MME下发网络标识给UE。RAT内局间TAU:  用户发起RAT内局间TAU时，MME下发网络标识给UE。RAT间局间TAU:  用户发起RAT间局间TAU时，MME下发网络标识给UE。局内切换后TAU:  用户发起局内切换后TAU时，MME下发网络标识给UE。RAT内局间切换后TAU:  用户发起RAT内局间切换后TAU时，MME下发网络标识给UE。RAT间局间切换后TAU:  用户发起RAT间局间切换后TAU时，MME下发网络标识给UE。业务请求:  用户发起业务请求时，MME下发网络标识给UE。网络标识改变:  当用户所在网络的网络标识发生改变，MME下发网络标识给UE。DST夏令时切入或切出:  网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE。时区改变:  用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络标识给UE。CP业务请求:  用户发起CP业务请求时，MME下发网络标识给UE。5G到4G局间GUTI附着:  基于N26接口，用户发起5G到4G局间GUTI附着时，MME下发网络标识给UE。5G到4G局间TAU:  基于N26接口，用户发起5G到4G局间TAU时，MME下发网络标识给UE。5G到4G局间切换后TAU:  基于N26接口，用户发起5G到4G局间切换后TAU时，MME下发网络标识给UE。如上MME/SGSN下发网络标识给UE的多种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置MME是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下场景: IMSI附着: 用户发起IMSI附着时，MME下发时区信息给UE。局内GUTI附着: 用户发起局内GUTI附着时，MME下发时区信息给UE。RAT内局间GUTI附着: 用户发起RAT内局间GUTI附着时，MME下发时区信息给UE。RAT间局间GUTI附着: 用户发起RAT间局间GUTI附着时，MME下发时区信息给UE。周期TAU: 用户发起周期TAU时，MME下发时区信息给UE。局内TAU: 用户发起局内TAU时，MME下发时区信息给UE。RAT内局间TAU: 用户发起RAT内局间TAU时，MME下发时区信息给UE。RAT间局间TAU: 用户发起RAT间局间TAU时，MME下发时区信息给UE。局内切换后TAU: 用户发起局内切换后TAU时，MME下发时区信息给UE。RAT内局间切换后TAU: 用户发起RAT内局间切换后TAU时，MME下发时区信息给UE。RAT间局间切换后TAU: 用户发起RAT间局间切换后TAU时，MME下发时区信息给UE。业务请求: 用户发起业务请求时，MME下发时区信息给UE。网络标识改变: 当用户所在网络的网络标识发生改变，MME下发时区信息给UE。DST夏令时切入或切出: 网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。时区改变: 用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE。CP业务请求: 用户发起CP业务请求时，MME下发时区信息给UE。当5G到4G局间GUTI附着: 基于N26接口，用户发起5G到4G局间GUTI附着时，MME下发时区信息给UE。当5G到4G局间TAU: 基于N26接口，用户发起5G到4G局间TAU时，MME下发时区信息给UE。当5G到4G局间切换后TAU: 基于N26接口，用户发起5G到4G局间切换后TAU时，MME下发时区信息给UE。如上MME/SGSN下发时区信息给UE的多种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。
ADDCNY|网络标识前面是否加国家名称缩写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发网络标识给UE，则通知UE需要在网络标识前添加国家名称缩写。该参数设置为“否(NO)”，若MME/SGSN需要下发网络标识给UE，则通知UE无需在网络标识前添加国家名称缩写。
LNAME|本网的网络长标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络全称。
LNAMECODE|长标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
SNAME|本网的网络短标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络简称。
SNAMECODE|短标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|注释该项配置信息，起备注作用。






[](None)命令举例 


设置发送NI场景为IMSI，发送TZ场景为IMSI，在下发TZ时是否通知用户网络时间为NO。 


SET MME NITZ:IFSENDNI="YES",SCENENI="IMSI",IFSENDTZ="YES",SCENETZ="IMSI",SENDTM="NO"; 








父主题： [MME全局NITZ配置](../../zh-CN/tree/N_12609311.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME全局NITZ配置(SHOW MME NITZ) 
### 查询MME全局NITZ配置(SHOW MME NITZ) 


[](None)命令功能 

该命令用于查询MME全局网络标识和时区。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置MME是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下场景：IMSI附着：用户发起IMSI附着时，MME下发网络标识给UE。局内GUTI附着：用户发起局内GUTI附着时，MME下发网络标识给UE。RAT内局间GUTI附着：用户发起RAT内局间GUTI附着时，MME下发网络标识给UE。RAT间局间GUTI附着：用户发起RAT间局间GUTI附着时，MME下发网络标识给UE。周期TAU：用户发起周期TAU时，MME下发网络标识给UE。局内TAU：用户发起局内TAU时，MME下发网络标识给UE。RAT内局间TAU：用户发起RAT内局间TAU时，MME下发网络标识给UE。RAT间局间TAU：用户发起RAT间局间TAU时，MME下发网络标识给UE。局内切换后TAU：用户发起局内切换后TAU时，MME下发网络标识给UE。RAT内局间切换后TAU：用户发起RAT内局间切换后TAU时，MME下发网络标识给UE。RAT间局间切换后TAU：用户发起RAT间局间切换后TAU时，MME下发网络标识给UE。业务请求：用户发起业务请求时，MME下发网络标识给UE。网络标识改变：当用户所在网络的网络标识发生改变，MME下发网络标识给UE。DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE。时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络标识给UE。CP业务请求：用户发起CP业务请求时，MME下发网络标识给UE。5G到4G局间GUTI附着：基于N26接口，用户发起5G到4G局间GUTI附着时，MME下发网络标识给UE。5G到4G局间TAU：基于N26接口，用户发起5G到4G局间TAU时，MME下发网络标识给UE。5G到4G局间切换后TAU：基于N26接口，用户发起5G到4G局间切换后TAU时，MME下发网络标识给UE。如上MME/SGSN下发网络标识给UE的多种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置MME是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下场景：IMSI附着：用户发起IMSI附着时，MME下发时区信息给UE。局内GUTI附着：用户发起局内GUTI附着时，MME下发时区信息给UE。RAT内局间GUTI附着：用户发起RAT内局间GUTI附着时，MME下发时区信息给UE。RAT间局间GUTI附着：用户发起RAT间局间GUTI附着时，MME下发时区信息给UE。周期TAU：用户发起周期TAU时，MME下发时区信息给UE。局内TAU：用户发起局内TAU时，MME下发时区信息给UE。RAT内局间TAU：用户发起RAT内局间TAU时，MME下发时区信息给UE。RAT间局间TAU：用户发起RAT间局间TAU时，MME下发时区信息给UE。局内切换后TAU：用户发起局内切换后TAU时，MME下发时区信息给UE。RAT内局间切换后TAU：用户发起RAT内局间切换后TAU时，MME下发时区信息给UE。RAT间局间切换后TAU：用户发起RAT间局间切换后TAU时，MME下发时区信息给UE。业务请求：用户发起业务请求时，MME下发时区信息给UE。网络标识改变：当用户所在网络的网络标识发生改变，MME下发时区信息给UE。DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE。CP业务请求：用户发起CP业务请求时，MME下发时区信息给UE。当5G到4G局间GUTI附着：基于N26接口，用户发起5G到4G局间GUTI附着时，MME下发时区信息给UE。当5G到4G局间TAU：基于N26接口，用户发起5G到4G局间TAU时，MME下发时区信息给UE。当5G到4G局间切换后TAU：基于N26接口，用户发起5G到4G局间切换后TAU时，MME下发时区信息给UE。如上MME/SGSN下发时区信息给UE的多种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。
ADDCNY|网络标识前面是否加国家名称缩写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发网络标识给UE，则通知UE需要在网络标识前添加国家名称缩写。该参数设置为“否(NO)”，若MME/SGSN需要下发网络标识给UE，则通知UE无需在网络标识前添加国家名称缩写。
LNAME|本网的网络长标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络全称。
LNAMECODE|长标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
SNAME|本网的网络短标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络简称。
SNAMECODE|短标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|注释该项配置信息，起备注作用。






[](None)命令举例 


查询MME下发网络标识和时区的场景、全局网络标识及其编码格式、是否下发网络时间、 网络标识前面是否加国家名称缩写。 


SHOW MME NITZ; 


`
命令 (No.2): SHOW MME NITZ

操作维护   是否发送NI   发送NI场景   是否发送TZ   发送TZ场景   在下发TZ时是否通知用户网络时间   网络标识前面是否加国家名称缩写   本网的网络长标识   长标识编码方式   本网的网络短标识   短标识编码方式   用户别名 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改       否           IMSI附着     否           IMSI附着     否                               否                               operator           BIT7             operator           BIT7  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.041 秒）。


` 








父主题： [MME全局NITZ配置](../../zh-CN/tree/N_12609311.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## MME基于IMSI号段的NITZ发送策略配置 
## MME基于IMSI号段的NITZ发送策略配置 


[](None)背景知识 


用户在MME中完成附着或TAU后，MME可以通过向UE发送EMM information消息，为用户提供网络标识信息和时区信息。用户收到后显示在终端界面以便用户获知当前接入到哪个网络，以及所在的时区。网络标识分为全名标识和简写标识两种。 


MME发送NITZ策略包括全局发送、基于IMSI号段发送。如果用户匹配IMSI号段，则执行按IMSI号段发送NITZ策略；否则执行全局NITZ策略。 




[](None)功能描述 


MME基于IMSI号段的NITZ发送策略配置，包括IMSI号段、是否发生NI、发送NI场景、是否发生TZ、发送TZ场景、在下发TZ时是否通知用户网络时间等参数的配置。 




[](None)相关主题 



 

新增MME基于IMSI号段的NITZ发送策略配置(ADD MME IMSI NITZ)
 

 

修改MME基于IMSI号段的NITZ发送策略配置(SET MME IMSI NITZ)
 

 

删除MME基于IMSI号段的NITZ发送策略配置(DEL MME IMSI NITZ)
 

 

查询MME基于IMSI号段的NITZ发送策略配置(SHOW MME IMSI NITZ)
 

 








父主题： [NITZ配置](../../zh-CN/tree/N_1260931.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增MME基于IMSI号段的NITZ发送策略配置(ADD MME IMSI NITZ) 
### 新增MME基于IMSI号段的NITZ发送策略配置(ADD MME IMSI NITZ) 


[](None)命令功能 

新增MME基于IMSI号段的NITZ发送策略配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|设置是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发网络标识给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发网络标识给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发网络标识或时区信息给UE，MME/SGSN下发网络标识给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发网络标识给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE（SGSN不支持）。当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络表示给UE（SGSN不支持）。上面MME/SGSN下发网络标识给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|设置是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发时区信息给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发时区信息给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发时区信息给UE，此时MME/SGSN下发时区信息给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发时区信息给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。（SGSN不支持）当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE（SGSN不支持）。上面MME/SGSN下发时区信息给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。






[](None)命令举例 


新增MME基于IMSI号段的NITZ发送策略，IMSI号段为“46001”，是否发送NI“是”，发送NI场景为“IMSI附着”，是否发送TZ“是”，发送TZ场景为“IMSI附着”。 


ADD MME IMSI NITZ:IMSIIDX="46001",IFSENDNI="YES",SCENENI="IMSI",IFSENDTZ="YES",SCENETZ="IMSI"; 








父主题： [MME基于IMSI号段的NITZ发送策略配置](../../zh-CN/tree/N_12609312.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改MME基于IMSI号段的NITZ发送策略配置(SET MME IMSI NITZ) 
### 修改MME基于IMSI号段的NITZ发送策略配置(SET MME IMSI NITZ) 


[](None)命令功能 

修改MME基于IMSI号段的NITZ发送策略配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发网络标识给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发网络标识给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发网络标识或时区信息给UE，MME/SGSN下发网络标识给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发网络标识给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE（SGSN不支持）。当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络表示给UE（SGSN不支持）。上面MME/SGSN下发网络标识给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发时区信息给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发时区信息给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发时区信息给UE，此时MME/SGSN下发时区信息给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发时区信息给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。（SGSN不支持）当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE（SGSN不支持）。上面MME/SGSN下发时区信息给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。






[](None)命令举例 


修改MME基于IMSI号段的NITZ发送策略，IMSI号段为“46001”，是否发送NI“是”，发送NI场景为“IMSI附着”，是否发送TZ“是”，发送TZ场景为“IMSI附着”。 


SET MME IMSI NITZ:IMSIIDX="46001",IFSENDNI="YES",SCENENI="IMSI",IFSENDTZ="YES",SCENETZ="IMSI"; 








父主题： [MME基于IMSI号段的NITZ发送策略配置](../../zh-CN/tree/N_12609312.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除MME基于IMSI号段的NITZ发送策略配置(DEL MME IMSI NITZ) 
### 删除MME基于IMSI号段的NITZ发送策略配置(DEL MME IMSI NITZ) 


[](None)命令功能 

删除MME基于IMSI号段的NITZ发送策略配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。






[](None)命令举例 


删除MME基于IMSI号段的NITZ发送策略，IMSI号段为“46001”。 


DEL MME IMSI NITZ:IMSIIDX="46001"; 








父主题： [MME基于IMSI号段的NITZ发送策略配置](../../zh-CN/tree/N_12609312.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询MME基于IMSI号段的NITZ发送策略配置(SHOW MME IMSI NITZ) 
### 查询MME基于IMSI号段的NITZ发送策略配置(SHOW MME IMSI NITZ) 


[](None)命令功能 

查询MME基于IMSI号段的NITZ发送策略配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发网络标识给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发网络标识给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发网络标识或时区信息给UE，MME/SGSN下发网络标识给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发网络标识给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE（SGSN不支持）。当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络表示给UE（SGSN不支持）。上面MME/SGSN下发网络标识给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发时区信息给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发时区信息给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发时区信息给UE，此时MME/SGSN下发时区信息给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发时区信息给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。（SGSN不支持）当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE（SGSN不支持）。上面MME/SGSN下发时区信息给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。






[](None)命令举例 


查询MME基于IMSI号段的NITZ发送策略配置。 


SHOW MME IMSI NITZ; 


`
命令 (No.1): SHOW MME IMSI NITZ


IMSI号段   是否发送NI   发送NI场景   是否发送TZ   发送TZ场景   在下发TZ时是否通知用户网络时间
---------------------------------------------------------------------------------------------
46001      是           IMSI附着     是           IMSI附着     否
---------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.037 秒）。
` 








父主题： [MME基于IMSI号段的NITZ发送策略配置](../../zh-CN/tree/N_12609312.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGSN全局NITZ配置 
## SGSN全局NITZ配置 


[](None)背景知识 


用户在SGSN中完成附着或RAU后，SGSN可以通过向UE发送GMM information消息，为用户提供网络标识信息和时区信息。用户收到后显示在终端界面以便用户获知当前接入到哪个网络，以及所在的时区。网络标识分为全名标识和简写标识两种。 


SGSN发送NITZ策略包括全局发送、基于IMSI号段发送。如果用户匹配IMSI号段，则执行按IMSI号段发送NITZ策略；否则执行全局NITZ策略。 




[](None)功能描述 


SGSN全局NITZ配置，包括是否发生NI、发送NI场景；是否发生TZ、发送TZ场景；在下发TZ时是否通知用户网络时间、本网的网络长标识、长标识编码方式、本网的网络短标识、长标识编码方式、短标识编码方式等参数的配置。 




[](None)相关主题 



 

设置SGSN全局NITZ配置(SET NITZ)
 

 

查询SGSN全局NITZ配置(SHOW NITZ)
 

 








父主题： [NITZ配置](../../zh-CN/tree/N_1260931.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置SGSN全局NITZ配置(SET NITZ) 
### 设置SGSN全局NITZ配置(SET NITZ) 


[](None)命令功能 

该命令用于设置SGSN全局网络标识和时区。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发网络标识给UE。终端正在业务接入：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发网络标识给UE。终端首次登记到网络：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发网络标识或时区信息给UE，MME/SGSN下发网络标识给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发网络标识给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE。时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络表示给UE。上面MME/SGSN下发网络标识给UE的 六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发时区信息给UE。终端正在业务接入：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发时区信息给UE。终端首次登记到网络：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发时区信息给UE，此时MME/SGSN下发时区信息给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发时区信息给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE。上面MME/SGSN下发时区信息给UE的 六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。
ADDCNY|网络标识前面是否加国家名称缩写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发网络标识给UE，则通知UE需要在网络标识前添加国家名称缩写。该参数设置为“否(NO)”，若MME/SGSN需要下发网络标识给UE，则通知UE无需在网络标识前添加国家名称缩写。
LNAME|本网的网络长标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络全称。
LNAMECODE|长标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
SNAME|本网的网络短标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络简称。
SNAMECODE|短标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|注释该项配置信息，起备注作用。






[](None)命令举例 


设置首次注册到本局MME时下发网络标识给UE、当首次注册到本局MME时下发时区信息给UE、下发时区时需要同时下发网络格林威治时间给UE、全局网络全称为“epc.mcc460.mnc03.3gpp.org.work.zte.com.cn”、全局网络全称的编码格式为“GSM 7 bit Default Alphabet”、全局网络简称为“zte.com.cn”、全局网络简称的编码格式为“UCS2”。 


设置成功后，用户首次接入到本网络时，比如用户附着或者用户从它局跟踪区更新到本局MME，通过EMM Information Request消息下发配置的网路标识给UE，包括使用“GSM 7 bit Default Alphabet”编码的网络全称、使用"UCS2"编码的网络简称；此外，EMM Information Request消息还携带当前时区以及当前网络格林威治时间给UE。 


SET NITZ:IFSENDNI="YES",SCENENI="REGIST",IFSENDTZ="YES",SCENETZ="REGIST",SENDTM="YES",ADDCNY="YES",LNAME="epc.mcc460.mnc03.3gpp.org.work.zte.com.cn",LNAMECODE="BIT7",SNAME="zte.com.cn",SNAMECODE="UCS2"; 








父主题： [SGSN全局NITZ配置](../../zh-CN/tree/N_12609313.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGSN全局NITZ配置(SHOW NITZ) 
### 查询SGSN全局NITZ配置(SHOW NITZ) 


[](None)命令功能 

该命令用于查询SGSN全局网络标识和时区。


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发网络标识给UE。终端正在业务接入：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发网络标识给UE。终端首次登记到网络：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发网络标识或时区信息给UE，MME/SGSN下发网络标识给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发网络标识给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE（SGSN不支持）。时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络表示给UE（SGSN不支持）。上面MME/SGSN下发网络标识给UE的 六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发时区信息给UE。终端正在业务接入：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发时区信息给UE。终端首次登记到网络：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发时区信息给UE，此时MME/SGSN下发时区信息给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发时区信息给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。（SGSN不支持）时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE（SGSN不支持）。上面MME/SGSN下发时区信息给UE的 六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。
ADDCNY|网络标识前面是否加国家名称缩写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发网络标识给UE，则通知UE需要在网络标识前添加国家名称缩写。该参数设置为“否(NO)”，若MME/SGSN需要下发网络标识给UE，则通知UE无需在网络标识前添加国家名称缩写。
LNAME|本网的网络长标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络全称。
LNAMECODE|长标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
SNAME|本网的网络短标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络简称。
SNAMECODE|短标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
NAME|用户别名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~50个字符。|注释该项配置信息，起备注作用。






[](None)命令举例 


查询MME下发网络标识和时区的场景、全局网络标识及其编码格式、是否下发网络时间、UE是否需要在网络名称前添加国家缩写。 


SHOW NITZ; 


`
命令 (No.9): SHOW NITZ

操作维护   是否发送NI   发送NI场景           是否发送TZ   发送TZ场景           在下发TZ时是否通知用户网络时间   网络标识前面是否加国家名称缩写   本网的网络长标识                            长标识编码方式   本网的网络短标识   短标识编码方式   用户别名
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改       是           终端首次登记到网络   是           终端首次登记到网络   是                               是                               epc.mcc460.mnc03.3gpp.org.work.zte.com.cn   BIT7             zte.com.cn         UCS2             
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.053 秒）。

` 








父主题： [SGSN全局NITZ配置](../../zh-CN/tree/N_12609313.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## SGSN基于IMSI号段的NITZ发送策略配置 
## SGSN基于IMSI号段的NITZ发送策略配置 


[](None)背景知识 


用户在SGSN中完成附着或RAU后，SGSN可以通过向UE发送GMM information消息，为用户提供网络标识信息和时区信息。用户收到后显示在终端界面以便用户获知当前接入到哪个网络，以及所在的时区。网络标识分为全名标识和简写标识两种。 


SGSN发送NITZ策略包括全局发送、基于IMSI号段发送。如果用户匹配IMSI号段，则执行按IMSI号段发送NITZ策略；否则执行全局NITZ策略。 




[](None)功能描述 


SGSN基于IMSI号段的NITZ发送策略配置，包括IMSI号段、是否发生NI、发送NI场景、是否发生TZ、发送TZ场景、在下发TZ时是否通知用户网络时间等参数的配置。 




[](None)相关主题 



 

新增SGSN基于IMSI号段的NITZ发送策略配置(ADD SGSN IMSI NITZ)
 

 

修改SGSN基于IMSI号段的NITZ发送策略配置(SET SGSN IMSI NITZ)
 

 

删除SGSN基于IMSI号段的NITZ发送策略配置(DEL SGSN IMSI NITZ)
 

 

查询SGSN基于IMSI号段的NITZ发送策略配置(SHOW SGSN IMSI NITZ)
 

 








父主题： [NITZ配置](../../zh-CN/tree/N_1260931.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增SGSN基于IMSI号段的NITZ发送策略配置(ADD SGSN IMSI NITZ) 
### 新增SGSN基于IMSI号段的NITZ发送策略配置(ADD SGSN IMSI NITZ) 


[](None)命令功能 

新增SGSN基于IMSI号段的NITZ发送策略配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|设置是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发网络标识给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发网络标识给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发网络标识或时区信息给UE，MME/SGSN下发网络标识给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发网络标识给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE（SGSN不支持）。当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络表示给UE（SGSN不支持）。上面MME/SGSN下发网络标识给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|设置是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发时区信息给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发时区信息给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发时区信息给UE，此时MME/SGSN下发时区信息给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发时区信息给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。（SGSN不支持）当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE（SGSN不支持）。上面MME/SGSN下发时区信息给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。






[](None)命令举例 


新增SGSN基于IMSI号段的NITZ发送策略，IMSI号段为“46001”，是否发送NI“是”，发送NI场景为“终端附着位置更新业务请求”，是否发送TZ“是”，发送TZ场景为“终端附着位置更新业务请求”。 


ADD SGSN IMSI NITZ:IMSIIDX="46001",IFSENDNI="YES",SCENENI="UEACCESS",IFSENDTZ="YES",SCENETZ="UEACCESS"; 








父主题： [SGSN基于IMSI号段的NITZ发送策略配置](../../zh-CN/tree/N_12609314.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改SGSN基于IMSI号段的NITZ发送策略配置(SET SGSN IMSI NITZ) 
### 修改SGSN基于IMSI号段的NITZ发送策略配置(SET SGSN IMSI NITZ) 


[](None)命令功能 

修改SGSN基于IMSI号段的NITZ发送策略配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发网络标识给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发网络标识给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发网络标识或时区信息给UE，MME/SGSN下发网络标识给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发网络标识给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE（SGSN不支持）。当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络表示给UE（SGSN不支持）。上面MME/SGSN下发网络标识给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发时区信息给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发时区信息给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发时区信息给UE，此时MME/SGSN下发时区信息给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发时区信息给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。（SGSN不支持）当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE（SGSN不支持）。上面MME/SGSN下发时区信息给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。






[](None)命令举例 


修改SGSN基于IMSI号段的NITZ发送策略，IMSI号段为“46001”，是否发送NI“是”，发送NI场景为“终端附着位置更新业务请求”，是否发送TZ“是”，发送TZ场景为“终端附着位置更新业务请求”。 


SET SGSN IMSI NITZ:IMSIIDX="46001",IFSENDNI="YES",SCENENI="UEACCESS",IFSENDTZ="YES",SCENETZ="UEACCESS"; 








父主题： [SGSN基于IMSI号段的NITZ发送策略配置](../../zh-CN/tree/N_12609314.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除SGSN基于IMSI号段的NITZ发送策略配置(DEL SGSN IMSI NITZ) 
### 删除SGSN基于IMSI号段的NITZ发送策略配置(DEL SGSN IMSI NITZ) 


[](None)命令功能 

删除SGSN基于IMSI号段的NITZ发送策略配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。






[](None)命令举例 


删除SGSN基于IMSI号段的NITZ发送策略，IMSI号段为“46001”。 


DEL SGSN IMSI NITZ:IMSIIDX="46001"; 








父主题： [SGSN基于IMSI号段的NITZ发送策略配置](../../zh-CN/tree/N_12609314.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询SGSN基于IMSI号段的NITZ发送策略配置(SHOW SGSN IMSI NITZ) 
### 查询SGSN基于IMSI号段的NITZ发送策略配置(SHOW SGSN IMSI NITZ) 


[](None)命令功能 

查询SGSN基于IMSI号段的NITZ发送策略配置。


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:任选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
IMSIIDX|IMSI号段|参数可选性:必选参数；参数类型:字符型；参数范围为:1~15个字符。|IMSI号段，IMSI号段是从IMSI号码中取前面特定位数的号码作为一部份用户号段，来标识具有特定号码开头的用户群体，如46001表示以46001开头的IMSI的用户的号段。
IFSENDNI|是否发送NI|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送NI信息给UE。
SCENENI|发送NI场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发网络标识给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发网络标识给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发网络标识给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发网络标识或时区信息给UE，MME/SGSN下发网络标识给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发网络标识给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发网络标识给UE（SGSN不支持）。当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发网络表示给UE（SGSN不支持）。上面MME/SGSN下发网络标识给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发网络标识给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发网络标识给UE。
IFSENDTZ|是否发送TZ|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置是否需发送TZ信息给UE。
SCENETZ|发送TZ场景|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|ZXUN uMAC-MME/SGSN下发时区信息给UE，目前支持如下六种场景：不发送：MME/SGSN不会下发时区信息给UE。终端在业务接入时：用户执行附着、跟踪区/路由区更新或者业务请求时，此时MME/SGSN下发时区信息给UE。终端首次登记到网络时：用户附着、用户从其他局跟踪区更新/路由区更新到本局、用户从其他局切换到本局、或者自用户附着以来MME/SGSN未下发时区信息给UE，此时MME/SGSN下发时区信息给UE。当网络改变它的标识：当用户所在网络的网络标识发生改变，或者若用户所在网络没有配置相关网络标识但全局网络标识发生改变，MME/SGSN下发时区信息给UE。当DST夏令时切入或切出：网络启用了夏令时，网络进入夏令时或者退出夏令时，此时MME下发时区信息给UE。（SGSN不支持）当时区改变：用户当前所在时区发生改变，或者MME之前未下发时区信息给UE，此时MME下发时区信息给UE（SGSN不支持）。上面MME/SGSN下发时区信息给UE的六种场景，无优先级区别，运营商可以选择一个或者多个场景，用以MME/SGSN下发时区信息给UE。当选择多个场景时，只要满足其中一个，则MME/SGSN下发时区信息给UE。
SENDTM|在下发TZ时是否通知用户网络时间|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发时区信息给UE，则时区信息包括用户当前所在时区、网络当前格林威治时间。该参数设置为“否(NO)”，若MME/SGSN需要下发时区信息给UE，则时区信息仅包括用户当前所在时区。






[](None)命令举例 


查询SGSN基于IMSI号段的NITZ发送策略配置。 


SHOW SGSN IMSI NITZ; 


`
命令 (No.1): SHOW SGSN IMSI NITZ


IMSI号段   是否发送NI   发送NI场景   是否发送TZ   发送TZ场景   在下发TZ时是否通知用户网络时间
---------------------------------------------------------------------------------------------
46001      是           IMSI附着     是           IMSI附着     否
---------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.037 秒）。
` 








父主题： [SGSN基于IMSI号段的NITZ发送策略配置](../../zh-CN/tree/N_12609314.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


## 基于PLMN的NI配置 
## 基于PLMN的NI配置 


[](None)背景知识 


用户在MME中完成附着或TAU后，MME可以通过向UE发送EMM information消息，为用户提供网络标识信息，用户收到后显示在终端界面以便用户获知当前接入到哪个网络。网络标识分为全名标识和简写标识两种。 




[](None)功能描述 



                如果MME需要为不同PLMN的用户，提供不同的网络标识，可以在“基于PLMN的NI配置”中针对不同的PLMN设置网络标识，MME在给UE下发EMM information消息时，携带用户归属PLMN对应的网络标识。
	当针对PLMN未配置时，MME使用全局默认网络标识下发，默认网络标识在
                [SET NITZ](../mml/1260230.html)
                命令中配置。
            



                MME可以控制是否下发网络标识，并支持区分场景下发网络标识，命令参见：
                [SET NITZ](../mml/1260230.html)
                。如果MME配置为不下发网络标识，“基于PLMN的NI配置”不生效。
            


本模块配置受NITZ License控制，License不支持时该命令不显示且不可执行 




[](None)相关主题 



 

新增基于PLMN的NI配置(ADD PLMN NI)
 

 

修改基于PLMN的NI配置(SET PLMN NI)
 

 

删除基于PLMN的NI配置(DEL PLMN NI)
 

 

查询基于PLMN的NI配置(SHOW PLMN NI)
 

 

设置PLMN NI策略配置(SET PLMN NI POLICY)
 

 

查询PLMN NI策略配置(SHOW PLMN NI POLICY)
 

 








父主题： [NITZ配置](../../zh-CN/tree/N_1260931.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 新增基于PLMN的NI配置(ADD PLMN NI) 
### 新增基于PLMN的NI配置(ADD PLMN NI) 


[](None)命令功能 


该命令用于新增基于PLMN的网络标识配置。当运营商需要针对不同的PLMN灵活配置网络标识时，使用该命令。配置成功后，若本局MME判断需要下发网络标识时，此时MME携带该配置对应的网络标识给UE。 




[](None)注意事项 


新增该配置之前，首先设置MME/SGSN下发网络标识的场景，配置命令为[SET NITZ](1260230.html)。


NI支持全局配置和按PLMN配置，优先采用PLMN配置的NI，如果接入的PLMN没有配置NI，则采用全局NI。全局NI设置命令为[SET NITZ](1260230.html)。


NI最大支持210个字节，采用不同编码方式会影响实际使用名称长度，如US2编码是2个字节来表示1个字符。 


在网络标识改变，对于已接入的用户，MME/SGSN并不主动通知UE发生了改变，UE下次接入时，才能发现相应信息已改变。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由MCC和MNC组成，用以标识某个国家的某个移动通信网络。比如中国移动GSM网络的PLMN为460 00。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|标识移动用户所在的国家或者地区，由三位十进制数字组成，比如中国大陆MCC为460，中国香港MCC为454。每个国家或者地区，其移动国家码都不会相同，具体分配由国际标准组织ITU负责。一个国家或者地区，可以有一个移动国家码，比如中国香港(454)，也可以有多个移动国家码，比如中国大陆(460和461)。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|一个国家可能拥有多个移动运营商，同一个移动运营商又有可能拥有多个移动通信网络。在一个国家或者地区范围内，移动网号可以确定移动用户归属于哪一个运营商的哪一个移动通信网络。移动网号有2或者3个十进制数字组成，具体分配由移动网络所在的地区或者国家负责。
ADDCI|网络标识前面是否加国家名称缩写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|该参数设置为“是(YES)”，若MME/SGSN需要下发网络标识给UE，则通知UE需要在网络标识前添加国家名称缩写。该参数设置为“否(NO)”，若MME/SGSN需要下发网络标识给UE，则通知UE无需在网络标识前添加国家名称缩写。
FULLNISTR|本网的网络长标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络全称。
FULLNICODEPLAN|长标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:GSM 7 bit Default Alphabet。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
SHORTNISTR|本网的网络短标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络简称。
SHORTNICODEPLAN|短标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:GSM 7 bit Default Alphabet。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。






[](None)命令举例 


新增PLMN为46001的网络标识，其网络长标识为“epc.mnc001.mcc460.3gppnetwork.org”，网络短标识为“zte.com.cn”。 


ADD PLMN NI:PLMN="460"-"01",FULLNISTR="epc.mnc001.mcc460.3gppnetwork.org",SHORTNISTR="zte.com.cn"; 








父主题： [基于PLMN的NI配置](../../zh-CN/tree/N_12609315.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 修改基于PLMN的NI配置(SET PLMN NI) 
### 修改基于PLMN的NI配置(SET PLMN NI) 


[](None)命令功能 


该命令用于修改基于PLMN的网络标识配置。当运营商需要修改特定PLMN所对应的网络标识时，使用该命令。配置成功后，后续本局MME判断需要下发网络标识时，此时MME携带修改后配置对应的网络标识给UE。 




[](None)注意事项 


新增该配置之前，首先设置MME/SGSN下发网络标识的场景，配置命令为[SET NITZ](1260230.html)。


NI支持全局配置和按PLMN配置，优先采用PLMN配置的NI，如果接入的PLMN没有配置NI，则采用全局NI。全局NI设置命令为[SET NITZ](1260230.html)。


NI最大支持210个字节，采用不同编码方式会影响实际使用名称长度，如US2编码是2个字节来表示1个字符。 


在网络标识改变，对于已接入的用户，MME/SGSN并不主动通知UE发生了改变，UE下次接入时，才能发现相应信息已改变。 




[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由MCC和MNC组成，用以标识某个国家的某个移动通信网络。比如中国移动GSM网络的PLMN为460 00。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|标识移动用户所在的国家或者地区，由三位十进制数字组成，比如中国大陆MCC为460，中国香港MCC为454。每个国家或者地区，其移动国家码都不会相同，具体分配由国际标准组织ITU负责。一个国家或者地区，可以有一个移动国家码，比如中国香港(454)，也可以有多个移动国家码，比如中国大陆(460和461)。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|一个国家可能拥有多个移动运营商，同一个移动运营商又有可能拥有多个移动通信网络。在一个国家或者地区范围内，移动网号可以确定移动用户归属于哪一个运营商的哪一个移动通信网络。移动网号有2或者3个十进制数字组成，具体分配由移动网络所在的地区或者国家负责。
ADDCI|网络标识前面是否加国家名称缩写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发网络标识给UE，则通知UE需要在网络标识前添加国家名称缩写。该参数设置为“否(NO)”，若MME/SGSN需要下发网络标识给UE，则通知UE无需在网络标识前添加国家名称缩写。
FULLNISTR|本网的网络长标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络全称。
FULLNICODEPLAN|长标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
SHORTNISTR|本网的网络短标识|参数可选性:任选参数；参数类型:字符型；参数范围为:0~208个字符。|运营商命名的移动通信网络简称。
SHORTNICODEPLAN|短标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。






[](None)命令举例 


将PLMN为46001的长网络标识编码格式修改为“UCS2”。 


SET PLMN NI:PLMN="460"-"01",FULLNICODEPLAN="UCS2"; 








父主题： [基于PLMN的NI配置](../../zh-CN/tree/N_12609315.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 删除基于PLMN的NI配置(DEL PLMN NI) 
### 删除基于PLMN的NI配置(DEL PLMN NI) 


[](None)命令功能 


该命令用于删除一个基于PLMN的网络标识配置。当运营商需要删除特定PLMN的网络标识时，使用该命令。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:必选参数；参数类型:复合参数|由MCC和MNC组成，用以标识某个国家的某个移动通信网络。比如中国移动GSM网络的PLMN为460 00。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|标识移动用户所在的国家或者地区，由三位十进制数字组成，比如中国大陆MCC为460，中国香港MCC为454。每个国家或者地区，其移动国家码都不会相同，具体分配由国际标准组织ITU负责。一个国家或者地区，可以有一个移动国家码，比如中国香港(454)，也可以有多个移动国家码，比如中国大陆(460和461)。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|一个国家可能拥有多个移动运营商，同一个移动运营商又有可能拥有多个移动通信网络。在一个国家或者地区范围内，移动网号可以确定移动用户归属于哪一个运营商的哪一个移动通信网络。移动网号有2或者3个十进制数字组成，具体分配由移动网络所在的地区或者国家负责。






[](None)命令举例 


删除PLMN为46001的网络标识配置。 


DEL PLMN NI:PLMN="460"-"01"; 








父主题： [基于PLMN的NI配置](../../zh-CN/tree/N_12609315.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询基于PLMN的NI配置(SHOW PLMN NI) 
### 查询基于PLMN的NI配置(SHOW PLMN NI) 


[](None)命令功能 


该命令用于查询本局MME配置的全部或者特定PLMN的网络标识。 


当该命令用于查询特定PLMN的网络标识配置，需要填写所需要查询的PLMN。 




[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:复合参数|由MCC和MNC组成，用以标识某个国家的某个移动通信网络。比如中国移动GSM网络的PLMN为460 00。
MCC|移动国家码|参数可选性:必选参数；参数类型:字符型；参数范围为:3~3个字符。|标识移动用户所在的国家或者地区，由三位十进制数字组成，比如中国大陆MCC为460，中国香港MCC为454。每个国家或者地区，其移动国家码都不会相同，具体分配由国际标准组织ITU负责。一个国家或者地区，可以有一个移动国家码，比如中国香港(454)，也可以有多个移动国家码，比如中国大陆(460和461)。
MNC|移动网号|参数可选性:必选参数；参数类型:字符型；参数范围为:2~3个字符。|一个国家可能拥有多个移动运营商，同一个移动运营商又有可能拥有多个移动通信网络。在一个国家或者地区范围内，移动网号可以确定移动用户归属于哪一个运营商的哪一个移动通信网络。移动网号有2或者3个十进制数字组成，具体分配由移动网络所在的地区或者国家负责。






[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
PLMN|PLMN|参数可选性:任选参数；参数类型:字符型。|由MCC和MNC组成，用以标识某个国家的某个移动通信网络。比如中国移动GSM网络的PLMN为460 00。
ADDCI|网络标识前面是否加国家名称缩写|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数设置为“是(YES)”，若MME/SGSN需要下发网络标识给UE，则通知UE需要在网络标识前添加国家名称缩写。该参数设置为“否(NO)”，若MME/SGSN需要下发网络标识给UE，则通知UE无需在网络标识前添加国家名称缩写。
FULLNISTR|本网的网络长标识|参数可选性:任选参数；参数类型:字符型。|运营商命名的移动通信网络全称。
FULLNICODEPLAN|长标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
SHORTNISTR|本网的网络短标识|参数可选性:任选参数；参数类型:字符型。|运营商命名的移动通信网络简称。
SHORTNICODEPLAN|短标识编码方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|目前支持两种编码方式：GSM 7 bit Default Alphabet编码格式。其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式。其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit default alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。






[](None)命令举例 


查询所有基于PLMN的网络标识配置。 


SHOW PLMN NI; 


`
命令 (No.1): SHOW PLMN NI

PLMN     网络标识前面是否加国家名称缩写   本网的网络长标识                    长标识编码方式               本网的网络短标识   短标识编码方式
--------------------------------------------------------------------------------------------------------------------------------------------
460-01   是                               epc.mnc001.mcc460.3gppnetwork.org   GSM 7 bit Default Alphabet   zte.com.cn         GSM 7 bit Default Alphabet
--------------------------------------------------------------------------------------------------------------------------------------------
记录数 1

命令执行成功（耗时 0.037 秒）。
` 








父主题： [基于PLMN的NI配置](../../zh-CN/tree/N_12609315.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 设置PLMN NI策略配置(SET PLMN NI POLICY) 
### 设置PLMN NI策略配置(SET PLMN NI POLICY) 


[](None)命令功能 

设置PLMN NI策略配置


[](None)注意事项 

无。


[](None)参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SELPLMNORIMSI|Selected PLMN或IMSI的PLMN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置根据用户接入的PLMN（Selected PLMN）或根据用户IMSI对应的HPLMN，下发不同的NI。






[](None)命令举例 


将PLMN NI策略修改为“Selected PLMN”。 


SET PLMN NI POLICY:SELPLMNORIMSI="SELECTED"; 








父主题： [基于PLMN的NI配置](../../zh-CN/tree/N_12609315.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


### 查询PLMN NI策略配置(SHOW PLMN NI POLICY) 
### 查询PLMN NI策略配置(SHOW PLMN NI POLICY) 


[](None)命令功能 

查询PLMN NI策略配置


[](None)注意事项 

无。


[](None)输出参数说明 


[](None)标识|名称|类型|说明
---|---|---|---
SELPLMNORIMSI|Selected PLMN或IMSI的PLMN|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|设置根据用户接入的PLMN（Selected PLMN）或根据用户IMSI对应的HPLMN，下发不同的NI。






[](None)命令举例 


查询PLMN NI策略配置。 


SHOW PLMN NI POLICY; 


`
命令 (No.1):  SHOW PLMN NI POLICY

Selected PLMN or PLMN of IMSI
-----------------------------
Selected PLMN(SELECTED)
-----------------------------
记录数 1

命令执行成功（耗时 0.037 秒）。
` 








父主题： [基于PLMN的NI配置](../../zh-CN/tree/N_12609315.html)












Copyright © ZTE Corporation. All right reserved. 


PPDN Online KnowledgeBase Powered by DITA.   Technology Management Dept, Central R&D Insititute. 


