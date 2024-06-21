# C430000001 EPS附着请求次数 


计数器描述 :统计附着类型为EPS附着（即Attach Type= EPS attach）的附着请求次数。 


测量触发点 :在EPS attach流程中，MME收到Attach Request消息后，MME附着处理成功或失败后进行统计。测量点如图中的A点和B点所示。 



采集方式 :CC 


# C430000002 EPS附着成功次数 


计数器描述 :统计附着类型为EPS附着的附着成功次数。 


测量触发点 :在EPS attach流程中，当MME下发Attach Accept消息后进行统计。测量点如下图A点所示。 
 


采集方式 :CC 


# C430000003 EPS附着失败次数(3-非法UE) 


计数器描述 :统计EPS附着失败次数（非法UE）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Illegal
UE）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000004 EPS附着失败次数(6-非法ME) 


计数器描述 :统计EPS附着失败次数（非法ME）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Illegal
ME）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000005 EPS附着失败次数(7-EPS服务不允许) 


计数器描述 :统计EPS附着失败次数（EPS服务不允许）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为EPS
services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000006 EPS附着失败次数(8-EPS服务和非EPS服务不允许) 


计数器描述 :统计EPS附着失败次数（EPS服务和非EPS服务不允许）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为EPS
services and non-EPS services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000007 EPS附着失败次数(11-PLMN不允许) 


计数器描述 :统计EPS附着失败次数（PLMN不允许）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为PLMN
not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000008 EPS附着失败次数(12-TA不允许) 


计数器描述 :统计EPS附着失败次数（TA不允许）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Tracking
Area not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000009 EPS附着失败次数(13-该TA不允许漫游) 


计数器描述 :统计EPS附着失败次数（该TA不允许漫游）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Roaming
not allowed in this tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000010 EPS附着失败次数(14-该PLMN不允许EPS服务) 


计数器描述 :统计EPS附着失败次数（该PLMN不允许EPS服务）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为EPS
services not allowed in this PLMN）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000011 EPS附着失败次数(15-该TA中没有合适的小区) 


计数器描述 :统计EPS附着失败次数（该TA中没有合适的小区）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为No
Suitable Cells In tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000012 EPS附着失败次数(17-网络失败) 


计数器描述 :统计EPS附着失败次数（网络失败）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Network
failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000013 EPS附着失败次数(19-ESM失败) 


计数器描述 :统计EPS附着失败次数（ESM失败）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为ESM
failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000014 EPS附着失败次数(19-ESM失败_用户原因) 


计数器描述 :统计EPS附着失败次数（用户原因导致的ESM失败）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为ESM
failure，ESM Message Container中包含的ESM cause为除了Insufficient resources、Request
rejected by Serving GW or PDN GW、Network failure之外的其他值）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000015 EPS附着失败次数(22-拥塞) 


计数器描述 :统计EPS附着失败次数（拥塞）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Congestion）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000016 EPS附着失败次数(25-CSG未授权) 


计数器描述 :统计EPS附着失败次数（CSG未授权）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Not
authorized for this CSG）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000017 EPS附着失败次数(35-请求的业务选项在该PLMN未授权) 


计数器描述 :该计数器用于统计EPS附着失败次数，失败原因是请求的业务选项在该PLMN未授权。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Requested
service option not authorized in this PLMN）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000018 EPS附着失败次数(96-必选字段无效) 


计数器描述 :统计EPS附着失败次数（必选字段无效）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Invalid
mandatory information）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000019 EPS附着失败次数(97-消息类型缺失或没有实现) 


计数器描述 :统计EPS附着失败次数（消息类型缺失或没有实现）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Message
type non-existent or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000020 EPS附着失败次数(99-信息元素不存在或未应用) 


计数器描述 :统计EPS附着失败次数（信息元素不存在或未应用）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Information
element non-existent or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000021 EPS附着失败次数(100-条件IE错误) 


计数器描述 :统计EPS附着失败次数（条件IE错误）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Conditional
IE error）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000022 EPS附着失败次数(111-协议错误) 


计数器描述 :统计EPS附着失败次数（协议错误）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Protocol
error, unspecified）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000023 EPS附着失败次数(其他原因) 


计数器描述 :统计EPS附着失败次数（其他原因）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Other
cause）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000024 EPS附着建立时长(毫秒) 


计数器描述 :统计EPS用户附着建立时长。 


测量触发点 :在统计周期内，统计MME收到附着类型为EPS attach的Attach
Request消息到MME下发Attach Accept消息的间隔时长（单位：毫秒）。如下图所示，统计时长为A点到B点的时长。


采集方式 :CC 


# C430000025 联合附着请求次数 


计数器描述 :统计附着类型为联合附着（即Attach Type =Combined
EPS/IMSI attach）的附着请求次数。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息后，MME附着处理成功或失败后统计。测量点如图中的A点和B点所示。 



采集方式 :CC 


# C430000026 联合附着成功次数 


计数器描述 :统计附着类型为联合附着的附着成功次数。 


测量触发点 :在combined attach流程中，当MME下发Attach Accept消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000027 联合附着SMS-only成功次数 


计数器描述 :该计数器用于统计附着类型为联合附着且附加更新结果是SMS-only的附着成功次数。 


测量触发点 :在combined attach流程中，MME向UE发送Attach
Accept消息，当消息中Additional update result信元值为“SMS Only”时进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000028 联合附着失败次数(2-在HSS中没有IMSI) 


计数器描述 :统计联合附着失败次数（在HSS中没有IMSI）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为IMSI unknown in HSS）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000029 联合附着失败次数(3-非法UE) 


计数器描述 :统计联合附着失败次数（非法UE）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Illegal UE）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000030 联合附着失败次数(6-非法ME) 


计数器描述 :统计联合附着失败次数（非法ME）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Illegal ME）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000031 联合附着失败次数(7-EPS服务不允许) 


计数器描述 :统计联合附着失败次数（EPS服务不允许）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为EPS services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000032 联合附着失败次数(8-EPS服务和非EPS服务不允许) 


计数器描述 :统计联合附着失败次数（EPS服务和非EPS服务不允许）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为EPS services and non-EPS services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000033 联合附着失败次数(9-UE标识不能在网络侧得到) 


计数器描述 :统计联合附着失败次数（UE标识不能在网络侧得到）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为UE identity cannot be derived by the network）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000034 联合附着失败次数(11-PLMN不允许) 


计数器描述 :统计联合附着失败次数（PLMN不允许）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为PLMN not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000035 联合附着失败次数(12-TA不允许) 


计数器描述 :统计联合附着失败次数（TA不允许）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Tracking Area not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000036 联合附着失败次数(13-该TA不允许漫游) 


计数器描述 :统计联合附着失败次数（该TA不允许漫游）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Roaming not allowed in this tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000037 联合附着失败次数(14-该PLMN不允许EPS服务) 


计数器描述 :统计联合附着失败次数（该PLMN不允许EPS服务）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为EPS services not allowed in this PLMN）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000038 联合附着失败次数(15-该TA中没有合适的小区) 


计数器描述 :统计联合附着失败次数（该TA中没有合适的小区）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为No Suitable Cells In tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000039 联合附着失败次数(16-MSC临时不可达) 


计数器描述 :统计联合附着失败次数（MSC临时不可达）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为MSC temporarily not reachable）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000040 联合附着失败次数(17-网络失败) 


计数器描述 :统计联合附着失败次数（网络失败）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Network failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000041 联合附着失败次数(18-CS域不可用) 


计数器描述 :统计联合附着失败次数（CS域不可用）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为CS domain not available）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000042 联合附着失败次数(19-ESM失败) 


计数器描述 :统计联合附着失败次数（ESM失败）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为ESM failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000043 联合附着失败次数(19-ESM失败_用户原因) 


计数器描述 :统计联合附着失败次数（ESM失败_用户原因导致的ESM失败）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为ESM failure，ESM Message Container中包含的ESM Cause为除了Insufficient
resources、Request rejected by Serving GW or PDN GW、Network failure之外的其他原因值）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000044 联合附着失败次数(22-拥塞) 


计数器描述 :统计联合附着失败次数（拥塞）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Congestion）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000045 联合附着失败次数(25-CSG未授权) 


计数器描述 :该计数器用于统计联合附着失败次数（CSG未授权）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Not authorized for this CSG）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000046 联合附着失败次数(35-请求的业务选项在该PLMN未授权) 


计数器描述 :该计数器用于统计联合附着失败次数，失败原因是请求的业务选项在该PLMN未授权。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Requested service option not authorized in this PLMN）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000047 联合附着失败次数(96-必选字段无效) 


计数器描述 :该计数器用于统计联合附着失败次数（必选字段无效）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Invalid mandatory information）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000048 联合附着失败次数(97-消息类型缺失或没有实现) 


计数器描述 :该计数器用于统计联合附着失败次数（消息类型缺失或没有实现）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Message type non-existent or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000049 联合附着失败次数(99-信息元素不存在或未应用) 


计数器描述 :该计数器用于统计联合附着失败次数（信息元素不存在或未应用）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Information element non-existent or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000050 联合附着失败次数(100-条件IE错误) 


计数器描述 :该计数器用于统计联合附着失败次数（条件IE错误）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Conditional IE error）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000051 联合附着失败次数(111-协议错误) 


计数器描述 :该计数器用于统计联合附着失败次数（协议错误）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Protocol error, unspecified）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000052 联合附着失败次数(其他原因) 


计数器描述 :该计数器用于统计联合附着失败次数（其他原因）。 


测量触发点 :在combined attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Other cause）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000053 联合附着仅EPS附着成功次数 


计数器描述 :该计数器用于统计附着类型为联合附着，仅EPS附着成功，IMSI附着失败的次数。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，MME向UE发送Attach
Accept消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000054 联合附着IMSI附着失败次数(2-在HSS中没有IMSI) 


计数器描述 :该计数器用于统计联合附着失败次数（在HSS中没有IMSI）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为IMSI unknown in HSS）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000055 联合附着IMSI附着失败次数(3-非法UE) 


计数器描述 :该计数器用于统计联合附着失败次数（非法UE）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Illegal UE）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000056 联合附着IMSI附着失败次数(6-非法ME) 


计数器描述 :该计数器用于统计联合附着失败次数（非法ME）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Illegal ME）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000057 联合附着IMSI附着失败次数(7-EPS服务不允许) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（EPS服务不允许）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为EPS services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000058 联合附着IMSI附着失败次数(8-EPS服务和非EPS服务不允许) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（EPS服务和非EPS服务不允许）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为EPS services and non-EPS services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000059 联合附着IMSI附着失败次数(9-UE标识不能在网络侧得到) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（UE标识不能在网络侧得到）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为UE identity cannot be derived by the network）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000060 联合附着IMSI附着失败次数(11-PLMN不允许) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（PLMN不允许）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为PLMN not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000061 联合附着IMSI附着失败次数(12-TA不允许) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（TA不允许）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Tracking Area not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000062 联合附着IMSI附着失败次数(13-该TA不允许漫游) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（该TA不允许漫游）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Roaming not allowed in this tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000063 联合附着IMSI附着失败次数(14-该PLMN不允许EPS服务) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（该PLMN不允许EPS服务）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为EPS services not allowed in this PLMN）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000064 联合附着IMSI附着失败次数(15-该TA中没有合适的小区) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（该TA中没有合适的小区）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为No Suitable Cells In tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000065 联合附着IMSI附着失败次数(16-MSC临时不可达) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（MSC临时不可达）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为MSC temporarily not reachable）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000066 联合附着IMSI附着失败次数(17-网络失败) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（网络失败）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Network failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000067 联合附着IMSI附着失败次数(18-CS域不可用) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（CS域不可用）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为CS domain not available）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000068 联合附着IMSI附着失败次数(22-拥塞) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（拥塞）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Congestion）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000069 联合附着IMSI附着失败次数(96-必选字段无效) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（必选字段无效）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Invalid mandatory information）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000070 联合附着IMSI附着失败次数(97-消息类型缺失或没有实现) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（消息类型缺失或没有实现）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Message type non-existent or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000071 联合附着IMSI附着失败次数(99-信息元素不存在或未应用) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（信息元素不存在或未应用）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Information element non-existent or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000072 联合附着IMSI附着失败次数(100-条件IE错误) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（条件IE错误）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Conditional IE error）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000073 联合附着IMSI附着失败次数(111-协议错误) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（协议错误）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Protocol error, unspecified）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000074 联合附着IMSI附着失败次数(其他原因) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数（其他原因）。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Other cause）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000075 联合附着IMSI附着失败次数(35-请求的业务选项在该PLMN未授权) 


计数器描述 :该计数器用于统计联合附着IMSI附着失败次数，失败原因是请求的业务选项在该PLMN未授权。 


测量触发点 :在combined attach流程中，IMSI附着失败，EPS附着成功，当MME向UE发送Attach
Accept（其中失败原因为Requested service option not authorized in this PLMN）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000076 联合附着建立时长(毫秒) 


计数器描述 :该计数器用于统计联合用户附着建立时长，单位：毫秒。 


测量触发点 :在统计周期内，MME收到附着类型为combined EPS/IMSI
attach的Attach Request消息到MME下发Attach Accept消息的间隔时长（单位：毫秒）。如下图所示，统计时长为A点到B点的时长。


采集方式 :CC 


# C430000077 联合附着(数据中心)请求次数 


计数器描述 :该计数器用于统计联合附着（数据中心）请求次数。 


测量触发点 :在combined attach流程中，MME收到UE发出的Attach
Request消息，并且消息中携带了Data centric字段，MME对该类消息处理成功或失败时进行统计。测量点如图中的A点和B点所示。 说明： 
仅仅EPS附着成功也需要统计。 



采集方式 :CC 


# C430000078 联合附着(数据中心)联合成功次数 


计数器描述 :该计数器用于统计联合附着（数据中心）联合成功次数。 


测量触发点 :在combined attach流程中，MME收到UE发出的Attach
Request消息，并且消息中携带了Data centric字段，MME向UE发送Attach Accept（combined EPS/IMSI
attach）消息后进行统计。测量点如图中的A点所示。 说明： 
只有在IMSI附着和EPS附着都成功时才统计，即EPS attach
result信元取值为combined EPS/IMSI attach。 
 


采集方式 :CC 


# C430000079 联合附着(数据中心)EPS成功次数 


计数器描述 :该计数器用于统计联合附着（数据中心）EPS成功次数。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，MME发送Attach Accept（EPS only）消息后进行统计。测量点如图中的A点所示。 说明： 
只有在EPS附着成功时才统计，即EPS attach result信元取值为EPS only。 
 


采集方式 :CC 


# C430000080 联合附着(数据中心)失败次数(2-在HSS中没有IMSI) 


计数器描述 :该计数器用于统计联合附着失败次数（在HSS中没有IMSI）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为IMSI unknown in HSS）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000081 联合附着(数据中心)失败次数(3-非法UE) 


计数器描述 :该计数器用于统计联合附着失败次数（非法UE）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Illegal UE）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000082 联合附着(数据中心)失败次数(6-非法ME) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（非法ME）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Illegal ME）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000083 联合附着(数据中心)失败次数(7-EPS服务不允许) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（EPS服务不允许）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为EPS services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000084 联合附着(数据中心)失败次数(8-EPS服务和非EPS服务不允许) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（EPS服务和非EPS服务不允许）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为EPS services and non-EPS services
not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000085 联合附着(数据中心)失败次数(9-UE标识不能在网络侧得到) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（UE标识不能在网络侧得到）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为UE identity cannot be derived
by the network）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000086 联合附着(数据中心)失败次数(11-PLMN不允许) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（PLMN不允许）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为PLMN not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000087 联合附着(数据中心)失败次数(12-TA不允许) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（TA不允许）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Tracking Area not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000088 联合附着(数据中心)失败次数(13-该TA不允许漫游) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（该TA不允许漫游）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Roaming not allowed in this
tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000089 联合附着(数据中心)失败次数(14-该PLMN不允许EPS服务) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（该PLMN不允许EPS服务）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为EPS services not allowed in
this PLMN）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000090 联合附着(数据中心)失败次数(15-该TA中没有合适的小区) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（该TA中没有合适的小区）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为No Suitable Cells In tracking
area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000091 联合附着(数据中心)失败次数(16-MSC临时不可达) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（MSC临时不可达）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为MSC temporarily not reachable）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000092 联合附着(数据中心)失败次数(17-网络失败) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（网络失败）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Network failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000093 联合附着(数据中心)失败次数(18-CS域不可用) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（CS域不可用）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为CS domain not available）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000094 联合附着(数据中心)失败次数(19-ESM失败) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（ESM失败）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为ESM failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000095 联合附着(数据中心)失败次数(19-ESM失败_用户原因) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（用户原因导致的ESM失败）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为ESM failure，ESM Message Container中包含的ESM
Cause为除了Insufficient resources、Request rejected by Serving GW or PDN
GW、Network failure之外的其他原因值）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000096 联合附着(数据中心)失败次数(22-拥塞) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（拥塞）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Congestion）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000097 联合附着(数据中心)失败次数(25-CSG未授权) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（CSG未授权）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Not authorized for this CSG）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000098 联合附着(数据中心)失败次数(96-必选字段无效) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（必选字段无效）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Invalid mandatory information）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000099 联合附着(数据中心)失败次数(97-消息类型缺失或没有实现) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（消息类型缺失或没有实现）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Message type non-existent
or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000100 联合附着(数据中心)失败次数(99-信息元素不存在或未应用) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（信息元素不存在或未应用）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Information element non-existent
or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000101 联合附着(数据中心)失败次数(100-条件IE错误) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（条件IE错误）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Conditional IE error）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000102 联合附着(数据中心)失败次数(111-协议错误) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（协议错误）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Protocol error, unspecified）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000103 联合附着(数据中心)失败次数(其他原因) 


计数器描述 :该计数器用于统计联合附着（数据中心）失败次数（其他原因）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Other cause）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000104 联合附着(数据中心)建立时长(毫秒) 


计数器描述 :统计MME上基于Data Centric的联合附着的建立时长，单位：毫秒。 


测量触发点 :在统计周期内，统计MME收到附着类型为combined EPS/IMSI
attach的Attach Request消息（携带Data centric）到MME下发Attach Accept消息的间隔时长（单位：毫秒）。如下图所示，统计时长为A点到B点的时长。 说明： 
必须是EPS和CS都附着成功，才统计。 
 


采集方式 :CC 


# C430000105 联合附着(语音中心)请求次数 


计数器描述 :该计数器用于统计联合附着（语音中心）请求次数。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，MME对该类消息处理成功或失败时进行统计。测量点如图中的A点和B点所示。 说明： 
仅仅EPS附着成功也需要统计。 



采集方式 :CC 


# C430000106 联合附着(语音中心)联合成功次数 


计数器描述 :该计数器用于统计联合附着（语音中心）联合成功次数。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，MME发送Attach Accept（combined EPS/IMSI attach）消息后进行统计。测量点如图中的A点所示。 说明： 
只有在IMSI附着和EPS附着都成功时才统计，即EPS attach result信元取值为combined EPS/IMSI
attach。 
 


采集方式 :CC 


# C430000107 联合附着(语音中心)EPS成功次数 


计数器描述 :该计数器用于统计联合附着（语音中心）EPS成功次数。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，MME发送Attach Accept（EPS only）消息后进行统计。测量点如图中的A点所示。 说明： 
只有在EPS附着成功时才统计，即EPS attach result信元取值为EPS only。 
 


采集方式 :CC 


# C430000108 联合附着(语音中心)失败次数(2-在HSS中没有IMSI) 


计数器描述 :该计数器用于统计联合附着失败次数（在HSS中没有IMSI）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为IMSI unknown in HSS）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000109 联合附着(语音中心)失败次数(3-非法UE) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（非法UE）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Illegal UE）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000110 联合附着(语音中心)失败次数(6-非法ME) 


计数器描述 :该计数器用于统计联合附着失败次数（非法ME）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Illegal ME）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000111 联合附着(语音中心)失败次数(7-EPS服务不允许) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（EPS服务不允许）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为EPS services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000112 联合附着(语音中心)失败次数(8-EPS服务和非EPS服务不允许) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（EPS服务和非EPS服务不允许）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为EPS services and non-EPS services
not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000113 联合附着(语音中心)失败次数(9-UE标识不能在网络侧得到) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（UE标识不能在网络侧得到）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为UE identity cannot be derived
by the network）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000114 联合附着(语音中心)失败次数(11-PLMN不允许) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（PLMN不允许）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为PLMN not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000115 联合附着(语音中心)失败次数(12-TA不允许) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（TA不允许）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Tracking Area not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000116 联合附着(语音中心)失败次数(13-该TA不允许漫游) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（该TA不允许漫游）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Roaming not allowed in this
tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000117 联合附着(语音中心)失败次数(14-该PLMN不允许EPS服务) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（该PLMN不允许EPS服务）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为EPS services not allowed in
this PLMN）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000118 联合附着(语音中心)失败次数(15-该TA中没有合适的小区) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（该TA中没有合适的小区）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为No Suitable Cells In tracking
area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000119 联合附着(语音中心)失败次数(16-MSC临时不可达) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（MSC临时不可达）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为MSC temporarily not reachable）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000120 联合附着(语音中心)失败次数(17-网络失败) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（网络失败）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Network failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000121 联合附着(语音中心)失败次数(18-CS域不可用) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（CS域不可用）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为CS domain not available）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000122 联合附着(语音中心)失败次数(19-ESM失败) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（ESM失败）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为ESM failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000123 联合附着(语音中心)失败次数(19-ESM失败_用户原因) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（用户原因导致的ESM失败）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject消息（其中失败原因为ESM failure，ESM Message
Container中包含的ESM Cause为除了Insufficient resources、Request rejected by
Serving GW or PDN GW、Network failure之外的其他原因值）时进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000124 联合附着(语音中心)失败次数(22-拥塞) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（拥塞）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Congestion）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000125 联合附着(语音中心)失败次数(25-CSG未授权) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（CSG未授权）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Not authorized for this CSG）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000126 联合附着(语音中心)失败次数(96-必选字段无效) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（必选字段无效）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Invalid mandatory information）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000127 联合附着(语音中心)失败次数(97-消息类型缺失或没有实现) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（消息类型缺失或没有实现）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Message type non-existent
or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000128 联合附着(语音中心)失败次数(99-信息元素不存在或未应用) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（信息元素不存在或未应用）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Information element non-existent
or not implemented）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000129 联合附着(语音中心)失败次数(100-条件IE错误) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（条件IE错误）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Conditional IE error）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000130 联合附着(语音中心)失败次数(111-协议错误) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（协议错误）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Protocol error, unspecified）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000131 联合附着(语音中心)失败次数(其他原因) 


计数器描述 :该计数器用于统计联合附着（语音中心）失败次数（其他原因）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Other cause）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000132 联合附着(语音中心)建立时长(毫秒) 


计数器描述 :该计数器用于统计基于Voice centric联合附着建立时长，单位：毫秒。 


测量触发点 :在统计周期内，统计MME收到附着类型为combined EPS/IMSI
attach的Attach Request消息（携带Voice centric）到 MME下发Attach Accept消息的间隔时长（单位：毫秒）。如下图所示，统计时长为A点到B点的时长。 说明： 
必须是EPS和CS都附着成功，才统计。 
 


采集方式 :CC 


# C430000133 EPS附着失败次数(5-IMEI不接受) 


计数器描述 :该计数器用于统计EPS附着失败次数，失败原因是IMEI不接受。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为IMEI
not accepted）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000134 EPS附着失败次数(7-EPS服务不允许_用户原因) 


计数器描述 :该计数器用于统计EPS附着失败次数，失败原因是用户原因的EPS服务不允许。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为EPS
services not allowed）消息，并满足以下场景之一时进行统计。 

 
MME上配置和本运营商签订4G漫游协议的运营商PLMN列表，未在列表中的运营商的用户漫游接入时。 

 
MME由于本地区域限制，导致拒绝UE附着。 

 
漫入用户归属运营商已和本运营商签订漫游协议，但是用户仅未开通LTE国际漫游（可能开通了2G/3G漫游）。HSS拒绝MME对该用户的位置更新（ULR），拒绝原因值为DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION（5420
with Error Diagnostic of NO_GPRS_DATA_SUBSCRIBED）。 

 
漫入用户归属运营商已和本运营商签订漫游协议，但是该用户未开通2G/3G/LTE的CS和PS国际漫游，用户尝试接入LTE网络时，HSS拒绝MME对该用户的位置更新（ULR），拒绝原因值为DIAMETER_ERROR_ROAMING_NOT_ALLOWED（5004）时。 

 
用户使用SIM卡接入，HSS拒绝向MME提供该用户的鉴权向量，拒绝原因值为DIAMETER_AUTHORIZATION_REJECTED（5003）。 

 
测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000135 EPS附着失败次数(15-该TA中没有合适的小区_用户原因) 


计数器描述 :该计数器用于统计EPS附着失败次数，失败原因是用户原因的EPS服务不允许。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为No
Suitable Cells In tracking area）消息，并满足以下场景之一时进行统计。 

 
在MME上配置和中国移动签订4G漫游协议的运营商PLMN列表，未在列表中的运营商的用户漫入时。 

 
MME由于本地区域限制，导致拒绝UE附着。 

 
运营商已和中国移动签订漫游协议，但是该用户仅未开通LTE国际漫游（可能开通了2/3G漫游），HSS拒绝MME对该用户的位置更新（ULR），拒绝原因值为IAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION（5420
without Error Diagnostic, or with Error Diagnostic of GPRS_DATA_SUBSCRIBED）。 

 
用户归属运营商和中国移动签订漫游协议，但是该用户未开通2G、3G、LTE的CS和PS国际漫游，用户尝试接入LTE网络时，HSS拒绝MME对该用户的位置更新（ULR），拒绝原因值为DIAMETER_ERROR_ROAMING_NOT_ALLOWED（5004）时。 

 
用户使用SIM卡接入，HSS拒绝向MME提供该用户的鉴权向量，拒绝原因值为DIAMETER_AUTHORIZATION_REJECTED（5003）。 

 
用户未签约4G、但是签约了2G/3G，HSS拒绝MME对该用户的鉴权，拒绝原因值为DIAMETER_ERROR_UNKNOWN_EPS_SUBSCRIPTION（5420
without Error Diagnostic, or with Error Diagnostic of GPRS_DATA_SUBSCRIBED）。 

 
测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000136 EPS附着失败次数(19-ESM失败_ODB) 


计数器描述 :该计数器用于统计EPS附着失败次数，失败原因是ODB导致的ESM失败。


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为ESM
failure，并且ESM failure是由于ODB引起的）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000137 联合附着失败次数(5-IMEI不接受) 


计数器描述 :该计数器用于统计联合附着失败次数，失败原因是IMEI不接受。 


测量触发点 :在combined EPS/IMSI attach流程中，当MME向UE发送Attach
Reject（其中失败原因为IMEI not accepted）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000138 联合附着失败次数(7-EPS服务不允许_用户原因) 


计数器描述 :该计数器用于统计联合附着失败次数，失败原因是用户原因的EPS服务不允许。 


测量触发点 :在combined EPS/IMSI attach流程中，当MME向UE发送Attach
Reject（其中失败原因为EPS services not allowed）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000139 联合附着失败次数(15-该TA中没有合适的小区_用户原因) 


计数器描述 :该计数器用于统计联合附着失败次数，失败原因是该TA中没有合适的小区。 


测量触发点 :在combined EPS/IMSI attach流程中，当MME向UE发送Attach
Reject（其中失败原因为No Suitable Cells In tracking area）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000140 联合附着失败次数(19-ESM失败_ODB) 


计数器描述 :该计数器用于统计联合附着失败次数，失败原因是ODB导致的ESM失败。


测量触发点 :在combined EPS/IMSI attach流程中，当MME向UE发送Attach
Reject（其中失败原因为ESM failure）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000141 EPS附着失败次数(10-隐式去附着) 


计数器描述 :EPS附着失败次数（隐式去附着）。 


测量触发点 :在EPS attach流程中，当MME向UE发送Attach Reject（其中失败原因为Implicitly
detached）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000142 联合附着失败次数(10-隐式去附着) 


计数器描述 :联合附着失败次数（隐式去附着）。 


测量触发点 :在combined EPS/IMSI attach流程中，当MME向UE发送Attach
Reject（其中失败原因为Implicitly detached）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000143 联合附着IMSI附着失败次数(10-隐式去附着) 


计数器描述 :基于data centric的联合附着失败次数（隐式去附着）。 


测量触发点 :在combined EPS/IMSI attach流程中，当MME向UE发送仅EPS附着成功的Attach
Accept（其中失败原因为Implicitly detached）消息后进行统计。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000144 联合附着(数据中心)失败次数(10-隐式去附着) 


计数器描述 :基于Voice centric的联合附着失败次数（隐式去附着）。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME向UE发送Attach Reject（其中失败原因为Implicitly detached）消息后进行统计
。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000145 联合附着(语音中心)失败次数(10-隐式去附着) 


计数器描述 :基于Voice Centric联合附着建立时长。 


测量触发点 :在combined attach流程中，MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME向UE发送Attach Reject（其中失败原因为Implicitly detached）消息后进行统计
。测量点如图中的A点所示。 
 


采集方式 :CC 


# C430000146 EPS附着完成建立时长(毫秒) 


计数器描述 :在采集周期内统计EPS附着完成建立时长(毫秒)。 


测量触发点 :MME给UE发送Attach Accept消息时，如果消息中的EPS
attach result指示为EPS only，开始记录，当收到Attach Complete时进行统计Attach Accept消息与Attach
Complete消息之间的时间差。（触发点如下图所示。） 
 


采集方式 :CC 


# C430000147 联合附着完成建立时长(毫秒) 


计数器描述 :在采集周期内统计联合附着完成建立时长(毫秒)。 


测量触发点 :MME给UE发送Attach Accept消息时，如果消息中的EPS
attach result指示为combined EPS attach，开始记录，当收到Attach Complete时统计Attach
Accept消息与Attach Complete消息之间的时间差。（触发点如下图所示。） 
 


采集方式 :CC 


# C430000148 联合附着完成(数据中心)建立时长(毫秒) 


计数器描述 :在采集周期内统计联合附着完成(数据中心)建立时长(毫秒)。 


测量触发点 :MME收到Attach Request消息，并且消息中携带了Data
centric字段，当MME给UE发送Attach Accept消息时（消息中的EPS attach result指示为combined
EPS attach），开始记录，当收到Attach Complete时统计Attach Accept消息与 Attach Complete消息之间的时间差。（触发点图如下图所示。） 
 


采集方式 :CC 


# C430000149 联合附着完成(语音中心)建立时长(毫秒) 


计数器描述 :在采集周期内统计联合附着完成(语音中心)建立时长(毫秒)。 


测量触发点 :MME收到Attach Request消息，并且消息中携带了Voice
centric字段，当MME给UE发送Attach Accept消息时（消息中的EPS attach result指示为combined
EPS attach），开始记录，当收到Attach Complete时统计Attach Accept消息与 Attach Complete消息之间的时间差。（触发点如下图所示。） 
 


采集方式 :CC 


# C430000150 EPS附着(CP)请求次数 


计数器描述 :在采集周期内统计CP优化的EPS附着请求次数。 


测量触发点 :MME收到Attach Request消息，如果消息中的Attach
Type指示为EPS attach，同时附加更新类型指示为CP优化（control plane CIoT EPS optimization），在附着处理成功（发送Attach
Accept消息，如下图A点）或失败（发送Attach Reject消息，如下图B点）后进行统计。 
 


采集方式 :CC 


# C430000151 EPS附着(CP)成功次数 


计数器描述 :在采集周期内统计CP优化的EPS附着成功次数。 


测量触发点 :MME收到Attach Request消息，如果消息中的Attach
Type指示为EPS attach，同时附加更新类型指示为CP优化（control plane CIoT EPS optimization），在附着处理成功（发送Attach
Accept消息）后进行统计。 
 


采集方式 :CC 


# C430000152 EPS附着(UP)请求次数 


计数器描述 :在采集周期内统计UP优化的EPS附着请求次数。 


测量触发点 :MME收到Attach Request消息，如果消息中的Attach
Type指示为EPS attach，同时附加更新类型指示为UP优化（user plane CIoT EPS optimization），在附着处理成功（发送Attach
Accept消息，如下图A点）或失败（发送Attach Reject消息，如下图B点）后进行统计。 
 


采集方式 :CC 


# C430000153 EPS附着(UP)成功次数 


计数器描述 :在采集周期内统计UP优化的EPS附着成功次数。 


测量触发点 :MME收到Attach Request消息，如果消息中的Attach
Type指示为EPS attach，同时附加更新类型指示为UP优化（user plane CIoT EPS optimization），在附着处理成功（发送Attach
Accept消息，如下图A点）后进行统计。 
 


采集方式 :CC 


# C430000154 EPS附着(SMS Only)请求次数 


计数器描述 :在采集周期内统计SMS Only的EPS附着请求次数。 


测量触发点 :MME收到Attach Request消息，如果消息中的Attach
Type指示为EPS attach，同时附加更新类型指示为SMS Only，在附着处理成功（发送Attach Accept消息，如下图A点）或失败（发送Attach
Reject消息，如下图B点）后进行统计。 
 


采集方式 :CC 


# C430000155 EPS附着(SMS Only)成功次数 


计数器描述 :在采集周期内统计SMS Only的EPS附着成功次数。 


测量触发点 :MME收到Attach Request消息，如果消息中的Attach
Type指示为EPS attach，同时附加更新类型指示为SMS Only，在附着处理成功（发送Attach Accept消息，如下图A点）后进行统计。 
 


采集方式 :CC 


# C430000156 EPS附着(w/o PDN)请求次数 


计数器描述 :在采集周期内统计无PDN连接请求的EPS 附着请求次数。 


测量触发点 :MME收到Attach Request消息，如果附着请求消息中不携带PDN连接请求，在附着处理成功（发送Attach
Accept消息，如下图A点）或失败（发送Attach Reject消息，如下图B点）后进行统计。 
 


采集方式 :CC 


# C430000157 EPS附着(w/o PDN)成功次数 


计数器描述 :在采集周期内统计无PDN连接请求的EPS 附着成功次数。 


测量触发点 :MME收到Attach Request消息，如果附着请求消息中不携带PDN连接请求，在附着处理成功（发送Attach
Accept消息，如下图A点）后进行统计。 
 


采集方式 :CC 


# C430000158 基于N26附着请求次数 


计数器描述 :在测量周期内，统计基于N26接口的附着请求次数。 


测量触发点 :在附着流程中，MME收到Attach Request消息后，当消息中携带UE
STATUS并且MME支持N26接口，MME附着处理成功或失败后进行统计。测量点如图中的A点和B点所示。 



采集方式 :CC 


# C430000159 基于N26附着成功次数 


计数器描述 :在测量周期内，统计基于N26接口的附着成功次数。 


测量触发点 :在附着流程中，MME收到Attach Request消息后，当消息中携带UE
STATUS并且MME支持N26接口，MME附着处理成功后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000160 无N26接口附着请求次数 


计数器描述 :在测量周期内，统计无N26接口的附着请求次数。 


测量触发点 :MME不支持N26接口，在附着流程中，MME收到Attach Request消息后，当消息中携带UE
STATUS，MME附着处理成功或失败后进行统计。测量点如图中的A点和B点所示。 



采集方式 :CC 


# C430000161 无N26接口附着成功次数 


计数器描述 :在测量周期内，统计无N26接口的附着请求成功次数。 


测量触发点 :MME不支持N26接口，在附着流程中，MME收到Attach Request消息后，当消息中携带UE
STATUS，MME支持N26接口，MME附着处理成功后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000162 紧急附着请求次数 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着请求次数。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，紧急附着处理成功或失败后进行统计。测量点如图中的A点和B点所示。 



采集方式 :CC 


# C430000163 紧急附着成功次数 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着成功次数。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Accept消息后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000164 紧急附着失败次数(非法UE) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是非法UE）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Illegal
UE）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000165 紧急附着失败次数(IMEI不接受) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是IMEI不接受）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=IMEI
not accepted）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000166 紧急附着失败次数(非法ME) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是非法ME）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Illegal
ME）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000167 紧急附着失败次数(EPS服务不允许) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是EPS服务不允许）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=EPS
services not allowed）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000168 紧急附着失败次数(EPS服务不允许_用户原因) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是EPS服务不允许_用户原因）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=EPS
services not allowed for user reason）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000169 紧急附着失败次数(EPS服务和非EPS服务不允许) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是EPS服务和非EPS服务不允许）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=EPS
services and non-EPS services not allowed）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000170 紧急附着失败次数(隐式去附着) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是隐式去附着）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Implicitly
detached）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000171 紧急附着失败次数(PLMN不允许) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是PLMN不允许）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=PLMN
not allowed）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000172 紧急附着失败次数(TA不允许) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是TA不允许）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Tracking
Area not allowed）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000173 紧急附着失败次数(该TA不允许漫游) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是该TA不允许漫游）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Roaming
not allowed in this tracking area）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000174 紧急附着失败次数(该PLMN不允许EPS服务) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是该PLMN不允许EPS服务）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=EPS
services not allowed in this PLMN）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000175 紧急附着失败次数(该TA中没有合适的小区) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是该TA中没有合适的小区）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=No
Suitable Cells In tracking area）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000176 紧急附着失败次数(该TA中没有合适的小区_用户原因) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是该TA中没有合适的小区）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=No
Suitable Cells In tracking area）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000177 紧急附着失败次数(网络失败) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是网络失败）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Network
failure）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000178 紧急附着失败次数(ESM失败) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是ESM失败）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=ESM
failure）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000179 紧急附着失败次数(ESM失败_用户原因) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是ESM失败_用户原因）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=ESM
failure for User Reason）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000180 紧急附着失败次数(ESM失败_ODB) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是ESM失败_ODB）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=ESM
failure for ODB）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000181 紧急附着失败次数(拥塞) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是拥塞）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Congestion）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000182 紧急附着失败次数(CSG未授权) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是CSG未授权）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Not
authorized for this CSG）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000183 紧急附着失败次数(请求的业务选项在该PLMN未授权) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是请求的业务选项在该PLMN未授权）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Requested
service option not authorized in this PLMN）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000184 紧急附着失败次数(必选字段无效) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是必选字段无效）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Invalid
mandatory information）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000185 紧急附着失败次数(消息类型缺失或没有实现) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是消息类型缺失或没有实现）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Message
type non-existent or not implemented）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000186 紧急附着失败次数(信息元素不存在或未应用) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是信息元素不存在或未应用）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Information
element non-existent or not implemented）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000187 紧急附着失败次数(条件IE错误) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是条件IE错误）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Conditional
IE error）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000188 紧急附着失败次数(协议错误) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是协议错误）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Protocol
error, unspecified）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000189 紧急附着失败次数(其他原因) 


计数器描述 :在测量周期内，统计附着类型为紧急附着的附着失败次数（其中失败原因是其他原因）。 


测量触发点 :MME收到Attach Request消息，其中EPS attach
type IE指示为EPS emergency attach，在MME向UE发送Attach Reject消息（且Cause=Other
causes）后进行统计。测量点如图中的A点所示。 



采集方式 :CC 


# C430000190 紧急附着建立时长(毫秒) 


计数器描述 :在测量周期内，统计紧急附着建立时长（单位：毫秒）。 


测量触发点 :从MME收到Attach Request消息（其中EPS attach
type IE指示为EPS emergency attach）到MME下发Attach Accept消息的间隔时长（单位：毫秒）为紧急附着建立时长。如下图所示，统计时长为A点到B点的时长。 



采集方式 :CC 


# C430000191 紧急附着完成建立时长(毫秒) 


计数器描述 :在测量周期内，统计紧急附着完成建立时长（单位：毫秒）。 


测量触发点 :MME收到Attach Request消息（其中EPS attach
type IE指示为EPS emergency attach），从MME给UE发送Attach Accept消息开始 
记录，当收到Attach
Complete时统计Attach Accept消息与Attach Complete消息之间的时间差。如下图所示，统计时长为A点到B点的时长。 



采集方式 :CC 


# C430000192 EPS附着(eDRX)请求次数 


计数器描述 :在测量周期内，统计MME从NB-IoT终端收到的Attach Request消息中携带Extended
DRX Parameter信元的次数。区分TA进行统计。 


测量触发点 :在NB-IoT场景下，MME从UE收到Attach Request消息中携带Extended
DRX Parameter信元时，在MME发送Attach Accept或者Attach Reject消息时进行统计。区分TA进行统计，重发消息不统计。触发点如下图A点所示。 



采集方式 :CC 


# C430000193 EPS附着(eDRX)成功次数 


计数器描述 :在测量周期内，统计MME向NB-IoT终端发送的Attach Accept消息中携带Extended
DRX Parameter信元的次数。区分TA进行统计。 


测量触发点 :在NB-IoT场景下，MME向UE发送Attach Accept消息中携带Extended
DRX Parameter信元时，计数器加1。区分TA进行统计，重发消息不统计。 



采集方式 :CC 


