# C405880003 由于非法用户导致的附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为非法用户）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为"Illegal MS"（cause值等于3）或失败原因为“IMSI unknown in HLR”（cause值等于2）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880004 由于位置区不允许导致附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为位置区不允许）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为位置区不允许（cause值等于12）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880005 由于漫游位置区不允许导致附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为漫游位置区不允许）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为漫游位置区不允许（cause值等于13）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880006 由于非法设备导致附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为非法设备）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为非法设备（cause值等于6）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880007 由于GPRS服务不允许导致GPRS附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为GPRS服务不允许。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为GPRS服务不允许（cause值等于7）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880008 由于GPRS服务在本PLMN不允许导致附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为GPRS服务在本PLMN不允许）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为GPRS服务在本PLMN不允许（cause值等于14）时统计。 
采集方式 : 
CC 
# C405880009 由于本位置区没有合适的小区导致附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为本位置区没有合适的小区）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为本位置区没有合适的小区（cause值等于15）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880010 由于网络无法获取MS ID导致的附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为网络无法获取MS
ID）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为网络侧无法获取MS ID（cause值等于9）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880011 由于GPRS服务和非GPRS服务不允许导致的附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为GPRS服务和非GPRS服务不允许）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为GPRS服务和非GPRS服务不允许（cause值等于8）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880012 由于PLMN不允许导致的附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值PLMN不允许）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为PLMN不允许（cause值等于11）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405880013 由于信元错误导致的附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为信元错误）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为信元错误（cause值等于0x63）时统计。 
采集方式 : 
CC 
# C405880014 由于未指定的协议错误导致的附着失败次数 

计数器描述 : 
某RNC上用户发起附着请求，附着失败（失败原因值为未指定的协议错误）的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（Attach Reject），其中GMM
cause指明失败原因为未指定的协议错误（cause值等于0x6F）时统计。 
采集方式 : 
CC 
# C405880015 由于非法用户导致的SGSN内的RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于非法用户导致的SGSN内的RAU失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Illegal MS”（cause值等于0x3）或“IMSI unknown
in HLR”（cause值等于0x2）时统计。 
采集方式 : 
CC 
# C405880016 由于位置区不允许导致的SGSN内的RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于位置区不允许导致的SGSN内的RAU失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Location Area not allowed”（cause值等于0xC）时统计。 
采集方式 : 
CC 
# C405880017 由于漫游位置区不允许导致的SGSN内的RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于漫游位置区不允许导致的SGSN内的RAU失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Roaming not allowed in this location area”（cause值等于0xD）时统计。 
采集方式 : 
CC 
# C405880018 由于非法设备导致的SGSN内的RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于非法设备导致的SGSN内的RAU失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Illegal ME”（cause值等于0x6）时统计。 
采集方式 : 
CC 
# C405880019 由于GPRS服务不允许导致的SGSN内的RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于GPRS服务不允许导致的SGSN内的RAU失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services not allowed”（cause值等于0x7）时统计。 
采集方式 : 
CC 
# C405880020 由于用户隐式分离导致的SGSN内的RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于用户隐式分离导致的SGSN内的RAU失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Implicitly detached”（cause值等于0xA）时统计。 
采集方式 : 
CC 
# C405880021 由于GPRS服务在本PLMN不允许导致的SGSN内的RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于GPRS服务在本PLMN不允许导致的SGSN内的RAU失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services not allowed in this PLMN”（cause值等于0xE）时统计。 
采集方式 : 
CC 
# C405880022 由于本位置区没有合适的小区导致的SGSN内的RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于本位置区没有合适的小区导致的SGSN内的RAU失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“No Suitable Cells In Location Area”（cause值等于0xF）时统计。 
采集方式 : 
CC 
# C405880023 由于消息类型不存在导致SGSN内的路由更新失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于消息类型不存在导致SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Message type non-existent or not implemented”（cause值等于0x61）时统计。 
采集方式 : 
CC 
# C405880024 由于必选项错误导致SGSN内的路由更新失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于必选项错误导致SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Invalid mandatory information”（cause值等于0x60）时统计。 
采集方式 : 
CC 
# C405880025 由于消息类型和协议不匹配导致SGSN内的路由更新失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于消息类型和协议不匹配导致SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Message not compatible with the protocol
state”（cause值等于0x62）时统计。 
采集方式 : 
CC 
# C405880026 由于网络无法获取MS ID导致SGSN内的路由更新失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于网络无法获取MS ID导致SGSN内的路由更新失败次数。 
测量触发点 : 
对于用户的SGSN内GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“MS identity cannot be derived by the network”（cause值等于0x9）时统计。 
采集方式 : 
CC 
# C405880027 由于GPRS服务和非GPRS服务不允许导致的SGSN内RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于GPRS服务和非GPRS服务不允许导致的SGSN内RAU失败次数。 
测量触发点 : 
对于用户的SGSN内路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services and non-GPRS services not
allowed”（cause值等于0x8）时统计。 
采集方式 : 
CC 
# C405880028 由于PLMN不允许导致的SGSN内RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于PLMN不允许导致的SGSN内RAU失败次数。 
测量触发点 : 
对于用户的SGSN内路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“PLMN not allowed”（cause值等于0x0B）时统计。 
采集方式 : 
CC 
# C405880029 由于信元错误导致的SGSN内RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于信元错误导致的SGSN内RAU失败次数。 
测量触发点 : 
对于用户的SGSN内路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Information element non-existent or not
implemented”（cause值等于0x63）时统计。 
采集方式 : 
CC 
# C405880030 由于未指定的协议错误导致的SGSN内RAU失败次数 

计数器描述 : 
某RNC上用户发起局内路由更新，由于未指定的协议错误导致的SGSN内RAU失败次数。 
测量触发点 : 
对于用户的SGSN内路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Protocol error, unspecified”（cause值等于0x6F）时统计。 
采集方式 : 
CC 
# C405880031 由于非法用户导致的SGSN间的RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于非法用户导致的SGSN间的RAU失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Illegal MS”（cause值等于0x3）或“IMSI unknown
in HLR”（cause值等于0x2）时统计。 
采集方式 : 
CC 
# C405880032 由于位置区不允许导致的SGSN间的RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于位置区不允许导致的SGSN间的RAU失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Location Area not allowed”（cause值等于0xC）时统计。 
采集方式 : 
CC 
# C405880033 由于漫游位置区不允许导致的SGSN间的RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于漫游位置区不允许导致的SGSN间的RAU失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Roaming not allowed in this location area”（cause值等于0xD）时统计。 
采集方式 : 
CC 
# C405880034 由于非法设备导致的SGSN间的RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于非法设备导致的SGSN间的RAU失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Illegal ME”（cause值等于0x6）时统计。 
采集方式 : 
CC 
# C405880035 由于GPRS服务不允许导致的SGSN间的RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于GPRS服务不允许导致的SGSN间的RAU失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services  not allowed”（cause值等于0x7）时统计。 
采集方式 : 
CC 
# C405880036 由于用户隐式分离导致的SGSN间的RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于用户隐式分离导致的SGSN间的RAU失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Implicitly detached”（cause值等于0xA）时统计。 
采集方式 : 
CC 
# C405880037 由于GPRS服务在本PLMN不允许导致的SGSN间的RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于GPRS服务在本PLMN不允许导致的SGSN间的RAU失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services not allowed in this PLMN”（cause值等于0xE）时统计。 
采集方式 : 
CC 
# C405880038 由于本位置区没有合适的小区导致的SGSN间的RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于本位置区没有合适的小区导致的SGSN间的RAU失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“No Suitable Cells In Location Area”（cause值等于0xF）时统计。 
采集方式 : 
CC 
# C405880039 由于消息类型不存在导致SGSN间的路由更新失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于消息类型不存在导致SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Message type non-existent or not implemented”（cause值等于0x61）时统计。 
采集方式 : 
CC 
# C405880040 由于必选项错误导致SGSN间的路由更新失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于必选项错误导致SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Invalid mandatory information”（cause值等于0x60）时统计。 
采集方式 : 
CC 
# C405880041 由于消息类型和协议不匹配导致SGSN间的路由更新失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于消息类型和协议不匹配导致SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Message not compatible with the protocol
state”（cause值等于0x62）时统计。 
采集方式 : 
CC 
# C405880042 由于网络无法获取MS ID导致SGSN间的路由更新失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于网络无法获取MS ID导致SGSN间的路由更新失败次数。 
测量触发点 : 
对于用户的SGSN间GPRS路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“MS identity cannot be derived by the network”（cause值等于0x9）时统计。 
采集方式 : 
CC 
# C405880043 由于GPRS服务和非GPRS服务不允许导致的SGSN间RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于GPRS服务和非GPRS服务不允许导致的SGSN间RAU失败次数。 
测量触发点 : 
对于用户的SGSN间路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services and non-GPRS services not
allowed”（cause值等于0x8）时统计。 
采集方式 : 
CC 
# C405880044 由于PLMN不允许导致的SGSN间RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于PLMN不允许导致的SGSN间RAU失败次数。 
测量触发点 : 
对于用户的SGSN间路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“PLMN not allowed”（cause值等于0x0B）时统计。 
采集方式 : 
CC 
# C405880045 由于信元错误导致的SGSN间RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于信元错误导致的SGSN间RAU失败次数。 
测量触发点 : 
对于用户的SGSN间路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Information element non-existent or not
implemented”（cause值等于0x63）时统计。 
采集方式 : 
CC 
# C405880046 由于未指定的协议错误导致的SGSN间RAU失败次数 

计数器描述 : 
某RNC上用户发起局间路由更新，由于未指定的协议错误导致的SGSN间RAU失败次数。 
测量触发点 : 
对于用户的SGSN间路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Protocol error, unspecified”（cause值等于0x6F）时统计。 
采集方式 : 
CC 
# C405880047 由于非法用户导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于非法用户导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Illegal MS”（cause值等于0x3）或“IMSI unknown
in HLR”（cause值等于0x2）时统计。 
采集方式 : 
CC 
# C405880048 由于位置区不允许导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于位置区不允许导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Location Area not allowed”（cause值等于0xC）时统计。 
采集方式 : 
CC 
# C405880049 由于漫游位置区不允许导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于漫游位置区不允许导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Roaming not allowed in this location area”（cause值等于0xD）时统计。 
采集方式 : 
CC 
# C405880050 由于非法设备导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于非法设备导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Illegal ME”（cause值等于0x6）时统计。 
采集方式 : 
CC 
# C405880051 由于GPRS服务不允许导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于GPRS服务不允许导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services not allowed”（cause值等于0x7）时统计。 
采集方式 : 
CC 
# C405880052 由于用户隐式分离导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于用户隐式分离导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Implicitly detached”（cause值等于0xA）时统计。 
采集方式 : 
CC 
# C405880053 由于GPRS服务在本PLMN不允许导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于GPRS服务在本PLMN不允许导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services not allowed in this PLMN”（cause值等于0xE）时统计。 
采集方式 : 
CC 
# C405880054 由于本位置区没有合适的小区导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于本位置区没有合适的小区导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“No Suitable Cells In Location Area”（cause值等于0xF）时统计。 
采集方式 : 
CC 
# C405880055 由于消息类型不存在导致周期性路由更新失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于消息类型不存在导致周期性路由更新失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Message type non-existent or not implemented”（cause值等于0x61）时统计。 
采集方式 : 
CC 
# C405880056 由于必选项错误导致周期性路由更新失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于必选项错误导致周期性路由更新失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Invalid mandatory information”（cause值等于0x60）时统计。 
采集方式 : 
CC 
# C405880057 由于消息类型和协议不匹配导致周期性路由更新失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于消息类型和协议不匹配导致周期性路由更新失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Message not compatible with the protocol
state”（cause值等于0x62）时统计。 
采集方式 : 
CC 
# C405880058 由于网络无法获取MS ID导致周期性路由更新失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于网络无法获取MS ID导致周期性路由更新失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“MS identity cannot be derived by the network”（cause值等于0x9）时统计。 
采集方式 : 
CC 
# C405880059 由于GPRS服务和非GPRS服务不允许导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于GPRS服务和非GPRS服务不允许导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“GPRS services and non-GPRS services not
allowed”（cause值等于0x8）时统计。 
采集方式 : 
CC 
# C405880060 由于PLMN不允许导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于PLMN不允许导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“PLMN not allowed”（cause值等于0x0B）时统计。 
采集方式 : 
CC 
# C405880061 由于信元错误导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于信元错误导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Information element non-existent or not
implemented”（cause值等于0x63）时统计。 
采集方式 : 
CC 
# C405880062 由于未指定的协议错误导致的周期性RAU失败次数 

计数器描述 : 
某RNC上用户发起周期性路由更新，由于未指定的协议错误导致的周期性RAU失败次数。 
测量触发点 : 
对于用户的周期性路由更新请求，SGSN下发路由更新拒绝消息（Routing
Area Update Reject），拒绝原因值为“Protocol error, unspecified”（cause值等于0x6F）时统计。 
采集方式 : 
CC 
# C405880063 由于用户参数不对引起的PDP失败的次数 

计数器描述 : 
测量某RNC上由于用户参数不对引起的PDP失败的次数。 
测量触发点 : 
SGSN向MS发送拒绝PDP激活请求消息，其中Cause Code为33时统计。 
采集方式 : 
CC 
# C405880064 由于APN丢失或不知道引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上由于APN丢失或不知道引起的PDP激活失败次数。 
测量触发点 : 
SGSN向MS发送拒绝PDP激活请求消息，其中Cause Code等于27时统计。 
采集方式 : 
CC 
# C405880065 由于未分类原因的PDP激活失败次数 

计数器描述 : 
测量某RNC上由于未分类原因引起的PDP激活失败次数。 
测量触发点 : 
SGSN向MS发出拒绝PDP激活请求的消息，其中Cause Code为其他原因值（即除了本测量类型下其他计数器中已定义的激活失败拒绝原因值以外的其他原因值）时统计。 
采集方式 : 
CC 
# C405880066 由于系统资源不足导致的MS发起PDP上下文激活失败次数 

计数器描述 : 
测量某RNC上由于系统资源不足导致的MS发起PDP上下文激活失败次数。 
测量触发点 : 
SGSN向MS发送Active PDP Context Reject消息，消息中携带拒绝原因为“insufficient
resource”（Cause Code为26）时统计。 
采集方式 : 
CC 
# C405880067 由于未知的PDP地址或PDP类型引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上由于用户激活请求中所带的PDP地址、PDP类型不合法或者错误引起的激活失败次数。 
测量触发点 : 
SGSN向MS发送拒绝PDP激活请求消息，消息中携带拒绝原因为“Unknown
PDP address or PDP type”（Cause Code为28）时统计。 
采集方式 : 
CC 
# C405880068 由于用户鉴权失败引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上激活过程中由于用户鉴权失败而引起的PDP激活失败次数。 
测量触发点 : 
SGSN向MS发送拒绝PDP激活请求消息，消息中携带拒绝原因为“User
Authentication failed”（Cause Code为29）时统计。 
采集方式 : 
CC 
# C405880069 由于不支持的请求业务及ODB引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上由于SGSN不支持的请求业务及ODB引起的PDP激活失败次数。 
测量触发点 : 
SGSN向MS发送拒绝PDP激活请求的消息，消息中携带拒绝原因为“Service
option not supported”（Cause Code为32）或“Operator Determined Barring”（Cause
Code为8）时统计。 
采集方式 : 
CC 
# C405880070 由于选择的服务乱序导致的激活失败次数 

计数器描述 : 
测量某RNC上由于流程冲突导致激活失败次数。 
测量触发点 : 
用户发起RAU流程（或其他用户级流程），当RAU流程未结束时，用户发起激活请求，两者产生冲突时统计。 
采集方式 : 
CC 
# C405880071 由于NSAPI已被使用导致的激活失败次数 

计数器描述 : 
某RNC上，MS发送的激活请求消息中携带NSAPI（Network-layer Service
Access Point Identifier，网络层业务接入点标识），但网络侧已有该用户相同NSAPI的PDP上下文，导致激活失败的次数。
测量触发点 : 
某RNC上，MS发送的激活请求消息中携带NSAPI，但网络侧已有该用户相同NSAPI的PDP上下文，导致激活失败，失败原因为“NSAPI
already used (not sent ”（Cause Code为35）时统计。 
采集方式 : 
CC 
# C405880072 由于协议错误导致的激活失败次数 

计数器描述 : 
测量某RNC上由于协议规定的参数错误导致激活失败次数。 
测量触发点 : 
SGSN收到MS发起的PDP上下文激活请求消息（activate PDP
context request），其必选参数NSAPI、SAPI或QoS不符合协议规定值，SGSN给MS发送激活拒绝的cause值为95~111时统计。 
采集方式 : 
CC 
# C405880073 由于未定义原因的PDP激活失败次数 

计数器描述 : 
测量某RNC上由于未定义原因导致的PDP激活失败次数。 
测量触发点 : 
SGSN向MS发出拒绝PDP激活请求的消息，消息中携带拒绝原因为“activation
rejected, unspecified”（Cause Code为31）时统计。 
采集方式 : 
CC 
# C405880074 由于ODB引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上激活过程中由于ODB导致的PDP激活失败次数。 
测量触发点 : 
用户在激活过程中，由于ODB原因而激活失败，失败原因为“Operator
Determined Barring”（Cause Code为8）时统计。 
采集方式 : 
CC 
# C405880075 由于GGSN/SGW/PGW激活拒绝引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上，在激活过程中由于GGSN/SGW/PGW激活拒绝导致的PDP激活失败次数。 
测量触发点 : 
用户在激活过程中，由于GGSN/SGW/PGW激活拒绝原因而激活失败，失败原因为“Activation
rejected by GGSN”（Cause Code为0x1E）时统计。 
采集方式 : 
CC 
# C405880076 由于QoS不接受引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上，在激活过程中由于QoS不接受导致的PDP激活失败次数。 
测量触发点 : 
用户在激活过程中，由于QoS不接受原因而激活失败，失败原因为“QoS
not accepted”（Cause Code为0x25）时统计。 
采集方式 : 
CC 
# C405880077 由于网络失败引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上，在激活过程中由于网络失败导致的PDP激活失败次数。 
测量触发点 : 
用户在激活过程中，由于网络失败原因而激活失败，失败原因为“Network
failure”（Cause Code为0x26）时统计。 
采集方式 : 
CC 
# C405880078 由于TFT错误引起的PDP激活失败次数 

计数器描述 : 
测量某RNC上，在激活过程中由于TFT错误导致的PDP激活失败次数。 
测量触发点 : 
用户在激活过程中，由于TFF错误原因而激活失败，失败原因为“Semantic
error in the TFT operation”（Cause Code为0X29）、“Syntactical error in
the TFT operation”（Cause Code为0X2A）、“Semantic errors in packet filter(s
”（Cause Code为0X2C）、“Syntactical errors in packet filter(s ”（Cause
Code为0X2D）、“PDP context without TFT already activated”（Cause Code为0X2E））时统计。 
采集方式 : 
CC 
# C405880079 由于不支持的请求业务引起的PDP激活失败次数 

计数器描述 : 
统计某RNC上，SGSN不支持的请求业务引起的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发送的PDP激活请求消息后，向MS发出拒绝PDP激活请求的消息，在拒绝PDP激活请求的消息中指示Cause
Code和原因为：Caused Code 32：Service option not supported（3G）时，进行统计。 
采集方式 : 
CC 
# C405880080 未知的PDP上下文原因引起的PDP激活失败次数 

计数器描述 : 
统计某RNC上，用户3G接入，二次激活过程中未知的PDP上下文原因导致二次激活失败次数。 
测量触发点 : 
MS（3G接入）/网络发起二次PDP上下文激活，SGSN在激活二次PDP拒绝消息中指示Cause
Code和原因为：Caused Code 43：unknown PDP context时，进行统计。 
采集方式 : 
CC 
# C405880081 由于语义错误消息导致的PDP激活失败次数 

计数器描述 : 
统计某RNC上，由于语义错误消息导致的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 95：Semantically incorrect message时，进行统计。 
采集方式 : 
CC 
# C405880082 由于无效的强制性信息导致的PDP激活失败次数 

计数器描述 : 
统计某RNC上，由于无效的强制性信息导致的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 96：Invalid mandatory information时，进行统计。 
采集方式 : 
CC 
# C405880083 由于消息类型不存在或不能实现导致的PDP激活失败次数 

计数器描述 : 
统计某RNC上，由于消息类型不存在或不能实现导致的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 97：Message type non-existent or not implemented时，进行统计。 
采集方式 : 
CC 
# C405880084 由于消息类型与协议状态不兼容导致的PDP激活失败次数 

计数器描述 : 
统计某RNC上，由于消息类型与协议状态不兼容导致的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 98：Message type not compatible with the protocol state时，进行统计。 
采集方式 : 
CC 
# C405880085 由于信息单元不存在或不能实现导致的PDP激活失败次数 

计数器描述 : 
统计某RNC上，由于信息单元不存在或不能实现导致的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 99：Information element non-existent or not implemented时，进行统计。 
采集方式 : 
CC 
# C405880086 由于IE错误条件导致的PDP激活失败次数 

计数器描述 : 
统计某RNC上，由于IE错误条件导致的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 100：Conditional IE error时，进行统计。 
采集方式 : 
CC 
# C405880087 由于消息不兼容协议状态导致的PDP激活失败次数 

计数器描述 : 
统计某RNC上，由于消息不兼容协议状态导致的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 101：Message not compatible with the protocol state时，进行统计。 
采集方式 : 
CC  
# C405880088 由于协议错误未指定导致的PDP激活失败次数 

计数器描述 : 
统计某RNC上，由于协议错误未指定导致的PDP激活失败次数（3G）。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 111：Protocol error, unspecified时，进行统计。 
采集方式 : 
CC 
# C405880089 由于隐式去附着导致的附着失败次数 

计数器描述 : 
统计某RNC上，由于隐式去附着导致用户（Iu口接入）GPRS附着失败的次数。 
测量触发点 : 
Iu口附着过程失败，SGSN向MS发送附着拒绝消息（ATTACH REJECT，3GPP
TS 24.008），其中GMM cause指明失败原因为隐式去附着（cause值等于10（十进制）），则计数器加1。 
采集方式 : 
CC 
# C405880090 由于超时导致的PDP激活失败次数 

计数器描述 : 
统计采集周期里超时导致PDP激活失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）由于无线侧、网络侧、CAMEL超时导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405880091 QoS不接受导致的MS修改会话失败次数 

计数器描述 : 
统计采集周期里QoS不接受导致MS修改会话失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）MS发起修改PDP，无线侧或网络侧QoS修改不接受导致流程失败时统计。 
采集方式 : 
CC 
# C405880092 未知的PDP上下文原因导致的MS修改会话失败次数 

计数器描述 : 
统计采集周期里MS发起修改PDP流程中，由于未找到上下文导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）MS发起修改PDP流程，由于当未找到上下文导致流程失败时统计。 
采集方式 : 
CC 
# C405880093 由于内部错误/限制导致的MS修改会话失败次数 

计数器描述 : 
统计采集周期内MS发起修改PDP流程中，由于内部错误/限制导致的流程失败次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）MS发起修改PDP流程， 由于内部错误/限制导致流程失败时统计。 
采集方式 : 
CC 
# C405880094 由于其他原因导致的MS修改会话失败次数 

计数器描述 : 
统计采集周期内MS发起修改PDP流程中，由于其他原因导致的流程失败次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）MS发起修改PDP流程，由于其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405880095 UE无响应导致的MS修改会话失败次数 
计数器描述 : 
统计采集周期内UE无响应导致的MS修改会话失败次数。 
测量触发点 : 
流程结束时发送消息通知UE，不存在等UE的响应的过程。 
采集方式 : 
CC 
# C405880096 由于内部错误/限制导致的SGSN修改会话失败次数 

计数器描述 : 
采集周期内统计SGSN发起修改PDP流程中，由于内部错误/限制导致失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）SGSN发起修改PDP流程，内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405880097 由于其他原因导致的SGSN修改会话失败次数 

计数器描述 : 
采集周期内统计SGSN发起修改PDP流程中，由于其他原因导致失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）SGSN发起修改PDP流程，其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405880098 系统失败导致的GGSN更新会话失败次数 

计数器描述 : 
采集周期内统计GGSN发起更新PDP流程中，由于系统原因导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）GGSN发起更新PDP流程，由于系统原因导致流程失败时统计。 
采集方式 : 
CC 
# C405880099 由于内部错误/限制导致的GGSN更新会话失败次数 

计数器描述 : 
采集周期内统计GGSN发起更新PDP流程中，由于内部错误/限制导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）GGSN发起更新PDP流程，由于内部错误/限制导致流程失败时统计。 
采集方式 : 
CC 
# C405880100 由于其他原因导致的GGSN修改会话失败次数 

计数器描述 : 
采集周期内统计GGSN发起更新PDP流程中，由于其他原因导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）GGSN发起更新PDP流程，由于其他原因导致流程失败时统计。 
采集方式 : 
CC 
# C405880101 协议错误导致的MS去激活会话失败次数 

计数器描述 : 
采集周期内统计MS发起去激活流程中，由于协议错误导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）MS发起去激活流程，由于协议错误导致流程失败时统计。 
采集方式 : 
CC 
# C405880102 由于内部错误/限制导致的MS去激活会话失败次数 

计数器描述 : 
采集周期内统计MS发起去激活流程中，由于内部错误/限制导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）MS发起去激活流程，由于内部错误/限制导致流程失败时统计。 
采集方式 : 
CC 
# C405880103 由于其他原因导致的MS去激活会话失败次数 

计数器描述 : 
采集周期内统计MS发起去激活流程中，由于其他原因导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）MS发起去激活流程，由于其他原因导致流程失败时统计。 
采集方式 : 
CC 
# C405880104 必选IE未携带导致的GGSN去激活会话失败次数 

计数器描述 : 
采集周期内统计GGSN发起去激活流程中，由于必选IE未携带导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）GGSN发起去激活流程，由于必选IE未携带导致流程失败时统计。 
采集方式 : 
CC 
# C405880105 由于内部错误/限制导致的GGSN去激活会话失败次数 

计数器描述 : 
采集周期内统计GGSN发起去激活流程中，由于内部错误/限制导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）GGSN发起去激活流程，由于内部错误/限制导致流程失败时统计。 
采集方式 : 
CC 
# C405880106 由于其他原因导致的GGSN去激活会话失败次数 

计数器描述 : 
采集周期内统计GGSN发起去激活流程中，由于其他原因导致流程失败的次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）GGSN发起去激活流程，由于其他原因导致流程失败时统计。 
采集方式 : 
CC 
