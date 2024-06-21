
分路由区统计UMTS的RAU流程消息时需要创建。建议颗粒为15分钟。 
# C405320003 SGSN内的RAU请求次数-UMTS 

计数器描述 : 
用户（Iu口接入）在SGSN内的RAU请求次数。
测量触发点 : 
SGSN收到“Routing Area Update Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为GPRS路由更新时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320004 SGSN内的RAU成功次数-UMTS 

计数器描述 : 
用户（Iu口接入）在SGSN内的RAU成功次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320005 SGSN内的联合路由更新请求次数-UMTS 

计数器描述 : 
用户（Iu口接入）在SGSN内的联合路由更新请求次数。 
测量触发点 : 
SGSN收到“Routing Area Update Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为combined
RA/LA updating，当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。 
采集方式 : 
CC 
# C405320006 SGSN内的联合路由更新成功次数-UMTS 

计数器描述 : 
用户（Iu口接入）在SGSN内的联合路由更新成功次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，当GPRS路由更新成功并且Gs口位置更新成功时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320007 SGSN间的RAU请求次数-UMTS 

计数器描述 : 
用户（Iu口接入）在SGSN间的RAU请求次数。 
测量触发点 : 
SGSN收到“Routing Area Update Request”消息，其中旧RA不属于本SGSN，路由更新类型为GPRS路由更新时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320008 SGSN间的RAU成功次数-UMTS 

计数器描述 : 
用户（Iu口接入）在SGSN间的RAU成功次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320009 SGSN间的联合路由更新请求次数-UMTS 

计数器描述 : 
用户（Iu口接入）在SGSN间的联合路由更新请求次数。 
测量触发点 : 
SGSN收到“Routing Area Update Request”消息，其中旧RA不属于本SGSN，路由更新类型为combined
RA/LA updating，当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320010 SGSN间的联合路由更新成功次数-UMTS 

计数器描述 : 
用户（Iu口接入）在SGSN间的联合路由更新成功次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，当GPRS路由更新成功并且Gs口位置更新成功时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320011 由于非法用户导致的SGSN内的RAU失败次数-UMTS 

计数器描述 : 
由于非法用户导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 
采集方式 : 
CC 
# C405320012 由于位置区不允许导致的SGSN内的RAU失败次数-UMTS 

计数器描述 : 
由于位置区不允许导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 
采集方式 : 
CC 
# C405320013 由于漫游位置区不允许导致的SGSN内的RAU失败次数-UMTS 

计数器描述 : 
由于漫游位置区不允许导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 
采集方式 : 
CC 
# C405320014 由于非法设备导致的SGSN内的RAU失败次数-UMTS 

计数器描述 : 
由于非法设备导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 
采集方式 : 
CC 
# C405320015 由于GPRS服务不允许导致的SGSN内的RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务不允许导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS
services not allowed”时统计。 
采集方式 : 
CC 
# C405320016 由于用户隐式分离导致的SGSN内的RAU失败次数-UMTS 

计数器描述 : 
由于用户隐式分离导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 
采集方式 : 
CC 
# C405320017 由于GPRS服务在本PLMN不允许导致的SGSN内的RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务在本PLMN不允许导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS
services not allowed in this PLMN”时统计。 
采集方式 : 
CC 
# C405320018 由于本位置区没有合适的小区导致的SGSN内的RAU失败次数-UMTS 

计数器描述 : 
由于本位置区没有合适的小区导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No
Suitable Cells In Location Area”时统计。 
采集方式 : 
CC 
# C405320019 由于非法用户导致的SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于非法用户导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal MS”或“0x2：IMSI unknown
in HLR”时统计。 
采集方式 : 
CC 
# C405320020 由于位置区不允许导致的SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于位置区不允许导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location Area not allowed”时统计。 
采集方式 : 
CC 
# C405320021 由于漫游位置区不允许导致的SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于漫游位置区不允许导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming not allowed in this
location area”时统计。 
采集方式 : 
CC 
# C405320022 由于非法设备导致的SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于非法设备导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal ME”时统计。 
采集方式 : 
CC 
# C405320023 由于GPRS服务不允许导致的SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务不允许导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320024 由于用户隐式分离导致的SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于用户隐式分离导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly detached”时统计。 
采集方式 : 
CC 
# C405320025 由于GPRS服务在本PLMN不允许导致的SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务在本PLMN不允许导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS services not allowed
in this PLMN”时统计。 
采集方式 : 
CC 
# C405320026 由于本位置区没有合适的小区导致的SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于本位置区没有合适的小区导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No Suitable Cells In Location
Area”时统计。 
采集方式 : 
CC 
# C405320027 由于非法用户导致的SGSN间的RAU失败次数-UMTS 

计数器描述 : 
由于非法用户导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，“拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 
采集方式 : 
CC 
# C405320028 由于位置区不允许导致的SGSN间的RAU失败次数-UMTS 

计数器描述 : 
由于位置区不允许导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 
采集方式 : 
CC 
# C405320029 由于漫游位置区不允许导致的SGSN间的RAU失败次数-UMTS 

计数器描述 : 
由于漫游位置区不允许导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 
采集方式 : 
CC 
# C405320030 由于非法设备导致的SGSN间的RAU失败次数-UMTS 

计数器描述 : 
由于非法设备导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 
采集方式 : 
CC 
# C405320031 由于GPRS服务不允许导致的SGSN间的RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务不允许导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS
services not allowed”时统计。 
采集方式 : 
CC 
# C405320032 由于用户隐式分离导致的SGSN间的RAU失败次数-UMTS 

计数器描述 : 
由于用户隐式分离导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 
采集方式 : 
CC 
# C405320033 由于GPRS服务在本PLMN不允许导致的SGSN间的RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务在本PLMN不允许导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS
services not allowed in this PLMN”时统计。 
采集方式 : 
CC 
# C405320034 由于本位置区没有合适的小区导致的SGSN间的RAU失败次数-UMTS 

计数器描述 : 
由于本位置区没有合适的小区导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No
Suitable Cells In Location Area”时统计。 
采集方式 : 
CC 
# C405320035 由于非法用户导致的SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于非法用户导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal MS”或“0x2：IMSI unknown
in HLR”时统计。 
采集方式 : 
CC 
# C405320036 由于位置区不允许导致的SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于位置区不允许导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location Area not allowed”时统计。 
采集方式 : 
CC 
# C405320037 由于漫游位置区不允许导致的SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于漫游位置区不允许导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming not allowed in this
location area”时统计。 
采集方式 : 
CC 
# C405320038 由于非法设备导致的SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于非法设备导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal ME”时统计。 
采集方式 : 
CC 
# C405320039 由于GPRS服务不允许导致的SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务不允许导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320040 由于用户隐式分离导致的SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于用户隐式分离导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly detached”时统计。 
采集方式 : 
CC 
# C405320041 由于GPRS服务在本PLMN不允许导致的SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务在本PLMN不允许导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS services not allowed
in this PLMN”时统计。 
采集方式 : 
CC 
# C405320042 由于本位置区没有合适的小区导致的SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于本位置区没有合适的小区导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No Suitable Cells In Location
Area”时统计。 
采集方式 : 
CC 
# C405320043 由于GPRS服务和非GPRS服务不允许导致的SGSN内RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务和非GPRS服务不允许导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320044 由于PLMN不允许导致的SGSN内RAU失败次数-UMTS 

计数器描述 : 
由于PLMN不允许导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 
采集方式 : 
CC 
# C405320045 由于信元错误导致的SGSN内RAU失败次数-UMTS 

计数器描述 : 
由于信元错误导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320046 由于未指定的协议错误导致的SGSN内RAU失败次数-UMTS 

计数器描述 : 
由于未指定的协议错误导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 
采集方式 : 
CC 
# C405320047 由于GPRS服务和非GPRS服务不允许导致的SGSN间RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务和非GPRS服务不允许导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320048 由于PLMN不允许导致的SGSN间RAU失败次数-UMTS 

计数器描述 : 
由于PLMN不允许导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 
采集方式 : 
CC 
# C405320049 由于信元错误导致的SGSN间RAU失败次数-UMTS 

计数器描述 : 
由于信元错误导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320050 由于未指定的协议错误导致的SGSN间RAU失败次数-UMTS 

计数器描述 : 
由于未指定的协议错误导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 
采集方式 : 
CC 
# C405320051 周期性路由更新请求次数-UMTS 

计数器描述 : 
用户（Iu口接入）周期性路由更新请求次数。 
测量触发点 : 
SGSN收到“Routing Area Update Request”消息，路由更新类型为周期性路由更新时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320052 周期性路由更新成功次数-UMTS 

计数器描述 : 
用户（Iu口接入）周期性路由更新成功次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320053 由于非法用户导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于非法用户导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 
采集方式 : 
CC 
# C405320054 由于位置区不允许导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于位置区不允许导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 
采集方式 : 
CC 
# C405320055 由于漫游位置区不允许导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于漫游位置区不允许导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 
采集方式 : 
CC 
# C405320056 由于非法设备导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于非法设备导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 
采集方式 : 
CC 
# C405320057 由于GPRS服务不允许导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务不允许导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“0x7：GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320058 由于用户隐式分离导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于用户隐式分离导致用户（Iu口接入）周期性RAU失败次数 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 
采集方式 : 
CC 
# C405320059 由于GPRS服务在本PLMN不允许导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务在本PLMN不允许导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS
services not allowed in this PLMN”时统计。 
采集方式 : 
CC 
# C405320060 由于本位置区没有合适的小区导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于本位置区没有合适的小区导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No
Suitable Cells In Location Area”时统计。 
采集方式 : 
CC 
# C405320061 由于GPRS服务和非GPRS服务不允许导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于GPRS服务和非GPRS服务不允许导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320062 由于PLMN不允许导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于PLMN不允许导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 
采集方式 : 
CC 
# C405320063 由于信元错误导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于信元错误导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320064 由于未指定的协议错误导致的周期性RAU失败次数-UMTS 

计数器描述 : 
由于未指定的协议错误导致用户（Iu口接入）周期性RAU失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol
error, unspecified”时统计。 
采集方式 : 
CC 
# C405320065 由于网络侧失败导致SGSN内的路由更新失败次数-UMTS 

计数器描述 : 
由于网络侧失败导致用户（Iu口接入）在SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 
采集方式 : 
CC 
# C405320066 由于网络侧失败导致SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于网络侧失败导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”时统计。 
采集方式 : 
CC 
# C405320067 由于网络侧失败导致周期性路由更新失败次数-UMTS 

计数器描述 : 
由于网络侧失败导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 
采集方式 : 
CC 
# C405320068 由于网络侧失败导致SGSN间的路由更新失败次数-UMTS 

计数器描述 : 
由于网络侧失败导致用户（Iu口接入）在SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 
采集方式 : 
CC 
# C405320069 由于网络侧失败导致SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于网络侧失败导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”时统计。 
采集方式 : 
CC 
# C405320070 由于消息类型不存在导致SGSN内的路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型不存在导致用户（Iu口接入）在SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320071 由于消息类型不存在导致SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型不存在导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message type non-existent
or not implemented”时统计。 
采集方式 : 
CC 
# C405320072 由于消息类型不存在导致周期性路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型不存在导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320073 由于消息类型不存在导致SGSN间的路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型不存在导致用户（Iu口接入）在SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320074 由于消息类型不存在导致SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型不存在导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message type non-existent
or not implemented”时统计。 
采集方式 : 
CC 
# C405320075 由于必选项错误导致SGSN内的路由更新失败次数-UMTS 

计数器描述 : 
由于必选项错误导致用户（Iu口接入）在SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 
采集方式 : 
CC 
# C405320076 由于必选项错误导致SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于必选项错误导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid mandatory information”时统计。 
采集方式 : 
CC 
# C405320077 由于必选项错误导致周期性路由更新失败次数-UMTS 

计数器描述 : 
由于必选项错误导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 
采集方式 : 
CC 
# C405320078 由于必选项错误导致SGSN间的路由更新失败次数-UMTS 

计数器描述 : 
由于必选项错误导致用户（Iu口接入）在SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 
采集方式 : 
CC 
# C405320079 由于必选项错误导致SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于必选项错误导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid mandatory information”时统计。 
采集方式 : 
CC 
# C405320080 由于消息类型和协议不匹配导致SGSN内的路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型和协议不匹配导致用户（Iu口接入）在SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 
采集方式 : 
CC 
# C405320081 由于消息类型和协议不匹配导致SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型和协议不匹配导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message not compatible with
the protocol state”时统计。 
采集方式 : 
CC 
# C405320082 由于消息类型和协议不匹配导致周期性路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型和协议不匹配导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 
采集方式 : 
CC 
# C405320083 由于消息类型和协议不匹配导致SGSN间的路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型和协议不匹配导致用户（Iu口接入）在SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 
采集方式 : 
CC 
# C405320084 由于消息类型和协议不匹配导致SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型和协议不匹配导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message not compatible with
the protocol state”时统计。 
采集方式 : 
CC 
# C405320085 由于网络无法获取MS ID导致SGSN内的路由更新失败次数-UMTS 

计数器描述 : 
由于网络无法获取MS ID导致用户（Iu口接入）在SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS
identity cannot be derived by the network”时统计。 
采集方式 : 
CC 
# C405320086 由于网络无法获取MS ID导致SGSN内的联合路由更新失败次数-UMTS 

计数器描述 : 
由于网络无法获取MS ID导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS identity cannot be derived
by the network”时统计。 
采集方式 : 
CC 
# C405320087 由于网络无法获取MS ID导致周期性路由更新失败次数-UMTS 

计数器描述 : 
由于网络无法获取MS ID导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS
identity cannot be derived by the network”时统计。 
采集方式 : 
CC 
# C405320088 由于网络无法获取MS ID导致SGSN间的路由更新失败次数-UMTS 

计数器描述 : 
由于网络无法获取MS ID导致用户（Iu口接入）在SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS
identity cannot be derived by the network”时统计。 
采集方式 : 
CC 
# C405320089 由于网络无法获取MS ID导致SGSN间的联合路由更新失败次数-UMTS 

计数器描述 : 
由于网络无法获取MS ID导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS identity cannot be derived
by the network”时统计。 
采集方式 : 
CC 
# C405320090 SGSN内IMSI附着的联合路由更新请求次数-UMTS 

计数器描述 : 
IMSI附着用户（Iu口接入）在SGSN内的联合路由更新请求次数。 
测量触发点 : 
SGSN收到“Routing Area Update Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为combined
RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320091 SGSN内IMSI附着的联合路由更新成功次数-UMTS 

计数器描述 : 
IMSI附着用户（Iu口接入）在SGSN内的联合路由更新成功次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，路由更新类型为combined RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320092 由于非法用户导致的SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于非法用户导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 
采集方式 : 
CC 
# C405320093 由于位置区不允许导致的SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于位置区不允许导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 
采集方式 : 
CC 
# C405320094 由于漫游位置区不允许导致的SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于漫游位置区不允许导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 
采集方式 : 
CC 
# C405320095 由于非法设备导致的SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于非法设备导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 
采集方式 : 
CC 
# C405320096 由于GPRS服务不允许导致的SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务不允许导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS services
not allowed”时统计。 
采集方式 : 
CC 
# C405320097 由于用户隐式分离导致的SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于用户隐式分离导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 
采集方式 : 
CC 
# C405320098 由于GPRS服务在本PLMN不允许导致的SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务在本PLMN不允许导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS services
not allowed in this PLMN”时统计。 
采集方式 : 
CC 
# C405320099 由于本位置区没有合适的小区导致的SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于本位置区没有合适的小区导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No Suitable
Cells In Location Area”时统计。 
采集方式 : 
CC 
# C405320100 由于网络侧失败导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于网络侧失败导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 
采集方式 : 
CC 
# C405320101 由于消息类型不存在导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型不存在导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320102 由于必选项错误导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于必选项错误导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 
采集方式 : 
CC 
# C405320103 由于消息类型和协议不匹配导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型和协议不匹配导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 
采集方式 : 
CC 
# C405320104 由于网络无法获取MS ID导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于网络无法获取MS ID导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS identity
cannot be derived by the network”时统计。 
采集方式 : 
CC 
# C405320105 SGSN间IMSI附着的联合路由更新请求次数-UMTS 

计数器描述 : 
IMSI附着用户（Iu口接入）在SGSN间的联合路由更新请求次数。 
测量触发点 : 
SGSN收到“Routing Area Update Request”消息，其中旧RA不属于本SGSN，路由更新类型为combined
RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320106 SGSN间IMSI附着的联合路由更新成功次数-UMTS 

计数器描述 : 
IMSI附着用户（Iu口接入）在SGSN间的联合路由更新成功次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，路由更新类型为combined RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时统计。下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405320107 由于非法用户导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于非法用户导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x3：Illegal
MS”或“0x2：IMSI unknown in HLR”时统计。 
采集方式 : 
CC 
# C405320108 由于位置区不允许导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于位置区不允许导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xC：Location
Area not allowed”时统计。 
采集方式 : 
CC 
# C405320109 由于漫游位置区不允许导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于漫游位置区不允许导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xD：Roaming
not allowed in this location area”时统计。 
采集方式 : 
CC 
# C405320110 由于非法设备导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于非法设备导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x6：Illegal
ME”时统计。 
采集方式 : 
CC 
# C405320111 由于GPRS服务不允许导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务不允许导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x7：GPRS services
not allowed”时统计。 
采集方式 : 
CC 
# C405320112 由于用户隐式分离导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

## 计数器描 
由于用户隐式分离导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数述。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xA：Implicitly
detached”时统计。 
采集方式 : 
CC 
# C405320113 由于GPRS服务在本PLMN不允许导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务在本PLMN不允许导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xE：GPRS services
not allowed in this PLMN”时统计。 
采集方式 : 
CC 
# C405320114 由于本位置区没有合适的小区导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于本位置区没有合适的小区导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0xF：No Suitable
Cells In Location Area”时统计。 
采集方式 : 
CC 
# C405320115 由于网络侧失败导致SGSN间IMSI附着的联合路由更新失败次数-UMTS 

## 计数器 
由于网络侧失败导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”时统计。 
采集方式 : 
CC 
# C405320116 由于消息类型不存在导致SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型不存在导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x61：Message
type non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320117 由于必选项错误导致SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于必选项错误导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x60：Invalid
mandatory information”时统计。 
采集方式 : 
CC 
# C405320118 由于消息类型和协议不匹配导致SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于消息类型和协议不匹配导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x62：Message
not compatible with the protocol state”时统计。 
采集方式 : 
CC 
# C405320119 由于网络无法获取MS ID导致SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于网络无法获取MS ID导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x9：MS identity
cannot be derived by the network”时统计。 
采集方式 : 
CC 
# C405320120 由于GPRS服务和非GPRS服务不允许导致的SGSN内联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务和非GPRS服务不允许导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320121 由于PLMN不允许导致的SGSN内联合路由更新失败次数-UMTS 

计数器描述 : 
由于PLMN不允许导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN not allowed”时统计。 
采集方式 : 
CC 
# C405320122 由于信元错误导致的SGSN内联合路由更新失败次数-UMTS 

计数器描述 : 
由于信元错误导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“Information element non-existent
or not implemented”时统计。 
采集方式 : 
CC 
# C405320123 由于未指定的协议错误导致的SGSN内联合路由更新失败次数-UMTS 

计数器描述 : 
由于未指定的协议错误导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN内的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol error, unspecified”时统计。 
采集方式 : 
CC 
# C405320124 由于GPRS服务和非GPRS服务不允许导致的SGSN间联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务和非GPRS服务不允许导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320125 由于PLMN不允许导致的SGSN间联合路由更新失败次数-UMTS 

计数器描述 : 
由于PLMN不允许导致用户（Iu口接入）在SGSN间的联合路由更新失败次数 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN not allowed”时统计。 
采集方式 : 
CC 
# C405320126 由于信元错误导致的SGSN间联合路由更新失败次数-UMTS 

计数器描述 : 
由于信元错误导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“Information element non-existent
or not implemented”时统计。 
采集方式 : 
CC 
# C405320127 由于未指定的协议错误导致的SGSN间联合路由更新失败次数-UMTS 

计数器描述 : 
由于未指定的协议错误导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于用户（Iu口接入）在SGSN间的路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol error, unspecified”时统计。 
采集方式 : 
CC 
# C405320128 由于GPRS服务和非GPRS服务不允许导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务和非GPRS服务不允许导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的联合路由更新路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320129 由于PLMN不允许导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于PLMN不允许导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN
not allowed”时统计。 
采集方式 : 
CC 
# C405320130 由于信元错误导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于信元错误导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的联合路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320131 由于未指定的协议错误导致SGSN内IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于未指定的协议错误导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN内的联合路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol error,
unspecified”时统计。 
采集方式 : 
CC 
# C405320132 由于GPRS服务和非GPRS服务不允许导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于GPRS服务和非GPRS服务不允许导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的联合路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“GPRS
services and non-GPRS services not allowed”时统计。 
采集方式 : 
CC 
# C405320133 由于PLMN不允许导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

## 计数器 
由于PLMN不允许导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的联合路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“PLMN not allowed”时统计。 
采集方式 : 
CC 
# C405320134 由于信元错误导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

## 计数器 
由于信元错误导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的联合路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“Information
element non-existent or not implemented”时统计。 
采集方式 : 
CC 
# C405320135 由于未指定的协议错误导致的SGSN间IMSI附着的联合路由更新失败次数-UMTS 

计数器描述 : 
由于未指定的协议错误导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 : 
对于IMSI附着用户（Iu口接入）在SGSN间的联合路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“Protocol error,
unspecified”时统计。 
采集方式 : 
CC 
