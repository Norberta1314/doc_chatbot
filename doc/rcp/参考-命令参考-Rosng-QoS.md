# CAR配置命令 
## interface 


interface (CAR配置模式) 




### 命令功能 


进入QoS接口配置模式。 






### 命令模式 


 CAR配置模式  






### 命令默认权限级别 


15 






### 命令格式 




interface 
  ＜interface-name 
＞







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


进入QoS接口配置模式：ZXROSNG(config)#qosZXROSNG(config-qos)#interface gei-0/9/0/11ZXROSNG(config-qos-if-gei-0/9/0/11)#进入QoS接口配置模式：ZXROSNG(config)#qosZXROSNG(config-qos)#interface gei-0/9/0/11ZXROSNG(config-qos-if-gei-0/9/0/11)#





### 相关命令 


qos 




## qos 


qos 




### 命令功能 


进入QoS配置模式。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 




qos 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


无 






### 范例 


从配置模式进入QoS配置模式：ZXROSNG(config)#qosZXROSNG(config-qos)#





### 相关命令 


无 




## rate-limit 


rate-limit 




### 命令功能 


在接口上配置流限速策略。 






### 命令模式 


 CAR接口配置模式  






### 命令默认权限级别 


15 






### 命令格式 



rate-limit 
  {input 
|output 
} [mode 
 {blind 
|aware 
}] {ipv4 
 {dscp 
 ＜dscp-value 
＞|precedence 
 ＜precedence-value 
＞}|ipv6 
 {dscp 
 ＜dscp-value 
＞|precedence 
 ＜precedence-value 
＞}|{unicast 
|broadcast 
|unknown 
|ipv4-access-list 
 ＜ipv4-access-list-name 
＞|ipv6-access-list 
 ＜ipv6-access-list-name 
＞|dscp 
 ＜dscp-value 
＞|mpls-exp 
 ＜mpls-exp-value 
＞|precedence 
 ＜precedence-value 
＞|localport 
|inner-vlan 
 ＜vlan-range 
＞ [outer-vlan 
 ＜vlan-range 
＞]|outer-vlan 
 ＜vlan-range 
＞|inner-8021p 
 ＜in-8021p-value 
＞ [outer-8021p 
 ＜out-8021p-value 
＞]|outer-8021p 
 ＜out-8021p-value 
＞|multicast 
|qos-group 
 ＜qosid-number 
＞|unknown-unicast 
|unknown-multicast 
}} cir 
 ＜cir-value 
＞ [{kbps 
|mbps 
|gbps 
}] cbs 
 ＜cbs-value 
＞ pir 
 ＜pir-value 
＞ [{kbps 
|mbps 
|gbps 
}] pbs 
 ＜pbs-value 
＞ conform-action 
 {set-prec-transmit 
 ＜precedence-value 
＞|set-dscp-transmit 
 ＜dscp-value 
＞|set-exp-transmit 
 [{imposition 
|topmost 
}] ＜mpls-exp-value 
＞|drop 
|transmit 
|set-8021p-transmit 
 [inner-outer 
] ＜8021p-value 
＞} exceed-action 
 {set-prec-transmit 
 ＜precedence-value 
＞|set-dscp-transmit 
 ＜dscp-value 
＞|set-exp-transmit 
 [{imposition 
|topmost 
}] ＜mpls-exp-value 
＞|drop 
|transmit 
|set-8021p-transmit 
 [inner-outer 
] ＜8021p-value 
＞} violate-action 
 {set-prec-transmit 
 ＜precedence-value 
＞|set-dscp-transmit 
 ＜dscp-value 
＞|set-exp-transmit 
 [{imposition 
|topmost 
}] ＜mpls-exp-value 
＞|drop 
|transmit 
|set-8021p-transmit 
 [inner-outer 
] ＜8021p-value 
＞} [statistical-share 
]
no rate-limit 
  {input 
|output 
} {ipv4 
 {dscp 
 ＜dscp-value 
＞|precedence 
 ＜precedence-value 
＞}|ipv6 
 {dscp 
 ＜dscp-value 
＞|precedence 
 ＜precedence-value 
＞}|{unicast 
|broadcast 
|unknown 
|ipv4-access-list 
 ＜ipv4-access-list-name 
＞|ipv6-access-list 
 ＜ipv6-access-list-name 
＞|dscp 
 ＜dscp-value 
＞|mpls-exp 
 ＜mpls-exp-value 
＞|precedence 
 ＜precedence-value 
＞|localport 
|inner-vlan 
 ＜vlan-range 
＞ [outer-vlan 
 ＜vlan-range 
＞]|outer-vlan 
 ＜vlan-range 
＞|inner-8021p 
 ＜in-8021p-value 
＞ [outer-8021p 
 ＜out-8021p-value 
＞]|outer-8021p 
 ＜out-8021p-value 
＞|multicast 
|qos-group 
 ＜qosid-number 
＞|unknown-unicast 
|unknown-multicast 
}}
				






### 命令参数解释 




参数|描述
---|---
input|输入
output|输出
mode|模式标识
blind|色盲模式
aware|色敏感模式
ipv4|匹配协议类型：IPv4
dscp|DSCP匹配项
＜dscp-value＞|DSCP值，取值范围<0-63>
precedence|匹配IP优先级
＜precedence-value＞|IP优先级值，取值范围<0-7>
ipv6|匹配协议类型：IPv6
dscp|DSCP匹配项
＜dscp-value＞|DSCP值，取值范围<0-63>
precedence|匹配IP优先级
＜precedence-value＞|IP优先级值，取值范围<0-7>
unicast|L2VPN单播流
broadcast|L2VPN广播流
unknown|L2VPN未知流
ipv4-access-list|匹配IPv4 ACL
＜ipv4-access-list-name＞|IPv4 ACL，参数范围<1-31>个字符
ipv6-access-list|匹配IPv6 ACL
＜ipv6-access-list-name＞|IPv6 ACL，参数范围<1-31>个字符
dscp|DSCP匹配项
＜dscp-value＞|DSCP值，取值范围<0-63>
mpls-exp|MPLS-EXP匹配项
＜mpls-exp-value＞|MPLS-EXP值，取值范围<0-7>
precedence|匹配IP优先级
＜precedence-value＞|IP优先级值，取值范围<0-7>
localport|本地端口
inner-vlan|inner-vlan匹配项
＜vlan-range＞|inner-vlan值，参数范围<1-4094>
outer-vlan|outer-vlan匹配项
＜vlan-range＞|inner-vlan值，参数范围<1-4094>
outer-vlan|outer-vlan匹配项
＜vlan-range＞|inner-vlan值，参数范围<1-4094>
inner-8021p|inner-802.1p匹配项
＜in-8021p-value＞|inner-802.1p值，参数范围<0-7>
outer-8021p|outer-802.1p匹配项
＜out-8021p-value＞|outer-802.1p值，参数范围<0-7>
outer-8021p|outer-802.1p匹配项
＜out-8021p-value＞|outer-802.1p值，参数范围<0-7>
multicast|组播匹配项
qos-group|qos-group匹配项
＜qosid-number＞|qos-group值，参数范围<1-16000>
unknown-unicast|未知单播报文
unknown-multicast|未知组播报文
＜cir-value＞|CIR值，取值范围<$#33816582#$~$#33816583#$>，默认单位：Kbps
kbps|以KBPS为单位
mbps|以MBPS为单位
gbps|以GBPS为单位
＜cbs-value＞|CBS值，取值范围$#33816578#$~$#33816579#$，默认单位：KB
＜pir-value＞|PIR值，取值范围<$#33816584#$~$#33816585#$>，默认单位：Kbps
kbps|以KBPS为单位
mbps|以MBPS为单位
gbps|以GBPS为单位
＜pbs-value＞|PBS值，取值范围$#33816580#$~$#33816581#$，默认单位：KB
set-prec-transmit|设置IP优先级值（0-7）并发送数据包
＜precedence-value＞|IP优先级值，取值范围<0-7>
set-dscp-transmit|设置DSCP值（0-63）并发送数据包
＜dscp-value＞|DSCP值，取值范围<0-63>
set-exp-transmit|设置MPLS优先级值（0-7）并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
＜mpls-exp-value＞|MPLS-EXP值，取值范围<0-7>
drop|丢弃数据包
transmit|发送数据包
set-8021p-transmit|设置802.1P优先级值（0-7）并发送数据包
inner-outer|内外层标记
＜8021p-value＞|802.1P优先级值，取值范围<0-7>
set-prec-transmit|设置IP优先级值（0-7）并发送数据包
＜precedence-value＞|IP优先级值，取值范围<0-7>
set-dscp-transmit|设置DSCP值（0-63）并发送数据包
＜dscp-value＞|DSCP值，取值范围<0-63>
set-exp-transmit|设置MPLS优先级值（0-7）并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
＜mpls-exp-value＞|MPLS-EXP值，取值范围<0-7>
drop|丢弃数据包
transmit|发送数据包
set-8021p-transmit|设置802.1P优先级值（0-7）并发送数据包
inner-outer|内外层标记
＜8021p-value＞|802.1P优先级值，取值范围<0-7>
set-prec-transmit|设置IP优先级值（0-7）并发送数据包
＜precedence-value＞|IP优先级值，取值范围<0-7>
set-dscp-transmit|设置DSCP值（0-63）并发送数据包
＜dscp-value＞|DSCP值，取值范围<0-63>
set-exp-transmit|设置MPLS优先级值（0-7）并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
＜mpls-exp-value＞|MPLS-EXP值，取值范围<0-7>
drop|丢弃数据包
transmit|发送数据包
set-8021p-transmit|设置802.1P优先级值（0-7）并发送数据包
inner-outer|内外层标记
＜8021p-value＞|802.1P优先级值，取值范围<0-7>
statistical-share|流分类标识








### 缺省 


无 






### 使用说明 


1.    同一接口方向下，CAR SET与HQoS互斥。2.    inner-802.1p、outer-802.1p、inner-vlan和outer-vlan只能配置在子接口下。





### 范例 


配置接口gei-0/9/0/11的CAR SET：ZXROSNG(config)#qosZXROSNG(config-qos)#interface gei-0/9/0/11ZXROSNG(config-qos-if-gei-0/9/0/11)#rate-limit input dscp 3 cir 66 cbs 20000 pir 88 pbs 30000 conform-action transmit exceed-action transmit violate-action dropZXROSNG(config-qos-if)#no rate-limit input dscp 3配置接口gei-0/9/0/11的CAR SET：ZXROSNG(config)#qosZXROSNG(config-qos)#interface gei-0/9/0/11ZXROSNG(config-qos-if-gei-0/9/0/11)#rate-limit input dscp 3 cir 66 cbs 20000 pir 88 pbs 30000 conform-action transmit exceed-action transmit violate-action dropZXROSNG(config-qos-if)#no rate-limit input dscp 3





### 相关命令 


无 




## rate-limit 


rate-limit 




### 命令功能 


在接口上配置流限速策略。 






### 命令模式 


 CAR接口配置模式  






### 命令默认权限级别 


15 






### 命令格式 



rate-limit 
  {input 
|output 
} [mode 
 {blind 
|aware 
}] {ipv4 
 {dscp 
 ＜dscp-value 
＞|precedence 
 ＜precedence-value 
＞}|ipv6 
 {dscp 
 ＜dscp-value 
＞|precedence 
 ＜precedence-value 
＞}|{unicast 
|broadcast 
|unknown 
|ipv4-access-list 
 ＜ipv4-access-list-name 
＞|ipv6-access-list 
 ＜ipv6-access-list-name 
＞|dscp 
 ＜dscp-value 
＞|mpls-exp 
 ＜mpls-exp-value 
＞|precedence 
 ＜precedence-value 
＞|localport 
|inner-vlan 
 ＜vlan-range 
＞ [outer-vlan 
 ＜vlan-range 
＞]|outer-vlan 
 ＜vlan-range 
＞|inner-8021p 
 ＜in-8021p-value 
＞ [outer-8021p 
 ＜out-8021p-value 
＞]|outer-8021p 
 ＜out-8021p-value 
＞|multicast 
|link-access-list 
 ＜link-access-list-name 
＞|qos-group 
 ＜qosid-number 
＞}} cir 
 ＜cir-value 
＞ [{kbps 
|mbps 
|gbps 
}] cbs 
 ＜cbs-value 
＞ pir 
 ＜pir-value 
＞ [{kbps 
|mbps 
|gbps 
}] pbs 
 ＜pbs-value 
＞ conform-action 
 {set-multi-exp-transmit 
 ＜multi-mpls-exp value 
＞ ＜multi-mpls-exp value 
＞|set-prec-transmit 
 ＜precedence-value 
＞|set-dscp-transmit 
 ＜dscp-value 
＞|set-exp-transmit 
 [{imposition 
|topmost 
|inner 
}] ＜mpls-exp-value 
＞|drop 
|transmit 
|set-8021p-transmit 
 ＜8021p-value 
＞} exceed-action 
 {set-multi-exp-transmit 
 ＜multi-mpls-exp value 
＞ ＜multi-mpls-exp value 
＞|set-prec-transmit 
 ＜precedence-value 
＞|set-dscp-transmit 
 ＜dscp-value 
＞|set-exp-transmit 
 [{imposition 
|topmost 
|inner 
}] ＜mpls-exp-value 
＞|drop 
|transmit 
|set-8021p-transmit 
 ＜8021p-value 
＞} violate-action 
 {set-multi-exp-transmit 
 ＜multi-mpls-exp value 
＞ ＜multi-mpls-exp value 
＞|set-prec-transmit 
 ＜precedence-value 
＞|set-dscp-transmit 
 ＜dscp-value 
＞|set-exp-transmit 
 [{imposition 
|topmost 
|inner 
}] ＜mpls-exp-value 
＞|drop 
|transmit 
|set-8021p-transmit 
 ＜8021p-value 
＞} [statistical-share 
]
no rate-limit 
  {input 
|output 
} {ipv4 
 {dscp 
 ＜dscp-value 
＞|precedence 
 ＜precedence-value 
＞}|ipv6 
 {dscp 
 ＜dscp-value 
＞|precedence 
 ＜precedence-value 
＞}|{unicast 
|broadcast 
|unknown 
|ipv4-access-list 
 ＜ipv4-access-list-name 
＞|ipv6-access-list 
 ＜ipv6-access-list-name 
＞|dscp 
 ＜dscp-value 
＞|mpls-exp 
 ＜mpls-exp-value 
＞|precedence 
 ＜precedence-value 
＞|localport 
|inner-vlan 
 ＜vlan-range 
＞ [outer-vlan 
 ＜vlan-range 
＞]|outer-vlan 
 ＜vlan-range 
＞|inner-8021p 
 ＜in-8021p-value 
＞ [outer-8021p 
 ＜out-8021p-value 
＞]|outer-8021p 
 ＜out-8021p-value 
＞|multicast 
|link-access-list 
 ＜link-access-list-name 
＞|qos-group 
 ＜qosid-number 
＞}}
				






### 命令参数解释 




参数|描述
---|---
input|输入
output|输出
mode|模式标识
blind|色盲模式
aware|色敏感模式
ipv4|匹配协议类型：IPv4
dscp|DSCP匹配项
＜dscp-value＞|DSCP值，取值范围<0-63>
precedence|匹配IP优先级
＜precedence-value＞|IP优先级值，取值范围<0-7>
ipv6|匹配协议类型：IPv6
dscp|DSCP匹配项
＜dscp-value＞|DSCP值，取值范围<0-63>
precedence|匹配IP优先级
＜precedence-value＞|IP优先级值，取值范围<0-7>
unicast|L2VPN单播流
broadcast|L2VPN广播流
unknown|L2VPN未知流
ipv4-access-list|匹配IPv4 ACL
＜ipv4-access-list-name＞|IPv4 ACL，参数范围<1-31>个字符
ipv6-access-list|匹配IPv6 ACL
＜ipv6-access-list-name＞|IPv6 ACL，参数范围<1-31>个字符
dscp|DSCP匹配项
＜dscp-value＞|DSCP值，取值范围<0-63>
mpls-exp|MPLS-EXP匹配项
＜mpls-exp-value＞|MPLS-EXP值，取值范围<0-7>
precedence|匹配IP优先级
＜precedence-value＞|IP优先级值，取值范围<0-7>
localport|本地端口
inner-vlan|inner-vlan匹配项
＜vlan-range＞|inner-vlan值，参数范围<1-4094>
outer-vlan|outer-vlan匹配项
＜vlan-range＞|inner-vlan值，参数范围<1-4094>
outer-vlan|outer-vlan匹配项
＜vlan-range＞|inner-vlan值，参数范围<1-4094>
inner-8021p|inner-802.1p匹配项
＜in-8021p-value＞|inner-802.1p值，参数范围<0-7>
outer-8021p|outer-802.1p匹配项
＜out-8021p-value＞|outer-802.1p值，参数范围<0-7>
outer-8021p|outer-802.1p匹配项
＜out-8021p-value＞|outer-802.1p值，参数范围<0-7>
multicast|组播匹配项
link-access-list|LINK ACL匹配项
＜link-access-list-name＞|LINK ACL，参数范围<1-31>个字符
qos-group|qos-group匹配项
＜qosid-number＞|qos-group值，参数范围<1-16000>
＜cir-value＞|CIR值，取值范围<$#33816582#$~$#33816583#$>，默认单位：Kbps
kbps|以KBPS为单位
mbps|以MBPS为单位
gbps|以GBPS为单位
＜cbs-value＞|CBS值，取值范围$#33816578#$~$#33816579#$，默认单位：KB
＜pir-value＞|PIR值，取值范围<$#33816584#$~$#33816585#$>，默认单位：Kbps
kbps|以KBPS为单位
mbps|以MBPS为单位
gbps|以GBPS为单位
＜pbs-value＞|PBS值，取值范围$#33816580#$~$#33816581#$，默认单位：KB
set-multi-exp-transmit|设置MPLS内外层标签
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
set-prec-transmit|设置IP优先级值（0-7）并发送数据包
＜precedence-value＞|IP优先级值，取值范围<0-7>
set-dscp-transmit|设置DSCP值（0-63）并发送数据包
＜dscp-value＞|DSCP值，取值范围<0-63>
set-exp-transmit|设置MPLS优先级值（0-7）并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
inner|倒数第二层（最外层为倒数第一层）
＜mpls-exp-value＞|MPLS-EXP值，取值范围<0-7>
drop|丢弃数据包
transmit|发送数据包
set-8021p-transmit|设置802.1P优先级值（0-7）并发送数据包
＜8021p-value＞|802.1P优先级值，取值范围<0-7>
set-multi-exp-transmit|设置MPLS内外层标签
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
set-prec-transmit|设置IP优先级值（0-7）并发送数据包
＜precedence-value＞|IP优先级值，取值范围<0-7>
set-dscp-transmit|设置DSCP值（0-63）并发送数据包
＜dscp-value＞|DSCP值，取值范围<0-63>
set-exp-transmit|设置MPLS优先级值（0-7）并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
inner|倒数第二层（最外层为倒数第一层）
＜mpls-exp-value＞|MPLS-EXP值，取值范围<0-7>
drop|丢弃数据包
transmit|发送数据包
set-8021p-transmit|设置802.1P优先级值（0-7）并发送数据包
＜8021p-value＞|802.1P优先级值，取值范围<0-7>
set-multi-exp-transmit|设置MPLS内外层标签
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
set-prec-transmit|设置IP优先级值（0-7）并发送数据包
＜precedence-value＞|IP优先级值，取值范围<0-7>
set-dscp-transmit|设置DSCP值（0-63）并发送数据包
＜dscp-value＞|DSCP值，取值范围<0-63>
set-exp-transmit|设置MPLS优先级值（0-7）并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
inner|倒数第二层（最外层为倒数第一层）
＜mpls-exp-value＞|MPLS-EXP值，取值范围<0-7>
drop|丢弃数据包
transmit|发送数据包
set-8021p-transmit|设置802.1P优先级值（0-7）并发送数据包
＜8021p-value＞|802.1P优先级值，取值范围<0-7>
statistical-share|流分类标识








### 缺省 


无 






### 使用说明 


1.    同一接口方向下，CAR SET与HQoS互斥。2.    inner-802.1p、outer-802.1p、inner-vlan和outer-vlan只能配置在子接口下。





### 范例 


配置接口gei-0/9/0/11的CAR SET：ZXROSNG(config)#qosZXROSNG(config-qos)#interface gei-0/9/0/11ZXROSNG(config-qos-if-gei-0/9/0/11)#rate-limit input dscp 3 cir 66 cbs 20000 pir 88 pbs 30000 conform-action transmit exceed-action transmit violate-action dropZXROSNG(config-qos-if)#no rate-limit input dscp 3配置接口gei-0/9/0/11的CAR SET：ZXROSNG(config)#qosZXROSNG(config-qos)#interface gei-0/9/0/11ZXROSNG(config-qos-if-gei-0/9/0/11)#rate-limit input dscp 3 cir 66 cbs 20000 pir 88 pbs 30000 conform-action transmit exceed-action transmit violate-action dropZXROSNG(config-qos-if)#no rate-limit input dscp 3





### 相关命令 


无 




# QoS基础配置命令 
## 8021p 


8021p 




### 命令功能 


802.1p与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



8021p 
  ＜8021p-value 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no 8021p 
  ＜8021p-value 
＞
				






### 命令参数解释 




参数|描述
---|---
＜8021p-value＞|802.1p优先级，取值范围<0-7>
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


8021p配置入方向802.1p用户优先级到本地服务级别的映射。 






### 范例 


# 配置802.1p 值为2 的上行VLAN 报文对应的服务等级为AF1，并将报文标记为绿色。ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#8021p 2 mapped to phb af1 green






### 相关命令 


show diffserv-domainshow running-config




## bandwidth 


bandwidth 




### 命令功能 


配置策略类的最小可用带宽。 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 




bandwidth 
 percent 
 ＜percent-value 
＞

no bandwidth 








### 命令参数解释 




参数|描述
---|---
percent|最小带宽的百分比
＜percent-value＞|最小带宽的百分比值，范围：1–100








### 缺省 


无 






### 使用说明 


1. 同一策略映射配置模式下，bandwidth 与priority-level互斥（配置在class-default上的priority-level除外）。2. 同一策略类配置下，bandwidth 与priority-llq、priority-level互斥。3. 同一策略映射配置模式下，所有策略类的带宽之和不能超过100。





### 范例 


配置策略映射为policy1、匹配zte2最小可用带宽的60：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#class zte2ZXROSNG(config-pmap-c)#bandwidth percent 60





### 相关命令 


show policy-map 




## bandwidth 


bandwidth 




### 命令功能 


配置策略类的最小可用带宽。 






### 命令模式 


 PHB-QoS策略类模式  






### 命令默认权限级别 


15 






### 命令格式 




bandwidth 
 percent 
 ＜percent-value 
＞

no bandwidth 








### 命令参数解释 




参数|描述
---|---
percent|最小带宽的百分比
＜percent-value＞|最小带宽的百分比值，范围：1–100








### 缺省 


无 






### 使用说明 


1. 同一策略映射配置模式下，bandwidth 与priority-level互斥（配置在class-default上的priority-level除外）。2. 同一策略类配置下，bandwidth 与priority-llq、priority-level互斥。3. 同一策略映射配置模式下，所有策略类的带宽之和不能超过100。





### 范例 


配置策略映射为policy1、匹配zte2最小可用带宽的60：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#class zte2ZXROSNG(config-pmap-c)#bandwidth percent 60





### 相关命令 


show policy-map 




## bandwidth 


bandwidth 




### 命令功能 


配置策略类的最小可用带宽。 






### 命令模式 


 子接口Qos策略类模式  






### 命令默认权限级别 


15 






### 命令格式 




bandwidth 
 percent 
 ＜percent-value 
＞

no bandwidth 








### 命令参数解释 




参数|描述
---|---
percent|最小带宽的百分比
＜percent-value＞|最小带宽的百分比值，范围：1–100








### 缺省 


无 






### 使用说明 


1. 同一策略映射配置模式下，bandwidth 与priority-level互斥（配置在class-default上的priority-level除外）。2. 同一策略类配置下，bandwidth 与priority-llq、priority-level互斥。3. 同一策略映射配置模式下，所有策略类的带宽之和不能超过100。





### 范例 


配置策略映射为policy1、匹配zte2最小可用带宽的60：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#class zte2ZXROSNG(config-pmap-c)#bandwidth percent 60





### 相关命令 


show policy-map 




## bandwidth-remaining 


bandwidth-remaining 




### 命令功能 


配置策略类的剩余带宽 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 




bandwidth-remaining 
 percent 
 ＜per_value 
＞

no bandwidth-remaining 








### 命令参数解释 




参数|描述
---|---
percent|标识配置剩余带宽
＜per_value＞|剩余带宽的百分比，范围：1-100








### 缺省 


无 






### 使用说明 


1．    在同一策略映射配置模式下，剩余带宽之和不能超过100.2．    在同一策略类配置模式下，剩余带宽与带宽相冲突.





### 范例 


配置策略映射为policy1、匹配流zte2最小可用剩余带宽的60：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#class zte2ZXROSNG(config-pmap-c)#bandwidth-remaining percent 60





### 相关命令 


show policy-map [<policy-map-name>]bandwidth percent<percentage>




## class 


class 




### 命令功能 


关联类映射并进入策略类配置模式。 






### 命令模式 


 QoS策略映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 



class 
  {class-default 
|＜pmap-class-name 
＞}
no class 
  {class-default 
|＜pmap-class-name 
＞}
				






### 命令参数解释 




参数|描述
---|---
class-default|默认关联类
＜pmap-class-name＞|关联的类映射名称，长度1–31个字符








### 缺省 


无 






### 使用说明 


1. <class-name>需要先使用class-map命令配置。2. 在<class-name>的类映射配置模式下，至少需要利用match显式匹配一个匹配项。





### 范例 


策略映射policy1关联类映射名称为zte2，并进入策略映射类配置模式：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#class zte2 ZXROSNG(config-pmap-c)#





### 相关命令 


show policy-map 




## class 


class 




### 命令功能 


关联类映射并进入策略类配置模式。 






### 命令模式 


 策略类映射CAR模板配置模式  






### 命令默认权限级别 


15 






### 命令格式 



class 
  {class-default 
|＜pmap-class-name 
＞}
no class 
  {class-default 
|＜pmap-class-name 
＞}
				






### 命令参数解释 




参数|描述
---|---
class-default|默认关联类
＜pmap-class-name＞|关联的类映射名称，长度1–31个字符








### 缺省 


无 






### 使用说明 


1. <class-name>需要先使用class-map命令配置。2. 在<class-name>的类映射配置模式下，至少需要利用match显式匹配一个匹配项。





### 范例 


策略映射policy1关联类映射名称为zte2，并进入策略映射类配置模式：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#class zte2 ZXROSNG(config-pmap-c)#





### 相关命令 


show policy-map 




## class 


class 




### 命令功能 


关联类映射并进入策略类配置模式。 






### 命令模式 


 PHB-QoS策略模式  






### 命令默认权限级别 


15 






### 命令格式 



class 
  {class-default 
|＜pmap-class-name 
＞}
no class 
  {class-default 
|＜pmap-class-name 
＞}
				






### 命令参数解释 




参数|描述
---|---
class-default|默认关联类
＜pmap-class-name＞|关联的类映射名称，长度1–31个字符








### 缺省 


无 






### 使用说明 


1. <class-name>需要先使用class-map命令配置。2. 在<class-name>的类映射配置模式下，至少需要利用match显式匹配一个匹配项。





### 范例 


策略映射policy1关联类映射名称为zte2，并进入策略映射类配置模式：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#class zte2 ZXROSNG(config-pmap-c)#





### 相关命令 


show policy-map 




## class 


class 




### 命令功能 


关联类映射并进入策略类配置模式。 






### 命令模式 


 子接口Qos策略模式  






### 命令默认权限级别 


15 






### 命令格式 



class 
  {class-default 
|＜pmap-class-name 
＞}
no class 
  {class-default 
|＜pmap-class-name 
＞}
				






### 命令参数解释 




参数|描述
---|---
class-default|默认关联类
＜pmap-class-name＞|关联的类映射名称，长度1–31个字符








### 缺省 


无 






### 使用说明 


1. <class-name>需要先使用class-map命令配置。2. 在<class-name>的类映射配置模式下，至少需要利用match显式匹配一个匹配项。





### 范例 


策略映射policy1关联类映射名称为zte2，并进入策略映射类配置模式：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#class zte2 ZXROSNG(config-pmap-c)#





### 相关命令 


show policy-map 




## class-map 


class-map 




### 命令功能 


创建class-map名字并进入类映射配置模式。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



class-map 
  ＜class-name 
＞ {{match-all 
|match-any 
} [service-type 
 ＜service-type-value 
＞ [effect-order 
 ＜effetc-order-value 
＞]]|phb-based 
|sub-interface-based 
|flowspec-based 
|switch-fabric-based 
}
no class-map 
  ＜class-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜class-name＞|class-map的名称
match-all|匹配类型为匹配所有
match-any|匹配类型为匹配任意一个
＜service-type-value＞|服务类型，范围<1-255>
＜effetc-order-value＞|生效顺序，范围<1-255>
phb-based|基于PHB的流分类标识
sub-interface-based|基于子接口流分类标识
flowspec-based|基于子流规格的流分类标识
switch-fabric-based|基于交换QoS的流分类标识








### 缺省 


无 






### 使用说明 


 1. 不能对class-default的类映射名进行配置操作。2. 若class-map已在某个policy-map中关联，则不能再对该已关联的class-map操作。3. 若选择match-all，必须匹配指定class-map的所有match项才能生效；若选择match-any，则匹配指定class-map的任一match项即可生效。





### 范例 


创建名称为zte的类映射：ZXROSNG(config)#class-map zte match-allZXROSNG(config-cmap)#





### 相关命令 


show class-map 




## description 


description 




### 命令功能 


配置class-map文本描述 






### 命令模式 


 交换QoS流分类模式  






### 命令默认权限级别 


15 






### 命令格式 




description 
  ＜class-map-description 
＞

no description 








### 命令参数解释 




参数|描述
---|---
＜class-map-description＞|class-map文本描述








### 缺省 


 无 






### 使用说明 


无 






### 范例 


ZXROSNG(config-cmap)#description ztedescription 






### 相关命令 


无 




## description 


description 




### 命令功能 


配置class-map文本描述 






### 命令模式 


 子接口Qos流分类模式  






### 命令默认权限级别 


15 






### 命令格式 




description 
  ＜class-map-description 
＞

no description 








### 命令参数解释 




参数|描述
---|---
＜class-map-description＞|class-map文本描述








### 缺省 


 无 






### 使用说明 


无 






### 范例 


ZXROSNG(config-cmap)#description ztedescription 






### 相关命令 


无 




## description 


description 




### 命令功能 


配置class-map文本描述 






### 命令模式 


 PHB-QoS流分类模式  






### 命令默认权限级别 


15 






### 命令格式 




description 
  ＜class-map-description 
＞

no description 








### 命令参数解释 




参数|描述
---|---
＜class-map-description＞|class-map文本描述








### 缺省 


 无 






### 使用说明 


无 






### 范例 


ZXROSNG(config-cmap)#description ztedescription 






### 相关命令 


无 




## description 


description 




### 命令功能 


配置class-map文本描述 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




description 
  ＜class-map-description 
＞

no description 








### 命令参数解释 




参数|描述
---|---
＜class-map-description＞|class-map文本描述








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config-cmap)#description ztedescription 






### 相关命令 


无 




## diffserv domain 


diffserv domain 




### 命令功能 


创建Diffserv域，并进入DS域配置模式。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



diffserv domain 
  ＜domain-name 
＞
no diffserv domain 
  ＜domain-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜domain-name＞|Diffserv域名称，最长31个字符








### 缺省 


无 






### 使用说明 


1. 系统缺省<default>的DS域映射策略表，不支持用户修改。2. 系统最多支持8个用户自定义DS域映射策略表。






### 范例 


定义一个DS 域d1。ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#






### 相关命令 


show diffserv-domainshow running-config




## ipv4-access-list 


ipv4-access-list 




### 命令功能 


IPv4 ACL与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv4-access-list 
  ＜ipv4-acl-name 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no ipv4-access-list 
  ＜ipv4-acl-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ipv4-acl-name＞|ACL名称，最长31个字符
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


1. 用到的IPv4 ACL，可以是用户未事先配置的2. IPv4 ACL在应用的情况下，也允许用户删除3. ipv4-access-list配置入方向匹配ACL的流量到本地服务级别的映射。






### 范例 


#将ipv4-access-list为acl1的报文映射为服务等级AF1，并将报文的颜色设置为红色。ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#ipv4-access-list acl1 mapped to phb af1 red






### 相关命令 


show diffserv-domainshow running-config




## ipv4-dscp 


ipv4-dscp 




### 命令功能 


IPv4 DSCP与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv4-dscp 
  ＜dscp-value 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no ipv4-dscp 
  ＜dscp-value 
＞
				






### 命令参数解释 




参数|描述
---|---
＜dscp-value＞|IPv4 DSCP优先级，取值范围<0-63>
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


ipv4-dscp配置入方向IPv4 DSCP用户优先级到本地服务级别的映射。 






### 范例 


#将DSCP 值为1的报文映射为服务等级AF1，并将报文的颜色设置为绿色 ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#ipv4-dscp 1 mapped to phb af1 yellow






### 相关命令 


show diffserv-domainshow running-config




## ipv4-mixed-access-list 


ipv4-mixed-access-list 




### 命令功能 


IPv4混合 ACL与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv4-mixed-access-list 
  ＜ipv4-mixed-acl-name 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no ipv4-mixed-access-list 
  ＜ipv4-mixed-acl-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ipv4-mixed-acl-name＞|ACL名称，最长31个字符
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


1. 用到的IPv4混合 ACL，可以是用户未事先配置的2. IPv4混合 ACL在应用的情况下，也允许用户删除3. ipv4-mixed-access-list配置入方向匹配ACL的流量到本地服务级别的映射。






### 范例 


# 将ipv4-mixed-access-list为acl1的报文映射为服务等级AF1，并将报文的颜色设置为红色.ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#ipv4-mixed-access-list acl1 mapped to phb af1 red






### 相关命令 


show diffserv-domainshow running-config




## ipv6-access-list 


ipv6-access-list 




### 命令功能 


IPv6 ACL与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv6-access-list 
  ＜ipv6-acl-name 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no ipv6-access-list 
  ＜ipv6-acl-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ipv6-acl-name＞|ACL名称，最长31个字符
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


1. 用到的IPv6 ACL，可以是用户未事先配置的2. IPv6 ACL在应用的情况下，也允许用户删除3. ipv6-access-list配置入方向匹配ACL的流量到本地服务级别的映射。






### 范例 


#将ipv6-access-list为acl1的报文映射为服务等级AF1，并将报文的颜色设置为红色。ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#ipv6-access-list acl1 mapped to phb af1 red






### 相关命令 


show diffserv-domainshow running-config




## ipv6-dscp 


ipv6-dscp 




### 命令功能 


IPv6 DSCP与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv6-dscp 
  ＜ipv6-dscp-value 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no ipv6-dscp 
  ＜ipv6-dscp-value 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ipv6-dscp-value＞|IPv6 DSCP优先级，取值范围<0-63>
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


ipv6-dscp配置入方向IPv6 DSCP用户优先级到本地服务级别的映射。 






### 范例 


#将DSCP 值为1的报文映射为服务等级AF1，并将报文的颜色设置为绿色 ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#ipv6-dscp 1 mapped to phb af1 yellow






### 相关命令 


show diffserv-domainshow running-config




## ipv6-mixed-access-list 


ipv6-mixed-access-list 




### 命令功能 


IPv6混合 ACL与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv6-mixed-access-list 
  ＜ipv6-mixed-acl-name 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no ipv6-mixed-access-list 
  ＜ipv6-mixed-acl-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ipv6-mixed-acl-name＞|ACL名称，最长31个字符
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


1. 用到的IPv6混合 ACL，可以是用户未事先配置的2. IPv6混合 ACL在应用的情况下，也允许用户删除3. ipv6-mixed-access-list配置入方向匹配ACL的流量到本地服务级别的映射。






### 范例 


# 将ipv6-mixed-access-list为acl1的报文映射为服务等级AF1，并将报文的颜色设置为红色.ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#ipv6-mixed-access-list acl1 mapped to phb af1 red






### 相关命令 


show diffserv-domainshow running-config




## link-access-list 


link-access-list 




### 命令功能 


二层 ACL与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



link-access-list 
  ＜link-acl-name 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no link-access-list 
  ＜link-acl-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜link-acl-name＞|ACL名称，最长31个字符
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


1. 用到的link ACL，可以是用户未事先配置的2. link ACL在应用的情况下，也允许用户删除3. link-access-list配置入方向匹配ACL的流量到本地服务级别的映射。






### 范例 


 #将link-access-list为acl1的报文映射为服务等级AF1，并将报文的颜色设置为红色.ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#link-access-list acl1 mapped to phb af1 red






### 相关命令 


show diffserv-domainshow running-config




## match child 


match child 




### 命令功能 


匹配子层的流分类规则 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match child 
 

no match child 








### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


一个流分类下只能配置一条match child，并且与其它匹配类型互斥 






### 范例 


ZXROSNG(config)#class-map zte match-allZXROSNG(config-flowspec-based-class)# match child






### 相关命令 


无 




## match dscp range 


match dscp range 




### 命令功能 


根据IP DSCP值来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match dscp range 
  [not 
] ＜range 
＞

no match dscp range 








### 命令参数解释 




参数|描述
---|---
not|逻辑取反
＜range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte match-allZXROSNG(config-cmap)#match dscp range 2-6,10-15





### 相关命令 


无 




## match dscp reserved-words 


match dscp reserved-words 




### 命令功能 


根据DSCP的预留关键字来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 



match dscp reserved-words 
  ＜DSCP-value 
＞
no match dscp reserved-words 
  ＜DSCP-value 
＞
				






### 命令参数解释 




参数|描述
---|---
＜DSCP-value＞|DSCP预留关键字，预留关键字到dscp值的映射分别是default 0、AF11 10、AF12 12、AF13 14、AF21 18、AF22 20、AF23 22、AF31 26、AF32 28、AF33 30、AF41 34、AF42  36、AF43 38、EF 46 、CS1 8、CS2 16、CS3 24、CS4 32、CS5 40、CS6 48、CS7 56








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte match-allZXROSNG(config-cmap)#match dscp reserved-words default





### 相关命令 


无 




## match in-8021p 


match in-8021p 




### 命令功能 


根据内层802.1p值来建立流分类规则 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match in-8021p 
  ＜range 
＞

no match in-8021p 








### 命令参数解释 




参数|描述
---|---
＜range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte6 match-allZXROSNG(config-cmap)#match in-8021p 0,1-3,5





### 相关命令 


无 




## match in-vlan 


match in-vlan 




### 命令功能 


根据内层VLAN值来建立流分类规则 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match in-vlan 
  ＜vlan-range 
＞

no match in-vlan 








### 命令参数解释 




参数|描述
---|---
＜vlan-range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte4 match-allZXROSNG(config-cmap)#match in-vlan 1-20,40-50,100,200-250





### 相关命令 


无 




## match ipv4 dscp range 


match ipv4 dscp range 




### 命令功能 


根据IPv4 DSCP值来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match ipv4 dscp range 
  [not 
] ＜range 
＞

no match ipv4 dscp range 








### 命令参数解释 




参数|描述
---|---
not|逻辑取反
＜range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte match-allZXROSNG(config-cmap)#match ipv4 dscp range 2-6,10-15





### 相关命令 


无 




## match ipv4 dscp reserved-words 


match ipv4 dscp reserved-words 




### 命令功能 


根据IPv4 DSCP的预留关键字来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 



match ipv4 dscp reserved-words 
  ＜DSCP-value 
＞
no match ipv4 dscp reserved-words 
  ＜DSCP-value 
＞
				






### 命令参数解释 




参数|描述
---|---
＜DSCP-value＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte match-allZXROSNG(config-cmap)#match ipv4 dscp reserved-words default





### 相关命令 


无 




## match ipv4 precedence 


match ipv4 precedence 




### 命令功能 


根据IPv4 Precedence值来建立流分类规则





### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 



match ipv4 precedence 
  [not 
] ＜range 
＞

no match ipv4 precedence 








### 命令参数解释 




参数|描述
---|---
not|逻辑取反
＜range＞|范围：0–7，最多可配置四段值或区间，每段用逗号隔开








### 缺省 


无





### 使用说明 


无





### 范例 


ZXROSNG(config)#class-map zte2 match-allZXROSNG(config-cmap)#match ipv4 precedence 0-2,4,6-7





### 相关命令 


无 




## match ipv4-access-list 


match ipv4-access-list 




### 命令功能 


根据IPv4类型的ACL规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 



match ipv4-access-list 
  ＜ipv4-access-list-name 
＞
no match ipv4-access-list 
  ＜ipv4-access-list-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ipv4-access-list-name＞|指定的IPv4类型ACL规则名称








### 缺省 


无 






### 使用说明 


在同一类映射下，最多可配置64个不同的ACL名称 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match ipv4-access-list ztezxr10





### 相关命令 


无 




## match ipv6 dscp range 


match ipv6 dscp range 




### 命令功能 


根据IPv6 DSCP值来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match ipv6 dscp range 
  [not 
] ＜range 
＞

no match ipv6 dscp range 








### 命令参数解释 




参数|描述
---|---
not|逻辑取反
＜range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte match-allZXROSNG(config-cmap)#match ipv6 dscp range 2-6,10-15





### 相关命令 


无 




## match ipv6 dscp reserved-words 


match ipv6 dscp reserved-words 




### 命令功能 


根据IPv6 DSCP的预留关键字来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 



match ipv6 dscp reserved-words 
  ＜DSCP-value 
＞
no match ipv6 dscp reserved-words 
  ＜DSCP-value 
＞
				






### 命令参数解释 




参数|描述
---|---
＜DSCP-value＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte match-allZXROSNG(config-cmap)#match ipv6 dscp reserved-words default





### 相关命令 


无 




## match ipv6 precedence 


match ipv6 precedence 




### 命令功能 


匹配IPv6的优先级字段 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match ipv6 precedence 
  [not 
] ＜range 
＞

no match ipv6 precedence 








### 命令参数解释 




参数|描述
---|---
not|逻辑取反
＜range＞|优先级值，范围 0-7，最多可配置四段值或区间，每段用逗号隔开。








### 缺省 


无 






### 使用说明 


一个class map实例中仅支持一条该命令，最多可配置一段值或区间。 






### 范例 


ZXROSNG(config)#class-map zteZXROSNG(config-flowspec-based-class)# match ipv6 precedence 0,3-4,6,7






### 相关命令 


无 




## match ipv6-access-list 


match ipv6-access-list 




### 命令功能 


根据IPv6类型的ACL规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 



match ipv6-access-list 
  ＜ipv6-access-list-name 
＞
no match ipv6-access-list 
  ＜ipv6-access-list-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ipv6-access-list-name＞|指定的IPv6类型ACL规则名称








### 缺省 


无 






### 使用说明 


在同一类映射下，最多可配置64个不同的ACL名称 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match ipv6-access-list ztezxr10





### 相关命令 


无 




## match link-access-list 


match link-access-list 




### 命令功能 


根据LINK类型的ACL规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 



match link-access-list 
  ＜link-access-list-name 
＞
no match link-access-list 
  ＜link-access-list-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜link-access-list-name＞|指定的LINK ACL规则名称








### 缺省 


无 






### 使用说明 


在同一类映射下，最多可配置64个不同的ACL名称 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match link-access-list ztezxr10





### 相关命令 


无 




## match mac-address 


match mac-address 




### 命令功能 


根据MAC地址值来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match mac-address 
  ＜mac-address 
＞

no match mac-address 








### 命令参数解释 




参数|描述
---|---
＜mac-address＞|MAC地址的具体值








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)#match mac-address 1111.1230.4567





### 相关命令 


无 




## match mpls-exp 


match mpls-exp 




### 命令功能 


根据MPLS-EXP规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match mpls-exp 
  ＜range 
＞

no match mpls-exp 








### 命令参数解释 




参数|描述
---|---
＜range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


在同一类映射下，最多可配置64个不同的ACL名称 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match mpls-exp 1





### 相关命令 


无 




## match multi-cast 


match multi-cast 




### 命令功能 


根据多播规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match multi-cast 
 

no match multi-cast 








### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match multi-cast





### 相关命令 


无 




## match out-8021p 


match out-8021p 




### 命令功能 


根据外层8021P规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match out-8021p 
  ＜range 
＞

no match out-8021p 








### 命令参数解释 




参数|描述
---|---
＜range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte7 match-allZXROSNG(config-cmap)#match out-8021p 1,4-5,7





### 相关命令 


无 




## match out-vlan 


match out-vlan 




### 命令功能 


根据外层VLAN规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match out-vlan 
  ＜vlan-range 
＞

no match out-vlan 








### 命令参数解释 




参数|描述
---|---
＜vlan-range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte5 match-allZXROSNG(config-cmap)#match out-vlan 1-20,40-50,100,200-250





### 相关命令 


无 




## match precedence 


match precedence 




### 命令功能 


根据IP优先级规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match precedence 
  [not 
] ＜range 
＞

no match precedence 








### 命令参数解释 




参数|描述
---|---
not|逻辑取反
＜range＞|配置参数范围，最多只能四段值或区间








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte2 match-allZXROSNG(config-cmap)#match precedence 0-2,4,6-7





### 相关命令 


无 




## match qos-group 


match qos-group 




### 命令功能 


根据qos group ID规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match qos-group 
  ＜qosid-number 
＞

no match qos-group 








### 命令参数解释 




参数|描述
---|---
＜qosid-number＞|指定qos group ID的具体值，范围：1–65535








### 缺省 


无 






### 使用说明 


在同一类映射下，最多可配置64个不同的ACL名称 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match qos-group 1





### 相关命令 


无 




## match service-class 


match service-class 




### 命令功能 


根据服务等级规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match service-class 
  ＜Service-class 
＞

no match service-class 








### 命令参数解释 




参数|描述
---|---
＜Service-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte11 match-allZXROSNG(config-cmap)#match service-class EF





### 相关命令 


无 




## match uni-cast 


match uni-cast 




### 命令功能 


根据单播规则来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match uni-cast 
 

no match uni-cast 








### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match uni-cast





### 相关命令 


无 




## match vpls 


match vpls 




### 命令功能 


根据VPLS的名称来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match vpls 
  ＜vpls-name 
＞

no match vpls 








### 命令参数解释 




参数|描述
---|---
＜vpls-name＞|指定的VPLS实例名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match vpls aaa





### 相关命令 


无 




## match vpws 


match vpws 




### 命令功能 


根据VPWS的名称来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match vpws 
  ＜vpws-name 
＞

no match vpws 








### 命令参数解释 




参数|描述
---|---
＜vpws-name＞|指定的VPWS实例名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match vpws aaa





### 相关命令 


无 




## match vrf-name 


match vrf-name 




### 命令功能 


根据VRF的名称来建立class-map数据流 






### 命令模式 


 QoS类映射配置模式  






### 命令默认权限级别 


15 






### 命令格式 




match vrf-name 
  ＜vpn-name 
＞

no match vrf-name 








### 命令参数解释 




参数|描述
---|---
＜vpn-name＞|指定的VRF实例名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte8 match-allZXROSNG(config-cmap)# match vrf aaa





### 相关命令 


无 




## match 


match 




### 命令功能 


根据配置的参数来建立class-map数据流。 






### 命令模式 


 PHB-QoS流分类模式  






### 命令默认权限级别 


15 






### 命令格式 




match 
 service-class 
 ＜Service-class 
＞

no match 
 service-class 








### 命令参数解释 




参数|描述
---|---
service-class|服务等级
＜Service-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>








### 缺省 


无 






### 使用说明 


无 






### 范例 


建立匹配规则为PHB的class-map数据流zte11：ZXROSNG(config)#class-map zte11 match-allZXROSNG(config-cmap)#match service-class EF






### 相关命令 


show class-map 




## match 


match 




### 命令功能 


根据配置的参数来建立class-map数据流。 






### 命令模式 


 子接口Qos流分类模式  






### 命令默认权限级别 


15 






### 命令格式 



match 
  {interface 
 ＜interface-name 
＞|localport 
}
no match 
  {localport 
|interface 
}
				






### 命令参数解释 




参数|描述
---|---
interface|根据接口名来建立class-map数据流
＜interface-name＞|接口的名称
localport|本接口








### 缺省 


无 






### 使用说明 


1.在同一类映射下，match localport与其它所有匹配规则冲突。 






### 范例 


建立class-map数据流zte10：ZXROSNG(config)#class-map zte10 match-allZXROSNG(config-cmap)#match localport






### 相关命令 


show class-map 




## mpls-exp 


mpls-exp 




### 命令功能 


MPLS EXP与PHB之间的映射 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



mpls-exp 
  ＜mpls-exp-value 
＞ mapped 
 to 
 phb 
 ＜serv-class 
＞ {green 
|yellow 
|red 
}
no mpls-exp 
  ＜mpls-exp-value 
＞
				






### 命令参数解释 




参数|描述
---|---
＜mpls-exp-value＞|MPLS EXP优先级，取值范围<0-7>
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


mpls-exp配置入方向MPLS EXP用户优先级到本地服务级别的映射。 






### 范例 


#将mpls-exp 值为1的报文映射为服务等级AF1，并将报文的颜色设置为红色 ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#mpls-exp 1 mapped to phb af1 red






### 相关命令 


show diffserv-domainshow running-config




## phb 


phb 




### 命令功能 


phb映射为vlan 802.1p的命令、映射为ipv4 dscp的命令、映射为ipv6 dscp的命令、映射为mpls exp的命令 






### 命令模式 


 DS域模式  






### 命令默认权限级别 


15 






### 命令格式 



phb 
  ＜serv-class 
＞ {green 
|yellow 
|red 
} mapped 
 to 
 {8021p 
 ＜8021p-value 
＞|ipv4-dscp 
 ＜dscp-value 
＞|mpls-exp 
 ＜mpls-exp-value 
＞|ipv6-dscp 
 ＜dscp-value 
＞}
no phb 
  ＜serv-class 
＞ {green 
|yellow 
|red 
} mapped 
 to 
 {8021p 
|ipv4-dscp 
|mpls-exp 
|ipv6-dscp 
}
				






### 命令参数解释 




参数|描述
---|---
＜serv-class＞|服务等级，取值<CS7, CS6, EF, AF4, AF3, AF2, AF1, BE>
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级
8021p|映射为vlan 802.1p的命令
＜8021p-value＞|802.1p优先级，取值范围<0-7>
ipv4-dscp|映射为ipv4 dscp的命令
＜dscp-value＞|DSCP优先级，取值范围<0-63>
mpls-exp|映射为mpls exp的命令
＜mpls-exp-value＞|MPLS EXP优先级，取值范围<0-7>
ipv6-dscp|映射为ipv6 dscp的命令
＜dscp-value＞|DSCP优先级，取值范围<0-63>








### 缺省 


无 






### 使用说明 


1. phb mapped to 8021p配置出方向phb映射到8021p的流量。2. phb mapped to ipv4-dscp配置出方向phb匹配ipv4 dscp的流量。3. phb mapped to ipv6-dscp配置出方向phb匹配ipv6 dscp的流量。4. phb mapped to 8021p配置出方向phb匹配mpls-exp的流量。






### 范例 


# 将服务等级为AF1，标识为绿色的报文映射到8021p值为1的下行报文。ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#phb af1 green mapped to 8021p 1
# 将服务等级为AF1，标识为绿色的报文映射到dscp值为1的下行报文。ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#phb af1 green mapped to ipv4-dscp 1# 将服务等级为AF1，标识为绿色的报文映射到ipv6 dscp值为1的下行报文。ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#phb af1 green mapped to ipv6-dscp 1# 将服务等级为AF1，标识为绿色的报文映射到mpls-exp值为1的下行报文。ZXROSNG#con terZXROSNG(config)#diffserv domain d1ZXROSNG(config-d1)#phb af1 green mapped to 8021p 1






### 相关命令 


show diffserv-domainshow running-config




## police 


police 




### 命令功能 


配置策略类的流量监管。 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 




police 
 cir 
 ＜cirValue 
＞ [{kbps 
|mbps 
|gbps 
}] [cbs 
 ＜cbsValue 
＞ [{kb 
|mb 
|gb 
}]] [pir 
 ＜pirValue 
＞ [{kbps 
|mbps 
|gbps 
}] [pbs 
 ＜pbsValue 
＞ [{kb 
|mb 
|gb 
}]]] [conform-action 
 {set-prec-transmit 
 ＜ippConform 
＞|set-dscp-transmit 
 ＜dscpConform 
＞|set-exp-transmit 
 ＜expConform 
＞|set-8021p-transmit 
 ＜8021pConform 
＞|set-priority-transmit 
 ＜priorityConform 
＞|transmit 
|drop 
} exceed-action 
 {set-prec-transmit 
 ＜ippExceed 
＞|set-dscp-transmit 
 ＜dscpExceed 
＞|set-exp-transmit 
 ＜expExceed 
＞|set-8021p-transmit 
 ＜8021pExceed 
＞|set-priority-transmit 
 ＜priorityExceed 
＞|transmit 
|drop 
} violate-action 
 {set-prec-transmit 
 ＜ippViolate 
＞|set-dscp-transmit 
 ＜dscpViolate 
＞|set-exp-transmit 
 ＜expViolate 
＞|set-8021p-transmit 
 ＜8021pViolate 
＞|set-priority-transmit 
 ＜priorityViolate 
＞|transmit 
|drop 
}]

no police 








### 命令参数解释 




参数|描述
---|---
＜cirValue＞|CIR值，最大值和最小值通过性能参数获取；取值范围为$#33816582#$~$#33816583#$；支持单位选择: kbps|mbps|gbps，默认单位kbps
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second
＜cbsValue＞|CBS值($#33816578#$~$#33816579#$)
kb|Kilobyte
mb|Megabyte
gb|Gigabyte
＜pirValue＞|PIR值($#33816584#$~$#33816585#$)
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second
＜pbsValue＞|PBS值($#33816580#$~$#33816581#$)
kb|Kilobyte
mb|Megabyte
gb|Gigabyte
set-prec-transmit|对符合指定速率超出PBS值的数据包，根据设置的IP值优先级发送数据包
＜ippConform＞|IP优先级值（0~7）
set-dscp-transmit|对符合指定速率超出PBS值的数据包，根据设置的DSCP值发送数据包
＜dscpConform＞|DSCP值（0~63）
set-exp-transmit|对符合指定速率超出PBS值的数据包，根据设置的MPLS优先级值并发送数据包
＜expConform＞|MPLS优先级值（0~7）
set-8021p-transmit|对符合指定速率超出PBS值的数据包，根据设置802.1P值优先级发送数据包
＜8021pConform＞|802.1P优先级值（0~7）
set-priority-transmit|对符合指定速率超出PBS值的数据包，根据设置优先级发送数据包
＜priorityConform＞|优先级值（1-4）
transmit|对符合指定速率超出PBS的数据包，发送数据包
drop|对符合指定速率超出PBS值的数据包，丢弃数据包
set-prec-transmit|对符合指定速率超出PBS值的数据包，根据设置的IP值优先级发送数据包
＜ippExceed＞|IP优先级值（0~7）
set-dscp-transmit|对符合指定速率超出PBS值的数据包，根据设置的DSCP值发送数据包
＜dscpExceed＞|DSCP优先级值（0~63）
set-exp-transmit|对符合指定速率超出PBS值的数据包，根据设置的MPLS优先级值并发送数据包
＜expExceed＞|MPLS优先级值（0~7）
set-8021p-transmit|对符合指定速率超出PBS值的数据包，根据设置802.1P值优先级发送数据包
＜8021pExceed＞|802.1P优先级值（0~7）
set-priority-transmit|对符合指定速率超出PBS值的数据包，根据设置优先级发送数据包
＜priorityExceed＞|优先级值（1-4）
transmit|对符合指定速率超出PBS的数据包，发送数据包
drop|对符合指定速率超出PBS值的数据包，丢弃数据包
set-prec-transmit|对符合指定速率超出PBS值的数据包，根据设置的IP值优先级发送数据包
＜ippViolate＞|IP优先级值（0~7)
set-dscp-transmit|对符合指定速率超出PBS值的数据包，根据设置的DSCP值发送数据包
＜dscpViolate＞|DSCP值（0~63）
set-exp-transmit|对符合指定速率超出PBS值的数据包，根据设置的MPLS优先级值并发送数据包
＜expViolate＞|MPLS优先级值（0~7）
set-8021p-transmit|对符合指定速率超出PBS值的数据包，根据设置802.1P值优先级发送数据包
＜8021pViolate＞|802.1P优先级值（0~7）
set-priority-transmit|对符合指定速率超出PBS值的数据包，根据设置优先级发送数据包
＜priorityViolate＞|优先级值（1-4）
transmit|对符合指定速率超出PBS的数据包，发送数据包
drop|对符合指定速率超出PBS值的数据包，丢弃数据包








### 缺省 


无 






### 使用说明 


无 






### 范例 


配置策略映射为policy3、匹配流分类zte4的流量监管：ZXROSNG(config)#class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 200ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#police cir 1024 cbs 512 pir 2048 pbs 1024






### 相关命令 


show policy-map 




## police 


police 




### 命令功能 


配置策略类的流量监管。





### 命令模式 


 策略类CAR模板配置模式  






### 命令默认权限级别 


15 






### 命令格式 



police 
 cir 
 ＜cirValue 
＞ [{kbps 
|mbps 
|gbps 
}] [cbs 
 ＜cbsValue 
＞] pir 
 ＜pirValue 
＞ [{kbps 
|mbps 
|gbps 
}] [pbs 
 ＜pbsValue 
＞] conform-action 
 {set-prec-transmit 
 ＜ippConform 
＞|set-dscp-transmit 
 ＜dscpConform 
＞|set-exp-transmit 
 [{imposition 
|topmost 
|inner 
}] ＜expConform 
＞|set-8021p-transmit 
 ＜8021pConform 
＞|set-multi-exp-transmit 
 ＜multi-mpls-exp value 
＞ ＜multi-mpls-exp value 
＞|transmit 
|drop 
} exceed-action 
 {set-prec-transmit 
 ＜ippExceed 
＞|set-dscp-transmit 
 ＜dscpExceed 
＞|set-exp-transmit 
 [{imposition 
|topmost 
|inner 
}] ＜expExceed 
＞|set-8021p-transmit 
 ＜8021pExceed 
＞|set-multi-exp-transmit 
 ＜multi-mpls-exp value 
＞ ＜multi-mpls-exp value 
＞|transmit 
|drop 
} violate-action 
 {set-prec-transmit 
 ＜ippViolate 
＞|set-dscp-transmit 
 ＜dscpViolate 
＞|set-exp-transmit 
 [{imposition 
|topmost 
|inner 
}] ＜expViolate 
＞|set-8021p-transmit 
 ＜8021pViolate 
＞|set-multi-exp-transmit 
 ＜multi-mpls-exp value 
＞ ＜multi-mpls-exp value 
＞|transmit 
|drop 
}

no police 








### 命令参数解释 




参数|描述
---|---
＜cirValue＞|CIR值，最大值和最小值通过性能参数获取；取值范围为$#33816582#$~$#33816583#$；支持单位选择: kbps|mbps|gbps，默认单位kbps
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second
＜cbsValue＞|CBS值($#33816578#$~$#33816579#$)
＜pirValue＞|PIR值($#33816584#$~$#33816585#$)
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second
＜pbsValue＞|PBS值($#33816580#$~$#33816581#$)
set-prec-transmit|对符合指定速率小于CIR值的数据包，根据设置的IP值优先级发送数据包
＜ippConform＞|IP优先级值（0~7）
set-dscp-transmit|对符合指定速率小于CIR值的数据包，根据设置的DSCP值发送数据包
＜dscpConform＞|DSCP值（0~63）
set-exp-transmit|对符合指定速率小于CIR值的数据包，根据设置的MPLS优先级值并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
inner|倒数第二层（最外层为倒数第一层）
＜expConform＞|MPLS优先级值（0~7）
set-8021p-transmit|对符合指定速率小于CIR值的数据包，根据设置802.1P值优先级发送数据包
＜8021pConform＞|{{802.1P优先级值（0~7）
set-multi-exp-transmit|设置MPLS内外层标签
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
transmit|对符合指定速率小于CIR值的数据包，发送数据包
drop|对符合指定速率小于CIR值的数据包，丢弃数据包
set-prec-transmit|对符合指定速率小于CIR值的数据包，根据设置的IP值优先级发送数据包
＜ippExceed＞|IP优先级值（0~7）
set-dscp-transmit|对符合指定速率小于CIR值的数据包，根据设置的DSCP值发送数据包
＜dscpExceed＞|DSCP值（0~63）
set-exp-transmit|对符合指定速率小于CIR值的数据包，根据设置的MPLS优先级值并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
inner|倒数第二层（最外层为倒数第一层）
＜expExceed＞|MPLS优先级值（0~7）
set-8021p-transmit|对符合指定速率小于CIR值的数据包，根据设置802.1P值优先级发送数据包
＜8021pExceed＞|802.1P优先级值（0~7）
set-multi-exp-transmit|设置MPLS内外层标签
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
transmit|对符合指定速率小于CIR值的数据包，发送数据包
drop|对符合指定速率小于CIR值的数据包，丢弃数据包
set-prec-transmit|对符合指定速率小于CIR值的数据包，根据设置的IP值优先级发送数据包
＜ippViolate＞|IP优先级值（0~7）
set-dscp-transmit|对符合指定速率小于CIR值的数据包，根据设置的DSCP值发送数据包
＜dscpViolate＞|DSCP优先级值（0~63）
set-exp-transmit|对符合指定速率小于CIR值的数据包，根据设置的MPLS优先级值并发送数据包
imposition|标识除最外层的所有层
topmost|标识最外层
inner|倒数第二层（最外层为倒数第一层）
＜expViolate＞|MPLS优先级值（0~7）
set-8021p-transmit|对符合指定速率小于CIR值的数据包，根据设置802.1P值优先级发送数据包
＜8021pViolate＞|802.1P优先级值（0~7）
set-multi-exp-transmit|设置MPLS内外层标签
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
＜multi-mpls-exp value＞|设置内层exp的值（0~7）
transmit|对符合指定速率小于CIR值的数据包，发送数据包
drop|对符合指定速率小于CIR值的数据包，丢弃数据包








### 缺省 


无 






### 使用说明 


无 






### 范例 


配置策略映射为policy3、匹配流分类zte4的流量监管：ZXROSNG(config)#class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 200ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#police cir 1024 cbs 512 pir 2048 pbs 1024





### 相关命令 


show policy-map



## police 


police 




### 命令功能 


配置策略类的流量监管。





### 命令模式 


 PHB-QoS策略类模式  






### 命令默认权限级别 


15 






### 命令格式 



police 
 cir 
 ＜cirValue 
＞ [{kbps 
|mbps 
|gbps 
}] [cbs 
 ＜cbsValue 
＞ [{kb 
|mb 
|gb 
}]] [pir 
 ＜pirValue 
＞ [{kbps 
|mbps 
|gbps 
}] [pbs 
 ＜pbsValue 
＞ [{kb 
|mb 
|gb 
}]]]

no police 








### 命令参数解释 




参数|描述
---|---
＜cirValue＞|CIR值，最大值和最小值通过性能参数获取；取值范围为$#33816582#$~$#33816583#$；支持单位选择: kbps|mbps|gbps，默认单位kbps
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second
＜cbsValue＞|CBS值($#33816578#$~$#33816579#$)
kb|单位：Kilobyte
mb|单位，Megabyte
gb|单位，Gigabyte
＜pirValue＞|PIR值($#33816584#$~$#33816585#$)
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second
＜pbsValue＞|PBS值($#33816580#$~$#33816581#$)
kb|单位：Kilobyte
mb|单位，Megabyte
gb|单位，Gigabyte








### 缺省 


无 






### 使用说明 


无 






### 范例 


配置策略映射为policy3、匹配流分类zte4的流量监管：ZXROSNG(config)#class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 200ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#police cir 1024 cbs 512 pir 2048 pbs 1024





### 相关命令 


show policy-map



## police 


police 




### 命令功能 


配置策略类的流量监管。





### 命令模式 


 子接口Qos策略类模式  






### 命令默认权限级别 


15 






### 命令格式 



police 
 cir 
 ＜cirValue 
＞ [{kbps 
|mbps 
|gbps 
}] [cbs 
 ＜cbsValue 
＞ [{kb 
|mb 
|gb 
}]] [pir 
 ＜pirValue 
＞ [{kbps 
|mbps 
|gbps 
}] [pbs 
 ＜pbsValue 
＞ [{kb 
|mb 
|gb 
}]]]

no police 








### 命令参数解释 




参数|描述
---|---
＜cirValue＞|CIR值，最大值和最小值通过性能参数获取；取值范围为$#33816582#$~$#33816583#$；支持单位选择: kbps|mbps|gbps，默认单位kbps
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second
＜cbsValue＞|CBS值($#33816578#$~$#33816579#$)
kb|单位，Kilobyte
mb|单位，Megabyte
gb|单位，Gigabyte
＜pirValue＞|PIR值($#33816584#$~$#33816585#$)
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second
＜pbsValue＞|PBS值($#33816580#$~$#33816581#$)
kb|单位，Kilobyte
mb|单位，Megabyte
gb|单位，Gigabyte








### 缺省 


无 






### 使用说明 


无 






### 范例 


配置策略映射为policy3、匹配流分类zte4的流量监管：ZXROSNG(config)#class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 200ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#police cir 1024 cbs 512 pir 2048 pbs 1024





### 相关命令 


show policy-map



## policy-map 


policy-map 




### 命令功能 


创建policy-map名字并进入策略映射配置模式。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



policy-map 
  ＜policy-name 
＞ [{car-action-type 
|phb-based 
|sub-interface-based 
|flowspec-based 
|switch-fabric-based 
}]
no policy-map 
  ＜policy-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜policy-name＞|policy-map的名称，长度1–31个字符
car-action-type|CAR模板标志
phb-based|基于phb的流分策略类标识
sub-interface-based|基于子接口流策略类分类标识
flowspec-based|基于子流规格的流策略标识
switch-fabric-based|基于交换QoS的流策略类标识








### 缺省 


无 






### 使用说明 


1. 若policy-map配置了可选参数car-action-type，则不能更新为不带car-action-type的policy-map，反之亦然。2. 若policy-map不配置可选参数car-action-type，则：(1)若某个policy-map已在另一个policy-map中被层级化，不能再对该被层级化的policy-map操作。(2) 若policy-map已在某个接口上HQoS绑定，不能再对该被绑定的policy-map操作。(3) 若policy-map已在交换网上HQoS绑定，不能再对该被绑定的policy-map操作。3. 若policy-map配置了可选参数car-action-type，则：(1) 只支持限速的策略行为，且必须配置限速的动作。(2) 不能被嵌套到其他policy-map中。(3) 如果被接口或交换网上HQoS绑定，支持更新。但被引用不允许删除。4. 引用的class-map的类型必须与policy-map的相同。比如：phb-based类型的policy-map引用的class-map的类型必须是phb-based。






### 范例 


创建名称为policy1的策略映射并进入名称为policy1的策略映射配置模式：ZXROSNG(config)#policy-map policy1ZXROSNG(config-pmap)#





### 相关命令 


show policy-map 




## priority-level 


priority-level 




### 命令功能 


配置策略类的PQ优先。 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 




priority-level 
  ＜pq-level 
＞

no priority-level 








### 命令参数解释 




参数|描述
---|---
＜pq-level＞|PQ的优先级别，范围：1–4








### 缺省 


无 






### 使用说明 


1. 同一策略类配置模式下，priority-level与bandwidth、priority-llq互斥。2. 同一策略映射配置模式下，priority-level与bandwidth互斥。但有如下例外：在非class-default下配置了bandwidth，则在class-default下可以配置priority-level。3. 同一策略映射配置模式下，priority-level与priority-llq互斥，但有如下例外：在非class-default下配置了priority-llq，则在class-default下可以配置priority-level，且<pq-level>为2或3或4。





### 范例 


配置策略映射为policy3、匹配外层VLAN值为300的流分类zte4的PQ优先级为2：ZXROSNG(config)# class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 300ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#priority-level 2





### 相关命令 


show policy-map 




## priority-level 


priority-level 




### 命令功能 


配置策略类的PQ优先。 






### 命令模式 


 PHB-QoS策略类模式  






### 命令默认权限级别 


15 






### 命令格式 




priority-level 
  ＜pq-level 
＞

no priority-level 








### 命令参数解释 




参数|描述
---|---
＜pq-level＞|PQ的优先级别，范围：1–4








### 缺省 


无 






### 使用说明 


1. 同一策略类配置模式下，priority-level与bandwidth、priority-llq互斥。2. 同一策略映射配置模式下，priority-level与bandwidth互斥。但有如下例外：在非class-default下配置了bandwidth，则在class-default下可以配置priority-level。3. 同一策略映射配置模式下，priority-level与priority-llq互斥，但有如下例外：在非class-default下配置了priority-llq，则在class-default下可以配置priority-level，且<pq-level>为2或3或4。





### 范例 


配置策略映射为policy3、匹配外层VLAN值为300的流分类zte4的PQ优先级为2：ZXROSNG(config)# class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 300ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#priority-level 2





### 相关命令 


show policy-map 




## priority-level 


priority-level 




### 命令功能 


配置策略类的PQ优先。 






### 命令模式 


 子接口Qos策略类模式  






### 命令默认权限级别 


15 






### 命令格式 




priority-level 
  ＜pq-level 
＞

no priority-level 








### 命令参数解释 




参数|描述
---|---
＜pq-level＞|PQ的优先级别，范围：1–4








### 缺省 


无 






### 使用说明 


1. 同一策略类配置模式下，priority-level与bandwidth、priority-llq互斥。2. 同一策略映射配置模式下，priority-level与bandwidth互斥。但有如下例外：在非class-default下配置了bandwidth，则在class-default下可以配置priority-level。3. 同一策略映射配置模式下，priority-level与priority-llq互斥，但有如下例外：在非class-default下配置了priority-llq，则在class-default下可以配置priority-level，且<pq-level>为2或3或4。





### 范例 


配置策略映射为policy3、匹配外层VLAN值为300的流分类zte4的PQ优先级为2：ZXROSNG(config)# class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 300ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#priority-level 2





### 相关命令 


show policy-map 




## priority-llq 


priority-llq 




### 命令功能 


配置策略类的LLQ优先。 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 




priority-llq 
 

no priority-llq 








### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


1. 同一策略类配置模式下，priority-llq与bandwidth、priority-level互斥2. 同一策略映射配置模式下，priority-llq与priority-level互斥，但有如下例外：在class-default下配置了priority-level，且<pq-level>为2或3或4，同时在非class-default下配置priority-llq。





### 范例 


配置策略映射为policy2、匹配外层VLAN值为200的流分类zte9为LLQ优先：ZXROSNG(config)# class-map zte9 match-allZXROSNG(config-cmap)#match out-vlan 200ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy2ZXROSNG(config-pmap)#class zte9ZXROSNG(config-pmap-c)#priority-llq





### 相关命令 


show policy-map  




## priority-llq 


priority-llq 




### 命令功能 


配置策略类的LLQ优先。 






### 命令模式 


 PHB-QoS策略类模式  






### 命令默认权限级别 


15 






### 命令格式 




priority-llq 
 

no priority-llq 








### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


1. 同一策略类配置模式下，priority-llq与bandwidth、priority-level互斥2. 同一策略映射配置模式下，priority-llq与priority-level互斥，但有如下例外：在class-default下配置了priority-level，且<pq-level>为2或3或4，同时在非class-default下配置priority-llq。





### 范例 


配置策略映射为policy2、匹配外层VLAN值为200的流分类zte9为LLQ优先：ZXROSNG(config)# class-map zte9 match-allZXROSNG(config-cmap)#match out-vlan 200ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy2ZXROSNG(config-pmap)#class zte9ZXROSNG(config-pmap-c)#priority-llq





### 相关命令 


show policy-map  




## priority-llq 


priority-llq 




### 命令功能 


配置策略类的LLQ优先。 






### 命令模式 


 子接口Qos策略类模式  






### 命令默认权限级别 


15 






### 命令格式 




priority-llq 
 

no priority-llq 








### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


1. 同一策略类配置模式下，priority-llq与bandwidth、priority-level互斥2. 同一策略映射配置模式下，priority-llq与priority-level互斥，但有如下例外：在class-default下配置了priority-level，且<pq-level>为2或3或4，同时在非class-default下配置priority-llq。





### 范例 


配置策略映射为policy2、匹配外层VLAN值为200的流分类zte9为LLQ优先：ZXROSNG(config)# class-map zte9 match-allZXROSNG(config-cmap)#match out-vlan 200ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy2ZXROSNG(config-pmap)#class zte9ZXROSNG(config-pmap-c)#priority-llq





### 相关命令 


show policy-map  




## qos diffserv-domain 


qos diffserv-domain 




### 命令功能 


应用Diffserv域 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



qos diffserv-domain 
 interface 
 ＜interface-name 
＞ apply 
 ＜ds-name 
＞
no qos diffserv-domain 
 interface 
 ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|使用DS域映射命令的接口。支持物理接口、子接口、smartgroup接口、smartgroup子接口
＜ds-name＞|用户自创建的Diffserv域名称，最长31个字符








### 缺省 


无 






### 使用说明 


1. 应用的DS域映射表必须是用户事先创建的2. 在应用的DS域映射表中，用户如果没有配置映射关系，那么按照系统缺省<default>映射表生效






### 范例 


# 在GE 接口上绑定DS 域。ZXROSNG# con terZXROSNG(config)# qos diffserv-domain interface smartgroup1 apply ds-name






### 相关命令 


show diffserv-domainshow running-config




## qos priority interface &amp;lt;mid&amp;gt; trust 


qos priority interface <mid> trust 




### 命令功能 


接口优先级信任 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 




qos priority interface  
 ＜interface-name 
＞ trust 
  {8021p 
|ip-dscp 
|mpls-exp 
}

no qos priority interface  
 ＜interface-name 
＞ trust 








### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口名称，1-31个字符
8021p|接口信任8021p
ip-dscp|接口信任dscp
mpls-exp|接口信任exp








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#qos priority interface gei-0/1/0/1 trust 8021p 






### 相关命令 


无 




## qos schedule interface 


qos schedule interface 




### 命令功能 


隧道接口应用phb-based类型的策略 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



qos schedule interface 
  ＜tunnel-name 
＞ {[{wfq 
 ＜weight_value 
＞|priority-level 
 ＜priority_value 
＞}],[service-policy 
 ＜policy-map name 
＞]}
no qos schedule interface 
  ＜tunnel-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜tunnel-name＞|Name of the attaching tunnel
wfq|wfq队列标识
＜weight_value＞|WFQ调度权重值
priority-level|pq优先队列标识
＜priority_value＞|PQ调度优先级
＜policy-map name＞|policy-map的名字








### 缺省 


无 






### 使用说明 


1. 隧道接口只能应用phb-based类型的策略。 






### 范例 


[M6000\M6000-S]: 在隧道接口gei-0/0/0/1上配置基于 phb-based类型的策略pmap：ZXROSNG(config)#class-map zteZXROSNG(config-cmap)#match out-vlan 800ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map pmap phb-basedZXROSNG(config- phb -based-policy)# class zteZXROSNG(config- phb -based-policy-class)# set 8021p 2ZXROSNG(config- phb -based-policy-class)# exitZXROSNG(config- phb -based-policy)#exitZXROSNG(config)# qos schedule interface gei-0/0/0/1 priority-level 3 service-policy pmap






### 相关命令 


无 




## qos schedule pw 


qos schedule pw 




### 命令功能 


隧道PW上应用phb-based类型的策略。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



qos schedule pw 
  ＜pw-name 
＞ {[{wfq 
 ＜weight_value 
＞|priority-level 
 ＜priority_value 
＞}],[service-policy 
 ＜policy-map name 
＞]}
no qos schedule pw 
  ＜pw-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜pw-name＞|伪线接口名称,格式为”pwX”, X为1-4294967295
wfq|wfq队列标识
＜weight_value＞|WFQ调度权重值
priority-level|pq优先队列标识
＜priority_value＞|PQ调度优先级
＜policy-map name＞|policy-map的名字








### 缺省 


无 






### 使用说明 


1. 隧道PW上只能应用phb-based类型的策略。 






### 范例 


ZXROSNG(config)#class-map zteZXROSNG(config-cmap)#match out-vlan 800ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map pmap phb-basedZXROSNG(config- phb -based-policy)# class zteZXROSNG(config- phb -based-policy-class)# set 8021p 2ZXROSNG(config- phb -based-policy-class)# exitZXROSNG(config- phb -based-policy)#exitZXROSNG(config)# qos schedule interface gei-0/0/0/1 priority-level 3 service-policy pmap






### 相关命令 


无 




## qos-statistics clear 


qos-statistics clear 




### 命令功能 


在指定接口上清除QoS流统计数据 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 




qos-statistics clear 
  ＜interface-name 
＞ {input 
|output 
}







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口名称
input|接口方向，入向
output|接口方向，出向








### 缺省 


无 






### 使用说明 


无 






### 范例 


创建名称为zte的类映射：ZXROSNG(config)# qos-statistics clear gei-0/1/0/1 inputZXROSNG(config)#






### 相关命令 


无 




## qos-statistics switch 


qos-statistics switch 




### 命令功能 


流统计功能开关 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 




qos-statistics switch 
  {on 
|off 
} ＜IfName 
＞ {input 
|output 
}







### 命令参数解释 




参数|描述
---|---
on|开启流统计功能
off|关闭流统计功能
＜IfName＞|接口的名称
input|入方向
output|出方向








### 缺省 


无 






### 使用说明 


流统计功能默认是关闭的 






### 范例 


配置接口gei-0/9/0/11的流统计打开功能：ZXROSNG(config)#qos-statistics gei-0/9/0/11 output enable






### 相关命令 


service-policy <interface-name> { input | output } <policy-map-name> [{ overwrite | append }][statistical-share] qos schedule pw <pw-name> 




## queue-limit 


queue-limit 




### 命令功能 


配置队列深度 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 




queue-limit 
  {16 
|24 
|64 
|512 
|2000 
|8000 
|7 
}

no queue-limit 








### 命令参数解释 




参数|描述
---|---
16|队列深度值
24|队列深度值
64|队列深度值
512|队列深度值
2000|队列深度值
8000|队列深度值
7|队列深度值








### 缺省 


无 






### 使用说明 


在同一策略映射类下，queue-limit与WRED相冲突。queue-limit只能配置在叶子节点上。 






### 范例 


ZXROSNG(config)#class-map zte15 match-allZXROSNG(config-cmap)#match out-vlan 800ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy9ZXROSNG(config-pmap)#class zte15ZXROSNG(config-pmap-c)#queue-limit 2000






### 相关命令 


show policy-map [<policy-map-name>] 




## random-detect 


random-detect 




### 命令功能 


开启/关闭WRED功能，配置平均队列长度、基于IP Precedence的WRED参数。 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 



random-detect 
  {enable 
|weight 
 ＜weight-value 
＞|precedence 
 ＜precedence-value 
＞ ＜min-threshold 
＞ [{kbytes 
|mbytes 
|gbytes 
}] ＜max-threshold 
＞ [{kbytes 
|mbytes 
|gbytes 
}] ＜mark-probability 
＞|color 
 {green 
|yellow 
|red 
} ＜min-threshold 
＞ ＜max-threshold 
＞ ＜mark-probability 
＞}
no random-detect 
  {enable 
|weight 
|precedence 
 ＜precedence-value 
＞|color 
 {green 
|yellow 
|red 
}}
				






### 命令参数解释 




参数|描述
---|---
enable|开启WRED功能
weight|平均队列长度
＜weight-value＞|平均队列长度，范围：1-16
＜precedence-value＞|基于IP Precedence值，范围：0–7
＜min-threshold＞|WRED的下限，范围：1–1024000 $#34275348#$~$#34275349#$，单位：KB
kbytes|以KB为单位
mbytes|以MB为单位
gbytes|以GB为单位
＜max-threshold＞|WRED的上限，范围：1–1024000 $#34275350#$~$#34275351#$，单位：KB
kbytes|以KB为单位
mbytes|以MB为单位
gbytes|以GB为单位
＜mark-probability＞|WRED的丢弃概率，范围：1–100
color|丢弃优先级
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级
＜min-threshold＞|WRED的下限，范围：1–1024000 $#34275348#$~$#34275349#$，单位：KB
＜max-threshold＞|WRED的上限，范围：1–1024000 $#34275350#$~$#34275351#$，单位：KB
＜mark-probability＞|WRED的丢弃概率，范围：1–100








### 缺省 


无 






### 使用说明 


1. 只有开启WRED功能，即配置random-detect enable，且在有基于IP Precedence的WRED参数时，WRED才生效；当关闭WRED功能，即配置no random-detect enable，基于IP Precedence的WRED参数都不生效（添加还是删除可在show policy-map中查看是否存在random-detect enable动作）。2. 配置的<min-threshold>必须小于<max-threshold>。3. 默认的weight值为8。4. random-detect只能配置在策略的叶子结点，即在同一策略映射类下，random-detect 与service-policy相冲突。





### 范例 


配置策略映射为policy9、匹配外层VLAN值为800的流分类zte15，其动作指定使能WRED，平均队列长度默认，且基于IP Precedence值为1的丢弃下限为3000KB，丢弃上限为5000KB，丢弃概率为60；基于IP Precedence值为3的丢弃下限为6000KB，丢弃上限为9000KB，丢弃概率为50：ZXROSNG(config)# class-map zte15 match-allZXROSNG(config-cmap)#match out-vlan 800ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy9ZXROSNG(config-pmap)#class zte15ZXROSNG(config-pmap-c)#random-detect enableZXROSNG(config-pmap-c)#random-detect precedence 1 3000 5000 60ZXROSNG(config-pmap-c)#random-detect precedence 3 6000 9000 50





### 相关命令 


show policy-map 




## service-policy 


service-policy 




### 命令功能 


配置策略类的层次化策略。 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 




service-policy 
  ＜hpolicy-name 
＞

no service-policy 








### 命令参数解释 




参数|描述
---|---
＜hpolicy-name＞|待层次化的策略映射名








### 缺省 


无 






### 使用说明 


在同一策略映射类下，service-policy与set 8021p、set dscp、set precedence、set mpls-exp、random-detect相冲突。 






### 范例 


配置策略映射为policy9、匹配外层VLAN值为800的流分类zte15层次化policy3：ZXROSNG(config)#class-map zte15 match-allZXROSNG(config-cmap)#match out-vlan 800ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy9ZXROSNG(config-pmap)#class zte15ZXROSNG(config-pmap-c)#service-policy policy3





### 相关命令 


show policy-map  




## service-policy 


service-policy 




### 命令功能 


在接口上绑定HQoS策略。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



service-policy 
  ＜interface-name 
＞ {input 
|output 
} ＜policy-name 
＞ [overwrite 
] [statistical-share 
]
no service-policy 
  ＜interface-name 
＞ {input 
|output 
} [overwrite 
]
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称
input|接口入方向
output|接口出方向
＜policy-name＞|HQoS策略名称
overwrite|overwrite绑定模式
statistical-share|流分解标识








### 缺省 


无 






### 使用说明 


1. 先要利用policy-map配置HQoS策略名。2. HQoS绑定和car-set接口限速在同一接口的同一方向下互斥。3. 可选参数 overwrite | append 用于配置链路级的HQoS策略时选择。选择 append 时，绑定的policy-map只能是一层，并且只能match全局端口号(配置的class不允许超过已经配置的子接口范围，可以小于但不能大于，配置的动作可以是限速、WFQ或者PQ等)。选择 overwrite时，该链路接口上的HQoS规则以此policy-map为准，且不能在其子接口上配置HQoS策略，否则提示错误信息。如果要重新配置基于子接口的策略，需要显式删除该覆盖型的链路接口HQoS配置。





### 范例 


配置接口gei-0/9/0/11的HQoS策略policy8：ZXROSNG(config)#class-map zte15ZXROSNG(config-cmap)#match out-vlan 800ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy8ZXROSNG(config-pmap)#class zte15ZXROSNG(config-pmap-c)#set 8021p 2ZXROSNG(config-pmap-c)#exitZXROSNG(config-pmap)#exitZXROSNG(config)#service-policy gei-0/9/0/11 output policy8





### 相关命令 


show policy-map 




## set 


set 




### 命令功能 


配置策略类使用指定值标记报文的802.1p字段。 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 



set 
  {dscp 
 {＜dscp_value 
＞|inherit-from 
 {precedence 
|mpls-exp 
|8021p 
|dscp 
}}|mpls-exp 
 [{topmost 
|imposition 
|inner 
}] {＜mpls_exp_value 
＞|inherit-from 
 {precedence 
|mpls-exp 
|8021p 
|dscp 
}}|precedence 
 {＜precedence_value 
＞|inherit-from 
 {precedence 
|mpls-exp 
|8021p 
|dscp 
}}|8021p 
 {＜8021p_value 
＞|inherit-from 
 {precedence 
|mpls-exp 
|8021p 
|dscp 
}}|multi-mpls-exp 
 ＜multi-mpls-exp value 
＞ ＜multi-mpls-exp value 
＞}
no set 
  {dscp 
|mpls-exp 
|precedence 
|8021p 
|multi-mpls-exp 
}
				






### 命令参数解释 




参数|描述
---|---
dscp|IP DSCP
＜dscp_value＞|DSCP值
inherit-from|VLAN 802.1p根据dscp，precedence，8021p，mpls-exp设置
precedence|IP Precedence
mpls-exp|MPLS-EXP
8021p|VLAN 802.1p
dscp|IP DSCP
mpls-exp|MPLS-EXP
topmost|Set the MPLS-EXP value on topmost label
imposition|Set the MPLS-EXP value on all imposed labels
inner|内部
＜mpls_exp_value＞|MPLS-EXP值
inherit-from|VLAN 802.1p根据dscp，precedence，8021p，mpls-exp设置
precedence|IP Precedence
mpls-exp|MPLS-EXP
8021p|VLAN 802.1p
dscp|IP DSCP
precedence|IP Precedence
＜precedence_value＞|IP Precedence值
inherit-from|VLAN 802.1p根据dscp，precedence，8021p，mpls-exp设置
precedence|IP Precedence
mpls-exp|MPLS-EXP
8021p|VLAN 802.1p
dscp|IP DSCP
8021p|VLAN 802.1p
＜8021p_value＞|802.1p值
inherit-from|VLAN 802.1p根据dscp，precedence，8021p，mpls-exp设置
precedence|IP Precedence
mpls-exp|MPLS-EXP
8021p|VLAN 802.1p
dscp|IP DSCP
multi-mpls-exp|多标签EXP
＜multi-mpls-exp value＞|multi-mpls-exp值
＜multi-mpls-exp value＞|multi-mpls-exp值








### 缺省 


无 






### 使用说明 


set 8021p只能配置在策略的叶子结点，即在同一策略映射类下，set 8021p与service-policy相冲突。 






### 范例 


配置策略映射为policy3、匹配外层VLAN值为600的流分类zte4的802.1p字段值为2：ZXROSNG(config)#class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 600ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#set 8021p 2





### 相关命令 


show policy-map 




## shape 


shape 




### 命令功能 


配置策略类的流量整形。 






### 命令模式 


 QoS策略类配置模式  






### 命令默认权限级别 


15 






### 命令格式 




shape 
  {peak 
|average 
} {＜shape-rate-value 
＞|percentage 
 ＜percent 
＞} [bc 
 ＜bc-value 
＞ be 
 ＜be-value 
＞]

no shape 








### 命令参数解释 




参数|描述
---|---
peak|峰值
average|平均值
＜shape-rate-value＞|指定整形的平均或峰值速率，范围：1-4294967295，单位：kbps
＜percent＞|指定速率百分比值，范围：1~100
＜bc-value＞|指定正常突发速率，范围：1-4294967295，单位：kilo bytes
＜be-value＞|指定最大突发速率，范围：1-4294967295，单位：kilo bytes








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#class-map zte4 match-allZXROSNG(config-cmap)#match out-vlan 200ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy3ZXROSNG(config-pmap)#class zte4ZXROSNG(config-pmap-c)#shape peak 2000 bc 3000 be 4000






### 相关命令 


show policy-map [<policy-map-name>]show running-config




## show class-map 


show class-map 




### 命令功能 


显示H-QoS的所有流分类及其匹配项，或者指定名称的流分类及其匹配项。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show class-map 
  [＜class-name 
＞] 







### 命令参数解释 




参数|描述
---|---
＜class-name＞|class-map名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


显示配置的所有流分类：ZXROSNG(config)#show class-map class-map zte match-all         match dscp 2-6,10-15        class-map zte2 match-all        match precedence 0-2,4,6-7    match multi-cast            class-map zte3 match-all        match mpls-exp 1,3-5,7      class-map zte4 match-all        match in-vlan 1-20,40-50,100,200-250class-map zte5 match-all        match out-vlan 1-20,40-50,100,200-250class-map zte6 match-all        match in-8021p 0-3,5        class-map zte7 match-all        match out-8021p 1,4-5,7     class-map zte8 match-all        match qos-group 30            match vrf-name vrf1           match uni-cast                match mac-address 1111.1230.4567  match ipv4-access-list ztezxr10class-map zte9 match-all  match multi-cast  match ipv6-access-list chlw  class-map zte10 match-all  match interface gei-0/9/0/11     class-map zte11 match-all       match child           





### 相关命令 


无 




## show diffserv domain 


show diffserv domain 




### 命令功能 


显示DS域以及DS域下的简单流分类映射关系。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show diffserv domain 
  [＜domain-name 
＞] 







### 命令参数解释 




参数|描述
---|---
＜domain-name＞|用户自定义的DS域名称。








### 缺省 


无 






### 使用说明 


默认DS域的映射关系不能显示。 






### 范例 


# 显示DS域的配置信息。ZXROSNG(config)#show diffserv domaindiffserv domain ds18021p-inbound 0 phb be green8021p-inbound 1 phb af1 green8021p-inbound 2 phb af2 green8021p-inbound 3 phb af3 green8021p-inbound 4 phb af4 green8021p-inbound 5 phb ef green8021p-inbound 6 phb cs6 green<省略>






### 相关命令 


show running-config 




## show policy-map 


show policy-map 




### 命令功能 


显示H-QoS的所有策略映射以及策略类和相关的动作，或者显示指定策略映射名称的策略类和相关的动作，或者显示指定策略类的动作。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show policy-map 
  [＜policy-name 
＞ [class 
 ＜class-name 
＞]] 







### 命令参数解释 




参数|描述
---|---
＜policy-name＞|策略映射名称，长度1–31个字符
＜class-name＞|关联的类映射名称，长度1–31个字符








### 缺省 


无 






### 使用说明 


无 






### 范例 


显示H-QoS的策略映射policy1：ZXROSNG#show policy-map policy1policy-map policy1              class class-default             bandwidth percent 10





### 相关命令 


无 




## show qos diffserv-domain 


show qos diffserv-domain 




### 命令功能 


显示接口上配置的优先级信任配置。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show qos diffserv-domain 
  [{interface 
 ＜interface-name 
＞|pw 
 ＜pw-name 
＞}] 







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口名称
＜pw-name＞|伪线接口名称,格式为”pwX”, X为1-4294967295








### 缺省 


无 






### 使用说明 


无 






### 范例 


# 显示DS 域的配置信息。ZXROSNG(config)# show qos diffserv-domain interface gei-0/1/0/1.1






### 相关命令 


show running-config 




## show qos priority 


show qos priority 




### 命令功能 


显示接口上信任优先级 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show qos priority 
  [interface 
 ＜intf-name 
＞ ]







### 命令参数解释 




参数|描述
---|---
＜intf-name＞|接口名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


sho qos priority interface gei-0/1/0/1 






### 相关命令 


无 




## show qos schedule 


show qos schedule 




### 命令功能 


显示隧道或者是伪线上的配置。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show qos schedule 
  {interface 
 {＜WORD 
＞|all 
}|pw 
 {＜pw-name 
＞|all 
}} 







### 命令参数解释 




参数|描述
---|---
interface|接口标识
＜WORD＞|Tunnel的名称，字符串长度为1-31
all|接口上所有Tunnel
pw|伪线的标识
＜pw-name＞|伪线接口名称,格式为”pwX”, X为1-4294967295
all|接口上所有Tunnel








### 缺省 


无 






### 使用说明 


无 






### 范例 


#显示隧道上或者是伪线上的配置。ZXROSNG(config)# qos schedule pw pw-name1 pq 3 service-policy pmapnameZXROSNG(config)# qos schedule pw pw-name2 pq 3ZXROSNG(config)# qos schedule interface tunnel-name1  pq 3 service-policy pmapnameZXROSNG(config)# qos schedule interface tunnel-name2 pq 3ZXROSNG(config)# show qos schedule pw pw-name1qos schedule pw pw-name1 pq 3 service-policy pmapnameZXROSNG(config)# show qos schedule pw allqos schedule pw pw-name1 pq 3 service-policy pmapnameqos schedule pw pw-name2 pq 3ZXROSNG(config)#show qos schedule interface tunnel-name1qos schedule interface tunnel-name1  pq 3 service-policy pmapnameZXROSNG(config)# show qos schedule interface allqos schedule interface tunnel-name1  pq 3 service-policy pmapnameqos schedule interface tunnel-name2 pq 3ZXROSNG(config)#






### 相关命令 


show running-config 




## show qos-queue 


show qos-queue 




### 命令功能 


显示指定线卡的队列数资源 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show qos-queue 
  ＜BoardName 
＞ 







### 命令参数解释 




参数|描述
---|---
＜BoardName＞|指定的线卡








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#show qos-queue PFU-0/1 total resource : 51200        used  resource : 25600       






### 相关命令 


service-policy 




## show qos-statistics interface 


show qos-statistics interface 




### 命令功能 


显示接口的HQoS策略的流量统计结果。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show qos-statistics interface 
  [＜interface-name 
＞ {input 
|output 
}] 







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称
input|接口入方向
output|接口出方向








### 缺省 


无 






### 使用说明 


无 






### 范例 


显示接口的HQoS策略下流量统计：ZXROSNG(config)#show qos-statistics interface gei-0/1/0/1 inputInterface gei-0/1/0/1 current service-policy configuration:  service-policy input : 1  total flow : 1456 packets, 186368 bytes  transmit   : 910 packets, 116480 bytes, 100 pps, 102400 bps  total drop : 546 packets, 69888 bytes,  60 pps, 61440 bps  tail drop  : 364 packets, 46592 bytes  wred drop  : 182 packets, 23296 bytes  car drop   : 273 packets, 34944 bytes  urpf drop  : 182 packets, 23296 bytes  filter drop: 91 packets, 11648 bytes    class-map : 1      total flow : 1456 packets, 186368 bytes      transmit   : 910 packets, 116480 bytes, 100 pps, 102400 bps      total drop : 546 packets, 69888 bytes, 60 pps, 61440 bps      tail drop  : 364 packets, 46592 bytes      wred drop  : 182 packets, 23296 bytes      car drop   : 273 packets, 34944 bytes      urpf drop  : 182 packets, 23296 bytes      filter drop: 91 packets, 11648 bytes






### 相关命令 


无 




## show service-policy 


show service-policy 




### 命令功能 


显示接口的HQoS策略。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show service-policy 
  [＜interface-name 
＞] 







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


显示接口的HQoS策略：ZXROSNG(config)#show service-policyservice-policy gei-0/9/0/11 output policy8





### 相关命令 


无 




## show switch-fabric 


show switch-fabric 




### 命令功能 


显示交换网的HQoS策略绑定。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show switch-fabric 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


无 






### 范例 


显示交换网的HQoS策略绑定：ZXROSNG(config)#show switch-fabricswitch-fabric service-policy policy8





### 相关命令 


无 




## show traffic-shape 


show traffic-shape 




### 命令功能 


显示接口上配置的DS域。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show traffic-shape 
  [＜intfName 
＞] 







### 命令参数解释 




参数|描述
---|---
＜intfName＞|接口名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


# 显示DS 域的配置信息。ZXROSNG(config)# show qos priority interface gei-0/1/0/1.1






### 相关命令 


show running-config 




## switch-fabric 


switch-fabric 




### 命令功能 


在交换网上绑定HQoS策略 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



switch-fabric 
 service-policy 
 ＜policy-name 
＞ shelf 
 ＜<0-7> 
＞ slot 
 ＜<0-17> 
＞ {subslot 
 {group1 
 multi-cast 
|group2 
 multi-cast 
|＜<0-3> 
＞ {uni-cast 
|port 
 ＜<1-48> 
＞ {switch-port 
|uni-cast 
}}}|uni-cast 
|multi-cast 
}
no switch-fabric 
 shelf 
 ＜<0-7> 
＞ slot 
 ＜<0-17> 
＞ {subslot 
 {group1 
 multi-cast 
|group2 
 multi-cast 
|＜<0-3> 
＞ {uni-cast 
|port 
 ＜<1-48> 
＞ {switch-port 
|uni-cast 
}}}|uni-cast 
|multi-cast 
}
				






### 命令参数解释 




参数|描述
---|---
＜policy-name＞|H-QoS策略名
＜<0-7>＞|机架号0-7
＜<0-17>＞|槽位号0-17
group1|Parameter template for subslot 0 and 1
multi-cast|组播，值为2
group2|Parameter template for subslot 2 and 3
multi-cast|组播，值为2
＜<0-3>＞|子槽位号0-3
uni-cast|单播，值为1
＜<1-48>＞|端口号
switch-port|交互接口，值为3
uni-cast|单播，值为1
uni-cast|单播，值为1
multi-cast|组播，值为2








### 缺省 


无 






### 使用说明 


先要利用policy-map配置HQoS策略名 






### 范例 


ZXROSNG(config)#class-map zte15 match-allZXROSNG(config-cmap)#match out-vlan 800ZXROSNG(config-cmap)#exitZXROSNG(config)#policy-map policy8ZXROSNG(config-pmap)#class zte15 ZXROSNG(config-pmap-c)#set 8021p 2ZXROSNG(config-pmap-c)#exitZXROSNG(config-pmap)#exitZXROSNG(config)#switch-fabric service-policy policy8






### 相关命令 


show policy-map [<policy-map-name>] 




## traffic-shape 


traffic-shape 




### 命令功能 


配置端口流整形 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



traffic-shape 
  ＜interface-name 
＞ rate 
 ＜rate 
＞ [＜burstSize 
＞] [＜excBurstSize 
＞] [network-header-length 
 ＜network-header-length 
＞]
no traffic-shape 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口名称
＜rate＞|速率。8-10000000  Kilo bits per second
＜burstSize＞|突发流量大小。2-250000000 Kilo bytes
＜excBurstSize＞|额外突发流量大小。2-250000000 Kilo bytes
＜network-header-length＞|报文封装长度精度补偿值，范围-63-63








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#traffic-shape gei-0/1/0/1 rate 100 200 300ZXROSNG(config)#show traffic-shape traffic-shape gei-0/1/0/1 100 200 300ZXROSNG(config)#traffic-shape gei-0/1/0/1 rate 200ZXROSNG(config)#show traffic-shape traffic-shape gei-0/1/0/1 200





### 相关命令 


show traffic-shape ＜interface-name＞ 




# QPPB配置命令 
## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
} {＜interface-name 
＞}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
} {＜interface-name 
＞}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值
＜interface-name＞|接口名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)# qos-policy destination qos-id gei-0/9/0/11开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)# qos-policy destination qos-id gei-0/9/0/11






### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 以太接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 posgroup接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 pos子接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 通道化cpos_e1接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 千兆以太接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 pos接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 multilink接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 通道化ce1接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 smartgroup子接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 以太子接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 smartgroup接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## qos-policy 


qos-policy 




### 命令功能 


在接口上开启接口QPPB功能。 






### 命令模式 


 10G以太接口模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
no qos-policy 
  [ipv6 
] {source 
|destination 
} {ip-precedence 
|qos-id 
}
				






### 命令参数解释 




参数|描述
---|---
ipv6|IPv6协议类型
source|表示用源IP查路由表
destination|表示用目的IP查路由表
ip-precedence|表示查路由取ip-precedence的值
qos-id|表示查路由取qos-id的值








### 缺省 


无 






### 使用说明 


无 






### 范例 


开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id开启接口gei-0/9/0/11的QPPB功能ZXROSNG(config)#interface gei-0/9/0/11ZXROSNG(config-if)# qos-policy destination qos-id





### 相关命令 


show qppb-groups 




## show qppb-groups 


show qppb-groups 




### 命令功能 


显示QPPB配置信息。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show qppb-groups 
  [{[by-direction 
 {source 
|destination 
}],[by-option 
 {ip-precedence 
|qos-id 
}],[by-interface 
 ＜interface-name 
＞]}] 







### 命令参数解释 




参数|描述
---|---
by-direction|根据方向显示QPPB配置
source|用源IP查路由表的QPPB配置进行显示
destination|用目地IP查路由表的QPPB配置进行显示
by-option|根据选项显示QPPB配置
ip-precedence|查路由取ip-precedence的值的QPPB配置进行显示
qos-id|查路由取qos-id的值的QPPB配置进行显示
by-interface|根据接口名显示QPPB配置
＜interface-name＞|接口名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config)#show qppb-groups Direction         Option            Interface name-----------------------------------------------------------------source            ip-precedence     gei-0/1/0/1source            qos-id            gei-0/1/0/1ZXROSNG(config)#show qppb-groups Direction         Option            Interface name-----------------------------------------------------------------source            ip-precedence     gei-0/1/0/1source            qos-id            gei-0/1/0/1





### 相关命令 


qos-policy 




# 优先级继承配置命令 
## mls-qos-mode 


mls-qos-mode 




### 命令功能 


配置接口的优先级继承模式。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



mls-qos-mode 
  ＜interface-name 
＞ {uniform 
|pipe 
 [＜service_class 
＞ {green 
|yellow 
|red 
}]|short-pipe 
 [＜service_class 
＞ {green 
|yellow 
|red 
}]}
no mls-qos-mode 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称
uniform|uniform继承模式
pipe|pipe继承模式
＜service_class＞|本地调度优先级
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级
short-pipe|short-pipe继承模式
＜service_class＞|本地调度优先级
green|本地最高丢弃优先级
yellow|本地中等丢弃优先级
red|本地最高丢弃优先级








### 缺省 


无 






### 使用说明 


无 






### 范例 


配置接口gei-0/9/0/11的优先级继承模式为pipe：ZXROSNG(config)#mls-qos-mode gei-0/9/0/11 pipe






### 相关命令 


show mls-qos-mode 




## qos-dot1p 


qos-dot1p 




### 命令功能 


配置接口的802.1p继承。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



qos-dot1p 
  ＜interface-name 
＞ [{cvlan-out 
|cvlan-in 
}]
no qos-dot1p 
  ＜interface-name 
＞ [{cvlan-out 
|cvlan-in 
}]
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称
cvlan-out|从出方向的802.1p值继承到内层VLAN
cvlan-in|从入方向的内层VLAN继承802.1p值








### 缺省 


无 






### 使用说明 


只有子接口才能配置802.1p继承。 






### 范例 


配置接口gei-0/9/0/11.1的802.1p继承：ZXROSNG(config)#qos-dot1p gei-0/9/0/11.1






### 相关命令 


show qos-dot1p 




## show mls-qos-mode 


show mls-qos-mode 




### 命令功能 


显示接口的优先级继承模式。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show mls-qos-mode 
  [＜interface-name 
＞] 







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


显示配置的配置接口的优先级继承：ZXROSNG(config)#show mls-qos-modemls-qos-mode gei-0/9/0/11 pipe





### 相关命令 


无 




## show qos-dot1p 


show qos-dot1p 




### 命令功能 


显示接口的802.1p继承。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show qos-dot1p 
  [＜interface-name 
＞] 







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称








### 缺省 


无 






### 使用说明 


无 






### 范例 


显示配置的配置接口的802.1p继承：ZXROSNG(config)#show qos-dot1pqos-dot1p gei-0/9/0/11.1 





### 相关命令 


qos-dot1p 




## show ttl-qos-mode 


show ttl-qos-mode 




### 命令功能 


显示接口的TTL复制属性模式。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show ttl-qos-mode 
  [{＜interface-name 
＞|global 
}] 







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称
global|全局








### 缺省 


无 






### 使用说明 


无 






### 范例 


显示配置的配置接口的优先级继承：ZXROSNG(config)#show ttl-qos-modettl-qos-mode gei-0/1/0/1 pipe





### 相关命令 


ttl-qos-mode 




## ttl-qos-mode 


ttl-qos-mode 




### 命令功能 


配置接口的TTL复制属性。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ttl-qos-mode 
  ＜interface-name 
＞ {uniform 
|pipe 
}
no ttl-qos-mode 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口的名称
uniform|uniform继承模式
pipe|pipe继承模式








### 缺省 


无 






### 使用说明 


无 






### 范例 


配置接口gei-0/1/0/1的TTL继承：ZXROSNG(config)#ttl-qos-mode gei-0/1/0/1 pipe配置接口gei-0/1/0/1的TTL继承：ZXROSNG(config)#ttl-qos-mode gei-0/1/0/1 pipe






### 相关命令 


show ttl-qos-mode 




