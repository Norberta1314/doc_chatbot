 拥塞与过负荷控制 
背景知识 
网络设备的故障、重启或大量用户并发的业务行为容易引起网络业务消息过多，进而造成网络设备发生拥塞或过负荷，此时需要能够对设备进行有效控制，使其能够继续提供服务而避免故障宕机。 
具体参见23501协议“5.19.5 AMF Control Of Overload”及“5.19.7 NAS level congestion control”章节。 
功能说明 
本功能用于配置在拥塞及过负荷情况下的控制信息及控制参数，帮助AMF有效应对拥塞及过负荷情况。 
子主题： 
# NAS拥塞控制配置 
# NAS拥塞控制配置 
背景知识 
大量UE的并发业务行为容易引起网络设备拥塞及异常，NAS拥塞控制功能可以帮助网络设备在一定时间内抑制UE发起业务，从而减少网络设备的话务输入，有效抑制拥塞及预防设备故障。 
具体参见3GPP TS 23.501协议“5.19.7 NAS level congestion control”章节。 
功能说明 
本功能用于配置NAS拥塞控制的不同控制方式和控制参数，帮助AMF设备应对NAS拥塞的情况。 
子主题： 
## NAS MM拥塞配置 
## NAS MM拥塞配置 
背景知识 
标准规范定义的MME/AMF，SGW/PGW/SMF通过携带Back-off Timer给UE（根据策略放行紧急业务及高优先级业务），从而在一定时间内对UE发起的业务进行抑制，从而减少系统话务输入，缓解及解决网络故障或话务高峰期间的网元负荷过高问题，从而实现有效的负荷控制和故障预防。 
功能说明 
本功能用于设置是否开启NAS MM拥塞控制开关，及相关参数配置。 
子主题： 
### 修改NASMM拥塞配置(SET NASMMCONGESTINCFG) 
### 修改NASMM拥塞配置(SET NASMMCONGESTINCFG) 
功能说明 
该命令用于查询NAS MM拥塞控制相关的信息。
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|NAS MM拥塞控制开关|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持NAS MM拥塞控制功能。
Type|NAS MM拥塞控制类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置NAS MM拥塞控制的三种方式：建立会话数当已建立会话数超过配置的最大建立会话数时，AMF执行NAS MM拥塞控制。建立会话速率当建立会话速率超过配置的最大建立会话速率时，AMF执行NAS MM拥塞控制。接收NAS MM信令速率当接收NAS MM信令的速率超过配置的最大接收NAS MM信令速率时，AMF执行NAS MM拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“NAS MM拥塞控制类型”为“建立会话数”时，此参数用于指示可支持的最大建立会话数，超过此配置值时，AMF执行NAS MM拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“NAS MM拥塞控制类型”为“建立会话速率”时，此参数用于指示可支持的最大建立会话速率，超过此配置值时，AMF执行NAS MM拥塞控制。
MAXNASMM|最大NAS MM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“NAS MM拥塞控制类型”为“接收NAS MM信令速率”时，此参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时，AMF执行NAS MM拥塞控制。
MINDELAY|最小Backoff时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最小值。
MAXDELAY|最大Backoff时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“NAS MM拥塞控制类型”为“建立会话速率”或“接收NAS MM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
开启NAS MM拥塞控制，控制类型为“建立会话速率”，最大会话建立速率设置为100。
SET NASMMCONGESTINCFG:CONGESTIONSWITCH="SUPCONGESTIONCTRL",TYPE="MAXRATE",MAXRATE=100
` 
### 查询NASMM拥塞配置(SHOW NASMMCONGESTINCFG) 
### 查询NASMM拥塞配置(SHOW NASMMCONGESTINCFG) 
功能说明 
本命令用于设置AMF是否开启NAS MM拥塞控制开关，及相关参数配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|NAS MM拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持NAS MM拥塞控制功能。
Type|NAS MM拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置NAS MM拥塞控制的三种方式：建立会话数当已建立会话数超过配置的最大建立会话数时，AMF执行NAS MM拥塞控制。建立会话速率当建立会话速率超过配置的最大建立会话速率时，AMF执行NAS MM拥塞控制。接收NAS MM信令速率当接收NAS MM信令的速率超过配置的最大接收NAS MM信令速率时，AMF执行NAS MM拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“NAS MM拥塞控制类型”为“建立会话数”时，此参数用于指示可支持的最大建立会话数，超过此配置值时，AMF执行NAS MM拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“NAS MM拥塞控制类型”为“建立会话速率”时，此参数用于指示可支持的最大建立会话速率，超过此配置值时，AMF执行NAS MM拥塞控制。
MAXNASMM|最大NAS MM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“NAS MM拥塞控制类型”为“接收NAS MM信令速率”时，此参数用于指示可支持的最大接收NAS MM信令速率，超过此配置值时，AMF执行NAS MM拥塞控制。
MINDELAY|最小Backoff时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最小值。
MAXDELAY|最大Backoff时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“NAS MM拥塞控制类型”为“建立会话速率”或“接收NAS MM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
查询NAS MM拥塞策略配置。
SHOW NASMMCONGESTINCFG
(No.1) : SHOW NASMMCONGESTINCFG:
-----------------Namf_Communication_0----------------
NAS MM拥塞控制开关     NAS MM拥塞控制类型 最大会话建立数 最大会话建立速率 最大NAS MM信令接收速率 最小Backoff时长(秒) 最大Backoff时长(秒) 拒绝比例
开启NAS MM拥塞控制     建立会话速率           0               100               0                   600               1800            100
记录数：1
执行成功耗时: 0.109 秒
` 
## DNN拥塞控制配置 
## DNN拥塞控制配置 
背景知识 
标准规范定义的MME/AMF，SGW/PGW/SMF通过携带Back-off Timer给UE（根据策略放行紧急业务及高优先级业务），从而在一定时间内对UE发起的业务进行抑制，从而减少系统话务输入，缓解及解决网络故障或话务高峰期间的网元负荷过高问题，从而实现有效的负荷控制和故障预防。 
功能说明 
本功能用于设置是否开启上行NAS SM DNN拥塞控制功能，及相关参数配置。 
子主题： 
### 增加DNN拥塞配置(ADD DNNCONGESTIONCFG) 
### 增加DNN拥塞配置(ADD DNNCONGESTIONCFG) 
功能说明 
本功能用于增加是否开启上行NAS SM DNN拥塞控制功能，及相关参数配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|DNN拥塞控制开关|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置是否支持DNN拥塞控制功能。当开启时，AMF启用DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只控制Initial Request（初始请求）。如果设置为“是”，表示只控制Initial Request（初始请求）。如果设置为“否”，表示对Existing PDU Session和Modification Request也进行控制。
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|本参数用于设置进行拥塞控制的DNN。DNN只支持输入小写。
Type|DNN拥塞控制类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置DNN拥塞控制的三种方式：建立会话数当已建立会话数超过配置的最大建立会话数时，AMF执行DNN拥塞控制。建立会话速率当建立会话速率超过配置的最大建立会话速率时，AMF执行DNN拥塞控制。接收NAS SM信令速率当接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行DNN拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话数”时，此参数用于指示可支持的最大建立会话数，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话速率”时，此参数用于指示可支持的最大建立会话速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“接收NAS SM信令速率”时，此参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“DNN拥塞控制类型”为“建立会话速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|DNN拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置是否支持DNN拥塞控制功能。当开启时，AMF启用DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只控制Initial Request（初始请求）。如果设置为“是”，表示只控制Initial Request（初始请求）。如果设置为“否”，表示对Existing PDU Session和Modification Request也进行控制。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|本参数用于设置进行拥塞控制的DNN。DNN只支持输入小写。
Type|DNN拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置DNN拥塞控制的三种方式：建立会话数当已建立会话数超过配置的最大建立会话数时，AMF执行DNN拥塞控制。建立会话速率当建立会话速率超过配置的最大建立会话速率时，AMF执行DNN拥塞控制。接收NAS SM信令速率当接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行DNN拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话数”时，此参数用于指示可支持的最大建立会话数，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话速率”时，此参数用于指示可支持的最大建立会话速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“接收NAS SM信令速率”时，此参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“DNN拥塞控制类型”为“建立会话速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
增加DNN拥塞配置
ADD DNNCONGESTIONCFG:CONGESTIONSWITCH="SUPDNNCONGESTIONCTRL",INITSWITCH="ONLYCTRLINITIALREQ",DNN="zte.com.cn",TYPE="MAXSESSION",MAXSESSION=0,MAXRATE=0,MAXNASSM=100000,MINDELAY=600,MAXDELAY=1800,REJECTRATE=100
` 
### 修改DNN拥塞配置(SET DNNCONGESTIONCFG) 
### 修改DNN拥塞配置(SET DNNCONGESTIONCFG) 
功能说明 
本功能用于修改是否开启上行NAS SM DNN拥塞控制功能。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|DNN拥塞控制开关|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置是否支持DNN拥塞控制功能。当开启时，AMF启用DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只控制Initial Request（初始请求）。如果设置为“是”，表示只控制Initial Request（初始请求）。如果设置为“否”，表示对Existing PDU Session和Modification Request也进行控制。
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|本参数用于设置进行拥塞控制的DNN。DNN只支持输入小写。
Type|DNN拥塞控制类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置DNN拥塞控制的三种方式：建立会话数当已建立会话数超过配置的最大建立会话数时，AMF执行DNN拥塞控制。建立会话速率当建立会话速率超过配置的最大建立会话速率时，AMF执行DNN拥塞控制。接收NAS SM信令速率当接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行DNN拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话数”时，此参数用于指示可支持的最大建立会话数，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话速率”时，此参数用于指示可支持的最大建立会话速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“接收NAS SM信令速率”时，此参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“DNN拥塞控制类型”为“建立会话速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|DNN拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置是否支持DNN拥塞控制功能。当开启时，AMF启用DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只控制Initial Request（初始请求）。如果设置为“是”，表示只控制Initial Request（初始请求）。如果设置为“否”，表示对Existing PDU Session和Modification Request也进行控制。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|本参数用于设置进行拥塞控制的DNN。DNN只支持输入小写。
Type|DNN拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置DNN拥塞控制的三种方式：建立会话数当已建立会话数超过配置的最大建立会话数时，AMF执行DNN拥塞控制。建立会话速率当建立会话速率超过配置的最大建立会话速率时，AMF执行DNN拥塞控制。接收NAS SM信令速率当接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行DNN拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话数”时，此参数用于指示可支持的最大建立会话数，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话速率”时，此参数用于指示可支持的最大建立会话速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“接收NAS SM信令速率”时，此参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“DNN拥塞控制类型”为“建立会话速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
修改DNN拥塞配置
SET DNNCONGESTIONCFG:CONGESTIONSWITCH="SUPDNNCONGESTIONCTRL",INITSWITCH="ONLYCTRLINITIALREQ",DNN="zte.com.cn",TYPE="MAXRATE",MAXSESSION=0,MAXRATE=1000000,MAXNASSM=0,MINDELAY=10,MAXDELAY=20,REJECTRATE=100
` 
### 删除DNN拥塞配置(DEL DNNCONGESTIONCFG) 
### 删除DNN拥塞配置(DEL DNNCONGESTIONCFG) 
功能说明 
本功能用于删除是否开启上行NAS SM DNN拥塞控制功能。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|本参数用于设置进行拥塞控制的DNN。DNN只支持输入小写。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|DNN拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置是否支持DNN拥塞控制功能。当开启时，AMF启用DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只控制Initial Request（初始请求）。如果设置为“是”，表示只控制Initial Request（初始请求）。如果设置为“否”，表示对Existing PDU Session和Modification Request也进行控制。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|本参数用于设置进行拥塞控制的DNN。DNN只支持输入小写。
Type|DNN拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置DNN拥塞控制的三种方式：建立会话数当已建立会话数超过配置的最大建立会话数时，AMF执行DNN拥塞控制。建立会话速率当建立会话速率超过配置的最大建立会话速率时，AMF执行DNN拥塞控制。接收NAS SM信令速率当接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行DNN拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话数”时，此参数用于指示可支持的最大建立会话数，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话速率”时，此参数用于指示可支持的最大建立会话速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“接收NAS SM信令速率”时，此参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“DNN拥塞控制类型”为“建立会话速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
删除DNN拥塞配置
DEL DNNCONGESTIONCFG:DNN="zte.com.cn"
` 
### 查询DNN拥塞配置(SHOW DNNCONGESTIONCFG) 
### 查询DNN拥塞配置(SHOW DNNCONGESTIONCFG) 
功能说明 
本功能用于查询是否开启上行NAS SM DNN拥塞控制功能。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|本参数用于设置进行拥塞控制的DNN。DNN只支持输入小写。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|DNN拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置是否支持DNN拥塞控制功能。当开启时，AMF启用DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只控制Initial Request（初始请求）。如果设置为“是”，表示只控制Initial Request（初始请求）。如果设置为“否”，表示对Existing PDU Session和Modification Request也进行控制。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|本参数用于设置进行拥塞控制的DNN。DNN只支持输入小写。
Type|DNN拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置DNN拥塞控制的三种方式：建立会话数当已建立会话数超过配置的最大建立会话数时，AMF执行DNN拥塞控制。建立会话速率当建立会话速率超过配置的最大建立会话速率时，AMF执行DNN拥塞控制。接收NAS SM信令速率当接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行DNN拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话数”时，此参数用于指示可支持的最大建立会话数，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“建立会话速率”时，此参数用于指示可支持的最大建立会话速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“DNN拥塞控制类型”为“接收NAS SM信令速率”时，此参数用于指示可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对DNN进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行DNN拥塞控制而拒绝业务时，拒绝消息中携带Backoff Time，此参数取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内不再发起业务。该参数用于指示AMF下发给终端Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“DNN拥塞控制类型”为“建立会话速率”或“接收NAS SM信令速率”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
查询DNN拥塞配置
SHOW DNNCONGESTIONCFG:DNN="zte.com.cn"
(No.1) : SHOW DNNCONGESTIONCFG:
-----------------Namf_Communication_0----------------
DNN拥塞控制开关 是否只控制初始请求 DNN        DNN拥塞控制类型 最大会话建立数 最大会话建立速率 最大NAS SM信令接收速率 最小Backoff时长 最大Backoff时长 拒绝比例
开启DNN拥塞控制                   zte.com.cn 建立会话速率                  100                                   600             1800             100
记录数：1
执行成功耗时: 0.141 秒
` 
## SNSSAI拥塞配置 
## SNSSAI拥塞配置 
背景知识 
标准规范定义的MME/AMF，SGW/PGW/SMF通过携带Back-off Timer给UE（根据策略放行紧急业务及高优先级业务），从而在一定时间内对UE发起的业务进行抑制，从而减少系统话务输入，缓解及解决网络故障或话务高峰期间的网元负荷过高问题，从而实现有效的负荷控制和故障预防。 
功能说明 
本功能用于设置是否开启上行NAS SM SNSSAI拥塞控制开关，及相关参数配置。 
子主题： 
### 增加SNSSAI拥塞配置(ADD SNSSAICONGESTIONCFG) 
### 增加SNSSAI拥塞配置(ADD SNSSAICONGESTIONCFG) 
功能说明 
该命令用于配置AMF是否支持NAS SM SNSSAI拥塞控制功能及相关参数值。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI拥塞控制开关|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Request消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAINAME|SNSSAI标识|参数可选性: 必选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI的标识，作为唯一索引，唯一标识该S-NSSAI。本参数的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
Type|SNSSAI拥塞控制类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI拥塞控制的三种方式。建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Request消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAINAME|SNSSAI标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI的标识，作为唯一索引，唯一标识该S-NSSAI。本参数的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
Type|SNSSAI拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI拥塞控制的三种方式。建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
增加SNSSAI拥塞配置：开启SNSSAI拥塞控制，SNSSAI标识为1，SST为eMBB，SD为303001，控制类型为“建立会话数”。
ADD SNSSAICONGESTIONCFG:CONGESTIONSWITCH="SUPSNSSAICONGESTIONCTRL",SNSSAINAME="1",SST="eMBB",SD="303001",TYPE="MAXSESSION",MINDELAY=600,MAXDELAY=1800,REJECTRATE=100
` 
### 修改SNSSAI拥塞配置(SET SNSSAICONGESTIONCFG) 
### 修改SNSSAI拥塞配置(SET SNSSAICONGESTIONCFG) 
功能说明 
该命令用于修改AMF是否支持NAS SM SNSSAI拥塞控制功能及相关参数值。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI拥塞控制开关|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Request消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAINAME|SNSSAI标识|参数可选性: 必选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI的标识，作为唯一索引，唯一标识该S-NSSAI。本参数的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
Type|SNSSAI拥塞控制类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI拥塞控制的三种方式。建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Request消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAINAME|SNSSAI标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI的标识，作为唯一索引，唯一标识该S-NSSAI。本参数的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
Type|SNSSAI拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI拥塞控制的三种方式。建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
修改SNSSAI拥塞配置：开启SNSSAI拥塞控制，SNSSAI标识为1，SST为eMBB，SD为303001，控制类型为“建立会话速率”。
SET SNSSAICONGESTIONCFG:CONGESTIONSWITCH="SUPSNSSAICONGESTIONCTRL",SNSSAINAME="1",SST="eMBB",SD="303001",TYPE="MAXRATE"
` 
### 删除SNSSAI拥塞配置(DEL SNSSAICONGESTIONCFG) 
### 删除SNSSAI拥塞配置(DEL SNSSAICONGESTIONCFG) 
功能说明 
该命令用于删除AMF是否支持NAS SM SNSSAI拥塞控制功能及相关参数值。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SNSSAINAME|SNSSAI标识|参数可选性: 必选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI的标识，作为唯一索引，唯一标识该S-NSSAI。本参数的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Request消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAINAME|SNSSAI标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI的标识，作为唯一索引，唯一标识该S-NSSAI。本参数的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
Type|SNSSAI拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI拥塞控制的三种方式。建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
删除SNSSAI标识为1的SNSSAI拥塞配置。
DEL SNSSAICONGESTIONCFG:SNSSAINAME="1"
` 
### 查询SNSSAI拥塞配置(SHOW SNSSAICONGESTIONCFG) 
### 查询SNSSAI拥塞配置(SHOW SNSSAICONGESTIONCFG) 
功能说明 
该命令用于查询AMF是否支持NAS SM SNSSAI拥塞控制功能及相关参数值。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SNSSAINAME|SNSSAI标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI的标识，作为唯一索引，唯一标识该S-NSSAI。本参数的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Request消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAINAME|SNSSAI标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI的标识，作为唯一索引，唯一标识该S-NSSAI。本参数的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
Type|SNSSAI拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI拥塞控制的三种方式。建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“SNSSAI拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“SNSSAI拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
查询SNSSAI标识为1的SNSSAI拥塞配置。
SHOW SNSSAICONGESTIONCFG:SNSSAINAME="1"
(No.3) : SHOW SNSSAICONGESTIONCFG:
-----------------Namf_Communication_0----------------
SNSSAI拥塞控制开关   是否只控制初始请求   SNSSAI标识  SST       SD     SNSSAI拥塞控制类型   最大会话建立数   最大会话建立速率   最大NAS SM信令接收速率   最小Backoff时长 最大Backoff时长 拒绝比例
开启SNSSAI拥塞控制  否                            123231        eMBB    NULL  建立会话数                                                                                                          600                  1800                      100
记录数：1
执行成功耗时: 0.107 秒
` 
## SNSSAI DNN拥塞配置 
## SNSSAI DNN拥塞配置 
背景知识 
标准规范定义的MME/AMF，SGW/PGW/SMF通过携带Back-off Timer给UE（根据策略放行紧急业务及高优先级业务），从而在一定时间内对UE发起的业务进行抑制，从而减少系统话务输入，缓解及解决网络故障或话务高峰期间的网元负荷过高问题，从而实现有效的负荷控制和故障预防。 
功能说明 
本功能用于设置是否开启上行NAS SM SNSSAI和DNN拥塞控制功能，及相关参数配置。 
子主题： 
### 增加SNSSAI DNN拥塞配置(ADD SNSSAIDNNCONGESTIONCFG) 
### 增加SNSSAI DNN拥塞配置(ADD SNSSAIDNNCONGESTIONCFG) 
功能说明 
本命令用于设置是否开启上行NAS SM DNN拥塞控制功能，及相关参数配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI DNN拥塞控制开关|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI和DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Requestf消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAIDNNIDENTITY|SNSSAI和DNN标识|参数可选性: 必选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI和DNN的标识，作为唯一索引，唯一标识该S-NSSAI。S-NSSAI ID的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|用本参数用于设置需要进行拥塞控制的DNN。
Type|拥塞控制类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI和DNN拥塞控制的三种方式：建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI DNN拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI和DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Requestf消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAIDNNIDENTITY|SNSSAI和DNN标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI和DNN的标识，作为唯一索引，唯一标识该S-NSSAI。S-NSSAI ID的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|用本参数用于设置需要进行拥塞控制的DNN。
Type|拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI和DNN拥塞控制的三种方式：建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
增加SNSSAI DNN拥塞配置：开启SNSSAI DNN拥塞控制，SNSSAI和DNN标识为1，SST为eMBB，SD为303001，DNN为zte.com.cn，拥塞控制类型为“建立会话数”。
ADD SNSSAIDNNCONGESTIONCFG:CONGESTIONSWITCH="SUPSNSSAIDNNCONGESTIONCTRL",SNSSAIDNNIDENTITY="1",SST="eMBB",SD="303001",DNN="zte.com.cn",TYPE="MAXSESSION",MINDELAY=600,MAXDELAY=1800,REJECTRATE=100
` 
### 修改SNSSAI DNN拥塞配置(SET SNSSAIDNNCONGESTIONCFG) 
### 修改SNSSAI DNN拥塞配置(SET SNSSAIDNNCONGESTIONCFG) 
功能说明 
本命令用于修改是否开启上行NAS SM DNN拥塞控制功能，及相关参数配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI DNN拥塞控制开关|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI和DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Requestf消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAIDNNIDENTITY|SNSSAI和DNN标识|参数可选性: 必选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI和DNN的标识，作为唯一索引，唯一标识该S-NSSAI。S-NSSAI ID的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 0-100|用本参数用于设置需要进行拥塞控制的DNN。
Type|拥塞控制类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI和DNN拥塞控制的三种方式：建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI DNN拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI和DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Requestf消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAIDNNIDENTITY|SNSSAI和DNN标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI和DNN的标识，作为唯一索引，唯一标识该S-NSSAI。S-NSSAI ID的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|用本参数用于设置需要进行拥塞控制的DNN。
Type|拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI和DNN拥塞控制的三种方式：建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
修改SNSSAI DNN拥塞配置：开启SNSSAI DNN拥塞控制，SNSSAI和DNN标识为1，SST为eMBB，SD为303001，DNN为zte.com.cn，拥塞控制类型为“建立会话速率”。
SET SNSSAIDNNCONGESTIONCFG:CONGESTIONSWITCH="SUPSNSSAIDNNCONGESTIONCTRL",SNSSAIDNNIDENTITY="1",SST="eMBB",SD="303001",DNN="zte.com.cn",TYPE="MAXRATE"
` 
### 删除SNSSAI DNN拥塞配置(DEL SNSSAIDNNCONGESTIONCFG) 
### 删除SNSSAI DNN拥塞配置(DEL SNSSAIDNNCONGESTIONCFG) 
功能说明 
本命令用于删除是否开启上行NAS SM DNN拥塞控制功能，及相关参数配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SNSSAIDNNIDENTITY|SNSSAI和DNN标识|参数可选性: 必选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI和DNN的标识，作为唯一索引，唯一标识该S-NSSAI。S-NSSAI ID的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI DNN拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI和DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Requestf消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAIDNNIDENTITY|SNSSAI和DNN标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI和DNN的标识，作为唯一索引，唯一标识该S-NSSAI。S-NSSAI ID的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|用本参数用于设置需要进行拥塞控制的DNN。
Type|拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI和DNN拥塞控制的三种方式：建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
删除SNSSAI和DNN标识为1的SNSSAI DNN拥塞配置。
DEL SNSSAIDNNCONGESTIONCFG:SNSSAIDNNIDENTITY="1"
` 
### 查询SNSSAI DNN拥塞配置(SHOW SNSSAIDNNCONGESTIONCFG) 
### 查询SNSSAI DNN拥塞配置(SHOW SNSSAIDNNCONGESTIONCFG) 
功能说明 
本命令用于查询是否开启上行NAS SM DNN拥塞控制功能，及相关参数配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SNSSAIDNNIDENTITY|SNSSAI和DNN标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI和DNN的标识，作为唯一索引，唯一标识该S-NSSAI。S-NSSAI ID的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CongestionSwitch|SNSSAI DNN拥塞控制开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否支持S-NSSAI和DNN拥塞控制功能。
INITSWITCH|是否只控制初始请求|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于设置AMF是否只对Initial Request消息进行拥塞控制。若本参数设置为“否”，则表示AMF除了对Initial Requestf消息进行拥塞控制，还会对Existing PDU Session和Modification Request消息也进行拥塞控制。
SNSSAIDNNIDENTITY|SNSSAI和DNN标识|参数可选性: 任选参数类型: 字符串参数范围: 1-50|本参数用于设置需要进行拥塞控制的S-NSSAI和DNN的标识，作为唯一索引，唯一标识该S-NSSAI。S-NSSAI ID的取值，是通过SHOW CONFIGUREDSNSSAI命令查询获取的。
SST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|本参数用于设置需要进行拥塞控制的S-NSSAI的SST。
SD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置需要进行拥塞控制的S-NSSAI的SD。
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 0-100|用本参数用于设置需要进行拥塞控制的DNN。
Type|拥塞控制类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置S-NSSAI和DNN拥塞控制的三种方式：建立会话数（max session establishment）：当前已建立会话数超过配置的最大建立会话数时，AMF执行拥塞控制。建立会话速率（max session establishment rate）：当前建立会话速率超过配置的最大建立会话速率时，AMF执行拥塞控制。接收NAS SM信令速率（max SNSSAI rate）：当前接收NAS SM信令的速率超过配置的最大接收NAS SM信令速率时，AMF执行拥塞控制。
MAXSESSION|最大会话建立数|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话数（max session establishment）”时，此参数用于指示AMF可支持的最大建立会话数，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MAXRATE|最大会话建立速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”时，此参数用于指示AMF可支持的最大建立会话速率，超过此配置值时。AMF会对S-NSSAI进行拥塞控制。
MAXNASSM|最大NAS SM信令接收速率|参数可选性: 任选参数类型: 数字参数范围: 0-4294967295|当“拥塞控制类型”为“接收NAS SM信令速率（max SNSSAI rate）”时，此参数用于指示AMF可支持的最大接收NAS SM信令速率，超过此配置值时，AMF会对S-NSSAI进行拥塞控制。
MINDELAY|最小Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最小值。
MAXDELAY|最大Backoff时长|参数可选性: 任选参数类型: 数字参数范围: 0-1116000默认值: 0|当AMF执行拥塞控制而拒绝业务时，需要在拒绝消息中携带Backoff Time，此参数的取值在Backoff Timer最小值与Backoff Timer最大值的范围内随机选择。终端在Backoff Time时间内，不再发起业务。该参数用于指示AMF下发给终端的Backoff Timer的最大值。
REJECTRATE|拒绝比例|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 100|当“拥塞控制类型”为“建立会话速率（max session establishment rate）”或“接收NAS SM信令速率（max SNSSAI rate）”时，该参数用于指示使用这两种拥塞控制方式时，AMF拒绝新接入业务的比例。
命令举例 
`
查询SNSSAI和DNN标识为1为SNSSAI DNN拥塞配置。
SHOW SNSSAIDNNCONGESTIONCFG:SNSSAIDNNIDENTITY="1"
(No.1) : SHOW SNSSAIDNNCONGESTIONCFG:SNSSAIDNNIDENTITY="1"
-----------------Namf_Communication_0----------------
SNSSAI DNN拥塞控制开关    是否只控制初始请求 SNSSAI和DNN标识    SST     SD      DNN            拥塞控制类型   最大会话建立数   最大会话建立速率 最大NAS SM信令接收速率 最小Backoff时长 最大Backoff时长 拒绝比例
开启SNSSAI                         DNN拥塞控制         1                           eMBB  NULL   zte.com.cn     建立会话数      600                   1800                 100
记录数：1
执行成功耗时: 0.093 秒
` 
# N2过负荷控制配置 
# N2过负荷控制配置 
背景知识 
AMF的Namf_Communication服务的Special实例可以在每个评估周期，根据NF整体负荷（即Namf_Communication和Namf_MT的NFS负荷的高值，目前取用的CPU占用率）的当前值判断AMF所处的负荷等级，根据本功能的配置值决定AMF是否发送OverloadStart消息给RAN。 
同样，根据NF整体负荷的当前值判断AMF所处的负荷等级，根据本功能的配置值决定AMF是否发送OverloadStop消息给RAN。参考协议3GPP TS 38413-f10-8.7.7, 8.7.8。 
功能说明 
本功能用于设置发送OverloadStart或OverloadStop消息的相关参数。 
子主题： 
## N2过负荷基本配置 
## N2过负荷基本配置 
背景知识 
AMF的Namf_Communication服务的Special实例可以在每个评估周期，根据NF整体负荷（即Namf_Communication和Namf_MT的NFS负荷的高值，目前取用的CPU占用率）的当前值判断AMF所处的负荷等级，根据本功能的配置值决定AMF是否发送OverloadStart消息给RAN。 
同样，根据NF整体负荷的当前值判断AMF所处的负荷等级，根据本功能的配置值决定AMF是否发送OverloadStop消息给RAN。参考协议3GPP TS 38413-f10-8.7.7, 8.7.8。 
功能说明 
本功能用于设置AMF是否开启RAN侧过负荷控制开关，及N2接口消息中相关信元参数配置值。 
子主题： 
### 修改基本参数配置(SET OLTORANBASICCFG) 
### 修改基本参数配置(SET OLTORANBASICCFG) 
功能说明 
该命令用于设置N2接口的overload基本参数。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
olToRanCycle|发送overload到RAN侧的周期(100ms)|参数可选性: 任选参数类型: 数字参数范围: 1-100默认值: 20|该参数用于配置AMF发送OverloadStart或OverloadStop到RAN侧的周期，单位：100ms。
sampleNum|每周期使用的CPU采样量|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 5|该参数用于配置控制周期中使用的CPU占用率的采样值。由于单次采集的CPU占用率不能精确表示当前AMF的整体CPU负荷，所以使用几个采集周期的CPU占用率，取平均值来作为控制对象，其中一个采集周期产生一个采样量。
sampleCycle|CPU采样周期(s)|参数可选性: 任选参数类型: 数字参数范围: 1-100默认值: 1|本参数用于设置CPU占用率的采样周期，单位：秒。
ltmMultiple|VRU数据采集周期/CPU采样周期|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 90|该参数用于计算AMF向LTM获取VRU数据的采样周期，AMF获取所有NFS的CPU占用率后，还需根据VRU的实际使用情况，对CPU占用率进行加权计算，获取最后的数据。由于VRU使用情况不是时刻变化，VRU的采集周期不需要像CPU占用率的采集周期那么频繁，可以按照几倍于CPU占用率的采样周期，来配置VRU数据采集周期。
命令举例 
`
设置overload基本配置参数信息。
SET OLTORANBASICCFG:OLTORANCYCLE=20,SAMPLENUM=5,SAMPLECYCLE=1,LTMMULTIPLE=80
` 
### 查询基本参数配置(SHOW OLTORANBASICCFG) 
### 查询基本参数配置(SHOW OLTORANBASICCFG) 
功能说明 
该命令用于查询overload基本参数信息。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
olToRanCycle|发送overload到RAN侧的周期(100ms)|参数可选性: 任选参数类型: 数字参数范围: 1-100默认值: 20|该参数用于配置AMF发送OverloadStart或OverloadStop到RAN侧的周期，单位：100ms。
sampleNum|每周期使用的CPU采样量|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 5|该参数用于配置控制周期中使用的CPU占用率的采样值。由于单次采集的CPU占用率不能精确表示当前AMF的整体CPU负荷，所以使用几个采集周期的CPU占用率，取平均值来作为控制对象，其中一个采集周期产生一个采样量。
sampleCycle|CPU采样周期(s)|参数可选性: 任选参数类型: 数字参数范围: 1-100默认值: 1|本参数用于设置CPU占用率的采样周期，单位：秒。
ltmMultiple|VRU数据采集周期/CPU采样周期|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 90|该参数用于计算AMF向LTM获取VRU数据的采样周期，AMF获取所有NFS的CPU占用率后，还需根据VRU的实际使用情况，对CPU占用率进行加权计算，获取最后的数据。由于VRU使用情况不是时刻变化，VRU的采集周期不需要像CPU占用率的采集周期那么频繁，可以按照几倍于CPU占用率的采样周期，来配置VRU数据采集周期。
命令举例 
`
查看overload基本配置参数信息。
SHOW OLTORANBASICCFG:
(No.1) : SHOW OLTORANBASICCFG:
-----------------Namf_Communication_0----------------
发送overload到RAN侧的周期(100ms)    每周期使用的CPU采样量    CPU采样周期(s)    VRU数据采集周期/CPU采样周期
20                                                     5                                   1                        90
记录数：1
执行成功耗时: 0.122 秒
` 
## N2过负荷参数配置 
## N2过负荷参数配置 
背景知识 
在系统CPU过负荷的情况下，AMF需要能够根据优先级，对业务消息进行区分处理，同时需要对超出正常处理能力的业务消息进行控制，以便恢复正常负荷状态，从而避免系统故障宕机。 
功能说明 
本功能用于配置消息及业务优先级，各接口入向业务消息最大通过量、业务权重及业务消息最大通过总量，以及各接口的出向业务消息最大通过量。 
子主题： 
### 修改RAN侧过载控制配置(SET OLTORANCFG) 
### 修改RAN侧过载控制配置(SET OLTORANCFG) 
功能说明 
该命令用于设置AMF是否需要开启RAN侧的过载控制功能，及相关消息信元参数值。
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
olSwitch|是否开启过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OLSWITCHOFF|本参数用于配置AMF是否开启过载控制。
nssaiSwitch|N2口消息中是否携带切片信息|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NSSAISWITCHOFF|本参数用于配置AMF发送给RAN侧的Overload Start消息包含的切片信息字段。携带该字段表示该切片下业务拥塞，由于是可选字段，AMF不需要每次都获取拥塞信息，故需要根据实际情况配置。
lowLevel|N2口发送Overload Start的低过载负荷等级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: SECONDARYLEVEL|本参数用于配置AMF发送给RAN侧的Overload Start消息的低过载负荷等级，通过SET OLCPULEVELCFG命令可以设置负荷等级对应CPU的实际占用率。当AMF的负载高于该配置的负荷等级但低于严重过载配置的负荷等级时，判定AMF处于轻微过载状态。
lowOlACT|轻微过载下Overload Start消息中Overload Action信元设置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: REJECTNONEMCONNECT|本参数用于配置轻微过载时，AMF发送给RAN侧的Overload Start消息中的Overload Action信元，基站根据该信元指示来控制对应类型的话务，包括：拒绝非紧急及非高优先级终端发起信令连接，拒绝新发起上行NAS信令连接，仅允许紧急及终呼信令连接，仅允许高优先级及终呼信令连接。
lowOlTLRI|轻微过载Traffic Load Reduction Indication信元设置|参数可选性: 任选参数类型: 数字参数范围: 1-99默认值: 10|本参数用于配置轻微过载时，AMF发送给RAN侧的Overload Start消息中的Traffic Load Reduction Indication信元，基站根据该信元指示来控制对应类型话务的百分比，其中控制话务类型根据Overload Action信元决定，该值设置越大表示基站控制话务的占比越大。
highLevel|N2口发送Overload Start的高过载负荷等级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: PRIMARYLEVEL|本参数用于配置AMF发送给RAN侧的Overload Start消息的高过载负荷等级，通过SET OLCPULEVELCFG命令可以设置负荷等级对应CPU的实际占用率。当AMF负载高于该参数配置的负荷等级时，判定AMF处于严重过载状态。
highOlACT|严重过载下Overload Start消息中Overload Action信元设置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: REJECTNONEMCONNECT|本参数用于配置严重过载时，AMF发送给RAN侧的Overload Start消息中的Overload Action信元，基站根据该信元指示来控制对应类型的话务，包括：拒绝非紧急及非高优先级终端发起信令连接，拒绝新发起上行NAS信令连接，仅允许紧急及终呼信令连接，仅允许高优先级及终呼信令连接。
highOlTLRI|严重过载Traffic Load Reduction Indication信元设置|参数可选性: 任选参数类型: 数字参数范围: 1-99默认值: 20|本参数用于配置严重过载时，AMF发送给RAN侧的Overload Start消息中的Traffic Load Reduction Indication信元，基站根据该信元指示来控制对应类型话务的百分比，其中控制话务类型根据Overload Action信元决定，该值设置越大表示基站控制话务的占比越大。
olGNBNum|发送Overload Start的最大gNodeB个数|参数可选性: 任选参数类型: 数字参数范围: 1-128默认值: 64|本功能用于配置AMF允许发送Overload Start消息的最大gNodeB个数。
命令举例 
`
设置RAN侧过载控制配置参数信息。
SET OLTORANCFG:OLSWITCH="OLSWITCHON",NSSAISWITCH="NSSAISWITCHON",LOWLEVEL=1,LOWOLACT="REJECTNONEMCONNECT",LOWOLTLRI=10,HIGHLEVEL=0,HIGHOLACT="REJECTUPNASCONNECT",HIGHOLTLRI=20,OLGNBNUM=128
` 
### 查询RAN侧过载控制配置(SHOW OLTORANCFG) 
### 查询RAN侧过载控制配置(SHOW OLTORANCFG) 
功能说明 
该命令用于查询AMF是否需要开启RAN侧的过载控制功能，及相关消息信元参数值。
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
olSwitch|是否开启过载控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OLSWITCHOFF|本参数用于配置AMF是否开启过载控制。
nssaiSwitch|N2口消息中是否携带切片信息|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NSSAISWITCHOFF|本参数用于配置AMF发送给RAN侧的Overload Start消息包含的切片信息字段。携带该字段表示该切片下业务拥塞，由于是可选字段，AMF不需要每次都获取拥塞信息，故需要根据实际情况配置。
lowLevel|N2口发送Overload Start的低过载负荷等级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: SECONDARYLEVEL|本参数用于配置AMF发送给RAN侧的Overload Start消息的低过载负荷等级，通过SET OLCPULEVELCFG命令可以设置负荷等级对应CPU的实际占用率。当AMF的负载高于该配置的负荷等级但低于严重过载配置的负荷等级时，判定AMF处于轻微过载状态。
lowOlACT|轻微过载下Overload Start消息中Overload Action信元设置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: REJECTNONEMCONNECT|本参数用于配置轻微过载时，AMF发送给RAN侧的Overload Start消息中的Overload Action信元，基站根据该信元指示来控制对应类型的话务，包括：拒绝非紧急及非高优先级终端发起信令连接，拒绝新发起上行NAS信令连接，仅允许紧急及终呼信令连接，仅允许高优先级及终呼信令连接。
lowOlTLRI|轻微过载Traffic Load Reduction Indication信元设置|参数可选性: 任选参数类型: 数字参数范围: 1-99默认值: 10|本参数用于配置轻微过载时，AMF发送给RAN侧的Overload Start消息中的Traffic Load Reduction Indication信元，基站根据该信元指示来控制对应类型话务的百分比，其中控制话务类型根据Overload Action信元决定，该值设置越大表示基站控制话务的占比越大。
highLevel|N2口发送Overload Start的高过载负荷等级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: PRIMARYLEVEL|本参数用于配置AMF发送给RAN侧的Overload Start消息的高过载负荷等级，通过SET OLCPULEVELCFG命令可以设置负荷等级对应CPU的实际占用率。当AMF负载高于该参数配置的负荷等级时，判定AMF处于严重过载状态。
highOlACT|严重过载下Overload Start消息中Overload Action信元设置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: REJECTNONEMCONNECT|本参数用于配置严重过载时，AMF发送给RAN侧的Overload Start消息中的Overload Action信元，基站根据该信元指示来控制对应类型的话务，包括：拒绝非紧急及非高优先级终端发起信令连接，拒绝新发起上行NAS信令连接，仅允许紧急及终呼信令连接，仅允许高优先级及终呼信令连接。
highOlTLRI|严重过载Traffic Load Reduction Indication信元设置|参数可选性: 任选参数类型: 数字参数范围: 1-99默认值: 20|本参数用于配置严重过载时，AMF发送给RAN侧的Overload Start消息中的Traffic Load Reduction Indication信元，基站根据该信元指示来控制对应类型话务的百分比，其中控制话务类型根据Overload Action信元决定，该值设置越大表示基站控制话务的占比越大。
olGNBNum|发送Overload Start的最大gNodeB个数|参数可选性: 任选参数类型: 数字参数范围: 1-128默认值: 64|本功能用于配置AMF允许发送Overload Start消息的最大gNodeB个数。
命令举例 
`
查看RAN侧过载控制配置参数信息。
SHOW OLTORANCFG
(No.1) : SHOW OLTORANCFG:
-----------------Namf_Communication_0----------------
操作维护       是否开启过载控制 N2口消息中是否携带切片信息 N2口发送Overload Start的低过载负荷等级 轻微过载下Overload Start消息中Overload Action信元设置 轻微过载Traffic Load Reduction Indication信元设置 N2口发送Overload Start的高过载负荷等级 严重过载下Overload Start消息中Overload Action信元设置 严重过载Traffic Load Reduction Indication信元设置 发送Overload Start的最大gNodeB个数 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           关闭             不携带                     二级负荷                               拒绝非紧急及非高优先级终端发起信令连接                10                                                一级负荷                               拒绝非紧急及非高优先级终端发起信令连接                20                                                64                                  
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-02-07 17:01:37 耗时: 0.286 秒
` 
# 状态码控制配置 
# 状态码控制配置 
背景知识 
AMF应支持对周边服务化接口的接收消息和发送消息分别进行流控，流控门限可配置，从而避免其它网元对AMF，以及AMF对其它网元造成信令冲击。AMF应支持服务化接口端到端的拥塞控制，包括以下原因值： 
 
503 Service Unavailable ，服务器处于过载状态，可以通过"Retry-After"的HTTP头指示重试时长。 
 
429 Too Many Requests，按照当前的业务量，服务器可能很快过载，可以通过"Retry-After"的HTTP头指示发送下一次请求消息时长。 
 
307 Temporary Redirect，服务器决定将请求消息重定向到另一个负荷较轻的服务器，Location头部携带目标服务器的URI。 
 
功能说明 
本功能用于设置及查询状态码控制。 
子主题： 
## 重定向状态码控制配置 
## 重定向状态码控制配置 
背景知识 
参见"状态码控制配置"中"307 Temporary Redirect"的描述。此配置用于设置每实例的控制门限及重定向的URI。 
功能说明 
本功能用于设置及查询重定向状态码控制参数。当AMF的“307状态码控制发送开关”打开时，才需要使用该功能。 
子主题： 
### 修改重定向状态码控制参数(SET REDIRSTATUSCODECFG) 
### 修改重定向状态码控制参数(SET REDIRSTATUSCODECFG) 
功能说明 
该命令用于增加重定向状态码控制参数。当AMF的“307状态码控制发送开关”打开时，使用该命令。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
threshold|控制门限|参数可选性: 必选参数类型: 数字参数范围: 1-500000|该参数用于配置AMF每实例PDU会话个数的控制门限。当PDU会话个数超过此门限时，AMF给SMF回复的Namf_N1N2 Message Transfer Response消息的Location头部中携带307的HTTP响应码，指示SMF进行AMF重定向。
redirectUri|重定向URI|参数可选性: 必选参数类型: 字符串参数范围: 1-255|该参数用于配置重定向的URI，当AMF发送307响应时在Location头部中携带。当启用307状态码发送功能时，可以使用此配置。如"http://192.0.2.16"。
命令举例 
`
设置控制门限为100000个，重定向URI为""http://192.0.2.16"。
SET REDIRSTATUSCODECFG:THRESHOLD=100000,REDIRECTURI="http://192.0.2.16"
` 
### 查询重定向状态码控制参数(SHOW REDIRSTATUSCODECFG) 
### 查询重定向状态码控制参数(SHOW REDIRSTATUSCODECFG) 
功能说明 
该命令用于查询重定向状态码控制参数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
threshold|控制门限|参数可选性: 任选参数类型: 数字参数范围: 1-500000|该参数用于配置AMF每实例PDU会话个数的控制门限。当PDU会话个数超过此门限时，AMF给SMF回复的Namf_N1N2 Message Transfer Response消息的Location头部中携带307的HTTP响应码，指示SMF进行AMF重定向。
redirectUri|重定向URI|参数可选性: 任选参数类型: 字符串参数范围: 1-255|该参数用于显示重定向的URI，当AMF发送307响应时在Location头部中携带。当启用307状态码发送功能时，可以使用此配置。如"http://192.0.2.16"。
命令举例 
`
查询重定向状态码控制参数。
SHOW REDIRSTATUSCODECFG
SHOW REDIRSTATUSCODECFG:
-----------------Namf_Communication_0----------------
控制门限    重定向URI
100000    http://192.0.2.16
记录数：1
执行成功耗时: 0.232 秒
` 
## 通用状态码控制配置 
## 通用状态码控制配置 
背景知识 
在接近过载或过载时，对服务化接口的对端NF发送的请求进行控制，从而降低网元负载，保障网元稳定运行。 
功能说明 
在接近过载或过载时，根据配置的接收消息门限以及服务化接口接收的消息情况，可以选择：对发送NF执行状态码过载控制，即对其回送429或503响应并携带重试时长，以便在此时间内抑制其主动发送请求。或者：可以选择对发送NF执行OCI控制，即对其发送OCI信息，以便其主动抑制发送请求。通过上述处理，来降低本网元负载。 
子主题： 
### 修改通用状态码控制或OCI控制参数命令(SET GENERALSTATUSCODECFG) 
### 修改通用状态码控制或OCI控制参数命令(SET GENERALSTATUSCODECFG) 
功能说明 
该命令用于查询通用状态码控制或OCI控制参数。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
NFTYPE|NF类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|用于设置此NF类型相关的控制参数。目前只支持对SMF和PCF执行状态码控制或OCI控制。OCI：Overload Control Information，过负荷控制信息。
MSGTHRESHOLD|每秒每实例接收消息数门限|参数可选性: 任选参数类型: 数字参数范围: 10-65535|每秒每实例接收单个NF请求消息数的门限。发送状态码429/503：当接近过载和过载时，对于超过此门限消息数的NF，会综合判断是否执行429状态码过载控制。执行429状态码过载控制是指，发送状态码429携带retry-after参数进行入向请求的抑制。综合判断后如果需要发送状态码429/503：当接近过载时，开始发送状态码429；过载后，开始发送状态码503。发送OCI：当满足OCI启控门限时，对于超过此门限消息数的NF，会综合判断是否发送OCI信息。
JUDGEPERCENT|比例门限|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 50|用于设置判定启动状态码控制的超消息数门限的实例数比例门限。当超过消息门限的实例数比例超过该比例门限配置值时，对此NF启动状态码控制。此处的消息数门限，即指“每秒每实例接收消息数门限”。
CTRLTOPNUM|执行状态码控制的NF个数|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|用于执行状态码429/503控制功能。当过载时，对于未执行429状态码控制的NF，选择本网元接收消息最多的若干个NF执行503状态码过载控制，NF个数由本参数值确定。
OCINFNUM|执行OCI控制的NF个数|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 5|用于执行OCI控制功能，选择若干个NF执行OCI控制，NF个数由本参数值确定。优先选择满足比例门限的NF。
ONLY503|仅发送503|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|用于设置当过载时，控制是否仅发送503状态码（即过载后对所有满足条件的NF都只发送503状态码）。缺省为NO，即功能关闭。
MINRETRYAFTER|时长最小取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|当执行状态码过载控制时，429或503响应消息中携带Retry-After参数。当执行OCI控制时，OCI信息会携带Period-of-Validity参数。上述两个参数取值在时长最小值与时长最大值的范围内随机选择。该参数用于指示时长的最小值。单位：秒。
MAXRETRYAFTER|时长最大取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 30|当执行状态码过载控制时，429或503响应消息中携带Retry-After参数。当执行OCI控制时，OCI信息会携带Period-of-Validity参数。上述两个参数取值在时长最小值与时长最大值的范围内随机选择。该参数用于指示时长的最大值。单位：秒。
命令举例 
`
修改通用状态码过载控制或OCI控制参数，NF类型是SMF，每秒每实例接收消息数门限是100，比例门限是50，执行状态码控制的NF个数是3，执行OCI控制的NF个数是5，仅发送503为关闭，时长最小取值是10，时长最大取值是30。
SET GENERALSTATUSCODECFG:NFTYPE="SMF",MSGTHRESHOLD=100,JUDGEPERCENT=50,CTRLTOPNUM=3,OCINFNUM=5,ONLY503="NO",MINRETRYAFTER=10,MAXRETRYAFTER=30
` 
### 查询通用状态码控制或OCI控制参数命令(SHOW GENERALSTATUSCODECFG) 
### 查询通用状态码控制或OCI控制参数命令(SHOW GENERALSTATUSCODECFG) 
功能说明 
该命令用于设置通用状态码过载控制或OCI控制参数。当AMF的“状态码控制发送开关”或“OCI发送开关”打开时，使用该命令。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NFTYPE|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|用于设置此NF类型相关的控制参数。目前只支持对SMF和PCF执行状态码控制或OCI控制。OCI：Overload Control Information，过负荷控制信息。
MSGTHRESHOLD|每秒每实例接收消息数门限|参数可选性: 任选参数类型: 数字参数范围: 10-65535|每秒每实例接收单个NF请求消息数的门限。发送状态码429/503：当接近过载和过载时，对于超过此门限消息数的NF，会综合判断是否执行429状态码过载控制。执行429状态码过载控制是指，发送状态码429携带retry-after参数进行入向请求的抑制。综合判断后如果需要发送状态码429/503：当接近过载时，开始发送状态码429；过载后，开始发送状态码503。发送OCI：当满足OCI启控门限时，对于超过此门限消息数的NF，会综合判断是否发送OCI信息。
JUDGEPERCENT|比例门限|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 50|用于设置判定启动状态码控制的超消息数门限的实例数比例门限。当超过消息门限的实例数比例超过该比例门限配置值时，对此NF启动状态码控制。此处的消息数门限，即指“每秒每实例接收消息数门限”。
CTRLTOPNUM|执行状态码控制的NF个数|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|用于执行状态码429/503控制功能。当过载时，对于未执行429状态码控制的NF，选择本网元接收消息最多的若干个NF执行503状态码过载控制，NF个数由本参数值确定。
OCINFNUM|执行OCI控制的NF个数|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 5|用于执行OCI控制功能，选择若干个NF执行OCI控制，NF个数由本参数值确定。优先选择满足比例门限的NF。
ONLY503|仅发送503|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|用于设置当过载时，控制是否仅发送503状态码（即过载后对所有满足条件的NF都只发送503状态码）。缺省为NO，即功能关闭。
MINRETRYAFTER|时长最小取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|当执行状态码过载控制时，429或503响应消息中携带Retry-After参数。当执行OCI控制时，OCI信息会携带Period-of-Validity参数。上述两个参数取值在时长最小值与时长最大值的范围内随机选择。该参数用于指示时长的最小值。单位：秒。
MAXRETRYAFTER|时长最大取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 30|当执行状态码过载控制时，429或503响应消息中携带Retry-After参数。当执行OCI控制时，OCI信息会携带Period-of-Validity参数。上述两个参数取值在时长最小值与时长最大值的范围内随机选择。该参数用于指示时长的最大值。单位：秒。
命令举例 
`
查询当前通用状态码控制或OCI控制配置信息
SHOW GENERALSTATUSCODECFG
SHOW GENERALSTATUSCODECFG:
-----------------Namf_Communication_0----------------
NF类型 每秒每实例接收消息数门限 比例门限 执行状态码控制的NF个数 执行OCI控制的NF个数 仅发送503  时长最小取值（秒） 时长最大取值（秒）
SMF    100                      50       3                      5                   否         10                 30
PCF    100                      50       3                      5                   否         10                 30
记录数：2
执行成功耗时: 1.333 秒
` 
## 状态码控制联动配置 
## 状态码控制联动配置 
背景知识 
AMF下游某类型的NF发生拥塞时，一般通过减少到此NF的话务可以缓解或恢复。若AMF下游某类型的NF大量或全部发生拥塞时，AMF可以通过启动AMF入向的NAS MM拥塞控制功能来延缓UE接入，整体减少网络话务，从而帮助拥塞的NF恢复正常工作状态。 
功能说明 
本功能用于配置状态码拥塞控制联动功能对应的NF类型及其控制参数。 
子主题： 
### 修改状态码控制联动配置(SET STATUSCTRLLINKAGECFG) 
### 修改状态码控制联动配置(SET STATUSCTRLLINKAGECFG) 
功能说明 
该命令用于修改指定状态码联动控制配置，当需要修改已有的指定NF的状态码联动控制配置时，可使用该命令。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于设置此NF类型的状态码拥塞控制联动参数。
linkageswitch|功能开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OFF|该参数用于设置是否启用对应NF类型的状态码拥塞控制联动功能。缺省为OFF，即功能关闭。
startthreshold|启动联动门限|参数可选性: 任选参数类型: 数字参数范围: 1-1024默认值: 10|该参数用于设置是否启动状态码拥塞控制联动延时定时器的NF门限。当下游同类型发送503的NF等于或超过“启动联动门限”的数量时，启动拥塞控制联动延时定时器，若定时器超时仍满足上述条件，则AMF启动入向NAS MM拥塞控制。注意：启动联动门限配置值需要大于解除联动门限配置值。
stopthreshold|解除联动门限|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|该参数用于设置是否解除状态码拥塞控制联动的NF门限。下游同类型发送503的NF低于或等于“解除联动门限”的数量，则解除拥塞控制联动，即解除因本功能而启动的NAS MM拥塞控制。注意：解除联动门限配置值需要小于启动联动门限配置值。
delaytime|延迟时间（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 20|该参数用于设置状态码拥塞控制联动的延时定时器时长。单位为秒。
命令举例 
`
修改状态码联动控制配置，NF类型为UDM，功能开关开启，启动门限为10，解除门限为0，延迟时间为20秒。
SET STATUSCTRLLINKAGECFG:NFTYPE="UDM",LINKAGESWITCH="ON",STARTTHRESHOLD=10,STOPTHRESHOLD=0,DELAYTIME=20
` 
### 查询状态码控制联动配置(SHOW STATUSCTRLLINKAGECFG) 
### 查询状态码控制联动配置(SHOW STATUSCTRLLINKAGECFG) 
功能说明 
该命令用于查询指定状态码联动控制配置的信息。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
nftype|NF类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-6|该参数用于显示此NF类型的状态码拥塞控制联动参数。
linkageswitch|功能开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OFF|该参数用于显示是否启用对应NF类型的状态码拥塞控制联动功能。缺省为OFF，即功能关闭。
startthreshold|启动联动门限|参数可选性: 任选参数类型: 数字参数范围: 1-1024默认值: 10|该参数用于显示是否启动状态码拥塞控制联动延时定时器的NF门限。当下游同类型发送503的NF等于或超过“启动联动门限”的数量时，启动拥塞控制联动延时定时器，若定时器超时仍满足上述条件，则AMF启动入向NAS MM拥塞控制。注意：启动联动门限配置值需要大于解除联动门限配置值。
stopthreshold|解除联动门限|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|该参数用于显示是否解除状态码拥塞控制联动的NF门限。下游同类型发送503的NF低于或等于“解除联动门限”的数量，则解除拥塞控制联动，即解除因本功能而启动的NAS MM拥塞控制。注意：解除联动门限配置值需要小于启动联动门限配置值。
delaytime|延迟时间（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 20|该参数用于显示状态码拥塞控制联动的延时定时器时长。单位为秒。
命令举例 
`
查询当前状态码联动控制配置信息。
SHOW STATUSCTRLLINKAGECFG
(No.1) : SHOW STATUSCTRLLINKAGECFG
-----------------Namf_Communication_0----------------
NF类型 功能开关 启动联动门限 解除联动门限 延迟时间（秒）
UDM    开启     10           0           20
AUSF   关闭     10           0           20
PCF    关闭     10           0           20
SMSF   关闭     10           0           20
NSSF   关闭     10           0           20
SMF    关闭     10           0           20
记录数：6
执行成功耗时: 0.076 秒
` 
## 指定状态码控制配置 
## 指定状态码控制配置 
背景知识 
参见"状态码控制配置"中"429 Too Many Requests"和"503 Service Unavailable"的描述。在接近过载或过载时，对服务化接口的对端NF发送的请求进行控制，从而降低网元负载，保障网元稳定运行。 
功能说明 
在接近过载或过载时，AMF根据配置的接收消息门限以及服务化接口接收的消息情况，可以选择对发送NF执行状态码过载控制，即对其回送429或503响应并携带重试时长，以便在此时间内抑制其主动发送请求，从而降低本AMF的负载。此功能用于特别指定NF实例的控制参数。 
子主题： 
### 增加指定状态码控制配置(ADD SPECSTATUSCODECFG) 
### 增加指定状态码控制配置(ADD SPECSTATUSCODECFG) 
功能说明 
该命令用于增加指定状态码控制配置，当需要增加一个指定NF的状态码控制时，可使用该命令。 
注意事项 
该命令执行后，结果立即生效。 
该命令最大只支持对10个NF实例进行控制。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
NFID|NF实例标识|参数可选性: 必选参数类型: 字符串参数范围: 0-100|该参数用于设置此NF相关的状态码控制参数，仅在需要特殊指定NF实例时使用。格式如下：采用UUID版本4格式（RFC 4122）。长度限制为128个bit。32个16进制数，以"-"分为5段标识，具体为：time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved  clock-seq-low "-" node。只能为a-f、0-9的字符。
MSGTHRESHOLD|每秒每实例接收消息门限|参数可选性: 必选参数类型: 数字参数范围: 10-65535|该参数用于设置每秒每实例接收单个NF采样消息的门限。当接近过载和过载时，对于超过此门限消息数的NF会综合判断是否执行429状态码过载控制。
JUDGEPERCENT|比例门限|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 50|该参数用于状态码控制开启时，设置判定超过消息数门限的实例数比例的门限。当超过消息门限的实例数比例超过比例门限时，对此NF启动状态码控制。
MINRETRYAFTER|重试时长最小取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|该参数用于设置Retry-After的最小值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
MAXRETRYAFTER|重试时长最大取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 30|该参数用于指示Retry-After的最大值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NFID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置此NF相关的状态码控制参数，仅在需要特殊指定NF实例时使用。格式如下：采用UUID版本4格式（RFC 4122）。长度限制为128个bit。32个16进制数，以"-"分为5段标识，具体为：time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved  clock-seq-low "-" node。只能为a-f、0-9的字符。
MSGTHRESHOLD|每秒每实例接收消息门限|参数可选性: 任选参数类型: 数字参数范围: 10-65535|该参数用于显示每秒每实例接收单个NF采样消息的门限。当接近过载和过载时，对于超过此门限消息数的NF会综合判断是否执行429状态码过载控制。
JUDGEPERCENT|比例门限|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 50|该参数用于状态码控制开启时，显示判定超过消息数门限的实例数比例的门限。当超过消息门限的实例数比例超过比例门限时，对此NF启动状态码控制。
MINRETRYAFTER|重试时长最小取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|该参数用于显示Retry-After的最小值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
MAXRETRYAFTER|重试时长最大取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 30|该参数用于显示Retry-After的最大值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
命令举例 
`
新增指定NF的状态码控制，NFID是33333333-7dec-11d0-a765-111111111111，每秒每实例接收消息门限是100，比例门限是50，重试时长最小值是10，重试时长最大值是30。
ADD SPECSTATUSCODECFG:NFID="33333333-7dec-11d0-a765-111111111111",MSGTHRESHOLD=100,JUDGEPERCENT=50,MINRETRYAFTER=10,MAXRETRYAFTER=30
` 
### 修改指定状态码控制配置(SET SPECSTATUSCODECFG) 
### 修改指定状态码控制配置(SET SPECSTATUSCODECFG) 
功能说明 
该命令用于修改指定状态码控制配置，当需要修改已有的指定NF的状态码控制时，可使用该命令。 
注意事项 
该命令执行后，结果立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
NFID|NF实例标识|参数可选性: 必选参数类型: 字符串参数范围: 0-100|该参数用于设置此NF相关的状态码控制参数，仅在需要特殊指定NF实例时使用。格式如下：采用UUID版本4格式（RFC 4122）。长度限制为128个bit。32个16进制数，以"-"分为5段标识，具体为：time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved  clock-seq-low "-" node。只能为a-f、0-9的字符。
MSGTHRESHOLD|每秒每实例接收消息门限|参数可选性: 任选参数类型: 数字参数范围: 10-65535|该参数用于设置每秒每实例接收单个NF采样消息的门限。当接近过载和过载时，对于超过此门限消息数的NF会综合判断是否执行429状态码过载控制。
JUDGEPERCENT|比例门限|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 50|该参数用于状态码控制开启时，设置判定超过消息数门限的实例数比例的门限。当超过消息门限的实例数比例超过比例门限时，对此NF启动状态码控制。
MINRETRYAFTER|重试时长最小取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|该参数用于设置Retry-After的最小值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
MAXRETRYAFTER|重试时长最大取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 30|该参数用于指示Retry-After的最大值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NFID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置此NF相关的状态码控制参数，仅在需要特殊指定NF实例时使用。格式如下：采用UUID版本4格式（RFC 4122）。长度限制为128个bit。32个16进制数，以"-"分为5段标识，具体为：time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved  clock-seq-low "-" node。只能为a-f、0-9的字符。
MSGTHRESHOLD|每秒每实例接收消息门限|参数可选性: 任选参数类型: 数字参数范围: 10-65535|该参数用于显示每秒每实例接收单个NF采样消息的门限。当接近过载和过载时，对于超过此门限消息数的NF会综合判断是否执行429状态码过载控制。
JUDGEPERCENT|比例门限|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 50|该参数用于状态码控制开启时，显示判定超过消息数门限的实例数比例的门限。当超过消息门限的实例数比例超过比例门限时，对此NF启动状态码控制。
MINRETRYAFTER|重试时长最小取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|该参数用于显示Retry-After的最小值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
MAXRETRYAFTER|重试时长最大取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 30|该参数用于显示Retry-After的最大值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
命令举例 
`
修改NFID是33333333-7dec-11d0-a765-111111111111的状态码控制配置，每秒每实例接收消息门限是110，比例门限是60。
SET SPECSTATUSCODECFG:NFID="33333333-7dec-11d0-a765-111111111111",MSGTHRESHOLD=110,JUDGEPERCENT=60
` 
### 删除指定状态码控制配置(DEL SPECSTATUSCODECFG) 
### 删除指定状态码控制配置(DEL SPECSTATUSCODECFG) 
功能说明 
该命令用于删除指定状态码控制配置，当需要删除一个指定NF的状态码控制时，可使用该命令。 
注意事项 
该命令执行后，结果立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
NFID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置此NF相关的状态码控制参数，仅在需要特殊指定NF实例时使用。格式如下：采用UUID版本4格式（RFC 4122）。长度限制为128个bit。32个16进制数，以"-"分为5段标识，具体为：time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved  clock-seq-low "-" node。只能为a-f、0-9的字符。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NFID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置此NF相关的状态码控制参数，仅在需要特殊指定NF实例时使用。格式如下：采用UUID版本4格式（RFC 4122）。长度限制为128个bit。32个16进制数，以"-"分为5段标识，具体为：time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved  clock-seq-low "-" node。只能为a-f、0-9的字符。
MSGTHRESHOLD|每秒每实例接收消息门限|参数可选性: 任选参数类型: 数字参数范围: 10-65535|该参数用于显示每秒每实例接收单个NF采样消息的门限。当接近过载和过载时，对于超过此门限消息数的NF会综合判断是否执行429状态码过载控制。
JUDGEPERCENT|比例门限|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 50|该参数用于状态码控制开启时，显示判定超过消息数门限的实例数比例的门限。当超过消息门限的实例数比例超过比例门限时，对此NF启动状态码控制。
MINRETRYAFTER|重试时长最小取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|该参数用于显示Retry-After的最小值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
MAXRETRYAFTER|重试时长最大取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 30|该参数用于显示Retry-After的最大值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
命令举例 
`
删除NFID是SMF_01的状态码控制配置。
DEL SPECSTATUSCODECFG:NFID="33333333-7dec-11d0-a765-111111111111"
` 
### 查询指定状态码控制配置(SHOW SPECSTATUSCODECFG) 
### 查询指定状态码控制配置(SHOW SPECSTATUSCODECFG) 
功能说明 
该命令用于查询指定状态码控制配置的信息。 
注意事项 
该命令执行后，结果立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
NFID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置此NF相关的状态码控制参数，仅在需要特殊指定NF实例时使用。格式如下：采用UUID版本4格式（RFC 4122）。长度限制为128个bit。32个16进制数，以"-"分为5段标识，具体为：time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved  clock-seq-low "-" node。只能为a-f、0-9的字符。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
NFID|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置此NF相关的状态码控制参数，仅在需要特殊指定NF实例时使用。格式如下：采用UUID版本4格式（RFC 4122）。长度限制为128个bit。32个16进制数，以"-"分为5段标识，具体为：time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved  clock-seq-low "-" node。只能为a-f、0-9的字符。
MSGTHRESHOLD|每秒每实例接收消息门限|参数可选性: 任选参数类型: 数字参数范围: 10-65535|该参数用于显示每秒每实例接收单个NF采样消息的门限。当接近过载和过载时，对于超过此门限消息数的NF会综合判断是否执行429状态码过载控制。
JUDGEPERCENT|比例门限|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 50|该参数用于状态码控制开启时，显示判定超过消息数门限的实例数比例的门限。当超过消息门限的实例数比例超过比例门限时，对此NF启动状态码控制。
MINRETRYAFTER|重试时长最小取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|该参数用于显示Retry-After的最小值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
MAXRETRYAFTER|重试时长最大取值（秒）|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 30|该参数用于显示Retry-After的最大值。当执行状态码过载控制时，429或503响应消息中携带Retry-After，此参数取值在Retry-After最小值与Retry-After最大值的范围内随机选择。
命令举例 
`
查询当前指定状态码控制NF配置信息。
SHOW SPECSTATUSCODECFG
(No.1) : SHOW SPECSTATUSCODECFG:
-----------------Namf_Communication_0----------------
NF实例标识                              每秒每实例接收消息门限 比例门限 重试时长最小取值（秒） 重试时长最大取值（秒）
33333333-7dec-11d0-a765-111111111111    100                   50       10                    30
记录数：1
执行成功耗时: 0.179 秒
` 
# 过负荷控制业务配置 
# 过负荷控制业务配置 
背景知识 
在系统CPU过负荷的情况下，AMF需要能够根据优先级，对业务消息进行区分处理，同时需要对超出正常处理能力的业务消息进行控制，以便恢复正常负荷状态，从而避免系统故障宕机。 
功能说明 
本功能用于配置消息及业务优先级，各接口入向业务消息最大通过量、业务权重及业务消息最大通过总量，以及各接口的出向业务消息最大通过量。 
子主题： 
## 保证通过量配置 
## 保证通过量配置 
背景知识 
保证通过量是指当CPU占用率达到拥塞，AMF启用CPU过负荷控制功能时，AMF最少仍需处理的消息个数。 
即无论CPU拥塞程度如何，当AMF启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的消息个数。 
功能说明 
本功能用于设置CPU过负荷控制时消息保证通过量。 
子主题： 
### 修改保证通过量配置(SET OLGUANUMCFG) 
### 修改保证通过量配置(SET OLGUANUMCFG) 
功能说明 
本命令用于设置AMF启用CPU过负荷控制功能时，每秒允许至少通过的消息个数。 
注意事项 
该命令在AMF启用CPU过负荷控制功能时，配置结果才会生效。 
通过[SET OVERLOADCFG]命令（Namf_MP模式下）设置“启用CPU过负荷控制”功能。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regGuaNum|初始注册每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 18|该参数用于设置AMF保证每秒通过的初始注册业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的初始注册消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
regUptGuaNum|注册更新每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 108|该参数用于设置AMF保证每秒通过的注册更新业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过注册更新消息数。 此处设置的个数针对单个SC（Service Component，服务组件）。
handoverGuaNum|切换每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 54|该参数用于设置AMF保证每秒通过的切换业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的切换请求消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
sevReqGuaNum|业务请求每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 300|该参数用于设置AMF保证每秒通过的业务请求业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的业务请求消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
pduSessGuaNum|PDU会话每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 18|该参数用于设置AMF保证每秒通过的PDU会话业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的PDU会话消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
ddnN1n2GuaNum|DDN类型的N1N2消息传输每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 138|该参数用于设置AMF保证每秒通过的DDN类型的N1N2消息业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的DDN类型的N1N2消息消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
pcfN1n2GuaNum|PCF类型的N1N2消息传输每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 30|该参数用于设置AMF保证每秒通过的PCF类型的N1N2消息业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的PCF类型的N1N2消息消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
pathSwitchGuaNum|Xn切换每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 186|该参数用于设置AMF保证每秒通过Xn切换业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的Xn切换消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
locRptGuaNum|Location Report每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 30|该参数用于设置AMF保证每秒通过Location Report业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的Location Report消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
periodicRegGuaNum|周期性注册每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 18|该参数用于设置AMF保证每秒通过的周期性注册业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的周期性注册消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
interSRGuaNum|局间业务请求每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 30|该参数用于设置AMF保证每秒通过的局间业务请求数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的局间业务请求数。局间业务请求是指：发起业务请求的用户并不是本AMF的用户，但由于用户所属的AMF故障，无线侧会将UE的业务请求发送给本AMF进行处理（相当于容灾场景）。在非全量备份情况下，由于没有PDF上文，业务请求会被本AMF拒绝。在全量备份的场景下，本AMF会根据容灾库内的用户信息进行处理，同时恢复承载，并通知周边网元（包括UDM，PCF等）。类似于位置改变的注册流程。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
设置各消息保证通过量为10。
SET OLGUANUMCFG:REGGUANUM=10,REGUPTGUANUM=10,HANDOVERGUANUM=10,SEVREQGUANUM=10,PDUSESSGUANUM=10,DDNN1N2GUANUM=10,PCFN1N2GUANUM=10,PERIODICREGGUANUM=10
` 
### 查询保证通过量配置(SHOW OLGUANUMCFG) 
### 查询保证通过量配置(SHOW OLGUANUMCFG) 
功能说明 
本命令用于查询AMF启用CPU过负荷控制功能时，每秒允许至少通过的消息个数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
regGuaNum|初始注册每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 18|该参数用于设置AMF保证每秒通过的初始注册业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的初始注册消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
regUptGuaNum|注册更新每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 108|该参数用于设置AMF保证每秒通过的注册更新业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过注册更新消息数。 此处设置的个数针对单个SC（Service Component，服务组件）。
handoverGuaNum|切换每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 54|该参数用于设置AMF保证每秒通过的切换业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的切换请求消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
sevReqGuaNum|业务请求每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 300|该参数用于设置AMF保证每秒通过的业务请求业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的业务请求消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
pduSessGuaNum|PDU会话每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 18|该参数用于设置AMF保证每秒通过的PDU会话业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的PDU会话消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
ddnN1n2GuaNum|DDN类型的N1N2消息传输每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 138|该参数用于设置AMF保证每秒通过的DDN类型的N1N2消息业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的DDN类型的N1N2消息消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
pcfN1n2GuaNum|PCF类型的N1N2消息传输每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 30|该参数用于设置AMF保证每秒通过的PCF类型的N1N2消息业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的PCF类型的N1N2消息消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
pathSwitchGuaNum|Xn切换每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 186|该参数用于设置AMF保证每秒通过Xn切换业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的Xn切换消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
locRptGuaNum|Location Report每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 30|该参数用于设置AMF保证每秒通过Location Report业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的Location Report消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
periodicRegGuaNum|周期性注册每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 18|该参数用于设置AMF保证每秒通过的周期性注册业务数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的周期性注册消息数。此处设置的个数针对单个SC（Service Component，服务组件）。
interSRGuaNum|局间业务请求每秒每实例保证通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 30|该参数用于设置AMF保证每秒通过的局间业务请求数，即无论CPU拥塞程度如何，AMF在启用CPU过负荷控制功能时，仍然需要确保每秒至少通过的局间业务请求数。局间业务请求是指：发起业务请求的用户并不是本AMF的用户，但由于用户所属的AMF故障，无线侧会将UE的业务请求发送给本AMF进行处理（相当于容灾场景）。在非全量备份情况下，由于没有PDF上文，业务请求会被本AMF拒绝。在全量备份的场景下，本AMF会根据容灾库内的用户信息进行处理，同时恢复承载，并通知周边网元（包括UDM，PCF等）。类似于位置改变的注册流程。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
查询消息保证通过量的配置值。
SHOW OLGUANUMCFG:
(No.1) : SHOW OLGUANUMCFG:
-----------------Namf_Communication_0----------------
操作维护       初始注册每秒每实例保证通过量 注册更新每秒每实例保证通过量 切换每秒每实例保证通过量 业务请求每秒每实例保证通过量 PDU会话每秒每实例保证通过量 DDN类型的N1N2消息传输每秒每实例保证通过量 PCF类型的N1N2消息传输每秒每实例保证通过量 Xn切换每秒每实例保证通过量 Location Report每秒每实例保证通过量 周期性注册每秒每实例保证通过量 局间业务请求每秒每实例保证通过量 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           18                           108                          54                       300                          18                          138                                       30                                        186                        30                                  18                             30                               
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
` 
## 优先级配置 
## 优先级配置 
背景知识 
在开启CPU过负荷功能情况下，AMF需要同时区分消息的优先级和业务的优先级，对优先级低的消息及优先级低的业务进行控制（丢弃处理），尽力保障对高优先级的消息及高优先级的业务进行及时处理。 
功能说明 
本功能用于配置消息优先级及业务优先级。 
子主题： 
### 消息优先级配置 
### 消息优先级配置 
背景知识 
每个NF需要从消息优先级和业务优先级两个角度来区分需要逐级控制的内容。 
 
在系统CPU占用率较低的情况下，AMF对低优先级的消息及业务进行控制（是否丢弃消息）。 
 
在系统CPU占用率较高的情况下，AMF在低优先级的消息及业务已完全控制（全部被丢弃）的情况下，开始控制高优先级消息及业务，直至系统负荷恢复正常。 
 
系统CPU占用率的控制原则如下。 
若CPU占用率超过[SET OLCPULEVELCFG]命令（Namf_MP模式下）配置的门限值，则AMF会启用CPU占用率的过负荷控制，根据各个级别的策略，决定是否丢弃收到的报文。
 
一级负荷
当CPU的实际占用率到达对应的数值时，AMF执行CPU占用率的过负荷控制的高负载控制，对高，中，低三个级别的报文均进行控制，丢弃所有的报文。 
 
二级负荷
当CPU的实际占用率到达对应的数值时，AMF执行CPU占用率的过负荷控制的低负载控制，只对中、低两个级别的报文进行控制，不对高优先级的报文进行控制，即只丢弃中、低两个级别的报文。 
 
三级负荷
当CPU的实际占用率到达对应的数值时，AMF不执行CPU占用率的过负荷控制，仅发送负荷情况的通知消息，用于提示操作员，当前的CPU负荷情况。 
 
四级负荷
当CPU的实际占用率到达对应的数值时，AMF不执行CPU占用率的过负荷控制，仅发送负荷情况的通知消息，用于提示操作员，当前的CPU负荷情况。 
 
功能说明 
本功能用于设置和查询过负荷控制消息优先级配置。 
子主题： 
#### 修改消息优先级配置(SET OLMSGPRIORITYCFG) 
#### 修改消息优先级配置(SET OLMSGPRIORITYCFG) 
功能说明 
该命令用于设置当AMF启用CPU过负荷控制功能时，业务的优先级。 
注意事项 
该命令在AMF启用CPU过负荷控制功能时，配置结果才会生效。 
通过[SET OVERLOADCFG]命令（Namf_MP模式下）设置“启用CPU过负荷控制”功能。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regPriority|初始注册优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“初始注册”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“初始注册”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“初始注册”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“初始注册”消息进行控制。
regUptPriority|移动性注册更新优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“移动性注册更新”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“注册更新”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“注册更新”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“注册更新”消息进行控制。
handoverPriority|切换优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“切换”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“切换”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“切换”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“切换”消息进行控制。
sevReqPriority|业务请求优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“业务请求”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“业务请求”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“业务请求”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“业务请求”消息进行控制。
pduSessPriority|PDU会话优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“PDU会话”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“PDU会话”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“PDU会话”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“PDU会话”消息进行控制。
ddnN1n2Priority|DDN类型的N1N2消息传输优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“DDN类型的N1N2”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“DDN类型的N1N2”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“DDN类型的N1N2”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“DDN类型的N1N2”消息进行控制。
pcfN1n2Priority|PCF类型的N1N2消息传输优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“PCF类型的N1N2消息”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“PCF类型的N1N2消息”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“PCF类型的N1N2消息”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“PCF类型的N1N2消息”消息进行控制。
pathSwitchPriority|Xn切换优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“Xn切换”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“Xn切换”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“Xn切换”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“Xn切换”消息进行控制。
locRptPriority|LOCATION REPORT优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“Location Report”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“Location Report”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“Location Report”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“Location Report”消息进行控制。
periodicRegPriority|周期性注册优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“周期性注册”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“周期性注册”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“周期性注册”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“周期性注册”消息进行控制。
命令举例 
`
修改消息优先级配置。
SET OLMSGPRIORITYCFG:REGPRIORITY="HIGHPRIORITY",REGUPTPRIORITY="HIGHPRIORITY",HANDOVERPRIORITY="HIGHPRIORITY",SEVREQPRIORITY="LOWPRIORITY",PDUSESSPRIORITY="HIGHPRIORITY",DDNN1N2PRIORITY="LOWPRIORITY",PCFN1N2PRIORITY="LOWPRIORITY",PATHSWITCHPRIORITY="LOWPRIORITY",PERIODICREGPRIORITY="LOWPRIORITY"
` 
#### 查询消息优先级配置(SHOW OLMSGPRIORITYCFG) 
#### 查询消息优先级配置(SHOW OLMSGPRIORITYCFG) 
功能说明 
该命令用于查询当AMF启用CPU过负荷控制功能时，业务的优先级。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
regPriority|初始注册优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“初始注册”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“初始注册”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“初始注册”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“初始注册”消息进行控制。
regUptPriority|移动性注册更新优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“移动性注册更新”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“注册更新”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“注册更新”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“注册更新”消息进行控制。
handoverPriority|切换优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“切换”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“切换”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“切换”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“切换”消息进行控制。
sevReqPriority|业务请求优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“业务请求”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“业务请求”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“业务请求”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“业务请求”消息进行控制。
pduSessPriority|PDU会话优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“PDU会话”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“PDU会话”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“PDU会话”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“PDU会话”消息进行控制。
ddnN1n2Priority|DDN类型的N1N2消息传输优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“DDN类型的N1N2”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“DDN类型的N1N2”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“DDN类型的N1N2”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“DDN类型的N1N2”消息进行控制。
pcfN1n2Priority|PCF类型的N1N2消息传输优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“PCF类型的N1N2消息”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“PCF类型的N1N2消息”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“PCF类型的N1N2消息”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“PCF类型的N1N2消息”消息进行控制。
pathSwitchPriority|Xn切换优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“Xn切换”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“Xn切换”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“Xn切换”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“Xn切换”消息进行控制。
locRptPriority|LOCATION REPORT优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOWPRIORITY|该参数用于设置“Location Report”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“Location Report”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“Location Report”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“Location Report”消息进行控制。
periodicRegPriority|周期性注册优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“周期性注册”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“周期性注册”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“周期性注册”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“周期性注册”消息进行控制。
命令举例 
`
查询消息优先级配置。
SHOW OLMSGPRIORITYCFG:
(No.1) : SHOW OLMSGPRIORITYCFG:
-----------------Namf_Communication_0----------------
操作维护       初始注册优先级 移动性注册更新优先级 切换优先级 业务请求优先级 PDU会话优先级 DDN类型的N1N2消息传输优先级 PCF类型的N1N2消息传输优先级 Xn切换优先级 LOCATION REPORT优先级 周期性注册优先级 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           低             高                   高         低             低            低                          低                          低           低                    高               
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
` 
### 业务优先级配置 
### 业务优先级配置 
背景知识 
每个NF需要从消息优先级和业务优先级两个角度来区分需要逐级控制的内容。 
 
在系统CPU占用率较低的情况下，AMF对低优先级的消息及业务进行控制（是否丢弃消息）。 
 
在系统CPU占用率较高的情况下，AMF在低优先级的消息及业务已完全控制（全部被丢弃）的情况下，开始控制高优先级消息及业务，直至系统负荷恢复正常。 
 
系统CPU占用率的控制原则如下。 
若CPU占用率超过[SET OLCPULEVELCFG]命令（Namf_MP模式下）配置的门限值，则AMF会启用CPU占用率的过负荷控制，根据各个级别的策略，决定是否丢弃收到的报文。
 
一级负荷
当CPU的实际占用率到达对应的数值时，AMF执行CPU占用率的过负荷控制的高负载控制，对高，中，低三个级别的报文均进行控制，丢弃所有的报文。 
 
二级负荷
当CPU的实际占用率到达对应的数值时，AMF执行CPU占用率的过负荷控制的低负载控制，只对中、低两个级别的报文进行控制，不对高优先级的报文进行控制，即只丢弃中、低两个级别的报文。 
 
三级负荷
当CPU的实际占用率到达对应的数值时，AMF不执行CPU占用率的过负荷控制，仅发送负荷情况的通知消息，用于提示操作员，当前的CPU负荷情况。 
 
四级负荷
当CPU的实际占用率到达对应的数值时，AMF不执行CPU占用率的过负荷控制，仅发送负荷情况的通知消息，用于提示操作员，当前的CPU负荷情况。 
 
功能说明 
本功能用于设置和查询过负荷控制业务优先级配置。 
子主题： 
#### 修改业务优先级配置(SET OLSRVPRIORITYCFG) 
#### 修改业务优先级配置(SET OLSRVPRIORITYCFG) 
功能说明 
该命令用于设置当AMF启用CPU过负荷控制功能时，MPS（Multimedia Priority Service，多媒体优先业务）业务和语音业务的优先级。 
注意事项 
该命令在AMF启用CPU过负荷控制功能时，配置结果才会生效。 
通过[SET OVERLOADCFG]命令（Namf_MP模式下）设置“启用CPU过负荷控制”功能。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mpsSrvPriority|MPS业务优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“MPS（Multimedia Priority Service，多媒体优先业务）业务”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“MPS业务”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“MPS业务”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“MPS业务”消息进行控制。
voiceSrvPriority|语音业务优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“语音业务”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“语音业务”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“语音业务”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“语音业务”消息进行控制。
命令举例 
`
修改业务优先级配置。
SET OLSRVPRIORITYCFG:MPSSRVPRIORITY="HIGHPRIORITY",VOICESRVPRIORITY="HIGHPRIORITY"
` 
#### 查询业务优先级配置(SHOW OLSRVPRIORITYCFG) 
#### 查询业务优先级配置(SHOW OLSRVPRIORITYCFG) 
功能说明 
该命令用于查询当AMF启用CPU过负荷控制功能时，MPS（Multimedia Priority Service，多媒体优先业务）业务和语音业务的优先级。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mpsSrvPriority|MPS业务优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“MPS（Multimedia Priority Service，多媒体优先业务）业务”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“MPS业务”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“MPS业务”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“MPS业务”消息进行控制。
voiceSrvPriority|语音业务优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HIGHPRIORITY|该参数用于设置“语音业务”消息的优先级，包括两个选项，高优先级和低优先级。设置消息为高优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）时，则AMF会对“语音业务”消息进行控制。如果当前CPU的负荷等级处于二级过负荷时（低过载）时，则AMF不会对“语音业务”消息进行控制。设置消息为低优先级时，当AMF启用CPU过负荷控制功能时，如果当前CPU的负荷等级处于一级过负荷（高过载）或者二级过负荷时（低过载）时，则AMF都会对“语音业务”消息进行控制。
命令举例 
`
查询业务优先级配置。
SHOW OLSRVPRIORITYCFG
(No.1) : SHOW OLSRVPRIORITYCFG:
-----------------Namf_Communication_0----------------
MPS业务优先级 语音业务优先级
高                    高
记录数：1
执行成功耗时: 0.072 秒
` 
## AMF自动业务控制策略配置 
## AMF自动业务控制策略配置 
背景知识 
AMF支持根据周边网元（AUSF，UDM等）返回的业务成功率来评判当前系统中是否存在拥塞，AMF通过限制接入的业务量，保证整个系统的业务正常。 
AMF自动业务控制策略配置功能是指AMF的周边网元（AUSF，UDM等）存在过载风险时，AMF根据周边网元返回的业务成功率的周期变化值，判断周边网元的负荷拥塞情况，以控制入向业务速率的方式来保护周边网元，通过调节初始注册、Inter-AMF业务请求、非本局GUTI的注册等业务流程的处理速率，控制AMF向周边网元发往的请求数，从而达到保护周边网元的目的。 
功能说明 
本功能用于设置AMF自动业务控制时的基本参数，包括流控控制周期、评判周期等。 
子主题： 
### 设置AMF自动业务控制基本参数(SET AMF AUTOCTL BASIC PARA) 
### 设置AMF自动业务控制基本参数(SET AMF AUTOCTL BASIC PARA) 
功能说明 
该命令用于设置AMF自动业务控制基本参数，包括控制周期、评判周期等。 
注意事项 
本命令执行后结果立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ctrltimer|业务采集周期（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-60默认值: 3|参数作用：本参数用于设置AMF自动业务控制算法计算业务通过数的周期（时间段），单位是秒，默认为5秒。修改影响：修改该参数会改变自动业务控制计算周期。数据来源：本端规划。默认值：5。配置原则：无。
judgetimer|评判周期/业务控制周期|参数可选性: 任选参数类型: 数字参数范围: 1-10默认值: 3|参数作用：本参数用于配置评判周期时长，即AMF自动识别周边网元拥塞控制时，动态调整当前允许通过业务数的频率。评判周期配置采用的是AMF自动业务控制周期的倍数。修改影响：修改本参数会改变评判周期。数据来源：本端规划。默认值：3。配置原则：无。
judgemethod|评判方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: MIXEDMODE|参数作用：本参数用于配置进行评判时，如何使用采集周期数据，在采集周期为5s，评判周期为3次情况下，配置为混合周期方式时，实际每5s进行一次评判，但使用的3个采集数据为前2个周期和当前周期的数据；配置为间隔周期方式时，实际15s进行一次评判，使用最近3次采集的数据。配置为混合周期方式，即每个采集周期都评判一次，使用当前和以前周期采集的数据，一起进行评判。配置为间隔周期方式，即每个评判周期评判一次，使用全新评判周期内，采集的数据。修改影响：修改该参数会改变评判方式。数据来源：本端规划。默认值：混合周期方式。配置原则：无。
islog|拥塞控制时是否上报日志|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：本参数用于控制在统一ALC流控时是否上报日志。修改影响：修改本参数会影响拥塞时日志是否上报。数据来源：本端规划。默认值：是。配置原则：无。
sysproc|被控制的流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4294967295默认值: INITIALREG&MOBILITYREGFROMOTHERAMF&INTERAMFREG&INTERAMFSERVICEREQ|参数作用：该参数用于配置被控制的业务流程。修改影响：修改本参数会改变流程是否受控。数据来源：本端规划。默认值：所有流程都受控。配置原则：无。
autolearnfg|是否开启自动学习|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CLOSED|参数作用：本参数为功能开关，根据此参数设置是否支持学习统一ALC流控的配置参数。修改影响：如开关关闭到开启需要重新清空数据。数据来源：本端规划。默认值：关闭。配置原则：无。
learntime|学习时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4294967295默认值: SIX&SEVEN&EIGHT&NINE&TEN&ELEVEN&TWELVE&THIRTEEN&FOURTEEN&FIFTEEN&SIXTEEN&SEVENTEEN&EIGHTEEN&NINETEEN&TWENTY&TWENTYONE&TWENTYTWO&TWENTYTHREE|参数作用：本参数用于设置自动学习时间端。默认 6到23点学习。0点到5点认为可能工程操作，该时间段避免学习。修改影响：修改该参数会影响自动学习时间段。数据来源：本端规划。默认值：6时至23时。配置原则：无。
命令举例 
`
设置AMF自动业务控制基本参数，设置业务采集周期为5秒。
SET AMF AUTOCTL BASIC PARA:CTRLTIMER=5
` 
### 查询AMF自动业务控制基本参数(SHOW AMF AUTOCTL BASIC PARA) 
### 查询AMF自动业务控制基本参数(SHOW AMF AUTOCTL BASIC PARA) 
功能说明 
该命令用于查询AMF自动业务控制基本参数。 
注意事项 
本命令执行后结果立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ctrltimer|业务采集周期（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-60默认值: 3|参数作用：本参数用于设置AMF自动业务控制算法计算业务通过数的周期（时间段），单位是秒，默认为5秒。
judgetimer|评判周期/业务控制周期|参数可选性: 任选参数类型: 数字参数范围: 1-10默认值: 3|参数作用：本参数用于配置评判周期时长，即AMF自动识别周边网元拥塞控制时，动态调整当前允许通过业务数的频率。评判周期配置采用的是AMF自动业务控制周期的倍数。
judgemethod|评判方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: MIXEDMODE|参数作用：本参数用于配置进行评判时，如何使用采集周期数据，在采集周期为5s，评判周期为3次情况下，配置为混合周期方式时，实际每5s进行一次评判，但使用的3个采集数据为前2个周期和当前周期的数据；配置为间隔周期方式时，实际15s进行一次评判，使用最近3次采集的数据。配置为混合周期方式，即每个采集周期都评判一次，使用当前和以前周期采集的数据，一起进行评判。配置为间隔周期方式，即每个评判周期评判一次，使用全新评判周期内，采集的数据。
islog|拥塞控制时是否上报日志|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：本参数用于控制在统一ALC流控时是否上报日志。
sysproc|被控制的流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4294967295默认值: INITIALREG&MOBILITYREGFROMOTHERAMF&INTERAMFREG&INTERAMFSERVICEREQ|参数作用：该参数用于配置被控制的业务流程。
autolearnfg|是否开启自动学习|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CLOSED|参数作用：本参数为功能开关，根据此参数设置是否支持学习统一ALC流控的配置参数。
learntime|学习时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4294967295默认值: SIX&SEVEN&EIGHT&NINE&TEN&ELEVEN&TWELVE&THIRTEEN&FOURTEEN&FIFTEEN&SIXTEEN&SEVENTEEN&EIGHTEEN&NINETEEN&TWENTY&TWENTYONE&TWENTYTWO&TWENTYTHREE|参数作用：本参数用于设置自动学习时间端。默认 6到23点学习。0点到5点认为可能工程操作，该时间段避免学习。
命令举例 
`
查询AMF自动业务控制基本参数。
SHOW AMF AUTOCTL BASIC PARA
(No.1) : SHOW AMF AUTOCTL BASIC PARA:
-----------------Namf_Communication_0----------------
操作维护       业务采集周期（秒） 评判周期/业务控制周期 评判方式 拥塞控制时是否上报日志 立刻开启日志 被控制的流程                                                                                    是否开启自动学习 学习时间                                                                                                                  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           3                  3                    混合周期方式    是                     0            初始注册流程&局间位置改变注册流程&全量容灾导致的他局用户注册流程&全量容灾导致的他局业务请求流程 关闭             六点&七点&八点&九点&十点&十一点&十二点&十三点&十四点&十五点&十六点&十七点&十八点&十九点&二十点&二十一点&二十二点&二十三点 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
` 
### 设置AMF N8N12 自动业务控制策略(SET AMF N8N12 AUTO CNGCTL) 
### 设置AMF N8N12 自动业务控制策略(SET AMF N8N12 AUTO CNGCTL) 
功能说明 
该命令用于设置N8N12口局向统一自动业务控制策略，当运营商要求对N8N12接口所有的AUSF/UDM局向进行统一ALC流控时，使用此命令设置流控参数。 
注意事项 
本命令执行后结果立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
flg|是否开启流控|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数为流控功能开关,用于设置是否支持N8N12口的统一ALC流控。修改影响：修改该参数会改变是否支持N8N12口的统一ALC流控。数据来源：本端规划。默认值：否。配置原则：无。
startcaps|触发拥塞的接入业务通过数量（单SC每秒）|参数可选性: 任选参数类型: 数字参数范围: 1-1000默认值: 120|参数作用：本参数用于配置触发拥塞的接入业务通过数量，只有在本SC每秒的业务数量（包括初始注册、局间位置改变注册流程、全量容灾导致的他局用户注册流程、全量容灾导致的他局业务请求流程）超过配置的值时，才可能会触发本功能。修改影响：修改本参数会改变触发拥塞的接入业务通过数量。数据来源：本端规划。默认值：120。配置原则：无。
limitcaps|初始限制的接入业务最大数量（单SC每秒）|参数可选性: 任选参数类型: 数字参数范围: 1-1000默认值: 300|参数作用：本参数用于配置初始限制的接入业务最大数量，只有在本SC每秒的业务数量（包括初始注册、局间位置改变注册流程、全量容灾导致的他局用户注册流程、全量容灾导致的他局业务请求流程）超过配置的值时，即使成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。修改影响：修改本参数会改变初始限制的接入业务最大数量。数据来源：本端规划。默认值：300。配置原则：无。
maxcaps|允许通过的接入业务最大数量（单SC每秒）|参数可选性: 任选参数类型: 数字参数范围: 1-10000默认值: 1800|参数作用：本参数用于配置本SC每秒最多允许通过的业务数量。修改影响：修改本参数会改变允许通过的接入业务最大数量。数据来源：本端规划。默认值：1800。配置原则：无。
succrate|触发拥塞的业务成功率（%）|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 80|参数作用：本参数用于配置触发拥塞的业务成功率，只有在业务成功率低于本配置时，才可能会触发本流控功能。修改影响：修改本参数会改变触发拥塞的业务成功率。数据来源：本端规划。默认值：80。配置原则：无。
goalsuccrate|触发提升通过业务数量的业务成功率（%）|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 90|参数作用：本参数用于配置触发拥塞的业务成功率，在触发本功能后，只要在业务成功率高于本配置时，就会继续提升通过的业务数量，尽量放行业务。修改影响：修改本参数会改变触发提升通过业务数量的业务成功率。数据来源：本端规划。默认值：90。配置原则：无。
step|接入业务控制步长|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 10|参数作用：本参数用于配置接入业务控制步长，一旦业务成功率降低（低于成功门限），且接入本模块的业务数也很高（高于业务门限），就会触发控制功能。如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。修改影响：修改本参数会改变接入业务控制步长。数据来源：本端规划。默认值：10。配置原则：无。
stepmethod|步长使用方法|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: DYNAMIC|参数作用：本参数用于配置是否使用动态计算调整步长的方法。修改影响：修改本参数会改变步长使用方法。数据来源：本端规划。默认值：动态二分法。配置原则：无。
lastime|控制持续时间（分钟）|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 5|参数作用：本参数用于配置控制持续时间。在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。 修改影响：修改本参数会改变控制持续时间。数据来源：本端规划。默认值：5。配置原则：无。
succeedmsg|用于成功率统计的服务操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4294967295默认值: UDMUECMREGREQ&UDMUECMDEREGREQ&UDMUECMUPTREQ&UDMSDMGETNSSAIDATAREQ&UDMSDMGETAMDATAREQ&UDMSDMGETSMFDATAREQ&UDMSDMGETSMSDATAREQ&UDMSDMGETUECTXINSMFDATAREQ&UDMSDMGETUECTXINSMSFDATAREQ&UDMSDMGETLCSMODATAREQ&UDMSDMGETMULTIDATAREQ&UDMSDMSUBREQ&UDMSDMUNSUBREQ&UDMSDMACKINFOREQ&AUSFAUTHREQ&AUSFAUTHCONFRIM&AUSFAUTHREAPSESSION|参数作用：本参数用于配置哪些服务操作用于计算成功率。在过负荷中，并非所有的服务操作会被控制。修改影响：修改本参数会影响服务成功率的计算。数据来源：本端规划。默认值：所有AMF发出的N8N12请求消息。配置原则：无。
excludeerrcode|被排除的错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4294967295|参数作用：本参数用于设置响应中接收到对应错误也认为是成功的响应码。修改影响：修改该参数会影响业务成功率的统计。数据来源：本端规划。默认值：无。配置原则：无。
autolimit|使用自动门限配置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: MAUNAL|参数作用：本参数为自动控制功能开关，开启后将自动触发拥塞，自动限制，开启时要求自动学习开关也开启。修改影响：修改该参数会影响自动控制功能。数据来源：本端规划。默认值：人工。配置原则：无。
命令举例 
`
设置AMF自动业务控制基本参数，设置触发拥塞的接入业务通过数量为120。
SET AMF N8N12 AUTO CNGCTL:STARTCAPS=120
` 
### 查询AMF N8N12 自动业务控制策略(SHOW AMF N8N12 AUTO CNGCTL) 
### 查询AMF N8N12 自动业务控制策略(SHOW AMF N8N12 AUTO CNGCTL) 
功能说明 
该命令用于查询AMF N8N12 自动业务控制策略。 
注意事项 
本命令执行后结果立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
flg|是否开启流控|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数为流控功能开关,用于设置是否支持N8N12口的统一ALC流控。
startcaps|触发拥塞的接入业务通过数量（单SC每秒）|参数可选性: 任选参数类型: 数字参数范围: 1-1000默认值: 120|参数作用：本参数用于配置触发拥塞的接入业务通过数量，只有在本SC每秒的业务数量（包括初始注册、局间位置改变注册流程、全量容灾导致的他局用户注册流程、全量容灾导致的他局业务请求流程）超过配置的值时，才可能会触发本功能。
limitcaps|初始限制的接入业务最大数量（单SC每秒）|参数可选性: 任选参数类型: 数字参数范围: 1-1000默认值: 300|参数作用：本参数用于配置初始限制的接入业务最大数量，只有在本SC每秒的业务数量（包括初始注册、局间位置改变注册流程、全量容灾导致的他局用户注册流程、全量容灾导致的他局业务请求流程）超过配置的值时，即使成功率高于门限，也会触发本功能，使初始业务速率不能大于该数值 。
maxcaps|允许通过的接入业务最大数量（单SC每秒）|参数可选性: 任选参数类型: 数字参数范围: 1-10000默认值: 1800|参数作用：本参数用于配置本SC每秒最多允许通过的业务数量。
succrate|触发拥塞的业务成功率（%）|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 80|参数作用：本参数用于配置触发拥塞的业务成功率，只有在业务成功率低于本配置时，才可能会触发本流控功能。
goalsuccrate|触发提升通过业务数量的业务成功率（%）|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 90|参数作用：本参数用于配置触发拥塞的业务成功率，在触发本功能后，只要在业务成功率高于本配置时，就会继续提升通过的业务数量，尽量放行业务。
step|接入业务控制步长|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 10|参数作用：本参数用于配置接入业务控制步长，一旦业务成功率降低（低于成功门限），且接入本模块的业务数也很高（高于业务门限），就会触发控制功能。如果业务被控制后，成功率增高，则会逐渐提升通过数量，即本配置的值。反之也会使用本配置的值，逐渐降低通过数量。
stepmethod|步长使用方法|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: DYNAMIC|参数作用：本参数用于配置是否使用动态计算调整步长的方法。修改影响：修改本参数会改变步长使用方法。数据来源：本端规划。默认值：动态二分法。配置原则：无。
lastime|控制持续时间（分钟）|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 5|参数作用：本参数用于配置控制持续时间。在进行控制状态后，一旦业务不再增多，没有继续被控制。在持续本配置的时长后，恢复正常。
succeedmsg|用于成功率统计的服务操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4294967295默认值: UDMUECMREGREQ&UDMUECMDEREGREQ&UDMUECMUPTREQ&UDMSDMGETNSSAIDATAREQ&UDMSDMGETAMDATAREQ&UDMSDMGETSMFDATAREQ&UDMSDMGETSMSDATAREQ&UDMSDMGETUECTXINSMFDATAREQ&UDMSDMGETUECTXINSMSFDATAREQ&UDMSDMGETLCSMODATAREQ&UDMSDMGETMULTIDATAREQ&UDMSDMSUBREQ&UDMSDMUNSUBREQ&UDMSDMACKINFOREQ&AUSFAUTHREQ&AUSFAUTHCONFRIM&AUSFAUTHREAPSESSION|参数作用：本参数用于配置哪些服务操作用于计算成功率。在过负荷中，并非所有的服务操作会被控制。
excludeerrcode|被排除的错误码|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4294967295|参数作用：本参数用于设置响应中接收到对应错误也认为是成功的响应码。
autolimit|使用自动门限配置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: MAUNAL|参数作用：本参数为自动控制功能开关，开启后将自动触发拥塞，自动限制，开启时要求自动学习开关也开启。
命令举例 
`
查询N8N12口局向统一自动业务控制策略。
SHOW AMF N8N12 AUTO CNGCTL
(No.1) : SHOW AMF N8N12 AUTO CNGCTL:
-----------------Namf_Communication_0----------------
操作维护       是否开启流控 触发拥塞的接入业务通过数量（单SC每秒） 初始限制的接入业务最大数量（单SC每秒） 允许通过的接入业务最大数量（单SC每秒） 触发拥塞的业务成功率（%） 触发提升通过业务数量的业务成功率（%） 接入业务控制步长 步长使用方法 控制持续时间（分钟） 用于成功率统计的服务操作                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  被排除的错误码 使用自动门限配置 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           否           120                                    300                                    1800                                   80                        90                                    10               动态二分法   5                    Nudm_UECM_Registration Request&Nudm_UECM_Deregistration Request&Nudm_UECM_Update Request&Nudm_SDM_Get_Nssai_Data Request&Nudm_SDM_Get_Am_Data Request&Nudm_SDM_Get_Smf_Select_Data Request&Nudm_SDM_Get_Sms_Data Request&Nudm_SDM_Get_Ue_Ctx_In_Smf_Data Request&Nudm_SDM_Get_Ue_Ctx_In_Smsf_Data Request&Nudm_SDM_Get_Lcs_Mo_Data Request&Nudm_SDM_Get_Multiple_Data Request&Nudm_SDM_Subscribe Request&Nudm_SDM_UnSubscribe Request&Nudm_SDM_Ack_Info Request&Nausf_UEAuthentication_Authenticate Request&Nausf_UEAuthentication_Authenticate Confirm&Nausf_UEAuthentication_EapSession                人工             
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
` 
## 入向业务容量配置 
## 入向业务容量配置 
背景知识 
为有效控制系统负荷，AMF需要对各个接口的入向业务消息个数进行控制，对于超出本功能配置数量的消息，AMF不再进行处理。 
功能说明 
本功能用于配置N2接口及SBI接口入向各业务消息的最大通过量及权重，以及入向业务消息的通过总量。 
子主题： 
### N2入向业务容量配置 
### N2入向业务容量配置 
背景知识 
N2接口是NR和AMF之间的接口，用于NR和AMF间的上下文管理、会话管理等消息的交互，具体功能包括： 
 
初始注册及周期性注册 
 
位置更新 
 
业务请求 
 
上行NAS转发 
 
切换 
 
上行NAS配置转发 
 
AMF可以根据每实例（SC）每秒最大通过的消息个数及业务权重这两个条件，对N2接口的消息进行过负荷入向控制。 
功能说明 
本功能用于设置和查询N2接口入向消息过负荷控制。 
子主题： 
#### 新增N2入向业务配置(ADD OLINPUTN2SRVCFG) 
#### 新增N2入向业务配置(ADD OLINPUTN2SRVCFG) 
功能说明 
该命令用于新增AMF启用业务通过量负荷控制功能时，N2接口入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
 
本命令执行后，配置立即生效。 
 
执行本命令之前，需要确认已经启用业务通过量负荷控制功能，即通过SET OVERLOADCFG命令（Namf_MP模式下）设置参数“启用业务通过量负荷控制(srvSwitch)”为“开启(SRVSWITCHON)”，否则本命令无法生效。 
 
该命令用于控制N2接口的入向业务量，为避免过量的入向业务对系统造成影响。修改配置值需要在中兴通讯技术支持的指导下进行。 
 
该命令设置的参数“过负荷控制业务权重（OLWEIGHT）”用于入向业务总量控制功能，来计算N2接口入向所有业务类型的消息个数总和。在统计某个接口的某种业务类型消息的入向业务总量时，如果本参数设置的该类型消息的权重是2， 表示该消息的数量需要×2。入向业务总量控制功能通过SET OLTOTALNUMCFG命令进行配置。 
 
系统的业务数据完成后，本命令已经存在初始配置值，如果运营商没有特殊需求，无需修改，按初始配置值生效。
该命令最多只能配置7条记录。
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-10|参数作用：该参数用于设置AMF的N2接口的入向业务类型，包括初始注册等。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
olMaxNum|N2口入向业务每秒每实例最大通过量|参数可选性: 必选参数类型: 数字参数范围: 10-65535默认值: 65535|参数作用：该参数用于设置AMF当前业务类型的N2接口入向业务每秒每实例最大通过量。修改影响：无。数据来源：本端规划。默认值：65535。配置原则：本参数设置为65535，表示AMF不会对当前业务类型的N2接口入向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 必选参数类型: 数字参数范围: 1-100|参数作用：该参数用于设置AMF当前类型的N2接口入向业务的过负荷控制业务权重。该参数在统计AMF的入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|参数作用：该参数用于设置AMF的N2接口的入向业务类型，包括初始注册等。
olMaxNum|N2口入向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|参数作用：该参数用于设置AMF当前业务类型的N2接口入向业务每秒每实例最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的N2接口入向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|参数作用：该参数用于设置AMF当前类型的N2接口入向业务的过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
命令举例 
`
新增初始注册消息最大通过量为100和权重为50。
ADD OLINPUTN2SRVCFG:SRVTYPE="REGISTRATION",OLMAXNUM=100,OLWEIGHT=50
` 
#### 修改N2入向业务配置(SET OLINPUTN2SRVCFG) 
#### 修改N2入向业务配置(SET OLINPUTN2SRVCFG) 
功能说明 
该命令用于修改AMF启用业务通过量负荷控制功能时，N2接口入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
 
本命令执行后，配置立即生效。 
 
执行本命令之前，需要确认已经启用业务通过量负荷控制功能，即通过SET OVERLOADCFG命令（Namf_MP模式下）设置参数“启用业务通过量负荷控制(srvSwitch)”为“开启(SRVSWITCHON)”，否则本命令无法生效。 
 
该命令用于控制N2接口的入向业务量，为避免过量的入向业务对系统造成影响。修改配置值需要在中兴通讯技术支持的指导下进行。 
 
该命令设置的参数“过负荷控制业务权重（OLWEIGHT）”用于入向业务总量控制功能，来计算N2接口入向所有业务类型的消息个数总和。在统计某个接口的某种业务类型消息的入向业务总量时，如果本参数设置的该类型消息的权重是2， 表示该消息的数量需要×2。入向业务总量控制功能通过SET OLTOTALNUMCFG命令进行配置。 
 
系统的业务数据完成后，本命令已经存在初始配置值，如果运营商没有特殊需求，无需修改，按初始配置值生效。
该命令最多只能配置7条记录。
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-10|参数作用：该参数用于设置AMF的N2接口的入向业务类型，包括初始注册等。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
olMaxNum|N2口入向业务每秒每实例最大通过量|参数可选性: 必选参数类型: 数字参数范围: 10-65535默认值: 65535|参数作用：该参数用于设置AMF当前业务类型的N2接口入向业务每秒每实例最大通过量。修改影响：无。数据来源：本端规划。默认值：65535。配置原则：本参数设置为65535，表示AMF不会对当前业务类型的N2接口入向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|参数作用：该参数用于设置AMF当前类型的N2接口入向业务的过负荷控制业务权重。该参数在统计AMF的入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|参数作用：该参数用于设置AMF的N2接口的入向业务类型，包括初始注册等。
olMaxNum|N2口入向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|参数作用：该参数用于设置AMF当前业务类型的N2接口入向业务每秒每实例最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的N2接口入向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|参数作用：该参数用于设置AMF当前类型的N2接口入向业务的过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
命令举例 
`
修改初始注册消息最大通过量100和权重为50。
SET OLINPUTN2SRVCFG:SRVTYPE="REGISTRATION",OLMAXNUM=100,OLWEIGHT=50
` 
#### 删除N2入向业务配置(DEL OLINPUTN2SRVCFG) 
#### 删除N2入向业务配置(DEL OLINPUTN2SRVCFG) 
功能说明 
该命令用于删除AMF启用业务通过量负荷控制功能时，N2接口入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
本命令执行后，配置立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-10|参数作用：该参数用于设置AMF的N2接口的入向业务类型，包括初始注册等。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|参数作用：该参数用于设置AMF的N2接口的入向业务类型，包括初始注册等。
olMaxNum|N2口入向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|参数作用：该参数用于设置AMF当前业务类型的N2接口入向业务每秒每实例最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的N2接口入向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|参数作用：该参数用于设置AMF当前类型的N2接口入向业务的过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
命令举例 
`
删除初始注册消息最大通过量和权重配置。
DEL OLINPUTN2SRVCFG:SRVTYPE="REGISTRATION"
` 
#### 查询N2入向业务配置(SHOW OLINPUTN2SRVCFG) 
#### 查询N2入向业务配置(SHOW OLINPUTN2SRVCFG) 
功能说明 
该命令用于查询AMF启用业务通过量负荷控制功能时，N2接口入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
该命令配置的参数“过负荷控制业务权重（OLWEIGHT）”用于入向业务总量控制功能，删除后会影响到入向业务总量计算。入向业务总量控制功能通过[SET OLTOTALNUMCFG]命令进行配置。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|参数作用：该参数用于设置AMF的N2接口的入向业务类型，包括初始注册等。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|参数作用：该参数用于设置AMF的N2接口的入向业务类型，包括初始注册等。
olMaxNum|N2口入向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|参数作用：该参数用于设置AMF当前业务类型的N2接口入向业务每秒每实例最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的N2接口入向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|参数作用：该参数用于设置AMF当前类型的N2接口入向业务的过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
命令举例 
`
查询初始注册消息最大通过量和权重配置。
SHOW OLINPUTN2SRVCFG:SRVTYPE="REGISTRATION"
(No.1) : SHOW OLINPUTN2SRVCFG:SRVTYPE="REGISTRATION"
-----------------Namf_Communication_0----------------
业务类型                     N2接口入向业务每秒每实例最大通过量  过负荷控制业务权重
初始注册                     100                               50
记录数：1
执行成功耗时: 0.102 秒
` 
### SBI入向业务容量配置 
### SBI入向业务容量配置 
背景知识 
AMF可以根据每实例（SC）每秒最大通过的消息个数，对SBI（Service Based Interface，基于服务的接口）入向的多种消息（如事件暴露订阅）进行控制。 
功能说明 
本功能用于设置和查询SBI（Service Based Interface，基于服务的接口）入向消息过负荷控制参数配置。 
子主题： 
#### 新增SBI入向业务配置(ADD OLINPUTSBISRVCFG) 
#### 新增SBI入向业务配置(ADD OLINPUTSBISRVCFG) 
功能说明 
该命令用于新增AMF启用业务通过量负荷控制功能时，SBI（Service Based Interface，基于服务的接口）入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
该命令在AMF启用业务通过量负荷控制功能时，配置结果才会生效。 
启用业务通过量负荷控制功能，即通过[SET OVERLOADCFG]命令（Namf_MP模式下）设置“启用业务通过量负荷控制(srvSwitch)”为“开启(SRVSWITCHON)”。
通过本命令，AMF支持对SBI接口入向的各种业务类型的消息个数进行限制。AMF同时支持对SBI接口入向所有的业务类型的消息个数的总和进行控制（即SBI接口入向各种业务类型的消息个数总和不能超过系统的配置值）。 
SBI接口入向所有业务类型的消息个数总和是通过[SET OLTOTALNUMCFG]命令（Namf_Communication模式下）配置的参数“每秒每实例SBI口入向控制总量(olInputSbiTotalNum)”配置的。
如果SBI接口入向的某种业务类型的消息个数没有超过本命令设置的数值，但是如果此时SBI接口入向所有业务类型的消息个数总和超过[SET OLTOTALNUMCFG]命令命令配置的总和，则AMF此时仍然会对此种业务类型的消息进行限制。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-10|该参数用于设置AMF的SBI的入向业务类型，包括NF状态通知等。
olMaxNum|SBI口入向业务每秒每实例最大通过量|参数可选性: 必选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前业务类型的SBI入向业务每秒每实例（SC）最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的SBI入向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 必选参数类型: 数字参数范围: 1-100|该参数用于设置AMF当前类型的SBI入向业务过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|该参数用于设置AMF的SBI的入向业务类型，包括NF状态通知等。
olMaxNum|SBI口入向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI入向业务每秒每实例（SC）最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的SBI入向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|该参数用于设置AMF当前类型的SBI入向业务过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
命令举例 
`
新增PDU建立请求类型的N1N2转发消息最大通过量为100和权重为50。
ADD OLINPUTSBISRVCFG:SRVTYPE="N1N2TRANSPDUSETUP",OLMAXNUM=100,OLWEIGHT=50
` 
#### 修改SBI入向业务配置(SET OLINPUTSBISRVCFG) 
#### 修改SBI入向业务配置(SET OLINPUTSBISRVCFG) 
功能说明 
该命令用于修改AMF启用业务通过量负荷控制功能时，SBI（Service Based Interface，基于服务的接口）入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-10|该参数用于设置AMF的SBI的入向业务类型，包括NF状态通知等。
olMaxNum|SBI口入向业务每秒每实例最大通过量|参数可选性: 必选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前业务类型的SBI入向业务每秒每实例（SC）最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的SBI入向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|该参数用于设置AMF当前类型的SBI入向业务过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|该参数用于设置AMF的SBI的入向业务类型，包括NF状态通知等。
olMaxNum|SBI口入向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI入向业务每秒每实例（SC）最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的SBI入向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|该参数用于设置AMF当前类型的SBI入向业务过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
命令举例 
`
修改PDU建立请求类型的N1N2转发消息最大通过量为100和权重为50。
SET OLINPUTSBISRVCFG:SRVTYPE="N1N2TRANSPDUSETUP",OLMAXNUM=100,OLWEIGHT=50
` 
#### 删除SBI入向业务配置(DEL OLINPUTSBISRVCFG) 
#### 删除SBI入向业务配置(DEL OLINPUTSBISRVCFG) 
功能说明 
该命令用于删除AMF启用业务通过量负荷控制功能时，SBI（Service Based Interface，基于服务的接口）入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-10|该参数用于设置AMF的SBI的入向业务类型，包括NF状态通知等。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|该参数用于设置AMF的SBI的入向业务类型，包括NF状态通知等。
olMaxNum|SBI口入向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI入向业务每秒每实例（SC）最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的SBI入向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|该参数用于设置AMF当前类型的SBI入向业务过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
命令举例 
`
删除PDU建立请求类型的N1N2转发消息最大通过量和权重配置。
DEL OLINPUTSBISRVCFG:SRVTYPE="N1N2TRANSPDUSETUP"
` 
#### 查询SBI入向业务配置(SHOW OLINPUTSBISRVCFG) 
#### 查询SBI入向业务配置(SHOW OLINPUTSBISRVCFG) 
功能说明 
该命令用于查询AMF启用业务通过量负荷控制功能时，SBI（Service Based Interface，基于服务的接口）入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|该参数用于设置AMF的SBI的入向业务类型，包括NF状态通知等。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-10|该参数用于设置AMF的SBI的入向业务类型，包括NF状态通知等。
olMaxNum|SBI口入向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI入向业务每秒每实例（SC）最大通过量。本参数设置为65535，表示AMF不会对当前业务类型的SBI入向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olWeight|过负荷控制业务权重|参数可选性: 任选参数类型: 数字参数范围: 1-100|该参数用于设置AMF当前类型的SBI入向业务过负荷控制业务权重。该参数用于统计入向业务总量时使用，在统计某个接口的某种业务类型消息的入向业务总量时，如果该类型消息的权重是2， 表示该消息的数量需要×2。
命令举例 
`
查询PDU建立请求类型的N1N2转发消息最大通过量和权重配置。
SHOW OLINPUTSBISRVCFG:SRVTYPE="N1N2TRANSPDUSETUP"
(No.1) : SHOW OLINPUTSBISRVCFG:SRVTYPE="N1N2TRANSPDUSETUP"
-----------------Namf_Communication_0----------------
业务类型                           SBI口入向业务每秒每实例最大通过量    过负荷控制业务权重
PDU建立请求类型的N1N2转发           100                                50
记录数：1
执行成功耗时: 0.091 秒
` 
### 入向业务总容量配置 
### 入向业务总容量配置 
背景知识 
本功能用于配置N2接口或SBI（Service Based Interface，基于服务的接口）入向所有业务消息的最大通过量。 
如果统计出的数值没有超过本功能配置的最大值，此时表示不对N2接口或SBI（Service Based Interface，基于服务的接口）的入向所有业务消息的最大通过量进行控制。 
在统计周期内，统计SBI或N2接口入向消息的总数， SBI入向消息总数=SBI各种消息类型的数量×权重。 
比如统计得到的SBI入向消息总数是2000个，将此统计得到的数据和本功能配置的数据进行比较，如果本功能配置的SBI入向消息总数大于2000， 则SBI入向消息总数都不受控（AMF不会对其进行丢弃处理），本功能配置的SBI入向消息总数小于2000， 则超过2000的SBI入向消息会受控（AMF会对其进行丢弃处理） 。 
N2接口或SBI（Service Based Interface，基于服务的接口）入向所有业务消息的最大通过量的优先级高于单项业务消息的最大通过量。 
功能说明 
本功能用于配置N2接口或SBI（Service Based Interface，基于服务的接口）入向所有业务消息的最大通过量。 
子主题： 
#### 修改入向业务总量配置(SET OLTOTALNUMCFG) 
#### 修改入向业务总量配置(SET OLTOTALNUMCFG) 
功能说明 
该命令用于设置AMF启用业务通过量负荷控制功能时，N2接口和SBI接口入向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
该命令在AMF启用业务通过量负荷控制功能时，配置结果才会生效。 
启用业务通过量负荷控制功能，即通过[SET OVERLOADCFG]命令（Namf_MP模式下）设置“启用业务通过量负荷控制(srvSwitch)”为“开启(SRVSWITCHON)”。
通过本命令，AMF支持对N2接口和SBI接口入向的各种业务类型的消息个数进行限制。AMF同时支持对N2接口和SBI接口入向所有的业务类型的消息个数的总和进行控制（即各种业务类型的消息个数总和不能超过系统的配置值）。 
N2接口和SBI接口入向所有业务类型的消息个数总和是通过[SET OLTOTALNUMCFG]命令（Namf_Communication模式下）配置的参数“每秒每实例N2口入向控制总量(olInputN2TotalNum)”和"每秒每实例SBI口入向控制总量(每秒每实例SBI口入向控制总量)"配置的。
如果N2接口或SBI接口入向的某种业务类型的消息个数没有超过本命令设置的数值，但是如果此时N2接口或SBI接口入向所有业务类型的消息个数总和超过[SET OLTOTALNUMCFG]命令配置的总和，则AMF此时仍然会对此种业务类型的消息进行限制。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
olInputN2TotalNum|每秒每实例N2口入向控制总量|参数可选性: 任选参数类型: 数字参数范围: 10-4294967295默认值: 4294967295|该参数用于设置AMF的N2接口所有的入向业务消息每秒每实例最大通过量。本参数设置为4294967295时，表示AMF不会对N2接口所有的入向业务消息每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olInputSbiTotalNum|每秒每实例SBI口入向控制总量|参数可选性: 任选参数类型: 数字参数范围: 10-4294967295默认值: 4294967295|该参数用于设置AMF的SBI所有的入向业务消息每秒每实例最大通过量。本参数设置为4294967295时，表示AMF不会对SBI接口所有的入向业务消息每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
修改消息通过总量的配置值。
SET OLTOTALNUMCFG:OLINPUTN2TOTALNUM=1000,OLINPUTSBITOTALNUM=1000
` 
#### 查询入向业务总量配置(SHOW OLTOTALNUMCFG) 
#### 查询入向业务总量配置(SHOW OLTOTALNUMCFG) 
功能说明 
该命令用于查询AMF在启用业务通过量负荷控制功能时，N2接口和SBI接口入向业务消息每秒每实例（SC）的最大通过总量。  
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
olInputN2TotalNum|每秒每实例N2口入向控制总量|参数可选性: 任选参数类型: 数字参数范围: 10-4294967295默认值: 4294967295|该参数用于设置AMF的N2接口所有的入向业务消息每秒每实例最大通过量。本参数设置为4294967295时，表示AMF不会对N2接口所有的入向业务消息每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
olInputSbiTotalNum|每秒每实例SBI口入向控制总量|参数可选性: 任选参数类型: 数字参数范围: 10-4294967295默认值: 4294967295|该参数用于设置AMF的SBI所有的入向业务消息每秒每实例最大通过量。本参数设置为4294967295时，表示AMF不会对SBI接口所有的入向业务消息每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
查询消息通过总量的配置值。
SHOW OLTOTALNUMCFG
(No.1) : SHOW OLTOTALNUMCFG:
-----------------Namf_Communication_0----------------
每秒每实例N2口入向控制总量   每秒每实例SBI口入向控制总量
1000                        1000
记录数：1
执行成功耗时: 0.134 秒
` 
## 出向业务容量配置 
## 出向业务容量配置 
背景知识 
为有效控制系统负荷及保护对端网元，需要对各接口的出向业务消息进行控制，对于超出配置通过量的消息进行控制。 
功能说明 
本功能用于配置N2接口及SBI（Service Based Interface，基于服务的接口）出向各种业务消息的最大通过量。 
子主题： 
### N2出向业务容量配置 
### N2出向业务容量配置 
背景知识 
AMF可以根据每实例（SC）每秒最大通过的消息个数，对N2接口出向的多种业务消息进行控制。 
功能说明 
本功能用于设置和查询N2接口出向消息过负荷控制参数配置。 
子主题： 
#### 新增N2出向业务配置(ADD OLOUTPUTN2SRVCFG) 
#### 新增N2出向业务配置(ADD OLOUTPUTN2SRVCFG) 
功能说明 
该命令用于新增AMF启用业务通过量负荷控制功能时，N2接口出向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
该命令在AMF启用业务通过量负荷控制功能时，配置结果才会生效。 
启用业务通过量负荷控制功能，即通过[SET OVERLOADCFG]命令（Namf_MP模式下）设置“启用业务通过量负荷控制(srvSwitch)”为“开启(SRVSWITCHON)”。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-0|该参数用于设置AMF的N2接口的出向业务类型，包括寻呼。
olMaxNum|N2口出向业务每秒每实例最大通过量|参数可选性: 必选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的N2接口出向业务每秒每实例最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的N2接口出向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-0|该参数用于设置AMF的N2接口的出向业务类型，包括寻呼。
olMaxNum|N2口出向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的N2接口出向业务每秒每实例最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的N2接口出向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
新增寻呼消息最大通过量配置。
ADD OLOUTPUTN2SRVCFG:SRVTYPE="PAGING",OLMAXNUM=100
` 
#### 修改N2出向业务配置(SET OLOUTPUTN2SRVCFG) 
#### 修改N2出向业务配置(SET OLOUTPUTN2SRVCFG) 
功能说明 
该命令用于修改AMF启用业务通过量负荷控制功能时，N2接口出向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-0|该参数用于设置AMF的N2接口的出向业务类型，包括寻呼。
olMaxNum|N2口出向业务每秒每实例最大通过量|参数可选性: 必选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的N2接口出向业务每秒每实例最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的N2接口出向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-0|该参数用于设置AMF的N2接口的出向业务类型，包括寻呼。
olMaxNum|N2口出向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的N2接口出向业务每秒每实例最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的N2接口出向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
修改寻呼消息最大通过量配置。
SET OLOUTPUTN2SRVCFG:SRVTYPE="PAGING",OLMAXNUM=100
` 
#### 删除N2出向业务配置(DEL OLOUTPUTN2SRVCFG) 
#### 删除N2出向业务配置(DEL OLOUTPUTN2SRVCFG) 
功能说明 
该命令用于删除AMF启用业务通过量负荷控制功能时，N2接口出向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-0|该参数用于设置AMF的N2接口的出向业务类型，包括寻呼。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-0|该参数用于设置AMF的N2接口的出向业务类型，包括寻呼。
olMaxNum|N2口出向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的N2接口出向业务每秒每实例最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的N2接口出向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
删除寻呼消息最大通过量配置。
DEL OLOUTPUTN2SRVCFG:SRVTYPE="PAGING"
` 
#### 查询N2出向业务配置(SHOW OLOUTPUTN2SRVCFG) 
#### 查询N2出向业务配置(SHOW OLOUTPUTN2SRVCFG) 
功能说明 
该命令用于查询AMF启用业务通过量负荷控制功能时，N2接口出向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-0|该参数用于设置AMF的N2接口的出向业务类型，包括寻呼。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-0|该参数用于设置AMF的N2接口的出向业务类型，包括寻呼。
olMaxNum|N2口出向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的N2接口出向业务每秒每实例最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的N2接口出向业务每秒每实例最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
查询寻呼消息最大通过量配置。
SHOW OLOUTPUTN2SRVCFG:SRVTYPE="PAGING"
(No.1) : SHOW OLOUTPUTN2SRVCFG:SRVTYPE="PAGING"
-----------------Namf_Communication_0----------------
业务类型      N2口出向业务每秒每实例最大通过量
寻呼            100
记录数：1
执行成功耗时: 0.163 秒
` 
### SBI出向业务容量配置 
### SBI出向业务容量配置 
背景知识 
AMF可以根据每实例（SC）每秒最大通过的消息个数，对SBI（Service Based Interface，基于服务的接口）出向的多种消息（如UE鉴权）进行控制。 
功能说明 
本功能用于设置和查询SBI（Service Based Interface，基于服务的接口）出向消息过负荷控制参数配置。 
子主题： 
#### 新增SBI出向业务配置(ADD OLOUTPUTSBISRVCFG) 
#### 新增SBI出向业务配置(ADD OLOUTPUTSBISRVCFG) 
功能说明 
该命令用于新增AMF启用业务通过量负荷控制功能时，SBI（Service Based Interface，基于服务的接口）出向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
该命令在AMF启用业务通过量负荷控制功能时，配置结果才会生效。 
启用业务通过量负荷控制功能，即通过[SET OVERLOADCFG]命令（Namf_MP模式下）设置“启用业务通过量负荷控制(srvSwitch)”为“开启(SRVSWITCHON)”。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置AMF的SBI的出向业务类型，包括SM上下文建立等。
olMaxNum|SBI口出向业务每秒每实例最大通过量|参数可选性: 必选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI出向业务每秒每实例（SC）最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的SBI出向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置AMF的SBI的出向业务类型，包括SM上下文建立等。
olMaxNum|SBI口出向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI出向业务每秒每实例（SC）最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的SBI出向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
新增sm上下文建立请求消息最大通过量配置。
ADD OLOUTPUTSBISRVCFG:SRVTYPE="SMCONTEXTCRT",OLMAXNUM=100
` 
#### 修改SBI出向业务配置(SET OLOUTPUTSBISRVCFG) 
#### 修改SBI出向业务配置(SET OLOUTPUTSBISRVCFG) 
功能说明 
该命令用于修改AMF启用业务通过量负荷控制功能时，SBI（Service Based Interface，基于服务的接口）出向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置AMF的SBI的出向业务类型，包括SM上下文建立等。
olMaxNum|SBI口出向业务每秒每实例最大通过量|参数可选性: 必选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI出向业务每秒每实例（SC）最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的SBI出向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置AMF的SBI的出向业务类型，包括SM上下文建立等。
olMaxNum|SBI口出向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI出向业务每秒每实例（SC）最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的SBI出向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
修改sm上下文建立请求消息最大通过量配置。
SET OLOUTPUTSBISRVCFG:SRVTYPE="SMCONTEXTCRT",OLMAXNUM=100
` 
#### 删除SBI出向业务配置(DEL OLOUTPUTSBISRVCFG) 
#### 删除SBI出向业务配置(DEL OLOUTPUTSBISRVCFG) 
功能说明 
该命令用于删除AMF启用业务通过量负荷控制功能时，SBI（Service Based Interface，基于服务的接口）出向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置AMF的SBI的出向业务类型，包括SM上下文建立等。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置AMF的SBI的出向业务类型，包括SM上下文建立等。
olMaxNum|SBI口出向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI出向业务每秒每实例（SC）最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的SBI出向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
删除sm上下文建立请求消息最大通过量配置。
DEL OLOUTPUTSBISRVCFG:SRVTYPE="SMCONTEXTCRT"
` 
#### 查询SBI出向业务配置(SHOW OLOUTPUTSBISRVCFG) 
#### 查询SBI出向业务配置(SHOW OLOUTPUTSBISRVCFG) 
功能说明 
该命令用于查询AMF启用业务通过量负荷控制功能时，SBI（Service Based Interface，基于服务的接口）出向业务消息每秒每实例（SC）的最大通过量。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置AMF的SBI的出向业务类型，包括SM上下文建立等。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5|该参数用于设置AMF的SBI的出向业务类型，包括SM上下文建立等。
olMaxNum|SBI口出向业务每秒每实例最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 65535|该参数用于设置AMF当前类型的SBI出向业务每秒每实例（SC）最大通过量，即在AMF启用业务通过量负荷控制功能时，每秒允许发送的指定消息最大个数。本参数设置为65535，表示AMF不会对当前业务类型的SBI出向业务每秒每实例（SC）最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
查询SM上下文建立请求消息最大通过量配置。
SHOW OLOUTPUTSBISRVCFG:SRVTYPE="SMCONTEXTCRT"
(No.1) : SHOW OLOUTPUTSBISRVCFG:SRVTYPE="SMCONTEXTCRT"
-----------------Namf_Communication_0----------------
业务类型            SBI口出向业务每秒每实例最大通过量
SM上下文建立        100
记录数：1
执行成功耗时: 0.078 秒
` 
# NG Setup入向控制业务配置 
# NG Setup入向控制业务配置 
背景知识 
为了AMF能够稳定正常的处理业务消息，需要控制AMF的处理负荷。对于RAN发起的NG Setup消息，同样需要进行控制。 
功能说明 
本功能用于配置AMF在接收NG Setup Request消息后，每秒最大处理请求数。 
子主题： 
## 修改NG Setup控制配置参数命令(SET NGSETUPCTLCFG) 
## 修改NG Setup控制配置参数命令(SET NGSETUPCTLCFG) 
功能说明 
该命令用于配置，AMF允许RAN发起的NG Setup入向业务消息的每秒最大通过量。  
注意事项 
本命令执行后，结果立即生效。  
RAN发起的NG Setup入向业务消息与N2接口入向的其他消息处理机制不相同。RAN发起的NG Setup入向业务消息的每秒最大通过量，不受到以下两个条件的限制。  
 
AMF是否启用业务通过量负荷控制功能。
启用业务通过量负荷控制功能，即通过SET OVERLOADCFG命令（Namf_MP模式下）设置“启用业务通过量负荷控制(srvSwitch)”为“开启(SRVSWITCHON)”。 
 
AMF是否对N2接口入向所有的业务类型的消息个数进行控制（即N2接口入向各种业务类型的消息个数总和不能超过总量的配置值）。
N2接口入向所有业务类型的消息个数总和是通过SET OLTOTALNUMCFG命令（Namf_Communication模式下）配置的参数“每秒每实例N2口入向控制总量(olInputN2TotalNum)”配置的。
如果RAN发起的NG Setup入向业务消息个数没有超过本命令设置的数值，但是如果此时N2接口入向所有业务类型的消息个数总和超过SET OLTOTALNUMCFG命令配置的总和，则AMF此时仍然不会对NG Setup入向业务消息进行限制。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
olMaxNum|NgSetup入向业务每秒最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 100|该参数用于设置AMF允许的当前NG Setup入向业务每秒最大通过量。本参数设置为65535时，表示AMF不会对RAN发起的NG Setup入向业务消息的每秒最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
修改NG Setup消息最大通过量100。
SET NGSETUPCTLCFG:OLMAXNUM=100
` 
## 查询NG Setup控制配置参数命令(SHOW NGSETUPCTLCFG) 
## 查询NG Setup控制配置参数命令(SHOW NGSETUPCTLCFG) 
功能说明 
该命令用于查询NG Setup入向业务消息的每秒最大通过量。  
注意事项 
本命令执行后，结果立即生效。  
输出参数说明 
标识|名称|类型|说明
---|---|---|---
olMaxNum|NgSetup入向业务每秒最大通过量|参数可选性: 任选参数类型: 数字参数范围: 10-65535默认值: 100|该参数用于设置AMF当前NG Setup入向业务每秒最大通过量。本参数设置为65535时，表示AMF不会对RAN发起的NG Setup入向业务消息的每秒最大通过量进行限制。此处设置的个数针对单个SC（Service Component，服务组件）。
命令举例 
`
查询NG Setup消息最大通过量100。
SHOW NGSETUPCTLCFG:OLMAXNUM=100
` 
# 抗信令冲击配置 
# 抗信令冲击配置 
背景知识 
性能测试要求使用10倍/20倍的话务进行测试。原因是采用大区制后，需要考虑其它大区完全宕机、全部容灾到另外一个大区的场景。 
考虑40%的Connect态用户在5~10秒内全部重试，产生的冲击流量的场景。由于需要同时考虑竞争力的问题，要求配置的虚机数量要少，就必须考虑在没有更多冗余的情况下能满足大量用户的冲击。 
功能说明 
本功能用于设置及查询每个线程的最大缓存消息数量（初始注册消息）以及每秒钟处理缓存消息数量。 
子主题： 
## 设置缓存消息配置(SET BUFMSGCFG) 
## 设置缓存消息配置(SET BUFMSGCFG) 
功能说明 
该命令用于设置AMF最大消息缓存数量以及每秒释放并处理缓存消息数。（每线程） 
注意事项 
最大缓存消息数量为0，表示不开启缓存功能。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
maxBufMsgNum|最大缓存消息数量（每线程）|参数可选性: 任选参数类型: 数字参数范围: 0-5000|该参数用于设置AMF每个线程可以缓存消息的最大数量。默认记录为0，即不开启缓存。 当开启本功能时，可根据processedMsgNum每秒处理缓存消息配合设置，确保缓存的报文在6s内处理完毕。因为终端一般6s会重发。
processedMsgNum|每秒处理缓存消息数量（每线程）|参数可选性: 任选参数类型: 数字参数范围: 0-500|该参数用于设置AMF每个线程每秒释放并处理缓存消息数。根据实际CPU处理能力设置。该数值设置过大时，则通过的Registration量越大，系统CPU符合越重。建议设置范围尽量不超过350，否则系统CPU会超过80%。
命令举例 
`
设置AMF当前最大缓存消息的数量为2800，每秒处理速率200caps/s。
SET BUFMSGCFG:MAXBUFMSGNUM=2800,PROCESSEDMSGNUM=200
` 
## 查询缓存消息配置(SHOW BUFMSGCFG) 
## 查询缓存消息配置(SHOW BUFMSGCFG) 
功能说明 
该命令用于显示AMF当前最大消息缓存数量以及每秒释放并处理缓存消息数。（每线程） 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
maxBufMsgNum|最大缓存消息数量（每线程）|参数可选性: 任选参数类型: 数字参数范围: 0-5000|该参数用于显示AMF每个线程可以缓存消息的最大数量。结合processedMsgNum每秒处理缓存消息数设置，尽量不超过其6倍（超过6s终端会重发）。
processedMsgNum|每秒处理缓存消息数量（每线程）|参数可选性: 任选参数类型: 数字参数范围: 0-500|该参数用于显示AMF每个线程每秒释放并处理缓存消息数。建议设置范围尽量不超过350，否则系统CPU会超过80%。
命令举例 
`
查询缓存消息配置
ZTE:>SHOW BUFMSGCFG:
(No.1) : SHOW BUFMSGCFG:
-----------------Namf_Communication_0_A----------------
最大缓存消息数量（每线程） 每秒处理缓存消息数量（每线程）
        0                        350
记录数：1
执行成功耗时: 0.48 秒
` 
# AMF异常信令管控配置 
# AMF异常信令管控配置 
背景知识 
信令风暴是由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。异常信令管控是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
功能说明 
当智能终端网络信令短时频繁成功或终端网络信令连续失败，造成AMF收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，AMF需要进行异常信令管控时，使用该命令。AMF异常信令管控配置成功后，AMF可以根据各配置值，采取一定的措施，减少网络侧要处理的信令，化解信令风暴，避免网络拥塞，确保网络设备安全运行，有力保障不在信令黑名单中的用户使用数据业务和其他业务的成功率。 
子主题： 
## AMF异常信令管控策略配置 
## AMF异常信令管控策略配置 
背景知识 
信令风暴是由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。异常信令管控是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
功能说明 
本功能用于配置是否开启AMF的异常信令管控功能。 
子主题： 
### 修改AMF异常信令管控策略配置(SET ABNORMALSIGMCPOLICY) 
### 修改AMF异常信令管控策略配置(SET ABNORMALSIGMCPOLICY) 
功能说明 
该命令用于设置AMF是否支持异常信令管控功能。当设置为支持时，AMF会对用户发起的初始注册请求消息进行统计。 
 
 当在配置的统计周期内，用户发起的初始注册请求数达到配置的门限值时，则把该用户加入异常信令管控黑名单中，并对用户回复注册拒绝消息，其中注册拒绝消息中携带的原因值可配置。 
 
 当在配置的统计周期内，用户发起的初始注册请求数没有达到配置的门限值时，则重新统计。 
 
注意事项 
在配置该命令之前，需要先开启license “AMF支持异常信令管控”。 
在配置该命令之前，需要执行[SET ABNORMALSIGMCCONFIG]，配置该功能需要使用的相关参数。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supportsigctrl|AMF是否支持异常信令管控|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否开启AMF异常信令管控功能。
命令举例 
`
设置AMF支持异常信令管控。 
SET ABNORMALSIGMCPOLICY:SUPPORTSIGCTRL="YES"
` 
### 查询AMF异常信令管控策略配置(SHOW ABNORMALSIGMCPOLICY) 
### 查询AMF异常信令管控策略配置(SHOW ABNORMALSIGMCPOLICY) 
功能说明 
该命令用于查询AMF是否支持异常信令管控。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supportsigctrl|AMF是否支持异常信令管控|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否开启AMF异常信令管控功能。
命令举例 
`
查询AMF是否支持异常信令管控。 
SHOW ABNORMALSIGMCPOLICY:
(No.1) : SHOW ABNORMALSIGMCPOLICY:
-----------------Namf_Communication_0_A----------------
AMF是否支持异常信令管控
支持
` 
## AMF异常信令管控配置 
## AMF异常信令管控配置 
背景知识 
信令风暴是由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。异常信令管控是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
功能说明 
本功能用于配置AMF异常信令管控用到的参数。 
子主题： 
### 修改AMF异常信令管控配置(SET ABNORMALSIGMCCONFIG) 
### 修改AMF异常信令管控配置(SET ABNORMALSIGMCCONFIG) 
功能说明 
该命令用于设置AMF异常信令管控功能需要使用的相关参数。 
注意事项 
在配置该命令之前，需要先开启license “AMF支持异常信令管控”。 
在配置该命令之后，需要执行[SET ABNORMALSIGMCPOLICY]，开启AMF支持异常信令管控功能。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regstatperiod|注册请求信令统计周期|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 720|该参数用于设置初始注册请求的统计周期时长。当统计周期内的初始注册请求数超过注册请求最大信令数时，AMF会把用户移入黑名单中，否则，AMF会重新统计。
regmaxsignum|注册请求最大信令数|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 30|该参数用于设置初始注册请求的统计周期内的最大信令数，当统计周期内的初始注册请求数超过该值后，AMF会把该用户引入黑名单中，并发送注册拒绝消息给用户，如果用户再次发起初始注册流程，AMF将发送网络侧去注册给用户，如果用户还会发起初始注册流程，AMF将直接丢弃注册请求消息。
regrejectcause|注册拒绝原因值|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 7|该参数用于设置AMF发送给UE的注册拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
regblacklistduration|注册请求黑名单定时器时长|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1200|该参数用于设置用户进入异常信令管控的黑名单的最大时长，超过这个时长后，用户会重新进入白名单。
srstatperiod|业务请求信令统计周期|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 720|该参数用于设置业务请求的统计周期时长。当统计周期内的业务请求数超过业务请求最大信令数时，AMF会把用户移入黑名单中，否则，AMF会重新统计。
srmaxsignum|业务请求最大信令数|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 60|该参数用于设置业务请求的统计周期内的最大信令数，当统计周期内的业务请求数超过该值后，AMF会把该用户引入黑名单中，并发送业务请求拒绝消息给用户，如果用户再次发起业务流程，AMF将发送网络侧去注册给用户。
srrejectcause|业务请求拒绝原因值|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 7|该参数用于设置AMF发送给UE的业务请求拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
srblacklistduration|业务请求黑名单定时器时长|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1200|该参数用于设置业务请求过程用户进入异常信令管控的黑名单的最大时长，超过这个时长后，用户会重新进入白名单。
pdueststatperiod|PDU会话建立请求信令统计周期|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 720|该参数用于设置PDU会话建立请求的统计周期时长。当统计周期内的PDU会话建立请求数超过PDU会话建立请求最大信令数时，AMF会把用户移入黑名单中，否则，AMF会重新统计。
pduestmaxsignum|PDU会话建立请求最大信令数|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 32|该参数用于设置PDU会话建立请求的统计周期内的最大信令数，当统计周期内的PDU会话建立请求数超过该值后，AMF会把该用户引入黑名单中，并发送PDU会话建立拒绝消息给用户，如果用户再次发起PDU会话建立流程，AMF将以fake DNN（能建立但是无法上网）让终端建立成功，如果用户还会发起PDU会话建立流程，AMF将发送网络侧去注册给用户。
pduestrejectcause|PDU会话建立请求拒绝原因值|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 7|该参数用于设置AMF发送给UE的PDU会话建立拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
pduestblackduration|PDU会话建立请求黑名单定时器时长|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1200|该参数用于设置PDU会话建立过程用户进入异常信令管控的黑名单的最大时长，超过这个时长后，用户会重新进入白名单。
fakednn|FAKE DNN名称|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于配置本局fake DNN，该DNN不在UDM签约，在AMF本地配置，并允许PDU建立成功。当不需要使用FAKE DNN名称时，需要将该值设置为“null”
命令举例 
`
设置初始注册请求消息的统计周期为60秒，设置统计周期内的最大初始注册请求数为10次，设置注册消息携带的拒绝原因值为7，设置初始注册的黑名单定时器时长为120秒。 
SET ABNORMALSIGMCCONFIG:REGSTATPERIOD=60,REGMAXSIGNUM=10,REGREJECTCAUSE=7,REGBLACKLISTDURATION=120
` 
### 查询AMF异常信令管控配置(SHOW ABNORMALSIGMCCONFIG) 
### 查询AMF异常信令管控配置(SHOW ABNORMALSIGMCCONFIG) 
功能说明 
该命令用于查询AMF异常信令管控功能需要使用的相关参数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
regstatperiod|注册请求信令统计周期|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 720|该参数用于设置初始注册请求的统计周期时长。当统计周期内的初始注册请求数超过注册请求最大信令数时，AMF会把用户移入黑名单中，否则，AMF会重新统计。
regmaxsignum|注册请求最大信令数|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 30|该参数用于设置初始注册请求的统计周期内的最大信令数，当统计周期内的初始注册请求数超过该值后，AMF会把该用户引入黑名单中，并发送注册拒绝消息给用户，如果用户再次发起初始注册流程，AMF将发送网络侧去注册给用户，如果用户还会发起初始注册流程，AMF将直接丢弃注册请求消息。
regrejectcause|注册拒绝原因值|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 7|该参数用于设置AMF发送给UE的注册拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
regblacklistduration|注册请求黑名单定时器时长|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1200|该参数用于设置用户进入异常信令管控的黑名单的最大时长，超过这个时长后，用户会重新进入白名单。
srstatperiod|业务请求信令统计周期|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 720|该参数用于设置业务请求的统计周期时长。当统计周期内的业务请求数超过业务请求最大信令数时，AMF会把用户移入黑名单中，否则，AMF会重新统计。
srmaxsignum|业务请求最大信令数|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 60|该参数用于设置业务请求的统计周期内的最大信令数，当统计周期内的业务请求数超过该值后，AMF会把该用户引入黑名单中，并发送业务请求拒绝消息给用户，如果用户再次发起业务流程，AMF将发送网络侧去注册给用户。
srrejectcause|业务请求拒绝原因值|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 7|该参数用于设置AMF发送给UE的业务请求拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
srblacklistduration|业务请求黑名单定时器时长|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1200|该参数用于设置业务请求过程用户进入异常信令管控的黑名单的最大时长，超过这个时长后，用户会重新进入白名单。
pdueststatperiod|PDU会话建立请求信令统计周期|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 720|该参数用于设置PDU会话建立请求的统计周期时长。当统计周期内的PDU会话建立请求数超过PDU会话建立请求最大信令数时，AMF会把用户移入黑名单中，否则，AMF会重新统计。
pduestmaxsignum|PDU会话建立请求最大信令数|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 32|该参数用于设置PDU会话建立请求的统计周期内的最大信令数，当统计周期内的PDU会话建立请求数超过该值后，AMF会把该用户引入黑名单中，并发送PDU会话建立拒绝消息给用户，如果用户再次发起PDU会话建立流程，AMF将以fake DNN（能建立但是无法上网）让终端建立成功，如果用户还会发起PDU会话建立流程，AMF将发送网络侧去注册给用户。
pduestrejectcause|PDU会话建立请求拒绝原因值|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 7|该参数用于设置AMF发送给UE的PDU会话建立拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
pduestblackduration|PDU会话建立请求黑名单定时器时长|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1200|该参数用于设置PDU会话建立过程用户进入异常信令管控的黑名单的最大时长，超过这个时长后，用户会重新进入白名单。
fakednn|FAKE DNN名称|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于配置本局fake DNN，该DNN不在UDM签约，在AMF本地配置，并允许PDU建立成功。当不需要使用FAKE DNN名称时，需要将该值设置为“null”
命令举例 
`
查询异常信令管控配置。
SHOW ABNORMALSIGMCCONFIG:
注册请求信令统计周期   注册请求最大信令数   注册拒绝原因值   注册请求黑名单定时器时长   业务请求信令统计周期   业务请求最大信令数   业务请求拒绝原因值   业务请求黑名单定时器时长   PDU会话建立请求信令统计周期   PDU会话建立请求最大信令数   PDU会话建立请求拒绝原因值   PDU会话建立请求黑名单定时器时长   FAKE DNN名称
720                    15                   7                1200                       720                    30                   7                    1200                       720                           10                          31                          1200       
` 
## AMF异常信令管控优化配置 
## AMF异常信令管控优化配置 
背景知识 
信令风暴是由于网络收到的终端信令请求超过了网络各项信令资源的处理能力，引发网络拥塞甚至雪崩效应，导致网络不可用。异常信令管控是网络侧采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
功能说明 
本功能用于配置AMF异常信令管控优化的参数。 
子主题： 
### 设置AMF异常信令管控优化配置(SET ABNORMALSIGMCOPT) 
### 设置AMF异常信令管控优化配置(SET ABNORMALSIGMCOPT) 
功能说明 
该命令用于设置AMF异常信令管控优化配置功能，包括业务请求异常信令管控优化开关、业务请求拒绝原因值、PDU会话异常信令管控优化开关、因PDU会话管控导致的注册拒绝原因值。 
注意事项 
AMF异常信令管控优化开启，需要打开AMF异常信令管控功能方可生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
bsupsrsigmcopt|支持业务请求异常信令管控优化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|该参数用于设置是否开启支持业务请求异常信令管控优化功能。
bsrrejcause|业务请求拒绝原因值|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 10|该参数用于设置当开启支持异常信令管控优化后AMF发送给UE的业务请求拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
bsuppduestsigmcopt|支持PDU会话建立异常信令管控优化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|该参数用于设置是否开启支持PDU会话建立异常信令管控优化功能。
bregrejcause|因PDU会话异常信令管控导致的注册拒绝原因|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 111|该参数用于设置当开启支持异常信令管控优化后，AMF因PDU会话异常管控发送给UE的注册拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
命令举例 
`
设置支持业务请求异常信令管控优化功能，业务请求拒绝原因值为10，支持PDU会话建立异常信令管控优化，因PDU会话异常信令管控导致的注册拒绝原因为111。 
SET ABNORMALSIGMCOPT:BSUPSRSIGMCOPT="SUPPORT",BSRREJCAUSE=10,BSUPPDUESTSIGMCOPT="SUPPORT",BREGREJCAUSE=111
` 
### 查询AMF异常信令管控优化配置(SHOW ABNORMALSIGMCOPT) 
### 查询AMF异常信令管控优化配置(SHOW ABNORMALSIGMCOPT) 
功能说明 
该命令用于查询AMF异常信令管控优化配置信息。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
bsupsrsigmcopt|支持业务请求异常信令管控优化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|该参数用于设置是否开启支持业务请求异常信令管控优化功能。
bsrrejcause|业务请求拒绝原因值|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 10|该参数用于设置当开启支持异常信令管控优化后AMF发送给UE的业务请求拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
bsuppduestsigmcopt|支持PDU会话建立异常信令管控优化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|该参数用于设置是否开启支持PDU会话建立异常信令管控优化功能。
bregrejcause|因PDU会话异常信令管控导致的注册拒绝原因|参数可选性: 任选参数类型: 数字参数范围: 1-255默认值: 111|该参数用于设置当开启支持异常信令管控优化后，AMF因PDU会话异常管控发送给UE的注册拒绝消息中携带的原因值，可选的原因值如下：3: Illegal UE5: PEI not accepted6: Illegal ME7: 5GS services not allowed9: UE identity cannot be derived by the network10: Implicitly de-registered11: PLMN not allowed12: Tracking area not allowed13: Roaming not allowed in this tracking area15: No suitable cells in tracking area20: MAC failure21: Synch failure22: Congestion27: N1 mode not allowed28: Restricted service area31: Redirection to EPC required62: No network slices available71: ngKSI already in use72: Non-3GPP access to 5GCN not allowed73: Serving network not authorized74: Temporarily not authorized for this SNPN76: Not authorized for this CAG or authorized for CAG cells only95: Semantically incorrect message96: Invalid mandatory information97: Message type non-existent or not implemented98: Message type not compatible with the protocol state99: Information element non-existent or not implemented100: Conditional IE error101: Message not compatible with the protocol state111: Protocol error, unspecified
命令举例 
`
查询AMF异常信令管控优化配置。
SHOW ABNORMALSIGMCOPT
支持业务请求异常信令管控优化   业务请求拒绝原因值   支持PDU会话建立异常信令管控优化   因PDU会话异常信令管控导致的注册拒绝原因
支持                          10                  支持                            111  
` 
# SBI拥塞控制配置 
# SBI拥塞控制配置 
背景知识 
在AMF周边的SBI接口网元（AUSF/UDM等）接近过载或过载，收到AMF的服务化接口请求消息时，回送429或503状态码并携带Retry-After头部。AMF在收到429或503状态码失败消息后，当所有对应网元拥塞时，AMF通过拥塞控制，控制终端的接入速率，使用户平稳接入，使网络恢复到正常状态。具体参见29500协议“6.4 Overload Control”章节。 
功能说明 
本功能用于配置服务化接口拥塞的控制策略和back-off timer值，AMF通过拥塞控制，控制终端的接入速率，降低对服务化接口网元的冲击，保障网络稳定运行。 
子主题： 
## AUSF拥塞控制配置 
## AUSF拥塞控制配置 
背景知识 
当AUSF接近过载或过载，收到AMF的服务化接口请求消息时，回送429或503状态码并携带Retry-After头部，AMF在收到429或503状态码失败消息后，当到所有对应AUSF网元拥塞时，AMF通过拥塞控制，控制终端的接入速率，使用户平稳接入，使AUSF平稳恢复到正常状态。 
功能说明 
本功能用于配置AUSF网元全拥塞的控制策略和back-off timer值，AMF通过拥塞控制，控制终端的接入速率，降低对AUSF网元的冲击，保障网络稳定运行。 
子主题： 
### 修改AUSF拥塞控制配置(SET AUSFCONGESTIONCFG) 
### 修改AUSF拥塞控制配置(SET AUSFCONGESTIONCFG) 
功能说明 
该命令用于设置AUSF拥塞时的拥塞控制开关，是否携带Backoff timer，最小back-off timer值和最大back-off timer值。当AUSF全部拥塞，需要进行AUSF拥塞控制时，执行此命令。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supausfcongctl|支持AUSF全拥塞控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AUSF全部拥塞时是否进行拥塞控制。修改影响：修改该参数可以改变AUSF全部拥塞时的拥塞控制策略。数据来源：本端规划。默认值：0。配置原则：开启AUSF拥塞控制，需通过SHOW AUSFCAUSEMAPPINGCFG命令查询在NAS原因值映射配置中，已配置AUSF全拥塞流控的映射原因值。
carrybackofftime|携带Backoff timer|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置AUSF全拥塞时是否携带back-off timer值。修改影响：开启之后，表明AUSF全拥塞时携带back-off timer值，终端收到后根据back-off timer值延时接入网络；否则，表明AUSF全拥塞时不携带back-off timer值。数据来源：本端规划。取值范围：整数类型，取值范围是0~1。默认值：0。配置原则：无。
minbackofftime|Backoff timer最小值(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-11160默认值: 0|参数作用：该参数用于设置back-off timer的最小值，用于计算发给终端的back-off timer时长。当AMF执行拥塞控制而拒绝业务时，拒绝消息中携带back-off timer，此参数取值在Backoff timer最小值与Backoff Timer最大值的范围内随机选择。修改影响：修改该参数可以改变计算发给终端的back-off timer时长。数据来源：本端规划。默认值：0秒。配置原则：无。
maxbackofftime|Backoff timer最大值(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-11160默认值: 0|参数作用：该参数用于设置back-off timer的最大值，用于计算发给终端的back-off timer时长。当AMF执行拥塞控制而拒绝业务时，拒绝消息中携带back-off timer，此参数取值在Backoff timer最小值与Backoff Timer最大值的范围内随机选择。修改影响：修改该参数可以改变计算发给终端的back-off timer时长。数据来源：本端规划。默认值：0秒。配置原则：该参数的取值必须大于等于“minbackofftime（Back-off timer最小值(秒)）”的取值。
命令举例 
`
设置AUSF拥塞控制配置，支持AUSF全拥塞控制，携带back-off timer，最小back-off timer为100秒，最大back-off timer值为1000秒。
SET AUSFCONGESTIONCFG:SUPAUSFCONGCTL="SPRT",CARRYBACKOFFTIME="CARRY",MINBACKOFFTIME=100,MAXBACKOFFTIME=1000
` 
### 查询AUSF拥塞控制配置(SHOW AUSFCONGESTIONCFG) 
### 查询AUSF拥塞控制配置(SHOW AUSFCONGESTIONCFG) 
功能说明 
该命令用于查询AUSF拥塞时的拥塞控制开关，是否携带Backoff timer，最小back-off timer值和最大back-off timer值。  
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supausfcongctl|支持AUSF全拥塞控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置AUSF全部拥塞时是否进行拥塞控制。
carrybackofftime|携带Backoff timer|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|该参数用于设置AUSF全拥塞时是否携带back-off timer值。
minbackofftime|Backoff timer最小值(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-11160默认值: 0|该参数用于设置back-off timer的最小值，用于计算发给终端的back-off timer时长。
maxbackofftime|Backoff timer最大值(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-11160默认值: 0|该参数用于设置back-off timer的最大值，用于计算发给终端的back-off timer时长。
命令举例 
`
查询AUSF拥塞控制配置，是否支持AUSF全拥塞控制，是否携带back-off timer，最小back-off timer值，最大back-off timer值。 
SHOW AUSFCONGESTIONCFG: 
(No.2) : SHOW AUSFCONGESTIONCFG:
-----------------Namf_Communication_0----------------
操作维护       支持AUSF全拥塞控制 携带Backoff timer Back-off timer最小值(秒) Back-off timer最大值(秒) 
----------------------------------------------------------------------------------------------------
修改           支持             携带            100                     1000                    
----------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-07-07 11:30:52 耗时: 0.151 秒
` 
## UDM拥塞控制配置 
## UDM拥塞控制配置 
背景知识 
当UDM接近过载或过载，收到AMF的服务化接口请求消息时，回送429或503状态码并携带Retry-After头部，AMF在收到429或503状态码失败消息后，当到所有对应UDM网元拥塞时，AMF通过拥塞控制，控制终端的接入速率，使用户平稳接入，使UDM平稳恢复到正常状态。 
功能说明 
本功能用于配置UDM网元全拥塞的控制策略和back-off timer值，AMF通过拥塞控制，控制终端的接入速率，降低对UDM网元的冲击，保障网络稳定运行。 
子主题： 
### 修改UDM拥塞控制配置(SET UDMCONGESTIONCFG) 
### 修改UDM拥塞控制配置(SET UDMCONGESTIONCFG) 
功能说明 
该命令用于设置UDM拥塞时的拥塞控制开关，携带Backoff timer，最小back-off timer值和最大back-off timer值。当UDM全部拥塞，需要进行UDM拥塞控制时，执行此命令。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supudmcongctl|支持UDM全拥塞控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置UDM全部拥塞时是否进行拥塞控制。修改影响：修改该参数可以改变UDM全部拥塞时的拥塞控制策略。数据来源：本端规划。默认值：0。配置原则：开启UDM拥塞控制，开启UDM拥塞控制，需通过SHOW UDMCAUSEMAPPINGCFG命令查询在NAS原因值映射配置中，已配置UDM全拥塞流控的映射原因值。
carrybackofftime|携带Backoff timer|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|参数作用：该参数用于设置UDM全拥塞时是否携带back-off timer值。修改影响：开启之后，表明UDM全拥塞时携带back-off time值，终端收到后根据back-off time值延时接入网络；否则，表明UDM全拥塞时不携带back-off timer值。数据来源：本端规划。默认值：0。配置原则：无。
minbackofftime|Backoff timer最小值(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-11160默认值: 0|参数作用：该参数用于设置back-off timer的最小值，用于计算发给终端的back-off timer时长。当AMF执行拥塞控制而拒绝业务时，拒绝消息中携带back-off timer，此参数取值在Backoff timer最小值与Backoff Timer最大值的范围内随机选择。修改影响：修改该参数可以改变计算发给终端的back-off timer时长。数据来源：本端规划。默认值：0秒。配置原则：无。
maxbackofftime|Backoff timer最大值(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-11160默认值: 0|参数作用：该参数用于设置back-off timer的最大值，用于计算发给终端的back-off timer时长。当AMF执行拥塞控制而拒绝业务时，拒绝消息中携带back-off timer，此参数取值在Backoff timer最小值与Backoff Timer最大值的范围内随机选择。修改影响：修改该参数可以改变计算发给终端的back-off timer时长。数据来源：本端规划。默认值：0秒。配置原则：该参数的取值必须大于等于“minbackofftime（back-off timer最小值(秒)）”的取值。
命令举例 
`
设置UDM拥塞控制配置，支持UDM全拥塞控制，携带Backoff timer，最小back-off timer为100秒，最大back-off timer值为1000秒。
SET UDMCONGESTIONCFG:SUPUDMCONGCTL="SPRT",CARRYBACKOFFTIME="CARRY",MINBACKOFFTIME=100,MAXBACKOFFTIME=1000
` 
### 查询UDM拥塞控制配置(SHOW UDMCONGESTIONCFG) 
### 查询UDM拥塞控制配置(SHOW UDMCONGESTIONCFG) 
功能说明 
该命令用于查询UDM拥塞时的拥塞控制开关，携带Backoff timer，最小back-off timer值和最大back-off timer值。  
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supudmcongctl|支持UDM全拥塞控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置UDM全部拥塞时是否进行拥塞控制。
carrybackofftime|携带Backoff timer|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRY|该参数用于设置UDM全拥塞时是否携带back-off timer值。
minbackofftime|Backoff timer最小值(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-11160默认值: 0|该参数用于设置back-off timer的最小值，用于计算发给终端的back-off timer时长。
maxbackofftime|Backoff timer最大值(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-11160默认值: 0|该参数用于设置back-off timer的最大值，用于计算发给终端的back-off timer时长。
命令举例 
`
查询UDM拥塞控制配置，是否支持UDM全拥塞控制，是否携带back-off timer，最小back-off timer值，最大back-off timer值。 
SHOW UDMCONGESTIONCFG: 
(No.1) : SHOW UDMCONGESTIONCFG:
-----------------Namf_Communication_0----------------
操作维护       支持UDM全拥塞控制 携带Backoff timer Backoff timer最小值(秒) Backoff timer最大值(秒) 
---------------------------------------------------------------------------------------------------
修改           支持            携带            100                     1000                    
---------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-07-07 11:30:04 耗时: 0.145 秒
` 
