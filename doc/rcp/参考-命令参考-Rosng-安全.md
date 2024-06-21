# Diameter配置命令 
## algorithm 

algorithm 
命令功能 : 
设置同一个组中选择链路的规则。master-slave方式优先选择主用链路；round-robin方式为负荷分担方式，主用链路不起作用 
命令模式 : 
 diameter组模式  
命令默认权限级别 : 
15 
命令格式 : 
algorithm 
  {master-slave 
|round-robin 
}
命令参数解释 : 
参数|描述
---|---
master-slave|主从方式。缺省方式。
round-robin|轮流通过组中的链路发送报文
缺省 : 
缺省值为：master-slave 
使用说明 : 
设置同一个组中选择链路的规则。只对open状态的链路进行选择，master-slave方式优先选择master链路，round-robin方式则轮流选择所有链路。 
范例 : 
ZXROSNG(config)#diameter-group 1ZXROSNG(config-diametergrp-1)#algorithm round-robin
相关命令 : 
linkshow diameter-group-config allshow running-config diameter 
## attr 

attr 
命令功能 : 
配置diameter报文属性值。 
命令模式 : 
 diameter-ping模式  
命令默认权限级别 : 
15 
命令格式 : 
attr 
  {aar 
|acr 
|ccr 
|der 
} [vendor 
 ＜vendor-id 
＞] attr-id 
 ＜attribute-id 
＞ type 
 {int 
 ＜int-value 
＞|string 
 ＜string 
＞|ipv4 
 ＜ipv4 address 
＞|ipv6 
 ＜ipv6 address 
＞}
no attr 
  {aar 
|acr 
|ccr 
|der 
} [vendor 
 ＜vendor-id 
＞] attr-id 
 ＜attribute-id 
＞
				
命令参数解释 : 
参数|描述
---|---
aar|diameter报文类型
acr|diameter报文类型
ccr|diameter报文类型
der|diameter报文类型
＜vendor-id＞|厂商属性编号，缺省为0，取值0~65535
＜attribute-id＞|属性编号，取值为1-4294967295
int|整数类型
＜int-value＞|<0-4294967295>
string|字符串类型
＜string＞|<1-128>
ipv4|IPv4类型
＜ipv4 address＞|A.B.C.D  IPv4 address
ipv6|IPv4类型
＜ipv6 address＞|X:X::X:X  IPv6 address
缺省 : 
无 
使用说明 : 
配置diameter报文属性值。 
范例 : 
ZXROSNG(config-diameter-ping)#attr aar attr-id 1113 type string Ilovethisgame ZXROSNG(config-diameter-ping)#
相关命令 : 
diameter-pingshow diameter-pingshow running-config diameter 
## deadtime 

deadtime 
命令功能 : 
设置链路重新链接的时间间隔。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
deadtime 
  ＜deadtime 
＞
命令参数解释 : 
参数|描述
---|---
＜deadtime＞|链路重新链接的时间间隔，单位分钟，范围10-255分钟，默认10分钟；
缺省 : 
默认10分钟 
使用说明 : 
该时间间隔单位为分钟，由于受到tcp连接的限制，通常不能小于10分钟。 
范例 : 
ZXROSNG(config)#diameter-link 1ZXROSNG(config-diameterlink-1)#deadtime 15ZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter 
## debug diameter all 

debug diameter all 
命令功能 : 
打开DIAMETER所有的debug显示。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug diameter all 
 
no debug diameter all 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开DIAMETER所有的debug显示。当配合diameter-debug-set使用时，只显示符合条件的debug信息。 
范例 : 
打开DIAMETER所有的debug显示：ZXROSNG#debug diameter allZXROSNG#diameter-debug-set user abc
相关命令 : 
diameter-debug-setshow debug diameter
## debug diameter data 

debug diameter data 
命令功能 : 
对diameter进行debug跟踪。可以配合diameter-debug-set使用 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug diameter data 
 
no debug diameter data 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
对diameter data进行debug跟踪。可以配合diameter-debug-set使用 
范例 : 
显示用户名为abc的所有data的debug信息ZXROSNG#debug diameter dataZXROSNG#ZXROSNG#diameter-debug-set user abc
相关命令 : 
diameter-debug-setshow debug diameter
## debug diameter error 

debug diameter error 
命令功能 : 
对diameter进行debug跟踪。可以配合diameter-debug-set使用 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug diameter error 
 
no debug diameter error 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
对diameter error进行debug跟踪。可以配合diameter-debug-set使用 
范例 : 
ZXROSNG#debug diameter errorZXROSNG#diameter-debug-set user abc
相关命令 : 
diameter-debug-setshow debug diameter
## debug diameter event 

debug diameter event 
命令功能 : 
对diameter事件进行debug跟踪。可以配合diameter-debug-set使用 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug diameter event 
 
no debug diameter event 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
对diameter event进行debug跟踪，可以配合diameter-debug-set使用 
范例 : 
打开DIAMETER的event信息显示，只显示用户名为abc的debug信息：ZXROSNG#debug diameter eventZXROSNG#diameter-debug-set user abc
相关命令 : 
diameter-debug-setshow debug diameter
## debug diameter exception 

debug diameter exception 
命令功能 : 
对diameter进行debug跟踪。可以配合diameter-debug-set使用 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug diameter exception 
 
no debug diameter exception 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
对diameter exception进行debug跟踪。可以配合diameter-debug-set使用 
范例 : 
对用户名为abc的exception信息进行debug跟踪：ZXROSNG#debug diameter exceptionZXROSNG#diameter-debug-set user abc
相关命令 : 
diameter-debug-setshow debug diameter
## debug diameter packet 

debug diameter packet 
命令功能 : 
对diameter进行debug跟踪。可以配合diameter-debug-set使用。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug diameter packet 
 
no debug diameter packet 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
对diameter 报文进行debug跟踪。可以配合diameter-debug-set使用。 
范例 : 
ZXROSNG#debug diameter packet ZXROSNG#diameter-debug-set user abc
相关命令 : 
diameter-debug-setshow debug diameter
## dest-host 

dest-host 
命令功能 : 
配置DIAMETER链路的dest-host参数。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
dest-host 
  ＜destination-host-name 
＞
no dest-host 
命令参数解释 : 
参数|描述
---|---
＜destination-host-name＞|对端主机名
缺省 : 
无 
使用说明 : 
配置DIAMETER链路的dest-host参数。 
范例 : 
ZXROSNG(config)#diameter link 1ZXROSNG(config-diameterlink-1)# dest-host chinanet@dim.com.cnZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## dest-port 

dest-port 
命令功能 : 
配置diameter 链路对等端端口。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
dest-port 
  ＜peer-port 
＞
no dest-port 
命令参数解释 : 
参数|描述
---|---
＜peer-port＞|对等端端口号
缺省 : 
缺省端口号为3868。 
使用说明 : 
配置diameter对等端端口号。 
范例 : 
ZXROSNG(config)#diameter-link 1ZXROSNG(config-diameterlink-1)#dest-port 6300ZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## dest-realm 

dest-realm 
命令功能 : 
配置DIAMETER链路的dest-realm参数。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
dest-realm 
  ＜destination-realm 
＞
no dest-realm 
命令参数解释 : 
参数|描述
---|---
＜destination-realm＞|对等端域名
缺省 : 
无 
使用说明 : 
配置DIAMETER链路的dest-realm参数。 
范例 : 
ZXROSNG(config-diameterlink-1)#dest-realm zteZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## diameter-capability accounting 

diameter-capability accounting 
命令功能 : 
配置DIAMETER的缺省全局local- capability。用于填写cer报文中的相应能力属性值，仅当对端对cer报文有特殊要求时使用 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-capability accounting 
  ＜No. 
＞ ＜value 
＞
no diameter-capability accounting 
  ＜No. 
＞
				
命令参数解释 : 
参数|描述
---|---
＜No.＞|计费组组号；
＜value＞|计费能力值；
缺省 : 
无 
使用说明 : 
配置diameter能力。用于填写cer报文中的相应能力属性值，仅当对端对cer报文有特殊要求时使用 
范例 : 
ZXROSNG(config)#diameter-capability accounting 1 2000 ZXROSNG(config)#
相关命令 : 
show running-config diameter 
## diameter-capability authentication 

diameter-capability authentication 
命令功能 : 
配置DIAMETER的缺省全局local- capability。用于在CER报文中进行能力交换使用，在对接没有明确要求的情况下不需要配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-capability authentication 
  ＜No. 
＞ ＜value 
＞
no diameter-capability authentication 
  ＜No. 
＞
				
命令参数解释 : 
参数|描述
---|---
＜No.＞|认证组组号；
＜value＞|认证能力值；
缺省 : 
无 
使用说明 : 
配置diameter能力。仅用于对端对能力交换有特殊需求的情况。 
范例 : 
ZXROSNG(config)#diameter-capability authentication 1 2000ZXROSNG(config)#
相关命令 : 
diameter-capability accountingdiameter-capability securitydiameter-capability vendorshow running-config diameter 
## diameter-capability security 

diameter-capability security 
命令功能 : 
配置DIAMETER的缺省全局local- capability。用于填写cer报文中的相应能力属性值，仅当对端对cer报文有特殊要求时使用 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-capability security 
  ＜No. 
＞ ＜value 
＞
no diameter-capability security 
  ＜No. 
＞
				
命令参数解释 : 
参数|描述
---|---
＜No.＞|安全组组号；
＜value＞|安全能力值；
缺省 : 
无 
使用说明 : 
配置diameter能力。用于填写cer报文中的相应能力属性值，仅当对端对cer报文有特殊要求时使用 
范例 : 
ZXROSNG(config)#diameter-capability security 1 2000ZXROSNG(config)#
相关命令 : 
diameter-capability  accounting     diameter-capability  authentication    diameter-capability  vendor show running-config diameter
## diameter-capability vendor 

diameter-capability vendor 
命令功能 : 
配置DIAMETER的缺省全局local- capability。用于填写cer报文中的相应能力属性值，仅当对端对cer报文有特殊要求时使用 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-capability vendor 
  ＜No. 
＞ ＜value 
＞
no diameter-capability vendor 
  ＜No. 
＞
				
命令参数解释 : 
参数|描述
---|---
＜No.＞|厂商属性组号；
＜value＞|厂商属性号；
缺省 : 
无 
使用说明 : 
配置diameter能力。用于填写cer报文中的相应能力属性值，仅当对端对cer报文有特殊要求时使用 
范例 : 
ZXROSNG(config)#diameter-capability vendor 1 2000ZXROSNG(config)#
相关命令 : 
diameter-capability  accounting     diameter-capability  authentication diameter-capability  security       show running-config diameter
## diameter-debug-set group 

diameter-debug-set group 
命令功能 : 
设置diameter相关Debug命令的过滤条件。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-debug-set group 
  ＜group-name 
＞
no diameter-debug-set group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|Diameter组号，范围1-10；
缺省 : 
无 
使用说明 : 
设置diameter相关Debug命令的过滤条件，可以选择链路组、链路和用户名等。 
范例 : 
ZXROSNG#diameter-debug-set group 1DIAMETER group has been turned onZXROSNG#
相关命令 : 
debug diametershow diameter-debug-set
## diameter-debug-set link 

diameter-debug-set link 
命令功能 : 
设置diameter相关Debug命令的过滤条件。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-debug-set link 
  ＜link No. 
＞
no diameter-debug-set link 
命令参数解释 : 
参数|描述
---|---
＜link No.＞|diameter链路号，取值1~128
缺省 : 
无 
使用说明 : 
设置diameter相关Debug命令的过滤条件。设置该命令后只显示制定链路的debug信息。 
范例 : 
ZXROSNG#diameter-debug-set link 1DIAMETER link has been turned onZXROSNG#
相关命令 : 
show diameter-debug-set 
## diameter-debug-set user 

diameter-debug-set user 
命令功能 : 
设置diameter相关Debug命令的过滤条件，只有指定用户名的报文相关信息会被debug显示出来。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-debug-set user 
  ＜user-name 
＞
no diameter-debug-set user 
命令参数解释 : 
参数|描述
---|---
＜user-name＞|用户名
缺省 : 
无 
使用说明 : 
设置diameter相关Debug命令的过滤条件，只有制定用户名的debug信息会被显示出来。 
范例 : 
ZXROSNG#diameter-debug-set user zte123DIAMETER user has been turned onZXROSNG#
相关命令 : 
debug diametershow diameter-debug-set
## diameter-group 

diameter-group 
命令功能 : 
进入diameter-group配置模式 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-group 
  ＜group-name 
＞
no diameter-group 
  ＜group-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-name＞|Diameter组名，(1-32 characters)
缺省 : 
无 
使用说明 : 
执行该命令将进入diameter-group配置模式。 
范例 : 
ZXROSNG(config)#diameter-group 1ZXROSNG(config-diametergrp-1)#exitZXROSNG(config)#
相关命令 : 
show diameter-group-config allshow running-config diameter 
## diameter-link 

diameter-link 
命令功能 : 
进入diameter-link配置模式 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-link 
  ＜link No. 
＞
no diameter-link 
  ＜link No. 
＞
				
命令参数解释 : 
参数|描述
---|---
＜link No.＞|Diameter链路号，范围1-128；
缺省 : 
无 
使用说明 : 
执行该命令将进入diameter-link配置模式。 
范例 : 
ZXROSNG(config)#diameter-link 1ZXROSNG(config-diameter-link-1)#exitZXROSNG(config)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter 
## diameter-local-host 

diameter-local-host 
命令功能 : 
配置DIAMETER的缺省全局local-host，用于填写diameter报文中对应属性值。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-local-host 
  ＜host-name 
＞
no diameter-local-host 
命令参数解释 : 
参数|描述
---|---
＜host-name＞|本端主机名
缺省 : 
无 
使用说明 : 
用于填写diameter报文中相应属性值，当diameter-link模式下未配置local-host时，则使用全局local-host。 
范例 : 
ZXROSNG(config)#diameter-local-host myhostZXROSNG(config)#
相关命令 : 
local-hostshow running-config diameter 
## diameter-local-realm 

diameter-local-realm 
命令功能 : 
配置DIAMETER的缺省全局local-realm。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-local-realm 
  ＜realm-name 
＞
no diameter-local-realm 
命令参数解释 : 
参数|描述
---|---
＜realm-name＞|本端域名
缺省 : 
无 
使用说明 : 
当diameter-link模式下未配置local-realm时，则使用全局local-realm。 
范例 : 
ZXROSNG(config)#diameter-local-realm myrealm.comZXROSNG(config)#
相关命令 : 
show running-config diameter 
## diameter-ping 

diameter-ping 
命令功能 : 
根据配置发送diameter报文。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-ping 
 link 
 ＜link No. 
＞ {aar 
|acr 
|ccr 
|der 
} [{[user 
 ＜user-name 
＞ password 
 ＜password 
＞],[times 
 ＜ping-times 
＞]}]
命令参数解释 : 
参数|描述
---|---
＜link No.＞|显示单条diameter链路信息（取值范围：1~128）
aar|Diameter报文类型
acr|Diameter报文类型
ccr|Diameter报文类型
der|Diameter报文类型
＜user-name＞|用户名
＜password＞|用户密码，取值为1～64字节字符串
＜ping-times＞|发送次数，取值1～10次。缺省1次
缺省 : 
times 缺省1次 
使用说明 : 
根据配置发送diameter报文。当返回“！”时，表示ping成功；当返回“.”时，表示超时无响应。
范例 : 
ZXROSNG#diameter-ping link 1 AAR user admin password 123 ！
相关命令 : 
diameter-ping-set  
## diameter-ping-set 

diameter-ping-set 
命令功能 : 
进入diameter-ping-set配置模式，用于在diameter-ping发送报文时，在报文中增加制定的属性值 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-ping-set 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
执行该命令将进入diameter-ping-set配置模式。 
范例 : 
ZXROSNG(config)#diameter-ping-setZXROSNG(config-diameter-ping)#
相关命令 : 
attrdiameter-pingshow diameter-pingshow running-config diameter 
## diameter-statistics 

diameter-statistics 
命令功能 : 
Diameter统计功能。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
diameter-statistics 
  {disable 
|enable 
}
命令参数解释 : 
参数|描述
---|---
disable|关闭diameter统计功能。当关闭时，保留统计数据。
enable|打开diameter统计功能。当打开时，清空历史统计数据。
缺省 : 
无 
使用说明 : 
当打开统计功能时，同时清空原统计数据。 
范例 : 
ZXROSNG#diameter-statistics enableZXROSNG#
相关命令 : 
show diameter-statistics 
## disable 

disable 
命令功能 : 
diameter链路链接去活命令。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
disable 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
去活diameter链路。 
范例 : 
ZXROSNG(config)#diameter-link 1ZXROSNG(config-diameter-link-1)#disableZXROSNG(config-diameter-link-1)#
相关命令 : 
enableshow diameter-link-config allshow diameter-link-status allshow running-config diameter 
## enable 

enable 
命令功能 : 
diameter链路链接激活命令。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
enable 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
激活diameter链路。 
范例 : 
ZXROSNG(config)#diameter-link 1ZXROSNG(config-diameter-link-1)#enableZXROSNG(config-diameter-link-1)#
相关命令 : 
disableshow diameter-link-config allshow diameter-link-status allshow running-config diameter 
## ip vrf 

ip vrf 
命令功能 : 
Vrf name配置。当diameter的链路地址是在vrf网络中时，需要配置该命令，否则不需要配置。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
ip vrf 
  {mng 
|＜vrf-name 
＞}
no ip vrf 
命令参数解释 : 
参数|描述
---|---
mng|Vrf  name为mng
＜vrf-name＞|Vrf-name长度为1~32（与配置模式下的ip vrf命令关联）
缺省 : 
无 
使用说明 : 
diameter链路vrf  name配置 
范例 : 
ZXROSNG(config)# diameter-link 1ZXROSNG(config-diameterlink-1)#ip vrf mngZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow running-config diameter peer-ipv4-addrpeer-ipv6-addr
## ip-type 

ip-type 
命令功能 : 
diameter链路ip类型配置。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
ip-type 
  {ipv4 
|ipv6 
}
命令参数解释 : 
参数|描述
---|---
ipv4|该链路为IPv4类型，缺省类型
ipv6|该链路为IPv6类型
缺省 : 
IPv4。 
使用说明 : 
diameter链路ip类型配置 
范例 : 
ZXROSNG(config)# diameter-link 1ZXROSNG(config-diameterlink-1)#ip-type ipv6ZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## link 

link 
命令功能 : 
将diameter链路添加到diameter组中。并可以选择其中一条为主用链路。当链路选择策略为master-slave时，当主用链路可用时，优先使用主用链路；当链路选择策略为round-robin时，主用链路选项不起作用。 
命令模式 : 
 diameter组模式  
命令默认权限级别 : 
15 
命令格式 : 
link 
  ＜link No. 
＞ [master 
]
no link 
  ＜link No. 
＞
				
命令参数解释 : 
参数|描述
---|---
＜link No.＞|链路编号，范围：1-128，每组最多4个
master|主用服务器,在一个组中只能有一个主用服务器
缺省 : 
无 
使用说明 : 
将diameter链路添加到diameter组中。每组最多4条链路，其中只能有一条为主用链路。主用链路的配置只有在链路选择策略为master-slave时才生效。 
范例 : 
ZXROSNG(config)#diameter-group 1ZXROSNG(config-diametergrp-1)#link 128 masterZXROSNG(config-diametergrp-1)#
相关命令 : 
algorithm master-slaveshow diameter-link-status alldiameter-groupshow diameter-group-config allshow running-config diameter 
## link-type 

link-type 
命令功能 : 
diameter链路连接类型配置。当类型为tcp时，只有第一个配置的对等端地址生效；当类型为sctp时，最多可以存在四个对等端地址。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
link-type 
  {tcp 
|sctp 
}
命令参数解释 : 
参数|描述
---|---
tcp|该链路为tcp，缺省类型
sctp|该链路为sctp类型
缺省 : 
tcp 
使用说明 : 
diameter链路连接类型配置。可选值为tcp和sctp，tcp只支持一个对等端地址，sctp支持四个对等端地址。 
范例 : 
ZXROSNG(config)# diameter-link 1ZXROSNG(config-diameterlink-1)#link-type sctpZXROSNG(config-diameterlink-1)#
相关命令 : 
peer-ipv4-addrpeer-ipv6-addrshow diameter-link-config allshow diameter-link-status allshow running-config diameter
## local-host 

local-host 
命令功能 : 
配置DIAMETER链路的local-host参数，如果在链路中未配置该参数，则取全局额度diameter-local-host参数。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
local-host 
  ＜local-host-name 
＞
no local-host 
命令参数解释 : 
参数|描述
---|---
＜local-host-name＞|本端主机名
缺省 : 
无 
使用说明 : 
配置DIAMETER链路的local-host参数，如果在链路中未配置该参数，则取全局额度diameter-local-host参数。 
范例 : 
ZXROSNG(config)#diameter link 1ZXROSNG(config-diameterlink-1)# local-host zxr10ZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## local-port 

local-port 
命令功能 : 
配置diameter 链路本地端口。正常情况下建议不配置该命令，这样可以由系统自动分配。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
local-port 
  ＜local-port 
＞
no local-port 
命令参数解释 : 
参数|描述
---|---
＜local-port＞|本端端口号
缺省 : 
自动分配，通常不配，除非特殊需要。 
使用说明 : 
配置diameter本端端口号。 
范例 : 
ZXROSNG(config)#diameter-link 1ZXROSNG(config-diameterlink-1)#local-port 6300ZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## local-realm 

local-realm 
命令功能 : 
配置DIAMETER链路的local-realm参数，如果在链路中未配置该参数，则取全局额度diameter-local-realm参数。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
local-realm 
  ＜local-realm 
＞
no local-realm 
命令参数解释 : 
参数|描述
---|---
＜local-realm＞|本端域名
缺省 : 
无 
使用说明 : 
配置DIAMETER链路的local-realm参数，如果在链路中未配置该参数，则取全局额度diameter-local-realm参数。 
范例 : 
ZXROSNG(config-diameterlink-1)# local-realm zteZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## peer-ipv4-addr 

peer-ipv4-addr 
命令功能 : 
配置diameter 链路对等端IPv4地址。注意：由于SCTP支持对应多个对端IP地址，因此当链路类型为SCTP时，允许配置多个IP地址。（SCTP模块目前最多支持4个地址）。
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
peer-ipv4-addr 
  ＜ipv4 address 
＞
no peer-ipv4-addr 
  ＜ipv4 address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipv4 address＞|Diameter对等端IPv4地址
缺省 : 
无 
使用说明 : 
配置diameter 链路对等端IPv4地址。即对端的diameter服务器地址。 
范例 : 
ZXROSNG(config)#diameter-link 1ZXROSNG(config-diameterlink-1)#peer-ipv4-addr 192.168.70.1ZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter 
## peer-ipv6-addr 

peer-ipv6-addr 
命令功能 : 
配置diameter 链路对等端IPv6地址。注意：由于SCTP支持对应多个对端IP地址，因此当链路类型为SCTP时，允许配置多个IP地址。（SCTP模块目前最多支持4个地址）。
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
peer-ipv6-addr 
  ＜ipv6 address 
＞
no peer-ipv6-addr 
  ＜ipv6 address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipv6 address＞|Diameter对等端IPv6地址
缺省 : 
无 
使用说明 : 
配置diameter 链路对等端IPv6地址。及对端diameter服务器的IPv6地址。 
范例 : 
ZXROSNG(config)#diameter-link 1ZXROSNG(config-diameterlink-1)#peer-ipv6-addr 1::1:1ZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter 
## retry-interval 

retry-interval 
命令功能 : 
设置报文重传间隔。缺省为3秒。 
命令模式 : 
 diameter组模式  
命令默认权限级别 : 
15 
命令格式 : 
retry-interval 
  ＜retry-interval 
＞
命令参数解释 : 
参数|描述
---|---
＜retry-interval＞|报文重传间隔时间
缺省 : 
缺省报文重传间隔时间为3秒。 
使用说明 : 
设置报文重传间隔。缺省为3秒。 
范例 : 
ZXROSNG(config-diametergrp-1)# retry-interval 10ZXROSNG(config-diametergrp-1)#
相关命令 : 
show diameter-group-config allshow running-config diameter 
## retry-times 

retry-times 
命令功能 : 
在单条链路上报文超时重发次数。缺省为3。 
命令模式 : 
 diameter组模式  
命令默认权限级别 : 
15 
命令格式 : 
retry-times 
  ＜retry-times 
＞
命令参数解释 : 
参数|描述
---|---
＜retry-times＞|单条链路上报文重发次数，范围1-255，默认值：3；
缺省 : 
默认值：3； 
使用说明 : 
在单条链路上报文超时重发次数。缺省为3。 
范例 : 
ZXROSNG(config-diametergrp-1)# retry-times 10ZXROSNG(config-diametergrp-1)#
相关命令 : 
show diameter-group-config allshow running-config diameter 
## send-cer-message 

send-cer-message 
命令功能 : 
diameter链路发送能力交换请求（CER）报文命令。默认发送CER消息，这也是diameter基础协议的要求。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
send-cer-message 
  {off 
|on 
}
命令参数解释 : 
参数|描述
---|---
off|不发送CER报文
on|发送CER报文。缺省发送。
缺省 : 
默认发送CER消息。 
使用说明 : 
diameter链路发送能力交换请求（CER）报文命令。默认发送CER报文，这也是diameter基础协议的要求。也可以关闭发送CER报文功能，则TCP（SCTP）连接成功后diameter会话也处于open状态。 
范例 : 
ZXROSNG(config)# diameter-link 1ZXROSNG(config-diameterlink-1)# send-cer-message offZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## send-dwr-message 

send-dwr-message 
命令功能 : 
diameter链路发送watchdog（DWR）报文命令。默认发送DWR消息。当链路处于active状态时，定期自动发送DWR报文。 
命令模式 : 
 diameter链路模式  
命令默认权限级别 : 
15 
命令格式 : 
send-dwr-message 
  {on 
|off 
}
命令参数解释 : 
参数|描述
---|---
on|发送DWR报文。缺省发送。
off|不发送DWR报文
缺省 : 
默认发送DWR消息。 
使用说明 : 
diameter链路发送watchdog（DWR）报文命令。默认发送DWR消息。 
范例 : 
ZXROSNG(config)# diameter-link 1ZXROSNG(config-diameterlink-1)# send-dwr-message offZXROSNG(config-diameterlink-1)#
相关命令 : 
show diameter-link-config allshow diameter-link-status allshow running-config diameter
## show debug diameter 

show debug diameter 
命令功能 : 
显示diameter的debug内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug diameter 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示diameter的debug内容。 
范例 : 
ZXROSNG#show debug diameter DIAMETER: DIAMETER event debugging is on DIAMETER data debugging is on DIAMETER packet debugging is on DIAMETER error debugging is on DIAMETER exception debugging is onZXROSNG#
相关命令 : 
debug diameter 
## show diameter-config 

show diameter-config 
命令功能 : 
显示diameter相关配置参数。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show diameter-config 
 all 
 
命令参数解释 : 
参数|描述
---|---
all|显示所有的diameter相关配置
缺省 : 
无 
使用说明 : 
显示diameter的相关配置 
范例 : 
ZXROSNG#show diameter-config all global capability:noneLink:1peer:1.1.1.2peer:1.1.1.3peer:1.1.1.4peer port:3868tcp,disablesend cersend dwrdeadtime:10link ipv4Link:33peer port:3868tcp,disablesend cersend dwrdeadtime:10link ipv4
相关命令 : 
show running-config diameter 
## show diameter-debug-set 

show diameter-debug-set 
命令功能 : 
显示diameter的debug设置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show diameter-debug-set 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示diameter的debug设置。和diameter-debug-set命令配合使用，用于对debug diameter的过滤。 
范例 : 
ZXROSNG#diameter-debug-set user abc DIAMETER user has been turned onZXROSNG#show diameter-debug-set DIAMETER group:2 debug onZXROSNG#
相关命令 : 
diameter-debug-set 
## show diameter-group 

show diameter-group 
命令功能 : 
显示diameter链路组的相关配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show diameter-group 
  {all 
|name 
 ＜group-name 
＞} 
命令参数解释 : 
参数|描述
---|---
all|显示所有diameter链路组状态
name|显示单个组的配置
＜group-name＞|Diameter组号，范围1-10
缺省 : 
无 
使用说明 : 
显示diameter链路组的相关配置。 
范例 : 
ZXROSNG#show diameter-group allGroup:1dim_algorithm:master-slavelink-no1:link 116link-no2:link 126link-no3:link 128 masterinterval:3retry:3                                                                
相关命令 : 
diameter-group 
## show diameter-link-config 

show diameter-link-config 
命令功能 : 
显示diameter链路的相关配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show diameter-link-config 
  {all 
|＜link No. 
＞} 
命令参数解释 : 
参数|描述
---|---
all|显示所有diameter链路状态
＜link No.＞|显示单条diameter链路信息（取值范围：1~128）
缺省 : 
无 
使用说明 : 
显示diameter链路的相关配置 
范例 : 
ZXROSNG#show diameter-link-config allLink:1peer:1.1.1.2peer:1.1.1.3peer:1.1.1.4peer port:3868tcp,disablesend cersend dwrdeadtime:10link ipv4Link:33peer port:3868tcp,disablesend cersend dwrdeadtime:10link ipv4Link:128peer port:3868tcp,disablesend cersend dwrdeadtime:10
相关命令 : 
diameter-link 
## show diameter-link-status 

show diameter-link-status 
命令功能 : 
显示diameter链路的状态。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show diameter-link-status 
  {all 
|＜link No. 
＞} 
命令参数解释 : 
参数|描述
---|---
all|显示所有diameter链路状态
＜link No.＞|显示单条diameter链路信息（取值范围：1~128）
缺省 : 
无 
使用说明 : 
显示diameter链路的相关状态。说明连接类型：tcp或者sctp；socket状态，diameter会话状态。其中diameter会话状态是建立在socket状态之上的，只有socket可用时diameter会话状态才有可能是open的，也可以调用以下命令关闭发送CER消息，则diameter会话状态与socket状态一致：ZXROSNG(config-diameterlink-1)#send-cer-message off
范例 : 
ZXROSNG#show diameter-link-status all LinkNum  Transport  SocketStatus  DIMSessionLink:1   tcp        dead/disable      closedLink:33  tcp        dead/disable      closedLink:128 tcp        dead/disable      closed
相关命令 : 
diameter-link 
## show diameter-ping 

show diameter-ping 
命令功能 : 
显示diameter-ping的自定义属性配置 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show diameter-ping 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示diameter-ping的自定义属性配置。 
范例 : 
ZXROSNG#show diameter-ping aar vendorid:0; attrid:1; attrtype:int;value:1 ZXROSNG#
相关命令 : 
diameter-ping-set 
## show diameter-statistics 

show diameter-statistics 
命令功能 : 
显示统计开关状态和diameter相关统计结果。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show diameter-statistics 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该统计结果包括以下参数：链路号、报文类型，发送成功次数、失败次数、重传次数等。 
范例 : 
ZXROSNG#show diameter-statistics DIAMETER statistics disableDIAMETER sendtimes:0DIAMETER resendtimes:0DIAMETER rcvtimes:0DIAMETER timeout:0AARsendtimes:0AARresendtimes:0AAArcvtimes:0AARtimeout:0
相关命令 : 
diameter-statistics 
# IPSec配置命令 
## accounting-template 

accounting-template 
命令功能 : 
绑定AAA计费模板。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
accounting-template 
  ＜template-number 
＞
no accounting-template 
命令参数解释 : 
参数|描述
---|---
＜template-number＞|AAA计费模板号，模板号范围为1-2128
缺省 : 
无 
使用说明 : 
在用户组下绑定AAA 计费模板，用户上线后，使用AAA模板下配置的计费方式进行计费。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#accounting-template 1ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  accounting-template 1!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupaccounting-updateshow isakmp user-group
## accounting-update 

accounting-update 
命令功能 : 
指定向AAA服务器发送计费更新报文的时间间隔。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
accounting-update 
  ＜update-period 
＞
no accounting-update 
命令参数解释 : 
参数|描述
---|---
＜update-period＞|发送计费更新报文的时间间隔，范围60s-604800s。
缺省 : 
600秒 
使用说明 : 
在用户组下绑定AAA 计费模板，用户上线后，使用该命令指定向AAA服务器发送计费更新报文的时间间隔。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#accounting-template 1ZXROSNG(config-isakmp-usergroup)# accounting-update 100ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  accounting-template 1accounting-update 100!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupaccounting-templateshow isakmp user-group
## authentication-template 

authentication-template 
命令功能 : 
绑定AAA认证模板。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
authentication-template 
  ＜template-number 
＞
no authentication-template 
命令参数解释 : 
参数|描述
---|---
＜template-number＞|绑定AAA认证模板号，模板号范围为1-2128
缺省 : 
无 
使用说明 : 
在用户组下绑定AAA 认证模板，对用户身份信息使用AAA模板下配置的认证方式进行核实。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#authentication-template 1ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  authentication-template 1!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupshow isakmp user-group
## authorization-template 

authorization-template 
命令功能 : 
绑定AAA 授权模板。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
authorization-template 
  ＜template-number 
＞
no authorization-template 
命令参数解释 : 
参数|描述
---|---
＜template-number＞|AAA授权模板号，模板号范围为1-2128
缺省 : 
无 
使用说明 : 
在用户组下绑定AAA 授权模板，对用户下发的资源，使用AAA模板下配置的授权方式。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)# authorization-template 1ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  authorization-template 1!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupshow isakmp user-group
## auth-pki-profile 

auth-pki-profile 
命令功能 : 
指定隧道虚接口使用的PKI策略模板 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
auth-pki-profile 
  ＜pki-profile-name 
＞
no auth-pki-profile 
命令参数解释 : 
参数|描述
---|---
＜pki-profile-name＞|PKI策略模板名字，可配字节数1-31
缺省 : 
无 
使用说明 : 
该命令用来指明隧道虚接口下绑定的PKI策略模板名字。当使用IKE证书认证方式协商时，需要使用此命令绑定PKI策略模板。当前支持空绑。 
范例 : 
假设在路由器R1上已经创建PKI策略模板”cert”，并在隧道虚接口上使用该模板，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-configZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#pki-profile certZXROSNG(config-ipsec-if-ipsec_tunnel1)#show this!<ipsec>pki-profile cert!</ipsec>
相关命令 : 
无 
## auth-pki-profile 

auth-pki-profile 
命令功能 : 
指定IPsec transport使用的PKI策略模板 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
auth-pki-profile 
  ＜pki-profile-name 
＞
no auth-pki-profile 
命令参数解释 : 
参数|描述
---|---
＜pki-profile-name＞|PKI策略模板名字，可配字节数1-31
缺省 : 
无 
使用说明 : 
该命令用来指明IPsec transport下绑定的PKI策略模板名字。当使用IKE证书认证方式协商时，需要使用此命令绑定PKI策略模板。当前支持空绑 
范例 : 
假设在路由器R1上已经创建PKI策略模板”cert”，并在IPsec transport上使用该模板，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#pki-profile certZXROSNG(config-ipsec-transport1)#show this!<ipsec>isakmp-profile cert!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
无 
## bound-to 

bound-to 
命令功能 : 
指明IPsec传输接口绑定的实际出接口。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
bound-to 
  ＜interface-to-bind-transport 
＞
no bound-to 
  ＜interface-to-bind-transport 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-to-bind-transport＞|接口名称
缺省 : 
无 
使用说明 : 
为IPsec传输虚接口绑定实际出接口。目前支持绑定FEI口、GEI口、GRE逻辑口等。每一个传输虚接口最多支持绑定32个出接口。 
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#bound-to gre_tunnel1ZXROSNG(config-ipsec-transport1)#show this!<ipsec>  bound-to gre_tunnel1!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
无 
## clear crypto ipsec client group 

clear crypto ipsec client group 
命令功能 : 
删除组下的用户。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear crypto ipsec client group 
  ＜group-name 
＞
命令参数解释 : 
参数|描述
---|---
＜group-name＞|远程用户组名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
删除指定组下的所用用户。 
范例 : 
ZXROSNG#clear crypto ipsec client group grp10Are you sure to proceed?[yes/no]:yesZXROSNG#
相关命令 : 
show crypto ipsec client group 
## clear crypto ipsec client interface 

clear crypto ipsec client interface 
命令功能 : 
删除隧道下的用户。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear crypto ipsec client interface 
  ＜interface-name 
＞
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|IPsec隧道虚接口名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
删除指定隧道下的所用用户。 
范例 : 
ZXROSNG#clear crypto ipsec client interface ipsec_tunnel1Are you sure to proceed?[yes/no]:yesZXROSNG#
相关命令 : 
show crypto ipsec client interface 
## clear crypto ipsec client user-ip 

clear crypto ipsec client user-ip 
命令功能 : 
删除隧道下指定IP地址的用户。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear crypto ipsec client user-ip 
  ＜internal-ip-address 
＞ interface 
 ＜interface-name 
＞
命令参数解释 : 
参数|描述
---|---
＜internal-ip-address＞|远程接入用户分配的IP地址，IPv4类型
＜interface-name＞|远程接入用户接入隧道名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
删除指定隧道下某个IP用户。 
范例 : 
ZXROSNG#clear crypto ipsec client user-ip 1.1.1.1 interface ipsec_tunnel1Are you sure to proceed?[yes/no]:yesZXROSNG#
相关命令 : 
show crypto ipsec client user-ip 
## clear crypto ipsec gdoi ks member 

clear crypto ipsec gdoi ks member 
命令功能 : 
清除Key server中的组成员 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear crypto ipsec gdoi ks member 
  {all 
|gm 
 ＜ip-address 
＞|server-name 
 ＜server name 
＞ [gm 
 ＜ip-address 
＞]} 
命令参数解释 : 
参数|描述
---|---
all|删除所有key server
gm|删除指定的GM
＜ip-address＞|GM的IP地址
server-name|删除指定的server
＜server name＞|Key server的名字，1-31个字符
gm|删除指定的GM
＜ip-address＞|GM的IP地址
缺省 : 
无 
使用说明 : 
只清除member信息，不触发相关的踢用户下线流程。用户生命期到期后，重新注册。 
范例 : 
ZXROSNG#clear crypto ipsec gdoi ks member allZXROSNG#
相关命令 : 
无 
## clear crypto ipsec gdoi ks server 

clear crypto ipsec gdoi ks server 
命令功能 : 
清除Key server中的所有用户信息以及生成的策略信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear crypto ipsec gdoi ks server 
  {all 
|server-name 
 ＜server name 
＞} 
命令参数解释 : 
参数|描述
---|---
all|删除所有key server
server-name|删除指定的key server
＜server name＞|Key server的名字，1-31个字符
缺省 : 
无 
使用说明 : 
清除此server下的所有用户信息以及生成的策略信息。 
范例 : 
ZXROSNG#clear crypto ipsec gdoi ks server allZXROSNG#
相关命令 : 
无 
## clear crypto ipsec sa 

clear crypto ipsec sa 
命令功能 : 
删除所有协商的IPsec SA。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear crypto ipsec sa 
  [{peer 
 {＜peer-ipv4-address 
＞ [vrf 
 ＜ipv4-vrf-name 
＞] [force 
]|＜peer-ipv6-address 
＞ [vrf 
 ＜ipv6-vrf-name 
＞] [force 
]}|entry 
 {＜ipv4-destination-address 
＞|＜ipv6-destination-address 
＞} {ah 
|esp 
} ＜spi-value 
＞ [force 
]|force 
|gdoi-group 
 ＜GDOI group name 
＞}]
命令参数解释 : 
参数|描述
---|---
＜peer-ipv4-address＞|ISAKMP协商对端的IPv4地址
＜ipv4-vrf-name＞|ISAKMP协商对端为IPv4地址所在的VRF
force|强制删除IPsec SA
＜peer-ipv6-address＞|ISAKMP协商对端的IPv6地址
＜ipv6-vrf-name＞|ISAKMP协商对端为IPv6地址所在的VRF
force|强制删除IPsec SA
＜ipv4-destination-address＞|ISAKMP协商对端的IPv4地址
＜ipv6-destination-address＞|ISAKMP协商对端的IPv6地址
ah|IPsec封装协议为AH
esp|IPsec封装协议为ESP
＜spi-value＞|IPsec封装的SPI值
force|强制删除IPsec SA
force|强制删除IPsec SA
＜GDOI group name＞|GDOI组的名字
缺省 : 
无 
使用说明 : 
第一条命令是删除全部IPsec SA。第二条命令是将指定对端IP地址和VRF对应的IPsec SA进行删除。第三条命令是将指定通讯目的地址、协议、SPI三元组构成的sa_id对应的IPsec SA进行删除。如果某些场景下删除不掉IPsec SA的时候，可以使用force选项
范例 : 
假设在路由器R1上删除所有的IPsec SA，则路由器R1上的配置示例如下：ZXROSNG#clear crypto ipsec saAre you sure to proceed?[yes/no]:yes
相关命令 : 
show crypto ipsec sa nego 
## clear crypto ipsec statistics 

clear crypto ipsec statistics 
命令功能 : 
clear指定隧道input和output流量信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear crypto ipsec statistics 
  ＜interface-name 
＞
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|＜interface-name＞ 隧道接口名，eg：ipsec_tunnel1
缺省 : 
无 
使用说明 : 
clear crypto ipsec statistics ipsec_tunnel1 
范例 : 
ZXROSNG#clear crypto ipsec statistic ipsec_tunnel1 
相关命令 : 
show crypto ipsec statistics 
## clear isakmp policy 

clear isakmp policy 
命令功能 : 
删除配置的所有IKE协商策略和policy-of-peer。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear isakmp policy 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
策略顺序号范围为1-10000，配置策略的个数不能超过40。此命令相当于批量删除命令，将会把配置的所有的policy以及相关的policy-of-peer全部删除，此后将只保留系统默认的配置。 
范例 : 
假设在路由器R1上要设定IKE协商的安全策略并显示，此后将全部配置删除，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp policy 1ZXROSNG(config-isakmp-1)#exit ZXROSNG(config)#isakmp policy 2ZXROSNG(config-isakmp-2)#exitZXROSNG(config)#show isakmp policy Protection suite of priority 1        Encryption algorithm  : 3des        Hash algorithm        : sha1        Authentication method : pre-share        Diffie-Hellman group  : group1        Lifetime              : 86400 secondsProtection suite of priority 2        Encryption algorithm  : 3des        Hash algorithm        : sha1        Authentication method : pre-share        Diffie-Hellman group  : group1        Lifetime              : 86400 secondsZXROSNG(config)#exit ZXROSNG#clear isakmp policyAre you sure to proceed?[yes/no]:yesZXROSNG#show isakmp policy
相关命令 : 
isakmp policyisakmp peershow isakmp policyshow isakmp policy-of-peer
## clear isakmp sa 

clear isakmp sa 
命令功能 : 
删除所有激活的ISAKMP SA。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear isakmp sa 
  [{force 
|peer 
 {＜peer-ipv4-address 
＞ [vrf 
 ＜ipv4-vrf-name 
＞] [{id-ipv4 
 ＜ipv4-address 
＞|id-fqdn 
 ＜hostname 
＞|id-user-fqdn 
 ＜user-fqdn 
＞|id-key-id 
 ＜key-id 
＞|id-dn 
 ＜pki-domain-name 
＞}]|＜peer-ipv6-address 
＞ [vrf 
 ＜ipv6-vrf-name 
＞]} [force 
]}]
命令参数解释 : 
参数|描述
---|---
force|强制删除ISAKMP SA
＜peer-ipv4-address＞|IKE协商对端的IPv4地址
＜ipv4-vrf-name＞|IKE协商对端为IPv4地址所在的VRF
＜ipv4-address＞|IPv4地址形式的对方ID信息
＜hostname＞|FQDN形式的对方ID信息，长度1-40字节
＜user-fqdn＞|USER-FQDN形式的对方ID信息，长度1-42字节
＜key-id＞|KEY-ID形式的对方ID信息，长度1-40字节
＜pki-domain-name＞|对端证书的domain name信息
＜peer-ipv6-address＞|IKE协商对端的IPv6地址
＜ipv6-vrf-name＞|IKE协商对端为IPv6地址所在的VRF
force|强制删除ISAKMP SA
缺省 : 
无 
使用说明 : 
删除激活的ISAKMP SA。可以通过指明peer和VRF以及peer身份信息删除具体某一个SA 
范例 : 
假设在路由器R1上删除ISAKMP SA，则路由器R1上的配置示例如下：ZXROSNG#clear isakmp saAre you sure to proceed?[yes/no]:yesZXROSNG#clear isakmp sa peer 1.1.1.1 Are you sure to proceed?[yes/no]:yesZXROSNG#clear isakmp sa peer 1.1.1.1 fvrfAre you sure to proceed?[yes/no]:yesZXROSNG#clear isakmp sa peer 20::1Are you sure to proceed?[yes/no]:yesZXROSNG#clear isakmp sa peer 20::1 fvrfAre you sure to proceed?[yes/no]:yesZXROSNG#clear isakmp sa peer 102.0.0.35 id-ipv4 102.0.0.35Are you sure to proceed?[yes/no]:yes
相关命令 : 
show isakmp sa 
## crypto ipsec commit 

crypto ipsec commit 
命令功能 : 
配置全局commit位。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec commit 
 
no crypto ipsec commit 
命令参数解释 : 
					无
				 
缺省 : 
不配置commit位。 
使用说明 : 
该命令配置全局commit位。 
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为IPsec设置commit位，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec commit ZXROSNG(config)#no crypto ipsec commit
相关命令 : 
show running-config ipsec 
## crypto ipsec dynamic-profile 

crypto ipsec dynamic-profile 
命令功能 : 
创建或删除IPsec动态Profile，供动态型隧道使用。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec dynamic-profile 
  ＜crypto-profile-tag 
＞
no crypto ipsec dynamic-profile 
  ＜crypto-profile-tag 
＞
				
命令参数解释 : 
参数|描述
---|---
＜crypto-profile-tag＞|profile名称,用字符串表示，长度不能超过18个字符
缺省 : 
无 
使用说明 : 
此命令创建动态Profile，该Profile下面可以配置转码集、sa的生命期、抗重放标记等。该Profile不能配置acl，默认自带的acl为ip any any。当动态Profile被隧道绑定后，不能修改其下面的配置（配置转码集除外，最多可以配置20个转码集）。 
范例 : 
假设在路由器R1上要配置名为dyn的动态态IPsec profile并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec dynamic-profile dynZXROSNG(config-ipsec-dynamic-profile)#ZXROSNG(config)#show crypto ipsec profile Crypto IPsec profile "dyn"   Access list                   : not configure    Profile type                  : dynamic  Security association lifetime : 1843200000 kilobytes / 28800 seconds  Anti-replay flag              : enable  Anti-replay win_size          : 2048  Anti-replay max_seq           : 4294967295  DH group                      : none  PFS level(none/key-identity)  : none  Transform-sets                : {                                  }  Responder-only (Y/N)          : YZXROSNG(config)# no crypto ipsec dynamic-profile dynZXROSNG(config)#show crypto ipsec profile  ZXROSNG(config)#
相关命令 : 
show crypto ipsec profile 
## crypto ipsec gdoi-group 

crypto ipsec gdoi-group 
命令功能 : 
创建或删除GDOI组。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec gdoi-group 
  ＜GDOI group name 
＞
no crypto ipsec gdoi-group 
  ＜GDOI group name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜GDOI group name＞|指定所要显示的GDOI组名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)# crypto ipsec gdoi-group 1ZXROSNG(config-ipsec-gdoi-group)#
相关命令 : 
无 
## crypto ipsec gdoi-profile 

crypto ipsec gdoi-profile 
命令功能 : 
创建或删除IPsec GDOI描述。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec gdoi-profile 
  ＜crypto-profile-tag 
＞
no crypto ipsec gdoi-profile 
  ＜crypto-profile-tag 
＞
				
命令参数解释 : 
参数|描述
---|---
＜crypto-profile-tag＞|profile名称,用字符串表示，长度不能超过18个字符
缺省 : 
无 
使用说明 : 
此命令创建一个GDOI IPsec profile，该profile可以被绑定在IPsec传输接口上。当被绑定后，不可以删除该profile。创建profile后，进入IPSEC GDOI 描述模式。no命令只能删除GDOI profile，不能删除其他profile。
范例 : 
假设在路由器R1上要配置名为profile1的GDOI IPsec profile并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec gdoi-profile profile2ZXROSNG(config-ipsec-gdoi-profile)#exitZXROSNG(config)#show crypto ipsec profileCrypto IPsec profile "profile2"Access list                   : not configureProfile type                  : gdoiSecurity association lifetime : 0 kilobytes / 0 secondsAnti-replay flag              : disableAnti-replay win_size          : 0Anti-replay max_seq           : 0DH group                      : nonePFS level(none/key-identity)  : noneTransform-sets                : {}Responder-only (Y/N)          : N
相关命令 : 
show crypto ipsec profile 
## crypto ipsec gdoi-server 

crypto ipsec gdoi-server 
命令功能 : 
设定key server的名字 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec gdoi-server 
  ＜server name 
＞
no crypto ipsec gdoi-server 
  ＜server name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜server name＞|gdoi服务的名称
缺省 : 
无 
使用说明 : 
创建key server组，进入IPsec-GDOI-server模式。 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)#exit
相关命令 : 
无 
## crypto ipsec load-balance mode 

crypto ipsec load-balance mode 
命令功能 : 
指定负荷分担的模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec load-balance mode 
  {auto 
|manual 
}
no crypto ipsec load-balance mode 
命令参数解释 : 
参数|描述
---|---
auto|自动模式
manual|手工模式
缺省 : 
自动模式 
使用说明 : 
指定负荷分担的模式。 
范例 : 
ZXROSNG(config)#crypto ipsec load-balance mode manual ZXROSNG(config)#show crypto ipsec load-balance mode Load balance mode : manualZXROSNG(config)#crypto ipsec load-balance mode auto ZXROSNG(config)#show crypto ipsec load-balance mode Load balance mode : auto 
相关命令 : 
ZXROSNG(config)#show crypto ipsec load-balance mode Load balance mode : manual
## crypto ipsec load-waiting 

crypto ipsec load-waiting 
命令功能 : 
设置机架上电负荷分担等待时间。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec load-waiting 
  ＜load-balance-waiting-time 
＞
no crypto ipsec load-waiting 
命令参数解释 : 
参数|描述
---|---
＜load-balance-waiting-time＞|指明机架上电时负荷分担等待时间，范围为2-600秒
缺省 : 
默认为$#35586051#$秒。 
使用说明 : 
机架主控上电成功后，等待一段时间，再进行负荷分担。no命令恢复默认配置。 
范例 : 
假设在路由器R1上设置负荷分担等待时间为200秒，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec load-waiting 200
相关命令 : 
show running-config ipsec 
## crypto ipsec manual-profile 

crypto ipsec manual-profile 
命令功能 : 
创建或删除IPsec手工描述。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec manual-profile 
  ＜crypto-profile-tag 
＞
no crypto ipsec manual-profile 
  ＜crypto-profile-tag 
＞
				
命令参数解释 : 
参数|描述
---|---
＜crypto-profile-tag＞|profile名称,用字符串表示，长度不能超过18个字符
缺省 : 
无 
使用说明 : 
此命令创建一个手工IPsec profile，该profile可以被绑定在IPsec隧道接口上。当被绑定后，不可以删除该profile。创建profile后，进入IPSEC 手工描述模式。no命令只能删除手工profile，不能删除静态profile。
范例 : 
假设在路由器R1上要配置名为profile1的手工IPsec profile并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec manual-profile profile2ZXROSNG(config-ipsec-manual-profile)#exitZXROSNG(config)#show crypto ipsec profileCrypto IPsec profile "profile2"   Access list                   : not configure    Profile type                  : manual  Security association lifetime : 0 kilobytes / 0 seconds  Anti-replay flag              : disable  Anti-replay win_size          : 0  Anti-replay max_seq           : 0  DH group                      : none  PFS level(none/key-identity)  : none  Transform-sets                : {                                  }  Responder-only (Y/N)          : N
相关命令 : 
show crypto ipsec profile 
## crypto ipsec reallocate 

crypto ipsec reallocate 
命令功能 : 
对IPsec隧道或IPsec transport进行重新负荷分担。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec reallocate 
  {all 
|interface 
 ＜interface-to-reallocate 
＞ [cpu-address 
 ＜cpu-address-name 
＞]|ipsec-transport 
 ＜ipsec-transport-to-reallocate 
＞ [cpu-address 
 ＜cpu-address-name 
＞]}
命令参数解释 : 
参数|描述
---|---
all|指明所有的IPsec隧道和IPsec transport进行重新负荷分担
＜interface-to-reallocate＞|指明让某个隧道进行负荷分担
＜cpu-address-name＞|指明负荷分担到某个CPU地址，以SPI接口的形式配置
＜ipsec-transport-to-reallocate＞|指明让某个IPsec transport进行负荷分担
＜cpu-address-name＞|指明负荷分担到某个CPU地址，以SPI接口的形式配置
缺省 : 
无 
使用说明 : 
对于手工类型的隧道以及手工配置的地址不进行重新负荷分担。 
范例 : 
ZXROSNG(config)#crypto ipsec reallocate all Are you sure to proceed?[yes/no]:yesZXROSNG(config)#crypto ipsec reallocate interface ipsec_tunnel1ZXROSNG(config)#ZXROSNG(config)#crypto ipsec reallocate ipsec-transport 1ZXROSNG(config)#
相关命令 : 
show crypto ipsec load-balance  
## crypto ipsec static-profile 

crypto ipsec static-profile 
命令功能 : 
创建或删除IPsec静态描述。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec static-profile 
  ＜crypto-profile-tag 
＞
no crypto ipsec static-profile 
  ＜crypto-profile-tag 
＞
				
命令参数解释 : 
参数|描述
---|---
＜crypto-profile-tag＞|profile名称,用字符串表示，长度不能超过18个字符
缺省 : 
无 
使用说明 : 
此命令创建一个静态IPsec profile，该profile可以被绑定在IPsec隧道接口上。当被绑定后，不可以删除该profile。创建profile后，进入IPSEC 静态描述模式。no命令只能删除静态profile，不能删除手工profile。
范例 : 
假设在路由器R1上要配置名为profile1的静态IPsec profile并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile profile1ZXROSNG(config-ipsec-static-profile)#exitZXROSNG(config)#show crypto ipsec profileCrypto IPsec profile "profile1"   Access list                   : not configure    Profile type                  : static  Security association lifetime : 1843200000 kilobytes / 28800 seconds  Anti-replay flag              : enable  Anti-replay win_size          : 2048  Anti-replay max_seq           : 4294967295  DH group                      : none  PFS level(none/key-identity)  : none  Transform-sets                : {                                  }  Responder-only (Y/N)          : N
相关命令 : 
show crypto ipsec profile 
## crypto ipsec transform-set 

crypto ipsec transform-set 
命令功能 : 
创建或删除用于IPsec保护的转码集。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec transform-set 
  ＜transform-set-tag 
＞
no crypto ipsec transform-set 
  ＜transform-set-tag 
＞
				
命令参数解释 : 
参数|描述
---|---
＜transform-set-tag＞|转码集名称，用字符串表示，长度不能超过18个字符
缺省 : 
无 
使用说明 : 
当转码集被引用时，不能被修改、删除。该转码集用来指明IKE协商第二阶段中的转码信息。 
范例 : 
假设需要在路由器R1上创建IPsec的转码集，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec transform-set mysetZXROSNG(config-crypto-trans)#exitZXROSNG(config)#show crypto ipsec transform-set mysetTransform set "myset": {}     will negotiate = {Tunnel}ZXROSNG(config)#no crypto ipsec transform-set mysetZXROSNG(config)#show crypto ipsec transform-setZXROSNG(config)#
相关命令 : 
show crypto ipsec transform-set 
## crypto ipsec-transport 

crypto ipsec-transport 
命令功能 : 
进入IPsec传输接口配置模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
crypto ipsec-transport 
  ＜ipsec-transport-index 
＞
no crypto ipsec-transport 
  ＜ipsec-transport-index 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipsec-transport-index＞|IPsec传输接口序号，范围：1~$#35586049#$
缺省 : 
无 
使用说明 : 
此命令进入IPsec传输接口配置模式。 
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#exitZXROSNG(config)#show running-config ipsec !<ipsec>crypto ipsec-transport 1$!</ipsec>ZXROSNG(config)#
相关命令 : 
无 
## debug isakmp all 

debug isakmp all 
命令功能 : 
打开IKE协商的所有调试开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug isakmp all 
 
no debug isakmp all 
命令参数解释 : 
					无
				 
缺省 : 
不打开IKE协商的所有调试开关。 
使用说明 : 
打开IKE协商的调试开关。 如果只需要看某个peer相关的打印信息，可以使用peer选项。 
范例 : 
假设在路由器R1上要打开IKE协商调试开关，则路由器R1上的配置示例如下：ZXROSNG#debug isakmp allAll ISAKMP debugging has been turned onZXROSNG#show debug isakmpISAKMP:  ISAKMP error debugging is on  ISAKMP event debugging is on  ISAKMP packet debugging is on  ISAKMP state debugging is on  ISAKMP schedule debugging is onZXROSNG#
相关命令 : 
show debug isakmp 
## debug isakmp error 

debug isakmp error 
命令功能 : 
打开IKE协商的错误打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug isakmp error 
  [peer 
 {{＜ipv4-destination-address 
＞} [{[local 
 ＜ipv4-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]|{＜ipv6-destination-address 
＞} [{[local 
 ＜ipv6-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]}]
no debug isakmp error 
命令参数解释 : 
参数|描述
---|---
＜ipv4-destination-address＞|IKE协商对端的IPv4地址
＜ipv4-local-address＞|IKE协商本端的IPv4地址
＜vrf-name＞|IKE协商对端所在的VRF
＜ipv6-destination-address＞|IKE协商的IPv6地址
＜ipv6-local-address＞|IKE协商的本端的IPv6地址
＜vrf-name＞|IKE协商对端所在的VRF
缺省 : 
不打开IKE协商的错误打印开关。 
使用说明 : 
打开IKE协商的调试开关。 如果只需要看某个peer相关的打印信息，可以使用peer选项。 
范例 : 
假设在路由器R1上要打开IKE协商调试开关，则路由器R1上的配置示例如下：ZXROSNG#debug isakmp errorISAKMP error debugging has been turned onZXROSNG#show debug isakmp ISAKMP:  ISAKMP error debugging is onZXROSNG#
相关命令 : 
show debug isakmp 
## debug isakmp event 

debug isakmp event 
命令功能 : 
打开IKE协商的事件打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug isakmp event 
  [peer 
 {{＜ipv4-destination-address 
＞} [{[local 
 ＜ipv4-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]|{＜ipv6-destination-address 
＞} [{[local 
 ＜ipv6-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]}]
no debug isakmp event 
命令参数解释 : 
参数|描述
---|---
＜ipv4-destination-address＞|IKE协商对端的IPv4地址
＜ipv4-local-address＞|IKE协商本端的IPv4地址
＜vrf-name＞|IKE协商对端所在的VRF
＜ipv6-destination-address＞|IKE协商对端的IPv6地址
＜ipv6-local-address＞|IKE协商本端的IPv6地址
＜vrf-name＞|IKE协商对端所在的VRF
缺省 : 
不打开IKE协商的事件打印开关。 
使用说明 : 
打开IKE协商的调试开关。 如果只需要看某个peer相关的打印信息，可以使用peer选项。 
范例 : 
假设在路由器R1上要打开IKE协商调试开关，则路由器R1上的配置示例如下：ZXROSNG#debug isakmp event ISAKMP event debugging has been turned onZXROSNG#show debug isakmpISAKMP:  ISAKMP event debugging is onZXROSNG#
相关命令 : 
show debug isakmp 
## debug isakmp packet 

debug isakmp packet 
命令功能 : 
打开IKE协商的报文打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug isakmp packet 
  [peer 
 {{＜ipv4-destination-address 
＞} [{[local 
 ＜ipv4-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]|{＜ipv6-destination-address 
＞} [{[local 
 ＜ipv6-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]}]
no debug isakmp packet 
命令参数解释 : 
参数|描述
---|---
＜ipv4-destination-address＞|IKE协商对端的IPv4地址
＜ipv4-local-address＞|IKE协商本端的IPv4地址
＜vrf-name＞|IKE协商对端所在的VRF
＜ipv6-destination-address＞|IKE协商对端的IPv6地址
＜ipv6-local-address＞|IKE协商本端的IPv6地址
＜vrf-name＞|IKE协商对端所在的VRF
缺省 : 
不打开IKE协商的报文打印开关。 
使用说明 : 
打开IKE协商的调试开关。 如果只需要看某个peer相关的打印信息，可以使用peer选项。 
范例 : 
假设在路由器R1上要打开IKE协商调试开关，则路由器R1上的配置示例如下：ZXROSNG#debug isakmp packet   ISAKMP packet debugging has been turned onZXROSNG#show debug isakmpISAKMP:  ISAKMP packet debugging is onZXROSNG#
相关命令 : 
show debug isakmp 
## debug isakmp schedule 

debug isakmp schedule 
命令功能 : 
打开IKE协商的调度打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug isakmp schedule 
  [peer 
 {{＜ipv4-destination-address 
＞} [{[local 
 ＜ipv4-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]|{＜ipv6-destination-address 
＞} [{[local 
 ＜ipv6-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]}]
no debug isakmp schedule 
命令参数解释 : 
参数|描述
---|---
＜ipv4-destination-address＞|IKE协商对端的IPv4地址
＜ipv4-local-address＞|IKE协商本端的IPv4地址
＜vrf-name＞|IKE协商对端所在的VRF
＜ipv6-destination-address＞|IKE协商对端的IPv6地址
＜ipv6-local-address＞|IKE协商本端的IPv6地址
＜vrf-name＞|IKE协商对端所在的VRF
缺省 : 
不打开IKE协商的调度打印开关。 
使用说明 : 
打开IKE协商的调试开关。 如果只需要看某个peer相关的打印信息，可以使用peer选项。 
范例 : 
假设在路由器R1上要打开IKE协商调试开关，则路由器R1上的配置示例如下：ZXROSNG#debug isakmp scheduleISAKMP schedule debugging has been turned onZXROSNG#show debug isakmpISAKMP:  ISAKMP schedule debugging is onZXROSNG#
相关命令 : 
show debug isakmp 
## debug isakmp state 

debug isakmp state 
命令功能 : 
打开IKE协商的状态打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug isakmp state 
  [peer 
 {{＜ipv4-destination-address 
＞} [{[local 
 ＜ipv4-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]|{＜ipv6-destination-address 
＞} [{[local 
 ＜ipv6-local-address 
＞],[vrf-name 
 ＜vrf-name 
＞]}]}]
no debug isakmp state 
命令参数解释 : 
参数|描述
---|---
＜ipv4-destination-address＞|IKE协商对端的IPv4地址
＜ipv4-local-address＞|IKE协商本端的IPv4地址
＜vrf-name＞|IKE协商对端所在的VRF
＜ipv6-destination-address＞|IKE协商对端的IPv6地址
＜ipv6-local-address＞|IKE协商本端的IPv6地址
＜vrf-name＞|IKE协商对端所在的VRF
缺省 : 
不打开IKE协商的状态打印开关。 
使用说明 : 
打开IKE协商的调试开关。 如果只需要看某个peer相关的打印信息，可以使用peer选项。 
范例 : 
假设在路由器R1上要打开IKE协商调试开关，则路由器R1上的配置示例如下：ZXROSNG#debug isakmp stateISAKMP state debugging has been turned onZXROSNG#show debug isakmpISAKMP:  ISAKMP state debugging is onZXROSNG#
相关命令 : 
show debug isakmp 
## default-key encrypted 

default-key encrypted 
命令功能 : 
创建ISAKMP Profile的密文预共享密钥。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
default-key encrypted 
  ＜encrypted-key 
＞
no default-key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|密文预共享密钥，字符串，长度小于172字节
缺省 : 
无 
使用说明 : 
在ISAKMP描述模式下配置默认的密文预共享密钥。密文字符串不能随意配置，必须是show running-config获得的或show isakmp profile获取的。 
范例 : 
ZXROSNG(config)#isakmp profile 2ZXROSNG(config-isakmp-profile)#default-key encrypted R8NHb+rr+Bk=ZXROSNG(config-isakmp-profile)#show this!<isakmp>  default-key encrypted R8NHb+rr+Bk=!</isakmp>ZXROSNG(config-isakmp-profile)#show isakmp profile 2ISAKMP profile "2"   Description                   :     IKE version                   : IKEv1  Self identity                 : address  Exchange mode                 : main  Nat transparency              : disable  Nat transparency keepalive    : 20  DPD interval                  : 0  DPD retry interval            : 0  Accept all peer identities    : disable  Default pre-share-key         : R8NHb+rr+Bk=   ISAKMP policy                 :    {    }  ISAKMP key-set                :    {    }  ISAKMP peer ID                :    {    }
相关命令 : 
isakmp profileshow isakmp profile
## default-key 

default-key 
命令功能 : 
配置ISAKMP Profile的默认预共享密钥。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
default-key 
  ＜key 
＞
no default-key 
命令参数解释 : 
参数|描述
---|---
＜key＞|默认预共享密钥，字符串，长度小于128字节
缺省 : 
无 
使用说明 : 
此命令在ISAKMP描述模式下配置，用来配置该描述的默认预共享密钥。如果配了此命令，意味着如果在协商时匹配不到key-set中的密钥，就会匹配此密钥。即协商过程中，优先匹配描述中key-set下的密钥，default-key作为最后的匹配方式。配置后，显示的都是密文。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#default-key zte123ZXROSNG(config-isakmp-profile)#show this!<isakmp>  default-key encrypted R8NHb+rr+Bk=!</isakmp>ZXROSNG(config-isakmp-profile)#ZXROSNG(config-isakmp-profile)#show isakmp profile 1ISAKMP profile "1"   Description                   :     IKE version                   : IKEv1  Self identity                 : address  Exchange mode                 : main  Nat transparency              : disable  Nat transparency keepalive    : 20  DPD interval                  : 0  DPD retry interval            : 0  Accept all peer identities    : disable  Default pre-share-key         : R8NHb+rr+Bk=   ISAKMP policy                 :    {    }  ISAKMP key-set                :    {    }  ISAKMP peer ID                :    {    }ZXROSNG(config-isakmp-profile)#no default-key ZXROSNG(config-isakmp-profile)#show isakmp profile 1ISAKMP profile "1"   Description                   :   IKE version                   : IKEv1  Self identity                 : address  Exchange mode                 : main  Nat transparency              : disable  Nat transparency keepalive    : 20  DPD interval                  : 0  DPD retry interval            : 0  Accept all peer identities    : disable  Default pre-share-key         : not-configure   ISAKMP policy                 :    {    }  ISAKMP key-set                :    {    }  ISAKMP peer ID                :    {    }ZXROSNG(config-isakmp-profile)#
相关命令 : 
isakmp profileshow isakmp profile
description : 

description 
命令功能 : 
配置预共享密钥描述。 
命令模式 : 
 ISAKMP密钥集模式  
命令默认权限级别 : 
15 
命令格式 : 
description 
  ＜key-set-description 
＞
no description 
命令参数解释 : 
参数|描述
---|---
＜key-set-description＞|描述字符串，长度小于64字节
缺省 : 
无 
使用说明 : 
配置预共享密钥描述。 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#description zte ZXROSNG(config-isakmp-key-set)#show this!<isakmp>  description zte!</isakmp>ZXROSNG(config-isakmp-key-set)#
相关命令 : 
无 
description : 

description 
命令功能 : 
配置ISAKMP profile描述。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
description 
  ＜isakmp-profile-description 
＞
no description 
命令参数解释 : 
参数|描述
---|---
＜isakmp-profile-description＞|描述字符串，长度小于64字节
缺省 : 
无 
使用说明 : 
配置ISAKMP profile描述。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#description zteZXROSNG(config-isakmp-profile)#show this!<isakmp>  description zte!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
无 
## df-bit inner 

df-bit inner 
命令功能 : 
配置根据原始IP报文的DF位进行处理的方式。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
df-bit inner 
  {ignore 
|aware 
}
no df-bit inner 
命令参数解释 : 
参数|描述
---|---
ignore|忽略内层报文的DF标志，如果大于MTU，依然分片
aware|不忽略内层报文DF标志，如果大于MTU，丢弃报文
缺省 : 
内层DF位缺省为aware。 
使用说明 : 
配置根据原始IP报文的DF位进行处理的方式。 
范例 : 
假设在路由器R1上为要设置df位，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#df-bit inner ignoreZXROSNG(config-ipsec-if-ipsec_tunnel1)#no df-bit inner
相关命令 : 
show running-config ipsec 
## df-bit outer 

df-bit outer 
命令功能 : 
对IPsec隧道IP头的DF位进行设置。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
df-bit outer 
  {clear 
|copy 
|set 
}
no df-bit outer 
命令参数解释 : 
参数|描述
---|---
clear|隧道封装时，外层IP头的DF标志被清除
copy|隧道封装时，外层IP头的DF标志拷贝内层IP报文的DF标志
set|隧道封装时，外层IP头的DF标志总被设置
缺省 : 
外层df位缺省为clear。 
使用说明 : 
对IPsec隧道IP头的DF位进行设置。 
范例 : 
假设在路由器R1上为要设置DF位，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#df-bit outer set XR10(config-ipsec-if-ipsec_tunnel1)#no df-bit outer
相关命令 : 
show running-config ipsec 
## dns 

dns 
命令功能 : 
配置DNS地址。 
命令模式 : 
 IPsec-pool模式  
命令默认权限级别 : 
15 
命令格式 : 
dns 
 first 
 ＜first-dns 
＞ [second 
 ＜second-dns 
＞]
no dns 
命令参数解释 : 
参数|描述
---|---
＜first-dns＞|首选的DNS地址, IP地址类型
＜second-dns＞|备选的DNS地址，IP地址类型
缺省 : 
无 
使用说明 : 
在IPsec pool下配置DNS，可以配置首选DNS地址，可选配备选DNS地址。 
范例 : 
ZXROSNG(config)#ipsec-pool zteZXROSNG(config-ipsec-pool)# dns first 1.2.3.4 second 4.5.6.7ZXROSNG(config-ipsec-pool)#show this!<isakmp>  dns first 1.2.3.4 second 4.5.6.7!</isakmp>
相关命令 : 
show ipsec-poolipsec-pool
## eap-query-identity 

eap-query-identity 
命令功能 : 
配置EAP认证是否需要对方的id信息 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
eap-query-identity 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能发送EAP请求对方身份功能
disable|撤销发送EAP请求对方身份功能
缺省 : 
配置EAP认证不需要对方的id信息 
使用说明 : 
此命令支持在ISAKMP用户组下配置，用来指明IKEv2协商中，server端是否发送请求对方identity的请求。 
范例 : 
ZXROSNG(config)#isakmp user-group ikev2ZXROSNG(config-isakmp-usergroup)#eap-query-identity enable ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  eap-query-identity enable!</isakmp>ZXROSNG(config-isakmp-usergroup)#show isakmp user-group ikev2Name:ikev2  Xauth                  : disable  Max users              : 256  Authentication template: 0  Authorization  template: 0  Accounting     template: 0  Accounting     update  : 600  Eap type               : N/A  Eap query identity     : enable
相关命令 : 
isakmp user-groupshow isakmp user-group
## eap-type 

eap-type 
命令功能 : 
指ISAKMP用户组的EAP认证类型。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
eap-type 
  {md5 
|mschapv2 
}
no eap-type 
命令参数解释 : 
参数|描述
---|---
md5|EAP认证方式为EAP-MD5
mschapv2|EAP认证方式为EAP-MSCHAPV2
缺省 : 
无 
使用说明 : 
此命令支持在ISAKMP用户组下配置，用来指明IKEv2协商中，用户组的EAP认证方式，如果不配置此命令，那么该用户组不支持EAP认证，如果配置了，则支持EAP认证，并指明作为server端，将以配置的认证类型作为EAP的认证类型。 
范例 : 
ZXROSNG(config)#isakmp user-group ikev2ZXROSNG(config-isakmp-usergroup)#eap-type ?  md5       EAP-MD5  mschapv2  EAP-MSCHAPV2ZXROSNG(config-isakmp-usergroup)#eap-type md5ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  eap-type md5!</isakmp>ZXROSNG(config-isakmp-usergroup)#no eap-type ZXROSNG(config-isakmp-usergroup)#show thisZXROSNG(config-isakmp-usergroup)#eap-type mschapv2 ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  eap-type mschapv2!</isakmp>ZXROSNG(config-isakmp-usergroup)#show isakmp user-group ikev2Name:ikev2  Xauth                  : disable  Max users              : 256  Authentication template: 0  Authorization  template: 0  Accounting     template: 0  Accounting     update  : 600  Eap type               : EAP-MSCHAPV2  Eap query identity     : disable
相关命令 : 
isakmp user-groupshow isakmp user-group
## encapsulation-mode 

encapsulation-mode 
命令功能 : 
在转码集存在的情况下，设置转码集的封装模式。 
命令模式 : 
 IPsec转码模式  
命令默认权限级别 : 
15 
命令格式 : 
encapsulation-mode 
  {transport 
|tunnel 
}
no encapsulation-mode 
命令参数解释 : 
参数|描述
---|---
transport|封装模式：传输模式
tunnel|封装模式：隧道模式
缺省 : 
转码集缺省封装模式是tunnel。 
使用说明 : 
在设定转码集的封装模式之前，转码集应该是存在的。转码集被引用时，不能修改转码集的封装模式。 
范例 : 
假设需要在路由器R1上配置已创建的转码集的封装模式，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec transform-set myset ZXROSNG(config-crypto-trans)#encapsulation-mode transportZXROSNG(config-crypto-trans)#exitZXROSNG(config)#show crypto ipsec transform-set Transform set "myset": {ah-md5-hmac,esp-3des}     will negotiate = {Transport}ZXROSNG(config)#crypto ipsec transform-set myset ZXROSNG(config-crypto-trans)#no encapsulation-mode ZXROSNG(config-crypto-trans)#exitZXROSNG(config)#show crypto ipsec transform-set Transform set "myset": {ah-md5-hmac,esp-3des}     will negotiate = {Tunnel}ZXROSNG(config)#
相关命令 : 
show crypto ipsec transform-setcrypto ipsec transform-setalgorithm
## exchange-mode 

exchange-mode 
命令功能 : 
设定IKE协商的交换类型。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
exchange-mode 
  {main 
|aggressive 
}
no exchange-mode 
命令参数解释 : 
参数|描述
---|---
main|主模式
aggressive|野蛮模式
缺省 : 
缺省方式是主模式交换类型。 
使用说明 : 
如果ISAKMP协商的身份类型为主机名，采用对端主机名配置预共享密钥认证方式，则ISAKMP协商的交换类型必须配置为野蛮模式，如果配置为主模式会造成协商失败。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#exchange-mode aggressive ZXROSNG(config-isakmp-profile)#show this!<isakmp>  exchange-mode aggressive!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
无 
## group 

group 
命令功能 : 
指定IKE策略的DH交换群。 
命令模式 : 
 ISAKMP模式  
命令默认权限级别 : 
15 
命令格式 : 
group 
  {1 
|2 
|5 
}
no group 
命令参数解释 : 
参数|描述
---|---
1|DH组为group1
2|DH组为group2
5|DH组为group5
缺省 : 
缺省方式是group1。 
使用说明 : 
此命令支持在isakmp policy下分级配置，用来指明IKE协商第一阶段中的当前策略的DH交换群。 
范例 : 
假设在路由器R1上已经创建IKE安全策略“1”，设定该安全策略的DH交换群，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp policy 1ZXROSNG(config-isakmp-1)#group 1 ZXROSNG(config-isakmp-1)#no group
相关命令 : 
isakmp policyshow isakmp policy
## identity fqdn 

identity fqdn 
命令功能 : 
配置 FQDN类型的用户身份。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
identity fqdn 
  ＜fqdn-name 
＞
no identity fqdn 
  ＜fqdn-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜fqdn-name＞|FQDN 身份描述信息，最大长度为40字节
缺省 : 
无 
使用说明 : 
在用户组下配置FQDN类型的 ID，用此ID对用户端进行身份识别。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#identity fqdn zteZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  identity fqdn zte!</isakmp>
相关命令 : 
isakmp user-groupshow isakmp user-group
## identity ipv4 

identity ipv4 
命令功能 : 
配置IPv4 地址类型的用户身份。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
identity ipv4 
 address 
 ＜local-ipv4-address 
＞
no identity ipv4 
 address 
 ＜local-ipv4-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜local-ipv4-address＞|IP地址类型的身份ID（IP地址）
缺省 : 
无 
使用说明 : 
在用户组下配置IPv4地址类型的ID，用此ID对用户端进行身份识别。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#identity ipv4-address 1.1.1.1ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  identity ipv4-address 1.1.1.1!</isakmp>
相关命令 : 
isakmp user-groupshow isakmp user-group
## identity key-id 

identity key-id 
命令功能 : 
配置 key类型的用户身份。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
identity key-id 
  ＜key-id 
＞
no identity key-id 
  ＜key-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜key-id＞|key类型身份描述信息，最大长度为40字节
缺省 : 
无 
使用说明 : 
在用户组下配置key类型 ID，用此ID对用户端进行身份识别。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#identity key-id cccZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  identity key-id ccc!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupshow isakmp user-group
## identity user 

identity user 
命令功能 : 
配置 User FQDN类型的用户身份。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
identity user 
  ＜user-name 
＞ fqdn 
 ＜fqdn-name 
＞
no identity user 
  ＜user-name 
＞ fqdn 
 ＜fqdn-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜user-name＞|用户描述信息，最大长度为20字节
＜fqdn-name＞|FQDN描述信息，最大长度为20字节
缺省 : 
无 
使用说明 : 
在用户组下配置User FQDN类型 ID，用此ID对用户端进行身份识别。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#identity user aaa fqdn bbbZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  identity user aaa fqdn bbb!</isakmp>
相关命令 : 
isakmp user-groupshow isakmp user-group
## identity 

identity 
命令功能 : 
创建或删除KS的组ID。 
命令模式 : 
 IPsec-GDOI组模式  
命令默认权限级别 : 
15 
命令格式 : 
identity 
  {ipv4-address 
 ＜Ipv4-address 
＞|number 
 ＜number 
＞}
no identity 
命令参数解释 : 
参数|描述
---|---
ipv4-address|IPv4地址
＜Ipv4-address＞|IPv4地址
number|Number的值
＜number＞|Number的值
缺省 : 
无 
使用说明 : 
不同gdoi group中的server address和id不能都相同 
范例 : 
ZXROSNG(config)# crypto ipsec gdoi-group 1ZXROSNG(config-ipsec-gdoi-group)# identity ipv4-address 1.1.1.1ZXROSNG(config-ipsec-gdoi-group)# show this!<ipsec>  identity ipv4-address 1.1.1.1!</ipsec>ZXROSNG(config-ipsec-gdoi-group)# 
相关命令 : 
无 
## identity 

identity 
命令功能 : 
设定key server的组ID 
命令模式 : 
 IPsec-GDOI-server模式  
命令默认权限级别 : 
15 
命令格式 : 
identity 
  {ipv4-address 
 ＜Ipv4-address 
＞|number 
 ＜number 
＞}
no identity 
命令参数解释 : 
参数|描述
---|---
ipv4-address|IPV4类型
＜Ipv4-address＞|可以为任意合法的IPv4地址
number|number类型
＜number＞|GDOI组的编号，取值范围为0～2147483647
缺省 : 
无 
使用说明 : 
该命令用来配置KS的组ID。no crypto ipsec identity命令用来删除KS的组ID。缺省情况下，未定义GDOI组的组ID。不通gdoi server的id必须不能相同。需要注意的是，一个KS只能配置一种类型的标识（IP地址或者组号），重复执行，新的配置会覆盖原有配置。 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)# identity number 1234ZXROSNG(config-ipsec-gdoi-server)#exit
相关命令 : 
crypto ipsec gdoi-server 
## ikev2-authentication 

ikev2-authentication 
命令功能 : 
指定IKEv2 AUTH的认证方式。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
ikev2-authentication 
  {pre-share 
|rsa-sig 
}
no ikev2-authentication 
命令参数解释 : 
参数|描述
---|---
pre-share|认证模式为预共享认证方式
rsa-sig|认证模式为RSA签名认证方式
缺省 : 
缺省方式是预共享认证方式。 
使用说明 : 
此命令支持在ISAKMP描述模式下配置，用来指明IKEv2协商AUTH载荷的认证方式。缺省为预共享密钥认证方式。此命令仅对IKEv2有效。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#ikev2-authentication rsa-sigZXROSNG(config-isakmp-profile)#show this!<isakmp>ikev2-authentication rsa-sig!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
isakmp profileshow isakmp profile
## initiator 

initiator 
命令功能 : 
指定发起方发起协商使用的IKE版本 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
initiator 
  {ikev1 
|ikev2 
}
命令参数解释 : 
参数|描述
---|---
ikev1|指明发起方使用IKE版本1.0协商
ikev2|指明发起方使用IKE版本2.0协商
缺省 : 
缺省方式是IKEv1 
使用说明 : 
此命令支持在isakmp-profile下配置，用来指明发起方使用哪个版本的IKE进行协商，默认使用IKEv1进行协商 
范例 : 
假设在路由器R1上已经创建IKE isakmp-profile “1”，设定该策略模板的发起方使用IKEv2版本，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#initiator ikev2ZXROSNG(config-isakmp-profile)#show this!<isakmp>  initiator ikev2!</isakmp>ZXROSNG(config-isakmp-profile)#show isakmp profile 1 ISAKMP profile "1"   Description                   :     IKE version                   : IKEv2  Self identity                  : address  Exchange mode               : main  Nat transparency              : disable  Nat transparency keepalive      : 20  DPD interval                  : 0  DPD retry interval              : 0  ISAKMP policy                 :    {    }  ISAKMP key-set                :    {    }  ISAKMP peer ID                :    {    }
相关命令 : 
isakmp profileshow isakmp profile
interface : 

interface (IPsec隧道模式) 
命令功能 : 
进入IPSEC隧道接口配置模式。 
命令模式 : 
 IPsec隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
interface 
  ＜interface-name 
＞
no interface 
  ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|IPsec隧道接口序号
缺省 : 
无 
使用说明 : 
此命令进入IPSEC隧道接口配置模式。进入的IPSEC隧道接口配置模式前该接口必须先被配置。 
范例 : 
假设在路由器R1上要进入ipsec_tunnel1的接口配置模式，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#exit
相关命令 : 
show running-config ipsec 
## interval 

interval 
命令功能 : 
配置密钥更新间隔 
命令模式 : 
 IPsec手工描述模式  
命令默认权限级别 : 
15 
命令格式 : 
interval 
  ＜interval 
＞
no interval 
命令参数解释 : 
参数|描述
---|---
＜interval＞|采用量子密钥的隧道或者传输更新密钥的周期间隔，范围<1~3600>秒
缺省 : 
40秒 
使用说明 : 
用于配置密钥更新的周期间隔，默认值为40s，如果密钥机性能差，或者性能比较好，可以通过这个参数来调整更新密钥的周期，密钥更新周期越短，安全性越高 
范例 : 
ZXROSNG(config)#crypto ipsec manual-profile zte_pflZXROSNG(config-ipsec-manual-profile)#interval 30
相关命令 : 
无 
## ip-pool 

ip-pool 
命令功能 : 
绑定IP pool地址池。 
命令模式 : 
 IPsec-pool模式  
命令默认权限级别 : 
15 
命令格式 : 
ip-pool 
  ＜ip-pool 
＞
no ip-pool 
命令参数解释 : 
参数|描述
---|---
＜ip-pool＞|绑定的IP pool地址池名称，最大长度为16字节
缺省 : 
无 
使用说明 : 
在IPsec pool下绑定IP pool。 
范例 : 
ZXROSNG(config)#ipsec-pool zteZXROSNG(config-ipsec-pool)# ip-pool dddddZXROSNG(config-ipsec-pool)#show this!<isakmp>  ip-pool ddddd!</isakmp>
相关命令 : 
show ipsec-poolipsec-pool
## ipsec-config 

ipsec-config 
命令功能 : 
进入IPSEC隧道配置模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipsec-config 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令进入IPSEC隧道配置模式。 
范例 : 
假设在路由器R1上要进入IPSEC配置模式，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#
相关命令 : 
show running-config ipsec 
## ipsec-pool 

ipsec-pool 
命令功能 : 
创建IPsec pool 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipsec-pool 
  ＜ipsec-pool-tag 
＞
no ipsec-pool 
  ＜ipsec-pool-tag 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipsec-pool-tag＞|IPsec pool描述名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
新增IPsec pool，可以在IPsec pool下指定ippool，dns和wins。此命令进入IPsec-pool模式。 
范例 : 
ZXROSNG(config)#ipsec-pool zteZXROSNG(config-ipsec-pool)#
相关命令 : 
show ipsec-poolipsec-poolisakmp user-groupip-pooldnswins
## ipsec-pool 

ipsec-pool 
命令功能 : 
用户组下绑定ipsec-pool。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
ipsec-pool 
  ＜ipsec-pool-name 
＞
no ipsec-pool 
  ＜ipsec-pool-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipsec-pool-name＞|绑定的IPsec pool名字，最大长度为32字节
缺省 : 
无 
使用说明 : 
用户组下绑定IPsec pool（需要先配置后，再绑定），如果用户上线用本地授权，则从此IPsec pool中指定的pool分配地址。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)# ipsec pool zteZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  ipsec pool zte!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupshow isakmp user-groupipsec-pool
## ipsec-profile 

ipsec-profile 
命令功能 : 
为IPsec隧道接口配置IPsec profile。 
命令模式 : 
 IPsec-GDOI-server-SA模式,IPsec隧道接口模式  
命令默认权限级别 : 
IPsec隧道接口模式:15,IPsec-GDOI-server-SA模式:15 
命令格式 : 
ipsec-profile 
  ＜ipsec-profile-name 
＞
no ipsec-profile 
命令参数解释 : 
参数|描述
---|---
＜ipsec-profile-name＞|IPsec profile名称
缺省 : 
无 
使用说明 : 
为IPsec隧道绑定IPsec profile，绑定的profile必须先被配置。如果profile是手工的，必须被配置key；如果是协商的，必须配置转码集。无论手工、协商，都必须配置ACL且转码集必须是隧道模式。
范例 : 
假设在路由器R1上为ipsec_tunnel1绑定IPsec profile1，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#ipsec-profile profile1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#exitZXROSNG(config-ipsec)#exitZXROSNG(config)#show running-config-interface ipsec_tunnel1!<Interface>interface ipsec_tunnel1$!</Interface>!<ipsec>ipsec-config  interface ipsec_tunnel1    ipsec-profile profile1  $$!</ipsec>ZXROSNG(config)#
相关命令 : 
show running-config-interface ipsec_tunnel 
## ipsec-profile 

ipsec-profile 
命令功能 : 
为IPsec传输接口配置IPsec profile。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
ipsec-profile 
  ＜ipsec-profile-name 
＞
no ipsec-profile 
命令参数解释 : 
参数|描述
---|---
＜ipsec-profile-name＞|IPsec profile名称
缺省 : 
无 
使用说明 : 
为IPsec传输接口绑定IPsec profile，绑定的profile必须先被配置。如果profile是手工的，必须被配置key，如果是协商的，必须配置转码集。无论手工、协商，都必须配置ACL。
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#ipsec-profile 1ZXROSNG(config-ipsec-transport1)#show this!<ipsec>  ipsec-profile 1!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
无 
## isakmp aggressive 

isakmp aggressive 
命令功能 : 
允许/禁止对端使用野蛮模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp aggressive 
  {disable 
|enable 
}
命令参数解释 : 
参数|描述
---|---
disable|禁止对端使用野蛮模式。
enable|允许对端使用野蛮模式。
缺省 : 
缺省方式是允许对端使用野蛮模式。 
使用说明 : 
此命令是IKE允许/禁止对端使用野蛮模式的开关。 
范例 : 
假设在路由器R1上要允许/禁止对端使用野蛮模式，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp aggressive enableZXROSNG(config)#isakmp aggressive disable
相关命令 : 
isakmp exchange-modeshow running-config isakmp
## isakmp disable 

isakmp disable 
命令功能 : 
关闭IKE协商功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp disable 
 
命令参数解释 : 
					无
				 
缺省 : 
缺省方式是IKE协商功能未启用。 
使用说明 : 
配置该命令将在设备上关闭IKE协商功能。 
范例 : 
假设在路由器R1上要关闭IKE协商功能，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp disable 
相关命令 : 
isakmp enableshow running-config isakmp
## isakmp enable 

isakmp enable 
命令功能 : 
开启IKE协商功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp enable 
 
命令参数解释 : 
					无
				 
缺省 : 
缺省方式是IKE协商功能未启用。 
使用说明 : 
配置了此命令后，设备才会支持IKE协商，否则不会进行协商。 
范例 : 
假设在路由器R1上要开启IKE协商功能，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp enable
相关命令 : 
isakmp disableshow running-config isakmp
## isakmp exchange-mode 

isakmp exchange-mode 
命令功能 : 
设定IKE协商的交换类型。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp exchange-mode 
  {main 
|aggressive 
} {ipv4-address 
 ＜peer-ipv4-address 
＞ netmask 
 ＜peer-ipv4-netmask 
＞ [vrf-name 
 ＜ipv4-vrf-name 
＞]|ipv6-address 
 ＜peer-ipv6-address 
＞ [vrf-name 
 ＜ipv6-vrf-name 
＞]}
no isakmp exchange-mode 
  {ipv4-address 
 ＜peer-ipv4-address 
＞ netmask 
 ＜peer-ipv4-netmask 
＞ [vrf-name 
 ＜ipv4-vrf-name 
＞]|ipv6-address 
 ＜peer-ipv6-address 
＞ [vrf-name 
 ＜ipv6-vrf-name 
＞]}
				
命令参数解释 : 
参数|描述
---|---
main|IKE协商的交换类型为主模式
aggressive|IKE协商的交换类型为野蛮模式
＜peer-ipv4-address＞|IKE协商对端的IPv4地址
＜peer-ipv4-netmask＞|IKE协商对端的子网掩码
＜ipv4-vrf-name＞|IKE协商对端为IPv4地址所在的VRF
＜peer-ipv6-address＞|IKE协商对端的IPv6地址和掩码
＜ipv6-vrf-name＞|IKE协商对端为IPv6地址所在的VRF
缺省 : 
缺省方式是主模式交换类型。 
使用说明 : 
如果IKE协商的身份类型为ID_FQDN，采用对端FQDN配置预共享密钥认证方式，则IKE协商的交换类型必须配置为野蛮模式，如果配置为主模式会造成协商失败。如果为一个子网地址设置交换类型，则此子网范围内的任何主机都可以采用此交换类型，不允许重复配置。 
范例 : 
假设在路由器R1上要设定IKE协商的交换模式并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp exchange-mode main ipv4-address 1.1.1.66 netmask 255.255.255.0 vrf-name fvrfZXROSNG(config)#show isakmp exchange-mode Address/Mask        Exchange-Mode       VRF-Name1.1.1.66/24         main                fvrfZXROSNG(config)#no isakmp exchange-mode ipv4-address 1.1.1.66 netmask 255.255.255.0 vrf-name fvrfZXROSNG(config)#isakmp exchange-mode aggressive ipv6-address 20::1/120 vrf-name fvrfZXROSNG(config)#show isakmp exchange-modeAddress/Mask        Exchange-Mode       VRF-Name20::1/120           aggressive          fvrfZXROSNG(config)#no isakmp exchange-mode ipv6-address 20::1/120 vrf-name fvrf 
相关命令 : 
show isakmp exchange-mode 
## isakmp global-keepalive 

isakmp global-keepalive 
命令功能 : 
设定全局DPD检测机制中DPD间隔和重传间隔。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp global-keepalive 
  ＜dpd-interval 
＞ retry 
 ＜dpd-pkt-interval 
＞
no isakmp global-keepalive 
命令参数解释 : 
参数|描述
---|---
＜dpd-interval＞|DPD间隔,范围为10-3600
＜dpd-pkt-interval＞|重传间隔，范围为2-60
缺省 : 
无 
使用说明 : 
DPD是Dead Peer Detect的缩写，用来检测对端是否出现故障。 
范例 : 
假设在路由器R1上要设定DPD并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp global-keepalive 32 retry 23ZXROSNG(config)#no isakmp global-keepalive
相关命令 : 
show running-config isakmp 
## isakmp identity 

isakmp identity 
命令功能 : 
设定IKE协商的身份类型。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp identity 
  {address 
|hostname 
}
no isakmp identity 
命令参数解释 : 
参数|描述
---|---
address|IKE协商的身份类型为address
hostname|IKE协商的身份类型为hostname
缺省 : 
缺省方式是IKE协商的身份类型为address。 
使用说明 : 
hostname身份类型实际采用的是ID_FQDN，即主机名。协商双方的身份类型必须设置一致，否则，ISAKMP协商会不成功。 
范例 : 
假设在路由器R1上要设定IKE协商的身份类型，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp identity hostname ZXROSNG(config)#isakmp identity address ZXROSNG(config)#show isakmp identity ISAKMP local identity type : addressZXROSNG(config)#no isakmp identity
相关命令 : 
show isakmp identity 
## isakmp keepalive 

isakmp keepalive 
命令功能 : 
为某个ISAKMP协商对端设定DPD检测机制中DPD间隔和重传间隔。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp keepalive 
  ＜dpd-interval 
＞ retry 
 ＜dpd-pkt-interval 
＞ {ipv4-address 
 ＜peer-ipv4-address 
＞ netmask 
 ＜peer-ipv4-netmask 
＞ [vrf-name 
 ＜ipv4-vrf-name 
＞]|ipv6-address 
 ＜peer-ipv6-address 
＞ [vrf-name 
 ＜ipv6-vrf-name 
＞]|fqdn 
 ＜hostname 
＞ [vrf-name 
 ＜fqdn-vrf-name 
＞]}
no isakmp keepalive 
  {ipv4-address 
 ＜peer-ipv4-address 
＞ netmask 
 ＜peer-ipv4-netmask 
＞ [vrf-name 
 ＜ipv4-vrf-name 
＞]|ipv6-address 
 ＜peer-ipv6-address 
＞ [vrf-name 
 ＜ipv6-vrf-name 
＞]|fqdn 
 ＜hostname 
＞ [vrf-name 
 ＜fqdn-vrf-name 
＞]}
				
命令参数解释 : 
参数|描述
---|---
＜dpd-interval＞|DPD间隔,范围为10-3600
＜dpd-pkt-interval＞|重传间隔，范围为2-60
＜peer-ipv4-address＞|ISAKMP协商对端的IPv4地址
＜peer-ipv4-netmask＞|ISAKMP协商对端的子网掩码
＜ipv4-vrf-name＞|ISAKMP协商对端为IPv4所在的VRF
＜peer-ipv6-address＞|ISAKMP协商对端的IPv6地址和掩码
＜ipv6-vrf-name＞|ISAKMP协商对端为IPv6所在的VRF
＜hostname＞|ISAKMP协商对端的FQDN
＜fqdn-vrf-name＞|ISAKMP协商对端所在的VRF
缺省 : 
无 
使用说明 : 
如果为一个子网地址设置DPD参数，则此子网范围内的任何主机都可以采用此DPD参数，不允许重复配置。 
范例 : 
假设在路由器R1上要设定DPD并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp keepalive 32 retry 23 ipv4-address 1.1.1.66 netmask 255.255.255.0 vrf-name FVRFZXROSNG(config)#no isakmp keepalive ipv4-address 1.1.1.66 netmask 255.255.255.0 vrf-name FVRF
相关命令 : 
show running-config isakmp 
## isakmp key-set 

isakmp key-set 
命令功能 : 
创建或删除一个密钥集。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp key-set 
  ＜key-set-name 
＞
no isakmp key-set 
  ＜key-set-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜key-set-name＞|密钥集名称
缺省 : 
无 
使用说明 : 
创建一个密钥集。 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#exitZXROSNG(config)#show isakmp key-set 1ISAKMP key-set "1"  Description           : zte  Pre-shared key        :ZXROSNG(config)#
相关命令 : 
show isakmp key-set 
## isakmp nat-transparency keepalive 

isakmp nat-transparency keepalive 
命令功能 : 
设置NAT穿越情况下NAT设备保活时间信息。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp nat-transparency keepalive 
  ＜keepalive-time 
＞
no isakmp nat-transparency keepalive 
命令参数解释 : 
参数|描述
---|---
＜keepalive-time＞|设置保活时间，单位为秒，范围为5-3600
缺省 : 
缺省为20秒。 
使用说明 : 
该命令参数当支持NAT穿越并有NAT设备后才真正有效，no命令将恢复默认配置。 
范例 : 
假设在路由器R1上要设定保活时间为100秒，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp nat-transparency keepalive 100ZXROSNG(config)#no isakmp nat-transparency keepalive
相关命令 : 
isakmp nat-transparency udp-encapsulation show running-config isakmp
## isakmp nat-transparency udp-encapsulation 

isakmp nat-transparency udp-encapsulation 
命令功能 : 
设备开启支持NAT穿越功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp nat-transparency udp-encapsulation 
 
no isakmp nat-transparency udp-encapsulation 
命令参数解释 : 
					无
				 
缺省 : 
不启用该功能。 
使用说明 : 
开启设备支持NAT穿越功能。 
范例 : 
假设在路由器R1上要支持NAT穿越功能，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp nat-transparency udp-encapsulation
相关命令 : 
isakmp nat-transparency keepaliveshow running-config isakmp
## isakmp peer 

isakmp peer 
命令功能 : 
针对peer地址与VRF配置第一阶段policy。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp peer 
  {ipv4-address 
 ＜peer-ipv4-address 
＞ [vrf-name 
 ＜ipv4-vrf-name 
＞]|ipv6-address 
 ＜peer-ipv6-address 
＞ [vrf-name 
 ＜ipv6-vrf-name 
＞]} policy 
 ＜policy-priority 
＞
no isakmp peer 
  {ipv4-address 
 ＜peer-ipv4-address 
＞ [vrf-name 
 ＜ipv4-vrf-name 
＞]|ipv6-address 
 ＜peer-ipv6-address 
＞ [vrf-name 
 ＜ipv6-vrf-name 
＞]}
				
命令参数解释 : 
参数|描述
---|---
＜peer-ipv4-address＞|ISAKMP协商对端的IPv4地址
＜ipv4-vrf-name＞|ISAKMP协商对端为IPv4地址所在的VRF
＜peer-ipv6-address＞|ISAKMP协商对端的IPv6地址
＜ipv6-vrf-name＞|ISAKMP协商对端为IPv6地址所在的VRF
＜policy-priority＞|ISAKMP策略的顺序号，范围为1-10000
缺省 : 
无 
使用说明 : 
当需要针对某个peer地址配置policy时，需要使用该命令。如果用户配置某个peer+VRF的该配置，则针对该peer+VRF的第一阶段协商时的转码选择，只会使用指明的policy，如果用户未配置，则使用默认的方式，即转码使用所有配置的policy。该命令中的policy 后面的参数即为之前配置的policy优先级数。命令中的policy必须先被配置。并且，如果该policy被某个peer使用，则不能被删除或修改。 
范例 : 
假设在路由器R1上要针对peer 1.2.3.4，vrf-name为zte的对端设置第一阶段策略（优先级序号为10），则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp policy 10ZXROSNG(config-isakmp-10)#exitZXROSNG(config)#isakmp peer ipv4-address 1.2.3.4 vrf-name zte policy 10
相关命令 : 
isakmp policy show isakmp policy-of-peerclear isakmp policy
## isakmp phase1 aggressive crypto 

isakmp phase1 aggressive crypto 
命令功能 : 
对野蛮模式协商的第三条报文，开启或关闭加密功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp phase1 aggressive crypto 
  {disable 
|enable 
}
命令参数解释 : 
参数|描述
---|---
disable|关闭加密功能
enable|开启加密功能
缺省 : 
未开启加密功能。 
使用说明 : 
对野蛮模式的协商的第三条报文，开启或关闭加密功能。 
范例 : 
假设在路由器R1上要对野蛮模式的协商的第三条报文，添加加密功能支持，则路由器R1上的配置示例如下：ZXROSNG(config)# isakmp phase1 aggressive crypto enableZXROSNG(config)# isakmp phase1 aggressive crypto disable
相关命令 : 
show isakmp phase1 
## isakmp policy 

isakmp policy 
命令功能 : 
创建或删除IKE协商策略。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp policy 
  ＜policy-priority 
＞
no isakmp policy 
  ＜policy-priority 
＞
				
命令参数解释 : 
参数|描述
---|---
＜policy-priority＞|ISAKMP策略的顺序号，范围为1-10000
缺省 : 
无 
使用说明 : 
策略顺序号范围为1-10000，配置策略的个数不能超过40，序列号越小，优先级越高。此命令用以指明IKE协商第一阶段所需要的转码载荷所需要的参数，主要是本端支持的加密套件，包括认证方式、DH交换群、hash算法、加密算法以及第一阶段SA（ISAKMP SA）的生命期。协商策略的配置是全局的，如果不配置策略则采用缺省配置进行协商。如果该策略被isakmp peer 命令绑定了，则删除和修改时必须先删除isakmp peer 命令。
范例 : 
假设在路由器R1上要设定IKE协商的安全策略并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp policy 1ZXROSNG(config-isakmp-1)#exit ZXROSNG(config)#isakmp policy 2ZXROSNG(config-isakmp-2)#exitZXROSNG(config)#show isakmp policy Protection suite of priority 1        Encryption algorithm  : 3des        Hash algorithm        : sha1        Authentication method : pre-share        Diffie-Hellman group  : group1        Lifetime              : 86400 secondsProtection suite of priority 2        Encryption algorithm  : 3des        Hash algorithm        : sha1        Authentication method : pre-share        Diffie-Hellman group  : group1        Lifetime              : 86400 secondsZXROSNG(config)#no isakmp policy 1ZXROSNG(config)#show isakmp policy Protection suite of priority 2        Encryption algorithm  : 3des        Hash algorithm        : sha1        Authentication method : pre-share        Diffie-Hellman group  : group1        Lifetime              : 86400 seconds ZXROSNG(config)#exit ZXROSNG#clear isakmp policyAre you sure to proceed?[yes/no]:yesZXROSNG#show isakmp policy
相关命令 : 
isakmp policyshow isakmp policyclear isakmp policyisakmp peer:如果配置的isakmp policy被此命令使用，则该policy无法修改和删除。
## isakmp pre-shared key fqdn 

isakmp pre-shared key fqdn 
命令功能 : 
设定IKE协商的fqdn类型的预共享密钥 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp pre-shared key fqdn 
  ＜hostname 
＞ [vrf-name 
 ＜fqdn-vrf-name 
＞]
no isakmp pre-shared key fqdn 
  ＜hostname 
＞ [vrf-name 
 ＜fqdn-vrf-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜hostname＞|fqdn主机名
vrf-name|指明当前命令配置带vrf-name配置
＜fqdn-vrf-name＞|fqdn vrf名称
缺省 : 
无 
使用说明 : 
在动态策略ISAKMP协商的预共享密钥配置时，可以根据对端协商IP地址来设置预共享密钥。如果ISAKMP协商的交换类型配置为主模式，则推荐根据IP地址来配置预共享密钥；如果交换类型配置为野蛮模式时，则可以根据IP地址或者FQDN来配置预共享密钥。如果为一个子网地址设置预共享密钥，则此子网范围内的任何主机都可以采用此预共享密钥，不允许重复配置。 
范例 : 
ZXROSNG(config)#isakmp pre-shared key fqdn zxr10 vrf-name fvrfZXROSNG(config-isakmp-pre-shared-key)#key abcZXROSNG(config-isakmp-pre-shared-key)#show isakmp key fqdnFQDN                Preshared-Key           Vrfnamezxr10               AazNIF8Zzpo=            fvrf
相关命令 : 
show isakmp key 
## isakmp pre-shared key ipv4-address 

isakmp pre-shared key ipv4-address 
命令功能 : 
设定IKE协商的预共享密钥。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp pre-shared key ipv4-address 
  ＜peer-ipv4-address 
＞ netmask 
 ＜peer-ipv4-netmask 
＞ [local 
 ＜local-ipv4-address 
＞] [vrf-name 
 ＜ipv4-vrf-name 
＞]
no isakmp pre-shared key ipv4-address 
  ＜peer-ipv4-address 
＞ netmask 
 ＜peer-ipv4-netmask 
＞ [local 
 ＜local-ipv4-address 
＞] [vrf-name 
 ＜ipv4-vrf-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜peer-ipv4-address＞|ISAKMP协商对端的IPv4地址
＜peer-ipv4-netmask＞|ISAKMP协商对端的子网掩码
local|指明当前命令有local配置
＜local-ipv4-address＞|ISAKMP协商本端的IPv4地址
vrf-name|指明当前配置有vrf-name配置
＜ipv4-vrf-name＞|ISAKMP协商对端为IPv4地址所在的VRF
缺省 : 
无 
使用说明 : 
在动态策略ISAKMP协商的预共享密钥配置时，可以根据对端协商IP地址来设置预共享密钥。如果ISAKMP协商的交换类型配置为主模式，则推荐根据IP地址来配置预共享密钥；如果交换类型配置为野蛮模式时，则可以根据IP地址或者FQDN来配置预共享密钥。如果为一个子网地址设置预共享密钥，则此子网范围内的任何主机都可以采用此预共享密钥，不允许重复配置。 
范例 : 
假设在路由器R1上要设定IKE协商的预共享密钥并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp pre-shared key ipv4-address 1.1.1.1 netmask 255.255.255.0 ZXROSNG(config-isakmp-pre-shared-key)#key 111ZXROSNG(config-isakmp-pre-shared-key)#show isakmp key ipAddress/Mask        Preshared-Key           Vrfname         LocalIP1.1.1.1/24          6hvoVj+v3EQ=  ZXROSNG(config)#isakmp pre-shared key fqdn zxr10 vrf-name fvrf ZXROSNG(config-isakmp-pre-shared-key)#key abcZXROSNG(config-isakmp-pre-shared-key)#show isakmp key fqdn FQDN                Preshared-Key           Vrfnamezxr10               AazNIF8Zzpo=            fvrf
相关命令 : 
show isakmp key 
## isakmp pre-shared key ipv6-address 

isakmp pre-shared key ipv6-address 
命令功能 : 
设定IKE协商的ipv6-address类型的预共享密钥 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp pre-shared key ipv6-address 
  ＜peer-ipv6-address 
＞ [local 
 ＜local-ipv6-address 
＞] [vrf-name 
 ＜ipv6-vrf-name 
＞]
no isakmp pre-shared key ipv6-address 
  ＜peer-ipv6-address 
＞ [local 
 ＜local-ipv6-address 
＞] [vrf-name 
 ＜ipv6-vrf-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜peer-ipv6-address＞|对端ipv6的地址
local|指明当前配置携带local配置
＜local-ipv6-address＞|local ipv6的地址
vrf-name|指明当前配置携带vrf配置
＜ipv6-vrf-name＞|vrf名称配置
缺省 : 
无 
使用说明 : 
在动态策略ISAKMP协商的预共享密钥配置时，可以根据对端协商IP地址来设置预共享密钥。如果ISAKMP协商的交换类型配置为主模式，则推荐根据IP地址来配置预共享密钥；如果交换类型配置为野蛮模式时，则可以根据IP地址或者FQDN来配置预共享密钥。如果为一个子网地址设置预共享密钥，则此子网范围内的任何主机都可以采用此预共享密钥，不允许重复配置。 
范例 : 
假设在路由器R1上要设定IKE协商的预共享密钥并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp pre-shared key ipv6-address 1::1/24 ZXROSNG(config-isakmp-pre-shared-key)#key 124ZXROSNG(config-isakmp-pre-shared-key)#exitZXROSNG(config)#
相关命令 : 
无 
## isakmp profile 

isakmp profile 
命令功能 : 
创建或删除ISAKMP 描述配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp profile 
  ＜isakmp-profile-tag 
＞
no isakmp profile 
  ＜isakmp-profile-tag 
＞
				
命令参数解释 : 
参数|描述
---|---
＜isakmp-profile-tag＞|ISAKMP profile名字，1-18字节
缺省 : 
无 
使用说明 : 
此命令创建一个ISAKMP profile，该profile可以被IPsec tunnel或IPsec transport绑定。创建ISAKMP profile后，进入ISAKMP 描述配置模式。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#exitZXROSNG(config)#no isakmp profile 1ZXROSNG(config)#
相关命令 : 
show isakmp profile 
## isakmp resend-count 

isakmp resend-count 
命令功能 : 
指定重传次数。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp resend-count 
  ＜resend-count 
＞
no isakmp resend-count 
命令参数解释 : 
参数|描述
---|---
＜resend-count＞|重传次数。缺省6次，范围为3-10。
缺省 : 
缺省方式是默认重传6次。 
使用说明 : 
配置重传次数，no 命令将会恢复默认配置。 
范例 : 
假设在路由器R1上已经指定默认重传次数，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp resend-count 10ZXROSNG(config)#no isakmp resend-count
相关命令 : 
isakmp resend-waitingshow running-config isakmp
## isakmp user-group 

isakmp user-group 
命令功能 : 
配置远程用户组。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp user-group 
  ＜user-group-name 
＞
no isakmp user-group 
  ＜user-group-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜user-group-name＞|远程用户组名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
添加用户接入组，组下配置组的各种属性。此组被绑定在动态型IPsec隧道下。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#max-users 10ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
user-groupxauthauthentication templateauthorization templateaccounting templateaccounting-updateipsec-poolmax-useridentity ipv4-addressidentity fqdnidentity useridentity key-idshow isakmp user-group
## isakmp-profile 

isakmp-profile 
命令功能 : 
为IPsec隧道绑定ISAKMP profile。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp-profile 
  ＜isakmp-profile-name 
＞
no isakmp-profile 
命令参数解释 : 
参数|描述
---|---
＜isakmp-profile-name＞|ISAKMP profile名称
缺省 : 
无 
使用说明 : 
为IPsec隧道配置ISAKMP profile，ISAKMP profile必须先被创建。 
范例 : 
ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#isakmp-profile 1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show this!<ipsec>    isakmp-profile 1!</ipsec>ZXROSNG(config-ipsec-if-ipsec_tunnel1)#
相关命令 : 
无 
## isakmp-profile 

isakmp-profile 
命令功能 : 
为IPsec transport绑定ISAKMP profile。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
isakmp-profile 
  ＜isakmp-profile-name 
＞
no isakmp-profile 
命令参数解释 : 
参数|描述
---|---
＜isakmp-profile-name＞|ISAKMP profile名称
缺省 : 
无 
使用说明 : 
为IPsec transport配置ISAKMP profile，ISAKMP profile必须先被创建。 
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#isakmp-profile 1ZXROSNG(config-ipsec-transport1)#show this!<ipsec>  isakmp-profile 1!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
无 
## keepalive 

keepalive 
命令功能 : 
本端使能DPD协商，设定DPD检测机制中DPD间隔和重传间隔。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
keepalive 
  ＜dpd-interval 
＞ [retry 
 ＜dpd-pkt-interval 
＞]
no keepalive 
命令参数解释 : 
参数|描述
---|---
＜dpd-interval＞|DPD间隔，范围为10-3600
＜dpd-pkt-interval＞|重传间隔，范围为2-60
缺省 : 
无 
使用说明 : 
本端使能DPD协商，设定DPD检测机制中DPD间隔和重传间隔。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#keepalive 123 retry 12 ZXROSNG(config-isakmp-profile)#show this!<isakmp>  keepalive 123 retry 12!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
无 
## key encrypted 

key encrypted 
命令功能 : 
设置对端密钥的密文。
命令模式 : 
 ISAKMP预共享密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key encrypted 
  ＜encrypted-key 
＞
no key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|密钥的密文值
缺省 : 
无 
使用说明 : 
配置密钥的密文，可以通过no key或no key encrypted清除密钥。
范例 : 
ZXROSNG(config)#isakmp pre-shared key fqdn zteZXROSNG(config-isakmp-pre-shared-key)#key encrypted EyENImO/l6Y=ZXROSNG(config-isakmp-pre-shared-key)#show this!<isakmp>  key encrypted EyENImO/l6Y=!</isakmp>ZXROSNG(config-isakmp-pre-shared-key)#
相关命令 : 
show isakmp key ipshow isakmp key fqdn
## key encrypted 

key encrypted 
命令功能 : 
设置key-set对端密钥的密文。
命令模式 : 
 ISAKMP密钥集预共享密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key encrypted 
  ＜encrypted-key 
＞
no key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|设置key-set对端密钥的密文。
缺省 : 
无 
使用说明 : 
配置密钥的密文，可以通过no key或no key encrypted清除密钥。
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key fqdn 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#key encrypted 9hvFkSGkois=ZXROSNG(config-isakmp-key-set-pre-shared-key)#exitZXROSNG(config-isakmp-key-set)#pre-shared key ipv4-address 1.1.1.1 netmask 255.255.255.0   ZXROSNG(config-isakmp-key-set-pre-shared-key)#key encrypted H67q6/ZZYLQ=ZXROSNG(config-isakmp-key-set-pre-shared-key)#exitZXROSNG(config-isakmp-key-set)#show this!<isakmp>  pre-shared key fqdn 1234    key encrypted 9hvFkSGkois=  $  pre-shared key ipv4-address 1.1.1.1 netmask 255.255.255.0    key encrypted H67q6/ZZYLQ=  $!</isakmp>ZXROSNG(config-isakmp-key-set)#
相关命令 : 
show isakmp key-set
## key encrypted 

key encrypted 
命令功能 : 
设置对端密钥的密文 
命令模式 : 
 ISAKMP预共享IPv6密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key encrypted 
  ＜encrypted-key 
＞
no key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|密钥的密文值
缺省 : 
无 
使用说明 : 
配置密钥的密文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp pre-shared key ipv6-address 1::1/24ZXROSNG(config-isakmp-pre-shared-key)#key encrypted EyENImO/l6Y=ZXROSNG(config-isakmp-pre-shared-key)#show this!<isakmp>key encrypted EyENImO/l6Y=!</isakmp>ZXROSNG(config-isakmp-pre-shared-key)#
相关命令 : 
无 
## key encrypted 

key encrypted 
命令功能 : 
设置对端密钥的密文。 
命令模式 : 
 ISAKMP预共享FQDN密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key encrypted 
  ＜encrypted-key 
＞
no key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|密钥的密文值
缺省 : 
无 
使用说明 : 
配置密钥的密文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp pre-shared key fqdn zteZXROSNG(config-isakmp-pre-shared-key)#key encrypted EyENImO/l6Y=ZXROSNG(config-isakmp-pre-shared-key)#show this!<isakmp>key encrypted EyENImO/l6Y=!</isakmp>ZXROSNG(config-isakmp-pre-shared-key)#
相关命令 : 
show isakmp key fqdn 
## key encrypted 

key encrypted 
命令功能 : 
设置key-set对端密钥的密文。 
命令模式 : 
 ISAKMP密钥集预共享IPv6密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key encrypted 
  ＜encrypted-key 
＞
no key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|设置key-set对端密钥的密文。
缺省 : 
无 
使用说明 : 
配置密钥的密文，可以通过no key或no key encrypted清除密钥 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key ipv6-address 1::1/24ZXROSNG(config-isakmp-key-set-pre-shared-key)#key encrypted 9hvFkSGkois=ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
show isakmp key-set 
## key encrypted 

key encrypted 
命令功能 : 
设置key-set对端密钥的密文 
命令模式 : 
 ISAKMP密钥集预共享FQDN密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key encrypted 
  ＜encrypted-key 
＞
no key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|设置key-set对端密钥的密文。
缺省 : 
无 
使用说明 : 
配置密钥的密文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key fqdn 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#key encrypted 9hvFkSGkois=ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
show isakmp key-set 
## key encrypted 

key encrypted 
命令功能 : 
设置key-set对端密钥的密文。 
命令模式 : 
 ISAKMP密钥集预共享USER_FQDN密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key encrypted 
  ＜encrypted-key 
＞
no key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|设置key-set对端密钥的密文。
缺省 : 
无 
使用说明 : 
配置密钥的密文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key user-fqdn 123ddZXROSNG(config-isakmp-key-set-pre-shared-key)#key encrypted 9hvFkSGkois=ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
show isakmp key-set 
## key encrypted 

key encrypted 
命令功能 : 
设置key-set对端密钥的密文。 
命令模式 : 
 ISAKMP密钥集预共享KEY_ID密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key encrypted 
  ＜encrypted-key 
＞
no key encrypted 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|设置key-set对端密钥的密文。
缺省 : 
无 
使用说明 : 
配置密钥的密文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key key-id 1234566deeeZXROSNG(config-isakmp-key-set-pre-shared-key)#key encrypted 9hvFkSGkois=ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
show isakmp key-set 
## key 

key 
命令功能 : 
设置对端密钥的明文 
命令模式 : 
 ISAKMP预共享密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key 
  ＜key 
＞
no key 
命令参数解释 : 
参数|描述
---|---
＜key＞|密钥的明文值
缺省 : 
无 
使用说明 : 
配置密钥的明文，可以通过no key或no key encrypted清除密钥。
范例 : 
ZXROSNG(config)#isakmp pre-shared key fqdn zteZXROSNG(config-isakmp-pre-shared-key)#key 123ZXROSNG(config-isakmp-pre-shared-key)#show this!<isakmp>  key encrypted EyENImO/l6Y=!</isakmp>ZXROSNG(config-isakmp-pre-shared-key)#
相关命令 : 
show isakmp key ipshow isakmp key fqdn
## key 

key 
命令功能 : 
设置key-set对端密钥的明文。
命令模式 : 
 ISAKMP密钥集预共享密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key 
  ＜key 
＞
no key 
命令参数解释 : 
参数|描述
---|---
＜key＞|密钥的明文值
缺省 : 
无 
使用说明 : 
配置密钥的明文，可以通过no key或no key encrypted清除密钥。
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key fqdn 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#key 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#exitZXROSNG(config-isakmp-key-set)#pre-shared key ipv4-address 1.1.1.1 netmask 255.255.255.0   ZXROSNG(config-isakmp-key-set-pre-shared-key)#key 5678ZXROSNG(config-isakmp-key-set-pre-shared-key)#exitZXROSNG(config-isakmp-key-set)#show this!<isakmp>  pre-shared key fqdn 1234    key encrypted 9hvFkSGkois=  $  pre-shared key ipv4-address 1.1.1.1 netmask 255.255.255.0    key encrypted H67q6/ZZYLQ=  $!</isakmp>ZXROSNG(config-isakmp-key-set)#
相关命令 : 
show isakmp key-set
## key 

key 
命令功能 : 
设置对端密钥的明文 
命令模式 : 
 ISAKMP预共享IPv6密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key 
  ＜key 
＞
no key 
命令参数解释 : 
参数|描述
---|---
＜key＞|密钥的明文值
缺省 : 
无 
使用说明 : 
配置密钥的明文，可以通过no key或no key encrypted清除密钥 
范例 : 
ZXROSNG(config)#isakmp pre-shared key ipv6-address 1::1/24ZXROSNG(config-isakmp-pre-shared-key)#key 123ZXROSNG(config-isakmp-pre-shared-key)#show this!<isakmp>key encrypted EyENImO/l6Y=!</isakmp>ZXROSNG(config-isakmp-pre-shared-key)#
相关命令 : 
无 
## key 

key 
命令功能 : 
设置对端密钥的明文 
命令模式 : 
 ISAKMP预共享FQDN密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key 
  ＜key 
＞
no key 
命令参数解释 : 
参数|描述
---|---
＜key＞|密钥的明文值
缺省 : 
无 
使用说明 : 
配置密钥的明文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp pre-shared key fqdn zteZXROSNG(config-isakmp-pre-shared-key)#key 123ZXROSNG(config-isakmp-pre-shared-key)#show this!<isakmp>key encrypted EyENImO/l6Y=!</isakmp>ZXROSNG(config-isakmp-pre-shared-key)#
相关命令 : 
show isakmp key fqdn 
## key 

key 
命令功能 : 
设置key-set对端密钥的明文。 
命令模式 : 
 ISAKMP密钥集预共享IPv6密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key 
  ＜key 
＞
no key 
命令参数解释 : 
参数|描述
---|---
＜key＞|密钥的明文值
缺省 : 
无 
使用说明 : 
配置密钥的明文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key ipv6-address 1::1/24ZXROSNG(config-isakmp-key-set-pre-shared-key)#key 5678ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
show isakmp key-set 
## key 

key 
命令功能 : 
设置key-set对端密钥的明文。 
命令模式 : 
 ISAKMP密钥集预共享FQDN密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key 
  ＜key 
＞
no key 
命令参数解释 : 
参数|描述
---|---
＜key＞|密钥的明文值
缺省 : 
无 
使用说明 : 
配置密钥的明文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key fqdn 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#key 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
show isakmp key-set 
## key 

key 
命令功能 : 
设置key-set对端密钥的明文。 
命令模式 : 
 ISAKMP密钥集预共享USER_FQDN密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key 
  ＜key 
＞
no key 
命令参数解释 : 
参数|描述
---|---
＜key＞|密钥的明文值
缺省 : 
无 
使用说明 : 
配置密钥的明文，可以通过no key或no key encrypted清除密钥 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key user-fqdn 123ddZXROSNG(config-isakmp-key-set-pre-shared-key)#key 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
show isakmp key-set 
## key 

key 
命令功能 : 
设置key-set对端密钥的明文 
命令模式 : 
 ISAKMP密钥集预共享KEY_ID密钥模式  
命令默认权限级别 : 
15 
命令格式 : 
key 
  ＜key 
＞
no key 
命令参数解释 : 
参数|描述
---|---
＜key＞|密钥的明文值
缺省 : 
无 
使用说明 : 
配置密钥的明文，可以通过no key或no key encrypted清除密钥。 
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key key-id 1234566deeeZXROSNG(config-isakmp-key-set-pre-shared-key)#key 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
show isakmp key-set 
## key-set 

key-set 
命令功能 : 
绑定预共享密钥集。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
key-set 
  ＜key-set-name 
＞
no key-set 
  ＜key-set-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜key-set-name＞|预共享密钥集名称
缺省 : 
无 
使用说明 : 
将要绑定的key-set必须已经存在。每一个ISAKMP profile可以配置6个key-set。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#key-set 1ZXROSNG(config-isakmp-profile)#show this!<isakmp>  key-set 1!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
isakmp key-set 
## lack-of-key 

lack-of-key 
命令功能 : 
当量子密钥不足是是否继续加密的开关 
命令模式 : 
 IPsec手工描述模式  
命令默认权限级别 : 
15 
命令格式 : 
lack-of-key 
  {stop-encryption 
|always-encrypted 
}
no lack-of-key 
命令参数解释 : 
参数|描述
---|---
stop-encryption|作用：当量子密钥不足时，停止加密
always-encrypted|作用：当量子密钥不足时，继续加密
缺省 : 
stop-encryption，默认量子密钥不足时停止加密 
使用说明 : 
针对量子密钥不足的时候是否继续加密的配置。如果配置为stop-encryption，则当密钥不足时，ipsec隧道的协议接口会down，当获取到新的密钥时，隧道接口会up。如果配置为always-encrypted，则当密钥不足时，隧道接口状态不变，加密时采用最后一个可用的密钥继续加密，当有新的密钥时，会切换到新的密钥上去加密。注意：这个命令目前对传输接口不生效。传输接口当密钥不足时则会一直使用最后一个密钥进行加密操作。
范例 : 
ZXROSNG(config)#crypto ipsec manual-profile zte_pflZXROSNG(config-ipsec-manual-profile)#lack-of-key stop-encryptionZXROSNG(config-ipsec-manual-profile)#lack-of-key always-encrypted
相关命令 : 
无 
## lifetime 

lifetime 
命令功能 : 
指定ISAKMP SA的生命期。 
命令模式 : 
 ISAKMP模式  
命令默认权限级别 : 
15 
命令格式 : 
lifetime 
  ＜lifetime 
＞
no lifetime 
命令参数解释 : 
参数|描述
---|---
＜lifetime＞|ISAKMP SA的生命期，单位：秒，范围为60-86400秒
缺省 : 
缺省方式isakmp SA的生命期为86400秒。 
使用说明 : 
此命令支持在isakmp policy下分级配置，用来指明IKE协商第一阶段中的当前策略的SA生命期。 
范例 : 
假设在路由器R1上已经创建IKE安全策略“1”，设定ISAKMP SA的生命期，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp policy 1ZXROSNG(config-isakmp-1)#lifetime 120ZXROSNG(config-isakmp-1)#no lifetime ZXROSNG(config-isakmp-1)#
相关命令 : 
isakmp policyshow isakmp policy
## load-sharing weight 

load-sharing weight 
命令功能 : 
指明该虚接口的负荷分担权重信息。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
load-sharing weight 
  ＜value-of-weight 
＞
no load-sharing weight 
命令参数解释 : 
参数|描述
---|---
＜value-of-weight＞|虚接口负荷分担权重值
缺省 : 
缺省值1 
使用说明 : 
此命令用来指定该虚接口的负荷分担权重值，主要对应于该虚接口下IPsec流的流量。默认此值为1，用户可以根据当前此虚接口可能存在的流量进行对应的比例替换，比如有3个虚接口，虚接口1的流量为10M，虚接口2的流量为100M，虚接口3的流量为50M，那么，虚接口可以设为1，虚接口2设为10，虚接口3设为5。 
范例 : 
ZXROSNG(config)#ipsec-configZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#load-sharing weight 3ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show this!<ipsec>load-sharing weight 12!</ipsec>ZXROSNG(config-ipsec-if-ipsec_tunnel1)#
相关命令 : 
无 
## load-sharing weight 

load-sharing weight 
命令功能 : 
指明该虚接口的负荷分担权重信息。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
load-sharing weight 
  ＜value-of-weight 
＞
no load-sharing weight 
命令参数解释 : 
参数|描述
---|---
＜value-of-weight＞|虚接口负荷分担权重值
缺省 : 
1 
使用说明 : 
此命令用来指定该虚接口的负荷分担权重值，主要对应于该虚接口下IPsec流的流量。默认此值为1，用户可以根据当前此虚接口可能存在的流量进行对应的比例替换，比如有3个虚接口，虚接口1的流量为10M，虚接口2的流量为100M，虚接口3的流量为50M，那么，虚接口可以设为1，虚接口2设为10，虚接口3设为5。 
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#load-sharing weight 12ZXROSNG(config-ipsec-transport1)#show this!<ipsec>load-sharing weight 12!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
无 
## local address 

local address 
命令功能 : 
设定key server的本端ipv4地址，发送rekey报文时候，源地址填写为该地址 
命令模式 : 
 IPsec-GDOI-server模式  
命令默认权限级别 : 
15 
命令格式 : 
local address 
 ipv4-address 
 ＜local-ipv4-address 
＞
no local address 
命令参数解释 : 
参数|描述
---|---
＜local-ipv4-address＞|本地IP地址，可以为任意合法的IPv4地址
缺省 : 
无 
使用说明 : 
该命令用来配置KS的rekey的本端地址。 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)# local address ipv4-address 1.1.1.1ZXROSNG(config-ipsec-gdoi-server)#exit
相关命令 : 
crypto ipsec gdoi-server 
## local 

local 
命令功能 : 
指明IPsec传输接口的本地地址。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
local 
  {ipv4-address 
 ＜local-ipv4-address 
＞|ipv6-address 
 ＜peer-ipv6-address 
＞|interface 
 ＜local-interface 
＞}
no local 
命令参数解释 : 
参数|描述
---|---
＜local-ipv4-address＞|指明具体的IP地址
＜peer-ipv6-address＞|指明具体的IPv6地址
＜local-interface＞|本端接口
缺省 : 
无 
使用说明 : 
配置传输接口的本地地址，通常该地址为物理口地址。本地地址类型需要和配置描述中的访问列表类型匹配。
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#local ipv4-address 1.1.1.1 ZXROSNG(config-ipsec-transport1)#show this!<ipsec>  local ipv4-address 1.1.1.1!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
remote ipv4-address  
## location 

location 
命令功能 : 
指明该虚接口的负荷分担地址信息。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
location 
  {mpu 
|spu 
 active 
 ＜cpu-address 
＞ [standby 
 ＜cpu-address 
＞]}
no location 
命令参数解释 : 
参数|描述
---|---
mpu|集中式版本中，指定ipsec业务在MPU上
spu|分布式版本中，指定ipsec业务在SPU上
＜cpu-address＞|主用IPsec业务CPU的地址信息，以SPI接口的形式配置
＜cpu-address＞|主用IPsec业务CPU的地址信息，以SPI接口的形式配置
缺省 : 
无 
使用说明 : 
对于静态型虚接口，此命令必须在其他命令配置（tunnel local，tunnel remote，tunnel vrf，ipsec-profile）之后再进行配置。对于动态型虚接口，当为远程接入时，ipsec-profile中的ACL规则必须要根据该虚接口的用户组IP地址池信息进行配置。对于手工型虚接口，此命令不需要配置。 
范例 : 
ZXROSNG(config)#ipsec-configZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#location spu active spi-0/1/0/1 standby spi-0/1/0/2ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show this!<ipsec>location spu active spi-0/1/0/1 standby spi-0/1/0/2!</ipsec>ZXROSNG(config-ipsec-if-ipsec_tunnel1)#ZXROSNG(config-ipsec-if-ipsec_tunnel1)#location mpuZXROSNG(config-ipsec-if-ipsec_tunnel1)#show this!<ipsec>location mpu!</ipsec>ZXROSNG(config-ipsec-if-ipsec_tunnel1)#
相关命令 : 
show crypto ipsec load-balance 
## location 

location 
命令功能 : 
指明该虚接口的负荷分担地址信息。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
location 
  {mpu 
|spu 
 active 
 ＜cpu-address 
＞ [standby 
 ＜cpu-address 
＞]}
no location 
命令参数解释 : 
参数|描述
---|---
mpu|集中式版本中，指定ipsec业务在MPU上
spu|分布式版本中，指定ipsec业务在SPU上
＜cpu-address＞|主用IPsec业务CPU的地址信息，以SPI接口的形式配置
＜cpu-address＞|主用IPsec业务CPU的地址信息，以SPI接口的形式配置
缺省 : 
无 
使用说明 : 
对于静态型虚接口，此命令必须在其他命令配置（local，remote，vrf，ipsec-profile）之后再进行配置。对于动态型虚接口，当为远程接入时，ipsec-profile中的ACL规则必须要根据该虚接口的用户组IP地址池信息进行配置。对于手工型虚接口，此命令不需要配置。 
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#location spu active spi-0/1/0/1 standby spi-0/1/0/2ZXROSNG(config-ipsec-transport1)#show this!<ipsec>location spu active spi-0/1/0/1 standby spi-0/1/0/2!</ipsec>ZXROSNG(config-ipsec-transport1)#ZXROSNG(config-ipsec-transport1)#location mpuZXROSNG(config-ipsec-transport1)#show this!<ipsec>location mpu!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
show crypto ipsec load-balance 
## match any-identity 

match any-identity 
命令功能 : 
配置ISAKMP Profile是否允许所有的对方ID身份。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
match any-identity 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启允许ISAKMP Profile所有的对端身份功能
disable|关闭允许ISAKMP Profile所有的对端身份功能
缺省 : 
disable。 
使用说明 : 
此命令支持在ISAKMP描述模式下配置。该功能开启的情况，相当于不认证对方的身份，即对方的任意身份都是许可的。该功能关闭的情况下，使用ISAKMP Profile中的match identity命令去匹配对方的身份。 
范例 : 
ZXROSNG(config)#isakmp profile 2ZXROSNG(config-isakmp-profile)#match any-identity enable ZXROSNG(config-isakmp-profile)#show this!<isakmp>  match any-identity enable!</isakmp>ZXROSNG(config-isakmp-profile)#show isakmp profile 2ISAKMP profile "2"   Description                   :     IKE version                   : IKEv1  Self identity                 : address  Exchange mode                 : main  Nat transparency              : disable  Nat transparency keepalive    : 20  DPD interval                  : 0  DPD retry interval            : 0  Accept all peer identities    : enable  Default pre-share-key         : not-configure   ISAKMP policy                 :    {    }  ISAKMP key-set                :    {    }  ISAKMP peer ID                :    {}ZXROSNG(config-isakmp-profile)#match any-identity disable ZXROSNG(config-isakmp-profile)#show isakmp profile 2ISAKMP profile "2"   Description                   :     IKE version                   : IKEv1  Self identity                 : address  Exchange mode                 : main  Nat transparency              : disable  Nat transparency keepalive    : 20  DPD interval                  : 0  DPD retry interval            : 0  Accept all peer identities    : disable  Default pre-share-key         : not-configure   ISAKMP policy                 :    {    }  ISAKMP key-set                :    {    }  ISAKMP peer ID                :    {    }
相关命令 : 
crypto ipsec dynamic-profileshow crypto ipsec profile
## match identity 

match identity 
命令功能 : 
设定IKE协商对端身份。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
match identity 
  {ipv4-address 
 ＜peer-ipv4-address 
＞|ipv6-address 
 ＜peer-ipv6-address 
＞|fqdn 
 ＜hostname 
＞|pki-common-name 
 ＜common-name 
＞}
no match identity 
  {ipv4-address 
 ＜peer-ipv4-address 
＞|ipv6-address 
 ＜peer-ipv6-address 
＞|fqdn 
 ＜hostname 
＞|pki-common-name 
 ＜common-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜peer-ipv4-address＞|对端IPv4地址
＜peer-ipv6-address＞|对端IPv6地址
＜hostname＞|对端主机名
＜common-name＞|证书domain 名称
缺省 : 
无 
使用说明 : 
IKE协商第一阶段对端发过来的ID必须与本端配置匹配，否则，ISAKMP协商会不成功。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#match identity fqdn 1234ZXROSNG(config-isakmp-profile)#match identity ipv4-address 1.1.1.1 ZXROSNG(config-isakmp-profile)#show this!<isakmp>  match identity fqdn 1234  match identity ipv4-address 1.1.1.1!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
无 
## match 

match 
命令功能 : 
为安全策略或者IPsec配置描述指定访问列表。 
命令模式 : 
 IPsec手工描述模式  
命令默认权限级别 : 
15 
命令格式 : 
match 
 acl 
 ＜access-list-name 
＞ {v4 
|v6 
}
no match 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|扩展访问列表的名字
v4|ACL类型为IPv4
v6|ACL类型为IPv6
缺省 : 
无 
使用说明 : 
设置的条件是IPsec配置描述已经被创建。此命令支持在profile下的分级配置。在一个IPsec配置描述下只能指定一个访问列表。当IPsec配置描述被引用或有对端/本端地址配置时，不能修改、删除访问列表的引用关系。
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该描述配置访问列表，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile myprofile  ZXROSNG(config-ipsec-static-profile)#match acl myacl v4ZXROSNG(config-ipsec-static-profile)#no match
相关命令 : 
crypto ipsec static-profilecrypto ipsec manual-profileshow crypto ipsec profile
## match 

match 
命令功能 : 
为安全策略或者IPsec配置描述指定访问列表。 
命令模式 : 
 IPsec静态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
match 
 acl 
 ＜access-list-name 
＞ {v4 
|v6 
}
no match 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|扩展访问列表的名字
v4|ACL类型为IPv4
v6|ACL类型为IPv6
缺省 : 
无 
使用说明 : 
设置的条件是IPsec配置描述已经被创建。此命令支持在profile下的分级配置。在一个IPsec配置描述下只能指定一个访问列表。当IPsec配置描述被引用或有对端/本端地址配置时，不能修改、删除访问列表的引用关系。
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该描述配置访问列表，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile myprofile  ZXROSNG(config-ipsec-static-profile)#match acl myacl v4ZXROSNG(config-ipsec-static-profile)#no match
相关命令 : 
crypto ipsec static-profilecrypto ipsec manual-profileshow crypto ipsec profile
## match 

match 
命令功能 : 
配置动态ipsec profile绑定的acl。 
命令模式 : 
 IPsec动态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
match 
 acl 
 ＜access-list-name 
＞ {v4 
|v6 
}
no match 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|扩展访问列表的名字
v4|ACL类型为IPv4
v6|ACL类型为IPv6
缺省 : 
无 
使用说明 : 
此命令支持在IPsec动态描述模式下配置，用来配置IPsec动态profile绑定的acl。在动态描述模式下，此命令可以配置，也可以不配置，如果不配置，表明ACL为通配，即permit ip any any的情况。 
范例 : 
ZXROSNG(config)#crypto ipsec dynamic-profile 1ZXROSNG(config-ipsec-dynamic-profile)#match acl 1 v4ZXROSNG(config-ipsec-dynamic-profile)#show this!<ipsec>  match acl 1 v4!</ipsec>ZXROSNG(config-ipsec-dynamic-profile)#
相关命令 : 
crypto ipsec dynamic-profileshow crypto ipsec profile
## match 

match 
命令功能 : 
为安全策略或者IPsec配置描述指定访问列表。 
命令模式 : 
 IPsec-GDOI描述模式  
命令默认权限级别 : 
15 
命令格式 : 
match 
 acl 
 ＜access-list-name 
＞ {v4 
|v6 
}
no match 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|扩展访问列表的名字
v4|ACL类型为IPv4
v6|ACL类型为IPv6
缺省 : 
无 
使用说明 : 
设置的条件是IPsec配置描述已经被创建。此命令支持在profile下的分级配置。在一个IPsec配置描述下只能指定一个访问列表。当IPsec配置描述被引用或有对端/本端地址配置时，不能修改、删除访问列表的引用关系。
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该描述配置访问列表，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec gdoi-profile myprofileZXROSNG(config-ipsec-gdoi-profile)#match acl myacl v4ZXROSNG(config-ipsec-gdoi-profile)#no match
相关命令 : 
crypto ipsec gdoi-profileshow crypto ipsec profile
## max-users 

max-users 
命令功能 : 
配置用户组的最大接入用户数量。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
max-users 
  ＜user-number 
＞
no max-users 
命令参数解释 : 
参数|描述
---|---
＜user-number＞|组的最大接入用户数量，范围1-256。
缺省 : 
256 
使用说明 : 
指定此组下允许的最大用户接入数目（默认256）。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)# max-users 10ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  max-users 10!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupshow isakmp user-group
## multicast-interface 

multicast-interface 
命令功能 : 
配置主播路由接口 
命令模式 : 
 IPsec-GDOI组模式  
命令默认权限级别 : 
15 
命令格式 : 
multicast-interface 
  ＜multicastl-interface 
＞
no multicast-interface 
命令参数解释 : 
参数|描述
---|---
＜multicastl-interface＞|组播路由接口
缺省 : 
无 
使用说明 : 
配置组播路由接口 
范例 : 
待补充 
相关命令 : 
无 
## nat-transparency keepalive 

nat-transparency keepalive 
命令功能 : 
设置NAT穿越情况下NAT设备保活时间信息。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
nat-transparency keepalive 
  ＜keepalive-time 
＞
no nat-transparency keepalive 
命令参数解释 : 
参数|描述
---|---
＜keepalive-time＞|设置保活时间，单位为秒，范围为5-3600
缺省 : 
缺省为20秒。 
使用说明 : 
该命令参数当支持NAT穿越并有NAT设备后才真正有效。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#nat-transparency keepalive 123 ZXROSNG(config-isakmp-profile)#show this!<isakmp>  nat-transparency keepalive 123!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
nat-transparency udp-encapsulation 
## nat-transparency udp-encapsulation 

nat-transparency udp-encapsulation 
命令功能 : 
使能或不使能设备支持NAT穿越功能。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
nat-transparency udp-encapsulation 
 
no nat-transparency udp-encapsulation 
命令参数解释 : 
					无
				 
缺省 : 
不使能。 
使用说明 : 
使能设备支持NAT穿越功能。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#nat-transparency udp-encapsulation ZXROSNG(config-isakmp-profile)#show this!<isakmp>  nat-transparency udp-encapsulation!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
nat-transparency keepalive 
## one-time-pad 

one-time-pad 
命令功能 : 
配置每个密钥可以使用的次数 
命令模式 : 
 IPsec手工描述模式  
命令默认权限级别 : 
15 
命令格式 : 
one-time-pad 
  ＜cycle 
＞
no one-time-pad 
命令参数解释 : 
参数|描述
---|---
＜cycle＞|作用：配置每个密钥可以使用的次数取值范围：1-1000000取值含义： 每个密钥可以使用的次数。如果没有配置，或者no命令删除后，这个值为0，表示由平台控制更新密钥。默认值：0
缺省 : 
缺省值为0，表示由平台控制更新密钥，每个密钥使用的次数不受限制。 
使用说明 : 
当由平台周期更新密钥时，采用no命令删除此配置；    当需要根据密钥使用次数来按需更新密钥时，采用此命令配置成适当的值。    转发面对报文加解密时，根据每个密钥使用的次数来决定是否需要更新密钥。
范例 : 
ZXROSNG(config)#crypto ipsec manual-profile zte_pflZXROSNG(config-ipsec-manual-profile)#one-time-pad 1000
相关命令 : 
无 
## peer identity 

peer identity 
命令功能 : 
IKEv2协商时，指定隧道虚接口对应的对方的ID身份 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
peer identity 
  {ipv4-address 
 ＜peer-ipv4-address 
＞|ipv6-address 
 ＜peer-ipv6-address 
＞|fqdn 
 ＜hostname 
＞}
no peer identity 
命令参数解释 : 
参数|描述
---|---
ipv4-address|用IPV4地址识别对端身份
＜peer-ipv4-address＞|对端IPv4地址
ipv6-address|用IPV6地址识别对端身份
＜peer-ipv6-address＞|对端IPv6地址
fqdn|用对端主机名识别对端身份
＜hostname＞|对端主机名，1-40字节
缺省 : 
无 
使用说明 : 
该命令用来在IKEv2协商时，指明对方ID身份载荷类型与载荷内容 
范例 : 
假设在路由器R1上已经创建ipsec_tunnel1，指明对方的ID身份为FQDN类型，ID内容为ZXR10：ZXROSNG(config)#ipsec-configZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#peer identity fqdn ZXR10ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show this!<ipsec>    peer identity fqdn ZXR10!</ipsec>ZXROSNG(config-ipsec-if-ipsec_tunnel1)#
相关命令 : 
无 
## peer identity 

peer identity 
命令功能 : 
IKEv2协商时，指定IPsec transport对应的对方的ID身份 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
peer identity 
  {ipv4-address 
 ＜peer-ipv4-address 
＞|ipv6-address 
 ＜peer-ipv6-address 
＞|fqdn 
 ＜hostname 
＞}
no peer identity 
命令参数解释 : 
参数|描述
---|---
ipv4-address|用IPV4地址识别对端身份
＜peer-ipv4-address＞|对端IPv4地址
ipv6-address|用IPV6地址识别对端身份
＜peer-ipv6-address＞|对端IPv6地址
fqdn|用主机名识别对端身份
＜hostname＞|对端主机名，1-40字节
缺省 : 
无 
使用说明 : 
该命令用来在IKEv2协商时，指明对方ID身份载荷类型与载荷内容 
范例 : 
假设在路由器R1上已经创建ipsec_transport1，指明对方的ID身份为FQDN类型，ID内容为ZXR10：ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#peer identity fqdn ZXR10ZXROSNG(config-ipsec-transport1)#show this!<ipsec>  peer identity fqdn ZXR10!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
无 
## policy 

policy 
命令功能 : 
配置第一阶段policy。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
policy 
  ＜policy-priority 
＞
no policy 
  ＜policy-priority 
＞
				
命令参数解释 : 
参数|描述
---|---
＜policy-priority＞|ISAKMP策略的顺序号，范围为1-10000
缺省 : 
无 
使用说明 : 
配置IKE协商第一阶段策略。命令中的policy必须先被创建。每一个ISAKMP profile可以配置38个policy。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#policy 1ZXROSNG(config-isakmp-profile)#show this!<isakmp>  policy 1!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
isakmp policy 
## pre-fragmentation 

pre-fragmentation 
命令功能 : 
开启或关闭预分片功能。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
pre-fragmentation 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启预分片功能
disable|关闭预分片功能
缺省 : 
预分片功能默认打开。 
使用说明 : 
是否使用预分片功能。 
范例 : 
假设需要在路由器R1上进行预分片，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#pre-fragmentation enableZXROSNG(config-ipsec-if-ipsec_tunnel1)#pre-fragmentation disable
相关命令 : 
show running-config ipsec 
## pre-shared key fqdn 

pre-shared key fqdn 
命令功能 : 
配置预共享密钥。 
命令模式 : 
 ISAKMP密钥集模式  
命令默认权限级别 : 
15 
命令格式 : 
pre-shared key fqdn 
  ＜hostname 
＞ [vrf-name 
 ＜fqdn-vrf-name 
＞]
no pre-shared key fqdn 
  ＜hostname 
＞ [vrf-name 
 ＜fqdn-vrf-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜hostname＞|配置fqdn名称
vrf-name|指明配置携带vrf-name配置
＜fqdn-vrf-name＞|vrf名称
缺省 : 
无 
使用说明 : 
进入ISAKMP密钥集预共享密钥配置模式，可以根据IP地址或者、FQDN等来配置预共享密钥。如果为一个子网地址设置预共享密钥，则此子网范围内的任何主机都可以采用此预共享密钥。每一个ISAKMP 密钥集可以配置100组预共享密钥
范例 : 
假设在路由器R1上要设定IKE协商的预共享密钥并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key fqdn 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#key 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
无 
## pre-shared key ipv4-address 

pre-shared key ipv4-address 
命令功能 : 
配置预共享密钥。 
命令模式 : 
 ISAKMP密钥集模式  
命令默认权限级别 : 
15 
命令格式 : 
pre-shared key ipv4-address 
  ＜peer-ipv4-address 
＞ netmask 
 ＜peer-ipv4-netmask 
＞ [vrf-name 
 ＜ipv4-vrf-name 
＞]
no pre-shared key ipv4-address 
  ＜peer-ipv4-address 
＞ netmask 
 ＜peer-ipv4-netmask 
＞ [vrf-name 
 ＜ipv4-vrf-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜peer-ipv4-address＞|ISAKMP协商对端的IPv4地址
＜peer-ipv4-netmask＞|ISAKMP协商对端的子网掩码
vrf-name|指明当前命令有vrf-name配置
＜ipv4-vrf-name＞|ISAKMP协商对端为IPv4地址所在的VRF
缺省 : 
无 
使用说明 : 
进入ISAKMP密钥集预共享密钥配置模式，可以根据IP地址或者、FQDN等来配置预共享密钥。如果为一个子网地址设置预共享密钥，则此子网范围内的任何主机都可以采用此预共享密钥。每一个ISAKMP 密钥集可以配置100组预共享密钥。
范例 : 
假设在路由器R1上要设定IKE协商的预共享密钥并显示，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key fqdn 1234 ZXROSNG(config-isakmp-key-set-pre-shared-key)#key 1234ZXROSNG(config-isakmp-key-set-pre-shared-key)#exitZXROSNG(config-isakmp-key-set)#pre-shared key ipv4-address 1.1.1.1 netmask 255.255.255.0   ZXROSNG(config-isakmp-key-set-pre-shared-key)#key 5678 ZXROSNG(config-isakmp-key-set-pre-shared-key)#exitZXROSNG(config-isakmp-key-set)#show this!<isakmp>  pre-shared key fqdn 1234    key encrypted 9hvFkSGkois=  $  pre-shared key ipv4-address 1.1.1.1 netmask 255.255.255.0    key encrypted H67q6/ZZYLQ=  $!</isakmp>ZXROSNG(config-isakmp-key-set)#
相关命令 : 
keykey encrypted
## pre-shared key ipv6-address 

pre-shared key ipv6-address 
命令功能 : 
配置预共享密钥。 
命令模式 : 
 ISAKMP密钥集模式  
命令默认权限级别 : 
15 
命令格式 : 
pre-shared key ipv6-address 
  ＜peer-ipv6-address 
＞ [vrf-name 
 ＜ipv6-vrf-name 
＞]
no pre-shared key ipv6-address 
  ＜peer-ipv6-address 
＞ [vrf-name 
 ＜ipv6-vrf-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜peer-ipv6-address＞|ISAKMP协商对端的IPv6地址和掩码
vrf-name|配置携带vrf-name
＜ipv6-vrf-name＞|ISAKMP协商对端为IPv6地址所在的VRF
缺省 : 
无 
使用说明 : 
进入ISAKMP密钥集预共享密钥配置模式，可以根据IP地址或者、FQDN等来配置预共享密钥。如果为一个子网地址设置预共享密钥，则此子网范围内的任何主机都可以采用此预共享密钥。每一个ISAKMP 密钥集可以配置100组预共享密钥。
范例 : 
假设在路由器R1上要设定IKE协商的预共享密钥并显示，则路由器R1上的配置示例如下：ZXROSNG(config-isakmp-key-set)#pre-shared key ipv6-address 1::1/24 ZXROSNG(config-isakmp-key-set-pre-shared-key)#key 234ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
keykey encrypted
## pre-shared key key-id 

pre-shared key key-id 
命令功能 : 
配置预共享密钥 
命令模式 : 
 ISAKMP密钥集模式  
命令默认权限级别 : 
15 
命令格式 : 
pre-shared key key-id 
  ＜key-identity 
＞ [vrf-name 
 ＜key-id-vrf-name 
＞]
no pre-shared key key-id 
  ＜key-identity 
＞ [vrf-name 
 ＜key-id-vrf-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜key-identity＞|key-id类型的ID
vrf-name|配置vrf-name
＜key-id-vrf-name＞|key-id类型的ID所在的VRF
缺省 : 
无 
使用说明 : 
进入ISAKMP密钥集预共享密钥配置模式，可以根据IP地址或者、FQDN等来配置预共享密钥。如果为一个子网地址设置预共享密钥，则此子网范围内的任何主机都可以采用此预共享密钥。每一个ISAKMP 密钥集可以配置100组预共享密钥。
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key key-id 1234566deeeZXROSNG(config-isakmp-key-set-pre-shared-key)#key 887ZXROSNG(config-isakmp-key-set-pre-shared-key)#exitZXROSNG(config-isakmp-key-set)#
相关命令 : 
keykey encrypted
## pre-shared key user-fqdn 

pre-shared key user-fqdn 
命令功能 : 
配置预共享密钥。 
命令模式 : 
 ISAKMP密钥集模式  
命令默认权限级别 : 
15 
命令格式 : 
pre-shared key user-fqdn 
  ＜username-domain 
＞ [vrf-name 
 ＜user-fqdn-vrf-name 
＞]
no pre-shared key user-fqdn 
  ＜username-domain 
＞ [vrf-name 
 ＜user-fqdn-vrf-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜username-domain＞|user-fqdn类型的ID
vrf-name|配置vrf-name
＜user-fqdn-vrf-name＞|user-fqdn类型的ID所在的VRF
缺省 : 
无 
使用说明 : 
进入ISAKMP密钥集预共享密钥配置模式，可以根据IP地址或者、FQDN等来配置预共享密钥。如果为一个子网地址设置预共享密钥，则此子网范围内的任何主机都可以采用此预共享密钥。每一个ISAKMP 密钥集可以配置100组预共享密钥。
范例 : 
ZXROSNG(config)#isakmp key-set 1ZXROSNG(config-isakmp-key-set)#pre-shared key user-fqdn 123ddZXROSNG(config-isakmp-key-set-pre-shared-key)#key 345ZXROSNG(config-isakmp-key-set-pre-shared-key)#exit
相关命令 : 
keykey encrypted
## prf 

prf 
命令功能 : 
指定IKE策略的prf算法 
命令模式 : 
 ISAKMP模式  
命令默认权限级别 : 
15 
命令格式 : 
prf 
  ＜pseudo-random function 
＞
no prf 
命令参数解释 : 
参数|描述
---|---
＜pseudo-random function＞|prf算法，支持配置md5，sha1，sha256，sha384，sha512
缺省 : 
缺省方式是sha1 
使用说明 : 
此命令支持在isakmp policy下分级配置，用来指明IKE协商第一阶段中的当前策略的prf算法 
范例 : 
假设在路由器R1上已经创建IKE安全策略“1”，设定该安全策略的prf算法，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp policy 1ZXROSNG(config-isakmp-1)#prf md5ZXROSNG(config-isakmp-1)#show this!<isakmp>  prf md5!</isakmp>ZXROSNG(config-isakmp-1)#no prfZXROSNG(config-isakmp-1)#show thisZXROSNG(config-isakmp-1)#
相关命令 : 
isakmp policyshow isakmp policy
## rekey authentication 

rekey authentication 
命令功能 : 
设定Key server的rekey绑定的RSA密钥对  
命令模式 : 
 IPsec-GDOI-server模式  
命令默认权限级别 : 
15 
命令格式 : 
rekey authentication 
 keypair 
 ＜Keypair name 
＞
no rekey authentication 
命令参数解释 : 
参数|描述
---|---
＜Keypair name＞|Keypair的命令，<1-15>个字符
缺省 : 
默认值为3des
使用说明 : 
该命令用来配置Key Server的rekey的绑定PKI的keypair名。 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)# rekey authentication keypair 123ZXROSNG(config-ipsec-gdoi-server)#exit
相关命令 : 
crypto ipsec gdoi-server 
## rekey encryption 

rekey encryption 
命令功能 : 
设定Key server的rekey加密算法 
命令模式 : 
 IPsec-GDOI-server模式  
命令默认权限级别 : 
15 
命令格式 : 
rekey encryption 
  ＜algorithm-name 
＞
no rekey encryption 
命令参数解释 : 
参数|描述
---|---
＜algorithm-name＞|取值为3des，des，aes-128，aes-192，aes-256,默认值为3des
缺省 : 
默认值为3des
使用说明 : 
该命令用来配置Key Server的rekey的加密算法，支持的加密算法为3des，des，aes-128，aes-192，aes-256。默认值为3des 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)# rekey encryption desZXROSNG(config-ipsec-gdoi-server)#exit
相关命令 : 
crypto ipsec gdoi-server 
## rekey lifetime 

rekey lifetime 
命令功能 : 
设定Key server的rekey的生命期 
命令模式 : 
 IPsec-GDOI-server模式  
命令默认权限级别 : 
15 
命令格式 : 
rekey lifetime 
 seconds 
 ＜seconds 
＞
no rekey lifetime 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|生命期时间，单位为秒，范围为300-86400
缺省 : 
默认值为86400s
使用说明 : 
该命令用来配置Key Server的的rekey的生命期。 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)# rekey lifetime seconds 1000ZXROSNG(config-ipsec-gdoi-server)#exit
相关命令 : 
crypto ipsec gdoi-server 
## rekey multicast-address 

rekey multicast-address 
命令功能 : 
设定Key server的组播的ipv4地址，发送rekey报文时候，目的地址填写为该地址 
命令模式 : 
 IPsec-GDOI-server模式  
命令默认权限级别 : 
15 
命令格式 : 
rekey multicast-address 
 ipv4-address 
 ＜ipv4-address 
＞
no rekey multicast-address 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|组播组的组地址
缺省 : 
无 
使用说明 : 
该命令用来配置KS的组播地址。暂时只支持配置一个组。发送rekey报文时候，目的地址填写为该地址 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)# rekey muticast-address  ipv4-address 225.0.0.1ZXROSNG(config-ipsec-gdoi-server)#exit
相关命令 : 
crypto ipsec gdoi-server 
## remote 

remote 
命令功能 : 
指明IPsec传输接口的对端地址。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
remote 
  {ipv4-address 
 ＜remote-ipv4-address 
＞|ipv6-address 
 ＜peer-ipv6-address 
＞}
no remote 
命令参数解释 : 
参数|描述
---|---
＜remote-ipv4-address＞|指明具体的IP地址
＜peer-ipv6-address＞|指明具体的IPv6地址
缺省 : 
无 
使用说明 : 
配置传输接口的对端地址。本地地址类型需要和配置描述中的访问列表类型匹配。
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#remote ipv4-address 2.2.2.2ZXROSNG(config-ipsec-transport1)#show this!<ipsec>  remote ipv4-address 2.2.2.2!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
local ipv4-address 
## responder-only 

responder-only 
命令功能 : 
指定IPsec隧道接口被动响应对方协商。 
命令模式 : 
 IPsec静态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
responder-only 
 
no responder-only 
命令参数解释 : 
					无
				 
缺省 : 
缺省为该功能关闭。 
使用说明 : 
IPsec隧道接口主动与对端协商，如果只想被动接受协商，可以通过本命令进行设置。 
范例 : 
假设在路由器R1上要为配置名为profile1的IPsec profile设置responder-only功能，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile profile1ZXROSNG(config-ipsec-static-profile)#responder-onlyZXROSNG(config-ipsec-static-profile)#exitZXROSNG(config)#show crypto ipsec profile profile1Crypto IPsec profile "profile1"   Access list                   : not configure    Profile type                  : static  Security association lifetime : 1843200000 kilobytes / 28800 seconds  Anti-replay flag              : enable  Anti-replay win_size          : 2048  Anti-replay max_seq           : 4294967295  DH group                      : none  PFS level(none/key-identity)  : none  Transform-sets                : {                                  }  Responder-only (Y/N)          : Y
相关命令 : 
show crypto ipsec profilecrypto ipsec static-profile
## reverse-route 

reverse-route 
命令功能 : 
用户上线时分配地址，为分配的地址添加路由。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
reverse-route 
 
no reverse-route 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
IPsec远程用户接入时，IPsec 网关为用户分配IP地址，该地址通常为一个私网地址，正常情况下，网关上是没有通往该私网地址的路由。当配置reverse-route时，则动态地为分配IP地址生成路由。 
范例 : 
ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)# reverse-routeZXROSNG(config-ipsec-if-ipsec_tunnel1)#show this!<ipsec>  type dynamicisakmp-profile 1reverse-route!</ipsec>ZXROSNG(config-ipsec-if-ipsec_tunnel1)#
相关命令 : 
无 
## sa 

sa 
命令功能 : 
增加绑定的ipsec sa 
命令模式 : 
 IPsec-GDOI-server模式  
命令默认权限级别 : 
15 
命令格式 : 
sa 
 ipsec 
 ＜1-65535 
＞
no sa 
 ipsec 
 ＜1-65535 
＞
				
命令参数解释 : 
参数|描述
---|---
＜1-65535＞|ipsec sa索引号
缺省 : 
无 
使用说明 : 
该命令用来配置KS增加绑定的ipsec sa，no sa ipsec <1-65535>删除配置，暂时支持一个server绑定10个ipsec sa。 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)# sa ipsec 1ZXROSNG(config-ipsec-gdoi-server-sa)#exit
相关命令 : 
crypto ipsec gdoi-server 
## self-identity 

self-identity 
命令功能 : 
设定IKE协商本端身份类型。 
命令模式 : 
 ISAKMP描述模式  
命令默认权限级别 : 
15 
命令格式 : 
self-identity 
  {address 
|hostname 
}
no self-identity 
命令参数解释 : 
参数|描述
---|---
address|IP地址
hostname|主机名
缺省 : 
缺省方式是IKE协商的身份类型为address。 
使用说明 : 
设定IKE协商本端身份类型。 
范例 : 
ZXROSNG(config)#isakmp profile 1ZXROSNG(config-isakmp-profile)#self-identity hostname ZXROSNG(config-isakmp-profile)#show this!<isakmp>  self-identity hostname!</isakmp>ZXROSNG(config-isakmp-profile)#
相关命令 : 
无 
## set anti-replay 

set anti-replay 
命令功能 : 
为IPsec配置描述指定抗重放策略。 
命令模式 : 
 IPsec静态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set anti-replay 
  {disable 
|enable 
|window-size 
 ＜set-replay-window-size 
＞|max-sequence 
 ＜set-repaly-maximum-sequence 
＞}
no set anti-replay 
  {window-size 
|max-sequence 
}
				
命令参数解释 : 
参数|描述
---|---
disable|关闭抗重放功能
enable|开启抗重放功能
＜set-replay-window-size＞|设置抗重放的窗口大小，取值范围为 <32-2048>
＜set-repaly-maximum-sequence＞|设置抗重放的最大序列号，取值范围为 <1000-4294967295>
No参数|描述
---|---
window-size|窗口大小
max-sequence|最大序列号
缺省 : 
开启抗重放功能，最大序列号为4294967295，窗口为2048。 
使用说明 : 
开启与关闭功能没有no命令，抗重放功能关闭后，最大序列号和窗口大小无效。manual类型的配置描述不能使用该命令。
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该策略指定生命期，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile myprofileZXROSNG(config-ipsec-static-profile)#set anti-replay window-size 36ZXROSNG(config-ipsec-static-profile)#no set anti-replay window-sizeZXROSNG(config-ipsec-static-profile)#set anti-replay max-sequence 20000ZXROSNG(config-ipsec-static-profile)#no set anti-replay max-sequence
相关命令 : 
show crypto ipsec profilecrypto ipsec static-profile
## set anti-replay 

set anti-replay 
命令功能 : 
为IPsec动态配置描述指定抗重放策略。 
命令模式 : 
 IPsec动态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set anti-replay 
  {disable 
|enable 
|window-size 
 ＜set-replay-window-size 
＞|max-sequence 
 ＜set-repaly-maximum-sequence 
＞}
no set anti-replay 
  {window-size 
|max-sequence 
}
				
命令参数解释 : 
参数|描述
---|---
disable|关闭抗重放功能
enable|开启抗重放功能
＜set-replay-window-size＞|设置抗重放的窗口大小，取值范围为 <32-2048>
＜set-repaly-maximum-sequence＞|设置抗重放的最大序列号，取值范围为 <1000-4294967295>
No参数|描述
---|---
window-size|窗口大小
max-sequence|最大序列号
缺省 : 
开启抗重放功能，最大序列号为4294967295，窗口为2048。 
使用说明 : 
开启与关闭功能没有no命令，抗重放功能关闭后，最大序列号和窗口大小无效。 
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该策略指定生命期，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec dynamic-profile myprofileZXROSNG(config-ipsec-dynamic-profile)#set anti-replay window-size 36ZXROSNG(config-ipsec-dynamic-profile)#no set anti-replay window-sizeZXROSNG(config-ipsec-dynamic-profile)#set anti-replay max-sequence 20000ZXROSNG(config-ipsec-dynamic-profile)#no set anti-replay max-sequence
相关命令 : 
show crypto ipsec profilecrypto ipsec dynamic-profile
## set gdoi-group 

set gdoi-group 
命令功能 : 
在transport上绑定 GDOI group。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
set gdoi-group 
  ＜GDOI group name 
＞
no set gdoi-group 
命令参数解释 : 
参数|描述
---|---
＜GDOI group name＞|GDOI group 名称
缺省 : 
无 
使用说明 : 
该命令用来指定IPsec GDOI安全策略引用的GDOI组。no set gdoi-group命令用来删除IPsec GDOI安全策略引用的GDOI组。缺省情况下，IPsec GDOI安全策略没有引用任何GDOI组。一个IPsec GDOI安全策略只能引用一个GDOI组，最后一次配置生效。 
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-group testZXROSNG(config-ipsec-gdoi-group)#!ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#set gdoi-group testZXROSNG(config-ipsec-transport1)#
相关命令 : 
crypto ipsec gdoi-group test 
## set mode 

set mode 
命令功能 : 
指明IPsec transport模式 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
set mode 
  {ipv4 
|ipv6 
}
命令参数解释 : 
参数|描述
---|---
ipv4|指明传输模式为IPv4
ipv6|指明传输模式为IPv6
缺省 : 
无 
使用说明 : 
此命令为扩展需要，可以不被配置。 
范例 : 
ZXROSNG(config-ipsec-transport1)# set mode ipv6 
相关命令 : 
无 
## set pfs 

set pfs 
命令功能 : 
为IPsec配置描述指定PFS群。 
命令模式 : 
 IPsec静态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set pfs 
  {group1 
|group2 
|group5 
}
no set pfs 
命令参数解释 : 
参数|描述
---|---
group1|DH组1
group2|DH组2
group5|DH组5
缺省 : 
无 
使用说明 : 
该命令与set pfslevel一起使用，指明PFS使用的DH组。manual类型的配置描述不能使用该命令。
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该策略指定PFS群，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile myprofileZXROSNG(config-ipsec-static-profile)#set pfs group1ZXROSNG(config-ipsec-static-profile)#no set pfs
相关命令 : 
crypto ipsec static-profileshow crypto ipsec profileset pfslevel
## set pfs 

set pfs 
命令功能 : 
为IPsec配置描述指定PFS群。 
命令模式 : 
 IPsec动态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set pfs 
  {group1 
|group2 
|group5 
}
no set pfs 
命令参数解释 : 
参数|描述
---|---
group1|DH组1
group2|DH组2
group5|DH组5
缺省 : 
无 
使用说明 : 
指明PFS使用的DH组。 
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该策略指定PFS群，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec dynamic-profile myprofileZXROSNG(config-ipsec-dynamic-profile)#set pfs group1ZXROSNG(config-ipsec-dynamic-profile)#no set pfs
相关命令 : 
crypto ipsec dynamic-profileshow crypto ipsec profileset pfslevel
## set pfslevel 

set pfslevel 
命令功能 : 
为IPsec配置描述指定PFS保护类型。 
命令模式 : 
 IPsec静态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set pfslevel 
 key-identity 
no set pfslevel 
命令参数解释 : 
参数|描述
---|---
key-identity|指定PFS保护类型为key identity类型
缺省 : 
缺省方式不设置pfslevel。 
使用说明 : 
manual类型的配置描述不能使用该命令。如果设定为key-identity，第一阶段协商必须使用主模式，而且只能为一个数据流提供保护，也就是说ACL中只能有一个规则。 
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该策略指定PFS保护类型，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile myprofileZXROSNG(config-ipsec-static-profile)#set pfslevel key-identity ZXROSNG(config-ipsec-static-profile)#no set pfslevel
相关命令 : 
crypto ipsec static-profileshow crypto ipsec profileset pfs
## set pfslevel 

set pfslevel 
命令功能 : 
为IPsec配置描述指定PFS保护类型。 
命令模式 : 
 IPsec动态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set pfslevel 
 key-identity 
no set pfslevel 
命令参数解释 : 
参数|描述
---|---
key-identity|指定PFS保护类型为key identity类型
缺省 : 
无 
使用说明 : 
如果设定为key-identity，第一阶段协商必须使用主模式，而且只能为一个数据流提供保护，也就是说ACL中只能有一个规则。 
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该策略指定PFS保护类型，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec dynamic-profile myprofileZXROSNG(config-ipsec-dynamic-profile)#set pfslevel key-identityZXROSNG(config-ipsec-dynamic-profile)#no set pfslevel
相关命令 : 
crypto ipsec dynamic-profileshow crypto ipsec profileset pfs
## set sa 

set sa 
命令功能 : 
为IPsec配置描述指定生命周期。 
命令模式 : 
 IPsec静态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set sa 
 lifetime 
 {kilobytes 
 ＜lifetime-in-kilobytes 
＞|seconds 
 ＜lifetime-in-seconds 
＞}
no set sa 
 lifetime 
 {kilobytes 
|seconds 
}
				
命令参数解释 : 
参数|描述
---|---
＜lifetime-in-kilobytes＞|生命期，单位：千字节，取值范围2560-4294900000；缺省值1843200000
＜lifetime-in-seconds＞|生命期，单位：秒，取值范围120-86400；缺省值为28800秒
No参数|描述
---|---
kilobytes|字节生命期
seconds|时间生命期
缺省 : 
缺省方式是全局配置的生命期。 
使用说明 : 
manual类型的配置描述不能使用该命令。时间生命期的范围是：120-864000 秒（10天），字节生命期的范围是：256-4,294,900,000 千字节。 
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该描述指定生命期，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile myprofileZXROSNG(config-ipsec-static-profile)#set sa lifetime seconds 10000ZXROSNG(config-ipsec-static-profile)#no set sa lifetime secondsZXROSNG(config-ipsec-static-profile)#set sa lifetime kilobytes 20000ZXROSNG(config-ipsec-static-profile)#no set sa lifetime kilobytes
相关命令 : 
crypto ipsec sa global-lifetimecrypto ipsec static-profileshow crypto ipsec profile
## set sa 

set sa 
命令功能 : 
为IPsec配置描述指定生命周期。 
命令模式 : 
 IPsec动态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set sa 
 lifetime 
 {kilobytes 
 ＜lifetime-in-kilobytes 
＞|seconds 
 ＜lifetime-in-seconds 
＞}
no set sa 
 lifetime 
 {kilobytes 
|seconds 
}
				
命令参数解释 : 
参数|描述
---|---
＜lifetime-in-kilobytes＞|生命期，单位：千字节，取值范围2560-4294900000；缺省值1843200000
＜lifetime-in-seconds＞|生命期，单位：秒，取值范围120-86400；缺省值为28800秒
No参数|描述
---|---
kilobytes|字节生命期
seconds|时间生命期
缺省 : 
默认时间生命期为28800秒；字节生命期为1843200000KByte 
使用说明 : 
时间生命期的范围是：120-864000 秒（10天），字节生命期的范围是：256-4,294,900,000 千字节。 
范例 : 
假设在路由器R1上已经创建IPsec的安全描述myprofile，为该描述指定生命期，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec dynamic-profile myprofileZXROSNG(config-ipsec-dynamic-profile)#set sa lifetime seconds 10000ZXROSNG(config-ipsec-dynamic-profile)#no set sa lifetime secondsZXROSNG(config-ipsec-dynamic-profile)#set sa lifetime kilobytes 20000ZXROSNG(config-ipsec-dynamic-profile)#no set sa lifetime kilobytes
相关命令 : 
crypto ipsec dynamic-profileshow crypto ipsec profile
## set sa 

set sa 
命令功能 : 
配置gdoi profile下的sa的生命期 
命令模式 : 
 IPsec-GDOI描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set sa 
 lifetime 
 seconds 
 ＜lifetime-in-seconds 
＞
no set sa 
 lifetime 
 seconds 
命令参数解释 : 
参数|描述
---|---
＜lifetime-in-seconds＞|生命期，单位：秒，取值范围120-86400；缺省值为86400秒
No参数|描述
---|---
seconds|生命期秒
缺省 : 
86400秒。 
使用说明 : 
时间生命期的范围是：120-864000 秒（10天）。
范例 : 
假设在路由器R1上已经创建IPsec的GDOI描述myprofile，为该描述指定生命期，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec gdoi-profile myprofileZXROSNG(config-ipsec-gdoi-profile)#set sa lifetime seconds 10000ZXROSNG(config-ipsec-gdoi-profile)#no set sa lifetime seconds
相关命令 : 
crypto ipsec gdoi-profileshow crypto ipsec profile
## set sa-level per-host 

set sa-level per-host 
命令功能 : 
指明传输模式下SA协商的粒度 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
set sa-level per-host 
 
no set sa-level per-host 
命令参数解释 : 
					无
				 
缺省 : 
匹配同一条ACL规则的流量共享一个IPsec SA 
使用说明 : 
默认配置下，匹配同一条ACL规则的流量共享一个IPsec SA。如果需要为每一个流创建单独的IPsec SA，可以配置本命令。 
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#set sa-level per-hostZXROSNG(config-ipsec-transport1)#no set sa-level per-host
相关命令 : 
无 
## set session-key inbound 

set session-key inbound 
命令功能 : 
为手工类型的profile设置入向SPI和密钥。 
命令模式 : 
 IPsec手工描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set session-key inbound 
  {ah 
 ＜ah-spi 
＞ {string 
 ＜ah-key-string 
＞|hex 
 ＜ah-key-hex 
＞|encrypted 
 {string 
 ＜ah-key-encrypt-string 
＞|hex 
 ＜ah-key-encrypt-hex 
＞}}|esp 
 ＜esp-spi 
＞ {{[authenticator 
 {string 
 ＜esp-authentication-key-string 
＞|hex 
 ＜esp-authentication-key-hex 
＞|encrypted 
 {string 
 ＜esp-auth-key-encrypt-string 
＞|hex 
 ＜esp-auth-key-encrypt-hex 
＞}}],[cipher 
 {string 
 ＜esp-cipher-key-string 
＞|hex 
 ＜esp-cipher-key-hex 
＞|encrypted 
 {string 
 ＜esp-cipher-key-encrypt-string 
＞|hex 
 ＜esp-cipher-key-encrypt-hex 
＞}}]}|to 
 ＜esp-spi 
＞ quantum-key 
 ＜quantum-key-profile 
＞}}
no set session-key inbound 
  {ah 
|esp 
}
				
命令参数解释 : 
参数|描述
---|---
ah|指明会话密钥为AH协议的密钥
＜ah-spi＞|指明AH会话密钥的SPI值
＜ah-key-string＞|指明AH会话密钥输入方式为字符串方式的密钥
＜ah-key-hex＞|指明AH会话密钥输入方式为16进制的密钥
＜ah-key-encrypt-string＞|指明AH会话密钥输入方式为密文字符串方式的密钥
＜ah-key-encrypt-hex＞|指明AH会话密钥输入方式为密文16进制的密钥
esp|指明会话密钥为ESP协议的密钥
＜esp-spi＞|指明ESP会话密钥的SPI值
＜esp-authentication-key-string＞|指明ESP会话密钥输入方式为字符串方式的认证密钥
＜esp-authentication-key-hex＞|指明ESP会话密钥输入方式为16进制的认证密钥
＜esp-auth-key-encrypt-string＞|指明ESP会话密钥输入方式为密文字符串方式的认证密钥
＜esp-auth-key-encrypt-hex＞|指明ESP会话密钥输入方式为密文16进制的认证密钥
＜esp-cipher-key-string＞|指明ESP会话密钥输入方式为字符串方式的加密密钥
＜esp-cipher-key-hex＞|指明ESP会话密钥输入方式为16进制的加密密钥
＜esp-cipher-key-encrypt-string＞|指明ESP会话密钥输入方式为密文字符串方式的加密密钥
＜esp-cipher-key-encrypt-hex＞|指明ESP会话密钥输入方式为密文16进制的加密密钥
＜esp-spi＞|指明ESP会话密钥的SPI值
＜quantum-key-profile＞|量子密钥描述文件描述文件信息主要用于与量子密钥服务器建立连接和读取密钥处理
缺省 : 
无 
使用说明 : 
只有manual类型的IPsec配置描述使用该命令。设置的条件是配置描述已经被创建，引用的转码也必须设定。协议和密钥的设置必须与转码对应，也就是说转码包含了AH，才能设置AH的SPI和密钥。密钥的长度必须与转码中设置算法对应。在配置时，需要先配置转码，才能配置密钥。hex和string设置的范围根据密钥具体协议而定。一个SPI值只能使用一次，即如果一个手工profile配置了该SPI值，那么OSPFv6不能再使用。 
范例 : 
假设在路由器R1上已经创建IPsec的手动的安全描述myprofile，为该策略指定SPI和密钥，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec transform-set mytrans        ZXROSNG(config-crypto-trans)#algorithm esp-des ZXROSNG(config-crypto-trans)#exitZXROSNG(config)#crypto ipsec manual-profile myprofileZXROSNG(config-ipsec-manual-profile)#set transform-set mytransZXROSNG(config-ipsec-manual-profile)#set session-key inbound esp 3350 cipher hex 0102030405060708090001020304050607080900ZXROSNG(config-ipsec-manual-profile)#set session-key outbound esp 3360 cipher hex 0102030405060708090001020304050607080900
相关命令 : 
show crypto ipsec profilecrypto ipsec manual-profilecrypto ipsec transform-set
## set session-key outbound 

set session-key outbound 
命令功能 : 
为手工类型的profile设置出向SPI和密钥。 
命令模式 : 
 IPsec手工描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set session-key outbound 
  {ah 
 ＜ah-spi 
＞ {string 
 ＜ah-key-string 
＞|hex 
 ＜ah-key-hex 
＞|encrypted 
 {string 
 ＜ah-key-encrypt-string 
＞|hex 
 ＜ah-key-encrypt-hex 
＞}}|esp 
 ＜esp-spi 
＞ {{[authenticator 
 {string 
 ＜esp-authentication-key-string 
＞|hex 
 ＜esp-authentication-key-hex 
＞|encrypted 
 {string 
 ＜esp-auth-key-encrypt-string 
＞|hex 
 ＜esp-auth-key-encrypt-hex 
＞}}],[cipher 
 {string 
 ＜esp-cipher-key-string 
＞|hex 
 ＜esp-cipher-key-hex 
＞|encrypted 
 {string 
 ＜esp-cipher-key-encrypt-string 
＞|hex 
 ＜esp-cipher-key-encrypt-hex 
＞}}]}|to 
 ＜esp-spi 
＞ quantum-key 
 ＜quantum-key-profile 
＞}}
no set session-key outbound 
  {ah 
|esp 
}
				
命令参数解释 : 
参数|描述
---|---
ah|指明会话密钥为AH协议的密钥
＜ah-spi＞|指明AH会话密钥的SPI值
＜ah-key-string＞|指明AH会话密钥输入方式为字符串方式的密钥
＜ah-key-hex＞|指明AH会话密钥输入方式为16进制的密钥
＜ah-key-encrypt-string＞|指明AH会话密钥输入方式为密文字符串方式的密钥
＜ah-key-encrypt-hex＞|指明AH会话密钥输入方式为密文16进制的密钥
esp|指明会话密钥为ESP协议的密钥
＜esp-spi＞|指明ESP会话密钥的SPI值
＜esp-authentication-key-string＞|指明ESP会话密钥输入方式为字符串方式的认证密钥
＜esp-authentication-key-hex＞|指明ESP会话密钥输入方式为16进制的认证密钥
＜esp-auth-key-encrypt-string＞|指明ESP会话密钥输入方式为密文字符串方式的认证密钥
＜esp-auth-key-encrypt-hex＞|指明ESP会话密钥输入方式为密文16进制的认证密钥
＜esp-cipher-key-string＞|指明ESP会话密钥输入方式为字符串方式的加密密钥
＜esp-cipher-key-hex＞|指明ESP会话密钥输入方式为16进制的加密密钥
＜esp-cipher-key-encrypt-string＞|指明ESP会话密钥输入方式为密文字符串方式的加密密钥
＜esp-cipher-key-encrypt-hex＞|指明ESP会话密钥输入方式为密文16进制的加密密钥
＜esp-spi＞|指明ESP会话密钥的SPI值
＜quantum-key-profile＞|量子密钥描述文件描述文件信息主要用于与量子密钥服务器建立连接和读取密钥处理
缺省 : 
无 
使用说明 : 
只有manual类型的IPsec配置描述使用该命令。设置的条件是配置描述已经被创建，引用的转码也必须设定。协议和密钥的设置必须与转码对应，也就是说转码包含了AH，才能设置AH的SPI和密钥。密钥的长度必须与转码中设置算法对应。在配置时，需要先配置转码，才能配置密钥。hex和string设置的范围根据密钥具体协议而定。一个SPI值只能使用一次，即如果一个手工profile配置了该SPI值，那么OSPFv6不能再使用。 
范例 : 
假设在路由器R1上已经创建IPsec的手动的安全描述myprofile，为该策略指定SPI和密钥，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec transform-set mytrans        ZXROSNG(config-crypto-trans)#algorithm esp-des ZXROSNG(config-crypto-trans)#exitZXROSNG(config)#crypto ipsec manual-profile myprofileZXROSNG(config-ipsec-manual-profile)#set transform-set mytransZXROSNG(config-ipsec-manual-profile)#set session-key inbound esp 3350 cipher hex 0102030405060708090001020304050607080900ZXROSNG(config-ipsec-manual-profile)#set session-key outbound esp 3360 cipher hex 0102030405060708090001020304050607080900
相关命令 : 
show crypto ipsec profilecrypto ipsec manual-profilecrypto ipsec transform-set
## set transform-set 

set transform-set 
命令功能 : 
为IPsec配置描述指定或者删除转码集。 
命令模式 : 
 IPsec静态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set transform-set 
  ＜proposal-tag 
＞ [＜proposal-tag 
＞ [＜proposal-tag 
＞ [＜proposal-tag 
＞ [＜proposal-tag 
＞ [＜proposal-tag 
＞]]]]]
no set transform-set 
命令参数解释 : 
参数|描述
---|---
＜proposal-tag＞|转码集名称
＜proposal-tag＞|转码集名称
＜proposal-tag＞|转码集名称
＜proposal-tag＞|转码集名称
＜proposal-tag＞|转码集名称
＜proposal-tag＞|转码集名称
缺省 : 
无 
使用说明 : 
设置的条件是配置描述已经被创建，转码集也已经建立。static类型的配置描述能设定六个转码集。IPsec配置描述下不能配置传输模式的转码集。当手工profile配置了SPI和密钥时，不能修改或删除转码集引用。
范例 : 
假设在路由器R1上已经创建IPsec的安全描述123，为该描述配置转码集，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec static-profile 123 ZXROSNG(config-ipsec-static-profile)#set transform-set mytransZXROSNG(config-ipsec-static-profile)#no set transform-set
相关命令 : 
show crypto ipsec profileshow crypto ipsec transform-setcrypto ipsec static-profilecrypto ipsec manual-profilecrypto ipsec transform-set
## set transform-set 

set transform-set 
命令功能 : 
为安全策略或者IPsec配置描述指定或者删除转码集。 
命令模式 : 
 IPsec手工描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set transform-set 
  ＜proposal-tag 
＞
no set transform-set 
命令参数解释 : 
参数|描述
---|---
＜proposal-tag＞|转码集名称，用字符串表示，长度不能超过18个字符，最多可配置6个转码集。
缺省 : 
无 
使用说明 : 
设置的条件是策略/配置描述已经被创建，转码集也已经建立。manual类型的策略/配置描述只能设定一个转码集，其他类型可设置最多6个转码集。IPsec配置描述下不能配置传输模式的转码集。当手工profile配置了SPI和密钥时，不能修改或删除转码集引用。
范例 : 
假设在路由器R1上已经创建IPsec的手工profile：myprofile，为该策略配置转码集，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec manual-profile myprofileZXROSNG(config-ipsec-manual-profile)#set transform-set mytransZXROSNG(config-ipsec-manual-profile)#no set transform-set 
相关命令 : 
show crypto ipsec profileshow crypto ipsec transform-setcrypto ipsec manual–profilecrypto ipsec transform-set
## set transform-set 

set transform-set 
命令功能 : 
为IPsec动态配置描述指定或者删除转码集。 
命令模式 : 
 IPsec动态描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set transform-set 
  ＜proposal-tag 
＞
no set transform-set 
  ＜proposal-tag 
＞
				
命令参数解释 : 
参数|描述
---|---
＜proposal-tag＞|转码集名称，用字符串表示，长度不能超过18个字符
缺省 : 
无 
使用说明 : 
设置的条件是策略/配置描述已经被创建，转码集也已经建立。配置IPsec动态Profile的转码集，此转码集必须先被创建，否则会有错误提示。一个IPsec动态Profile下最多可以配置20个转码集。该Profile被隧道绑定也能配置。 
范例 : 
ZXROSNG(config)#crypto ipsec dynamic-profile 1ZXROSNG(config-ipsec-dynamic-profile)#set transform-set DES3ZXROSNG(config-ipsec-dynamic-profile)#set transform-set DESZXROSNG(config-ipsec-dynamic-profile)#show crypto ipsec profile Crypto IPsec profile "1"   Access list                   : not configure    Profile type                  : dynamic  Security association lifetime : 1843200000 kilobytes / 28800 seconds  Anti-replay flag              : enable  Anti-replay win_size          : 2048  Anti-replay max_seq           : 4294967295  DH group                      : none  PFS level(none/key-identity)  : none  Transform-sets                : {DES,                                   DES3                                  }  Responder-only (Y/N)          : YZXROSNG(config-ipsec-dynamic-profile)#
相关命令 : 
crypto ipsec transform-set 
## set transform-set 

set transform-set 
命令功能 : 
配置gdoi profile下绑定的指定或者删除转码集。 
命令模式 : 
 IPsec-GDOI描述模式  
命令默认权限级别 : 
15 
命令格式 : 
set transform-set 
  ＜proposal-tag 
＞
no set transform-set 
命令参数解释 : 
参数|描述
---|---
＜proposal-tag＞|转码集名称，用字符串表示，长度不能超过18个字符。
缺省 : 
无 
使用说明 : 
设置的条件是策略/配置描述已经被创建，转码集也已经建立。GDOI类型的策略/配置描述只能设定一个转码集。
范例 : 
假设在路由器R1上已经创建IPsec的profile：myprofile，为该策略配置转码集，则路由器R1上的配置示例如下：ZXROSNG(config)#crypto ipsec gdoi-profile myprofileZXROSNG(config-ipsec-gdoi-profile)#set transform-set mytransZXROSNG(config-ipsec-gdoi-profile)#no set transform-set
相关命令 : 
show crypto ipsec profileshow crypto ipsec transform-setcrypto ipsec gdoi–profilecrypto ipsec transform-set
## set type 

set type 
命令功能 : 
配置ipsec transport的类型 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
set type 
  {static 
|dynamic 
|manual 
|gdoi 
}
no set type 
命令参数解释 : 
参数|描述
---|---
static|静态模式
dynamic|动态模式
manual|手工模式
gdoi|组加密模式
缺省 : 
静态模式 
使用说明 : 
此命令支持在IPsec-transport模式下配置，用来配置ipsec transport的类型。 
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#set type dynamicZXROSNG(config-ipsec-transport1)#show this !<ipsec>  set type dynamic!</ipsec>ZXROSNG(config-ipsec-transport2)#
相关命令 : 
crypto ipsec-transport  
## show crypto ipsec client group 

show crypto ipsec client group 
命令功能 : 
显示指定组下的所用用户信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec client group 
  ＜group-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|远程用户组名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
显示指定组下的所用用户信息。 
范例 : 
ZXROSNG#show crypto ipsec client group grp10Index Tunnel            Internal-IP     User-group      Remote-IP1     ipsec_tunnel1     192.168.1.1     grp10           10.42.195.174ZXROSNG#
相关命令 : 
clear crypto ipsec client group 
## show crypto ipsec client interface 

show crypto ipsec client interface 
命令功能 : 
显示指定隧道下的所用用户信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec client interface 
  ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|IPsec隧道名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
显示指定隧道下的所用用户信息。 
范例 : 
ZXROSNG#show crypto ipsec client interface ipsec_tunnel1Index Tunnel            Internal-IP     User-group      Remote-IP1     ipsec_tunnel1     192.168.1.1     grp10           10.42.195.174ZXROSNG#
相关命令 : 
clear crypto ipsec client interface 
## show crypto ipsec client user-ip 

show crypto ipsec client user-ip 
命令功能 : 
显示指定隧道下某个IP用户信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec client user-ip 
  ＜internal-ip-address 
＞ interface 
 ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜internal-ip-address＞|远程接入用户分配的IP地址，IPv4类型
＜interface-name＞|远程接入用户接入隧道名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
显示指定隧道下某个IP用户信息。 
范例 : 
ZXROSNG#show crypto ipsec client user-ip 192.168.1.1 interface ipsec_tunnel1Tunnel    : ipsec_tunnel1      Internal-IP: 192.168.1.1       Local     : 101.0.0.100        Remote     : 10.42.195.174     WINS-1    : not configure      WINS-2     : not configure   DNS-1     : 1.2.3.4            DNS-2      : 4.5.6.7           Outer VRF : not configured                  User-group: grp10                            IP-pool   : zte                             ZXROSNG#
相关命令 : 
clear crypto ipsec client user-ip 
## show crypto ipsec gdoi gm 

show crypto ipsec gdoi gm 
命令功能 : 
显示GDOI组员信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec gdoi gm 
  [＜GDOI group name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜GDOI group name＞|GDOI组名
缺省 : 
无 
使用说明 : 
显示指定GDOI组或者所有GDOI组的信息 
范例 : 
ZXROSNG#show crypto ipsec gdoi gmGroup Member Information For Group 1:    Group member             : 55.1.1.2         vrf: None       Registration status   : Registered       Registered with       : 55.1.1.1       Re-registers in       : 3398 sec       Succeeded registration: 1       Attempted registration: 1       Last rekey from       : 0.0.0.0       Last rekey seq num    : 0       Multicast rekey rcvd  : 
相关命令 : 
无 
## show crypto ipsec gdoi ks acl 

show crypto ipsec gdoi ks acl 
命令功能 : 
显示Key server绑定的acl信息
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec gdoi ks acl 
  {all 
|server-name 
 ＜server name 
＞} 
命令参数解释 : 
参数|描述
---|---
all|显示所有key server
server-name|显示指定的key server
＜server name＞|Key server的名字，1-31个字符
缺省 : 
无 
使用说明 : 
显示指定Key server组或者所有Key server组的绑定的acl信息 
范例 : 
ZXROSNG#show crypto ipsec gdoi ks acl allServer Name      :1  Key Server ID  :1.1.1.1  Configured ACL :Access-list a
相关命令 : 
无 
## show crypto ipsec gdoi ks member 

show crypto ipsec gdoi ks member 
命令功能 : 
显示组成员信息
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec gdoi ks member 
  {all 
|gm 
 ＜ip-address 
＞|server-name 
 ＜server name 
＞} 
命令参数解释 : 
参数|描述
---|---
all|显示所有key server
gm|显示指定的GM
＜ip-address＞|GM的IP地址
server-name|显示指定的server
＜server name＞|Key server的名字，1-31个字符
缺省 : 
无 
使用说明 : 
显示指定Key server组或者所有Key server组的绑定的组成员信息
范例 : 
ZXROSNG#show crypto ipsec gdoi ks member allGroup Member ID    : 100.2.0.23Key Server ID     : 100.2.0.30     Identity          : 33.0.0.16     Server Name        : gdoigroup1
相关命令 : 
无 
## show crypto ipsec gdoi ks rekey 

show crypto ipsec gdoi ks rekey 
命令功能 : 
显示rekey信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec gdoi ks rekey 
  {all 
|server-name 
 ＜server name 
＞} 
命令参数解释 : 
参数|描述
---|---
all|显示所有的key server
server-name|显示指定的key server
＜server name＞|Key server的名字，1-31个字符
缺省 : 
无
使用说明 : 
显示指定Key server组的rekey信息 
范例 : 
ZXROSNG#show crypto ipsec gdoi ks rekey allServer  gdoigroup1  local 100.2.0.30：     Group members                           : 2    Rekey count                              : 0    Multicast destination address           : 100.1.0.123    KEK sequence                               : 0    KEK rekey lifetime                    : 86400(s)        Remaining lifetime                    : 452(s)
    IPSec SA 1  lifetime                   : 500(s)        Remaining lifetime                    : 452(s)
    IPSec SA 2  lifetime                       : 500(s)        Remaining lifetime                    : 452(s)
相关命令 : 
无 
## show crypto ipsec gdoi ks sa 

show crypto ipsec gdoi ks sa 
命令功能 : 
显示Key Server上的KEK和TEK的信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec gdoi ks sa 
  {all 
|server-name 
 ＜server name 
＞} 
命令参数解释 : 
参数|描述
---|---
all|显示所有key server
server-name|显示指定的key server
＜server name＞|Key server的名字，1-31个字符
缺省 : 
无 
使用说明 : 
显示指定Key server组或者所有Key server组的绑定的KEK和TEK的信息
范例 : 
ZXROSNG#show crypto ipsec gdoi ks sa all Server Name             :1KEK SA:   KEK sequence         :0   KEK cookie           :b6a9da5844188a24694e3c08133bf298   Encryption algorithm :3des        Remain lifetime      :12345(s)        Sig key name         :1TEK total:1TEK SA <1>:    SPI                      :4079520148   Protocol                 :AH   Access-list              :1    Authentication algorithm :hmac-md5   Encryption algorithm     :not configure   Encapsulation mode       :tunnel   Remain lifetime          :86400(s)
相关命令 : 
无 
## show crypto ipsec gdoi ks server 

show crypto ipsec gdoi ks server 
命令功能 : 
显示Key server下当前的基本信息，主要是配置信息和已注册的成员个数 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec gdoi ks server 
  {all 
|server-name 
 ＜server name 
＞} 
命令参数解释 : 
参数|描述
---|---
all|显示所有key server
server-name|显示指定的key server
＜server name＞|Key server的名字，1-31个字符
缺省 : 
无 
使用说明 : 
显示指定Key server组或者所有Key server组的显示server下当前的基本信息，主要是配置信息和已注册的成员个数 
范例 : 
ZXROSNG#show crypto ipsec gdoi ks server all Server Name             : 1    Identity            : 1    Local IP            : 1.1.1.22    Group members       : 0    Group lifetime      : 12345(s)    Encryption algorithm          : 3des     Multicast destination address : 225.1.0.1    Keypair                       : 1    IPSec SA 1:      IPSec SA lifetime           : 86400(s)      Transform-set               : {ah-md5-hmac},{tunnel}      Access-list                 : 1
相关命令 : 
无 
## show crypto ipsec load-balance interface 

show crypto ipsec load-balance interface 
命令功能 : 
按照接口显示负荷分担信息，主要显示接口名、负荷分担地址、类型、本端地址、对端地址、ACL名字。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec load-balance interface 
  ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|需要显示负荷分担信息的接口名称。
缺省 : 
无 
使用说明 : 
负荷分担发生后，可以使用此命令查看对应接口的负荷分担信息。 
范例 : 
ZXROSNG(config)#show crypto ipsec load-balance interface ipsec_tunnel1 ipsec_tunnel1               Type  : unknown     Local : 0.0.0.0           Peer  : 0.0.0.0           VRF   :                                   CPU   : invalid
相关命令 : 
show crypto ipsec load-balance 
## show crypto ipsec load-balance ipsec-transport 

show crypto ipsec load-balance ipsec-transport 
命令功能 : 
显示IPsec负荷分担信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec load-balance ipsec-transport 
  ＜ipsec-transport-index 
＞ 
命令参数解释 : 
参数|描述
---|---
＜ipsec-transport-index＞|IPsec transport索引，范围：1-$#35586049#$
缺省 : 
无 
使用说明 : 
显示IPsec隧道负荷分担信息，其以接口名为索引显示。如果全为invalid说明目前负荷分担的地址无效。type字段指明了该虚接口的配置类型的，static代表协商静态配置类型，manual代表是手工配置类型，dynamic代表动态配置类型。 
范例 : 
ZXROSNG#show crypto ipsec load-balance ipsec-transport 1ipsec_transport1Type  : unknownLocal : 0.0.0.0Peer  : 0.0.0.0VRF   :CPU   : invalid
相关命令 : 
show crypto ipsec load-balancecrypto ipsec reallocate ipsec-transport
## show crypto ipsec load-balance mode 

show crypto ipsec load-balance mode 
命令功能 : 
显示IPsec负荷分担的模式。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec load-balance mode 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示负荷分担的模式：auto表示自动模式，manual表示手动模式。 
范例 : 
ZXROSNG(config)#show crypto ipsec load-balance modeLoad balance mode : auto
相关命令 : 
crypto ipsec load-balance mode 
## show crypto ipsec load-balance timer 

show crypto ipsec load-balance timer 
命令功能 : 
按照接口显示负荷分担定时器信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec load-balance timer 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示负荷分担定时器信息。 
范例 : 
ZXROSNG(config)#show crypto ipsec load-balance timer Load waiting time:  20 seconds
相关命令 : 
show crypto ipsec load-balance 
## show crypto ipsec load-balance 

show crypto ipsec load-balance 
命令功能 : 
显示IPsec隧道负荷分担信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec load-balance 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示IPsec隧道负荷分担信息，其以接口名为索引显示。如果为invalid说明目前负荷分担的地址无效。 
范例 : 
ZXROSNG#show crypto ipsec load-balance ipsec_tunnel1               Type  : static      Local : 90.1.1.1          Peer  : 90.1.1.2          VRF   :                                   CPU   : spi-0/3/0/1             ipsec_transport1          Type  : dynamic   Local : 80.1.1.1        Peer            VRF             NAT-OAi         CPU160.1.1.1       ipsec1234567890                 spi-0/3/0/1                12345678901234                  161.1.1.1       ipsec1234567890                 spi-0/3/0/1                12345678901234                  162.1.1.1       ipsec1234567890                 spi-0/3/0/1                12345678901234                  164.1.1.1       ipsec1234567890                 spi-0/3/0/1                12345678901234                  ipsec_transport2          Type  : dynamic   Local : 10.42.119.250   Peer            VRF             NAT-OAi         CPU 
相关命令 : 
crypto ipsec load-waiting 
## show crypto ipsec profile 

show crypto ipsec profile 
命令功能 : 
显示所有的或特定的profile信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec profile 
  [＜profile-tag 
＞] 
命令参数解释 : 
参数|描述
---|---
＜profile-tag＞|指明显示的profile名字
缺省 : 
无 
使用说明 : 
按照参数显示全部或者显示某个指定的profile。 
范例 : 
假设在路由器R1上配置了名为profile1的IPsec profile，需显示，则路由器R1上的配置示例如下：ZXROSNG(config)#show crypto ipsec profileCrypto IPsec profile "profile1"Access list                   : 1600Profile type                  : staticSecurity association lifetime : 1843200000 kilobytes / 28800 secondsAnti-replay flag              : enableAnti-replay win_size          : 2048Anti-replay max_seq           : 4294967295DH group                      : nonePFS level(none/key-identity)  : noneTransform-sets                : {1}Responder-only (Y/N)          : NCommit type                   : quick-mode
相关命令 : 
crypto ipsec static-profilecrypto ipsec manual-profileshow crypto ipsec profile
## show crypto ipsec sa 

show crypto ipsec sa 
命令功能 : 
显示IPsec SA。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec sa 
  {manual 
|nego 
} [{interface 
 ＜interface-name 
＞|ipsec-transport 
 ＜transport-number 
＞}] 
命令参数解释 : 
参数|描述
---|---
manual|显示手工配置的sa
nego|显示协商生成的sa
＜interface-name＞|指明显示具体某个接口的sa
＜transport-number＞|指明显示具体某个IPsec transport的sa，范围：1-$#35586049#$
缺省 : 
无 
使用说明 : 
分别显示协商SA和手工SA；如果配置了接口或transport，那么显示该接口或transport下的IPsec SA。 
范例 : 
假设在路由器R1上显示协商SA，则路由器R1上的配置示例如下：ZXROSNG#show crypto ipsec sa nego Interface: ipsec_tunnel2 IKE version               : v2IPsec profile tag:2 Local endpt:101.0.0.25       Current remote endpt: 101.0.0.35 Local  ident(addr/mask/prot/port_min/port_max) :   (1.0.0.0/255.255.255.0/6/50/100) Remote ident(addr/mask/prot/port_min/port_max) :   (1.0.0.0/255.255.255.0/6/50/100) IPsec MTU                 : 1444    FVRF                      : not configure IVRF                      : not configure Pre-fragmentation         : enable Original IP header DF-bit : aware  Tunnel IP header DF-bit   : clear  SA type                   : negotiationRemain lifetime           : 28700(s) Remain inbound throughput : 1843200000(KB) Remain outbound throughput: 1843200000(KB) Inbound ESP SA:  SPI                      : 0x100003d  Authentication algorithm : hmac-sha1  Encryption algorithm     : des  Encapsulation mode       : tunnel  Throughput               : 0KB  Inbound AH SA: Outbound ESP SA:  SPI                      : 0x100003d  Authentication algorithm : hmac-sha1  Encryption algorithm     : des  Encapsulation mode       : tunnel  Throughput               : 0KB  Outbound AH SA:Interface: ipsec_tunnel2 IKE version               : v2IPsec profile tag:2 Local endpt:101.0.0.25       Current remote endpt: 101.0.0.35 Local  ident(addr/mask/prot/port_min/port_max) :   (3.0.0.0/255.255.255.0/1/Invalid/Invalid) Remote ident(addr/mask/prot/port_min/port_max) :   (3.0.0.0/255.255.255.0/1/Invalid/Invalid) IPsec MTU                 : 1444    FVRF                      : not configure IVRF                      : not configure Pre-fragmentation         : enable Original IP header DF-bit : aware  Tunnel IP header DF-bit   : clear  SA type                   : negotiationRemain lifetime           : 28700(s) Remain inbound throughput : 1843200000(KB) Remain outbound throughput: 1843200000(KB) Inbound ESP SA:  SPI                      : 0x100003f  Authentication algorithm : hmac-sha1  Encryption algorithm     : des  Encapsulation mode       : tunnel  Throughput               : 0KB  Inbound AH SA: Outbound ESP SA:  SPI                      : 0x100003f  Authentication algorithm : hmac-sha1  Encryption algorithm     : des  Encapsulation mode       : tunnel  Throughput               : 0KB  Outbound AH SA:Interface: ipsec_tunnel3 IKE version               : v1IPsec profile tag:3 Local endpt:102.0.0.25       Current remote endpt: 102.0.0.35 Local  ident(addr/mask/prot/port_min/port_max) :   (1.0.0.0/255.255.255.0/0/Invalid/Invalid) Remote ident(addr/mask/prot/port_min/port_max) :   (1.0.0.0/255.255.255.0/0/Invalid/Invalid) IPsec MTU                 : 1444    FVRF                      : not configure IVRF                      : not configure Pre-fragmentation         : enable Original IP header DF-bit : aware  Tunnel IP header DF-bit   : clear  SA type                   : negotiationRemain lifetime           : 28700(s) Remain inbound throughput : 1843200000(KB) Remain outbound throughput: 1843200000(KB) Inbound ESP SA:  SPI                      : 0x1000040  Authentication algorithm : hmac-sha1  Encryption algorithm     : des  Encapsulation mode       : tunnel  Throughput               : 0KB  Inbound AH SA: Outbound ESP SA:  SPI                      : 0x1000040  Authentication algorithm : hmac-sha1  Encryption algorithm     : des  Encapsulation mode       : tunnel  Throughput               : 0KB 
相关命令 : 
clear isakmp saclear crypto ipsec sa show isakmp sa
## show crypto ipsec service-cpu 

show crypto ipsec service-cpu 
命令功能 : 
显示启了IPsec业务的GSU信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec service-cpu 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示启了IPsec业务的GSU信息。如果CPU-INFO字段为invalid，说明启IPsec业务的GSU无效。 
范例 : 
假设在路由器R1的GSU上启了IPsec业务，则路由器R1的配置示例如下：ZXROSNG#show crypto ipsec service-cpu NO.       CPU-INFO1         spi-0/3/0/1
相关命令 : 
show crypto ipsec load-balance 
## show crypto ipsec statistics 

show crypto ipsec statistics 
命令功能 : 
show指定隧道input和output流量信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec statistics 
  ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|＜interface-name＞ 隧道接口名，eg：ipsec_tunnel1
缺省 : 
无 
使用说明 : 
show crypto ipsec statistics ipsec_tunnel1入向TOTAL统计的是解密前的字节数，入向SUCCESS统计的是解密后的字节数，因此入向TOTAL比SUCCESS字节数大出向TOTAL统计的是加密前的字节数，出向SUCCESS统计的是加密后的字节数，因此出向TOTAL比SUCCESS字节数小
范例 : 
ZXROSNG#show crypto ipsec statistic ipsec_tunnel1                Total      input  packets/bytes:         5/700           Successful input  packets/bytes:         5/500            Total      output packets/bytes:         5/500                  Successful output packets/bytes:         5/700
相关命令 : 
clear crypto ipsec statistics 
## show crypto ipsec transform-set 

show crypto ipsec transform-set 
命令功能 : 
显示所有的或者特定的已配置转码集。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show crypto ipsec transform-set 
  [＜transform-set-tag 
＞] 
命令参数解释 : 
参数|描述
---|---
＜transform-set-tag＞|转码集的名字，长度小于18个字符
缺省 : 
无 
使用说明 : 
显示所有的或者特定的已配置转码集。 
范例 : 
假设在路由器R1上显示已配置的所有转码集或者特定的转码集，则路由器R1上的配置示例如下：ZXROSNG(config)#show crypto ipsec transform-set                                   Transform set "zte": {esp-3des}                                                    will negotiate = {Tunnel}                                                    Transform set "zxr": {ah-md5-hmac}                                                 will negotiate = {Transport}                                                 ZXROSNG(config)#show crypto ipsec transform-set zte                               Transform set "zte": {esp-3des}                                                    will negotiate = {Tunnel}                                                    ZXROSNG(config)#
相关命令 : 
crypto ipsec transform-set 
## show debug isakmp 

show debug isakmp 
命令功能 : 
显示IKE协商的调试开关状态。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug isakmp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示IKE协商的调试开关状态。 
范例 : 
假设路由器R1上的配置示例如下：ZXROSNG#debug isakmp allZXROSNG#show debug isakmp ISAKMP:  ISAKMP error debugging is on  ISAKMP event debugging is on  ISAKMP packet debugging is on  ISAKMP state debugging is on  ISAKMP schedule debugging is on
相关命令 : 
debug isakmp 
## show ipsec-pool 

show ipsec-pool 
命令功能 : 
显示配置的IPsec pool。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ipsec-pool 
  [＜ipsec-pool 
＞] 
命令参数解释 : 
参数|描述
---|---
＜ipsec-pool＞|指定所要显示的IPsec pool名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
显示IPsec pool配置信息。可以全部显示，也可以指定显示IPsec pool。 
范例 : 
ZXROSNG(config)#show ipsec-pool Name:zte                                     IP Pool  : zte                   DNS      : 1.2.3.4          4.5.6.7           WINS     :                                  ZXROSNG(config)#
相关命令 : 
ipsec-poolip-pooldnswins
## show isakmp exchange-mode 

show isakmp exchange-mode 
命令功能 : 
显示IKE协商的交换模式设置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp exchange-mode 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示IKE协商的交换模式设置。 
范例 : 
假设在路由器R1上显示IKE协商的交换模式设置，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp exchange-mode main ipv4-address 1.1.1.66 netmask 255.255.255.0 vrf-name fvrfZXROSNG(config)#show isakmp exchange-mode Address/Mask        Exchange-Mode       VRF-Name1.1.1.66/24         main                fvrfZXROSNG(config)#
相关命令 : 
isakmp exchange-mode 
## show isakmp identity 

show isakmp identity 
命令功能 : 
显示IKE协商的身份类型。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp identity 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示IKE协商的身份类型。 
范例 : 
假设在路由器R1上显示IKE协商的身份类型，则路由器R1上的配置示例如下：ZXROSNG(config)#show isakmp identityISAKMP local identity type : address
相关命令 : 
isakmp identity 
## show isakmp key 

show isakmp key 
命令功能 : 
显示IKE协商的预共享密钥设置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp key 
  {ip 
|fqdn 
} 
命令参数解释 : 
参数|描述
---|---
ip|显示IKE协商的身份类型是IP地址的配置
fqdn|显示IKE协商的身份类型是FQDN的配置
缺省 : 
无 
使用说明 : 
显示IKE协商的预共享密钥设置。 
范例 : 
假设在路由器R1上显示IKE协商的预共享密钥设置，则路由器R1上的配置示例如下：ZXROSNG(config)#isakmp pre-shared key ipv4-address 192.168.0.1 netmask 255.255.0.0 vrf-name fvrfZXROSNG(config-isakmp-pre-shared-key)#key zte ZXROSNG(config)#isakmp pre-shared key fqdn zxr10 vrf-name fvrfZXROSNG(config-isakmp-pre-shared-key)#key xyzZXROSNG(config)#show isakmp key ipAddress/Mask        Preshared-Key           Vrfname         LocalIP192.168.0.1/16      4un4E+QOelI=            fvrf            ZXROSNG(config)#show isakmp key fqdnFQDN                Preshared-Key           Vrfnamezxr10               iwJmcSYf1IQ=            fvrf            ZXROSNG(config)#
相关命令 : 
isakmp pre-shared key 
## show isakmp key-set 

show isakmp key-set 
命令功能 : 
显示ISAKMP key-set的信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp key-set 
  [＜key-set-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜key-set-name＞|key-set名称
缺省 : 
无 
使用说明 : 
带key-set名称是显示当前key-set所有信息，包括里面具体的pre-shared-key，不带key-set名称的是显示所有key-set的信息，仅显示key-set名称和key-set下配置的pre-shared-key的数目。 
范例 : 
ZXROSNG(config)#show isakmp key-set 1ISAKMP key-set "1"  Description           : zte  Pre-shared key        :    pre-shared-key 9hvFkSGkois= fqdn 1234 vrf-name vrf_none    pre-shared-key H67q6/ZZYLQ= ipv4-address 1.1.1.1/255.255.255.0 vrf-name vrf_v4ZXROSNG(config)#show isakmp key-set Key set name                        Pre-shared-key number1                                   22                                   0ZXROSNG(config)#
相关命令 : 
isakmp key-set 
## show isakmp phase1 

show isakmp phase1 
命令功能 : 
显示第一阶段相关信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp phase1 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
目前只显示是否开启野蛮模式加密标记功能。 
范例 : 
假设在路由器R1上要显示第一阶段相关信息，则路由器R1上的配置示例如下：ZXROSNG(config)#show isakmp phase1 ISAKMP phase 1 configuration:        Aggressive mode encryption  : disable
相关命令 : 
isakmp phase1 aggressive crypto 
## show isakmp policy 

show isakmp policy 
命令功能 : 
显示已配置的IKE协商策略。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp policy 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示已配置的IKE协商策略。 
范例 : 
假设在路由器R1上要显示IKE协商的安全策略，则路由器R1上的配置示例如下：ZXROSNG(config)#ZXROSNG(config)#show isakmp policyProtection suite of priority 1        Encryption algorithm  : des        Hash algorithm        : md5        Authentication method : pre-share        Diffie-Hellman group  : group1        Lifetime              : 86400 seconds        Pseudo-random function: sha1
相关命令 : 
isakmp policyclear isakmp policy
## show isakmp policy-of-peer 

show isakmp policy-of-peer 
命令功能 : 
显示已经配置的policy-of-peer。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp policy-of-peer 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示已经配置的policy-of-peer。 
范例 : 
假设在路由器R1上显示所有配置的policy-of-peer信息，则路由器R1上的配置示例如下：ZXROSNG(config)#show isakmp policy-of-peer Peer              VRF                              Policy1.2.3.4                                            120::1                                              2
相关命令 : 
clear isakmp policyisakmp policy isakmp peer
## show isakmp profile 

show isakmp profile 
命令功能 : 
显示ISAKMP描述的信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp profile 
  [＜profile-tag 
＞] 
命令参数解释 : 
参数|描述
---|---
＜profile-tag＞|ISAKMP profile名称
缺省 : 
无 
使用说明 : 
带profile名称的是显示当前profile的信息，不带profile名称的是显示所有profile的信息。 
范例 : 
假设在路由器R1上已经创建isakmp profile “pc”，则路由器R1上的配置示例如下：ZXROSNG(config)#show isakmp profileISAKMP profile "pc"   Description                   :     IKE version                   : IKEv2  Self identity                 : address  Exchange mode                 : main  Nat transparency              : disable  Nat transparency keepalive    : 20  DPD interval                  : 0  DPD retry interval            : 0  ISAKMP policy                 :    {      1    }
  ISAKMP key-set                :    {      pc    }
  ISAKMP peer ID                :    {      102.0.0.35    }
ISAKMP profile "ike"   Description                   :     IKE version                   : IKEv2  Self identity                 : hostname  Exchange mode                 : aggressive  Nat transparency              : disable  Nat transparency keepalive    : 20  DPD interval                  : 0  DPD retry interval            : 0  ISAKMP policy                 :    {      1    }
  ISAKMP key-set                :    {      key    }
  ISAKMP peer ID                :    {      ZXR10    }
相关命令 : 
isakmp profile 
## show isakmp sa 

show isakmp sa 
命令功能 : 
显示ISAKMP SA。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp sa 
  [{peer 
 ＜peer-ipv4-address 
＞} [vrf-name 
 ＜ipv4-vrf-name 
＞] [{id-ipv4 
 ＜ipv4-address 
＞|id-fqdn 
 ＜hostname 
＞|id-user-fqdn 
 ＜user-fqdn 
＞|id-key-id 
 ＜key-id 
＞|id-dn 
 ＜pki-domain-name 
＞}]] 
命令参数解释 : 
参数|描述
---|---
＜peer-ipv4-address＞|ISAKMP协商的IPv4类型
＜ipv4-vrf-name＞|ISAKMP协商对端的VRF
＜ipv4-address＞|IPv4地址形式的对方ID信息
＜hostname＞|FQDN形式的对方ID信息，长度1-40字节
＜user-fqdn＞|USER-FQDN形式的对方ID信息，长度1-42字节
＜key-id＞|KEY-ID形式的对方ID信息，长度1-40字节
＜pki-domain-name＞|对端证书的domain name信息
缺省 : 
无 
使用说明 : 
可以通过指明peer和VRF以及对方的ID信息来唯一显示某一个具体的ISAKMP SA。 
范例 : 
假设在路由器R1上显示所有已协商成功的ISAKMP SA的信息，则路由器R1上的配置示例如下：ZXROSNG#show isakmp saCodes: D - Dead Peer Detection       N - NAT-TraversalC-id Local          Remote         VRF     Type Remote-ID      Ver Status Cap1    80.1.1.1       160.1.1.1      ipsec12 IPv4 160.1.1.1      v1  active                                    3456789                                                                   0123456                                                                   7890123                                                                   4                                      2    80.1.1.1       161.1.1.1      ipsec12 IPv4 161.1.1.1      v1  active                                    3456789                                                                   0123456                                                                   7890123                                                                   4                                      3    80.1.1.1       162.1.1.1      ipsec12 IPv4 162.1.1.1      v1  active                                    3456789                                                                   0123456                                                                   7890123                                                                   4                                      4    80.1.1.1       164.1.1.1      ipsec12 FQDN ZXR10          v2  active                                    3456789                                                                   0123456                                                                   7890123                                                                   4ZXROSNG(config)#show isakmp saCodes: D - Dead Peer Detection       N - NAT-TraversalC-id Local          Port Remote         Port VRF      Ver Status Lifetime Cap1    101.0.0.25     500  101.0.0.35     500           v2  active 86400    DZXROSNG#show isakmp sa peer 160.1.1.1C-id:1    Local:80.1.1.1           Port:500   Peer :160.1.1.1          Port:500   VRF:ipsec123456789012345678901234   ID-Type:IPv4                 Remote-ID:160.1.1.1                                           Ver:v1  Side:RESPONDER Enc:3DES     Hash:SHA1   Group:1  Mode:MAIN       Auth:PSKEY      Cki:f26c740b7033c8fb     Ckr:e95324a7060c760b     Lifetime:86400  RemainTime:86298  Cap: 
相关命令 : 
clear isakmp saclear crypto ipsec sa show crypto ipsec sa
## show isakmp user-group 

show isakmp user-group 
命令功能 : 
显示配置的ISAKMP user-group。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show isakmp user-group 
  [＜user-group-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜user-group-name＞|指定所要显示的用户组名称，最大长度为32字节
缺省 : 
无 
使用说明 : 
显示ISAKMP 用户组的配置信息，可以全部显示，也可以按照用户组名显示。全部显示时，对identity、IPsec pool、user name信息只显示该组下总的配置数目。当指定组显示时，具体的信息都会显示出来。 
范例 : 
ZXROSNG(config)#show isakmp user-groupName:grp1  Xauth                  : enable  Max users              : 256  Authentication template: 1  Authorization  template: 1  Accounting     template: 1  Accounting     update  : 600    IPsec Pool number      : 7    User name number       : 8  Identity number        : 8Name:grp2  Xauth                  : enable  Max users              : 256  Authentication template: 1  Authorization  template: 1  Accounting     template: 1  Accounting     update  : 600    IPsec Pool number      : 7    User name number       : 6  Identity number        : 8 ZXROSNG(config)#show isakmp user-group grp1Name:grp1  Xauth                  : enable  Max users              : 256  Authentication template: 1  Authorization  template: 1  Accounting     template: 1  Accounting     update  : 600  IPsec Pool number      : 2    zte    test  User name number       : 2    User name            : user1      Password           : 4un4E+QOelI=    User name            : user2      Password           : 4un4E+QOelI=  Identity number        : 8    identity ipv4-address 192.168.168.168    identity ipv4-address 192.168.168.167            identity fqdn 1234567890    identity fqdn 34455    identity user user1 fqdn user1Fqdn    identity user user2 fqdn user2Fqdn    identity key-id keyId1    identity key-id keyId2
相关命令 : 
isakmp user-groupxauthauthentication templateauthorization templateaccounting templateaccounting-updateipsec-poolmax-useridentity ipv4-addressidentity fqdnidentity useridentity key-id
## size 

size 
命令功能 : 
向量子密钥机一次获取密钥的长度 
命令模式 : 
 IPsec手工描述模式  
命令默认权限级别 : 
15 
命令格式 : 
size 
  ＜quantum-key-size 
＞
no size 
命令参数解释 : 
参数|描述
---|---
＜quantum-key-size＞|作用：配置向密钥机一次获取密钥的长度取值范围：<1-64> kilobytes取值含义：向密钥机一次获取密钥的长度默认值：1 kilobytes
缺省 : 
1 kilobytes，默认一次向密钥机获取1 kilobytes长度的密钥。 
使用说明 : 
向密钥机获取密钥的长度由size命令配置，密钥机根据请求的长度来生成密钥，然后以一次1k长度密钥分多个报文发送请求方。 
范例 : 
ZXROSNG(config)#crypto ipsec manual-profile zte_pflZXROSNG(config-ipsec-manual-profile)#size 35
相关命令 : 
无 
## tunnel local 

tunnel local 
命令功能 : 
指明IPsec隧道接口的本地地址。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel local 
  {ipv4-address 
 ＜local-ipv4-address 
＞|ipv6-address 
 ＜peer-ipv6-address 
＞|interface 
 ＜local-interface 
＞}
no tunnel local 
命令参数解释 : 
参数|描述
---|---
＜local-ipv4-address＞|指明具体的IP地址
＜peer-ipv6-address＞|指明具体的IPv6地址
＜local-interface＞|本地接口
缺省 : 
无 
使用说明 : 
配置隧道的本地地址，通常该地址为物理口地址。本地地址类型需要和IPSEC配置描述中的访问列表类型匹配。
范例 : 
假设在路由器R1上为ipsec_tunnel配置local地址为101.0.0.25，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#tunnel local ipv4-address 101.0.0.25ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show running-config-interface ipsec_tunnel1!<Interface>interface ipsec_tunnel1$!</Interface>!<ipsec>ipsec-config  interface ipsec_tunnel1    tunnel mode ipv4    tunnel local ipv4-address 101.0.0.25    ipsec-profile profile1  $$!</ipsec>
相关命令 : 
show running-config ipsec 
## tunnel mode 

tunnel mode 
命令功能 : 
指明IPsec隧道接口模式。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mode 
  {ipv4 
|ipv6 
}
命令参数解释 : 
参数|描述
---|---
ipv4|指明隧道模式为IPv4
ipv6|指明隧道模式为IPv6
缺省 : 
无 
使用说明 : 
此命令为扩展需要，可以不被配置。 
范例 : 
假设在路由器R1上为ipsec_tunnel设置模式为IPv4，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#tunnel mode ipv4ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show running-config-interface ipsec_tunnel1!<Interface>interface ipsec_tunnel1$!</Interface>!<ipsec>ipsec-config  interface ipsec_tunnel1    tunnel mode ipv4    ipsec-profile profile1  $$!</ipsec>
相关命令 : 
show running-config-interface ipsec_tunnel 
## tunnel protect 

tunnel protect 
命令功能 : 
配置绑定到ipsec-transport的隧道接口的封装类型是否启用tunnel protect功能 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel protect 
  ＜interface-to-protect 
＞
no tunnel protect 
  ＜interface-to-protect 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-to-protect＞|保护的接口名
缺省 : 
无 
使用说明 : 
当绑定的接口为隧道类型的接口，比如GRE接口。如果不配置该命令，封装时，针对内层报文做IPsec封装，此后再做外层隧道的封装。如果配置该命令，封装时，先做外层隧道的封装，此后再根据外层IP信息做IPsec封装。必须先绑定接口到ipsec-transport下，才能继续配置本命令。
范例 : 
ZXROSNG#configure terminalZXROSNG(config)#crypto ipsec-transport1ZXROSNG(config-ipsec-transport1)#bound-to gre_tunnel1ZXROSNG(config-ipsec-transport1)#tunnel protect gre_tunnel1
相关命令 : 
bound-to 
## tunnel remote 

tunnel remote 
命令功能 : 
指明IPsec隧道接口的对端地址。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel remote 
  {ipv4-address 
 ＜remote-ipv4-address 
＞|ipv6-address 
 ＜peer-ipv6-address 
＞}
no tunnel remote 
命令参数解释 : 
参数|描述
---|---
＜remote-ipv4-address＞|指明具体的IP地址
＜peer-ipv6-address＞|指明具体的IPv6地址
缺省 : 
无 
使用说明 : 
配置隧道的对端地址。本地地址类型需要和配置描述中的访问列表类型匹配。
范例 : 
假设在路由器R1上为ipsec_tunnel配置remote地址为101.0.0.35，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#tunnel remote ipv4-address 101.0.0.35ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show running-config-interface ipsec_tunnel1!<Interface>interface ipsec_tunnel1$!</Interface>!<ipsec>ipsec-config  interface ipsec_tunnel1    tunnel mode ipv4    tunnel local ipv4-address 101.0.0.25    tunnel remote ipv4-address 101.0.0.35    ipsec-profile profile1  $$!</ipsec>
相关命令 : 
show running-config ipsec 
## tunnel vrf 

tunnel vrf 
命令功能 : 
为IPsec隧道接口配置外层VRF信息。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel vrf 
  ＜vrf-name 
＞
no tunnel vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名字，范围<1-32>字节
缺省 : 
无 
使用说明 : 
为IPsec隧道配置外层VRF名字，如果要配置外层VRF，必须要先于其他隧道信息配置，并且该VRF需要之前被配置过。 
范例 : 
假设在路由器R1上为ipsec_tunnel设置外层VRF为vrf1，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#tunnel vrf vrf1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show running-config-interface ipsec_tunnel1!<Interface>interface ipsec_tunnel1$!</Interface>!<ipsec>ipsec-config  interface ipsec_tunnel1    ipsec-profile profile1    tunnel vrf vrf1  $$!</ipsec>
相关命令 : 
show running-config-interface ipsec_tunnel 
## type 

type 
命令功能 : 
设置隧道的类型。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
type 
  {static 
|dynamic 
|manual 
}
no type 
命令参数解释 : 
参数|描述
---|---
static|静态型隧道
dynamic|动态型隧道
manual|手工型隧道
缺省 : 
缺省为static，静态型隧道 
使用说明 : 
配置隧道的类型，缺省为静态型隧道，该type值必须和ipsec-profile的类型相同，否则会有错误提示。对于动态型隧道，隧道配置remote是无效的，location命令也是无效的。 
范例 : 
假设在路由器R1上为ipsec_tunnel1配置类型为动态类型，则路由器R1上的配置示例如下：ZXROSNG(config)#ipsec-config ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)#type dynamic ZXROSNG(config-ipsec-if-ipsec_tunnel1)#ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show running-config ipsecZXROSNG(config-ipsec-if-ipsec_tunnel1)#show running-config ipsec!<ipsec>ipsec-config  interface ipsec_tunnel1    type dynamic  $$!</ipsec>
相关命令 : 
show running-config ipsec 
## user-group 

user-group 
命令功能 : 
在隧道下绑定user group。 
命令模式 : 
 IPsec隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
user-group 
  ＜User-group-name 
＞
no user-group 
  ＜User-group-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜User-group-name＞|远程用户组名，最大长度为32字节
缺省 : 
无 
使用说明 : 
在动态隧道下绑定用户组。远程接入时，用户协商时，可以根据该配置组查找到对应的隧道。如果使用了模式配置，会从该配置组分配IP地址给用户。 
范例 : 
ZXROSNG(config-ipsec)#interface ipsec_tunnel1ZXROSNG(config-ipsec-if-ipsec_tunnel1)# reverse-routeZXROSNG(config-ipsec-if-ipsec_tunnel1)# user-group grp10ZXROSNG(config-ipsec-if-ipsec_tunnel1)#show this!<ipsec>  type dynamicisakmp-profile 1reverse-routeuser-group grp10!</ipsec>ZXROSNG(config-ipsec-if-ipsec_tunnel1)#
相关命令 : 
无 
## user-name 

user-name 
命令功能 : 
配置用户的用户名和密码。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
user-name 
  ＜user-name 
＞ password 
 {encrypted 
 ＜encrypted-password 
＞|＜password 
＞}
no user-name 
  ＜user-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜user-name＞|用户名，字符串格式，最大长度为32字节
＜encrypted-password＞|密文密码，字符串类型，密文最大长度为44字节
＜password＞|明文密码，字符串类型，明文最大长度为32字节
缺省 : 
无 
使用说明 : 
配置用户的用户名和密码，在用户登录时进行身份识别。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)# user-name zte password encrypted 4un4E+QOelI=ZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  user-name zte password encrypted 4un4E+QOelI=!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupshow isakmp user-group
## vrf 

vrf 
命令功能 : 
指明IPsec传输接口的外层VRF名称。 
命令模式 : 
 IPsec-transport模式  
命令默认权限级别 : 
15 
命令格式 : 
vrf 
  ＜vrf-name 
＞
no vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名字
缺省 : 
无 
使用说明 : 
为IPsec传输虚接口配置外层VRF名字，如果要配置外层VRF，必须要先于其他隧道信息配置，并且该VRF需要之前被配置过。 
范例 : 
ZXROSNG(config)#crypto ipsec-transport 1ZXROSNG(config-ipsec-transport1)#vrf 1                ZXROSNG(config-ipsec-transport1)#show this!<ipsec>  vrf 1!</ipsec>ZXROSNG(config-ipsec-transport1)#
相关命令 : 
无 
## vrf 

vrf 
命令功能 : 
设定Key server的绑定的本地vrf名 
命令模式 : 
 IPsec-GDOI-server模式  
命令默认权限级别 : 
15 
命令格式 : 
vrf 
  ＜vrf-name 
＞
no vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|vrf名字，1-32字符
缺省 : 
无 
使用说明 : 
该命令用来为Key Server配置VRF名字，如果要配置该VRF，VRF需要之前被配置过。
范例 : 
ZXROSNG(config)#crypto ipsec gdoi-server 1 ZXROSNG(config-ipsec-gdoi-server)# vrf vpn-nameZXROSNG(config-ipsec-gdoi-server)#exit
相关命令 : 
crypto ipsec gdoi-server
## wins 

wins 
命令功能 : 
配置wins地址。 
命令模式 : 
 IPsec-pool模式  
命令默认权限级别 : 
15 
命令格式 : 
wins 
 first 
 ＜first-wins 
＞ [second 
 ＜second-wins 
＞]
no wins 
命令参数解释 : 
参数|描述
---|---
＜first-wins＞|首选 wins地址，IP地址类型
＜second-wins＞|备选 wins地址，IP地址类型
缺省 : 
无 
使用说明 : 
在IPsec pool下配置wins，可以配置首选wins地址，可选配备选wins地址。 
范例 : 
ZXROSNG(config)#ipsec-pool zteZXROSNG(config-ipsec-pool)#wins first 1.2.3.4 second 5.6.7.8ZXROSNG(config-ipsec-pool)#show this!<isakmp>  wins first 1.2.3.4 second 5.6.7.8!</isakmp>ZXROSNG(config-ipsec-pool)#
相关命令 : 
show ipsec-poolipsec-pool
## xauth 

xauth 
命令功能 : 
开启IPsec 扩展认证过程。 
命令模式 : 
 ISAKMP用户组模式  
命令默认权限级别 : 
15 
命令格式 : 
xauth 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启xauth认证阶段
disable|关闭xauth认证阶段
缺省 : 
disable 
使用说明 : 
远程用户接入时，需要对用户的身份进行扩展认证，可以开启此过程。 
范例 : 
ZXROSNG(config)#isakmp user-group grp10ZXROSNG(config-isakmp-usergroup)#xauth enableZXROSNG(config-isakmp-usergroup)#show this!<isakmp>  xauth enable!</isakmp>ZXROSNG(config-isakmp-usergroup)#
相关命令 : 
isakmp user-groupshow isakmp user-group
# RADIUS配置命令 
## algorithm 

algorithm 
命令功能 : 
设置组内RADIUS服务器的调度策略。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
algorithm 
  {first 
|round-robin 
}
命令参数解释 : 
参数|描述
---|---
first|总是选择当前有效的一个服务器作为当前请求的目标服务器
round-robin|总是选择下一个有效的服务器作为当前请求的目标服务器
缺省 : 
默认值为first。 
使用说明 : 
服务器调度策略描述如下：first：1）如果配置了master服务器，选择master服务器；如果master不可用（由于网络不通等原因造成的dead状态），进入2）选择流程；2）如果没有配置master服务器，选择当前使用的服务器；如果当前没有正在使用的服务器或者是这个组首次请求，进入3）选择流程；3）在active的服务中选择编号最小的服务器；4）如果没有active服务器，则选择失败round-robin：选择当前服务器的下一个active服务器。
范例 : 
设置RADIUS计费服务器组1的选择算法为first：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#algorithm firstZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radius 
## algorithm 

algorithm 
命令功能 : 
设置组内RADIUS服务器的调度策略。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
algorithm 
  {first 
|round-robin 
|rollover-on-reject 
}
命令参数解释 : 
参数|描述
---|---
first|总是选择当前有效的一个服务器作为当前请求的目标服务器
round-robin|总是选择下一个有效的服务器作为当前请求的目标服务器
rollover-on-reject|设备收到radius认证拒绝消息时，可以继续轮询其他服务器进行认证
缺省 : 
first。 
使用说明 : 
服务器调度策略描述如下：first：1）如果配置了master服务器，选择master服务器；如果master不可用（由于网络不通等原因造成的dead状态），进入2）选择流程；2）如果没有配置master服务器，选择当前使用的服务器；如果当前没有正在使用的服务器或者是这个组首次请求，进入3）选择流程；3）在active的服务中选择编号最小的服务器；4）如果没有active服务器，则选择失败round-robin：选择当前服务器的下一个active服务器。rollover-on-reject:设备收到radius认证拒绝消息时，可以继续轮询其他服务器进行认证。
范例 : 
设置RADIUS认证服务器组1的选择算法为round-robin：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#algorithm round-robinZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## alias 

alias 
命令功能 : 
配置服务器组的别名。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
alias 
  ＜alias-name 
＞
no alias 
命令参数解释 : 
参数|描述
---|---
＜alias-name＞|服务器组别名，长度1-31个字符
缺省 : 
无。 
使用说明 : 
服务器组之间的别名是唯一的，不允许重复。别名不能包含空格等空字符。 
范例 : 
设置计费服务器组1别名为acc_grp1：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#alias acc_grp1ZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radius 
## alias 

alias 
命令功能 : 
配置服务器组的别名。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
alias 
  ＜alias-name 
＞
no alias 
命令参数解释 : 
参数|描述
---|---
＜alias-name＞|服务器组别名，长度1-31个字符
缺省 : 
无。 
使用说明 : 
服务器组之间的别名是唯一的，不允许重复。别名不能包含空格等空字符。 
范例 : 
设置认证服务器组1别名为authen_grp1：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#alias authen_grp1ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## attribute convert 

attribute convert 
命令功能 : 
设置指定属性在计费报文中进行转义。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
attribute convert 
  {＜source-attribute-vendor-id 
＞|standard 
} ＜source-attribute-type 
＞ to 
 {＜dest-attribute-vendor-id 
＞|standard 
} ＜dest-attribute-type 
＞ [{multiplied-by 
|divided-by 
} ＜coefficient 
＞] {send 
|receive 
}
no attribute convert 
  {＜source-attribute-vendor-id 
＞|standard 
} ＜source-attribute-type 
＞ {send 
|receive 
}
				
命令参数解释 : 
参数|描述
---|---
＜source-attribute-vendor-id＞|转义源属性的厂商id，取值1-65535
standard|转义源属性为标准属性
＜source-attribute-type＞|转义源属性的属性号，取值1-255
＜dest-attribute-vendor-id＞|转义目标属性的厂商id，取值1-65535
standard|转义源属性为标准属性
＜dest-attribute-type＞|转义目标属性的属性号，取值1-255
multiplied-by|转义属性值倍数放大
divided-by|转义属性值倍数缩小
＜coefficient＞|转义属性的缩放倍数，取值1- 4294967295
send|转义属性在发送方向的报文中生效
receive|转义属性在接收方向的报文中生效
缺省 : 
无 
使用说明 : 
属性转义即将配置中源属性的值当做目的属性来使用。设置转义属性时，如果是本设备支持的属性源和目标属性的类型必须一致，源和目标属性任何一方为未知属性时不受该规则约束；只有数值类型的属性才能配置系数缩放，未知属性类型不受该规则约束；对于下发的属性，如果目的属性是设备不支持的属性，则配置不生效；对于发送的属性，如果源属性是设备不支持的属性，则配置不生效；如果在发送方向的报文中配置了多个源对应同一个目标的转义，则可能在同一个报文中出现多个目的属性，建议避免这种情况。对于发送报文来说，禁用某属性即不发送该属性；对于接收到的报文来说来说，禁用某属性即报文中若携带了该属性但不生效。每个服务器组可配置128条属性转义条目；整个设备可配置1024条属性转义条目（包含认证组的属性转义）。
范例 : 
配置标准属性的31号属性在发送方向报文中转义成标准属性的1号属性：ZXROSNG(config-acctgrp-2)# attribute convert standard 31 to standard 1 send ZXROSNG(config-acctgrp-2)#配置自定义厂商(3902)属性227号属性在接收方向的所有报文中转义成标准属性的46号，并带有10倍的值放大：ZXROSNG(config-acctgrp-2)# attribute convert 3902 227 to standard 46 multiplied-by 10 receive ZXROSNG(config-acctgrp-2)#
相关命令 : 
attribute forbidshow running-config radiusshow configuration radius attribute convert
## attribute convert 

attribute convert 
命令功能 : 
设置指定属性在认证报文中进行转义。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
attribute convert 
  {＜source-attribute-vendor-id 
＞|standard 
} ＜source-attribute-type 
＞ to 
 {＜dest-attribute-vendor-id 
＞|standard 
} ＜dest-attribute-type 
＞ [{multiplied-by 
|divided-by 
} ＜coefficient 
＞] {send 
 [{[access-request 
],[coa-response 
],[disconnect-response 
]}]|receive 
 [{[access-response 
],[coa-request 
],[disconnect-request 
]}]}
no attribute convert 
  {＜source-attribute-vendor-id 
＞|standard 
} ＜source-attribute-type 
＞ {send 
|receive 
}
				
命令参数解释 : 
参数|描述
---|---
＜source-attribute-vendor-id＞|转义源属性的厂商id，取值1-65535
standard|转义源属性为标准属性
＜source-attribute-type＞|转义源属性的属性号，取值1-255
＜dest-attribute-vendor-id＞|转义目标属性的厂商id，取值1-65535
standard|转义源属性为标准属性
＜dest-attribute-type＞|转义目标属性的属性号，取值1-255
multiplied-by|转义属性值倍数放大
divided-by|转义属性值倍数缩小
＜coefficient＞|转义属性的缩放倍数，取值1- 4294967295
send|转义属性在发送方向的报文中生效
access-request|转义属性在access-request报文中生效
coa-response|转义属性在coa-response报文中生效
disconnect-response|转义属性在disconnect-response报文中生效
receive|转义属性在接收方向的报文中生效
access-response|转义属性在access-accept报文中生效
coa-request|转义属性在coa-request报文中生效
disconnect-request|转义属性在disconnect-request报文中生效
缺省 : 
无 
使用说明 : 
属性转义即将配置中源属性的值当做目标属性来使用。发送（send）与接收（receive）方向各包含3种报文，如果不指定任何一种，表示配置在这个方向上的所有报文中均生效；如果指定其中的报文种类，表示只在指定的报文中生效属性禁用配置；设置转义属性时，如果是本设备支持的属性源和目标属性的类型必须一致，源和目标属性任何一方为未知属性时不受该规则约束；只有数值类型的属性才能配置系数缩放，未知属性类型不受该规则约束；对于下发的属性，如果目的属性是设备不支持的属性，则配置不生效；对于发送的属性，如果源属性是设备不支持的属性，则配置不生效；如果在发送方向的报文中配置了多个源对应同一个目标的转义，则可能在同一个报文中出现多个目标属性，建议避免这种情况。对于发送报文来说，属性转义即将本应该填写成源属性的值填写在目标属性中；对于接收到的报文来说，即将源属性的值解析成目标属性来使用。每个服务器组可配置128条属性转义条目；整个设备可配置1024条属性转义条目（包含认证组的属性转义）。
范例 : 
配置标准属性的31号属性在access-request与coa-response报文中转义成标准属性的1号属性：ZXROSNG(config-authgrp-1)# attribute convert standard 31 to standard 1 send access-request coa-responseZXROSNG(config-authgrp-1)#配置自定义厂商(3902)属性227号属性在接收方向的所有报文中转义成标准属性的46号，并带有10倍的值放大：ZXROSNG(config-authgrp-1)# attribute convert 3902 227 to standard 46 multiplied-by 10 receive ZXROSNG(config-authgrp-1)#
相关命令 : 
attribute forbidshow running-config radiusshow configuration radius attribute convert
## attribute forbid 

attribute forbid 
命令功能 : 
设置指定属性在计费报文中禁用。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
attribute forbid 
  {＜attribute-vendor-id 
＞|standard 
} ＜attribute-type 
＞ {send 
|receive 
}
no attribute forbid 
  {＜attribute-vendor-id 
＞|standard 
} ＜attribute-type 
＞ {send 
|receive 
}
				
命令参数解释 : 
参数|描述
---|---
＜attribute-vendor-id＞|禁用属性的厂商id(厂商自定义属性使用)，取值1-65535
standard|禁用属性为标准属性
＜attribute-type＞|禁用属性号，取值1-255
send|禁用属性在发送方向的报文中生效
receive|禁用属性在接收方向的报文中生效
缺省 : 
无 
使用说明 : 
可以同时在接收方向和发送方向禁用指定属性，发送方向的禁用就是指在Accounting-Request报文中禁用，接收方向上的禁用就是在Accounting-Response报文解析时禁用。配置的属性禁用在相应的RADIUS报文中必须支持携带，才可生效。对于Accounting-Request来说，禁用某属性即不发送该属性；对于Accounting-Response来说，禁用某属性即报文中若携带了该属性但不处理。每个服务器组可配置128条属性禁用条目；整个设备可配置1024条属性禁用条目（包含认证组的属性禁用）。
范例 : 
配置标准属性的31号属性在send方向的报文中禁用：ZXROSNG(config-acctgrp-2)#attribute forbid standard 31 send ZXROSNG(config-acctgrp-2)#
相关命令 : 
attribute convertshow running-config radius allshow configuration radius attribute forbid 
## attribute forbid 

attribute forbid 
命令功能 : 
配置认证相关报文接收和发送方向属性的禁用。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
attribute forbid 
  {＜attribute-vendor-id 
＞|standard 
} ＜attribute-type 
＞ {send 
 [{[access-request 
],[coa-response 
],[disconnect-response 
]}]|receive 
 [{[access-response 
],[coa-request 
],[disconnect-request 
]}]}
no attribute forbid 
  {＜attribute-vendor-id 
＞|standard 
} ＜attribute-type 
＞ {send 
|receive 
}
				
命令参数解释 : 
参数|描述
---|---
＜attribute-vendor-id＞|禁用属性的厂商id(厂商自定义属性使用)，取值1-65535
standard|禁用属性为标准属性
＜attribute-type＞|禁用属性号，取值1-255
send|禁用属性在发送方向的报文中生效
access-request|禁用属性在access-request报文中生效
coa-response|禁用属性在coa-response报文中生效
disconnect-response|禁用属性在disconnect-response报文中生效
receive|禁用属性在接收方向的报文中生效
access-response|禁用属性在access-response报文中生效
coa-request|禁用属性在coa-request报文中生效
disconnect-request|禁用属性在disconnect-request报文中生效
缺省 : 
无 
使用说明 : 
发送（send）与接收（receive）方向各包含3种报文，如果不指定任何一种，表示配置在这个方向上的所有报文中均生效；如果指定其中的报文种类，表示只在指定的报文中生效属性禁用配置。可以同时在接收方向和发送方向禁用此属性。可以同时在接收方向和发送方向禁用指定属性，对于发送报文来说，警用某属性指改属性在发送的报文中不填写；对于接收到的报文来说禁用某属性即报文中若携带了该属性但不处理。每个服务器组可配置128条属性禁用条目；整个设备可配置1024条属性禁用条目（包含认证组的属性禁用）。
范例 : 
1.配置标准属性的31号属性在access-request与coa-response报文中禁用：ZXROSNG(config-authgrp-1)#attribute forbid standard 31 send access-request coa-responseZXROSNG(config-authgrp-1)#2.配置自定义厂商(3902)属性227号属性在接收方向的所有报文中生效：ZXROSNG(config-authgrp-1)#attribute forbid 3902 227 receive ZXROSNG(config-authgrp-1)#
相关命令 : 
attribute convertshow running-config radiusshow configuration radius attribute forbid
## attribute replace nas-identifier 

attribute replace nas-identifier 
命令功能 : 
设置PROXY转发RADIUS报文时，是否替换原始报文中的NAS-Identifier属性地址为本地配置的NAS-Identifier。 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
attribute replace nas-identifier 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|替换
disable|不替换
缺省 : 
disable。 
使用说明 : 
使能此功能后，设备代理转发RADIUS客户端的请求报文时，将报文中的NAS-Identifier属性替换为本地配置的NAS-Identifier。本地配置的NAS-Identifier获取策略参见命令nas-identifier。 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#attribute replace nas-identifier enable 
相关命令 : 
无 
## attribute replace nas-ip-address 

attribute replace nas-ip-address 
命令功能 : 
设置PROXY转发RADIUS报文时，是否替换原始报文中的NAS-IP-Address属性地址为本地配置的NAS-IP-Address。 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
attribute replace nas-ip-address 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|替换NAS-IP-Address
disable|不替换NAS-IP-Address
缺省 : 
disable 
使用说明 : 
使能此功能后，设备代理转发RADIUS客户端的请求报文时，将报文中的NAS-IP-Address属性替换为本地配置的NAS-IP-Address（由RADIUS认证组模式的nas-ip-address命令配置），避免某些RADIUS服务器直接向原始报文所标识的NAS-IP-Address地址回应报文或发送动态授权报文。 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#attribute replace nas-ip-address enable 
相关命令 : 
无 
## authentication-server-group 

authentication-server-group 
命令功能 : 
配置客户组使用的认证组 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
authentication-server-group 
  ＜group-name 
＞
no authentication-server-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|RADIUS认证服务器组的组名，RADIUS组名长度为1-31个字符。
缺省 : 
无 
使用说明 : 
使用的认证组必须已经配置 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#authentication-server-group 1
相关命令 : 
无 
## called-station-format 

called-station-format 
命令功能 : 
配置将Called-Station-Id以ssid格式上送。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
called-station-format 
  {ssid 
}
no called-station-format 
命令参数解释 : 
参数|描述
---|---
ssid|将Called-Station-Id以ssid格式上送。
缺省 : 
无 
使用说明 : 
如果不配置该命令，则认证报文中无Called-Station-ID属性。 
范例 : 
开启将Called-Station-Id以ssid格式上送功能：ZZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#called-station-format ssid ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## calling-station-format 

calling-station-format 
命令功能 : 
配置Calling-Station-Id属性字段格式定义。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
calling-station-format 
  {class1 
|class2 
|class3 
|class4 
|class5 
|user-defined 
 [{[slot 
],[port 
],[sub-slot 
],[vlan 
],[second-vlan 
],[mac1 
],[mac2 
],[mac3 
],[mac4 
],[mac5 
],[mac6 
]}] text 
 ＜text-string 
＞}
no calling-station-format 
命令参数解释 : 
参数|描述
---|---
class1|class1：表示用户接入的物理接口信息，各数值的16进制打印格式以无分隔符连接在一起，排列的域分别为slot（2字节）、port（2字节）、vpi（2字节）、vci（4字节）、vlanid（4字节）、mac（12字节）
class2|class2：表示用户接入的物理接口信息，各数值的16进制打印格式以无分隔符连接在一起，排列的域分别为slot（2字节）、port（2字节）、vpi（2字节）、vci（4字节）、vlanid（1字节）
class3|class3：仅保留MAC地址，格式为xx:xx:xx:xx:xx:xx
class4|class4：土电slot-port格式，ATM接入： Hostname#shelf/slot/subslot/port#VPI#VCIETH接入： Hostname#shelf/slot/subslot/port#exVlan:inVlan各物理信息数值为10进制打印格式
class5|class5：尼泊尔电信定制格式，Hostname/{atm|eth|trunk} NAS_slot/NAS_subslot/NAS_port: XPI.XCI  AccessNodeIdentifier/ ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port[:ANI_xpi.ANI_xci]，各数值采用10进制打印格式
user-defined|支持Calling-Station-Id按照用户配置的字符串格式编码，slot、subslot、port、vlan、second-vlan、mac可选择
slot|slot选项
port|port选项
sub-slot|sub-slot选项
vlan|vlan选项
second-vlan|second-vlan选项
mac1|mac1选项
mac2|mac2选项
mac3|mac3选项
mac4|mac4选项
mac5|mac5选项
mac6|mac6选项
＜text-string＞|格式字符串，1~88个字符
缺省 : 
class3。 
使用说明 : 
user-defined格式在slot、subslot、port、vlan、second-vlan、mac中选择希望在Calling-Station-Id中携带的参数；参数组织格式由text输入的字符串决定，格式串采用ANSIC标准C语言定义的格式化输入字符串。格式字符由下表给出：格式字符      说明d    ：以带符号的十进制形式输出整数（正数不输出符号）x, X    ：以十六进制无符号形式输出整数（不输出前导符0x）， 用x则输出十六进制数的a~f时以小写形式输出。用X时，则以大写字母输出u    ：以无符号十进制形式输出整数字母l    ：用于长整型整数，可加在格式符d，x，X，u前面数字m    ：加在以上格式字符组合前面，表示最小输出宽度，不满足最小宽度用默认使用空格填充，超过最大按实际宽度输出数字n    ：加在以上格式字符组合前面，表示不足宽度要求用来填充的数字
范例 : 
配置计费服务器的Calling-Station-Id属性格式为class2：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)# calling-station-format class2ZXROSNG(config-acctgrp-1)#配置计费服务器的Calling-Station-Id属性格式为user-defined，希望在报文中输出的Calling-Station-Id属性为vlan=0x04 second-vlan=0x0a: port=1758 sub-slot=12:MAC=010203040506：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)# calling-station-format user-defined vlan second-vlan slot sub-slot mac1 mac2 mac3 mac4 mac5 mac6 text vlan=0x%02x second-vlan=0x%02x:slot=%04u sub-slot=%02u:MAC=%02x%02x%02x%02x%02x%02xZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radius 
## calling-station-format 

calling-station-format 
命令功能 : 
配置Calling-Station-Id属性字段格式定义。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
calling-station-format 
  {class1 
|class2 
|class3 
|class4 
|class5 
|user-defined 
 [{[slot 
],[port 
],[sub-slot 
],[vlan 
],[second-vlan 
],[mac1 
],[mac2 
],[mac3 
],[mac4 
],[mac5 
],[mac6 
]}] text 
 ＜text-string 
＞}
no calling-station-format 
命令参数解释 : 
参数|描述
---|---
class1|class1：表示用户接入的物理接口信息，各数值的16进制打印格式以无分隔符连接在一起，排列的域分别为slot（2字节）、port（2字节）、vpi（2字节）、vci（4字节）、vlanid（4字节）、mac（12字节）
class2|class2：表示用户接入的物理接口信息，各数值的16进制打印格式以无分隔符连接在一起，排列的域分别为slot（2字节）、port（2字节）、vpi（2字节）、vci（4字节）、vlanid（1字节）
class3|class3：仅保留MAC地址，格式为xx:xx:xx:xx:xx:xx
class4|class4：土电slot-port格式，ATM接入： Hostname#shelf/slot/subslot/port#VPI#VCIETH接入： Hostname#shelf/slot/subslot/port#exVlan:inVlan各物理信息数值为10进制打印格式
class5|class5：尼泊尔电信定制格式，Hostname/{atm|eth|trunk} NAS_slot/NAS_subslot/NAS_port: XPI.XCI  AccessNodeIdentifier/ ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port[:ANI_xpi.ANI_xci]，各数值采用10进制打印格式
user-defined|支持Calling-Station-Id按照用户配置的字符串格式编码，slot、subslot、port、vlan、second-vlan、mac可选择
slot|slot选项
port|port选项
sub-slot|sub-slot选项
vlan|vlan选项
second-vlan|second-vlan选项
mac1|mac1选项
mac2|mac2选项
mac3|mac3选项
mac4|mac4选项
mac5|mac5选项
mac6|mac6选项
＜text-string＞|格式字符串，1~88个字符
缺省 : 
class3。 
使用说明 : 
user-defined格式在slot、subslot、port、vlan、second-vlan、mac中选择希望在Calling-Station-Id中携带的参数；参数组织格式由text输入的字符串决定，格式串采用ANSIC标准C语言定义的格式化输入字符串。格式字符由下表给出：格式字符      说明d    ：以带符号的十进制形式输出整数（正数不输出符号）x, X    ：以十六进制无符号形式输出整数（不输出前导符0x）， 用x则输出十六进制数的a~f时以小写形式输出。用X时，则以大写字母输出u    ：以无符号十进制形式输出整数字母l    ：用于长整型整数，可加在格式符d，x，X，u前面数字m    ：加在以上格式字符组合前面，表示最小输出宽度，不满足最小宽度用默认使用空格填充，超过最大按实际宽度输出数字n    ：加在以上格式字符组合前面，表示不足宽度要求用来填充的数字
范例 : 
配置认证服务器的Calling-Station-Id属性字段格式定义为class2：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#calling-station-format class2ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## class-as-car 

class-as-car 
命令功能 : 
配置将Class（标准25号）属性解析成CAR属性。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
class-as-car 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启将class属性解析成CAR属性功能
disable|关闭将class属性解析成CAR属性功能
缺省 : 
disable。 
使用说明 : 
如果配置了此命令，并且Class属性（标准属性25号）已经成功解析为CAR属性，则其他下发的CAR属性将不生效，包括我司自定义属性ZTE-Rate-Ctrl-Src-Down（83号）、ZTE-Rate-Ctrl-Src-Up（89号）、ZTE-Rate-Ctrl-Burst-Down（84号）、ZTE-Rate-Ctrl-Burst-Up（91号）。当Class属性内容解析为CAR属性时，同时也生效为Class属性
范例 : 
开启将Class属性解析成CAR属性功能：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#class-as-car enable ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## clear accounting local-buffer 

clear accounting local-buffer 
命令功能 : 
清除RADIUS本地缓存的计费报文。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear accounting local-buffer 
  {group 
 ＜group-name 
＞|all 
}
命令参数解释 : 
参数|描述
---|---
＜group-name＞|RADIUS计费服务器组的组名，长度为1-31个字符。
all|清除RADIUS本地缓存的所有计费报文
缺省 : 
无。 
使用说明 : 
手动清除计费报文会通知该报文的用户报文被清除。因计费缓存空间有限，可以通过此功能释放之前的缓存报文，给新报文的存储腾出空间。计费缓存功能通过RADIUS计费组模式下的命令local-buffer命令开启，具体参见改命令说明。
范例 : 
清除RADIUS本地缓存的所有计费报文：ZXROSNG# clear accounting local-buffer allZXROSNG#
清除RADIUS计费组1下缓存的计费报文：ZXROSNG# clear accounting local-buffer group 1ZXROSNG#
相关命令 : 
show accounting local-buffer all 
## clear radius counter 

clear radius counter 
命令功能 : 
清除计费服务器计数信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear radius counter 
  {authentication-group 
 ＜auth-grp-name 
＞|accounting-group 
 ＜acct-grp-name 
＞|all 
}
命令参数解释 : 
参数|描述
---|---
authentication-group|指定清除认证服务器计数
＜auth-grp-name＞|RADIUS认证服务器组的组名，RADIUS组名长度为1-31个字符。
accounting-group|指定清除计费服务器计数
＜acct-grp-name＞|RADIUS计费服务器组的组名，RADIUS组名长度为1-31个字符。
all|清除所有服务器计数
缺省 : 
无。 
使用说明 : 
可以指定清除某个组的计数统计信息，也可以通过all参数清除所有组的计数信息。注意：只清除组下的统计信息，统计信息的全局部分是不清除的。
范例 : 
清除RADIUS指定计费组服务器计数信息：ZXROSNG#clear radius counter accounting-group 2000Clear radius counters of accounting group 2000 success!
相关命令 : 
show radius counter 
## client 

client 
命令功能 : 
配置客户组下的客户端 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
client 
 ip 
 ＜client-ip 
＞ [vrf 
 ＜VRF-name 
＞] [key 
 {encrypted 
 ＜encrypted-key 
＞|＜key-string 
＞ [showclear 
]}]
no client 
 ip 
 ＜client-ip 
＞ [vrf 
 ＜VRF-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜client-ip＞|ip地址，目前只支持IPv4地址
＜VRF-name＞|VRF名称，长度为1~32字节
＜encrypted-key＞|加密的共享密钥，长度为64字节
＜key-string＞|未加密的共享密钥，长度为1~31字节
showclear|明文密钥显示的标志，缺省为加密。
缺省 : 
无 
使用说明 : 
同一个客户组下的客户端，其VRF要一致，并且每个组下最多只能配置64个客户端 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#client ip 192.168.122.10 vrf xin key zte
相关命令 : 
无 
## deadtime 

deadtime 
命令功能 : 
配置服务器的无效时间。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
deadtime 
  ＜deadtime 
＞
no deadtime 
命令参数解释 : 
参数|描述
---|---
＜deadtime＞|无效时间，范围：0-3600，单位：分钟
缺省 : 
5分钟。 
使用说明 : 
当一个请求报文发送到服务器以后没有得到回应（经过超时重传），服务器进入dead状态，该状态持续的时间就是deadtime，deadtime时间过后，服务器将重新转为active。在dead状态下，设备不会向这个服务器发送请求。 
范例 : 
设置计费服务器无效时间为3分钟：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)# deadtime 3ZXROSNG(config-acctgrp-1)#no deadtime
相关命令 : 
timeoutmax-retriesshow running-config radius
## deadtime 

deadtime 
命令功能 : 
配置服务器的无效时间。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
deadtime 
  ＜deadtime 
＞
no deadtime 
命令参数解释 : 
参数|描述
---|---
＜deadtime＞|无效时间，范围：0-3600，单位：分钟
缺省 : 
5分钟。 
使用说明 : 
当一个请求报文发送到服务器以后没有得到回应（经过超时重传），服务器进入dead状态，该状态持续的时间就是deadtime，deadtime时间过后，服务器将重新转为active。在dead状态下，设备不会向这个服务器发送请求。 
范例 : 
设置认证服务器无效时间为3分钟。ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#deadtime 3ZXROSNG(config-authgrp-1)#
相关命令 : 
timeoutmax-retriesshow running-config radius
## debug radius accounting data 

debug radius accounting data 
命令功能 : 
打开/关闭RADIUS计费debug data。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius accounting data 
 
no debug radius accounting data 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS计费debug data。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS 计费组data信息显示：ZXROSNG# debug radius accounting dataZXROSNG#ZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: accttype:STARTZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: svrgroup:999ZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: username:HUNTERZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: ispname:zteZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: acctsession:120107144336DingG181824ACCT0001打开RADIUS 计费组data信息显示：ZXROSNG# debug radius accounting dataZXROSNG#ZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: accttype:STARTZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: svrgroup:999ZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: username:HUNTERZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: ispname:zteZXR10 MPU-0/20/0 2012-1-7 06:43:36 APP_RADIUS: RADIUS data: acctsession:120107144336DingG181824ACCT0001
相关命令 : 
debug radius filtershow debug radius
## debug radius accounting error 

debug radius accounting error 
命令功能 : 
打开/关闭RADIUS计费debug error。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius accounting error 
 
no debug radius accounting error 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS计费debug error。具体参看命令debug radius all说明 
范例 : 
打开RADIUS 计费组错误信息显示：ZXROSNG#debug radius accounting errorZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS err :Receive packet vector invalid打开RADIUS 计费组错误信息显示：ZXROSNG#debug radius accounting errorZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS err :Receive packet vector invalid
相关命令 : 
debug radius filtershow debug radius
## debug radius accounting event 

debug radius accounting event 
命令功能 : 
打开/关闭RADIUS计费debug event。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius accounting event 
 
no debug radius accounting event 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS计费debug event。具体参看命令debug radius all说明 
范例 : 
打开RADIUS 计费组event信息显示：ZXROSNG#debug radius accounting eventZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: RP Process Accounting RequestZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: RADIUS add accounting request to sending queue and send it to serverZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: send accounting request packet 100.1.1.1:6118->100.1.1.10:1813ZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: receive accounting response packet 100.1.1.10:1813->100.1.1.1:6118ZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: RADIUS delete request element from group queue打开RADIUS 计费组event信息显示：ZXROSNG#debug radius accounting eventZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: RP Process Accounting RequestZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: RADIUS add accounting request to sending queue and send it to serverZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: send accounting request packet 100.1.1.1:6118->100.1.1.10:1813ZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: receive accounting response packet 100.1.1.10:1813->100.1.1.1:6118ZXR10 MPU-0/20/0 2012-1-7 06:38:04 APP_RADIUS: RADIUS event: RADIUS delete request element from group queue
相关命令 : 
debug radius filtershow debug radius
## debug radius accounting packet 

debug radius accounting packet 
命令功能 : 
打开/关闭RADIUS计费debug packet。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius accounting packet 
 
no debug radius accounting packet 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS计费debug packet。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS计费组packet开关，相应的显示：ZXROSNG#debug radius accounting packetRADIUS packet accounting debugging has been turned onZXROSNG#ZXR10 MPU-0/20/0 2013-5-13 07:44:27 APP_RADIUS: packet:   send Accounting-Request packet 100.0.0.250:6118->192.168.10.53:1813ZXR10 MPU-0/20/0 2013-5-13 07:44:28 APP_RADIUS: packet:   code = 4(Accounting-Request)  id = 4  length = 183  Authenticator = 9E 1C E0 D8 FB B1 E1 2B D7 25 A5 1A 7F F7 8E 32   [Type : Attribute No                   ] [len] [value]  [Acct-Session-Id : 44                  ] [33 ] [130513154427DingG181824ACCT0002]  [NAS-IP-Address : 4                    ] [6  ] [100.0.0.250]  [Acct-Delay-Time : 41                  ] [6  ] [0]  [Acct-Status-Type : 40                 ] [6  ] [1:Start]  [NAS-Identifier : 32                   ] [19 ] [SE-KCEKMECE-ZTE-1]  [ZTE-Auth-Action : 3902-254            ] [6  ] [0]  [User-Name : 1                         ] [5  ] [zte]  [Calling-Station-Id : 31               ] [19 ] [00:00:00:00:00:00]  [Acct-Authentic : 45                   ] [6  ] [1:RADIUS]  [NAS-Port : 5                          ] [6  ] [00 00 00 00 ]  [NAS-Port-Type : 61                    ] [6  ] [0:Async]  [NAS-Port-Id : 87                      ] [39 ] [0 1/2/3:88.99 zte-t8000/0/0/0/0/0:0.0]ZXR10 MPU-0/20/0 2013-5-13 07:44:28 APP_RADIUS: packet:   radius packet original data:  0000  04 04 00 B7 9E 1C E0 D8  FB B1 E1 2B D7 25 A5 1A   ........ ...+.%..  0010  7F F7 8E 32 2C 21 31 33  30 35 31 33 31 35 34 34   ...2,!13 05131544  0020  32 37 44 69 6E 67 47 31  38 31 38 32 34 41 43 43   27DingG1 81824ACC  0030  54 30 30 30 32 04 06 64  00 00 FA 29 06 00 00 00   T0002..d ...)....  0040  00 28 06 00 00 00 01 20  13 53 45 2D 4B 43 45 4B   .(.....  .SE-KCEK  0050  4D 45 43 45 2D 5A 54 45  2D 31 1A 0C 00 00 0F 3E   MECE-ZTE -1.....>  0060  FE 06 00 00 00 00 01 05  7A 74 65 1F 13 30 30 3A   ........ zte..00:  0070  30 30 3A 30 30 3A 30 30  3A 30 30 3A 30 30 2D 06   00:00:00 :00:00-.  0080  00 00 00 01 05 06 00 00  00 00 3D 06 00 00 00 00   ........ ..=.....  0090  57 27 30 20 31 2F 32 2F  33 3A 38 38 2E 39 39 20   W'0 1/2/ 3:88.99   00A0  7A 74 65 2D 74 38 30 30  30 2F 30 2F 30 2F 30 2F   zte-t800 0/0/0/0/  00B0  30 2F 30 3A 30 2E 30                               0/0:0.0ZXR10 MPU-0/20/0 2013-5-13 07:44:28 APP_RADIUS: packet:   receive Accounting-Response packet 192.168.10.53:1813->100.0.0.250:6118ZXR10 MPU-0/20/0 2013-5-13 07:44:28 APP_RADIUS: packet:   code = 5(Accounting-Response)  id = 4  length = 20  Authenticator = A0 FA 3B 18 38 4F 8A F9 CD D8 F2 2D 13 82 E5 69 ZXR10 MPU-0/20/0 2013-5-13 07:44:28 APP_RADIUS: packet:   radius packet original data:  0000  05 04 00 14 A0 FA 3B 18  38 4F 8A F9 CD D8 F2 2D   ......;. 8O.....-  0010  13 82 E5 69                                        ...i
相关命令 : 
debug radius filtershow debug radius
## debug radius all 

debug radius all 
命令功能 : 
打开/关闭所有RADIUS debug开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius all 
 
no debug radius all 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
RADIUS debug各开关可以同时打开/关闭，也可以分别打开/关闭。RADIUS debug开关按业务分为3种：authentication : 认证；accounting     : 计费；dm-coa         : DM/CoA；其中每种业务按功能分为4种：data  ： RADIUS模块收到与回复的消息内容；event ： 业务运行过程中的事件，比如收发报文；error ： 错误信息；packet： 报文；上面两大类组合出一共12个开关。另外还有一种无业务类型的开关：exception： 异常信息，比如报文长度异常。当某个开关打开时，则相应的信息在运行的过程中实时打印在终端。另外debug打印受debug radius set filter的过滤器影响，在开关的基础上叠加过滤条件，符合条件的才会打印，具体参见debug radius set filter个命令。
范例 : 
打开RADIUS 所有的debug显示（范例为一次认证请求和一次计费开始请求报文）：ZXROSNG#debug radius allZXROSNG#ZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS event: RP Process Authentication RequestZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS data: authtype:PAPZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS data: svrgroup:888ZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS data: username:HUNTERZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS data: ispname:zteZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS event: send access request packet: 100.1.1.1:6024->100.1.1.10:1812ZXR10 MPU-0/20/0 2012-1-7 06:18:35 code = 1  id = 10  length = 139ZXR10 MPU-0/20/0 2012-1-7 06:18:35 authenticator = 5B 42 E0 74 E9 B8 6E C8 ED 7E A7 9D 0C C7 DC 17 ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 1  , length = 12 , value = 48 55 4E 54 45 52 40 7A 74 65  : HUNTER@zteZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 2  , length = 18 , value = 2F AD 07 D9 23 D5 D4 11 82 3C 68 DC BE 78 22 84  : /...#....<h..x".ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 32 , length = 7  , value = 5A 58 52 31 30  : ZXR10ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 4  , length = 6  , value = 64 01 01 01  : d...ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 31 , length = 19 , value = 30 30 3A 30 30 3A 30 30 3A 30 30 3A 30 30 3A 30 30  : 00:00:00:00:00:00ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 61 , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 5  , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 87 , length = 39 , value = 30 20 31 2F 32 2F 33 3A 38 38 2E 39 39 20 7A 74 65 2D 74 38 30 30 30 2F 34 2F 35 2F 36 2F 37 2F 38 3A 30 2E 30  : 0 1/2/3:88.99 zte-t8000/4/5/6/7/8:0.0ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 6  , length = 6  , value = 00 00 00 01  : ....ZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS event: receive access accept packet: 100.1.1.10:1812->100.1.1.1:6024ZXR10 MPU-0/20/0 2012-1-7 06:18:35 code = 2  id = 10  length = 20ZXR10 MPU-0/20/0 2012-1-7 06:18:35 authenticator = 87 FD C7 FF D3 4F 49 96 80 A6 E4 4D 5F F9 6E 13 ZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS event: RADIUS delete request element from group queueZXROSNG#ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: RP Process Accounting RequestZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: accttype:STARTZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: svrgroup:999ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: username:HUNTERZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: ispname:zteZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: acctsession:120107150721DingG181824ACCT0001ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: RADIUS add accounting request to sending queue and send it to serverZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: send accounting request packet 100.1.1.1:6118->100.1.1.10:1813ZXR10 MPU-0/20/0 2012-1-7 07:07:21 code = 4  id = 97  length = 186ZXR10 MPU-0/20/0 2012-1-7 07:07:21 authenticator = 78 75 9F 4D 84 A2 B8 62 C0 8F DC 16 C1 96 F5 42 ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 44 , length = 33 , value = 31 32 30 31 30 37 31 35 30 37 32 31 44 69 6E 67 47 31 38 31 38 32 34 41 43 43 54 30 30 30 31  : 120107150721DingG181824ACCT0001ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 4  , length = 6  , value = 64 01 01 01  : d...ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 41 , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 40 , length = 6  , value = 00 00 00 01  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 32 , length = 7  , value = 5A 58 52 31 30  : ZXR10ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 123, length = 20 , value = 00 40 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 00  : .@123456789012345.ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 1  , length = 12 , value = 48 55 4E 54 45 52 40 7A 74 65  : HUNTER@zteZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 31 , length = 19 , value = 30 30 3A 30 30 3A 30 30 3A 30 30 3A 30 30 3A 30 30  : 00:00:00:00:00:00ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 45 , length = 6  , value = 00 00 00 01  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 5  , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 61 , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 87 , length = 39 , value = 30 20 31 2F 32 2F 33 3A 38 38 2E 39 39 20 7A 74 65 2D 74 38 30 30 30 2F 34 2F 35 2F 36 2F 37 2F 38 3A 30 2E 30  : 0 1/2/3:88.99 zte-t8000/4/5/6/7/8:0.0ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: receive accounting response packet 100.1.1.10:1813->100.1.1.1:6118ZXR10 MPU-0/20/0 2012-1-7 07:07:21 code = 5  id = 97  length = 20ZXR10 MPU-0/20/0 2012-1-7 07:07:21 authenticator = 5F 7D E6 92 85 DF 2A 4B 2D 1B 62 46 68 00 AC 08 ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: RADIUS delete request element from group queue打开RADIUS 所有的debug显示（范例为一次认证请求和一次计费开始请求报文）：ZXROSNG#debug radius allZXROSNG#ZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS event: RP Process Authentication RequestZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS data: authtype:PAPZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS data: svrgroup:888ZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS data: username:HUNTERZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS data: ispname:zteZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS event: send access request packet: 100.1.1.1:6024->100.1.1.10:1812ZXR10 MPU-0/20/0 2012-1-7 06:18:35 code = 1  id = 10  length = 139ZXR10 MPU-0/20/0 2012-1-7 06:18:35 authenticator = 5B 42 E0 74 E9 B8 6E C8 ED 7E A7 9D 0C C7 DC 17 ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 1  , length = 12 , value = 48 55 4E 54 45 52 40 7A 74 65  : HUNTER@zteZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 2  , length = 18 , value = 2F AD 07 D9 23 D5 D4 11 82 3C 68 DC BE 78 22 84  : /...#....<h..x".ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 32 , length = 7  , value = 5A 58 52 31 30  : ZXR10ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 4  , length = 6  , value = 64 01 01 01  : d...ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 31 , length = 19 , value = 30 30 3A 30 30 3A 30 30 3A 30 30 3A 30 30 3A 30 30  : 00:00:00:00:00:00ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 61 , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 5  , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 87 , length = 39 , value = 30 20 31 2F 32 2F 33 3A 38 38 2E 39 39 20 7A 74 65 2D 74 38 30 30 30 2F 34 2F 35 2F 36 2F 37 2F 38 3A 30 2E 30  : 0 1/2/3:88.99 zte-t8000/4/5/6/7/8:0.0ZXR10 MPU-0/20/0 2012-1-7 06:18:35 type = 6  , length = 6  , value = 00 00 00 01  : ....ZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS event: receive access accept packet: 100.1.1.10:1812->100.1.1.1:6024ZXR10 MPU-0/20/0 2012-1-7 06:18:35 code = 2  id = 10  length = 20ZXR10 MPU-0/20/0 2012-1-7 06:18:35 authenticator = 87 FD C7 FF D3 4F 49 96 80 A6 E4 4D 5F F9 6E 13 ZXR10 MPU-0/20/0 2012-1-7 06:18:35 APP_RADIUS: RADIUS event: RADIUS delete request element from group queueZXROSNG#ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: RP Process Accounting RequestZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: accttype:STARTZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: svrgroup:999ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: username:HUNTERZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: ispname:zteZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS data: acctsession:120107150721DingG181824ACCT0001ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: RADIUS add accounting request to sending queue and send it to serverZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: send accounting request packet 100.1.1.1:6118->100.1.1.10:1813ZXR10 MPU-0/20/0 2012-1-7 07:07:21 code = 4  id = 97  length = 186ZXR10 MPU-0/20/0 2012-1-7 07:07:21 authenticator = 78 75 9F 4D 84 A2 B8 62 C0 8F DC 16 C1 96 F5 42 ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 44 , length = 33 , value = 31 32 30 31 30 37 31 35 30 37 32 31 44 69 6E 67 47 31 38 31 38 32 34 41 43 43 54 30 30 30 31  : 120107150721DingG181824ACCT0001ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 4  , length = 6  , value = 64 01 01 01  : d...ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 41 , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 40 , length = 6  , value = 00 00 00 01  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 32 , length = 7  , value = 5A 58 52 31 30  : ZXR10ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 123, length = 20 , value = 00 40 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 00  : .@123456789012345.ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 1  , length = 12 , value = 48 55 4E 54 45 52 40 7A 74 65  : HUNTER@zteZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 31 , length = 19 , value = 30 30 3A 30 30 3A 30 30 3A 30 30 3A 30 30 3A 30 30  : 00:00:00:00:00:00ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 45 , length = 6  , value = 00 00 00 01  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 5  , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 61 , length = 6  , value = 00 00 00 00  : ....ZXR10 MPU-0/20/0 2012-1-7 07:07:21 type = 87 , length = 39 , value = 30 20 31 2F 32 2F 33 3A 38 38 2E 39 39 20 7A 74 65 2D 74 38 30 30 30 2F 34 2F 35 2F 36 2F 37 2F 38 3A 30 2E 30  : 0 1/2/3:88.99 zte-t8000/4/5/6/7/8:0.0ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: receive accounting response packet 100.1.1.10:1813->100.1.1.1:6118ZXR10 MPU-0/20/0 2012-1-7 07:07:21 code = 5  id = 97  length = 20ZXR10 MPU-0/20/0 2012-1-7 07:07:21 authenticator = 5F 7D E6 92 85 DF 2A 4B 2D 1B 62 46 68 00 AC 08 ZXR10 MPU-0/20/0 2012-1-7 07:07:21 APP_RADIUS: RADIUS event: RADIUS delete request element from group queue
相关命令 : 
show debug radiusdebug radius set filter
## debug radius authentication data 

debug radius authentication data 
命令功能 : 
打开/关闭RADIUS认证debug data。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius authentication data 
 
no debug radius authentication data 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS认证debug data。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS 认证组data信息显示：ZXROSNG#debug radius authentication dataZXROSNG#ZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS data: authtype:PAPZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS data: svrgroup:888ZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS data: username:HUNTERZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS data: ispname:zte打开RADIUS 认证组data信息显示：ZXROSNG#debug radius authentication dataZXROSNG#ZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS data: authtype:PAPZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS data: svrgroup:888ZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS data: username:HUNTERZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS data: ispname:zte
相关命令 : 
debug radius filtershow debug radius
## debug radius authentication error 

debug radius authentication error 
命令功能 : 
打开RADIUS 认证组错误信息显示。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius authentication error 
 
no debug radius authentication error 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
打开RADIUS 认证组错误信息显示：ZXROSNG# debug radius authentication errorZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS err :Receive packet vector invalid打开RADIUS 认证组错误信息显示：ZXROSNG# debug radius authentication errorZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS err :Receive packet vector invalid
相关命令 : 
show debug radius all 
## debug radius authentication event 

debug radius authentication event 
命令功能 : 
打开/关闭RADIUS认证debug event。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius authentication event 
 
no debug radius authentication event 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS认证debug event。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS 认证组event信息显示：ZXR10 MPU-0/20/0 2012-1-6 06:29:41 APP_RADIUS: RADIUS event: RP Process Authentication RequestZXR10 MPU-0/20/0 2012-1-6 06:29:41 APP_RADIUS: RADIUS event: send access request packet: 100.1.1.1:6024->100.1.1.10:1812ZXR10 MPU-0/20/0 2012-1-6 06:29:41 APP_RADIUS: RADIUS event: receive access accept packet: 100.1.1.10:1812->100.1.1.1:6024ZXR10 MPU-0/20/0 2012-1-6 06:29:41 APP_RADIUS: RADIUS event: delete RADIUS request element from group queueZXROSNG#ZXR10 MPU-0/20/0 2012-1-6 06:30:39 APP_RADIUS: RADIUS event: RP Process Authentication RequestZXR10 MPU-0/20/0 2012-1-6 06:30:39 APP_RADIUS: RADIUS event: send access request packet: 100.1.1.1:6024->100.1.1.10:1812ZXR10 MPU-0/20/0 2012-1-6 06:30:41 APP_RADIUS: RADIUS event: receive access reject packet: 100.1.1.10:1812->100.1.1.1:6024ZXR10 MPU-0/20/0 2012-1-6 06:30:41 APP_RADIUS: RADIUS event: delete RADIUS request element from group queue打开RADIUS 认证组event信息显示：ZXR10 MPU-0/20/0 2012-1-6 06:29:41 APP_RADIUS: RADIUS event: RP Process Authentication RequestZXR10 MPU-0/20/0 2012-1-6 06:29:41 APP_RADIUS: RADIUS event: send access request packet: 100.1.1.1:6024->100.1.1.10:1812ZXR10 MPU-0/20/0 2012-1-6 06:29:41 APP_RADIUS: RADIUS event: receive access accept packet: 100.1.1.10:1812->100.1.1.1:6024ZXR10 MPU-0/20/0 2012-1-6 06:29:41 APP_RADIUS: RADIUS event: delete RADIUS request element from group queueZXROSNG#ZXR10 MPU-0/20/0 2012-1-6 06:30:39 APP_RADIUS: RADIUS event: RP Process Authentication RequestZXR10 MPU-0/20/0 2012-1-6 06:30:39 APP_RADIUS: RADIUS event: send access request packet: 100.1.1.1:6024->100.1.1.10:1812ZXR10 MPU-0/20/0 2012-1-6 06:30:41 APP_RADIUS: RADIUS event: receive access reject packet: 100.1.1.10:1812->100.1.1.1:6024ZXR10 MPU-0/20/0 2012-1-6 06:30:41 APP_RADIUS: RADIUS event: delete RADIUS request element from group queue
相关命令 : 
debug radius filtershow debug radius
## debug radius authentication packet 

debug radius authentication packet 
命令功能 : 
打开/关闭RADIUS认证debug packet。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius authentication packet 
 
no debug radius authentication packet 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS认证debug packet。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS 认证组packet，相应的debug打印如下：ZXROSNG#debug radius authentication packet RADIUS packet authentication has been turned onZXROSNG#ZXR10 MPU-0/20/0 2013-5-13 07:42:08 APP_RADIUS: packet:   send Access-Request packet 100.0.0.250:6024->192.168.10.53:1812ZXR10 MPU-0/20/0 2013-5-13 07:42:08 APP_RADIUS: packet:   code = 1(Access-Request)  id = 4  length = 106  Authenticator = F6 CB A7 74 71 FB 2B B3 61 47 47 D7 1E D8 EA 31   [Type : Attribute No                   ] [len] [value]  [User-Name : 1                         ] [5  ] [zte]  [User-Password : 2                     ] [18 ] [E1 24 25 FF BD F1 5A 3C 6F D8 75 C7 F3 1D A2 BE ]  [NAS-Identifier : 32                   ] [7  ] [ZXR10]  [NAS-IP-Address : 4                    ] [6  ] [100.0.0.250]  [Calling-Station-Id : 31               ] [19 ] [00:00:00:00:00:00]  [NAS-Port-Type : 61                    ] [6  ] [0:Async]  [NAS-Port : 5                          ] [6  ] [00 00 00 00 ]  [NAS-Port-Id : 87                      ] [19 ] [00:00:00:00:00:00]ZXR10 MPU-0/20/0 2013-5-13 07:42:08 APP_RADIUS: packet:   radius packet original data:  0000  01 04 00 6A F6 CB A7 74  71 FB 2B B3 61 47 47 D7   ...j...t q.+.aGG.  0010  1E D8 EA 31 01 05 7A 74  65 02 12 E1 24 25 FF BD   ...1..zt e...$%..  0020  F1 5A 3C 6F D8 75 C7 F3  1D A2 BE 20 07 5A 58 52   .Z<o.u.. ... .ZXR  0030  31 30 04 06 64 00 00 FA  1F 13 30 30 3A 30 30 3A   10..d... ..00:00:  0040  30 30 3A 30 30 3A 30 30  3A 30 30 3D 06 00 00 00   00:00:00 :00=....  0050  00 05 06 00 00 00 00 57  13 30 30 3A 30 30 3A 30   .......W .00:00:0  0060  30 3A 30 30 3A 30 30 3A  30 30                     0:00:00: 00ZXR10 MPU-0/20/0 2013-5-13 07:42:08 APP_RADIUS: packet:   receive Access-Accept packet 192.168.10.53:1812->100.0.0.250:6024ZXR10 MPU-0/20/0 2013-5-13 07:42:08 APP_RADIUS: packet:   code = 2(Access-Accept)  id = 4  length = 56  Authenticator = D9 13 77 44 4C 75 31 8A 65 73 45 8E FC 1A BC 69   [Type : Attribute No                   ] [len] [value]  [ZTE-Client-DNS-Pri : 3902-1           ] [6  ] [99.99.88.77]  [ZTE-Client-DNS-Sec : 3902-2           ] [6  ] [100.99.88.77]  [Framed-IP-Address : 8                 ] [6  ] [168.10.10.10]  [Framed-IP-Netmask : 9                 ] [6  ] [255.255.255.255]ZXR10 MPU-0/20/0 2013-5-13 07:42:08 APP_RADIUS: packet:   radius packet original data:  0000  02 04 00 38 D9 13 77 44  4C 75 31 8A 65 73 45 8E   ...8..wD Lu1.esE.  0010  FC 1A BC 69 1A 0C 00 00  0F 3E 01 06 63 63 58 4D   ...i.... .>..ccXM  0020  1A 0C 00 00 0F 3E 02 06  64 63 58 4D 08 06 A8 0A   .....>.. dcXM....  0030  0A 0A 09 06 FF FF FF FF                            ........
相关命令 : 
debug radius filtershow debug radius
## debug radius dmcoa data 

debug radius dmcoa data 
命令功能 : 
打开RADIUS DM/CoA data debug信息显示 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius dmcoa data 
 
no debug radius dmcoa data 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS DM/CoA debug data。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS DM/CoA debug data开关，相应的信息显示：ZXROSNG#debug radius dmcoa data     RADIUS data dccoa has been turned onZXROSNG#ZXR10 MPU-0/20/0 2013-5-13 07:18:48 APP_RADIUS: data: result: sent to slaveZXR10 MPU-0/20/0 2013-5-13 07:18:48 APP_RADIUS: data: identifier: 166ZXR10 MPU-0/20/0 2013-5-13 07:18:48 APP_RADIUS: data: request ip: 192.168.10.2ZXR10 MPU-0/20/0 2013-5-13 07:18:48 APP_RADIUS: data: request port: 46489ZXR10 MPU-0/20/0 2013-5-13 07:18:48 APP_RADIUS: data: request vpnid: 0ZXR10 MPU-0/20/0 2013-5-13 07:18:48 APP_RADIUS: data: Error-Cause: 503
相关命令 : 
debug radius filtershow debug radius
## debug radius dmcoa error 

debug radius dmcoa error 
命令功能 : 
打开/关闭RADIUS DM/CoA debug event。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius dmcoa error 
 
no debug radius dmcoa error 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS DM/CoA debug event。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS DM/CoA debug error开关，相应的信息显示：ZXROSNG#debug radius dmcoa error RADIUS error dmcoa has been turned onZXROSNG#ZXR10 MPU-0/20/0 2013-5-13 07:21:39 APP_RADIUS: error: send DM/CoA packet by SIBP failed
相关命令 : 
debug radius filtershow debug radius
## debug radius dmcoa event 

debug radius dmcoa event 
命令功能 : 
打开/关闭RADIUS DM/CoA debug event。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius dmcoa event 
 
no debug radius dmcoa event 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS DM/CoA debug event。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS DM/CoA debug event开关，相应的信息显示：ZXROSNG#debug radius dmcoa eventRADIUS event dmcoa has been turned onZXROSNG#ZXR10 MPU-0/20/0 2013-5-13 07:20:08 APP_RADIUS: event:   receive Disconnect-Request packet 192.168.10.2:39593->192.168.10.101:3799ZXR10 MPU-0/20/0 2013-5-13 07:20:08 APP_RADIUS: event:   send Disconnect-NAK packet 192.168.10.101:3799->192.168.10.2:39593
相关命令 : 
debug radius filtershow debug radius
## debug radius dmcoa packet 

debug radius dmcoa packet 
命令功能 : 
打开/关闭RADIUS DM/CoA debug packet。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius dmcoa packet 
 
no debug radius dmcoa packet 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS DM/CoA debug packet。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS DM/CoA debug packet开关，相应的信息显示：ZXROSNG#debug radius dmcoa packet RADIUS packet dmcoa debugging has been turned onZXROSNG#ZXR10 MPU-0/20/0 2013-5-13 07:22:28 APP_RADIUS: packet:   receive Disconnect-Request packet 192.168.10.2:37473->192.168.10.101:3799ZXR10 MPU-0/20/0 2013-5-13 07:22:28 APP_RADIUS: packet:   code = 40(Disconnect-Request)  id = 214  length = 62  Authenticator = BB D0 50 C1 82 80 F6 14 FE 2D 61 33 99 14 F3 9F   [Type : Attribute No                   ] [len] [value]  [User-Name : 1                         ] [16 ] [testlinux@zte1]  [Acct-Session-Id : 44                  ] [26 ] [testlinuxacct-session-id]ZXR10 MPU-0/20/0 2013-5-13 07:22:28 APP_RADIUS: packet:   radius packet original data:  0000  28 D6 00 3E BB D0 50 C1  82 80 F6 14 FE 2D 61 33   (..>..P. .....-a3  0010  99 14 F3 9F 01 10 74 65  73 74 6C 69 6E 75 78 40   ......te stlinux@  0020  7A 74 65 31 2C 1A 74 65  73 74 6C 69 6E 75 78 61   zte1,.te stlinuxa  0030  63 63 74 2D 73 65 73 73  69 6F 6E 2D 69 64         cct-sess ion-idZXR10 MPU-0/20/0 2013-5-13 07:22:28 APP_RADIUS: packet:   send Disconnect-NAK packet 192.168.10.101:3799->192.168.10.2:37473ZXR10 MPU-0/20/0 2013-5-13 07:22:28 APP_RADIUS: packet:   code = 42(Disconnect-NAK)  id = 214  length = 52  Authenticator = 17 10 43 33 88 7F BA 2D 89 88 18 CA EB 28 84 40   [Type : Attribute No                   ] [len] [value]  [Error-Cause : 101                     ] [6  ] [503:Session-Context-Not-Found]  [Acct-Session-Id : 44                  ] [26 ] [testlinuxacct-session-id]ZXR10 MPU-0/20/0 2013-5-13 07:22:28 APP_RADIUS: packet:   radius packet original data:  0000  2A D6 00 34 17 10 43 33  88 7F BA 2D 89 88 18 CA   *..4..C3 ...-....  0010  EB 28 84 40 65 06 00 00  01 F7 2C 1A 74 65 73 74   .(.@e... ..,.test  0020  6C 69 6E 75 78 61 63 63  74 2D 73 65 73 73 69 6F   linuxacc t-sessio  0030  6E 2D 69 64                                        n-id
相关命令 : 
debug radius filtershow debug radius
## debug radius exception 

debug radius exception 
命令功能 : 
打开/关闭RADIUS异常信息debug打印。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius exception 
 
no debug radius exception 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
打开/关闭RADIUS异常信息debug打印。具体参看命令debug radius all说明。 
范例 : 
打开RADIUS 额外的信息打印显示：ZXROSNG#debug radius exceptionZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS excep:RADIUS insert AVL node failed打开RADIUS 额外的信息打印显示：ZXROSNG#debug radius exceptionZXR10 MPU-0/20/0 2012-1-6 08:45:02 APP_RADIUS: RADIUS excep:RADIUS insert AVL node failed
相关命令 : 
debug radius filtershow debug radius
## debug radius set filter acct-server-group 

debug radius set filter acct-server-group 
命令功能 : 
设置以计费组号为条件的debug过滤器。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius set filter acct-server-group 
  ＜group-name 
＞
no debug radius set filter acct-server-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|服务器组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
该命令设置一个以计费组名为条件的debug打印信息过滤器。配置了该命令后，debug认证信息只打印该计费组下的内容，对所有的计费debug开关均有效。该条件只影响计费debug信息的输出，对其他业务无影响。 
范例 : 
想要只看计费组10的error和packet打印，可以这样设置debug命令：ZXROSNG#debug radius accounting errorRADIUS error accounting has been turned onZXROSNG#debug radius accounting packetRADIUS packet accounting has been turned onZXROSNG#debug radius set filter acct-server-group 10RADIUS filter accounting server-group 10 has been set
相关命令 : 
show debug radius 
## debug radius set filter acct-session-id 

debug radius set filter acct-session-id 
命令功能 : 
设置以属性Acct-Session-Id(标准44号)为匹配条件的过滤器。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius set filter acct-session-id 
  ＜acct-session-id 
＞
no debug radius set filter acct-session-id 
命令参数解释 : 
参数|描述
---|---
＜acct-session-id＞|Acct-Session-Id，范围1-64个字符
缺省 : 
无。 
使用说明 : 
配置这个命令，会将这个条件与报文中含的有Acct-Session-Id进行匹配，命中则打印交互过程中的DEBUG信息。该过滤条件对所有的debug开关均有效。 
范例 : 
想到看到DM/CoA交互流程中包含以下Acct-Session-Id的所有打印: 10228153943DingG181824ACCT:ZXROSNG#debug radius dmcoa errorRADIUS error dmcoa has been turned onZXROSNG#debug radius dmcoa packetRADIUS packet dmcoa has been turned onZXROSNG#debug radius data errordataRADIUS data dmcoa has been turned onZXROSNG#debug radius event packeteventRADIUS event dmcoa has been turned onZXROSNG#debug radius set filter acct-session-id 10228153943DingG181824ACCTRADIUS filter acct-session-id 10228153943DingG181824ACCT has been set
相关命令 : 
show debug radius 
## debug radius set filter authen-server-group 

debug radius set filter authen-server-group 
命令功能 : 
设置以认证组号为条件的debug过滤器。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius set filter authen-server-group 
  ＜group-name 
＞
no debug radius set filter authen-server-group 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|服务器组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
该命令设置一个以认证组名为条件的debug打印信息过滤器。配置了该命令后，debug认证信息只打印该认证组下的内容，对所有的认证debug开关均有效。该条件只影响认证debug信息的输出，对其他业务无影响。 
范例 : 
想要只看认证组10的error和packet打印，可以这样设置debug命令：ZXROSNG#debug radius authentication errorRADIUS error authentication has been turned onZXROSNG#debug radius authentication packetRADIUS packet authentication has been turned onZXROSNG#debug radius set filter authen-server-group 10RADIUS filter authentication server-group 10 has been set
相关命令 : 
show debug radius 
## debug radius set filter client-group 

debug radius set filter client-group 
命令功能 : 
设置以客户端组为条件的debug过滤器。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius set filter client-group 
  ＜client--group-name 
＞
no debug radius set filter client-group 
命令参数解释 : 
参数|描述
---|---
＜client--group-name＞|客户端组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
该命令设置一个以客户端组名为条件的debug打印信息过滤器。配置了该命令后，debug认证信息只打印该客户端组下的内容，对所有的debug开关均有效。 
范例 : 
想要看客户端组yuhuatai信息的error和packet打印，可以这样设置debug命令：ZXROSNG#debug radius accounting errorRADIUS error accounting has been turned onZXROSNG#debug radius accounting packetRADIUS packet accounting has been turned onZXROSNG#debug radius set filter client-group yuhuataiRADIUS filter client-group yuhuatai has been set
相关命令 : 
show debug radius 
## debug radius set filter user 

debug radius set filter user 
命令功能 : 
设置用户名域名为条件的debug过滤器。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug radius set filter user 
  {[username 
 ＜subscriber-name 
＞],[domainname 
 ＜domain-name 
＞]}
no debug radius set filter user 
命令参数解释 : 
参数|描述
---|---
＜subscriber-name＞|用户名称，字符串长度为1-160
＜domain-name＞|域名，字符串长度为1-31
缺省 : 
无。 
使用说明 : 
该命令设置一个以用户名为条件debug信息过滤器，对所有的debug信息均有效。user-name-format命令会影响报文中用户名的呈现形式，而本节的用户名与域名的依据为设备上实际存在的用户名，而不是最后RADIUS报文中组装的用户名。例如：一个PPP用户(用户名为ppp，其所在的域为domainname)上线，认证组下用户名格式配置为：user-name-format strip-domain，最后认证报文中的User-Name属性为ppp，但是想要查看针对该用户名的debug信息，相应的开关为：debug radius user ppp domainname。对于proxy报文，内部会对其按分隔“@”进行解析用户名与域名然后与debug的设置进行匹配。若其内部带的分隔符不是“@”则无法解析，我们的处理是将这个整体当作username字段来处理，根据这个特点，可以将用户名域名的组合都填入username字段中，而不要指定domainname，即可筛选到该类型的打印信息。用户在使用这个命令进行筛选时，应清楚当前所需查看用户名的文本特点，并选择适当的方式配置相应的过滤条件。
范例 : 
如用户名域名为abc@nj，想看这个用户的所有信息：ZXROSNG#debug radius allAll RADIUS debugging has been turned onZXROSNG#debug radius set filter user username abc domainname nj若只是计费发生异常，关注该用户的error信息基本可以定位问题，不想看到那么多的打印则可以作如下配置：ZXROSNG#debug radius accounting errorRADIUS error accounting has been turned onZXROSNG#debug radius set filter user username abc domainname njRADIUS filter user username abc domainname nj has been set此时若想再多一项报文（packet）信息，添加以下命令：ZXROSNG# debug radius accounting packetRADIUS packet accounting has been turned on在上面的基础上，若想看还有没有其他用户有error信息而不只是这个用户，且不再关注packet信息，只需要去掉显示packet的开关来关闭packet的打印，并且把过滤条件也去掉，这时候就能显示所有用户的打印：ZXROSNG#no debug radius accounting packetRADIUS packet accounting has been turned offZXROSNG#no debug radius set filter userRADIUS filter user has been canceled想要查看域名为nj的用户的计费和认证packet信息：ZXROSNG#debug radius authentication packetRADIUS packet authentication has been turned onZXROSNG#debug radius accounting packetRADIUS packet accounting has been turned onZXROSNG#debug radius set filter user domainname njRADIUS filter user domainname nj has been set想要查看走PROXY流程，报文中User-Name(1号属性)字段为abc#shanghai的用户的packet信息(#是用户名分隔符)：ZXROSNG#debug radius authentication packetRADIUS packet authentication has been turned onZXROSNG#debug radius accounting packetRADIUS packet accounting has been turned onZXROSNG#debug radius set filter user username abd#shanghai                       RADIUS filter user username abd#shanghai has been set
相关命令 : 
show debug radius
## default-key 

default-key 
命令功能 : 
设置客户端组使用的默认共享密钥。 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
default-key 
  {encrypted 
 ＜encrypted-key-string 
＞|＜key-string 
＞ [showclear 
]}
no default-key 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key-string＞|加密的共享密钥，长度为64字节
＜key-string＞|未加密的共享密钥，长度为1~31字节
showclear|明文密钥显示标志，缺省为加密显示
缺省 : 
缺省该密钥为空；如果配置有密钥，缺省显示为加密。 
使用说明 : 
客户端组下的客户端若没有配置单独的密钥则采用这个默认共享密钥；注意：RADIUS协议两端通信必须有一个共享密钥，因此客户端组下若配有未指定共享密钥的客户端，需要在组下配置一个默认共享密钥才可以使用。
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#default-key zteZXROSNG(config)#radius client-group bbbZXROSNG(config-radius-clientgrp)#default encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB
相关命令 : 
show running-config radius  
## dm-coa max-retries 

dm-coa max-retries 
命令功能 : 
设置向客户端发送DM/CoA报文的重传次数。 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
dm-coa max-retries 
  ＜retry-time 
＞
no dm-coa max-retries 
命令参数解释 : 
参数|描述
---|---
＜retry-time＞|重传次数，取值范围为1~10次
缺省 : 
3次。 
使用说明 : 
当DM/CoA发送给客户端以后，设备会等待客户端的回应。如果在一定时间(dm-coa timeout)内没有收到回应以后会发起重传，每次重传等待的时间也是dm-coa timeout配置的时间，尝试次数为dm-coa max-retries配置的次数。当几次尝试都没有得到回应，通知应用该请求失败。 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#dm-coa max-retries ?  <1-10>  Max-retries value (default: 3)ZXROSNG(config-radius-clientgrp)#dm-coa max-retries 5ZXROSNG(config-radius-clientgrp)#
相关命令 : 
dm-coa timeout 
## dm-coa timeout 

dm-coa timeout 
命令功能 : 
配置等待客户端回应DM/CoA报文的等待时间。 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
dm-coa timeout 
  ＜timeout 
＞
no dm-coa timeout 
命令参数解释 : 
参数|描述
---|---
＜timeout＞|超时时间，取值范围为1~60,单位为second
缺省 : 
3 seconds。 
使用说明 : 
当DM/CoA发送给客户端以后，设备会等待客户端的回应。如果在这个配置时间内没有收到回应以后会发起重传，每次重传等待的时间也是dm-coa timeout配置的时间，尝试次数为dm-coa max-retries配置的次数。当几次尝试都没有得到回应，通知应用该请求失败。 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#dm-coa timeout ?  <1-60>  Timeout value (default: 3 seconds)ZXROSNG(config-radius-clientgrp)#dm-coa timeout 5ZXROSNG(config-radius-clientgrp)#
相关命令 : 
dm-coa max-retriesshow running-config radius
## dsl-vendor 

dsl-vendor 
命令功能 : 
配置向RADIUS服务器发送的报文中是否包含宽带论坛(DSL）的自定义属性。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
dsl-vendor 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|发送宽带论坛自定义属性
disable|不发送宽带论坛自定义属性
缺省 : 
disable。 
使用说明 : 
当需要向RADIUS服务器上送宽带论坛（DSL, 协议vendor号3561）的自定义属性时打开此开关。 
范例 : 
配置发送的RADIUS计费协议包中发送宽带论坛自定义属性：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#dsl-vendor enable
相关命令 : 
show running-config radius 
## dsl-vendor 

dsl-vendor 
命令功能 : 
配置向RADIUS服务器发送的报文中是否包含宽带论坛(DSL）的自定义属性。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
dsl-vendor 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|发送宽带论坛自定义属性
disable|不发送宽带论坛自定义属性
缺省 : 
disable。 
使用说明 : 
当需要向RADIUS服务器上送宽带论坛（DSL, 协议vendor号3561）的自定义属性时打开此开关。 
范例 : 
配置发送的RADIUS认证协议包中不发送宽带论坛自定义属性：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#dsl-vendor disableZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## filter-id direction 

filter-id direction 
命令功能 : 
配置RADIUS公有11号属性（Filter-Id）的生效方向（数据流上行方向和下行方向）。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
filter-id direction 
  {out 
|in 
|both 
}
no filter-id direction 
命令参数解释 : 
参数|描述
---|---
out|11号filter-id属性在out方向ACL生效
in|11号filter-id属性在in方向ACL生效
both|11号filter-id属性在双向ACL生效
缺省 : 
out。 
使用说明 : 
RADIUS 11号标准属性Filter-Id是一个ACL规则，这个配置指定该ACL规则在数据流的上行（out）还是下行（in）方向生效。当配置为in，Filter-Id作用在下行数据流上，当配置为out，Filter-Id作用在上行数据流上，配置为both，则在两个方向都生效。同时我司有一个属性ZTE-Filter-In（195号）是下行数据流的ACL规则。当该配置为in或者both方向并且Filter-Id下发成功，则下行数据流的ACL规则Filter-Id来执行，ZTE-Filter-In即使下发也不生效。
范例 : 
设置认证服务器组2000 Filter-Id生效方向为双向：ZXROSNG(config)#radius authentication-group 2000ZXROSNG(config-authgrp-2000)#filter-id direction both ZXROSNG(config-authgrp-2000)#
相关命令 : 
show running-config radius 
## flow-unit 

flow-unit 
命令功能 : 
配置RADIUS计费报文中字节流量单位。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
flow-unit 
  {byte 
|kbyte 
|mbyte 
|gbyte 
}
no flow-unit 
命令参数解释 : 
参数|描述
---|---
byte|单位为字节
kbyte|单位为千字节
mbyte|单位为兆字节
gbyte|单位为吉字节
缺省 : 
byte。 
使用说明 : 
为了满足日益增大的网络流量应用，将原有按字节统计的流量配置成更大的单位来统计。可以指定的单位包括字节（byte）、千字节（kbyte）、兆字节。（mbyte）、吉字节（gbyte）。其中转换单位的系数为1024，而非1000。流量属性包括下面几个标准属性（Id:Name）：42：Acct-Input-Octets43：Acct-Output-Octets52：Acct-Input-Gigawords53：Acct-Output-Gigawords
范例 : 
设置计费服务器组1字节流量单位为kbyte：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#flow-unit kbyteZXROSNG(config-acctgrp-1)#no flow-unit
相关命令 : 
show running-config radius 
## ip vrf 

ip vrf 
命令功能 : 
配置改计费组下的服务器归属的VRF 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
ip vrf 
  {mng 
|＜vrf-name 
＞}
no ip vrf 
命令参数解释 : 
参数|描述
---|---
mng|管理口VRF
＜vrf-name＞|VRF名称，长度为1-32个字符
缺省 : 
默认不关联VRF。 
使用说明 : 
一个服务器组的服务器可以与一个VRF关联，不关联VRF的服务器组属于全局路由域。当一个组内切换VRF（新增配置、变更配置或者删除VRF）的时候，认为改组的服务器地址发生了变更（即服务器的地址由VRF、IP地址和Port三元信息来唯一决定），会触发这些服务器关联的请求清除的动作，即正在运行在该组下的业务都将中断。
范例 : 
设置RADIUS计费服务器组和VRF关联：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)# ip vrf vrf1ZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radius 
## ip vrf 

ip vrf 
命令功能 : 
配置改计费组下的服务器归属的VRF 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
ip vrf 
  {mng 
|＜vrf-name 
＞}
no ip vrf 
命令参数解释 : 
参数|描述
---|---
mng|管理口VRF
＜vrf-name＞|VRF名称，长度为1-32个字符
缺省 : 
默认不关联VRF。 
使用说明 : 
一个服务器组的服务器可以与一个VRF关联，不关联VRF的服务器组属于全局路由域。当一个组内切换VRF（新增配置、变更配置或者删除VRF）的时候，认为改组的服务器地址发生了变更（即服务器的地址由VRF、IP地址和Port三元信息来唯一决定），会触发这些服务器关联的请求清除的动作，即正在运行在该组下的业务都将中断。
范例 : 
设置RADIUS认证服务器组和VRF关联：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)# ip vrf vrf1ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## life-time 

life-time 
命令功能 : 
配置计费开始和计费停止报文缓存的生命时间。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
life-time 
  ＜life-time 
＞
no life-time 
命令参数解释 : 
参数|描述
---|---
＜life-time＞|生命时间，范围：2-1024，单位：小时
缺省 : 
2小时。 
使用说明 : 
计费开始报文与计费停止报文在没有得到服务器回应会被缓存到本地一段时间，这个时间长度由叫生命时间。计费报文如果没有得到服务器的回应会被缓存到本地一段时间并伺机再次发送，但当缓存超过生命时间便被丢弃。
范例 : 
配置计费开始和计费结束报文在缓存队列中的生命时间为10（小时）：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)# life-time 10ZXROSNG(config-acctgrp-1)#no life-time
相关命令 : 
local-buffershow running-config radius
## local-buffer 

local-buffer 
命令功能 : 
设置计费服务器组是否将得不到服务器回应的报文进行本地缓存。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
local-buffer 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|启用计费本地缓存
disable|不进行计费本地缓存
缺省 : 
disable。 
使用说明 : 
1. 当计费请求报文没有收到服务器的回应的时候，进行缓存；2. 计费缓存只缓存计费开始包与计费结束包，对于计费中间包不予缓存；3. 计费缓存报文的缓存总时间通过life-time命令来配置；4. 一旦组下有服务器对其他用户的计费请求有回应的时候，计费缓存中的报文将批量向该服务器发出；5. 当服务器一直处于dead状态或者没有回应任何请求，缓存中的报文将每隔30分钟尝试发出去，如果得不到回应将重新入缓存。
范例 : 
设置计费服务器组进行本地缓存：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#local-buffer enableZXROSNG(config-acctgrp-1)#local-buffer disable
相关命令 : 
life-timeshow running-config radius
## max-retries 

max-retries 
命令功能 : 
设置报文的超时重传次数。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
max-retries 
  ＜retry-time 
＞
no max-retries 
命令参数解释 : 
参数|描述
---|---
＜retry-time＞|重传次数，范围：1-255
缺省 : 
3次。 
使用说明 : 
发送给服务器的请求报文的处理描述如下：1. 发起请求，等待回应，如果服务器及时回应，那么处理流程结束；2. 如果在等待了一定的时长（组模式下timeout配置的值）后没有收到回应则认为请求超时，重新发起请求，继续等待回应；4. 重发的过成功如果得到回应则流程结束；3. 一共可以重传(retry)若干次（组配置模式下max-retries配置的值），如果一直得不到回应，则该请求失败并将失败结果通知用户。
范例 : 
设置RADIUS计费服务器超时重发次数为10次：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#max-retries 10ZXROSNG(config-acctgrp-1)#
相关命令 : 
timeoutshow running-config radius
## max-retries 

max-retries 
命令功能 : 
设置报文的超时重传次数。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
max-retries 
  ＜retry-time 
＞
no max-retries 
命令参数解释 : 
参数|描述
---|---
＜retry-time＞|重传次数，范围：1-255
缺省 : 
3次。 
使用说明 : 
发送给服务器的请求报文的处理描述如下：1. 发起请求，等待回应，如果服务器及时回应，那么处理流程结束；2. 如果在等待了一定的时长（组模式下timeout配置的值）后没有收到回应则认为请求超时，重新发起请求，继续等待回应；4. 重发的过成功如果得到回应则流程结束；3. 一共可以重传(retry)若干次（组配置模式下max-retries配置的值），如果一直得不到回应，则该请求失败并将失败结果通知用户。
范例 : 
设置RADIUS认证服务器超时重发10次：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#max-retries 10ZXROSNG(config-authgrp-1)#
相关命令 : 
timeoutshow running-config radius
## nas-identifier 

nas-identifier 
命令功能 : 
配置呈现在RADIUS报文中的设备主机名（NAS-Identifier）。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-identifier 
  ＜nas-identifier 
＞
no nas-identifier 
命令参数解释 : 
参数|描述
---|---
＜nas-identifier＞|设备主机名字符串，长度为1-31个字符
缺省 : 
无。 
使用说明 : 
这个配置将在计费/认证请求报文的NAS-Identifier（标准属性32号）中呈现。如果没有配置，则取NAS的hostname配置。 
范例 : 
设置RADIUS计费组设备主机名为 ZXR-10：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)# nas-identifier ZXR-10ZXROSNG(config-acctgrp-1)#no nas-identifier
相关命令 : 
show running-config radius 
## nas-identifier 

nas-identifier 
命令功能 : 
配置呈现在RADIUS报文中的设备主机名（NAS-Identifier）。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-identifier 
  ＜nas-identifier 
＞
no nas-identifier 
命令参数解释 : 
参数|描述
---|---
＜nas-identifier＞|设备主机名字符串，长度为1-31个字符
缺省 : 
无。 
使用说明 : 
这个配置将在计费/认证请求报文的NAS-Identifier（标准属性32号）中呈现。如果没有配置，则取NAS的hostname配置。 
范例 : 
设置RADIUS认证组设备主机名为 ZXR-10：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)# nas-identifier ZXR-10ZXROSNG(config-authgrp-1)# no nas-identifier
相关命令 : 
show running-config radius 
## nas-ip-address 

nas-ip-address 
命令功能 : 
用于设置RADIUS服务器的NAS-IP，对应协议包的NAS-IP-Address字段和协议包的源IP地址，该命令同时支持配置引用接口源地址作为RADIUS服务器的NAS-IP地址。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-ip-address 
  {＜nas-ipv4-address 
＞|source-interface 
 ＜local-interface 
＞}
no nas-ip-address 
命令参数解释 : 
参数|描述
---|---
＜nas-ipv4-address＞|NAS-IP-Address
＜local-interface＞|本地接口名
缺省 : 
无。 
使用说明 : 
1.同一个组内的NAS的IP地址与服务器的IP地址的类型需要相互匹配，即都是IPv6或者都是IPv4。2.由于NAS-IP-Address同时作为RADIUS报文的源地址，所以该配置是必选配置，否则RADIUS报文将无法成功组包。3.配置为引用接口时，引用的是接口上的主地址（IPV4）。4.配置命令时，接口上可以没有配置地址，没有配置引用接口、接口上没有配置IPv4主地址、接口状态为down、接口主地址删除，这几种情况导致的结果都是NAS IP不可用，此时RADIUS的行为逻辑和没有配置nas-ip-address时一致，具体而言，是认为正在处理的用户会话本次发送报文操作失败，不立即丢弃用户会话本身，用户会话的重传操作可以并继续进行。5.新增配置引用接口、接口上增加配置主地址、接口状态由down转up，这几种情况导致的结果是NAS IP变化为可用，此时RADIUS模块的行为和配置了nas-ip-address行为一致，具体而言，需要对以后处理的用户会话都使用(新的)NAS IP地址，包括已经排队缓存的用户会话。
范例 : 
1.设置RADIUS计费服务器的NAS-IP-Address为192.168.70.2：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#nas-ip-address 192.168.70.2ZXROSNG(config-acctgrp-1)#no nas-ip-address2.设置RADIUS计费服务器的NAS-IP-Address为引用本地接口gei-0/1/0/8ZXROSNG(config- acctgrp-1)#nas-ip-address source-interface gei-0/1/0/8ZXROSNG(config- acctgrp-1)#show this!<radius>  nas-ip-address source-interface gei-0/1/0/8  server 1 192.168.122.22 key encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB!</radius>ZXROSNG(config- acctgrp-1)#
相关命令 : 
show running-config radiusserverserver6interface 
## nas-ip-address 

nas-ip-address 
命令功能 : 
用于设置RADIUS服务器的NAS-IP，对应协议包的NAS-IP-Address字段和协议包的源IP地址，该命令同时支持配置引用接口源地址作为RADIUS服务器的NAS-IP地址。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-ip-address 
  {＜nas-ipv4-address 
＞|source-interface 
 ＜local-interface 
＞}
no nas-ip-address 
命令参数解释 : 
参数|描述
---|---
＜nas-ipv4-address＞|NAS-IP-Address
＜local-interface＞|本地接口名
缺省 : 
无。 
使用说明 : 
1.同一个组内的NAS的IP地址与服务器的IP地址的类型需要相互匹配，即都是IPv6或者都是IPv4。2.由于NAS-IP-Address同时作为RADIUS报文的源地址，所以该配置是必选配置，否则RADIUS报文将无法成功组包。3.配置为引用接口时，引用的是接口上的主地址（IPV4）。4.配置命令时，接口上可以没有配置地址，没有配置引用接口、接口上没有配置IPv4主地址、接口状态为down、接口主地址删除，这几种情况导致的结果都是NAS IP不可用，此时RADIUS的行为逻辑和没有配置nas-ip-address时一致，具体而言，是认为正在处理的用户会话本次发送报文操作失败，不立即丢弃用户会话本身，用户会话的重传操作可以并继续进行。5.新增配置引用接口、接口上增加配置主地址、接口状态由down转up，这几种情况导致的结果是NAS IP变化为可用，此时RADIUS模块的行为和配置了nas-ip-address行为一致，具体而言，需要对以后处理的用户会话都使用(新的)NAS IP地址，包括已经排队缓存的用户会话。
范例 : 
1.设置RADIUS认证服务器的NAS-IP-Address为192.168.70.2：ZXROSNG(config)# radius authentication-group 1ZXROSNG(config-authgrp-1)#nas-ip-address 192.168.70.2ZXROSNG(config-authgrp-1)#no nas-ip-address2.设置RADIUS认证服务器的NAS-IP-Address为引用本地接口gei-0/1/0/8ZXROSNG(config-authgrp-1)#nas-ip-address source-interface gei-0/1/0/8ZXROSNG(config-authgrp-1)#show this!<radius>  nas-ip-address source-interface gei-0/1/0/8  server 1 192.168.122.22 key encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB!</radius>ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radiusserverserver6
## nas-ipv6-address 

nas-ipv6-address 
命令功能 : 
用于设置NAS的IPv6地址，对应协议包的NAS-IPv6-Address字段和协议包的源IPv6地址，该命令同时支持配置引用接口源地址作为NAS的IPv6地址。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-ipv6-address 
  {＜nas-ipv6-address 
＞|source-interface 
 ＜local-interface 
＞}
no nas-ipv6-address 
命令参数解释 : 
参数|描述
---|---
＜nas-ipv6-address＞|NAS-IPv6-Address
＜local-interface＞|本地接口名
缺省 : 
无。 
使用说明 : 
1.同一个组内的NAS的IP地址与服务器的IP地址的类型需要相互匹配，即都是IPv6或者都是IPv4。2.由于NAS-IPv6-Address同时作为RADIUS报文的源地址，所以该配置是必选配置，否则RADIUS报文将无法成功组包。3.配置为引用接口时，引用地址为引用接口上的某一个符合条件的地址，条件包括1）全球单播地址；2）非linklocal地址；3）非IN6_IFF_NOTREADY、IN6_IFF_ANYCAST和IN6_IFF_DETACHED中任一状态的IPv6地址。4.配置命令时，接口上可以没有配置地址，没有配置引用接口、接口上没有配置IPv4主地址、接口状态为down、接口主地址删除，接口上不存在符合条件的IPv6地址，这几种情况导致的结果都是NAS IP不可用，此时RADIUS的行为逻辑和没有配置nas-ip-address时一致，具体而言，是认为正在处理的用户会话本次发送报文操作失败，不立即丢弃用户会话本身，用户会话的重传操作可以并继续进行。5.新增配置引用接口、接口上增加配置主地址、接口状态由down转up，接口上出现存在符合条件的IPv6地址，这几种情况导致的结果是NAS IP变化为可用，此时RADIUS模块的行为和配置了nas-ip-address行为一致，具体而言，需要对以后处理的用户会话都使用(新的)NAS IP地址，包括已经排队缓存的用户会话。
范例 : 
1.设置RADIUS计费服务器的Nas-IPv6-Address为2000::1：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#nas-ipv6-address 2000::1ZXROSNG(config-acctgrp-1)#no nas-ipv6-address 2.设置RADIUS计费服务器的Nas-IPv6-Address为引用本地接口gei-0/1/0/6ZXROSNG(config)#interface gei-0/1/0/6ZXROSNG(config-if-gei-0/1/0/6)#show this!<if-intf>  ipv6 enable  no shutdown!</if-intf>ZXROSNG(config-if-gei-0/1/0/6)#exitZXROSNG(config)# radius accounting-group 1ZXROSNG(config- acctgrp-1)#nas-ipv6-address source-interface gei-0/1/0/6ZXROSNG(config- acctgrp-1)#show this!<radius>  nas-ipv6-address source-interface gei-0/1/0/6!</radius>ZXROSNG(config- acctgrp-1)#no nas-ipv6-addressZXROSNG(config- acctgrp-1)#show thisZXROSNG(config- acctgrp-1)#
相关命令 : 
show running-config radiusserverserver6interface
## nas-ipv6-address 

nas-ipv6-address 
命令功能 : 
用于设置NAS的IPv6地址，对应协议包的NAS-IPv6-Address字段和协议包的源IPv6地址，该命令同时支持配置引用接口源地址作为NAS的IPv6地址。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-ipv6-address 
  {＜nas-ipv6-address 
＞|source-interface 
 ＜local-interface 
＞}
no nas-ipv6-address 
命令参数解释 : 
参数|描述
---|---
＜nas-ipv6-address＞|NAS-IPv6-Address
＜local-interface＞|本地接口名
缺省 : 
无。 
使用说明 : 
1.同一个组内的NAS的IP地址与服务器的IP地址的类型需要相互匹配，即都是IPv6或者都是IPv4。2.由于NAS-IPv6-Address同时作为RADIUS报文的源地址，所以该配置是必选配置，否则RADIUS报文将无法成功组包。3.配置为引用接口时，引用地址为引用接口上的某一个符合条件的地址，条件包括    1）全球单播地址；    2）    非linklocal地址；    3）非IN6_IFF_NOTREADY、IN6_IFF_ANYCAST和IN6_IFF_DETACHED中任一状态的IPv6地址。4.配置命令时，接口上可以没有配置地址，没有配置引用接口、接口上没有配置IPv4主地址、接口状态为down、接口主地址删除，接口上不存在符合条件的IPv6地址，这几种情况导致的结果都是NAS IP不可用，此时RADIUS的行为逻辑和没有配置nas-ip-address时一致，具体而言，是认为正在处理的用户会话本次发送报文操作失败，不立即丢弃用户会话本身，用户会话的重传操作可以并继续进行。5.新增配置引用接口、接口上增加配置主地址、接口状态由down转up，接口上出现存在符合条件的IPv6地址，这几种情况导致的结果是NAS IP变化为可用，此时RADIUS模块的行为和配置了nas-ip-address行为一致，具体而言，需要对以后处理的用户会话都使用(新的)NAS IP地址，包括已经排队缓存的用户会话。
范例 : 
1.设置计费服务器1 2000::10 为主服务器，共享密钥为“zte”，明文密钥显示：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#server6 1 2000::10 key zte showclear ZXROSNG(config-acctgrp-1)#show this!<radius>  server6 1 2000::10 key zte showclear!</radius>ZXROSNG(config-acctgrp-1)#2.设置计费服务器1 2000::10 为主服务器，共享密钥为“zte”，密文密钥显示：ZXROSNG(config-acctgrp-1)#server6 1 2000::10 key zte ZXROSNG(config-acctgrp-1)#show this!<radius>  server6 1 2000::10 key encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB!</radius>ZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radiusserverserver6
## nas-port-format user-defined 

nas-port-format user-defined 
命令功能 : 
配置NAS-Port属性字段格式定义。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-port-format user-defined 
  ＜user-defined-string 
＞
no nas-port-format user-defined 
命令参数解释 : 
参数|描述
---|---
＜user-defined-string＞|NAS-Port 属性自定义格式，1~31个字符
缺省 : 
无。 
使用说明 : 
举例格式：s8b4p8i12字母标识对应字段关系为:s:slot， b:subslot， p:port， e:Ex-Vlan， i:In-Vlan， z:0（0填充）， n:1（1填充）字母后面跟数字表示位宽，所有字段位宽加起来必须等于32。
范例 : 
配置向计费服务器发送的NAS-Port字段格式为8位的slot、8位的port，16位的In-Vlan组合：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#nas-port-format user-defined s8p8i16ZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radius 
## nas-port-format user-defined 

nas-port-format user-defined 
命令功能 : 
配置NAS-Port属性字段格式定义。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-port-format user-defined 
  ＜user-defined-string 
＞
no nas-port-format user-defined 
命令参数解释 : 
参数|描述
---|---
＜user-defined-string＞|NAS-Port 属性自定义格式，1~31个字符
缺省 : 
无。 
使用说明 : 
举例格式：s8b4p8i12字母标识对应字段关系为:s:slot， b:subslot， p:port， e:Ex-Vlan， i:In-Vlan， z:0（0填充）， n:1（1填充）字母后面跟数字表示位宽，所有字段位宽加起来必须等于32。
范例 : 
配置向认证服务器发送的NAS-Port字段格式为8位的slot、8位的port，16位的In-Vlan组合：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#nas-port-format user-defined s8p8i16ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## nas-port-id-format 

nas-port-id-format 
命令功能 : 
配置Nas-Port-Id属性字段格式定义。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-port-id-format 
  {china-tel 
|china-unicom 
|china-tel-keep-remote-info 
|local-and-agent-circuit-id 
|class1 
|class2 
|class3 
|class4 
|class5 
|class6 
|class7 
|class8 
|keep-agent-circuit-id 
|user-defined 
 [{[slot 
],[port 
],[sub-slot 
],[vlan 
],[second-vlan 
],[vlan-invalid 
],[second-vlan-invalid 
]}] text 
 ＜text-string 
＞}
no nas-port-id-format 
命令参数解释 : 
参数|描述
---|---
china-tel|电信格式，形式为：{atm|eth|trunk} slotNAS_subslot/port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port:ANI_XPI.ANI_XCI。其中{atm|eth|trunk}表示NAS-Port-Type，如果不在这三者之内直接显示其数值；AccessNodeIdentifier为字符串，其他参数为十进制形式
china-unicom|表示联通接入方式，包含ONU设备信息，包含PON信息，有XPIXCI信息：----------{eth|trunk} NAS_slot/NAS_subslot/NAS_port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port/ONU_ID ONU_Slot/ONU_Subslot/Port_ID:{ptm|atm|eth}/Port_XPI.Port_XCI [{EP|GP}] 以上{AD|V2}和{EP|GP}都支持作为可选项，有则打印；AccessNodeIdentifier、ONU_ID、{atm|eth|trunk}、{AD|V2}和{EP|GP}为字符串形式，其他参数为十进制数字；其中{atm|eth|trunk}表示NAS-Port-Type，如果不在这三者之内直接显示其数值
china-tel-keep-remote-info|保持远端信息的电信格式，该格式下local信息按照电路格式组织并保持远端设备定位信息不变
local-and-agent-circuit-id|在option82或者PPPOE+或者VBAS之前加上bras的位置信息
class1|class1格式为：为十六进制数值的排列并打印成字符串的形式，各域排列顺序为：slot port vpi vci vlan-out，字符宽度为（2 2 2 4 4）
class2|class2格式为明文编码方式，是华为定义的格式，格式为：slot=xx;subslot=xx;port=xx;vlanid=xx;vlanid2=xx
class3|class3格式为：：为十六进制数值的排列并打印成字符串的形式，各域排列顺序为：slot port vpi vci vlanid，无分隔符，字符宽度为（2 2 2 4 4）,若VLAN无效，则以ffff来填充
class4|class4格式为：slot=xx;subslot=xx;port=xx;vlanid=xx;vlanid2=xx，其中xx表示各数值的十进制打印形式
class5|AccessNodeIdentifier {atm|eth|unknown} ANI_frame/ANI_slot/ANI_subslot/ANI_port:ANI_XPI.ANI_XCI当接入线路为eth时，(:ANI_XPI.ANI_XCI部分)需要根据其数值有效性(1-4095为有效)来选择形式:若都无效，则不包含该部分的信息；若ANI_XCI无效，则为(:ANI_XPI)；若ANI_XPI无效，则为(:ANI_XCI)
class6|土电physical格式，格式为：1. 若为LNS用户，则为：256/172. 若接入类型为ATM：slot/port vpi-vci vpi vci，其中vpi-vci为关键词，其余为数值的十进制形式；3. 若接入类型为ETH和TRUNK：slot/port vlan-id vlan-out:vlan-in，其中vlan-id为关键词，其他为数值的十进制形式；若VLAN包含无效的数值（有效为1-4095），则只包含有效的部分，如：vlan-in无效，则vlan部分为vlan-id vlan-out，vlan-out无效，则vlan部分为vlan-id vlan-in，两者都无效则无VLAN部分
class7|土电all格式，格式为：1. LNS用户：固定填入L2TP LNS2. PPPOE和LAC用户：1）ATM接入： slot/port vpi-vci vpi vci pppoe sess-id2）ETM和TRUNK接入： slot/port vlan-id vlan-out:vlan-in pppoe sess-id3. 其他用户类型与PPPOE和LAC用户类型的区别是不包含pppoe sess-id部分其中：vpi-vci、vlan-id、pppoe为关键字，其他数值为十进制形式；若VLAN包含无效的数值（有效为1-4095），则只包含有效的部分，如：vlan-in无效，则vlan部分为vlan-id vlan-out，vlan-out无效，则vlan部分为vlan-id vlan-in，两者都无效则无VLAN部分
class8|广东联通格式，格式为：主机名 {atm|eth} 0/槽位号/子槽位号/端口号:{vpi.vci|vlan|evlan.ivlan}1. ATM： hostname atm 0/slot/subslot/port:vpi.vci2. ETH和TRUNK： hostname eth 0/slot/subslot/port:vlan-out.vlan-in各数值为十进制形式；若VLAN包含无效的数值（有效为1-4095），则只包含有效的部分，如：vlan-in无效，则vlan部分为:vlan-out，vlan-out无效，则vlan部分为vlan-in，两者都无效则无VLAN部分
keep-agent-circuit-id|透传模式，透传下联设备的agent-circuit-id用户线路信息
user-defined|支持NAS-Port-Id按照用户配置的字符串格式编码，slot、subslot、port、vlan、second-vlan可选择
slot|slot选项
port|port选项
sub-slot|sub-slot选项
vlan|vlan选项
second-vlan|second-vlan选项
vlan-invalid|vlan-invalid选项
second-vlan-invalid|second-vlan-invalid选项
＜text-string＞|格式字符串，1~88字符
缺省 : 
默认值是china-tel，代表电信格式。 
使用说明 : 
user-defined格式在slot、subslot、port、vlan、second-vlan、vlan-invalid、second-vlan-invalid中选择希望在NAS-Port-Id中携带的参数；参数组织格式由text输入的字符串决定，格式串采用ANSIC标准C语言定义的格式化输入字符串。格式字符说明：d    ：以带符号的十进制形式输出整数（正数不输出符号）x, X    ：以十六进制无符号形式输出整数（不输出前导符0x）， 用x则输出十六进制数的a~f时以小写形式输出。用X时，则以大写字母输出u    ：以无符号十进制形式输出整数字母l    ：用于长整型整数，可加在格式符d，x，X，u前面数字m    ：加在以上格式字符组合前面，表示最小输出宽度，不满足最小宽度用默认使用空格填充，超过最大按实际宽度输出数字n    ：加在以上格式字符组合前面，表示不足宽度要求用来填充的数字需要注意的是：选中可选选项(可选项vlan-invalid和second-vlan-invalid除外)的个数必须与后面格式化输入格式控制字符的个数一致。用户自定义格式配置字符串最多支持4条配置，以vlan-invalid和second-vlan-invalid区分，即1）类型1：均未选中选项vlan-invalid和second-vlan-invalid；2）类型2：仅选中选项vlan-invalid；3）类型3：仅选中选项second-vlan-invalid； 4）类型4：均选中选项vlan-invalid和second-vlan-invalid；以上支持4种类型的独立各自更新，不支持单独no掉某一个用户自定义格式字符串，要no都会no掉，即恢复默认值china-tel，同理，如果修改为某一个非用户自定义格式的话，那么之前配置的自定义格式串都会被no掉；vlan-invalid与second-vlan-invalid关键词的作用是匹配在用户传递vlan或second-vlan的值是无效(有效范围为1-4095)的条件下的特殊格式，举例：若用户传递的vlan值无效，则在匹配有vlan-invalid这条格式的配置；second-vlan同理；若vlan与second-vlan都无效，则匹配有vlan-invalid与second-vlan-invalid这条格式的配置。若这些情况下并没有匹配到相应的配置，则使用默认的配置（无vlan-invalid与second-vlan-invalid，相当于不管是否有效）。
范例 : 
配置NAS-Port-Id为联通格式china-unicom：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#nas-port-id-format china-unicomZXROSNG(config-acctgrp-1)#配置自定义格式的期望效果为：slot=xx::sub-slot=xx::port=xx::valn=xxxx.second-vlan=xxxx，其中'x'表示其数值，个数表示其字节数：ZXROSNG(config-authgrp-1)#nas-port-id-format user-defined  slot sub-slot port vlan second-vlan text slot=%02x::sub-slot=%02x::port=%02x::valn=%04x.second-vlan=%04xZXROSNG(config-authgrp-1)#同时期望如果在vlan无效的情况下的格式为：slot=xx::sub-slot=xx::port=xx::valn=xxxx.second-vlan=xxxx*THIS VLAN IS INVALID*ZXROSNG(config-authgrp-1)#$  slot sub-slot port vlan second-vlan vlan-invalid  text slot=%02x::sub-slot=%02x::port=%02x::valn=%04x.second-vlan=%04x*THIS VLAN IS INVALID*ZXROSNG(config-authgrp-1)#show this!<radius>nas-port-id-format user-defined slot sub-slot port vlan second-vlan text slot=%02x::sub-slot=%02x::port=%02x::valn=%04x.second-vlan=%04xnas-port-id-format user-defined slot sub-slot port vlan second-vlan vlan-invalid text slot=%02x::sub-slot=%02x::port=%02x::valn=%04x.second-vlan=%04x*THIS VLAN IS INVALID*!</radius>ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## nas-port-id-format 

nas-port-id-format 
命令功能 : 
配置Nas-Port-Id属性字段格式定义。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
nas-port-id-format 
  {china-tel 
|china-unicom 
|china-tel-keep-remote-info 
|local-and-agent-circuit-id 
|class1 
|class2 
|class3 
|class4 
|class5 
|class6 
|class7 
|class8 
|keep-agent-circuit-id 
|user-defined 
 [{[slot 
],[port 
],[sub-slot 
],[vlan 
],[second-vlan 
],[vlan-invalid 
],[second-vlan-invalid 
]}] text 
 ＜text-string 
＞}
no nas-port-id-format 
命令参数解释 : 
参数|描述
---|---
china-tel|电信格式，形式为：{atm|eth|trunk} slotNAS_subslot/port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port:ANI_XPI.ANI_XCI。其中{atm|eth|trunk}表示NAS-Port-Type，如果不在这三者之内直接显示其数值；AccessNodeIdentifier为字符串，其他参数为十进制形式
china-unicom|表示联通接入方式，包含ONU设备信息，包含PON信息，有XPIXCI信息：----------{eth|trunk} NAS_slot/NAS_subslot/NAS_port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port/ONU_ID ONU_Slot/ONU_Subslot/Port_ID:{ptm|atm|eth}/Port_XPI.Port_XCI [{EP|GP}] 以上{AD|V2}和{EP|GP}都支持作为可选项，有则打印；AccessNodeIdentifier、ONU_ID、{atm|eth|trunk}、{AD|V2}和{EP|GP}为字符串形式，其他参数为十进制数字；其中{atm|eth|trunk}表示NAS-Port-Type，如果不在这三者之内直接显示其数值
china-tel-keep-remote-info|保持远端信息的电信格式，该格式下local信息按照电路格式组织并保持远端设备定位信息不变
local-and-agent-circuit-id|在option82或者PPPOE+或者VBAS之前加上bras的位置信息
class1|class1格式为：为十六进制数值的排列并打印成字符串的形式，各域排列顺序为：slot port vpi vci vlan-out，字符宽度为（2 2 2 4 4）
class2|class2格式为明文编码方式，是华为定义的格式，格式为：slot=xx;subslot=xx;port=xx;vlanid=xx;vlanid2=xx
class3|class3格式为：：为十六进制数值的排列并打印成字符串的形式，各域排列顺序为：slot port vpi vci vlanid，无分隔符，字符宽度为（2 2 2 4 4）,若VLAN无效，则以ffff来填充
class4|class4格式为：slot=xx;subslot=xx;port=xx;vlanid=xx;vlanid2=xx，其中xx表示各数值的十进制打印形式
class5|AccessNodeIdentifier {atm|eth|unknown} ANI_frame/ANI_slot/ANI_subslot/ANI_port:ANI_XPI.ANI_XCI当接入线路为eth时，(:ANI_XPI.ANI_XCI部分)需要根据其数值有效性(1-4095为有效)来选择形式:若都无效，则不包含该部分的信息；若ANI_XCI无效，则为(:ANI_XPI)；若ANI_XPI无效，则为(:ANI_XCI)
class6|土电physical格式，格式为：1. 若为LNS用户，则为：256/172. 若接入类型为ATM：slot/port vpi-vci vpi vci，其中vpi-vci为关键词，其余为数值的十进制形式；3. 若接入类型为ETH和TRUNK：slot/port vlan-id vlan-out:vlan-in，其中vlan-id为关键词，其他为数值的十进制形式；若VLAN包含无效的数值（有效为1-4095），则只包含有效的部分，如：vlan-in无效，则vlan部分为vlan-id vlan-out，vlan-out无效，则vlan部分为vlan-id vlan-in，两者都无效则无VLAN部分
class7|土电all格式，格式为：1. LNS用户：固定填入L2TP LNS2. PPPOE和LAC用户：1）ATM接入： slot/port vpi-vci vpi vci pppoe sess-id2）ETM和TRUNK接入： slot/port vlan-id vlan-out:vlan-in pppoe sess-id3. 其他用户类型与PPPOE和LAC用户类型的区别是不包含pppoe sess-id部分其中：vpi-vci、vlan-id、pppoe为关键字，其他数值为十进制形式；若VLAN包含无效的数值（有效为1-4095），则只包含有效的部分，如：vlan-in无效，则vlan部分为vlan-id vlan-out，vlan-out无效，则vlan部分为vlan-id vlan-in，两者都无效则无VLAN部分
class8|广东联通格式，格式为：主机名 {atm|eth} 0/槽位号/子槽位号/端口号:{vpi.vci|vlan|evlan.ivlan}1. ATM： hostname atm 0/slot/subslot/port:vpi.vci2. ETH和TRUNK： hostname eth 0/slot/subslot/port:vlan-out.vlan-in各数值为十进制形式；若VLAN包含无效的数值（有效为1-4095），则只包含有效的部分，如：vlan-in无效，则vlan部分为:vlan-out，vlan-out无效，则vlan部分为vlan-in，两者都无效则无VLAN部分
keep-agent-circuit-id|透传模式，透传下联设备的agent-circuit-id用户线路信息
user-defined|支持NAS-Port-Id按照用户配置的字符串格式编码，slot、subslot、port、vlan、second-vlan可选择
slot|slot选项
port|port选项
sub-slot|sub-slot选项
vlan|vlan选项
second-vlan|second-vlan选项
vlan-invalid|vlan-invalid选项
second-vlan-invalid|second-vlan-invalid选项
＜text-string＞|格式字符串，1~88字符
缺省 : 
默认值是china-tel，代表电信格式。 
使用说明 : 
user-defined格式在slot、subslot、port、vlan、second-vlan、vlan-invalid、second-vlan-invalid中选择希望在NAS-Port-Id中携带的参数；参数组织格式由text输入的字符串决定，格式串采用ANSIC标准C语言定义的格式化输入字符串。格式字符说明：d    ：以带符号的十进制形式输出整数（正数不输出符号）x, X    ：以十六进制无符号形式输出整数（不输出前导符0x）， 用x则输出十六进制数的a~f时以小写形式输出。用X时，则以大写字母输出u    ：以无符号十进制形式输出整数字母l    ：用于长整型整数，可加在格式符d，x，X，u前面数字m    ：加在以上格式字符组合前面，表示最小输出宽度，不满足最小宽度用默认使用空格填充，超过最大按实际宽度输出数字n    ：加在以上格式字符组合前面，表示不足宽度要求用来填充的数字需要注意的是：选中可选选项(可选项vlan-invalid和second-vlan-invalid除外)的个数必须与后面格式化输入格式控制字符的个数一致。用户自定义格式配置字符串最多支持4条配置，以vlan-invalid和second-vlan-invalid区分，即1）类型1：均未选中选项vlan-invalid和second-vlan-invalid；2）类型2：仅选中选项vlan-invalid；3）类型3：仅选中选项second-vlan-invalid； 4）类型4：均选中选项vlan-invalid和second-vlan-invalid；以上支持4种类型的独立各自更新，不支持单独no掉某一个用户自定义格式字符串，要no都会no掉，即恢复默认值china-tel，同理，如果修改为某一个非用户自定义格式的话，那么之前配置的自定义格式串都会被no掉；vlan-invalid与second-vlan-invalid关键词的作用是匹配在用户传递vlan或second-vlan的值是无效(有效范围为1-4095)的条件下的特殊格式，举例：若用户传递的vlan值无效，则在匹配有vlan-invalid这条格式的配置；second-vlan同理；若vlan与second-vlan都无效，则匹配有vlan-invalid与second-vlan-invalid这条格式的配置。若这些情况下并没有匹配到相应的配置，则使用默认的配置（无vlan-invalid与second-vlan-invalid，相当于不管是否有效）。
范例 : 
配置NAS-Port-Id为联通格式china-unicom：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#nas-port-id-format china-unicomZXROSNG(config-acctgrp-1)#配置自定义格式的期望效果为：slot=xx::sub-slot=xx::port=xx::valn=xxxx.second-vlan=xxxx，其中'x'表示其数值，个数表示其字节数：ZXROSNG(config-authgrp-1)#nas-port-id-format user-defined  slot sub-slot port vlan second-vlan text slot=%02x::sub-slot=%02x::port=%02x::valn=%04x.second-vlan=%04xZXROSNG(config-authgrp-1)#
同时期望如果在vlan无效的情况下的格式为：slot=xx::sub-slot=xx::port=xx::valn=xxxx.second-vlan=xxxx*THIS VLAN IS INVALID*ZXROSNG(config-authgrp-1)#$  slot sub-slot port vlan second-vlan vlan-invalid  text slot=%02x::sub-slot=%02x::port=%02x::valn=%04x.second-vlan=%04x*THIS VLAN IS INVALID*ZXROSNG(config-authgrp-1)#show this!<radius>nas-port-id-format user-defined slot sub-slot port vlan second-vlan text slot=%02x::sub-slot=%02x::port=%02x::valn=%04x.second-vlan=%04xnas-port-id-format user-defined slot sub-slot port vlan second-vlan vlan-invalid text slot=%02x::sub-slot=%02x::port=%02x::valn=%04x.second-vlan=%04x*THIS VLAN IS INVALID*!</radius>ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## queue-depth 

queue-depth 
命令功能 : 
（注意，该命令已废弃）配置RADIUS组下认证报文队列深度。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
queue-depth 
  ＜queue-depth 
＞
no queue-depth 
命令参数解释 : 
参数|描述
---|---
＜queue-depth＞|发送速度的倍数，范围1-20
缺省 : 
默认值是3。 
使用说明 : 
设置认证组的请求报文队列缓存深度（同一时刻认证请求的并发数），报文队列数目最大值为send-rate-limit*queue-depth；另并发数受性能参数的控制。因此队列深度为send-rate-limit*queue-depth与性能参数两者中较小的值.。 
范例 : 
配置认证组下queue-depth值为5：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)# queue-depth 5ZXROSNG(config-authgrp-1)#
相关命令 : 
send-rate-limit 
## radius accounting-group 

radius accounting-group 
命令功能 : 
进入ACCOUNT_GROUP模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius accounting-group 
  ＜group-name 
＞
no radius accounting-group 
  ＜group-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-name＞|RADIUS计费服务器组的组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
此命令创建一个RADIUS计费组，并进入RADIUS组配置模式。当组名指向的组已经存在时则进入该组的配置模式。设备能配置的计费组总数由性能参数来定义。 
范例 : 
进入RADIUS计费服务器组1的配置模式：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#exitZXROSNG(config)#
相关命令 : 
show running-config radius 
## radius accounting-off 

radius accounting-off 
命令功能 : 
手动发送计费停止报文（Acct-Status-Type = Accounting-On）。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
radius accounting-off 
  {all 
|group 
 ＜accounting-group-name 
＞ [server 
 ＜accounting-server-number 
＞]}
命令参数解释 : 
参数|描述
---|---
all|向所有的RADIUS计费组发送计费停止报文
＜accounting-group-name＞|RADIUS计费服务器组的组名，长度为1-31个字符
＜accounting-server-number＞|RADIUS计费服务器的编号，范围：1-16
缺省 : 
无。 
使用说明 : 
计费停止报文的作用旨在告诉RADIUS服务器现在我的RADIUS客服端已经不再计费了，那么由服务器来决定现在用户的上线和计费状态和作一些用户下线的处理。比如：可以防止NAS因为重启或者其他异常情况用户需要重新上线，如果服务器不知道这个情况有可能以为用户重复上线，可能会不让用户上线或者其他异常情况，有了这个功能后，服务器会根据NAS的停止计费而作相应的操作。 
范例 : 
手动发送accounting-off包：ZXROSNG#radius accounting-off group 1      Send accounting off packet to radius accounting group 1!
相关命令 : 
无。 
## radius attribute vendor-specific vendor-id 

radius attribute vendor-specific vendor-id 
命令功能 : 
配置向服务器发送的报文中的ZTE私有属性的厂商号（Vendor Id）。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius attribute vendor-specific vendor-id 
  ＜vendor-id 
＞
no radius attribute vendor-specific vendor-id 
命令参数解释 : 
参数|描述
---|---
＜vendor-id＞|Vendor号，范围：1-65535
缺省 : 
3902。 
使用说明 : 
当需要指定厂商号是可使用此命令。是否发送ZTE自定义属性受认证组模式或计费组模式下的命令vendor控制。 
范例 : 
配置NAS向服务器发送的报文中的私有属性的vendor号为4096：ZXROSNG(config)#radius attribute vendor-specific vendor-id 4096
相关命令 : 
vendorshow running-config radius
## radius authentication-group 

radius authentication-group 
命令功能 : 
创建一个RADIUS组，或者进入AUTHEN_GROUP模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius authentication-group 
  ＜group-name 
＞
no radius authentication-group 
  ＜group-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-name＞|RADIUS认证服务器组的组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
此命令创建一个RADIUS认证组，并进入RADIUS组配置模式。当组名指向的组已经存在时则进入该组的配置模式。设备能配置的认证组总数由性能参数来定义。 
范例 : 
进入RADIUS认证服务器组1的配置模式：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#exitZXROSNG(config)#
相关命令 : 
show running-config radius 
## radius client-group 

radius client-group 
命令功能 : 
配置或者删除RADIUS客户端组 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius client-group 
  ＜client-group-name 
＞
no radius client-group 
  ＜client-group-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜client-group-name＞|RADIUS客户端组组名
缺省 : 
无 
使用说明 : 
使用命令后进入客户端组模式，在客户端组模式下可以继续配置客户端以及其他配置。全设备最多可以配置4000个客户端组，每个客户端组下最多可以配置64个客户端。 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#
相关命令 : 
show configuration radius allshow configuration radius client-group briefshow configuration radius client-group group-name
## radius client-group-default 

radius client-group-default 
命令功能 : 
配置默认客户组 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius client-group-default 
  ＜client--group-name 
＞
no radius client-group-default 
命令参数解释 : 
参数|描述
---|---
＜client--group-name＞|客户组名名称，长度为1~31个字节
缺省 : 
无 
使用说明 : 
设置全局默认客户端组，根据请求报文的ip和vrf找不到匹配的客户端时走默认客户端组，设置的客户端组必须是本地已经创建的。 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config)#radius client-group-default aaa
相关命令 : 
show configuration radius client-group all 
## radius dev-backup 

radius dev-backup 
命令功能 : 
配置NAS的RADIUS双机热备的主备状态。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius dev-backup 
  {master 
|slave 
}
no radius dev-backup 
命令参数解释 : 
参数|描述
---|---
master|设置RADIUS在本设备的热备状态是master状态
slave|设置RADIUS在本设备的热备状态是slave状态
缺省 : 
master。 
使用说明 : 
通常只有在NAS双机热备组网下才需要配置。该配置决定采用的发送报文的源端口号的区间。发送报文的源端口区间由性能参数配置决定。例如在默认的性能参数配置下：配置为master，认证端口采用11000~11046，计费端口采用11094~11152；配置为slave，认证端口采用11047~11093，计费端口采用11153~11211。
范例 : 
配置RADIUS热备的状态为slave状态：ZXROSNG(config)#radius dev-backup slaveZXROSNG(config)#no radius dev-backup
相关命令 : 
show running-config radius 
## radius listening-port accounting 

radius listening-port accounting 
命令功能 : 
配置或者删除计费监听端口 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius listening-port accounting 
  ＜accounting-listening-port 
＞
no radius listening-port accounting 
  ＜accounting-listening-port 
＞
				
命令参数解释 : 
参数|描述
---|---
＜accounting-listening-port＞|端口号，取值范围为1025~65535
缺省 : 
无 
使用说明 : 
此命令可以配置RADIUS PROXY监听RADIUS计费报文的端口。当端口被其他协议占用时会返回失败。可以通过命令show radius listening-port查看绑定状态，正常情况下都应该是绑定成功（success）。 
范例 : 
ZXROSNG(config)#radius listening-port accounting  3000ZXROSNG(config)#
相关命令 : 
show radius listening-port 
## radius listening-port authentication 

radius listening-port authentication 
命令功能 : 
配置或者删除认证监听端口 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius listening-port authentication 
  ＜authentication-listening-port 
＞
no radius listening-port authentication 
  ＜authentication-listening-port 
＞
				
命令参数解释 : 
参数|描述
---|---
＜authentication-listening-port＞|端口号，范围为1025~65535
缺省 : 
无 
使用说明 : 
此命令可以配置RADIUS PROXY监听RADIUS认证报文的端口。当端口被其他协议占用时会返回失败。可以通过命令show radius listening-port查看绑定状态，正常情况下都应该是绑定成功（success）。 
范例 : 
ZXROSNG(config)#radius listening-port authentication 7000ZXROSNG(config)#
相关命令 : 
show radius listening-port 
## radius server-port-check 

radius server-port-check 
命令功能 : 
设置是否检查RADIUS服务器发送的报文中的中的源端口号。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
radius server-port-check 
  {on 
|off 
}
命令参数解释 : 
参数|描述
---|---
on|检查RADIUS回应报文中的服务器端口号
off|不检查RADIUS回应报文中的服务器端口号
缺省 : 
on。 
使用说明 : 
开关打开，则同时对收到的报文进行源地址与端口的匹配，如果和配置的不一致，则认为报文非法。 
范例 : 
开关打开，则同时对收到的报文进行源端口的匹配，如果服务器发送回应报文采用的源端口与客服端发送请求报文的目的端口不匹配，则丢弃该报文。 
相关命令 : 
show running-config radius 
## radius-ping accounting-group 

radius-ping accounting-group 
命令功能 : 
通过发送一个RADIUS报文（非真实用户）到指定的RADIUS计费服务器（组）检测RADIUS计费组是否可达。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
radius-ping accounting-group 
  ＜accounting-group-name 
＞ ＜subscriber-name 
＞ [domain 
 ＜domain-name 
＞] [detail 
]
命令参数解释 : 
参数|描述
---|---
＜accounting-group-name＞|RADIUS计费服务器组的组名，长度为1-31个字符。
＜subscriber-name＞|设置用户名，字符串长度为1-127字符
＜domain-name＞|设置域名，字符串长度为1-31字符
detail|是否显示radius-ping的详细信息
缺省 : 
缺省不带域名，不显示详细信息 
使用说明 : 
1. 在服务器组dead时，仍然可以发起radius-ping请求，用来检测当前服务器是否通。如果当前发送的报文服务器给予回应，则改服务器立马恢复为active状态。2. radius-ping请求的使用用户不会携带用户的接入信息，因为触发请求的不是实际用户接入，而是RADIUS Client端根据用户名构造请求报文并携带最精简的信息发送给服务器，仅仅是为了达到检测服务器通断的目的，和用户是否能顺利接入无关。
范例 : 
检测RADIUS计费组是否可达：ZXROSNG#radius-ping accounting-group 1 hunter domain ztePing radius accounting-group 1 with hunter@zte at 07:10:53!Ping server 1 100.1.1.10 at 07:10:53!Reply from server 1 accept at 07:10:53!
相关命令 : 
无。 
## radius-ping authentication-group 

radius-ping authentication-group 
命令功能 : 
通过发送一个RADIUS报文（非真实用户）到指定的RADIUS认证服务器（组）检测RADIUS认证组是否可达。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
radius-ping authentication-group 
  ＜authentication-group-name 
＞ ＜subscriber-name 
＞ ＜password 
＞ [domain 
 ＜domain-name 
＞] {chap 
|pap 
} [detail 
]
命令参数解释 : 
参数|描述
---|---
＜authentication-group-name＞|RADIUS认证服务器组的组名，长度为1-31个字符。
＜subscriber-name＞|设置用户名，字符串长度为1-127字符
＜password＞|设置密码，字符串长度为1-31字符
＜domain-name＞|设置域名，字符串长度为1-31字符
chap|chap认证类型
pap|pap认证类型
detail|是否显示radius-ping的详细信息
缺省 : 
缺省不带域名，不显示详细信息 
使用说明 : 
1. 在服务器组dead时，仍然可以发起radius-ping请求，用来检测当前服务器是否通。如果当前发送的报文服务器给予回应，则改服务器立马恢复为active状态。2. radius-ping请求的使用用户不会携带用户的接入信息，因为触发请求的不是实际用户接入，而是RADIUS Client端根据用户名构造请求报文并携带最精简的信息发送给服务器，仅仅是为了达到检测服务器通断的目的，和用户是否能顺利接入无关。
范例 : 
检测RADIUS认证组是否可达：ZXROSNG#radius-ping authentication-group 1 HUNTER 123 papPing radius authentication-group 1 with HUNTER at 07:08:23!Ping server 1 100.1.1.10 at 07:08:23!Reply from server 1 accept at 07:08:23!
相关命令 : 
无。 
## send-rate-limit 

send-rate-limit 
命令功能 : 
配置RADIUS组下报文发送速率。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
send-rate-limit 
  ＜send-rate-limit 
＞
no send-rate-limit 
命令参数解释 : 
参数|描述
---|---
＜send-rate-limit＞|组下发送报文的速率值，范围1~4000，单位：个/秒；
缺省 : 
600 个/秒。 
使用说明 : 
设置组下发送报文的速率上限，组下报文发送速率将被限制在这个值以内，因为限速导致不能及时发送的报文将排在发送队列中等待下一批发送。该功能可以使用在服务器处理能力不足的场景中，保证性能不高的服务器不会因为客户端请求过多导致宕机等问题。
范例 : 
配置计费组下send-rate-limit值为100：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)# send-rate-limit 100ZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radius all 
## send-rate-limit 

send-rate-limit 
命令功能 : 
配置RADIUS组下报文发送速率。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
send-rate-limit 
  ＜send-rate-limit 
＞
no send-rate-limit 
命令参数解释 : 
参数|描述
---|---
＜send-rate-limit＞|组下发送报文的速率值，范围1~4000，单位：个/秒；
缺省 : 
600 个/秒。 
使用说明 : 
设置组下发送报文的速率上限，组下报文发送速率将被限制在这个值以内，因为限速导致不能及时发送的报文将排在发送队列中等待下一批发送。该功能可以使用在服务器处理能力不足的场景中，保证性能不高的服务器不会因为客户端请求过多导致宕机等问题。
范例 : 
配置认证组下send-rate-limit值为100：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)# send-rate-limit 100ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius all 
## server 

server 
命令功能 : 
设置RADIUS服务器及其参数。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
server 
  ＜server-number 
＞ ＜server-ipv4-address 
＞ [master 
] {key 
 {encrypted 
 ＜encrypted-password 
＞|＜password 
＞ [showclear 
]}|longkey 
 {encrypted 
 ＜encrypted longkey 
＞|＜password 
＞ [showclear 
]}} [port 
 ＜server-port 
＞] [weight 
 ＜server-weight 
＞]
no server 
  ＜server-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜server-number＞|服务器编号，范围：1-16
＜server-ipv4-address＞|服务器的IP地址
master|可选参数，表示该服务器为主服务器，一个服务器组只能有一个主服务器
＜encrypted-password＞|服务器与NAS之间的共享密文密钥，长度为64个字符
＜password＞|服务器与NAS之间的共享明文密钥，长度为1-31个字符
showclear|明文密钥显示标志，缺省为加密。
＜encrypted longkey＞|加密后的长密钥，长度172个字符
＜password＞|服务器与NAS之间的共享明文密钥，长度为1-31个字符
showclear|明文密钥显示标志，缺省为加密。
＜server-port＞|可选参数，服务器端口号，范围：1025-65535
＜server-weight＞|服务器权重，范围0-100
缺省 : 
RADIUS计费服务器端口号默认值为1813，认证服务器端口号默认值为1812。 
使用说明 : 
同一个组内的NAS的IP地址与服务器的IP地址的类型需要匹配，即都是IPv6或者都是IPv4，否则配置时会提示错误。 
范例 : 
设置计费服务器1 192.168.70.5 为主服务器，共享密钥为“zte”，端口1813：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#server 1 192.168.70.5 master key zte port 1813ZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radiusnas-ip-addressnas-ipv6-address
## server 

server 
命令功能 : 
设置RADIUS服务器及其参数。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
server 
  ＜server-number 
＞ ＜server-ipv4-address 
＞ [master 
] {key 
 {encrypted 
 ＜encrypted-password 
＞|＜password 
＞ [showclear 
]}|longkey 
 {encrypted 
 ＜encrypted- longkey 
＞|＜longKey 
＞ [showclear 
]}} [port 
 ＜server-port 
＞] [weight 
 ＜server-weight 
＞]
no server 
  ＜server-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜server-number＞|服务器编号，范围：1-16
＜server-ipv4-address＞|服务器的IP地址
master|可选参数，表示该服务器为主服务器，一个服务器组只能有一个主服务器
＜encrypted-password＞|服务器与NAS之间的共享密文密钥，长度为64个字符
＜password＞|服务器与NAS之间的共享明文密钥，长度为1-31个字符
showclear|明文密钥显示标志，缺省为加密
＜encrypted- longkey＞|加密后的长密钥，长度172个字符
＜longKey＞|长密钥，长度1-128个字符
showclear|明文密钥显示标志，缺省为加密
＜server-port＞|可选参数，服务器端口号，范围：1025-65535
＜server-weight＞|服务器权重，范围0-100
缺省 : 
RADIUS计费服务器端口号默认值为1813，认证服务器端口号默认值为1812。 
使用说明 : 
同一个组内的NAS的IP地址与服务器的IP地址的类型需要匹配，即都是IPv6或者都是IPv4，否则配置时会提示错误。 
范例 : 
设置认证服务器1 192.168.70.5为主服务器，共享密钥为“zte”，端口1812：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#server 1 192.168.70.5 master key zte port 1812ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radiusnas-ip-addressnas-ipv6-address
## server6 

server6 
命令功能 : 
设置RADIUS IPv6地址服务器及其参数。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
server6 
  ＜server-number 
＞ ＜server-ipv6-address 
＞ [master 
] {key 
 {encrypted 
 ＜encrypted-password 
＞|＜password 
＞ [showclear 
]}|longkey 
 {encrypted 
 ＜encrypted-password 
＞|＜password 
＞ [showclear 
]}} [port 
 ＜port-number 
＞] [weight 
 ＜server-weight 
＞]
no server6 
  ＜server-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜server-number＞|服务器编号，范围：1-16
＜server-ipv6-address＞|服务器的IPv6地址
master|可选参数，表示该服务器为主服务器，一个服务器组只能有一个主服务器
＜encrypted-password＞|服务器与NAS之间的共享密文密钥，长度为64个字符
＜password＞|服务器与NAS之间的共享明文密钥，长度为1-31个字符
showclear|明文密钥显示标志，缺省为加密。
＜encrypted-password＞|服务器与NAS之间的共享密文密钥，长度为64个字符
＜password＞|服务器与NAS之间的共享明文密钥，长度为1-31个字符
showclear|明文密钥显示标志，缺省为加密。
＜port-number＞|可选参数，服务器端口号，范围：1025-65535
＜server-weight＞|服务器权重，范围0-100
缺省 : 
RADIUS计费服务器端口号默认值为1813，认证服务器端口号默认值为1812。 
使用说明 : 
同一个组内的NAS的IP地址与服务器的IP地址的类型需要匹配，即都是IPv6或者都是IPv4，否则配置时会提示错误。 
范例 : 
1.设置计费服务器1 2000::10 为主服务器，共享密钥为“zte”，明文密钥显示：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#server6 1 2000::10 key zte showclear ZXROSNG(config-acctgrp-1)#show this!<radius>  server6 1 2000::10 key zte showclear!</radius>ZXROSNG(config-acctgrp-1)#2.设置计费服务器1 2000::10 为主服务器，共享密钥为“zte”，密文密钥显示：ZXROSNG(config-acctgrp-1)#server6 1 2000::10 key zte ZXROSNG(config-acctgrp-1)#show this!<radius>  server6 1 2000::10 key encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB!</radius>ZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radiusnas-ip-addressnas-ipv6-address
## server6 

server6 
命令功能 : 
设置RADIUS IPv6地址服务器及其参数。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
server6 
  ＜server-number 
＞ ＜server-ipv6-address 
＞ [master 
] {key 
 {encrypted 
 ＜encrypted-password 
＞|＜password 
＞ [showclear 
]}|longkey 
 {encrypted 
 ＜encrypted-password 
＞|＜password 
＞ [showclear 
]}} [port 
 ＜server-port 
＞] [weight 
 ＜server-weight 
＞]
no server6 
  ＜server-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜server-number＞|服务器编号，范围：1-16
＜server-ipv6-address＞|服务器的IPv6地址
master|可选参数，表示该服务器为主服务器，一个服务器组只能有一个主服务器
＜encrypted-password＞|服务器与NAS之间的共享密文密钥，长度为64个字符
＜password＞|服务器与NAS之间的共享明文密钥，长度为1-31个字符
showclear|明文密钥显示标志，缺省为加密
＜encrypted-password＞|服务器与NAS之间的共享密文密钥，长度为64个字符
＜password＞|服务器与NAS之间的共享明文密钥，长度为1-31个字符
showclear|明文密钥显示标志，缺省为加密
＜server-port＞|可选参数，服务器端口号，范围：1025-65535
＜server-weight＞|服务器权重，范围0-100
缺省 : 
RADIUS计费服务器端口号默认值为1813，认证服务器端口号默认值为1812。 
使用说明 : 
同一个组内的NAS的IP地址与服务器的IP地址的类型需要匹配，即都是IPv6或者都是IPv4，否则配置时会提示错误。 
范例 : 
设置认证服务器1 2000::20为主服务器，共享密钥为“zte”，端口1812：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#server6 1 2000::20 master key zte port 1812ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radiusnas-ip-addressnas-ipv6-address
## set-dscp-outer 

set-dscp-outer 
命令功能 : 
配置RADIUS的IP报文DSCP值。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
set-dscp-outer 
  ＜dscp-value 
＞
no set-dscp-outer 
命令参数解释 : 
参数|描述
---|---
＜dscp-value＞|DSCP值，范围：0-63
缺省 : 
无。 
使用说明 : 
该命令用来指定RADIUS的IP报文DSCP值。当该命令未配置时，由设备底层协议来填写。 
范例 : 
配置发送的RADIUS计费报文的优先级为63：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)# set-dscp-outer 63ZXROSNG(config-acctgrp-1)#
相关命令 : 
show running-config radius 
## set-dscp-outer 

set-dscp-outer 
命令功能 : 
配置RADIUS的IP报文DSCP值。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
set-dscp-outer 
  ＜dscp-value 
＞
no set-dscp-outer 
命令参数解释 : 
参数|描述
---|---
＜dscp-value＞|DSCP值，范围：0-63
缺省 : 
无。 
使用说明 : 
该命令用来指定RADIUS的IP报文DSCP值。当该命令未配置时，由设备底层协议来填写。 
范例 : 
配置发送的RADIUS认证报文的优先级为63：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)# set-dscp-outer 63ZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## show accounting local-buffer all 

show accounting local-buffer all 
命令功能 : 
显示RADIUS所有本地缓存的计费报文。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show accounting local-buffer all 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
显示所有本地计费缓存。计费缓存是当计费报文没有得到服务器响应以后缓存到本地的报文，待服务器可用以后继续发往服务器。各显示表项说明如下：slot            单板编号group           组名type            计费报文类型，分为以下类型                start               计费开始                stop                计费停止                tunnel-start        隧道计费开始                tunnel-stop         隧道计费停止                tunnel-link-start   隧道链路计费开始                tunnel-link-stop    隧道链路计费停止session-id      Acct-Session-Idsave-time       计费报文保存的时间send-to-server  最后一次尝试发往的服务器IP地址
范例 : 
显示RADIUS 所有本地缓存的计费报文：ZXROSNG#show accounting local-buffer allslot  group type         session-id                        save-time  send-to-server20   1     stop         130301162045DingG181824ACCT0002   08:20:56   100.1.1.1003/01/2013
20   1     tunnel-start 130301162047DingG181824ACCT0003   08:20:59   100.1.1.1003/01/2013
20   1     start        130301162110DingG181824ACCT0004   08:21:21   100.1.1.1003/01/2013
20   1     stop         130301162113DingG181824ACCT0005   08:21:24   100.1.1.1003/01/2013
20   1     tunnel-start 130301162115DingG181824ACCT0006   08:21:26   100.1.1.1003/01/2013
20   1     tunnel-stop  130301162117DingG181824ACCT0007   08:21:28   100.1.1.1003/01/2013
20   1     tunnel-link- 130301162119DingG181824ACCT0008   08:21:30   100.1.1.10start                                          03/01/201320   1     tunnel-link- 130301162121DingG181824ACCT0009   08:21:32   100.1.1.10stop                                           03/01/20133   1     stop         130301162045DingG181824ACCT0002   08:20:56   100.1.1.1003/01/2013
3   1     tunnel-start 130301162047DingG181824ACCT0003   08:20:59   100.1.1.1003/01/2013
相关命令 : 
无。 
## show accounting local-buffer group 

show accounting local-buffer group 
命令功能 : 
显示RADIUS 指定计费组本地缓存的计费报文。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show accounting local-buffer group 
  ＜group-name 
＞ [{[head 
 ＜head-count 
＞]|[tail 
 ＜tail-count 
＞]|[index 
 ＜index 
＞ [＜index-count 
＞]]}] 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|RADIUS计费服务器组的组名，RADIUS组名长度为1-31个字符。
＜head-count＞|从计费缓存队列头开始，需要显示的缓存记录的条目数；
＜tail-count＞|从计费缓存队列尾开始，需要显示的缓存记录的条目数；
＜index＞|指定从哪一条缓存记录开始显示；
＜index-count＞|需要显示的缓存记录的条目数；
缺省 : 
无。 
使用说明 : 
显示所有本地计费缓存。计费缓存是当计费报文没有得到服务器响应以后缓存到本地的报文，待服务器可用以后继续发往服务器。各显示表项说明如下：slot            单板编号group           组名type            计费报文类型，分为以下类型                start               计费开始                stop                计费停止                tunnel-start        隧道计费开始                tunnel-stop         隧道计费停止                tunnel-link-start   隧道链路计费开始                tunnel-link-stop    隧道链路计费停止session-id      Acct-Session-Idsave-time       计费报文保存的时间send-to-server  最后一次尝试发往的服务器IP地址
范例 : 
显示RADIUS 计费组1的本地缓存的计费报文：ZXROSNG#show accounting local-buffer group 1Slot   group type         session-id                        save-time  send-to-server20    1     stop         130301162045DingG181824ACCT0002   08:20:56   100.1.1.1003/01/2013
20    1     tunnel-start 130301162047DingG181824ACCT0003   08:20:59   100.1.1.1003/01/2013
20    1     start        130301162110DingG181824ACCT0004   08:21:21   100.1.1.1003/01/2013
20    1     stop         130301162113DingG181824ACCT0005   08:21:24   100.1.1.1003/01/2013
20    1     tunnel-start 130301162115DingG181824ACCT0006   08:21:26   100.1.1.1003/01/2013
20    1     tunnel-stop  130301162117DingG181824ACCT0007   08:21:28   100.1.1.1003/01/2013
20    1     tunnel-link- 130301162119DingG181824ACCT0008   08:21:30   100.1.1.10start                                          03/01/201320    1     tunnel-link- 130301162121DingG181824ACCT0009   08:21:32   100.1.1.10stop                                           03/01/20133    1     stop         130301162045DingG181824ACCT0002   08:20:56   100.1.1.1003/01/2013
3    1     tunnel-start 130301162047DingG181824ACCT0003   08:20:59   100.1.1.1003/01/2013
相关命令 : 
show accounting local-buffer all 
## show accounting local-buffer session 

show accounting local-buffer session 
命令功能 : 
显示RADIUS 指定Acct-Session-Id值的计费缓存报文。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show accounting local-buffer session 
  ＜accounting-session-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜accounting-session-id＞|RADIUS计费报文中的Acct-Session-Id值
缺省 : 
无。 
使用说明 : 
显示指定Acct-Session-Id的计费缓存报文。计费缓存是当计费报文没有得到服务器响应以后缓存到本地的报文，待服务器可用以后继续发往服务器。各显示表项说明如下：group           组名type            计费报文类型，分为以下类型                start               计费开始                stop                计费停止                tunnel-start        隧道计费开始                tunnel-stop         隧道计费停止                tunnel-link-start   隧道链路计费开始                tunnel-link-stop    隧道链路计费停止session-id      Acct-Session-Idgenerate_tick   计费报文产生的时间save-time       计费报文保存的时间times_in_buffer 计费报文被缓存的时长user            计费报文的用户名属性
范例 : 
显示RADIUS计费报文session_id为999999999999DingG181824ACCT9999的计费报文：ZXROSNG#show accounting local-buffer session 999999999999DingG181824ACCT9999----------------------------------------------------------------session         : 999999999999DingG181824ACCT9999type            : startgroup           : 1generate_tick   : 02:36:04 01/30/2011save_time       : 02:36:07 01/30/2011times_in_buffer : 00:18:31user            : hunter----------------------------------------------------------------session         : 999999999999DingG181824ACCT9999type            : stop group           : 1generate_tick   : 02:36:04 01/30/2011save_time       : 02:36:07 01/30/2011times_in_buffer : 00:18:31user            : hunter----------------------------------------------------------------session         : 999999999999DingG181824ACCT9999type            : startgroup           : 2generate_tick   : 02:36:04 01/30/2011save_time       : 02:36:06 01/30/2011times_in_buffer : 00:18:32user            : hunter----------------------------------------------------------------session         : 999999999999DingG181824ACCT9999type            : stop group           : 2generate_tick   : 02:36:04 01/30/2011save_time       : 02:36:06 01/30/2011times_in_buffer : 00:18:32user            : hunterZXROSNG# 
相关命令 : 
show accounting local-buffer all 
## show accounting local-buffer sum 

show accounting local-buffer sum 
命令功能 : 
显示RADIUS所有本地缓存的计费报文的个数统计。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show accounting local-buffer sum 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
分组显示计费报文的个数。计费缓存是当计费报文没有得到服务器响应以后缓存到本地的报文，待服务器可用以后继续发往服务器。各字段说明如下：group name      组名record-number   计费报文条目数，其中同一个session的报文即便有多个（一个计费开始和一个计费停止）缓存，也只算做一个条目relation-number 附属于计费开始报文的计费停止报文的个数
范例 : 
显示RADIUS 所有本地缓存的计费报文的个数统计：ZXROSNG#show accounting local-buffer sumgroup number: 1        record-number: 3     relation-number: 3    group number: 999      record-number: 20    relation-number: 0    total local accounting record-number: 23    relation-number: 3 ZXROSNG#
相关命令 : 
show accounting local-buffer all 
## show accounting local-buffer user 

show accounting local-buffer user 
命令功能 : 
显示RADIUS指定用户名的本地缓存的计费报文。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show accounting local-buffer user 
  ＜user-name 
＞ [＜user-count 
＞] 
命令参数解释 : 
参数|描述
---|---
＜user-name＞|RADIUS计费报文的用户名，如果有domain名需包含domain名，字符串长度为1-159字符
＜user-count＞|指定显示缓存计费报文的条目数
缺省 : 
无。 
使用说明 : 
显示所有本地计费缓存。计费缓存是当计费报文没有得到服务器响应以后缓存到本地的报文，待服务器可用以后继续发往服务器。各显示表项说明如下：slot            单板编号group           组名type            计费报文类型，分为以下类型                start               计费开始                stop                计费停止                tunnel-start        隧道计费开始                tunnel-stop         隧道计费停止                tunnel-link-start   隧道链路计费开始                tunnel-link-stop    隧道链路计费停止session-id      Acct-Session-Idsave-time       计费报文保存的时间send-to-server  最后一次尝试发往的服务器IP地址
范例 : 
显示RADIUS 用户名为hunter的计费报文：ZXROSNG#show accounting local-buffer user HUNTER@zteslot  group type         session-id                        save-time  send-to-server20   1     stop         130301162045DingG181824ACCT0002   08:20:56   100.1.1.1003/01/2013
20   1     tunnel-start 130301162047DingG181824ACCT0003   08:20:59   100.1.1.1003/01/2013
20   1     start        130301162110DingG181824ACCT0004   08:21:21   100.1.1.1003/01/2013
20   1     stop         130301162113DingG181824ACCT0005   08:21:24   100.1.1.1003/01/2013
20   1     tunnel-start 130301162115DingG181824ACCT0006   08:21:26   100.1.1.1003/01/2013
20   1     tunnel-stop  130301162117DingG181824ACCT0007   08:21:28   100.1.1.1003/01/2013
20   1     tunnel-link- 130301162119DingG181824ACCT0008   08:21:30   100.1.1.10start                                          03/01/201320   1     tunnel-link- 130301162121DingG181824ACCT0009   08:21:32   100.1.1.10stop                                           03/01/20133   1     stop         130301162045DingG181824ACCT0002   08:20:56   100.1.1.1003/01/2013
3   1     tunnel-start 130301162047DingG181824ACCT0003   08:20:59   100.1.1.1003/01/2013
相关命令 : 
show accounting local-buffer all 
## show configuration radius accounting-group 

show configuration radius accounting-group 
命令功能 : 
显示RADIUS 计费组配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius accounting-group 
  ＜accounting-group-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜accounting-group-name＞|RADIUS计费服务器组的组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
显示指定RADIUS计费组的配置。显示形式与命令行输入一致。 
范例 : 
显示RADIUS 计费组1配置：ZXROSNG#show config radius accounting-group 999radius accounting-group 999  algorithm first  calling-station-format class3  deadtime 0  dsl-vendor disable  flow-unit byte  interim-packet-quota 80  life-time 2  local-buffer disable  max-retries 3  nas-ip-address 100.1.1.1  nas-port-id-format china-tel  server 1 100.1.1.10 master key encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB port 1812  set-dscp-outer 48  timeout 3  user-name-format strip-domain  vendor enable!ZXROSNG#
相关命令 : 
show running-config radiusshow configuration radius all
## show configuration radius all 

show configuration radius all 
命令功能 : 
显示RADIUS模块的所有配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius all 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
显示RADIUS模块所有的配置。配置显示形式与配置命令的输入形式一致，包含默认配置的条目 
范例 : 
显示RADIUS的所有配置：ZXROSNG#show config radius allradius authentication-group 888  algorithm first  calling-station-format class3  class-as-car disable  deadtime 0  dsl-vendor disable  filter-id direction out  max-retries 3  nas-ip-address 100.1.1.1  nas-port-id-format china-tel  server 1 100.1.1.10 master key encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB port 1812  set-dscp-outer 48  timeout 3  user-name-format strip-domain  vendor enable!radius accounting-group 999  algorithm rollover-on-reject  calling-station-format class3  deadtime 0  dsl-vendor disable  flow-unit byte  interim-packet-quota 80  life-time 2  local-buffer disable  max-retries 3  nas-ip-address 100.1.1.1  nas-port-id-format china-tel  server 1 100.1.1.10 master key encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB port 1812  set-dscp-outer 48  timeout 3  user-name-format strip-domain  vendor enable!        ZXROSNG#   ZXROSNG#
相关命令 : 
show running-config radius 
## show configuration radius attribute 

show configuration radius attribute 
命令功能 : 
1.显示全局配置中发送给服务器厂商属性ID；2.显示属性禁用与转义的配置。
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius attribute 
  [{convert 
|forbid 
} [{authentication 
|accounting 
} [group 
 ＜group-name 
＞]]] 
命令参数解释 : 
参数|描述
---|---
convert|显示属性转义配置
forbid|显示属性禁用配置
authentication|指定只显示认证组的属性配置
accounting|指定只显示计费组的属性配置
＜group-name＞|RADIUS服务器组的组名，长度为1-31个字符。
缺省 : 
不指定任何参数将显示当前配置的ZTE厂商属性号； 
使用说明 : 
将以命令行配置的形式显示。 
范例 : 
显示RADIUS attribute的配置：ZXROSNG#show configuration radius attribute Radius vendor-id : 4096显示属性禁用与转义配置：ZXROSNG#show conf radius attribute forbid radius authentication-group 10  attribute forbid 100 1 send  attribute forbid 100 1 receive!radius authentication-group 2000  attribute forbid 20000 1 send  attribute forbid 20000 1 receive!radius accounting-group 10  attribute forbid 101 1 send  attribute forbid 101 1 receive!radius accounting-group 2000  attribute forbid 20001 1 send  attribute forbid 20001 1 receive!ZXROSNG#show conf radius attribute forbid authZXROSNG#show conf radius attribute forbid authentication radius authentication-group 10  attribute forbid 100 1 send  attribute forbid 100 1 receive!radius authentication-group 2000  attribute forbid 20000 1 send  attribute forbid 20000 1 receive!ZXROSNG#show conf radius attribute forbid authentication gZXROSNG#show conf radius attribute forbid authentication group 10radius authentication-group 10  attribute forbid 100 1 send  attribute forbid 100 1 receive!ZXROSNG#ZXROSNG#ZXROSNG#show conf radius attribute c                             ZXROSNG#show conf radius attribute convert radius authentication-group 10  attribute convert 100 1 to 10 1 send  attribute convert 100 1 to 10 1 receive
!radius authentication-group 2000  attribute convert 20000 1 to 2000 1 send  attribute convert 20000 1 to 2000 1 receive!radius accounting-group 10  attribute convert 101 1 to 10 1 send  attribute convert 101 1 to 10 1 receive!radius accounting-group 2000  attribute convert 20001 1 to 2000 1 send  attribute convert 20001 1 to 2000 1 receive!ZXROSNG#ZXROSNG#show conf radius attribute convert auZXROSNG#show conf radius attribute convert authentication radius authentication-group 10  attribute convert 100 1 to 10 1 send  attribute convert 100 1 to 10 1 receive
!radius authentication-group 2000  attribute convert 20000 1 to 2000 1 send  attribute convert 20000 1 to 2000 1 receive!ZXROSNG#ZXROSNG#show conf radius attribute convert authentication gZXROSNG#show conf radius attribute convert authentication group 10radius authentication-group 10  attribute convert 100 1 to 10 1 send  attribute convert 100 1 to 10 1 receive
相关命令 : 
radius attribute vendor-specificattribute forbidattribute convert
## show configuration radius authentication-group 

show configuration radius authentication-group 
命令功能 : 
显示RADIUS认证组的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius authentication-group 
  ＜authentication-group-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜authentication-group-name＞|RADIUS认证服务器组的组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
显示指定认证服务器的配置，显示形式与命令行输入一致。 
范例 : 
显示RADIUS认证组888配置：ZXROSNG#show config radius authentication-group 888radius authentication-group 888  algorithm rollover-on-reject  calling-station-format class3  class-as-car disable  deadtime 0  dsl-vendor disable  filter-id direction out  max-retries 3  nas-ip-address 100.1.1.1  nas-port-id-format china-tel  server 1 100.1.1.10 master key encrypted 33A8EC1030727EB3A9B61002E10BDBEDB5BEA986F5505AD19582826921F45FCB port 1812  set-dscp-outer 48  timeout 3  user-name-format strip-domain  vendor enable!ZXROSNG#
相关命令 : 
show running-config radiusshow configuration radius all
## show configuration radius client-group all 

show configuration radius client-group all 
命令功能 : 
显示所有RADIUS客户端组的配置信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius client-group all 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示所有客户端组的配置信息，客户端组下的配置信息将以配置命令输入的形式来显示，包含默认配置的条目。 
范例 : 
ZXROSNG#show configuration radius client-group allradius client-group aaa  dm-coa timeout 3  dm-coa max-retries 3  attribute replace nas-ip-address disable  attribute replace nas-identifier disable!
radius client-group bbb  dm-coa timeout 3  dm-coa max-retries 3  attribute replace nas-ip-address disable  attribute replace nas-identifier disable!
radius client-group ccc  dm-coa timeout 3  dm-coa max-retries 3  attribute replace nas-ip-address disable  attribute replace nas-identifier disable!        radius client-group ddd  dm-coa timeout 3  dm-coa max-retries 3  attribute replace nas-ip-address disable  attribute replace nas-identifier disable!
radius client-group eee  dm-coa timeout 3  dm-coa max-retries 3  attribute replace nas-ip-address disable  attribute replace nas-identifier disable!
radius client-group fff  dm-coa timeout 3  dm-coa max-retries 3  attribute replace nas-ip-address disable  attribute replace nas-identifier disable!
相关命令 : 
show running-config radius 
## show configuration radius client-group brief 

show configuration radius client-group brief 
命令功能 : 
显示配置的客户端组的摘要信息（名称） 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius client-group brief 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
目前只显示客户端组的名称。 
范例 : 
ZXROSNG#show configuration radius client-group brief radius client-group aaaradius client-group bbbradius client-group cccradius client-group dddradius client-group eeeradius client-group fff
相关命令 : 
show running-config radius 
## show configuration radius client-group group-name 

show configuration radius client-group group-name 
命令功能 : 
显示指定RADIUS客户端组的配置信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius client-group group-name 
  ＜group-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|客户端组组名，长度为1~31个字节
缺省 : 
无。 
使用说明 : 
显示RADIUS客户端组的配置信息。配置显示形式与配置命令的输入形式一致，包含默认配置的条目。 
范例 : 
ZXROSNG#show configuration radius client-group group-name aaaradius client-group aaa  dm-coa timeout 3  dm-coa max-retries 3  attribute replace nas-ip-address disable  attribute replace nas-identifier disable!
相关命令 : 
show running-config radius 
## show configuration radius dev-backup 

show configuration radius dev-backup 
命令功能 : 
显示RADIUS双机热备状态。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius dev-backup 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
显示当前设备RADIUS的双机热备状态。对应配置命令radius dev-backup，显示形式为配置命令的输入形式。具体命令使用情况参见该命令。 
范例 : 
显示RADIUS 热备状态：ZXROSNG#show configuration radius dev-backup Radius device backup status is masterZXROSNG#
相关命令 : 
show running-config radius 
## show configuration radius server-port-check 

show configuration radius server-port-check 
命令功能 : 
显示RADIUS server-port-check的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show configuration radius server-port-check 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
显示内容对应radius server-port-check命令的配置，将以命令行配置的形式显示。 
范例 : 
显示RADIUS server-port-check的配置：ZXROSNG#show configuration radius server-port-check Check ports of all radius servers on
相关命令 : 
show running-config radius 
## show debug radius 

show debug radius 
命令功能 : 
显示RADIUS已经打开的debug选项。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug radius 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
显示RADIUS debug 开关以及过滤条件的设置情况。debug命令的使用参看命令debug radius。每个开关都显示为一行条目；每个过滤条件也被显示为一行条目。显示内容参看范例。 
范例 : 
显示RADIUS 已经打开的debug开关，其中包含一个用户名的过滤条件：ZXROSNG#show debug radius RADIUS:  RADIUS exception debugging is on  RADIUS event authentication debugging is on  RADIUS event accounting debugging is on  RADIUS event dmcoa debugging is on  RADIUS packet authentication debugging is on  RADIUS packet accounting debugging is on  RADIUS packet dmcoa debugging is on  RADIUS data authentication debugging is on  RADIUS data accounting debugging is on  RADIUS data dmcoa debugging is on  RADIUS error authentication debugging is on  RADIUS error accounting debugging is on  RADIUS error dmcoa debugging is on  RADIUS debug filter:    username            : user@zte
相关命令 : 
debug radius alldebug radius set filter
## show radius counter 

show radius counter 
命令功能 : 
显示服务器统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius counter 
  {authentication-group 
 ＜auth-grp-name 
＞|accounting-group 
 ＜acct-grp-name 
＞|all 
} 
命令参数解释 : 
参数|描述
---|---
authentication-group|指定查看认证服务器计数
＜auth-grp-name＞|RADIUS认证服务器组的组名，长度为1-31个字符。
accounting-group|指定查看计费服务器计数
＜acct-grp-name＞|RADIUS计费服务器组的组名，长度为1-31个字符。
all|查看所有服务器计数
缺省 : 
无。 
使用说明 : 
全局统计部分信息：radius client statisticauth_svr_used : 设备上认证服务器的个数acct_svr_used : 设备上计费服务器的个数AuthClientInvalidServerAddresses : 收到来自无效服务器（未配置）的认证报文AcctClientInvalidServerAddresses : 收到来自无效服务器（未配置）的计费报文认证服务器部分信息：Counter start time: 当前服务器统计信息开始的时间Round trip time:  与该服务器交互的最后一个报文所费的时候，从发出去到收到的时间只差，可能用来反应网络延时，单位为微秒Requests sent:  对该服务器发送的请求个数，不包括重复发送的次数Requests retransmitted : 对该服务器发送的报文中的重传次数Accepts received:  该服务器回应的Access-Accept报文的个数Rejects received:  该服务器回应的Access-Reject报文的个数Challenges received:  该服务器回应的Access-Challenge报文的个数Malformed responses received:  该服务器回应的畸形报文的个数，比如长度与UDP 数据区长度不一致，属性长度出错Bad authenticators received:  该服务器回应的错误的Authenticatior个数Pending requests:  对该服务器发送的报文中正在等待回应的个数Requests timeout:  该服务器未给予回应的请求个数Unknown types received:  该服务器回应的报文类型未知的报文个数Receive packets dropped:  该服务器回应的未知错误类型的报文
计费服务器部分信息：Counter start time: 当前服务器统计信息开始的时间Round trip time:  与该服务器交互的最后一个报文所费的时候，从发出去到收到的时间只差，可能用来反应网络延时，单位为微秒Requests sent:  对该服务器发送的请求个数，不包括重复发送的次数Requests retransmitted : 对该服务器发送的报文中的重传次数Responses received:  该服务器回应的报文的个数Malformed responses received:  该服务器回应的畸形报文的个数，比如长度与UDP 数据区长度不一致，属性长度出错Bad authenticators received:  该服务器回应的错误的Authenticatior个数Pending requests:  对该服务器发送的报文中正在等待回应的个数Requests timeout:  该服务器未给予回应的请求个数Unknown types received:  该服务器回应的报文类型未知的报文个数Receive packets dropped:  该服务器回应的未知错误类型的报文
范例 : 
显示RADIUS计费组服务器计数信息：XR10#show radius counter accounting-group 2000--------------------------------------------------------------Accounting server 2000-1 192.1.0.111-1813Clear time: 14:58:15 11/08/2011Round trip time:  00s.00th (0microsecond)Requests sent:  1Requests retransmitted:  1Responses received:  0Malformed responses received:  0Bad authenticators received:  0Pending requests:  0Requests timeout:  2Unknown types received:  0Receive packets dropped:  0--------------------------------------------------------------Accounting server 2000-2 2.2.2.2-1813Clear time: 14:58:15 11/08/2011Round trip time:  00s.00th (0microsecond)Requests sent:  1Requests retransmitted:  1Responses received:  0Malformed responses received:  0Bad authenticators received:  0Pending requests:  0Requests timeout:  2Unknown types received:  0Receive packets dropped:  0 显示RADIUS所有服务器计数信息：ZXROSNG#show radius counter allradius client statisticauth_svr_used : 7  acct_svr_used : 9AuthClientInvalidServerAddresses : 0AcctClientInvalidServerAddresses : 0--------------------------------------------------------------Authentication server 1-1 192.1.0.100-1812Counter start time: 04:21:31 11/12/2011Round trip time:  00s.00th (0microsecond)Requests sent:  0Requests retransmitted : 0Accepts received:  0Rejects received:  0Challenges received:  0Malformed responses received:  0Bad authenticators received:  0Pending requests:  0Requests timeout:  0Unknown types received:  0Receive packets dropped:  0--------------------------------------------------------------Accounting server 1-1 192.1.1.1-1813Clear time: 04:21:32 11/12/2011Round trip time:  00s.00th (0microsecond)Requests sent:  1Requests retransmitted:  3Responses received:  0Malformed responses received:  0Bad authenticators received:  0Pending requests:  0Requests timeout:  4Unknown types received:  0Receive packets dropped:  0         --------------------------------------------------------------Accounting server 2-1 192.1.0.100-1813Clear time: 04:21:32 11/12/2011Round trip time:  00s.00th (0microsecond)Requests sent:  1Requests retransmitted:  3Responses received:  0Malformed responses received:  0Bad authenticators received:  0Pending requests:  0Requests timeout:  4Unknown types received:  0Receive packets dropped:  0
相关命令 : 
clear radius counter 
## show radius listening-port 

show radius listening-port 
命令功能 : 
显示RADIUS PROXY配置的监听端口信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius listening-port 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示RADIUS PROXY所配置的监听端口号，并且显示端口号绑定的结果，正常情况都应该是success。 
范例 : 
ZXROSNG#show radius listening-port authentication listening port : 3000 register-state:successauthentication listening port : 4000 register-state:successaccounting listening port : 5000 register-state:successaccounting listening port : 6000 register-state:success
相关命令 : 
show configuration radius listening-port 
## show radius-attribute name 

show radius-attribute name 
命令功能 : 
按属性名显示RADIUS属性信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius-attribute name 
  ＜attribute-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜attribute-name＞|属性名，字符串，长度1~64；
缺省 : 
无。 
使用说明 : 
按属性名显示RADIUS属性信息。每个属性都有一个唯一的属性名。显示的信息包括：厂商号、属性号、属性名、所支持的报文类型、以及属性描述。
范例 : 
按属性名显示RADIUS属性信息。每个属性都有一个唯一的属性名。显示的信息包括：厂商号、属性号、属性名、所支持的报文类型、以及属性描述。
相关命令 : 
无。 
## show radius-attribute type 

show radius-attribute type 
命令功能 : 
按属性号及厂商号来显示RADIUS属性信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius-attribute type 
  ＜type {standard | cisco } 
＞ ＜attribute-number 
＞ 
命令参数解释 : 
参数|描述
---|---
＜type {standard | cisco }＞|厂商，standard表示共有属性，其他为各厂商；
＜attribute-number＞|属性号，范围1~255；
缺省 : 
无。 
使用说明 : 
按属性号及其厂商号显示RADIUS属性信息。每个属性都有一个唯一的属性名。显示的信息包括：厂商号、属性号、属性名、所支持的报文类型、以及属性描述。
范例 : 
ZXROSNG#show radius-attribute type standard 25Vendor           : Standard(0)Type             : 25Name             : ClassSupported Packets: Access-Accept(2),Access-Reject(3),Accounting-Request(4),CoA Request(43).Description      : This Attribute is available to be sent by the server to the client in an Access-Accept and SHOULD be sent unmodified by the client to the accounting server as part of the Accounting-Request packet if accounting is supported.  The client MUST NOT interpret the attribute locally.
相关命令 : 
无。 
## show radius-attribute 

show radius-attribute 
命令功能 : 
显示设备支持的RADIUS属性信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius-attribute 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
显示设备上支持的所有的RADIUS属性及相关信息。如下范例中的格式，表格之上是对表格各项表项中具体字段的解释，其中：Codes段: code表项对应的RADIUS报文code字段各值及其完整的名称；Supported段：support表项中的值的含义；Vendors Ids段：Vendor表项中厂商名的缩写对应的完整厂商名。属性表格各表项的说明：Attribute Name(Type)： 属性名，括号中是其属性号；Vendor： 属性所属的厂商；Auth Req ~CoA Res： 各类型的报文对属性的支持情况。
范例 : 
ZXROSNG#show radius-attribute Codes:     Auth Req  : Access-Request(1),Access-Challenge(11)    Auth Accp : Access-Accept(2)    Auth Rej  : Access-Reject(3)    Acct Req  : Access-Request(4)    Acct Resp : Accounting-Response(5)    CoA Req   : CoA Request(43)    CoA Res   : CoA ACK(44),CoA NAK(45)Supported:    0         : Can not be existed in this packet    1         : Can be existed in this packetVendors Ids:    Std       : 0 (Standard)    Cisco     : 9     MS        : 311(Microsoft)    ZTE       : 3902    ZTE-Ex    : 10008    China-Tel : 20942(China-Tel)    DSL       : 3561-------------------------------------------------------------------------------Attribute Name(Type)                Vendor    Auth Auth Auth Acct Acct CoA  CoA                                              Req  Accp Rej  Req  Resp Req  Res-------------------------------------------------------------------------------User-Name(1)                         Std       1    1    1    1    0    1    0User-Password(2)                     Std       1    0    0    0    0    0    0CHAP-Password(3)                     Std       1    0    0    0    0    0    0NAS-IP-Address(4)                    Std       1    0    0    1    0    0    0NAS-Port(5)                          Std       1    0    0    1    0    1    0Service-Type(6)                      Std       1    1    1    1    0    0    0Framed-Protocol(7)                   Std       1    0    0    1    0    0    0Framed-IP-Address(8)                 Std       1    1    1    1    0    1    0Framed-IP-Netmask(9)                 Std       0    1    1    0    0    0    0......
相关命令 : 
无。 
## show radius-resource 

show radius-resource 
命令功能 : 
显示RADIUS进程资源使用情况。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius-resource 
  {authentication-group 
|accounting-group 
} [＜group-name 
＞] 
命令参数解释 : 
参数|描述
---|---
authentication-group|显示认证组的资源使用情况；
accounting-group|显示计费组的资源使用情况；
＜group-name＞|RADIUS 认证组或者计费组组名，组名长度为1-31个字符；
缺省 : 
无。 
使用说明 : 
命令带组名为显示指定组下的资源使用情况信息。不带组名为显示全局统计信息以及所有组的资源使用情况的逐个显示。详见范例及说明。 
范例 : 
1.    显示RADIUS指定认证组的资源使用情况：ZXROSNG#show radius-resource authentication-group regcAuthGroup   :   regc                                                                      SendRate: 600       AuthReq Limit :   1800                                                                                 ------------------  --This Group Queue    Info-------------------- --------------------QueueType           Send      PreSend      Peak      LimitHits  HitClock   AuthReq                0             0                   10           0                   -------------------- This Group Message  Info---------------------------ReqMsgType       ReqMsgCount            RespMsgCount        RespMsgType AUTH_REQ          20                                 20                                AUTH_RES    说明：Send            ：表示队列中已发送的请求个数PreSend     ：表示队列中待发送的请求个数Peak            ：表示队列中请求个数的历史最大值LimitHits   ：表示请求队列到达上限值的次数HitClock    ：表示请求队列最近一次到达上限值时的时刻2.    显示RADIUS所有认证组的资源使用情况：ZXROSNG(config-authgrp-1)#show radius-resource authentication-group AuthReq Limit:      12032                                            DmcoaReq  Limit: 6144         -------------------         -The  Global Auth Queue Info---------------------------------QueueType                  Send(DM)  PreSend(COA) Peak   LimitHits HitClock     AuthReq                       0                   0                           10         0                  Rad-C-DmcoaReq      0                  0                            0           0                  Rad-S-DmcoaReq      0                  0                            9           0                  --------------------The  Global Auth Message Info-------------------------------ReqMsgType                                           ReqMsgCount  RespMsgCount RespMsgType        AUTH_REQ                                               20                        20                         AUTH_RES RAD_C_DM_REQ/RAD_S_DM_REQ   0/10                   0/10           DM_ACK/DM_NAK      RAD_C_COA_REQ/RAD_S_COA_REQ  0/0                   0/0              COA_ACK/COA_NAK    --------------------The  Global Auth ReqId Info------------------------------------------------ReqIdResource                   Used         UnUsed       Total       AuthReqId                            0                12032          12032      DmcoaReqId                       0                  6144            6144        ==============================================================AuthGroup    :      1                        SendRate: 600       AuthReq Limit:      1800                                         --------------------This Group Queue    Info----------------------------------------------------QueueType           Send      PreSend   Peak      LimitHits HitClock  AuthReq                0              0                 0           0                 --------------------This Group Message  Info---------------------------------------------------ReqMsgType          ReqMsgCount   RespMsgCount        RespMsgType  AUTH_REQ              0                            0                                 AUTH_RES     说明：Rad-C-DmcoaReq ：表示RAD作为client接收/发送的dmcoa请求队列Rad-S-DmcoaReq ：表示RAD作为sever接收/发送的dmcoa请求队列Send(DM)    ：表示认证请求队列中已发送的请求个数或者DM请求个数PreSend(COA)：表示认证请求队列中待发送的请求个数或者COA请求个数RAD_C_DM_REQ/RAD_S_DM_REQ        ：RAD_C_DM_REQ表示RAD作为client接收(或者发送)的DM请求个数；RAD_S_DM_REQ表示RAD作为server接收(或者发送)的DM请求个数RAD_C_COA_REQ/RAD_S_COA_REQ：RAD_C_DM_REQ表示RAD作为client接收(或者发送)的COA请求个数；RAD_S_DM_REQ表示RAD作为server接收(或者发送)的COA请求个数3.    显示RADIUS指定计费组的资源使用情况ZXROSNG#show radius-resource accounting-group test1AcctGroup        :  test1                         SendRate: 10         AcctReq    Limit :  100                                               LocalBuf   Limit :  100                   WaitSend  Limit   : 100        --------------------This Group Message  Info--------------------------------------------------QueueType        Send     PreSend   Peak   LimitHits      HitClock            AcctReq              0             0                100     1                      06:21:29 09/11/2015 LocalBuf           ---            100            100     1                     06:22:16 09/11/2015 --------------------The Global Queue    Info-----------------------------------------------------QueueType        Send     PreSend   Peak   LimitHits   HitClock            AcctReq              0             0                100     1                   06:21:29 09/11/2015 LocalBuf             ---           100           100      1                  06:22:16 09/11/2015 WaitSend           ---           0                 11        0                        --------------------This Group Message  Info---------------------------------------------------ReqMsgType       ReqMsgCount       RespMsgCount   RespMsgType ACCT_REQ           110                           10                            ACCT_RES   ==============================================================ZXROSNG#说明：AcctReq     ：表示计费请求队列LocalBuf     ：表示计费缓存队列，计费请求超时后若使能缓存则进入计费缓存WaitSend    ：表示计费请求等待发送队列，请求ID资源使用完后，后面的请求进入等待发送队列Send       ：表示队列中已发送的请求个数PreSend    ：表示队列中待发送的请求个数，由于收发送速率的限制，同时发送多个请求时，部分请求将进入待发送队列Peak       ：表示队列中请求个数的历史最大值LimitHits    ：表示请求队列到达上限值的次数HitClock    ：表示请求队列最近一次到达上限值时的时刻4.    显示RADIUS所有计费组的资源使用情况ZXROSNG#show radius-resource accounting-group AcctReq    Limit :  12032                                             LocalBuf   Limit :  12288                  WaitSend  Limit   : 65536     --------------------The Global Queue    Info------------------------------------QueueType          Send      PreSend   Peak      LimitHits HitClock     AcctReqSend         0           0                 0            0                  LocalBuf                 ---         0                  0           0                  WaitSend            ---            0                  0           0                   --------------------The Global Message  Info------------------------------------ReqMsgType        ReqMsgCount       RespMsgCount    RespMsgType    ACCT_REQ            0                                 0                             ACCT_RES        --------------------The Global AcctReqId  Info----------------------------------ReqIdResource       Used                UnUsed         Total          AcctReqId                0                        12032           12032        =========================================================ZXROSNG#
相关命令 : 
无。 
## show radius-server accounting-group 

show radius-server accounting-group 
命令功能 : 
显示RADIUS指定计费组服务器信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius-server accounting-group 
  ＜accounting-group-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜accounting-group-name＞|RADIUS计费服务器组的组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
表头信息包含：1. Accounting-group: 当前表显示的是计费组；2. groupname: 组名；3. Server count: 当前组含有的服务器个数；4. Master： master服务器号，如果没有配置，显示N/A；表项信息：Id: 服务器在组内配置的id；Address： 服务器的IP地址；Port： 服务器的端口号；State： active/dead，服务器的状态；Deadtime： dead状态剩余的时间，精确到秒；Deadclock： 上次dead的时刻。
范例 : 
显示RADIUS指定计费组服务器信息：ZXROSNG(config-authgrp-1)#show radius-server accounting-group 2Accounting-group  2   Server count: 1  Master: 3   Current: 3------------------------------------------------------------------------
Id    Address           Port    State    Deadtime    Deadclock------------------------------------------------------------------------
3     3.3.3.4           1813    active   0'00"                          ------------------------------------------------------------------------
相关命令 : 
show running-config radius 
## show radius-server all 

show radius-server all 
命令功能 : 
显示RADIUS模块所有认证计费组服务器信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius-server all 
 
命令参数解释 : 
					无
				 
缺省 : 
无。 
使用说明 : 
表头信息包含：1. Authentication-group/Accounting-group: 当前表显示的是认证组/计费组；2. groupname: 组名；3. Server count: 当前组含有的服务器个数；4. Master： master服务器号，如果没有配置，显示N/A；表项信息：Id: 服务器在组内配置的id；Address： 服务器的IP地址；Port： 服务器的端口号；State： active/dead，服务器的状态；Deadtime： dead状态剩余的时间，精确到秒；Deadclock： 上次dead的时刻。
范例 : 
显示RADIUS所有认证计费组服务器信息：ZXROSNG(config-acctgrp-2)#show radius-server allAuthentication-group  1   Server count: 1  Master: N/A   Current: 1------------------------------------------------------------------------
Id    Address           Port    State    Deadtime    Deadclock------------------------------------------------------------------------
1     1.2.3.4           1812    active   0'00"                          ------------------------------------------------------------------------
Accounting-group  2   Server count: 1  Master: 3   Current: 3------------------------------------------------------------------------
Id    Address           Port    State    Deadtime    Deadclock------------------------------------------------------------------------
3     3.3.3.4           1813    active   0'00"                          ------------------------------------------------------------------------
相关命令 : 
show running-config radius 
## show radius-server authentication-group 

show radius-server authentication-group 
命令功能 : 
显示RADIUS指定认证组服务器信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show radius-server authentication-group 
  ＜authentication-group-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜authentication-group-name＞|RADIUS认证服务器组的组名，长度为1-31个字符。
缺省 : 
无。 
使用说明 : 
表头信息包含：1. Authentication-group: 当前表显示的是认证组；2. groupname: 组名；3. Server count: 当前组含有的服务器个数；4. Master： master服务器号，如果没有配置，显示N/A；表项信息：Id: 服务器在组内配置的id；Address： 服务器的IP地址；Port： 服务器的端口号；State： active/dead，服务器的状态；Deadtime： dead状态剩余的时间，精确到秒；Deadclock： 上次dead的时刻。
范例 : 
显示RADIUS指定认证组服务器信息：ZXROSNG(config-authgrp-1)#show radius-server authentication-group 1Authentication-group  1   Server count: 2  Master: 4   Current: 4------------------------------------------------------------------------
Id    Address           Port    State    Deadtime    Deadclock------------------------------------------------------------------------
1     1.2.3.4           1812    active   0'00"                          4     5.6.6.8           1485    active   0'00"                          ------------------------------------------------------------------------
相关命令 : 
show running-config radius 
## source-ip 

source-ip 
命令功能 : 
设置设备作为RADIUS服务器时发送DM/CoA报文使用的源IP地址。 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
source-ip 
  ＜source-ip 
＞
no source-ip 
命令参数解释 : 
参数|描述
---|---
＜source-ip＞|IP地址，目前只支持IPv4
缺省 : 
无。 
使用说明 : 
当设备作为RADIUS服务器向RADIUS客户端发送DM/CoA报文时需要指定一个源IP地址，如果不配置，报文将不会发送出去。 
范例 : 
ZXROSNG(config)#radius client-group aaaZXROSNG(config-radius-clientgrp)#source-ip 192.168.122.10ZXROSNG(config-radius-clientgrp)#
相关命令 : 
show running-config radius 
## standby 

standby 
命令功能 : 
使能/去使能客户端组热备功能 
命令模式 : 
 RADIUS客户端组模式  
命令默认权限级别 : 
15 
命令格式 : 
standby 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能本组的热备功能
disable|去使能本组的热备功能
缺省 : 
disable 
使用说明 : 
配置本命令使能或去使能热备功能。热备功能的实现参看具体用户及业务的说明。 
范例 : 
ZXROSNG(config-radius-clientgrp)#standby enableZXROSNG(config-radius-clientgrp)#
相关命令 : 
show configuration radius client-groupshow running-config radius 
## timeout 

timeout 
命令功能 : 
设置报文的超时时间。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
timeout 
  ＜timeout 
＞
no timeout 
命令参数解释 : 
参数|描述
---|---
＜timeout＞|报文超时时间，单位：秒，范围：1-255
缺省 : 
3秒。 
使用说明 : 
发送给服务器的请求报文的处理描述如下：1. 发起请求，等待回应，如果服务器及时回应，那么处理流程结束；2. 如果在等待了一定的时长（组模式下timeout配置的值）后没有收到回应则认为请求超时，重新发起请求，继续等待回应；4. 重发的过成功如果得到回应则流程结束；3. 一共可以重传(retry)若干次（组配置模式下max-retries配置的值），如果一直得不到回应，则该请求失败并将失败结果通知用户。
范例 : 
设置RADIUS计费服务器超时时间为5秒：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#timeout 5ZXROSNG(config-acctgrp-1)#
相关命令 : 
max-retriesshow running-config radius
## timeout 

timeout 
命令功能 : 
设置报文的超时时间。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
timeout 
  ＜timeout 
＞
no timeout 
命令参数解释 : 
参数|描述
---|---
＜timeout＞|报文超时时间，单位：秒，范围：1-255
缺省 : 
3秒。 
使用说明 : 
发送给服务器的请求报文的处理描述如下：1. 发起请求，等待回应，如果服务器及时回应，那么处理流程结束；2. 如果在等待了一定的时长（组模式下timeout配置的值）后没有收到回应则认为请求超时，重新发起请求，继续等待回应；4. 重发的过成功如果得到回应则流程结束；3. 一共可以重传(retry)若干次（组配置模式下max-retries配置的值），如果一直得不到回应，则该请求失败并将失败结果通知用户。
范例 : 
设置RADIUS认证服务器超时时间为5秒：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#timeout 5ZXROSNG(config-authgrp-1)#
相关命令 : 
max-retriesshow running-config radius
## user-name-format 

user-name-format 
命令功能 : 
配置请求报文的用户名格式。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
user-name-format 
  {[{include-domain 
|strip-domain 
|only-domain 
|original 
}],[max-length 
 ＜username-max-len 
＞],[pattern 
 class1 
],[delimiter 
 ＜domain-delimiter 
＞]}
no user-name-format 
  {[domain-format 
],[max-length 
],[pattern 
],[domain-delimiter 
]}
				
命令参数解释 : 
参数|描述
---|---
include-domain|包含域名的格式
strip-domain|不包含域名的格式
only-domain|只包含域名的格式
original|使用用户上送的原始的用户名的格式
＜username-max-len＞|用户名最大长度限制；
class1|用户名字格式限制模式1：用户名和域名 只包括大小写字母、数字、"-"、"_"。不允许包含其它字符
＜domain-delimiter＞|域名分隔符，长度为一个字符，默认值为"@"
缺省 : 
域名格式为strip-domain，域名分隔符为"@"，默认无长度与模式限制。 
使用说明 : 
该命令用来设置用户名属性（User-Name，标准属性1号）组装的方式，以及格式的合法性检查方式。假设用户上送的用户名为xxx，其所在的域为local，配置与用户名组装结果的对应如下：include-domain：xxx@local；strip-domain：xxxonly-domain：localoriginal：xxx。组装后的用户名如果超过username-max-len的限制则认为不合法；如果配置了class1模式，则用户名需要满足其限制，否则认为不合法。不合法的用户名请求不予发送。
范例 : 
配置NAS向RADIUS计费服务器发送的用户名字段包含域名，分隔符为“#”，限制最大长度为64，格式模式检查为class1：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#user-name-format delimiter # pattern class1 max-length 64 include-domain
相关命令 : 
show running-config radius 
## user-name-format 

user-name-format 
命令功能 : 
配置请求报文的用户名格式。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
user-name-format 
  {[{include-domain 
|strip-domain 
|only-domain 
|original 
}],[max-length 
 ＜username-max-len 
＞],[pattern 
 class1 
],[delimiter 
 ＜domain-delimiter 
＞]}
no user-name-format 
  {[domain-format 
],[max-length 
],[pattern 
],[domain-delimiter 
]}
				
命令参数解释 : 
参数|描述
---|---
include-domain|包含域名的格式
strip-domain|不包含域名的格式
only-domain|只包含域名的格式
original|使用用户上送的原始的用户名的格式
＜username-max-len＞|用户名最大长度限制
class1|用户名字格式限制模式1：用户名和域名 只包括大小写字母、数字、"-"、"_"。不允许包含其它字符
＜domain-delimiter＞|域名分隔符，长度为一个字符，默认值为"@"
缺省 : 
域名格式为strip-domain，域名分隔符为"@"，默认无长度与模式限制。 
使用说明 : 
该命令用来设置用户名属性（User-Name，标准属性1号）组装的方式，以及格式的合法性检查方式。假设用户上送的用户名为xxx，其所在的域为local，配置与用户名组装结果的对应如下：include-domain：xxx@local；strip-domain：xxxonly-domain：localoriginal：xxx。组装后的用户名如果超过username-max-len的限制则认为不合法；如果配置了class1模式，则用户名需要满足其限制，否则认为不合法。不合法的用户名请求不予发送。
范例 : 
配置NAS向RADIUS计费服务器发送的用户名字段包含域名，分隔符为“#”，限制最大长度为64，格式模式检查为class1：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#user-name-format delimiter # pattern class1 max-length 64 include-domainZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
## vendor 

vendor 
命令功能 : 
配置NAS向RADIUS服务器发送的报文中是否包含ZTE自定义属性。 
命令模式 : 
 RADIUS计费组模式  
命令默认权限级别 : 
15 
命令格式 : 
vendor 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|发送厂商自定义属性
disable|不发送厂商自定义属性
缺省 : 
enable。 
使用说明 : 
选择enable配置时将在发送的RADIUS请求报文中包含ZTE的厂商属性，否则将不包含。 
范例 : 
配置发送的RADIUS计费协议包中发送厂商自定义属性：ZXROSNG(config)#radius accounting-group 1ZXROSNG(config-acctgrp-1)#vendor enable
相关命令 : 
show running-config radius 
## vendor 

vendor 
命令功能 : 
配置NAS向RADIUS服务器发送的报文中是否包含ZTE自定义属性。 
命令模式 : 
 RADIUS认证组模式  
命令默认权限级别 : 
15 
命令格式 : 
vendor 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|发送厂商自定义属性
disable|不发送厂商自定义属性
缺省 : 
enable。 
使用说明 : 
选择enable配置时将在发送的RADIUS请求报文中包含ZTE的厂商属性，否则将不包含。 
范例 : 
配置发送的RADIUS认证协议包中不发送厂商自定义属性：ZXROSNG(config)#radius authentication-group 1ZXROSNG(config-authgrp-1)#vendor disableZXROSNG(config-authgrp-1)#
相关命令 : 
show running-config radius 
# TACACS+配置命令 
## debug tacplus accounting 

debug tacplus accounting 
命令功能 : 
打开TACPLUS 记账信息显示。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug tacplus accounting 
 
no debug tacplus accounting 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开TACPLUS 记账信息显示。 
范例 : 
打开TACPLUS 记账信息显示：ZXROSNG#debug tacplus accounting TACPLUS accounting debugging is on
相关命令 : 
debug tacplus all 
## debug tacplus all 

debug tacplus all 
命令功能 : 
打开TACPLUS 所有debug信息显示。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug tacplus all 
 
no debug tacplus all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开TACPLUS 所有debug信息显示。 
范例 : 
打开TACPLUS 所有debug信息显示：ZXROSNG#debug tacplus allAll TACPLUS debugging has been turned on
相关命令 : 
debug tacplus authenticationdebug tacplus authorizationdebug tacplus accountingdebug tacplus exception
## debug tacplus authentication 

debug tacplus authentication 
命令功能 : 
打开TACPLUS 认证信息显示。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug tacplus authentication 
 
no debug tacplus authentication 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开TACPLUS 认证信息显示。 
范例 : 
打开TACPLUS 认证信息显示：ZXROSNG#debug tacplus authentication TACPLUS authentication debugging is on
相关命令 : 
debug tacplus all 
## debug tacplus authorization 

debug tacplus authorization 
命令功能 : 
打开TACPLUS 授权信息显示。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug tacplus authorization 
 
no debug tacplus authorization 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开TACPLUS 授权信息显示。 
范例 : 
打开TACPLUS 授权信息显示：ZXROSNG#debug tacplus authorization TACPLUS authorization debugging is on
相关命令 : 
debug tacplus all 
## debug tacplus exception 

debug tacplus exception 
命令功能 : 
打开TACPLUS 异常信息显示。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug tacplus exception 
 
no debug tacplus exception 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开TACPLUS 异常信息显示。 
范例 : 
打开TACPLUS 异常信息显示：ZXROSNG#debug tacplus exception TACPLUS exception debugging is on
相关命令 : 
debug tacplus all 
## server6 

server6 
命令功能 : 
该命令工作于Tacplus服务器组模式下，用于配置TACPLUS的IPv6服务器组成员，使用no命令删除服务器组成员。 
命令模式 : 
 Tacplus服务器组模式  
命令默认权限级别 : 
15 
命令格式 : 
server6 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜ipv6-address 
＞ [port 
 {＜port-number 
＞|＜49 
＞}] [{master 
|slave 
}]
no server6 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜ipv6-address 
＞ [port 
 {＜port-number 
＞|＜49 
＞}]
				
命令参数解释 : 
参数|描述
---|---
mng|管理口VRF
＜vrf-name＞|VRF名称，长度1–32个字符
＜ipv6-address＞|TACACS+服务器IPv6地址，必须是已经配置过的TACACS+服务器
＜port-number＞|TACACS+服务器端口号，范围：1025–65535
＜49＞|TACACS+服务器默认端口号
master|标记此服务器为主服务器
slave|标记此服务器为备用服务器，此为默认值
缺省 : 
端口缺省值为49 
使用说明 : 
1.  必须先配置TACPLUS服务器组和TACACS+host6服务器，即server6的vrf名称和IP地址，以及端口信息必须与命令与tacacs-server host6配置的一致，每组下Server的最大数量为4个。2.  配置为master的服务器，会优先选择，若master的状态为dead，就在组内依据配置顺序从当前服务器开始轮循选择一个为active状态的服务器。3.  需先配置相应的全局服务器，才能在组下进行绑定配置。删除组下的配置后才能删除全局配置下的服务器。
范例 : 
进入服务器组配置模式，配置TACPLUS服务器组成员，并查看配置结果ZXROSNG(config)# show running-config tacplus !<TACPLUS>tacacs enabletacacs-server host 192.65.254.147 key encrypted AC4C378D1C985ECA33C9D12E652E3EAB0F34CA22D1409AAABD38171B724C4416169FB58C63856B119FCF04D636C90DAB4C8D5E68C0CBBB344A44AD5C7C38523Atacacs-server host6 4000::56 timeout 10 key encrypted 145E3E04B79DF8DFAF4A80874F9A03423344A4CE5E566F6A75E1AFF2A512A2D9BA46696C2F0460B90D6690328BAA22BA0D582CD2DB4DF3A6EB86F38BF1728B58tacacs-server host6 vrf v6 6000::53 port 4000 key encrypted 145E3E04B79DF8DFAF4A80874F9A03423344A4CE5E566F6A75E1AFF2A512A2D9BA46696C2F0460B90D6690328BAA22BA0D582CD2DB4DF3A6EB86F38BF1728B58tacplus group-server t4  server 192.65.254.147$!</TACPLUS>ZXROSNG(config)#tacplus group-server tttZXROSNG(config-sg)#server6 vrf v6 6000::53 port 4000                             ZXROSNG(config-sg)#show this!<TACPLUS>  server6 vrf v6 6000::53 port 4000!</TACPLUS>ZXROSNG(config-sg)#show tacplus group-server ttttacplus group-server ttt  state:active  server   vrf:v6  ip_addr:6000::53  port:4000  current serverZXROSNG(config-sg)#
相关命令 : 
tacacs enabletacacs-server host6tacplus group-server
## server 

server 
命令功能 : 
该命令工作于Tacplus服务器组模式下，用于配置TACPLUS的服务器组成员，使用no命令删除服务器组成员。 
命令模式 : 
 Tacplus服务器组模式  
命令默认权限级别 : 
15 
命令格式 : 
server 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜ip-address 
＞ [port 
 {＜port-number 
＞|＜49 
＞}] [{master 
|slave 
}]
no server 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜ip-address 
＞ [port 
 {＜port-number 
＞|＜49 
＞}]
				
命令参数解释 : 
参数|描述
---|---
mng|管理口VRF
＜vrf-name＞|VRF名称，长度1–32个字符
＜ip-address＞|TACACS+服务器IP地址，必须是已经配置过的TACACS+服务器
＜port-number＞|TACACS+服务器端口号，范围：1025–65535
＜49＞|TACACS+服务器默认端口号
master|标记此服务器为主服务器
slave|标记此服务器为备用服务器，此为默认值
缺省 : 
无 
使用说明 : 
1.  必须先配置TACPLUS服务器组和TACACS+ 全局服务器host，即server 的vrf名称和IP地址，以及端口号必须与命令tacacs-server host配置信息一致每组server的最大数量为4个。2.  配置为master的服务器，会优先选择，若master的状态为dead，就在组内依据配置顺序从当前服务器开始轮循选择一个为active状态的服务器。3.  需先配置相应的全局服务器，才能在组下进行绑定配置。删除组下的配置后才能删除全局配置下的服务器。
范例 : 
进入服务器组配置模式，配置TACPLUS服务器组成员：ZXROSNG(config)#tacacs-server host 192.168.2.49ZXROSNG(config)#tacplus group-server  tacNtTacZXROSNG(config-sg)#server 192.168.2.49
相关命令 : 
tacacs enabletacacs-server hosttacplus group-server
## show debug tacplus 

show debug tacplus 
命令功能 : 
显示TACPLUS 已经打开的debug选项。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug tacplus 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示TACPLUS 已经打开的debug选项。 
范例 : 
显示TACPLUS 已经打开的debug选项：ZXROSNG#show debug tacplus TACACS:  TACACS authentication debugging is on  TACACS authorization debugging is on  TACACS accounting debugging is on  TACACS exception debugging is on
相关命令 : 
无 
## show tacacs global-config 

show tacacs global-config 
命令功能 : 
该命令工作于除用户模式外其他所有模式，用于显示tacacs+的全局配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show tacacs global-config 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
    显示TACACS+的全局配置信息，未配置的显示为参数默认值，没有默认值的不显示。    具体显示参数信息包括：1）    tacacs+协议开关配置信息enable/disable，如：tacacs enable2）    tacacs enable-packet配置信息，即显示enable-packet authen-type 的配置信息。 3）    tacacs author-packet配置信息,包括authen-type、authen-method和authen-service的配置信息。4）    tacacs-server配置信息：包括packect、timeout、deadtime和key的信息。。例如：tacacs enable  packet:1024  timeout:5  deadtime:55）    tacacs-client和tacacs-client6配置信息，包括IP地址和端口号，没有配置则不显示。如：tacacs-client 192.168.122.100
范例 : 
显示TACACS+的全局配置信息：ZXROSNG(config)#tacacs-server key zzzz    ZXROSNG(config)#show tacacs global-config tacacs enable  packet:1024  timeout:5  encrypted key:955E9DABDB10FF18D73C9F216C3D1D143CFBA2569F9EDA01BA0FC16E862FB6C0B014CC31331D566AB2EB4F2BD04A76D2C7393312344F49C5861831EA382AA753
相关命令 : 
tacacs enabletacacs-server timeouttacacs-clienttacacs-server keytacacs-server packettacacs enable-packet authen-typetacacs author-packet authen-type tacacs author-packet authen-methodtacacs author-packet authen–service
## show tacacs-server6 

show tacacs-server6 
命令功能 : 
该命令工作于除用户模式外其他所有模式，用于显示TACACS+ IPv6 服务器的信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show tacacs-server6 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
    显示tacacs-server host6配置的相关参数，未配置的参数显示默认值。    具体显示参数信息包括：1）    Server  IP地址和端口号，以及运行状态信息。2）    Server timeout时间。3）    Server key信息，若在命令tacacs-server host6中配置了key的值，则显示为其配置的值的加密字串。
范例 : 
显示TACACS+ IPv6 服务器的配置信息：ZXROSNG(config)#show tacacs-server6tacacs-server  ip_addr:2000::147  port:49  active  encrypted key:43EC772D8A3D118A3E4304515C80BD935A6FFDA8D0C4100E1A8BB60E64B23678EB747E84419275C5396A1FD56812D5A23F92283CB5F2E625AA7A87315C400BD4tacacs-server  ip_addr:1000::147  port:49  active  encrypted key:43EC772D8A3D118A3E4304515C80BD935A6FFDA8D0C4100E1A8BB60E64B23678EB747E84419275C5396A1FD56812D5A23F92283CB5F2E625AA7A87315C400BD4tacacs-server  vrf:v6  ip_addr:2000::147  port:49  activetacacs-server  vrf:v4v6  ip_addr:2000::147  port:49  active
相关命令 : 
tacacs-server host6 
## show tacacs-server 

show tacacs-server 
命令功能 : 
该命令工作于除用户模式外其他所有模式，用于显示tacacs+服务器的配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show tacacs-server 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
    显示tacacs-server host配置的相关参数，未配置的参数显示默认值。    具体显示参数信息包括：1）    Server  IP地址和端口号，以及运行状态信息，如：tacacs-server  ip_addr:192.168.122.100  port:49  active2）    Server timeout时间。3）    Server key信息，显示为其配置的值的加密字串。
范例 : 
显示TACACS+服务器的配置信息：ZXROSNG(config-authgrp-1)#show tacacs-server tacacs-server  ip_addr:192.168.2.49  port:49  encrypted key:145E3E04B79DF8DFAF4A80874F9A03423344A4CE5E566F6A75E1AFF2A512A2D9BA46696C2F0460B90D6690328BAA22BA0D582CD2DB4DF3A6EB86F38BF1728B58tacacs-server  ip_addr:192.168.10.200  port:1030  
相关命令 : 
tacacs enabletacacs-server host
## show tacplus group-server 

show tacplus group-server 
命令功能 : 
该命令工作于除用户模式外其他所有模式，用于显示TACPLUS服务器组的配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show tacplus group-server 
  [＜group-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜group-name＞|TACPLUS服务器组名称，长度1–31个字符。此参数为可选项，缺省时为显示所有服务器组的配置信息。
缺省 : 
无 
使用说明 : 
1.TACPLUS服务器组不能以数字开头，不能是关键字tacacs+。2.具体显示参数信息包括：   1）    服务器组组名，如：        tacplus group-server t  2）    该服务器组状态信息active/timeout，如：        tacplus group-server t      state:timeout  (UTC 07:02:05 08/12/2014)。        tacplus group-server v6      state:active  3）    组下服务器配置信息,包括server ip或者vrf名和ip、服务器 端口号(缺省为49)、服务器是主服务器还是从服务器、是否为最近可用的服务器。
范例 : 
显示TACPLUS 所有服务器组的配置信息：ZXROSNG(config)#show tacplus group-server tacplus group-server tstate:timeout  (UTC 07:02:05 08/12/2014)server  ip_addr:192.168.122.100  port:49  slave  current servertacplus group-server v6state:activeserver  ip_addr:2000::53  port:49  slave  current serverZXROSNG(config)#tacplus group-server t1  server  ip_addr:10.40.65.136
相关命令 : 
tacacs enabletacplus group-serversever
## tacacs author-packet authen-method 

tacacs author-packet authen-method 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于配置授权请求报文中认证服务字段，使用no命令删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs author-packet authen-method 
  ＜authen-method 
＞
no tacacs author-packet authen-method 
命令参数解释 : 
参数|描述
---|---
＜authen-method＞|notset    notset方法none    none方法krb5    krb5方法line    line方法enable    enable方法local    local方法tacplus    tacplus方法guest    guest方法radius    radius方法krb4    krb4方法rcmd    rcmd方法
缺省 : 
无 
使用说明 : 
1.  这个字段的值和认证请求start报文中service字段的值，即服务类型相对应。对于某些类型，可能服务器不支持，请确认后配置。2.  没有默认值。缺省配置时，其值为0,即为none服务类型。
范例 : 
配置授权请求报文认证方法字段为none：ZXROSNG(config)# tacacs author-packet authen-method none
相关命令 : 
show tacacs global-config
## tacacs author-packet authen-service 

tacacs author-packet authen-service 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于配置授权请求报文中认证方法字段，使用no命令删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs author-packet authen-service 
  ＜authen-service 
＞
no tacacs author-packet authen-service 
命令参数解释 : 
参数|描述
---|---
＜authen-service＞|none    none服务login    login服务enable    enable服务ppp    ppp服务arap    arap服务pt    pt服务rcmd    rcmd服务x25    x25服务nasi    nasi服务fwproxy    fwproxy服务
缺省 : 
无 
使用说明 : 
1.  认证方法表示NAS(网络接入服务器)客户端获取用户信息的方法。比如local是指从NAS的本地用户数据库获取用户信息；radius是指RADIUS认证协议，即根据radius协议获取用户信息；tacplus是指TACSCS+认证协议，即根据TACACS+协议获取用户信息。2.  没有默认值。
范例 : 
配置授权请求报文认证服务字段为none：ZXROSNG(config)# tacacs author-packet authen–service none
相关命令 : 
show tacacs global-config
## tacacs author-packet authen-type 

tacacs author-packet authen-type 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于配置授权请求报文中认证类型字段，使用no命令删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs author-packet authen-type 
  ＜authen-type 
＞
no tacacs author-packet authen-type 
命令参数解释 : 
参数|描述
---|---
＜authen-type＞|none    none认证方式ascii    ascii认证方式pap    pap认证方式chap    chap认证方式arap    arap认证方式mschap    mschap认证方式
缺省 : 
无 
使用说明 : 
1.  这个字段的值和认证请求start报文中authen-type字段的值，即认证类型相对应。表示其使用的认证类型。对于某些类型，可能服务器不支持，请确认后配置。2.  没有默认值。缺省配置时，其值为认证请求的start报文中authen-type字段的值。
范例 : 
配置授权请求报文认证类型字段为ascii：ZXROSNG(config)# tacacs author-packet authen-type ascii
相关命令 : 
show tacacs global-config
## tacacs enable-packet authen-type 

tacacs enable-packet authen-type 
命令功能 : 
该命令工作于全局配置模式，用于强制填充enable认证的start报文中认证类型字段的值以满足服务器器对于该认证方式对于该字段属性值的要求，对于某些类型，可能服务器不支持，请确认后配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs enable-packet authen-type 
  ＜authen-type 
＞
no tacacs enable-packet authen-type 
命令参数解释 : 
参数|描述
---|---
＜authen-type＞|none    none认证方式ascii    ascii认证方式pap    pap认证方式chap    chap认证方式arap    arap认证方式mschap    mschap认证方式
缺省 : 
无 
使用说明 : 
1. 使用no命令删除配置。2. 没有默认值。
范例 : 
配置enable认证类型字段为ascii：ZXROSNG(config)# tacacs enable-packet authen-type ascii
相关命令 : 
show tacacs global-config
## tacacs 

tacacs 
命令功能 : 
打开或者关闭TACACS+协议功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启TACACS+协议功能。
disable|关闭TACACS+协议功能。
缺省 : 
无 
使用说明 : 
打开或者关闭TACACS+协议功能。 
范例 : 
开启TACACS+协议功能：ZXROSNG(config)#tacacs enable关闭TACACS+协议功能：ZXROSNG(config)#tacacs disable
相关命令 : 
无 
## tacacs-client6 

tacacs-client6 
命令功能 : 
配置TACACS+客户端IPv6地址和端口，作为设备和TACACS+ IPv6服务器通信的地址。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs-client6 
  {＜ipv6-address 
＞|source-interface 
 ＜interfacename 
＞} [port 
 ＜port-number 
＞]
no tacacs-client6 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|客户端IPv6地址
＜interfacename＞|引用的接口名称
＜port-number＞|客户端四层端口，范围：1025-65535
缺省 : 
无 
使用说明 : 
用户根据实际需要决定是否配置TACACS+客户端IPv6地址和端口。如果要限制了客户端的端口需慎重，由于同时与一个服务器只能建立一个连接，因此与只支持多连接不支持单连接的服务器通信同一时刻只能进行一次会话。
范例 : 
配置TACACS+客户端地址为2000::101，端口2049：ZXROSNG(config)#tacacs-client6 2000::101 port 2049ZXROSNG(config)#
相关命令 : 
tacacs enable
## tacacs-client 

tacacs-client 
命令功能 : 
配置TACACS+客户端IP地址和端口，作为高端路由器和TACACS+服务器通信的IP地址。使用no命令 删除配置。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs-client 
  {＜ip-address 
＞|source-interface 
 ＜interfacename 
＞} [port 
 ＜port-number 
＞]
no tacacs-client 
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|客户端IP地址
＜interfacename＞|引用的接口名称
＜port-number＞|客户端四层端口，范围：1025-65535
缺省 : 
无。 
使用说明 : 
用户根据实际需要决定是否配置TACACS+客户端IP地址和端口，如果配置必须配置正确。
范例 : 
配置TACACS+客户端地址为192.168.2.10，端口2049：ZXROSNG(config)# tacacs-client 192.168.2.10 port 2049
相关命令 : 
tacacs enable 
## tacacs-server deadtime 

tacacs-server deadtime 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于设置TACACS+服务器进入dead状态保持的时间,单位为分钟。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs-server deadtime 
  ＜deadtime 
＞
no tacacs-server deadtime 
命令参数解释 : 
参数|描述
---|---
＜deadtime＞|TACACS+服务器进入dead状态保持的时间，单位分钟
缺省 : 
5分钟 
使用说明 : 
1.  配置以后，若服务器由于等待回应超时，即进入dead状态，并保存这个状态deadtime的时间长度，到时后即刻进入ative状态；配置为0，仍然发生切换，但不保持dead状态。2.  服务器的选择是跳过dead状态的服务器，首选标记为master的服务器，若没有，则依据组内配置顺序从当前服务器开始轮循选择一个active的服务器进行链接尝试。3.  配置了master服务器的的情况下不要配置deatime为0，因为当master连接超时后不保持dead状态，会一直选择master服务器进行尝试连接。4.  no命令恢复到默认值配置。默认为5分钟。
范例 : 
设置服务器deadtime时间为14：ZXROSNG(config)#tacacs-server deadtime 14ZXROSNG(config)#查看当前deadtime配置：ZXROSNG(config)#show tacacs global-config tacacs enable  packet:1024  timeout:5  deadtime:14
相关命令 : 
tacacs enable 
## tacacs-server host6 

tacacs-server host6 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于配置TACACS+ IPv6 服务器参数。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs-server host6 
  [vrf 
 {mng 
|＜vrfname 
＞}] ＜ipv6-address 
＞ [{[port 
 {＜49 
＞|＜port-number 
＞}],[timeout 
 ＜timeout 
＞],[key 
 {encrypted 
 ＜encrypted-key 
＞|＜key 
＞}]}]
no tacacs-server host6 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜ipv6-address 
＞ [port 
 {＜49 
＞|＜port-number 
＞}]
				
命令参数解释 : 
参数|描述
---|---
mng|管理口VRF
＜vrfname＞|VRF名称，长度1–32个字符
＜ipv6-address＞|TACACS+服务器IPv6地址
＜49＞|默认端口号
＜port-number＞|定义TACACS+服务器的端口号, 范围：1025–65535
＜timeout＞|连接超时时间，此处配置将使全局配置无效，范围：1–1000，单位：秒
＜encrypted-key＞|NAS和TACACS+服务器之间的密文加密密钥，此处配置将使全局配置无效，长度128个字符（不包括空格）
＜key＞|NAS和TACACS+服务器之间的明文加密密钥，此处配置将使全局配置无效，长度1-63个字符（不包括空格）
缺省 : 
port默认值为49。 
使用说明 : 
1.  配置TACACS+ IPv6 服务器参数，最大可配置服务器数由性能参数决定，如BRAS项目中为256个。其中引用的vrf必须已经使能了IPv6地址族。2.  此处配置的timeout和key值是针对该服务器的，若没有配置即使用的是全局配置的timeout和key值。
范例 : 
配置地址为4000::56的服务器，端口值为默认ZXROSNG(config)#tacacs-server host6 4000::56 ZXROSNG(config)#show tacacs-server6tacacs-server  ip_addr:4000::56  port:49  activeZXROSNG(config)#
更新配置上述服务器，为其添加共享密钥 “zxr10”，timeout为10s，并查看结果配置结果：ZXROSNG(config)#tacacs-server host6 4000::56 timeout 10 key zxr10ZXROSNG(config)#show tacacs-server6tacacs-server  ip_addr:4000::56  port:49  timeout:10  active  encrypted key:145E3E04B79DF8DFAF4A80874F9A03423344A4CE5E566F6A75E1AFF2A512A2D9BA46696C2F0460B90D6690328BAA22BA0D582CD2DB4DF3A6EB86F38BF1728B58ZXROSNG(config)#
添加新的服务器，地址 6000::53，vrf名称为v6， 端口4000，密钥加密输入：ZXROSNG(config)#tacacs-server host6 vrf v6 6000::53 port 4000 key encrypted 145E3E04B79DF8DFAF4A80874F9A03423344A4CE5E566F6A75E1AFF2A512A2D9BA46696C2F0460B90D6690328BAA22BA0D582CD2DB4DF3A6EB86F38BF1728B58ZXROSNG(config)#show tacacs-server6tacacs-server  ip_addr:4000::56  port:49  timeout:10  active  encrypted key:145E3E04B79DF8DFAF4A80874F9A03423344A4CE5E566F6A75E1AFF2A512A2D9BA46696C2F0460B90D6690328BAA22BA0D582CD2DB4DF3A6EB86F38BF1728B58tacacs-server  vrf:v6  ip_addr:6000::53  port:4000  active  encrypted key:145E3E04B79DF8DFAF4A80874F9A03423344A4CE5E566F6A75E1AFF2A512A2D9BA46696C2F0460B90D6690328BAA22BA0D582CD2DB4DF3A6EB86F38BF1728B58ZXROSNG(config)#
相关命令 : 
tacacs enableserver6
## tacacs-server host 

tacacs-server host 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于配置TACACS+服务器(IPv4)参数。使用no命令删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs-server host 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜ip-address 
＞ [{[port 
 {＜49 
＞|＜port-number 
＞}],[timeout 
 ＜timeout 
＞],[key 
 {encrypted 
 ＜encrypted-key 
＞|＜key 
＞}]}]
no tacacs-server host 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜ip-address 
＞ [port 
 {＜49 
＞|＜port-number 
＞}]
				
命令参数解释 : 
参数|描述
---|---
mng|管理口VRF
＜vrf-name＞|VRF名称，长度1–32个字符
＜ip-address＞|TACACS+服务器IP地址
＜49＞|默认端口号
＜port-number＞|定义TACACS+服务器的端口号，范围：1025–65535
＜timeout＞|连接超时时间，此处配置将使全局配置无效，范围：1–1000，单位：秒
＜encrypted-key＞|NAS和TACACS+服务器之间的密文加密密钥，此处配置将使全局配置无效，长度128个字符（不包括空格）
＜key＞|NAS和TACACS+服务器之间的明文加密密钥，此处配置将使全局配置无效，长度1-63个字符（不包括空格）
缺省 : 
port默认49。 
使用说明 : 
1.  配置TACACS+服务器(IPv4)参数。最大可配置服务器数由性能参数决定，如BRAS项目中为256个。使用no命令删除配置。2.  此处配置的timeout和key值是针对该服务器的，若没有配置即使用的是全局配置的timeout和key值。
范例 : 
配置TACACS+服务器地址为192.168.2.49，端口默认：ZXROSNG(config)#tacacs-server host 192.168.2.49更新配置上述服务器，为其添加共享密钥 “zxr10”，并查看结果ZXROSNG(config)#tacacs-server host 192.168.2.49 key zxr10ZXROSNG(config)#show running-config tacplus !<TACPLUS>tacacs enable145E3E04B79DF8DFAF4A80874F9A03423344A4CE5E566F6A75E1AFF2A512A2D9BA46696C2F0460B90D6690328BAA22BA0D582CD2DB4DF3A6EB86F38BF1728B58!</TACPLUS>添加新的服务器，192.168.10.200，端口1030，共享密钥密文输入（该密钥对应明文为zte），并查看结果：ZXROSNG(config)#tacacs-server host 192.168.10.200 port 1030 key encrypted 30FD73F50A27785F93622A84DDD81BD4908AC3F8B8592C89C1BFFA6FEC35A0D3CA5A47042B891AE780450CAB513FA47FCEB551F82FC4D1741D58612D9FE71267ZXROSNG(config)#show running-config tacplus !<TACPLUS>tacacs enabletacacs-server host 192.168.10.200 port 1030 key encrypted 30FD73F50A27785F93622A84DDD81BD4908AC3F8B8592C89C1BFFA6FEC35A0D3CA5A47042B891AE780450CAB513FA47FCEB551F82FC4D1741D58612D9FE71267!</TACPLUS>ZXROSNG(config)#
相关命令 : 
tacacs enable 
## tacacs-server key 

tacacs-server key 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于配置全局TACACS+协议加密密钥，对所有未指定密钥的服务器有效。使用no命令删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs-server key 
  {encrypted 
 ＜encrypted-key 
＞|＜key 
＞}
no tacacs-server key 
命令参数解释 : 
参数|描述
---|---
＜encrypted-key＞|NAS和服务器交换报文使用的密文加密密钥。长度128个字符（不包括空格）
＜key＞|NAS和服务器交换报文使用的明文加密密钥。长度1–63个字符（不包括空格）
缺省 : 
无 
使用说明 : 
配置全局TACACS+协议加密密钥，对所有未指定密钥的服务器有效。 
范例 : 
配置TACACS+全局明文密钥为“zxr10”：ZXROSNG(config)#tacacs-server key zxr10
相关命令 : 
tacacs enable 
## tacacs-server packet 

tacacs-server packet 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于配置tacacs+协议最大接收报文长度，默认1024B使用no命令恢复到默认配置1024。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs-server packet 
  {＜length 
＞}
no tacacs-server packet 
命令参数解释 : 
参数|描述
---|---
＜length＞|作用：设置tacacs+协议最大接收报文长度。取值范围：1024~4096，单位字节。默认值：1024B。
缺省 : 
默认1024字节。 
使用说明 : 
1.  配置TACACS+协议最大报文长度， 范围：1024–4096，单位：字节(B)。2.  默认为1024B。用户可根据实际情况修改配置，改变配置后，在下次enable协议后生效。
范例 : 
配置TACACS+报文最大长度为1096字节：ZXROSNG(config)#tacacs-server packet 1096
相关命令 : 
tacacs enable 
## tacacs-server timeout 

tacacs-server timeout 
命令功能 : 
该命令工作于TACACS+全局配置模式，用于配置TACACS+服务器连接超时时长，默认5s。使用no命令恢复到默认配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacacs-server timeout 
  {＜timeout 
＞}
no tacacs-server timeout 
命令参数解释 : 
参数|描述
---|---
＜timeout＞|作用：设置超时时长，单位为秒。有效值范围：1~1000,单位秒。默认值：5s。
缺省 : 
默认5秒。 
使用说明 : 
1.  配置全局TACACS+服务器连接超时时长,对所有没指定timeout的服务器有效2.  默认值为5s，使用no命令恢复默认设置为5s。服务器超时没有响应，提示超时。
范例 : 
配置TACACS+服务器端超时时长为10秒：ZXROSNG(config)#tacacs-server timeout 10
相关命令 : 
tacacs enable 
## tacplus group-server 

tacplus group-server 
命令功能 : 
该命令工作于TACPLUS全局配置模式，用于创建并进入TACPLUS服务器组配置模式。使用no命令删除服务器组配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tacplus group-server 
  {＜group-name 
＞}
no tacplus group-server 
  {＜group-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜group-name＞|TACPLULS服务器组名称，长度1–31个字符
缺省 : 
无 
使用说明 : 
TACPLUS服务器组不能以数字开头，不能是关键字tacacs+。 
范例 : 
进入服务器组配置模式，配置TACPLUS服务器组tacNtTac：ZXROSNG(config)# tacplus group-server tacNtTacZXROSNG(config-sg)#
相关命令 : 
tacacs enableserver
# URPF配置命令 
## ipv4 verify unicast source reachable-via 

ipv4 verify unicast source reachable-via 
命令功能 : 
解绑/绑定URPF到接口 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv4 verify unicast source reachable-via 
  {rx 
 interface 
 ＜interface-name 
＞ [acl-name 
 ＜acl-name 
＞]|any 
 interface 
 ＜interface-name 
＞ [acl-name 
 ＜acl-name 
＞] [ignore-default-route 
]}
no ipv4 verify unicast source reachable-via 
 interface 
 ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
rx|严格模式
＜interface-name＞|解绑URPF的接口名称
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
any|松散模式
＜interface-name＞|解绑URPF的接口名称
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
ignore-default-route|默认路由选项
缺省 : 
无 
使用说明 : 
绑定/解绑时接口必须存在。 
范例 : 
绑定URPF到接口gei-0/1/0/1：ZXROSNG(config)#ipv4 verify unicast source reachable-via any interface gei-0/1/0/1 acl-name myacl ignore-default-route查看配置结果信息：ZXROSNG(config)#show running-config urpf!<URPF>interface gei-0/1/0/1  ipv4 verify unicast source reachable-via any acl-name myacl ignore-default-route$
相关命令 : 
无 
## ipv4 verify unicast source reachable-via 

ipv4 verify unicast source reachable-via 
命令功能 : 
解绑/绑定URPF到接口 
命令模式 : 
 10G以太接口模式,posgroup接口模式,pos子接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
posgroup接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,pos接口模式:15,千兆以太接口模式:15,以太接口模式:15,pos子接口模式:15 
命令格式 : 
ipv4 verify unicast source reachable-via 
  {rx 
 [acl-name 
 ＜acl-name 
＞]|any 
 [acl-name 
 ＜acl-name 
＞] [ignore-default-route 
]}
no ipv4 verify unicast source reachable-via 
命令参数解释 : 
参数|描述
---|---
rx|严格模式
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
any|松散模式
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
ignore-default-route|默认路由选项
缺省 : 
无 
使用说明 : 
绑定时接口必须存在。 
范例 : 
绑定URPF到接口smartgroup1：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#ipv4 verify unicast source reachable-via any acl-name myacl ignore-default-route查看配置结果信息：ZXROSNG(config-if-smartgroup1)#show running-config urpf!<URPF>interface smartgroup1  ipv4 verify unicast source reachable-via any acl-name myacl ignore-default-route$!</URPF>ZXROSNG(config-if-smartgroup1)#
相关命令 : 
无 
## ipv4 verify unicast source reachable-via 

ipv4 verify unicast source reachable-via 
命令功能 : 
解绑/绑定URPF到接口 
命令模式 : 
 dialer接口模式,multilink接口模式,serial接口模式,supervlan接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
serial接口模式:15,supervlan接口模式:15,multilink接口模式:15,通道化cpos_e1接口模式:15,dialer接口模式:15,通道化ce1接口模式:15 
命令格式 : 
ipv4 verify unicast source reachable-via 
  {rx 
 [acl-name 
 ＜acl-name 
＞]|any 
 [acl-name 
 ＜acl-name 
＞] [ignore-default-route 
]}
no ipv4 verify unicast source reachable-via 
命令参数解释 : 
参数|描述
---|---
rx|严格模式
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
any|松散模式
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
ignore-default-route|默认路由选项
缺省 : 
无 
使用说明 : 
绑定时接口必须存在。 
范例 : 
绑定URPF到接口smartgroup1：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#ipv4 verify unicast source reachable-via any acl-name myacl ignore-default-route查看配置结果信息：ZXROSNG(config-if-smartgroup1)#show running-config urpf!<URPF>interface smartgroup1  ipv4 verify unicast source reachable-via any acl-name myacl ignore-default-route$!</URPF>ZXROSNG(config-if-smartgroup1)#
相关命令 : 
无 
## ipv6 verify unicast source reachable-via 

ipv6 verify unicast source reachable-via 
命令功能 : 
解绑/绑定URPF到接口 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6 verify unicast source reachable-via 
  {rx 
 interface 
 ＜interface-name 
＞ [acl-name 
 ＜acl-name 
＞]|any 
 interface 
 ＜interface-name 
＞ [acl-name 
 ＜acl-name 
＞] [ignore-default-route 
]}
no ipv6 verify unicast source reachable-via 
 interface 
 ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
rx|严格模式
＜interface-name＞|绑定时接口必须存在。
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
any|松散模式
＜interface-name＞|绑定时接口必须存在。
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
ignore-default-route|默认路由选项
缺省 : 
无 
使用说明 : 
绑定时接口必须存在。 
范例 : 
绑定URPF到接口gei-0/1/0/1：ZXROSNG(config)#ipv6 verify unicast source reachable-via any interface gei-0/1/0/1 acl-name myacl ignore-default-route查看配置结果信息：ZXROSNG(config)#show running-config urpf!<URPF>interface gei-0/1/0/1  ipv6 verify unicast source reachable-via any acl-name myacl ignore-default-route$
相关命令 : 
无 
## ipv6 verify unicast source reachable-via 

ipv6 verify unicast source reachable-via 
命令功能 : 
解绑/绑定URPF到接口 
命令模式 : 
 10G以太接口模式,posgroup接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  
命令默认权限级别 : 
posgroup接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,pos接口模式:15,千兆以太接口模式:15,以太接口模式:15 
命令格式 : 
ipv6 verify unicast source reachable-via 
  {rx 
 [acl-name 
 ＜acl-name 
＞]|any 
 [acl-name 
 ＜acl-name 
＞] [ignore-default-route 
]}
no ipv6 verify unicast source reachable-via 
命令参数解释 : 
参数|描述
---|---
rx|严格模式
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
any|松散模式
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
ignore-default-route|默认路由选项
缺省 : 
无 
使用说明 : 
绑定时接口必须存在。 
范例 : 
绑定URPF到接口smartgroup1：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#ipv6 verify unicast source reachable-via any acl-name myacl ignore-default-route查看配置结果信息：ZXROSNG(config-if-smartgroup1)#show running-config urpf!<URPF>interface smartgroup1  ipv6 verify unicast source reachable-via any acl-name myacl ignore-default-route$!</URPF>ZXROSNG(config-if-smartgroup1)#
相关命令 : 
无 
## ipv6 verify unicast source reachable-via 

ipv6 verify unicast source reachable-via 
命令功能 : 
解绑/绑定URPF到接口 
命令模式 : 
 dialer接口模式,multilink接口模式,serial接口模式,supervlan接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  
命令默认权限级别 : 
multilink接口模式:15,dialer接口模式:15,通道化cpos_e1接口模式:15,serial接口模式:15,supervlan接口模式:15,通道化ce1接口模式:15 
命令格式 : 
ipv6 verify unicast source reachable-via 
  {rx 
 [acl-name 
 ＜acl-name 
＞]|any 
 [acl-name 
 ＜acl-name 
＞] [ignore-default-route 
]}
no ipv6 verify unicast source reachable-via 
命令参数解释 : 
参数|描述
---|---
rx|严格模式
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
any|松散模式
acl-name|关键字，acl名称
＜acl-name＞|acl名称，1-31个字符
ignore-default-route|默认路由选项
缺省 : 
无 
使用说明 : 
绑定时接口必须存在。 
范例 : 
绑定URPF到接口smartgroup1：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#ipv6 verify unicast source reachable-via any acl-name myacl ignore-default-route查看配置结果信息：ZXROSNG(config-if-smartgroup1)#show running-config urpf!<URPF>interface smartgroup1  ipv6 verify unicast source reachable-via any acl-name myacl ignore-default-route$!</URPF>ZXROSNG(config-if-smartgroup1)#
相关命令 : 
无 
# 镜像配置命令 
## default destination interface 

default destination interface 
命令功能 : 
向会话条目添加/删除默认目的端口。 
命令模式 : 
 端口镜像模式  
命令默认权限级别 : 
15 
命令格式 : 
default destination interface 
  ＜destination-interface 
＞ [{include-link-header 
|exclude-link-header 
}]
no default destination interface 
  ＜destination-interface 
＞
				
命令参数解释 : 
参数|描述
---|---
＜destination-interface＞|指定镜像的目的端口名
include-link-header|包含二层头
exclude-link-header|不包含二层头
缺省 : 
无 
使用说明 : 
只能配置1条。
范例 : 
1. 配置默认目的镜像端口：ZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#default destination interface gei-0/1/0/12. 删除配置：ZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#no default destination interface gei-0/1/0/1
相关命令 : 
show monitor session 
## default destination interface 

default destination interface 
命令功能 : 
向会话条目添加/删除默认目的端口。 
命令模式 : 
 端口镜像模式  
命令默认权限级别 : 
15 
命令格式 : 
default destination interface 
  ＜destination-interface 
＞
no default destination interface 
  ＜destination-interface 
＞
				
命令参数解释 : 
参数|描述
---|---
＜destination-interface＞|指定镜像的目的端口名
缺省 : 
无 
使用说明 : 
无
范例 : 
1. 配置默认目的镜像端口：ZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#default destination interface gei-0/1/0/12. 删除配置：ZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#no default destination interface gei-0/1/0/1
相关命令 : 
show monitor session 
## default destination vpws 

default destination vpws 
命令功能 : 
使用vpws作为镜像的目的 
命令模式 : 
 端口镜像模式  
命令默认权限级别 : 
15 
命令格式 : 
default destination vpws 
  ＜vpws-instance 
＞
no default destination vpws 
  ＜vpws-instance 
＞
				
命令参数解释 : 
参数|描述
---|---
＜vpws-instance＞|指定一个存在的VPWS实例为镜像的，1-32字符
缺省 : 
对源接口镜像，缺省镜像方向为both。 
使用说明 : 
默认镜像目的或者使用端口或者使用vpws，二者不能同时使用。 
范例 : 
1. 配置默认目的镜像为vpws：ZXROSNG(config)#vpws-for-monitor testZXROSNG(config-monitor-test)#exitZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#default destination vpws test2. 删除配置：ZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#no default destination vpws test
相关命令 : 
show monitor sessionvpws-for-monitor
## default destination vpws 

default destination vpws 
命令功能 : 
使用vpws作为镜像的目的 
命令模式 : 
 端口镜像模式  
命令默认权限级别 : 
15 
命令格式 : 
default destination vpws 
  ＜vpws-instance 
＞ [{include-link-header 
|exclude-link-header 
}]
no default destination vpws 
  ＜vpws-instance 
＞
				
命令参数解释 : 
参数|描述
---|---
＜vpws-instance＞|指定一个存在的VPWS实例为镜像的，1-32字符
include-link-header|包含二层头
exclude-link-header|不包含二层头
缺省 : 
对源接口镜像，缺省镜像方向为both。 
使用说明 : 
默认镜像目的或者使用端口或者使用vpws，二者不能同时使用。 
范例 : 
1. 配置默认目的镜像为vpws：ZXROSNG(config)#vpws-for-monitor testZXROSNG(config-monitor-test)#exitZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#default destination vpws test2. 删除配置：ZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#no default destination vpws test
相关命令 : 
show monitor sessionvpws-for-monitor
## monitor apply session &amp;lt;mid&amp;gt; source 

monitor apply session <mid> source 
命令功能 : 
将指定会话绑定/解绑到源接口。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
monitor apply session  
 ＜session-id 
＞ source 
  {interface 
 ＜source-interface 
＞ [direction 
 {both 
|rx 
|tx 
}]|vpws 
 ＜vpws-instance 
＞ direction 
 rx 
}
no monitor apply session  
 ＜session-id 
＞ source 
  {interface 
 ＜source-interface 
＞ [direction 
 {both 
|rx 
|tx 
}]|vpws 
 ＜vpws-instance 
＞ direction 
 rx 
}
				
命令参数解释 : 
参数|描述
---|---
＜session-id＞|会话号，范围1~$#35717121#$
interface|指定镜像源为端口
＜source-interface＞|指定源端口名
both|绑定端口镜像的方向为入向和出向
rx|绑定端口镜像的方向为入向
tx|绑定端口镜像的方向为出向
vpws|指定镜像源为vpws
＜vpws-instance＞|指定一个存在的VPWS实例为镜像的，1-32字符
rx|绑定端口镜像的方向为入向
缺省 : 
对源端口镜像，缺省镜像方向为both。 
使用说明 : 
无
范例 : 
1. 将指定会话绑定镜像源端口：ZXROSNG(config)#monitor apply session 1 source interface gei-0/1/0/22. 解绑镜像源端口：ZXROSNG(config)#no monitor apply session 1 source interface gei-0/1/0/23.使用vpws做远端镜像：ZXROSNG(config)#vpws-for-monitor testZXROSNG(config-monitor-test)#exitZXROSNG(config)#monitor apply session 1 source vpws test direction rx4. 解绑对vpws的镜像：ZXROSNG(config)#no monitor apply session 1 source vpws test direction rx
相关命令 : 
show monitor session 
## monitor rate-limit 

monitor rate-limit 
命令功能 : 
镜像限速配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
monitor rate-limit 
  ＜BoardName 
＞ cir 
 ＜cir 
＞ cbs 
 ＜cbs 
＞ [pir 
 ＜pir 
＞ pbs 
 ＜pbs 
＞]
no monitor rate-limit 
  ＜BoardName 
＞
				
命令参数解释 : 
参数|描述
---|---
＜BoardName＞|子卡名称
＜cir＞|CIR值，范围1～30000(Mbps)
＜cbs＞|CBS值，范围1～16(MB)
＜pir＞|PIR值，范围1～30000(Mbps)
＜pbs＞|PBS值，范围1～16(MB)
缺省 : 
无 
使用说明 : 
此命令只支持对线卡PFU进行配置，并且目前配置单板类型中槽位号是有效的。 
范例 : 
1. 镜像限速配置：ZXROSNG(config)#monitor rate-limit PIU-0/1/1 cir 100 cbs 10 pir 100 pbs 5 2. 删除配置：ZXROSNG(config)#no monitor rate-limit PIU-0/1/1
相关命令 : 
show monitor ratelimit 
## monitor session 

monitor session 
命令功能 : 
添加或删除一个端口镜像会话。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
monitor session 
  ＜session-id 
＞
no monitor session 
  ＜session-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜session-id＞|会话号，配置范围<1-$#35717121#$>
缺省 : 
无 
使用说明 : 
创建端口镜像会话。使用no命令删除端口镜像会话。
范例 : 
1. 创建端口镜像会话1：ZXROSNG(config)#monitor session 1ZXROSNG(config-monitor-session)#2. 删除端口镜像会话1：ZXROSNG(config)#no monitor session 1
相关命令 : 
show monitor session 
## rule 

rule 
命令功能 : 
向会话条目添加/删除带ACL的目的端口。 
命令模式 : 
 端口镜像模式  
命令默认权限级别 : 
15 
命令格式 : 
rule 
  {ipv4-access-list 
|ipv6-access-list 
} ＜aclname 
＞ destination 
 {interface 
 ＜destination-interface 
＞|vpws 
 ＜vpws-instance 
＞}
no rule 
  {ipv4-access-list 
|ipv6-access-list 
} ＜aclname 
＞ destination 
 {interface 
 ＜destination-interface 
＞|vpws 
 ＜vpws-instance 
＞}
				
命令参数解释 : 
参数|描述
---|---
ipv4-access-list|指定为IPv4_ACL类型
ipv6-access-list|指定为IPv6_ACL类型
＜aclname＞|ACL名字，1-31个字符
interface|目的的类型为接口类型
＜destination-interface＞|指定镜像的目的端口名
vpws|目的的类型为VPWS类型
＜vpws-instance＞|指定一个存在的VPWS实例为镜像的目的端
缺省 : 
无 
使用说明 : 
无
范例 : 
1. 向会话添加IPv4 ACL名为aaa，镜像目的端口为gei-0/1/0/1的条目：ZXROSNG(config-monitor-session)#rule ipv4-access-list aaa destination interface gei-0/1/0/12. 删除IPv4 ACL名为aaa，镜像目的端口为gei-0/1/0/1的条目：ZXROSNG(config-monitor-session)#no rule ipv4-access-list aaa destination interface gei-0/1/0/1
相关命令 : 
show monitor session 
## show monitor ratelimit 

show monitor ratelimit 
命令功能 : 
显示镜像限速的配置内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show monitor ratelimit 
  [＜shelf 
＞ ＜slot 
＞ ＜subCard 
＞] 
命令参数解释 : 
参数|描述
---|---
＜shelf＞|机架号，范围0~79
＜slot＞|槽位号，范围0~$#35717129#$
＜subCard＞|子卡号，范围0~3
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示限速条目的内容：ZXROSNG(config)#show monitor ratelimit -------------------------------------------------   Shelf: 0  Slot: 1  SubCard: 0             Cir(Mbps): 10000           Cbs(MB): 16     Pir(Mbps): 10000           Pbs(MB): 16-------------------------------------------------   Shelf: 0  Slot: 1  SubCard: 1             Cir(Mbps): 10000           Cbs(MB): 16     Pir(Mbps): 10000           Pbs(MB): 16ZXROSNG(config)#show monitor ratelimit 0 1 0-------------------------------------------------  Shelf: 0  Slot: 1  SubCard: 0            Cir(Mbps): 10000           Cbs(MB): 16     Pir(Mbps): 10000           Pbs(MB): 16  
相关命令 : 
无 
## show monitor session 

show monitor session 
命令功能 : 
显示会话条目的内容。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show monitor session 
  {＜session-id 
＞|all 
} 
命令参数解释 : 
参数|描述
---|---
＜session-id＞|显示指定会话，会话号1-$#35717121#$
all|显示所有会话
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-monitor-session)#show monitor session 1Session 1------------Destination Port: gei-0/1/0/2               Destination Type:interface    Port Status:inactive    IPV4 ACL name:testDefault Destination Port: gei-0/1/0/1            Destination Type:interface    Port Status:inactive
相关命令 : 
无 
# 控制平面安全配置命令 
## apply flow limit 

apply flow limit 
命令功能 : 
该命令工作于CPS接口模式下，用于绑定flowtype流类型的限速模板到指定物理接口对应物理接口下模板内配置的flowtype流类型进行相应的限速操作。当需要修改多个flowtype流类型的限速值时，使用该命令绑定指定模板到对应的接口，成功后相应接口下的对应flowtype流类型限速按照模板配置的值生效。 
命令模式 : 
 CPS接口模式  
命令默认权限级别 : 
15 
命令格式 : 
apply flow limit 
 profile 
 ＜profile-name 
＞
no apply flow limit 
命令参数解释 : 
参数|描述
---|---
＜profile-name＞|flowtype限速的模板名，范围：1-16
缺省 : 
无 
使用说明 : 
1、配置后对物理接口绑定模板；2、当模板配置发生改变后，直接生效于应用的所有接口；3、模板命令与接口下的命令同时配置时，优先级小于接口下的命令
范例 : 
配置端口应用接口flowtype模板ZXROSNG#show running-config cps!<cps>control-plane-security    flow limit profile 5     flow limit flowtype gvrp rate-limit 4 quota-limit 41     flow limit flowtype dhcp rate-limit 3 quota-limit 31     flow limit flowtype gre rate-limit 2 quota-limit 21     flow limit flowtype nd rate-limit 1 quota-limit 11   $$!</cps>ZXROSNG(config-cps-if-fei-0/1/0/5)#apply flow limit profile 5
相关命令 : 
flow limit profile 
## clear cps ctm statistics 

clear cps ctm statistics 
命令功能 : 
该命令用于清除CTM队列统计计数信息。当需要清除CTM队列统计数据时执行该命令。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
clear cps ctm statistics 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
清除CTM队列计数 
范例 : 
清除CTM的统计信息ZXROSNG(config-cps)# clear cps ctm statistics
相关命令 : 
无 
## clear cps flow statistics 

clear cps flow statistics 
命令功能 : 
该命令工作于CPS模式下，用于清除各flowtype流类型的上送控制面流量以及丢包计数。当需要清除计数信息时使用该命令，成功后，所有flowtype流类型的全部计数信息清零。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
clear cps flow statistics 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
清除上送控制面所有flowtype流的收/发统计计数。 
范例 : 
清除flowtype的上送/下发统计信息ZXROSNG(config-cps)#clear cps flow statistics
相关命令 : 
show cps flow statistics 
## clear cps gtsm statistics 

clear cps gtsm statistics 
命令功能 : 
该命令工作于CPS模式下，用于清除GTSM收包、丢包统计计数信息。当需要清除GTSM统计计数信息时，使用该命令，成功后，所有GTSM统计计数信息清零。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
clear cps gtsm statistics 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
清除GTSM统计计数。 
范例 : 
清除GTSM的统计信息ZXROSNG(config-cps)# clear cps gtsm statistics
相关命令 : 
show cps gtsm statistics 
## control-plane-security 

control-plane-security 
命令功能 : 
该命令工作于全局配置模式下，用于进入控制面安全命令配置模式。当需要进行控制面安全配置时，输入该命令，成功后，进入CPS配置模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
control-plane-security 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#control-plane-security ZXROSNG(config-cps)#
相关命令 : 
无 
## cps-log 

cps-log 
命令功能 : 
该命令工作于全局配置模式下，用于配置日志功能的开关。当需要打开或关闭控制面安全的日志记录功能时，使用该命令，成功后，可以打开或关闭日志功能。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
cps-log 
  {on 
|off 
}
命令参数解释 : 
参数|描述
---|---
on|打开
off|关闭
缺省 : 
缺省关闭该功能 
使用说明 : 
无 
范例 : 
打开CPS日志功能：ZXR10<config-cps>#cps-log on
相关命令 : 
无 
## ctm queue-limit 

ctm queue-limit 
命令功能 : 
该命令工作于CPS模式下，用于配置某个上送队列的报文上送目的CPU的队列深度值，深度值越大，表示缓存越大。当需要指定某个队列到目的CPU的队列深度值时，使用该命令，配置成功后，该队列到目的CPU的深度值按配置生效。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
ctm queue-limit 
  {high 
|middle 
|normal 
|low 
} destcpu 
 {r-cpu 
|l-cpu 
} priority-queue 
 {＜up-priority 
＞|＜down-priority 
＞} interface 
 ＜interface-list 
＞
no ctm queue-limit 
 destcpu 
 {r-cpu 
|l-cpu 
} priority-queue 
 {＜up-priority 
＞|＜down-priority 
＞} interface 
 ＜interface-list 
＞
				
命令参数解释 : 
参数|描述
---|---
high|队列深度值：high   :  4M bytesmiddle :  1M bytesnormal :  512K byteslow   :  128K bytes
middle|队列深度值：high   :  4M bytesmiddle :  1M bytesnormal :  512K byteslow   :  128K bytes
normal|队列深度值：high   :  4M bytesmiddle :  1M bytesnormal :  512K byteslow   :  128K bytes
low|队列深度值：high   :  4M bytesmiddle :  1M bytesnormal :  512K byteslow   :  128K bytes
r-cpu|主控CPU
l-cpu|线卡CPU
＜up-priority＞|队列号，也就是优先级，up<0-7>, down<16-19>
＜down-priority＞|队列号，也就是优先级，up<0-7>, down<16-19>
＜interface-list＞|队列深度作用的物理接口名称
缺省 : 
无 
使用说明 : 
需指定目的CPU，队列号，接口名列表high|middle|normal|low为配置内容
范例 : 
在安全配置模式下，设置作用于接口fei-0/1/0/5，到cpu 为MPU-0/20/0的队列2的队列深度为high级别：ZXROSNG(config-cps)#ctm queue-limit high destcpu r-cpu priority-queue 2 interface fei-0/1/0/5
相关命令 : 
show cps ctm-queue 
## ctm rate-limit 

ctm rate-limit 
命令功能 : 
该命令工作于CPS模式下，用于配置报文从源单板到目的CPU的限速值。当需要修改以CPU为粒度的限速配置时，使用该命令，成功后，按照配置值生效。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
ctm rate-limit 
 destcpu 
 {r-cpu 
|l-cpu 
} board 
 ＜board-name 
＞ {up-ctm 
 cir 
 ＜cir 
＞ cbs 
 ＜cbs 
＞ eir 
 ＜eir 
＞|down-ctm 
 cir 
 ＜cir 
＞ cbs 
 ＜cbs 
＞ eir 
 ＜eir 
＞}
no ctm rate-limit 
 destcpu 
 {r-cpu 
|l-cpu 
} board 
 ＜board-name 
＞ {up-ctm 
|down-ctm 
}
				
命令参数解释 : 
参数|描述
---|---
r-cpu|主控CPU
l-cpu|线卡CPU
＜board-name＞|board名称-机框号/槽位号，指定上送报文的源单板
up-ctm|区分上下行 up-ctm 上行，down-ctm 下行
＜cir＞|约定信息速率，范围up-ctm (0-600,000), down-ctm ( 0~ 2,000,000)， 单位kbps
＜cbs＞|约定突发尺寸， 范围0~256，  单位KByte
＜eir＞|额外信息速率，范围up-ctm (0-200,000) down-ctm ( 0~ 2,000,000)， 单位kbps
down-ctm|区分上下行 up-ctm 上行，down-ctm 下行
＜cir＞|约定信息速率，范围up-ctm (0-600,000), down-ctm ( 0~ 2,000,000)， 单位kbps
＜cbs＞|约定突发尺寸， 范围0~256，  单位KByte
＜eir＞|额外信息速率，范围up-ctm (0-200,000) down-ctm ( 0~ 2,000,000)， 单位kbps
缺省 : 
ZXROSNG(config-cps)#show cps ctm-rate destcpu {<l-cpu>|<r-cpu>} board <name>-<shelf>/<slot>显示默认值
使用说明 : 
需要指定目的CPU及源板信息，区分上行和下行cir、eir、cbs为配置内容
范例 : 
配置从PFU-0/1单板上送到目的CPU(PFU-0/1/0)的上行限速值cir 100，cbs 100，eir 100,下行限速值cir 100，cbs 100，eir 100ZXROSNG(config-cps)#ctm rate-limit destcpu l-cpu board PFU-0/1 up-ctm cir 100 cbs 100 eir 100ZXROSNG(config-cps)#ctm rate-limit destcpu l-cpu board PFU-0/1 down-ctm cir 100 cbs 100 eir 100
相关命令 : 
show cps ctm-rate  
## flow back-press flowtype 

flow back-press flowtype 
命令功能 : 
该命令工作在CPS接口模式下，用于将用户期望的反压策略与物理接口的flowtype进行绑定。当需要对指定接口下指定flowtype流类型进行反压操作时，使用该命令，成功后，对应接口下指定flowtype流类型会根据统计值和告警值的比较关系，按照配置的反压策略进行限速。 
命令模式 : 
 CPS接口模式  
命令默认权限级别 : 
15 
命令格式 : 
flow back-press flowtype 
  ＜flowtype-name 
＞ profile 
 ＜profile-name 
＞
no flow back-press flowtype 
  ＜flowtype-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜flowtype-name＞|与反应策略进行绑定流类型
＜profile-name＞|与流类型绑定的反压策略模板
缺省 : 
无 
使用说明 : 
1、可以通过该命令有效配置指定flowtype应用反压策略。2、使用no命令取消特定流的反压策略。3、反压策略模板必须已经存在。
范例 : 
在CPS接口配置模式下，将用户期望的反压策略2与物理接口fei-0/1/0/5的流类型nd进行绑定：ZXROSNG(config-cps-if-fei-0/1/0/5)# flow back-press flowtype nd profile 2
相关命令 : 
flow back-press profile 
## flow back-press 

flow back-press 
命令功能 : 
该命令工作在CPS模式下，用于配置用户期望的反压策略模板。反压策略就是当flowtype上送速率超过某一个阈值时，根据配置的反压策略对flowtype限速进行进一步的上送流量控制，以保护控制面安全。当需要进行反压模板配置时，使用该命令，成功后，生成反压模板号，并进入反压策略模板配置模式。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
flow back-press 
 profile 
 ＜profile-name 
＞
no flow back-press 
 profile 
 ＜profile-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜profile-name＞|反压策略模板 <1-16>
缺省 : 
无 
使用说明 : 
允许配置16个策略模板，范围为1-16 
范例 : 
在安全配置模式下，进入配置反压策略模板2：ZXROSNG(config-cps)#flow back-press profile 2ZXROSNG(config-cps-back-press-profile-2)#
相关命令 : 
show cps flow limit profile 
## flow limit 

flow limit 
命令功能 : 
该命令工作在CPS模式下，用于配置flowtype流类型的限速模板。限速模板是通过绑定对应模板到指定接口，避免同一种或相同多个flowtype在多个接口下重复配置限速，达到快速配置多个flowtype流类型在指定接口下的限速。当需要配置指定flowtype流类型的限速值及配额值时，使用该命令，成功后，会产生相应的限速模板，进一步的可以到指定接口下进行绑定操作。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
flow limit 
 profile 
 ＜profile-name 
＞
no flow limit 
 profile 
 ＜profile-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜profile-name＞|flowtype限速的模板名，范围：1-16
缺省 : 
无 
使用说明 : 
1、配置后进入端口flow限速的模板配置模式2、如果模板被绑定，则不允许删除模板
范例 : 
生成flow限速模板：ZXROSNG(config-cps)#flow limit profile 10ZXROSNG(config-cps-flow-limit-profile-10)#
相关命令 : 
show cps flow limit profile 
## flow limit 

flow limit 
命令功能 : 
该命令工作在CPS-flow限速策略模式下，用于配置控指定flowtype上送报文的上送速率与配额。一般上送速率与配额值一致，规定配额值>=速率值，当上送速率超过配额值时，产生告警。 
命令模式 : 
 CPS-flow限速策略模式  
命令默认权限级别 : 
15 
命令格式 : 
flow limit 
 flowtype 
 ＜flowtype-name 
＞ rate-limit 
 ＜rate-limit-value 
＞ quota-limit 
 ＜quota-limit-value 
＞
no flow limit 
 flowtype 
 ＜flowtype-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜flowtype-name＞|指定的flowtype类型名
＜rate-limit-value＞|指定flowtype上送速率。单位：pps，取值0-$#67240228#$；可配置的最大值由性能参数控制，性能参数定制范围为85000-4294967295，默认为85000
＜quota-limit-value＞|指定flowtype接收配额。单位：pps，取值0-$#67240228#$；可配置的最大值由性能参数控制，性能参数定制范围为85000-4294967295，默认为85000
缺省 : 
无 
使用说明 : 
1、可以通过该命令有效配置指定flowtype在某个接口的上送速率，如果设置为0，则该接口禁止此   flowytpe流量的上送。2、使用no命令删除模板配置。3、可修改flow limit模板配置，同步到绑定该模板接口的rate limit 和quota limit的值。其优先级小于手动配置的值
范例 : 
配置模板上指定flowtype的上送速率ZXROSNG(config-cps)#flow limit profile 10ZXROSNG(config-cps-flow-limit-profile-10)# flow limit flowtype nd rate-limit 100 quota-limit 100ZXROSNG(config-cps-flow-limit-profile-10)# flow limit flowtype gre rate-limit 2 quota-limit 21ZXROSNG(config-cps-flow-limit-profile-10)# flow limit flowtype dhcp rate-limit 3 quota-limit 31 ZXROSNG(config-cps-flow-limit-profile-10)# flow limit flowtype gvrp rate-limit 4 quota-limit 41
相关命令 : 
show cps flow limit profile 
## flow limit 

flow limit 
命令功能 : 
该命令工作在CPS接口模式下，用于配置物理接口指定flowtype的上送速率与上送配额。上送速率控制flowtype流类型的上送速度，速率超过配额值时会产生告警。当需要单独指定某个接口下的某种flowtype流类型的上送速率和配额值时，使用该命令，成功后，该接口下的这种flowtype流类型按照配置值生效。 
命令模式 : 
 CPS接口模式  
命令默认权限级别 : 
15 
命令格式 : 
flow limit 
 flowtype 
 ＜flowtype-name 
＞ rate-limit 
 ＜rate-limit-value 
＞ quota-limit 
 ＜quota-limit-value 
＞
no flow limit 
 flowtype 
 ＜flowtype-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜flowtype-name＞|指定进行限速的flowtype流类型名
＜rate-limit-value＞|指定flowtype上送速率。单位：pps，取值0-$#67240228#$；配置的最大值由性能参数控制，性能参数定制范围为85000-4294967295，默认为85000
＜quota-limit-value＞|指定flowtype接收配额。单位：pps，取值0-$#67240228#$；可配置的最大值由性能参数控制，性能参数定制范围为85000-4294967295，默认为85000
缺省 : 
缺省情况下，每物理接口不同的flowtype的上送速率与允许的配额不相同，在没有修改配置的情况下，可以通过show cps flow limit命令显示每种flowtype的缺省值。 
使用说明 : 
1、可以通过该命令有效配置指定flowtype在某个接口的上送速率，如果设置为0，则该接口禁止此   flowytpe流量的上送。2、使用no命令恢复缺省值的配置。3、优先级高于模板配置，但是在线卡上，优先级小于反压产生的rate limit
范例 : 
配置接口上指定flowtype的上送速率ZXROSNG(config-cps)#interface fei-0/1/0/5ZXROSNG(config-cps-if-fei-0/1/0/5)# flow limit flowtype nd rate-limit 100 quota-limit 100ZXROSNG(config-cps-if-fei-0/1/0/5)# flow limit flowtype gre rate-limit 2 quota-limit 21ZXROSNG(config-cps-if-fei-0/1/0/5)# flow limit flowtype dhcp rate-limit 3 quota-limit 31 ZXROSNG(config-cps-if-fei-0/1/0/5)# flow limit flowtype gvrp rate-limit 4 quota-limit 41
相关命令 : 
show cps flow limit 
## flow statistics-interval 

flow statistics-interval 
命令功能 : 
该命令工作在CPS模式下，用于配置流类型统计时间间隔。当需要指定统计间隔时，使用该命令，成功后，统计周期按照配置的值生效。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
flow statistics-interval 
  {＜halt-flow-statistic 
＞|＜set-interval 
＞}
no flow statistics-interval 
命令参数解释 : 
参数|描述
---|---
＜halt-flow-statistic＞|停止统计，值为：0
＜set-interval＞|设置统计时间间隔，取值范围：5-120，单位：s
缺省 : 
缺省时间为10s 
使用说明 : 
如果需要停止统计，需要将时间间隔设为0，否则应该5-120之间取值，默认间隔为10s 
范例 : 
ZXROSNG(config-cps)#flow statistics-interval ?  0        Halt flow statistics  <5-120>  Set flow statistics interval(s)配置时间间隔为5s：ZXROSNG(config-cps)#flow statistics-interval 5ZXROSNG(config-cps)#
相关命令 : 
无 
## management-service 

management-service 
命令功能 : 
该命令工作在CPS模式下，用于配置业务口管理协议收包的上送/丢包策略。当需要对业务口下的某种管理协议进行协议过滤时，使用该命令，成功后，按照配置过滤规则生效。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
management-service 
  {deny 
|permit 
} ＜management-service-type-name 
＞ [interface 
 ＜interface-name 
＞]
no management-service 
  ＜management-service-type-name 
＞ [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
deny|配置是否允许指定接口的协议类型，deny：拒绝 permit：允许
permit|配置是否允许指定接口的协议类型，deny：拒绝 permit：允许
＜management-service-type-name＞|ftp、Telnet、ssh、snmp、http、ping、tftp
＜interface-name＞|指定的接口名
缺省 : 
缺省各业务口的管理协议均是permit 
使用说明 : 
1、当参数interface不设置时，配置对全局接口生效2、配置对设备作为服务端与客户端同时生效
范例 : 
1、接口管理协议的接收策略带接口配置ZXROSNG(config-cps)# management-service deny telnet  interface gei-0/1/0/12、接口管理协议的接收策略不带接口配置：ZXROSNG(config-cps)# management-service deny telnet 
相关命令 : 
show cps management-service 
## mng-access ip-forwarding 

mng-access ip-forwarding 
命令功能 : 
配置管理口是否转发IP报文 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
mng-access ip-forwarding 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|是能管理口转发IP报文
disable|去使能管理口转发IP报文
缺省 : 
管理口转发报文 $#67240265:0/不转发;1/可以转发#$ 
使用说明 : 
使用场景： 管理口如果支持报文转发，在特殊组网的情况下，可能会导致一些安全漏洞。为了避免出现这种情况，可以通过命令配置关闭管理口的IP报文转发能力，报文直接丢弃。
范例 : 
使能管理口的IP报文转发ZXROSNG(config)#control-plane-security ZXROSNG(config-cps)#mng-access ip-forward enable
相关命令 : 
control-plane-security 
## mng-access peer-ip 

mng-access peer-ip 
命令功能 : 
该命令工作在CPS模式下，用于配置管理口收包时对报文源IP安全过滤（收包/丢包）策略。当需要针对管理口的某个远端IP地址进行过滤时，使用该命令，成功后，按照配置的过滤规则生效。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
mng-access peer-ip 
  {deny 
|permit 
} {any 
|＜ip-address 
＞ ＜ip-address-mask 
＞}
no mng-access peer-ip 
  {any 
|＜ip-address 
＞ ＜ip-address-mask 
＞}
				
命令参数解释 : 
参数|描述
---|---
deny|禁止接入
permit|允许接入
any|所有IP地址
＜ip-address＞|远端IP地址
＜ip-address-mask＞|远端IP地址掩码
缺省 : 
系统默认不对管理口收包的源IP进行过滤 
使用说明 : 
1、若配置any参数，则对所有源IP生效。2、若指定<ip-address>与指定any同时配置，则以细粒度的<ip-address>配置优先。3、管理口配置时同时指定了peer ip地址过滤，peer mac地址过滤，以及protocol过滤时，系统匹配的顺序为：首先匹配peer mac地址规则，再匹配peer ip地址规则，最后匹配protocol。
范例 : 
配置管理口的安全策略：允许接入报文的源IP为20.1.1.0/24,其它源IP过来的报文均丢弃。ZXROSNG(config-cps)#mng-access peer-ip permit 20.1.1.0 255.255.255.0ZXROSNG(config-cps)#mng-access peer-ip deny any
相关命令 : 
mng-access peer-macmng-access protocol show cps mng-access
## mng-access peer-ipv6 

mng-access peer-ipv6 
命令功能 : 
该命令工作在CPS模式下，用于配置管理口收包时对报文源IPv6地址安全过滤（收包/丢包）策略。当需要管理口针对某个指定的远端v6地址进行过滤时，使用该命令，成功后，按照配置的过滤规则生效。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
mng-access peer-ipv6 
  {deny 
|permit 
} {any 
|＜ipv6-address-mask 
＞}
no mng-access peer-ipv6 
  {any 
|＜ipv6-address-mask 
＞}
				
命令参数解释 : 
参数|描述
---|---
deny|禁止接入
permit|允许接入
any|所有IPv6地址
＜ipv6-address-mask＞|远端IPv6地址前缀
缺省 : 
系统默认不对管理口收包的源IPv6地址进行过滤 
使用说明 : 
1、若配置any参数，则对所有源IPv6地址生效。2、若指定<ipv6-address-mask>与指定any同时配置，则以细粒度的<ipv6-address-mask>配置优先。3、管理口配置时同时指定了peer ipv6地址过滤，peer mac地址过滤，以及protocol过滤时，系统匹配的顺序为：首先匹配peer mac地址规则，再匹配peer ipv6地址规则，最后匹配protocol。
范例 : 
配置管理口的安全策略：允许接入报文的源IPv6地址前缀为10::1/128,其它源IPv6过来的报文均丢弃。ZXROSNG(config-cps)#mng-access peer-ipv6 deny anyZXROSNG(config-cps)#mng-access peer-ipv6 permit 10::1/128
相关命令 : 
mng-access peer-macmng-access protocol show cps mng-access
## mng-access peer-mac 

mng-access peer-mac 
命令功能 : 
该命令工作在CPS模式下，用于配置管理口收包时对报文源MAC安全过滤（收包/丢包）策略。当需要管理口针对某个指定MAC地址进行过滤时，使用该命令，成功后，按照配置的过滤规则生效。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
mng-access peer-mac 
  {deny 
|permit 
} {any 
|＜mac-address 
＞}
no mng-access peer-mac 
  {any 
|＜mac-address 
＞}
				
命令参数解释 : 
参数|描述
---|---
deny|禁止接入
permit|允许接入
any|所有MAC地址
＜mac-address＞|描述远端接入的MAC地址
缺省 : 
系统默认不对管理口收包的源MAC进行过滤 
使用说明 : 
1、若配置any参数，则对所有源MAC生效；2、若指定<mac-address>与指定any同时配置，则以细粒度的<mac-address>配置优先。3、管理口配置时同时指定了peer ip地址过滤，peer mac地址过滤，以及protocol过滤时，系统匹配的顺序为：首先匹配peer mac地址规则，再匹配peer ip地址规则，最后匹配protocol
范例 : 
配置管理口的安全策略：允许接入报文的源MAC为00d0.d0c0.d111,其它源MAC过来的报文均丢弃。ZXROSNG(config-cps)#mng-access peer-mac permit 00d0.d0c0.d111ZXROSNG(config-cps)#mng-access peer-mac deny any
相关命令 : 
mng-access peer-ipmng-access protocol show cps mng-access
## mng-access port 

mng-access port 
命令功能 : 
配置管理口收包时对报文接入端口过滤策略配置 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
mng-access port 
  {deny 
|permit 
} {tcp 
|udp 
} {local 
|remote 
} ＜port 
＞
no mng-access port 
  {tcp 
|udp 
} {local 
|remote 
} ＜port 
＞
				
命令参数解释 : 
参数|描述
---|---
deny|禁止接入
permit|允许接入
tcp|TCP协议TCP协议
udp|UDP协议UDP协议
local|本端端口号本端端口号
remote|远端端口号远端端口号
＜port＞|端口号，取值1-65535端口号，取值1-65535
缺省 : 
系统默认不对管理口收包的端口进行过滤。 
使用说明 : 
管理口配置时同时指定了peer ip地址过滤，peer mac地址过滤，port过滤以及protocol过滤时，系统匹配的顺序为：首先匹配peer mac地址规则，再匹配peer ip地址规则，再匹配port端口规则，最后匹配protocol 。 
范例 : 
1. 配置管理口的安全策略：ZXROSNG(config-cps)# mng-access port permit tcp 2323ZXROSNG(config-cps)# mng-access port permit udp 5059
相关命令 : 
show cps mng-access 
## mng-access protocol 

mng-access protocol 
命令功能 : 
该命令工作在CPS模式下，用于配置管理口收包时对报文接入协议过滤策略（收包/丢包）配置。当需要管理口针对某种协议进行过滤配置时，使用该命令，成功后，按照配置的过滤规则生效。 
命令模式 : 
 CPS模式  
命令默认权限级别 : 
15 
命令格式 : 
mng-access protocol 
  {deny 
|permit 
 [rate-limit 
 ＜rate-limit-value 
＞]} ＜mng-access-protocol-name 
＞
no mng-access protocol 
  ＜mng-access-protocol-name 
＞
				
命令参数解释 : 
参数|描述
---|---
deny|禁止接入
permit|允许接入
＜rate-limit-value＞|指定协议上送速率。单位：pps，取值1-5000
＜mng-access-protocol-name＞|描述管理口接入的协议
缺省 : 
系统默认允许通过的协议包括：arp/icmp/ftp/radius/snmp/ssh/tacacs plus/telnet/tftp/dhcp这些协议均是指IPv4协议，缺省其它协议均不允许接入 
使用说明 : 
1、若配置any参数，特指所有应用协议。2、若配置any与指定协议配置同时出现，则优先匹配细粒度指定协议的配置。3、管理口配置时同时指定了peer ip地址过滤，peer mac地址过滤，以及protocol过滤时，系统匹配的顺序为：首先匹配peer mac地址规则，再匹配peer ip地址规则，最后匹配protocol 。4、为了提高限速效率，报文在限速值附近，限速效果会存在误差。
范例 : 
配置管理口的安全策略：只允许接入ARP,ICMP协议，其它全部丢弃。ZXROSNG(config-cps)# mng-access protocol permit arpZXROSNG(config-cps)# mng-access protocol permit rate-limit 10 icmpZXROSNG(config-cps)# mng-access protocol deny any
相关命令 : 
mng-access peer-ipmng-access peer-macshow cps mng-access
## overshot 

overshot 
命令功能 : 
该命令工作在CPS反压策略模式下，用于配置反压策略模板的反压策略信息，即超过配额值多少比例时，需要降低限速值多少比例。当需要配置相应的反压策略时，使用该命令，成功后，生成对应的反压策略模板，进一步可以绑定到指定接口下的指定flowtype流类型上实施反压操作。 
命令模式 : 
 CPS反压策略模式  
命令默认权限级别 : 
15 
命令格式 : 
overshot 
  ＜ucovershot 
＞ {restore 
|decline 
 ＜ucdeclineto 
＞|suspend 
}
no overshot 
  ＜ucovershot 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ucovershot＞|超过配额的百分比，单位 %
restore|恢复原速率，  即decline 0
＜ucdeclineto＞|反压当前速率的百分比，单位 %
suspend|抑制上送速率，即decline 100
缺省 : 
无 
使用说明 : 
1、一个策略模板下允许配置的条目是可控范围的。2、配置要符合逻辑性，即超过的配额值越大抑制应该越大
范例 : 
反压策略配置模式下，配置反压策略模板15的反压策略信息为：1、超过配额值20% ，反压原速率10%ZXROSNG(config-cps)#flow back-press profile 15ZXROSNG(config-cps-back-press-profile-15)#overshot 20 decline 102、超过配额值50% ，反压原速率50%ZXROSNG(config-cps)#flow back-press profile 15ZXROSNG(config-cps-back-press-profile-15)#overshot 50 decline 503、超过配额值80% ，反压原速率100%ZXROSNG(config-cps)#flow back-press profile 15ZXROSNG(config-cps-back-press-profile-15)#overshot 80 decline 100
相关命令 : 
无 
## show cps ctm-queue statistics 

show cps ctm-queue statistics 
命令功能 : 
该命令用于显示CTM队列统计信息，包括上送和丢包计数。当需要显示某接口下CTM队列统计计数信息时，使用该命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps ctm-queue statistics 
 destcpu 
 ＜cpu-name 
＞ interface 
 ＜interface-name 
＞ [priority-queue 
 {＜up-priority-queue 
＞|＜dow-priority-queue 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜cpu-name＞|CPU名称
＜interface-name＞|接口名
＜up-priority-queue＞|上送队列队列号，也就是优先级，范围：0-7
＜dow-priority-queue＞|下行队列队列号，也就是优先级，范围：16-19
缺省 : 
无 
使用说明 : 
priority-queue为可选参数，当不指定时，显示所有队列的统计数据。 
范例 : 
显示队列0的丢包上送统计数据：ZXROSNG(config-cps)#show cps ctm-queue statistics destcpu PFU-0/1/0 interface gei-0/1/0/1 priority-queue 0Cpu          Interface      Priority      Upsend packet      Drop packet PFU-0/1/0   gei-0/1/0/1    0              12345                54321
相关命令 : 
无 
## show cps ctm-queue 

show cps ctm-queue 
命令功能 : 
该命令用于显示指定报文目的CPU的某个上送队列的深度值。当需要显示对应接口上送目的CPU的某个队列的深度值时，使用该命令，当没有配置时，显示默认配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps ctm-queue 
 destcpu 
 {r-cpu 
|l-cpu 
} priority-queue 
 {＜up-priority 
＞|＜down-priority 
＞} interface 
 ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
r-cpu|主控CPU
l-cpu|线卡CPU
＜up-priority＞|上送队列队列号，也就是优先级，范围：0-7
＜down-priority＞|下行队列队列号，也就是优先级，范围：16-19
＜interface-name＞|进行显示的接口名
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示通过接口fei-0/1/0/5，指定上送到目的cpu为MPU-0/20/0，队列2的队列深度值：ZXROSNG#show cps ctm-queue destcpu r-cpu priority-queue 2 interface fei-0/1/0/5 Cpu            Interface           Priority        Levelr-cpu    fei-0/1/0/5           2                high
相关命令 : 
ctm queue-limit 
## show cps ctm-rate 

show cps ctm-rate 
命令功能 : 
该命令用于显示指定报文目的CPU和上送源单板的限速值。当需要显示指定源单板上送到目的CPU的限速配置时，使用该命令，当没有配置时，显示默认配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps ctm-rate 
 destcpu 
 {r-cpu 
|l-cpu 
} board 
 ＜board-name 
＞ 
命令参数解释 : 
参数|描述
---|---
r-cpu|主控CPU
l-cpu|线卡CPU
＜board-name＞|格式为：单板名称-机框号/槽位号，用于指定显示上送报文的源单板。
缺省 : 
无 
使用说明 : 
显示ctm-rate时，若配置了显示配置值，若没配置显示默认值。 
范例 : 
显示从PFU-0/1单板上送到目的CPU(PFU-0/1/0)的上行限速值cir 100，cbs 100，eir 100,下行限速值cir 100，cbs 100，eir 100ZXROSNG(config-cps)#show cps ctm-rate destcpu l-cpu board PFU-0/1 Cpu         Board    Location  Cir(kbps) Cbs(KByte)Eir(kbps) l-cpu   PFU-0/1  down-ctm  100       100       100       l-cpu   PFU-0/1  up-ctm    100       100       100
相关命令 : 
ctm rate-limit 
## show cps flow back-press flowtype 

show cps flow back-press flowtype 
命令功能 : 
该命令用于显示某个接口下用户期望的反压策略与物理接口的flowtype进行绑定的信息。当需要显示某种flowtype流类型在指定接口下和反压模板的对应绑定关系时，使用该命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps flow back-press flowtype 
 interface 
 ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|指定显示反压策略与flowtype绑定信息的接口名
缺省 : 
无 
使用说明 : 
需要指定接口名 
范例 : 
显示接口fei-0/1/0/5下，策略模板与流类型绑定的信息：ZXROSNG(config-cps)#show cps flow back-press flowtype interface fei-0/1/0/5Interface              Flowtype                             Profilefei-0/1/0/5            bfd-known                               2 fei-0/1/0/5            arp-default                             2
相关命令 : 
flow back-press flowtype 
## show cps flow back-press profile 

show cps flow back-press profile 
命令功能 : 
该命令用于显示配置用户期望的反压策略。当需要显示对应模板的具体反压策略时，使用该命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps flow back-press profile 
  [＜profile-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜profile-name＞|指定显示的模板名，可以不指定，即显示所有配的策略模板信息，范围：1-16
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示策略模板2的反压策略信息：ZXROSNG(config-cps)#show cps flow back-press profile 2Profile2exceed 20%             decline 30%exceed 50%             decline 50%exceed 90%             suspend
相关命令 : 
flow back-press profile 
## show cps flow limit profile 

show cps flow limit profile 
命令功能 : 
该命令用于显示用户期望的flow limit模板配置。当需要显示具体的flowtype限速模板配置时，使用该命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps flow limit profile 
  [＜profile-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜profile-name＞|指定显示的模板名，可以不指定，即显示所有配的策略模板信息，范围：1-16
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示flow limit模板10的策略信息：ZXROSNG#show cps flow limit profile 10Profile 10        Flowtype            Rate(pps) Quota(pps)        dhcp                 3           31                nd                   1           11                gre                  2           21                gvrp                 4           41       
相关命令 : 
无 
## show cps flow limit 

show cps flow limit 
命令功能 : 
该命令用于显示指定接口的flowtype的上送速率配置信息。当需要显示某个指定接口下的flowtype限速信息时，使用该命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps flow limit 
 interface 
 ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名，限定物理接口
缺省 : 
无 
使用说明 : 
需要指定物理接口名 
范例 : 
显示指定接口的flowtype配置上送速率值ZXROSNG(config-cps)#show cps flow limit interface fei-0/1/0/5Interface           IfIndex   Flowtype            Rate(pps) Quota(pps)fei-0/1/0/5         7         ah                  10        10        (*)fei-0/1/0/5         7         arp-default         100       100       (*)fei-0/1/0/5         7         arp-suppress        100       100       (*)fei-0/1/0/5         7         atm-oam             10        10        (*)fei-0/1/0/5         7         bfd-default         20        20        (*)                   
相关命令 : 
flow limit profile 
## show cps flow statistics 

show cps flow statistics 
命令功能 : 
该命令用于显示指定物理接口/CPU上送控制面流量指定flowtype的上送/丢弃计数。当需要显示指定接口下对应flowtype的上送、丢弃报文；所有接口下总的上送、丢弃报文；指定CPU收到、发送的报文时，使用该命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps flow statistics 
  [flowtype 
 ＜flowtype-name 
＞] [{interface 
 ＜interface-name 
＞|cpu 
 ＜cpu-name 
＞|summary 
}] 
命令参数解释 : 
参数|描述
---|---
＜flowtype-name＞|系统定义的流类型
＜interface-name＞|指定接口名
＜cpu-name＞|具体的CPU信息
summary|所有接口下对应流类型的计数统计和
缺省 : 
无 
使用说明 : 
1.支持显示指定物理接口指定flowtype的流的入向接收/丢弃统计计数。2.支持显示指定物理接口所有flowtype的流的入向接收/丢弃统计计数。3.支持显示指定CPU下的指定flowtype的流的控制面接收/控制面发送统计计数。4.支持显示指定CPU下的所有flowtype的流的控制面接收/控制面发送统计计数。5.支持显示系统所有物理端口下指定flowtype的流的入向接收/丢弃统计计数。6.支持显示系统所有物理端口下所有flowtype的流的入向接收/丢弃统计计数。7.支持显示系统所有物理端口下指定flowtype的流的入向接收/丢弃统计计数
范例 : 
1. 显示从指定接口接收指定flowtype的上送统计信息ZXROSNG#show cps flow statistics flowtype bgp-known interface gei-0/1/0/4Interface     Flowtype    In-packets      Upsend-packets      Drop-packetsGei-0/1/0/4  Bgp-known        1000           900                 1002. 显示从指定接口接收所有flowtype的上送统计信息ZXROSNG#show cps flow statictics interface gei-0/1/0/4Interface      Flowtype    In-packets   Upsend-packets  Drop-packets   Gei-0/1/0/4   bgp-default  100         50               50           bgp-config   200        200               0            bgp-known   1000      1000              0              ospf-default  300        300               023. 显示指定CPU的所有flowtype的上送统计信息ZXROSNG#show cps flow statistics cpu MPU-0/20/0Flowtype      In-packets      Send-packetsdefault         900              900bgp-default    90                90bgp-config     300               3004. 显示指定CPU的指定flowtype的上送统计信息ZXROSNG#show cps flow statictics flowtype bgp-known cpu MPU-0/20/0Flowtype      In-packets        Send-packetsbgp-known     300              3005. 显示系统所有接口指定flowtype的上送统计信息ZXROSNG#show cps flow statictics flowtype bgp-knownInterface    Flowtype   In-packets   Upsend-packets  Drop-packetsGei-10/1/0/1 bgp-known   1000        1000            0     Gei-10/1/0/2 bgp-known   300          300            06. 显示系统所有端口的控制面上送报文的收包/丢包信息ZXROSNG#show cps flow statictics Interface    Flowtype   In-packets   Upsend-packets  Drop-packetsGei-10/1/0/1 default     1000         100             900          bgp-default     100          50              50         bgp-config      200          200             0         bgp-known      1000        1000            0        ospf-default     300          300             0              ...Gei-10/1/0/2 default      100          100             0          bgp-default     10           10              0        bgp-config      20           20              07. 显示系统控制面上送报文的收包/丢包总统计信息（不区分接口）ZXROSNG#show cps flow statictics summaryFlowtype   In-packets   Upsend-packets  Drop-packetsdefault      1000        100            900  bgp-default  100         50             50 bgp-config   200         200             0 bgp-known  1000        970             30ospf-default  300         300             0
相关命令 : 
clear cps flow statistics 
## show cps gtsm statistics 

show cps gtsm statistics 
命令功能 : 
该命令用于查看GTSM统计计数信息。当需要显示对应的flowtype的GTSM收包、丢包统计信息时，使用该命令。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps gtsm statistics 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
用于显示GTSM统计信息 
范例 : 
显示GTSM的统计信息ZXROSNG(config-if-fei-0/1/0/5)#show cps gtsm statistics Flowtype                Upsend-packets          Drop-packets   
相关命令 : 
clear cps gtsm statistics 
## show cps management-service 

show cps management-service 
命令功能 : 
该命令用于显示指定接口的管理协议的安全配置。当需要显示指定接口下对应管理协议的过滤规则时，使用该命令，当没有配置时，显示默认配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps management-service 
 interface 
 ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|指定接口名
缺省 : 
无 
使用说明 : 
需指定对应的接口名如果没有配置，缺省显示permit
范例 : 
显示接口上管理协议的安全配置显示效果ZXROSNG(config)#show cps management-service interface fei-0/1/0/5management-service  permission      --------------------------------------telnet                  permit          ssh                     permit          ftp                     permit          snmp                    permit  
相关命令 : 
management-service {permit|deny} <protocol> 
## show cps mng-access 

show cps mng-access 
命令功能 : 
该命令用于显示管理口生效的安全过滤规则。当需要显示当前管理口针对IP地址、MAC地址、端口过滤、协议过滤的规则时，使用该命令。当没有配置时，管理协议显示默认配置，其余过滤规则默认为permit。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cps mng-access 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无配置的情况下显示缺省配置 
范例 : 
显示管理口的安全策略ZXROSNG#show cps mng-access                           Peer-mac                                            --------------------------------------                      deny                 any                            deny                 0000.0000.0000                 deny                 2233.4444.5555                 deny                 3342.2234.5552         Peer-ip                                             --------------------------------------                      deny                 any                            deny                 0.0.0.0 255.255.0.0            deny                 100.1.1.0 255.255.255.0Protocol                                            --------------------------------------                      deny                any                             permit              arp                             permit              ftp                             permit              icmp                            permit              radius                          permit              snmp                            permit              ssh                             permit              tacacs-plus                     permit              telnet                          permit              tftp
相关命令 : 
mng-access peer-ipmng-access peer-macmng-access protocol
