

统计全局的GSM网络的路由更新流程时需要创建。建议颗粒为15分钟。 


# C405770001 SGSN内的RAU请求次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN内的RAU请求次数。 


测量触发点 :SGSN收到“Routing Area Update Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为GPRS路由更新，路由更新成功或失败后统计。 


采集方式 :CC 


# C405770002 SGSN内的RAU成功次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN内的RAU成功次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405770003 由于非法用户导致的SGSN内的RAU失败次数-GSM 


计数器描述 :由于非法用户导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 


采集方式 :CC 


# C405770004 由于非法设备导致的SGSN内的RAU失败次数-GSM 


计数器描述 :由于非法设备导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 


采集方式 :CC 


# C405770005 由于GPRS服务不允许导致的SGSN内的RAU失败次数-GSM 


计数器描述 :由于GPRS服务不允许导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS
services not allowed”时统计。 


采集方式 :CC 


# C405770006 由于GPRS服务和非GPRS服务不允许导致的SGSN内RAU失败次数-GSM 


计数器描述 :由于GPRS服务和非GPRS服务不允许导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770007 由于网络无法获取MS ID导致SGSN内的路由更新失败次数-GSM 
计数器描述 :由于网络无法获取MS ID导致用户（Gb口接入）在SGSN内的路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS
identity cannot be derived by the network”时统计。 
采集方式 :CC 
# C405770008 由于用户隐式分离导致的SGSN内的RAU失败次数-GSM 


计数器描述 :由于用户隐式分离导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 


采集方式 :CC 


# C405770009 由于PLMN不允许导致的SGSN内RAU失败次数-GSM 


计数器描述 :由于PLMN不允许导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 


采集方式 :CC 


# C405770010 由于位置区不允许导致的SGSN内的RAU失败次数-GSM 


计数器描述 :由于位置区不允许导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 


采集方式 :CC 


# C405770011 由于漫游位置区不允许导致的SGSN内的RAU失败次数-GSM 


计数器描述 :由于漫游位置区不允许导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 


采集方式 :CC 


# C405770012 由于GPRS服务在本PLMN不允许导致的SGSN内的RAU失败次数-GSM 


计数器描述 :由于GPRS服务在本PLMN不允许导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS
services not allowed in this PLMN”时统计。 


采集方式 :CC 


# C405770013 由于本位置区没有合适的小区导致的SGSN内的RAU失败次数-GSM 


计数器描述 :由于本位置区没有合适的小区导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No
Suitable Cells In Location Area”时统计。 


采集方式 :CC 


# C405770014 由于网络侧失败导致SGSN内的路由更新失败次数-GSM 


计数器描述 :由于网络侧失败导致用户（Gb口接入）在SGSN内的路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 


采集方式 :CC 


# C405770015 由于必选项错误导致SGSN内的路由更新失败次数-GSM 


计数器描述 :由于必选项错误导致用户（Gb口接入）在SGSN内的路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 


采集方式 :CC 


# C405770016 由于消息类型不存在导致SGSN内的路由更新失败次数-GSM 


计数器描述 :由于消息类型不存在导致用户（Gb口接入）在SGSN内的路由更新失败次数 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770017 由于消息类型和协议不匹配导致SGSN内的路由更新失败次数-GSM 


计数器描述 :由于消息类型和协议不匹配导致用户（Gb口接入）在SGSN内的路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 


采集方式 :CC 


# C405770018 由于信元错误导致的SGSN内RAU失败次数-GSM 


计数器描述 :由于信元错误导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770019 由于未指定的协议错误导致的SGSN内RAU失败次数-GSM 


计数器描述 :由于未指定的协议错误导致用户（Gb口接入）在SGSN内的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 


采集方式 :CC 


# C405770020 SGSN内的联合路由更新请求次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN内的联合路由更新请求次数。 


测量触发点 :SGSN收到“Routing Area Update Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为combined
RA/LA updating，当GPRS路由更新成功并且Gs口位置更新成功时或者SGSN内联合路由更新失败时统计。 


采集方式 :CC 


# C405770021 SGSN内的联合路由更新成功次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN内的联合路由更新成功次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，当GPRS路由更新成功并且Gs口位置更新成功时统计。 


采集方式 :CC 


# C405770022 由于非法用户导致的SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于非法用户导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal MS”或“0x2：IMSI unknown
in HLR”时统计。 


采集方式 :CC 


# C405770023 由于非法设备导致的SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于非法设备导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal ME”时统计。 


采集方式 :CC 


# C405770024 由于GPRS服务不允许导致的SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务不允许导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770025 由于GPRS服务和非GPRS服务不允许导致的SGSN内联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务和非GPRS服务不允许导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770026 由于网络无法获取MS ID导致SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于网络无法获取MS ID导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS identity cannot be derived
by the network”时统计。 


采集方式 :CC 


# C405770027 由于用户隐式分离导致的SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于用户隐式分离导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly detached”时统计。 


采集方式 :CC 


# C405770028 由于PLMN不允许导致的SGSN内联合路由更新失败次数-GSM 


计数器描述 :由于PLMN不允许导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 


采集方式 :CC 


# C405770029 由于位置区不允许导致的SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于位置区不允许导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location Area not allowed”时统计。 


采集方式 :CC 


# C405770030 由于漫游位置区不允许导致的SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于漫游位置区不允许导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming not allowed in this
location area”时统计。 


采集方式 :CC 


# C405770031 由于GPRS服务在本PLMN不允许导致的SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务在本PLMN不允许导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS services not allowed
in this PLMN”时统计。 


采集方式 :CC 


# C405770032 由于本位置区没有合适的小区导致的SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于本位置区没有合适的小区导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No Suitable Cells In Location
Area”时统计。  


采集方式 :CC 


# C405770033 由于网络侧失败导致SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于网络侧失败导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”时统计。 


采集方式 :CC 


# C405770034 由于消息类型不存在导致SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于消息类型不存在导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message type non-existent
or not implemented”时统计。 


采集方式 :CC 


# C405770035 由于必选项错误导致SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于必选项错误导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid mandatory information”时统计。 


采集方式 :CC 


# C405770036 由于消息类型和协议不匹配导致SGSN内的联合路由更新失败次数-GSM 


计数器描述 :由于消息类型和协议不匹配导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message not compatible with
the protocol state”时统计。 


采集方式 :CC 


# C405770037 由于信元错误导致的SGSN内联合路由更新失败次数-GSM 


计数器描述 :由于信元错误导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770038 由于未指定的协议错误导致的SGSN内联合路由更新失败次数-GSM 


计数器描述 :由于未指定的协议错误导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 


采集方式 :CC 


# C405770039 SGSN间的RAU请求次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN间的RAU请求次数。 


测量触发点 :SGSN收到“Routing Area Update Request”消息，其中旧RA不属于本SGSN，路由更新类型为GPRS路由更新，更新成功或失败后统计。 


采集方式 :CC 


# C405770040 SGSN间的RAU成功次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN间的RAU成功次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405770041 由于非法用户导致的SGSN间的RAU失败次数-GSM 


计数器描述 :由于非法用户导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 


采集方式 :CC 


# C405770042 由于非法设备导致的SGSN间的RAU失败次数-GSM 


计数器描述 :由于非法设备导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 


采集方式 :CC 


# C405770043 由于GPRS服务不允许导致的SGSN间的RAU失败次数-GSM 


计数器描述 :由于GPRS服务不允许导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS
services not allowed”时统计。 


采集方式 :CC 


# C405770044 由于GPRS服务和非GPRS服务不允许导致的SGSN间RAU失败次数-GSM 


计数器描述 :由于GPRS服务和非GPRS服务不允许导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770045 由于网络无法获取MS ID导致SGSN间的路由更新失败次数-GSM 


计数器描述 :由于网络无法获取MS ID导致用户（Gb口接入）在SGSN间的路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS
identity cannot be derived by the network”时统计。 


采集方式 :CC 


# C405770046 由于用户隐式分离导致的SGSN间的RAU失败次数-GSM 


计数器描述 :由于用户隐式分离导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 


采集方式 :CC 


# C405770047 由于PLMN不允许导致的SGSN间RAU失败次数-GSM 


计数器描述 :由于PLMN不允许导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 


采集方式 :CC 


# C405770048 由于位置区不允许导致的SGSN间的RAU失败次数-GSM 


计数器描述 :由于位置区不允许导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 


采集方式 :CC 


# C405770049 由于漫游位置区不允许导致的SGSN间的RAU失败次数-GSM 


计数器描述 :由于漫游位置区不允许导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 


采集方式 :CC 


# C405770050 由于GPRS服务在本PLMN不允许导致的SGSN间的RAU失败次数-GSM 


计数器描述 :由于GPRS服务在本PLMN不允许导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS
services not allowed in this PLMN”时统计。 


采集方式 :CC 


# C405770051 由于本位置区没有合适的小区导致的SGSN间的RAU失败次数-GSM 


计数器描述 :由于本位置区没有合适的小区导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No
Suitable Cells In Location Area”时统计。 


采集方式 :CC 


# C405770052 由于网络侧失败导致SGSN间的路由更新失败次数-GSM 


计数器描述 :由于网络侧失败导致用户（Gb口接入）在SGSN间的路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 


采集方式 :CC 


# C405770053 由于必选项错误导致SGSN间的路由更新失败次数-GSM 


计数器描述 :由于必选项错误导致用户（Gb口接入）在SGSN间的路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 


采集方式 :CC 


# C405770054 由于消息类型不存在导致SGSN间的路由更新失败次数-GSM 


计数器描述 :由于消息类型不存在导致用户（Gb口接入）在SGSN间的路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770055 由于消息类型和协议不匹配导致SGSN间的路由更新失败次数-GSM 


计数器描述 :由于消息类型和协议不匹配导致用户（Gb口接入）在SGSN间的路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 


采集方式 :CC 


# C405770056 由于信元错误导致的SGSN间RAU失败次数-GSM 


计数器描述 :由于信元错误导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770057 由于未指定的协议错误导致的SGSN间RAU失败次数-GSM 


计数器描述 :由于未指定的协议错误导致用户（Gb口接入）在SGSN间的RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 


采集方式 :CC 


# C405770058 SGSN间的联合路由更新请求次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN间的联合路由更新请求次数。 


测量触发点 :SGSN收到“Routing Area Update Request”消息，其中旧RA不属于本SGSN，路由更新类型为combined
RA/LA updating，当GPRS路由更新成功并且Gs口位置更新成功时或者SGSN间联合路由更新失败时统计。 


采集方式 :CC 


# C405770059 SGSN间的联合路由更新成功次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN间的联合路由更新成功次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，当GPRS路由更新成功并且Gs口位置更新成功时统计。 


采集方式 :CC 


# C405770060 由于非法用户导致的SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于非法用户导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal MS”或“0x2：IMSI unknown
in HLR”时统计。 


采集方式 :CC 


# C405770061 由于非法设备导致的SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于非法设备导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal ME”时统计。 


采集方式 :CC 


# C405770062 由于GPRS服务不允许导致的SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务不允许导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770063 由于GPRS服务和非GPRS服务不允许导致的SGSN间联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务和非GPRS服务不允许导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770064 由于网络无法获取MS ID导致SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于网络无法获取MS ID导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS identity cannot be derived
by the network”时统计。 


采集方式 :CC 


# C405770065 由于用户隐式分离导致的SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于用户隐式分离导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly detached”时统计。 


采集方式 :CC 


# C405770066 由于PLMN不允许导致的SGSN间联合路由更新失败次数-GSM 


计数器描述 :由于PLMN不允许导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 


采集方式 :CC 


# C405770067 由于位置区不允许导致的SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于位置区不允许导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location Area not allowed”时统计。 


采集方式 :CC 


# C405770068 由于漫游位置区不允许导致的SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于漫游位置区不允许导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming not allowed in this
location area”时统计。 


采集方式 :CC 


# C405770069 由于GPRS服务在本PLMN不允许导致的SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务在本PLMN不允许导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS services not allowed
in this PLMN”时统计。 


采集方式 :CC 


# C405770070 由于本位置区没有合适的小区导致的SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于本位置区没有合适的小区导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No Suitable Cells In Location
Area”时统计。 


采集方式 :CC 


# C405770071 由于网络侧失败导致SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于网络侧失败导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”时统计。 


采集方式 :CC 


# C405770072 由于必选项错误导致SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于必选项错误导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid mandatory information”时统计。 


采集方式 :CC 


# C405770073 由于消息类型不存在导致SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于消息类型不存在导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message type non-existent
or not implemented”时统计。 


采集方式 :CC 


# C405770074 由于消息类型和协议不匹配导致SGSN间的联合路由更新失败次数-GSM 


计数器描述 :由于消息类型和协议不匹配导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message not compatible with
the protocol state”时统计。 


采集方式 :CC 


# C405770075 由于信元错误导致的SGSN间联合路由更新失败次数-GSM 


计数器描述 :由于信元错误导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770076 由于未指定的协议错误导致的SGSN间联合路由更新失败次数-GSM 


计数器描述 :由于未指定的协议错误导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN间的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 


采集方式 :CC 


# C405770077 周期性路由更新请求次数-GSM 


计数器描述 :用户（Gb口接入）周期性路由更新请求次数。 


测量触发点 :SGSN收到“Routing Area Update Request”消息，路由更新类型为周期性路由更新，更新成功或失败后统计。 


采集方式 :CC 


# C405770078 周期性路由更新成功次数-GSM 


计数器描述 :用户（Gb口接入）周期性路由更新成功次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405770079 由于非法用户导致的周期性RAU失败次数-GSM 


计数器描述 :由于非法用户导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 


采集方式 :CC 


# C405770080 由于非法设备导致的周期性RAU失败次数-GSM 


计数器描述 :由于非法设备导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 


采集方式 :CC 


# C405770081 由于GPRS服务不允许导致的周期性RAU失败次数-GSM 


计数器描述 :由于GPRS服务不允许导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“0x7：GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770082 由于GPRS服务和非GPRS服务不允许导致的周期性RAU失败次数-GSM 


计数器描述 :由于GPRS服务和非GPRS服务不允许导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770083 由于网络无法获取MS ID导致周期性路由更新失败次数-GSM 


计数器描述 :由于网络无法获取MS ID导致用户（Gb口接入）周期性路由更新失败次数 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS
identity cannot be derived by the network”时统计。 


采集方式 :CC 


# C405770084 由于用户隐式分离导致的周期性RAU失败次数-GSM 


计数器描述 :由于用户隐式分离导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 


采集方式 :CC 


# C405770085 由于PLMN不允许导致的周期性RAU失败次数-GSM 


计数器描述 :由于PLMN不允许导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 


采集方式 :CC 


# C405770086 由于位置区不允许导致的周期性RAU失败次数-GSM 


计数器描述 :由于位置区不允许导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 


采集方式 :CC 


# C405770087 由于漫游位置区不允许导致的周期性RAU失败次数-GSM 


计数器描述 :由于漫游位置区不允许导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 


采集方式 :CC 


# C405770088 由于GPRS服务在本PLMN不允许导致的周期性RAU失败次数-GSM 


计数器描述 :由于GPRS服务在本PLMN不允许导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS
services not allowed in this PLMN”时统计。 


采集方式 :CC 


# C405770089 由于本位置区没有合适的小区导致的周期性RAU失败次数-GSM 


计数器描述 :由于本位置区没有合适的小区导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No
Suitable Cells In Location Area”时统计。 


采集方式 :CC 


# C405770090 由于网络侧失败导致周期性路由更新失败次数-GSM 


计数器描述 :由于网络侧失败导致用户（Gb口接入）周期性路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 


采集方式 :CC 


# C405770091 由于必选项错误导致周期性路由更新失败次数-GSM 


计数器描述 :由于必选项错误导致用户（Gb口接入）周期性路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 


采集方式 :CC 


# C405770092 由于消息类型不存在导致周期性路由更新失败次数-GSM 


计数器描述 :由于消息类型不存在导致用户（Gb口接入）周期性路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770093 由于消息类型和协议不匹配导致周期性路由更新失败次数-GSM 


计数器描述 :由于消息类型和协议不匹配导致用户（Gb口接入）周期性路由更新失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 


采集方式 :CC 


# C405770094 由于信元错误导致的周期性RAU失败次数-GSM 


计数器描述 :由于信元错误导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770095 由于未指定的协议错误导致的周期性RAU失败次数-GSM 


计数器描述 :由于未指定的协议错误导致用户（Gb口接入）周期性RAU失败次数。 


测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 


采集方式 :CC 


# C405770096 SGSN内IMSI附着的联合路由更新请求次数-GSM 


计数器描述 :IMSI附着用户（Gb口接入）在SGSN内的联合路由更新请求次数。 


测量触发点 :SGSN收到“Routing Area Update Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为combined
RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。 


采集方式 :CC 


# C405770097 SGSN内IMSI附着的联合路由更新成功次数-GSM 


计数器描述 :IMSI附着用户（Gb口接入）在SGSN内的联合路由更新成功次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的联合路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN向MS发送“Routing Area Update Accept”消息，当GPRS路由更新成功并且Gs口位置更新成功时统计。 


采集方式 :CC 


# C405770098 由于非法用户导致的SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于非法用户导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 


采集方式 :CC 


# C405770099 由于非法设备导致的SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于非法设备导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 


采集方式 :CC 


# C405770100 由于GPRS服务不允许导致的SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务不允许导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS services
not allowed”时统计。 


采集方式 :CC 


# C405770101 由于GPRS服务和非GPRS服务不允许导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务和非GPRS服务不允许导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770102 由于网络无法获取MS ID导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于网络无法获取MS ID导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS identity
cannot be derived by the network”时统计。 


采集方式 :CC 


# C405770103 由于用户隐式分离导致的SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于用户隐式分离导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 


采集方式 :CC 


# C405770104 由于PLMN不允许导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于PLMN不允许导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 


采集方式 :CC 


# C405770105 由于位置区不允许导致的SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于位置区不允许导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 


采集方式 :CC 


# C405770106 由于漫游位置区不允许导致的SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于漫游位置区不允许导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 


采集方式 :CC 


# C405770107 由于GPRS服务在本PLMN不允许导致的SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务在本PLMN不允许导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS services
not allowed in this PLMN”时统计。 


采集方式 :CC 


# C405770108 由于本位置区没有合适的小区导致的SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于本位置区没有合适的小区导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No Suitable
Cells In Location Area”时统计。 


采集方式 :CC 


# C405770109 由于网络侧失败导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于网络侧失败导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 


采集方式 :CC 


# C405770110 由于必选项错误导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于必选项错误导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 


采集方式 :CC 


# C405770111 由于消息类型不存在导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于消息类型不存在导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770112 由于消息类型和协议不匹配导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于消息类型和协议不匹配导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 


采集方式 :CC 


# C405770113 由于信元错误导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于信元错误导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770114 由于未指定的协议错误导致SGSN内IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于未指定的协议错误导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 


采集方式 :CC 


# C405770115 SGSN间IMSI附着的联合路由更新请求次数-GSM 


计数器描述 :IMSI附着用户（Gb口接入）在SGSN间的联合路由更新请求次数。 


测量触发点 :SGSN收到“Routing Area Update Request”消息，其中旧RA不属于本SGSN，路由更新类型为combined
RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。 


采集方式 :CC 


# C405770116 SGSN间IMSI附着的联合路由更新成功次数-GSM 


计数器描述 :IMSI附着用户（Gb口接入）在SGSN间的联合路由更新成功次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的联合路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN向MS发送“Routing Area Update Accept”消息，当GPRS路由更新成功并且Gs口位置更新成功时统计。下图中的“A”表示了该测量项在流程中的触发位置。 



采集方式 :CC 


# C405770117 由于非法用户导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于非法用户导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 


采集方式 :CC 


# C405770118 由于非法设备导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于非法设备导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 


采集方式 :CC 


# C405770119 由于GPRS服务不允许导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务不允许导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS services
not allowed”时统计。 


采集方式 :CC 


# C405770120 由于GPRS服务和非GPRS服务不允许导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务和非GPRS服务不允许导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 


采集方式 :CC 


# C405770121 由于网络无法获取MS ID导致SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于网络无法获取MS ID导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS identity
cannot be derived by the network”时统计。 


采集方式 :CC 


# C405770122 由于用户隐式分离导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于用户隐式分离导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 


采集方式 :CC 


# C405770123 由于PLMN不允许导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于PLMN不允许导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 


采集方式 :CC 


# C405770124 由于位置区不允许导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于位置区不允许导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 


采集方式 :CC 


# C405770125 由于漫游位置区不允许导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于漫游位置区不允许导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 


采集方式 :CC 


# C405770126 由于GPRS服务在本PLMN不允许导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于GPRS服务在本PLMN不允许导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS services
not allowed in this PLMN”时统计。 


采集方式 :CC 


# C405770127 由于本位置区没有合适的小区导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于本位置区没有合适的小区导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No Suitable
Cells In Location Area”时统计。 


采集方式 :CC 


# C405770128 由于网络侧失败导致SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于网络侧失败导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 


采集方式 :CC 


# C405770129 由于必选项错误导致SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于必选项错误导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 


采集方式 :CC 


# C405770130 由于消息类型不存在导致SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于消息类型不存在导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770131 由于消息类型和协议不匹配导致SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于消息类型和协议不匹配导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 


采集方式 :CC 


# C405770132 由于信元错误导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于信元错误导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 


采集方式 :CC 


# C405770133 由于未指定的协议错误导致的SGSN间IMSI附着的联合路由更新失败次数-GSM 


计数器描述 :由于未指定的协议错误导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 


测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 


采集方式 :CC 


# C405770134 RAU更新总时长(毫秒)-GSM 
计数器描述 :从SGSN收到用户（Gb口接入）RAU请求到SGSN下发RAU接受的总时间长度。 
测量触发点 :用户通过Gb口进行RA更新，RAU成功时统计。 
采集方式 :CC 
# C405770137 局间的RAU请求次数(老局为MME)-GSM 
计数器描述 :MS（Gb口接入）发起的局间RAU请求次数（老局为MME）。 
测量触发点 :SGSN从MS（Gb口接入）收到“Routing Area Update
Request”消息，老局为MME，路由更新类型为GPRS路由更新，更新成功或失败后统计。 
采集方式 :CC 
# C405770138 局间的RAU请求成功次数(老局为MME)-GSM 
计数器描述 :MS（Gb口接入）发起的局间RAU请求成功次数（老局为MME）。 
测量触发点 :对于MS（Gb口接入）的局间GPRS路由更新请求（老局为MME），SGSN向MS发送“Routing
Area Update Accept”消息后统计。 
采集方式 :CC 
