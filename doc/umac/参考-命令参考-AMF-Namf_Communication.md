# 服务配置 
# 服务配置 
背景知识 
SBA（Service Based Architecture，服务化架构）是3GPP定义的基于服务的架构体系，是全新的电信业务部署架构。SBA明确定义了5GC中需要呈现的服务，以及需要集中管理的数据上下文。 
3GPP标准定义了SBA架构的如下内容。 
 
适当粒度的NF Service（将NF的功能进行服务化，简称NFS），以及关键数据的存储和访问模型。 
 
NF Service之间的交互由SBI（Service Based Interface，基于服务的接口）接口完成。 
 
AMF部署采用SBA架构体系，由4个NFS：
Namf_Communication、Namf_EventExposure、Namf_MT、Namf_Location。 
 
功能说明 
服务配置包括服务基本功能和服务关联HTTP服务端配置。 
子主题： 
## SERVICE基本配置 
## SERVICE基本配置 
背景知识 
AMF提供了Namf_Communication、Namf_EventExposure和Namf_MT等服务，每个服务提供不同的功能，可参见23501协议“7.2.2 AMF Services”章节。 
该参数用于配置AMF的服务类型（NFS），包括namf_communication、namf_eventexposure、namf_mt、namf_location。 
AMF包括四种NFS。 
 
namf_communication，使NF消费者能够通过AMF与UE或RN通信，该服务使SMF能够请求分配EBI，以支持与EPS互通。参见3GPP TS 23.501协议“5.2.2.2"。 
 
namf_eventexposure，允许其他消费者获得与移动相关的事件和统计信息的通知。参见3GPP TS 23.501协议“5.2.2.3"。 
 
namf_mt，使NF消费者能够确保UE可以访问。参见3GPP TS 23.501协议“5.2.2.4"。 
 
namf_location，使NF消费者能够请求目标UE的位置信息。参见3GPP TS 23.501协议“5.2.2.5"。 
 
功能说明 
本功能用于配置AMF支持的NFS（Network Function Service，网络功能服务），以及每个NFS对应的信息，包括作为HTTP服务端时IP地址类型、版本号、优先级、容量。 
只有正确设置这些信息，AMF下的每个NF Service才能为其他NF提供相应的服务。 
子主题： 
### 新增服务配置(ADD SERVICECFG) 
### 新增服务配置(ADD SERVICECFG) 
功能说明 
本命令用于新增AMF支持的NFS（Network Function Service，网络功能服务），及设置该NFS的HTTP服务端时的IP地址类型、版本号、优先级、容量等信息。 
当AMF部署成功后，通过该命令添加AMF当前支持的NFS。添加成功后，AMF将服务信息成功注册或更新到NRF中，可供其他NF使用。 
注意事项 
 
本命令执行后，配置立即生效。 
 
每种服务类型，只支持配置一条记录。 
 
该命令最多只能配置4条记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3|参数作用：该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
version|URI版本号|参数可选性: 必选参数类型: 数字参数范围: 0-255|参数作用：该参数用于设置访问对应服务的URI中使用的NFS的版本号。修改影响：如果本参数发生了变化，会影响AMF向NRF注册时，“nfServices”字段中携带的“apiVersionInUri”字段的值，且会触发向NRF更新。数据来源：本端规划。默认值：无。配置原则：无。
ipAddrType|作为服务端IP地址类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|参数作用：该参数用于设置当AMF的NFS作为HTTP服务端时的IP地址类型，取值及含义如下：IPV4IPV6修改影响：如果本参数发生了变化，会影响AMF向NRF注册时，“nfServices”字段中携带的“callbackUri”字段的值，且会触发向NRF更新。数据来源：本端规划。默认值：IPV4。配置原则：无。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|参数作用：该参数用于配置AMF支持的NFS优先级。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据优先级来选择NFS。修改影响：当优先级为有效时，如果该参数发生了变化，会影响AMF向NRF注册时，“nfServices”字段中携带的“priority”字段的值，且会触发向NRF更新。数据来源：本端规划。默认值： 65535。配置原则：该参数在优先级是否有效为是时生效。
priorityFlg|优先级是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ISVALID|参数作用：该参数用于配置AMF支持的NFS的优先级标记，用于标识NFS是否启用优先级，控制AMF向NRF注册时，“nfServices”字段中是否携带的“priority”字段，取值及含义如下：否：不携带“priority”字段是：携带“priority”字段修改影响：修改此参数，会影响AMF向NRF注册时，“nfServices”字段中是否携带的“priority”字段，且会触发向NRF更新。数据来源：本端规划。默认值：是。配置原则：无。
capacity|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535|参数作用：该参数用于配置AMF支持的NFS容量。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据容量比例来选择NFS。修改影响：当容量值为有效时，如果该参数发生了变化，会影响AMF向NRF注册时，“nfServices”字段中携带的“capacity”字段的值，且会触发向NRF更新。数据来源：本端规划。默认值：无。配置原则：无。
capacityFlg|容量值是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：本参数用于配置AMF支持的NFS的容量标记，标识NFS是否启用容量值，用于控制AMF向NRF注册时，是否携带“capacity”字段，取值及含义如下：否：不携带“capacity”字段是：携带“capacity”字段修改影响：修改此参数，会影响AMF向NRF注册时，“nfServices”字段中是否携带的“capacity”字段，且会触发向NRF更新。数据来源：本端规划。默认值：否。配置原则：该参数生效的前提，是容量值是否有效为是时生效。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|参数作用：该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。
version|URI版本号|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于设置访问对应服务的URI中使用的NFS的版本号。
ipAddrType|作为服务端IP地址类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|参数作用：该参数用于设置当AMF的NFS作为HTTP服务端时的IP地址类型，取值及含义如下：IPV4IPV6
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|参数作用：该参数用于配置AMF支持的NFS优先级。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据优先级来选择NFS。
priorityFlg|优先级是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ISVALID|参数作用：该参数用于配置AMF支持的NFS的优先级标记，用于标识NFS是否启用优先级，控制AMF向NRF注册时，“nfServices”字段中是否携带的“priority”字段，取值及含义如下：否：不携带“priority”字段是：携带“priority”字段
capacity|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535|参数作用：该参数用于配置AMF支持的NFS容量。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据容量比例来选择NFS。
capacityFlg|容量值是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：本参数用于配置AMF支持的NFS的容量标记，标识NFS是否启用容量值，用于控制AMF向NRF注册时，是否携带“capacity”字段，取值及含义如下：否：不携带“capacity”字段是：携带“capacity”字段
命令举例 
`
新增Communication服务，版本号为1。
ADD SERVICECFG:SERVICETYPE="COMMUNICATION",VERSION=1
` 
### 修改服务配置(SET SERVICECFG) 
### 修改服务配置(SET SERVICECFG) 
功能说明 
该命令用于修改指定的AMF的NFS（Network Function Service，网络功能服务）对应的HTTP服务端时IP地址类型、版本号、优先级、容量等信息。 
注意事项 
 
本命令执行后，配置立即生效。 
 
该命令为高危命令！本命令执行后，会修改NFS的相应信息，AMF会自动触发服务信息更新流程，通知NRF，NFS的相应信息已经发生了变化。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3|参数作用：该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
version|URI版本号|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于设置访问对应服务的URI中使用的NFS的版本号。修改影响：如果本参数发生了变化，会影响AMF向NRF注册时，“nfServices”字段中携带的“apiVersionInUri”字段的值，且会触发向NRF更新。数据来源：本端规划。默认值：无。配置原则：无。
ipAddrType|作为服务端IP地址类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|参数作用：该参数用于设置当AMF的NFS作为HTTP服务端时的IP地址类型，取值及含义如下：IPV4IPV6修改影响：如果本参数发生了变化，会影响AMF向NRF注册时，“nfServices”字段中携带的“callbackUri”字段的值，且会触发向NRF更新。数据来源：本端规划。默认值：IPV4。配置原则：无。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|参数作用：该参数用于配置AMF支持的NFS优先级。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据优先级来选择NFS。修改影响：当优先级为有效时，如果该参数发生了变化，会影响AMF向NRF注册时，“nfServices”字段中携带的“priority”字段的值，且会触发向NRF更新。数据来源：本端规划。默认值： 65535。配置原则：该参数在优先级是否有效为是时生效。
priorityFlg|优先级是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ISVALID|参数作用：该参数用于配置AMF支持的NFS的优先级标记，用于标识NFS是否启用优先级，控制AMF向NRF注册时，“nfServices”字段中是否携带的“priority”字段，取值及含义如下：否：不携带“priority”字段是：携带“priority”字段修改影响：修改此参数，会影响AMF向NRF注册时，“nfServices”字段中是否携带的“priority”字段，且会触发向NRF更新。数据来源：本端规划。默认值：是。配置原则：无。
capacity|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535|参数作用：该参数用于配置AMF支持的NFS容量。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据容量比例来选择NFS。修改影响：当容量值为有效时，如果该参数发生了变化，会影响AMF向NRF注册时，“nfServices”字段中携带的“capacity”字段的值，且会触发向NRF更新。数据来源：本端规划。默认值：无。配置原则：无。
capacityFlg|容量值是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：本参数用于配置AMF支持的NFS的容量标记，标识NFS是否启用容量值，用于控制AMF向NRF注册时，是否携带“capacity”字段，取值及含义如下：否：不携带“capacity”字段是：携带“capacity”字段修改影响：修改此参数，会影响AMF向NRF注册时，“nfServices”字段中是否携带的“capacity”字段，且会触发向NRF更新。数据来源：本端规划。默认值：否。配置原则：该参数生效的前提，是容量值是否有效为是时生效。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|参数作用：该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。
version|URI版本号|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于设置访问对应服务的URI中使用的NFS的版本号。
ipAddrType|作为服务端IP地址类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|参数作用：该参数用于设置当AMF的NFS作为HTTP服务端时的IP地址类型，取值及含义如下：IPV4IPV6
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|参数作用：该参数用于配置AMF支持的NFS优先级。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据优先级来选择NFS。
priorityFlg|优先级是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ISVALID|参数作用：该参数用于配置AMF支持的NFS的优先级标记，用于标识NFS是否启用优先级，控制AMF向NRF注册时，“nfServices”字段中是否携带的“priority”字段，取值及含义如下：否：不携带“priority”字段是：携带“priority”字段
capacity|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535|参数作用：该参数用于配置AMF支持的NFS容量。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据容量比例来选择NFS。
capacityFlg|容量值是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：本参数用于配置AMF支持的NFS的容量标记，标识NFS是否启用容量值，用于控制AMF向NRF注册时，是否携带“capacity”字段，取值及含义如下：否：不携带“capacity”字段是：携带“capacity”字段
命令举例 
`
修改Communication服务的版本号为2。
SET SERVICECFG:SERVICETYPE="COMMUNICATION",VERSION=2
` 
### 删除服务配置(DEL SERVICECFG) 
### 删除服务配置(DEL SERVICECFG) 
功能说明 
该命令用于删除AMF支持的NFS（Network Function Service，网络功能服务）。 
注意事项 
 
本命令执行后，配置立即生效。 
 
该命令为高危命令！本命令执行后，会删除NFS的相应信息，AMF会自动触发服务信息更新流程，通知NRF，NFS的相应信息已经发生了变化，而且AMF下的该NFS不能为其他NF提供相应的服务。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3|参数作用：该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|参数作用：该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。
version|URI版本号|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于设置访问对应服务的URI中使用的NFS的版本号。
ipAddrType|作为服务端IP地址类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|参数作用：该参数用于设置当AMF的NFS作为HTTP服务端时的IP地址类型，取值及含义如下：IPV4IPV6
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|参数作用：该参数用于配置AMF支持的NFS优先级。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据优先级来选择NFS。
priorityFlg|优先级是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ISVALID|参数作用：该参数用于配置AMF支持的NFS的优先级标记，用于标识NFS是否启用优先级，控制AMF向NRF注册时，“nfServices”字段中是否携带的“priority”字段，取值及含义如下：否：不携带“priority”字段是：携带“priority”字段
capacity|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535|参数作用：该参数用于配置AMF支持的NFS容量。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据容量比例来选择NFS。
capacityFlg|容量值是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：本参数用于配置AMF支持的NFS的容量标记，标识NFS是否启用容量值，用于控制AMF向NRF注册时，是否携带“capacity”字段，取值及含义如下：否：不携带“capacity”字段是：携带“capacity”字段
命令举例 
`
删除Communication服务。
DEL SERVICECFG:SERVICETYPE="COMMUNICATION"
` 
### 查询服务配置(SHOW SERVICECFG) 
### 查询服务配置(SHOW SERVICECFG) 
功能说明 
该命令用于显示AMF支持的NFS（Network Function Service，网络功能服务），及各个NFS对应的HTTP服务端时的IP地址类型、版本号、优先级、容量等信息。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|参数作用：该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|参数作用：该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。
version|URI版本号|参数可选性: 任选参数类型: 数字参数范围: 0-255|参数作用：该参数用于设置访问对应服务的URI中使用的NFS的版本号。
ipAddrType|作为服务端IP地址类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: IPV4|参数作用：该参数用于设置当AMF的NFS作为HTTP服务端时的IP地址类型，取值及含义如下：IPV4IPV6
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 65535|参数作用：该参数用于配置AMF支持的NFS优先级。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据优先级来选择NFS。
priorityFlg|优先级是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ISVALID|参数作用：该参数用于配置AMF支持的NFS的优先级标记，用于标识NFS是否启用优先级，控制AMF向NRF注册时，“nfServices”字段中是否携带的“priority”字段，取值及含义如下：否：不携带“priority”字段是：携带“priority”字段
capacity|容量|参数可选性: 任选参数类型: 数字参数范围: 0-65535|参数作用：该参数用于配置AMF支持的NFS容量。AMF在向NRF注册时，会将此信息携带给NRF，便于其他NF发现AMF时，根据容量比例来选择NFS。
capacityFlg|容量值是否有效|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: INVALID|参数作用：本参数用于配置AMF支持的NFS的容量标记，标识NFS是否启用容量值，用于控制AMF向NRF注册时，是否携带“capacity”字段，取值及含义如下：否：不携带“capacity”字段是：携带“capacity”字段
命令举例 
`
查询Communication服务信息。
SHOW SERVICECFG:SERVICETYPE="COMMUNICATION"
(No.1) : SHOW SERVICECFG:SERVICETYPE="COMMUNICATION"
-----------------Namf_Communication_0----------------
服务类型    URI版本号  作为服务端IP地址类型 优先级 优先级是否有效 容量 容量值是否有效
namf-comm   1           IPV4                65535   是                  否            
记录数：1
执行成功耗时: 0.096 秒
` 
## SERVICE关联HTTP服务端模板配置 
## SERVICE关联HTTP服务端模板配置 
背景知识 
AMF与PCF、UDM、AUSF、SMF、AMF等网元通过AMF服务化接口进行交互，采用HTTP协议。 
当AMF作为HTTP服务端时，需要对外提供服务端对应的端口、地址等信息。HTTP服务端模板用于配置这些端口、地址等信息。模板ID用于指定配置的HTTP服务端模板。 
功能说明 
本功能用于添加AMF的Service作为HTTP服务端时所关联的HTTP服务端模板ID，间接的设置AMF的各Service作为HTTP服务端时对应的地址、端口。 
HTTP服务端模板在“HTTP配置管理”中进行配置。 
子主题： 
### 新增关联HTTP服务端模板ID配置(ADD ASSOCIATED HTTPSERVERPROFILEID) 
### 新增关联HTTP服务端模板ID配置(ADD ASSOCIATED HTTPSERVERPROFILEID) 
功能说明 
本命令用于新增指定类型AMF的Service作为HTTP服务端时关联的HTTP服务端模板。 
注意事项 
配置本命令的前提，需要切换到CommonS_HTTP_LB配置模式下，通过[ADD SERVERPROFILE]命令配置，先配置HTTP服务端模板。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。该参数用于配置AMF的服务类型（NFS），包括Namf_Communication、Namf_EventExposure、Namf_MT、Namf_Location。AMF包括四种NFS。Namf_Communication，使NF消费者能够通过AMF与UE或RAN通信，该服务使SMF能够请求分配EBI，以支持与EPS互通。参见3GPP TS 23.501协议“5.2.2.2"。 Namf_EventExposure，允许其他消费者获得与移动相关的事件和统计信息的通知。参见3GPP TS 23.501协议“5.2.2.3"。Namf_MT，使NF消费者能够确保UE可以访问。参见3GPP TS 23.501协议“5.2.2.4"。Namf_Location，使NF消费者能够请求目标UE的位置信息。参见3GPP TS 23.501协议“5.2.2.5"。
httpServerProfileId|关联的HTTP服务端模板ID|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数用于设置AMF的NFS关联的HTTP服务端模板ID。本参数的取值是通过SHOW SERVERPROFILE命令查询获取的。
命令举例 
`
新增Communication服务关联HTTP服务端模板ID配置，关联的模板ID为1。
ADD ASSOCIATED HTTPSERVERPROFILEID:SERVICETYPE=COMMUNICATION,HTTPSERVERPROFILEID=1;
` 
### 删除关联HTTP服务端模板ID配置(DEL ASSOCIATED HTTPSERVERPROFILEID) 
### 删除关联HTTP服务端模板ID配置(DEL ASSOCIATED HTTPSERVERPROFILEID) 
功能说明 
本命令用于删除指定类型AMF的Service作为HTTP服务端时关联的HTTP服务端模板。 
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。该参数用于配置AMF的服务类型（NFS），包括Namf_Communication、Namf_EventExposure、Namf_MT、Namf_Location。AMF包括四种NFS。Namf_Communication，使NF消费者能够通过AMF与UE或RAN通信，该服务使SMF能够请求分配EBI，以支持与EPS互通。参见3GPP TS 23.501协议“5.2.2.2"。 Namf_EventExposure，允许其他消费者获得与移动相关的事件和统计信息的通知。参见3GPP TS 23.501协议“5.2.2.3"。Namf_MT，使NF消费者能够确保UE可以访问。参见3GPP TS 23.501协议“5.2.2.4"。Namf_Location，使NF消费者能够请求目标UE的位置信息。参见3GPP TS 23.501协议“5.2.2.5"。
httpServerProfileId|关联的HTTP服务端模板ID|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数用于设置AMF的NFS关联的HTTP服务端模板ID。本参数的取值是通过SHOW SERVERPROFILE命令查询获取的。
命令举例 
`
删除Communication服务关联的HTTP服务端模板ID配置，删除的关联模板ID为1。
DEL ASSOCIATED HTTPSERVERPROFILEID:SERVICETYPE=COMMUNICATION,HTTPSERVERPROFILEID=1;
` 
### 查询关联HTTP服务端模板ID配置(SHOW ASSOCIATED HTTPSERVERPROFILEID) 
### 查询关联HTTP服务端模板ID配置(SHOW ASSOCIATED HTTPSERVERPROFILEID) 
功能说明 
本命令用于查看AMF的Service作为HTTP服务端时关联的HTTP服务端模板ID信息。 
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。该参数用于配置AMF的服务类型（NFS），包括Namf_Communication、Namf_EventExposure、Namf_MT、Namf_Location。AMF包括四种NFS。Namf_Communication，使NF消费者能够通过AMF与UE或RAN通信，该服务使SMF能够请求分配EBI，以支持与EPS互通。参见3GPP TS 23.501协议“5.2.2.2"。 Namf_EventExposure，允许其他消费者获得与移动相关的事件和统计信息的通知。参见3GPP TS 23.501协议“5.2.2.3"。Namf_MT，使NF消费者能够确保UE可以访问。参见3GPP TS 23.501协议“5.2.2.4"。Namf_Location，使NF消费者能够请求目标UE的位置信息。参见3GPP TS 23.501协议“5.2.2.5"。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3|该参数用于设置AMF支持的NFS（Network Function Service，网络功能服务）。该参数用于配置AMF的服务类型（NFS），包括Namf_Communication、Namf_EventExposure、Namf_MT、Namf_Location。AMF包括四种NFS。Namf_Communication，使NF消费者能够通过AMF与UE或RAN通信，该服务使SMF能够请求分配EBI，以支持与EPS互通。参见3GPP TS 23.501协议“5.2.2.2"。 Namf_EventExposure，允许其他消费者获得与移动相关的事件和统计信息的通知。参见3GPP TS 23.501协议“5.2.2.3"。Namf_MT，使NF消费者能够确保UE可以访问。参见3GPP TS 23.501协议“5.2.2.4"。Namf_Location，使NF消费者能够请求目标UE的位置信息。参见3GPP TS 23.501协议“5.2.2.5"。
httpServerProfileId|关联的HTTP服务端模板ID|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数用于设置AMF的NFS关联的HTTP服务端模板ID。本参数的取值是通过SHOW SERVERPROFILE命令查询获取的。
命令举例 
`
查询AMF服务关联的HTTP服务端模板ID配置。
SHOW ASSOCIATED HTTPSERVERPROFILEID:
(No.5) : SHOW ASSOCIATED HTTPSERVERPROFILEID:
-----------------Namf_Communication_0----------------
服务类型                 关联的HTTP服务端模板ID
Namf_Communication       1
记录数：1
执行成功耗时: 0.132 秒
` 
# 接口配置 
# 接口配置 
背景知识 
Namf_Communication服务通过多种接口与其他NF交互完成业务处理流程。具体参见3GPP TS 23502协议“5.2 Network Function services”章节及各NF对应的接口协议，如NSSF协议29531及DNS协议RFC1034。 
功能说明 
本功能用于配置与Namf_Communication服务相关的其他NF如NSSF，DNS等NF的配置信息。 
子主题： 
## DNS配置 
## DNS配置 
背景知识 
在4/5G互操作流程中，AMF需要知道MME的地址，如果在AMF中没有配置MME的地址，则AMF需要到DNS服务器进行查询，以获取MME的地址，此时AMF需要作为DNS客户端，具备DNS客户端的功能。 
功能说明 
本功能用于配置当AMF作为DNS客户端的相关数据。 
DNS配置包含了和DNS服务器交互的DNS全局参数配置、DNS服务器配置、DNS服务器组配置、DNS Profile配置、DNS服务器状态监测机制配置。 
子主题： 
### DNS全局配置 
### DNS全局配置 
背景知识 
DNS全局配置是针对AMF作为DNS客户端的全局参数配置，用于运营商根据实际的网络情况来调整AMF和DNS服务器之间的交互。 
 
DNS UDP查询超时时长（秒）：即AMF采用UDP连接查询DNS服务器，等待DNS服务器响应的时长。运营商可以根据网络时延情况，设置AMF等待DNS服务器响应的时长。 
 
DNS UDP重发次数：AMF重发DNS消息（基于UDP连接）的次数。当运营商希望网络瞬断对业务无影响时，即不因为一次无响应就导致业务失败，则需要配置AMF的重发次数大于1。 
 
TTL（分钟）：即DNS记录的生存时间，该参数决定了AMF和DNS服务器交互的频率，AMF中缓存的TTL取AMF配置的TTL和DNS服务器指定的TTL中较短的值。 
 
DNS查询方式：指AMF基于何种连接方式向DNS服务器发起查询，包括UDP、TCP和UDP优先方式。 
 
支持非权威服务器SOA记录缓存：该参数用来控制AMF是否保存DNS服务器返回的SOA记录。 
 
非权威服务器SOA记录缓存抑制百分比：即当AMF支持非权威服务器SOA记录缓存时，缓存的SOA记录占总缓存记录的百分比。 
 
TCP查询方式超时时长（秒）：即AMF采用TCP连接查询DNS服务器，等待DNS服务器响应的时长。运营商可以根据网络时延情况，设置AMF等待DNS服务器响应的时长。 
 
TCP保活时长（秒）：即AMF向DNS服务器发送保活消息的间隔时长。 
 
功能说明 
DNS全局配置是针对AMF作为DNS客户端的全局参数配置，用于运营商根据实际的网络情况来调整AMF和DNS服务器之间的交互。 
子主题： 
#### 设置DNS全局参数(SET COMMU DNS GLB) 
#### 设置DNS全局参数(SET COMMU DNS GLB) 
功能说明 
该命令用于设置AMF作为DNS客户端的相关参数。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
TIMEOUT|DNS UDP查询超时时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 1-8|该参数用于设置DNS UDP超时时长。当AMF与DNS服务器采用UDP连接时，AMF作为DNS客户端等待DNS服务器响应的时长，当等待时间超过设定的时长后，AMF认为DNS服务器无响应。
MAXRET|DNS UDP重发次数|参数可选性: 任选参数类型: 数字参数范围: 1-3|该参数用于设置DNS UDP重发次数。AMF与DNS服务器采用UDP连接时，AMF等待DNS服务器响应超时后的重发次数。若该值不为零，当AMF等待DNS服务器响应超时后，会重发消息。
TTL|TTL（分钟）|参数可选性: 任选参数类型: 数字参数范围: 1-34560|该参数用于设置TTL，即DNS记录的生存时间。DNS域名解析记录在时长内有效，超时后AMF需要跟DNS服务器重新请求DNS域名解析记录。
MODE|DNS查询方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置DNS查询方式，分为如下三种：UDP（UDP）：UDP方式。TCP（TCP）：TCP方式。UDP优先（UDPFIRST）：UDP优先方式。
SUPPNONASOACACHE|支持非权威服务器SOA记录缓存|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用来控制DNS客户端是否缓存非权威服务器SOA（Start of Authority，起始授权）记录。取值含义如下：不支持：不缓存非权威服务器SOA记录。 支持：缓存非权威服务器SOA记录。
NASOACACHERESPERC|非权威服务器SOA记录缓存抑制百分比|参数可选性: 任选参数类型: 数字参数范围: 1-100|该参数用于设置缓存的非权威SOA（Start of Authority，起始授权）记录数占总缓存记录数的百分比。
DNSTCPTIMEOUT|TCP查询方式超时时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 1-30|AMF与DNS服务器采用TCP连接时，AMF等待DNS服务器响应超时时长（秒）。
TCPALIVETIME|TCP保活时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-7200|AMF与DNS服务器间发送保活消息的间隔时长（秒）。
SUPPADDITIONAL|支持Additional|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|支持接受DNS查询响应中的additional信息。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TIMEOUT|DNS UDP查询超时时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 1-8|该参数用于设置DNS UDP超时时长。当AMF与DNS服务器采用UDP连接时，AMF作为DNS客户端等待DNS服务器响应的时长，当等待时间超过设定的时长后，AMF认为DNS服务器无响应。
MAXRET|DNS UDP重发次数|参数可选性: 任选参数类型: 数字参数范围: 1-3|该参数用于设置DNS UDP重发次数。AMF与DNS服务器采用UDP连接时，AMF等待DNS服务器响应超时后的重发次数。若该值不为零，当AMF等待DNS服务器响应超时后，会重发消息。
TTL|TTL（分钟）|参数可选性: 任选参数类型: 数字参数范围: 1-34560|该参数用于设置TTL，即DNS记录的生存时间。DNS域名解析记录在时长内有效，超时后AMF需要跟DNS服务器重新请求DNS域名解析记录。
MODE|DNS查询方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置DNS查询方式，分为如下三种：UDP（UDP）：UDP方式。TCP（TCP）：TCP方式。UDP优先（UDPFIRST）：UDP优先方式。
SUPPNONASOACACHE|支持非权威服务器SOA记录缓存|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用来控制DNS客户端是否缓存非权威服务器SOA（Start of Authority，起始授权）记录。取值含义如下：不支持：不缓存非权威服务器SOA记录。 支持：缓存非权威服务器SOA记录。
NASOACACHERESPERC|非权威服务器SOA记录缓存抑制百分比|参数可选性: 任选参数类型: 数字参数范围: 1-100|该参数用于设置缓存的非权威SOA（Start of Authority，起始授权）记录数占总缓存记录数的百分比。
DNSTCPTIMEOUT|TCP查询方式超时时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 1-30|AMF与DNS服务器采用TCP连接时，AMF等待DNS服务器响应超时时长（秒）。
TCPALIVETIME|TCP保活时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-7200|AMF与DNS服务器间发送保活消息的间隔时长（秒）。
SUPPADDITIONAL|支持Additional|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|支持接受DNS查询响应中的additional信息。
命令举例 
`
修改DNS UDP查询超时时长为2秒、DNS UDP重发次数为3、TTL为15分钟、DNS查询方式为UDP、支持非权威服务器SOA记录缓存为不支持、非权威服务器SOA记录缓存抑制百分比为80%、TCP查询方式超时时长为6秒和TCP保活时长为2秒。
SET COMMU DNS GLB:TIMEOUT=2,MAXRET=3,TTL=15,MODE="UDP",SUPPNONASOACACHE="NO",NASOACACHERESPERC=80,DNSTCPTIMEOUT=6,TCPALIVETIME=2
` 
#### 查询DNS全局参数(SHOW COMMU DNS GLB) 
#### 查询DNS全局参数(SHOW COMMU DNS GLB) 
功能说明 
该命令用于查询AMF作为DNS客户端的相关参数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TIMEOUT|DNS UDP查询超时时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 1-8|该参数用于设置DNS UDP超时时长。当AMF与DNS服务器采用UDP连接时，AMF作为DNS客户端等待DNS服务器响应的时长，当等待时间超过设定的时长后，AMF认为DNS服务器无响应。
MAXRET|DNS UDP重发次数|参数可选性: 任选参数类型: 数字参数范围: 1-3|该参数用于设置DNS UDP重发次数。AMF与DNS服务器采用UDP连接时，AMF等待DNS服务器响应超时后的重发次数。若该值不为零，当AMF等待DNS服务器响应超时后，会重发消息。
TTL|TTL（分钟）|参数可选性: 任选参数类型: 数字参数范围: 1-34560|该参数用于设置TTL，即DNS记录的生存时间。DNS域名解析记录在时长内有效，超时后AMF需要跟DNS服务器重新请求DNS域名解析记录。
MODE|DNS查询方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|该参数用于设置DNS查询方式，分为如下三种：UDP（UDP）：UDP方式。TCP（TCP）：TCP方式。UDP优先（UDPFIRST）：UDP优先方式。
SUPPNONASOACACHE|支持非权威服务器SOA记录缓存|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用来控制DNS客户端是否缓存非权威服务器SOA（Start of Authority，起始授权）记录。取值含义如下：不支持：不缓存非权威服务器SOA记录。 支持：缓存非权威服务器SOA记录。
NASOACACHERESPERC|非权威服务器SOA记录缓存抑制百分比|参数可选性: 任选参数类型: 数字参数范围: 1-100|该参数用于设置缓存的非权威SOA（Start of Authority，起始授权）记录数占总缓存记录数的百分比。
DNSTCPTIMEOUT|TCP查询方式超时时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 1-30|AMF与DNS服务器采用TCP连接时，AMF等待DNS服务器响应超时时长（秒）。
TCPALIVETIME|TCP保活时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-7200|AMF与DNS服务器间发送保活消息的间隔时长（秒）。
SUPPADDITIONAL|支持Additional|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|支持接受DNS查询响应中的additional信息。
命令举例 
`
查询DNS全局参数。
SHOW COMMU DNS GLB
(No.1) : SHOW COMMU DNS GLB:
-----------------Namf_Communication_0----------------
DNS UDP查询超时时长(秒) DNS UDP重发次数 TTL（分钟） DNS查询方式 支持非权威服务器SOA记录缓存 非权威服务器SOA记录缓存抑制百分比 TCP查询方式超时时长(秒) TCP保活时长(秒) 支持Additional
2                                    3                         15               UDP             不缓存非权威服务器SOA记录    80                                                 6                                 2                      支持接受DNS查询响应中的additional信息
记录数：1
执行成功耗时: 0.084 秒
` 
### DNS服务器配置 
### DNS服务器配置 
背景知识 
AMF作为DNS客户端，可以跟多个DNS服务器相连接。一对客户端地址和服务器地址标识一个DNS服务器。 
AMF最多连接32个DNS服务器。 
功能说明 
本功能用于配置DNS服务器的基本信息，包括DNS客户端地址、DNS服务器端地址、VRFID、DNS服务器编号以及名称。 
子主题： 
#### 新增DNS服务器配置(ADD COMMU DNS SERVER) 
#### 新增DNS服务器配置(ADD COMMU DNS SERVER) 
功能说明 
该命令用于增加DNS服务器配置，包括配置DNS客户端和服务端地址、VRFID和服务器名称。  
注意事项 
 
本命令执行后，配置立即生效。 
 
该命令最多只能配置32条记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器编号|参数可选性: 必选参数类型: 数字参数范围: 1-32|参数作用：该参数用于设置DNS服务器的内部编号，便于索引和进行分组配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
serverIpAddr|DNS服务器IP地址|参数可选性: 必选参数类型: 字符串|参数作用：该参数用于设置DNS服务器地址，可以是IPv4地址也可以是IPv6地址。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
clientIpAddr|DNS客户端IP地址|参数可选性: 必选参数类型: 字符串|参数作用：该参数用于设置DNS客户端地址，和本配置中DNS服务器IP地址需要为同一种类型，即DNS客户端IP地址和DNS服务器IP地址都是IPv4或都是IPv6地址。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
vrfId|VRFID|参数可选性: 必选参数类型: 数字默认值: 0|参数作用：该参数用于设置VRFID，是在VRF配置中已经配置的VRFID。修改影响：无。数据来源：本端规划。默认值：0。配置原则：当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置。
tcpNum|TCP链路数量|参数可选性: 必选参数类型: 数字参数范围: 0-4默认值: 1|参数作用：该参数用于设置AMF和DNS服务器之间的TCP链路数量。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果AMF需要通过TCP方式访问DNS服务器，必须要配置到该DNS服务器的链路，指明需要参与负荷分担的TCP链路条数，AMF自动生成具体的TCP链路。
name|DNS服务器名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置DNS服务器名称。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器编号|参数可选性: 任选参数类型: 数字参数范围: 1-32|参数作用：该参数用于设置DNS服务器的内部编号，便于索引和进行分组配置。
serverIpAddr|DNS服务器IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS服务器地址，可以是IPv4地址也可以是IPv6地址。
clientIpAddr|DNS客户端IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS客户端地址，和本配置中DNS服务器IP地址需要为同一种类型，即DNS客户端IP地址和DNS服务器IP地址都是IPv4或都是IPv6地址。
vrfId|VRFID|参数可选性: 任选参数类型: 数字默认值: 0|参数作用：该参数用于设置VRFID，是在VRF配置中已经配置的VRFID。当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置。
tcpNum|TCP链路数量|参数可选性: 任选参数类型: 数字参数范围: 0-4默认值: 1|参数作用：该参数用于设置AMF和DNS服务器之间的TCP链路数量。
name|DNS服务器名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置DNS服务器名称。
命令举例 
`
新增DNS服务器配置，增加编号为1,DNS服务器IP地址为172.16.12.101，DNS客户端IP地址为100.51.0.52，VRFID为202，1条TCP链路，DNS服务器名称为lte.zte.com.cn的配置
ADD COMMU DNS SERVER:ID=1,SERVERIPADDR="172.16.12.101",CLIENTIPADDR="100.51.0.52",VRFID=202,TCPNUM=1,NAME="lte.zte.com.cn"
` 
#### 修改DNS服务器配置(SET COMMU DNS SERVER) 
#### 修改DNS服务器配置(SET COMMU DNS SERVER) 
功能说明 
该命令用于修改DNS服务器配置，可以修改服务器IP地址、客户端IP地址和VRFID。  
注意事项 
 
本命令执行后，配置立即生效。 
 
不支持修改“DNS服务器编号（ID）”，若需要修改已有配置记录的“DNS服务器编号（ID）”，则应先通过DEL COMMU DNS SERVER命令删除对应的配置记录，然后通过ADD COMMU DNS SERVER命令新增对应的配置记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器编号|参数可选性: 必选参数类型: 数字参数范围: 1-32|参数作用：该参数用于设置DNS服务器的内部编号，便于索引和进行分组配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
serverIpAddr|DNS服务器IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS服务器地址，可以是IPv4地址也可以是IPv6地址。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
clientIpAddr|DNS客户端IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS客户端地址，和本配置中DNS服务器IP地址需要为同一种类型，即DNS客户端IP地址和DNS服务器IP地址都是IPv4或都是IPv6地址。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
vrfId|VRFID|参数可选性: 任选参数类型: 数字默认值: 0|参数作用：该参数用于设置VRFID，是在VRF配置中已经配置的VRFID。修改影响：无。数据来源：本端规划。默认值：0。配置原则：当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置。
tcpNum|TCP链路数量|参数可选性: 任选参数类型: 数字参数范围: 0-4默认值: 1|参数作用：该参数用于设置AMF和DNS服务器之间的TCP链路数量。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果AMF需要通过TCP方式访问DNS服务器，必须要配置到该DNS服务器的链路，指明需要参与负荷分担的TCP链路条数，AMF自动生成具体的TCP链路。
name|DNS服务器名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置DNS服务器名称。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器编号|参数可选性: 任选参数类型: 数字参数范围: 1-32|参数作用：该参数用于设置DNS服务器的内部编号，便于索引和进行分组配置。
serverIpAddr|DNS服务器IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS服务器地址，可以是IPv4地址也可以是IPv6地址。
clientIpAddr|DNS客户端IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS客户端地址，和本配置中DNS服务器IP地址需要为同一种类型，即DNS客户端IP地址和DNS服务器IP地址都是IPv4或都是IPv6地址。
vrfId|VRFID|参数可选性: 任选参数类型: 数字默认值: 0|参数作用：该参数用于设置VRFID，是在VRF配置中已经配置的VRFID。当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置。
tcpNum|TCP链路数量|参数可选性: 任选参数类型: 数字参数范围: 0-4默认值: 1|参数作用：该参数用于设置AMF和DNS服务器之间的TCP链路数量。
name|DNS服务器名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置DNS服务器名称。
命令举例 
`
修改DNS服务器配置，修改DNS服务器编号为1的DNS服务器IP地址为172.16.12.102
SET COMMU DNS SERVER:ID=1,SERVERIPADDR="172.16.12.102"
` 
#### 删除DNS服务器配置(DEL COMMU DNS SERVER) 
#### 删除DNS服务器配置(DEL COMMU DNS SERVER) 
功能说明 
该命令用于根据DNS服务器编号删除DNS服务器配置。  
注意事项 
 
本命令执行后，配置立即生效。 
 
该命令为高危命令！如果“DNS服务器编号（ID）”被ADD COMMU DNS SRVGRP命令引用，则不能通过本命令删除。如果未被引用，本命令执行成功后，不会对业务造成影响。 
 
本命令仅支持一次删除一条配置记录，即删除指定“DNS服务器编号（ID）”对应的配置记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器编号|参数可选性: 必选参数类型: 数字参数范围: 1-32|参数作用：该参数用于设置DNS服务器的内部编号，便于索引和进行分组配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器编号|参数可选性: 任选参数类型: 数字参数范围: 1-32|参数作用：该参数用于设置DNS服务器的内部编号，便于索引和进行分组配置。
serverIpAddr|DNS服务器IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS服务器地址，可以是IPv4地址也可以是IPv6地址。
clientIpAddr|DNS客户端IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS客户端地址，和本配置中DNS服务器IP地址需要为同一种类型，即DNS客户端IP地址和DNS服务器IP地址都是IPv4或都是IPv6地址。
vrfId|VRFID|参数可选性: 任选参数类型: 数字默认值: 0|参数作用：该参数用于设置VRFID，是在VRF配置中已经配置的VRFID。当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置。
tcpNum|TCP链路数量|参数可选性: 任选参数类型: 数字参数范围: 0-4默认值: 1|参数作用：该参数用于设置AMF和DNS服务器之间的TCP链路数量。
name|DNS服务器名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置DNS服务器名称。
命令举例 
`
删除DNS服务器配置，删除DNS服务器编号为8的配置。 
DEL COMMU DNS SERVER:ID=8
` 
#### 查询DNS服务器配置(SHOW COMMU DNS SERVER) 
#### 查询DNS服务器配置(SHOW COMMU DNS SERVER) 
功能说明 
该命令用于查询DNS服务器配置。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器编号|参数可选性: 任选参数类型: 数字参数范围: 1-32|参数作用：该参数用于设置DNS服务器的内部编号，便于索引和进行分组配置。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器编号|参数可选性: 任选参数类型: 数字参数范围: 1-32|参数作用：该参数用于设置DNS服务器的内部编号，便于索引和进行分组配置。
serverIpAddr|DNS服务器IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS服务器地址，可以是IPv4地址也可以是IPv6地址。
clientIpAddr|DNS客户端IP地址|参数可选性: 任选参数类型: 字符串|参数作用：该参数用于设置DNS客户端地址，和本配置中DNS服务器IP地址需要为同一种类型，即DNS客户端IP地址和DNS服务器IP地址都是IPv4或都是IPv6地址。
vrfId|VRFID|参数可选性: 任选参数类型: 数字默认值: 0|参数作用：该参数用于设置VRFID，是在VRF配置中已经配置的VRFID。当需要让DNS接口的信令/数据在某个特定的虚拟路由域内传输时设置。
tcpNum|TCP链路数量|参数可选性: 任选参数类型: 数字参数范围: 0-4默认值: 1|参数作用：该参数用于设置AMF和DNS服务器之间的TCP链路数量。
name|DNS服务器名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置DNS服务器名称。
命令举例 
`
查询DNS服务器配置。 
SHOW COMMU DNS SERVER
(No.1) : SHOW COMMU DNS SERVER:
-----------------Namf_Communication_0----------------
DNS服务器编号     DNS服务器IP地址   DNS客户端IP地址     VRFID   TCPNUM    DNS服务器名称
1                         192.168.32.32        192.168.32.100        0          1
记录数：1
执行成功耗时: 0.095 秒
` 
### DNS服务器组配置 
### DNS服务器组配置 
背景知识 
一个DNS服务器组包含一个或多个DNS服务器，多个DNS服务器之间的工作模式可以是负荷分担或主备，选择策略如下 
 
多个DNS服务器之间为负荷分担时，AMF则需要根据各DNS服务器的权重进行选择，DNS服务器的权重值越大，则被AMF选择的概率越高。 
 
多个DNS服务器之间为主备时（权重值不生效），排列在第一个的服务器是主用DNS服务器，其余都是备用DNS服务器。备用服务器依照排列顺序，优先级逐渐降低，优先级高的服务器可达时，选择高优先级的DNS服务器。 
 
一个DNS服务器组中最多可以配置4个DNS服务器。一个AMF最多配置8个DNS服务器组。 
功能说明 
本功能配置DNS服务器组中关联的DNS服务器编号、权重、DNS服务器的选择模式以及DNS服务器组的名称。 
子主题： 
#### 新增DNS服务器组配置(ADD COMMU DNS SRVGRP) 
#### 新增DNS服务器组配置(ADD COMMU DNS SRVGRP) 
功能说明 
该命令用于增加DNS服务器组配置，包括服务器选择模式、DNS服务器编号、DNS服务器权重DNS服务器组名称。  
注意事项 
 
本命令执行后，配置立即生效。 
 
本命令执行之前，需要确认已经通过ADD COMMU DNS SERVER命令配置了DNS服务器的相关信息。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器组编号|参数可选性: 必选参数类型: 数字参数范围: 1-8|本参数用于配置DNS服务器组编号，后续可以在ADD COMMU DNS PROFILE命令中被引用。
SELECTMODE|选择模式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|本参数用于配置DNS服务器组中DNS服务器的选择模式，有负荷分担和主备两种选择模式。
SRVID1|DNS服务器1ID|参数可选性: 必选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器1编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT1|DNS服务器1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器1在服务器组中的权重。当选择模式为负荷分担时有效
SRVID2|DNS服务器2ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器2编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT2|DNS服务器2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器2在服务器组中的权重。当选择模式为负荷分担时有效
SRVID3|DNS服务器3ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器3编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT3|DNS服务器3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器3在服务器组中的权重。当选择模式为负荷分担时有效
SRVID4|DNS服务器4ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器4编号，本参数的取值来源于ADD COMMU DNS SERVERE配置的值。
WEIGHT4|DNS服务器4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器4在服务器组中的权重。当选择模式为负荷分担时有效
NAME|DNS服务器组名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|本参数用于配置DNS服务器组名称，用于标识一个DNS服务器组。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器组编号|参数可选性: 任选参数类型: 数字参数范围: 1-8|本参数用于配置DNS服务器组编号，后续可以在ADD COMMU DNS PROFILE命令中被引用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|本参数用于配置DNS服务器组中DNS服务器的选择模式，有负荷分担和主备两种选择模式。
SRVID1|DNS服务器1ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器1编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT1|DNS服务器1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器1在服务器组中的权重。当选择模式为负荷分担时有效
SRVID2|DNS服务器2ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器2编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT2|DNS服务器2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器2在服务器组中的权重。当选择模式为负荷分担时有效
SRVID3|DNS服务器3ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器3编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT3|DNS服务器3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器3在服务器组中的权重。当选择模式为负荷分担时有效
SRVID4|DNS服务器4ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器4编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT4|DNS服务器4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器4在服务器组中的权重。当选择模式为负荷分担时有效
NAME|DNS服务器组名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|本参数用于配置DNS服务器组名称，用于标识一个DNS服务器组。
命令举例 
`
新增DNS服务器组，增加DNS服务器组编号为3，选择模式为主备，DNS服务器列表包含服务器编号1和2，DNS服务器组名为"LTE DNS Group"的配置。
ADD COMMU DNS SRVGRP:ID=3,SELECTMODE="BACKUP",SRVID1=1,WEIGHT1=0,SRVID2=2,WEIGHT2=0,NAME="LTE DNS Group"
` 
#### 修改DNS服务器组配置(SET COMMU DNS SRVGRP) 
#### 修改DNS服务器组配置(SET COMMU DNS SRVGRP) 
功能说明 
该命令用于修改服务器选择模式、DNS服务器编号、DNS服务器权重、DNS服务器组名称。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器组编号|参数可选性: 必选参数类型: 数字参数范围: 1-8|本参数用于配置DNS服务器组编号，后续可以在ADD COMMU DNS PROFILE命令中被引用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|本参数用于配置DNS服务器组中DNS服务器的选择模式，有负荷分担和主备两种选择模式。
SRVID1|DNS服务器1ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器1编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT1|DNS服务器1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器1在服务器组中的权重。当选择模式为负荷分担时有效
SRVID2|DNS服务器2ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器2编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT2|DNS服务器2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器2在服务器组中的权重。当选择模式为负荷分担时有效
SRVID3|DNS服务器3ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器3编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT3|DNS服务器3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器3在服务器组中的权重。当选择模式为负荷分担时有效
SRVID4|DNS服务器4ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器4编号，本参数的取值来源于ADD COMMU DNS SERVERE配置的值。
WEIGHT4|DNS服务器4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器4在服务器组中的权重。当选择模式为负荷分担时有效
NAME|DNS服务器组名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|本参数用于配置DNS服务器组名称，用于标识一个DNS服务器组。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器组编号|参数可选性: 任选参数类型: 数字参数范围: 1-8|本参数用于配置DNS服务器组编号，后续可以在ADD COMMU DNS PROFILE命令中被引用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|本参数用于配置DNS服务器组中DNS服务器的选择模式，有负荷分担和主备两种选择模式。
SRVID1|DNS服务器1ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器1编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT1|DNS服务器1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器1在服务器组中的权重。当选择模式为负荷分担时有效
SRVID2|DNS服务器2ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器2编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT2|DNS服务器2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器2在服务器组中的权重。当选择模式为负荷分担时有效
SRVID3|DNS服务器3ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器3编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT3|DNS服务器3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器3在服务器组中的权重。当选择模式为负荷分担时有效
SRVID4|DNS服务器4ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器4编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT4|DNS服务器4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器4在服务器组中的权重。当选择模式为负荷分担时有效
NAME|DNS服务器组名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|本参数用于配置DNS服务器组名称，用于标识一个DNS服务器组。
命令举例 
`
修改DNS服务器组，修改DNS服务器组编号为1记录的选择模式为负荷分担，DNS服务器组名称为LTE DNS Group1
SET COMMU DNS SRVGRP:ID=1,SELECTMODE="PARTAKE",NAME="LTE DNS Group1"
` 
#### 删除DNS服务器组配置(DEL COMMU DNS SRVGRP) 
#### 删除DNS服务器组配置(DEL COMMU DNS SRVGRP) 
功能说明 
该命令用于根据DNS服务器组编号删除DNS服务器组的配置。  
注意事项 
 
本命令执行后，配置立即生效。 
 
该命令为高危命令！如果“DNS服务器组编号（ID）”被ADD COMMU DNS PROFILE命令引用，则不能通过本命令删除。如果未被引用，本命令执行成功后，不会对业务造成影响。 
 
本命令仅支持一次删除一条配置记录，即删除指定“DNS服务器组编号（ID）”对应的配置记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器组编号|参数可选性: 必选参数类型: 数字参数范围: 1-8|本参数用于配置DNS服务器组编号，后续可以在ADD COMMU DNS PROFILE命令中被引用。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器组编号|参数可选性: 任选参数类型: 数字参数范围: 1-8|本参数用于配置DNS服务器组编号，后续可以在ADD COMMU DNS PROFILE命令中被引用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|本参数用于配置DNS服务器组中DNS服务器的选择模式，有负荷分担和主备两种选择模式。
SRVID1|DNS服务器1ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器1编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT1|DNS服务器1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器1在服务器组中的权重。当选择模式为负荷分担时有效
SRVID2|DNS服务器2ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器2编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT2|DNS服务器2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器2在服务器组中的权重。当选择模式为负荷分担时有效
SRVID3|DNS服务器3ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器3编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT3|DNS服务器3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器3在服务器组中的权重。当选择模式为负荷分担时有效
SRVID4|DNS服务器4ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器4编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT4|DNS服务器4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器4在服务器组中的权重。当选择模式为负荷分担时有效
NAME|DNS服务器组名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|本参数用于配置DNS服务器组名称，用于标识一个DNS服务器组。
命令举例 
`
删除DNS服务器组，删除DNS服务器组编号为3的记录。 
DEL COMMU DNS SRVGRP:ID=3
` 
#### 查询DNS服务器组配置(SHOW COMMU DNS SRVGRP) 
#### 查询DNS服务器组配置(SHOW COMMU DNS SRVGRP) 
功能说明 
该命令用于查询指定DNS服务器组编号的配置，若不输入编号则查询所有DNS服务器组的配置。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器组编号|参数可选性: 任选参数类型: 数字参数范围: 1-8|本参数用于配置DNS服务器组编号，后续可以在ADD COMMU DNS PROFILE命令中被引用。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|DNS服务器组编号|参数可选性: 任选参数类型: 数字参数范围: 1-8|本参数用于配置DNS服务器组编号，后续可以在ADD COMMU DNS PROFILE命令中被引用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|本参数用于配置DNS服务器组中DNS服务器的选择模式，有负荷分担和主备两种选择模式。
SRVID1|DNS服务器1ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器1编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT1|DNS服务器1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器1在服务器组中的权重。当选择模式为负荷分担时有效
SRVID2|DNS服务器2ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器2编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT2|DNS服务器2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器2在服务器组中的权重。当选择模式为负荷分担时有效
SRVID3|DNS服务器3ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器3编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT3|DNS服务器3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器3在服务器组中的权重。当选择模式为负荷分担时有效
SRVID4|DNS服务器4ID|参数可选性: 任选参数类型: 数字参数范围: 1-32|本参数用于配置DNS服务器4编号，本参数的取值来源于ADD COMMU DNS SERVER配置的值。
WEIGHT4|DNS服务器4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|本参数用于配置DNS服务器4在服务器组中的权重。当选择模式为负荷分担时有效
NAME|DNS服务器组名称|参数可选性: 任选参数类型: 字符串参数范围: 0-50|本参数用于配置DNS服务器组名称，用于标识一个DNS服务器组。
命令举例 
`
查询DNS服务器组配置，不输入参数查询所有DNS服务器组配置。 
SHOW COMMU DNS SRVGRP:
SHOW COMMU DNS SRVGRP:
------------------------------------------------------------------------------------------------------------------Namf_Communication_0-----------------------------------------------------------------------------------------------------------------
DNS服务器组编号          选择模式         DNS服务器1ID         DNS服务器1权重         DNS服务器2ID         DNS服务器2权重         DNS服务器3ID         DNS服务器3权重         DNS服务器4ID         DNS服务器4权重         DNS服务器组名称
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               1                               主备                            1                                   0                                      0                                     0                                       0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功耗时: 0.205 秒
` 
### DNS Profile配置 
### DNS Profile配置 
背景知识 
DNS Profile是AMF进行DNS查询时，选择DNS服务器的入口，包括EPC Profile和GPRS Profile。 
 
EPC Profile用于AMF进行EPC查询时，选择DNS服务器，GPRS Profile用于AMF进行GPRS查询时，选择DNS服务器。 
 
一个DNS Profile包含一个或多个DNS服务器组，最多四个DNS服务器组，多个DNS服务器组之间可以为负荷分担或主备。 
 
一个DNS Profile包含一个或多个DNS服务器组时，选择策略如下。 
 
多个DNS服务器组之间为负荷分担时，AMF则需要根据各DNS服务器组的权重进行选择，DNS服务器的权重值越大，则被AMF选择的概率越高。 
 
多个DNS服务器组之间为主备时（权重值不生效），则排列在第一个的DNS服务器组是第一优先级的服务器组，依照排列顺序，优先级逐渐降低，优先级高的DNS服务器组中有DNS服务器可达时，则AMF一定选择高优先级的服务器组。 
 
功能说明 
本功能用于配置DNS Profile的基本信息，包括Profile的类型、Profile中关联的服务器组编号、权重和服务器组的选择模式。 
子主题： 
#### 新增DNS Profile配置(ADD COMMU DNS PROFILE) 
#### 新增DNS Profile配置(ADD COMMU DNS PROFILE) 
功能说明 
该命令用于增加DNS Profile配置，主要包括DNS Profile的类型、Profile中关联的DNS服务器组列表。  
注意事项 
 
本命令执行后，配置立即生效。 
 
本命令执行之前，需要确认已经通过ADD COMMU DNS SRVGRP命令配置了DNS服务器组的相关信息。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性用。
SELECTMODE|选择模式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRVGRPID1|DNS服务器组1ID|参数可选性: 必选参数类型: 数字参数范围: 1-8|DNS服务器组1编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT1|DNS服务器组1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组1在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID2|DNS服务器组2ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组2编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT2|DNS服务器组2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组2在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID3|DNS服务器组3ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组3编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT3|DNS服务器组3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组3在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID4|DNS服务器组4ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组4编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT4|DNS服务器组4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组4在本Profile中的权重，当选择模式为负荷分担时有效。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRVGRPID1|DNS服务器组1ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组1编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT1|DNS服务器组1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组1在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID2|DNS服务器组2ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组2编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT2|DNS服务器组2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组2在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID3|DNS服务器组3ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组3编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT3|DNS服务器组3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组3在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID4|DNS服务器组4ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组4编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT4|DNS服务器组4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组4在本Profile中的权重，当选择模式为负荷分担时有效。
命令举例 
`
新增DNS Profile配置，新增DNS Profile类型为GPRS,服务器组列表包含服务器组编号1和服务器组编号2，选择模式为负荷分担的配置。
ADD COMMU DNS PROFILE:TYPE="GPRS",SELECTMODE="PARTAKE",SRVGRPID1=1,WEIGHT1=1,SRVGRPID2=2,WEIGHT2=0,WEIGHT3=0,WEIGHT4=0
` 
#### 修改DNS Profile配置(SET COMMU DNS PROFILE) 
#### 修改DNS Profile配置(SET COMMU DNS PROFILE) 
功能说明 
该命令用于修改EPC Profile或GPRS Profile的配置。包括修改Profile关联的DNS服务器组、选择模式和服务器组的权重。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRVGRPID1|DNS服务器组1ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组1编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT1|DNS服务器组1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组1在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID2|DNS服务器组2ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组2编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT2|DNS服务器组2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组2在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID3|DNS服务器组3ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组3编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT3|DNS服务器组3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组3在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID4|DNS服务器组4ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组4编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT4|DNS服务器组4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组4在本Profile中的权重，当选择模式为负荷分担时有效。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRVGRPID1|DNS服务器组1ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组1编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT1|DNS服务器组1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组1在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID2|DNS服务器组2ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组2编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT2|DNS服务器组2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组2在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID3|DNS服务器组3ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组3编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT3|DNS服务器组3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组3在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID4|DNS服务器组4ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组4编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT4|DNS服务器组4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组4在本Profile中的权重，当选择模式为负荷分担时有效。
命令举例 
`
修改DNS Profile配置，修改DNS Profile类型为GPRS的记录的选择模式为负荷分担，服务器组编号1和服务器组编号2的权重为100。
SET COMMU DNS PROFILE:TYPE="GPRS",SELECTMODE="PARTAKE",SRVGRPID1=1,WEIGHT1=100,SRVGRPID2=2,WEIGHT2=100
` 
#### 删除DNS Profile配置(DEL COMMU DNS PROFILE) 
#### 删除DNS Profile配置(DEL COMMU DNS PROFILE) 
功能说明 
该命令用于删除EPC Profile或GPRS Profile。  
注意事项 
 
本命令执行后，配置立即生效。 
 
该命令为高危命令！本命令执行后，可能导致AMF向DNS查询解析失败，导致业务成功率下降。为避免AMF向DNS查询解析失败，在删除DNS Profile配置之前，需要通过ADD COMMU DNS PROFILE命令添加一条新的DNS Profile配置数据。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性用。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRVGRPID1|DNS服务器组1ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组1编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT1|DNS服务器组1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组1在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID2|DNS服务器组2ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组2编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT2|DNS服务器组2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组2在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID3|DNS服务器组3ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组3编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT3|DNS服务器组3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组3在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID4|DNS服务器组4ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组4编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT4|DNS服务器组4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组4在本Profile中的权重，当选择模式为负荷分担时有效。
命令举例 
`
删除DNS Profile配置，删除DNS Profile类型为GPRS的记录。 
DEL COMMU DNS PROFILE:TYPE="GPRS"
` 
#### 查询DNS Profile配置(SHOW COMMU DNS PROFILE) 
#### 查询DNS Profile配置(SHOW COMMU DNS PROFILE) 
功能说明 
该命令用于查询EPC Profile或GPRS Profile的配置，查看Profile关联的DNS服务器组、选择模式和DNS服务器组权重。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性用。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
TYPE|DNS Profile类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|DNS服务器Profile的类型，用于标识DNS服务器组的类型和属性用。
SELECTMODE|选择模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: BACKUP|服务器组中服务器的选择模式，有负荷分担和主备两种选择模式。
SRVGRPID1|DNS服务器组1ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组1编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT1|DNS服务器组1权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组1在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID2|DNS服务器组2ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组2编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT2|DNS服务器组2权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组2在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID3|DNS服务器组3ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组3编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT3|DNS服务器组3权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组3在本Profile中的权重，当选择模式为负荷分担时有效。
SRVGRPID4|DNS服务器组4ID|参数可选性: 任选参数类型: 数字参数范围: 1-8|DNS服务器组4编号，本参数的取值是通过ADD COMMU DNS SRVGRP命令配置的。
WEIGHT4|DNS服务器组4权重|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 0|DNS服务器组4在本Profile中的权重，当选择模式为负荷分担时有效。
命令举例 
`
查询DNS Profile配置，不输入参数查询所有DNS Profile配置。 
SHOW COMMU DNS PROFILE:
(No.1) : SHOW COMMU DNS PROFILE:
-----------------Namf_Communication_0----------------
DNS Profile类型 选择模式 DNS服务器组1ID DNS服务器组1权重 DNS服务器组2ID DNS服务器组2权重 DNS服务器组3ID DNS服务器组3权重 DNS服务器组4ID DNS服务器组4权重
GPRS                主备       1                       0                                                  0                                                  0                                                  0
记录数：1
执行成功耗时: 0.148 秒
` 
### DNS服务器状态检测配置 
### DNS服务器状态检测配置 
背景知识 
DNS服务器状态检测包括故障检测和故障恢复检测两方面功能。在本功能中，故障检测周期即可用服务器检测周期，故障恢复检测周期即故障服务器握手周期。 
 
故障检测，是指AMF对当前可用的DNS服务器进行定时检测，以便尽快了解其是否故障。 
 
故障恢复检测，是指AMF对当前处于不可用的DNS服务器进行定时检测，以确定其是否恢复可用。 
 
DNS服务器检测方式分为三种类型。 
 
业务触发的检测
是指在业务查询连续失败多次的情况下，将DNS服务器状态置为不可用。 
 
标准协议方式的检测。
是指按照DNS协议的要求，在查询请求中明确指示是状态请求。 
 
自定义查询的检测
是指通过在DNS服务器端配置一个固定的业务不会使用的查询记录，DNS客户端会定时查询该记录，以确定DNS服务器状态。 
 
功能说明 
本功能配置置AMF到DNS服务器之间的状态检测方式、故障检测周期、故障恢复检测周期以及各检测模式下需要的参数。 
子主题： 
#### 设置DNS服务器状态检测配置(SET COMMU DNS SRVCHECK) 
#### 设置DNS服务器状态检测配置(SET COMMU DNS SRVCHECK) 
功能说明 
该命令用于修改DNS服务器状态检测配置。 
注意事项 
当配置DNS检测方式为标准协议方式时，需要确认所有相连的DNS服务器都支持标准协议。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
CHECKTYPE|检测方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置AMF到DNS服务器之间的检测方式，分为如下三种：业务触发的检测是指在业务查询连续失败多次的情况下，将DNS服务器状态置为不可用。标准协议方式的检测是指按照DNS协议的要求，在查询请求中明确指示是状态请求。 自定义查询的检测 是指通过在DNS服务器端配置一个固定的业务不会使用的查询记录，DNS客户端会定时查询该记录，以确定DNS服务器状态。
FLTCHKTIME|可用服务器检测周期（秒）|参数可选性: 任选参数类型: 数字参数范围: 15-300|本参数用于设置状态可达的DNS服务器检测周期，即故障检测周期，当检测方式为标准协议或自定义查询时，必需配置。
RESENDNUM|重发次数|参数可选性: 任选参数类型: 数字参数范围: 1-3|本参数用于设置检测消息的响应超时时重发次数，当检测方式为标准协议或自定义查询时，必需配置。
TIMEOUT|握手超时时长（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-10|本参数用于设置检测消息的响应超时时重发时长，当检测方式为标准协议或自定义查询时，必需配置。
RECOVERTIME|故障服务器握手周期（秒）|参数可选性: 任选参数类型: 数字参数范围: 15-300|本参数用于设置状态不可达的DNS服务器的状态检测周期，即故障恢复周期，当检测方式为标准协议或自定义查询时，必需配置。
RESUMETIME|告警恢复时长（分钟）|参数可选性: 任选参数类型: 数字参数范围: 1-30|本参数用于设置检测方式为业务触发时，则故障发生时间和当前时间差大于等于本配置时，自动恢复服务器为可用，即将告警进行恢复，后继业务可以选择该DNS服务器。
QNAME|查询名称|参数可选性: 任选参数类型: 字符串参数范围: 0-99|本参数用于设置检测方式为自定义查询方式时的查询字符串。
TCPPROTOCOLCHECK|支持TCP协议检测服务器状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|本参数用于设置AMF是否支持TCP协议方式的服务器状态检测。只有在通过SET COMMU DNS GLB命令配置了DNS查询方式为TCP时（通过SHOW COMMU DNS GLB命令查看DNS查询方式），本参数设置为支持才会生效。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CHECKTYPE|检测方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置AMF到DNS服务器之间检测方式，分为如下三种：业务触发的检测是指在业务查询连续失败多次的情况下，将DNS服务器状态置为不可用。标准协议方式的检测是指按照DNS协议的要求，在查询请求中明确指示是状态请求。 自定义查询的检测 是指通过在DNS服务器端配置一个固定的业务不会使用的查询记录，DNS客户端会定时查询该记录，以确定DNS服务器状态。
FLTCHKTIME|可用服务器检测周期（秒）|参数可选性: 任选参数类型: 数字参数范围: 15-300|本参数用于设置状态可达的DNS服务器检测周期，即故障检测周期，当检测方式为标准协议或自定义查询时，必需配置。
RESENDNUM|重发次数|参数可选性: 任选参数类型: 数字参数范围: 1-3|本参数用于设置检测消息的响应超时时重发次数，当检测方式为标准协议或自定义查询时，必需配置。
TIMEOUT|握手超时时长（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-10|本参数用于设置检测消息的响应超时时重发时长，当检测方式为标准协议或自定义查询时，必需配置。
RECOVERTIME|故障服务器握手周期（秒）|参数可选性: 任选参数类型: 数字参数范围: 15-300|本参数用于设置状态不可达的DNS服务器的状态检测周期，即故障恢复周期，当检测方式为标准协议或自定义查询时，必需配置。
RESUMETIME|告警恢复时长（分钟）|参数可选性: 任选参数类型: 数字参数范围: 1-30|本参数用于设置检测方式为业务触发时，则故障发生时间和当前时间差大于等于本配置时，自动恢复服务器为可用，即将告警进行恢复，后继业务可以选择该DNS服务器。
QNAME|查询名称|参数可选性: 任选参数类型: 字符串参数范围: 0-99|本参数用于设置检测方式为自定义查询方式时的查询字符串。
TCPPROTOCOLCHECK|支持TCP协议检测服务器状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|本参数用于设置AMF是否支持TCP协议方式的服务器状态检测。只有在通过SET COMMU DNS GLB命令配置了DNS查询方式为TCP时（通过SHOW COMMU DNS GLB命令查看DNS查询方式），本参数设置为支持才会生效。
命令举例 
`
修改DNS服务器状态检测配置，修改检测方式为标准协议类型，可用服务器检测周期为150秒，重发次数为2次。
SET COMMU DNS SRVCHECK:CHECKTYPE="PROTOCOL",FLTCHKTIME=150,RESENDNUM=2;
` 
#### 查询DNS服务器状态检测配置(SHOW COMMU DNS SRVCHECK) 
#### 查询DNS服务器状态检测配置(SHOW COMMU DNS SRVCHECK) 
功能说明 
该命令用于查询DNS服务器状态检测配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
CHECKTYPE|检测方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|本参数用于设置AMF到DNS服务器之间检测方式，分为如下三种：业务触发的检测是指在业务查询连续失败多次的情况下，将DNS服务器状态置为不可用。标准协议方式的检测是指按照DNS协议的要求，在查询请求中明确指示是状态请求。 自定义查询的检测 是指通过在DNS服务器端配置一个固定的业务不会使用的查询记录，DNS客户端会定时查询该记录，以确定DNS服务器状态。
FLTCHKTIME|可用服务器检测周期（秒）|参数可选性: 任选参数类型: 数字参数范围: 15-300|本参数用于设置状态可达的DNS服务器检测周期，即故障检测周期，当检测方式为标准协议或自定义查询时，必需配置。
RESENDNUM|重发次数|参数可选性: 任选参数类型: 数字参数范围: 1-3|本参数用于设置检测消息的响应超时时重发次数，当检测方式为标准协议或自定义查询时，必需配置。
TIMEOUT|握手超时时长（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-10|本参数用于设置检测消息的响应超时时重发时长，当检测方式为标准协议或自定义查询时，必需配置。
RECOVERTIME|故障服务器握手周期（秒）|参数可选性: 任选参数类型: 数字参数范围: 15-300|本参数用于设置状态不可达的DNS服务器的状态检测周期，即故障恢复周期，当检测方式为标准协议或自定义查询时，必需配置。
RESUMETIME|告警恢复时长（分钟）|参数可选性: 任选参数类型: 数字参数范围: 1-30|本参数用于设置检测方式为业务触发时，则故障发生时间和当前时间差大于等于本配置时，自动恢复服务器为可用，即将告警进行恢复，后继业务可以选择该DNS服务器。
QNAME|查询名称|参数可选性: 任选参数类型: 字符串参数范围: 0-99|本参数用于设置检测方式为自定义查询方式时的查询字符串。
TCPPROTOCOLCHECK|支持TCP协议检测服务器状态|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|本参数用于设置AMF是否支持TCP协议方式的服务器状态检测。只有在通过SET COMMU DNS GLB命令配置了DNS查询方式为TCP时（通过SHOW COMMU DNS GLB命令查看DNS查询方式），本参数设置为支持才会生效。
命令举例 
`
查询DNS服务器状态检测配置。
SHOW COMMU DNS SRVCHECK
(No.1) : SHOW COMMU DNS SRVCHECK:
-----------------Namf_Communication_0----------------
检测方式      可用服务器检测周期（秒） 重发次数  握手超时时长（秒） 故障服务器握手周期（秒） 告警恢复时长（分钟） 查询名称  支持TCP协议检测服务器状态
标准协议方式  180                      3         8                  180                      10                             否
记录数：1
执行成功耗时: 0.318 秒
` 
### DNS缓存配置 
### DNS缓存配置 
背景知识 
AMF作为DNS客户端向DNS服务器查询信息，查询成功后AMF会把查询结果缓存在本地，后续对于同一域名的查询请求，直接使用缓存中的查询结果，不再向DNS服务器进行查询，有效的减少网络中交互的信令数量。 
功能说明 
本功能设置DNS缓存相关参数，如是否支持快速老化、快速老化门限、是否支持缓存保护、缓存保护时长等。 
子主题： 
#### 修改DNS缓存配置(SET DNS CACHE) 
#### 修改DNS缓存配置(SET DNS CACHE) 
功能说明 
该命令用于设置DNS缓存相关参数，如是否支持快速老化、快速老化门限、是否支持缓存保护、缓存保护时长等。当需要对DNS的缓存配置中的参数进行修改时，使用此命令。 
该命令配置成功后，可以通过[SHOW DNS CACHE]命令进行查询 。
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supFastAging|支持快速老化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置AMF是否支持DNS缓存的快速老化功能，选项如下：是：AMF支持DNS缓存快速老化功能。否：AMF不支持DNS缓存快速老化功能。AMF从DNS服务器查询到的结果会携带TTL（生存时间，Time To Live），到达该时间后会将本地缓存记录删掉。快速老化是指不使用TTL，而是使用本配置中的快速老化门限（比如设置为缓存区上限的50%），当缓存记录数达到缓存上限的百分比门限时，快速老化缓存记录。
fastAgingThreshold|快速老化门限(%)|参数可选性: 任选参数类型: 数字参数范围: 50-90默认值: 80|该参数用于设置DNS缓存的快速老化门限值。当AMF支持快速老化功能开启时，该配置值生效，否则该配置值不生效。
supProtectCache|支持缓存保护|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置AMF是否支持DNS缓存保护功能。当AMF对接的所有DNS服务器都不可达时，AMF会对缓存中已经存在的功能进行保护，保证缓存可用，直至有DNS服务器恢复正常状态。是：当所有DNS服务器不可达时，AMF支持DNS缓存保护功能。否：当所有DNS服务器不可达时，AMF不支持DNS缓存保护功能。
protectTimeLen|缓存保护时长(min)|参数可选性: 任选参数类型: 数字参数范围: 0-43200默认值: 30|该参数用于设置缓存保护时长，单位为分钟。缓存保护时长，表示有DNS服务器恢复正常可使用后，延长保护缓存的时间。当AMF支持缓存保护开关开启时，该配置值生效。否则该配置值不生效。
alarmThreshold1|缓存数据区一级告警门限(%)|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 90|该参数用于设置DNS缓存数据区一级告警的门限值，单位为百分比。当DNS缓存数据区的数据超过该门限值，会上报一级告警。
alarmThreshold2|缓存数据区二级告警门限(%)|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 80|该参数用于设置DNS缓存数据区二级告警的门限值，单位为百分比。当DNS缓存数据区的数据超过该门限值，会上报二级告警。
alarmThreshold3|缓存数据区三级告警门限(%)|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 70|该参数用于设置DNS缓存数据区三级告警的门限值，单位为百分比。当DNS缓存数据区的数据超过该门限值，会上报三级告警。
restoreThreshold|缓存数据区告警恢复门限(%)|参数可选性: 任选参数类型: 数字参数范围: 1-100默认值: 65|该参数用于设置DNS缓存数据区告警恢复的门限值，单位为百分比。当DNS缓存数据区的数据低于该门限值，撤销告警。
命令举例 
`
设置DNS缓存配置：支持快速老化、快速老化门限80%、不支持缓存保护、缓存保护时长30分钟、缓存数据区一级告警门限90%、缓存数据区二级告警门限80%、缓存数据区三级告警门限70%、缓存数据区告警恢复门限65%。
SET DNS CACHE:SUPFASTAGING="YES",FASTAGINGTHRESHOLD=80,SUPPROTECTCACHE="NO",PROTECTTIMELEN=30,ALARMTHRESHOLD1=90,ALARMTHRESHOLD2=80,ALARMTHRESHOLD3=70,RESTORETHRESHOLD=65
` 
#### 查询DNS缓存配置(SHOW DNS CACHE) 
#### 查询DNS缓存配置(SHOW DNS CACHE) 
功能说明 
该命令用于查询DNS缓存相关配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supFastAging|支持快速老化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置AMF是否支持DNS缓存的快速老化功能，选项如下：是：AMF支持DNS缓存快速老化功能。否：AMF不支持DNS缓存快速老化功能。AMF从DNS服务器查询到的结果会携带TTL（生存时间，Time To Live），到达该时间后会将本地缓存记录删掉。快速老化是指不使用TTL，而是使用本配置中的快速老化门限（比如设置为缓存区上限的50%），当缓存记录数达到缓存上限的百分比门限时，快速老化缓存记录。
fastAgingThreshold|快速老化门限(%)|参数可选性: 任选参数类型: 数字参数范围: 50-90默认值: 80|该参数用于设置DNS缓存的快速老化门限值。当AMF支持快速老化功能开启时，该配置值生效，否则该配置值不生效。
supProtectCache|支持缓存保护|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置AMF是否支持DNS缓存保护功能。当AMF对接的所有DNS服务器都不可达时，AMF会对缓存中已经存在的功能进行保护，保证缓存可用，直至有DNS服务器恢复正常状态。是：当所有DNS服务器不可达时，AMF支持DNS缓存保护功能。否：当所有DNS服务器不可达时，AMF不支持DNS缓存保护功能。
protectTimeLen|缓存保护时长(min)|参数可选性: 任选参数类型: 数字参数范围: 0-43200默认值: 30|该参数用于设置缓存保护时长，单位为分钟。缓存保护时长，表示有DNS服务器恢复正常可使用后，延长保护缓存的时间。当AMF支持缓存保护开关开启时，该配置值生效。否则该配置值不生效。
alarmThreshold1|缓存数据区一级告警门限(%)|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 90|该参数用于设置DNS缓存数据区一级告警的门限值，单位为百分比。当DNS缓存数据区的数据超过该门限值，会上报一级告警。
alarmThreshold2|缓存数据区二级告警门限(%)|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 80|该参数用于设置DNS缓存数据区二级告警的门限值，单位为百分比。当DNS缓存数据区的数据超过该门限值，会上报二级告警。
alarmThreshold3|缓存数据区三级告警门限(%)|参数可选性: 任选参数类型: 数字参数范围: 0-100默认值: 70|该参数用于设置DNS缓存数据区三级告警的门限值，单位为百分比。当DNS缓存数据区的数据超过该门限值，会上报三级告警。
restoreThreshold|缓存数据区告警恢复门限(%)|参数可选性: 任选参数类型: 数字参数范围: 1-100默认值: 65|该参数用于设置DNS缓存数据区告警恢复的门限值，单位为百分比。当DNS缓存数据区的数据低于该门限值，撤销告警。
命令举例 
`
查询DNS缓存配置。
SHOW DNS CACHE
(No.1) : SHOW DNS CACHE:
-----------------Namf_Communication_0_A----------------
支持快速老化 快速老化门限(%) 支持缓存保护 缓存保护时长(min) 缓存数据区一级告警门限(%) 缓存数据区二级告警门限(%) 缓存数据区三级告警门限(%) 缓存数据区告警恢复门限(%)
是           80              否           30                90                        80                       70                      65
记录数：1
执行成功开始时间:2020-06-30 15:41:29 耗时: 0.937 秒
` 
### DNS功能参数配置 
### DNS功能参数配置 
背景知识 
AMF作为DNS客户端向DNS服务器查询信息，为了方便用户查询关注的信息，需要对查询结果的输出项和输出方式进行配置。 
功能说明 
本功能设置DNS查询的功能参数，用于根据用户的需求，对DNS查询结果的输出项和输出方式进行配置。 
子主题： 
#### 修改DNS功能参数配置(SET DNS FUNCPARA) 
#### 修改DNS功能参数配置(SET DNS FUNCPARA) 
功能说明 
该命令用于设置DNS功能参数配置，用于根据用户的需求，对DNS查询结果的输出项和输出方式进行配置。 
该命令配置成功后，可以通过[SHOW DNS FUNCPARA]命令进行查询 。
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
srvSortMode|SRV记录排序模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BY_DNS_SERVER_OR_BY_ORDER_AND_WEIGHT|该参数用于设置SRV记录的排序模式，选项如下。按照DNS服务器返回顺序或者根据权重优先级进行重新排序：支持多SRV时，则服从DNS服务器返回顺序，不支持多SRV时，则按照SRV的权重优先级进行重新排序。按照DNS服务器返回顺序：无论是否支持多SRV，都服从DNS服务器返回的SRV记录顺序。根据权重优先级进行重新排序：无论是否支持多SRV，都对SRV记录根据权重优先级进行重新排序。
nestQueryMaxTimes|DNS嵌套查询最大次数|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 15|该参数用于设置DNS嵌套查询最大次数，默认为15次。
supAnySoaQuery|解析DNS Additional记录|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: A_AAAA_RECURSION_QUERY|该参数用于设置是否解析DNS Additional记录及查询方式，选项如下：不再进行查询：不查询DNS Additional记录。A/AAAA类递归查询：使用递归查询解析DNS Additional记录，A记录表示查询IPv4记录，AAAA记录表示查询IPv6记录。ANY类迭代查询：使用迭代查询解析DNS Additional记录，ANY表示查询所有类型的记录。
reselectDnsServer|支持DNS查询超时后重选服务器|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否支持DNS查询超时后重选服务器，选项如下：是：支持DNS查询超时后重选DNS服务器。否：不支持DNS查询超时后重选服务器。默认不支持。
supAnyCnameQuery|支持DNS ANY类型C-NAME查询|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置是否支持DNS ANY类型C-NAME查询。如果业务进行DNS查询时选择的查询类型为ANY，并且设置本参数为支持，则从查询结果中匹配出C-NAME记录。选项如下：是：支持DNS ANY类型C-NAME查询。默认支持。 否：不支持DNS ANY类型C-NAME查询。
reselDnsForTcpQry|支持UDP方式的查询结果被截断时重选DNS服务器进行TCP查询|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否支持当UDP方式的DNS查询结果被截断时重选DNS服务器进行TCP查询。选项如下： 是：支持当UDP方式的DNS查询结果被截断时重选DNS服务器进行TCP查询 。否：不支持当UDP方式的DNS查询结果被截断时重选DNS服务器进行TCP查询。默认不支持。
selDnsForUdpPrefer|UDP优先下DNS服务器选择优化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数应用于DNS查询时选择DNS Server的场景。选项如下： 是：在DNS查询方式为UDP优先的前提下，当AMF选择DNS Server并向其发送DNS查询请求时，优先选择UDP和TCP连接状态都正常的DNS Server，如果符合此要求的DNS Server不存在，则选择UDP连接状态正常的DNS Server 。否：在DNS查询方式为UDP优先的前提下，当AMF选择DNS Server并向其发送DNS查询请求时，优先选择UDP连接状态正常的DNS Server。默认为否。
tcpAssemTimeLen|DNS TCP消息重组超时时长（秒）|参数可选性: 任选参数类型: 数字参数范围: 2-180默认值: 30|该参数用于设置DNS TCP消息重组超时时长，默认为30秒。
命令举例 
`
设置DNS功能参数配置：SRV记录排序模式为按照DNS服务器返回顺序或者根据权重优先级进行重新排序、DNS嵌套查询最大次数15次、通过A/AAAA类递归查询解析DNS Additional记录、支持DNS查询超时后重选服务器、支持DNS ANY类型C-NAME查询、不支持UDP方式的查询结果被截断时重选DNS服务器进行TCP查询、DNS TCP消息重组超时时长为30秒。
SET DNS FUNCPARA:SRVSORTMODE="BY_DNS_SERVER_OR_BY_ORDER_AND_WEIGHT",NESTQUERYMAXTIMES=15,SUPANYSOAQUERY="A_AAAA_RECURSION_QUERY",RESELECTDNSSERVER="NO",SUPANYCNAMEQUERY="YES",RESELDNSFORTCPQRY="NO",TCPASSEMTIMELEN=30
` 
#### 查询DNS功能参数配置(SHOW DNS FUNCPARA) 
#### 查询DNS功能参数配置(SHOW DNS FUNCPARA) 
功能说明 
该命令用于查询DNS功能参数配置。当需要确认当前DNS功能参数的配置时，使用该命令。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
srvSortMode|SRV记录排序模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BY_DNS_SERVER_OR_BY_ORDER_AND_WEIGHT|该参数用于设置SRV记录的排序模式，选项如下。按照DNS服务器返回顺序或者根据权重优先级进行重新排序：支持多SRV时，则服从DNS服务器返回顺序，不支持多SRV时，则按照SRV的权重优先级进行重新排序。按照DNS服务器返回顺序：无论是否支持多SRV，都服从DNS服务器返回的SRV记录顺序。根据权重优先级进行重新排序：无论是否支持多SRV，都对SRV记录根据权重优先级进行重新排序。
nestQueryMaxTimes|DNS嵌套查询最大次数|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 15|该参数用于设置DNS嵌套查询最大次数，默认为15次。
supAnySoaQuery|解析DNS Additional记录|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: A_AAAA_RECURSION_QUERY|该参数用于设置是否解析DNS Additional记录及查询方式，选项如下：不再进行查询：不查询DNS Additional记录。A/AAAA类递归查询：使用递归查询解析DNS Additional记录，A记录表示查询IPv4记录，AAAA记录表示查询IPv6记录。ANY类迭代查询：使用迭代查询解析DNS Additional记录，ANY表示查询所有类型的记录。
reselectDnsServer|支持DNS查询超时后重选服务器|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否支持DNS查询超时后重选服务器，选项如下：是：支持DNS查询超时后重选DNS服务器。否：不支持DNS查询超时后重选服务器。默认不支持。
supAnyCnameQuery|支持DNS ANY类型C-NAME查询|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置是否支持DNS ANY类型C-NAME查询。如果业务进行DNS查询时选择的查询类型为ANY，并且设置本参数为支持，则从查询结果中匹配出C-NAME记录。选项如下：是：支持DNS ANY类型C-NAME查询。默认支持。 否：不支持DNS ANY类型C-NAME查询。
reselDnsForTcpQry|支持UDP方式的查询结果被截断时重选DNS服务器进行TCP查询|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于设置是否支持当UDP方式的DNS查询结果被截断时重选DNS服务器进行TCP查询。选项如下： 是：支持当UDP方式的DNS查询结果被截断时重选DNS服务器进行TCP查询 。否：不支持当UDP方式的DNS查询结果被截断时重选DNS服务器进行TCP查询。默认不支持。
selDnsForUdpPrefer|UDP优先下DNS服务器选择优化|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数应用于DNS查询时选择DNS Server的场景。选项如下： 是：在DNS查询方式为UDP优先的前提下，当AMF选择DNS Server并向其发送DNS查询请求时，优先选择UDP和TCP连接状态都正常的DNS Server，如果符合此要求的DNS Server不存在，则选择UDP连接状态正常的DNS Server 。否：在DNS查询方式为UDP优先的前提下，当AMF选择DNS Server并向其发送DNS查询请求时，优先选择UDP连接状态正常的DNS Server。默认为否。
tcpAssemTimeLen|DNS TCP消息重组超时时长（秒）|参数可选性: 任选参数类型: 数字参数范围: 2-180默认值: 30|该参数用于设置DNS TCP消息重组超时时长，默认为30秒。
命令举例 
`
查询DNS功能参数配置。
SHOW DNS FUNCPARA:
(No.1) : SHOW DNS FUNCPARA:
-----------------Namf_Communication_0----------------
操作维护       SRV记录排序模式                                     DNS嵌套查询最大次数 解析DNS Additional记录 支持DNS查询超时后重选服务器 支持DNS ANY类型C-NAME查询 支持UDP方式的查询结果被截断时重选DNS服务器进行TCP查询 UDP优先下DNS服务器选择优化 DNS TCP消息重组超时时长（秒） 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           按照DNS服务器返回顺序或者根据权重优先级进行重新排序 15                  A/AAAA类递归查询       否                          是                        否                                                    否                         30                            
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功耗时: 0.17 秒
` 
# 网络切片配置 
# 网络切片配置 
背景知识 
网络切片可以让运营商在同一套硬件基础设施上，按需划分出多个虚拟的逻辑的端到端网络，每个网络切片在逻辑上隔离，适配各种类型服务的不同特征需求，同时满足高带宽、低时延、超大连接以及多业务支持。 
功能说明 
网络切片配置包括网络切片选择策略、AMF重分配方式、Configured NSSAI策略、网络切片实例。 
子主题： 
## 网络切片策略配置 
## 网络切片策略配置 
背景知识 
网络切片可以让运营商在同一套硬件基础设施上，按需划分出多个虚拟的端到端逻辑网络，适配各种类型服务的不同特征及需求，且每个网络切片在逻辑上隔离。 
网络切片是一个完整的逻辑网络，包含一系列能够提供一定网络能力和网络特性的网络功能和相应资源。网络切片有三个关键特征： 
 
端到端的逻辑网络：网络切片至少包含接入网、承载网、核心网，也可以包含第三方应用。 
 
按需定制的逻辑网络：网络切片可按需提供网络业务，按需提供容量，按需提供切片生命周期，按需分布式部署。 
 
切片之间的隔离：包括安全隔离、资源隔离、操作维护隔离。切片之间相互隔离，一个切片的异常不会影响到其它切片。 
 
终端用户在注册（Registration）过程中，AMF需要为终端用户选择合适的网络切片。如果当前AMF不能满足用户的需求，AMF需要与NSSF进行交互，获取可满足要求的AMF（可以为用户提供所需的网络切片）之后，触发AMF之间的重新定位，参见协议23502第4.2.2.2.3节Registration with AMF re-allocation。 
在PDU会话建立过程中，AMF可能也需要先选择网络切片，进而选择合适的SMF，参见23502协议第4.3.2.2.3.2 Non-roaming and roaming with local breakout。 
功能说明 
该功能用于配置AMF网络切片策略。 
支持网络切片选择功能是指在终端用户注册的过程中，5GC网络需为UE确定Allowed NSSAI和Rejected NSSAI，选择支持Allowed NSSAI的AMF，并把Allowed NSSAI等信息通知终端和NR。 
当同一区域部署了多个网络切片，且不同网络切片中所使用的AMF不同的情况下，需要开启AMF支持网络切片选择功能。 
开启AMF支持网络切片选择功能后，在终端用户注册过程中，AMF会和NSSF进行交互，可能会涉及AMF的重分配流程。在后续的PDU会话建立过程中，AMF首先为当前PDU会话选择合适的NSI（Network Slice instance，网络切片实例），并把Requested S-NSSAI传送给NR。 
配置AMF支持网络切片选择功能后，还涉及到如下配置。 
 
需要通过ADD AMFSNSSAI命令，配置AMF自身所支持的S-NSSAI信息。 
 
当AMF自身不能满足终端用户请求的网络切片时，AMF需要和NSSF进行交互，因此还需要通过ADD NSSFPROFILECFG命令、ADD NSSFSERPROFILECFG命令和ADD NSSFLOCALADDRPOOL命令设置NSSF的地址和端口号。 
 
子主题： 
### 修改网络切片策略配置(SET AMFSUPPOTSLICESELECT) 
### 修改网络切片策略配置(SET AMFSUPPOTSLICESELECT) 
功能说明 
该功能用于设置网络切片策略，当同一区域有多个网络切片，且AMF并不完全共享，有多个AMF Set时，需要开启该功能。 
注意事项 
该命令执行后立即生效。 
本命令需要和[ADD AMFSNSSAI]命令和[SET NSSFPROFILECFG]命令配合使用。
 
当AMF自身能满足终端请求的网络切片时，不需要再向NSSF为UE请求选择合适的网络切片，此时AMF上还需要通过ADD AMFSNSSAI命令配置自身所支持的S-NSSAI。 
 
当AMF自身不能满足终端请求的网络切片时，AMF需要和NSSF进行交互，要求NSSF为UE选择合适的网络切片，还需要通过SET NSSFPROFILECFG命令设置AMF与NSSF通信的IP地址和端口号。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ifServeUeWithAllowed|本地有Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFSUPTSLICESELECT|参数作用：该参数用于配置，在终端用户的注册流程中，如果AMF本地上下文中已经获取了UE的Allowed NSSAI时，AMF是否支持本地网络切片选择功能。修改影响：在设置为"不支持切片选择”的情况下，当AMF已经获取了UE的Allowed NSSAI时，AMF不会选择本地切片，会向NSSF请求协商切片，会加大系统负荷。数据来源：本端规划。默认值：支持切片选择。配置原则：当设置成"不支持切片选择”，表示AMF没有网络切片协商的能力，AMF将UE携带的切片信息和签约的切片信息等都传递给NSSF，由NSSF协商网络切片。当设置成“支持切片选择”，表示AMF有网络切片协商的能力，AMF先进行本地协商切片，判断当前AMF是否能为该UE服务，如果当前AMF能为这个UE服务，则流程继续；如果当前AMF不能为这个UE服务，AMF将UE携带的切片信息和签约的切片信息等都传递给NSSF，由NSSF协商网络切片，并选择可以服务此UE的AMF。
ifServeUeWithout|本地无Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFSUPTSLICESELECT|参数作用：该参数用于配置，在终端用户的注册流程中，如果AMF本地上下文没有获取到UE的Allowed NSSAI时，AMF是否支持本地网络切片选择功能。修改影响：在设置为"不支持切片选择”的情况下，当AMF没有获取UE的Allowed NSSAI时，AMF不会选择本地切片，会向NSSF请求协商切片，会加大系统负荷。数据来源：本端规划。默认值：支持切片选择。配置原则：当设置成"不支持切片选择”，表示AMF没有网络切片协商的能力，AMF将UE携带的切片信息和签约的切片信息等都传递给NSSF，由NSSF协商网络切片。当设置成“支持切片选择”，表示AMF有网络切片协商的能力，AMF先进行本地协商切片，判断当前AMF是否能为该UE服务，如果当前AMF能为这个UE服务，则流程继续；如果当前AMF不能为这个UE服务，AMF将UE携带的切片信息和签约的切片信息等都传递给NSSF，由NSSF协商网络切片，并选择可以服务此UE的AMF。
pduSupSliceSelect|PDU会话建立支持切片选择|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFSUPTSLICESELECT|参数作用：该参数用于配置，在PDU会话建立流程中，AMF是否支持网络切片选择功能。在PDU会话建立过程中，AMF可能也需要先选择网络切片实例，进而选择该切片实例下的SMF，参见3GPP TS 23.502协议"4.3.2.2.3.2 Non-roaming and roaming with local breakout"。修改影响：设置成支持后，在PDU建立流程中，AMF会向NSSF请求支持该SNSSAI的切片实例，会增加系统负荷。数据来源：本端规划。默认值：不支持切片选择。配置原则：无。
processafterfail|切片选择失败后处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTPASS|参数作用：该参数适用于AMF容量比较小的场景，在UE注册流程中，AMF执行切片选择失败后的处理方式。修改影响：无数据来源：本端规划。默认值：不放行。配置原则：无。当设置成放行，AMF执行切片选择失败后，AMF继续处理用户的注册请求。当设置成不放行，AMF执行切片选择失败后，AMF拒绝用户的注册请求，用户注册失败。
regrejcarryrejnssai|是否支持注册拒绝携带reject NSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYREJECTNSSAIINREGREJ|参数作用：该参数用于控制AMF是否在注册拒绝消息中携带rejected NSSAI。修改影响：当参数配置为支持，UE注册流程被拒绝的原因值为#62 (No network slices available)时，AMF会在注册拒绝消息携带reject NSSAI。数据来源：本端规划。默认值：支持注册拒绝携带RejectNssai。配置原则：无。
命令举例 
`
设置AMF网络切片选择策略。
SET AMFSUPPOTSLICESELECT:IFSERVEUEWITHALLOWED="AMFNOTSUPTSLICESELECT",IFSERVEUEWITHOUT="AMFNOTSUPTSLICESELECT",PDUSUPSLICESELECT="AMFNOTSUPTSLICESELECT",PROCESSAFTERFAIL="NOTPASS",REGREJCARRYREJNSSAI="CARRYREJECTNSSAIINREGREJ"
` 
### 查询网络切片策略配置(SHOW AMFSUPPOTSLICESELECT) 
### 查询网络切片策略配置(SHOW AMFSUPPOTSLICESELECT) 
功能说明 
该命令用于查询AMF网络切片选择策略。 
注意事项 
该命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ifServeUeWithAllowed|本地有Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFSUPTSLICESELECT|参数作用：该参数用于配置，在终端用户的注册流程中，AMF本地上下文有UE的Allowed NSSAI时，AMF是否支持本地网络切片选择功能。
ifServeUeWithout|本地无Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFSUPTSLICESELECT|参数作用：该参数用于配置，在终端用户的注册流程中，AMF本地上下文没有UE的Allowed NSSAI时，AMF是否支持本地网络切片选择功能。
pduSupSliceSelect|PDU会话建立支持切片选择|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFSUPTSLICESELECT|参数作用：该参数用于配置，在PDU会话建立流程中，AMF是否支持网络切片选择功能。在PDU会话建立过程中，AMF可能也需要先选择网络切片实例，进而选择该切片实例下的SMF，参见3GPP TS 23.502协议"4.3.2.2.3.2 Non-roaming and roaming with local breakout"。
processafterfail|切片选择失败后处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTPASS|参数作用：该参数主要用于AMF小型化局场景，当UE注册流程执行切片选择失败后的处理方式。
regrejcarryrejnssai|是否支持注册拒绝携带reject NSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYREJECTNSSAIINREGREJ|参数作用：该参数用于控制AMF是否在注册拒绝消息中携带rejected NSSAI。
命令举例 
`
查询本AMF网络切片选择策略。
SHOW AMFSUPPOTSLICESELECT:
(No.4) : SHOW AMFSUPPOTSLICESELECT:
-----------------Namf_Communication_0----------------
操作维护       本地有Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务     本地无Allowed NSSAI时AMF是否被允许确定是否可以为该UE服务    PDU会话建立支持切片选择   切片选择失败后处理     是否支持注册拒绝携带reject NSSAI 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改             支持切片选择                                                                          支持切片选择                                                                             支持切片选择                             不放行               不支持注册拒绝携带RejectNssai    
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-12-25 18:20:44 耗时: 0.138 秒
` 
## AMF Re-allocation方式配置 
## AMF Re-allocation方式配置 
背景知识 
终端向5GC网络注册（Registration）时，如果携带Request NSSAI，但没有携带GUTI（全球唯一临时UE标识，Globally Unique Temporary UE Identity）时，NR会选择默认的AMF为终端服务。 
GUTI是由AMF为移动用户分配的全球唯一临时标识。 
当默认AMF获取到终端的签约数据之后，发现自身无法满足终端的网络切片要求，源AMF需要为终端选择合适的AMF（目标AMF），并将终端转移到目标AMF上。 
在终端注册过程中，源AMF将NAS消息重路由到目标AMF有两种途径： 
 
AMF之间直接传送，源AMF将NAS消息通过Namf_Communication_N1MessageNotify操作，直接传递给目标AMF。 
 
通过RAN传递，源AMF将NAS消息及其目标AMF的信息投递给NR，由NR将NAS报文再发送给目标AMF。 
 
具体流程参见3GPP TS 23502协议的“4.2.2.2.3 Registration with AMF re-allocation”。 
功能说明 
本功能用于设置在Registration with AMF re-allocation流程中，AMF转发NAS报文的具体方式。当开启网络切片选择功能时，需要设置NAS重路由的具体方式。 
如果之前通过[SET AMFSUPPOTSLICESELECT]命令设置AMF支持网络切片功能，则必须配置此功能。
子主题： 
### 修改 AMF重分配方式(SET AMFREALLOCATIONMODE) 
### 修改 AMF重分配方式(SET AMFREALLOCATIONMODE) 
功能说明 
该参数用于配置在终端注册过程中，如果发生了AMF Re-allocation（AMF重定位），在这种情况下，源AMF将NAS消息重新路由到目标AMF的方式。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
amfReallocationMode|AMF重分配模式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NASFROWARDING|参数作用：该参数用于配置在终端注册过程中，如果发生了AMF Re-allocation（AMF重定位），在这种情况下，源AMF将NAS消息重新路由到目标AMF的方式。修改影响：无。数据来源：本端规划。默认值：通过NAS直传。配置原则：运营商根据实际组网情况进行选择。当设置成“通过NAS直传”：表示AMF之间直接传送，源AMF将NAS消息通过Namf_Communication_N1MessageNotify操作，直接传递给目标AMF。当设置成“通过RAN传递”：源AMF将NAS消息及其目标AMF的信息投递给RAN，由RAN将NAS报文再发送给目标AMF。
命令举例 
`
设置AMF Re-allocation过程中转发NAS的方式为“通过RAN”。
SET AMFREALLOCATIONMODE:AMFREALLOCATIONMODE=VIARAN
` 
### 查询 AMF重分配方式(SHOW AMFREALLOCATIONMODE) 
### 查询 AMF重分配方式(SHOW AMFREALLOCATIONMODE) 
功能说明 
该参数用于查询在终端注册过程中，如果发生了AMF Re-allocation（AMF重定位），在这种情况下，源AMF将NAS消息重新路由到目标AMF的方式。 
注意事项 
该命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
amfReallocationMode|AMF重分配模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NASFROWARDING|参数作用：该参数用于配置在终端注册过程中，如果发生了AMF Re-allocation（AMF重定位），在这种情况下，源AMF将NAS消息重新路由到目标AMF的方式。
命令举例 
`
查询AMF Re-allocation过程中转发NAS的方式。
SHOW AMFREALLOCATIONMODE:
(No.1) : SHOW AMFREALLOCATIONMODE:
-----------------Namf_Communication_0----------------
AMF重定位模式
通过ran
记录数：1
执行成功耗时: 5.005 秒
` 
## Configured NSSAI配置 
## Configured NSSAI配置 
背景知识 
在以下几种场景中，5GC会下发准确和完整的Configured NSSAI给终端，便于终端使用网络切片。 
 
首次接入VPLMN的漫游用户 
 
终端用户的签约NSSAI发生改变 
 
终端的Configured NSSAI不完整或有错误 
 
功能说明 
Configured NSSAI配置包括下发Configured NSSAI的策略，以及下发的Configured NSSAI列表。 
子主题： 
### Configured NSSAI下发策略配置 
### Configured NSSAI下发策略配置 
背景知识 
本功能用于配置AMF是否可以通过Registration Accept消息或者Configuration Upadte Command消息中将Configured NSSAI下发给UE。 
AMF是否可以下发Configured NSSAI给终端，包括如下情况： 
 
强制下发（FORCESEND）：允许通过Registration Accept或者Configuration Upadte Command消息中将Configured NSSAI下发给UE，但最终是否下发，还需要取决于其他配置项目，包括UE是否在ConfiguredNssai号段规划内、UE对应的ConfiguredNssai获取策略、签约NSSAI、AMF上的配置等条件（参见"Configured SNSSAI配置"、"Configured NSSAI Supi 号段配置"、"默认Configured Snssai 策略配置"及"默认Configured Snssai 标识列表配置"的说明）。 
 
强制不下发（FORCENOTSEND）： 不允许通过Registration Accept或者Configuration Upadte Command将Configured NSSAI下发给UE。 
 
系统判断(SYSTEMDEF)： 根据系统来决定是否下发。 
 
对于系统判断(SYSTEMDEF)这种情况，详细描述如下： 
本选项仅用于判断在UE注册（Registration）过程中是否下发Configured NSSAI，不涉及Configuration Upadte流程。 
3GPP TS 24501协议的5.5.1.2.4章节中描述：当Registration Request（注册请求）消息满足如下条件时，网络侧可以在Registration Accept消息中将Configured NSSAI下发给UE： 
Registration Request消息中未携带Request NSSAI 
Registration Request消息中携带的Request NSSAI包含UE服务PLMN非法的S-NSSAI(s) 
Registration Request消息中携带的Request NSSAI包含错误的S-NSSAI(s) 
Registration Request消息中携带Network slicing indication字段，指示UE携带的Request NSSAI来自于默认Configured NSSAI(DCNI is set to "1") 
目前，在1和4这两种条件中。允许AMF在Registration Accept消息给UE下发Configured NSSAI，但最终是否下发，取决于UE是否在Configured NSSAI号段规划内、UE对应的Configured NSSAI获取策略、签约NSSAI、AMF上的配置等条件(参见"Configured SNSSAI配置"、"Configured NSSAI Supi 号段配置"、"默认Configured NSSAI策略配置"及"默认Configured NSSAI标识列表配置"的说明)。不满足条件1或条件4，则强制不下发。 
另外，对于Configuration Upadte流程，若UE最终匹配到的获取策略为“系统判断”，则按照“强制下发”的处理逻辑决策是否在Configuration Upadte Command中下发Configured NSSAI 。 
功能说明 
本功能用于配置AMF是否可以通过Registration Accept消息或者Configuration Upadte Command将Configured NSSAI下发给UE。 
子主题： 
#### 修改ConfiguredNssai控制配置(SET CONFIGNSSAICONTROL) 
#### 修改ConfiguredNssai控制配置(SET CONFIGNSSAICONTROL) 
功能说明 
本命令用于配置AMF是否可以通过Registration Accept消息或者Configuration Update Command消息中将Configured NSSAI下发给UE。 
注意事项 
该命令执行后立即生效。 
AMF可以通过Registration Accept消息或者Configuration Update Command消息将Configured NSSAI下发给UE，但最终是否下发给UE，是由其他命令的配置结果以及用户本身的NSSAI签约信息等条件共同决策的，涉及到的命令包括： 
 
UE的号码是否在Configured NSSAI号段规划的号段范围内（通过ADD CONFIG SNSSAI SUPI命令配置） 
 
SUPI号段与Configured SNSSAI列表的对应关系（通过ADD SUPI CONFIG SNSSAIID LIST配置） 
 
默认Configured NSSAI的获取策略（通过SET DEFAULT CONFIG SNSSAI POLICY命令配置） 
 
默认的Configured SNSSAI标识（通过ADD DEFAULT CONFIG SNSSAI ID命令配置） 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
configNssaiControl|Configured NSSAI下发控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: FORCESEND|参数作用：本参数用于配置AMF是否可以通过Registration Accept消息或者Configuration Update Command消息将Configured NSSAI下发给UE。强制下发（Force Send）：AMF可以通过Registration Accept消息或者Configuration Update Command消息将Configured NSSAI下发给UE，但最终是否下发给UE，是由其他命令的配置结果以及用户本身的签约信息等条件共同决策的 ，包括UE的号码是否在Configured NSSAI号段规划内（通过ADD CONFIG SNSSAI SUPI命令配置）、SUPI号段与Configured SNSSAI列表的对应关系（通过ADD SUPI CONFIG SNSSAIID LIST配置）、默认Configured NSSAI的获取策略（通过SET DEFAULT CONFIG SNSSAI POLICY命令配置）、默认的Configured SNSSAI标识（通过ADD DEFAULT CONFIG SNSSAI ID命令配置）及用户的NSSAI签约信息等。强制不下发（Force Not Send）：AMF不允许通过Registration Accept消息或者Configuration Update Command将Configured NSSAI下发给UE。系统判断（System Define）：根据系统来决定是否下发。策略配置为系统判断时，仅用于判断AMF在UE注册（Registration）流程中是否下发Configuration Nssai给UE，不涉及配置更新（Configuration Update）流程。修改影响：修改此参数，影响AMF给UE下发Configured NSSAI的策略。 数据来源：本端规划。 默认值：强制下发（Force Send）。配置原则： “系统判断（System Define）”这个选项的配置原则如下：3GPP TS 24501协议的5.5.1.2.4描述：当Registration Request（注册请求）消息满足如下条件时，网络侧可以在Registration Accept消息中将Configured NSSAI下发给UE：条件1：Registration Request消息中未携带Request NSSAI。条件2：Registration Request消息中携带的Request NSSAI包含UE服务PLMN非法的S-NSSAI(s)。条件3：Registration Request消息中携带的Request NSSAI包含错误的S-NSSAI(s)。条件4：Registration Request消息中携带Network slicing indication字段，指示UE携带的Request NSSAI来自于默认Configured NSSAI(DCNI is set to "1")。目前，当满足条件1或条件4时，允许AMF在Registration Accept消息给UE下发Configured NSSAI，但最终是否下发给UE，是由其他命令的配置结果以及用户本身的签约信息等条件共同决策的 ，包括UE的号码是否在Configured NSSAI号段规划内（通过ADD CONFIG SNSSAI SUPI命令配置）、SUPI号段与Configured SNSSAI列表的对应关系（通过ADD SUPI CONFIG SNSSAIID LIST配置）、默认Configured NSSAI的获取策略（通过SET DEFAULT CONFIG SNSSAI POLICY命令配置）、默认的Configured SNSSAI标识（通过ADD DEFAULT CONFIG SNSSAI ID命令配置）及用户的NSSAI签约信息等。不满足条件1或条件4，则强制不下发。对于配置更新（Configuration Update）流程，若UE最终匹配到的获取策略为“系统判断”，则按照“强制下发”的判断逻辑决策是否在Configuration Update Command中下发Configured NSSAI。
命令举例 
`
设置ConfiguredNssai下发控制为强制不下发。
SET CONFIGNSSAICONTROL:CONFIGNSSAICONTROL=FORCENOTSEND
` 
#### 查询ConfiguredNssai控制配置(SHOW CONFIGNSSAICONTROL) 
#### 查询ConfiguredNssai控制配置(SHOW CONFIGNSSAICONTROL) 
功能说明 
该命令用于查询AMF是否允许向UE下发Configured NSSAI。 
注意事项 
该命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
configNssaiControl|Configured NSSAI下发控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: FORCESEND|参数作用：本参数用于配置AMF是否可以通过Registration Accept消息或者Configuration Update Command消息将Configured NSSAI下发给UE。
命令举例 
`
查询ConfiguredNssai下发控制配置。
SHOW CONFIGNSSAICONTROL:
(No.1) : SHOW CONFIGNSSAICONTROL:
-----------------Namf_Communication_0----------------
ConfiguredNssai下发控制 强制不下发
记录数：1
执行成功耗时: 5.005 秒
` 
### Configured SNSSAI配置 
### Configured SNSSAI配置 
背景知识 
Configured NSSAI（配置NSSAI）的概念，属于网络切片的范畴，用于AMF向UE指示5GC网络可以提供的网络切片业务。典型应用场景如下： 
 
对于漫游用户，UE首次接入VPLMN 5GC网络时，UE携带的请求的NSSAI一般为空或者可能是通用的NSSAI，5GC下发给UE的Allowed NSSAI为默认签约NSSAI或被授权的通用NSSAI。根据漫游协议，VPLMN 5GC网络需要为UE提供除了默认签约NSSAI和被授权的通用NSSAI之外的网络切片业务时，可以通过Configured NSSAI指示给UE。或者，漫游用户的签约NSSAI发生改变时，也可通过Configured NSSAI指示给UE。 
 
对于本地用户，在USIM中已写入了Configured NSSAI，如果后续5GC网络新增了网络切片业务（比如新增了签约NSSAI），可以为UE提供新的网络切片业务时，可以通过Configured NSSAI指示给UE。 
 
Configured NSSAI可以在UE在注册（Registration）过程或UE配置更新过程中，AMF通过Registration Accept消息或者Configuration Upadte Command消息投递给UE。 
Configured NSSAI需要依据AMF SUPI号段Configured NSSAI配置(参见[ADD CONFIG SNSSAI SUPI]和[ADD SUPI CONFIG SNSSAIID LIST]或者默认Configured NSSAI相关配置(参见[SET DEFAULT CONFIG SNSSAI POLICY]和[ADD DEFAULT CONFIG SNSSAI ID])确定。
功能说明 
本功能通过增加1-4096个S-NSSAI而形成一个AMF本地的Configured NSSAI 集合，“按号段Configured NSSAI配置”和“默认Configured NSSAI配置”中的”配置SNSSAI标识”均必须引用本功能的配置数据。 
该功能配置的结果，用于后续配置SNSSAI标识使用，涉及到[SET DEFAULT CONFIG SNSSAI POLICY]命令和[ADD DEFAULT CONFIG SNSSAI ID]命令。
子主题： 
#### 新增ConfiguredSnssai配置(ADD CONFIGUREDSNSSAI) 
#### 新增ConfiguredSnssai配置(ADD CONFIGUREDSNSSAI) 
功能说明 
该命令用于增加一个AMF本地配置的S-NSSAI。 
S-NSSAI标识为关键字，AMF内唯一。对于某个指定S-NSSAI，可以仅配置SST，也可以同时配置SST和SD。 
注意事项 
该命令执行后立即生效。 
如果增加的S-NSSAI没有SD，则配置为“NULL”。 
每个SNSSAI标识，只能对应一个S-NSSAI。 
本命令配置的参数“SNSSAIID”会被[ADD SUPI CONFIG SNSSAIID LIST]或[ADD DEFAULT CONFIG SNSSAI ID]命令关联使用。
最多可以增加4096条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
snssaiId|SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于标识一个配置S-NSSAI，该参数在本AMF内唯一标识一个S-NSSAI。修改影响：此参数为本配置的主键，不可以修改，如需修改，需要先通过DEL CONFIGUREDSNSSAI命令删除配置记录，再通过ADD CONFIGUREDSNSSAI命令}命令增加。数据来源：本端规划。 默认值：无。配置原则：本参数配置的数值会被ADD SUPI CONFIG SNSSAIID LIST或ADD DEFAULT CONFIG SNSSAI ID命令关联使用。
sst|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。修改影响：修改SST，最终可以影响AMF带给UE的Configured NSSAI。数据来源：本端规划。默认值：无。配置原则：目前协议明确的SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：修改SD，最终可以影响AMF带给UE的Configured NSSAI。数据来源：本端规划 默认值：无。配置原则：无。
命令举例 
`
新增标识为1的配置S-NSSAI，SST为"eMBB"，SD为"1234AB。
ADD CONFIGUREDSNSSAI:SNSSAIID=1,SST="eMBB",SD="1234AB"
` 
#### 修改ConfiguredSnssai配置(SET CONFIGUREDSNSSAI) 
#### 修改ConfiguredSnssai配置(SET CONFIGUREDSNSSAI) 
功能说明 
该命令用于修改一个已经成功配置的本地配置S-NSSAI。 
可以仅修改某个SNSSAI标识对应的SST，也可以同时修改SST和SD。 
注意事项 
该命令执行后立即生效。 
只能修改参数“SD”和参数“SST”，参数“SNSSAID”为主键，不能修改，如需修改，需要先通过[DEL CONFIGUREDSNSSAI]命令删除配置记录，再通过[DEL CONFIGUREDSNSSAI]命令}命令增加。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
snssaiId|SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于标识一个配置S-NSSAI，该参数在本AMF内唯一标识一个S-NSSAI。修改影响：此参数为本配置的主键，不可以修改，如需修改，需要先通过DEL CONFIGUREDSNSSAI命令删除配置记录，再通过ADD CONFIGUREDSNSSAI命令}命令增加。数据来源：本端规划。 默认值：无。配置原则：本参数配置的数值会被ADD SUPI CONFIG SNSSAIID LIST或ADD DEFAULT CONFIG SNSSAI ID命令关联使用。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。修改影响：修改SST，最终可以影响AMF带给UE的Configured NSSAI。数据来源：本端规划。默认值：无。配置原则：目前协议明确的SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：修改SD，最终可以影响AMF带给UE的Configured NSSAI。数据来源：本端规划 默认值：无。配置原则：无。
命令举例 
`
修改已经配置成功的标识为1的配置S-NSSAI，SD由"1234AB修改为"ABCDEF"。"eMBB"不变。
SET CONFIGUREDSNSSAI:SNSSAIID=1,SD="ABCDEF"
` 
#### 删除ConfiguredSnssai配置(DEL CONFIGUREDSNSSAI) 
#### 删除ConfiguredSnssai配置(DEL CONFIGUREDSNSSAI) 
功能说明 
该命令用于通过一个已经成功配置的S-NSSAI标识，删除一个配置S-NSSAI。 
注意事项 
该命令执行后立即生效。 
如果需要删除的S-NSSAI标识已被[ADD SUPI CONFIG SNSSAIID LIST]或[ADD DEFAULT CONFIG SNSSAI ID]命令关联使用，则不可以删除，需要先通过[DEL SUPI CONFIG SNSSAIID LIST]命令或者[DEL DEFAULT CONFIG SNSSAI ID]命令删除关联配置后，才能通过本命令进行删除。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
snssaiId|SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于标识一个配置S-NSSAI，该参数在本AMF内唯一标识一个S-NSSAI。修改影响：此参数为本配置的主键，不可以修改，如需修改，需要先通过DEL CONFIGUREDSNSSAI命令删除配置记录，再通过ADD CONFIGUREDSNSSAI命令}命令增加。数据来源：本端规划。 默认值：无。配置原则：本参数配置的数值会被ADD SUPI CONFIG SNSSAIID LIST或ADD DEFAULT CONFIG SNSSAI ID命令关联使用。
命令举例 
`
删除已经成功配置的标识为1的配置S-NSSAI。
DEL CONFIGUREDSNSSAI:SNSSAIID=1
` 
#### 查询ConfiguredSnssai配置(SHOW CONFIGUREDSNSSAI) 
#### 查询ConfiguredSnssai配置(SHOW CONFIGUREDSNSSAI) 
功能说明 
该命令用于查询AMF配置的所有S-NSSAI的详细信息。 
注意事项 
该命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
snssaiId|SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于标识一个配置S-NSSAI，该参数在本AMF内唯一标识一个S-NSSAI。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
命令举例 
`
查询AMF上所有的配置S-NSSAI。
 SHOW CONFIGUREDSNSSAI:
(No.8) : SHOW CONFIGUREDSNSSAI:
--------------------------------
SNSSAI标识    SST      SD
1             eMBB     ABCDEF
333           100      NULL
记录数：2
执行成功耗时: 0.411 秒
` 
### 按号段Configured NSSAI来源策略配置 
### 按号段Configured NSSAI来源策略配置 
背景知识 
AMF根据SUPI号段来配置S-NSSAI信息，具体地，就是为每个SUPI号段配置相应的"S-NSSAI标识列表"和"获取策略"，其中"S-NSSAI标识列表"是通过[ADD SUPI CONFIG SNSSAIID LIST]命令配置的。
"获取策略"的详细说明如下： 
 
本地配置(LOCALCONFIGURED): AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。 
 
签约(SUBSCRIPTION)： AMF下发给UE的Configured NSSAI是签约NSSAI。 
 
NSSF优先(SYSTEMDEF)： 如果UE在注册(Registration)过程中，AMF向NSSF成功获取过切片信息，则AMF下发给Configured NSSAI为NSSF返回的Configured NSSAI。 
 
功能说明 
本功能用于配置每个SUPI号段的NSSAI获取策略。 
子主题： 
#### 新增Configured Snssai Supi 配置(ADD CONFIG SNSSAI SUPI) 
#### 新增Configured Snssai Supi 配置(ADD CONFIG SNSSAI SUPI) 
功能说明 
本命令用于配置AMF支持根据UE对应的SUPI号段来获取对应NSSAI的策略。 
注意事项 
该命令执行后立即生效。 
当本命令的参数"CONFISNSSAIPOLICY"配置为"本地配置(LOCALCONFIGURED)"时，本命令配置的参数“SUPISEGMENT”会被[ADD SUPI CONFIG SNSSAIID LIST]命令关联使用。操作员后续需要通过[ADD SUPI CONFIG SNSSAIID LIST]命令增加对应号段的配置数据。 比如通过本命令配置4600123号段用户的NSSAI的获取来源为"本地配置(LOCALCONFIGURED)"，后续必须通过[ADD SUPI CONFIG SNSSAIID LIST]命令增加4600123号段的相关配置。
根据用户的SUPI号码，匹配本命令配置的数据时，AMF按照号段最长匹配原则进行匹配。比如，存在46001和4600123两个号段的配置数据时，对于用户46001234567890，AMF按照4600123号段的配置数据进行匹配。 
如果根据用户的SUPI号码，无法匹配到本命令配置的数据，即AMF无法获取到某个用户的NSSAI，则AMF会为用户分配默认NSSAI，默认的NSSAI的获取策略是通过[SET DEFAULT CONFIG SNSSAI POLICY]命令和[ADD DEFAULT CONFIG SNSSAI ID]命令配置的。
最多可以配置1000条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。修改影响：该参数为此配置的主键，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
confiSnssaiPolicy|Configured NSSAI 策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于配置某个SUPI号段获取Configured NSSAI的策略。修改影响：修改此参数会影响AMF获取UE的Configured NSSAI的策略。数据来源：本端规划。 默认值：无。配置原则：本地配置(LOCALCONFIGURED)： AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。签约(SUBSCRIPTION)：AMF下发给UE的Configured NSSAI是用户签约的NSSAI。NSSF优先(NSSFPRIORITY)：如果UE在注册（Registration）过程中，AMF向NSSF成功获取过切片信息，则AMF下发给UE的Configured NSSAI是NSSF之前向AMF返回的Configured NSSAI。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
confiSnssaiPolicy|Configured NSSAI 策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于配置某个SUPI号段获取Configured NSSAI的策略。本地配置(LOCALCONFIGURED): AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。签约(SUBSCRIPTION)：AMF下发给UE的Configured NSSAI是签约NSSAI。NSSF优先(NSSFPRIORITY)：如果UE在注册（Registration）过程中，AMF向NSSF成功获取过切片信息，则AMF下发给UE的Configured NSSAI是NSSF之前向AMF返回的Configured NSSAI。
命令举例 
`
将SUPI号段"4601100"加入配置NSSAI规划，获取策略设置为"签约(SUBSCRIPTION)"。
ADD CONFIG SNSSAI SUPI:SUPISEGMENT="4601100",CONFISNSSAIPOLICY="SUBSCRIPTION"
` 
#### 修改Configured Snssai Supi 配置(SET CONFIG SNSSAI SUPI) 
#### 修改Configured Snssai Supi 配置(SET CONFIG SNSSAI SUPI) 
功能说明 
该命令用于修改一个已经成功配置的"Configured NSSAI SUPI号段"的NSSAI获取策略。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。修改影响：该参数为此配置的主键，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
confiSnssaiPolicy|Configured NSSAI 策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于配置某个SUPI号段获取Configured NSSAI的策略。修改影响：修改此参数会影响AMF获取UE的Configured NSSAI的策略。数据来源：本端规划。 默认值：无。配置原则：本地配置(LOCALCONFIGURED)： AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。签约(SUBSCRIPTION)：AMF下发给UE的Configured NSSAI是用户签约的NSSAI。NSSF优先(NSSFPRIORITY)：如果UE在注册（Registration）过程中，AMF向NSSF成功获取过切片信息，则AMF下发给UE的Configured NSSAI是NSSF之前向AMF返回的Configured NSSAI。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
confiSnssaiPolicy|Configured NSSAI 策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于配置某个SUPI号段获取Configured NSSAI的策略。本地配置(LOCALCONFIGURED): AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。签约(SUBSCRIPTION)：AMF下发给UE的Configured NSSAI是签约NSSAI。NSSF优先(NSSFPRIORITY)：如果UE在注册（Registration）过程中，AMF向NSSF成功获取过切片信息，则AMF下发给UE的Configured NSSAI是NSSF之前向AMF返回的Configured NSSAI。
命令举例 
`
将已经成功配置的SUPI号段"4601100"的Configured NSSAI获取策略修改为"本地配置(LOCALCONFIGURE)"。
SET CONFIG SNSSAI SUPI:SUPISEGMENT="4601100",CONFISNSSAIPOLICY="LOCALCONFIGURED"
` 
#### 删除Configured Snssai Supi 配置(DEL CONFIG SNSSAI SUPI) 
#### 删除Configured Snssai Supi 配置(DEL CONFIG SNSSAI SUPI) 
功能说明 
该命令用于删除一个已经成功配置的"Configured NSSAI SUPI号段号段"的NSSAI获取策略。 
注意事项 
该命令执行后立即生效。 
如果需要删除的SUPI号段已经在[ADD SUPI CONFIG SNSSAIID LIST]命令中被关联，则无法删除，必须先通过[DEL SUPI CONFIG SNSSAIID LIST]命令删除关联配置后，才能通过本命令进行删除。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。修改影响：该参数为此配置的主键，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
confiSnssaiPolicy|Configured NSSAI 策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于配置某个SUPI号段获取Configured NSSAI的策略。本地配置(LOCALCONFIGURED): AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。签约(SUBSCRIPTION)：AMF下发给UE的Configured NSSAI是签约NSSAI。NSSF优先(NSSFPRIORITY)：如果UE在注册（Registration）过程中，AMF向NSSF成功获取过切片信息，则AMF下发给UE的Configured NSSAI是NSSF之前向AMF返回的Configured NSSAI。
命令举例 
`
将已经成功配置的SUPI号段"4601100"从AMF配置NSSAI规划中移除。
DEL CONFIG SNSSAI SUPI:SUPISEGMENT="4601100"
` 
#### 查询Configured Snssai Supi 配置(SHOW CONFIG SNSSAI SUPI) 
#### 查询Configured Snssai Supi 配置(SHOW CONFIG SNSSAI SUPI) 
功能说明 
该命令通过特定"SUPI号段"，查询一个已经成功配置的"Configured NSSAI SUPI号段"的NSSAI获取策略。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。修改影响：该参数为此配置的主键，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。
confiSnssaiPolicy|Configured NSSAI 策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于配置某个SUPI号段获取Configured NSSAI的策略。本地配置(LOCALCONFIGURED): AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。签约(SUBSCRIPTION)：AMF下发给UE的Configured NSSAI是签约NSSAI。NSSF优先(NSSFPRIORITY)：如果UE在注册（Registration）过程中，AMF向NSSF成功获取过切片信息，则AMF下发给UE的Configured NSSAI是NSSF之前向AMF返回的Configured NSSAI。
命令举例 
`
查询SUPI号段"4601100"是否在"Configured SNSSAI Supi 号段配置"中，以及对应的获取策略。
SHOW CONFIG SNSSAI SUPI:SUPISEGMENT="4601100"
(No.3) : SHOW CONFIG SNSSAI SUPI:
-----------------Namf_Communication_0----------------
SUPI号段    Configured NSSAI 策略
4601100     本地配置
记录数：1
执行成功耗时: 0.12 秒
` 
### 基于PLMN和号段Configured SNSSAI列表配置 
### 基于PLMN和号段Configured SNSSAI列表配置 
背景知识 
AMF根据用户接入的PLMN和SUPI号段来配置S-NSSAI信息，具体地，就是为每个PLMN和SUPI号段配置相应的"S-NSSAI标识列表"，其中"S-NSSAI标识列表"是通过[ADD SUPI CONFIG SNSSAIID LIST]命令配置的。
功能说明 
本功能用于配置每个PLMN和SUPI号段对应的S-NSSAI列表。 
其中，S-NSSAI标识是通过[ADD CONFIGUREDSNSSAI]命令配置的。
子主题： 
#### 新增基于PLMN和号段Configured SNSSAI列表配置(ADD SEGPLMNCONFIGNSSAI) 
#### 新增基于PLMN和号段Configured SNSSAI列表配置(ADD SEGPLMNCONFIGNSSAI) 
功能说明 
本命令用于配置AMF支持根据用户的PLMN和用户的SUPI号段，这两个维度来获取用户对应Configured NSSAI。 
AMF支持同一个PLMN下，不同的SUPI号段的用户可以配置不的Configured NSSAI。 
注意事项 
当[SHOW PLMNSNSSAIPLY]命令中的参数"是否支持PLMN粒度切片策略配置"及"是否支持PLMN粒度Configured NSSAI"均设置为“是"时，此命令执行后，结果才会生效。
S-NSSAI列表中的每一个S-NSSAI必须已经通过[ADD CONFIGUREDSNSSAI]命令增加。
如果根据用户的PLMN和用户的SUPI号段，无法匹配到本命令配置的数据，即AMF无法根据用户的PLMN和用户的SUPI号段，获取到某个用户的NSSAI，则AMF会为用户分配默认NSSAI，默认的NSSAI的获取策略是通过[SET DEFAULT CONFIG SNSSAI POLICYI]命令和[ADD DEFAULT CONFIG SNSSAI ID]命令配置的。
每个号段下的每个PLMN配置的Configured NSSAI最多包含16个SNSSAI。 
本配置最多可以增加8192条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于将一个SUPI号段加入AMF的配置NSSAI规划信息中。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
configsnssaiid|Configured SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置根据用户的PLMN和用户的SUPI号段，这两个维度来获取用户对应的SNSSAI标识。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”, 必须已经通过ADD CONFIGUREDSNSSAI命令增加。每个号段下的每个PLMN配置的Configured NSSAI最多包含16个SNSSAI。
命令举例 
`
此命令用来为SUPI号段"46011012"，移动国家码"460"，移动网络码"02"的PLMN增加一个Configured S-NSSAI标识。S-NSSAI标识必须已经通过ADD CONFIGUREDSNSSAI命令添加过。
ADD SEGPLMNCONFIGNSSAI:SUPISEGMENT="46011012",MCC="460", MNC="02",CONFIGSNSSAIID=1
` 
#### 删除基于PLMN和号段Configured SNSSAI列表配置(DEL SEGPLMNCONFIGNSSAI) 
#### 删除基于PLMN和号段Configured SNSSAI列表配置(DEL SEGPLMNCONFIGNSSAI) 
功能说明 
该命令用于删除某号段下全部PLMN的Configured SNSSAI列表配置，或者删除某号段下某PLMN的全部Configured SNSSAI列表或者列表中的某个S-NSSAI。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于将一个SUPI号段加入AMF的配置NSSAI规划信息中。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
configsnssaiid|Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置根据用户的PLMN和用户的SUPI号段，这两个维度来获取用户对应的SNSSAI标识。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”, 必须已经通过ADD CONFIGUREDSNSSAI命令增加。每个号段下的每个PLMN配置的Configured NSSAI最多包含16个SNSSAI。
命令举例 
`
此命令用来删除一条SUPI号段为"46011012"，移动国家码为"460"，移动网络码为"02"，Configured SNSSAI标识为1的配置记录。
DEL SEGPLMNCONFIGNSSAI:SUPISEGMENT="46011012",MCC="460", MNC="02",CONFIGSNSSAIID=1
` 
#### 查询基于PLMN和号段Configured SNSSAI列表配置(SHOW SEGPLMNCONFIGNSSAI) 
#### 查询基于PLMN和号段Configured SNSSAI列表配置(SHOW SEGPLMNCONFIGNSSAI) 
功能说明 
该命令用于查询全部号段和PLMN的Configured SNSSAI列表配置，或者某个号段下全部PLMN的Configured SNSSAI列表配置，或者某个号段下某个PLMN的Configured SNSSAI列表配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于将一个SUPI号段加入AMF的配置NSSAI规划信息中。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
configsnssaiid|Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置根据用户的PLMN和用户的SUPI号段，这两个维度来获取用户对应的SNSSAI标识。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”, 必须已经通过ADD CONFIGUREDSNSSAI命令增加。每个号段下的每个PLMN配置的Configured NSSAI最多包含16个SNSSAI。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于将一个SUPI号段加入AMF的配置NSSAI规划信息中。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
configsnssaiid|Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置根据用户的PLMN和用户的SUPI号段，这两个维度来获取用户对应的SNSSAI标识。
命令举例 
`
此命令用来查询"46011012"号段关联的所有基于PLMN和号段Configured SNSSAI列表配置。
SHOW SEGPLMNCONFIGNSSAI:SUPISEGMENT="46011012":
(No.9) :SHOW SEGPLMNCONFIGNSSAI:SUPISEGMENT="46011012"
-----------------Namf_Communication_0----------------
SUPI号段      移动国家码      移动网络码      Configured SNSSAI标识        
46011012      460             02              1
记录数：1
执行成功耗时: 0.075 秒
` 
### 基于PLMN Configured SNSSAI列表配置 
### 基于PLMN Configured SNSSAI列表配置 
背景知识 
AMF根据用户接入的PLMN来配置S-NSSAI信息，具体地，就是为每个PLMN配置相应的"S-NSSAI标识列表"，其中"S-NSSAI标识列表"是通过[ADD SUPI CONFIG SNSSAIID LIST]命令配置的。
功能说明 
本功能用于配置每个PLMN对应的S-NSSAI列表。 
其中，S-NSSAI标识是通过[ADD CONFIGUREDSNSSAI]命令配置的。
子主题： 
#### 新增基于PLMN Configured SNSSAI列表配置(ADD PLMNCONFIGNSSAI) 
#### 新增基于PLMN Configured SNSSAI列表配置(ADD PLMNCONFIGNSSAI) 
功能说明 
该命令用于按用户当前服务PLMN增加Configured SNSSAI。 
注意事项 
当[SHOW PLMNSNSSAIPLY]命令中的参数"是否支持PLMN粒度切片策略配置"及"是否支持PLMN粒度Configured NSSAI"均设置为“是"时，此命令执行后，结果才会生效。
本命令中的需要配置的S-NSSAI列表中的每一个S-NSSAI必须已经通过[ADD CONFIGUREDSNSSAI]命令增加。
如果根据用户的PLMN，无法匹配到本命令配置的数据，即AMF无法根据用户的PLMN，获取到某个用户的Configured NSSAI，则AMF会为用户分配默认Configured NSSAI，默认的Configured NSSAI的获取策略是通过[SET DEFAULT CONFIG SNSSAI POLICY]命令和[ADD DEFAULT CONFIG SNSSAI ID]命令配置的。
每个PLMN配置的Configured NSSAI最多可以有16个SNSSAI。 
本配置最多可以增加4096条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
configsnssaiid|Configured SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于置此PLMN对应的S-NSSAI标识。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”, 必须已经通过ADD CONFIGUREDSNSSAI命令增加。每个PLMN最多可以关联16个S-NSSAI标识。
命令举例 
`
此命令用来增加一条移动国家码"460"，移动网络码"02"，Configured S-NSSAI标识为1的配置。S-NSSAI标识必须已经通过ADD CONFIGUREDSNSSAI命令增加过。
ADD PLMNCONFIGNSSAI:MCC="460",MNC="02",CONFIGSNSSAIID=1
` 
#### 删除基于PLMN Configured SNSSAI列表配置(DEL PLMNCONFIGNSSAI) 
#### 删除基于PLMN Configured SNSSAI列表配置(DEL PLMNCONFIGNSSAI) 
功能说明 
该命令用于删除某PLMN下全部Configured NSSAI列表或者列表中的某个S-NSSAI。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
configsnssaiid|Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于置此PLMN对应的S-NSSAI标识。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”, 必须已经通过ADD CONFIGUREDSNSSAI命令增加。每个PLMN最多可以关联16个S-NSSAI标识。
命令举例 
`
此命令用来删除一条移动国家码为"460"，移动网络码为"02"，Configured SNSSAI标识为1的配置记录。
DEL SEGPLMNCONFIGNSSAI:MCC="460",MNC="02",CONFIGSNSSAIID=1
` 
#### 查询基于PLMN Configured SNSSAI列表配置(SHOW PLMNCONFIGNSSAI) 
#### 查询基于PLMN Configured SNSSAI列表配置(SHOW PLMNCONFIGNSSAI) 
功能说明 
该命令用于查询全部基于PLMN Configured NSSAI配置记录，或者某个PLMN下的全部或者某个Configured SNSSAI。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
configsnssaiid|Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于置此PLMN对应的S-NSSAI标识。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”, 必须已经通过ADD CONFIGUREDSNSSAI命令增加。每个PLMN最多可以关联16个S-NSSAI标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
configsnssaiid|Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于置此PLMN对应的S-NSSAI标识。
命令举例 
`
此命令用来查询移动国家码为"460"，移动网络码为"02"关联的所有基于PLMN Configured SNSSAI列表配置。
SHOW PLMNCONFIGNSSAI:MCC="460",MNC="02":
(No.9) :SHOW PLMNCONFIGNSSAI:MCC="460",MNC="02"
-----------------Namf_Communication_0----------------
 移动国家码      移动网络码      Configured SNSSAI标识        
 460                 02                      1
记录数：1
执行成功耗时: 0.075 秒
` 
### 按号段Configured SNSSAI列表配置 
### 按号段Configured SNSSAI列表配置 
背景知识 
AMF根据SUPI号段来配置S-NSSAI信息，具体地，就是为每个SUPI号段配置相应的"S-NSSAI标识列表"和"获取策略"，其中"S-NSSAI标识列表"是通过[ADD SUPI CONFIG SNSSAIID LIST]命令配置的。
"获取策略"的详细说明如下： 
 
本地配置(LOCALCONFIGURED): AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。 
 
签约(SUBSCRIPTION)： AMF下发给UE的Configured NSSAI是签约NSSAI。 
 
NSSF优先(SYSTEMDEF)： 如果UE在注册(Registration)过程中，AMF向NSSF成功获取过切片信息，则AMF下发给Configured NSSAIo NSSF返回的Configured NSSAI。 
 
功能说明 
本功能用于配置每个SUPI号段对应的S-NSSAI列表。 
其中，SUPI号段是通过[ADD CONFIG SNSSAI SUPI]命令配置的，S-NSSAI标识是通过[ADD CONFIGUREDSNSSAI]命令配置的。
子主题： 
#### 新增Supi号段Configured SnssaiId List 配置(ADD SUPI CONFIG SNSSAIID LIST) 
#### 新增Supi号段Configured SnssaiId List 配置(ADD SUPI CONFIG SNSSAIID LIST) 
功能说明 
该命令用于为某个已经成功配置的"Configured NSSAI SUPI号段配置"增加关联的S-NSSAI列表。 
注意事项 
该命令执行后立即生效。 
本命令需要和如下命令配合使用： 
 
本命令配置的SUPI号段，是引用于ADD CONFIG SNSSAI SUPI命令中配置的参数“SUPISEGMENT”，必须预先通过ADD CONFIG SNSSAI SUPI命令配置。 
 
本命令的配置记录生效的前提，该SUPI号段在ADD CONFIG SNSSAI SUPI命令中的参数“CONFISNSSAIPOLICY”必须为"本地配置(LOCALCONFIGURED)"。 
 
本命令配置的SUPI号段对应的SNSSAI标识，是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”，必须预先通过ADD CONFIGUREDSNSSAI命令配置。 
 
每个SUPI号段最多可以配置16条记录，即关联16个Configured SNSSAI。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。修改影响：该参数为此配置的主键，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
supiConfigsnssaiId|Supi号段配置SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于为某个已经配置的SUPI号段增加关联的配置S-NSSAI标识。修改影响：修改此参数，会影响AMF给UE下发Configured NSSAI的策略。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”，必须预先通过ADD CONFIGUREDSNSSAI命令配置。每个SUPI号段最多可以关联16个S-NSSAI标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。
命令举例 
`
SUPI号段"46011012"已经成功加入配置NSSAI规划，此命令用来为"46011012"增加一个配置S-NSSAI标识。S-NSSAI标识必须已经通过ADD CONFIGUREDSNSSAI命令添加过。
ADD SUPI CONFIG SNSSAIID LIST:SUPISEGMENT="46011012",SUPICONFIGSNSSAIID=1
` 
#### 删除Supi号段Configured SnssaiId List 配置(DEL SUPI CONFIG SNSSAIID LIST) 
#### 删除Supi号段Configured SnssaiId List 配置(DEL SUPI CONFIG SNSSAIID LIST) 
功能说明 
该命令用于删除一个已经成功配置的"SUPI号段Configured Snssai 配置"，即删除某个"Configured NSSAI SUPI号段配置"关联的配置S-NSSAI列表中的一个标识。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。修改影响：该参数为此配置的主键，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
supiConfigsnssaiId|Supi号段配置SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于为某个已经配置的SUPI号段增加关联的配置S-NSSAI标识。修改影响：修改此参数，会影响AMF给UE下发Configured NSSAI的策略。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”，必须预先通过ADD CONFIGUREDSNSSAI命令配置。每个SUPI号段最多可以关联16个S-NSSAI标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。
命令举例 
`
SUPI号段"46011012"已经成功加入配置NSSAI规划。此命令用来删除"46011012"号段关联的一个配置S-NSSAI标识。S-NSSAI标识必须已经通过ADD SUPI CONFIG SNSSAIID LIST命令添加过。
DEL SUPI CONFIG SNSSAIID LIST:SUPISEGMENT="46011012",SUPICONFIGSNSSAIID=1
` 
#### 查询Supi号段Configured SnssaiId List 配置(SHOW SUPI CONFIG SNSSAIID LIST) 
#### 查询Supi号段Configured SnssaiId List 配置(SHOW SUPI CONFIG SNSSAIID LIST) 
功能说明 
该命令用于查询已经成功配置的"SUPI号段Configured Snssai 配置"。可以直接查询所有配置，也可以通过键入"SUPI号段"来查询某个指定SUPI(号段)的配置S-NSSAI列表。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。修改影响：该参数为此配置的主键，不允许修改。数据来源：本端规划。默认值：无。配置原则：无。
supiConfigsnssaiId|Supi号段配置SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于为某个已经配置的SUPI号段增加关联的配置S-NSSAI标识。修改影响：修改此参数，会影响AMF给UE下发Configured NSSAI的策略。数据来源：本端规划。默认值：无。配置原则：本参数的取值是引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAID”，必须预先通过ADD CONFIGUREDSNSSAI命令配置。每个SUPI号段最多可以关联16个S-NSSAI标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要获取Configured NSSAI分配策略的一个SUPI号段。
supiConfigsnssaiId|Supi号段配置SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于为某个已经配置的SUPI号段增加关联的配置S-NSSAI标识。
命令举例 
`
SUPI(号段)"460110123456789"已经成功加入配置NSSAI规划。此命令用来查询"46011012"号段已经关联配置过的所有配置S-NSSAI。
SHOW SUPI CONFIG SNSSAIID LIST:SUPISEGMENT="46011012":
(No.9) :SHOW SUPI CONFIG SNSSAIID LIST:SUPISEGMENT="46011012"
-----------------Namf_Communication_0----------------
SUPI号段      Supi号段配置SNSSAI标识
46011012      1
记录数：1
执行成功耗时: 0.075 秒
` 
### 默认Configured NSSAI 来源策略配置 
### 默认Configured NSSAI 来源策略配置 
背景知识 
AMF根据终端的SUPI号段配置对应的S-NSSAI，具体地，就是为每个SUPI号段配置相应的"S-NSSAI标识"和"获取策略"。 
其中，SUPI(号段)是通过[ADD CONFIG SNSSAI SUPI]命令配置的，S-NSSAI标识是通过[ADD CONFIGUREDSNSSAI]命令配置的。
另外，对于没有通过[ADD CONFIG SNSSAI SUPI]命令配置的其他SUPI号段，AMF提供一个默认的"获取策略"以及相应的默认的"S-NSSAI标识"。
默认的"获取策略"的详细说明如下： 
 
本地配置(LOCALCONFIGURED): AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。 
 
签约(SUBSCRIPTION)： AMF下发给UE的Configured NSSAI是签约NSSAI。 
 
NSSF优先(SYSTEMDEF)： 如果UE在注册(Registration)过程中，AMF向NSSF成功获取过切片信息，则AMF下发给Configured NSSAI为NSSF返回的Configured NSSAI。 
 
功能说明 
本功能用于为没有通过[ADD CONFIG SNSSAI SUPI]命令配置的其他SUPI号段, 提供一个默认的Configured NSSAI获取策略。
子主题： 
#### 修改默认Configured Snssai 策略配置(SET DEFAULT CONFIG SNSSAI POLICY) 
#### 修改默认Configured Snssai 策略配置(SET DEFAULT CONFIG SNSSAI POLICY) 
功能说明 
该命令用于设置Configured NSSAI的默认获取策略。 
注意事项 
该命令执行后立即生效。 
本命令需要和以下命令配合使用。 
 
当AMF根据用户的SUPI号码，无法匹配到ADD CONFIG SNSSAI SUPI命令配置的数据，即AMF无法获取到某个用户的NSSAI，则AMF会为用户分配默认NSSAI，默认的NSSAI的获取策略是通过本命令和ADD DEFAULT CONFIG SNSSAI ID命令配置的。 
 
当本命令的参数“DEFACONFISNSSAIPOLICY”配置为“本地配置(LOCALCONFIGURED)”时，本命令需要和ADD DEFAULT CONFIG SNSSAI ID命令共同确定一个默认Configured NSSAI，操作员后续需要通过ADD DEFAULT CONFIG SNSSAI ID命令配置默认的Configured NSSAI。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiPol|Configured NSSAI 默认策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于设置Configured NSSAI的缺省获取策略，当AMF根据用户的SUPI号码，无法匹配到ADD CONFIG SNSSAI SUPI命令配置的数据，即AMF无法获取到某个用户的NSSAI，则AMF会使用本命令配置的默认策略为用户分配默认NSSAI。修改影响：修改此参数可能影响AMF带给UE的ConfiguredNSSAI。数据来源：本端规划。默认值：无。配置原则：包括三个取值：本地配置(LOCALCONFIGURED)： AMF下发给UE的Configured NSSAI是通过本命令配置的SUPI号段对应的S-NSSAI和签约NSSAI的交集。签约(SUBSCRIPTION)： AMF下发给UE的Configured NSSAI是签约NSSAI。NSSF优先(NSSFPRIORITY)： 如果UE在注册(Registration)过程中，AMF向NSSF成功获取过切片信息，则AMF下发给UE从NSSF返回的Configured NSSAI。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiPol|Configured NSSAI 默认策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于设置Configured NSSAI的缺省获取策略，当AMF根据用户的SUPI号码，无法匹配到ADD CONFIG SNSSAI SUPI命令配置的数据，即AMF无法获取到某个用户的NSSAI，则AMF会使用本命令配置的默认策略为用户分配默认NSSAI。
命令举例 
`
将Configured NSSAI的默认获取策略设置为"本地配置(LOCALCONFIGURED)"。
SET DEFAULT CONFIG SNSSAI POLICY:DEFACONFISNSSAIPOL="LOCALCONFIGURED"
` 
#### 查询默认Configured Snssai 策略配置(SHOW DEFAULT CONFIG SNSSAI POLICY) 
#### 查询默认Configured Snssai 策略配置(SHOW DEFAULT CONFIG SNSSAI POLICY) 
功能说明 
该命令用于查询Configured NSSAI的默认获取策略。 
注意事项 
该命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiPol|Configured NSSAI 默认策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SUBSCRIPTION|参数作用：该参数用于设置Configured NSSAI的缺省获取策略，当AMF根据用户的SUPI号码，无法匹配到ADD CONFIG SNSSAI SUPI命令配置的数据，即AMF无法获取到某个用户的NSSAI，则AMF会使用本命令配置的默认策略为用户分配默认NSSAI。
命令举例 
`
查询Configured NSSAI的默认获取策略。
SHOW DEFAULT CONFIG SNSSAI POLICY:
(No.1) : SHOW DEFAULT CONFIG SNSSAI POLICY:
-----------------Namf_Communication_0----------------
Configured NSSAI 默认策略
签约
记录数：1
执行成功耗时: 0.259 秒
` 
### 默认Configured SNSSAI列表配置 
### 默认Configured SNSSAI列表配置 
背景知识 
AMF根据终端的SUPI号段配置对应的S-NSSAI，具体地，就是为每个SUPI号段配置相应的"S-NSSAI标识"和"获取策略"。 
其中，SUPI(号段)是通过[ADD CONFIG SNSSAI SUPI]命令配置的，S-NSSAI标识是通过[ADD CONFIGUREDSNSSAI]命令配置的。
另外，对于没有通过[ADD CONFIG SNSSAI SUPI]命令配置的其他SUPI号段，AMF提供一个默认的"获取策略"以及相应的默认的"S-NSSAI标识"。
功能说明 
本功能用于设置Configured NSSAI的默认S-NSSAI。 
子主题： 
#### 增加默认Configured Snssai Id 配置(ADD DEFAULT CONFIG SNSSAI ID) 
#### 增加默认Configured Snssai Id 配置(ADD DEFAULT CONFIG SNSSAI ID) 
功能说明 
该命令用于为默认Configured NSSAI配置关联的S-NSSAI列表。 
注意事项 
该命令执行后立即生效。 
在配置本命令之前， 需要先通过[ADD CONFIGUREDSNSSAI]命令配置Configured SNSSAI标识，本命令配置的每一个默认Configured SNSSAI标识，都是通过[ADD CONFIGUREDSNSSAI]命令增加的。
最多可以输入16条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiId|默认 Configured SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535默认值: 1|参数作用：该参数用于为默认Configured SNSSAI配置关联的S-NSSAI标识，修改影响：此参数不可修改，如需修改，需先删除，再增加。数据来源：本端规划。默认值：无。配置原则：最多可配置16个，本参数的取值引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAIID”，必须先通过ADD CONFIGUREDSNSSAI命令预先配置。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiId|默认 Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1|参数作用：该参数用于为默认Configured SNSSAI配置关联的S-NSSAI标识，
命令举例 
`
此命令用来为默认Configured NSSAI配置增加一个关联S-NSSAI标识1。S-NSSAI标识必须已经通过ADD CONFIGUREDSNSSAI命令添加过。
ADD DEFAULT CONFIG SNSSAI ID:DEFACONFISNSSAIID=1
` 
#### 删除默认Configured Snssai Id 配置(DEL DEFAULT CONFIG SNSSAI ID) 
#### 删除默认Configured Snssai Id 配置(DEL DEFAULT CONFIG SNSSAI ID) 
功能说明 
该命令用于删除一个已经成功配置的默认Configured S-NSSAI"，即删除默认Configured NSSAI关联的S-NSSAI。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiId|默认 Configured SNSSAI标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535默认值: 1|参数作用：该参数用于为默认Configured SNSSAI配置关联的S-NSSAI标识，修改影响：此参数不可修改，如需修改，需先删除，再增加。数据来源：本端规划。默认值：无。配置原则：最多可配置16个，本参数的取值引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAIID”，必须先通过ADD CONFIGUREDSNSSAI命令预先配置。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiId|默认 Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1|参数作用：该参数用于为默认Configured SNSSAI配置关联的S-NSSAI标识，
命令举例 
`
此命令用来删除默认Configured NSSAI配置已经关联的一个S-NSSAI标识1。
DEL DEFAULT CONFIG SNSSAI ID:DEFACONFISNSSAIID=1
` 
#### 查询默认Configured Snssai Id 配置(SHOW DEFAULT CONFIG SNSSAI ID) 
#### 查询默认Configured Snssai Id 配置(SHOW DEFAULT CONFIG SNSSAI ID) 
功能说明 
该命令用于查询默认Configured NSSAI关联的所有S-NSSAI。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiId|默认 Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1|参数作用：该参数用于为默认Configured SNSSAI配置关联的S-NSSAI标识，修改影响：此参数不可修改，如需修改，需先删除，再增加。数据来源：本端规划。默认值：无。配置原则：最多可配置16个，本参数的取值引用于ADD CONFIGUREDSNSSAI命令配置的参数“SNSSAIID”，必须先通过ADD CONFIGUREDSNSSAI命令预先配置。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
defaConfiSnssaiId|默认 Configured SNSSAI标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 1|参数作用：该参数用于为默认Configured SNSSAI配置关联的S-NSSAI标识，
命令举例 
`
此命令用来查询默认Configured NSSAI配置已经关联过的所有配置S-NSSAI标识。
SHOW DEFAULT CONFIG SNSSAI ID
(No.3) : SHOW DEFAULT CONFIG SNSSAI ID:
-----------------Namf_Communication_0----------------
默认 Configured SNSSAI标识
10001
记录数：1
执行成功耗时: 0.12 秒
` 
## NSSAI Profile 配置 
## NSSAI Profile 配置 
背景知识 
网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟逻辑的端到端网络，每个网络切片在逻辑上隔离，适配各种类型服务的不同特征需求,同时满足高带宽、低时延、超大连接以及多业务支持。 
S-NSSAI（Single Network Slice Selection Assistance information，单个网络切片选择辅助信息）用于标识一个网络切片，可以是一个标准值或PLMN-specific 相关的值。NSSAI为一组S-NSSAI的集合，由一个或多个S-NSSAI组成。 
功能说明 
配置NSSAI Profile，每个NSSAI Profile包含一个或多个S-NSSAI。 
子主题： 
### 新增NSSAI Profile配置(ADD NSSAI PROFILE) 
### 新增NSSAI Profile配置(ADD NSSAI PROFILE) 
功能说明 
该命令用于在NSSAI Profile中增加一个S-NSSAI。 
注意事项 
该命令执行后立即生效。 
NSSAI Profile标识、SST和SD为关键字。对于某个指定S-NSSAI，可以仅配置SST，也可以同时配置SST和SD。 
如果需要配置的S-NSSAI没有SD，则本命令中的参数“SD”配置为“NULL”。 
本命令配置的参数“PROFILEID”后续会被[ADD SEGSLISUPTPCFPOLICY]命令中的参数“NSSAIPROFILEID”关联使用。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
profileId|NSSAI Profile标识|参数可选性: 必选参数类型: 数字参数范围: 0-2048|参数作用：本参数用于配置NSSAI Profile的标识，用于表示一个S-NSSAI。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个NSSAI Profile标识可以对应多个S-NSSAI，当NSSAI Profile标识为0时，标志着该NSSAI Profile不生效。本参数“PROFILEID”后续会被ADD SEGSLISUPTPCFPOLICY命令关联使用，即ADD SEGSLISUPTPCFPOLICY命令中配置的参数“NSSAIPROFILEID”取值引用于本参数配置的值。
sst|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。修改影响：无。数据来源：本端规划。默认值：无。配置原则目前协议明确的标准SST有三种：eMBB：提供高带宽、大数据量的服务。uRLLC：提供超高可靠低时延服务。mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。
sd|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
命令举例 
`
在NSSAI Profile中新增标识为1的S-NSSAI，SST为"eMBB"，SD为"1234AB。
ADD NSSAI PROFILE:PROFILEID=1,SST="eMBB",SD="1234AB"
` 
### 删除NSSAI Profile配置(DEL NSSAI PROFILE) 
### 删除NSSAI Profile配置(DEL NSSAI PROFILE) 
功能说明 
该命令用于通过一个已经成功配置的NSSAI Profile标识、SST和SD，删除对应的S-NSSAI。 
注意事项 
该命令执行后立即生效。 
如果参数“PROFILEID”已经被[ADD SEGSLISUPTPCFPOLICY]命令关联使用，则无法通过本命令删除，需要先通过[DEL SEGSLISUPTPCFPOLICY]命令删除关联配置后，再通过本命令进行删除。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
profileId|NSSAI Profile标识|参数可选性: 必选参数类型: 数字参数范围: 0-2048|参数作用：本参数用于配置NSSAI Profile的标识，用于表示一个S-NSSAI。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个NSSAI Profile标识可以对应多个S-NSSAI，当NSSAI Profile标识为0时，标志着该NSSAI Profile不生效。本参数“PROFILEID”后续会被ADD SEGSLISUPTPCFPOLICY命令关联使用，即ADD SEGSLISUPTPCFPOLICY命令中配置的参数“NSSAIPROFILEID”取值引用于本参数配置的值。
sst|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。修改影响：无。数据来源：本端规划。默认值：无。配置原则目前协议明确的标准SST有三种：eMBB：提供高带宽、大数据量的服务。uRLLC：提供超高可靠低时延服务。mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。
sd|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
命令举例 
`
在NSSAI Profile中删除标识为1，SST为"eMBB"，SD为"1234AB的S-NSSAI。
DEL NSSAI PROFILE:PROFILEID=1,SST="eMBB",SD="1234AB"
` 
### 查询NSSAI Profile配置(SHOW NSSAI PROFILE) 
### 查询NSSAI Profile配置(SHOW NSSAI PROFILE) 
功能说明 
该命令用于查询NSSAI Profile中所有配置的S-NSSAI的详细信息。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
profileId|NSSAI Profile标识|参数可选性: 任选参数类型: 数字参数范围: 0-2048|参数作用：本参数用于配置NSSAI Profile的标识，用于表示一个S-NSSAI。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个NSSAI Profile标识可以对应多个S-NSSAI，当NSSAI Profile标识为0时，标志着该NSSAI Profile不生效。本参数“PROFILEID”后续会被ADD SEGSLISUPTPCFPOLICY命令关联使用，即ADD SEGSLISUPTPCFPOLICY命令中配置的参数“NSSAIPROFILEID”取值引用于本参数配置的值。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
profileId|NSSAI Profile标识|参数可选性: 任选参数类型: 数字参数范围: 0-2048|参数作用：本参数用于配置NSSAI Profile的标识，用于表示一个S-NSSAI。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
命令举例 
`
查询NSSAI Profile中所有配置的S-NSSAI。
SHOW NSSAI PROFILE:
(No.8) : SHOW NSSAI PROFILE:
--------------------------------
NSSAI Profile标识    SST     SD
1                   eMBB    ABCDEF
2048                255     NULL
记录数：2
执行成功耗时: 0.411 秒
` 
## 网络切片实例配置 
## 网络切片实例配置 
背景知识 
网络切片（Network Slice）可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的逻辑的端到端网络，每个网络切片在逻辑上隔离，适配各种类型服务的不同特征需求。 
NSI（Network Slice instance，网络切片实例）是指一组网络功能实例和需要的资源（比如：计算、存储和网络资源）形成了一个部署的网络切片。同一类型的网络切片可以有多个切片实例NSI，同一NSI也可以支持多种网络切片类型。 
功能说明 
本功能用于配置AMF所归属的NSI（Network Slice instance，网络切片实例）。如果一个AMF被多个NSI共享，需要配置多个NSI。 
当AMF部署成功之后或AMF归属的NSI信息发生变化时，需要涉及到此功能的配置。 
子主题： 
### 新增AMF NSI配置(ADD NSIID) 
### 新增AMF NSI配置(ADD NSIID) 
功能说明 
该命令用于配置AMF所归属的NSI（Network Slice instance，网络切片实例）。 
当AMF部署成功或AMF被其他NSI（Network Slice instance，网络切片实例）共享时，需要使用此命令。  
注意事项 
该命令执行后立即生效。 
一个AMF只支持配置最多20个NSI（Network Slice instance，网络切片实例）。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
nsiid|网络切片实例|参数可选性: 必选参数类型: 字符串参数范围: 0-128|参数作用：网络切片实例，是一个端到端的逻辑网络，通常包含接入网、承载网、核心网，也可以包含第三方应用。本参数用于设置AMF归属的网络切片实例号（Network Slice Instance），由运营商统一编号。修改影响：删除掉AMF归属的切片实例信息后，无法再基于该切片实例号进行性能统计。数据来源：本端规划。默认值：无。配置原则：一个AMF可以归属多个切片实例。
nssiid|子切片|参数可选性: 必选参数类型: 字符串参数范围: 0-128|参数作用：网络子切片实例，是一个端到端的逻辑网络，通常包含接入网、承载网、核心网，也可以包含第三方应用。本参数用于设置AMF归属于哪个网络切片实例（Network Slice Instance）下的子切片（Sub Network Slice Instance），由运营商统一编号。修改影响：删除或修改AMF归属的切片下的子切片信息后，无法再基于该切片下的子切片实例号进行性能统计。数据来源：本端规划。默认值：无。配置原则：一个AMF可以归属多个切片实例，但是在一个切片实例下只能归属于某个特定的子切片。
命令举例 
`
新增AMF所归属的网络切片实例，其实例号为1。
 ADD NSIID:NSIID="1",NSSIID="1"
` 
### 删除AMF NSI配置(DEL NSIID) 
### 删除AMF NSI配置(DEL NSIID) 
功能说明 
该命令用于删除AMF所属的NSI（Network Slice instance，网络切片实例）。 
当网络规划发生变更，AMF不再归属某个NSI（Network Slice instance，网络切片实例）时，可以使用此命令删除AMF所属的NSI（Network Slice instance，网络切片实例）。 
注意事项 
该命令执行后立即生效。 
操作员不能修改AMF归属的NSI（Network Slice instance，网络切片实例），只能先通过本命令删除AMF所属的NSI（Network Slice instance，网络切片实例），再通过[ADD NSIID]命令增加。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
nsiid|网络切片实例|参数可选性: 必选参数类型: 字符串参数范围: 0-128|参数作用：网络切片实例，是一个端到端的逻辑网络，通常包含接入网、承载网、核心网，也可以包含第三方应用。本参数用于设置AMF归属的网络切片实例号（Network Slice Instance），由运营商统一编号。修改影响：删除掉AMF归属的切片实例信息后，无法再基于该切片实例号进行性能统计。数据来源：本端规划。默认值：无。配置原则：一个AMF可以归属多个切片实例。
nssiid|子切片|参数可选性: 必选参数类型: 字符串参数范围: 0-128|参数作用：网络子切片实例，是一个端到端的逻辑网络，通常包含接入网、承载网、核心网，也可以包含第三方应用。本参数用于设置AMF归属于哪个网络切片实例（Network Slice Instance）下的子切片（Sub Network Slice Instance），由运营商统一编号。修改影响：删除或修改AMF归属的切片下的子切片信息后，无法再基于该切片下的子切片实例号进行性能统计。数据来源：本端规划。默认值：无。配置原则：一个AMF可以归属多个切片实例，但是在一个切片实例下只能归属于某个特定的子切片。
命令举例 
`
删除AMF所归属的网络切片实例，其实例号为1。
DEL NSIID:NSIID="1",NSSIID="1"
` 
### 查询AMF NSI配置(SHOW NSIID) 
### 查询AMF NSI配置(SHOW NSIID) 
功能说明 
该命令用于查询AMF所归属的NSI（Network Slice instance，网络切片实例）。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
nsiid|网络切片实例|参数可选性: 任选参数类型: 字符串参数范围: 0-128|参数作用：网络切片实例，是一个端到端的逻辑网络，通常包含接入网、承载网、核心网，也可以包含第三方应用。本参数用于设置AMF归属的网络切片实例号（Network Slice Instance），由运营商统一编号。修改影响：删除掉AMF归属的切片实例信息后，无法再基于该切片实例号进行性能统计。数据来源：本端规划。默认值：无。配置原则：一个AMF可以归属多个切片实例。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
nsiid|网络切片实例|参数可选性: 任选参数类型: 字符串参数范围: 0-128|参数作用：网络切片实例，是一个端到端的逻辑网络，通常包含接入网、承载网、核心网，也可以包含第三方应用。本参数用于设置AMF归属的网络切片实例号（Network Slice Instance），由运营商统一编号。
nssiid|子切片|参数可选性: 任选参数类型: 字符串参数范围: 0-128|参数作用：网络子切片实例，是一个端到端的逻辑网络，通常包含接入网、承载网、核心网，也可以包含第三方应用。本参数用于设置AMF归属于哪个网络切片实例（Network Slice Instance）下的子切片（Sub Network Slice Instance），由运营商统一编号。
命令举例 
`
查询AMF所归属的网络切片实例。
SHOW NSIID:
No.3) : SHOW NSIID:
-----------------Namf_Communication_0----------------
网络切片实例    子切片
1                    1
记录数：1
执行成功耗时: 0.22 秒
` 
## NSSAI inclusion mode配置 
## NSSAI inclusion mode配置 
背景知识 
NSSAI Inclusion mode用于指示UE在初始注册、移动性注册更新、周期性注册更新、业务请求流程中，是否需要在RRC层携带NSSAI信息。 
功能说明 
NSSAI inclusion mode配置可以配置基于SUPI号段的NSSAI inclusion mode策略和缺省NSSAI inclusion mode策略。 
该功能需License项“AMF支持NSSAI inclusion mode功能”为“打开”才可以使用 
子主题： 
### 基于PLMN和号段NSSAI inclusion mode策略配置 
### 基于PLMN和号段NSSAI inclusion mode策略配置 
背景知识 
NSSAI inclusion mode用于AMF指示UE，在以下四个流程中，是否需要在RRC层携带NSSAI信息。 
 
初始注册流程 
 
移动性注册更新流程 
 
周期性注册更新流程 
 
业务请求流程 
 
功能说明 
该命令用于新增基于PLMN和SUPI两个维度来控制的NSSAI inclusion mode策略，包括如下内容。 
 
AMF支持基于PLMN和SUPI两个维度，来决定对哪些UE进行NSSAI inclusion mode策略控制。 
 
在AMF发送给UE的Registration Accept消息中，是否携带NSSAI Inclusion mode。 
 
AMF发送给UE的Registration Accept消息中的NSSAI Inclusion mode的取值。 
 
子主题： 
#### 新增基于PLMN和号段NSSAI inclusion mode策略配置(ADD PLMNSUPI NIM POLICY) 
#### 新增基于PLMN和号段NSSAI inclusion mode策略配置(ADD PLMNSUPI NIM POLICY) 
功能说明 
该命令用于新增基于PLMN和SUPI两个维度来控制的NSSAI inclusion mode策略，包括如下内容。 
 
AMF支持基于PLMN和SUPI两个维度，来决定对哪些UE进行NSSAI inclusion mode策略控制。 
 
在AMF发送给UE的Registration Accept消息中，是否携带NSSAI Inclusion mode。 
 
AMF发送给UE的Registration Accept消息中的NSSAI Inclusion mode的取值。 
 
注意事项 
该命令执行后，结果立即生效。 
该功能需License项“AMF支持NSSAI inclusion mode功能”为“打开”才可以使用。 
用户的SUPI号段和PLMN，这两个参数共同决定UE的范围。 
最多可以增加65535条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要执行NSSAI inclusion mode策略控制的用户的SUPI号段。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：每位必须配置为‘0’-‘9’的数字。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
ifcarrynssaiincmode|是否携带NSSAI Inclusion mode|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置在AMF发送给UE的Registration Accept消息中，是否携带NSSAI Inclusion mode。修改影响：更改SUPI和PLMN下的NSSAI Inclusion mode下发策略。数据来源：本端规划。默认值：否。配置原则：该参数包括如下取值：是：Registration Accept消息中携带NSSAI Inclusion mode。否：Registration Accept消息中不携带NSSAI Inclusion mode。
nssaiincmode|NSSAI Inclusion mode|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：该参数用于配置NSSAI inclusion mode的具体取值。该参数只有在"是否携带NSSAI inclusion mode"参数指示为"是"时才有效，用于AMF告知UE，后续哪些流程需要UE上传切片信息。修改影响：更改下发给UE的NSSAI Inclusion mode参数取值。数据来源：本端规划。默认值：NSSAI inclusion mode A。配置原则：该参数包括如下取值。NSSAI inclusion mode ANSSAI inclusion mode BNSSAI inclusion mode CNSSAI inclusion mode D
命令举例 
`
增加一条基于PLMN和号段NSSAI inclusion mode策略配置：SUPI号段为“460111”，MCC为“460”，MNC为“111”，携带NSSAI inclusion mode，并且NSSAI inclusion mode设置为NSSAI inclusion mode A。即当UE号段最大左匹配到460111号段，PLMN匹配460111，则Registration Accept消息携带NSSAI inclusion Mode，携带值为“NSSAI inclusion mode A”。
ADD PLMNSUPI NIM POLICY:SUPISEGMENT="460111",MCC="460",MNC="111",IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_A"
` 
#### 修改基于PLMN和号段NSSAI inclusion mode策略配置(SET PLMNSUPI NIM POLICY) 
#### 修改基于PLMN和号段NSSAI inclusion mode策略配置(SET PLMNSUPI NIM POLICY) 
功能说明 
该命令用于修改基于PLMN和SUPI两个维度来控制的NSSAI inclusion mode策略。 
注意事项 
该命令执行后，结果立即生效。 
通过该命令修改SUPI号段在该PLMN下的NSSAI Inclusion mode策略配置，设置是否携带NSSAI Inclusion mode字段、NSSAI Inclusion mode字段参数。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要执行NSSAI inclusion mode策略控制的用户的SUPI号段。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：每位必须配置为‘0’-‘9’的数字。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
ifcarrynssaiincmode|是否携带NSSAI Inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置在AMF发送给UE的Registration Accept消息中，是否携带NSSAI Inclusion mode。修改影响：更改SUPI和PLMN下的NSSAI Inclusion mode下发策略。数据来源：本端规划。默认值：否。配置原则：该参数包括如下取值：是：Registration Accept消息中携带NSSAI Inclusion mode。否：Registration Accept消息中不携带NSSAI Inclusion mode。
nssaiincmode|NSSAI Inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：该参数用于配置NSSAI inclusion mode的具体取值。该参数只有在"是否携带NSSAI inclusion mode"参数指示为"是"时才有效，用于AMF告知UE，后续哪些流程需要UE上传切片信息。修改影响：更改下发给UE的NSSAI Inclusion mode参数取值。数据来源：本端规划。默认值：NSSAI inclusion mode A。配置原则：该参数包括如下取值。NSSAI inclusion mode ANSSAI inclusion mode BNSSAI inclusion mode CNSSAI inclusion mode D
命令举例 
`
修改一条基于PLMN和号段NSSAI inclusion mode策略配置：将SUPI号段为“460111”，MCC为“460”，MNC为“111”的IFCARRYNSSAIINCMODE修改为YES，NSSAI inclusion mode修改为NSSAI inclusion mode B
SET PLMNSUPI NIM POLICY:SUPISEGMENT="460111",MCC="460",MNC="111",IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_B"
` 
#### 删除基于PLMN和号段NSSAI inclusion mode策略配置(DEL PLMNSUPI NIM POLICY) 
#### 删除基于PLMN和号段NSSAI inclusion mode策略配置(DEL PLMNSUPI NIM POLICY) 
功能说明 
该命令用于删除基于PLMN和SUPI两个维度来控制的NSSAI inclusion mode策略。 
注意事项 
该命令执行后，结果立即生效。 
可以通过SUPI和PLMN删除一条记录，也可以通过单一SUPI参数删除对应号段下的所有PLMN记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要执行NSSAI inclusion mode策略控制的用户的SUPI号段。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：每位必须配置为‘0’-‘9’的数字。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
命令举例 
`
删除SUPI号段为460111，MCC为“460”，MNC为“111”的配置记录
DEL PLMNSUPI NIM POLICY:SUPISEGMENT="460111",MCC="460",MNC="111"
` 
#### 查询基于PLMN和号段NSSAI inclusion mode策略配置(SHOW PLMNSUPI NIM POLICY) 
#### 查询基于PLMN和号段NSSAI inclusion mode策略配置(SHOW PLMNSUPI NIM POLICY) 
功能说明 
该命令用于查询基于PLMN和SUPI两个维度来控制的NSSAI inclusion mode策略。 
注意事项 
该命令执行后，结果立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要执行NSSAI inclusion mode策略控制的用户的SUPI号段。修改影响：该参数为配置关键字，不允许修改。数据来源：本端规划。默认值：无。配置原则：每位必须配置为‘0’-‘9’的数字。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supisegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：该参数用于配置需要执行NSSAI inclusion mode策略控制的用户的SUPI号段。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
ifcarrynssaiincmode|是否携带NSSAI Inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置在AMF发送给UE的Registration Accept消息中，是否携带NSSAI Inclusion mode。
nssaiincmode|NSSAI Inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：该参数用于配置NSSAI inclusion mode的具体取值。该参数只有在"是否携带NSSAI inclusion mode"参数指示为"是"时才有效，用于AMF告知UE，后续哪些流程需要UE上传切片信息。
命令举例 
`
查询基于SUPI和PLMN的NSSAI inclusion mode策略的所有配置记录
SHOW PLMNSUPI NIM POLICY
-----------------Namf_Communication_0----------------
操作维护       SUPI号段 移动国家码 移动网络码 是否携带NSSAI Inclusion mode NSSAI Inclusion mode   
-----------------------------------------------------------------------------------------------
复制 修改 删除 46011    460        11         否                           NSSAI inclusion mode B 
-----------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-12-09 10:43:39 耗时: 0.159 秒
` 
### 基于PLMN NSSAI inclusion mode策略配置 
### 基于PLMN NSSAI inclusion mode策略配置 
背景知识 
NSSAI inclusion mode用于AMF指示UE，在以下四个流程中，是否需要在RRC层携带NSSAI信息。
 
初始注册流程 
 
移动性注册更新流程 
 
周期性注册更新流程 
 
业务请求流程 
 
功能说明 
该命令用于新增基于PLMN控制的NSSAI inclusion mode策略，包括如下内容。 
 
AMF支持基于PLMN，来决定对哪些UE进行NSSAI inclusion mode策略控制。 
 
在AMF发送给UE的Registration Accept消息中，是否携带NSSAI Inclusion mode。 
 
AMF发送给UE的Registration Accept消息中的NSSAI Inclusion mode的取值。 
 
子主题： 
#### 新增基于PLMN NSSAI inclusion mode策略配置(ADD PLMN NIM POLICY) 
#### 新增基于PLMN NSSAI inclusion mode策略配置(ADD PLMN NIM POLICY) 
功能说明 
该命令用于新增NSSAI inclusion mode策略，包括如下内容。 
 
AMF支持基于PLMN，来决定对哪些UE进行NSSAI inclusion mode策略控制。 
 
在AMF发送给UE的Registration Accept消息中，是否携带NSSAI Inclusion mode。 
 
AMF发送给UE的Registration Accept消息中的NSSAI Inclusion mode的取值。 
 
注意事项 
该命令执行后，结果立即生效。 
最多可以增加256条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
ifcarrynssaiincmode|是否携带NSSAI Inclusion mode|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数标识AMF是否携带NSSAI Inclusion mode信息下发给UE。修改影响：更改SUPI和PLMN下的NSSAI Inclusion mode下发策略。数据来源：本端规划。默认值：否。配置原则：该参数包括如下取值：是：Registration Accept消息中携带NSSAI Inclusion mode。否：Registration Accept消息中不携带NSSAI Inclusion mode。
nssaiincmode|NSSAI Inclusion mode|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：该参数标识NSSAI inclusion mode的具体取值。该参数只有在"是否携带NSSAI inclusion mode"参数指示为"是"时才有效。用于告知UE后续哪些流程需要UE上传切片信息。修改影响：更改下发给UE的NSSAI Inclusion mode参数取值。数据来源：本端规划。默认值：NSSAI inclusion mode A。配置原则：该参数包括如下取值：NSSAI inclusion mode ANSSAI inclusion mode BNSSAI inclusion mode CNSSAI inclusion mode D
命令举例 
`
增加一条基于PLMN NSSAI inclusion mode策略配置：MCC为“460”，MNC为“111”，携带NSSAI inclusion mode，并且NSSAI inclusion mode设置为NSSAI inclusion mode A。即PLMN匹配460111，则Registration Accept消息携带NSSAI inclusion Mode，携带值为“NSSAI inclusion mode A”。
ADD PLMN NIM POLICY:MCC="460",MNC="111",IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_A"
` 
#### 修改基于PLMN NSSAI inclusion mode策略配置(SET PLMN NIM POLICY) 
#### 修改基于PLMN NSSAI inclusion mode策略配置(SET PLMN NIM POLICY) 
功能说明 
该命令用于修改基于PLMN NSSAI inclusion mode策略。 
注意事项 
该命令执行后，结果立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
ifcarrynssaiincmode|是否携带NSSAI Inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数标识AMF是否携带NSSAI Inclusion mode信息下发给UE。修改影响：更改SUPI和PLMN下的NSSAI Inclusion mode下发策略。数据来源：本端规划。默认值：否。配置原则：该参数包括如下取值：是：Registration Accept消息中携带NSSAI Inclusion mode。否：Registration Accept消息中不携带NSSAI Inclusion mode。
nssaiincmode|NSSAI Inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：该参数标识NSSAI inclusion mode的具体取值。该参数只有在"是否携带NSSAI inclusion mode"参数指示为"是"时才有效。用于告知UE后续哪些流程需要UE上传切片信息。修改影响：更改下发给UE的NSSAI Inclusion mode参数取值。数据来源：本端规划。默认值：NSSAI inclusion mode A。配置原则：该参数包括如下取值：NSSAI inclusion mode ANSSAI inclusion mode BNSSAI inclusion mode CNSSAI inclusion mode D
命令举例 
`
修改一条基于PLMN inclusion mode策略配置：MCC为“460”，MNC为“111”的IFCARRYNSSAIINCMODE修改为YES，NSSAI inclusion mode修改为NSSAI inclusion mode B
SET PLMN NIM POLICY:MCC="460",MNC="111",IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_B"
` 
#### 删除基于PLMN NSSAI inclusion mode策略配置(DEL PLMN NIM POLICY) 
#### 删除基于PLMN NSSAI inclusion mode策略配置(DEL PLMN NIM POLICY) 
功能说明 
该命令用于删除基于PLMN NSSAI inclusion mode策略配置。 
注意事项 
该命令执行后，结果立即生效。 
可以通过PLMN删除一条策略或多条策略。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
命令举例 
`
删除MCC为“460”，MNC为“111”的配置记录
DEL PLMN NIM POLICY:MCC="460",MNC="111"
` 
#### 查询基于PLMN NSSAI inclusion mode策略配置(SHOW PLMN NIM POLICY) 
#### 查询基于PLMN NSSAI inclusion mode策略配置(SHOW PLMN NIM POLICY) 
功能说明 
该命令用于查询基于PLMN NSSAI inclusion mode策略配置。 
注意事项 
该命令执行后，结果立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
ifcarrynssaiincmode|是否携带NSSAI Inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数标识AMF是否携带NSSAI Inclusion mode信息给UE。
nssaiincmode|NSSAI Inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：该参数标识NSSAI inclusion mode的具体取值。该参数只有在"是否携带NSSAI inclusion mode"参数指示为"是"时才有效
命令举例 
`
查询基于PLMN的NSSAI inclusion mode策略的所有配置记录
SHOW PLMN NIM POLICY
-----------------Namf_Communication_0----------------
操作维护       移动国家码 移动网络码 是否携带NSSAI Inclusion mode NSSAI Inclusion mode   
--------------------------------------------------------------------------------------
复制 修改 删除 460        11         是                           NSSAI inclusion mode A 
--------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-12-09 11:55:32 耗时: 0.16 秒
` 
### 基于号段NSSAI inclusion mode策略配置 
### 基于号段NSSAI inclusion mode策略配置 
背景知识 
NSSAI inclusion mode用于指示UE在初始注册、移动性注册更新、周期性注册更新、业务请求流程中，是否需要在RRC层携带NSSAI信息。 
功能说明 
按号段NSSAI inclusion mode策略配置，可以设置是否需要携带NSSAI inclusion mode的开关，以及在需要携带NSSAI inclusion mode时，设置NSSAI inclusion mode的具体值。 
子主题： 
#### 新增基于SUPI号段NSSAI inclusion mode策略配置(ADD SUPI NIM POLICY) 
#### 新增基于SUPI号段NSSAI inclusion mode策略配置(ADD SUPI NIM POLICY) 
功能说明 
该命令用于新增基于SUPI号段NSSAI inclusion mode策略配置。按号段NSSAI inclusion mode策略配置，可以设置是否需要携带NSSAI Inclusion mode的开关，以及在需要携带NSSAI Inclusion mode时，设置NSSAI Inclusion mode的具体值。 
注意事项 
该命令执行后立即生效。 
本命令和[SET DEFAULT NIM POLICY]命令是共同配合使用的。
AMF首先根据用户的SUPI号码查询本命令的配置结果，并且根据号段最长匹配原则进行匹配。比如存在46001和4600123两个号段的配置数据时，对于用户46001234567890，AMF会匹配到4600123号段的配置数据。如果通过本命令匹配不到对应的数据时，会使用[SET DEFAULT NIM POLICY]命令的配置数据对用户进行下一步处理。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：本参数用于设置需要使用NSSAI inclusion mode控制策略的用户的SUPI号段。修改影响：修改此参数，会修改使用NSSAI inclusion mode控制策略的用户号段。数据来源：本端规划。默认值：无。配置原则：无。
IFCARRYNSSAIINCMODE|是否携带NSSAI inclusion mode|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于配置AMF是否携带NSSAI inclusion mode信息给UE。修改影响：修改此参数，可以更改NSSAI inclusion mode信息的携带策略。数据来源：本端规划。默认值：不携带。配置原则：无。
NSSAIINCMODE|NSSAI inclusion mode|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：本参数用于配置NSSAI inclusion mode的具体取值。修改影响：修改此参数，可以更改NSSAI inclusion mode的取值。数据来源：本端配置。默认值：NSSAI inclusion mode A。配置原则：该参数只有在"是否携带NSSAI inclusion mode"参数配置为"是"时，取值才有效。
命令举例 
`
增加一条基于SUPI号段NSSAI inclusion mode策略配置记录：SUPI号段为"460111"；携带NSSAI inclusion mode，携带的mode是“NSSAI inclusion mode A”。当UE号段最大左匹配到460111号段，在Registration Accept消息携带NSSAI inclusion Mode，携带的值为“NSSAI inclusion mode A”。
ADD SUPI NIM POLICY:SUPISEGMENT="460111",IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_A"
` 
#### 修改基于SUPI号段NSSAI inclusion mode策略配置(SET SUPI NIM POLICY) 
#### 修改基于SUPI号段NSSAI inclusion mode策略配置(SET SUPI NIM POLICY) 
功能说明 
该命令用于修改基于SUPI号段NSSAI inclusion mode策略配置。 
注意事项 
该命令执行后立即生效。 
本命令和[SET DEFAULT NIM POLICY]命令是共同配合使用的。
AMF首先根据用户的SUPI号码查询本命令的配置结果，并且根据号段最长匹配原则进行匹配。比如存在46001和4600123两个号段的配置数据时，对于用户46001234567890，AMF会匹配到4600123号段的配置数据。如果通过本命令匹配不到对应的数据时，会使用[SET DEFAULT NIM POLICY]命令的配置数据对用户进行下一步处理。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：本参数用于设置需要使用NSSAI inclusion mode控制策略的用户的SUPI号段。修改影响：修改此参数，会修改使用NSSAI inclusion mode控制策略的用户号段。数据来源：本端规划。默认值：无。配置原则：无。
IFCARRYNSSAIINCMODE|是否携带NSSAI inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于配置AMF是否携带NSSAI inclusion mode信息给UE。修改影响：修改此参数，可以更改NSSAI inclusion mode信息的携带策略。数据来源：本端规划。默认值：不携带。配置原则：无。
NSSAIINCMODE|NSSAI inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：本参数用于配置NSSAI inclusion mode的具体取值。修改影响：修改此参数，可以更改NSSAI inclusion mode的取值。数据来源：本端配置。默认值：NSSAI inclusion mode A。配置原则：该参数只有在"是否携带NSSAI inclusion mode"参数配置为"是"时，取值才有效。
命令举例 
`
修改ADD命令中增加的配置记录。即：将SUPI号段为"460111"的NSSAI inclusion mode修改为"NSSAI inclusion mode B"。
SET SUPI NIM POLICY:SUPISEGMENT="460111",IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_B"
` 
#### 删除基于SUPI号段NSSAI inclusion mode策略配置(DEL SUPI NIM POLICY) 
#### 删除基于SUPI号段NSSAI inclusion mode策略配置(DEL SUPI NIM POLICY) 
功能说明 
该命令用于删除基于SUPI号段NSSAI inclusion mode策略配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|参数作用：本参数用于设置需要使用NSSAI inclusion mode控制策略的用户的SUPI号段。修改影响：修改此参数，会修改使用NSSAI inclusion mode控制策略的用户号段。数据来源：本端规划。默认值：无。配置原则：无。
命令举例 
`
删除ADD命令中增加的配置记录。即：将SUPI号段为"460111"的配置记录删除。
DEL SUPI NIM POLICY:SUPISEGMENT="460111"
` 
#### 查询基于SUPI号段NSSAI inclusion mode策略配置(SHOW SUPI NIM POLICY) 
#### 查询基于SUPI号段NSSAI inclusion mode策略配置(SHOW SUPI NIM POLICY) 
功能说明 
该命令用于查询基于SUPI号段NSSAI inclusion mode策略配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|参数作用：本参数用于设置需要使用NSSAI inclusion mode控制策略的用户的SUPI号段。修改影响：修改此参数，会修改使用NSSAI inclusion mode控制策略的用户号段。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|该参数用于显示需要控制的用户的SUPI号段。
IFCARRYNSSAIINCMODE|是否携带NSSAI inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于显示AMF是否携带NSSAI inclusion mode信息给UE。
NSSAIINCMODE|NSSAI inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|该参数用于显示NSSAI inclusion mode的具体取值。该参数只有在"是否携带NSSAI inclusion mode"参数指示为"是"时才有效。
命令举例 
`
查询基于SUPI号段NSSAI inclusion mode策略的所有配置记录。
SHOW SUPI NIM POLICY:
(No.6) : SHOW SUPI NIM POLICY:
-----------------Namf_Communication_0----------------
SUPI号段    是否携带NSSAI inclusion mode     NSSAI inclusion mode
4601100012           是                     NSSAI inclusion mode A
记录数：1
执行成功耗时: 0.221 秒
` 
### 缺省NSSAI inclusion mode策略配置 
### 缺省NSSAI inclusion mode策略配置 
背景知识 
NSSAI inclusion mode用于指示UE在初始注册、移动性注册更新、周期性注册更新、业务请求流程中，是否需要在RRC层携带NSSAI信息。 
功能说明 
缺省NSSAI inclusion mode策略配置，可以设置是否需要携带NSSAI inclusion mode的开关，以及在需要携带NSSAI inclusion mode时，设置NSSAI inclusion mode的具体值。 
子主题： 
#### 修改缺省NSSAI inclusion mode策略配置(SET DEFAULT NIM POLICY) 
#### 修改缺省NSSAI inclusion mode策略配置(SET DEFAULT NIM POLICY) 
功能说明 
该命令用于修改缺省NSSAI inclusion mode策略配置。AMF在下发Registration Accept消息时，使用用户的SUPI在“基于SUPI号段NSSAI inclusion mode策略配置”中不能找到相关的配置记录时，使用该命令配置的NSSAI inclusion mode策略决策是否携带NSSAI inclusion mode。 
注意事项 
该命令执行后立即生效。 
本命令的配置结果受[ADD SUPI NIM POLICY]命令的影响，当AMF根据用户的SUPI号码查询[ADD SUPI NIM POLICY]命令的配置结果，匹配不到对应的数据时，才会使用本命令的配置数据对用户进行处理。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
IFCARRYNSSAIINCMODE|是否携带NSSAI inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于配置AMF是否携带NSSAI inclusion mode信息给UE。修改影响：修改此参数，可以更改NSSAI inclusion mode信息的携带策略。数据来源：本端规划。默认值：不携带。配置原则：无。
NSSAIINCMODE|NSSAI inclusion Mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：本参数用于标识NSSAI inclusion mode的具体取值。修改影响：修改此参数，可以更改NSSAI inclusion mode的取值。数据来源：本端规划。默认值：NSSAI inclusion mode A。配置原则：该参数只有在"是否携带NSSAI inclusion mode"参数配置为"是"时，取值才有效。
命令举例 
`
修改缺省NSSAI inclusion mode策略配置记录。即：携带NSSAI inclusion Mode，并将NSSAI inclusion Mode设置为"NSSAI inclusion mode B"。
SET DEFAULT NIM POLICY:IFCARRYNSSAIINCMODE="YES",NSSAIINCMODE="NSSAIINCLUMODE_B"
` 
#### 查询缺省NSSAI inclusion mode策略配置(SHOW DEFAULT NIM POLICY) 
#### 查询缺省NSSAI inclusion mode策略配置(SHOW DEFAULT NIM POLICY) 
功能说明 
该命令用于查询缺省NSSAI inclusion mode策略配置。 
注意事项 
该命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IFCARRYNSSAIINCMODE|是否携带NSSAI inclusion mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于配置AMF是否携带NSSAI inclusion mode信息给UE。
NSSAIINCMODE|NSSAI inclusion Mode|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: NSSAIINCLUMODE_A|参数作用：本参数用于标识NSSAI inclusion mode的具体取值。
命令举例 
`
查询缺省NSSAI inclusion mode策略配置记录。
SHOW DEFAULT NIM POLICY
(No.3) : SHOW DEFAULT NIM POLICY:
-----------------Namf_Communication_0_A----------------
是否携带NSSAI inclusion mode    NSSAI inclusion Mode
            否                 NSSAI inclusion mode A
记录数：1
执行成功耗时: 0.506 秒
` 
## 切片可用性配置 
## 切片可用性配置 
背景知识 
网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的逻辑的端到端网络，每个网络切片在逻辑上隔离，适配各种类型服务的不同特征需求,同时满足高带宽、低时延、超大连接以及多业务支持。 
网络切片可用性指网络切片可以在整个PLMN有效，也可以仅在一个或多个TA下有效。 
TA下有效性信息包括特定TA下支持哪些切片，以及哪些切片对漫游用户的额外限制。 
功能说明 
切片可用性配置可以配置切片可用性策略、TA下RestrictedSnssai、RestrictedSnssai模板配置。 
子主题： 
### 切片可用性策略配置 
### 切片可用性策略配置 
背景知识 
网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的逻辑的端到端网络，每个网络切片在逻辑上隔离，适配各种类型服务的不同特征需求，同时满足高带宽、低时延、超大连接以及多业务支持。 
网络切片可用性指网络切片可以在整个PLMN有效，也可以仅在一个或多个TA下有效。 
TA下有效性信息包括特定TA下支持哪些切片，以及哪些切片对漫游用户的额外限制。 
功能说明 
本功能用于设置切片可用性策略。 
子主题： 
#### 设置切片可用性策略(SET 5GSLICEAVAILPLY) 
#### 设置切片可用性策略(SET 5GSLICEAVAILPLY) 
功能说明 
本命令用于设置切片可用性策略，包括如下策略。 
 
AMF支持切片可用性功能。 
 
AMF向NSSF同步TA下supportedSnssaiList。 
 
AMF向NSSF订阅切片可用性信息变更。 
 
NSSF可用性订阅信息到期时长。 
 
AMF使用切片可用性信息策略。 
 
AMF向NSSF同步切片可用性信息间隔时长。(单位: 秒) 
 
等待NSSF切片可用性响应消息时长。(单位: 秒) 
 
等待NSSF切片可用性响应消息超时后重试间隔。(单位: 秒) 
 
支持ONSSAI 
 
更新请求中是否使用tacRangeList 
 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ifsliceavail|AMF支持切片可用性功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数是AMF是否支持切片可用性功能的功能开关。
ifupdtasprtslice|AMF向NSSF同步TA下supportedSnssaiList|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数标识AMF是否向NSSF同步RAN提供的TA下supportedSnssaiList信息。功能开关"AMF支持切片可用性功能"设置为"是"时才有效。
ifsubsliceavail|AMF向NSSF订阅切片可用性信息变更|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数标识AMF是否向NSSF订阅切片可用性信息变更。功能开关"AMF支持切片可用性功能"设置为"是"时才有效。
expirytime|AMF向NSSF订阅切片可用性的有效时长(单位: 秒)|参数可选性: 任选参数类型: 数字参数范围: 0-16777215默认值: 0|该参数用于设置AMF向NSSF订阅切片可用性的有效时长。单位为秒。
useavailply|AMF使用切片可用性信息策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: USENSSFPRI|该参数用于设置AMF使用切片可用性信息策略。
delayupdnssf|AMF向NSSF同步切片可用性信息间隔时长(单位: 秒)|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 30|该参数用于设置AMF向NSSF同步切片可用性信息间隔时长。(单位: 秒)
nssfslicersptime|等待NSSF切片可用性响应消息时长(单位: 秒)|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 60|该参数用于设置等待NSSF切片可用性响应消息时长。(单位: 秒)
reattempttime|等待NSSF切片可用性响应消息超时后重试间隔(单位: 秒)|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 120|该参数用于设置等待NSSF切片可用性响应消息超时后重试间隔。(单位: 秒)
ifonssai|支持ONSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置AMF是否支持ONSSAI功能。修改影响：如果配置为支持，AMF和NSSF之间的切片可用性功能相关的接口消息，可以使用taiList和taiRangeList字段。数据来源：本端规划。默认值：否。配置原则：无。
iftacrangeupdmsg|更新请求中是否使用tacRangeList|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数标识AMF在向NSSF发送Update Request消息时，是否使用tacRangeList字段。修改影响：如果配置为支持，AMF向NSSF发送Update Request消息时，会把支持相同切片的TAC相邻的TA，填充到tacRangeList字段。数据来源：本端规划。默认值：否。配置原则：在参数“支持ONSSAI”设置为“支持”时，本参数才有效，只能在控制在Update Request消息中是否使用tacRangeList字段。
命令举例 
`
设置切片可用性策略：支持切片可用性功能，支持AMF向NSSF同步TA下supportedSnssaiList, 支持AMF向NSSF订阅切片可用性信息变更，AMF向NSSF订阅切片可用性的有效时长为3600s，支持ONSSAI，更新请求中使用tacRangeList。
SET 5GSLICEAVAILPLY:IFSLICEAVAIL="YES",IFUPDTASPRTSLICE="YES",IFSUBSLICEAVAIL="YES",EXPIRYTIME=3600,IFONSSAI="YES",IFTACRANGEUPDMSG="YES"
` 
#### 查询切片可用性策略(SHOW 5GSLICEAVAILPLY) 
#### 查询切片可用性策略(SHOW 5GSLICEAVAILPLY) 
功能说明 
本命令用于查询切片可用性策略配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ifsliceavail|AMF支持切片可用性功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数是AMF是否支持切片可用性功能的功能开关。
ifupdtasprtslice|AMF向NSSF同步TA下supportedSnssaiList|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数标识AMF是否向NSSF同步RAN提供的TA下supportedSnssaiList信息。功能开关"AMF支持切片可用性功能"设置为"是"时才有效。
ifsubsliceavail|AMF向NSSF订阅切片可用性信息变更|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数标识AMF是否向NSSF订阅切片可用性信息变更。功能开关"AMF支持切片可用性功能"设置为"是"时才有效。
expirytime|AMF向NSSF订阅切片可用性的有效时长(单位: 秒)|参数可选性: 任选参数类型: 数字参数范围: 0-16777215默认值: 0|该参数用于设置AMF向NSSF订阅切片可用性的有效时长。单位为秒。
useavailply|AMF使用切片可用性信息策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: USENSSFPRI|该参数用于设置AMF使用切片可用性信息策略。
delayupdnssf|AMF向NSSF同步切片可用性信息间隔时长(单位: 秒)|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 30|该参数用于设置AMF向NSSF同步切片可用性信息间隔时长。(单位: 秒)
nssfslicersptime|等待NSSF切片可用性响应消息时长(单位: 秒)|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 60|该参数用于设置等待NSSF切片可用性响应消息时长。(单位: 秒)
reattempttime|等待NSSF切片可用性响应消息超时后重试间隔(单位: 秒)|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 120|该参数用于设置等待NSSF切片可用性响应消息超时后重试间隔。(单位: 秒)
ifonssai|支持ONSSAI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置AMF是否支持ONSSAI功能。
iftacrangeupdmsg|更新请求中是否使用tacRangeList|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数标识AMF在向NSSF发送Update Request消息时，是否使用tacRangeList字段。
命令举例 
`
查询切片可用性策略配置。
SHOW 5GSLICEAVAILPLY
(No.2) : SHOW 5GSLICEAVAILPLY:
-----------------Namf_Communication_0----------------
AMF支持切片可用性功能   AMF向NSSF同步TA下supportedSnssaiList   AMF向NSSF订阅切片可用性信息变更   AMF向NSSF订阅切片可用性的有效时长   支持ONSSAI   更新请求中是否使用tacRangeList  
1                       1                       1                   3600                       1                       1                       
记录数：1
执行成功耗时: 0.277 秒
` 
### RestrictedSnssai模板配置 
### RestrictedSnssai模板配置 
背景知识 
网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的逻辑的端到端网络，每个网络切片在逻辑上隔离，适配各种类型服务的不同特征需求,同时满足高带宽、低时延、超大连接以及多业务支持。 
网络切片可用性指网络切片可以在整个PLMN有效，也可以仅在一个或多个TA下有效。 
TA下有效性信息包括特定TA下支持哪些切片，以及哪些切片对漫游用户的额外限制。 
功能说明 
本功能用于配置RestrictedSnssai模板，该模板关联一组对漫游用户限制使用的切片，其中，每个切片可以是如下两种类型之一： 
 
对特定PLMN的漫游用户限制使用的切片 。 
 
对所有的漫游用户都限制使用的切片。 
 
子主题： 
#### 增加RestrictedSnssai模板配置(ADD RSTRNSSAI) 
#### 增加RestrictedSnssai模板配置(ADD RSTRNSSAI) 
功能说明 
该命令用于增加RestrictedSnssai模板配置。 
注意事项 
该命令执行后立即生效。 
参数“PROFILEID”、“S-NSSAI(SST+SD）”、“PLMN(MCC+MNC）”是此命令的组合关键字，唯一确定一条配置记录。 
参数“PROFILEID”为非唯一索引，因此，同一个PROFILEID下，可以配置多条记录。 
本命令配置的参数“PROFILEID”后续会被[ADD 5GTARSTRNSSAI]命令引用。
最多可以增加1024条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
profileid|RestrictedSnssai模板标识|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置一组S-NSSAI的模板标识 ，就是一组S-NSSAI与它可以使用的漫游用户的PLMN之间的对应关系。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：本标识为非唯一索引，即同一标识可以关联多个上述对应关系的配置。
sst|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。 默认值：无。配置原则：无。
sd|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：SD需配置为"NULL"或者长度为6且每一位均为'0'-'9' 或者 'A'-'F' 的字符串。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
roamrestr|漫游限制标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置SST+SD对应的S-NSSAI，是否对所有漫游用户都限制使用。修改影响：修改该参数，影响本配置记录中的S-NSSAI是否对所有漫游用户都限制使用的决策。数据来源：本端规划。默认值：否。配置原则：漫游限制标识配置为“0（否）”时，标识不是对所有漫游用户都限制使用对应的S-NSSAI，而仅限制配置的PLMN对应的用户限制使用对应的S-NSSAI。MCC和MNC不可以同时配置为“FFF”，在实际配置中，由于“FFF”对于MCC和MNC都是无效的，因此，其中一个配置为“FFF”的情况也不允许出现。漫游标限制标识配置为“1（是）”时，标识对所有漫游用户都限制使用对应的S-NSSAI，MCC和MNC必须同时配置为“0xFFF”。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 1-30|该参数用于设置RestrictedSnssai模板标识的别名。修改影响：本参数仅为RestrictedSnssai模板的别名，修改无影响。数据来源：本端规划。默认值：无。配置原则：根据实际情况进行修改。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
profileid|RestrictedSnssai模板标识|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置一组S-NSSAI的模板标识 ，就是一组S-NSSAI与它可以使用的漫游用户的PLMN之间的对应关系。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置漫游用户的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置漫游用户的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。
roamrestr|漫游限制标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置SST+SD对应的S-NSSAI，是否对所有漫游用户都限制使用。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 1-30|该参数用于设置RestrictedSnssai模板标识的别名。
命令举例 
`
增加一条RestrictedSnssai模板配置，其中RestrictedSnssai模板标识为1，SST为"1-eMBB", SD为"123456"，移动国家码为"460"， 移动网络码为"01", 漫游限制标识为"NO"即不限制，别名为"RestrictedSnssai ProfileId 001"。
ADD RSTRNSSAI:PROFILEID=1,SST="eMBB",SD="123456",MCC="460",MNC="01",ROAMRESTR="NO",ALIAS="RestrictedSnssai ProfileId 001"
` 
#### 删除RestrictedSnssai模板配置(DEL RSTRNSSAI) 
#### 删除RestrictedSnssai模板配置(DEL RSTRNSSAI) 
功能说明 
该命令用于删除一条RestrictedSnssai模板配置。 
注意事项 
该命令执行后立即生效。 
参数“PROFILEID”、“S-NSSAI(SST+SD）”、“PLMN(MCC+MNC）”是此此命令的组合关键字，如果需要删除一条指定的配置记录，需要正确输入"PROFILEID+SST+SD+MCC+MNC"。 
当参数“PROFILEID”被[ADD 5GTARSTRNSSAI]命令引用时，不能被删除。必须先通过[DEL 5GTARSTRNSSAI]命令删除关联关系后，才可以使用本命令进行删除。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
profileid|RestrictedSnssai模板标识|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置一组S-NSSAI的模板标识 ，就是一组S-NSSAI与它可以使用的漫游用户的PLMN之间的对应关系。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：本标识为非唯一索引，即同一标识可以关联多个上述对应关系的配置。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。 默认值：无。配置原则：无。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：SD需配置为"NULL"或者长度为6且每一位均为'0'-'9' 或者 'A'-'F' 的字符串。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：整网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
profileid|RestrictedSnssai模板标识|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置一组S-NSSAI的模板标识 ，就是一组S-NSSAI与它可以使用的漫游用户的PLMN之间的对应关系。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置漫游用户的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置漫游用户的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。
roamrestr|漫游限制标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置SST+SD对应的S-NSSAI，是否对所有漫游用户都限制使用。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 1-30|该参数用于设置RestrictedSnssai模板标识的别名。
命令举例 
`
删除一条RestrictedSnssai模板标识为1，SST为"1-eMBB", SD为"123456"，移动国家码为"460"， 移动网络码为"01"的RestrictedSnssai模板配置。
DEL RSTRNSSAI:PROFILEID=1,SST="1-eMBB",SD="123456",MCC="460",MNC="01"
` 
#### 查询RestrictedSnssai模板配置(SHOW RSTRNSSAI) 
#### 查询RestrictedSnssai模板配置(SHOW RSTRNSSAI) 
功能说明 
该命令用于查询RestrictedSnssai模板配置。可以查询特定配置，也可以查询所有配置。 
注意事项 
该命令执行后立即生效。 
参数“PROFILEID”、“S-NSSAI(SST+SD）”、“PLMN(MCC+MNC）”是此此命令的组合关键字，如果需要查询一条指定的配置记录，需要正确输入"PROFILEID+SST+SD+MCC+MNC"。
不输入任何参数，表示查询所有的配置记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
profileid|RestrictedSnssai模板标识|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置一组S-NSSAI的模板标识 ，就是一组S-NSSAI与它可以使用的漫游用户的PLMN之间的对应关系。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：本标识为非唯一索引，即同一标识可以关联多个上述对应关系的配置。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
profileid|RestrictedSnssai模板标识|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置一组S-NSSAI的模板标识 ，就是一组S-NSSAI与它可以使用的漫游用户的PLMN之间的对应关系。
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6|参数作用：该参数用于配置S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息）的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置漫游用户的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置漫游用户的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。
roamrestr|漫游限制标识|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置SST+SD对应的S-NSSAI，是否对所有漫游用户都限制使用。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 1-30|该参数用于设置RestrictedSnssai模板标识的别名。
命令举例 
`
查询RestrictedSnssai模板配置。
SHOW RSTRNSSAI:PROFILEID=1
(No.2) : SHOW RSTRNSSAI:PROFILEID=1
-----------------Namf_Communication_0_A----------------
操作维护       RestrictedSnssai模板标识 SST    SD     移动国家码 移动网络码 漫游限制标识 别名                           
------------------------------------------------------------------------------------------------------------------------
复制  删除      1                        1-eMBB 123456 460        01         否           RestrictedSnssai ProfileId 001 
------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-09-21 11:49:16 耗时: 0.142 秒
执行成功耗时: 0.277 秒
` 
### TA下RestrictedSnssai配置 
### TA下RestrictedSnssai配置 
背景知识 
网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的逻辑的端到端网络，每个网络切片在逻辑上隔离，适配各种类型服务的不同特征需求,同时满足高带宽、低时延、超大连接以及多业务支持。 
网络切片可用性指网络切片可以对整个PLMN的用户生效，也可以仅对在一个或多个TA下的用户生效。 
功能说明 
本功用于设置TA范围内对漫游用户限制使用的切片集合。 
TA范围与漫游用户限制切片的对应关系，是通过将"跟踪区组配置（[ADD TAGROUPCFG]命令）"中的参数"跟踪区组类型（tagrptype）"为"切片可用性（SLICEAVAILABILITY）"的某个"跟踪区组标识（taGroupId）"与 "RestrictedSnssai模板配置（[ADD RSTRNSSAI]命令）"中的"RestrictedSnssai模板标识（profileid）"关联来实现的。
本功能仅针对漫游用户生效。 
子主题： 
#### 增加TA下RestrictedSnssai配置(ADD 5GTARSTRNSSAI) 
#### 增加TA下RestrictedSnssai配置(ADD 5GTARSTRNSSAI) 
功能说明 
该命令用于配置TA的切片限制列表，即增加TA与“S-NSSAI+PLMN"的关联关系。具体地，是建立"跟踪区组号"和"限制切片信息Profile ID"的关联。 
"跟踪区组号"引用自MP配置子模型下的"跟踪区组配置"。该跟踪区组号必须已经存在，可通过"查询跟踪区组配置"命令查询已存在的跟踪区组标识， 并且，被关联的“跟踪区组标识”对应的“跟踪区组类型”必须为“4：切片可用性"。 
"限制切片信息Profile ID"引用自"RestrictedSnssai模板配置"。该模板标识必须已经存在，可通过[SHOW RSTRNSSAI]命令查询已存在的RestrictedSnssai模板。
注意事项 
该命令执行后立即生效。 
配置此命令前，需要确认操作员已经通过Namf_MP_0组件中[ADD TAGROUPCFG]命令配置了AMF管理的所有跟踪区组，并且已经通过Namf_MP_0组件中的[SHOW TAGROUPCFG]命令获取当前的所有跟踪区组的“TAGROUPID”。
配置此命令前，需要确认操作员已经通过[ADD RSTRNSSAI]命令配置了RestrictedSnssai模板标识，并且已经通过[SHOW RSTRNSSAI]命令获取了当前配置的所有RestrictedSnssai模板标识。
参数"跟踪区组号（TAGRPID）"为本命令的关键字，即每个跟踪区组号，只可以配置一条记录。 
"限制切片信息Profile ID（RSTRNSSAI）"是非唯一索引，即同一个模板标识可以与不同的"跟踪区组号（TAGRPID）"建立关联关系。 
最多可以配置1024条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
tagrpid|跟踪区组号|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于设置跟踪区组标识，实际代表的是跟踪区组标识对应的一组TA。修改影响：本参数为配置的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须先通过ADD TAGROUPCFG命令预先配置。“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。被关联的 "跟踪区组标识" 所配置的 "跟踪区组类型" 仅可以是 "4：切片可用性"，否则禁止被引用。
rstrnssai|限制切片信息Profile ID|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置 "跟踪区组号"标识的每个TA下所关联RestrictedSnssai模板标识，此模板标识代表的是一组S-NSSAI+PLMN。修改影响：修改本参数，会影响本TA组关联的所有TA需要限制的切片。数据来源：本端规划。默认值：无。配置原则：本参数的取值引于ADD RSTRNSSAI命令配置的参数“PROFILEID”，必须已经增加过，可使用SHOW RSTRNSSAI命令查询。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置置某个"TA下RestrictedSnssai配置"的别名。修改影响：本参数仅为TA下RestrictedSnssai配置的别名，修改无影响。数据来源：本端规划。默认值：无。配置原则：根据实际情况进行配置。
命令举例 
`
增加一条TA下RestrictedSnssai配置，其中tagrpid为1，rstrnssai为1，别名为"taresrictnssai001"。
ADD 5GTARSTRNSSAI:TAGRPID=1,RSTRNSSAI=1,ALIAS="taresrictnssai001"
` 
#### 修改TA下RestrictedSnssai配置(SET 5GTARSTRNSSAI) 
#### 修改TA下RestrictedSnssai配置(SET 5GTARSTRNSSAI) 
功能说明 
该命令用于修改已经建立的TA与“S-NSSAI+PLMN"的关联关系。具体地，即修改"跟踪区组号"和"限制切片信息Profile ID"的关联。 
"限制切片信息Profile ID"引用自"RestrictedSnssai模板配置"。该模板标识必须已经存在，可通过[SHOW RSTRNSSAI]命令查询已存在的RestrictedSnssai模板。
注意事项 
该命令执行后立即生效。 
参数"跟踪区组号（TAGRPID）"为本命令的关键字，因此修改"跟踪区组号（TAGRPID）"和"限制切片信息Profile ID（RSTRNSSAI）"的关联关系，仅指修改跟踪区组号所关联的"限制切片信息Profile ID（RSTRNSSAI）"。即表示只能修改"限制切片信息Profile ID（RSTRNSSAI）"，不能修改"跟踪区组号（TAGRPID）"。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
tagrpid|跟踪区组号|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于设置跟踪区组标识，实际代表的是跟踪区组标识对应的一组TA。修改影响：本参数为配置的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须先通过ADD TAGROUPCFG命令预先配置。“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。被关联的 "跟踪区组标识" 所配置的 "跟踪区组类型" 仅可以是 "4：切片可用性"，否则禁止被引用。
rstrnssai|限制切片信息Profile ID|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置 "跟踪区组号"标识的每个TA下所关联RestrictedSnssai模板标识，此模板标识代表的是一组S-NSSAI+PLMN。修改影响：修改本参数，会影响本TA组关联的所有TA需要限制的切片。数据来源：本端规划。默认值：无。配置原则：本参数的取值引于ADD RSTRNSSAI命令配置的参数“PROFILEID”，必须已经增加过，可使用SHOW RSTRNSSAI命令查询。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置置某个"TA下RestrictedSnssai配置"的别名。修改影响：本参数仅为TA下RestrictedSnssai配置的别名，修改无影响。数据来源：本端规划。默认值：无。配置原则：根据实际情况进行配置。
命令举例 
`
修改tagrpid为1的TA下RestrictedSnssai配置，rstrnssai修改为2，别名修改为"taresrictnssai002"。
SET 5GTARSTRNSSAI:TAGRPID=1,RSTRNSSAI=2, ALIAS="taresrictnssai002"
` 
#### 删除TA下RestrictedSnssai配置(DEL 5GTARSTRNSSAI) 
#### 删除TA下RestrictedSnssai配置(DEL 5GTARSTRNSSAI) 
功能说明 
该命令用于删除已经建立的TA与“S-NSSAI+PLMN"的关联关系。具体地，即删除一对"跟踪区组号"和"限制切片信息Profile ID"的关联。 
注意事项 
该命令执行后立即生效。 
删除全部配置记录，会导致AMF无法处理配置变更，不能给后续业务使用，因此，此配置仅支持使用关键字"跟踪区组号（TAGRPID）"逐条删除，不能一次性全部删除。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
tagrpid|跟踪区组号|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于设置跟踪区组标识，实际代表的是跟踪区组标识对应的一组TA。修改影响：本参数为配置的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须先通过ADD TAGROUPCFG命令预先配置。“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。被关联的 "跟踪区组标识" 所配置的 "跟踪区组类型" 仅可以是 "4：切片可用性"，否则禁止被引用。
命令举例 
`
删除tagrpid为1的TA下RestrictedSnssai配置。
DEL 5GTARSTRNSSAI:TAGRPID=1
` 
#### 查询TA下RestrictedSnssai配置(SHOW 5GTARSTRNSSAI) 
#### 查询TA下RestrictedSnssai配置(SHOW 5GTARSTRNSSAI) 
功能说明 
该命令用于查询已经建立的TA与“S-NSSAI+PLMN"的关联关系。 
可以查询全部已配置的"TA下切片限制列表”,也可以通过键入配置关键字"跟踪区组号"来查询特定跟踪区组号的切片限制列表，即跟踪区组号关联的"限制切片信息Profile ID"。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
tagrpid|跟踪区组号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于设置跟踪区组标识，实际代表的是跟踪区组标识对应的一组TA。修改影响：本参数为配置的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须先通过ADD TAGROUPCFG命令预先配置。“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。被关联的 "跟踪区组标识" 所配置的 "跟踪区组类型" 仅可以是 "4：切片可用性"，否则禁止被引用。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
tagrpid|跟踪区组号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于设置跟踪区组标识，实际代表的是跟踪区组标识对应的一组TA。
rstrnssai|限制切片信息Profile ID|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置 "跟踪区组号"标识的每个TA下所关联RestrictedSnssai 模板标识，此模板标识代表的是一组S-NSSAI+PLMN。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于设置置某个"TA下RestrictedSnssai配置"的别名。
命令举例 
`
查询tagrpid为1的TA下RestrictedSnssai配置。
SHOW 5GTARSTRNSSAI:TAGRPID=1
(No.9) : SHOW 5GTARSTRNSSAI:TAGRPID=1
-----------------Namf_Communication_0_A----------------
操作维护       跟踪区组号 限制切片信息Profile ID 别名              
-------------------------------------------------------------------
复制 修改 删除 1          1                      taresrictnssai002 
-------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-09-21 14:17:34 耗时: 0.129 秒
` 
### 基于SUPI号段的RestrictedSnssai配置 
### 基于SUPI号段的RestrictedSnssai配置 
背景知识 
网络切片可以让运营商在同一套硬件基础设施上按需切分出多个虚拟的逻辑的端到端网络，每个网络切片在逻辑上隔离，适配各种类型服务的不同特征需求,同时满足高带宽、低时延、超大连接以及多业务支持。 
基于SUPI号段的网络切片用于配置特定号段的漫游用户所限制使用的切片。 
功能说明 
本功能用于配置当启用基于PLMN维度的切片功能时，特定SUPI号段的漫游用户所限制使用的切片。 
AMF支持限制不同用户使用不同的切片，便于运营商灵活规划切片。 
本功能仅针对漫游用户有效。 
子主题： 
#### 新增基于SUPI号段的RestrictedSnssai配置(ADD 5GSUPIRSTRNSSAI) 
#### 新增基于SUPI号段的RestrictedSnssai配置(ADD 5GSUPIRSTRNSSAI) 
功能说明 
该命令用于新增基于SUPI号段的RestrictedSnssai配置。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置限制切片访问的用户SUPI号段。修改影响：运营商可根据需求设置限制切片访问的SUPI号段。数据来源：本端规划 默认值：无 配置原则：无
sst|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于设置SST（Slice/Service Type，切片/服务类型）。修改影响：运营商可根据需求设置限制的切片/服务类型。数据来源：本端规划 默认值：无 配置原则：编号0-127为标准SST，编号128-255为运营商自定义的SST。1-eMBB：适用于处理5G增强型移动宽带。2-uRLLC：适用于处理超可靠的低延迟通信。3-mIoT：适用于处理大规模物联网。4-V2X：适用于处理V2X服务。
sd|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于设置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：运营商可根据需求设置限制的切片。数据来源：本端规划默认值：NULL 配置原则：无
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 1-50|参数作用：该参数用于设置SupiRestrictedSnssai记录的别名。修改影响：运营商可设置记录的别名，方便理解此记录存在的场景。数据来源：本端规划 默认值：无 配置原则：无
命令举例 
`
新增基于SUPI号段的RestrictedSnssai配置，SUPI号段为"460"，对应限制的切片SST为eMBB，SD为“123456"。
ADD 5GSUPIRSTRNSSAI:SUPISEG="460",SST=eMBB,SD="123456"
` 
#### 修改基于SUPI号段的RestrictedSnssai配置(SET 5GSUPIRSTRNSSAI) 
#### 修改基于SUPI号段的RestrictedSnssai配置(SET 5GSUPIRSTRNSSAI) 
功能说明 
该命令用于修改基于SUPI号段的RestrictedSnssai配置。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置限制切片访问的用户SUPI号段。修改影响：运营商可根据需求设置限制切片访问的SUPI号段。数据来源：本端规划 默认值：无 配置原则：无
sst|SST|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于设置SST（Slice/Service Type，切片/服务类型）。修改影响：运营商可根据需求设置限制的切片/服务类型。数据来源：本端规划 默认值：无 配置原则：编号0-127为标准SST，编号128-255为运营商自定义的SST。1-eMBB：适用于处理5G增强型移动宽带。2-uRLLC：适用于处理超可靠的低延迟通信。3-mIoT：适用于处理大规模物联网。4-V2X：适用于处理V2X服务。
sd|SD|参数可选性: 必选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于设置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：运营商可根据需求设置限制的切片。数据来源：本端规划默认值：NULL 配置原则：无
alias|别名|参数可选性: 必选参数类型: 字符串参数范围: 1-50|参数作用：该参数用于设置SupiRestrictedSnssai记录的别名。修改影响：运营商可设置记录的别名，方便理解此记录存在的场景。数据来源：本端规划 默认值：无 配置原则：无
命令举例 
`
修改基于SUPI号段的RestrictedSnssai配置，SUPI号段为"460"，限制的切片SST为eMBB，SD为“123456"，该条记录的别名为"RestrictedSnssai ProfileId 001"。
SET 5GSUPIRSTRNSSAI:SUPISEG="460",SST=eMBB,SD="123456",ALIAS="RestrictedSnssai ProfileId 001"
` 
#### 删除基于SUPI号段的RestrictedSnssai配置(DEL 5GSUPIRSTRNSSAI) 
#### 删除基于SUPI号段的RestrictedSnssai配置(DEL 5GSUPIRSTRNSSAI) 
功能说明 
该命令用于删除基于SUPI号段的RestrictedSnssai配置。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置限制切片访问的用户SUPI号段。修改影响：运营商可根据需求设置限制切片访问的SUPI号段。数据来源：本端规划 默认值：无 配置原则：无
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于设置SST（Slice/Service Type，切片/服务类型）。修改影响：运营商可根据需求设置限制的切片/服务类型。数据来源：本端规划 默认值：无 配置原则：编号0-127为标准SST，编号128-255为运营商自定义的SST。1-eMBB：适用于处理5G增强型移动宽带。2-uRLLC：适用于处理超可靠的低延迟通信。3-mIoT：适用于处理大规模物联网。4-V2X：适用于处理V2X服务。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于设置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：运营商可根据需求设置限制的切片。数据来源：本端规划默认值：NULL 配置原则：无
命令举例 
`
删除SUPI号段为“460"的基于SUPI号段的RestrictedSnssai配置。
DEL 5GSUPIRSTRNSSAI:SUPISEG="460"
` 
#### 查询基于SUPI号段的RestrictedSnssai配置(SHOW 5GSUPIRSTRNSSAI) 
#### 查询基于SUPI号段的RestrictedSnssai配置(SHOW 5GSUPIRSTRNSSAI) 
功能说明 
该命令用于查询基于SUPI号段的RestrictedSnssai配置。支持单索引、全部查询等方式。 
注意事项 
无。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置限制切片访问的用户SUPI号段。修改影响：运营商可根据需求设置限制切片访问的SUPI号段。数据来源：本端规划 默认值：无 配置原则：无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置限制切片访问的用户SUPI号段。修改影响：运营商可根据需求设置限制切片访问的SUPI号段。数据来源：本端规划 默认值：无 配置原则：无
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|参数作用：该参数用于设置SST（Slice/Service Type，切片/服务类型）。修改影响：运营商可根据需求设置限制的切片/服务类型。数据来源：本端规划 默认值：无 配置原则：编号0-127为标准SST，编号128-255为运营商自定义的SST。1-eMBB：适用于处理5G增强型移动宽带。2-uRLLC：适用于处理超可靠的低延迟通信。3-mIoT：适用于处理大规模物联网。4-V2X：适用于处理V2X服务。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|参数作用：该参数用于设置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。修改影响：运营商可根据需求设置限制的切片。数据来源：本端规划默认值：NULL 配置原则：无
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 1-50|参数作用：该参数用于设置SupiRestrictedSnssai记录的别名。修改影响：运营商可设置记录的别名，方便理解此记录存在的场景。数据来源：本端规划 默认值：无 配置原则：无
命令举例 
`
查询基于SUPI号段的RestrictedSnssai配置。
SHOW 5GSUPIRSTRNSSAI
(No.1) : SHOW 5GSUPIRSTRNSSAI:
-----------------Namf_Communication_0----------------
操作维护       SUPI号段 SST    SD     别名                               
-------------------------------------------------------------------------
复制 修改 删除 460      1-eMBB 123456 460 RestrictedSnssai ProfileId 001 
-------------------------------------------------------------------------
记录数：1
执行成功 开始时间:2021-12-15 14:30:44 耗时: 0.15 秒
` 
# 接入区域配置 
# 接入区域配置 
背景知识 
在5G网络中，人为的把移动网络管理的物理范围划分为各种区域。移动网络中的各个NF使用区域对终端进行移动性管理。 
功能说明 
在接入区域配置中，TA配置和注册区域属于基于的配置，用于用户的移动性管理。 
子主题： 
## TA 配置 
## TA 配置 
背景知识 
TAI：跟踪区域标识（Tracking Area Identity），由MCC（Mobile Country Code，移动国家码）、MNC（Mobility Network Code，移动网络码）和TAC（Tracking Area Code，跟踪区域码）组成，由运营商统一规划。每个TAI对应一定物理位置区域。 
功能说明 
本功能用于配置本AMF所管理的跟踪区（TAI）信息、每个TAI对应的语音策略属性、以及紧急业务配置，紧急业务配置包括紧急号码、紧急回落能力等。 
配置本功能前，需要先通过[ADD 5GTAVOICEPOLICYTEMPLATE]命令，配置语音策略模板，通过[ADD 5GTAVOICEPOLICYTEMPLATE]命令，配置注册区域标识，通过[ADD 5GEMERNUMLIST]命令，配置紧急号码列表，通过[ADD 5GEXTEMERNUMLIST]命令，配置扩展紧急呼叫号码列表。
子主题： 
### 新增跟踪区配置(ADD TACFG) 
### 新增跟踪区配置(ADD TACFG) 
功能说明 
该命令用于增加TAI配置信息。 
TAI是AMF的基本配置数据，当AMF部署成功时，需要配置本AMF管理的TAI，或运营商网络规划变更，需要新增TAI时，也需要通过本命令进行配置。 
注意事项 
该命令执行后立即生效。 
配置本命令前，需要先通过[ADD 5GTAVOICEPOLICYTEMPLATE]命令，配置参数“POLICYTEMPID”，然后在此命令中通过参数“TAVOICEPOLICYTEMPID”将跟踪区与[ADD 5GTAVOICEPOLICYTEMPLATE]命令配置的参数“POLICYTEMPID”关联起来。
在支持紧急呼叫功能的场景下，需要先通过[ADD 5GEMERNUMLIST]命令，配置参数“LISTID”，然后在此命令中通过参数“EMERGENCYNUMLISTID”将跟踪区与[ADD 5GEMERNUMLIST]命令配置的参数“LISTID”关联起来。
最多可输入100000条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
taId|跟踪区标识|参数可选性: 必选参数类型: 数字参数范围: 1-16777215默认值: 1|参数作用：该参数用于配置跟踪区标识。修改影响：无。数据来源：全网规划。默认值：无。配置原则：一个跟踪区标识在一个AMF内唯一。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：无。数据来源：全网规划。默认值：无。配置原则：MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。修改影响：无。数据来源：全网规划。默认值：无。配置原则：MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tac|跟踪区码（HEX）|参数可选性: 必选参数类型: 字符串参数范围: 6-6|参数作用：该参数用于配置跟踪区编号，由运营商在PLMN内统一规划，以16进制数字编码。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
taName|跟踪区名称|参数可选性: 必选参数类型: 字符串参数范围: 1-13|参数作用：该参数用于配置跟踪区名称，由运营商自定义命名。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
taVoicePolicyTempId|TA语音策略模板ID|参数可选性: 必选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置TA关联的语音策略模板ID，即该TA下的用户使用的语音策略。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值引用于ADD 5GTAVOICEPOLICYTEMPLATE命令配置的参数“POLICYTEMPID”，必须通过ADD 5GTAVOICEPOLICYTEMPLATE命令预先配置。
emergCapa|紧急业务能力|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务的无线接入类型。修改影响：无。数据来源：本端规划。默认值：NR和E-UTRAN均支持。配置原则：NR和E-UTRAN均不支持：本TA下NR和E-UTRAN均不支持紧急业务。仅NR支持：本TA下仅NR支持紧急业务。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务。
sprtEmergFallback|支持紧急业务回落|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于配置控制本TA是否支持紧急业务回落。修改影响：无。数据来源：本端规划。默认值：不支持。配置原则：无。
emergFallbackCapa|紧急回落能力|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA支持紧急业务回落的无线接入类型。修改影响：无。数据来源：本端规划。默认值：NR和E-UTRAN均支持。配置原则：仅NR支持：本TA下仅NR支持紧急业务回落。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务回落。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务回落。
emergencyNumListID|紧急号码列表ID|参数可选性: 必选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：该参数用于配置本TA所关联的紧急号码列表ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值引用于ADD 5GEMERNUMLIST命令配置的参数“LISTID”，必须通过ADD 5GEMERNUMLIST命令预先配置。
extEmergNumListID|扩展紧急号码列表ID|参数可选性: 必选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：该参数用于配置本TA所关联的扩展紧急号码列表ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值引用于ADD 5GEXTEMERNUMLIST命令配置的参数“LISTID”，必须通过ADD 5GEXTEMERNUMLIST命令预先配置。
suppcanceln2rel|RAN是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: USERANDEFAULTCAPA|参数作用：该参数用于配置本TA下RAN是否支持取消用户无活动触发的N2释放流程。修改影响：不支持：本TA下RAN不支持取消用户无活动触发的N2释放流程。支持：本TA下RAN支持取消用户无活动触发的N2释放流程。 使用RAN缺省支持能力：本TA下使用RAN缺省支持能力。数据来源：本端规划。默认值：使用RAN缺省支持能力。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
taId|跟踪区标识|参数可选性: 任选参数类型: 数字参数范围: 1-16777215默认值: 1|参数作用：该参数用于配置跟踪区标识。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tac|跟踪区码（HEX）|参数可选性: 任选参数类型: 字符串参数范围: 6-6|参数作用：该参数用于配置跟踪区编号，由运营商在PLMN内统一规划，以16进制数字编码。
taName|跟踪区名称|参数可选性: 任选参数类型: 字符串参数范围: 1-13|参数作用：该参数用于配置跟踪区名称，由运营商自定义命名。
taVoicePolicyTempId|TA语音策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置TA关联的语音策略ID，即该TA下的用户使用的语音策略。
emergCapa|紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务的无线接入类型。NR和E-UTRAN均不支持：本TA下NR和E-UTRAN均不支持紧急业务。仅NR支持：本TA下仅NR支持紧急业务。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务。
sprtEmergFallback|支持紧急业务回落|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于配置控制本TA是否支持紧急业务回落。
emergFallbackCapa|紧急回落能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务回落的无线接入类型，默认“NR和E-UTRAN均支持”。仅NR支持：本TA下仅NR支持紧急业务回落。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务回落。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务回落。
emergencyNumListID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|该参数用于配置本TA所关联的紧急号码列表ID。由运营商根据网络规划。
extEmergNumListID|扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|该参数用于配置本TA所关联的扩展紧急号码列表ID。由运营商根据网络规划。
suppcanceln2rel|RAN是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: USERANDEFAULTCAPA|参数作用：该参数用于配置本TA下RAN是否支持取消用户无活动触发的N2释放流程。
命令举例 
`
新增标识1的TAI配置，修改后MCC为460，MNC为11，TAC为000001，关联语音策略模板1。
ADD TACFG:TAID=1,MCC="460",MNC="11",TAC="000001",TANAME="ngTA-1",TAVOICEPOLICYTEMPID=1,EMERGCAPA="BOTHNRANDEUTRANSPRT",SPRTEMERGFALLBACK="YES",EMERGFALLBACKCAPA="BOTHNRANDEUTRANSPRT",EMERGENCYNUMLISTID=1,EXTEMERGNUMLISTID=1
` 
### 修改跟踪区配置(SET TACFG) 
### 修改跟踪区配置(SET TACFG) 
功能说明 
该命令用于修改已经配置成功的TAI信息。 
当运营商的网络规划数据发生变更，需要使用本命令对已有TAI进行修改，或TAI对应的注册区域、语音策略模板发生变化、或者紧急业务配置需要改变时，也需要通过本命令进行修改。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
taId|跟踪区标识|参数可选性: 必选参数类型: 数字参数范围: 1-16777215默认值: 1|参数作用：该参数用于配置跟踪区标识。修改影响：无。数据来源：全网规划。默认值：无。配置原则：一个跟踪区标识在一个AMF内唯一。
taName|跟踪区名称|参数可选性: 任选参数类型: 字符串参数范围: 1-13|参数作用：该参数用于配置跟踪区名称，由运营商自定义命名。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
taVoicePolicyTempId|TA语音策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置TA关联的语音策略模板ID，即该TA下的用户使用的语音策略。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值引用于ADD 5GTAVOICEPOLICYTEMPLATE命令配置的参数“POLICYTEMPID”，必须通过ADD 5GTAVOICEPOLICYTEMPLATE命令预先配置。
emergCapa|紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务的无线接入类型。修改影响：无。数据来源：本端规划。默认值：NR和E-UTRAN均支持。配置原则：NR和E-UTRAN均不支持：本TA下NR和E-UTRAN均不支持紧急业务。仅NR支持：本TA下仅NR支持紧急业务。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务。
sprtEmergFallback|支持紧急业务回落|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于配置控制本TA是否支持紧急业务回落。修改影响：无。数据来源：本端规划。默认值：不支持。配置原则：无。
emergFallbackCapa|紧急回落能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA支持紧急业务回落的无线接入类型。修改影响：无。数据来源：本端规划。默认值：NR和E-UTRAN均支持。配置原则：仅NR支持：本TA下仅NR支持紧急业务回落。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务回落。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务回落。
emergencyNumListID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：该参数用于配置本TA所关联的紧急号码列表ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值引用于ADD 5GEMERNUMLIST命令配置的参数“LISTID”，必须通过ADD 5GEMERNUMLIST命令预先配置。
extEmergNumListID|扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：该参数用于配置本TA所关联的扩展紧急号码列表ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值引用于ADD 5GEXTEMERNUMLIST命令配置的参数“LISTID”，必须通过ADD 5GEXTEMERNUMLIST命令预先配置。
suppcanceln2rel|RAN是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: USERANDEFAULTCAPA|参数作用：该参数用于配置本TA下RAN是否支持取消用户无活动触发的N2释放流程。修改影响：不支持：本TA下RAN不支持取消用户无活动触发的N2释放流程。支持：本TA下RAN支持取消用户无活动触发的N2释放流程。 使用RAN缺省支持能力：本TA下使用RAN缺省支持能力。数据来源：本端规划。默认值：使用RAN缺省支持能力。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
taId|跟踪区标识|参数可选性: 任选参数类型: 数字参数范围: 1-16777215默认值: 1|参数作用：该参数用于配置跟踪区标识。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tac|跟踪区码（HEX）|参数可选性: 任选参数类型: 字符串参数范围: 6-6|参数作用：该参数用于配置跟踪区编号，由运营商在PLMN内统一规划，以16进制数字编码。
taName|跟踪区名称|参数可选性: 任选参数类型: 字符串参数范围: 1-13|参数作用：该参数用于配置跟踪区名称，由运营商自定义命名。
taVoicePolicyTempId|TA语音策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置TA关联的语音策略ID，即该TA下的用户使用的语音策略。
emergCapa|紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务的无线接入类型。NR和E-UTRAN均不支持：本TA下NR和E-UTRAN均不支持紧急业务。仅NR支持：本TA下仅NR支持紧急业务。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务。
sprtEmergFallback|支持紧急业务回落|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于配置控制本TA是否支持紧急业务回落。
emergFallbackCapa|紧急回落能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务回落的无线接入类型，默认“NR和E-UTRAN均支持”。仅NR支持：本TA下仅NR支持紧急业务回落。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务回落。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务回落。
emergencyNumListID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|该参数用于配置本TA所关联的紧急号码列表ID。由运营商根据网络规划。
extEmergNumListID|扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|该参数用于配置本TA所关联的扩展紧急号码列表ID。由运营商根据网络规划。
suppcanceln2rel|RAN是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: USERANDEFAULTCAPA|参数作用：该参数用于配置本TA下RAN是否支持取消用户无活动触发的N2释放流程。
命令举例 
`
修改标识1234的TAI配置，关联语音策略模板1。
SET TACFG:TAID=1234,TAVOICEPOLICYTEMPID=1
` 
### 删除跟踪区配置(DEL TACFG) 
### 删除跟踪区配置(DEL TACFG) 
功能说明 
该命令用于删除一个本AMF管理的TAI。 
注意事项 
该命令执行后立即生效。 
配置的一个跟踪区可能会被其他命令所引用，在删除一个跟踪区时，必须保证此跟踪区没有被其他的命令所引用，否则无法删除。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
taId|跟踪区标识|参数可选性: 必选参数类型: 数字参数范围: 1-16777215默认值: 1|参数作用：该参数用于配置跟踪区标识。修改影响：无。数据来源：全网规划。默认值：无。配置原则：一个跟踪区标识在一个AMF内唯一。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
taId|跟踪区标识|参数可选性: 任选参数类型: 数字参数范围: 1-16777215默认值: 1|参数作用：该参数用于配置跟踪区标识。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tac|跟踪区码（HEX）|参数可选性: 任选参数类型: 字符串参数范围: 6-6|参数作用：该参数用于配置跟踪区编号，由运营商在PLMN内统一规划，以16进制数字编码。
taName|跟踪区名称|参数可选性: 任选参数类型: 字符串参数范围: 1-13|参数作用：该参数用于配置跟踪区名称，由运营商自定义命名。
taVoicePolicyTempId|TA语音策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置TA关联的语音策略ID，即该TA下的用户使用的语音策略。
emergCapa|紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务的无线接入类型。NR和E-UTRAN均不支持：本TA下NR和E-UTRAN均不支持紧急业务。仅NR支持：本TA下仅NR支持紧急业务。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务。
sprtEmergFallback|支持紧急业务回落|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于配置控制本TA是否支持紧急业务回落。
emergFallbackCapa|紧急回落能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务回落的无线接入类型，默认“NR和E-UTRAN均支持”。仅NR支持：本TA下仅NR支持紧急业务回落。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务回落。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务回落。
emergencyNumListID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|该参数用于配置本TA所关联的紧急号码列表ID。由运营商根据网络规划。
extEmergNumListID|扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|该参数用于配置本TA所关联的扩展紧急号码列表ID。由运营商根据网络规划。
suppcanceln2rel|RAN是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: USERANDEFAULTCAPA|参数作用：该参数用于配置本TA下RAN是否支持取消用户无活动触发的N2释放流程。
命令举例 
`
删除标识为1234的TAI配置。
DEL TACFG:TAID=1234
` 
### 查询跟踪区配置(SHOW TACFG) 
### 查询跟踪区配置(SHOW TACFG) 
功能说明 
该命令用于查询已经配置的TAI信息。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
taId|跟踪区标识|参数可选性: 任选参数类型: 数字参数范围: 1-16777215默认值: 1|参数作用：该参数用于配置跟踪区标识。修改影响：无。数据来源：全网规划。默认值：无。配置原则：一个跟踪区标识在一个AMF内唯一。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
taId|跟踪区标识|参数可选性: 任选参数类型: 数字参数范围: 1-16777215默认值: 1|参数作用：该参数用于配置跟踪区标识。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tac|跟踪区码（HEX）|参数可选性: 任选参数类型: 字符串参数范围: 6-6|参数作用：该参数用于配置跟踪区编号，由运营商在PLMN内统一规划，以16进制数字编码。
taName|跟踪区名称|参数可选性: 任选参数类型: 字符串参数范围: 1-13|参数作用：该参数用于配置跟踪区名称，由运营商自定义命名。
taVoicePolicyTempId|TA语音策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置TA关联的语音策略ID，即该TA下的用户使用的语音策略。
emergCapa|紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务的无线接入类型。NR和E-UTRAN均不支持：本TA下NR和E-UTRAN均不支持紧急业务。仅NR支持：本TA下仅NR支持紧急业务。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务。
sprtEmergFallback|支持紧急业务回落|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于配置控制本TA是否支持紧急业务回落。
emergFallbackCapa|紧急回落能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BOTHNRANDEUTRANSPRT|参数作用：该参数用于配置本TA下支持紧急业务回落的无线接入类型，默认“NR和E-UTRAN均支持”。仅NR支持：本TA下仅NR支持紧急业务回落。 仅E-UTRAN支持：本TA下仅E-UTRAN支持紧急业务回落。NR和E-UTRAN均支持：本TA下NR和E-UTRAN均支持紧急业务回落。
emergencyNumListID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|该参数用于配置本TA所关联的紧急号码列表ID。由运营商根据网络规划。
extEmergNumListID|扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|该参数用于配置本TA所关联的扩展紧急号码列表ID。由运营商根据网络规划。
suppcanceln2rel|RAN是否支持取消用户无活动触发的N2释放流程|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: USERANDEFAULTCAPA|参数作用：该参数用于配置本TA下RAN是否支持取消用户无活动触发的N2释放流程。
命令举例 
`
SHOW TACFG:
(No.1) : SHOW TACFG:
-----------------Namf_Communication_0_A----------------
操作维护       跟踪区标识 移动国家码 移动网络码 跟踪区码（HEX） 跟踪区名称 TA语音策略模板ID 紧急业务能力      支持紧急业务回落 紧急回落能力      紧急号码列表ID 扩展紧急号码列表ID RAN是否支持取消用户无活动触发的N2释放流程
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1000       460        11         100000          100000     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
复制 修改 删除 1001       460        11         100001          100001     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
复制 修改 删除 1002       460        11         100002          100002     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
复制 修改 删除 1003       460        11         100003          100003     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
复制 修改 删除 1004       460        11         100004          100004     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
复制 修改 删除 1005       460        11         100005          100005     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
复制 修改 删除 1006       460        11         100006          100006     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
复制 修改 删除 1007       460        11         100007          100007     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
复制 修改 删除 1008       460        11         100008          100008     0                NR和E-UTRAN均支持 是               NR和E-UTRAN均支持 0              0                  不支持
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：9
执行成功开始时间:2020-10-19 20:10:35 耗时: 0.128 秒
` 
## 注册区域配置 
## 注册区域配置 
背景知识 
注册区域属于5G网络的范畴，在5G中把网络中划分的区域标识为注册区域。在移动性管理中，通过注册流程和注册更新流程完成注册区域的分配和更新。 
注册区域应该包含该终端的允许服务器区内的一组TA所包括的范围。 
功能说明 
本功能用于配置UE注册和注册更新流程中的注册区域的分配以及分配策略。 
子主题： 
### 注册区域标识 
### 注册区域标识 
背景知识 
AMF在UE注册成功的时候为UE分配注册区域。当UE移动到注册区域范围之外时，UE会发起移动性的注册更新流程。注册区域的分配参考多个因素。 
参见3GPP TS 23501协议的”5.3.2.3 Registration Area management“。 
功能说明 
本功能用于配置注册区域，可根据运营商的实际规划数据，划分若干个注册区域，用户注册的时候，根据用户当前位置所在的区域，为用户分配注册区域。 
本功能与TA配置数据相关，通过[ADD TACFG]命令配置TA的时候需要设置每个TA所归属的注册区域。
子主题： 
#### 新增注册区域配置(ADD REGAREACFG) 
#### 新增注册区域配置(ADD REGAREACFG) 
功能说明 
该命令用于新增注册区域，当运营商根据网络规划数据，新增一个注册区域时，操作员可使用此命令增加新的注册区域。 
增加成功之后，该注册区域才能被分配给UE。 
注意事项 
该命令执行后立即生效。 
一个AMF最多可以配置65535个注册区域。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域标识。修改影响：一个注册区域标识在一个AMF内唯一标识一个注册区域，该参数不允许修改。数据来源：本端规划。默认值：无。配置原则：一个注册区域标识在一个AMF内唯一，一个AMF最多可以配置65535个注册区域ID。
regAreaName|注册区域名称|参数可选性: 必选参数类型: 字符串参数范围: 1-50|参数作用：该参数用于配置注册区域名称，由运营商自定义。修改影响：修改该参数表明该注册区域名称发生变更。数据来源：本端规划。默认值：无。配置原则：无。
命令举例 
`
新增一个标识2的注册区域，其名称为"RegArea_Nanjing_Yuhua”
ADD REGAREACFG:REGAREAID=2,REGAREANAME="RegArea_Nanjing_Yuhua"
` 
#### 修改注册区域配置(SET REGAREACFG) 
#### 修改注册区域配置(SET REGAREACFG) 
功能说明 
该命令用于修改注册区域的名称，当该注册区域名称发生变更时，涉及到此命令的配置。 
注意事项 
该命令执行后立即生效。 
操作员通过本命令，只能修改注册区域的名称，不能修改注册区域的ID，即只能修改某个“REGAREAID”对应的“REGAREANAME”，不能修改“REGAREAID”。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域标识。修改影响：一个注册区域标识在一个AMF内唯一标识一个注册区域，该参数不允许修改。数据来源：本端规划。默认值：无。配置原则：一个注册区域标识在一个AMF内唯一，一个AMF最多可以配置65535个注册区域ID。
regAreaName|注册区域名称|参数可选性: 任选参数类型: 字符串参数范围: 1-50|参数作用：该参数用于配置注册区域名称，由运营商自定义。修改影响：修改该参数表明该注册区域名称发生变更。数据来源：本端规划。默认值：无。配置原则：无。
命令举例 
`
修改标识2的注册区域，其名称修改为"RegArea_Nanjing_Yuhuatai”
SET REGAREACFG:REGAREAID=2,REGAREANAME="RegArea_Nanjing_Yuhuatai"
` 
#### 删除注册区域配置(DEL REGAREACFG) 
#### 删除注册区域配置(DEL REGAREACFG) 
功能说明 
该命令用于删除某特定注册区域。当运营商的网络数据规划发生变化，需要删除某个注册区域时，涉及到此命令的使用。 
注意事项 
该命令执行后立即生效。 
操作员在删除某个注册区域时，操作员需要先将该注册区域下配置的TA，通过[ADD REGAREA TAIDLIST]命令，将这些TA配置到其他注册区域下。否则此注册区域被删除后，此被删除注册区域原对应的TA将不会被分配给UE。
可以通过[SHOW REGAREA TAIDLIST]命令查看注册区域下所对应的TA。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域标识。修改影响：一个注册区域标识在一个AMF内唯一标识一个注册区域，该参数不允许修改。数据来源：本端规划。默认值：无。配置原则：一个注册区域标识在一个AMF内唯一，一个AMF最多可以配置65535个注册区域ID。
命令举例 
`
删除标识1的注册区域。
DEL REGAREACFG:REGAREAID=1
` 
#### 查询注册区域配置(SHOW REGAREACFG) 
#### 查询注册区域配置(SHOW REGAREACFG) 
功能说明 
该命令用于查看当前AMF中已经配置的注册区域。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域标识。修改影响：一个注册区域标识在一个AMF内唯一标识一个注册区域，该参数不允许修改。数据来源：本端规划。默认值：无。配置原则：一个注册区域标识在一个AMF内唯一，一个AMF最多可以配置65535个注册区域ID。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域标识。
regAreaName|注册区域名称|参数可选性: 任选参数类型: 字符串参数范围: 1-50|参数作用：该参数用于配置注册区域名称，由运营商自定义。
命令举例 
`
查询本AMF当前已配置的全部注册区域或某个特定的注册区域。
SHOW REGAREACFG:
(No.4) : SHOW REGAREACFG:
-----------------Namf_Communication_0----------------
注册区域ID 注册区域名称
1 registAear_1
2 RegArea_Nanjing_Yuhuatai
记录数：2
执行成功耗时: 0.069 秒
` 
### 注册区域跟踪区标识列表配置 
### 注册区域跟踪区标识列表配置 
背景知识 
AMF在UE注册成功的时候为UE分配注册区域。当UE移动到注册区域范围之外时，UE会发起移动性的注册更新流程。注册区域的分配参考多个因素。 
参见3GPP TS 23501协议的”5.3.2.3 Registration Area management“。 
功能说明 
该配置是“注册区域标识”的子表配置，即为“注册区域标识”已经存在的某个注册区域增加关联的跟踪区列表。 
子主题： 
#### 增加注册区域跟踪区标识列表(ADD REGAREA TAIDLIST) 
#### 增加注册区域跟踪区标识列表(ADD REGAREA TAIDLIST) 
功能说明 
该命令用于为已经配置成功的注册区域下增加对应的跟踪区列表。每个注册区域最多可配置16个跟踪区标识。 
注意事项 
该命令执行后立即生效。 
由于每个注册区域下需要配置跟踪区，在配置本命令前，需要先通过[ADD TACFG]命令，配置跟踪区。
由于每个注册区域是通过注册区域标识来进行表示的，配置本功能前，需要先通过[ADD REGAREACFG]命令，配置注册区域标识。
一个跟踪区只能归属一个注册区域。 
一个注册区域下，最多允许配置16个跟踪区。 
本命令最多可配置65535条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个跟踪区只能归属一个注册区域，每个注册区域最多配置16个TA标识。本参数的取值引用于ADD REGAREACFG命令配置的参数“REGAREAID”，必须通过ADD REGAREACFG命令预先配置。
taId|跟踪区标识|参数可选性: 必选参数类型: 数字参数范围: 1-16777215|参数作用：该参数用于配置注册区域对应的跟踪区。修改影响：用户可以删除某个注册区域下已经配置的跟踪区标识。数据来源：本端规划。默认值：无。配置原则：一个跟踪区只能归属一个注册区域，每个注册区域最多配置16个TA标识。本参数的取值引用于ADD TACFG命令配置的参数“TAID”，必须通过ADD TACFG命令预先配置。
命令举例 
`
为已经成功配置的标识为1的注册区域增加一个标识为2的TA配置，该TA的MCC/MNC/TAC/REGAREAID/TANAM/TAVOICEPOLICYTEMPID信息都需要先通过ADD TACFG命令配置。
ADD REGAREA TAIDLIST:REGAREAID=1,TAID=2
` 
#### 删除注册区域跟踪区标识列表(DEL REGAREA TAIDLIST) 
#### 删除注册区域跟踪区标识列表(DEL REGAREA TAIDLIST) 
功能说明 
该命令用于删除某个注册区域下已经配置的跟踪区标识。 
注意事项 
该命令执行后立即生效。 
本命令是和[DEL REGAREACFG]命令配合使用的，操作员在通过[DEL REGAREACFG]删除某个注册区域时，如果该注册区域下配置了TA，操作员需要先通过本命令删除该注册区域下配置的TA，并通过[ADD REGAREA TAIDLIST]命令，将这些TA配置到其他注册区域下。否则此注册区域被删除后，此被删除注册区域下配置的TA将不会被分配给UE。
可以通过[SHOW REGAREA TAIDLIST]命令查看注册区域下所对应的TA。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个跟踪区只能归属一个注册区域，每个注册区域最多配置16个TA标识。本参数的取值引用于ADD REGAREACFG命令配置的参数“REGAREAID”，必须通过ADD REGAREACFG命令预先配置。
taId|跟踪区标识|参数可选性: 必选参数类型: 数字参数范围: 1-16777215|参数作用：该参数用于配置注册区域对应的跟踪区。修改影响：用户可以删除某个注册区域下已经配置的跟踪区标识。数据来源：本端规划。默认值：无。配置原则：一个跟踪区只能归属一个注册区域，每个注册区域最多配置16个TA标识。本参数的取值引用于ADD TACFG命令配置的参数“TAID”，必须通过ADD TACFG命令预先配置。
命令举例 
`
删除标识为1的注册区域下已经成功增加的标识为2的TA配置。
DEL REGAREA TAIDLIST:REGAREAID=1,TAID=2
` 
#### 查询注册区域跟踪区标识列表(SHOW REGAREA TAIDLIST) 
#### 查询注册区域跟踪区标识列表(SHOW REGAREA TAIDLIST) 
功能说明 
该命令用于查询已经配置的跟踪区标识。可以直接查询所有注册区域对应的跟踪区标识列表配置，也可以通过键入注册区域ID查询特定注册区域ID对应的跟踪区标识列表配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：一个跟踪区只能归属一个注册区域，每个注册区域最多配置16个TA标识。本参数的取值引用于ADD REGAREACFG命令配置的参数“REGAREAID”，必须通过ADD REGAREACFG命令预先配置。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
regAreaId|注册区域ID|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于配置注册区域ID。
taId|跟踪区标识|参数可选性: 任选参数类型: 数字参数范围: 1-16777215|参数作用：该参数用于配置注册区域对应的跟踪区。
命令举例 
`
查询AMF上所有注册区域配置。
SHOW REGAREA TAIDLIST:
(No.12) : SHOW REGAREA TAIDLIST:
-----------------Namf_Communication_0_A----------------
注册区域ID 跟踪区标识
1          1000
1          1001
1          1002
1          1003
1          1004
1          1005
1          1006
1          1007
1          1008
记录数：9
执行成功耗时: 0.164 秒
` 
### 注册区域分配策略 
### 注册区域分配策略 
背景知识 
注册区域（Registration Area），是终端在网络侧注册（Registration）之后，AMF给终端分配的一个区域，终端移动出此区域时，会触发移动性（Mobility类型）的注册（Registration）请求。 
参见3GPP TS 23.501  “5.3.2.3 Registration Area management”章节。 
该功能用于设置终端的注册区域的分配策略，需要考虑到如下因素。 
 
所分配注册区域中的TA（Tracking Area，跟踪区域）是否具有相同的IMS-Voice-Over-PS能力。
如果分配注册区域中的TA都具有相同的IMS-Voice-Over-PS能力，AMF向UDM注册时，携带的"Homogeneous Support of IMS Voice over PS Sessions" 指示了终端的IMS-Voice-Over-PS能力，便于后续UDM发起Terminating Access Domain Selection (T-ADS)流程。  具体描述参见TS23501“5.16.3.3 Homogeneous support for IMS voice over PS Session supported indication” 章节。 
 
所分配注册区域中的TA（Tracking Area，跟踪区域）是否具有相同的紧急业务能力。终端发起紧急呼叫时，参考AMF下发的网络侧紧急业务能力，确保选择合适的注册区域。 
 
所分配注册区域中的TA是否具有相同的紧急业务回落能力。终端发起紧急呼叫时，参考AMF下发的网络侧紧急业务回落能力，确保选择合适的注册区域。 
 
分配注册区域是否将终端最近一次访问的TA追加到注册区域中，因为这个终端可能很快又回到最近一次访问的TA下，这样可以减少频繁的移动性注册更新流程。 
 
功能说明 
本功能用于设置AMF给终端分配注册区域时的参考策略。 
 
如果网络内连续的区域都支持VoNR，则建议分配注册区域时，需要参考IMS能力，确保给终端分配的注册区域都支持IMS-Voice-Over-PS能力。AMF向UDM注册时携带的"Homogeneous Support of IMS Voice over PS Sessions" 为“Supported”,避免后续 Terminating Access Domain Selection (T-ADS) 时，向AMF请求终端位置。 
 
如果网络内支持VoNR的区域不连续，则建议分配注册区域时，不需要参考IMS能力，避免给终端分配的注册区域过小，导致终端移动性更新流程频度太大。 同时如果不开启此功能，AMF向UDM注册时携带的"Homogeneous Support of IMS Voice over PS Sessions" 为“unknown”，后续在Terminating Access Domain Selection (T-ADS) 时，需要向AMF请求终端的位置信息。 
 
如果网络内连续的区域都具有不同的紧急业务能力，则建议分配TA List时，参考紧急业务能力，确保给终端分配的注册区域都支持相同的紧急业务能力。AMF在注册接受消息中，会携带该紧急能力给终端，协助终端在紧急呼叫时选择合适的接入区域。 
 
如果网络内连续的区域都具有不同的紧急业务回落能力，则建议设置分配TA List，参考紧急业务回落能力，确保给终端分配的注册区域都支持相同的紧急业务回落能力。AMF在注册接受消息中，携带该紧急回落能力给终端，协助终端在紧急呼叫时选择合适的接入区域。 
 
子主题： 
#### 设置注册区域分配策略(SET 5GTALISTASSIGNPOLICY) 
#### 设置注册区域分配策略(SET 5GTALISTASSIGNPOLICY) 
功能说明 
该命令用于设置用户注册区域分配策略，如，是否确保TA具有相同的IMS能力，是否增加UE最近一次拜访的TA到注册区域中。 
对于"是否确保TA具有相同的IMS能力"参数，当开启VoNR（Voice over New Radio，新空口承载语音）时，需要根据网络实际状况进行设置，即支持VoNR的区域是否连续。该参数的设置，会影响用户注册区域的分配，影响AMF向UDM注册时携带的"Homogeneous Support of IMS Voice over PS Sessions"取值，进而影响Terminating Access Domain Selection (T-ADS) 时，UDM是否向AMF查询用户位置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SAMEIMSVOPS|注册区域分配参考IMS VoPS能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于设置当AMF给UE分配注册区域时，AMF是否确保该注册区域下的所有的TA是否具有相同的IMS能力（即这些TA是否都支持IMS Voice Over PS能力）。修改影响：修改为需要具有相同的IMS VoPS能力后，表明AMF给UE分配注册区域时，确保该注册区域下的所有的TA都具有相同的IMS能力。修改为不需要具有相同的IMS VoPS能力后，表明AMF给UE分配注册区域时，不需要确保该注册区域下的所有的TA都具有相同的IMS能力。数据来源：本端规划。默认值：需要具有相同的IMS VoPS能力。配置原则：当开启VoNR功能时，运营商根据现网实际状况进行设置配置。需要具有相同的IMS VoPS能力：如果5G网络内连续的区域都支持VoNR，则建议本参数设置为"需要具有相同的IMS VoPS能力"，即支持分配TAList参考IMS能力，确保给用户分配的注册区域都支持IMS语音。在这种情况下，AMF向UDM注册时，携带的"Homogeneous Support of IMS Voice over PS Sessions" 为"Supported"，避免后续在Terminating Access Domain Selection (T-ADS) 时，UDM向AMF请求用户位置。 不需要具有相同的IMS VoPS能力：如果网络支持VoNR的区域不连续，则建议本参数设置为"不需要具有相同的IMS VoPS能力"，避免给用户分配的注册区域过小，导致用户移动性更新流程频度太大。在这种情况下，AMF向UDM注册时，携带的"Homogeneous Support of IMS Voice over PS Sessions" 为"unknown"，后续在Terminating Access Domain Selection (T-ADS) 流程，UDM会向AMF请求用户位置。
SAMEEMCCAPA|注册区域分配参考紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSAMEEMC|参数作用：该参数用于设置AMF给UE分配注册区域时，是否确保该注册区域下的所有的TA都具有相同的紧急业务能力。修改影响：修改为需要具有相同的紧急业务能力后，表明AMF给UE分配注册区域时，确保该注册区域下的所有的TA都具有相同的紧急业务能力。修改为不需要具有相同的紧急业务能力后，表明AMF给UE分配注册区域时，不需要确保该注册区域下的所有的TA都具有相同的紧急业务能力。数据来源：本端规划。默认值：不需要具有相同的紧急业务能力。配置原则：当开启紧急业务功能时，运营商根据现网实际状况进行设置配置。需要具有相同的紧急业务能力：如果网络内连续的区域具有相同的紧急业务能力，则建议配置为该选项。不需要具有相同的紧急业务能力：如果网络内连续的区域具有不同的紧急业务能力，则建议配置为该选项。
SAMEEMFCAPA|注册区域分配参考紧急业务回落能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSAMEEMF|参数作用：设置AMF给UE分配注册区域时，是否确保该注册区域下的所有的TA都具有相同的紧急业务回落能力。修改影响：修改为需要具有相同的紧急业务回落能力后，表明AMF给UE分配注册区域时，需要确保该注册区域下的所有的TA都具有相同的紧急业务回落能力。修改为不需要具有相同的紧急业务回落能力后，表明AMF给UE分配注册区域时，不需要确保该注册区域下的所有的TA都具有相同的紧急业务回落能力。数据来源：本端规划。默认值：不需要具有相同的紧急业务回落能力。配置原则：当开启紧急业务回落功能时，运营商根据现网实际状况进行设置配置。需要具有相同的紧急业务回落能力：如果网络内连续的区域具有相同的紧急业务回落能力，则建议配置为该选项。 不需要具有相同的紧急业务回落能力：如果网络内连续的区域具有不同的紧急业务回落能力，则建议配置为该选项。
WITHLASTVISITEDTA|分配注册区域增加UE最近一次拜访的TA|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPTLASTTA|参数作用：该参数用于设置AMF给UE分配注册区域时，是否将UE最近一次拜访的TA（Tracking Area，跟踪区域）添加到注册区域中。UE最近一次拜访的TA，是指注册请求消息中携带的LastVisitRegTAI。修改影响：修改为支持分配注册区域增加UE最近一次拜访的TA后，表明设置AMF给UE分配注册区域时，支持将UE最近一次拜访的TA（Tracking Area，跟踪区域）添加到注册区域。修改为不支持分配注册区域增加UE最近一次拜访的TA后，表明设置AMF给UE分配注册区域时，不支持将UE最近一次拜访的TA（Tracking Area，跟踪区域）添加到注册区域。数据来源：本端规划。默认值：不支持分配注册区域增加UE最近一次拜访的TA。配置原则：无。"支持分配注册区域增加UE最近一次拜访的TA"：表明设置AMF给UE分配注册区域时，支持将UE最近一次拜访的TA（Tracking Area，跟踪区域）添加到注册区域。"不支持分配注册区域增加UE最近一次拜访的TA"：表明设置AMF给UE分配注册区域时，不支持将UE最近一次拜访的TA（Tracking Area，跟踪区域）添加到注册区域。
WITHLASTSEENTA|分配注册区域增加UE最近一次活动的TA|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: WITHLASTSEENTA|参数作用：该参数用于设置AMF给UE分配注册区域时，是否将UE最近一次活动的TA（Tracking Area，跟踪区域）添加到注册区域中。UE最近一次活动的TA指AMF从无线侧感知的，UE最近一次活动的TA。修改影响：修改为支持分配注册区域增加UE最近一次活动的TA后，表明设置AMF给UE分配注册区域时，支持将UE最近一次活动的TA（Tracking Area，跟踪区域）添加到注册区域中。修改为不支持分配注册区域增加UE最近一次活动的TA后，表明设置AMF给UE分配注册区域时，不支持将UE最近一次活动的TA（Tracking Area，跟踪区域）添加到注册区域中。数据来源：本端规划。默认值：支持分配注册区域增加UE最近一次活动的TA。配置原则：无。"支持分配注册区域增加UE最近一次活动的TA"：表明设置AMF给UE分配注册区域时，支持将UE最近一次活动的TA（Tracking Area，跟踪区域）添加到注册区域中。"不支持分配注册区域增加UE最近一次活动的TA"：表明设置AMF给UE分配注册区域时，不支持将UE最近一次活动的TA（Tracking Area，跟踪区域）添加到注册区域中。
SAMEPLMN|TA List必须属于同一PLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSAMEPLMN|参数作用：该参数用于配置AMF给UE分配的TA List是否需要属于同一PLMN，即在相同的PLMN范围下。修改影响：为UE分配新的TA List时，会产生影响。数据来源：本端规划。默认值：给UE分配的TA List必须属于同一PLMN。配置原则否（NO）：给UE分配的TA List不需要属于同一PLMN。是（YES）：给UE分配的TA List必须属于同一PLMN。建议设置为“是”，因为如果不设置，UE重新选择PLMN后可能不会发起注册更新，之后发起的业务请求流程，根据协议，并没有要求重新分配GUTI，但GUTI中的PLMN要求为服务PLMN。
命令举例 
`
设置分配注册区域分配策略：参考用户IMS能力，确保被分配的TA IMS能力一致；追加UE最近一次访问的TA到注册区域中
SET 5GTALISTASSIGNPOLICY:SAMEIMSVOPS="YES",WITHLASTVISITEDTA="SUPTLASTTA"
` 
#### 查询注册区域分配策略(SHOW 5GTALISTASSIGNPOLICY) 
#### 查询注册区域分配策略(SHOW 5GTALISTASSIGNPOLICY) 
功能说明 
该命令用于查询AMF的注册区域分配策略。 
注意事项 
该命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SAMEIMSVOPS|注册区域分配参考IMS VoPS能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于设置当AMF给UE分配注册区域时，AMF是否确保该注册区域下的所有的TA是否具有相同的IMS能力（即这些TA是否都支持IMS Voice Over PS能力）。
SAMEEMCCAPA|注册区域分配参考紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSAMEEMC|参数作用：该参数用于设置AMF给UE分配注册区域时，是否确保该注册区域下的所有的TA都具有相同的紧急业务能力。
SAMEEMFCAPA|注册区域分配参考紧急业务回落能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSAMEEMF|参数作用：设置AMF给UE分配注册区域时，是否确保该注册区域下的所有的TA都具有相同的紧急业务回落能力。
WITHLASTVISITEDTA|分配注册区域增加UE最近一次拜访的TA|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPTLASTTA|参数作用：该参数用于设置AMF给UE分配注册区域时，是否将UE最近一次拜访的TA（Tracking Area，跟踪区域）添加到注册区域中。UE最近一次拜访的TA，是指注册请求消息中携带的LastVisitRegTAI。
WITHLASTSEENTA|分配注册区域增加UE最近一次活动的TA|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: WITHLASTSEENTA|参数作用：该参数用于设置AMF给UE分配注册区域时，是否将UE最近一次活动的TA（Tracking Area，跟踪区域）添加到注册区域中。UE最近一次活动的TA指AMF从无线侧感知的，UE最近一次活动的TA。
SAMEPLMN|TA List必须属于同一PLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSAMEPLMN|参数作用：该参数用于配置AMF给UE分配的TA List是否需要属于同一PLMN，即在相同的PLMN范围下。
命令举例 
`
查询AMF设置的注册区域分配是否参考IMS VoPS能力。
SHOW 5GTALISTASSIGNPOLICY:
(No.1) : SHOW 5GTALISTASSIGNPOLICY:
-----------------Namf_Communication_0----------------
注册区域分配参考IMS VoPS能力      注册区域分配参考紧急业务能力     注册区域分配参考紧急业务回落能力       分配注册区域增加UE最近一次拜访的TA          分配注册区域增加UE最近一次活动的TA         TA List必须属于同一PLMN
不需要具有相同的IMS VoPS能力      不需要具有相同的紧急业务能力     不需要具有相同的紧急业务回落能力       不支持分配注册区域增加UE最近一次拜访的TA    支持分配注册区域增加UE最近一次活动的TA     给UE分配的TA List必须属于同一PLMN
记录数：1
执行成功耗时: 1.49 秒
` 
## 区域编码配置 
## 区域编码配置 
背景知识 
UDM上签约禁止区域和服务区域，可以是明确的跟踪区列表，也可以是其他地理信息（例如，经度/纬度，邮政编码等），叫做区域编码（Area Code）。UDM将区域编码（Area Code）发给AMF，AMF本地解析映射为具体的跟踪区列表，再进行禁止区域和服务区域的处理。 
功能说明 
UDM上签约禁止区域和服务区域，可以是明确的跟踪区列表，也可以是其他地理信息（例如，经度/纬度，邮政编码等），叫做区域编码（Area Code）。UDM将区域编码（Area Code）发给AMF，AMF本地解析映射为具体的跟踪区列表，再进行禁止区域和服务区域的处理。 
子主题： 
### 禁止区域编码配置 
### 禁止区域编码配置 
背景知识 
禁止区域是用来定义用户是否可以接入网络的区域范围，在禁止区域内，禁止UE与网络发起任何通信。 
在UDM上签约禁止区域，可以是明确的跟踪区列表，也可以是其他地理信息（例如，经度/纬度，邮政编码等），叫做区域编码（Area Code）。UDM将区域编码（Area Code）发给AMF，AMF本地解析映射为具体的跟踪区列表，再进行禁止区域限制处理。 
功能说明 
AMF需要将UDM下发的禁止区域编码（Area Code）配置映射为具体的服务区域TA列表。然后使用具体的禁止TA列表进行禁止区域限制处理。 
AMF支持按SUPI号段将禁止区域编码（Area Code）配置映射为具体的禁止区域TA列表，以便灵活地针对不同SUPI号段提供差异化的映射配置。即“基于SUPI号段的禁止区域编码配置”。 
对于不需要提供差异化配置的SUPI号段，AMF提供了“禁止区域编码配置”，这些号段可以共享该配置，统一使用该配置将禁止区域编码（Area Code）映射为具体的禁止区域TA列表配置。 
子主题： 
#### 新增禁止区域编码配置(ADD FORBIDDENAREACODE) 
#### 新增禁止区域编码配置(ADD FORBIDDENAREACODE) 
功能说明 
该命令用于配置禁止区域（Forbidden Area）和跟踪区的对应关系。一个禁止区域中包括了一组跟踪区。 
禁止区域（Forbidden Area），指终端不被允许发起连接的一个区域。在终端的签约信息中含有禁止区域的情况下，当终端移动到这些禁止区域内，终端被禁止接入5GC网络，不能接受任何网络服务。 
终端在UDM（Unified Data Management，统一数据管理）上签约的禁止区域，可以是一个明确的跟踪区列表（TA List），也可以是其他地理信息（例如，经度/纬度，邮政编码等），这些其他的地理信息统一称为区域编码（Area Code）。UDM将区域编码（Area Code）发送给AMF，AMF通过本命令配置的对应关系进行解析，将区域编码（Area Code）映射为具体的跟踪区列表（TA List），之后AMF就可以根据跟踪区列表（TA List）对终端进行禁止区域限制处理。 
注意事项 
该命令执行后立即生效。 
配置此命令前，需要确认操作员已经通过Namf_MP_0组件的[ADD TAGROUPCFG]命令配置了禁止区域对应的所有跟踪区。
最多可输入8192条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置禁止区域编码，禁止区域编码包含了一组跟踪区。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
areatype|区域类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: TAGROUPAREA|参数作用：该参数用于配置禁止区域编码对应的区域类型，包括：0：跟踪区组区域1：整个AMF区域修改影响：受配置原则的约束，此参数无法修改。数据来源：本端规划。默认值：0：跟踪区组区域。配置原则：区域类型为"跟踪区组区域"时，"跟踪区组"必须为有效值[1-1024]。区域类型为"整个AMF区域"时，"跟踪区组"必须为无效值0。区域类型为"整个AMF区域"时，当前记录关联的区域编码，仅允许添加此1条记录。
taGroupId|跟踪区组|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置禁止区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中"跟踪区组配置"中的"新增跟踪区组配置"ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须已预先配置。“TAGROUPID”可通过Namf_MP_0组件中"跟踪区组配置"中的"查询跟踪区组配置"SHOW TAGROUPCFG命令查询获取。"跟踪区组"为有效值[1-1024]时，区域类型必须为"跟踪区组区域"。"跟踪区组"为无效值0时，区域类型必须为"整个AMF区域"。
命令举例 
`
增加禁止区域编码配置，将区域编码1234567890映射到标识为1的跟踪区组，区域类型为"跟踪区组区域"。
ADD FORBIDDENAREACODE:AREACODE="1234567890",AREATYPE="TAGROUPAREA",TAGROUPID=1
` 
#### 删除禁止区域编码配置(DEL FORBIDDENAREACODE) 
#### 删除禁止区域编码配置(DEL FORBIDDENAREACODE) 
功能说明 
该命令用于删除禁止区域（Forbidden Area）和跟踪区的对应关系。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置禁止区域编码，禁止区域编码包含了一组跟踪区。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
taGroupId|跟踪区组|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置禁止区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中"跟踪区组配置"中的"新增跟踪区组配置"ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须已预先配置。“TAGROUPID”可通过Namf_MP_0组件中"跟踪区组配置"中的"查询跟踪区组配置"SHOW TAGROUPCFG命令查询获取。"跟踪区组"为有效值[1-1024]时，区域类型必须为"跟踪区组区域"。"跟踪区组"为无效值0时，区域类型必须为"整个AMF区域"。
命令举例 
`
删除禁止区域编码配置，不再对区域编码1234567890做映射。
DEL FORBIDDENAREACODE:AREACODE="1234567890"
` 
#### 查询禁止区域编码配置(SHOW FORBIDDENAREACODE) 
#### 查询禁止区域编码配置(SHOW FORBIDDENAREACODE) 
功能说明 
该命令用于查询禁止区域（Forbidden Area）和跟踪区的对应关系。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 任选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置禁止区域编码，禁止区域编码包含了一组跟踪区。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 任选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置禁止区域编码，禁止区域编码包含了一组跟踪区。
areatype|区域类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: TAGROUPAREA|参数作用：该参数用于配置禁止区域编码对应的区域类型，包括：0：跟踪区组区域1：整个AMF区域
taGroupId|跟踪区组|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置禁止区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。
命令举例 
`
查询禁止区域编码配置。
SHOW FORBIDDENAREACODE:
(No.1) : SHOW FORBIDDENAREACODE:
-----------------Namf_Communication_0----------------
区域编码      区域类型      跟踪区组
1234567890    跟踪区组区域  1
记录数：1
执行成功耗时: 0.188 秒
` 
### 基于SUPI号段的禁止区域编码配置 
### 基于SUPI号段的禁止区域编码配置 
背景知识 
禁止区域是用来定义用户是否可以接入网络的区域范围，在禁止区域内，禁止UE与网络发起任何通信。 
在UDM上签约禁止区域，可以是明确的跟踪区列表，也可以是其他地理信息（例如，经度/纬度，邮政编码等），叫做区域编码（Area Code）。UDM将区域编码（Area Code）发给AMF，AMF本地解析映射为具体的跟踪区列表，再进行禁止区域限制处理。 
功能说明 
AMF需要将UDM下发的禁止区域编码（Area Code）配置映射为具体的服务区域TA列表。然后使用具体的禁止TA列表进行禁止区域限制处理。 
AMF支持按SUPI号段将禁止区域编码（Area Code）配置映射为具体的禁止区域TA列表，以便灵活地针对不同SUPI号段提供差异化的映射配置。即“基于SUPI号段的禁止区域编码配置”。 
对于不需要提供差异化配置的SUPI号段，AMF提供了“禁止区域编码配置”，这些号段可以共享该配置，统一使用该配置将禁止区域编码（Area Code）映射为具体的禁止区域TA列表配置。 
子主题： 
#### 新增基于SUPI号段的禁止区域编码配置(ADD SUPISEGFORBAREACODE) 
#### 新增基于SUPI号段的禁止区域编码配置(ADD SUPISEGFORBAREACODE) 
功能说明 
该命令用于增加基于SUPI号段的禁止区域编码配置。AMF支持按SUPI号段进行禁止区域编码（Area Code）配置映射为具体的禁止区域TA列表，以便灵活地针对不同SUPI号段提供差异化的映射配置。 
注意事项 
该命令执行后立即生效。 
配置此命令前，需要确认操作员已经通过Namf_MP_0组件的[ADD TAGROUPCFG]命令配置了禁止区域对应的所有跟踪区。
最多可输入8192条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置SUPI号段。修改影响：无。数据来源：全网规划。默认值：无。配置原则：运营商规划好某个SUPI号段对应的禁止区域编码后，操作员需要在该SUPI号段下配置所有的禁止区域编码。AMF根据用户的SUPI号码和本命令配置的SUPI号段进行匹配，匹配原则是按最长号段进行匹配，一旦匹配到最长SUPI号段后，AMF会使用该SUPI号段下的禁止区域编码配置，不会再尝试查询其他较短号段或者默认的禁止区域编码配置。
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置禁止区域编码，禁止区域编码包含了一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的来源是通过ADD FORBIDDENAREACODE命令配置的参数“AREACODE“，必须先通过ADD FORBIDDENAREACODE命令预先配置。
areatype|区域类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: TAGROUPAREA|参数作用：该参数用于配置禁止区域编码对应的区域类型，包括：0：跟踪区组区域1：整个AMF区域修改影响：受配置原则的约束，此参数无法修改。数据来源：本端规划。默认值：0：跟踪区组区域。配置原则：区域类型为"跟踪区组区域"时，"跟踪区组"必须为有效值[1-1024]。区域类型为"整个AMF区域"时，"跟踪区组"必须为无效值0。区域类型为"整个AMF区域"时，当前记录关联的区域编码，仅允许添加此1条记录。
taGroupId|跟踪区组|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置禁止区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中"跟踪区组配置"中的"新增跟踪区组配置"ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须已预先配置。“TAGROUPID”可通过Namf_MP_0组件中"跟踪区组配置"中的"查询跟踪区组配置"SHOW TAGROUPCFG命令查询获取。"跟踪区组"为有效值[1-1024]时，区域类型必须为"跟踪区组区域"。"跟踪区组"为无效值0时，区域类型必须为"整个AMF区域"。
命令举例 
`
增加基于SUPI号段的禁止区域编码配置，在46001的SUPI号段下由区域编码1234567890映射到标识为1的跟踪区组。
ADD SUPISEGFORBAREACODE:SUPISEG="46001",AREACODE="1234567890",AREATYPE="TAGROUPAREA",TAGROUPID=1
` 
#### 删除基于SUPI号段的禁止区域编码配置(DEL SUPISEGFORBAREACODE) 
#### 删除基于SUPI号段的禁止区域编码配置(DEL SUPISEGFORBAREACODE) 
功能说明 
该命令用于删除基于SUPI号段的禁止区域编码配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置SUPI号段。修改影响：无。数据来源：全网规划。默认值：无。配置原则：运营商规划好某个SUPI号段对应的禁止区域编码后，操作员需要在该SUPI号段下配置所有的禁止区域编码。AMF根据用户的SUPI号码和本命令配置的SUPI号段进行匹配，匹配原则是按最长号段进行匹配，一旦匹配到最长SUPI号段后，AMF会使用该SUPI号段下的禁止区域编码配置，不会再尝试查询其他较短号段或者默认的禁止区域编码配置。
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置禁止区域编码，禁止区域编码包含了一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的来源是通过ADD FORBIDDENAREACODE命令配置的参数“AREACODE“，必须先通过ADD FORBIDDENAREACODE命令预先配置。
taGroupId|跟踪区组|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置禁止区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中"跟踪区组配置"中的"新增跟踪区组配置"ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须已预先配置。“TAGROUPID”可通过Namf_MP_0组件中"跟踪区组配置"中的"查询跟踪区组配置"SHOW TAGROUPCFG命令查询获取。"跟踪区组"为有效值[1-1024]时，区域类型必须为"跟踪区组区域"。"跟踪区组"为无效值0时，区域类型必须为"整个AMF区域"。
命令举例 
`
删除基于SUPI号段的禁止区域编码配置，在46001的SUPI号段下不再对区域编码1234567890做映射。
DEL SUPISEGFORBAREACODE:SUPISEG="46001",AREACODE="1234567890"
` 
#### 查询基于SUPI号段的禁止区域编码配置(SHOW SUPISEGFORBAREACODE) 
#### 查询基于SUPI号段的禁止区域编码配置(SHOW SUPISEGFORBAREACODE) 
功能说明 
该命令用于查询基于SUPI号段的禁止区域编码配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置SUPI号段。修改影响：无。数据来源：全网规划。默认值：无。配置原则：运营商规划好某个SUPI号段对应的禁止区域编码后，操作员需要在该SUPI号段下配置所有的禁止区域编码。AMF根据用户的SUPI号码和本命令配置的SUPI号段进行匹配，匹配原则是按最长号段进行匹配，一旦匹配到最长SUPI号段后，AMF会使用该SUPI号段下的禁止区域编码配置，不会再尝试查询其他较短号段或者默认的禁止区域编码配置。
areaCode|区域编码|参数可选性: 任选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置禁止区域编码，禁止区域编码包含了一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的来源是通过ADD FORBIDDENAREACODE命令配置的参数“AREACODE“，必须先通过ADD FORBIDDENAREACODE命令预先配置。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于设置终端的SUPI号段。
areaCode|区域编码|参数可选性: 任选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置禁止区域编码，禁止区域编码包含了一组跟踪区。
areatype|区域类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: TAGROUPAREA|参数作用：该参数用于配置禁止区域编码对应的区域类型，包括：0：跟踪区组区域1：整个AMF区域
taGroupId|跟踪区组|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置禁止区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。
命令举例 
`
查询基于SUPI号段的禁止区域编码配置。
SHOW SUPISEGFORBAREACODE
(No.1) : SHOW SUPISEGFORBAREACODE:
-----------------Namf_Communication_0----------------
SUPI号段     区域编码       区域类型       跟踪区组
46001        1234567890     跟踪区组区域   1
` 
### 服务区域编码配置 
### 服务区域编码配置 
背景知识 
服务区域是用来定义是否允许用户获取服务的区域范围，服务区域可以是允许区域或者非允许区域。如果定义了允许区域，那么允许区域之外的区域都是非允许区域，如果定义了非允许区域，那么非允许区域之外的区域都是允许区域。 
在非允许区域（或者允许区域之外的区域），UE和网络不允许启动业务请求流程或者发起SM信令流程来获取通信服务。 
服务区域可以由运营商在UDM上签约，由PCF进一步调整，由AMF下发给UE。AMF和UE按照服务区域限制要求进行服务限制。 
在UDM上签约服务区域，可以是明确的跟踪区列表，也可以是其他地理信息（例如，经度/纬度，邮政编码等），叫做区域编码（Area Code）。UDM将区域编码（Area Code）发给AMF，AMF需要本地解析映射为具体的服务跟踪区列表，再进行服务区域限制处理。 
功能说明 
AMF需要将UDM下发的服务区域编码（Area Code）配置映射为具体的服务区域TA列表。然后使用具体的服务TA列表发送给PCF、RAN、UE。 
AMF支持按SUPI号段进行服务区域编码（Area Code）配置映射为具体的服务区域TA列表，以便灵活地针对不同SUPI号段提供差异化的映射配置。即“基于SUPI号段的服务区域编码配置”。 
对于不需要提供差异化配置的SUPI号段，AMF提供了“服务区域编码配置”，这些号段可以共享该配置，统一使用该配置将服务区域编码（Area Code）映射为具体的服务区域TA列表配置。 
子主题： 
#### 新增服务区域编码配置(ADD SERVICEAREACODE) 
#### 新增服务区域编码配置(ADD SERVICEAREACODE) 
功能说明 
该命令用于配置服务区域（Servcie Area）和跟踪区的对应关系。一个服务区域中包含了一组跟踪区。 
注意事项 
该命令执行后立即生效。 
配置此命令前，需要确认操作员已经通过通过Namf_MP_0组件中的[ADD TAGROUPCFG]命令配置了服务区域对应的所有跟踪区。
最多可输入8192条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
taGroupId|跟踪区组|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置服务区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须先通过ADD TAGROUPCFG命令预先配置。“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。
命令举例 
`
增加服务区域编码配置，由区域编码1234567890映射到标识为1的跟踪区组。
ADD SERVICEAREACODE:AREACODE="1234567890",TAGROUPID=1
` 
#### 修改服务区域编码配置(SET SERVICEAREACODE) 
#### 修改服务区域编码配置(SET SERVICEAREACODE) 
功能说明 
该命令用于修改服务区域（Servcie Area）和跟踪区的对应关系。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
taGroupId|跟踪区组|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置服务区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须先通过ADD TAGROUPCFG命令预先配置。“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。
命令举例 
`
修改服务区域编码配置，由区域编码1234567890映射到标识为2的跟踪区组。
SET SERVICEAREACODE:AREACODE="1234567890",TAGROUPID=2
` 
#### 删除服务区域编码配置(DEL SERVICEAREACODE) 
#### 删除服务区域编码配置(DEL SERVICEAREACODE) 
功能说明 
该命令用于删除服务区域（Servcie Area）和跟踪区的对应关系。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
命令举例 
`
删除服务区域编码配置，不再对区域编码1234567890做映射。
DEL SERVICEAREACODE:AREACODE="1234567890"
` 
#### 查询服务区域编码配置(SHOW SERVICEAREACODE) 
#### 查询服务区域编码配置(SHOW SERVICEAREACODE) 
功能说明 
该命令用于查询服务区域（Servcie Area）和跟踪区的对应关系 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 任选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
areaCode|区域编码|参数可选性: 任选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。
taGroupId|跟踪区组|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置服务区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。
命令举例 
`
查询服务区域编码配置。
SHOW SERVICEAREACODE:
(No.1) : SHOW SERVICEAREACODE:
-----------------Namf_Communication_0----------------
区域编码         跟踪区组
1234567890    1
记录数：1
执行成功耗时: 0.188 秒
` 
### 基于SUPI号段的服务区域编码配置 
### 基于SUPI号段的服务区域编码配置 
背景知识 
服务区域是用来定义是否允许用户获取服务的区域范围，服务区域可以是允许区域或者非允许区域。如果定义了允许区域，那么允许区域之外的区域都是非允许区域，如果定义了非允许区域，那么非允许区域之外的区域都是允许区域。 
在非允许区域（或者允许区域之外的区域），UE和网络不允许启动业务请求流程或者发起SM信令流程来获取通信服务。 
服务区域可以由运营商在UDM上签约，由PCF进一步调整，由AMF下发给UE。AMF和UE按照服务区域限制要求进行服务限制。 
在UDM上签约服务区域，可以是明确的跟踪区列表，也可以是其他地理信息（例如，经度/纬度，邮政编码等），叫做区域编码（Area Code）。UDM将区域编码（Area Code）发给AMF，AMF需要本地解析映射为具体的服务跟踪区列表，再进行服务区域限制处理。 
功能说明 
AMF需要将UDM下发的服务区域编码（Area Code）配置映射为具体的服务区域TA列表。然后使用具体的服务TA列表发送给PCF、RAN、UE。 
AMF支持按SUPI号段进行服务区域编码（Area Code）配置映射为具体的服务区域TA列表，以便灵活地针对不同SUPI号段提供差异化的映射配置。即“基于SUPI号段的服务区域编码配置”。 
对于不需要提供差异化配置的SUPI号段，AMF提供了“服务区域编码配置”，这些号段可以共享该配置，统一使用该配置将服务区域编码（Area Code）映射为具体的服务区域TA列表配置。 
子主题： 
#### 新增基于SUPI号段的服务区域编码配置(ADD SUPISEGSERVAREACODE) 
#### 新增基于SUPI号段的服务区域编码配置(ADD SUPISEGSERVAREACODE) 
功能说明 
AMF支持按SUPI号段将服务区域编码（Area Code）配置映射为具体的服务区域TA列表，以便灵活地针对不同SUPI号段提供差异化的映射配置。该命令用于增加基于SUPI号段的服务区域编码配置。 
注意事项 
该命令执行后立即生效。 
配置此命令前，需要确认操作员已经通过Namf_MP_0组件的[ADD TAGROUPCFG]命令配置了服务区域对应的所有跟踪区。
最多可输入8192条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于配置SUPI号段。修改影响：无。数据来源：全网规划。默认值：无。配置原则：运营商规划好某个SUPI号段对应的服务区域编码后，操作员需要在该SUPI号段下配置所有的服务区域编码。AMF根据用户的SUPI号码和本命令配置的SUPI号段进行匹配，匹配原则是按最长号段进行匹配，一旦匹配到最长SUPI号段后，AMF会使用该SUPI号段下的服务区域编码配置，不会再尝试查询其他较短号段或者默认的服务区域编码配置。
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的来源是通过ADD FORBIDDENAREACODE命令配置的参数“AREACODE“，必须先通过ADD FORBIDDENAREACODE命令预先配置。
taGroupId|跟踪区组|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置服务区域编码对应的跟踪区组，跟踪区组包含一组跟踪区，在Namf_MP模型下“跟踪区组配置”中进行配置管理。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须先通过ADD TAGROUPCFG命令预先配置。“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。
命令举例 
`
增加基于SUPI号段的服务区域编码配置。46001号段的用户将服务区域编码“1234567890”映射成标识为1的跟踪区组
。
ADD SUPISEGSERVAREACODE:SUPISEG="46001",AREACODE="1234567890",TAGROUPID=1
` 
#### 修改基于SUPI号段的服务区域编码配置(SET SUPISEGSERVAREACODE) 
#### 修改基于SUPI号段的服务区域编码配置(SET SUPISEGSERVAREACODE) 
功能说明 
该命令用于修改基于SUPI号段的服务区域编码配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于配置SUPI号段。修改影响：无。数据来源：全网规划。默认值：无。配置原则：运营商规划好某个SUPI号段对应的服务区域编码后，操作员需要在该SUPI号段下配置所有的服务区域编码。AMF根据用户的SUPI号码和本命令配置的SUPI号段进行匹配，匹配原则是按最长号段进行匹配，一旦匹配到最长SUPI号段后，AMF会使用该SUPI号段下的服务区域编码配置，不会再尝试查询其他较短号段或者默认的服务区域编码配置。
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的来源是通过ADD FORBIDDENAREACODE命令配置的参数“AREACODE“，必须先通过ADD FORBIDDENAREACODE命令预先配置。
taGroupId|跟踪区组|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置服务区域编码对应的跟踪区组，跟踪区组包含一组跟踪区，在Namf_MP模型下“跟踪区组配置”中进行配置管理。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的取值来源于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须先通过ADD TAGROUPCFG命令预先配置。“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。
命令举例 
`
修改基于SUPI号段的服务区域编码配置。46001号段的用户将服务区域编码“1234567890”映射成标识为2的跟踪区组
。
SET SUPISEGSERVAREACODE:SUPISEG="46001",AREACODE="1234567890",TAGROUPID=2
` 
#### 删除基于SUPI号段的服务区域编码配置(DEL SUPISEGSERVAREACODE) 
#### 删除基于SUPI号段的服务区域编码配置(DEL SUPISEGSERVAREACODE) 
功能说明 
该命令用于删除基于SUPI号段的服务区域编码配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于配置SUPI号段。修改影响：无。数据来源：全网规划。默认值：无。配置原则：运营商规划好某个SUPI号段对应的服务区域编码后，操作员需要在该SUPI号段下配置所有的服务区域编码。AMF根据用户的SUPI号码和本命令配置的SUPI号段进行匹配，匹配原则是按最长号段进行匹配，一旦匹配到最长SUPI号段后，AMF会使用该SUPI号段下的服务区域编码配置，不会再尝试查询其他较短号段或者默认的服务区域编码配置。
areaCode|区域编码|参数可选性: 必选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的来源是通过ADD FORBIDDENAREACODE命令配置的参数“AREACODE“，必须先通过ADD FORBIDDENAREACODE命令预先配置。
命令举例 
`
删除基于SUPI号段的服务区域编码配置。46001号段下不再对服务区域编码“1234567890”做映射。
DEL SUPISEGSERVAREACODE:SUPISEG="46001",AREACODE="1234567890"
` 
#### 查询基于SUPI号段的服务区域编码配置(SHOW SUPISEGSERVAREACODE) 
#### 查询基于SUPI号段的服务区域编码配置(SHOW SUPISEGSERVAREACODE) 
功能说明 
该命令用于查询基于SUPI号段的服务区域编码配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于配置SUPI号段。修改影响：无。数据来源：全网规划。默认值：无。配置原则：运营商规划好某个SUPI号段对应的服务区域编码后，操作员需要在该SUPI号段下配置所有的服务区域编码。AMF根据用户的SUPI号码和本命令配置的SUPI号段进行匹配，匹配原则是按最长号段进行匹配，一旦匹配到最长SUPI号段后，AMF会使用该SUPI号段下的服务区域编码配置，不会再尝试查询其他较短号段或者默认的服务区域编码配置。
areaCode|区域编码|参数可选性: 任选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。修改影响：无。数据来源：本端规划。默认值：无。配置原则：本参数的来源是通过ADD FORBIDDENAREACODE命令配置的参数“AREACODE“，必须先通过ADD FORBIDDENAREACODE命令预先配置。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：该参数用于配置SUPI号段。
areaCode|区域编码|参数可选性: 任选参数类型: 字符串参数范围: 1-128|参数作用：该参数用于配置服务区域编码，服务区域编码包含了一组跟踪区。
taGroupId|跟踪区组|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置服务区域编码对应的跟踪区组，跟踪区组包含一组跟踪区。
命令举例 
`
查询基于SUPI号段的服务区域编码配置。
SHOW SUPISEGSERVAREACODE
(No.1) : SHOW SUPISEGSERVAREACODE:
-----------------Namf_Communication_0----------------
SUPI号段     区域编码      跟踪区组
46001        1234567890    1
记录数：1
执行成功耗时: 0.188 秒
` 
## SMF服务区域配置 
## SMF服务区域配置 
背景知识 
如果现网没有部署NRF或者NRF故障，当用户移动，AMF决策是否需要插入或改变I-SMF时，AMF本地提供SMF服务区域配置，用于判断I-SMF的动作是插入、改变、还是删除。 
功能说明 
 本配置提供SMF FQDN对应的跟踪区组号，再根据“跟踪区组配置”获得对应的TA List。 
AMF比较当前TA是否在获取的TA范围内，如果当前TA在获取的TA范围内，则表示此SMF能服务当前TA，不需要插入I-SMF；如果当前TA不在获取的TA范围内，表示此SMF不能服务当前TA，需要插入I-SMF。 
子主题： 
### 新增SMF服务区域(ADD SMFSERVAREACFG) 
### 新增SMF服务区域(ADD SMFSERVAREACFG) 
功能说明 
如果AMF所在的5GC网络中没有部署NRF或者部署的NRF处于故障状态，当用户终端发生移动，AMF需要决策是否需要插入或改变I-SMF时，AMF需要在本地提供SMF服务区域配置。 
该命令用于配置SMF的FQDN（Fully Qualified Domain Name，全称域名）和跟踪区（Tracking Area，跟踪区域）组号的对应关系。 
注意事项 
该命令执行后立即生效。 
配置此命令前，需要确认操作员已经通过Namf_MP_0组件中[ADD TAGROUPCFG]命令配置了AMF管理的所有跟踪区组，并且已经通过Namf_MP_0组件中的[SHOW TAGROUPCFG]命令获取当前的所有跟踪区组的“TAGROUPID”。
一个SMF的FQDN最多配置10个跟踪区组号。 
最多可输入1024条记录。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的编号。修改影响：修改此参数，可以更改SMF服务区域配置的编号。数据来源：本端规划。默认值：无。配置原则：无。
FQDN|SMF FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：本参数用于设置SMF的FQDN。修改影响：修改此参数，可以更改SMF服务区域配置的FQDN。数据来源：整网规划。默认值：无。配置原则：无。
TAGRPID|跟踪区组号|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的FQDN关联的跟踪区组号。修改影响：修改此参数，可以更改SMF服务区域关联的跟踪区组号。数据来源：本端规划。默认值：无。配置原则：本参数的取值引用于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须通过ADD TAGROUPCFG命令预先配置，“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的编号。
FQDN|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：本参数用于设置SMF的FQDN。
TAGRPID|跟踪区组号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的FQDN关联的跟踪区组号。
命令举例 
`
新增一条SMF服务区域配置，编号为1，SMF FQDN为smf.jiangsu.nanjing.1，跟踪区组号为1。
ADD SMFSERVAREACFG:ID=1,FQDN="smf.jiangsu.nanjing.1",TAGRPID=1
` 
### 修改SMF服务区域(SET SMFSERVAREACFG) 
### 修改SMF服务区域(SET SMFSERVAREACFG) 
功能说明 
该命令用于修改SMF管理的跟踪区组号。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的编号。修改影响：修改此参数，可以更改SMF服务区域配置的编号。数据来源：本端规划。默认值：无。配置原则：无。
FQDN|SMF FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|参数作用：本参数用于设置SMF的FQDN。修改影响：修改此参数，可以更改SMF服务区域配置的FQDN。数据来源：整网规划。默认值：无。配置原则：无。
TAGRPID|跟踪区组号|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的FQDN关联的跟踪区组号。修改影响：修改此参数，可以更改SMF服务区域关联的跟踪区组号。数据来源：本端规划。默认值：无。配置原则：本参数的取值引用于Namf_MP_0组件中ADD TAGROUPCFG命令配置的参数“TAGROUPID”，必须通过ADD TAGROUPCFG命令预先配置，“TAGROUPID”是通过Namf_MP_0组件中SHOW TAGROUPCFG命令查询获取的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的编号。
FQDN|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：本参数用于设置SMF的FQDN。
TAGRPID|跟踪区组号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的FQDN关联的跟踪区组号。
命令举例 
`
修改一条SMF服务区域配置，编号为1，SMF FQDN为smf.jiangsu.nanjing.1，跟踪区组号为1。
SET SMFSERVAREACFG:ID=1,FQDN="smf.jiangsu.nanjing.1",TAGRPID=1
` 
### 删除SMF服务区域(DEL SMFSERVAREACFG) 
### 删除SMF服务区域(DEL SMFSERVAREACFG) 
功能说明 
该命令用于删除SMF管理的跟踪区组号。 
注意事项 
该命令执行后立即生效。 
该命令输入参数只能是编号或者SMF的FQDN，两者中的一种。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必须单选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的编号。修改影响：修改此参数，可以更改SMF服务区域配置的编号。数据来源：本端规划。默认值：无。配置原则：无。
FQDN|SMF FQDN|参数可选性: 必须单选参数类型: 字符串参数范围: 1-100|参数作用：本参数用于设置SMF的FQDN。修改影响：修改此参数，可以更改SMF服务区域配置的FQDN。数据来源：整网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的编号。
FQDN|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：本参数用于设置SMF的FQDN。
TAGRPID|跟踪区组号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的FQDN关联的跟踪区组号。
命令举例 
`
删除一条编号为1的SMF服务区域配置。
DEL SMFSERVAREACFG:ID=1
` 
### 查询SMF服务区域(SHOW SMFSERVAREACFG) 
### 查询SMF服务区域(SHOW SMFSERVAREACFG) 
功能说明 
该命令用于查询SMF管理的跟踪区组号。 
可以查询所有配置，也可以按SMF FQDN查询特定SMF的配置。 
注意事项 
该命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的编号。修改影响：修改此参数，可以更改SMF服务区域配置的编号。数据来源：本端规划。默认值：无。配置原则：无。
FQDN|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：本参数用于设置SMF的FQDN。修改影响：修改此参数，可以更改SMF服务区域配置的FQDN。数据来源：整网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的编号。
FQDN|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|参数作用：本参数用于设置SMF的FQDN。
TAGRPID|跟踪区组号|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：本参数用于设置SMF的FQDN关联的跟踪区组号。
命令举例 
`
查询所有SMF服务区域配置。
SHOW SMFSERVAREACFG
(No.1) : SHOW SMFSERVAREACFG:
-----------------Namf_Communication_0_A----------------
编号  SMF FQDN               跟踪区组号
1    smf.jiangsu.nanjing.1     1
记录数：1
` 
# 安全配置 
# 安全配置 
背景知识 
在5G网络中，网络侧和终端需要完成双向认证。 
 
网络侧需要对终端认证，以防止未经授权的终端接入网络 
 
终端也需要对网络侧进行认证，避免网络欺诈。 
 
同时，定义了NAS和AS的完整性保护和加密保护，提供了很好的安全性保护。 
功能说明 
本功能包括对UE进行鉴权的策略、支持的NAS信令的加密算法和完整性算法以及各个算法的优先级等信息。 
子主题： 
## 加密完保配置 
## 加密完保配置 
背景知识 
网络对用户鉴权通过以后，用户即为合法用户，可以接入网络，享受网络提供的服务。为了进一步提升合法用户使用网络服务的安全性，网络还可以对用户的信令和数据进行完整加密。网络可以根据终端支持的完保加密算法、网络支持的完保加密算法、灵活的优先级策略，来选择完保加密算法来进行完保加密处理。 
功能说明 
该功能用于设置AMF的加密完保配置，包括AMF所支持的完整性算法、加密算法及各算法对应的优先级。 
当AMF部署成功之后，需要使用此命令进行安全设置，之后AMF才能正常为UE提供服务。 
注意： AMF需要至少支持一种完整性算法，至少支持一种加密算法。 
子主题： 
### 修改加密完保配置(SET ENCRYANDINTEG) 
### 修改加密完保配置(SET ENCRYANDINTEG) 
功能说明 
该命令用于修改加密完保配置。 
注意事项 
 
本命令执行后，配置立即生效。 
 
至少需要配置支持一种加密算法。 
 
至少需要配置支持一种完保算法。 
 
本命令最多只能配置1条记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ea0|EA0算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持加密算法EA0。加密算法EA0为空算法。修改影响：无。数据来源：本端规划。默认值：0。配置原则：无。
ea0AlgPriority|EA0算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置EA0加密算法的优先级。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。优先级0最高，7最低。
ea1|EA1算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持加密算法EA1，取值及含义如下：不支持5G加密算法1。支持5G加密算法1。修改影响：无。数据来源：本端规划。默认值：支持5G加密算法1。配置原则：无。
ea1AlgPriority|EA1算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置EA1加密算法的优先级。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。优先级0最高，7最低。
ea2|EA2算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持加密算法EA2，取值及含义如下：不支持5G加密算法2。支持5G加密算法2。修改影响：无。数据来源：本端规划。默认值：不支持5G加密算法2。配置原则：无。
ea2AlgPriority|EA2算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置EA2加密算法的优先级。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。优先级0最高，7最低。
ea3|EA3算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持加密算法EA3，取值及含义如下：不支持5G加密算法3。支持5G加密算法3。修改影响：无。数据来源：本端规划。默认值：不支持5G加密算法3。配置原则：无。
ea3AlgPriority|EA3算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置EA3加密算法的优先级。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。优先级0最高，7最低。
ia1|IA1算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持5G完整性保护算法IA1，取值及含义如下：不支持5G完整性保护算法1。支持5G完整性保护算法1。修改影响：无。数据来源：本端规划。默认值：支持5G完整性保护算法1。配置原则：无。
ia1AlgPriority|IA1算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置IA1加密算法的优先级。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。优先级0最高，7最低。
ia2|IA2算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持完整性保护算法IA2，取值及含义如下：不支持5G完整性保护算法2。支持5G完整性保护算法2。修改影响：无。数据来源：本端规划。默认值：不支持5G完整性保护算法2。配置原则：无。
ia2AlgPriority|IA2算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置IA2加密算法的优先级。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。   优先级0最高，7最低。
ia3|IA3算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持完整性保护算法IA3，取值及含义如下：不支持5G完整性保护算法3。支持5G完整性保护算法3。修改影响：无。数据来源：本端规划。默认值：不支持5G完整性保护算法3。配置原则：无。
ia3AlgPriority|IA3算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置IA3加密算法的优先级。修改影响：无。数据来源：本端规划。默认值：1。配置原则：如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。优先级0最高，7最低。
命令举例 
`
设置AMF加密完保配置，加密算法为：”支持EA0，优先级7；“支持EAI，优先级6”、“支持EA2，优先级1”，“不支持EA3。完整性算法分别为：”支持IA1，优先级7“，” 支持IA2，优先级6“，”支持IA3，优先级1”。
SET ENCRYANDINTEG:EA0=EA0SUPPORT,EA0ALGPRIORITY=7,EA1=EA1SUPPORT,EA1ALGPRIORITY=6,EA2=EA2SUPPORT,EA2ALGPRIORITY=1,EA3=EA3NOSUPPORT,EA3ALGPRIORITY=1,IA1=IA1SUPPORT,IA1ALGPRIORITY=7,IA2=IA2SUPPORT,IA2ALGPRIORITY=6,IA3=IA3SUPPORT,IA3ALGPRIORITY=1
` 
### 查询加密完保配置(SHOW ENCRYANDINTEG) 
### 查询加密完保配置(SHOW ENCRYANDINTEG) 
功能说明 
该命令用于查询加密完保配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ea0|EA0算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持加密算法EA0。加密算法EA0为空算法。
ea0AlgPriority|EA0算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置EA0加密算法的优先级。
ea1|EA1算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持加密算法EA1，取值及含义如下：不支持5G加密算法1。支持5G加密算法1。
ea1AlgPriority|EA1算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置EA1加密算法的优先级。
ea2|EA2算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持加密算法EA2，取值及含义如下：不支持5G加密算法2。支持5G加密算法2。
ea2AlgPriority|EA2算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置EA2加密算法的优先级。
ea3|EA3算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持加密算法EA3，取值及含义如下：不支持5G加密算法3。支持5G加密算法3。
ea3AlgPriority|EA3算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置EA3加密算法的优先级。
ia1|IA1算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持5G完整性保护算法IA1，取值及含义如下：不支持5G完整性保护算法1。支持5G完整性保护算法1。
ia1AlgPriority|IA1算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置IA1加密算法的优先级。
ia2|IA2算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持完整性保护算法IA2，取值及含义如下：不支持5G完整性保护算法2。支持5G完整性保护算法2。
ia2AlgPriority|IA2算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置IA2加密算法的优先级。
ia3|IA3算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持完整性保护算法IA3，取值及含义如下：不支持5G完整性保护算法3。支持5G完整性保护算法3。
ia3AlgPriority|IA3算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|参数作用：该参数用于设置IA3加密算法的优先级。
命令举例 
`
查询AMF当前的安全配置。
SHOW ENCRYANDINTEG:
(No.1) : SHOW ENCRYANDINTEG:
-----------------Namf_Communication_0----------------
操作维护       EA0算法开关       EA0算法优先级 EA1算法开关     EA1算法优先级 EA2算法开关       EA2算法优先级 EA3算法开关       EA3算法优先级 IA1算法开关       IA1算法优先级 IA2算法开关         IA2算法优先级 IA3算法开关         IA3算法优先级 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           不支持5G加密算法0 1             支持5G加密算法1 1             不支持5G加密算法2 1             不支持5G加密算法3 1             支持5G完整性算法1 1             不支持5G完整性算法2 1             不支持5G完整性算法3 1             
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-01-08 15:36:50 耗时: 0.213 秒
` 
## 缺省鉴权策略配置 
## 缺省鉴权策略配置 
背景知识 
鉴权，即网络对用户身份进行识别认证，鉴定用户是否合法用户。对合法用户鉴权认证通过，接受合法用户接入网络，享受网络提供的服务。对非法用户鉴权认证不通过，拒绝非法用户接入网络。合法用户在鉴权过程中，网络侧还对用户提供了密钥，后续可以对用户信令和数据进行完整性保护和加密，进一步提升合法用户接入网络的安全性。 
功能说明 
AMF可以根据业务类型，提供配置策略，控制网络侧在用户发起的对应业务场景下，是否进行鉴权。 
AMF可以设置缺省的策略控制；也可以区分用户，针对不同SUPI号段，设置不同的鉴权策略，进行差异化的鉴权控制。 
本节点用于设置与SUPI号段无关的AMF缺省鉴权策略配置，当用户的SUPI号码在基于SUPI号段鉴权配置中没有配置时将使用此配置策略。 
子主题： 
### 修改缺省鉴权策略配置(SET DEFAUTHSTRATEGY) 
### 修改缺省鉴权策略配置(SET DEFAUTHSTRATEGY) 
功能说明 
该命令用于设置AMF的缺省鉴权策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-12|业务类型，即业务流程类型。AMF鉴权时根据业务流程和具体场景，将业务类型细分为13种，可以针对不同的业务类型，配置采取不同的鉴权策略。0：SUCI初始注册1：局内GUTI初始注册2：RAT内局间GUTI初始注册3：RAT间局间GUTI初始注册4：周期性注册更新5：局内移动性注册更新6：RAT内局间移动性注册更新7：RAT间局间移动性注册更新8：局内切换后的移动性注册更新9：RAT内局间切换后的移动性注册更新10：RAT间局间切换后的移动性注册更新11：业务请求12：去注册请求
authStrategy|鉴权策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SYSTEMDEFINE|该参数用于设置对应的业务流程下，所采用的鉴权策略。系统判断：表示相应流程根据系统判断进行鉴权控制。比如网络中不存在UE的安全上下文、网络对UE的NAS消息进行完整性检查失败，此时经过AMF系统判决，认为需要对UE发起鉴权过程。强制鉴权：表示相应流程每次都需要鉴权。强制不鉴权：表示相应流程每次都不需要鉴权。
命令举例 
`
设置AMF的SUCI初始注册流程的缺省鉴权策略为“强制鉴权”。
SET DEFAUTHSTRATEGY:SERVICETYPE="SUCIINITREG",AUTHSTRATEGY="FORCEAUTH"
` 
### 查询缺省鉴权策略配置(SHOW DEFAUTHSTRATEGY) 
### 查询缺省鉴权策略配置(SHOW DEFAUTHSTRATEGY) 
功能说明 
该命令用于查询AM的缺省鉴权策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-12|业务类型，即业务流程类型。AMF鉴权时根据业务流程和具体场景，将业务类型细分为13种，可以针对不同的业务类型，配置采取不同的鉴权策略。0：SUCI初始注册1：局内GUTI初始注册2：RAT内局间GUTI初始注册3：RAT间局间GUTI初始注册4：周期性注册更新5：局内移动性注册更新6：RAT内局间移动性注册更新7：RAT间局间移动性注册更新8：局内切换后的移动性注册更新9：RAT内局间切换后的移动性注册更新10：RAT间局间切换后的移动性注册更新11：业务请求12：去注册请求
输出参数说明 
标识|名称|类型|说明
---|---|---|---
serviceType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-12|业务类型，即业务流程类型。AMF鉴权时根据业务流程和具体场景，将业务类型细分为13种，可以针对不同的业务类型，配置采取不同的鉴权策略。0：SUCI初始注册1：局内GUTI初始注册2：RAT内局间GUTI初始注册3：RAT间局间GUTI初始注册4：周期性注册更新5：局内移动性注册更新6：RAT内局间移动性注册更新7：RAT间局间移动性注册更新8：局内切换后的移动性注册更新9：RAT内局间切换后的移动性注册更新10：RAT间局间切换后的移动性注册更新11：业务请求12：去注册请求
authStrategy|鉴权策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SYSTEMDEFINE|该参数用于设置对应的业务流程下，采用的具体鉴权策略。0：系统判断：表示相应流程根据系统判断进行鉴权控制。比如网络中不存在UE的安全上下文、网络对UE的NAS消息进行完整性检查失败，此时经过AMF系统判决，认为需要对UE发起鉴权过程。1：强制鉴权：表示相应流程每次都需要鉴权。2：强制不鉴权：表示相应流程每次都不需要鉴权。
命令举例 
`
查询AMF中业务类型为“SUCI初始注册”所对应的缺省鉴权策略。
SHOW DEFAUTHSTRATEGY:SERVICETYPE="SUCIINITREG"
(No.1) : SHOW DEFAUTHSTRATEGY:
-----------------Namf_Communication_0_A----------------
业务类型             鉴权策略
SUCI初始注册         系统判断
` 
## 基于SUPI号段的鉴权策略配置 
## 基于SUPI号段的鉴权策略配置 
背景知识 
鉴权，即网络对用户身份进行识别认证，鉴定用户是否合法用户。对合法用户鉴权认证通过，接受合法用户接入网络，享受网络提供的服务。对非法用户鉴权认证不通过，拒绝非法用户接入网络。合法用户在鉴权过程中，网络侧还对用户提供了密钥，后续可以对用户信令和数据进行完保和加密，进一步提升合法用户接入网络的安全性。 
功能说明 
AMF可以根据业务类型，提供配置策略，控制网络侧在用户发起的对应业务场景下，是否进行鉴权。 
AMF还能够设置缺省的策略控制，也能区分用户，针对不同SUPI号段，设置不同的鉴权策略，进行差异化的鉴权控制。 
本功能用于配置AMF基于SUPI号段的鉴权策略。当运营商需要根据SUPI号段设置不同的鉴权策略时使用该功能。 
当该功能配置成功后，AMF针对不同SUPI号段的用户采取对应鉴权策略。 
子主题： 
### 增加基于SUPI号段的鉴权策略配置(ADD SUPIAUTHSTRATEGY) 
### 增加基于SUPI号段的鉴权策略配置(ADD SUPIAUTHSTRATEGY) 
功能说明 
该命令用于修改基于SUPI号段的鉴权策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段。
serviceType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-12|业务类型，即业务流程类型。AMF鉴权时根据业务流程和具体场景，将业务类型细分为13种，可以针对不同的业务类型，配置采取不同的鉴权策略。0：SUCI初始注册1：局内GUTI初始注册2：RAT内局间GUTI初始注册3：RAT间局间GUTI初始注册4：周期性注册更新5：局内移动性注册更新6：RAT内局间移动性注册更新7：RAT间局间移动性注册更新8：局内切换后的移动性注册更新9：RAT内局间切换后的移动性注册更新10：RAT间局间切换后的移动性注册更新11：业务请求12：去注册请求
authStrategy|鉴权策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SYSTEMDEFINE|该参数用于设置对应的业务流程下，采用的具体鉴权策略。0：系统判断：表示相应流程根据系统判断进行鉴权控制。比如网络中不存在UE的安全上下文、网络对UE的NAS消息进行完整性检查失败，此时经过AMF系统判决，认为需要对UE发起鉴权过程。1：强制鉴权：表示相应流程每次都需要鉴权。2：强制不鉴权：表示相应流程每次都不需要鉴权。
命令举例 
`
增加一条基于SUPI号段的鉴权策略配置记录，SUPI号段为“460111”且流程为SUCI初始注册的鉴权策略为“强制鉴权”。
ADD SUPIAUTHSTRATEGY:SUPISEG="460111",SERVICETYPE="SUCIINITREG",AUTHSTRATEGY="FORCEAUTH"
` 
### 修改基于SUPI号段的鉴权策略配置(SET SUPIAUTHSTRATEGY) 
### 修改基于SUPI号段的鉴权策略配置(SET SUPIAUTHSTRATEGY) 
功能说明 
该命令用于修改基于SUPI号段的鉴权策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段。
serviceType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-12|业务类型，即业务流程类型。AMF鉴权时根据业务流程和具体场景，将业务类型细分为13种，可以针对不同的业务类型，配置采取不同的鉴权策略。0：SUCI初始注册1：局内GUTI初始注册2：RAT内局间GUTI初始注册3：RAT间局间GUTI初始注册4：周期性注册更新5：局内移动性注册更新6：RAT内局间移动性注册更新7：RAT间局间移动性注册更新8：局内切换后的移动性注册更新9：RAT内局间切换后的移动性注册更新10：RAT间局间切换后的移动性注册更新11：业务请求12：去注册请求
authStrategy|鉴权策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SYSTEMDEFINE|该参数用于设置对应的业务流程下，采用的具体鉴权策略。0：系统判断：表示相应流程根据系统判断进行鉴权控制。比如网络中不存在UE的安全上下文、网络对UE的NAS消息进行完整性检查失败，此时经过AMF系统判决，认为需要对UE发起鉴权过程。1：强制鉴权：表示相应流程每次都需要鉴权。2：强制不鉴权：表示相应流程每次都不需要鉴权。
命令举例 
`
修改一条基于SUPI号段的鉴权策略配置记录，SUPI号段为“460111”且流程为SUCI初始注册的鉴权策略为“强制鉴权”。
SET SUPIAUTHSTRATEGY:SUPISEG="460111",SERVICETYPE="SUCIINITREG",AUTHSTRATEGY="FORCEAUTH"
` 
### 删除基于SUPI号段的鉴权策略配置(DEL SUPIAUTHSTRATEGY) 
### 删除基于SUPI号段的鉴权策略配置(DEL SUPIAUTHSTRATEGY) 
功能说明 
该命令用于删除基于SUPI号段的鉴权策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段。
serviceType|业务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-12|业务类型，即业务流程类型。AMF鉴权时根据业务流程和具体场景，将业务类型细分为13种，可以针对不同的业务类型，配置采取不同的鉴权策略。0：SUCI初始注册1：局内GUTI初始注册2：RAT内局间GUTI初始注册3：RAT间局间GUTI初始注册4：周期性注册更新5：局内移动性注册更新6：RAT内局间移动性注册更新7：RAT间局间移动性注册更新8：局内切换后的移动性注册更新9：RAT内局间切换后的移动性注册更新10：RAT间局间切换后的移动性注册更新11：业务请求12：去注册请求
命令举例 
`
删除基于SUPI号段的鉴权策略配置记录，删除SUPI号段为“460111”且流程为SUCI初始注册的鉴权策略。
DEL SUPIAUTHSTRATEGY:SUPISEG="460111",SERVICETYPE="SUCIINITREG"
` 
### 查询基于SUPI号段的鉴权策略配置(SHOW SUPIAUTHSTRATEGY) 
### 查询基于SUPI号段的鉴权策略配置(SHOW SUPIAUTHSTRATEGY) 
功能说明 
该命令用于查询基于SUPI号段的鉴权策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段。
serviceType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-12|业务类型，即业务流程类型。AMF鉴权时根据业务流程和具体场景，将业务类型细分为13种，可以针对不同的业务类型，配置采取不同的鉴权策略。0：SUCI初始注册1：局内GUTI初始注册2：RAT内局间GUTI初始注册3：RAT间局间GUTI初始注册4：周期性注册更新5：局内移动性注册更新6：RAT内局间移动性注册更新7：RAT间局间移动性注册更新8：局内切换后的移动性注册更新9：RAT内局间切换后的移动性注册更新10：RAT间局间切换后的移动性注册更新11：业务请求12：去注册请求
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSeg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于设置SUPI号段。
serviceType|业务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-12|业务类型，即业务流程类型。AMF鉴权时根据业务流程和具体场景，将业务类型细分为13种，可以针对不同的业务类型，配置采取不同的鉴权策略。0：SUCI初始注册1：局内GUTI初始注册2：RAT内局间GUTI初始注册3：RAT间局间GUTI初始注册4：周期性注册更新5：局内移动性注册更新6：RAT内局间移动性注册更新7：RAT间局间移动性注册更新8：局内切换后的移动性注册更新9：RAT内局间切换后的移动性注册更新10：RAT间局间切换后的移动性注册更新11：业务请求12：去注册请求
authStrategy|鉴权策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: SYSTEMDEFINE|该参数用于设置对应的业务流程下，采用的具体鉴权策略。0：系统判断：表示相应流程根据系统判断进行鉴权控制。比如网络中不存在UE的安全上下文、网络对UE的NAS消息进行完整性检查失败，此时经过AMF系统判决，认为需要对UE发起鉴权过程。1：强制鉴权：表示相应流程每次都需要鉴权。2：强制不鉴权：表示相应流程每次都不需要鉴权。
命令举例 
`
查询所有基于SUPI号段的鉴权策略配置记录。
SHOW SUPIAUTHSTRATEGY
(No.1) : SHOW SUPIAUTHSTRATEGY:
-----------------Namf_Communication_0_A----------------
SUPI号段     业务类型                           鉴权策略
460111       Initial Registration With SUCI     Force Authentication
` 
## PEI检查配置 
## PEI检查配置 
背景知识 
PEI(Permanent Equipment Identifier)，就是终端的永久设备标识。PEI检查，即网络对接入的终端设备进行合法性检查，确认终端的合法性。对合法终端检查通过，接受接入网络。对非法终端检查不通过，拒绝接入网络。通过PEI检查，可以增加网络安全性，避免非法终端接入网络，还可以追踪被盗终端，辅助找回用户的被盗终端。 
功能说明 
本节点用于配置PEI检查功能的一些策略。如果需要开通PEI检查功能，需要先根据现网情况规划好这些策略，再进行配置。主要有三个部分： 
 
AMF是否进行PEI检查，包括AMF是否开启PEI检查功能，AMF在哪些流程进行PEI检查。 
 
AMF发送给5G-EIR网元携带的参数，包括PEI是携带IMEI还是IMEISV，是否携带SUPI，是否携带GPSI。 
 
AMF收到5G-EIR网元返回的检查结果的处理，包括是否限制灰名单，是否限制黑名单，是否限制未知设备，返回其他失败是否限制接入，超时无响应是否限制接入，发现5G-EIR失败是否限制接入，是否上报灰名单/黑名单告警。 
 
子主题： 
### 修改PEI检查配置(SET PEICHECKCONFIG) 
### 修改PEI检查配置(SET PEICHECKCONFIG) 
功能说明 
该命令用于修改PEI检查的配置。 
PEI(Permanent Equipment Identifier)，是终端的永久设备标识。PEI检查，即网络对接入的终端设备进行合法性检查，确认终端的合法性。对合法终端检查通过，接受接入网络。对非法终端检查不通过，拒绝接入网络。通过PEI检查，可以增加网络安全性，避免非法终端接入网络，还可以追踪被盗终端，辅助找回用户的被盗终端。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
support|AMF是否支持PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: SUPPORT_NO|该参数用于设置是否开启PEI检查功能。0-不支持1-支持修改影响：此参数的修改会影响是否开启PEI检查功能。数据来源：本端规划。默认值：0-不支持。配置原则： 1.当选择"支持"的时候，必须同时设置“AMF移动性配置”配置中的“是否AMF是否获取IMEI(SV)”参数。
chkinitreg|初始注册流程是否进行PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: INITREG_YES|该参数用于设置是否在初始注册流程中进行PEI检查。0-否1-是修改影响：此参数的修改会影响用户发起初始注册流程时，AMF是否进行PEI检查。数据来源：本端规划。默认值：1-是。配置原则：无。
chkinterregupdate|局间注册更新流程是否进行PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: INTERREGUPDATE_YES|该参数用于设置是否在局间注册更新流程中进行PEI检查。0-否1-是修改影响：此参数的修改会影响用户发起局间注册更新流程时，AMF是否进行PEI检查。数据来源：本端规划。默认值：1-是。配置原则：无。
chkintraregupdate|局内注册更新流程是否进行PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: INTRAREGUPDATE_NO|该参数用于设置是否在局内注册更新流程中进行PEI检查。0-否1-是修改影响：此参数的修改会影响用户发起局内注册更新流程时，AMF是否进行PEI检查。数据来源：本端规划。默认值：0-否。配置原则：无。
carryimeisv|AMF携带IMEI还是IMEISV给EIR|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: CARRYIMEI|该参数用于设置AMF发送ME identity check请求消息给EIR时，是携带IMEI还是携带IMEISV。0-携带IMEI1-携带IMEISV修改影响：此参数的修改会影响AMF发送ME identity check请求消息给EIR时，是携带IMEI还是IMEISV。数据来源：本端规划。默认值：0-携带IMEI。配置原则：无。
carrysupi|AMF是否携带SUPI给EIR|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: CARRYSUPI_YES|该参数用于设置AMF发送ME identity check请求消息给EIR时，是否携带SUPI。0-否1-是修改影响：此参数的修改会影响AMF发送ME identity check请求消息给EIR时，是否携带SUPI。数据来源：本端规划。默认值：1-是。配置原则：无。
carrygpsi|AMF是否携GPSI给EIR|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: CARRYGPSI_NO|该参数用于设置AMF发送ME identity check请求消息给EIR时，是否携带GPSI，当EIR不支持GPSI时，不要携带该参数。0-否1-是修改影响：此参数的修改会影响AMF发送ME identity check请求消息给EIR时，是否携带GPSI。数据来源：本端规划。默认值：0-否。配置原则：无。
chkaftersubdata|AMF是否在获取签约数据之后进行PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: AFTERSUBDATA_NO|该参数用于设置AMF是否在获取用户的签约数据之后，再发起ME identity check流程。0-否1-是修改影响：此参数的修改会影响注册流程中AMF发起PEI检查的时机，3GPP TS 29.511协议上规定ME identity check流程是在鉴权流程之后发起，但是请求消息中GPSI参数需要在获取签约数据后才能得到，所以通过该参数控制AMF发起PEI检查的时机。数据来源：本端规划。默认值：0-否。配置原则：无。
limitblack|AMF是否限制黑名单设备接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: BLACKLIST_YES|该参数用于设置当EIR返回用户的设备状态为黑名单时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响用户的设备状态为黑名单时，AMF是否限制用户接入。数据来源：本端规划。默认值：1-是。配置原则：无。
limitgrey|AMF是否限制灰名单设备接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: GREYLIST_NO|该参数用于设置当EIR返回用户的设备状态为灰名单时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响用户的设备状态为灰名单时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
limitunknown|AMF是否限制未知设备接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: UNKOWNEQUIP_YES|该参数用于设置当EIR返回用户的设备状态为未知设备时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响用户的设备状态为未知设备时，AMF是否限制用户接入。数据来源：本端规划。默认值：1-是。配置原则：无。
limiteirreturnfail|EIR返回失败时AMF是否限制接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: EIRRETFAIL_NO|该参数用于设置当EIR返回失败的响应消息时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响EIR返回失败的响应消息时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
limiteirnorsp|EIR超时无响应时AMF是否限制接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: EIRNORSP_NO|该参数用于设置当EIR不返回响应消息时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响EIR不返回响应消息时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
limitdisceirfail|发现EIR失败时AMF是否限制接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: DISCEIRFAIL_NO|该参数用于设置AMF发现EIR失败时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响AMF发现EIR失败时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
limitgetimeisvfail|向UE获取IMEI(SV)失败时AMF是否限制接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: GETIMEISVFAIL_NO|该参数用于设置AMF向用户获取IMEISV失败时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响AMF向用户获取IMEISV失败时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
sendstatealarm|AMF是否发送用户灰/黑名单状态告警通知|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: NOTSENDALARM|该参数用于设置当EIR返回用户的设备状态为灰名单或黑名单时，AMF是否发送告警通知。0-不发送告警1-发送灰名单告警2-发送黑名单告警3-发送灰名单和黑名单告警修改影响：此参数的修改会影响EIR返回用户的设备状态为灰名单或黑名单时，AMF是否上报报警通知。数据来源：本端规划。默认值：0-不发送告警。配置原则：无。
命令举例 
`
修改PEI检查配置。
SET PEICHECKCONFIG:
(No.1) : SET PEICHECKCONFIG:SUPPORT="SUPPORT_YES"
-----------------Namf_Communication_0----------------
执行成功耗时: 1.135 秒
` 
### 查询PEI检查配置(SHOW PEICHECKCONFIG) 
### 查询PEI检查配置(SHOW PEICHECKCONFIG) 
功能说明 
该命令用于查询PEI检查的配置。 
PEI(Permanent Equipment Identifier)，是终端的永久设备标识。PEI检查，即网络对接入的终端设备进行合法性检查，确认终端的合法性。对合法终端检查通过，接受接入网络。对非法终端检查不通过，拒绝接入网络。通过PEI检查，可以增加网络安全性，避免非法终端接入网络，还可以追踪被盗终端，辅助找回用户的被盗终端。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
support|AMF是否支持PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: SUPPORT_NO|该参数用于设置是否开启PEI检查功能。0-不支持1-支持修改影响：此参数的修改会影响是否开启PEI检查功能。数据来源：本端规划。默认值：0-不支持。配置原则： 1.当选择"支持"的时候，必须同时设置“AMF移动性配置”配置中的“是否AMF是否获取IMEI(SV)”参数。
chkinitreg|初始注册流程是否进行PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: INITREG_YES|该参数用于设置是否在初始注册流程中进行PEI检查。0-否1-是修改影响：此参数的修改会影响用户发起初始注册流程时，AMF是否进行PEI检查。数据来源：本端规划。默认值：1-是。配置原则：无。
chkinterregupdate|局间注册更新流程是否进行PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: INTERREGUPDATE_YES|该参数用于设置是否在局间注册更新流程中进行PEI检查。0-否1-是修改影响：此参数的修改会影响用户发起局间注册更新流程时，AMF是否进行PEI检查。数据来源：本端规划。默认值：1-是。配置原则：无。
chkintraregupdate|局内注册更新流程是否进行PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: INTRAREGUPDATE_NO|该参数用于设置是否在局内注册更新流程中进行PEI检查。0-否1-是修改影响：此参数的修改会影响用户发起局内注册更新流程时，AMF是否进行PEI检查。数据来源：本端规划。默认值：0-否。配置原则：无。
carryimeisv|AMF携带IMEI还是IMEISV给EIR|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: CARRYIMEI|该参数用于设置AMF发送ME identity check请求消息给EIR时，是携带IMEI还是携带IMEISV。0-携带IMEI1-携带IMEISV修改影响：此参数的修改会影响AMF发送ME identity check请求消息给EIR时，是携带IMEI还是IMEISV。数据来源：本端规划。默认值：0-携带IMEI。配置原则：无。
carrysupi|AMF是否携带SUPI给EIR|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: CARRYSUPI_YES|该参数用于设置AMF发送ME identity check请求消息给EIR时，是否携带SUPI。0-否1-是修改影响：此参数的修改会影响AMF发送ME identity check请求消息给EIR时，是否携带SUPI。数据来源：本端规划。默认值：1-是。配置原则：无。
carrygpsi|AMF是否携GPSI给EIR|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: CARRYGPSI_NO|该参数用于设置AMF发送ME identity check请求消息给EIR时，是否携带GPSI，当EIR不支持GPSI时，不要携带该参数。0-否1-是修改影响：此参数的修改会影响AMF发送ME identity check请求消息给EIR时，是否携带GPSI。数据来源：本端规划。默认值：0-否。配置原则：无。
chkaftersubdata|AMF是否在获取签约数据之后进行PEI检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: AFTERSUBDATA_NO|该参数用于设置AMF是否在获取用户的签约数据之后，再发起ME identity check流程。0-否1-是修改影响：此参数的修改会影响注册流程中AMF发起PEI检查的时机，3GPP TS 29.511协议上规定ME identity check流程是在鉴权流程之后发起，但是请求消息中GPSI参数需要在获取签约数据后才能得到，所以通过该参数控制AMF发起PEI检查的时机。数据来源：本端规划。默认值：0-否。配置原则：无。
limitblack|AMF是否限制黑名单设备接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: BLACKLIST_YES|该参数用于设置当EIR返回用户的设备状态为黑名单时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响用户的设备状态为黑名单时，AMF是否限制用户接入。数据来源：本端规划。默认值：1-是。配置原则：无。
limitgrey|AMF是否限制灰名单设备接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: GREYLIST_NO|该参数用于设置当EIR返回用户的设备状态为灰名单时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响用户的设备状态为灰名单时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
limitunknown|AMF是否限制未知设备接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: UNKOWNEQUIP_YES|该参数用于设置当EIR返回用户的设备状态为未知设备时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响用户的设备状态为未知设备时，AMF是否限制用户接入。数据来源：本端规划。默认值：1-是。配置原则：无。
limiteirreturnfail|EIR返回失败时AMF是否限制接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: EIRRETFAIL_NO|该参数用于设置当EIR返回失败的响应消息时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响EIR返回失败的响应消息时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
limiteirnorsp|EIR超时无响应时AMF是否限制接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: EIRNORSP_NO|该参数用于设置当EIR不返回响应消息时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响EIR不返回响应消息时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
limitdisceirfail|发现EIR失败时AMF是否限制接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: DISCEIRFAIL_NO|该参数用于设置AMF发现EIR失败时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响AMF发现EIR失败时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
limitgetimeisvfail|向UE获取IMEI(SV)失败时AMF是否限制接入|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: GETIMEISVFAIL_NO|该参数用于设置AMF向用户获取IMEISV失败时，AMF是否限制用户接入。0-否1-是修改影响：此参数的修改会影响AMF向用户获取IMEISV失败时，AMF是否限制用户接入。数据来源：本端规划。默认值：0-否。配置原则：无。
sendstatealarm|AMF是否发送用户灰/黑名单状态告警通知|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: NOTSENDALARM|该参数用于设置当EIR返回用户的设备状态为灰名单或黑名单时，AMF是否发送告警通知。0-不发送告警1-发送灰名单告警2-发送黑名单告警3-发送灰名单和黑名单告警修改影响：此参数的修改会影响EIR返回用户的设备状态为灰名单或黑名单时，AMF是否上报报警通知。数据来源：本端规划。默认值：0-不发送告警。配置原则：无。
命令举例 
`
查询PEI检查配置。
SHOW PEICHECKCONFIG:
(No.1) : SHOW PEICHECKCONFIG:
-----------------Namf_Communication_0----------------
AMF是否支持PEI检查    初始注册流程是否进行PEI检查     局间注册更新流程是否进行PEI检查  局内注册更新流程是否进行PEI检查  AMF携带IMEI还是IMEISV给EIR  AMF是否携带SUPI给EIR  AMF是否携GPSI给EIR  AMF是否在获取签约数据之后进行PEI检查  AMF是否限制黑名单设备接入  AMF是否限制灰名单设备接入  AMF是否限制未知设备接入   EIR返回失败时AMF是否限制接入  EIR超时无响应时AMF是否限制接入 发现EIR失败时AMF是否限制接入  向UE获取IMEI(SV)失败时AMF是否限制接入  AMF是否发送用户灰/黑名单状态告警通知
Not support     Yes     Yes     No     Carry IMEI    Carry    Not Carry     No    Yes    No   Yes    No    No   No   No   Not Send Alarm
记录数：1
执行成功开始时间:2020-06-23 10:18:22 耗时: 0.353 秒
` 
# AM和UE策略配置 
# AM和UE策略配置 
背景知识 
在5GC网络中，PCF可以根据终端用户已接入的业务，执行以下功能。 
 
动态调整终端的接入和移动性管理（Access和Mobility）策略控制，简称AM策略控制 
 
动态的下发UE策略 
 
N15接口是AMF和PCF之间的接口，用于AMF和PCF之间的消息交互。 
AMF可以通过N15接口向PCF请求AM策略控制，或上报AM策略控制相关事件。PCF可以通过N15接口向AMF推送最新的AM策略，并订阅AM策略控制相关事件。 
功能说明 
本功能包括了与N15接口相关功能的配置，包括AM策略和UE策略。 
子主题： 
## 向PCF获取AM和UE策略的策略配置 
## 向PCF获取AM和UE策略的策略配置 
背景知识 
在5GC网络中，PCF可以根据终端用户已接入的业务，执行以下功能。 
 
动态调整终端的接入和移动性管理（Access和Mobility）策略控制，简称AM策略控制 
 
动态的下发UE策略 
 
功能说明 
可以根据多个维度，控制AMF是否向PCF获取用户AM策略和UE策略。 
子主题： 
### 缺省向PCF获取AM和UE策略的策略配置 
### 缺省向PCF获取AM和UE策略的策略配置 
背景知识 
在5GC中，PCF可以根据用户已接入的业务，既动态调整用户的接入和移动性管理策略，又可以动态的下发UE策略。 
功能说明 
本功能用于在全局维度控制是否向PCF获取用户AM策略和UE策略。 
子主题： 
#### 修改缺省向PCF获取AM策略和UE策略的策略配置(SET DEFASUPTPCFPOLICY) 
#### 修改缺省向PCF获取AM策略和UE策略的策略配置(SET DEFASUPTPCFPOLICY) 
功能说明 
该命令用于设置AMF未基于号段和切片向PCF获取AM策略和UE策略的缺省情况下，是否向PCF获取AM策略和UE策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ifAmPolicy|向PCF获取AM策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMPOLICYSUPT|该参数用于设置AMF未基于号段和切片向PCF获取AM策略和UE策略的缺省情况下，是否向PCF获取AM策略。
ifUePolicy|向PCF获取UE策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: UEPOLICYSUPT|该参数用于设置AMF未基于号段和切片向PCF获取AM策略和UE策略的缺省情况下，是否向PCF获取UE策略。
命令举例 
`
设置AMF未基于号段和切片向PCF获取AM策略和UE策略的缺省情况下，不支持向PCF获取UE策略。
SET DEFASUPTPCFPOLICY:IFUEPOLICY="UEPOLICYNOTSUPT"
` 
#### 查询缺省向PCF获取AM策略和UE策略的策略配置(SHOW DEFASUPTPCFPOLICY) 
#### 查询缺省向PCF获取AM策略和UE策略的策略配置(SHOW DEFASUPTPCFPOLICY) 
功能说明 
该命令用于查询AMF未基于号段和切片向PCF获取AM策略和UE策略的缺省情况下，是否向PCF获取AM策略和UE策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ifAmPolicy|向PCF获取AM策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMPOLICYSUPT|该参数用于设置AMF未基于号段和切片向PCF获取AM策略和UE策略的缺省情况下，是否向PCF获取AM策略。
ifUePolicy|向PCF获取UE策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: UEPOLICYSUPT|该参数用于设置AMF未基于号段和切片向PCF获取AM策略和UE策略的缺省情况下，是否向PCF获取UE策略。
命令举例 
`
查询AMF未基于号段和切片向PCF获取AM策略和UE策略的缺省情况下，是否向PCF获取AM策略和UE策略。
SHOW DEFASUPTPCFPOLICY
(No.4) : SHOW DEFASUPTPCFPOLICY:
-----------------Namf_Communication_0----------------
向PCF获取AM策略    向PCF获取UE策略
支持AM策略         不支持UE策略
记录数：1
命令执行成功（耗时 0.031 秒）。
` 
### 基于号段和切片向PCF获取AM和UE策略的策略配置 
### 基于号段和切片向PCF获取AM和UE策略的策略配置 
背景知识 
在5GC中，PCF可以根据用户已接入的业务，既动态调整用户的接入和移动性管理策略，又可以动态的下发UE策略。 
功能说明 
本功能用于在号段和切片信息维度控制是否向PCF获取用户AM策略和UE策略。 
子主题： 
#### 新增基于号段和切片向PCF获取AM策略和UE策略的策略配置(ADD SEGSLISUPTPCFPOLICY) 
#### 新增基于号段和切片向PCF获取AM策略和UE策略的策略配置(ADD SEGSLISUPTPCFPOLICY) 
功能说明 
该命令用于增加特定的号段和切片下，AMF是否向PCF获取AM策略和UE策略的策略配置。 
注意事项 
用户号段类型、用户号段和NSSAI Profile标识共同组成唯一标示，用来确认特定号段和切片下的策略配置。如果不希望匹配号段，请将用户号段类型设置为不匹配用户号段，将用户号段设置为“NULL”；如果不希望匹配切片，请将NSSAI Profile标识设置为无效值0。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
segmentType|用户号段类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: GPSISEGMENT|该参数用于设置需要被匹配的用户号段类型。用户号段类型可以为SUPI或者GPSI，也可以不匹配用户号段。
userSegment|用户号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16默认值: NULL|该参数用于设置需要被匹配的用户号段。如果不需要匹配用户号段，请设置为“NULL”。
nssaiProfileId|NSSAI Profile标识|参数可选性: 必选参数类型: 数字参数范围: 0-2048|该参数用于标识NSSAI Profile中的一个S-NSSAI，NSSAI Profile内唯一，用于被基于号段和切片向PCF获取AM策略和UE策略的策略配置引用。如果不需要匹配切片，请设置为无效值0。
ifAmPolicy|向PCF获取AM策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMPOLICYSUPT|该参数用于设置基于特定的号段和切片下，AMF是否向PCF获取AM策略。
ifUePolicy|向PCF获取UE策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: UEPOLICYSUPT|该参数用于设置基于特定的号段和切片下，AMF是否向PCF获取UE策略。
命令举例 
`
增加向PCF获取AM策略和UE策略的策略配置：不匹配用户号段，如果用户协商的Allowed NSSAI包含NSSAI Profile标识为1的S-NSSAI，则支持AM策略，不支持UE策略。
ADD SEGSLISUPTPCFPOLICY:SEGMENTTYPE="GPSISEGMENT",USERSEGMENT="NULL",NSSAIPROFILEID=1,IFAMPOLICY="AMPOLICYSUPT",IFUEPOLICY="UEPOLICYNOTSUPT"
` 
#### 修改基于号段和切片向PCF获取AM策略和UE策略的策略配置(SET SEGSLISUPTPCFPOLICY) 
#### 修改基于号段和切片向PCF获取AM策略和UE策略的策略配置(SET SEGSLISUPTPCFPOLICY) 
功能说明 
该命令用于修改特定的号段和切片下，AMF是否向PCF获取AM策略和UE策略的策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
segmentType|用户号段类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: GPSISEGMENT|该参数用于设置需要被匹配的用户号段类型。用户号段类型可以为SUPI或者GPSI，也可以不匹配用户号段。
userSegment|用户号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16默认值: NULL|该参数用于设置需要被匹配的用户号段。如果不需要匹配用户号段，请设置为“NULL”。
nssaiProfileId|NSSAI Profile标识|参数可选性: 任选参数类型: 数字参数范围: 0-2048|该参数用于标识NSSAI Profile中的一个S-NSSAI，NSSAI Profile内唯一，用于被基于号段和切片向PCF获取AM策略和UE策略的策略配置引用。如果不需要匹配切片，请设置为无效值0。
ifAmPolicy|向PCF获取AM策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMPOLICYSUPT|该参数用于设置基于特定的号段和切片下，AMF是否向PCF获取AM策略。
ifUePolicy|向PCF获取UE策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: UEPOLICYSUPT|该参数用于设置基于特定的号段和切片下，AMF是否向PCF获取UE策略。
命令举例 
`
修改向PCF获取AM策略和UE策略的策略配置：不匹配用户号段，如果用户协商的Allowed NSSAI包含NSSAI Profile标识为1的S-NSSAI，则支持UE策略。
SET SEGSLISUPTPCFPOLICY:SEGMENTTYPE="GPSISEGMENT",USERSEGMENT="NULL",NSSAIPROFILEID=1,IFUEPOLICY="UEPOLICYSUPT"
` 
#### 删除基于号段和切片向PCF获取AM策略和UE策略的策略配置(DEL SEGSLISUPTPCFPOLICY) 
#### 删除基于号段和切片向PCF获取AM策略和UE策略的策略配置(DEL SEGSLISUPTPCFPOLICY) 
功能说明 
该命令用于删除特定的号段和切片下，AMF是否向PCF获取AM策略和UE策略的策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
segmentType|用户号段类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: GPSISEGMENT|该参数用于设置需要被匹配的用户号段类型。用户号段类型可以为SUPI或者GPSI，也可以不匹配用户号段。
userSegment|用户号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16默认值: NULL|该参数用于设置需要被匹配的用户号段。如果不需要匹配用户号段，请设置为“NULL”。
nssaiProfileId|NSSAI Profile标识|参数可选性: 必选参数类型: 数字参数范围: 0-2048|该参数用于标识NSSAI Profile中的一个S-NSSAI，NSSAI Profile内唯一，用于被基于号段和切片向PCF获取AM策略和UE策略的策略配置引用。如果不需要匹配切片，请设置为无效值0。
命令举例 
`
删除向PCF获取AM策略和UE策略的策略配置：不匹配用户号段，如果用户协商的Allowed NSSAI包含NSSAI Profile标识为1的S-NSSAI，不再对是否支持AM策略和UE策略做决策。
DEL SEGSLISUPTPCFPOLICY:SEGMENTTYPE="GPSISEGMENT",USERSEGMENT="NULL",NSSAIPROFILEID=1
` 
#### 查询基于号段和切片向PCF获取AM策略和UE策略的策略配置(SHOW SEGSLISUPTPCFPOLICY) 
#### 查询基于号段和切片向PCF获取AM策略和UE策略的策略配置(SHOW SEGSLISUPTPCFPOLICY) 
功能说明 
该命令用于查询不同号段和切片下，AMF是否向PCF获取AM策略和UE策略的策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
segmentType|用户号段类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: GPSISEGMENT|该参数用于设置需要被匹配的用户号段类型。用户号段类型可以为SUPI或者GPSI，也可以不匹配用户号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
segmentType|用户号段类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: GPSISEGMENT|该参数用于设置需要被匹配的用户号段类型。用户号段类型可以为SUPI或者GPSI，也可以不匹配用户号段。
userSegment|用户号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16默认值: NULL|该参数用于设置需要被匹配的用户号段。如果不需要匹配用户号段，请设置为“NULL”。
nssaiProfileId|NSSAI Profile标识|参数可选性: 任选参数类型: 数字参数范围: 0-2048|该参数用于标识NSSAI Profile中的一个S-NSSAI，NSSAI Profile内唯一，用于被基于号段和切片向PCF获取AM策略和UE策略的策略配置引用。如果不需要匹配切片，请设置为无效值0。
ifAmPolicy|向PCF获取AM策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMPOLICYSUPT|该参数用于设置基于特定的号段和切片下，AMF是否向PCF获取AM策略。
ifUePolicy|向PCF获取UE策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: UEPOLICYSUPT|该参数用于设置基于特定的号段和切片下，AMF是否向PCF获取UE策略。
命令举例 
`
查询不同号段和切片下，AMF是否向PCF获取AM策略和UE策略的策略配置。
SHOW SEGSLISUPTPCFPOLICY:
(No.1) : SHOW SEGSLISUPTPCFPOLICY:
-----------------Namf_Communication_0----------------
操作维护       用户号段类型 用户号段 NSSAI Profile标识 向PCF获取AM策略 向PCF获取UE策略
---------------------------------------------------------------------------------------
复制 修改 删除 GPSI         NULL     1                 支持AM策略      不支持UE策略
复制 修改 删除 SUPI         46011    0                 不支持AM策略    支持UE策略
---------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-07-19 19:45:55 耗时: 0.139 秒
` 
## 局间流程PCF策略配置 
## 局间流程PCF策略配置 
背景知识 
在AMF重定位场景下，Old AMF可以基于Old AMF和New AM是否属于同一个PLMN，来决定是否向New AMF传递AM（Access&Mobility）策略和UE策略关联信息，包含PCF ID，AM策略及UE策略关联URI以及策略控制触发器。 
基于AMF配置的本地策略，New AMF可以通过两种方式处理在AMF重定位后的AM策略和UE策略关联： 
 
不使用Old AMF带回来的AM策略信息，选择新的PCF并与新的PCF重新建立AM策略和UE策略关联。 
 
使用Old AMF带回来的AM策略信息，直接用AM策略和UE策略关联URI向老的PCF发起策略关联建立。 
 
具体流程参见23502协议的“4.16.1.2 AM Policy Association Establishment with new Selected PCF”和“4.16.2.1.2 AM Policy Association Modification with old PCF during AMF relocation”。 
功能说明 
本功能用于设置AMF重定位情况下（包含局间注册更新、局间切换、AMF重分配三种场景）AM策略和UE策略关联处理的相关配置，包含Old AMF是否携带PCF信息给新AMF以及新AMF是否重选PCF。 
子主题： 
### 修改局间流程PCF策略配置(SET INTERAMFPCFCFG) 
### 修改局间流程PCF策略配置(SET INTERAMFPCFCFG) 
功能说明 
该命令用于设置的AMF重定位情况下（包含局间注册更新、局间切换、AMF重分配三种场景）AM策略及UE策略处理的相关配置，Old AMF是否携带PCF信息给New AMF以及New AMF是否重选PCF的本地策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
oldAmfcarryPcfInfo|老局携带PCF信息策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BASEONPLMN|该参数用于设置在AMF发生重定位的场景下，Old AMF是否携带PCF信息给New AMF。不携带PCF信息：OldAMF不需要携带PCF信息给New AMF。携带PCF信息：Old AMF需要携带PCF信息给New AMF。基于PLMN携带PCF信息：如果Old AMF和New AMF不属于同一PLMN，则Old AMF不需要携带PCF信息给New AMF。如果Old AMF和New AMF属于同一PLMN，则Old AMF需要携带PCF信息给New AMF。
newAmfreselectPcf|新局重选PCF策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BASEONPLMN|该参数用于设置在AMF发生重定位的场景下，New AMF是否重新选择新的PCF，重新建立AM策略关联。不重选PCF：New AMF不需要重选PCF，使用Old AMF带回来的AM策略信息重选PCF：则New AMF不使用Old AMF带回来的AM策略信息，选择新的PCF并与新的PCF重新建立AM策略关联。基于PLMN重选PCF：New AMF如果和Old AMF在同一PLMN，则New AMF不需要重选PCF，使用Old AMF带回来的AM策略信息。New AMF如果和Old AMF不在同一PLMN，则New AMF不使用Old AMF带回来的AM策略信息，选择新的PCF并与新的PCF重新建立AM策略关联。
命令举例 
`
设置重定位后的注册流程中，New AMF向Old AMF获取用户上下文时，Old AMF基于PLMN决定是否携带PCF信息给New AMF，AM及UE策略建立时New AMF基于PLMN决定是否重选PCF。
SET INTERAMFPCFCFG:OLDAMFCARRYPCFINFO="BASEONPLMN",NEWAMFRESELECTPCF="BASEONPLMN"
` 
### 查询局间流程PCF策略配置(SHOW INTERAMFPCFCFG) 
### 查询局间流程PCF策略配置(SHOW INTERAMFPCFCFG) 
功能说明 
该命令用于查询重定位情况下处理AM策略和UE策略关联，Old AMF是否携带PCF信息给New AMF以及New AMF是否重选PCF的本地策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
oldAmfcarryPcfInfo|老局携带PCF信息策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BASEONPLMN|该参数用于显示在AMF发生重定位的场景下，Old AMF是否携带PCF信息给New AMF。不携带PCF信息：OldAMF不需要携带PCF信息给New AMF。携带PCF信息：Old AMF需要携带PCF信息给New AMF。基于PLMN携带PCF信息：如果Old AMF和New AMF属于同一PLMN，则Old AMF不需要携带PCF信息给New AMF。如果Old AMF和New AMF不属于同一PLMN，则Old AMF需要携带PCF信息给New AMF。
newAmfreselectPcf|新局重选PCF策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: BASEONPLMN|该参数用于显示在AMF发生重定位的场景下，New AMF是否重新选择新的PCF，重新建立AM策略关联。不重选PCF：New AMF不需要重选PCF，使用Old AMF带回来的AM策略信息重选PCF：则New AMF不使用Old AMF带回来的AM策略信息，选择新的PCF并与新的PCF重新建立AM策略关联。基于PLMN重选PCF：New AMF如果和Old AMF在同一PLMN，则New AMF不需要重选PCF，使用Old AMF带回来的AM策略信息。New AMF如果和Old AMF不在同一PLMN，则New AMF不使用Old AMF带回来的AM策略信息，选择新的PCF并与新的PCF重新建立AM策略关联。
命令举例 
`
查询AMF重定位情况下AM及UE策略处理的配置。
SHOW  INTERAMFPCFCFG
(No.1) : SHOW INTERAMFPCFCFG:
-----------------Namf_Communication_0_A----------------
操作维护       老局携带PCF信息策略 新局重选PCF策略 
---------------------------------------------------
修改           基于PLMN携带PCF信息 基于PLMN重选PCF 
---------------------------------------------------
记录数：1
执行成功开始时间:2020-10-19 20:34:02 耗时: 0.145 秒
` 
## UE策略配置 
## UE策略配置 
背景知识 
在5GC中，UE Policy是指AMF给UE下发的包括URSP（UE Route Selection Policy，UE路由选择策略）等等一系列的策略，这使得运营商可以根据终端的业务信息，网络负荷，网络拓扑等信息，对终端接入业务的路由等实施动态的策略控制。 
功能说明 
本功能用于设置UE Policy相关的策略。 
子主题： 
### 投递UE策略结束时长 
### 投递UE策略结束时长 
背景知识 
PCF决策UE Policy，UE使用UE Policy，AMF在UE和PCF之间透传UE Policy ，还需要透传UE给PCF回复的响应（Manage UE Policy Complete）或拒绝（Manage UE Policy Reject）消息，通常都不是一条消息，而是通过多条消息下发多个策略。多条消息可能连续的，也可能是间隔的。 
功能说明 
该功能用于配置AMF为PCF及UE透传上下行的UE Policy 消息的持续时长。即从AMF为PCF透传第一条下行UE Policy消息开始的一段时间内， AMF可以持续处理多条下行和上行的Ue Policy消息。 
子主题： 
#### 修改投递UE策略结束时长(SET UEPOLICY DELIVER DURATION) 
#### 修改投递UE策略结束时长(SET UEPOLICY DELIVER DURATION) 
功能说明 
该功能用于配置AMF为PCF及UE透传上下行的UE Policy 消息的持续时长。即从AMF为PCF透传第一条下行UE Policy消息开始的一段时间内， AMF可以持续处理多条下行和上行的Ue Policy消息。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
uePolicyDeliverDura|投递UE策略结束时长|参数可选性: 必选参数类型: 数字参数范围: 0-60000默认值: 1000|该参数用于标识AMF为PCF及UE透传上下行的UE Policy 消息的持续时长。单位为ms，默认1000ms。
命令举例 
`
设置AMF为PCF和UE透传上下行UEPolicy消息的持续时长为2s。
SET UEPOLICY DELIVER DURATION:UEPOLICYDELIVERDURA=2000"
` 
#### 查询投递UE策略结束时长(SHOW UEPOLICY DELIVER DURATION) 
#### 查询投递UE策略结束时长(SHOW UEPOLICY DELIVER DURATION) 
功能说明 
该功能用于查询AMF为PCF及UE透传上下行的UE Policy 消息的持续时长。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
uePolicyDeliverDura|投递UE策略结束时长|参数可选性: 任选参数类型: 数字参数范围: 0-60000默认值: 1000|该参数用于标识AMF为PCF及UE透传上下行的UE Policy 消息的持续时长。单位为ms，默认1000ms。
命令举例 
`
查询AMF为PCF和UE透传上下行UEPolicy消息的持续时长。
SHOW UEPOLICY DELIVER DURATION:
(No.3) : SHOW UEPOLICY DELIVER DURATION:
-----------------Namf_Communication_0----------------
投递UE策略结束时长(ms)
2000
记录数：1
执行成功耗时: 0.136 秒
` 
# 网络标识和时区配置 
# 网络标识和时区配置 
背景知识 
网络标识和时区，即NITZ(Network Identity and Time Zone)，一般用于通过无线网络向移动设备自动配置日期，时间和时区等信息，同时也向移动设备提供运营商信息。 
功能说明 
本功能用于配置网络标识及时区相关控制信息及参数。 
子主题： 
## 全局NITZ配置 
## 全局NITZ配置 
背景知识 
NITZ（Network Identity and Time Zone），即网络标识和时区，用于自动配置本地的时间和日期的机制，同时也通过无线网向移动设备提供运营商信息。NITZ经常被用来自动更新移动网络的系统时钟。 
功能说明 
本功能用于配置与NITZ相关的参数。 
子主题： 
### 修改网络标识和时区配置(SET NITZCFG) 
### 修改网络标识和时区配置(SET NITZCFG) 
功能说明 
该命令用于设置或修改网络名称和时区配置。  
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
carryNI|携带NI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYNI|该参数用于设置AMF是否下发网络名称。
carryTZ|携带TZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYTZ|该参数用于设置AMF是否下发时区。
intialReg|初始注册流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYININTIALREG|该参数用于设置AMF是否在初始注册流程中下发NITZ。
interAmf|跨AMF流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYININTERAMFREG|该参数用于设置AMF是否在跨AMF流程中下发NITZ。
interRat|跨RAT流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYININTERRAT|该参数用于设置AMF是否在跨RAT流程中下发NITZ。
periodicReg|周期性注册流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYINPERIODICREG|该参数用于设置AMF是否在周期性注册流程中下发NITZ。
intraAmfMobileReg|局内移动性注册流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYININTRAAMFMOBILEREG|该参数用于设置AMF是否在局内移动性注册流程中下发NITZ。
addCi|携带国家名缩写|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYCI|该参数用于设置AMF是否携带国家名缩写。
fullNiCodePlan|长网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLUSEBIT7|该参数用于设置AMF长网络名称编码方式。
fullNi|长网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置AMF长网络名称。需要将长网络名称修改为空时，配置为“N/A”。
shortNiCodePlan|短网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SHORTUSEBIT7|该参数用于设置AMF短网络名称编码方式。
shortNi|短网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置AMF短网络名称。需要将短网络名称修改为空时，配置为“N/A”。
命令举例 
`
设置下发网络名称，设置下发时区，设置在初始注册流程中下发NITZ，设置在跨AMF流程中下发NITZ，设置在跨RAT流程中下发NITZ，设置在周期性注册流程中下发NITZ，设置在局内移动性注册流程中下发NITZ，设置携带国家名缩写，设置长网络名称编码方式为BIT7，长网络名称为chinamobile，设置短网络名称编码方式为BIT7，短网络名称为cmcc。
SET NITZCFG:CARRYNI="CARRYNI",CARRYTZ="CARRYTZ",INTIALREG="CARRYININTIALREG",INTERAMF="CARRYININTERAMFREG",INTERRAT="CARRYININTERRAT",PERIODICREG="CARRYINPERIODICREG",INTRAAMFMOBILEREG="CARRYININTRAAMFMOBILEREG",ADDCI="CARRYCI",FULLNICODEPLAN="FULLUSEBIT7",FULLNI="chinamobile",SHORTNICODEPLAN="SHORTUSEBIT7",SHORTNI="cmcc"
` 
### 查询网络标识和时区配置(SHOW NITZCFG) 
### 查询网络标识和时区配置(SHOW NITZCFG) 
功能说明 
该命令用于查询网络名称和时区配置。  
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
carryNI|携带NI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYNI|该参数用于设置AMF是否下发网络名称。
carryTZ|携带TZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYTZ|该参数用于设置AMF是否下发时区。
intialReg|初始注册流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYININTIALREG|该参数用于设置AMF是否在初始注册流程中下发NITZ。
interAmf|跨AMF流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYININTERAMFREG|该参数用于设置AMF是否在跨AMF流程中下发NITZ。
interRat|跨RAT流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYININTERRAT|该参数用于设置AMF是否在跨RAT流程中下发NITZ。
periodicReg|周期性注册流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYINPERIODICREG|该参数用于设置AMF是否在周期性注册流程中下发NITZ。
intraAmfMobileReg|局内移动性注册流程是否携带NITZ|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTCARRYININTRAAMFMOBILEREG|该参数用于设置AMF是否在局内移动性注册流程中下发NITZ。
addCi|携带国家名缩写|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYCI|该参数用于设置AMF是否携带国家名缩写。
fullNiCodePlan|长网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLUSEBIT7|该参数用于设置AMF长网络名称编码方式。
fullNi|长网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置AMF长网络名称。
shortNiCodePlan|短网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SHORTUSEBIT7|该参数用于设置AMF短网络名称编码方式。
shortNi|短网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置AMF短网络名称。
命令举例 
`
查询AMF网络名称和时区配置。
SHOW NITZCFG:
(No.1) : SHOW NITZCFG:
-----------------Namf_Communication_0----------------
携带NI    携带TZ   初始注册流程是否携带NITZ   跨AMF流程是否携带NITZ 跨RAT流程是否携带NITZ 周期性注册流程是否携带NITZ 局内移动性注册流程是否携带NITZ 携带国家名缩写 长网络名称编码方式 长网络名称 短网络名称编码方式  短网络名称
携带网络名称    携带时区     初始注册流程携带NITZ    跨AMF流程携带NITZ    跨RAT流程携带NITZ    周期性注册流程携带NITZ    局内移动性注册流程携带NITZ   携带国家名缩写    长网络名称编码用BIT7    chinamobile    短网络名称编码用BIT7   cmcc
记录数：1
执行成功耗时: 0.152 秒
` 
## 基于PLMN的NI配置 
## 基于PLMN的NI配置 
背景知识 
用户接入AMF后，AMF可以通过向UE发送配置更新消息，为用户提供NI（Network Identifier，网络标识信息），用户收到后，NI会显示在终端界面，以便用户获知当前接入的网络。 
功能说明 
本功能用于配置基于PLMN的NI（Network Identifier，网络标识信息），当运营商需要针对不同的PLMN灵活配置NI时，可以使用本功能。包含两部分配置内容： 
 
配置不同PLMN对应的NI。 
 
配置PLMN的获取策略，即根据哪个PLMN来查询NI，可以配置为基于用户接入的PLMN（Selected PLMN）或者基于用户SUPI对应的HPLMN（Home PLMN）。 
 
子主题： 
### 增加基于PLMN的NI配置(ADD AMF PLMN NI) 
### 增加基于PLMN的NI配置(ADD AMF PLMN NI) 
功能说明 
该命令用于增加基于PLMN的网络标识配置。当运营商需要针对不同的PLMN灵活配置网络标识时，使用该命令。配置成功后，若本局AMF判断需要下发网络标识时，携带该配置对应的网络标识给UE。 
注意事项 
本命令执行后，结果立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置PLMN中的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置PLMN中的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
fullni|长网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置基于PLMN选择的长网络名称。修改影响：无。数据来源：本端规划。默认值：无。配置原则：编码方式为BIT7时，长网络名称不能输入中文字符。需要将长网络名称修改为空时，配置为“N/A”。
fullnicodeplan|长网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLUSEBIT7|参数作用：该参数用于配置基于PLMN选择的长网络名称的编码方式。目前支持两种编码方式：Alphabet编码格式（BIT7）：其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式（USC2）：其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit Default Alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。修改影响：无。数据来源：本端规划。默认值：长网络名称编码用BIT7。配置原则：无。
shortni|短网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置基于PLMN选择的短网络名称。修改影响：无。数据来源：本端规划。默认值：无。配置原则：编码方式为BIT7时，短网络名称不能输入中文字符。需要将长网络名称修改为空时，配置为“N/A”。
shortnicodeplan|短网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SHORTUSEBIT7|参数作用：该参数用于配置基于PLMN选择的短网络名称的编码方式。目前支持两种编码方式：Alphabet编码格式（BIT7）：其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式（USC2）：其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit Default Alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。修改影响：无。数据来源：本端规划。默认值：短网络名称编码用BIT7。配置原则：无。
addci|携带国家名缩写|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYCI|参数作用：该参数用于配置基于PLMN选择的网络标识前面是否添加国家名称缩写。修改影响：无。数据来源：本端规划。默认值：携带国家名缩写。配置原则：无。
命令举例 
`
增加基于PLMN的NI配置：设置国家码460，设置网络码01，设置长网络标识china mobile，设置长网络标识编码方式BIT7，设置短网络标识cmcc，设置短网络标识编码方式BIT7，设置携带国家名缩写
ADD AMF PLMN NI:MCC="460",MNC="01",FULLNI="china mobile",FULLNICODEPLAN="FULLUSEBIT7",SHORTNI="cmcc",SHORTNICODEPLAN="SHORTUSEBIT7",ADDCI="CARRYCI"
` 
### 修改基于PLMN的NI配置(MOD AMF PLMN NI) 
### 修改基于PLMN的NI配置(MOD AMF PLMN NI) 
功能说明 
该命令用于修改基于PLMN的网络标识配置。当运营商需要修改特定PLMN对应的网络标识时，使用该命令。配置成功后，后续本局AMF判断需要下发网络标识时，携带修改后配置对应的网络标识给UE。 
注意事项 
本命令执行后，结果立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置PLMN中的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置PLMN中的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
fullni|长网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置基于PLMN选择的长网络名称。修改影响：无。数据来源：本端规划。默认值：无。配置原则：编码方式为BIT7时，长网络名称不能输入中文字符。需要将长网络名称修改为空时，配置为“N/A”。
fullnicodeplan|长网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLUSEBIT7|参数作用：该参数用于配置基于PLMN选择的长网络名称的编码方式。目前支持两种编码方式：Alphabet编码格式（BIT7）：其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式（USC2）：其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit Default Alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。修改影响：无。数据来源：本端规划。默认值：长网络名称编码用BIT7。配置原则：无。
shortni|短网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置基于PLMN选择的短网络名称。修改影响：无。数据来源：本端规划。默认值：无。配置原则：编码方式为BIT7时，短网络名称不能输入中文字符。需要将长网络名称修改为空时，配置为“N/A”。
shortnicodeplan|短网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SHORTUSEBIT7|参数作用：该参数用于配置基于PLMN选择的短网络名称的编码方式。目前支持两种编码方式：Alphabet编码格式（BIT7）：其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式（USC2）：其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit Default Alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。修改影响：无。数据来源：本端规划。默认值：短网络名称编码用BIT7。配置原则：无。
addci|携带国家名缩写|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYCI|参数作用：该参数用于配置基于PLMN选择的网络标识前面是否添加国家名称缩写。修改影响：无。数据来源：本端规划。默认值：携带国家名缩写。配置原则：无。
命令举例 
`
修改基于PLMN的NI配置：修改的网络名称国家码460，修改的网络名称网络码01，修改长网络名称为china mobile，修改长网络名称编码方式为UCS2，修改短网络名称为cmcc，修改短网络名称编码方式为UCS2，修改为不携带国家名缩写
MOD AMF PLMN NI:MCC="460",MNC="01",FULLNI="china mobile",FULLNICODEPLAN="FULLUSEUCS2",SHORTNI="cmcc",SHORTNICODEPLAN="SHORTUSEUCS2",ADDCI="NOTCARRYCI"
` 
### 删除基于PLMN的NI配置(DEL AMF PLMN NI) 
### 删除基于PLMN的NI配置(DEL AMF PLMN NI) 
功能说明 
该命令用于删除基于PLMN的网络标识配置。当运营商需要删除特定PLMN的网络标识时，使用该命令。 
注意事项 
本命令执行后，结果立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置PLMN中的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置PLMN中的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
命令举例 
`
删除基于PLMN的NI配置：删除的网络名称国家码460，删除的网络名称网络码01
DEL AMF PLMN NI:MCC="460",MNC="01"
` 
### 查询基于PLMN的NI配置(SHOW AMF PLMN NI) 
### 查询基于PLMN的NI配置(SHOW AMF PLMN NI) 
功能说明 
该命令用于查询基于PLMN的网络标识配置。系统支持查询配置的全部或特定PLMN的网络标识，当查询特定PLMN的网络标识配置时，需要填写所需要查询的PLMN。 
注意事项 
本命令执行后，结果立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置PLMN中的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置PLMN中的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置PLMN中的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中唯一标识一个国家信息。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置PLMN中的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中唯一标识一个运营商网络信息。
fullni|长网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置基于PLMN选择的长网络名称。
fullnicodeplan|长网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: FULLUSEBIT7|参数作用：该参数用于配置基于PLMN选择的长网络名称的编码方式。目前支持两种编码方式：Alphabet编码格式（BIT7）：其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式（USC2）：其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit Default Alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
shortni|短网络名称|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于配置基于PLMN选择的短网络名称。
shortnicodeplan|短网络名称编码方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SHORTUSEBIT7|参数作用：该参数用于配置基于PLMN选择的短网络名称的编码方式。目前支持两种编码方式：Alphabet编码格式（BIT7）：其字母表由128个字符以及10个扩展字符组成。128个非扩展字符的每个字符使用7个BIT位来表示。10个扩展字符以字母表中的Escape字符（字符码值0x1B）打头。该编码格式使用拉丁语系的编码，比如英语。具体可参阅3GPP协议23.038。UCS2编码格式（USC2）：其字母表中每个字符使用16个BIT位表示。相对于GSM 7 bit Default Alphabet编码格式，UCS2可以胜任非拉丁语系的编码，比如汉语、日语等。具体可参阅ISO/IEC10646。
addci|携带国家名缩写|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRYCI|参数作用：该参数用于配置基于PLMN选择的网络标识前面是否添加国家名称缩写。
命令举例 
`
查询基于PLMN的NI配置 
SHOW AMF PLMN NI:MCC="460",MNC="01"
-----------------Namf_Communication_0----------------
操作维护       移动国家码 移动网络码 长网络名称   长网络名称编码方式   短网络名称 短网络名称编码方式   携带国家名缩写 
----------------------------------------------------------------------------------------------------------------------
复制  删除      460        01         china mobile 长网络名称编码用BIT7 cmcc       短网络名称编码用BIT7 携带国家名缩写 
----------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-01-18 16:27:22 耗时: 0.166 秒
` 
### 修改基于PLMN的NI策略配置(MOD AMF PLMN NI POLICY) 
### 修改基于PLMN的NI策略配置(MOD AMF PLMN NI POLICY) 
功能说明 
该命令用于修改基于PLMN的网络标识策略配置。当运营商需要调整基于PLMN的网络标识策略时，使用该命令。 
注意事项 
本命令执行后，结果立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
selplmnorsupiplmn|接入的PLMN或SUPI的HPLMN|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SELPLMN|参数配置：该参数用于配置向UE下发网络标识时，获取对应网络标识配置依据的PLMN，可以是用户接入的PLMN（Selected PLMN）或者用户SUPI对应的HPLMN。修改影响：无。数据来源：本端规划。默认值：用户接入的PLMN。配置原则：无。
命令举例 
`
修改基于PLMN的NI策略配置：修改PLMN的NI策略为SUPIPLMN
MOD AMF PLMN NI POLICY:SELPLMNORSUPIPLMN="SUPIPLMN"
` 
### 查询基于PLMN的NI策略配置(SHOW AMF PLMN NI POLICY) 
### 查询基于PLMN的NI策略配置(SHOW AMF PLMN NI POLICY) 
功能说明 
该命令用于查询基于PLMN的网络标识策略配置。 
注意事项 
本命令执行后，结果立即生效。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
selplmnorsupiplmn|接入的PLMN或SUPI的HPLMN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SELPLMN|参数配置：该参数用于配置向UE下发网络标识时，获取对应网络标识配置依据的PLMN，可以是用户接入的PLMN（Selected PLMN）或者用户SUPI对应的HPLMN。
命令举例 
`
查询基于PLMN的NI策略配置
SHOW AMF PLMN NI POLICY
-----------------Namf_Communication_0----------------
info            
----------------
用户SUPI的HPLMN 
----------------
记录数：1
执行成功开始时间:2022-01-18 16:55:52 耗时: 0.246 秒
` 
# 4/5G互操作配置 
# 4/5G互操作配置 
背景知识 
在5G网络实现全覆盖之前，在很长时间内，4G网络都是5G网络的良好补充，这就意味着5G用户将会在4/5G网络中移动。终端在移动过程中的业务连续性直接影响业务使用体验，尤其是语音类业务。4/5G互操作就是为了保证业务连续性的技术。 
为了支持4G和5G互操作，3GPP定义了专用于跨系统互操作的4G/5G融合网元，包括HSS+UDM、PCF+PCRF、SMF+PGW-C和UPF+PGW-U。具有4G/5G能力的终端用户，可以选择以上四个合一网元。 
根据MME和AMF之间是否有N26接口，4G和5G互操作可分为： 
 
Interworking with N26
终端在4G和5G网络间移动时，在源系统和目标系统间可以交换移动性管理状态及会话管理状态。
当网络中部署了N26接口时，N26接口的存在将能够支持在互操作过程中，在源网络和目标网络之间传送移动性管理状态和会话管理状态，因此当运营商部署了N26接口时，UE仅需以单注册模式运行，同时网络仅需同时保持UE的一种可用的移动性管理状态，即可保证用户无缝的业务和会话连续性。当UE从5GC移动到EPC时，由SMF基于EPS能力以及运营商具体的管理策略决定哪些PDU会话可以重定位到目标EPS，并释放无法迁移到EPS的那部分PDU会话。
当UE处于空闲态时，如果发生5GC到EPC的移动，UE可以选择使用由5G-GUTI映射而来的EPS-GUTI进行跟踪区更新流程或4G附着流程完成移动性处理，MME通过N26接口获取UE在5G的移动性管理上下文和会话管理上下文。在此过程中，MME并不感知跨系统互操作过程，整个处理过程中，N26接口从MME处理的角度来说等同于S10接口。如果空闲态下UE发生EPC到5GC的移动，UE将使用由EPS-GUTI映射而来的5G-GUTI执行移动性注册（Mobility Registration）流程，并且向网络指示该UE的源网络是EPC，同时AMF通过N26接口获取UE在4G的移动性管理上下文和会话管理上下文，并将会话部分的信息发送给SMF。 
 
Interworking without N26
终端在4G和5G间移动时，在源系统和目标系统间可以交换会话管理状态，但不交换移动性管理状态。
在未部署N26接口的网络中，网络使用HSS+UDM存储UE相关的PGW-C+SMF和APN/DNN信息，以此来保障UE的IP地址连续性。在未部署N26接口的情况下，网络侧应在UE初始附着的过程中指示网络具备双注册能力，以协助UE决定是否在互操作流程触发前提前在目标网络进行注册。如果UE在以双注册模式注册到网络后移动到支持N26接口的区域（如在漫游场景下VPLMN部署了N26接口），网络侧可以以携带重注册指示的注销请求将UE从网络中注销，并在UE重注册过程中不再携带网络侧支持双注册模式的指示，让UE以单注册模式在网络中进行重注册。 
 
根据UE的能力，4G和5G互操作可分为： 
 
单注册模式
终端具有4G和5G能力，但同时只能接入4G系统或者5G系统其中之一，终端仅维护4G或5G网络中的移动性管理上下文。 
 
双注册模式
终端具有4G和5G能力，可以同时接入4G系统和5G系统，终端可以同时维护4G和5G网络中移动性上下文。 
 
功能说明 
4/5G互操作配置包括互操作模式配置、EBI分配策略配置、MME地址解析配置、AMF的EPC NAS加密和完整性保护配置。 
子主题： 
## AMF互操作配置 
## AMF互操作配置 
背景知识 
在5G网络实现全覆盖之前，在很长时间内，4G网络都是5G网络的良好补充，这就意味着5G用户将会在4/5G网络中移动。终端在移动过程中的业务连续性直接影响业务使用体验，尤其是语音类业务。4/5G互操作就是为了保证业务连续性的技术。 
为了提供业务连续性，3GPP定义了两种互操作方案：
 
Interworking with N26
当网络中部署了N26接口时，N26接口能够支持在互操作过程中，在源网络和目标网络之间传递移动性管理状态及会话管理状态。当部署了N26接口时，UE仅需以单注册模式运行，即可保证用户无缝的业务和会话连续性。要求保持终端的IP地址不变，并且中断时间敏感的业务时，需要使用此模式。 
 
Interworking without N26
Interworking without N26: 当网络中未部署N26接口时，网络使用HSS+UDM存储UE相关的PGW-C+SMF和APN/DNN信息，以此来保证UE的IP地址连续性。无法实现业务连续性，但可以实现终端的IP地址保持不变。 
 
功能说明 
当终端用户在4/5G网络之间移动时，且需要保证业务连续性时，需要使用本功能，设置AMF所支持的4/5G互操作模式，及其是否支持Interworking with N26和Interworking without N26功能。 
使用此功能前，先开启对应的4/5G互操作的license， 并配置互操作的其他相关命令。 
子主题： 
### 修改 AMF互操作配置(SET 5GINTERWORKCFG) 
### 修改 AMF互操作配置(SET 5GINTERWORKCFG) 
功能说明 
该命令用于设置或修改AMF所支持的4/5G网络互操作模式，及其是否支持Interworking with N26和Interworking without N26。 
当需要开启4/5G网络互操作功能的时候，根据5GC网络中是否支持N26接口，选择相应的4/5G网络互操作模式。  
注意事项 
 
本命令执行后，配置立即生效。 
 
本命令中的参数“支持N26互操作”生效的前提，需要确认License项："uMAC_AMF_7202 "AMF支持N26互操作功能""已激活。 
 
本命令中的参数“"支持无N26互操作"生效的前提，需要确认License项：uMAC_AMF_7203 "AMF支持无N26互操作功能"已激活。 
 
本命令最多只能配置1条记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supInterWithN26|支持N26互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持N26互操作，取值及含义如下：不支持N26互操作。支持N26互操作。修改影响：无。数据来源：本端配置。默认值：支持N26互操作。配置原则：在5GC网络中部署了N26接口，可开启此功能。在此模式下可保证终端用户的业务连续性。需要确认License项："uMAC_AMF_7202 "AMF支持N26互操作功能""已激活，否则本参数无法生效。
supInterWithoutN26|支持无N26互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置在没有部署N26接口的情况下，AMF是否支持4/5G网络互操作功能，取值及含义如下：不支持无N26互操作：如果设置为不支持无N26互操作，则AMF不支持4/5G网络互操作功能。支持无N26互操作：在没有部署N26接口的情况下，如果设置为支持无N26互操作，则AMF支持4/5G网络互操作功能。修改影响：无。数据来源：本端配置。默认值：不支持无N26互操作。配置原则：在5GC网络中未部署N26接口的情况下，可开启此功能，此模式下无法保证用户的业务在4G/5G网络的连续性。需要确认License项：uMAC_AMF_7203 "AMF支持无N26互操作功能"已激活，否则本参数无法生效。
interworkMode|互操作模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置4/5G互操作的模式，取值及含义如下：有N26：如果设置为有N26，则会部署N26接口。无N26：如果设置为无N26，则不会部署N26接口。修改影响：无。数据来源：本端配置。默认值：有N26。配置原则：需要根据实际环境中，5GC网络是否支持N26接口，来设置本参数。
gtpRetryTimes|GTP重发队列次数|参数可选性: 任选参数类型: 数字参数范围: 3-30默认值: 5|参数作用：该参数用于设置4/5G互操作时，GTP队列的最大重新发送次数。修改影响：无。数据来源：本端配置。默认值：5次。配置原则：无。
gtpRetryInterval|GTP重发队列间隔(秒)|参数可选性: 任选参数类型: 数字参数范围: 3-30默认值: 3|参数作用：该参数用于设置4/5G互操作时，重新发送GTP队列的时间间隔，单位（秒/s）。修改影响：无。数据来源：本端配置。默认值：3秒。配置原则：无。
supIndFwdTunnel|AMF支持非直接数据前转|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: INDFWDSPRT|参数作用：该参数用于设置4/5G互操作时，AMF是否支持非直接数据前转，取值及含义如下：不支持：如果该参数设置为不支持，AMF不支持创建非直接数据前转隧道。支持：如果该参数设置为支持，4/5G互操作时，AMF支持创建非直接数据前转隧道。仅PLMN改变时支持：4/5G互操作时，仅当PLMN改变时，AMF支持创建非直接数据前转隧道。修改影响：无。数据来源：本端配置。默认值：支持。配置原则：无。
selPoliForCombSMF|互操作是否需要UE签约支持|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NONEED|参数作用：该参数用于设置融合SMF选择策略，取值及含义如下：不需要UE签约支持互操作：如果该参数设置为“不需要UE签约支持互操作”，无论终端的签约数据是否支持互操作与否，在其它条件满足时，AMF都会优选融合的SMF。需要UE签约支持互操作：如果该参数设置为“需要UE签约支持互操作”，并且终端的签约数据不支持互操作时，即使其它条件都满足，AMF也不会优选融合的SMF。仅PLMN改变时支持：4/5G互操作时，仅当PLMN改变时，AMF支持创建非直接数据前转隧道。。修改影响：无数据来源：本端配置。默认值：不需要UE签约支持互操作。配置原则：无。
carryEpsUeSecCap|S1 mode to N1 mode NAS transparent container中是否携带 EPS UE security capability|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数标识用户从4G网络切换到5G网络时，AMF下发Handover Request消息中的S1 mode to N1 mode NAS transparent container中是否携带EPS UE安全能力，取值及含义如下：否：如果设置为否，则不会携带EPS UE安全能力。是：如果设置为是，会携带EPS UE安全能力。修改影响：无。数据来源：本端配置。默认值：否。配置原则：无。
SPRT5GREPREFI|AMF是否支持5G的Return Preferred|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF支持5G的Return Preferred，取值及含义如下：不支持5G的Return Preferred支持5G的Return Preferred修改影响：无。数据来源：本端配置。默认值：不支持5G的Return Preferred。配置原则：无。
SPRT4GREPREFI|AMF是否支持4G的Return Preferred|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF是否支持4G的Return Preferred，取值及含义如下：不支持4G的Return Preferred支持4G的Return Preferred修改影响：无。数据来源：本端配置。默认值：不支持4G的Return Preferred。配置原则：无。
carryMmeCapa|向SMF请求会话上下文时是否携带MME能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRY|参数作用：该参数用于配置用户从5G网络移动到4G网络的场景下，AMF向SMF发送的请求会话上下文的请求消息中是否携带MME能力，取值及含义如下：否：如果设置为否，AMF向SMF发送的请求会话上下文的请求消息中不会携带MME能力。是：如果设置为是，AMF向SMF发送的请求会话上下文的请求消息中会携带MME能力。修改影响：无。数据来源：本端配置。默认值：是。配置原则：无。
supivsmfreselidle|支持空闲态模式下4G移动5G时V-SMF或I-SMF重选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于控制在空闲态模式下4G移动到5G过程中，重选V-SMF或I-SMF，取值及含义如下：不支持：如果设置为不支持，则不会重选V-SMF或I-SMF。支持：如果设置为支持，AMF根据默认V-SMF、默认I-SMF或者SMF+PGW-C返回的S-NSSAI，判断是否需要重选V-SMF或者I-SMF，或者插入I-SMF。修改影响：无。数据来源：本端配置。默认值：不支持。配置原则：无。
idleiwksnssaiply|空闲态模式下互操作S-NSSAI获取策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOCALCONFIG|参数作用：该参数用于控制在空闲态模式下4G移动到5G过程中选择S-NSSAI的策略，取值及含义如下：基于本地配置：如果设置为基于本地配置，取本地配置的互操作S-NSSAI，如果存在多个，则任意选择一个。智能推导：如果设置为智能推导，根据用户请求携带的切片、PDU会话的DNN信息以及用户签约（DNN和切片对应关系）取交集选择切片。若交集为空或PDU会话的DNN无签约的切片，则直接取本地配置的互操作切片。修改影响：无。数据来源：本端配置。默认值：基于本地配置。配置原则：无。
supDnnFault|支持DNN格式容错|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该命令用于设置DNN参数配置。AMF向SMF发送PDU会话创建消息时，EpsPdnCnxContainer中携带的APN是否包含APN OI；AMF向MME发送Forward Relocation Request消息时，EpsPdnCnxContainer中携带的APN是否包含APN OI，取值及含义如下：不支持：如果设置为不支持，则透传EpsPdnCnxContainer中的APN。支持：如果设置为支持，对EpsPdnCnxContainer进行解码，SMF或者MME没有携带APN OI时，AMF将为其填充APN OI。修改影响：无。数据来源：本端配置。默认值：不支持。配置原则：无。
amfReallocIn4To5Ho|支持4G到5G切换过程中AMF重选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置用户在从4G网络到5G网络的切换流程中，是否支持重选AMF，取值及含义如下：否：如果设置为不支持，在用户从4G网络切换到5G网络的过程中，则不支持AMF重定向过程。是：如果设置为支持，用户在从4G网络切换到5G网络过程中，当AMF从SMF+PGW-C处获取到PDU会话的切片后，AMF会向UDM获取用户签约的详细切片信息。AMF判断本AMF本地配置数据中是否有包含在用户签约信息中的全部PDU会话的切片，若本AMF没有包含在签约信息中的全部PDU会话切片，则本AMF会触发为用户重新选择AMF的流程，若最终选择的AMF不是本AMF，则本AMF会执行AMF重定向过程。修改影响：无。数据来源：本端配置。默认值：否。配置原则：无。
localSliceSeIn4To5Ho|支持4G到5G切换过程中本地切片选择|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于配置用户在从4G网络到5G网络的切换流程中，是否支持本地切片选择，取值及含义如下：否：如果设置为不支持，用户在从4G网络切换到5G网络过程中，则不支持本地切片选择。是：如果设置为支持，用户在从4G网络切换到5G网络过程中，AMF把从SMF+PGW-C获取的PDU会话切片作为Requested NSSAI，然后将此Requested NSSAI与从用户的签约信息中的切片，两者取交集，从而得到Allowed NSSAI。若本AMF支持该Allowed NSSAI，则继续为该用户服务，无需重选AMF。否则，本AMF需要触发NSSF切片选择流程。修改影响：无。数据来源：本端配置。默认值：是。配置原则：该参数生效的前提是"支持4G到5G切换过程中AMF重选（AMFREALLOCIN4TO5HO）"参数设置为“是”。
命令举例 
`
设置AMF支持N26互操作、不支持无N26互操作、互操作模式为有N26、gtp重发队列次数为5次、gtp重发队列间隔为3秒、AMF支持非直接数据前转、不需要UE签约支持互操作、S1 mode to N1 mode NAS transparent container中不携带 EPS UE security capability、AMF不支持5G的Return Preferred、AMF不支持4G的Return Preferred、向SMF请求会话上下文时携带MME能力、不支持空闲态模式下4G移动5G时V-SMF或I-SMF重选、空闲态模式下互操作S-NSSAI获取策略为基于本地配置、AMF不支持DNN格式容错、AMF支持4G到5G切换过程中AMF重选、AMF支持4G到5G切换过程中本地切片选择、AMF支持4G到5G切换后注册更新过程中切片选择：
SET 5GINTERWORKCFG:SUPINTERWITHN26="SPRT",SUPINTERWITHOUTN26="NOSPRT",INTERWORKMODE="WITHN26",GTPRETRYTIMES=5,GTPRETRYINTERVAL=3,SUPINDFWDTUNNEL="INDFWDSPRT",SELPOLIFORCOMBSMF="NONEED",CARRYEPSUESECCAP="NO",SPRT5GREPREFI="NOSPRT",SPRT4GREPREFI="NOSPRT",CARRYMMECAPA="CARRY",SUPIVSMFRESELIDLE="NOSPRT",IDLEIWKSNSSAIPLY="LOCALCONFIG",SUPDNNFAULT="NOSPRT",AMFREALLOCIN4TO5HO="YES",LOCALSLICESEIN4TO5HO="YES",SLICENEGAFTER4TO5HO="YES"
` 
### 查询 AMF互操作配置(SHOW 5GINTERWORKCFG) 
### 查询 AMF互操作配置(SHOW 5GINTERWORKCFG) 
功能说明 
该命令用于查看AMF所支持的4/5G互操作模式，及其是否支持Interworking with N26和Interworking without N26。  
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supInterWithN26|支持N26互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF是否支持N26互操作，取值及含义如下：不支持N26互操作。支持N26互操作。
supInterWithoutN26|支持无N26互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置在没有部署N26接口的情况下，AMF是否支持4/5G网络互操作功能，取值及含义如下：不支持无N26互操作：如果设置为不支持无N26互操作，则AMF不支持4/5G网络互操作功能。支持无N26互操作：在没有部署N26接口的情况下，如果设置为支持无N26互操作，则AMF支持4/5G网络互操作功能
interworkMode|互操作模式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置4/5G互操作的模式，取值及含义如下：有N26：如果设置为有N26，则会部署N26接口无N26：如果设置为无N26，则不会部署N26接口。
gtpRetryTimes|GTP重发队列次数|参数可选性: 任选参数类型: 数字参数范围: 3-30默认值: 5|参数作用：该参数用于设置4/5G互操作时，GTP队列的最大重新发送次数。
gtpRetryInterval|GTP重发队列间隔(秒)|参数可选性: 任选参数类型: 数字参数范围: 3-30默认值: 3|参数作用：该参数用于设置4/5G互操作时，重新发送GTP队列的时间间隔，单位（秒/s）。
supIndFwdTunnel|AMF支持非直接数据前转|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: INDFWDSPRT|参数作用：该参数用于设置4/5G互操作时，AMF是否支持非直接数据前转，取值及含义如下：不支持：如果该参数设置为不支持，AMF不支持创建非直接数据前转隧道。支持：如果该参数设置为支持，4/5G互操作时，AMF支持创建非直接数据前转隧道。仅PLMN改变时支持：4/5G互操作时，仅当PLMN改变时，AMF支持创建非直接数据前转隧道。
selPoliForCombSMF|互操作是否需要UE签约支持|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NONEED|参数作用：该参数用于设置融合SMF选择策略，取值及含义如下：不需要UE签约支持互操作：如果该参数设置为“不需要UE签约支持互操作”，无论终端的签约数据是否支持互操作与否，在其它条件满足时，AMF都会优选融合的SMF。需要UE签约支持互操作：如果该参数设置为“需要UE签约支持互操作”，并且终端的签约数据不支持互操作时，即使其它条件都满足，AMF也不会优选融合的SMF。仅PLMN改变时支持：4/5G互操作时，仅当PLMN改变时，AMF支持创建非直接数据前转隧道。。
carryEpsUeSecCap|S1 mode to N1 mode NAS transparent container中是否携带 EPS UE security capability|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数标识用户从4G网络切换到5G网络时，AMF下发Handover Request消息中的S1 mode to N1 mode NAS transparent container中是否携带EPS UE安全能力，取值及含义如下：否：如果设置为否，则不会携带EPS UE安全能力。是：如果设置为是，会携带EPS UE安全能力。
SPRT5GREPREFI|AMF是否支持5G的Return Preferred|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF支持5G的Return Preferred，取值及含义如下：不支持5G的Return Preferred支持5G的Return Preferred
SPRT4GREPREFI|AMF是否支持4G的Return Preferred|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于配置AMF是否支持4G的Return Preferred，取值及含义如下：不支持4G的Return Preferred支持4G的Return Preferred
carryMmeCapa|向SMF请求会话上下文时是否携带MME能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: CARRY|参数作用：该参数用于配置用户从5G网络移动到4G网络的场景下，AMF向SMF发送的请求会话上下文的请求消息中是否携带MME能力，取值及含义如下：否：如果设置为否，AMF向SMF发送的请求会话上下文的请求消息中不会携带MME能力。是：如果设置为是，AMF向SMF发送的请求会话上下文的请求消息中会携带MME能力。
supivsmfreselidle|支持空闲态模式下4G移动5G时V-SMF或I-SMF重选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于控制在空闲态模式下4G移动到5G过程中，重选V-SMF或I-SMF，取值及含义如下：不支持：如果设置为不支持，则不会重选V-SMF或I-SMF。支持：如果设置为支持，AMF根据默认V-SMF、默认I-SMF或者SMF+PGW-C返回的S-NSSAI，判断是否需要重选V-SMF或者I-SMF，或者插入I-SMF。
idleiwksnssaiply|空闲态模式下互操作S-NSSAI获取策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOCALCONFIG|参数作用：该参数用于控制在空闲态模式下4G移动到5G过程中选择S-NSSAI的策略，取值及含义如下：基于本地配置：如果设置为基于本地配置，取本地配置的互操作S-NSSAI，如果存在多个，则任意选择一个。智能推导：如果设置为智能推导，根据用户请求携带的切片、PDU会话的DNN信息以及用户签约（DNN和切片对应关系）取交集选择切片。若交集为空或PDU会话的DNN无签约的切片，则直接取本地配置的互操作切片。
supDnnFault|支持DNN格式容错|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该命令用于设置DNN参数配置。AMF向SMF发送PDU会话创建消息时，EpsPdnCnxContainer中携带的APN是否包含APN OI；AMF向MME发送Forward Relocation Request消息时，EpsPdnCnxContainer中携带的APN是否包含APN OI，取值及含义如下：不支持：如果设置为不支持，则透传EpsPdnCnxContainer中的APN。支持：如果设置为支持，对EpsPdnCnxContainer进行解码，SMF或者MME没有携带APN OI时，AMF将为其填充APN OI。
amfReallocIn4To5Ho|支持4G到5G切换过程中AMF重选|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置用户在从4G网络到5G网络的切换流程中，是否支持重选AMF，取值及含义如下：否：如果设置为不支持，在用户从4G网络切换到5G网络的过程中，则不支持AMF重定向过程。是：如果设置为支持，用户在从4G网络切换到5G网络过程中，当AMF从SMF+PGW-C处获取到PDU会话的切片后，AMF会向UDM获取用户签约的详细切片信息。AMF判断本AMF本地配置数据中是否有包含在用户签约信息中的全部PDU会话的切片，若本AMF没有包含在签约信息中的全部PDU会话切片，则本AMF会触发为用户重新选择AMF的流程，若最终选择的AMF不是本AMF，则本AMF会执行AMF重定向过程。
localSliceSeIn4To5Ho|支持4G到5G切换过程中本地切片选择|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：该参数用于配置用户在从4G网络到5G网络的切换流程中，是否支持本地切片选择，取值及含义如下：否：如果设置为不支持，用户在从4G网络切换到5G网络过程中，则不支持本地切片选择。是：如果设置为支持，用户在从4G网络切换到5G网络过程中，AMF把从SMF+PGW-C获取的PDU会话切片作为Requested NSSAI，然后将此Requested NSSAI与从用户的签约信息中的切片，两者取交集，从而得到Allowed NSSAI。若本AMF支持该Allowed NSSAI，则继续为该用户服务，无需重选AMF。否则，本AMF需要触发NSSF切片选择流程。
命令举例 
`
查看AMF上配置的4/5G互操作模式及其功能开关。
SHOW 5GINTERWORKCFG:
(No.1) : SHOW 5GINTERWORKCFG:
-----------------Namf_Communication_0----------------
操作维护       支持N26互操作 支持无N26互操作   互操作模式 gtp重发队列次数 gtp重发队列间隔(秒) AMF支持非直接数据前转 互操作是否需要UE签约支持 S1 mode to N1 mode NAS transparent container中是否携带 EPS UE security capability AMF是否支持5G的Return Preferred AMF是否支持4G的Return Preferred 向SMF请求会话上下文时是否携带MME能力 支持空闲态模式下4G移动5G时V-SMF或I-SMF重选 空闲态模式下互操作S-NSSAI获取策略 支持DNN格式容错 支持4G到5G切换过程中AMF重选 支持4G到5G切换过程中本地切片选择 支持4G到5G切换后注册更新过程中切片选择
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           支持N26互操作 不支持无N26互操作 有N26      5               3                   支持                  不需要UE签约支持互操作   否                                                                                不支持5G的Return Preferred      不支持4G的Return Preferred      是                                   不支持                                     基于本地配置                      不支持          是                          是                               是
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-07-22 11:17:22 耗时: 0.192 秒
` 
## EBI分配配置 
## EBI分配配置 
背景知识 
为了支持Interworking with N26这种4/5G互操作方式，5G网络需要为可以切换到4G网络的QoS Flow分配EBI（EPS Bearer Identity，EPS承载标识），EBI由AMF负责分配，AMF提供服务接口给SMF，SMF在新建、修改、删除QoS Flow时，调用AMF提供的申请或释放EBI的服务接口。 
功能说明 
EBI分配配置包括AMF的EBI分配策略和EBI抢占优先级策略。 
子主题： 
### EBI分配基本配置 
### EBI分配基本配置 
背景知识 
当终端用户在4G和5G网络互相切换时，为支持无缝切换，4/5G终端用户从5G网络接入时，5GC网络需要为终端提前分配4G EBI（EPS Bearer Identity，EPS承载标识），SMF为QoS Flow向AMF申请EBI，并通过N1 SM容器及N2 SM容器通知UE及NR，详细描述参见3GPP 23.502的 4.11.1.4章节。 
5G网络为终端分配EBI，可保证UE、PGW-C、SMF正确记录QoS Flow、EPS QoS、EBI之间的关联关系，并向NR侧提供正确的EBI。 
在4G网络中，MME是用户会话的汇聚点，EBI由MME分配。在5G网络中，EBI由AMF统一分配。 
功能说明 
对于EPC而言，同一个DNN，可以激活多个PDN连接，但是只会关联同一个SGW/PGW/SMF。 
本功能用于配置EBI分配的基本策略。 
子主题： 
#### 修改 EBI分配基本配置(SET 5GEBIASSIGNPOLICY) 
#### 修改 EBI分配基本配置(SET 5GEBIASSIGNPOLICY) 
功能说明 
在EPC网络中，同一个APN（5G网络中为DNN），可以激活多个PDN连接，但是只会关联同一个PGW。在C/U分离场景下，这些PDN连接只会关联同一个PGW-C和同一个PGW-U。 
在5GC网络中，同一个终端用户在同一个DNN下，根据不同的S-NSSAI，可以激活不同的PDU会话。这些PDU会话可能关联到不同的SMF，也可能关联到同一个SMF下的不同的UPF。为了后续终端用户能够顺利从5G网络切换到EPC网络，对于这两种场景下的EBI分配需要进行限制。 
该命令用于设置或修改EBI的分配策略，包括“同一DNN多SMF时EBI分配策略”和“EBI资源不足时EBI分配策略”。
 
“同一DNN多SMF时EBI分配策略”，表示在PDU会话关联到不同的SMF的场景下，AMF可以根据本地策略，决策拒绝当前收到的EBI分配请求消息，或者抢占相同DNN下已激活PDU会话的EBI。 
 
“EBI资源不足时EBI分配策略”，表示AMF收到EBI分配请求，判断不能满足分配要求时，决策拒绝当前收到的EBI分配请求消息，或者抢占已激活PDU会话的EBI。  
 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ebiAssiPlyforSevSmf|同一DNN多SMF时EBI分配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置同一DNN多SMF时，EBI分配策略。表示在PDU会话关联到不同的SMF的场景下，AMF可以根据本地策略，决策拒绝当前收到的EBI分配请求消息，或者抢占相同DNN下已激活PDU会话的EBI。
ebiAssiPlyforInRsc|EBI资源不足时EBI分配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置EBI资源不足时EBI分配策略。表示AMF收到EBI分配请求，判断不能满足分配要求时，决策拒绝当前收到的EBI分配请求消息，或者抢占已激活PDU会话的EBI。
命令举例 
`
设置EBI分配基本策略配置：同一DNN多SMF时EBI分配策略为"抢占"，EBI资源不足时EBI分配策略为"抢占"：
SET 5GEBIASSIGNPOLICY:EBIASSIPLYFORSEVSMF="EMPTION",EBIASSIPLYFORINRSC="EMPTION"
` 
#### 查询 EBI分配基本配置(SHOW 5GEBIASSIGNPOLICY) 
#### 查询 EBI分配基本配置(SHOW 5GEBIASSIGNPOLICY) 
功能说明 
该命令用于查询EBI分配基本策略配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ebiAssiPlyforSevSmf|同一DNN多SMF时EBI分配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置同一DNN多SMF时，EBI分配策略。表示在PDU会话关联到不同的SMF的场景下，AMF可以根据本地策略，决策拒绝当前收到的EBI分配请求消息，或者抢占相同DNN下已激活PDU会话的EBI。
ebiAssiPlyforInRsc|EBI资源不足时EBI分配策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置EBI资源不足时EBI分配策略。表示AMF收到EBI分配请求，判断不能满足分配要求时，决策拒绝当前收到的EBI分配请求消息，或者抢占已激活PDU会话的EBI。
命令举例 
`
查询EBI分配基本策略配置：
SHOW 5GEBIASSIGNPOLICY
(No.15) : SHOW 5GEBIASSIGNPOLICY:
-----------------Namf_Communication_0----------------
同一DNN多SMF时EBI分配策略    EBI资源不足时EBI分配策略
抢占                                            抢占
记录数：1
执行成功耗时: 1.051 秒
` 
### EBI抢占优先级配置 
### EBI抢占优先级配置 
背景知识 
当终端用户在4G和5G网络互相切换时，为支持无缝切换，4/5G用户从5G网络接入时，5GC网络需要为终端提前分配4G EBI（EPS Bearer Identity，EPS承载标识），SMF为QoS Flow向AMF申请EBI，并通过N1 SM容器及N2 SM容器通知到UE及NR，详细描述参见3GPP 23.502的 4.11.1.4章节。 
由5G网络为终端分配EBI，可保证UE、PGW-C、SMF正确记录QoS Flow、EPS QoS、EBI之间的关联关系，并向NR侧提供正确的EBI。 
在4G网络中，MME是用户会话的汇聚点，EBI由MME分配。在5G网络中，EBI由AMF统一分配。 
功能说明 
本功能用于AMF根据S_NSSAI+ARP没有匹配到对应EBI时的场景。 
该功能用于新增一个EBI分配优先级标识对应的优先级配置，包括S_NSSAI和ARP优先级配置。 
AMF使用基于APR和S-NSSAI对应的优先级来解决EBI的抢占问题，AMF在收到SMF发送的请求消息后，AMF给消息中的每一组“ARP+S-NSSAI”分配优先级。 
分配原则：AMF首先根据“ARP+NSSAI”一起查询[ADD 5GEBIASSIGNPRIORITY]命令配置的结果，如果不能匹配到对应的结果，则使用ARP和S-NSSAI分开查询。
AMF先使用ARP进行查询，还是先使用S-NSSAI进行查询，两者的先后顺序是由“EBI优先级匹配顺序配置”（[SET 5GEBIPRIOMATCHORDER]命令）配置的。
 
如果通过SET 5GEBIPRIOMATCHORDER命令设置为“ARP优先”，则AMF只用消息中的ARP来查询对应的优先级，此时S-NSSAI使用默认优先级（通过SET 5GDEFAULTEBIASSIGNPRIORITY命令配置）。 
 
如果通过SET 5GEBIPRIOMATCHORDER命令设置为“NSSAI优先”，则AMF只用消息中的S-NSSAI来查询对应的优先级，此时ARP使用默认优先级（通过SET 5GDEFAULTEBIASSIGNPRIORITY命令配置）。 
 
子主题： 
#### 设置EBI优先级匹配顺序配置(SET 5GEBIPRIOMATCHORDER) 
#### 设置EBI优先级匹配顺序配置(SET 5GEBIPRIOMATCHORDER) 
功能说明 
AMF使用基于APR和S-NSSAI对应的优先级来解决EBI的抢占问题，AMF在收到SMF发送的请求消息后，AMF给消息中的每一组“ARP+S-NSSAI”分配优先级。 
分配原则：AMF首先根据“ARP+NSSAI”一起查询[ADD 5GEBIASSIGNPRIORITY]命令配置的结果，如果不能匹配到对应的结果，则使用ARP和S-NSSAI分开查询。
AMF先使用ARP进行查询，还是先使用S-NSSAI进行查询，两者的先后顺序是由本命令配置的。
注意事项 
该命令的默认值是默认S-NSSAI优先。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
priomatchord|EBI优先级匹配顺序配置|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于配置当AMF首先根据“ARP+NSSAI”一起查询ADD 5GEBIASSIGNPRIORITY命令配置的结果，如果不能匹配到对应的结果，需要使用ARP和S-NSSAI分开查询时，AMF先使用ARP进行查询，还是先使用S-NSSAI进行查询的顺序。
命令举例 
`
设置EBI优先级匹配顺序值为：S-NSSAI优先：
SET 5GEBIPRIOMATCHORDER:PRIOMATCHORD="SNSSNIPRIO"
` 
#### 查询EBI优先级匹配顺序配置(SHOW 5GEBIPRIOMATCHORDER) 
#### 查询EBI优先级匹配顺序配置(SHOW 5GEBIPRIOMATCHORDER) 
功能说明 
该命令用于查询EBI优先级匹配顺序。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
priomatchord|EBI优先级匹配顺序配置|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|本参数用于配置当AMF首先根据“ARP+NSSAI”一起查询ADD 5GEBIASSIGNPRIORITY命令配置的结果，如果不能匹配到对应的结果，需要使用ARP和S-NSSAI分开查询时，AMF先使用ARP进行查询，还是先使用S-NSSAI进行查询的顺序。
命令举例 
`
查询EBI优先级匹配顺序：
SHOW 5GEBIPRIOMATCHORDER:
(No.21) : SHOW 5GEBIPRIOMATCHORDER:
-----------------Namf_Communication_0----------------
EBI优先级匹配顺序配置
S-NSSAI优先
记录数：1
执行成功耗时: 0.039 秒
` 
#### 设置EBI分配默认优先级配置(SET 5GDEFAULTEBIASSIGNPRIORITY) 
#### 设置EBI分配默认优先级配置(SET 5GDEFAULTEBIASSIGNPRIORITY) 
功能说明 
在AMF根据S_NSSAI+ARP没有匹配到对应EBI时的场景下，该命令用于设置或修改EBI（EPS Bearer Identity，EPS承载标识）分配默认优先级。 
AMF使用基于APR和S-NSSAI对应的优先级来解决EBI的抢占问题，AMF在收到SMF发送的请求消息后，AMF给消息中的每一组“ARP+S-NSSAI”分配优先级。 
分配原则：AMF首先根据“ARP+NSSAI”一起查询[ADD 5GEBIASSIGNPRIORITY]命令配置的结果，如果不能匹配到对应的结果，则使用ARP和S-NSSAI分开查询。
AMF先使用ARP进行查询，还是先使用S-NSSAI进行查询，两者的先后顺序是由“EBI优先级匹配顺序配置”（[SET 5GEBIPRIOMATCHORDER]命令）配置的。
如果通过[SET 5GEBIPRIOMATCHORDER]命令设置为“ARP优先”，则AMF只用消息中的ARP来查询对应的优先级，此时S-NSSAI使用默认优先级（通过[SET 5GDEFAULTEBIASSIGNPRIORITY]命令配置）。
如果通过[SET 5GEBIPRIOMATCHORDER]命令设置为“NSSAI优先”，则AMF只用消息中的S-NSSAI来查询对应的优先级，此时ARP使用默认优先级（通过[SET 5GDEFAULTEBIASSIGNPRIORITY]命令配置）。
注意事项 
优先级设置的值越大，优先级越高。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
defaultPriority|EBI分配默认优先级|参数可选性: 必选参数类型: 数字参数范围: 1-15默认值: 1|该参数用于在AMF根据S_NSSAI+ARP没有匹配到对应EBI时设置EBI分配默认优先级。
命令举例 
`
设置EBI分配默认优先级值为1。
SET 5GDEFAULTEBIASSIGNPRIORITY:DEFAULTPRIORITY=1
` 
#### 查询EBI分配默认优先级配置(SHOW 5GDEFAULTEBIASSIGNPRIORITY) 
#### 查询EBI分配默认优先级配置(SHOW 5GDEFAULTEBIASSIGNPRIORITY) 
功能说明 
在AMF根据S_NSSAI+ARP没有匹配到对应EBI时的场景下，该命令用于查询EBI分配默认优先级。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
defaultPriority|EBI分配默认优先级|参数可选性: 任选参数类型: 数字参数范围: 1-15默认值: 1|该参数用于在AMF根据S_NSSAI+ARP没有匹配到对应EBI时设置EBI分配默认优先级。
命令举例 
`
查询EBI分配默认优先级。
SHOW 5GDEFAULTEBIASSIGNPRIORITY
(No.2) : SHOW 5GDEFAULTEBIASSIGNPRIORITY:
-----------------Namf_Communication_0----------------
EBI Assignment default priority
1
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
#### 新增基于S_NSSAI和ARP 的优先级配置(ADD 5GEBIASSIGNPRIORITY) 
#### 新增基于S_NSSAI和ARP 的优先级配置(ADD 5GEBIASSIGNPRIORITY) 
功能说明 
该命令用于新增一个EBI分配优先级标识对应的优先级配置，包括S_NSSAI和ARP优先级配置。 
AMF使用基于APR和S-NSSAI对应的优先级来解决EBI的抢占问题，AMF在收到SMF发送的请求消息后，AMF给消息中的每一组“ARP+S-NSSAI”分配优先级。 
分配原则：AMF首先根据“ARP+NSSAI”一起查询本命令配置的结果，如果不能匹配到对应的结果，则使用ARP和S-NSSAI分开查询。
AMF先使用ARP进行查询，还是先使用S-NSSAI进行查询，两者的先后顺序是由“EBI优先级匹配顺序配置”（[SET 5GEBIPRIOMATCHORDER]命令）配置的。
 
如果通过SET 5GEBIPRIOMATCHORDER命令设置为“ARP优先”，则AMF只用消息中的ARP来查询对应的优先级，此时S-NSSAI使用默认优先级（通过SET 5GDEFAULTEBIASSIGNPRIORITY命令配置）。 
 
如果通过SET 5GEBIPRIOMATCHORDER命令设置为“NSSAI优先”，则AMF只用消息中的S-NSSAI来查询对应的优先级，此时ARP使用默认优先级（通过SET 5GDEFAULTEBIASSIGNPRIORITY命令配置）。 
 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ebiAssignpriId|EBI分配优先级标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置EBI分配优先级的标识。
arpPriLev|ARP优先级|参数可选性: 任选参数类型: 数字参数范围: 1-15|该参数用于设置ARP优先级。
arpEmptionCap|ARP抢占能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置ARP抢占能力，选项如下。抢占不能抢占
arpEmptionVul|ARP被抢占能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置ARP被抢占能力，选项如下。被抢占不被抢占
snssaiSST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
snssaiSD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
priority|EBI分配优先级|参数可选性: 必选参数类型: 数字参数范围: 1-15|该参数用于设置EBI分配优先级，参数取值范围：1~15
命令举例 
`
新增一个基于S_NSSAI和ARP 的优先级配置，其中EBI分配优先级标识值为1，ARP优先级值为1，ARP抢占能力值为"不抢占"，ARP被抢占能力值为"不被抢占"，SNSSAI SST值为eMBB,SNSSAI SD值为123456，EBI分配优先级为5：
ADD 5GEBIASSIGNPRIORITY:EBIASSIGNPRIID=1,ARPPRILEV=1,ARPEMPTIONCAP="NO",ARPEMPTIONVUL="NO",SNSSAISST="eMBB",SNSSAISD="123456",PRIORITY=5
` 
#### 修改基于S_NSSAI和ARP 的优先级配置(MOD 5GEBIASSIGNPRIORITY) 
#### 修改基于S_NSSAI和ARP 的优先级配置(MOD 5GEBIASSIGNPRIORITY) 
功能说明 
该命令用于修改一个具体EBI分配优先级标识的优先级配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ebiAssignpriId|EBI分配优先级标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置EBI分配优先级的标识。
arpPriLev|ARP优先级|参数可选性: 任选参数类型: 数字参数范围: 1-15|该参数用于设置ARP优先级。
arpEmptionCap|ARP抢占能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置ARP抢占能力，选项如下。抢占不能抢占
arpEmptionVul|ARP被抢占能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置ARP被抢占能力，选项如下。被抢占不被抢占
snssaiSST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
snssaiSD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
priority|EBI分配优先级|参数可选性: 必选参数类型: 数字参数范围: 1-15|该参数用于设置EBI分配优先级，参数取值范围：1~15
命令举例 
`
修改一个基于S_NSSAI和ARP 的优先级配置，其中EBI分配优先级标识值为1：
MOD 5GEBIASSIGNPRIORITY:EBIASSIGNPRIID=1,ARPPRILEV=2,PRIORITY=5
` 
#### 删除基于S_NSSAI和ARP 的优先级配置(DEL 5GEBIASSIGNPRIORITY) 
#### 删除基于S_NSSAI和ARP 的优先级配置(DEL 5GEBIASSIGNPRIORITY) 
功能说明 
该命令用于删除一个具体EBI分配优先级标识的优先级配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ebiAssignpriId|EBI分配优先级标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置EBI分配优先级的标识。
命令举例 
`
删除一个基于S_NSSAI和ARP 的优先级配置，其中EBI分配优先级标识值为1：
DEL 5GEBIASSIGNPRIORITY:EBIASSIGNPRIID=1
` 
#### 查询基于S_NSSAI和ARP 的优先级配置(SHOW 5GEBIASSIGNPRIORITY) 
#### 查询基于S_NSSAI和ARP 的优先级配置(SHOW 5GEBIASSIGNPRIORITY) 
功能说明 
该命令用于查询一个具体EBI分配优先级标识的优先级配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ebiAssignpriId|EBI分配优先级标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置EBI分配优先级的标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ebiAssignpriId|EBI分配优先级标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置EBI分配优先级的标识。
arpPriLev|ARP优先级|参数可选性: 任选参数类型: 数字参数范围: 1-15|该参数用于设置ARP优先级。
arpEmptionCap|ARP抢占能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置ARP抢占能力，选项如下。抢占不能抢占
arpEmptionVul|ARP被抢占能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置ARP被抢占能力，选项如下。被抢占不被抢占
snssaiSST|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
snssaiSD|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
priority|EBI分配优先级|参数可选性: 任选参数类型: 数字参数范围: 1-15|该参数用于设置EBI分配优先级，参数取值范围：1~15
命令举例 
`
查询基于S_NSSAI和ARP 的优先级配置
SHOW 5GEBIASSIGNPRIORITY:
(No.19) : SHOW 5GEBIASSIGNPRIORITY:
-----------------Namf_Communication_0----------------
EBI分配优先级标识   ARP优先级   ARP抢占能力  ARP被抢占能力   SNSSAI   SST   SNSSAI   SD   EBI分配优先级
1                           1                不抢占           不被抢占            eMBB     11     5
记录数：1
执行成功耗时: 0.062 秒
` 
## EPC加密配置 
## EPC加密配置 
背景知识 
4/5G切换过程中，需要包含已协商好的EPS NAS安全算法，终端接入5G时，AMF提前为终端分配好EPS NAS安全算法。在4/5G切换时，由AMF发送给MME。切换完成后，如果MME希望重协商算法，可通过SMC流程进行算法重协商。 
功能说明 
本功能用于设置4/5G互操作过程中，AMF协商的EPS NAS加密算法。 
当开启4/5G互操作，且需要基于N26接口互操作时，会使用此配置。 
子主题： 
### 修改EPC加密配置(SET EPC NAS ENCRYPT CONFIG) 
### 修改EPC加密配置(SET EPC NAS ENCRYPT CONFIG) 
功能说明 
该命令用于设置或修改协商EPS NAS加密算法时的参数， 包括AMF所支持的各种算法和对应的优先级 。  
当开启4/5G互操作功能，且要求支持基于N26接口的互操作时，需要使用此配置设置4G加密算法的协商参数。设置成功之后，对于支持S1模式的终端，AMF会在安全模式过程中，将协商EPS NAS加密算法携带给终端。 同时在终端切换到4G MME时，AMF将此算法携带给MME，用于切换使用。  
注意事项 
在配置本命令时，还需要同时设置EPS NAS完整性保护算法的协商参数，参见命令[SET EPC NAS INTEGRATE CONFIG]
输入参数说明 
标识|名称|类型|说明
---|---|---|---
epc_ea0|4G EA0算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS加密算法EA0。加密算法EA0为空算法。
epc_ea0AlgPriority|4G EA0算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA0加密算法的优先级。如果终端和网络侧同时支持多种算法，则依据优先级为终端选择最终的加密算法。 优先级0最高，7最低。
epc_ea1|4G EA1算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS加密算法EA1。
epc_ea1AlgPriority|4G EA1算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA1加密算法的优先级。 如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。优先级0最高，7最低。
epc_ea2|4G EA2算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设AMF是否支持加密算法EPS NAS EA2。
epc_ea2AlgPriority|4G EA2算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA2加密算法的优先级。如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。 优先级0最高，7最低。
epc_ea3|4G EA3算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS加密算法EA3。
epc_ea3AlgPriority|4G EA3算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA3加密算法的优先级。 如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。 优先级0最高，7最低。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
epc_ea0|4G EA0算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS加密算法EA0。加密算法EA0为空算法。
epc_ea0AlgPriority|4G EA0算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA0加密算法的优先级。如果终端和网络侧同时支持多种算法，则依据优先级为终端选择最终的加密算法。 优先级0最高，7最低。
命令举例 
`
设置EPC NAS加密算法，支持EA0算法，优先级1； 支持EA1，优先级2； 支持EA2，优先级3；不支持EA3算法。
SET EPC NAS ENCRYPT CONFIG:EPC_EA0="EPCEA0SUPPORT",EPC_EA0ALGPRIORITY=1,EPC_EA1="EPCEA1SUPPORT",EPC_EA1ALGPRIORITY=2,EPC_EA2="EPCEA2SUPPORT",EPC_EA2ALGPRIORITY=3,EPC_EA3="EPCEA3NOSUPPORT",EPC_EA3ALGPRIORITY=4
` 
### 查询EPC加密配置(SHOW EPC NAS ENCRYPT CONFIG) 
### 查询EPC加密配置(SHOW EPC NAS ENCRYPT CONFIG) 
功能说明 
该命令用于查询AMF配置的EPS加密算法协商参数。  
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
epc_ea0|4G EA0算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS加密算法EA0。加密算法EA0为空算法。
epc_ea0AlgPriority|4G EA0算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA0加密算法的优先级。如果终端和网络侧同时支持多种算法，则依据优先级为终端选择最终的加密算法。 优先级0最高，7最低。
epc_ea1|4G EA1算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS加密算法EA1。
epc_ea1AlgPriority|4G EA1算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA1加密算法的优先级。 如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。优先级0最高，7最低。
epc_ea2|4G EA2算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设AMF是否支持加密算法EPS NAS EA2。
epc_ea2AlgPriority|4G EA2算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA2加密算法的优先级。如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。 优先级0最高，7最低。
epc_ea3|4G EA3算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS加密算法EA3。
epc_ea3AlgPriority|4G EA3算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS EA3加密算法的优先级。 如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的加密算法。 优先级0最高，7最低。
命令举例 
`
查询EPC NAS加密算法的支持情况。 
SHOW EPC NAS ENCRYPT CONFIG:
(No.13) : SHOW EPC NAS ENCRYPT CONFIG:
-----------------Namf_Communication_0----------------
4G EA0算法开关 4G EA0算法优先级 4G EA1算法开关 4G EA1算法优先级 4G EA2算法开关 4G EA2算法优先级 4G EA3算法开关 4G EA3算法优先级
支持4G加密算法0 0 支持4G加密算法1 1 支持4G加密算法2 2 不支持4G加密算法3 3
记录数：1
` 
## EPC完保配置 
## EPC完保配置 
背景知识 
4/5G切换过程中，需要包含已协商好的EPS NAS安全算法，用户接入5G时AMF提前为用户分配好EPS NAS安全算法。在4/5G切换时由AMF发送给MME。切换完成后如果MME希望重协商算法，可通过SMC流程进行算法重协商。  
功能说明 
本功能用于设置互操作过程中AMF协商的EPS完整性保护算法。当开启4/5G互操作，且需要基于N26互操作时，需要使用此配置。 此配置用于设置或修改协商EPS NAS完整性保护算法时的参数。 
子主题： 
### 修改EPC完保配置(SET EPC NAS INTEGRATE CONFIG) 
### 修改EPC完保配置(SET EPC NAS INTEGRATE CONFIG) 
功能说明 
该命令用于设置或修改协商EPS NAS完整性保护算法时的参数， 包括所支持的各种算法和对应的优先级 。  
当开启4/5G互操作功能，且要求支持基于N26接口的互操作时，需要使用此配置设置4G完整性保护算法的协商参数。设置成功之后，对于支持S1模式的终端，AMF会在安全模式过程中，将协商EPS NAS完整性保护算法携带给终端。 同时在终端切换到4G MME时，AMF将此算法携带给MME，用于切换使用。  
注意事项 
使用此配置时，还需要同时设置EPS NAS加密算法的协商参数，参见命令[SET EPC NAS ENCRYPT CONFIG]
输入参数说明 
标识|名称|类型|说明
---|---|---|---
epc_ia1|4G IA1算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS完整性保护算法IA1。
epc_ia1AlgPriority|4G IA1算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS完整性保护 算法IA1的优先级。 如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。优先级0最高，7最低。
epc_ia2|4G IA2算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持完整性保护算法EPC NAS IA2。
epc_ia2AlgPriority|4G IA2算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPC NAS 完整性保护算法IA2的优先级。如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。 优先级0最高，7最低。
epc_ia3|4G IA3算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持EPS NAS完整性保护算法IA3。
epc_ia3AlgPriority|4G IA3算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS完整性保护 算法IA3优先级。 如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。 优先级0最高，7最低。
命令举例 
`
设置EPS NAS完整性算法，算法IAI支持，优先级1； 算法IA2支持，优先级2；算法IA3不支持。
SET EPC NAS INTEGRATE CONFIG:EPC_IA1="EPCIA1SUPPORT",EPC_IA1ALGPRIORITY=1,EPC_IA2="EPCIA2SUPPORT",EPC_IA2ALGPRIORITY=2,EPC_IA3="EPCIA3NOSUPPORT"
` 
### 查询EPC完保配置(SHOW EPC NAS INTEGRATE CONFIG) 
### 查询EPC完保配置(SHOW EPC NAS INTEGRATE CONFIG) 
功能说明 
该命令用于查询AMF配置的EPS NAS的完整性保护算法协商参数。  
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
epc_ia1|4G IA1算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置AMF是否支持EPS NAS完整性保护算法IA1。
epc_ia1AlgPriority|4G IA1算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS完整性保护 算法IA1的优先级。 如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。优先级0最高，7最低。
epc_ia2|4G IA2算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持完整性保护算法EPC NAS IA2。
epc_ia2AlgPriority|4G IA2算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPC NAS 完整性保护算法IA2的优先级。如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。 优先级0最高，7最低。
epc_ia3|4G IA3算法开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置是否支持EPS NAS完整性保护算法IA3。
epc_ia3AlgPriority|4G IA3算法优先级|参数可选性: 任选参数类型: 数字参数范围: 0-7默认值: 7|该参数用于设置EPS NAS完整性保护 算法IA3优先级。 如果终端和AMF同时支持多种算法，则依据优先级为终端选择最终的完整性保护算法。 优先级0最高，7最低。
命令举例 
`
查看AMF上设置的EPS NAS完整性保护算法的支持情况及其优先级设置。
SHOW EPC NAS INTEGRATE CONFIG
SHOW EPC NAS INTEGRATE CONFIG:
-----------------Namf_Communication_0----------------
4G IA1算法开关 4G IA1算法优先级 4G IA2算法开关 4G IA2算法优先级 4G IA3算法开关 4G IA3算法优先级
支持4G完整性算法1 0 支持4G完整性算法2 1 不支持4G完整性算法3 2
记录数：1
执行成功耗时: 0.12 秒
` 
## MME主机解析配置 
## MME主机解析配置 
背景知识 
在Interworking with N26的4/5G互操作场景下，如果终端用户从5G网络切换到4G网络，则AMF需根据TA等信息解析MME的IP地址列表，如果终端用户从4G网络切换到到5G网络，则AMF需根据MME GUMMEI解析Old MME。 
在AMF根据TA等信息解析到MME的IP地址列表后，AMF可以根据AMF的优先级、权重、子网优先级等信息选择合适的MME。 
功能说明 
MME主机解析配置包括MME主机地址解析配置、MME地址选择策略配置、MME地址解析优选子网段配置、地址池配置 
子主题： 
### 地址池配置 
### 地址池配置 
背景知识 
当DNS服务器出现故障，或者测试局点进行测试而不需要配置DNS服务器时，AMF需要通过本功能配置的MME地址解析数据，查询MME地址。 
功能说明 
本功能用于配置某个IP地址池下的MME的IP地址。 
子主题： 
#### 新增地址池配置(ADD ADDRPOOL) 
#### 新增地址池配置(ADD ADDRPOOL) 
功能说明 
该命令需要和[ADD MMEHOST]命令配合使用，本命令用于配置地址池ID对应的MME地址，一个地址池可以配置多个地址。
注意事项 
本命令需要和[ADD MMEHOST]命令配合使用，命令配置的地址池ID后续在[ADD MMEHOST]命令中被引用。
单个地址池最多只支持15个IP地址，超过15个后，只取前面15个。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ipType|IP类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置IP地址的类型，可以选择“IPv4”或者“IPv6”。
ipAddr|IP地址|参数可选性: 必选参数类型: 字符串|该参数用于设置IP地址，可以是IPv4格式，也可以是IPv6格式。
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于设置IP地址池标识，该地址池标识需要和ADD MMEHOST命令中的“地址池标识（addrPoolID）”一致。
命令举例 
`
添加IP地址标识为1，IP地址为“192.168.22.22”，IP类型为IPv4的记录。
ADD ADDRPOOL:IPTYPE="IPV4",IPADDR="192.168.22.22",ADDRPOOLID=1
` 
#### 删除地址池配置(DEL ADDRPOOL) 
#### 删除地址池配置(DEL ADDRPOOL) 
功能说明 
该命令用于删除地址池ID对应的MME地址，可以一次性删除某个地址池对应的所有地址，或者删除某个具体地址。 
注意事项 
删除某个具体地址，需要填写待删除的IP地址和地址池ID。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ipType|IP类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置IP地址的类型，可以选择“IPv4”或者“IPv6”。
ipAddr|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IP地址，可以是IPv4格式，也可以是IPv6格式。
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP地址池标识，该地址池标识需要和ADD MMEHOST命令中的“地址池标识（addrPoolID）”一致。
命令举例 
`
删除地址池为2的所有地址
DEL ADDRPOOL:ADDRPOOLID=2
删除1个特定地址
DEL ADDRPOOL:IPTYPE="IPV4",IPADDR="192.168.29.29",ADDRPOOLID=1
` 
#### 查询地址池配置(SHOW ADDRPOOL) 
#### 查询地址池配置(SHOW ADDRPOOL) 
功能说明 
该命令用于查询MME地址池对应的地址配置，可以查询所有的地址，还可以查询某个地址池对应的地址。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP地址池标识，该地址池标识需要和ADD MMEHOST命令中的“地址池标识（addrPoolID）”一致。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ipType|IP类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|该参数用于设置IP地址的类型，可以选择“IPv4”或者“IPv6”。
ipAddr|IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置IP地址，可以是IPv4格式，也可以是IPv6格式。
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于设置IP地址池标识，该地址池标识需要和ADD MMEHOST命令中的“地址池标识（addrPoolID）”一致。
命令举例 
`
显示所有配置的地址池记录。
SHOW ADDRPOOL
(No.2) : SHOW ADDRPOOL:
-----------------Namf_Communication_0----------------
IP类型    IP地址         地址池标识
0           94.60.20.1    65535
记录数：1
执行成功耗时: 0.339 秒
查询单个地址池信息。
SHOW ADDRPOOL:ADDRPOOLID=1
(No.4) : SHOW ADDRPOOL:ADDRPOOLID=1
-----------------Namf_Communication_0_A----------------
操作维护       IP类型 IP地址  地址池标识 
-----------------------------------------
复制  删除      IPV4   1.1.1.1 1          
-----------------------------------------
记录数：1
执行成功开始时间:2020-10-16 10:43:32 耗时: 0.13 秒
` 
### MME主机地址解析配置 
### MME主机地址解析配置 
背景知识 
在Interworking with N26的4/5G互操作场景下，如果终端用户从5G网络切换到4G网络，则AMF需根据TA等信息解析MME的IP地址列表，如果终端用户从4G网络切换到到5G网络，则AMF需根据MME GUMMEI解析Old MME。 
功能说明 
本功能用于配置逻辑名称，主机名对应的IP地址池标识，优先级和权重。 
子主题： 
#### 新增MME地址解析配置(ADD MMEHOST) 
#### 新增MME地址解析配置(ADD MMEHOST) 
功能说明 
该命令用于新增MME地址解析配置。 
当DNS服务器出现故障，或者测试局点进行测试而不需要配置DNS服务器时，AMF需要通过本命令配置的MME地址解析数据，查询MME地址。 
注意事项 
确定一个MME地址解析记录，需要二个关键字：FQDN和主机名。
相同的FQDN，可以配置具有不同主机名的MME地址解析记录。比如：ADD MMEHOST:LOGICNAME="mmec86.mmegi0140.mme.epc.mnc002.mcc460.3gppnetwork.org",HOSTNAME="mme22",PRIORITY=1,WEIGHT=100,ADDRPOOLID=1;和ADD MMEHOST:LOGICNAME="tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org",HOSTNAME="mme23",PRIORITY=10,WEIGHT=200,ADDRPOOLID=1。 
如果存在多个优先级相同的IP地址池，则先通过轮选方式从这些IP地址池中选中一个地址池，然后从这个选中的地址池中按照[ADD HOSTSUBNETPRI]命令配置的IP子网优先级进行选择，最后选择一个MME地址。
单个FQDN最多只支持8个主机名，超过8个后，只取前面8个。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
hostName|主机名|参数可选性: 必选参数类型: 字符串参数范围: 1-100|本参数用于设置MME的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
priority|优先级|参数可选性: 必选参数类型: 数字参数范围: 0-65535默认值: 0|查询MME网元IP地址时，根据TAI FQDN或者MME FQDN查询得到多组MME FQDN地址解析。此时，根据该参数从查询得到的多组MME FQDN地址解析中，选择优先级最高的MME FQDN地址解析。
weight|权重|参数可选性: 必选参数类型: 数字参数范围: 0-65535默认值: 200|查询MME网元IP地址时，根据TAI FQDN或者MME FQDN查询得到多组MME FQDN地址解析。此时，首先根据优先级从查询得到的多组MME FQDN地址解析中，选择优先级最高的MME FQDN地址解析。若多组MME FQDN地址解析都配置了最高优先级，则根据该参数在此多组MME FQDN地址解析中随机选择一组EPC FQDN地址解析。
addrPoolID|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|网元IP地址池标识。每个IP地址池对应的IP列表在“MME地址池配置”里面配置
命令举例 
`
添加FQDN为"tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org”，主机名称为“mme1”，优先级为1，权重为50，地址池为1的MME地址解析记录。
ADD MMEHOST:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",HOSTNAME="mme1",PRIORITY=1,WEIGHT=50,ADDRPOOLID=1
添加MME FQDN记录：
ADD MMEHOST:LOGICNAME="mmec86.mmegi0140.mme.epc.mnc002.mcc460.3gppnetwork.org",HOSTNAME="mme22",PRIORITY=1,WEIGHT=100,ADDRPOOLID=1
` 
#### 修改MME地址解析配置(SET MMEHOST) 
#### 修改MME地址解析配置(SET MMEHOST) 
功能说明 
该命令用于修改特定FQDN和主机名对应的本地地址解析配置的IP地址池配置、优先级和权重。当目标地址，权重，优先级发生改变，使用该命令。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
hostName|主机名|参数可选性: 必选参数类型: 字符串参数范围: 1-100|本参数用于设置MME的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|查询MME网元IP地址时，根据TAI FQDN或者MME FQDN查询得到多组MME FQDN地址解析。此时，根据该参数从查询得到的多组MME FQDN地址解析中，选择优先级最高的MME FQDN地址解析。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|查询MME网元IP地址时，根据TAI FQDN或者MME FQDN查询得到多组MME FQDN地址解析。此时，首先根据优先级从查询得到的多组MME FQDN地址解析中，选择优先级最高的MME FQDN地址解析。若多组MME FQDN地址解析都配置了最高优先级，则根据该参数在此多组MME FQDN地址解析中随机选择一组EPC FQDN地址解析。
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|网元IP地址池标识。每个IP地址池对应的IP列表在“MME地址池配置”里面配置
命令举例 
`
修改FQDN为“"tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org”，主机名为mme1的MME地址解析记录的优先级为2。
SET MMEHOST:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",HOSTNAME="mme1",PRIORITY=2
` 
#### 删除MME地址解析配置(DEL MMEHOST) 
#### 删除MME地址解析配置(DEL MMEHOST) 
功能说明 
该命令用于删除特定FQDN所对应的全部MME地址解析配置，或者特定MME地址解析配置。 
若要删除特定FQDN所对应的全部MME地址解析配置，则只需要填写“FQDN”这个参数。命令执行成功后，AMF将无法通过本地地址解析，获取“FQDN”所对应的任何目标局IP地址。 
若要删除特定MME地址解析配置，则需要填写“FQDN”、“主机名”。命令执行成功后，AMF将无法通过本地地址解析，获取“FQDN”与“主机名”所对应的目标局IP地址。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
hostName|主机名|参数可选性: 任选参数类型: 字符串参数范围: 1-100|本参数用于设置MME的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
命令举例 
`
删除FQDN为“"tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org”的MME地址解析记录。
DEL MMEHOST:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org"
删除指定FQDN和主机名下的配置。
DEL MMEHOST:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",HOSTNAME="mme1"
` 
#### 查询MME地址解析配置(SHOW MMEHOST) 
#### 查询MME地址解析配置(SHOW MMEHOST) 
功能说明 
该命令用于查询全部MME地址解析配置、特定FQDN所对应的全部MME地址解析配置、特定FQDN和主机名所对应的特定EPC地址解析配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
hostName|主机名|参数可选性: 任选参数类型: 字符串参数范围: 1-100|本参数用于设置MME的主机名称，由最多不超过100个ASCII码符号组成。一般采用类似于DNS域名的点分格式，比如mme50.zte.com.cn。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|查询MME网元IP地址时，根据TAI FQDN或者MME FQDN查询得到多组MME FQDN地址解析。此时，根据该参数从查询得到的多组MME FQDN地址解析中，选择优先级最高的MME FQDN地址解析。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|查询MME网元IP地址时，根据TAI FQDN或者MME FQDN查询得到多组MME FQDN地址解析。此时，首先根据优先级从查询得到的多组MME FQDN地址解析中，选择优先级最高的MME FQDN地址解析。若多组MME FQDN地址解析都配置了最高优先级，则根据该参数在此多组MME FQDN地址解析中随机选择一组EPC FQDN地址解析。
addrPoolID|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|网元IP地址池标识。每个IP地址池对应的IP列表在“MME地址池配置”里面配置
命令举例 
`
查询所有的MME地址解析配置。
SHOW MMEHOST
(No.1) : SHOW MMEHOST:
-----------------Namf_Communication_0----------------
FQDN                                                                                 主机名    优先级   权重   地址池标识
tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org   mme22   10         200   1
记录数：1
执行成功耗时: 0.089 秒
` 
### MME地址解析优选子网段配置 
### MME地址解析优选子网段配置 
背景知识 
当DNS服务器出现故障，或者测试局点进行测试而不需要配置DNS服务器时，AMF需要通过本功能配置的MME地址解析数据，查询MME地址。 
功能说明 
本功能用于配置每个子网段对应的优先级。 
子主题： 
#### 新增MME地址解析优选子网配置(ADD HOSTSUBNETPRI) 
#### 新增MME地址解析优选子网配置(ADD HOSTSUBNETPRI) 
功能说明 
该命令用于AMF新增MME地址解析优选子网配置。 
在特定MME地址解析配置中，配置了分属不同网段的目标IP地址时，AMF可以使用该命令设置不同子网段的优先级。 
该命令执行成功后，AMF依据配置的子网段优先级，选择具有最高子网段优先级的目标IP地址。 
注意事项 
新增该配置之前，首先需要通过[ADD MMEHOST]命令新增MME地址解析配置。
若具有最高子网段优先级的子网段对应多个目标IP地址，或者多个子网段具有相同的最高优先级，根据[SET MMESELECTPOLICYCFG]命令中配置的“优选IP类型（ Preferential IP type）”，如果终端优选IPv4的MME地址，并且选择结果中存在IPv4的地址，则选择IPv4的MME地址，否则优选IPV6的地址。
经过优选后，如果还存在多个地址的话，则只能随机选择一个作为目标MME地址。 
一个特定FQDN，最多可以包含16个子网段IP优先级。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
ipType|IP类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|IP地址类型，可以选择IPv4或者IPv6。
subnetAddr|子网地址|参数可选性: 必选参数类型: 字符串|本参数用于设置IPv4或者IPv6网络地址，比如10.24.0.0。
maskLen|掩码长度|参数可选性: 必选参数类型: 数字参数范围: 0-128|本参数用于设置IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
priority|优先级|参数可选性: 必选参数类型: 数字参数范围: 0-16|本参数用于设置IPv4或者IPv6网络地址中IP地址优先级。当MME地址解析配置中，配置了多个IP地址时，AMF根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
命令举例 
`
添加TAI FQDN为“tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org”，IP类型为IPv4，子网地址为“1.1.1.0”，掩码长度为24，优先级为1的记录：
ADD HOSTSUBNETPRI:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",IPTYPE="IPV4",SUBNETADDR="1.1.1.0",MASKLEN=24,PRIORITY=1
添加MME节点FQDN为“mmec86.mmegi0140.mme.epc.mnc002.mcc460.3gppnetwork.org”，IP类型为IPv4，子网地址为“2.1.1.0”，掩码长度为24，优先级为1的记录：
ADD HOSTSUBNETPRI:LOGICNAME="mmec86.mmegi0140.mme.epc.mnc002.mcc460.3gppnetwork.org",IPTYPE="IPV4",SUBNETADDR="2.1.1.0",MASKLEN=24,PRIORITY=1
` 
#### 修改MME地址解析优选子网配置(SET HOSTSUBNETPRI) 
#### 修改MME地址解析优选子网配置(SET HOSTSUBNETPRI) 
功能说明 
该命令用于AMF修改特定子网段优先级。当特定子网段优先级需要调整时，AMF使用该命令。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
ipType|IP类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1|IP地址类型，可以选择IPv4或者IPv6。
subnetAddr|子网地址|参数可选性: 必选参数类型: 字符串|本参数用于设置IPv4或者IPv6网络地址，比如10.24.0.0。
maskLen|掩码长度|参数可选性: 必选参数类型: 数字参数范围: 0-128|本参数用于设置IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-16|本参数用于设置IPv4或者IPv6网络地址中IP地址优先级。当MME地址解析配置中，配置了多个IP地址时，AMF根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
命令举例 
`
修改FQDN为“tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org”的记录，优先级为2:
SET HOSTSUBNETPRI:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",IPTYPE="IPV4",SUBNETADDR="1.1.1.0",MASKLEN=24,PRIORITY=2
` 
#### 删除MME地址解析优选子网配置(DEL HOSTSUBNETPRI) 
#### 删除MME地址解析优选子网配置(DEL HOSTSUBNETPRI) 
功能说明 
该命令用于删除特定FQDN所对应的全部子网段优先级配置，或者删除特定FQDN所对应的某个特定子网段优先级配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
ipType|IP类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|IP地址类型，可以选择IPv4或者IPv6。
subnetAddr|子网地址|参数可选性: 任选参数类型: 字符串|本参数用于设置IPv4或者IPv6网络地址，比如10.24.0.0。
maskLen|掩码长度|参数可选性: 任选参数类型: 数字参数范围: 0-128|本参数用于设置IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
命令举例 
`
删除特定FQDN下所有的子网段优先级配置：
DEL HOSTSUBNETPRI:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org"
删除特定FQDN下某个具体的子网段优先级配置：
DEL HOSTSUBNETPRI:LOGICNAME="tac-lb01.tac-hb50.tac.epc.mnc011.mcc460.3gppnetwork.org",SUBNETADDR="1.1.1.0",MASKLEN=24
` 
#### 查询MME地址解析优选子网配置(SHOW HOSTSUBNETPRI) 
#### 查询MME地址解析优选子网配置(SHOW HOSTSUBNETPRI) 
功能说明 
该命令用于查询特定FQDN所对应的全部子网段优先级配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
logicName|FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|本参数用于设置FQDN，包括两种：TAI FQDNMME节点FQDNTAI FQDNTA标识具有固定格式“tac-lbWW.tac-hbXX.tac.epc.mncYYY.mccZZZ.3gppnetwork.org”WW分别为2位数值表示的TAC的低字节，不足2位的，靠前补零。XX分别为2位数值表示的TAC的高字节，不足2位的，靠前补零。YYY、ZZZ为3位数值表示的MNC、MCC，不足3位的，靠前补零。W、X为十六进制数。Y、Z为十进制数。如：TAC低字节为1、高字节为2、MNC为3、MCC460时，格式为：tac-lb01.tac-hb02.tac.epc.mnc003.mcc460.3gppnetwork.orgMME节点FQDNMME节点标识具有固定形式“mmecXX.mmegiYYYY.mme.epc.mncZZZ.mccWWW.3gppnetwork.org”XX为2位数值表示的MMEC、不足2位的，靠前补零。YYYY为4位数值表示的MMEGI不足4位的，靠前补零。ZZZ、WWW分别为3位数值表示的MNC、MCC，不足3位的，靠前补零。X、Y为十六进制数。Z、W为十进制数。如：MMEC为2、MMEGI为3、MNC为4、MCC460时，格式为：mmec02.mmegi0003.mme.epc.mnc004.mcc460.3gppnetwork.orgFQDN只支持输入小写。
ipType|IP类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|IP地址类型，可以选择IPv4或者IPv6。
subnetAddr|子网地址|参数可选性: 任选参数类型: 字符串|本参数用于设置IPv4或者IPv6网络地址，比如10.24.0.0。
maskLen|掩码长度|参数可选性: 任选参数类型: 数字参数范围: 0-128|本参数用于设置IPv4或者IPv6网络地址掩码长度，比如网络10.24.0.0，其掩码长度为16。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-16|本参数用于设置IPv4或者IPv6网络地址中IP地址优先级。当MME地址解析配置中，配置了多个IP地址时，AMF根据各地址归属网络的优先级配置，选择优先级最高的IP地址。
命令举例 
`
查询MME地址解析优选子网段配置：
SHOW HOSTSUBNETPRI
(No.1) : SHOW HOSTSUBNETPRI:
-----------------Namf_Communication_0----------------
FQDN                                                       IP类型  子网地址        掩码长度    优先级
tac-lb02.tac-hb01.tac.epc.mnc011.mcc460.3gppnetwork.org    IPV4    192.168.0.0    16          10
记录数：1
执行成功 耗时: 0.063 秒
` 
### MME选择策略配置 
### MME选择策略配置 
背景知识 
用户在空闲态从4G移动到5G时发起注册请求，或者在连接态从5G移动到4G时NG-RAN发起切换请求，AMF收到请求后，根据TAI/MME节点标识组成逻辑名称，本地或者DNS解析得到目标局MME的IP地址。在进行MME地址解析时，根据不同的查询方式和过滤手段，可以按策略获取不同的MME地址，以保证切换流程的正常进行。 
功能说明 
本功能可设置及查询MME地址解析优先级、设置是否支持多SRV查询、是否支持权重和优先级切换目标MME以及优选IPV4或IPV6的MME地址。 
子主题： 
#### 设置MME选择策略配置(SET MMESELECTPOLICYCFG) 
#### 设置MME选择策略配置(SET MMESELECTPOLICYCFG) 
功能说明 
该命令用于设置AMF获取MME的IP地址的选择策略。 
AMF支持通过以下三种方式解析MME的地址。 
 
Host Local：表示本地解析，AMF通过本地配置的数据获取MME的地址。 
 
DNS Cache：DNS Cache是AMF本地的一个数据表，用于保存之前AMF到DNS服务器的历史查询结果，AMF在DNS Cache中查询需要获取的MME地址。  
 
DNS Server：AMF需要到DNS服务器进行解析，以获取MME的IP地址。 
 
注意事项 
 
本命令执行后，配置立即生效。 
 
本命令最多只能配置1条记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mmeAddrResolPri|MME地址解析优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: HOST_DCACHE_DSERVER|参数作用：该参数用于设置AMF获取MME地址的三种方式的优先级，共有4种组合方式，取值及含义如下：Host Local ->DNS Cache->DNS Server：表示AMF按本地解析、DNS Cache、DNS Server，这个顺序进行查询。 AMF可以先通过本地配置数据解析获取MME的地址，如果获到不到，再到DNS Cache中查询需要解析的域名，如果查询不到结果，再将域名发送到DNS服务器进行解析。Host Local ->DNS Server：表示AMF按本地解析、DNS Server，这个顺序进行查询。DNS Cache ->DNS Server->Host Local：表示AMF按DNS Cache、DNS Server本地解析，这个顺序进行查询。DNS Server ->Host Local：表示AMF按DNS Server、DNS Cache，这个顺序进行查询。修改影响：要根据实际网络部署情况，来配置优先级，如果修改错误会导致互操作流程信令负荷增加，造成系统不稳定。数据来源：本端规划。默认值：Host Local->DNS Cache->DNS Server。配置原则：无。
supportMutiSRV|支持多SRV查询|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|参数作用：该参数用于设置是否支持多SRV查询，DNS SRV是DNS记录中一种，用来查询指定服务的地址。与常见的A记录、CNAME不同的是，SRV中除了记录服务器的地址，还记录了服务的端口，并且可以设置每个服务地址的优先级和权重，AMF作为DNS Client访问DNS服务器的时候，AMF从DNS服务器查询到一个地址列表，根据优先级和权重，从中选取一个地址作为本次请求的目标地址，取值及含义如下：不支持：不支持多SRV查询时，无论DNS服务器返回多少个SRV，只有第一个SRV生效。支持：支持多SRV查询时，DNS服务器返回多少个SRV，AMF会处理多个SRV。修改影响：如果修改错误会导致4、5G互操作流程中，AMF选择MME失败，流程失败。数据来源：本端规划。默认值：支持。配置原则：无。
servIPType4DuStack|优选IP类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF本地查找目标MME时，优先选择的目标MME的IP类型，取值及含义如下：IPv4IPv6修改影响：根据本局IP支持情况来配置，如果修改错误，会导致选出来的MME地址类型和本局支持的不匹配，AMF和MME交互失败，流程失败。数据来源：本端规划。默认值：IPv4。配置原则：无。
amfSelMmeByPrior|支持通过权重和优先级选择切换目标MME|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF查找选择目标MME的顺序，在AMF选择MME时，需要确定按照“主机名优先级选择-子网优先级选择”顺序依次选择，还是只进行“IP子网优先级选择”，取值及含义如下：不支持：如果设置为“不支持”，则AMF只根据IP子网优先级选择目标MME。支持：如果设置为“支持”，则AMF按照“先根据主机名优先级选择，再根据IP子网优先级选择”的顺序依次选择目标MME。修改影响：如果修改错误会导致无法根据权重优先级选目标MME，导致无法平衡目标MME的负荷。数据来源：本端规划。默认值：支持。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supportMutiSRV|支持多SRV查询|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|参数作用：该参数用于设置是否支持多SRV查询，DNS SRV是DNS记录中一种，用来查询指定服务的地址。与常见的A记录、CNAME不同的是，SRV中除了记录服务器的地址，还记录了服务的端口，并且可以设置每个服务地址的优先级和权重，AMF作为DNS Client访问DNS服务器的时候，AMF从DNS服务器查询到一个地址列表，根据优先级和权重，从中选取一个地址作为本次请求的目标地址，取值及含义如下：不支持：不支持多SRV查询时，无论DNS服务器返回多少个SRV，只有第一个SRV生效。支持：支持多SRV查询时，DNS服务器返回多少个SRV，AMF会处理多个SRV。
命令举例 
`
设置MME地址解析优先级为 DNS Server -> Host Local，支持多SRV查询，优选IP类型为IPV4，支持通过权重和优先级选择切换目标MME。
SET MMESELECTPOLICYCFG:MMEADDRRESOLPRI="DSERVER_HOST",SUPPORTMUTISRV="SUPPORT",SERVIPTYPE4DUSTACK="IPv4",AMFSELMMEBYPRIOR="SUPPORT"
` 
#### 查询MME选择策略配置(SHOW MMESELECTPOLICYCFG) 
#### 查询MME选择策略配置(SHOW MMESELECTPOLICYCFG) 
功能说明 
该命令用于查询MME选择策略配置信息。 
注意事项 
无。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mmeAddrResolPri|MME地址解析优先级|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: HOST_DCACHE_DSERVER|参数作用：该参数用于设置AMF获取MME地址的三种方式的优先级，共有4种组合方式，取值及含义如下：Host Local ->DNS Cache->DNS Server：表示AMF按本地解析、DNS Cache、DNS Server，这个顺序进行查询。 AMF可以先通过本地配置数据解析获取MME的地址，如果获到不到，再到DNS Cache中查询需要解析的域名，如果查询不到结果，再将域名发送到DNS服务器进行解析。Host Local ->DNS Server：表示AMF按本地解析、DNS Server，这个顺序进行查询。DNS Cache ->DNS Server->Host Local：表示AMF按DNS Cache、DNS Server本地解析，这个顺序进行查询。DNS Server ->Host Local：表示AMF按DNS Server、DNS Cache，这个顺序进行查询。
supportMutiSRV|支持多SRV查询|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|参数作用：该参数用于设置是否支持多SRV查询，DNS SRV是DNS记录中一种，用来查询指定服务的地址。与常见的A记录、CNAME不同的是，SRV中除了记录服务器的地址，还记录了服务的端口，并且可以设置每个服务地址的优先级和权重，AMF作为DNS Client访问DNS服务器的时候，AMF从DNS服务器查询到一个地址列表，根据优先级和权重，从中选取一个地址作为本次请求的目标地址，取值及含义如下：不支持：不支持多SRV查询时，无论DNS服务器返回多少个SRV，只有第一个SRV生效。支持：支持多SRV查询时，DNS服务器返回多少个SRV，AMF会处理多个SRV。
servIPType4DuStack|优选IP类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF本地查找目标MME时，优先选择的目标MME的IP类型，取值及含义如下：IPv4IPv6
amfSelMmeByPrior|支持通过权重和优先级选择切换目标MME|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：该参数用于设置AMF查找选择目标MME的顺序，在AMF选择MME时，需要确定按照“主机名优先级选择-子网优先级选择”顺序依次选择，还是只进行“IP子网优先级选择”，取值及含义如下：不支持：如果设置为“不支持”，则AMF只根据IP子网优先级选择目标MME。支持：如果设置为“支持”，则AMF按照“先根据主机名优先级选择，再根据IP子网优先级选择”的顺序依次选择目标MME。
命令举例 
`
查询MME选择策略配置：
ZTE:>SHOW MMESELECTPOLICYCFG:
(No.1) : SHOW MMESELECTPOLICYCFG:
-----------------Namf_Communication_0----------------
MME地址解析优先级           支持多SRV查询    优选IP类型    支持通过权重和优先级选择切换目标MME
Host Local->DNS Server         支持           IPv4                    不支持
记录数：1
执行成功耗时: 0.179 秒
` 
### 号段选择MME配置 
### 号段选择MME配置 
背景知识 
AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入到哪个MME，主要用于运营商拨测场景。 
 
运维人员需要对新接入网络的MME进行功能测试，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME进行功能测试。 
 
当网络中的某个MME可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME，进行测试。 
 
功能说明 
AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入到哪个MME，主要用于运营商拨测场景。 
AMF在切换流程中，选择目标MME时，首先根据终端用户的GPSI/SUPI号码号段选择目标MME，在选择失败的情况下，后续再重新通过到DNS获取或本地解析这两种方式发现目标MME。 
子主题： 
#### 基于号段选择MME策略 
#### 基于号段选择MME策略 
背景知识 
AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入到哪个MME，主要用于运营商拨测场景。 
 
运维人员需要对新接入网络的MME进行功能测试，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME进行功能测试。 
 
当网络中的某个MME可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME，进行测试。 
 
功能说明 
AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入到哪个MME，主要用于运营商拨测场景。 
本配置用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入到哪个MME。 
子主题： 
##### 设置基于号段选择MME策略(SET SELECTMMEPLYBASENUMSEG) 
##### 设置基于号段选择MME策略(SET SELECTMMEPLYBASENUMSEG) 
功能说明 
该命令用于配置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入的MME。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supmmenumsel|支持基于号段选择MME|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入的MME。修改影响：修改参数为支持时，AMF基于终端用户的GPSI或SUPI号段选择一个需要切换接入的MME地址，然后进行从5G网络切换到4G网络的操作。数据来源：本端配置。默认值：不支持。配置原则：本参数需要根据运营商拨测场景进行配置：1、运维人员需要对新接入网络的MME进行功能测试，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME进行功能测试；2、当网络中的某个MME可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME，进行测试。
命令举例 
`
设置AMF支持基于号段选择MME。
SET SELECTMMEPLYBASENUMSEG:SUPMMENUMSEL="SPRT"
` 
##### 查询基于号段选择MME策略(SHOW SELECTMMEPLYBASENUMSEG) 
##### 查询基于号段选择MME策略(SHOW SELECTMMEPLYBASENUMSEG) 
功能说明 
该命令用于查询AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入的MME。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supmmenumsel|支持基于号段选择MME|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入的MME。修改影响：修改参数为支持时，AMF基于终端用户的GPSI或SUPI号段选择一个需要切换接入的MME地址，然后进行从5G网络切换到4G网络的操作。数据来源：本端配置。默认值：不支持。配置原则：本参数需要根据运营商拨测场景进行配置：1、运维人员需要对新接入网络的MME进行功能测试，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME进行功能测试；2、当网络中的某个MME可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME，进行测试。
命令举例 
`
查询基于号段选择MME策略配置。 
SHOW SELECTMMEPLYBASENUMSEG:
(No.6) : SHOW SELECTMMEPLYBASENUMSEG:
-----------------Namf_Communication_0----------------
操作维护       info   
----------------------
修改           不支持 
----------------------
记录数：1
执行成功开始时间:2021-06-21 20:29:57 耗时: 0.242 秒
` 
#### 基于号段选择MME配置 
#### 基于号段选择MME配置 
背景知识 
AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入到哪个MME，主要用于运营商拨测场景。 
 
运维人员需要对新接入网络的MME进行功能测试，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME进行功能测试。 
 
当网络中的某个MME可能有问题或者故障，运维人员需要确认其是否故障，AMF能够根据测试用户的GPSI/SUPI号码，将该用户切换接入到该MME，进行测试。 
 
功能说明 
AMF支持基于终端用户的GPSI/SUPI号段来为终端用户选择切换接入到哪个MME，主要用于运营商拨测场景。 
本功能提供基于号段选择MME的配置，包括：用户号段、号码类型、优先级，权重和有效时长的配置。 
子主题： 
##### 新增基于号段选择MME配置(ADD SELECTMMECFGBYNUMSEG) 
##### 新增基于号段选择MME配置(ADD SELECTMMECFGBYNUMSEG) 
功能说明 
该命令新增基于号段选择MME配置，用于拨测场景，让某一部分测试用户选择到指定的MME。该命令配置的数据包括GPSI/SUPI号段、地址池标识、优先级、权重和有效期。 
该命令的配置结果可以通过[SHOW SELECTMMECFGBYNUMSEG]命令进行查询。
注意事项 
如需要在基于GPSI/SUPI号段选择MME配置中配置地址池，必须先配置MME地址池。可以通过[SHOW ADDRPOOL]命令查询当前已配置的MME地址池。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：不能修改。数据来源：本端配置。默认值：无。配置原则：无。
number|用户号码|参数可选性: 必选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：该字段和号码类型可以确定一组或多组MME号段地址解析，后面再根据优先级和权重参数，选出一个MME地址。数据来源：本端配置。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置终端用户的号码类型。修改影响：该参数有两个选项：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）数据来源：本端配置。默认值：无。配置原则：无。
ipaddresspoolid|地址池标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置MME IP地址池标识。修改影响：无。数据来源：本端配置。默认值：无。配置原则：每个IP地址池对应的IP列表是通过ADD ADDRPOOL命令配置的，需要先通过SHOW ADDRPOOL命令查询获取当前的配置记录。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置一组数据的优先级。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。根据该参数从查询得到的多组MME号段地址解析中，选择优先级最高的MME地址。数据来源：本端配置。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置一组数据的权重。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。此时，首先根据优先级从查询得到的多组MME号段地址解析中，选择优先级最高的MME 号段地址解析。若多组MME号段地址解析都配置了最高优先级，则根据该参数在此多组MME 号段地址解析中随机选择一个MME地址。数据来源：本端配置。默认值：200。配置原则：无。
validityperiod|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长为空表示号段解析无有效截止日期。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。如果某一组的有效时间小于当前时间，则此组数据无效，如果为空，则表示这组数据无有效截止时间。数据来源：本端配置。默认值：无。配置原则：无。
命令举例 
`
新增一条基于GPSI/SUPI号段选择MME配置，其中编号为1，用户号码为13895122456，号码类型为GPSI，地址池标识为1，优先级为1，权重为10，有效时间为2020-01-20 11:16:38。
ADD SELECTMMECFGBYNUMSEG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",IPADDRESSPOOLID=1,PRIORITY=1,WEIGHT=10,VALIDITYPERIOD="2020-01-20 11:16:38"
` 
##### 修改基于号段选择MME配置(SET SELECTMMECFGBYNUMSEG) 
##### 修改基于号段选择MME配置(SET SELECTMMECFGBYNUMSEG) 
功能说明 
该命令修改基于号段选择MME配置，让某一部分测试用户选择到指定的MME。 
该命令的配置结果可以通过[SHOW SELECTMMECFGBYNUMSEG]命令进行查询。
注意事项 
如需要修改基于GPSI/SUPI号段选择MME配置中的地址池，该地址池必须存在。可以通过[SHOW ADDRPOOL]命令查询已配置的MME地址池。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：不能修改。数据来源：本端配置。默认值：无。配置原则：无。
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：该字段和号码类型可以确定一组或多组MME号段地址解析，后面再根据优先级和权重参数，选出一个MME地址。数据来源：本端配置。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置终端用户的号码类型。修改影响：该参数有两个选项：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）数据来源：本端配置。默认值：无。配置原则：无。
ipaddresspoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置MME IP地址池标识。修改影响：无。数据来源：本端配置。默认值：无。配置原则：每个IP地址池对应的IP列表是通过ADD ADDRPOOL命令配置的，需要先通过SHOW ADDRPOOL命令查询获取当前的配置记录。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置一组数据的优先级。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。根据该参数从查询得到的多组MME号段地址解析中，选择优先级最高的MME地址。数据来源：本端配置。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置一组数据的权重。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。此时，首先根据优先级从查询得到的多组MME号段地址解析中，选择优先级最高的MME 号段地址解析。若多组MME号段地址解析都配置了最高优先级，则根据该参数在此多组MME 号段地址解析中随机选择一个MME地址。数据来源：本端配置。默认值：200。配置原则：无。
validityperiod|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长为空表示号段解析无有效截止日期。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。如果某一组的有效时间小于当前时间，则此组数据无效，如果为空，则表示这组数据无有效截止时间。数据来源：本端配置。默认值：无。配置原则：无。
命令举例 
`
修改一条基于GPSI/SUPI号段选择MME配置，其中，修改ID为1的用户号码为13895122456，号码类型为GPSI，地址池标识为1，优先级为1，权重为10。
SET SELECTMMECFGBYNUMSEG:ID=1,NUMBER="13895122456",NUMTYPE="GPSI",IPADDRESSPOOLID=1,PRIORITY=1,WEIGHT=10
` 
##### 删除基于号段选择MME配置(DEL SELECTMMECFGBYNUMSEG) 
##### 删除基于号段选择MME配置(DEL SELECTMMECFGBYNUMSEG) 
功能说明 
该命令删除基于号段选择MME的配置数据。 
该命令的配置结果可以通过[SHOW SELECTMMECFGBYNUMSEG]命令进行查询。
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 必选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：不能修改。数据来源：本端配置。默认值：无。配置原则：无。
命令举例 
`
删除一条基于GPSI/SUPI号段选择MME配置，其中编号为1。
DEL SELECTMMECFGBYNUMSEG:ID=1
` 
##### 查询基于号段选择MME配置(SHOW SELECTMMECFGBYNUMSEG) 
##### 查询基于号段选择MME配置(SHOW SELECTMMECFGBYNUMSEG) 
功能说明 
该命令用于查询基于号段选择MME的配置数据。 
可以查询所有配置，也可以按号码段查询特定配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：不能修改。数据来源：本端配置。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
id|编号|参数可选性: 任选参数类型: 数字参数范围: 1-4096|参数作用：该参数为每个配置赋予不同的编号，用于区分不同配置。修改影响：不能修改。数据来源：本端配置。默认值：无。配置原则：无。
number|用户号码|参数可选性: 任选参数类型: 字符串参数范围: 10-15|参数作用：该参数用于设置GPSI/SUPI号码或号段。修改影响：该字段和号码类型可以确定一组或多组MME号段地址解析，后面再根据优先级和权重参数，选出一个MME地址。数据来源：本端配置。默认值：无。配置原则：无。
numtype|号码类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-2默认值: GPSI|参数作用：该参数用于设置终端用户的号码类型。修改影响：该参数有两个选项：GPSI（Generic Public Subscription Identifier，一般公共用户标识）SUPI（Subscriber Permanent Identifier，用户永久标识）数据来源：本端配置。默认值：无。配置原则：无。
ipaddresspoolid|地址池标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|参数作用：该参数用于设置MME IP地址池标识。修改影响：无。数据来源：本端配置。默认值：无。配置原则：每个IP地址池对应的IP列表是通过ADD ADDRPOOL命令配置的，需要先通过SHOW ADDRPOOL命令查询获取当前的配置记录。
priority|优先级|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于设置一组数据的优先级。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。根据该参数从查询得到的多组MME号段地址解析中，选择优先级最高的MME地址。数据来源：本端配置。默认值：0。配置原则：无。
weight|权重|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 200|参数作用：该参数用于设置一组数据的权重。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。此时，首先根据优先级从查询得到的多组MME号段地址解析中，选择优先级最高的MME 号段地址解析。若多组MME号段地址解析都配置了最高优先级，则根据该参数在此多组MME 号段地址解析中随机选择一个MME地址。数据来源：本端配置。默认值：200。配置原则：无。
validityperiod|有效时间|参数可选性: 任选参数类型: 字符串参数范围: 19-25|参数作用：该参数表示本号段解析的有效截止日期，输入标准的年月日时分秒格式的时间,比如2020-01-20 11:16:38。有效时长为空表示号段解析无有效截止日期。修改影响：通过用户号码和号码类型可以确定一组或多组MME号段地址解析。如果某一组的有效时间小于当前时间，则此组数据无效，如果为空，则表示这组数据无有效截止时间。数据来源：本端配置。默认值：无。配置原则：无。
命令举例 
`
查询所有基于GPSI/SUPI号段选择MME配置。
SHOW SELECTMMECFGBYNUMSEG
(No.5) : SHOW SELECTMMECFGBYNUMSEG:
-----------------Namf_Communication_0----------------
操作维护       编号  用户号码    号码类型 地址池标识 优先级 权重 有效时间 
-------------------------------------------------------------------------
复制 修改 删除  1    13895122456 GPSI     1          1      10  2020-01-20 11:16:38          
-------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-06-21 20:07:34 耗时: 0.975 秒
` 
## 互操作SNSSAI配置 
## 互操作SNSSAI配置 
背景知识 
S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息） 可用于标识网络切片，由SST（Slice/Service Type，切片/服务类型）和SD（Slice Differentiator，切片区分信息）组成。 
 
SST（Service/Slice Type）：业务或切片类型，如eMBB、mMTC、uRLLC，后续可以继续扩展。 
 
SD：其它可以区分切片的信息，比如区域信息，租户信息等。 
 
功能说明 
HR（Home routed，归属地）漫游时，如果终端通过N26接口从4G网络切换到5G网络，AMF需要选择一个默认的Visit SMF，这时可以根据DNN或者DNN+默认Visit SMF对应的S-NSSAI来选择Visit SMF。 
本功能用于配置这个默认Visit SMF对应的S-NSSAI。 
子主题： 
### 设置互操作的SNSSAI配置(SET INTERWORKINGSNSSAI) 
### 设置互操作的SNSSAI配置(SET INTERWORKINGSNSSAI) 
功能说明 
HR（Home routed，归属地）漫游时，如果终端通过N26接口从4G网络切换到5G网络，AMF需要选择一个默认的Visit SMF，这时可以根据DNN或者DNN+默认Visit SMF对应的S-NSSAI来选择Visit SMF。  
本命令用于配置这个默认Visit SMF对应的S-NSSAI。  
配置成功后，如果本AMF能满足终端请求和签约的NSSAI，则不需要向NSSF进行切片选择。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
命令举例 
`
设置互操作的S-NSSAI，SST为eMBB，SD为"abcdef"。
SET INTERWORKINGSNSSAI:SST="eMBB",SD="ABCDEF"
` 
### 查询互操作的SNSSAI配置(SHOW INTERWORKINGSNSSAI) 
### 查询互操作的SNSSAI配置(SHOW INTERWORKINGSNSSAI) 
功能说明 
本命令用于查询互操作的S-NSSAI配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
sst|SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255|该参数用于配置SST（Slice/Service Type，切片/服务类型）的编号，其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
sd|SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|该参数用于配置SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。
命令举例 
`
查询互操作的S-NSSAI配置。
SHOW INTERWORKINGSNSSAI:
(No.1):SHOW INTERWORKINGSNSSAI:
-----------------Namf_Communication_0----------------
操作维护       SST    SD     
-----------------------------
修改           1-eMBB ABCDEF 
-----------------------------
记录数 1
命令执行成功（耗时 0.031 秒）。
` 
## MME能力配置 
## MME能力配置 
背景知识 
在用户从5G移动4G场景下，AMF向SMF请求会话上下文信息时，告知SMF目标MME的能力，比如是否支持non-IP PDN类型，SMF基于目标MME的能力，决策是否返回non-IP的PDU会话类型。 
功能说明 
本功能用于用户从5G移动到4G时，配置目标MME能力。 
可配置缺省MME能力，也可配置指定IP的MME能力 
子主题： 
### 缺省MME能力配置 
### 缺省MME能力配置 
背景知识 
当全网规划MME具有相同能力，或者绝大部分MME具有相同能力时，可以配置缺省MME能力，提升开局效率。 
功能说明 
本功能用于用户从5G移动到4G时，配置目标MME缺省能力。 
子主题： 
#### 修改缺省MME能力配置(SET DEFMMECAPA) 
#### 修改缺省MME能力配置(SET DEFMMECAPA) 
功能说明 
该命令用于设置或修改缺省MME是否支持non-IP PDN类型。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
nonIpSprt|支持non-IP PDN类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置缺省MME是否支持non-IP PDN类型。
命令举例 
`
设置缺省MME支持non-IP PDN类型。 
SET DEFMMECAPA:NONIPSPRT="SPRT"
` 
#### 查询缺省MME能力配置(SHOW DEFMMECAPA) 
#### 查询缺省MME能力配置(SHOW DEFMMECAPA) 
功能说明 
该命令用于查询缺省MME是否支持non-IP PDN类型。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
nonIpSprt|支持non-IP PDN类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于设置缺省MME是否支持non-IP PDN类型。
命令举例 
`
查询缺省MME支持non-IP PDN类型。 
SHOW DEFMMECAPA:
(No.5) : SHOW DEFMMECAPA:
-----------------Namf_Communication_0----------------
支持non-IP PDN类型
是
记录数：1
执行成功耗时: 0.549 秒
` 
### 指定MME能力配置 
### 指定MME能力配置 
背景知识 
当用户从5G网络切换到4G网络时，AMF需要把MME是否具有支持non-IP PDN类型的能力告诉SMF，当网络中存在多个MME的时候，每个MME是否具有这样的能力，在AMF上都需要一一配置。 
当运营商整个5GC网络中规划的MME具有相同的能力，或者绝大部分MME具有相同能力时，可以配置一条缺省的MME能力，在这种情况下，在AMF上只需要配置一条缺省的MME能力即可，不需要对所有的MME一一进行配置，可以提升部署AMF的效率。 
与缺省的MME相对是的是指定MME，如果某些MME的能力与缺省MME能力不一致时，这些MME就是指定MME，可以在AMF上单独配置这些指定MME的能力，达到提升配置灵活性的目的。 
功能说明 
本功能用于当用户从5G网络切换到4G网络时，在AMF上配置指定MME的能力。 
这里的MME的能力是指，MME是否具有支持non-IP PDN类型的能力。 
子主题： 
#### 新增 指定MME能力配置(ADD SPECIALMMEIP) 
#### 新增 指定MME能力配置(ADD SPECIALMMEIP) 
功能说明 
本功能用于当用户从5G网络切换到4G网络时，在AMF上配置指定MME的能力。 
这里的MME的能力是指，MME是否具有支持non-IP PDN类型的能力。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mmeip|MME IP地址|参数可选性: 必选参数类型: 字符串|该参数用于设置指定MME的IP地址。当用户从5G网络切换到4G网络时，AMF需要把MME是否具有支持non-IP PDN类型的能力告诉SMF，当网络中存在多个MME的时候，每个MME是否具有这样的能力，在AMF上都需要一一配置。当运营商整个5GC网络中规划的MME具有相同的能力，或者绝大部分MME具有相同能力时，可以配置一条缺省的MME能力，在这种情况下，在AMF上只需要配置一条缺省的MME能力即可，不需要对所有的MME一一进行配置，可以提升部署AMF的效率。与缺省的MME相对是的是指定MME，如果某些MME的能力与缺省MME能力不一致时，这些MME就是指定MME，可以在AMF上单独配置这些指定MME的能力，达到提升配置灵活性的目的。
nonipsprt|支持non-IP PDN类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于配置指定的MME是否支持non-IP PDN类型。
命令举例 
`
配置IP为1.1.1.1的MME为指定MME，此MME支持non-IP PDN类型的能力。
ADD SPECIALMMEIP:MMEIP=1.1.1.1,NONIPSPRT="SPRT"
` 
#### 修改 指定MME能力配置(SET SPECIALMMEIP) 
#### 修改 指定MME能力配置(SET SPECIALMMEIP) 
功能说明 
该命令用于修改指定MME能力配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mmeip|MME IP地址|参数可选性: 必选参数类型: 字符串|该参数用于设置指定MME的IP地址。当用户从5G网络切换到4G网络时，AMF需要把MME是否具有支持non-IP PDN类型的能力告诉SMF，当网络中存在多个MME的时候，每个MME是否具有这样的能力，在AMF上都需要一一配置。当运营商整个5GC网络中规划的MME具有相同的能力，或者绝大部分MME具有相同能力时，可以配置一条缺省的MME能力，在这种情况下，在AMF上只需要配置一条缺省的MME能力即可，不需要对所有的MME一一进行配置，可以提升部署AMF的效率。与缺省的MME相对是的是指定MME，如果某些MME的能力与缺省MME能力不一致时，这些MME就是指定MME，可以在AMF上单独配置这些指定MME的能力，达到提升配置灵活性的目的。
nonipsprt|支持non-IP PDN类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于配置指定的MME是否支持non-IP PDN类型。
命令举例 
`
修改IP为1.1.1.1的MME的能力，修改为不支持non-IP PDN类型的能力。
SET SPECIALMMEIP:MMEIP="1.1.1.1",NONIPSPRT="NOSPRT"
` 
#### 删除 指定MME能力配置(DEL SPECIALMMEIP) 
#### 删除 指定MME能力配置(DEL SPECIALMMEIP) 
功能说明 
该命令用于删除指定MME能力配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mmeip|MME IP地址|参数可选性: 必选参数类型: 字符串|该参数用于设置指定MME的IP地址。当用户从5G网络切换到4G网络时，AMF需要把MME是否具有支持non-IP PDN类型的能力告诉SMF，当网络中存在多个MME的时候，每个MME是否具有这样的能力，在AMF上都需要一一配置。当运营商整个5GC网络中规划的MME具有相同的能力，或者绝大部分MME具有相同能力时，可以配置一条缺省的MME能力，在这种情况下，在AMF上只需要配置一条缺省的MME能力即可，不需要对所有的MME一一进行配置，可以提升部署AMF的效率。与缺省的MME相对是的是指定MME，如果某些MME的能力与缺省MME能力不一致时，这些MME就是指定MME，可以在AMF上单独配置这些指定MME的能力，达到提升配置灵活性的目的。
命令举例 
`
修改IP为1.1.1.1的MME，让其不再为AMF的指定MME。
DEL SPECIALMMEIP:MMEIP=1.1.1.1
` 
#### 查询 指定MME能力配置(SHOW SPECIALMMEIP) 
#### 查询 指定MME能力配置(SHOW SPECIALMMEIP) 
功能说明 
该命令用于查询指定MME能力配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mmeip|MME IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置指定MME的IP地址。当用户从5G网络切换到4G网络时，AMF需要把MME是否具有支持non-IP PDN类型的能力告诉SMF，当网络中存在多个MME的时候，每个MME是否具有这样的能力，在AMF上都需要一一配置。当运营商整个5GC网络中规划的MME具有相同的能力，或者绝大部分MME具有相同能力时，可以配置一条缺省的MME能力，在这种情况下，在AMF上只需要配置一条缺省的MME能力即可，不需要对所有的MME一一进行配置，可以提升部署AMF的效率。与缺省的MME相对是的是指定MME，如果某些MME的能力与缺省MME能力不一致时，这些MME就是指定MME，可以在AMF上单独配置这些指定MME的能力，达到提升配置灵活性的目的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mmeip|MME IP地址|参数可选性: 任选参数类型: 字符串|该参数用于设置指定MME的IP地址。当用户从5G网络切换到4G网络时，AMF需要把MME是否具有支持non-IP PDN类型的能力告诉SMF，当网络中存在多个MME的时候，每个MME是否具有这样的能力，在AMF上都需要一一配置。当运营商整个5GC网络中规划的MME具有相同的能力，或者绝大部分MME具有相同能力时，可以配置一条缺省的MME能力，在这种情况下，在AMF上只需要配置一条缺省的MME能力即可，不需要对所有的MME一一进行配置，可以提升部署AMF的效率。与缺省的MME相对是的是指定MME，如果某些MME的能力与缺省MME能力不一致时，这些MME就是指定MME，可以在AMF上单独配置这些指定MME的能力，达到提升配置灵活性的目的。
nonipsprt|支持non-IP PDN类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于配置指定的MME是否支持non-IP PDN类型。
命令举例 
`
查询配置的指定MME能力的信息。
SHOW SPECIALMMEIP
(No.1) : SHOW SPECIALMMEIP
-----------------Namf_Communication_0----------------
MME ip地址  支持non-IP PDN类型
1.1.1.1         是
记录数：1
执行成功耗时: 0.079 秒
` 
# 语音配置 
# 语音配置 
背景知识 
5G语音包括：VoNR（Voice over New Radio，新空口承载语音）和紧急呼叫。 
 
VoNR：UE通过5G网络接入IMS，使用IMS进行语音服务。 
 
紧急呼叫：5G网络通过与IMS网络建立紧急呼叫会话，来给终端提供紧急呼叫业务。 
 
功能说明 
本功能用于配置5G网络的VoNR业务和紧急呼叫业务。 
子主题： 
## VoNR配置 
## VoNR配置 
背景知识 
VoNR（Voice over New Radio，新空口承载语音）是基于5GC网络的语音解决方案，即在5GC覆盖区域内提供基于IP的高清晰语音业务。它是一种IP数据传输技术，全部业务承载于5G网络上，实现数据与语音业务在同一网络下的统一。换言之，5G网络提供高速率的数据业务，同时还提供高质量的音视频通话，音视频通话通过VoNR技术来实现。 
5G NR语音方案设计，延续了4G LTE通过IP网络承载语音业务的方式，通过5G网络（无线网+核心网）和IMS系统承载语音业务，该种方式称为VoNR（Voice over NR）。 
AMF决策UE是否具有IMS over PS能力时参考如下因素： 
 
服务PLMN的VoNR能力（本局VoNR开关） 
 
归属PLMN的VoNR能力（IMSI号段） 
 
TA 
 
UE语音能力 
 
语音连续性能力 
 
功能说明 
VoNR配置提供AMF支持VoNR和基于SUPI号段/TA/DNN的语音策略配置。 
子主题： 
### AMF支持VoNR配置 
### AMF支持VoNR配置 
背景知识 
VoNR（Voice over New Radio）即为NR承载语音，是指在5G网络中进行IMS语音。参见3PGG TS 23501 第“5.16.3 IMS support”章节。 
在VoNR特性中，AMF的主要作用包括： 
 
根据UE的UE语音能力(UE's usage setting和voice preferred)、无线覆盖（TA）、漫游协议（IMSI号段），以及用户签约的DNN是否支持语音业务，确定IMS语音能力。 
 
用户注册区域的分配考虑IMS语音能力。 
 
把IMS语音同向性信息指示给UDM，UDM用于后续T-ADS查询。 
 
功能说明 
本功能用于设置AMF是否支持VoNR功能、及其是否支持UE无线能力检查功能。当需要开启VoNR功能时，需要使用此配置，开启VoNR功能开关。当需求根据UE无线能力识别的IMS语音连续性能力时，需要使用此配置设置“支持无线能力检查”功能。 
开启VoNR功能时，首先要确保license中支持VoNR。 
子主题： 
#### 修改 AMF支持VONR配置(SET 5GVONRCFG) 
#### 修改 AMF支持VONR配置(SET 5GVONRCFG) 
功能说明 
本命令用于设置AMF是否支持VoNR功能、及其AMF是否支持UE无线能力检查功能。 
开启VoNR功能后，AMF会根据UE语音能力(UE's usage setting和voice preferred)、无线覆盖（TA）、漫游协议（IMSI号段），确定IMS语音能力，并指示给终端用户。 
当开启“支持无线能力检查”之后，在终端用户Registration过程中，AMF会和NR之间进行UE无线能力检查过程（UE RADIO CAPABILITY CHECK），并将NR返回的结果作为该终端是否支持IMS语音能力的一个考虑因素。 
注意事项 
 
该命令执行后，配置立即生效。 
 
使用本命令开启VoNR功能前，需要确认License项：uMAC_AMF_7209    AMF Support VoNR Function"已激活，否则VoNR功能无法生效。 
 
使用本命令开启“无线能力检查” 之前，需要先通过SHOW UE RADIOCAPABILITY命令确认NR是否支持UE无线能力检查过程（通过SHOW UE RADIOCAPABILITY命令查询）。 
 
该命令最多可以配置1条记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
IMSVoPS|IMSVoPs|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否开启VoNR功能，取值及含义如下：不支持IMS VoPS业务支持IMS VoPS业务修改影响：修改此参数，影响AMF是否支持VoNR功能。数据来源：本端规划。默认值：不支持IMS VoPS业务。配置原则：无。
UERADIOCAPCHECK|UE无线能力检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于设置AMF是否开启检查UE无线能力功能，取值及含义如下：不检查UE无线能力检查UE无线能力修改影响：修改此参数，影响AMF是否支持"UE无线能力检查"功能。数据来源：本端规划。默认值：不检查UE无线能力。配置原则：无。
命令举例 
`
设置AMF支持VoNR能力，但不支持UE无线能力检查。
SET 5GVONRCFG:IMSVOPS="SPRT",UERADIOCAPCHECK="NO"
` 
#### 查询 AMF支持VONR配置(SHOW 5GVONRCFG) 
#### 查询 AMF支持VONR配置(SHOW 5GVONRCFG) 
功能说明 
本命令用于查看AMF是否支持VoNR功能。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSVoPS|IMSVoPs|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否开启VoNR功能，取值及含义如下：不支持IMS VoPS业务支持IMS VoPS业务
UERADIOCAPCHECK|UE无线能力检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于设置AMF是否开启检查UE无线能力功能，取值及含义如下：不检查UE无线能力检查UE无线能力
命令举例 
`
查询VoNR功能和UE无线能力检查功能是否开启。 
SHOW 5GVONRCFG:
(No.2) : SHOW 5GVONRCFG:
-----------------Namf_Communication_0----------------
IMSVoPs                        UE无线能力检查
不支持IMS VoPS业务             不检查UE无线能力
记录数：1
` 
### 基于SUPI号段语音策略配置 
### 基于SUPI号段语音策略配置 
背景知识 
在5G网络的终端注册过程中，AMF需要向终端发送一个”IMS over PS是否支持”的指示消息，终端将该指示作为后续选择语音支持能力的一个考量项。 
5G网络对IMS支持能力的判断通过5GC的语音能力、IMSI、TA、UE语音能力（USAGESET）、语音连续性能力，以及终端用户签约的DNN是否支持语音业务，确定终端是否支持IMS及支持哪种Access Type。 
5G网络中定义的DNN就是4G网络中定义的APN。 
功能说明 
本功能用于设置缺省SUPI（Subscriber Permanent Identifier，用户永久标识）语音参数策略配置是否开启IMS VoPS业务。 
子主题： 
#### 修改缺省语音参数策略配置(SET 5GDEFAULTSUPIVOICEPOLICY) 
#### 修改缺省语音参数策略配置(SET 5GDEFAULTSUPIVOICEPOLICY) 
功能说明 
该命令用于设置或修改是否开启缺省SUPI语音参数策略IMS VoPS业务。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
IMSVoPS|IMSVoPs|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|该参数用于设置缺省SUPI语音参数策略是否支持IMS VoPS业务。
命令举例 
`
设置缺省SUPI语音参数策略IMS VoPS业务为开启。 
SET 5GDEFAULTSUPIVOICEPOLICY:IMSVOPS="SPRT"
` 
#### 查询缺省语音参数策略配置(SHOW 5GDEFAULTSUPIVOICEPOLICY) 
#### 查询缺省语音参数策略配置(SHOW 5GDEFAULTSUPIVOICEPOLICY) 
功能说明 
该命令用于查询是否开启缺省SUPI语音参数策略IMS VoPS业务。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSVoPS|IMSVoPs|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|该参数用于设置缺省SUPI语音参数策略是否支持IMS VoPS业务。
命令举例 
`
查询缺省SUPI语音参数策略IMS VoPS业务是否开启。 
SHOW 5GDEFAULTSUPIVOICEPOLICY:
(No.5) : SHOW 5GDEFAULTSUPIVOICEPOLICY:
-----------------Namf_Communication_0----------------
User Alias
not support IMS VoPS
记录数：1
执行成功耗时: 0.549 秒
` 
#### 新增基于SUPI的语音参数策略配置(ADD 5GSUPIVOICEPOLICY) 
#### 新增基于SUPI的语音参数策略配置(ADD 5GSUPIVOICEPOLICY) 
功能说明 
本命令用于配置AMF根据终端用户的SUPI（Subscriber Permanent Identifier，用户永久标识）号段和无线侧的接入方式，来设置是否支持 IMS over PS。 
配置成功之后，终端用户在接入5GC网络时，AMF根据本命令配置的结果，决策指示该终端用户是否使用IMS over PS功能。 
注意事项 
在配置此命令之前，需要先通过[SET 5GVONRCFG]命令配置AMF支持VoNR功能，命令格式为：SET 5GVONRCFG:IMSVOPS="SPRT"
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|本参数用于配置终端用户的SUPI号段。
AccessType|接入类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: _3GPP|本参数用于设置终端接入5GC网络的方式，包括3GPP接入或Non-3GPP接入。
IMSVoPS|IMSVoPs|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|本参数用于设置终端是否支持IMS over PS。
命令举例 
`
新增配置，"4600100001"号段的用户在3GPP继续模式下，支持IMS VoPS。
ADD 5GSUPIVOICEPOLICY:SUPI="4600100001",ACCESSTYPE="_3GPP",IMSVOPS="SPRT"
` 
#### 修改基于SUPI的语音参数策略配置(MOD 5GSUPIVOICEPOLICY) 
#### 修改基于SUPI的语音参数策略配置(MOD 5GSUPIVOICEPOLICY) 
功能说明 
该命令用于修改AMF根据终端用户的SUPI（Subscriber Permanent Identifier，用户永久标识）号段和无线侧的接入方式，来设置是否支持 IMS over PS。当某号段用户的语音策略发生变化时，使用此命令修改。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|本参数用于配置终端用户的SUPI号段。
AccessType|接入类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: _3GPP|本参数用于设置终端接入5GC网络的方式，包括3GPP接入或Non-3GPP接入。
IMSVoPS|IMSVoPs|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|本参数用于设置终端是否支持IMS over PS。
命令举例 
`
修改配置，"4600100001"号段的用户在3GPP继续模式下，不支持IMS VoPS。
MOD 5GSUPIVOICEPOLICY:SUPI="4600100001",ACCESSTYPE="_3GPP",IMSVOPS="NOSPRT"
` 
#### 删除基于SUPI的语音参数策略配置(DEL 5GSUPIVOICEPOLICY) 
#### 删除基于SUPI的语音参数策略配置(DEL 5GSUPIVOICEPOLICY) 
功能说明 
该命令用于删除AMF根据终端用户的SUPI（Subscriber Permanent Identifier，用户永久标识）号段和无线侧的接入方式，来设置是否支持 IMS over PS。。 当配置错误，或对应号段不需要使用此配置时，使用此命令删除。 
注意事项 
删除之后，对应号段的语音策略依赖默认配置。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-16|本参数用于配置终端用户的SUPI号段。
命令举例 
`
删除"4600100001"号段的语音配置。
DEL 5GSUPIVOICEPOLICY:SUPI="4600100001"
` 
#### 查询基于SUPI的语音参数策略配置(SHOW 5GSUPIVOICEPOLICY) 
#### 查询基于SUPI的语音参数策略配置(SHOW 5GSUPIVOICEPOLICY) 
功能说明 
该命令用于查询AMF根据终端用户的SUPI（Subscriber Permanent Identifier，用户永久标识）号段和无线侧的接入方式，来设置是否支持 IMS over PS。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|本参数用于配置终端用户的SUPI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-16|本参数用于配置终端用户的SUPI号段。
AccessType|接入类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: _3GPP|本参数用于设置终端接入5GC网络的方式，包括3GPP接入或Non-3GPP接入。
IMSVoPS|IMSVoPs|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|本参数用于设置终端是否支持IMS over PS。
命令举例 
`
查询已经配置的TA语音模板。 
SHOW 5GDEFAULTSUPIVOICEPOLICY
(No.1) : SHOW 5GDEFAULTSUPIVOICEPOLICY:
-----------------Namf_Communication_0----------------
IMSVoPs
不支持IMS VoPS业务
记录数：1
` 
### 基于TA语音策略配置 
### 基于TA语音策略配置 
背景知识 
在5G网络的终端注册过程中，AMF需要向终端发送一个”IMS over PS是否支持”的指示消息，终端将该指示作为后续选择语音支持能力的一个考量项。 
5G网络对IMS支持能力的判断通过5GC的语音能力、IMSI、TA、UE语音能力（USAGESET）、语音连续性能力，以及终端用户签约的DNN是否支持语音业务，确定终端是否支持IMS及支持哪种Access Type。 
5G NR语音方案设计，延续了4G LTE通过IP网络承载语音业务的方式，通过5G网络（无线网+核心网）和IMS系统承载语音业务，该种方式称为VoNR（Voice over NR）。同样地，考虑到5G不同阶段部署规模不同，而4G网络已经广泛部署并可能在未来长期存在，以及对语音业务连续性保证的需求，回落方案设计也是十分必要的，因此演进的分组系统回落（EPS Fallback）方案也是5G语音方案的一种。这里EPS Fallback主要指回落到4G网络通过VoLTE的方式实现语音业务。 
功能说明 
本功能用于设置缺省TA语音参数策略配置，包括是否开启IMS VoPS业务和是否开启Fall Back业务。 
子主题： 
#### 修改缺省语音参数策略配置(SET 5GDEFAULTTAVOICEPOLICY) 
#### 修改缺省语音参数策略配置(SET 5GDEFAULTTAVOICEPOLICY) 
功能说明 
该命令用于设置缺省TA语音参数策略，包括用户别名，是否支持IMS VoPS业务、EPS FallBack业务，以及下发IMS指示时是否参考终端S1能力。  
当开启VoNR功能时，需要使用此命令设置缺省TA语音参数策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
IMSVoPS|IMSVoPs|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置缺省TA语音参数策略是否支持IMS VoPS业务。修改影响：开启之后，表明基于缺省TA语音参数策略的AMF支持IMS VoPS业务；否则，表明基于缺省TA语音参数策略的AMF不支持IMS VoPS业务。数据来源：本端规划。默认值：不支持IMS VoPS业务。配置原则：无。
FallBack|EPS FallBack|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置缺省TA语音参数策略是否支持EPS FallBack业务。修改影响：开启之后，表明基于缺省TA语音参数策略的AMF支持EPS FallBack业务；否则，表明基于缺省TA语音参数策略的AMF不支持EPS FallBack业务。数据来源：本端规划。默认值：不支持EPS FallBack业务。配置原则：无。
UserAlias|用户别名|参数可选性: 任选参数类型: 字符串参数范围: 0-13默认值: NULL|参数作用：该参数用于设置缺省TA语音参数策略的用户别名。修改影响：修改后，该参数设置缺省TA语音参数策略的用户别名。数据来源：本端规划。默认值：NULL。配置原则：无。
considerS1CapForIms|参考终端S1能力下发IMS指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持下发IMS指示时参考终端S1模式能力。修改影响：开启之后，表明基于缺省TA语音参数策略的AMF支持下发IMS指示时参考终端S1模式能力；否则，表明基于缺省TA语音参数策略的AMF支持下发IMS指示时不参考终端S1模式能力。数据来源：本端规划。默认值：不支持。配置原则：无。
命令举例 
`
设置缺省TA语音参数策略IMS VoPS业务为开启，EPS FallBack业务为开启，用户别名为111，支持参考终端S1能力下发IMS指示。 
SET 5GDEFAULTTAVOICEPOLICY:IMSVOPS="SPRT",FALLBACK="SPRT",USERALIAS="111",CONSIDERS1CAPFORIMS="SPRT"
` 
#### 查询缺省语音参数策略配置(SHOW 5GDEFAULTTAVOICEPOLICY) 
#### 查询缺省语音参数策略配置(SHOW 5GDEFAULTTAVOICEPOLICY) 
功能说明 
该命令用于查询缺省TA语音参数策略配置。  
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
IMSVoPS|IMSVoPs|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|该参数用于显示缺省TA语音参数策略是否支持IMS VoPS业务。
FallBack|EPS FallBack|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于显示缺省TA语音参数策略是否支持EPS FallBack业务。
UserAlias|用户别名|参数可选性: 任选参数类型: 字符串参数范围: 0-13默认值: NULL|该参数用于显示缺省TA语音参数策略的用户别名。
considerS1CapForIms|参考终端S1能力下发IMS指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于显示AMF是否支持下发IMS指示时参考终端S1模式能力。
命令举例 
`
查询缺省TA语音参数策略IMS VoPS业务是否开启，EPS FallBack业务是否开启，参考终端S1能力下发IMS指示是否开启。 
SHOW 5GDEFAULTTAVOICEPOLICY: 
(No.7) : SHOW 5GDEFAULTTAVOICEPOLICY:
-----------------Namf_Communication_0----------------
操作维护       IMSVoPs            EPS FallBack           用户别名 参考终端S1能力下发IMS指示       
--------------------------------------------------------------------------------------------------
修改           不支持IMS VoPS业务 不支持EPS FallBack业务 NULL     支持 
--------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-06-21 16:18:03 耗时: 0.194 秒
` 
#### 新增基于TA的语音参数策略模板配置(ADD 5GTAVOICEPOLICYTEMPLATE) 
#### 新增基于TA的语音参数策略模板配置(ADD 5GTAVOICEPOLICYTEMPLATE) 
功能说明 
该命令用于新增TA语音策略模板。 
当开启VoNR功能时，需要使用此命令增加语音策略模板。配置成功之后，这些语音策略模板可以被相应的TA关联引用。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
policyTempId|策略模板标识|参数可选性: 必选参数类型: 数字参数范围: 1-255|参数作用：该参数用于设置TA语音策略模板ID，该参数的取值 是通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取的。修改影响：修改后，该参数设置TA语音策略模板ID。数据来源：通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取。默认值：无。配置原则：无。
IMSVoPS|IMSVoPs|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置TA语音参数策略是否支持IMS VoPS业务。修改影响：开启之后，表明基于TA语音参数策略的AMF支持IMS VoPS业务；否则，表明基于TA语音参数策略的AMF不支持IMS VoPS业务。数据来源：本端规划。默认值：不支持IMS VoPS业务。配置原则：无。
FallBack|EPS FallBack|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置TA语音参数策略是否支持EPS FallBack业务。修改影响：开启之后，表明基于TA语音参数策略的AMF支持EPS FallBack业务；否则，表明基于TA语音参数策略的AMF不支持EPS FallBack业务。数据来源：本端规划。默认值：不支持EPS FallBack业务。配置原则：无。
UserAlias|用户别名|参数可选性: 任选参数类型: 字符串参数范围: 0-13|参数作用：该参数用于设置TA语音参数策略的用户别名。修改影响：修改后，该参数设置TA语音参数策略的用户别名。数据来源：本端规划。默认值：无。配置原则：无。
considerS1CapForIms|参考终端S1能力下发IMS指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持下发IMS指示时参考终端S1模式能力。修改影响：开启之后，表明基于TA语音参数策略的AMF支持下发IMS指示时参考终端S1模式能力；否则，表明基于TA语音参数策略的AMF支持下发IMS指示时不参考终端S1模式能力。数据来源：本端规划。默认值：不支持。配置原则：无。
命令举例 
`
新增TA语音策略模板1，支持IMS VoPS，不支持EPS Fallback，模板名字为"ta-vocie-temp-1"，支持参考终端S1能力下发IMS指示。
ADD 5GTAVOICEPOLICYTEMPLATE:POLICYTEMPID=1,IMSVOPS="SPRT",FALLBACK="NOSPRT",USERALIAS="ta-voice-1",CONSIDERS1CAPFORIMS="SPRT"
` 
#### 修改基于TA的语音参数策略模板配置(MOD 5GTAVOICEPOLICYTEMPLATE) 
#### 修改基于TA的语音参数策略模板配置(MOD 5GTAVOICEPOLICYTEMPLATE) 
功能说明 
该命令用于修改TA语音策略模板信息，包括是否支持IMS over PS，是否支持EPS Fallback，是否支持参考终端S1能力下发IMS指示。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
policyTempId|策略模板标识|参数可选性: 必选参数类型: 数字参数范围: 1-255|参数作用：该参数用于设置TA语音策略模板ID，该参数的取值 是通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取的。修改影响：修改后，该参数设置TA语音策略模板ID。数据来源：通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取。默认值：无。配置原则：无。
IMSVoPS|IMSVoPs|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置TA语音参数策略是否支持IMS VoPS业务。修改影响：开启之后，表明基于TA语音参数策略的AMF支持IMS VoPS业务；否则，表明基于TA语音参数策略的AMF不支持IMS VoPS业务。数据来源：本端规划。默认值：不支持IMS VoPS业务。配置原则：无。
FallBack|EPS FallBack|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置TA语音参数策略是否支持EPS FallBack业务。修改影响：开启之后，表明基于TA语音参数策略的AMF支持EPS FallBack业务；否则，表明基于TA语音参数策略的AMF不支持EPS FallBack业务。数据来源：本端规划。默认值：不支持EPS FallBack业务。配置原则：无。
UserAlias|用户别名|参数可选性: 任选参数类型: 字符串参数范围: 0-13|参数作用：该参数用于设置TA语音参数策略的用户别名。修改影响：修改后，该参数设置TA语音参数策略的用户别名。数据来源：本端规划。默认值：无。配置原则：无。
considerS1CapForIms|参考终端S1能力下发IMS指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持下发IMS指示时参考终端S1模式能力。修改影响：开启之后，表明基于TA语音参数策略的AMF支持下发IMS指示时参考终端S1模式能力；否则，表明基于TA语音参数策略的AMF支持下发IMS指示时不参考终端S1模式能力。数据来源：本端规划。默认值：不支持。配置原则：无。
命令举例 
`
修改TA语音策略模板1，支持IMS VoPS，不支持EPS Fallback，模板名字为"ta-voice-2"，不支持参考终端S1能力下发IMS指示
MOD 5GTAVOICEPOLICYTEMPLATE:POLICYTEMPID=1,IMSVOPS="SPRT",FALLBACK="NOSPRT",USERALIAS="ta-voice-2",CONSIDERS1CAPFORIMS="NOSPRT"
` 
#### 删除基于TA的语音参数策略模板配置(DEL 5GTAVOICEPOLICYTEMPLATE) 
#### 删除基于TA的语音参数策略模板配置(DEL 5GTAVOICEPOLICYTEMPLATE) 
功能说明 
该命令用于删除TA语音策略模板。当某个模板不再使用的时候，可使用此命令删除。 
注意事项 
删除之前需要确保被删除的语音模板没有被某些TA引用。其中的"TA语音策略模板ID"是通过[ADD 5GTAVOICEPOLICYTEMPLATE]命令配置的。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
policyTempId|策略模板标识|参数可选性: 必选参数类型: 数字参数范围: 1-255|参数作用：该参数用于设置TA语音策略模板ID，该参数的取值 是通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取的。修改影响：修改后，该参数设置TA语音策略模板ID。数据来源：通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取。默认值：无。配置原则：无。
命令举例 
`
删除TA语音模板1。
DEL 5GTAVOICEPOLICYTEMPLATE:POLICYTEMPID=1
` 
#### 查询基于TA的语音参数策略模板配置(SHOW 5GTAVOICEPOLICYTEMPLATE) 
#### 查询基于TA的语音参数策略模板配置(SHOW 5GTAVOICEPOLICYTEMPLATE) 
功能说明 
该命令用于查询已经配置的TA语音策略模板。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
policyTempId|策略模板标识|参数可选性: 任选参数类型: 数字参数范围: 1-255|参数作用：该参数用于设置TA语音策略模板ID，该参数的取值 是通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取的。修改影响：修改后，该参数设置TA语音策略模板ID。数据来源：通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
policyTempId|策略模板标识|参数可选性: 任选参数类型: 数字参数范围: 1-255|该参数用于显示TA语音策略模板ID，该参数的取值是通过SHOW 5GTAVOICEPOLICYTEMPLATE命令查询获取的。
IMSVoPS|IMSVoPs|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于显示TA语音参数策略是否支持IMS VoPS业务。
FallBack|EPS FallBack|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于显示TA语音参数策略是否支持EPS FallBack业务。
UserAlias|用户别名|参数可选性: 任选参数类型: 字符串参数范围: 0-13|该参数用于显示TA语音参数策略的用户别名。
considerS1CapForIms|参考终端S1能力下发IMS指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|该参数用于显示AMF是否支持下发IMS指示时参考终端S1模式能力。
命令举例 
`
查询已经配置的TA语音模板。 
SHOW 5GTAVOICEPOLICYTEMPLATE:
(No.12) : SHOW 5GTAVOICEPOLICYTEMPLATE:
-----------------Namf_Communication_0_A----------------
操作维护       策略模板标识 IMSVoPs          EPS FallBack           用户别名       参考终端S1能力下发IMS指示
-----------------------------------------------------------------------------------------------------------------
复制  删除      1            支持IMS VoPS业务 不支持EPS FallBack业务 ta-voice-1    支持
-----------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-09-27 23:40:03 耗时: 0.129 秒
` 
### 基于DNN语音策略配置 
### 基于DNN语音策略配置 
背景知识 
一般运营商规划的语音的DNN和数据的DNN不同，语音的DNN依赖于运营商的本地配置。 
功能说明 
基于DNN语音策略配置提供基于DNN语音控制和支持语音的DNN配置。 
子主题： 
#### 基于DNN语音控制 
#### 基于DNN语音控制 
背景知识 
在5G注册过程中，AMF需要向UE发送一个”IMS over PS是否支持”的指示，UE将该指示作为后续语音域选择的一个考量项。 
5GC对IMS支持能力的判断通过5GC的语音能力、IMSI、TA、UE语音能力（USAGESET）、语音连续性能力，以及用户签约的DNN是否支持语音业务，确定UE是否支持IMS及哪种Access Type支持。 
功能说明 
本命令用于设置开启支持基于DNN的语音策略开关。 
如果本局支持VONR功能，开启支持基于DNN的语音策略开关后，会判断本局支持语音策略的DNN列表中的DNN能否能匹配上用户签约的DNN，能匹配上则表示该用户支持语音业务，否则不支持 
如果本局支持VONR功能，关闭支持基于DNN的语音策略开关，则默认用户签约的DNN都支持语音业务。 
在配置此命令之前，需要先开启AMF支持VONR功能。 
子主题： 
##### 修改AMF支持基于DNN语音策略配置(SET 5GDNNVOICESWITCH) 
##### 修改AMF支持基于DNN语音策略配置(SET 5GDNNVOICESWITCH) 
功能说明 
本命令用于设置AMF是否支持根据终端用户接入的DNN，来开启VoNR功能。 
5G网络中定义的DNN就是4G网络中定义的APN。 
如果本AMF支持VoNR功能，通过本命令设置AMF支持基于DNN的语音策略后，AMF会判断通过[ADD 5GDNNVOICEPOLICY]命令配置的DNN列表中的DNN能否能匹配上终端用户签约的DNN，如果可以匹配上，则表示该终端用户支持VoNR业务，否则该终端用户不能在5GC网络进行VoNR业务。
如果本AMF支持VoNR功能，通过本命令设置AMF不支持基于DNN的语音策略后，则默认用户签约的DNN都支持VoNR。/p> 
注意事项 
在配置此命令之前，需要先通过[SET 5GVONRCFG]命令配置AMF支持VoNR功能，命令格式为：SET 5GVONRCFG:IMSVOPS="SPRT"
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SuptDnnVoicePolicy|支持DNN语音策略开关|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|本命令用于设置AMF是否支持根据终端用户接入的DNN，来开启VoNR功能。
命令举例 
`
设置开启支持基于DNN的语音策略开关。 
SET 5GDNNVOICESWITCH:SUPTDNNVOICEPOLICY="SPRT"
` 
##### 查询AMF支持基于DNN语音策略配置(SHOW 5GDNNVOICESWITCH) 
##### 查询AMF支持基于DNN语音策略配置(SHOW 5GDNNVOICESWITCH) 
功能说明 
本命令用于查询AMF是否支持根据终端用户接入的DNN，来开启VoNR功能。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SuptDnnVoicePolicy|支持DNN语音策略开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|本命令用于设置AMF是否支持根据终端用户接入的DNN，来开启VoNR功能。
命令举例 
`
查询AMF支持基于DNN语音策略配置。 
SHOW 5GDNNVOICESWITCH
(No.1) : SHOW 5GDNNVOICESWITCH:
-----------------Namf_Communication_0----------------
支持DNN语音策略开关
支持DNN语音策略
记录数：1
执行成功耗时: 1.612 秒
` 
#### 支持语音的DNN配置 
#### 支持语音的DNN配置 
背景知识 
5GC SA架构下，有三种语音解决方案： 
 
VoNR：语音呼叫通过NR接入5GC网络，在5GC网络中进行IMS语音。 
 
EPS fallback：语音呼叫时回落到4G EPS网络，在EPS网络中进行IMS语音或进一步回落到2/3G进行CS语音。 
 
RAT fallback：语音呼叫时回落到4G eLTE基站但还是接入5GC网络，在5GC网络中进行IMS语音。 
 
功能说明 
该命令用于新增支持语音策略的DNN（Data Network Name，数据网络名称）配置。当开启VoNR功能时，需要在AMF中添加此配置。 
配置成功后，如果配置的DNN能匹配上用户签约的DNN，则表示该用户支持语音业务。 
如果配置的DNN匹配不上用户签约的DN，则表示该用户不支持语音业务。 
在配置此命令之前，需要先执行[SET 5GVONRCFG]命令开启AMF支持VONR功能，再执行[SET 5GDNNVOICESWITCH]命令打开AMF支持DNN语音策略开关。
子主题： 
##### 新增支持语音策略的DNN配置(ADD 5GDNNVOICEPOLICY) 
##### 新增支持语音策略的DNN配置(ADD 5GDNNVOICEPOLICY) 
功能说明 
该命令用于新增支持语音策略的DNN（Data Network Name，数据网络名称）配置。当开启VoNR（Voice over New Radio，新空口承载语音）功能时，需要在AMF中添加此配置。 
配置成功后，如果配置的DNN能匹配上用户签约的DNN，则表示该用户支持语音业务。 
如果配置的DNN匹配不上用户签约的DNN，则表示该用户不支持语音业务。 
注意事项 
一个AMF最多只能配置255个DNN语音配置列表。 
在配置此命令之前，需要先执行[SET 5GVONRCFG]命令开启AMF支持VONR功能，再执行[SET 5GDNNVOICESWITCH]命令打开AMF支持DNN语音策略开关。
仅需配置DNN网络ID部分，不要配置运营商ID。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|该参数用于配置DNN（Data Network Name，数据网络名称）。5G网络中定义的DNN（Data Network Name，数据网络名称）。就是4G网络中定义的APN，这两个标识符具有相同的含义并携带相同的信息（参见3GPP TS23.003 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。在PDU会话建立流程中，需要用到DNN参数选择SMF，如果请求消息中携带的DNN不合法，本地可以更正，影响SMF选择。DNN只支持输入小写。
命令举例 
`
新增支持语音策略的DNN配置，DNN为zte.com.cn。
ADD 5GDNNVOICEPOLICY:DNN="zte.com.cn"
` 
##### 删除支持语音策略的DNN配置(DEL 5GDNNVOICEPOLICY) 
##### 删除支持语音策略的DNN配置(DEL 5GDNNVOICEPOLICY) 
功能说明 
该命令用于删除支持语音策略的DNN配置。 
当网络规划发生变更，某个DNN不再支持语音业务，可以使用此命令删除指定的DNN。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
DNN|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|该参数用于配置DNN（Data Network Name，数据网络名称）。5G网络中定义的DNN（Data Network Name，数据网络名称）。就是4G网络中定义的APN，这两个标识符具有相同的含义并携带相同的信息（参见3GPP TS23.003 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。在PDU会话建立流程中，需要用到DNN参数选择SMF，如果请求消息中携带的DNN不合法，本地可以更正，影响SMF选择。DNN只支持输入小写。
命令举例 
`
删除支持语音策略的DNN配置。
DEL 5GDNNVOICEPOLICY:DNN="zte.com.cn"
` 
##### 查询支持语音策略的DNN配置(SHOW 5GDNNVOICEPOLICY) 
##### 查询支持语音策略的DNN配置(SHOW 5GDNNVOICEPOLICY) 
功能说明 
该命令用于查询本AMF所支持的DNN语音配置列表信息，或查询某个指定DNN信息。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置DNN（Data Network Name，数据网络名称）。5G网络中定义的DNN（Data Network Name，数据网络名称）。就是4G网络中定义的APN，这两个标识符具有相同的含义并携带相同的信息（参见3GPP TS23.003 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。在PDU会话建立流程中，需要用到DNN参数选择SMF，如果请求消息中携带的DNN不合法，本地可以更正，影响SMF选择。DNN只支持输入小写。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
DNN|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置DNN（Data Network Name，数据网络名称）。5G网络中定义的DNN（Data Network Name，数据网络名称）。就是4G网络中定义的APN，这两个标识符具有相同的含义并携带相同的信息（参见3GPP TS23.003 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。在PDU会话建立流程中，需要用到DNN参数选择SMF，如果请求消息中携带的DNN不合法，本地可以更正，影响SMF选择。DNN只支持输入小写。
命令举例 
`
查询已经配置的支持语音策略的DNN配置列表。 
SHOW 5GDNNVOICEPOLICY"
(No.3) : SHOW 5GDNNVOICEPOLICY:
-----------------Namf_Communication_0----------------
DNN
1
记录数：1
执行成功耗时: 0.26 秒
` 
## 紧急业务配置 
## 紧急业务配置 
背景知识 
在5GC网络中，运营商通过IMS为用户提供语音业务，也提供紧急呼叫业务，5GC与IMS网络建立紧急会话来给用户提供紧急呼叫业务。 
根据用户合法性分，AMF支持紧急的呼叫有： 
 
仅完全合法有效用户可以紧急呼叫。 
 
仅鉴权合法用户（可能位置被限制）可以紧急呼叫。 
 
具有SUPI的用户（可能鉴权失败、位置被限制）可以紧急呼叫。 
 
任意用户（可能不具有SUPI、鉴权失败、位置被限制）可以紧急呼叫。 
 
功能说明 
紧急呼叫配置提供紧急业务策略、紧急数据、紧急号码、紧急业务回落和紧急业务SNSSAI配置。 
子主题： 
### 紧急业务策略配置 
### 紧急业务策略配置 
背景知识 
普通电信业务必须获得网络授权认证后，方可成功接入网络。但紧急业务关系到社会、个人的安全保障，是电信企业承担社会责任的重要体现。在某些特殊场景下，比如无卡终端用户、终端用户欠费、终端用户进入受限区域、终端终端非法等等，必须能够保证终端用户仍旧可以发起紧急业务。 
AMF为了满足运营商对于紧急业务的灵活配置要求，需要提供一些灵活策略配置，比如是否支持紧急业务、是否支持无卡用户紧急业务、紧急业务是否鉴权、紧急业务鉴权失败是否放行、紧急业务受限用户是否放行等，以便运营商根据网络和用户的实际情况，选择对应的配置，以便达到企业效益与社会责任的平衡。 
功能说明 
该功能用于灵活配置紧急业务策略，比如是否支持紧急业务、是否支持无卡用户紧急业务、是否支持受限用户紧急业务等。运营商应该根据自身网络和用户实际情况，选择对应的策略配置。 
AMF当前支持如下功能配置： 
 
支持紧急业务：用于控制AMF是否开启紧急业务，默认支持。 
 
支持无卡用户紧急业务：用于控制AMF是否允许无卡终端用户触发紧急业务，默认支持。 
 
紧急注册鉴权：用于控制用户紧急注册时，AMF是否需要启动鉴权，默认需要。 
 
鉴权失败放行紧急业务：用于控制当用户鉴权失败时，若该用户已经激活紧急业务，则AMF是否允许该用户继续紧急业务，默认允许。 
 
受限用户放行紧急业务：用于控制当用户处于受限状态，比如进入受限区域，AMF是否允许用户继续紧急业务，默认允许。 
 
紧急注册检查PEI：用于控制用户紧急注册时，AMF是否需要启动PEI检查，默认不启动。 
 
PEI检查失败放行紧急业务：用于控制当PEI检查失败时，若该用户已经激活紧急业务，AMF是否允许该用户继续紧急业务, 默认不允许。 
 
向UE获取IMEI(SV)失败限制接入时放行紧急业务：用于控制当AMF向UE获取IMEI(SV)失败时，如果系统"向UE获取IMEI(SV)失败时AMF是否限制接入"配置为限制接入并且当前是紧急业务，是否针对紧急业务进行额外放行, 默认不放行。 
 
上报PEI构造的SUPI：用于控制无卡用户使用PEI进行紧急注册时，AMF使用用户的PEI构造了SUPI，在进行信令跟踪和失败观察业务时，是否上报此构造的SUPI，默认上报。 
 
默认紧急业务能力：用于控制本AMF下支持紧急业务的无线接入类型，包括四种策略选择：NR和E-UTRAN均不支持、仅NR支持、仅E-UTRAN支持以及NR和E-UTRAN均支持，默认NR和E-UTRAN均支持。 
 
AMF在终端用户触发注册流程时，通过注册接受消息携带给UE。 
 
缺省是否支持EMC：在“基于号段的紧急业务策略配置”中没有匹配到号段时，使用该参数控制是否支持EMC。 
 
缺省是否支持EMF：在“基于号段的紧急业务策略配置”中没有匹配到号段时，使用该参数控制是否支持EMF。 
 
缺省是否携带紧急号码列表：在“基于号段的紧急业务策略配置”中没有匹配到号段时，使用该参数标识是否携带紧急号码列表给UE。 
 
缺省是否携带扩展紧急号码列表：在“基于号段的紧急业务策略配置”中没有匹配到号段时，使用该参数标识是否携带扩展紧急号码列表给UE。 
 
缺省紧急号码列表ID：在“基于号段的紧急业务策略配置”中没有匹配到号段时，使用该参数控制下发给UE的紧急号码列表ID。 
 
设置为0表示无效，表示使用服务TA上配置的扩展紧急号码列表ID。 
 
设置为非0表示有效，表示使用本处配置的紧急号码列表ID。 
 
缺省扩展紧急号码列表ID： 
 
设置为0表示无效，表示使用服务TA上配置的扩展紧急号码列表ID。 
 
设置为非0表示有效，表示使用本处配置的扩展紧急号码列表ID。 
 
AMF仅在支持紧急呼叫时下发紧急号码：用于控制是否仅在支持紧急呼叫时下发紧急号码给UE，包括以下三种策略方式： 
 
0：仅AMF指示UE支持紧急业务（EMC）或者紧急业务回落（EMF）时下发紧急号码。 
 
1：仅AMF开启支持紧急业务或者紧急业务回落时下发紧急号码。 
 
2：总是下发紧急号码。 
 
子主题： 
#### 设置紧急业务策略(SET EMERGSRVPLY) 
#### 设置紧急业务策略(SET EMERGSRVPLY) 
功能说明 
本命令用于配置紧急业务策略，比如是否支持紧急业务、是否支持无卡用户紧急业务、紧急业务是否鉴权、紧急业务鉴权失败是否放行、紧急业务受限用户是否放行等。 
注意事项 
 
该命令执行后，配置立即生效。 
 
系统的业务数据完成后，本命令已经存在初始配置值，如果运营商没有特殊需求，无需修改，按初始配置值生效。 
 
该命令最多可以配置1条记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
sprtEmergSrv|支持紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制AMF是否开启紧急业务，取值及含义如下：否：不开启紧急业务启：开启紧急业务是修改影响：修改此参数，影响AMF是否支持紧急业务。数据来源：本端规划。 默认值：否。配置原则：无。
sprtEmergSrvCardless|支持无卡用户紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制AMF是否允许无卡终端用户触发紧急业务，取值及含义如下：否：无卡用户不能发起紧急业务。是：无卡用户可以发起紧急业务。修改影响：修改此参数，影响AMF是否允许无卡终端用户触发紧急业务。数据来源：本端规划。 默认值：否。配置原则：无。
authEmergRegist|紧急注册鉴权|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制用户紧急注册时，AMF是否需要启动鉴权，取值及含义如下：否：AMF不启动鉴权。是：AMF启动鉴权。修改影响：修改此参数，影响紧急注册时AMF是否启动鉴权。数据来源：本端规划。 默认值：否。配置原则：无。
passAuthFail|鉴权失败放行紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制当用户鉴权失败时，若该用户已经激活紧急业务，则AMF是否允许该用户继续紧急业务，取值及含义如下：否：AMF不允许该用户继续紧急业务。是：AMF允许该用户继续紧急业务。修改影响：修改此参数，影响紧急用户鉴权失败时，AMF是否允许用户继续紧急业务。数据来源：本端规划。 默认值：否。配置原则：无。
passLimitedUser|受限用户放行紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制当用户业务受限（受限业务包括：接入限制、移动性限制、会话限制、签约限制）时，若该用户已经激活紧急业务，则AMF是否允许该用户继续紧急业务，取值及含义如下：否：AMF不允许该用户继续紧急业务。是：AMF允许该用户继续紧急业务。修改影响：修改此参数，影响当用户的某些业务受限时，AMF是否允许用户继续紧急业务。数据来源：本端规划。 默认值：否。配置原则：无。
peiCheckEmergRegist|紧急注册检查PEI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制用户紧急注册时，AMF是否需要启动PEI检查，取值及含义如下：否：AMF不启动PEI检查是：AMF启动PEI检查修改影响：修改此参数，影响AMF是否对紧急用户启动PEI检查。数据来源：本端规划。 默认值：否。配置原则：无。
passPeiCheckFail|PEI检查限制接入时放行紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|本参数用于控制当AMF启用PEI检查，导致用户接入限制时，AMF是否允许该用户继续紧急业务，取值及含义如下：否：AMF不允许该用户继续紧急业务。是：AMF允许该用户继续紧急业务。修改影响：修改此参数，影响PEI检查，导致用户接入限制时，AMF是否允许该用户继续紧急业务。数据来源：本端规划。 默认值：否。配置原则：无。
passpeigetfail|向UE获取IMEI(SV)失败限制接入时放行紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：当AMF向用户获取IMEI(SV)失败时，如果SET PEICHECKCONFIG命令中的参数“向UE获取IMEI(SV)失败时AMF是否限制接入（LIMITGETIMEISVFAIL）“配置为限制接入并且当前用户是紧急业务，需要根据本参数的配置值控制AMF是否允许该用户继续紧急业务，取值及含义如下： 否：AMF不允许该用户继续紧急业务。是：AMF允许该用户继续紧急业务。修改影响：影响当AMF向用户获取IMEI(SV)失败时，如果当前用户是紧急业务，AMF是否允许该用户继续紧急业务。 数据来源：本端规划 默认值：否。配置原则：无。
rptSupiConstuByPei|上报PEI构造的SUPI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制无卡用户使用PEI进行紧急业务注册时，AMF使用无卡用户的PEI构造了SUPI，在进行信令跟踪和失败观察业务时，AMF是否上报此构造的SUPI，取值及含义如下：否：AMF不上报构造的SUPI是：AMF上报构造的SUPI修改影响：影响在进行信令跟踪和失败观察业务时，AMF是否上报用PEI构造的SUPI。 数据来源：本端规划 默认值：否。配置原则：无。
emergencyCapa|默认紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: BOTHNRANDEUTRANSPRT|参数作用：本参数用于配置AMF支持紧急业务的默认无线接入类型，取值及含义如下：NR和E-UTRAN均不支持：在本AMF没有配置的TA下，使用NR和E-UTRAN接入方式的用户均不支持紧急业务。仅NR支持：在本AMF没有配置的TA下，使用NR接入方式的用户支持紧急业务。 仅E-UTRAN支持：在本AMF没有配置的TA下，使用E-UTRAN接入方式的用户支持紧急业务。NR和E-UTRAN均支持：在本AMF没有配置的TA下，使用NR和E-UTRAN接入方式的用户均支持紧急业务。修改影响：影响不同无线接入方式的用户是否可以使用紧急业务。 数据来源：本端规划 默认值：NR和E-UTRAN均支持。配置原则：无。
dftemc|缺省是否支持EMC|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，使用该参数控制AMF是否支持EMC（Elastic Management Control，弹性管理控制），取值及含义如下：否：不支持EMC是：支持EMC修改影响：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，修改此参数, 会影响用户是否支持紧急业务的决策结果，最终影响注册接受消息"network feature support"字段中的EMC标记是否携带或携带时的取值。数据来源：本端规划。默认值：是配置原则：在新开局场景，或者对局点执行升级的场景下都要设置为默认值。
dftemf|缺省是否支持EMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，使用该参数控制AMF是否支持EMF（Network Element Mediation Function，网元中介功能），取值及含义如下：否：不支持EMF是：支持EMF修改影响：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，修改此参数, 会影响用户是否支持紧急回落业务的决策结果，最终影响注册接受消息"network feature support"字段中的EMF标记是否携带或携带时的取值。数据来源：本端规划。默认值：是配置原则：升级局和新建局都要设置为默认值。
ifcarryemrnumlist|缺省是否携带紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，使用该参数标识AMF是否携带紧急号码列表给UE，取值及含义如下：否：AMF不携带紧急号码列表给UE。是：AMF携带紧急号码列表给UE。修改影响：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，修改此参数, 会影响用户是否携带紧急号码列表，最终影响注册接受消息的“emergencyNumberList”字段是否携带。数据来源：本端规划。默认值：是配置原则：升级局和新建局都要设置为默认值。
ifcarryextemrnumlist|缺省是否携带扩展紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，使用该参数标识AMF是否携带扩展紧急号码列表给UE，取值及含义如下：否：AMF不携带扩展紧急号码列表给UE是：AMF携带扩展紧急号码列表给UE修改影响：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，修改此参数, 会影响用户是否携带紧急号码列表，最终影响注册接受消息的“extendEmergencyNumberList”字段是否携带。数据来源：本端规划。默认值：是配置原则：在新开局场景，或者对局点执行升级的场景下都要设置为默认值。
emergnumlistid|缺省紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，如果紧急业务策略配置支持携带紧急号码列表，使用该参数控制下AMF发给UE的紧急号码列表ID。设置为0表示无效，表示使用服务TA上配置的紧急号码列表ID。设置为非0表示有效，表示使用本参数配置的紧急号码列表ID。修改影响：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，如果紧急业务策略配置支持携带紧急号码列表，修改此参数，会影响下发给用户的紧急号码列表ID，最终影响注册接受消息的“emergencyNumberList”字段携带的紧急号码列表。数据来源：本端规划。默认值：0。配置原则：本参数的取值引用于ADD 5GEMERNUMLIST命令配置的参数“紧急号码列表ID（LISTID） ”，必须通过ADD 5GEMERNUMLIST命令预先配置。
extemergnumlistid|缺省扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，如果紧急业务策略配置支持携带扩展紧急号码列表，使用该参数控制AMF下发给UE的扩展紧急号码列表ID，取值及含义如下：设置为0表示无效，表示使用服务TA上配置的扩展紧急号码列表ID。设置为非0表示有效，表示使用此处配置的扩展紧急号码列表ID。修改影响：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，如果紧急业务策略配置支持携带扩展紧急号码列表，修改此参数，会影响下发给用户的扩展紧急号码列表ID，最终影响注册接受消息的“extendEmergencyNumberList”字段携带的扩展紧急号码列表。数据来源：本端规划。默认值：0。配置原则：本参数的取值引用于ADD 5GEXTEMERNUMLIST命令配置的参数“紧急号码列表ID（LISTID） ”，必须通过ADD 5GEXTEMERNUMLIST命令预先配置。
sendemgnumsptemgcall|AMF下发紧急号码对支持紧急呼叫的依赖策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: AMFINDICATEUESPTEMCEMF|参数作用：本参数用于控制是否在AMF支持紧急呼叫时才下发紧急号码。下发的紧急号码用于UE识别呼叫是否为紧急呼叫，当AMF不支持紧急呼叫时，UE能够根据拨号识别紧急呼叫，选择其它类型网元（比如CS）发起紧急呼叫。包括以下三种策略方式：0：AMF指示UE支持紧急业务（EMC）或者紧急业务回落（EMF）时下发紧急号码。1：AMF开启支持紧急业务或者紧急业务回落时下发紧急号码。2：总是下发紧急号码。修改影响：无。数据来源：本端规划。默认值：AMF指示UE支持紧急业务（EMC）或者紧急业务回落（EMF）时下发紧急号码。配置原则：无。
命令举例 
`
设置紧急业务策略：支持紧急业务，支持无卡用户紧急业务，紧急注册不需要鉴权，鉴权失败放行紧急业务，受限用户放行紧急业务，上报PEI构造的SUPI，默认紧急业务能力为NR和E-UTRAN均支持，缺省支持EMC，缺省支持EMF，缺省携带紧急号码列表，缺省携带扩展紧急号码列表，缺省紧急号码列表ID为0，缺省扩展紧急号码列表ID为0，AMF下发紧急号码对支持紧急呼叫的依赖策略为AMF指示UE支持紧急业务或紧急业务回落时下发紧急号码
SET EMERGSRVPLY:SPRTEMERGSRV="YES",SPRTEMERGSRVCARDLESS="YES",AUTHEMERGREGIST="YES",PASSAUTHFAIL="YES",PASSLIMITEDUSER="YES",PEICHECKEMERGREGIST="YES",PASSPEICHECKFAIL="YES",PASSPEIGETFAIL="YES",RPTSUPICONSTUBYPEI="YES",EMERGENCYCAPA="BOTHNRANDEUTRANSPRT",DFTEMC="YES",DFTEMF="YES",IFCARRYEMRNUMLIST="YES",IFCARRYEXTEMRNUMLIST="YES",EMERGNUMLISTID=0,EXTEMERGNUMLISTID=0,SENDEMGNUMSPTEMGCALL="AMFINDICATEUESPTEMCEMF"
` 
#### 查询紧急业务策略(SHOW EMERGSRVPLY) 
#### 查询紧急业务策略(SHOW EMERGSRVPLY) 
功能说明 
本命令用于查询紧急业务策略配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
sprtEmergSrv|支持紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制AMF是否开启紧急业务。0：否1：是
sprtEmergSrvCardless|支持无卡用户紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制AMF是否允许无卡终端用户触发紧急业务。0：否1：是
authEmergRegist|紧急注册鉴权|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制用户紧急注册时，AMF是否需要启动鉴权。0：否1：是
passAuthFail|鉴权失败放行紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制当用户鉴权失败时，若该用户已经激活紧急业务，则AMF是否允许该用户继续紧急业务。0：否1：是
passLimitedUser|受限用户放行紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制当用户业务受限时，若该用户已经激活紧急业务，则AMF是否允许该用户继续紧急业务。受限业务包括：接入限制、移动性限制、会话限制、签约限制。0：否1：是
peiCheckEmergRegist|紧急注册检查PEI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制用户紧急注册时，AMF是否需要启动PEI检查。0：否1：是
passPeiCheckFail|PEI检查限制接入时放行紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|本参数用于控制当PEI检查导致接入限制，流程失败是否放行紧急业务。0：否1：是
passpeigetfail|向UE获取IMEI(SV)失败限制接入时放行紧急业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：当AMF向UE获取IMEI(SV)失败时，如果"PEI检查配置"中的"向UE获取IMEI(SV)失败时AMF是否限制接入"配置为限制接入并且当前是紧急业务，需要继续判断此开关, 根据此开关控制针对紧急业务是否额外放行。 0: 否1: 是
rptSupiConstuByPei|上报PEI构造的SUPI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：本参数用于控制无卡用户使用PEI进行紧急注册时，AMF使用用户的PEI构造了SUPI，在进行信令跟踪和失败观察业务时，是否上报此构造的SUPI。0: 否1: 是
emergencyCapa|默认紧急业务能力|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: BOTHNRANDEUTRANSPRT|参数作用：本参数用于配置支持紧急业务的默认无线接入类型，取值及含义如下：0：NR和E-UTRAN均不支持。本AMF没有配置的TA下，使用NR和E-UTRAN接入的用户均不支持紧急业务。1：仅NR支持。本AMF没有配置的TA下，仅NR接入的用户支持紧急业务。 2：仅E-UTRAN支持。本AMF没有配置的TA下，仅E-UTRAN接入的用户支持紧急业务。3：NR和E-UTRAN均支持。本AMF没有配置的TA下，NR和E-UTRAN接入的用户均支持紧急业务。
dftemc|缺省是否支持EMC|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，使用该参数控制是否支持EMC。0: 否1: 是
dftemf|缺省是否支持EMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，使用该参数控制是否支持EMF。0: 否1: 是
ifcarryemrnumlist|缺省是否携带紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，使用该参数标识是否携带紧急号码列表给UE。0: 否1: 是
ifcarryextemrnumlist|缺省是否携带扩展紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，使用该参数标识是否携带扩展紧急号码列表给UE。0: 否1: 是
emergnumlistid|缺省紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，如果紧急业务策略配置支持携带紧急号码列表，使用该参数控制下发给UE的紧急号码列表ID。设置为0表示无效，表示使用服务TA上配置的紧急号码列表ID。设置为非0表示有效，表示使用此处配置的紧急号码列表ID。
extemergnumlistid|缺省扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：在“基于号段的紧急呼叫策略配置（通过SHOW USERSEGEMERGSRPLY命令查询获取结果）”中没有匹配到号段时，如果紧急业务策略配置支持携带扩展紧急号码列表，使用该参数控制下发给UE的扩展紧急号码列表ID。设置为0表示无效，表示使用服务TA上配置的扩展紧急号码列表ID。设置为非0表示有效，表示使用此处配置的扩展紧急号码列表ID。
sendemgnumsptemgcall|AMF下发紧急号码对支持紧急呼叫的依赖策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: AMFINDICATEUESPTEMCEMF|本参数用于控制是否在支持紧急呼叫时才下发紧急号码。下发的紧急号码用于让UE识别呼叫是否为紧急呼叫，当AMF不支持紧急呼叫时，UE能够根据拨号识别紧急呼叫，选择其它类型网元（比如CS）发起紧急呼叫。包括以下三种策略方式：0：AMF指示UE支持紧急业务或者紧急业务回落时下发紧急号码。1：AMF开启支持紧急业务或者紧急业务回落时下发紧急号码。2：无依赖，总是下发紧急号码。
命令举例 
`
查询紧急业务策略。
SHOW EMERGSRVPLY
(No.4) : SHOW EMERGSRVPLY:
-----------------Namf_Communication_0----------------
操作维护       支持紧急业务 支持无卡用户紧急业务 紧急注册鉴权 鉴权失败放行紧急业务 受限用户放行紧急业务 紧急注册检查PEI PEI检查限制接入时放行紧急业务 向UE获取IMEI(SV)失败限制接入时放行紧急业务 上报PEI构造的SUPI 默认紧急业务能力  缺省是否支持EMC 缺省是否支持EMF 缺省是否携带紧急号码列表 缺省是否携带扩展紧急号码列表 缺省紧急号码列表ID 缺省扩展紧急号码列表ID AMF下发紧急号码对支持紧急呼叫的依赖策略
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           是           是                   是           是                   是                   是              是                            是                                         是                NR和E-UTRAN均支持 是              是              是                       是                           0                  0                    仅AMF指示UE支持紧急业务或紧急业务回落时下发紧急号码  
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-07-11 15:08:22 耗时: 0.166 秒
` 
### 基于号段的紧急业务策略配置 
### 基于号段的紧急业务策略配置 
背景知识 
在5GC网络中，运营商通过IMS为用户提供语音业务，也提供紧急呼叫业务，5GC网络与IMS网络建立紧急会话来给用户提供紧急呼叫业务。 
根据用户合法性划分，AMF支持紧急的呼叫有： 
 
仅完全合法有效用户可以发起紧急业务呼叫。 
 
仅鉴权合法用户（可能位置被限制）可以发起紧急业务呼叫。 
 
具有SUPI的用户（可能鉴权失败、位置被限制）可以发起紧急业务呼叫。 
 
任意用户（可能不具有SUPI、鉴权失败、位置被限制）可以发起紧急业务呼叫。 
 
功能说明 
AMF支持根据用户的号段，来配置紧急呼叫业务，可以设置特定用户号段的用户的紧急业务策略，用于区分不同用户，可以使用不同紧急业务策略。 
子主题： 
#### 新增基于号段的紧急业务策略配置(ADD USERSEGEMERGSRPLY) 
#### 新增基于号段的紧急业务策略配置(ADD USERSEGEMERGSRPLY) 
功能说明 
本命令用于新增基于SUPI号段或GPSI号段或PEI号段设置紧急业务策略配置。当需要针对SUPI号段或GPSI号段或PEI号段设置紧急业务策略时，使用该命令进行配置。 
配置成功后，如果用户号段匹配本配置，则AMF向用户提供的紧急业务受此配置影响。 
注意事项 
此命令执行后立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
usersegment|用户标识|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于配置需要设置紧急呼叫策略的用户的SUPI或GPSI或PEI号段。其中PEI号段指的是用户的IMEI号段。 修改影响：本字段为关键索引, 不允许修改，如需修改，需先删除，再增加。 数据来源：本端规划。 默认值：无。配置原则： 本字段为配置关键索引，不允许重复。
segmenttype|用户标识类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|参数作用：此参数用于标识号段的类型。0-SUPI1-GPSI2-PEI（PEI指用户的IMEI）修改影响：本字段为关键索引, 不允许修改，如需修改，需先删除，再增加。 数据来源：本端规划。 默认值：0。 配置原则：无 。
emc|是否支持EMC|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：此参数用于配置该用户号段是否支持紧急业务。修改影响：当根据号段可以匹配到此配置时, 修改此参数, 会影响用户是否支持紧急业务的决策结果，最终影响注册接受消息"network feature support"字段中的EMC标记是否携带或携带时的取值。 数据来源：本端规划。 默认值：1。 配置原则： 无。
emf|是否支持EMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：此参数用于配置该用户号段是否支持紧急回落业务。修改影响：当根据号段可以匹配到此配置时, 修改此参数, 会影响用户是否支持紧急回落业务的决策结果，最终影响注册接受消息"network feature support"字段中的EMF标记是否携带或携带时的取值。 数据来源：本端规划。 默认值：1。 配置原则： 无。
ifcarryemrnumlist|是否携带紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：此参数用于设置AMF是否给本号段用户下发紧急号码列表。修改影响：当根据号段可以匹配到此配置时，修改此参数会影响AMF是否下发紧急号码列表给UE的决策结果，最终影响注册接受消息是否携带emergencyNumberList字段。数据来源：本端规划。默认值：1。配置原则：无。
ifcarryextemrnumlist|是否携带扩展紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：此参数用于设置AMF是否给本号段用户下发扩展紧急号码列表。修改影响：当根据号段可以匹配到此配置时，修改此参数会影响AMF是否给本号段用户下发扩展紧急号码列表的决策结果，最终影响注册接受消息是否携带extendEmergencyNumberList字段。数据来源：本端规划。默认值：1。配置原则：无。
emergnumlistid|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：此参数用于设置AMF给本号段用户下发的紧急号码列表的ID。??设置为0表示无效，表示使用服务TA上配置的紧急号码列表ID；??设置为非0表示有效，表示使用此处配置的紧急号码列表ID。修改影响：当根据号段可以匹配到此配置时，如果AMF向本号段用户下发紧急号码列表，修改此参数会影响下发给用户的紧急号码列表ID，最终影响注册接受消息的“emergencyNumberList”字段携带的紧急号码列表。数据来源：本端规划。默认值：0。配置原则：本参数的取值引用于ADD 5GEMERNUMLIST命令配置的参数“ListID ”，必须通过ADD 5GEMERNUMLIST命令预先配置。
extemergnumlistid|扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：此参数用于设置AMF给本号段用户下发的扩展紧急号码列表的ID。??设置为0表示无效，表示使用服务TA上配置的扩展紧急号码列表ID；??设置为非0表示有效，表示使用此处配置的扩展紧急号码列表ID。修改影响：当根据号段可以匹配到此配置时，如果AMF向本号段用户下发扩展紧急号码列表，修改此参数会影响下发给用户的扩展紧急号码列表ID，最终影响注册接受消息的“extendEmergencyNumberList”字段携带的扩展紧急号码列表。数据来源：本端规划。默认值：0。配置原则：本参数的取值引用于ADD 5GEXTEMERNUMLIST命令配置的参数“ListID ”，必须通过ADD 5GEXTEMERNUMLIST命令预先配置。
命令举例 
`
新增基于号段的紧急业务策略配置：设置用户号段为“46011”，设置用户号段类型为SUPITYPE，支持携带EMC，支持携带EMF，支持携带紧急号码列表，支持携带扩展紧急号码列表，关联的紧急号码列表ID是1，关联的扩展紧急号码列表ID是1
ADD USERSEGEMERGSRPLY:USERSEGMENT="46011",SEGMENTTYPE="SUPITYPE",EMC="YES",EMF="YES",IFCARRYEMRNUMLIST="YES",IFCARRYEXTEMRNUMLIST="YES",EMERGNUMLISTID=1,EXTEMERGNUMLISTID=1
` 
#### 修改基于号段的紧急业务策略配置(SET USERSEGEMERGSRPLY) 
#### 修改基于号段的紧急业务策略配置(SET USERSEGEMERGSRPLY) 
功能说明 
本命令用于修改基于SUPI号段或GPSI号段或PEI号段设置的紧急业务策略配置。 
当本号段用户的紧急业务策略变更时，使用此命令修改本号段用户的紧急业务策略。 
注意事项 
此命令执行后立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
usersegment|用户标识|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于配置需要设置紧急呼叫策略的用户的SUPI或GPSI或PEI号段。其中PEI号段指的是用户的IMEI号段。 修改影响：本字段为关键索引, 不允许修改，如需修改，需先删除，再增加。 数据来源：本端规划。 默认值：无。配置原则： 本字段为配置关键索引，不允许重复。
segmenttype|用户标识类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|参数作用：此参数用于标识号段的类型。0-SUPI1-GPSI2-PEI（PEI指用户的IMEI）修改影响：本字段为关键索引, 不允许修改，如需修改，需先删除，再增加。 数据来源：本端规划。 默认值：0。 配置原则：无 。
emc|是否支持EMC|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：此参数用于配置该用户号段是否支持紧急业务。修改影响：当根据号段可以匹配到此配置时, 修改此参数, 会影响用户是否支持紧急业务的决策结果，最终影响注册接受消息"network feature support"字段中的EMC标记是否携带或携带时的取值。 数据来源：本端规划。 默认值：1。 配置原则： 无。
emf|是否支持EMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：此参数用于配置该用户号段是否支持紧急回落业务。修改影响：当根据号段可以匹配到此配置时, 修改此参数, 会影响用户是否支持紧急回落业务的决策结果，最终影响注册接受消息"network feature support"字段中的EMF标记是否携带或携带时的取值。 数据来源：本端规划。 默认值：1。 配置原则： 无。
ifcarryemrnumlist|是否携带紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：此参数用于设置AMF是否给本号段用户下发紧急号码列表。修改影响：当根据号段可以匹配到此配置时，修改此参数会影响AMF是否下发紧急号码列表给UE的决策结果，最终影响注册接受消息是否携带emergencyNumberList字段。数据来源：本端规划。默认值：1。配置原则：无。
ifcarryextemrnumlist|是否携带扩展紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：此参数用于设置AMF是否给本号段用户下发扩展紧急号码列表。修改影响：当根据号段可以匹配到此配置时，修改此参数会影响AMF是否给本号段用户下发扩展紧急号码列表的决策结果，最终影响注册接受消息是否携带extendEmergencyNumberList字段。数据来源：本端规划。默认值：1。配置原则：无。
emergnumlistid|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：此参数用于设置AMF给本号段用户下发的紧急号码列表的ID。??设置为0表示无效，表示使用服务TA上配置的紧急号码列表ID；??设置为非0表示有效，表示使用此处配置的紧急号码列表ID。修改影响：当根据号段可以匹配到此配置时，如果AMF向本号段用户下发紧急号码列表，修改此参数会影响下发给用户的紧急号码列表ID，最终影响注册接受消息的“emergencyNumberList”字段携带的紧急号码列表。数据来源：本端规划。默认值：0。配置原则：本参数的取值引用于ADD 5GEMERNUMLIST命令配置的参数“ListID ”，必须通过ADD 5GEMERNUMLIST命令预先配置。
extemergnumlistid|扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|参数作用：此参数用于设置AMF给本号段用户下发的扩展紧急号码列表的ID。??设置为0表示无效，表示使用服务TA上配置的扩展紧急号码列表ID；??设置为非0表示有效，表示使用此处配置的扩展紧急号码列表ID。修改影响：当根据号段可以匹配到此配置时，如果AMF向本号段用户下发扩展紧急号码列表，修改此参数会影响下发给用户的扩展紧急号码列表ID，最终影响注册接受消息的“extendEmergencyNumberList”字段携带的扩展紧急号码列表。数据来源：本端规划。默认值：0。配置原则：本参数的取值引用于ADD 5GEXTEMERNUMLIST命令配置的参数“ListID ”，必须通过ADD 5GEXTEMERNUMLIST命令预先配置。
命令举例 
`
修改基于号段的紧急业务策略配置：修改用户号段为“46011”，用户号段类型为SUPITYPE的紧急业务策略配置为不支持携带EMC，不支持携带EMF不支持携带紧急号码列表，不支持携带扩展紧急号码列表，关联的紧急号码列表ID为1，关联的扩展紧急号码列表为1。
` 
#### 删除基于号段的紧急业务策略配置(DEL USERSEGEMERGSRPLY) 
#### 删除基于号段的紧急业务策略配置(DEL USERSEGEMERGSRPLY) 
功能说明 
本命令用于删除基于SUPI号段或GPSI号段或PEI号段设置的紧急业务策略配置。 
当本号段用户的紧急业务策略变更，需要删除本号段用户的紧急业务策略时，使用此命令删除本号段用户的紧急业务策略。 
注意事项 
此命令执行后立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
usersegment|用户标识|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于配置需要设置紧急呼叫策略的用户的SUPI或GPSI或PEI号段。其中PEI号段指的是用户的IMEI号段。 修改影响：本字段为关键索引, 不允许修改，如需修改，需先删除，再增加。 数据来源：本端规划。 默认值：无。配置原则： 本字段为配置关键索引，不允许重复。
segmenttype|用户标识类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2|参数作用：此参数用于标识号段的类型。0-SUPI1-GPSI2-PEI（PEI指用户的IMEI）修改影响：本字段为关键索引, 不允许修改，如需修改，需先删除，再增加。 数据来源：本端规划。 默认值：0。 配置原则：无 。
命令举例 
`
删除基于号段的紧急业务策略配置：删除的用户号段为“46011”，号段类型为“SUPITYPE”。
DEL USERSEGEMERGSRPLY:USERSEGMENT="46011",SEGMENTTYPE="SUPITYPE"
` 
#### 查询基于号段的紧急业务策略配置(SHOW USERSEGEMERGSRPLY) 
#### 查询基于号段的紧急业务策略配置(SHOW USERSEGEMERGSRPLY) 
功能说明 
本命令用于查询基于SUPI号段或GPSI号段或PEI号段设置的紧急业务策略配置。 
注意事项 
此命令执行后立即生效。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
usersegment|用户标识|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：此参数用于配置需要设置紧急呼叫策略的用户的SUPI或GPSI或PEI号段。其中PEI号段指的是用户的IMEI号段。 修改影响：本字段为关键索引, 不允许修改，如需修改，需先删除，再增加。 数据来源：本端规划。 默认值：无。配置原则： 本字段为配置关键索引，不允许重复。
segmenttype|用户标识类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|参数作用：此参数用于标识号段的类型。0-SUPI1-GPSI2-PEI（PEI指用户的IMEI）修改影响：本字段为关键索引, 不允许修改，如需修改，需先删除，再增加。 数据来源：本端规划。 默认值：0。 配置原则：无 。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
usersegment|用户标识|参数可选性: 任选参数类型: 字符串参数范围: 1-15|此参数用于配置需要设置紧急呼叫策略的用户的SUPI或GPSI或PEI号段。
segmenttype|用户标识类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2|此参数用于标识号段的类型。
emc|是否支持EMC|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|此参数用于配置该用户号段是否支持紧急业务。
emf|是否支持EMF|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|此参数用于配置该用户号段是否支持紧急回落业务。
ifcarryemrnumlist|是否携带紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|此参数用于设置AMF是否给本号段用户下发紧急号码列表。
ifcarryextemrnumlist|是否携带扩展紧急号码列表|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|此参数用于设置AMF是否给本号段用户下发紧急号码列表。
emergnumlistid|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|此参数用于设置AMF给本号段用户下发的紧急号码列表的ID。??设置为0表示无效，表示使用服务TA上配置的紧急号码列表ID；??设置为非0表示有效，表示使用此处配置的紧急号码列表ID。
extemergnumlistid|扩展紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 0-50默认值: 0|此参数用于设置AMF给本号段用户下发的扩展紧急号码列表的ID。??设置为0表示无效，表示使用服务TA上配置的扩展紧急号码列表ID；??设置为非0表示有效，表示使用此处配置的扩展紧急号码列表ID。
命令举例 
`
查询基于号段的紧急业务策略配置
SHOW USERSEGEMERGSRPLY:USERSEGMENT="46011",SEGMENTTYPE="SUPITYPE"
(No.9) : SHOW USERSEGEMERGSRPLY:USERSEGMENT="46011",SEGMENTTYPE="SUPITYPE"
-----------------Namf_Communication_0----------------
Operation and maintenance 用户标识 用户标识类型 是否支持EMC 是否支持EMF 是否携带紧急号码列表 是否携带扩展紧急号码列表 紧急号码列表ID 扩展紧急号码列表ID 
--------------------------------------------------------------------------------------------------------------------------------------------------------
COPY MODIFY DELETE        46011    SUPI号段     是          是          是                   是                       1              1                  
--------------------------------------------------------------------------------------------------------------------------------------------------------
Total Records：1
Execute SuccessfullyStart Time:2022-06-25 19:15:18 Elapsed Time: 0.152 s
` 
### 紧急数据配置 
### 紧急数据配置 
背景知识 
AMF支持1个PLMN配置1条紧急数据，紧急数据包括紧急DNN、紧急DNN对应的SMF信息（包括SMF IP地址、SMF端口号、SMF FQDN等）。 
功能说明 
本功能用于配置紧急数据。 
通过本功能的配置数据，当终端用户进行紧急业务时，AMF根据紧急DNN找到支持紧急业务的SMF，将紧急PDU会话建立请求消息，路由给该SMF，完成紧急PDU会话的建立。 
子主题： 
#### 新增紧急数据配置(ADD EMERGDATA) 
#### 新增紧急数据配置(ADD EMERGDATA) 
功能说明 
该命令用于增加紧急数据配置。 
通过本命令的配置数据，当终端用户进行紧急业务时，AMF根据紧急DNN找到支持紧急业务的SMF，将紧急PDU会话建立请求消息，路由给该SMF，完成紧急PDU会话的建立。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 必选参数类型: 字符串参数范围: 1-63|该参数用于配置启用紧急业务时，使用的DNN（Data Network Name，数据网名称） NI名称。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。
smfIp|SMF IP|参数可选性: 任选参数类型: 字符串参数范围: 2-40|该参数用于配置启用紧急业务时，SMF的IP地址，地址格式可以为IPv4或IPv6。
smfPort|SMF端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置启用紧急业务时，SMF的端口号。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置启用紧急业务时，SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置配置启用紧急业务时，SMF的API版本，比如v1或v2。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
smffqdn|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置启用紧急业务时，SMF的FQDN（Fully Qualified Domain Name，全称域名）。FQDN只支持输入小写。
supportinterworking|支持互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTSPRTINTERWORKING|本参数用于控制紧急业务是否支持互操作，参数如下：不支持互操作支持互操作根据用户能力判断默认值为不支持互操作
name|名称|参数可选性: 任选参数类型: 字符串参数范围: 1-50|该参数用于配置该条紧急数据名称，由操作员自行定义。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置SMF网元的实例名称，依据网络规划配置。修改影响：nfInstanceName是一个网元的唯一实例名称，操作员不能随意修改，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：同类型NF本地解析配置中，nfInstanceName不允许重复。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于配置启用紧急业务时，使用的DNN（Data Network Name，数据网名称） NI名称。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。
smfIp|SMF IP|参数可选性: 任选参数类型: 字符串参数范围: 2-40|该参数用于配置启用紧急业务时，SMF的IP地址，地址格式可以为IPv4或IPv6。
smfPort|SMF端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置启用紧急业务时，SMF的端口号。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置启用紧急业务时，SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置配置启用紧急业务时，SMF的API版本，比如v1或v2。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
smffqdn|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置启用紧急业务时，SMF的FQDN（Fully Qualified Domain Name，全称域名）。FQDN只支持输入小写。
supportinterworking|支持互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTSPRTINTERWORKING|本参数用于控制紧急业务是否支持互操作，参数如下：不支持互操作支持互操作根据用户能力判断默认值为不支持互操作
name|名称|参数可选性: 任选参数类型: 字符串参数范围: 1-50|该参数用于配置该条紧急数据名称，由操作员自行定义。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置SMF网元的实例名称，依据网络规划配置。
命令举例 
`
增加PLMN为MCC460，MNC01的紧急数据配置，DNN为"cmnet.com"，SMF IP为"10.10.10.10"，SMF端口号为8080.URI模式为"HTTP",版本为"V1"，NF实例标识为f81d4fae-7dec-1111-a765-00a0c91e6789，FQDN为fqdn.com,并且支持互操作,并且NFINSTANCENAME为"GD_GX_NN_SMF100_C_ZTE"。
ADD EMERGDATA:MCC="460",MNC="01",DNN="cmnet.com",SMFIP="10.10.10.10",SMFPORT=8080,SCHEMA="HTTP",APIVERSION="V1",NFINSTANCEID="f81d4fae-7dec-1111-a765-00a0c91e6789",SMFFQDN="fqdn.com",SUPPORTINTERWORKING="SPRTINTERWORKING",NFINSTANCENAME="GD_GX_NN_SMF100_C_ZTE"
` 
#### 修改紧急数据配置(SET EMERGDATA) 
#### 修改紧急数据配置(SET EMERGDATA) 
功能说明 
该命令用于修改紧急数据配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于配置启用紧急业务时，使用的DNN（Data Network Name，数据网名称） NI名称。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。
smfIp|SMF IP|参数可选性: 任选参数类型: 字符串参数范围: 2-40|该参数用于配置启用紧急业务时，SMF的IP地址，地址格式可以为IPv4或IPv6。
smfPort|SMF端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置启用紧急业务时，SMF的端口号。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置启用紧急业务时，SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置配置启用紧急业务时，SMF的API版本，比如v1或v2。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
smffqdn|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置启用紧急业务时，SMF的FQDN（Fully Qualified Domain Name，全称域名）。FQDN只支持输入小写。
supportinterworking|支持互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTSPRTINTERWORKING|本参数用于控制紧急业务是否支持互操作，参数如下：不支持互操作支持互操作根据用户能力判断默认值为不支持互操作
name|名称|参数可选性: 任选参数类型: 字符串参数范围: 1-50|该参数用于配置该条紧急数据名称，由操作员自行定义。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置SMF网元的实例名称，依据网络规划配置。修改影响：nfInstanceName是一个网元的唯一实例名称，操作员不能随意修改，必须全网统一规划，确保全网没有重复。数据来源：全网规划。默认值：无。配置原则：同类型NF本地解析配置中，nfInstanceName不允许重复。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于配置启用紧急业务时，使用的DNN（Data Network Name，数据网名称） NI名称。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。
smfIp|SMF IP|参数可选性: 任选参数类型: 字符串参数范围: 2-40|该参数用于配置启用紧急业务时，SMF的IP地址，地址格式可以为IPv4或IPv6。
smfPort|SMF端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置启用紧急业务时，SMF的端口号。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置启用紧急业务时，SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置配置启用紧急业务时，SMF的API版本，比如v1或v2。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
smffqdn|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置启用紧急业务时，SMF的FQDN（Fully Qualified Domain Name，全称域名）。FQDN只支持输入小写。
supportinterworking|支持互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTSPRTINTERWORKING|本参数用于控制紧急业务是否支持互操作，参数如下：不支持互操作支持互操作根据用户能力判断默认值为不支持互操作
name|名称|参数可选性: 任选参数类型: 字符串参数范围: 1-50|该参数用于配置该条紧急数据名称，由操作员自行定义。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置SMF网元的实例名称，依据网络规划配置。
命令举例 
`
修改PLMN为MCC460，MNC01的紧急数据配置，DNN为"cmnet.com"，SMF IP为"20.20.20.20"，SMF端口号为9090.
SET EMERGDATA:MCC="460",MNC="01",SMFIP="20.20.20.20",SMFPORT=9090
` 
#### 删除紧急数据配置(DEL EMERGDATA) 
#### 删除紧急数据配置(DEL EMERGDATA) 
功能说明 
该命令用于删除紧急数据配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于配置启用紧急业务时，使用的DNN（Data Network Name，数据网名称） NI名称。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。
smfIp|SMF IP|参数可选性: 任选参数类型: 字符串参数范围: 2-40|该参数用于配置启用紧急业务时，SMF的IP地址，地址格式可以为IPv4或IPv6。
smfPort|SMF端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置启用紧急业务时，SMF的端口号。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置启用紧急业务时，SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置配置启用紧急业务时，SMF的API版本，比如v1或v2。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
smffqdn|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置启用紧急业务时，SMF的FQDN（Fully Qualified Domain Name，全称域名）。FQDN只支持输入小写。
supportinterworking|支持互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTSPRTINTERWORKING|本参数用于控制紧急业务是否支持互操作，参数如下：不支持互操作支持互操作根据用户能力判断默认值为不支持互操作
name|名称|参数可选性: 任选参数类型: 字符串参数范围: 1-50|该参数用于配置该条紧急数据名称，由操作员自行定义。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置SMF网元的实例名称，依据网络规划配置。
命令举例 
`
删除PLMN为MCC460，MNC01的紧急数据配置
DEL EMERGDATA:MCC="460",MNC="01" 
` 
#### 查询紧急数据配置(SHOW EMERGDATA) 
#### 查询紧急数据配置(SHOW EMERGDATA) 
功能说明 
该命令用于查询紧急数据配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
dnn|DNN|参数可选性: 任选参数类型: 字符串参数范围: 1-63|该参数用于配置启用紧急业务时，使用的DNN（Data Network Name，数据网名称） NI名称。5G网络中定义的DNN就是4G网络中定义的APN，DNN和APN是等价的（参见3GPP TS23.003? 9A章节），所以3GPP协议中对APN的描述和定义与使用就是DNN的描述和定义与使用。DNN或APN的组成有两部分：网络ID，这部分表示一个外部网络，这部分是必选的。运营商ID，这部分表示其属于哪个运营商的，这部分是可选的。网络ID：网络ID至少包含有一个标签，其长度最长为63字节；其不能以字符串“rac”、"lac"、"sgsn"、"rnc"等网元名称开头，不能以".gprs"结尾，此外还不能包含"*"。运营商ID：运营商ID由三个标签组成，最后一个标签必须为“.gprs”，第一和第二个标签要唯一地标识出一个PLMN；每个运营商都有一个默认的DNN/APN运营商ID，默认的运营商ID是从IMSI推导出来的：“mnc.mcc.gprs”。对于LBO的漫游场景（也就是在VPLMN的PGW/UPF提供访问外部网络的业务时），DNN/APN的运营商ID应该是VPLMN的网络ID。DNN只支持输入小写。
smfIp|SMF IP|参数可选性: 任选参数类型: 字符串参数范围: 2-40|该参数用于配置启用紧急业务时，SMF的IP地址，地址格式可以为IPv4或IPv6。
smfPort|SMF端口号|参数可选性: 任选参数类型: 数字参数范围: 1-65535默认值: 8080|该参数用于配置启用紧急业务时，SMF的端口号。
schema|URI scheme|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: HTTP|该参数用于配置启用紧急业务时，SMF的URI scheme。比如 "http"、"https"。
apiVersion|API版本|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: V1|该参数用于配置配置启用紧急业务时，SMF的API版本，比如v1或v2。
nfinstanceid|NF实例标识|参数可选性: 任选参数类型: 字符串参数范围: 36-36|NF实例标识，用于查询配置中对应的SMF Profile标识。采用UUID版本4格式（RFC 4122）共128个bit，以32个16进制数，并以"-"分为5段标识，具体为："time-low "-" time-mid "-" time-high-and-version "-" clock-seq-and-reserved clock-seq-low "-" node。只能为a-f、0-9的字符。
smffqdn|SMF FQDN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置启用紧急业务时，SMF的FQDN（Fully Qualified Domain Name，全称域名）。FQDN只支持输入小写。
supportinterworking|支持互操作|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: NOTSPRTINTERWORKING|本参数用于控制紧急业务是否支持互操作，参数如下：不支持互操作支持互操作根据用户能力判断默认值为不支持互操作
name|名称|参数可选性: 任选参数类型: 字符串参数范围: 1-50|该参数用于配置该条紧急数据名称，由操作员自行定义。
nfinstancename|NF实例名|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：该参数用于设置SMF网元的实例名称，依据网络规划配置。
命令举例 
`
查询PLMN为MCC460，MNC01的紧急数据配置
SHOW EMERGDATA:MCC="460",MNC="01";
(No.1) : SHOW EMERGDATA:
-----------------Namf_Communication_0----------------
操作维护       移动国家码 移动网络码 DNN SMF IP      SMF端口号 URI scheme API版本 NF实例标识                           SMF FQDN 支持互操作 名称   NF实例名
-------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 460        01         ims 20.20.20.20 8080      http       v1      f81d4fae-7dec-1111-a765-00a0c91e6789 zte.com  支持互操作      
-------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-12 15:30:13 耗时: 0.136 秒
` 
### 紧急号码配置 
### 紧急号码配置 
背景知识 
不同国家的紧急号码不同，当终端移动到不同区域时，运营商要指示终端，其所处位置的紧急号码。 
功能说明 
终端注册时，AMF要指示终端，当前位置支持的紧急号码列表。 
子主题： 
#### 紧急号码列表配置 
#### 紧急号码列表配置 
背景知识 
在UE注册时，AMF通知UE紧急号码，以便UE在拨打呼叫时判断是否为紧急呼叫。 
紧急号码可以基于UE接入的TA设置，也可以基于用户号段设置，当二者都设置时，以号段设置优先。 
功能说明 
本功能用于配置多组紧急号码列表，以紧急号码列表ID为标识。每组号码列表中包含多个号码（比如110报警号码、119火警号码）。 
在跟踪区配置[ADD TACFG]/[SET TACFG]命令中，可以为TA选择其对应的紧急号码列表ID；在基于号段的紧急业务策略配置[ADD USERSEGEMERGSRPLY]/[SET USERSEGEMERGSRPLY]命令中，可以为号段选择其对应的紧急号码列表ID，当号段和TA都配置紧急号码列表ID时，以号段配置优先。
在注册流程中，AMF根据TA配置和号段配置，决策使用紧急号码列表ID，在REGISTRATION ACCEPT消息中将紧急号码列表发送给UE终端，UE基于此号码列表判断拨打的号码是否为紧急号码。 
子主题： 
##### 新增紧急号码列表配置(ADD 5GEMERNUMLIST) 
##### 新增紧急号码列表配置(ADD 5GEMERNUMLIST) 
功能说明 
该命令用于增加紧急号码列表中的紧急号码。当需要指示UE哪些是紧急号码以便UE识别紧急呼叫时，使用该命令。 
在通过本命令设置紧急呼叫列表并通过[ADD TACFG]命令关联到相应的TA后，当终端从该TA成功接入后，AMF会将相应的紧急号码列表发送给UE。当通过用户号段配置关联紧急呼叫号码列表时，系统优先使用用户号段关联的紧急号码下发给UE。
注意事项 
 
当紧急号码长度较大时，AMF会减少实际携带的号码数量。由于号码长度不同，而协议中携带的数据大小有限，因此并不能保证10个号码都能携带给终端。一般情况下足够使用，可携带至少10个4位数的紧急号码。 
 
在创建或修改TA时，在ADD TACFG命令或者SET TACFG命令中，可以设置该TA关联使用的紧急号码列表，其中参数emergencyNumListID即该TA使用的紧急号码列表ID。需要先通过本命令先配置“紧急号码列表ID”，然后在ADD TACFG命令中引用此“紧急号码列表ID。当需要开启基于用户号段下发不同紧急号码功能时，使用命令ADD USERSEGEMERGSRPLY或者SET USERSEGEMERGSRPLY可以设置该号段关联使用的紧急号码列表，其中参数emergnumlistid即该号段使用的紧急号码列表ID；使用命令SET EMERGSRVPLY可以设置缺省号段关联使用的紧急号码列表，其中参数emergnumlistid即缺省号段使用的紧急号码列表ID。 
 
是否下发紧急号码，受紧急业务策略配置（SET EMERGSRVPLY）命令中的配置参数“AMF下发紧急号码对支持紧急呼叫的依赖策略”控制，具体控制策略为：
0-AMF指示UE支持EMC或者EMF时下发紧急号码
1-AMF开启支持EMC或者EMF时下发紧急号码
2-无依赖，AMF总是下发紧急号码
 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 必选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 必选参数类型: 字符串参数范围: 1-20|紧急呼叫对应的紧急号码，例如：110、119、120。
type|服务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
输出参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|紧急呼叫对应的紧急号码，例如：110、119、120。
type|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
命令举例 
`
新增紧急号码列表ID为1、号码为110，类型为"报警"的紧急号码。
ADD 5GEMERNUMLIST:LISTID=1,NUMBER="110",TYPE="PC"
` 
##### 修改紧急号码列表配置(SET 5GEMERNUMLIST) 
##### 修改紧急号码列表配置(SET 5GEMERNUMLIST) 
功能说明 
该命令用于修改紧急号码列表中的紧急号码。。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 必选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 必选参数类型: 字符串参数范围: 1-20|紧急呼叫对应的紧急号码，例如：110、119、120。
type|服务类型|参数可选性: 必选参数类型: 枚举，参见枚举定义|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
输出参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|紧急呼叫对应的紧急号码，例如：110、119、120。
type|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
命令举例 
`
将紧急号码ID为1并且号码为110的紧急号码的紧急类型修改为"报警"
SET 5GEMERNUMLIST:LISTID=1,NUMBER="110",TYPE="PC"
` 
##### 删除紧急号码列表配置(DEL 5GEMERNUMLIST) 
##### 删除紧急号码列表配置(DEL 5GEMERNUMLIST) 
功能说明 
该命令用于从紧急号码列表中删除一个紧急号码。 
删除该号码之后，UE不再将此号码作为紧急呼叫使用，只会按照普通电话的要求建立连接。 
注意事项 
 
当删除命令中仅包含紧急号码列表ID时，则可以删除该紧急号码ID关联全部的紧急号码。 
 
在删除紧急号码ID下全部的紧急号码前，需要先删除ADD TACFG、SET TACFG、ADD USERSEGEMERGSRPLY、SET USERSEGEMERGSRPLY和SET EMERGSRVPLY命令中所关联的该紧急号码列表ID。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 必选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|紧急呼叫对应的紧急号码，例如：110、119、120。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|紧急呼叫对应的紧急号码，例如：110、119、120。
type|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
命令举例 
`
将紧急号码ID为1并且号码为110的紧急号码删除
DEL 5GEMERNUMLIST:LISTID=1,NUMBER="110"
` 
##### 查询紧急号码列表配置(SHOW 5GEMERNUMLIST) 
##### 查询紧急号码列表配置(SHOW 5GEMERNUMLIST) 
功能说明 
该命令用于显示紧急号码列表的紧急号码及其类型。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|紧急呼叫对应的紧急号码，例如：110、119、120。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|紧急呼叫对应的紧急号码，例如：110、119、120。
type|服务类型|参数可选性: 任选参数类型: 枚举，参见枚举定义|该参数用于指定紧急呼叫号码类型。一个紧急号码可以属于一种或多种类型。例如美国911既是报警，也是火警、救援号码。而中国119仅是火警号码。取值含义：PC：报警AMB：救护FIRE：火警MG：海洋救援MR：山地救援MIE：手动触发的紧急呼叫AIE：自动触发的紧急呼叫
命令举例 
`
查询紧急号码ID为1关联的所有紧急号码
SHOW 5GEMERNUMLIST:LISTID=1
(No.1) : SHOW 5GEMERNUMLIST:
-----------------Namf_Communication_0----------------
紧急号码列表ID    紧急号码    服务类型
1                        110          PC
记录数：1
执行成功耗时: 0.12 秒
` 
#### 扩展紧急号码列表配置 
#### 扩展紧急号码列表配置 
背景知识 
在UE注册时，AMF通知UE扩展紧急号码，以便UE在拨打呼叫时判断是否为紧急呼叫。 
扩展紧急号码可以基于UE接入的TA设置，也可以基于用户号段设置，当二者都设置时，以号段设置优先。 
功能说明 
本模块配置多组扩展紧急号码列表，以扩展紧急号码列表ID为标识。每组号码列表中包含多个号码（比如110报警号码、119火警号码）。 
在跟踪区配置[ADD TACFG]/[SET TACFG]命令中，可以为TA选择其对应的扩展紧急号码列表ID；在基于号段的紧急业务策略配置[ADD USERSEGEMERGSRPLY]/[SET USERSEGEMERGSRPLY]命令中，可以为号段选择其对应的扩展紧急号码列表ID，当号段和TA都配置扩展紧急号码列表ID时，以号段配置优先。
在注册流程中，AMF根据TA配置和号段配置，决策使用扩展紧急号码列表ID，在REGISTRATION ACCEPT消息中将扩展紧急号码列表发送给UE终端，UE基于此号码列表判断拨打的号码是否为紧急号码。 
子主题： 
##### 新增扩展紧急号码列表配置(ADD 5GEXTEMERNUMLIST) 
##### 新增扩展紧急号码列表配置(ADD 5GEXTEMERNUMLIST) 
功能说明 
该命令用于增加扩展紧急号码列表中的扩展紧急号码。当需要指示UE扩展紧急号码以便UE识别扩展紧急呼叫时，使用该命令。 
在通过本命令设置扩展紧急呼叫列表并通过[ADD TACFG]命令关联到相应的TA后，当终端从该TA成功接入后，AMF会将相应的扩展紧急号码列表发送给UE。当通过用户号段配置关联扩展紧急呼叫号码列表时，系统优先使用用户号段关联的扩展紧急号码下发给UE。
注意事项 
 
当紧急号码长度较大时，AMF会减少实际携带的号码数量。由于号码长度不同，而协议中携带的数据大小有限，因此并不能保证10个号码都能携带给终端。一般情况下足够使用，10个4位数的紧急号码没有问题。 
 
在创建或修改TA时，在ADD TACFG命令或者SET TACFG命令中，可以设置该TA关联使用的紧急号码列表，其中参数extEmergNumListID即该TA使用的扩展紧急号码列表ID。当需要开启基于用户号段下发不同扩展紧急号码功能时，使用命令ADD USERSEGEMERGSRPLY或者SET USERSEGEMERGSRPLY可以设置该号段关联使用的扩展紧急号码列表，其中参数extemergnumlistid即该号段使用的扩展紧急号码列表ID；使用命令SET EMERGSRVPLY可以设置缺省号段关联使用的扩展紧急号码列表，其中参数extemergnumlistid即缺省号段使用的扩展紧急号码列表ID。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 必选参数类型: 数字参数范围: 1-50默认值: 1|参数作用：不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。修改影响：此参数是关键参数，不可修改。数据来源：本端规划。默认值：无。配置原则：无。
number|紧急号码|参数可选性: 必选参数类型: 字符串参数范围: 1-20|参数作用：该参数用于配置紧急呼叫对应的紧急号码，例如：110、119、120。修改影响：此参数是关键参数，不可修改，如需修改，请先删除该紧急号码，再新增。数据来源：本端规划。默认值：无。配置原则：一个扩展紧急号码列表ID最多可以配置20个紧急号码。
urnType|URN类型|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于设置紧急业务URN类型，比如“urn:service:sos.ambulance”，“urn:service:sos”表示业务类型是紧急业务，“ambulance”表示子业务类型是救护子业务，AMF会将子业务类型发送给UE。紧急业务前缀“urn:service:sos”可以输入，也可以不输入。如果输入，AMF会将其剥离，只携带紧急业务子类型发送给UE。如果不输入，AMF认为输入的只是子业务类型，直接发送给UE。如果配置为空，或者配置为“urn:service:sos”，则表示没有子业务类型，AMF指示UE无子业务类型，使用修改命令修改时，输入“N/A”表示修改为空。3GPP TS 24.229定义了如下紧急业务URN类型：urn:service:sosurn:service:sos.ambulanceurn:service:sos.policeurn:service:sos.fireurn:service:sos.marineurn:service:sos.mountainurn:service:sos.ecall.manualurn:service:sos.ecall.automaticRFC5301定义了如下紧急业务URN类型：urn:service:sosurn:service:sos.ambulanceurn:service:sos.animal-controlurn:service:sos.fireurn:service:sos.gasurn:service:sos.marineurn:service:sos.mountainurn:service:sos.physicianurn:service:sos.poisonurn:service:sos.police修改影响：修改该参数，可以修改对应紧急号码的类别。数据来源：本端规划。默认值：无。配置原则：配置URN类型时需遵循以下原则：1、只可以输入字符“:”、“.”、“-”、“a-z”、“A-Z”、“0-9”；2、“:”、“.”、“-”后不能接着出现“:”、“.”、“-”；3、“:”、“.”、“-”不能出现在开头和结尾；4、如果以“urn:service:sos”（大小写不敏感）开头，允许配置如下两种场景，其它都不允许输入。a：整个输入就是“urn:service:sos”；b：“urn:service:sos”后面还有输入，则至少再出现两个字符，第一个必须是“.”，“.”后面必须跟着“A-Z”、“a-z”、“0-9”中的一个，不允许跟着“-”；5、子业务类型中不能出现“:”，具体控制是：a：如果以“urn:service:sos”（大小写不敏感）开头，“urn:service:sos”后面的所有输入不能出现“:”；b：如果不以“urn:service:sos”开头，则输入中不能出现“:”。6、增加命令输入为空时，表示该字段配置为空。7、修改命令输入“N/A”时表示该字段修改为空。
eenlv|扩展紧急号码使用范围指示|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: VALIDINCOUNTRY|参数作用：该参数用于指示扩展紧急号码的使用范围。取值含义：0：在PLMN所属的国家有效。1：仅在归属的PLMN内有效。修改影响：修改该参数，可以修改对应紧急号码的使用范围。数据来源：本端规划。默认值：0。配置原则：一个listID下的eenlv字段配置应一致。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|该参数用于配置紧急呼叫对应的紧急号码，例如：110、119、120。
urnType|URN类型|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置紧急业务URN类型，比如“urn:service:sos.ambulance”，“urn:service:sos”表示业务类型是紧急业务，“ambulance”表示子业务类型是救护子业务，AMF会将子业务类型发送给UE。
eenlv|扩展紧急号码使用范围指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: VALIDINCOUNTRY|该参数用于指示扩展紧急号码的使用范围。取值含义：0：在PLMN所属的国家有效1：仅在归属的PLMN内有效
命令举例 
`
新增扩展紧急号码列表ID为1、号码为110，URN类型为"报警"、扩展紧急号码使用范围指示为"PLMN所属国家内有效"的扩展紧急号码。
ADD 5GEXTEMERNUMLIST:LISTID=1,NUMBER="110",URNTYPE="urn:service:sos.police",EENLV="VALIDINCOUNTRY"
` 
##### 修改扩展紧急号码列表配置(SET 5GEXTEMERNUMLIST) 
##### 修改扩展紧急号码列表配置(SET 5GEXTEMERNUMLIST) 
功能说明 
该命令用于修改扩展紧急号码列表中的扩展紧急号码。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 必选参数类型: 数字参数范围: 1-50默认值: 1|参数作用：不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。修改影响：此参数是关键参数，不可修改。数据来源：本端规划。默认值：无。配置原则：无。
number|紧急号码|参数可选性: 必选参数类型: 字符串参数范围: 1-20|参数作用：该参数用于配置紧急呼叫对应的紧急号码，例如：110、119、120。修改影响：此参数是关键参数，不可修改，如需修改，请先删除该紧急号码，再新增。数据来源：本端规划。默认值：无。配置原则：一个扩展紧急号码列表ID最多可以配置20个紧急号码。
urnType|URN类型|参数可选性: 任选参数类型: 字符串参数范围: 0-100|参数作用：该参数用于设置紧急业务URN类型，比如“urn:service:sos.ambulance”，“urn:service:sos”表示业务类型是紧急业务，“ambulance”表示子业务类型是救护子业务，AMF会将子业务类型发送给UE。紧急业务前缀“urn:service:sos”可以输入，也可以不输入。如果输入，AMF会将其剥离，只携带紧急业务子类型发送给UE。如果不输入，AMF认为输入的只是子业务类型，直接发送给UE。如果配置为空，或者配置为“urn:service:sos”，则表示没有子业务类型，AMF指示UE无子业务类型，使用修改命令修改时，输入“N/A”表示修改为空。3GPP TS 24.229定义了如下紧急业务URN类型：urn:service:sosurn:service:sos.ambulanceurn:service:sos.policeurn:service:sos.fireurn:service:sos.marineurn:service:sos.mountainurn:service:sos.ecall.manualurn:service:sos.ecall.automaticRFC5301定义了如下紧急业务URN类型：urn:service:sosurn:service:sos.ambulanceurn:service:sos.animal-controlurn:service:sos.fireurn:service:sos.gasurn:service:sos.marineurn:service:sos.mountainurn:service:sos.physicianurn:service:sos.poisonurn:service:sos.police修改影响：修改该参数，可以修改对应紧急号码的类别。数据来源：本端规划。默认值：无。配置原则：配置URN类型时需遵循以下原则：1、只可以输入字符“:”、“.”、“-”、“a-z”、“A-Z”、“0-9”；2、“:”、“.”、“-”后不能接着出现“:”、“.”、“-”；3、“:”、“.”、“-”不能出现在开头和结尾；4、如果以“urn:service:sos”（大小写不敏感）开头，允许配置如下两种场景，其它都不允许输入。a：整个输入就是“urn:service:sos”；b：“urn:service:sos”后面还有输入，则至少再出现两个字符，第一个必须是“.”，“.”后面必须跟着“A-Z”、“a-z”、“0-9”中的一个，不允许跟着“-”；5、子业务类型中不能出现“:”，具体控制是：a：如果以“urn:service:sos”（大小写不敏感）开头，“urn:service:sos”后面的所有输入不能出现“:”；b：如果不以“urn:service:sos”开头，则输入中不能出现“:”。6、增加命令输入为空时，表示该字段配置为空。7、修改命令输入“N/A”时表示该字段修改为空。
eenlv|扩展紧急号码使用范围指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: VALIDINCOUNTRY|参数作用：该参数用于指示扩展紧急号码的使用范围。取值含义：0：在PLMN所属的国家有效。1：仅在归属的PLMN内有效。修改影响：修改该参数，可以修改对应紧急号码的使用范围。数据来源：本端规划。默认值：0。配置原则：一个listID下的eenlv字段配置应一致。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|该参数用于配置紧急呼叫对应的紧急号码，例如：110、119、120。
urnType|URN类型|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置紧急业务URN类型，比如“urn:service:sos.ambulance”，“urn:service:sos”表示业务类型是紧急业务，“ambulance”表示子业务类型是救护子业务，AMF会将子业务类型发送给UE。
eenlv|扩展紧急号码使用范围指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: VALIDINCOUNTRY|该参数用于指示扩展紧急号码的使用范围。取值含义：0：在PLMN所属的国家有效1：仅在归属的PLMN内有效
命令举例 
`
将扩展紧急号码ID为1并且号码为110的扩展紧急号码的URN类型修改为"报警"、扩展紧急号码使用范围指示为"仅PLMN内有效"。
SET 5GEXTEMERNUMLIST:LISTID=1,NUMBER="110",URNTYPE="urn:service:sos.alarm",EENLV="VALIDINPLMN"
` 
##### 删除扩展紧急号码列表配置(DEL 5GEXTEMERNUMLIST) 
##### 删除扩展紧急号码列表配置(DEL 5GEXTEMERNUMLIST) 
功能说明 
该命令用于从扩展紧急号码列表中删除一个扩展紧急号码。 
删除该号码之后，UE不再将此号码作为紧急呼叫使用，只会按照普通电话的要求建立连接。 
注意事项 
 
当删除命令中仅包含紧急号码的列表ID时，可以删除该紧急号码ID关联全部的紧急号码。 
 
在删除扩展紧急号码列表ID下全部的扩展紧急号码前，需要先删除ADD TACFG、SET TACFG、ADD USERSEGEMERGSRPLY、SET USERSEGEMERGSRPLY和SET EMERGSRVPLY命令中所关联的该扩展紧急号码列表ID。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 必选参数类型: 数字参数范围: 1-50默认值: 1|参数作用：不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。修改影响：此参数是关键参数，不可修改。数据来源：本端规划。默认值：无。配置原则：无。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|参数作用：该参数用于配置紧急呼叫对应的紧急号码，例如：110、119、120。修改影响：此参数是关键参数，不可修改，如需修改，请先删除该紧急号码，再新增。数据来源：本端规划。默认值：无。配置原则：一个扩展紧急号码列表ID最多可以配置20个紧急号码。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|该参数用于配置紧急呼叫对应的紧急号码，例如：110、119、120。
urnType|URN类型|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置紧急业务URN类型，比如“urn:service:sos.ambulance”，“urn:service:sos”表示业务类型是紧急业务，“ambulance”表示子业务类型是救护子业务，AMF会将子业务类型发送给UE。
eenlv|扩展紧急号码使用范围指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: VALIDINCOUNTRY|该参数用于指示扩展紧急号码的使用范围。取值含义：0：在PLMN所属的国家有效1：仅在归属的PLMN内有效
命令举例 
`
删除扩展紧急号码ID为1的所有扩展紧急号码。
DEL 5GEXTEMERNUMLIST:LISTID=1
` 
##### 查询扩展紧急号码列表配置(SHOW 5GEXTEMERNUMLIST) 
##### 查询扩展紧急号码列表配置(SHOW 5GEXTEMERNUMLIST) 
功能说明 
该命令用于显示扩展紧急号码列表的扩展紧急号码及其类型。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|参数作用：不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。修改影响：此参数是关键参数，不可修改。数据来源：本端规划。默认值：无。配置原则：无。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|参数作用：该参数用于配置紧急呼叫对应的紧急号码，例如：110、119、120。修改影响：此参数是关键参数，不可修改，如需修改，请先删除该紧急号码，再新增。数据来源：本端规划。默认值：无。配置原则：一个扩展紧急号码列表ID最多可以配置20个紧急号码。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
listID|紧急号码列表ID|参数可选性: 任选参数类型: 数字参数范围: 1-50默认值: 1|不同地区的紧急号码数量、类型或者号码可能不完全一样，紧急号码列表用于区分不同地区携带的紧急号码，可以把一个地区的紧急号码归纳到一个紧急号码列表中。例如存在一个接入网跨越地区A和地区B，根据这两地的紧急号码定义不同，A处接入的TA则使用紧急号码列表1，可以含有110、119、120等号码；而在B处接入的TA则使用紧急号码列表2，可以含有999等号码。。
number|紧急号码|参数可选性: 任选参数类型: 字符串参数范围: 1-20|该参数用于配置紧急呼叫对应的紧急号码，例如：110、119、120。
urnType|URN类型|参数可选性: 任选参数类型: 字符串参数范围: 0-100|该参数用于设置紧急业务URN类型，比如“urn:service:sos.ambulance”，“urn:service:sos”表示业务类型是紧急业务，“ambulance”表示子业务类型是救护子业务，AMF会将子业务类型发送给UE。
eenlv|扩展紧急号码使用范围指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: VALIDINCOUNTRY|该参数用于指示扩展紧急号码的使用范围。取值含义：0：在PLMN所属的国家有效1：仅在归属的PLMN内有效
命令举例 
`
查询紧急号码ID为1关联的所有紧急号码
SHOW 5GEXTEMERNUMLIST:LISTID=1
(No.11) : SHOW 5GEXTEMERNUMLIST:
-----------------Namf_Communication_0----------------
Emergency Number List ID Emergency Number URN Type EENLV
1
120
urn:service:sos.ambulance
Valid in the country of the PLMN
记录数：1
执行成功耗时: 0.138 秒
` 
### 紧急业务回落配置 
### 紧急业务回落配置 
背景知识 
紧急业务回落（Fallback）能力是TA（Tracking Area，跟踪区域）支持紧急业务回落的能力，不同的TA对紧急业务回落能力的支持不一样。 
TAI：跟踪区域标识（Tracking Area Identity），由国家码（MCC）、移动网络码 （MNC）和跟踪区编号（TAC）组成，由运营商统一规划。每个TAI唯一对应一个TA。 
AMF在配置自己所管理的TA时，需要配置每个TA对应的紧急业务回落能力。由于AMF还支持UE从本AMF没有管理的TA上接入，此时AMF还需要配置一个全局默认的紧急业务回落能力。当UE从本AMF没有管理的TA接入时，使用这个默认的全局紧急业务回落能力。 
功能说明 
本功能用于设置AM默认的全局配置紧急回落策略，比如紧急号码列表、扩展紧急号码列表、是否支持紧急回落以及紧急回落能力。 
该功能适用于，当终端用户从非本AMF管理的TA接入的场景，决策是否启用紧急业务回落、紧急业务能力、紧急号码列表以及扩展紧急号码。 
子主题： 
#### 设置紧急业务回落策略(SET EMERGSRVFALLBACKPLY) 
#### 设置紧急业务回落策略(SET EMERGSRVFALLBACKPLY) 
功能说明 
本命令用于设置AMF全局配置紧急回落策略，比如紧急号码列表、扩展紧急号码列表、是否支持紧急回落。 
注意事项 
 
当不需要配置紧急号码列表或者扩展紧急号码时，对应的紧急号码列表ID或扩展紧急号码列表ID配置为0。  
 
当需要配置紧急号码列表或者扩展紧急号码时，需要首先通过ADD 5GEMERNUMLIST命令配置紧急号码列表，或者通过ADD 5GEXTEMERNUMLIST命令配置扩展紧急号码。  
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
sprtEmergFallback|支持紧急业务回落|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置本AMF是否支持紧急业务回落，默认不支持。
命令举例 
`
设置AMF紧急呼叫策略：支持紧急呼叫。
SET EMERGSRVFALLBACKPLY:SPRTEMERGFALLBACK="YES"
(No.2) : SET EMERGSRVFALLBACKPLY:SPRTEMERGFALLBACK="YES"
-----------------Namf_Communication_0----------------
执行成功耗时: 0.532 秒
` 
#### 查询紧急业务回落策略(SHOW EMERGSRVFALLBACKPLY) 
#### 查询紧急业务回落策略(SHOW EMERGSRVFALLBACKPLY) 
功能说明 
本命令用于查询AMF全局配置紧急回落策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
sprtEmergFallback|支持紧急业务回落|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置本AMF是否支持紧急业务回落，默认不支持。
命令举例 
`
查询AMF紧急呼叫策略。
SHOW EMERGSRVFALLBACKPLY:
(No.1) : SHOW EMERGSRVFALLBACKPLY:
-----------------Namf_Communication_0_A----------------
支持紧急回落
是
记录数：1
耗时: 0.22 秒
` 
### 紧急业务SNSSAI配置 
### 紧急业务SNSSAI配置 
背景知识 
终端用户在进行紧急业务时，AMF需要忽略终端用户携带的S-NSSAI。终端用户需要使用AMF专门为紧急业务配置的一个专用S-NSSAI。 
S-NSSAI（Single Network Slice Selection Assistance Information，单个网络切片选择辅助信息） 可用于标识网络切片，由SST（Slice/Service Type，切片/服务类型）和SD（Slice Differentiator，切片区分信息）组成。 
 
SST（Service/Slice Type）：业务或切片类型，如eMBB（Enhanced Mobile Broadband，增强移动宽带）、mMTC（Massive Machine Type Communication，海量机器类通信）、uRLLC（Ultra Reliable Low Latency Communication，超高可靠超低时延通信），后续可以继续扩展。 
 
SD（Slice Differentiator，切片区分信息）：其它可以区分切片的信息，比如区域信息，租户信息等。 
 
功能说明 
本功能用于配置紧急业务的专用S-NSSAI。 
子主题： 
#### 设置紧急业务SNSSAI(SET EMERGSRVSNSSAI) 
#### 设置紧急业务SNSSAI(SET EMERGSRVSNSSAI) 
功能说明 
本命令用于配置紧急业务的S-NSSAI。 
当终端用户激活紧急PDU会话时，AMF会忽略激活请求消息中，终端携带的S-NSSAI，直接使用本命令的S-NSSAI作为终端用户的S-NSSAI。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
emgSst|紧急业务SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: eMBB|本参数用于设置紧急业务S-NSSAI中的SST（Slice/Service Type，切片/服务类型）的编号，默认为eMBB。其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
emgSd|紧急业务SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置紧急业务S-NSSAI中的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。，默认为"NULL"。
命令举例 
`
设置紧急业务的SNSSAI，SST为"eMBB"，SD为“123456”
SET EMERGSRVSNSSAI:EMGSST="eMBB",EMGSD="123456"
` 
#### 查询紧急业务SNSSAI(SHOW EMERGSRVSNSSAI) 
#### 查询紧急业务SNSSAI(SHOW EMERGSRVSNSSAI) 
功能说明 
本命令用于查询紧急业务的S-NSSAI。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
emgSst|紧急业务SST|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: eMBB|本参数用于设置紧急业务S-NSSAI中的SST（Slice/Service Type，切片/服务类型）的编号，默认为eMBB。其中编号0-127为标准SST，编号128-255为运营商自定义的SST。目前协议明确的标准SST有三种。1：eMBB：提供高带宽、大数据量的服务。2：uRLLC：提供超高可靠低时延服务。3：mIoT：提供海量的连接数，但是数据量比较小，且对时延要求不高。具体解释参见协议23501的"5.15.2.2 Standardised SST values"。
emgSd|紧急业务SD|参数可选性: 任选参数类型: 字符串参数范围: 4-6默认值: NULL|本参数用于设置紧急业务S-NSSAI中的SD（Slice Differentiator，切片区分信息）。SD用于区分同一种SST之内不同的S-NSSAI。，默认为"NULL"。
命令举例 
`
查询紧急业务的SNSSAI。
SHOW EMERGSRVSNSSAI
(No.4) : SHOW EMERGSRVSNSSAI:
-----------------Namf_Communication_0----------------
紧急业务SST     紧急业务SD
1                     NULL
记录数：1
执行成功耗时: 0.32 秒
` 
# SMS over NAS配置 
# SMS over NAS配置 
背景知识 
AMF支持SMS over NAS，即由NAS消息传递短消息业务。 
AMF支持以下功能： 
 
短消息注册 
 
短消息起呼，包括UE空闲态起呼和连接态起呼 
 
短消息终呼，包括UE空闲态终呼和连接态终呼 
 
功能说明 
本功能用于配置SMS over NAS策略。 
子主题： 
## SMS over NAS策略配置 
## SMS over NAS策略配置 
背景知识 
SMS Over NAS功能是5GC系统的可选功能。 
对于一个终端而言，是否支持SMS Over NAS功能需要考虑终端能力、签约以及AMF能力。通过本地配置的方式，AMF可以开启或者关闭是否支持SMS Over NAS能力，从而控制5GC是否提供SMS Over NAS能力。 
功能说明 
本功能用于设置SMS业务相关的配置。 
 
设置AMF是否支持SMS over NAS功能。 
 
设置当终端去注册时，AMF是否通知SMSF。 
 
子主题： 
### 修改 SMS策略配置(SET SMSPOLICY) 
### 修改 SMS策略配置(SET SMSPOLICY) 
功能说明 
该命令用于修改SMS策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supportSmsOverNas|AMF是否支持SMS over NAS|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOT_SUPPORT|该参数用于设置AMF是否开启SMS over NAS功能。
supsmscol|AMF是否支持短信业务管制功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOT_SUPPORT|该参数用于设置短信管控开关，当“AMF支持5G通信管制功能”license支持后，通过此开关开启短信管控。
mtsmsctlpolicy|MT短信管控策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: DISCARD|该参数用于设置MT短消息在管控时的策略。
key|加密密钥|参数可选性: 任选参数类型: 字符串参数范围: 0-32|加密密钥， CCMS和核心网约定的加密密钥，通过此密钥和加密向量进行解码白名单。
命令举例 
`
打开AMF支持SMS Over NAS功能开关。
SET SMSPOLICY:SUPPORTSMSOVERNAS="SUPPORT"
` 
### 查询 SMS策略配置(SHOW SMSPOLICY) 
### 查询 SMS策略配置(SHOW SMSPOLICY) 
功能说明 
该命令用于查询SMS策略配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supportSmsOverNas|AMF是否支持SMS over NAS|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOT_SUPPORT|该参数用于设置AMF是否开启SMS over NAS功能。
supsmscol|AMF是否支持短信业务管制功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOT_SUPPORT|该参数用于设置短信管控开关，当“AMF支持5G通信管制功能”license支持后，通过此开关开启短信管控。
mtsmsctlpolicy|MT短信管控策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: DISCARD|该参数用于设置MT短消息在管控时的策略。
key|加密密钥|参数可选性: 任选参数类型: 字符串参数范围: 0-32|加密密钥， CCMS和核心网约定的加密密钥，通过此密钥和加密向量进行解码白名单。
命令举例 
`
查询SMS策略配置。
SHOW SMSPOLICY
(No.2) : SHOW SMSPOLICY:
-----------------Namf_Communication_0----------------
操作维护       AMF是否支持SMS over NAS AMF是否支持短信业务管制功能 MT短信管控策略 加密密钥 
-------------------------------------------------------------------------------------------
修改           AMF不支持SMS over NAS   AMF不支持短信业务管制功能   丢弃MT短信              
-------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-04-20 11:58:47 耗时: 0.228 秒
` 
# LADN配置 
# LADN配置 
背景知识 
LADN（Local Area Data Network，局域数据网）是由服务PLMN提供的一项功能。LADN服务区域是一组跟踪区， 用户通过PDU会话接入数据网络，仅在特定的LADN服务区中可用，详细参见协议3GPP TS 23.501第5.6.5节Support for Local Area Data Network。 
功能说明 
AMF在终端用户注册时，告知终端用户所在的LADN区域。LADN配置提供LADN ID和LADN跟踪区标识列表配置。 
子主题： 
## LADN ID配置 
## LADN ID配置 
背景知识 
用户在注册（Registration）过程或者UE配置更新过程中，AMF向UE提供LADN信息(即LADN服务区域和LADN DNN)。AMF下发的LADN列表，需要依据UE注册请求消息中携带的LADN指示(参见协议3GPP TS 24.501第9.11.3.29节 LADN indication)、AMF本地配置(经由OAM)以及用户的DNN签约信息几方面来确定： 
 
UE注册请求既没有提供LADN DNN也没有提供请求LADN信息的指示：则LADN信息的DNN列表，是用户签约DNN中的LADN DNN与AMF配置的LADN DNN的交集；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 
 
UE注册请求提供了请求LADN信息的指示但未提供LADN DNN：此时LADN信息的DNN列表，还需要依据UE的DNN签约信息来确定：如果UE的签约了通配DNN(wildcard *)并且通配DNN为LADN DNN，LADN信息中的DNN列表，是AMF配置的 LADN DNN；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。如果UE没有签约通配DNN或者签约了通配DNN但非LADN DNN，LADN信息的LADN DNN列表，是签约DNN中的LADN DNN与AMF配置的LADN DNN的交集；每个LADN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 
 
UE注册请求提供了请求LADN信息的指示及LADN DNN：此时LADN信息的DNN列表，还需要依据UE的DNN签约信息来确定：如果UE的签约了通配DNN并且通配DNN为LADN DNN，LADN信息中的DNN列表，是ladn Indication 的LADN DNN与AMF配置的LADN DNN的交集；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。如果UE没有签约通配DNN或者签约了通配DNN但非LADN DNN，LADN信息的LADN DNN列表，是ladn Indication指示的、签约DNN中的LADN DNN及AMF配置的LADN DNN三者的交集；每个LADN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 
 
用户在注册（Registration）过程中，AMF需要按前述规则确定LADN Information，将最多不超过8个Ladn Information通过注册接受消息中带给UE。另外，当网络侧UE的LADN DNN信息改变时，AMF也可以通过UE配置更新过程(即在configuration update command消息中携带新的LADN Information给UE)更新LADN信息。 
功能说明 
本功能用于设置AMF本地配置的LADN Information。 
当AMF支持LADN功能时，需要涉及到此功能的配置。 
子主题： 
### 新增AmfLadn配置(ADD AMFLADN) 
### 新增AmfLadn配置(ADD AMFLADN) 
功能说明 
该命令用于增加LADN配置信息。 
注意事项 
本命令配置的数据，用于后续在[ADD AMFLADN TAIDLIST]命令中使用。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
ladnDnn|LADNDNN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|该参数用于配置LADN信息的LADN DNN，AMF内唯一。LADNDNN 只支持输入小写。
命令举例 
`
新增标识为1的LADN配置，LADN DNN为"zte.com"。
ADD AMFLADN:LADNID=1,LADNDNN="zte.com"
` 
### 修改AmfLadn配置(SET AMFLADN) 
### 修改AmfLadn配置(SET AMFLADN) 
功能说明 
该命令用于修改已经配置成功的LADN信息。 
注意事项 
当LADN DNN发生变更，需要使用本命令对已有LADN进行修改。由于LADN ID通常已经被关联使用，不建议用此命令直接修改，而是应该先通过[DEL AMFLADN TAIDLIST]命令和[DEL AMFLADN]命令删除相关配置，再通过[ADD AMFLADN]命令重新增加的方式来修改。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
ladnDnn|LADNDNN|参数可选性: 必选参数类型: 字符串参数范围: 1-100|该参数用于配置LADN信息的LADN DNN，AMF内唯一。LADNDNN 只支持输入小写。
命令举例 
`
修改标识为1的LADN配置，LADN DNN由"zte.com"修改为"zte.com.cn"。
SET AMFLADN:LADNID=1,LADNDNN="zte.com.cn"
` 
### 删除AmfLadn配置(DEL AMFLADN) 
### 删除AmfLadn配置(DEL AMFLADN) 
功能说明 
该命令用于删除已经配置成功的LADN信息。 
注意事项 
由于LADN ID通常已经被关联使用，不建议用此命令直接修改，而是应该先通过[DEL AMFLADN TAIDLIST]命令和[DEL AMFLADN]命令删除相关配置，再使用本命令。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
命令举例 
`
删除标识为1的LADN配置。
DEL AMFLADN:LADNID=1
` 
### 查询AmfLadn配置(SHOW AMFLADN) 
### 查询AmfLadn配置(SHOW AMFLADN) 
功能说明 
该命令用于查询已经配置的LADN信息。可以直接查询所有LADN信息配置，也可以通过键入LadnId来查询某个特定LADN信息的配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
ladnDnn|LADNDNN|参数可选性: 任选参数类型: 字符串参数范围: 1-100|该参数用于配置LADN信息的LADN DNN，AMF内唯一。LADNDNN 只支持输入小写
命令举例 
`
查询所有的LADN配置。
SHOW AMFLADN
(No.1) : SHOW AMFLADN:
-----------------Namf_Communication_0----------------
局域数据网标识    LADNDNN
1                       1
记录数：1
执行成功耗时: 0.12 秒
` 
## LADN跟踪区标识列表配置 
## LADN跟踪区标识列表配置 
背景知识 
用户在注册（Registration）过程或者UE配置更新过程中，AMF向UE提供LADN信息(即LADN服务区域和LADN DNN)。AMF下发的LADN列表，需要依据UE注册请求消息中携带的LADN指示(参见协议24501第9.11.3.29节 LADN indication)、AMF本地配置(经由OAM)以及用户的DNN签约信息几方面来确定： 
 
UE注册请求既没有提供LADN DNN也没有提供请求LADN信息的指示：则LADN信息的DNN列表，是用户签约DNN中的LADN DNN与AMF配置的LADN DNN的交集；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 
 
UE注册请求提供了请求LADN信息的指示但未提供LADN DNN：此时LADN信息的DNN列表，还需要依据UE的DNN签约信息来确定：如果UE的签约了通配DNN(wildcard *)并且通配DNN为LADN DNN，LADN信息中的DNN列表，是AMF配置的 LADN DNN；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。如果UE没有签约通配DNN或者签约了通配DNN但非LADN DNN，LADN信息的LADN DNN列表，是签约DNN中的LADN DNN与AMF配置的LADN DNN的交集；每个LADN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 
 
UE注册请求提供了请求LADN信息的指示及LADN DNN：此时LADN信息的DNN列表，还需要依据UE的DNN签约信息来确定：如果UE的签约了通配DNN并且通配DNN为LADN DNN，LADN信息中的DNN列表，是ladn Indication 的LADN DNN与AMF配置的LADN DNN的交集；每个LADN DNN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。如果UE没有签约通配DNN或者签约了通配DNN但非LADN DNN，LADN信息的LADN DNN列表，是ladn Indication指示的、签约DNN中的LADN DNN及AMF配置的LADN DNN三者的交集；每个LADN对应的服务区域，是AMF配置的LADN DNN跟踪区列表与AMF为UE分配的当前注册区域的交集，如果没有交集，对应配置的DNN也需要从前述LADN DNN列表中剔除。 
 
用户在注册（Registration）过程中，AMF需要按前述规则确定LADN Information，将最多不超过8个Ladn Information通过注册接受消息中带给UE。另外，当网络侧UE的LADN DNN信息改变时，AMF也可以通过UE配置更新过程(即在configuration update command消息中携带新的LADN Information给UE)更新LADN信息。 
功能说明 
该功能用于为已经配置好的某个LADN ID增加关联的跟踪区（TA）列表。 
子主题： 
### 增加AMF LADN跟踪区标识列表(ADD AMFLADN TAIDLIST) 
### 增加AMF LADN跟踪区标识列表(ADD AMFLADN TAIDLIST) 
功能说明 
该命令用于为已经配置成功的LADN ID增加对应服务区域，即跟踪区列表。每个LADN ID最多可配置16个跟踪区标识。 
注意事项 
由于跟踪区标识引用自TA配置，因此，配置本命令前，需要先通过[ADD TACFG]命令，配置跟踪区。
配置本命令前，还需要先通过[ADD AMFLADN]命令，配置LADN ID。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
taId|LADN跟踪区标识|参数可选性: 必选参数类型: 数字参数范围: 1-16777215|该参数用于配置LADN对应的TA标识，每个LADN最多配置16个TA标识。该参数的取值是通过SHOW TACFG命令查询获取的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
命令举例 
`
为已经成功配置的标识为1的LADN增加一个标识为2的TA配置，该TA的MCC/MNC/TAC/REGAREAID/TANAM/TAVOICEPOLICYTEMPID信息均引用自"TA 配置"。
ADD AMFLADN TAIDLIST:LADNID=1,TAID=2
` 
### 删除AMF LADN跟踪区标识列表(DEL AMFLADN TAIDLIST) 
### 删除AMF LADN跟踪区标识列表(DEL AMFLADN TAIDLIST) 
功能说明 
该命令用于删除某个LADN ID下已经配置的跟踪区标识。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
taId|LADN跟踪区标识|参数可选性: 必选参数类型: 数字参数范围: 1-16777215|该参数用于配置LADN对应的TA标识，每个LADN最多配置16个TA标识。该参数的取值是通过SHOW TACFG命令查询获取的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
命令举例 
`
删除标识为1的LADN下已经成功增加的标识为2的TA配置。
DEL AMFLADN TAIDLIST:LADNID=1,TAID=2
` 
### 查询AMF LADN跟踪区标识列表(SHOW AMFLADN TAIDLIST) 
### 查询AMF LADN跟踪区标识列表(SHOW AMFLADN TAIDLIST) 
功能说明 
该命令用于查询已经配置的跟踪区标识。可以直接查询所有LADN ID对应的跟踪区标识列表配置，也可以通过键入LadnId查询特定LADN ID对应的跟踪区标识列表配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ladnId|局域数据网标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于配置AMF LADN信息标识，AMF内唯一。
taId|LADN跟踪区标识|参数可选性: 任选参数类型: 数字参数范围: 1-16777215|该参数用于配置LADN对应的TA标识，每个LADN最多配置16个TA标识。该参数的取值是通过SHOW TACFG命令查询获取的。
命令举例 
`
查询AMF上所有LADN。
SHOW AMFLADN TAIDLIST:
(No.1) : SHOW AMFLADN TAIDLIST:
-----------------Namf_Communication_0----------------
局域数据网标识    LADN跟踪区标识
1                       1000
记录数：1
执行成功耗时: 0.299 秒
` 
# 漫游配置 
# 漫游配置 
背景知识 
漫游，指移动终端用户移动到归属运营商网络以外的国家或地区仍能继续使用移动终端业务。 
根据移动终端的漫游业务接入策略，按业务是否需要迂回到归属地，可以分为两种漫游模式：Home routed（归属地）漫游接入、Local breakout（漫游地）漫游接入。 
 
HR漫游接入：Home routed（归属地）漫游接入
指漫游用户经由拜访地网络连接到归属地网络接入， 获取归属网络提供的业务。 
 
LBO漫游接入：Local breakout（漫游地）漫游接入
指漫游用户通过拜访地网络接入获取相应业务，业务的提供者可以是归属网络，也可以是拜访网络。 
 
功能说明 
漫游配置包括漫游全局策略配置、基于SUPI号段的漫游策略配置、互操作S-NSSAI配置等。 
子主题： 
## 漫游策略配置 
## 漫游策略配置 
背景知识 
支持终端漫游是移动运营商的基本需求之一，移动通讯技术演进到第5代（5G）后，如何提供漫游成为运营商需要解决的重要问题之一。 
功能说明 
本功能用于设置漫游策略，包括SUPI号段漫游策略，home SMF数量， 默认LBO（Local breakout）策略，默认home SMF查询方式。 
子主题： 
### 设置漫游策略配置(SET ROAMINGPOLICY) 
### 设置漫游策略配置(SET ROAMINGPOLICY) 
功能说明 
本命令用于设置或修改漫游策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiRoamingPolicy|SUPI号段漫游策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|该参数用于设置根据终端的SUPI（Subscriber Permanent Identifier，用户永久标识）号段配置的漫游策略。若设置为支持，则AMF会根据终端的SUPI来匹配通过ADD SUPIROAMINGPOLICY命令配置的漫游策略。
additionalHSMFNum|额外的hSMF数量|参数可选性: 任选参数类型: 数字参数范围: 0-10默认值: 2|该参数用于设置额外的home SMF数量。当终端的漫游方式为HR（Home Routed）时，AMF发送给SMF的PDU创建请求消息中，需要携带本参数配置的home SMF的数量。
lboPolicy|默认LBO策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIBE|当AMF基于终端的SUPI号段匹配LBO（Local breakout）策略失败，则使用此参数配置的默认LBO策略。配置为“限制”，表示终端不支持LBO（Local Breakout）漫游。配置为“签约”，表示根据终端的签约数据来决策终端的漫游方式。
hSMFQueryMode|默认hSMF查询方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOHNSSFRETURNNRF|该参数用于设置默认hSMF查询方式。若不使用home NSSF返回的NRF，则AMF采用本地配置的数据来获取NRF。
命令举例 
`
设置漫游策略策略。
SET ROAMINGPOLICY:SUPIROAMINGPOLICY="SUPPORT",ADDITIONALHSMFNUM=1,LBOPOLICY="SUBSCRIBE",HSMFQUERYMODE="HNSSFRETURNNRF"
` 
### 查询漫游策略配置(SHOW ROAMINGPOLICY) 
### 查询漫游策略配置(SHOW ROAMINGPOLICY) 
功能说明 
本命令用于查询漫游策略。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiRoamingPolicy|SUPI号段漫游策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUPPORT|该参数用于设置根据终端的SUPI（Subscriber Permanent Identifier，用户永久标识）号段配置的漫游策略。若设置为支持，则AMF会根据终端的SUPI来匹配通过ADD SUPIROAMINGPOLICY命令配置的漫游策略。
additionalHSMFNum|额外的hSMF数量|参数可选性: 任选参数类型: 数字参数范围: 0-10默认值: 2|该参数用于设置额外的home SMF数量。当终端的漫游方式为HR（Home Routed）时，AMF发送给SMF的PDU创建请求消息中，需要携带本参数配置的home SMF的数量。
lboPolicy|默认LBO策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIBE|当AMF基于终端的SUPI号段匹配LBO（Local breakout）策略失败，则使用此参数配置的默认LBO策略。配置为“限制”，表示终端不支持LBO（Local Breakout）漫游。配置为“签约”，表示根据终端的签约数据来决策终端的漫游方式。
hSMFQueryMode|默认hSMF查询方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOHNSSFRETURNNRF|该参数用于设置默认hSMF查询方式。若不使用home NSSF返回的NRF，则AMF采用本地配置的数据来获取NRF。
命令举例 
`
查询漫游策略策略。
SHOW ROAMINGPOLICY
(No.1) : SHOW ROAMINGPOLICY:
-----------------Namf_Communication_0----------------
SUPI号段漫游策略   额外的hSMF数量   默认LBO策略    默认hSMF查询方式
支持                      3                     限制                   不需hNSSF返回NRF信息
记录数：1
执行成功耗时: 0.151 秒
` 
## 基于SUPI号段漫游策略配置 
## 基于SUPI号段漫游策略配置 
背景知识 
支持终端漫游是移动运营商的基本需求之一，移动通讯技术演进到第5代（5G）后，如何提供漫游成为运营商需要解决的重要问题之一。 
功能说明 
本功能用于配置基于SUPI号段的漫游策略，包括LBO策略和hSMF查询方式。 
在配置此命令前，必须先通过[SET ROAMINGPOLICY]命令，支持漫游功能，开启漫游策略的命令：SET ROAMINGPOLICY：SUPIROAMINGPOLICY="SUPPORT"
子主题： 
### 新增基于SUPI号段的漫游策略配置(ADD SUPIROAMINGPOLICY) 
### 新增基于SUPI号段的漫游策略配置(ADD SUPIROAMINGPOLICY) 
功能说明 
本命令用于配置基于SUPI号段的漫游策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|supi|参数可选性: 必选参数类型: 字符串参数范围: 1-16|本参数用于配置SUPI号段。
LBO|LBO|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RESTRICT|本参数用于设置LBO策略，LBO是指Local breakout（漫游地）漫游接入，指漫游用户通过拜访地PGW接入获取相应业务，业务的提供者可以是归属网络，也可以是拜访网络。限制：表示终端不允许使用LBO。签约：表示AMF需要根据终端的签约信息，来确定终端是否可以使用LBO。
hSMFQueryMode|hSMF查询方式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOHNSSFRETURNNRF|本参数用于设置home SMF的查询方式。在HR漫游方式下，AMF需要选择home SMF。HR漫游接入：Home routed（归属地）漫游接入，指漫游用户经由拜访地网络连接到归属地网络接入， 获取归属网络提供的业务。若配置为“需要hNSSF返回NRF信息”，则AMF需要到home NSSF返回的NRF上，查询获取home SMF。若配置为“不需hNSSF返回NRF信息”，则AMF需要到本地配置的NRF上，查询获取home SMF。
命令举例 
`
新增漫游配置，"4600100001"号段的LBO策略为限制，hSMF查询方式为需hNSSF返回NRF信息。
ADD SUPIROAMINGPOLICY:SUPI="4600100001",LBO="RESTRICT",hSMFQueryMode="HNSSFRETURNNRF"
` 
### 修改基于SUPI号段的漫游策略配置(MOD SUPIROAMINGPOLICY) 
### 修改基于SUPI号段的漫游策略配置(MOD SUPIROAMINGPOLICY) 
功能说明 
该命令用于修改基于SUPI号段的漫游策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|supi|参数可选性: 必选参数类型: 字符串参数范围: 1-16|本参数用于配置SUPI号段。
LBO|LBO|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RESTRICT|本参数用于设置LBO策略，LBO是指Local breakout（漫游地）漫游接入，指漫游用户通过拜访地PGW接入获取相应业务，业务的提供者可以是归属网络，也可以是拜访网络。限制：表示终端不允许使用LBO。签约：表示AMF需要根据终端的签约信息，来确定终端是否可以使用LBO。
hSMFQueryMode|hSMF查询方式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOHNSSFRETURNNRF|本参数用于设置home SMF的查询方式。在HR漫游方式下，AMF需要选择home SMF。HR漫游接入：Home routed（归属地）漫游接入，指漫游用户经由拜访地网络连接到归属地网络接入， 获取归属网络提供的业务。若配置为“需要hNSSF返回NRF信息”，则AMF需要到home NSSF返回的NRF上，查询获取home SMF。若配置为“不需hNSSF返回NRF信息”，则AMF需要到本地配置的NRF上，查询获取home SMF。
命令举例 
`
修改漫游配置，"4600100001"号段的LBO策略为签约，hSMF查询方式为需hNSSF返回NRF信息。
MOD SUPIROAMINGPOLICY:SUPI="4600100001",LBO="SUBSCRIBE",hSMFQueryMode="HNSSFRETURNNRF"
` 
### 删除基于SUPI号段的漫游策略配置(DEL SUPIROAMINGPOLICY) 
### 删除基于SUPI号段的漫游策略配置(DEL SUPIROAMINGPOLICY) 
功能说明 
该命令用于删除基于SUPI号段的漫游策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|supi|参数可选性: 必选参数类型: 字符串参数范围: 1-16|本参数用于配置SUPI号段。
命令举例 
`
删除"4600100001"号段的漫游配置。
DEL SUPIROAMINGPOLICY:SUPI="4600100001"
` 
### 查询基于SUPI号段的漫游策略配置(SHOW SUPIROAMINGPOLICY) 
### 查询基于SUPI号段的漫游策略配置(SHOW SUPIROAMINGPOLICY) 
功能说明 
该命令用于查询已经配置的基于SUPI号段的漫游策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|supi|参数可选性: 任选参数类型: 字符串参数范围: 1-16|本参数用于配置SUPI号段。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
SUPI|supi|参数可选性: 任选参数类型: 字符串参数范围: 1-16|本参数用于配置SUPI号段。
LBO|LBO|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: RESTRICT|本参数用于设置LBO策略，LBO是指Local breakout（漫游地）漫游接入，指漫游用户通过拜访地PGW接入获取相应业务，业务的提供者可以是归属网络，也可以是拜访网络。限制：表示终端不允许使用LBO。签约：表示AMF需要根据终端的签约信息，来确定终端是否可以使用LBO。
hSMFQueryMode|hSMF查询方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOHNSSFRETURNNRF|本参数用于设置home SMF的查询方式。在HR漫游方式下，AMF需要选择home SMF。HR漫游接入：Home routed（归属地）漫游接入，指漫游用户经由拜访地网络连接到归属地网络接入， 获取归属网络提供的业务。若配置为“需要hNSSF返回NRF信息”，则AMF需要到home NSSF返回的NRF上，查询获取home SMF。若配置为“不需hNSSF返回NRF信息”，则AMF需要到本地配置的NRF上，查询获取home SMF。
命令举例 
`
查询已经配置的SUPI漫游策略配置。 
SHOW SUPIROAMINGPOLICY
(No.1) : SHOW SUPIROAMINGPOLICY:
-----------------Namf_Communication_0----------------
supi     LBO      hSMF查询方式
4601    限制      不需hNSSF返回NRF信息
记录数：1
执行成功耗时: 0.094 秒
` 
## 跨PLMN移动策略 
## 跨PLMN移动策略 
背景知识 
漫游，指移动终端用户移动到归属运营商网络以外的国家或地区仍能继续使用移动终端业务。 
根据移动终端的漫游业务接入策略，按业务是否需要迂回到归属地，可以分为两种漫游模式：Home routed（归属地）漫游接入、Local breakout（漫游地）漫游接入。 
 
HR漫游接入
指漫游用户经由拜访地网络连接到归属地网络接入， 获取归属网络提供业务。 
 
LBO漫游接入
指漫游用户通过拜访地网络接入获取相应业务，业务的提供者可以是归属网络，也可以是拜访网络。 
 
功能说明 
跨PLMN移动策略包括跨PLMN移动全局策略、基于PLMN的跨PLMN移动策略等。 
子主题： 
### 跨PLMN移动全局策略 
### 跨PLMN移动全局策略 
背景知识 
漫游，指移动终端用户移动到归属运营商网络以外的国家或地区仍能继续使用移动终端业务。 
根据移动终端的漫游业务接入策略，按业务是否需要迂回到归属地，可以分为两种漫游模式：Home routed（归属地）漫游接入、Local breakout（漫游地）漫游接入。 
 
HR漫游接入
指漫游用户经由拜访地网络连接到归属地网络接入， 获取归属网络提供业务。 
 
LBO漫游接入
指漫游用户通过拜访地网络接入获取相应业务，业务的提供者可以是归属网络，也可以是拜访网络。 
 
功能说明 
本功能用于设置跨PLMN移动全局策略，包括功能开关，跨PLMN N14接口默认处理策略，跨PLMN N26接口默认处理策略等。 
子主题： 
#### 设置跨PLMN移动全局策略(SET GLOBALINTERPLMNMOBPLY) 
#### 设置跨PLMN移动全局策略(SET GLOBALINTERPLMNMOBPLY) 
功能说明 
该命令用于设置跨PLMN移动全局策略。 
注意事项 
 
本命令执行后，结果立即生效。 
 
当license“AMF支持跨PLMN移动”开启下，本配置才能生效。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ifsprtinterplmnmob|支持跨PLMN移动|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持跨PLMN的移动策略。本参数为总开关，当本参数开启时，忽略N14/N26等参数才生效。修改影响：用于控制AMF是否支持跨PLMN的移动策略。数据来源：本端规划。默认值：AMF不支持跨PLMN移动策略。配置原则：如果需要AMF支持跨PLMN移动策略，则可开启此功能。
ifskipn14in|漫入用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N14接口处理。当AMF支持漫入用户忽略N14接口时，则AMF跳过执行向老局AMF获取上下文的流程。修改影响：用于控制AMF对于漫入用户是否支持忽略N14接口。数据来源：本端规划。默认值：AMF支持漫入用户忽略N14接口。配置原则：如果需要AMF对漫入用户进行忽略N14接口处理，则可开启此功能。
ifskipn14out|漫出用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N14接口处理。当AMF支持漫出用户忽略N14接口时，则AMF作为老局时直接丢弃收到的来自AMF的上下文请求消息。修改影响：用于控制AMF对于漫出用户是否支持忽略N14接口。数据来源：本端规划。默认值：AMF支持漫出用户忽略N14接口。配置原则：如果需要AMF对漫出用户进行忽略N14接口处理，则可开启此功能。
ifskipn26in|漫入用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N26接口处理。当AMF支持漫入用户忽略N26接口时，则AMF跳过执行向老局MME获取上下文的流程。修改影响：用于控制AMF对于漫入用户是否支持忽略N26接口。数据来源：本端规划。默认值：AMF支持漫入用户忽略N26接口。配置原则：如果需要AMF对漫入用户进行忽略N26接口处理，则可开启此功能。
ifskipn26out|漫出用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N26接口处理。当AMF支持漫出用户忽略N26接口时，则AMF作为老局时直接丢弃收到的来自MME的上下文请求消息。修改影响：用于控制AMF对于漫出用户是否支持忽略N26接口。数据来源：本端规划。默认值：AMF支持漫出用户忽略N26接口。配置原则：如果需要AMF对漫出用户进行忽略N26接口处理，则可开启此功能。
ifgetsucifailfromold|网络侧没有获取到用户上下文时是否向UE要SUCI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，是否向UE获取SUCI，使注册更新流程继续下去。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。修改影响：当AMF获取上下文失败时，若该参数设置为是，则继续执行流程；若设置为否，则中止流程，下发注册拒绝数据来源：本端规划。默认值：在AMF获取用户上下文失败时，需要向UE索要SUCI。配置原则：如果需要AMF在获取用户上下文失败时，继续执行流程，则可开启此功能。
causefailfromold|从老局获取用户上下文失败时注册拒绝原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: UEIDNOTDERIVEDBYNET|参数作用：该参数用于设置AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，如果拒绝用户接入，拒绝的5GMM原因值。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。修改影响：设置当AMF获取上下文失败，如果拒绝用户接入，拒绝的5GMM原因值数据来源：本端规划。默认值：9-UE identity cannot be derived by the network。配置原则：如果需要修改AMF在获取用户上下文失败时，下发注册拒绝的5GMM原因值，则可设置该参数。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。
ifinterplmnapiroot|支持interPlmnApiRoot功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持interPlmnApiRoot功能。当AMF支持interPlmnApiRoot功能时，在用户发生跨PLMN移动的情况下，AMF会使用SMF返回的interPlmnApiRoot，重新构造smContextRef，再发送给SMF，后续SMF使用AMF重新构造的smContextRef，从而实现SMF在不同PLMN使用不同的FQDN。修改影响：用于控制AMF是否支持interPlmnApiRoot功能。数据来源：本端规划。默认值：AMF不支持interPlmnApiRoot功能。配置原则：如果需要AMF支持interPlmnApiRoot功能，则可开启此功能。
命令举例 
`
修改跨PLMN移动全局配置记录，修改为支持跨PLMN移动，漫入用户忽略N14接口，漫出用户忽略N14接口，漫入用户忽略N26，漫出用户忽略N26接口，网络侧没有获取到用户上下文时向UE索要SUCI，从老局获取用户上下文失败时拒绝原因值为UEIDNOTDERIVEDBYNET
SET GLOBALINTERPLMNMOBPLY:IFSPRTINTERPLMNMOB=1,IFSKIPN14IN=1,IFSKIPN14OUT=1,IFSKIPN26IN=1,IFSKIPN26OUT=1,IFGETSUCIFAILFROMOLD=1,CAUSEFAILFROMOLD="UEIDNOTDERIVEDBYNET"
` 
#### 查询跨PLMN移动全局策略(SHOW GLOBALINTERPLMNMOBPLY) 
#### 查询跨PLMN移动全局策略(SHOW GLOBALINTERPLMNMOBPLY) 
功能说明 
该命令用于查询跨PLMN移动全局策略。 
注意事项 
本命令执行后立即生效。 
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ifsprtinterplmnmob|支持跨PLMN移动|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持跨PLMN的移动策略。本参数为总开关，当本参数开启时，忽略N14/N26等参数才生效。
ifskipn14in|漫入用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N14接口处理。当AMF支持漫入用户忽略N14接口时，则AMF跳过执行向老局AMF获取上下文的流程。
ifskipn14out|漫出用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N14接口处理。当AMF支持漫出用户忽略N14接口时，则AMF作为老局时直接丢弃收到的来自AMF的上下文请求消息。
ifskipn26in|漫入用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N26接口处理。当AMF支持漫入用户忽略N26接口时，则AMF跳过执行向老局MME获取上下文的流程。
ifskipn26out|漫出用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N26接口处理。当AMF支持漫出用户忽略N26接口时，则AMF作为老局时直接丢弃收到的来自MME的上下文请求消息。
ifgetsucifailfromold|网络侧没有获取到用户上下文时是否向UE要SUCI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，是否向UE获取SUCI，使注册更新流程继续下去。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。
causefailfromold|从老局获取用户上下文失败时注册拒绝原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: UEIDNOTDERIVEDBYNET|参数作用：该参数用于设置AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，如果拒绝用户接入，拒绝的5GMM原因值。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于性能统计时归类使用。
ifinterplmnapiroot|支持interPlmnApiRoot功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOSPRT|参数作用：该参数用于设置AMF是否支持interPlmnApiRoot功能。当AMF支持interPlmnApiRoot功能时，在用户发生跨PLMN移动的情况下，AMF会使用SMF返回的interPlmnApiRoot，重新构造smContextRef，再发送给SMF，后续SMF使用AMF重新构造的smContextRef，从而实现SMF在不同PLMN使用不同的FQDN。
命令举例 
`
查询跨PLMN移动全局配置记录
SHOW GLOBALINTERPLMNMOBPLY
(No.1) : SHOW GLOBALINTERPLMNMOBPLY:
-----------------Namf_Communication_0----------------
操作维护       支持跨PLMN移动 漫入用户忽略N14接口处理 漫出用户忽略N14接口处理 漫入用户忽略N26接口处理 漫出用户忽略N26接口处理 网络侧没有获取到用户上下文时是否向UE要SUCI 从老局获取用户上下文失败时注册拒绝原因值         计数归类 支持interPlmnApiRoot功能 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           否             是                      是                      是                      是                      是                                         9 - UE identity cannot be derived by the network 0        否                       
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-05-9 15:44:53 耗时: 0.136 秒
` 
### 基于PLMN的跨PLMN移动策略配置 
### 基于PLMN的跨PLMN移动策略配置 
背景知识 
漫游，指移动终端用户移动到归属运营商网络以外的国家或地区仍能继续使用移动终端业务。 
根据移动终端的漫游业务接入策略，按业务是否需要迂回到归属地，可以分为两种漫游模式：Home routed（归属地）漫游接入、Local breakout（漫游地）漫游接入。 
 
HR漫游接入
指漫游用户经由拜访地网络连接到归属地网络接入， 获取归属网络提供业务。 
 
LBO漫游接入
指漫游用户通过拜访地网络接入获取相应业务，业务的提供者可以是归属网络，也可以是拜访网络。 
 
功能说明 
对于漫游用户，HPLMN和VPLMN间N14或N26接口是否安全可用，是运营商间确定的。本功能配置用户跨PLMN移动时N14或N26接口是否可用策略。 
子主题： 
#### 新增基于PLMN的跨PLMN移动策略配置(ADD INTERPLMNMOBPLY) 
#### 新增基于PLMN的跨PLMN移动策略配置(ADD INTERPLMNMOBPLY) 
功能说明 
该命令用于新增基于PLMN的跨PLMN移动策略。当需要设置与某个PLMN的N14或N26接口是否可用时，通过本命令增加该特定PLMN移动策略。 
N14接口是AMF与其他AMF之间的接口。 
N26接口是AMF与MME之间的接口。 
注意事项 
 
本命令执行后，结果立即生效。 
 
当SET GLOBALINTERPLMNMOBPLY命令中的参数“支持跨PLMN移动（ifsprtinterplmnmob）”设置为“支持（YES）”时，并且license“AMF支持跨PLMN移动”开启下，本命令才能生效。 
 
MCC和MNC无法设置"FFF"+"FF"的通配形式。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：全网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：全网规划。默认值：无。配置原则：无。
ifskipn14in|漫入用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N14接口处理。当AMF支持漫入用户忽略N14接口时，则AMF跳过执行向老局AMF获取上下文的流程。修改影响：用于控制AMF对于漫入用户是否支持忽略N14接口。数据来源：本端规划。默认值：AMF支持漫入用户忽略N14接口。配置原则：如果需要AMF对漫入用户进行忽略N14接口处理，则可开启此功能。
ifskipn14out|漫出用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N14接口处理。当AMF支持漫出用户忽略N14接口时，则AMF作为老局时直接丢弃收到的来自AMF的上下文请求消息。修改影响：用于控制AMF对于漫出用户是否支持忽略N14接口。数据来源：本端规划。默认值：AMF支持漫出用户忽略N14接口。配置原则：如果需要AMF对漫出用户进行忽略N14接口处理，则可开启此功能。
ifskipn26in|漫入用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N26接口处理。当AMF支持漫入用户忽略N26接口时，则AMF跳过执行向老局MME获取上下文的流程。修改影响：用于控制AMF对于漫入用户是否支持忽略N26接口。数据来源：本端规划。默认值：AMF支持漫入用户忽略N26接口。配置原则：如果需要AMF对漫入用户进行忽略N26接口处理，则可开启此功能。
ifskipn26out|漫出用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N26接口处理。当AMF支持漫出用户忽略N26接口时，则AMF作为老局时直接丢弃收到的来自MME的上下文请求消息。修改影响：用于控制AMF对于漫出用户是否支持忽略N26接口。数据来源：本端规划。默认值：AMF支持漫出用户忽略N26接口。配置原则：如果需要AMF对漫出用户进行忽略N26接口处理，则可开启此功能。
ifgetsucifailfromold|网络侧没有获取到用户上下文时是否向UE要SUCI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，是否向UE获取SUCI，使注册更新流程继续下去。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。修改影响：当AMF获取上下文失败时，若该参数设置为是，则继续执行流程；若设置为否，则中止流程，下发注册拒绝数据来源：本端规划。默认值：在AMF获取用户上下文失败时，需要向UE索要SUCI。配置原则：如果需要AMF在获取用户上下文失败时，继续执行流程，则可开启此功能。
causefailfromold|从老局获取用户上下文失败时注册拒绝原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: UEIDNOTDERIVEDBYNET|参数作用：该参数用于设置AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，如果拒绝用户接入，拒绝的5GMM原因值。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。修改影响：设置当AMF获取上下文失败，如果拒绝用户接入，拒绝的5GMM原因值数据来源：本端规划。默认值：9-UE identity cannot be derived by the network。配置原则：如果需要修改AMF在获取用户上下文失败时，下发注册拒绝的5GMM原因值，则可设置该参数。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于填写对配置记录的详细说明。修改影响：运营商可设置记录的别名，方便理解此记录存在的场景。数据来源：本端规划 默认值：无 配置原则：无
命令举例 
`
新增一条配置记录，其中MCC为460，MNC为11，漫入用户忽略N14接口，漫出用户忽略N14接口，漫入用户忽略N26，漫出用户忽略N26接口，网络侧没有获取到用户上下文时向UE索要SUCI，从老局获取用户上下文失败时拒绝原因值为UEIDNOTDERIVEDBYNET
ADD INTERPLMNMOBPLY:MCC="460",MNC="11",IFSKIPN14IN=1,IFSKIPN14OUT=1,IFSKIPN26IN=1,IFSKIPN26OUT=1,IFGETSUCIFAILFROMOLD=1,CAUSEFAILFROMOLD="UEIDNOTDERIVEDBYNET"
` 
#### 修改基于PLMN的跨PLMN移动策略配置(SET INTERPLMNMOBPLY) 
#### 修改基于PLMN的跨PLMN移动策略配置(SET INTERPLMNMOBPLY) 
功能说明 
该命令用于修改基于PLMN的跨PLMN移动策略。 
注意事项 
本命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：全网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：全网规划。默认值：无。配置原则：无。
ifskipn14in|漫入用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N14接口处理。当AMF支持漫入用户忽略N14接口时，则AMF跳过执行向老局AMF获取上下文的流程。修改影响：用于控制AMF对于漫入用户是否支持忽略N14接口。数据来源：本端规划。默认值：AMF支持漫入用户忽略N14接口。配置原则：如果需要AMF对漫入用户进行忽略N14接口处理，则可开启此功能。
ifskipn14out|漫出用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N14接口处理。当AMF支持漫出用户忽略N14接口时，则AMF作为老局时直接丢弃收到的来自AMF的上下文请求消息。修改影响：用于控制AMF对于漫出用户是否支持忽略N14接口。数据来源：本端规划。默认值：AMF支持漫出用户忽略N14接口。配置原则：如果需要AMF对漫出用户进行忽略N14接口处理，则可开启此功能。
ifskipn26in|漫入用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N26接口处理。当AMF支持漫入用户忽略N26接口时，则AMF跳过执行向老局MME获取上下文的流程。修改影响：用于控制AMF对于漫入用户是否支持忽略N26接口。数据来源：本端规划。默认值：AMF支持漫入用户忽略N26接口。配置原则：如果需要AMF对漫入用户进行忽略N26接口处理，则可开启此功能。
ifskipn26out|漫出用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N26接口处理。当AMF支持漫出用户忽略N26接口时，则AMF作为老局时直接丢弃收到的来自MME的上下文请求消息。修改影响：用于控制AMF对于漫出用户是否支持忽略N26接口。数据来源：本端规划。默认值：AMF支持漫出用户忽略N26接口。配置原则：如果需要AMF对漫出用户进行忽略N26接口处理，则可开启此功能。
ifgetsucifailfromold|网络侧没有获取到用户上下文时是否向UE要SUCI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，是否向UE获取SUCI，使注册更新流程继续下去。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。修改影响：当AMF获取上下文失败时，若该参数设置为是，则继续执行流程；若设置为否，则中止流程，下发注册拒绝数据来源：本端规划。默认值：在AMF获取用户上下文失败时，需要向UE索要SUCI。配置原则：如果需要AMF在获取用户上下文失败时，继续执行流程，则可开启此功能。
causefailfromold|从老局获取用户上下文失败时注册拒绝原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: UEIDNOTDERIVEDBYNET|参数作用：该参数用于设置AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，如果拒绝用户接入，拒绝的5GMM原因值。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。修改影响：设置当AMF获取上下文失败，如果拒绝用户接入，拒绝的5GMM原因值数据来源：本端规划。默认值：9-UE identity cannot be derived by the network。配置原则：如果需要修改AMF在获取用户上下文失败时，下发注册拒绝的5GMM原因值，则可设置该参数。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于性能统计时归类使用。修改影响：修改此参数, 影响性能统计计数归类。数据来源：本端规划 默认值：无。配置原则：无。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于填写对配置记录的详细说明。修改影响：运营商可设置记录的别名，方便理解此记录存在的场景。数据来源：本端规划 默认值：无 配置原则：无
命令举例 
`
修改MCC为460，MNC为11的配置记录，修改为漫入用户忽略N14接口，漫出用户忽略N14接口，漫入用户忽略N26，漫出用户忽略N26接口，网络侧没有获取到用户上下文时向UE索要SUCI，从老局获取用户上下文失败时拒绝原因值为UEIDNOTDERIVEDBYNET
SET INTERPLMNMOBPLY:MCC="460",MNC="11",IFSKIPN14IN=1,IFSKIPN14OUT=1,IFSKIPN26IN=1,IFSKIPN26OUT=1,IFGETSUCIFAILFROMOLD=1,CAUSEFAILFROMOLD="UEIDNOTDERIVEDBYNET"
` 
#### 删除基于PLMN的跨PLMN移动策略配置(DEL INTERPLMNMOBPLY) 
#### 删除基于PLMN的跨PLMN移动策略配置(DEL INTERPLMNMOBPLY) 
功能说明 
该命令用于删除基于PLMN的跨PLMN移动策略配置。 
注意事项 
本命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：全网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：全网规划。默认值：无。配置原则：无。
命令举例 
`
删除MCC为460，MNC为11的配置记录
DEL INTERPLMNMOBPLY:MCC="460",MNC="11"
` 
#### 查询基于PLMN的跨PLMN移动策略配置(SHOW INTERPLMNMOBPLY) 
#### 查询基于PLMN的跨PLMN移动策略配置(SHOW INTERPLMNMOBPLY) 
功能说明 
该命令用于查询基于PLMN的跨PLMN移动策略配置。 
注意事项 
本命令执行后立即生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：全网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：本参数为命令的主键之一，不可以被修改；如需修改，需先删除此条配置记录再增加。数据来源：全网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置AMF基于PLMN的跨PLMN移动性策略。MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
ifskipn14in|漫入用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N14接口处理。当AMF支持忽略N14接口时，则AMF跳过执行向老局AMF获取上下文的流程。
ifskipn14out|漫出用户忽略N14接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N14接口处理。当AMF支持漫出用户忽略N14接口时，则AMF作为老局时直接丢弃收到的来自AMF的上下文请求消息。
ifskipn26in|漫入用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫入用户是否忽略N26接口处理。当AMF支持漫入用户忽略N26接口时，则AMF跳过执行向老局MME获取上下文的流程。
ifskipn26out|漫出用户忽略N26接口处理|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于设置AMF对于漫出用户是否忽略N26接口处理。当AMF支持漫出用户忽略N26接口时，则AMF作为老局时直接丢弃收到的来自MME的上下文请求消息。
ifgetsucifailfromold|网络侧没有获取到用户上下文时是否向UE要SUCI|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SPRT|参数作用：该参数用于AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，是否向UE获取SUCI，使注册更新流程继续下去。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。
causefailfromold|从老局获取用户上下文失败时注册拒绝原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: UEIDNOTDERIVEDBYNET|参数作用：该参数用于设置AMF在跨AMF或跨RAT注册更新流程中向老局AMF或MME获取用户上下文失败时，如果拒绝用户接入，拒绝的5GMM原因值。向老局AMF或MME获取用户上下文失败，包括忽略N14接口处理、忽略N26接口处理、解析老局AMF或MME失败、没有收到老局AMF或MME的响应、老局AMF或MME返回失败等场景。
counter|计数归类|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于性能统计时归类使用。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-50|参数作用：该参数用于填写对配置记录的详细说明。
命令举例 
`
查询MCC为460，MNC为11的配置记录
SHOW INTERPLMNMOBPLY
(No.1) : SHOW INTERPLMNMOBPLY:
-----------------Namf_Communication_0----------------
操作维护       移动国家码   移动网络码  漫入用户忽略N14接口处理  漫出用户忽略N14接口处理  漫入用户忽略N26接口处理  漫出用户忽略N26接口处理  网络侧没有获取到用户上下文时是否向UE要SUCI 从老局获取用户上下文失败时注册拒绝原因值 计数归类 别名
------------------------------------------------------------------------
修改            460         11     是       是       是       是         是      9 - UE identity cannot be derived by the network
------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-05-9 15:44:53 耗时: 0.136 秒
` 
# MOCN配置 
# MOCN配置 
背景知识 
MOCN（Multi-Operator Core Network，多运营商核心网）是指多个运营商可以共享无线接入网络，但不共享核心网元的一种网络共享方式，这种场景是指多个运营商共同出资建设共享的无线接入网络，分担网络建设成本，降低网络建设风险，提高建网速度。 
开启MOCN功能的时候，多个PLMN会共享一个NR，NR在切换时，需要根据当前服务的PLMN选择target PLMN时，也会考虑网络侧下发的EPLMN（Equivalent Public Land Mobile Network，对等公用陆地移动网）。 网络侧AMF需要在EPLMN的切换限制列表中，携带Servcie PLMN给NR，便于NR在切换时，选择PLMN。 
关于MOCN的介绍，可参见TS23501第“5.18 Network Sharing”章节。 
功能说明 
本功能用于设置AMF是否需要支持MOCN功能。 开启本功能之后，AMF在5GS到EPS的切换过程中发送Forward Relocation Request消息时，会携带Selected PLMN ID。 
子主题： 
## 修改 AMF支持MOCN配置(SET AMFSUPPORTMOCN) 
## 修改 AMF支持MOCN配置(SET AMFSUPPORTMOCN) 
功能说明 
该命令用于设置或修改AMF是否开启MOCN功能。  
当需要开启或关闭MOCN功能时，可使用此命令。  
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
amfSupportMOCN|AMF支持MOCN选择|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFNOTSUPTMOCN|该参数用于设置AMF是否开启MOCN功能。
命令举例 
`
设置或修改是否支持MOCN功能。
SET AMFSUPPORTMOCN:AMFSUPPORTMOCN="AMFSUPTMOCN"
` 
## 查询 AMF支持MOCN配置(SHOW AMFSUPPORTMOCN) 
## 查询 AMF支持MOCN配置(SHOW AMFSUPPORTMOCN) 
功能说明 
该命令用于查询本AMF是否开启MOCN功能。  
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
amfSupportMOCN|AMF支持MOCN选择|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AMFNOTSUPTMOCN|该参数用于设置AMF是否开启MOCN功能。
命令举例 
`
查询MOCN功能是否开启。 
SHOW AMFSUPPORTMOCN:
(No.1) : SHOW AMFSUPPORTMOCN:
-----------------Namf_Communication_0----------------
AMF支持MOCN选择
支持MOCN
记录数：1
` 
# Nnrf注册管理 
# Nnrf注册管理 
背景知识 
AMF通过NRF实现NF服务相关的管理，功能包括： 
 
AMF部署成功后，主动向NRF注册AMF的NF Profile及包含的服务实例信息，用于其他NF可以通过NRF发现本AMF。 
 
当本AMF信息发生改变或不可用时，AMF可通过注册更新或去注册流程通知NRF，用于NRF及其他NF及时更新AMF的信息。 
 
AMF支持通过NRF实现其他NF的状态订阅和去订阅。 
 
功能说明 
Nnrf注册管理配置提供向NRF更新方式、向NRF订阅和心跳时长配置。 
子主题： 
## 向NRF更新方式配置 
## 向NRF更新方式配置 
背景知识 
AMF部署成功后，主动向NRF注册AMF的NF Profile及包含的服务实例信息，用于其他NF可以通过NRF发现本AMF。 
AMF通过向NRF发送更新NF Profile请求，来更改原先在NRF上注册的AMF的NF Profile信息。协议参考章节：3GPP TS  29510-f00-5.2.2.3.1。 
功能说明 
本功能用于配置AMF的NF Profile信息更新时，AMF所采用的方法及触发方式。 
子主题： 
### 修改NF更新方式配置(SET NFUPDATEMODE) 
### 修改NF更新方式配置(SET NFUPDATEMODE) 
功能说明 
本命令用于配置AMF的NF Profile信息更新时，AMF所采用的方法及触发方式。 
当NF向NRF发起更新流程时，需要使用该配置命令。 
注意事项 
系统默认采用PATCH方法，及自动更新方式。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
updateMethod|更新方法|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: PATCH|本参数用于设置AMF的NF Profile信息的更新方法，包括PUT和PATCH两种方式。PUT：完整替换原来的NF Profile。PATCH：部分替换原来的NF Profile。未启用SBI-GW功能时，该方式不支持用于TaiList和TaiRangeList的更新。
triggerMode|触发方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AUTOMATIC|本参数用于设置AMF的NF Profile信息更新的触发方式，包括手动和自动两种方式。自动：修改配置后，AMF立即触发向NRF更新。手动：修改配置后，AMF需要执行动态管理操作来触发更新。
nfUptDelayTimerLen|配置变更触发NF更新的延时定时器时长（毫秒）|参数可选性: 任选参数类型: 数字参数范围: 0-120000默认值: 10000|参数作用：本参数用于设置由于TAC（Tracking Area Code，跟踪区域码）和基于PLMN的AMF支持的SNSSAI配置变更，导致AMF向NRF更新的延时时长，目的在于避免由于配置频繁变更导致AMF向NRF更新过于频繁。修改影响：修改本参数后，可以避免由于配置频繁变更导致AMF向NRF更新过于频繁。数据来源：本端规划。默认值：10000ms。配置原则：无。
tasourcemode|AMF向NRF注册AMF信息时携带TA的来源方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOCALTACFG|参数作用：本参数用于配置AMF向NRF注册AMF信息时，携带TA（Tracking Area，跟踪区域）的来源方式，包括以下两种方式：AMF本地TA配置方式当选择此种方式时，AMF将根据本地配置的TA信息向NRF进行注册。从gNB侧学习方式当选择此种方式时，AMF将根据从gNB侧携带上来所学习到的TA信息向NRF进行注册。修改影响：修改本参数后，AMF会触发向NRF的TA更新流程。数据来源：本端规划。默认值：AMF本地TA配置方式。配置原则：无。
talearntime|AMF向gNB侧学习TA信息时长（分）|参数可选性: 任选参数类型: 数字参数范围: 1-120默认值: 5|参数作用：本参数用于配置AMF向gNB侧学习TA（Tracking Area，跟踪区域）信息时长。考虑到AMF上电后的一段时间内，可能会有大量的gNB与AMF之间进行建链流程。此时，如果AMF选择从gNB侧学习TA的方式，会导致AMF不停的向NRF进行注册信息更新。为了避免AMF与NRF之间产生大量的更新消息，通过本配置，可以在AMF上电初始的一段时间内，限制AMF不向NRF进行更新流程，等到AMF的上电时长超过此参数配置的AMF向gNB侧学习TA信息时长后，再向NRF进行更新流程。修改影响：修改参数后，当基站侧携带的TA信息发生变化时，会改变上电后向NRF发送更新消息的等待时长。数据来源：本端规划。默认值：5分钟。配置原则：无。
chkgnbtachgtime|AMF定时检查gNB侧TA信息变更时长（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-60默认值: 10|参数作用：本参数用于配置AMF定时检查gNB侧TA信息变更时长。当gNB侧携带的TA信息发生变化时，在本参数配置的时长内，AMF将向NRF进行注册信息的更新。修改影响：修改参数后，当gNB侧携带的TA信息发生变化时，会改变AMF向NRF进行注册信息的更新的等待时长。数据来源：本端规划。默认值：10秒。配置原则：无。
ifchktarange|AMF向gNB学习TA信息时是否做AMF本地TA范围配置检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：本参数用于配置AMF向gNB学习TA信息时，是否进行AMF本地TA范围配置检查，包括两个选项：开启：AMF会将gNB携带的TA信息与AMF本地配置的TA范围，两者进行比较。如果gNB携带的TA信息不在AMF本地配置的TA范围内，则AMF不会将该TA信息向NRF进行更新。关闭：AMF不会将gNB携带的TA信息与AMF本地配置的TA范围，两者进行比较。修改影响：修改参数后，将影响向NRF进行更新的TA信息。数据来源：本端规划。默认值：是。配置原则：无。
命令举例 
`
设置当前NFNF Profile为PUT，触发方式为手动。
SET NFUPDATEMODE:UPDATEMETHOD="PUT",TRIGGERMODE="MANUAL"
` 
### 查询NF更新方式配置(SHOW NFUPDATEMODE) 
### 查询NF更新方式配置(SHOW NFUPDATEMODE) 
功能说明 
该命令用于显示当前NF Profile更新时，采用的更新方法及触发方式。
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
updateMethod|更新方法|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: PATCH|本参数用于设置AMF的NF Profile信息的更新方法，包括PUT和PATCH两种方式。PUT：完整替换原来的NF Profile。PATCH：部分替换原来的NF Profile。该方式不支持TaiList和TaiRangeList的更新。
triggerMode|触发方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: AUTOMATIC|本参数用于设置AMF的NF Profile信息更新的触发方式，包括手动和自动两种方式。自动：修改配置后，AMF立即触发向NRF更新。手动：修改配置后，AMF需要执行动态管理操作来触发更新。
nfUptDelayTimerLen|配置变更触发NF更新的延时定时器时长（毫秒）|参数可选性: 任选参数类型: 数字参数范围: 0-120000默认值: 10000|本参数用于设置TAC和基于PLMN的AMF支持的SNSSAI配置变更，导致AMF向NRF更新的延时时长，目的在于避免配置频繁变更导致AMF向NRF更新过于频繁。
tasourcemode|AMF向NRF注册AMF信息时携带TA的来源方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOCALTACFG|参数作用：本参数用于配置AMF向NRF注册AMF信息时，携带TA（Tracking Area，跟踪区域）的来源方式，包括以下两种方式：AMF本地TA配置方式当选择此种方式时，AMF将根据本地配置的TA信息向NRF进行注册。从gNB侧学习方式当选择此种方式时，AMF将根据从gNB侧携带上来所学习到的TA信息向NRF进行注册。
talearntime|AMF向gNB侧学习TA信息时长（分）|参数可选性: 任选参数类型: 数字参数范围: 1-120默认值: 5|参数作用：本参数用于配置AMF向gNB侧学习TA（Tracking Area，跟踪区域）信息时长。考虑到AMF上电后的一段时间内，可能会有大量的gNB与AMF之间进行建链流程。此时，如果AMF选择从gNB侧学习TA的方式，会导致AMF不停的向NRF进行注册信息更新。为了避免AMF与NRF之间产生大量的更新消息，通过本配置，可以在AMF上电初始的一段时间内，限制AMF不向NRF进行更新流程，等到AMF的上电时长超过此参数配置的AMF向gNB侧学习TA信息时长后，再向NRF进行更新流程。
chkgnbtachgtime|AMF定时检查gNB侧TA信息变更时长（秒）|参数可选性: 任选参数类型: 数字参数范围: 1-60默认值: 10|参数作用：本参数用于配置AMF定时检查gNB侧TA信息变更时长。当gNB侧携带的TA信息发生变化时，在本参数配置的时长内，AMF将向NRF进行注册信息的更新。
ifchktarange|AMF向gNB学习TA信息时是否做AMF本地TA范围配置检查|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|参数作用：本参数用于配置AMF向gNB学习TA信息时，是否进行AMF本地TA范围配置检查，包括两个选项：开启：AMF会将gNB携带的TA信息与AMF本地配置的TA范围，两者进行比较。如果gNB携带的TA信息不在AMF本地配置的TA范围内，则AMF不会将该TA信息向NRF进行更新。关闭：AMF不会将gNB携带的TA信息与AMF本地配置的TA范围，两者进行比较。
命令举例 
`
查询当前采用的NF Profile更新方法。 
SHOW NFUPDATEMODE:
(No.1) : SHOW NFUPDATEMODE:
-----------------Namf_Communication_0----------------
操作维护       更新方法 触发方式 配置变更触发NF更新的延时定时器时长（毫秒） AMF向NRF注册AMF信息时携带TA的来源方式 AMF向gNB侧学习TA信息时长（分） AMF定时检查gNB侧TA信息变更时长（秒） AMF向gNB学习TA信息时是否做AMF本地TA范围配置检查 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           部分更新 自动     10000                                      AMF本地TA配置                         5                              10                                   是                                              
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
` 
## 向NRF订阅配置 
## 向NRF订阅配置 
背景知识 
AMF通过向NRF发现NF后，AMF会订阅发现成功的NF，当NF信息发生变更后，AMF会收到NRF发送的变更通知，AMF再进行后续的相应处理，保证业务的正常进行。 
功能说明 
本功能提供向NRF订阅策略和订阅有效时长配置。 
子主题： 
### 订阅有效时长配置 
### 订阅有效时长配置 
背景知识 
AMF向NRF发现NF后，AMF订阅发现成功的NF，NF信息发生变更后，AMF会收到NRF的变更通知，AMF再进行后续的相应处理，保证业务的正常进行。 
功能说明 
本功能用于配置AMF向NRF订阅NF信息变更的有效时长。 
子主题： 
#### 修改NF订阅有效时长配置(SET NFSUBSCRIBEVALIDITYTIME) 
#### 修改NF订阅有效时长配置(SET NFSUBSCRIBEVALIDITYTIME) 
功能说明 
本命令用于设置或修改AMF向NRF订阅NF的有效时长。 
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
nfSubValidityTime|NF订阅有效时长(分钟)|参数可选性: 必选参数类型: 数字参数范围: 10-60000默认值: 600|该参数用于设置AMF订阅NF信息的有效时长。
命令举例 
`
设置AMF向NRF订阅NF的有效时长为600分钟。
SET NFSUBSCRIBEVALIDITYTIME:NFSUBVALIDITYTIME=600
` 
#### 查询NF订阅有效时长配置(SHOW NFSUBSCRIBEVALIDITYTIME) 
#### 查询NF订阅有效时长配置(SHOW NFSUBSCRIBEVALIDITYTIME) 
功能说明 
本命令用于查询AMF向NRF订阅NF的有效时长。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
nfSubValidityTime|NF订阅有效时长(分钟)|参数可选性: 任选参数类型: 数字参数范围: 10-60000默认值: 600|该参数用于设置AMF订阅NF信息的有效时长。
命令举例 
`
查询AMF向NRF订阅NF的有效时长。
SHOW NFSUBSCRIBEVALIDITYTIME:
SHOW NFSUBSCRIBEVALIDITYTIME:
-----------------Namf_Communication_0----------------
NF订阅有效时长(分钟)
-----------------------------------------------------------------
              600
-----------------------------------------------------------------
记录数：1
执行成功耗时: 0.963 秒
` 
## 心跳时长配置 
## 心跳时长配置 
背景知识 
AMF向NRF发送的注册请求消息中，可能包含AMF到NRF的两条连续心跳消息之间的预期时间（秒），当AMF向NRF发送的注册请求消息中存在该字段时，应包含由NF服务消费者来指定的心跳时间。 
功能说明 
本功能用于设置AMF向NRF注册时，AMF向NRF发送的注册请求消息中的NF Profile中所携带的心跳时长。 
子主题： 
### 修改NRF心跳时长配置(SET NRFHEARTBEATTIMER) 
### 修改NRF心跳时长配置(SET NRFHEARTBEATTIMER) 
功能说明 
本命令用于设置或修改AMF向NRF注册时携带的心跳时长字段：heartBeatTimer，单位为秒。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
nrfHeartbeatTimer|NRF心跳时长(秒)|参数可选性: 必选参数类型: 数字参数范围: 0-65535默认值: 10|该参数用于设置AMF向NRF注册时，携带的心跳时长：heartBeatTimer。该心跳时长，表示AMF向NRF发送两条连续心跳消息之间的预期时间，如果NRF根据本配置的结果接受期望的心跳时间，则使用与注册请求中相同的值；否则，NRF使用预先配置的值覆盖本命令配置的值，并在注册响应消息中返回给AMF。若心跳时间配置为0，则AMF在向NRF发送的注册请求中，不会携带心跳时长heartBeatTimer。
命令举例 
`
设置AMF向NRF注册时携带的心跳时长心跳时长heartBeatTimer为600秒。
SET NRFHEARTBEATTIMER:NRFHEARTBEATTIMER=600
` 
### 查询NRF心跳时长配置(SHOW NRFHEARTBEATTIMER) 
### 查询NRF心跳时长配置(SHOW NRFHEARTBEATTIMER) 
功能说明 
本命令用于查询AMF向NRF注册时携带的心跳时长heartBeatTimer配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
nrfHeartbeatTimer|NRF心跳时长(秒)|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 10|该参数用于设置AMF向NRF注册时，携带的心跳时长：heartBeatTimer。该心跳时长，表示AMF向NRF发送两条连续心跳消息之间的预期时间，如果NRF根据本配置的结果接受期望的心跳时间，则使用与注册请求中相同的值；否则，NRF使用预先配置的值覆盖本命令配置的值，并在注册响应消息中返回给AMF。若心跳时间配置为0，则AMF在向NRF发送的注册请求中，不会携带心跳时长heartBeatTimer。
命令举例 
`
查询AMF向NRF注册携带的心跳时长心跳时长heartBeatTimer设置。
SHOW NRFHEARTBEATTIMER:
(No.1) : SHOW NRFHEARTBEATTIMER:
-----------------Namf_Communication_0----------------
NRF心跳时长(秒)
10
记录数：1
执行成功耗时: 1.05 秒
` 
## AMF TA范围配置 
## AMF TA范围配置 
背景知识 
AMF向NRF注册AMF信息时，AMF可以携带自身管理的TA（Tracking Area，跟踪区域）信息给NRF。AMF管理的TA信息可以通过两个方式获取到： 
 
AMF从无线侧获取TA信息
此种情况下，AMF需要在本地配置一个较大范围段的TA，然后向无线侧获取具体的TA，但是，如果无线侧的具体的TA，不在AMF本地配置的这个较大范围的TA中，则AMF不需要获取，即AMF只需要从无线侧获取本地配置的较大范围段TA的具体TA。AMF再将获取到的TA的具体信息进行精确分段汇聚，发送给NRF。 
 
AMF本地配置TA信息
此种情况下，AMF需要在本地详细配置完整的TA信息，AMF将所有TA信息进行精确分段汇聚后再传递给NRF。 
 
功能说明 
本功能用于增加AMF的TA（Tracking Area，跟踪区域）范围，配置AMF支持的跟踪区范围。 
 
本跟踪区范围为TA大段范围配置，AMF需要根据该配置范围，进一步向无线学习TA信息，AMF再将学习到的TA信息进行精确分段汇聚，得到精确的TA分段范围。 
 
子主题： 
### 新增AMF跟踪区范围配置(ADD AMF TRACKING AREA RANGE CONFIGURATION) 
### 新增AMF跟踪区范围配置(ADD AMF TRACKING AREA RANGE CONFIGURATION) 
功能说明 
该命令用于新增一条AMF跟踪区范围配置。 
注意事项 
跟踪区码终止必须大于等于跟踪区起始。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tacst|跟踪区码起始|参数可选性: 必选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的起始值。
tacend|跟踪区码终止|参数可选性: 必选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的终止。跟踪区码终止值必须大于等于跟踪区码起始值。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的起始值。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的终止。跟踪区码终止值必须大于等于跟踪区码起始值。
命令举例 
`
新增TA RANGE配置，MCC为460，MNC为11，TAC起始为000001,TAC终止为000002。
ADD AMF TRACKING AREA RANGE CONFIGURATION:MCC="460",MNC="11",TACST="000001",TACEND="000002"
` 
### 删除AMF跟踪区范围配置(DEL AMF TRACKING AREA RANGE CONFIGURATION) 
### 删除AMF跟踪区范围配置(DEL AMF TRACKING AREA RANGE CONFIGURATION) 
功能说明 
该命令用于删除一条AMF跟踪区范围配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tacst|跟踪区码起始|参数可选性: 必选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的起始值。
tacend|跟踪区码终止|参数可选性: 必选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的终止。跟踪区码终止值必须大于等于跟踪区码起始值。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的起始值。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的终止。跟踪区码终止值必须大于等于跟踪区码起始值。
命令举例 
`
删除TA RANGE配置，MCC为460，MNC为11，TAC起始为000001,TAC终止为000002。
DEL AMF TRACKING AREA RANGE CONFIGURATION:MCC="460",MNC="11",TACST="000001",TACEND="000002"
` 
### 查询AMF跟踪区范围配置(SHOW AMF TRACKING AREA RANGE CONFIGURATION) 
### 查询AMF跟踪区范围配置(SHOW AMF TRACKING AREA RANGE CONFIGURATION) 
功能说明 
该命令用于查询AMF跟踪区范围配置，系统支持查询单个AMF跟踪区范围配置或者全部AMF跟踪区范围配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的起始值。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的终止。跟踪区码终止值必须大于等于跟踪区码起始值。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的起始值。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6|该参数用于配置TA（Tracking Area，跟踪区域）编号段的终止。跟踪区码终止值必须大于等于跟踪区码起始值。
命令举例 
`
查询所有的TA RANGE配置。
SHOW AMF TRACKING AREA RANGE CONFIGURATION:
(No.7) : SHOW AMF TRACKING AREA RANGE CONFIGURATION:
-----------------Namf_Communication_0-----------------
操作维护       移动国家码 移动网络码 跟踪区码起始 跟踪区码终止 
---------------------------------------------------------------
复制           460        11         000001       000002         
---------------------------------------------------------------
记录数：1
` 
# 节点管理 
# 节点管理 
背景知识 
本功能用于配置AMF对现有网络中的GTP节点进行管理。 
功能说明 
本功能用于配置AMF对现有网络中的GTP节点进行管理。 
子主题： 
## GTP节点管理配置 
## GTP节点管理配置 
背景知识 
目前现网以4G网络为主，在4G/5G互操作时，要尽量避免对传统网络进行改造，以5G网络适配为主。AMF与MME之间采用GTP协议接口，AMF需要对现有网络中的GTP节点进行管理。 
功能说明 
本功能用于配置AMF对现有网络中的GTP节点进行管理。 
子主题： 
### GTP节点管理配置策略 
### GTP节点管理配置策略 
背景知识 
目前现网以4G网络为主，在4G/5G互操作时，要尽量避免对传统网络进行改造，以5G网络适配为主。AMF与MME之间采用GTP协议接口，AMF需要对现有网络中的GTP节点进行管理。 
功能说明 
本功能用于配置与GTP节点管理相关的策略。 
子主题： 
#### 修改GTP节点管理策略(SET GTPNODEPOLICY) 
#### 修改GTP节点管理策略(SET GTPNODEPOLICY) 
功能说明 
该命令用于修改GTP节点管理策略。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
retryTimes|ECHO消息发送次数|参数可选性: 任选参数类型: 数字参数范围: 3-30默认值: 5|该参数用于配置Echo Request消息的发送尝试次数（包括首次发送和后续重发）。 当重发达到最大次数，仍然没有收到对端返回的Echo Response消息，则停止发送，认为对端链路故障或对端网元发生故障。
retryInterval|ECHO消息重发间隔(秒)|参数可选性: 任选参数类型: 数字参数范围: 1-20默认值: 10|该参数用于配置Echo Request消息超时重发间隔（秒）。
alarmNodeAgeingLen|告警节点老化时长(小时)|参数可选性: 任选参数类型: 数字参数范围: 0-168默认值: 72|该参数配置GTP节点定时回收时长。如果该参数配置为0，表示关闭告警节点老化功能，配置为其他值，则表示告警节点老化时长。
gtpabnormalpolicy|GTP路径异常时策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-3默认值: TRIGGERECHODETECTION|该参数配置GTP节点异常时的管理策略。
命令举例 
`
ECHO消息发送次数(5次)、ECHO消息重发间隔(10秒)、告警节点老化时长(72小时)、GTP路径异常时测量“触发Echo检测”
SET GTPNODEPOLICY:RETRYTIMES=5,RETRYINTERVAL=10,ALARMNODEAGEINGLEN=72,GTPABNORMALPOLICY="TRIGGERECHODETECTION"
` 
#### 查询GTP节点管理策略(SHOW GTPNODEPOLICY) 
#### 查询GTP节点管理策略(SHOW GTPNODEPOLICY) 
功能说明 
该命令用于查询GTP节点管理策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
retryTimes|ECHO消息发送次数|参数可选性: 任选参数类型: 数字参数范围: 3-30默认值: 5|该参数用于配置Echo Request消息的发送尝试次数（包括首次发送和后续重发）。 当重发达到最大次数，仍然没有收到对端返回的Echo Response消息，则停止发送，认为对端链路故障或对端网元发生故障。
retryInterval|ECHO消息重发间隔(秒)|参数可选性: 任选参数类型: 数字参数范围: 1-20默认值: 10|该参数用于配置Echo Request消息超时重发间隔（秒）。
alarmNodeAgeingLen|告警节点老化时长(小时)|参数可选性: 任选参数类型: 数字参数范围: 0-168默认值: 72|该参数配置GTP节点定时回收时长。如果该参数配置为0，表示关闭告警节点老化功能，配置为其他值，则表示告警节点老化时长。
gtpabnormalpolicy|GTP路径异常时策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-3默认值: TRIGGERECHODETECTION|该参数配置GTP节点异常时的管理策略。
命令举例 
`
查询GTP节点管理策略。
SHOW GTPNODEPOLICY
(No.1) : SHOW GTPNODEPOLICY:
-----------------Namf_Communication_0----------------
操作维护       ECHO消息发送次数 ECHO消息重发间隔(秒) 告警节点老化时长(小时) GTP路径异常时策略 
----------------------------------------------------------------------------------------------
修改           5                10                   72                     触发ECHO检测      
----------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-11-06 11:44:01 耗时: 0.198 秒
` 
## GTP链路告警过滤配置 
## GTP链路告警过滤配置 
背景知识 
对于现网中大量出现的GTP链路断链告警，对于运营商而言，不需要关注所有的MME，只需要关注某些断链的MME，而不需要关注的MME断链，则不需要告警，每个GTP节点都上报告警的方式是不可取的。
通过本功能，可以配置AMF关注的对端MME节点才会上报告警，其他不关注的MME节点则不上报告警。 
功能说明 
AMF对GTP链路告警进行过滤，关注重要的MME节点是否发生故障。 
子主题： 
### 修改 GTP链路告警过滤策略(SET GTPCALARMFILTERPOLICY) 
### 修改 GTP链路告警过滤策略(SET GTPCALARMFILTERPOLICY) 
功能说明 
该命令用于设置或修改GTP链路告警过滤策略。 
注意事项 
若功能关闭，对所有对端GTP节点，如果发生断链，都会向AMF上报GTP链路告警。 
开启此功能之后，已通过[ADD GTPCALARMPEERADDRESS]命令配置了地址的对端GTP节点，如果发生断链，会向AMF上报GTP链路告警。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supportAlarmFilter|AMF是否支持GTP链路告警过滤|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOT_SUPPORT|该参数用于设置AMF是否开启GTP链路告警过滤功能。
命令举例 
`
设置GTP链路告警过滤策略
SET GTPCALARMFILTERPOLICY:SUPPORTALARMFILTER="SUPPORT"
` 
### 查询 GTP链路告警过滤策略(SHOW GTPCALARMFILTERPOLICY) 
### 查询 GTP链路告警过滤策略(SHOW GTPCALARMFILTERPOLICY) 
功能说明 
该命令用于查询GTP链路告警过滤策略。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supportAlarmFilter|AMF是否支持GTP链路告警过滤|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOT_SUPPORT|该参数用于设置AMF是否开启GTP链路告警过滤功能。
命令举例 
`
查询GTP链路告警过滤策略。
SHOW GTPCALARMFILTERPOLICY
(No.1) : SHOW GTPCALARMFILTERPOLICY:
-----------------Namf_Communication_0----------------
AMF是否支持GTP链路告警过滤
AMF支持GTP链路告警过滤
记录数：1
执行成功耗时: 0.192 秒
` 
### 新增 GTP链路告警对端节点地址(ADD GTPCALARMPEERADDRESS) 
### 新增 GTP链路告警对端节点地址(ADD GTPCALARMPEERADDRESS) 
功能说明 
该命令用于新增需要向AMF上报GTP链路断链告警的GTP节点地址。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
PeerAddress|GTP链路告警对端节点地址|参数可选性: 必选参数类型: 字符串|该参数用于设置需要向AMF上报GTP链路断链告警的GTP节点地址。开启GTP链路告警过滤功能后，只有通过此命令配置了地址的对端GTP节点发生断链时，会向AMF上报GTP链路告警。
命令举例 
`
增加GTP链路告警对端节点地址：1.1.1.1。
ADD GTPCALARMPEERADDRESS:PEERADDRESS=1.1.1.1
` 
### 删除 GTP链路告警对端节点地址(DEL GTPCALARMPEERADDRESS) 
### 删除 GTP链路告警对端节点地址(DEL GTPCALARMPEERADDRESS) 
功能说明 
该命令用于删除需要向AMF上报GTP链路断链告警的GTP节点地址。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
PeerAddress|GTP链路告警对端节点地址|参数可选性: 必选参数类型: 字符串|该参数用于设置需要向AMF上报GTP链路断链告警的GTP节点地址。开启GTP链路告警过滤功能后，只有通过此命令配置了地址的对端GTP节点发生断链时，会向AMF上报GTP链路告警。
命令举例 
`
删除GTP链路告警对端节点地址：1.1.1.1。
DEL GTPCALARMPEERADDRESS:PEERADDRESS=1.1.1.1
` 
### 查询 GTP链路告警对端节点地址(SHOW GTPCALARMPEERADDRESS) 
### 查询 GTP链路告警对端节点地址(SHOW GTPCALARMPEERADDRESS) 
功能说明 
该命令用于查询需要向AMF上报GTP链路断链告警的GTP节点地址。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
PeerAddress|GTP链路告警对端节点地址|参数可选性: 任选参数类型: 字符串|该参数用于设置需要向AMF上报GTP链路断链告警的GTP节点地址。开启GTP链路告警过滤功能后，只有通过此命令配置了地址的对端GTP节点发生断链时，会向AMF上报GTP链路告警。
命令举例 
`
查询GTP链路告警对端节点地址。
SHOW GTPCALARMPEERADDRESS
(No.1) : SHOW GTPCALARMPEERADDRESS
-----------------Namf_Communication_0----------------
GTP链路告警对端节点地址
1.1.1.1
2.2.2.2
记录数：2
执行成功耗时: 0.079 秒
` 
# 弹性配置 
# 弹性配置 
背景知识 
AMF为了提供电信级的高可靠性服务，使用统一存储节点UDSF（Unstructured Data Storage Function，非结构化数据存储功能）存储用户数据，将用户与计算节点解耦，达到无状态化的效果。 
计算节点可以随意弹缩，宕机等，对用户业务都不会产生影响。 
功能说明 
本功能用于配置与弹性相关的参数。 
子主题： 
## 修改弹性配置(SET SCALE CONFIG) 
## 修改弹性配置(SET SCALE CONFIG) 
功能说明 
该命令用于设置弹性参数配置。 
弹性参数配置是AMF系统运行的一些弹性相关、UDSF相关的内部参数设置。 
注意事项 
普通情况下，建议使用系统默认值，操作维护人员不得更改。针对某些特殊运营商、特殊场景、特殊情况下需要设置的，需要联系中兴通讯的技术支持人员才能修改。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
loadCtxFromUdsf|从UDSF加载上下文|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOADCTXFROMUDSF|该参数用于设置在弹缩、宕机、上电、负载均衡等场景时，群负荷分担发生了变化，接管群负荷的SC是否从UDSF加载用户上下文。系统默认配置向UDSF加载群下用户上下文，待用户活动时，系统再向UDSF单个获取用户上下文
userNumGetMode|用户数获取方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: GETFROMCONTEXT|该参数用于设置用户数获取方式，可以设置为“从资源中获取”、“从上下文中获取”两种方式。在5G网络中，存储节点和计算节点是分离部署的，当发生弹缩、宕机等触发群迁移时，群迁入计算节点上可以不立即向UDSF批量恢复用户上下文，待用户活动时，再向UDSF进行恢复，这样计算节点通过用户上下文个数来获取SC上的用户数就不准确了。所以，AMF提供了通过从SC分配出去的临时标识资源个数中获取用户数的方式。
preMigOutGrpScanRate|预迁出群扫描速率（个/100ms）|参数可选性: 任选参数类型: 数字参数范围: 1-300默认值: 60|该参数用于设置预迁出群扫描速率。系统因为弹缩、上电下电、负载重平衡等，会导致群负荷发生迁移。AMF为了将负荷迁移过程处理得平稳均衡，需要对群迁移速率进行速率控制。系统已经给出了默认的群迁移速率，通常情况下不能更改。如果因为特殊运营商的特殊使用场景下，导致该迁移速率也需要调整，则需要联系中兴通迅技术支持工程师，再进行修改。
migOutGrpScanRate|迁出群扫描速率（个/100ms）|参数可选性: 任选参数类型: 数字参数范围: 1-300默认值: 60|该参数用于设置迁出群扫描速率。系统因为弹缩、上电下电、负载重平衡等，会导致群负荷发生迁移。AMF为了将负荷迁移过程处理得平稳均衡，需要对群迁移速率进行速率控制。系统已经给出了默认的群迁移速率，通常情况下不能更改。如果因为特殊运营商的特殊使用场景下，导致该迁移速率也需要调整，则需要联系中兴通迅技术支持工程师，再进行修改。
migInGrpScanRate|迁入群扫描速率（个/100ms）|参数可选性: 任选参数类型: 数字参数范围: 1-30默认值: 1|该参数用于设置迁入群扫描速率。系统因为弹缩、上电下电、负载重平衡等，会导致群负荷发生迁移。AMF为了将负荷迁移过程处理得平稳均衡，需要对群迁移速率进行速率控制。系统已经给出了默认的群迁移速率，通常情况下不能更改。如果因为特殊运营商的特殊使用场景下，导致该迁移速率也需要调整，则需要联系中兴通迅技术支持工程师，再进行修改。
usernumlimitforscale|单SC支持的在线用户数的弹性上限|参数可选性: 任选参数类型: 数字参数范围: 0-350000默认值: 0|参数作用：该参数用于设置Communication服务弹缩时，使用的单SC支持的最大用户数。系统通过上下文比例来弹缩时，需要计算每个SC上的上下文比例即当前用户数和最大用户数的比例。修改影响：修改后，按照该配置值进行弹缩。数据来源：商务要求的单SC支持的用户数。默认值：0。配置原则：无。
periodsyncctx|定时向UDSF同步上下文|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NEEDPERIODICSYNC|参数作用：该参数用于设置AMF是否定时向UDSF同步上下文。AMF在增、删、改上下文时，会实时向UDSF触发同步。如果某次实时同步失败，可能导致UDSF和本地的数据不一致。为了确保UDSF和本地上下文数据一致，可以开启定时同步机制，除了实时同步数据之外，AMF还会定时全量扫描本地上下文，向UDSF发起数据同步。修改影响：修改后，按照该配置值进行定时同步。数据来源：根据运营商的实际要求，确认AMF是否需要定时向UDSF同步上下文。默认值：1。配置原则：无。
ctxcdbttl|上下文在UDSF上的TTL（小时）|参数可选性: 任选参数类型: 数字参数范围: 0-96默认值: 48|参数作用：该参数用于设置用户上下文在UDSF上的TTL（即Time-To-Live，有效生命时长）。如果UDSF上的用户上下文在TTL内没有得到同步刷新，UDSF会认为用户上下文已经老化失效，会对其进行删除处理。TTL设置为0表示用户上下文在UDSF上永久有效，UDSF不会对其进行删除。修改影响：系统已经给出了默认的TTL，通常情况下不能更改。如果因为特殊运营商的特殊使用场景下，导致该TTL也需要调整，则需要联系中兴通讯技术支持工程师，再进行修改。数据来源：该参数是从运营商的规划数据中获取的。默认值：48。配置原则：无。
命令举例 
`
设置弹性相关配置
SET SCALE CONFIG:LOADCTXFROMUDSF="NOTLOADCTXFROMUDSF",USERNUMGETMODE="GETFROMRESOURCE",PREMIGOUTGRPSCANRATE=60,MIGOUTGRPSCANRATE=60,MIGINGRPSCANRATE=1,USERNUMLIMITFORSCALE=100000,PERIODSYNCCTX="NEEDPERIODICSYNC",CTXCDBTTL=48
` 
## 查询弹性配置(SHOW SCALE CONFIG) 
## 查询弹性配置(SHOW SCALE CONFIG) 
功能说明 
该命令用于查询弹性参数配置。 
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
loadCtxFromUdsf|从UDSF加载上下文|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: LOADCTXFROMUDSF|该参数用于设置在弹缩、宕机、上电、负载均衡等场景时，群负荷分担发生了变化，接管群负荷的SC是否从UDSF加载用户上下文。系统默认配置向UDSF加载群下用户上下文，待用户活动时，系统再向UDSF单个获取用户上下文
userNumGetMode|用户数获取方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: GETFROMCONTEXT|该参数用于设置用户数获取方式，可以设置为“从资源中获取”、“从上下文中获取”两种方式。在5G网络中，存储节点和计算节点是分离部署的，当发生弹缩、宕机等触发群迁移时，群迁入计算节点上可以不立即向UDSF批量恢复用户上下文，待用户活动时，再向UDSF进行恢复，这样计算节点通过用户上下文个数来获取SC上的用户数就不准确了。所以，AMF提供了通过从SC分配出去的临时标识资源个数中获取用户数的方式。
preMigOutGrpScanRate|预迁出群扫描速率（个/100ms）|参数可选性: 任选参数类型: 数字参数范围: 1-300默认值: 60|该参数用于设置预迁出群扫描速率。系统因为弹缩、上电下电、负载重平衡等，会导致群负荷发生迁移。AMF为了将负荷迁移过程处理得平稳均衡，需要对群迁移速率进行速率控制。系统已经给出了默认的群迁移速率，通常情况下不能更改。如果因为特殊运营商的特殊使用场景下，导致该迁移速率也需要调整，则需要联系中兴通迅技术支持工程师，再进行修改。
migOutGrpScanRate|迁出群扫描速率（个/100ms）|参数可选性: 任选参数类型: 数字参数范围: 1-300默认值: 60|该参数用于设置迁出群扫描速率。系统因为弹缩、上电下电、负载重平衡等，会导致群负荷发生迁移。AMF为了将负荷迁移过程处理得平稳均衡，需要对群迁移速率进行速率控制。系统已经给出了默认的群迁移速率，通常情况下不能更改。如果因为特殊运营商的特殊使用场景下，导致该迁移速率也需要调整，则需要联系中兴通迅技术支持工程师，再进行修改。
migInGrpScanRate|迁入群扫描速率（个/100ms）|参数可选性: 任选参数类型: 数字参数范围: 1-30默认值: 1|该参数用于设置迁入群扫描速率。系统因为弹缩、上电下电、负载重平衡等，会导致群负荷发生迁移。AMF为了将负荷迁移过程处理得平稳均衡，需要对群迁移速率进行速率控制。系统已经给出了默认的群迁移速率，通常情况下不能更改。如果因为特殊运营商的特殊使用场景下，导致该迁移速率也需要调整，则需要联系中兴通迅技术支持工程师，再进行修改。
usernumlimitforscale|单SC支持的在线用户数的弹性上限|参数可选性: 任选参数类型: 数字参数范围: 0-350000默认值: 0|参数作用：该参数用于设置Communication服务弹缩时，使用的单SC支持的最大用户数。系统通过上下文比例来弹缩时，需要计算每个SC上的上下文比例即当前用户数和最大用户数的比例。
periodsyncctx|定时向UDSF同步上下文|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NEEDPERIODICSYNC|参数作用：该参数用于设置AMF是否定时向UDSF同步上下文。AMF在增、删、改上下文时，会实时向UDSF触发同步。如果某次实时同步失败，可能导致UDSF和本地的数据不一致。为了确保UDSF和本地上下文数据一致，可以开启定时同步机制，除了实时同步数据之外，AMF还会定时全量扫描本地上下文，向UDSF发起数据同步。
ctxcdbttl|上下文在UDSF上的TTL（小时）|参数可选性: 任选参数类型: 数字参数范围: 0-96默认值: 48|参数作用：该参数用于设置用户上下文在UDSF上的TTL（即Time-To-Live，有效生命时长）。如果UDSF上的用户上下文在TTL内没有得到同步刷新，UDSF会认为用户上下文已经老化失效，会对其进行删除处理。TTL设置为0表示用户上下文在UDSF上永久有效，UDSF不会对其进行删除。
命令举例 
`
查询弹性相关配置。
SHOW SCALE CONFIG:
(No.3) : SHOW SCALE CONFIG:
-----------------Namf_Communication_0----------------
操作维护       从UDSF加载上下文 用户数获取方式 预迁出群扫描速率（个/100ms） 迁出群扫描速率（个/100ms） 迁入群扫描速率（个/100ms） 单SC支持的在线用户数的弹性上限 定时向UDSF同步上下文 上下文在UDSF上的TTL（小时） 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           不加载           从资源中获取   60                           60                         1                          100000                         需要定时同步         48                          
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-08-23 17:22:32 耗时: 0.227 秒
` 
# 跟踪管理 
# 跟踪管理 
背景知识 
出于特定的目的，出于对特定目标对象的行为分析，需要跟踪相关的信令消息。 
功能说明 
跟踪管理提供了根据配置跟踪特定用户的信令消息及AMF在Trace Start消息携带MDT参数等功能。 
子主题： 
## 跟踪管理控制参数配置 
## 跟踪管理控制参数配置 
背景知识 
为了进行更精准的功能控制，需要增加配置来控制某些功能是否生效，或者配置相应的控制参数等。目前仅支持MDT路测功能控制及信令MDT功能，当需要对某些区域进行路测及下发Trace Start携带MDT参数时，使用该组命令打开控制开关。 
功能说明 
跟踪管理控制参数配置包括管理MDT功能控制开关、信令MDT功能控制开关等。 
子主题： 
### 设置跟踪管理控制参数(SET TRACEMDTPARACFG) 
### 设置跟踪管理控制参数(SET TRACEMDTPARACFG) 
功能说明 
该命令用于设置跟踪管理控制参数中的路测开关。当需要对某一区域进行路测时，使用此命令。 
命令执行成功后，当功能设置为支持且通过[ADD MDTPLMNLISTCFG]命令设置了MDT PLMN时，AMF会通过用户初始上下文建立或切换请求消息把配置的PLMNLIST带给基站。
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
manamdtfunc|支持管理MDT功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPMANAMDTFUNC|该参数表示支持管理MDT功能的开关。当设置为支持管理MDT功能，且通过ADD MDTPLMNLISTCFG命令设置了MDT PLMN时，AMF会通过用户初始上下文建立或切换请求消息把配置的PLMNLIST带给基站。Not Support Management MDT Function：不支持管理MDT功能。Support Management MDT Function：支持管理MDT功能。
sigmdtfunc|支持信令MDT功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPSIGMDTFUNC|该参数为信令MDT的功能开关。当设置为支持，且MDT功能license开启时，AMF支持下发TRACE START消息携带用户MDT参数给基站。Not Support Signalling MDT Function：不支持信令MDT功能。Support Signalling MDT Function：支持信令MDT功能。
命令举例 
`
修改支持管理MDT功能的开关为支持; 修改支持信令MDT功能的开关为支持
SET TRACEMDTPARACFG:MANAMDTFUNC="SUPPMANAMDTFUNC",SIGMDTFUNC="SUPPSIGMDTFUNC"
` 
### 查询跟踪管理控制参数(SHOW TRACEMDTPARACFG) 
### 查询跟踪管理控制参数(SHOW TRACEMDTPARACFG) 
功能说明 
该命令用于查询跟踪管理控制参数。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
manamdtfunc|支持管理MDT功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPMANAMDTFUNC|该参数表示支持管理MDT功能的开关。当设置为支持管理MDT功能，且通过ADD MDTPLMNLISTCFG命令设置了MDT PLMN时，AMF会通过用户初始上下文建立或切换请求消息把配置的PLMNLIST带给基站。Not Support Management MDT Function：不支持管理MDT功能。Support Management MDT Function：支持管理MDT功能。
sigmdtfunc|支持信令MDT功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPSIGMDTFUNC|该参数为信令MDT的功能开关。当设置为支持，且MDT功能license开启时，AMF支持下发TRACE START消息携带用户MDT参数给基站。Not Support Signalling MDT Function：不支持信令MDT功能。Support Signalling MDT Function：支持信令MDT功能。
命令举例 
`
查询支持管理MDT和信令MDT功能的开关
SHOW TRACEMDTPARACFG
(No.15) : SHOW TRACEMDTPARACFG:
-----------------Namf_Communication_0----------------
操作维护       支持管理MDT功能      支持信令MDT功能         
-----------------------------------------------------
修改           支持管理MDT功能      支持信令MDT功能  
-----------------------------------------------------
记录数：1
执行成功开始时间:2021-02-04 09:47:18 耗时: 0.131 秒
` 
## 管理MDT PLMN列表配置 
## 管理MDT PLMN列表配置 
背景知识 
MDT(Minimization of Drive Tests，最小化路测技术)功能分为基于信令MDT和基于管理MDT。 
 
基于信令MDT用于收集某些终端在网络中的测量信息。 
 
基于管理MDT用于收集进入某些特定区域所有UE的测量信息。 
 
功能说明 
该配置用于配置管理MDT功能下，AMF下发给RAN侧的PLMN列表。配置MDT PLMN列表前，应通过跟踪管理控制参数配置打开MDT开关。 
子主题： 
### 增加管理MDT的PLMN列表(ADD MDTPLMNLISTCFG) 
### 增加管理MDT的PLMN列表(ADD MDTPLMNLISTCFG) 
功能说明 
该命令用于增加管理MDT(Minimization of Drive Tests，最小化路测技术)的PLMN列表。当需要对某一区域进行路测时，使用此命令。 
命令执行成功后，AMF会通过初始上下文建立请求或切换请求消息，将配置好的管理MDT的PLMN列表带给RAN。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
命令举例 
`
增加MCC为460，MNC为111的管理MDT PLMN。
ADD MDTPLMNLISTCFG:MCC="460",MNC="111"
` 
### 删除管理MDT的PLMN列表(DEL MDTPLMNLISTCFG) 
### 删除管理MDT的PLMN列表(DEL MDTPLMNLISTCFG) 
功能说明 
该命令用于删除管理MDT的PLMN列表。当不再需要对某区域进行路测时，使用此命令。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
命令举例 
`
删除CC为460，MNC为111的管理MDT PLMN。
DEL MDTPLMNLISTCFG:MCC="460",MNC="111"
` 
### 查询管理MDT的PLMN列表(SHOW MDTPLMNLISTCFG) 
### 查询管理MDT的PLMN列表(SHOW MDTPLMNLISTCFG) 
功能说明 
该命令用于查询管理MDT的PLMN列表。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|本参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|本参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商“中国移动“在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
命令举例 
`
查询管理MDT的PLMN列表
SHOW MDTPLMNLISTCFG
(No.19) : SHOW MDTPLMNLISTCFG:
-----------------Namf_Communication_0----------------
操作维护       移动国家码 移动网络码 
-------------------------------------
复制  删除      460        111        
-------------------------------------
记录数：1
执行成功开始时间:2021-02-04 09:48:16 耗时: 0.128 秒
` 
## TCE 跟踪 
## TCE 跟踪 
背景知识 
出于特定的目的，实现全网元的信令跟踪（Trace）功能。 
功能说明 
本功能用于配置tce trace跟踪任务 
子主题： 
### 用户TCE跟踪 
### 用户TCE跟踪 
背景知识 
5GC还未实现全网元的信令跟踪（Trace）功能，尤其是无线侧必须要和AMF合作才能实现按号码跟踪,小区跟踪等维护功能。Tce Trace用于实现全网元跟踪。理论上是TCE下发跟踪任务，目前是通过本配置下发跟踪任务，由AMF网元将跟踪任务转发给其他网元，并最终各网元将需要跟踪的信令发送给TCE服务器 
功能说明 
本功能用于TCE Trace跟踪任务的具体配置。 
子主题： 
#### 新增TCE跟踪任务配置(ADD TCETRACETASKCFG) 
#### 新增TCE跟踪任务配置(ADD TCETRACETASKCFG) 
功能说明 
该命令用于增加TCE的跟踪任务。 
注意事项 
请仔细阅读每个参数的详细说明。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商"中国移动"在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
traceID|跟踪标识|参数可选性: 必选参数类型: 数字参数范围: 0-16777215|TRACEID由用户跟踪系统生成，长度为3字节的整数，目前为手动配置，mcc+mnc+traceID是跟踪任务的唯一标识。
traceTargetType|跟踪目标类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-8默认值: IMSI|该参数用于配置要跟踪的用户类型，AMF侧支持IMSI以及MSISDN的类型。0: IMSI IMSI1: IMEI IMEI2: IMEISV IMEISV3: PUB_ID Public ID4: UTRAN_CELL UTRAN_CELL5: E_UTRAN_CELL E_UTRAN_CELL6: ENB eNB7: RNC RNC8: MSISDN MSISDN
traceTargetValues|跟踪目标值|参数可选性: 必选参数类型: 字符串参数范围: 0-50|该参数用于配置要跟踪的用户，其值的类型要符合traceTargetType的定义。
traceDepth|跟踪深度|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-5默认值: MAX|该参数用于应如何在网络元素中记录详细信息，目前支持max方式的解析。0 MIN Minimum1 MED Medium2 MAX Maximum3 MINWITHOUTVEND_SPECEXT MinWithoutVendorSpecExt4 MEDWITHOUTVEND_SPECEXT MedWithoutVendorSpecExt5 MAXWITHOUTVEND_SPECEXT MaxWithoutVendorSpecExt
listOfNeTypes|跟踪网元类型|参数可选性: 必选参数类型: 数字参数范围: 0-65535|该参数用于设置网元跟踪标识值。AMF：1SMF：2PCF：4gNB-CU-UP：8gNB-CU-CP：16ng-eNB：32gNB-DU：64如果要跟踪单个网元，就输入网元对应标识值就可以，如果要跟踪多个网元请输入标识值和，例如AMF和SMF就是3，SMF和PCF和gNB-CU-CP就是22。
listOfInterfaces|跟踪接口|参数可选性: 必选参数类型: 字符串参数范围: 0-100|AMF需要跟踪的接口：N1          跟踪接口标识:1需要跟踪的接口：N2          跟踪接口标识:2需要跟踪的接口：N8          跟踪接口标识:4需要跟踪的接口：N11         跟踪接口标识:8需要跟踪的接口：N12         跟踪接口标识:16需要跟踪的接口：N14         跟踪接口标识:32需要跟踪的接口：N15         跟踪接口标识:64需要跟踪的接口：N20         跟踪接口标识:128需要跟踪的接口：N22         跟踪接口标识:256需要跟踪的接口：N26         跟踪接口标识:512SMF:需要跟踪的接口：N4         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N10        跟踪接口标识:4需要跟踪的接口：N11        跟踪接口标识:8需要跟踪的接口：S5-C       跟踪接口标识:16PCF:需要跟踪的接口：N5         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N15        跟踪接口标识:4ng-eNB/gNB-CU-CP/gNB-CU-UP/gNB-DU:需要跟踪的接口：NG-C         跟踪接口标识:1需要跟踪的接口：Xn-C/X2      跟踪接口标识:2需要跟踪的接口：Uu           跟踪接口标识:4需要跟踪的接口：F1-C         跟踪接口标识:8需要跟踪的接口：E1-C         跟踪接口标识:16如果要跟踪AMF的N1和N12接口，就是配置：1-17，如果要跟踪 AMF的N1和N12接口和ng-eNB的Uu和E1-C接口，则配置1-17&32-20，也就是‘-’前面是网元标识，‘-’后面是要跟踪的接口标识的和，&用于连接要跟踪的不同网元的接口。
triggeringEvent|跟踪触发事件|参数可选性: 必选参数类型: 字符串参数范围: 0-100|只有AMF，SMF和PCF涉及。AMF需要跟踪的流程事件：UE initiated Registration Procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated Service Request Procedure，对应的事件号标示：2需要跟踪的流程事件：N2 or Xn Handover，对应的事件号标示：4需要跟踪的流程事件：UE initiated Deregistration Procedure，对应的事件号标示：8需要跟踪的流程事件：Network initiated Deregistration Procedure，对应的事件号标示：16需要跟踪的流程事件：UE mobility from EPC，对应的事件号标示：32需要跟踪的流程事件：UE mobility to EPC，对应的事件号标示：64SMF需要跟踪的流程事件：UE initiated PDU Session Establishment procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated PDU Session Modification procedure，对应的事件号标示：2需要跟踪的流程事件：UE initiated PDU Session Release procedure，对应的事件号标示：4需要跟踪的流程事件：UE initiated PDU Session UP activation / deactivation，对应的事件号标示：8需要跟踪的流程事件：Mobility of a PDU Session between 3GPP and N3GPP access to 5GC，对应的事件号标示：16需要跟踪的流程事件：Mobility of a PDU Session from EPC，对应的事件号标示：32PCF需要跟踪的流程事件：AM Policy Control，对应的事件号标示：1需要跟踪的流程事件：SM Policy，对应的事件号标示：2需要跟踪的流程事件：Policy Authorization ，对应的事件号标示：4需要跟踪的流程事件：Background data transfer policy，对应的事件号标示：8如果要跟踪AMF前两个流程的事件，就是输入1-3，其中1是AMF的网元类型，详细见：跟踪网元类型 字段，3是前两个事件标示的和，如果要跟踪AMF前两个事件和SMF的第二个和第四个流程的事件，就是 1-3&2-10，其中2是PCF的网元类型，10是第二个事件和第三个的和，必须用&连接。
traceCollectionAddr|TCE IP 地址|参数可选性: 必选参数类型: 字符串|跟踪采集实体地址，最终收到任务的网元上传信令给这个地址。
jobtype|Job类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: TRACEONLY|参数作用：此参数用于配置trace任务的激活类型。 0：仅即时MDT（Immediate MDT only）1：仅Logged MDT（Logged MDT only）2：仅Trace（Trace only）3：即时MDT与Trace（Immediate MDT and Trace）修改影响：修改job类型，影响AMF下发给RAN的Trace Start消息中携带的字段类型。 数据来源：本端规划 默认值：仅Trace（Trace only）配置原则： 当选择Immediate MDT only、Logged MDT only、Immediate MDT and Trace时，以下参数必选，必须配置有效数据： MDT范围类型必须配置为有效值1-4。 MDT模式类型：当配置为Immediate MDT only、Immediate MDT and Trace 时，MDT模式类型必须为Immediate MDT；当配置为Logged MDT only时，MDT模式类型必须为Logged MDT。
mdtarea|MDT范围类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: INVALIDMDTAREA|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围类型。0：无效MDT范围类型1：NR CGI列表2：TAI列表 3：PLMN 4：TAC列表 修改影响：修改此参数，AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的区域范围类型会变化。 数据来源：本端规划。 默认值： 0：无效MDT范围类型。 配置原则： 该参数选择“NR CGI列表”、“TAI列表”、“TAC列表”时，需要检查“MDT范围”配置参数，包括数量、格式要求等。 该参数选择为PLMN的时候，忽略“MDT范围”配置参数。
mdtareaprofileid|MDT范围|参数可选性: 任选参数类型: 字符串参数范围: 0-600|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围，为字符串类型。修改影响：修改此参数，AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的区域范围会变化。 数据来源：本端规划。 默认值：无。 配置原则：  1当"MDT范围类型"选择"1-NR CGI list"时，配置NR CGI列表。最多配置32个，格式为: MCC-MNC-CELLID。多个使用&符分隔。比如:"460-11-123456789&460-123-101010101&462-100-444555000&460-23-987654321&461-34-202104270&461-34-202104272", 包含了6个CGI。当"MDT范围类型"选择TAI时，配置TAI列表。最多配置8个, 格式为: MCC-MNC-TAI。多个使用&符分隔。比如:"460-11-ABCDEF&460-123-222222&462-100-AAA333&460-23-C00001&461-34-11CE0A",包含了5个TAI。当"MDT范围类型"选择TAC时，配置TAC列表。最多配置8个。格式为: TAC。多个使用&符分隔。比如:"ABCDEF&222222&AAA333&C00001&11CE0A&123456&700800&A12CDB",包含了满配8个TAC。当"MDT范围类型"选择PLMN时，无需配置该参数。区域的唯一性由操作维护人员保证, 配置时需要注意, 避免重复。
mdtmode|MDT模式类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: INVAILDMDTMOD|参数作用：此参数用于配置MDT的模式。 0：无效MDT模式1：即时MDT模式2：Logged MDT模式 修改影响：此参数的修改会影响AMF下发给RAN的Trace Start消息中携带的MDT参数(NR)。数据来源：本端规划 。默认值：0：无效MDT模式。 配置原则： 当选择"即时MDT模式"的时候，必须配置"即时MDT测量结果列表"。 当选择"Logged MDT"的时候，必须配置"记录间隔"、"记录持续时间"、"Logged MDT报告类型"。
listofmeasurements|即时MDT测量结果列表|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置即时MDT的测量结果列表。此参数为复选项, 每一个BIT位标识不同的测量结果，可以全不选，也可以选择一项或多项。 修改影响：此参数的修改，影响AMF下发给RAN的Trace Start消息中携带的MDT参数(NR)中的即时MDT参数。数据来源：本端规划。 默认值：全部不选择。配置原则：选择M1的时候，必须配置“M1 报告触发器”。 选择M4的时候，必须配置“M4采集周期”、“M4记录”。选择M5的时候，必须配置“M5采集周期”、“M5记录”。选择M6的时候，必须配置“M6采集周期”、“M6记录”。选择M7的时候，必须配置“M7采集周期”、“M7记录”。
m1reportrigger|M1报告触发器|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置M1 报告触发器, 此参数为枚举复选框，但为互斥选项，即三种触发类型只能选择一个。 定期触发，对应的事件号标示：1。LTE和NR的A2 EVENT，对应的事件号标示：2。LTE和NR的A2 EVENT定期触发，对应的事件号标示：16。修改影响：此参数的修改会影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的即时MDT定位参数中的M1测量参数。 数据来源：本端规划。  默认值：不选择任何触发器类型。 配置原则：  当此参数选择"LTE和NR的A2 EVENT" 或"LTE和NR的A2 EVENT定期触发"时，必须配置有效的"M1门限类型"。 当此参数选择 "定期触发"或 "LTE和NR的A2 EVENT定期触发"时，必须配置有效的"M1 报告间隔"和"M1 报告Amount"。
m1reportinterva|M1报告间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 27-42默认值: INVALIDM1RPTINTERVA|参数作用：该参数用于配置当UE处于连接模式时，要进行的周期性测量的时间间隔。27：无效M1报告间隔28：120ms29：240 ms30：480 ms31：640 ms32：1024 ms33：2048 ms34：5120 ms35：10240 ms38：1 minute(60000 ms)39：6 minute(360000 ms)40：12 minute(720000 ms)41：30 minute(1800000 ms)42：60 minute(3600000 ms)修改影响：影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的即时MDT定位参数中的M1测量参数。数据来源：本端规划。默认值： 27：无效M1报告间隔。配置原则：当"Logged MDT报告类型"配置为"定期"(例如LTE/NR中的M1测量)，并且"Job类型"配置为"0-Immediate MDT only"或"3-Immediate MDT and Trace"时, 此参数必须配置为NR的有效值[28-42]。
m1reportamount|M1报告数目|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: AMOUNT_INVALID|参数作用：该参数用于配置定期报告的测量报告数量。0：11：22：43：84：165：326：647：无穷255：无效M1报告数量修改影响：影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的即时MDT定位参数中的M1测量参数。数据来源：本端规划。默认值：255：无效M1报告数量。配置原则：当"Logged MDT报告类型"配置为"定期"(例如LTE/NR中的M1测量和UMTS中的M1/M2测量)，并且"Job类型"配置为"0-Immediate MDT only"或"3-Immediate MDT and Trace"时, 此参数必须配置为有效值[0-7]。
m1thresholdtype|M1门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-255默认值: TYPE_INVALID|参数作用：该参数用于配置M1门限类型。 1：-RSRP2：RSRQ3：SINR255：无效M1门限类型修改影响：影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的即时MDT定位参数中的M1测量参数。数据来源：本端规划。 默认值： 255：无效M1门限类型。 配置原则：无。
rsrprsrosinr|RSRP-RSRQ-SINR数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置NR的RSRP-RSRQ-SINR数值，对应于NR，有效值范围为[0, 127]。修改影响：影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的RSRP\RSRQ\SINR值。数据来源：本端规划。默认值：0。配置原则：当配置了有效的"M1门限类型"时，必须配置此参数为有效值。参数的数值需要与M1门限类型匹配。
m4collperiod|M4采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M4COLPERIO_INVALID|参数作用：该参数用于配置在进行M4数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M4度量，应使用相同的收集周期。0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M4采集周期修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M4采集周期数值。数据来源：本端规划。默认值：255：无效M4采集周期。配置原则：当"即时MDT测量结果列表"勾选了"M4"时, 此参数必须配置为有效值[0-4]。
m4log|M4 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M4LOG_INVALID|参数作用：该参数用于配置M4 Links to Log，取值范围如下。 0：无效M4 Links to Log1：上行2：下行3：上行和下行修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M4 M4 Links to Log取值。数据来源：本端规划。 默认值： 0：无效M4 Links to Log。配置原则：当"即时MDT测量结果列表"勾选了"M4"时, 此参数必须配置为有效值[1-3]。
m5collperiod|M5采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M5COLPERIO_INVALID|参数作用：该参数用于配置在进行M5数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M5度量，应使用相同的收集周期。 0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M5采集周期修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M5采集周期数值。数据来源：本端规划 。默认值：255：无效M5采集周期。配置原则： 当"即时MDT测量结果列表"勾选了"M5"时, 此参数必须配置为有效值[0-4]。
m5log|M5 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M5LOG_INVALID|参数作用：该参数用于配置M5 Links to Log。0：无效M5 Links to Log1：上行2：下行3：上行和下行修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M5 Links to Log取值。数据来源：本端规划。 默认值： 0：无效M5 Links to Log。 配置原则： 当"即时MDT测量结果列表"勾选了"M5"时, 此参数必须配置为有效值[1-3]。
m6collperiod|M6采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M6COLPERIO_INVALID|参数作用：该参数用于配置在进行M6数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M6度量，应使用相同的收集周期。0：120ms1：240ms2：480ms3：640ms4：1024ms5：2048ms6：5120ms7：10240ms8：20480ms9：40960ms10：1minute11：6minute12：12minute13：30minute255：无效M6采集周期修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M6采集周期数值。数据来源：本端规划。 默认值：255：无效M6采集周期。配置原则：当"即时MDT测量结果列表"勾选了"M6"时, 此参数必须配置为有效值[0-13]。
m6log|M6 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M6LOG_INVALID|参数作用：该参数用于配置M6 Links to Log。0：无效M6 Links to Log1：上行2：下行3：上行和下行修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M6 Links to Log取值。数据来源：本端规划。默认值：0：无效M6 Links to Log。配置原则：当"即时MDT测量结果列表"勾选了"M6"时, 此参数必须配置为有效值[1-3]。
m7collperiod|M7采集周期|参数可选性: 任选参数类型: 数字参数范围: 0-60默认值: 0|参数作用：M7采集周期，单位为分钟，配置范围为[0, 60], 有效范围为[1, 60] , 0(min)为无效值。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M7采集周期数值。数据来源：本端规划。默认值：0：无效M7采集周期。配置原则：当"即时MDT测量结果列表"勾选了"M7"时, 此参数必须配置为有效值[1-60]。
m7log|M7 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M7LOG_INVALID|参数作用：该参数用于配置M7 Links to Log。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M7采集周期数值。数据来源：本端规划。默认值：0：无效M7 Links to Log。配置原则：当"即时MDT测量结果列表"勾选了"M7"时, 此参数必须配置为有效值[1-3]。
mdtlocinf|MDT位置信息|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：MDT位置信息，位图中的每个位置表示TS 37.320协议中定义的请求位置信息。目前第一位表示GNSS, 其他位保留供将来使用，如果收到则忽略。值"1"表示"激活", 值"0"表示"不激活"。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中是否包含位置信息。数据来源：本端规划。默认值：不勾选GNSS, 即"不激活"。配置原则：无。
bluename|蓝牙名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的蓝牙名称列表，为字符串类型。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的蓝牙列表信息。数据来源：本端规划。默认值：无 。配置原则：最多4个，使用&符隔开。每个名称最多允许输入248字符。
wlanname|WLAN名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的WLAN名称列表，为字符串类型。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的WLAN列表信息。数据来源：本端规划。默认值：无。配置原则：最多4个，使用&符隔开。每个名称最多允许输入248字符。
sensorinf|传感器信息列表|参数可选性: 任选参数类型: 字符串参数范围: 0-17|参数作用：该参数用于配置MDT的传感器信息列表，为字符串类型。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的传感器列表信息。数据来源：本端规划。默认值：无。配置原则：最多3个字符串，使用&符隔开。每个字符串按照Barometric pressure-UE speed-UE orientation模式配置。比如：0-1-0&1-0-0&0-0-1。
loginterva|记录间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGINTERVA_INVALID|参数作用：该参数定义了UE处于空闲状态时用于记录MDT测量结果的周期性，以进行周期性的下行链路导频强度测量。0：1280 ms1：2560 ms2：5120 ms3：10240 ms4：20480 ms5：30720 ms6：40960 ms7：61440 ms8：320 ms9：640 ms10：无穷255：无效记录间隔修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的记录间隔取值。数据来源：本端规划 。默认值：255：无效记录间隔 。配置原则："MDT模式类型"配置为"2-Logged MDT"时, 此参数必须配置为有效值[0-10]。
logduration|记录持续时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 6-255默认值: DURATION_INVALID|参数作用：该参数用于确定IDLE态时Logged MDT配置的有效性。定时器在UE接收到配置时启动，并且独立于UE状态迁移和RAT或RPLMN变化而运行。6：600 second7：1200 second8：2400 second9：3600 second10：5400 second11：7200 second255：无效持续记录时间修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的记录持续时间。数据来源：本端规划。默认值：255：无记录持续时间。配置原则："MDT模式类型"配置为"Logged MDT"，时此参数必须配置为有效值[6-11]。
logmdtrpttype|Logged MDT报告类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGMDTRPTTYPE_INVAL|参数作用：该参数用于配置Logged MDT报告类型。 0：定期报告。1：事件触发。255：无效Logged MDT报告类型。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中的Logged MDT报告类型及对应参数。数据来源：本端规划 。默认值：255：无效Logged MDT报告类型。配置原则：当"MDT模式类型"配置为"Logged MDT"时，此参数必须配置为有效值(0 or 1)。
eventtritype|事件触发器类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OUTOFCOVERAGE|参数作用：该参数用于配置事件触发器类型。0：超出覆盖范围。1：L1 Event。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中与事件触发类型相关的参数。数据来源：本端规划。默认值：0：超出覆盖范围。 配置原则：当本参数配置为"L1 Event"时，必须配置“滞后"和"触发的时间"且"L1事件门限类型"必须配置且为有效值。
l1thresholdtype|L1事件门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: L1THRESTYPE_INVALID|参数作用：该参数用于配置L1事件门限类型。0：RSRP。1：RSRQ。255：无效L1事件门限类型。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中与L1时间门限类型相关的参数。数据来源：本端规划 。默认值：255：无效L1事件门限类型。配置原则：当"事件触发器类型"配置为"L1 Event"时,此参数必须配置为有效值(0或1)。
rsrprsrq|RSRP/RSRQ数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置RSRP/RSRQ数值。取值范围[0, 127]。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中RSRP/RSRQ的取值。数据来源：本端规划。默认值：0。配置原则：当"L1事件门限类型"配置为"RSRP"时, 必须配置此参数。由于默认值0为有效取值，因此该配置原则是无条件支持的。
hysteresis|滞后|参数可选性: 任选参数类型: 数字参数范围: 0-30默认值: 0|参数作用：该参数用于配置事件触发报告条件的进入和离开条件。取值范围[0,30]。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中滞后时间的取值。数据来源：本端规划。默认值：0。配置原则：当"事件触发器类型"配置为"L1 Event"时, 必须配置此参数。由于默认值0为有效取值，因此该配置原则是无条件支持的。
timetrigger|触发的时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-15默认值: TIMETRIG_0MS|参数作用：该参数为触发测量报告而需要满足事件特定标准的时间 。0：0ms1：40ms2：64ms3：80ms4：100ms5：128ms6：160ms7：256ms8：320ms9：480ms10：512ms11：640ms12：1024ms13：1280ms14：2560ms15：5120ms修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中触发时间的取值。数据来源：本端规划。默认值：0：0ms。配置原则：当"事件触发器类型"配置为"L1 Event"时, 必须配置此参数。
plmnlist|PLMN列表|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：此参数用于指示允许进行测量收集、状态指示和日志报告的PLMN，它将作为plmn-IdentityList传达给UE。在NF之间，根据MDT的激活方式，它作为基于管理的MDT PLMN列表或作为基于信令的MDT PLMN列表进行通信。 修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的PlMN列表信息。数据来源：本端规划。默认值：无。配置原则：最多16个。格式要求：MCC-MNC。多个时使用&分隔。比如"460-11&142-123&460-012"。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商"中国移动"在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
traceID|跟踪标识|参数可选性: 任选参数类型: 数字参数范围: 0-16777215|TRACEID由用户跟踪系统生成，长度为3字节的整数，目前为手动配置，mcc+mnc+traceID是跟踪任务的唯一标识。
traceTargetType|跟踪目标类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-8默认值: IMSI|该参数用于配置要跟踪的用户类型，AMF侧支持IMSI以及MSISDN的类型。0: IMSI IMSI1: IMEI IMEI2: IMEISV IMEISV3: PUB_ID Public ID4: UTRAN_CELL UTRAN_CELL5: E_UTRAN_CELL E_UTRAN_CELL6: ENB eNB7: RNC RNC8: MSISDN MSISDN
traceTargetValues|跟踪目标值|参数可选性: 任选参数类型: 字符串参数范围: 0-50|该参数用于配置要跟踪的用户，其值的类型要符合traceTargetType的定义。
traceDepth|跟踪深度|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5默认值: MAX|该参数用于应如何在网络元素中记录详细信息，目前支持max方式的解析。0 MIN Minimum1 MED Medium2 MAX Maximum3 MINWITHOUTVEND_SPECEXT MinWithoutVendorSpecExt4 MEDWITHOUTVEND_SPECEXT MedWithoutVendorSpecExt5 MAXWITHOUTVEND_SPECEXT MaxWithoutVendorSpecExt
listOfNeTypes|跟踪网元类型|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置网元跟踪标识值。AMF：1SMF：2PCF：4gNB-CU-UP：8gNB-CU-CP：16ng-eNB：32gNB-DU：64如果要跟踪单个网元，就输入网元对应标识值就可以，如果要跟踪多个网元请输入标识值和，例如AMF和SMF就是3，SMF和PCF和gNB-CU-CP就是22。
listOfInterfaces|跟踪接口|参数可选性: 任选参数类型: 字符串参数范围: 0-100|AMF需要跟踪的接口：N1          跟踪接口标识:1需要跟踪的接口：N2          跟踪接口标识:2需要跟踪的接口：N8          跟踪接口标识:4需要跟踪的接口：N11         跟踪接口标识:8需要跟踪的接口：N12         跟踪接口标识:16需要跟踪的接口：N14         跟踪接口标识:32需要跟踪的接口：N15         跟踪接口标识:64需要跟踪的接口：N20         跟踪接口标识:128需要跟踪的接口：N22         跟踪接口标识:256需要跟踪的接口：N26         跟踪接口标识:512SMF:需要跟踪的接口：N4         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N10        跟踪接口标识:4需要跟踪的接口：N11        跟踪接口标识:8需要跟踪的接口：S5-C       跟踪接口标识:16PCF:需要跟踪的接口：N5         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N15        跟踪接口标识:4ng-eNB/gNB-CU-CP/gNB-CU-UP/gNB-DU:需要跟踪的接口：NG-C         跟踪接口标识:1需要跟踪的接口：Xn-C/X2      跟踪接口标识:2需要跟踪的接口：Uu           跟踪接口标识:4需要跟踪的接口：F1-C         跟踪接口标识:8需要跟踪的接口：E1-C         跟踪接口标识:16如果要跟踪AMF的N1和N12接口，就是配置：1-17，如果要跟踪 AMF的N1和N12接口和ng-eNB的Uu和E1-C接口，则配置1-17&32-20，也就是‘-’前面是网元标识，‘-’后面是要跟踪的接口标识的和，&用于连接要跟踪的不同网元的接口。
triggeringEvent|跟踪触发事件|参数可选性: 任选参数类型: 字符串参数范围: 0-100|只有AMF，SMF和PCF涉及。AMF需要跟踪的流程事件：UE initiated Registration Procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated Service Request Procedure，对应的事件号标示：2需要跟踪的流程事件：N2 or Xn Handover，对应的事件号标示：4需要跟踪的流程事件：UE initiated Deregistration Procedure，对应的事件号标示：8需要跟踪的流程事件：Network initiated Deregistration Procedure，对应的事件号标示：16需要跟踪的流程事件：UE mobility from EPC，对应的事件号标示：32需要跟踪的流程事件：UE mobility to EPC，对应的事件号标示：64SMF需要跟踪的流程事件：UE initiated PDU Session Establishment procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated PDU Session Modification procedure，对应的事件号标示：2需要跟踪的流程事件：UE initiated PDU Session Release procedure，对应的事件号标示：4需要跟踪的流程事件：UE initiated PDU Session UP activation / deactivation，对应的事件号标示：8需要跟踪的流程事件：Mobility of a PDU Session between 3GPP and N3GPP access to 5GC，对应的事件号标示：16需要跟踪的流程事件：Mobility of a PDU Session from EPC，对应的事件号标示：32PCF需要跟踪的流程事件：AM Policy Control，对应的事件号标示：1需要跟踪的流程事件：SM Policy，对应的事件号标示：2需要跟踪的流程事件：Policy Authorization ，对应的事件号标示：4需要跟踪的流程事件：Background data transfer policy，对应的事件号标示：8如果要跟踪AMF前两个流程的事件，就是输入1-3，其中1是AMF的网元类型，详细见：跟踪网元类型 字段，3是前两个事件标示的和，如果要跟踪AMF前两个事件和SMF的第二个和第四个流程的事件，就是 1-3&2-10，其中2是PCF的网元类型，10是第二个事件和第三个的和，必须用&连接。
traceCollectionAddr|TCE IP 地址|参数可选性: 任选参数类型: 字符串|跟踪采集实体地址，最终收到任务的网元上传信令给这个地址。
jobtype|Job类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: TRACEONLY|参数作用：此参数用于配置trace任务的激活类型。 0：仅即时MDT（Immediate MDT only）1：仅Logged MDT（Logged MDT only）2：仅Trace（Trace only）3：即时MDT与Trace（Immediate MDT and Trace）
mdtarea|MDT范围类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: INVALIDMDTAREA|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围类型。0：无效MDT范围类型1：NR CGI列表2：TAI列表 3：PLMN 4：TAC列表
mdtareaprofileid|MDT范围|参数可选性: 任选参数类型: 字符串参数范围: 0-600|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围，为字符串类型。
mdtmode|MDT模式类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: INVAILDMDTMOD|参数作用：此参数用于配置MDT的模式。 0：无效MDT模式1：即时MDT模式2：Logged MDT模式
listofmeasurements|即时MDT测量结果列表|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置即时MDT的测量结果列表。此参数为复选项, 每一个BIT位标识不同的测量结果，可以全不选，也可以选择一项或多项。
m1reportrigger|M1报告触发器|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置M1 报告触发器, 此参数为枚举复选框，但为互斥选项，即三种触发类型只能选择一个。 定期触发，对应的事件号标示：1。LTE和NR的A2 EVENT，对应的事件号标示：2。LTE和NR的A2 EVENT定期触发，对应的事件号标示：16。
m1reportinterva|M1报告间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 27-42默认值: INVALIDM1RPTINTERVA|参数作用：该参数用于配置当UE处于连接模式时，要进行的周期性测量的时间间隔。27：无效M1报告间隔28：120ms29：240 ms30：480 ms31：640 ms32：1024 ms33：2048 ms34：5120 ms35：10240 ms38：1 minute(60000 ms)39：6 minute(360000 ms)40：12 minute(720000 ms)41：30 minute(1800000 ms)42：60 minute(3600000 ms)
m1reportamount|M1报告数目|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: AMOUNT_INVALID|参数作用：该参数用于配置定期报告的测量报告数量。0：11：22：43：84：165：326：647：无穷255：无效M1报告数量
m1thresholdtype|M1门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-255默认值: TYPE_INVALID|参数作用：该参数用于配置M1门限类型。 1：-RSRP2：RSRQ3：SINR255：无效M1门限类型
rsrprsrosinr|RSRP-RSRQ-SINR数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置NR的RSRP-RSRQ-SINR数值，对应于NR，有效值范围为[0, 127]。
m4collperiod|M4采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M4COLPERIO_INVALID|参数作用：该参数用于配置在进行M4数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M4度量，应使用相同的收集周期。0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M4采集周期
m4log|M4 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M4LOG_INVALID|参数作用：该参数用于配置M4 Links to Log，取值范围如下。 0：无效M4 Links to Log1：上行2：下行3：上行和下行
m5collperiod|M5采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M5COLPERIO_INVALID|参数作用：该参数用于配置在进行M5数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M5度量，应使用相同的收集周期。 0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M5采集周期
m5log|M5 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M5LOG_INVALID|参数作用：该参数用于配置M5 Links to Log。0：无效M5 Links to Log1：上行2：下行3：上行和下行
m6collperiod|M6采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M6COLPERIO_INVALID|参数作用：该参数用于配置在进行M6数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M6度量，应使用相同的收集周期。0：120ms1：240ms2：480ms3：640ms4：1024ms5：2048ms6：5120ms7：10240ms8：20480ms9：40960ms10：1minute11：6minute12：12minute13：30minute255：无效M6采集周期
m6log|M6 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M6LOG_INVALID|参数作用：该参数用于配置M6 Links to Log。0：无效M6 Links to Log1：上行2：下行3：上行和下行
m7collperiod|M7采集周期|参数可选性: 任选参数类型: 数字参数范围: 0-60默认值: 0|参数作用：M7采集周期，单位为分钟，配置范围为[0, 60], 有效范围为[1, 60] , 0(min)为无效值。
m7log|M7 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M7LOG_INVALID|参数作用：该参数用于配置M7 Links to Log。
mdtlocinf|MDT位置信息|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：MDT位置信息，位图中的每个位置表示TS 37.320协议中定义的请求位置信息。目前第一位表示GNSS, 其他位保留供将来使用，如果收到则忽略。值"1"表示"激活", 值"0"表示"不激活"。
bluename|蓝牙名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的蓝牙名称列表，为字符串类型。
wlanname|WLAN名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的WLAN名称列表，为字符串类型。
sensorinf|传感器信息列表|参数可选性: 任选参数类型: 字符串参数范围: 0-17|参数作用：该参数用于配置MDT的传感器信息列表，为字符串类型。
loginterva|记录间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGINTERVA_INVALID|参数作用：该参数定义了UE处于空闲状态时用于记录MDT测量结果的周期性，以进行周期性的下行链路导频强度测量。0：1280 ms1：2560 ms2：5120 ms3：10240 ms4：20480 ms5：30720 ms6：40960 ms7：61440 ms8：320 ms9：640 ms10：无穷255：无效记录间隔
logduration|记录持续时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 6-255默认值: DURATION_INVALID|参数作用：该参数用于确定IDLE态时Logged MDT配置的有效性。定时器在UE接收到配置时启动，并且独立于UE状态迁移和RAT或RPLMN变化而运行。6：600 second7：1200 second8：2400 second9：3600 second10：5400 second11：7200 second255：无效持续记录时间
logmdtrpttype|Logged MDT报告类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGMDTRPTTYPE_INVAL|参数作用：该参数用于配置Logged MDT报告类型。 0：定期报告。1：事件触发。255：无效Logged MDT报告类型。
eventtritype|事件触发器类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OUTOFCOVERAGE|参数作用：该参数用于配置事件触发器类型。0：超出覆盖范围。1：L1 Event。
l1thresholdtype|L1事件门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: L1THRESTYPE_INVALID|参数作用：该参数用于配置L1事件门限类型。0：RSRP。1：RSRQ。255：无效L1事件门限类型。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中与L1时间门限类型相关的参数。数据来源：本端规划 。默认值：255：无效L1事件门限类型。配置原则：当"事件触发器类型"配置为"L1 Event"时,此参数必须配置为有效值(0或1)。
rsrprsrq|RSRP/RSRQ数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置RSRP/RSRQ数值。取值范围[0, 127]。
hysteresis|滞后|参数可选性: 任选参数类型: 数字参数范围: 0-30默认值: 0|参数作用：该参数用于配置事件触发报告条件的进入和离开条件。取值范围[0,30]。
timetrigger|触发的时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-15默认值: TIMETRIG_0MS|参数作用：该参数为触发测量报告而需要满足事件特定标准的时间 。0：0ms1：40ms2：64ms3：80ms4：100ms5：128ms6：160ms7：256ms8：320ms9：480ms10：512ms11：640ms12：1024ms13：1280ms14：2560ms15：5120ms
plmnlist|PLMN列表|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：此参数用于指示允许进行测量收集、状态指示和日志报告的PLMN，它将作为plmn-IdentityList传达给UE。在NF之间，根据MDT的激活方式，它作为基于管理的MDT PLMN列表或作为基于信令的MDT PLMN列表进行通信。
命令举例 
`
新增移动国家码为460，移动网络码为1，跟踪标示为1跟踪任务，用户类型为IMSI，IMSI值为460119990010005，要跟踪AMF网元，跟踪N1口，跟踪初始注册，最终任务上报给地址为2.2.2.2的TCE服务器。MDT job类型为即时MDT, 其它MDT参数按即时MDT配置原则配置。
ADD TCETRACETASKCFG:MCC="460",MNC="01",TRACEID=1,TRACETARGETTYPE="IMSI",TRACETARGETVALUES="460119990010005",TRACEDEPTH="MAX",LISTOFNETYPES=1,LISTOFINTERFACES="1-1",TRIGGERINGEVENT="1-1",TRACECOLLECTIONADDR=2.2.2.2,JOBTYPE="IMMEDIATEMDTONLY",MDTAREA="PLMN",MDTMODE="IMMEDIATEMDTMOD",LISTOFMEASUREMENTS="IMMEMDTMEASLIST_M1"&"IMMEMDTMEASLIST_M5"&"IMMEMDTMEASLIST_M7"&"IMMEMDTMEASLIST_M4",M1REPORTRIGGER="PERIODICAL",M1REPORTINTERVA="640MS",M1REPORTAMOUNT="AMOUNT_32",M1THRESHOLDTYPE="TYPE_RSRP",RSRPRSROSINR=32,M4COLLPERIOD="M4COLPERIO_2048MS",M4LOG="M4LOG_UP_DOWN_LINK",M5COLLPERIOD="M5COLPERIO_1MINUTE",M5LOG="M5LOG_UP_DOWN_LINK",M6COLLPERIOD="M6COLPERIO_640MS",M6LOG="M6LOG_DOWNLINK",M7COLLPERIOD=10,M7LOG="M7LOG_UP_DOWN_LINK",MDTLOCINF="GNSS",BLUENAME="zte.bluetooth001&zte.com.blue002",WLANNAME="ztewlan001&zteWlan002",SENSORINF="0-1-0&1-0-0",LOGINTERVA="LOGINTERVA_1280MS",LOGDURATION="DURATION_2400S",LOGMDTRPTTYPE="LOGMDTRPTTYPE_PERIO",EVENTTRITYPE="L1EVENT",L1THRESHOLDTYPE="L1THRESTYPE_RSRQ",RSRPRSRQ=22,HYSTERESIS=23,TIMETRIGGER="TIMETRIG_40MS",PLMNLIST="460-11&460-123"
` 
#### 修改TCE跟踪任务配置(SET TCETRACETASKCFG) 
#### 修改TCE跟踪任务配置(SET TCETRACETASKCFG) 
功能说明 
该命令用于修改已经配置成功的TCE的跟踪任务。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商"中国移动"在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
traceID|跟踪标识|参数可选性: 必选参数类型: 数字参数范围: 0-16777215|TRACEID由用户跟踪系统生成，长度为3字节的整数，目前为手动配置，mcc+mnc+traceID是跟踪任务的唯一标识。
traceTargetType|跟踪目标类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-8默认值: IMSI|该参数用于配置要跟踪的用户类型，AMF侧支持IMSI以及MSISDN的类型。0: IMSI IMSI1: IMEI IMEI2: IMEISV IMEISV3: PUB_ID Public ID4: UTRAN_CELL UTRAN_CELL5: E_UTRAN_CELL E_UTRAN_CELL6: ENB eNB7: RNC RNC8: MSISDN MSISDN
traceTargetValues|跟踪目标值|参数可选性: 任选参数类型: 字符串参数范围: 0-50|该参数用于配置要跟踪的用户，其值的类型要符合traceTargetType的定义。
traceDepth|跟踪深度|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5默认值: MAX|该参数用于应如何在网络元素中记录详细信息，目前支持max方式的解析。0 MIN Minimum1 MED Medium2 MAX Maximum3 MINWITHOUTVEND_SPECEXT MinWithoutVendorSpecExt4 MEDWITHOUTVEND_SPECEXT MedWithoutVendorSpecExt5 MAXWITHOUTVEND_SPECEXT MaxWithoutVendorSpecExt
listOfNeTypes|跟踪网元类型|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置网元跟踪标识值。AMF：1SMF：2PCF：4gNB-CU-UP：8gNB-CU-CP：16ng-eNB：32gNB-DU：64如果要跟踪单个网元，就输入网元对应标识值就可以，如果要跟踪多个网元请输入标识值和，例如AMF和SMF就是3，SMF和PCF和gNB-CU-CP就是22。
listOfInterfaces|跟踪接口|参数可选性: 任选参数类型: 字符串参数范围: 0-100|AMF需要跟踪的接口：N1          跟踪接口标识:1需要跟踪的接口：N2          跟踪接口标识:2需要跟踪的接口：N8          跟踪接口标识:4需要跟踪的接口：N11         跟踪接口标识:8需要跟踪的接口：N12         跟踪接口标识:16需要跟踪的接口：N14         跟踪接口标识:32需要跟踪的接口：N15         跟踪接口标识:64需要跟踪的接口：N20         跟踪接口标识:128需要跟踪的接口：N22         跟踪接口标识:256需要跟踪的接口：N26         跟踪接口标识:512SMF:需要跟踪的接口：N4         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N10        跟踪接口标识:4需要跟踪的接口：N11        跟踪接口标识:8需要跟踪的接口：S5-C       跟踪接口标识:16PCF:需要跟踪的接口：N5         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N15        跟踪接口标识:4ng-eNB/gNB-CU-CP/gNB-CU-UP/gNB-DU:需要跟踪的接口：NG-C         跟踪接口标识:1需要跟踪的接口：Xn-C/X2      跟踪接口标识:2需要跟踪的接口：Uu           跟踪接口标识:4需要跟踪的接口：F1-C         跟踪接口标识:8需要跟踪的接口：E1-C         跟踪接口标识:16如果要跟踪AMF的N1和N12接口，就是配置：1-17，如果要跟踪 AMF的N1和N12接口和ng-eNB的Uu和E1-C接口，则配置1-17&32-20，也就是‘-’前面是网元标识，‘-’后面是要跟踪的接口标识的和，&用于连接要跟踪的不同网元的接口。
triggeringEvent|跟踪触发事件|参数可选性: 任选参数类型: 字符串参数范围: 0-100|只有AMF，SMF和PCF涉及。AMF需要跟踪的流程事件：UE initiated Registration Procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated Service Request Procedure，对应的事件号标示：2需要跟踪的流程事件：N2 or Xn Handover，对应的事件号标示：4需要跟踪的流程事件：UE initiated Deregistration Procedure，对应的事件号标示：8需要跟踪的流程事件：Network initiated Deregistration Procedure，对应的事件号标示：16需要跟踪的流程事件：UE mobility from EPC，对应的事件号标示：32需要跟踪的流程事件：UE mobility to EPC，对应的事件号标示：64SMF需要跟踪的流程事件：UE initiated PDU Session Establishment procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated PDU Session Modification procedure，对应的事件号标示：2需要跟踪的流程事件：UE initiated PDU Session Release procedure，对应的事件号标示：4需要跟踪的流程事件：UE initiated PDU Session UP activation / deactivation，对应的事件号标示：8需要跟踪的流程事件：Mobility of a PDU Session between 3GPP and N3GPP access to 5GC，对应的事件号标示：16需要跟踪的流程事件：Mobility of a PDU Session from EPC，对应的事件号标示：32PCF需要跟踪的流程事件：AM Policy Control，对应的事件号标示：1需要跟踪的流程事件：SM Policy，对应的事件号标示：2需要跟踪的流程事件：Policy Authorization ，对应的事件号标示：4需要跟踪的流程事件：Background data transfer policy，对应的事件号标示：8如果要跟踪AMF前两个流程的事件，就是输入1-3，其中1是AMF的网元类型，详细见：跟踪网元类型 字段，3是前两个事件标示的和，如果要跟踪AMF前两个事件和SMF的第二个和第四个流程的事件，就是 1-3&2-10，其中2是PCF的网元类型，10是第二个事件和第三个的和，必须用&连接。
traceCollectionAddr|TCE IP 地址|参数可选性: 任选参数类型: 字符串|跟踪采集实体地址，最终收到任务的网元上传信令给这个地址。
jobtype|Job类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: TRACEONLY|参数作用：此参数用于配置trace任务的激活类型。 0：仅即时MDT（Immediate MDT only）1：仅Logged MDT（Logged MDT only）2：仅Trace（Trace only）3：即时MDT与Trace（Immediate MDT and Trace）修改影响：修改job类型，影响AMF下发给RAN的Trace Start消息中携带的字段类型。 数据来源：本端规划 默认值：仅Trace（Trace only）配置原则： 当选择Immediate MDT only、Logged MDT only、Immediate MDT and Trace时，以下参数必选，必须配置有效数据： MDT范围类型必须配置为有效值1-4。 MDT模式类型：当配置为Immediate MDT only、Immediate MDT and Trace 时，MDT模式类型必须为Immediate MDT；当配置为Logged MDT only时，MDT模式类型必须为Logged MDT。
mdtarea|MDT范围类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: INVALIDMDTAREA|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围类型。0：无效MDT范围类型1：NR CGI列表2：TAI列表 3：PLMN 4：TAC列表 修改影响：修改此参数，AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的区域范围类型会变化。 数据来源：本端规划。 默认值： 0：无效MDT范围类型。 配置原则： 该参数选择“NR CGI列表”、“TAI列表”、“TAC列表”时，需要检查“MDT范围”配置参数，包括数量、格式要求等。 该参数选择为PLMN的时候，忽略“MDT范围”配置参数。
mdtareaprofileid|MDT范围|参数可选性: 任选参数类型: 字符串参数范围: 0-600|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围，为字符串类型。修改影响：修改此参数，AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的区域范围会变化。 数据来源：本端规划。 默认值：无。 配置原则：  1当"MDT范围类型"选择"1-NR CGI list"时，配置NR CGI列表。最多配置32个，格式为: MCC-MNC-CELLID。多个使用&符分隔。比如:"460-11-123456789&460-123-101010101&462-100-444555000&460-23-987654321&461-34-202104270&461-34-202104272", 包含了6个CGI。当"MDT范围类型"选择TAI时，配置TAI列表。最多配置8个, 格式为: MCC-MNC-TAI。多个使用&符分隔。比如:"460-11-ABCDEF&460-123-222222&462-100-AAA333&460-23-C00001&461-34-11CE0A",包含了5个TAI。当"MDT范围类型"选择TAC时，配置TAC列表。最多配置8个。格式为: TAC。多个使用&符分隔。比如:"ABCDEF&222222&AAA333&C00001&11CE0A&123456&700800&A12CDB",包含了满配8个TAC。当"MDT范围类型"选择PLMN时，无需配置该参数。区域的唯一性由操作维护人员保证, 配置时需要注意, 避免重复。
mdtmode|MDT模式类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: INVAILDMDTMOD|参数作用：此参数用于配置MDT的模式。 0：无效MDT模式1：即时MDT模式2：Logged MDT模式 修改影响：此参数的修改会影响AMF下发给RAN的Trace Start消息中携带的MDT参数(NR)。数据来源：本端规划 。默认值：0：无效MDT模式。 配置原则： 当选择"即时MDT模式"的时候，必须配置"即时MDT测量结果列表"。 当选择"Logged MDT"的时候，必须配置"记录间隔"、"记录持续时间"、"Logged MDT报告类型"。
listofmeasurements|即时MDT测量结果列表|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置即时MDT的测量结果列表。此参数为复选项, 每一个BIT位标识不同的测量结果，可以全不选，也可以选择一项或多项。 修改影响：此参数的修改，影响AMF下发给RAN的Trace Start消息中携带的MDT参数(NR)中的即时MDT参数。数据来源：本端规划。 默认值：全部不选择。配置原则：选择M1的时候，必须配置“M1 报告触发器”。 选择M4的时候，必须配置“M4采集周期”、“M4记录”。选择M5的时候，必须配置“M5采集周期”、“M5记录”。选择M6的时候，必须配置“M6采集周期”、“M6记录”。选择M7的时候，必须配置“M7采集周期”、“M7记录”。
m1reportrigger|M1报告触发器|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置M1 报告触发器, 此参数为枚举复选框，但为互斥选项，即三种触发类型只能选择一个。 定期触发，对应的事件号标示：1。LTE和NR的A2 EVENT，对应的事件号标示：2。LTE和NR的A2 EVENT定期触发，对应的事件号标示：16。修改影响：此参数的修改会影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的即时MDT定位参数中的M1测量参数。 数据来源：本端规划。  默认值：不选择任何触发器类型。 配置原则：  当此参数选择"LTE和NR的A2 EVENT" 或"LTE和NR的A2 EVENT定期触发"时，必须配置有效的"M1门限类型"。 当此参数选择 "定期触发"或 "LTE和NR的A2 EVENT定期触发"时，必须配置有效的"M1 报告间隔"和"M1 报告Amount"。
m1reportinterva|M1报告间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 27-42默认值: INVALIDM1RPTINTERVA|参数作用：该参数用于配置当UE处于连接模式时，要进行的周期性测量的时间间隔。27：无效M1报告间隔28：120ms29：240 ms30：480 ms31：640 ms32：1024 ms33：2048 ms34：5120 ms35：10240 ms38：1 minute(60000 ms)39：6 minute(360000 ms)40：12 minute(720000 ms)41：30 minute(1800000 ms)42：60 minute(3600000 ms)修改影响：影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的即时MDT定位参数中的M1测量参数。数据来源：本端规划。默认值： 27：无效M1报告间隔。配置原则：当"Logged MDT报告类型"配置为"定期"(例如LTE/NR中的M1测量)，并且"Job类型"配置为"0-Immediate MDT only"或"3-Immediate MDT and Trace"时, 此参数必须配置为NR的有效值[28-42]。
m1reportamount|M1报告数目|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: AMOUNT_INVALID|参数作用：该参数用于配置定期报告的测量报告数量。0：11：22：43：84：165：326：647：无穷255：无效M1报告数量修改影响：影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的即时MDT定位参数中的M1测量参数。数据来源：本端规划。默认值：255：无效M1报告数量。配置原则：当"Logged MDT报告类型"配置为"定期"(例如LTE/NR中的M1测量和UMTS中的M1/M2测量)，并且"Job类型"配置为"0-Immediate MDT only"或"3-Immediate MDT and Trace"时, 此参数必须配置为有效值[0-7]。
m1thresholdtype|M1门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-255默认值: TYPE_INVALID|参数作用：该参数用于配置M1门限类型。 1：-RSRP2：RSRQ3：SINR255：无效M1门限类型修改影响：影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的即时MDT定位参数中的M1测量参数。数据来源：本端规划。 默认值： 255：无效M1门限类型。 配置原则：无。
rsrprsrosinr|RSRP-RSRQ-SINR数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置NR的RSRP-RSRQ-SINR数值，对应于NR，有效值范围为[0, 127]。修改影响：影响AMF下发给RAN的Trace Start消息中的MDT参数(NR)中的RSRP\RSRQ\SINR值。数据来源：本端规划。默认值：0。配置原则：当配置了有效的"M1门限类型"时，必须配置此参数为有效值。参数的数值需要与M1门限类型匹配。
m4collperiod|M4采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M4COLPERIO_INVALID|参数作用：该参数用于配置在进行M4数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M4度量，应使用相同的收集周期。0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M4采集周期修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M4采集周期数值。数据来源：本端规划。默认值：255：无效M4采集周期。配置原则：当"即时MDT测量结果列表"勾选了"M4"时, 此参数必须配置为有效值[0-4]。
m4log|M4 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M4LOG_INVALID|参数作用：该参数用于配置M4 Links to Log，取值范围如下。 0：无效M4 Links to Log1：上行2：下行3：上行和下行修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M4 M4 Links to Log取值。数据来源：本端规划。 默认值： 0：无效M4 Links to Log。配置原则：当"即时MDT测量结果列表"勾选了"M4"时, 此参数必须配置为有效值[1-3]。
m5collperiod|M5采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M5COLPERIO_INVALID|参数作用：该参数用于配置在进行M5数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M5度量，应使用相同的收集周期。 0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M5采集周期修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M5采集周期数值。数据来源：本端规划 。默认值：255：无效M5采集周期。配置原则： 当"即时MDT测量结果列表"勾选了"M5"时, 此参数必须配置为有效值[0-4]。
m5log|M5 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M5LOG_INVALID|参数作用：该参数用于配置M5 Links to Log。0：无效M5 Links to Log1：上行2：下行3：上行和下行修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M5 Links to Log取值。数据来源：本端规划。 默认值： 0：无效M5 Links to Log。 配置原则： 当"即时MDT测量结果列表"勾选了"M5"时, 此参数必须配置为有效值[1-3]。
m6collperiod|M6采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M6COLPERIO_INVALID|参数作用：该参数用于配置在进行M6数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M6度量，应使用相同的收集周期。0：120ms1：240ms2：480ms3：640ms4：1024ms5：2048ms6：5120ms7：10240ms8：20480ms9：40960ms10：1minute11：6minute12：12minute13：30minute255：无效M6采集周期修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M6采集周期数值。数据来源：本端规划。 默认值：255：无效M6采集周期。配置原则：当"即时MDT测量结果列表"勾选了"M6"时, 此参数必须配置为有效值[0-13]。
m6log|M6 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M6LOG_INVALID|参数作用：该参数用于配置M6 Links to Log。0：无效M6 Links to Log1：上行2：下行3：上行和下行修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M6 Links to Log取值。数据来源：本端规划。默认值：0：无效M6 Links to Log。配置原则：当"即时MDT测量结果列表"勾选了"M6"时, 此参数必须配置为有效值[1-3]。
m7collperiod|M7采集周期|参数可选性: 任选参数类型: 数字参数范围: 0-60默认值: 0|参数作用：M7采集周期，单位为分钟，配置范围为[0, 60], 有效范围为[1, 60] , 0(min)为无效值。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M7采集周期数值。数据来源：本端规划。默认值：0：无效M7采集周期。配置原则：当"即时MDT测量结果列表"勾选了"M7"时, 此参数必须配置为有效值[1-60]。
m7log|M7 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M7LOG_INVALID|参数作用：该参数用于配置M7 Links to Log。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的M7采集周期数值。数据来源：本端规划。默认值：0：无效M7 Links to Log。配置原则：当"即时MDT测量结果列表"勾选了"M7"时, 此参数必须配置为有效值[1-3]。
mdtlocinf|MDT位置信息|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：MDT位置信息，位图中的每个位置表示TS 37.320协议中定义的请求位置信息。目前第一位表示GNSS, 其他位保留供将来使用，如果收到则忽略。值"1"表示"激活", 值"0"表示"不激活"。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中是否包含位置信息。数据来源：本端规划。默认值：不勾选GNSS, 即"不激活"。配置原则：无。
bluename|蓝牙名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的蓝牙名称列表，为字符串类型。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的蓝牙列表信息。数据来源：本端规划。默认值：无 。配置原则：最多4个，使用&符隔开。每个名称最多允许输入248字符。
wlanname|WLAN名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的WLAN名称列表，为字符串类型。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的WLAN列表信息。数据来源：本端规划。默认值：无。配置原则：最多4个，使用&符隔开。每个名称最多允许输入248字符。
sensorinf|传感器信息列表|参数可选性: 任选参数类型: 字符串参数范围: 0-17|参数作用：该参数用于配置MDT的传感器信息列表，为字符串类型。修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的传感器列表信息。数据来源：本端规划。默认值：无。配置原则：最多3个字符串，使用&符隔开。每个字符串按照Barometric pressure-UE speed-UE orientation模式配置。比如：0-1-0&1-0-0&0-0-1。
loginterva|记录间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGINTERVA_INVALID|参数作用：该参数定义了UE处于空闲状态时用于记录MDT测量结果的周期性，以进行周期性的下行链路导频强度测量。0：1280 ms1：2560 ms2：5120 ms3：10240 ms4：20480 ms5：30720 ms6：40960 ms7：61440 ms8：320 ms9：640 ms10：无穷255：无效记录间隔修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的记录间隔取值。数据来源：本端规划 。默认值：255：无效记录间隔 。配置原则："MDT模式类型"配置为"2-Logged MDT"时, 此参数必须配置为有效值[0-10]。
logduration|记录持续时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 6-255默认值: DURATION_INVALID|参数作用：该参数用于确定IDLE态时Logged MDT配置的有效性。定时器在UE接收到配置时启动，并且独立于UE状态迁移和RAT或RPLMN变化而运行。6：600 second7：1200 second8：2400 second9：3600 second10：5400 second11：7200 second255：无效持续记录时间修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的记录持续时间。数据来源：本端规划。默认值：255：无记录持续时间。配置原则："MDT模式类型"配置为"Logged MDT"，时此参数必须配置为有效值[6-11]。
logmdtrpttype|Logged MDT报告类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGMDTRPTTYPE_INVAL|参数作用：该参数用于配置Logged MDT报告类型。 0：定期报告。1：事件触发。255：无效Logged MDT报告类型。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中的Logged MDT报告类型及对应参数。数据来源：本端规划 。默认值：255：无效Logged MDT报告类型。配置原则：当"MDT模式类型"配置为"Logged MDT"时，此参数必须配置为有效值(0 or 1)。
eventtritype|事件触发器类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OUTOFCOVERAGE|参数作用：该参数用于配置事件触发器类型。0：超出覆盖范围。1：L1 Event。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中与事件触发类型相关的参数。数据来源：本端规划。默认值：0：超出覆盖范围。 配置原则：当本参数配置为"L1 Event"时，必须配置“滞后"和"触发的时间"且"L1事件门限类型"必须配置且为有效值。
l1thresholdtype|L1事件门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: L1THRESTYPE_INVALID|参数作用：该参数用于配置L1事件门限类型。0：RSRP。1：RSRQ。255：无效L1事件门限类型。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中与L1时间门限类型相关的参数。数据来源：本端规划 。默认值：255：无效L1事件门限类型。配置原则：当"事件触发器类型"配置为"L1 Event"时,此参数必须配置为有效值(0或1)。
rsrprsrq|RSRP/RSRQ数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置RSRP/RSRQ数值。取值范围[0, 127]。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中RSRP/RSRQ的取值。数据来源：本端规划。默认值：0。配置原则：当"L1事件门限类型"配置为"RSRP"时, 必须配置此参数。由于默认值0为有效取值，因此该配置原则是无条件支持的。
hysteresis|滞后|参数可选性: 任选参数类型: 数字参数范围: 0-30默认值: 0|参数作用：该参数用于配置事件触发报告条件的进入和离开条件。取值范围[0,30]。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中滞后时间的取值。数据来源：本端规划。默认值：0。配置原则：当"事件触发器类型"配置为"L1 Event"时, 必须配置此参数。由于默认值0为有效取值，因此该配置原则是无条件支持的。
timetrigger|触发的时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-15默认值: TIMETRIG_0MS|参数作用：该参数为触发测量报告而需要满足事件特定标准的时间 。0：0ms1：40ms2：64ms3：80ms4：100ms5：128ms6：160ms7：256ms8：320ms9：480ms10：512ms11：640ms12：1024ms13：1280ms14：2560ms15：5120ms修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中触发时间的取值。数据来源：本端规划。默认值：0：0ms。配置原则：当"事件触发器类型"配置为"L1 Event"时, 必须配置此参数。
plmnlist|PLMN列表|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：此参数用于指示允许进行测量收集、状态指示和日志报告的PLMN，它将作为plmn-IdentityList传达给UE。在NF之间，根据MDT的激活方式，它作为基于管理的MDT PLMN列表或作为基于信令的MDT PLMN列表进行通信。 修改影响：影响AMF下发给RAN的Trace Start消息携带的MDT参数(NR)中的PlMN列表信息。数据来源：本端规划。默认值：无。配置原则：最多16个。格式要求：MCC-MNC。多个时使用&分隔。比如"460-11&142-123&460-012"。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商"中国移动"在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
traceID|跟踪标识|参数可选性: 任选参数类型: 数字参数范围: 0-16777215|TRACEID由用户跟踪系统生成，长度为3字节的整数，目前为手动配置，mcc+mnc+traceID是跟踪任务的唯一标识。
traceTargetType|跟踪目标类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-8默认值: IMSI|该参数用于配置要跟踪的用户类型，AMF侧支持IMSI以及MSISDN的类型。0: IMSI IMSI1: IMEI IMEI2: IMEISV IMEISV3: PUB_ID Public ID4: UTRAN_CELL UTRAN_CELL5: E_UTRAN_CELL E_UTRAN_CELL6: ENB eNB7: RNC RNC8: MSISDN MSISDN
traceTargetValues|跟踪目标值|参数可选性: 任选参数类型: 字符串参数范围: 0-50|该参数用于配置要跟踪的用户，其值的类型要符合traceTargetType的定义。
traceDepth|跟踪深度|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5默认值: MAX|该参数用于应如何在网络元素中记录详细信息，目前支持max方式的解析。0 MIN Minimum1 MED Medium2 MAX Maximum3 MINWITHOUTVEND_SPECEXT MinWithoutVendorSpecExt4 MEDWITHOUTVEND_SPECEXT MedWithoutVendorSpecExt5 MAXWITHOUTVEND_SPECEXT MaxWithoutVendorSpecExt
listOfNeTypes|跟踪网元类型|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置网元跟踪标识值。AMF：1SMF：2PCF：4gNB-CU-UP：8gNB-CU-CP：16ng-eNB：32gNB-DU：64如果要跟踪单个网元，就输入网元对应标识值就可以，如果要跟踪多个网元请输入标识值和，例如AMF和SMF就是3，SMF和PCF和gNB-CU-CP就是22。
listOfInterfaces|跟踪接口|参数可选性: 任选参数类型: 字符串参数范围: 0-100|AMF需要跟踪的接口：N1          跟踪接口标识:1需要跟踪的接口：N2          跟踪接口标识:2需要跟踪的接口：N8          跟踪接口标识:4需要跟踪的接口：N11         跟踪接口标识:8需要跟踪的接口：N12         跟踪接口标识:16需要跟踪的接口：N14         跟踪接口标识:32需要跟踪的接口：N15         跟踪接口标识:64需要跟踪的接口：N20         跟踪接口标识:128需要跟踪的接口：N22         跟踪接口标识:256需要跟踪的接口：N26         跟踪接口标识:512SMF:需要跟踪的接口：N4         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N10        跟踪接口标识:4需要跟踪的接口：N11        跟踪接口标识:8需要跟踪的接口：S5-C       跟踪接口标识:16PCF:需要跟踪的接口：N5         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N15        跟踪接口标识:4ng-eNB/gNB-CU-CP/gNB-CU-UP/gNB-DU:需要跟踪的接口：NG-C         跟踪接口标识:1需要跟踪的接口：Xn-C/X2      跟踪接口标识:2需要跟踪的接口：Uu           跟踪接口标识:4需要跟踪的接口：F1-C         跟踪接口标识:8需要跟踪的接口：E1-C         跟踪接口标识:16如果要跟踪AMF的N1和N12接口，就是配置：1-17，如果要跟踪 AMF的N1和N12接口和ng-eNB的Uu和E1-C接口，则配置1-17&32-20，也就是‘-’前面是网元标识，‘-’后面是要跟踪的接口标识的和，&用于连接要跟踪的不同网元的接口。
triggeringEvent|跟踪触发事件|参数可选性: 任选参数类型: 字符串参数范围: 0-100|只有AMF，SMF和PCF涉及。AMF需要跟踪的流程事件：UE initiated Registration Procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated Service Request Procedure，对应的事件号标示：2需要跟踪的流程事件：N2 or Xn Handover，对应的事件号标示：4需要跟踪的流程事件：UE initiated Deregistration Procedure，对应的事件号标示：8需要跟踪的流程事件：Network initiated Deregistration Procedure，对应的事件号标示：16需要跟踪的流程事件：UE mobility from EPC，对应的事件号标示：32需要跟踪的流程事件：UE mobility to EPC，对应的事件号标示：64SMF需要跟踪的流程事件：UE initiated PDU Session Establishment procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated PDU Session Modification procedure，对应的事件号标示：2需要跟踪的流程事件：UE initiated PDU Session Release procedure，对应的事件号标示：4需要跟踪的流程事件：UE initiated PDU Session UP activation / deactivation，对应的事件号标示：8需要跟踪的流程事件：Mobility of a PDU Session between 3GPP and N3GPP access to 5GC，对应的事件号标示：16需要跟踪的流程事件：Mobility of a PDU Session from EPC，对应的事件号标示：32PCF需要跟踪的流程事件：AM Policy Control，对应的事件号标示：1需要跟踪的流程事件：SM Policy，对应的事件号标示：2需要跟踪的流程事件：Policy Authorization ，对应的事件号标示：4需要跟踪的流程事件：Background data transfer policy，对应的事件号标示：8如果要跟踪AMF前两个流程的事件，就是输入1-3，其中1是AMF的网元类型，详细见：跟踪网元类型 字段，3是前两个事件标示的和，如果要跟踪AMF前两个事件和SMF的第二个和第四个流程的事件，就是 1-3&2-10，其中2是PCF的网元类型，10是第二个事件和第三个的和，必须用&连接。
traceCollectionAddr|TCE IP 地址|参数可选性: 任选参数类型: 字符串|跟踪采集实体地址，最终收到任务的网元上传信令给这个地址。
jobtype|Job类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: TRACEONLY|参数作用：此参数用于配置trace任务的激活类型。 0：仅即时MDT（Immediate MDT only）1：仅Logged MDT（Logged MDT only）2：仅Trace（Trace only）3：即时MDT与Trace（Immediate MDT and Trace）
mdtarea|MDT范围类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: INVALIDMDTAREA|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围类型。0：无效MDT范围类型1：NR CGI列表2：TAI列表 3：PLMN 4：TAC列表
mdtareaprofileid|MDT范围|参数可选性: 任选参数类型: 字符串参数范围: 0-600|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围，为字符串类型。
mdtmode|MDT模式类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: INVAILDMDTMOD|参数作用：此参数用于配置MDT的模式。 0：无效MDT模式1：即时MDT模式2：Logged MDT模式
listofmeasurements|即时MDT测量结果列表|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置即时MDT的测量结果列表。此参数为复选项, 每一个BIT位标识不同的测量结果，可以全不选，也可以选择一项或多项。
m1reportrigger|M1报告触发器|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置M1 报告触发器, 此参数为枚举复选框，但为互斥选项，即三种触发类型只能选择一个。 定期触发，对应的事件号标示：1。LTE和NR的A2 EVENT，对应的事件号标示：2。LTE和NR的A2 EVENT定期触发，对应的事件号标示：16。
m1reportinterva|M1报告间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 27-42默认值: INVALIDM1RPTINTERVA|参数作用：该参数用于配置当UE处于连接模式时，要进行的周期性测量的时间间隔。27：无效M1报告间隔28：120ms29：240 ms30：480 ms31：640 ms32：1024 ms33：2048 ms34：5120 ms35：10240 ms38：1 minute(60000 ms)39：6 minute(360000 ms)40：12 minute(720000 ms)41：30 minute(1800000 ms)42：60 minute(3600000 ms)
m1reportamount|M1报告数目|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: AMOUNT_INVALID|参数作用：该参数用于配置定期报告的测量报告数量。0：11：22：43：84：165：326：647：无穷255：无效M1报告数量
m1thresholdtype|M1门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-255默认值: TYPE_INVALID|参数作用：该参数用于配置M1门限类型。 1：-RSRP2：RSRQ3：SINR255：无效M1门限类型
rsrprsrosinr|RSRP-RSRQ-SINR数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置NR的RSRP-RSRQ-SINR数值，对应于NR，有效值范围为[0, 127]。
m4collperiod|M4采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M4COLPERIO_INVALID|参数作用：该参数用于配置在进行M4数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M4度量，应使用相同的收集周期。0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M4采集周期
m4log|M4 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M4LOG_INVALID|参数作用：该参数用于配置M4 Links to Log，取值范围如下。 0：无效M4 Links to Log1：上行2：下行3：上行和下行
m5collperiod|M5采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M5COLPERIO_INVALID|参数作用：该参数用于配置在进行M5数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M5度量，应使用相同的收集周期。 0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M5采集周期
m5log|M5 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M5LOG_INVALID|参数作用：该参数用于配置M5 Links to Log。0：无效M5 Links to Log1：上行2：下行3：上行和下行
m6collperiod|M6采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M6COLPERIO_INVALID|参数作用：该参数用于配置在进行M6数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M6度量，应使用相同的收集周期。0：120ms1：240ms2：480ms3：640ms4：1024ms5：2048ms6：5120ms7：10240ms8：20480ms9：40960ms10：1minute11：6minute12：12minute13：30minute255：无效M6采集周期
m6log|M6 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M6LOG_INVALID|参数作用：该参数用于配置M6 Links to Log。0：无效M6 Links to Log1：上行2：下行3：上行和下行
m7collperiod|M7采集周期|参数可选性: 任选参数类型: 数字参数范围: 0-60默认值: 0|参数作用：M7采集周期，单位为分钟，配置范围为[0, 60], 有效范围为[1, 60] , 0(min)为无效值。
m7log|M7 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M7LOG_INVALID|参数作用：该参数用于配置M7 Links to Log。
mdtlocinf|MDT位置信息|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：MDT位置信息，位图中的每个位置表示TS 37.320协议中定义的请求位置信息。目前第一位表示GNSS, 其他位保留供将来使用，如果收到则忽略。值"1"表示"激活", 值"0"表示"不激活"。
bluename|蓝牙名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的蓝牙名称列表，为字符串类型。
wlanname|WLAN名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的WLAN名称列表，为字符串类型。
sensorinf|传感器信息列表|参数可选性: 任选参数类型: 字符串参数范围: 0-17|参数作用：该参数用于配置MDT的传感器信息列表，为字符串类型。
loginterva|记录间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGINTERVA_INVALID|参数作用：该参数定义了UE处于空闲状态时用于记录MDT测量结果的周期性，以进行周期性的下行链路导频强度测量。0：1280 ms1：2560 ms2：5120 ms3：10240 ms4：20480 ms5：30720 ms6：40960 ms7：61440 ms8：320 ms9：640 ms10：无穷255：无效记录间隔
logduration|记录持续时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 6-255默认值: DURATION_INVALID|参数作用：该参数用于确定IDLE态时Logged MDT配置的有效性。定时器在UE接收到配置时启动，并且独立于UE状态迁移和RAT或RPLMN变化而运行。6：600 second7：1200 second8：2400 second9：3600 second10：5400 second11：7200 second255：无效持续记录时间
logmdtrpttype|Logged MDT报告类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGMDTRPTTYPE_INVAL|参数作用：该参数用于配置Logged MDT报告类型。 0：定期报告。1：事件触发。255：无效Logged MDT报告类型。
eventtritype|事件触发器类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OUTOFCOVERAGE|参数作用：该参数用于配置事件触发器类型。0：超出覆盖范围。1：L1 Event。
l1thresholdtype|L1事件门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: L1THRESTYPE_INVALID|参数作用：该参数用于配置L1事件门限类型。0：RSRP。1：RSRQ。255：无效L1事件门限类型。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中与L1时间门限类型相关的参数。数据来源：本端规划 。默认值：255：无效L1事件门限类型。配置原则：当"事件触发器类型"配置为"L1 Event"时,此参数必须配置为有效值(0或1)。
rsrprsrq|RSRP/RSRQ数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置RSRP/RSRQ数值。取值范围[0, 127]。
hysteresis|滞后|参数可选性: 任选参数类型: 数字参数范围: 0-30默认值: 0|参数作用：该参数用于配置事件触发报告条件的进入和离开条件。取值范围[0,30]。
timetrigger|触发的时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-15默认值: TIMETRIG_0MS|参数作用：该参数为触发测量报告而需要满足事件特定标准的时间 。0：0ms1：40ms2：64ms3：80ms4：100ms5：128ms6：160ms7：256ms8：320ms9：480ms10：512ms11：640ms12：1024ms13：1280ms14：2560ms15：5120ms
plmnlist|PLMN列表|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：此参数用于指示允许进行测量收集、状态指示和日志报告的PLMN，它将作为plmn-IdentityList传达给UE。在NF之间，根据MDT的激活方式，它作为基于管理的MDT PLMN列表或作为基于信令的MDT PLMN列表进行通信。
命令举例 
`
修改移动国家码为460，移动网络码为1，跟踪标识为1的跟踪任务，最终任务上报给地址为3.3.3.3的TCE服务器; 同时修改此条配置的一些信令MDT的参数。
SET TCETRACETASKCFG:MCC="460",MNC="01",TRACEID=1,TRACETARGETTYPE="IMSI",TRACETARGETVALUES="460119990010005",LISTOFNETYPES=1,LISTOFINTERFACES="1-1",TRIGGERINGEVENT="1-1",TRACECOLLECTIONADDR=3.3.3.3,M1REPORTAMOUNT="AMOUNT_64",RSRPRSROSINR=30,M4LOG="M4LOG_DOWNLINK",M7COLLPERIOD=10,BLUENAME="zte.bluetooth001&zte.com.blue002",WLANNAME="ztewlan001&zteWlan002",SENSORINF="0-1-0&1-0-0",RSRPRSRQ=22,HYSTERESIS=23,TIMETRIGGER="TIMETRIG_160MS",PLMNLIST="460-11&460-123&444-555"
` 
#### 删除TCE跟踪任务配置(DEL TCETRACETASKCFG) 
#### 删除TCE跟踪任务配置(DEL TCETRACETASKCFG) 
功能说明 
该命令用于删除一个TCE的跟踪任务。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商"中国移动"在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
traceID|跟踪标识|参数可选性: 必选参数类型: 数字参数范围: 0-16777215|TRACEID由用户跟踪系统生成，长度为3字节的整数，目前为手动配置，mcc+mnc+traceID是跟踪任务的唯一标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商"中国移动"在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
traceID|跟踪标识|参数可选性: 任选参数类型: 数字参数范围: 0-16777215|TRACEID由用户跟踪系统生成，长度为3字节的整数，目前为手动配置，mcc+mnc+traceID是跟踪任务的唯一标识。
traceTargetType|跟踪目标类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-8默认值: IMSI|该参数用于配置要跟踪的用户类型，AMF侧支持IMSI以及MSISDN的类型。0: IMSI IMSI1: IMEI IMEI2: IMEISV IMEISV3: PUB_ID Public ID4: UTRAN_CELL UTRAN_CELL5: E_UTRAN_CELL E_UTRAN_CELL6: ENB eNB7: RNC RNC8: MSISDN MSISDN
traceTargetValues|跟踪目标值|参数可选性: 任选参数类型: 字符串参数范围: 0-50|该参数用于配置要跟踪的用户，其值的类型要符合traceTargetType的定义。
traceDepth|跟踪深度|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5默认值: MAX|该参数用于应如何在网络元素中记录详细信息，目前支持max方式的解析。0 MIN Minimum1 MED Medium2 MAX Maximum3 MINWITHOUTVEND_SPECEXT MinWithoutVendorSpecExt4 MEDWITHOUTVEND_SPECEXT MedWithoutVendorSpecExt5 MAXWITHOUTVEND_SPECEXT MaxWithoutVendorSpecExt
listOfNeTypes|跟踪网元类型|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置网元跟踪标识值。AMF：1SMF：2PCF：4gNB-CU-UP：8gNB-CU-CP：16ng-eNB：32gNB-DU：64如果要跟踪单个网元，就输入网元对应标识值就可以，如果要跟踪多个网元请输入标识值和，例如AMF和SMF就是3，SMF和PCF和gNB-CU-CP就是22。
listOfInterfaces|跟踪接口|参数可选性: 任选参数类型: 字符串参数范围: 0-100|AMF需要跟踪的接口：N1          跟踪接口标识:1需要跟踪的接口：N2          跟踪接口标识:2需要跟踪的接口：N8          跟踪接口标识:4需要跟踪的接口：N11         跟踪接口标识:8需要跟踪的接口：N12         跟踪接口标识:16需要跟踪的接口：N14         跟踪接口标识:32需要跟踪的接口：N15         跟踪接口标识:64需要跟踪的接口：N20         跟踪接口标识:128需要跟踪的接口：N22         跟踪接口标识:256需要跟踪的接口：N26         跟踪接口标识:512SMF:需要跟踪的接口：N4         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N10        跟踪接口标识:4需要跟踪的接口：N11        跟踪接口标识:8需要跟踪的接口：S5-C       跟踪接口标识:16PCF:需要跟踪的接口：N5         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N15        跟踪接口标识:4ng-eNB/gNB-CU-CP/gNB-CU-UP/gNB-DU:需要跟踪的接口：NG-C         跟踪接口标识:1需要跟踪的接口：Xn-C/X2      跟踪接口标识:2需要跟踪的接口：Uu           跟踪接口标识:4需要跟踪的接口：F1-C         跟踪接口标识:8需要跟踪的接口：E1-C         跟踪接口标识:16如果要跟踪AMF的N1和N12接口，就是配置：1-17，如果要跟踪 AMF的N1和N12接口和ng-eNB的Uu和E1-C接口，则配置1-17&32-20，也就是‘-’前面是网元标识，‘-’后面是要跟踪的接口标识的和，&用于连接要跟踪的不同网元的接口。
triggeringEvent|跟踪触发事件|参数可选性: 任选参数类型: 字符串参数范围: 0-100|只有AMF，SMF和PCF涉及。AMF需要跟踪的流程事件：UE initiated Registration Procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated Service Request Procedure，对应的事件号标示：2需要跟踪的流程事件：N2 or Xn Handover，对应的事件号标示：4需要跟踪的流程事件：UE initiated Deregistration Procedure，对应的事件号标示：8需要跟踪的流程事件：Network initiated Deregistration Procedure，对应的事件号标示：16需要跟踪的流程事件：UE mobility from EPC，对应的事件号标示：32需要跟踪的流程事件：UE mobility to EPC，对应的事件号标示：64SMF需要跟踪的流程事件：UE initiated PDU Session Establishment procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated PDU Session Modification procedure，对应的事件号标示：2需要跟踪的流程事件：UE initiated PDU Session Release procedure，对应的事件号标示：4需要跟踪的流程事件：UE initiated PDU Session UP activation / deactivation，对应的事件号标示：8需要跟踪的流程事件：Mobility of a PDU Session between 3GPP and N3GPP access to 5GC，对应的事件号标示：16需要跟踪的流程事件：Mobility of a PDU Session from EPC，对应的事件号标示：32PCF需要跟踪的流程事件：AM Policy Control，对应的事件号标示：1需要跟踪的流程事件：SM Policy，对应的事件号标示：2需要跟踪的流程事件：Policy Authorization ，对应的事件号标示：4需要跟踪的流程事件：Background data transfer policy，对应的事件号标示：8如果要跟踪AMF前两个流程的事件，就是输入1-3，其中1是AMF的网元类型，详细见：跟踪网元类型 字段，3是前两个事件标示的和，如果要跟踪AMF前两个事件和SMF的第二个和第四个流程的事件，就是 1-3&2-10，其中2是PCF的网元类型，10是第二个事件和第三个的和，必须用&连接。
traceCollectionAddr|TCE IP 地址|参数可选性: 任选参数类型: 字符串|跟踪采集实体地址，最终收到任务的网元上传信令给这个地址。
jobtype|Job类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: TRACEONLY|参数作用：此参数用于配置trace任务的激活类型。 0：仅即时MDT（Immediate MDT only）1：仅Logged MDT（Logged MDT only）2：仅Trace（Trace only）3：即时MDT与Trace（Immediate MDT and Trace）
mdtarea|MDT范围类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: INVALIDMDTAREA|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围类型。0：无效MDT范围类型1：NR CGI列表2：TAI列表 3：PLMN 4：TAC列表
mdtareaprofileid|MDT范围|参数可选性: 任选参数类型: 字符串参数范围: 0-600|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围，为字符串类型。
mdtmode|MDT模式类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: INVAILDMDTMOD|参数作用：此参数用于配置MDT的模式。 0：无效MDT模式1：即时MDT模式2：Logged MDT模式
listofmeasurements|即时MDT测量结果列表|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置即时MDT的测量结果列表。此参数为复选项, 每一个BIT位标识不同的测量结果，可以全不选，也可以选择一项或多项。
m1reportrigger|M1报告触发器|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置M1 报告触发器, 此参数为枚举复选框，但为互斥选项，即三种触发类型只能选择一个。 定期触发，对应的事件号标示：1。LTE和NR的A2 EVENT，对应的事件号标示：2。LTE和NR的A2 EVENT定期触发，对应的事件号标示：16。
m1reportinterva|M1报告间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 27-42默认值: INVALIDM1RPTINTERVA|参数作用：该参数用于配置当UE处于连接模式时，要进行的周期性测量的时间间隔。27：无效M1报告间隔28：120ms29：240 ms30：480 ms31：640 ms32：1024 ms33：2048 ms34：5120 ms35：10240 ms38：1 minute(60000 ms)39：6 minute(360000 ms)40：12 minute(720000 ms)41：30 minute(1800000 ms)42：60 minute(3600000 ms)
m1reportamount|M1报告数目|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: AMOUNT_INVALID|参数作用：该参数用于配置定期报告的测量报告数量。0：11：22：43：84：165：326：647：无穷255：无效M1报告数量
m1thresholdtype|M1门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-255默认值: TYPE_INVALID|参数作用：该参数用于配置M1门限类型。 1：-RSRP2：RSRQ3：SINR255：无效M1门限类型
rsrprsrosinr|RSRP-RSRQ-SINR数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置NR的RSRP-RSRQ-SINR数值，对应于NR，有效值范围为[0, 127]。
m4collperiod|M4采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M4COLPERIO_INVALID|参数作用：该参数用于配置在进行M4数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M4度量，应使用相同的收集周期。0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M4采集周期
m4log|M4 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M4LOG_INVALID|参数作用：该参数用于配置M4 Links to Log，取值范围如下。 0：无效M4 Links to Log1：上行2：下行3：上行和下行
m5collperiod|M5采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M5COLPERIO_INVALID|参数作用：该参数用于配置在进行M5数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M5度量，应使用相同的收集周期。 0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M5采集周期
m5log|M5 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M5LOG_INVALID|参数作用：该参数用于配置M5 Links to Log。0：无效M5 Links to Log1：上行2：下行3：上行和下行
m6collperiod|M6采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M6COLPERIO_INVALID|参数作用：该参数用于配置在进行M6数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M6度量，应使用相同的收集周期。0：120ms1：240ms2：480ms3：640ms4：1024ms5：2048ms6：5120ms7：10240ms8：20480ms9：40960ms10：1minute11：6minute12：12minute13：30minute255：无效M6采集周期
m6log|M6 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M6LOG_INVALID|参数作用：该参数用于配置M6 Links to Log。0：无效M6 Links to Log1：上行2：下行3：上行和下行
m7collperiod|M7采集周期|参数可选性: 任选参数类型: 数字参数范围: 0-60默认值: 0|参数作用：M7采集周期，单位为分钟，配置范围为[0, 60], 有效范围为[1, 60] , 0(min)为无效值。
m7log|M7 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M7LOG_INVALID|参数作用：该参数用于配置M7 Links to Log。
mdtlocinf|MDT位置信息|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：MDT位置信息，位图中的每个位置表示TS 37.320协议中定义的请求位置信息。目前第一位表示GNSS, 其他位保留供将来使用，如果收到则忽略。值"1"表示"激活", 值"0"表示"不激活"。
bluename|蓝牙名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的蓝牙名称列表，为字符串类型。
wlanname|WLAN名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的WLAN名称列表，为字符串类型。
sensorinf|传感器信息列表|参数可选性: 任选参数类型: 字符串参数范围: 0-17|参数作用：该参数用于配置MDT的传感器信息列表，为字符串类型。
loginterva|记录间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGINTERVA_INVALID|参数作用：该参数定义了UE处于空闲状态时用于记录MDT测量结果的周期性，以进行周期性的下行链路导频强度测量。0：1280 ms1：2560 ms2：5120 ms3：10240 ms4：20480 ms5：30720 ms6：40960 ms7：61440 ms8：320 ms9：640 ms10：无穷255：无效记录间隔
logduration|记录持续时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 6-255默认值: DURATION_INVALID|参数作用：该参数用于确定IDLE态时Logged MDT配置的有效性。定时器在UE接收到配置时启动，并且独立于UE状态迁移和RAT或RPLMN变化而运行。6：600 second7：1200 second8：2400 second9：3600 second10：5400 second11：7200 second255：无效持续记录时间
logmdtrpttype|Logged MDT报告类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGMDTRPTTYPE_INVAL|参数作用：该参数用于配置Logged MDT报告类型。 0：定期报告。1：事件触发。255：无效Logged MDT报告类型。
eventtritype|事件触发器类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OUTOFCOVERAGE|参数作用：该参数用于配置事件触发器类型。0：超出覆盖范围。1：L1 Event。
l1thresholdtype|L1事件门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: L1THRESTYPE_INVALID|参数作用：该参数用于配置L1事件门限类型。0：RSRP。1：RSRQ。255：无效L1事件门限类型。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中与L1时间门限类型相关的参数。数据来源：本端规划 。默认值：255：无效L1事件门限类型。配置原则：当"事件触发器类型"配置为"L1 Event"时,此参数必须配置为有效值(0或1)。
rsrprsrq|RSRP/RSRQ数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置RSRP/RSRQ数值。取值范围[0, 127]。
hysteresis|滞后|参数可选性: 任选参数类型: 数字参数范围: 0-30默认值: 0|参数作用：该参数用于配置事件触发报告条件的进入和离开条件。取值范围[0,30]。
timetrigger|触发的时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-15默认值: TIMETRIG_0MS|参数作用：该参数为触发测量报告而需要满足事件特定标准的时间 。0：0ms1：40ms2：64ms3：80ms4：100ms5：128ms6：160ms7：256ms8：320ms9：480ms10：512ms11：640ms12：1024ms13：1280ms14：2560ms15：5120ms
plmnlist|PLMN列表|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：此参数用于指示允许进行测量收集、状态指示和日志报告的PLMN，它将作为plmn-IdentityList传达给UE。在NF之间，根据MDT的激活方式，它作为基于管理的MDT PLMN列表或作为基于信令的MDT PLMN列表进行通信。
命令举例 
`
删除移动国家码为460，移动网络码为1，跟踪标识为的1跟踪任务。
DEL TCETRACETASKCFG:MCC="460",MNC="01",TRACEID=1
` 
#### 查询TCE跟踪任务配置(SHOW TCETRACETASKCFG) 
#### 查询TCE跟踪任务配置(SHOW TCETRACETASKCFG) 
功能说明 
该命令用于查询已经配置的TCE的跟踪任务。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商"中国移动"在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
traceID|跟踪标识|参数可选性: 任选参数类型: 数字参数范围: 0-16777215|TRACEID由用户跟踪系统生成，长度为3字节的整数，目前为手动配置，mcc+mnc+traceID是跟踪任务的唯一标识。
traceTargetType|跟踪目标类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-8默认值: IMSI|该参数用于配置要跟踪的用户类型，AMF侧支持IMSI以及MSISDN的类型。0: IMSI IMSI1: IMEI IMEI2: IMEISV IMEISV3: PUB_ID Public ID4: UTRAN_CELL UTRAN_CELL5: E_UTRAN_CELL E_UTRAN_CELL6: ENB eNB7: RNC RNC8: MSISDN MSISDN
traceTargetValues|跟踪目标值|参数可选性: 任选参数类型: 字符串参数范围: 0-50|该参数用于配置要跟踪的用户，其值的类型要符合traceTargetType的定义。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息，例如中国为460。MCC对于所有的记录都是唯一的。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。例如运营商"中国移动"在中国运营的GSM网络的MNC为01。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
traceID|跟踪标识|参数可选性: 任选参数类型: 数字参数范围: 0-16777215|TRACEID由用户跟踪系统生成，长度为3字节的整数，目前为手动配置，mcc+mnc+traceID是跟踪任务的唯一标识。
traceTargetType|跟踪目标类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-8默认值: IMSI|该参数用于配置要跟踪的用户类型，AMF侧支持IMSI以及MSISDN的类型。0: IMSI IMSI1: IMEI IMEI2: IMEISV IMEISV3: PUB_ID Public ID4: UTRAN_CELL UTRAN_CELL5: E_UTRAN_CELL E_UTRAN_CELL6: ENB eNB7: RNC RNC8: MSISDN MSISDN
traceTargetValues|跟踪目标值|参数可选性: 任选参数类型: 字符串参数范围: 0-50|该参数用于配置要跟踪的用户，其值的类型要符合traceTargetType的定义。
traceDepth|跟踪深度|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-5默认值: MAX|该参数用于应如何在网络元素中记录详细信息，目前支持max方式的解析。0 MIN Minimum1 MED Medium2 MAX Maximum3 MINWITHOUTVEND_SPECEXT MinWithoutVendorSpecExt4 MEDWITHOUTVEND_SPECEXT MedWithoutVendorSpecExt5 MAXWITHOUTVEND_SPECEXT MaxWithoutVendorSpecExt
listOfNeTypes|跟踪网元类型|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于设置网元跟踪标识值。AMF：1SMF：2PCF：4gNB-CU-UP：8gNB-CU-CP：16ng-eNB：32gNB-DU：64如果要跟踪单个网元，就输入网元对应标识值就可以，如果要跟踪多个网元请输入标识值和，例如AMF和SMF就是3，SMF和PCF和gNB-CU-CP就是22。
listOfInterfaces|跟踪接口|参数可选性: 任选参数类型: 字符串参数范围: 0-100|AMF需要跟踪的接口：N1          跟踪接口标识:1需要跟踪的接口：N2          跟踪接口标识:2需要跟踪的接口：N8          跟踪接口标识:4需要跟踪的接口：N11         跟踪接口标识:8需要跟踪的接口：N12         跟踪接口标识:16需要跟踪的接口：N14         跟踪接口标识:32需要跟踪的接口：N15         跟踪接口标识:64需要跟踪的接口：N20         跟踪接口标识:128需要跟踪的接口：N22         跟踪接口标识:256需要跟踪的接口：N26         跟踪接口标识:512SMF:需要跟踪的接口：N4         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N10        跟踪接口标识:4需要跟踪的接口：N11        跟踪接口标识:8需要跟踪的接口：S5-C       跟踪接口标识:16PCF:需要跟踪的接口：N5         跟踪接口标识:1需要跟踪的接口：N7         跟踪接口标识:2需要跟踪的接口：N15        跟踪接口标识:4ng-eNB/gNB-CU-CP/gNB-CU-UP/gNB-DU:需要跟踪的接口：NG-C         跟踪接口标识:1需要跟踪的接口：Xn-C/X2      跟踪接口标识:2需要跟踪的接口：Uu           跟踪接口标识:4需要跟踪的接口：F1-C         跟踪接口标识:8需要跟踪的接口：E1-C         跟踪接口标识:16如果要跟踪AMF的N1和N12接口，就是配置：1-17，如果要跟踪 AMF的N1和N12接口和ng-eNB的Uu和E1-C接口，则配置1-17&32-20，也就是‘-’前面是网元标识，‘-’后面是要跟踪的接口标识的和，&用于连接要跟踪的不同网元的接口。
triggeringEvent|跟踪触发事件|参数可选性: 任选参数类型: 字符串参数范围: 0-100|只有AMF，SMF和PCF涉及。AMF需要跟踪的流程事件：UE initiated Registration Procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated Service Request Procedure，对应的事件号标示：2需要跟踪的流程事件：N2 or Xn Handover，对应的事件号标示：4需要跟踪的流程事件：UE initiated Deregistration Procedure，对应的事件号标示：8需要跟踪的流程事件：Network initiated Deregistration Procedure，对应的事件号标示：16需要跟踪的流程事件：UE mobility from EPC，对应的事件号标示：32需要跟踪的流程事件：UE mobility to EPC，对应的事件号标示：64SMF需要跟踪的流程事件：UE initiated PDU Session Establishment procedure，对应的事件号标示：1需要跟踪的流程事件：UE initiated PDU Session Modification procedure，对应的事件号标示：2需要跟踪的流程事件：UE initiated PDU Session Release procedure，对应的事件号标示：4需要跟踪的流程事件：UE initiated PDU Session UP activation / deactivation，对应的事件号标示：8需要跟踪的流程事件：Mobility of a PDU Session between 3GPP and N3GPP access to 5GC，对应的事件号标示：16需要跟踪的流程事件：Mobility of a PDU Session from EPC，对应的事件号标示：32PCF需要跟踪的流程事件：AM Policy Control，对应的事件号标示：1需要跟踪的流程事件：SM Policy，对应的事件号标示：2需要跟踪的流程事件：Policy Authorization ，对应的事件号标示：4需要跟踪的流程事件：Background data transfer policy，对应的事件号标示：8如果要跟踪AMF前两个流程的事件，就是输入1-3，其中1是AMF的网元类型，详细见：跟踪网元类型 字段，3是前两个事件标示的和，如果要跟踪AMF前两个事件和SMF的第二个和第四个流程的事件，就是 1-3&2-10，其中2是PCF的网元类型，10是第二个事件和第三个的和，必须用&连接。
traceCollectionAddr|TCE IP 地址|参数可选性: 任选参数类型: 字符串|跟踪采集实体地址，最终收到任务的网元上传信令给这个地址。
jobtype|Job类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: TRACEONLY|参数作用：此参数用于配置trace任务的激活类型。 0：仅即时MDT（Immediate MDT only）1：仅Logged MDT（Logged MDT only）2：仅Trace（Trace only）3：即时MDT与Trace（Immediate MDT and Trace）
mdtarea|MDT范围类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-4默认值: INVALIDMDTAREA|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围类型。0：无效MDT范围类型1：NR CGI列表2：TAI列表 3：PLMN 4：TAC列表
mdtareaprofileid|MDT范围|参数可选性: 任选参数类型: 字符串参数范围: 0-600|参数作用：此参数用于配置Immediate MDT和Logged MDT的跟踪范围，为字符串类型。
mdtmode|MDT模式类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: INVAILDMDTMOD|参数作用：此参数用于配置MDT的模式。 0：无效MDT模式1：即时MDT模式2：Logged MDT模式
listofmeasurements|即时MDT测量结果列表|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置即时MDT的测量结果列表。此参数为复选项, 每一个BIT位标识不同的测量结果，可以全不选，也可以选择一项或多项。
m1reportrigger|M1报告触发器|参数可选性: 任选参数类型: 枚举，参见枚举定义|参数作用：此参数用于配置M1 报告触发器, 此参数为枚举复选框，但为互斥选项，即三种触发类型只能选择一个。 定期触发，对应的事件号标示：1。LTE和NR的A2 EVENT，对应的事件号标示：2。LTE和NR的A2 EVENT定期触发，对应的事件号标示：16。
m1reportinterva|M1报告间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 27-42默认值: INVALIDM1RPTINTERVA|参数作用：该参数用于配置当UE处于连接模式时，要进行的周期性测量的时间间隔。27：无效M1报告间隔28：120ms29：240 ms30：480 ms31：640 ms32：1024 ms33：2048 ms34：5120 ms35：10240 ms38：1 minute(60000 ms)39：6 minute(360000 ms)40：12 minute(720000 ms)41：30 minute(1800000 ms)42：60 minute(3600000 ms)
m1reportamount|M1报告数目|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: AMOUNT_INVALID|参数作用：该参数用于配置定期报告的测量报告数量。0：11：22：43：84：165：326：647：无穷255：无效M1报告数量
m1thresholdtype|M1门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 1-255默认值: TYPE_INVALID|参数作用：该参数用于配置M1门限类型。 1：-RSRP2：RSRQ3：SINR255：无效M1门限类型
rsrprsrosinr|RSRP-RSRQ-SINR数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置NR的RSRP-RSRQ-SINR数值，对应于NR，有效值范围为[0, 127]。
m4collperiod|M4采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M4COLPERIO_INVALID|参数作用：该参数用于配置在进行M4数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M4度量，应使用相同的收集周期。0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M4采集周期
m4log|M4 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M4LOG_INVALID|参数作用：该参数用于配置M4 Links to Log，取值范围如下。 0：无效M4 Links to Log1：上行2：下行3：上行和下行
m5collperiod|M5采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M5COLPERIO_INVALID|参数作用：该参数用于配置在进行M5数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M5度量，应使用相同的收集周期。 0：1024ms1：2048ms2：5120ms3：10240ms4：1minute255：无效M5采集周期
m5log|M5 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M5LOG_INVALID|参数作用：该参数用于配置M5 Links to Log。0：无效M5 Links to Log1：上行2：下行3：上行和下行
m6collperiod|M6采集周期|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: M6COLPERIO_INVALID|参数作用：该参数用于配置在进行M6数据量度量和IP吞吐量度量时，收集可用度量样本的收集周期。在同一MDT或Trace与MDT合并任务中请求的所有M6度量，应使用相同的收集周期。0：120ms1：240ms2：480ms3：640ms4：1024ms5：2048ms6：5120ms7：10240ms8：20480ms9：40960ms10：1minute11：6minute12：12minute13：30minute255：无效M6采集周期
m6log|M6 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M6LOG_INVALID|参数作用：该参数用于配置M6 Links to Log。0：无效M6 Links to Log1：上行2：下行3：上行和下行
m7collperiod|M7采集周期|参数可选性: 任选参数类型: 数字参数范围: 0-60默认值: 0|参数作用：M7采集周期，单位为分钟，配置范围为[0, 60], 有效范围为[1, 60] , 0(min)为无效值。
m7log|M7 Links to Log|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: M7LOG_INVALID|参数作用：该参数用于配置M7 Links to Log。
mdtlocinf|MDT位置信息|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1|参数作用：MDT位置信息，位图中的每个位置表示TS 37.320协议中定义的请求位置信息。目前第一位表示GNSS, 其他位保留供将来使用，如果收到则忽略。值"1"表示"激活", 值"0"表示"不激活"。
bluename|蓝牙名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的蓝牙名称列表，为字符串类型。
wlanname|WLAN名称列表|参数可选性: 任选参数类型: 字符串参数范围: 0-995|参数作用：该参数用于配置MDT的WLAN名称列表，为字符串类型。
sensorinf|传感器信息列表|参数可选性: 任选参数类型: 字符串参数范围: 0-17|参数作用：该参数用于配置MDT的传感器信息列表，为字符串类型。
loginterva|记录间隔|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGINTERVA_INVALID|参数作用：该参数定义了UE处于空闲状态时用于记录MDT测量结果的周期性，以进行周期性的下行链路导频强度测量。0：1280 ms1：2560 ms2：5120 ms3：10240 ms4：20480 ms5：30720 ms6：40960 ms7：61440 ms8：320 ms9：640 ms10：无穷255：无效记录间隔
logduration|记录持续时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 6-255默认值: DURATION_INVALID|参数作用：该参数用于确定IDLE态时Logged MDT配置的有效性。定时器在UE接收到配置时启动，并且独立于UE状态迁移和RAT或RPLMN变化而运行。6：600 second7：1200 second8：2400 second9：3600 second10：5400 second11：7200 second255：无效持续记录时间
logmdtrpttype|Logged MDT报告类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: LOGMDTRPTTYPE_INVAL|参数作用：该参数用于配置Logged MDT报告类型。 0：定期报告。1：事件触发。255：无效Logged MDT报告类型。
eventtritype|事件触发器类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: OUTOFCOVERAGE|参数作用：该参数用于配置事件触发器类型。0：超出覆盖范围。1：L1 Event。
l1thresholdtype|L1事件门限类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: L1THRESTYPE_INVALID|参数作用：该参数用于配置L1事件门限类型。0：RSRP。1：RSRQ。255：无效L1事件门限类型。修改影响：影响AMF下发给RAN的Trace Start消息携带MDT参数(NR)中与L1时间门限类型相关的参数。数据来源：本端规划 。默认值：255：无效L1事件门限类型。配置原则：当"事件触发器类型"配置为"L1 Event"时,此参数必须配置为有效值(0或1)。
rsrprsrq|RSRP/RSRQ数值|参数可选性: 任选参数类型: 数字参数范围: 0-127默认值: 0|参数作用：该参数用于配置RSRP/RSRQ数值。取值范围[0, 127]。
hysteresis|滞后|参数可选性: 任选参数类型: 数字参数范围: 0-30默认值: 0|参数作用：该参数用于配置事件触发报告条件的进入和离开条件。取值范围[0,30]。
timetrigger|触发的时间|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-15默认值: TIMETRIG_0MS|参数作用：该参数为触发测量报告而需要满足事件特定标准的时间 。0：0ms1：40ms2：64ms3：80ms4：100ms5：128ms6：160ms7：256ms8：320ms9：480ms10：512ms11：640ms12：1024ms13：1280ms14：2560ms15：5120ms
plmnlist|PLMN列表|参数可选性: 任选参数类型: 字符串参数范围: 0-127|参数作用：此参数用于指示允许进行测量收集、状态指示和日志报告的PLMN，它将作为plmn-IdentityList传达给UE。在NF之间，根据MDT的激活方式，它作为基于管理的MDT PLMN列表或作为基于信令的MDT PLMN列表进行通信。
命令举例 
`
查询所有移动国家码为460的tce跟踪任务。
SHOW TCETRACETASKCFG:MCC="460"
(No.1) : SHOW TCETRACETASKCFG:MCC="460"
-----------------Namf_Communication_0----------------
操作维护       移动国家码 移动网络码 跟踪标识 跟踪目标类型 跟踪目标值      跟踪深度 跟踪网元类型 跟踪接口 跟踪触发事件 TCE IP 地址 Job类型   MDT范围类型 MDT范围 MDT模式类型 即时MDT测量结果列表 M1报告触发器 M1报告间隔 M1报告数目 M1门限类型 RSRP-RSRQ-SINR数值 M4采集周期 M4 Links to Log M5采集周期 M5 Links to Log M6采集周期 M6 Links to Log M7采集周期 M7 Links to Log MDT位置信息 蓝牙名称列表                     WLAN名称列表          传感器信息列表 记录间隔    记录持续时间 Logged MDT报告类型 事件触发器类型 L1事件门限类型 RSRP/RSRQ数值 滞后 触发的时间 PLMN列表       
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 460        01         1        IMSI         460119990010005 Maximum  1            1-1      1-1          2.2.2.2     仅即时MDT PLMN                即时MDT模式 M1&M4&M5&M7         定期触发      640 ms      32          RSRP       32                 2048ms     上行和下行      10240ms    上行和下行      640ms      下行            10         上行和下行      GNSS        zte.bluetooth001&zte.com.blue002 ztewlan001&zteWlan002 0-1-0&1-0-0    1280 ms (0) 2400 second  定期报告           L1 Event       RSRQ           22            23   40ms       460-11&460-123 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-04-22 20:56:08 耗时: 0.26 秒
` 
# rm功能控制 
# rm功能控制 
背景知识 
在网络运行时，一个RM承接多个COMMUNICATION的业务量。如果不加以控制，当COMMUNICATION的业务量过大时，RM可能超过系统的负荷，影响正常业务。 
功能说明 
本功能用于配置COMMUNICATION与RM交互的消息、参数等功能的控制 
子主题： 
## 消息发送速率控制配置 
## 消息发送速率控制配置 
背景知识 
RM和Communication之间存在大量的消息交互，而且消息长度都比较小，进而引起性能问题，所以需要对消息进行缓存和打包之后再发送。本配置用于设置缓存和打包的相关参数。 
功能说明 
本功能用于设置消息发送速率控制相关参数，包括消息发送速率、消息重发次数、消息缓存最大数目。  
子主题： 
### 设置消息发送速率控制配置(SET MESSAGERATECTRL) 
### 设置消息发送速率控制配置(SET MESSAGERATECTRL) 
功能说明 
该命令用于设置或修改消息发送速率控制相关参数。 
目的是提高服务之间通讯的性能和稳定性、避免波动。 
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
msgRate|消息发送速率(包/秒)|参数可选性: 任选参数类型: 数字参数范围: 0-10000|该参数用于设置消息发送速率，默认值为2000（单位：包/秒），0表示不限制。
resendCount|消息重发次数|参数可选性: 任选参数类型: 数字参数范围: 0-10|该参数用于设置消息重发次数，默认值为3，0表示一直重发。
cacheMaxCount|消息缓存最大数目|参数可选性: 任选参数类型: 数字参数范围: 0-100000|该参数用于设置消息缓存最大数目，默认值为10000，0表示不限制。
命令举例 
`
设置消息发送速率控制：消息发送速率为500包/秒，消息重发次数为3。
SET MESSAGERATECTRL:MSGRATE=500,RESENDCOUNT=3
` 
### 查询消息发送速率控制配置(SHOW MESSAGERATECTRL) 
### 查询消息发送速率控制配置(SHOW MESSAGERATECTRL) 
功能说明 
该命令用于查看消息发送速率控制相关参数值。  
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
msgRate|消息发送速率(包/秒)|参数可选性: 任选参数类型: 数字参数范围: 0-10000|该参数用于设置消息发送速率，默认值为2000（单位：包/秒），0表示不限制。
resendCount|消息重发次数|参数可选性: 任选参数类型: 数字参数范围: 0-10|该参数用于设置消息重发次数，默认值为3，0表示一直重发。
cacheMaxCount|消息缓存最大数目|参数可选性: 任选参数类型: 数字参数范围: 0-100000|该参数用于设置消息缓存最大数目，默认值为10000，0表示不限制。
命令举例 
`
查询消息发送速率控制配置。 
SHOW MESSAGERATECTRL:
SHOW MESSAGERATECTRL:
-----------------Namf_Communication_0----------------
消息发送速率          消息重发次数          消息缓存最大数目
-----------------------------------------------------------------
         2000                            3                                10000
-----------------------------------------------------------------
记录数：1
执行成功耗时：0.22s
` 
# ODB配置 
# ODB配置 
背景知识 
ODB（Operator Determined Barring），即运营商的限制，运营商能够通过设置ODB参数，来对用户的某些类别的业务进行限制或者漫游进行限制。 
分组数据业务的ODB限制，由UDM签约和AMF两者配合实现。要求UDM支持ODB签约信息，能够根据签约数据决定是否触发ODB业务，如果UDM签约对分组数据业务进行ODB限制，AMF也配置了支持ODB限制，则AMF进行对应的分组业务的ODB限制。 
功能说明 
通过AMF ODB配置，结合UDM ODB的签约信息，AMF可以进行以下类别的ODB限制。 
 
支持禁止所有分组业务。 
 
支持禁止漫游用户HPLMN接入业务。 
 
支持禁止漫游用户VPLMN接入业务。 
 
AMF对未签约的DNN是否发起PDU去激活。 
 
子主题： 
## 修改ODB配置(SET 5GODBCFG) 
## 修改ODB配置(SET 5GODBCFG) 
功能说明 
本命令用于设置ODB配置。 
注意事项 
无  
输入参数说明 
标识|名称|类型|说明
---|---|---|---
barAllPs|支持禁止所有分组业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置AMF是否支持”禁止所有分组业务”。当AMF配置支持”禁止所有分组业务”且UDM签约”禁止所有分组业务”时，AMF实行禁止所有分组业务的ODB限制。默认值为不支持。
barRoamHplmn|支持禁止漫游用户HPLMN接入业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置AMF是否支持”禁止漫游用户HPLMN接入业务”。当AMF配置支持”禁止漫游用户HPLMN接入业务”且UDM签约”禁止漫游用户HPLMN接入业务”时，AMF实行禁止漫游用户接入HPLMN的ODB限制。默认值为不支持。
barRoamVplmn|支持禁止漫游用户VPLMN接入业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置AMF是否支持”禁止漫游用户VPLMN接入业务”。当AMF配置支持”禁止漫游用户VPLMN接入业务”且UDM签约”禁止漫游用户VPLMN接入业务”时，AMF实行禁止漫游用户VPLMN用户接入的ODB限制。默认值为不支持。
barAllPsRegistStry|禁止所有分组业务时用户接入策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: JUDGEBYSERVICE|该参数用于配置当对用户实行“禁止所有分组业务”的ODB限制后，AMF是否还允许UE注册到网络。策略可以是以下三种：(1)禁止用户接入，AMF拒绝用户注册到网络。对于已经注册在AMF的用户，AMF将对UE发起去注册流程，将用户从网络侧去注册。(2)允许用户接入时，AMF接受用户注册到网络。对于已经注册在AMF的用户，维持用户注册在网络。(3)根据业务判断时，UE还可能做SMS短消息业务和LADN本地网用户接入业务。所以AMF需要根据UE是否签约SMS业务及UE是否签约LADN业务，来决策是否让UE注册到网络，以便能进行后续的SMS业务和LADN本地网用户接入业务。如果能确定UE后续不会再有LADN业务和短消息业务，则AMF拒绝UE注册到网络。 该参数默认值为根据业务判断
registRejCauseOdb|ODB限制注册拒绝NAS原因|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: N1MODENOTALLOWED|当对用户实施“禁止所有分组业务”的ODB限制后，AMF需要拒绝UE注册到网络。AMF对发起注册请求的用户回注册拒绝，对已经注册在AMF的用户发起去注册请求。携带的NAS原因值配置。该参数用于配置用户发起注册请求，AMF因为ODB限制给UE回注册拒绝时，携带的NAS原因。 该参数默认值为：27 - N1 mode not allowed
deregistreqcauseodb|ODB限制去注册请求NAS原因|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: N1MODENOTALLOWED|当对用户实施“禁止所有分组业务”的ODB限制后，AMF根据策略，可能拒绝UE注册到网络。如果AMF拒绝UE注册到网络，AMF对新发起注册请求的用户回注册拒绝，对已经注册在AMF的用户发起去注册请求。该参数用于配置AMF因为ODB限制给UE发起去注册请求时，去注册请求携带的NAS原因值配置，也支持配置为不携带NAS原因。 该参数默认值为：27 - N1 mode not allowed
unSubDnnDeActPdu|AMF对未签约的DNN是否发起PDU去激活|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置AMF是否对未签约的DNN对应的PDU发起去激活。因为DNN签约取消时，UDM可能通知AMF和SMF，有可能SMF来触发PDU去激活。所以AMF增加开关控制。默认取值不对未签约的DNN对应的PDU发起去激活。
命令举例 
`
设置ODB配置，禁止所有分组业务。
SET 5GODBCFG:BARALLPS="YES",BARROAMHPLMN="YES",BARROAMVPLMN="YES",BARALLPSREGISTSTRY="JUDGEBYSERVICE",REGISTREJCAUSEODB="SERVICENOTALLOWED",DEREGISTREQCAUSEODB="N1MODENOTALLOWED",UNSUBDNNDEACTPDU="YES"
` 
## 查询ODB配置(SHOW 5GODBCFG) 
## 查询ODB配置(SHOW 5GODBCFG) 
功能说明 
本命令用于查询ODB配置。 
注意事项 
无  
输出参数说明 
标识|名称|类型|说明
---|---|---|---
barAllPs|支持禁止所有分组业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置AMF是否支持”禁止所有分组业务”。当AMF配置支持”禁止所有分组业务”且UDM签约”禁止所有分组业务”时，AMF实行禁止所有分组业务的ODB限制。默认值为不支持。
barRoamHplmn|支持禁止漫游用户HPLMN接入业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置AMF是否支持”禁止漫游用户HPLMN接入业务”。当AMF配置支持”禁止漫游用户HPLMN接入业务”且UDM签约”禁止漫游用户HPLMN接入业务”时，AMF实行禁止漫游用户接入HPLMN的ODB限制。默认值为不支持。
barRoamVplmn|支持禁止漫游用户VPLMN接入业务|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置AMF是否支持”禁止漫游用户VPLMN接入业务”。当AMF配置支持”禁止漫游用户VPLMN接入业务”且UDM签约”禁止漫游用户VPLMN接入业务”时，AMF实行禁止漫游用户VPLMN用户接入的ODB限制。默认值为不支持。
barAllPsRegistStry|禁止所有分组业务时用户接入策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: JUDGEBYSERVICE|该参数用于配置当对用户实行“禁止所有分组业务”的ODB限制后，AMF是否还允许UE注册到网络。策略可以是以下三种：(1)禁止用户接入，AMF拒绝用户注册到网络。对于已经注册在AMF的用户，AMF将对UE发起去注册流程，将用户从网络侧去注册。(2)允许用户接入时，AMF接受用户注册到网络。对于已经注册在AMF的用户，维持用户注册在网络。(3)根据业务判断时，UE还可能做SMS短消息业务和LADN本地网用户接入业务。所以AMF需要根据UE是否签约SMS业务及UE是否签约LADN业务，来决策是否让UE注册到网络，以便能进行后续的SMS业务和LADN本地网用户接入业务。如果能确定UE后续不会再有LADN业务和短消息业务，则AMF拒绝UE注册到网络。 该参数默认值为根据业务判断
registRejCauseOdb|ODB限制注册拒绝NAS原因|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: N1MODENOTALLOWED|当对用户实施“禁止所有分组业务”的ODB限制后，AMF需要拒绝UE注册到网络。AMF对发起注册请求的用户回注册拒绝，对已经注册在AMF的用户发起去注册请求。携带的NAS原因值配置。该参数用于配置用户发起注册请求，AMF因为ODB限制给UE回注册拒绝时，携带的NAS原因。 该参数默认值为：27 - N1 mode not allowed
deregistreqcauseodb|ODB限制去注册请求NAS原因|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: N1MODENOTALLOWED|当对用户实施“禁止所有分组业务”的ODB限制后，AMF根据策略，可能拒绝UE注册到网络。如果AMF拒绝UE注册到网络，AMF对新发起注册请求的用户回注册拒绝，对已经注册在AMF的用户发起去注册请求。该参数用于配置AMF因为ODB限制给UE发起去注册请求时，去注册请求携带的NAS原因值配置，也支持配置为不携带NAS原因。 该参数默认值为：27 - N1 mode not allowed
unSubDnnDeActPdu|AMF对未签约的DNN是否发起PDU去激活|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数用于配置AMF是否对未签约的DNN对应的PDU发起去激活。因为DNN签约取消时，UDM可能通知AMF和SMF，有可能SMF来触发PDU去激活。所以AMF增加开关控制。默认取值不对未签约的DNN对应的PDU发起去激活。
命令举例 
`
查询ODB配置。 
SHOW 5GODBCFG:
(No.1) : SHOW 5GODBCFG:
-----------------Namf_Communication_0_A----------------
操作维护       支持禁止所有分组业务 支持禁止漫游用户HPLMN接入业务 支持禁止漫游用户VPLMN接入业务 禁止所有分组业务时用户接入策略 ODB限制注册拒绝NAS原因  ODB限制去注册请求NAS原因 AMF对未签约的DNN是否发起PDU去激活 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
修改           是               是                        是                        根据业务判断                   7 - 5GS业务不允许     27 - N1模式不允许  是                                
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2020-09-10 17:43:05 耗时: 0.134 秒
` 
# CN辅助无线信息配置 
# CN辅助无线信息配置 
背景知识 
AMF应支持在注册、业务请求、切换等流程发生时基于UE粒度下发辅助信息给NG-RAN，辅助NG-RAN决定UE是否进入RRC Inactive状态、生成寻呼策略、用户移动性/可达性管理。辅助信息若发生变化，AMF应支持通知NG-RAN辅助信息更新。 
功能说明 
CN辅助无线信息配置提供CN辅助无线信息策略配置。 
子主题： 
## CN辅助无线信息策略配置 
## CN辅助无线信息策略配置 
背景知识 
AMF应支持在注册、业务请求、切换等流程发生时基于UE粒度下发辅助信息给NG-RAN，辅助NG-RAN决定UE是否进入RRC Inactive状态、生成寻呼策略、用户移动性/可达性管理。辅助信息若发生变化，AMF应支持通知NG-RAN辅助信息更新。 
功能说明 
CN辅助无线信息配置提供CN辅助无线信息策略配置。 
子主题： 
### 修改CN辅助无线信息策略配置(SET CNASSISTANCEINFO POLICY) 
### 修改CN辅助无线信息策略配置(SET CNASSISTANCEINFO POLICY) 
功能说明 
该命令用于设置CN辅助无线信息策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
AssiInfoSwitch|辅助无线信息功能开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ON|该参数用于设置是否启用CN辅助无线信息功能。
命令举例 
`
修改CN辅助无线信息策略配置：开启CN辅助无线信息功能。
SET CNASSISTANCEINFO POLICY:ASSIINFOSWITCH="ON"
` 
### 查询CN辅助无线信息策略配置(SHOW CNASSISTANCEINFO POLICY) 
### 查询CN辅助无线信息策略配置(SHOW CNASSISTANCEINFO POLICY) 
功能说明 
该命令用于查询CN辅助无线信息策略配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
AssiInfoSwitch|辅助无线信息功能开关|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: ON|该参数用于设置是否启用CN辅助无线信息功能。
命令举例 
`
查询CN辅助无线信息策略配置。
SHOW CNASSISTANCEINFO POLICY
(No.1) : SHOW CNASSISTANCEINFO POLICY:
-----------------Namf_Communication_0_A----------------
辅助无线信息功能开关
打开
记录数：1
` 
# 特性协商管理配置 
# 特性协商管理配置 
背景知识 
AMF的特性协商机制，用于协商AMF与其他NF之间适用的可选特性。
AMF支持的可选特性在3GPP协议中定义，包括：DTSSA（Deployments Topologies with specific SMF Service Areas） 
功能说明 
“特性协商管理配置”用于管理AMF的特性协商，包括：
1、支持DTSSA特性协商 
子主题： 
## 设置特性协商管理配置(SET AMFFEATURENEG) 
## 设置特性协商管理配置(SET AMFFEATURENEG) 
功能说明 
该命令用于设置特性协商管理配置。当需要管理AMF的特性协商时，需要在AMF中设置特性协商管理配置。29.518协议定义了Namf_Communication服务的supportedFeatures，目前AMF仅支持DTSSA特性协商，AMF通过与I-SMF/SMF间的信令交互执行DTSSA特性协商 
当需要开启或关闭特性协商功能时，可使用此命令。  
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supDTSSANeg|支持DTSSA特性协商|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于设置AMF是否支持DTSSA特性协商功能。
命令举例 
`
设置或修改是否支持DTSSA特性协商功能。
SET AMFFEATURENEG:SUPDTSSANEG="SUPPORT"
` 
## 查询特性协商管理配置(SHOW AMFFEATURENEG) 
## 查询特性协商管理配置(SHOW AMFFEATURENEG) 
功能说明 
该命令用于查询AMF是否支持特性协商功能。  
注意事项 
无
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supDTSSANeg|支持DTSSA特性协商|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPPORT|该参数用于显示AMF是否支持DTSSA特性协商功能。
命令举例 
`
查询AMF是否支持DTSSA特性协商功能。
SHOW AMFFEATURENEG:
(No.1) : SHOW AMFFEATURENEG:
-----------------Namf_Communication_0----------------
支持DTSSA特性协商
支持
记录数：1
执行成功耗时： 0.381 秒
` 
# 双连接配置 
# 双连接配置 
背景知识 
双连接是指用户终端可以连接主基站和从基站，其中只有主基站用于实现控制平面的功能，数据业务可以选择由主基站传输，还是从基站传输，或者二者同时传输。 
从基站和主基站可以是相同RAT的基站，也可以是不同RAT的基站。 
功能说明 
双连接配置主要包括双连接策略配置、Secondary RAT限制配置等。 
子主题： 
## 双连接策略配置 
## 双连接策略配置 
背景知识 
p>双连接是指用户终端可以连接主基站和从基站，其中只有主基站用于实现控制平面的功能，数据业务可以选择由主基站传输，还是从基站传输，或者二者同时传输。 
功能说明 
双连接策略配置包括双连接功能开关等。 
该功能需要License的支持，对应的License项为“AMF支持双连接功能”。 
子主题： 
### 修改双连接策略配置(SET 5GDUALCONN) 
### 修改双连接策略配置(SET 5GDUALCONN) 
功能说明 
本命令用于设置双连接策略配置。 
双连接是指用户终端可以连接主基站和从基站，其中只有主基站用于实现控制平面的功能，数据业务可以选择由主基站传输，还是从基站传输，或者二者同时传输。 
通过该配置，设置AMF是否支持双连接功能；以及在AMF支持双连接功能时，是否支持Secondary RAT Usage Reporting功能。 
注意事项 
该功能需要License的支持，对应的License项为"AMF支持双连接功能".  
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ifamfdualconn|AMF支持双连接功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数标识AMF是否支持双连接功能。默认值为不支持。
ifSupUsageReport|AMF支持用量报告|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|在AMF支持双连接功能时，该参数标识AMF是否支持Secondary RAT Usage Reporting功能。
命令举例 
`
设置双连接策略配置，设置AMF支持双连接功能。
SET 5GDUALCONN:IFAMFDUALCONN="YES",IFSUPUSAGEREPORT="YES"
` 
### 查询双连接策略配置(SHOW 5GDUALCONN) 
### 查询双连接策略配置(SHOW 5GDUALCONN) 
功能说明 
本命令用于查询双连接策略配置。 
注意事项 
无  
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ifamfdualconn|AMF支持双连接功能|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|该参数标识AMF是否支持双连接功能。默认值为不支持。
ifSupUsageReport|AMF支持用量报告|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|在AMF支持双连接功能时，该参数标识AMF是否支持Secondary RAT Usage Reporting功能。
命令举例 
`
查询双连接策略配置。 
SHOW 5GDUALCONN:
(No.1) : SHOW 5GDUALCONN:
-----------------Namf_Communication_0----------------
操作维护       AMF支持双连接功能 AMF支持用量报告 
-------------------------------------------------
修改           否                否              
-------------------------------------------------
记录数：1
执行成功开始时间:2021-03-18 21:10:52 耗时: 0.608 秒
` 
## 双连接Rat限制策略配置 
## 双连接Rat限制策略配置 
背景知识 
双连接是指用户终端可以连接主基站和从基站，其中只有主基站用于实现控制平面的功能，数据业务可以选择由主基站传输，还是从基站传输，或者二者同时传输。 
从基站和主基站可以是相同RAT的基站，也可以是不同RAT的基站。5GC可以通过移动限制列表中的Primary RAT Restriction和Secondary RAT Restriction信息，通知RAN限制哪些RAT下双连接的建立。 
功能说明 
双连接RAT限制策略配置主要包括双连接RAT限制跟踪区组配置、双连接RAT限制策略模板配置、全局双连接RAT限制策略配置、基于SUPI号段和区域的双连接RAT限制策略配置等。 
子主题： 
### 双连接RAT限制跟踪区组配置 
### 双连接RAT限制跟踪区组配置 
背景知识 
双连接是指用户终端可以连接主基站和从基站，其中只有主基站用于实现控制平面的功能，数据业务可以选择由主基站传输，还是从基站传输，或者二者同时传输。 
从基站和主基站可以是相同RAT的基站，也可以是不同RAT的基站。5GC可以通过移动限制列表中的Primary RAT Restriction和Secondary RAT Restriction信息，通知RAN限制哪些RAT下双连接的建立。 
功能说明 
该配置用于增加跟踪区组号下对应的TA和/或TA范围。 
子主题： 
#### 新增双连接RAT限制跟踪区组配置(ADD DUALCONNRATRSTTAGROUP) 
#### 新增双连接RAT限制跟踪区组配置(ADD DUALCONNRATRSTTAGROUP) 
功能说明 
该命令用于新增一组双连接RAT限制跟踪区组配置，用于增加跟踪区组号下对应的TA和/或TA范围，每个TA组编号可以关联最多1024个TA。 
注意事项 
 
本命令配置的数据，在AMF下一次给RAN下发Mobility Restriction List时生效。 
 
配置本命令之前，需要确认License项： " AMF支持双连接功能"已激活，否则本命令无法生效。 
 
本命令配置的跟踪区组中包含的TA不能重叠。 
 
最多只能配置1024条记录。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于设置跟踪区组标识，是一组TA的集合。修改影响：无。数据来源：本端规划。默认值：无。配置原则：双连接RAT限制跟踪区组中包含的TA不能重叠。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置跟踪区(组)的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置跟踪区(组)的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区(组)的单列跟踪区编号，由运营商在PLMN内统一规划，以16进制数字编码。在移动网络中，规定对终端的物理位置采用跟踪区TA（Tracking Area）来进行管理，TAI（Tracking Area Identity，跟踪区域标识），由国家码（MCC）、移动网络码 （MNC）和TAC （Tracking Area Code，跟踪区码）组成， 跟踪区的划分由运营商统一规划，一般运营商对于TAC的编码方式都有明确的规定，在配置前需要提前确定TAC的分配和编码。修改影响：无。数据来源：全网规划。默认值：000000。配置原则：默认值为000000，表示无效，如果想配置TAC，必须修改为有效值。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区(组)的跟踪区码起始值，由运营商在PLMN内统一规划，以16进制数字编码。修改影响：无。数据来源：全网规划。默认值：000000。配置原则：当存在PLMN相同且TAC连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须一个一个依次增加，使配置更加灵活。如果希望TAC范围有效，跟踪区码起始和终止均不能为000000。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区(组)的跟踪区码终止值，由运营商在PLMN内统一规划，以16进制数字编码。修改影响：无。数据来源：本端规划。默认值：000000。配置原则：当存在PLMN相同且TAC连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须一个一个依次增加，使配置更加灵活。如果希望TAC范围有效，跟踪区码起始和终止均不能为000000。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 1-30|参数作用：该参数用于配置跟踪区组的别名，方便记忆和区别。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
命令举例 
`
新增跟踪区组号为1，MCC为"460"、MNC为"11"，跟踪区码"000001"，跟踪区码范围为"000003"到"000008"的配置。
ADD DUALCONNRATRSTTAGROUP:TAGROUPID=1,MCC="460",MNC="11",TAC="000001",TACST="000003",TACEND="000008"
` 
#### 删除双连接RAT限制跟踪区组配置(DEL DUALCONNRATRSTTAGROUP) 
#### 删除双连接RAT限制跟踪区组配置(DEL DUALCONNRATRSTTAGROUP) 
功能说明 
该命令用于删除双连接RAT限制跟踪区组配置。 
注意事项 
本命令删除的数据，在AMF下一次给RAN下发Mobility Restriction List时生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于设置跟踪区组标识，是一组TA的集合。修改影响：无。数据来源：本端规划。默认值：无。配置原则：双连接RAT限制跟踪区组中包含的TA不能重叠。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：该参数用于配置跟踪区(组)的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：该参数用于配置跟踪区(组)的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区(组)的单列跟踪区编号，由运营商在PLMN内统一规划，以16进制数字编码。在移动网络中，规定对终端的物理位置采用跟踪区TA（Tracking Area）来进行管理，TAI（Tracking Area Identity，跟踪区域标识），由国家码（MCC）、移动网络码 （MNC）和TAC （Tracking Area Code，跟踪区码）组成， 跟踪区的划分由运营商统一规划，一般运营商对于TAC的编码方式都有明确的规定，在配置前需要提前确定TAC的分配和编码。修改影响：无。数据来源：全网规划。默认值：000000。配置原则：默认值为000000，表示无效，如果想配置TAC，必须修改为有效值。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区(组)的跟踪区码起始值，由运营商在PLMN内统一规划，以16进制数字编码。修改影响：无。数据来源：全网规划。默认值：000000。配置原则：当存在PLMN相同且TAC连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须一个一个依次增加，使配置更加灵活。如果希望TAC范围有效，跟踪区码起始和终止均不能为000000。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置跟踪区(组)的跟踪区码终止值，由运营商在PLMN内统一规划，以16进制数字编码。修改影响：无。数据来源：本端规划。默认值：000000。配置原则：当存在PLMN相同且TAC连续的若干跟踪区时，可以采用"跟踪区码起始/跟踪区码终止"的方式配置，无须一个一个依次增加，使配置更加灵活。如果希望TAC范围有效，跟踪区码起始和终止均不能为000000。
命令举例 
`
删除跟踪区组号为1，MCC为"460"、MNC为"11"，跟踪区码"000001"，跟踪区码范围为"000003"到"000008"的配置。
DEL DUALCONNRATRSTTAGROUP:TAGROUPID=1,MCC="460",MNC="11",TAC="000001",TACST="000003",TACEND="000008"
` 
#### 查询双连接RAT限制跟踪区组配置(SHOW DUALCONNRATRSTTAGROUP) 
#### 查询双连接RAT限制跟踪区组配置(SHOW DUALCONNRATRSTTAGROUP) 
功能说明 
该命令用于查询双连接RAT限制跟踪区组配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于设置跟踪区组标识，是一组TA的集合。修改影响：无。数据来源：本端规划。默认值：无。配置原则：双连接RAT限制跟踪区组中包含的TA不能重叠。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
tagroupid|跟踪区组标识|参数可选性: 任选参数类型: 数字参数范围: 1-1024|一组TA的集合。双连接RAT限制跟踪区组中包含的TA不能重叠。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|该参数用于配置跟踪区(组)的MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|该参数用于配置跟踪区(组)的MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|该参数用于配置跟踪区(组)的单列跟踪区编号，由运营商在PLMN内统一规划，以16进制数字编码。
tacst|跟踪区码起始|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|该参数用于配置跟踪区(组)的跟踪区码起始值，由运营商在PLMN内统一规划，以16进制数字编码。
tacend|跟踪区码终止|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|该参数用于配置跟踪区(组)的跟踪区码终止值，由运营商在PLMN内统一规划，以16进制数字编码。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 1-30|该参数用于配置跟踪区组的别名。
命令举例 
`
查询所有的跟踪区组配置。
SHOW DUALCONNRATRSTTAGROUP
(No.23) : 
-----------------Namf_Communication_0----------------
操作维护       跟踪区组标识 移动国家码 移动网络码 跟踪区码 跟踪区码起始 跟踪区码终止 别名 
------------------------------------------------------------------------------------------
复制  删除      1            460        11         000001   000003       000008            
------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-08-10 14:34:36 耗时: 0.134 秒
` 
### 双连接RAT限制策略模板配置 
### 双连接RAT限制策略模板配置 
背景知识 
双连接是指用户终端可以连接主基站和从基站，其中只有主基站用于实现控制平面的功能，数据业务可以选择由主基站传输，还是从基站传输，或者二者同时传输。 
从基站和主基站可以是相同RAT的基站，也可以是不同RAT的基站。5GC可以通过移动限制列表中的Primary RAT Restriction和Secondary RAT Restriction信息，通知RAN限制哪些RAT下双连接的建立。 
功能说明 
该配置用于设置PLMN粒度的Primary RAT和Secondary RAT限制策略模板等。 
子主题： 
#### 新增双连接RAT限制策略模板配置(ADD DUALCONNRATRSTPLYPRO) 
#### 新增双连接RAT限制策略模板配置(ADD DUALCONNRATRSTPLYPRO) 
功能说明 
该命令用于新增基于PLMN粒度的双连接RAT限制策略模板配置，每个策略模板中可以包含多个PLMN的Primary RAT和Secondary RAT限制策略。当网络支持按PLMN进行Primary RAT和Secondary RAT限制时，执行该命令。 
注意事项 
 
本命令配置的数据，在AMF下一次给RAN下发Mobility Restriction List时生效。 
 
配置本命令之前，需要确认License项： " AMF支持双连接功能"已激活，否则本命令无法生效。 
 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置双连接RAT限制策略模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
primaryratrstply|Primary RAT限制策略|参数可选性: 必选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置"双连接RAT限制策略模板ID"参数对应的Primary RAT策略。修改影响：无。数据来源：本端规划。默认值：0。配置原则：RAT限制策略，是对各种RAT类型进行编号，根据编号，配置为不同的取值，表示对不同的RAT类型进行限制，每种RAT类型对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64nR-unlicensed限制（nR-unlicensed restriction）：32nR-LEO限制（nR-LEO restriction）：16nR-MEO限制（nR-MEO restriction）：8nR-GEO限制（nR-GEO restriction）：4nR-OTHERSAT限制（nR-OTHERSAT restriction）：2配置此参数时，根据实际情况，将要限制的RAT类型取值相加，例如：要限制e-UTRAN和NR，则参数值应为192（128与64相加），取值及含义如下： 0：所有的RAT类型全部不限制254：所有的RAT类型全部限制如果是0到254之间的整数：根据具体数值确认需要限制的RAT类型，比如12，表示限制的RAT为nR-MEO和nR-GEO。
secratrstply|Secondary RAT限制策略|参数可选性: 必选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置"双连接RAT限制策略模板ID"参数对应的Secondary RAT策略。修改影响：无。数据来源：本端规划。默认值：0。配置原则：RAT限制策略，是对各种RAT类型进行编号，根据编号，配置为不同的取值，表示对不同的RAT类型进行限制，每种RAT类型对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64e-UTRA-unlicensed限制（e-UTRA-unlicensed restriction）:32nR-unlicensed限制（nR-unlicensed restriction）:16配置此参数时，根据实际情况，将要限制的RAT类型取值相加，例如：要限制e-UTRAN和nR，则参数值应为192（128与64相加），取值及含义如下： 0：所有的RAT类型全部不限制240：所有的RAT类型全部限制如果是0到240之间的整数：根据具体数值确认需要限制的RAT类型，比如48，表示限制的RAT为e-UTRA-unlicensed和nR-unlicensed。
命令举例 
`
新增双连接RAT限制策略模板ID为1, 移动国家码为"460", 移动网络码为"11",Primary RAT限制策略为1，Secondary RAT限制策略为1的配置记录。
ADD DUALCONNRATRSTPLYPRO:DUALRATRSTPROFILEID=1,MCC="460",MNC="11",PRIMARYRATRSTPLY=1,SECRATRSTPLY=1
` 
#### 修改双连接RAT限制策略模板配置(SET DUALCONNRATRSTPLYPRO) 
#### 修改双连接RAT限制策略模板配置(SET DUALCONNRATRSTPLYPRO) 
功能说明 
该命令用于修改基于PLMN粒度的双连接RAT限制策略模板配置。 
注意事项 
本命令修改的数据，在AMF下一次给RAN下发Mobility Restriction List时生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置双连接RAT限制策略模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
primaryratrstply|Primary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置"双连接RAT限制策略模板ID"参数对应的Primary RAT策略。修改影响：无。数据来源：本端规划。默认值：0。配置原则：RAT限制策略，是对各种RAT类型进行编号，根据编号，配置为不同的取值，表示对不同的RAT类型进行限制，每种RAT类型对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64nR-unlicensed限制（nR-unlicensed restriction）：32nR-LEO限制（nR-LEO restriction）：16nR-MEO限制（nR-MEO restriction）：8nR-GEO限制（nR-GEO restriction）：4nR-OTHERSAT限制（nR-OTHERSAT restriction）：2配置此参数时，根据实际情况，将要限制的RAT类型取值相加，例如：要限制e-UTRAN和NR，则参数值应为192（128与64相加），取值及含义如下： 0：所有的RAT类型全部不限制254：所有的RAT类型全部限制如果是0到254之间的整数：根据具体数值确认需要限制的RAT类型，比如12，表示限制的RAT为nR-MEO和nR-GEO。
secratrstply|Secondary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：该参数用于配置"双连接RAT限制策略模板ID"参数对应的Secondary RAT策略。修改影响：无。数据来源：本端规划。默认值：0。配置原则：RAT限制策略，是对各种RAT类型进行编号，根据编号，配置为不同的取值，表示对不同的RAT类型进行限制，每种RAT类型对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64e-UTRA-unlicensed限制（e-UTRA-unlicensed restriction）:32nR-unlicensed限制（nR-unlicensed restriction）:16配置此参数时，根据实际情况，将要限制的RAT类型取值相加，例如：要限制e-UTRAN和nR，则参数值应为192（128与64相加），取值及含义如下： 0：所有的RAT类型全部不限制240：所有的RAT类型全部限制如果是0到240之间的整数：根据具体数值确认需要限制的RAT类型，比如48，表示限制的RAT为e-UTRA-unlicensed和nR-unlicensed。
命令举例 
`
将双连接RAT限制策略模板ID为1, 移动国家码为"460", 移动网络码为"11"的配置中Primary RAT限制策略修改为2，Secondary RAT限制策略修改为2。
SET DUALCONNRATRSTPLYPRO:DUALRATRSTPROFILEID=1,MCC="460",MNC="11",PRIMARYRATRSTPLY=2,SECRATRSTPLY=2
` 
#### 删除双连接RAT限制策略模板配置(DEL DUALCONNRATRSTPLYPRO) 
#### 删除双连接RAT限制策略模板配置(DEL DUALCONNRATRSTPLYPRO) 
功能说明 
该命令用于删除基于PLMN粒度的双连接RAT限制策略模板配置。 
注意事项 
本命令删除的数据，在AMF下一次给RAN下发Mobility Restriction List时生效。 
输入参数说明 
标识|名称|类型|说明
---|---|---|---
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 必选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置双连接RAT限制策略模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
命令举例 
`
删除双连接RAT限制策略模板ID为1, 移动国家码为"460", 移动网络码为"11"的配置。
DEL DUALCONNRATRSTPLYPRO:DUALRATRSTPROFILEID=1,MCC="460",MNC="11"
` 
#### 查询双连接RAT限制策略模板配置(SHOW DUALCONNRATRSTPLYPRO) 
#### 查询双连接RAT限制策略模板配置(SHOW DUALCONNRATRSTPLYPRO) 
功能说明 
该命令用于查询基于PLMN粒度的双连接RAT限制策略模板配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 1-1024|参数作用：该参数用于配置双连接RAT限制策略模板ID。修改影响：无。数据来源：本端规划。默认值：无。配置原则：无。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。修改影响：无。数据来源：全网规划。默认值：无。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 1-1024|该参数用于配置双连接RAT限制策略模板ID。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。
primaryratrstply|Primary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|该参数用于配置"双连接RAT限制策略模板ID"参数对应的Primary RAT策略。
secratrstply|Secondary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|该参数用于配置"双连接RAT限制策略模板ID"参数对应的Secondary RAT策略。
命令举例 
`
查询所有双连接RAT限制策略模板配置。
SHOW DUALCONNRATRSTPLYPRO
(No.6) :SHOW DUALCONNRATRSTPLYPRO:
-----------------------------------------Namf_Communication_0-----------------------------------------
操作维护       双连接RAT限制策略模板ID  移动国家码 移动网络码 Primary RAT限制策略 Secondary RAT限制策略
------------------------------------------------------------------------------------------------------
复制 修改 删除 1                         460        11        2                   2
------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间：2022-08-31 16:13:42  耗时: 0.993 秒
` 
### 全局双连接RAT限制策略配置 
### 全局双连接RAT限制策略配置 
背景知识 
双连接是指用户终端可以连接主基站和从基站，其中只有主基站用于实现控制平面的功能，数据业务可以选择由主基站传输，还是从基站传输，或者二者同时传输。 
从基站和主基站可以是相同RAT的基站，也可以是不同RAT的基站。5GC可以通过移动限制列表中的Primary RAT Restriction和Secondary RAT Restriction信息，通知RAN限制哪些RAT下双连接的建立。 
功能说明 
该配置用于设置双连接RAT限制策略功能开关、双连接RAT限制获取方式、双连接RAT限制策略模板、默认双连接RAT限制策略等。 
子主题： 
#### 修改全局双连接RAT限制策略配置(SET GLOBALDUALCONNRATRSTPLY) 
#### 修改全局双连接RAT限制策略配置(SET GLOBALDUALCONNRATRSTPLY) 
功能说明 
该命令用于修改全局双连接RAT限制策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ifsprtdualratrst|支持双连接RAT Restriction|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置双连接RAT限制功能开关。如果为“是”，则在Mobility Restriction List中才可能携带Extended RAT Restriction Information信息，取值及含义如下： 是：支持双连接否：不支持双连接修改影响：修改该参数，影响AMF是否支持双连接，在Mobility Restriction List中是否携带Extended RAT Restriction Information信息。数据来源：本端规划 。默认值：不支持。配置原则：无。
dualratrstmethod|双连接RAT限制获取方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIPTION|参数作用：该参数用于配置全局双连接RAT限制信息获取方式：取签约双连接RAT限制信息或本地配置的双连接RAT限制信息，取值及含义如下： 0：签约值1：本地配置修改影响：修改该参数，影响AMF双连接RAT限制信息获取方式。数据来源：本端规划 。默认值：签约值。配置原则：无。
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置全局双连接RAT限制策略模板ID，默认值为0。当"双连接RAT限制获取方式"配置为"本地配置"，本参数才有效。当本参数设置为0时，表示不支持按PLMN配置双连接RAT限制策略，双连接RAT限制信息中包含当前服务PLMN的双连接RAT限制，取值为"默认Primary RAT限制策略配置"和"默认Secondary RAT限制策略配置"中配置信息。当本参数设置为非0时，根据“双连接RAT限制策略模板配置”中关联的各个PLMN的双连接RAT限制策略，设置双连接RAT限制信息。取值及含义如下： 0：不支持按PLMN配置双连接RAT限制策略1-1024：根据“双连接RAT限制策略模板配置”中关联的各个PLMN的双连接RAT限制策略，设置双连接RAT限制信息修改影响：修改该参数，影响AMF双连接RAT策略限制的取值。数据来源：本端规划 。默认值：0。配置原则：无。
defprimaryratrstply|默认Primary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64nR-unlicensed限制（nR-unlicensed restriction）：32nR-LEO限制（nR-LEO restriction）：16nR-MEO限制（nR-MEO restriction）：8nR-GEO限制（nR-GEO restriction）：4nR-OTHERSAT限制（nR-OTHERSAT restriction）：2该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制254：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Primary策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
defsecratrstply|默认Secondary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）:128nR限制（nR restriction）:64e-UTRA-unlicensed限制（e-UTRA-unlicensed restriction）:32nR-unlicensed限制（nR-unlicensed restriction）:16该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制240：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Second策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
命令举例 
`
修改全局双连接RAT限制策略配置
SET GLOBALDUALCONNRATRSTPLY:IFSPRTDUALRATRST="YES",DUALRATRSTMETHOD="LOCALCONFIGURATION",DUALRATRSTPROFILEID=1,DEFPRIMARYRATRSTPLY=128,DEFSECRATRSTPLY=64
` 
#### 查询全局双连接RAT限制策略配置(SHOW GLOBALDUALCONNRATRSTPLY) 
#### 查询全局双连接RAT限制策略配置(SHOW GLOBALDUALCONNRATRSTPLY) 
功能说明 
该命令用于查询全局双连接RAT限制策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ifsprtdualratrst|支持双连接RAT Restriction|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置双连接RAT限制功能开关。如果为“是”，则在Mobility Restriction List中才可能携带Extended RAT Restriction Information信息，取值及含义如下： 是：支持双连接否：不支持双连接修改影响：修改该参数，影响AMF是否支持双连接，在Mobility Restriction List中是否携带Extended RAT Restriction Information信息。数据来源：本端规划 。默认值：不支持。配置原则：无。
dualratrstmethod|双连接RAT限制获取方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIPTION|参数作用：该参数用于配置全局双连接RAT限制信息获取方式：取签约双连接RAT限制信息或本地配置的双连接RAT限制信息，取值及含义如下： 0：签约值1：本地配置修改影响：修改该参数，影响AMF双连接RAT限制信息获取方式。数据来源：本端规划 。默认值：签约值。配置原则：无。
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置全局双连接RAT限制策略模板ID，默认值为0。当"双连接RAT限制获取方式"配置为"本地配置"，本参数才有效。当本参数设置为0时，表示不支持按PLMN配置双连接RAT限制策略，双连接RAT限制信息中包含当前服务PLMN的双连接RAT限制，取值为"默认Primary RAT限制策略配置"和"默认Secondary RAT限制策略配置"中配置信息。当本参数设置为非0时，根据“双连接RAT限制策略模板配置”中关联的各个PLMN的双连接RAT限制策略，设置双连接RAT限制信息。取值及含义如下： 0：不支持按PLMN配置双连接RAT限制策略1-1024：根据“双连接RAT限制策略模板配置”中关联的各个PLMN的双连接RAT限制策略，设置双连接RAT限制信息修改影响：修改该参数，影响AMF双连接RAT策略限制的取值。数据来源：本端规划 。默认值：0。配置原则：无。
defprimaryratrstply|默认Primary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64nR-unlicensed限制（nR-unlicensed restriction）：32nR-LEO限制（nR-LEO restriction）：16nR-MEO限制（nR-MEO restriction）：8nR-GEO限制（nR-GEO restriction）：4nR-OTHERSAT限制（nR-OTHERSAT restriction）：2该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制254：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Primary策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
defsecratrstply|默认Secondary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）:128nR限制（nR restriction）:64e-UTRA-unlicensed限制（e-UTRA-unlicensed restriction）:32nR-unlicensed限制（nR-unlicensed restriction）:16该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制240：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Second策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ifsprtdualratrst|支持双连接RAT Restriction|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NO|参数作用：该参数用于配置双连接RAT限制功能开关。如果为“是”，则在Mobility Restriction List中才可能携带Extended RAT Restriction Information信息，取值及含义如下： 是：支持双连接否：不支持双连接修改影响：修改该参数，影响AMF是否支持双连接，在Mobility Restriction List中是否携带Extended RAT Restriction Information信息。数据来源：本端规划 。默认值：不支持。配置原则：无。
dualratrstmethod|双连接RAT限制获取方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIPTION|参数作用：该参数用于配置全局双连接RAT限制信息获取方式：取签约双连接RAT限制信息或本地配置的双连接RAT限制信息，取值及含义如下： 0：签约值1：本地配置修改影响：修改该参数，影响AMF双连接RAT限制信息获取方式。数据来源：本端规划 。默认值：签约值。配置原则：无。
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置全局双连接RAT限制策略模板ID，默认值为0。当"双连接RAT限制获取方式"配置为"本地配置"，本参数才有效。当本参数设置为0时，表示不支持按PLMN配置双连接RAT限制策略，双连接RAT限制信息中包含当前服务PLMN的双连接RAT限制，取值为"默认Primary RAT限制策略配置"和"默认Secondary RAT限制策略配置"中配置信息。当本参数设置为非0时，根据“双连接RAT限制策略模板配置”中关联的各个PLMN的双连接RAT限制策略，设置双连接RAT限制信息。取值及含义如下： 0：不支持按PLMN配置双连接RAT限制策略1-1024：根据“双连接RAT限制策略模板配置”中关联的各个PLMN的双连接RAT限制策略，设置双连接RAT限制信息修改影响：修改该参数，影响AMF双连接RAT策略限制的取值。数据来源：本端规划 。默认值：0。配置原则：无。
defprimaryratrstply|默认Primary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64nR-unlicensed限制（nR-unlicensed restriction）：32nR-LEO限制（nR-LEO restriction）：16nR-MEO限制（nR-MEO restriction）：8nR-GEO限制（nR-GEO restriction）：4nR-OTHERSAT限制（nR-OTHERSAT restriction）：2该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制254：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Primary策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
defsecratrstply|默认Secondary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）:128nR限制（nR restriction）:64e-UTRA-unlicensed限制（e-UTRA-unlicensed restriction）:32nR-unlicensed限制（nR-unlicensed restriction）:16该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制修改影响：修改该参数，影响AMF双连接RAT Second策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
命令举例 
`
查询全局双连接RAT限制策略配置。
SHOW GLOBALDUALCONNRATRSTPLY:
(No.1) : SHOW GLOBALDUALCONNRATRSTPLY:
-----------------Namf_Communication_0----------------
操作维护       支持双连接RAT Restriction 双连接RAT限制获取方式 双连接RAT限制策略模板ID 默认Primary RAT限制策略 默认Secondary RAT限制策略 
-----------------------------------------------------------------------------------------------------------------------------------------
修改           否                        基于签约              0                       0                       0                         
-----------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-08-29 18:41:24 耗时: 0.26 秒
` 
### 基于SUPI号段和区域的双连接RAT限制策略配置 
### 基于SUPI号段和区域的双连接RAT限制策略配置 
背景知识 
双连接是指用户终端可以连接主基站和从基站，其中只有主基站用于实现控制平面的功能，数据业务可以选择由主基站传输，还是从基站传输，或者二者同时传输。 
从基站和主基站可以是相同RAT的基站，也可以是不同RAT的基站。5GC可以通过移动限制列表中的Primary RAT Restriction和Secondary RAT Restriction信息，通知RAN限制哪些RAT下双连接的建立。 
功能说明 
该命令用于设置基于SUPI号段和区域的双连接RAT限制信息策略，包括双连接RAT限制获取方式（双连接RAT限制信息策略取签约信息还是本地配置）和双连接RAT限制策略模板ID。当双连接RAT限制获取方式为“本地配置”时双连接RAT限制策略模板ID有效。如果双连接RAT限制策略模板ID为0，则双连接RAT限制列表中仅包含当前服务PLMN的RAT限制策略，双连接RAT限制从全局双连接RAT限制策略中获取。如果Secondary RAT限制策略模板ID为非0，则需要通过ADD DUALCONNRATRSTPLY命令，新增与PLMN相关的双连接RAT限制策略模板。 
子主题： 
#### 新增SUPI号段和区域的双连接RAT限制策略配置(ADD SUPIAREADUALCONNRATRSTPLY) 
#### 新增SUPI号段和区域的双连接RAT限制策略配置(ADD SUPIAREADUALCONNRATRSTPLY) 
功能说明 
该命令用于新增SUPI号段和区域的双连接RAT限制策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：本参数用于设置终端的SUPI号段，根据运营商实际规划需要而定。终端的真实身份在5GC网络中被称为SUPI（Subscriber Permanent Identifier，用户永久标识），类似于2/3/4G网络中的IMSI（International Mobile Subscriber Identity，国际移动用户标识），取值及含义如下： 46011：SUPI号段修改影响：修改该参数，影响SUPI号段的配置值。数据来源：本端规划 。默认值：不支持。配置原则：无。
areatype|区域类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AllAMFAREA|参数作用：该参数用于配置SUPI号段所在区域的区域类型，取值及含义如下： 0：整个AMF区域(All AMF Area)1：PLMN区域(PLMN Area)2：TA组区域(TA Group)3：单个TA区域(Single TA)修改影响：修改该参数，影响SUPI号段所在区域的区域类型。数据来源：本端规划 。默认值：不支持。配置原则：无。
tagroupid|跟踪区组标识|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置区域类型为TA组区域时的TA组标识。当区域类型为TA组区域时，该参数必须填写有效（1~1024），否则必须为无效值0。该参数引用"Secondary RAT限制跟踪区组配置"中的跟踪区组标识字段，引用的值需要先有配置，取值及含义如下： 0：无效值1-1024：引用"Secondary RAT限制跟踪区组配置"中的跟踪区组标识字段，引用的值需要先有配置。修改影响：修改该参数，影响配置区域类型为TA组区域时的TA组标识。数据来源：本端规划 。默认值：0。配置原则：无。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。当区域类型为PLMN区域或者单个TA区域时，该参数必须填写有效，否则必须为无效值全F，取值及含义如下： FFF：无效值修改影响：修改该参数，影响MCC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3默认值: FFF|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。当区域类型为PLMN区域或者单个TA区域时，该参数必须填写有效，否则必须为无效值全F，取值及含义如下： FFF：无效值修改影响：修改该参数，影响MNC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
tac|跟踪区码|参数可选性: 必选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置区域类型为单个TA区域时的TAC （Tracking Area Code，跟踪区码）。当区域类型为单个TA区域时，该参数必须填写有效，否则必须为无效值全F。在移动网络中，规定对终端的物理位置采用跟踪区TA（Tracking Area）来进行管理，TAI（Tracking Area Identity，跟踪区域标识），由国家码（MCC）、移动网络码 （MNC）和TAC （Tracking Area Code，跟踪区码）组成， 跟踪区的划分由运营商统一规划，一般运营商对于TAC的编码方式都有明确的规定，在配置前需要提前确定TAC的分配和编码，取值及含义如下： 000000：无效值修改影响：修改该参数，影响TAC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
dualratrstmethod|双连接RAT限制获取方式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIPTION|参数作用：该参数用于配置全局双连接RAT限制信息获取方式：取签约双连接RAT限制信息或本地配置的双连接RAT限制信息，取值及含义如下： 0：签约值1：本地配置修改影响：修改该参数，影响AMF双连接RAT限制信息获取方式。数据来源：本端规划 。默认值：签约值。配置原则：无。
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置双连接RAT限制策略模板ID，默认值为0。当"双连接RAT限制获取方式"配置为"本地配置"，本参数才有效。当本参数设置为0时，表示不支持按PLMN配置双连接RAT限制策略，双连接RAT限制信息中包含当前服务PLMN的双连接RAT限制，取值为默认Primary RAT限制策略和默认Secondary RAT限制策略信息。当本参数设置为非0时，根据“双连接RAT限制策略模板配置”中关联的各个PLMN 双连接RAT限制策略，设置双连接RAT限制信息，取值及含义如下： 0:表示不支持按PLMN配置双连接RAT限制策略1-1024:根据“双连接RAT限制策略模板配置”中关联的各个PLMN 双连接RAT限制策略修改影响：修改该参数，影响双连接RAT限制策略功能。数据来源：本端规划 。默认值：0。配置原则：无。
defprimaryratrstply|默认Primary RAT限制策略|参数可选性: 必选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64nR-unlicensed限制（nR-unlicensed restriction）：32nR-LEO限制（nR-LEO restriction）：16nR-MEO限制（nR-MEO restriction）：8nR-GEO限制（nR-GEO restriction）：4nR-OTHERSAT限制（nR-OTHERSAT restriction）：2该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制254：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Primary策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
defsecratrstply|默认Secondary RAT限制策略|参数可选性: 必选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）:128nR限制（nR restriction）:64e-UTRA-unlicensed限制（e-UTRA-unlicensed restriction）:32nR-unlicensed限制（nR-unlicensed restriction）:16该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制240：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Second策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
命令举例 
`
新增SUPI号段为46011123和区域为单个TA的双连接RAT限制策略配置
ADD SUPIAREADUALCONNRATRSTPLY:SUPISEG="46011123",AREATYPE="TA",TAGROUPID=0,MCC="460",MNC="11",TAC="000004",DUALRATRSTMETHOD="LOCALCONFIGURATION",DUALRATRSTPROFILEID=0,DEFPRIMARYRATRSTPLY=128,DEFSECRATRSTPLY=64
` 
#### 修改SUPI号段和区域的双连接RAT限制策略配置(SET SUPIAREADUALCONNRATRSTPLY) 
#### 修改SUPI号段和区域的双连接RAT限制策略配置(SET SUPIAREADUALCONNRATRSTPLY) 
功能说明 
该命令用于修改SUPI号段和区域的双连接RAT限制策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：本参数用于设置终端的SUPI号段，根据运营商实际规划需要而定。终端的真实身份在5GC网络中被称为SUPI（Subscriber Permanent Identifier，用户永久标识），类似于2/3/4G网络中的IMSI（International Mobile Subscriber Identity，国际移动用户标识），取值及含义如下： 46011：SUPI号段修改影响：修改该参数，影响SUPI号段的配置值。数据来源：本端规划 。默认值：不支持。配置原则：无。
areatype|区域类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AllAMFAREA|参数作用：该参数用于配置SUPI号段所在区域的区域类型，取值及含义如下： 0：整个AMF区域(All AMF Area)1：PLMN区域(PLMN Area)2：TA组区域(TA Group)3：单个TA区域(Single TA)修改影响：修改该参数，影响SUPI号段所在区域的区域类型。数据来源：本端规划 。默认值：不支持。配置原则：无。
tagroupid|跟踪区组标识|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置区域类型为TA组区域时的TA组标识。当区域类型为TA组区域时，该参数必须填写有效（1~1024），否则必须为无效值0。该参数引用"Secondary RAT限制跟踪区组配置"中的跟踪区组标识字段，引用的值需要先有配置，取值及含义如下： 0：无效值1-1024：引用"Secondary RAT限制跟踪区组配置"中的跟踪区组标识字段，引用的值需要先有配置。修改影响：修改该参数，影响配置区域类型为TA组区域时的TA组标识。数据来源：本端规划 。默认值：0。配置原则：无。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。当区域类型为PLMN区域或者单个TA区域时，该参数必须填写有效，否则必须为无效值全F，取值及含义如下： FFF：无效值修改影响：修改该参数，影响MCC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3默认值: FFF|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。当区域类型为PLMN区域或者单个TA区域时，该参数必须填写有效，否则必须为无效值全F，取值及含义如下： FFF：无效值修改影响：修改该参数，影响MNC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
tac|跟踪区码|参数可选性: 必选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置区域类型为单个TA区域时的TAC （Tracking Area Code，跟踪区码）。当区域类型为单个TA区域时，该参数必须填写有效，否则必须为无效值全F。在移动网络中，规定对终端的物理位置采用跟踪区TA（Tracking Area）来进行管理，TAI（Tracking Area Identity，跟踪区域标识），由国家码（MCC）、移动网络码 （MNC）和TAC （Tracking Area Code，跟踪区码）组成， 跟踪区的划分由运营商统一规划，一般运营商对于TAC的编码方式都有明确的规定，在配置前需要提前确定TAC的分配和编码，取值及含义如下： 000000：无效值修改影响：修改该参数，影响TAC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
dualratrstmethod|双连接RAT限制获取方式|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIPTION|参数作用：该参数用于配置全局双连接RAT限制信息获取方式：取签约双连接RAT限制信息或本地配置的双连接RAT限制信息，取值及含义如下： 0：签约值1：本地配置修改影响：修改该参数，影响AMF双连接RAT限制信息获取方式。数据来源：本端规划 。默认值：签约值。配置原则：无。
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 必选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置双连接RAT限制策略模板ID，默认值为0。当"双连接RAT限制获取方式"配置为"本地配置"，本参数才有效。当本参数设置为0时，表示不支持按PLMN配置双连接RAT限制策略，双连接RAT限制信息中包含当前服务PLMN的双连接RAT限制，取值为默认Primary RAT限制策略和默认Secondary RAT限制策略信息。当本参数设置为非0时，根据“双连接RAT限制策略模板配置”中关联的各个PLMN 双连接RAT限制策略，设置双连接RAT限制信息，取值及含义如下： 0:表示不支持按PLMN配置双连接RAT限制策略1-1024:根据“双连接RAT限制策略模板配置”中关联的各个PLMN 双连接RAT限制策略修改影响：修改该参数，影响双连接RAT限制策略功能。数据来源：本端规划 。默认值：0。配置原则：无。
defprimaryratrstply|默认Primary RAT限制策略|参数可选性: 必选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64nR-unlicensed限制（nR-unlicensed restriction）：32nR-LEO限制（nR-LEO restriction）：16nR-MEO限制（nR-MEO restriction）：8nR-GEO限制（nR-GEO restriction）：4nR-OTHERSAT限制（nR-OTHERSAT restriction）：2该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制254：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Primary策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
defsecratrstply|默认Secondary RAT限制策略|参数可选性: 必选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）:128nR限制（nR restriction）:64e-UTRA-unlicensed限制（e-UTRA-unlicensed restriction）:32nR-unlicensed限制（nR-unlicensed restriction）:16该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制240：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Second策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
命令举例 
`
修改SUPI号段和区域的双连接RAT限制策略配置
SET SUPIAREADUALCONNRATRSTPLY:SUPISEG=46011123,AREATYPE=TA,TAGROUPID=0,MCC=460,MNC=11,TAC=000004,DUALRATRSTPROFILEID=0,DEFPRIMARYRATRSTPLY=128,DEFSECRATRSTPLY=64
` 
#### 删除SUPI号段和区域的双连接RAT限制策略配置(DEL SUPIAREADUALCONNRATRSTPLY) 
#### 删除SUPI号段和区域的双连接RAT限制策略配置(DEL SUPIAREADUALCONNRATRSTPLY) 
功能说明 
该命令用于删除SUPI号段和区域的双连接RAT限制策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|参数作用：本参数用于设置终端的SUPI号段，根据运营商实际规划需要而定。终端的真实身份在5GC网络中被称为SUPI（Subscriber Permanent Identifier，用户永久标识），类似于2/3/4G网络中的IMSI（International Mobile Subscriber Identity，国际移动用户标识），取值及含义如下： 46011：SUPI号段修改影响：修改该参数，影响SUPI号段的配置值。数据来源：本端规划 。默认值：不支持。配置原则：无。
areatype|区域类型|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AllAMFAREA|参数作用：该参数用于配置SUPI号段所在区域的区域类型，取值及含义如下： 0：整个AMF区域(All AMF Area)1：PLMN区域(PLMN Area)2：TA组区域(TA Group)3：单个TA区域(Single TA)修改影响：修改该参数，影响SUPI号段所在区域的区域类型。数据来源：本端规划 。默认值：不支持。配置原则：无。
tagroupid|跟踪区组标识|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置区域类型为TA组区域时的TA组标识。当区域类型为TA组区域时，该参数必须填写有效（1~1024），否则必须为无效值0。该参数引用"Secondary RAT限制跟踪区组配置"中的跟踪区组标识字段，引用的值需要先有配置，取值及含义如下： 0：无效值1-1024：引用"Secondary RAT限制跟踪区组配置"中的跟踪区组标识字段，引用的值需要先有配置。修改影响：修改该参数，影响配置区域类型为TA组区域时的TA组标识。数据来源：本端规划 。默认值：0。配置原则：无。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。当区域类型为PLMN区域或者单个TA区域时，该参数必须填写有效，否则必须为无效值全F，取值及含义如下： FFF：无效值修改影响：修改该参数，影响MCC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3默认值: FFF|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。当区域类型为PLMN区域或者单个TA区域时，该参数必须填写有效，否则必须为无效值全F，取值及含义如下： FFF：无效值修改影响：修改该参数，影响MNC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置区域类型为单个TA区域时的TAC （Tracking Area Code，跟踪区码）。当区域类型为单个TA区域时，该参数必须填写有效，否则必须为无效值全F。在移动网络中，规定对终端的物理位置采用跟踪区TA（Tracking Area）来进行管理，TAI（Tracking Area Identity，跟踪区域标识），由国家码（MCC）、移动网络码 （MNC）和TAC （Tracking Area Code，跟踪区码）组成， 跟踪区的划分由运营商统一规划，一般运营商对于TAC的编码方式都有明确的规定，在配置前需要提前确定TAC的分配和编码，取值及含义如下： 000000：无效值修改影响：修改该参数，影响TAC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
命令举例 
`
删除SUPI号段为46011123和区域为单个TA的双连接RAT限制策略配置
DEL SUPIAREADUALCONNRATRSTPLY:SUPISEG=46011123,AREATYPE=TA,TAGROUPID=0,MCC=460,MNC=11,TAC=000004
` 
#### 查询SUPI号段和区域的双连接RAT限制策略配置(SHOW SUPIAREADUALCONNRATRSTPLY) 
#### 查询SUPI号段和区域的双连接RAT限制策略配置(SHOW SUPIAREADUALCONNRATRSTPLY) 
功能说明 
该命令用于查询SUPI号段和区域的双连接RAT限制策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：本参数用于设置终端的SUPI号段，根据运营商实际规划需要而定。终端的真实身份在5GC网络中被称为SUPI（Subscriber Permanent Identifier，用户永久标识），类似于2/3/4G网络中的IMSI（International Mobile Subscriber Identity，国际移动用户标识），取值及含义如下： 46011：SUPI号段修改影响：修改该参数，影响SUPI号段的配置值。数据来源：本端规划 。默认值：不支持。配置原则：无。
areatype|区域类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AllAMFAREA|参数作用：该参数用于配置SUPI号段所在区域的区域类型，取值及含义如下： 0：整个AMF区域(All AMF Area)1：PLMN区域(PLMN Area)2：TA组区域(TA Group)3：单个TA区域(Single TA)修改影响：修改该参数，影响SUPI号段所在区域的区域类型。数据来源：本端规划 。默认值：不支持。配置原则：无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|参数作用：本参数用于设置终端的SUPI号段，根据运营商实际规划需要而定。终端的真实身份在5GC网络中被称为SUPI（Subscriber Permanent Identifier，用户永久标识），类似于2/3/4G网络中的IMSI（International Mobile Subscriber Identity，国际移动用户标识），取值及含义如下： 46011：SUPI号段修改影响：修改该参数，影响SUPI号段的配置值。数据来源：本端规划 。默认值：不支持。配置原则：无。
areatype|区域类型|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AllAMFAREA|参数作用：该参数用于配置SUPI号段所在区域的区域类型，取值及含义如下： 0：整个AMF区域(All AMF Area)1：PLMN区域(PLMN Area)2：TA组区域(TA Group)3：单个TA区域(Single TA)修改影响：修改该参数，影响SUPI号段所在区域的区域类型。数据来源：本端规划 。默认值：不支持。配置原则：无。
tagroupid|跟踪区组标识|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置区域类型为TA组区域时的TA组标识。当区域类型为TA组区域时，该参数必须填写有效（1~1024），否则必须为无效值0。该参数引用"Secondary RAT限制跟踪区组配置"中的跟踪区组标识字段，引用的值需要先有配置，取值及含义如下： 0：无效值1-1024：引用"Secondary RAT限制跟踪区组配置"中的跟踪区组标识字段，引用的值需要先有配置。修改影响：修改该参数，影响配置区域类型为TA组区域时的TA组标识。数据来源：本端规划 。默认值：0。配置原则：无。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3默认值: FFF|参数作用：MCC（Mobile Country Code，移动国家码），由运营商根据国际电联分配的国家码进行规划配置，用于在移动网络中，唯一标识一个国家信息。当区域类型为PLMN区域或者单个TA区域时，该参数必须填写有效，否则必须为无效值全F，取值及含义如下： FFF：无效值修改影响：修改该参数，影响MCC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3默认值: FFF|参数作用：MNC（Mobile Network Code，移动网络号），由运营商根据国际电联分配的网络号进行规划配置，用于在移动网络中，基于MCC唯一标识一个运营商网络信息。MCC和MNC标识唯一的一个PLMN，标识移动用户的归属PLMN，也就是移动用户归属的运营商的移动网络。当区域类型为PLMN区域或者单个TA区域时，该参数必须填写有效，否则必须为无效值全F，取值及含义如下： FFF：无效值修改影响：修改该参数，影响MNC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
tac|跟踪区码|参数可选性: 任选参数类型: 字符串参数范围: 6-6默认值: 000000|参数作用：该参数用于配置区域类型为单个TA区域时的TAC （Tracking Area Code，跟踪区码）。当区域类型为单个TA区域时，该参数必须填写有效，否则必须为无效值全F。在移动网络中，规定对终端的物理位置采用跟踪区TA（Tracking Area）来进行管理，TAI（Tracking Area Identity，跟踪区域标识），由国家码（MCC）、移动网络码 （MNC）和TAC （Tracking Area Code，跟踪区码）组成， 跟踪区的划分由运营商统一规划，一般运营商对于TAC的编码方式都有明确的规定，在配置前需要提前确定TAC的分配和编码，取值及含义如下： 000000：无效值修改影响：修改该参数，影响TAC的值。数据来源：本端规划 。默认值：不支持。配置原则：无。
dualratrstmethod|双连接RAT限制获取方式|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: SUBSCRIPTION|参数作用：该参数用于配置全局双连接RAT限制信息获取方式：取签约双连接RAT限制信息或本地配置的双连接RAT限制信息，取值及含义如下： 0：签约值1：本地配置修改影响：修改该参数，影响AMF双连接RAT限制信息获取方式。数据来源：本端规划 。默认值：签约值。配置原则：无。
dualratrstprofileid|双连接RAT限制策略模板ID|参数可选性: 任选参数类型: 数字参数范围: 0-1024默认值: 0|参数作用：该参数用于配置双连接RAT限制策略模板ID，默认值为0。当"双连接RAT限制获取方式"配置为"本地配置"，本参数才有效。当本参数设置为0时，表示不支持按PLMN配置双连接RAT限制策略，双连接RAT限制信息中包含当前服务PLMN的双连接RAT限制，取值为默认Primary RAT限制策略和默认Secondary RAT限制策略信息。当本参数设置为非0时，根据“双连接RAT限制策略模板配置”中关联的各个PLMN 双连接RAT限制策略，设置双连接RAT限制信息，取值及含义如下： 0:表示不支持按PLMN配置双连接RAT限制策略1-1024:根据“双连接RAT限制策略模板配置”中关联的各个PLMN 双连接RAT限制策略修改影响：修改该参数，影响双连接RAT限制策略功能。数据来源：本端规划 。默认值：0。配置原则：无。
defprimaryratrstply|默认Primary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）：128nR限制（nR restriction）：64nR-unlicensed限制（nR-unlicensed restriction）：32nR-LEO限制（nR-LEO restriction）：16nR-MEO限制（nR-MEO restriction）：8nR-GEO限制（nR-GEO restriction）：4nR-OTHERSAT限制（nR-OTHERSAT restriction）：2该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制254：RAT类型全部限制修改影响：修改该参数，影响AMF双连接RAT Primary策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
defsecratrstply|默认Secondary RAT限制策略|参数可选性: 任选参数类型: 数字参数范围: 0-255默认值: 0|参数作用：每种RAT类型如果要限制，其对应的十进制取值如下：e-UTRA 限制（e-UTRA restriction）:128nR限制（nR restriction）:64e-UTRA-unlicensed限制（e-UTRA-unlicensed restriction）:32nR-unlicensed限制（nR-unlicensed restriction）:16该参数配置时，根据实际情况，将要限制的RAT类型取值相加。取值及含义如下： 0：RAT类型全部不限制修改影响：修改该参数，影响AMF双连接RAT Second策略限制类型。数据来源：本端规划 。默认值：0。配置原则：无。
命令举例 
`
查询SUPI号段和区域的双连接RAT限制策略配置
SHOW SUPIAREADUALCONNRATRSTPLY:
(No.3) : SHOW SUPIAREADUALCONNRATRSTPLY:
-----------------Namf_Communication_0----------------
操作维护       SUPI号段 区域类型   跟踪区组标识 移动国家码 移动网络码 跟踪区码 双连接RAT限制获取方式 双连接RAT限制策略模板ID 默认Primary RAT限制策略 默认Secondary RAT限制策略 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 46011123 单个TA区域 0            460        11         000004   基于本地配置          0                       128                     64                        
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2022-08-29 18:47:06 耗时: 0.158 秒
` 
# NPN配置 
# NPN配置 
背景知识 
NPN（Non-Public Network，非公共网络）包括两种类型： 
 
SNPN（Stand-alone Non-Public Network）：独立的NPN，不依赖PLMN。 
 
PNI-NPN（Public Network Integrated NPN）：集成在公共网络的NPN，在PLMN上提供NPN。 
 
功能说明 
NPN配置包括PNI-NPN配置等。 
子主题： 
## PNI-NPN配置 
## PNI-NPN配置 
背景知识 
PNI-NPN指PLMN网络内集成的NPN功能，NPN使用专用DNN或切片标识。但网络切片无法避免UE接入非授权的小区，因此需要CAG（Closed Access Group，闭合接入组）功能，用于避免UE在非授权小区接入。 
功能说明 
PNI-NPN配置可以配置基于SUPI号段的CAG策略、缺省CAG策略。 
该功能需License项“AMF支持PNI-NPN功能”配置为“打开”时才可以使用。 
子主题： 
### CAG Profile配置 
### CAG Profile配置 
背景知识 
PNI-NPN指PLMN网络内集成的NPN功能，NPN使用专用DNN或切片标识。但网络切片无法避免UE接入非授权的小区，因此需要CAG（Closed Access Group，闭合接入组）功能，用于避免UE在非授权小区接入。 
 
无线广播每个小区支持的CAG列表。 
 
在UDM签约用户可接入的CAG列表。 
 
AMF通知UE可接入的CAG列表。 
 
在专网接入模式下的UE，仅会在AMF通知的允许的CAG列表对应的小区接入。 
 
功能说明 
CAG Profile配置可以配置一组CAG标识和CAG only指示。CAG Profile标识被CAG Profile组配置关联。 
子主题： 
#### 增加CAG Profile配置(ADD CAG PROFILE) 
#### 增加CAG Profile配置(ADD CAG PROFILE) 
功能说明 
该命令用于增加一条CAG（Closed Access Group，闭合接入组） Profile配置。CAG Profile包括一组CAG标识和CAG only指示。配置完成后，CAG Profile标识被CAG Profile组配置关联。 
注意事项 
同一个CAG Profile标识对应的MCC和MNC的取值必须相同，且同一个CAG Profile标识对应的配置记录最多12条。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
cagprofileid|CAG Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG列表。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MCC。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MNC。
cagid|CAG标识|参数可选性: 必选参数类型: 字符串参数范围: 8-8|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的CAG ID。
cagonly|CAG ONLY指示|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置UE是否仅在CAG小区下接入。NOT CAG ONLY：指示该用户可以在CAG小区接入，也可以在普通PLMN小区接入。CAG ONLY：指示该用户只支持在CAG小区接入。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
增加CAG Profile标识为1，移动国家码为460，移动网络码为11，CAG标识为11111111，CAG ONLY指示为仅CAG的记录。
ADD CAG PROFILE:CAGPROFILEID=1,MCC="460",MNC="11",CAGID="11111111",CAGONLY=YES
` 
#### 修改CAG Profile配置(SET CAG PROFILE) 
#### 修改CAG Profile配置(SET CAG PROFILE) 
功能说明 
该命令用于修改一条CAG Profile配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
cagprofileid|CAG Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG列表。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MCC。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MNC。
cagid|CAG标识|参数可选性: 必选参数类型: 字符串参数范围: 8-8|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的CAG ID。
cagonly|CAG ONLY指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置UE是否仅在CAG小区下接入。NOT CAG ONLY：指示该用户可以在CAG小区接入，也可以在普通PLMN小区接入。CAG ONLY：指示该用户只支持在CAG小区接入。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
修改CAG Profile标识为1，移动国家码为460，移动网络码为11，CAG标识为11111111的记录的CAG ONLY指示字段为非仅CAG。
SET CAG PROFILE:CAGPROFILEID=1,MCC="460",MNC="11",CAGID="11111111",CAGONLY=NO
` 
#### 删除CAG Profile配置(DEL CAG PROFILE) 
#### 删除CAG Profile配置(DEL CAG PROFILE) 
功能说明 
该命令用于删除一条CAG Profile配置。 
注意事项 
当CAG Profile标识被CAG Profile组配置所引用时，不能被删除。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
cagprofileid|CAG Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG列表。
mcc|移动国家码|参数可选性: 必选参数类型: 字符串参数范围: 3-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MCC。
mnc|移动网络码|参数可选性: 必选参数类型: 字符串参数范围: 2-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MNC。
cagid|CAG标识|参数可选性: 必选参数类型: 字符串参数范围: 8-8|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的CAG ID。
命令举例 
`
删除CAG Profile标识为1，移动国家码为460,移动网络码为11,CAG标识为11111111的记录。
DEL CAG PROFILE:CAGPROFILEID=1,MCC="460",MNC="11",CAGID="11111111"
` 
#### 查询CAG Profile配置(SHOW CAG PROFILE) 
#### 查询CAG Profile配置(SHOW CAG PROFILE) 
功能说明 
该命令用于查询CAG Profile配置。可单条查询和全部查询。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
cagprofileid|CAG Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG列表。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MCC。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MNC。
cagid|CAG标识|参数可选性: 任选参数类型: 字符串参数范围: 8-8|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的CAG ID。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
cagprofileid|CAG Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG列表。
mcc|移动国家码|参数可选性: 任选参数类型: 字符串参数范围: 3-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MCC。
mnc|移动网络码|参数可选性: 任选参数类型: 字符串参数范围: 2-3|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的MNC。
cagid|CAG标识|参数可选性: 任选参数类型: 字符串参数范围: 8-8|Global CAG ID由MCC+MNC+CAG ID组成，该参数标识Global CAG ID中的CAG ID。
cagonly|CAG ONLY指示|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: YES|该参数用于设置UE是否仅在CAG小区下接入。NOT CAG ONLY：指示该用户可以在CAG小区接入，也可以在普通PLMN小区接入。CAG ONLY：指示该用户只支持在CAG小区接入。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
查询CAG Profile标识为1的记录。
SHOW CAG PROFILE:CAGPROFILEID=1
(No.1) : SHOW CAG PROFILE:CAGPROFILEID=1:
-----------------Namf_Communication_0----------------
 CAG Profile标识 移动国家码 移动网络码 CAG标识  CAG ONLY指示 别名 
 1               460        11         11111111 CAG ONLY  
记录数：1   
执行成功耗时: 0.12 秒
` 
### CAG Profile组配置 
### CAG Profile组配置 
背景知识 
PNI-NPN指PLMN网络内集成的NPN功能，NPN使用专用DNN或切片标识。但网络切片无法避免UE接入非授权的小区，因此需要CAG（Closed Access Group，闭合接入组）功能，用于避免UE在非授权小区接入。 
 
无线广播每个小区支持的CAG列表。 
 
在UDM签约用户可接入的CAG列表。 
 
AMF通知UE可接入的CAG列表。 
 
在专网接入模式下的UE，仅会在AMF通知的允许的CAG列表对应的小区接入。 
 
功能说明 
CAG Profile组配置可以配置一组CAG Profile。不同的CAG Profile归属于不同的PLMN。当需要用到本地配置时需要配置。 
子主题： 
#### 增加CAG Profile组配置(ADD CAG GROUP) 
#### 增加CAG Profile组配置(ADD CAG GROUP) 
功能说明 
该命令用于增加一条CAG（Closed Access Group，闭合接入组） Profile组配置。CAG Profile组配置可以配置一组CAG Profile。不同的CAG Profile归属于不同的PLMN。当需要用到本地配置时需要配置。 
注意事项 
一个CAG Profile组标识最多关联16个CAG Profile标识。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
caggroupid|CAG Profile组标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile组。
cagprofileid|CAG Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile。通过ADD CAG PROFILE命令配置CAG Profile标识。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
增加一条CAG Profile组标识为1，CAG Profile标识为1的记录。
ADD CAG GROUP:CAGGROUPID=1,CAGPROFILEID=1
` 
#### 修改CAG Profile组配置(SET CAG GROUP) 
#### 修改CAG Profile组配置(SET CAG GROUP) 
功能说明 
该命令用于修改一条CAG Profile组配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
caggroupid|CAG Profile组标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile组。
cagprofileid|CAG Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile。通过ADD CAG PROFILE命令配置CAG Profile标识。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
修改CAG Profile组标识为1，CAG Profile标识为1的记录对应的别名为"aaa"。
SET CAG GROUP:CAGGROUPID=1,CAGPROFILEID=1,ALIAS="aaa"
` 
#### 删除CAG Profile组配置(DEL CAG GROUP) 
#### 删除CAG Profile组配置(DEL CAG GROUP) 
功能说明 
该命令用于删除一条CAG Profile组配置。 
注意事项 
当CAG Profile组标识被"
基于SUPI号段CAG策略配置"或" 缺省CAG策略配置"所引用时，不能被删除。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
caggroupid|CAG Profile组标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile组。
cagprofileid|CAG Profile标识|参数可选性: 必选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile。通过ADD CAG PROFILE命令配置CAG Profile标识。
命令举例 
`
删除一条CAG Profile组标识为1，CAG Profile标识为1的记录。
DEL CAG GROUP:CAGGROUPID=1,CAGPROFILEID=1
` 
#### 查询CAG Profile组配置(SHOW CAG GROUP) 
#### 查询CAG Profile组配置(SHOW CAG GROUP) 
功能说明 
该命令用于查询CAG Profile组配置。可单条查询和全部查询。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
caggroupid|CAG Profile组标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile组。
cagprofileid|CAG Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile。通过ADD CAG PROFILE命令配置CAG Profile标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
caggroupid|CAG Profile组标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile组。
cagprofileid|CAG Profile标识|参数可选性: 任选参数类型: 数字参数范围: 1-65535|该参数用于标识唯一的CAG Profile。通过ADD CAG PROFILE命令配置CAG Profile标识。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
查询CAG Profile组标识为1，CAG Profile标识为1的记录。
SHOW CAG GROUP:CAGGROUPID=1,CAGPROFILEID=1
(No.1) : SHOW CAG GROUP:CAGGROUPID=1,CAGPROFILEID=1:
-----------------Namf_Communication_0----------------
CAG Profile组标识        CAG Profile标识      别名     
1                              1                       
Execute Successfully Elapsed Time: : 0.12 s
` 
### 基于SUPI号段CAG策略配置 
### 基于SUPI号段CAG策略配置 
背景知识 
PNI-NPN指PLMN网络内集成的NPN功能，NPN使用专用DNN或切片标识。但网络切片无法避免UE接入非授权的小区，因此需要CAG（Closed Access Group，闭合接入组）功能，用于避免UE在非授权小区接入。 
 
无线广播每个小区支持的CAG列表。 
 
在UDM签约用户可接入的CAG列表。 
 
AMF通知UE可接入的CAG列表。 
 
在专网接入模式下的UE，仅会在AMF通知的允许的CAG列表对应的小区接入。 
 
功能说明 
基于SUPI号段CAG策略配置可以按SUPI号段设置CAG策略。在“缺省CAG策略配置”中设置支持基于SUPI号段的CAG策略。 
子主题： 
#### 增加基于SUPI号段的CAG策略配置(ADD SUPI CAG POLICY) 
#### 增加基于SUPI号段的CAG策略配置(ADD SUPI CAG POLICY) 
功能说明 
该命令用于增加一条基于SUPI号段CAG策略配置。当“缺省CAG策略配置”启用基于SUPI号段的CAG策略功能时，该配置才生效。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数为需要控制接入的用户SUPI号段。
cagpolicy|CAG策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: SUB|该参数用于配置AMF确定UE的Allowed CAG List的策略。签约：取签约配置得到的CAG相关信息。本地：取本地配置得到的CAG相关信息。签约与本地交集：取签约和本地配置得到的CAG相关信息的交集 。签约与本地并集：取签约和本地配置得到的CAG相关信息的并集 。
caggroupid|CAG Profile组标识|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于标识一个CAG Profile组。通过ADD CAG GROUP命令配置CAG Profile组标识。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
增加一条SUPI号段为"460"，CAG策略为签约，CAG Profile组标识为1的配置记录。
ADD SUPI CAG POLICY:SUPISEGMENT="460",CAGPOLICY="SUB",CAGGROUPID=1
` 
#### 修改基于SUPI号段的CAG策略配置(SET SUPI CAG POLICY) 
#### 修改基于SUPI号段的CAG策略配置(SET SUPI CAG POLICY) 
功能说明 
该命令用于修改一条基于SUPI号段CAG策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数为需要控制接入的用户SUPI号段。
cagpolicy|CAG策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: SUB|该参数用于配置AMF确定UE的Allowed CAG List的策略。签约：取签约配置得到的CAG相关信息。本地：取本地配置得到的CAG相关信息。签约与本地交集：取签约和本地配置得到的CAG相关信息的交集 。签约与本地并集：取签约和本地配置得到的CAG相关信息的并集 。
caggroupid|CAG Profile组标识|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于标识一个CAG Profile组。通过ADD CAG GROUP命令配置CAG Profile组标识。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
修改SUPI号段为"460"的配置记录对应的CAG策略为签约。
SET SUPI CAG POLICY:SUPISEGMENT="460",CAGPOLICY="SUB"
` 
#### 删除基于SUPI号段的CAG策略配置(DEL SUPI CAG POLICY) 
#### 删除基于SUPI号段的CAG策略配置(DEL SUPI CAG POLICY) 
功能说明 
该命令用于删除一条基于SUPI号段CAG策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数为需要控制接入的用户SUPI号段。
命令举例 
`
删除SUPI号段为"460"的配置记录。
DEL SUPI CAG POLICY:SUPISEGMENT="460"
` 
#### 查询基于SUPI号段的CAG策略配置(SHOW SUPI CAG POLICY) 
#### 查询基于SUPI号段的CAG策略配置(SHOW SUPI CAG POLICY) 
功能说明 
该命令用于查询基于SUPI号段CAG策略配置。可单条查询和全部查询。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数为需要控制接入的用户SUPI号段。
cagpolicy|CAG策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: SUB|该参数用于配置AMF确定UE的Allowed CAG List的策略。签约：取签约配置得到的CAG相关信息。本地：取本地配置得到的CAG相关信息。签约与本地交集：取签约和本地配置得到的CAG相关信息的交集 。签约与本地并集：取签约和本地配置得到的CAG相关信息的并集 。
caggroupid|CAG Profile组标识|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于标识一个CAG Profile组。通过ADD CAG GROUP命令配置CAG Profile组标识。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiSegment|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数为需要控制接入的用户SUPI号段。
cagpolicy|CAG策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: SUB|该参数用于配置AMF确定UE的Allowed CAG List的策略。签约：取签约配置得到的CAG相关信息。本地：取本地配置得到的CAG相关信息。签约与本地交集：取签约和本地配置得到的CAG相关信息的交集 。签约与本地并集：取签约和本地配置得到的CAG相关信息的并集 。
caggroupid|CAG Profile组标识|参数可选性: 任选参数类型: 数字参数范围: 0-65535|该参数用于标识一个CAG Profile组。通过ADD CAG GROUP命令配置CAG Profile组标识。
alias|别名|参数可选性: 任选参数类型: 字符串参数范围: 0-30|该参数用于填写对配置记录的详细说明。
命令举例 
`
查询SUPI号段为"460"的配置记录。
SHOW SUPI CAG POLICY:SUPISEGMENT="460"
(No.1) : SHOW SUPI CAG POLICY:SUPISEGMENT="460":
-----------------Namf_Communication_0----------------
SUPI号段        CAG策略     CAG Profile组标识     别名
460               SUB           1                  
记录数：1   
执行成功耗时: 0.12 秒
` 
### 缺省CAG策略配置 
### 缺省CAG策略配置 
背景知识 
PNI-NPN指PLMN网络内集成的NPN功能，NPN使用专用DNN或切片标识。但网络切片无法避免UE接入非授权的小区，因此需要CAG（Closed Access Group，闭合接入组）功能，用于避免UE在非授权小区接入。 
 
无线广播每个小区支持的CAG列表。 
 
在UDM签约用户可接入的CAG列表。 
 
AMF通知UE可接入的CAG列表。 
 
在专网接入模式下的UE，仅会在AMF通知的允许的CAG列表对应的小区接入。 
 
功能说明 
缺省CAG策略配置用于配置是否支持CAG功能，是否支持基于SUPI号段的CAG策略，以及CAG策略。 
子主题： 
#### 修改缺省CAG策略配置(SET DEFAULT CAG POLICY) 
#### 修改缺省CAG策略配置(SET DEFAULT CAG POLICY) 
功能说明 
该命令用于修改缺省CAG（Closed Access Group，闭合接入组）策略配置。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
ifsprtpninpn|是否支持PNI-NPN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSPRTPNINPN|该参数用于设置AMF是否支持PNI-NPN（Public Network Integrated NPN公共网络集成的NPN网络，即非独立专网）功能。PNI-NPN指PLMN网络内集成的NPN功能，NPN使用专用DNN或切片标识。当需要实现非专网下的专网接入功能，需要开启此功能。
ifsprtsupicag|是否支持基于SUPI号段的CAG策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSPRTSUPICAG|该参数用于设置AMF是否支持基于用户的SUPI号段设置CAG策略的功能。否：该参数配置为否，则通过ADD SUPI CAG POLICY命令配置的基于SUPI号段CAG策略不会生效。是：该参数配置为是，则AMF会优先去匹配通过ADD SUPI CAG POLICY命令配置的基于SUPI号段CAG策略，AMF如果匹配到了相关的配置策略，则按匹配的配置策略执行后续操作，如果匹配不到，按照本命令配置的参数“CAG策略”获取的策略执行。
cagpolicy|CAG策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: SUB|该参数用于配置AMF确定UE的Allowed CAG List的策略。签约：取签约配置得到的CAG相关信息。本地：取本地配置得到的CAG相关信息。签约与本地交集：取签约和本地配置得到的CAG相关信息的交集 。签约与本地并集：取签约和本地配置得到的CAG相关信息的并集 。
caggroupid|CAG Profile组标识|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于配置一个CAG Profile组。修改影响：无数据来源：本端规划。默认值：无配置原则：本参数的取值是引用于ADD CAG GROUP命令配置的参数“CAG Profile组标识”，必须预先通过ADD CAG GROUP命令配置。
nosprtcagrejcause|UE不支持CAG并且被CAG限制接入时的拒绝原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: NOSUITABLECELLSINTA|该参数用于配置UE在CAG（Closed Access Group，闭合接入组）小区接入，AMF在触发AUSF对UE进行鉴权的同时，把Cell CAG List信息给AUSF后，由于AUSF判断该UE在此CAG限制接入，导致AMF拒绝其接入时，AUSF给AMF返回鉴权失败消息时，携带的拒绝原因值。
ifcellcagtoausf|鉴权过程中是否携带Cell CAG List给AUSF|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|该参数用于配置AMF在触发AUSF对UE进行鉴权时，是否把Cell CAG List信息带给AUSF。
ifcagcelluecause|CAG小区接入用户被UDM拒绝时是否指定原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|参数作用：该参数用于配置UE在CAG（Closed Access Group，闭合接入组）小区接入，AMF在触发AUSF对UE进行鉴权的同时，把Cell CAG List信息给AUSF后，AUSF如果给AMF返回鉴权失败消息时，是否需要在返回的鉴权失败消息中，携带指定的失败原因值。本参数仅在“鉴权过程中是否携带Cell CAG List给AUSF”命令设置为“是”时才有效。修改影响：会景程 AUSF给AMF返回的鉴权失败消息中是否携带原因值。数据来源：本端规划。默认值：无。配置原则：该参数包括如下取值。否：表示AUSF给AMF返回的鉴权失败消息中，不需指定原因值。是：表示AUSF给AMF返回的鉴权失败消息中的原因值使用本命令配置的参数“CAG小区接入用户被UDM拒绝时原因值”中的值。
cagcelluerejcause|CAG小区接入用户被UDM拒绝时原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NOSUITABLECELLSINTA|该参数用于配置UE在CAG（Closed Access Group，闭合接入组）小区接入，AMF在触发AUSF对UE进行鉴权的同时，把Cell CAG List信息给AUSF后，AUSF如果给AMF返回鉴权失败消息时，携带的指定的失败原因值。该参数在“鉴权过程中是否携带Cell CAG List给AUSF”为“是”且“CAG小区接入用户被UDM拒绝时是否指定原因值”为“是”时才有效。
ifcagtoueausfrej|CAG小区接入用户被UDM拒绝时是否携带CAG信息给UE|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|该参数用于配置UE在CAG（Closed Access Group，闭合接入组）小区接入，AMF在触发AUSF对UE进行鉴权的同时，把Cell CAG List信息给AUSF后，AUSF如果给AMF返回鉴权失败消息时，AMF是否需把AMF本地配置的UE支持的CAG List信息给UE。该参数在“鉴权过程中是否携带Cell CAG List给AUSF”为“是”时才有效。AMF本地配置的UE支持的CAG List信息为本命令配置的“CAG Profile组标识”对应的CAG List。
ifrlsn2amfreallcmp|AMF重定向的注册过程完成后是否立刻释放N2连接|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|该参数用于配置Target AMF在完成AMF间的AMF重定向的注册过程后，因为Target AMF没有Cell CAG List信息，因此通过该参数标识在UE注册完成后，AMF是否立刻释放N2连接。否：表示不需立刻释放N2连接。是：表示需立刻释放N2连接。
ifdetachuesubchange|新的签约CAG信息和小区下CAG信息无交集时是否去注册用户|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|该参数用于配置用户签约的CAG List发生改变，导致新的Allowed CAG List和Cell CAG List无交集时，是否需去注册用户。否：表示不需去注册用户。是：表示需去注册用户。
命令举例 
`
设置AMF支持PNI-NPN功能。
SET DEFAULT CAG POLICY:IFSPRTPNINPN="SPRTPNINPN"
` 
#### 查询缺省CAG策略配置(SHOW DEFAULT CAG POLICY) 
#### 查询缺省CAG策略配置(SHOW DEFAULT CAG POLICY) 
功能说明 
该命令用于查询缺省CAG策略配置。可单条查询和全部查询。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
ifsprtpninpn|是否支持PNI-NPN|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSPRTPNINPN|该参数用于设置AMF是否支持PNI-NPN（Public Network Integrated NPN公共网络集成的NPN网络，即非独立专网）功能。PNI-NPN指PLMN网络内集成的NPN功能，NPN使用专用DNN或切片标识。当需要实现非专网下的专网接入功能，需要开启此功能。
ifsprtsupicag|是否支持基于SUPI号段的CAG策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSPRTSUPICAG|该参数用于设置AMF是否支持基于用户的SUPI号段设置CAG策略的功能。否：该参数配置为否，则通过ADD SUPI CAG POLICY命令配置的基于SUPI号段CAG策略不会生效。是：该参数配置为是，则AMF会优先去匹配通过ADD SUPI CAG POLICY命令配置的基于SUPI号段CAG策略，AMF如果匹配到了相关的配置策略，则按匹配的配置策略执行后续操作，如果匹配不到，按照本命令配置的参数“CAG策略”获取的策略执行。
cagpolicy|CAG策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: SUB|该参数用于配置AMF确定UE的Allowed CAG List的策略。签约：取签约配置得到的CAG相关信息。本地：取本地配置得到的CAG相关信息。签约与本地交集：取签约和本地配置得到的CAG相关信息的交集 。签约与本地并集：取签约和本地配置得到的CAG相关信息的并集 。
caggroupid|CAG Profile组标识|参数可选性: 任选参数类型: 数字参数范围: 0-65535默认值: 0|参数作用：该参数用于配置一个CAG Profile组。修改影响：无数据来源：本端规划。默认值：无配置原则：本参数的取值是引用于ADD CAG GROUP命令配置的参数“CAG Profile组标识”，必须预先通过ADD CAG GROUP命令配置。
nosprtcagrejcause|UE不支持CAG并且被CAG限制接入时的拒绝原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-255默认值: NOSUITABLECELLSINTA|该参数用于配置UE在CAG（Closed Access Group，闭合接入组）小区接入，AMF在触发AUSF对UE进行鉴权的同时，把Cell CAG List信息给AUSF后，由于AUSF判断该UE在此CAG限制接入，导致AMF拒绝其接入时，AUSF给AMF返回鉴权失败消息时，携带的拒绝原因值。
ifcellcagtoausf|鉴权过程中是否携带Cell CAG List给AUSF|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|该参数用于配置AMF在触发AUSF对UE进行鉴权时，是否把Cell CAG List信息带给AUSF。
ifcagcelluecause|CAG小区接入用户被UDM拒绝时是否指定原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|参数作用：该参数用于配置UE在CAG（Closed Access Group，闭合接入组）小区接入，AMF在触发AUSF对UE进行鉴权的同时，把Cell CAG List信息给AUSF后，AUSF如果给AMF返回鉴权失败消息时，是否需要在返回的鉴权失败消息中，携带指定的失败原因值。本参数仅在“鉴权过程中是否携带Cell CAG List给AUSF”命令设置为“是”时才有效。修改影响：会景程 AUSF给AMF返回的鉴权失败消息中是否携带原因值。数据来源：本端规划。默认值：无。配置原则：该参数包括如下取值。否：表示AUSF给AMF返回的鉴权失败消息中，不需指定原因值。是：表示AUSF给AMF返回的鉴权失败消息中的原因值使用本命令配置的参数“CAG小区接入用户被UDM拒绝时原因值”中的值。
cagcelluerejcause|CAG小区接入用户被UDM拒绝时原因值|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NOSUITABLECELLSINTA|该参数用于配置UE在CAG（Closed Access Group，闭合接入组）小区接入，AMF在触发AUSF对UE进行鉴权的同时，把Cell CAG List信息给AUSF后，AUSF如果给AMF返回鉴权失败消息时，携带的指定的失败原因值。该参数在“鉴权过程中是否携带Cell CAG List给AUSF”为“是”且“CAG小区接入用户被UDM拒绝时是否指定原因值”为“是”时才有效。
ifcagtoueausfrej|CAG小区接入用户被UDM拒绝时是否携带CAG信息给UE|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|该参数用于配置UE在CAG（Closed Access Group，闭合接入组）小区接入，AMF在触发AUSF对UE进行鉴权的同时，把Cell CAG List信息给AUSF后，AUSF如果给AMF返回鉴权失败消息时，AMF是否需把AMF本地配置的UE支持的CAG List信息给UE。该参数在“鉴权过程中是否携带Cell CAG List给AUSF”为“是”时才有效。AMF本地配置的UE支持的CAG List信息为本命令配置的“CAG Profile组标识”对应的CAG List。
ifrlsn2amfreallcmp|AMF重定向的注册过程完成后是否立刻释放N2连接|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|该参数用于配置Target AMF在完成AMF间的AMF重定向的注册过程后，因为Target AMF没有Cell CAG List信息，因此通过该参数标识在UE注册完成后，AMF是否立刻释放N2连接。否：表示不需立刻释放N2连接。是：表示需立刻释放N2连接。
ifdetachuesubchange|新的签约CAG信息和小区下CAG信息无交集时是否去注册用户|参数可选性: 任选参数类型: 枚举，参见枚举定义默认值: NO|该参数用于配置用户签约的CAG List发生改变，导致新的Allowed CAG List和Cell CAG List无交集时，是否需去注册用户。否：表示不需去注册用户。是：表示需去注册用户。
命令举例 
`
查询缺省CAG策略配置。
SHOW DEFAULT CAG POLICY
(No.1) :SHOW DEFAULT CAG POLICY:
-----------------Namf_Communication_0----------------
是否支持PNI-NPN 是否支持基于SUPI号段的CAG策略 CAG策略 CAG Profile组标识  UE不支持CAG并且被CAG限制接入时的拒绝原因值
否              否                            签约          0           15 - No suitable cells in tracking area       
记录数：1   
执行成功耗时: 0.12 秒
` 
# QoS控制策略配置 
# QoS控制策略配置 
背景知识 
欧洲运营商的用户，一般签约的QoS比国内用户高，当这些用户漫游到国内后，国内运营商要避免国际漫游用户占用过多的网络资源，需要AMF进行本地QoS控制。5GC网络AMF管理的QoS参数包括:
UE-AMBR(User Equipment-Aggregate Maximum Bit Rate，用户设备-累计最大比特率):用来限制每个UE所有非GBR QoS Flow的汇聚最大速率的QoS参数。AMF将签约的UE-AMBR传递给RAN，RAN根据Session-AMBR和签约的UE-AMBR计算出UE-AMBR。 
功能说明 
"QoS控制策略配置"可以方便运营商灵活地根据SUPI号段设置本地策略，控制下发给RAN的UE-AMBR，包括:
(1) 缺省QoS控制策略配置，
(2) 基于SUPI的QoS控制策略配置。  
子主题： 
## 缺省QoS控制策略配置 
## 缺省QoS控制策略配置 
背景知识 
欧洲运营商的用户，一般签约的QoS比国内用户高，当这些用户漫游到国内后，国内运营商要避免国际漫游用户占用过多的网络资源，需要AMF进行本地QoS控制。5GC网络AMF管理的QoS参数即UE-AMBR，AMF需要对UE-AMBR进行控制。 
功能说明 
缺省QoS策略配置”用于设置AMF全局的缺省QoS控制策略,包括: 
 
是否支持用户QoS控制。 
 
QoS控制策略。 
 
上行UE累计最大比特率和下行UE累计最大比特率。 
 
QoS控制策略，包括如下几种。 
 
签约：使用签约的UE-AMBR。 
 
本地配置：使用本地配置的UE-AMBR。 
 
签约与本地配置取小：如果本地UE-AMBR和签约UE-AMBR均有效，则比较本地UE-AMBR和签约UE-AMBR，使用较小的值；否则，不执行本地QoS控制，使用签约的UE-AMBR。 
 
子主题： 
### 设置缺省QoS控制策略配置(SET DEFAULT QOS CONTROL POLICY) 
### 设置缺省QoS控制策略配置(SET DEFAULT QOS CONTROL POLICY) 
功能说明 
该命令用于设置缺省QoS控制策略配置。当需要AMF进行QoS控制时，使用该命令。 
注意事项 
无。
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supqosctrl|支持用户QoS控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPQOSCTRL|本参数用于设置支持用户QoS控制。
policy|控制策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: UEAMBRSUB|该参数用于设置用户QoS控制的默认获取策略，包括"签约"、"本地配置"、"签约与本地配置取小"三个取值。 默认用户QoS控制获取策略的详细说明如下：签约(SUB)： 使用签约的UE-AMBR。本地配置(LOCAL): 使用本地配置的UE-AMBR。签约与本地配置取小(SMALLER)： 如果本地UE-AMBR和签约UE-AMBR均有效，则比较本地UE-AMBR和签约UE-AMBR，使用较小的值；否则，不执行本地QoS控制，使用签约的UE-AMBR。
ueambrdl|下行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 2000000000000|本参数用于设置下行消息的AMBR，取值范围:0 - 4000000000000。
ueambrul|上行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 2000000000000|本参数用于设置上行消息的AMBR，取值范围:0 - 4000000000000。
unit|比特率单位|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AMBRBPS|本参数用于设置比特率单位。
命令举例 
`
设置缺省QoS控制策略配置为"支持用户QoS控制"，策略为"本地配置"，设置下行UEAMBR值为456000，上行UEAMBR值为12300，比特率单位为"KBPS"。
SET DEFAULT QOS CONTROL POLICY:SUPQOSCTRL="SUPQOSCTRL",POLICY="UEAMBRLOCAL",UEAMBRDL="456000",UEAMBRUL="12300",UNIT="AMBRKBPS"
` 
### 查询缺省QoS控制策略配置(SHOW DEFAULT QOS CONTROL POLICY) 
### 查询缺省QoS控制策略配置(SHOW DEFAULT QOS CONTROL POLICY) 
功能说明 
该命令用于查询缺省QoS控制策略配置。 
注意事项 
无。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supqosctrl|支持用户QoS控制|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-1默认值: NOTSUPQOSCTRL|本参数用于设置支持用户QoS控制。
policy|控制策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: UEAMBRSUB|该参数用于设置用户QoS控制的默认获取策略，包括"签约"、"本地配置"、"签约与本地配置取小"三个取值。 默认用户QoS控制获取策略的详细说明如下：签约(SUB)： 使用签约的UE-AMBR。本地配置(LOCAL): 使用本地配置的UE-AMBR。签约与本地配置取小(SMALLER)： 如果本地UE-AMBR和签约UE-AMBR均有效，则比较本地UE-AMBR和签约UE-AMBR，使用较小的值；否则，不执行本地QoS控制，使用签约的UE-AMBR。
ueambrdl|下行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 2000000000000|本参数用于设置下行消息的AMBR，取值范围:0 - 4000000000000。
ueambrul|上行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 2000000000000|本参数用于设置上行消息的AMBR，取值范围:0 - 4000000000000。
unit|比特率单位|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AMBRBPS|本参数用于设置比特率单位。
命令举例 
`
查询缺省QoS控制策略配置。
SHOW DEFAULT QOS CONTROL POLICY:
(No.3) : SHOW DEFAULT QOS CONTROL POLICY:
-----------------Namf_Communication_0----------------
操作维护       支持用户QoS控制 控制策略 下行消息的UEAMBR 上行消息的UEAMBR 比特率单位 
-------------------------------------------------------------------------------------
修改           支持用户QoS控制 本地配置 456000           12300               Kbps 
-------------------------------------------------------------------------------------
记录数：1
执行成功开始时间:2021-01-29 10:01:30 耗时: 0.136 秒
` 
## 基于SUPI的QoS控制策略配置 
## 基于SUPI的QoS控制策略配置 
背景知识 
欧洲运营商的用户，一般签约的QoS比国内用户高，当这些用户漫游到国内后，国内运营商要避免国际漫游用户占用过多的网络资源，需要AMF进行本地QoS控制。5GC网络AMF管理的QoS参数即UE-AMBR，AMF需要对UE-AMBR进行控制。 
功能说明 
基于SUPI的QoS控制策略配置”可以基于SUPI号段配置QoS控制策略。QoS控制策略，包括如下几种: 
 
签约：使用签约的UE-AMBR。 
 
本地配置：使用本地配置的UE-AMBR。 
 
签约与本地配置取小：如果本地UE-AMBR和签约UE-AMBR均有效，则比较本地UE-AMBR和签约UE-AMBR，使用较小的值；否则，不执行本地QoS控制，使用签约的UE-AMBR。 
 
子主题： 
### 增加基于SUPI的QoS控制策略配置(ADD CONFIG QOS CONTROL POLICY SUPI) 
### 增加基于SUPI的QoS控制策略配置(ADD CONFIG QOS CONTROL POLICY SUPI) 
功能说明 
该命令用于增加基于SUPI的QoS控制策略配置。当需要针对SUPI号段配置QoS控制策略时，使用该命令。 
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于将一个SUPI号段加入AMF的基于SUPI的QoS控制策略配置中。该参数的取值是通过ADD CONFIG QOS CONTROL POLICY SUPI命令配置的。
policy|控制策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: UEAMBRSUB|该参数用于设置用户QoS控制的默认获取策略，包括"签约"、"本地配置"、"签约与本地配置取小"三个取值。 默认用户QoS控制获取策略的详细说明如下：签约(SUB)： 使用签约的UE-AMBR。本地配置(LOCAL): 使用本地配置的UE-AMBR。签约与本地配置取小(SMALLER)： 如果本地UE-AMBR和签约UE-AMBR均有效，则比较本地UE-AMBR和签约UE-AMBR，使用较小的值；否则，不执行本地QoS控制，使用签约的UE-AMBR。
ueambrdl|下行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 0|本参数用于设置下行消息的AMBR，取值范围:0 - 4000000000000。
ueambrul|上行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 0|本参数用于设置上行消息的AMBR，取值范围:0 - 4000000000000。
unit|比特率单位|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AMBRBPS|本参数用于设置比特率单位。
命令举例 
`
将SUPI号段"4601100"加入AMF的基于SUPI的QoS控制策略配置中，策略为"签约与本地配置取小"，设置下行UEAMBR值为500，上行UEAMBR值为600，比特率单位为"MBPS"。
ADD CONFIG QOS CONTROL POLICY SUPI:SUPISEG="4601100",POLICY="UEAMBRSMALLER",UEAMBRDL="500",UEAMBRUL="600",UNIT="AMBRMBPS"
` 
### 修改基于SUPI的QoS控制策略配置(SET CONFIG QOS CONTROL POLICY SUPI) 
### 修改基于SUPI的QoS控制策略配置(SET CONFIG QOS CONTROL POLICY SUPI) 
功能说明 
该命令用于修改基于SUPI的QoS控制策略配置。 
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于将一个SUPI号段加入AMF的基于SUPI的QoS控制策略配置中。该参数的取值是通过ADD CONFIG QOS CONTROL POLICY SUPI命令配置的。
policy|控制策略|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: UEAMBRSUB|该参数用于设置用户QoS控制的默认获取策略，包括"签约"、"本地配置"、"签约与本地配置取小"三个取值。 默认用户QoS控制获取策略的详细说明如下：签约(SUB)： 使用签约的UE-AMBR。本地配置(LOCAL): 使用本地配置的UE-AMBR。签约与本地配置取小(SMALLER)： 如果本地UE-AMBR和签约UE-AMBR均有效，则比较本地UE-AMBR和签约UE-AMBR，使用较小的值；否则，不执行本地QoS控制，使用签约的UE-AMBR。
ueambrdl|下行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 0|本参数用于设置下行消息的AMBR，取值范围:0 - 4000000000000。
ueambrul|上行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 0|本参数用于设置上行消息的AMBR，取值范围:0 - 4000000000000。
unit|比特率单位|参数可选性: 必选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AMBRBPS|本参数用于设置比特率单位。
命令举例 
`
将已经成功配置的SUPI号段"4601100"的基于SUPI的QoS控制策略配置修改为策略为"本地配置"，下行和上行UEAMBR值不变，比特率单位由"MBPS"修改为"KBPS"。
SET CONFIG QOS CONTROL POLICY SUPI:SUPISEG="4601100",POLICY="UEAMBRLOCAL",UNIT="AMBRKBPS"
` 
### 删除基于SUPI的QoS控制策略配置(DEL CONFIG QOS CONTROL POLICY SUPI) 
### 删除基于SUPI的QoS控制策略配置(DEL CONFIG QOS CONTROL POLICY SUPI) 
功能说明 
该命令用于删除基于SUPI的QoS控制策略配置。 
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 必选参数类型: 字符串参数范围: 1-15|该参数用于将一个SUPI号段加入AMF的基于SUPI的QoS控制策略配置中。该参数的取值是通过ADD CONFIG QOS CONTROL POLICY SUPI命令配置的。
命令举例 
`
将已经成功配置的SUPI号段"4601100"从基于SUPI的QoS控制策略配置中移除。
DEL CONFIG QOS CONTROL POLICY SUPI:SUPISEG="4601100"
` 
### 查询基于SUPI的QoS控制策略配置(SHOW CONFIG QOS CONTROL POLICY SUPI) 
### 查询基于SUPI的QoS控制策略配置(SHOW CONFIG QOS CONTROL POLICY SUPI) 
功能说明 
该命令用于查询基于SUPI的QoS控制策略配置。 
注意事项 
无
输入参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于将一个SUPI号段加入AMF的基于SUPI的QoS控制策略配置中。该参数的取值是通过ADD CONFIG QOS CONTROL POLICY SUPI命令配置的。
输出参数说明 
标识|名称|类型|说明
---|---|---|---
supiseg|SUPI号段|参数可选性: 任选参数类型: 字符串参数范围: 1-15|该参数用于将一个SUPI号段加入AMF的基于SUPI的QoS控制策略配置中。该参数的取值是通过ADD CONFIG QOS CONTROL POLICY SUPI命令配置的。
policy|控制策略|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-2默认值: UEAMBRSUB|该参数用于设置用户QoS控制的默认获取策略，包括"签约"、"本地配置"、"签约与本地配置取小"三个取值。 默认用户QoS控制获取策略的详细说明如下：签约(SUB)： 使用签约的UE-AMBR。本地配置(LOCAL): 使用本地配置的UE-AMBR。签约与本地配置取小(SMALLER)： 如果本地UE-AMBR和签约UE-AMBR均有效，则比较本地UE-AMBR和签约UE-AMBR，使用较小的值；否则，不执行本地QoS控制，使用签约的UE-AMBR。
ueambrdl|下行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 0|本参数用于设置下行消息的AMBR，取值范围:0 - 4000000000000。
ueambrul|上行消息的UEAMBR|参数可选性: 任选参数类型: 字符串参数范围: 1-13默认值: 0|本参数用于设置上行消息的AMBR，取值范围:0 - 4000000000000。
unit|比特率单位|参数可选性: 任选参数类型: 枚举，参见枚举定义参数范围: 0-3默认值: AMBRBPS|本参数用于设置比特率单位。
命令举例 
`
查询当前所有基于SUPI的QoS控制策略配置。
 SHOW CONFIG QOS CONTROL POLICY SUPI:
(No.8) : SHOW CONFIG QOS CONTROL POLICY SUPI:
-----------------Namf_Communication_0----------------
操作维护       SUPI号段  控制策略           下行消息的UEAMBR 上行消息的UEAMBR 比特率单位 
-----------------------------------------------------------------------------------------
复制 修改 删除 460001111 签约               0                0                bps   
复制 修改 删除 4601100   签约与本地配置取小 500              600              Mbps 
-----------------------------------------------------------------------------------------
记录数：2
执行成功开始时间:2021-01-29 10:07:28 耗时: 0.141 秒
` 
