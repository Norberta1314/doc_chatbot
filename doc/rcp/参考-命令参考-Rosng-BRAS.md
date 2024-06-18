# VPDN配置命令 
## initiate-to-ipv6-addr 


initiate-to-ipv6-addr 




### 命令功能 


该命令工作于VPDN组配置模式，用于配置隧道的对端IPv6地址。 






### 命令模式 


 VPDN组模式  






### 命令默认权限级别 


15 






### 命令格式 



initiate-to-ipv6-addr 
  ＜ipv6-address 
＞ [priority 
 ＜priority 
＞]
no initiate-to-ipv6-addr 
  ＜ipv6-address 
＞
				






### 命令参数解释 




参数|描述
---|---
＜ipv6-address＞|隧道对端IPv6地址。取值范围：无。默认值：无。
＜priority＞|隧道对端地址优先级，值越小优先级越高。取值范围：0-65535。默认值：无。








### 缺省 


优先级默认值为50。 






### 使用说明 


该命令用于配置隧道对端IPv6地址以及该对端地址的优先级，最多可以配置8个对端地址。目前IPv4和IPv6对端IP地址不能同时配置，一个VPDN组下，只能配置IPv4地址或者IPv6对端地址。执行no命令清除配置的IPv6地址。该命令执行完，命令模式不改变。对端地址优先级的取值范围：0-65535。默认值为50。






### 范例 


配置隧道对端IPv6地址为100::1，优先级20：ZXROSNG(config-vpdn-group)#initiate-to-ipv6-addr 100::1 priority 20ZXROSNG(config-vpdn-group)#






### 相关命令 


show running-config vpdnshow vpdn group




## terminate-from local-ipv6 


terminate-from local-ipv6 




### 命令功能 


用于配置隧道LNS端IPv6终结地址。 






### 命令模式 


 VPDN组模式  






### 命令默认权限级别 


15 






### 命令格式 




terminate-from local-ipv6 
  ＜ipv6-address 
＞

no terminate-from local-ipv6 








### 命令参数解释 




参数|描述
---|---
＜ipv6-address＞|IPv6地址。 取值范围：无。 默认值：无。








### 缺省 


无 






### 使用说明 


no 命令清除配置。不同的VPDN GROUP 不可以配置相同的terminate-from local-ipv6 。每个VPDN组下只能配置一个LNS端隧道终结IPv6地址。该命令只用于VPDN组的服务类型为LNS的情况下。如果VPDN组的服务类型为LAC，则该配置无效。






### 范例 


在VPDN组配置模式下，配置隧道LNS端IPv6终结地址：ZXROSNG(config)#vpdn-group zteZXROSNG(config-vpdn-group)#terminate-from local-ipv6 100::1ZXROSNG(config-vpdn-group)#






### 相关命令 


show running-config vpdnshow vpdn group




