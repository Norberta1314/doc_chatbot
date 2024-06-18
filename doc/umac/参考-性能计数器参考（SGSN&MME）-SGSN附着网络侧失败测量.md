

统计区分HLR，SGSN，无线等原因造成附着失败的次数时需要创建。建议颗粒为15分钟。 


# C405500003 SGSN内部失败导致的GPRS附着失败次数-UMTS 


## 计数器描述 
SGSN内部失败导致用户（Iu口接入）GPRS附着失败的次数。 


## 测量触发点 
对于用户（Iu口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，由于SGSN内部原因引起的失败时统计。 


## 采集方式 
CC 


# C405500004 SGSN内部失败导致的GPRS附着失败次数-GSM 


## 计数器描述 
SGSN内部失败导致用户（Gb口接入）GPRS附着失败的次数。 


## 测量触发点 
对于用户（Gb口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，由于SGSN内部原因引起的失败时统计。 


## 采集方式 
CC 


# C405500005 HLR失败导致的GPRS附着失败次数-UMTS 


## 计数器描述 
HLR失败导致用户（Iu口接入）GPRS附着失败的次数。 


## 测量触发点 
对于用户（Iu口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“获取鉴权向量”、“MAP错误”、“更新HLR超时”或“HLR未知”时统计。 


## 采集方式 
CC 


# C405500006 HLR失败导致的GPRS附着失败次数-GSM 


## 计数器描述 
HLR失败导致用户（Gb口接入）GPRS附着失败的次数。 


## 测量触发点 
对于用户（Gb口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“获取鉴权向量”、“MAP错误”、“更新HLR超时”或“HLR未知”时统计。 


## 采集方式 
CC 


# C405500007 无线侧失败导致的GPRS附着失败次数-UMTS 


## 计数器描述 
RAN失败导致用户（Iu口接入）GPRS附着失败的次数。 


## 测量触发点 
对于用户（Iu口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“鉴权”或“安全模式流程超时”时统计。 


## 采集方式 
CC 


# C405500008 无线侧失败导致的GPRS附着失败次数-GSM 


## 计数器描述 
RAN失败导致用户（Gb口接入）GPRS附着失败的次数。 


## 测量触发点 
对于用户（Gb口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“鉴权”或“安全模式流程超时”时统计。 


## 采集方式 
CC 


# C405500009 CAMEL失败导致的GPRS附着失败次数-UMTS 


## 计数器描述 
CAMEL失败导致用户（Iu口接入）GPRS附着失败的次数。


## 测量触发点 
对于用户（Iu口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“CAMEL检查释放”或“CAMEL检查超时”时统计。 


## 采集方式 
CC 


# C405500010 CAMEL失败导致的GPRS附着失败次数-GSM 


## 计数器描述 
CAMEL失败导致用户（Gb口接入）GPRS附着失败的次数。


## 测量触发点 
对于用户（Gb口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“CAMEL检查释放”或“CAMEL检查超时”时统计。 


## 采集方式 
CC 


# C405500011 SGSN内部失败导致的联合附着失败次数-UMTS 


## 计数器描述 
SGSN内部失败导致用户（Iu口接入）联合附着失败的次数。 


## 测量触发点 
对于用户（Iu口接入）的联合附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，由于SGSN内部原因引起的失败时统计。 


## 采集方式 
CC 


# C405500012 SGSN内部失败导致的联合附着失败次数-GSM 


## 计数器描述 
SGSN内部失败导致用户（Gb口接入）联合附着失败的次数。 


## 测量触发点 
对于用户（Gb口接入）的联合附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，由于SGSN内部原因引起的失败时统计。 


## 采集方式 
CC 


# C405500013 HLR失败导致的联合附着失败次数-UMTS 


## 计数器描述 
HLR失败导致用户（Iu口接入）联合附着失败次数。 


## 测量触发点 
对于用户（Iu口接入）的联合附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“获取鉴权向量”、“MAP错误”、“更新HLR超时”或“HLR未知”时统计。 


## 采集方式 
CC 


# C405500014 HLR失败导致的联合附着失败次数-GSM 


## 计数器描述 
HLR失败导致用户（Gb口接入）联合附着失败次数。 


## 测量触发点 
对于用户（Gb口接入）的联合附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“获取鉴权向量”、“MAP错误”、“更新HLR超时”或“HLR未知”时统计。 


## 采集方式 
CC 


# C405500015 无线侧失败导致的联合附着失败次数-UMTS 


## 计数器描述 
RAN失败导致用户（Iu口接入）联合附着失败的次数。


## 测量触发点 
对于用户（Iu口接入）的联合附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“鉴权”或“安全模式流程超时”时统计。 


## 采集方式 
CC 


# C405500016 无线侧失败导致的联合附着失败次数-GSM 


## 计数器描述 
RAN失败导致用户（Gb口接入）联合附着失败的次数。


## 测量触发点 
对于用户（Gb口接入）的联合附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“鉴权”或“安全模式流程超时”时统计。 


## 采集方式 
CC 


# C405500017 CAMEL失败导致的联合附着失败次数-UMTS 


## 计数器描述 
CAMEL失败导致用户（Iu口接入）联合附着失败的次数。 


## 测量触发点 
对于用户（Iu口接入）的联合附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“CAMEL检查释放”时统计。 


## 采集方式 
CC 


# C405500018 CAMEL失败导致的联合附着失败次数-GSM 


## 计数器描述 
CAMEL失败导致用户（Gb口接入）联合附着失败的次数。 


## 测量触发点 
对于用户（Gb口接入）的联合附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“CAMEL检查释放”时统计。 


## 采集方式 
CC 


# C405500019 SGSN内部失败导致的已IMSI附着的GPRS附着失败次数-UMTS 


## 计数器描述 
SGSN内部失败导致已IMSI附着的用户（Iu口接入）GPRS附着失败的次数。 


## 测量触发点 
对于已IMSI附着的用户（Iu口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，由于SGSN内部原因引起的失败时统计。 


## 采集方式 
CC 


# C405500020 SGSN内部失败导致的已IMSI附着的GPRS附着失败次数-GSM 


## 计数器描述 
SGSN内部失败导致已IMSI附着的用户（Gb口接入）GPRS附着失败的次数。 


## 测量触发点 
对于已IMSI附着的用户（Gb口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，由于SGSN内部原因引起的失败时统计。 


## 采集方式 
CC 


# C405500021 HLR失败导致的已IMSI附着的GPRS附着失败次数-UMTS 


## 计数器描述 
HLR失败导致已IMSI附着的用户（Iu口接入）GPRS附着失败的次数。 


## 测量触发点 
对于已IMSI附着的用户（Iu口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“获取鉴权向量”、“MAP错误”、“更新HLR超时”或“HLR未知”时统计。 


## 采集方式 
CC 


# C405500022 HLR失败导致的已IMSI附着的GPRS附着失败次数-GSM 


## 计数器描述 
HLR失败导致已IMSI附着的用户（Gb口接入）GPRS附着失败的次数。 


## 测量触发点 
对于已IMSI附着的用户（Gb口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“获取鉴权向量”、“MAP错误”、“更新HLR超时”或“HLR未知”时统计。 


## 采集方式 
CC 


# C405500023 无线侧失败导致的已IMSI附着的GPRS附着失败次数-UMTS 


## 计数器描述 
RAN失败导致已IMSI附着的用户（Iu口接入）GPRS附着失败的次数。 


## 测量触发点 
对于已IMSI附着的用户（Iu口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“鉴权”或“安全模式流程超时”时统计。 


## 采集方式 
CC 


# C405500024 无线侧失败导致的已IMSI附着的GPRS附着失败次数-GSM 


## 计数器描述 
RAN失败导致已IMSI附着的用户（Gb口接入）GPRS附着失败的次数。 


## 测量触发点 
对于已IMSI附着的用户（Gb口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“鉴权”或“安全模式流程超时”时统计。 


## 采集方式 
CC 


# C405500025 CAMEL失败导致的已IMSI附着的GPRS附着失败次数-UMTS 


## 计数器描述 
CAMEL失败导致已IMSI附着的用户（Iu口接入）GPRS附着失败的次数。 


## 测量触发点 
对于已IMSI附着的用户（Iu口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“CAMEL检查释放”时统计。 


## 采集方式 
CC 


# C405500026 CAMEL失败导致的已IMSI附着的GPRS附着失败次数-GSM 


## 计数器描述 
CAMEL失败导致已IMSI附着的用户（Gb口接入）GPRS附着失败的次数。 


## 测量触发点 
对于已IMSI附着的用户（Gb口接入）的GPRS附着请求，SGSN下发附着拒绝消息（Attach
Reject），拒绝原因值为“Network failure”，SGSN细化失败原因为“CAMEL检查释放”时统计。 


## 采集方式 
CC 


