

对GSM和UTMS的会话进行统计时需要创建。建议颗粒为5分钟。 


# C405070001 MS激活会话请求次数-UMTS 


## 计数器描述 
MS（Iu口接入）发起PDP上下文激活的请求次数。


## 测量触发点 
SGSN收到MS（Iu口接入）发来的PDP上下文激活请求，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活会话失败时统计。 


## 采集方式 
CC 


# C405070002 MS激活会话请求次数-GSM 


## 计数器描述 
MS（Gb口接入）发起PDP上下文激活的请求次数。 


## 测量触发点 
SGSN收到MS（Gb口接入）发来的PDP上下文激活请求，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活会话失败时统计。 


## 采集方式 
CC 


# C405070003 MS激活会话成功次数-UMTS 


## 计数器描述 
MS（Iu口接入）发起PDP上下文激活的成功次数。 


## 测量触发点 
MS（Iu口接入）上下文激活成功，SGSN向MS发送激活接受消息（Activate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297676.png)


## 采集方式 
CC 


# C405070004 MS激活会话成功次数-GSM 


## 计数器描述 
MS（Gb口接入）发起PDP上下文激活的成功次数。 


## 测量触发点 
MS（Gb口接入）上下文激活成功，SGSN向MS发送激活接受消息（Activate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297678.png)


## 采集方式 
CC 


# C405070005 网络激活会话请求次数-UMTS 


## 计数器描述 
网络对MS（Iu口接入）发起PDP上下文激活的尝试次数。 


## 测量触发点 
SGSN收到网络对MS（Iu口接入）发起的PDP上下文激活请求消息（PDU
Notification Request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297680.png)


## 采集方式 
CC 


# C405070006 网络激活会话请求次数-GSM 


## 计数器描述 
网络对MS（Gb口接入）发起PDP上下文激活的尝试次数。 


## 测量触发点 
SGSN收到网络对MS（Gb口接入）发起的PDP上下文激活请求消息（PDU
Notification Request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297680.png)


## 采集方式 
CC 


# C405070007 网络激活会话成功次数-UMTS 


## 计数器描述 
网络对MS（Iu口接入）发起PDP上下文激活的成功次数。 


## 测量触发点 
网络对MS（Iu口接入）发起的PDP上下文激活成功，SGSN向MS发送激活接受消息（Activate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297683.png)


## 采集方式 
CC 


# C405070008 网络激活会话成功次数-GSM 


## 计数器描述 
网络对MS（Gb口接入）发起PDP上下文激活的成功次数。 


## 测量触发点 
网络对MS（Gb口接入）发起的PDP上下文激活成功，SGSN向MS发送激活接受消息（Activate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297685.png)


## 采集方式 
CC 


# C405070009 使用动态地址激活会话请求次数-UMTS 


## 计数器描述 
MS（Iu口接入）使用动态地址激活会话请求次数。 


## 测量触发点 
MS（Iu口接入）发起动态PDP上下文激活请求消息，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活会话流程失败时统计。 


## 采集方式 
CC 


# C405070010 使用动态地址激活会话请求次数-GSM 


## 计数器描述 
MS（Gb口接入）使用动态地址激活会话请求次数。 


## 测量触发点 
MS（Gb口接入）发起动态PDP上下文激活请求消息，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活会话流程失败时统计。 


## 采集方式 
CC 


# C405070011 使用动态地址激活会话成功次数-UMTS 


## 计数器描述 
MS（Iu口接入）使用动态地址激活会话成功次数。 


## 测量触发点 
MS（Iu口接入）发起动态PDP上下文激活成功，SGSN向MS发送激活接受消息（activate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297689.png)


## 采集方式 
CC 


# C405070012 使用动态地址激活会话成功次数-GSM 


## 计数器描述 
MS（Gb口接入）使用动态地址激活会话成功次数。 


## 测量触发点 
MS（Gb口接入）发起动态PDP上下文激活成功，SGSN向MS发送激活接受消息（activate
PDP context accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297691.png)


## 采集方式 
CC 


# C405070013 有激活会话的平均用户数-UMTS 


## 计数器描述 
有激活会话的3G平均用户数。 


## 测量触发点 
按照采集粒度对有激活PDP上下文的3G用户数进行取样，再对测量时段内的各取样值取平均值得到该测量值。 


## 采集方式 
TA 


# C405070014 有激活会话的平均用户数-GSM 


## 计数器描述 
有激活会话的2G平均用户数。 


## 测量触发点 
按照采集粒度对有激活PDP上下文的2G用户数进行取样，再对测量时段内的各取样值取平均值得到该测量值。 


## 采集方式 
TA 


# C405070015 有激活会话的最大用户数-UMTS 


## 计数器描述 
有激活会话的3G最大用户数。 


## 测量触发点 
按照采集粒度对有激活PDP上下文的3G用户数进行取样，再对测量时段内的各取样值取最大值得到该测量值。 


## 采集方式 
Max 


# C405070016 有激活会话的最大用户数-GSM 


## 计数器描述 
有激活会话的2G最大用户数。 


## 测量触发点 
按照采集粒度对有激活PDP上下文的2G用户数进行取样，再对测量时段内的各取样值取最大值得到该测量值。 


## 采集方式 
Max 


# C405070017 处于激活态的会话平均数-UMTS 


## 计数器描述 
处于激活态的3G会话平均数。 


## 测量触发点 
按照采集粒度对PDP上下文处于激活态的的3G会话数进行取样，再对测量时段内的各取样值取平均值得到该测量值。 


## 采集方式 
TA 


# C405070018 处于激活态的会话平均数-GSM 


## 计数器描述 
处于激活态的2G会话平均数。 


## 测量触发点 
按照采集粒度对PDP上下文处于激活态的2G会话数进行取样，再对测量时段内的各取样值取平均值得到该测量值。 


## 采集方式 
TA 


# C405070019 处于激活态的会话最大数-UMTS 


## 计数器描述 
处于激活态的3G会话最大数。 


## 测量触发点 
按照采集粒度对PDP上下文处于激活态的3G会话数进行取样，再对测量时段内的各取样值取最大值得到该测量值。 


## 采集方式 
Max 


# C405070020 处于激活态的会话最大数-GSM 


## 计数器描述 
处于激活态的2G会话最大数。 


## 测量触发点 
按照采集粒度对PDP上下文处于激活态的2G会话数进行取样，再对测量时段内的各取样值取最大值得到该测量值。 


## 采集方式 
Max 


# C405070021 SGSN去激活请求次数(SGSN原因)-UMTS 
## 计数器描述 
统计由于SGSN原因引起SGSN在Iu接口向MS发起去激活会话的请求次数。 
## 测量触发点 
由于SGSN原因（如UP重启、等待用户面响应超时等）导致SGSN在Iu接口主动发起去激活PDP上下文请求（Deactivate
PDP Context Request）时统计。 
## 采集方式 
CC 
# C405070022 SGSN去激活请求次数(SGSN原因)-GSM 
## 计数器描述 
统计由于SGSN原因引起SGSN在Gb接口向MS发起去激活会话的请求次数。 
## 测量触发点 
由于SGSN原因（如UP重启、等待用户面响应超时等）导致SGSN在Gb接口主动发起去激活PDP上下文请求（Deactivate
PDP Context Request）时统计。 
## 采集方式 
CC 
# C405070023 SGSN去激活的成功次数(SGSN原因)-UMTS 
## 计数器描述 
统计由于SGSN原因引起SGSN在Iu接口向MS发起去激活会话的成功次数。 
## 测量触发点 
由于SGSN原因导致SGSN在Iu接口主动发起去激活PDP上下文请求，当SGSN收到该去激活PDP上下文请求的成功响应（Deactivate
PDP Context Response）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297703.png)
## 采集方式 
CC 
# C405070024 SGSN去激活的成功次数(SGSN原因)-GSM 
## 计数器描述 
统计由于SGSN原因引起SGSN在Gb接口向MS发起去激活会话的成功次数。 
## 测量触发点 
由于SGSN原因导致SGSN在Gb接口主动发起去激活PDP上下文请求，当SGSN收到该去激活PDP上下文请求的成功响应（Deactivate
PDP Context Response）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297705.png)
## 采集方式 
CC 
# C405070025 MS去激活会话的请求次数-UMTS 


## 计数器描述 
MS（Iu口接入）去激活会话的请求次数。 


## 测量触发点 
SGSN收到MS（Iu口接入）发送的去激活请求消息，SGSN给MS回去激活接受消息（Deactivate
PDP context accept），或者去激活流程失败时统计。 


## 采集方式 
CC 


# C405070026 MS去激活会话的请求次数-GSM 


## 计数器描述 
MS（Gb口接入）去激活会话的请求次数。 


## 测量触发点 
SGSN收到MS（Gb口接入）发送的去激活请求消息，SGSN给MS回去激活接受消息（Deactivate
PDP context accept），或者去激活流程失败时统计。 


## 采集方式 
CC 


# C405070027 MS去激活会话的成功次数-UMTS 


## 计数器描述 
MS（Iu口接入）发起去激活会话的成功次数。 


## 测量触发点 
MS（Iu口接入）发起的去激活业务处理成功，SGSN给MS发送去激活接受消息（Deactivate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297709.png)


## 采集方式 
CC 


# C405070028 MS去激活会话的成功次数-GSM 


## 计数器描述 
MS（Gb口接入）发起去激活会话的成功次数。 


## 测量触发点 
MS（Gb口接入）发起的去激活业务处理成功，SGSN给MS发送去激活接受消息（Deactivate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297711.png)


## 采集方式 
CC 


# C405070029 GGSN去激活会话的请求次数-UMTS 


## 计数器描述 
GGSN对用户（Iu口接入）发起去激活会话的请求次数。 


## 测量触发点 
针对Iu口接入的用户，SGSN向GGSN返回去激活响应消息（Delete
PDP Context Response）且消息中携带原因值为Request Accepted时，或者GGSN发起的去激活流程失败时统计。 


## 采集方式 
CC 


# C405070030 GGSN去激活会话的请求次数-GSM 


## 计数器描述 
GGSN对用户（Gb口接入）发起去激活会话的请求次数。 


## 测量触发点 
针对Gb口接入的用户，SGSN向GGSN返回去激活响应消息（Delete
PDP Context Response）且消息中携带原因值为Request Accepted时，或者GGSN发起的去激活流程失败时统计。 


## 采集方式 
CC 


# C405070031 GGSN去激活会话成功次数-UMTS 


## 计数器描述 
GGSN对用户（Iu口接入）发起去激活会话的成功次数。 


## 测量触发点 
针对Iu口接入的用户，SGSN向GGSN返回去激活响应消息（Delete
PDP Context Response）且消息中携带原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297715.png)


## 采集方式 
CC 


# C405070032 GGSN去激活会话成功次数-GSM 


## 计数器描述 
GGSN对用户（Gb口接入）发起去激活会话的成功次数。 


## 测量触发点 
针对Gb口接入的用户，SGSN向GGSN返回去激活响应消息（Delete
PDP Context Response）且消息中携带原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297715.png)


## 采集方式 
CC 


# C405070033 二次激活的请求次数-UMTS 


## 计数器描述 
MS （Iu口接入）发起二次激活的请求次数。 


## 测量触发点 
SGSN给MS（Iu口接入）发送二次激活接受消息（Secondary
PDP context accept），或者二次激活流程失败时统计。 


## 采集方式 
CC 


# C405070034 二次激活的请求次数-GSM 


## 计数器描述 
MS （Gb口接入）发起二次激活的请求次数。 


## 测量触发点 
SGSN给MS（Gb口接入）发送二次激活接受消息（Secondary
PDP context accept），或者二次激活流程失败时统计。 


## 采集方式 
CC 


# C405070035 二次激活的成功次数-UMTS 


## 计数器描述 
MS （Iu口接入）发起二次激活的成功次数。 


## 测量触发点 
SGSN给MS （Iu口接入）发送二次激活接受消息（Secondary
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297720.png)


## 采集方式 
CC 


# C405070036 二次激活的成功次数-GSM 


## 计数器描述 
MS （Gb口接入）发起二次激活的成功次数。 


## 测量触发点 
SGSN给MS （Gb口接入）发送二次激活接受消息（Secondary
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297722.png)


## 采集方式 
CC 


# C405070037 MS修改会话请求次数-UMTS 


## 计数器描述 
MS （Iu口接入）发起修改会话的请求次数。 


## 测量触发点 
SGSN给MS（Iu口接入）发送修改会话接受消息（Modify PDP
context accept），或者MS发起的修改流程失败时统计。 


## 采集方式 
CC 


# C405070038 MS修改会话请求次数-GSM 


## 计数器描述 
MS （Gb口接入）发起修改会话的请求次数。 


## 测量触发点 
SGSN给MS（Gb口接入）发送修改会话接受消息（Modify PDP
context accept），或者MS发起的修改流程失败时统计。 


## 采集方式 
CC 


# C405070039 MS修改会话成功次数-UMTS 


## 计数器描述 
MS （Iu口接入）发起修改会话的成功次数。 


## 测量触发点 
SGSN给MS （Iu口接入）发送修改会话接受消息（Modify PDP
Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297726.png)


## 采集方式 
CC 


# C405070040 MS修改会话成功次数-GSM 


## 计数器描述 
MS （Gb口接入）发起修改会话的成功次数。 


## 测量触发点 
SGSN给MS （Gb口接入）发送修改会话接受消息（Modify PDP
Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297728.png)


## 采集方式 
CC 


# C405070041 SGSN修改会话的请求次数-UMTS 


## 计数器描述 
SGSN对MS（Iu口接入）发起修改会话的请求次数。 


## 测量触发点 
SGSN收到MS（Iu口接入）发送的修改会话接受消息（Modify
PDP context accept），或者修改失败时统计。 


## 采集方式 
CC 


# C405070042 SGSN修改会话的请求次数-GSM 


## 计数器描述 
SGSN对MS（Gb口接入）发起修改会话的请求次数。 


## 测量触发点 
SGSN收到MS（Gb口接入）发送的修改会话接受消息（Modify
PDP context accept），或者修改失败时统计。 


## 采集方式 
CC 


# C405070043 SGSN修改会话的成功次数-UMTS 


## 计数器描述 
SGSN对MS（Iu口接入）发起修改会话的成功次数。 


## 测量触发点 
SGSN收到MS（Iu口接入）发送来的修改会话接受消息（Modify
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297732.png)


## 采集方式 
CC 


# C405070044 SGSN修改会话的成功次数-GSM 


## 计数器描述 
SGSN对MS（Gb口接入）发起修改会话的成功次数。 


## 测量触发点 
SGSN收到MS（Gb口接入）发送来的修改会话接受消息（Modify
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297734.png)


## 采集方式 
CC 


# C405070045 GGSN更新会话的请求次数-UMTS 


## 计数器描述 
针对Iu口接入的MS，GGSN向SGSN发起更新会话的请求次数。 


## 测量触发点 
针对Iu口接入的MS，SGSN向GGSN发出更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted，或者更新失败时统计。 


## 采集方式 
CC 


# C405070046 GGSN更新会话的请求次数-GSM 


## 计数器描述 
针对Gb口接入的MS，GGSN向SGSN发起更新会话的请求次数。 


## 测量触发点 
针对Gb口接入的MS，SGSN向GGSN发出更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted，或者更新失败时统计。 


## 采集方式 
CC 


# C405070047 GGSN更新会话的成功次数-UMTS 


## 计数器描述 
针对Iu口接入的MS，GGSN向SGSN发起更新会话的成功次数。 


## 测量触发点 
针对Iu口接入的MS，SGSN向GGSN发送更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297738.png)


## 采集方式 
CC 


# C405070048 GGSN更新会话的成功次数-GSM 


## 计数器描述 
针对Gb口接入的MS，GGSN向SGSN发起更新会话的成功次数。 


## 测量触发点 
针对Gb口接入的MS，SGSN向GGSN发送更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297740.png)


## 采集方式 
CC 


# C405070049 SGSN更新会话的请求次数-UMTS 


## 计数器描述 
针对Iu口接入的MS，SGSN向GGSN发起更新会话的请求次数。 


## 测量触发点 
针对Iu口接入的MS，SGSN向GGSN发送更新会话请求消息（Update
PDP Context Request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297742.png)


## 采集方式 
CC 


# C405070050 SGSN更新会话的请求次数-GSM 


## 计数器描述 
针对Gb口接入的MS，SGSN向GGSN发起更新会话的请求次数。 


## 测量触发点 
针对Gb口接入的MS，SGSN向GGSN发送更新会话请求消息（Update
PDP Context Resquest）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297744.png)


## 采集方式 
CC 


# C405070051 SGSN更新会话的成功次数-UMTS 


## 计数器描述 
针对Iu口接入的MS，SGSN向GGSN发起更新会话的成功次数。 


## 测量触发点 
针对Iu口接入的MS，SGSN收到GGSN发送的更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297746.png)


## 采集方式 
CC 


# C405070052 SGSN更新会话的成功次数-GSM 


## 计数器描述 
针对Gb口接入的MS，SGSN向GGSN发起更新会话的成功次数。 


## 测量触发点 
针对Gb口接入的MS，SGSN收到GGSN发送的更新会话响应消息（Update
PDP Context Response）且消息中携带的原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297748.png)


## 采集方式 
CC 


# C405070053 PDP会话保留次数-UMTS 


## 计数器描述 
PDP会话（3G接入）保留的次数。 


## 测量触发点 
当SGSN收到RAB或Iu释放消息，PDP上下文（3G接入）被保留且不需要修改QoS（PDP的QoS业务类型为交互类或者背景类）时统计，下图中的“A”表示了该测量项在流程中的触发位置。
[]images/img-0012643128.png)


## 采集方式 
CC 


# C405070054 PDP会话保留成功次数-UMTS 


## 计数器描述 
PDP会话（3G接入）保留成功的次数。 


## 测量触发点 
当SGSN收到RAB或Iu释放消息，PDP上下文（3G接入）被保留且不需要修改QoS（PDP的QoS业务类型为交互类或者背景类）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012643128.png)


## 采集方式 
CC 


# C405070057 用户参数不对引起的PDP失败的次数-UMTS 


## 计数器描述 
用户（Iu口接入）参数不对引起PDP失败的次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 33（3G）时统计。 


## 采集方式 
CC 


# C405070058 用户参数不对引起的PDP失败的次数-GSM 


## 计数器描述 
用户（Gb口接入）参数不对引起PDP失败的次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 33（2G）时统计。 


## 采集方式 
CC 


# C405070059 APN丢失或不知道引起的PDP激活失败次数-UMTS 


## 计数器描述 
APN丢失或APN未知引起MS（Iu口接入）PDP激活失败次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 27（3G）时统计。 


## 采集方式 
CC 


# C405070060 APN丢失或不知道引起的PDP激活失败次数-GSM 


## 计数器描述 
APN丢失或APN未知引起MS（Gb口接入）PDP激活失败次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 27（2G）时统计。 


## 采集方式 
CC 


# C405070061 未分类原因的PDP激活失败次数-UMTS 


## 计数器描述 
未分类原因引起的MS（Iu口接入）PDP激活失败次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求的消息，且导致拒绝的原因不为该测量类型下其他PDP激活失败计数器对应的原因（包括用户参数不对、APN丢失或不知道、系统资源不足、未知的PDP地址或PDP类型、用户鉴权失败、不支持的请求业务及ODB、选择的服务乱序、NSAPI已被使用、协议错误等）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297757.png)


## 采集方式 
CC 


# C405070062 未分类原因的PDP激活失败次数-GSM 


## 计数器描述 
未分类原因引起的MS（Gb口接入）PDP激活失败次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发送拒绝PDP激活请求的消息，且导致拒绝的原因不为该测量类型下其他PDP激活失败计数器对应的原因（包括用户参数不对、APN丢失或不知道、系统资源不足、未知的PDP地址或PDP类型、用户鉴权失败、不支持的请求业务及ODB、选择的服务乱序、NSAPI已被使用、协议错误等）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297759.png)


## 采集方式 
CC 


# C405070067 系统资源不足导致的MS发起PDP上下文激活失败次数-UMTS 


## 计数器描述 
系统资源不足导致MS（Iu口接入）发起PDP上下文激活的失败次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发送Active PDP Context
Reject消息且消息中携带Cause Code 26 insufficient resource （3G）时统计。 


## 采集方式 
CC 


# C405070068 系统资源不足导致的MS发起PDP上下文激活失败次数-GSM 


## 计数器描述 
系统资源不足导致MS（Gb口接入）发起PDP上下文激活的失败次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发送Active PDP Context
Reject消息且消息中携带Cause Code 26 insufficient resource （2G）时统计。 


## 采集方式 
CC 


# C405070069 未知的PDP地址或PDP类型引起的PDP激活失败次数-UMTS 


## 计数器描述 
用户（Iu口接入）激活请求中所带的PDP地址、PDP类型不合法或者错误引起的激活失败次数。 


## 测量触发点 
SGSN向用户（Iu口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 28 Unknown PDP Address or PDP Type（3G）时统计。 


## 采集方式 
CC 


# C405070070 未知的PDP地址或PDP类型引起的PDP激活失败次数-GSM 


## 计数器描述 
用户（Gb口接入）激活请求中所带的PDP地址、PDP类型不合法或者错误引起的激活失败次数。 


## 测量触发点 
SGSN向用户（Gb口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Cause
Code 28 Unknown PDP Address or PDP Type（2G）时统计。 


## 采集方式 
CC 


# C405070071 用户鉴权失败引起的PDP激活失败次数-UMTS 


## 计数器描述 
激活过程中由于用户（Iu口接入）鉴权失败而引起的PDP激活失败次数。 


## 测量触发点 
SGSN向用户（Iu口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 29 User Authentication Failed（3G）时统计。 


## 采集方式 
CC 


# C405070072 用户鉴权失败引起的PDP激活失败次数-GSM 


## 计数器描述 
激活过程中由于用户（Gb口接入）鉴权失败而引起的PDP激活失败次数。 


## 测量触发点 
SGSN向用户（Gb口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 29 User Authentication Failed（2G）时统计。 


## 采集方式 
CC 


# C405070073 不支持的请求业务及ODB引起的PDP激活失败次数-UMTS 


## 计数器描述 
SGSN不支持的请求业务及ODB引起MS（Iu口接入）PDP激活失败的次数。


## 测量触发点 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 32 Service Option Not Supported（3G）或 Caused Code 8 Operator Determined
Barring（3G）时统计。 


## 采集方式 
CC 


# C405070074 不支持的请求业务及ODB引起的PDP激活失败次数-GSM 


## 计数器描述 
SGSN不支持的请求业务及ODB引起MS（Gb口接入）PDP激活失败的次数。


## 测量触发点 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 32 Service Option Not Supported（2G）或 Caused Code 8 Operator Determined
Barring（2G）时统计。 


## 采集方式 
CC 


# C405070075 由于选择的服务乱序导致的激活失败次数-UMTS 


## 计数器描述 
由于流程冲突导致MS（Iu口接入）激活失败次数。 


## 测量触发点 
MS（Iu口接入）发起RAU流程或其他用户级流程，在流程未结束时发起激活请求导致产生冲突时统计。 


## 采集方式 
CC 


# C405070076 由于选择的服务乱序导致的激活失败次数-GSM 


## 计数器描述 
由于流程冲突导致MS（Gb口接入）激活失败次数。 


## 测量触发点 
MS（Gb口接入）发起RAU流程或其他用户级流程，在流程未结束时发起激活请求导致产生冲突时统计。 


## 采集方式 
CC 


# C405070077 由于NSAPI已被使用导致的激活失败次数-UMTS 


## 计数器描述 
由于NSAPI已被使用导致MS（Iu口接入）PDP上下文激活失败次数。 


## 测量触发点 
MS（Iu口接入）激活请求带上NSAPI，而网络侧已有该用户相同NSAPI的PDP上下文导致激活失败时统计。 


## 采集方式 
CC 


# C405070078 由于NSAPI已被使用导致的激活失败次数-GSM 


## 计数器描述 
由于NSAPI已被使用导致MS（Gb口接入）PDP上下文激活失败次数。 


## 测量触发点 
MS（Gb口接入）激活请求带上NSAPI，而网络侧已有该用户相同NSAPI的PDP上下文导致激活失败时统计。 


## 采集方式 
CC 


# C405070079 由于协议错误导致的激活失败次数-UMTS 


## 计数器描述 
单个路由区内测量由于协议规定的参数错误导致MS（Iu口接入）激活失败的次数。 


## 测量触发点 
SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）且消息中的必选参数NSAPI 或SAPI或Qos不符合协议规定值，SGSN给MS发送激活拒绝的Cause
Code为95~111时统计。 


## 采集方式 
CC 


# C405070080 由于协议错误导致的激活失败次数-GSM 


## 计数器描述 
单个路由区内测量由于协议规定的参数错误导致MS（Gb口接入）激活失败的次数。 


## 测量触发点 
SGSN收到MS（Gb口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）且消息中的必选参数NSAPI 或SAPI或Qos不符合协议规定值，SGSN给MS发送激活拒绝的Cause
Code为95~111时统计。 


## 采集方式 
CC 


# C405070081 "签约某APN为*"且"签约静态PDP地址" 
## 计数器描述 
用户在签约静态IP地址时，需指定APN，否则存在静态地址路由问题。这种情况下，SGSN兼容考虑，允许用户激活，但记录这种情况的数量。 
## 测量触发点 
SGSN收到用户激活请求且用户签约某APN的静态PDP地址时统计。 
## 采集方式 
CC 
# C405070082 激活PDP上下文时发起的DNS解析请求次数 


## 计数器描述 
激活PDP上下文时发起的DNS解析请求次数（不计重发次数）。 


## 测量触发点 
PDP上下文激活，SGSN网管上没有配置相应的APN本地域名解析时，则发起DNS解析。SGSN作为DNS
Server的客户端，DNS查询功能由SGSN的SM实现，SM向前台DNS Client发送域名解析请求消息，收到前台DNS Client的域名解析响应消息查找PDP上下文成功时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297776.png)


## 采集方式 
CC 


# C405070088 收到找不到对应PDP上下文的GGSN更新会话请求次数-GTPV1 


## 计数器描述 
SGSN收到GGSN发送的更新PDP请求（GTPV1），SGSN不存在对应的PDP上下文的次数。 


## 测量触发点 
SGSN收到GGSN发送的更新PDP请求（GTPV1），SGSN发现不存在对应的上下文时统计（包括重发次数）。 


## 采集方式 
CC 


# C405070090 收到找不到对应PDP上下文的GGSN删除会话请求次数-GTPV1 


## 计数器描述 
SGSN收到GGSN发送的去活PDP请求（GTPV1），SGSN不存在对应的PDP上下文的次数。 


## 测量触发点 
SGSN收到GGSN发送的去活PDP请求（GTPV1），SGSN发现不存在对应的上下文时进行统计（包括重发次数）。 


## 采集方式 
CC 


# C405070091 收到找不到对应PDP上下文的GGSN删除会话请求次数-GTPV0 


## 计数器描述 
SGSN收到GGSN发送的去活PDP请求（GTPV0），SGSN不存在对应的PDP上下文的次数。 


## 测量触发点 
SGSN收到GGSN发送的去活PDP请求（GTPV0），SGSN发现不存在对应的上下文时进行统计（包括重发次数）。 


## 采集方式 
CC 


# C405070092 未定义原因的PDP激活失败次数-UMTS 


## 计数器描述 
由于未定义原因引起MS（Iu口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 31 activation rejected, unspecified （3G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297781.png)


## 采集方式 
CC 


# C405070093 未定义原因的PDP激活失败次数-GSM 


## 计数器描述 
由于未定义原因引起MS（Gb口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发送拒绝PDP激活请求消息且拒绝消息中包含Caused
Code 31 activation rejected, unspecified （2G）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297783.png)


## 采集方式 
CC 


# C405070094 MS激活会话建立总时长(毫秒)-UMTS 
## 计数器描述 
有效MS（Iu口接入）激活会话建立总时长（单位：毫秒）。 
## 测量触发点 
累计本统计周期内从SGSN收到MS（Iu口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长。对于跨统计周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
## 采集方式 
CC 
# C405070095 MS激活会话建立总时长(毫秒)-GSM 
## 计数器描述 
有效MS（Gb口接入）激活会话建立总时长（单位：毫秒）。 
## 测量触发点 
累计本统计周期内从SGSN收到MS（Gb口接入）发起的PDP上下文激活请求消息（Activate
PDP Context Request）到SGSN向MS发送激活接受消息（Activate PDP Context Accept）消息的间隔时长。对于跨统计周期的MS激活会话，MS激活会话建立时长仅在激活接受消息所在周期内计算。 
## 采集方式 
CC 
# C405070096 激活PDP上下文时由于域名错误导致DNS解析失败的次数 


## 计数器描述 
激活PDP上下文时由于域名错误导致DNS解析失败的次数。 


## 测量触发点 
PDP上下文激活，网管上没有配置相应的APN本地域名解析，SGSN发送域名解析请求消息，在SGSN收到域名解析失败响应且失败原因值为“域名错误”时进行统计。 


## 采集方式 
CC 


# C405070097 激活PDP上下文时由于服务器原因导致DNS解析失败次数 


## 计数器描述 
激活PDP上下文时由于服务器原因导致DNS解析失败次数。 


## 测量触发点 
PDP上下文激活，网管上没有配置相应的APN本地域名解析，SGSN发送域名解析请求消息，在SGSN收到域名解析失败响应且失败原因值为“服务器错误”时进行统计。 


## 采集方式 
CC 


# C405070098 激活PDP上下文时由于内部原因导致DNS解析失败次数 


## 计数器描述 
激活PDP上下文时由于内部原因导致DNS解析失败次数。 


## 测量触发点 
PDP上下文激活，网管上没有配置相应的APN本地域名解析，SGSN发送域名解析请求消息，在SGSN收到域名解析失败响应且失败原因值为“内部原因”时进行统计；超时而未收到域名解析响应时也进行统计。 


## 采集方式 
CC 


# C405070102 APN更正的MS激活会话次数-UMTS 


## 计数器描述 
对检查不通过的APN进行更正的MS（Iu口接入）激活会话次数。 


## 测量触发点 
MS（Iu口接入）激活时，请求的APN和签约的APN不匹配，检查不通过，SGSN根据APN配置对该用户激活进行APN更正时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297790.png)


## 采集方式 
CC 


# C405070103 APN更正的MS激活会话次数-GSM 


## 计数器描述 
对检查不通过的APN进行更正的MS（Gb口接入）激活会话次数。 


## 测量触发点 
MS（Gb口接入）激活时，请求的APN和签约的APN不匹配，检查不通过，SGSN根据APN配置对该用户激活进行APN更正时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297792.png)


## 采集方式 
CC 


# C405070104 DT状态的PDP上下文平均数 


## 计数器描述 
DT状态的PDP上下文平均数。 


## 测量触发点 
统计模块采用求平均算法计算DT状态的PDP上下文平均数。 


## 采集方式 
TA 


# C405070105 DT状态的PDP上下文最大数 


## 计数器描述 
DT状态的PDP上下文最大数。 


## 测量触发点 
统计模块采用求峰值算法计算DT状态的PDP上下文最大数。 


## 采集方式 
Max 


# C405070106 使用静态地址激活会话请求次数-UMTS 


## 计数器描述 
MS（Iu口接入）使用静态地址激活会话请求次数。 


## 测量触发点 
MS（Iu口接入）发起静态PDP上下文激活请求，APN检查通过且地址模式为静态地址，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活失败时统计。 


## 采集方式 
CC 


# C405070107 使用静态地址激活会话请求次数-GSM 


## 计数器描述 
MS（Gb口接入）使用静态地址激活会话请求次数。 


## 测量触发点 
MS（Gb口接入）发起静态PDP上下文激活请求，APN检查通过且地址模式为静态地址，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活失败时统计。 


## 采集方式 
CC 


# C405070108 使用静态地址激活会话成功次数-UMTS 


## 计数器描述 
MS（Iu口接入）使用静态地址激活会话成功次数。 


## 测量触发点 
MS（Iu口接入）发起PDP上下文激活成功且地址模式为静态地址，SGSN向MS发送激活接受消息（Aactivate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297798.png)


## 采集方式 
CC 


# C405070109 使用静态地址激活会话成功次数-GSM 


## 计数器描述 
MS（Gb口接入）使用静态地址激活会话成功次数。 


## 测量触发点 
MS（Gb口接入）发起PDP上下文激活成功且地址模式为静态地址，SGSN向MS发送激活接受消息（Aactivate
PDP Context Accept）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297800.png)


## 采集方式 
CC 


# C405070110 MS激活会话失败次数(RAB指派失败)-UMTS 
## 计数器描述 
RAB指派失败引起MS（Iu口接入）激活失败的次数。 
## 测量触发点 
SGSN收到RNC发送的RAB Assignment Response消息，由于RAB指派失败导致PDP激活失败时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012643131.png)
## 采集方式 
CC 
# C405070111 MS激活会话失败次数(RAB指派无响应)-UMTS 
## 计数器描述 
RAB指派无响应引起MS（Iu口接入）激活失败的次数。 
## 测量触发点 
SGSN未收到RAB Assignment Response消息导致PDP激活失败时统计。 
## 采集方式 
CC 
# C405070112 MS激活会话失败次数(GGSN回网络侧原因)-UMTS 
## 计数器描述 
MS（Iu口接入）会话激活过程中，GGSN回网络侧原因引起的激活失败次数。 
## 测量触发点 
MS（Iu口接入）会话激活过程中，SGSN收到Create PDP
Context Response消息或Update PDP Context Response消息且消息中携带的原因值不为200、208、209、219、220，导致PDP激活失败时统计，下图中的“A”、“B”表示了该测量项在流程中的触发位置。 
[]images/img-0012643134.png)
## 采集方式 
CC 
# C405070113 MS激活会话失败次数(GGSN回网络侧原因)-GSM 
## 计数器描述 
MS（Gb口接入）会话激活过程中，GGSN回网络侧原因引起的激活失败次数。 
## 测量触发点 
MS（Gb口接入）会话激活过程中，SGSN收到Create PDP
Context Response消息或Update PDP Context Response消息且消息中携带的原因值不为200、208、209、219、220，导致PDP激活失败时统计，下图中的“A”、“B”表示了该测量项在流程中的触发位置。 
[]images/img-0012643136.png)
## 采集方式 
CC 
# C405070114 MS激活会话失败次数(GGSN回用户原因)-UMTS 
## 计数器描述 
MS（Iu口接入）会话激活过程中，GGSN回用户原因引起的激活失败次数。 
## 测量触发点 
MS（Iu口接入）会话激活过程中，SGSN收到Create PDP
Context Response或Update PDP Context Response消息且消息中携带的原因值为200、208、209、219、220，导致PDP激活失败时统计，下图中的“A”、“B”表示了该测量项在流程中的触发位置。 
[]images/img-0012643138.png)
## 采集方式 
CC 
# C405070115 MS激活会话失败次数(GGSN回用户原因)-GSM 
## 计数器描述 
MS（Gb口接入）会话激活过程中，GGSN回用户原因引起的激活失败次数。 
## 测量触发点 
MS（Gb口接入）会话激活过程中，SGSN收到Create PDP
Context Response或Update PDP Context Response消息且消息中携带的原因值为200、208、209、219、220，导致PDP激活失败时统计，下图中的“A”、“B”表示了该测量项在流程中的触发位置。 
[]images/img-0012643140.png)
## 采集方式 
CC 
# C405070116 MS激活会话失败次数(GGSN无响应)-UMTS 
## 计数器描述 
MS（Iu口接入）会话激活过程中，GGSN无响应引起的激活失败次数。 
## 测量触发点 
MS（Iu口接入）会话激活过程中，SGSN没有收到GGSN的Create
PDP Context Response或Update PDP Context Response消息，导致PDP激活失败时统计，下图中的“A”、“B”表示了该测量项在流程中的触发位置。 
[]images/img-0012643142.png)
## 采集方式 
CC 
# C405070117 MS激活会话失败次数(GGSN无响应)-GSM 
## 计数器描述 
MS（Gb口接入）会话激活过程中，GGSN无响应引起的激活失败次数。 
## 测量触发点 
MS（Gb口接入）会话激活过程中，SGSN没有收到GGSN的Create
PDP Context Response或Update PDP Context Response消息，导致PDP激活失败时统计，下图中的“A”、“B”表示了该测量项在流程中的触发位置。 
[]images/img-0012643144.png)
## 采集方式 
CC 
# C405070118 MS激活会话失败次数(SGSN原因)-UMTS 
## 计数器描述 
由于SGSN内部原因导致MS（Iu口接入）激活失败的次数。 
## 测量触发点 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且该拒绝消息是由于SGSN内部原因（例如进程数据区不足，用户面资源不足，上下文不足等）引起时统计。 
## 采集方式 
CC 
# C405070119 MS激活会话失败次数(SGSN原因)-GSM 
## 计数器描述 
由于SGSN内部原因导致MS（Gb口接入）激活失败的次数。 
## 测量触发点 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且该拒绝消息是由于SGSN内部原因（例如进程数据区不足，用户面资源不足，上下文不足等）引起时统计。 
## 采集方式 
CC 
# C405070120 PDP去活次数(无线原因)-UMTS 
## 计数器描述 
由于无线侧原因导致用户（Iu口接入）PDP去活的次数。 
## 测量触发点 
MS发起PDP上下文修改，RAB指派失败（原因值不为20、33、34、21、35、36）或等待RAB指派超时导致PDP被去活时统计。 
GGSN、SGSN、HLR发起PDP上下文修改，RAB指派失败或等待RAB指派超时导致PDP被去活时统计。 
RNC发起RAB修改流程，RAB指派失败或等待RAB指派超时导致PDP被去活时统计。 
在业务请求（包括下行数据触发的RAB重建）流程中，RAB指派失败或等待RAB指派超时会根据安全变量“业务请求RAB指派失败控制”来控制是保留PDP上下文还是删除PDP上下文。如果是删除PDP，导致PDP被去活时统计。 
局内重定位过程中，SGSN在发送RELOCATION COMMAND消息后一直没有收到RELOCATION COMPLETE消息或者收到TRNC的IU
RELEASE COMMAND消息而导致流程失败，将所有PDP去活时统计。 
局内局间重定位过程中，SGSN收到TRNC的RELOCATION REQUEST ACKNOWLEDGE消息中只有部分RAB建立成功，在重定位完成通知GGSN更新PDP后会将RAB没有建立成功的PDP去活时统计。 
## 采集方式 
CC 
# C405070121 MS激活会话失败次数(CAMEL拒绝)-UMTS 
## 计数器描述 
由于CAMEL拒绝导致MS（Iu口接入）PDP激活失败的次数。 
## 测量触发点 
CAMLE用户激活过程中，SGSN在给CAMEL上报事件后收到CAMEL拒绝消息，从而导致激活失败时统计。 
## 采集方式 
CC 
# C405070122 MS激活会话失败次数(CAMEL拒绝)-GSM 
## 计数器描述 
由于CAMEL拒绝导致的MS（Gb口接入）PDP激活失败的次数。 
## 测量触发点 
CAMLE用户激活过程中，SGSN在给CAMEL上报事件后收到CAMEL拒绝消息，从而导致激活失败时统计。 
## 采集方式 
CC 
# C405070123 MS激活会话失败次数(CAMEL无响应)-UMTS 
## 计数器描述 
由于CAMEL无响应导致的MS（Iu口接入）PDP激活失败的次数。 
## 测量触发点 
CAMLE用户激活过程中，SGSN在给CAMEL上报事件后没有收到CAMEL的响应消息，定时器超时，从而导致激活失败时统计。 
## 采集方式 
CC 
# C405070124 MS激活会话失败次数(CAMEL无响应)-GSM 
## 计数器描述 
由于CAMEL无响应导致的MS（Gb口接入）PDP激活失败的次数。 
## 测量触发点 
CAMLE用户激活过程中，SGSN在给CAMEL上报事件后没有收到CAMEL的响应消息，定时器超时，从而导致激活失败时统计。 
## 采集方式 
CC 
# C405070125 ODB引起的PDP激活失败次数-UMTS 


## 计数器描述 
由于ODB引起MS（Iu口接入）PDP激活失败的次数。 


## 测量触发点 
MS（Iu口接入）在激活过程中，由于ODB原因而激活失败，SGSN发送拒绝PDP激活请求消息中且消息中携带Cause
Code 8 Operator Determined Barring（3G）时统计。 


## 采集方式 
CC 


# C405070126 ODB引起的PDP激活失败次数-GSM 


## 计数器描述 
由于ODB引起MS（Gb口接入）PDP激活失败次数。 


## 测量触发点 
MS（Gb口接入）在激活过程中，由于ODB原因而激活失败，SGSN发送拒绝PDP激活请求消息中且消息中携带Cause
Code 8 Operator Determined Barring（2G）时统计。 


## 采集方式 
CC 


# C405070127 MS Info Change请求次数 


## 计数器描述 
SGSN向GGSN发起的MS Info Change Request次数。 


## 测量触发点 
SGSN向GGSN发出更新请求消息（MS Info Change Request）时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297826.png)


## 采集方式 
CC 


# C405070128 MS Info Change成功次数 


## 计数器描述 
SGSN向GGSN发起MS Info Change Request成功的次数。 


## 测量触发点 
SGSN收到GGSN发来的更新响应消息（MS Info Change
Response）且消息中携带原因值为Request Accepted时统计，下图中的“A”表示了该测量项在流程中的触发位置。 
[]images/img-0012297828.png)


## 采集方式 
CC 


# C405070129 在线PDP上下文个数-UMTS 


## 计数器描述 
处于激活态的3G用户PDP上下文个数。 


## 测量触发点 
在测量周期内，按照采集粒度对处于激活态的3G用户PDP上下文数进行取样获得该测量值。 


## 采集方式 
Sample 


# C405070130 在线PDP上下文个数-GSM 


## 计数器描述 
处于激活态的2G用户PDP上下文个数。 


## 测量触发点 
在测量周期内，按照采集粒度对处于激活态的2G用户PDP上下文数进行取样获得该测量值。 


## 采集方式 
Sample 


# C405070131 QoS降低的MS激活会话次数 
## 计数器描述 
SGSN在MS激活过程中降低QoS的次数。 
## 测量触发点 
SGSN收到激活请求（含二次激活）后，查询MM上下文记录发现用户上次去活原因值为“37 QoS not accepted”，则SGSN将根据网管配置降低QOS，使用户能够成功激活，此时触发统计该测量值。
## 采集方式 
CC 
# C405070132 二次激活失败次数(SGSN原因)-UMTS 
## 计数器描述 
由于SGSN原因导致的MS（Iu口接入）二次激活失败次数。 
## 测量触发点 
SGSN向MS（Iu口接入）发出拒绝PDP二次激活请求消息且该拒绝消息是由于SGSN内部原因（例如进程数据区不足，用户面资源不足，上下文不足等）引起时统计。 
## 采集方式 
CC 
# C405070133 二次激活失败次数(SGSN原因)-GSM 
## 计数器描述 
由于SGSN原因导致的MS（Gb口接入）二次激活失败次数。 
## 测量触发点 
SGSN向MS（Gb口接入）发出拒绝PDP二次激活请求消息且该拒绝消息是由于SGSN内部原因（例如进程数据区不足，用户面资源不足，上下文不足等）引起时统计。 
## 采集方式 
CC 
# C405070134 SGSN去激活请求次数(HLR原因)-UMTS 
## 计数器描述 
由于HLR原因导致SGSN向MS（Iu口接入）发起去激活会话请求的次数。 
## 测量触发点 
由于HLR原因（如删除签约数据、修改签约数据等），导致SGSN在Iu接口主动发起去激活PDP上下文请求（Deactivate
PDP context request）消息时统计。 
## 采集方式 
CC 
# C405070135 SGSN去激活请求次数(HLR原因)-GSM 
## 计数器描述 
由于HLR原因导致SGSN向MS（Gb口接入）发起去激活会话请求的次数。 
## 测量触发点 
由于HLR原因（如删除签约数据、修改签约数据等），导致SGSN在Gb接口主动发起去激活PDP上下文请求（Deactivate
PDP context request）消息时统计。 
## 采集方式 
CC 
# C405070136 SGSN去激活成功次数(HLR原因)-UMTS 
## 计数器描述 
由于HLR原因导致SGSN向MS（Iu口接入）发起去激活会话的成功次数。 
## 测量触发点 
由于HLR原因导致SGSN在Iu接口主动发起去激活PDP上下文请求成功时统计。 
## 采集方式 
CC 
# C405070137 SGSN去激活成功次数(HLR原因)-GSM 
## 计数器描述 
由于HLR原因导致SGSN向MS（Gb口接入）发起去激活会话的成功次数。 
## 测量触发点 
由于HLR原因导致SGSN在Gb接口主动发起去激活PDP上下文请求成功时统计。 
## 采集方式 
CC 
# C405070138 SGSN去激活请求次数(GGSN原因)-UMTS 
## 计数器描述 
由于GGSN原因导致SGSN向MS（Iu口接入）发起去激活会话请求的次数。 
## 测量触发点 
由于GGSN原因（如GGSN重启、收到GGSN的ErrInd消息等），导致SGSN在Iu接口主动发起去激活PDP上下文请求（Deactivate
PDP context request）消息时统计。 
## 采集方式 
CC 
# C405070139 SGSN去激活请求次数(GGSN原因)-GSM 
## 计数器描述 
由于GGSN原因导致SGSN向MS（Gb口接入）发起去激活会话请求的次数。 
## 测量触发点 
由于GGSN原因（如GGSN重启、收到GGSN的ErrInd消息等），导致SGSN在Gb接口主动发起去激活PDP上下文请求（Deactivate
PDP context request）消息时统计。 
## 采集方式 
CC 
# C405070140 SGSN去激活成功次数(GGSN原因)-UMTS 
## 计数器描述 
由于GGSN原因导致SGSN向MS（Iu口接入）发起去激活会话成功的次数。 
## 测量触发点 
由于GGSN原因导致SGSN在Iu接口主动发起去激活PDP上下文请求成功时统计。 
## 采集方式 
CC 
# C405070141 SGSN去激活成功次数(GGSN原因)-GSM 
## 计数器描述 
由于GGSN原因导致SGSN向MS（Gb口接入）发起去激活会话成功的次数。 
## 测量触发点 
由于GGSN原因导致SGSN在Gb接口主动发起去激活PDP上下文请求成功时统计。 
## 采集方式 
CC 
# C405070142 SGSN去激活会话请求次数-UMTS 


## 计数器描述 
SGSN向MS（Iu口接入）发起去激活会话请求的次数。 


## 测量触发点 
SGSN在Iu接口主动发起去激活PDP上下文请求（Deactivate
PDP Context Request）时统计。 


## 采集方式 
CC 


# C405070143 SGSN去激活会话请求次数-GSM 


## 计数器描述 
SGSN向MS（Gb口接入）发起去激活会话请求的次数。 


## 测量触发点 
SGSN在Gb接口主动发起去激活PDP上下文请求（Deactivate
PDP Context Request）时统计。 


## 采集方式 
CC 


# C405070144 SGSN去激活会话的成功次数-UMTS 


## 计数器描述 
SGSN向MS（Iu口接入）发起去激活会话的成功次数。 


## 测量触发点 
SGSN在Iu接口主动发起去激活PDP上下文请求（Deactivate
PDP Context Request）成功时统计。 


## 采集方式 
CC 


# C405070145 SGSN去激活会话的成功次数-GSM 


## 计数器描述 
SGSN向MS（Gb口接入）发起去激活会话的成功次数。 


## 测量触发点 
SGSN在Gb接口主动发起去激活PDP上下文请求（Deactivate
PDP Context Request）成功时统计。 


## 采集方式 
CC 


# C405070146 二次激活失败次数(RAB指派失败)-UMTS 
## 计数器描述 
RAB指派失败引起MS（Iu口接入）二次激活失败的次数。 
## 测量触发点 
SGSN收到RAB Assignment Response消息，由于RAB建立失败导致PDP二次激活失败时统计。 
## 采集方式 
CC 
# C405070147 二次激活失败次数(RAB指派无响应)-UMTS 
## 计数器描述 
RAB指派无响应引起MS（Iu口接入）二次激活失败的次数。 
## 测量触发点 
SGSN没有收到RAB Assignment Response消息而导致PDP二次激活失败时统计。 
## 采集方式 
CC 
# C405070148 二次激活失败次数(GGSN回网络侧原因)-UMTS 
## 计数器描述 
MS（Iu口接入）二次激活过程中，GGSN回网络侧原因引起二次激活失败的次数。 
## 测量触发点 
MS（Iu口接入）二次激活过程中，SGSN收到Create PDP
Context Response消息或Update PDP Context Response消息，且消息中携带的原因值不为200、208、209、219、220，导致PDP二次激活失败时统计。 
## 采集方式 
CC 
# C405070149 二次激活失败次数(GGSN回网络侧原因)-GSM 
## 计数器描述 
MS（Gb口接入）二次激活过程中，GGSN回网络侧原因引起二次激活失败的次数。 
## 测量触发点 
MS（Gb口接入）二次激活过程中，SGSN收到Create PDP
Context Response消息或Update PDP Context Response消息，且消息中携带的原因值不为200、208、209、219、220，导致PDP二次激活失败时统计。 
## 采集方式 
CC 
# C405070150 二次激活失败次数(GGSN回用户原因)-UMTS 
## 计数器描述 
MS（Iu口接入）二次激活过程中，GGSN回用户原因引起二次激活失败的次数。 
## 测量触发点 
MS（Iu口接入）二次激活过程中，SGSN收到Create PDP
Context Response消息或Update PDP Context Response消息，且消息中携带的原因值为200、208、209、219、220，导致PDP二次激活失败时统计。 
## 采集方式 
CC 
# C405070151 二次激活失败次数(GGSN回用户原因)-GSM 
## 计数器描述 
MS（Gb口接入）二次激活过程中，GGSN回用户原因引起二次激活失败的次数。 
## 测量触发点 
MS（Gb口接入）二次激活过程中，SGSN收到Create PDP
Context Response消息或Update PDP Context Response消息，且消息中携带的原因值为200、208、209、219、220，导致PDP二次激活失败时统计。 
## 采集方式 
CC 
# C405070152 二次激活失败次数(GGSN无响应)-UMTS 
## 计数器描述 
MS（Iu口接入）二次激活过程中，GGSN无响应引起二次激活失败的次数。 
## 测量触发点 
MS（Iu口接入）二次激活过程中，SGSN没有收到GGSN的Create
PDP Context Response消息或Update PDP Context Response消息，导致PDP二次激活失败时统计。 
## 采集方式 
CC 
# C405070153 二次激活失败次数(GGSN无响应)-GSM 
## 计数器描述 
MS（Gb口接入）二次激活过程中，GGSN无响应引起二次激活失败的次数。 
## 测量触发点 
MS（Gb口接入）二次激活过程中，SGSN没有收到GGSN的Create
PDP Context Response消息或Update PDP Context Response消息，导致PDP二次激活失败时统计。 
## 采集方式 
CC 
# C405070154 二次激活失败次数(CAMEL拒绝)-UMTS 
## 计数器描述 
由于CAMEL拒绝导致的MS（Iu口接入）PDP二次激活失败次数。 
## 测量触发点 
CAMEL用户在二次激活过程中，SGSN在给CAMEL上报事件后收到CAMEL拒绝消息，从而导致二次激活失败时统计。 
## 采集方式 
CC 
# C405070155 二次激活失败次数(CAMEL拒绝)-GSM 
## 计数器描述 
由于CAMEL拒绝导致的MS（Gb口接入）PDP二次激活失败次数。 
## 测量触发点 
CAMEL用户在二次激活过程中，SGSN在给CAMEL上报事件后收到CAMEL拒绝消息，从而导致二次激活失败时统计。 
## 采集方式 
CC 
# C405070156 二次激活失败次数(CAMEL无响应)-UMTS 
## 计数器描述 
由于CAMEL无响应导致MS（Iu口接入）PDP二次激活失败次数。 
## 测量触发点 
CAMEL用户在二次激活过程中，SGSN在给CAMEL上报事件后没有收到CAMEL的响应消息，定时器超时，从而导致二次激活失败时统计。 
## 采集方式 
CC 
# C405070157 二次激活失败次数(CAMEL无响应)-GSM 
## 计数器描述 
由于CAMEL无响应导致MS（Gb口接入）PDP二次激活失败次数。 
## 测量触发点 
CAMEL用户在二次激活过程中，SGSN在给CAMEL上报事件后没有收到CAMEL的响应消息，定时器超时，从而导致二次激活失败时统计。 
## 采集方式 
CC 
# C405070158 GGSN/SGW/PGW激活拒绝的失败次数-GSM 


## 计数器描述 
由于GGSN/SGW/PGW激活拒绝导致MS（Gb口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝原因为Activation
rejected by GGSN, Serving GW or PDN GW（0X1E），导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070159 GGSN/SGW/PGW激活拒绝的失败次数-UMTS 


## 计数器描述 
由于GGSN/SGW/PGW激活拒绝导致MS（Iu口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝原因为Activation
rejected by GGSN, Serving GW or PDN GW（0X1E），导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070160 QoS不接受导致的激活失败次数-GSM 


## 计数器描述 
QoS不接受导致MS（Gb口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝原因为QoS
not accepted（0X25），导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070161 QoS不接受导致的激活失败次数-UMTS 


## 计数器描述 
QoS不接受导致MS（Iu口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝原因为QoS
not accepted（0X25），导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070162 网络失败导致的激活失败次数-GSM 


## 计数器描述 
网络失败导致MS（Gb口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝原因为Network
failure（0X26），导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070163 网络失败导致的激活失败次数-UMTS 


## 计数器描述 
网络失败导致MS（Iu口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝原因为Network
failure（0X26），导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070164 TFT错误导致的激活失败次数-GSM 


## 计数器描述 
TFT错误导致MS（Gb口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Gb口接入）发出拒绝PDP激活请求消息且拒绝原因为：Semantic
error in the TFT operation（0X29）、Syntactical error in the TFT operation（0X2A）、Semantic
errors in packet filter(s  （0X2C）、Syntactical errors in packet filter(s
 （0X2D）或PDP context without TFT already activated（0X2E），导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070165 TFT错误导致的激活失败次数-UMTS 


## 计数器描述 
TFT错误导致MS（Iu口接入）PDP激活失败的次数。 


## 测量触发点 
SGSN向MS（Iu口接入）发出拒绝PDP激活请求消息且拒绝原因为：Semantic
error in the TFT operation（0X29）、Syntactical error in the TFT operation（0X2A）、Semantic
errors in packet filter(s  （0X2C）、Syntactical errors in packet filter(s
 （0X2D）或PDP context without TFT already activated（0X2E），导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070166 RAB Assignment请求次数 


## 计数器描述 
RAB Assignment请求消息发送次数。 


## 测量触发点 
SGSN收到RAB指配响应或等待响应定时器超时时统计。 


## 采集方式 
CC 


# C405070167 RAB Assignment成功次数 


## 计数器描述 
RAB Assignment成功次数。 


## 测量触发点 
SGSN收到RNC返回成功的RAB指配响应时统计。 


## 采集方式 
CC 


# C405070172 GW返回失败时SGSN重选GW次数 


## 计数器描述 
GW回复失败时，SGSN重选GW的次数。 


## 测量触发点 
激活过程中，SGSN支持GW回复失败重选GW功能，在SGSN发送了Create
PDP Context Request消息之后，收到了失败消息或没有收到Create PDP Context Response消息，SGSN成功重选GW时统计。 


## 采集方式 
CC 


# C405070174 MS激活会话失败次数(UE原因)-UMTS 
## 计数器描述 
由于UE原因导致MS（Iu口接入）激活会话失败的次数。 
## 测量触发点 
用户（Iu口接入）在激活会话过程中，由于UE原因导致激活失败时统计。 
## 采集方式 
CC 
# C405070175 二次激活失败次数(UE原因)-UMTS 
## 计数器描述 
由于UE原因导致MS（Iu口接入）PDP二次激活失败的次数。 
## 测量触发点 
用户（Iu口接入）在二次激活过程中，由于UE原因导致二次激活失败时统计。 
## 采集方式 
CC 
# C405070176 MS激活会话失败次数(UE原因)-GSM 
## 计数器描述 
由于UE原因导致MS（Gb口接入）激活会话失败的次数。 
## 测量触发点 
用户（Gb口接入）在激活会话过程中，由于UE原因导致激活失败时统计。 
## 采集方式 
CC 
# C405070177 二次激活失败次数(UE原因)-GSM 
## 计数器描述 
由于UE原因导致MS（Gb口接入）PDP二次激活失败的次数。 
## 测量触发点 
用户（Gb口接入）在二次激活过程中，由于UE原因导致二次激活失败时统计。 
## 采集方式 
CC 
# C405070178 MS激活会话失败次数(DNS原因)-UMTS 
## 计数器描述 
由于DNS原因导致MS（Iu口接入）激活会话失败的次数。 
## 测量触发点 
用户（Iu口接入）在激活会话过程中，由于DNS原因导致激活失败时统计。 
## 采集方式 
CC 
# C405070179 MS激活会话失败次数(DNS原因)-GSM 
## 计数器描述 
由于DNS原因导致MS（Gb口接入）激活会话失败的次数。 
## 测量触发点 
用户（Gb口接入）在激活会话过程中，由于DNS原因导致激活失败时统计。 
## 采集方式 
CC 
# C405070180 携带空APN的MS激活会话请求次数-UMTS 


## 计数器描述 
统计携带空APN的MS（3G接入）发起的PDP上下文激活的尝试次数。 


## 测量触发点 
SGSN收到携带空APN的MS（3G接入）发来的PDP上下文激活请求，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活会话失败时统计。 


## 采集方式 
CC 


# C405070181 携带错误APN的MS激活会话请求次数-UMTS 


## 计数器描述 
统计携带错误APN的MS（3G接入）发起的PDP上下文激活的尝试次数。 


## 测量触发点 
SGSN收到携带错误APN的MS（3G接入）发来的PDP上下文激活请求，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活会话失败时统计。 


## 采集方式 
CC 


# C405070182 携带空APN的MS激活会话请求次数-GSM 


## 计数器描述 
统计携带空APN的MS（2G接入）发起的PDP上下文激活的尝试次数。 


## 测量触发点 
SGSN收到携带空APN的MS（2G接入）发来的PDP上下文激活请求，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活会话失败时统计。 


## 采集方式 
CC 


# C405070183 携带错误APN的MS激活会话请求次数-GSM 


## 计数器描述 
统计携带错误APN的MS（2G接入）发起的PDP上下文激活的尝试次数。 


## 测量触发点 
SGSN收到携带错误APN的MS（2G接入）发来的PDP上下文激活请求，SGSN向MS发送激活接受消息（activate
PDP context accept）或者激活会话失败时统计。 


## 采集方式 
CC 


# C405070184 不支持的请求业务引起的PDP激活失败次数-UMTS 


## 计数器描述 
统计SGSN不支持的请求业务引起的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发送的PDP激活请求消息后，向MS发出拒绝PDP激活请求的消息，在拒绝PDP激活请求的消息中指示Cause
Code和原因为：Caused Code 32：Service option not supported（3G）时，进行统计。 


## 采集方式 
CC 


# C405070185 不支持的请求业务引起的PDP激活失败次数-GSM 


## 计数器描述 
统计SGSN不支持的请求业务引起的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发送的PDP激活请求消息后，向MS发出拒绝PDP激活请求的消息，在拒绝PDP激活请求的消息中指示Cause
Code和原因为：Caused Code 32：Service option not supported（2G）时，进行统计。 


## 采集方式 
CC 


# C405070186 未知的PDP上下文原因引起的PDP激活失败次数-UMTS 


## 计数器描述 
统计用户3G接入，二次激活过程中未知的PDP上下文原因导致二次激活失败次数。 


## 测量触发点 
MS（3G接入）/网络发起二次PDP上下文激活，SGSN在激活二次PDP拒绝消息中指示Cause
Code和原因为：Caused Code 43：unknown PDP context时，进行统计。 


## 采集方式 
CC 


# C405070187 未知的PDP上下文原因引起的PDP激活失败次数-GSM 


## 计数器描述 
统计用户2G接入，二次激活过程中未知的PDP上下文原因导致二次激活失败次数。 


## 测量触发点 
MS（2G接入）/网络发起二次PDP上下文激活，SGSN在激活二次PDP拒绝消息中指示Cause
Code和原因为：Caused Code 43：unknown PDP context时，进行统计。 


## 采集方式 
CC 


# C405070188 由于语义错误消息导致的PDP激活失败次数-UMTS 


## 计数器描述 
统计由于语义错误消息导致的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 95：Semantically incorrect message时，进行统计。 


## 采集方式 
CC 


# C405070189 由于语义错误消息导致的PDP激活失败次数-GSM 


## 计数器描述 
统计由于语义错误消息导致的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 95：Semantically incorrect message时，进行统计。 


## 采集方式 
CC 


# C405070190 由于无效的强制性信息导致的PDP激活失败次数-UMTS 


## 计数器描述 
统计由于无效的强制性信息导致的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 96：Invalid mandatory information时，进行统计。 


## 采集方式 
CC 


# C405070191 由于无效的强制性信息导致的PDP激活失败次数-GSM 


## 计数器描述 
统计由于无效的强制性信息导致的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 96：Invalid mandatory information时，进行统计。 


## 采集方式 
CC 


# C405070192 由于消息类型不存在或不能实现导致的PDP激活失败次数-UMTS 


## 计数器描述 
统计由于消息类型不存在或不能实现导致的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 97：Message type non-existent or not implemented时，进行统计。 


## 采集方式 
CC 


# C405070193 由于消息类型不存在或不能实现导致的PDP激活失败次数-GSM 


## 计数器描述 
统计由于消息类型不存在或不能实现导致的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 97：Message type non-existent or not implemented时，进行统计。 


## 采集方式 
CC 


# C405070194 由于消息类型与协议状态不兼容导致的PDP激活失败次数-UMTS 


## 计数器描述 
统计由于消息类型与协议状态不兼容导致的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 98：Message type not compatible with the protocol state时，进行统计。 


## 采集方式 
CC 


# C405070195 由于消息类型与协议状态不兼容导致的PDP激活失败次数-GSM 


## 计数器描述 
统计由于消息类型与协议状态不兼容导致的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 98：Message type not compatible with the protocol state时，进行统计。 


## 采集方式 
CC 


# C405070196 由于信息单元不存在或不能实现导致的PDP激活失败次数-UMTS 


## 计数器描述 
统计由于信息单元不存在或不能实现导致的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 99：Information element non-existent or not implemented时，进行统计。 


## 采集方式 
CC 


# C405070197 由于信息单元不存在或不能实现导致的PDP激活失败次数-GSM 


## 计数器描述 
统计由于信息单元不存在或不能实现导致的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 99：Information element non-existent or not implemented时，进行统计。 


## 采集方式 
CC 


# C405070198 由于IE错误条件导致的PDP激活失败次数-UMTS 


## 计数器描述 
统计由于IE错误条件导致的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 100：Conditional IE error时，进行统计。 


## 采集方式 
CC 


# C405070199 由于IE错误条件导致的PDP激活失败次数-GSM 


## 计数器描述 
统计由于IE错误条件导致的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 100：Conditional IE error时，进行统计。 


## 采集方式 
CC 


# C405070200 由于消息不兼容协议状态导致的PDP激活失败次数-UMTS 


## 计数器描述 
统计由于消息不兼容协议状态导致的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 101：Message not compatible with the protocol state时，进行统计。 


## 采集方式 
CC 


# C405070201 由于消息不兼容协议状态导致的PDP激活失败次数-GSM 


## 计数器描述 
统计由于消息不兼容协议状态导致的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 101：Message not compatible with the protocol state时，进行统计。 


## 采集方式 
CC  


# C405070202 由于协议错误未指定导致的PDP激活失败次数-UMTS 


## 计数器描述 
统计由于协议错误未指定导致的PDP激活失败次数-UMTS。 


## 测量触发点 
SGSN收到MS（3G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 111：Protocol error, unspecified时，进行统计。 


## 采集方式 
CC 


# C405070203 由于协议错误未指定导致的PDP激活失败次数-GSM 


## 计数器描述 
统计由于协议错误未指定导致的PDP激活失败次数-GSM。 


## 测量触发点 
SGSN收到MS（2G接入）发起的PDP上下文激活请求消息（activate
PDP context request），其必选参数NSAPI or SAPI or Qos不符合协议规定值。SGSN给MS发送激活拒绝的cause值为Caused
Code 111：Protocol error, unspecified时，进行统计。 


## 采集方式 
CC 


# C405070204 SGSN去激活会话请求次数(重激活原因)-UMTS 
## 计数器描述 
统计由于重激活原因引起的SGSN向MS（3G接入）发起的去激活会话请求次数。 
## 测量触发点 
SGSN向MS（3G接入）发起PDP去激活请求的消息，消息中指示Cause
Code和原因为：Caused Code 39：reactivation requested（3G）时，进行统计。 
## 采集方式 
CC 
# C405070205 SGSN去激活会话请求次数(重激活原因)-GSM 
## 计数器描述 
统计由于重激活原因引起的SGSN向MS（2G接入）发起的去激活会话请求次数。 
## 测量触发点 
SGSN向MS（2G接入）发起PDP去激活请求的消息，消息中指示Cause
Code和原因为：Caused Code 39：reactivation requested（2G）时，进行统计。 
## 采集方式 
CC 
# C405070206 MS激活会话成功次数(只允许IPv4的PDP类型)-UMTS 
## 计数器描述 
统计MS（3G接入）发起双栈的PDP上下文激活，只允许IPv4的PDP类型的PDP激活成功次数。 
## 测量触发点 
MS（3G接入）发起双栈的PDP上下文激活请求，SGSN只允许IPv4的PDP类型的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 50：PDP type IPv4 only allowed（3G）时，进行统计。 
## 采集方式 
CC 
# C405070207 MS激活会话成功次数(只允许IPv4的PDP类型)-GSM 
## 计数器描述 
统计MS（2G接入）发起双栈的PDP上下文激活，只允许IPv4的PDP类型的PDP激活成功次数。 
## 测量触发点 
MS（2G接入）发起双栈的PDP上下文激活请求，SGSN只允许IPv4的PDP类型的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 50：PDP type IPv4 only allowed（2G））时，进行统计。 
## 采集方式 
CC 
# C405070208 MS激活会话成功次数(只允许IPv6的PDP类型)-UMTS 
## 计数器描述 
统计MS（3G接入）发起双栈的PDP上下文激活，只允许IPv6的PDP类型的PDP激活成功次数。 
## 测量触发点 
MS（3G接入）发起双栈的PDP上下文激活请求，SGSN只允许IPv6的PDP类型的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 51：PDP type IPv6 only allowed（3G）时，进行统计。 
## 采集方式 
CC 
# C405070209 MS激活会话成功次数(只允许IPv6的PDP类型)-GSM 
## 计数器描述 
统计MS（2G接入）发起双栈的PDP上下文激活，只允许IPv6的PDP类型的PDP激活成功次数。 
## 测量触发点 
MS（2G接入）发起双栈的PDP上下文激活请求，SGSN只允许IPv6的PDP类型的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 51：PDP type IPv6 only allowed（2G）时，进行统计。 
## 采集方式 
CC 
# C405070210 MS激活会话成功次数(只允许单地址承载)-UMTS 
## 计数器描述 
统计MS（3G接入）发起双栈的PDP上下文激活，只允许单地址承载的PDP激活成功次数。 
## 测量触发点 
MS（3G接入）发起双栈的PDP上下文激活请求，SGSN只允许单地址承载的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 52：Single address bearers only
allowed（3G）时，进行统计。 
## 采集方式 
CC 
# C405070211 MS激活会话成功次数(只允许单地址承载)-GSM 
## 计数器描述 
统计MS（2G接入）发起双栈的PDP上下文激活，只允许单地址承载的PDP激活成功次数。 
## 测量触发点 
MS（2G接入）发起双栈的PDP上下文激活请求，SGSN只允许单地址承载的上下文激活成功，向MS发送激活接受消息（activate
PDP context accept），消息中指示Caused Code 52：Single address bearers only
allowed（2G）时，进行统计。 
## 采集方式 
CC 
# C405070212 MS修改会话失败次数(RAB指派失败)-UMTS 


## 计数器描述 
采集周期内统计RAB指派失败引起的修改会话流程失败的次数（针对3G用户统计）
。 


## 测量触发点 
MS发起的PDP修改流程，SGSN收到RAB Assignment
Response（RAB建立失败），导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070213 MS修改会话失败次数(RAB指派无响应)-UMTS 


## 计数器描述 
采集周期内统计RAB指派无响应引起的修改会话失败的次数 （针对3G用户统计）
。 


## 测量触发点 
MS发起的PDP修改流程，SGSN没有收到RAB Assignment
Response，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070214 MS修改会话失败次数(GGSN回网络侧原因)-UMTS 


## 计数器描述 
采集周期内统计PDP修改过程中GGSN回网络侧原因引起的失败响应次数（针对3G用户统计）
。 


## 测量触发点 
MS发起的PDP修改流程，SGSN收到Update PDP Context
Response消息，cause原因值不为200"Service not supported"，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070215 MS修改会话失败次数(GGSN回用户原因)-UMTS 


## 计数器描述 
采集周期内统计PDP修改过程中GGSN回用户原因引起的失败响应次数（针对3G用户统计）
。 


## 测量触发点 
MS发起的PDP修改流程，SGSN收到Update PDP Context
Response消息，cause原因值为200"Service not supported"，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070216 MS修改会话失败次数(GGSN无响应)-UMTS 


## 计数器描述 
采集周期内统计GGSN无响应引起的修改失败次数（针对3G用户统计）
。 


## 测量触发点 
MS发起的PDP修改流程，SGSN没有收到GGSN的Update PDP
Context Response，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070217 MS修改会话失败次数(SGSN原因)-UMTS 


## 计数器描述 
采集周期内统计SGSN原因导致的PDP修改失败次数（针对3G用户统计）。 


## 测量触发点 
MS发起的PDP修改流程，SGSN内部原因，如：进程数据区不足，用户面资源不足，上下文不足，板间通讯异常等，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070218 MS修改会话失败次数(GGSN回网络侧原因)-GSM 


## 计数器描述 
采集周期内统计PDP修改过程中由于网络侧原因引起的PDP修改失败次数（针对2G用户统计）。 


## 测量触发点 
MS发起的PDP修改流程，SGSN收到Update PDP Context
Response消息，cause原因值不为200"Service not supported"，导致PDP修改失败时统计。（针对2G用户统计） 


## 采集方式 
CC 


# C405070219 MS修改会话失败次数(GGSN回用户原因)-GSM 


## 计数器描述 
采集周期内统计PDP修改过程中GGSN回用户原因引起的PDP修改失败次数（针对2G用户统计）。 


## 测量触发点 
MS发起的PDP修改流程，SGSN收到Update PDP Context
Response消息，cause原因值为200"Service not supported"，导致PDP修改失败时统计。（针对2G用户统计） 


## 采集方式 
CC 


# C405070220 MS修改会话失败次数(GGSN无响应)-GSM 


## 计数器描述 
采集周期内统计由于GGSN无响应引起的PDP修改失败次数（针对2G用户统计）。 


## 测量触发点 
MS发起的PDP修改流程，SGSN没有收到GGSN的Update PDP
Context Response，导致PDP修改失败时统计。（针对2G用户统计） 


## 采集方式 
CC 


# C405070221 MS修改会话失败次数(SGSN原因)-GSM 


## 计数器描述 
采集周期内统计由于SGSN原因导致的PDP修改失败次数（针对2G用户统计）。 


## 测量触发点 
MS发起的PDP修改流程，SGSN内部原因，如：进程数据区不足，用户面资源不足，上下文不足，板间通讯异常等，导致PDP修改失败时统计。
（针对2G用户统计） 


## 采集方式 
CC 


# C405070222 SGSN修改会话失败次数(SGSN原因)-UMTS 


## 计数器描述 
采集周期内统计由于SGSN原因导致的PDP修改失败次数（针对3G用户统计） 


## 测量触发点 
SGSN向MS发起修改会话，SGSN内部原因，如：进程数据区不足，用户面资源不足，上下文不足，板间通讯异常等，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070223 SGSN修改会话失败次数(UE原因)-UMTS 


## 计数器描述 
采集周期内统计由于UE原因导致的PDP修改失败次数（针对3G用户统计）。 


## 测量触发点 
SGSN向MS发起修改会话，由于UE原因导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070224 SGSN修改会话失败次数(SGSN原因)-GSM 


## 计数器描述 
采集周期内统计由于SGSN原因导致的PDP修改失败次数（针对2G用户统计）。 


## 测量触发点 
SGSN向MS发起修改会话，SGSN内部原因，如：进程数据区不足，用户面资源不足，上下文不足，板间通讯异常等，导致PDP修改失败时统计。（针对2G用户统计） 


## 采集方式 
CC 


# C405070225 SGSN修改会话失败次数(UE原因)-GSM 


## 计数器描述 
采集周期内统计由于UE原因导致的PDP修改失败次数（针对2G用户统计）。 


## 测量触发点 
SGSN向MS发起修改会话，由于UE原因导致PDP修改失败时统计。（针对2G用户统计） 


## 采集方式 
CC 


# C405070226 GGSN更新会话失败次数(RAB指派失败)-UMTS 


## 计数器描述 
采集周期内统计GGSN发起的更新会话流程中，由于RAB指派失败引起的更新失败次数（针对3G用户统计）。 


## 测量触发点 
GGSN发起的更新会话流程，SGSN收到RAB Assignment
Response（RAB建立失败），导致PDP更新失败时统计。 


## 采集方式 
CC 


# C405070227 GGSN更新会话失败次数(RAB指派无响应)-UMTS 


## 计数器描述 
采集周期内统计GGSN发起的更新会话流程中，由于RAB指派无响应引起的更新失败次数（针对3G用户统计）。 


## 测量触发点 
GGSN发起的更新会话流程，SGSN没有收到RAB Assignment
Response，导致PDP更新失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070228 GGSN更新会话失败次数(SGSN原因)-UMTS 


## 计数器描述 
采集周期内统计GGSN发起的更新会话流程，由于SGSN原因导致的更新失败次数（针对3G用户统计）。 


## 测量触发点 
GGSN发起的更新会话流程，SGSN内部原因，如：进程数据区不足，用户面资源不足，上下文不足，板间通讯异常等，导致PDP更新失败时统计。
（针对3G用户统计） 


## 采集方式 
CC 


# C405070229 GGSN更新会话失败次数(UE原因)-UMTS 


## 计数器描述 
采集周期内统计GGSN发起的更新会话流程，由于SGSN原因导致的更新失败次数（针对2G用户统计）。 


## 测量触发点 
GGSN发起的更新会话流程，SGSN内部原因，如：进程数据区不足，用户面资源不足，上下文不足，板间通讯异常等，导致PDP更新失败时统计。
（针对2G用户统计） 


## 采集方式 
CC 


# C405070230 GGSN更新会话失败次数(SGSN原因)-GSM 


## 计数器描述 
采集周期内统计GGSN发起的更新会话流程，由于SGSN原因导致的更新失败次数（针对2G用户统计）。 


## 测量触发点 
GGSN发起的更新会话流程，SGSN内部原因，如：进程数据区不足，用户面资源不足，上下文不足，板间通讯异常等，导致PDP更新失败时统计。
（针对2G用户统计） 


## 采集方式 
CC 


# C405070231 GGSN更新会话失败次数(UE原因)-GSM 


## 计数器描述 
采集周期内统计GGSN发起的更新会话流程，由于UE原因导致的更新失败次数（针对2G用户统计）。 


## 测量触发点 
GGSN发起的更新会话流程，由于UE原因导致PDP更新失败时统计。
（针对2G用户统计） 


## 采集方式 
CC 


# C405070232 SGSN更新会话失败次数(GGSN回网络侧原因)-UMTS 


## 计数器描述 
采集周期内统计SGSN发起的更新会话流程，由于GGSN回网络侧原因引起的更新失败次数（针对3G用户统计）。 


## 测量触发点 
SGSN发起的更新会话流程，SGSN收到Update PDP Context
Response消息，cause原因值不为200"Service not supported"，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070233 SGSN更新会话失败次数(GGSN回用户原因)-UMTS 


## 计数器描述 
采集周期内统计SGSN发起的更新会话流程，由于GGSN的响应消息中携带了用户原因引起的更新失败次数（针对3G用户统计）。 


## 测量触发点 
SGSN发起的更新会话流程，SGSN收到Update PDP Context
Response消息，cause原因值为200"Service not supported"，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070234 SGSN更新会话失败次数(GGSN无响应)-UMTS 


## 计数器描述 
采集周期内统计SGSN发起的更新会话流程中，由于GGSN无响应引起的更新失败次数（针对3G用户统计）。 


## 测量触发点 
SGSN发起的更新会话流程，SGSN没有收到GGSN的Update
PDP Context Response，导致PDP修改失败时统计。（针对3G用户统计） 


## 采集方式 
CC 


# C405070235 SGSN更新会话失败次数(GGSN回网络侧原因)-GSM 


## 计数器描述 
采集周期内统计SGSN发起的更新会话流程中，由于GGSN回网络侧原因引起的更新失败次数（针对2G用户统计）。 


## 测量触发点 
SGSN发起的更新会话流程，SGSN收到Update PDP Context
Response消息，cause原因值不为200"Service not supported"，导致PDP修改失败时统计。（针对2G用户统计） 


## 采集方式 
CC 


# C405070236 SGSN更新会话失败次数(GGSN回用户原因)-GSM 


## 计数器描述 
采集周期内统计SGSN发起的更新会话流程中，由于GGSN的响应消息中携带了用户原因引起的更新失败次数（针对2G用户统计）。 


## 测量触发点 
SGSN发起的更新会话流程，SGSN收到Update PDP Context
Response消息，cause原因值为200"Service not supported"，导致PDP修改失败时统计。（针对2G用户统计） 


## 采集方式 
CC 


# C405070237 SGSN更新会话失败次数(GGSN无响应)-GSM 


## 计数器描述 
采集周期内统计SGSN发起的更新会话流程中，由于GGSN无响应引起的更新失败次数（针对2G用户统计）。 


## 测量触发点 
SGSN发起的更新会话流程，SGSN没有收到GGSN的Update
PDP Context Response，导致PDP修改失败时统计。（针对2G用户统计） 


## 采集方式 
CC 


# C405070238 MS激活会话成功次数(会话类)-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建会话类PDP上下文次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起的PDP激活成功时统计。 


## 采集方式 
CC 


# C405070239 MS激活会话成功次数(流类)-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建流类PDP上下文次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起的PDP激活成功时统计。 


## 采集方式 
CC 


# C405070240 MS激活会话成功次数(交互类THP 1)-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建THP1类PDP上下文次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起的PDP激活成功时统计。 


## 采集方式 
CC 


# C405070241 MS激活会话成功次数(交互类THP 2)-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建THP2类PDP上下文次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起的PDP激活成功时统计。 


## 采集方式 
CC 


# C405070242 MS激活会话成功次数(交互类THP 3)-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建THP3类PDP上下文次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起的PDP激活成功时统计。 


## 采集方式 
CC 


# C405070243 MS激活会话成功次数(背景类)-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建背景类PDP上下文次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起的PDP激活成功时统计。 


## 采集方式 
CC 


# C405070244 由于超时导致的PDP激活失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，由于超时导致流程失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）无线侧、网络侧、CAMEL超时导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070245 由于内部错误/限制导致的PDP激活失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，由于内部错误/限制导致流程失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）无3G用户发起修改PDP流程，内部错误/限制导致流程失败时进行统计。 


## 采集方式 
CC 


# C405070246 MS激活会话建立最大时长(毫秒)-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程持续最大时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内最大的激活会话时长。 


## 采集方式 
CC 


# C405070247 MS激活会话建立最小时长(毫秒)-UMTS 


## 计数器描述 
采集周期内统计MS发起激活会话流程持续最小时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内最小的激活会话时长。 


## 采集方式 
CC 


# C405070248 MS激活会话成功次数(会话类)-GSM 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建会话类PDP上下文次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 


## 采集方式 
CC 


# C405070249 MS激活会话成功次数(流类)-GSM 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建流类PDP上下文次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 


## 采集方式 
CC 


# C405070250 MS激活会话成功次数(交互类THP 1)-GSM 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建THP1类PDP上下文次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 


## 采集方式 
CC 


# C405070251 MS激活会话成功次数(交互类THP 2)-GSM 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建THP2类PDP上下文次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 


## 采集方式 
CC 


# C405070252 MS激活会话成功次数(交互类THP 3)-GSM 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建THP3类PDP上下文次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 


## 采集方式 
CC 


# C405070253 MS激活会话成功次数(背景类)-GSM 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，成功创建背景类PDP上下文次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） SGSN发送PDP激活成功时统计。 


## 采集方式 
CC 


# C405070254 由于超时导致的PDP激活失败次数-GSM 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，由于超时导致流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）无线侧、网络侧、CAMEL超时导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070255 由于内部错误/限制导致的PDP激活失败次数-GSM 


## 计数器描述 
采集周期内统计MS发起激活会话流程中，由于内部错误/限制导致流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）由于内部错误/限制导致PDP激活失败时统计。 


## 采集方式 
CC 


# C405070256 MS激活会话建立最大时长(毫秒)-GSM 


## 计数器描述 
采集周期内MS发起激活会话流程持续最大时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内最大的激活会话时长。 


## 采集方式 
MAX 


# C405070257 MS激活会话建立最小时长(毫秒)-GSM 


## 计数器描述 
采集周期内MS发起激活会话流程持续最大时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内最小的激活会话时长。 


## 采集方式 
MIN 


# C405070258 QoS不接受导致的MS修改会话失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起修改PDP流程中，由于QoS不接受导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起PDP修改流程，由于网络侧或无线侧QoS不接受导致流程失败时进行统计。 


## 采集方式 
CC 


# C405070259 未知的PDP上下文原因导致的MS修改会话失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起修改PDP流程中，由于未找到上下文导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起PDP修改流程，由于未知的PDP上下文原因导致流程失败时进行统计。 


## 采集方式 
CC 


# C405070260 由于内部错误/限制导致的MS修改会话失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起修改PDP流程中，由于内部错误/限制导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起PDP修改流程，由于内部错误/限制导致流程失败时进行统计。 


## 采集方式 
CC 


# C405070261 由于其他原因导致的MS修改会话失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起修改PDP流程中，由于其他原因导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起PDP修改流程，由于其他原因导致流程失败时进行统计。 


## 采集方式 
CC 


# C405070262 MS修改会话总时长(毫秒)-UMTS 


## 计数器描述 
采集周期内MS发起修改PDP流程总时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070263 MS修改会话最大时长(毫秒)-UMTS 


## 计数器描述 
采集周期内MS发起修改PDP流程最大时长（针对3G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内最大的激活会话时长。 


## 采集方式 
MAX 


# C405070264 MS修改会话最小时长(毫秒)-UMTS 


## 计数器描述 
采集周期内MS发起修改PDP流程最小时长（针对3G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内最小的激活会话时长。 


## 采集方式 
MIN 


# C405070265 UE无响应导致的SGSN修改会话失败次数-UMTS 


## 计数器描述 
采集周期内统计SGSN发起修改PDP流程中，由于UE无响应导致的失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）SGSN发起修改PDP上下文流程，由于UE无响应导致流程失败时统计 


## 采集方式 
CC 


# C405070266 由于内部错误/限制导致的SGSN修改会话失败次数-UMTS 


## 计数器描述 
采集周期内统计SGSN发起修改PDP流程中，由于内部错误/限制导致的失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）SGSN发起修改PDP上下文流程，由于内部错误/限制导致流程失败时统计。 


## 采集方式 
CC 


# C405070267 由于其他原因导致的SGSN修改会话失败次数-UMTS 


## 计数器描述 
采集周期内统计SGSN发起修改PDP流程中，由于其他原因导致的失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）SGSN发起修改PDP上下文流程，由于其他原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070268 SGSN修改会话总时长(毫秒)-UMTS 


## 计数器描述 
采集周期内SGSN发起修改PDP流程总时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为修改会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070269 SGSN修改会话最大时长(毫秒)-UMTS 


## 计数器描述 
采集周期内SGSN发起修改PDP流程最大时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最大时长。 


## 采集方式 
MAX 


# C405070270 SGSN修改会话最小时长(毫秒)-UMTS 


## 计数器描述 
采集周期内SGSN发起修改PDP流程最小时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最小时长。 


## 采集方式 
MIN 


# C405070271 系统失败导致的GGSN更新会话失败次数-UMTS 


## 计数器描述 
采集周期内统计GGSN发起更新PDP流程中，由于系统原因导致流程失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）GGSN发起更新PDP上下文流程，由于系统原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070272 由于内部错误/限制导致的GGSN更新会话失败次数-UMTS 


## 计数器描述 
采集周期内统计GGSN发起更新PDP流程中，由于内部错误/限制导致流程失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）GGSN发起更新PDP上下文流程，由于内部错误/限制导致流程失败时统计。 


## 采集方式 
CC 


# C405070273 由于其他原因导致的GGSN修改会话失败次数-UMTS 


## 计数器描述 
采集周期内统计GGSN发起更新PDP流程中，由于其他原因导致流程失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）GGSN发起更新PDP上下文流程，由于其他原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070274 GGSN更新会话总时长(毫秒)-UMTS 


## 计数器描述 
采集周期内GGSN发起修改PDP流程总长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070275 GGSN更新会话最大时长(毫秒)-UMTS 


## 计数器描述 
采集周期内GGSN发起修改PDP流程最大时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最大时长。 


## 采集方式 
MAX 


# C405070276 GGSN更新会话最小时长(毫秒)-UMTS 


## 计数器描述 
采集周期内GGSN发起修改PDP流程最小时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最小时长。 


## 采集方式 
MIN 


# C405070277 QoS不接受导致的MS修改会话失败次数-GSM 


## 计数器描述 
采集周期内统计MS发起修改PDP流程中，由于QoS不接受导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）MS发起修改PDP上下文流程，由于网络侧或无线侧QoS不接受导致流程失败时统计。 


## 采集方式 
CC 


# C405070278 未知的PDP上下文原因导致的MS修改会话失败次数-GSM 


## 计数器描述 
采集周期内统计MS发起修改PDP流程中，由于找不到PDP上下文导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）MS发起修改PDP上下文流程，由于未知的PDP上下文原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070279 由于内部错误/限制导致的MS修改会话失败次数-GSM 


## 计数器描述 
采集周期内统计MS发起修改PDP流程中，由于内部错误/限制导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）MS发起修改PDP上下文流程，由于内部错误/限制导致流程失败时统计。 


## 采集方式 
CC 


# C405070280 由于其他原因导致的MS修改会话失败次数-GSM 


## 计数器描述 
采集周期内统计MS发起修改PDP流程中，由于其他原因导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）MS发起修改PDP上下文流程，由于其他原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070281 MS修改会话总时长(毫秒)-GSM 


## 计数器描述 
采集周期内MS发起修改PDP流程总时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070282 MS修改会话最大时长(毫秒)-GSM 


## 计数器描述 
采集周期内MS发起修改PDP流程最大时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最大时长。 


## 采集方式 
MAX 


# C405070283 MS修改会话最小时长(毫秒)-GSM 


## 计数器描述 
采集周期内MS发起修改PDP流程最小时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最小时长。 


## 采集方式 
MIN 


# C405070284 UE无响应导致的SGSN修改会话失败次数-GSM 
## 计数器描述 
采集周期内统计SGSN发起修改PDP流程中，由于网络失败导致的失败次数（针对2G用户统计）。 
## 测量触发点 
（针对2G用户统计） SGSN发起修改PDP上下文流程，由于终端无响应导致的流程失败时统计。 
## 采集方式 
CC 
# C405070285 由于内部错误/限制导致的SGSN修改会话失败次数-GSM 


## 计数器描述 
采集周期内统计SGSN发起修改PDP流程中，由于内部错误/限制导致的失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） SGSN发起修改PDP上下文流程，由于内部错误/限制导致的流程失败时统计。 


## 采集方式 
CC 


# C405070286 由于其他原因导致的SGSN修改会话失败次数-GSM 


## 计数器描述 
采集周期内统计SGSN发起修改PDP流程中，由于其他原因导致的失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） SGSN发起修改PDP上下文流程，由于其他原因导致的流程失败时统计。 


## 采集方式 
CC 


# C405070287 SGSN修改会话总时长(毫秒)-GSM 


## 计数器描述 
采集周期内SGSN发起修改PDP流程总时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070288 SGSN修改会话最大时长(毫秒)-GSM 


## 计数器描述 
采集周期内SGSN发起修改PDP流程最大时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最大时长。 


## 采集方式 
MAX 


# C405070289 SGSN修改会话最小时长(毫秒)-GSM 


## 计数器描述 
采集周期内SGSN发起修改PDP流程最小时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最小时长。 


## 采集方式 
MIN 


# C405070290 系统失败导致的GGSN更新会话失败次数-GSM 


## 计数器描述 
采集周期内统计GGSN发起修改PDP流程中，由于系统原因导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）GGSN发起更新PDP上下文流程，由于系统原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070291 由于内部错误/限制导致的GGSN更新会话失败次数-GSM 


## 计数器描述 
采集周期内统计GGSN发起修改PDP流程中，由于内部错误/限制导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）GGSN发起更新PDP上下文流程，由于内部错误/限制导致流程失败时统计。 


## 采集方式 
CC 


# C405070292 由于其他原因导致的GGSN修改会话失败次数-GSM 


## 计数器描述 
采集周期内统计GGSN发起修改PDP流程中，由于其他原因导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）GGSN发起更新PDP上下文流程，由于其他原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070293 GGSN更新会话总时长(毫秒)-GSM 


## 计数器描述 
统计采集周期内GGSN发起修改PDP流程总时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070294 GGSN更新会话最大时长(毫秒)-GSM 


## 计数器描述 
统计采集周期内GGSN发起修改PDP流程最大时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最大时长。 


## 采集方式 
MAX 


# C405070295 GGSN更新会话最小时长(毫秒)-GSM 


## 计数器描述 
统计采集周期内GGSN发起修改PDP流程最小时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最小时长。 


## 采集方式 
MIN 


# C405070296 协议错误导致的MS去激活会话失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起去激活流程中，由于协议错误导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起PDP去激活流程，由于协议错误导致流程失败时统计。 


## 采集方式 
CC 


# C405070297 由于内部错误/限制导致的MS去激活会话失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起去激活流程中，由于内部错误/限制导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起PDP去激活流程，由于内部错误/限制导致流程失败时统计。 


## 采集方式 
CC 


# C405070298 由于其他原因导致的MS去激活会话失败次数-UMTS 


## 计数器描述 
采集周期内统计MS发起去激活流程中，由于其他原因导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
3G用户发起PDP去激活流程，由于其他原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070299 MS去激活会话总时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内MS发起去激活流程总时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070300 MS去激活会话最大时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内MS发起去激活流程最大时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为取激活会话时长，一个周期结束时取本周期内激活会话最大时长。 


## 采集方式 
MAX 


# C405070301 MS去激活会话最小时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内MS发起去激活流程最小时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内激活会话最小时长。 


## 采集方式 
MIN 


# C405070302 SGSN去激活会话总时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内SGSN发起去激活流程总时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070303 SGSN去激活会话最大时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内SGSN发起去激活流程最大时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内激活会话最大时长。 


## 采集方式 
CC 


# C405070304 SGSN去激活会话最小时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内SGSN发起去激活流程最小时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内激活会话最小时长。 


## 采集方式 
CC 


# C405070305 必选IE未携带导致的GGSN去激活会话失败次数-UMTS 


## 计数器描述 
采集周期内统计GGSN发起去激活流程中，由于必选IE未携带导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）GGSN发起PDP去激活流程，由于必选IE未携带导致流程失败时统计。 


## 采集方式 
CC 


# C405070306 由于内部错误/限制导致的GGSN去激活会话失败次数-UMTS 


## 计数器描述 
采集周期内统计GGSN发起去激活流程中，由于内部错误/限制导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）GGSN发起PDP去激活流程，由于内部错误/限制导致流程失败时统计。 


## 采集方式 
CC 


# C405070307 由于其他原因导致的GGSN去激活会话失败次数-UMTS 


## 计数器描述 
采集周期内统计GGSN发起去激活流程中，由于其他原因导致的流程失败次数（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计）GGSN发起PDP去激活流程，由于其他原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070308 GGSN去激活会话总时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内GGSN发起去激活流程总时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内激活会话总时长。 


## 采集方式 
CC 


# C405070309 GGSN去激活会话最大时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内GGSN发起去激活流程最大时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内激活会话最大时长。 


## 采集方式 
MAX 


# C405070310 GGSN去激活会话最小时长(毫秒)-UMTS 


## 计数器描述 
统计采集周期内GGSN发起去激活流程最小时长（针对3G用户统计）。 


## 测量触发点 
（针对3G用户统计） 流程成功时间与流程开始时间之差为激活会话时长，一个周期结束时取本周期内激活会话最小时长。 


## 采集方式 
MIN 


# C405070311 协议错误导致的MS去激活会话失败次数-GSM 


## 计数器描述 
采集周期内统计由于协议错误导致用户发起去激活流程失败的次数（针对2G用户统计）。 


## 测量触发点 
2G用户发起去激活流程，由于协议错误导致流程失败时统计。 


## 采集方式 
CC 


# C405070312 由于内部错误/限制导致的MS去激活会话失败次数-GSM 


## 计数器描述 
采集周期内统计由于内部错误/限制导致用户发起去激活流程失败的次数（针对2G用户统计）。 


## 测量触发点 
2G用户发起去激活流程，由于内部错误/限制导致流程失败时统计。 


## 采集方式 
CC 


# C405070313 由于其他原因导致的MS去激活会话失败次数-GSM 


## 计数器描述 
采集周期内统计由于其他原因导致用户发起去激活流程失败的次数（针对2G用户统计）。 


## 测量触发点 
2G用户发起去激活流程，由于其他原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070314 MS去激活会话总时长(毫秒)-GSM 


## 计数器描述 
由于采集周期内MS发起去激活流程总时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话时长之和。 


## 采集方式 
CC 


# C405070315 MS去激活会话最大时长(毫秒)-GSM 


## 计数器描述 
由于采集周期内MS发起去激活流程最大时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话最大时长。 


## 采集方式 
MAX 


# C405070316 MS去激活会话最小时长(毫秒)-GSM 


## 计数器描述 
由于采集周期内MS发起去激活流程最小时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话最小时长。 


## 采集方式 
MIN 


# C405070317 SGSN去激活会话总时长(毫秒)-GSM 


## 计数器描述 
由于采集周期内SGSN发起去激活流程总时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话时长之和。 


## 采集方式 
CC 


# C405070318 SGSN去激活会话最大时长(毫秒)-GSM 


## 计数器描述 
由于采集周期内SGSN发起去激活流程最大时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话最大时长。 


## 采集方式 
MAX 


# C405070319 SGSN去激活会话最小时长(毫秒)-GSM 


## 计数器描述 
由于采集周期内SGSN发起去激活流程最小时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话最小时长。 


## 采集方式 
MIN 


# C405070320 必选IE未携带导致的GGSN去激活会话失败次数-GSM 


## 计数器描述 
采集周期内统计在GGSN发起去激活流程中，由于必选IE未携带导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）GGSN发起PDP去激活流程，由于必选IE未携带导致流程失败时统计。 


## 采集方式 
CC 


# C405070321 由于内部错误/限制导致的GGSN去激活会话失败次数-GSM 


## 计数器描述 
采集周期内统计在GGSN发起去激活流程中，由于内部错误/限制导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）GGSN发起PDP去激活流程，由于内部错误/限制导致流程失败时统计。 


## 采集方式 
CC 


# C405070322 由于其他原因导致的GGSN去激活会话失败次数-GSM 


## 计数器描述 
采集周期内统计在GGSN发起去激活流程中，由于其他原因导致的流程失败次数（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计）GGSN发起PDP去激活流程，由于其他原因导致流程失败时统计。 


## 采集方式 
CC 


# C405070323 GGSN去激活会话总时长(毫秒)-GSM 


## 计数器描述 
统计采集周期内GGSN发起去激活流程总时长（针对2G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话总时长。 


## 采集方式 
CC 


# C405070324 GGSN去激活会话最大时长(毫秒)-GSM 


## 计数器描述 
统计采集周期内GGSN发起去激活流程最大时长（针对3G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话最大时长。 


## 采集方式 
MAX 


# C405070325 GGSN去激活会话最小时长(毫秒)-GSM 


## 计数器描述 
统计采集周期内GGSN发起去激活流程最小时长（针对3G用户统计）。 


## 测量触发点 
（针对2G用户统计） 流程成功时间与流程开始时间之差为去激活会话时长，一个周期结束时取本周期内去激活会话最小时长。 


## 采集方式 
MIN 


# C405070326 在线PDP上下文个数(会话类)-UMTS 


## 计数器描述 
采集周期内统计在线的会话类PDP上下文个数（针对3G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070327 在线PDP上下文个数(流类)-UMTS 


## 计数器描述 
采集周期内统计在线的流类PDP上下文个数（针对3G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070328 在线PDP上下文个数(交互类THP 1)-UMTS 


## 计数器描述 
采集周期内统计在线的THP1类PDP上下文个数（针对3G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070329 在线PDP上下文个数(交互类THP 2)-UMTS 


## 计数器描述 
采集周期内统计在线的THP2类PDP上下文个数（针对3G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070330 在线PDP上下文个数(交互类THP 3)-UMTS 


## 计数器描述 
采集周期内统计在线的THP3类PDP上下文个数（针对3G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070331 在线PDP上下文个数(背景类)-UMTS 


## 计数器描述 
采集周期内统计在线的背景类PDP上下文个数（针对3G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070332 在线PDP上下文个数(会话类)-GSM 


## 计数器描述 
采集周期内统计在线的会话类PDP上下文个数（针对2G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070333 在线PDP上下文个数(流类)-GSM 


## 计数器描述 
采集周期内统计在线的流类PDP上下文个数（针对2G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070334 在线PDP上下文个数(交互类THP 1)-GSM 


## 计数器描述 
采集周期内统计在线的THP1类PDP上下文个数（针对2G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070335 在线PDP上下文个数(交互类THP 2)-GSM 


## 计数器描述 
采集周期内统计在线的THP2类PDP上下文个数（针对2G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070336 在线PDP上下文个数(交互类THP 3)-GSM 


## 计数器描述 
采集周期内统计在线的THP3类PDP上下文个数（针对2G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070337 在线PDP上下文个数(背景类)-GSM 


## 计数器描述 
采集周期内统计在线的背景类PDP上下文个数（针对2G用户统计）。 


## 测量触发点 
采集周期到达时统计。 


## 采集方式 
CC 


# C405070338 计费特性Bit15为1时国内漫游用户非扩展APN解析GGSN次数-UMTS 


## 计数器描述 
在测量周期内统计签约计费特性Bit15为1的3G接入国内漫游用户，其解析GGSN/PGW时没有使用APN扩展的次数。 


## 测量触发点 
对于3G接入的国内漫游用户，如果其签约计费特性Bit15位为1，PDP激活过程中解析GGSN/PGW时没有对APN进行扩展，则进行统计。 


## 采集方式 
CC 


# C405070339 计费特性 Bit15为1时国内漫游用户非扩展APN解析GGSN次数-GSM 


## 计数器描述 
在测量周期内统计签约计费特性Bit15为1的2G接入国内漫游用户，其解析GGSN/PGW时没有使用APN扩展的次数。 


## 测量触发点 
对于2G接入的国内漫游用户，如果其签约计费特性Bit15位为1，PDP激活过程中解析GGSN/PGW时没有对APN进行扩展，则进行统计。 


## 采集方式 
CC 


# C405070340 RAB Setup请求次数 
## 计数器描述 
在测量周期内统计RAB Setup请求消息发送的次数。 
## 测量触发点 
SGSN收到RAB建立请求或等待响应定时器超时，则进行统计。 
## 采集方式 
CC 
# C405070341 RAB Setup成功次数 
## 计数器描述 
在测量周期内统计RAB Setup成功的次数。 
## 测量触发点 
SGSN收到RAB建立成功响应消息时统计。 
## 采集方式 
CC 
# C405070342 RAB Release请求次数 
## 计数器描述 
在测量周期内统计RAB Release请求消息发送次数。 
## 测量触发点 
SGSN收到RAB释放响应或等待响应定时器超时，则进行统计。 
## 采集方式 
CC 
# C405070343 RAB Release成功次数 
## 计数器描述 
在测量周期内统计RAB Release成功次数。 
## 测量触发点 
SGSN收到RAB释放成功响应消息时统计。 
## 采集方式 
CC 
