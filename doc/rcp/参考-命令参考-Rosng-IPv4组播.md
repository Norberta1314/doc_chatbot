# PIM Snooping配置命令 
## clear pimsnoop group 

clear pimsnoop group 
命令功能 : 
清除指定组播组的动态用户信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear pimsnoop group 
  ＜ipv4-address 
＞ [＜ipv4-address 
＞] {vpls 
 ＜vpls-name 
＞}
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|组播源地址，主机IP，点分十进制形式
＜ipv4-address＞|组播源地址，主机IP，点分十进制形式
＜vpls-name＞|VPLS实例名称，长度为1-32个字符
缺省 : 
无 
使用说明 : 
清除指定实例下指定组播组或指定组源下所有动态用户，其中组播源地址为可选参数。 
范例 : 
ZXROSNG#clear pimsnoop group 225.0.0.1 1.1.1.1 vpls zte 
相关命令 : 
show ip pim snooping port-info vpls 
## clear pimsnoop groups vpls 

clear pimsnoop groups vpls 
命令功能 : 
清除指定VPLS实例的全部组播组的动态用户信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear pimsnoop groups vpls 
  ＜vpls-name 
＞
命令参数解释 : 
参数|描述
---|---
＜vpls-name＞|VPLS实例名称，长度为1-32个字符
缺省 : 
无 
使用说明 : 
清除动态用户的信息，静态用户不会被清除。 
范例 : 
ZXROSNG#clear pimsnoop groups vpls zte 
相关命令 : 
show ip pim snooping port-info vpls 
## clear pimsnoop groups 

clear pimsnoop groups 
命令功能 : 
清除全部组播组的动态用户信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear pimsnoop groups 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
清除动态用户的信息，静态用户不会被清除。 
范例 : 
ZXROSNG#clear pimsnoop groups 
相关命令 : 
show ip pim snooping entry 
## debug pimsnoop 

debug pimsnoop 
命令功能 : 
打开PIM snooping 模块的debug功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug pimsnoop 
  {all 
|packet 
|event 
|error 
}
no debug pimsnoop 
  {all 
|packet 
|event 
|error 
}
				
命令参数解释 : 
参数|描述
---|---
all|关闭所有debug
packet|只关闭报文debug
event|只关闭事件debug
error|只关闭错误debug
缺省 : 
默认情况下，debug开关关闭。 
使用说明 : 
一般情况下，建议打开所有的debug开关以方便查看调试信息，如果信息过多，可以通过携带packet等参数过滤部分调试信息。可以指定多种参数组合打开debug，没有先后顺序。
范例 : 
ZXROSNG#debug pimsnoop allAll PIMSNOOP debugging is on
相关命令 : 
show debug pimsnoop 
## pim snooping 

pim snooping 
命令功能 : 
全局下PIM snooping使能。使用no命令关闭PIM snooping功能。 
命令模式 : 
 组播PIM-Snooping全局模式  
命令默认权限级别 : 
15 
命令格式 : 
pim snooping 
 
no pim snooping 
命令参数解释 : 
					无
				 
缺省 : 
全局下的PIM snooping功能关闭 
使用说明 : 
全局和实例下PIM snooping功能需要都开启才有用。 
范例 : 
在PIMSNOOP配置模式下开启全局pim snooping：ZXROSNG(config-pimsnoop)# pim  snooping 
相关命令 : 
无 
## pim snooping 

pim snooping 
命令功能 : 
VPLS实例下PIM snooping使能。使用no命令关闭PIM snooping功能 
命令模式 : 
 组播PIM-Snooping-VPLS模式  
命令默认权限级别 : 
15 
命令格式 : 
pim snooping 
 
no pim snooping 
命令参数解释 : 
					无
				 
缺省 : 
VPLS实例下的PIM snooping功能关闭 
使用说明 : 
需全局PIM snooping功能开启的情况下，VPLS实例下的PIM snooping功能开启才有效。VPLS实例必须已经存在。 
范例 : 
在PIMSNOOP_VPLS配置模式下配置pim snooping使能：ZXROSNG(config-pimsnoop)#vpls zte  ZXROSNG(config-pimsnoop-vpls-zte)#pim snooping
相关命令 : 
无 
## pimsnoop 

pimsnoop 
命令功能 : 
从全局配置模式进入PIMSNOOP配置模式 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
pimsnoop 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
在全局配置模式下输入pimsnoop，模式跳转进入PIMSNOOP配置模式。 
范例 : 
ZXROSNG(config)#pimsnoop ZXROSNG(config-pimsnoop)# 
相关命令 : 
无 
## show debug pimsnoop 

show debug pimsnoop 
命令功能 : 
显示PIMSNOOP模块的debug开关信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug pimsnoop 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
查看PIMSNOOP的debug开关信息。 
范例 : 
ZXROSNG#show debug pimsnoopPIMSNOOP:  PIMSNOOP packet debugging is on  PIMSNOOP event debugging is on  PIMSNOOP error debugging is on
相关命令 : 
show debug 
## show ip pim snooping detail entry vpls 

show ip pim snooping detail entry vpls 
命令功能 : 
显示指定VPLS实例下的条目详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping detail entry vpls 
  ＜vpls-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜vpls-name＞|VPLS 实例名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
如果全局或VPLS实例下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示该VPLS实例下存在的所有条目信息。 
范例 : 
ZXROSNG#show ip pim snooping detail entry vpls zte Index: 1    ID              : 1    Group address   : 225.1.1.1    Source address  : *    Present time    : 00:00:02
相关命令 : 
无 
## show ip pim snooping detail neighbor-info 

show ip pim snooping detail neighbor-info 
命令功能 : 
显示所有邻居详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping detail neighbor-info 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
如果全局下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示所有存在的邻居信息。 
范例 : 
ZXROSNG#show ip pim snooping detail neighbor-info Index: 1    Type            : VPLS    ID              : 1    Name            : zte    Port            : gei-0/1/0/7    Neighbor IP     : 192.168.1.1    Present time    : 00:00:21    Expire time     : 00:01:24
相关命令 : 
无 
## show ip pim snooping detail port-info vpls 

show ip pim snooping detail port-info vpls 
命令功能 : 
显示指定VPLS实例下的端口详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping detail port-info vpls 
  ＜vpls-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜vpls-name＞|VPLS 实例名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
如果全局或VPLS实例下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示该VPLS实例下存在的所有用户条目信息。 
范例 : 
ZXROSNG#show ip pim snooping detail port-info vpls zteIndex: 1    ID              : 1    Group address   : 225.1.1.1    Source address  : *    Port            : gei-0/1/0/7    Present time    : 00:00:11    Expire time     : 00:04:49
相关命令 : 
无 
## show ip pim snooping entry vpls 

show ip pim snooping entry vpls 
命令功能 : 
显示指定VPLS实例下的条目信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping entry vpls 
  ＜vpls-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜vpls-name＞|VPLS 实例名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
如果全局或VPLS实例下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示该VPLS实例下存在的所有条目信息。 
范例 : 
ZXROSNG(config-pimsnoop)#show ip pim snooping entry vpls zteIndex VPNID    Source-IP       Group-IP----------------------------------------------1     1        1.1.1.1         225.1.1.1
相关命令 : 
无 
## show ip pim snooping entry 

show ip pim snooping entry 
命令功能 : 
显示所有实例下的条目 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping entry 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
如果全局下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示全局下存在的所有条目信息。 
范例 : 
ZXROSNG(config-pimsnoop)#show ip pim snooping entryIndex VLAN    VPNID    Source-IP       Group-IP------------------------------------------------------1     0       1        1.1.1.1         225.1.1.1
相关命令 : 
无 
## show ip pim snooping neighbor-info 

show ip pim snooping neighbor-info 
命令功能 : 
显示所有邻居信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping neighbor-info 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
如果全局下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示所有存在的邻居信息。 
范例 : 
ZXROSNG(config)#show ip pim sn neighbor-infoIndex   Port             VLAN   VPNID   Neighbor-ip      RemainTime-----------------------------------------------------------------1       gei-0/1/0/1      10     0       168.2.0.11       240
相关命令 : 
无 
## show ip pim snooping port-info vpls 

show ip pim snooping port-info vpls 
命令功能 : 
显示指定VPLS实例下的端口信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping port-info vpls 
  ＜vpls-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜vpls-name＞|VPLS 实例名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
如果全局或VPLS实例下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示该VPLS实例下存在的所有用户条目信息。 
范例 : 
ZXROSNG(config-pimsnoop)#show ip pim snooping port-info vpls ztePIM snooping is globally enabled.PIM snooping is enabled in this VPLS.Index  VPNID  Source-IP   Group-IP         Ports                 Time-----------------------------------------------------------------------1      1      1.1.1.1     225.1.1.1        gei-0/1/0/1           220
相关命令 : 
无 
## show ip pim snooping summary entry vpls 

show ip pim snooping summary entry vpls 
命令功能 : 
显示指定VPLS实例下的条目统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping summary entry vpls 
  ＜vpls-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜vpls-name＞|VPLS 实例名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
如果全局或VPLS实例下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示该VPLS实例下存在的所有条目统计信息。 
范例 : 
ZXROSNG(config)#show ip pim snooping summary entry vpls zteThe summary information about group entry:     Type                         Summary-------------------------------------------------------     Total                        2               Source-Specific              1               Anycast-Specific             1     
相关命令 : 
show ip pim snooping entry vpls ＜vpls-name＞ 
## show ip pim snooping summary entry 

show ip pim snooping summary entry 
命令功能 : 
显示所有条目的统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping summary entry 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
如果全局下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示全局下存在的所有条目统计信息。 
范例 : 
ZXROSNG(config)#show ip pim snooping summary entry The summary information about group entry:     Type                         Summary-------------------------------------------------------     Total                        2               Source-Specific              1               Anycast-Specific             1       
相关命令 : 
show ip pim snooping entry  
## show ip pim snooping summary neighbor-info 

show ip pim snooping summary neighbor-info 
命令功能 : 
显示邻居统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping summary neighbor-info 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
如果全局下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示所有存在的邻居统计信息。 
范例 : 
ZXROSNG(config)#show ip pim snooping summary neighbor-info The summary information about neighbor:     Type                         Summary-------------------------------------------------------     Total                        2              
相关命令 : 
show ip pim snooping neighbor-info  
## show ip pim snooping summary port-info vpls 

show ip pim snooping summary port-info vpls 
命令功能 : 
显示指定VPLS实例下的用户条目统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping summary port-info vpls 
  ＜vpls-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜vpls-name＞|VPLS 实例名称，长度为1~32个字符
缺省 : 
无 
使用说明 : 
如果全局或VPLS实例下的PIM snooping功能未打开，该show命令将给出相应提示。否则显示该VPLS实例下存在的所有用户条目统计信息。 
范例 : 
ZXROSNG(config)#show ip pim snooping summary port-info vpls zteThe summary information about port:     Type                         Summary-------------------------------------------------------     Total                        2              
相关命令 : 
show ip pim snooping port-info vpls ＜vpls-name＞ 
## show ip pim snooping summary port-info 

show ip pim snooping summary port-info 
命令功能 : 
显示所有用户条目的统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip pim snooping summary port-info 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
如果全局的PIM snooping功能未打开，该show命令将给出相应提示。否则显示存在的所有用户条目统计信息。 
范例 : 
ZXROSNG(config)#show ip pim snooping summary port-info The summary information about port:     Type                         Summary-------------------------------------------------------     Total                        2            
相关命令 : 
show ip pim snooping entry 
## vpls 

vpls 
命令功能 : 
从PIMSNOOP配置模式进入PIMSNOOP_VPLS配置模式 
命令模式 : 
 组播PIM-Snooping全局模式  
命令默认权限级别 : 
15 
命令格式 : 
vpls 
  ＜vpls name 
＞
命令参数解释 : 
参数|描述
---|---
＜vpls name＞|vpls 实例名称，1-32个字符
缺省 : 
无 
使用说明 : 
必须先创建VPLS实例，再操作该实例下PIM snooping相关命令。 
范例 : 
从PIMSNOOP配置进入PIMSNOOP_VPLS配置模式：ZXROSNG(config-pimsnoop)#vpls zte ZXROSNG(config-pimsnoop-vpls-zte)# 
相关命令 : 
无 
# 组播配置命令 
## accept-register 

accept-register 
命令功能 : 
配置对接收到的register报文中封装的组播数据报文进行过滤，使用no命令取消过滤。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
accept-register 
  ＜access-list-name 
＞
no accept-register 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|它定义了一个地址范围，该范围是对register报文中封装的组播数据报文的源地址和组地址进行过滤。
缺省 : 
不对register报文中封装的组播数据报文进行过滤。 
使用说明 : 
根据ACL访问表中定义的规则，对register报文中封装的组播数据报文的源地址和组地址进行过滤，如果注册报文中的数据报文被与ACL规则不匹配，RP将会丢弃此注册报文，该组播源不能在RP上注册。 
范例 : 
根据访问控制列表a对接收到的register报文中封装的组播数据报文进行过滤：ZXROSNG(config)#ipv4-access-list aZXROSNG(config-ipv4-acl)#rule 1 permit ip 2.2.2.2 0.0.0.255 225.5.5.5 0.0.0.0ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#accept-register a
相关命令 : 
无 
## accept-rp 

accept-rp 
命令功能 : 
对BSR消息中通告的候选RP地址进行过滤，使用no命令取消过滤。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
accept-rp 
  ＜access-list-name 
＞
no accept-rp 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|它定义了一个地址范围，该范围是对接收的BSR消息中通告的候选RP进行过滤。
缺省 : 
不对BSR消息中通告的候选RP地址进行过滤。 
使用说明 : 
如果本路由器不是BSR，则根据ACL访问表中定义的规则对接收的BSR消息中通告的候选RP进行过滤，符合规则的添入本地RP集，不符合规则的忽略。如果本路由器是BSR，则根据ACL访问表中定义的规则对发送的BSR消息中通告的候选RP进行过滤，符合规则添入报文通告，不符合规则的忽略。
范例 : 
在BSR消息中对访问控制列表zte的候选RP地址进行过滤：ZXROSNG(config)#ipv4-access-list zteZXROSNG(config-ipv4-acl)#rule 1 permit 20.1.1.1 0.0.0.0ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#accept-rp zte
相关命令 : 
无 
## access-group 

access-group 
命令功能 : 
配置允许IGMP加入的组范围，使用no命令取消限制。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
access-group 
  ＜acl-name 
＞
no access-group 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|标准IP访问表名，长度1–31字符
缺省 : 
缺省没有IGMP加入组限制。 
使用说明 : 
该命令只对动态加入的组有效，对配置的静态组无效。
范例 : 
配置允许IGMP加入的组范围：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#access-group zte
相关命令 : 
无 
## anycast-rp-local 

anycast-rp-local 
命令功能 : 
配置Anycast-RP本端接口，用于转发注册报文。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
anycast-rp-local 
  ＜interface-name 
＞
no anycast-rp-local 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口的名称。
缺省 : 
没有配置anycast-rp-local。 
使用说明 : 
如果RP接收到来自与源直连的DR的注册报文，且此RP配置了anycast-rp-local命令，则可以将收到的注册报文转发给其他RP。 
范例 : 
配置Anycast-RP本端接口为gei-0/1/0/1：ZXROSNG(config-mcast-pim)#anycast-rp-local gei-0/1/0/1
相关命令 : 
anycast-rp-peer：配置对端RP接收注册报文的地址。 
## anycast-rp-peer 

anycast-rp-peer 
命令功能 : 
配置Anycast-RP对端地址，用于接收注册报文。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
anycast-rp-peer 
  ＜ip-address 
＞
no anycast-rp-peer 
  ＜ip-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|对端接口的ip地址。
缺省 : 
没有配置anycast-rp-peer。 
使用说明 : 
如果此RP接收到来自与源直连的DR的注册报文，若配置anycast-rp-peer命令，其他RP则可以收到注册报文。 
范例 : 
配置Anycast-RP对端接口地址为10.1.1.1：ZXROSNG(config-mcast-pim)#anycast-rp-peer 10.1.1.1
相关命令 : 
anycast-rp-local：配置本端RP发送注册报文的接口。 
## assert-disable 

assert-disable 
命令功能 : 
在接口上取消assert功能。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
assert-disable 
 
no assert-disable 
命令参数解释 : 
					无
				 
缺省 : 
接口上有assert功能。 
使用说明 : 
在多路访问网络中,使用断言assert机制来选举唯一的转发者以防向同一网段重复转发组播数据包。默认接口上是有assert功能的，如果配置了assert-disable则取消此功能。 
范例 : 
在接口gei-0/1/0/1上取消assert功能：ZXROSNG(config-mcast-pim)# interface gei-0/1/0/1 ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#assert-disable
相关命令 : 
无 
## assert-holdtime 

assert-holdtime 
命令功能 : 
配置assert状态保持时间。使用no命令恢复默认值。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
assert-holdtime 
  ＜seconds 
＞
no assert-holdtime 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|assert状态保持时间，范围：60-65535，单位：秒
缺省 : 
assert状态保持时间，缺省为180秒 
使用说明 : 
需先使能PIM才能配置此命令 
范例 : 
配置assert-holdtime为200秒：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router pim ZXROSNG(config-mcast-pim)# assert-holdtime 200
相关命令 : 
router pim：使能PIM。 
## bfd-enable 

bfd-enable 
命令功能 : 
对MSDP邻居配置此命令之后，可以快速检测TCP连接链路状态。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER-VRF模式:15,MSDP-PEER模式:15 
命令格式 : 
bfd-enable 
 
no bfd-enable 
命令参数解释 : 
					无
				 
缺省 : 
非使能 
使用说明 : 
MSDP peer 使能BFD后，peer之间能够建立BFD邻居，从而快速感知链路状态，MSDP peer状态快速做出相应的切换。 
范例 : 
对ip地址为10.10.10.2的MSDP邻居使能BFD功能：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#route msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)# bfd-enable
相关命令 : 
无 
## bfd-enable 

bfd-enable 
命令功能 : 
在接口上启用BFD。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
bfd-enable 
 
no bfd-enable 
命令参数解释 : 
					无
				 
缺省 : 
接口不启用BFD。 
使用说明 : 
该命令配置之前必须先使能PIM-SM。 
范例 : 
配置在接口gei-0/1/0/1上启用BFD功能：ZXROSNG(config-mcast-pim)# interface gei-0/1/0/1 ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#bfd-enable
相关命令 : 
show ip pim bfd：显示配置BFD的接口信息。 
## bind 

bind 
命令功能 : 
为pim-group绑定关联接口，使用no删除接口绑定。 
命令模式 : 
 PIM-GROUP-VRF模式,PIM-GROUP模式  
命令默认权限级别 : 
PIM-GROUP模式:15,PIM-GROUP-VRF模式:15 
命令格式 : 
bind 
  ＜interface-name 
＞ {active 
|passive 
}
no bind 
  ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
active|接口模式是active
passive|接口模式是passive
缺省 : 
不绑定任何接口。 
使用说明 : 
1.配置pim-group的管理接口，active模式接口PIM协议状态将会影响当前pim-group的转发状态，passive模式接口转发状态继承于当前pim-group；2.在一个pim-group里，必须先配置active模式接口才能配置passive模式接口，并且一个接口只可绑定在一个pim-group。
范例 : 
配置bind：ZXROSNG(config-mcast-pim)#pim-group protect-groupZXROSNG(config-mcast-pim-group-protect-group)#bind gei-0/1/0/1 active     ZXROSNG(config-mcast-pim-group-protect-group)#bind gei-0/1/0/2 passive
相关命令 : 
pim-group 
## bsm-unicast 

bsm-unicast 
命令功能 : 
配置单播发送BSR消息。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
bsm-unicast 
 
no bsm-unicast 
命令参数解释 : 
					无
				 
缺省 : 
组播形式发送BSR消息。 
使用说明 : 
如果配置了bsm-unicast命令，DR接口发现新邻居时，将向该邻居单播发送第一个BSM报文，后面的BSM报文仍是组播形式发送。 
范例 : 
配置单播发送BSR消息：ZXROSNG(config-mcast-pim)#bsm-unicast
相关命令 : 
无 
## bsr-border 

bsr-border 
命令功能 : 
配置接口使其成为PIM域边界。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
bsr-border 
 
no bsr-border 
命令参数解释 : 
					无
				 
缺省 : 
接口不配置为PIM域边界。 
使用说明 : 
当在接口上配置该命令时，没有BSM能在任一方向上通过该边界。该命令有效地将网络划分成使用不同BSM的区域。其他PIM报文可以通过域边界。 
范例 : 
在路由器接口gei-0/1/0/1上配置PIM域边界：ZXROSNG(config-mcast-pim)# interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#bsr-border
相关命令 : 
无 
## bsr-candidate 

bsr-candidate 
命令功能 : 
配置路由器使其宣布作为自举路由器（BSR）的候选者，使用no命令取消该路由器作为自举路由器的候选者。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
bsr-candidate 
  ＜interface-name 
＞ [{[hash-mask-length 
 ＜hash-mask-length 
＞],[priority 
 ＜priority 
＞]}]
no bsr-candidate 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口的名称。
＜hash-mask-length＞|哈希掩码长度，范围：0–32，缺省为30。
＜priority＞|优先级，范围：0–255，缺省为0。
缺省 : 
本路由器不是候选BSR。 
使用说明 : 
1.候选BSR的缺省优先级为0，具有较高优先级的候选BSR成为最终BSR；2.如果多个路由器的BSR优先级一样，则比较IP地址，具有最大地址的候选BSR成为最终BSR;3.推荐用户将候选BSR配置在loopback接口上，从而减少由于物理接口up/down造成的网络震荡。
范例 : 
在接口loopback1上配置候选BSR，哈希掩码长度为30，优先级为100：ZXROSNG(config-mcast-pim)#bsr-candidate loopback1 hash-mask-length 30 priority 100show命令查看配置结果信息：ZXROSNG(config-mcast-pim)#show ip pim bsr          BSR address: 2.2.2.3Uptime: 00:00:48, BSR Priority :100, Hash mask length:30Expires:00:00:03This system is a candidate BSR!  candidate BSR address: 2.2.2.3(loopback1),                priority: 100,                hash mask length: 30No candidate RP information!
相关命令 : 
show ip pim bsr：查看BSR配置信息。 
## bsr-candidate-holdtime 

bsr-candidate-holdtime 
命令功能 : 
设置C-BSR保持时间。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
bsr-candidate-holdtime 
  ＜seconds 
＞
no bsr-candidate-holdtime 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|设置C-BSR保持时间，范围：130–65535，单位：秒。
缺省 : 
不设置C-BSR保持时间，默认130秒。 
使用说明 : 
设置的C-BSR保持时间必须大于或等于BSM消息发送周期的两倍加10秒。 
范例 : 
设置C-BSR保持时间为200秒：ZXROSNG(config-mcast-pim)#bsr-candidate-holdtime 200
相关命令 : 
bsr-candidate-interval：设置BSM消息发送周期。 
## bsr-candidate-interval 

bsr-candidate-interval 
命令功能 : 
设置BSM消息发送周期。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
bsr-candidate-interval 
  ＜seconds 
＞
no bsr-candidate-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|设置BSM消息发送周期，范围：10–65535，单位：秒。
缺省 : 
不设置BSM消息发送周期，默认60秒。 
使用说明 : 
1.设置的BSM消息发送周期必须小于或等于C-BSR保持时间减去10s的时间的一半。2.设置的BSM消息发送周期必须小于或等于最小C-RP保持时间的2/5。
范例 : 
设置BSM消息发送周期为80秒：ZXROSNG(config-mcast-pim)# bsr-candidate-interval 80
相关命令 : 
bsr-candidate-holdtime：设置C-BSR保持时间。 
## bsr-policy 

bsr-policy 
命令功能 : 
PIM对BSR地址过滤。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
bsr-policy 
  ＜access-list-name 
＞
no bsr-policy 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|访问控制列表名称，长度1–31个字符。
缺省 : 
不对PIM BSR地址过滤。 
使用说明 : 
如果本路由器不是BSR，则根据ACL访问表中定义的规则对接收的BSR消息中BSR地址进行过滤；如果本路由器是BSR，则根据ACL访问表中定义的规则对配置的BSR地址进行过滤。 
范例 : 
用访问控制列表zte对BSR地址进行过滤：ZXROSNG(config)#ipv4-access-list zteZXROSNG(config-ipv4-acl)#rule 1 permit 100.10.10.20ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#bsr-policy zte
相关命令 : 
无 
## clear ip igmp groups 

clear ip igmp groups 
命令功能 : 
删除动态加入的组播组。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip igmp groups 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
1. 如果没有接口选项，则删除所有动态加入的组播组。2. 如果选择接口，则删除指定接口上所有动态加入的组播组。
范例 : 
删除所有动态加入的组播组：ZXROSNG#clear ip igmp groupsAre you sure to delete the IGMP group entries?[yes/no]:yesZXROSNG#
相关命令 : 
无 
## clear ip igmp packet-count 

clear ip igmp packet-count 
命令功能 : 
清除IGMP接收和发送的报文统计计数。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip igmp packet-count 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
清除公网所有使能PIM协议的接口，igmp协议报文接收和发送统计计数：clear ip igmp packet-count；清除公网接口igmp协议报文接收和发送统计计数：clear ip igmp packet-count <interface-name>;清除私网所有使能PIM协议的接口，接口igmp协议报文接收和发送统计计数：clear ip igmp packet-count <vrf-name>清除私网接口igmp协议报文接收和发送统计计数：clear ip igmp packet-count <vrf-name> <interface-name>
范例 : 
清除IGMP接收和发送的报文统计计数：ZXROSNG#clear ip igmp packet-count
相关命令 : 
无 
## clear ip mroute 

clear ip mroute 
命令功能 : 
清除IP组播路由表。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip mroute 
  [vrf 
 ＜vrf-name 
＞] [group-address 
 ＜group-address 
＞ [source-address 
 ＜source-address 
＞]]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符
＜group-address＞|组播组地址，十进制点分形式
＜source-address＞|源地址，十进制点分形式
缺省 : 
无 
使用说明 : 
1. 如果没有参数选项，则删除公网所有组播路由条目。2. 如果只选择组选项，则删除（*，g）和相关的所有（s，g）组播路由条目。3. 如果选择组和源地址选项，在删除相应的（s，g）组播路由条目。 4. 如果选择vrf选项，则删除指定vrf实例下所有组播路由条目。
范例 : 
删除公网组播路由条目：ZXROSNG#clear ip mrouteAre you sure to delete the IP multicast routing entries? [yes/no]:yesZXROSNG#
相关命令 : 
show ip mroute 
## clear ip msdp peer 

clear ip msdp peer 
命令功能 : 
清除与所有或指定MSDP邻居建立的TCP连接。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip msdp peer 
  [vrf 
 ＜vrf-name 
＞] [＜peer-address 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符
＜peer-address＞|MSDP邻居的IP地址
缺省 : 
无 
使用说明 : 
此命令关闭与MSDP邻居的TCP连接，重置MSDP邻居的所有统计。若参数缺省，表示关闭与所有MSDP邻居的TCP连接，重置所有MSDP邻居的所有统计。 
范例 : 
清除与IP地址为101.1.1.1的MSDP邻居的TCP连接：ZXROSNG#clear ip msdp peer 101.1.1.1 
相关命令 : 
无 
## clear ip msdp sa-cache 

clear ip msdp sa-cache 
命令功能 : 
清除MSDP SA cache项。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip msdp sa-cache 
  [vrf 
 ＜vrf-name 
＞] [＜group-address 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符
＜group-address＞|组播组地址
缺省 : 
无 
使用说明 : 
如果没有特别指定具体的组播组地址，将清除对应实例下所有的SA cache项。 
范例 : 
清除cache中来源于组播组224.1.1.1的SA cache项：ZXROSNG#clear ip msdp sa-cache 224.1.1.1
相关命令 : 
无 
## clear ip msdp statistics 

clear ip msdp statistics 
命令功能 : 
清除MSDP邻居的统计数据，但并不重置MSDP会话。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip msdp statistics 
  [vrf 
 ＜vrf-name 
＞] [＜peer-address 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符
＜peer-address＞|MSDP邻居的IP地址
缺省 : 
无 
使用说明 : 
如果没有特别指定具体的邻居地址，将清除所有的邻居的统计数据。 
范例 : 
清除IP地址为101.1.1.1的MSDP邻居的统计数据：ZXROSNG#clear ip msdp statistics 101.1.1.1
相关命令 : 
无 
## clear ip pim traffic 

clear ip pim traffic 
命令功能 : 
清零PIM协议流量统计信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear ip pim traffic 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞]
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
1.删除具体哪个VRF实例下的PIM流量统计信息，可采用<vrf-name>来指定，不指定则删除公网的；2.删除具体哪个PIM接口的流量统计信息，可采用<interface-name>来指定，不指定则删除所有PIM接口的流量统计信息。
范例 : 
配置删除公网的PIM协议流量统计信息。ZXROSNG#clear ip pim trafficZXROSNG#show ip pim trafficPIM packet       Received   Sent       Filter     ErrorInterface: gei-0/20/0/2  Hello:         0          0          0          0  Join/Prune:    0          0          0          0  Register:      0          0          0          0  Register-Stop: 0          0          0          0  Bootstrap:     0          0          0          0  C-RP-Ad:       0          0          0          0  Assert:        0          0          0          0  State-Refresh: 0          0          0          0  Graft:         0          0          0          0  Graft-Ack:     0          0          0          0  Df-Election:   0          0          0          0  PFM-TLV:       0          0          0          0Total traffic in current PIM instance:  Total:         0          0          0          0  Hello:         0          0          0          0  Join/Prune:    0          0          0          0  Register:      0          0          0          0  Register-Stop: 0          0          0          0  Bootstrap:     0          0          0          0  C-RP-Ad:       0          0          0          0  Assert:        0          0          0          0  State-Refresh: 0          0          0          0  Graft:         0          0          0          0  Graft-Ack:     0          0          0          0  Df-Election:   0          0          0          0  PFM-TLV:       0          0          0          0Current Time:  2019-09-25 01:32:00
相关命令 : 
show ip pim traffic：显示PIM流量统计信息。 
## connect-source 

connect-source 
命令功能 : 
配置TCP连接的源IP地址。使用no命令删除。 
命令模式 : 
 MSDP-VRF模式,MSDP模式  
命令默认权限级别 : 
MSDP模式:15,MSDP-VRF模式:15 
命令格式 : 
connect-source 
  ＜interface-name 
＞
no connect-source 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称，其地址将成为TCP连接的源IP地址
缺省 : 
无 
使用说明 : 
如果在MSDP模式或MSDP-VRF模式下配置了connect-source，本地路由器同邻居的TCP连接使用接口IP作为源IP。如果在MSDP-PEER模式或MSDP-PEER-VRF模式下对指定邻居配置connect-source。本地路由器同该邻居的TCP连接使用接口IP作为源IP。如果同时在MSDP模式和MSDP-PEER模式，或MSDP-VRF模式和MSDP-PEER-VRF模式下配置connect-source，则MSDP-PEER或MSDP-PEER-VRF模式下的配置命令生效。
范例 : 
将接口fei-0/9/0/1的IP配置为本地路由器TCP连接的源IP：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)#router msdpZXROSNG(config-mcast-vrf-zte-msdp)#connect-source gei-0/9/0/1
相关命令 : 
无 
## connect-source 

connect-source 
命令功能 : 
配置和指定MSDP邻居TCP连接的源IP地址。使用no命令删除。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
connect-source 
  ＜interface-name 
＞
no connect-source 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称，其地址成为同指定MSDP邻居TCP连接的源IP地址
缺省 : 
无 
使用说明 : 
如果在MSDP模式或MSDP-VRF模式下配置了connect-source，本地路由器同邻居的TCP连接使用接口IP作为源IP。如果在MSDP-PEER模式或MSDP-PEER-VRF模式下对指定邻居配置connect-source。本地路由器同该邻居的TCP连接使用接口IP作为源IP。如果同时在MSDP模式和MSDP-PEER模式，或MSDP-VRF模式和MSDP-PEER-VRF模式下配置connect-source，则MSDP-PEER或MSDP-PEER-VRF模式下的配置命令生效。
范例 : 
将接口gei-0/1/0/1的IP配置为本地路由器同邻居10.10.10.1的TCP连接的源IP：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.1ZXROSNG(config-mcast-msdp-peer)#connect-source gei-0/1/0/1
相关命令 : 
无 
## damping-enable 

damping-enable 
命令功能 : 
配置组播震荡延迟功能，使用no命令取消配置。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
damping-enable 
 
no damping-enable 
命令参数解释 : 
					无
				 
缺省 : 
不使能组播防震荡功能。 
使用说明 : 
1.使能组播防震荡功能2.配置震荡阈值，超过阈值将开启防震荡功能。3.最大等待时间是60秒，60秒后不管震荡次数多少，路由都会强制下发下去。
范例 : 
配置使能组播防震荡功能。ZXROSNG(config-mcast)#damping-enable
相关命令 : 
damping-threshold  
## damping-threshold 

damping-threshold 
命令功能 : 
配置组播震荡延迟功能，使用no命令取消配置。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
damping-threshold 
  ＜value 
＞
no damping-threshold 
命令参数解释 : 
参数|描述
---|---
＜value＞|震荡阈值, 取值2-100
缺省 : 
不使能组播防震荡功能。 
使用说明 : 
1.使能组播防震荡功能2.配置震荡阈值，超过阈值将开启防震荡功能。3.最大等待时间是60秒，60秒后不管震荡次数多少，路由都会强制下发下去。
范例 : 
配置震荡阈值为3次，超过阈值将开启防震荡功能。ZXROSNG(config-mcast)#damping-enableZXROSNG(config-mcast)#damping-threshold 3
相关命令 : 
damping-enable 
## data-filter 

data-filter 
命令功能 : 
PIM源数据过滤。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
data-filter 
  ＜access-list-name 
＞
no data-filter 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|访问控制列表名称，长度1–31个字符。
缺省 : 
不对PIM源数据过滤。 
使用说明 : 
根据ACL访问表中定义的规则，对组播数据报文的源地址和组地址进行过滤，与ACL规则不匹配的报文将丢弃。 
范例 : 
用访问控制列表zte对源数据进行过滤：ZXROSNG(config)#ipv4-access-list zteZXROSNG(config-ipv4-acl)#rule 1 permit ip any 225.5.5.5 0.0.0.0 ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#data-filter zte
相关命令 : 
无 
## debug ip igmp all 

debug ip igmp all 
命令功能 : 
打开IGMP协议相关的所有打印开关，使用no命令关闭开关后，不再输出信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip igmp all 
 
no debug ip igmp all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开IGMP协议相关的所有打印开关，使用no命令关闭开关 
范例 : 
打开IGMP协议相关的所有打印开关：ZXROSNG#debug ip igmp allAll IGMP debugging has been turned on
相关命令 : 
无 
## debug ip igmp 

debug ip igmp 
命令功能 : 
打开IGMP相关信息的调试开关，使用no命令关闭开关后，不再输出信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip igmp 
  [vrf 
 ＜vrf-name 
＞] [{[＜group-address 
＞]|[＜interface-name 
＞]}]
no debug ip igmp 
  [vrf 
 ＜vrf-name 
＞] [{[＜group-address 
＞]|[＜interface-name 
＞]}]
				
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜group-address＞|组地址，十进制点分形式
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
打开IGMP相关信息的调试开关，可以分别针对实例、组以及接口名：debug ip igmp [vrf ＜vrf-name＞] [{[＜group-address＞]|[＜interface-name＞]}]
范例 : 
打开IGMP相关信息的调试开关：ZXROSNG#debug ip igmp  IGMP debugging is on
相关命令 : 
无 
## debug ip mroute all 

debug ip mroute all 
命令功能 : 
打开mroute相关的所有打印开关。使用no命令关闭mroute相关的所有打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip mroute all 
 
no debug ip mroute all 
命令参数解释 : 
					无
				 
缺省 : 
打印开关关闭 
使用说明 : 
1.使用此命令前必须开启组播。2.此命令可以打开和关闭组播公网和私网的所有信息开关。
范例 : 
打开mroute相关的所有打印开关：ZXROSNG#debug ip mroute allAll MROUTE debugging has been turned on
相关命令 : 
show debug mroute 
## debug ip mroute 

debug ip mroute 
命令功能 : 
设置mroute相关信息的调试开关。使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip mroute 
  [vrf 
 ＜vrf-name 
＞] [{data-info 
|data 
|packet-recv 
|packet-send 
|tlv-recv 
|tlv-send 
|mrt-recv 
|mrt-syn 
}]
no debug ip mroute 
  [vrf 
 ＜vrf-name 
＞] [{data-info 
|data 
|packet-recv 
|packet-send 
|tlv-recv 
|tlv-send 
|mrt-recv 
|mrt-syn 
}]
				
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|设置某个vrf实例信息的调试开关
data-info|设置mroute整包数据信息的调试开关
data|设置mroute数据信息的调试开关
packet-recv|设置mroute接收报文信息的调试开关
packet-send|设置mroute发送报文信息的调试开关
tlv-recv|设置mroute接收TLV报文信息的调试开关
tlv-send|设置mroute发送TLV报文信息的调试开关
mrt-recv|设置mroute接收组播路由信息的调试开关
mrt-syn|设置mroute同步组播路由信息的调试开关
缺省 : 
打印开关关闭。 
使用说明 : 
1.设置具体哪个VRF实例的mroute信息的调试开关，可采用<vrf-name>来指定，如果没有<vrf-name>选项，则设置所有公网mroute信息的调试开关；2.如果增加配置选项，则相应设置相关mroute信息的调试开关。3.使用此命令前必须先启用组播。
范例 : 
设置mroute相关信息的调试开关：ZXROSNG#debug ip mroute   MROUTE debugging is on 
相关命令 : 
debug all mroute：打开mroute相关的所有打印开关。 
## debug ip msdp all 

debug ip msdp all 
命令功能 : 
开启MSDP全部调试信息开关,使用no命令关闭调试。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip msdp all 
 
no debug ip msdp all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
开启调试开关后使用terminal monitor命令开始打印调试信息。 
范例 : 
开启MSDP全部信息调试：ZXROSNG#debug ip msdp allAll MSDP debugging has been turned on
相关命令 : 
无 
## debug ip msdp 

debug ip msdp 
命令功能 : 
开启MSDP调试信息开关,使用no命令关闭调试。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip msdp 
  [vrf 
 ＜vrf-name 
＞] [{message-recv 
|message-send 
|connect 
|warning 
}]
no debug ip msdp 
  [vrf 
 ＜vrf-name 
＞] [{message-recv 
|message-send 
|connect 
|warning 
}]
				
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符
message-recv|设置收包信息的调试开关
message-send|设置发包信息的调试开关
connect|设置邻居连接信息的调试开关
warning|设置告警信息的调试开关
缺省 : 
无 
使用说明 : 
开启调试开关后使用terminal monitor命令开始打印调试信息。 
范例 : 
开启MSDP连接信息调试：ZXROSNG#debug ip msdp connect   MSDP connect debugging is on
相关命令 : 
无 
## debug ip mvpn all 

debug ip mvpn all 
命令功能 : 
打开MVPN协议相关的所有打印开关，使用no命令关闭。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip mvpn all 
 
no debug ip mvpn all 
命令参数解释 : 
					无
				 
缺省 : 
打印开关关闭。 
使用说明 : 
1.使用此命令前必须先启用组播和MVPN功能。2.此命令可以打开和关闭组播MVPN所有实例的信息开关。
范例 : 
打开MVPN协议相关的所有打印开关：ZXROSNG#debug ip mvpn all     All MVPN debugging has been turned onZXROSNG#no debug ip mvpn allAll MVPN debugging has been turned offZXROSNG#
相关命令 : 
debug all mvpn：与此命令功能相同。 
## debug ip mvpn 

debug ip mvpn 
命令功能 : 
设置MVPN相关信息的调试开关，使用no命令关闭。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip mvpn 
  [vrf 
 ＜vrf-name 
＞] [{rec-ad 
|intra-ad 
|inter-ad 
|spmsi-ad 
|leaf-ad 
|src-act 
|sg-join 
|xg-join 
|event 
|report 
|nexthop 
|warning 
}]
no debug ip mvpn 
  [vrf 
 ＜vrf-name 
＞] [{rec-ad 
|intra-ad 
|inter-ad 
|spmsi-ad 
|leaf-ad 
|src-act 
|sg-join 
|xg-join 
|event 
|report 
|nexthop 
|warning 
}]
				
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|vrf实例名称
rec-ad|设置rec-ad信息的调试开关
intra-ad|设置intra-ad信息的调试开关
inter-ad|设置inter-ad信息的调试开关
spmsi-ad|设置spmsi-ad信息的调试开关
leaf-ad|设置leaf-ad信息的调试开关
src-act|设置source-active信息的调试开关
sg-join|设置sg-join信息的调试开关
xg-join|设置xg-join信息的调试开关
event|设置evernt信息的调试开关
report|设置report信息的调试开关
nexthop|设置nexthop信息的调试开关
warning|设置warning信息的调试开关
缺省 : 
打印开关关闭。 
使用说明 : 
1.设置具体哪个VRF实例的MVPN信息的调试开关，可采用<vrf-name>来指定，如果没有<vrf-name>选项，则设置所有MVPN信息的调试开关；2.如果增加配置选项，则相应设置相关MVPN信息的调试开关。3.使用此命令前必须先启用组播
范例 : 
设置所有MVPN信息的调试开关：ZXROSNG#debug ip mvpn   MVPN debugging is onZXROSNG#no debug ip mvpn  MVPN debugging is off ZXROSNG#
相关命令 : 
show debug mvpn：显示打开的MVPN调试开关。 
## debug ip pim all 

debug ip pim all 
命令功能 : 
打开PIM协议相关的所有打印开关，使用no命令关闭。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip pim all 
 
no debug ip pim all 
命令参数解释 : 
					无
				 
缺省 : 
打印开关关闭。 
使用说明 : 
使用此命令前必须先启用组播和PIM功能。 
范例 : 
打开PIM协议相关的所有打印开关。ZXROSNG# debug ip pim allAll PIM debugging has been turned on
相关命令 : 
debug ip pim：设置PIM相关信息的调试开关。 
## debug ip pim 

debug ip pim 
命令功能 : 
设置PIM相关信息的调试开关，使用no命令关闭。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ip pim 
  [vrf 
 ＜vrf-name 
＞] [{bsr-rp 
|downstream-fsm 
|ast 
|register 
|nbr 
|nhp 
|mrt 
|packet-recv 
|packet-send 
|packet-dump 
|data-info 
|local 
|[group 
 ＜group-address 
＞]|[source 
 ＜source-address 
＞]|msdp 
|bfd 
}]
no debug ip pim 
  [vrf 
 ＜vrf-name 
＞] [{bsr-rp 
|downstream-fsm 
|ast 
|register 
|nbr 
|nhp 
|mrt 
|packet-recv 
|packet-send 
|packet-dump 
|data-info 
|local 
|[group 
 ＜group-address 
＞]|[source 
 ＜source-address 
＞]|msdp 
|bfd 
}]
				
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|设置VRF实例信息的调试开关，VRF名称，长度为1–32个字符
bsr-rp|设置PIM BSR和RP信息的调试开关
downstream-fsm|设置PIM下游状态机信息的调试开关
ast|设置PIM assert信息的调试开关
register|设置PIM注册报文信息的调试开关
nbr|设置PIM邻居信息的调试开关
nhp|设置PIM下一跳信息的调试开关
mrt|设置PIM路由表信息的调试开关
packet-recv|设置PIM接收报文信息的调试开关
packet-send|设置PIM发送报文信息的调试开关
packet-dump|设置PIM报文字段详细信息及错误信息的调试开关
data-info|设置PIM数据信息的调试开关
local|设置本地加入信息的调试开关
＜group-address＞|组播组地址，十进制点分形式，设置过滤组后的PIM相关信息的调试开关
＜source-address＞|源地址，十进制点分形式，设置过滤源后的PIM相关信息的调试开关
msdp|设置MSDP相关信息的调试开关
bfd|设置PIM BFD信息的调试开关
缺省 : 
打印开关关闭。 
使用说明 : 
1.设置具体哪个VRF实例的PIM信息的调试开关，可采用<vrf-name>来指定，如果没有<vrf-name>选项，则设置所有公网PIM信息的调试开关；2.如果增加其他选项，则相应设置相关PIM信息的调试开关；3.使用此命令前必须先启用组播和PIM功能。
范例 : 
设置打开所有公网PIM信息的调试开关。ZXROSNG#debug ip pim  PIM debugging is on 
相关命令 : 
show debug pim：显示打开的PIM调试开关。debug ip pim all：开启所有PIM打印开关。
## default-peer 

default-peer 
命令功能 : 
定义一个默认MSDP邻居，本地路由器将接收来自这个邻居的所有SA消息。使用no命令删除该默认邻居。 
命令模式 : 
 MSDP-VRF模式,MSDP模式  
命令默认权限级别 : 
MSDP模式:15,MSDP-VRF模式:15 
命令格式 : 
default-peer 
  ＜peer-address 
＞ [list 
 ＜acl-name 
＞]
no default-peer 
  ＜peer-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜peer-address＞|默认MSDP邻居的IP地址
＜acl-name＞|ACL名，长度1-31个字符
缺省 : 
无 
使用说明 : 
1.    如果不将MSDP邻居同时配置成BGP邻居，使用本命令。2.    如果用peer命令只配置了一个MSDP邻居，则这个邻居可当作默认MSDP邻居。此时不需要使用本命令配置默认MSDP邻居。3.    如果没有指定list <acl-name> 参数，本地路由器将接收所有来自默认MSDP邻居的SA消息；如果指定了list <acl-name> 参数，本地路由器将接收来自默认MSDP邻居并由与list <acl-name> 参数相匹配的RP所产生的SA消息。4.    本命令可以配置多条，但配置的所有命令必须都带有list关键字或者都没有list关键字，具体规则如下：a. 当使用多条带有list关键字的命令时，可以同时使用多个带有不同RP前缀的默认MSDP邻居。这种规则通常用于连接多个stub site子网的网络。b. 当使用多条不带list关键字的命令时，只使用一个活动的默认MSDP邻居用于接收所有的SA消息。当这个MSDP邻居离线时，将切换至另一个已配置好的默认MSDP邻居。这种规则通常用于一个单独的stub site。
范例 : 
将邻居10.10.10.2定义为默认MSDP邻居：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#default-peer 10.10.10.2
相关命令 : 
peer 
description : 

description 
命令功能 : 
给MSDP邻居添加说明性描述。使用no命令删除描述。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
description 
  ＜description 
＞
no description 
命令参数解释 : 
参数|描述
---|---
＜description＞|MSDP邻居的描述，不超过80个字符的文本
缺省 : 
无 
使用说明 : 
这个描述将显示在show ip msdp peer命令的输出结果中。 
范例 : 
给MSDP邻居10.10.10.1添加说明性描述：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.1ZXROSNG(config-mcast-msdp-peer)#description hello
相关命令 : 
无 
## dr-priority 

dr-priority 
命令功能 : 
配置PIM接口DR优先级，使用no命令恢复缺省值。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
dr-priority 
  ＜priority 
＞
no dr-priority 
命令参数解释 : 
参数|描述
---|---
＜priority＞|PIM接口DR优先级，缺省为1，范围：0–4294967295
缺省 : 
PIM接口DR优先级缺省为1。 
使用说明 : 
1.在共享网段上对多个PIM路由器进行DR竞选时，首先比较DR优先级，优先级数值大者获胜；如果DR优先级一致，则比较接口地址，地址大者获胜。2.在连接组播数据源的共享网段上，只有DR能够向RP封装数据报文发送Register消息。3.在连接接收者的共享网段上，只有DR才能响应IGMP加入、离开消息。
范例 : 
在路由器接口gei-0/1/0/1上配置DR优先级：ZXROSNG(config-mcast-pim)#interface gei-0/1/0/1 ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#dr-priority 20show命令查看配置结果信息：ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#show ip pim interface ZXROSNG(config)#show ip pim interface Interface                        State Nbr   Hello  DR         PIM      Mode                                       Count Period Priority   Silent  gei-0/1/0/1                      Up    0     30     20         Disabled   S    Address: 192.168.10.20    DR     : 192.168.10.20
相关命令 : 
show ip pim interface：显示接口相关信息。 
## dr-switchback-delay 

dr-switchback-delay 
命令功能 : 
设置接口启用BFD时由DR变为非DR后重新计算路由的时间。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
dr-switchback-delay 
  ＜seconds 
＞
no dr-switchback-delay 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|设置接口启用BFD时由DR变为非DR后重新计算路由的时间，范围：1–300，单位：秒。
缺省 : 
DR变化后立刻计算路由。 
使用说明 : 
设置接口启用BFD时由DR变为非DR后重新计算路由的时间，默认是立即计算。 
范例 : 
设置接口启用BFD时由DR变为非DR后重新计算路由的时间为10秒：ZXROSNG(config-mcast-pim)#dr-switchback-delay 10
相关命令 : 
bfd-enable:使能PIM BFD 
## error packet pim record 

error packet pim record 
命令功能 : 
使能或去使能PIM协议模块的错误报文记录功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
error packet pim record 
  {disable 
|enable 
 [＜number 
＞]}
命令参数解释 : 
参数|描述
---|---
disable|去使能PIM协议模块的错误报文记录功能。
enable|使能PIM协议模块的错误报文记录功能。
＜number＞|记录的错误报文个数，范围1-200，默认值是10。
缺省 : 
默认为enable，记录最近10个错误报文。 
使用说明 : 
1.disable时不清空已有记录缓存。2.收到的错误报文个数大于number时，新收到的错误报文覆盖最老的错误报文；3.number变小时，只保留最近收到的number个错误报文。
范例 : 
1.使能PIM协议模块的错误报文记录功能，并记录最近10个错误报文；ZXROSNG(config)#error packet pim record enable 2.使能PIM协议模块的错误报文记录功能，并记录最近200个错误报文；ZXROSNG(config)#error packet pim record enable 2003.去使能PIM协议模块的错误报文记录功能；ZXROSNG(config)#error packet pim record disable 
相关命令 : 
无 
## filter-policy monitor-interface 

filter-policy monitor-interface 
命令功能 : 
设置组播过滤策略，使用no命令取消配置。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
filter-policy monitor-interface 
  {＜interface-name 
＞} {include 
|exclude 
} {add 
|delete 
}
no filter-policy monitor-interface 
  [＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
include|接口路由过滤模式
exclude|接口路由过滤模式
add|接口过滤类型
delete|接口过滤类型
缺省 : 
不配置组播过滤策略 
使用说明 : 
1.配置基于接口的过滤规则，对全部路由生效，include为继承路由的既有出接口，exclude为过滤掉路由的既有出接口，add为添加既有路由一个出接口，delete为删除既有路由的出接口。接口的路由过滤模式需要全局统一。使用no命令取消配置2.配置基于路由的过滤规则，对配置的基于源组的路由生效，include为继承该路由的既有出接口，exclude为过滤掉该路由的既有出接口，add为添加该路由一个出接口，delete为删除该路由的出接口。只配置monitor-mroute-interface时，则路由的默认过滤模式为include。使用no命令取消配置。
范例 : 
ZXROSNG(config-mcast)#filter-policy monitor-interface gei-0/1/0/6 include addZXROSNG(config-mcast)#filter-policy monitor-mroute-mode 0.0.0.0 224.1.1.1 includeZXROSNG(config-mcast)#filter-policy monitor-mroute-interface 0.0.0.0 224.1.1.1 gei-0/1/0/6 add
相关命令 : 
filter-policy monitor-mroute-mode filter-policy monitor-mroute-interface filter-policy monitor-interface
## filter-policy monitor-mroute-interface 

filter-policy monitor-mroute-interface 
命令功能 : 
设置组播过滤策略，使用no命令取消配置。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
filter-policy monitor-mroute-interface 
  ＜source-address 
＞ ＜group-address 
＞ {＜interface-name 
＞} {add 
|delete 
}
no filter-policy monitor-mroute-interface 
  ＜source-address 
＞ ＜group-address 
＞ [＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜source-address＞|源地址，十进制点分形式
＜group-address＞|组地址，十进制点分形式
＜interface-name＞|接口名称
add|接口过滤类型
delete|接口过滤类型
缺省 : 
不配置组播过滤策略 
使用说明 : 
1.配置基于接口的过滤规则，对全部路由生效，include为继承路由的既有出接口，exclude为过滤掉路由的既有出接口，add为添加既有路由一个出接口，delete为删除既有路由的出接口。接口的路由过滤模式需要全局统一。使用no命令取消配置2.配置基于路由的过滤规则，对配置的基于源组的路由生效，include为继承该路由的既有出接口，exclude为过滤掉该路由的既有出接口，add为添加该路由一个出接口，delete为删除该路由的出接口。只配置monitor-mroute-interface时，则路由的默认过滤模式为include。使用no命令取消配置。
范例 : 
ZXROSNG(config-mcast)#filter-policy monitor-interface gei-0/1/0/6 include addZXROSNG(config-mcast)#filter-policy monitor-mroute-mode 0.0.0.0 224.1.1.1 includeZXROSNG(config-mcast)#filter-policy monitor-mroute-interface 0.0.0.0 224.1.1.1 gei-0/1/0/6 add
相关命令 : 
filter-policy monitor-mroute-mode filter-policy monitor-interface
## filter-policy monitor-mroute-mode 

filter-policy monitor-mroute-mode 
命令功能 : 
设置组播过滤策略，使用no命令取消配置。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
filter-policy monitor-mroute-mode 
  ＜source-address 
＞ ＜group-address 
＞ {include 
|exclude 
}
no filter-policy monitor-mroute-mode 
  ＜source-address 
＞ ＜group-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜source-address＞|源地址，十进制点分形式
＜group-address＞|组地址，十进制点分形式
include|接口路由过滤模式
exclude|接口路由过滤模式
缺省 : 
不配置组播过滤策略 
使用说明 : 
1.配置基于接口的过滤规则，对全部路由生效，include为继承路由的既有出接口，exclude为过滤掉路由的既有出接口，add为添加既有路由一个出接口，delete为删除既有路由的出接口。接口的路由过滤模式需要全局统一。使用no命令取消配置2.配置基于路由的过滤规则，对配置的基于源组的路由生效，include为继承该路由的既有出接口，exclude为过滤掉该路由的既有出接口，add为添加该路由一个出接口，delete为删除该路由的出接口。只配置monitor-mroute-interface时，则路由的默认过滤模式为include。使用no命令取消配置。
范例 : 
ZXROSNG(config-mcast)#filter-policy monitor-interface gei-0/1/0/6 include addZXROSNG(config-mcast)#filter-policy monitor-mroute-mode 0.0.0.0 224.1.1.1 includeZXROSNG(config-mcast)#filter-policy monitor-mroute-interface 0.0.0.0 224.1.1.1 gei-0/1/0/6 add
相关命令 : 
filter-policy monitor-mroute-interface filter-policy monitor-interface
## forwarding-policy 

forwarding-policy 
命令功能 : 
配置组播转发策略。使用no命令取消配置。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播模式:15,组播VRF模式:15 
命令格式 : 
forwarding-policy 
  {per-stream 
|per-packet 
|per-user 
} [group-list 
 ＜acl-name 
＞]
no forwarding-policy 
命令参数解释 : 
参数|描述
---|---
per-stream|选路策略为逐流优先
per-packet|选路策略为逐包优先
per-user|选路策略按用户选路
＜acl-name＞|ACL名称，用于指定组播组地址
缺省 : 
bras版本选路策略为按用户选路，非bras版本为逐流优先。 
使用说明 : 
1.如果选择group-list选项，则根据ACL规则进行过滤。2.使用per-user选项，转发流量会根据用户分担流量，使用per-packet选项，转发流量会根据包分担流量，使用per-stream选项，转发流量会根据路由分担流量。
范例 : 
1.配置组播转发策略ZXROSNG(config-mcast)#forwarding-policy per-packet2.配置带ACL的组播转发策略ZXROSNG(config-mcast)#forwarding-policy per-packet group-list test
相关命令 : 
ipv4-access-list 
## frr 

frr 
命令功能 : 
在PIM接口模式下配置frr enable，打开PIM BFD快切开关。主要表现为首先BDR设备往上游引流，同时在BDR设备上会下发不转发接口属性到转发面，当BDR向DR切换时，BDR设备的不转发属性会更新为转发属性。配置frr disable关闭PIM BFD快切开关，主要表现为BDR设备不再往上游引流，强制清除接口上的不转发标记。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
frr 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启PIM BFD快切功能
disable|关闭PIM BFD快切功能
缺省 : 
关闭PIM BFD快切功能 
使用说明 : 
在PIM接口模式下配置frr enable，打开PIM BFD快切开关。主要表现为首先BDR设备往上游引流，同时在BDR设备上会下发不转发接口属性到转发面，当BDR向DR切换时，BDR设备的不转发属性会更新为转发属性。配置frr disable关闭PIM BFD快切开关，主要表现为BDR设备不再往上游引流，强制清除接口上的不转发标记。 
范例 : 
ZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#frr enaZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#frr enable ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#frr disZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#frr disable ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#
相关命令 : 
PIM BFD  
## graft-retry-time 

graft-retry-time 
命令功能 : 
配置graft重传时间。使用no命令恢复默认值。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
graft-retry-time 
  ＜seconds 
＞
no graft-retry-time 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|graft重传时间，范围：1-65535，单位：秒
缺省 : 
graft重传时间，缺省为3秒 
使用说明 : 
需先使能PIM才能配置此命令 
范例 : 
配置 graft-retry-time：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router pim ZXROSNG(config-mcast-pim)# graft-retry-time 200
相关命令 : 
router pim：使能PIM。 
## hello-dr-address 

hello-dr-address 
命令功能 : 
使能PIM接口发送hello报文时携带DR地址选项。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
hello-dr-address 
 
no hello-dr-address 
命令参数解释 : 
					无
				 
缺省 : 
接口不使能hello-dr-address。 
使用说明 : 
为了防止在网络中有新增PIM设备时，进行DR选举，可能造成网络中原有流量的震荡，即老的DR不再转发流量，新的DR还未学全路由信息，设备都使能hello-dr-address功能，当有新增PIM设备时，新增设备收到的hello报文会携带现在网络中选举出来的DR地址，新增设备认为此地址就是当前的DR地址不再进行DR选举。 
范例 : 
在接口gei-0/1/0/1上启动hello-dr-address：ZXROSNG(config) # ip multicast-routingZXROSNG(config-mcast) #router pimZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#hello-dr-address
相关命令 : 
pimsm,pimdm 
## hello-interval 

hello-interval 
命令功能 : 
配置接口PIM hello报文发送间隔，使用no命令恢复缺省值。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
hello-interval 
  ＜seconds 
＞
no hello-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|PIM路由器hello报文发送周期间隔，缺省为30秒，范围：1–65535，单位：秒。
缺省 : 
PIM路由器hello报文发送周期间隔，缺省为30秒。 
使用说明 : 
该命令对于PIM-DM和PIM-SM都有效。此命令用来配置路由器发送hello报文的时间间隔。 
范例 : 
在路由器接口gei-0/1/0/1上配置PIM hello报文发送间隔：ZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#hello-interval 25show命令查看配置结果信息：ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#show ip pim interface Interface                        State Nbr   Hello  DR         PIM      Mode                                       Count Period Priority   Silent  gei-0/1/0/1                      Up    0     25     1          Disabled   S    Address: 192.168.10.20    DR     : 192.168.10.20
相关命令 : 
show ip pim interface：显示接口相关信息。 
## hello-join-attribute 

hello-join-attribute 
命令功能 : 
使能PIM hello加入属性选项开关。 
命令模式 : 
 PIM模式  
命令默认权限级别 : 
15 
命令格式 : 
hello-join-attribute 
 
no hello-join-attribute 
命令参数解释 : 
					无
				 
缺省 : 
不使能。 
使用说明 : 
命令使能后，PIM hello报文携带加入属性选项。 
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#hello-join-attribute
相关命令 : 
无 
## holdtime 

holdtime 
命令功能 : 
配置MSDP邻居的保持时间。使用no命令恢复缺省值。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER-VRF模式:15,MSDP-PEER模式:15 
命令格式 : 
holdtime 
  ＜seconds 
＞
no holdtime 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|MSDP邻居的保持时间，范围：1–75，单位：秒。
缺省 : 
不设置MSDP邻居的超时时间，默认值为75秒。 
使用说明 : 
无 
范例 : 
给IP地址为10.10.10.2的MSDP邻居配置邻居保持时间为60：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)# holdtime 60
相关命令 : 
无 
## igmp-proxy 

igmp-proxy 
命令功能 : 
在下游接口，又称路由器接口上，配置proxy功能所对应的上游接口，在上游接口上发送IGMP report消息，使用no命令恢复缺省状态。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
igmp-proxy 
  ＜interface-name 
＞
no igmp-proxy 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|proxy功能所对应的上游接口
缺省 : 
无 
使用说明 : 
在IGMP接口模式下配置igmp-proxy <intface-name>,该接口下所有的组成员将通过proxy接口向上游路由器发送report报文。该命令需要下面两个命令一起使用：1. IGMP模式下的proxy enable;2. proxy接口下配置proxy service;
范例 : 
配置接口上proxy的上游接口：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#igmp-proxy fei-0/1/0/2查看配置结果信息：ZXROSNG#show ip igmp proxy groupsTotal: 1 groupsGroup addr      Interface           Present239.255.255.250 fei-0/1/0/2         01:42:21    
相关命令 : 
proxy-enableproxy-service
## immediate-leave 

immediate-leave 
命令功能 : 
配置允许IGMP立即离开的组范围，使用no命令取消限制。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
immediate-leave 
  {all 
|group-list 
 ＜acl-name 
＞}
no immediate-leave 
命令参数解释 : 
参数|描述
---|---
all|所有组播组有效
＜acl-name＞|标准IP访问表名，长度1–31字符
缺省 : 
缺省收到离开报文后，路由器发送指定组查询报文，查询是否还有组成员存在。
使用说明 : 
当配置了该命令，路由器收到离开报文，不发送指定组查询报文，直接删除组。仅对IGMP v2接口有效。如果没有选项，则对所有组播组有效。 
范例 : 
配置允许IGMP立即离开的组范围：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#immediate-leave all 
相关命令 : 
无 
## inactive-holdtime 

inactive-holdtime 
命令功能 : 
配置MSDP邻居inactive状态保持时间。使用no命令恢复缺省值。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER-VRF模式:15,MSDP-PEER模式:15 
命令格式 : 
inactive-holdtime 
  ＜seconds 
＞
no inactive-holdtime 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|MSDP邻居inactive状态保持时间，范围：1–60，单位：秒。
缺省 : 
不设置MSDP邻居inactive状态保持时间，默认值为60秒。 
使用说明 : 
无 
范例 : 
给IP地址为10.10.10.2的MSDP邻居配置邻居inactive状态保持时间为55：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)# inactive-holdtime 55
相关命令 : 
无 
interface : 

interface (IGMP-VRF模式,IGMP模式) 
命令功能 : 
进入IGMP接口配置模式，与接口开启IGMP协议无关，IGMP协议开启由接口开启PIM协议触发，使用no命令删除接口配置，恢复默认配置。 
命令模式 : 
 IGMP-VRF模式,IGMP模式  
命令默认权限级别 : 
IGMP-VRF模式:15,IGMP模式:15 
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
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
进入IGMP接口配置模式，使用no命令删除接口配置，恢复默认配置。 
范例 : 
进入IGMP接口配置模式：ZXROSNG(config)#ip multicast-routing                                      ZXROSNG(config-mcast)#router igmp ZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#
相关命令 : 
无 
interface : 

interface (PIM-VRF模式,PIM模式) 
命令功能 : 
将命令模式切换到PIM接口配置模式下。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
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
＜interface-name＞|接口的名称。
缺省 : 
无 
使用说明 : 
1.将命令模式切换到PIM接口配置模式下；2.不切换到PIM接口配置下，PIM接口下配置命令无法运行。
范例 : 
在路由器接口loopback1上配置interface命令，将命令模式切换到PIM接口配置模式下：ZXROSNG(config-mcast-pim)#interface loopback1ZXROSNG(config-mcast-pim-if-loopback1)#
相关命令 : 
无 
## ip multicast-routing 

ip multicast-routing 
命令功能 : 
启用IP组播路由功能。使用no命令关闭组播路由功能。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ip multicast-routing 
 
no ip multicast-routing 
命令参数解释 : 
					无
				 
缺省 : 
关闭组播功能。 
使用说明 : 
关闭IP组播路由选择功能后，路由器不转发任何组播数据包，同时停止组播路由协议的运行。 
范例 : 
启用IP组播路由功能：ZXROSNG(config)#ip multicast-routing
相关命令 : 
无 
## ip multicast-static-frr 

ip multicast-static-frr 
命令功能 : 
设置回切延迟间隔。在备入接口使用时，主入接口从无效变到UP且有track的话track UP，开始计时，延时WTR时间恢复主入接口。使用no命令取消WTR时间。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
ip multicast-static-frr 
 wtr 
 ＜wtr 
＞
no ip multicast-static-frr 
命令参数解释 : 
参数|描述
---|---
＜wtr＞|静态组播路由入接口回切延迟间隔，范围1-12，单位：分钟
缺省 : 
立即回切。 
使用说明 : 
1．没有配置ip multicast-static-start，不能配置该命令。2．备入接口有效，主入接口从无效切换到有效时，没配置该命令，则立即切换到主入接口，配置该命令则延时WTR后切换。
范例 : 
配置静态组播路由回切延迟时间：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#ip multicast-static-startZXROSNG(config-mcast)#ip multicast-static-frr wtr 6
相关命令 : 
ip multicast-static-startip multicast-static-limitip multicast-static-route
## ip multicast-static-interface 

ip multicast-static-interface 
命令功能 : 
配置静态组播出接口列表，使用no命令删除配置 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
ip multicast-static-interface 
 index 
 ＜index 
＞ interface 
 ＜interface-name 
＞
no ip multicast-static-interface 
 index 
 ＜index 
＞ [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜index＞|出接口列表索引号，范围1-100
＜interface-name＞|与出接口列表索引号关联的接口名
缺省 : 
缺省无出接口列表 
使用说明 : 
1．支持的出接口列表索引号范围是1-100，每个索引下可关联接口的个数最多64个。2．删除出接口列表时既支持删除整个出接口列表，也支持删除某个出接口列表下的某一个接口。3．出接口列表配置后，如删除某一接口，那么出接口列表下关联相应接口自动被删除，当此接口再次被创建时，需重新配置。4．删除出接口列表中的最后一个接口后，该出接口列表也被删除。
范例 : 
将gei-0/1/0/1配置到出接口列表10下：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)#ip multicast-static-interface index 10 interface gei-0/1/0/1
相关命令 : 
show ip multicast-static-interfaceip multicast-static-limitip multicast-static-startip multicast-routing
## ip multicast-static-interface 

ip multicast-static-interface 
命令功能 : 
配置静态组播出接口列表，使用no命令删除配置 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
ip multicast-static-interface 
 index 
 ＜index 
＞ interface 
 ＜interface-name 
＞
no ip multicast-static-interface 
 index 
 ＜index 
＞ [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜index＞|出接口列表索引号，范围1-100
＜interface-name＞|接口名称
缺省 : 
缺省无出接口列表 
使用说明 : 
1．支持的出接口列表索引号范围是1-100，每个索引下可关联接口的个数最多64个。2．删除出接口列表时既支持删除整个出接口列表，也支持删除某个出接口列表下的某一个接口。3．出接口列表配置后，如删除某一接口，那么出接口列表下关联相应接口自动被删除，当此接口再次被创建时，需重新配置。4．删除出接口列表中的最后一个接口后，该出接口列表也被删除。
范例 : 
将gei-0/1/0/1配置到出接口列表10下：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#ip multicast-static-interface index 10 interface gei-0/1/0/1
相关命令 : 
show ip multicast-static-interfaceip multicast-static-limitip multicast-static-startip multicast-routing
## ip multicast-static-limit 

ip multicast-static-limit 
命令功能 : 
配置允许配置的静态组播路由条目数，使用no命令删除配置 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
ip multicast-static-limit 
 xg 
 ＜xg-limit 
＞ sg 
 ＜sg-limit 
＞
no ip multicast-static-limit 
命令参数解释 : 
参数|描述
---|---
＜xg-limit＞|允许配置的静态组播(*,G)路由条目数，范围1~$#134348848#$
＜sg-limit＞|允许配置的静态组播(S,G)路由条目数，范围1~$#134348848#$
缺省 : 
缺省允许配置的静态组播(*,G)和(S,G)路由条目数为0，为0时不能配置静态组播条目 
使用说明 : 
1．配置的静态组播容量不能超过线卡支持的最大容量。2．如果两次配置不同的静态组播容量，第二次配置容量需要比第一次容量大才可直接配，如果需要将容量改小，需要首先将已经配置的容量通过no命令删除，再重新配置较小容量，不可直接配置将容量改小。如果改小会出现错误提示：Parameter can't be smaller than the last configured,delete the last configured first and try again.3.xg和sg条目数的配置范围从1到版本中性能参数规定的值。
范例 : 
配置允许配置的静态组播(*,G)路由条目数为10，(S,G)路由条目数为10：ZXROSNG(config-mcast)#ip multicast-static-limit xg 10 sg 10
相关命令 : 
ip multicast-static-startip multicast-routing
## ip multicast-static-route 

ip multicast-static-route 
命令功能 : 
配置静态组播路由，使用no命令删除配置 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播模式:15,组播VRF模式:15 
命令格式 : 
ip multicast-static-route 
  ＜source-address 
＞ ＜group-address 
＞ [inc-mask 
 ＜mask-address 
＞ count 
 ＜number 
＞] [{[iif 
 ＜in-interface-name 
＞ [track 
 ＜master-track-name 
＞] [slave-iif 
 ＜slave-in-interface-name 
＞ [track 
 ＜slave-track-name 
＞]]],[oif 
 ＜out-interface-index 
＞]]
no ip multicast-static-route 
  ＜source-address 
＞ ＜group-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜source-address＞|静态组播源地址，为十进制点分形式
＜group-address＞|静态组播组地址，为十进制点分形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，十进制点分形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜in-interface-name＞|静态组播条目入接口名
＜master-track-name＞|静态组播路由主入接口关联检测的track名称，长度1-31个字符
＜slave-in-interface-name＞|静态组播条目备入接口名
＜slave-track-name＞|静态组播路由备入接口关联检测的track名称，长度1-31个字符
＜out-interface-index＞|静态组播条目出接口列表索引号
缺省 : 
缺省无静态组播路由 
使用说明 : 
1．静态组播源地址参数在配置(S,G)静态组播路由时为源地址，配置(*,G)静态组播路由时为0.0.0.0。2．没有配置ip multicast-static-limit，无法配置ip multicast-static-route。3．静态组播出接口列表为ip multicast-static-interface命令配置的出接口列表。4．配置静态组播路由备入接口时，必须同时配置主入接口。5．静态组播路由主入接口和备入接口不能是同一个接口。6．批量配置时，掩码步长和数目需要同时配置，确保所有组地址的合法性。7．避免不同配置命令创建相同的路由条目。
范例 : 
1．配置（100.10.50.100，225.1.1.1）静态组播路由，入接口gei-0/1/0/5，出接口列表10：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)# ip multicast-static-route 100.10.50.100 225.1.1.1 iif gei-0/1/0/5 oif 10或者：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)# ip multicast-static-route 100.10.50.100 225.1.1.1 oif 10 iif gei-0/1/0/52．配置静态组播路由主入接口关联检测的track：ZXROSNG(config-mcast)# ip multicast-static-route 100.10.50.100 225.1.1.1 iif gei-0/1/0/1 track test oif 10取消此路由主入接口关联检测的track：ZXROSNG(config-mcast)# ip multicast-static-route 100.10.50.100 225.1.1.1 iif gei-0/1/0/1 oif 103． 配置静态组播路由备入接口：ZXROSNG(config-mcast)# ip multicast-static-route 100.10.50.100 225.1.1.1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 oif 10取消此路由备入接口：ZXROSNG(config-mcast)# ip multicast-static-route 100.10.50.100 225.1.1.1 iif gei-0/1/0/1 oif 104．配置静态组播路由备入接口关联检测的track：ZXROSNG(config-mcast)# ip multicast-static-route 100.10.50.100 225.1.1.1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 track test oif 10取消此路由备入接口关联检测的track：ZXROSNG(config-mcast)# ip multicast-static-route 100.10.50.100 225.1.1.1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 oif 105．批量配置（100.10.50.100，225.1.1.1）静态组播路由，掩码步长0.0.0.1，批量数目为10：ZXROSNG(config-mcast)# ip multicast-static-route 100.10.50.100 225.1.1.1 inc-mask 0.0.0.2 count 10
相关命令 : 
ip multicast-static-startip multicast-static-limitip multicast-static-interfaceip multicast-routing
## ip multicast-static-start 

ip multicast-static-start 
命令功能 : 
启用静态组播路由协议MSTATIC，使用no命令关闭MSTATIC 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
ip multicast-static-start 
 
no ip multicast-static-start 
命令参数解释 : 
					无
				 
缺省 : 
不使能静态组播 
使用说明 : 
1. 默认不启用静态组播，没有启用静态组播时静态组播相关命令将不可用。2. 没有配置ip multicast-routing，MSTATIC路由协议无法运行。
范例 : 
启用静态组播路由协议MSTATIC： ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)#ip multicast-static-start 
相关命令 : 
ip multicast-routing 
## ip-source-check 

ip-source-check 
命令功能 : 
开启IGMP report和leave报文的源地址过滤功能，只有收到的报文和当前接口地址在同一网段才处理，否则丢弃，使用no命令删除。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
ip-source-check 
 
no ip-source-check 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
开启IGMP report和leave报文的源地址过滤功能，只有收到的报文和当前接口地址在同一网段才处理 
范例 : 
在公网实例下，配置loopback1口过滤report 和leave报文的源地址：ZXROSNG(config-mcast-igmp-if-loopback1)#ip-source-check
相关命令 : 
无 
## join-group 

join-group 
命令功能 : 
配置IGMP接口上的静态组成员，要发送report报文，使用no命令删除接口上的静态组成员。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
join-group 
  ＜group-address 
＞ [inc-mask 
 ＜mask-address 
＞ count 
 ＜number 
＞] [source 
 {＜source-address 
＞ [{include 
|exclude 
}]}]
no join-group 
  ＜group-address 
＞ [inc-mask 
 ＜mask-address 
＞] [source 
 ＜source-address 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜group-address＞|静态IGMP加入组地址，十进制点分形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，十进制点分形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜source-address＞|源地址，十进制点分形式
include|切换到模式include
exclude|切换到模式exclude
缺省 : 
无 
使用说明 : 
1.    Join-group配置IGMP接口上的静态组成员要发送report报文，static-goup命令配置的静态组成员不会发送report报文。2.    配置IGMP接口上的静态组成员：join-group ＜group-address＞[inc-mask ＜mask-address＞ count ＜number＞][source ＜source-address＞ [{include|exclude}]]使用no命令删除接口上的静态组成员。3.    接口上批量配置静态组加入：批量配置静态组的时候，需要先使能PIM接口；反之，在删除PIM接口的时候，检查批量静态组是否存在，不存在才能执行no命令。4.   删除接口上批量配置时，必须输入inc-mask参数。5.配置带源的Join group时，接口需使能IGMP v3版本才能发送IGMP v3 report6.Join group配置源信息时可指定include或者exclude模式，也可不指定，不指定模式时默认为include模式
范例 : 
1.配置IGMP接口上的组成员：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#join-group  225.1.1.100ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#join-group  225.0.0.1查看配置结果信息：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#show ip igmp groupsTotal: 2 groupsGroup addr      Interface           Present     Expire      Last Reporter225.0.0.1       gei-0/7/1/2         02:00:26    never       0.0.0.0225.1.1.100     gei-0/7/1/2         00:01:36    never       0.0.0.02.配置loopback1接口加入起始组地址为224.1.1.1，递增掩码步长为0.1.1.1，组地址数量为3的批量组播组：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface loopback1ZXROSNG(config-mcast-igmp-if-loopback1)#join-group 224.1.1.1 inc-mask 0.1.1.1 count 3ZXROSNG(config-mcast-igmp-if-loopback1)#show ip igmp groupsTotal: 3 groupsGroup addr      Interface                      Present/Expire    Last Reporter224.1.1.1       loopback1                      00:00:19/never    1.2.3.4224.2.2.2       loopback1                      00:00:19/never    1.2.3.4224.3.3.3       loopback1                      00:00:19/never    1.2.3.43..配置IGMP接口上的组成员，带源地址为10.1.1.1，include模式:R2(config)#ip multicast-routingR2(config-mcast)#router igmpR2(config-mcast-igmp)#interface fei-0/20/0/2R2(config-mcast-igmp-if-fei-0/20/0/2)#join-group 225.0.0.0 source 10.1.1.1 include查看配置结果信息：R2(config-mcast-igmp-if-fei-0/20/0/2)#show ip igmp groupsTotal: 1 groupsGroup addr      Interface                      Present/Expire    Last Reporter225.0.0.0       fei-0/20/0/2                   00:00:57/never    10.2.2.2R2(config-mcast-igmp-if-fei-0/20/0/2)#show ip igmp groups detailFlags: S - Static Group, SSM - SSM Group, M - MDT GroupInterface:      fei-0/20/0/2Group:          225.0.0.0Flags:Uptime:         00:00:58Group mode:     INCLUDELast reporter:  10.2.2.2Group source list: (M - SSM Mapping, S - Static, R - Report)  Source addr      Present   Expire   Fwd  Flag  10.1.1.1         00:00:58  Never     Yes  SR2(config-mcast-igmp-if-fei-0/20/0/2)#
相关命令 : 
pimsm，pimdm，version 
## join-prune-holdtime 

join-prune-holdtime 
命令功能 : 
设置发送Join/Prune报文的holdtime值。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
join-prune-holdtime 
  ＜seconds 
＞
no join-prune-holdtime 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|设置发送Join/Prune报文的holdtime值的时间，范围：210–65535，单位：秒，默认值为210秒。
缺省 : 
不设置发送Join/Prune报文的holdtime值。 
使用说明 : 
设置发送Join/Prune报文的holdtime值，接收到J/P报文的路由器依据holdtime来确定对应下游接口保持加入或者剪枝状态的时间。通常情况下holdtime的值为发送J/P报文时间间隔的3.5倍。 
范例 : 
设置发Join/Prune报文的holdtime值为270秒：ZXROSNG(config-mcast-pim)#join-prune-holdtime 270
相关命令 : 
无 
## join-prune-interval 

join-prune-interval 
命令功能 : 
设置发送Join/Prune报文的周期，使用no命令恢复默认值。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
join-prune-interval 
  ＜seconds 
＞
no join-prune-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|发送Join/Prune报文的周期，范围：10–6000，单位：秒，默认值为60秒。
缺省 : 
发送Join/Prune报文的周期缺省值60秒。 
使用说明 : 
此命令设置周期性的向上游路由器发送Join/Prune报文的时间间隔，上游路由器收到下游的Join/Prune报文，会更新下游接口状态，维护(*,G)和（S,G）表项。 
范例 : 
设置发送Join/Prune报文的时间间隔为270秒：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#route pimZXROSNG(config-mcast-pim)#join-prune-interval 270
相关命令 : 
无 
## join-prune-speed 

join-prune-speed 
命令功能 : 
配置PIM JP报文每秒发送的表项个数。使用no命令恢复默认值。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
join-prune-speed 
  ＜speed 
＞
no join-prune-speed 
命令参数解释 : 
参数|描述
---|---
＜speed＞|每秒发送的表项个数，范围：1000-50000，单位：个/秒
缺省 : 
PIM JP报文每秒发送的表项个数，缺省为210个/秒 
使用说明 : 
需先使能PIM才能配置此命令 
范例 : 
配置 join-prune-speed：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router pim ZXROSNG(config-mcast-pim)# join-prune-speed 2000
相关命令 : 
router pim：使能PIM。 
## jp-max-packet-length 

jp-max-packet-length 
命令功能 : 
配置PIM发送的Join/Prune报文的最大长度。使用no命令取消配置。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM-VRF接口模式:15,PIM接口模式:15 
命令格式 : 
jp-max-packet-length 
  ＜bytes 
＞
no jp-max-packet-length 
命令参数解释 : 
参数|描述
---|---
＜bytes＞|PIM发送的Join/Prune报文的最大长度，范围：100-8100，单位：字节
缺省 : 
PIM发送的Join/Prune报文的最大长度，缺省为1400字节。 
使用说明 : 
接口下需先使能PIM才能配置此命令。jp-max-packet-length命令配置的报文长度如果大于接口IP MTU值，则实际报文发送最大长度为接口IP MTU值。实际报文最小长度小于此配置，则按照实际报文长度发送。对于(S,G,rpt)剪枝的场景，命令配置的报文长度小于1400，如果该大小能装下该组所有的(S,G,rpt)剪枝，则用当前报文大小，如果装不下，则按照1400发包，配置长度大于1400则按照命令配置发包。 
范例 : 
ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router pim ZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#pimsm ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#jp-max-packet-length 100
相关命令 : 
ip mtu:配置接口上的IP MTU。pimsm：配置接口上的PIM-SM。pimdm：配置接口上的PIM-DM。
## keepalive-period 

keepalive-period 
命令功能 : 
配置MSDP邻居报文发送时间间隔。使用no命令恢复缺省值。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
keepalive-period 
  ＜seconds 
＞
no keepalive-period 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|MSDP邻居报文发送时间间隔，范围：1–60，单位：秒。
缺省 : 
不设置MSDP邻居报文发送时间间隔，默认值为60秒。 
使用说明 : 
无 
范例 : 
给IP地址为10.10.10.2的MSDP邻居配置邻居报文发送时间间隔为44：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)# keepalive-period 44
相关命令 : 
无 
## keychain 

keychain 
命令功能 : 
配置TCP连接建立时的keychain认证。使用no命令取消keychain认证。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
keychain 
  ＜keychain 
＞
no keychain 
命令参数解释 : 
参数|描述
---|---
＜keychain＞|keychain的名称，长度1-31个字符。
缺省 : 
无 
使用说明 : 
1.keychain与password命令互斥。2.不校验keyhcain实例是否存在。
范例 : 
给MSDP邻居TCP连接配置密码：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 101.1.1.1ZXROSNG(config-mcast-msdp-peer)#keychain zte
相关命令 : 
无 
## last-member-query-interval 

last-member-query-interval 
命令功能 : 
配置IGMP最后成员查询间隔，使用no命令恢复缺省值。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
last-member-query-interval 
  ＜seconds 
＞
no last-member-query-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|组查询间隔，缺省为1秒，范围：1–25，单位：秒
缺省 : 
无 
使用说明 : 
当查询路由器收到离开报文，立即发送指定组查询报文，为保证指定组查询报文的顺利到达，会发送多次，此命令就是设置指定组查询报文发送间隔的。
范例 : 
配置IGMP特定组查询间隔：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#last-member-query-interval 10
相关命令 : 
无 
## longest-match 

longest-match 
命令功能 : 
通过用户配置组播选择单播路由规则的，从mbgp migp 和单播转发表中选组播路由的规则。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
longest-match 
 
no longest-match 
命令参数解释 : 
					无
				 
缺省 : 
没有配置 
使用说明 : 
1.通过用户配置组播选择单播路由规则的，从mbgp migp 和单播转发表中选组播路由的规则 配置后按照最长匹配规则去匹配。 
范例 : 
ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# longest-match
相关命令 : 
ip multicast-routing 
## maximum-joins 

maximum-joins 
命令功能 : 
配置igmp接口允许的最大加入数，使用no命令取消限制。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
maximum-joins 
  ＜number 
＞
no maximum-joins 
命令参数解释 : 
参数|描述
---|---
＜number＞|IGMP接口允许的最大加入数，范围：1-40000
缺省 : 
无 
使用说明 : 
限制此命令生效之后的动态组加入。
范例 : 
配置IGMP最大加入数：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#maximum-joins 100
相关命令 : 
无 
## mdt auto-discovery 

mdt auto-discovery 
命令功能 : 
配置后mdt自动发现控制开关 打开之后会自动收发ad路由进行自动发现。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mdt auto-discovery 
 
no mdt auto-discovery 
命令参数解释 : 
					无
				 
缺省 : 
没有配置mdt自动发现 
使用说明 : 
配置mdt自动发现控制开关 打开之后会自动收发ad路由进行自动发现 
范例 : 
ZXROSNG(config-mcast-vrf-zte)#mdt auto-discovery ZXROSNG(config-mcast-vrf-zte)#
相关命令 : 
无 
## mdt data 

mdt data 
命令功能 : 
配置组播某实例的mdt data信息。使用no命令取消配置。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mdt data 
  {mpls-mldp 
 ＜num-tree 
＞|＜group-address 
＞ ＜wildcard 
＞ [＜acl-name 
＞]}
no mdt data 
命令参数解释 : 
参数|描述
---|---
＜num-tree＞|配置Data MDT可选范围，配置范围1-5000
＜group-address＞|VRF实例的MDT data group组地址
＜wildcard＞|VRF实例的MDT data group组掩码（反掩码）
＜acl-name＞|ACL名称，长度1-31个字符
缺省 : 
不配置组播某实例的mdt data。 
使用说明 : 
需要先配置VRF实例，才能在组播VRF配置模式下通过此命令配置mdt data。要求配置的反掩码范围在16位及以上。 
范例 : 
1.配置组播某实例的mdt data group：ZXROSNG(config-mcast-vrf-zte)#mdt data 224.1.1.1 0.0.0.2552.配置组播某实例带ACL的mdt data group：ZXROSNG(config-mcast-vrf-zte)#mdt data 224.1.1.1 0.0.0.255 test3.配置组播某实例的mdt data mpls-mldp：ZXROSNG(config-mcast-vrf-zte)#mdt data mpls-mldp 5
相关命令 : 
ip vrfaddress-familyrd
## mdt default 

mdt default 
命令功能 : 
配置组播某实例的mdt default 信息。使用no命令取消配置。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mdt default 
  {＜group-address 
＞|mpls-mldp 
 ＜root-address 
＞}
no mdt default 
  {＜group-address 
＞|mpls-mldp 
 ＜root-address 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜group-address＞|VRF实例的MDT default group组地址
＜root-address＞|远端PE地址，配置后即创建以该地址为根的LSP
缺省 : 
不配置组播某实例的mdt default。 
使用说明 : 
需要先配置VRF实例，才能在组播VRF配置模式下通过此命令配置mdt default。mdt default mpls-mldp分支命令最多可配32条。
范例 : 
配置组播某实例的mdt default group地址：ZXROSNG(config-mcast-vrf-zte)#mdt default 225.1.1.1 配置组播某实例的mdt default mpls-mldp地址：ZXROSNG(config-mcast-vrf-zte)#mdt default mpls-mldp 1.1.1.10
相关命令 : 
ip vrfaddress-familyrd
## mesh-group 

mesh-group 
命令功能 : 
配置指定的MSDP邻居为某mesh group成员。使用no命令删除设置。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
mesh-group 
  ＜mesh-group 
＞
no mesh-group 
命令参数解释 : 
参数|描述
---|---
＜mesh-group＞|Mesh group的名称，长度1-32个字符
缺省 : 
无 
使用说明 : 
1.    mesh group是一个由MSDP发言者组成，且两两之间均有MSDP连接的组。收到来自于同一mesh group中MSDP邻居的SA报文时，不会向此mesh group的其他MSDP邻居转发。使用mesh group可以达到以下两个目的：a 减少SA消息的泛滥。b 简化邻居RPF检查机制（不需要在MSDP邻居间运行BGP或MBGP）。2.    这个命令配置将显示在show ip msdp peer命令的输出结果中。
范例 : 
将地址为10.10.10.2的MSDP邻居配置成名称为zte的mesh-group的成员：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)#mesh-group zte
相关命令 : 
无 
## mldp-signal filter 

mldp-signal filter 
命令功能 : 
只有符合ACL规则的SG路由才能够向向MLDP通告触发Inbind Signaling行为，使用no命令取消限制。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
mldp-signal filter 
  ＜access-list-name 
＞
no mldp-signal filter 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|ACL名称，用于指定组播源和组地址
缺省 : 
无 
使用说明 : 
配置了该命令以后，只有该ACL访问表允许的（S，G）同时满足相关通告条件的路由才会向MLDP通告触发Inbind Signaling行为。 
范例 : 
在公网PIM实例上配置：ZXROSNG(config) #ip multicast-routingZXROSNG(config-mcast) #router pimZXROSNG(config-mcast-pim)# mldp-signal filter zte在私网实例上启用mldp Inbind Signaling功能：ZXROSNG(config) #ip multicast-routingZXROSNG(config-mcast) #vrf aZXROSNG(config-mcast -vrf-a) #router pimZXROSNG(config-mcast -vrf-a -pim)# mldp-signal filter zte
相关命令 : 
无 
## mldp-signal 

mldp-signal 
命令功能 : 
mldp Inbind Signaling功能开关，使能使用mldp-signal enable，去使能使用mldp-signal disable。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
mldp-signal 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能mldp Inbind Signaling功能
disable|去使能mldp Inbind Signaling功能
缺省 : 
不使能。 
使用说明 : 
如果实例下没有配置mldp-signal使能，对于组播SG路由，即使满足到源的单播下一跳是MBGP路由并且上游PIM邻居不存在的条件，也不会触发通告MLDP触发inbind Signaling行为。 
范例 : 
在公网PIM实例上启用mldp Inbind Signaling功能：ZXROSNG(config) #ip multicast-routingZXROSNG(config-mcast) #router pimZXROSNG(config-mcast-pim)# mldp-signal enable在私网实例上启用mldp Inbind Signaling功能：ZXROSNG(config) #ip multicast-routingZXROSNG(config-mcast) #vrf aZXROSNG(config-mcast -vrf-a) #router pimZXROSNG(config-mcast -vrf-a -pim)# mldp-signal enable
相关命令 : 
无 
## mofrr 

mofrr 
命令功能 : 
开启MoFRR功能，只有符合ACL规则的sg路由条目才能开启，使用no命令恢复缺省状态。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
mofrr 
  ＜access-list-name 
＞
no mofrr 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|ACL名，长度1-31个字符。
缺省 : 
不开启MoFRR功能。 
使用说明 : 
此命令配置后，在SPT切换时，下发路由能在一定时间内保持两个入接口都有效，即从SPT和RPT过来的流量都能转发，可以减少SPT切换丢包的数量。配置ACL规则是来过滤(S,G)路由条目的源地址和组地址的。 
范例 : 
开启MoFRR功能：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#route pimZXROSNG(config-mcast-pim)#mofrr zte
相关命令 : 
show ip pim mroute 
## monitor-interface 

monitor-interface 
命令功能 : 
配置组播监控接口，使用no命令取消配置。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
monitor-interface 
  ＜interface-name 
＞
no monitor-interface 
  [＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
缺省 : 
不配置组播监控接口。 
使用说明 : 
1.配置monitor-interface监控接口命令 ，需要和monitor-mroute命令一起使用监控功能。2.monitor-mroute配置监控路由时，如果没有指定监控接口参数，则该条路由正常同步。如果配置的接口参数在monitor-interface配置的参数中 则断流 ，不在其中就正常同步。
范例 : 
配置组播监控接口ZXROSNG(config-mcast)#monitor-interface gei-0/1/0/1
相关命令 : 
无 
## monitor-mroute 

monitor-mroute 
命令功能 : 
配置组播监控路由。使用no命令取消配置。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
monitor-mroute 
  ＜source-address 
＞ ＜group-address 
＞ [interface 
 ＜interface-name 
＞]
no monitor-mroute 
  ＜source-address 
＞ ＜group-address 
＞ [interface 
 ＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜source-address＞|源地址，十进制点分形式
＜group-address＞|组地址，十进制点分形式
＜interface-name＞|接口名称
缺省 : 
不配置组播监控路由。 
使用说明 : 
1.配置monitor-mroute监控路由命令 ，需要和monitor-interface命令一起使用监控功能。如果没有配置monitor-interface 则路由断流。2.monitor-mroute配置监控路由时，如果没有指定监控接口参数，则该条路由正常同步。如果配置的接口参数在monitor-interface配置的参数中 则断流 ，不在其中就正常同步。3.目前仅对公网有效。
范例 : 
配置组播监控路由ZXROSNG(config-mcast)#monitor-mroute 100.10.10.1 226.0.0.1 interface gei-0/1/0/1
相关命令 : 
monitor-interface 
## mroute-downstream-limit 

mroute-downstream-limit 
命令功能 : 
通过用户命令，用户可以根据实际组网情况和业务性能要求对组播转发表中单条表项的下行节点数目（即出接口数目）进行限制，以缓解路由器的复制压力。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
mroute-downstream-limit 
  ＜limit 
＞
no mroute-downstream-limit 
命令参数解释 : 
参数|描述
---|---
＜limit＞|配置出接口数目，范围最大值通过性能参数动态获取，范围为1-$#134348804#$
缺省 : 
正常生成出接口条目。 
使用说明 : 
1.通过配置limit参数先设置下流出接口的数目范围，范围最大值通过性能参数动态获取. 
范例 : 
配置组播转发表中单条表项的下行节点数目限制ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# mroute-downstream-limit 24
相关命令 : 
ip multicast-routing 
## mroute-limit p-instance 

mroute-limit p-instance 
命令功能 : 
根据实际组网情况和业务性能要求，配置组播公网路由条目数量限制。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
mroute-limit p-instance 
  ＜limit 
＞
no mroute-limit p-instance 
命令参数解释 : 
参数|描述
---|---
＜limit＞|配置公网路由条目数量限制，范围1~$#134348824#$。
缺省 : 
没有配置组播公网路由条目数量限制。 
使用说明 : 
1．命令配置不设置约束，即单实例数量限制可以大于全局数量限制。2．limit的配置范围，从1到版本中性能参数规定的值。
范例 : 
配置组播公网路由条目数量限制ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# mroute-limit p-instance 1%Info 9030: Reload or use 'clear ip mroute' command, this command may take effect.
相关命令 : 
mroute-limit 
## mroute-limit 

mroute-limit 
命令功能 : 
根据实际组网情况和业务性能要求，配置组播路由条目数量限制。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
mroute-limit 
  ＜limit 
＞
no mroute-limit 
命令参数解释 : 
参数|描述
---|---
＜limit＞|配置路由条目数目限制，范围1~$#134348824#$
缺省 : 
没有配置组播路由条目限制。 
使用说明 : 
1．组播模式下，配置此命令，控制全局路由条目数量限制。2．组播VRF模式下，配置此命令，控制此VRF实例下路由条目数量限制。3．命令配置不设置约束，即单实例数量限制可以大于全局数量限制。4．limit的配置范围，从1到版本中性能参数规定的值。
范例 : 
1．配置组播全局路由条目数量限制ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# mroute-limit 1024%Info 9030: Reload or use 'clear ip mroute' command, this command may take effect.2．配置vrf1实例下路由条目数量限制ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)#vrf vrf1ZXROSNG(config-mcast-vrf-vrf1)#mroute-limit 1000%Info 9030: Reload or use 'clear ip mroute' command, this command may take effect.
相关命令 : 
mroute-limit p-instance 
## mroute-proxy 

mroute-proxy 
命令功能 : 
在下游接口，又称路由器接口上，配置proxy功能所对应的上游接口，出接口包括该接口的（*,G）条目，可以在上游接口上发送IGMP report消息，使用no命令恢复缺省状态。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
mroute-proxy 
  ＜interface-name 
＞
no mroute-proxy 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|proxy功能所对应的上游接口
缺省 : 
无 
使用说明 : 
在IGMP接口模式下配置mroute-proxy <interface-name>,该接口下所有的组成员将通过proxy接口往上游路由器发report报文,但是需要确保该proxy接口本身属于对应组形成的XG的出接口。除此之外,还需要配置如下命令才能使该命令生效：1. IGMP模式下配置proxy enable2. proxy接口在IGMP接口模式下配置proxy service
范例 : 
配置接口上proxy的上游接口：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#mroute-proxy fei-0/1/0/2查看配置结果信息：ZXROSNG#show ip igmp proxy groupsTotal: 1 groupsGroup addr      Interface           Present239.255.255.250 fei-0/1/0/2         01:42:21    
相关命令 : 
proxy-enableproxy-service
## mtrace 

mtrace 
命令功能 : 
查找到源的逆向路径。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
mtrace 
  ＜source-address 
＞ [＜destination-address 
＞ [＜group-address 
＞]]
命令参数解释 : 
参数|描述
---|---
＜source-address＞|源地址，十进制点分形式
＜destination-address＞|目的地址，十进制点分形式
＜group-address＞|组地址，十进制点分形式
缺省 : 
无 
使用说明 : 
1. 如果只有源地址参数选项，则查找到源的单播路由。2. 如果选择组地址选项，如果匹配不到(s，g)则匹配(*，g)。3. 如果选择组和目的地址选项，则查找从源地址到目的地址的组播路由。
范例 : 
查找到源的逆向路径：ZXROSNG#mtrace 5.1.1.2 Type escape sequence to abort.Mtrace from 5.1.1.2 to  via RPF-1 5.1.1.1 PIM  93 ms NO_ROUTE  [finished]ZXROSNG#mtrace 5.1.1.1 5.1.1.2 227.0.0.1 Type escape sequence to abort.Mtrace from 5.1.1.1 to 5.1.1.2 via group 227.0.0.10 5.1.1.2 PIM  4 ms-1 5.1.1.1 PIM  93 ms NO_ROUTE  [finished]
相关命令 : 
无 
## mtunnel 

mtunnel 
命令功能 : 
将接口配置成mtunnel接口模式。使用no命令取消mtunnel接口配置。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mtunnel 
  ＜interface-name 
＞
no mtunnel 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口的名称
缺省 : 
不配置mtunnel接口。 
使用说明 : 
1.需要先配置VRF实例，才能在组播VRF配置模式下通过此命令配置mtunnel接口。2.接口使用公网接口
范例 : 
将lookback1接口配置成mtunnel接口模式：ZXROSNG(config-mcast-vrf-zte)#mtunnel loopback1
相关命令 : 
ip vrfaddress-familyrd：在VRF实例创建后需要进一步配置rd，才能使能实例供mtunnel等其他命令使用。
## multicast-boundary 

multicast-boundary 
命令功能 : 
通过用户命令，在接口上配置组播转发边界，以形成一个封闭的组播转发区域 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
multicast-boundary 
  ＜access-list-name 
＞ ＜interface-name 
＞
no multicast-boundary 
  [＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|配置过滤地址的规则
＜interface-name＞|接口名称
缺省 : 
接口未设置组播转发边界 
使用说明 : 
1.通过用户命令，在接口上配置组播转发边界，以形成一个封闭的组播转发区域，符合规则的组播组将不会被转发。2，如果边界配置在入接口上则停止转发这条路由的流量，配置在出接口上则停止该接口流量。
范例 : 
在接口上配置组播转发边界ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# multicast-boundary zte gei-0/1/0/1
相关命令 : 
ip multicast-routing 
## multicast-ttl 

multicast-ttl 
命令功能 : 
配置组播转发ttl限制。使用no命令取消配置。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
multicast-ttl 
  ＜limit 
＞ ＜interface-name 
＞
no multicast-ttl 
  [＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜limit＞|ttl限制值，范围 <1-255>
＜interface-name＞|接口名称
缺省 : 
不配置组播转发ttl限制。 
使用说明 : 
限制组播数据包的转发，如果收到的组播数据包中ttl值小于配置的<ttl-limit>，则不再转发。 
范例 : 
配置组播转发ttl限制：ZXROSNG(config-mcast)#multicast-ttl 11 vlan10
相关命令 : 
无。 
## multipath 

multipath 
命令功能 : 
配置组播负荷分担模式。使用no命令取消配置。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
multipath 
  [s-g-hash 
 {basic 
|next-hop-based 
|balance 
}]
no multipath 
命令参数解释 : 
参数|描述
---|---
basic|默认基于源组的哈希
next-hop-based|基于下一跳的哈希
balance|基于接口上ecmp-cost的哈希
缺省 : 
关闭组播负荷分担。 
使用说明 : 
1. 如果没有参数选项，则使用基于源的哈希算法分担负荷。2. 如果选择basic选项，则使用基于源组的哈希算法分担负荷。3. 如果选择next-hop-based选项，则使用基于下一跳的哈希算法分担负荷。 4. 如果选择balance选项，则使用基于接口上ecmp-cost的哈希算法分担负荷。
范例 : 
1.配置基于源的组播负荷分担模式：ZXROSNG(config-mcast)#multipath 2.配置基于源组的组播负荷分担模式：ZXROSNG(config-mcast)#multipath s-g-hash basic3.配置基于下一跳的组播负荷分担模式：ZXROSNG(config-mcast)#multipath s-g-hash next-hop-based4.配置基于接口上ecmp-cost的组播负荷分担模式：ZXROSNG(config-mcast)#multipath s-g-hash balance
相关命令 : 
无 
## mvpn receive-site-only 

mvpn receive-site-only 
命令功能 : 
配置MVPN 为receive site only模式。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mvpn receive-site-only 
 
no mvpn receive-site-only 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下MVPN为send  site和receive site共存模式。 
使用说明 : 
1. 配置为receive site only模式下，本地PE只接收私网数据，出接口不再添加隧道接口。 
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)# mvpn receive-site-only
相关命令 : 
本命令与mvpn send-site-only互斥 
## mvpn send-site-only 

mvpn send-site-only 
命令功能 : 
配置MVPN 为send site only模式。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mvpn send-site-only 
 
no mvpn send-site-only 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下MVPN为send  site和receive site共存模式。 
使用说明 : 
1. 配置为send site only模式下，本地PE只发送私网数据，不再向上游PE发送XG和SG加入路由。 
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)# mvpn send-site-only
相关命令 : 
本命令与mvpn receive-site-only互斥 
## mvpn spmsi aggregation 

mvpn spmsi aggregation 
命令功能 : 
配置MVPN SPMSI隧道聚合。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mvpn spmsi aggregation 
  {source-based 
|＜count 
＞}
no mvpn spmsi aggregation 
命令参数解释 : 
参数|描述
---|---
source-based|每MVPN SPMSI隧道基于源地址聚合组播路由条目。
＜count＞|每MVPN SPMSI隧道聚合组播路由条目数量，范围：1~$#134348802#$
缺省 : 
每MVPN SPMSI隧道最多可聚合200条组播路由条目。 
使用说明 : 
1. 如果没有配置此命令，每MVPN SPMSI隧道最多可聚合200条组播路由条目。2. 如果选择source-based选项，则相同源的组播路由聚合到相同的MVPN SPMSI隧道。3. 如果选择count选项，每MVPN SPMSI隧道最多可聚合<count>条组播路由条目。 4. 单播隧道不适用以上规则，按照每路由每隧道聚合。5. 此命令只对新建SPMSI生效，已有的SPMSI隧道不响应此命令变更。
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)# mvpn spmsi aggregation source-based
相关命令 : 
无 
## mvpn spt-only 

mvpn spt-only 
命令功能 : 
配置MVPN 为SPT only模式，即私网只有SPT才能穿越公网。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mvpn spt-only 
 
no mvpn spt-only 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下MVPN为spt-rpt模式，私网SPT和RPT均可穿越公网。 
使用说明 : 
1. 配置为spt-only模式下，私网RPT将不再穿越公网. 
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)# mvpn spt-only
相关命令 : 
无 
## mvpn switchover interval 

mvpn switchover interval 
命令功能 : 
配置MVPN隧道切换间隔。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mvpn switchover interval 
  ＜seconds 
＞
no mvpn switchover interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|MVPN隧道切换间隔，范围：3–65535，单位：秒
缺省 : 
无 
使用说明 : 
配置MVPN 隧道切换延时间隔，MDT场景为default MDT向data MDT切换延时，MVPN场景为I-PMSI向S-PMSI切换延时。 
范例 : 
配置MVPN隧道切换延迟间隔为10秒：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)# mvpn switchover interval 10
相关命令 : 
无 
## mvpn switchover threshold-infinity 

mvpn switchover threshold-infinity 
命令功能 : 
配置MVPN隧道永不切换。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
mvpn switchover threshold-infinity 
 group-list 
 ＜access-list-name 
＞
no mvpn switchover threshold-infinity 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|ACL名，长度1-31个字符。
缺省 : 
无 
使用说明 : 
配置MVPN永不切换ACL。当该ACL规则permit时，MDT场景不向data MDT切换，MVPN场景不向S-PMSI切。配置ACL规则是来过滤(*,G)或者(S,G)路由条目的源地址和组地址的。 
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)# mvpn switchover threshold-infinity group-list aaa
相关命令 : 
无 
## neighbor-filter 

neighbor-filter 
命令功能 : 
限制某些路由器成为PIM邻居，使用no命令取消限制。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
neighbor-filter 
  ＜access-list-name 
＞
no neighbor-filter 
命令参数解释 : 
参数|描述
---|---
＜access-list-name＞|它定义了一个地址范围，该范围是对成为PIM邻居的路由器的限定。
缺省 : 
缺省情况下不限制其它路由器成为PIM邻居。 
使用说明 : 
配置此命令后，满足ACL过滤规则的邻居将被过滤掉，不能成为路由器的邻居。 
范例 : 
在接口gei-0/1/0/1上禁止访问控制列表zte限定的路由器成为PIM邻居：ZXROSNG(config)#ipv4-access-list zteZXROSNG(config-ipv4-acl)#rule 1 deny 20.1.1.1 0.0.0.0ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#neighbor-filter zte
相关命令 : 
无 
## nexthop 

nexthop 
命令功能 : 
配置单播路由静态下一跳。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
nexthop 
  ＜ip-address 
＞ ＜network-mask 
＞ {＜interface-name 
＞ ＜nexthop 
＞ [{[slave 
],[track 
 ＜track-name 
＞]}]|fallback-lookup 
 vrf 
 ＜vrf-name 
＞|path-list 
 ＜path-list-name 
＞}
no nexthop 
  ＜ip-address 
＞ ＜network-mask 
＞ [＜interface-name 
＞ ＜nexthop 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|目的地址, 可以为主机地址或网络地址
＜network-mask＞|网络地址掩码
＜interface-name＞|下一跳出接口
＜nexthop＞|下一跳地址
slave|备下一跳标记
＜track-name＞|下一跳TRACK名称，长度1-31字符
＜vrf-name＞|fallback私网实例VRF名称，长度1-32字符
＜path-list-name＞|RPF路径列表名称，长度1-31字符
缺省 : 
不配置静态下一跳 
使用说明 : 
1. 对于一个目的地址或网段可以配置多个静态下一跳。指定下一跳出接口和下一跳地址。2. 可以使用static-first命令提高静态下一跳优先级。3. 对于同一个目的地址或网段，只能有一条nexthop带slave参数，带slave参数的nexthop存在时，另外只能有一条不带slave参数的nexthop，此时形成FRR，并且和ECMP互斥。4. 静态配置path-list功能和fallback功能和具体路径功能（ECMP和FRR）互斥，同一目的网段的fallback配置不能直接修改，必须先删除再重新配置，且不能配置fallback到当前实例。5. 公网配置fallback或path-list可以进入nexthop模式，但不能配置select-mroute。6. 配置track选项用于监测下一跳是否有效。
范例 : 
1. 配置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.3：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.3  2. 配置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.4为备下一跳：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.4 slave3. 配置到目的地址10.10.10.3的单播路由fallback到私网实例vrf1：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# nexthop 10.10.10.3 255.255.255.255 fallback-lookup vrf vrf1ZXROSNG(config-mcast-nexthop)#4. 配置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.3，带track选项：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.3 track abc5. 配置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.4为备下一跳且带track选项：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.4 slave track abc6. 配置到目的地址10.10.10.2的单播路由下一跳迭代查找RPF路径列表abc的单播下一跳：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# nexthop 10.10.10.2 255.255.255.255 path-list abc
相关命令 : 
static-firstrpf-proxy-vector path-list
## nexthop 

nexthop 
命令功能 : 
配置单播路由静态下一跳。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
nexthop 
  ＜ip-address 
＞ ＜network-mask 
＞ {＜interface-name 
＞ ＜nexthop 
＞ [{[slave 
],[track 
 ＜track-name 
＞]}]|fallback-lookup 
 {global 
|vrf 
 ＜vrf-name 
＞}}
no nexthop 
  ＜ip-address 
＞ ＜network-mask 
＞ [＜interface-name 
＞ ＜nexthop 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|目的地址, 可以为主机地址或网络地址
＜network-mask＞|网络地址掩码
＜interface-name＞|下一跳出接口
＜nexthop＞|下一跳地址
slave|备下一跳标记
＜track-name＞|下一跳TRACK名称，长度1-31字符
global|fallback公网实例
＜vrf-name＞|fallback私网实例VRF名称，长度1-32字符
缺省 : 
不配置静态下一跳 
使用说明 : 
1. 对于一个目的地址或网段可以配置多个静态下一跳。指定下一跳出接口和下一跳地址。2. 可以使用static-first命令提高静态下一跳优先级。3. 对于同一个目的地址或网段，只能有一条nexthop带slave参数，带slave参数的nexthop存在时，另外只能有一条不带slave参数的nexthop，此时形成FRR，并且和ECMP互斥。4. 静态配置fallback功能和具体路径功能（ECMP和FRR）互斥，同一目的网段的fallback配置不能直接修改，必须先删除再重新配置，且不能配置fallback到当前实例。5. 配置track选项用于监测下一跳是否有效。
范例 : 
1. 配置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.3：ZXROSNG(config-mcast)# nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.3  2. 配置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.4为备下一跳：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.4 slave3. 私网vrf1实例下配置到目的地址10.10.10.3的单播路由fallback到公网实例：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#vrf vrf1ZXROSNG(config-mcast-vrf-vrf1)# nexthop 10.10.10.3 255.255.255.255 fallback-lookup globalZXROSNG(config-mcast-vrf-vrf1)#4. 私网vrf1实例下配置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.3，带track选项：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf vrf1ZXROSNG(config-mcast-vrf-vrf1)# nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.3 track abc5. 私网vrf1实例下配置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.4为备下一跳且带track选项：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf vrf1ZXROSNG(config-mcast-vrf-vrf1)#nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.4 slave track abc
相关命令 : 
static-first 
## nsf-lifetime 

nsf-lifetime 
命令功能 : 
通过用户配置此命令，预估备板倒换后路由收敛时间后，组播重新开始生成路由。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
nsf-lifetime 
  ＜time 
＞
no nsf-lifetime 
命令参数解释 : 
参数|描述
---|---
＜time＞|配置组播主备倒换时间，配置范围30-1800
缺省 : 
默认配置为60秒。 
使用说明 : 
1.一般配置此命令值尽量配大一点，保证备板倒换完成2.一般在倒换时间之内无法配置组播相关命令。
范例 : 
ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# nsf-lifetime 600
相关命令 : 
ip multicast-routing 
## older-version-querier-present 

older-version-querier-present 
命令功能 : 
配置在上游接口上，在收到低版本查询以后，配置等待可以发送高版本report消息的时间间隔，使用no命令恢复缺省状态。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
older-version-querier-present 
  ＜seconds 
＞
no older-version-querier-present 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|缺省值为400秒,配置范围60-32000，单位秒。
缺省 : 
缺省值为400秒 
使用说明 : 
配置等待发送高版本report消息的时间间隔 
范例 : 
配置等待发送高版本report消息的时间间隔：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#older-version-querier-present 200
相关命令 : 
无 
## originator-id 

originator-id 
命令功能 : 
把指定接口的IP地址用作SA消息中的RP地址。使用no命令取消设置。 
命令模式 : 
 MSDP-VRF模式,MSDP模式  
命令默认权限级别 : 
MSDP模式:15,MSDP-VRF模式:15 
命令格式 : 
originator-id 
  ＜interface-name 
＞
no originator-id 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
缺省 : 
RP地址被用作originator-id 
使用说明 : 
无 
范例 : 
把指定接口的IP地址用作SA消息中的RP地址：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#originator-id gei-0/3/0/8
相关命令 : 
无 
## override-interval 

override-interval 
命令功能 : 
配置PIM接口的否决间隔。使用no命令取消配置。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
override-interval 
  ＜100 milliseconds 
＞
no override-interval 
命令参数解释 : 
参数|描述
---|---
＜100 milliseconds＞|PIM接口的否决间隔，范围：1-600，单位：一百毫秒
缺省 : 
PIM接口的否决间隔，缺省为25百毫秒 
使用说明 : 
接口下需先使能PIM才能配置此命令 
范例 : 
在路由器接口gei-0/1/0/1上配置override-interval：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router pim ZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-pim-if-gei-0/1/0/1)# override-interval 100
相关命令 : 
pimsm：配置接口上的PIM-SM。配置PIM接口的否决间隔与配置接口上PIM-SM前置依赖。pimdm：配置接口上的PIM-DM。配置PIM接口的否决间隔与配置接口上PIM-DM前置依赖。
## password 

password 
命令功能 : 
配置TCP连接建立的密码。使用no命令删除密码。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
password 
  {encrypted 
 ＜encrypted-password 
＞|clear 
 ＜password 
＞|＜password 
＞}
no password 
命令参数解释 : 
参数|描述
---|---
＜encrypted-password＞|加密后的MSDP邻居TCP连接建立密码，长度为81-120字符。
＜password＞|MSDP邻居TCP连接建立密码，长度1-80个字符。
＜password＞|MSDP邻居TCP连接建立密码，长度1-80个字符。
缺省 : 
无 
使用说明 : 
1）配置命令参数为encryped-password表示配置MSDP建链的密文形式密码时，要保证配置的密文能够解密；2）password ＜password＞ 表示配置MSDP建链的明文形式密码，但是不能配置以字母e开头的明文密码；3）password clear ＜password＞ 参数clear表示配置MSDP建链的明文形式密码，可以配置任何合法的明文密码。
范例 : 
给MSDP邻居TCP连接配置密码：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#route msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)#password hello
相关命令 : 
无 
## peer 

peer 
命令功能 : 
配置MSDP邻居。使用no命令删除MSDP邻居。 
命令模式 : 
 MSDP-VRF模式,MSDP模式  
命令默认权限级别 : 
MSDP模式:15,MSDP-VRF模式:15 
命令格式 : 
peer 
  ＜peer-address 
＞
no peer 
  ＜peer-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜peer-address＞|MSDP邻居的IP地址，十进制点分形式
缺省 : 
无 
使用说明 : 
无 
范例 : 
将IP地址为10.10.10.2的路由器配置为本地路由器的MSDP邻居：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2
相关命令 : 
show ip msdp peer 
## pimdm 

pimdm 
命令功能 : 
接口启用组播PIM-DM协议。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
pimdm 
 
no pimdm 
命令参数解释 : 
					无
				 
缺省 : 
接口未启用PIM-DM。 
使用说明 : 
选定的接口启用组播PIM-DM协议。 
范例 : 
在接口gei-0/1/0/1上配置interface命令，开启组播PIM-DM协议：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#pimdm
相关命令 : 
interface：必须先进入PIM接口配置模式。show ip pim interface: 显示接口相关信息。
## pimdm-reg 

pimdm-reg 
命令功能 : 
入接口配置为PIM-DM模式时，配置该命令，设备收到非直连流量也需要向RP注册。 
命令模式 : 
 PIM模式  
命令默认权限级别 : 
15 
命令格式 : 
pimdm-reg 
 
no pimdm-reg 
命令参数解释 : 
					无
				 
缺省 : 
默认情况设备收到非直连流量不需向RP注册。 
使用说明 : 
入接口为PIM-DM模式，配置了pimdm-reg命令，设备收到非直连流量也需要向RP发送注册报文。 
范例 : 
配置pimdm-reg命令，设备收到非直连流量向RP注册：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)# pimdm-reg
相关命令 : 
无 
## pim-group 

pim-group 
命令功能 : 
创建pim-group，使用no删除pim-group 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
pim-group 
  ＜group-name 
＞
no pim-group 
  ＜group-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-name＞|pim组名字，长度1-31字符
缺省 : 
不创建pim-group 
使用说明 : 
默认不创建pim-group。没有创建pim-group时pim-group相关命令将不可用； 
范例 : 
配置pim-group：ZXROSNG(config-mcast-pim)#pim-group protect-groupZXROSNG(config-mcast-pim-group-protect-group)#
相关命令 : 
bind：为pim-group绑定接口 
## pim-neighbor auto-discovery 

pim-neighbor auto-discovery 
命令功能 : 
配置pim静态邻居自动发现控制开关 打开之后会通过ad路由生成静态pim邻居。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
pim-neighbor auto-discovery 
 
no pim-neighbor auto-discovery 
命令参数解释 : 
					无
				 
缺省 : 
没有配置pim邻居自动发现 
使用说明 : 
配置pim静态邻居自动发现控制开关 打开之后会通过ad路由生成静态pim邻居 
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)#pim-neighbor auto-discoveryZXROSNG(config-mcast-vrf-zte)#
相关命令 : 
无 
## pim-silent 

pim-silent 
命令功能 : 
接口禁止发送和接收PIM协议报文。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
pim-silent 
 
no pim-silent 
命令参数解释 : 
					无
				 
缺省 : 
接口不启动pim-silent。 
使用说明 : 
为了防止恶意主机模拟发送PIM hello报文导致路由器瘫痪，可以配置pim-silent命令，禁止接收和转发任何PIM协议报文。 
范例 : 
在接口gei-0/1/0/1上启动pim-silent：ZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#pim-silent 
相关命令 : 
show ip pim interface：显示接口相关信息。 
## pimsm 

pimsm 
命令功能 : 
配置路由器在接口上开启组播PIM-SM协议功能。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
pimsm 
 
no pimsm 
命令参数解释 : 
					无
				 
缺省 : 
接口不启动组播路由协议PIM-SM。 
使用说明 : 
接口上启动组播路由协议PIM-SM时，会自动在该接口上启动IGMP。 
范例 : 
在路由器接口loopback1上配置interface命令，开启组播PIM-SM协议：ZXROSNG(config-mcast-pim)#interface loopback1ZXROSNG(config-mcast-pim-if-loopback1)#pimsm
相关命令 : 
interface：必须先进入PIM接口模式。show ip pim interface: 显示接口相关信息。
## propagation-delay 

propagation-delay 
命令功能 : 
配置PIM接口的传输时延。使用no命令取消配置。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM接口模式:15,PIM-VRF接口模式:15 
命令格式 : 
propagation-delay 
  ＜100 milliseconds 
＞
no propagation-delay 
命令参数解释 : 
参数|描述
---|---
＜100 milliseconds＞|PIM接口的传输时延，范围：1-100，单位：一百毫秒
缺省 : 
PIM接口的传输时延，缺省为5百毫秒 
使用说明 : 
接口下需先使能PIM才能配置此命令 
范例 : 
在路由器接口gei-0/1/0/1上配置propagation-delay：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router pim ZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#propagation-delay 100
相关命令 : 
pimsm：配置接口上的PIM-SM。配置PIM接口传输时延与配置接口上PIM-SM前置依赖。pimdm：配置接口上的PIM-DM。配置PIM接口传输时延与配置接口上PIM-DM前置依赖。
## provider-tunnel 

provider-tunnel 
命令功能 : 
配置组播隧道。 
命令模式 : 
 组播VRF模式  
命令默认权限级别 : 
15 
命令格式 : 
provider-tunnel 
  {mldp-p2mp 
|rsvp-te 
}
no provider-tunnel 
命令参数解释 : 
参数|描述
---|---
mldp-p2mp|设置隧道走mldp标签转发
rsvp-te|设置隧道走te标签转发
缺省 : 
隧道走mdt方式 
使用说明 : 
1.通过配置mldp-p2mp和rsvp-te参数设置隧道走不同的标签转发。 
范例 : 
组播隧道配置：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)#provider-tunnel mldp-p2mp
相关命令 : 
无 
## proxy-enable 

proxy-enable 
命令功能 : 
开启IGMP proxy功能，使用no命令删除使能。 
命令模式 : 
 IGMP-VRF模式,IGMP模式  
命令默认权限级别 : 
IGMP-VRF模式:15,IGMP模式:15 
命令格式 : 
proxy-enable 
 
no proxy-enable 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
开启IGMP proxy功能否则proxy其他相关配置将无法生效
范例 : 
开启IGMP代理功能：ZXROSNG(config-mcast-igmp)# proxy-enable
相关命令 : 
igmp-proxymroute-proxy
## proxy-service 

proxy-service 
命令功能 : 
配置主机侧代理功能，在这个接口可以发送IGMP report消息，使用no命令恢复缺省状态。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
proxy-service 
 
no proxy-service 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
配置主机侧代理功能，在这个接口可以发送IGMP report消息 
范例 : 
开启主机侧代理服务功能：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#proxy-service
相关命令 : 
igmp-proxymroute-proxy
## querier-election connect 

querier-election connect 
命令功能 : 
限制只在同一网段进行查询器选举，使用no命令取消限制。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
querier-election connect 
 
no querier-election connect 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下，所有路由器参与查询者选举。 
使用说明 : 
限制只在同一网段进行查询器选举，使用no命令取消限制 
范例 : 
配置IGMP查询者选举规避：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#querier-election connect
相关命令 : 
querier-election disable 
## querier-election disable 

querier-election disable 
命令功能 : 
查询者选举规避，即路由器认为自己就是查询路由器，使用no命令取消限制。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
querier-election disable 
 
no querier-election disable 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下，所有路由器参与查询者选举。 
使用说明 : 
查询者选举规避，配置该命令后，该路由器不参与查询者选举 
范例 : 
配置IGMP查询者选举规避：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#querier-election disable
相关命令 : 
querier-election connect 
## querier-timeout 

querier-timeout 
命令功能 : 
配置IGMP查询器超时时间，使用no命令恢复缺省值。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
querier-timeout 
  ＜seconds 
＞
no querier-timeout 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|查询器超时时间，范围：60–300，单位：秒
缺省 : 
无 
使用说明 : 
组播路由器确定不再有其他查询者而自己当选查询者的时间间隔。缺省情况下IGMP查询器超时时间为两倍IGMP查询间隔加查询响应间隔的一半，即（查询间隔×2＋查询响应间隔/2）秒。
范例 : 
配置IGMP查询器超时时间：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#querier-timeout 80 
相关命令 : 
无 
## query-interval 

query-interval 
命令功能 : 
配置IGMP发送普通查询报文的间隔，使用no命令恢复缺省值。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
query-interval 
  ＜seconds 
＞
no query-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|IGMP查询间隔，缺省为125秒，范围：1–65535，单位：秒
缺省 : 
缺省为125秒 
使用说明 : 
查询路由器周期性的发送普通查询报文，询问组成员的存在。普通查询报文的间隔是由该命令控制的。
范例 : 
配置IGMP查询间隔：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#query-interval 120
相关命令 : 
无 
## query-max-response-time 

query-max-response-time 
命令功能 : 
配置IGMP协议发送查询消息时携带的max response time时间值，使用no命令恢复缺省值。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
query-max-response-time 
  ＜seconds 
＞
no query-max-response-time 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|时间值，缺省为10秒，范围：1–25，单位：秒
缺省 : 
无 
使用说明 : 
仅对IGMP v2,v3接口有效。 
范例 : 
配置IGMP协议发送查询消息时携带的max response time时间值：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#query-max-response-time 12
相关命令 : 
无 
## reconnect-period 

reconnect-period 
命令功能 : 
配置MSDP邻居尝试连接时间间隔。使用no命令恢复缺省值。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER-VRF模式:15,MSDP-PEER模式:15 
命令格式 : 
reconnect-period 
  ＜seconds 
＞
no reconnect-period 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|MSDP邻居尝试连接时间间隔，范围：1–60，单位：秒。
缺省 : 
不设置MSDP邻居尝试连接时间间隔，默认值为30秒。 
使用说明 : 
无 
范例 : 
给IP地址为10.10.10.2的MSDP邻居配置尝试连接时间间隔为35：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)# reconnect-period 35
相关命令 : 
无 
redistribute : 

redistribute 
命令功能 : 
根据配置的ACL规则，只有满足这些规则的（S，G）组播路由条目才会出现在由MSDP邻居产生的SA消息中。使用no命令取消配置。 
命令模式 : 
 MSDP-VRF模式,MSDP模式  
命令默认权限级别 : 
MSDP模式:15,MSDP-VRF模式:15 
命令格式 : 
redistribute 
  [list 
 ＜acl-name 
＞]
no redistribute 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名，范围1-31个字符
缺省 : 
无 
使用说明 : 
1. 如果没有配置本命令，只有当MSDP发言者是要接收本地源信息的组播组的RP时，此本地源信息才会被广播出去。如果配置了本命令，有以下两种情况：a. 如果带有list < acl-name> 参数，则只有满足ACL规则的（S，G）组播路由条目才会出现在产生的SA消息中。b. 如果不带list < acl-name> 参数，将不广播任何组播源信息。2. 此命令只影响SA消息的产生，而不影响SA消息的转发。如果要对SA消息的转发进行过滤，需使用sa-filter in或sa-filter out命令。
范例 : 
配置只有满足这些规则的（S，G）组播路由条目才会出现在由MSDP邻居产生的SA消息中：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#redistribute list acl
相关命令 : 
无 
## register-holdtime 

register-holdtime 
命令功能 : 
设置路由器收不到注册停止保持注册状态的时间，使用no命令关闭。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
register-holdtime 
  ＜seconds 
＞
no register-holdtime 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|路由器收不到注册停止保持注册状态的时间，范围：1-600，单位：秒, 默认不配置，收不到注册停止则不停止注册。
缺省 : 
收不到注册停止则不停止注册。 
使用说明 : 
默认不配置此命令则收不到注册停止报文则一直发送注册报文；配置此命令用来设置路由器收不到注册停止报文时保持注册状态的时间。 
范例 : 
设置路由器收不到注册停止保持注册状态的时间为70秒： ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#route pimZXROSNG(config-mcast-pim)#register-holdtime 70
相关命令 : 
无 
## register-probe-interval 

register-probe-interval 
命令功能 : 
设置路由器向RP发送注册探索消息的时间间隔。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
register-probe-interval 
  ＜seconds 
＞
no register-probe-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|设置向RP发送注册探索消息的时间间隔，范围：1–210，单位：秒, 默认5秒。
缺省 : 
不设置发送注册探索消息的时间间隔。 
使用说明 : 
此命令用来配置组播源侧DR向RP发送注册探索（空注册）消息的时间间隔。设置的发送注册探索消息的时间间隔必须小于保持注册抑制状态的时间间隔的一半。 
范例 : 
设置路由器向RP发送注册探索消息的时间间隔为10秒：ZXROSNG(config-mcast-pim)#register-probe-interval 10
相关命令 : 
register-suppression-interval：设置路由器保持注册抑制状态的时间间隔。 
## register-source 

register-source 
命令功能 : 
通过配置此命令，修改注册报文的源地址。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
register-source 
  ＜interface-name 
＞
no register-source 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口的名称
缺省 : 
没有配置register-source。 
使用说明 : 
如果配置的接口没有地址或接口down，则注册报文的源地址采用默认值，即直连源的DR地址。在配置register-source命令时，会校验指定接口绑定的vpn与当前实例的vpn是否一致，如果不一致，则配置不成功。
范例 : 
配置register-source：ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#register-source gei-0/1/0/7 
相关命令 : 
router pim 
## register-suppression-interval 

register-suppression-interval 
命令功能 : 
设置路由器保持注册抑制状态的时间间隔。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
register-suppression-interval 
  ＜seconds 
＞
no register-suppression-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|设置路由器保持注册抑制状态的时间间隔，范围：60–3600，单位：秒, 默认60秒。
缺省 : 
不设置保持注册抑制状态的时间间隔。 
使用说明 : 
当组播源测DR收到RP发来的注册停止报文后，会立即停止发送注册报文，进入注册抑制状态。此命令就是用来配置保持注册抑制状态的超时时间。设置的保持注册抑制状态的时间间隔必须大于发送注册探索消息的时间间隔的两倍。 
范例 : 
设置路由器保持注册抑制状态的时间间隔为70秒：ZXROSNG(config-mcast-pim)#register-suppression-interval 70
相关命令 : 
register-probe-interval：路由器向RP发送注册探索消息的时间间隔。 
## reject-inbound-data 

reject-inbound-data 
命令功能 : 
通过用户命令，禁止转发面接收组播数据报文，组播路由器不能在指定接口上接收组播数据报文。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
reject-inbound-data 
  ＜interface-name 
＞
no reject-inbound-data 
  [＜interface-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
缺省 : 
接口接收组播数据报文。 
使用说明 : 
1.通过配置<interface-name>指定接口不接受组播报文。 
范例 : 
配置禁止转发面在接口上接收组播数据报文ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# reject-inbound-data gei-0/1/0/1
相关命令 : 
ip multicast-routing 
## require-alert-options 

require-alert-options 
命令功能 : 
丢弃IP头中不包含Router_Alert_Options告警选项的IGMP报文。通过no命令取消限制，恢复默认状态。 
命令模式 : 
 IGMP-VRF模式,IGMP模式  
命令默认权限级别 : 
IGMP-VRF模式:15,IGMP模式:15 
命令格式 : 
require-alert-options 
 
no require-alert-options 
命令参数解释 : 
					无
				 
缺省 : 
缺省状态下，不检查IP报文头中的Router_Alert_Options告警选项，即路由器可以处理IP头部不包含Router_Alert_Options告警选项的IGMP报文。 
使用说明 : 
在IGMPv1中，即使配置了该命令，也不会检查IP头部的Router_Alert_Options告警选项。 
范例 : 
进入IGMP组播配置模式：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#require-alert-options
相关命令 : 
无 
## robustness-count 

robustness-count 
命令功能 : 
配置允许子网丢包的次数，使用no命令恢复缺省值。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
robustness-count 
  ＜number 
＞
no robustness-count 
命令参数解释 : 
参数|描述
---|---
＜number＞|鲁棒系数缺省为2，范围：2–7
缺省 : 
缺省为2 
使用说明 : 
当鲁棒变量为n，允许丢包的次数为n-1。
范例 : 
配置允许丢包的次数为4：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#robustness-count 5
相关命令 : 
无 
## router igmp 

router igmp 
命令功能 : 
进入IGMP模式，与IGMP协议开启无关，协议开启由ip multicast-routing控制，使用no命令删除IGMP所有配置，使用默认配置。
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
router igmp 
 
no router igmp 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
没有配置ip multicast-routing，router igmp命令无效。
范例 : 
进入IGMP组播配置模式：ZXROSNG(config-mcast)#router igmp ZXROSNG(config-mcast-igmp)# 
相关命令 : 
无 
## router msdp 

router msdp 
命令功能 : 
启用IP组播协议MSDP。使用no命令关闭MSDP。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播模式:15,组播VRF模式:15 
命令格式 : 
router msdp 
 
no router msdp 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
没有配置ip multicast-routing，MSDP路由协议无法运行。 
范例 : 
启用IP组播协议MSDP：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#vrf zteZXROSNG(config-mcast-vrf-zte)#router msdp
相关命令 : 
无 
## router pim 

router pim 
命令功能 : 
启用IP组播协议PIM，使用no命令关闭PIM。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播模式:15,组播VRF模式:15 
命令格式 : 
router pim 
 
no router pim 
命令参数解释 : 
					无
				 
缺省 : 
不启动组播路由协议PIM。 
使用说明 : 
默认不启用PIM，没有启用PIM时PIM相关命令将不可用；启用PIM后进入PIM配置模式；没有配置ip multicast-routing，PIM路由协议无法运行。 
范例 : 
ZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#
相关命令 : 
interface：进入PIM接口模式。 
## rp-candidate 

rp-candidate 
命令功能 : 
配置路由器使其通告自己为候选RP，使用no命令取消该路由器作为RP的候选者。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
rp-candidate 
  ＜interface-name 
＞ [{[group-list 
 ＜prefix-list-name 
＞],[priority 
 ＜priority 
＞],[holdtime 
 ＜seconds 
＞]}]
no rp-candidate 
  ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口的名称。
＜prefix-list-name＞|它定义了一个组范围，该范围是被通告RP服务范围。
＜priority＞|优先级，范围：0–255，缺省为192。
＜seconds＞|保持时间，范围：150–65535，单位：秒。
缺省 : 
本地路由器不为候选RP，holdtime默认值150秒。 
使用说明 : 
1.如果该命令不带 <prefix-list-name >参数，表明该候选RP为所有组服务;2.候选RP的缺省优先级为192，优先级数值较小的候选RP优先；如果优先级数值相同，则比较hash值，hash值大的RP优先；如果hash值相同，则比较地址，地址大的RP优先;3.推荐用户将候选RP配置在loopback接口上，从而减少由于物理接口up/down造成的网络震荡;4.候选RP的holdtime配置的时间必须大于或等于BSM消息发送周期的2.5倍。
范例 : 
在接口loopback1上配置候选RP，优先级为180，保持时间为190秒：ZXROSNG(config-mcast-pim)#rp-candidate loopback1 priority 180 holdtime 190show命令查看配置结果信息：ZXROSNG(config-mcast-pim)#show ip pim bsrBSR address: 2.2.2.3Uptime: 00:15:26, BSR Priority :100, Hash mask length:30Expires:00:00:11This system is a candidate BSR!  candidate BSR address: 2.2.2.3(loopback1),                priority: 100,                hash mask length: 30This system is a candidate RP!  candidate RP address: 2.2.2.3(loopback1),priority:180
相关命令 : 
show ip pim bsr：查看候选RP配置信息。 
## rpf-proxy-vector mbgp 

rpf-proxy-vector mbgp 
命令功能 : 
控制MBGP路由查下一跳的(S,G) join报文是否携带向量属性 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
rpf-proxy-vector mbgp 
  ＜acl-name 
＞
no rpf-proxy-vector mbgp 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名，范围1-31个字符
缺省 : 
(S,G) join报文不携带向量属性 
使用说明 : 
1.控制MBGP路由查下一跳的(S,G) join报文是否携带向量属性 
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#rpf-proxy-vector mbgp 123ZXROSNG(config-mcast)#
相关命令 : 
无 
## rpf-proxy-vector mdt 

rpf-proxy-vector mdt 
命令功能 : 
控制MDT路由查下一跳的(S,G) join报文是否携带向量属性。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
rpf-proxy-vector mdt 
 
no rpf-proxy-vector mdt 
命令参数解释 : 
					无
				 
缺省 : 
(S,G) join报文不携带向量属性 
使用说明 : 
1.控制MDT路由查下一跳的(S,G) join报文是否携带向量属性 
范例 : 
ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#rpf-proxy-vector mdtZXROSNG(config-mcast)#
相关命令 : 
无 
## rpf-proxy-vector path-list 

rpf-proxy-vector path-list 
命令功能 : 
配置RPF迭代路径列表。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
rpf-proxy-vector path-list 
  ＜path-list-name 
＞ index 
 ＜path-index 
＞ ＜path-address 
＞ {loose 
|strict 
}
no rpf-proxy-vector path-list 
  ＜path-list-name 
＞ [index 
 ＜path-index 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜path-list-name＞|RPF路径列表名称，长度1-31字符
＜path-index＞|路径索引，范围<1-65535>
＜path-address＞|路径地址，十进制点分形式
loose|稀疏模式
strict|严格模式
缺省 : 
无 
使用说明 : 
1. 同一实例下最多配置100个路径列表名称。2. 同一路径列表名称下最多配置10条路径地址。3. 同一路径列表名称下不能配置相同的路径地址。4. RPF向量路径列表功能生效需要在PIM实例下使能hello-join-attribute命令。
范例 : 
ZXROSNG(config)# ip multicast-routingZXROSNG(config-mcast)# rpf-proxy-vector path-list a index 1 1.2.3.4 strict  
相关命令 : 
nexthophello-join-attribute
## rp-proxy 

rp-proxy 
命令功能 : 
配置rp-proxy的路由器在本地RP信息与J/P报文中的不一致时也正常的处理J/P报文。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
rp-proxy 
 
no rp-proxy 
命令参数解释 : 
					无
				 
缺省 : 
默认处理J/P报文时要检查RP信息，若与本地RP信息不一致，则丢弃J/P报文。 
使用说明 : 
配置rp-proxy的路由器在本地RP信息与J/P报文中的不一致时也正常的处理J/P报文；不配置此命令则发现本地RP信息与J/P报文中的不一致时就丢弃J/P报文。 
范例 : 
配置rp-proxy：ZXROSNG(config-mcast)#router pimZXROSNG(config-mcast-pim)#rp-proxy
相关命令 : 
无 
## rp-smart 

rp-smart 
命令功能 : 
启用RP智能切换。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
rp-smart 
 
no rp-smart 
命令参数解释 : 
					无
				 
缺省 : 
不启用RP智能切换。 
使用说明 : 
如果配置了rp-smart，则配置静态RP时要检查到这个RP地址有没有单播路由，没有就不创建这个静态RP。 
范例 : 
配置rp-smart：ZXROSNG(config-mcast-pim)#rp-smart
相关命令 : 
无 
## sa-advertisement-period 

sa-advertisement-period 
命令功能 : 
配置MSDP SA报文发送时间间隔。使用no命令恢复缺省值。 
命令模式 : 
 MSDP-VRF模式,MSDP模式  
命令默认权限级别 : 
MSDP-VRF模式:15,MSDP模式:15 
命令格式 : 
sa-advertisement-period 
  ＜seconds 
＞
no sa-advertisement-period 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|MSDP SA报文发送时间间隔，范围：1–60，单位：秒。
缺省 : 
不设置SA报文发送时间间隔，默认值为60秒。 
使用说明 : 
无 
范例 : 
配置MSDP公网实例的SA报文发送时间间隔为58：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)# sa-advertisement-period 58
相关命令 : 
无 
## sa-cache-holdtime 

sa-cache-holdtime 
命令功能 : 
配置MSDP SA cache条目保持时间。使用no命令恢复缺省值。 
命令模式 : 
 MSDP-VRF模式,MSDP模式  
命令默认权限级别 : 
MSDP模式:15,MSDP-VRF模式:15 
命令格式 : 
sa-cache-holdtime 
  ＜seconds 
＞
no sa-cache-holdtime 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|MSDP  SA cache条目保持时间，范围：150-3600，单位：秒。
缺省 : 
不设置SA cache条目保持时间，默认值为360秒。 
使用说明 : 
无 
范例 : 
配置MSDP公网实例的SA cache条目保持时间为500：ZXROSNG(config)#ip multicast-routing ZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)# sa-cache-holdtime 500
相关命令 : 
无 
## sa-filter in 

sa-filter in 
命令功能 : 
配置对来自指定MSDP邻居的SA消息进行过滤。使用no命令取消设置。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
sa-filter in 
  [list 
 ＜acl-name 
＞]
no sa-filter in 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名，范围1-31个字符
缺省 : 
无 
使用说明 : 
1. 如果没有配置此命令，所有来自于MSDP邻居的SA消息均会被接收。2. 如果本命令不带参数，所有来自指定MSDP邻居的SA消息都将被过滤；如果带有list<acl-name> 参数，则只有该ACL访问表允许的（S，G）对能够被接收。
范例 : 
对所有来自地址为10.10.10.2的MSDP邻居的SA消息进行过滤：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)#sa-filter in
相关命令 : 
无 
## sa-filter out 

sa-filter out 
命令功能 : 
配置对向指定MSDP邻居的SA消息进行过滤。使用no命令取消设置。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
sa-filter out 
  [list 
 ＜acl-name 
＞]
no sa-filter out 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名，范围1-31个字符
缺省 : 
无 
使用说明 : 
1. 如果没有配置此命令，发出的SA消息将不会被过滤；所有收到的SA消息均会向MSDP邻居转发。2. 如果本命令不带参数，所有向指定MSDP邻居发送的SA消息都将被过滤；如果带有list<acl-name> 参数，则只有该ACL访问表允许的（S，G）对能够被转发。
范例 : 
向地址为10.10.10.2的MSDP邻居转发SA消息时，所有的（S，G）被过滤：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)#sa-filter out
相关命令 : 
无 
## sa-limit 

sa-limit 
命令功能 : 
限制SA cache表中来自于指定MSDP邻居的SA消息数量。使用no命令取消限制。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
sa-limit 
  ＜limit 
＞
no sa-limit 
命令参数解释 : 
参数|描述
---|---
＜limit＞|SA cache表中允许来自某一MSDP邻居的SA消息的最大数量，范围：1–2147483646
缺省 : 
无 
使用说明 : 
使用此命令可以防止分布式拒绝服务（DDoS）攻击，因此推荐在所有的MSDP邻居连接上配置此命令。 
范例 : 
给IP地址为10.10.10.2的MSDP邻居配置SA消息限制数量为100：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)#sa-limit 100
相关命令 : 
无 
## select-mroute 

select-mroute 
命令功能 : 
配置静态路由的指定下一跳。 
命令模式 : 
 组播NEXTHOP模式  
命令默认权限级别 : 
15 
命令格式 : 
select-mroute 
  ＜source-address 
＞ ＜group-address 
＞
no select-mroute 
  ＜source-address 
＞ ＜group-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜source-address＞|源地址，为0时表示xg，否则表示sg
＜group-address＞|组播组地址
缺省 : 
不配置指定路由静态下一跳 
使用说明 : 
1.对于一个目的地址或网段可以配置多个静态下一跳。2.可以对指定的源组规定静态下一跳。3.可以根据ecmp cost的值进行hash选路。4.本命令只支持M6000系列产品。
范例 : 
设置到目的地址10.10.10.2的单播路由下一跳出接口为gei-0/1/0/5，下一跳地址为3.3.3.3，设置源：10.10.10.2，组为224.1.1.1的单播下一跳为gei-0/1/0/6，下一跳地址为4.4.4.4，这样，源为10.10.10.2组为224.1.1.1的入接口为gei-0/1/0/5，其他相关sg入接口为gei-0/1/0/6：ZXROSNG(config-mcast)# nexthop 10.10.10.2 255.255.255.255 gei-0/1/0/5 3.3.3.3  ZXROSNG(config-mcast-nexthop)# select-mroute 10.10.10.2 224.1.1.1 
相关命令 : 
static-first 
## set-dscp-outer 

set-dscp-outer 
命令功能 : 
设置组播协议数据包TOS优先级。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
set-dscp-outer 
  ＜value 
＞
no set-dscp-outer 
命令参数解释 : 
参数|描述
---|---
＜value＞|tos优先级，范围0-63。
缺省 : 
组播协议数据包tos优先级，没有配置时默认为无效值.取值范围为0-63 
使用说明 : 
1.组播协议数据包tos优先级默认为没有配置，配置范围从0到63. 
范例 : 
把组播协议数据包tos优先级设置为1：ZXROSNG(config-mcast)#set-dscp-outer 1  
相关命令 : 
无 
## shaping packets-number 

shaping packets-number 
命令功能 : 
限制所有接口报文上送数量，使用no命令取消限制。 
命令模式 : 
 IGMP-VRF模式,IGMP模式  
命令默认权限级别 : 
IGMP-VRF模式:15,IGMP模式:15 
命令格式 : 
shaping packets-number 
  ＜number 
＞
no shaping packets-number 
命令参数解释 : 
参数|描述
---|---
＜number＞|上送报文的数量，范围1-4294967295
缺省 : 
无 
使用说明 : 
此命令是限制所有接口下报文的总数。每隔5s会重置限制阀值
范例 : 
配置限制IGMP报文上送数量：ZXROSNG(config-mcast-igmp)#shaping packets-number 100
相关命令 : 
shaping-packets-number 
## shaping-packets-number 

shaping-packets-number 
命令功能 : 
限制某一接口报文上送数量，使用no命令取消限制。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
shaping-packets-number 
  ＜number 
＞
no shaping-packets-number 
命令参数解释 : 
参数|描述
---|---
＜number＞|上送报文的数量，范围1-4294967295
缺省 : 
无 
使用说明 : 
此命令限制某一接口报文上送数量每隔5s,重置接口上的限制报文上送阀值。
范例 : 
配置限制IGMP某一接口报文上送数量：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#shaping-packets-number 100
相关命令 : 
shaping packets-number 
## show debug igmp 

show debug igmp 
命令功能 : 
查看IGMP协议所有打印消息开关是否开启。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug igmp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
查看IGMP协议所有打印消息开关是否开启。 
范例 : 
查看IGMP的debug开关开启的情况：ZXROSNG#show debug igmpIGMP:  IGMP debugging is on  IGMP permit group (224.1.1.1) debugging is on  IGMP permit interface (loopback1) debugging is on
相关命令 : 
无 
## show debug mroute 

show debug mroute 
命令功能 : 
显示组播debug选项状态 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug mroute 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令会将包括私网和公网的所有打开的debug信息全部显示出来。 
范例 : 
显示组播debug选项状态：ZXROSNG#show debug mrouteMROUTE:  MROUTE debugging is on  MROUTE (VPN zte) debugging is on
相关命令 : 
无 
## show debug msdp 

show debug msdp 
命令功能 : 
显示MSDP调试信息开关状态。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug msdp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示MSDP调试信息状态：ZXROSNG#show debug msdp                                                          MSDP:  MSDP connect debugging is onZXROSNG#
相关命令 : 
无 
## show debug mvpn 

show debug mvpn 
命令功能 : 
显示开启的mvpn debug开关 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug mvpn 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
查看开启了哪些mvpn debug开关。 
范例 : 
显示开启的mvpn debug开关：ZXROSNG#show debug mvpnMVPN:  MVPN debugging is on  MVPN (VPN zte) debugging is onZXROSNG#
相关命令 : 
debug ip mvpn：设置MVPN相关信息的调试开关
## show debug pim 

show debug pim 
命令功能 : 
显示开启的pim debug开关。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug pim 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
查看开启了哪些pim debug开关。 
范例 : 
ZXROSNG#debug ip pim   PIM debugging is on ZXROSNG#show debug pimPIM:  PIM debugging is on
相关命令 : 
debug ip pim all：开启所有PIM打印开关。debug ip pim：设置PIM相关信息的调试开关。
## show error packet pim statistics 

show error packet pim statistics 
命令功能 : 
显示PIM协议模块收到的错误报文统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show error packet pim statistics 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示PIM各协议报文在所有实例下分别累计的错误报文计数。 
范例 : 
1.显示PIM协议模块收到的错误报文统计信息：ZXROSNG(config)#sho error packet pim statistics PIM error packets:Hello:2Register:413Register-Stop:0Join/Prune:0Bootstrap:0Assert:0Graft:0Graft-Ack:0C-RP-Ad:0State-Refresh:0DF-Election:0ECMP-Redirect:0PFM-GSH-TLV:0显示信息说明：Hello：错误Hello报文的累计个数；Register：错误Register报文的累计个数；Register-Stop：错误Register-Stop报文的累计个数；Join/Prune：错误Join/Prune报文的累计个数；Bootstrap：错误BSM报文的累计个数；Assert：错误Assert报文的累计个数；Graft：错误Graft报文的累计个数；Graft-Ack：错误Graft-Ack报文的累计个数；C-RP-Ad：错误C-RP通告报文的累计个数；State-Refresh：错误State-Refresh报文的累计个数；DF-Election：错误DF-Election报文的累计个数；ECMP-Redirect：错误ECMP重定向报文的累计个数；PFM-GSH-TLV：错误PFM-GSH报文的累计个数；
相关命令 : 
error packet pim record{disable|enable[<number>]} 
## show error packet pim 

show error packet pim 
命令功能 : 
显示PIM协议模块最近收到的错误报文。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show error packet pim 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1-32个字符
缺省 : 
无 
使用说明 : 
1.不指定参数。显示所有实例的PIM协议模块最近收到的错误报文。2.指定vrf-name，显示实例名为vrf-name的PIM协议模块最近收到的错误报文。
范例 : 
1.不指定参数显示所有的PIM协议模块最近收到的错误报文：ZXROSNG(config)#show error packet pim Packet Index : 1Record Time  : 2016-3-16 23:30:32Interface    : gei-0/20/0/1Instance     : vrf zte1Length       : 28Error Reason : Register multicast address error0000: 21  00  be  ff  00  00  00  00  65  00  00  64  7c  28  00  00 0010: 1f  11  33  5d  0a  01  01  01  e0  01  01  01---------------------------------------------------------------------Packet Index : 2Record Time  : 2016-3-16 23:30:31Interface    : gei-0/20/0/1Instance     : vrf zte1Length       : 6Error Reason : Register packet length error0000: 21  00  de  ff  00  00 ---------------------------------------------------------------------Packet Index : 3Record Time  : 2016-3-16 22:57:35Interface    : gei-0/20/0/2Instance     : globalLength       : 2Length       : 70Error Reason : Hello checksum error0000: 20  00  00  00  00  01  00  02  00  46  00  02  00  04  01  f4 0010: 09  c4  00  13  00  04  00  00  00  0a  00  14  00  04  63  de 0020: f0  02  00  15  00  04  01  3c  00  00  00  16  00  00  00  1a 0030: 00  00  ff  dd  00  06  01  00  64  01  01  0a  00  18  00  06 0040: 01  00  01  02  03  04  ---------------------------------------------------------------------2.指定vrf-name显示PIM协议模块最近收到的错误报文：ZXROSNG(config)#show error packet pim vrf zte1Packet Index : 1Record Time  : 2016-3-16 23:30:32Interface    : gei-0/20/0/1Instance     : vrf zte1Length       : 28Error Reason : Register multicast address error0000: 21  00  be  ff  00  00  00  00  65  00  00  64  7c  28  00  00 0010: 1f  11  33  5d  0a  01  01  01  e0  01  01  01---------------------------------------------------------------------Packet Index : 2Record Time  : 2016-3-16 23:30:31Interface    : gei-0/20/0/1Instance     : vrf zte1Length       : 6Error Reason : Register packet length error0000: 21  00  de  ff  00  00 ---------------------------------------------------------------------显示信息说明：Packet Index：报文序号；Record Time：记录时间；Interface：收到错误报文的接口名称；Instance：收到错误报文的实例名称；Length：从PIM头开始计算的错误报文长度；Error Reason：错误原因；0000：该字段后面的内容是从PIM头开始记录的错误报文内容。
相关命令 : 
error packet pim record{disable|enable[<number>]} 
## show ip igmp groups summary 

show ip igmp groups summary 
命令功能 : 
查看接口上IGMP组数目总和。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip igmp groups summary 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
缺省 : 
无 
使用说明 : 
查看接口上IGMP组数目总和。区分实例：show ip igmp groups summary vrf ＜vrf-name＞
范例 : 
显示接口上IGMP组数目总和： ZXROSNG#show ip igmp groups summaryIGMP groups summary: Interface           Static    Joined    Total  gei-0/11/0/8        0         1000      1000gei-0/14/0/1        0         1000      1000Summary             0         2000      2000
相关命令 : 
无 
## show ip igmp groups 

show ip igmp groups 
命令功能 : 
查看接口上IGMP组加入情况。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip igmp groups 
  [vrf 
 ＜vrf-name 
＞] [{[＜interface-name 
＞],[＜group-address 
＞]}] [detail 
] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜interface-name＞|接口的名称
＜group-address＞|组地址，十进制点分形式
detail|显示IGMP的源列表等细节信息
缺省 : 
无 
使用说明 : 
查看某个实例下所有接口的组加入情况：show ip igmp groups vrf <vrf-name>;查看公网某个接口的组加入情况：show ip igmp groups <interface-name>;查看公网某个特定组的加入情况：show ip igmp groups <group-address>;需要查看的源加入信息：show ip igmp groups detail;
范例 : 
ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#show ip igmp groupsTotal  : 2 groups                                                  Group addr      Interface           Present     Expire      Last Reporter224.0.0.1       gei-0/7/1/2         02:07:35    never       0.0.0.0225.1.1.100     gei-0/7/1/2         00:08:45    never       0.0.0.0 
相关命令 : 
无 
## show ip igmp interface 

show ip igmp interface 
命令功能 : 
查看接口上IGMP配置情况。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip igmp interface 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜interface-name＞|接口名称
缺省 : 
无 
使用说明 : 
分为主机侧和网络侧的接口显示。当配置了proxy-service后，此命令显示主机侧接口状态，否则显示路由器侧的接口状态。
范例 : 
查看接口上IGMP配置情况：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#show ip igmp interface gei-0/7/1/2                          gei-0/7/1/2    Internet address is 0.0.0.0, subnet mask is 0    IGMP is enabled on interface  Current IGMP version is 2         IGMP query interval is 120 seconds   IGMP last member query interval is 10 seconds   IGMP query max response time is 12 seconds    IGMP querier timeout period is 246 seconds   IGMP robustness variable is 2    IGMP querier is 0.0.0.0, never expire  Inbound IGMP access group is not set  IGMP immediate leave control is not set   IGMP shaping packets number is not set  IGMP maximum joins is not set  IGMP access IP source is not set
相关命令 : 
无 
## show ip igmp packet-count 

show ip igmp packet-count 
命令功能 : 
查看IGMP协议报文接收和发送的统计计数。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip igmp packet-count 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜interface-name＞|接口名称
缺省 : 
无 
使用说明 : 
查看IGMP协议报文接收和发送的统计计数。针对特定实例的所有接口：show ip igmp packet-count vrf <vrf-name>针对特定接口：show ip igmp packet-count <interface-name>
范例 : 
查看IGMP协议报文接收和发送的统计计数：ZXROSNG(config)#sho ip igmp packet-count gei-0/1/0/1IGMP Packet Counts:Received/SentInterface:gei-0/1/0/1  Query:5/2  Leave:0/0  ReportV1:0/0  ReportV2:0/0  ReportV3:0/0  Spec-Query:0/0  Grp-Src-Query:0/0  Dropped:0/0  Invalid:7/0  Total:12/2Current Time:  2017-03-01 17:58:59显示信息说明：Current time：显示当前时间。
相关命令 : 
无 
## show ip igmp proxy groups 

show ip igmp proxy groups 
命令功能 : 
查看接口上IGMP proxy 组加入情况。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip igmp proxy groups 
  [vrf 
 ＜vrf-name 
＞] [{[＜interface-name 
＞],[＜group-address 
＞]}] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜interface-name＞|接口名称
＜group-address＞|组地址，十进制点分形式
缺省 : 
无 
使用说明 : 
查看接口上IGMP proxy 组加入情况区分实例：show ip igmp proxy groups vrf <vrf-name>;区分接口：接口一般是配置使能proxy-service的接口show ip igmp proxy groups <interface-name>;区分组：show ip igmp proxy groups <group-address>;
范例 : 
查看接口上IGMP proxy组加入情况：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#show ip igmp proxy groups Total: 1 groupsGroup addr      Interface           Present239.255.255.250 fei-0/1/0/2         01:58:32  
相关命令 : 
igmp-proxymroute-proxyproxy-serviceproxy-enable
## show ip mdt cache 

show ip mdt cache 
命令功能 : 
显示组播IP MDT TLV cache信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip mdt cache 
 vrf 
 ＜vrf-name 
＞ {send 
|receive 
 [mdt-source 
 ＜mdt-source 
＞]} [{[vpn-source 
 ＜vpn-source 
＞],[vpn-group 
 ＜vpn-group 
＞],[{mdt-group 
 ＜mdt-group 
＞|mpls-mldp 
 ＜num-tree 
＞}]}] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF实例名，长度1–32字符
send|本地发送的MDT TLV信息
receive|收到远端的MDT TLV信息
＜mdt-source＞|MDT data源地址，十进制点分形式
＜vpn-source＞|私网源地址，十进制点分形式
＜vpn-group＞|私网组地址，十进制点分形式
＜mdt-group＞|MDT data组地址，十进制点分形式
＜num-tree＞|MDT data隧道索引，范围1-4294967295
缺省 : 
无 
使用说明 : 
该命令用于显示指定VRF下本地或远端的MDT TLV缓存相关信息。 
范例 : 
显示组播IP MDT TLV信息：ZXROSNG(config)#show ip mdt cache vrf zte1 send(102.102.102.11, 225.0.0.5)  MDT sender: local  MDT data: mLDP global ID 1  Expire time: 00:00:41(102.102.102.15, 225.0.0.5)  MDT sender: local  MDT data: mLDP global ID 2  Expire time: 00:00:41(102.102.102.17, 225.0.0.3)  MDT sender: local  MDT data: mLDP global ID 3  Expire time: 00:00:41显示信息说明MDT sender：MDT TLV发送者；MDT data：MDT data树信息；Expire time：MDT TLV老化时间；
相关命令 : 
mdt datamdt defaultmtunnel
## show ip mdt 

show ip mdt 
命令功能 : 
显示组播MDT信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip mdt 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令直接显示出所有vrf下的mdt的相关信息 
范例 : 
显示组播MDT信息：ZXROSNG(config)# show ip mdt VRF name: zteDefault mode: GRE, Data mode: GRERoot ID: 0.0.0.0, VPN ID: 0:0Data Tree Num: 0, Next S-PMSI Index: 1MTunnel is: gei-0/1/0/1 192.168.14.80(PIM-mdt disable)Default group is: 224.2.2.2Data group is: 224.2.22.2/32 aclname zteVRF name: aaaDefault mode: GRE, Data mode: GRERoot ID: 0.0.0.0, VPN ID: 0:0Data Tree Num: 0, Next S-PMSI Index: 1MTunnel is: NULLDefault group is: 224.3.3.3Data group is: 224.3.4.4/32显示信息说明Default mode：Default公网转发模式；Data mode：Data公网转发模式；Data Tree Num：Data公网标签隧道范围；Next S-PMSI Index：待切换S-PMSI索引； 
相关命令 : 
vrf 
## show ip mroute brief 

show ip mroute brief 
命令功能 : 
显示IP组播路由表的简明信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip mroute brief 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1-32个字符
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的组播路由情况，可采用<vrf-name>来指定，不指定则显示公网的； 
范例 : 
ZXROSNG(config)#show ip mroute briefIP Multicast Routing Table Brief(*, 226.0.0.1), TYPE: DYNAMIC(100.10.10.112, 226.0.0.1), TYPE: DYNAMIC
相关命令 : 
无 
## show ip mroute nexthop 

show ip mroute nexthop 
命令功能 : 
显示组播传输方向下一跳信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip mroute nexthop 
  [vrf 
 ＜vrf-name 
＞] [＜ip-address 
＞] [detail 
] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|vrf名称
＜ip-address＞|目的地址
detail|保护特定路由的详细信息
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的下一跳情况，可采用<vrf-name>来指定，不指定则显示公网的；2.查看到到某一特定目的地址的下一跳情况，可采用<ip-address>来指定
范例 : 
显示组播下一跳的信息：ZXROSNG(config)#show ip mroute nexthopIP Multicast Nexthop TableNexthop flags and user: L:Local, C:Connect, CTOP:Across the backbone,UNR:Unreachable unicast, MSN:Multicast static nexthop, M:Master, S:SlaveDest address:1.2.3.4 05:55:14 PIM(RTM)MSTATIC nexthop:  Metric:1, Preference:1, Masklen:32, Flags:  RPF path list: abcMBGP nexthop:Metric:4294967295, Preference:0, Masklen:0, Flags:UNRECMP list: MIGP nexthop:Metric:4294967295, Preference:0, Masklen:0, Flags:UNRECMP list:RTM nexthop:Metric:20, Preference:110, Masklen:32, Flags:ECMP list:Nexthop:101.1.1.1Oif:gei-0/1/0/1(M)Nhp:101.1.1.1RelNhp:101.1.1.1Nexthop:102.1.1.1Oif:gei-0/1/0/2(S)Nhp:102.1.1.1RelNhp:102.1.1.1Dest address:10.3.3.5 00:04:18 PIM(MSN)  MSTATIC nexthop:  Metric:1, Preference:1, Masklen:24, Flags:  Fallback: vrf zte  MBGP nexthop:  Metric:4294967295, Preference:0, Masklen:0, Flags:UNR  ECMP list:  MIGP nexthop:  Metric:4294967295, Preference:0, Masklen:0, Flags:UNR  ECMP list:  RTM nexthop:  Metric:4294967295, Preference:0, Masklen:0, Flags:UNR  ECMP list:ZXROSNG(config-mcast)#show ip mroute nexthop vrf zteIP Multicast Nexthop TableNexthop flags and user: L:Local, C:Connect, CTOP:Across the backbone,UNR:Unreachable unicast, MSN:Multicast static nexthop, M:Master, S:SlaveDest address:1.1.1.1 00:05:39 PIM(MSN)  MSTATIC nexthop:  Metric:1, Preference:1, Masklen:24, Flags:  Fallback: IP global  MBGP nexthop:  Metric:4294967295, Preference:0, Masklen:0, Flags:UNR  ECMP list:  MIGP nexthop:  Metric:4294967295, Preference:0, Masklen:0, Flags:UNR  ECMP list:  RTM nexthop:  Metric:4294967295, Preference:0, Masklen:0, Flags:UNR  ECMP list:显示信息说明：L：表示本地。C：表示连接。CTOP：表示跨主干网。UNR：单播不可达。MSN：组播静态配置的下一跳。M：主路由。S：备路由。Dest address：目的地址。Metric：下一跳的路由度量值。Preference：下一跳的路由优先级。Masklen：掩码。Flags：标记位。ECMP list：ECMP列表。Fallback：IP global表示下一跳是公网实例，vrf zte表示下一跳是私网zte实例。RPF path list：RPF路径列表。
相关命令 : 
无 
## show ip mroute summary all-instance 

show ip mroute summary all-instance 
命令功能 : 
显示IP组播所有实例的路由表总数的具体数目。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip mroute summary all-instance 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示IP组播所有实例的路由表总数的具体数目：ZXROSNG(config-igmp)#show ip mroute summary all-instanceIP multicast routing table summary(*,G): 3 routes(S,G): 4 routesTotal: 7 routes显示信息说明：(*,G)：表示配置的组播(*,G)条目数；(S,G)：表示配置的组播(S,G)条目数；Total：表示配置的组播(*,G) 和(S,G)条目数总和。
相关命令 : 
show ip mroute summary 
## show ip mroute summary 

show ip mroute summary 
命令功能 : 
显示IP组播路由表的具体数目。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip mroute summary 
  [vrf 
 ＜vrf-name 
＞] [iif 
 ＜in-interface-name 
＞] [oif 
 ＜out-interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|vrf名称
＜in-interface-name＞|入接口名
＜out-interface-name＞|出接口名
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的路由数目，可采用<vrf-name>来指定，不指定则显示公网的；可指定入接口或出接口查询路由数目。 
范例 : 
显示IP组播路由表的具体数目：ZXROSNG(config-igmp)#show ip mroute summary IP multicast routing table summary   (*,G): 1 routes   (S,G): 1 routes   Total: 2 routes
相关命令 : 
无 
## show ip mroute 

show ip mroute 
命令功能 : 
显示IP组播路由表的内容。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip mroute 
  [vrf 
 ＜vrf-name 
＞] [{[group 
 ＜group-address 
＞ [source 
 ＜source-address 
＞]]|[source 
 ＜source-address 
＞]}] [iif 
 ＜in-interface-name 
＞] [oif 
 ＜out-interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|vrf名称
＜group-address＞|组地址，十进制点分形式
＜source-address＞|静态组播源地址，为十进制点分形式
＜source-address＞|静态组播源地址，为十进制点分形式
＜in-interface-name＞|入接口名
＜out-interface-name＞|出接口名
缺省 : 
无 
使用说明 : 
1．由于现在SG老化不再由协议发起，SG老化时间不再显示。2. 如果没有可选项，则显示所有的组播路由表。3. 如果增加组选项，则显示该组（*，g）和所有相关的（s，g）路由条目。4. 如果增加组和源地址选项，则显示特定的（s，g）路由条目。5. 如果增加入接口和出接口选项，则显示特定出接口或入接口的路由条目。
范例 : 
范例1显示IP组播路由表的内容：ZXROSNG(config)#show ip mrouteIP Multicast Routing TableFlags:NS:SPT upsend, RT:Reg upsend, MT:Tunnel, F:Forward, S:Syn mrt,NTP:NTP join, FLT:Flt add, FD:Flt del, DPU:Damping enable, DPD:Damping del,SU:Slave in use, Vir:Virtual,(*, 224.1.1.1)  TYPE: DYNAMIC, FLAGS:  RP: 11.1.1.1  Incoming interface: NULL, flags:  Outgoing interface list: 1    gei-0/1/0/1.2, flags: F/S(*, 224.1.1.2)  TYPE: DYNAMIC, FLAGS:  RP: 11.1.1.1  Incoming interface: NULL, flags:  Outgoing interface list: 1    gei-0/1/0/1.2, flags: F/S(*,224.1.1.3)  TYPE: STATIC, FLAGS: SU  RP: 0.0.0.0  Incoming interface: gei-0/1/0/1, flags:  Secondary RPF interface: gei-0/1/0/2  Outgoing interface list: 2    gei-0/1/0/3, flags: F/S    gei-0/1/0/1, flags: F/S(1.1.1.1, 225.1.1.1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: loopback1, flags: NS  Outgoing interface list: 0  Fallback extranet receivers: 1    vrf zte(10.3.3.5, 225.1.1.1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: using vrf zte, flags: NS  Outgoing interface list: 1    gei-0/20/0/2, flags: F/SZXROSNG(config-mcast)#show ip mroute vrf zteIP Multicast Routing TableFlags:NS:SPT upsend, RT:Reg upsend, MT:Tunnel, F:Forward, S:Syn mrt,NTP:NTP join, FLT:Flt add, FD:Flt del, DPU:Damping enable, DPD:Damping del,SU:Slave in use, Vir:Virtual,(1.1.1.1, 225.1.1.1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: using global, flags: NS  Outgoing interface list: 1    gei-0/20/0/3, flags: F/S(10.3.3.5, 225.1.1.1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: gei-0/20/0/3, flags: NS  Outgoing interface list: 0  Fallback extranet receivers: 1    IP globalZXROSNG#show ip mroute IP Multicast Routing TableFlags:NS:SPT upsend, RT:Reg upsend, MT:Tunnel, F:Forward, S:Syn mrt,NTP:NTP join, FLT:Flt add, FD:Flt del, DPU:Damping enable, DPD:Damping del,SU:Slave in use, Vir:Virtual,(10.20.30.40, 225.1.1.1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: gei-0/20/0/2, flags: NS  Outgoing interface list: 2    mldp_oif, flags: Vir    loopback1, flags: F/SZXROSNG#显示信息说明：TYPE：条目类型，DYNAMIC表示动态，STATIC表示静态；FLAGS：表示路由上标记位；RP：表示路由条目对应的RP地址；Incoming interface：表示条目入接口，后面flags表示入接口标记位；Secondary RPF interface：表示条目备入接口；Outgoing interface list：表示条目出接口列表，后面flags表示出接口标记位。using global：表示组播路由上游实例名称。当上游是公网实例，显示using global。using vrf zte：表示组播路由上游实例名称。当上游是私网实例zte，显示using vrf zte。Fallback extranet receivers：表示Fallback扩展的接收者信息，后面接IP global表示是公网实例，接vrf zte表示是私网zte。范例2配置BIER的时候，显示的公网IP组播路由表的内容：ZXROSNG(config)#show ip mrouteIP Multicast Routing TableFlags:NS:SPT upsend, RT:Reg upsend, MT:Tunnel, F:Forward, S:Syn mrt,NTP:NTP join, FLT:Flt add, FD:Flt del, DPU:Damping enable, DPD:Damping del,SU:Slave in use, Vir:Virtual,(*, 225.0.0.1)  TYPE: STATIC, FLAGS:   RP: 0.0.0.0  Incoming interface: gei-0/1/0/8, flags:   Outgoing interface list: 2    gei-0/1/0/1, flags: FLT/S    loopback4, flags: FLT/S  BFER sub-domain-id: 1   BFER num: 4    BFR-prefix: 1.1.1.1         BFR-id: -    BFR-prefix: 1.1.1.2         BFR-id: -    BFR-prefix: 5.6.7.8         BFR-id: 3001BFR-prefix: 101.1.1.2       BFR-id: -(108.1.1.10, 225.0.0.1)  TYPE: STATIC, FLAGS:   Incoming interface: gei-0/1/0/8, flags:   Outgoing interface list: 2    gei-0/1/0/1, flags: FLT/S    loopback4, flags: FLT/S  BFER sub-domain-id: 1   BFER num: 4    BFR-prefix: 1.1.1.1         BFR-id: -    BFR-prefix: 1.1.1.2         BFR-id: -    BFR-prefix: 5.6.7.8         BFR-id: 3001BFR-prefix: 101.1.1.2       BFR-id: -显示信息说明：TYPE：条目类型，DYNAMIC表示动态，STATIC表示静态；FLAGS：表示路由上标记位；RP：表示路由条目对应的RP地址；Incoming interface：表示条目入接口，后面flags表示入接口标记位；Secondary RPF interface：表示条目备入接口；Outgoing interface list：表示条目出接口列表，后面flags表示出接口标记位。BIER sub-domain-id：表示BIER子域ID，BFER num:表示BFER数量。BFR-prefix：表示BFR前缀地址，BFR-id:表示BFR标识。BFR-id: -表示没有BFR ID。
相关命令 : 
无 
## show ip msdp count 

show ip msdp count 
命令功能 : 
显示SA消息产生的源/组播组数量和SA cache中来自每个MSDP邻居的SA消息数量。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip msdp count 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符。
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示SA消息产生的源/组播组数量：ZXROSNG(config-mcast-msdp-peer)#show ip msdp count SA State per Peer Counters, <Peer>: <#SA learned>    10.10.10.2: 0    Total entries: 0
相关命令 : 
无 
## show ip msdp peer 

show ip msdp peer 
命令功能 : 
显示MSDP邻居的详细信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip msdp peer 
  [vrf 
 ＜vrf-name 
＞] [＜peer-address 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符。
＜peer-address＞|MSDP邻居地址
缺省 : 
无 
使用说明 : 
若不指定邻居地址，显示对应实例下MSDP所有邻居的详细信息。 
范例 : 
显示MSDP邻居的详细信息：ZXROSNG(config-mcast-msdp-peer)#show ip msdp peerMSDP Peer 100.10.10.20  Description:   Connection status:    State: Up, Resets: 2    Connection source: gei-0/20/0/1 (100.10.10.10)    Uptime(Downtime): 22:57:10, Messages sent/received: 1392/1378    Connection and counters cleared 23:30:17 ago  SA Filtering:    Input (S,G) filter: none    Output (S,G) filter: none  Peer ttl threshold: 1  Peer ttl security hops: 0  SAs learned from this peer: 0  SAs local: 1显示信息说明：MSDP Peer：MSDP邻居地址；Description：表示该邻居的说明性描述；Connection status：表示该邻居的连接状态；SA Filtering：表示SA消息的过滤信息；Peer ttl threshold：表示SA报文发送给邻居的TTL限值；Peer ttl security hops：表示SA报文发送给邻居的TTL安全跳数值；SAs learned from this peer：表示从该邻居学到的SA消息数目；SAs local：表示本地SA消息数目。
相关命令 : 
无 
## show ip msdp sa-cache 

show ip msdp sa-cache 
命令功能 : 
显示来自各MSDP邻居的（S，G）状态。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip msdp sa-cache 
  [vrf 
 ＜vrf-name 
＞] [＜group-address 
＞ [＜source-address 
＞]] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符
＜group-address＞|指定的组播组地址
＜source-address＞|指定的组播源地址
缺省 : 
无 
使用说明 : 
如果同时指定了两个地址，将显示对应这些地址的（S，G）项；如果只指定了组播组地址，将显示这个组播组的所有源；如果未指定任何选项，将显示整个SA cache表。 
范例 : 
显示来自各MSDP邻居的（S，G）状态：ZXROSNG#show ip msdp sa-cacheMSDP Source-Active Cache - 4 entriesTimers:Uptime/Expires(101.101.101.101, 224.1.1.1), RP 49.4.4.4, 00:21:45/ 00:05:57(101.101.101.101, 224.1.1.2), RP 49.4.4.4, 00:21:45/ 00:05:57(101.101.101.101, 226.1.1.1), RP 50.4.4.4, 00:09:04/ 00:04:57(101.101.101.101, 226.1.1.2), RP 50.4.4.4, 00:09:04/ 00:04:57
相关命令 : 
无 
## show ip msdp summary 

show ip msdp summary 
命令功能 : 
显示MSDP邻居状态。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip msdp summary 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32个字符
缺省 : 
无 
使用说明 : 
命令显示列表中Reset Count为TCP连接重启次数。SA Count为SA cache中来自此MSDP邻居的SA消息数量。 
范例 : 
显示MSDP邻居状态：ZXROSNG(config-mcast-msdp-peer)#show ip msdp summary MSDP Peer Status SummaryPeer Address           State     Uptime/     Reset    SA                                 Downtime    Count    Count10.10.10.2             Down      04:10:51    0        0
相关命令 : 
无 
## show ip multicast-static-interface 

show ip multicast-static-interface 
命令功能 : 
显示静态组播出接口列表 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip multicast-static-interface 
  [vrf 
 ＜vrf-name 
＞] [index 
 ＜index 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度1–32字符
＜index＞|显示指定索引号的出接口列表，范围1-100
缺省 : 
缺省显示所有出接口列表 
使用说明 : 
1.查看指定VRF实例的出接口情况，可以通过vrf-name来指定。2.查看指定索引号的出接口情况，可以通过index来指定。3.没有指定索引号则显示所有出接口。
范例 : 
1．    显示公网所有静态组播出接口列表：ZXROSNG#show ip multicast-static-interfaceStatic multicast out port index 10:  Outgoing Interface:    gei-0/1/0/1Static multicast out port index 11:  Outgoing Interface:    gei-0/1/0/1    gei-0/1/0/22．    显示公网指定出接口索引号为10的出接口列表：ZXROSNG#show ip multicast-static-interface index 10Static multicast out port index 10:  Outgoing Interface:    gei-0/1/0/13．    显示私网所有静态组播出接口列表：ZXROSNG#show ip multicast-static-interface vrf zteStatic multicast out port index 1:  Outgoing Interface:    gei-0/1/0/7    loopback1Static multicast out port index 2:  Outgoing Interface:    loopback2    loopback14．    显示私网指定出接口索引号为1的出接口列表：ZXROSNG#show ip multicast-static-interface vrf zte index 1Static multicast out port index 1:  Outgoing Interface:    gei-0/1/0/7    loopback15．    配置BIER时显示公网出接口列表：ZXROSNG#show ip multicast-static-interface Static multicast out port index 1:  Outgoing Interface: NULL  BFER Info:    BFER index: 1   sub-domain-id: 1  Static multicast out port index 2:  Outgoing Interface:     loopback1    loopback4  BFER Info:     BFER index: 1   sub-domain-id: 1    
相关命令 : 
无 
## show ip multicast-static-route 

show ip multicast-static-route 
命令功能 : 
显示静态组播路由表和路由表统计信息 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip multicast-static-route 
  [vrf 
 ＜vrf-name 
＞] [{[group 
 ＜group-address 
＞ [source 
 ＜source-address 
＞]]|[source 
 ＜source-address 
＞]|[summary 
]}] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜group-address＞|组地址
＜source-address＞|源地址
＜source-address＞|源地址
summary|显示路由表统计信息
缺省 : 
缺省显示所有静态组播路由表 
使用说明 : 
可以通过此命令查看指定VRF实例、指定源静态组播路由、指定组静态组播路由和指定源组静态组播路由，及静态组播路由表统计信息 
范例 : 
1. 显示公网静态组播路由表：ZXROSNG#show ip multicast-static-routeThe Capability of Static Multicast Route(*, g) 10, (s, g) 10IP Multicast Static Routing TableFlags: A- Available, F- Forward, N- Not available, W- Wait to restore(*, 235.1.1.1)  Incoming interface: gei-0/1/0/1  A/W  Track name: a  Secondary RPF interface: gei-0/1/0/2  A  Track name: b  Outgoing interface list:    loopback3  F    loopback4  F(1.2.3.4, 235.1.1.1)  Incoming interface: gei-0/1/0/1  A/W  Track name: a  Secondary RPF interface: gei-0/1/0/2  A  Track name: b  Outgoing interface list:    loopback3  F    loopback4  F显示信息说明：(*, g)：表示(*, g)最大可配条目数；(s, g)：表示(s, g)最大可配条目数；Incoming interface：表示条目主入接口；Secondary RPF interface：表示条目备入接口；Track name：表示条目主备入接口关联检测的track名；Outgoing interface list：表示条目出接口列表。2. 显示公网静态组播路由表统计信息：ZXROSNG#show ip multicast-static-route summaryIP Static Multicast Routing Table Summary(*,G): 1 routes(S,G): 1 routesTotal: 2 routes显示信息说明：(*,G)：表示配置的(*,G)条目数；(S,G)：表示配置的(S,G)条目数；Total：表示配置的(*,G) 和(S,G)条目数总和。3. 显示私网静态组播路由表：ZXROSNG#show ip multicast-static-route vrf zteThe Capability of Static Multicast Route(*, g) 10, (s, g) 10IP Multicast Static Routing TableFlags: A- Available, F- Forward, N- Not available, W- Wait to restore(*, 235.1.1.1)  Incoming interface: gei-0/1/0/7  A/W  Track name: a  Secondary RPF interface: gei-0/1/0/8  Track name: b  Outgoing interface list:    loopback1  F    loopback2  F(1.2.3.4, 235.1.1.1)  Incoming interface: gei-0/1/0/7  A  Secondary RPF interface: NULL  Outgoing interface list:    loopback1  F    loopback2  F4. 显示私网静态组播路由表统计信息：ZXROSNG#show ip multicast-static-route vrf zte summaryIP Static Multicast Routing Table Summary(*,G): 1 routes(S,G): 1 routesTotal: 2 routes5. 配置BIER时，显示公网静态组播路由表信息：ZXROSNG#show ip multicast-static-route The Capability of Static Multicast Route(*, g) 100, (s, g) 100IP Multicast Static Routing TableFlags: A- Available, F- Forward, N- Not available, W- Wait to restore(*, 225.0.0.1)  Incoming interface: gei-0/1/0/8  A  Secondary RPF interface: NULL  Outgoing interface list:  BFER Info:     BFER index: 1   sub-domain-id: 1  (1.1.1.1, 225.0.0.1)  Incoming interface: gei-0/1/0/8  A  Secondary RPF interface: NULL  Outgoing interface list:  BFER Info:     BFER index: 1   sub-domain-id: 1  (1.1.1.1, 225.0.0.2)  Incoming interface: loopback1  A  Secondary RPF interface: NULL  Outgoing interface list:    loopback1  F    loopback4  F  BFER Info:     BFER index: 1   sub-domain-id: 1 
相关命令 : 
无 
## show ip mvpn ad-route summary 

show ip mvpn ad-route summary 
命令功能 : 
显示MVPN AD路由统计信息 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip mvpn ad-route summary 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称,1-32个字符
缺省 : 
无 
使用说明 : 
1.可以指定vrf实例查看AD路由统计信息，使用<vrf-name>来指定实例，如果不指定，则显示公网的AD路由统计信息。 
范例 : 
ZXROSNG#show ip mvpn ad-route summary vrf zteType            Local     Received  Total     Intra-AS        1         0         1         Inter-AS        0         1         1         Spmsi-AD        0         0         0         Leaf-AD         0         0         0         Source Active   0         0         0         XG Join         0         10        10        SG Join         0         0         0         Total           1         11        12显示信息说明Type:AD路由类型Local:本地的路由个数Received:接收到的路由个数Intra-AS,Inter-AS,Spmsi-AD, Leaf-AD, Source Active, XG Join, SG Join:1~7型AD路由
相关命令 : 
无 
## show ip mvpn ad-route 

show ip mvpn ad-route 
命令功能 : 
显示MVPN AD路由信息 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip mvpn ad-route 
  [vrf 
 ＜vrf-name 
＞] [{[group 
 ＜group-address 
＞],[source 
 ＜source-address 
＞],[origin 
 ＜origin-address 
＞],[{intra-as 
|inter-as 
|spmsi-ad 
|leaf-ad 
|source-active 
|xg-join 
|sg-join 
}]}] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，1-32个字符
＜group-address＞|组地址，十进制点分形式
＜source-address＞|源地址，十进制点分形式
＜origin-address＞|origin地址，十进制点分形式
intra-as|指定显示Intra-as ad 路由
inter-as|指定显示Inter-as ad 路由
spmsi-ad|指定显示Spmsi-ad 路由
leaf-ad|指定显示Leaf-ad 路由
source-active|指定显示Source active 路由
xg-join|指定显示(*,G)加入路由
sg-join|指定显示(S,G)加入路由
缺省 : 
无 
使用说明 : 
该命令显示相关隧道标签信息，可以在显示命令后面参数选项中指定需要的过滤信息，直接显示出来指定的路由信息。如果没有<vrf-name>选项，则显示所有公网的MVPN AD路由信息。 
范例 : 
显示公网的AD路由信息：ZXROSNG#show ip mvpn ad-routeFlags: L- Local,R- Remote,J- Join Ptnl,S- Start Ptnl,T0- No PtnlT1- RSVP-TE,T2- mLDP-P2MP,T3- PIM-SSM,T4- PIM-SM,T5- PIM-BidirT6- Ingress-Replication,T7- mLDP-MP2MP,T11- BIERNLRI                                 (P-tunl|Next Hop)/Flags[Type][Key]                         ((flags/type/label/id)|Next Hop)/Flags[1][1:1][1.1.1.1]                   (0/2/0/2:1000:1.1.1.1)/(J/T2/R)(0/6/0/1)/(S/T6/R)[2][1:1][2]                         (0/2/0/2:1002:2.2.2.2)/(S/T2/R)(1/6/206225/3.3.3.3)/(J/T6/R)[4][2][1:1][2][2.2.2.2]             (0/6/206225/60001)/(T6/L)显示私网的AD路由信息：ZXROSNG(config-mcast)#show ip mvpn ad-route vrf zteFlags: L- Local,R- Remote,J- Join Ptnl,S- Start Ptnl,T0- No PtnlT1- RSVP-TE,T2- mLDP-P2MP,T3- PIM-SSM,T4- PIM-SM,T5- PIM-BidirT6- Ingress-Replication,T7- mLDP-MP2MP,T11- BIERNLRI                                (P-tunl|Next Hop)/Flags[Type][Key]                         ((flags/type/label/id)|Next Hop)/Flags[1][1:1][1.1.1.1]                   (0/2/0/2:1002:1.1.1.1)/(S/T2/L)[2][1:1][2]                         (0/2/0/2:1004:2.2.2.2)/(J/T2/R)[6][1:1][108.108.108.10,225.0.0.1]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.2]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.3]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.4]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.5]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.6]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.7]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.8]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.9]  (2.2.2.2)(R)[6][1:1][108.108.108.10,225.0.0.10] (2.2.2.2)(R)ZXROSNG(config)#show ip mvpn ad-route vrf zte1Flags: L- Local,R- Remote,J- Join Ptnl,S- Start Ptnl,T0- No Ptnl       T1- RSVP-TE,T2- mLDP-P2MP,T3- PIM-SSM,T4- PIM-SM,T5- PIM-Bidir       T6- Ingress-Replication,T7- mLDP-MP2MP,T11- BIERNLRI                                (P-tunl|Next Hop)/Flags[Type][Key]                         ((flags/type/label/id)|Next Hop)/Flags[1][10:10][1.1.1.10]                (1/11/16/0:123:6.6.6.10)/(S/T11/L)[1][10:10][1.1.1.20]                (1/11/16/255:456:6.6.6.20)/(J/T11/R)[4][1][10:10][1.1.1.10][1.1.1.20]   (0/11/0/0:456:6.6.6.20)/(T11/R)[4][1][10:10][1.1.1.20][1.1.1.10]   (0/11/0/255:123:6.6.6.10)/(T11/L)[7][10:10][102.102.102.11,225.0.0.1]                                    (1.1.1.20)/(R)显示信息说明[Type]：AD路由类型[Key]：对于不同类型的AD路由key值不同，1#路由key为[RD][origin IP]，2#路由key为[RD][AS]，3#路由key为[RD] [multicast source][multicast group] [origin IP]，4#路由key为[route key][origin IP]，5#路由key为[RD] [multicast source][multicast group],6#和7#的key都为[RD] [AS] [multicast source][multicast group]flags/type/label/id：flags表示是否需要生成4#路由，type表示隧道类型，label表示隧道标签，id表示隧道ID，只有1-4#路由才显示Next Hop：下一跳，只有5-7#路由才显示Flags：隧道和路由的标记L:本地路由R:远端路由J:标记是否加入远端隧道S:标记为隧道头节点T0--T11：隧道的8种类型
相关命令 : 
provider-tunnel 
## show ip mvpn instance 

show ip mvpn instance 
命令功能 : 
显示组播vpn的实例信息 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip mvpn instance 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，1-32个字符
缺省 : 
无 
使用说明 : 
显示具体哪个VRF实例的MVPN实例信息，可采用<vrf-name>来指定，如果没有<vrf-name>选项，则显示公网的MVPN实例信息。 
范例 : 
显示组播私网VPN实例信息：ZXROSNG(config-mcast-vrf-zte)#show ip mvpn instance vrf zteMVPN name zteRD: 1:10Import mcast RT: 1.2.3.4:10Provider tunnel: PIM-MDTOrigin IP: 1.2.3.4Protocol State:Route State:  EnableMLDP State:  EnableP-PIM State:  EnableC-PIM State:  EnableUpstream Protocol:  PIMPIM-MDT Info:MDT tunnel: loopback1MDT source: 1.2.3.4MDT tunnel state:   up / PIM enableDefault group : 239.1.1.1Data group is: 225.0.0.0/32显示MVPN公网实例信息：ZXROSNG(config)#show ip mvpn instance MVPN name IP global     RD: None     Import mcast RT: None      Provider tunnel: mLDP-P2MP      Origin IP: 2.2.2.2  Routable,Local    TE ID: <not set>  Protocol State:         Route State: Enable      mLDP State: Enable      P-PIM State: Enable      C-PIM State: Enable      Upstream Protocol: BGP    PIM-MDT Info:         MDT tunnel: loopback1      MDT source: 2.2.2.2      MDT tunnel state:   up / PIM disable    Default group:     Data group is:显示信息说明MVPN name: VRF实例名称RD: VRF实例对应的RD值Import mcast RT: 导入组播路由目标Provider tunnel: 支持隧道模式Origin IP: PE设备源IP地址Protocol State: 协议状态Route State: BGP是否使能MLDP State: MLDP是否使能P-PIM State: 公网PIM状态C-PIM State: 私网PIM状态Upstream Protocol: 上游协议PIM-MDT Info: MDT配置信息MDT tunnel: MDT隧道MDT source: MDT源地址MDT tunnel state: MDT隧道状态Default group: MDT Default组地址Data group is: MDT Data组地址
相关命令 : 
无 
## show ip mvpn mrib 

show ip mvpn mrib 
命令功能 : 
显示组播VPN的route infomation base 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip mvpn mrib 
 vrf 
 ＜vrf-name 
＞ [{[group 
 ＜group-address 
＞],[source 
 ＜source-address 
＞]}] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|vrf名称
＜group-address＞|组地址
＜source-address＞|源地址
缺省 : 
无 
使用说明 : 
1.显示时需指定<vrf-name>组播VPN的路由信息，可以使用<source-address>和<group-address>作为过滤条件来显示指定的路由信息 
范例 : 
ZXROSNG#show ip mvpn mrib vrf zteLegend for mvpn routes propertiesLO -- Local VPN route  RM -- remote VPN routeIFT -- Receive from P-tunnel  OFT -- Send to P-tunnelOFNL -- Downstream join state(10.1.1.11,224.1.1.1)  Flags: /OFT/OFNLUpstream Status:Upstream PE: LocalUpstream tunnel:-RPF Tunnel:-Downstream Status:Downstream tunnel: RSVP-TE,201,201,1.2.3.1Switch tunnel: RSVP-TE,202,202,1.2.3.1Switch timer : 00:00:04Correlative discovery route tableType:3, RD:1:10, Properties: LONlri:(10.1.1.11,224.1.1.1):1.2.3.1Ptnl:RSVP-TE,202,202,1.2.3.1Type:4, RD:1:10, Properties: RMNlri:(10.1.1.11,224.1.1.1):1.2.3.1:2.3.4.2Type:5, RD:1:10, Properties: LONlri:(10.1.1.11,224.1.1.1), Probe: 00:00:07Type:7, RD:1:10, Properties: RMNlri:(10.1.1.11,224.1.1.1)(10.1.1.12,224.1.1.1)  Flags: /OFT/OFNLUpstream Status:Upstream PE: LocalUpstream tunnel:-RPF Tunnel:-Downstream Status:Downstream tunnel: RSVP-TE,201,201,1.2.3.1Switch tunnel: RSVP-TE,203,203,1.2.3.1Switch timer : 00:00:04Correlative discovery route tableType:3, RD:1:10, Properties: LONlri:(10.1.1.12,224.1.1.1):1.2.3.1Ptnl:RSVP-TE,203,203,1.2.3.1Type:4, RD:1:10, Properties: RMNlri:(10.1.1.12,224.1.1.1):1.2.3.1:2.3.4.2Type:5, RD:1:10, Properties: LONlri:(10.1.1.12,224.1.1.1), Probe: 00:00:08Type:7, RD:1:10, Properties: RMNlri:(10.1.1.12,224.1.1.1)R2(config-mcast-vrf-zte)#show ip mvpn mrib vrf zteLegend for MVPN routes properties   LO -- Local VPN route  RM -- remote VPN route   IFT -- Receive from P-tunnel  OFT -- Send to P-tunnel   OFNL -- Downstream join state(10.1.1.11,225.1.1.1)  Flags: IFT/OFNL  Upstream Status:    Upstream PE: 3.4.5.6    Upstream tunnel: mLDP-P2MP,1001,3.4.5.6    RPF Tunnel: 60005  Slave upstream Status:    Slave upstream PE: 1.2.3.4    Slave upstream tunnel: mLDP-P2MP,1001,1.2.3.4    Slave RPF tunnel: 60007    Egress WTR timer: 00:00:00  Downstream Status:    Downstream tunnel:    Switch tunnel:    Switch timer:  Correlative discovery route table  Type:3, RD:1:10, Uptime:00:00:24, Properties: RM          Nlri:(10.1.1.11,225.1.1.1):1.2.3.4          [Leaf]:mLDP-P2MP,1001,1.2.3.4  Type:3, RD:1:10, Uptime:00:00:15, Properties: RM          Nlri:(10.1.1.11,225.1.1.1):3.4.5.6          [Leaf]:mLDP-P2MP,1001,3.4.5.6  Type:5, RD:1:10, Uptime:01:16:12, Properties: RM          Nlri:(10.1.1.11,225.1.1.1)  Type:7, RD:1:10, Uptime:01:16:13, Properties: LO          Nlri:(10.1.1.11,225.1.1.1)R1(config-mcast-vrf-zte)#show ip mvpn mrib vrf zteLegend for MVPN routes properties   LO -- Local VPN route  RM -- remote VPN route   IFT -- Receive from P-tunnel  OFT -- Send to P-tunnel   OFNL -- Downstream join state(10.1.1.11,225.1.1.1)  Flags: OFT/OFNL  Upstream Status:    Upstream PE: Local    Upstream tunnel:    RPF Tunnel:  Protect Status:    Master node: 3.4.5.6    Slave node: 1.2.3.4    Detect type: stream    Detect tunnel: mLDP-P2MP,1001,3.4.5.6    Detect RPF tunnel: 60002    Ingress WTR timer: 00:00:00  Downstream Status:    Downstream tunnel: mLDP-P2MP,1001,1.2.3.4    Switch tunnel:    Switch timer:  Correlative discovery route table  Type:3, RD:1:10, Uptime:01:18:10, Properties: LO          Nlri:(10.1.1.11,225.1.1.1):1.2.3.4          [Root]:mLDP-P2MP,1001,1.2.3.4  Type:3, RD:1:10, Uptime:00:02:12, Properties: RM          Nlri:(10.1.1.11,225.1.1.1):3.4.5.6          [Leaf]:mLDP-P2MP,1001,3.4.5.6  Type:5, RD:1:10, Uptime:01:18:10, Properties: LO          Nlri:(10.1.1.11,225.1.1.1)  Type:7, RD:1:10, Uptime:01:18:11, Properties: RM          Nlri:(10.1.1.11,225.1.1.1)显示信息说明Upstream Status：上游状态Upstream PE：上游PEUpstream tunnel：上游隧道RPF Tunnel：RPF隧道 Slave upstream Status: 上游备状态 Slave upstream PE: 备上游PE Slave upstream tunnel: 备上游隧道 Slave RPF tunnel: 备RPF 隧道Egress WTR timer: 出PE wtr时间FRR Status:  FRR状态FRR master:  FRR主节点FRR slave: FRR 备节点FRR detect: FRR检测类型Detect tunnel: 检测隧道Detect RPF tunnel: 检测RPF 隧道Ingress WTR timer: 入PE WTR时间Downstream Status：下游状态Downstream tunnel：下游隧道Switch tunnel：待切换隧道Switch timer：隧道切换延时定时器Type：AD路由类型Nlri：网络层可达信息
相关命令 : 
无 
## show ip mvpn mtib 

show ip mvpn mtib 
命令功能 : 
显示组播VPN的tunnel infomation base的信息 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip mvpn mtib 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称,1-32个字符
缺省 : 
无 
使用说明 : 
1.可以指定vrf实例查看隧道信息，使用<vrf-name>来指定实例，如果不指定就会显示公网实例的隧道信息。 
范例 : 
显示公网隧道信息：ZXROSNG(config)#show ip mvpn mtibName: mLDP-P2MP Root Tunnel 1004  Properties:    Leaf required: 0, Label: 0, Type: 2     Opaque ID: 1004, Root ID: 2.2.2.2  Status:    Oper: Create, PriVRF: IP global  All VPN Info:    VRF name: IP global      VPN label: 0, C-Flow Num: 0, Send Num: 0, Switch Num: 0Name: mLDP-P2MP Leaf Tunnel 60000  Properties:    Leaf required: 0, Label: 0, Type: 2     Opaque ID: 1002, Root ID: 1.1.1.1  Status:    Oper: Create, Protocol: Join, PriVRF: IP global, LvDly: 00:00:00  All VPN Info:    VRF name: IP global,Join      VPN label: 0, C-Flow Num: 0, Send Num: 0, Switch Num: 0Name: Ingress-Replication Root Tunnel 1001  Properties:    Leaf required: 0, Label: 0, Type: 6     Tunnel ID: 1001  Status:    Oper: Create, PriVRF: IP global  All VPN Info:    VRF name: IP global      VPN label: 0, C-Flow Num: 0, Send Num: 0, Switch Num: 0Name: Ingress-Replication Leaf Tunnel 60003  Properties:    Leaf required: 1, Label: 206225, Type: 6     End Point: 3.3.3.3  Status:    Oper: Create, Protocol: Join, PriVRF: IP global, LvDly: 00:00:00  All VPN Info:    VRF name: IP global,Join      VPN label: 0, C-Flow Num: 0, Send Num: 0, Switch Num: 0显示私网隧道信息：ZXROSNG#show ip mvpn mtib vrf zteName: TE-P2MP Leaf Tunnel 62001Properties:Leaf required: 1, Label: 0, Type: 1P2MP ID: 201, Tunnel ID: 201, Extend ID:2.3.4.2Status:Oper: Create, Protocol: Join, PriVRF: zte, LvDly: 00:00:00All VPN Info:VRF name: zteVPN label: 0, C-Flow Num: 1, Send Num: 0, Switch Num: 0Name: TE-P2MP Root Tunnel 201Properties:Leaf required: 1, Label: 0, Type: 1P2MP ID: 201, Tunnel ID: 201, Extend ID:1.2.3.1Status:Oper: Create, Protocol: Up, PriVRF: zteAll VPN Info:VRF name: zteVPN label: 0, C-Flow Num: 1, Send Num: 0, Switch Num: 0Name: TE-P2MP Root Tunnel 202Properties:Leaf required: 1, Label: 0, Type: 1P2MP ID: 202, Tunnel ID: 202, Extend ID:1.2.3.1Status:Oper: Create, Protocol: Up, PriVRF: zteAll VPN Info:VRF name: zteVPN label: 0, C-Flow Num: 1, Send Num: 1, Switch Num: 0Name: TE-P2MP Root Tunnel 203Properties:Leaf required: 1, Label: 0, Type: 1P2MP ID: 203, Tunnel ID: 203, Extend ID:1.2.3.1Status:Oper: Create, Protocol: Up, PriVRF: zteAll VPN Info:VRF name: zteVPN label: 0, C-Flow Num: 1, Send Num: 1, Switch Num: 0显示信息说明Name:隧道名称Properties:隧道属性Leaf required:标记是否需要创建叶子路由Label:标签（固定填0）Type:隧道类型P2MP ID，Tunnel ID，Extend ID 隧道FEC三元组Status:隧道状态Oper:操作状态Protocol:协议状态PriVRF:主VPNLvDly:延时离开定时器All VPN Info:所有VPN实例信息VRF name:VPN名称VPN label:内存标签C-Flow Num:关联SG计数Send Num:注册SG计数Switch Num:切换隧道次数
相关命令 : 
无 
## show ip mvpn mtunnel 

show ip mvpn mtunnel 
命令功能 : 
显示MVPN的PMSI隧道信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip mvpn mtunnel 
  [{rsvp-te 
|mldp-p2mp 
|pim-ssm 
|pim-sm 
|ingress-replication 
|bier 
} [＜tunnel-id 
＞]] 
命令参数解释 : 
参数|描述
---|---
rsvp-te|隧道类型为TE-P2MP
mldp-p2mp|隧道类型为mLDP-P2MP
pim-ssm|隧道类型为PIM-SSM
pim-sm|隧道类型为PIM-SM
ingress-replication|隧道类型为 Ingress-Replication
bier|隧道类型为BIER
＜tunnel-id＞|隧道ID，范围：1-4294967295
缺省 : 
无 
使用说明 : 
1.可以指定隧道类型以及隧道ID查看隧道信息。 
范例 : 
显示全局MVPN隧道信息：ZXROSNG(config)#show ip mvpn mtunnelName: mLDP-P2MP Root Tunnel 1003Main VRF: zte1All MRT information:    VRF name: zte1        (*,225.0.0.1)        (*,225.0.0.2)        (*,225.0.0.3)        (*,225.0.0.4)        (*,225.0.0.5)        (*,225.0.0.6)        (*,225.0.0.7)        (*,225.0.0.8)        (*,225.0.0.9)        (*,225.0.0.10)Name: mLDP-P2MP Root Tunnel 1004Main VRF: zte2All MRT information:    VRF name: zte2        (*,226.0.0.1)        (*,226.0.0.2)        (*,226.0.0.3)        (*,226.0.0.4)        (*,226.0.0.5)        (*,226.0.0.6)        (*,226.0.0.7)        (*,226.0.0.8)        (*,226.0.0.9)        (*,226.0.0.10)Name: mLDP-P2MP Leaf Tunnel 60003Main VRF: zte1All MRT information:Name: mLDP-P2MP Leaf Tunnel 60004Main VRF: zte2All MRT information:显示信息说明Name:隧道名称Type:隧道类型Main VRF:主VPN名称All MRT information:所有关联此隧道的组播路由信息VRF name:VPN名称
相关命令 : 
无 
## show ip pim bfd 

show ip pim bfd 
命令功能 : 
显示PIM BFD信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim bfd 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的PIM BFD信息，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个接口的PIM BFD信息，可采用<interface-name>来指定，不指定则显示所有接口的BFD信息。
范例 : 
ZXROSNG(config)#show ip pim bfd                    Interface: gei-0/1/0/1   State: CONNECT  BFD Local-Addr: 101.1.1.2(BDR)  BFD Peer-Addr：101.1.1.1(DR)显示信息说明：Interface：接口地址；BFD Local_Addr：本端配置BFD的接口地址；BFD Peer_Addr：对端配置BFD的接口地址；State：BFD链接状态。
相关命令 : 
bfd-enable：在接口上启用BFD。 
## show ip pim bsr 

show ip pim bsr 
命令功能 : 
显示自举路由器（BSR）的信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim bsr 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
缺省 : 
无 
使用说明 : 
查看具体哪个VRF实例下的BSR信息及本地配置的候选RP的信息，可采用<vrf-name>来指定，不指定则显示公网的。 
范例 : 
ZXROSNG(config)#show ip pim bsrBSR address: 2.2.2.3Uptime: 03:20:27, BSR Priority :0, Hash mask length:30Expires:00:00:33This system is a candidate BSR!  candidate BSR address: 2.2.2.3(loopback1),                priority: 0,                hash mask length: 30This system is a candidate RP!  candidate RP address: 2.2.2.3(loopback1),priority:192  candidate RP address: 3.1.1.2(loopback2),priority:192显示信息说明：BSR address：BSR的IP地址；Uptime    ：BSR的存活时间；BSR Priority：BSR优先级；Hash mask length：BSR 掩码长度；Expires：BSR的过期时间或者是发送BSR消息的过期时间；candidate RP address：本地配置的候选RP的IP地址；priority：本地配置的候选RP优先级。
相关命令 : 
bsr-candidate：配置候选BSR。 
## show ip pim group 

show ip pim group 
命令功能 : 
显示配置的pim-group信息 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim group 
  [vrf 
 ＜vrf-name 
＞] [＜group-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜group-name＞|pim组名字，长度1-31个字符
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的pim-group情况，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个组的pim-group情况，可采用<group-name>来指定，不指定则显示所有组的pim-group情况。
范例 : 
配置show ip pim group：ZXROSNG(config-mcast-pim)#show ip pim group PIM Group TableGroup name: a                                 Group id: 1           Total bind interfaces:2                   Interface                Bind_State Fwd_Stategei-0/1/0/1                       Active      TRUE       gei-0/1/0/2                       Passive     TRUE  显示信息说明：Group name: pim-group名称；Group ID: pim-group ID；Total bind interfaces:为pim-group绑定关联接口的数目；Interface：绑定的接口名称；Bind-State：接口的绑定状态；Fwd-State：流量转发状态，TRUE表示需要转发，FALSE表示不需要转发。     
相关命令 : 
pim-group 
## show ip pim interface brief 

show ip pim interface brief 
命令功能 : 
查看PIM接口概要信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip pim interface brief 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的PIM接口概要信息，可采用<vrf-name>来指定，不指定则显示公网的。 
范例 : 
ZXROSNG(config)#show ip pim interface briefTotal: 2Interface                        State Nbr   Hello  DR                                       Count Period PriorityDR-Addressgei-0/1/0/1                      Up    1     30     1100.10.10.20loopback1                        Up    0     30     11.1.1.1(local)ZXROSNG(config)#显示信息说明：Total：接口数目统计；Interface：接口名称；State：接口状态up/down；Nbr Count：邻居个数；Hello Period：HELLO报文的发送时间间隔；DR Priority：该接口的DR优先级；DR-Address：该接口的DR地址。
相关命令 : 
show ip pim interface 
## show ip pim interface 

show ip pim interface 
命令功能 : 
查看配置的PIM-SM和PIM-DM接口情况。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip pim interface 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的PIM接口情况，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个PIM接口情况，可采用<interface-name>来指定，不指定则显示所有PIM接口。
范例 : 
ZXROSNG(config)#show ip pim interface Total: 4Interface                        State Nbr   Hello  DR         PIM      Mode                                       Count Period Priority   Silent  gei-0/20/0/1                     Up    0     30     1          Disabled   S    Address: 100.10.10.10    DR     : 100.10.10.10gei-0/20/0/2                     Up    1     30     1          Disabled   S    Address: 100.10.20.10    DR     : 100.10.20.10gei-0/20/0/6                     Up    1     30     1          Disabled   S    Address: 100.30.30.10    DR     : 100.30.30.10loopback1                        Up    0     30     1          Disabled   S    Address: 1.2.3.4    DR     : 1.2.3.4ZXROSNG(config)#显示信息说明：Total：接口数目统计；Address：接口配置的接口地址；Interface：接口名称；State：接口状态up/down；Nbr Count：邻居个数；Hello Period：HELLO报文的发送时间间隔；DR Priority：该接口的DR优先级；DR：该接口的DR；PIMSilent：是否启用PIM silent；Mode：接口使能的是哪些PIM模式(SM和DM)。
相关命令 : 
hello-interval：配置接口PIM hello报文发送间隔。dr-priority：配置PIM接口DR优先级。pim-silent：接口禁止发送和接收PIM协议报文。
## show ip pim mroute summary all-instance 

show ip pim mroute summary all-instance 
命令功能 : 
显示IP组播所有实例的PIM路由表总数的具体数目。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip pim mroute summary all-instance 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示IP组播所有实例的PIM路由表总数的具体数目：ZXROSNG(config)#show ip pim mroute summary all-instancePIM Multicast Routing Table Summary(*, G):4 , (S, G):3, (S, G, rpt):0, Register:3显示信息说明：(*,G)：表示配置的组播PIM (*,G)条目数；(S,G)：表示配置的组播PIM (S,G)条目数；(S, G, rpt)：表示配置的组播PIM (S, G, rpt)条目数；Register：表示配置的组播PIM注册条目数。
相关命令 : 
show ip pim mroute summary 
## show ip pim mroute summary 

show ip pim mroute summary 
命令功能 : 
显示IP组播PIM路由表的内容统计信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim mroute summary 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
缺省 : 
无 
使用说明 : 
查看特定VRF实例下的PIM路由表的路由条目统计信息，可采用<vrf-name>来指定，不指定则显示公网的路由条目统计信息。 
范例 : 
ZXROSNG(config)#show ip pim mroute summary PIM Multicast Routing Table Summary(*, G):1 , (S, G):0, (S, G, rpt):0, Register:0(*, 224.1.1.1) (JOINED), RP: 2.2.2.3
相关命令 : 
无 
## show ip pim mroute 

show ip pim mroute 
命令功能 : 
显示组播PIM路由表的内容。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim mroute 
  [vrf 
 ＜vrf-name 
＞] [group 
 ＜group-address 
＞ [source 
 ＜source-address 
＞]] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜group-address＞|组播组地址，十进制点分形式
＜source-address＞|源地址，十进制点分形式
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的组播路由表，可采用<vrf-name>来指定，不指定则显示所有公网的组播路由表；2.查看具体哪个组的路由条目，可采用<group-address>来指定，不指定则显示所有组的路由条目；3.查看具体哪个源的路由条目，可采用<source-address>来指定，不指定则显示所有源的路由条目。
范例 : 
1.组播路由条目显示：ZXROSNG#show ip pim mroute                                                       PIM Multicast Routing TableFlags: T- SPT-bit set,A- Forward,J- Join SPT,U- Upsend,S- PIM-SM,D- PIM-DM, Macro state: Ind- Pim Include Macro,Exd- Pim Exclude Macro,       Jns- Pim Joins Macro,LAst- Pim Lost_assert Macro,       Imo- Pim Immediate_olist Macro,Ino- Pim Inherited_olist Macro,       Lcd- Pim Local_receiver_include Macro,       Fbk- Fallback extranet receiver number Timers:UpTime/Expire(Upstream State)/KAT (*, 225.1.1.1)  00:07:30/00:00:31(JOINED)/00:00:00  RP address: 100.10.10.10  Ind:0/Jns:1/LAst:0/Imo:1/Lcd:0/Fbk:0  Iif: NULL, RPF nbr: 0.0.0.0  Oif: 1    gei-0/20/0/1,     Joins  /  ImoXG  /  UpTime: 00:07:30, Expire: 00:03:01(100.10.80.100, 225.1.1.1)  00:00:38/00:00:00(JOINED)/00:02:52  RP:100.10.10.10;   Reg:NO INFO; RT:NULL;   MSDP: TO BE ADV ;   Ind:0/Exd:0/Jns:1/LAst:0/Imo:1/Ino:1/Fbk:0  Iif: gei-0/20/0/8, RPF nbr:0.0.0.0(S); AT       RPF nbr:0.0.0.0(D); 00:00:00(FORWARD); (100.10.80.100, 225.1.1.1, rpt)  00:00:37/00:00:00(PRUNED),   Pru:1/LAst:0/Ino:0  Iif:NULL; RPF nbr:0.0.0.0;   Oif: 2     gei-0/20/0/1,   PrunesSGRpt  /  InheritedFromXG      gei-0/20/0/2,   JoinsSG  /  InoSG  /  UpTime: 00:00:38, Expire: 00:02:52         (*, 226.1.1.1)  00:07:30/00:00:31(JOINED)/00:00:00  RP address: 100.10.10.10  Ind:0/Jns:1/LAst:0/Imo:1/Lcd:0/Fbk:0  Iif: NULL, RPF nbr: 0.0.0.0  Oif: 1     gei-0/20/0/1,     Joins  /  ImoXG  /  UpTime: 00:07:30, Expire: 00:03:01ZXROSNG#   ZXROSNG#show ip pim mroute group 226.1.1.1PIM Multicast Routing TableFlags: T- SPT-bit set,A- Forward,J- Join SPT,U- Upsend,S- PIM-SM,D- PIM-DM, Macro state: Ind- Pim Include Macro,Exd- Pim Exclude Macro,       Jns- Pim Joins Macro,LAst- Pim Lost_assert Macro,       Imo- Pim Immediate_olist Macro,Ino- Pim Inherited_olist Macro,       Lcd- Pim Local_receiver_include Macro,       Fbk- Fallback extranet receiver number Timers:UpTime/Expire(Upstream State)/KAT (*, 226.1.1.1)  00:07:39/00:00:22(JOINED)/00:00:00  RP address: 100.10.10.10  Ind:0/Jns:1/LAst:0/Imo:1/Lcd:0/Fbk:0  Iif: NULL, RPF nbr: 0.0.0.0  Oif: 1    gei-0/20/0/1,     Joins  /  ImoXG  /  UpTime: 00:07:39, Expire: 00:02:52ZXROSNG#2.支持fallback功能的组播路由条目显示：ZXROSNG(config)#show ip pim mroute PIM Multicast Routing TableFlags: T- SPT-bit set,A- Forward,J- Join SPT,U- Upsend,S- PIM-SM,D- PIM-DM, Macro state: Ind- Pim Include Macro,Exd- Pim Exclude Macro,       Jns- Pim Joins Macro,LAst- Pim Lost_assert Macro,       Imo- Pim Immediate_olist Macro,Ino- Pim Inherited_olist Macro,       Lcd- Pim Local_receiver_include Macro,       Fbk- Fallback extranet receiver number Timers:UpTime/Expire(Upstream State)/KAT (*, 225.1.1.1)  00:01:07/00:00:54(JOINED)/00:00:00  RP address: 1.2.3.4  Ind:2/Jns:0/LAst:0/Imo:2/Lcd:2/Fbk:1  Iif: NULL, RPF nbr: 0.0.0.0  Oif: 1    loopback1,     LocalIn  /  ImoXG  /  UpTime: 00:01:07, Expire: 00:00:00(10.1.2.3, 225.1.1.1)  00:01:07/00:00:00(JOINED)/00:00:00  RP:1.2.3.4;   Reg:NO INFO; RT:NULL;   Ind:2/Exd:0/Jns:0/LAst:0/Imo:2/Ino:2/Fbk:1  Iif: gei-0/20/0/1, RPF nbr:0.0.0.0(S); AU       RPF nbr:0.0.0.0(D); 00:00:00(FORWARD);   Oif: 1     loopback1,   LocalInSG  /  InheritedFromXG  /  InoSGRpt  /  InoSG  /  UpTime: 00:01:07, Expire: 00:00:00         (100.10.80.100, 225.1.1.1)  00:01:06/00:00:00(NOT JOINED)/00:00:00  RP:1.2.3.4;   Reg:NO INFO; RT:NULL;   Ind:0/Exd:1/Jns:0/LAst:0/Imo:0/Ino:1/Fbk:0  Iif: gei-0/20/0/8, RPF nbr:0.0.0.0(S); AU       RPF nbr:0.0.0.0(D); 00:00:00(FORWARD); (100.10.80.100, 225.1.1.1, rpt)  00:01:06/00:00:00(NOT PRUNED),   Pru:0/LAst:0/Ino:1  Iif:NULL; RPF nbr:0.0.0.0;   Oif: 1     loopback1,   InheritedFromXG  /  InoSGRpt  /  InoSG  ZXROSNG(config)#ZXROSNG(config)#show ip pim mroute vrf zte_mcast1PIM Multicast Routing TableFlags: T- SPT-bit set,A- Forward,J- Join SPT,U- Upsend,S- PIM-SM,D- PIM-DM, Macro state: Ind- Pim Include Macro,Exd- Pim Exclude Macro,       Jns- Pim Joins Macro,LAst- Pim Lost_assert Macro,       Imo- Pim Immediate_olist Macro,Ino- Pim Inherited_olist Macro,       Lcd- Pim Local_receiver_include Macro,       Fbk- Fallback extranet receiver number Timers:UpTime/Expire(Upstream State)/KAT (*, 225.1.1.1)  00:01:27/00:00:00(JOINED)/00:00:00  RP address: 1.2.3.4  Ind:1/Jns:0/LAst:0/Imo:1/Lcd:1/Fbk:0  Iif: using global, RPF nbr:0.0.0.0; J  Oif: 1    loopback2,     LocalIn  /  ImoXG  /  UpTime: 00:01:27, Expire: 00:00:00(10.1.2.3, 225.1.1.1)  00:01:27/00:00:00(JOINED)/00:00:00  RP:1.2.3.4;   Reg:NO INFO; RT:NULL;   Ind:1/Exd:0/Jns:0/LAst:0/Imo:1/Ino:1/Fbk:0  Iif: using global, RPF nbr:0.0.0.0(S); AU       RPF nbr:0.0.0.0(D); 00:00:00(FORWARD);   Oif: 1    loopback2,   LocalInSG  /  InheritedFromXG  /  InoSGRpt  /  InoSG  /  UpTime: 00:01:27, Expire: 00:00:00(100.10.80.100, 225.1.1.1)  00:01:27/00:00:00(JOINED)/00:00:00  RP:1.2.3.4;   Reg:NO INFO; RT:NULL;   Ind:1/Exd:0/Jns:0/LAst:0/Imo:1/Ino:1/Fbk:0  Iif: NULL; RPF nbr: 0.0.0.0(S/D); (100.10.80.100, 225.1.1.1, rpt)  00:01:27/00:00:00(PRUNED),   Pru:0/LAst:0/Ino:1  Iif: using global; RPF nbr:0.0.0.0; A  Oif: 1    loopback2,   LocalInSG  /  InheritedFromXG  /  InoSGRpt  /  InoSG  /  UpTime: 00:01:27, Expire: 00:00:00ZXROSNG(config)#显示信息说明：T：表示此路由条目接收到来自SPT树的组播包A：表示此路由条目的入接口有效U：表示向该条目上送组播包J：表示接收到数据流向SPT树切换Ind: 表示有本地IGMP加入接收数据流的接口数Exd: 表示有本地IGMP加入不接收数据流的接口数LAst: 表示接收数据流但是asser失败的接口数Imo: 表示直接根据路由类型建立的出接口数Ino: 表示继承其他路由类型的出接口数Fbk：表示fallback扩展的接收者个数UpTime/Expire: 表示此路由条目的运行时间和过期时间RP address: 表示PIM-SM产生的（*，G）条目对应的RPIif: 表示条目入接口RPF nbr: 表示条目相应的RPF邻居Oif：表示出接口列表，后面数字表示出接口个数，UpTime表示该接口作为路由出接口的时间，Expire表示PIM协议状态到期时间的倒计时MoFRR Iif: 表示条目的备入接口Vector: 向量属性using global：表示组播路由上游实例名称。当上游是公网实例，显示using global。using vrf zte：表示组播路由上游实例名称。当上游是私网实例zte，显示using vrf zte。
相关命令 : 
无 
## show ip pim neighbor 

show ip pim neighbor 
命令功能 : 
查看配置的PIM接口的邻居情况 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim neighbor 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的PIM接口邻居情况，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个PIM接口的邻居情况，可采用<interface-name>来指定，不指定则显示所有PIM接口的邻居情况。
范例 : 
ZXROSNG(config)# show ip pim neighborNeighbor Address:101.1.1.1  Interface:gei-0/1/0/1  Uptime:05:57:59  Expire:00:01:23  DR Pri:100  Attr:N/A 显示信息说明：Neighbor Address：邻居IP地址；Interface：接口名称；DR Priority：邻居的DR优先级；Uptime    ：邻居的存活时间；Expires：邻居的过期时间；Attr：hello报文中的JOIN选项，N/A表示报文中没有此选项，P表示使用了此选项。
相关命令 : 
dr-priority：配置PIM接口DR优先级。pimsm：接口使能PIM-SM。pimdm：接口使能PIM-DM。
## show ip pim nexthop 

show ip pim nexthop 
命令功能 : 
查看PIM下一跳的信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim nexthop 
  [vrf 
 ＜vrf-name 
＞] [dest-address 
 ＜ip-address 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜ip-address＞|目的IP地址
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的PIM下一跳信息，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体到哪个目的地址的PIM下一跳信息，可采用dest-address来指定，不指定则显示所有PIM下一跳信息。
范例 : 
ZXROSNG(config)#show ip pim nexthopPIM Nexthop TableNexthop state: R- Nexthop to RP,S- Nexthop to Source,O- Related with Unicast,U- No Unicast Route,L- Local Route,C- Connect to Dest,Dest:2.2.2.3                                 (00:02:10)Type:.R. .O. .L.Metric:0Preference:0ECMP list:Nexthop:2.2.2.3(is Local)Port:loopback1Dest:3.1.1.2                                 (00:02:10)Type:.R. .O. .L.Metric:0Preference:0ECMP list:Nexthop:3.1.1.2(is Local)Port:loopback2Dest:10.3.3.5                                (00:00:38)  Type:. .S.O. . .   Metric:1       Preference:1      Fallback: vrf zteDest:10.3.3.6                                (00:00:40)  Type:. .S.O. . .   Metric:1       Preference:1      RPF path list: abcZXROSNG(config-mcast)#show ip pim nexthop vrf ztePIM Nexthop TableNexthop state: R- Nexthop to RP,S- Nexthop to Source,       O- Related with Unicast,U- No Unicast Route,       L- Local Route,C- Connect to Dest, Dest:1.1.1.1                                 (00:02:52)  Type:. .S.O. . .   Metric:1       Preference:1      Fallback:  IP global显示信息说明：Dest：目的IP地址（下一跳的到期时间）；Type：下一跳路由的类型；Metric    ：下一跳的路由度量值；Preference：下一跳的路由优先级；Nexthop：下一跳IP地址；port：单播路由的出接口。Fallback：IP global表示下一跳是公网实例，vrf zte表示下一跳是私网zte实例。RPF path list：RPF路径列表。
相关命令 : 
pimsm：接口使能PIM-SM。 
## show ip pim rp hash 

show ip pim rp hash 
命令功能 : 
显示特定组播组选择的RP信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim rp hash 
  [vrf 
 ＜vrf-name 
＞] ＜group-address 
＞ 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜group-address＞|组播组地址，十进制点分形式
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的特定组播组选择的RP信息，可采用<vrf-name>来指定，不指定则显示公网的；2.必选参数＜group-address＞显示特定组播组选择的RP信息。
范例 : 
ZXROSNG(config)#show ip pim rp hash 224.1.1.1RP address: 3.1.1.2
相关命令 : 
rp-candidate：配置候选RP。static-rp：配置静态RP。
## show ip pim rp mapping 

show ip pim rp mapping 
命令功能 : 
显示所有的RP集信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
除用户模式外的其他所有模式:15,用户模式:1 
命令格式 : 
show ip pim rp mapping 
  [vrf 
 ＜vrf-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
缺省 : 
无 
使用说明 : 
查看特定VRF实例下的RP集信息，可采用<vrf-name>来指定，不指定则显示公网的RP集信息。 
范例 : 
ZXROSNG(config-mcast-pim)#show ip pim rp mappingGroup(s): 224.0.0.0/4(SM)  RP: 2.2.2.3, v2, Priority:192       BSR: 2.2.2.3, via bootstrap       Uptime: 1d0h, expires: 00:01:42  RP: 3.1.1.2, v2, Priority:192       BSR: 2.2.2.3, via bootstrap       Uptime: 1d0h, expires: 00:01:42Group(s): 224.0.0.0/4(SM)  RP: 3.1.1.2, Static, Priority:192Group(s): 0.0.0.0/0(NOUSED)显示信息说明：Group：组播组地址和掩码；RP：该组播组通告的候选RP地址，版本，优先级等；Static    ：表明此候选RP不是BSR通告，是本地静态配置的；BSR：BSR IP地址；Uptime    ：候选RP的存活时间；expires：候选RP的过期时间。
相关命令 : 
rp-candidate：配置候选RP。static-rp：配置静态RP。
## show ip pim traffic 

show ip pim traffic 
命令功能 : 
显示PIM流量统计信息。 
命令模式 : 
 用户模式,除用户模式外的其他所有模式  
命令默认权限级别 : 
用户模式:1,除用户模式外的其他所有模式:15 
命令格式 : 
show ip pim traffic 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
1.查看具体哪个VRF实例下的PIM流量统计信息，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个PIM接口的流量统计信息，可采用<interface-name>来指定，不指定则显示所有PIM接口的流量统计信息。
范例 : 
ZXROSNG(config)#show ip pim traffic vrf zte1PIM packet       Received   Sent       Filter     ErrorInterface: loopback2Hello:         0          3          0          0Join/Prune:    0          0          0          0Register:      0          0          0          0Register-Stop: 0          0          0          0Bootstrap:     0          0          0          0C-RP-Ad:       0          0          0          0Assert:        0          0          0          0State-Refresh: 0          0          0          0Graft:         0          0          0          0Graft-Ack:     0          0          0          0DF-Election:   0          0          0          0PFM-TLV:        0          0          0          0Interface: mvpn_tunnel1Hello:         2          4          0          0Join/Prune:    0          0          0          0Register:      0          0          0          0Register-Stop: 0          0          0          0Bootstrap:     1          0          0          0C-RP-Ad:       0          0          0          0Assert:        0          0          0          0State-Refresh: 0          0          0          0Graft:         0          0          0          0Graft-Ack:     0          0          0          0Df-Election:   0          0          0          0PFM-TLV:        0          0          0          0Total traffic in current PIM instance:Total:         3          7          0          0Hello:         2          7          0          0Join/Prune:    0          0          0          0Register:      0          0          0          0Register-Stop: 0          0          0          0Bootstrap:     1          0          0          0C-RP-Ad:       0          0          0          0Assert:        0          0          0          0State-Refresh: 0          0          0          0Graft:         0          0          0          0Graft-Ack:     0          0          0          0DF-Election:   0          0          0          0PFM-TLV:        0          0          0          0Current Time:  2017-09-25 19:03:20显示信息说明：1. 接口下协议报文收发信息显示说明，分发送，接收，接收过滤和接收错误四部分：Interface：接口名；Hello：Hello报文个数；Register：注册报文个数；Register-Stop：注册停止报文个数；Join/Prune：J/P报文个数；Bootstrap：BSM报文个数；Assert：Assert报文个数；C-RP-Ad：C-RP通告报文个数；State-Refresh：State-Refresh报文个数；Graft：Graft报文个数；Graft-Ack：Graft-Ack报文个数。DF-Election：DF-Election报文个数。PFM-TLV：PFM-TLV报文个数。2. PIM实例下信息显示说明：Total：汇总所有接口流量信息，具体报文同上；3. 当前系统时间显示说明：Current time：显示当前时间。
相关命令 : 
clear ip pim traffic：清除PIM流量统计信息。 
shutdown : 

shutdown 
命令功能 : 
关闭一个已配置好的MSDP邻居。使用no命令打开指定MSDP邻居。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
shutdown 
 
no shutdown 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
关闭IP地址为10.10.10.2的MSDP邻居：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)#shutdown
相关命令 : 
无 
## spt-threshold 

spt-threshold 
命令功能 : 
配置有直连接收者的路由器永不从RPT切换到SPT，使用no命令禁止这一特性。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
spt-threshold 
 infinity 
 [group-list 
 ＜access-list-name 
＞]
no spt-threshold 
命令参数解释 : 
参数|描述
---|---
infinity|常量，表示永不从RPT切换到SPT。
＜access-list-name＞|标准IP访问表名，范围1–31字符，定义了一个组范围。
缺省 : 
缺省情况下，从共享树切换到源最短路径树的阈值为0。 
使用说明 : 
infinity表示永不切换，group-list规定哪些组永不切换。 
范例 : 
配置有直连接收者的路由器永不从RPT切换到SPT。ZXROSNG(config-mcast-pim)#spt-threshold infinity
相关命令 : 
无 
## ssm enable 

ssm enable 
命令功能 : 
启用SSM协议。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
ssm enable 
 
no ssm enable 
命令参数解释 : 
					无
				 
缺省 : 
不启用SSM协议。 
使用说明 : 
PIM的SSM命令需要和IGMP的static-group和ssm-map配套使用。 
范例 : 
在PIM配置模式下启用SSM协议：ZXROSNG(config-mcast-pim)#ssm enable
相关命令 : 
ssm range：配置SSM组地址范围。 
## ssm range 

ssm range 
命令功能 : 
配置SSM组地址范围。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM-VRF模式:15,PIM模式:15 
命令格式 : 
ssm range 
  {default 
|group-list 
 ＜access-list-name 
＞}
no ssm range 
命令参数解释 : 
参数|描述
---|---
default|常量，表示默认SSM组范围。
＜access-list-name＞|ACL名，长度1-31个字符。
缺省 : 
缺省情况下为default，SSM支持的组范围是232.0.0.0/8。 
使用说明 : 
1.group-list配置SSM组范围；2.先要配置ssm enable，ssm range才有效。
范例 : 
配置缺省SSM组地址范围：ZXROSNG(config-mcast-pim)#ssm range default
相关命令 : 
ssm enable：启用SSM协议。 
## ssm-map static 

ssm-map static 
命令功能 : 
配置特定范围组向源地址的映射，使用no命令取消限制。 
命令模式 : 
 IGMP-VRF模式,IGMP模式  
命令默认权限级别 : 
IGMP模式:15,IGMP-VRF模式:15 
命令格式 : 
ssm-map static 
  {default 
|group-list 
 ＜acl-name 
＞} ＜source-address 
＞
no ssm-map static 
  [{default 
|group-list 
 ＜acl-name 
＞} ＜source-address 
＞]
				
命令参数解释 : 
参数|描述
---|---
default|映射default的组，default组是232.0.0.0-232.255.255.255
＜acl-name＞|SSM组访问列表名，范围1–31字符
＜source-address＞|源地址，点分十进制形式
缺省 : 
默认映射组范围232.0.0.0-232.255.255.255 
使用说明 : 
配置特定范围组向源地址的映射使用：ssm-map static {default|group-list ＜acl-name＞} ＜source-address＞;除非是默认映射范围组，否则用于映射的组地址必须在ssm range配置的group-list <acl-name>范围内才会map上源
范例 : 
配置IGMP源地址的映射：ZXROSNG(config-mcast-igmp)#ssm-map static group-list zte 122.1.1.1 
相关命令 : 
ssm enablessm range static-group 
## startup-query-count 

startup-query-count 
命令功能 : 
配置IGMP发送接口UP初始查询报文的次数，使用no命令恢复缺省值。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
startup-query-count 
  ＜number 
＞
no startup-query-count 
命令参数解释 : 
参数|描述
---|---
＜number＞|IGMP接口UP初始查询报文次数，缺省为2次，范围：1–10
缺省 : 
缺省为2 
使用说明 : 
以初始查询间隔为周期发送查询报文startup-query-count次后，使用query-interval为周期发送查询报文。 
范例 : 
配置IGMP接口UP初始查询报文次数：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/1/0/1ZXROSNG(config-mcast-igmp-if-gei-0/1/0/1)#startup-query-count 5
相关命令 : 
startup-query-intervalquery-interval
## startup-query-interval 

startup-query-interval 
命令功能 : 
配置IGMP发送接口UP初始查询报文的间隔，使用no命令恢复缺省值。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
startup-query-interval 
  ＜seconds 
＞
no startup-query-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|IGMP接口UP初始查询间隔，缺省为31秒，范围：1–18000，单位：秒
缺省 : 
缺省为31秒 
使用说明 : 
当接口UP后，查询路由器会发送一定次数（可以通过startup-query-count命令配置，默认值为2）的普通查询报文，查询报文发送间隔为此命令配置值和query-interval命令配置值/4中的较小值。一定次数发送结束后恢复以query-interval命令配置值为周期发送普通查询报文。 
范例 : 
配置IGMP接口UP初始查询间隔：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/1/0/1ZXROSNG(config-mcast-igmp-if-gei-0/1/0/1)#startup-query-interval 10
相关命令 : 
startup-query-countquery-interval
## static-first 

static-first 
命令功能 : 
设置组播查找单播路由静态下一跳优先。 
命令模式 : 
 组播VRF模式,组播模式  
命令默认权限级别 : 
组播VRF模式:15,组播模式:15 
命令格式 : 
static-first 
 
no static-first 
命令参数解释 : 
					无
				 
缺省 : 
静态下一跳优先级小于直连路由和本地路由。 
使用说明 : 
配置命令后，静态下一跳优先级大于直连路由和本地路由。
范例 : 
设置组播查找路由静态下一跳优先：ZXROSNG(config-mcast)# static-first  
相关命令 : 
nexthop 
## static-group 

static-group 
命令功能 : 
配置IGMP接口上的静态组成员，使用no命令删除接口上的静态组成员。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
static-group 
  ＜group-address 
＞ [inc-mask 
 ＜mask-address 
＞ count 
 ＜number 
＞] [source 
 {＜source-address 
＞ [{include 
|exclude 
}]|ssm-map 
}]
no static-group 
  ＜group-address 
＞ [inc-mask 
 ＜mask-address 
＞] [source 
 {ssm-map 
|＜source-address 
＞}]
				
命令参数解释 : 
参数|描述
---|---
＜group-address＞|静态IGMP加入组地址，十进制点分形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，十进制点分形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜source-address＞|源地址，十进制点分形式
include|切换到模式include
exclude|切换到模式exclude
ssm-map|通过map，获取源信息
缺省 : 
配置静态带源列表不带过滤模式的组加入默认模式是include。 
使用说明 : 
配置不带源的静态组加入使用：static group <group-address>;配置带源的静态组加入使用：static group <group-address> source {＜source-address＞ [{include|exclude}]|ssm-map}];RFC规定通过ssm-map源列表的模式默认是include，命令中ssm-map后模式参数不让配置。通过ssm-map配置带源的静态组加入时，必须在PIM模式/PIM-VRF模式下配置ssm-enable才能使该命令生效。配置批量的静态组加入：static-group  ＜group-address＞[  inc-mask <mask-address>  count <number>  ] [source {＜source-address＞ [{include|exclude}]|ssm-map}]批量配置静态组的时候，需要先使能PIM接口；反之，在删除PIM接口的时候，检查批量静态组是否存在，不存在才能执行no命令。
范例 : 
配置IGMP接口上的静态组成员：ZXROSNG(config-mcast-igmp-if-gei-0/1/0/1)#static-group 224.1.1.1 source 2.1.1.1ZXROSNG(config-mcast-igmp-if-gei-0/1/0/1)#static-group 224.1.1.1 source 2.1.1.2查看配置结果信息：ZXROSNG(config-mcast-igmp-if-gei-0/1/0/1)#show ip igmp groups detail Flags: S - Static Group, SSM - SSM Group, M - MDT GroupInterface:      gei-0/1/0/1Group:          224.1.1.1Flags:          Uptime:         00:00:45Group mode:     INCLUDELast reporter:  192.168.20.40Group source list: (M - SSM Mapping, S - Static, R - Report)  Source addr      Present   Expires   Fwd  Flag  2.1.1.1          00:00:45  Never     Yes  S      2.1.1.2          00:00:39  Never     Yes  S 
相关命令 : 
ssm-map static 
## static-rp override 

static-rp override 
命令功能 : 
配置静态RP优先。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
static-rp override 
 
no static-rp override 
命令参数解释 : 
					无
				 
缺省 : 
动态RP选举优先。 
使用说明 : 
如果没有配置此命令，则路由器优先选择BSR机制选出的C-RP，如果没有配置C-RP或者C-RP失效，静态RP才能生效；如果配置了此命令，则优先选择静态RP。 
范例 : 
配置静态RP优先：ZXROSNG(config-mcast-pim)#static-rp override
相关命令 : 
show ip pim rp mapping 
## static-rp 

static-rp 
命令功能 : 
配置静态RP地址，使用no命令删除静态RP地址。 
命令模式 : 
 PIM-VRF模式,PIM模式  
命令默认权限级别 : 
PIM模式:15,PIM-VRF模式:15 
命令格式 : 
static-rp 
  ＜ip-address 
＞ [{[group-list 
 ＜prefix-list-name 
＞],[priority 
 ＜priority 
＞]}]
no static-rp 
  ＜ip-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|静态RP地址，为十进制点分形式。
＜prefix-list-name＞|它定义了一个组范围，该范围是被通告rp服务范围。
＜priority＞|优先级，缺省为192，范围：0–255。
缺省 : 
没有静态RP设置。 
使用说明 : 
1.静态RP配置后即进入RP集参加选择，即使这个路由器没有收到任何BSR的RP信息通告；2.<prefix-list-name>参数配置RP服务范围，如果不带 <prefix-list-name>参数，静态RP适用于所有组播组；3.静态RP的缺省优先级为192，优先级数值较小的静态RP优先；如果优先级数值相同，则比较地址，地址大的RP优先。
范例 : 
配置地址11.1.1.1为静态RP地址，服务于所有组播组：ZXROSNG(config-mcast-pim)#static-rp 11.1.1.1 priority 100show命令查看配置结果信息：ZXROSNG(config-mcast-pim)#show ip pim rp mappingGroup(s): 224.0.0.0/4(SM)  RP: 11.1.1.1, Static, Priority:100Group(s): 0.0.0.0/0(NOUSED)
相关命令 : 
show ip pim rp mapping：显示所有的RP集信息。 
## triggered-hello-delay 

triggered-hello-delay 
命令功能 : 
配置triggered hello报文的延时时间，使用no命令恢复缺省值。 
命令模式 : 
 PIM-VRF接口模式,PIM接口模式  
命令默认权限级别 : 
PIM-VRF接口模式:15,PIM接口模式:15 
命令格式 : 
triggered-hello-delay 
  ＜seconds 
＞
no triggered-hello-delay 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|PIM路由器triggered hello报文的延时时间，缺省为5秒，范围：1–5，单位：秒。
缺省 : 
PIM路由器triggered hello报文的延时时间，缺省为5秒。 
使用说明 : 
无 
范例 : 
在路由器接口gei-0/1/0/1上配置triggered hello报文的延时时间：ZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#triggered-hello-delay 25
相关命令 : 
无 
## ttl-security-hops 

ttl-security-hops 
命令功能 : 
限制本地接收MSDP邻居数据包的ttl范围，使用no命令取消限制。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
ttl-security-hops 
  ＜ttl-hops 
＞
no ttl-security-hops 
命令参数解释 : 
参数|描述
---|---
＜ttl-hops＞|TTL值，范围：1–254
缺省 : 
无 
使用说明 : 
此命令限制限制本地接收MSDP邻居数据包的ttl范围。若配置为n，只有当邻居数据包IP头中的TTL在范围<255-n+1，255> 之内时，本地才接收该数据包。 
范例 : 
配置IP地址为10.10.10.2的MSDP邻居上的ttl-security-hops为8跳：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)#ttl-security-hops 8
相关命令 : 
无 
## ttl-threshold 

ttl-threshold 
命令功能 : 
限制组播数据包封装在SA报文中发送给MSDP邻居的范围。使用no命令取消限制。 
命令模式 : 
 MSDP-PEER-VRF模式,MSDP-PEER模式  
命令默认权限级别 : 
MSDP-PEER模式:15,MSDP-PEER-VRF模式:15 
命令格式 : 
ttl-threshold 
  ＜ttl-threshold 
＞
no ttl-threshold 
命令参数解释 : 
参数|描述
---|---
＜ttl-threshold＞|TTL值,范围：1–255
缺省 : 
ttl-threshold缺省为1. 
使用说明 : 
此命令用于限制封装了组播数据报的SA报文的发送。只有当组播数据包IP头中的TTL不小于配置的< ttl-value> 参数时，才能向指定的MSDP邻居转发。 
范例 : 
配置IP地址为10.10.10.2的MSDP邻居上的TTL threshold为8跳：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router msdpZXROSNG(config-mcast-msdp)#peer 10.10.10.2ZXROSNG(config-mcast-msdp-peer)#ttl-threshold 8
相关命令 : 
无 
## unsolicited-report-interval 

unsolicited-report-interval 
命令功能 : 
在上游接口上，配置主机侧初始发送report报文的间隔，使用no命令恢复缺省状态。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP-VRF接口模式:15,IGMP接口模式:15 
命令格式 : 
unsolicited-report-interval 
  ＜seconds 
＞
no unsolicited-report-interval 
命令参数解释 : 
参数|描述
---|---
＜seconds＞|缺省值为10秒,配置范围1-25，单位秒。
缺省 : 
缺省值为10秒 
使用说明 : 
配置准备第一次发送成员关系的时延间隔 
范例 : 
配置准备第一次发送成员关系的时延间隔：ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#unsolicited-report-interval  2
相关命令 : 
无 
## version 

version 
命令功能 : 
配置接口上IGMP协议版本号，使用no命令恢复缺省状态。 
命令模式 : 
 IGMP-VRF接口模式,IGMP接口模式  
命令默认权限级别 : 
IGMP接口模式:15,IGMP-VRF接口模式:15 
命令格式 : 
version 
  {1 
|2 
|3 
}
no version 
命令参数解释 : 
参数|描述
---|---
1|IGMP版本号，代表igmpv1
2|IGMP版本号，代表igmpv2
3|IGMP版本号，代表igmpv3
缺省 : 
版本缺省是IGMPv2。 
使用说明 : 
同一子网上所有IGMP路由器和主机都必须配置相同的版本号，出于组播网络安全方面的考虑，不支持IGMP V1自动侦测和协商。
范例 : 
配置接口上IGMP协议版本号：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router igmpZXROSNG(config-mcast-igmp)#interface gei-0/7/1/2ZXROSNG(config-mcast-igmp-if-gei-0/7/1/2)#version 2
相关命令 : 
无 
## vrf 

vrf 
命令功能 : 
配置组播VRF模式。使用no命令取消配置。 
命令模式 : 
 组播模式  
命令默认权限级别 : 
15 
命令格式 : 
vrf 
  ＜vrf-name 
＞
no vrf 
  ＜vrf-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF的名称，长度1-32个字符。
缺省 : 
关闭VRF模式。 
使用说明 : 
需要先配置VRF实例，才能在组播配置模式下通过此命令配置组播VRF模式。
范例 : 
配置组播VRF模式：ZXROSNG(config)# ip vrf zteZXROSNG(config-vrf-zte)#rd 1：2ZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#exitZXROSNG(config-vrf-zte)#exitZXROSNG(config)#ip multicast-routing     ZXROSNG(config-mcast)#vrf zte   ZXROSNG(config-mcast-vrf-zte)#
相关命令 : 
ip vrfaddress-familyrd：在VRF实例创建后需要进一步配置rd，才能使能实例供vrf等其他命令使用。
