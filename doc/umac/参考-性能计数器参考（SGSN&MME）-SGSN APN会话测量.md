
用于区分APN统计会话时需要创建，SGSN中需要执行[ADD GPRS APN]命令配置GPRS
APN HOST。建议颗粒为15分钟。
# C405180003 每APN由MS发起的PDP上下文激活尝试次数-UMTS 

计数器描述 : 
按APN标识号分类测量SGSN收到MS（Iu口接入）发过来的PDP激活请求的次数。
测量触发点 : 
SGSN接收到MS（Iu口接入）的PDP激活请求，向MS回PDP激活成功时或者激活流程失败时统计。 
采集方式 : 
CC 
# C405180004 每APN由MS发起的PDP上下文激活尝试次数-GSM 

计数器描述 : 
按APN标识号分类测量SGSN收到MS（Gb口接入）发送来的PDP激活请求的次数。 
测量触发点 : 
SGSN接收到MS（Gb口接入）的PDP激活请求，向MS回PDP激活成功时或者激活流程失败时统计。 
采集方式 : 
CC 
# C405180005 每APN由MS发起的PDP上下文激活成功次数-UMTS 

计数器描述 : 
按APN标识号分类测量MS（Iu口接入）发起PDP激活请求的成功次数（根据要求的APN分类测量）。 
测量触发点 : 
SGSN向MS（Iu口接入）发送Activate PDP context
accept时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180006 每APN由MS发起的PDP上下文激活成功次数-GSM 

计数器描述 : 
按APN标识号分类测量MS（Gb口接入）发起PDP激活请求的成功次数（根据要求的APN分类测量）。 
测量触发点 : 
SGSN向MS（Gb口接入）发送Activate PDP context
accept时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180007 每APN由MS去激活会话的请求次数-UMTS 

计数器描述 : 
按APN标识号分类测量MS（Iu口接入）去激活会话的请求次数。 
测量触发点 : 
SGSN给MS（Iu口接入）回PDP去激活成功时或者去激活流程失败时统计。 
采集方式 : 
CC 
# C405180008 每APN由MS去激活会话的请求次数-GSM 

计数器描述 : 
按APN标识号分类测量MS（Gb口接入）去激活会话的请求次数。 
测量触发点 : 
SGSN给MS（Gb口接入）回PDP去激活成功时或者去激活流程失败时统计。 
采集方式 : 
CC 
# C405180009 每APN由MS去激活会话的成功次数-UMTS 

计数器描述 : 
按APN标识号分类测量MS（Iu口接入）去激活会话的成功次数。 
测量触发点 : 
MS（Iu口接入）去激活会话成功，SGSN给MS回去激活接受消息（Deactivate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180010 每APN由MS去激活会话的成功次数-GSM 

计数器描述 : 
按APN标识号分类测量MS（Gb口接入）去激活会话的成功次数。 
测量触发点 : 
MS（Gb口接入）去激活会话成功，SGSN给MS回去激活接受消息（Deactivate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180011 分APN测量MS激活会话建立总时长(毫秒)-UMTS 
计数器描述 : 
按APN标识号分类测量有效MS（Iu口接入）激活会话建立总时长（单位：毫秒）。 
测量触发点 : 
按APN标识号分类测量，累计本统计周期内从SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长。对于跨统计周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180012 分APN测量MS激活会话建立总时长(毫秒)-GSM 
计数器描述 : 
按APN标识号分类测量有效MS（Gb口接入）激活会话建立总时长（单位：毫秒）。 
测量触发点 : 
按APN标识号分类测量，累计本统计周期内从SGSN收到MS（Gb口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长。对于跨统计周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180013 分APN测量MS激活会话最大建立时长(毫秒)-UMTS 
计数器描述 : 
按APN标识号分类测量MS（Iu口接入）激活会话最大建立时长（单位：毫秒）。 
测量触发点 : 
按APN标识号分类测量，统计本测量周期内从SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长的最大值。对于跨测量周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180014 分APN测量MS激活会话最大建立时长(毫秒)-GSM 
计数器描述 : 
按APN标识号分类测量MS（Gb口接入）激活会话最大建立时长（单位：毫秒）。 
测量触发点 : 
按APN标识号分类测量，统计本测量周期内从SGSN收到MS（Gb口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长的最大值。对于跨测量周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180015 分APN测量MS进行PDP上下文激活保持总时长(秒)-UMTS 
计数器描述 : 
按APN标识号分类测量MS（Iu口接入）进行PDP上下文激活保持的总时长。 
测量触发点 : 
该计数器用于计算MS（Iu口接入）的PDP上下文激活保持平均时长。  
采集方式 : 
CC 
# C405180016 分APN测量MS进行PDP上下文激活保持总时长(秒)-GSM 
计数器描述 : 
按APN标识号分类测量MS（Gb口接入）进行PDP上下文激活保持的总时长。 
测量触发点 : 
该计数器用于计算MS（Gb口接入）的PDP上下文激活保持平均时长。  
采集方式 : 
CC 
# C405180019 分APN测量网络激活会话请求次数-UMTS 

计数器描述 : 
按APN标识号分类测量网络对MS（Iu口接入）发起的PDP上下文激活尝试次数。 
测量触发点 : 
按APN标识号分类测量，SGSN收到网络对MS（Iu口接入）发起的PDP上下文激活请求消息（PDU
Notification Request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180020 分APN测量网络激活会话请求次数-GSM 

计数器描述 : 
按APN标识号分类测量网络对MS（Gb口接入）发起的PDP上下文激活尝试次数。 
测量触发点 : 
按APN标识号分类测量，SGSN收到网络对MS（Gb口接入）发起的PDP上下文激活请求消息（PDU
Notification Request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180021 分APN测量网络激活会话成功次数-UMTS 

计数器描述 : 
按APN标识号分类测量，网络对MS（Iu口接入）发起的PDP上下文激活的成功次数。 
测量触发点 : 
按APN标识号分类测量，网络对MS（Iu口接入）发起的PDP上下文激活成功，SGSN向MS发送激活接受消息（Activate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180022 分APN测量网络激活会话成功次数-GSM 

计数器描述 : 
按APN标识号分类测量，网络对MS（Gb口接入）发起的PDP上下文激活的成功次数。 
测量触发点 : 
按APN标识号分类测量，网络对MS（Gb口接入）发起的PDP上下文激活成功，SGSN向MS发送激活接受消息（Activate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180023 分APN测量网络激活会话建立总时长(毫秒)-UMTS 
计数器描述 : 
按APN标识号分类测量针对Iu口接入用户的有效网络激活会话建立总时长（单位：毫秒）。 
测量触发点 : 
按APN标识号分类测量，累计本统计周期内从SGSN收到网络对用户（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长。对于跨测量周期的网络激活会话，网络激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180024 分APN测量网络激活会话建立总时长(毫秒)-GSM 
计数器描述 : 
按APN标识号分类测量针对Gb口接入用户的有效网络激活会话建立总时长（单位：毫秒）。 
测量触发点 : 
按APN标识号分类测量，累计本统计周期内从SGSN收到网络对用户（Gb口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长。对于跨测量周期的网络激活会话，网络激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180025 分APN测量网络激活会话最大建立时长(毫秒)-UMTS 
计数器描述 : 
按APN标识号分类测量针对Iu口接入用户的网络激活会话最大建立时长（单位：毫秒）。 
测量触发点 : 
按APN标识号分类测量，统计本测量周期内从SGSN收到网络对用户（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长的最大值。对于跨测量周期的网络激活会话，网络激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180026 分APN测量网络激活会话最大建立时长(毫秒)-GSM 
计数器描述 : 
按APN标识号分类测量针对Gb口接入用户的网络激活会话最大建立时长（单位：毫秒）。 
测量触发点 : 
按APN标识号分类测量，统计本测量周期内从SGSN收到网络对用户（Gb口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长的最大值。对于跨测量周期的网络激活会话，网络激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180027 分APN测量会话类业务MS激活会话最大建立时间(毫秒) 
计数器描述 : 
按APN标识号分类测量MS（Iu口接入）激活业务类型为会话类业务的最大建立时长（单位：毫秒）。 
测量触发点 : 
针对Qos的业务类型为会话类型的业务，按APN标识号分类测量，统计本测量周期内从SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长的最大值。对于跨测量周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180028 分APN测量流类业务MS激活会话最大建立时间(毫秒) 
计数器描述 : 
按APN标识号分类测量MS（Iu口接入）激活业务类型为流类业务的最大建立时长（单位：毫秒）。 
测量触发点 : 
针对Qos的业务类型为流类型的业务，按APN标识号分类测量，统计本测量周期内从SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长的最大值。对于跨测量周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180029 分APN测量交互类业务MS激活会话最大建立时间(毫秒) 
计数器描述 : 
按APN标识号分类测量MS（Iu口接入）激活业务类型为交互类业务的最大建立时长（单位：毫秒）。 
测量触发点 : 
针对Qos的业务类型为交互类型的业务，按APN标识号分类测量，统计本测量周期内从SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长的最大值。对于跨测量周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180030 分APN测量背景类业务MS激活会话最大建立时间(毫秒) 
计数器描述 : 
按APN标识号分类测量MS（Iu口接入）激活业务类型为背景类业务的最大建立时长（单位：毫秒）。 
测量触发点 : 
针对Qos的业务类型为背景类型的业务，按APN标识号分类测量，统计本测量周期内从SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长的最大值。对于跨测量周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
采集方式 : 
CC 
# C405180031 分APN使用动态地址激活会话2GCN请求次数 

计数器描述 : 
按APN标识号分类测量MS（Gb口接入）使用动态地址激活会话请求次数。 
测量触发点 : 
MS（Gb口接入）发起动态PDP上下文激活请求消息，消息中的PDP地址为空并且通过APN检查，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活流程失败时统计。 
采集方式 : 
CC 
# C405180032 分APN使用动态地址激活会话3GCN请求次数 

计数器描述 : 
按APN标识号分类测量MS（Iu口接入）使用动态地址激活会话请求次数。 
测量触发点 : 
MS（Iu口接入）发起动态PDP上下文激活请求消息，消息中的PDP地址为空并且通过APN检查，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活流程失败时统计。 
采集方式 : 
CC 
# C405180033 分APN使用动态地址激活会话2GCN成功次数 

计数器描述 : 
按APN标识号分类测量MS（Gb口接入）使用动态地址激活会话请求成功次数。 
测量触发点 : 
MS（Gb口接入）发起动态PDP上下文激活成功，SGSN向MS发送激活接受消息（activate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180034 分APN使用动态地址激活会话3GCN成功次数 

计数器描述 : 
按APN标识号分类测量MS（Iu口接入）使用动态地址激活会话请求成功次数。 
测量触发点 : 
MS（Iu口接入）发起动态PDP上下文激活成功，SGSN向MS发送激活接受消息（activate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180035 分APN使用静态地址激活会话请求次数-UMTS 

计数器描述 : 
测量MS（Iu口接入）使用静态地址激活会话请求次数。 
测量触发点 : 
MS（Iu口接入）发起静态PDP上下文激活请求，APN检查通过且地址模式为静态地址，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活失败时统计。 
采集方式 : 
CC 
# C405180036 分APN使用静态地址激活会话请求次数-GSM 

计数器描述 : 
测量MS（2G接入）使用静态地址激活会话请求次数。 
测量触发点 : 
MS（2G接入）发起静态PDP上下文激活请求，APN检查通过且地址模式为静态地址，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活失败时统计。 
采集方式 : 
CC 
# C405180037 分APN使用静态地址激活会话成功次数-UMTS 

计数器描述 : 
测量MS（Iu口接入）发起静态PDP上下文激活的成功次数。 
测量触发点 : 
MS（Iu口接入）发起静态PDP上下文激活成功，SGSN向MS发送激活接受消息（activate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180038 分APN使用静态地址激活会话成功次数-GSM 

计数器描述 : 
测量MS（Gb口接入）发起静态PDP上下文激活的成功次数。 
测量触发点 : 
MS（Gb口接入）发起静态PDP上下文激活成功，SGSN向MS发送激活接受消息（activate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180039 分APN由SGSN发起的去激活会话请求次数-UMTS 

计数器描述 : 
SGSN向MS（Iu口接入）发起去激活会话请求的次数。 
测量触发点 : 
SGSN对MS（Iu口接入）主动发起去激活PDP上下文请求（Deactivate
PDP context request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180040 分APN由SGSN发起的去激活会话请求次数-GSM 

计数器描述 : 
SGSN向MS（Gb口接入）发起去激活会话请求的次数。 
测量触发点 : 
SGSN对MS（Gb口接入）主动发起去激活PDP上下文请求（Deactivate
PDP context request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180041 分APN由SGSN发起的去激活会话的成功次数-UMTS 

计数器描述 : 
SGSN向MS（Iu口接入）发起去激活会话的成功次数。 
测量触发点 : 
SGSN对MS（Iu口接入）主动发起去激活PDP上下文请求成功，SGSN收到MS发来的去激活PDP上下文接受消息（Deactivate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180042 分APN由SGSN发起的去激活会话的成功次数-GSM 

计数器描述 : 
SGSN向MS（Gb口接入）发起去激活会话的成功次数。 
测量触发点 : 
SGSN对MS（Gb口接入）主动发起去激活PDP上下文请求成功，SGSN收到MS发来的去激活PDP上下文接受消息（Deactivate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180043 分APN由GGSN发起的去激活会话的请求次数-UMTS 

计数器描述 : 
GGSN对用户（Iu口接入）发起去激活会话的请求次数。 
测量触发点 : 
针对Iu口接入的用户，SGSN向GGSN返回去激活响应消息（Delete
PDP Context Response）且消息中携带原因值为Request Accepted时，或者GGSN发起的去激活流程失败时统计。 
采集方式 : 
CC 
# C405180044 分APN由GGSN发起的去激活会话的请求次数-GSM 

计数器描述 : 
GGSN对用户（Gb口接入）发起去激活会话的请求次数。 
测量触发点 : 
针对Gb口接入的用户，SGSN向GGSN返回去激活响应消息（Delete
PDP Context Response）且消息中携带原因值为Request Accepted时，或者GGSN发起的去激活流程失败时统计。 
采集方式 : 
CC 
# C405180045 分APN由GGSN发起的去激活会话成功次数-UMTS 

计数器描述 : 
GGSN对用户（Iu口接入）发起去激活会话的成功次数。 
测量触发点 : 
针对Iu口接入的用户，SGSN向GGSN返回去激活响应消息（Delete
PDP Context Response）且消息中携带原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180046 分APN由GGSN发起的去激活会话成功次数-GSM 

计数器描述 : 
GGSN对用户（Gb口接入）发起去激活会话的成功次数。 
测量触发点 : 
针对Gb口接入的用户，SGSN向GGSN返回去激活响应消息（Delete
PDP Context Response）且消息中携带原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180047 分APN二次激活的请求次数-UMTS 

计数器描述 : 
MS （Iu口接入）发起二次激活的请求次数。 
测量触发点 : 
SGSN给MS（Iu口接入）发送二次激活接受消息（Secondary
PDP context accept），或者二次激活流程失败时统计。 
采集方式 : 
CC 
# C405180048 分APN二次激活的请求次数-GSM 

计数器描述 : 
MS （Gb口接入）发起二次激活的请求次数。 
测量触发点 : 
SGSN给MS（Gb口接入）发送二次激活接受消息（Secondary
PDP context accept），或者二次激活流程失败时统计。 
采集方式 : 
CC 
# C405180049 分APN二次激活的成功次数-UMTS 

计数器描述 : 
MS （Iu口接入）发起二次激活的成功次数。 
测量触发点 : 
SGSN给MS （Iu口接入）发送二次激活接受消息（Secondary
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180050 分APN二次激活的成功次数-GSM 

计数器描述 : 
MS （Gb口接入）发起二次激活的成功次数。 
测量触发点 : 
SGSN给MS （Gb口接入）发送二次激活接受消息（Secondary
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180051 分APN由MS发起的修改会话请求次数-UMTS 

计数器描述 : 
MS （Iu口接入）发起修改会话的请求次数。 
测量触发点 : 
SGSN给MS（Iu口接入）发送修改会话接受消息（Modify PDP
context accept），或者MS发起的修改流程失败时统计。 
采集方式 : 
CC 
# C405180052 分APN由MS发起的修改会话请求次数-GSM 

计数器描述 : 
MS （Gb口接入）发起修改会话的请求次数。 
测量触发点 : 
SGSN给MS（Gb口接入）发送修改会话接受消息（Modify PDP
context accept），或者MS发起的修改流程失败时统计。 
采集方式 : 
CC 
# C405180053 分APN由MS发起的修改会话成功次数-UMTS 

计数器描述 : 
MS （Iu口接入）发起修改会话的成功次数。 
测量触发点 : 
SGSN给MS （Iu口接入）发送修改会话接受消息（Modify PDP
Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180054 分APN由MS发起的修改会话成功次数-GSM 

计数器描述 : 
MS （Gb口接入）发起修改会话的成功次数。 
测量触发点 : 
SGSN给MS （Gb口接入）发送修改会话接受消息（Modify PDP
Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180055 分APN由SGSN发起的修改会话的请求次数-UMTS 

计数器描述 : 
SGSN对MS（Iu口接入）发起修改会话的请求次数。 
测量触发点 : 
SGSN收到MS（Iu口接入）发送的修改会话接受消息（Modify
PDP context accept），或者修改失败时统计。 
采集方式 : 
CC 
# C405180056 分APN由SGSN发起的修改会话的请求次数-GSM 

计数器描述 : 
SGSN对MS（Gb口接入）发起修改会话的请求次数。 
测量触发点 : 
SGSN收到MS（Gb口接入）发送的修改会话接受消息（Modify
PDP context accept），或者修改失败时统计。 
采集方式 : 
CC 
# C405180057 分APN由SGSN发起的修改会话的成功次数-UMTS 

计数器描述 : 
SGSN对MS（Iu口接入）发起修改会话的成功次数。 
测量触发点 : 
SGSN收到MS（Iu口接入）发送来的修改会话接受消息（Modify
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180058 分APN由SGSN发起的修改会话的成功次数-GSM 

计数器描述 : 
SGSN对MS（Gb口接入）发起修改会话的成功次数。 
测量触发点 : 
SGSN收到MS（Gb口接入）发送来的修改会话接受消息（Modify
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180059 分APN由GGSN发起的更新会话的请求次数-UMTS 

计数器描述 : 
针对Iu口接入的MS，GGSN向SGSN发起更新会话的请求次数。 
测量触发点 : 
针对Iu口接入的MS，SGSN向GGSN发出更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted，或者更新失败时统计。 
采集方式 : 
CC 
# C405180060 分APN由GGSN发起的更新会话的请求次数-GSM 

计数器描述 : 
针对Gb口接入的MS，GGSN向SGSN发起更新会话的请求次数。 
测量触发点 : 
针对Gb口接入的MS，SGSN向GGSN发出更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted，或者更新失败时统计。 
采集方式 : 
CC 
# C405180061 分APN由GGSN发起的更新会话的成功次数-UMTS 

计数器描述 : 
针对Iu口接入的MS，GGSN向SGSN发起更新会话的成功次数。 
测量触发点 : 
针对Iu口接入的MS，SGSN向GGSN发送更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180062 分APN由GGSN发起的更新会话的成功次数-GSM 

计数器描述 : 
针对Gb口接入的MS，GGSN向SGSN发起更新会话的成功次数。 
测量触发点 : 
针对Gb口接入的MS，SGSN向GGSN发送更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180063 分APN由SGSN发起的更新会话的请求次数-UMTS 

计数器描述 : 
针对Iu口接入的MS，SGSN向GGSN发起更新会话的请求次数。 
测量触发点 : 
针对Iu口接入的MS，SGSN向GGSN发送更新会话请求消息（Update
PDP Context Request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180064 分APN由SGSN发起的更新会话的请求次数-GSM 

计数器描述 : 
针对Gb口接入的MS，SGSN向GGSN发起更新会话的请求次数。 
测量触发点 : 
针对Gb口接入的MS，SGSN向GGSN发送更新会话请求消息（Update
PDP Context Resquest）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180065 分APN由SGSN发起的更新会话的成功次数-UMTS 

计数器描述 : 
针对Iu口接入的MS，SGSN向GGSN发起更新会话的成功次数。 
测量触发点 : 
针对Iu口接入的MS，SGSN收到GGSN发送的更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180066 分APN由SGSN发起的更新会话的成功次数-GSM 

计数器描述 : 
针对Gb口接入的MS，SGSN向GGSN发起更新会话的成功次数。 
测量触发点 : 
针对Gb口接入的MS，SGSN收到GGSN发送的更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180067 分APN由于系统资源不足导致的MS发起PDP上下文激活失败次数-UMTS 

计数器描述 : 
由于系统资源不足导致MS（Iu口接入）发起PDP上下文激活的失败次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发送Active PDP Context
Reject消息且消息中携带Cause Code 26 insufficient resource （3G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180068 分APN由于系统资源不足导致的MS发起PDP上下文激活失败次数-GSM 

计数器描述 : 
由于系统资源不足导致MS（Gb口接入）发起PDP上下文激活的失败次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发送Active PDP Context
Reject消息且消息中携带Cause Code 26 insufficient resource （2G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180069 分APN由于APN丢失或不知道引起的PDP激活失败次数-UMTS 

计数器描述 : 
由于APN丢失或APN未知引起MS（Iu口接入）PDP激活失败次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 27（3G）时统计。 
采集方式 : 
CC 
# C405180070 分APN由于APN丢失或不知道引起的PDP激活失败次数-GSM 

计数器描述 : 
由于APN丢失或APN未知引起MS（Gb口接入）PDP激活失败次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 27（2G）时统计。 
采集方式 : 
CC 
# C405180071 分APN由于未知的PDP地址或PDP类型引起的PDP激活失败次数-UMTS 

计数器描述 : 
用户（Iu口接入）激活请求中所带的PDP地址、PDP类型不合法或者错误引起的激活失败次数。 
测量触发点 : 
SGSN向用户（Iu口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 28 Unknown PDP Address or PDP Type（3G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180072 分APN由于未知的PDP地址或PDP类型引起的PDP激活失败次数-GSM 

计数器描述 : 
用户（Gb口接入）激活请求中所带的PDP地址、PDP类型不合法或者错误引起的激活失败次数。 
测量触发点 : 
SGSN向用户（Gb口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Cause
Code 28 Unknown PDP Address or PDP Type（2G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180073 分APN由于用户鉴权失败引起的PDP激活失败次数-UMTS 

计数器描述 : 
激活过程中由于用户（Iu口接入）鉴权失败而引起的PDP激活失败次数。 
测量触发点 : 
SGSN向用户（Iu口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 29 User Authentication Failed（3G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180074 分APN由于用户鉴权失败引起的PDP激活失败次数-GSM 

计数器描述 : 
激活过程中由于用户（Gb口接入）鉴权失败而引起的PDP激活失败次数。 
测量触发点 : 
SGSN向用户（Gb口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 29 User Authentication Failed（2G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180075 分APN由于GGSN拒绝接入引起的激活失败次数-UMTS 

计数器描述 : 
由于GGSN拒绝接入引起MS（Iu口接入）激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 30 activation rejected by GGSN时统计。 
采集方式 : 
CC 
# C405180076 分APN由于GGSN拒绝接入引起的激活失败次数-GSM 

计数器描述 : 
由于GGSN拒绝接入引起MS（Gb口接入）激活失败的次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 30 activation rejected by GGSN时统计。 
采集方式 : 
CC 
# C405180077 分APN由于未定义原因的PDP激活失败次数-UMTS 

计数器描述 : 
由于未定义原因引起MS（Iu口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 31 activation rejected, unspecified （3G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180078 分APN由于未定义原因的PDP激活失败次数-GSM 

计数器描述 : 
由于未定义原因引起MS（Gb口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 31 activation rejected, unspecified （2G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180079 分APN由于不支持的请求业务引起的PDP激活失败次数-UMTS 

计数器描述 : 
由于SGSN不支持的请求业务引起MS（Iu口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 32 Service Option Not Supported（3G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180080 分APN由于不支持的请求业务引起的PDP激活失败次数-GSM 

计数器描述 : 
由于SGSN不支持的请求业务引起MS（Gb口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 32 Service Option Not Supported（2G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
采集方式 : 
CC 
# C405180081 分APN由于选择的服务乱序导致的激活失败次数-UMTS 

计数器描述 : 
由于流程冲突导致MS（Iu口接入）激活失败次数。 
测量触发点 : 
MS（Iu口接入）发起RAU流程或其他用户级流程，在流程未结束时发起激活请求，产生冲突导致激活失败时统计。 
采集方式 : 
CC 
# C405180082 分APN由于选择的服务乱序导致的激活失败次数-GSM 

计数器描述 : 
由于流程冲突导致MS（Gb口接入）激活失败次数。 
测量触发点 : 
MS（Gb口接入）发起RAU流程或其他用户级流程，在流程未结束时发起激活请求，产生冲突导致激活失败时统计。 
采集方式 : 
CC 
# C405180083 分APN由于NSAPI已被使用导致的激活失败次数-UMTS 

计数器描述 : 
由于NSAPI已被使用导致MS（Iu口接入）PDP上下文激活失败次数。 
测量触发点 : 
MS（Iu口接入）激活请求带上NSAPI，而网络侧已有该用户相同NSAPI的PDP上下文导致激活失败时统计。 
采集方式 : 
CC 
# C405180084 分APN由于NSAPI已被使用导致的激活失败次数-GSM 

计数器描述 : 
由于NSAPI已被使用导致MS（Gb口接入）PDP上下文激活失败次数。 
测量触发点 : 
MS（Gb口接入）激活请求带上NSAPI，而网络侧已有该用户相同NSAPI的PDP上下文导致激活失败时统计。 
采集方式 : 
CC 
# C405180085 分APN由于协议错误导致的激活失败次数-UMTS 

计数器描述 : 
由于协议规定的参数错误导致MS（Iu口接入）激活失败的次数。 
测量触发点 : 
SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）且消息中的必选参数NSAPI 或SAPI或Qos不符合协议规定值，SGSN给MS发送激活拒绝的Cause
Code为95~111时统计。 
采集方式 : 
CC 
# C405180086 分APN由于协议错误导致的激活失败次数-GSM 

计数器描述 : 
由于协议规定的参数错误导致MS（Gb口接入）激活失败的次数。 
测量触发点 : 
SGSN收到MS（Gb口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）且消息中的必选参数NSAPI 或SAPI或Qos不符合协议规定值，SGSN给MS发送激活拒绝的Cause
Code为95~111时统计。 
采集方式 : 
CC 
# C405180087 分APN未分类原因的PDP激活失败次数-UMTS 

计数器描述 : 
未分类原因引起MS（Iu口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求的消息，且导致拒绝的原因不为该测量类型下其他PDP激活失败计数器对应的原因（包括用户参数不对、APN丢失或不知道、系统资源不足、未知的PDP地址或PDP类型、用户鉴权失败、不支持的请求业务、ODB、选择的服务乱序、NSAPI已被使用、协议错误等）时统计。 
采集方式 : 
CC 
# C405180088 分APN未分类原因的PDP激活失败次数-GSM 

计数器描述 : 
未分类原因引起MS（Iu口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求的消息，且导致拒绝的原因不为该测量类型下其他PDP激活失败计数器对应的原因（包括用户参数不对、APN丢失或不知道、系统资源不足、未知的PDP地址或PDP类型、用户鉴权失败、不支持的请求业务、ODB、选择的服务乱序、NSAPI已被使用、协议错误等）时统计。 
采集方式 : 
CC 
# C405180089 分APN由于SGSN内部原因导致的激活失败次数-UMTS 

计数器描述 : 
由于SGSN内部原因导致MS（Iu口接入）激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且该拒绝消息是由于SGSN内部原因（例如用户面资源不足）引起时统计。 
采集方式 : 
CC 
# C405180090 分APN由于SGSN内部原因导致的激活失败次数-GSM 

计数器描述 : 
由于SGSN内部原因导致MS（Gb口接入）激活失败的次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且该拒绝消息是由于SGSN内部原因（例如用户面资源不足）引起时统计。 
采集方式 : 
CC 
# C405180091 分APN由于ODB引起的PDP激活失败次数-UMTS 

计数器描述 : 
由于ODB引起MS（Iu口接入）PDP激活失败的次数。 
测量触发点 : 
MS（Iu口接入）在激活过程中，由于ODB原因而激活失败， SGSN向MS发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 8 Operator Determined Barring（3G）时统计。 
采集方式 : 
CC 
# C405180092 分APN由于ODB引起的PDP激活失败次数-GSM 

计数器描述 : 
由于ODB引起MS（Gb口接入）PDP激活失败的次数。 
测量触发点 : 
MS（Gb口接入）在激活过程中，由于ODB原因而激活失败， SGSN向MS发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 8 Operator Determined Barring（2G）时统计。 
采集方式 : 
CC 
# C405180093 分APN由于用户参数不对引起的PDP失败的次数-UMTS 

计数器描述 : 
用户（Iu口接入）参数不对引起PDP失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 33（3G）时统计。 
采集方式 : 
CC 
# C405180094 分APN由于用户参数不对引起的PDP失败的次数-GSM 

计数器描述 : 
用户（Gb口接入）参数不对引起PDP失败的次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 33（2G）时统计。 
采集方式 : 
CC 
# C405180095 分APN由于QoS不接受的激活失败次数-UMTS 

计数器描述 : 
由于QoS不接受导致MS（Iu口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝原因为QoS
not accepted（0X25），导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405180096 分APN由于QoS不接受的激活失败次数-GSM 

计数器描述 : 
由于QoS不接受导致MS（Gb口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝原因为QoS
not accepted（0X25），导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405180097 分APN由于网络失败的激活失败次数-UMTS 

计数器描述 : 
网络失败导致MS（Iu口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝原因为Network
failure（0X26），导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405180098 分APN由于网络失败的激活失败次数-GSM 

计数器描述 : 
网络失败导致MS（Gb口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝原因为Network
failure（0X26），导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405180099 分APN由于TFT错误的激活失败次数-UMTS 

计数器描述 : 
由于TFT错误导致MS（Iu口接入）PDP激活失败的次数。 
测量触发点 : 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝原因为：Semantic
error in the TFT operation（0X29）、Syntactical error in the TFT operation（0X2A）、Semantic
errors in packet filter(s  （0X2C）、Syntactical errors in packet filter(s
 （0X2D）或PDP context without TFT already activated（0X2E），导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405180100 分APN由于TFT错误的激活失败次数-GSM 

计数器描述 : 
由于TFT错误导致MS（Gb口接入）激活失败的次数。 
测量触发点 : 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝原因为：Semantic
error in the TFT operation（0X29）、Syntactical error in the TFT operation（0X2A）、Semantic
errors in packet filter(s  （0X2C）、Syntactical errors in packet filter(s
 （0X2D）或PDP context without TFT already activated（0X2E），导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405180101 分APN未知的PDP上下文原因引起的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计用户3G接入，二次激活过程中未知的PDP上下文原因导致二次激活失败次数。 
测量触发点 : 
MS（3G接入）/网络发起二次PDP上下文激活，SGSN在激活二次PDP拒绝消息中指示Cause
Code和原因为：Caused Code 43：unknown PDP context时，进行统计。 
采集方式 : 
CC 
# C405180102 分APN未知的PDP上下文原因引起的PDP激活失败次数-GSM 

计数器描述 : 
根据APN来统计用户2G接入，二次激活过程中未知的PDP上下文原因导致二次激活失败次数。 
测量触发点 : 
MS（2G接入）/网络发起二次PDP上下文激活，SGSN在激活二次PDP拒绝消息中指示Cause
Code和原因为：Caused Code 43：unknown PDP context时，进行统计。 
采集方式 : 
CC 
# C405180103 分APN由于语义错误消息导致的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计由于语义错误消息导致的PDP激活失败次数-UMTS。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 95：Semantically incorrect message时，进行统计。 
采集方式 : 
CC 
# C405180104 分APN由于语义错误消息导致的PDP激活失败次数-GSM 

计数器描述 : 
根据APN来统计由于语义错误消息导致的PDP激活失败次数-GSM。 
测量触发点 : 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 95：Semantically incorrect message时，进行统计。 
采集方式 : 
CC 
# C405180105 分APN由于无效的强制性信息导致的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计由于无效的强制性信息导致的PDP激活失败次数-UMTS。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 96：Invalid mandatory information时，进行统计。 
采集方式 : 
CC 
# C405180106 分APN由于无效的强制性信息导致的PDP激活失败次数-GSM 

计数器描述 : 
根据APN来统计由于无效的强制性信息导致的PDP激活失败次数-GSM。 
测量触发点 : 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 96：Invalid mandatory information时，进行统计。 
采集方式 : 
CC 
# C405180107 分APN由于消息类型不存在或不能实现导致的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计由于消息类型不存在或不能实现导致的PDP激活失败次数-UMTS。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 97：Message type non-existent or not implemented时，进行统计。 
采集方式 : 
CC 
# C405180108 分APN由于消息类型不存在或不能实现导致的PDP激活失败次数-GSM 

计数器描述 : 
统计由于消息类型不存在或不能实现导致的PDP激活失败次数-GSM。 
测量触发点 : 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 97：Message type non-existent or not implemented时，进行统计。 
采集方式 : 
CC 
# C405180109 分APN由于消息类型与协议状态不兼容导致的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计由于消息类型与协议状态不兼容导致的PDP激活失败次数-UMTS。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 98：Message type not compatible with the protocol state时，进行统计。 
采集方式 : 
CC 
# C405180110 分APN由于消息类型与协议状态不兼容导致的PDP激活失败次数-GSM 

计数器描述 : 
根据APN来统计由于消息类型与协议状态不兼容导致的PDP激活失败次数-GSM。 
测量触发点 : 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 98：Message type not compatible with the protocol state时，进行统计。 
采集方式 : 
CC 
# C405180111 分APN由于信息单元不存在或不能实现导致的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计由于信息单元不存在或不能实现导致的PDP激活失败次数-UMTS。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 99：Information element non-existent or not implemented时，进行统计。 
采集方式 : 
CC 
# C405180112 分APN由于信息单元不存在或不能实现导致的PDP激活失败次数-GSM 

计数器描述 : 
根据APN来统计由于信息单元不存在或不能实现导致的PDP激活失败次数-GSM。 
测量触发点 : 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 99：Information element non-existent or not implemented时，进行统计。 
采集方式 : 
CC 
# C405180113 分APN由于IE错误条件导致的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计由于IE错误条件导致的PDP激活失败次数-UMTS。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 100：Conditional IE error时，进行统计。 
采集方式 : 
CC 
# C405180114 分APN由于IE错误条件导致的PDP激活失败次数-GSM 

计数器描述 : 
根据APN来统计由于IE错误条件导致的PDP激活失败次数-GSM。 
测量触发点 : 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 100：Conditional IE error时，进行统计。 
采集方式 : 
CC 
# C405180115 分APN由于消息不兼容协议状态导致的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计由于消息不兼容协议状态导致的PDP激活失败次数-UMTS。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 101：Message not compatible with the protocol state时，进行统计。 
采集方式 : 
CC 
# C405180116 分APN由于消息不兼容协议状态导致的PDP激活失败次数-GSM 

计数器描述 : 
根据APN来统计由于消息不兼容协议状态导致的PDP激活失败次数-GSM。 
测量触发点 : 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 101：Message not compatible with the protocol state时，进行统计。 
采集方式 : 
CC  
# C405180117 分APN由于协议错误未指定导致的PDP激活失败次数-UMTS 

计数器描述 : 
根据APN来统计由于协议错误未指定导致的PDP激活失败次数-UMTS。 
测量触发点 : 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 111：Protocol error, unspecified时，进行统计。 
采集方式 : 
CC 
# C405180118 分APN由于协议错误未指定导致的PDP激活失败次数-GSM 

计数器描述 : 
根据APN来统计由于协议错误未指定导致的PDP激活失败次数-GSM。 
测量触发点 : 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 111：Protocol error, unspecified时，进行统计。 
采集方式 : 
CC 
# C405180119 分APN SGSN去激活会话请求次数(重激活原因)-UMTS 
计数器描述 : 
根据APN来统计由于重激活原因引起的SGSN向MS（3G接入）发起的去激活会话请求次数。 
测量触发点 : 
SGSN向MS（3G接入）发起PDP去激活请求的消息，消息中指示Cause
Code和原因为：Caused Code 39：reactivation requested（3G）时，进行统计。 
采集方式 : 
CC 
# C405180120 分APN SGSN去激活会话请求次数(重激活原因)-GSM 
计数器描述 : 
根据APN来统计由于重激活原因引起的SGSN向MS（2G接入）发起的去激活会话请求次数。 
测量触发点 : 
SGSN向MS（2G接入）发起PDP去激活请求的消息，消息中指示Cause
Code和原因为：Caused Code 39：reactivation requested（2G）时，进行统计。 
采集方式 : 
CC 
# C405180121 每APN由MS发起的PDP上下文激活成功次数(只允许IPv4的PDP类型)-UMTS 
计数器描述 : 
根据APN来统计MS（3G接入）发起双栈的PDP上下文激活，只允许IPv4的PDP类型的PDP激活成功次数。 
测量触发点 : 
MS（3G接入）发起双栈的PDP上下文激活请求，SGSN只允许IPv4的PDP类型的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 50：PDP type IPv4 only allowed（3G）时，进行统计。 
采集方式 : 
CC 
# C405180122 每APN由MS发起的PDP上下文激活成功次数(只允许IPv4的PDP类型)-GSM 
计数器描述 : 
根据APN来统计MS（2G接入）发起双栈的PDP上下文激活，只允许IPv4的PDP类型的PDP激活成功次数。 
测量触发点 : 
MS（2G接入）发起双栈的PDP上下文激活请求，SGSN只允许IPv4的PDP类型的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 50：PDP type IPv4 only allowed（2G））时，进行统计。 
采集方式 : 
CC 
# C405180123 每APN由MS发起的PDP上下文激活成功次数(只允许IPv6的PDP类型)-UMTS 
计数器描述 : 
根据APN来统计MS（3G接入）发起双栈的PDP上下文激活，只允许IPv6的PDP类型的PDP激活成功次数。 
测量触发点 : 
MS（3G接入）发起双栈的PDP上下文激活请求，SGSN只允许IPv6的PDP类型的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 51：PDP type IPv6 only allowed（3G）时，进行统计。 
采集方式 : 
CC 
# C405180124 每APN由MS发起的PDP上下文激活成功次数(只允许IPv6的PDP类型)-GSM 
计数器描述 : 
根据APN来统计MS（2G接入）发起双栈的PDP上下文激活，只允许IPv6的PDP类型的PDP激活成功次数。 
测量触发点 : 
MS（2G接入）发起双栈的PDP上下文激活请求，SGSN只允许IPv6的PDP类型的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 51：PDP type IPv6 only allowed（2G）时，进行统计。 
采集方式 : 
CC 
# C405180125 每APN由MS发起的PDP上下文激活成功次数(只允许单地址承载)-UMTS 
计数器描述 : 
根据APN来统计MS（3G接入）发起双栈的PDP上下文激活，只允许单地址承载的PDP激活成功次数。 
测量触发点 : 
MS（3G接入）发起双栈的PDP上下文激活请求，SGSN只允许单地址承载的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 52：Single address bearers only
allowed（3G）时，进行统计。 
采集方式 : 
CC 
# C405180126 每APN由MS发起的PDP上下文激活成功次数(只允许单地址承载)-GSM 
计数器描述 : 
根据APN来统计MS（2G接入）发起双栈的PDP上下文激活，只允许单地址承载的PDP激活成功次数。 
测量触发点 : 
MS（2G接入）发起双栈的PDP上下文激活请求，SGSN只允许单地址承载的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 52：Single address bearers only
allowed（2G）时，进行统计。 
采集方式 : 
CC 
# C405180127 每APN MS激活会话成功次数(会话类)-UMTS 

计数器描述 : 
采集周期内区分APN统计MS激活会话成功次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180128 每APN MS激活会话成功次数(流类)-UMTS 

计数器描述 : 
采集周期内区分APN统计激活会话（流类）成功次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180129 每APN MS激活会话成功次数(交互类THP 1)-UMTS 

计数器描述 : 
采集周期内区分APN统计激活会话（交互类THP 1）成功次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180130 每APN MS激活会话成功次数(交互类THP 2)-UMTS 

计数器描述 : 
采集周期内区分APN统计激活会话（交互类THP 2）成功次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180131 每APN MS激活会话成功次数(交互类THP 3)-UMTS 

计数器描述 : 
采集周期内区分APN统计激活会话（交互类THP 3）成功次数（针对3G用户统计）. 
测量触发点 : 
（针对3G用户统计） SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180132 每APN MS激活会话成功次数(背景类)-UMTS 

计数器描述 : 
采集周期内区分APN统计激活会话（背景类）成功次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计） SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180133 每APN由于超时导致的PDP激活失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于超时导致的PDP激活失败次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）无线侧、网络侧、CAMEL超时导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405180134 每APN MS激活会话建立最小时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计激活会话建立最小时长（毫秒）（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）流程成功时间（SGSN发送Activate PDP
Context Accept）与流程开始时间（SGSN收到Activate PDP Context Request）之差为MS发起的激活会话时长，一个周期结束时区分APN统计本周期内激活会话时长的总和。 
采集方式 : 
MIN 
# C405180135 每APN MS激活会话成功次数(会话类)-GSM 

计数器描述 : 
采集周期内区分APN统计激活会话（会话类）成功次数（针对2G用户统计）。 
测量触发点 : 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180136 每APN MS激活会话成功次数(流类)-GSM 

计数器描述 : 
采集周期内区分APN统计激活会话（流类）成功次数（针对2G用户统计）。 
测量触发点 : 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180137 MS激活会话成功次数(交互类THP 1)-GSM 

计数器描述 : 
采集周期内区分APN统计激活会话（交互类THP 1）成功次数（针对2G用户统计）。 
测量触发点 : 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 
采集方式 : 
CC 
# C405180138 每APN MS激活会话成功次数(交互类THP 2)-GSM 

计数器描述 : 
采集周期内区分APN统计激活会话成功次数（交互类THP 2）（针对2G用户统计）。 
测量触发点 : 
（针对2G用户统计） SGSN发送PDP激活成功时统计 
采集方式 : 
CC 
# C405180139 每APN MS激活会话成功次数(交互类THP 3)-GSM 

计数器描述 : 
采集周期内区分APN统计激活会话成功次数（交互类THP 3）（针对2G用户统计）。 
测量触发点 : 
（针对2G用户统计） SGSN发送PDP激活成功时统计 
采集方式 : 
CC 
# C405180140 每APN MS激活会话成功次数(背景类)-GSM 

计数器描述 : 
采集周期内区分APN统计激活会话成功次数（背景类）（针对2G用户统计）。 
测量触发点 : 
（针对2G用户统计） SGSN发送PDP激活成功时统计 
采集方式 : 
CC 
# C405180141 每APN由于超时导致的PDP激活失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计超时导致的PDP激活失败次数（针对2G用户统计）。 
测量触发点 : 
（针对2G用户统计）无线侧、网络侧、CAMEL超时导致PDP激活失败时统计。 
采集方式 : 
CC 
# C405180142 每APN MS激活会话建立最小时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计激活会话建立最小时长（毫秒）（针对2G用户统计）。 
测量触发点 : 
（针对2G用户统计） 流程成功时间（SGSN发送Activate PDP
Context Accept）与流程开始时间（SGSN收到Activate PDP Context Request）之差为MS发起的激活会话时长，一个周期结束时区分APN统计本周期内激活会话时长的总和。 
采集方式 : 
MIN 
# C405180143 每APN QoS不接受导致的MS修改会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计QoS不接受导致的MS修改会话失败次数（针对3G用户统计）。 
测量触发点 : 
（针对3G用户统计）MS发起修改PDP，无线侧或网络侧QoS修改不接受时统计。 
采集方式 : 
CC 
# C405180144 每APN未知的PDP上下文原因导致的MS修改会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计MS发起修改PDP流程，由于未找到上下文导致的流程失败次数（针对3G用户统计）。 
测量触发点 : 
MS发起修改PDP流程，未找到上下文时统计（针对3G用户统计）。 
采集方式 : 
CC 
# C405180145 每APN由于内部错误/限制导致的MS修改会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致的MS发起修改PDP流程失败次数（针对3G用户统计）。 
测量触发点 : 
MS发起修改PDP流程，内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180146 每APN由于其他原因导致的MS修改会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致的MS发起修改PDP流程失败次数（针对3G用户统计）。 
测量触发点 : 
MS发起修改PDP流程，由于其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180147 每APN MS修改会话总时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计MS发起的修改PDP流程总时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为MS发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内MS发起的修改PDP流程时长的总和。 
采集方式 : 
CC 
# C405180148 每APN MS修改会话最大时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计MS发起修改PDP流程最大时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为MS发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内MS发起的修改PDP流程时长的最大值。 
采集方式 : 
MAX 
# C405180149 每APN MS修改会话最小时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计MS发起修改PDP流程最小时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为MS发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内MS发起的修改PDP流程时长的最小值。 
采集方式 : 
MIN 
# C405180150 每APN UE无响应导致的MS修改会话失败次数-UMTS 
计数器描述 : 
采集周期内区分APN统计由于网络失败导致的MS发起的修改会话流程失败次数（针对3G用户统计）。 
测量触发点 : 
SGSN发起修改PDP流程，终端无响应导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180151 每APN由于内部错误/限制导致的SGSN修改会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致的SGSN发起修改PDP流程失败次数（针对3G用户统计）。 
测量触发点 : 
SGSN发起修改PDP流程，内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180152 每APN由于其他原因导致的SGSN修改会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致的SGSN发起修改PDP流程失败次数（针对3G用户统计）。 
测量触发点 : 
SGSN发起修改PDP流程，其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180153 每APN SGSN修改会话总时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计SGSN发起修改PDP流程总时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为SGSN发起的修改PDP流程的时长，一个周期结束时区分APN统计本周期内SGSN发起的修改PDP流程时长的总和。 
采集方式 : 
CC 
# C405180154 每APN SGSN修改会话最大时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计SGSN发起修改PDP流程最大时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为SGSN发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内SGSN发起的修改PDP流程时长的最大值。 
采集方式 : 
MAX 
# C405180155 每APN SGSN修改会话最小时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计SGSN发起修改PDP流程最小时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为SGSN发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内SGSN发起的修改PDP流程时长的最小值。 
采集方式 : 
MIN 
# C405180156 每APN系统失败导致的GGSN更新会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于系统原因导致的GGSN发起更新PDP流程失败次数（针对3G用户统计）。 
测量触发点 : 
GGSN发起更新PDP流程，由于系统原因导致流程失败时统计。 
采集方式 : 
CC 
# C405180157 每APN由于内部错误/限制导致的GGSN更新会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致GGSN发起更新PDP流程的失败次数（针对3G用户统计）。 
测量触发点 : 
GGSN发起更新PDP流程，由于内部错误/限制导致流程失败时统计。 
采集方式 : 
CC 
# C405180158 每APN由于其他原因导致的GGSN修改会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致GGSN发起更新PDP流程的失败次数（针对3G用户统计）。 
测量触发点 : 
GGSN发起更新PDP流程，由于其他原因导致流程失败时统计。 
采集方式 : 
CC 
# C405180159 每APN GGSN更新会话总时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计GGSN发起修改PDP流程总长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为GGSN发起的修改PDP流程的时长，一个周期结束时区分APN统计本周期内GGSN发起的修改PDP流程时长的总和。 
采集方式 : 
CC 
# C405180160 每APN GGSN更新会话最大时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计GGSN发起修改PDP流程最大时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为GGSN发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内GGSN发起的修改PDP流程时长的最大值。 
采集方式 : 
MAX 
# C405180161 每APN GGSN更新会话最小时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计GGSN发起修改PDP流程最小时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为GGSN发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内GGSN发起的修改PDP流程时长的最小值。 
采集方式 : 
MIN 
# C405180162 每APN QoS不接受导致的MS修改会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于QoS不接受导致MS发起修改PDP流程的失败次数（针对2G用户统计）。 
测量触发点 : 
MS发起修改PDP流程，由于QoS不接受导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180163 每APN未知的PDP上下文原因导致的MS修改会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于找不到PDP上下文导致MS发起修改PDP流程的失败次数（针对2G用户统计）。 
测量触发点 : 
MS发起修改PDP流程，由于找不到PDP上下文导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180164 每APN由于内部错误/限制导致的MS修改会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致MS发起修改PDP流程的失败次数（针对2G用户统计）。 
测量触发点 : 
MS发起修改PDP流程，由于内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180165 每APN由于其他原因导致的MS修改会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致MS发起修改PDP流程的失败次数（针对2G用户统计）。 
测量触发点 : 
S发起修改PDP流程，由于其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180166 每APN MS修改会话总时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计MS发起修改PDP流程总时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为MS发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内MS发起的修改PDP流程时长的总和。 
采集方式 : 
CC 
# C405180167 每APN MS修改会话最大时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计MS发起修改PDP流程最大时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为MS发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内MS发起的修改PDP流程时长的最大值。 
采集方式 : 
MAX 
# C405180168 每APN MS修改会话最小时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计MS发起修改PDP流程最小时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为MS发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内MS发起的修改PDP流程时长的最小值。 
采集方式 : 
MIN 
# C405180169 每APN UE无响应导致的MS修改会话失败次数-GSM 
计数器描述 : 
采集周期内区分APN统计由于UE无响应导致SGSN发起的修改PDP流程失败的次数（针对2G用户统计）。 
测量触发点 : 
SGSN发起修改PDP流程，由于UE无响应导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180170 每APN由于内部错误/限制导致的SGSN修改会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致SGSN发起的修改PDP流程失败次数（针对2G用户统计）。 
测量触发点 : 
SGSN发起修改PDP流程，由于内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180171 每APN由于其他原因导致的SGSN修改会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于其他原因SGSN发起的修改PDP流程失败次数（针对2G用户统计）。 
测量触发点 : 
SGSN发起修改PDP流程，由于其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180172 每APN SGSN修改会话总时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计SGSN发起修改PDP流程总时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为SGSN发起的修改PDP流程的时长，一个周期结束时区分APN统计本周期内SGSN发起的修改PDP流程时长的总和。 
采集方式 : 
CC 
# C405180173 每APN SGSN修改会话最大时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计SGSN发起修改PDP流程最大时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为SGSN发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内SGSN发起的修改PDP流程时长的最大值。 
采集方式 : 
MAX 
# C405180174 每APN SGSN修改会话最小时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计SGSN发起修改PDP流程最小时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为SGSN发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内SGSN发起的修改PDP流程时长的最小值。 
采集方式 : 
MIN 
# C405180175 每APN系统失败导致的GGSN更新会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于系统失败导致GGSN发起的修改PDP流程失败次数（针对2G用户统计）。 
测量触发点 : 
GGSN发起修改PDP流程，由于系统失败导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180176 每APN由于内部错误/限制导致的GGSN更新会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致GGSN发起的修改PDP流程失败次数（针对2G用户统计）。 
测量触发点 : 
GGSN发起修改PDP流程，由于内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180177 每APN由于其他原因导致的GGSN修改会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致GGSN发起的修改PDP流程失败次数（针对2G用户统计）。 
测量触发点 : 
GGSN发起修改PDP流程，由于其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180178 每APN GGSN更新会话总时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计GGSN发起修改PDP流程总时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为GGSN发起的修改PDP流程的时长，一个周期结束时区分APN统计本周期内GGSN发起的修改PDP流程时长的总和。 
采集方式 : 
CC 
# C405180179 每APN GGSN更新会话最大时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计GGSN发起修改PDP流程最大时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为GGSN发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内GGSN发起的修改PDP流程时长的最大值。 
采集方式 : 
MAX 
# C405180180 每APN GGSN更新会话最小时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计GGSN发起修改PDP流程最小时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间与流程开始时间之差为GGSN发起修改PDP流程的时长，一个周期结束时区分APN统计本周期内GGSN发起的修改PDP流程时长的最小值。 
采集方式 : 
MIN 
# C405180181 每APN协议错误导致的MS去激活会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于协议错误导致MS发起的去激活流程失败次数（针对3G用户统计）。 
测量触发点 : 
MS发起去激活流程，由于协议错误导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180182 每APN由于内部错误/限制导致的MS去激活会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致MS发起的去激活流程失败次数（针对3G用户统计）。 
测量触发点 : 
MS发起去激活流程，由于内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180183 每APN由于其他原因导致的MS去激活会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致MS发起的去激活流程失败次数（针对3G用户统计）。 
测量触发点 : 
MS发起去激活流程，由于其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180184 每APN MS去激活会话总时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计MS发起去激活流程总时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为MS发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程的总时长。 
采集方式 : 
CC 
# C405180185 每APN MS去激活会话最大时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计MS发起去激活流程最大时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为MS发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程时长的最大值。 
采集方式 : 
MAX 
# C405180186 每APN MS去激活会话最小时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计MS发起去激活流程最小时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为MS发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程时长的最小值。 
采集方式 : 
MIN 
# C405180187 每APN SGSN去激活会话总时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计SGSN发起去激活流程总时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为SGSN发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程的总时长。 
采集方式 : 
CC 
# C405180188 每APN SGSN去激活会话最大时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计SGSN发起去激活流程最大时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为SGSN发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程时长的最大值。 
采集方式 : 
MAX 
# C405180189 每APN SGSN去激活会话最小时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计SGSN发起去激活流程最小时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为SGSN发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程时长的最小值。 
采集方式 : 
MIN 
# C405180190 每APN必选IE未携带导致的GGSN去激活会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于必选IE未携带导致GGSN发起的去激活流程失败次数（针对3G用户统计）。 
测量触发点 : 
GGSN发起去激活流程，由于必选IE未携带导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180191 每APN由于内部错误/限制导致的GGSN去激活会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致GGSN发起的去激活流程失败次数（针对3G用户统计）。 
测量触发点 : 
GGSN发起去激活流程，由于内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180192 每APN由于其他原因导致的GGSN去激活会话失败次数-UMTS 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致GGSN发起的去激活流程失败次数（针对3G用户统计）。 
测量触发点 : 
GGSN发起去激活流程，由于其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180193 每APN GGSN去激活会话总时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计GGSN发起去激活流程总时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为GGSN发起去激活流程总时长 
采集方式 : 
CC 
# C405180194 每APN GGSN去激活会话最大时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计GGSN发起去激活流程最大时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为GGSN发起去激活流程总时长，一个周期结束时取本周期内最大的时长 
采集方式 : 
MAX 
# C405180195 每APN GGSN去激活会话最小时长(毫秒)-UMTS 

计数器描述 : 
采集周期内区分APN统计GGSN发起去激活流程最小时长（针对3G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为GGSN发起去激活流程总时长，一个周期结束时取本周期内最小的时长 
采集方式 : 
MIN 
# C405180196 每APN协议错误导致的MS去激活会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于协议错误导致的MS去激活会话流程失败次数（针对2G用户统计）。 
测量触发点 : 
MS发起去激活PDP请求流程，由于协议错误导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180197 每APN由于内部错误/限制导致的MS去激活会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致的MS去激活会话流程失败次数（针对2G用户统计）。 
测量触发点 : 
MS发起去激活PDP请求流程，由于内部错误/限制导致导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180198 每APN由于其他原因导致的MS去激活会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致的MS去激活会话流程失败失败次数（针对2G用户统计）。 
测量触发点 : 
MS发起去激活PDP请求流程，其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180199 每APN MS去激活会话总时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计MS发起去激活流程总时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为MS发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程的总时长。 
采集方式 : 
CC 
# C405180200 每APN MS去激活会话最大时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计MS发起去激活流程最大时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为MS发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程时长的最大值。 
采集方式 : 
MAX 
# C405180201 每APN MS去激活会话最小时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计MS发起去激活流程最小时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为MS发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程时长的最小值。 
采集方式 : 
MIN 
# C405180202 每APN SGSN去激活会话总时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计SGSN发起去激活流程总时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为SGSN发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程的总时长。 
采集方式 : 
CC 
# C405180203 每APN SGSN去激活会话最大时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计SGSN发起去激活流程最大时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为SGSN发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程时长的最大值。 
采集方式 : 
MAX 
# C405180204 每APN SGSN去激活会话最小时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计SGSN发起去激活流程最小时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为SGSN发起的去激活流程时长，一个周期结束时区分APN统计MS发起的去激活流程时长的最小值。 
采集方式 : 
MIN 
# C405180205 每APN必选IE未携带导致的GGSN去激活会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于必选IE未携带导致GGSN发起的去激活流程失败次数（针对2G用户统计）。 
测量触发点 : 
GGSN发起去激活流程，由于必选IE未携带导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180206 每APN由于内部错误/限制导致的GGSN去激活会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于内部错误/限制导致GGSN发起的去激活流程失败次数（针对2G用户统计）。 
测量触发点 : 
GGSN发起去激活流程，由于内部错误/限制导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180207 每APN由于其他原因导致的GGSN去激活会话失败次数-GSM 

计数器描述 : 
采集周期内区分APN统计由于其他原因导致GGSN发起的去激活流程失败次数（针对2G用户统计）。 
测量触发点 : 
GGSN发起去激活流程，由于其他原因导致流程失败时进行统计。 
采集方式 : 
CC 
# C405180208 每APN GGSN去激活会话总时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计GGSN发起去激活流程总时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为GGSN发起的去激活流程时长，一个周期结束时区分APN统计GGSN发起的去激活流程的总时长。 
采集方式 : 
CC 
# C405180209 每APN GGSN去激活会话最大时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计GGSN发起去激活流程最大时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为GGSN发起的去激活流程时长，一个周期结束时区分APN统计GGSN发起的去激活流程时长的最大值。 
采集方式 : 
MAX 
# C405180210 每APN GGSN去激活会话最小时长(毫秒)-GSM 

计数器描述 : 
采集周期内区分APN统计GGSN发起去激活流程最小时长（针对2G用户统计）。 
测量触发点 : 
流程成功时间减去流程开始时间为GGSN发起的去激活流程时长，一个周期结束时区分APN统计GGSN发起的去激活流程时长的最小值。 
采集方式 : 
MIN 
# C405180211 分APN的计费特性 Bit15为1时国内漫游用户非扩展APN解析GGSN次数-UMTS 

计数器描述 : 
在测量周期内统计签约计费特性Bit15为1的3G接入国内漫游用户，其解析GGSN/PGW时没有使用APN扩展的次数。 
测量触发点 : 
对于3G接入的国内漫游用户，如果其签约计费特性Bit15位为1，PDP激活过程中解析GGSN/PGW时没有对APN进行扩展，则进行统计。 
采集方式 : 
CC 
# C405180212 分APN的计费特性 Bit15为1时国内漫游用户非扩展APN解析GGSN次数-GSM 

计数器描述 : 
在测量周期内统计签约计费特性Bit15为1的2G接入的国内漫游用户，其解析GGSN/PGW时没有使用APN扩展的次数。 
测量触发点 : 
对于2G接入的国内漫游用户，如果其签约计费特性Bit15位为1，PDP激活过程中解析GGSN/PGW时没有对APN进行扩展，则进行统计。 
采集方式 : 
CC 
