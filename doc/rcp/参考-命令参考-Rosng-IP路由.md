# ISIS配置命令 
description :

description 




命令功能 :

ISIS实例下配置实例描述信息。 






命令模式 :

 路由ISIS模式  






命令默认权限级别 :

15 






命令格式 :



description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|配置ISIS实例描述信息，长度1-63个字符








缺省 :

无 






使用说明 :

使用场景配置ISIS实例，在实例下配置实例描述信息。






范例 :

配置ISIS实例描述信息：ZXROSNG(config)#router isis 1ZXROSNG(config-isis-1)#description abc






相关命令 :

无 




## fast-reroute policy 


fast-reroute policy 




命令功能 :

配置ISIS FRR下发备份路由的策略。 






命令模式 :

 路由ISIS模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute policy 
 host-only 


no fast-reroute policy 








命令参数解释 :



参数|描述
---|---
host-only|配置仅有主机路由策略。








缺省 :

无 






使用说明 :

使用场景配置host-only路由策略后，只有32位主机路由才会下发备份路由。






范例 :

配置FRR路由host-only策略：ZXROSNG(config)#router isis 1ZXROSNG(config-isis-1)#fast-reroute policy host-only






相关命令 :

fast-reroute 




## fast-reroute policy 


fast-reroute policy 




命令功能 :

配置IPv6 ISIS FRR下发备份路由的策略。 






命令模式 :

 路由ISIS-IPv6地址簇模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute policy 
 host-only 


no fast-reroute policy 








命令参数解释 :



参数|描述
---|---
host-only|配置仅有主机路由策略








缺省 :

无 






使用说明 :

使用场景配置host-only路由策略后，只有128位主机路由才会下发备份路由。






范例 :

配置FRR路由host-only策略：ZXROSNG(config)#router isis 1ZXROSNG(config-isis-1)#address-family ipv6 ZXROSNG(config-isis-1-af)#fast-reroute policy host-only






相关命令 :

fast-reroute 




## fast-reroute srlg 


fast-reroute srlg 




命令功能 :

ISIS接口FRR SRLG共享链路风险组配置。 






命令模式 :

 路由ISIS接口模式  






命令默认权限级别 :

15 






命令格式 :


fast-reroute srlg 
  ＜srlg-identifier 
＞
no fast-reroute srlg 
  ＜srlg-identifier 
＞
				






命令参数解释 :



参数|描述
---|---
＜srlg-identifier＞|配置接口FRR SRLG标识，参数范围：0-4294967295








缺省 :

无 






使用说明 :

使用场景配置接口srlg，如果一组接口下有相同的srlg值，说明这组接口具有共同的共享风险链路分担，在计算TILFA的时候是优先计算非共享风险链路成为备份链路，目前只对TILFA计算生效。






范例 :

配置FRR SRLG的值：ZXROSNG(config)#router isis 1ZXROSNG(config-isis-1)#interface gei-0/1/0/1ZXROSNG(config-isis-1-if-gei-0/1/0/1)#fast-reroute srlg 100ZXROSNG(config-isis-1-if-gei-0/1/0/1)#no fast-reroute srlg 100






相关命令 :

fast-reroute ti-lfa sr-mplsfast-reroute ti-lfa srv6




## microloop-prevention policy 


microloop-prevention policy 




命令功能 :

ISIS实例模式下配置防微环路由策略。 






命令模式 :

 路由ISIS模式  






命令默认权限级别 :

15 






命令格式 :



microloop-prevention policy 
 host-only 


no microloop-prevention policy 








命令参数解释 :



参数|描述
---|---
host-only|配置仅有主机路由策略








缺省 :

无 






使用说明 :

使用场景配置host-only路由策略后，只有32位路由才会进行防微环延迟处理。






范例 :

配置microloop-prevention路由host-only策略：ZXROSNG(config)#router isis 1ZXROSNG(config-isis-1)#microloop-prevention policy host-only






相关命令 :

microloop-prevention 




## microloop-prevention policy 


microloop-prevention policy 




命令功能 :

ISIS IPv6地址簇模式下配置防微环路由策略。 






命令模式 :

 路由ISIS-IPv6地址簇模式  






命令默认权限级别 :

15 






命令格式 :



microloop-prevention policy 
 host-only 


no microloop-prevention policy 








命令参数解释 :



参数|描述
---|---
host-only|配置仅有主机路由策略








缺省 :

无 






使用说明 :

使用场景配置host-only路由策略后，只有128位路由才会进行防微环延迟处理。






范例 :

配置microloop-prevention路由host-only策略：ZXROSNG(config)#router isis 1ZXROSNG(config-isis-1)#address-family ipv6 ZXROSNG(config-isis-1-af)#microloop-prevention policy host-only






相关命令 :

microloop-prevention 




## show isis process 


show isis process 




命令功能 :

显示当前ISIS实例下的生效信息。 






命令模式 :

 用户模式  






命令默认权限级别 :

1 






命令格式 :



show isis process 
  [process-id 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|实例号，范围：0-65535








缺省 :

无 






使用说明 :

使用场景用于查询ISIS实例下的生效信息。注意事项1.如果不指定实例号，则显示所有ISIS实例下的生效信息。2.如果指定实例号，则显示指定ISIS实例下的生效信息。






范例 :

显示当前实例的生效信息：ZXROSNG(config)#router isis 1ZXROSNG(config-isis-1)#show isis processProcess ID: 1    Description                     : --    Create Time                     : 0h0m4s    Vrf Name                        : --    Area Address                    : --    System Id                       : --    Router Id                       : --    IPv6 Router Id                  : --    IS Type                         : level-1-2    Dynamic Hostname Status         : enable    Dynamic Hostname String         : R1    Metric Style                    : narrow    Waiting State                   : unset    Waiting State Timeout           : 0s    Set Overload Bit                : unset    Set IPv6 Overload Bit           : unset    Lsp Refresh Time                : 900s    Lsp LifeTime                    : 1200s    Lsp Originate Size              : 1492    Lsp Receive Size                : 1492    Lsp Generate Interval L1        : max 1s, hold 50ms, first 50ms    Lsp Generate Interval L2        : max 1s, hold 50ms, first 50ms    Lsp Authentication Type L1      : --    Lsp Authentication Type L2      : --    Spf Interval L1                 : max 1s, hold 50ms, first 50ms    Spf Interval L2                 : max 1s, hold 50ms, first 50ms    Multi-Topo IPv6 Spf Interval L1 : max 1s, hold 50ms, first 50ms    Multi-Topo IPv6 Spf Interval L2 : max 1s, hold 50ms, first 50ms    Multi-Topo IPv6                 : disableDescription：ISIS实例描述信息Create Time：ISIS实例创建的时间Vrf Name：Vrf名字Area Address：区域地址System Id：System IdRouter Id：router idIPv6 Router Id：IPv6 router IdIS Type：IS类型Dynamic Hostname Status：动态hostname状态Dynamic Hostname String：动态hostnameMetric Style：metric类型Waiting State：Waiting StateWaiting State Timeout：Waiting State TimeoutSet Overload Bit：OL位Set IPv6 Overload Bit：IPv6 OL位Lsp Refresh Time：Lsp Refresh TimeLsp LifeTime：Lsp LifeTimeLsp Originate Size：Lsp Originate SizeLsp Receive Size：Lsp Receive SizeLsp Generate Interval L1        : L1 LSP生成间隔Lsp Generate Interval L2        : L2 LSP生成间隔Lsp Authentication Type L1      : L1 LSP 认证类型Lsp Authentication Type L2      : L2 LSP 认证类型Spf Interval L1                 : Spf Interval L1Spf Interval L2                 : Spf Interval L2Multi-Topo IPv6 Spf Interval L1 :MT IPv6 Spf Interval L1Multi-Topo IPv6 Spf Interval L2 : MT IPv6 Spf Interval L2Multi-Topo IPv6                 : 是否使能MT IPv6






相关命令 :

无 




## show isis process 


show isis process 




命令功能 :

显示当前ISIS实例下的生效信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show isis process 
  [process-id 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|实例号，范围：0-65535








缺省 :

无 






使用说明 :

使用场景用于查询ISIS实例下的生效信息。注意事项1.如果不指定实例号，则显示所有ISIS实例下的生效信息。2.如果指定实例号，则显示指定ISIS实例下的生效信息。






范例 :

显示当前实例的生效信息：ZXROSNG(config)#router isis 1ZXROSNG(config-isis-1)#show isis processProcess ID: 1    Description                     : --    Create Time                     : 0h0m4s    Vrf Name                        : --    Area Address                    : --    System Id                       : --    Router Id                       : --    IPv6 Router Id                  : --    IS Type                         : level-1-2    Dynamic Hostname Status         : enable    Dynamic Hostname String         : R1    Metric Style                    : narrow    Waiting State                   : unset    Waiting State Timeout           : 0s    Set Overload Bit                : unset    Set IPv6 Overload Bit           : unset    Lsp Refresh Time                : 900s    Lsp LifeTime                    : 1200s    Lsp Originate Size              : 1492    Lsp Receive Size                : 1492    Lsp Generate Interval L1        : max 1s, hold 50ms, first 50ms    Lsp Generate Interval L2        : max 1s, hold 50ms, first 50ms    Lsp Authentication Type L1      : --    Lsp Authentication Type L2      : --    Spf Interval L1                 : max 1s, hold 50ms, first 50ms    Spf Interval L2                 : max 1s, hold 50ms, first 50ms    Multi-Topo IPv6 Spf Interval L1 : max 1s, hold 50ms, first 50ms    Multi-Topo IPv6 Spf Interval L2 : max 1s, hold 50ms, first 50ms    Multi-Topo IPv6                 : disableDescription：ISIS实例描述信息Create Time：ISIS实例创建的时间Vrf Name：Vrf名字Area Address：区域地址System Id：System IdRouter Id：router idIPv6 Router Id：IPv6 router IdIS Type：IS类型Dynamic Hostname Status：动态hostname状态Dynamic Hostname String：动态hostnameMetric Style：metric类型Waiting State：Waiting StateWaiting State Timeout：Waiting State TimeoutSet Overload Bit：OL位Set IPv6 Overload Bit：IPv6 OL位Lsp Refresh Time：Lsp Refresh TimeLsp LifeTime：Lsp LifeTimeLsp Originate Size：Lsp Originate SizeLsp Receive Size：Lsp Receive SizeLsp Generate Interval L1        : L1 LSP生成间隔Lsp Generate Interval L2        : L2 LSP生成间隔Lsp Authentication Type L1      : L1 LSP 认证类型Lsp Authentication Type L2      : L2 LSP 认证类型Spf Interval L1                 : Spf Interval L1Spf Interval L2                 : Spf Interval L2Multi-Topo IPv6 Spf Interval L1 :MT IPv6 Spf Interval L1Multi-Topo IPv6 Spf Interval L2 : MT IPv6 Spf Interval L2Multi-Topo IPv6                 : 是否使能MT IPv6






相关命令 :

无 




# OSPF配置命令 
## advertise interface 


advertise interface 




命令功能 :

配置ospf的通告loopback接口命令，让该loopback接口对应的网段在所有区域中产生相应32位的stub-link。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


advertise interface 
  ＜interface-name 
＞
no advertise interface 
  ＜interface-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|advertise命令需要通告的接口，只能通告loopback口，使得该loopback口在所有区域中产生一个32位的stub-link。advertise命令需要通告的接口，只能通告loopback口，使得该loopback口在所有区域中产生一个32位的stub-link。








缺省 :

缺省条件下默认没有配置advertise命令。 






使用说明 :

1. advertise interface {loopback<number>}每个ospf实例下都可以配置多个advertise命令，做多可以配置64个。命令配置会检查该ospf的每个区域，如果该区域中已经有了network通告的该loopback接口，则不在该区域产生32位的stub-link，否则就产生32位的stub-link。2. no advertise interface {loopback<number >}no命令需要带配置的时候的loopback口。





范例 :

Ospf实例模式下advertise命令的范例:1. 首先配置一个通告loopback1接口的advertise命令，再配置一个通告loopback2接口的advertise命令，然后逐个删除。ZXROSNG(config)# router ospf 1ZXROSNG(config-ospf-1)# advertise interface loopback1ZXROSNG(config-ospf-1)# advertise interface loopback2ZXROSNG(config-ospf-1)# no advertise interface loopback1ZXROSNG(config-ospf-1)# no advise interface loopback2





相关命令 :

无 




## area 


area 




命令功能 :

选择OSPF的一个区域进行配置 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


area 
  {＜area-id 
＞|＜area-id 
＞}
no area 
  {＜area-id 
＞|＜area-id 
＞}
				






命令参数解释 :



参数|描述
---|---
＜area-id＞|区域标识符，可以指定为一个十进制点分形式的IP地址或十进制数值，数值范围：0–4294967295
＜area-id＞|区域标识符，可以指定为一个十进制点分形式的IP地址或十进制数值，数值范围：0–4294967295








缺省 :

无 






使用说明 :

无 






范例 :

无 






相关命令 :

无 




## authentication 


authentication 




命令功能 :

在OSPF区域上使认证起作用。使用no命令使认证无效 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



authentication 
  [{message-digest 
|keychain 
 ＜Keychain name 
＞}]

no authentication 








命令参数解释 :



参数|描述
---|---
message-digest|在该区域使用类型2认证，即报文摘要认证
＜Keychain name＞|指定一个keychain用于报文加密，长度为1~31个字符








缺省 :

无认证 






使用说明 :

如果不带参数，则为类型1认证，即简单口令认证；如果带参数，则为类型2认证，即报文摘要认证。如果该区域不存在则自动创建。






范例 :

RP1(config)#router ospf 1RP1(config-ospf-1)#area 2RP1(config-ospf-1-area-2)#authentication keychain keychain_ospf





相关命令 :

无 




## authentication 


authentication 




命令功能 :

配置接口认证方式。使用no命令删除所配置的接口认证方式。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



authentication 
  {[null 
]|[message-digest 
]}

no authentication 








命令参数解释 :



参数|描述
---|---
null|在该接口使用类型0认证，即无认证
message-digest|在该接口使用类型2认证，即报文摘要认证








缺省 :

不指定接口的认证方式，如果接口所在的区域起了认证，接口继承区域的认证方式。 






使用说明 :

1. 不带参数时，本命令配置接口的认证方式为简单口令认证方式（类型1认证）。2. 如果接口所在的区域起了认证，并且接口也起了认证，以接口的配置为准。






范例 :

ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#authentication message-digest 






相关命令 :

无 




## authentication-key 


authentication-key 




命令功能 :

为简单口令认证类型的接口设置口令。使用no命令删除配置的OSPF口令。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



authentication-key 
  {encrypted 
 ＜authen-key 
＞|clear 
 ＜authen-key 
＞|＜authen-key 
＞}

no authentication-key 








命令参数解释 :



参数|描述
---|---
＜authen-key＞|经加密后的认证口令，长度为24个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜authen-key＞|经加密后的认证口令，长度为24个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜authen-key＞|经加密后的认证口令，长度为24个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\








缺省 :

不指定口令。 






使用说明 :

无 






范例 :

ZXROSNG(config-ospfv2-if-gei-0/1/0/1)#authentication-key zxr10 






相关命令 :

authentication [null|message-digest] 




## authentication-key 


authentication-key 




命令功能 :

为简单口令认证类型的接口设置口令。使用no命令删除配置的OSPF口令。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



authentication-key 
  {encrypted 
 ＜authen-key 
＞|clear 
 ＜authen-key 
＞|＜authen-key 
＞}

no authentication-key 








命令参数解释 :



参数|描述
---|---
＜authen-key＞|认证口令，长度1–8个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜authen-key＞|认证口令，长度1–8个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜authen-key＞|认证口令，长度1–8个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\








缺省 :

不指定口令。 






使用说明 :

无 






范例 :

[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config-ospfv2-if-gei-0/1/0/1)#authentication-key zxr10{{%6800}}ZXROSNG(config-ospfv2-if-gei-1/1)#authentication-key zxr10{{%6800}}[89\9900]1. 为简单口令认证类型的接口设置口令为zxr10：ZXROSNG(config-ospfv2-if)#authentication-key zxr10





相关命令 :

authentication [null|message-digest] 




## authentication-key 


authentication-key 




命令功能 :

配置多区域接口简单认证的认证密钥。 






命令模式 :

 IPv4-OSPF-MULTI-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



authentication-key 
  {encrypted 
 ＜encrypted-key 
＞|clear 
 ＜clear-key 
＞|＜clear-key 
＞}

no authentication-key 








命令参数解释 :



参数|描述
---|---
＜encrypted-key＞|经加密后的认证口令，长度为24个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜clear-key＞|指定明文认证的口令，长度1–8个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜clear-key＞|指定明文认证的口令，长度1–8个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\








缺省 :

无 






使用说明 :

在使用多区域接口建链时，当需要配置认证类型为普通认证类型时，则应当通过此命令配置密钥，如果authentication-key不匹配则不能建立多区域接口的邻居。 






范例 :

配置IPv4 OSPF实例1的区域100下添加fei-0/1/0/1多区域接口，配置多区域接口fei-0/1/0/1的简单认证明文为zxr10。R1(config)#router ospf 1R1(config-ospf-1)#area 100R1(config-ospf-1-area-100)#multi-area-interface fei-0/1/0/1R1(config-ospf-1-area-100-mif-fei-0/1/0/1)# authentication-key zxr10






相关命令 :

无 




## auto-cost 


auto-cost 




命令功能 :

修改该OSPF进程的参考带宽（Reference bandwidth）。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



auto-cost 
 reference-bandwidth 
 ＜ref-bw 
＞

no auto-cost 








命令参数解释 :



参数|描述
---|---
＜ref-bw＞|参考带宽，缺省为100Mbps，范围：1–4000000，单位：Mbps








缺省 :

无 






使用说明 :

1. 本命令配置后即时生效。2. 如果OSPF进程的接口未显式用协议接口配置模式下cost命令配置，该接口的OSPF接口的cost为用参考带宽除以接口的带宽；否则，该接口的OSPF接口的cost使用该接口cost命令配置的值。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)# auto-cost reference-bandwidth 10000





相关命令 :

无 




## bfd 


bfd 




命令功能 :

使能OSPFv2实例的bfd功能。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


bfd 
  [interval 
 ＜interval 
＞ min-rx 
 ＜min-rx 
＞ multiplier 
 ＜multiplier 
＞]
no bfd 
  [time-negotiation 
]
				






命令参数解释 :



参数|描述
---|---
＜interval＞|BFD发送检测报文的间隔，范围：$#35389448#$~$#35389449#$
＜min-rx＞|BFD接收检测报文的间隔，范围：$# 35389450#$~$# 35389451#$
＜multiplier＞|本地检测时间倍数，范围3-50






No参数|描述
---|---
time-negotiation|清除协商时间








缺省 :

无 






使用说明 :

无 






范例 :

1. 使区域1所有接口都支持BFD功能：ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#area 1ZXR10 (config-ospfv2-area-1)#bfd2. 配置区域1支持BFD功能的参数：interval为11，min-rx为12，multiplier为13ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#area 1ZXR10 (config-ospfv2-area-1)#bfd interval 11 min-rx 12 multiplier 133. no掉bfd的时间协商参数ZXR10 (config-ospfv2-area-1)#no bfd time-negotiation






相关命令 :

无 




## bfd 


bfd 




命令功能 :

配置接口的双向转发检测（bfd, bidirection forwarding detect）属性。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :


bfd 
  {[disable 
]|[interval 
 ＜interval 
＞ min-rx 
 ＜min-rx 
＞ multiplier 
 ＜multiplier 
＞]}
no bfd 
  [time-negotiation 
]
				






命令参数解释 :



参数|描述
---|---
disable|双向转发检测无效
＜interval＞|BFD发送检测报文的间隔，范围：$#35389448#$~$#35389449#$
＜min-rx＞|BFD接收检测报文的间隔，范围：$# 35389450#$~$# 35389451#$
＜multiplier＞|本地检测时间倍数，范围3-50






No参数|描述
---|---
time-negotiation|清除时间协商参数








缺省 :

无 






使用说明 :

IPv4-OSPF接口模式和IPv4-OSPF_AREA接口模式都可以配置接口的双向转发检测（bfd）属性，IPv4-OSPF_AREA接口模式下的配置优先生效，如果IPv4-OSPF_AREA接口模式下没有配置，并且IPv4-OSPF接口模式下有配置，就以IPv4-OSPF接口模式下的配置生效。 






范例 :

1. 设置接口的双向转发检测，并配置bfd参数，interval为11，min-rx为12，multiplier为13，然后no掉bfd的时间协商参数：ZXROSNG(config-ospfv2-if)#bfd interval 11 min-rx 12 multiplier 13ZXROSNG(config-ospfv2-if)#no bfd time-negotiation[M6000\M6000-S\ZSR]ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#bfd interval 11 min-rx 12 multiplier 13ZXROSNG(config-ospf-1-if-gei-0/1/0/1)# no bfd time-negotiation






相关命令 :

无 




## bfd 


bfd 




命令功能 :

配置所有接口的双向转发检测（bfd, bidirection forwarding detect）功能。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


bfd 
  [interval 
 ＜interval 
＞ min-rx 
 ＜min-rx 
＞ multiplier 
 ＜multiplier 
＞]
no bfd 
  [time-negotiation 
]
				






命令参数解释 :



参数|描述
---|---
＜interval＞|BFD发送检测报文的间隔，范围：$#35389448#$~$#35389449#$
＜min-rx＞|BFD接收检测报文的间隔，范围：$# 35389450#$~$# 35389451#$
＜multiplier＞|本地检测时间倍数，范围3-50






No参数|描述
---|---
time-negotiation|清除时间协商参数








缺省 :

无 






使用说明 :

如果IPv4-OSPF_AREA接口模式配置了，就以IPv4-OSPF_AREA接口模式的配置生效，否则就继承IPv4-OSPF接口模式的配置，如果IPv4-OSPF接口模式也没有配置，就去继承IPv4-OSPF区域模式的配置，否则才去继承IPv4-OSPF模式的配置。 






范例 :

1. 使区域1所有接口都支持BFD功能：ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#area 1 ZXR10 (config-ospfv2-area-1)#bfd2. 配置区域1支持BFD功能的参数：interval为11，min-rx为12，multiplier为13ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#area 1 ZXR10 (config-ospfv2-area-1)#bfd interval 11 min-rx 12 multiplier 133. no掉bfd的时间协商参数ZXR10 (config-ospfv2-area-1)#no bfd time-negotiation






相关命令 :

无 




## bfd 


bfd 




命令功能 :

配置所有接口的双向转发检测（bfd, bidirection forwarding detect）功能。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :


bfd 
  {[disable 
]|[interval 
 ＜interval 
＞ min-rx 
 ＜min-rx 
＞ multiplier 
 ＜multiplier 
＞]}
no bfd 
  [time-negotiation 
]
				






命令参数解释 :



参数|描述
---|---
disable|双向转发检测无效
＜interval＞|BFD发送检测报文的间隔，范围：$#35389448#$~$#35389449#$
＜min-rx＞|BFD接收检测报文的间隔，范围：$# 35389450#$~$# 35389451#$
＜multiplier＞|本地检测时间倍数，范围3-50






No参数|描述
---|---
time-negotiation|清除时间协商参数








缺省 :

无 






使用说明 :

如果IPv4-OSPF_AREA接口模式配置了，就以IPv4-OSPF_AREA接口模式的配置生效，否则就继承IPv4-OSPF接口模式的配置，如果IPv4-OSPF接口模式也没有配置，就去继承IPv4-OSPF区域模式的配置，否则才去继承IPv4-OSPF模式的配置。 






范例 :

1. 设置接口的双向转发检测，并配置bfd参数，interval为11，min-rx为12，multiplier为13：ZXROSNG(config-ospfv2-if)#bfd interval 11 min-rx 12 multiplier 13[M6000\M6000-S\ZSR]ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#bfd interval 11 min-rx 12 multiplier 13ZXROSNG(config-ospf-1-if-gei-0/1/0/1)# no bfd time-negotiation






相关命令 :

无 




## bgp link-state 


bgp link-state 




命令功能 :

使用BGP来分发链路状态信息。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


bgp link-state 
  [instance-id 
 ＜instance-id 
＞]
no bgp link-state 
  [instance-id 
]
				






命令参数解释 :



参数|描述
---|---
＜instance-id＞|用于标识BGP-LS信息所属的routing universe,范围：0-65535，默认值：0






No参数|描述
---|---
instance-id|清除BGP-LS信息所属的routing universe








缺省 :

如果没有配置该命令，缺省是不使能该功能的。如果配置了bgp link-state，instance-id的缺省值是0





使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#bgp link-state instance-id 1ZXR10 (config-ospf-1)#





相关命令 :

无 




## capability opaque 


capability opaque 




命令功能 :

使路由支持不透明路由状态通告（Opaque LSA），用no命令表示不支持。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



capability opaque 
  [disable 
]

no capability opaque 








命令参数解释 :



参数|描述
---|---
disable|使路由不支持不透明路由状态通告（Opaque LSA）








缺省 :

支持不透明路由状态通告。 






使用说明 :

1. 在链路状态数据库交换过程中，不透明链路状态通告被包含在数据库摘要列表中，发送到同样支持不透明链路状态通告的紧邻路由器中。2. 当一个路由器洪泛不透明链路状态通告到邻接路由器时，该路由器首先检查邻接路由器是否支持不透明链路状态通告这一功能。不透明链路状态通告仅仅发送到具有该功能的邻接路由器中；更确切一些说是被添加到邻接路由器的链路状态重发列表中。当链路状态更新报表为多播时，不支持该功能的邻接路由器会被动接受该通告，然后简单丢弃。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#no capability opaque





相关命令 :

无 




## capability vrf-lite 


capability vrf-lite 




命令功能 :

用来使路由忽略OSPF VRF环路抑制，使用no命令表示不忽略。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



capability vrf-lite 
 

no capability vrf-lite 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#no capability vrf-lite





相关命令 :

无 




## clear ip ospf process 


clear ip ospf process 




命令功能 :

重启OSPF进程。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear ip ospf process 
  ＜process-id 
＞







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在命令show running-config中显示。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#endZXROSNG#clear ip ospf process 1Reset ospf process? [yes/no]:yZXROSNG#






相关命令 :

无 




## clear ip ospf redistribution 


clear ip ospf redistribution 




命令功能 :

重启OSPF进程的重分配。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear ip ospf redistribution 
  ＜process-id 
＞







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在命令show running-config中显示。 






范例 :

ZXROSNG#clear ip ospf redistribution 1 






相关命令 :

无 




## compatible rfc1583 


compatible rfc1583 




命令功能 :

控制多条到相同ASBR的选优规则。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



compatible rfc1583 
  [disable 
]

no compatible rfc1583 








命令参数解释 :



参数|描述
---|---
disable|不使用rfc1583规定的规则来进行ASBR择优








缺省 :

使用RFC 1583兼容规则。 






使用说明 :

为了降低路由回环的可能，所有OSPF域中的路由器本项配置的值应该相同。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#compatible rfc1583





相关命令 :

无 




## cost link-damping 


cost link-damping 




命令功能 :

接口下第一个邻居FULL后开始调整接口的花费来抑制该链路。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



cost link-damping 
  {increase 
 ＜increase-value 
＞|maximum 
} damping-time 
 ＜damping-time 
＞

no cost link-damping 








命令参数解释 :



参数|描述
---|---
increase|当damping状态生效的情况下调整该接口的花费，在原来花费的基础上增加一个花费值。
＜increase-value＞|花费调整值，范围是100-10000。
maximum|当damping状态生效的情况下直接调整该接口的花费到最大值65535。
＜damping-time＞|damping状态持续的时间。范围是1-3600000，单位是毫秒








缺省 :

如果没有配置该命令，缺省是不使能该功能的。 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#area 1ZXR10 (config-ospf-1-area-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-area-1-if- gei-0/1/0/1)# cost link-damping increase 3001 damping-time 200000





相关命令 :

无 




## cost link-sd 


cost link-sd 




命令功能 :

接口处于SD状态的时候，指定接口的相对花费或者最大花费。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



cost link-sd 
  {increase 
 ＜number 
＞|maximum 
}

no cost link-sd 








命令参数解释 :



参数|描述
---|---
＜number＞|增加相应的花费值，范围：100-10000
maximum|指定接口的花费为最大花费值65535








缺省 :

配置increase且cost是3000 






使用说明 :

1.    当接口处于SD状态时，可以通过此命令，设置建链接口的cost。2.    两条命令是二选一，彼此覆盖的关系。3.    配置increase的时候，接口cost=原cost + increase cost；当配置maximum的时候，接口cost为最大值655354.    以上配置在任何接口下都可以配，但只有同时满足如下两个条件才会真正生效：    接口处于SD状态    建立OSPF邻居的实接口





范例 :

指定接口gei-0/1/0/1的cost link-sd是999ZXROSNG(config-ospf-1-area-1-if-gei-0/1/0/1)#cost link-sd increase 999 





相关命令 :

无 




## cost 


cost 




命令功能 :

显式说明接口费用。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



cost 
  ＜cost 
＞

no cost 








命令参数解释 :



参数|描述
---|---
＜cost＞|接口费用，缺省为1，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#cost 10 






相关命令 :

无 




## cost 


cost 




命令功能 :

显式说明接口费用。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



cost 
  ＜cost 
＞

no cost 








命令参数解释 :



参数|描述
---|---
＜cost＞|接口费用，缺省为1，范围：1–65535








缺省 :

[M6000\M6000-S\ZSR]无[89\9900]使用［reference-bandwidth / 接口带宽］的值，计算cost不足１的情况下赋cost为１。





使用说明 :

[M6000\M6000-S\ZSR]无[89\9900]如果在接口已经配置了cost，这样再使用auto-costreference-bandwidth命令将不起作用，要使得auto-costreference-bandwidth命令起作用，必须先将先前cost命令配置的cost值删除掉。





范例 :

[M6000\M6000-S\ZSR]ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#cost 10[89\9900]1. 显式配置接口费用为10：ZXROSNG(config-ospfv2-if)#cost 10





相关命令 :

无 




## cost 


cost 




命令功能 :

配置多区域接口的花费。 






命令模式 :

 IPv4-OSPF-MULTI-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



cost 
  ＜cost 
＞

no cost 








命令参数解释 :



参数|描述
---|---
＜cost＞|接口花费，范围：1–65535








缺省 :

无 






使用说明 :

使用场景在使用多区域接口建链时，可以通过cost命令配置多区域接口建链的链路metric，从而影响路由择优。






范例 :

配置IPv4 OSPF实例1的区域100下添加fei-0/1/0/1多区域接口，配置多区域接口fei-0/1/0/1的cost值为123。R1(config)#router ospf 1R1(config-ospf-1)#area 100R1(config-ospf-1-area-100)#multi-area-interface fei-0/1/0/1R1(config-ospf-1-area-100-mif-fei-0/1/0/1)# cost 123






相关命令 :

无 




## dead-interval 


dead-interval 




命令功能 :

指定接口上邻居的死亡时间。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



dead-interval 
  ＜seconds 
＞

no dead-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口上邻居的死亡时间，缺省为4倍的缺省hello-interval时长。当网络类型为广播网或P2P时，缺省为40秒；当网络类型为P2MP或NBMA网络时，缺省为120秒，范围：1–65535，单位：秒








缺省 :

缺省为4倍的缺省hello-interval时长. 






使用说明 :

无 






范例 :

ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#dead-interval 80 






相关命令 :

无 




## dead-interval 


dead-interval 




命令功能 :

配置接口发送HELLO报文的时间间隔。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



dead-interval 
  ＜seconds 
＞

no dead-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口发送HELLO报文的时间间隔，缺省为1/4的缺省dead-interval时长。当网络类型为广播网或P2P时，缺省为10秒；当网络类型为P2MP或NBMA网络时，缺省为30秒，范围：1–65535，单位：秒








缺省 :

缺省为1/4的缺省dead-interval时长. 






使用说明 :

无 






范例 :

[89\9900]1. 指定接口上发送hello报文的时间间隔为40秒：ZXROSNG(config-ospfv2-if)#hello-interval 40[M6000\M6000-S\ZSR]ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#hello-interval 40





相关命令 :

无 




## dead-interval 


dead-interval 




命令功能 :

配置多区域接口的dead周期。 






命令模式 :

 IPv4-OSPF-MULTI-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



dead-interval 
  ＜seconds 
＞

no dead-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口dead-interval的值，单位为秒，不配置的情况下为40s。范围1~65535








缺省 :

缺省为4倍的hello-interval时长。 






使用说明 :

使用场景在使用多区域接口建链时，应当配置两端dead-interval相同，才能建链成功。如果超过dead-interval时长未收到Hello报文，则多区域接口的邻居断链。






范例 :

配置IPv4 OSPF实例1的区域100下添加fei-0/1/0/1多区域接口，配置多区域接口fei-0/1/0/1停止接收Hello包后的断链时长为120秒。R1(config)#router ospf 1R1(config-ospf-1)#area 100R1(config-ospf-1-area-100)#multi-area-interface fei-0/1/0/1R1(config-ospf-1-area-100-mif-fei-0/1/0/1)# dead-interval 120






相关命令 :

无 




## debug ip ospf adj 


debug ip ospf adj 




命令功能 :

打开回送OSPF邻接事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf adj 
  ＜process-id 
＞
no debug ip ospf adj 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf adj 1 






相关命令 :

无 




## debug ip ospf all 


debug ip ospf all 




命令功能 :

打开所有OSPF调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf all 
  [＜process-id 
＞]
no debug ip ospf all 
  [＜process-id 
＞]
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf all 1 






相关命令 :

无 




## debug ip ospf cspf 


debug ip ospf cspf 




命令功能 :

调试OSPF基于约束的最短路径计算。使用no命令关闭调试。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf cspf 
  ＜process-id 
＞
no debug ip ospf cspf 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf cspf 1OSPF cspf events debugging is on






相关命令 :

无 




## debug ip ospf database-timer 


debug ip ospf database-timer 




命令功能 :

打开回送OSPF链路状态数据库定时器事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf database-timer 
  ＜process-id 
＞
no debug ip ospf database-timer 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf database-timer 1 






相关命令 :

无 




## debug ip ospf events 


debug ip ospf events 




命令功能 :

打开回送OSPF重要事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf events 
  ＜process-id 
＞
no debug ip ospf events 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf events 1 






相关命令 :

无 




## debug ip ospf fast-reroute external 


debug ip ospf fast-reroute external 




命令功能 :

打开回送OSPF自治系统外部快速重路由调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf fast-reroute external 
  ＜process-id 
＞
no debug ip ospf fast-reroute external 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF的实例号，取值范围是1-65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf fast-reroute external 1OSPF fast-reroute external events debugging is on






相关命令 :

无 




## debug ip ospf fast-reroute inter 


debug ip ospf fast-reroute inter 




命令功能 :

打开回送OSPF区域间快速重路由调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf fast-reroute inter 
  ＜process-id 
＞
no debug ip ospf fast-reroute inter 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF的实例号，取值范围是1-65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf fast-reroute inter 1OSPF fast-reroute inter events debugging is on






相关命令 :

无 




## debug ip ospf fast-reroute intra 


debug ip ospf fast-reroute intra 




命令功能 :

打开回送OSPF区域内部快速重路由调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf fast-reroute intra 
  ＜process-id 
＞
no debug ip ospf fast-reroute intra 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF的实例号，取值范围是1-65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf fast-reroute intra 1OSPF fast-reroute intra events debugging is on






相关命令 :

无 




## debug ip ospf fast-reroute nbrspf 


debug ip ospf fast-reroute nbrspf 




命令功能 :

打开回送OSPF邻居的快速重路由调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf fast-reroute nbrspf 
  ＜process-id 
＞
no debug ip ospf fast-reroute nbrspf 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF的实例号，取值范围是1-65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf fast-reroute nbrspf 1OSPF fast-reroute nbr spf events debugging is on






相关命令 :

无 




## debug ip ospf fast-reroute 


debug ip ospf fast-reroute 




命令功能 :

打开回送OSPF快速重路由调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf fast-reroute 
  ＜process-id 
＞
no debug ip ospf fast-reroute 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF的实例号，取值范围是1-65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG# debug ip ospf fast-reroute   1OSPF fast-reroute external events debugging is onOSPF fast-reroute inter events debugging is onOSPF fast-reroute intra events debugging is onOSPF fast-reroute nbr spf events debugging is on





相关命令 :

无 




## debug ip ospf flood 


debug ip ospf flood 




命令功能 :

打开回送OSPF洪泛事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf flood 
  ＜process-id 
＞
no debug ip ospf flood 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf flood 1 






相关命令 :

无 




## debug ip ospf lsa-generation 


debug ip ospf lsa-generation 




命令功能 :

打开回送OSPF生成链路状态通告事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf lsa-generation 
  ＜process-id 
＞
no debug ip ospf lsa-generation 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf lsa-generation 1OSPF summary lsa generation debugging is on





相关命令 :

无 




## debug ip ospf nsf 


debug ip ospf nsf 




命令功能 :

打开OSPF支持不间断转发事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf nsf 
  ＜process-id 
＞
no debug ip ospf nsf 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf nsf 1OSPF non-stop forwarding event debugging is on





相关命令 :

无 




## debug ip ospf packet 


debug ip ospf packet 




命令功能 :

打开回送OSPF收发包事件调试信息的开关，监听所有OSPF包的接收和发送。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf packet 
  ＜process-id 
＞
no debug ip ospf packet 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf packet 1OSPF packet debugging is on





相关命令 :

无 




## debug ip ospf retransmission 


debug ip ospf retransmission 




命令功能 :

打开回送OSPF重传队列事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf retransmission 
  ＜process-id 
＞
no debug ip ospf retransmission 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf retransmission 1OSPF retransmission events debugging is on





相关命令 :

无 




## debug ip ospf spf external 


debug ip ospf spf external 




命令功能 :

打开回送OSPF外部路由计算事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf spf external 
  ＜process-id 
＞
no debug ip ospf spf external 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf  spf external 1OSPF spf external events debugging is on






相关命令 :

无 




## debug ip ospf spf inter 


debug ip ospf spf inter 




命令功能 :

打开回送OSPF域间路由计算事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf spf inter 
  ＜process-id 
＞
no debug ip ospf spf inter 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf  spf inter 1OSPF spf inter events debugging is on






相关命令 :

无 




## debug ip ospf spf intra 


debug ip ospf spf intra 




命令功能 :

打开回送OSPF区域内路由计算事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf spf intra 
  ＜process-id 
＞
no debug ip ospf spf intra 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf spf intra 1OSPF spf intra events debugging is onZXROSNG#






相关命令 :

无 




## debug ip ospf spf 


debug ip ospf spf 




命令功能 :

打开回送OSPF路由计算事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf spf 
  ＜process-id 
＞
no debug ip ospf spf 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf spf 1OSPF spf external events debugging is onOSPF spf inter events debugging is onOSPF spf intra events debugging is on





相关命令 :

无 




## debug ip ospf te-topology-change 


debug ip ospf te-topology-change 




命令功能 :

打开回送OSPFte拓扑变化事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ip ospf te-topology-change 
  ＜process-id 
＞
no debug ip ospf te-topology-change 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug ip ospf te-topology-change 1OSPF TE-topology change event debugging is on






相关命令 :

无 




## debug 


debug 




命令功能 :

打开某个OSPF进程的调试信息。使用no命令关闭调试信息。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



debug 
  [disable 
]

no debug 








命令参数解释 :



参数|描述
---|---
disable|关闭某个OSPF进程的调试信息








缺省 :

无 






使用说明 :

无 






范例 :

无 






相关命令 :

无 




## default-metric 


default-metric 




命令功能 :

设置重分配后的缺省metric。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



default-metric 
  ＜metric-value 
＞

no default-metric 








命令参数解释 :



参数|描述
---|---
＜metric-value＞|设置系统的外部路由缺省费用值，范围：1–16777214








缺省 :

缺省metric在重分配BGP路由时为1，其他路由时为20。 






使用说明 :

1. 该命令的设置值只有在用户没有设置外部路由的费用值时生效。2. 重分配BGP的时候，不受该命令的影响，只可以通过命令redistribute来修改BGP的重分配metric值。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#default-metric 10





相关命令 :

无 




## disable area 


disable area 




命令功能 :

使存在的指定区域无效。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



disable area 
  {＜area-id 
＞|＜area-id 
＞}







命令参数解释 :



参数|描述
---|---
＜area-id＞|区域标识符，可以指定为一个十进制点分形式的IP地址或十进制数值，数值范围：0–4294967295
＜area-id＞|区域标识符，可以指定为一个十进制点分形式的IP地址或十进制数值，数值范围：0–4294967295








缺省 :

无 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在命令show running-config中显示。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#disable area 1





相关命令 :

无 




## disable interface 


disable interface 




命令功能 :

使指定范围内的接口失效，对已经失效的接口该命令无效。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



disable interface 
  ＜ip-address 
＞ ＜wildcard-mask 
＞







命令参数解释 :



参数|描述
---|---
＜ip-address＞|IP所在地址的区域，与上反掩码后值为零，十进制点分形式
＜wildcard-mask＞|反掩码，十进制点分形式








缺省 :

无 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在命令show running-config中显示。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10(onfig-ospf-1)#disable interface 10.1.0.0 0.0.255.255





相关命令 :

无 




## disable ip ospf 


disable ip ospf 




命令功能 :

如果该OSPF协议进程处于有效状态，则使该OSPF协议无效，否则命令不起作用。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



disable ip ospf 
  ＜process-id 
＞







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

如果已配置OSPF协议，缺省状态为有效状态。 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在命令show running-config中显示。 






范例 :

ZXROSNG(config)#disable ip ospf 1Proceed with disable ip ospf? [yes/no]:





相关命令 :

无 




## distance ospf 


distance ospf 




命令功能 :

定义基于路由类型的OSPF路由管辖距离。使用相应的no命令使内部路由距离，或第一类外部路由距离或第二类外部路由距离恢复到缺省值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


distance ospf 
  {[internal 
 ＜distance 
＞],[ext1 
 ＜distance 
＞],[ext2 
 ＜distance 
＞]}
no distance ospf 
  [{[internal 
],[ext1 
],[ext2 
]}]
				






命令参数解释 :



参数|描述
---|---
＜distance＞|内部路由的距离值，缺省为110，范围：1–255
＜distance＞|内部路由的距离值，缺省为110，范围：1–255
＜distance＞|内部路由的距离值，缺省为110，范围：1–255






No参数|描述
---|---
internal|清除内部路由管理距离
ext1|清除外部1型路由的管理距离
ext2|清除外部2型的管理距离








缺省 :

缺省距离值为110 






使用说明 :

路由的优先级为255时，该路由不生效。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#distance ospf internal 100





相关命令 :

无 




## distribute-list 


distribute-list 




命令功能 :

Distribute-list的in命令，用于过滤owner为OSPF的路由。Distribute-list的out命令，在5、7型LSA生成以后，用于控制外部路由导入OSPF域，是redistribute命令的补充。





命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


distribute-list 
  {access-list 
 ＜access-list-name 
＞ {in 
|out 
}|gateway 
 ＜gateway 
＞ in 
|prefix 
 ＜prefix-list 
＞ {out 
|[gateway 
 ＜prefix-gateway 
＞] in 
}|route-map 
 ＜route-map 
＞ in 
 [local-mt 
]}
no distribute-list 
  {in 
|out 
}
				






命令参数解释 :



参数|描述
---|---
＜access-list-name＞|名字型的ACL，第一个字符可以是数字，可以使用当前不存在的ACL
in|In表示指定的模板用于路由的过滤
out|0ut表示指定的模板用于对重分配进行补充
＜gateway＞|通过gateway来进行过滤
in|In表示指定的模板用于路由的过滤
＜prefix-list＞|通过prefix-list来进行过滤
out|0ut表示指定的模板用于对重分配进行补充
＜prefix-gateway＞|通过prefix-gateway来进行过滤
in|In表示指定的模板用于路由的过滤
＜route-map＞|通过route-map来进行过滤
in|In表示指定的模板用于路由的过滤
local-mt|使能自动路由short-cut方式的时候，为组播路由协议生成下一跳是物理口的路由








缺省 :

不配置该命令，即不进行路由的过滤和externalLSA的导入控制。 






使用说明 :

1. Gate-way，route-map只用于in命令。2. ACL：策略模板决策为permit时，返回permit，否则，返回deny；策略模板不存在时，返回deny。3.gate-way，route-map：策略模板为permit时，返回permit，否则，返回deny；策略模板不存在时，返回permit。4. 由于模板的缺省都是deny all，如果要deny某些路由，需要加配permit all，将其他的路由允许。5. Route-map用于in命令的时候，没有set项，匹配项只对路由前缀，metric，下一跳和5、7型LSA的tag生效，其余无效。6. 使用in命令过滤路由的时候要小心，鉴于OSPF路由之间的关联性，有如下几个建议：  最好不要过滤2型LSA对应的路由，否则会导致网络拓扑不全。  允许某5型路由进入的时候，注意确保forwarding address路由的存在，如果不存在，也要在模板设置中将对应路由允许。






范例 :

ZXROSNG(config)#ipv4-access-list zxr10ZXR10 (config-ipv4-acl)#rule 1 deny 12.1.1.0ZXR10 (config-ipv4-acl)#rule 2 permit anyZXROSNG(config#router ospf 1ZXR10 (config-ospf-1)#distribute-list access-list zxr10 in





相关命令 :

无 




## domain-id 


domain-id 




命令功能 :

为某路由器指定域ID,使用no命令去掉域ID 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



domain-id 
  ＜domain-id 
＞

no domain-id 








命令参数解释 :



参数|描述
---|---
＜domain-id＞|点分十进制形式的ID








缺省 :

未配置时候，使用OSPF的实例号作为domain-id号。 






使用说明 :

该命令的作用是划定OSPF实例的VPN域，有着相同domain-id的实例，或者domain-id兼容的实例（一个路由器的domain-id是另外一个路由器的其中一个domain-id），被认为是在相同的域。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#domain-id 0.0.0.100





相关命令 :

无 




## domain-tag 


domain-tag 




命令功能 :

指定OSPF的域tag，使用no命令去掉域tag 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



domain-tag 
  ＜domain-tag 
＞

no domain-tag 








命令参数解释 :



参数|描述
---|---
＜domain-tag＞|当redistribute BGP的时候，生成的external LSA的tag值








缺省 :

无 






使用说明 :

配置了domain-tag，当redistribute BGP的时候，生成的external LSA的tag值为该配置值。在出现不必要的路由防环过滤的时候，可以用该命令在一端PE上修改tag值，在另一端PE上就不会进行防环过滤。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#domain-tag 1200





相关命令 :

无 




## dynamic-remote-lfa mpls-ldp capability 


dynamic-remote-lfa mpls-ldp capability 




命令功能 :

配置动态远端LFA capability功能。无no命令。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



dynamic-remote-lfa mpls-ldp capability 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|enable表示实例下使能动态LFA功能
disable|disable表示实例下去使能动态LFA功能








缺省 :

去使能。 






使用说明 :

无。 






范例 :

1.实例下使能动态LFA功能。ZXROSNG(config)router ospf 1ZXROSNG(config-ospf-1)# dynamic-remote-lfa mpls-ldp capability enable






相关命令 :

无 




## dynamic-remote-lfa mpls-ldp capability 


dynamic-remote-lfa mpls-ldp capability 




命令功能 :

区域下配置动态远端LFA capability功能，使用no命令取消配置。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



dynamic-remote-lfa mpls-ldp capability 
  {enable 
|disable 
}

no dynamic-remote-lfa mpls-ldp capability 








命令参数解释 :



参数|描述
---|---
enable|enable表示区域下使能动态LFA功能.
disable|disable表示区域下去使能动态LFA功能








缺省 :

无。 






使用说明 :

1.    如果不配置，区域下动态LFA功能没有配置，继承实例下dynamic-remote-lfa 的配置；2.    区域下可以配置使能，去使能两种状态。






范例 :

1.区域下使能动态LFA功能。ZXROSNG(config)router ospf 1ZXROSNG(config-ospf-1-area-1)# dynamic-remote-lfa mpls-ldp capability enable2.区域下去使能动态lfa功能。ZXROSNG(config-ospf-1- area-1)# dynamic-remote-lfa mpls-ldp capability disable3.区域下去动态lfa配置。ZXROSNG(config-ospf-1- area-1)#no dynamic-remote-lfa mpls-ldp capability






相关命令 :

无 




## dynamic-remote-lfa mpls-ldp maximum-cost 


dynamic-remote-lfa mpls-ldp maximum-cost 




命令功能 :

配置动态远端LFA maximum-cost值。使用no命令取消配置。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



dynamic-remote-lfa mpls-ldp maximum-cost 
  ＜maximum cost 
＞

no dynamic-remote-lfa mpls-ldp maximum-cost 








命令参数解释 :



参数|描述
---|---
＜maximum cost＞|隧道路径允许的最大cost值，当隧道计算出的cost大于该配置的cost时，隧道不可用，取值范围1-16777214。








缺省 :

无。 






使用说明 :

当隧道计算出的cost大于该配置的cost时，隧道不可用。 






范例 :

1.    实例下配置动态远端LFA maximum-cost值。ZXROSNG(config)router ospf 1ZXROSNG(config-ospf-1)# dynamic-remote-lfa mpls-ldp maximum-cost 100






相关命令 :

无 




## dynamic-remote-lfa mpls-ldp maximum-cost 


dynamic-remote-lfa mpls-ldp maximum-cost 




命令功能 :

区域下配置动态远端LFA maximum-cost值，使用no命令取消配置。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



dynamic-remote-lfa mpls-ldp maximum-cost 
  ＜maximum-cost 
＞

no dynamic-remote-lfa mpls-ldp maximum-cost 








命令参数解释 :



参数|描述
---|---
＜maximum-cost＞|隧道路径允许的最大cost值，当隧道计算出的cost大于该配置的cost时，隧道不可用，取值1-16777214。








缺省 :

无。 






使用说明 :

1.    当隧道计算出的cost大于该配置的cost时，隧道不可用。2.    如果没有配置区域下动态LFA maximum-cost值，继承实例下的配置值。






范例 :

1.区域下配置动态远端LFA maximum-cost值。ZXROSNG(config)router ospf 1ZXROSNG(config-ospf-1-area-1)# dynamic-remote-lfa mpls-ldp maximum-cost 1002.区域下删除配置动态远端lfa maximum-cost值。ZXROSNG(config-ospf-1-area-1)# no dynamic-remote-lfa mpls-ldp maximum-cost






相关命令 :

无 




## enable area 


enable area 




命令功能 :

如果存在所指区域，就使该区域有效。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



enable area 
  {＜area-id 
＞|＜area-id 
＞}







命令参数解释 :



参数|描述
---|---
＜area-id＞|区域标识符，可以指定为一个十进制点分形式的IP地址或十进制数值，数值范围：0–4294967295
＜area-id＞|区域标识符，可以指定为一个十进制点分形式的IP地址或十进制数值，数值范围：0–4294967295








缺省 :

无 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在命令show running-config中显示。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)# enable area 1





相关命令 :

无 




## enable interface 


enable interface 




命令功能 :

使能指定范围内失效的接口，对已经使能的接口该命令无效 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



enable interface 
  ＜ip-address 
＞ ＜wildcard-mask 
＞







命令参数解释 :



参数|描述
---|---
＜ip-address＞|IP地址，为十进制点分形式
＜wildcard-mask＞|反掩码，为十进制点分形式








缺省 :

如果已配置该interface，缺省状态为有效状态。 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在命令show running-config中显示。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#enable interface 10.1.0.0 0.0.255.255





相关命令 :

无 




## enable ip ospf 


enable ip ospf 




命令功能 :

如果该OSPF协议进程处于失效状态，则使能该OSPF协议，否则命令无效。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



enable ip ospf 
  ＜process-id 
＞







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在命令show running-config中显示。 






范例 :

ZXROSNG(config)#enable ip ospf 1 






相关命令 :

无 




## fast-reroute dynamic-remote-lfa 


fast-reroute dynamic-remote-lfa 




命令功能 :

配置动态远端LFA优先级，使用no命令取消配置。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute dynamic-remote-lfa 
 priority 
 ＜prority 
＞

no fast-reroute dynamic-remote-lfa 
 priority 








命令参数解释 :



参数|描述
---|---
＜prority＞|dynamic-remote-lfa优先级值，值越大优先级越小，取值范围1-255。






No参数|描述
---|---
priority|清除dynamic-remote-lfa优先级值








缺省 :

不配置默认动态LFA优先级值为110。 






使用说明 :

无。 






范例 :

1.实例下配置动态远端LFA优先级值。ZXROSNG(config)router ospf 1ZXROSNG(config-ospf-1)#fast-reroute dynamic-remote-lfa priority100






相关命令 :

无 




## fast-reroute lfa 


fast-reroute lfa 




命令功能 :

配置LFA优先级，使用no命令取消配置。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute lfa 
 priority 
 ＜prority 
＞

no fast-reroute lfa 
 priority 








命令参数解释 :



参数|描述
---|---
＜prority＞|LFA优先级值，值越大优先级越小，取值范围1-255






No参数|描述
---|---
priority|清除LFA优先级








缺省 :

不配置默认LFA优先级值为110。 






使用说明 :

无。 






范例 :

1.实例下配置LFA优先级值。ZXROSNG(config)router ospf 1ZXROSNG(config-ospf-1)#fast-reroute lfa priority 100






相关命令 :

无 




## fast-reroute policy-type 


fast-reroute policy-type 




命令功能 :

配置FRR备份路由策略。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute policy-type 
 route-policy 
 ＜route-policy 
＞

no fast-reroute policy-type 








命令参数解释 :



参数|描述
---|---
route-policy|策略类型为route-policy。
＜route-policy＞|策略名称。长度：1-31字符








缺省 :

如果没有配置该命令，缺省是不使能该功能的。 






使用说明 :

如果配置了该策略，那么只有匹配策略的路由条目才会把备份下一跳下给转发表。该策略对普通的IP FRR、DRLFA、SRLFA都生效。






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#fast-reroute policy-type route-policy zteZXROSNG(config-ospfv3-1)#






相关命令 :

无 




## fast-reroute static-remote-lfa 


fast-reroute static-remote-lfa 




命令功能 :

配置静态远端LFA优先级，使用no命令取消配置。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute static-remote-lfa 
 priority 
 ＜prority 
＞

no fast-reroute static-remote-lfa 
 priority 








命令参数解释 :



参数|描述
---|---
＜prority＞|static-remote-lfa优先级值，值越大优先级越小，取值范围1-255。






No参数|描述
---|---
priority|清除static-remote-lfa优先级值








缺省 :

不配置默认静态LFA优先级值为110。 






使用说明 :

无。 






范例 :

1.实例下配置静态远端LFA优先级值。ZXROSNG(config)router ospf 1ZXROSNG(config-ospf-1)#fast-reroute static-remote-lfa priority 100






相关命令 :

无 




## fast-reroute tiebreaker per-prefix downstream 


fast-reroute tiebreaker per-prefix downstream 




命令功能 :

为每前缀FRR配置downstream保护类型备份下一跳的优先级 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute tiebreaker per-prefix downstream 
 index 
 ＜downstream-index 
＞

no fast-reroute tiebreaker per-prefix downstream 








命令参数解释 :



参数|描述
---|---
＜downstream-index＞|downstream保护类型备份下一跳的优先级，范围1-255








缺省 :

90 






使用说明 :

该配置只有在使能了FRR之后才能生效。优先级数值越小，优先级越高。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#fast-reroute tiebreaker per-prefix downstream index 109ZXROSNG(config-ospf-1)#






相关命令 :

fast-reroute 




## fast-reroute tiebreaker per-prefix lowest-backup-metric 


fast-reroute tiebreaker per-prefix lowest-backup-metric 




命令功能 :

为每前缀FRR配置最小花费类型备份下一跳的优先级。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute tiebreaker per-prefix lowest-backup-metric 
 index 
 ＜lower-metric-index 
＞

no fast-reroute tiebreaker per-prefix lowest-backup-metric 








命令参数解释 :



参数|描述
---|---
＜lower-metric-index＞|花费最小类型备份下一跳的优先级，范围1-255








缺省 :

110 






使用说明 :

该配置只有在使能了FRR之后才能生效。优先级数值越小，优先级越高。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#fast-reroute tiebreaker per-prefix lowest-backup-metric index 109ZXROSNG(config-ospf-1)#






相关命令 :

fast-reroute 




## fast-reroute tiebreaker per-prefix node-protecting 


fast-reroute tiebreaker per-prefix node-protecting 




命令功能 :

为每前缀FRR配置节点保护类型备份下一跳的优先级。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute tiebreaker per-prefix node-protecting 
 index 
 ＜node-protecting-index 
＞

no fast-reroute tiebreaker per-prefix node-protecting 








命令参数解释 :



参数|描述
---|---
＜node-protecting-index＞|节点保护类型备份下一跳的优先级，范围1-255








缺省 :

70 






使用说明 :

该配置只有在使能了FRR之后才能生效。优先级数值越小，优先级越高。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#fast-reroute tiebreaker per-prefix node-protecting index 109ZXROSNG(config-ospf-1)#






相关命令 :

fast-reroute 




## fast-reroute tiebreaker per-prefix primary-path 


fast-reroute tiebreaker per-prefix primary-path 




命令功能 :

为每前缀FRR配置ECMP类型备份下一跳的优先级。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute tiebreaker per-prefix primary-path 
 index 
 ＜primary-path-index 
＞

no fast-reroute tiebreaker per-prefix primary-path 








命令参数解释 :



参数|描述
---|---
＜primary-path-index＞|ECMP类型备份下一跳的优先级，范围1-255。








缺省 :

30 






使用说明 :

该配置只有在使能了FRR之后才能生效。优先级数值越小，优先级越高。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#fast-reroute tiebreaker per-prefix primary-path index 109ZXROSNG(config-ospf-1)#






相关命令 :

fast-reroute 




## fast-reroute tiebreaker per-prefix secondary-path 


fast-reroute tiebreaker per-prefix secondary-path 




命令功能 :

为每前缀FRR配置非ECMP类型备份下一跳的优先级。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute tiebreaker per-prefix secondary-path 
 index 
 ＜secondary-path-index 
＞

no fast-reroute tiebreaker per-prefix secondary-path 








命令参数解释 :



参数|描述
---|---
＜secondary-path-index＞|非ECMP类型备份下一跳的优先级，范围1-255。








缺省 :

50 






使用说明 :

该配置只有在使能了FRR之后才能生效。优先级数值越小，优先级越高。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#fast-reroute tiebreaker per-prefix secondary-path index 109ZXROSNG(config-ospf-1)#






相关命令 :

fast-reroute 




## fast-reroute ti-lfa priority 


fast-reroute ti-lfa priority 




命令功能 :

OSPF配置TI-LFA备份路由的优先级。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute ti-lfa priority 
  ＜priority 
＞

no fast-reroute ti-lfa priority 








命令参数解释 :



参数|描述
---|---
＜priority＞|TI-LFA的优先级，范围：1-255








缺省 :

110 






使用说明 :

数值越小，优先级越高。 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#fast-reroute ti-lfa priority 120 ZXROSNG(config-ospf-1)#






相关命令 :

IPv4-OSPF模式下的ti-lfa capability命令 




## fast-reroute 


fast-reroute 




命令功能 :

指定OSPF快速重计算备份路由（fast-reroute）的类型。使用no命令恢复缺省值 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute 
 per-prefix 


no fast-reroute 
 per-prefix 








命令参数解释 :



参数|描述
---|---
per-prefix|在每个前缀上实现FRR








缺省 :

无 






使用说明 :

无 






范例 :

1.实例下使能FRR功能。ZXROSNG(config-ospf-1)#fast-reroute per-prefix2.实例下去使能FRR功能。ZXROSNG(config-ospf-1)#no fast-reroute per-prefix






相关命令 :

无 




## fast-reroute 


fast-reroute 




命令功能 :

设置接口上的快速重计算路由（fast-reroute）属性。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute 
  {disable 
|backup-interface 
 ＜interface-name 
＞}

no fast-reroute 








命令参数解释 :



参数|描述
---|---
disable|快速重计算路由无效
＜interface-name＞|指定接口名








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#fast-reroute backup-interface gei-0/1/0/2





相关命令 :

无 




## fast-reroute 


fast-reroute 




命令功能 :

设置接口上的快速重计算路由（fast-reroute）属性。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute 
  {disable 
}

no fast-reroute 








命令参数解释 :



参数|描述
---|---
disable|快速重计算路由无效








缺省 :

[M6000\M6000-S\ZSR]无[89\9900]快速重计算无效





使用说明 :

无 






范例 :

[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#area 1 ZXR10 (config-ospf-1-area)#interface gei-0/1/0/1ZXR10 (config-ospf-1-area-if-gei-0/1/0/1)#fast-reroute disable[ZSR]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#area 1 ZXR10 (config-ospf-1-area)#interface gei-1/1ZXR10 (config-ospf-1-area-if-gei-1/1)#fast-reroute disable[89\9900]1. 指定接口vlan1上快速重计算路由的备份接口为vlan2：ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#area 1 ZXROSNG(config-ospf-1-area)#interface vlan1ZXROSNG(config-ospf-1-area-interface)#fast-reroute disable





相关命令 :

无 




## filter 


filter 




命令功能 :

控制外部LSA产生的路由是否导入路由表以及导入的优先级。使用no命令去除设定的过滤命令。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


filter 
  [exact 
] ＜ip-address 
＞ ＜net-mask 
＞ ＜prefence 
＞
no filter 
  ＜ip-address 
＞ ＜net-mask 
＞
				






命令参数解释 :



参数|描述
---|---
exact|表示精确匹配
＜ip-address＞|IP地址，为十进制点分形式
＜net-mask＞|IP子网掩码，十进制点分形式
＜prefence＞|描述导入匹配路由的优先级，范围：1–255








缺省 :

外部LSA产生的路由导入路由表中。 






使用说明 :

1. 该命令是在路由层面上不向转发表添加不符合添加条件的OSPF路由，而命令area filter-list的过滤是在数据库的层面上控制某些LSA的产生。2. 路由的优先级为255时，该路由不生效。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#filter exact 10.10.10.0 255.255.255.0 20





相关命令 :

无 




## filter-list 


filter-list 




命令功能 :

实现在OSPF区域之间网络路由信息的过滤。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


filter-list 
 prefix 
 ＜prefix-list 
＞ {out 
|in 
}
no filter-list 
  {out 
|in 
}
				






命令参数解释 :



参数|描述
---|---
＜prefix-list＞|前缀列表的名称
out|从该区域中导出路由信息时进行过滤
in|从该区域中导入路由信息时进行过滤








缺省 :

OSPF区域之间无网络路由信息的过滤。 






使用说明 :

1. 如果该区域不存在则自动创建。2. filter-list的in命令，指某区域不允许相应3型LSA进入该区域， 所以就不会有路由。out命令，指某区域不允许相应的路由生成3型LSA到别的区域。3. 该命令只用于在ABR上过滤3型的LSA对应的路由，对5型的路由无效。4. 该命令只有满足匹配的时候才是permit，否则是deny all。即，如果模板不存在，或者存在但是匹配不上，都为deny。






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 1ZXROSNG(config-ospf-1-area-1)#network 20.20.20.0 0.0.0.255ZXROSNG(config-ospf-1-area-1)#exitZXROSNG(config-ospf-1)#exitZXROSNG(config)#ip prefix-list zxr10 deny 20.20.20.0 24ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 1ZXROSNG(config-ospf-1-area-1)#filter-list prefix zxr10 outZXROSNG(config-ospf-1-area-1)#





相关命令 :

无 




## grace-period 


grace-period 




命令功能 :

配置NSF运行所需的最长时间，使用no命令还原为默认值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



grace-period 
  ＜period 
＞

no grace-period 








命令参数解释 :



参数|描述
---|---
＜period＞|无中断转发进行的最长的时间值，范围：1–1800，单位：秒








缺省 :

无中断转发进行的最长时间的值缺省值是120s。 






使用说明 :

Grace-period的值必须能够确保在该时间后NSF能够顺利完成，否则会在NSF没有完成之前就超时退出NSF，达不到无中断的要求。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#grace-period 300





相关命令 :

无 




## hello-interval 


hello-interval 




命令功能 :

配置接口发送HELLO报文的时间间隔。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



hello-interval 
  ＜seconds 
＞

no hello-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口发送HELLO报文的时间间隔，缺省为1/4的缺省dead-interval时长。当网络类型为广播网或P2P时，缺省为10秒；当网络类型为P2MP或NBMA网络时，缺省为30秒，范围：1–65535，单位：秒








缺省 :

缺省为1/4的缺省dead-interval时长. 






使用说明 :

无 






范例 :

ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#hello-interval 40 






相关命令 :

无 




## hello-interval 


hello-interval 




命令功能 :

配置接口发送HELLO报文的时间间隔。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



hello-interval 
  ＜seconds 
＞

no hello-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口发送HELLO报文的时间间隔，缺省为1/4的缺省dead-interval时长。当网络类型为广播网或P2P时，缺省为10秒；当网络类型为P2MP或NBMA网络时，缺省为30秒，范围：1–65535，单位：秒








缺省 :

缺省为1/4的缺省dead-interval时长. 






使用说明 :

无 






范例 :

[89\9900]1. 指定接口上发送hello报文的时间间隔为40秒：ZXROSNG(config-ospfv2-if)#hello-interval 40[M6000\M6000-S\ZSR]ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#hello-interval 40





相关命令 :

无 




## hello-interval 


hello-interval 




命令功能 :

配置多区域接口的hello周期。 






命令模式 :

 IPv4-OSPF-MULTI-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



hello-interval 
  ＜seconds 
＞

no hello-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口发送HELLO报文的时间间隔，不配置的情况下，缺省为1/4的缺省dead-interval时长；不配置dead-interval时，缺省为10秒，范围：1–65535，单位：秒








缺省 :

不配置的情况下，缺省为1/4的缺省dead-interval时长；不配置dead-interval时，缺省为10秒。 






使用说明 :

使用场景在使用多区域接口建链时，应当配置两端hello-interval相同，才能建链成功。多区域接口会以hello-interval的时间间隔发送HELLO报文。






范例 :

配置IPv4 OSPF实例1的区域100下添加fei-0/1/0/1多区域接口，配置多区域接口fei-0/1/0/1发送和接收Hello包的时间间隔为120秒。R1(config)#router ospf 1R1(config-ospf-1)#area 100R1(config-ospf-1-area-100)#multi-area-interface fei-0/1/0/1R1(config-ospf-1-area-100-mif-fei-0/1/0/1)# hello-interval 120






相关命令 :

无 




interface :

interface (IPv4-OSPF模式) 




命令功能 :

选择一个接口进行配置。 






命令模式 :

 IPv4-OSPF模式  






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
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-ospf-1)#interface gei-0/1/0/1                                     ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#





相关命令 :

无 




interface :

interface (IPv4-OSPF区域模式) 




命令功能 :

选择一个接口进行配置。 






命令模式 :

 IPv4-OSPF区域模式  






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
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

[M6000\M6000-S\ZSR]无[89\9900]使用此命令会进入OSPF接口配置模式





范例 :

[89\9900][89\9900]:1. 配置模式下选择接口进行配置：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if)#2. 路由ospf模式下选择接口进行配置ZXROSNG(config-ospfv2)#interface gei-0/1/0/1ZXROSNG(config-ospfv2-if)#[ZSR]:1. 配置模式下选择接口进行配置：ZXROSNG(config)#interface gei-1/1ZXROSNG(config-if)#2. 路由ospf模式下选择接口进行配置ZXROSNG(config-ospfv2)#interface gei-1/1ZXROSNG(config-ospfv2-if)#[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config-ospf-1)#interface gei-0/1/0/1ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#[ZSR]:ZXROSNG(config-ospf-1)#interface gei-1/1ZXROSNG(config-ospf-1-if-gei-1/1)#





相关命令 :

无 




## ispf 


ispf 




命令功能 :

使能OSPFv2实例的增量SPF计算功能。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



ispf 
 

no ispf 








命令参数解释 :


					无
				 






缺省 :

缺省没有配置。 






使用说明 :

无 






范例 :

1.使能ispf功能ZXROSNG(config-ospf-1)# ispf2.去使能ispf功能ZXROSNG(config-ospf-1)#no ispf





相关命令 :

无 




## local-mt 


local-mt 




命令功能 :

使能自动路由short-cut方式的时候，为组播路由协议生成下一跳是物理口的路由 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



local-mt 
 enable 


no local-mt 








命令参数解释 :



参数|描述
---|---
enable|使能自动路由short-cut方式的时候，为组播路由协议生成下一跳是物理口的路由








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-ospf-1)#local-mt enable ZXROSNG(config-ospf-1)#
ZXROSNG(config-ospf-1)#no local-mt ZXROSNG(config-ospf-1)#






相关命令 :

无 




## lsa-limit 


lsa-limit 




命令功能 :

开启OSPF链路状态数据库过载保护功能 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



lsa-limit 
  ＜max-number 
＞ [{[warning 
 [threshold 
 ＜threshold 
＞]]|{[limit-cnt 
 ＜limit-cnt 
＞],[limit-time 
 ＜limit-time 
＞],[refresh-time 
 ＜refresh-time 
＞],[threshold 
 ＜threshold 
＞]}}]

no lsa-limit 








命令参数解释 :



参数|描述
---|---
＜max-number＞|开启OSPF链路状态数据库过载保护功能
warning|配置实例数据库超载后的行为
＜threshold＞|配置告警门限的值
＜limit-cnt＞|配置允许进入limit state状态的次数
＜limit-time＞|配置处于limit state状态的时间片
＜refresh-time＞|配置刷新limit cnt的时间片
＜threshold＞|配置告警门限的值








缺省 :

warning的默认值为FALSEthreshold默认值为75slimit-time默认值为5slimit-cnt默认值为5srefresh-time默认值为10s





使用说明 :

无 






范例 :

1 配置接口重传LSA的时间间隔为10秒:ZXE10(config)#router ospf 1ZXE10(config-ospf-1)#lsa-limit 1000 limit-time 5 limit-cnt 5 refresh-time 10






相关命令 :

无 




## maximum-paths 


maximum-paths 




命令功能 :

设置OSPF协议负载均衡时支持的最大路由数目。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



maximum-paths 
  ＜path-number 
＞

no maximum-paths 








命令参数解释 :



参数|描述
---|---
＜path-number＞|设置OSPF协议负载均衡时支持的最大路由数目，缺省为1，范围：1-$#134283317#$








缺省 :

负载均衡最大路由是1 






使用说明 :

1. 当路由器有了一个完整的链路状态数据库时，它就准备好要创建它的路由表以便能够转发数据流。缺省的开销度量是基于网络介质的带宽。要计算到达目的地的最低开销，可以通过maximum-paths进行配置。2. 路由器一般选择具有最小度量值的路径；如果同时出现了多条度量值最低且相同的路径，那么在这多条路径上将启用负载均衡，通过使用maximum-paths命令可以支持多条相同度量值路径。3. 该命令立刻生效，分时处理，无需用户手工干预，但需要等待一定的时间。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#maximum-paths 4





相关命令 :

无 




## max-metric 


max-metric 




命令功能 :

设置自己产生的路由器最大metric值LSA的时间间隔。使用no命令恢复缺省值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


max-metric 
 router-lsa 
 [on-startup 
 {wait-for-bgp 
|timeout 
 ＜timeout 
＞}]
no max-metric 
 router-lsa 
 [on-startup 
 {wait-for-bgp 
|timeout 
}]
				






命令参数解释 :



参数|描述
---|---
router-lsa|命令作用对象为router-lsa
wait-for-bgp|等待BGP确定何时产生路由器LSA
＜timeout＞|设置产生最大metric值的时间间隔






No参数|描述
---|---
timeout|清除产生最大metric值的时间间隔








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#max-metric router-lsa on-startup timeout 100





相关命令 :

无 




## message-digest-key 


message-digest-key 




命令功能 :

为采用报文摘要口令认证类型的接口设置口令序号对。使用no命令删除配置的OSPF口令。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :


message-digest-key 
  ＜key-id 
＞ md5 
 {encrypted 
 ＜md5-key 
＞|clear 
 ＜md5-key 
＞|＜md5-key 
＞} [delay 
 ＜delay 
＞]
no message-digest-key 
  ＜key-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜key-id＞|口令序号，范围：1–255
md5|配置md5加密的密码
＜md5-key＞|经加密后的认证口令，长度24个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\，实际上该字段是不建议随意配置的，因为其对应的明文密码无法直接获取。
＜md5-key＞|经加密后的认证口令，长度24个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\，实际上该字段是不建议随意配置的，因为其对应的明文密码无法直接获取。
＜md5-key＞|经加密后的认证口令，长度24个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\，实际上该字段是不建议随意配置的，因为其对应的明文密码无法直接获取。
＜delay＞|延迟时间，范围：0–100000，单位：分钟








缺省 :

不指定口令。 






使用说明 :

如果带可选参数，协议数据包的发送在<time>分钟内,暂时不使用该口令序号对来发送报文，但可以接收。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#message-digest-key 2 md5 zxr10





相关命令 :

无 




## message-digest-key 


message-digest-key 




命令功能 :

为采用报文摘要口令认证类型的接口设置口令序号对。使用no命令删除配置的OSPF口令。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :


message-digest-key 
  ＜key-id 
＞ md5 
 {encrypted 
 ＜md5-key 
＞|clear 
 ＜md5-key 
＞|＜md5-key 
＞} [delay 
 ＜delay 
＞]
no message-digest-key 
  ＜key-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜key-id＞|口令序号，范围：1–255
md5|配置md5加密的密码
＜md5-key＞|认证口令，长度1–16个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜md5-key＞|认证口令，长度1–16个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜md5-key＞|认证口令，长度1–16个字符（不包含空格），允许的字符范围如下： 0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\
＜delay＞|延迟时间，范围：0–100000，单位：分钟








缺省 :

不指定口令。 






使用说明 :

如果带可选参数，协议数据包的发送在<time>分钟内,暂时不使用该口令序号对来发送报文，但可以接收。 






范例 :

[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#message-digest-key 2 md5 zxr10[ZSR]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-1/1ZXR10 (config-ospf-1-if-gei-1/1)#message-digest-key 2 md5 zxr10[89\9900]1. 为采用报文摘要口令认证类型的接口设置口令序号为２，认证口令为zxr10：ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#interface vlan1ZXR10 (config-ospfv2-if)#message-digest-key 2 md5 zxr10





相关命令 :

[M6000\M6000-S\ZSR]无[89\9900]authentication [null|message-digest]



## microloop-prevention remote-lfa capability 


microloop-prevention remote-lfa capability 




命令功能 :

配置远端LFA微环保护能力。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



microloop-prevention remote-lfa capability 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能远端LFA微环保护
disable|去使能远端LFA微环保护








缺省 :

使能远端LFA微环保护 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)# microloop-prevention remote-lfa capability enable





相关命令 :

microloop-prevention remote-lfa delay-time 




## microloop-prevention remote-lfa delay-time 


microloop-prevention remote-lfa delay-time 




命令功能 :

配置远端LFA微环保护路由延迟时间。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



microloop-prevention remote-lfa delay-time 
  ＜delay-time 
＞

no microloop-prevention remote-lfa delay-time 








命令参数解释 :



参数|描述
---|---
＜delay-time＞|路由延迟时间，单位：毫秒，范围：1-300000








缺省 :

3000 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)# microloop-prevention remote-lfa delay-time 10





相关命令 :

microloop-prevention remote-lfa capability 




## mpls ldp auto-config 


mpls ldp auto-config 




命令功能 :

实例下使能LDP自动配置功能。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp auto-config 
 

no mpls ldp auto-config 








命令参数解释 :


					无
				 






缺省 :

不配置LDP自动配置功能。 






使用说明 :

如果需要在某个实例下使能LDP自动配置功能，必须配置该命令。 






范例 :

设置OSPF实例1使能LDP自动配置功能：ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#mpls ldp auto-config





相关命令 :

IPv4-OSPF模式下area mpls ldp auto-config配置命令和IPv4-OSPF接口模式下mpls ldp auto-config配置命令。这三个配置命令的优先顺序依次是：接口、区域和实例。例如：接口下配置了去使能，即使区域和实例下使能，命令生效为去使能。 




## mpls ldp auto-config 


mpls ldp auto-config 




命令功能 :

接口下使能LDP自动配置功能。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp auto-config 
  {enable 
|disable 
}

no mpls ldp auto-config 








命令参数解释 :



参数|描述
---|---
enable|使能LDP自动配置功能。
disable|去使能LDP自动配置功能。








缺省 :

不配置LDP自动配置功能。 






使用说明 :

如果需要在接口下使能LDP自动配置功能，必须配置该命令。 






范例 :

设置接口gei-0/1/0/1使能LDP自动配置功能：ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#interface gei-0/1/0/1ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#mpls ldp auto-config enable





相关命令 :

IPv4-OSPF模式下mpls ldp auto-config配置命令和area mpls ldp auto-config配置命令。这三个配置命令的优先顺序依次是：接口、区域和实例。例如：接口下配置了去使能，即使区域和实例下使能，命令生效为去使能。 




## mpls ldp auto-config 


mpls ldp auto-config 




命令功能 :

区域下使能LDP自动配置功能。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp auto-config 
  {enable 
|disable 
}

no mpls ldp auto-config 








命令参数解释 :



参数|描述
---|---
enable|使能该功能
disable|去使能该功能








缺省 :

不配置LDP自动配置功能。 






使用说明 :

如果需要在某个区域下使能LDP自动配置功能，必须配置该命令 






范例 :

设置区域0使能LDP自动配置功能：ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#area 0ZXROSNG(config-ospf-1-area-0)#mpls ldp auto-config enable ZXROSNG(config-ospf-1-area-0)#






相关命令 :

IPv4-OSPF模式下mpls ldp auto-config配置命令和IPv4-OSPF接口模式下mpls ldp auto-config配置命令。这三个配置命令的优先顺序依次是：接口、区域和实例。例如：接口下配置了去使能，即使区域和实例下使能，命令生效为去使能。 




## mpls ldp auto-config 


mpls ldp auto-config 




命令功能 :

接口下使能LDP自动配置功能。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp auto-config 
  {enable 
|disable 
}

no mpls ldp auto-config 








命令参数解释 :



参数|描述
---|---
enable|使能接口下LDP自动配置功能
disable|接口下LDP自动配置功能去使能








缺省 :

不使能接口下自动配置功能 






使用说明 :

无 






范例 :

[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#mpls ldp auto-config [ZSR]:ZXROSNG(config-ospf-1-if-gei-1/1)#mpls ldp auto-config [89\9900][89\9900]:ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#mpls ldp auto-config [ZSR]:ZXROSNG(config-ospf-1-if-gei-1/1)#mpls ldp auto-config 





相关命令 :

[M6000\M6000-S\ZSR]实例下使能LDP IGP同步功能：mpls ldp sync区域下使能LDP IGP同步功能area <area_id> mpls ldp sync  [disable][89\9900]实例下使能LDP IGP同步功能：mpls ldp auto-config 区域下使能LDP自动配置功能area <area_id> mpls ldp auto-config  [disable]



## mpls ldp sync set-max-distance 


mpls ldp sync set-max-distance 




命令功能 :

使能LDP-IGP未同步时设置最大路由管理距离功能 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp sync set-max-distance 
 

no mpls ldp sync set-max-distance 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

OSPF实例下配置LDP-IGP同步功能后（即配置mpls ldp sync），该命令才能生效 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#mpls ldp sync set-max-distance ZXROSNG(config-ospf-1)#






相关命令 :

mpls ldp sync 




## mpls ldp sync 


mpls ldp sync 




命令功能 :

Ospf实例下使能LDP IGP同步功能 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp sync 
 

no mpls ldp sync 








命令参数解释 :


					无
				 






缺省 :

不使能LDP IGP同步功能 






使用说明 :

OSPF实例下使能ldp igp同步功能后，实例下所有的接口同步使能 






范例 :

ZXROSNG(config-ospf-1)#mpls ldp sync 






相关命令 :

区域下使能LDP IGP同步功能：area <area_id> mpls ldp sync  [disable]接口下使能LDP IGP同步功能mpls ldp sync  [disable]



## mpls ldp sync 


mpls ldp sync 




命令功能 :

接口下使能LDP IGP同步功能。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp sync 
  [disable 
]

no mpls ldp sync 








命令参数解释 :



参数|描述
---|---
disable|接口 下LDP  IGP同步功能去使能








缺省 :

不使能LDP IGP同步功能 






使用说明 :

无 






范例 :

ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#mpls ldp sync 






相关命令 :

实例下使能LDP IGP同步功能：mpls ldp sync 区域下使能LDP IGP同步功能area <area_id> mpls ldp sync  [disable]



## mpls ldp sync 


mpls ldp sync 




命令功能 :

区域下使能LDP IGP同步功能。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp sync 
  [disable 
]

no mpls ldp sync 








命令参数解释 :



参数|描述
---|---
disable|Area 下LDP  IGP同步功能去使能








缺省 :

不使能LDP IGP同步功能 






使用说明 :

区域下使能ldp igp同步功能后，区域下所有的接口同步使能 






范例 :

ZXROSNG(config-ospf-1)#ZXROSNG(config-ospf-1)#area 0ZXROSNG(config-ospf-1-area-0)# mpls ldp sync





相关命令 :

实例下使能LDP IGP同步功能：mpls ldp sync接口下使能LDP IGP同步功能mpls ldp sync  [disable]



## mpls ldp sync 


mpls ldp sync 




命令功能 :

接口下使能LDP IGP同步功能。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp sync 
  [disable 
]

no mpls ldp sync 








命令参数解释 :



参数|描述
---|---
disable|接口 下LDP  IGP同步功能去使能








缺省 :

不使能LDP IGP同步功能 






使用说明 :

无 






范例 :

[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#mpls ldp sync[ZSR]:ZXROSNG(config-ospf-1-if-gei-1/1)#mpls ldp sync[89\9900][89\9900]:ZXROSNG(config-ospf-1-if-gei-0/1/0/1)#mpls ldp sync[ZSR]:ZXROSNG(config-ospf-1-if-gei-1/1)#mpls ldp sync





相关命令 :

[M6000\M6000-S\ZSR]实例下使能LDP IGP同步功能：mpls ldp sync区域下使能LDP IGP同步功能area <area_id> mpls ldp sync  [disable][89\9900]实例下使能LDP IGP同步功能：mpls ldp sync区域下使能LDP IGP同步功能area <area_id> mpls ldp sync  [disable]



## mpls traffic-eng 


mpls traffic-eng 




命令功能 :

启用设备支持产生自己的TE信息并洪泛到特定区域。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



mpls traffic-eng 
 

no mpls traffic-eng 








命令参数解释 :


					无
				 






缺省 :

不支持。 






使用说明 :

如果需要在某个区域上支持流量工程，必须配置该命令。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#area 1ZXROSNG(config-ospf-1-area-1)#mpls traffic-eng ZXROSNG(config-ospf-1-area-1)#





相关命令 :

无 




## mtu-ignore 


mtu-ignore 




命令功能 :

配置接口忽略DD报文交换时的MTU检查。使用no命令恢复缺省状态。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



mtu-ignore 
 

no mtu-ignore 








命令参数解释 :


					无
				 






缺省 :

DD报文交换时检查MTU。 






使用说明 :

1. MTU检查主要是检查对方填写在DD报文的MTU字段的值，是否小于等于本接口的MRU，否则丢弃该DD报文。2. 如果确认收发报文时，MTU没有配置上的问题，可通过配置本命令忽略该检测。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#mtu-ignore 





相关命令 :

无 




## mtu-ignore 


mtu-ignore 




命令功能 :

配置接口忽略DD报文交换时的MTU检查。使用no命令恢复缺省状态。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



mtu-ignore 
 

no mtu-ignore 








命令参数解释 :


					无
				 






缺省 :

DD报文交换时检查MTU。 






使用说明 :

1. MTU检查主要是检查对方填写在DD报文的MTU字段的值，是否小于等于本接口的MRU，否则丢弃该DD报文。2. 如果确认收发报文时，MTU没有配置上的问题，可通过配置本命令忽略该检测。





范例 :

[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#mtu-ignore[ZSR]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-1/1ZXR10 (config-ospf-1-if-gei-1/1)#mtu-ignore[89\9900]1. 如果确认收发报文时MTU没有配置上的问题，可通过配置本命令忽略该检测：ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#interface vlan1ZXR10 (config-ospfv2-if)#mtu-ignore





相关命令 :

无 




## mtu-ignore 


mtu-ignore 




命令功能 :

配置接口忽略DD报文交换时的MTU检查。 






命令模式 :

 IPv4-OSPF-MULTI-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



mtu-ignore 
 

no mtu-ignore 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

使用场景在使用多区域接口建链时，如果不希望MTU检查影响DD报文交互从而影响建链，则应配置此命令。






范例 :

配置IPv4 OSPF实例1的区域100下添加fei-0/1/0/1多区域接口，配置多区域接口fei-0/1/0/1接收DD包时忽略MTU字段。R1(config)#router ospf 1R1(config-ospf-1)#area 100R1(config-ospf-1-area-100)#multi-area-interface fei-0/1/0/1R1(config-ospf-1-area-100-mif-fei-0/1/0/1)# mtu-ignore






相关命令 :

无 




## neighbor 


neighbor 




命令功能 :

配置非广播网络上的邻居路由器，需要对所有接口进行遍历，当邻居IP地址和接口的IP地址在同一网段时，将邻居挂接到该接口。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


neighbor 
  ＜neighbor-id 
＞ [{[priority 
 ＜priority 
＞],[poll-interval 
 ＜seconds 
＞],[cost 
 ＜cost 
＞]}]
no neighbor 
  ＜neighbor-id 
＞ [{[priority 
],[poll-interval 
],[cost 
]}]
				






命令参数解释 :



参数|描述
---|---
＜neighbor-id＞|邻居IP地址，为十进制点分形式
＜priority＞|邻居的优先级，对点到多点邻居无效，范围：0–255
＜seconds＞|邻居的轮询间隔，对点到多点邻居无效，范围：1–65535
＜cost＞|到邻居的代价，对NBMA邻居无效，范围：1–65535






No参数|描述
---|---
priority|清除邻居的优先级
poll-interval|清除邻居的轮询时间
cost|清除邻居的花费








缺省 :

没有定义邻居路由器。点到多点邻居的代价缺省为自动计算；NBMA邻居的优先级缺省为1；NBMA邻居的轮询间隔缺省为120。






使用说明 :

1. 只对点到多点非广播网络和NBMA网络进行该配置。2. no neighbor <ip-address> cost使到邻居的代价恢复到缺省值。3. no neighbor <ip-address> priority使邻居优先级恢复到缺省值。4. no neighbor <ip-address> poll-interval使邻居轮询间隔恢复到缺省值。5. no neighbor <ip-address>删除指定邻居。同配置邻居的命令一样，此命令也需要对接口进行遍历，找到邻居所属的接口并从中将邻居删除。6. 没有配置neighbor <ip-address> cost，使用cost或者默认值。有配置neighbor <ip-address> cost，建链的接口也配置cost，前者生效。7. neighbor priority是指定某邻居优先级，用于初期选举DR，BDR，如果priority为0，该邻居不参与DR，BDR的选举。真正建链以后，会以邻居的hello报文里面通告的值为准。建议该值配置来和实际的邻居priority一致。






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#neighbor 10.1.1.3





相关命令 :

无 




network :

network 




命令功能 :

定义OSPF协议运行的接口以及对这些接口定义区域ID，如果该区域不存在则自动创建。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


network 
  ＜ip-address 
＞ ＜wildcard-mask 
＞
no network 
  ＜ip-address 
＞ ＜wildcard-mask 
＞
				






命令参数解释 :



参数|描述
---|---
＜ip-address＞|IP地址，为十进制点分形式
＜wildcard-mask＞|反掩码，为十进制点分形式








缺省 :

将要配置的网段不属于任何区域。 






使用说明 :

1. 定义OSPF协议运行的接口以及对这些接口定义区域ID，如果该区域不存在则自动创建。2. 当IP接口地址对应<wildcard-mask>的“0”bit位和<ip-address>相等时，我们称该命令对该IP接口地址有效。当多个network命令对同一IP接口地址有效时，该IP接口地址所对应的OSPF接口将被创建，并被附加在<wildcard-mask>最小的network命令所指定的区域中。当新配的IP接口地址存在对该IP接口有效的network命令，该IP接口地址所对应的OSPF接口将自动被创建，并被附加在对它有效的<wildcard-mask>最小的network命令所指定的区域中。当IP接口地址被删除时，OSPF接口也将自动被删除。3. no命令是只针对已配置的network命令的反操作，如果不存在相应network命令，则no命令无效。如果存在相应network命令，且network命令对OSPF区域中的OSPF接口有效，则使这些OSPF接口脱离该区域。如果还存在其它对OSPF接口的IP接口地址有效的network命令，则将其附加到该network命令中指定的OSPF区域中。如果多个network命令对同一接口有效，则将其附加到<wildcard-mask>最小的network命令中指定的OSPF区域。如果不存在其它对该接口有效的network命令，则删除该OSPF接口。






范例 :

配置实例1区域0下的网络，网络号是149.88.1.0，掩码是255.255.255.0：ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 0ZXROSNG(config-ospf-1-area-0)#network 149.88.1.0 0.0.0.255





相关命令 :

无 




network :

network 




命令功能 :

配置接口类型。使用no命令使接口类型恢复到接口的网络类型。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



network 
  {broadcast 
|non-broadcast 
|point-to-point 
|point-to-multipoint 
 [non-broadcast 
]}

no network 








命令参数解释 :



参数|描述
---|---
broadcast|广播类型
non-broadcast|点到多点类型的非广播类型（要配合neighbor命令使用）
point-to-point|点到点类型
point-to-multipoint|点到多点类型
non-broadcast|点到多点类型的非广播类型（要配合neighbor命令使用）








缺省 :

无 






使用说明 :

依赖于网络类型，点到多点类型需配置。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#network point-to-point





相关命令 :

无 




network :

network 




命令功能 :

配置接口类型。使用no命令使接口类型恢复到接口的网络类型。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



network 
  {broadcast 
|non-broadcast 
|point-to-point 
|point-to-multipoint 
 [non-broadcast 
]}

no network 








命令参数解释 :



参数|描述
---|---
broadcast|广播类型
non-broadcast|点到多点类型的非广播类型（要配合neighbor命令使用）
point-to-point|点到点类型
point-to-multipoint|点到多点类型
non-broadcast|点到多点类型的非广播类型（要配合neighbor命令使用）








缺省 :

无 






使用说明 :

依赖于网络类型，点到多点类型需配置。 






范例 :

[89\9900]1. 将接口vlan1配置成point-to-point接口类型：ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 0ZXROSNG(config-ospf-1-area-0)#interface vlan1ZXROSNG(config-ospf-1-area-0-if-vlan1)#network point-to-point[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 0ZXROSNG(config-ospf-1-area-0)#interface gei-0/1/0/1ZXROSNG(config-ospf-1-area-0-if-gei-0/1/0/1)#network point-to-point[ZSR]:ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 0ZXROSNG(config-ospf-1-area-0)#interface gei-1/1ZXROSNG(config-ospf-1-area-0-if-gei-1/1)#network point-to-point






相关命令 :

无 




## notify default route 


notify default route 




命令功能 :

当本路由器通过其他协议或配置静态路由方式获得一条缺省路由0.0.0.0/0时，需要将其通告；没有缺省路由时，则按正常方式通告具体的可达路由；使用该命令后路由器成为一个ASBR。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


notify default route 
  [{[always 
],[metric 
 ＜metric-value 
＞],[metric-type 
 {ext-2 
|ext-1 
}],[route-map 
 ＜map-tag 
＞]}]
no notify default route 
  [{[always 
],[metric 
],[metric-type 
],[route-map 
]}]
				






命令参数解释 :



参数|描述
---|---
always|指定always表示不论本路由器是否存在缺省路由，都通告缺省路由；如果没有指定always则根据路由器的路由表中是否有缺省路由来决定是否通告，若存在缺省路由则通告，若不存在则不通告
＜metric-value＞|指定缺省路由的费用，缺省为1，范围：0–16777214
ext-2|设置路由链路状态通告的类型为ext-2
ext-1|设置路由链路状态通告的类型为ext-1
＜map-tag＞|产生该缺省路由的路由映射名称，长度1–31个字符






No参数|描述
---|---
metric|清除缺省路由的花费
metric-type|清除缺省路由的花费类型
route-map|清除缺省路由的映射表








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#notify default route always metric 20 metric-typeext-1 route-map map





相关命令 :

无 




## nsf 


nsf 




命令功能 :

配置无中断转发（Non-stop Forwarding）能力, 用no命令表示不支持。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



nsf 
 

no nsf 








命令参数解释 :


					无
				 






缺省 :

不支持无中断转发能力。 






使用说明 :

使用前必须确保所运行的OSPF实例支持不透明链路状态通告（Opaque LSA）。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#nsf





相关命令 :

无 




## nssa 


nssa 




命令功能 :

定义一个区域为NSSA区域。使用no命令将该NSSA区域定义为非NSSA区域。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


nssa 
  [{[default-information-originate 
 [metric 
 ＜metric-value 
＞] [metric-type 
 {ext-2 
|ext-1 
}]],[translator-role 
 {candidate 
|always 
}],[translator-stab-intv 
 ＜stab-intv 
＞],[no-summary 
],[no-redistribution 
],[trans-type7-suppress-fa 
]}]
no nssa 
  [{[default-information-originate 
 [metric 
] [metric-type 
]],[no-redistribution 
],[no-summary 
],[translator-role 
],[translator-stab-intv 
],[trans-type7-suppress-fa 
]}]
				






命令参数解释 :



参数|描述
---|---
default-information-originate|产生7型缺省路由链路状态通告
＜metric-value＞|7型缺省路由链路状态通告的费用值，取值为一个24位数，范围0~16777214
ext-2|设置路由链路状态通告的类型为ext-2
ext-1|设置路由链路状态通告的类型为ext-1
candidate|设置翻译角色为candidate
always|设置翻译角色为always
＜stab-intv＞|失去翻译资格后继续保持翻译角色的时间长度
no-summary|不向该NSSA区域发送汇总链路状态通告
no-redistribution|不向该NSSA区域再分配NSSA链路状态通告
trans-type7-suppress-fa|在7型转5型时抑制转发地址






No参数|描述
---|---
metric|清除7型LSA的花费
metric-type|清除7型LSA的花费值类型
translator-role|清除NSSA翻译角色
translator-stab-intv|失去翻译资格后继续保持翻译角色的时间长度








缺省 :

没有定义NSSA区域。对NSSA区域来说，如果产生了7型缺省通告，则缺省费用值为1，类型为ext-2。






使用说明 :

1. 区域0，stub区域，有虚链的区域不能配置成为nssa区域；一台路由器上可以同时配置多个nssa区域。2. 可以同时指定是否需要禁止ABR将汇总路由信息发送到该NSSA区域，是否向NSSA区域导入7型外部链路状态通告，以及是否产生7型缺省链路状态通告。缺省为：不禁止汇总路由，导入7型路由，不产生缺省7型路由。3. 如果该区域不存在则自动创建。






范例 :

配置OSPF实例1区域1为NSSA区域，并产生7型缺省路由链路状态通告。R1(config)#router ospf 1R1(config-ospf-1)#area 1R1(config-ospf-1-area-1)#nssa default-information-originate






相关命令 :

无 




## passive-interface 


passive-interface 




命令功能 :

将一个接口配置为被动的接口, 使得该接口不能发送hello包，并且不会接受任何报文，不能和其他的路由器建立邻居及邻接的关系。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


passive-interface 
  {default 
|＜interface-name 
＞ [disable 
]}
no passive-interface 
  {default 
|＜interface-name 
＞}
				






命令参数解释 :



参数|描述
---|---
default|默认，即将所有的接口都配置成为passive-interface接口
＜interface-name＞|接口名称
disable|将某个接口的被动属性取消








缺省 :

所有的接口都是一般的接口，可以正常的收发OSPF协议包，建立邻居。 






使用说明 :

1. passive-interface default表示将所有的接口都默认为被动的接口。2. passive-interface interface表示将某个接口设置为被动的接口。3. passive-interface interface disable表示将某个接口的被动属性取消。






范例 :

ZXROSNG(config-ospf-1)#passive-interface default  






相关命令 :

无 




## prefix-priority 


prefix-priority 




命令功能 :

配置OSPF的前缀优先级收敛命令，使匹配命令的LSA优先得到计算 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


prefix-priority 
  {critical 
|high 
|medium 
} {prefix-name 
 ＜prefix-name 
＞|tag 
 ＜tag-number 
＞}
no prefix-priority 
  {critical 
|high 
|medium 
} {prefix-name 
|tag 
 ＜tag-number 
＞}
				






命令参数解释 :



参数|描述
---|---
critical|配置critical级别的优先级配置critical级别的优先级
high|配置high级别的优先级配置high级别的优先级
medium|配置medium级别的优先级配置medium级别的优先级
＜prefix-name＞|匹配的prefix-list的名称，长度为1-31个字符
tag|匹配tag匹配tag
＜tag-number＞|匹配的tag值，范围为1-4294967295匹配的tag值，范围为1-4294967295






No参数|描述
---|---
prefix-name|策略名








缺省 :

缺省条件下默认没有配置prefix-priority命令 






使用说明 :

1.每个优先级只能配置一个带prefix-name的命令，继续配置新的带prefix-name的命令会覆盖之前的配置。每个优先级最多可以配置20个带tag的命令。2. no命令是只针对已配置的prefix-priority命令的反操作，如果不存在相应prefix-priority命令，则no命令无效。如果是no带prefix-name的命令，则不需要带prefix-list的名称；如果是no到tag的命令，则需要带tag的数值大小。





范例 :

1配置一个critical优先级的匹配prefix-list的命令，其prefix-list名称为zxr10ZXROSNG(config-ospf-1)# prefix-priority critical prefix-name zxr102配置一个匹配critical优先级的匹配tag的命令，tag的值为1ZXROSNG(config-ospf-1)#prefix-priority critical tag 13 no掉critical优先级的匹配prefix-list的命令ZXROSNG(config-ospf-1)# no prefix-priority critical prefix-name4 no掉匹配critical优先级的匹配tag的值为1的命令ZXROSNG(config-ospf-1)#no prefix-priority critical tag 1





相关命令 :

无 




## priority 


priority 




命令功能 :

设置接口优先级。使用no命令使接口优先级恢复到缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



priority 
  ＜priority 
＞

no priority 








命令参数解释 :



参数|描述
---|---
＜priority＞|接口优先级，缺省为1，范围：0–255








缺省 :

缺省值1 






使用说明 :

接口优先级设置为0的时候，该路由器不能作为DR和BDR。 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#priority 10 





相关命令 :

无 




## priority 


priority 




命令功能 :

设置接口优先级。使用no命令使接口优先级恢复到缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



priority 
  ＜priority 
＞

no priority 








命令参数解释 :



参数|描述
---|---
＜priority＞|接口优先级，缺省为1，范围：0–255








缺省 :

缺省值1 






使用说明 :

接口优先级设置为0的时候，该路由器不能作为DR和BDR。 






范例 :

[89\9900]1. 配置接口的优先级为10：ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#interface vlan1ZXR10 (config-ospfv2-if)#priority 10[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#priority 10[ZSR]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-1/1ZXR10 (config-ospf-1-if-gei-1/1)#priority 10





相关命令 :

无 




## range 


range 




命令功能 :

配置区域内的汇总地址范围，如果该区域不存在则需要创建。使用no命令使配置的汇总地址范围失效。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


range 
  ＜ip-address 
＞ ＜net-mask 
＞ {summary-link 
 [{[{advertise 
|not-advertise 
}],[cost 
 ＜cost-value 
＞]}]|nssa-external-link 
 [{[{advertise 
|not-advertise 
}],[tag 
 ＜tag-value 
＞],[cost 
 ＜cost-value 
＞]}]}
no range 
  ＜ip-address 
＞ ＜net-mask 
＞ {summary-link 
 [cost 
]|nssa-external-link 
 [{[tag 
],[cost 
]}]}
				






命令参数解释 :



参数|描述
---|---
＜ip-address＞|汇总地址范围的IP地址，为十进制点分形式
＜net-mask＞|汇总地址范围的掩码，为十进制点分形式
summary-link|汇总type-3链路状态
advertise|通告汇总的LSA
not-advertise|禁止通告汇总的LSA，在其他区域中不会收到关于此网段的路由信息
＜cost-value＞|设置汇总lsa的绝对cost，范围0~16777214
nssa-external-link|汇总type-7链路状态
advertise|通告汇总的LSA
not-advertise|禁止通告汇总的LSA，在其他区域中不会收到关于此网段的路由信息
＜tag-value＞|设置汇总lsa的tag，范围0~4294967295
＜cost-value＞|设置汇总lsa的绝对cost，范围0~16777214






No参数|描述
---|---
cost|清除5型汇总lsa的绝对cost
tag|清除汇总lsa的tag
cost|清除5型汇总lsa的绝对cost








缺省 :

没有指定区域的汇总地址范围。 






使用说明 :

1. 此命令只能用在域边界路由器上，它用作对一个区域进行合并计算和汇总路由，其结果是一个概要路由被域边界路由器（ABR）通告到其他区域，路由选择信息在  区域边界被压缩。2. type-3汇总的对象是1型或者2型LSA对应的路由，其他的路由不能汇总。3. type-7汇总的对象是7型LSA对应的路由，其它的路由不能汇总。4. 如果该区域不存在则自动创建。






范例 :

ZXROSNG(config-ospf-1)#area 1ZXROSNG(config-ospf-1-area-1)#range 10.0.0.0 255.0.0.0 summary-link






相关命令 :

无 




redistribute :

redistribute 




命令功能 :

控制其他协议符合条件的路由导入OSPF自治系统中，使用该命令后路由器成为一个ASBR。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


redistribute 
  {sl-nat64-ipv4 
|dyn-leasedline 
|user-special 
|nat 
|natpt 
|subscriber-host 
|subscriber-aggregation 
|static 
|connected 
|rip 
|{ospf-int 
|ospf-ext 
} ＜process-id 
＞|{isis-1 
|isis-2 
|isis-1-2 
} [＜process-id 
＞]|{bgp-ext 
|bgp-int 
} [{[as 
 <1-65535>/<1-65535>.<0-65535> 
],[peer 
 ＜peer-address 
＞]}]|ps-busi-addr 
|ps-user-addr 
|zenic-local 
|nat-mask 
|bras-pool 
|ipsec 
} [{[with-originate-metric 
],[tag 
 ＜tag-value 
＞],[metric 
 ＜metric-value 
＞],[metric-type 
 {ext-2 
|ext-1 
}],[route-map 
 ＜map-tag 
＞],[host-only 
]}]
no redistribute 
  {sl-nat64-ipv4 
|dyn-leasedline 
|user-special 
|nat 
|natpt 
|subscriber-host 
|subscriber-aggregation 
|static 
|connected 
|rip 
|{ospf-int 
|ospf-ext 
} ＜process-id 
＞|{isis-1 
|isis-2 
|isis-1-2 
} [＜process-id 
＞]|{bgp-ext 
|bgp-int 
} [{[as 
],[peer 
]}]|ps-busi-addr 
|ps-user-addr 
|zenic-local 
|nat-mask 
|bras-pool 
|ipsec 
} [{[with-originate-metric 
],[tag 
],[metric 
],[metric-type 
],[route-map 
],[host-only 
]}]
				






命令参数解释 :



参数|描述
---|---
sl-nat64-ipv4|重分发sl-nat64-ipv4路由
dyn-leasedline|重分发Dynamic-leased-line路由
user-special|重分发用户特殊路由
nat|重分发NAT路由
natpt|重分发Port-addrees Translation路由
subscriber-host|重分发Bras subscriber's host路由
subscriber-aggregation|重分发Bras subscriber's aggregation路由
static|重分发静态路由
connected|重分发直连路由
rip|重分发rip路由
ospf-int|重分发内部OSPF路由
ospf-ext|重分发外部OSPF路由
＜process-id＞|ISIS进程号，取值范围0-65535
isis-1|重分发IS-IS level-1路由
isis-2|重分发IS-IS level-2路由
isis-1-2|重分发IS-IS level-1和IS-IS level-2路由
＜process-id＞|ISIS进程号，取值范围0-65535
bgp-ext|重分发外部BGP路由
bgp-int|重分发内部BGP路由
<1-65535>/<1-65535>.<0-65535>|BGP的AS号
＜peer-address＞|重分发BGP外部路由的对端的ip地址
ps-busi-addr|重分发Ps-busi-addr路由
ps-user-addr|重分发Ps-user-addr路由
zenic-local|重分发zenic-local路由
nat-mask|重分发nat-mask路由
bras-pool|重分发BRAS-pool路由
ipsec|IPsec路由
with-originate-metric|使用初始花费
tag|设置再分配后的LSA的tag，范围：0–4294967295
＜tag-value＞|设置再分配后的LSA的tag，范围：0–4294967295
＜metric-value＞|设置再分配后的LSA的metric-type，取值为ext-1或ext-2，缺省为ext-2
ext-2|设置路由链路状态通告的类型为ext-2
ext-1|设置路由链路状态通告的类型为ext-1
＜map-tag＞|设置当前协议再分配的路由映射名称，长度1–31个字符
host-only|重分发host-only路由






No参数|描述
---|---
as|当<protocol-value> 为bgp-ext时可以有两个附加的条件：<as-number>和<peer-address>，<as-number>表示对端AS号。取值为<1-65535>或者<1-65535>.<0-65535>
peer|重分发BGP外部路由的对端的ip地址
metric|重分配后的LSA的metric
metric-type|重分配后的LSA的metric-type
route-map|当前协议再分配的路由映射名称








缺省 :

其他协议的路由不导入OSPF自治系统。缺省metric在再分配BGP路由时为1，其他路由时为20。






使用说明 :

1. no redistribute <protocol>去除对该协议的路由的再分配。2. no redistribute <protocol> tag恢复该协议路由再分配的5型LSA的TAG缺省值。3. no redistribute <protocol> metric恢复该协议路由再分配的5型LSA的metric缺省值。4. no redistribute <protocol> metric type恢复该协议路由再分配的5型LSA的metric-type缺省值。5. no redistribute <protocol> route-map取消对该协议路由再分配进行路由映射的控制。6. 在redistribute isis时，如果已进行了isisi-1-2的重分配，再进行isis-1或isis-2的重分配，则该次的redistribute isis-1或redistribute isis-2不起任何作用，除非能保证重分配后isis-1与isis-2的所有选项值都一致，否则不建议使用命令redistribute isis-1-2。7. 如果在进行isis-1-2重分配之前已进行了isis-1或isis-2的重分配，则以前的isis-1或isis-2的重分配将不再起作用，而是按照isis-1-2模板进行新的重分配。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#redistribute bgp-int tag 1 route-map mapZXR10 (config-ospf-1)#no redistribute bgp-int route-map map





相关命令 :

无 




## resync-timeout 


resync-timeout 




命令功能 :

等待邻居重新同步的时间间隔。使用no命令使该时间间隔恢复到缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



resync-timeout 
  ＜seconds 
＞

no resync-timeout 








命令参数解释 :



参数|描述
---|---
＜seconds＞|等待邻居重新同步的时间间隔，缺省为40秒，范围：1–3600，单位：秒








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#resync-timeout 100





相关命令 :

无 




## resync-timeout 


resync-timeout 




命令功能 :

等待邻居重新同步的时间间隔。使用no命令使该时间间隔恢复到缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



resync-timeout 
  ＜seconds 
＞

no resync-timeout 








命令参数解释 :



参数|描述
---|---
＜seconds＞|等待邻居重新同步的时间间隔，缺省为40秒，范围：1–3600，单位：秒








缺省 :

[M6000\M6000-S\ZSR]无[89\9900]缺省值40s





使用说明 :

无 






范例 :

[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#resync-timeout 100[ZSR]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-1/1ZXR10 (config-ospf-1-if-gei-1/1)#resync-timeout 100[89\9900]1. 配置接口vlan1的resync-timeout为100秒：ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#interface vlan1ZXR10 (config-ospfv2-if)#resync-timeout 100





相关命令 :

无 




## retransmit-interval 


retransmit-interval 




命令功能 :

指定接口重传LSA的时间间隔。使用no命令使接口重传LSA的时间间隔恢复到缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



retransmit-interval 
  ＜seconds 
＞

no retransmit-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口重传LSA的时间间隔，缺省为5秒，范围：1–65535，单位：秒








缺省 :

缺省值为5s 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#retransmit-interval 10





相关命令 :

无 




## retransmit-interval 


retransmit-interval 




命令功能 :

指定接口重传LSA的时间间隔。使用no命令使接口重传LSA的时间间隔恢复到缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



retransmit-interval 
  ＜seconds 
＞

no retransmit-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口重传LSA的时间间隔，缺省为5秒，范围：1–65535，单位：秒








缺省 :

[89\9900]缺省值5s[M6000\M6000-S\ZSR]缺省值为5s





使用说明 :

无 






范例 :

[89\9900]1. 配置接口重传LSA的时间间隔为10秒：ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#interface vlan1ZXR10 (config-ospfv2-if)#retransmit-interval 10[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#retransmit-interval 10[ZSR]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-1/1ZXR10 (config-ospf-1-if-gei-1/1)#retransmit-interval 10





相关命令 :

无 




## retransmit-interval 


retransmit-interval 




命令功能 :

指定接口重传LSA的时间间隔。使用no命令使接口重传LSA的时间间隔恢复到缺省值。





命令模式 :

 IPv4-OSPF-MULTI-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :


retransmit-interval 
  ＜seconds 
＞

no retransmit-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口重传LSA的时间间隔，缺省为5秒，范围：1–65535，单位：秒








缺省 :

5 






使用说明 :

使用场景在使用多区域接口建链时，如果想要手动指定重传时间间隔，则应配置此命令。






范例 :

配置IPv4 OSPF实例1的区域100下添加fei-0/1/0/1多区域接口，配置多区域接口fei-0/1/0/1接口重传LSA的时间间隔为120秒。R1(config)#router ospf 1R1(config-ospf-1)#area 100R1(config-ospf-1-area-100)#multi-area-interface fei-0/1/0/1R1(config-ospf-1-area-100-mif-fei-0/1/0/1)# retransmit-interval 120






相关命令 :

无 




## router ospf 


router ospf 




命令功能 :

如果尚未启动OSPF协议则启动OSPF协议，然后进入OSPF协议配置模式。使用no命令取消指定进程号的OSPF协议进程。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


router ospf 
  ＜process-id 
＞ [{[vrf 
 ＜vrf-name 
＞],[router-id 
 ＜router-id 
＞]}]
no router ospf 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围：1–65535
＜vrf-name＞|VRF名称，长度1–32个字符
router-id|OSPF的唯一路由器标识，ip地址格式
＜router-id＞|OSPF的唯一路由器标识，ip地址格式








缺省 :

没有启动OSPF协议。 






使用说明 :

1. 如果已启动OSPF协议，且OSPF协议有效，直接进入OSPF协议配置模式。2. 全局的OSPF及各个VRF下的OSPF使用不同的进程号。3. 当OSPF启动时需要从本地IP地址中分配router-id，如果本地一个地址也没有，则启动失败。






范例 :

ZXROSNG(config)#router ospf 2 vrf vpn1 






相关命令 :

无 




## router-id 


router-id 




命令功能 :

指定一个OSPF进程的路由器标识。使用no命令删除指定的路由器标识。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



router-id 
  ＜router-id 
＞

no router-id 








命令参数解释 :



参数|描述
---|---
＜router-id＞|IP地址形式的OSPF路由器标识








缺省 :

OSPF进程使用自动选取的OSPF路由器标识。 






使用说明 :

1. 配置本命令使该OSPF进程使用指定的IP地址形式的OSPF路由器标识。为了让OSPF进程使用自动选取的OSPF路由器标识，使用本命令的no命令形式。2. 该配置在路由器重启或该OSPF进程手工重启后生效。手工重启OSPF使用clear ip ospf process命令。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#router-id 1.1.1.33





相关命令 :

无 




## segment-routing mpls mapping-server 


segment-routing mpls mapping-server 




命令功能 :

使能segment-routing  mapping-server功能





命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


segment-routing mpls mapping-server 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|使能SRMS(Segment Routing Mapping Server)功能
disable|去使能SRMS(Segment Routing Mapping Server)功能








缺省 :

默认disable 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#segment-routing mpls mapping-server enableZXROSNG(config-ospf-1)#segment-routing mpls mapping-server disable






相关命令 :

无 




## segment-routing mpls 


segment-routing mpls 




命令功能 :

OSPF使能SR功能。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



segment-routing mpls 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能分段路由功能
disable|去使能分段路由功能








缺省 :

该功能是不使能的 






使用说明 :

1.该命令只打开了OSPF的SR使能开关，还需要全局的SR使能了才能真正生效。2.在VRF实例下不能配置。在VRF实例下配置会提示错误






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#segment-routing mpls enable ZXROSNG(config-ospf-1)#segment-routing mpls disable ZXROSNG(config-ospf-1)#






相关命令 :

无 




## sequence-backup 


sequence-backup 




命令功能 :

设置为优雅重启（graceful restart）备份的最近DBD报文的序列号。使用no命令取消配置。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



sequence-backup 
  ＜sequence-number 
＞

no sequence-backup 








命令参数解释 :



参数|描述
---|---
＜sequence-number＞|报文序列号，十进制整数，范围：1-4294967295








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#sequence-backup 256600





相关命令 :

无 




## sham-link 


sham-link 




命令功能 :

在两PE路由器之间，建立通过MPLS VPN来传递OSPF协议包的link。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


sham-link 
  ＜source-address 
＞ ＜destination-address 
＞ [cost 
 ＜cost-value 
＞]
no sham-link 
  ＜source-address 
＞ ＜destination-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜source-address＞|Sham-link建链借用的本地IP地址，必须是32位loopback地址才能生效
＜destination-address＞|Sham-link建链借用的远端IP地址，必须是32位loopback地址才能生效
＜cost-value＞|Sham-link接口代价，缺省为loopback口的cost,取值范围为1-65535








缺省 :

不配置该命令，VPN链路上就没有OSPF sham-link。 






使用说明 :

1．    Sham-link要up，需要同时满足如下5个条件：        Sham-link配置。        Source-address 和destination-address IP地址有对应接口。        Destination-address 有对应BGP路由。        在OSPF的VRF实例下进行配置。        OSPF实例下有重分配BGP命令。2．    Sham-link使用时机：        两PE之间的VPN site在同一OSPF area。        两VPN site有后门链路（私网链路），且也在同一区域。3．    Sham-link借用的loopback接口地址需要绑定对应的VRF。4．    通过改变sham-link cost，可以实现VPN链路和后门链路的任意切换。5．    Sham-link使用的区域应该和VPN site所在的区域一致。6．    该区域不存在会自动创建。7．    绑定sham-link的loopback接口的地址不能用network通告到OSPF中，否则可能会震荡loopback地址的掩码必须是32位的。






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#area 1 ZXR10 (config-ospf-1-area-1)#sham-link 10.22.1.1 10.22.1.2 cost 100





相关命令 :

无 




## show debug ospf 


show debug ospf 




命令功能 :

显示进程调试信息开关情况 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug ospf 
  [＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show debug ospf 1OSPF 1:   OSPF adjacency events debugging is on  OSPF spf external events debugging is on  OSPF spf inter events debugging is on  OSPF spf intra events debugging is on





相关命令 :

无 




## show error packet ospfv2 


show error packet ospfv2 




命令功能 :

OSPFv2显示协议的错误报文信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show error packet ospfv2 
  [{statistics 
 [detail 
]|{[{[process 
 ＜process-id 
＞],[interface 
 ＜interface-name 
＞]}]|[number 
 ＜number 
＞]} [detail 
]}]







命令参数解释 :



参数|描述
---|---
statistics|显示统计信息
detail|是否需要显示具体报文详细信息
＜process-id＞|指定实例查询，范围1-65535
＜interface-name＞|指定接口查询
＜number＞|查询最新异常报文的数目，范围1-200
detail|是否需要显示具体报文详细信息








缺省 :

无 






使用说明 :

1.指定实例或接口的时候不能加上显示数目。 






范例 :

OSPFv2显示协议错误报文统计信息：ZXROSNG(config)# show error packet ospfv2 statisticsPacket Type                 NumberUnknown Type Packet         0Hello                       17Database Description        0Link State Request          0Link State Update           0Link State Acknowledgment   0Total                       17域    描述Hello    Hello错误报文数目Database Description    DD错误报文数目Link State Reques    LSR错误报文数目Link State Update    LSU错误报文数目Link State Acknowledgment    LSA错误报文数目Total    所有错误报文总数OSPFv2显示协议错误报文详细的统计信息：ZXROSNG#show error packet ospfv2 statistics detail   Hello:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Bad option:                      0    DR or BDR error:                 0    Hello interval mismatch:         0    Dead interval mismatch:          0    Total                            0  Database Description:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Local MRU mismatch neighbor MTU: 0    Bad option:                      0    Total                            0  Link State Request:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Total                            0  Link State Update:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Total                            0  Link State Acknowledgment:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Total                            0域    描述Bad checksum: 验证码不对，报文里携带的checksum和计算出的不一致Bad authentication type: 报文里携带的认证类型和收报接口的认证类型不匹配Bad authentication key： 认证的key不匹配  Bad authentication sequence：认证的seq不正确，比如没有递增Bad digest:报文里携带的摘要和本地根据报文计算出的不一致VPN ID mismatch:socket报文解析出的vpn id和本地收报接口所在的vpn id不一致Bad TTL:解析出来的TTL错误Bad packet length:：报文长度不对，比如ospf的报文长度大于ip的报文长度，比如小于报文的最小长度等等Bad router id:报文里携带的router id不对，比如为0，比如和收报接口所在实例的router id一致Local interface invalid：收报接口异常，比如找不到，比如接口状态是down，比如是passiveNeighbor invalid:邻居不对，比如邻居状态是downBad source address:报文发送的源地址有错误Bad dest address:收报的目的地址有错误Area mismatch:报文发送端和接收端区域不一致Bad version:    报文里携带的version字段不对Local MRU mismatch neighbor MTU:DD报文本地的MRU小于报文里携带的MTU Bad option:  DD报文和HELLO报文中携带的option字段与本地检查冲突，比如携带了Nbit，但是本地接口不在nssa区域    DR or BDR error:  hello报文中携带的dr，bdr信息异常    Hello interval mismatch:        hello报文中携带的hello interval和收报接口不一致    Dead interval mismatch:         hello报文中携带的dead inteval和收报接口的不一致OSPFv2显示实例1的协议错误报文详细信息：ZXROSNG(config)# show error packet ospfv2 process 1 detailPacket index  : 17Record time   : 2016-05-19 14:36:18Process ID    : 1Area ID       : 255.0.0.0Interface     : gei-0/1/0/1PDU type      : HelloError reason  : Bad Hello Interval expected:6, received:10Packet length : 440x00000000: 02 01 00 2c 01 00 00 02 ff 00 00 00 fc 9b 00 000x00000010: 00 00 00 00 00 00 00 00 ff ff ff 00 00 0a 02 010x00000020: 00 00 00 28 00 00 00 00 00 00 00 00域    描述Packet index      错误报文记录索引Record time     错误报文记录时间Process ID    错误报文接收所在实例Area ID      错误报文接收所在区域Interface    错误报文接收接口PDU type    错误报文类型Error reason    错误报文原因Packet length    错误报文长度0x000000000x00000010..    错误报文内容





相关命令 :

无 




## show ip ospf border-lfas 


show ip ospf border-lfas 




命令功能 :

显示替代快速重计算路由的非自环路由信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip ospf border-lfas 
  [{[router-id 
 ＜router-id 
＞],[process 
 ＜process-id 
＞]}] 







命令参数解释 :



参数|描述
---|---
＜router-id＞|路由器ID，为十进制点分形式的IP地址
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXR10>show ip ospf border-lfas process 1Protect Type: link-protect   0x80000001, ecmp-protect   0x80000004              node-protect   0x80000002, stat-protect   0x80000008                 OSPF Router with ID (10.10.10.1) (Process ID 1)OSPF internal LFA TableDestination     Next Hop        Cost    Type    RteType    Area            ProtectType     Primary NextHop





相关命令 :

无 




## show ip ospf border-routers 


show ip ospf border-routers 




命令功能 :

显示边界路由器的路由信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip ospf border-routers 
  [{[router-id 
 ＜router-id 
＞],[process 
 ＜process-id 
＞]}] 







命令参数解释 :



参数|描述
---|---
＜router-id＞|路由器ID，为十进制点分形式的IP地址
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXR10>show ip ospf border-routers process 1            OSPF Router with ID (10.10.10.1) (Process ID 1)OSPF internal Routing TableDestination     Next Hop        Cost   Type RteType   Area10.10.10.2      10.10.10.2      1      ABR  INTRA     0.0.0.010.10.10.2      12.12.12.2      1      ABR  INTRA     0.0.0.3





相关命令 :

无 




## show ip ospf database asbr-summary 


show ip ospf database asbr-summary 




命令功能 :

只显示自治系统边界路由器汇总链路状态通告 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip ospf database asbr-summary 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ip ospf database asbr-summary           OSPF Router with ID (1.1.1.33) (Process ID 1)           OSPF Router with ID (63.1.1.1) (Process ID 5)               Summary ASB Link States (Area 0.0.0.90) Routing Bit Set on this LSA LS age: 745 Options: (No TOS-capability, DC) LS Type: Summary Links(AS Boundary Router) Link State ID: 99.99.1.1 (AS Boundary Router address) Advertising Router: 1.1.1.35 LS Seq Number: 0x80000004 Checksum: 0xf257 Length: 28 Network Mask: /0       TOS: 0  Metric: 2 Routing Bit Set on this LSA LS age: 1453 Options: (No TOS-capability, DC) LS Type: Summary Links(AS Boundary Router) Link State ID: 1.1.1.33 (AS Boundary Router address) Advertising Router: 1.1.1.35 LS Seq Number: 0x80000002 Checksum: 0x47aa Length: 28 Network Mask: /0       TOS: 0  Metric: 1





相关命令 :

无 




## show ip ospf database database-summary 


show ip ospf database database-summary 




命令功能 :

显示每个区域每种链路状态通告的数目和整个数据库的链路状态通告总数 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database database-summary 
  [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf database database-summary           OSPF Router with ID (110.1.1.1) (Process ID 1)Area 0.0.0.0 database summary LSA Type       Count Router          2 Network         1 Summary Net     1 Summary ASBR    0 Type-7 Ext      0 Opaque Link     0 Opaque Area     0 Subtotal        4 Process 11 database summary LSA Type       Count Router          2 Network         1 Summary Net     1 Summary ASBR    0 Type-7 Ext      0 Opaque Link     0 Opaque Area     0 Type-5 Ext      0 Opaque AS            0 Total           4





相关命令 :

无 




## show ip ospf database external 


show ip ospf database external 




命令功能 :

只显示5型外部链路状态通告 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database external 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ip ospf database external           OSPF Router with ID (1.1.1.33) (Process ID 1)               Type-5 AS External Link States LS age: 1726 Options: (No TOS-capability, No DC, Upward) LS Type: AS External Link Link State ID: 20.31.95.0 (External Network Number) Advertising Router: 192.0.0.1 LS Seq Number: 0x80000003 Checksum: 0x5f6 Length: 36 Network Mask: /24       Metric Type: 1 (Comparable directly to link state metric)       TOS: 0       Metric: 1       Forward Address: 0.0.0.0       External Route Tag: 0





相关命令 :

无 




## show ip ospf database network 


show ip ospf database network 




命令功能 :

只显示网络链路状态通告 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database network 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ip ospf database network           OSPF Router with ID (1.1.1.33) (Process ID 1)               Net Link States (Area 0.0.0.10) Routing Bit Set on this LSA LS age: 1777 Options: (No TOS-capability, DC) LS Type: Network Links Link State ID: 72.1.1.53 (Address of Designated Router) Advertising Router: 10.10.10.53 LS Seq Number: 0x80000061 Checksum: 0xb84 Length: 32 Network Mask: /24       Attached Router: 10.10.10.53       Attached Router: 1.1.1.35





相关命令 :

无 




## show ip ospf database nssa 


show ip ospf database nssa 




命令功能 :

只显示7型外部链路状态通告 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database nssa 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-ospf-1)#show ip ospf database nssa             OSPF Router with ID (1.1.1.1) (Process ID 1)                Type-7 AS External Link States (Area 0.0.0.2)  LS age: 163  Options: (No TOS-capability, No Type 7/5 translation,   DC, Upward)  LS Type: AS External Link  Link State ID: 0.0.0.0 (External Network Number)  Advertising Router: 1.1.1.1  LS Seq Number: 0x80000002  Checksum: 0xecbf  Length: 36  Network Mask: /0        Metric Type: 2 (Larger than any link state path)        TOS: 0        Metric: 1        Forward Address: 0.0.0.0        External Route Tag: 0
  LS age: 28  Options: (No TOS-capability, No Type 7/5 translation,   DC, Upward)  LS Type: AS External Link  Link State ID: 0.0.0.0 (External Network Number)  Advertising Router: 2.2.2.2  LS Seq Number: 0x80000002  Checksum: 0xced9  Length: 36  Network Mask: /0        Metric Type: 2 (Larger than any link state path)        TOS: 0        Metric: 1        Forward Address: 0.0.0.0        External Route Tag: 0






相关命令 :

无 




## show ip ospf database opaque-area 


show ip ospf database opaque-area 




命令功能 :

只显示区域不透明链路状态通告 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database opaque-area 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf d opaque-area self-originate                      OSPF Router with ID (100.1.1.1) (Process ID 1)                      Type-10 Opaque Link Area Link States  (Area 0.0.0.1)LS age: 851  Options: (No TOS-capability, DC)  LS Type: Opaque Area Link  Link State ID: 1.0.0.0  Opaque Type: 1  Opaque ID: 0  Advertising Router: 0.0.0.1  LS Seq Number: 0x80000001  Checksum: 0x70bc  Length: 28  Fragment number: 0    MPLS TE router ID : 1.1.1.1    Number of Links : 0  LS age: 308  Options: (No TOS-capability, DC)  LS Type: Opaque Area Link  Link State ID: 1.0.0.6  Opaque Type: 1  Opaque ID: 6  Advertising Router: 0.0.0.1  LS Seq Number: 0x80000001  Checksum: 0x36de  Length: 124  Fragment number: 6    Link connected to Point-to-point network      Link ID : 0.0.0.2      Interface Address : 10.0.0.1      Neighbor Interface Address : 10.0.0.2      Admin Metric : 1      Maximum bandwidth : 125000000      Maximum reservable bandwidth : 0      Number of Priority : 8      Priority 0 : 0         Priority 1 : 0               Priority 2 : 0         Priority 3 : 0               Priority 4 : 0         Priority 5 : 0               Priority 6 : 0         Priority 7 : 0               Affinity Bit : 0x0    Number of Links : 1  LS age: 14  Options: (No TOS-capability, DC)  LS Type: Opaque Area Link  Link State ID: 1.0.0.6  Opaque Type: 1  Opaque ID: 6  Advertising Router: 0.0.0.1  LS Seq Number: 0x80000001  Checksum: 0x3ed8  Length: 124  Fragment number: 6             Link connected to Broadcast network      Link ID : 10.0.0.1      Interface Address : 10.0.0.1      Neighbor Interface Address : 0.0.0.0      Admin Metric : 1      Maximum bandwidth : 125000000      Maximum reservable bandwidth : 0      Number of Priority : 8      Priority 0 : 0         Priority 1 : 0               Priority 2 : 0         Priority 3 : 0               Priority 4 : 0         Priority 5 : 0               Priority 6 : 0         Priority 7 : 0               Affinity Bit : 0x0    Number of Links : 1  LS age: 1684  Options: (No TOS-capability, DC)  LS Type: Opaque Area Link  Link State ID: 4.0.0.0  Opaque Type: 4  Opaque ID: 0  Advertising Router: 100.1.1.1  LS Seq Number: 0x80000030  Checksum: 0xcb34  Length: 44  Fragment number: 0    Segment Routing Algorithm TLV: Length: 1      Algorithm: 0    Segment Routing Range TLV: Length: 12      Range Size: 65536      SID sub-TLV: Length: 4       SID: 900000  LS age: 1684  Options: (No TOS-capability, DC)  LS Type: Opaque Area Link  Link State ID: 7.0.0.25  Opaque Type: 7  Opaque ID: 25  Advertising Router: 100.1.1.1  LS Seq Number: 0x80000030  Checksum: 0xd5de  Length: 44  Fragment number: 25    Extended Prefix TLV: Length: 20      Route Type: 1      AF        : 0      Flags     : 0x0      Prefix    : 101.1.1.1/32      SID sub-TLV: Length: 8        Flags     : 0x0        MTID      : 0        Algo      : 0        SID Index : 20          LS age: 135  Options: (No TOS-capability, DC)  LS Type: Opaque Area Link  Link State ID: 8.0.0.6  Opaque Type: 8  Opaque ID: 6  Advertising Router: 123.0.0.1  LS Seq Number: 80000001  Checksum: 0x55e1  Length: 68    Extended Link TLV: Length: 24      Link Type : Point-to-point      Link ID   : 100.1.1.1      Link Data : 80.0.0.1      Adj sub-TLV: Length: 7        Flags     : 0xe0        MTID      : 0        Weight    : 0        Label     : 24000  LS age: 135  Options: (No TOS-capability, DC)  LS Type: Opaque Area Link  Link State ID: 8.0.0.6  Opaque Type: 8  Opaque ID: 6  Advertising Router: 123.0.0.1  LS Seq Number: 80000001  Checksum: 0x55e1  Length: 68    Extended Link TLV: Length: 28      Link Type : Broadcast      Link ID   : 100.1.1.1      Link Data : 80.0.0.1      LAN Adj sub-TLV: Length: 11        Flags     : 0xe0        MTID      : 0        Weight    : 0        Neighbor ID: 1.1.1.1        Label     : 24000域信息说明LS age:LSA的年龄Options: LSA的选项LS Type: LSA的类型Link State ID: LSA的链路状态IDOpaque Type: Opaque类型Opaque ID: Opaque IDAdvertising Router: 通告路由器LS Seq Number: 序列号Checksum: 校验和Length: LSA的长度Fragment number: Opaque IDSegment Routing Algorithm TLV: 表示这是一个SR 算法tlvLength: tlv的长度Algorithm: 算法Segment Routing Range TLV: 表示这是一个SR range tlvRange Size: tlv中的range sizeSID sub-TLV: 表示这是一个SID子tlvSID: SID起始值Label: tlv中携带的标签
Extended Prefix TLV: 表示这是一个Extended Prefix TLVRoute Type:tlv中携带的路由类型AF: tlv中携带的地址族信息Flags: tlv中携带的标记位Prefix: tlv中携带的前缀信息SID sub-TLV: 表示这是一个prefix SID子tlvFlags: tlv中携带的标记位MTID: tlv中携带的MTIDAlgo: tlv中携带的算法SID Index: tlv中携带的SID索引Label: tlv中携带的标签
Extended Link TLV: 表示这是一个Extended Link TLVLink Type: link类型Link ID: link IDLink Data: Link DataAdj sub-TLV: 表示这是一个Adj sub-TLVFlags: tlv中携带的标记位MTID: tlv中携带的MTIDWeight: tlv中携带的权重SID Index: tlv中携带的SID索引Label: tlv中携带的标签
LAN Adj sub-TLV:: 表示这是一个LAN Adj sub-TLVFlags: tlv中携带的标记位MTID: tlv中携带的MTIDWeight: tlv中携带的权重Neighbor ID: tlv中携带的邻居IDSID Index: tlv中携带的SID索引Label: tlv中携带的标签






相关命令 :

无 




## show ip ospf database opaque-as 


show ip ospf database opaque-as 




命令功能 :

显示11型Opaque LSA的详细信息 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database opaque-as 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf database opaque-as                      OSPF Router with ID (0.0.0.1) (Process ID 1)                            Type-11 Opaque As Link States  LS age: 395  Options: (No TOS-capability, DC)  LS Type: Opaque As  Link State ID: 7.239.255.255  Opaque Type: 7  Opaque ID: 15728639  Advertising Router: 0.0.0.2  LS Seq Number: 0x80000007  Checksum: 0x307d  Length: 44  Fragment number: 15728639    Extended Prefix TLV: Length: 20      Route Type: 5      AF        : 0      Flags     : 0x0      Prefix    : 1.2.3.4/32      SID sub-TLV: Length: 8        Flags     : 0x40        MTID      : 0        Algo      : 0        SID Index : 1000






相关命令 :

无 




## show ip ospf database opaque-link 


show ip ospf database opaque-link 




命令功能 :

只显示本地不透明链路状态通告 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database opaque-link 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf database opaque-link           OSPF Router with ID (5.5.5.45) (Process ID 45)               Type-9 Opaque Link-local Link States (Area 0.0.0.0) LS age: 1269 Options: (No TOS-capability,No DC) LS Type: Opaque Link-local Link State ID: 3.0.0.0 Opaque Type: 3 Opaque ID: 0 Advertising Router: 5.5.5.46 LS Seq Number: 80000001 Checksum: 0x6b4c Length: 44 Fragment number: 0   Grace period: 1000    NSF reason: switch to redundant control processor     Interface ip addr: 201.46.45.0





相关命令 :

无 




## show ip ospf database router 


show ip ospf database router 




命令功能 :

只显示路由器链路状态通告 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database router 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf database router          OSPF Router with ID (192.168.1.1) (Process ID 1)                Router Link States (Area 0.0.0.1)  Routing Bit Set on this LSA  LS age: 94  Options: (No TOS-capability, DC)  LS Type: Router Links  Link State ID: 192.168.1.1  Advertising Router: 192.168.1.1  LS Seq Number: 0x80000023  Checksum: 0x626c  Length: 36  Number of Links: 1    Link connected to: a Stub Network     (Link ID) Network/subnet number: 192.168.1.1     (Link Data) Network Mask: 255.255.255.255      Number of TOS metrics: 0       TOS 0 Metrics: 0





相关命令 :

无 




## show ip ospf database summary 


show ip ospf database summary 




命令功能 :

只显示网络汇总链路状态通告 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf database summary 
  [＜link-state-id 
＞] {adv-router 
 ＜router-id 
＞|[self-originate 
]} [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜link-state-id＞|链路状态通告包含的网络环境的一部分，它的值的含义与链路状态类型有关。当链路状态通告描述一个网络时，<link-state-id>以采取以下两种形式：1. 网络地址 2. 从网络地址取得的一个详细地址，该地址和网络掩码的与等于网络地址 当链路状态通告描述一个路由器时，<link-state-id>总是为该路有器的Router ID， 当一个自治系统外部链路状态通告描述一跳缺省路由时，它的<link-state-id>为0.0.0.0
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf database summary          OSPF Router with ID (192.168.1.1) (Process ID 1)                Summary Net Link States (Area 0.0.0.0)                  Routing Bit Set on this LSA  LS age: 70  Options: (No TOS-capability, DC, Upward)  LS Type: Summary Links(Network)  Link State ID: 192.168.1.0 (Summary Network Number)  Advertising Router: 10.0.0.2  LS Seq Number: 0x80000001  Checksum: 0x8e39  Length: 28  Network Mask: /24        TOS: 0  Metric: 1





相关命令 :

无 




## show ip ospf database 


show ip ospf database 




命令功能 :

显示特定路由器OSPF数据库相关信息列表，该命令的不同形式显示不同集合的链路状态通告。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip ospf database 
  {adv-router 
 ＜router-id 
＞|[self-originate 
]} [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜router-id＞|路由器ID，为十进制点分形式的IP地址
self-originate|自己生成的链路状态通告
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf database             OSPF Router with ID (10.10.10.2) (Process ID 1)                Router Link States (Area 0.0.0.0)Link ID         ADV Router      Age     Seq#         Checksum   Link count10.10.10.1      10.10.10.1      1222    0x80000004   0xfab6     110.10.10.2      10.10.10.2      1229    0x80000003   0xfab4     1                Net Link States (Area 0.0.0.0)Link ID         ADV Router      Age     Seq#         Checksum10.10.10.2      10.10.10.2      1229    0x80000001   0xbffc                     Summary Net Link States (Area 0.0.0.0)Link ID         ADV Router      Age     Seq#         Checksum11.11.11.0      10.10.10.2      1342    0x80000001   0x27d5     11.11.11.0      10.10.10.1      1270    0x80000001   0x2dd0                     Router Link States (Area 0.0.0.1)Link ID         ADV Router      Age     Seq#         Checksum   Link count10.10.10.1      10.10.10.1      1224    0x80000004   0x3774     110.10.10.2      10.10.10.2      1222    0x80000004   0x3573     1                         Net Link States (Area 0.0.0.1)         Link ID         ADV Router      Age     Seq#         Checksum11.11.11.2      10.10.10.2      1223    0x80000001   0x9b1e                              Summary Net Link States (Area 0.0.0.1)         Link ID         ADV Router      Age     Seq#         Checksum10.10.10.0      10.10.10.2      1345    0x80000001   0x4bb4     10.10.10.0      10.10.10.1      1271    0x80000001   0x51af     ZXROSNG#   





相关命令 :

无 




## show ip ospf interface 


show ip ospf interface 




命令功能 :

显示OSPF接口的信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf interface 
  {[＜interface-name 
＞]|[brief 
]} [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称
brief|OSPF接口列表简要信息
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf interfaceOSPF Router with ID (10.10.10.2) (Process ID 1)gei-0/1/0/1 is upInternet Address 10.10.10.2 255.255.255.0 enableUp for 00:17:39In the area 0.0.0.0 DRCost 1, Priority 1, Network Type broadcastTransmit Delay(sec) 1, Authentication Type nullTimer intervals(sec) : Hello 10, Dead 40, Retransmit 5Designated Router (ID) 10.10.10.2, Interface address 10.10.10.2Backup Designated router (ID) 10.10.10.1, Interface address 10.10.10.1Number of Neighbors 1, Number of Adjacent neighbors 110.10.10.1      BDRgei-0/1/0/2 is upInternet Address 11.11.11.2 255.255.255.0 enableUp for 00:17:37In the area 0.0.0.1 DRCost 1, Priority 1, Network Type broadcastTransmit Delay(sec) 1, Authentication Type nullTimer intervals(sec) : Hello 10, Dead 40, Retransmit 5Designated Router (ID) 10.10.10.2, Interface address 11.11.11.2Backup Designated router (ID) 10.10.10.1, Interface address 11.11.11.1Number of Neighbors 1, Number of Adjacent neighbors 110.10.10.1      BDR2.显示OSPF实例下的接口列表简要信息ZXROSNG(config)#show ip ospf interface brief            OSPF Router with ID (1.1.1.1) (Process ID 1)Area:0.0.0.0Interface         IP Address/Mask     State        Cost   Neighbors(F/T)gei-0/1/0/1       30.1.1.1/24         DR           30    1/1gei-0/1/0/2       40.1.1.1/24         DR           1     0/0Area:0.0.0.1Interface         IP Address/Mask    State         Cost   Neighbors(F/T)gei-0/1/0/3       10.1.1.1/24        DROTHER      30    1/1gei-0/1/0/4       0.1.1.1/24         BDR           1     1/1            OSPF Router with ID (1.1.1.1) (Process ID 2)Area:0.0.0.1Interface          IP Address/Mask     State       Cost    Neighbors(F/T)loopback1          1.1.1.1/32          LOOPBACK  0      0/0   loopback2          1.1.1.1/32          LOOPBACK  0      0/0 域说明：Interface: OSPF接口的名字。IP Address/Mask：OSPF接口的地址和掩码。State：OSPF接口的状态。DR:Designated Router;BDR:Backup Designated Router;DROTHER:DR Other。Cost：OSPF接口的花费值。    Neighbors(F/T)：OSPF接口的邻居数量。F（FULL简称）代表full的邻居数量；T（TOTAL简称）代表总共的邻居数量。






相关命令 :

无 




## show ip ospf mpls 


show ip ospf mpls 




命令功能 :

显示OSPF的流量工程链路信息 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf mpls 
 traffic-eng 
 link 
 [area 
 {＜area-id 
＞|＜area-id 
＞}] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜area-id＞|network命令中指定的与地址范围相联系的区域号
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show  ip ospf mpls traffic-eng link           OSPF Router with ID (1.1.1.33) (Process ID 1) Area 0.0.0.10 has 3 MPLS TE links.   Link is associated with fragment 3     Link connected to Broadcast network     Link ID : 66.1.1.35     Interface Address : 66.1.1.33     Neighbor Interface Address : 0.0.0.0     Admin Metric te: 1 igp: 100     Maximum bandwidth : 12500000     Maximum reservable bandwidth : 9375000     Number of Priority : 8     Priority 0 : 9375000     Priority 1 : 9375000     Priority 2 : 9375000     Priority 3 : 9375000     Priority 4 : 9375000     Priority 5 : 9375000     Priority 6 : 9375000     Priority 7 : 9375000     Affinity Bit : 0x0   Link is associated with fragment 1     Link connected to Broadcast network     Link ID : 72.2.2.1     Interface Address : 72.2.2.33     Neighbor Interface Address : 0.0.0.0     Admin Metric te: 1 igp: 100     Maximum bandwidth : 12500000     Maximum reservable bandwidth : 9375000     Number of Priority : 8     Priority 0 : 9375000     Priority 1 : 9375000     Priority 2 : 9375000     Priority 3 : 9375000     Priority 4 : 9375000     Priority 5 : 9375000     Priority 6 : 9375000     Priority 7 : 9375000     Affinity Bit : 0x0   Link is associated with fragment 2     Link connected to Broadcast network     Link ID : 73.2.2.1     Interface Address : 73.2.2.33     Neighbor Interface Address : 0.0.0.0     Admin Metric te: 1 igp: 100     Maximum bandwidth : 12500000     Maximum reservable bandwidth : 9375000     Number of Priority : 8     Priority 0 : 9375000     Priority 1 : 9375000     Priority 2 : 9375000     Priority 3 : 9375000     Priority 4 : 9375000     Priority 5 : 9375000     Priority 6 : 9375000     Priority 7 : 9375000     Affinity Bit : 0x0           OSPF Router with ID (63.1.1.1) (Process ID 5)





相关命令 :

无 




## show ip ospf neighbor 


show ip ospf neighbor 




命令功能 :

显示OSPF邻居的信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip ospf neighbor 
  {[detail 
] [interface 
 ＜interface-name 
＞] [neighbor-id 
 ＜neighbor-id 
＞]|summary 
|statistics 
|log 
 [interface 
 ＜interface-name 
＞]} [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
detail|以详细格式显示邻居信息
＜interface-name＞|接口名称
＜neighbor-id＞|邻居ID，十进制点分形式的IP地址
summary|统计邻居摘要
statistics|统计邻居数量
log|邻居状态变化日志
＜interface-name＞|接口名称
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

1. 显示OSPF实例1的邻居信息：ZXROSNG#show ip ospf neighbor detailOSPF Router with ID (10.10.10.2) (Process ID 1)Neighbor 10.10.10.1In the area 0.0.0.0Via interface gei-0/1/0/1 10.10.10.1Neighbor is BDRState FULL, Priority 1, Cost 1Queue count : Retransmit 0, DD 0, LS Req 0Dead time : 00:00:39 Options : 0x42In Full State for 00:14:13Neighbor 10.10.10.1In the area 0.0.0.1Via interface gei-0/1/0/2 11.11.11.1Neighbor is BDRState FULL, Priority 1, Cost 1Queue count : Retransmit 0, DD 0, LS Req 0Dead time : 00:00:35 Options : 0x42In Full State for 00:14:062、显示所有实例下的邻居数量：ZXROSNG#show ip ospf neighbor statistics            OSPF Router with ID (0.0.0.1) (Process ID 1)Total: 8000  DOWN: 1000      ATTE: 1000      INIT: 1000      2WAY: 1000EXST: 1000      EXCH: 1000      LOAD: 1000      FULL: 1000            OSPF Router with ID (0.0.0.2) (Process ID 2)Total: 8000  DOWN: 1000      ATTE: 1000      INIT: 1000      2WAY: 1000EXST: 1000      EXCH: 1000      LOAD: 1000      FULL: 10003.显示指定实例下的邻居数量ZXROSNG#show ip ospf neighbor statistics process 1            OSPF Router with ID (0.0.0.1) (Process ID 1)Total: 8000  DOWN: 1000      ATTE: 1000      INIT: 1000      2WAY: 1000EXST: 1000      EXCH: 1000      LOAD: 1000      FULL: 1000域说明：Total: 所有邻居数量之和。DOWN: 处于down状态的邻居数量。ATTE: 处于attempt状态下的邻居数量。INIT: 处于init状态的邻居数量。2WAY：处于2-way状态的邻居数量。EXST: 处于exstart状态的邻居数量.EXCH: 处于exchange状态的邻居数量。LOAD: 处于loading状态的邻居数量。FULL: 处于full状态的邻居数量。






相关命令 :

无 




## show ip ospf nsf 


show ip ospf nsf 




命令功能 :

显示OSPF无中断转发的信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf nsf 
  [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf nsf           OSPF Router with ID (134.1.1.200) (Process ID 200)instance is graceful restarting   Restart reason is switch to redundant control processor      Grace period 240      Start time 00：00：00     Time to leave 223 s     Helper 134.1.1.201     In the area 0.0.0.0     via interface gei-0/1/0/1 134.1.1.201     Neighbor is DR2WAY 





相关命令 :

无 




## show ip ospf request-list 


show ip ospf request-list 




命令功能 :

显示路由器请求的所有链路状态通告列表。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf request-list 
  {＜neighbor-id 
＞|[interface 
 ＜interface-name 
＞]|[process 
 ＜process-id 
＞]} 







命令参数解释 :



参数|描述
---|---
＜neighbor-id＞|显示所有等待为该邻居请求的链路状态通告
＜interface-name＞|显示所有在该接口上等待请求的链路状态通告
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf request-list             OSPF Router with ID (10.10.10.1) (Process ID 1) Neighbor 10.10.10.2, interface gei-0/1/0/9 address 10.10.10.1Type LS ID           ADV RTR         Seq NO      Age    Checksum1    10.10.10.1      10.10.10.1      0x8000002b  809    0x9b7f    Neighbor 10.10.10.2, interface gei-0/1/0/10 address 20.20.20.1Type LS ID           ADV RTR         Seq NO      Age    Checksum1    10.10.10.1      10.10.10.1      0x80000027  814    0x1b33   






相关命令 :

无 




## show ip ospf retransmission-list 


show ip ospf retransmission-list 




命令功能 :

显示路由器重传的所有链路状态通告列表 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf retransmission-list 
  [interface 
 ＜interface-name 
＞] [neighbor-id 
 ＜neighbor-id 
＞] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|显示在该接口上所有等待重传的链路状态通告
＜neighbor-id＞|显示所有在该接口上等待为该邻居重传的链路状态通告
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf retransmission-list             OSPF Router with ID (10.10.10.2) (Process ID 1)





相关命令 :

无 




## show ip ospf route 


show ip ospf route 




命令功能 :

显示OSPF的路由信息 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf route 
  [{[summary 
 [process 
 ＜process-id 
＞]]|[{{[process 
 ＜process-id 
＞],[adv-router 
 ＜router-id 
＞]}|[network 
 ＜Network prefix 
＞ [mask 
 ＜Network mask 
＞]]} [detail 
]]}] 







命令参数解释 :



参数|描述
---|---
summary|显示OSPF理由摘要信息
＜process-id＞|实例ID
＜process-id＞|实例ID
＜router-id＞|产生该OSPF路由的LSA的adv-router
＜Network prefix＞|按照指定网段前缀，显示该网段的OSPF路由信息
＜Network mask＞|指定前缀的掩码
detail|以detail模式显示OSPF路由信息








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ip ospf route summary process 11OSPF Local Ipv4 Routing TableCodes: O - OSPF intra, E1 - OSPF ext 1, E2 = OSPF ext2, D3 - OSPF type3 discard       OI - OSPF inter, D5 - OSPF type5 discard, D7 - OSPF type7 discardProcess ID: 11  OSPF-intra 5  OSPF-inter 0  OSPF-3D 0  OSPF-5D 0  OSPF-7D 0  OSPF-E1 0  OSPF-E2 0  Total 5ZXROSNG(config)#





相关命令 :

无 




## show ip ospf sham-links 


show ip ospf sham-links 




命令功能 :

显示OSPF后门链路信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf sham-links 
  [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf sham-links  Sham Link(To 22.22.22.22) is UP Up for 00:00:00  In area 0.0.0.1 Local interface loopback2 11.11.11.11 State DOWN, Transmit Delay(sec) 1, Cost 1, Authentication Type null  Timer intervals(sec) : Hello 10, Dead 40, Retransmit 5 Adjacency State DOWN Dead time : 00:00:00 Options : 0x0 In Full State for 00:00:00





相关命令 :

无 




## show ip ospf vertex backup 


show ip ospf vertex backup 




命令功能 :

显示OSPF节点的备份下一跳信息 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf vertex backup 
  [{[process 
 ＜process-id 
＞],[adv-router 
 ＜router-id 
＞]}] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|实例ID
＜router-id＞|拓扑的adv-router








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf vertex backupOSPFv2 Router ID (23.23.23.23) Process ID (23)Vertex Information (Area 0.0.0.1)Vertex type: router, Advertising Router: 12.12.12.12, Link State ID: 12.12.12.12via neighbor: 15.15.2.2, gei-0/1/0/2, cost 1, [primary]via neighbor: 15.15.3.2, gei-0/1/0/3, cost 5, [dynamic remote LFA]Session type: MPLS_LDP, Session status: downPeer session ID: 56.56.56.56, Peer metric: 3Protect type(S->PQ): link, nodeProtect type(PQ->D): NULLUpdate time: 1h15m22sVertex type: router, Advertising Router: 23.23.23.23, Link State ID: 23.23.23.23no primary information.Vertex type: router, Advertising Router: 56.56.56.56, Link State ID: 56.56.56.56via neighbor: 15.15.3.2, gei-0/1/0/3, cost 3, [primary]via neighbor: 15.15.2.2, gei-0/1/0/2, cost 3, [dynamic remote LFA]Session type: MPLS_LDP, Session status: downPeer session ID: 56.56.56.56, Peer metric: 3Protect type(S->PQ): link, nodeProtect type(PQ->D): node, downstreamUpdate time: 1h15m23svia neighbor: 15.15.2.2, gei-0/1/0/2, cost 3, [primary]via neighbor: 15.15.3.2, gei-0/1/0/3, cost 3, [dynamic remote LFA]Session type: MPLS_LDP, Session status: downPeer session ID: 56.56.56.56, Peer metric: 3Protect type(S->PQ): link, nodeProtect type(PQ->D): node, downstreamUpdate time: 1h15m23s  via neighbor: 60.0.0.2, gei-0/1/0/6, cost 401, [TI-LFA]    Tunnel type: SR-MPLS, Tunnel index: 8    Update time: 0h0m3s    Repair list:      [01] Node: 0.0.0.6      [02] Node: 0.0.0.5      [03] Node: 0.0.0.4    Repair path description:      [01] Node: 0.0.0.6      [02] Local IP: 50.0.0.2, Remote IP: 50.0.0.1      [03] Local IP: 40.0.0.1, Remote IP: 40.0.0.2Vertex type: network, Advertising Router: 34.1.1.1, Link State ID: 15.15.3.2no primary information.Vertex type: network, Advertising Router: 45.45.45.45, Link State ID: 15.15.4.1via neighbor: 15.15.3.2, gei-0/1/0/3, cost 2, [primary]via neighbor: 15.15.2.2, gei-0/1/0/2, cost 5, [dynamic remote LFA]Session type: MPLS_LDP, Session status: downPeer session ID: 56.56.56.56, Peer metric: 3Protect type(S->PQ): link, nodeProtect type(PQ->D): nodeUpdate time: 1h15m23svia neighbor: 15.15.2.2, gei-0/1/0/3, cost 2, [IP-FRR LFA]Protect type: link, node, downstreamUpdate time: 0h0m25sVertex type: router, Advertising Router: 103.0.0.1, Link State ID: 103.0.0.1via neighbor: 15.15.11.2, gei-0/1/0/1.1, cost 2, [primary]via neighbor: 15.15.2.2, gei-0/1/0/3, cost 3, [IP-FRR LFA]Protect type: link, node, downstreamUpdate time: 0h0m25s域信息说明：OSPFv2 Router ID：OSPFv2的router-id；Process ID：实例ID；Area：区域ID；Vertex type：vertex的类型，有两种类型：router和network；Advertising Router：通告路由器；Link State ID：连接状态ID；via neighbor: 15.15.3.2, gei-0/1/0/3, cost 2, [primary]：主下一跳的邻居，出接口和cost值；via neighbor: 15.15.2.2, gei-0/1/0/2, cost 5, [dynamic remote LFA]：DRLFA备份下一跳的邻居，出接口和cost值；Session type：建立会话的类型；Session status：会话的状态；Peer session ID：建立会话的对端ID；Peer metric：到对端会话的距离；Protect type(S->PQ)：源节点到PQ节点的保护类型，有NULL，link和node三种类型，可以是其中一种，也可以两种都是，两种都不是就是NULL；Protect type(PQ->D)：PQ节点到目的节点的保护类型，有NULL，node和downstream三种类型，可以是其中一种，也可以两种都是，两种都不是就是NULL；Update time：会话更新的时间。no primary information：表示当前vertex下没有主备下一跳信息。via neighbor: 15.15.2.2, gei-0/1/0/3, cost 3, [IP-FRR LFA]: IP-FRR备份下一跳的邻居，出接口和cost值；Protect type：IP-FRR保护类型，有NULL,node,link,downstream四种类型，可以是其中一种，也可以是多种，都不是就是NULL;Update time：会话更新的时间。via neighbor: 60.0.0.2, gei-0/1/0/6, cost 401, [TI-LFA]：TI-LFA备份下一跳的邻居，出接口和cost值；Tunnel type：隧道类型；Tunnel index：表示内部生成的隧道索引，用于转发；Repair list: 表示根据TI-LFA算法计算出的修复路径列表；Repair path description：表示根据修复路径的描述信息；Node：节点标识（OSPFv2的Router-ID）；Local IP: 节点本端接口地址；Remote IP: 节点远端端接口地址。






相关命令 :

无 




## show ip ospf virtual-links 


show ip ospf virtual-links 




命令功能 :

显示OSPF虚拟链路信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip ospf virtual-links 
  [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show ip ospf virtual-linksVirtual Link to router 1.33.33.1 is DOWN    Up for 00:00:00 (Demand circuit)    Transit area 0.0.0.1    via interface NULL 0.0.0.0    State DOWN, Transmit Delay(sec) 1    Cost 65535, Authentication Type null    Timer intervals(sec):Hello 10,Dead 40,Retransmit 5    Adjacency State DOWN    Dead time : 00:00:00 Options:0x0    In Full State for 00:00:00





相关命令 :

无 




## show ip ospf 


show ip ospf 




命令功能 :

显示OSPF协议的概要信息以及各个OSPF区域的概要信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip ospf 
  [＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，即配置的OSPF实例号，范围：1–65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXR10>show ip ospf 1OSPF 1 Router ID 10.10.10.1 enableDescription: This_instance_contains_three_areasDomain ID type 0x5,value 0.0.0.1Enabled for 1d18h,Debug onNumber of areas 3, Normal 2, Stub 1, NSSA 0Number of interfaces 3Number of neighbors 2Number of adjacent neighbors 2Number of virtual links 0Total number of entries in LSDB 14Number of ASEs in LSDB 0, Checksum Sum 0x00000000Number of grace LSAs 0Number of new LSAs received 687Number of self-originated LSAs 561Number of non self-originated LSAs 0Hold time between consecutive SPF 1 secsMicroloop-prevention remote-lfa enabled, delay time 3000 msNon-stop Forwarding disabled, last NSF restart 1d18h ago (took 0 secs)Area 0.0.0.0 enable (Demand circuit available)Enabled for 1d18hArea has no authenticationTimes spf has been run 8Number of interfaces 1. Up 1Number of ASBR local to this area 0Number of ABR local to this area 2Total number of intra/inter entries in LSDB 6. Checksum Sum 0x0001f81eArea-filter out not setArea-filter in not setArea ranges count 0Area 0.0.0.1 enable (Demand circuit available)Enabled for 23:50:27It is a stub area, no summary LSAMetric for default route 100Area has no authenticationTimes spf has been run 20Number of interfaces 1. Up 1Number of ASBR local to this area 0Number of ABR local to this area 1Total number of intra/inter entries in LSDB 2. Checksum Sum 0x0000806cArea-filter zxr10 outArea-filter in not setArea ranges count 110.0.0.0          255.0.0.0         advertiseArea 0.0.0.3 enable (Demand circuit available)Enabled for 1d17hArea has no authenticationTimes spf has been run 15Number of interfaces 1. Up 1Number of ASBR local to this area 0Number of ABR local to this area 2Total number of intra/inter entries in LSDB 6. Checksum Sum 0x000431d1Area-filter out not setArea-filter in not setArea ranges count 0ZXR10>






相关命令 :

无 




## snmp context 


snmp context 




命令功能 :

设置OSPF路由SNMP标识以支持MIB多实例显示。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



snmp context 
  ＜context-name 
＞

no snmp context 








命令参数解释 :



参数|描述
---|---
＜context-name＞|实例SNMP标识，长度1–30个字符








缺省 :

无 






使用说明 :

为支持MIB多实例显示，可设置OSPF标识，SNMP配置中可指定相同的SNMP上下文标识以读取该指定的实例MIB信息。 






范例 :

在实例上配置实例标识为zte：ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#snmp context zteZXROSNG(config-ospf-1)#exitZXROSNG(config)#snmp-server context zte





相关命令 :

snmp-server context 




## static-remote-lfa mpls-ldp 


static-remote-lfa mpls-ldp 




命令功能 :

配置静态远端LFA功能。使用no命令取消配置。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :


static-remote-lfa mpls-ldp 
 next-hop 
 ＜next-hop 
＞ [interface 
 ＜interface-name 
＞ gateway 
 ＜gateway 
＞] [prefix 
 ＜prefix-list-name 
＞]
no static-remote-lfa mpls-ldp 
  [prefix 
 ＜prefix-list-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜next-hop＞|指定静态远端LFA的下一跳，IP地址格式，范围是有效的IP地址的范围
＜interface-name＞|指定的备份出接口名
＜gateway＞|指定的备份下一跳网关，IP地址格式
＜prefix-list-name＞|指定前缀列表名








缺省 :

无 






使用说明 :

1.如果不带prefix，则表示通配所有的地址前缀。2.指定的远端下一跳是否合适等由人工保证。详见配置指导文档。3.如果不带interface-name 和 gateway，表示不指定本地下一跳，由指定的远端下一跳迭代出本地下一跳。






范例 :

ZXROSNG(config-ospf-1-area-1-if-loopback1)#static-remote-lfa mpls-ldp next-hop 1.1.1.1 prefix zte 






相关命令 :

无 




## stub 


stub 




命令功能 :

定义一个区域为stub区域。使用no命令取消配置。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


stub 
  [{[no-summary 
],[default-cost 
 ＜cost 
＞],default-information-originate 
}]
no stub 
  [{[no-summary 
],[default-cost 
],default-information-originate 
}]
				






命令参数解释 :



参数|描述
---|---
no-summary|禁止ABR将汇总路由信息发送到该stub区域
＜cost＞|向该stub区域通告的缺省路由的费用，范围：0–65535
default-information-originate|向stub区域通告静态缺省路由






No参数|描述
---|---
default-cost|清除缺省花费








缺省 :

1）    区域默认不是stub区域。2）    对于stub区域来说:    在不配置no-summary选项的情况下，允许ABR向stub区域通告其它区域的汇总信息。    不配置default-information-originate选项的情况下，如果stub区域不是协议规定的ABR，不会向stub区域通告缺省路由。    不配置default-cost选项的情况下，通告的缺省路由的花费是1。





使用说明 :

不让ABR往stub区域通告汇总路由信息可以配置no-summary选项；如果想向stub区域通告静态缺省路由可以通过配置default-information-originate选项，默认的缺省路由的花费是1，通过改变default-cost选项的值可以改变stub区域的缺省路由的花费。





范例 :

ZXROSNG(config-ospf-1)#area 1ZXROSNG(config-ospf-1-area-1)#stub no-summary default-cost 100 default-information-originate






相关命令 :

无 




## stub-host 


stub-host 




命令功能 :

添加一个区域内本路由器通告的主机路由。使用no命令取消配置。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


stub-host 
  ＜ip-address 
＞ cost 
 ＜cost 
＞
no stub-host 
  ＜ip-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ip-address＞|需作为存根主机通告的主机地址，为十进制点分形式
＜cost＞|通告的该主机路由的费用，范围：1–65535








缺省 :

区域内没有本路由器要通告的主机路由。 






使用说明 :

1. 该区域不存在则自动创建。2. no area < area-id> stub-host < ip-address>删除一个区域内本路由器通告的主机路由。






范例 :

在OSPF实例1的区域1添加一个区域内本路由器通告的主机路由，IP地址为17.17.1.7，花费值为10。ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#area 1ZXROSNG(config-ospf-1-area-1)#stub-host 17.17.1.7 cost 10ZXROSNG(config-ospf-1-area-1)#






相关命令 :

无 




## summary-address 


summary-address 




命令功能 :

配置OSPF聚集地址，汇总正重新分配到OSPF的其他路由选择协议路径。使用no命令取消配置。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


summary-address 
  ＜ip-address 
＞ ＜net-mask 
＞ [cost 
 ＜cost-value 
＞]
no summary-address 
  ＜ip-address 
＞ ＜net-mask 
＞ [cost 
]
				






命令参数解释 :



参数|描述
---|---
＜ip-address＞|IP地址，十进制点分形式
＜net-mask＞|概要路径的IP子网掩码，十进制点分形式
＜cost-value＞|此汇聚范围的代价






No参数|描述
---|---
cost|清除汇聚范围的花费








缺省 :

OSPF无聚集地址。 






使用说明 :

1. 可以对一个给定的级汇总多组地址，从其他路由选择协议获得的路由也可以进行汇总。2. 用于公告概要路径的计量尺度是所有更具体路径中的最小计量尺度。3. 此命令有助于减少路由表的大小。






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#summary-address　10.1.0.0 255.255.0.0





相关命令 :

无 




## ti-lfa capability 


ti-lfa capability 




命令功能 :

OSPF使能TI-LFA功能。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



ti-lfa capability 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能TI-LFA功能
disable|去使能TI-LFA功能








缺省 :

该功能是不使能的。 






使用说明 :

TI-LFA功能需要使用到MPLS TE隧道，而目前MPLS不支持VRF实例，所以在VRF实例中使能了TI-LFA也无法生效。TI-LFA功能还需要配置了segment-routing mpls之后才能算出备份路径。仅配置TI-LFA功能无法生效。






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#ti-lfa capability enable ZXROSNG(config-ospf-1)#ti-lfa capability disable ZXROSNG(config-ospf-1)#






相关命令 :

IPv4-OSPF模式下的segment-routing mpls命令 




## timers fast-reroute 


timers fast-reroute 




命令功能 :

设置两个连续快速重计算路由（IPFRR）SPF计算之间的最小时间间隔。使用no命令使该时间间隔恢复到缺省值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers fast-reroute 
  ＜spf-holdtime 
＞

no timers fast-reroute 








命令参数解释 :



参数|描述
---|---
＜spf-holdtime＞|两个连续IPFRR SPF计算之间的最小时间，缺省1秒，范围：1–65535，单位：秒








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#timers fast-reroute 8





相关命令 :

无 




## timers lsa-group-pacing 


timers lsa-group-pacing 




命令功能 :

设置OSPF LSA组定步的时间间隔。使用no命令使OSPF LSA组定步的时间间隔恢复到缺省值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers lsa-group-pacing 
  ＜timeout 
＞

no timers lsa-group-pacing 








命令参数解释 :



参数|描述
---|---
＜timeout＞|OSPF LSA组定步的时间间隔，缺省1秒，范围：1–1800，单位：秒








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#timer lsa-group-pacing 2





相关命令 :

无 




## timers spf 


timers spf 




命令功能 :

设置触发SPF计算的延时。使用no命令使该时间恢复到缺省值。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers spf 
  ＜spf-holdtime 
＞

no timers spf 








命令参数解释 :



参数|描述
---|---
＜spf-holdtime＞|设置触发SPF计算的延时，缺省1秒，范围：1–65535，单位：秒








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#timer spf 2





相关命令 :

无 




## timers throttle lsa 


timers throttle lsa 




命令功能 :

使能退避指数定时器，LSA生成的时候退避 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers throttle lsa 
  ＜hold time 
＞ ＜min delay time 
＞ ＜max delay time 
＞

no timers throttle lsa 








命令参数解释 :



参数|描述
---|---
＜hold time＞|两次拓扑变化导致更新LSA的持续时间，范围：1-600000，单位：毫秒
＜min delay time＞|更新LSA的最小延迟时间，范围：1-600000，单位：毫秒
＜max delay time＞|最大延时时间时间，单位：毫秒。数值范围：1–600000








缺省 :

不使用退避定时器 






使用说明 :

配置了退避定时器后，SPF计算会使用退避定时器.其中三个参数要满足hold_time<= delay_time<= max_delay_time,如果配置的值不满足，会自动调整，使其满足。






范例 :

Ospf实例下配置退避定时器：ZXROSNG(config-ospf-1)# timers throttle spf 30 40 500






相关命令 :

无 




## timers throttle lsa-arrival 


timers throttle lsa-arrival 




命令功能 :

使能退避指数定时器，退避接收相同的LSA 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers throttle lsa-arrival 
  ＜hold time 
＞ ＜min delay time 
＞ ＜max delay time 
＞

no timers throttle lsa-arrival 








命令参数解释 :



参数|描述
---|---
＜hold time＞|接收更新的LSA第一次触发的时间，小于等于delay_time,单位ms。数值范围：0–600000
＜min delay time＞|最小延时时间时间，小于等于max_delay_time，单位ms。数值范围：0–600000
＜max delay time＞|最大延时时间时间，单位ms。 数值范围：0–600000








缺省 :

不使用退避定时器 






使用说明 :

配置了退避定时器后，会退避接收相同的LSA，当LSA在不断震荡或者需要快速接收LSA的时候使用该命令。当把所有参数都配置成0的时候表示不延时接收，用在拓扑稳定且需要快速接收LSA的场景下实现。当配置参数不为0的时候，则会根据退避算法，在一定时间内不会接收这些LSA，保证网络的稳定。其中三个参数要满足start_time<= delay_time<= max_delay_time,如果配置的值不满足，会自动调整，使其满足。





范例 :

Ospf实例下配置退避定时器：ZXROSNG(config-ospf-1)# timers throttle lsa-arrival 100 500 2000





相关命令 :

无 




## timers throttle spf 


timers throttle spf 




命令功能 :

使能退避指数定时器，SPF计算的时候退避计算 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers throttle spf 
  ＜hold time 
＞ ＜min delay time 
＞ ＜max delay time 
＞

no timers throttle spf 








命令参数解释 :



参数|描述
---|---
＜hold time＞|两次拓扑变化导致SPF计算的持续时间，范围：1-600000，单位：毫秒
＜min delay time＞|第一次和第二次SPF计算的延迟时间，范围：1-600000，单位：毫秒
＜max delay time＞|最大延时时间时间，单位：毫秒。数值范围：1–600000








缺省 :

不使用退避定时器 






使用说明 :

配置了退避定时器后，SPF计算会使用退避定时器.其中三个参数要满足hold_time<= delay_time<= max_delay_time,如果配置的值不满足，会自动调整，使其满足。





范例 :

Ospf实例下配置退避定时器：ZXROSNG(config-ospf-1)# timers throttle spf 30 40 500





相关命令 :

无 




track :

track 




命令功能 :

根据efm的检测结果进行联动 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


track 
  ＜track-name 
＞
no track 
  ＜track-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜track-name＞|检测的关联接口名称








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXROSNG(config-ospf-1)#track gei-0/1/0/1






相关命令 :

无 




## transmit-delay 


transmit-delay 




命令功能 :

配置接口传输一个链路状态更新数据包的迟延。使用no命令使接口传输一个链路状态更新数据包的迟延恢复到缺省值。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



transmit-delay 
  ＜seconds 
＞

no transmit-delay 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口传输一个链路状态更新数据包的迟延，缺省为1秒，范围：1–65535，单位：秒








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#transmit-delay 2





相关命令 :

无 




## transmit-delay 


transmit-delay 




命令功能 :

配置接口传输一个链路状态更新数据包的迟延。使用no命令使接口传输一个链路状态更新数据包的迟延恢复到缺省值。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



transmit-delay 
  ＜seconds 
＞

no transmit-delay 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口传输一个链路状态更新数据包的迟延，缺省为1秒，范围：1–65535，单位：秒








缺省 :

[89\9900]缺省值1s[M6000\M6000-S\ZSR]无





使用说明 :

无 






范例 :

[89\9900]1. 配置接口重传LSA的时间间隔为2秒：ZXROSNG(config)#router ospf 1ZXR10 (config-ospfv2)#interface vlan1ZXR10 (config-ospfv2-if)#retransmit-delay 2[M6000\M6000-S\ZSR][M6000\M6000-S]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-0/1/0/1ZXR10 (config-ospf-1-if-gei-0/1/0/1)#transmit-delay 2[ZSR]:ZXROSNG(config)#router ospf 1ZXR10 (config-ospf-1)#interface gei-1/1ZXR10 (config-ospf-1-if-gei-1/1)#transmit-delay 2





相关命令 :

无 




## transmit-delay 


transmit-delay 




命令功能 :

配置接口传输一个链路状态更新数据包的迟延。使用no命令使接口传输一个链路状态更新数据包的迟延恢复到缺省值。 






命令模式 :

 IPv4-OSPF-MULTI-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



transmit-delay 
  ＜seconds 
＞

no transmit-delay 








命令参数解释 :



参数|描述
---|---
＜seconds＞|接口传输一个链路状态更新数据包的迟延，缺省为1秒，范围：1–65535，单位：秒








缺省 :

1 






使用说明 :

使用场景在使用多区域接口建链时，如果想要手动指定接口传输一个链路状态更新数据包的迟延，则应配置此命令。






范例 :

配置IPv4 OSPF实例1的区域100下添加fei-0/1/0/1多区域接口，配置多区域接口fei-0/1/0/1链路状态更新数据包的迟延为120秒。R1(config)#router ospf 1R1(config-ospf-1)#area 100R1(config-ospf-1-area-100)#multi-area-interface fei-0/1/0/1R1(config-ospf-1-area-100-mif-fei-0/1/0/1)# transmit-delay 120






相关命令 :

无 




## ttl-security 


ttl-security 




命令功能 :

配置OSPF实例的邻居TTL跳数。 






命令模式 :

 IPv4-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



ttl-security 
 all-interfaces 
 hops 
 ＜hops 
＞

no ttl-security 








命令参数解释 :



参数|描述
---|---
＜hops＞|允许的跳数，缺省不配置，范围：1–254，单位：跳








缺省 :

没有配置 






使用说明 :

1.    这里的跳数是两个邻居之间的距离，而不是TTL值。2.    如果配置了OSPF的GTSM功能，而协议报文承载于MPLS之上，不能保证GTSM功能正确生效。3.    承载于IP隧道（如GRE隧道）上的OSPF协议可以启用GTSM功能。






范例 :

ZXROSNG(config-ospf-1)# ttl-security all-interfaces hops 2 






相关命令 :

无 




## ttl-security 


ttl-security 




命令功能 :

配置OSPF接口的邻居TTL跳数。 






命令模式 :

 IPv4-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



ttl-security 
 hops 
 ＜hops 
＞

no ttl-security 








命令参数解释 :



参数|描述
---|---
＜hops＞|允许的跳数，缺省不配置，范围：1–254，单位：跳








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-ospf-1-if-gei-0/1/0/1)# ttl-security hops 2 






相关命令 :

无 




## ttl-security 


ttl-security 




命令功能 :

配置OSPF接口的邻居TTL跳数。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



ttl-security 
 hops 
 ＜hops 
＞

no ttl-security 








命令参数解释 :



参数|描述
---|---
＜hops＞|允许的跳数，缺省不配置，范围：1–254，单位：跳








缺省 :

[M6000\M6000-S\ZSR]无[89\9900]缺省没有配置。





使用说明 :

[M6000\M6000-S\ZSR]无[89\9900]1.    这里的跳数是两个邻居之间的距离，而不是TTL值。2.    如果配置了OSPF的GTSM功能，而协议报文承载于MPLS之上，不能保证GTSM功能正确生效。3.    承载于IP隧道（如GRE隧道）上的OSPF协议可以启用GTSM功能。





范例 :

[M6000\M6000-S\ZSR]ZXROSNG(config-ospf-1-if-gei-0/1/0/1)# ttl-security hops 2[89\9900]1. 配置OSPF邻居的跳数为2ZXROSNG(config-ospfv2-if)# ttl-security hops 2






相关命令 :

相关命令[M6000\M6000-S\ZSR]无[89\9900]show ip ospf interface



## virtual-link 


virtual-link 




命令功能 :

定义OSPF虚拟链路，如果指定区域不存在则自动创建。使用no命令删除指定虚拟链路。 






命令模式 :

 IPv4-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


virtual-link 
  ＜neighbor-id 
＞ [{[hello-interval 
 ＜hello-interval 
＞],[retransmit-interval 
 ＜retransmit-interval 
＞],[transmit-delay 
 ＜transmit-delay 
＞],[dead-interval 
 ＜dead-interval 
＞],[dead-delay 
 ＜dead-delay 
＞],[authentication-key 
 {encrypted 
 ＜authenkey encrpted 
＞|clear 
 ＜_auth_key 
＞|＜_auth_key 
＞}]}] [{[authentication 
 [{null 
|message-digest 
|keychain 
 ＜Keychain name 
＞}]]|[message-digest-key 
 ＜key-id 
＞ md5 
 {encrypted 
 ＜md5-key 
＞|clear 
 ＜md5-key 
＞|＜md5-key 
＞} [delay 
 ＜delay-time 
＞]]}]
no virtual-link 
  ＜neighbor-id 
＞ [{[hello-interval 
],[retransmit-interval 
],[transmit-delay 
],[dead-interval 
],[dead-delay 
],[authentication-key 
],[message-digest-key 
 ＜key-id 
＞],[authentication 
]}]
				






命令参数解释 :



参数|描述
---|---
＜neighbor-id＞|虚拟链路对端路由器ID，为十进制点分形式的IP地址
＜hello-interval＞|虚拟链路上发送HELLO报文的时间间隔，缺省为10秒，范围：1–8192，单位：秒
＜retransmit-interval＞|虚拟链路上重传间隔，缺省为5秒，范围：1–8192，单位：秒
＜transmit-delay＞|虚拟链路上发送一个链路状态更新数据包的迟延，缺省为1秒，范围：1–8192，单位：秒
＜dead-interval＞|虚拟链路上邻居死亡时间，缺省为40秒，范围：1–8192，单位：秒
＜dead-delay＞|虚拟链路上邻居死亡延迟时间，缺省为40秒，范围：1–8192，单位：秒
＜authenkey encrpted＞|加密后的明文密码
＜_auth_key＞|明文密码
＜_auth_key＞|明文密码
authentication|在虚拟链路上配置认证方式
null|null 为在该虚拟链路使用类型0认证，即无认证
message-digest|message-digest 为在该虚拟链路使用类型2认证，即md5认证
＜Keychain name＞|虚链使用keychain-name指定的keychain用于加解密，长度为1~31个字符
＜key-id＞|虚拟链路上的md5认证口令序号，范围：1–255
md5|虚拟链路上的md5认证
＜md5-key＞|为虚拟链路上的md5认证口令
＜md5-key＞|为虚拟链路上的md5认证口令
＜md5-key＞|为虚拟链路上的md5认证口令
＜delay-time＞|虚拟链路上md5认证延迟生效的时间，范围：0–100000，单位：分钟






No参数|描述
---|---
hello-interval|清除发送HELLO报文的时间间隔
retransmit-interval|清除重传间隔
transmit-delay|链路状态更新数据包的迟延
dead-interval|清除邻居死亡时间
dead-delay|清除邻居死亡延迟时间
authentication-key|清除认证密钥








缺省 :

没有定义虚拟链路。对虚拟链路来说，没有预定义口令；没有预定义报文摘要认证口令。






使用说明 :

1．    如果该区域不存在则自动创建2．    虚链上的认证要起作用，需在area 0上配置区域认证方式，<key>和<cryptkey>不能为空。3．    参数<key>和<cryptkey>所允许的字符范围如下：0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ`*-=~!@#$%^&（）_+[]{}|;':,./<>\\4．    不能在区域0，stub区域和nssa区域建立虚链。






范例 :

RP1(config)#router ospf 1RP1(config-ospf-1)#area 2RP1(config-ospf-1-area-2)#virtual-link 1.1.1.1 authentication keychain kk






相关命令 :

无 




## virtual-system 


virtual-system 




命令功能 :

使能OSPF区域接口的虚系统。 






命令模式 :

 IPv4-OSPF-AREA接口模式  






命令默认权限级别 :

15 






命令格式 :



virtual-system 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|打开接口虚系统功能
disable|关闭接口虚系统功能








缺省 :

默认不使能 






使用说明 :

配置接口启用虚系统,启用虚系统接口发包使用虚拟id,根据虚系统启用情况产生虚拟拓补LSA,根据邻居实际情况补充虚拟Router LSA的拓补信息，可以形成负荷分担。





范例 :

R1(config)#router ospf 1R1(config-ospf-1)#area 100R1(config-ospf-1-area-100)#interface gei-0/1/0/1R1(config-ospf-1-area-100-if-gei-0/1/0/1)#virtual-system enable 






相关命令 :

无 




# 静态路由配置命令 
## ip route nexthop 


ip route nexthop 




命令功能 :

该命令在全局配置模式下执行，用于在配置私网静态路由的公网下一跳（global静态路由）带BFD检测时，或者在配置公网静态路由非直连下一跳带BFD检测时，创建BFD会话时需要指定一个本端接口地址作为其local地址。这种情况下，为BFD会话指定本地接口地址时使用该命令。对于某些私网多跳BFD场景（如静态路由迭代PE多导入路由），需要使用指定私网下的loopback口作为多跳BFD的源端地址。但是如果没有指定，则按迭代的结果作为源端地址创建BFD会话。






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ip route nexthop 
 source 
 [vrf 
 ＜vrf-name 
＞] ＜interface_name 
＞
no ip route nexthop 
 source 
 [vrf 
 ＜vrf-name 
＞]
				






命令参数解释 :



参数|描述
---|---
source|辅助参数标识，表示创建BFD 多跳会话下一跳对应的源端。
＜vrf-name＞|私网静态路由对应的VRF名称，不配置该参数表示配置公网。VRF名称的取值长度为1-32位字符串。
＜interface_name＞|配置绑定的接口名称，目前只支持绑定环回接口loopback口。绑定该接口后，使用该接口的地址作为BFD会话的local地址。环回接口取值范围为loopback1-loopback64。缺省时不绑定任何接口。








缺省 :

缺省情况下不绑定任何环回口。 






使用说明 :

1、此命令与静态路由配置命令（参见配置命令ip route）以及BFD会话配置命令（参见配置命令bfd）配合使用。2、当前仅支持配置loopback1~loopback64接口，采用loopback接口地址作为BFD会话的local端地址。3、公网的配置命令只适用于公网静态路由非直连下一跳及global静态路由创建BFD会话时使用。4、私网的配置命令适用于私网静态路由创建多跳BFD会话，要求指定loopback口必须绑定在指定的VRF下才有意义。一个VRF下只允许配置一个loopback口。5、如果没有配置公网的源端地址命令，则公网多跳BFD以及global路由不会创建BFD会话。6、如果没有配置私网的源端地址命令，则私网多跳BFD会话会继续用迭代的结果作为源端地址，目的是为了兼容之前的已实现功能。7、实际应用中建议一个loopback口对应一个VRF。如果一个loopback口对应多个VRF，可以配置成功，也不会有错误提示，但实际有意义的只有一组。 8、实际应用时必须将配置loopback口绑定在指定的VRF下才有意义，否则BFD会话可能无法UP。如果loopback口不在指定的VRF下，不会有错误提示。9、当绑定的loopback出现变更或loopback口的地址发生变更，已创建的BFD会话的源端地址会自动更新到最新状态。10、当指定的loopback口不存在时，该命令会提示错误，用户需要先创建对应的loopback口，再配置该命令。11、当指定的VRF不存在时，该命令会提示错误，用户需要先创建对应的VRF实例，再配置该命令。12、当删除VRF实例时，如果本配置命令已经存在，会提示错误，用户需要先删除本配置命令，再删除VRF实例。13、当删除loopback口时，如果本配置命令已经存在，会提示错误，用户需要先删除本配置命令，再删除loopback口。






范例 :

三台交换机R1，R2，R3依次进行直连，R1 上loopback1的地址为2.1.1.1/32，gei-0/1/0/1地址为192.168.1.101/24；R2 的gei-0/1/0/1地址为192.168.1.102/24，gei-0/1/0/6地址为168.1.1.2/24；R3的gei-0/1/0/6地址为168.1.1.3/24。R1的配置：ZXROSNG(config-if-gei-0/1/0/1)#ip address 192.168.1.101 255.255.255.0ZXROSNG(config-if-gei-0/1/0/6)#no shutdownZXROSNG(config-if-loopback1)#ip address 2.1.1.1 255.255.255.255ZXROSNG(config-if-gei-0/1/0/6)#no shutdownZXROSNG(config)#ip route 168.1.1.3 255.255.255.255 192.168.1.102ZXROSNG(config)#ip route 6.0.0.0 255.0.0.0 168.1.1.3 bfd enable  //指定非直连下一跳ZXROSNG(config)#ip route nexthop source loopback1R2的配置：ZXROSNG(config-if-gei-0/1/0/1)#ip address 192.168.1.102 255.255.255.0ZXROSNG(config-if-gei-0/1/0/1)#no shutdownZXROSNG(config-if-gei-0/1/0/6)#ip address 168.1.1.2 255.255.255.0ZXROSNG(config-if-gei-0/1/0/6)#no shutdownZXROSNG(config)#ip route 2.1.1.1 255.255.255.255 192.168.1.101R3的配置：ZXROSNG(config-if-gei-0/1/0/6)#ip address 168.1.1.3 255.255.255.0ZXROSNG(config-if-gei-0/1/0/6)#no shutdownZXROSNG(config)#ip route 2.1.1.1 255.255.255.255 168.1.1.2ZXROSNG(config-bfd)#bfdZXROSNG(config-bfd)# session 1 peer-bfd ipv4 168.1.1.3 2.1.1.1配置验证：在R1上查看BFD会话：ZXROSNG(config)#show bfd neighbors ip brief LocalAddr       PeerAddr        LD        RD        Hold   State     Interface2.1.1.1         168.1.1.3       2049      2049      150    UP           ---在R3上查看BFD会话：ZXROSNG(config)#show bfd neighbors ip brief LocalAddr        PeerAddr        LD        RD        Hold   State     Interface168.1.1.3        2.1.1.1         2049      2049      150    UP           ---






相关命令 :

ip route 静态路由的配置命令。 




## ip route 


ip route 




命令功能 :

该命令在全局配置模式下执行，用于手动配置静态路由。在网络管理员对全网拓扑熟悉的情况下，可以根据自己的路由需求通过该命令进行手动配置，以达到对网络中路由行为的精确控制。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ip route 
  {vrf 
 {mng 
|＜vrf-name 
＞} {＜prefix 
＞ ＜net-mask 
＞|＜prefix/prefix-length 
＞} {＜forwarding-router's-addres 
＞ [global 
] [＜distance-metric 
＞] [metric 
 ＜metric-value 
＞] [tag 
 ＜tag-value 
＞] [bfd 
 enable 
]|＜interface-name 
＞ {＜forwarding-router's-address 
＞ [＜distance-metric 
＞] [metric 
 ＜metric-value 
＞] [tag 
 ＜tag-value 
＞] [bfd 
 enable 
]|[＜distance-metric 
＞] [metric 
 ＜metric-value 
＞] [tag 
 ＜tag-value 
＞]}} [track 
 ＜track-name 
＞] [name 
 ＜description-name 
＞]|{＜prefix 
＞ ＜net-mask 
＞|＜prefix/prefix-length 
＞} {＜forwarding-router's-addres 
＞ [＜distance-metric 
＞] [metric 
 ＜metric-value 
＞] [tag 
 ＜tag-value 
＞] [bfd 
 enable 
]|＜interface-name 
＞ {＜forwarding-router's-address 
＞ [＜distance-metric 
＞] [metric 
 ＜metric-value 
＞] [tag 
 ＜tag-value 
＞] [bfd 
 enable 
]|[＜distance-metric 
＞] [metric 
 ＜metric-value 
＞] [tag 
 ＜tag-value 
＞]}} [track 
 ＜track-name 
＞] [name 
 ＜description-name 
＞]}
no ip route 
  [vrf 
 {mng 
|＜vrf-name 
＞}] {all 
|{＜prefix 
＞ ＜net-mask 
＞|＜prefix/prefix-length 
＞} [{＜forwarding-router's-address 
＞|＜interface-name 
＞ [＜forwarding-router's-address 
＞]}]}
				






命令参数解释 :



参数|描述
---|---
mng|用于提示配置管理口静态路由。
＜vrf-name＞|私网静态路由对应的VRF名称，不配置该参数表示配置公网静态路由。VRF名称的取值长度为1-32位字符串。
＜prefix＞|路由的网络前缀。采用十进制点分形式A.B.C.D，不能配置为0.x.x.x地址、组播地址（224.x.x.x-255.x.x.x）、环回地址（127.x.x.x）、保留地址（240.x.x.x-255.x.x.x）以及全1的广播地址（255.255.255.255）。
＜net-mask＞|网络的子网掩码，必须与网络前缀相匹配。采用十进制点分形式A.B.C.D。
＜prefix/prefix-length＞|指定前缀地址和掩码长度配置路由。掩码长度范围为：0-32
＜forwarding-router's-addres＞|为静态路由指定下一跳。采用十进制点分形式A.B.C.D，不能配置为全0地址（0.0.0.0）、0.x.x.x地址、组播地址（224.x.x.x-255.x.x.x）、环回地址（127.x.x.x）、保留地址（240.x.x.x-255.x.x.x）以及全1的广播地址（255.255.255.255）。
global|为私网静态路由指定公网下一跳，只有在配置vrf<vrf-name>和仅配置下一跳时才允许配置。取消此属性需采用删除路由或者配置相同路由而不配置此属性的方式。带global属性的静态路由，可简称为global路由。缺省为不配置该属性，即为非global静态路由。
＜distance-metric＞|配置静态路由的管理距离，相当于路由协议的优先级，值越小，优先级越高。缺省情况下静态路由的优先级高于动态路由，默认为1，但是通过设置可使动态路由优先于静态路由。采用1-255之间的整数。默认值为1。
＜metric-value＞|配置静态路由的路由度量，度量值越小表示路由越优。采用0-255之间的整数。默认值为0。
＜tag-value＞|配置静态路由的路由标识，主要用于routemap路由过滤规则。采用0-4294967295之间的整数。默认值为0。
enable|为静态路由关联bfd检测的使能开关。取消BFD检测，采用删除路由或者配置相同路由而不配置bfd选项的方式。缺省为不使能BFD。
＜interface-name＞|为静态路由指定出接口。指定的出接口既可以是物理接口（以太网接口、POS接口），也可以是逻辑接口（loopback接口、supervlan接口、null口、smartgroup接口、posgroup接口、Ulei接口（Universal Logic Ethernet Interface，通用逻辑以太网接口）、te_tunnel接口、multilink(Multilink（PPP Multilink Protocol，多链路协议)接口、gre_tunnel (Generic Routing Encapsulation Tunnel，GRE隧道) 、te_tunnel接口（RSVP-TE信令建立的隧道）、v6_tunnel接口（IPv6 over IPv4隧道））等。
＜forwarding-router's-address＞|配置出接口时指定的下一跳，只有配置了静态路由出接口时，该参数才允许配置。当指定的出接口为以太网接口或三层VLAN接口时，建议配置下一跳，否则可能导致下层流量不通。采用十进制点分形式A.B.C.D，不能配置为全0地址（0.0.0.0）、0.x.x.x地址、组播地址（224.x.x.x-255.x.x.x）、环回地址（127.x.x.x）、保留地址（240.x.x.x-255.x.x.x）以及全1的广播地址（255.255.255.255）。
＜distance-metric＞|配置静态路由的管理距离，相当于路由协议的优先级，值越小，优先级越高。缺省情况下静态路由的优先级高于动态路由，默认为1，但是通过设置可使动态路由优先于静态路由。采用1-255之间的整数。默认值为1。
＜metric-value＞|配置静态路由的路由度量，度量值越小表示路由越优。采用0-255之间的整数。默认值为0。
＜tag-value＞|配置静态路由的路由标识，主要用于routemap路由过滤规则。采用0-4294967295之间的整数。默认值为0。
enable|为静态路由关联bfd检测的使能开关。取消BFD检测，采用删除路由或者配置相同路由而不配置bfd选项的方式。缺省为不使能BFD。
＜distance-metric＞|配置静态路由的管理距离，相当于路由协议的优先级，值越小，优先级越高。缺省情况下静态路由的优先级高于动态路由，默认为1，但是通过设置可使动态路由优先于静态路由。采用1-255之间的整数。默认值为1。
＜metric-value＞|配置静态路由的路由度量，度量值越小表示路由越优。采用0-255之间的整数。默认值为0。
＜tag-value＞|配置静态路由的路由标识，主要用于routemap路由过滤规则。采用0-4294967295之间的整数。默认值为0。
＜track-name＞|为静态路由故障联动处理关联的track名称。取消联动关联检测，采用删除路由或者配置相同路由而不配置track选项的方式。采用1-31位字符串。缺省为不关联track检测对象。
＜description-name＞|静态路由的描述信息。采用1-64位字符串。缺省为没有描述信息。
＜prefix＞|路由的网络前缀。采用十进制点分形式A.B.C.D，不能配置为0.x.x.x地址、组播地址（224.x.x.x-255.x.x.x）、环回地址（127.x.x.x）、保留地址（240.x.x.x-255.x.x.x）以及全1的广播地址（255.255.255.255）。
＜net-mask＞|网络的子网掩码，必须与网络前缀相匹配。采用十进制点分形式A.B.C.D。
＜forwarding-router's-addres＞|为静态路由指定下一跳。采用十进制点分形式A.B.C.D，不能配置为全0地址（0.0.0.0）、0.x.x.x地址、组播地址（224.x.x.x-255.x.x.x）、环回地址（127.x.x.x）、保留地址（240.x.x.x-255.x.x.x）以及全1的广播地址（255.255.255.255）。
＜distance-metric＞|配置静态路由的管理距离，相当于路由协议的优先级，值越小，优先级越高。缺省情况下静态路由的优先级高于动态路由，默认为1，但是通过设置可使动态路由优先于静态路由。采用1-255之间的整数。默认值为1。
＜metric-value＞|配置静态路由的路由度量，度量值越小表示路由越优。采用0-255之间的整数。默认值为0。
＜tag-value＞|配置静态路由的路由标识，主要用于routemap路由过滤规则。采用0-4294967295之间的整数。默认值为0。
enable|为静态路由关联bfd检测的使能开关。取消BFD检测，采用删除路由或者配置相同路由而不配置bfd选项的方式。缺省为不使能BFD。
＜interface-name＞|为静态路由指定出接口。指定的出接口既可以是物理接口（以太网接口、POS接口），也可以是逻辑接口（loopback接口、supervlan接口、null口、smartgroup接口、posgroup接口、Ulei接口（Universal Logic Ethernet Interface，通用逻辑以太网接口）、te_tunnel接口、multilink(Multilink（PPP Multilink Protocol，多链路协议)接口、gre_tunnel (Generic Routing Encapsulation Tunnel，GRE隧道) 、te_tunnel接口（RSVP-TE信令建立的隧道）、v6_tunnel接口（IPv6 over IPv4隧道））等。
＜forwarding-router's-address＞|配置出接口时指定的下一跳，只有配置了静态路由出接口时，该参数才允许配置。当指定的出接口为以太网接口或三层VLAN接口时，建议配置下一跳，否则可能导致下层流量不通。采用十进制点分形式A.B.C.D，不能配置为全0地址（0.0.0.0）、0.x.x.x地址、组播地址（224.x.x.x-255.x.x.x）、环回地址（127.x.x.x）、保留地址（240.x.x.x-255.x.x.x）以及全1的广播地址（255.255.255.255）。
＜distance-metric＞|配置静态路由的管理距离，相当于路由协议的优先级，值越小，优先级越高。缺省情况下静态路由的优先级高于动态路由，默认为1，但是通过设置可使动态路由优先于静态路由。采用1-255之间的整数。默认值为1。
＜metric-value＞|配置静态路由的路由度量，度量值越小表示路由越优。采用0-255之间的整数。默认值为0。
＜tag-value＞|配置静态路由的路由标识，主要用于routemap路由过滤规则。采用0-4294967295之间的整数。默认值为0。
enable|为静态路由关联bfd检测的使能开关。取消BFD检测，采用删除路由或者配置相同路由而不配置bfd选项的方式。缺省为不使能BFD。
＜distance-metric＞|配置静态路由的管理距离，相当于路由协议的优先级，值越小，优先级越高。缺省情况下静态路由的优先级高于动态路由，默认为1，但是通过设置可使动态路由优先于静态路由。采用1-255之间的整数。默认值为1。
＜metric-value＞|配置静态路由的路由度量，度量值越小表示路由越优。采用0-255之间的整数。默认值为0。
＜tag-value＞|配置静态路由的路由标识，主要用于routemap路由过滤规则。采用0-4294967295之间的整数。默认值为0。
＜track-name＞|为静态路由故障联动处理关联的track名称。取消联动关联检测，采用删除路由或者配置相同路由而不配置track选项的方式。采用1-31位字符串。缺省为不关联track检测对象。
＜description-name＞|静态路由的描述信息。采用1-64位字符串。缺省为没有描述信息。






No参数|描述
---|---
all|删除当前网络下的所有静态路由。








缺省 :

缺省情况下表示没有配置静态路由。 






使用说明 :

1、只有在设备配置了VPN（参见ip vrf配置命令）的情况下才可配置私网静态路由。2、配置静态路由关联track对象检测，只有在通过SAMGR（参见samgr配置命令）配置了track检测对象的情况下，配置的静态路由才可生效。3、仅配置出接口形式的静态路由不允许配置关联BFD检测。4、带global属性的静态路由（简称global路由）仅在某VPN下可以配置，而且仅允许配置下一跳形式，与此同时下一跳必须为公网下一跳。也即公网下配置静态路由不能指定该属性。5、当指定的出接口为以太网接口或三层VLAN接口时，建议配置下一跳，否则可能导致下层流量不通。6、在实际使用中不建议两侧均使用静态路由创建BFD会话，推荐一侧使用静态BFD会话。7、可配置的最大静态路由条目数由性能参数控制，目前在ROSNGV3.00.10版本默认可配置的最大数目为16K个。8、该命令一些参数之间存在的其他限制请参考参数说明。9、配置目的地址时可以采用网络地址前缀/前缀长的形式进行配置，配置效果与指定网络地址和掩码相同，show running-config以网络地址和掩码的形式呈现。






范例 :

1、发给网络99.0.0.0/8的包将被路由到拥有地址10.1.1.2的路由器：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2或者：ZXROSNG(config)#ip route 99.0.0.0/8 10.1.1.22、发给网络99.0.0.0/8的包将被从接口loopback1转发：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 loopback1或者：ZXROSNG(config)#ip route 99.0.0.0/8 loopback13、发给网络99.0.0.0/8的包将被从接口gei-0/1/0/1转发到拥有地址10.1.1.2地址的路由器ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 gei-0/1/0/1 10.1.1.2或者：ZXROSNG(config)#ip route 99.0.0.0/8 gei-0/1/0/1 10.1.1.24. 发给网络99.0.0.0/8的包将被负载均衡转发到拥有地址10.1.1.2和20.1.1.2的路由器ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 20.1.1.25. 发给网络99.0.0.0/8的包将被优先转发到拥有地址10.1.1.2的路由器：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2ZXROSNG(config#ip route 99.0.0.0 255.0.0.0 20.1.1.2 106、私网zte下配置公网下一跳10.1.1.2静态路由ZXROSNG(config)#ip route vrf zte 99.0.0.0 255.0.0.0 10.1.1.2 global或者：ZXROSNG(config)#ip route vrf zte 99.0.0.0/8 10.1.1.2 global7、配置一条管理口路由，下一跳为拥有地址10.1.1.2地址的路由器ZXROSNG(config)#ip route vrf mng 99.0.0.0 255.0.0.0 10.1.1.2或者：ZXROSNG(config)#ip route vrf mng 99.0.0.0/8 10.1.1.28、配置静态路由bfd检测：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2 bfd enable或者：ZXROSNG(config)#ip route 99.0.0.0/8 10.1.1.2 bfd enable取消此路由的bfd检测：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2或者：ZXROSNG(config)#ip route 99.0.0.0/8 10.1.1.29、配置静态路由track联动检测：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2 track test或者：ZXROSNG(config)#ip route 99.0.0.0/8 10.1.1.2 track test取消此路由的track联动检测：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2或者：ZXROSNG(config)#ip route 99.0.0.0/8 10.1.1.210、配置带permanent属性的静态路由：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2 permanent或者：ZXROSNG(config)#ip route 99.0.0.0/8 10.1.1.2 permanent取消此路由的permanent属性：ZXROSNG(config)#ip route 99.0.0.0 255.0.0.0 10.1.1.2或者：ZXROSNG(config)#ip route 99.0.0.0/8 10.1.1.211、删除公网下所有静态路由ZXROSNG(config)#no ip route all12、删除私网zte下所有静态路由ZXROSNG(config)#no ip route vrf zte all13、删除管理口下所有静态路由ZXROSNG(config)#no ip route vrf mng all14、删除公网下9.0.0.0网段的所有静态路由ZXROSNG(config)#no ip route 9.0.0.0 255.0.0.0或者：ZXROSNG(config)#no ip route 9.0.0.0/815、删除管理口下9.0.0.0网段、下一跳为10.1.1.2的静态路由ZXROSNG(config)#no ip route vrf mng 9.0.0.0 255.0.0.0 10.1.1.2或者：ZXROSNG(config)#no ip route vrf mng 9.0.0.0/8 10.1.1.2






相关命令 :

无 




## ip route-static bfd 


ip route-static bfd 




命令功能 :

配置IPv4静态路由的BFD模板。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ip route-static bfd 
  {＜interface-name 
＞|[vrf 
 ＜vrf-name 
＞] local-address 
 ＜Local address 
＞} nexthop 
 ＜Static route nexthop address 
＞ template 
 ＜template-name 
＞
no ip route-static bfd 
  {＜interface-name 
＞|[vrf 
 ＜vrf-name 
＞] local-address 
 ＜Local address 
＞} nexthop 
 ＜Static route nexthop address 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|IPv4静态路由指定的接口名。
＜vrf-name＞|VPN名称，范围1-32个字符。
＜Local address＞|IPv4静态路由的本端地址
＜Static route nexthop address＞|IPv4静态路由指定的下一跳地址。
＜template-name＞|BFD模板名，长度为1-31个字符








缺省 :

无。 






使用说明 :

使用场景：当配置静态路由的BFD需要指定多种配置参数时，可以通过配置BFD模板名实现该模板名下的BFD参数配置。注意事项：1.配置静态路由BFD模板的最大个数为$#134283310#$。2.配置BFD模板需要对应静态路由创建BFD会话成功才能生效。3.指定出接口和下一跳地址时配置的是单跳BFD会话模板，指定本端地址和下一跳地址时配置的是多跳BFD会话模板。






范例 :

1.配置一条IPv4静态路由的单跳BFD模板名为”$zte$”：ZXROSNG(config)#ip route-static bfd fei-0/1/0/1 nexthop 1.1.1.2 template $zte$2.配置一条IPv4静态路由的多跳BFD模板名为”!zte!”：ZXROSNG(config)#ip route-static bfd nexthop 2.2.2.2 local-address 1.1.1.1 template !zte!






相关命令 :

ip route 




## ip route-static update-delay 


ip route-static update-delay 




命令功能 :

配置静态路由延迟更新下发的时间。使用no命令关闭此功能。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ip route-static update-delay 
  ＜update-delay 
＞

no ip route-static update-delay 








命令参数解释 :



参数|描述
---|---
＜update-delay＞|延迟更新时间，范围0-1200（秒）








缺省 :

静态路由延迟下发关闭 






使用说明 :

1.静态路由延迟更新的应用场景为下层希望等网络稳定再下发静态路由更新信息。比如ECMP个数发生变化时，等待一个延迟时间，再下发最终结果。2.当最优路由从其他类型变为静态路由或从静态路由变为其他路由时，均直接下发不延迟。3.配置人员设置延迟更新时间时，应充分考虑网络拓扑，谨慎配置。






范例 :

配置静态路由延迟更新时间为5秒ZXROSNG(config)#ip route-static update-delay 5






相关命令 :

无 




## ip route-static 


ip route-static 




命令功能 :

该命令在全局配置模式下执行，用于使能静态路由FRR计算功能或使能静态路由保护动态协议功能。FRR（Fast ReRoute）是指在当网络中链路或者节点失效后，为这些重要的节点或链路提供备份保护，实现快速重路由，减少链路或节点失效时对流量的影响，使流量实现快速恢复。当需要为静态路由使能FRR路由计算功能或某些场景需要使能静态路由保护动态协议功能时使用该命令。当需要使能静态路由递归L3VPN路由功能时使用该命令。






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ip route-static 
  {vrf 
 ＜vrf-name 
＞ {fast-reroute 
 [wtr 
 ＜time-interval 
＞]|protect 
 {rip 
|ospf 
|bgp 
|isis 
}|recursion-l3vpn 
}|{fast-reroute 
 [wtr 
 ＜time-interval 
＞]|protect 
 {rip 
|ospf 
|bgp 
|isis 
}}}
no ip route-static 
  {vrf 
 ＜vrf-name 
＞ {fast-reroute 
|protect 
 {all 
|rip 
|ospf 
|bgp 
|isis 
}|recursion-l3vpn 
}|{fast-reroute 
|protect 
 {all 
|rip 
|ospf 
|bgp 
|isis 
}}}
				






命令参数解释 :



参数|描述
---|---
＜vrf-name＞|静态路由所属VPN的VRF名称。配置该参数，表示使能私网静态路由的FRR或保护动态协议路由功能；不配置该参数，使能公网静态路由的FRR或保护动态协议路由功能。VRF名称的取值长度为1-32位字符串。
fast-reroute|辅助参数，使能或去使能静态路由FRR标识。缺省情况下该功能为关闭状态。
＜time-interval＞|设置回切延迟的时间间隔WTR（frrWaitToRestore）。范围为0-12分钟。默认值为0分钟。
protect|辅助参数，使能或去使能静态路由保护动态协议路由功能。缺省情况下该功能为关闭状态。
rip|使能或去使能静态路由保护RIP路由标识，缺省情况下为不保护。
ospf|使能或去使能静态路由保护OSPF路由标识，缺省情况下为不保护。
bgp|使能或去使能静态路由保护BGP路由标识，缺省情况下为不保护。
isis|使能或去使能静态路由保护ISIS路由标识，缺省情况下为不保护。
recursion-l3vpn|使能或去使能静态路由递归L3VPN标识，缺省情况下为不使能。
fast-reroute|辅助参数，使能或去使能静态路由FRR标识。缺省情况下该功能为关闭状态。
＜time-interval＞|设置回切延迟的时间间隔WTR（frrWaitToRestore）。范围为0-12分钟。默认值为0分钟。
protect|辅助参数，使能或去使能静态路由保护动态协议路由功能。缺省情况下该功能为关闭状态。
rip|使能或去使能静态路由保护RIP路由标识，缺省情况下为不保护。
ospf|使能或去使能静态路由保护OSPF路由标识，缺省情况下为不保护。
bgp|使能或去使能静态路由保护BGP路由标识，缺省情况下为不保护。
isis|使能或去使能静态路由保护ISIS路由标识，缺省情况下为不保护。






No参数|描述
---|---
all|删除所有静态路由保护规则。
all|删除所有静态路由保护规则。








缺省 :

此功能为关闭状态 






使用说明 :

1、该命令与静态路由的配置命令（参见配置命令ip route）配合使用。2、当使能静态路由FRR功能时，主备路由都必须为静态路由，形成条件为备路由目的地址、掩码需与主路由一致，出接口和下一跳不能和主路由同时相同，优先级或metric需次于主路由。此外，黑洞路由（NULL口或LOOPBCAK口）之间、黑洞路由与普通路由之间、非permanent路由与permanent路由之间均不可以形成FRR关系。3、当使能静态路由保护动态协议功能时，主路由一定是动态协议路由（如RIP、OSPF、ISIS、BGP），备路由一定是静态路由。主路由不能为动态协议的DISCARD路由，而备路由不能为黑洞路由、global路由、permanent路由，备路由的优先级要低于动态协议路由。此外，主备路由的出接口和下一跳不能相同。4、目前FRR功能仅限于一主一备，当有多条路由形成负载均衡，则不会计算FRR；如有多条路由均满足备路由条件，也只会按一定规则选择其中一条。5、管理口静态路由不支持该功能。6、目前使能静态路由FRR命令在公网下或某VPN下仅可配置一条；静态路由保护动态协议路由命令在公网下或某VPN下最多支持同时配置4次，即可以同时使能保护RIP路由、BGP路由、OSPF路由和ISIS路由，也可仅保护其中的1种或2种或3种路由。7、静态路由支持递归L3VPN的场景需要使用该命令。但注意，该功能只能在私网下配置。






范例 :

1、使能公网静态路由FRR计算功能。ZXROSNG(config)#ip route-static fast-reroute2、使能公网静态路由保护RIP路由ZXROSNG(config)#ip route-static protect rip3、使能私网zte静态路由保护BGP路由ZXROSNG(config)#ip route-static vrf zte protect bgp4、去使能私网zte静态路由保护ISIS路由ZXROSNG(config)#no ip route-static vrf zte protect isis5、去使能公网静态路由保护所有配置的动态协议路由ZXROSNG(config)#no ip route-static protect all6、使能公网静态路由FRR计算功能，通过show命令观察主路由与备路由。配置过程：ZXROSNG(config)#ip route-static fast-reroute //开启FRRZXROSNG(config)#ip route 2.1.1.0 255.255.255.0 gei-0/1/0/1 metric 1ZXROSNG(config)#ip route 2.1.1.0 255.255.255.0 gei-0/1/0/2 metric 10配置验证： ZXROSNG(config)#show ip forwarding route 2.1.1.0                  IPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE;Status codes: *valid, >best;   Dest          Gw            Interface         Owner     Pri  Metric*> 2.1.1.0/24      192.168.1.101   gei-0/1/0/1         Static      1   1     ZXROSNG(config)#show ip forwarding backup route 2.1.1.0             IPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority,  M/S: Master/Slave,          Sta: Status;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE;Status codes: *valid, >best, M: Master, S: Slave, I: Inuse, U: Unuse;   Dest        Gw            Interface   Owner  Pri  Metric  M/S  Sta *> 2.1.1.0/24    192.168.1.101   gei-0/1/0/1  Static    1   1      M    I*  2.1.1.0/24    61.1.1.1        gei-0/1/0/2  Static    1   10     S    U7、使能公网静态路由保护BGP路由功能，通过show命令观察主路由与备路由。配置过程：先进行bgp协议相关配置，生成BGP路由ZXROSNG(config)#show ip proto r network 9.0.0.0 Heads: Dest = Destination, Prf\RoutePrf = Router preference,       Metric\RouteMetric = Router metricCodes: OSPF-3D = ospf-type3-discard, OSPF-5D = ospf-type5-discard, TE = rsvpte,       OSPF-7D = ospf-type7-discard, USER-I = user-ipaddr, RIP-D = rip-discard,       OSPF-E = ospf-ext, ASBR-V = asbr-vpn, GW-FWD = ps-busi, GW-UE = ps-user,       BGP-AD = bgp-aggr-discard, BGP-CE = bgp-confed-ext, NAT64 = sl-nat64-v4,       USER-N = user-network, USER-S = user-special, DHCP-S = dhcp-static,       DHCP-D = dhcp-dft, VES = video-enhanced-serviceMarks: *valid, >best, s-stale    Dest               NextHop         RoutePrf   RouteMetric Protocol*>  9.0.0.0/8          1.1.1.9         200        0           BGP-INT使能静态路由保护BGP路由功能，并配置静态路由优先级低于BGP路由ZXROSNG(config)#ip route-static protect bgpZXROSNG(config)#ip route 9.0.0.0 255.0.0.0 2.1.1.9 220 ZXROSNG(config)#show ip proto r network 9.0.0.0                                  Heads: Dest = Destination, Prf\RoutePrf = Router preference,       Metric\RouteMetric = Router metricCodes: OSPF-3D = ospf-type3-discard, OSPF-5D = ospf-type5-discard, TE = rsvpte,       OSPF-7D = ospf-type7-discard, USER-I = user-ipaddr, RIP-D = rip-discard,       OSPF-E = ospf-ext, ASBR-V = asbr-vpn, GW-FWD = ps-busi, GW-UE = ps-user,       BGP-AD = bgp-aggr-discard, BGP-CE = bgp-confed-ext, NAT64 = sl-nat64-v4,       USER-N = user-network, USER-S = user-special, DHCP-S = dhcp-static,       DHCP-D = dhcp-dft, VES = video-enhanced-serviceMarks: *valid, >best, s-stale    Dest               NextHop         RoutePrf   RouteMetric Protocol*>  9.0.0.0/8          1.1.1.9         200        0           BGP-INT *  9.0.0.0/8          2.1.1.9         220        0           Static查看备路由表ZXROSNG(config)#show ip forwarding backup route 9.0.0.0IPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority,  M/S: Master/Slave,          Sta: Status;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE;Status codes: *valid, >best, M: Master, S: Slave, I: Inuse, U: Unuse;   Dest               Gw              Interface       Owner  Pri Metric M/S Sta *> 9.0.0.0/8          1.1.1.9         gei-0/1/0/1     BGP    200 0      M   I*  9.0.0.0/8          2.1.1.9         gei-0/1/0/2     Static 220 0      S   U8、使能静态路由递归L3VPN功能。ZXROSNG(config)#ip route-static vrf zte recursion-l3vpn





相关命令 :

ip route 静态路由的配置命令。 




# 路由基础命令 
## debug ipv4-route 


debug ipv4-route 




命令功能 :

用于在特权模式开启ipv4-route模块的所有debug开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv4-route 
  [all 
]
no debug ipv4-route 
  [all 
]
				






命令参数解释 :



参数|描述
---|---
all|<作用>ipv4-route模块的所有debug开关<默认值>无








缺省 :

无 






使用说明 :

可以通过show debug ipv4-route命令查看是否开启此debug开关 






范例 :

1.开启ipv4-route的所有debug开关，可以通过show debug ipv4-route命令查看此开关是否被开启：ZXROSNG#debug ipv4-route all All ipv4-route debugging has been turned onZXROSNG#show debug ipv4-route COURIER:  Ipv4-Route debugging is onZXROSNG#
2.关闭ipv4-route的所有debug开关，可以通过show debug ipv4-route命令查看此开关是否被关闭：ZXROSNG#no debug ipv4-route all All ipv4-route debugging has been turned offZXROSNG#
ZXROSNG#show debug ipv4-route  ZXROSNG#






相关命令 :

无 




## ip max-routes 


ip max-routes 




命令功能 :

在全局配置模式下设置IPv4公网路由的最大路由条目和告警百分比。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ip max-routes 
  ＜max-routes 
＞ ＜warning-percent 
＞

no ip max-routes 








命令参数解释 :



参数|描述
---|---
＜max-routes＞|<作用>设置公网路由表中的最大路由条目<取值范围> 1-4294967295<默认值>无
＜warning-percent＞|<作用>设置公网路由表中的路由达到上限的百分比<取值范围> 1-100<默认值>无








缺省 :

无 






使用说明 :

1.如果用户配置了公网最大路由条目和告警百分比，一旦用户配置公网的路由表中路由总数第一次达到或者超过此告警值（最大路由条目*告警百分比）时给出告警提示，此后可以继续添加路由，但系统不会再次给出告警提示。在告警发生后，如果用户删除路由，使得公网路由表中的条目小于告警阀值，就会打印取消告警的信息；2.可以通过show running-config route-protocol-mgr命令查看配置的信息。






范例 :

1.配置最大路由条目为10，告警阀值为10%，即当路由条目超过1条时即打印告警：ZXROSNG(config)#show ip protocol routing Protocol routes:status codes: *valid, >best, i-internal, s-staleDest NextHop RoutePrf RouteMetric ProtocolZXROSNG(config)#ip max-routes 10 10ZXROSNG(config)#ip route 10.1.1.1 255.255.255.255 null1ZXROSNG(config)#ip route 10.1.1.2 255.255.255.255 null1 ZXROSNG(config)#
An alarm 200315 ID 11 level 5 occurred at 19:37:50 06-28-2018 sent by ZXR10 MPU-0/20/0%IP-GLOBAL-TABLE% Routes warning limit is reached.  Warning data:The routes warning limit of ip instance is reachedZXROSNG(config)#
ZXROSNG(config)#no ip route 10.1.1.2 255.255.255.255 null1ZXROSNG(config)#
An alarm 200315 ID 11 level 5 cleared at 19:39:51 06-28-2018 sent by ZXR10 MPU-0/20/0%IP-GLOBAL-TABLE% Routes warning limit is reached.  Warning data:The routes warning limit of ip instance is reachedZXROSNG(config)#
2.no命令执行后，不再对路由条目发告警；ZXROSNG(config)#no ip max-routes ZXROSNG(config)#
ZXROSNG(config)#ip route 10.1.1.2 255.255.255.255 null1ZXROSNG(config)#






相关命令 :

无 




## ip protocol convergence-priority 


ip protocol convergence-priority 




命令功能 :

设置路由协议收敛优先级。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ip protocol convergence-priority 
  [vrf 
 ＜vrf-name 
＞] {ospf 
|isis 
|bgp 
|rip 
} {critical 
|high 
|medium 
}
no ip protocol convergence-priority 
  [vrf 
 ＜vrf-name 
＞] {ospf 
|isis 
|bgp 
|rip 
}
				






命令参数解释 :



参数|描述
---|---
＜vrf-name＞|<作用> VRF名称。<取值范围>取值长度为1-32字符。
ospf|<作用>设置OSPF路由的收敛优先级。
isis|<作用>设置ISIS路由的收敛优先级。
bgp|<作用>设置BGP路由的收敛优先级。
rip|<作用>设置RIP路由的收敛优先级。
critical|<作用>设置收敛优先级为关键的。
high|<作用>设置收敛优先级为高的。
medium|<作用>设置收敛优先级为中等的。








缺省 :

无 






使用说明 :

1.收敛优先级critical> high> medium，这三个优先级的含义和ospf、isis内部配置的前缀优先级相同。2.如果不配置vrf的话，设置的是公网下协议的收敛优先级。3. 此收敛优先级的作用是不同优先级的前缀同时生成时尽量保证高优先级的前缀先到达转发面。






范例 :

1.配置公网ospf路由的协议收敛优先级为critical.ZXROSNG(config)#ip protocol convergence-priority ospf critical取消公网ospf路由的协议收敛优先级配置ZXROSNG(config)#no ip protocol convergence-priority ospf2.配置私网isis路由的协议收敛优先级为high.ZXROSNG(config)#ip protocol convergence-priority vrf zte isis high取消私网isis路由的协议收敛优先级配置ZXROSNG(config)#no ip protocol convergence-priority vrf zte isis






相关命令 :

无 




## ip-lsb 


ip-lsb 




命令功能 :

配置源IP和目的IP的低有效字节作为流量负荷分担的哈希因子 






命令模式 :

 负荷分担哈希key IPv6单板模式  






命令默认权限级别 :

15 






命令格式 :



ip-lsb 
 

no ip-lsb 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

(1)    在全局配置模式下通过load-sharing hash-key ipv6 命令进行全局或指定单板级别配置；(2)    在该模式下可以与ip-msb 同时配置生效；(3)    配置指定接口级别时，使用load-sharing hash-key ipv6 interface 进入负荷分担哈希key IPv6接口模式，通过该模式命令ip-lsb和ip-msb进行配置；(4)    配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-key ipv6ZXROSNG(config-ldsh-hk-ipv6-)#
ZXROSNG(config-ldsh-hk-ipv6-)#ip-lsb ZXROSNG(config-ldsh-hk-ipv6-)#






相关命令 :

(1)    load-sharing hash-key ipv6(2)    负荷分担哈希key IPv6模式ip-msb(3)    load-sharing hash-key ipv6 interface(4)    负荷分担哈希key IPv6接口模式ip-lsb(5)    负荷分担哈希key IPv6接口模式ip-msb



## ip-lsb 


ip-lsb 




命令功能 :

配置源IP和目的IP的低有效字节作为流量负荷分担的哈希因子 






命令模式 :

 负荷分担哈希key IPv6模式  






命令默认权限级别 :

15 






命令格式 :



ip-lsb 
 

no ip-lsb 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

(1)    在全局配置模式下通过load-sharing hash-key ipv6 命令进行全局或指定单板级别配置；(2)    在该模式下可以与ip-msb 同时配置生效；(3)    配置指定接口级别时，使用load-sharing hash-key ipv6 interface 进入负荷分担哈希key IPv6接口模式，通过该模式命令ip-lsb和ip-msb进行配置；(4)    配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-key ipv6ZXROSNG(config-ldsh-hk-ipv6-)#
ZXROSNG(config-ldsh-hk-ipv6-)#ip-lsb ZXROSNG(config-ldsh-hk-ipv6-)#






相关命令 :

(1)    load-sharing hash-key ipv6(2)    负荷分担哈希key IPv6模式ip-msb(3)    load-sharing hash-key ipv6 interface(4)    负荷分担哈希key IPv6接口模式ip-lsb(5)    负荷分担哈希key IPv6接口模式ip-msb



## ip-msb 


ip-msb 




命令功能 :

配置源IP和目的IP的高有效字节作为流量负荷分担的哈希因子 






命令模式 :

 负荷分担哈希key IPv6单板模式  






命令默认权限级别 :

15 






命令格式 :



ip-msb 
 

no ip-msb 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

(1)    在全局配置模式下通过load-sharing hash-key ipv6命令进行全局或指定单板级别配置；(2)    在该模式下可以与ip-lsb同时配置生效；(3)    配置指定接口级别时，使用load-sharing hash-key ipv6 interface进入负荷分担哈希key IPv6接口模式，通过该模式下命令ip-lsb和ip-msb进行配置；(4)    配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-key ipv6ZXROSNG(config-ldsh-hk-ipv6)#ZXROSNG(config-ldsh-hk-ipv6)#ip-msb ZXROSNG(config-ldsh-hk-ipv6)#





相关命令 :

(1)    load-sharing hash-key ipv6(2)    负荷分担哈希key IPv6模式ip-lsb(3)    load-sharing hash-key ipv6 interface(4)    负荷分担哈希key IPv6接口模式ip-lsb(5)    负荷分担哈希key IPv6接口模式ip-msb



## ip-msb 


ip-msb 




命令功能 :

配置源IP和目的IP的高有效字节作为流量负荷分担的哈希因子 






命令模式 :

 负荷分担哈希key IPv6模式  






命令默认权限级别 :

15 






命令格式 :



ip-msb 
 

no ip-msb 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

(1)    在全局配置模式下通过load-sharing hash-key ipv6命令进行全局或指定单板级别配置；(2)    在该模式下可以与ip-lsb同时配置生效；(3)    配置指定接口级别时，使用load-sharing hash-key ipv6 interface进入负荷分担哈希key IPv6接口模式，通过该模式下命令ip-lsb和ip-msb进行配置；(4)    配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-key ipv6ZXROSNG(config-ldsh-hk-ipv6)#ZXROSNG(config-ldsh-hk-ipv6)#ip-msb ZXROSNG(config-ldsh-hk-ipv6)#





相关命令 :

(1)    load-sharing hash-key ipv6(2)    负荷分担哈希key IPv6模式ip-lsb(3)    load-sharing hash-key ipv6 interface(4)    负荷分担哈希key IPv6接口模式ip-lsb(5)    负荷分担哈希key IPv6接口模式ip-msb



## ipv6 max-routes 


ipv6 max-routes 




命令功能 :

在全局配置模式下设置IPv6公网路由的最大路由条目和告警百分比。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 max-routes 
  ＜max-routes 
＞ ＜warning-percent 
＞

no ipv6 max-routes 








命令参数解释 :



参数|描述
---|---
＜max-routes＞|<作用>设置公网路由表中的最大路由条目<取值范围> 1-4294967295
＜warning-percent＞|<作用>设置公网路由表中的路由达到上限的百分比<取值范围> 1-100








缺省 :

无。 






使用说明 :

1.如果用户配置了公网最大路由条目和告警百分比，一旦用户公网的路由表中路由总数第一次达到或者超过此告警值（最大路由条目*告警百分比）时给出告警提示，此后可以继续添加路由，但系统不会再次给出告警提示。在告警发生后，如果用户删除路由，使得公网路由表中的条目小于告警阀值，就会打印取消告警的信息；2.可以通过show running-config route-protocol-mgr命令查看配置的信息。






范例 :

1.配置最大路由条目为10，告警阀值为20%，即当路由条目大于等于2条时打印告警：ZXROSNG(config)#ipv6 max-routes 10 20ZXROSNG(config)#ipv6 route 5601::/64 null1ZXROSNG(config)#ipv6 route 5602::/64 null1ZXROSNG(config)#An alarm 200319 ID 427 level 5 occurred at 01:32:26 09-13-2018 sent by ZXR10 MPU-0/20/0%IPV6-GLOBAL-TABLE% IPv6 routes warning limit is reached.  Warning data:The IPv6 routes warning limit of ip instance is reached
ZXROSNG(config)#2.no命令执行后，不再对路由条目发告警:ZXROSNG(config)#no ipv6 route 5602::/64 null1ZXROSNG(config)#An alarm 200319 ID 427 level 5 cleared at 21:48:14 09-13-2018 sent by ZXR10 MPU-0/20/0%IPV6-GLOBAL-TABLE% IPv6 routes warning limit is reached.  Warning data:The IPv6 routes warning limit of ip instance is reached






相关命令 :

无。 




## load-sharing bandwidth-unaware 


load-sharing bandwidth-unaware 




命令功能 :

负荷分担是否感知外层负荷分担带宽变化的开关 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



load-sharing bandwidth-unaware 
 

no load-sharing bandwidth-unaware 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

配置后，外层负荷分担带宽变化不影响内层负荷分担带宽默认是影响的。






范例 :

ZXROSNG(config)#load-sharing bgp bandwidth-unaware ?  <cr>ZXROSNG(config)#load-sharing bgp bandwidth-unaware ZXROSNG(config)#






相关命令 :

无 




## load-sharing hash-algorithm 


load-sharing hash-algorithm 




命令功能 :

配置流量负荷分担的哈希算法 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


load-sharing hash-algorithm 
  [＜Set board 
＞] {crc16 
|crc32 
}
no load-sharing hash-algorithm 
  [＜Set board 
＞]
				






命令参数解释 :



参数|描述
---|---
＜Set board＞|单板名称
crc16|CRC16算法
crc32|CRC32算法








缺省 :

无 






使用说明 :

(1)    未指定单板名称时为全局配置；(2)    配置的命令针对IPv4和IPv6都生效；(3)    指定接口级别配置时使用load-sharing hash-algorithm interface命令配置；(4)    CRC16与CRC32为互斥的，只能配置一种参数作为哈希的算法；(5)    配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-algorithm PFU-0/1 crc32 






相关命令 :

(1)    load-sharing hash-algorithm interface(2)    load-sharing hash-algorithm-level(3)    load-sharing hash-algorithm-level interface



## load-sharing hash-fields ipv4 


load-sharing hash-fields ipv4 




命令功能 :

根据不同类型的业务流量转发场景，配置IPv4流量负荷分担的哈希因子 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


load-sharing hash-fields ipv4 
  [＜Set board 
＞] {l3src 
|l3 
|l4 
}
no load-sharing hash-fields ipv4 
  [＜Set board 
＞]
				






命令参数解释 :



参数|描述
---|---
＜Set board＞|单板名称
l3src|哈希因子为源IP地址信息，即哈希算法的依据是接口上行流量的源IP地址。
l3|哈希因子为源IP地址和目的IP地址二元组信息，即哈希算法的依据是接口上行流量的源IP地址和目的IP地址。当接口板上行流量的源IP地址和目的IP地址分布较均匀时，推荐配置本参数。
l4|哈希因子为源IP地址、目的IP地址、源端口号、目的端口号和协议号，即哈希算法的依据是接口上行流量的源IP地址、目的IP地址、源端口号、目的端口号和协议号。当接口板上行流量的源IP地址和目的IP地址分布不均匀时，推荐配置本参数。








缺省 :

无 






使用说明 :

(1)    未指定单板名称时为全局配置；(2)    配置IPv6全局或者单板级别时使用load-sharing hash-fields ipv6进行配置；(3)    IPv4指定接口级别配置时使用load-sharing hash-fields ipv4 interface命令配置；(4)    IPv6指定接口级别配置时使用load-sharing hash-fields ipv6 interface命令配置；(5)    l3src、l3、l4为互斥的，只能配置其中一种类型参数作为哈希因子；(6)    配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-fields ipv4 PFU-0/1 l4 






相关命令 :

(1)    load-sharing hash-fields ipv6(2)    load-sharing hash-fields ipv4 interface(3)    load-sharing hash-fields ipv6 interface



## load-sharing hash-fields ipv6 


load-sharing hash-fields ipv6 




命令功能 :

根据不同类型的业务流量转发场景，配置IPv6流量负荷分担的哈希因子。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


load-sharing hash-fields ipv6 
  [＜Set board 
＞] {l3src 
|l3 
|l4 
}
no load-sharing hash-fields ipv6 
  [＜Set board 
＞]
				






命令参数解释 :



参数|描述
---|---
＜Set board＞|单板名称。
l3src|哈希因子为源IP地址信息，即哈希算法的依据是接口上行流量的源IP地址。
l3|哈希因子为源IP地址和目的IP地址二元组信息，即哈希算法的依据是接口上行流量的源IP地址和目的IP地址。当接口板上行流量的源IP地址和目的IP地址分布较均匀时，推荐配置本参数。
l4|哈希因子为源IP地址、目的IP地址、源端口号、目的端口号和协议号，即哈希算法的依据是接口上行流量的源IP地址、目的IP地址、源端口号、目的端口号和协议号。当接口板上行流量的源IP地址和目的IP地址分布不均匀时，推荐配置本参数。








缺省 :

无 






使用说明 :

(1)    未指定单板名称时为全局配置；(2)    IPv4全局或者指定单板级别配置时使用load-sharing hash-fields ipv4命令配置；(3)    IPv4指定接口级别配置时使用load-sharing hash-fields ipv4 interface命令配置；(4)    IPv6指定接口级别配置时使用load-sharing hash-fields ipv6 interface命令配置；(5)    l3src、l3、l4为互斥的，只能配置其中一种类型参数作为哈希因子；(6)    配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-fields ipv6 PFU-0/1 l4 






相关命令 :

(1)    load-sharing hash-fields ipv4(2)    load-sharing hash-fields ipv4 interface(3)    load-sharing hash-fields ipv6 interface



## load-sharing hash-fields mpls 


load-sharing hash-fields mpls 




命令功能 :

配置标签负荷分担哈希因子 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


load-sharing hash-fields mpls 
  [＜board 
＞] {ip-l3 
|ip-l4 
|label 
} [incoming-port-num 
]
no load-sharing hash-fields mpls 
  [＜board 
＞]
				






命令参数解释 :



参数|描述
---|---
＜board＞|单板名称，不输入默认整机生效。
ip-l3|哈希因子为源IP地址、目的IP地址、TTL、协议类型、VPNID五元组信息，即哈希算法的依据是接口上行流量的源IP地址、目的IP地址、TTL、协议类型、VPNID等参数作为因子计算的。当入口流量中五元组相关字段变化时推荐配置本参数。
ip-l4|哈希因子除了包括源IP地址、目的IP地址、TTL、Protocol、VPNID五元组信息外，还包括四层报文头中的目的与源端口号信息。当流量中这些字段发送变化时，尤其是带有TCP/UDP头部的报文推荐本参数。
label|哈希因子为入口MPLS流量的多层标签。当入口MPLS流量中mpls lable发送变化时，推荐本参数。
incoming-port-num|指定入接口端口号作为哈希因子。








缺省 :

无 






使用说明 :

(1)    未指定单板名称时为全局配置；(2)    配置的命令针对IPv4和IPv6都生效；(3)    指定接口级别配置时使用load-sharing hash-fields mpls interface命令配置；(4)    ip-l3、ip-l4、mpls为互斥的，只能配置其中一种类型参数作为哈希因子；(5)    配置生效次序是接口、单板、全局。





范例 :

1.指定单板PFU-0/1的MPLS哈希因子采用ip-l4：ZXROSNG(config)#load-sharing hash-fields mpls PFU-0/1 ip-l42.删除单板PFU-0/1的MPLS哈希因子：ZXROSNG(config)#no load-sharing hash-fields mpls PFU-0/1





相关命令 :

(1)    load-sharing hash-fields mpls interface 




## load-sharing hash-key ipv6 board 


load-sharing hash-key ipv6 board 




命令功能 :

根据不同类型的业务流量转发场景，配置单板级别作为流量负荷分担的哈希因子IPv6的流特征值。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


load-sharing hash-key ipv6 board 
  ＜Set board 
＞
no load-sharing hash-key ipv6 board 
  ＜Set board 
＞
				






命令参数解释 :



参数|描述
---|---
＜Set board＞|单板名称








缺省 :

无。 






使用说明 :

（1）配置指定单板级别时，在全局配置模式下使用load-sharing hash-key ipv6 board进入负荷分担哈希key IPv6单板模式，通过该模式下命令进行配置；（2）另有指定全局和接口级别的负荷分担哈希key IPv6配置命令，配置生效次序是接口、单板、全局。






范例 :

ZXROSNG(config)#load-sharing hash-key ipv6 board PFU-0/1ZXROSNG(config-ldsh-hk-ipv6-PFU-0/1)#






相关命令 :

（1）load-sharing hash-key ipv6（2）load-sharing hash-key ipv6 interface




## load-sharing hash-key ipv6 


load-sharing hash-key ipv6 




命令功能 :

指定全局流量负荷分担的哈希因子IPv6的流特征值。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



load-sharing hash-key ipv6 
 

no load-sharing hash-key ipv6 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

（1）在全局配置模式下通过该命令进入负荷分担哈希key IPv6模式，使用该模式下命令进行配置（2）另有指定接口级别和单板级别的负荷分担哈希key IPv6属性命令，配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-key ipv6 ZXROSNG(config-ldsh-hk-ipv6)#






相关命令 :

（1）load-sharing hash-key ipv6 interface（2）load-sharing hash-key ipv6 board



## load-sharing hash-key scramble 


load-sharing hash-key scramble 




命令功能 :

配置负荷分担哈希扰码数值 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



load-sharing hash-key scramble 
  ＜scramble 
＞

no load-sharing hash-key scramble 








命令参数解释 :



参数|描述
---|---
＜scramble＞|哈希扰码数值，范围为1-65535








缺省 :

无 






使用说明 :

(1)    未指定单板名称时为全局配置；(2)    配置的命令针对IPv4和IPv6都生效；(3)    指定接口级别配置时使用load-sharing hash-key scramble interface命令配置；(4)    配置生效次序是接口、单板、全局。





范例 :

ZXROSNG(config)#load-sharing hash-key scramble 1234ZXROSNG(config)#





相关命令 :

(1)    load-sharing hash-key scramble interface 




## load-sharing wtr 


load-sharing wtr 




命令功能 :

配置负荷分担延时切换时间 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



load-sharing wtr 
  ＜Set wtr time 
＞

no load-sharing wtr 








命令参数解释 :



参数|描述
---|---
＜Set wtr time＞|wtr时间








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#load-sharing wtr ?  <1-12>  Set wtr time(min)ZXROSNG(config)#load-sharing wtr 11?<1-12>   ZXROSNG(config)#load-sharing wtr 11ZXROSNG(config)#






相关命令 :

无 




## show all forwarding route 


show all forwarding route 




命令功能 :

显示所有IPv4公网、私网路由信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show all forwarding route 
  {ipv4 
} 







命令参数解释 :



参数|描述
---|---
ipv4|显示所有IPv4路由表。








缺省 :

无。 






使用说明 :

该命令用于故障时一键式收集路由信息，不建议在正常情况且系统存在大量路由时使用此命令。 






范例 :

ZXROSNG#show all forwarding route ipv4Global:Dest/mask          Gateway                       Interface          Owner1.1.1.1/32         1.1.1.1                       loopback1          Address2.2.2.2/32         12.12.12.22                   gei-0/1/2/1        OSPF12.12.12.0/24      12.12.12.11                   gei-0/1/2/1        Direct12.12.12.11/32     12.12.12.11                   gei-0/1/2/1        Address13.1.1.0/24        13.1.1.1                      fei-0/1/0/3        Direct13.1.1.1/32        13.1.1.1                      fei-0/1/0/3        Address14.1.1.0/24        14.1.1.1                      fei-0/1/0/4        Direct14.1.1.1/32        14.1.1.1                      fei-0/1/0/4        Address15.1.1.0/24        15.1.1.1                      fei-0/1/0/5        Direct15.1.1.1/32        15.1.1.1                      fei-0/1/0/5        Address16.1.1.0/24        16.1.1.1                      fei-0/1/0/6        Direct16.1.1.1/32        16.1.1.1                      fei-0/1/0/6        Address100.1.1.1/32       13.1.1.2                      fei-0/1/0/3        Static=============================================================================VRF name: 5VDest/mask          Gateway                       Interface          Owner11.22.16.16/32     11.22.16.16                   loopback2          Address=============================================================================VRF name: zteDest/mask          Gateway                       Interface          Owner111.111.111.111/32 111.111.111.111               loopback11         Address222.222.222.222/32 1111:1111:2222:2222:aaaa:bbbb $vxlan_tunnel2     BGP                   :cccc:dddd222.222.222.222/32 3333:4444:5555:6666:eeee:8888 $vxlan_tunnel1     BGP                   :9999:ffef=============================================================================VRF name: GGMDest/mask          Gateway                       Interface          Owner5.5.5.5/32         20.18.12.66                   gei-0/1/2/2        ISIS-L120.18.12.0/24      20.18.12.6                    gei-0/1/2/2        Direct20.18.12.6/32      20.18.12.6                    gei-0/1/2/2        Address222.222.222.222/32 20.18.12.66                   gei-0/1/2/2        OSPF=============================================================================VRF name: mngDest/mask          Gateway                       Interface          Owner10.0.0.0/8         192.168.100.1                 mgmt_eth           Static192.168.100.0/24   192.168.100.250               mgmt_eth           Direct192.168.100.250/32 192.168.100.250               mgmt_eth           Address=============================================================================ZXROSNG#域信息描述表：域             描述Global         公网路由VRF name       私网路由对应vrf名称Dest/mask      路由前缀，IP地址/掩码长度Gateway        路由下一跳，IPv4/IPv6地址形式Interface      路由出接口名称Owner          路由协议名称






相关命令 :

show ip forwarding routeshow ip forwarding route vrf <vrf-name>




## show debug ipv4-route 


show debug ipv4-route 




命令功能 :

用于在除用户模式外的其他所有模式下查看ipv4-route的debug开关是否打开。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug ipv4-route 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

1.开启ipv4-route debug开关，show命令显示如下ZXROSNG#show debug ipv4-route COURIER:Ipv4-Route debugging is onZXROSNG#
2.关闭ipv4-route debug开关，show命令显示如下ZXROSNG#show debug ipv4-route ZXROSNG#






相关命令 :

无 




## show fc forwarding-table vsan 


show fc forwarding-table vsan 




命令功能 :

以太网FCOE产品回显FC的转发路由信息表 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show fc forwarding-table vsan 
  ＜vasan id 
＞







命令参数解释 :



参数|描述
---|---
＜vasan id＞|vasan id号








缺省 :

无 






使用说明 :

无 






范例 :

switch#show fc forwarding-table vsan 5Total forwarding routes : 4 Destination/mask   Interface   0x040000/8         Vfc10    0x040000/8         Vfc20    0x040000/8         Vfc30    0x040000/8         Vfc40   





相关命令 :

无 




## show ip forwarding backup route vrf 


show ip forwarding backup route vrf 




命令功能 :

显示v4私网备路由 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding backup route vrf 
  ＜vpn-name 
＞ {[{＜network-address 
＞} [＜network-mask 
＞ {weak-match 
|exact-match 
}]]|[＜protocol-name 
＞]} 







命令参数解释 :



参数|描述
---|---
＜vpn-name＞|vrf名称
＜network-address＞|目的地址
＜network-mask＞|掩码
weak-match|最长匹配
exact-match|精确匹配
＜protocol-name＞|协议类型








缺省 :

无 






使用说明 :

无 






范例 :

1.ZXROSNG(config)#show ip forwarding backup route vrf zteIPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority,  M/S: Master/Slave,         Sta: Status;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best, M: Master, S: Slave, I: Inuse, U: Unuse, R: Relay,              W: WTR;    Dest               Gw              Interface                       Owner  Pri Metric M/S Sta*>  11.12.13.14/32     1.1.1.1         gei-0/1/0/4                     STAT-V 1   0      M   I*   11.12.13.14/32     2.2.2.2         gei-0/1/0/4                     STAT-V 100 0      S   U*>  12.12.13.18/32     1.1.1.1         gei-0/1/0/4                     STAT-V 1   0      M   U/W*   12.12.13.18/32     2.2.2.2         gei-0/1/0/4                     STAT-V 100 0      S   I域信息描述表：域    描述Dest    路由前缀，IP地址/掩码长度Gw    路由下一跳地址，IP地址形式Interface    路由出接口名称Owner    路由协议名称Pri    路由优先级Metric    路由度量值M/S    路由的主备状态，M表示为主路由，S表示为备路由Sta    路由的当前转发状态，I表示路由处于使用状态，U表示没有被使用，W表示处于WTR阶段2.主路由是迭代路由时显示实际转发路径ZXROSNG#show ip forwarding backup route vrf zteIPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority,  M/S: Master/Slave,         Sta: Status;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best, M: Master, S: Slave, I: Inuse, U: Unuse, R: Relay,              W: WTR;    Dest               Gw              Interface                       Owner  Pri Metric M/S Sta*>  2.2.2.2/32         10.10.1.2       gei-0/1/0/1                     Static 1   0      M   I*   2.2.2.2/32         20.20.2.2       gei-0/1/0/2                     Static 1   20     S   U*>  4.4.4.4/32         2.2.2.2         gei-0/1/0/1                     BGP    200 0      M   I*>  4.4.4.4/32         2.2.2.2         gei-0/1/0/2                     BGP    200 0      M   I*   4.4.4.4/32         6.6.6.6         gei-0/1/0/2                     BGP    200 0      S   U*>  6.6.6.6/32         20.20.2.2       gei-0/1/0/2                     Static 1   0      M   I*   6.6.6.6/32         10.10.1.2       gei-0/1/0/1                     Static 1   2      S   U  可以看到，4.4.4.4/32的BGP路由中，主路由下一跳是2.2.2.2，迭代出两个不同的出接口。






相关命令 :

无 




## show ip forwarding backup route 


show ip forwarding backup route 




命令功能 :

显示v4公网备路由 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding backup route 
  {[＜network-address 
＞ [＜network-mask 
＞ {weak-match 
|exact-match 
}]]|[＜protocol-name 
＞]} 







命令参数解释 :



参数|描述
---|---
＜network-address＞|目的地址
＜network-mask＞|掩码
weak-match|最长匹配
exact-match|精确匹配
＜protocol-name＞|协议类型








缺省 :

无 






使用说明 :

无 






范例 :

1.ZXROSNG(config)#show ip forwarding backup routeIPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority,  M/S: Master/Slave,         Sta: Status;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best, M: Master, S: Slave, I: Inuse, U: Unuse, R: Relay, W: WTR;    Dest               Gw              Interface                       Owner  Pri Metric M/S Sta*>  4.4.4.4/32         30.1.1.2        gei-0/1/0/1                     Static 1   0      M   I*   4.4.4.4/32         40.1.1.2        gei-0/1/0/2                     Static 100 0      S   U*>  6.2.2.2/32         30.1.1.2        gei-0/1/0/1                     Static 1   0      M   U/W*   6.2.2.2/32         40.1.1.2        gei-0/1/0/2                     Static 100 0      S   I域信息描述表：域    描述Dest    路由前缀，IP地址/掩码长度Gw    路由下一跳地址，IP地址形式Interface    路由出接口名称Owner    路由协议名称Pri    路由优先级Metric    路由度量值M/S    路由的主备状态，M表示为主路由，S表示为备路由Sta    路由的当前转发状态，I表示路由处于使用状态，U表示没有被使用，W表示处于WTR阶段2.主路由是迭代路由时显示实际转发路径ZXROSNG(config)#show ip forwarding backup routeIPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority,  M/S: Master/Slave, Sta: Status;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best, M: Master, S: Slave, I: Inuse, U: Unuse, R: Relay, W: WTR;    Dest               Gw              Interface                       Owner  Pri Metric M/S Sta*>  2.2.2.2/32         10.10.1.2       gei-0/1/0/1                     Static 1   0      M   I*   2.2.2.2/32         20.20.2.2       gei-0/1/0/2                     Static 1   20     S   U*>  4.4.4.4/32         2.2.2.2         gei-0/1/0/1                     BGP    200 0      M   I*>  4.4.4.4/32         2.2.2.2         gei-0/1/0/2                     BGP    200 0      M   I*   4.4.4.4/32         6.6.6.6         gei-0/1/0/2                     BGP    200 0      S   U*>  6.6.6.6/32         20.20.2.2       gei-0/1/0/2                     Static 1   0      M   I*   6.6.6.6/32         10.10.1.2       gei-0/1/0/1                     Static 1   2      S   U  可以看到，4.4.4.4/32的BGP路由中，主路由下一跳是2.2.2.2，迭代出两个不同的出接口。






相关命令 :

无 




## show ip forwarding route summary all 


show ip forwarding route summary all 




命令功能 :

显示IPv4公网路由和各VRF下路由数目，与show ip forwarding route summary相比，包括了组播路由和广播路由。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding route summary all 
 







命令参数解释 :


					无
				 






缺省 :

无。 






使用说明 :

无。 






范例 :

R1#show ip forwarding route summary all IPv4 route prefix capacity: 1048576IPv4 total route prefix count: 79IPv4 global route prefix count: 3IPv4 VRF ospf61 route prefix count: 25IPv4 VRF ospf23 route prefix count: 22IPv4 VRF ospf45 route prefix count: 22IPv4 VRF mng route prefix count: 7





相关命令 :

无。 




## show ip forwarding route summary global 


show ip forwarding route summary global 




命令功能 :

显示v4公网路由数目 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding route summary global 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ip forwarding route summary  global The total routes of the global:Route Source   Countstatic:           4direct:           3martian:          0address:          4ospf:             1bgp:              0rip:              0isis_level1:      0isis_level2:      0icmp:             0snmp:             0nat:              0pat:              0vrrp:             0ppp:              0asbrvpn:          0rsvpte:           0user_ipaddr:      0user_network:     0static_vrf:       0ipsec:            0perVrf_label:     0ps_busi:          0ps_user:          0ldp_area:         0user_special:     0dhcp_dft:         0dhcp_static:      0nat64_sl:         0ves:              0bras-pool:        0hagp:             0nat-mask:         0dyn-leasedline:   0Total:            12ZXROSNG(config)#






相关命令 :

无 




## show ip forwarding route summary vrf 


show ip forwarding route summary vrf 




命令功能 :

显示v4私网路由数目 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding route summary vrf 
  ＜vpn-name 
＞ 







命令参数解释 :



参数|描述
---|---
＜vpn-name＞|vrf名称，长度1~32个字符








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ip forwarding route summary  vrf zteThe total routes of the vpn:Route Source   Countstatic:           0direct:           2martian:          0address:          2ospf:             0bgp:              0rip:              0isis_level1:      0isis_level2:      0icmp:             0snmp:             0nat:              0pat:              0vrrp:             0ppp:              0asbrvpn:          0rsvpte:           0user_ipaddr:      0user_network:     0static_vrf:       1ipsec:            0perVrf_label:     0ps_busi:          0ps_user:          0ldp_area:         0user_special:     0dhcp_dft:         0dhcp_static:      0nat64_sl:         0ves:              0bras-pool:        0hagp:             0nat-mask:         0dyn-leasedline:   0Total:            5






相关命令 :

无 




## show ip forwarding route summary 


show ip forwarding route summary 




命令功能 :

显示v4公私网路由数目 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding route summary 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ip forwarding route summaryThe total routes of global and all VPNs:Route Source   Countstatic:           0direct:           3martian:          0address:          3ospf:             0bgp:              0rip:              0isis-level1:      0isis-level2:      0icmp:             0snmp:             0nat:              0pat:              0vrrp:             0ppp:              0asbrvpn:          0rsvpte:           0user-ipaddr:      0user-network:     0static-vrf:       0ipsec:            0perVrf-label:     0ps-busi:          0ps-user:          0ldp-area:         0user-special:     0dhcp-dft:         0dhcp-static:      0nat64-sl:         0ves:              0bras-pool:        0hagp:             0nat-mask:         0dyn-leasedline:   0Total:            6 ZXROSNG(config)#





相关命令 :

无 




## show ip forwarding route vrf 


show ip forwarding route vrf 




命令功能 :

显示IPv4私网路由 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding route vrf 
  ＜vpn-name 
＞ {[＜network-address 
＞ {[detail 
]|[＜network-mask 
＞ {detail 
|{weak-match 
|exact-match 
 [detail 
]}}]}]|[＜protocol-name 
＞]} 







命令参数解释 :



参数|描述
---|---
＜vpn-name＞|VRF名称，长度为1–32位字符串，不包含空格，区分大小写。
＜network-address＞|目的地址
detail|显示路由详细信息
＜network-mask＞|掩码
detail|显示路由详细信息
weak-match|最长匹配
exact-match|精确匹配
detail|显示路由详细信息
＜protocol-name＞|协议类型








缺省 :

无 






使用说明 :

无 






范例 :

1.显示zte私网的IPv4路由：ZXROSNG(config)#show ip forwarding route vrf zteIPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAG: Hybrid-access-gateway;Status codes: *valid, >best;   Dest               Gw              Interface           Owner       Pri Metric*> 11.12.13.14/32     1.1.1.1         gei-0/1/0/4         STAT-V      1   0     *> 70.1.1.0/24        70.1.1.1        gei-0/1/0/7         Direct      0   0     *> 70.1.1.1/32        70.1.1.1        gei-0/1/0/7         Address     0   0     *> 80.1.1.0/24        80.1.1.1        gei-0/1/0/8         Direct      0   0     *> 80.1.1.1/32        80.1.1.1        gei-0/1/0/8         Address     0   0     ZXROSNG(config)#域信息描述表：域                描述Dest              路由前缀，IP地址/掩码长度Gw                路由下一跳，IP地址形式Interface         路由出接口名称Owner             路由协议名称Pri               路由优先级Metric            路由度量值2.显示zte私网路由详细信息ZXROSNG(config)#show ip forwarding route vrf zte 2.0.0.0 255.0.0.0 exact-match detail 2016/12/07 02:44:44.122.0.0.0/8  via 1.1.1.3, static, relay, distance 1, metric 0    path-index 1    next-hop 1.1.1.3, via 1.1.1.0/24     [1] 10.1.1.2 gei-0/1/0/8     [2] 101.1.1.2 gei-0/1/0/1  via 10.1.1.2, static, distance 1, metric 0    path-index 2    next-hop 10.1.1.2, via 0.0.0.0/0     [3] 10.1.1.2 gei-0/1/0/8  via 101.1.1.2, distance 1, metric 0    path-index 3    next-hop 101.1.1.2, via 0.0.0.0/0     [4] 101.1.1.2 gei-0/1/0/1域信息描述表：域                                         描述2016/12/07 02:44:44.12            命令执行日期和时间2.0.0.0/8                         路由前缀信息via 1.1.1.3                       前缀下具体一条路由的下一跳static                            该前缀的当前路由类型relay                             当前路由下一跳需要解析path-index                        路径索引编号next-hop 10.1.1.2, via 0.0.0.0/0  当前路由的下一跳，如果是解析的via后是解析到的本地路由，非解析则via后为0.0.0.0/0[1]                               当前在用转发路径的编号。10.1.1.2 gei-0/1/0/8              实际转发路径中的下一跳及出接口3.按路由类型过滤显示ZXROSNG(config)#show ip forwarding route vrf pss123 static Routes:  3            Route-paths:  5IPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best, R: Relay;    Dest               Gw              Interface          Owner       Pri Metric*>  2.0.0.0/8          0.0.0.0         null1              Static      1   0     *>  3.0.0.0/8          1.1.1.2         gei-0/1/0/1        Static      1   0     *>R 4.0.0.0/8          6.0.0.1         gei-0/1/0/2        Static      1   0     *>R 4.0.0.0/8          6.0.0.3         gei-0/1/0/2        Static      1   0 域信息描述表：域             描述Dest           路由前缀，IP地址/掩码长度Gw            路由下一跳，IP地址形式Interface       路由出接口名称Owner         路由协议名称Pri            路由优先级Metric         路由度量值Routes         路由前缀总数Route-paths    路由的路径总数4.显示迭代路由的实际转发路径ZXROSNG#show ip forwarding route vrf zteIPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best, R: Relay;    Dest               Gw              Interface          Owner       Pri Metric*>  1.1.1.1/32         1.1.1.1         loopback1          Address     0   0     *>  2.2.2.2/32         10.10.1.2       gei-0/1/0/1        Static      1   0     *>  3.3.3.3/32         3.3.3.3         loopback2          Address     0   0     *>  4.4.4.4/32         2.2.2.2         gei-0/1/0/1        BGP         200 0     *>  4.4.4.4/32         2.2.2.2         gei-0/1/0/2        BGP         200 0     *>  5.5.5.5/32         5.5.5.5         loopback3          Address     0   0     *>  6.6.6.6/32         20.20.2.2       gei-0/1/0/2        Static      1   0     *>  10.10.1.0/24       10.10.1.1       gei-0/1/0/1        Direct      0   0     *>  10.10.1.1/32       10.10.1.1       gei-0/1/0/1        Address     0   0     *>  20.20.2.0/24       20.20.2.1       gei-0/1/0/2        Direct      0   0     *>  20.20.2.1/32       20.20.2.1       gei-0/1/0/2        Address     0   0  其中，4.4.4.4/32的BGP路由下一跳2.2.2.2迭代出两条路径，出接口分别为gei-0/1/0/1和gei-0/1/0/2。






相关命令 :

无 




## show ip forwarding route 


show ip forwarding route 




命令功能 :

显示IPv4公网路由 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding route 
  {[＜network-address 
＞ {[detail 
]|[＜network-mask 
＞ {detail 
|{weak-match 
|exact-match 
 [detail 
]}}]}]|[＜protocol-name 
＞]} 







命令参数解释 :



参数|描述
---|---
＜network-address＞|目的地址
detail|显示路由详细信息
＜network-mask＞|掩码
detail|显示路由详细信息
weak-match|最长匹配
exact-match|精确匹配
detail|显示路由详细信息
＜protocol-name＞|协议








缺省 :

无 






使用说明 :

无 






范例 :

1.显示IPv4公网路由：ZXROSNG(config)#show ip forwarding routeIPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best;   Dest               Gw              Interface           Owner       Pri Metric*> 1.1.1.1/32         40.1.1.2        gei-0/1/0/4         Static      20  0       *> 2.2.2.2/32         40.1.1.2        gei-0/1/0/4         Static      1   0       *> 3.3.3.3/32         30.1.1.2        gei-0/1/0/3         Static      1   0       *> 4.4.4.4/32         30.1.1.2        gei-0/1/0/3         Static      1   0       *> 6.1.1.0/24         6.1.1.1         te_tunnel1          Direct      0   0       *> 6.1.1.1/32         6.1.1.1         te_tunnel1          Address     0   0       *> 30.1.1.0/24        30.1.1.1        gei-0/1/0/3         Direct      0   0       *> 30.1.1.1/32        30.1.1.1        gei-0/1/0/3         Address     0   0       *> 40.1.1.0/24        40.1.1.1        gei-0/1/0/4         Direct      0   0       *> 40.1.1.1/32        40.1.1.1        gei-0/1/0/4         Address     0   0       *> 100.1.1.1/32       100.1.1.1       loopback1           Address     0   0       *> 200.1.1.1/32       6.1.1.1         te_tunnel1          OSPF        110 2       *> 1.1.1.1/32         40.1.1.2        gei-0/1/0/4         Static      20  0     *> 2.2.2.2/32         40.1.1.2        gei-0/1/0/4         Static      1   0     *> 3.3.3.3/32         30.1.1.2        gei-0/1/0/3         Static      1   0     *> 4.4.4.4/32         30.1.1.2        gei-0/1/0/3         Static      1   0     *> 6.1.1.0/24         6.1.1.1         te_tunnel1          Direct      0   0     *> 6.1.1.1/32         6.1.1.1         te_tunnel1          Address     0   0     *> 30.1.1.0/24        30.1.1.1        gei-0/1/0/3         Direct      0   0     *> 30.1.1.1/32        30.1.1.1        gei-0/1/0/3         Address     0   0     *> 40.1.1.0/24        40.1.1.1        gei-0/1/0/4         Direct      0   0     *> 40.1.1.1/32        40.1.1.1        gei-0/1/0/4         Address     0   0     *> 100.1.1.1/32       100.1.1.1       loopback1           Address     0   0     *> 200.1.1.1/32       6.1.1.1         te_tunnel1          OSPF        110 2     ZXROSNG(config)#域信息描述表：域             描述Dest           路由前缀，IP地址/掩码长度Gw             路由下一跳，IP地址形式Interface      路由出接口名称Owner          路由协议名称Pri            路由优先级Metric         路由度量值2.显示路由详细信息ZXROSNG(config)#show ip forwarding route 2.0.0.0 255.0.0.0 exact-match detail 2016/12/07 02:44:44.122.0.0.0/8  via 1.1.1.3, static, relay, distance 1, metric 0    path-index 1    next-hop 1.1.1.3, via 1.1.1.0/24     [1] 10.1.1.2 gei-0/1/0/8     [2] 101.1.1.2 gei-0/1/0/1  via 10.1.1.2, static, distance 1, metric 0    path-index 2    next-hop 10.1.1.2, via 0.0.0.0/0     [3] 10.1.1.2 gei-0/1/0/8  via 101.1.1.2, static, distance 1, metric 0    path-index 3    next-hop 101.1.1.2, via 0.0.0.0/0     [4] 101.1.1.2 gei-0/1/0/1域信息描述表：域                                    描述2016/12/07 02:44:44.12        命令执行日期和时间2.0.0.0/8                     路由前缀信息via 1.1.1.3                   前缀下具体一条路由的下一跳static                        当前路由类型relay                         当前路由下一跳需要解析path-index                    路径索引编号next-hop 10.1.1.2, via 0.0.0.0/0       当前路由的下一跳，如果是解析的via后是解析到的本地路由，非解析则via后为0.0.0.0/0[1]                           当前在用转发路径的编号。10.1.1.2 gei-0/1/0/8          实际转发路径中的下一跳及出接口3.按路由类型过滤显示ZXROSNG(config)#show ip forwarding route static Routes:  3            Route-paths:  5IPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best, R: Relay;    Dest               Gw              Interface          Owner       Pri Metric*>  2.0.0.0/8          0.0.0.0         null1              Static      1   0     *>  3.0.0.0/8          1.1.1.2         gei-0/1/0/1        Static      1   0     *>R 4.0.0.0/8          6.0.0.1         gei-0/1/0/2        Static      1   0     *>R 4.0.0.0/8          6.0.0.3         gei-0/1/0/2        Static      1   0 域信息描述表：域             描述Dest           路由前缀，IP地址/掩码长度Gw            路由下一跳，IP地址形式Interface       路由出接口名称Owner         路由协议名称Pri            路由优先级Metric         路由度量值Routes         路由前缀总数Route-paths    路由的路径总数4.显示迭代路由的实际转发路径ZXROSNG#show ip forwarding route vrf zteIPv4 Routing Table:Headers: Dest: Destination,  Gw: Gateway,  Pri: Priority;Codes  : BROADC: Broadcast, USER-I: User-ipaddr, USER-S: User-special,         MULTIC: Multicast, USER-N: User-network, DHCP-D: DHCP-DFT,         ASBR-V: ASBR-VPN, STAT-V: Static-VRF, DHCP-S: DHCP-static,         GW-FWD: PS-BUSI, NAT64: Stateless-NAT64, LDP-A: LDP-area,         GW-UE: PS-USER, P-VRF: Per-VRF-label, TE: RSVP-TE,         BP: BRAS-pool, HAGP: Hybrid-access-gateway-protocol;Status codes: *valid, >best, R: Relay;    Dest               Gw              Interface          Owner       Pri Metric*>  1.1.1.1/32         1.1.1.1         loopback1          Address     0   0     *>  2.2.2.2/32         10.10.1.2       gei-0/1/0/1        Static      1   0     *>  3.3.3.3/32         3.3.3.3         loopback2          Address     0   0     *>  4.4.4.4/32         2.2.2.2         gei-0/1/0/1        BGP         200 0     *>  4.4.4.4/32         2.2.2.2         gei-0/1/0/2        BGP         200 0     *>  5.5.5.5/32         5.5.5.5         loopback3          Address     0   0     *>  6.6.6.6/32         20.20.2.2       gei-0/1/0/2        Static      1   0     *>  10.10.1.0/24       10.10.1.1       gei-0/1/0/1        Direct      0   0     *>  10.10.1.1/32       10.10.1.1       gei-0/1/0/1        Address     0   0     *>  20.20.2.0/24       20.20.2.1       gei-0/1/0/2        Direct      0   0     *>  20.20.2.1/32       20.20.2.1       gei-0/1/0/2        Address     0   0  其中，4.4.4.4/32的BGP路由下一跳2.2.2.2迭代出两条路径，出接口分别为gei-0/1/0/1和gei-0/1/0/2。






相关命令 :

无 




## show ip forwarding route-path summary 


show ip forwarding route-path summary 




命令功能 :

显示v4公私网路由出向链路数目 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip forwarding route-path summary 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ip forwarding route-path summary The total active and backup route-paths of global and all VPNs:Route Source   Countstatic:           7direct:           6broadcast:        3multicast:        6martian:          0address:          7ospf:             1bgp:              0rip:              0isis_level1:      0isis_level2:      0icmp:             0snmp:             0nat:              0pat:              0vrrp:             0ppp:              0asbrvpn:          0rsvpte:           0user_ipaddr:      0user_network:     0static_vrf:       0ipsec:            0perVrf_label:     0ps_busi:          0ps_user:          0ldp_area:         0user_special:     0dhcp_dft:         0dhcp_static:      0nat64_sl:         0ves:              0bras-pool:        0hagp:             0Total:            30






相关命令 :

无 




## show ip protocol routing 


show ip protocol routing 




命令功能 :

该命令用于查看IPv4路由协议表的路由条目信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip protocol routing 
  {summary 
|vrf-summary 
 ＜vrf-name 
＞|detail 
 [vrf 
 ＜vrf-name 
＞] {latest 
|[＜protocol 
＞] [{[network 
 ＜ipv4-address 
＞ [mask 
 ＜ipv4-address-mask 
＞]]|all 
}]}|[{[vrf 
 ＜vrf-name 
＞] [＜protocol 
＞]|migp 
 [{isis-l1 
|isis-l2 
|ospf 
}]}] [{[network 
 ＜ipv4-address 
＞ [mask 
 ＜ipv4-address-mask 
＞]]|all 
}]} 







命令参数解释 :



参数|描述
---|---
summary|<作用>查看IPv4路由协议表的公网路由条目总数。
vrf-summary|<作用>辅助参数，用于查看IPv4路由协议表的私网网路由条目总数。
＜vrf-name＞|<作用> 查看指定VPN下的路由条目。<取值范围> VRF名称的取值长度为1-32字符。<默认值> 无
detail|<作用> 查看指定路由条目的详细信息。<默认值> 无
＜vrf-name＞|<作用> 查看指定VPN下的路由条目。<取值范围> VRF名称的取值长度为1-32字符。<默认值> 无
latest|<作用> 显示最近变化的路由。<默认值> 无
＜protocol＞|<作用> 指定路由的协议类型查看路由信息。<取值范围>目前支持指定的路由类型有目前DHCP-dft路由、BGP路由、直连和地址路由、DHCP-static路由、ISIS路由、LDP路由、NAT路由、NAT-PT路由、OSPF路由、PPP路由、Ps-busi_addr路由、Ps-user_addr路由、RIP路由、User special路由、stateless NAT64路由、静态路由、用户路由、视频路由、VRRP路由等。<默认值> 无
＜ipv4-address＞|<作用>点分十进制，指定要显示的路由的目的网络前缀，模糊匹配<默认值> 无
＜ipv4-address-mask＞|<作用>点分十进制，指定要显示的路由的目的网络前缀及掩码，精确匹配<默认值>无
all|<作用>显示协议表中的所有路由<默认值>无
＜vrf-name＞|<作用> 查看指定VPN下的路由条目。<取值范围> VRF名称的取值长度为1-32字符。<默认值> 无
＜protocol＞|<作用> 指定路由的协议类型查看路由信息。<取值范围>目前支持指定的路由类型有目前DHCP-dft路由、BGP路由、直连和地址路由、DHCP-static路由、ISIS路由、LDP路由、NAT路由、NAT-PT路由、OSPF路由、PPP路由、Ps-busi_addr路由、Ps-user_addr路由、RIP路由、User special路由、stateless NAT64路由、静态路由、用户路由、视频路由、VRRP路由等。<默认值> 无
migp|<作用> 显示协议表中的具有migp属性的路由。<默认值> 无
isis-l1|<作用> 指定ISIS层一路由。<默认值> 无
isis-l2|<作用> 指定ISIS层二路由。<默认值> 无
ospf|<作用> 指定OSPF路由。<默认值> 无
＜ipv4-address＞|<作用>点分十进制，指定要显示的路由的目的网络前缀，模糊匹配<默认值> 无
＜ipv4-address-mask＞|<作用>点分十进制，指定要显示的路由的目的网络前缀及掩码，精确匹配<默认值>无
all|<作用>显示协议表中的所有路由<默认值>无








缺省 :

显示路由协议表中公网下的所有有效路由； 






使用说明 :

show ip protocol routing [[network]<A.B.C.D> [<A.B.C.D>]]命令带掩码长度时显示与指定目的网络号和掩码精确匹配的路由的详细信息，不带掩码时显示与指定目的网络号最长匹配的路由的信息。 






范例 :

1. show ip protocol routing, 显示公网下的所有有效路由：ZXROSNG(config)#show ip protocol  routing        Heads: Dest = Destination, Prf\RoutePrf = Router preference,       Metric\RouteMetric = Router metricCodes: OSPF-3D = ospf-type3-discard, OSPF-5D = ospf-type5-discard, TE = rsvpte,       OSPF-7D = ospf-type7-discard, USER-I = user-ipaddr, RIP-D = rip-discard,       OSPF-E = ospf-ext, ASBR-V = asbr-vpn, GW-FWD = ps-busi, GW-UE = ps-user,       BGP-AD = bgp-aggr-discard, BGP-CE = bgp-confed-ext, NAT64 = sl-nat64-v4,       USER-N = user-network, USER-S = user-special, DHCP-S = dhcp-static,       DHCP-D = dhcp-dft, VES = video-enhanced-service, HAGP = hybrid-access-gateway-protocolMarks: *valid, >best, s-stale    Dest               NextHop         RoutePrf   RouteMetric Protocol*>  1.1.1.0/24         1.1.1.1         0          0           direct*>  1.1.1.1/32         1.1.1.1         0          0           address2. show ip protocol routing all, 显示公网中的所有路由：ZXROSNG(config)#show ip protocol  routing allHeads: Dest = Destination, Prf\RoutePrf = Router preference,       Metric\RouteMetric = Router metricCodes: OSPF-3D = ospf-type3-discard, OSPF-5D = ospf-type5-discard, TE = rsvpte,       OSPF-7D = ospf-type7-discard, USER-I = user-ipaddr, RIP-D = rip-discard,       OSPF-E = ospf-ext, ASBR-V = asbr-vpn, GW-FWD = ps-busi, GW-UE = ps-user,       BGP-AD = bgp-aggr-discard, BGP-CE = bgp-confed-ext, NAT64 = sl-nat64-v4,       USER-N = user-network, USER-S = user-special, DHCP-S = dhcp-static,       DHCP-D = dhcp-dft, VES = video-enhanced-service, HAGP = hybrid-access-gateway-protocolMarks: *valid, >best, s-stale    Dest               NextHop         RoutePrf   RouteMetric Protocol*>  1.1.1.0/24         1.1.1.1         0          0           direct*>  1.1.1.1/32         1.1.1.1         0          0           address >  10.1.1.1/32        0.0.0.0         1          0           static 3. show ip protocol routing network+前缀, 显示某网段的路由；ZXROSNG(config)#show ip protocol routing network 1.1.1.0Heads: Dest = Destination, Prf\RoutePrf = Router preference,       Metric\RouteMetric = Router metricCodes: OSPF-3D = ospf-type3-discard, OSPF-5D = ospf-type5-discard, TE = rsvpte,       OSPF-7D = ospf-type7-discard, USER-I = user-ipaddr, RIP-D = rip-discard,       OSPF-E = ospf-ext, ASBR-V = asbr-vpn, GW-FWD = ps-busi, GW-UE = ps-user,       BGP-AD = bgp-aggr-discard, BGP-CE = bgp-confed-ext, NAT64 = sl-nat64-v4,       USER-N = user-network, USER-S = user-special, DHCP-S = dhcp-static,       DHCP-D = dhcp-dft, VES = video-enhanced-service, HAGP = hybrid-access-gateway-protocol     Marks: *valid, >best, s-stale    Dest               NextHop         RoutePrf   RouteMetric Protocol*>  1.1.1.0/24         1.1.1.1         0          0           direct*>  1.1.1.1/32         1.1.1.1         0          0           address4. show ip protocol routing network+前缀和掩码, 显示公网下的协议表中的路由某条具体路由信息：ZXROSNG(config)#show ip protocol routing network 1.1.1.0 mask 255.255.255.0Heads: Dest = Destination, Prf\RoutePrf = Router preference,       Metric\RouteMetric = Router metricCodes: OSPF-3D = ospf-type3-discard, OSPF-5D = ospf-type5-discard, TE = rsvpte,       OSPF-7D = ospf-type7-discard, USER-I = user-ipaddr, RIP-D = rip-discard,       OSPF-E = ospf-ext, ASBR-V = asbr-vpn, GW-FWD = ps-busi, GW-UE = ps-user,       BGP-AD = bgp-aggr-discard, BGP-CE = bgp-confed-ext, NAT64 = sl-nat64-v4,       USER-N = user-network, USER-S = user-special, DHCP-S = dhcp-static,       DHCP-D = dhcp-dft, VES = video-enhanced-service, HAGP = hybrid-access-gateway-protocol      Marks: *valid, >best, s-stale    Dest               NextHop         RoutePrf   RouteMetric Protocol*>  1.1.1.0/24         1.1.1.1         0          0           direct5. show ip protocol routing +协议类型, 显示公网下的协议表中的指定路由类型的路由信息：ZXROSNG(config)#show ip protocol routing connectedHeads: Dest = Destination, Prf\RoutePrf = Router preference,       Metric\RouteMetric = Router metricCodes: OSPF-3D = ospf-type3-discard, OSPF-5D = ospf-type5-discard, TE = rsvpte,       OSPF-7D = ospf-type7-discard, USER-I = user-ipaddr, RIP-D = rip-discard,       OSPF-E = ospf-ext, ASBR-V = asbr-vpn, GW-FWD = ps-busi, GW-UE = ps-user,       BGP-AD = bgp-aggr-discard, BGP-CE = bgp-confed-ext, NAT64 = sl-nat64-v4,       USER-N = user-network, USER-S = user-special, DHCP-S = dhcp-static,       DHCP-D = dhcp-dft, VES = video-enhanced-service, HAGP = hybrid-access-gateway-protocol     Marks: *valid, >best, s-stale    Dest               NextHop         RoutePrf   RouteMetric Protocol*>  12.0.0.0/8         12.21.21.21     0          0           direct*>  12.21.21.21/32     12.21.21.21     0          0           address6. show ip protocol routing migp, 显示MIGP路由表的路由信息：ZXROSNG(config)#show ip protocol routing migpHeads: Dest = Destination, Prf\RoutePrf = Router preference,       Metric\RouteMetric = Router metricCodes: OSPF-3D = ospf-type3-discard, OSPF-5D = ospf-type5-discard, TE = rsvpte,       OSPF-7D = ospf-type7-discard, USER-I = user-ipaddr, RIP-D = rip-discard,       OSPF-E = ospf-ext, ASBR-V = asbr-vpn, GW-FWD = ps-busi, GW-UE = ps-user,       BGP-AD = bgp-aggr-discard, BGP-CE = bgp-confed-ext, NAT64 = sl-nat64-v4,       USER-N = user-network, USER-S = user-special, DHCP-S = dhcp-static,       DHCP-D = dhcp-dft, VES = video-enhanced-service, HAGP = hybrid-access-gateway-protocol      Marks: *valid, >best, s-stale    Dest               NextHop         RoutePrf   RouteMetric Protocol*   1.1.1.0/24         1.1.1.2         115        20          isis-l1*>  89.89.89.0/24      1.1.1.2         115        20          isis-l17. show ip protocol routing summary, 显示公网下的所有有效路由数量：ZXROSNG(config)#show ip protocol routing summaryRoute Source    Countconnected:       2static:          0ospf:            0rip:             0bgp:             0isis:            0nat:             0natpt:           0vrrp:            0ppp:             0asbr_vpn:        0rsvpte:          0usr-ipaddr:      0usr-net:         0ipsec:           0ps-user:         0ps-busi:         0ves:             0ldp:             0user-special:    0dhcp-dft:        0dhcp-static:     0sl_nat64_v4:     0bras-pool:       0hagp:            0nat-mask:        0Total:           28. show ip protocol routing vrf-summary <vrf_name>, 显示某私网下的所有有效路由数量：VRF   Source    Countconnected:       2static:          0ospf:            0rip:             0bgp:             0isis:            0nat:             0natpt:           0vrrp:            0ppp:             0asbr_vpn:        0rsvpte:          0usr-ipaddr:      0usr-net:         0ipsec:           0ps-user:         0ps-busi:         0ves:             0ldp:             0user-special:    0dhcp-dft:        0dhcp-static:     0sl_nat64_v4:     0bras-pool:       0hagp:            0nat-mask:        0Total:           2





相关命令 :

无 




## show ipv6 forwarding backup route vrf 


show ipv6 forwarding backup route vrf 




命令功能 :

显示IPv6私网备份路由 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 forwarding backup route vrf 
  ＜vpn-name 
＞ {[＜network-address 
＞]|[＜network-address-mask 
＞ {weak-match 
|exact-match 
}]|[＜protocol-name 
＞]} 







命令参数解释 :



参数|描述
---|---
＜vpn-name＞|vrf名称
＜network-address＞|目的地址
＜network-address-mask＞|掩码
weak-match|最长匹配
exact-match|精确匹配
＜protocol-name＞|协议类型








缺省 :

无 






使用说明 :

无 






范例 :

显示zte6的私网FRR路由信息：ZXROSNG(config)#show ipv6 forwarding backup route vrf zte6IPv6 Routing Table:Headers: Dest: Destination, Gw: Gateway, Pri: Priority, M/S: Master/Slave;Codes  : K: kernel, I1: isis-l1, SFN: sf-nat64, R: ripng, AF: aftr, B: bgp,         D: direct, I2: isis-l2, SLN: sl-nat64, O: ospfv3, D6: dhcp, P: ppp,         S: static, N: nd, V: vrrp, A: address, M: multicast, UI: user-ipaddr,         GW-FWD: PS-BUSI,GW-UE: PS-USER,LDP-A: LDP-AREA, UN: user-network,         US: user-special, BP: BRAS-pool, DL: dynamic-leased-line,         BE: bgp-evpn;Flag codes: M: Master, S: Slave, I: Inuse, U: Unuse, R: Relay, W: WTR;Dest                                              Owner   Metric  Interface                       Pri  M/S  Flags  Gw1:2::3:4/128                                      S        1  gei-0/1/0/5                     1    M    I    ::1:2::3:4/128                                      S        100  gei-0/1/0/6                     100  S    U    ::域信息描述符表：域    描述Dest    FRR路由目的地Owner    FRR路由协议类型Metric    FRR路由Metric属性Interface    FRR路由出接口Pri    FRR路由优先级M/S    FRR路由主备属性Sta    FRR路由当前转发状态Gw    FRR路由下一跳





相关命令 :

无 




## show ipv6 forwarding backup route 


show ipv6 forwarding backup route 




命令功能 :

显示IPv6公网备份路由 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 forwarding backup route 
  {[＜network-address 
＞]|[＜network-address-mask 
＞ {weak-match 
|exact-match 
}]|[＜protocol-name 
＞]} 







命令参数解释 :



参数|描述
---|---
＜network-address＞|目的地址
＜network-address-mask＞|掩码
weak-match|最长匹配
exact-match|精确匹配
＜protocol-name＞|协议类型








缺省 :

无 






使用说明 :

无 






范例 :

显示所有公网FRR路由信息：ZXROSNG(config)#show ipv6 forwarding backup routeIPv6 Routing Table:Headers: Dest: Destination, Gw: Gateway, Pri: Priority, M/S: Master/Slave,Sta: Status;Codes  : K: kernel, I1: isis-l1, SFN: sf-nat64, R: ripng, AF: aftr, B: bgp,D: direct, I2: isis-l2, SLN: sl-nat64, O: ospfv3, D6: dhcp, P: ppp,S: static, N: nd, V: vrrp, A: address, M: multicast, UI: user-ipaddr,GW-FWD: PS-BUSI,GW-UE: PS-USER,LDP-A: LDP-AREA, UN: user-network,US: user-special;Status codes: M: Master, S: Slave, I: Inuse, U: Unuse;Dest                                              Owner    MetricInterface                       Pri  M/S  Sta  Gw2222:2222:2222:2222:2222:2222:2222:110/128        S        0NULL                            1    M    I    ::ffff:1.1.1.12222:2222:2222:2222:2222:2222:2222:110/128        S        0gei-0/1/0/5                     7    S    U    1111:1111:1111:1111:1111:1111:1111:1132222:2222:2222:2222:2222:2222:2222:111/128        S        0NULL                            1    M    I    ::ffff:1.1.1.12222:2222:2222:2222:2222:2222:2222:111/128        S        0gei-0/1/0/5                     7    S    U    1111:1111:1111:1111:1111:1111:1111:1132222:2222:2222:2222:2222:2222:2222:112/128        S        0NULL                            1    M    I    ::ffff:1.1.1.12222:2222:2222:2222:2222:2222:2222:112/128        S        0gei-0/1/0/5                     7    S    U    1111:1111:1111:1111:1111:1111:1111:1132222:2222:2222:2222:2222:2222:2222:113/128        S        0NULL                            1    M    I    ::ffff:1.1.1.12222:2222:2222:2222:2222:2222:2222:113/128        S        0gei-0/1/0/5                     7    S    U    1111:1111:1111:1111:1111:1111:1111:113域信息描述符表：域    描述Dest    FRR路由目的地Owner    FRR路由协议类型Metric    FRR路由Metric属性Interface    FRR路由出接口Pri    FRR路由优先级M/S    FRR路由主备属性Sta    FRR路由当前转发状态Gw    FRR路由下一跳





相关命令 :

无 




## show ipv6 forwarding route summary all 


show ipv6 forwarding route summary all 




命令功能 :

显示IPv6公网路由数目和各VRF路由数目。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 forwarding route summary all 
 







命令参数解释 :


					无
				 






缺省 :

无。 






使用说明 :

无。 






范例 :

R1#show ipv6 forwarding route summary allIPv6 route prefix capacity: 100100IPv6 total route prefix count: 2IPv6 global route prefix count: 1IPv6 VRF mng route prefix count: 1





相关命令 :

无。 




## show ipv6 forwarding route summary global 


show ipv6 forwarding route summary global 




命令功能 :

显示V6公网路由数目 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 forwarding route summary global 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ipv6 forwarding route summary gZXROSNG(config)#show ipv6 forwarding route summary global The total routes of global:Route Source   Countkernel:           0connect:          1static:           0ripng:            0ospfv3:           0bgp:              0isis-l1:          0isis-l2:          0icmp:             0multicast:        1user-ipaddr:      0vrrp:             0ppp:              0nd:               0address:          1dhcp:             0sf-nat64:         0sl-nat64:         0aftr:             0ps-busi:          0ps-user:          0ldp-area:         0user-network:     0user-special:     0bras-pool:        0srv6:             0dyn-leasedline:   0Total:            3





相关命令 :

无 




## show ipv6 forwarding route summary vrf 


show ipv6 forwarding route summary vrf 




命令功能 :

显示v6私网路由数目 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 forwarding route summary vrf 
  ＜vpn-name 
＞ 







命令参数解释 :



参数|描述
---|---
＜vpn-name＞|vrf名称








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ipv6 forwarding route summary  vrf zte6The total routes of the vpn:Route Source   Countkernel:           0connect:          1static:           0ripng:            0ospfv3:           0bgp:              0isis-l1:          0isis-l2:          0icmp:             0multicast:        1user-ipaddr:      0vrrp:             0ppp:              0nd:               0address:          1dhcp:             0sf-nat64:         0sl-nat64:         0aftr:             0ps-busi:          0ps-user:          0ldp-area:         0user-network:     0user-special:     0bras-pool:        0srv6:             0dyn-leasedline:   0Total:            3





相关命令 :

无 




## show ipv6 forwarding route summary 


show ipv6 forwarding route summary 




命令功能 :

显示v6公私网路由数目 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 forwarding route summary 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ipv6 forwarding route summaryThe total routes of global and all VPNs:Route Source   Countkernel:           0connect:          2static:           0ripng:            0ospfv3:           0bgp:              0isis-l1:          0isis-l2:          0icmp:             0multicast:        3user-ipaddr:      0vrrp:             0ppp:              0nd:               0address:          2dhcp:             0sf-nat64:         0sl-nat64:         0aftr:             0ps-busi:          0ps-user:          0ldp-area:         0user-network:     0user-special:     0bras-pool:        0srv6:             0dyn-leasedline:   0Total:            7





相关命令 :

无 




## show ipv6 forwarding route vrf 


show ipv6 forwarding route vrf 




命令功能 :

显示v6私网路由 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 forwarding route vrf 
  ＜vpn-name 
＞ {[＜network-address 
＞]|[＜network-address-mask 
＞ {weak-match 
|exact-match 
 [detail 
]}]|[＜protocol-name 
＞]} 







命令参数解释 :



参数|描述
---|---
＜vpn-name＞|VRF名称，长度为1–32位字符串，不包含空格，区分大小写。
＜network-address＞|目的地址
＜network-address-mask＞|掩码
weak-match|最长匹配
exact-match|精确匹配
detail|显示路由详细信息
＜protocol-name＞|协议类型








缺省 :

无 






使用说明 :

无 






范例 :

1.显示IPv6转发表ZXROSNG(config)#show ipv6 forwarding route vrf zte6IPv6 Routing Table:Headers: Dest: Destination, Gw: Gateway, Pri: Priority;Codes  : K: kernel, I1: isis-l1, SFN: sf-nat64, R: ripng, AF: aftr, B: bgp,         D: direct, I2: isis-l2, SLN: sl-nat64, O: ospfv3, D6: dhcp, P: ppp,         S: static, N: nd, V: vrrp, A: address, M: multicast, UI: user-ipaddr,         GW-FWD: PS-BUSI,GW-UE: PS-USER,LDP-A: LDP-AREA, UN: user-network,         US: user-special, BP: BRAS-pool;Flag codes: R: Relay;Dest                                              Owner   Flags  Metric  Interface                       Pri  Gw 1:2::3:4/128                                      S              0           gei-0/1/0/3                     1    31::331::/120                                          D              0           gei-0/1/0/3                     0    31::131::1/128                                         A              0           gei-0/1/0/3                     0    31::141::/120                                          D              0           gei-0/1/0/4                     0    41::141::1/128                                         A              0           gei-0/1/0/4                     0    41::1ff02::/16                                         M              0           NULL                            0    ::域信息描述符表：域              描述Dest         路由目的地Owner        路由协议类型Flags        路由的一些状态和标记，如静态路由下一跳解析标记（R）Metric       路由metric属性Interface    路由出接口Pri          路由优先级Gw           路由下一跳2. 查看指定IPv6路由的详细信息ZXROSNG(config)#show ipv6 forwarding route 30::/16 exact-match detail 2016/12/07 03:32:51.77330::/16  via 20::3, static, inuse, relay, distance 1, metric 0    path-index 1    next-hop 20::3, via 20::/16     [1] 20:: gei-0/1/0/1     [2] 20:: gei-0/1/0/2  via 20::5, static, backup, unuse, relay, distance 56, metric 0    path-index 2    next-hop 20::5, via 20::/16     20:: gei-0/1/0/1域信息描述表：域                                     描述2016/12/07 03:32:51.773        命令执行的日期和时间30::/16                        路由的前缀信息via 20::3                      该路由的下一跳static                         当前路由类型distance 56, metric 0          该路由的管理距离和度量值backup                         备份路由inuse/unuse                    当前主路由和备份路由的使用情况，仅在存在FRR关系时显示relay                          该路由下一跳需要解析path-index                     该前缀路由的路径索引next-hop 20::3, via 20::/16    该路由的下一跳，如果需要解析，via后为解析到的路由前缀[1]                            当前在用转发路径的编号。20:: gei-0/1/0/1               实际转发路径的下一跳和出接口





相关命令 :

无 




## show ipv6 forwarding route 


show ipv6 forwarding route 




命令功能 :

显示v6公网路由 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 forwarding route 
  {[＜network-address 
＞]|[＜network-address-mask 
＞ {weak-match 
|exact-match 
 [detail 
]}]|[＜protocol-name 
＞]} 







命令参数解释 :



参数|描述
---|---
＜network-address＞|目的地址
＜network-address-mask＞|掩码
weak-match|最长匹配
exact-match|精确匹配
detail|显示路由详细信息
＜protocol-name＞|协议类型








缺省 :

无 






使用说明 :

无 






范例 :

1.显示IPv6转发表ZXROSNG(config)#show ipv6 forwarding routeIPv6 Routing Table:Headers: Dest: Destination, Gw: Gateway, Pri: Priority;Codes  : K: kernel, I1: isis-l1, SFN: sf-nat64, R: ripng, AF: aftr, B: bgp,         D: direct, I2: isis-l2, SLN: sl-nat64, O: ospfv3, D6: dhcp, P: ppp,         S: static, N: nd, V: vrrp, A: address, M: multicast, UI: user-ipaddr,         GW-FWD: PS-BUSI,GW-UE: PS-USER,LDP-A: LDP-AREA, UN: user-network,         US: user-special, BP: BRAS-pool;Flag codes: R: Relay;Dest                                              Owner   Flags  Metric  Interface                       Pri  Gw 101::/120                                         D              0           gei-0/1/0/1                     0    101::1101::1/128                                        A              0           gei-0/1/0/1                     0    101::1201::/120                                         D              0           gei-0/1/0/2                     0    201::1201::1/128                                        A              0           gei-0/1/0/2                     0    201::12222:2222:2222:2222:2222:2222:2222:110/128        S              0           gei-0/1/0/1                     1    101::3ff02::/16                                         M              0           NULL                            0    ::域信息描述符表：域                   描述Dest             路由目的地Owner            路由协议类型Flags            路由的一些状态和标记，如静态路由下一跳解析标记（R）Metric           路由metric属性Interface        路由出接口Pri              路由优先级Gw               路由下一跳2. 查看指定IPv6路由的详细信息ZXROSNG(config)#show ipv6 forwarding route 30::/16 exact-match detail 2016/12/07 03:32:51.77330::/16  via 20::3, static, inuse, relay, distance 1, metric 0    path-index 1    next-hop 20::3, via 20::/16     [1] 20:: gei-0/1/0/1     [2] 20:: gei-0/1/0/2  via 20::5, static, backup, unuse, relay, distance 56, metric 0    path-index 2    next-hop 20::5, via 20::/16      20:: gei-0/1/0/1域信息描述表：域                                          描述2016/12/07 03:32:51.773            命令执行的日期和时间30::/16                            路由的前缀信息via 20::3                          该路由的下一跳static                             当前路由类型distance 56, metric 0              该路由的管理距离和度量值relay                              该路由下一跳需要解析backup                             备份路由inuse/unuse                        当前主路由和备份路由的使用情况，仅在存在FRR关系时显示relay                              该路由下一跳需要解析path-index                         该前缀路由的路径索引next-hop 20::3, via 20::/16        该路由的下一跳，如果需要解析，via后为解析到的路由前缀[1]                                当前在用转发路径的编号。20:: gei-0/1/0/1                   实际转发路径的下一跳和出接口





相关命令 :

无 




## show ipv6 forwarding route-path summary 


show ipv6 forwarding route-path summary 




命令功能 :

显示v6公私网路由出向链路数目 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 forwarding route-path summary 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ipv6 forwarding route-path summaryThe total route-paths of global and all VPNs:Route Source   Countkernel:           0connect:          2static:           0ripng:            0ospfv3:           0bgp:              0isis-l1:          0isis-l2:          0icmp:             0multicast:        3user-ipaddr:      0vrrp:             0ppp:              0nd:               0address:          2dhcp:             0sf-nat64:         0sl-nat64:         0aftr:             0ps-busi:          0ps-user:          0ldp-area:         0user-network:     0user-special:     0bras-pool:        0Total:            7ZXROSNG(config)#





相关命令 :

无 




## show resource statistics fib 


show resource statistics fib 




命令功能 :

显示FIB表资源统计计数 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show resource statistics fib 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show resource statistics fib       Used        Free        Usage(%)IPv4  9           1048567     0.00086 IPv6  4           100096      0.00400域信息描述表：域             描述Used        已使用的资源数目Free         空闲资源数目Usage      已使用的资源在总资源中占用率，单位为百分比





相关命令 :

无 




