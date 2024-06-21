

统计网络原因造成路由更新失败的细分原因时需要创建，区分HLR，无线，SGSN等原因。建议颗粒为15分钟。 


# C405810001 SGSN局内RAU失败次数(RAN原因)-UMTS 
计数器描述 :由于RAN导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：安全模式无响应或拒绝）导致时统计。 
采集方式 :CC 
# C405810002 SGSN局内RAU失败次数(SGSN原因)-UMTS 
计数器描述 :由于SGSN导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810003 SGSN局内RAU失败次数(HLR原因)-UMTS 
计数器描述 :由于HLR导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应、HLR未知，MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810004 SGSN局内RAU失败次数(CAMEL原因)-UMTS 
计数器描述 :由于CAMEL导致用户（Iu口接入）在SGSN内的RAU失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810005 SGSN局内联合路由更新失败次数(RAN原因)-UMTS 
计数器描述 :由于RAN导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于无线侧原因（如：安全模式无响应或拒绝）导致时统计。 
采集方式 :CC 
# C405810006 SGSN局内联合路由更新失败次数(SGSN原因)-UMTS 
计数器描述 :由于SGSN导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810007 SGSN局内联合路由更新失败次数(HLR原因)-UMTS 
计数器描述 :由于HLR导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于HLR异常（例如：HLR无响应、HLR未知、MAP
Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810008 SGSN局内联合路由更新失败次数(CAMEL原因)-UMTS 
计数器描述 :由于CAMEL导致用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810009 SGSN局内IMSI附着的联合路由更新失败次数(RAN原因)-UMTS 
计数器描述 :由于RAN导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Iu口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：安全模式无响应或拒绝）导致时统计。 
采集方式 :CC 
# C405810010 SGSN局内IMSI附着的联合路由更新失败次数(SGSN原因)-UMTS 
计数器描述 :由于SGSN导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Iu口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810011 SGSN局内IMSI附着的联合路由更新失败次数(HLR原因)-UMTS 
计数器描述 :由于HLR导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Iu口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应、HLR未知、MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810012 SGSN局内IMSI附着的联合路由更新失败次数(CAMEL原因)-UMTS 
计数器描述 :由于CAMEL导致IMSI附着用户（Iu口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Iu口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810013 周期性路由更新失败次数(RAN原因)-UMTS 
计数器描述 :由于RAN导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：安全模式无响应或拒绝）导致时统计。 
采集方式 :CC 
# C405810014 周期性路由更新失败次数(SGSN原因)-UMTS 
计数器描述 :由于SGSN导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810015 周期性路由更新失败次数(HLR原因)-UMTS 
计数器描述 :由于HLR导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应、HLR未知、MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810016 周期性路由更新失败次数(CAMEL原因)-UMTS 
计数器描述 :由于CAMEL导致用户（Iu口接入）周期性路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810017 SGSN局内RAU失败次数(RAN原因)-GSM 
计数器描述 :由于RAN导致用户（Gb口接入）在SGSN内的RAU失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：加密无响应）导致时统计。 
采集方式 :CC 
# C405810018 SGSN局内RAU失败次数(SGSN原因)-GSM 
计数器描述 :由于SGSN导致用户（Gb口接入）在SGSN内的RAU失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810019 SGSN局内RAU失败次数(HLR原因)-GSM 
计数器描述 :由于HLR导致用户（Gb口接入）在SGSN内的RAU失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应，HLR未知，MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810020 SGSN局内RAU失败次数(CAMEL原因)-GSM 
计数器描述 :由于CAMEL导致用户（Gb口接入）在SGSN内的RAU失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810021 SGSN局内联合路由更新失败次数(RAN原因)-GSM 
计数器描述 :由于RAN导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于无线侧原因（如：加密无响应）导致时统计。 
采集方式 :CC 
# C405810022 SGSN局内联合路由更新失败次数(SGSN原因)-GSM 
计数器描述 :由于SGSN导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810023 SGSN局内联合路由更新失败次数(HLR原因)-GSM 
计数器描述 :由于HLR导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于HLR异常（例如：HLR无响应，HLR未知，MAP
Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810024 SGSN局内联合路由更新失败次数(CAMEL原因)-GSM 
计数器描述 :由于CAMEL导致用户（Gb口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810025 SGSN局内IMSI附着的联合路由更新失败次数(RAN原因)-GSM 
计数器描述 :由于RAN导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：加密无响应）导致时统计。 
采集方式 :CC 
# C405810026 SGSN局内IMSI附着的联合路由更新失败次数(SGSN原因)-GSM 
计数器描述 :由于SGSN导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810027 SGSN局内IMSI附着的联合路由更新失败次数(HLR原因)-GSM 
计数器描述 :由于HLR导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应，HLR未知，MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810028 SGSN局内IMSI附着的联合路由更新失败次数(CAMEL原因)-GSM 
计数器描述 :由于CAMEL导致IMSI附着用户（Gb口接入）在SGSN内的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN内的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810029 周期性路由更新失败次数(RAN原因)-GSM 
计数器描述 :由于RAN导致用户（Gb口接入）周期性路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：加密无响应）导致时统计。 
采集方式 :CC 
# C405810030 周期性路由更新失败次数(SGSN原因)-GSM 
计数器描述 :由于SGSN导致用户（Gb口接入）周期性路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810031 周期性路由更新失败次数(HLR原因)-GSM 
计数器描述 :由于HLR导致用户（Gb口接入）周期性路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应，HLR未知，MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810032 周期性路由更新失败次数(CAMEL原因)-GSM 
计数器描述 :由于CAMEL导致用户（Gb口接入）周期性路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN内的周期性路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810033 SGSN局间RAU失败次数(RAN原因)-UMTS 
计数器描述 :由于RAN导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：安全模式无响应或拒绝）导致时统计。 
采集方式 :CC 
# C405810034 SGSN局间RAU失败次数(SGSN原因)-UMTS 
计数器描述 :由于SGSN导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810035 SGSN局间RAU失败次数(HLR原因)-UMTS 
计数器描述 :由于HLR导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应，HLR未知，MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810036 SGSN局间RAU失败次数(CAMEL原因)-UMTS 
计数器描述 :由于CAMEL导致用户（Iu口接入）在SGSN间的RAU失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810037 SGSN局间联合路由更新失败次数(RAN原因)-UMTS 
计数器描述 :由于RAN导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于无线侧原因（如：安全模式无响应或拒绝）导致时统计。 
采集方式 :CC 
# C405810038 SGSN局间联合路由更新失败次数(SGSN原因)-UMTS 
计数器描述 :由于SGSN导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810039 SGSN局间联合路由更新失败次数(HLR原因)-UMTS 
计数器描述 :由于HLR导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于HLR异常（例如：HLR无响应，HLR未知，MAP
Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810040 SGSN局间联合路由更新失败次数(CAMEL原因)-UMTS 
计数器描述 :由于CAMEL导致用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于用户（Iu口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810041 SGSN局间IMSI附着的联合路由更新失败次数(RAN原因)-UMTS 
计数器描述 :由于RAN导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Iu口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：安全模式无响应或拒绝）导致时统计。 
采集方式 :CC 
# C405810042 SGSN局间IMSI附着的联合路由更新失败次数(SGSN原因)-UMTS 
计数器描述 :由于SGSN导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Iu口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810043 SGSN局间IMSI附着的联合路由更新失败次数(HLR原因)-UMTS 
计数器描述 :由于HLR导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Iu口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应、HLR未知、MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810044 SGSN局间IMSI附着的联合路由更新失败次数(CAMEL原因)-UMTS 
计数器描述 :由于CAMEL导致IMSI附着用户（Iu口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Iu口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810045 SGSN局间RAU失败次数(RAN原因)-GSM 
计数器描述 :由于RAN导致用户（Gb口接入）在SGSN间的RAU失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：加密无响应）导致时统计。 
采集方式 :CC 
# C405810046 SGSN局间RAU失败次数(SGSN原因)-GSM 
计数器描述 :由于SGSN导致用户（Gb口接入）在SGSN间的RAU失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810047 SGSN局间RAU失败次数(HLR原因)-GSM 
计数器描述 :由于HLR导致用户（Gb口接入）在SGSN间的RAU失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应、HLR未知、MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810048 SGSN局间RAU失败次数(CAMEL原因)-GSM 
计数器描述 :由于CAMEL导致用户（Gb口接入）在SGSN间的RAU失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810049 SGSN局间联合路由更新失败次数(RAN原因)-GSM 
计数器描述 :由于RAN导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于无线侧原因（如：加密无响应）导致时统计。 
采集方式 :CC 
# C405810050 SGSN局间联合路由更新失败次数(SGSN原因)-GSM 
计数器描述 :由于SGSN导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810051 SGSN局间联合路由更新失败次数(HLR原因)-GSM 
计数器描述 :由于HLR导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于HLR异常（例如：HLR无响应、HLR未知、MAP
Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810052 SGSN局间联合路由更新失败次数(CAMEL原因)-GSM 
计数器描述 :由于CAMEL导致用户（Gb口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于用户（Gb口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810053 SGSN局间IMSI附着的联合路由更新失败次数(RAN原因)-GSM 
计数器描述 :由于RAN导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于无线侧原因（如：加密无响应）导致时统计。 
采集方式 :CC 
# C405810054 SGSN局间IMSI附着的联合路由更新失败次数(SGSN原因)-GSM 
计数器描述 :由于SGSN导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于SGSN内部原因（例如：申请不到资源（数据区、上下文或其他）、内部读写错、内部通讯异常等）导致时统计。 
采集方式 :CC 
# C405810055 SGSN局间IMSI附着的联合路由更新失败次数(HLR原因)-GSM 
计数器描述 :由于HLR导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于HLR异常（例如：HLR无响应、HLR未知、MAP Error或获取鉴权向量失败等）导致时统计。 
采集方式 :CC 
# C405810056 SGSN局间IMSI附着的联合路由更新失败次数(CAMEL原因)-GSM 
计数器描述 :由于CAMEL导致IMSI附着用户（Gb口接入）在SGSN间的联合路由更新失败次数。 
测量触发点 :对于IMSI附着用户（Gb口接入）在SGSN间的GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，拒绝原因值为“0x11：Network
failure”，失败是由于CAMEL（如：CAMEL检查释放、CAMEL无响应）导致时统计。 
采集方式 :CC 
# C405810057 SGSN局内RAU请求次数-UMTS 


计数器描述 :用户（Iu口接入）在SGSN局内发起RAU请求的次数。 


测量触发点 :SGSN从MS（Iu口接入）收到“Routing Area Update
Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为GPRS路由更新，路由更新成功或失败后统计。 


采集方式 :CC 


# C405810058 SGSN局内RAU成功次数-UMTS 


计数器描述 :用户（Iu口接入）在SGSN局内发起RAU请求成功的次数。 


测量触发点 :对于用户（Iu口接入）的SGSN局内GPRS路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405810059 SGSN局内RAU失败次数(UE原因)-UMTS 
计数器描述 :由于UE导致用户（Iu口接入）发起SGSN局内RAU失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局内GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810060 SGSN局内RAU失败次数(EIR原因)-UMTS 
计数器描述 :由于EIR导致用户（Iu口接入）发起SGSN局内RAU失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局内GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810061 SGSN局内联合路由更新请求次数-UMTS 


计数器描述 :用户（Iu口接入）在SGSN局内发起联合路由更新请求的次数。 


测量触发点 :SGSN从MS（Iu口接入）收到“Routing Area Update
Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为combined RA/LA updating。当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局内RAU请求次数。 


采集方式 :CC 


# C405810062 SGSN局内联合路由更新成功次数-UMTS 


计数器描述 :用户（Iu口接入）在SGSN局内发起联合路由更新成功的次数。 


测量触发点 :对于用户（Iu口接入）的SGSN局内联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息。当GPRS路由更新成功并且Gs口位置更新成功时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局内RAU成功次数。 


采集方式 :CC 


# C405810063 SGSN局内联合路由更新失败次数(UE原因)-UMTS 
计数器描述 :由于UE导致用户（Iu口接入）发起SGSN局内联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局内GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810064 SGSN局内联合路由更新失败次数(EIR原因)-UMTS 
计数器描述 :由于EIR导致用户（Iu口接入）发起SGSN局内联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局内GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810065 SGSN局内IMSI附着的联合路由更新请求次数-UMTS 


计数器描述 :已IMSI附着的用户（Iu口接入）在SGSN局内发起联合路由更新请求的次数。 


测量触发点 :SGSN从MS（Iu口接入）收到“Routing Area Update
Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为combined RA/LA updating with IMSI
attach。当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局内RAU请求次数。 


采集方式 :CC 


# C405810066 SGSN局内IMSI附着的联合路由更新成功次数-UMTS 


计数器描述 :已IMSI附着的用户（Iu口接入）在SGSN局内发起联合路由更新成功的次数。 


测量触发点 :对于用户（Iu口接入）的SGSN局内联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，路由更新类型为combined RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局内RAU成功次数。 


采集方式 :CC 


# C405810067 SGSN局内IMSI附着的联合路由更新失败次数(UE原因)-UMTS 
计数器描述 :由于UE导致已IMSI附着的用户（Iu口接入）发起SGSN局内联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局内GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810068 SGSN局内IMSI附着的联合路由更新失败次数(EIR原因)-UMTS 
计数器描述 :由于EIR导致已IMSI附着的用户（Iu口接入）发起SGSN局内联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局内GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810069 周期性路由更新请求次数-UMTS 


计数器描述 :用户（Iu口接入）发起周期性路由更新请求的次数。 


测量触发点 :SGSN从MS（Iu口接入）收到“Routing Area Update
Request”消息，路由更新类型为周期性路由更新，更新成功或失败后统计。 


采集方式 :CC 


# C405810070 周期性路由更新成功次数-UMTS 


计数器描述 :用户（Iu口接入）发起周期性路由更新成功的次数。 


测量触发点 :对于用户（Iu口接入）的SGSN内周期性路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405810071 周期性路由更新失败次数(UE原因)-UMTS 
计数器描述 :由于UE导致用户（Iu口接入）周期性路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的周期性路由更新请求，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810072 周期性路由更新失败次数(EIR原因)-UMTS 
计数器描述 :由于EIR导致用户（Iu口接入）周期性路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的周期性路由更新请求，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810073 SGSN局间RAU请求次数-UMTS 


计数器描述 :用户（Iu口接入）在SGSN局间发起RAU请求的次数。 


测量触发点 :SGSN从MS（Iu口接入）收到“Routing Area Update
Request”消息，其中旧RA不属于本SGSN，路由更新类型为GPRS路由更新，路由更新成功或失败后统计。 


采集方式 :CC 


# C405810074 SGSN局间RAU成功次数-UMTS 


计数器描述 :用户（Iu口接入）在SGSN局间发起RAU请求成功的次数。 


测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405810075 SGSN局间RAU失败次数(UE原因)-UMTS 
计数器描述 :由于UE导致用户（Iu口接入）发起SGSN局间RAU失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810076 SGSN局间RAU失败次数(EIR原因)-UMTS 
计数器描述 :由于EIR导致用户（Iu口接入）发起SGSN局间RAU失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810077 SGSN局间RAU失败次数(其他SGSN原因)-UMTS 
计数器描述 :由于其他SGSN导致用户（Iu口接入）发起SGSN局间RAU失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于其他SGSN导致时统计。 
采集方式 :CC 
# C405810078 SGSN局间联合路由更新请求次数-UMTS 


计数器描述 :用户（Iu口接入）在SGSN局间发起联合路由更新请求的次数。 


测量触发点 :SGSN从MS（Iu口接入）收到“Routing Area Update
Request”消息，其中旧RA不属于本SGSN，路由更新类型为combined RA/LA updating。当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局间RAU请求次数。 


采集方式 :CC 


# C405810079 SGSN局间联合路由更新成功次数-UMTS 


计数器描述 :用户（Iu口接入）在SGSN局间发起联合路由更新成功的次数。 


测量触发点 :对于用户（Iu口接入）的SGSN局间联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息。当GPRS路由更新成功并且Gs口位置更新成功时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局间RAU成功次数。 


采集方式 :CC 


# C405810080 SGSN局间联合路由更新失败次数(UE原因)-UMTS 
计数器描述 :由于UE导致用户（Iu口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810081 SGSN局间联合路由更新失败次数(EIR原因)-UMTS 
计数器描述 :由于EIR导致用户（Iu口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810082 SGSN局间联合路由更新失败次数(其他SGSN原因)-UMTS 
计数器描述 :由于其他SGSN导致用户（Iu口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于其他SGSN导致时统计。 
采集方式 :CC 
# C405810083 SGSN局间IMSI附着的联合路由更新请求次数-UMTS 


计数器描述 :已IMSI附着的用户（Iu口接入）在SGSN局间发起联合路由更新请求的次数。 


测量触发点 :SGSN从MS（Iu口接入）收到“Routing Area Update
Request”消息，其中旧RA不属于本SGSN，路由更新类型为combined RA/LA updating with IMSI
attach，当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局间RAU请求次数。 


采集方式 :CC 


# C405810084 SGSN局间IMSI附着的联合路由更新成功次数-UMTS 


计数器描述 :已IMSI附着的用户（Iu口接入）在SGSN局间发起联合路由更新成功的次数。 


测量触发点 :对于用户（Iu口接入）的SGSN局间联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，路由更新类型为combined RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局间RAU成功次数。 


采集方式 :CC 


# C405810085 SGSN局间IMSI附着的联合路由更新失败次数(UE原因)-UMTS 
计数器描述 :由于UE导致已IMSI附着的用户（Iu口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810086 SGSN局间IMSI附着的联合路由更新失败次数(EIR原因)-UMTS 
计数器描述 :由于EIR导致已IMSI附着的用户（Iu口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810087 SGSN局间IMSI附着的联合路由更新失败次数(其他SGSN原因)-UMTS 
计数器描述 :由于其他SGSN导致已IMSI附着的用户（Iu口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于其他SGSN导致时统计。 
采集方式 :CC 
# C405810088 SGSN局内RAU请求次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN局内发起RAU请求的次数。 


测量触发点 :SGSN从MS（Gb口接入）收到“Routing Area Update
Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为GPRS路由更新，路由更新成功或失败后统计。 


采集方式 :CC 


# C405810089 SGSN局内RAU成功次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN局内发起RAU请求成功的次数。 


测量触发点 :对于用户（Gb口接入）的SGSN局内GPRS路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405810090 SGSN局内RAU失败次数(UE原因)-GSM 
计数器描述 :由于UE导致用户（Gb口接入）发起SGSN局内RAU失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局内GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810091 SGSN局内RAU失败次数(EIR原因)-GSM 
计数器描述 :由于EIR导致用户（Gb口接入）发起SGSN局内RAU失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局内GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810092 SGSN局内联合路由更新请求次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN局内发起联合路由更新请求的次数。 


测量触发点 :SGSN从MS（Gb口接入）收到“Routing Area Update
Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为combined RA/LA updating。当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局内RAU请求次数。 


采集方式 :CC 


# C405810093 SGSN局内联合路由更新成功次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN局内发起联合路由更新成功的次数。 


测量触发点 :对于用户（Gb口接入）的SGSN局内联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息。当GPRS路由更新成功并且Gs口位置更新成功时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局内RAU成功次数。 


采集方式 :CC 


# C405810094 SGSN局内联合路由更新失败次数(UE原因)-GSM 
计数器描述 :由于UE导致用户（Gb口接入）发起SGSN局内联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局内GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810095 SGSN局内联合路由更新失败次数(EIR原因)-GSM 
计数器描述 :由于EIR导致用户（Gb口接入）发起SGSN局内联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局内GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810096 SGSN局内IMSI附着的联合路由更新请求次数-GSM 


计数器描述 :已IMSI附着的用户（Gb口接入）在SGSN局内发起联合路由更新请求的次数。 


测量触发点 :SGSN从MS（Gb口接入）收到“Routing Area Update
Request”消息，其中旧RA与新RA都属于本SGSN，路由更新类型为combined RA/LA updating with IMSI
attach。当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局内RAU请求次数。 


采集方式 :CC 


# C405810097 SGSN局内IMSI附着的联合路由更新成功次数-GSM 


计数器描述 :已IMSI附着的用户（Gb口接入）在SGSN局内发起联合路由更新成功的次数。 


测量触发点 :对于用户（Gb口接入）的SGSN局内联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，路由更新类型为combined RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局内RAU成功次数。 


采集方式 :CC 


# C405810098 SGSN局内IMSI附着的联合路由更新失败次数(UE原因)-GSM 
计数器描述 :由于UE导致已IMSI附着的用户（Gb口接入）发起SGSN局内联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局内GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810099 SGSN局内IMSI附着的联合路由更新失败次数(EIR原因)-GSM 
计数器描述 :由于EIR导致已IMSI附着的用户（Gb口接入）发起SGSN局内联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局内GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810100 周期性路由更新请求次数-GSM 


计数器描述 :用户（Gb口接入）发起周期性路由更新请求的次数。 


测量触发点 :SGSN从MS（Gb口接入）收到“Routing Area Update
Request”消息，路由更新类型为周期性路由更新，更新成功或失败后统计。 


采集方式 :CC 


# C405810101 周期性路由更新成功次数-GSM 


计数器描述 :用户（Gb口接入）发起周期性路由更新成功的次数。 


测量触发点 :对于用户（Gb口接入）的SGSN内周期性路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405810102 周期性路由更新失败次数(UE原因)-GSM 
计数器描述 :由于UE导致用户（Gb口接入）周期性路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的周期性路由更新请求，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810103 周期性路由更新失败次数(EIR原因)-GSM 
计数器描述 :由于EIR导致用户（Gb口接入）周期性路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的周期性路由更新请求，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810104 SGSN局间RAU请求次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN局间发起RAU请求的次数。 


测量触发点 :SGSN从MS（Gb口接入）收到“Routing Area Update
Request”消息，其中旧RA不属于本SGSN，路由更新类型为GPRS路由更新，路由更新成功或失败后统计。 


采集方式 :CC 


# C405810105 SGSN局间RAU成功次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN局间发起RAU请求成功的次数。 


测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息后统计。 


采集方式 :CC 


# C405810106 SGSN局间RAU失败次数(UE原因)-GSM 
计数器描述 :由于UE导致用户（Gb口接入）发起SGSN局间RAU失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810107 SGSN局间RAU失败次数(EIR原因)-GSM 
计数器描述 :由于EIR导致用户（Gb口接入）发起SGSN局间RAU失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810108 SGSN局间RAU失败次数(其他SGSN原因)-GSM 
计数器描述 :由于其他SGSN导致用户（Gb口接入）发起SGSN局间RAU失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于其他SGSN导致时统计。 
采集方式 :CC 
# C405810109 SGSN局间联合路由更新请求次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN局间发起联合路由更新请求的次数。 


测量触发点 :SGSN从MS（Gb口接入）收到“Routing Area Update
Request”消息，其中旧RA不属于本SGSN，路由更新类型为combined RA/LA updating。当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局间RAU请求次数。 


采集方式 :CC 


# C405810110 SGSN局间联合路由更新成功次数-GSM 


计数器描述 :用户（Gb口接入）在SGSN局间发起联合路由更新成功的次数。 


测量触发点 :对于用户（Gb口接入）的SGSN局间联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息。当GPRS路由更新成功并且Gs口位置更新成功时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局间RAU成功次数。 


采集方式 :CC 


# C405810111 SGSN局间联合路由更新失败次数(UE原因)-GSM 
计数器描述 :由于UE导致用户（Gb口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810112 SGSN局间联合路由更新失败次数(EIR原因)-GSM 
计数器描述 :由于EIR导致用户（Gb口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810113 SGSN局间联合路由更新失败次数(其他SGSN原因)-GSM 
计数器描述 :由于其他SGSN导致用户（Gb口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于其他SGSN导致时统计。 
采集方式 :CC 
# C405810114 SGSN局间IMSI附着的联合路由更新请求次数-GSM 


计数器描述 :已IMSI附着的用户（Gb口接入）在SGSN局间发起联合路由更新请求的次数。 


测量触发点 :SGSN从MS（Gb口接入）收到“Routing Area Update
Request”消息，其中旧RA不属于本SGSN，路由更新类型为combined RA/LA updating with IMSI
attach，当GPRS路由更新成功并且Gs口位置更新成功时或者联合路由更新失败时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局间RAU请求次数。 


采集方式 :CC 


# C405810115 SGSN局间IMSI附着的联合路由更新成功次数-GSM 


计数器描述 :已IMSI附着的用户（Gb口接入）在SGSN局间发起联合路由更新成功的次数。 


测量触发点 :对于用户（Gb口接入）的SGSN局间联合路由更新请求，SGSN向MS发送“Routing
Area Update Accept”消息，路由更新类型为combined RA/LA updating with IMSI attach，当GPRS路由更新成功并且Gs口位置更新成功时统计。当GPRS路由更新成功但Gs口位置更新不成功时，不统计到本计数器，统计到SGSN局间RAU成功次数。 


采集方式 :CC 


# C405810116 SGSN局间IMSI附着的联合路由更新失败次数(UE原因)-GSM 
计数器描述 :由于UE导致已IMSI附着的用户（Gb口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于UE导致时统计。 
采集方式 :CC 
# C405810117 SGSN局间IMSI附着的联合路由更新失败次数(EIR原因)-GSM 
计数器描述 :由于EIR导致已IMSI附着的用户（Gb口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于EIR导致时统计。 
采集方式 :CC 
# C405810118 SGSN局间IMSI附着的联合路由更新失败次数(其他SGSN原因)-GSM 
计数器描述 :由于其他SGSN导致已IMSI附着的用户（Gb口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于其他SGSN导致时统计。 
采集方式 :CC 
# C405810119 SGSN局间RAU失败次数(DNS原因)-UMTS 
计数器描述 :由于DNS导致用户（Iu口接入）发起SGSN局间RAU失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于DNS导致时统计。 
采集方式 :CC 
# C405810120 SGSN局间联合路由更新失败次数(DNS原因)-UMTS 
计数器描述 :由于DNS导致用户（Iu口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于DNS导致时统计。 
采集方式 :CC 
# C405810121 SGSN局间IMSI附着的联合路由更新失败次数(DNS原因)-UMTS 
计数器描述 :由于DNS导致已IMSI附着的用户（Iu口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Iu口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于DNS导致时统计。 
采集方式 :CC 
# C405810122 SGSN局间RAU失败次数(DNS原因)-GSM 
计数器描述 :由于DNS导致用户（Gb口接入）发起SGSN局间RAU失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，SGSN下发路由更新拒绝消息，失败是由于DNS导致时统计。 
采集方式 :CC 
# C405810123 SGSN局间联合路由更新失败次数(DNS原因)-GSM 
计数器描述 :由于DNS导致用户（Gb口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating，SGSN下发路由更新拒绝消息，失败是由于DNS导致时统计。 
采集方式 :CC 
# C405810124 SGSN局间IMSI附着的联合路由更新失败次数(DNS原因)-GSM 
计数器描述 :由于DNS导致已IMSI附着的用户（Gb口接入）发起SGSN局间联合路由更新失败的次数。 
测量触发点 :对于用户（Gb口接入）的SGSN局间GPRS路由更新请求，路由更新类型为combined
RA/LA updating with IMSI attach，SGSN下发路由更新拒绝消息，失败是由于DNS导致时统计。 
采集方式 :CC 
