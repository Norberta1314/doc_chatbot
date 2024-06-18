# ARP配置命令 
## acl 


acl 




### 命令功能 


在接口绑定ACL规则 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



acl 
  ＜interface name 
＞ bind 
 ＜acl-name 
＞
no acl 
  ＜interface name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface name＞|接口名
＜acl-name＞|ACL规则名








### 缺省 


无 






### 使用说明 


在指定接口绑定ACL规则 






### 范例 


1、进入arp全局模式在smartgroup1接口上绑定ACL规则 abc：ZXROSNG(config)#arpZXROSNG(config-arp)#acl smartgroup1 bind abc2、进入arp全局模式在smartgroup1接口上解绑ACL规则：ZXROSNG(config)#arpZXROSNG(config-arp)#no acl smartgroup1






### 相关命令 


无 




## acl 


acl 




### 命令功能 


ARP绑定ACL规则，根据绑定的ACL规则，过滤ARP报文，不符合ACL规则的ARP报文将被丢弃 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




acl 
 bind 
 ＜acl-name 
＞

no acl 








### 命令参数解释 




参数|描述
---|---
＜acl-name＞|要绑定的acl名称,长度1-31个字符








### 缺省 


无 






### 使用说明 


绑定ACL规则时，此ACL规则必须存在。 






### 范例 


1、在以太网接口上绑定ACL规则 rulea：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#acl bind rulea2、去除以太网接口上配置的ACL规则:ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no acl bind rulea





### 相关命令 


ipv4-access-list 




## alarm-threshold learn-limit 


alarm-threshold learn-limit 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口的ARP学习限制保护的告警阈值。可以通过no命令将保护值恢复成默认值。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



alarm-threshold learn-limit 
  ＜interface-name 
＞ ＜packet_num 
＞
no alarm-threshold learn-limit 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜packet_num＞|每10s丢弃的ARP报文数目总合达到指定的阈值时，产生告警。范围为1-65535。








### 缺省 


阈值缺省每10秒300个报文 






### 使用说明 


默认告警阈值为300，即10秒内因学习限制而丢弃的ARP报文总数达到300个时，发出告警。  本命令只有当learn-limit功能开启时，才会起作用。因为只有当learn-limit功能打开，才会因此丢弃报文。告警产生后，如果下一个10秒内未在出现因ARP学习限制丢弃的ARP报文超过阈值的情况，恢复告警。no命令恢复默认值。






### 范例 


1、在接口gei-0/1/0/1上配置学习限制报文丢弃告警阈值为10个：ZXROSNG(config)#arpZXROSNG(config-arp)#alarm-threshold  learn-limit gei-0/1/0/1 102、恢复接口gei-0/1/0/1上配置学习限制报文丢弃告警阈值为默认值：ZXROSNG(config)#arpZXROSNG(config-arp)# no alarm-threshold learn-limit gei-0/1/0/1





### 相关命令 


learn-limitshow arp statistics 




## alarm-threshold learn-limit 


alarm-threshold learn-limit 




### 命令功能 


该命令工作于ARP接口配置模式下，配置指定接口的ARP学习限制保护的告警阈值。可以通过no命令将保护值恢复成默认值。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




alarm-threshold learn-limit 
  ＜packet_num 
＞

no alarm-threshold learn-limit 








### 命令参数解释 




参数|描述
---|---
＜packet_num＞|每10s丢弃的ARP报文数目总合达到指定的阈值时，产生告警。范围为1-65535。








### 缺省 


阈值缺省每10秒300个报文 






### 使用说明 


默认告警阈值为300，即10秒内因学习限制而丢弃的ARP报文总数达到300个时，发出告警。 本命令只有当learn-limit功能开启时，才会起作用。因为只有当learn-limit功能打开，才会因此丢弃报文。告警产生后，如果下一个10秒内未在出现因ARP学习限制丢弃的ARP报文超过阈值的情况，恢复告警。no命令恢复默认值。






### 范例 


1、在接口gei-0/1/0/1上配置学习限制报文丢弃告警阈值为10个：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#alarm-threshold learn-limit 102、恢复接口gei-0/1/0/1上配置学习限制报文丢弃告警阈值为默认值：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no alarm-threshold learn-limit





### 相关命令 


learn-limitshow arp statistics




## alarm-threshold source-filter 


alarm-threshold source-filter 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口的ARP源过滤保护的告警阈值。可以通过no命令将保护值恢复成默认值。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



alarm-threshold source-filter 
  ＜interface-name 
＞ ＜packet_num 
＞
no alarm-threshold source-filter 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜packet_num＞|每10s丢弃的ARP报文数目总合达到指定的阈值时，产生告警。范围为1-65535。








### 缺省 


阈值缺省每10秒300个报文 






### 使用说明 


默认告警阈值为300，即10秒内因源过滤而丢弃的ARP报文总数达到300个时，发出告警。  本命令只有当source-filter功能开启时，才会起作用。因为只有当source-filter功能打开，才会因此丢弃报文。告警产生后，如果下一个10秒内未在出现因ARP学习限制丢弃的ARP报文超过阈值的情况，恢复告警。no命令恢复默认值。






### 范例 


1、在接口gei-0/1/0/1上配置学习限制报文丢弃告警阈值为10个：ZXROSNG(config)#arpZXROSNG(config-arp)#alarm-threshold source-filter gei-0/1/0/1 102、恢复接口gei-0/1/0/1上配置学习限制报文丢弃告警阈值为默认值：ZXROSNG(config)#arpZXROSNG(config-arp)#no alarm-threshold source-filter gei-0/1/0/1





### 相关命令 


source-filteredshow arp statistics




## alarm-threshold source-filter 


alarm-threshold source-filter 




### 命令功能 


该命令工作于ARP接口配置模式下，配置指定接口的ARP源过滤保护的告警阈值。可以通过no命令将保护值恢复成默认值。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




alarm-threshold source-filter 
  ＜packet_num 
＞

no alarm-threshold source-filter 








### 命令参数解释 




参数|描述
---|---
＜packet_num＞|每10s丢弃的ARP报文数目总合达到指定的阈值时，产生告警。范围为1-65535。








### 缺省 


阈值缺省每10秒300个报文 






### 使用说明 


默认告警阈值为300，即10秒内因源过滤而丢弃的ARP报文总数达到300个时，发出告警。  本命令只有当source-filter功能开启时，才会起作用。因为只有当source-filter功能打开，才会因此丢弃报文。告警产生后，如果下一个10秒内未在出现因ARP学习限制丢弃的ARP报文超过阈值的情况，恢复告警。no命令恢复默认值。






### 范例 


1、在接口gei-0/1/0/1上配置学习限制报文丢弃告警阈值为10个：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#alarm-threshold source-filter 102、恢复接口gei-0/1/0/1上配置学习限制报文丢弃告警阈值为默认值：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no alarm-threshold source-filter





### 相关命令 


source-filteredshow arp statistics




## arp &amp;lt;mid&amp;gt; permanent 


arp <mid> permanent 




### 命令功能 


配置永久ARP条目, 使用no命令可以清除配置的永久ARP条目。配置后写数据库的ARP条目，配置并保存后，重启设备，依然存在，这种ARP条目即为永久类型ARP条目。此类ARP条目不会老化丢失，可长期保存，主要用于保存固定且安全的IP+MAC地址组合。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



arp  
 ＜interface-name 
＞ permanent 
  ＜ip-address 
＞ ＜mac-address 
＞ [＜external-vlan-id 
＞ [＜internal-vlan-id 
＞]]
no arp  
 ＜interface-name 
＞ permanent 
  ＜ip-address 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口名，用于指定配置的接口 。
＜ip-address＞|ip地址
＜mac-address＞|MAC地址，为点分十六进制形式
＜external-vlan-id＞|指明该条目的外层VLAN ID，范围是<1-4094>，无缺省值
＜internal-vlan-id＞|指明该条目的内层VLAN ID，范围是<1-4094>，无缺省值








### 缺省 


无 






### 使用说明 


配置永久ARP时，指定的内外层VLAN和VLAN封装形式必须与接口的VLAN配置相对应。接口上即使没有IP地址也可以配置永久ARP。变更接口VRF时，需要判断接口上是否有永久ARP，如果有，需要先删除永久ARP。 






### 范例 


范例1、在以太网接口上绑定IP地址（10.1.1.1）与MAC地址（000a.010c.e2c6）：ZXROSNG(config)#arpZXROSNG(config-arp)#arp gei-0/1/0/1 permanent 10.1.1.1 000a.010c.e2c62、删除以太网接口上IP地址（10.1.1.1）的永久ARP:ZXROSNG(config)#arpZXROSNG(config-arp)#no arp gei-0/1/0/1 permanent 10.1.1.1





### 相关命令 


show arpclear arp-cache



## arp &amp;lt;mid&amp;gt; static 


arp <mid> static 




### 命令功能 


配置静态ARP条目, 使用no命令可以清除配置的静态ARP条目，该配置产生的ARP条目不写数据库，设备重启后没有相关的ARP条目 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



arp  
 ＜interface-name 
＞ static 
  ＜ip-address 
＞ ＜mac-address 
＞ [＜external-vlan-id 
＞ [＜internal-vlan-id 
＞]]
no arp  
 ＜interface-name 
＞ static 
  ＜ip-address 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口名，用于指定配置的接口 。
＜ip-address＞|ip地址
＜mac-address＞|MAC地址，为点分十六进制形式
＜external-vlan-id＞|指明该条目的外层VLAN ID，范围是<1-4094>，无缺省值
＜internal-vlan-id＞|指明该条目的内层VLAN ID，范围是<1-4094>，无缺省值








### 缺省 


无 






### 使用说明 


配置静态ARP时，指定的内外层VLAN和VLAN封装形式必须与接口的VLAN配置相对应。接口上即使没有IP地址也可以配置静态ARP。 






### 范例 


1、在以太网接口上绑定IP地址（10.1.1.1）与MAC地址（000a.010c.e2c6）：ZXROSNG(config)#arpZXROSNG(config-arp)#arp gei-0/1/0/1 static 10.1.1.1 000a.010c.e2c62、删除以太网接口上IP地址（10.1.1.1）的永久ARP:ZXROSNG(config)#arpZXROSNG(config-arp)#no arp gei-0/1/0/1 static  10.1.1.1





### 相关命令 


show arpclear arp-cache



## arp permanent 


arp permanent 




### 命令功能 


该命令工作于ARP接口配置模式下，用于配置永久类型ARP条目，使用no命令可以清除配置的永久ARP条目。配置后写数据库的ARP条目，配置并保存后，重启设备，依然存在，这种ARP条目即为永久类型ARP条目。此类ARP条目不会老化丢失，可长期保存，主要用于保存固定且安全的IP+MAC地址组合。





### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



arp permanent 
  ＜ip-address 
＞ ＜mac-address 
＞ [＜external-vlan-id 
＞ [＜internal-vlan-id 
＞]]
no arp permanent 
  ＜ip-address 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ip-address＞|IPV4类型IP地址，格式为点分十进制形式（用户需要配置的地址，不是接口地址，用户自己决定）默认值：无。
＜mac-address＞|MAC地址，点分十六进制形式（用户需要配置的地址，不是接口地址，用户自己决定）默认值：无。
＜external-vlan-id＞|指明配置条目的VLAN ID或者外层VLAN ID取值范围：1-4094默认值：无。
＜internal-vlan-id＞|指明配置条目的内层VLAN ID取值范围：1-4094默认值：无。








### 缺省 


无 






### 使用说明 


该命令用于在ARP接口配置模下配置永久类型ARP条目。可配置数目：平台默认4096条，不同项目具体数目由项目性能参数控制。MAC地址不能是全0、广播或者组播MAC。






### 范例 


1、在ARP接口配置模式下，在接口gei-0/1/0/1下配置IP地址为10.1.1.1和MAC地址为000a.010c.e2c6的永久类型ARP条目，则输入以下命令：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#arp permanent 10.1.1.1 .000a.010c.e2c62、在ARP接口配置模式下，在接口gei-0/1/0/1下，去除IP地址为10.1.1.1和MAC地址为000a.010c.e2c6的永久类型ARP条目，则输入以下命令：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no arp permanent 10.1.1.1





### 相关命令 


无 




## arp static 


arp static 




### 命令功能 


配置静态ARP条目, 使用no命令可以清除配置静态ARP条目。该配置产生的ARP条目不写数据库，设备重启后没有相关的ARP条目。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



arp static 
  ＜ip-address 
＞ ＜mac-address 
＞ [＜external-vlan-id 
＞ [＜internal-vlan-id 
＞]]
no arp static 
  ＜ip-address 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ip-address＞|IP地址，为点分十进制形式
＜mac-address＞|MAC地址，为点分十六进制形式
＜external-vlan-id＞|指明该条目的外层VLAN ID，范围是<1-4094>，无缺省值
＜internal-vlan-id＞|指明该条目的内层VLAN ID，范围是<1-4094>，无缺省值








### 缺省 


无 






### 使用说明 


配置静态ARP时，指定的内外层VLAN和VLAN封装形式必须与接口的VLAN配置相对应。接口上即使没有IP地址也可以配置静态ARP。MAC地址不能是全0、广播或者组播MAC。






### 范例 


1、在以太网接口上绑定IP地址（10.1.1.1）与MAC地址（000a.010c.e2c6）：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#arp static 10.1.1.1 000a.010c.e2c62、删除以太网接口上IP地址（10.1.1.1）的永久ARP:ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no arp static 10.1.1.1





### 相关命令 


show arpclear arp-cache



## arp 


arp 




### 命令功能 


该命令工作于全局配置模式下，用于进入ARP配置模式。ARP（Address Resolution Protocol，地址解析协议）：IP数据包常通过以太网发送，但以太网设备并不识别32位IP地址（IPV4地址类型），它们是以48位以太网地址传输以太网数据包。因此，必须把IP目的地址转换成以太网目的地址。ARP协议用于将网络中的IP地址解析为目标硬件地址（MAC地址），以保证通信的顺利进行。ARP模式下可以配置ARP模块大部分配置命令，比如to-static,purge-delay等等命令。






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



arp 
 






### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


该命令用于从全局配置模式进入ARP配置模式 






### 范例 


从全局配置模式进入ARP配置模式：则输入以下命令：ZXROSNG(config)#arpZXROSNG(config-arp)#






### 相关命令 


无 




## arp-logging 


arp-logging 




### 命令功能 


该命令工作在ARP全局模式，用于控制ARP模块的日志上报功能的开启和关闭。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 




arp-logging 
  {on 
|off 
}







### 命令参数解释 




参数|描述
---|---
on|ARP日志上报功能的开启
off|ARP日志上报功能的关闭








### 缺省 


关闭 






### 使用说明 


无 






### 范例 


1、开启ARP日志上报功能：ZXROSNG(config)#arpZXROSNG(config-arp)#arp-logging on2、关闭ARP日志上报功能：ZXROSNG(config)#arpZXROSNG(config-arp)#arp-logging off






### 相关命令 


无 




## arp-scan 


arp-scan 




### 命令功能 


该命令配置时指定接口，指定IP地址范围，配置成功后，立即对配置的所有IP地址发送一次ARP请求报文，通过收到ARP应答来学习配置的IP地址对应的MAC信息。。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




arp-scan 
  ＜interface-name 
＞ ＜begin-ip-address 
＞ ＜end-ip-address 
＞







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜begin-ip-address＞|IP地址段的起始值
＜end-ip-address＞|IP地址段的结束值








### 缺省 


无 






### 使用说明 


指定的接口必须为三层属性的接口，并且已经配置IP地址。当需要扫描单个IP地址时，起始IP与结束IP相同。指定扫描的地址段，不能超过255个IP地址。本命令为操作命令，不存盘不写库，show running-config和show running-config all都不需要显示，在手动模式下直接执行。






### 范例 


配置接口gei-0/1/0/1在地址段10.1.1.1到10.1.1.128的ARP扫描：ZXROSNG#arp-scan gei-0/1/0/1 10.1.1.1 10.1.1.128





### 相关命令 


无 




## backupvrrp-learn 


backupvrrp-learn 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口的备VRRP ARP学习功能。设备收到目的IP地址为本接口的VRRP地址且VRRP状态为备的情况下，若该功能打开则学习ARP条目，若该功能关闭时则不学习。可以通过no命令来关闭此功能。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



backupvrrp-learn 
  ＜interface-name 
＞
no backupvrrp-learn 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


该功能关闭。 






### 使用说明 


默认接口为备VRRP状态时，不学习ARP条目。开启此功能后，当接口为备VRRP状态时，且ARP报文的目的IP地址为VRRP地址时，依然正常学习ARP。如果目的IP是接口地址，非VRRP地址时，即使VRRP是备状态，也不受该命令控制





### 范例 


1、配置接口gei-0/1/0/1的备VRRP ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)# backupvrrp-learn gei-0/1/0/12、关闭接口gei-0/1/0/1的备VRRP ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)#no backupvrrp-learn gei-0/1/0/1






### 相关命令 


无 




## backupvrrp-learn 


backupvrrp-learn 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口的备VRRP ARP学习功能。设备收到目的IP地址为本接口的VRRP地址且VRRP状态为备的情况下，若该功能打开则学习ARP条目，若该功能关闭时则不学习。可以通过no命令来关闭此功能。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




backupvrrp-learn 
 

no backupvrrp-learn 








### 命令参数解释 



					无
				 






### 缺省 


缺省不开启备VRRP ARP学习功能。 






### 使用说明 


默认接口为备VRRP状态时，不学习ARP条目。开启此功能后，当接口为备VRRP状态时，且ARP报文的目的IP地址为VRRP地址时，依然正常学习ARP。如果目的IP是接口地址，非VRRP地址时，即使VRRP是备状态，也不受该命令控制。





### 范例 


1、配置接口gei-0/1/0/1的备VRRP ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# backupvrrp-learn2、关闭接口gei-0/1/0/1的备VRRP ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no backupvrrp-learn





### 相关命令 


无 




## clear arp statistics 


clear arp statistics 




### 命令功能 


该命令工作于特权模式下，清空接口报文统计计数。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear arp statistics 
  ＜interface-name 
＞







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


无 






### 使用说明 


主要用于观察接下来的各接口报文计数，首先进行清空，在收包完成后，再执行show arp statistics，即可观察上一段时间内各接口报文计数。 






### 范例 


显示所有接口的报文接受信息：Rcv_packets：该接口下收到的ARP报文总数Err_packets：该接口下收到的ARP报文错误数量ZXROSNG#show arp statistics Interface                    Rcv_packets  Err_packets-----------------------------------------------------------gei-0/1/0/1                      1            0gei-0/1/0/2                      2            0gei-0/1/0/3                      0            0gei-0/1/0/4                      0            0gei-0/1/0/5                      0            0gei-0/1/0/6                      0            0gei-0/1/0/7                      0            0gei-0/1/0/8                      0            0mgmt_eth                     44           44清除接口报文接受信息：ZXROSNG#clear arp statistics 在gei-0/1/0/1学习ARP之后，再进行show arp statistics操作：ZXROSNG#show arp statistics     Interface                    Rcv_packets  Err_packets-----------------------------------------------------------gei-0/1/0/1                      2            0gei-0/1/0/2                      0            0gei-0/1/0/3                      0            0gei-0/1/0/4                      0            0gei-0/1/0/5                      0            0gei-0/1/0/6                      0            0gei-0/1/0/7                      0            0gei-0/1/0/8                      0            0mgmt_eth                      0            0





### 相关命令 


show arp statistics 




## clear arp-cache controller 


clear arp-cache controller 




### 命令功能 


清除控制器下发的ARP条目。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear arp-cache controller 
 

no clear arp-cache controller 








### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


可以清除所有控制器下发的ARP条目。 






### 范例 


清除所有控制器下发的ARP条目：ZXROSNG#clear arp-cache controller





### 相关命令 


show arp 




## clear arp-cache permanent 


clear arp-cache permanent 




### 命令功能 


该命令工作于特权模式下，按指定范围清除永久ARP条目。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear arp-cache permanent 
  [interface 
 ＜interface-name 
＞]







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|按指定的接口删除永久ARP。








### 缺省 


无 






### 使用说明 


可以在全局和接口范围内删除永久ARP条目。该命令只对配置的永久ARP条目生效。 






### 范例 


1、清除接口gei-0/1/0/1下永久ARP：ZXROSNG#clear arp-cache permanent interface gei-0/1/0/12、清除全局下永久ARP条目：ZXROSNG#clear arp-cache permanent





### 相关命令 


show arp 




## clear arp-cache static 


clear arp-cache static 




### 命令功能 


按指定的范围清除静态ARP条目。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear arp-cache static 
  [interface 
 ＜interface-name 
＞]







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口名








### 缺省 


无 






### 使用说明 


按指定的范围清除静态ARP条目。该命令只对配置的静态条目生效。 






### 范例 


1、清除接口vlan1上的动态ARP条目ZXROSNG#clear arp-cache interface vlan12、清除接口vlan1上的静态ARP条目ZXROSNG#clear arp-cache static interface vlan1





### 相关命令 


show arp 




## clear arp-cache to-static 


clear arp-cache to-static 




### 命令功能 


该命令工作于特权模式下，按指定范围清除to-static类型ARP条目。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear arp-cache to-static 
  [interface 
 ＜interface-name 
＞]







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|按指定的接口删除to-static类型ARP。








### 缺省 


无 






### 使用说明 


可以在全局和接口范围内删除动态转静态的ARP条目。该命令只对原先是动态生成的后来通过to-static命令转成静态的ARP条目生效，也就是to-static类型的ARP条目 






### 范例 


1、清除接口gei-0/1/0/1下to-static类型ARP：ZXROSNG#clear arp-cache to-static interface gei-0/1/0/12、清除全局下to-static类型ARP条目：ZXROSNG#clear arp-cache to-static





### 相关命令 


show arp 




## clear arp-cache 


clear arp-cache 




### 命令功能 


该命令工作于特权模式下，按指定范围清除动态ARP条目。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear arp-cache 
  [interface 
 ＜interface-name 
＞] [{ip 
 ＜ip-address 
＞|mac 
 ＜mac-address 
＞|ip-range 
 from 
 ＜begin-ip-address-of-range 
＞ to 
 ＜end-ip-address-of-range 
＞}]







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|按指定的接口删除动态ARP。
＜ip-address＞|按指定的IP地址删除动态ARP。IP地址，点分十进制。
＜mac-address＞|按指定的MAC地址删除动态ARP。MAC地址，点分十六进制。
＜begin-ip-address-of-range＞|按指定的IP地址范围删除动态ARP。IP范围的下限。
＜end-ip-address-of-range＞|按指定的IP地址范围删除动态ARP。IP范围的上限。








### 缺省 


无 






### 使用说明 


可以在全局和接口范围内按IP地址、MAC地址和IP范围来删除动态ARP条目。该命令只能删除动态学习的ARP条目，对配置的ARP条目或其他方式得到的ARP条目不生效。






### 范例 


1、清除接口gei-0/1/0/1下动态ARP：ZXROSNG#clear arp-cache interface gei-0/1/0/12、清除指定IP地址1.1.1.1的动态ARP条目：ZXROSNG#clear arp-cache ip 1.1.1.13、清除指定MAC地址0001.0002.0003的动态ARP条目：ZXROSNG#clear arp-cache mac 0001.0002.00034、清除irb接口的ARP：ZXROSNG#clear arp-cache interface irb1





### 相关命令 


show arp 




## conflict-notify 


conflict-notify 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口的IP冲突检测功能。可以通过no命令来关闭此功能。IP冲突检测功能：开启此功能后，当接口收到请求类型免费ARP报文时，当源IP所对应的报文中的源MAC和已经学习到的ARP表中IP所对应的MAC地址不一样时，向源IP设备回复免费ARP应答报文，并将ARP表中学到的条目进行老化。





### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



conflict-notify 
  ＜interface name 
＞ {enable 
|disable 
}






### 命令参数解释 




参数|描述
---|---
＜interface name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
enable|使能通知用户IP冲突功能
disable|关闭通知用户IP冲突功能








### 缺省 


默认不开启IP冲突通知功能。 






### 使用说明 


该功能一般在两个用户IP地址可能会冲突的情况下使用。 






### 范例 


1、在接口gei-0/1/0/1上配置IP地址冲突告警功能：ZXROSNG(config)#arpZXROSNG(config-arp)#conflict-notify gei-0/1/0/1 enable2、关闭接口gei-0/1/0/1上IP地址冲突告警功能：ZXROSNG(config)#arp ZXROSNG(config-arp)#conflict-notify gei-0/1/0/1 disable






### 相关命令 


无 




## conflict-notify 


conflict-notify 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口的IP冲突检测功能。可以通过no命令来关闭此功能。IP冲突检测功能：开启此功能后，当接口收到请求类型免费ARP报文时，当源IP所对应的报文中的源MAC和已经学习到的ARP表中IP所对应的MAC地址不一样时，向源IP设备回复免费ARP应答报文，并将ARP表中学到的条目进行老化。





### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



conflict-notify 
  {enable 
|disable 
}






### 命令参数解释 




参数|描述
---|---
enable|使能通知用户IP冲突功能
disable|关闭通知用户IP冲突功能








### 缺省 


默认不开启IP冲突通知功能。 






### 使用说明 


该功能一般在两个用户IP地址可能会冲突的情况下使用。 






### 范例 


在接口gei-0/1/0/1上配置IP地址冲突告警功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#conflict-notify enable2、关闭接口gei-0/1/0/1上IP地址冲突告警功能： ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#conflict-notify disable






### 相关命令 


无 




## debug arp 


debug arp 




### 命令功能 


打开ARP的packets debug功能，显示地址解析协议ARP处理收发包状态的调试信息，显示是否在发送或接收ARP报文。使用no命令关闭该功能。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


2 






### 命令格式 



debug arp 
  {packets 
 {interface 
 ＜interface-name 
＞|{source 
|destination 
} {＜ip-address 
＞|＜mac-address 
＞}}|trace 
 {receive 
|send 
} {source 
|destination 
} {＜ip-address 
＞|＜mac-address 
＞}|all 
}
no debug arp 
  {packets 
 {interface 
 ＜interface-name 
＞|{source 
|destination 
} {＜ip-address 
＞|＜mac-address 
＞}}|trace 
 {receive 
|send 
} {source 
|destination 
} {＜ip-address 
＞|＜mac-address 
＞}|all 
}
				






### 命令参数解释 




参数|描述
---|---
packets|打印ARP收发报文状态
interface|打印指定接口的ARP包
＜interface-name＞|接口名称
source|打印指定源IP地址的ARP包
destination|打印指定目的IP地址的ARP包
＜ip-address＞|IP地址
＜mac-address＞|MAC地址
trace|打印ARP收发报文流程
receive|打印ARP接收报文流程
send|打印ARP发送报文流程
source|打印指定源IP地址的ARP包
destination|打印指定目的IP地址的ARP包
＜ip-address＞|IP地址
＜mac-address＞|MAC地址
all|打印所有收发ARP报文状态和流程








### 缺省 


无 






### 使用说明 


debug  arp packet interface 接口名，可以查看指定接口的ARP报文收发情况；debug arp trace 可以查看指定报文的处理结果，如果丢弃，可显示丢弃原因。 






### 范例 


打印接口gei-0/1/0/1上ARP报文的收发情况：ZXROSNG#debug arp packets interface gei-0/1/0/1






### 相关命令 


show debug arp 




## detect looptime 


detect looptime 




### 命令功能 


配置ARP探测周期，即隔多长时间发起下一次探测。该命令在detect命令同时开启时生效。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




detect looptime 
  ＜looptime 
＞

no detect looptime 








### 命令参数解释 




参数|描述
---|---
＜looptime＞|探测周期，单位为秒，范围<2-14400>








### 缺省 


缺省探测时间为60秒。 






### 使用说明 


当探测功能开启时，该命令生效；探测功能关闭时，该命令无效。如果开启了探测功能，按探测周期进行ARP探测，优先级大于老化时间，即timeout命令失效。no命令恢复配置默认值。 






### 范例 


1、配置接口gei-0/1/0/1的ARP探测周期：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#detect enableZXROSNG(config-arp-gei-0/1/0/1)#detect looptime 22、恢复接口gei-0/1/0/1的ARP探测周期为缺省值：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#no detect looptime





### 相关命令 


detect  




## detect mode 


detect mode 




### 命令功能 


配置ARP探测模式，可配置报文探测模式或事件探测模式。报文探测模式只将探测失败导致的ARP删除通知snooping, 事件探测模式所有事件触发的ARP删除都通知snooping。该命令在detect命令同时开启时生效。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




detect mode 
  {packet 
|event 
}







### 命令参数解释 




参数|描述
---|---
packet|报文探测模式
event|事件探测模式








### 缺省 


缺省为报文探测模式。 






### 使用说明 


当探测功能开启时，该命令生效；探测功能关闭时，该命令无效。 






### 范例 


1、配置接口gei-0/1/0/1的ARP探测模式为报文模式：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#detect enableZXROSNG(config-arp-gei-0/1/0/1)#detect mode packet2、配置接口gei-0/1/0/1的ARP探测模式为事件模式：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#detect enableZXROSNG(config-arp-gei-0/1/0/1)#detect mode event





### 相关命令 


detect  




## detect retry-times 


detect retry-times 




### 命令功能 


配置ARP探测次数。配置探测功能和探测周期后，进行ARP探测，该命令用于配置每次探测周期到达进行ARP的探测次数，默认为3次。探测功能开启时才使用该命令配置的探测次数，不开启探测次数，ARP老化探测次数为固定值3次。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




detect retry-times 
  ＜retry-times 
＞

no detect retry-times 








### 命令参数解释 




参数|描述
---|---
＜retry-times＞|探测次数








### 缺省 


缺省探测次数为3次。 






### 使用说明 


当探测功能开启时，该命令生效；探测功能关闭时，该命令无效。no命令恢复配置默认值。 






### 范例 


1、配置接口gei-0/1/0/1的ARP探测次数：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#detect enableZXROSNG(config-arp-gei-0/1/0/1)#detect looptime 6ZXROSNG(config-arp-gei-0/1/0/1)#detect retry_times 22、恢复接口gei-0/1/0/1的ARP探测次数为缺省值：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#no detect retry_times





### 相关命令 


detect  




## detect timeout 


detect timeout 




### 命令功能 


配置ARP探测应答报文的延时时间，过了此延时时间认为没有收到报文。探测功能开启才使用该命令配置延时时间，否则使用固定时间3秒钟（热备接口项目可定制延时时间）。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




detect timeout 
  ＜timeout 
＞

no detect timeout 








### 命令参数解释 




参数|描述
---|---
＜timeout＞|探测应答报文的延时时间，单位为秒，范围<1-60>








### 缺省 


缺省探测应答报文的延时时间为3秒。 






### 使用说明 


当探测功能开启时，该命令生效；探测功能关闭时，该命令无效。no命令恢复配置默认值。 






### 范例 


1、配置接口gei-0/1/0/1的ARP探测报文应答延时时间：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#detect enableZXROSNG(config-arp-gei-0/1/0/1)#detect timeout 52、恢复接口gei-0/1/0/1的ARP探测报文应答延时时间为缺省值：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#no detect timeout





### 相关命令 


detect  




## detect 


detect 




### 命令功能 


使能ARP探测功能。开启ARP探测功能后，会对该 接口下学习到的动态ARP进行 定时探测，在规定的探测次数内探测不到用户，老化删除该ARP条目。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




detect 
  {enable 
|disable 
}







### 命令参数解释 




参数|描述
---|---
enable|打开ARP探测功能
disable|关闭ARP探测功能








### 缺省 


缺省关闭ARP探测功能。 






### 使用说明 


当开启探测功能时，ARP老化时间失效，按detect  looptime时间进行老化，即探测周期优于老化周期。 






### 范例 


1、配置接口gei-0/1/0/1的ARP探测功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#detect enable2、关闭接口gei-0/1/0/1的ARP探测功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)#detect disable 





### 相关命令 


timeoutdetect  modedetect  looptimedetect  retry_timesdetect  timeout




## gratuitous-learn 


gratuitous-learn 




### 命令功能 


该命令工作于ARP配置模式下，打开指定接口的免费ARP学习功能，可以通过no命令关闭此功能。免费ARP学习功能打开后，对于收到的免费ARP报文，将进行ARP学习；默认情况下，此功能未打开时，收到免费ARP不会进行ARP学习。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



gratuitous-learn 
  ＜interface-name 
＞
no gratuitous-learn 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


无 






### 使用说明 


默认免费ARP学习功能关闭。 






### 范例 


1、开启接口gei-0/1/0/1的免费ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)# gratuitous-learn gei-0/1/0/12、关闭接口gei-0/1/0/1的免费ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)# no gratuitous-learn gei-0/1/0/1





### 相关命令 


无 




## gratuitous-learn 


gratuitous-learn 




### 命令功能 


该命令工作于ARP接口配置模式下，打开指定接口的免费ARP学习功能。可以通过no命令关闭此功能。免费ARP学习功能打开后，对于收到的免费ARP报文，将进行ARP学习；默认情况下，此功能未打开时，收到免费ARP不会进行ARP学习。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



gratuitous-learn 
 

no gratuitous-learn 








### 命令参数解释 



					无
				 






### 缺省 


缺省不开启免费ARP学习功能。 






### 使用说明 


默认免费ARP学习功能关闭。 






### 范例 


1、开启接口gei-0/1/0/1的免费ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# gratuitous-learn2、关闭接口gei-0/1/0/1的免费ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no gratuitous-learn 






### 相关命令 


无 




## gratuitous-proxy-arp periodic 


gratuitous-proxy-arp periodic 




### 命令功能 


该命令工作于ARP配置模式下，配置免费代理ARP的定时发送时间。可以通过no命令恢复默认发送时间。当开启接口的免费代理ARP定时发送功能后，会定时使用接口上配置的代理IP地址向外发送免费ARP报文。配置时可以指定免费代理ARP的发送间隔，不指定则默认为30s。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



gratuitous-proxy-arp periodic 
  ＜interface-name 
＞ [＜seconds 
＞]
no gratuitous-proxy-arp periodic 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜seconds＞|接口定时发送免费代理ARP的间隔，范围1~14400，单位秒，默认30s








### 缺省 


不开启定时发送功能。 






### 使用说明 


默认免费代理ARP定时发送时间间隔为30秒。  这里配置的发送间隔当启用免费代理ARP的接口较少且接口上配置的代理IP地址不多时是正确的，但是启动免费代理ARP功能的接口很多或当接口上配置了打了的代理IP地址时，免费代理ARP的发送是采用分批的方式。这里配置的发送间隔与实际发送的间隔会存在一些差距，差距的大小由需要发送免费代理ARP的接口数量以及接口上代理IP地址的数量成正比。使用no命令关闭接口定时发送免费代理ARP的功能。命令支持保存重启和主备倒换，show run配置时显示在接口下。在gratuitous-proxy-arp命令未设置开启的情况下，本命令可以设置但是无法起到作用；本命令（gratuitous-proxy-arp periodic）和gratuitous-proxy-arp命令设置顺序不分前后，但只有gratuitous-proxy-arp命令设置完成后，免费ARP代理发送时间间隔设置才能真正起作用 






### 范例 


1、在接口gei-0/1/0/1上配置免费代理ARP报文的定时发送时间间隔为20秒：ZXROSNG(config)#arpZXROSNG(config-arp)# gratuitous-proxy-arp periodic gei-0/1/0/1 202、恢复接口gei-0/1/0/1上配置免费代理ARP报文的定时发送时间间隔为30秒：ZXROSNG(config)#arpZXROSNG(config-arp)# no gratuitous-proxy-arp periodic gei-0/1/0/1





### 相关命令 


gratuitous-proxy-arp 




## gratuitous-proxy-arp periodic 


gratuitous-proxy-arp periodic 




### 命令功能 


该命令工作于ARP接口配置模式下，配置免费代理ARP的定时发送时间。可以通过no命令恢复默认发送时间。当开启接口的免费代理ARP定时发送功能后，会定时使用接口上配置的代理IP地址向外发送免费ARP报文。配置时可以指定免费代理ARP的发送间隔，不指定则默认为30s。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



gratuitous-proxy-arp periodic 
  [＜seconds 
＞]

no gratuitous-proxy-arp periodic 








### 命令参数解释 




参数|描述
---|---
＜seconds＞|接口定时发送免费代理ARP的间隔，范围1~14400，单位秒，默认30s








### 缺省 


不开启定时发送功能。 






### 使用说明 


    默认免费代理ARP定时发送时间间隔为30秒      这里配置的发送间隔当启用免费代理ARP的接口较少且接口上配置的代理IP地址不多时是正确的，但是启动免费代理ARP功能的接口很多或当接口上配置了打了的代理IP地址时，免费代理ARP的发送是采用分批的方式。这里配置的发送间隔与实际发送的间隔会存在一些差距，差距的大小由需要发送免费代理ARP的接口数量以及接口上代理IP地址的数量成正比。    使用no命令关闭接口定时发送免费代理ARP的功能。命令支持保存重启和主备倒换，show run配置时显示在接口下。    在gratuitous-proxy-arp命令未设置开启的情况下，本命令可以设置但是无法起到作用；本命令（gratuitous-proxy-arp periodic）和gratuitous-proxy-arp命令设置顺序不分前后，但只有gratuitous-proxy-arp命令设置完成后，免费ARP代理发送时间间隔设置才能真正起作用 






### 范例 


1、在接口gei-0/1/0/1上配置免费代理ARP报文的定时发送时间间隔为20秒：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# gratuitous-proxy-arp periodic 202、恢复接口gei-0/1/0/1上配置免费代理ARP报文的定时发送时间间隔为30秒：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no gratuitous-proxy-arp periodic





### 相关命令 


gratuitous-proxy-arp 




## gratuitous-proxy-arp 


gratuitous-proxy-arp 




### 命令功能 


该命令工作于ARP配置模式下，在指定接口配置发送免费代理ARP使用的IP地址或地址段，并进行定时发送。可以通过no命令关闭此功能。开启免费ARP代理定时发送功能后，接口将对配置的地址逐一定时发送免费ARP报文，报文的源IP和目的IP使用的配置地址，MAC使用的是接口MAC地址。





### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



gratuitous-proxy-arp 
  ＜interface-name 
＞ ＜begin-ip-address 
＞ ＜end-ip-address 
＞
no gratuitous-proxy-arp 
  ＜interface-name 
＞ {＜begin-ip-address 
＞ ＜end-ip-address 
＞|all 
}
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜begin-ip-address＞|IP地址段的起始值。（ARP协议本身只支持IPV4,所有IPV6相关配置均在ND协议实现，RFC国际通用标准）
＜end-ip-address＞|IP地址段的结束值（ARP协议本身只支持IPV4,所有IPV6相关配置均在ND协议实现，RFC国际通用标准）








### 缺省 


无 






### 使用说明 


默认免费代理ARP定时发送功能关闭。   配置end-ip和begin-ip的差值不能大于128，一个接口上最多支持128个IP地址段，且这些地址段间不能存在包含关系。当配置单个IP地址段时，起始IP与结束IP相同。使用no命令可以指定范围删除已配置在接口上的代理IP地址段，也可以使用all参数删除接口上配置的所有代理IP地址。命令支持保持重启和主备倒换，show run配置时显示在接口下。配置代理IP后，发送免费ARP的时间间隔默认为30秒，自行设置定时时间间隔的命令为：gratuitous-proxy-arp periodic





### 范例 


1、在接口gei-0/1/0/1上配置IP为10.1.1.1到 10.1.1.128地址段的免费代理ARP发送功能：ZXROSNG(config)#arp ZXROSNG(config-arp)# gratuitous-proxy-arp gei-0/1/0/1 10.1.1.1 10.1.1.1282、关闭接口gei-0/1/0/1上配置IP为10.1.1.1到 10.1.1.120地址段的免费代理ARP发送功能：ZXROSNG(config)#arp ZXROSNG(config-arp)# no gratuitous-proxy-arp gei-0/1/0/1 10.1.1.1 10.1.1.1203、关闭接口gei-0/1/0/1上所有配置带来发送免费ARP的地址：ZXROSNG(config)#arpZXROSNG(config-arp)#no gratuitous-proxy-arp gei-0/1/0/1 all






### 相关命令 


gratuitous-proxy-arp periodic 




## gratuitous-proxy-arp 


gratuitous-proxy-arp 




### 命令功能 


该命令工作于ARP配置模式下，在指定接口配置发送免费代理ARP使用的IP地址或地址段，并进行定时发送。可以通过no命令关闭此功能。开启免费ARP代理定时发送功能后，接口将对配置的地址逐一定时发送免费ARP报文，报文的源IP和目的IP使用的配置地址，MAC使用的是接口MAC地址。





### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



gratuitous-proxy-arp 
  ＜begin-ip-address 
＞ ＜end-ip-address 
＞
no gratuitous-proxy-arp 
  {＜begin-ip-address 
＞ ＜end-ip-address 
＞|all 
}
				






### 命令参数解释 




参数|描述
---|---
＜begin-ip-address＞|IP地址段的起始值。（ARP协议本身只支持IPV4,所有IPV6相关配置均在ND协议实现，RFC国际通用标准）
＜end-ip-address＞|IP地址段的结束值（ARP协议本身只支持IPV4,所有IPV6相关配置均在ND协议实现，RFC国际通用标准）








### 缺省 


无 






### 使用说明 


默认免费代理ARP定时发送功能关闭。   配置end-ip和begin-ip的差值不能大于128，一个接口上最多支持128个IP地址段，且这些地址段间不能存在包含关系。当配置单个IP地址段时，起始IP与结束IP相同。使用no命令可以指定范围删除已配置在接口上的代理IP地址段，也可以使用all参数删除接口上配置的所有代理IP地址。命令支持保持重启和主备倒换，show run配置时显示在接口下。配置代理IP后，发送免费ARP的时间间隔默认为30秒，自行设置定时时间间隔的命令为：gratuitous-proxy-arp periodic





### 范例 


1、在接口gei-0/1/0/1上配置IP为10.1.1.1到 10.1.1.128地址段的免费代理ARP发送功能： ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# gratuitous-proxy-arp 10.1.1.1 10.1.1.1282、关闭接口gei-0/1/0/1上配置IP为10.1.1.1到 10.1.1.120地址段的免费代理ARP发送功能： ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no gratuitous-proxy-arp 10.1.1.1 10.1.1.1203、关闭接口gei-0/1/0/1上所有配置带来发送免费ARP的地址：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no gratuitous-proxy-arp all






### 相关命令 


gratuitous-proxy-arp periodic 




## inspection 


inspection 




### 命令功能 


使能ARP DAI检测，使能该命令，对于ARP报文进行检查。检查内容为：1、ARP报文的源MAC、目的MAC是否与二层头里的源MAC目的MAC相符合，否则报文被丢弃；2、源IP和目的IP是否合法，否则报文被丢弃；3、查询用户是否为合法用户，源IP和源MAC查snooping表，查询成功认为是合法用户，否则报文丢弃。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




inspection 
  {enable 
|disable 
}







### 命令参数解释 




参数|描述
---|---
enable|打开ARP DAI检测功能
disable|关闭ARP DAI检测功能








### 缺省 


缺省ARP DAI检测不打开。 






### 使用说明 


无 






### 范例 


1、使能接口gei-0/1/0/1的ARP DAI检测功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)# inspection enable2、关闭接口gei-0/1/0/1的ARP DAI检测功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-gei-0/1/0/1)# inspection disable





### 相关命令 


无 




## interface 


interface (ARP模式) 




### 命令功能 


该命令工作于ARP配置模式下，用于进入ARP接口配置模式。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 




interface 
  ＜interface-name 
＞







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于进入ARP接口配置模式，通过接口模块命令show ip interface brief可获取接口名。








### 缺省 


无 






### 使用说明 


通过该命令从ARP配置模式进入ARP接口配置模式 






### 范例 


从ARP配置模式中进入接口名为gei-0/1/0/1的ARP接口配置模式，则输入以下命令：ZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#





### 相关命令 


无 




## inter-vlan-proxy 


inter-vlan-proxy 




### 命令功能 


设置相同接口，不同vlan间ARP代理功能 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




inter-vlan-proxy 
 

no inter-vlan-proxy 








### 命令参数解释 



					无
				 






### 缺省 


缺省接口下关闭vlan间ARP代理 






### 使用说明 


使用no命令恢复默认值 






### 范例 


1、设置接口gei-0/1/0/1.1不同vlan间ARP代理开关：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1.1ZXROSNG(config-arp-if-gei-0/1/0/1.1)#inter-vlan-proxy2、恢复默认值：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1.1ZXROSNG(config-arp-if-gei-0/1/0/1.1)#no inter-vlan-proxy





### 相关命令 


无 




## learn-disable 


learn-disable 




### 命令功能 


该命令工作于ARP配置模式下，禁止ARP学习功能。可以通过no命令来恢复其学习功能。关闭ARP学习的情况下，将不再进行ARP条目的学习和添加。比如对于ARP的请求报文，关闭ARP学习后，就只进行回应，而对请求报文中的源地址将不在进行ARP条目添加和学习。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



learn-disable 
  ＜interface-name 
＞
no learn-disable 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


缺省开启ARP学习功能 






### 使用说明 


默认开启ARP学习功能。开启ARP学习的情况下，只要符合条件，就进行目的ARP条目的学习和添加。





### 范例 


1、关闭接口gei-0/1/0/1的ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)# learn-disable gei-0/1/0/12、开启接口gei-0/1/0/1的ARP学习功能：ZXROSNG(config)#arpZXROSNG(config-arp)# no learn-disable gei-0/1/0/1





### 相关命令 


无 




## learn-disable 


learn-disable 




### 命令功能 


该命令工作于ARP接口配置模式下，禁止ARP学习功能。可以通过no命令来恢复其学习功能。关闭ARP学习的情况下，将不再进行ARP条目的学习和添加。比如对于ARP的请求报文，关闭ARP学习后，就只进行回应，而对请求报文中的源地址将不在进行ARP条目添加和学习。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




learn-disable 
 

no learn-disable 








### 命令参数解释 



					无
				 






### 缺省 


缺省开启ARP学习功能 






### 使用说明 


默认开启ARP学习功能开启ARP学习的情况下，只要符合条件，就进行目的ARP条目的学习和添加。





### 范例 


关闭接口gei-0/1/0/1的ARP学习功能： ZXROSNG(config-arp-if-gei-0/1/0/1)# learn-disable 开启接口gei-0/1/0/1的ARP学习功能：ZXROSNG(config-arp-if-gei-0/1/0/1)# no learn-disable






### 相关命令 


无 




## learn-limit 


learn-limit 




### 命令功能 


该命令工作于ARP配置模式下，打开指定接口的ARP学习限制功能。可以通过no命令关闭此功能。学习限制功能打开后，对于收到的ARP请求报文，只进行应答回应，而不进行ARP条目学习；对于收到的ARP应答报文，除了自己发出请求收到的应答，其它应答报文不进行处理。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



learn-limit 
  ＜interface-name 
＞
no learn-limit 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


默认ARP的学习限制功能关闭。 






### 使用说明 


show running-config时会在对应的接口下显示配置结果，全局下不会显示。 






### 范例 


1、开启接口gei-0/1/0/1的ARP学习限制功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp)# learn-limit gei-0/1/0/12、关闭接口gei-0/1/0/1的ARP学习限制功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp)# no learn-limit gei-0/1/0/1





### 相关命令 


无 




## learn-limit 


learn-limit 




### 命令功能 


该命令工作于ARP接口配置模式下，打开指定接口的ARP学习限制功能。可以通过no命令关闭此功能。学习限制功能打开后，对于收到的ARP请求报文，只进行应答回应，而不进行ARP条目学习；对于收到的ARP应答报文，除了自己发出请求收到的应答，其它应答报文不进行处理。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



learn-limit 
 

no learn-limit 








### 命令参数解释 



					无
				 






### 缺省 


默认ARP的学习限制功能关闭。 






### 使用说明 


show running-config时会在对应的接口下显示配置结果，全局下不会显示。 






### 范例 


1、开启接口gei-0/1/0/1的ARP学习限制功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# learn-limit2、关闭接口gei-0/1/0/1的ARP学习限制功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no learn-limit





### 相关命令 


无 




## limit-time 


limit-time 




### 命令功能 


该命令工作于ARP接口配置模式下，设置ARP报文抑制时间。no命令恢复抑制时间为默认值。设置ARP报文抑制速度上限的情况下，如果一秒种内指定接口处理的ARP报文数量达到了配置的上限值，那么在抑制时间内指定接口将不再进行任何ARP报文的处理，直到抑制时间结束，恢复正常报文处理流程。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



limit-time 
  ＜seconds 
＞

no limit-time 








### 命令参数解释 




参数|描述
---|---
＜seconds＞|设置接口ARP报文抑制时间，单位为秒，范围为0-1000。默认值：10秒。








### 缺省 


缺省ARP报文抑制时间是10秒 






### 使用说明 


默认ARP报文抑制时间为10秒。 在port-speed命令未设置开启的情况下，本命令可以设置但是无法起到作用；本命令（limit-time）和port-speed命令设置顺序不分前后，但只有port-speed命令设置完成后，报文抑制功能才能正常工作。仅适用于各路由器系列。






### 范例 


1、设置接口gei-0/1/0/1的ARP报文抑制时间值为20秒：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#port-speed 30ZXROSNG(config-arp-if-gei-0/1/0/1)# limit-time 202、恢复接口gei-0/1/0/1的ARP报文抑制时间值为10秒：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no limit-time





### 相关命令 


port-speed 




## limit-time 


limit-time 




### 命令功能 


该命令工作于ARP配置模式下，设置ARP报文抑制时间。no命令恢复抑制时间为默认值。设置ARP报文抑制速度上限的情况下，如果一秒种内指定接口处理的ARP报文数量达到了配置的上限值，那么在抑制时间内指定接口将不再进行任何ARP报文的处理，直到抑制时间结束，恢复正常报文处理流程。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



limit-time 
  ＜interface-name 
＞ ＜seconds 
＞
no limit-time 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜seconds＞|设置接口ARP报文抑制时间，单位为秒，范围<0-1000>








### 缺省 


缺省ARP报文抑制时间是10秒 






### 使用说明 


默认ARP报文抑制时间为10秒。 在port-speed命令未设置开启的情况下，本命令可以设置但是无法起到作用；本命令（limit-time）和port-speed命令设置顺序不分前后，但只有port-speed命令设置完成后，报文抑制功能才能正常工作。仅适用于路由器。






### 范例 


1、设置接口gei-0/1/0/1的ARP报文抑制时间值为20秒：ZXROSNG(config)#arpZXROSNG(config-arp)#port-speed gei-0/1/0/1 30ZXROSNG(config-arp)# limit-time gei-0/1/0/1 202、恢复接口gei-0/1/0/1的ARP报文抑制时间值为10秒：ZXROSNG(config)#arpZXROSNG(config-arp)# no limit-time gei-0/1/0/1





### 相关命令 


port-speed 




## local-proxy-arp 


local-proxy-arp 




### 命令功能 


配置同一接口下ARP代理功能，可以通过no命令来取消其代理功能。ARP本地代理：与ARP代理一样，对于ROSNG平台的区别在于，ARP代理是对请求目的出口地址在不同接口的代理，ARP本地代理是对请求目的地址的出口在相同接口的代理。ARP代理： 对于没有配置缺省网关的计算机要和其他网络中的计算机实现通信，网关收到源计算机的 ARP 请求会使用自己的 MAC 地址与目标计算机的 IP地址对源计算机进行应答。





### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



local-proxy-arp 
 

no local-proxy-arp 








### 命令参数解释 



					无
				 






### 缺省 


默认不进行同一接口下ARP代理 






### 使用说明 


默认不进行同一接口下ARP代理。 






### 范例 


1、配置接口的本地ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#local-proxy-arp2、关闭接口的本地ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no local-proxy-arp





### 相关命令 


无 




## local-proxy-arp 


local-proxy-arp 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口的ARP本地代理功能。使用no命令将取消其本地代理功能。ARP本地代理：与ARP代理一样，对于ROSNG平台的区别在于，ARP代理是对请求目的出口地址在不同接口的代理，ARP本地代理是对请求目的地址的出口在相同接口的代理。ARP代理： 对于没有配置缺省网关的计算机要和其他网络中的计算机实现通信，网关收到源计算机的 ARP 请求会使用自己的 MAC 地址与目标计算机的 IP地址对源计算机进行应答。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



local-proxy-arp 
  ＜interface-name 
＞
no local-proxy-arp 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


默认不进行同一接口下ARP代理 






### 使用说明 


默认不开启ARP本地代理功能。开启ARP代理后，接口若收到符合ARP本地代理要求的ARP请求报文，则进行代理应答。





### 范例 


1、开启接口gei-0/1/0/1的ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)# local-proxy-arp gei-0/1/0/12、关闭接口gei-0/1/0/1的ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)# no local-proxy-arp gei-0/1/0/1





### 相关命令 


无 




## periodic freearp 


periodic freearp 




### 命令功能 


该命令工作于ARP配置模式下，打开接口的定期免费ARP报文发送功能。通过no命令可以关闭该功能。该命令可以带发送周期参数，也可不带周期参数，若不带周期参数默认30秒发送一次。免费ARP：即源IP和目的IP都为自身的广播类型ARP报文，用于通告它人自身最新IP地址，以防止IP地址冲突。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



periodic freearp 
  ＜interface-name 
＞ [＜seconds 
＞]
no periodic freearp 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜seconds＞|设置接口定期发送免费ARP报文的时间间隔，单位是秒，范围为10-14400。默认值：30秒








### 缺省 


缺省免费ARP周期发送功能关闭。在使能免费ARP周期发送的情况下，默认免费ARP发送的时间间隔是30秒。 






### 使用说明 


默认不发送接口免费ARP报文。打开发送接口免费ARP报文发送开关后，默认免费发送时间间隔为30秒。仅适用于各路由器系列。






### 范例 


1、开启接口gei-0/1/0/1的免费ARP定时发送功能：ZXROSNG(config)#arpZXROSNG(config-arp)#periodic freearp gei-0/1/0/12、设置接口gei-0/1/0/1的免费ARP定时发送时间间隔为50秒：ZXROSNG(config)#arpZXROSNG(config-arp)#periodic freearp gei-0/1/0/1 503、关闭接口gei-0/1/0/1的免费ARP定时发送功能：ZXROSNG(config)#arpZXROSNG(config-arp)# no periodic freearp  gei-0/1/0/1





### 相关命令 


无 




## periodic freearp 


periodic freearp 




### 命令功能 


该命令工作于ARP接口配置模式下，打开接口的定期免费ARP报文发送功能。通过no命令可以关闭该功能。该命令可以带发送周期参数，也可不带周期参数，若不带周期参数默认30秒发送一次。免费ARP：即源IP和目的IP都为自身的广播类型ARP报文，用于通告它人自身最新IP地址，以防止IP地址冲突。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



periodic freearp 
  [＜seconds 
＞]

no periodic freearp 








### 命令参数解释 




参数|描述
---|---
＜seconds＞|设置接口定期发送免费ARP报文的时间间隔，单位是秒，范围为10-14400。默认值：30秒








### 缺省 


缺省免费ARP周期发送功能关闭。在使能免费ARP周期发送的情况下，默认免费ARP发送的时间间隔是30秒。 






### 使用说明 


如果不指定发送免费ARP报文的时间间隔，接口的定期发送免费ARP报文的时间间隔默认值是30秒。仅适用于各路由器系列。 






### 范例 


1、开启接口gei-0/1/0/1的免费ARP定时发送功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#periodic freearp2、设置接口gei-0/1/0/1的免费ARP定时发送时间间隔为50秒：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#periodic freearp 503、关闭接口gei-0/1/0/1的免费ARP定时发送功能：：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no periodic freearp





### 相关命令 


无 




## port-speed 


port-speed 




### 命令功能 


该命令工作于ARP接口配置模式下，：设置ARP接口报文抑制速度，当收到的ARP报文速率达到抑制上限时，在ARP抑制时间内不进行ARP报文处理。开启ARP报文抑制速度的情况下，如果一秒种内指定接口处理的ARP报文数量达到了配置的上限值，那么在抑制时间内指定接口将不再进行任何ARP报文的处理，直到抑制时间结束，恢复正常报文处理流程。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



port-speed 
  ＜packets-number-per-second 
＞

no port-speed 








### 命令参数解释 




参数|描述
---|---
＜packets-number-per-second＞|报文抑制速度上限值，范围为1-1000，单位：个。默认值：无








### 缺省 


缺省不进行ARP报文速度抑制 






### 使用说明 


使用该命令开启报文速度抑制功能后，默认的抑制时间是10秒钟，抑制时间可使用limit-time配置。仅适用于路由器项目。 






### 范例 


1、设置接口gei-0/1/0/1的ARP报文抑制速度上限值为10：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# port-speed 102、关闭接口gei-0/1/0/1的ARP报文抑制功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# no port-speed





### 相关命令 


limit-time 




## port-speed 


port-speed 




### 命令功能 


设置ARP接口报文抑制速度，当收到的ARP报文速率达到抑制上限时，在ARP抑制时间内不进行ARP报文处理。no命令删除该配置。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



port-speed 
  ＜interface-name 
＞ ＜packets-number-per-second 
＞
no port-speed 
  ＜interface name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|接口名
＜packets-number-per-second＞|设置的接口收发ARP报文的上限，单位为个/秒，范围<1-1000>






No参数|描述
---|---
＜interface name＞|接口名








### 缺省 


缺省不进行ARP报文速度抑制 






### 使用说明 


使用该命令开启报文速度抑制功能后，默认的抑制时间是10秒钟，抑制时间可使用limit-time配置。仅适用于路由器项目。 






### 范例 


1、配置接口gei-0/1/0/1的ARP报文抑制速度上限：ZXROSNG(config)#arpZXROSNG(config-arp)#port-speed gei-0/1/0/1 882、关闭接口gei-0/1/0/1的ARP报文速度抑制功能：ZXROSNG(config)#arpZXROSNG(config-arp)#no port-speed gei-0/1/0/1





### 相关命令 


limit-time 




## protect common-mac 


protect common-mac 




### 命令功能 


配置所有MAC的ARP保护功能，可以通过no命令去除所有MAC 的ARP保护功能。开启所有MAC的ARP保护功能后，如果在某一MAC学习到的ARP条目数达到配置上限，不允许通过ARP报文学习新的ARP条目。如果同时配置了特殊MAC保护，此命令不生效。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 




protect common-mac 
 limit-num 
 ＜protect-limit-number 
＞

no protect common-mac 








### 命令参数解释 




参数|描述
---|---
＜protect-limit-number＞|设置所有MAC的ARP保护条目上限，范围为1-$#67239942#$








### 缺省 


不进行所有MAC的ARP保护限制 






### 使用说明 


默认不进行所有MAC的ARP保护限制。 






### 范例 


1、配置ARP的所有MAC保护阈值为1000:ZXROSNG(config)#arpZXROSNG(config-arp)#protect common-maclimit-num 10002、关闭ARP的所有MAC保护功能:ZXROSNG(config)#arpZXROSNG(config-arp)#no protect common-mac





### 相关命令 


无 




## protect interface 


protect interface 




### 命令功能 


该命令工作于ARP配置模式下，配置ARP的保护功能。可以通过no命令去除ARP保护功能。配置ARP保护功能后，如果在此接口学习的ARP条目数达到配置上限，不允许该接口通过ARP报文学习新的ARP条目。ARP保护功能：指当前设备中保存ARP条目的数目上限，如果ARP条目数达到配置上限，则不允许通过ARP报文学习新的ARP条目。





### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



protect interface 
  ＜interface-name 
＞ limit-num 
 ＜protect-limit-number 
＞
no protect interface 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|表示配置基于接口的保护。输入对应接口名，对此接口进行保护。
＜protect-limit-number＞|设置的ARP保护条目上限，范围为1-$#67239942#$








### 缺省 


不进行接口ARP保护限制。 






### 使用说明 


基于接口模式：该接口学习ARP条目上限数目； 






### 范例 


1、在ARP配置模式下，配置接口gei-0/1/0/1的ARP保护阈值为1000：ZXROSNG(config)#arpZXROSNG(config-arp)#protect interface gei-0/1/0/1 limit-num 10002、在ARP配置模式下，去除接口gei-0/1/0/1的ARP保护限制：ZXROSNG(config)#arpZXROSNG(config-arp)#no protect interface gei-0/1/0/1





### 相关命令 


无 




## protect special-mac 


protect special-mac 




### 命令功能 


配置指定MAC的ARP保护功能，可以通过no命令去除指定MAC 的ARP保护功能。开启指定MAC的ARP保护功能后，如果ARP条目数达到配置上限，不允许通过ARP报文学习新的ARP条目 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



protect special-mac 
  ＜mac-address 
＞ limit-num 
 ＜protect-limit-number 
＞
no protect special-mac 
  ＜mac-address 
＞
				






### 命令参数解释 




参数|描述
---|---
＜mac-address＞|表示基于特定MAC地址的ARP条目个数保护。输入对应的MAC地址，采用点分十六进制形式。
＜protect-limit-number＞|设置的ARP保护条目上限,范围为1-$#67239942#$








### 缺省 


不进行特定MAC的ARP保护限制 






### 使用说明 


默认不进行特定MAC的ARP保护限制。如果同时配置普通MAC保护和特殊MAC保护，对于所指定的MAC地址，特殊MAC地址优先级高，即达到指定MAC地址保护上限就不能进行ARP学习。ARP保护的主要应用为：可根据使用需要，设定学习ARP上限值，不至于在ARP报文过多的情况下，不停的刷新ARP表；另外可保证设备上ARP条目总数，可按用户要求进行分配，不至于一个MAC地址或一个接口占用过多空间而影响其它接口和MAC地址的学习。






### 范例 


1、配置ARP的特定MAC保护阈值为1000:ZXROSNG(config)#arpZXROSNG(config-arp)#protect special-mac 0010.0020.0030 limit-num 10002、关闭ARP的特定MAC保护功能:ZXROSNG(config)#arpZXROSNG(config-arp)#no protect special-mac 0010.0020.0030






### 相关命令 


无 




## protect whole 


protect whole 




### 命令功能 


配置全局的ARP保护功能，可以通过no命令去除全局的ARP保护功能。开启全局的ARP保护功能后，如果ARP条目数达到配置上限，不允许通过ARP报文学习新的ARP条目 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 




protect whole 
 limit-num 
 ＜protect-limit-number 
＞

no protect whole 








### 命令参数解释 




参数|描述
---|---
＜protect-limit-number＞|设置全局的ARP保护条目上限，范围为1-$#67239942#$








### 缺省 


不进行全局的ARP保护限制 






### 使用说明 


默认不进行全局的ARP保护限制。 






### 范例 


1、配置ARP的全局保护阈值为1000:ZXROSNG(config)#arpZXROSNG(config-arp)#protect whole limit-num 10002、关闭ARP的全局保护功能:ZXROSNG(config)#arpZXROSNG(config-arp)#no protect whole





### 相关命令 


无 




## protect 


protect 




### 命令功能 


该命令工作于ARP接口配置模式下，为配置ARP的接口保护功能。可以通过no命令关闭接口保护。开启该接口的ARP保护功能后，如果在此接口学习的ARP条目数达到配置上限，不允许该接口通过ARP报文学习新的ARP条目，配置静态ARP不受限制。ARP接口保护功能：如果该接口下ARP条目数达到配置上限，不允许该接口通过ARP报文学习新的ARP条目。





### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



protect 
 limit-num 
 ＜protect-limit-number 
＞

no protect 








### 命令参数解释 




参数|描述
---|---
＜protect-limit-number＞|设置的ARP保护条目上限，范围为1-$#67239942#$








### 缺省 


不进行ARP保护限制 






### 使用说明 


根据参数可以分别基于接口来对ARP进行保护的设置, 默认不进行ARP条目的保护 






### 范例 


1、在ARP接口配置模式下，配置接口gei-0/1/0/1的学习条目保护上限为1000，则输入以下命令：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#protect limit-num 10002、在ARP接口配置模式下，对接口gei-0/1/0/1去除学习条目保护上限，则输入以下命令：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no protect





### 相关命令 


无 




## proxy local 


proxy local 




### 命令功能 


配置开启到loopback接口的ARP代理功能。当loopback口上IP地址与机架上另一个A接口IP地址之间符合网段包含关系时（即loopback口上IP地址网段包含A接口IP地址网段，比如loopback口地址为1.1.1.1，掩码为16位，另一个接口地址为1.1.5.7掩码为24位），远端从A接口请求loopback口的IP地址对应的AR条目P时，由A接口对远端进行ARP代理应答。可以通过no命令来取消其代理功能。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




proxy local 
 

no proxy local 








### 命令参数解释 



					无
				 






### 缺省 


默认不开启到loopback接口的 ARP代理功能。 






### 使用说明 


默认不开启到loopback接口的 ARP代理功能。show run时会在对应的接口下显示配置结果，全局下不会显示。只在XGW项目上支持。






### 范例 


1、配置接口gei-0/1/0/1的到loopback接口的ARP代理功能:ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#proxy local2、关闭接口gei-0/1/0/1的到loopback接口的ARP代理功能:ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no proxy local






### 相关命令 


无 




## proxy local 


proxy local 




### 命令功能 


该命令工作于ARP配置模式下，当loopback口上IP地址与机架上另一个A接口IP地址之间符合网段包含关系时（即loopback口上IP地址网段包含A接口IP地址网段，比如loopback口地址为1.1.1.1，掩码为16位，另一个接口地址为1.1.5.7掩码为24位），远端从A接口请求loopback口的IP地址对应的AR条目P时，由A接口对远端进行ARP代理应答。可以通过no命令来关闭此功能。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



proxy local 
  ＜interface-name 
＞
no proxy local 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


默认不开启到loopback接口的ARP代理功能。 






### 使用说明 


默认不开启到loopback接口的 ARP代理功能。show run时会在对应的接口下显示配置结果，全局下不会显示。只在XGW项目上支持。






### 范例 


1、配置接口gei-0/1/0/1到loopback接口的ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)# proxy local gei-0/1/0/12、关闭接口gei-0/1/0/1到loopback接口的ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)#no  proxy local gei-0/1/0/1





### 相关命令 


无 




## proxy 


proxy 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口的ARP代理功能。使用no命令将取消其代理功能。ARP代理： 对于没有配置缺省网关的计算机要和其他网络中的计算机实现通信，网关收到源计算机的 ARP 请求会使用自己的 MAC 地址与目标计算机的 IP地址对源计算机进行应答。





### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



proxy 
  ＜interface-name 
＞
no proxy 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


默认不进行ARP代理 






### 使用说明 


默认不开启ARP代理功能。开启ARP代理后，接口若收到符合代理要求的ARP请求报文，则进行代理应答。





### 范例 


1、开启接口gei-0/1/0/1的ARP代理功能：ZXROSNG(config)#arp ZXROSNG(config-arp)# proxy gei-0/1/0/12、关闭接口gei-0/1/0/1的ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)#no proxy gei-0/1/0/1





### 相关命令 


无 




## proxy 


proxy 




### 命令功能 


该命令工作于ARP接口配置模式下，配置指定接口的ARP代理功能。使用no命令将取消其代理功能。ARP代理： 对于没有配置缺省网关的计算机要和其他网络中的计算机实现通信，网关收到源计算机的 ARP 请求会使用自己的 MAC 地址与目标计算机的 IP地址对源计算机进行应答。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



proxy 
 

no proxy 








### 命令参数解释 



					无
				 






### 缺省 


默认不进行ARP代理 






### 使用说明 


默认不开启ARP代理功能。开启ARP代理后，接口若收到符合ARP代理要求的ARP请求报文，则进行代理应答。






### 范例 


1、开启接口gei-0/1/0/1的ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# proxy2、关闭接口gei-0/1/0/1的ARP代理功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no proxy 






### 相关命令 


无 




## purge-delay 


purge-delay 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口协议DOWN时动态ARP条目的延迟清除时间。可以通过no命令来恢复默认延迟清除值。本命令主要应用：接口DOWN后，如果接口再UP时，则不用重新学习之前接口学习到的ARP，保证其它应用协议需要查ARP表时，不会出错，所以进行了ARP条目的延迟删除。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



purge-delay 
  ＜interface-name 
＞ ＜seconds 
＞
no purge-delay 
  ＜interface-name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜seconds＞|要设置的清除时间，单位为秒，范围为1-36000。默认值：600秒（ROSNG平台）。








### 缺省 


默认清除时间由各项目性能参数值规定，平台默认延迟删除事件为600秒。本命令不可关闭，只可配置延迟删除时间的长短





### 使用说明 


设置接口协议down时，接口上ARP条目的清除时间，默认时间取项目定制值，若项目没有定制则取平台默认600秒。 






### 范例 


1、配置接口gei-0/1/0/1协议down后，ARP的清除时间为1000秒：ZXROSNG(config)#arpZXROSNG(config-arp)#purge-delay gei-0/1/0/1 10002、接口gei-0/1/0/1协议down后，恢复ARP的清除时间为默认值：ZXROSNG(config)#arpZXROSNG(config-arp)#no purge-delay gei-0/1/0/1





### 相关命令 


无 




## purge-delay 


purge-delay 




### 命令功能 


该命令工作于ARP接口配置模式下，配置指定接口协议DOWN时动态ARP条目的延迟清除时间。可以通过no命令来恢复默认延迟清除值。本命令主要应用：接口DOWN后，如果接口再UP时，则不用重新学习之前接口学习到的ARP，保证其它应用协议需要查ARP表时，不会出错，所以进行了ARP条目的延迟删除。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



purge-delay 
  ＜seconds 
＞

no purge-delay 








### 命令参数解释 




参数|描述
---|---
＜seconds＞|要设置的清除时间，单位为秒，范围为1-36000。默认值：600秒（ROSNG平台）。








### 缺省 


缺省600秒 






### 使用说明 


设置接口协议down时，接口上ARP条目的清除时间，默认时间是600秒。 






### 范例 


配置接口gei-0/1/0/1协议DOWN后，ARP的清除时间为1000秒： ZXROSNG(config-arp-if-gei-0/1/0/1)#purge-delay 1000恢复接口gei-0/1/0/1协议DOWN后，ARP的清除时间为默认值：ZXROSNG(config-arp-if-gei-0/1/0/1)#no purge-delay 






### 相关命令 


无 




## show arp statistics 


show arp statistics 




### 命令功能 


该命令工作于特权模式下，显示基于接口的报文统计总数。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show arp statistics 
  [＜interface-name 
＞ [detail 
]] 







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
detail|丢包详细信息








### 缺省 


无 






### 使用说明 


显示基于接口的报文统计计数。仅支持路由器。 






### 范例 


ZXROSNG#show arp statistics Interface                    Rcv_packets  Err_packets-----------------------------------------------------------gei-0/1/0/1                      0            0gei-0/1/0/2                      2            0gei-0/1/0/3                      0            0gei-0/1/0/4                      0            0gei-0/1/0/5                      0            0gei-0/1/0/6                      0            0gei-0/1/0/7                      0            0gei-0/1/0/8                      0            0mgmt_eth                     44           44显示gei-0/1/0/2接口的报文接受信息：ZXROSNG#show arp statistics gei-0/1/0/2        Interface                        Rcv_packets  Err_packets-----------------------------------------------------------gei-0/1/0/2                      2            0显示接口gei-0/1/0/1上的报文统计计数:ZXROSNG#show arp statistics gei-0/1/0/1 detailARP packet receive:0ARP packet drop for limit number:0ARP packet drop for source filter:0ARP packet drop for learn limit:0ARP packet drop for speed:0ARP packet drop for others:0






### 相关命令 


clear arp statistics 




## show arp 


show arp 




### 命令功能 


该命令可工作于任何置模式下，按要求显示ARP条目。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


除用户模式外的其他所有模式:15,用户模式:1 






### 命令格式 




show arp 
  [{{dynamic 
|static 
|permanent 
|arp-to-static 
} [＜interface-name 
＞]|＜ip-address 
＞|interface 
 ＜interface-name 
＞ [{＜ip-address 
＞ [detail 
]|＜mac-address 
＞}]|vlan 
 {intervlanid 
 ＜internal-vlan-id 
＞ [extervlanid 
 ＜external-vlan-id 
＞]|extervlanid 
 ＜external-vlan-id 
＞}|ip-range 
 from 
 ＜begin-ip-address-of-range 
＞ to 
 ＜end-ip-address-of-range 
＞|vrf 
 ＜vrf-name 
＞}] [{include 
 ＜ip-or-mac-regular-expression 
＞|exclude 
 ＜ip-or-mac-regular-expression 
＞|begin 
 ＜ip-or-mac-regular-expression 
＞}] 







### 命令参数解释 




参数|描述
---|---
dynamic|显示动态ARP条目
static|显示静态类型条目
permanent|显示permanent属性ARP条目
arp-to-static|显示arp-to-static属性ARP条目
＜interface-name＞|接口名。显示指定接口下所有ARP条目。
＜ip-address＞|IP地址（ARP协议本身只支持IPV4,所有IPV6相关配置均在ND协议实现，RFC国际通用标准）
＜interface-name＞|接口名。显示指定接口下所有ARP条目。
＜ip-address＞|IP地址（ARP协议本身只支持IPV4,所有IPV6相关配置均在ND协议实现，RFC国际通用标准）
detail|显示该ARP条目具体的各个属性值
＜mac-address＞|MAC地址，用户需要显示ARP条目中对应MAC地址。
＜internal-vlan-id＞|ARP条目的内层vlanid
＜external-vlan-id＞|ARP条目的外层vlanid
＜external-vlan-id＞|ARP条目的外层vlanid
＜begin-ip-address-of-range＞|IP范围的下限
＜end-ip-address-of-range＞|IP范围的上限
＜vrf-name＞|VRF名。显示该VRF的所用ARP条目。
include|显示包含IP或者MAC地址模糊表达式的ARP
＜ip-or-mac-regular-expression＞|IP或者MAC模糊表达式
exclude|显示不包含IP或者MAC地址模糊表达式的ARP
＜ip-or-mac-regular-expression＞|IP或者MAC模糊表达式
begin|显示符合IP或者MAC模糊表达式的ARP以及之后的ARP
＜ip-or-mac-regular-expression＞|IP或者MAC模糊表达式








### 缺省 


无 






### 使用说明 


无 






### 范例 


ZXROSNG(config-if-gei-0/1/0/1)#show arpArp protect whole is disabled The count is 4IP                     Hardware                    Exter  Inter  SubAddress         Age     Address        Interface    VlanID VlanID Interface1.0.0.1         H        0016.3e64.0105 gei-0/1/0/1  N/A    N/A    N/A1.0.0.2         00:00:04 0016.3e64.0305 gei-0/1/0/1  N/A    N/A    gei-0/1/0/1172.1.1.1       B        0016.3e64.0105 irb1         N/A    N/A    irb1表头解释：IP Address: ARP条目下一条IP地址。Age：ARP条目生存时间。Hardware Address: MAC地址。Interface: 接口名称。Exter VlanID：外层VLAN ID。Inter VlanID：内层VLAN ID。Sub Interface: 出接口名称。ZXROSNG(config-if-gei-0/1/0/1)#show arp interface gei-0/1/0/1 1.0.0.2 detail ARP IP address : 1.0.0.2ARP item age : 00:00:00ARP MAC address : 0016.3e64.0305ARP interface : gei-0/1/0/1ARP physical interface : gei-0/1/0/1ARP item attribute : NORMALARP item class : N/AARP learn time stamp : 11761ARP learn IP address : 1.0.0.1ARP item VRF : N/AARP data source : Local     ARP CPS trust : N/AARP VTEP interface : gei-0/1/0/1ARP VXLAN instance ID : 1ARP VPLS instace ID：0ARP tunnel ID : 1ARP remote IP : N/A





### 相关命令 


arpto-staticclear arp-cache




## show debug arp 


show debug arp 




### 命令功能 


该命令工作于特权模式下，显示ARP的debug信息。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show debug arp 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


无 






### 范例 


查看ARP的DEBUG信息：ZXROSNG#show debug arp   ARP:  ARP packets trace send source ip 1.1.1.1 debugging is on  ARP packets trace receive destination ip 1.1.1.1 debugging is on  ARP packets interface gei-0/1/0/2 debugging is on





### 相关命令 


debug arp 




## show debug 


show debug 




### 命令功能 


该命令工作于特权模式下，显示ARP的debug信息。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show debug 
 







### 命令参数解释 



					无
				 






### 缺省 


缺省不开启ARP的DEBUG信息 






### 使用说明 


使用sho debug arp 命令查看ARP模块当前DEBUG信息 






### 范例 


查看ARP的DEBUG信息：ZXROSNG#show debug arp   ARP:  ARP packets trace send source ip 1.1.1.1 debugging is on  ARP packets trace receive destination ip 1.1.1.1 debugging is on  ARP packets interface gei-0/1/0/2 debugging is on






### 相关命令 


debug arp packets interface 




## source-filtered 


source-filtered 




### 命令功能 


该命令工作于ARP配置模式下，打开接口的源地址过滤功能。通过可选参数disable关闭该功能。开启ARP源过滤的情况下，将先进行报文内容检测，对于收到的ARP报文，如果查找不到报文中源地址的路由，那么就丢弃报文，不进行进一步处理；关闭ARP源过滤的情况下，将不进行该项报文内容检测，进行正常流程处理。






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 



source-filtered 
  [disable 
]






### 命令参数解释 




参数|描述
---|---
disable|设置无效








### 缺省 


缺省开启源地址过滤功能 






### 使用说明 


使用source-filtered 开启源地址过滤功能；使用source-filtered disable关闭源地址过滤功能。 






### 范例 


1、开启接口gei-0/1/0/1的ARP源地址过滤功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# source-filtered 2、关闭接口gei-0/1/0/1的ARP源地址过滤功能：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)# source-filtered disable





### 相关命令 


无 




## source-filtered 


source-filtered 




### 命令功能 


该命令工作于ARP配置模式下，打开接口的源地址过滤功能。通过可选参数disable关闭该功能。开启ARP源过滤的情况下，将先进行报文内容检测，对于收到的ARP报文，如果查找不到报文中源地址的路由，那么就丢弃报文，不进行进一步处理；关闭ARP源过滤的情况下，将不进行该项报文内容检测，进行正常流程处理。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



source-filtered 
  ＜interface-name 
＞ [disable 
]






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
disable|设置无效








### 缺省 


缺省开启源地址过滤功能 






### 使用说明 


使用source-filtered  ＜interface-name＞开启源地址过滤功能；使用source-filtered  ＜interface-name＞ disable关闭源地址过滤功能。 






### 范例 


1、开启接口gei-0/1/0/1的ARP源地址过滤功能：ZXROSNG(config)#arpZXROSNG(config-arp)#source-filtered gei-0/1/0/12、关闭接口gei-0/1/0/1的ARP源地址过滤功能：ZXROSNG(config)#arpZXROSNG(config-arp)#source-filtered gei-0/1/0/1 disable





### 相关命令 


无 




## timeout interface 


timeout interface 




### 命令功能 


该命令工作于ARP配置模式下，配置指定接口学习到动态ARP条目的老化时间。使用no命令将ARP表项的老化时间恢复为缺省值。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



timeout interface 
  ＜Interface name 
＞ ＜seconds 
＞
no timeout interface 
  ＜Interface name 
＞
				






### 命令参数解释 




参数|描述
---|---
＜Interface name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。
＜seconds＞|ARP缓存中的ARP条目的老化时间，单位为秒，范围为1-2147483。默认值：14400秒。








### 缺省 


缺省接口下条目老化时间为4个小时 






### 使用说明 


ARP动态条目默认老化时间为4个小时。ARP动态条目达到老化时间后，将进行老化处理，发三次请求，若无回应，该条目进行删除；若学习到，该条目重新变为动态条目，等待下次老化。






### 范例 


1、配置接口gei-0/1/0/1的ARP老化时间为1200秒：ZXROSNG(config)#arpZXROSNG(config-arp)#timeout interface gei-0/1/0/1 12002、恢复接口gei-0/1/0/1的ARP老化时间为默认值：ZXROSNG(config)#arpZXROSNG(config-arp)#no timeout interface gei-0/1/0/1





### 相关命令 


无 




## timeout whole 


timeout whole 




### 命令功能 


设置整机ARP条目老化时间，此命令优先级低于接口老化时间配置timeout，两个配置都在，接口老化时间生效。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 




timeout whole 
  ＜seconds 
＞

no timeout whole 








### 命令参数解释 




参数|描述
---|---
＜seconds＞|整机ARP条目老化时间；范围：最小值为1，最大值为2147483,默认值为14400








### 缺省 


默认14400秒 






### 使用说明 


使用no命令恢复默认值 






### 范例 


1.设置整机ARP条目老化时间为3秒：ZXROSNG(config)#arpZXROSNG(config-arp)# timeout whole 32.恢复默认值：ZXROSNG(config)#arpZXROSNG(config-arp-supervlan1)#no timeout whole





### 相关命令 


timeout  




## timeout 


timeout 




### 命令功能 


该命令工作于ARP接口配置模式下，配置指定接口学习到动态ARP条目的老化时间。使用no命令将ARP表项的老化时间恢复为缺省值。若同时配置了该命令和整机老化命令，该配置生效，优先级高。 






### 命令模式 


 ARP接口模式  






### 命令默认权限级别 


15 






### 命令格式 




timeout 
  ＜seconds 
＞

no timeout 








### 命令参数解释 




参数|描述
---|---
＜seconds＞|ARP缓存中的ARP条目的老化时间，单位为秒，范围为1-2147483。默认值：14400秒








### 缺省 


默认老化时间是14400秒 






### 使用说明 


ARP动态条目默认老化时间为4个小时ARP动态条目达到老化时间后，将进行老化处理，发三次请求，若无回应，该条目进行删除；若学习到，该条目重新变为动态条目，等待下次老化。






### 范例 


1、配置接口gei-0/1/0/1的ARP老化时间为1200秒： ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#timeout 12002、恢复接口gei-0/1/0/1的ARP老化时间为默认值：ZXROSNG(config)#arpZXROSNG(config-arp)#interface gei-0/1/0/1ZXROSNG(config-arp-if-gei-0/1/0/1)#no timeout






### 相关命令 


无 




## to-permanent 


to-permanent 




### 命令功能 


将动态的ARP条目转化为永久类型的条目。转化后的永久ARP条目可以写盘重启，配置不消失。 






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 




to-permanent 
  ＜interface-name 
＞







### 命令参数解释 




参数|描述
---|---
＜interface-name＞|指定的接口名，将该接口学习到的动态条目进行转换








### 缺省 


无 






### 使用说明 


该命令只在ARP配模式下可配置，可转化条目数和永久ARP使用同一性能参数控制。 






### 范例 


将接口gei-0/1/0/1的动态ARP条目转化成永久 ARP条目:ZXROSNG(config)#arpZXROSNG(config-arp)#to-permanent gei-0/1/0/1






### 相关命令 


无 




## to-static 


to-static 




### 命令功能 


该命令工作于ARP配置模式下，用于将指定接口下的动态类型ARP条目转化为to-static类型ARP条目。使用no命令可以还原该操作，将to-static类型ARP条目再变为动态类型ARP条目。to-static类型ARP条目：此类ARP由学习到的动态ARP条目转化而来，不会老化丢失，用于保存安全的IP+MAC地址组合。与永久类型ARP条目的区别在于，to-static类型ARP条目不写数据库，设备重启后不复存在。






### 命令模式 


 ARP模式  






### 命令默认权限级别 


15 






### 命令格式 



to-static 
  [interface 
 ＜interface-name 
＞]
no to-static 
  [interface 
 ＜interface-name 
＞]
				






### 命令参数解释 




参数|描述
---|---
＜interface-name＞|配置ARP命令的具体接口名称，用于指定配置接口。可通过接口模块命令show ip interface brief可获取。








### 缺省 


无 






### 使用说明 


可转化条目数：不同项目具体数目由项目性能参数控制。该命令仅对动态ARP条目有效，其它类型ARP条目不可转化。






### 范例 


1、在ARP配置模式下，将接口gei-0/1/0/1的动态ARP条目转化成to-static类型 ARP条目，则输入以下命令：ZXROSNG(config)#arpZXROSNG(config-arp)#to-static interface gei-0/1/0/12、在ARP配置模式下，将接口gei-0/1/0/1下的to-static类型ARP条目恢复为动态类型 ARP条目，则输入以下命令：ZXROSNG(config)#arpZXROSNG(config-arp)# no to-static interface gei-0/1/0/1





### 相关命令 


无 




# TCPv4配置命令 
## clear tcp connect 


clear tcp connect 




### 命令功能 


该命令工作于特权模式，用于手动清除指定五元组(源地址、源端口、vrf域、远端地址、远端端口)的TCP连接。当系统中有不需要的TCP连接或者某个TCP连接存在异常时，可使用该命令进行清除。清除命令执行后，TCP首先发送RST重置报文通知对端清除相应的TCP连接，然后再清除本端的TCP连接信息。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear tcp connect 
  {＜local-ip-address 
＞|mng 
 ＜local-ip-address 
＞|vrf 
 ＜vrf-name 
＞ ＜local-ip-address 
＞} ＜local-port 
＞ ＜remote-ip-address 
＞ ＜remote-port 
＞







### 命令参数解释 




参数|描述
---|---
＜local-ip-address＞|本地IP地址，为十进制点分形式
＜local-ip-address＞|本地IP地址，为十进制点分形式
＜vrf-name＞|IP地址所属的VRF名称，长度为1-32个字符
＜local-ip-address＞|本地IP地址，为十进制点分形式
＜local-port＞|本地端口号，范围1-65535
＜remote-ip-address＞|本地IP地址，为十进制点分形式
＜remote-port＞|远端端口号，范围1-65535








### 缺省 


无 






### 使用说明 


清除TCP连接的同时，会通知上层业务模块删除与该连接对应的邻居信息。对于BGP协议来说，会撤销之前在该邻居上学习的路由，导致路由振荡；对于FTP协议来说，会删除之前传输的数据，FTP拷贝终止。命令执行清除时，没有确认提示，请慎用该清除命令。





### 范例 


通过clear命令清除系统中指定五元组的TCP连接，则输入以下命令：ZXROSNG#show tcp brief TCB Index      Local Address            Foreign Address          State5              1.1.1.1:21580            1.1.1.2:179              ESTABZXROSNG#clear tcp connect 1.1.1.1 21580 1.1.1.2 179 





### 相关命令 


show tcp brief 




## clear tcp statistics 


clear tcp statistics 




### 命令功能 


该命令工作于特权模式，用于清除系统TCP的统计信息。当需要观察系统在一段时间内TCP的统计信息时，使用该命令清除当前的统计信息，以方便收集一段时间段内TCP统计信息情况。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear tcp statistics 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


清除命令执行后，TCP的统计信息（参见操作命令show tcp statistics）将全部清零，并开始重新的统计过程。清除命令执行后，将不能恢复之前的统计信息，请慎用该清除命令。





### 范例 


统计信息显示参见操作命令show tcp statistics，则输入以下命令：ZXROSNG#show tcp statistics Rcvd: 6501 Total, 0 no port      0 checksum error, 0 bad offset, 0 too short      6491 packets (61774 bytes) in sequence      0 out-of-order packets (0 bytes)      0 packets (0 bytes) with data after window      0 packets after close      0 window probe packets, 1 window update packets      2 dup ack packets, 0 ack packets with unsend data      6491 ack packets (61774 bytes)Sent: 8326 Total, 0 urgent packets      1841 control packets (including 1668 retransmitted)       3243 data packets (61791 bytes)      1 data packets (19 bytes) retransmitted      3246 ack only packets (0 delayed)      0 window probe packets, 0 window update packets163 Connections initiated, 3 connections accepted1 Connections established,288 connections closed1669 Total rxmt timeout, 0 connections dropped in rxmt timeout6488 Keepalive timeout, 0 keepalive probe0 Connections dropped in keepalive
通过clear命令清除系统TCP统计信息，则输入以下命令：ZXROSNG#clear tcp statistics ZXROSNG#show tcp statistics   Rcvd: 0 Total, 0 no port      0 checksum error, 0 bad offset, 0 too short      0 packets (0 bytes) in sequence      0 out-of-order packets (0 bytes)      0 packets (0 bytes) with data after window      0 packets after close      0 window probe packets, 0 window update packets      0 dup ack packets, 0 ack packets with unsend data      0 ack packets (0 bytes)Sent: 0 Total, 0 urgent packets      0 control packets (including 0 retransmitted)       0 data packets (0 bytes)      0 data packets (0 bytes) retransmitted      0 ack only packets (0 delayed)      0 window probe packets, 0 window update packets0 Connections initiated, 0 connections accepted1 Connections established,0 connections closed0 Total rxmt timeout, 0 connections dropped in rxmt timeout0 Keepalive timeout, 0 keepalive probe0 Connections dropped in keepalive






### 相关命令 


show tcp statistics 




## clear tcp tcb 


clear tcp tcb 




### 命令功能 


该命令工作于特权模式，用于手动清除指定索引号的TCP连接。当系统中有不需要的TCP连接或者某个TCP连接存在异常时，可使用该命令进行清除。清除命令执行后，TCP首先发送RST重置报文通知对端清除相应的TCP连接，然后再清除本端的TCP连接信息。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


15 






### 命令格式 




clear tcp tcb 
  ＜tcb-index 
＞







### 命令参数解释 




参数|描述
---|---
＜tcb-index＞|TCP本地索引号，可通过show tcp brief命令查询有效范围：1-4294967295








### 缺省 


无 






### 使用说明 


清除TCP连接的同时，会通知上层业务模块删除与该连接对应的邻居信息。对于BGP协议来说，会撤销之前在该邻居上学习的路由，导致路由振荡；对于FTP协议来说，会删除之前传输的数据，FTP拷贝终止。命令执行清除时，没有确认提示，请慎用该清除命令。





### 范例 


通过show tcp brief 命令查询TCB索引号，然后执行clear命令清除系统中指定索引号的TCP连接，则输入以下命令：ZXROSNG#show tcp brief TCB Index      Local Address            Foreign Address          State5              1.1.1.1:21580            1.1.1.2:179              ESTABZXROSNG#clear tcp tcb 5 





### 相关命令 


show tcp brief 




## debug ip tcp all 


debug ip tcp all 




### 命令功能 


该命令工作于特权模式，用于开启TCP所有的打印开关。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


2 






### 命令格式 




debug ip tcp all 
 

no debug ip tcp all 








### 命令参数解释 



					无
				 






### 缺省 


关闭该调试功能 






### 使用说明 


使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面TCP控制事件信息。开启的TCP打印开关包括报文收发打印开关（参见操作命令debug ip tcp packet）、控制信息打印开关（参见操作命令debug ip tcp driver）、报文相关的控制信息打印开关（参见操作命令debug ip tcp driver-pak）、重要处理信息打印开关（参见操作命令debug ip tcp transactions）。可使用no debug ip tcp all或者no debug all命令关闭该debug开关。





### 范例 


打开TCP所有的debug开关，则输入以下命令：ZXROSNG#terminal monitorZXROSNG#debug ip tcp all All TCP debugging has been turned on关闭TCP所有的debug开关，则输入以下命令：ZXROSNG#no debug ip tcp all                                                   All TCP debugging has been turned off打开TCP所有打印开关后，输出的信息参见debug ip tcp packet、debug ip tcp driver、debug ip tcp driver-pak、debug ip tcp transactions这四个命令的输出信息。





### 相关命令 


terminal monitor    show debug tcp



## debug ip tcp driver 


debug ip tcp driver 




### 命令功能 


该命令工作于特权模式，用于开启TCP控制信息的打印开关。当需要查看TCP连接建链和关闭等控制事件信息时，使用该命令。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


2 






### 命令格式 




debug ip tcp driver 
 

no debug ip tcp driver 








### 命令参数解释 



					无
				 






### 缺省 


关闭该调试功能 






### 使用说明 


使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面TCP控制事件信息。打印的信息包括TCP连接主动建链成功信息、被动建链成功信息、启动SYNWAIT超时定时器信息、正常关闭TCP连接的信息、异常终止TCP连接的信息。可使用no debug ip tcp driver、no debug ip tcp all或者no debug all命令关闭该debug开关。为了避免该类debug信息的循环打印，TELNET应用对应TCP连接的控制信息不予打印。





### 范例 


打开TCP控制信息的debug开关，则输入以下命令：ZXROSNG#terminal monitor ZXROSNG#debug ip tcp driver TCP driver event debugging is on关闭TCP控制信息的debug开关，则输入以下命令：ZXROSNG#no debug ip tcp driver                                                   TCP driver event debugging is off在打开TCP控制信息的debug开关后，OAM界面会显示TCP控制事件的详细信息，如下：ZXROSNG#ZXR10 MPU-0/20/0 2013-12-13 05:38:31 TCB[6]: 1.1.1.1:179-->1.1.1.2:22868 CloseZXROSNG#ZXR10 MPU-0/20/0 2013-12-13 05:38:32 TCB[7]: Active open 1.1.1.1:0-->1.1.1.2:179 OK,lport 21579ZXR10 MPU-0/20/0 2013-12-13 05:38:32 TCB[7]: enable tcp open timeouts输出信息中的参数信息解释如下：参数名称                                                       参数说明ZXR10                                                          设备系列MPU-0/20/0                                                     产生该打印信息的单板及槽位信息2013-12-13 05:38:31                                            产生该打印的时间TCB[6]: 1.1.1.1:179-->1.1.1.2:22868 Close                      索引号为6，本端地址为1.1.1.1，本端端口为179，远端地址为1.1.1.2，远端端口为22868的TCP连接关闭TCB[7]: Active open 1.1.1.1:0-->1.1.1.2:179 OK,lport 21579     索引号为7，本端地址为1.1.1.1，远端地址为1.1.1.2，远端端口为179的TCP连接主动开启成功，分配的本地端口号为21579TCB[7]: enable tcp open timeouts                               索引号为7的TCP连接启用SYNWAIT定时器






### 相关命令 


terminal monitor    show debug tcp



## debug ip tcp driver-pak 


debug ip tcp driver-pak 




### 命令功能 


该命令工作于特权模式，用于开启TCP报文相关的控制信息打印开关。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


2 






### 命令格式 




debug ip tcp driver-pak 
 

no debug ip tcp driver-pak 








### 命令参数解释 



					无
				 






### 缺省 


关闭该调试功能 






### 使用说明 


使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面TCP控制事件信息。打印的信息包括应用写入TCP发送缓存的数据信息、TCP发送报文简要信息、TCP接收报文简要信息、TCP删除先序队列信息。可使用no debug ip tcp driver-pak、no debug ip tcp all或者no debug all命令关闭该debug开关。





### 范例 


打开TCP报文相关的控制信息debug开关，则输入以下命令：ZXROSNG#terminal monitor ZXROSNG#debug ip tcp driver-pak TCP driver verbose debugging is on关闭TCP报文相关的控制信息debug开关，则输入以下命令：ZXROSNG#no debug ip tcp driver-pak                                                   TCP driver verbose debugging is off在打开TCP报文相关的控制信息debug开关后，OAM界面会显示信息如下：ZXROSNG#ZXR10 MPU-0/20/0 2013-12-13 06:19:33 TCB[6]: recv 19 bytes (SEQ: 4259081009)ZXR10 MPU-0/20/0 2013-12-13 06:19:33 TCB[6]: sending packet(len 20)ZXR10 MPU-0/20/0 2013-12-13 06:19:51 TCB[6]: packet(len 19) is put in output queue.ZXR10 MPU-0/20/0 2013-12-13 06:19:51 TCB[6]: sending packet(len 39)输出信息中的参数信息解释如下：参数名称                                         参数说明ZXR10                                            设备系列MPU-0/20/0                                       产生该打印信息的单板及槽位信息2013-12-13 06:19:33                              产生该打印信息的时间TCB[6]: recv 19 bytes (SEQ: 4259081009)          索引号为6的TCP连接接收到数据长度为19字节的报文，接收报文的序列号为4259081009TCB[6]: sending packet(len 20)                   索引号为6的TCP连接发送数据长度为20字节的报文（包含TCP头）TCB[6]: packet(len 19) is put in output queue    长度为19字节的报文加入到索引号为6的TCP连接的发送队列中





### 相关命令 


terminal monitor    show debug tcp



## debug ip tcp packet 


debug ip tcp packet 




### 命令功能 


该命令工作于特权模式，用于开启TCP收发报文的打印开关。当需要查看TCP连接报文收发情况时，使用该命令。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


2 






### 命令格式 




debug ip tcp packet 
  [{[address 
 ＜ip-address 
＞],[port 
 ＜port-num 
＞],[{out 
|in 
}],[detail 
]}]

no debug ip tcp packet 








### 命令参数解释 




参数|描述
---|---
＜ip-address＞|源地址或者目的地址
＜port-num＞|端口号
out|发送的报文
in|接受的报文
detail|更多报文详细描述








### 缺省 


关闭该调试功能 






### 使用说明 


使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面打印报文收发信息。可使用no debug ip tcp packet、no debug ip tcp all或者no debug all命令关闭该debug开关。为了避免报文收发debug信息的循环打印，TELNET应用对应TCP连接的报文收发情况不予打印。





### 范例 


 






### 相关命令 


terminal monitor    show debug tcp



## debug ip tcp transactions 


debug ip tcp transactions 




### 命令功能 


该命令工作于特权模式，用于开启TCP重要处理信息的打印开关。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


2 






### 命令格式 




debug ip tcp transactions 
 

no debug ip tcp transactions 








### 命令参数解释 



					无
				 






### 缺省 


关闭该调试功能 






### 使用说明 


使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面TCP控制事件信息。打印的重要处理信息包括TCP状态迁移、TCP重传信息、TCP建链信息、TCP连接清除信息。可使用no debug ip tcp transactions、no debug ip tcp all或者no debug all命令关闭该debug开关。为了避免该类debug信息的循环打印，TELNET应用对应TCP连接的重要处理信息不予打印。





### 范例 


打开TCP重要处理信息的debug开关，则输入以下命令：ZXROSNG#terminal monitor ZXROSNG#debug ip tcp transactions TCP special event debugging is on关闭TCP重要处理信息的debug开关，则输入以下命令：ZXROSNG#no debug ip tcp transactions                                                   TCP special event debugging is off在打开TCP重要处理信息的debug开关后，OAM界面会显示信息如下：ZXROSNG#ZXR10 MPU-0/20/0 2013-12-13 06:59:26 TCB[6]: state was ESTAB -> FINWAIT-1 [179 -> 1.1.1.2(22869)]ZXR10 MPU-0/20/0 2013-12-13 06:59:26 TCB[6]: state was FINWAIT-1 -> CLOSING [179 -> 1.1.1.2(22869)]ZXROSNG#ZXR10 MPU-0/20/0 2013-12-13 06:59:27 TCB[5]: Connection to 1.1.1.2:179, advertising MSS 1460ZXR10 MPU-0/20/0 2013-12-13 06:59:27 输出信息中的参数信息解释如下：参数名称                                                        参数说明ZXR10                                                           设备系列MPU-0/20/0                                                      产生该打印信息的单板及槽位信息2013-12-13 06:59:26                                             产生该打印信息的时间TCB[6]: state was ESTAB -> FINWAIT-1 [179 -> 1.1.1.2(22869)]    索引号为6的TCP连接状态从ESTAB迁移到FINWAIT-1（用户执行CLOSE操作），本端端口179，远端地址1.1.1.2，远端端口22869，具体状态及状态迁移参见RFC793第3.2节TCB[6]: state was FINWAIT-1 -> CLOSING [179 -> 1.1.1.2(22869)]  索引号为6的TCP连接状态从FINWAIT-1迁移到CLOSING（收到对方的FIN报文），本端端口179，远端地址1.1.1.2，远端端口22869TCB[5]: Connection to 1.1.1.2:179, advertising MSS 1460         本端发起向1.1.1.2的TCP建链请求，远端端口为179，通告的TCP MSS值为1460






### 相关命令 


terminal monitor    show debug tcp



## debug ip udp 


debug ip udp 




### 命令功能 


该命令工作于特权模式，用于开启UDP收发报文的打印开关。当需要查看UDP报文收发情况时，使用该命令。 






### 命令模式 


 特权模式  






### 命令默认权限级别 


2 






### 命令格式 




debug ip udp 
  [{[address 
 ＜ip-address 
＞],[port 
 ＜port-num 
＞]}]

no debug ip udp 








### 命令参数解释 




参数|描述
---|---
＜ip-address＞|源地址或者目的地址
＜port-num＞|端口号








### 缺省 


关闭该调试功能 






### 使用说明 


该命令需要伴随terminal monitor命令使用（参见操作命令terminal monitor），否则无法在OAM界面打印报文收发信息。可使用no debug ip udp或者no debug all命令关闭该debug开关。参数ip-address配置全0时，不进行地址过滤。参数port-num配置范围为<1-65535>






### 范例 


ZXROSNG#terminal monitorZXROSNG#debug ip udp UDP packet debugging is onZXROSNG#debug ip udp port 1UDP packet debugging is on for port number 1ZXROSNG#debug ip udp address 1.1.1.1 UDP packet debugging is on for address 1.1.1.1ZXROSNG#show debug udpUDP:  UDP packet debugging is on for address 1.1.1.1ZXROSNG#trace 1.1.1.1               Tracing the route to 1.1.1.1 over a maximum of 30 hop(s):ZXR10 MPU-0/20/0 2013-3-19 06:29:55  UDP: sending src=1.1.1.1(21921), dst=1.1.1.1(33480), len=108ZXR10 MPU-0/20/0 2013-3-19 06:29:55  UDP: rcvd src=1.1.1.1(21921), dst=1.1.1.1(33480), len=1081    *ZXR10 MPU-0/20/0 2013-3-19 06:29:58  UDP: sending src=1.1.1.1(21921), dst=1.1.1.1(33473), len=108输出信息中的参数信息解释如下：参数名称               参数说明ZXR10                  设备系列MPU-0/20/0             产生该打印信息的单板及槽位信息2013-3-19 06:29:55     产生该打印信息的时间UDP                    表示是UDP模块的debug打印信息sending                表示UDP模块发送的报文rcvd                   表示UDP模块接收的报文src=1.1.1.1(21921)     UDP本端IP地址为1.1.1.1，本端端口号为21921dst=1.1.1.2(33480)     UDP远端IP地址为1.1.1.1，远端端口号为33480len=108                UDP报文长度（包括UDP头）






### 相关命令 


terminal monitor    show debug udp



## ip tcp adjust-mss 


ip tcp adjust-mss 




### 命令功能 


该命令工作于接口模式（包括以太接口模式、千兆以太接口模式、pos接口模式、multilink接口模式、smartgroup子接口模式、以太子接口模式、smartgroup接口模式、supervlan接口模式、10G以太接口模式、gre隧道接口模式、posgroup接口模式、pos子接口模式），用于转发面调整转发的TCP建链SYN报文的MSS（Maximum Segment Size）值。当网络中有节点的MTU（Maximum Transmission Unit）较小时，可以使用该命令调整途径该设备TCP建链SYN报文中的MSS值，使得TCP两端协商的MSS值不大于该设置值，确保TCP报文经过该网络时不会被分片。配置成功后，转发面在转发SYN报文时，如果SYN报文中的MSS选项值大于该配置值，则以配置值重置MSS选项值。TCP MSS是在建链时两端协商的最大报文长度，建链以后两端发送的报文长度不应超过该协商值。合理的MSS值可以避免TCP报文在中间网络分片或者丢弃。TCP MSS调整是在没有部署PMTU（Path MTU）发现状况下一个有效避免TCP报文在中间网络分片的方法。





### 命令模式 


 10G以太接口模式,multilink接口模式,posgroup接口模式,pos子接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,supervlan接口模式,ulei子接口模式,ulei接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






### 命令默认权限级别 


千兆以太接口模式:15,以太接口模式:15,pos接口模式:15,multilink接口模式:15,smartgroup子接口模式:15,以太子接口模式:15,smartgroup接口模式:15,supervlan接口模式:15,10G以太接口模式:15,posgroup接口模式:15,pos子接口模式:15,ulei接口模式:15,ulei子接口模式:15 






### 命令格式 



ip tcp adjust-mss 
  ＜max-segment-size 
＞

no ip tcp adjust-mss 








### 命令参数解释 




参数|描述
---|---
＜max-segment-size＞|TCP最大报文段长度，取值范围500~1460,单位：字节








### 缺省 


不配置TCP调整MSS值 






### 使用说明 


拥有管理员权限的操作员可以使用该命令设置经过该接口转发出去的TCP SYN报文的MSS值。转发面只会修改TCP SYN报文中MSS选项值大于该配置值的报文。默认不使能该功能。






### 范例 


在gei-0/1/0/1接口下设置TCP调整MSS的值为1000字节，则输入以下命令：ZXROSNG(config-if-gei-0/1/0/1)# ip tcp adjust-mss 1000在gei-0/1/0/1接口下去除设置TCP调整MSS值，则输入以下命令：ZXROSNG(config-if-gei-0/1/0/1)# no ip tcp adjust-mss





### 相关命令 


无 




## ip tcp adjust-mss 


ip tcp adjust-mss 




### 命令功能 


该命令工作于接口模式（包括以太接口模式、千兆以太接口模式、pos接口模式、multilink接口模式、smartgroup子接口模式、以太子接口模式、smartgroup接口模式、supervlan接口模式、10G以太接口模式、gre隧道接口模式、posgroup接口模式、pos子接口模式），用于转发面调整转发的TCP建链SYN报文的MSS（Maximum Segment Size）值。当网络中有节点的MTU（Maximum Transmission Unit）较小时，可以使用该命令调整途径该设备TCP建链SYN报文中的MSS值，使得TCP两端协商的MSS值不大于该设置值，确保TCP报文经过该网络时不会被分片。配置成功后，转发面在转发SYN报文时，如果SYN报文中的MSS选项值大于该配置值，则以配置值重置MSS选项值。TCP MSS是在建链时两端协商的最大报文长度，建链以后两端发送的报文长度不应超过该协商值。合理的MSS值可以避免TCP报文在中间网络分片或者丢弃。TCP MSS调整是在没有部署PMTU（Path MTU）发现状况下一个有效避免TCP报文在中间网络分片的方法。





### 命令模式 


 gre隧道接口模式  






### 命令默认权限级别 


15 






### 命令格式 



ip tcp adjust-mss 
  ＜max-segment-size 
＞

no ip tcp adjust-mss 








### 命令参数解释 




参数|描述
---|---
＜max-segment-size＞|TCP最大报文段长度，取值范围500~1460,单位：字节








### 缺省 


不配置TCP调整MSS值 






### 使用说明 


拥有管理员权限的操作员可以使用该命令设置经过该接口转发出去的TCP SYN报文的MSS值。转发面只会修改TCP SYN报文中MSS选项值大于该配置值的报文。默认不使能该功能。






### 范例 


在gei-0/1/0/1接口下设置TCP调整MSS的值为1000字节，则输入以下命令：ZXROSNG(config-if-gei-0/1/0/1)# ip tcp adjust-mss 1000在gei-0/1/0/1接口下去除设置TCP调整MSS值，则输入以下命令：ZXROSNG(config-if-gei-0/1/0/1)# no ip tcp adjust-mss





### 相关命令 


无 




## ip tcp finwait-time 


ip tcp finwait-time 




### 命令功能 


该命令工作于全局配置模式，用于设置TCP FINWAIT-2超时时间。配置成功后，当系统关闭TCP连接时，TCP连接处于FINWAIT-2状态的超时时间为该设置值，超过该超时时间而没有收到对方回应的FIN报文，本端TCP将强行关闭该TCP连接。TCP FINWAIT-2状态为TCP主动关闭一方可能经过的一个中间状态，处于该状态下的TCP连接等待对端发送FIN报文，如果等待一段时间本端依然没有接收到对端的FIN报文，本端TCP将强行关闭该TCP连接，所等待的时间就是本条命令配置的时间。TCP状态迁移及FINWAIT-2状态介绍参见RFC793第3.2节。使用no命令恢复默认值。






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ip tcp finwait-time 
  ＜seconds 
＞

no ip tcp finwait-time 








### 命令参数解释 




参数|描述
---|---
＜seconds＞|关闭TCP连接时间，单位：秒，范围100~600，缺省为150秒








### 缺省 


关闭tcp连接的等待时间为150秒 






### 使用说明 


TCP FINWAIT-2超时时间默认值是150秒，拥有管理员权限的操作员可以使用这条命令变更TCP FINWAIT-2超时时间。配置变更后，TCP FINWAIT-2超时时间只对新进入FINWAIT-2状态的TCP连接生效，之前已经处于FINWAIT-2状态的TCP连接的超时时间不会变化。





### 范例 


设置TCP FINWAIT-2超时时间为100秒，则输入以下命令：ZXROSNG(config)# ip tcp finwait-time 100去除设置TCP FINWAIT-2超时时间，恢复为默认值150秒，则输入以下命令：ZXROSNG(config)# no ip tcp finwait-time





### 相关命令 


show tcp config 




## ip tcp initial-window 


ip tcp initial-window 




### 命令功能 


该命令工作于全局配置模式，用于设置TCP初始发送窗口大小，单位为MSS。配置TCP初始窗口大小，在TCP刚启动或者从空闲状态（idle）恢复的时候设置为初始窗口，设置较大的初始窗口可以提高TCP传输速度，特别对于Portal、Web等少数据交互的场景。未配置该命令时按照RFC5681约定取2-4个MSS大小，配置后可对现有连接生效，但现有连接只有从idle恢复时才会取用初始窗口。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 




ip tcp initial-window 
  ＜MSS 
＞

no ip tcp initial-window 








### 命令参数解释 




参数|描述
---|---
＜MSS＞|初始窗口大小，范围2-10，单位MSS，表示2-10倍MSS大小








### 缺省 


无 






### 使用说明 


配置TCP初始窗口大小，在TCP启动或者从idle恢复的时候设置为初始窗口，设置较大的初始窗口可以提高TCP传输速度，特别对于Portal、Web等少数据交互的场景。未配置该命令时按照RFC5681约定取2-4个MSS大小，配置后可对现有连接生效，但现有连接只有从idle恢复时才会取用初始窗口。 






### 范例 


设置TCP 初始窗口大小为为10个MSS，则输入以下命令：ZXROSNG(config)# ip tcp initial-window 10去除设置TCP 初始化窗口大小，则输入以下命令：ZXROSNG(config)# no ip tcp initial-window





### 相关命令 


show tcp config 




## ip tcp max-retrans-retries 


ip tcp max-retrans-retries 




### 命令功能 


该命令工作于全局配置模式，用于设置TCP最大重传次数。TCP是一种数据可靠传输机制，因此在本端发送的数据没有在规定的时间内得到对方应答时，则会进行报文的重传，重传的次数是有限制，此命令用来配置TCP的最大重传次数。设置TCP最大重传次数，未配置时在有丢包的情况下的最大重传次数为7次，通过设置可以手动的调整TCP超时重传的次数，以便灵活的设定TCP在丢包情况下的老化时间。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 




ip tcp max-retrans-retries 
  ＜max-retrans-retries 
＞

no ip tcp max-retrans-retries 








### 命令参数解释 




参数|描述
---|---
＜max-retrans-retries＞|TCP最大重传次数，范围5-20








### 缺省 


无 






### 使用说明 


设置后对现有连接不生效，连接重建后才可生效。可以通过show tcp config命令查看当前配置。 






### 范例 


设置TCP最大重传次数为10次，则输入以下命令：ZXROSNG(config)# ip tcp max-retrans-retries 10去除设置TCP 最大重传次数，则输入以下命令：ZXROSNG(config)# no ip tcp max-retrans-retries





### 相关命令 


show tcp config 




## ip tcp mss 


ip tcp mss 




### 命令功能 


该命令工作于全局配置模式，用于设置TCP MSS值的大小，即TCP发送报文最大分片大小。通常TCP MSS的大小是通过查找目的地址路由信息，根据路由类型来选择合适的MSS，直连路由为1460字节，非直连路由为536字节。但如果业务对组网环境很熟悉，可以通过配置MSS的大小，来提升TCP发送报文最大分片大小。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 




ip tcp mss 
  ＜bytes 
＞

no ip tcp mss 








### 命令参数解释 




参数|描述
---|---
＜bytes＞|最大分片大小，单位字节，范围<68-10000>








### 缺省 


默认不使用该方式选择MSS 






### 使用说明 


配置变更后，TCP MSS只对新建的TCP连接生效，正在建链或者已经建链成功的TCP连接不会受到影响。 






### 范例 


设置TCP MSS大小为1460字节，则输入以下命令：ZXROSNG(config)# ip tcp mss 1460去除设置TCP MSS，则输入以下命令：ZXROSNG(config)# no ip tcp mss





### 相关命令 


show tcp config 




## ip tcp retrans-time 


ip tcp retrans-time 




### 命令功能 


该命令工作于全局配置模式，用于设置TCP最小和最大重传时间。TCP是一种数据可靠传输机制，因此当本端发送的数据没有在规定的时间内收到对方应答时，则会进行报文的重传，此配置命令就是用来设定TCP重传报文的最小和最大重传时间。设置TCP重传的最小和最大重传时间，按照RFC6298的要求，最小重传时间为1秒，最大重传时间为60秒，ROSNG系统在未配置该命令时按照RFC6298要求。 






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 




ip tcp retrans-time 
 minimum 
 ＜min-retrans-time 
＞ maximum 
 ＜max-retrans-time 
＞

no ip tcp retrans-time 








### 命令参数解释 




参数|描述
---|---
＜min-retrans-time＞|最小重传时间，范围300-3000，单位毫秒（ms）
＜max-retrans-time＞|最大重传时间，范围8000-120000，单位毫秒（ms）








### 缺省 


无 






### 使用说明 


设置TCP重传的最小和最大重传时间，按照RFC6298的要求，最小重传时间为1秒，最大重传时间为60秒，ROSNG系统在未配置该命令时按照RFC6298要求。提供配置命令方便用户在不同场景下进行有效的设置，比如在某些场景下需要加快重传的老化速度，那么就可以配置较小的最小和最大重传时间值；而在某些场景希望TCP能够容忍网络丢包，延缓由于丢包导致的TCP断链，那么就可以配置较大的最小和最大重传时间值。配置后可对现有连接生效。 






### 范例 


设置TCP最小重传时间为500ms，最大重传时间为10000ms，则输入以下命令：ZXROSNG(config)# ip tcp retrans-time minimum 500 maximum 10000去除设置TCP 最小与最大重传时间，则输入以下命令：ZXROSNG(config)# no ip tcp retrans-time





### 相关命令 


show tcp config 




## ip tcp synflood-protect defence 


ip tcp synflood-protect defence 




### 命令功能 


该命令工作于全局配置模式，用于配置TCP SYN Flood防护功能的防护模式。当需要变更TCP SYN Flood防护功能的防护模式，或者改变防护模式中的参数设置时，使用该命令。配置成功后，当系统受到TCP SYN Flood攻击时，系统将根据配置的防护模式及参数启动相应的防护策略，保证TCP资源的可用性。TCP SYN Flood防护模式分为三种，0：删除TCP半连接并且加快TCP半连接的老化速度；1：删除TCP半连接；2：加快TCP半连接的老化速度。其中每次删除半连接的个数及TCP半连接的老化时间均可通过参数设置。





### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ip tcp synflood-protect defence 
  {＜defence-parameter-0 
＞ waittime 
 ＜wait-time 
＞ num 
 ＜half-connect-numbers 
＞|＜defence-parameter-1 
＞ num 
 ＜half-connect-numbers 
＞|＜defence-parameter-2 
＞ waittime 
 ＜wait-time 
＞}

no ip tcp synflood-protect defence 








### 命令参数解释 




参数|描述
---|---
＜defence-parameter-0＞|和1、2是三选一。若设置为0，则TCP SYN Flood防护功能的防护模式为删除TCP半连接，并且加快TCP半连接的老化速度。
＜wait-time＞|设置TCP半连接的老化时间，防护模式为0、2时可配置。取值范围：配置范围为1-80秒。默认值：30秒。
＜half-connect-numbers＞|设置每次删除TCP半连接的个数，防护模式为0、1时可配置。取值范围：配置范围为1-65535个。默认值：1个。
＜defence-parameter-1＞|和0、2是三选一。若设置为1，则TCP SYN Flood防护功能的防护模式为删除TCP半连接。
＜half-connect-numbers＞|设置每次删除TCP半连接的个数，防护模式为0、1时可配置。取值范围：配置范围为1-65535个。默认值：1个。
＜defence-parameter-2＞|和0、1是三选一。若设置为2，则TCP SYN Flood防护功能的防护模式为加快TCP半连接的老化速度。
＜wait-time＞|设置TCP半连接的老化时间，防护模式为0、2时可配置。取值范围：配置范围为1-80秒。默认值：30秒。








### 缺省 


在TCP SYN Flood防护功能打开的情况下，默认配置是防护策略类型是:减少SYN等待超时时间的同时还删除旧的半连接，SYN等待超时时间为30秒，半连接老化数为1。 






### 使用说明 


TCP SYN Flood防护功能的防护模式默认为0，即删除TCP半连接并且加快TCP半连接的老化速度，每次删除的TCP半连接个数为1个，TCP半连接的老化时间为30秒。拥有管理员权限的操作员可以使用该命令变更TCP SYN Flood防护功能的防护模式或者改变防护模式中的参数设置。当修改TCP SYN Flood防护功能的防护模式，或者修改防护模式中的参数设置后，需要开启TCP SYN Flood防护功能（参见配置命令ip tcp synflood-protect enable）才能生效。建议采用TCP SYN Flood防护功能的默认防护模式。拥有管理员权限的操作员可以根据实际情况变更每次删除TCP半连接的个数以及TCP半连接的老化时间，TCP半连接的老化时间不建议配置为小于3秒，以防止正常的建链请求被误删除。





### 范例 


配置TCP SYN Flood防护功能的防护模式为0，并变更删除的TCP半连接个数以及TCP半连接的老化速度，则输入以下命令：ZXROSNG(config)# ip tcp synflood-protect defence 0 waittime 10 num 100去配置TCP SYN Flood防护功能的防护模式，恢复为默认值，则输入以下命令：ZXROSNG(config)# no ip tcp synflood-protect defence





### 相关命令 


ip tcp synflood-protect enableshow tcp synflood-protect config



## ip tcp synflood-protect enable 


ip tcp synflood-protect enable 




### 命令功能 


该命令工作于全局配置模式，用于开启TCP SYN Flood防护功能。当需要保护系统的TCP资源免受攻击时，使用该命令。配置成功后，当系统受到TCP SYN Flood攻击时，系统将采取一些措施删除或者加快老化TCP半连接，保证TCP资源的可用性。TCP SYN Flood攻击是攻击者发送大量伪造的SYN报文，并且不对被攻击者回应的SYN+ACK报文进行ACK回应，导致被攻击者系统中存在大量的TCP半连接，消耗被攻击者系统TCP资源，阻止被攻击者系统响应正常的TCP建链请求，从而达到DoS(Deny of Service)的攻击目的。TCP SYN Flood防护功能就是为了防止该类DoS攻击，避免系统的TCP资源被攻击者的半连接占满，保障系统可以响应正常的TCP建链请求。





### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ip tcp synflood-protect enable 
 

no ip tcp synflood-protect enable 








### 命令参数解释 



					无
				 






### 缺省 


TCP SYN Flood防护功能关闭 






### 使用说明 


TCP SYN Flood防护功能默认是关闭的，拥有管理员权限的操作员可以使用该命令开启TCP SYN Flood防护功能。配置该命令后，当TCP连接个数占系统最大TCP资源个数达到一定的比率(参见配置命令ip tcp synflood-protect max-connect)，或者一分钟内建立的TCP连接个数占系统最大TCP资源个数达到一定的比率(参见配置命令ip tcp synflood-protect one-minute)，TCP SYN Flood防护功能会删除或者加快老化一些TCP半连接（参见配置命令ip tcp synflood-protect defence）。通过no ip tcp synflood-protect enable命令关闭TCP SYN Flood防护功能。





### 范例 


开启TCP SYN Flood防护功能，则输入以下命令：ZXROSNG(config)# ip tcp synflood-protect enable关闭TCP SYN Flood防护功能，则输入以下命令：ZXROSNG(config)# no ip tcp synflood-protect enable





### 相关命令 


show tcp synflood-protect config 




## ip tcp synflood-protect max-connect 


ip tcp synflood-protect max-connect 




### 命令功能 


该命令工作于全局配置模式，用于配置TCP SYN Flood防护功能的TCP连接比率值。当需要修改TCP SYN Flood防护功能的TCP连接比率值时，使用该命令。配置成功后，当系统的TCP连接个数占系统最大TCP资源个数的比率值达到配置的高比率值后，系统将根据配置的防护模式（参见配置命令ip tcp synflood-protect defence）启动相应的防护策略，保证TCP资源的可用性。比率值的配置分为高和低两个值，当TCP连接个数占系统最大TCP资源个数的比率值达到高比率值时，系统启动相应的防护策略，进入防御状态；达到低比率值时，系统进入告警状态，不启动防护策略。





### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ip tcp synflood-protect max-connect 
  {[high 
 ＜high-number 
＞],[low 
 ＜low-number 
＞]}

no ip tcp synflood-protect max-connect 








### 命令参数解释 




参数|描述
---|---
＜high-number＞|设置TCP SYN Flood防护功能的TCP连接高比率值取值范围：配置范围为1-100，单位%。默认值：90%。
＜low-number＞|设置TCP SYN Flood防护功能的TCP连接低比率值取值范围：配置范围为1-100，单位%。默认值：60%。








### 缺省 


在TCP SYN Flood防护功能打开的情况下， 默认配置是总连接数达到最大连接数的90%开始防御，达到60%进行告警 






### 使用说明 


TCP SYN Flood防护功能的TCP连接比率值分为高和低两个值，高比率值默认为90（单位%），低比率值默认为60（单位%），默认情况下系统TCP连接个数占系统最大TCP资源个数的比率值达到90%以后，系统将根据配置的防护模式（参见配置命令ip tcp synflood-protect defence）启动相应的防护策略。拥有管理员权限的操作员可以使用该命令修改TCP SYN Flood防护功能的TCP连接比率值。配置的TCP连接高比率值必须大于配置的TCP连接低比率值，否则配置以报错结束。配置的TCP连接高比率值不能小于配置的一分钟TCP连接的高比率值（参见配置命令ip tcp synflood-protect one-minute)；配置的TCP连接低比率值不能小于配置的一分钟TCP连接的低比率值（参见配置命令ip tcp synflood-protect one-minute)；





### 范例 


配置TCP SYN Flood防护功能的TCP连接高比率值80%，低比率值60%，则输入以下命令：ZXROSNG(config)# ip tcp synflood-protect max-connect high 80 low 60去配置TCP SYN Flood防护功能的TCP连接比率值，恢复为默认值，则输入以下命令：ZXROSNG(config)# no ip tcp synflood-protect max-connect





### 相关命令 


ip tcp synflood-protect enableshow tcp synflood-protect config



## ip tcp synflood-protect one-minute 


ip tcp synflood-protect one-minute 




### 命令功能 


该命令工作于全局配置模式，用于配置TCP SYN Flood防护功能的一分钟TCP连接比率值。当需要变更TCP SYN Flood防护功能的一分钟TCP连接比率值时，使用该命令。配置成功后，当系统受到TCP SYN Flood攻击时，且一分钟内新增的TCP连接个数占系统最大TCP资源个数的比率值达到该高比率值后，系统将根据配置的防护模式（参见配置命令ip tcp synflood-protect defence）启动相应的防护策略，保证TCP资源的可用性。比率值的配置分为高和低两个值，当一分钟内新增的TCP连接个数占系统最大TCP资源个数的比率值达到高比率值时，系统启动相应的防护策略，进入防御状态；达到低比率值时，系统进入告警状态，不启动防护策略。





### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ip tcp synflood-protect one-minute 
  {[high 
 ＜high-number 
＞],[low 
 ＜low-number 
＞]}

no ip tcp synflood-protect one-minute 








### 命令参数解释 




参数|描述
---|---
＜high-number＞|设置TCP SYN Flood防护功能的一分钟TCP连接高比率值取值范围：配置范围为1-100，单位%。默认值：80%。
＜low-number＞|设置TCP SYN Flood防护功能的一分钟TCP连接低比率值取值范围：配置范围为1-100，单位%。默认值：50%。








### 缺省 


在TCP SYN Flood防护功能打开的情况下， 默认配置是一分钟内达到最大连接数80%开始防御，达到最大连接数的50%进行告警 






### 使用说明 


TCP SYN Flood防护功能的一分钟TCP连接比率值分为高和低两个值，高比率值默认为80（单位%），低比率值默认为50（单位%），默认情况下一分钟内新增的TCP连接个数占系统最大TCP资源个数的比率值达到80%以后，系统将根据配置的防护模式（参见配置命令ip tcp synflood-protect defence）启动相应的防护策略。拥有管理员权限的操作员可以使用这条命令修改TCP SYN Flood防护功能的一分钟TCP连接比率值。配置的一分钟TCP连接高比率值必须大于配置的一分钟TCP连接低比率值，否则配置以报错结束。配置的一分钟TCP连接高比率值不能大于配置的TCP连接高比率值(参见配置命令ip tcp synflood-protect max-connect）；配置的一分钟TCP连接低比率值不能大于配置的TCP连接低比率值(参见配置命令ip tcp synflood-protect max-connect）；





### 范例 


配置TCP SYN Flood防护功能的一分钟TCP连接高比率值70%，低比率值50%，则输入以下命令：ZXROSNG(config)# ip tcp synflood-protect one-minute high 70 low 50去配置TCP SYN Flood防护功能的一分钟TCP连接比率值，恢复为默认值，则输入以下命令：ZXROSNG(config)# no ip tcp synflood-protect one-minute





### 相关命令 


ip tcp synflood-protect enableshow tcp synflood-protect config



## ip tcp synwait-time 


ip tcp synwait-time 




### 命令功能 


该命令工作于全局配置模式，用于设置TCP SYNWAIT超时时间。配置成功后，当系统发起TCP建链请求，TCP连接处于SYNSENT状态的时间超过该设置的超时时间而没有收到对方回应的SYN+ACK报文，本端TCP将强行关闭该TCP连接；或者当系统被动响应TCP建链请求，TCP连接处于SYNRCVD状态的时间超过该设置的超时时间而没有收到对方回应的ACK报文，本端TCP将强行关闭该TCP连接。TCP SYNWAIT超时时间用于控制TCP三次握手的超时时间，超过该设置时间而没有完成三次握手过程的将强行关闭处于半连接状态(SYNSENT和SYNRCVD)的TCP连接。TCP状态迁移及SYNSENT、SYNRCVD状态介绍参见RFC793第3.2节。使用no命令恢复默认值。






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ip tcp synwait-time 
  ＜seconds 
＞

no ip tcp synwait-time 








### 命令参数解释 




参数|描述
---|---
＜seconds＞|TCP试探建链时间，单位：秒，范围30~80，缺省为30秒








### 缺省 


建立一个tcp连接的等待时间为30秒 






### 使用说明 


TCP SYNWAIT超时时间默认值是30秒，拥有管理员权限的操作员可以使用这条命令变更TCP SYNWAIT超时时间。配置变更后，TCP SYNWAIT超时时间只对新进入SYNSENT和SYNRCVD状态的TCP半连接生效，之前已经处于SYNSENT或SYNRCVD状态的TCP半连接的超时时间不会变化，依然使用配置前的超时时间。





### 范例 


设置TCP SYNWAIT超时时间为60秒，则输入以下命令：ZXROSNG(config)# ip tcp synwait-time 60去除设置TCP SYNWAIT超时时间，恢复为默认值30秒，则输入以下命令：ZXROSNG(config)# no ip tcp synwait-time





### 相关命令 


show tcp config 




## ip tcp window-size 


ip tcp window-size 




### 命令功能 


该命令工作于全局配置模式，用于设置TCP 接收窗口的大小。当需要提高TCP传输性能，可以使用该命令设置较大的接收窗口。配置成功后，新建立的TCP连接的接收窗口为该配置值，并在SYN报文中通告给TCP连接的对端。TCP接收窗口实现TCP的流量控制，TCP通过在交互报文中携带的接收窗口字段，通告TCP连接的对端：本端的接收能力。TCP连接的对端不能发送超过本端接收窗口大小的报文。使用no命令恢复默认值。






### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ip tcp window-size 
  ＜bytes 
＞

no ip tcp window-size 








### 命令参数解释 




参数|描述
---|---
＜bytes＞|TCP侦听方窗口大小，单位：字节，范围100~1048560，缺省为65535字节








### 缺省 


tcp连接的侦听方窗口为65535字节 






### 使用说明 


TCP 接收窗口默认值是65535字节，拥有管理员权限的操作员可以使用这条命令变更TCP接收窗口大小，以调整TCP连接的传输能力。配置变更后，TCP接收窗口只对新建的TCP连接生效，正在建链或者已经建链成功的TCP连接不会改变接收窗口值。





### 范例 


设置TCP 接收窗口为32678字节，则输入以下命令：ZXROSNG(config)# ip tcp window-size 32678去除设置TCP 接收窗口，恢复为默认值65535字节，则输入以下命令：ZXROSNG(config)# no ip tcp window-size





### 相关命令 


show tcp config 




## ipv6 tcp synflood-protect defence 


ipv6 tcp synflood-protect defence 




### 命令功能 


该命令工作于全局配置模式，用于配置TCP6 SYN Flood防护功能的防护模式。当需要变更TCP6 SYN Flood防护功能的防护模式，或者改变防护模式中的参数设置时，使用该命令。配置成功后，当系统受到TCP6 SYN Flood攻击时，系统将根据配置的防护模式及参数启动相应的防护策略，保证TCP6资源的可用性。TCP6 SYN Flood防护模式分为三种，0：删除TCP6半连接并且加快TCP6半连接的老化速度；1：删除TCP6半连接；2：加快TCP6半连接的老化速度。其中每次删除半连接的个数及TCP6半连接的老化时间均可通过参数设置。





### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv6 tcp synflood-protect defence 
  {＜defence-parameter-0 
＞ waittime 
 ＜wait-time 
＞ num 
 ＜half-connect-numbers 
＞|＜defence-parameter-1 
＞ num 
 ＜half-connect-numbers 
＞|＜defence-parameter-2 
＞ waittime 
 ＜wait-time 
＞}

no ipv6 tcp synflood-protect defence 








### 命令参数解释 




参数|描述
---|---
＜defence-parameter-0＞|和1、2是三选一。若设置为0，则TCP6 SYN Flood防护功能的防护模式为删除TCP6半连接，并且加快TCP6半连接的老化速度。
＜wait-time＞|设置TCP6半连接的老化时间，防护模式为0、2时可配置。取值范围：配置范围为1-80秒。默认值：30秒。
＜half-connect-numbers＞|设置每次删除TCP6半连接的个数，防护模式为0、1时可配置。取值范围：配置范围为1-65535个。默认值：1个。
＜defence-parameter-1＞|和0、2是三选一。若设置为1，则TCP6 SYN Flood防护功能的防护模式为删除TCP6半连接。
＜half-connect-numbers＞|设置每次删除TCP6半连接的个数，防护模式为0、1时可配置。取值范围：配置范围为1-65535个。默认值：1个。
＜defence-parameter-2＞|和0、1是三选一。若设置为2，则TCP6 SYN Flood防护功能的防护模式为加快TCP6半连接的老化速度。
＜wait-time＞|设置TCP6半连接的老化时间，防护模式为0、2时可配置。取值范围：配置范围为1-80秒。默认值：30秒。








### 缺省 


在TCP6 SYN Flood防护功能打开的情况下，默认配置是防护策略类型是减少SYN等待超时时间的同时还删除旧的半连接，SYN等待超时时间为30秒，半连接老化数为1。 






### 使用说明 


TCP6 SYN Flood防护功能的防护模式默认为0，即删除TCP6半连接并且加快TCP6半连接的老化速度，每次删除的TCP6半连接个数为1个，TCP6半连接的老化时间为30秒。拥有管理员权限的操作员可以使用该命令变更TCP6 SYN Flood防护功能的防护模式或者改变防护模式中的参数设置。当修改TCP6 SYN Flood防护功能的防护模式，或者修改防护模式中的参数设置后，需要开启TCP6 SYN Flood防护功能（参见配置命令ip TCP6 synflood-protect enable）才能生效。建议采用TCP6 SYN Flood防护功能的默认防护模式。拥有管理员权限的操作员可以根据实际情况变更每次删除TCP6半连接的个数以及TCP6半连接的老化时间，TCP6半连接的老化时间不建议配置为小于3秒，以防止正常的建链请求被误删除。





### 范例 


配置TCP6 SYN Flood防护功能的防护模式为0，并变更删除的TCP6半连接个数以及TCP6半连接的老化速度，则输入以下命令：ZXROSNG(config)# ipv6 tcp synflood-protect defence 0 waittime 10 num 100去配置TCP6 SYN Flood防护功能的防护模式，恢复为默认值，则输入以下命令：ZXROSNG(config)# no ipv6 tcp synflood-protect defence





### 相关命令 


ipv6 tcp synflood-protect enableshow tcp6 synflood-protect config



## ipv6 tcp synflood-protect enable 


ipv6 tcp synflood-protect enable 




### 命令功能 


该命令工作于全局配置模式，用于开启TCP6 SYN Flood防护功能。当需要保护系统的TCP6资源免受攻击时，使用该命令。配置成功后，当系统受到TCP6 SYN Flood攻击时，系统将采取一些措施删除或者加快老化TCP6半连接，保证TCP6资源的可用性。TCP6 SYN Flood攻击是攻击者发送大量伪造的SYN报文，并且不对被攻击者回应的SYN+ACK报文进行ACK回应，导致被攻击者系统中存在大量的TCP6半连接，消耗被攻击者系统TCP6资源，阻止被攻击者系统响应正常的TCP6建链请求，从而达到DoS(Deny of Service)的攻击目的。TCP6 SYN Flood防护功能就是为了防止该类DoS攻击，避免系统的TCP6资源被攻击者的半连接占满，保障系统可以响应正常的TCP6建链请求。





### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv6 tcp synflood-protect enable 
 

no ipv6 tcp synflood-protect enable 








### 命令参数解释 



					无
				 






### 缺省 


TCP6 SYN Flood防护功能关闭。 






### 使用说明 


TCP6 SYN Flood防护功能默认是关闭的，拥有管理员权限的操作员可以使用该命令开启TCP6 SYN Flood防护功能。配置该命令后，当TCP6连接个数占系统最大TCP6资源个数达到一定的比率(参见配置命令ipv6 tcp synflood-protect max-connect)，或者一分钟内建立的TCP6连接个数占系统最大TCP6资源个数达到一定的比率(参见配置命令ipv6 tcp synflood-protect one-minute)，TCP6 SYN Flood防护功能会删除或者加快老化一些TCP6半连接（参见配置命令ipv6 tcp synflood-protect defence）。通过no ipv6 tcp synflood-protect enable命令关闭TCP6 SYN Flood防护功能。





### 范例 


开启TCP6 SYN Flood防护功能，则输入以下命令：ZXROSNG(config)# ipv6 tcp synflood-protect enable关闭TCP6 SYN Flood防护功能，则输入以下命令：ZXROSNG(config)# no ipv6 tcp synflood-protect enable





### 相关命令 


show tcp6 synflood-protect config  




## ipv6 tcp synflood-protect max-connect 


ipv6 tcp synflood-protect max-connect 




### 命令功能 


该命令工作于全局配置模式，用于配置TCP6 SYN Flood防护功能的TCP6连接比率值。当需要修改TCP6 SYN Flood防护功能的TCP6连接比率值时，使用该命令。配置成功后，当系统的TCP6连接个数占系统最大TCP6资源个数的比率值达到配置的高比率值后，系统将根据配置的防护模式（参见配置命令ipv6 tcp synflood-protect defence）启动相应的防护策略，保证TCP6资源的可用性。比率值的配置分为高和低两个值，当TCP6连接个数占系统最大TCP6资源个数的比率值达到高比率值时，系统启动相应的防护策略，进入防御状态；达到低比率值时，系统进入告警状态，不启动防护策略。





### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv6 tcp synflood-protect max-connect 
  {[high 
 ＜high-number 
＞],[low 
 ＜low-number 
＞]}

no ipv6 tcp synflood-protect max-connect 








### 命令参数解释 




参数|描述
---|---
＜high-number＞|设置TCP6 SYN Flood防护功能的TCP6连接高比率值取值范围：配置范围为1-100，单位%。默认值：90%。
＜low-number＞|设置TCP6 SYN Flood防护功能的TCP6连接低比率值取值范围：配置范围为1-100，单位%。默认值：60%。








### 缺省 


在TCP6 SYN Flood防护功能打开的情况下， 默认配置是总连接数达到最大连接数的90%开始防御，达到60%进行告警。 






### 使用说明 


TCP6 SYN Flood防护功能的TCP6连接比率值分为高和低两个值，高比率值默认为90（单位%），低比率值默认为60（单位%），默认情况下系统TCP6连接个数占系统最大TCP6资源个数的比率值达到90%以后，系统将根据配置的防护模式（参见配置命令ip TCP6 synflood-protect defence）启动相应的防护策略。拥有管理员权限的操作员可以使用该命令修改TCP6 SYN Flood防护功能的TCP6连接比率值。配置的TCP6连接高比率值必须大于配置的TCP6连接低比率值，否则配置以报错结束。配置的TCP6连接高比率值不能小于配置的一分钟TCP6连接的高比率值（参见配置命令ipv6 tcp synflood-protect one-minute)；配置的TCP6连接低比率值不能小于配置的一分钟TCP6连接的低比率值（参见配置命令ipv6 tcp synflood-protect one-minute)；





### 范例 


配置TCP6 SYN Flood防护功能的TCP6连接高比率值80%，低比率值60%，则输入以下命令：ZXROSNG(config)# ipv6 tcp synflood-protect max-connect high 80 low 60去配置TCP6 SYN Flood防护功能的TCP6连接比率值，恢复为默认值，则输入以下命令：ZXROSNG(config)# no ipv6 tcp synflood-protect max-connect





### 相关命令 


ipv6 tcp synflood-protect enableshow tcp6 synflood-protect config



## ipv6 tcp synflood-protect one-minute 


ipv6 tcp synflood-protect one-minute 




### 命令功能 


该命令工作于全局配置模式，用于配置TCP6 SYN Flood防护功能的一分钟TCP6连接比率值。当需要变更TCP6 SYN Flood防护功能的一分钟TCP6连接比率值时，使用该命令。配置成功后，当系统受到TCP6 SYN Flood攻击时，且一分钟内新增的TCP6连接个数占系统最大TCP6资源个数的比率值达到该高比率值后，系统将根据配置的防护模式（参见配置命令ipv6 tcp synflood-protect defence）启动相应的防护策略，保证TCP6资源的可用性。比率值的配置分为高和低两个值，当一分钟内新增的TCP6连接个数占系统最大TCP6资源个数的比率值达到高比率值时，系统启动相应的防护策略，进入防御状态；达到低比率值时，系统进入告警状态，不启动防护策略。





### 命令模式 


 全局配置模式  






### 命令默认权限级别 


15 






### 命令格式 



ipv6 tcp synflood-protect one-minute 
  {[high 
 ＜high-number 
＞],[low 
 ＜low-number 
＞]}

no ipv6 tcp synflood-protect one-minute 








### 命令参数解释 




参数|描述
---|---
＜high-number＞|设置TCP6 SYN Flood防护功能的一分钟TCP6连接高比率值取值范围：配置范围为1-100，单位%。默认值：80%。
＜low-number＞|设置TCP6 SYN Flood防护功能的一分钟TCP6连接低比率值取值范围：配置范围为1-100，单位%。默认值：50%。








### 缺省 


在TCP6 SYN Flood防护功能打开的情况下， 默认配置是一分钟内达到最大连接数80%开始防御，达到最大连接数的50%进行告警。 






### 使用说明 


TCP6 SYN Flood防护功能的一分钟TCP6连接比率值分为高和低两个值，高比率值默认为80（单位%），低比率值默认为50（单位%），默认情况下一分钟内新增的TCP6连接个数占系统最大TCP6资源个数的比率值达到80%以后，系统将根据配置的防护模式（参见配置命令ip TCP6 synflood-protect defence）启动相应的防护策略。拥有管理员权限的操作员可以使用这条命令修改TCP6 SYN Flood防护功能的一分钟TCP6连接比率值。配置的一分钟TCP6连接高比率值必须大于配置的一分钟TCP6连接低比率值，否则配置以报错结束。配置的一分钟TCP6连接高比率值不能大于配置的TCP6连接高比率值(参见配置命令ipv6 tcp synflood-protect max-connect）；配置的一分钟TCP6连接低比率值不能大于配置的TCP6连接低比率值(参见配置命令ipv6 tcp synflood-protect max-connect）





### 范例 


配置TCP6 SYN Flood防护功能的一分钟TCP6连接高比率值70%，低比率值50%，则输入以下命令：ZXROSNG(config)# ipv6 tcp synflood-protect one-minute high 70 low 50去配置TCP6 SYN Flood防护功能的一分钟TCP6连接比率值，恢复为默认值，则输入以下命令：ZXROSNG(config)# no ipv6 tcp synflood-protect one-minute





### 相关命令 


ipv6 tcp synflood-protect enableshow tcp6 synflood-protect config



## show debug tcp 


show debug tcp 




### 命令功能 


该命令工作于除用户模式外的其他所有模式，用于显示系统中TCP debug的开启情况。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show debug tcp 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


当需要显示当前系统的TCP debug开启情况时，使用该命令。 






### 范例 


通过show命令显示系统TCP debug开启情况，则输入以下命令：ZXROSNG#show debug tcpTCP:  TCP driver event debugging is on  TCP driver verbose debugging is on  TCP packet debugging is on  TCP special debugging is on输出信息中的参数信息解释如下：参数名称                                参数说明TCP                                     表示显示的是TCP模块的debug信息TCP driver event debugging is on        TCP控制信息debug开关（参见操作命令debug ip tcp driver）打开TCP driver verbose debugging is on      TCP报文相关的控制信息debug开关（参见操作命令debug ip tcp driver-pak）打开TCP packet debugging is on              TCP报文收发debug开关（参见操作命令debug ip tcp packet）打开TCP special debugging is on             TCP重要处理信息debug开关（参见操作命令debug ip tcp transactions）打开






### 相关命令 


debug ip tcp alldebug ip tcp driverdebug ip tcp driver-pakdebug ip tcp packetdebug ip tcp transactions



## show debug udp 


show debug udp 




### 命令功能 


该命令工作于除用户模式外的其他所有模式，用于显示系统中UDP debug的开启情况。 






### 命令模式 


 除用户模式外的其他所有模式  






### 命令默认权限级别 


15 






### 命令格式 




show debug udp 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


当需要显示当前系统的UDP debug开启情况时，使用该命令。 






### 范例 


ZXROSNG#debug  ip  udp  UDP packet debugging is onZXROSNG#show debug udpUDP:  UDP packet debugging is on





### 相关命令 


debug  ip  udp  



## show tcp brief 


show tcp brief 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示系统中所有TCP连接的简要信息，包括本地地址和端口、远端地址和端口、TCP连接状态等信息。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


除用户模式外的其他所有模式:15,用户模式:1 






### 命令格式 




show tcp brief 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


无 






### 范例 


通过show命令显示系统所有TCP连接简要信息，则输入以下命令：ZXROSNG(config)#sho tcp briefTCB Index   Local Address          Foreign Address        State6           1.1.1.1:21418          1.1.1.2:179            SYNSENT             7           2.2.2.1:21419          2.2.2.2:179            ESTAB输出信息中的参数信息解释如下：参数名称         参数说明TCB Index         TCP连接在本地的索引值Local Address         TCP连接本端地址和端口号，中间用分号隔开Foreign Address         TCP连接远端地址和端口号，中间用分号隔开State                 TCP连接状态，包括LISTEN、SYNSENT、SYNRCVD、ESTAB、FINWAIT-1、FINWAIT-2、CLOSEWAIT、CLOSING、LASTACK、TIMEWAIT、CLOSED等等，具体参见RFC793第3.2节






### 相关命令 


无 




## show tcp config 


show tcp config 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示系统TCP的配置信息，包括FINWAIT-2老化时间配置（参见配置命令ip tcp finwait-time）、SYNWAIT老化时间配置（参见配置命令ip tcp synwait-time）、接收窗口配置（参见配置命令ip tcp window-size）。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


用户模式:1,除用户模式外的其他所有模式:15 






### 命令格式 




show tcp config 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


该命令用于显示系统TCP的配置信息，当未配置数据时，显示系统默认值。 






### 范例 


通过show命令显示系统TCP配置信息，则输入以下命令：ZXROSNG(config)#ip tcp finwait-time 100ZXROSNG(config)#ip tcp synwait-time 40ZXROSNG(config)#ip tcp window-size 65535ZXROSNG(config)#show tcp config TCP SYNWAIT:           40TCP FINWAIT:          100TCP WINDOWSIZE:     65535输出信息中的参数信息解释如下：参数名称    参数说明TCP SYNWAIT    ip tcp synwait-time配置值，未配置时默认为30秒TCP FINWAIT    ip tcp finwait-time配置值，未配置时默认为150秒TCP WINDOWSIZE    ip tcp window-size配置值，未配置时默认为32768





### 相关命令 


ip tcp finwait-time<wait-time>ip tcp window-size<window-size>ip tcp synwait-time<wait-time>



## show tcp idle-connection 


show tcp idle-connection 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示系统中所有处于空闲（没有数据交互）时长等于或大于设定时长的TCP连接的简要信息，包括本地地址和端口、远端地址和端口、TCP连接状态、空闲时长等信息。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


除用户模式外的其他所有模式:15,用户模式:1 






### 命令格式 




show tcp idle-connection 
  [＜idle-time 
＞] 







### 命令参数解释 




参数|描述
---|---
＜idle-time＞|空闲时间，范围10-10080，单位分钟，显示空闲超过idle-time的TCP连接信息；如果不指定时间进行查询，则显示空闲时间超过120分钟的TCP连接信息。








### 缺省 


无 






### 使用说明 


无





### 范例 


通过show命令显示系统所有空闲时长等于或大于指定时长的TCP连接简要信息，则输入以下命令：ZXROSNG(config)#show tcp idle-connetion 10TCB Index   Local Address    Foreign Address    State     Idle7           2.2.2.1:21419    2.2.2.2:179        ESTAB     15输出信息中的参数信息解释如下：参数名称        参数说明TCB Index       TCP连接在本地的索引值Local Address   TCP连接本端地址和端口号，中间用冒号隔开Foreign Address TCP连接远端地址和端口号，中间用冒号隔开State           TCP连接状态，包括LISTEN、SYNSENT、SYNRCVD、ESTAB、FINWAIT-1、FINWAIT-2、CLOSEWAIT、CLOSING、LASTACK、TIMEWAIT、CLOSED等等，具体参见RFC793第3.2节Idle            TCP 连接空闲时长，单位为分钟






### 相关命令 


show tcp briefshow tcp tcb <tcb-index>



## show tcp resource 


show tcp resource 




### 命令功能 


查询设备上TCP资源信息 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


除用户模式外的其他所有模式:15,用户模式:1 






### 命令格式 




show tcp resource 
 







### 命令参数解释 



					无
				 






### 缺省 


缺省 






### 使用说明 


使用show tcp resource命令来查询当前设备TCP资源 






### 范例 


RP1#show tcp resource Instance:1, Resource limit:5120, Current connections:8LISTEN       7                      SYNSENT        0SYNRCVD      0                      ESTAB          1FINWAIT-1    0                      FINWAIT-2      0CLOSING      0                      CLOSEWAIT      0LAST-ACK     0                      TIMEWAIT       0
Instance:2, Resource limit:5120, Current connections:3LISTEN       2                      SYNSENT        0SYNRCVD      0                      ESTAB          1FINWAIT-1    0                      FINWAIT-2      0CLOSING      0                      CLOSEWAIT      0LAST-ACK     0                      TIMEWAIT       0
Instance:3, Resource limit:5120, Current connections:4LISTEN       2                      SYNSENT        0SYNRCVD      0                      ESTAB          2FINWAIT-1    0                      FINWAIT-2      0CLOSING      0                      CLOSEWAIT      0LAST-ACK     0                      TIMEWAIT       0
Instance:4, Resource limit:5120, Current connections:4LISTEN       2                      SYNSENT        0SYNRCVD      0                      ESTAB          2FINWAIT-1    0                      FINWAIT-2      0CLOSING      0                      CLOSEWAIT      0LAST-ACK     0                      TIMEWAIT       0
Instance:5, Resource limit:5120, Current connections:3LISTEN       2                      SYNSENT        0SYNRCVD      0                      ESTAB          1FINWAIT-1    0                      FINWAIT-2      0CLOSING      0                      CLOSEWAIT      0LAST-ACK     0                      TIMEWAIT       0






### 相关命令 


缺省 




## show tcp statistics 


show tcp statistics 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示系统TCP统计信息，包括收发报文信息、连接建立情况等统计信息。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


用户模式:1,除用户模式外的其他所有模式:15 






### 命令格式 




show tcp statistics 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


无 






### 范例 


通过show命令显示系统TCP统计信息，则输入如下命令：ZXROSNG#show tcp statistics Rcvd: 26 Total, 0 no port      0 checksum error, 0 bad offset, 0 too short      25 packets (262 bytes) in sequence      0 out-of-order packets (0 bytes)      0 packets (0 bytes) with data after window      0 packets after close      0 window probe packets, 0 window update packets      0 dup ack packets, 0 ack packets with unsend data      25 ack packets (262 bytes)Sent: 1852 Total, 0 urgent packets      1829 control packets (including 1667 retransmitted)       13 data packets (281 bytes)      0 data packets (0 bytes) retransmitted      10 ack only packets (0 delayed)      0 window probe packets, 0 window update packets161 Connections initiated, 1 connections accepted1 Connections established,161 connections closed1667 Total rxmt timeout, 0 connections dropped in rxmt timeout26 Keepalive timeout, 0 keepalive probe0 Connections dropped in keepalive输出信息中的参数信息解释如下：参数名称                                 参数说明Rcvd                                         TCP接收报文统计情况Total                                        TCP接收报文总数no port                                      TCP接收匹配端口失败的报文个数checksum error                               TCP接收校验和错误的报文个数bad offset                                   TCP接收包头长度错误的报文个数     too short                                    TCP接收长度错误的报文个数packets (bytes) in sequence                  TCP接收符合预期序列号报文个数以及对应的字节数，例如25 ack packets (262 bytes)，表示TCP接收符合预期序列号报文25个，对应的字节数为262 bytes。out-of-order packets(bytes)                  TCP接收失序的报文个数以及对应的字节数，例如0 out-of-order packets (0 bytes)，表示TCP接收时序的报文个数为0，对应的字节数为0。packets (bytes) with data after window       TCP接收序列号在接收窗口之外的报文个数以及对应的字节数，例如0 packets (0 bytes) with data after window，表示TCP接收序列号在接收窗口之外的报文个数为0个，对应的字节数为0。packets after close                          TCP处于CLOSED状态接收的报文个数window probe packets                         TCP接收的窗口探测报文个数window update packets                        TCP接收的窗口更新报文个数dup ack packets                              TCP接收的重复ACK个数ack packets with unsend data                 TCP接收的未发送数据的ACK报文个数ack packets ( bytes)                         TCP接收的ACK报文个数以及确认的字节数，例如25 ack packets (262 bytes)，表示TCP接收到ack确认报文25个，确认262个字节。Sent                                         TCP发送报文统计情况Total                                        TCP发送的报文总个数urgent packets                               TCP发送的携带Urgent标记的报文个数control packets (including retransmitted)    TCP发送的控制报文个数（包括SYN、FIN、RST），包含重传的控制报文个数。例如1829 control packets (including 1667 retransmitted)，表示TCP发送的控制报文1829个，重传的控制报文个数为1667个。data packets (bytes)                         TCP发送的携带数据的报文个数以及对应的字节数，例如13 data packets (281 bytes)，表示TCP发送鞋带数据的报文个数13个，携带的字节数为281 bytes。data packets (bytes) retransmitted           TCP重传的数据报文个数以及对应的字节数，例如0 data packets (0 bytes) retransmitted，表示TCP重传的数据报文个数为0，重传字节数为0 bytes。ack only packets(delayed)                    TCP发送的纯ACK报文个数以及延时确认的ACK报文个数，例如10 ack only packets (0 delayed)，表示TCP发送的纯ACK报文个数为10个，延时确认的ACK报文个数为0个。window probe packets                         TCP发送的窗口探测报文个数window update packets                        TCP发送的窗口更新报文个数Connections initiated                        TCP主动建链的连接个数connections accepted                         TCP被动建链的连接个数Connections established                      TCP建链成功的连接个数connections closed                           TCP关闭的连接个数Total rxmt timeout                           TCP重传的次数connections dropped in rxmt timeout          TCP因为重传超时关闭的连接个数Keepalive timeout                            TCP Keepalive超时次数keepalive probe                              TCP Keepalive探测次数Connections dropped in keepalive             TCP因为Keepalive探测失败而关闭的连接个数






### 相关命令 


无 




## show tcp synflood-protect all 


show tcp synflood-protect all 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示TCP SYN Flood防护功能的配置信息以及统计信息。当需要查看TCP SYN Flood防护功能的配置信息、防护状态或者统计信息时，使用该命令。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


用户模式:1,除用户模式外的其他所有模式:15 






### 命令格式 




show tcp synflood-protect all 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


该命令显示的TCP SYN Flood防护功能的配置信息包括：1、配置的TCP SYN Flood防护功能的开启和关闭状态（参见配置命令ip tcp synflood-protect enable）；2、配置的TCP SYN Flood防护功能的防护模式及参数值（参见配置命令ip tcp synflood-protect defence）；3、配置的TCP SYN Flood防护功能的TCP连接比率值（参见配置命令ip tcp synflood-protect max-connect）；4、配置的TCP SYN Flood防护功能的一分钟TCP连接比率值（参见配置命令ip tcp synflood-protect one-minute）。该命令显示的TCP SYN Flood防护功能的统计信息包括：1、TCP SYN Flood防护功能所处的实例；2、TCP SYN Flood防护功能的防御状态；3、系统当前的TCP连接个数；4、系统当前的TCP半连接个数；5、系统一分钟内新增的TCP连接个数；6、系统一分钟内新增的TCP半连接个数；7、系统最大TCP资源个数；8、TCP连接个数占系统最大TCP资源个数的比率值；9、一分钟内新增TCP连接个数占系统最大TCP资源个数比率值。当TCP连接个数占系统最大TCP资源个数的比率值，大于配置的TCP SYN Flood防护功能的TCP连接比率值，或者一分钟内新增TCP连接个数占系统最大TCP资源个数比率值，大于配置的TCP SYN Flood防护功能的一分钟TCP连接比率值时，系统将根据配置的TCP SYN Flood防护功能的防护模式及参数值进行防御。





### 范例 


通过show命令显示TCP SYN Flood防护功能的配置信息和统计信息，则输入以下命令：ZXROSNG(config)#show tcp synflood-protect allconfiguration information:synflood-prevent is enableprevent means is quickening the TCP connection aging and deleting the old TCP half-connections  syn-waittime  is 10 (seconds)old-half-connect is 100max-connect high limit is 80%max-connect low limit is 60%one-minute high limit is 70%one-minute low limit is 50%statistics information:                                       maxcon:current total connectionsmaxhcon:current total half-connectionsonecon:oneminute connections    onehcon:oneminute half-connections  maxper:maxcon/tolcon*100%       oneper:onecon/tolcon*100%           tolcon:max connections of the cpu allowed   instance  status    maxcon  maxhcon onecon  onehcon tolcon  maxper    oneper    1         safety    4       0       0       0       5120    0.08%     0.00%    2         safety    4       0       0       0       5120    0.08%     0.00%    3         safety    4       0       0       0       5120    0.08%     0.00%    4         safety    4       0       0       0       5120    0.08%     0.00%    5         safety    4       0       0       0       5120    0.08%     0.00%输出信息中的参数信息解释如下：参数名称                  参数说明syn-waittime              配置的TCP老化时间old-half-connect          配置的每次删除的TCP半连接个数max-connect high limit    配置的TCP连接高比率值，TCP连接个数比率超过该值时，启动TCP防护策略max-connect low limit     配置的TCP连接低比率值one-minute high limit     配置的一分钟内新增TCP连接高比率值，一分钟内新增的TCP连接个数比率超过该值时，启动TCP防护策略one-minute low limit      配置的一分钟内新增TCP连接低比率值instance                  TCP SYN Flood防护功能所处的实例status                    TCP SYN Flood防护功能的防御状态maxcon                    系统当前的TCP连接个数maxhcon                   系统当前的TCP半连接个数onecon                    系统一分钟内新增的TCP连接个数onehcon                   系统一分钟内新增的TCP半连接个数tolcon                    系统最大TCP资源个数maxper                    TCP连接个数占系统最大TCP资源个数的比率值oneper                    一分钟内新增的TCP连接个数占系统最大TCP资源个数比率值






### 相关命令 


ip tcp synflood-protect enableip tcp synflood-protect defenceip tcp synflood-protect max-connectip tcp synflood-protect one-minute



## show tcp synflood-protect config 


show tcp synflood-protect config 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示TCP SYN Flood防护功能的配置信息。当需要查看TCP SYN Flood防护功能的配置信息时，使用该命令。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


除用户模式外的其他所有模式:15,用户模式:1 






### 命令格式 




show tcp synflood-protect config 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


该命令显示的TCP SYN Flood防护功能的配置信息包括：1、配置的TCP SYN Flood防护功能的开启和关闭状态（参见配置命令ip tcp synflood-protect enable）；2、配置的TCP SYN Flood防护功能的防护模式及参数值（参见配置命令ip tcp synflood-protect defence）；3、配置的TCP SYN Flood防护功能的TCP连接比率值（参见配置命令ip tcp synflood-protect max-connect）；4、配置的TCP SYN Flood防护功能的一分钟TCP连接比率值（参见配置命令ip tcp synflood-protect one-minute）。





### 范例 


通过show命令显示TCP SYN Flood防护功能的配置信息，则输入以下命令：ZXROSNG(config)#show tcp synflood-protect configsynflood-prevent is enableprevent means is quickening the TCP connection aging and deleting the old TCP half-connections  syn-waittime  is 10 (seconds)old-half-connect is 100max-connect high limit is 80%max-connect low limit is 60%one-minute high limit is 70%one-minute low limit is 50%输出信息中的参数信息解释如下：参数名称                  参数说明syn-waittime              配置的TCP老化时间old-half-connect          配置的每次删除的TCP半连接个数max-connect high limit    配置的TCP连接高比率值，TCP连接个数比率超过该值时，启动TCP防护策略max-connect low limit     配置的TCP连接低比率值one-minute high limit     配置的一分钟内新增TCP连接高比率值，一分钟内新增的TCP连接个数比率超过该值时，启动TCP防护策略one-minute low limit      配置的一分钟内新增TCP连接低比率值






### 相关命令 


ip tcp synflood-protect enableip tcp synflood-protect defenceip tcp synflood-protect max-connectip tcp synflood-protect one-minute




## show tcp synflood-protect statistics 


show tcp synflood-protect statistics 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示TCP SYN Flood防护功能的统计信息。当需要查看TCP SYN Flood防护功能的防护状态或者统计信息时，使用该命令。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


用户模式:1,除用户模式外的其他所有模式:15 






### 命令格式 




show tcp synflood-protect statistics 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


该命令显示的TCP SYN Flood防护功能的统计信息包括：1、TCP SYN Flood防护功能所处的实例；2、TCP SYN Flood防护功能的防御状态；3、系统当前的TCP连接个数；4、系统当前的TCP半连接个数；5、系统一分钟内新增的TCP连接个数；6、系统一分钟内新增的TCP半连接个数；7、系统最大TCP资源个数；8、TCP连接个数占系统最大TCP资源个数的比率值；9、一分钟内新增TCP连接个数占系统最大TCP资源个数比率值。当TCP连接个数占系统最大TCP资源个数的比率值，大于配置的TCP SYN Flood防护功能的TCP连接比率值，或者一分钟内新增TCP连接个数占系统最大TCP资源个数比率值，大于配置的TCP SYN Flood防护功能的一分钟TCP连接比率值时，系统将根据配置的TCP SYN Flood防护功能的防护模式及参数值进行防御。





### 范例 


通过show命令显示TCP SYN Flood防护功能的统计信息，则输入以下命令：ZXROSNG(config)#show tcp synflood-protect statistics              maxcon:current total connectionsmaxhcon:current total half-connectionsonecon:oneminute connections    onehcon:oneminute half-connections  maxper:maxcon/tolcon*100%       oneper:onecon/tolcon*100%           tolcon:max connections of the cpu allowed         instance  status    maxcon  maxhcon onecon  onehcon tolcon  maxper    oneper    1         safety    4       0       0       0       5120    0.08%     0.00%    2         safety    4       0       0       0       5120    0.08%     0.00%    3         safety    4       0       0       0       5120    0.08%     0.00%    4         safety    4       0       0       0       5120    0.08%     0.00%    5         safety    4       0       0       0       5120    0.08%     0.00%输出信息中的参数信息解释如下：参数名称          参数说明instance          TCP SYN Flood防护功能所处的实例status            TCP SYN Flood防护功能的防御状态maxcon            系统当前的TCP连接个数maxhcon           系统当前的TCP半连接个数onecon            系统一分钟内新增的TCP连接个数onehcon           系统一分钟内新增的TCP半连接个数tolcon            系统最大TCP资源个数maxper            TCP连接个数占系统最大TCP资源个数的比率值，单位百分比oneper            一分钟内新增的TCP连接个数占系统最大TCP资源个数比率值，单位百分比





### 相关命令 


ip tcp synflood-protect enableip tcp synflood-protect defenceip tcp synflood-protect max-connectip tcp synflood-protect one-minute




## show tcp tcb 


show tcp tcb 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示系统中指定TCP的连接信息，包括本地地址和端口、远端地址和端口、TCP连接状态、序列号和确认号、收发报文个数等信息。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


除用户模式外的其他所有模式:15,用户模式:1 






### 命令格式 




show tcp tcb 
  ＜tcb-index 
＞ 







### 命令参数解释 




参数|描述
---|---
＜tcb-index＞|TCP本地索引号，可通过show tcp brief命令查询有效范围：1-4294967295








### 缺省 


无 






### 使用说明 


该命令显示的TCP 连接信息和show tcp命令一致，区别是show tcp显示所有连接的信息，show tcp tcb显示的是指定索引号的TCP连接信息。 






### 范例 


通过show命令显示系统TCP索引为2的TCP连接信息，则输入以下命令：ZXROSNG#show tcp tcb 2Stand-alone TCP connection from host 1.1.1.2Connection state is ESTABLocal host: 1.1.1.1, Local port: 179 Foreign host: 1.1.1.2, Foreign port: 22868Event Timers (Current time is 0x15c180d0):Timer               Starts            WakeupsRetrans                  6                  0TimeWait                 0                  0AckHold                  2                  0KeepAlive               11                 11Persist                  0                  0SynWait                  1                  0FinWait                  0                  0iss: 1004866784  snduna: 1004866914  sndnxt: 1004866914  sndwnd: 32768irs: 1217962500  rcvnxt: 1217962630  rcvwnd: 65535SRTT: 280 ms, RTTO:  411 ms, KRTT: 411 ms minRTT: 213 ms,  maxRTT: 377 ms,  ACK hold: 200 msFlags: passive openDatagrams (max data segment is 536 bytes):Rcvd: 11 (out of order: 0), with data: 5, total data bytes: 129Sent: 9 (retransmit: 0), with data: 5, total data bytes: 129输出信息中的参数信息解释如下：参数名称                              参数说明Stand-alone TCP connection from host  TCP连接的远端IP地址Connection state is ESTAB             TCP连接状态，包括LISTEN、SYNSENT、SYNRCVD、ESTAB、FINWAIT-1、FINWAIT-2、CLOSEWAIT、CLOSING、LASTACK、TIMEWAIT、CLOSED，具体参见RFC793第3.2节Local host                            TCP连接本端地址Local port                            TCP连接本端端口Foreign host                          TCP连接远端地址Foreign port                          TCP连接远端端口Event Timers                          显示事件定时器信息，包括Retrans（重传定时器）、TimeWait（TimeWait定时器）、AckHold（延时ACK定时器）、KeepAlive（KeepAlive保活定时器）、Persist（零窗口探测定时器）、SynWait（SYNWAIT超时定时器）、FinWait（FINWAIT-2超时定时器）Timer                                 显示的是事件定时器的类型Retrans                               重传定时器。TCP发送的数据报文在RTO时间内没有收到对端的确认，触发重传定时器重传该报文，确保数据传输的可靠性TimeWait                              TimeWait定时器。TCP连接主动关闭方在删除TCP资源前需要等待一段时间，以确定本端最后发送的ACK报文被对端正确接收了，该等待时间即为TimeWait定时器所控制AckHold                               延时ACK定时器。为了节约网络带宽，TCP约定无需对每个数据报文都进行ACK确认，一般建议收到两个数据报文再进行一次ACK合并确认，但对端未必连续发送偶数个数报文，因此需要设置一个延时ACK定时器，以便在该定时器超时后及时确认对端发送的单个报文KeepAlive                             KeepAlive保活定时器。TCP连接建立后，如果长时间没有报文交互，则由该保活定时器触发发送保活报文探测对端TCP连接是否正常，以便在对端异常关闭情况下，本端的TCP资源能够被释放Persist                               零窗口探测定时器。TCP对端通告的接收窗口为0后，本端将不能继续发送新的数据，启用该定时器是为了探测对端接收窗口的恢复情况，以便本端能够及时恢复数据的发送SynWait                               SYNWAIT超时定时器。控制TCP三次握手超时的定时器，具体参见配置命令ip tcp synwait-time中的介绍FinWait                               FINWAIT-2超时定时器。控制TCP FINWAIT-2超时的定时器，具体参见配置命令ip tcp finwait-time中的介绍Starts                                定时器启动次数Wakeups                               定时器超时次数iss(Initial send sequence number)     TCP发送初始序列号                                snduna                                TCP发送并且得到对方ACK确认的序列号(Last send sequence number that the local host sent but has not received an acknowledgment for)sndnxt                                TCP下次发送新数据的序列号(Sequence number the local host will send next)sndwnd                                TCP发送窗口值，表示TCP能发送的最大字节数irs(Initial receive sequence number)  TCP接收初始序列号                           rcvnxt                                TCP接收并且已经确认的序列号(Last receive sequence number that the local host has acknowledged)rcvwnd                                TCP本端接收窗口大小，可通过配置命令ip tcp window-size配置其最大值SRTT(Smoothed Round-Trip Timeout)     TCP报文传输的平滑往返时间                                     RTTO(Round-Trip Timeout)              TCP报文传输的往返时间，用于重传定时器设置重传超时时间KRTT                                  记录TCP上次重传的超时时间 minRTT                                TCP计算得到的往返时间最小值maxRTT                                TCP计算得到的往返时间最大值ACK hold                              延时ACK的延时等待时间Flags: active open                    TCP主动建链或者被动建链标志。active open：主动建链，passive open：被动建链Datagrams (max data segment is 536 bytes) TCP 协商的MSS大小，TCP传输报文的最大长度Rcvd                                  TCP接收到的总报文个数out of order                          TCP接收到的先序报文个数with data                             TCP接收的带数据的报文个数total data bytes                      TCP接收的总字节数Sent                                  TCP发送的总报文个数retransmit                            TCP重传的报文个数with data                             TCP发送的带数据的报文个数total data bytes                      TCP发送的总字节数





### 相关命令 


show tcp brief 




## show tcp 


show tcp 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示系统中所有TCP的连接信息，包括本地地址和端口、远端地址和端口、TCP连接状态、序列号和确认号、收发报文个数等信息。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


用户模式:1,除用户模式外的其他所有模式:15 






### 命令格式 




show tcp 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


无 






### 范例 


通过show命令显示系统所有TCP连接信息，则输入以下命令：ZXROSNG#show tcp Stand-alone TCP connection from host 1.1.1.2Connection state is ESTABLocal host: 1.1.1.1, Local port: 179 Foreign host: 1.1.1.2, Foreign port: 22868Event Timers (Current time is 0x15c180d0):Timer               Starts            WakeupsRetrans                  6                  0TimeWait                 0                  0AckHold                  2                  0KeepAlive               11                 11Persist                  0                  0SynWait                  1                  0FinWait                  0                  0iss: 1004866784  snduna: 1004866914  sndnxt: 1004866914  sndwnd: 32768irs: 1217962500  rcvnxt: 1217962630  rcvwnd: 65535SRTT: 280 ms, RTTO:  411 ms, KRTT: 411 ms minRTT: 213 ms,  maxRTT: 377 ms,  ACK hold: 200 msFlags: passive openDatagrams (max data segment is 536 bytes):Rcvd: 11 (out of order: 0), with data: 5, total data bytes: 129Sent: 9 (retransmit: 0), with data: 5, total data bytes: 129输出信息中的参数信息解释如下：参数名称                              参数说明Stand-alone TCP connection from host  TCP连接的远端IP地址Connection state is ESTAB             TCP连接状态，包括LISTEN、SYNSENT、SYNRCVD、ESTAB、FINWAIT-1、FINWAIT-2、CLOSEWAIT、CLOSING、LASTACK、TIMEWAIT、CLOSED，具体参见RFC793第3.2节Local host                            TCP连接本端地址Local port                            TCP连接本端端口Foreign host                          TCP连接远端地址Foreign port                          TCP连接远端端口Event Timers                          显示事件定时器信息，包括Retrans（重传定时器）、TimeWait（TimeWait定时器）、AckHold（延时ACK定时器）、KeepAlive（KeepAlive保活定时器）、Persist（零窗口探测定时器）、SynWait（SYNWAIT超时定时器）、FinWait（FINWAIT-2超时定时器）Timer                                 显示的是事件定时器的类型Retrans                               重传定时器。TCP发送的数据报文在RTO时间内没有收到对端的确认，触发重传定时器重传该报文，确保数据传输的可靠性TimeWait                              TimeWait定时器。TCP连接主动关闭方在删除TCP资源前需要等待一段时间，以确定本端最后发送的ACK报文被对端正确接收了，该等待时间即为TimeWait定时器所控制AckHold                               延时ACK定时器。为了节约网络带宽，TCP约定无需对每个数据报文都进行ACK确认，一般建议收到两个数据报文再进行一次ACK合并确认，但对端未必连续发送偶数个数报文，因此需要设置一个延时ACK定时器，以便在该定时器超时后及时确认对端发送的单个报文KeepAlive                             KeepAlive保活定时器。TCP连接建立后，如果长时间没有报文交互，则由该保活定时器触发发送保活报文探测对端TCP连接是否正常，以便在对端异常关闭情况下，本端的TCP资源能够被释放Persist                               零窗口探测定时器。TCP对端通告的接收窗口为0后，本端将不能继续发送新的数据，启用该定时器是为了探测对端接收窗口的恢复情况，以便本端能够及时恢复数据的发送SynWait                               SYNWAIT超时定时器。控制TCP三次握手超时的定时器，具体参见配置命令ip tcp synwait-time中的介绍FinWait                               FINWAIT-2超时定时器。控制TCP FINWAIT-2超时的定时器，具体参见配置命令ip tcp finwait-time中的介绍Starts                                定时器启动次数Wakeups                               定时器超时次数iss(Initial send sequence number)     TCP发送初始序列号                                snduna                                TCP发送并且得到对方ACK确认的序列号(Last send sequence number that the local host sent but has not received an acknowledgment for)sndnxt                                TCP下次发送新数据的序列号(Sequence number the local host will send next)sndwnd                                TCP发送窗口值，表示TCP能发送的最大字节数irs(Initial receive sequence number)  TCP接收初始序列号                           rcvnxt                                TCP接收并且已经确认的序列号(Last receive sequence number that the local host has acknowledged)rcvwnd                                TCP本端接收窗口大小，可通过配置命令ip tcp window-size配置其最大值SRTT(Smoothed Round-Trip Timeout)     TCP报文传输的平滑往返时间                                     RTTO(Round-Trip Timeout)              TCP报文传输的往返时间，用于重传定时器设置重传超时时间KRTT                                  记录TCP上次重传的超时时间 minRTT                                TCP计算得到的往返时间最小值maxRTT                                TCP计算得到的往返时间最大值ACK hold                              延时ACK的延时等待时间Flags: active open                    TCP主动建链或者被动建链标志。active open：主动建链，passive open：被动建链Datagrams (max data segment is 536 bytes) TCP 协商的MSS大小，TCP传输报文的最大长度Rcvd                                  TCP接收到的总报文个数out of order                          TCP接收到的先序报文个数with data                             TCP接收的带数据的报文个数total data bytes                      TCP接收的总字节数Sent                                  TCP发送的总报文个数retransmit                            TCP重传的报文个数with data                             TCP发送的带数据的报文个数total data bytes                      TCP发送的总字节数





### 相关命令 


无 




## show tcp6 synflood-protect all 


show tcp6 synflood-protect all 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示TCP6 SYN Flood防护功能的配置信息以及统计信息。当需要查看TCP6 SYN Flood防护功能的配置信息、防护状态或者统计信息时，使用该命令。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


用户模式:1,除用户模式外的其他所有模式:15 






### 命令格式 




show tcp6 synflood-protect all 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


该命令显示的TCP6 SYN Flood防护功能的配置信息包括：1、配置的TCP6 SYN Flood防护功能的开启和关闭状态（参见配置命令ipv6 tcp synflood-protect enable）；2、配置的TCP6 SYN Flood防护功能的防护模式及参数值（参见配置命令ipv6 tcp synflood-protect defence）；3、配置的TCP6 SYN Flood防护功能的TCP6连接比率值（参见配置命令ipv6 tcp synflood-protect max-connect）；4、配置的TCP6 SYN Flood防护功能的一分钟TCP6连接比率值（参见配置命令ipv6 tcp  synflood-protect one-minute）。该命令显示的TCP6 SYN Flood防护功能的统计信息包括：1、TCP6 SYN Flood防护功能所处的实例；2、TCP6 SYN Flood防护功能的防御状态；3、系统当前的TCP6连接个数；4、系统当前的TCP6半连接个数；5、系统一分钟内新增的TCP6连接个数；6、系统一分钟内新增的TCP6半连接个数；7、系统最大TCP6资源个数；8、TCP6连接个数占系统最大TCP6资源个数的比率值；9、一分钟内新增TCP6连接个数占系统最大TCP6资源个数比率值。当TCP6连接个数占系统最大TCP6资源个数的比率值，大于配置的TCP6 SYN Flood防护功能的TCP6连接比率值，或者一分钟内新增TCP6连接个数占系统最大TCP6资源个数比率值，大于配置的TCP6 SYN Flood防护功能的一分钟TCP6连接比率值时，系统将根据配置的TCP6 SYN Flood防护功能的防护模式及参数值进行防御。





### 范例 


通过show命令显示TCP6 SYN Flood防护功能的配置信息和统计信息，则输入以下命令：ZXROSNG(config)#show tcp6 synflood-protect allconfiguration information:synflood-prevent is enableprevent means is quickening the TCP6 connection aging and deleting the old TCP6 half-connections  syn-waittime  is 10 (seconds)old-half-connect is 100max-connect high limit is 80%max-connect low limit is 60%one-minute high limit is 70%one-minute low limit is 50%statistics information:                                       maxcon:current total connectionsmaxhcon:current total half-connectionsonecon:oneminute connections    onehcon:oneminute half-connections  maxper:maxcon/tolcon*100%       oneper:onecon/tolcon*100%           tolcon:max connections of the cpu allowed         instance  status    maxcon  maxhcon onecon  onehcon tolcon  maxper    oneper    1         safety    4       0       0       0       5120    0.08%     0.00%    2         safety    4       0       0       0       5120    0.08%     0.00%    3         safety    4       0       0       0       5120    0.08%     0.00%    4         safety    4       0       0       0       5120    0.08%     0.00%    5         safety    4       0       0       0       5120    0.08%     0.00% 输出信息中的参数信息解释如下：参数名称                  参数说明syn-waittime              配置的TCP6老化时间old-half-connect          配置的每次删除的TCP6半连接个数max-connect high limit    配置的TCP6连接高比率值，TCP6连接个数比率超过该值时，启动TCP6防护策略max-connect low limit     配置的TCP6连接低比率值one-minute high limit     配置的一分钟内新增TCP6连接高比率值，一分钟内新增的TCP6连接个数比率超过该值时，启动TCP6防护策略one-minute low limit      配置的一分钟内新增TCP6连接低比率值instance                  TCP6 SYN Flood防护功能所处的实例status                    TCP6 SYN Flood防护功能的防御状态maxcon                    系统当前的TCP6连接个数maxhcon                   系统当前的TCP6半连接个数onecon                    系统一分钟内新增的TCP6连接个数onehcon                   系统一分钟内新增的TCP6半连接个数tolcon                    系统最大TCP6资源个数maxper                    TCP6连接个数占系统最大TCP6资源个数的比率值oneper                    一分钟内新增的TCP6连接个数占系统最大TCP资源个数比率值





### 相关命令 


无 




## show tcp6 synflood-protect config 


show tcp6 synflood-protect config 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示TCP6 SYN Flood防护功能的配置信息。当需要查看TCP6 SYN Flood防护功能的配置信息时，使用该命令。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


除用户模式外的其他所有模式:15,用户模式:1 






### 命令格式 




show tcp6 synflood-protect config 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


该命令显示的TCP6 SYN Flood防护功能的配置信息包括：1、配置的TCP6 SYN Flood防护功能的开启和关闭状态（参见配置命令ipv6 tcp synflood-protect enable）；2、配置的TCP6 SYN Flood防护功能的防护模式及参数值（参见配置命令ipv6 tcp synflood-protect defence）；3、配置的TCP6 SYN Flood防护功能的TCP6连接比率值（参见配置命令ipv6 tcp synflood-protect max-connect）；4、配置的TCP6 SYN Flood防护功能的一分钟TCP6连接比率值（参见配置命令ipv6 tcp synflood-protect one-minute）。





### 范例 


通过show命令显示TCP6 SYN Flood防护功能的配置信息，则输入以下命令：ZXROSNG(config)#show tcp6 synflood-protect configsynflood-prevent is enableprevent means is quickening the TCP6 connection aging and deleting the old TCP6 half-connections  syn-waittime  is 10 (seconds)old-half-connect is 100max-connect high limit is 80%max-connect low limit is 60%one-minute high limit is 70%one-minute low limit is 50%输出信息中的参数信息解释如下：参数名称                  参数说明syn-waittime              配置的TCP6老化时间old-half-connect          配置的每次删除的TCP6半连接个数max-connect high limit    配置的TCP6连接高比率值，TCP6连接个数比率超过该值时，启动TCP6防护策略max-connect low limit     配置的TCP6连接低比率值one-minute high limit     配置的一分钟内新增TCP6连接高比率值，一分钟内新增的TCP6连接个数比率超过该值时，启动TCP6防护策略one-minute low limit      配置的一分钟内新增TCP6连接低比率值






### 相关命令 


无 




## show tcp6 synflood-protect statistics 


show tcp6 synflood-protect statistics 




### 命令功能 


该命令工作于所有模式，包括用户模式和除用户模式外的其他所有模式，用于显示TCP6 SYN Flood防护功能的统计信息。当需要查看TCP6 SYN Flood防护功能的防护状态或者统计信息时，使用该命令。 






### 命令模式 


 用户模式,除用户模式外的其他所有模式  






### 命令默认权限级别 


用户模式:1,除用户模式外的其他所有模式:15 






### 命令格式 




show tcp6 synflood-protect statistics 
 







### 命令参数解释 



					无
				 






### 缺省 


无 






### 使用说明 


该命令显示的TCP6 SYN Flood防护功能的统计信息包括：1、TCP6 SYN Flood防护功能所处的实例；2、TCP6 SYN Flood防护功能的防御状态；3、系统当前的TCP6连接个数；4、系统当前的TCP6半连接个数；5、系统一分钟内新增的TCP6连接个数；6、系统一分钟内新增的TCP6半连接个数；7、系统最大TCP6资源个数；8、TCP6连接个数占系统最大TCP6资源个数的比率值；9、一分钟内新增TCP6连接个数占系统最大TCP6资源个数比率值。当TCP6连接个数占系统最大TCP6资源个数的比率值，大于配置的TCP6 SYN Flood防护功能的TCP6连接比率值，或者一分钟内新增TCP6连接个数占系统最大TCP6资源个数比率值，大于配置的TCP6 SYN Flood防护功能的一分钟TCP6连接比率值时，系统将根据配置的TCP6 SYN Flood防护功能的防护模式及参数值进行防御。





### 范例 


通过show命令显示TCP6 SYN Flood防护功能的统计信息，则输入以下命令：ZXROSNG(config)#show tcp6 synflood-protect statistics             maxcon:current total connectionsmaxhcon:current total half-connectionsonecon:oneminute connections    onehcon:oneminute half-connections  maxper:maxcon/tolcon*100%       oneper:onecon/tolcon*100%           tolcon:max connections of the cpu allowed         instance  status    maxcon  maxhcon onecon  onehcon tolcon  maxper    oneper    1         safety    4       0       0       0       5120    0.08%     0.00%    2         safety    4       0       0       0       5120    0.08%     0.00%    3         safety    4       0       0       0       5120    0.08%     0.00%    4         safety    4       0       0       0       5120    0.08%     0.00%    5         safety    4       0       0       0       5120    0.08%     0.00% 输出信息中的参数信息解释如下：参数名称          参数说明instance          TCP6 SYN Flood防护功能所处的实例status            TCP6 SYN Flood防护功能的防御状态maxcon            系统当前的TCP6连接个数maxhcon           系统当前的TCP6半连接个数onecon            系统一分钟内新增的TCP6连接个数onehcon           系统一分钟内新增的TCP6半连接个数tolcon            系统最大TCP6资源个数maxper            TCP6连接个数占系统最大TCP资源个数的比率值，单位百分比oneper            一分钟内新增的TCP6连接个数占系统最大TCP6资源个数比率值，单位百分比






### 相关命令 


无 




