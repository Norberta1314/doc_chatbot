# IPv6基础配置命令 
## clear ipv6 traffic 


clear ipv6 traffic 




命令功能 :

该命令工作于特权模式，用于清除IPv6、ICMPv6、TCP6和UDP6层的收发以及异常计数。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear ipv6 traffic 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

如果用户不需要之前的统计信息，可以用此命令清除。清除之后各统计项从0开始重新计数。 






范例 :

ZXROSNG#clear ipv6 trafficZXROSNG#show ipv6 trafficIPv6 statistics:  Rcvd: 0 total, 0 local destination        format errors      truncated datagrams  hop count exceeded        0                  0                    0                               unknown protocol        0   Frags:reassembled        timeouts             couldn't reassemble        0                  0                    0                               fragmented         couldn't fragment        0                  0                      Mcast:received           sent        0                  0                      Sent: generated          forwarded            encapsulation failed    no route        0                  0                    0                       0ICMPv6 statistics:  Rcvd: 0 total        format errors      checksum errors      bad code          bad len        0                  0                    0                       0        dest unreach       packet too big       time exceeded     param problem        0                  0                    0                       0        echo request       echo reply           redirects        0                  0                    0                               group query        group report(v1)     group reduce       group report(v2)              0                  0                    0                       0                           router solicit        router advert        neighbor solicit      neighbor advert               0                  0                    0                       0                   Sent: error messages     rate-limited         0                  0                            dest unreach       packet too big       time exceeded     param problem        0                  0                    0                       0        echo request       echo reply           redirects        0                  0                    0                               group query        group report(v1)     group reduce       group report(v2)              0                  0                    0                       0                           router solicit     router advert        neighbor solicit   neighbor advert               0                  0                    0                       0                 UDP6 statistics:  Rcvd: 0 total, 0 no checksum, 0 checksum errors,         0 bad len, 0 no port  Sent: 0 totalTCP6 statistics:  Rcvd: 0 total, 0 checksum errors  Sent: 0 total





相关命令 :

show ipv6 traffic 




## debug ipv6 icmp 


debug ipv6 icmp 




命令功能 :

该命令工作于特权模式，用于开启ICMPv6报文发送与接收打印开关。该命令主要用于故障诊断，开启该开关后，可以查看本地所有ICMPv6报文的收发情况。





命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 icmp 
  [address 
 ＜ipv6-address 
＞]

no debug ipv6 icmp 








命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|IPv6地址,可以是源地址或目的地址








缺省 :

无 






使用说明 :

该命令需要与terminal monitor命令同时使用，否则看不到相关打印信息。可以通过命令show debug icmp6查看该打印开关是否开启。该打印开关默认为关闭，即不打印ICMPv6报文的收发信息。





范例 :

ZXROSNG#debug ipv6 icmp  ZXROSNG#terminal monitorZXROSNG#ping6 100::1 repeat 1 size 400sending 1,400-byte ICMP echo(es) to 100:0:0:0:0:0:0:1,timeout is 2 second(s).ZXR10 MPU-0/20/0 2014-7-2 09:04:31 ICMPv6: Sending to 100::1 type:echo request ZXR10 MPU-0/20/0 2014-7-2 09:04:31 ICMPv6: Received from 100::1 type:echo request ZXR10 MPU-0/20/0 2014-7-2 09:04:31 ICMPv6: Sending to 100::1 type:echo reply !ZXR10 MPU-0/20/0 2014-7-2 09:04:31 ICMPv6: Received from 100::1 type:echo reply输出信息中的参数信息解释如下：参数名称         参数说明MPU-0/20/0       单板名称Sending          发送Received         接收echo request     ICMP回显请求报文echo reply       ICMP回显应答报文ZXROSNG#debug ipv6 icmp address 1::2ZXROSNG#ping6 1::2sending 5,100-byte ICMP echo(es) to 1:0:0:0:0:0:0:2,timeout is 2 second(s).ZXR10 MPU-0/20/0 2017-7-3 19:18:23 ICMPv6: Sending to 1::2 Source is 1::1 type:echo request !ZXR10 MPU-0/20/0 2017-7-3 19:18:23 ICMPv6: Received from 1::2 Destination is 1::1 type:echo reply 






相关命令 :

terminal monitor



## debug ipv6 packet 


debug ipv6 packet 




命令功能 :

该命令工作于特权模式，用于开启IPv6报文发送与接收打印开关。该命令主要用于故障诊断，开启该开关后，可以查看所有本地IPv6报文的收发情况。





命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 packet 
  [interface 
 ＜interface-name 
＞] [protocol 
 ＜protocol-name 
＞] [detail 
] [address 
 ＜ipv6-address 
＞]

no debug ipv6 packet 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称，字符类型，长度为1-32
＜protocol-name＞|指定协议类型为icmp、tcp、udp、vrrp、ospf、pim
detail|显示IPv6协议处理的具体调试信息
＜ipv6-address＞|指定IPv6地址（源地址或目的地址）








缺省 :

关闭该调试功能





使用说明 :

该命令需要与terminal monitor命令同时使用，否则看不到相关打印信息。可以通过命令show debug ipv6查看该打印开关是否开启。该打印开关默认为关闭，即不打印IPv6报文的收发信息。由于该命令打印的是所有本地IPv6报文的收发情况，可能会打印大量的无关报文收发信息，建议指定接口或者指定协议来打印某一接口上的报文或者某种协议的报文。





范例 :

ZXROSNG#debug ipv6 packet interface loopback1IPv6 packets debugging is onZXROSNG#terminal monitor ZXR10 MPU-0/20/0 2014-7-2 08:47:28 IPv6: sent on:loopback1     source: 100::1     dest:  100::1     flow label:0 ,payload length:260 ,hops:64 ,nexthead:58 sending 1,300-byte ICMP echo(es) to 100:0:0:0:0:0:0:1,timeout is 2 second(s).ZXR10 MPU-0/20/0 2014-7-2 08:47:28 IPv6: rcvd on:loopback1     source: 100::1     dest:  100::1     flow label:0 ,payload length:260 ,hops:64 ,nexthead:58     输出信息中的参数信息解释如下：参数名称        参数说明MPU-0/20/0      单板名称sent            发送rcvd            接收source          源IPv6地址dest            目的IPv6地址






相关命令 :

terminal monitor 




## error packet ipv6 record 


error packet ipv6 record 




命令功能 :

配置IPv6错误报文记录功能是否使能。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



error packet ipv6 record 
  {disable 
|enable 
}







命令参数解释 :



参数|描述
---|---
disable|IPv6错误报文记录功能去使能
enable|IPv6错误报文记录功能使能








缺省 :

IPv6错误报文记录功能使能。 






使用说明 :

当该功能使能后，收到的IPv6错误报文被记录，IPSTACK_RP、IPSTACK_LP、LPP每个收包进程最多可以记录200条，当超过200条以后，时间最老的记录会被新记录覆盖；当该功能去使能后，收到的IPv6错误报文不再记录。





范例 :

ZXROSNG(config)# error packet ipv6 record enableZXROSNG(config)# error packet ipv6 record disable





相关命令 :

show error packet ipv6 




## show debug icmp6 


show debug icmp6 




命令功能 :

该命令工作于除用户模式之外的所有模式，用于查看ICMPv6 debug开关是否开启。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug icmp6 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于帮助用户查看ICMPv4 debug开关开启情况，在debug ipv6 icmp开关关闭的情况下，执行该命令后没有debug开关关闭的回显信息，只有在debug ipv6 icmp开关开启时，才会有相应的回显信息。 






范例 :

ZXROSNG#debug ipv6 icmp  ICMPv6 debugging is onZXROSNG#show debug icZXROSNG#show debug icmp6ICMP6:  ICMP6 packet debugging is on





相关命令 :

debug ipv6 icmp



## show debug ipv6 


show debug ipv6 




命令功能 :

该命令工作于除用户模式之外的所有模式，用于查看IPv6 debug开关是否开启。





命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :


show debug ipv6 
 






命令参数解释 :


					无
				 






缺省 :

关闭该调试功能 






使用说明 :

该命令用于帮助用户查看IPv6 debug开关开启情况，在debug ipv6 packet开关关闭的情况下，执行该命令后没有debug开关关闭的回显信息，只有在debug ipv6 packet开关开启时，才会有相应的回显信息。 






范例 :

ZXROSNG#debug ipv6 packet protocol udp  ZXROSNG#debug ipv6 packet protocol udp IPv6 packets debugging is onZXROSNG#show debug ipv6IPv6:  IPv6 packets debugging is on(all interface|udp6|no detail)





相关命令 :

debug ipv6 packet 




## show error packet ipv6 


show error packet ipv6 




命令功能 :

查看IPv6错误报文记录。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show error packet ipv6 
  [number 
 ＜number 
＞] 







命令参数解释 :



参数|描述
---|---
＜number＞|每个收包进程显示的错误报文记录个数








缺省 :

不指定CPU和显示个数时，每个收包进程显示10条记录。 






使用说明 :

指定显示个数时，每个收包进程显示指定个数的记录。 






范例 :

ZXROSNG(config)# show error packet ipv6CPU         : MPU-0/1/0Instance ID : 1Seq ID      : 2Record Time : 2016-06-01 14:50:02Interface   : gei-0/1/0/8Source MAC  : 2e:7d:a4:ec:28:faError Reason: IP router opt with unknown next protoPacket Len  : 56Packet      : 0000:60 00 00 00 00 10 2b 40 01 00 00 00 00 00 00 00 0010:00 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 0020:00 00 00 00 00 00 00 02 2b 00 00 00 00 00 00 00 0030:3b 00 00 00 00 00 00 00 ----------------------------------------------------CPU         : MPU-0/1/0Instance ID : 1Seq ID      : 1Record Time : 2016-06-01 14:49:02Interface   : gei-0/1/0/8Source MAC  : 2e:7d:a4:ec:28:faError Reason: IP router opt with unknown next protoPacket Len  : 56Packet      : 0000:60 00 00 00 00 10 2b 40 01 00 00 00 00 00 00 00 0010:00 00 00 00 00 00 00 01 01 00 00 00 00 00 00 00 0020:00 00 00 00 00 00 00 02 2b 00 00 00 00 00 00 00 0030:3b 00 00 00 00 00 00 00 ----------------------------------------------------输出信息中的参数信息解释如下：参数名称           参数说明CPU            错误报文记录所在的Cpu名称Instance ID    收包进程的ID号Seq ID         记录号Record Time    记录时间Interface      收包接口Source MAC     报文中的源MAC地址Error Reason   错误原因Packet Len     报文长度Packet         报文内容





相关命令 :

error packet ipv6 record 




## show ipv6 pmtu 


show ipv6 pmtu 




命令功能 :

该命令工作于除用户模式之外的所有模式，用于查看学习到的IPv6 PMTU条目。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 pmtu 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于帮助用户查看IPv6 PMTU条目，以及条目对应的源地址、目的地址、VRFNAME以及条目剩余的老化时间。 






范例 :

ZXROSNG(config)#show ipv6 pmtuMTU     Timeout      Src              Dest      Vrfname(Vpnid)1400     6m          100::1            202::1            11400     6m          100::1            203::1            11400     6m          100::1            201::1            11400     6m          100::1            204::1            11400     6m          100::1            205::1            1输出信息中的参数信息解释如下：参数名称          参数说明MTU               路径mtu值Timeout           剩余的老化时间Src               PMTU条目的源IPv6地址Dest              PMTU条目的目的IPv6地址Vrfname(Vpnid)    PMTU条目所属的VRFNAME，当对应的VPN删掉后，显示vpnid






相关命令 :

无 




## show ipv6 traffic 


show ipv6 traffic 




命令功能 :

该命令工作于除用户模式之外的所有模式，用于显示IPv6传输的统计信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 traffic 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令主要用来显示IPv6、ICMPv6、TCP6和UDP6层的收发以及异常计数。可以结合clear ipv6 traffic命令查看某个时间段内的IPv6协议栈报文收发个数 






范例 :

ZXROSNG#show ipv6 traffic IPv6 statistics:  Rcvd: 29 total, 26 local destination        format errors    truncated datagrams  hop count exceeded        0                0                    0                               unknown protocol        0   Frags:reassembled      timeouts          couldn't reassemble        0                0                 0                               fragmented       couldn't fragment        0                0                      Mcast:received         sent        23               4                      Sent: generated        forwarded         encapsulation failed    no route        10               0                 0                       0ICMPv6 statistics:  Rcvd: 13 total        format errors    checksum errors   bad code          bad len        0                0                 0                 0        dest unreach     packet too big    time exceeded     param problem        0                0                 0                 0        echo request     echo reply        redirects        3                3                 0                        group query      group report(v1)  group reduce      group report(v2)        0                0                 0                 3                          router solicit   router advert     neighbor solicit  neighbor advert          3                0                 1                 0                  Sent: error messages   rate-limited         20               0                            dest unreach     packet too big    time exceeded     param problem        0                0                 0                 0        echo request     echo reply        redirects        3                3                 0                               group query      group report(v1)  group reduce      group report(v2)        0                0                 0                 0                          router solicit   router advert     neighbor solicit  neighbor advert          0                0                 3                 1                UDP6 statistics:  Rcvd: 16 total, 0 no checksum, 0 checksum errors,         0 bad len, 16 no port  Sent: 0 totalTCP6 statistics:  Rcvd: 0 total, 0 checksum errors  Sent: 0 total  输出信息中的参数信息解释如下：参数名称                  参数说明IPv6 statistics           IPv6层的统计信息Rcvd                      收到的IP报文total                     总数local destination         本地报文个数format errors             由于IP头错误而丢包的个数truncated datagrams       收到报文长度错误的报文个数。hop count exceeded        在转发过程中由于hoplimit耗尽而丢包的个数unknown protocol          由于对应的协议没有开启（不在运行）而丢包的个数Frags                     分片报文reassembled               重组成功的报文个数timeouts                  重组超时的报文个数couldn't reassemble       重组失败的报文个数fragmented                分片成功的报文个数couldn't fragment         分片失败的报文个数Mcast                     组播报文received                  收到的组播报文个数sent                      发送的组播报文个数Sent                      发送的报文generated                 本地发送的个数forwarded                 转发的个数encapsulation failed      在IP封装过程由于某些错误（包括查不到路由、路由类型错误、出接口没有up、内存不够等）而丢包的个数no route                  由于查不到路由而丢包的个数ICMPv6 statistics         ICMPv6层的统计信息Rcvd                      收到的ICMPv6报文total                     总数format errors             由于头错误（包括报文头长度错误等）而丢包的个数checksum errors           由于校验和错误而丢包的个数bad code                  由于code字段错误而丢包的个数bad len                   由于报文长度错误而丢包的个数dest unreach              收到的目的不可达报文个数packet too big            收到的包过大报文个数time exceeded             收到的超时报文个数param problem             收到的参数错误报文个数echo request              收到的回显请求报文个数echo reply                收到的回显应答报文个数redirects                 收到的重定向报文个数group query               收到的group query报文个数group report(v1)          收到的group report(v1)报文个数group reduce              收到的group reduce报文个数group report(v2)          收到的group report(v2)报文个数router solicit            收到的路由器请求报文个数router advert             收到的路由器公告报文个数neighbor solicit          收到的邻居请求报文个数neighbor advert           收到的邻居公告报文个数Sent                      发送的ICMPv6报文error messages            发送的ICMPv6错误报文个数rate-limited              由于限速而丢掉的ICMPv6报文个数dest unreach              发出的目的不可达报文个数packet too big            发出的包过大报文个数time exceeded             发出的超时报文个数param problem             发出的参数错误报文个数echo request              发出的回显请求报文个数echo reply                发出的回显应答报文个数redirects                 发出的重定向报文个数group query               发出的group query报文个数group report(v1)          发出的group report(v1)报文个数group reduce              发出的group reduce报文个数group report(v2)          发出的group report(v2)报文个数router solicit            发出的路由器请求报文个数router advert             发出的路由器公告报文个数neighbor solicit          发出的邻居请求报文个数neighbor advert           发出的邻居公告报文个数UDP6 statistics           UDP6层的统计信息Rcvd                      收到的UDP6报文total                     收到的UDP6报文个数no checksum               收到的没有填写校验和的UDP6报文个数checksum errors           由于校验和错误而丢包的个数bad len                   由于报文长度错误而丢包的个数no port                   由于端口没有开启而丢包的个数TCP6 statistics           TCP6层的统计信息Rcvd                      收到的TCP6报文total                     收到的TCP6报文个数checksum errors           由于校验和而丢包的个数Sent                      发送的TCP6报文total                     发送的TCP6报文个数






相关命令 :

clear ipv6 traffic 




# IPv6静态路由配置命令 
## ipv6 route nexthop 


ipv6 route nexthop 




命令功能 :

该命令在全局配置模式下执行，用于在配置公网IPv6静态路由非直连下一跳带BFD检测时，创建BFD会话时需要指定一个本端接口地址作为其local地址。这种情况下，为BFD会话指定本地接口地址时使用该命令。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 route nexthop 
 source 
 ＜if_name 
＞

no ipv6 route nexthop 
 source 








命令参数解释 :



参数|描述
---|---
source|<作用> 辅助参数，表示创建BFD 多跳会话下一跳对应的源端。
＜if_name＞|<作用> 配置绑定的接口名称。绑定该接口后，使用该接口的地址作为BFD会话的local地址。<取值范围>目前只支持loopback口。<默认值> 不绑定任何接口








缺省 :

无 






使用说明 :

1、此命令与IPv6静态路由配置命令（参见配置命令ipv6 route）以及BFD会话配置命令（参见配置命令bfd）配合使用。2、该命令只适用于公网静态路由非直连下一跳创建BFD会话时使用。3、当前仅支持配置loopback接口，采用loopback接口地址作为BFD会话的local端地址。4、如果未配置该命令，或者命令绑定的接口无IPv6地址，则不创建BFD 会话。等接口IPv6地址更新时才会通知IPv6静态路由创建BFD 会话。5、当变更绑定的接口时，若新接口无IPv6地址，则会删除原先的BFD会话；若新指定的loopback口中有IPv6地址，则会依据新IPv6更新BFD会话。6、当删除绑定的接口，也就是操作删除命令解除绑定时，会直接删除原先的BFD会话。7、目前该命令全局仅可配置一条。





范例 :

1. 配置v6静态路由指定源端下一跳：ZXROSNG(config)#ipv6 route nexthop source loopback1 ZXROSNG(config)#sho running-config ipv6-static !<ipv6-static>ipv6 route nexthop source loopback1!</ipv6-static>2. 删除v6静态路由指定源端下一跳：ZXROSNG(config)#no ipv6 route nexthop source ZXROSNG(config)#
ZXROSNG(config)#sho running-config ipv6-static      ZXROSNG(config)#






相关命令 :

无 




## ipv6 route 


ipv6 route 




命令功能 :

该命令在全局配置模式下执行，用于手动配置IPv6静态路由。在网络管理员对全网拓扑熟悉的情况下，可以根据自己的路由需求通过该命令进行手动配置，以达到对网络中路由行为的精确控制。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 route 
  [vrf 
 {mng 
|＜vrf-name 
＞}] ＜ipv6-address-mask 
＞ {＜ipv6-address 
＞ [＜distance 
＞] [metric 
 ＜cost 
＞] [tag 
 ＜tag-value 
＞] [bfd 
 enable 
]|＜interface-name 
＞ {＜ipv6-address 
＞ [＜distance 
＞] [metric 
 ＜cost 
＞] [tag 
 ＜tag-value 
＞] [bfd 
 enable 
]|[＜distance 
＞] [metric 
 ＜cost 
＞] [tag 
 ＜tag-value 
＞]}} [track 
 ＜track-name 
＞] [name 
 ＜static-description 
＞]
no ipv6 route 
  [vrf 
 {mng 
|＜vrf-name 
＞}] {all 
|＜ipv6-address-mask 
＞ [{＜ipv6-address 
＞|＜interface-name 
＞ [＜ipv6-address 
＞]}]}
				






命令参数解释 :



参数|描述
---|---
mng|<作用>删除管理口静态路由。
＜vrf-name＞|<作用> 私网静态路由对应的VRF名称，不配置该参数表示配置公网静态路由。<取值范围> VRF名称的取值长度为1-32字符。<默认值> 无
＜ipv6-address-mask＞|<作用>删除IPv6静态路由的网络前缀及掩码长度<取值范围>前缀不支持的类型：组播地址，还回地址，link-local地址，掩码长度取值范围0-128取值范围<默认值>无
＜ipv6-address＞|<作用>IPv6静态路由下一跳网关地址前缀(这个下一跳地址是配置出接口时指定的下一跳，只有配置了静态路由出接口时，该参数才允许配置。)<取值范围>不支持的地址类型：全零地址，还回地址，link-local地址，组播地址<默认值>无
＜distance＞|<作用>IPv6静态路由管辖距离<取值范围> 1–255<默认值>1
＜cost＞|<作用>配置IPv6静态路由的度量值<取值范围>0-255<默认值>0
＜tag-value＞|<作用>IPv6静态路由的路由标识<取值范围>0-4294967295<默认值>0
enable|<作用>使能IPv6静态路由关联bfd检测的开关<取值范围>0-1<默认值>0
＜interface-name＞|<作用>配置IPv6静态路由的出接口名<默认值>无
＜ipv6-address＞|<作用>IPv6静态路由下一跳网关地址前缀(这个下一跳地址是配置出接口时指定的下一跳，只有配置了静态路由出接口时，该参数才允许配置。)<取值范围>不支持的地址类型：全零地址，还回地址，link-local地址，组播地址<默认值>无
＜distance＞|<作用>IPv6静态路由管辖距离<取值范围> 1–255<默认值>1
＜cost＞|<作用>配置IPv6静态路由的度量值<取值范围>0-255<默认值>0
＜tag-value＞|<作用>IPv6静态路由的路由标识<取值范围>0-4294967295<默认值>0
enable|<作用>使能IPv6静态路由关联bfd检测的开关<取值范围>0-1<默认值>0
＜distance＞|<作用>IPv6静态路由管辖距离<取值范围> 1–255<默认值>1
＜cost＞|<作用>配置IPv6静态路由的度量值<取值范围>0-255<默认值>0
＜tag-value＞|<作用>IPv6静态路由的路由标识<取值范围>0-4294967295<默认值>0
＜track-name＞|<作用>为静态路由故障联动处理关联的track名称<取值范围> 1-31字符。<默认值> 缺省不关联track检测对象
＜static-description＞|<作用> IPv6静态路由描述信息。<取值范围> 1-64字符。<默认值> 无






No参数|描述
---|---
all|删除当前网络内所有静态路由。








缺省 :

缺省情况下表示没有配置IPv6静态路由 






使用说明 :

1、只有在设备配置了相应的VPN（参见ip vrf配置命令）后才可配置私网静态路由。2、<distance>相当于路由协议的优先级，值越小，优先级越高。缺省情况下静态路由的优先级高于动态路由，默认为1，但是通过设置可使动态路由优先于静态路由。3、bfd enable为静态路由关联bfd检测的使能开关。取消bfd检测，采用删除路由或者配置相同路由而不配置bfd选项的方式。4、配置静态路由关联track对象检测，只有在通过SAMGR（参见samgr配置命令）配置了track检测对象的情况下，配置的静态路由才可生效。5、仅配置出接口形式的静态路由不允许配置关联BFD检测。6、当指定的出接口为以太网接口或三层VLAN接口时，建议配置下一跳，否则可能导致下层流量不通。7、可配置的最大静态路由条目数由性能参数控制，目前在ROSNGV3.00.10版本默认可配置的最大数目为16K。8、该命令一些参数之间存在的其他限制请参考参数说明。






范例 :

1. 发给网络10::/60的包将被路由到拥有地址100::2的路由器转发：ZXROSNG(config)#ipv6 route 10::/60 100::22. 发给网络20::/56的包将被从接口loopback1转发：ZXROSNG(config)#ipv6 route 20::/56 loopback13. 发给网络30::/56的包将被从接口loopback转发到拥有地址100::3地址的路由器                                                                             ZXROSNG(config)#ipv6 route 30::/56 loopback1 100::3 4. 发给网络30::/56的包将被负载均衡转发到拥有地址100::3和100::6的路由器：ZXROSNG(config)#ipv6 route 30::/56 100::3ZXROSNG(config)#ipv6 route 30::/56 100::65. 发给网络30::/56的包将被优先转发到拥有地址100::3的路由器：ZXROSNG(config)#ipv6 route 30::/56 100::3 ZXROSNG(config)#ipv6 route 30::/56 100::6 106. 发给网络30::/56的包将被优先转发到拥有地址100::3的路由器：ZXROSNG(config)#ipv6 route 30::/56 100::3 10ZXROSNG(config)#ipv6 route 30::/56 100::6 10 metirc 207. 配置静态路由bfd检测ZXROSNG(config)#ipv6 route 30::/56 100::3 bfd enable取消此路由的bfd检测ZXROSNG(config)#ipv6 route 30::/56 100::38. 配置到达vrf名为zte的10::/90的从200::2路由器转发的静态路由        ZXROSNG(config)#ipv6 route vrf zte 10::/90 200::29. 删除vrf名为zte的10::/90的从200::2路由器转发的静态路由ZXROSNG(config)#show running-config ipv6-static ! <ipv6-static>ipv6 route vrf zte 10::/90 200::2! </ipv6-static>ZXROSNG(config)#no ipv6 route vrf zte 10::/90 200::210. 删除vrf名为zte的10::/90的从所有路由器转发的静态路由ZXROSNG(config)#show running-config ipv6-static ! <ipv6-static>ipv6 route vrf zte 10::/90 200::2ipv6 route vrf zte 10::/90 200::3ipv6 route vrf zte 10::/90 200::4ipv6 route vrf zte 10::/90 200::5ipv6 route vrf zte 10::/90 200::6ipv6 route vrf zte 10::/90 loopback1! </ipv6-static>ZXROSNG(config)#no ipv6 route vrf zte 10::/90ZXROSNG(config)#show running-config ipv6-static






相关命令 :

无 




## ipv6 route-static bfd 


ipv6 route-static bfd 




命令功能 :

配置IPv6静态路由的BFD模板。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 route-static bfd 
  {＜interface-name 
＞|[vrf 
 ＜vrf-name 
＞] local-address 
 ＜ipv6-address 
＞} nexthop 
 ＜ipv6-address 
＞ template 
 ＜template-name 
＞
no ipv6 route-static bfd 
  {＜interface-name 
＞|[vrf 
 ＜vrf-name 
＞] local-address 
 ＜ipv6-address 
＞} nexthop 
 ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|IPv6静态路由指定的接口名
＜vrf-name＞|VRF名称，长度为1-32个字符。
＜ipv6-address＞|IPv6地址。
＜template-name＞|BFD模板名，长度为1-31个字符








缺省 :

无。 






使用说明 :

使用场景当配置静态路由的BFD需要指定多种配置参数时，可以通过配置BFD模板名实现该模板名下的BFD参数配置。注意事项1.配置静态路由BFD模板的最大个数为$#134283310#$。2.配置BFD模板需要对应静态路由创建BFD会话成功才能生效。3.指定出接口和下一跳地址时配置的是单跳BFD会话模板，指定本端地址和下一跳地址时配置的是多跳BFD会话模板。






范例 :

1.配置一条IPv6静态路由的单跳BFD模板名为”$zte$”：ZXROSNG(config)#ipv6 route-static bfd fei-0/1/0/1 nexthop 1300::2 template $zte$2.配置一条IPv6静态路由的多跳BFD模板名为”!zte!”：ZXROSNG(config)#ipv6 route-static bfd nexthop 1100::1 local-address 1300::1 template !zte!






相关命令 :

ipv6 route 




## ipv6 route-static 


ipv6 route-static 




命令功能 :

使能IPv6静态路由FRR路由计算功能。使用no命令关闭此功能。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 route-static 
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
no ipv6 route-static 
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
＜vrf-name＞|VRF名称，长度1~32个字符
fast-reroute|辅助参数，使能静态路由FRR
＜time-interval＞|<作用> 设置回切wtr（Waiting-Time-Return） 延迟的时间间隔。<取值范围> 范围为0-12（mins）。<默认值> 0
protect|辅助参数，去使能静态路由保护其他协议路由
rip|去使能静态路由保护RIP路由
ospf|去使能静态路由保护OSPF路由
bgp|去使能静态路由保护BGP路由
isis|去使能静态路由保护ISIS路由
recursion-l3vpn|支持静态路由迭代到L3-VPN路由。
fast-reroute|辅助参数，使能静态路由FRR
＜time-interval＞|<作用> 设置回切wtr（Waiting-Time-Return） 延迟的时间间隔。<取值范围> 范围为0-12（mins）。<默认值> 0
protect|辅助参数，去使能静态路由保护其他协议路由
rip|去使能静态路由保护RIP路由
ospf|去使能静态路由保护OSPF路由
bgp|去使能静态路由保护BGP路由
isis|去使能静态路由保护ISIS路由






No参数|描述
---|---
all|关闭所有网络的FRR功能。
all|关闭所有网络的FRR功能。








缺省 :

不配置命令代表关闭frr计算路由功能 






使用说明 :

IPv6静态路由的主备路由形成条件为，不同出接口，不同管辖距离或度量值的相同目的地址路由。 






范例 :

1.使能公网IPv6静态路由计算frr路由功能：ZXROSNG(config)#ipv6 route-static fast-reroute ZXROSNG(config)#2.使能私网(vrf名为zte)IPv6静态路由计算frr路由功能：  ZXROSNG(config)#ipv6 route-static vrf zte fast-reroute ZXROSNG(config)#3.设置wtr的时间间隔为2分钟ZXROSNG(config)#ipv6 route-static fast-reroute wtr 2ZXROSNG(config)#4.取消IPv6静态路由FRR功能ZXROSNG(config)#no ipv6 route-static fast-reroute ZXROSNG(config)#5. 使能公网IPv6静态路由保护RIP路由ZXROSNG(config)#ipv6 route-static protect rip6. 使能私网zte的IPv6静态路由保护BGP路由ZXROSNG(config)#ipv6 route-static vrf zte protect bgp7. 去使能私网zte的IPv6静态路由保护ISIS路由ZXROSNG(config)#no ipv6 route-static vrf zte protect isis8. 去使能公网IPv6静态路由保护所有配置的其他协议路由ZXROSNG(config)#no ipv6 route-static protect all






相关命令 :

无 




## show ipv6 protocol routing 


show ipv6 protocol routing 




命令功能 :

该命令用与查看IPv6路由协议表的路由条目信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 protocol routing 
  {{[summary 
]|[vrf-summary 
 ＜vrf-name 
＞]}|[{[vrf 
 ＜vrf-name 
＞] [{[network 
 {＜ipv6-address 
＞|＜ipv6-address-mask 
＞}]|[＜protocol 
＞]}]}]} 







命令参数解释 :



参数|描述
---|---
summary|<作用>查看IPv6路由协议表的公网路由条目总数。
＜vrf-name＞|<作用> 查看指定VPN下的路由条目。<取值范围> VRF名称的取值长度为1-32字符。<默认值> 无
＜vrf-name＞|<作用> 查看指定VPN下的路由条目。<取值范围> VRF名称的取值长度为1-32字符。<默认值> 无
＜ipv6-address＞|<作用>指定要显示的路由的目的网络前缀，网段模糊匹配 <默认值>无
＜ipv6-address-mask＞|<作用>指定要显示的路由的目的网络前缀及掩码长度，精确匹配<取值范围>掩码长度取值范围0-128取值范围<默认值>无
＜protocol＞|<作用>指定具体的协议名，根据指定的协议名显示相应路由的信息；<取值范围>目前支持显示的协议类型有AFTR路由、BGP路由、直连和地址路由、DHCPv6路由、ISIS路由、OSPFv3路由、PPP路由、RIPng路由、stateful NAT64路由、stateless NAT64路由、静态路由、用户路由、VRRP路由等；<默认值>无








缺省 :

显示路由协议表中公网下的所有有效路由； 






使用说明 :

show ipv6 protocol routing [vrf <vrf-name>] + protocol命令显示指定vrf中指定协议类型的或者全部类型的路由缩略表。show ipv6 protocol routing [vrf <vrf-name>]+{network <X:X::X:X>/<0~128>| network <X:X::X:X >}命令带掩码长度时显示指定vrf中与指定目的网络号和掩码长度精确匹配的路由的详细信息，不带掩码长度时显示与指定目的网络号最长匹配的路由的详细信息。show ipv6 protocol routing [vrf <vrf-name>] database命令显示指定vrf中全部类型的路由缩略表。






范例 :

1. show ipv6 protocol routing显示公网下的所有有效路由：ZXROSNG(config)#show ipv6 protocol routingIPv6 Routing TableCodes: D - Direct, A - Address, S - Static, R - RIP, UI - USER_IPADDR,       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS static,       O - OSPF intra, OI - OSPF inter, E1 - OSPF ext 1, E2 - OSPF ext 2,       N - ND, B - BGP, IB - IBGP, EB - EBGP, AG - BGP AGG, V - VRRP, P - PPP,       D6 - DHCPv6, SFN - Stateful NAT64, SLN - Stateless NAT64, AF - AFTR,       NP - ND_PREFIX, NF - ND_DFROUTE, NH - ND_HOST, SP - SPECIAL,       PSB - PS_BUSI_ADDR, PSU - PS_USER_ADDR, UN - USER_NETWORK,       US - USER_SPECIAL, BP - BRAS pool, ZL - ZENIC local,       DL - dynamic-leased-line, OL-OSPF local, IL-ISIS localTime: The time of last modified!S   10::/60 [1/0]via 100::2, loopback1, 0h8m56sS   20::/56 [1/0]via ::, loopback1, 0h10m23sS   30::/56 [1/0]via 100::3, loopback1, 0h11m22sS   30::/56 [1/0]via 100::6, loopback1, 0h14m19sD   100::/56via ::, loopback1, 0h6m46sA   100::1/128via ::, loopback1, 0h6m46s2. show ipv6 protocol routing static显示公网中的静态路由：ZXROSNG(config)#show ipv6 protocol routing staticIPv6 Routing TableCodes: D - Direct, A - Address, S - Static, R - RIP, UI - USER_IPADDR,       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS static,       O - OSPF intra, OI - OSPF inter, E1 - OSPF ext 1, E2 - OSPF ext 2,       N - ND, B - BGP, IB - IBGP, EB - EBGP, AG - BGP AGG, V - VRRP, P - PPP,       D6 - DHCPv6, SFN - Stateful NAT64, SLN - Stateless NAT64, AF - AFTR,       NP - ND_PREFIX, NF - ND_DFROUTE, NH - ND_HOST, SP - SPECIAL,       PSB - PS_BUSI_ADDR, PSU - PS_USER_ADDR, UN - USER_NETWORK,       US - USER_SPECIAL, BP - BRAS pool, ZL - ZENIC local,       DL - dynamic-leased-line, OL-OSPF local, IL-ISIS local       M - Multicast        * - FIB route       > - selected route, p - stale infoTime: The time of last modified!S> 10::/60 [1/0]*  via 100::2, loopback1,[out label:-1 in label:-1], 0h8m59sS> 20::/56 [1/0]*  via ::, loopback1,[out label:-1 in label:-1], 0h10m26sS> 30::/56 [1/0]*  via 100::3, loopback1,[out label:-1 in label:-1], 0h11m25sS> 30::/56 [1/0]*  via 100::6, loopback1,[out label:-1 in label:-1], 0h14m22s3. show ipv6 protocol routing network 100::显示公网中100::网段的路由：ZXROSNG(config)#show ipv6 protocol routing network 100::IPv6 Routing TableCodes: D - Direct, A - Address, S - Static, R - RIP, UI - USER_IPADDR,       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS static,       O - OSPF intra, OI - OSPF inter, E1 - OSPF ext 1, E2 - OSPF ext 2,       N - ND, B - BGP, IB - IBGP, EB - EBGP, AG - BGP AGG, V - VRRP, P - PPP,       D6 - DHCPv6, SFN - Stateful NAT64, SLN - Stateless NAT64, AF - AFTR,       NP - ND_PREFIX, NF - ND_DFROUTE, NH - ND_HOST, SP - SPECIAL,       PSB - PS_BUSI_ADDR, PSU - PS_USER_ADDR, UN - USER_NETWORK,       US - USER_SPECIAL, BP - BRAS pool, ZL - ZENIC local,       DL - dynamic-leased-line, OL-OSPF local, IL-ISIS local       M - Multicast        * - FIB route       > - selected route, p - stale infoTime: The time of last modified!D> 100::/56*  via ::, loopback1,[out label:-1 in label:-1], 0h6m46sA> 100::1/128*  via ::, loopback1,[out label:-1 in label:-1], 0h6m46sZXROSNG(config)#
4. show ipv6 protocol routing network 100::/56 显示公网中100::/56网段的路由ZXROSNG(config)#show ipv6 protocol routing network 100::/56Routing entry for 100::/56Known via "connected", distance 0, metric 0, bestdirectly connected, loopback1  Last update at 0h43m16sZXROSNG(config)#
5. show ipv6 protocol routing vrf + zte 显示vrf名为zte的路由协议表中的路由条目；ZXROSNG(config)#show ipv6 protocol routing vrf zteVrf zte IPv6 Routing TableCodes: D - Direct, A - Address, S - Static, R - RIP, UI - USER_IPADDR,       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS static,       O - OSPF intra, OI - OSPF inter, E1 - OSPF ext 1, E2 - OSPF ext 2,       N - ND, B - BGP, IB - IBGP, EB - EBGP, AG - BGP AGG, V - VRRP, P - PPP,       D6 - DHCPv6, SFN - Stateful NAT64, SLN - Stateless NAT64, AF - AFTR,       NP - ND_PREFIX, NF - ND_DFROUTE, NH - ND_HOST, SP - SPECIAL,       PSB - PS_BUSI_ADDR, PSU - PS_USER_ADDR, UN - USER_NETWORK,       US - USER_SPECIAL, BP - BRAS pool, ZL - ZENIC local,       DL - dynamic-leased-line, OL-OSPF local, IL-ISIS localTime: The time of last modified!S   10::/90 [1/0]via 200::2, loopback2, 0h47m26sD   200::/56via ::, loopback2, 0h47m3sA   200::1/128via ::, loopback2, 0h47m3s6. show ipv6 protocol routing vrf zte static 显示vrf名为zte的路由协议表中静态路由条目；ZXROSNG(config)#show ipv6 protocol routing vrf zte staticVrf zte IPv6 Routing TableCodes: D - Direct, A - Address, S - Static, R - RIP, UI - USER_IPADDR,       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS static,       O - OSPF intra, OI - OSPF inter, E1 - OSPF ext 1, E2 - OSPF ext 2,       N - ND, B - BGP, IB - IBGP, EB - EBGP, AG - BGP AGG, V - VRRP, P - PPP,       D6 - DHCPv6, SFN - Stateful NAT64, SLN - Stateless NAT64, AF - AFTR,       NP - ND_PREFIX, NF - ND_DFROUTE, NH - ND_HOST, SP - SPECIAL,       PSB - PS_BUSI_ADDR, PSU - PS_USER_ADDR, UN - USER_NETWORK,       US - USER_SPECIAL, BP - BRAS pool, ZL - ZENIC local,       DL - dynamic-leased-line, OL-OSPF local, IL-ISIS local       M - Multicast        * - FIB route       > - selected route, p - stale infoTime: The time of last modified!S> 123::1/128 [1/0]*  via 600::3, loopback6, [out label:-1 in label:-1], 22h45m59sZXROSNG(config)#
7. show ipv6 protocol routing vrf  zte network 600:: 显示vrf名为zte的路由协议表中600::网段的路由条目；ZXROSNG(config)#show ipv6 protocol routing vrf zte network 600::Vrf zte IPv6 Routing TableCodes: D - Direct, A - Address, S - Static, R - RIP, UI - USER_IPADDR,       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS static,       O - OSPF intra, OI - OSPF inter, E1 - OSPF ext 1, E2 - OSPF ext 2,       N - ND, B - BGP, IB - IBGP, EB - EBGP, AG - BGP AGG, V - VRRP, P - PPP,       D6 - DHCPv6, SFN - Stateful NAT64, SLN - Stateless NAT64, AF - AFTR,       NP - ND_PREFIX, NF - ND_DFROUTE, NH - ND_HOST, SP - SPECIAL,       PSB - PS_BUSI_ADDR, PSU - PS_USER_ADDR, UN - USER_NETWORK,       US - USER_SPECIAL, BP - BRAS pool, ZL - ZENIC local,       DL - dynamic-leased-line, OL-OSPF local, IL-ISIS local       M - Multicast        * - FIB route       > - selected route, p - stale infoTime: The time of last modified!D> 600::/56*  via ::, loopback6, [out label:-1 in label:-1], 22h45m43sA> 600::1/128*  via ::, loopback6, [out label:-1 in label:-1], 22h45m43sZXROSNG(config)#
8. show ipv6 protocol routing vrf  zte  network 600::/56显示vrf名为zte的路由协议表中600::/56这条路由条目；ZXROSNG(config)#show ipv6 protocol routing vrf zte network 600::/56Routing entry for 600::/56Known via "connected", distance 0, metric 0, best* directly connected, loopback6  Last update at 22h45m46sZXROSNG(config)#
9. show ipv6 protocol routing summary显示公网下的所有有效路由的总数：ZXROSNG(config)#show ipv6 protocol routing summaryIPv6 Routing Table Summary - 0 entriesCONNECT    0STATIC     0RIP        0BGP        0IS-IS      0OSPF       0ICMP       0USER-ADDR  0VRRP       0PPP        0ND         0D6         0AF         0SFN        0SLN        0PSB         0PSU         0LDP         0UN          0US          0BRAS-POOL   0ZXROSNG(config)#
10. show ipv6 protocol routing vrf-summary com2显示vrf为com2的私网下的所有有效路由条目的总和：ZXROSNG(config)#show ipv6 protocol routing vrf-summary com2IPv6 Routing Table Summary - 2 entriesCONNECT    2STATIC     0RIP        0BGP        0IS-IS      0OSPF       0ICMP       0USER-ADDR  0VRRP       0PPP        0ND         0D6         0AF         0SFN        0SLN        0PSB         0PSU         0LDP         0UN          0US          0BRAS-POOL   0ZXROSNG(config)#






相关命令 :

无 




# IPv6隧道配置命令 
## debug ipv6-tunnel interface 


debug ipv6-tunnel interface 




命令功能 :

打开指定V6隧道的debug报文打印开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6-tunnel interface 
  ＜interface-name 
＞
no debug ipv6-tunnel interface 
  ＜interface-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|已创建的ipv6_tunnel接口








缺省 :

默认关闭该打印功能。 






使用说明 :

接口名必须是已经创建的V6隧道接口，否则会提示命令错误 






范例 :

ZXROSNG#debug ipv6-tunnel interface v6_tunnel1IPv6 tunnel interface debugging is onZXROSNG#no debug ipv6-tunnel interface v6_tunnel1IPv6 tunnel interface debugging is off





相关命令 :

terminal monitordebug ipv6-tunnelno debug ipv6-tunnel



## debug ipv6-tunnel 


debug ipv6-tunnel 




命令功能 :

该命令工作于特权模式，用于开启IPv6隧道的报文封装与解封装打印开关。该命令用于调试IPv6隧道，检查IPv6隧道的封装与解封装流程。用户开启该开关后，可以查看所有IPv6隧道的报文封装与解封装信息，从而可以根据这些信息检查隧道的封装与解封装流程是否正确。





命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6-tunnel 
 

no debug ipv6-tunnel 








命令参数解释 :


					无
				 






缺省 :

关闭该调试功能 






使用说明 :

该命令需要伴随terminal monitor命令使用（参见命令terminal monitor），否则用户看不到隧道的封装与解封装打印信息。该打印开关状态可以通过命令show debug ipv6-tunnel查看（参见命令show debug ipv6-tunnel）。该命令开关默认为关闭，即默认不打印隧道封装与解封装信息。该命令开关打开后，会打印所有IPv6隧道中报文的封装与解封装信息。





范例 :

ZXROSNG#terminal monitorZXROSNG#debug ipv6-tunnel IPv6 tunnel debugging is onZXROSNG#no debug ipv6-tunnel IPv6 tunnel debugging is off在用户开启debug ipv6-tunnel开关后，如果有报文进出IPv6隧道，可看到IPv6隧道报文封装与解封装信息：v6_tunnel1: IPv6/IP packet to be encapsulated: 6:1::1-->6:1::2 (len=100 ttl=64) ZXR10 MPU-0/20/0 2014-7-1 19:20:04 v6_tunnel1: IPv6/IP packet encapsulated: 11.1.1.1-->11.1.1.2 (len=120 ttl=255) ZXR10 MPU-0/20/0 2014-7-1 19:20:05 v6_tunnel1: IPv6/IP packet to be decapsulated: 11.1.1.2-->11.1.1.1 (len=120 ttl=255) ZXR10 MPU-0/20/0 2014-7-1 19:20:05 v6_tunnel1: IPv6/IP packet decapsulated: 6:1::2-->6:1::1 (len=100 ttl=64) 





相关命令 :

terminal monitor    show debug ipv6-tunnel



interface :

interface (IPv6隧道模式) 




命令功能 :

该命令工作于IPv6隧道配置模式，用于进入特定隧道的IPv6隧道接口业务配置模式。执行成功后，可以在IPv6隧道接口业务配置模式下对该隧道进行配置。 






命令模式 :

 IPv6隧道模式  






命令默认权限级别 :

15 






命令格式 :



interface 
  {byname 
 ＜interface-byname 
＞|＜interface-name 
＞}







命令参数解释 :



参数|描述
---|---
＜interface-byname＞|用于标识IPv6隧道的接口别名。取值范围：1-32位的字符串。默认值：无。
＜interface-name＞|用于标识IPv6隧道的接口名称。取值范围：1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

执行该命令前，需要提前创建相应的IPv6隧道接口（参见全局配置模式下的配置命令interface），如果需要用到接口别名，需要在创建的IPv6隧道接口中创建接口别名。可以通过show ip interface brief命令查询已经存在的IPv6隧道接口。进入IPv6隧道接口业务配置模式后，拥有管理员权限的操作员可以对隧道的模式，源地址和目的地址等信息进行配置，详细操作请参考隧道接口业务配置模式下的命令。





范例 :

ZXROSNG#configure terminal ZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#byname tunnel1ZXROSNG(config-if-v6_tunnel1)#!ZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#exitZXROSNG(config-ipv6-tunnel)#interface byname tunnel1 ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#





相关命令 :

ipv6-tunnel-config  




## ipv6-tunnel-config 


ipv6-tunnel-config 




命令功能 :

该命令工作于全局配置模式，用于进入IPv6隧道配置模式。隧道是一种封装技术，它利用一种网络协议来传输另一种网络协议，即利用一种网络传输协议，将其他协议产生的数据报文封装在它自己的报文中，然后在网络中传输。IPv6隧道分为以下两种：IPv6 over IPv4隧道机制是将IPv6数据报文前封装上IPv4的报文头，通过隧道（Tunnel）使IPv6报文穿越IPv4网络，实现隔离的IPv6网络的互通, 另一种IPv4或IPv6 over IPv6隧道协议是对IPv4或者IPv6的数据报进行封装，使这些被封装的数据报能够在另一个IPv6网络中传输。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ipv6-tunnel-config 
 






命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

拥有管理员权限的操作员通过该命令进入IPv6隧道配置模式，之后才可以指定隧道接口名进入IPv6隧道接口业务配置模式。 






范例 :

ZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#该模式下可通过指定隧道接口进入IPv6隧道接口配置模式，如下所示：ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#





相关命令 :

configure terminalinterface v6_tunnel<tunnel no>



## show debug ipv6-tunnel 


show debug ipv6-tunnel 




命令功能 :

该命令工作于任意模式下，用于查看IPv6隧道debug开关是否开启。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug ipv6-tunnel 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于帮助用户查看IPv6隧道的debug开关开启情况，在debug ipv6-tunnel开关默认关闭的情况下，执行该show命令后没有debug开关关闭的回显信息，只有在debug ipv6-tunnel开关开启时，才会有相应的回显信息。 






范例 :

ZXROSNG#show debug ipv6-tunnel ZXROSNG#ZXROSNG#debug ipv6-tunnel IPv6 tunnel debugging is onZXROSNG#show debug ipv6-tunnel IPv6 TUNNEL:  IPv6 tunnel packets debugging is on当用户执行show debug ipv6-tunnel命令后有回显提示IPv6 tunnel packets debugging is on，说明GRE隧道的debug调试开关处于开启状态，否则处于关闭状态。





相关命令 :

debug ipv6-tunnelterminal monitor



## tunnel 6rd-ipv4-mask-length 


tunnel 6rd-ipv4-mask-length 




命令功能 :

该命令工作于IPv6隧道接口业务模式，用于配置6RD隧道的IPv4掩码长度。6RD隧道是动态隧道，目的地址需要从报文中获取。这个命令就是计算隧道目的地址的重要依据之一。 






命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :



tunnel 6rd-ipv4-mask-length 
  ＜length 
＞

no tunnel 6rd-ipv4-mask-length 








命令参数解释 :



参数|描述
---|---
＜length＞|用于为隧道设置的6RD前缀取值范围：为6RD隧道配置IPv4掩码长度,范围为0~32默认值：未配置








缺省 :

未配置6RD的IPv4掩码长度 






使用说明 :

在未配置时6RD隧道是无法正常工作的。配置这个命令需要先配置tunnel mode ipv6ip 6rd，这个命令只是专为6RD隧道设置的，其它隧道无法使用；用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG#configure terminalZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#exitZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel mode ipv6ip 6rdZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel 6rd-ipv4-mask-length 0ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel 6rd-ipv4-mask-length





相关命令 :

interface v6_tunnel<tunnel no>ipv6-tunnel-configtunnel mode ipv6ip 6rd



## tunnel 6rd-prefix 


tunnel 6rd-prefix 




命令功能 :

该命令工作于IPv6隧道接口业务模式，用于配置6RD隧道的IPv6前缀，在没有配置6RD中继的情况下，只有目的地址与配置的前缀一致的报文才能通过6RD隧道。具体协议参考RFC5598, draft-ietf-softwire-ipv6-6rd-10等草案。





命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel 6rd-prefix 
  ＜ipv6-address-mask 
＞

no tunnel 6rd-prefix 








命令参数解释 :



参数|描述
---|---
＜ipv6-address-mask＞|用于为隧道设置的6RD前缀取值范围：为6RD隧道配置IPv6前缀，其中前缀长度的范围为0-128默认值：未配置








缺省 :

前缀未配置 






使用说明 :

在未配置时6RD隧道是无法正常工作的。配置这个命令需要先配置tunnel mode ipv6ip 6rd，这个命令只是专为6RD隧道设置的，其它隧道无法使用；用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG#configure terminalZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#exitZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel mode ipv6ip 6rdZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel 6rd-prefix 300::1/16ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel 6rd-prefix





相关命令 :

interface v6_tunnel<tunnel no>ipv6-tunnel-configtunnel mode ipv6ip 6rd




## tunnel destination dhcp-interface 


tunnel destination dhcp-interface 




命令功能 :

该命令工作于IPv6隧道接口业务模式，使用接口名为隧道配置目的地址。该命令实现功能与tunnel destination相同，不同的是tunnel destination命令直接为隧道指定源地址，而本命令是通过为隧道指定DHCP接口名称，通过从DHCP接口上获取AFTR地址。





命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel destination dhcp-interface 
  ＜interface-name 
＞

no tunnel destination dhcp-interface 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|用于设置隧道目的地址接口取值范围：1-32位的字符串。默认值：无。








缺省 :

隧道未配置目的地址 






使用说明 :

配置该命令前需要先通过tunnel mode命令配置隧道模式为ds-lite-b4。配置的接口必须是本地的物理接口或是通过interface命令创建的逻辑接口。命令与tunnel destination ipv6、tunnel destination domain配置冲突，不能同时配置。隧道从配置的DCHP接口中获取到目的地址后，该隧道的源地址，目的地址以及VRF三者不能与其他隧道完全一致，否则会导致配置错误。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#exitZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel mode ipipv6 ds-lite-b4ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel destination dhcp-interface gei-0/1/0/1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel destination dhcp-interface





相关命令 :

interface v6_tunnel<tunnel no>ipv6-tunnel-configtunnel mode ipipv6 ds-lite-b4



## tunnel destination domain 


tunnel destination domain 




命令功能 :

该命令工作于IPv6隧道接口业务模式，使用域名为隧道配置目的地址。该命令实现功能与tunnel destination相同，不同的是tunnel destination命令直接为隧道指定源地址，而本命令是通过为隧道指定域名获取目的地址。





命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel destination domain 
  ＜domain-name 
＞

no tunnel destination domain 








命令参数解释 :



参数|描述
---|---
＜domain-name＞|用于设置隧道目的域名取值范围：1-128位的字符串。默认值：无。








缺省 :

隧道未配置目的域名 






使用说明 :

配置该命令前需要先通过tunnel mode命令配置隧道模式为ds-lite-b4。该命令与tunnel destination ipv6、tunnel destination dhcp-interface配置冲突，不能同时配置。隧道从配置的域名中获取到目的地址后，该隧道的源地址，目的地址以及VRF三者不能与其他隧道完全一致，否则会导致配置错误。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#exitZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel mode ipipv6 ds-lite-b4ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel destination domain www.zte.comZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel destination domain





相关命令 :

interface v6_tunnel<tunnel no>ipv6-tunnel-configtunnel mode ipipv6 ds-lite-b4



## tunnel destination 


tunnel destination 




命令功能 :

该命令工作于IPv6隧道接口业务配置模式，用于为隧道配置目的地址。用户使用该命令为隧道指定隧道目的地址后，在隧道对报文进行封装时，隧道会将该地址作为封装后的IPv4或IPv6报文的目的地址。





命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel destination 
  {ipv4 
 ＜ipv4-address 
＞|ipv6 
 ＜ipv6-address 
＞}

no tunnel destination 








命令参数解释 :



参数|描述
---|---
ipv4|隧道封装模式为ipv6ip，外层为IPv4报文，目的地址为一个IPv4类型的地址，内层为IPv6报文，隧道为ipv6 over ipv4隧道
＜ipv4-address＞|用于设置隧道的末端ip地址。取值范围：合法ipv4地址。默认值：无。
ipv6|隧道封装模式为ipipv6，外层为IPv6报文，目的地址为一个IPv6类型的地址，内层为IPv4报文，隧道为ipv4 over ipv6隧道
＜ipv6-address＞|用于设置隧道的ipv6地址。取值范围：合法ipv6地址。默认值：无。








缺省 :

隧道未配置目的地址 






使用说明 :

隧道目的地址配置支持IPv4和IPv6两种类型。通过本命令配置的目的地址类型必须与通过tunnel mode命令配置的隧道模式相同，即当隧道模式为ip时，只能配置IPv4类型的目的地址，否则会有错误提示，隧道模式为ipv6时，只能配置IPv6类型的目的地址。不同隧道的基本信息配置不能冲突，即通过tunnel source命令配置的源地址、通过tunnel destination命令配置的目的地址以及通过tunnel vrf命令配置的VRF，不同的隧道对应的这三个配置不能完全一致，否则会有隧道冲突。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG(config)#ZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel mode ipv6ip 6in4ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel destination ipv4 1.1.1.2ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel destination ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#





相关命令 :

interface v6_tunnel<tunnel no>ipv6-tunnel-configtunnel mode



## tunnel dscp 


tunnel dscp 




命令功能 :

该命令工作于IPv6隧道接口业务模式，用于启用IPv6隧道DSCP（Differentiated Services Codepoint）设置的功能。DSCP由RFC2474定义，它重新命名了IPv4报头中TOS使用的1字节和IPv6报头中数据类（Traffic Class）1字节，新的名字称为DS字段（Differentiated Services Field）。该字段的作用没有变，仍然被QoS工具用来标记数据。不同的是IPP使用3比特，而DSCP使用6比特，最低2比特不用。RFC2474 定义最高3比特为级别／类别选择代码（ClassSelector Codepoints，CS），其意义和IPv4报头中IP优先级的定义是相同的，CS0 ～CS7的级别相等于IP优先级0 ～7。但它并没有定义第3到第5比特的具体含义以及使用规则。DSCP使用6比特，可以定义64个优先级（0－63）。





命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel dscp 
  ＜dscp 
＞

no tunnel dscp 








命令参数解释 :



参数|描述
---|---
＜dscp＞|用于为隧道设置的dscp选项值取值范围：0-63的数字串默认值：未配置








缺省 :

隧道未配置dscp，发包时优先级从内层继承 






使用说明 :

在未配置隧道DSCP优先级时，隧道封装时默认从内层IP/IPv6头中继承DSCP值； 未配置时，对于IPv6隧道，如果内层为isis封装报文，则不做继承；配置以后以配置值封装外层IP/IPv6报文的DSCP优先级，否则从内层继承IPP/DSCP/EXP优先级；





范例 :

ZXROSNG#configure terminalZXROSNG#configure terminalZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#exitZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel dscp 60ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel dscp





相关命令 :

interface v6_tunnel<tunnel num>ipv6-tunnel-config 



## tunnel mode 


tunnel mode 




命令功能 :

该命令工作于IPv6隧道接口业务配置模式，用于配置当前隧道的模式。隧道的封装模式主要分为IPv6IP以及IPIPv6两种。前者表示外层封装IPv6报文并在IPv4网络中传输，后者表示外层封装IPv4报文并在IPv6网络中传输。





命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel mode 
  {ipipv6 
 {4in6 
|ds-lite 
 {dynamic 
|static 
}|ds-lite-b4 
}|ipv6ip 
 {6to4 
|6rd 
|isatap 
|6in4 
}}

no tunnel mode 








命令参数解释 :



参数|描述
---|---
4in6|隧道模式的一种，IPv4 over IPv6隧道模式
dynamic|隧道模式的一种，动态DS Lite隧道模式， 该命令在当前网元中不支持
static|隧道模式的一种，静态DS Lite隧道模式
ds-lite-b4|隧道模式的一种，允许使用域名或者接口名称指定隧道的目的地址。
6to4|隧道模式的一种，是点到多点的自动隧道，使用特殊的6to4地址。
6rd|隧道模式的一种，是点到多点的自动隧道，没有特殊地址类型的限制，可以看作是6to4隧道的扩展
isatap|隧道模式的一种，是点到多点的自动隧道，使用特殊的EUI-64地址。
6in4|隧道模式的一种，IPv6 over IPv4隧道模式








缺省 :

隧道模式未配置 






使用说明 :

用户在配置该命令前，如果隧道已经有源、目的地址等配置，该隧道模式的配置需要与源目的地址的类型相匹配，即如果隧道源目的地址配置为IPv4类型，隧道模式应该为IPv6IP，否则会有配置错误信息提示。该隧道模式的变更或取消时，会清除隧道的其它配置。例如隧道接口配置有源地址时，使用tunnel mode命令变更隧道模式或执行no tunnel mode命令会清除隧道原有的源地址配置信息。





范例 :

ZXROSNG(config)#ZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel mode ipv6ip 6in4ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel modeZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#





相关命令 :

interface v6_tunnel<tunnel no>ipv6-tunnel-config



## tunnel source 


tunnel source 




命令功能 :

该命令工作于IPv6隧道接口业务配置模式，用于为隧道配置源地址。用户使用该命令为隧道指定隧道源地址后，在隧道对报文进行封装时，隧道会将该地址作为封装后的IPv4报文或IPv6报文的源地址。





命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel source 
  {ipv4 
 ＜ipv4-address 
＞|ipv6 
 ＜ipv6-address 
＞}

no tunnel source 








命令参数解释 :



参数|描述
---|---
ipv4|和隧道源地址类型ipv6二选一，如果承载网络为IPv4 Internet，则需要选择该源地址类型
＜ipv4-address＞|用于为隧道接口绑定本地接口IPv4地址。取值范围：合法IPv4地址。默认值：无。
ipv6|和隧道源地址类型ipv4二选一，如果承载网络为IPv6 Internet，则需要选择该源地址类型
＜ipv6-address＞|用于为隧道接口绑定本地接口IPv6地址。取值范围：合法IPv6地址。默认值：无。








缺省 :

隧道未配置源地址 






使用说明 :

隧道源地址配置支持ipv4和ipv6两种模式，通过本命令配置的源地址类型必须与通过tunnel mode命令配置的隧道模式相同，即当隧道模式为ipv6ip时，只能配置IPv4类型的源地址，否则会有错误提示，隧道模式为ipipv6时，只能配置IPv6类型的源地址。不同隧道的基本信息配置不能重复，即通过tunnel source命令配置的源地址、通过tunnel destination命令配置的目的地址以及通过tunnel vrf命令配置的VRF，不同的隧道对应的这三个配置不能完全一致，否则会有隧道冲突。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG(config)#ZXROSNG(config)#ipv6-tunnel-config ZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel mode ipv6ip 6in4ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel source ipv4 1.1.1.1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel source ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#





相关命令 :

interface v6_tunnel<tunnel no>ipv6-tunnel-configtunnel mode



## tunnel vrf 


tunnel vrf 




命令功能 :

该命令工作于IPv6隧道接口业务模式，用于指定隧道绑定的VRF名称。本命令用于支持IPv6隧道私网配置，实现IPv6隧道对报文封装后的私网传输。当用户需要IPv6隧道封装后的报文进入私网传输时，使用此命令。





命令模式 :

 IPv6隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel vrf 
  ＜vrf 
＞

no tunnel vrf 








命令参数解释 :



参数|描述
---|---
＜vrf＞|用于指定隧道绑定的VRF名称取值范围：1-32位的字符串。默认值：无。








缺省 :

IPv6隧道不配置外层vpn 






使用说明 :

该命令配置的VRF值必须是先前通过ip vrf命令配置的vrf-name值。相关的VRF信息可以通过命令show ip vrf来查看。配置tunnel vrf时，与该隧道模式对应的该VRF的协议类型必须使能（参见ip vrf配置命令），即如果该隧道模式为ip，则该命令使用的VRF必须支持IPv4协议，而如果隧道模式为ipv6，则该命令使用的VRF必须支持IPv6协议，否则会发生配置错误。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#!ZXROSNG(config)#ipv6-tunnel-configZXROSNG(config-ipv6-tunnel)#interface v6_tunnel1ZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#tunnel vrf zteZXROSNG(config-ipv6-tunnel-if-v6_tunnel1)#no tunnel vrf





相关命令 :

interface v6_tunnelipv6-tunnel-config




# IPv6组播配置命令 
## accept-register 


accept-register 




命令功能 :

配置对接收到的register报文中封装的组播数据报文进行过滤，使用no命令取消过滤。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



accept-register 
  ＜access-list-name 
＞

no accept-register 








命令参数解释 :



参数|描述
---|---
＜access-list-name＞|定义了一个地址范围，该范围是对register报文中封装的组播数据报文的源地址和组地址进行过滤








缺省 :

不对register报文中封装的组播数据报文进行过滤。 






使用说明 :

根据ACL访问表中定义的规则，对register报文中封装的组播数据报文的源地址和组地址进行过滤。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#accept-register zte






相关命令 :

无 




## accept-register 


accept-register 




命令功能 :

配置对接收到的register报文中封装的组播数据报文进行过滤，使用no命令取消过滤。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



accept-register 
  ＜access-list-name 
＞

no accept-register 








命令参数解释 :



参数|描述
---|---
＜access-list-name＞|定义了一个地址范围，该范围是对register报文中封装的组播数据报文的源地址和组地址进行过滤








缺省 :

不对register报文中封装的组播数据报文进行过滤。 






使用说明 :

根据ACL访问表中定义的规则，对register报文中封装的组播数据报文的源地址和组地址进行过滤。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#accept-register zte






相关命令 :

无 




## accept-rp 


accept-rp 




命令功能 :

对BSR消息中通告的候选RP地址进行过滤，使用no命令取消过滤。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



accept-rp 
  ＜access-list-name 
＞

no accept-rp 








命令参数解释 :



参数|描述
---|---
＜access-list-name＞|定义了一个地址范围，该范围是对接收的BSR消息中通告的候选RP进行过滤








缺省 :

不对BSR消息中通告的候选RP地址进行过滤。 






使用说明 :

如果本路由器不是BSR，则根据ACL访问表中定义的规则对接收的BSR消息中通告的候选RP进行过滤，符合规则的添入本地RP集，不符合规则的忽略。如果本路由器是BSR，则根据ACL访问表中定义的规则对发送的BSR消息中通告的候选RP进行过滤，符合规则添入报文通告，不符合规则的忽略。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#accept-rp zte






相关命令 :

show ipv6 pim rp mapping：显示所有的RP集信息。 




## accept-rp 


accept-rp 




命令功能 :

对BSR消息中通告的候选RP地址进行过滤，使用no命令取消过滤。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



accept-rp 
  ＜access-list-name 
＞

no accept-rp 








命令参数解释 :



参数|描述
---|---
＜access-list-name＞|定义了一个地址范围，该范围是对接收的BSR消息中通告的候选RP进行过滤








缺省 :

不对BSR消息中通告的候选RP地址进行过滤。 






使用说明 :

如果本路由器不是BSR，则根据ACL访问表中定义的规则对接收的BSR消息中通告的候选RP进行过滤，符合规则的添入本地RP集，不符合规则的忽略。如果本路由器是BSR，则根据ACL访问表中定义的规则对发送的BSR消息中通告的候选RP进行过滤，符合规则添入报文通告，不符合规则的忽略。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#accept-rp zte





相关命令 :

show ipv6 pim rp mapping：显示所有的RP集信息。 




## access-group 


access-group 




命令功能 :

限制接口上主机的组播组加入请求，使用no命令取消限制。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






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

缺省没有MLD加入组限制。 






使用说明 :

该命令只对动态加入的组有效，对配置的静态组无效。 






范例 :

配置允许MLD加入的组范围：ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#access-group zte





相关命令 :

无 




## access-group 


access-group 




命令功能 :

限制接口上主机的组播组加入请求，使用no命令取消限制。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






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

缺省没有MLD加入组限制。 






使用说明 :

该命令只对动态加入的组有效，对配置的静态组无效。 






范例 :

配置允许MLD加入的组范围：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#access-group zte





相关命令 :

无 




## anycast-rp-local 


anycast-rp-local 




命令功能 :

配置Anycast-RP本端地址，用于转发注册报文。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



anycast-rp-local 
  ＜ipv6-address 
＞

no anycast-rp-local 








命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|Anycast-RP本端地址，为X:X::X:X形式








缺省 :

没有配置anycast-rp-local。 






使用说明 :

如果RP接收到来自与源直连的DR的注册报文，且此RP配置anycast-rp-local命令，则可以将收到的注册报文转发给其他RP。 






范例 :

配置Anycast-RP本端地址为2::2：ZXROSNG(config-mcast-ipv6-pim)#anycast-rp-local 2::2






相关命令 :

anycast-rp-peer：配置接收注册报文的对端地址。 




## anycast-rp-local 


anycast-rp-local 




命令功能 :

配置Anycast-RP本端地址，用于转发注册报文。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



anycast-rp-local 
  ＜ipv6-address 
＞

no anycast-rp-local 








命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|Anycast-RP本端地址，为X:X::X:X形式








缺省 :

没有配置anycast-rp-local。 






使用说明 :

如果RP接收到来自与源直连的DR的注册报文，且此RP配置anycast-rp-local命令，则可以将收到的注册报文转发给其他RP。 






范例 :

配置Anycast-RP本端地址为2::2：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#anycast-rp-local 2::2






相关命令 :

anycast-rp-peer：配置接收注册报文的对端地址。 




## anycast-rp-peer 


anycast-rp-peer 




命令功能 :

配置Anycast-RP对端地址，用于接收注册报文。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :


anycast-rp-peer 
  ＜ipv6-address 
＞
no anycast-rp-peer 
  ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|anycast-rp对端地址，为X:X::X:X形式








缺省 :

没有配置anycast-rp-peer。 






使用说明 :

如果RP接收到来自与源直连的DR的注册报文，且此RP配置anycast-rp-peer命令，其他RP则可以收到注册报文。 






范例 :

配置Anycast-RP对端接口地址为2::2：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#anycast-rp-peer 2::2






相关命令 :

anycast-rp-local：配置本端RP转发注册报文的地址。 




## anycast-rp-peer 


anycast-rp-peer 




命令功能 :

配置Anycast-RP对端地址，用于接收注册报文。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :


anycast-rp-peer 
  ＜ipv6-address 
＞
no anycast-rp-peer 
  ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|anycast-rp对端地址，为X:X::X:X形式








缺省 :

没有配置anycast-rp-peer。 






使用说明 :

如果RP接收到来自与源直连的DR的注册报文，且此RP配置anycast-rp-peer命令，其他RP则可以收到注册报文。 






范例 :

配置Anycast-RP对端接口地址为2::2：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#anycast-rp-peer 2::2






相关命令 :

anycast-rp-local：配置本端RP转发注册报文的地址。 




## assert-disable 


assert-disable 




命令功能 :

在接口上取消IPv6 PIM assert功能。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



assert-disable 
 

no assert-disable 








命令参数解释 :


					无
				 






缺省 :

接口上有IPv6 PIM assert功能。 






使用说明 :

在多路访问网络中,使用断言assert机制来选举唯一的转发者以防向同一网段重复转发组播数据包。默认接口上是有IPv6 PIM assert功能的，如果配置了assert-disable则取消此功能。 






范例 :

在接口gei-0/1/0/1上取消assert功能：ZXROSNG(config)#ipv6 multicastZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)# interface gei-0/1/0/1 ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#assert-disable





相关命令 :

pimsmpimdm




## assert-disable 


assert-disable 




命令功能 :

在接口上取消IPv6 PIM assert功能。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



assert-disable 
 

no assert-disable 








命令参数解释 :


					无
				 






缺省 :

接口上有IPv6 PIM assert功能。 






使用说明 :

在多路访问网络中,使用断言assert机制来选举唯一的转发者以防向同一网段重复转发组播数据包。默认接口上是有IPv6 PIM assert功能的，如果配置了assert-disable则取消此功能。 






范例 :

在接口gei-0/1/0/1上取消assert功能：ZXROSNG(config)#ipv6 multicastZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#assert-disable





相关命令 :

pimsmpimdm




## assert-holdtime 


assert-holdtime 




命令功能 :

配置assert状态保持时间。使用no命令恢复默认值。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

配置assert-holdtime为200秒：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#assert-holdtime 200






相关命令 :

router pim：使能PIM。 




## assert-holdtime 


assert-holdtime 




命令功能 :

配置assert状态保持时间。使用no命令恢复默认值。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

配置assert-holdtime为200秒：ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pim ZXROSNG(config-mcast-ipv6-pim)# assert-holdtime 200





相关命令 :

router pim：使能PIM。 




## bfd-enable 


bfd-enable 




命令功能 :

在接口上启用BFD。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



bfd-enable 
 

no bfd-enable 








命令参数解释 :


					无
				 






缺省 :

接口不启用BFD。 






使用说明 :

该命令配置之前必须先使能IPv6 PIM-SM。





范例 :

配置在接口gei-0/1/0/1上启用BFD功能：ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#bfd-enable ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#!ZXROSNG(config)#show ipv6 pim bfd Interface: gei-0/1/0/1   State: CONNECT  BFD Local-Addr: fe80::2ee:ffff:fe10:2000(DR)  BFD Peer-Addr: fe80::2ee:ffff:fe10:1000(BDR) 






相关命令 :

show ipv6 pim bfd：显示配置BFD的接口信息。 




## bfd-enable 


bfd-enable 




命令功能 :

在接口上启用BFD。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



bfd-enable 
 

no bfd-enable 








命令参数解释 :


					无
				 






缺省 :

接口不启用BFD。 






使用说明 :

该命令配置之前必须先使能IPv6 PIM-SM。





范例 :

配置在接口gei-0/1/0/1上启用BFD功能：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#bfd-enable






相关命令 :

show ipv6 pim bfd：显示配置BFD的接口信息。 




## bsm-unicast 


bsm-unicast 




命令功能 :

配置单播发送BSR消息。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

配置单播发送BSR消息：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#bsm-unicast






相关命令 :

无 




## bsm-unicast 


bsm-unicast 




命令功能 :

配置单播发送BSR消息。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

配置单播发送BSR消息：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#bsm-unicast






相关命令 :

无 




## bsr-border 


bsr-border 




命令功能 :

配置接口使其成为PIM域边界，使用no命令删除配置。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



bsr-border 
 

no bsr-border 








命令参数解释 :


					无
				 






缺省 :

接口不配置为PIM域边界。 






使用说明 :

当在接口上配置该命令时，没有引导报文能在任一方向上通过该边界。该命令有效地将网络划分成使用不同引导报文的区域。其他PIM报文可以通过域边界。 






范例 :

在路由器接口gei-0/1/0/1上配置PIM域边界：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6-pim)# interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#bsr-border






相关命令 :

无 




## bsr-border 


bsr-border 




命令功能 :

配置接口使其成为PIM域边界，使用no命令删除配置。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



bsr-border 
 

no bsr-border 








命令参数解释 :


					无
				 






缺省 :

接口不配置为PIM域边界。 






使用说明 :

当在接口上配置该命令时，没有引导报文能在任一方向上通过该边界。该命令有效地将网络划分成使用不同引导报文的区域。其他PIM报文可以通过域边界。 






范例 :

在路由器接口gei-0/1/0/1上配置PIM域边界：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#bsr-border






相关命令 :

无 




## bsr-candidate 


bsr-candidate 




命令功能 :

配置路由器使其宣布作为引导路由器（BSR）的候选者，使用no命令取消该路由器作为引导路由器的候选者。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



bsr-candidate 
  ＜ipv6-address 
＞ [{[hash-mask-length 
 ＜hash-mask-length 
＞],[priority 
 ＜priority 
＞]}]

no bsr-candidate 








命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|接口的地址，为X:X::X:X形式
＜hash-mask-length＞|哈希掩码长度，范围：0–128，缺省为126
＜priority＞|候选BSR优先级，范围：0–255，缺省为0








缺省 :

本路由器不是候选BSR。 






使用说明 :

1.候选BSR的缺省优先级为0，具有较高优先级的候选BSR成为最终BSR；2.如果多个路由器的BSR优先级一样，则比较IP地址，具有最大地址的候选BSR成为最终BSR;3.推荐用户将候选BSR配置在loopback接口上，从而减少由于物理接口up/down造成的网络震荡。






范例 :

在IPv6地址为101::20的接口上配置候选BSR，哈希掩码长度为30，优先级为100：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#bsr-candidate 101::20 hash-mask-length 30 priority 100






相关命令 :

show ipv6 pim bsr：查看BSR配置信息。 




## bsr-candidate 


bsr-candidate 




命令功能 :

配置路由器使其宣布作为引导路由器（BSR）的候选者，使用no命令取消该路由器作为引导路由器的候选者。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



bsr-candidate 
  ＜ipv6-address 
＞ [{[hash-mask-length 
 ＜hash-mask-length 
＞],[priority 
 ＜priority 
＞]}]

no bsr-candidate 








命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|接口的地址，为X:X::X:X形式
＜hash-mask-length＞|哈希掩码长度，范围：0–128，缺省为126
＜priority＞|候选BSR优先级，范围：0–255，缺省为0








缺省 :

本路由器不是候选BSR。 






使用说明 :

1.候选BSR的缺省优先级为0，具有较高优先级的候选BSR成为最终BSR；2.如果多个路由器的BSR优先级一样，则比较IP地址，具有最大地址的候选BSR成为最终BSR;3.推荐用户将候选BSR配置在loopback接口上，从而减少由于物理接口up/down造成的网络震荡。






范例 :

在IPv6地址为101::20的接口上配置候选BSR，哈希掩码长度为30，优先级为100：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#bsr-candidate 101::20 hash-mask-length 30 priority 100






相关命令 :

show ipv6 pim bsr：查看BSR配置信息。 




## bsr-candidate-holdtime 


bsr-candidate-holdtime 




命令功能 :

设置C-BSR保持时间。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

设置C-BSR保持时间为200秒：ZXROSNG(config-mcast-ipv6-pim)#bsr-candidate-holdtime 200





相关命令 :

bsr-candidate-interval：设置BSM消息发送周期。 




## bsr-candidate-holdtime 


bsr-candidate-holdtime 




命令功能 :

设置C-BSR保持时间。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

设置C-BSR保持时间为200秒：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#bsr-candidate-holdtime 200






相关命令 :

bsr-candidate-interval：设置BSM消息发送周期。 




## bsr-candidate-interval 


bsr-candidate-interval 




命令功能 :

设置BSM消息发送周期。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

1．设置的BSM消息发送周期必须小于或等于C-BSR保持时间减去10s的时间的一半。2．设置的BSM消息发送周期必须小于或等于最小C-RP保持时间的2/5。





范例 :

设置BSM消息发送周期为80秒：ZXROSNG(config-mcast-ipv6-pim)#bsr-candidate-interval 80





相关命令 :

bsr-candidate-holdtime：设置C-BSR保持时间。 




## bsr-candidate-interval 


bsr-candidate-interval 




命令功能 :

设置BSM消息发送周期。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

1．设置的BSM消息发送周期必须小于或等于C-BSR保持时间减去10s的时间的一半。2．设置的BSM消息发送周期必须小于或等于最小C-RP保持时间的2/5。





范例 :

设置BSM消息发送周期为80秒：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#bsr-candidate-interval 80






相关命令 :

bsr-candidate-holdtime：设置C-BSR保持时间。 




## bsr-policy 


bsr-policy 




命令功能 :

IPv6 PIM对BSR地址过滤。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

不对IPv6 PIM BSR地址过滤。 






使用说明 :

如果本路由器不是BSR，则根据ACL访问表中定义的规则对接收的BSR消息中BSR地址进行过滤；如果本路由器是BSR，则根据ACL访问表中定义的规则对配置的BSR地址进行过滤。 






范例 :

用访问控制列表zte对BSR地址进行过滤：ZXROSNG(config)#ipv6-access-list zteZXROSNG(config-ipv6-acl)#rule permit ipv6 101::20/128 anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#bsr-policy zte






相关命令 :

无 




## bsr-policy 


bsr-policy 




命令功能 :

IPv6 PIM对BSR地址过滤。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

不对IPv6 PIM BSR地址过滤。 






使用说明 :

如果本路由器不是BSR，则根据ACL访问表中定义的规则对接收的BSR消息中BSR地址进行过滤；如果本路由器是BSR，则根据ACL访问表中定义的规则对配置的BSR地址进行过滤。 






范例 :

用访问控制列表zte对BSR地址进行过滤：ZXROSNG(config)#ipv6-access-list zteZXROSNG(config-ipv6-acl)#rule permit ipv6 101::20/128 anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#bsr-policy zte






相关命令 :

无 




## clear ipv6 mld groups 


clear ipv6 mld groups 




命令功能 :

删除动态加入的组播组。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear ipv6 mld groups 
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

1. 如果没有接口选项，则删除所有动态加入的组播组。2. 如果选择接口，则删除指定接口上所有动态加入的组播组。





范例 :

删除所有动态加入的组播组ZXROSNG#clear ipv6 mld groupsAre you sure to delete the MLD group entries? [yes/no]:yesZXROSNG#






相关命令 :

无 




## clear ipv6 mld packet-count 


clear ipv6 mld packet-count 




命令功能 :

清除MLD接收和发送的报文统计计数。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear ipv6 mld packet-count 
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

清除公网所有使能PIM协议的接口，MLD协议报文接收和发送统计计数：clear ipv6 mld packet-count；清除公网指定接口MLD协议报文接收和发送统计计数：clear ipv6 mld packet-count <interface-name>;清除私网所有使能PIM协议的接口接口MLD协议报文接收和发送统计计数：clear ipv6 mld packet-count <vrf-name>清除私网指定接口MLD协议报文接收和发送统计计数：clear ipv6 mld packet-count <vrf-name> <interface-name>





范例 :

清除MLD接收和发送的报文统计计数：ZXROSNG#clear ipv6 mld packet-countZXROSNG#show ipv6 mld packet-count MLD Packet Counts:Received/SentInterface:gei-0/1/0/1  Query:0/0  Done:0/0  ReportV1:0/0  ReportV2:0/0  Spec-Query:0/0  Grp-Src-Query:0/0  Dropped:0/0  Invalid:0/0  Total:0/0Total packets received in current MLD instance:  Query:0/0  Done:0/0  ReportV1:0/0  ReportV2:0/0  Spec-Query:0/0  Grp-Src-Query:0/0  Dropped:0/0  Invalid:0/0  Total:0/0Current Time:  2019-09-25 01:04:12ZXROSNG#






相关命令 :

无 




## clear ipv6 mroute 


clear ipv6 mroute 




命令功能 :

从IPv6组播路由表中删除记录。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear ipv6 mroute 
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
＜group-address＞|组地址 X:X::X:X 形式
＜source-address＞|源地址，X:X::X:X形式








缺省 :

无 






使用说明 :

1. 如果没有参数选项，则删除所有组播路由条目。2. 如果只选择组选项，则删除（*，g）和相关的所有（s，g）组播路由条目。3. 如果选择组和源地址选项，则删除相应的（s，g）组播路由条目。 4. 如果选择vrfname选项，则删除相应vrf的组播路由条目






范例 :

删除IPv6组播路由表记录：ZXROSNG#clear ipv6 mrouteAre you sure to delete the IPv6 multicast routing entries? [yes/no]:yesZXROSNG#






相关命令 :

show ipv6 mroute 




## clear ipv6 pim traffic 


clear ipv6 pim traffic 




命令功能 :

清零IPv6 PIM协议流量统计信息。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear ipv6 pim traffic 
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

1.删除具体哪个VRF实例下的IPv6 PIM流量统计信息，可采用<vrf-name>来指定，不指定则删除公网的；2.删除具体哪个IPv6 PIM接口的流量统计信息，可采用<interface-name>来指定，不指定则删除所有IPv6 PIM接口的流量统计信息。






范例 :

配置删除公网的IPv6 PIM协议流量统计信息。ZXROSNG#clear ipv6 pim trafficZXROSNG#show ipv6 pim trafficIPv6 PIM packet  Received   Sent       Filter     ErrorInterface: gei-0/1/0/1  Hello:         0          0          0          0  Join/Prune:    0          0          0          0  Register:      0          0          0          0  Register-Stop: 0          0          0          0  Bootstrap:     0          0          0          0  C-RP-Ad:       0          0          0          0  Assert:        0          0          0          0  State-Refresh: 0          0          0          0  Graft:         0          0          0          0  Graft-Ack:     0          0          0          0  Df-Election:   0          0          0          0Interface: loopback1  Hello:         0          0          0          0  Join/Prune:    0          0          0          0  Register:      0          0          0          0  Register-Stop: 0          0          0          0  Bootstrap:     0          0          0          0  C-RP-Ad:       0          0          0          0  Assert:        0          0          0          0  State-Refresh: 0          0          0          0  Graft:         0          0          0          0  Graft-Ack:     0          0          0          0  Df-Election:   0          0          0          0Total traffic in current PIM instance:  Total:         0          0          0          0  Hello:         0          0          0          0  Join/Prune:    0          0          0          0  Register:      0          0          0          0  Register-Stop: 0          0          0          0  Bootstrap:     0          0          0          0  C-RP-Ad:       0          0          0          0  Assert:        0          0          0          0  State-Refresh: 0          0          0          0  Graft:         0          0          0          0  Graft-Ack:     0          0          0          0  Df-Election:   0          0          0          0Current Time:  2018-06-29 21:47:27ZXROSNG#





相关命令 :

show ipv6 pim traffic：显示IPv6 PIM流量统计信息。 




## damping-enable 


damping-enable 




命令功能 :

配置组播震荡延迟功能，使用no命令取消配置。 






命令模式 :

 IPv6-组播模式  






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

1.使能组播防震荡功能。2.配置震荡阈值时，超过阈值将开启防震荡功能。3.最大等待时间是60秒，60秒后不管震荡次数多少，路由都会强制下发下去。





范例 :

配置使能组播防震荡功能。ZXROSNG(config-mcast-ipv6)#damping-enable






相关命令 :

damping-threshold 




## damping-threshold 


damping-threshold 




命令功能 :

配置组播震荡延迟功能，使用no命令取消配置。 






命令模式 :

 IPv6-组播模式  






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

震荡阈值默认为5。 






使用说明 :

1.使能组播防震荡功能。2.配置震荡阈值，超过阈值将开启防震荡功能。3.最大等待时间是60秒，60秒后不管震荡次数多少，路由都会强制下发下去。





范例 :

配置震荡阈值为3次，超过阈值将开启防震荡功能。ZXROSNG(config-mcast-ipv6)#damping-threshold 3






相关命令 :

damping-enable 




## data-filter 


data-filter 




命令功能 :

IPv6 PIM源数据过滤。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

不对IPv6 PIM源数据过滤。 






使用说明 :

根据ACL访问表中定义的规则，对组播数据报文的源地址和组地址进行过滤，与ACL规则不匹配的报文将丢弃。





范例 :

用访问控制列表zte对源数据进行过滤：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pim ZXROSNG(config-mcast-ipv6-pim)#data-filter zte






相关命令 :

无 




## data-filter 


data-filter 




命令功能 :

IPv6 PIM源数据过滤。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

不对IPv6 PIM源数据过滤。 






使用说明 :

根据ACL访问表中定义的规则，对组播数据报文的源地址和组地址进行过滤，与ACL规则不匹配的报文将丢弃。





范例 :

用访问控制列表zte对源数据进行过滤：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#data-filter zte






相关命令 :

无 




## debug ipv6 mld all 


debug ipv6 mld all 




命令功能 :

打开MLD协议相关的所有打印开关，使用no命令关闭开关后，不再输出信息。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 mld all 
 

no debug ipv6 mld all 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

打开MLD协议相关的所有打印开关 






范例 :

打开MLD协议相关的所有打印开关：ZXROSNG#debug ipv6 mld allAll MLD debugging has been turned on





相关命令 :

无 




## debug ipv6 mld 


debug ipv6 mld 




命令功能 :

打开MLD相关信息的调试开关，使用no命令关闭开关后，不再输出信息。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 mld 
  [vrf 
 ＜vrf-name 
＞] [{[＜group-address 
＞]|[＜interface-name 
＞]}]
no debug ipv6 mld 
  [vrf 
 ＜vrf-name 
＞] [{[＜group-address 
＞]|[＜interface-name 
＞]}]
				






命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜group-address＞|IPv6格式的组播组地址，X:X::X:X形式
＜interface-name＞|接口的名称








缺省 :

无 






使用说明 :

打开MLD相关信息的调试开关，可以分别针对实例、组以及接口名：debug ipv6 mld [vrf ＜vrf-name＞] [{[＜group-address＞]|[＜interface-name＞]}]





范例 :

打开MLD相关信息的打印开关：R1#debug ipv6 mldR1#debug ipv6 mld   MLD debugging is onR1#R1#terR1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#no join-group ff1e::100               R1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#no join-group ff1e::100 R1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#R1 MPU-0/20/0 2014-7-10 07:56:32  MLD : Delete group ff1e::100 on gei-0/1/0/1R1 MPU-0/20/0 2014-7-10 07:56:32  MLD : Send report for group(ff1e::100) type(TO_IN(3) : 0 src) on gei-0/1/0/1R1 MPU-0/20/0 2014-7-10 07:56:32  MLD : Send MLDv2 report on gei-0/1/0/1R1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#no static-group ff1e::200             R1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#R1 MPU-0/20/0 2014-7-10 07:57:01  MLD : Delete group ff1e::200 on gei-0/1/0/1R1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#R1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#R1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#R1 MPU-0/20/0 2014-7-10 07:57:04  MLD : Send MLDv2 general query on gei-0/1/0/1R1(config-mcast-ipv6-mld-if-gei-0/1/0/1)#R1 MPU-0/20/0 2014-7-10 08:03:40  MLD : Create group (ff1e::20) on gei-0/1/0/1R1 MPU-0/20/0 2014-7-10 08:03:40  MLD : Switch ff1e::20 to static group






相关命令 :

无 




## debug ipv6 mroute all 


debug ipv6 mroute all 




命令功能 :

打开mroute6相关的所有打印开关。使用no命令关闭mroute6相关的所有打印开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 mroute all 
 

no debug ipv6 mroute all 








命令参数解释 :


					无
				 






缺省 :

打印开关关闭 






使用说明 :

1.使用此命令前必须开启组播。2.此命令可以打开和关闭组播公网和私网的所有信息开关。






范例 :

打开mroute6相关的所有打印开关。ZXROSNG#debug ipv6 mroute allAll MROUTE6 debugging has been turned on






相关命令 :

show debug mroute6



## debug ipv6 mroute 


debug ipv6 mroute 




命令功能 :

设置mroute6相关信息的调试开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 mroute 
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
no debug ipv6 mroute 
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
data-info|设置mroute6整包数据信息的调试开关
data|设置mroute6数据信息的调试开关
packet-recv|设置mroute6接收报文信息的调试开关
packet-send|设置mroute6发送报文信息的调试开关
tlv-recv|设置mroute6接收TLV报文信息的调试开关
tlv-send|设置mroute6发送TLV报文信息的调试开关
mrt-recv|设置mroute6接收组播路由信息的调试开关
mrt-syn|设置mroute6同步组播路由信息的调试开关








缺省 :

打印开关关闭。 






使用说明 :

1.设置具体哪个VRF实例的mroute6信息的调试开关，可采用<vrf-name>来指定，如果没有<vrf-name>选项，则设置所有公网mroute信息的调试开关；2.如果增加配置选项，则相应设置相关mroute6信息的调试开关。3.使用此命令前必须先启用组播。





范例 :

设置mroute6相关信息的调试开关：ZXROSNG#debug ipv6 mroute   MROUTE6 debugging is on






相关命令 :

debug all mroute6：打开mroute6相关的所有打印开关 




## debug ipv6 mvpn all 


debug ipv6 mvpn all 




命令功能 :

打开IPv6 MVPN协议相关的所有打印开关，使用no命令关闭。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 mvpn all 
 

no debug ipv6 mvpn all 








命令参数解释 :


					无
				 






缺省 :

打印开关关闭 






使用说明 :

1.使用此命令前必须先启用组播和MVPN功能。2.此命令可以打开和关闭组播MVPN所有实例的信息开关。






范例 :

打开IPv6 MVPN协议相关的所有打印开关：ZXROSNG#debug ipv6 mvpn all     All IPv6 MVPN debugging has been turned onZXROSNG#no debug ipv6 mvpn allAll IPv6 MVPN debugging has been turned offZXROSNG#





相关命令 :

debug ipv6 mvpnshow debug ipv6-mvpn



## debug ipv6 mvpn 


debug ipv6 mvpn 




命令功能 :

打开IPv6 MVPN相关信息的调试开关，使用no命令关闭。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 mvpn 
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
no debug ipv6 mvpn 
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
＜vrf-name＞|实例名，长度1–32字符
rec-ad|设置rec-ad信息的调试开关
intra-ad|设置intra-ad信息的调试开关
inter-ad|设置inter-ad信息的调试开关
spmsi-ad|设置spmsi-ad信息的调试开关
leaf-ad|设置leaf-ad信息的调试开关
src-act|设置src-act信息的调试开关
sg-join|设置sg-join信息的调试开关
xg-join|设置xg-join信息的调试开关
event|设置evernt信息的调试开关
report|设置report信息的调试开关
nexthop|设置nexthop信息的调试开关
warning|设置warning信息的调试开关








缺省 :

打印开关关闭 






使用说明 :

1.使用此命令前必须先启用组播2.debug ipv6 mvpn all命令打开所有IPv6 MVPN信息的调试开关。3.debug ipv6 mvpn<命令参数>打开相应IPv6 MVPN信息的调试开关。no debug ipv6 mvpn<命令参数>关闭相应IPv6 MVPN信息的调试开关。4.设置具体哪个VRF实例的MVPN信息的调试开关，可采用<vrf-name>来指定，如果没有<vrf-name>选项，则设置所有实例的MVPN信息的调试开关；





范例 :

设置所有IPv6 MVPN信息的调试开关：ZXROSNG#debug ipv6 mvpn   IPv6 MVPN debugging is onZXROSNG#no debug ipv6 mvpn  IPv6 MVPN debugging is off 





相关命令 :

show debug ipv6-mvpndebug ipv6 mvpn all



## debug ipv6 pim all 


debug ipv6 pim all 




命令功能 :

打开IPv6 PIM协议相关的所有调试开关，使用no命令关闭。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 pim all 
 

no debug ipv6 pim all 








命令参数解释 :


					无
				 






缺省 :

默认情况下，debug打印开关是关闭的。 






使用说明 :

使用此命令前必须先启用IPv6组播和IPv6 PIM功能。 






范例 :

打开IPv6 PIM协议相关的所有调试开关。ZXROSNG#debug ipv6 pim allAll IPv6 PIM debugging has been turned onZXROSNG#show debug pim6IPv6 PIM:  IPv6 PIM debugging is onZXROSNG#





相关命令 :

show debug pim6：显示打开的IPv6 PIM调试开关。 




## debug ipv6 pim 


debug ipv6 pim 




命令功能 :

设置IPv6 PIM相关信息的调试开关，使用no命令关闭。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 pim 
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
＞]|bfd 
}]
no debug ipv6 pim 
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
＞]|bfd 
}]
				






命令参数解释 :



参数|描述
---|---
＜vrf-name＞|设置vrf实例信息的调试开关，VRF名称，长度为1–32个字符
bsr-rp|设置IPv6 PIM bsr和rp信息的调试开关
downstream-fsm|设置IPv6 PIM 下游状态机信息的调试开关
ast|设置IPv6 PIM assert信息的调试开关
register|设置IPv6 PIM 注册报文信息的调试开关
nbr|设置IPv6 PIM 邻居信息的调试开关
nhp|设置IPv6 PIM 下一跳信息的调试开关
mrt|设置IPv6 PIM 组播路由表信息的调试开关
packet-recv|设置IPv6 PIM 接收报文信息的调试开关
packet-send|设置IPv6 PIM 发送报文信息的调试开关
packet-dump|设置IPv6 PIM 报文字段详细信息及错误信息的调试开关
data-info|设置IPv6 PIM 数据信息的调试开关
local|设置本地加入信息的调试开关
＜group-address＞|组地址，设置过滤组后的IPv6 PIM 相关信息的调试开关
＜source-address＞|源地址，设置过滤源后的IPv6 PIM 相关信息的调试开关
bfd|设置IPv6 PIM bfd信息的调试开关








缺省 :

默认情况下，debug打印开关是关闭的。 






使用说明 :

1.设置具体哪个VRF实例的IPv6 PIM信息的调试开关，可采用<vrf-name>来指定，如果没有<vrf-name>选项，则设置所有公网IPv6 PIM信息的调试开关；2.如果增加其他选项，则相应设置相关IPv6 PIM信息的调试开关；3.使用此命令前必须先启用组播和IPv6 PIM功能。






范例 :

打开IPv6 PIM数据信息的调试开关。ZXROSNG#debug ipv6 pim data-info   IPv6 PIM packet data info debugging is on ZXROSNG#show debug pim6IPv6 PIM:  IPv6 PIM packet data info debugging is on





相关命令 :

show debug pim6：显示打开的IPv6 PIM调试开关。 




## dr-priority 


dr-priority 




命令功能 :

配置PIM接口DR优先级，使用no命令恢复缺省值。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






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

默认接口DR优先级为1。 






使用说明 :

1.在共享网段上对多个PIM路由器进行DR竞选时，首先比较DR优先级，优先级数值大者获胜；如果DR优先级一致，则比较接口地址，地址大者获胜。2.在连接组播数据源的共享网段上，只有DR能够向RP封装数据报文发送Register消息。3.在连接接收者的共享网段上，只有DR才能响应MLD加入、离开消息。






范例 :

在路由器接口gei-0/1/0/1上配置DR优先级：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6-pim)# interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#dr-priority 72






相关命令 :

show ipv6 pim interface：显示PIM6接口信息。 




## dr-priority 


dr-priority 




命令功能 :

配置PIM接口DR优先级，使用no命令恢复缺省值。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






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

默认接口DR优先级为1。 






使用说明 :

1.在共享网段上对多个PIM路由器进行DR竞选时，首先比较DR优先级，优先级数值大者获胜；如果DR优先级一致，则比较接口地址，地址大者获胜。2.在连接组播数据源的共享网段上，只有DR能够向RP封装数据报文发送Register消息。3.在连接接收者的共享网段上，只有DR才能响应MLD加入、离开消息。






范例 :

在路由器接口gei-0/1/0/1上配置DR优先级：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#dr-priority 72






相关命令 :

show ipv6 pim interface：显示PIM6接口信息。 




## dr-switchback-delay 


dr-switchback-delay 




命令功能 :

设置接口启用BFD时由DR变为非DR后重新计算路由的时间。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



dr-switchback-delay 
  ＜seconds 
＞

no dr-switchback-delay 








命令参数解释 :



参数|描述
---|---
＜seconds＞|设置接口启用BFD时由DR变为非DR后重新计算路由的时间，范围：1-300，单位：秒。








缺省 :

DR变化后立即计算路由。 






使用说明 :

设置接口启用BFD时由DR变为非DR后重新计算路由的时间，默认是立即计算。 






范例 :

设置接口启用BFD时由DR变为非DR后重新计算路由的时间为10秒：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#dr-switchback-delay 10






相关命令 :

bfd-enable：使能PIM BFD 




## dr-switchback-delay 


dr-switchback-delay 




命令功能 :

设置接口启用BFD时由DR变为非DR后重新计算路由的时间。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



dr-switchback-delay 
  ＜seconds 
＞

no dr-switchback-delay 








命令参数解释 :



参数|描述
---|---
＜seconds＞|设置接口启用BFD时由DR变为非DR后重新计算路由的时间，范围：1-300，单位：秒。








缺省 :

DR变化后立即计算路由。 






使用说明 :

设置接口启用BFD时由DR变为非DR后重新计算路由的时间，默认是立即计算。 






范例 :

设置接口启用BFD时由DR变为非DR后重新计算路由的时间为10秒：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#dr-switchback-delay 10






相关命令 :

bfd-enable：使能PIM BFD 




## embedded-rp disable 


embedded-rp disable 




命令功能 :

取消PIM协议指定嵌入式RP汇聚点功能。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



embedded-rp disable 
 

no embedded-rp disable 








命令参数解释 :


					无
				 






缺省 :

不取消PIM协议指定嵌入式RP汇聚点功能。 






使用说明 :

mld组加入组信息中默认可以嵌入RP信息，配置该命令取消此功能。 






范例 :

配置取消PIM协议指定嵌入式RP汇聚点功能。ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#embedded-rp disable 






相关命令 :

show ipv6 pim rp mapping embedded：显示嵌入式RP信息。 




## embedded-rp disable 


embedded-rp disable 




命令功能 :

取消PIM协议指定嵌入式RP汇聚点功能。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



embedded-rp disable 
 

no embedded-rp disable 








命令参数解释 :


					无
				 






缺省 :

不取消PIM协议指定嵌入式RP汇聚点功能。 






使用说明 :

mld组加入组信息中默认可以嵌入RP信息，配置该命令取消此功能。 






范例 :

配置取消PIM协议指定嵌入式RP汇聚点功能。ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#embedded-rp disable 






相关命令 :

show ipv6 pim rp mapping embedded：显示嵌入式RP信息。 




## error packet ipv6 pim record 


error packet ipv6 pim record 




命令功能 :

使能或去使能IPv6 PIM协议模块的错误报文记录功能。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



error packet ipv6 pim record 
  {disable 
|enable 
 [＜number 
＞]}







命令参数解释 :



参数|描述
---|---
disable|去使能IPv6 PIM协议模块的错误报文记录功能。
enable|使能IPv6 PIM协议模块的错误报文记录功能。
＜number＞|记录的错误报文个数，范围1-200，默认值是10。








缺省 :

默认为enable，记录最近10个错误报文。 






使用说明 :

1.disable时不清空已有记录缓存。2.收到的错误报文个数大于number时，新收到的错误报文覆盖最老的错误报文；3.number变小时，只保留最近收到的number个错误报文。






范例 :

1.使能IPv6 PIM协议模块的错误报文记录功能，并记录最近10个错误报文；ZXROSNG(config)#error packet ipv6 pim record enable 2.使能IPv6 PIM协议模块的错误报文记录功能，并记录最近200个错误报文；ZXROSNG(config)#error packet ipv6 pim record enable 2003.去使能IPv6 PIM协议模块的错误报文记录功能；ZXROSNG(config)#error packet ipv6 pim record disable 






相关命令 :

无 




## forwarding-policy 


forwarding-policy 




命令功能 :

配置IPv6组播转发策略。使用no命令取消配置。 






命令模式 :

 IPv6-组播模式,MULTICAST6-VRF模式  






命令默认权限级别 :

MULTICAST6-VRF模式:15,IPv6-组播模式:15 






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
per-stream|选路策略为逐流优先。
per-packet|选路策略为逐包优先。
per-user|选路策略为逐用户优先。
＜acl-name＞|ACL名称，用于指定组播组地址。








缺省 :

bras版本选路策略为按用户选路，非bras版本为逐流优先。 






使用说明 :

1.如果选择group-list选项，则根据ACL规则进行过滤。2.使用per-user选项，转发流量会根据用户分担流量，使用per-stream选项，转发流量会根据路由分担流量。






范例 :

1.配置组播转发策略ZXROSNG(config-mcast-ipv6)#forwarding-policy per-packet2.配置带ACL的组播转发策略ZXROSNG(config-mcast-ipv6)#forwarding-policy per-packet group-list test





相关命令 :

ipv6-access-list 




## frr 


frr 




命令功能 :

配置frr enable打开IPv6-PIM BFD快切开关，配置frr disable关闭IPv6-PIM BFD快切开关。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



frr 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启IPv6-PIM BFD快切功能
disable|关闭IPv6-PIM BFD快切功能








缺省 :

关闭IPv6-PIM BFD快切功能 






使用说明 :

在IPv6-PIM接口模式下配置frr enable，打开IPv6-PIM BFD快切开关。主要表现为首先BDR设备往上游引流，同时在BDR设备上会下发不转发接口属性到转发面，当BDR向DR切换时，BDR设备的不转发属性会更新为转发属性。配置frr disable关闭IPv6-PIM BFD快切开关，主要表现为BDR设备不再往上游引流，强制清除接口上的不转发标记。 






范例 :

ZXROSNG(config)#ipv6 multicastZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#frr enableZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#frr disable





相关命令 :

bfd-enable 




## frr 


frr 




命令功能 :

配置frr enable打开IPv6-PIM BFD快切开关，配置frr disable关闭IPv6-PIM BFD快切开关。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



frr 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启IPv6-PIM BFD快切功能
disable|关闭IPv6-PIM BFD快切功能








缺省 :

关闭IPv6-PIM BFD快切功能 






使用说明 :

在IPv6-PIM接口模式下配置frr enable，打开IPv6-PIM BFD快切开关。主要表现为首先BDR设备往上游引流，同时在BDR设备上会下发不转发接口属性到转发面，当BDR向DR切换时，BDR设备的不转发属性会更新为转发属性。配置frr disable关闭IPv6-PIM BFD快切开关，主要表现为BDR设备不再往上游引流，强制清除接口上的不转发标记。 






范例 :

ZXROSNG(config)#ipv6 multicastZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#frr enableZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#frr disable





相关命令 :

bfd-enable 




## graft-retry-time 


graft-retry-time 




命令功能 :

配置graft重传时间。使用no命令恢复默认值。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

配置 graft-retry-time：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#graft-retry-time 200






相关命令 :

router pim：使能PIM。 




## graft-retry-time 


graft-retry-time 




命令功能 :

配置graft重传时间。使用no命令恢复默认值。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

配置 graft-retry-time：ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pim ZXROSNG(config-mcast-ipv6-pim)# graft-retry-time 200





相关命令 :

router pim：使能PIM。 




## hello-dr-address 


hello-dr-address 




命令功能 :

使能PIM接口发送hello报文时携带DR地址选项。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






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

在接口gei-0/1/0/1上启动hello-dr-address：ZXROSNG(config) #ipv6 multicast-routingZXROSNG(config-mcast) #router pimZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#hello-dr-address





相关命令 :

pimsm,pimdm 




## hello-dr-address 


hello-dr-address 




命令功能 :

使能PIM接口发送hello报文时携带DR地址选项。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






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

在接口gei-0/1/0/1上启动hello-dr-address：ZXROSNG(config) #ipv6 multicast-routingZXROSNG(config-mcast) #router pimZXROSNG(config-mcast-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-pim-if-gei-0/1/0/1)#hello-dr-address





相关命令 :

pimsm,pimdm 




## hello-interval 


hello-interval 




命令功能 :

配置接口PIM hello报文发送间隔，使用no命令恢复缺省值。 






命令模式 :

 IPv6-PIM接口模式  






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
＜seconds＞|PIM路由器hello报文发送周期间隔，缺省为30秒，范围：1–65535，单位：秒








缺省 :

PIM路由器hello报文发送周期间隔，缺省为30秒。 






使用说明 :

该命令对于PIM-DM和PIM-SM都有效。此命令用来配置路由器发送hello报文的时间间隔。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6-pim)# interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#hello-interval 200






相关命令 :

show ipv6 pim interface：显示PIM6接口信息。 




## hello-interval 


hello-interval 




命令功能 :

配置接口PIM hello报文发送间隔，使用no命令恢复缺省值。 






命令模式 :

 IPv6-PIM-VRF接口模式  






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
＜seconds＞|PIM路由器hello报文发送周期间隔，缺省为30秒，范围：1–65535，单位：秒








缺省 :

PIM路由器hello报文发送周期间隔，缺省为30秒。 






使用说明 :

该命令对于PIM-DM和PIM-SM都有效。此命令用来配置路由器发送hello报文的时间间隔。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#hello-interval 200






相关命令 :

show ipv6 pim interface：显示PIM6接口信息。 




## hello-join-attribute 


hello-join-attribute 




命令功能 :

使能PIM hello加入属性选项开关。 






命令模式 :

 IPv6-PIM模式  






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

命令使能后，PIM hello报文携带向量加入属性选项。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#hello-join-attribute






相关命令 :

无 




## immediate-leave 


immediate-leave 




命令功能 :

配置允许MLD立即离开的组范围，即路由器在收到离开报文后，查询者不发送指定组查询，直接认为成员离开，使用no命令取消限制。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






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

无 






使用说明 :

1. 接口模式下，仅对MLD v1接口有效。2. 该命令如果没有选项，则对所有组播组有效。





范例 :

配置允许MLD立即离开的组范围：ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#immediate-leave all 





相关命令 :

无 




## immediate-leave 


immediate-leave 




命令功能 :

配置允许MLD立即离开的组范围，即路由器在收到离开报文后，查询者不发送指定组查询，直接认为成员离开，使用no命令取消限制。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






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

无 






使用说明 :

1. 接口模式下，仅对MLD v1接口有效。2. 该命令如果没有选项，则对所有组播组有效。





范例 :

配置允许MLD立即离开的组范围：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#immediate-leave all 





相关命令 :

无 




interface :

interface (IPv6-PIM模式) 




命令功能 :

将命令模式切换到PIM6接口配置模式下。 






命令模式 :

 IPv6-PIM模式  






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
＜interface-name＞|接口的名称








缺省 :

无 






使用说明 :

1.将命令模式切换到PIM6接口配置模式下。2.不切换到PIM6接口配置下，PIM6接口下配置命令无法运行。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6-pim)# interface gei-0/1/0/1






相关命令 :

无 




interface :

interface (IPv6-PIM-VRF模式) 




命令功能 :

将命令模式切换到PIM6接口配置模式下。 






命令模式 :

 IPv6-PIM-VRF模式  






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
＜interface-name＞|接口的名称








缺省 :

无 






使用说明 :

1.将命令模式切换到PIM6接口配置模式下。2.不切换到PIM6接口配置下，PIM6接口下配置命令无法运行。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1






相关命令 :

无 




interface :

interface (MLD模式) 




命令功能 :

进入MLD接口配置模式，与接口开启MLD协议无关，MLD协议开启由接口开启PIM协议触发，使用no命令删除接口配置，恢复默认配置。 






命令模式 :

 MLD模式  






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
＜interface-name＞|接口的名称








缺省 :

无 






使用说明 :

进入MLD接口配置模式:interface <interface-name>;






范例 :

进入MLD接口配置模式ZXROSNG(config)#ipv6 multicast-routing                                      ZXROSNG(config-mcast-ipv6)#router mld ZXROSNG(config-mcast-ipv6-mld)#interface gei-0/3/0/8





相关命令 :

无 




interface :

interface (MLD-VRF模式) 




命令功能 :

进入MLD-VRF接口配置模式，与接口开启MLD协议无关，MLD协议开启由接口开启PIM协议触发，使用no命令删除接口配置，恢复默认配置。 






命令模式 :

 MLD-VRF模式  






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
＜interface-name＞|接口的名称








缺省 :

无 






使用说明 :

进入MLD-VRF接口配置模式:interface <interface-name>;






范例 :

进入MLD-VRF接口配置模式ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/3/0/8





相关命令 :

无 




## ipv6 multicast-routing 


ipv6 multicast-routing 




命令功能 :

启用IPv6组播路由功能。使用no命令关闭组播路由功能。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 multicast-routing 
 

no ipv6 multicast-routing 








命令参数解释 :


					无
				 






缺省 :

关闭IPv6组播路由功能。 






使用说明 :

关闭IP组播路由选择功能后，路由器不转发任何组播数据包，同时停止组播路由协议的运行。缺省情况下组播功能是关闭的。 






范例 :

  启用IP组播路由功能：ZXROSNG(config)#ipv6 multicast-routing





相关命令 :

无 




## ipv6 multicast-static-frr 


ipv6 multicast-static-frr 




命令功能 :

设置回切延迟间隔。在备入接口使用时，主入接口从无效变到UP且有track的话track UP，开始计时，延时WTR时间恢复主入接口。使用no命令取消WTR时间。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 multicast-static-frr 
 wtr 
 ＜wtr 
＞

no ipv6 multicast-static-frr 








命令参数解释 :



参数|描述
---|---
＜wtr＞|静态组播路由入接口回切延迟间隔，范围1-12，单位：分钟








缺省 :

立即回切。 






使用说明 :

1．没有配置ipv6 multicast-static-start，不能配置该命令。2．备入接口有效，主入接口从无效切换到有效时，没配置该命令，则立即切换到主入接口，配置该命令则延时WTR后切换。





范例 :

配置静态组播路由回切延迟时间：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#ipv6 multicast-static-startZXROSNG(config-mcast-ipv6)#ipv6 multicast-static-frr wtr 6





相关命令 :

ipv6 multicast-static-startipv6 multicast-static-limitipv6 multicast-static-route



## ipv6 multicast-static-frr 


ipv6 multicast-static-frr 




命令功能 :

设置回切延迟间隔。在备入接口使用时，主入接口从无效变到UP且有track的话track UP，开始计时，延时WTR时间恢复主入接口。使用no命令取消WTR时间。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 multicast-static-frr 
 wtr 
 ＜wtr 
＞

no ipv6 multicast-static-frr 








命令参数解释 :



参数|描述
---|---
＜wtr＞|静态组播路由入接口回切延迟间隔，范围1-12，单位：分钟








缺省 :

立即回切。 






使用说明 :

1．没有配置ipv6 multicast-static-start，不能配置该命令。2．备入接口有效，主入接口从无效切换到有效时，没配置该命令，则立即切换到主入接口，配置该命令则延时WTR后切换。





范例 :

配置静态组播路由回切延迟时间：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#ipv6 multicast-static-startZXROSNG(config-mcast-ipv6-vrf-zte)#ipv6 multicast-static-frr wtr 6





相关命令 :

ipv6 multicast-static-startipv6 multicast-static-limitipv6 multicast-static-route



## ipv6 multicast-static-interface 


ipv6 multicast-static-interface 




命令功能 :

配置静态组播出接口列表，使用no命令删除配置。 






命令模式 :

 IPv6-组播模式,MULTICAST6-VRF模式  






命令默认权限级别 :

MULTICAST6-VRF模式:15,IPv6-组播模式:15 






命令格式 :


ipv6 multicast-static-interface 
 index 
 ＜index 
＞ interface 
 ＜interface-name 
＞
no ipv6 multicast-static-interface 
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

缺省无出接口列表。 






使用说明 :

1．支持的出接口列表索引号范围是1-100，每个索引下可关联接口的个数最多64个。2．删除出接口列表时既支持删除整个出接口列表，也支持删除某个出接口列表下的某一个接口。3．出接口列表配置后，如删除某一接口，那么出接口列表下关联相应接口自动被删除，当此接口再次被创建时，需重新配置。4．删除出接口列表中的最后一个接口后，该出接口列表也被删除。





范例 :

将gei-0/1/0/1配置到出接口列表10下：ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#ipv6 multicast-static-interface index 10 interface gei-0/1/0/1





相关命令 :

show ipv6 multicast-static-interfaceipv6 multicast-static-limitipv6 multicast-static-startipv6 multicast-routing



## ipv6 multicast-static-limit 


ipv6 multicast-static-limit 




命令功能 :

配置允许配置的静态组播路由条目数，使用no命令删除配置 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 multicast-static-limit 
 xg 
 ＜xg-limit 
＞ sg 
 ＜sg-limit 
＞

no ipv6 multicast-static-limit 








命令参数解释 :



参数|描述
---|---
＜xg-limit＞|允许配置的静态组播(*,G)路由条目数，范围1~$#134348849#$
＜sg-limit＞|允许配置的静态组播(S,G)路由条目数，范围1~$#134348849#$








缺省 :

缺省允许配置的静态组播(*,G)和(S,G)路由条目数为0，为0时不能配置静态组播条目。 






使用说明 :

1．配置的静态组播容量不能超过线卡支持的最大容量。2．如果两次配置不同的静态组播容量，第二次配置容量需要比第一次容量大才可直接配，如果需要将容量改小，需要首先将已经配置的容量通过no命令删除，再重新配置较小容量，不可直接配置将容量改小。如果改小会出现错误提示：Parameter can't be smaller than the last configured,delete the last configured first and try again!3.xg和sg条目数的配置范围从1到版本中性能参数规定的值。






范例 :

配置允许配置的静态组播(*,G)路由条目数为10，(S,G)路由条目数为10：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#ipv6 multicast-static-limit xg 10 sg 10





相关命令 :

ipv6 multicast-static-startipv6 multicast-routing



## ipv6 multicast-static-route 


ipv6 multicast-static-route 




命令功能 :

配置静态组播路由，使用no命令删除配置。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 multicast-static-route 
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
no ipv6 multicast-static-route 
  ＜source-address 
＞ ＜group-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜source-address＞|静态组播源地址，为X:X::X:X形式
＜group-address＞|静态组播组地址，为X:X::X:X形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，X:X::X:X形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜in-interface-name＞|静态组播条目入接口名
＜master-track-name＞|静态组播路由主入接口关联检测的track名称，长度1-31个字符
＜slave-in-interface-name＞|静态组播条目备入接口名
＜slave-track-name＞|静态组播路由备入接口关联检测的track名称，长度1-31个字符
＜out-interface-index＞|静态组播条目出接口列表索引号








缺省 :

缺省无静态组播路由 






使用说明 :

1．静态组播源地址参数在配置(S,G)静态组播路由时为源地址，配置(*,G)静态组播路由时为0::0。2．没有配置ipv6 multicast-static-limit，无法配置ipv6 multicast-static-route。3．静态组播出接口列表为ipv6 multicast-static-interface命令配置的出接口列表。4．配置静态组播路由备入接口时，必须同时配置主入接口。5．静态组播路由主入接口和备入接口不能是同一个接口。6．批量配置时，掩码步长和数目需要同时配置，确保所有组地址的合法性。7．避免不同配置命令创建相同的路由条目8. 批量配置时，组地址和掩码步长的最高字节位都不参与计算。






范例 :

1．配置（1::1，ff88::1）静态组播路由，入接口gei-0/1/0/5，出接口列表10：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/5 oif 10或者：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 oif 10 iif gei-0/1/0/52．配置静态组播路由主入接口关联检测的track：ZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 track test oif 10取消此路由主入接口关联检测的track：ZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 oif 103． 配置静态组播路由备入接口：ZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 oif 10取消此路由备入接口：ZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 oif 104．配置静态组播路由备入接口关联检测的track：ZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 track test oif 10取消此路由备入接口关联检测的track：ZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 oif 105．批量配置（1::1，ff88::1）静态组播路由，掩码步长1::1，批量数目为10：ZXROSNG(config-mcast-ipv6)# ipv6 multicast-static-route 1::1 ff88::1 inc-mask 1::1 count 10





相关命令 :

ipv6 multicast-static-startipv6 multicast-static-limitipv6 multicast-static-interfaceipv6 multicast-routing



## ipv6 multicast-static-route 


ipv6 multicast-static-route 




命令功能 :

配置IPv6静态组播路由，使用no命令删除配置。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 multicast-static-route 
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
no ipv6 multicast-static-route 
  ＜source-address 
＞ ＜group-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜source-address＞|静态组播源地址，为X:X::X:X形式
＜group-address＞|静态组播组地址，为X:X::X:X形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，X:X::X:X形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜in-interface-name＞|静态组播条目入接口名
＜master-track-name＞|静态组播路由主入接口关联检测的track名称，长度1-31个字符
＜slave-in-interface-name＞|静态组播条目备入接口名
＜slave-track-name＞|静态组播路由备入接口关联检测的track名称，长度1-31个字符
＜out-interface-index＞|静态组播条目出接口列表索引号








缺省 :

缺省无静态组播路由 






使用说明 :

1．静态组播源地址参数在配置(S,G)静态组播路由时为源地址，配置(*,G)静态组播路由时为0::0。2．没有配置ipv6 multicast-static-limit，无法配置ipv6 multicast-static-route。3．静态组播出接口列表为ipv6 multicast-static-interface命令配置的出接口列表。4．配置静态组播路由备入接口时，必须同时配置主入接口。5．静态组播路由主入接口和备入接口不能是同一个接口。6．批量配置时，掩码步长和数目需要同时配置，确保所有组地址的合法性。7．避免不同配置命令创建相同的路由条目8. 批量配置时，组地址和掩码步长的最高字节位都不参与计算。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)1．配置（1::1，ff88::1）静态组播路由，入接口gei-0/1/0/5，出接口列表10：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/5 oif 10或者：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 oif 10 iif gei-0/1/0/52．配置静态组播路由主入接口关联检测的track：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 track test oif 10取消此路由主入接口关联检测的track：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 oif 103． 配置静态组播路由备入接口：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 oif 10取消此路由备入接口：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 oif 104．配置静态组播路由备入接口关联检测的track：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 track test oif 10取消此路由备入接口关联检测的track：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 iif gei-0/1/0/1 slave-iif gei-0/1/0/2 oif 105．批量配置（1::1，ff88::1）静态组播路由，掩码步长1::1，批量数目为10：ZXROSNG(config-mcast-ipv6-vrf-zte)# ipv6 multicast-static-route 1::1 ff88::1 inc-mask 1::1 count 10





相关命令 :

ipv6 multicast-static-startipv6 multicast-static-limitipv6 multicast-static-interfaceipv6 multicast-routing



## ipv6 multicast-static-start 


ipv6 multicast-static-start 




命令功能 :

启用静态组播路由协议MSTATIC，使用no命令关闭MSTATIC。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 multicast-static-start 
 

no ipv6 multicast-static-start 








命令参数解释 :


					无
				 






缺省 :

不使能。 






使用说明 :

1. 默认不启用静态组播，没有启用静态组播时静态组播相关命令将不可用。2. 没有配置ipv6 multicast-routing，MSTATIC路由协议无法运行。





范例 :

启用静态组播路由协议MSTATIC：ZXROSNG(config)#ipv6 multicast-routing  ZXROSNG(config-mcast-ipv6)#ipv6 multicast-static-start 





相关命令 :

ipv6 multicast-routing 




## ipv6 multicast-static-start 


ipv6 multicast-static-start 




命令功能 :

启用静态组播路由协议MSTATIC，使用no命令关闭MSTATIC。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 multicast-static-start 
 

no ipv6 multicast-static-start 








命令参数解释 :


					无
				 






缺省 :

不使能。 






使用说明 :

1. 默认不启用静态组播，没有启用静态组播时静态组播相关命令将不可用。2. 没有配置ipv6 multicast-routing，MSTATIC路由协议无法运行。





范例 :

启用私网静态组播路由协议MSTATIC： ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#ipv6 multicast-static-start 






相关命令 :

ipv6 multicast-routing 




## join-group 


join-group 




命令功能 :

配置MLD接口上的静态组成员，要发送report报文，使用no命令删除接口上的静态组成员。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






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
＜group-address＞|IPv6格式的组播组地址，X:X::X:X形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，X:X::X:X形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜source-address＞|IPv6格式的单播源地址，X:X::X:X形式
include|切换到include模式
exclude|切换到exclude模式








缺省 :

无 






使用说明 :

1.    Join-group配置MLD接口上的静态组成员要发送report报文，static-goup命令配置的静态组成员不会发送report报文。2.    配置MLD接口上的静态组成员:join-group ＜group-address＞[source ＜source-address＞ [{include|exclude}]]3.    接口上批量配置静态组加入：批量配置静态组的时候，需要先使能PIM接口；反之，在删除PIM接口的时候，检查批量静态组是否存在，不存在才能执行no命令。4.    删除接口上批量配置时，必须输入inc-mask参数。5. 接口上批量配置静态组加入时，组地址和掩码步长的最高字节位都不参与计算。6.配置带源的Join group时，接口需使能MLD v2版本才能发送MLD v2 report7.Join group配置源信息时可指定include或者exclude模式，也可不指定，不指定模式时默认为include模式






范例 :

1.    配置MLD接口上的组成员：ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#join-group ff88::1查看配置结果信息：ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#show ipv6 mld groupsTotal: 1 groupsGroup Address : ff88::1Last Reporter : fe80::2ee:ffff:fe30:1000Interface : gei-0/1/0/10Uptime : 00:57:32Expires : never2.    配置loopback1接口加入起始组地址为ff33::1，递增掩码步长为::2，组地址数量为4的批量组播组：ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast)#router mldZXROSNG(config-mcast-ipv6-mld)#interface loopback1ZXROSNG(config-mcast-ipv6-mld-if-loopback1)# join-group ff33::1 inc-mask ::2 count 4ZXROSNG(config-mcast-ipv6-mld-if-loopback1)#show ipv6 mld groupsTotal: 4 groupsGroup Address : ff33::1Last Reporter : fe80::216:3eff:fe64:105Interface : loopback1Uptime : 00:00:06Expire : neverGroup Address : ff33::3Last Reporter : fe80::216:3eff:fe64:105Interface : loopback1Uptime : 00:00:06Expire : neverGroup Address : ff33::5Last Reporter : fe80::216:3eff:fe64:105Interface : loopback1Uptime : 00:00:06Expire : neverGroup Address : ff33::7Last Reporter : fe80::216:3eff:fe64:105Interface : loopback1Uptime : 00:00:06Expire : never3.配置接口组成员，组地址为ffee::10,源地址为2002::10,源模式为include模式ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/20/0/2ZXROSNG(config-mcast-ipv6-mld-if-gei-0/20/0/2)#join-group ffee::10 source 2002::10 include查看配置结果信息：ZXROSNG(config-mcast-ipv6-mld-if-gei-0/20/0/2)#show ipv6 mld groupsTotal: 1 groupsGroup Address : ffee::10Last Reporter : fe80::216:3eff:fe64:305    Interface : gei-0/20/0/2       Uptime : 00:01:04       Expire : neverZXROSNG(config-mcast-ipv6-mld-if-gei-0/20/0/2)#show ipv6 mld groups detailFlags: S - Static Group, SSM - SSM Group, M - MDT GroupInterface:      gei-0/20/0/2Group:          ffee::10Flags:Uptime:         00:01:05Group mode:     INCLUDELast reporter:  fe80::216:3eff:fe64:305Group source list: (M - SSM Mapping, S - Static, R - Report)  Source addr                             Present   Expire   Fwd  Flag  2002::10                                00:01:05  Never     Yes  S





相关命令 :

pimsm，pimdm，version 




## join-group 


join-group 




命令功能 :

配置MLD接口上的静态组成员，要发送report报文，使用no命令删除接口上的静态组成员。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






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
＜group-address＞|IPv6格式的组播组地址，X:X::X:X形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，X:X::X:X形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜source-address＞|IPv6格式的单播源地址，X:X::X:X形式
include|切换到include模式
exclude|切换到exclude模式








缺省 :

无 






使用说明 :

1.    Join-group配置IGMP接口上的静态组成员要发送report报文，static-goup命令配置的静态组成员不会发送report报文。2.    配置MLD接口上的静态组成员:join-group ＜group-address＞[source ＜source-address＞ [{include|exclude}]]3.    接口上批量配置静态组加入：批量配置静态组的时候，需要先使能PIM接口；反之，在删除PIM接口的时候，检查批量静态组是否存在，不存在才能执行no命令。4.    删除接口上批量配置时，必须输入inc-mask参数。5. 接口上批量配置静态组加入时，组地址和掩码步长的最高字节位都不参与计算。6.配置带源的Join group时，接口需使能MLD v2版本才能发送MLD v2 report7.Join group配置源信息时可指定include或者exclude模式，也可不指定，不指定模式时默认为include模式






范例 :

1.    配置MLD接口上的组成员：ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#join-group ff88::1查看配置结果信息：ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#show ipv6 mld groups vrf zteTotal: 1 groupsGroup Address : ff88::1Last Reporter : fe80::2ee:ffff:fe30:1000Interface : gei-0/1/0/10Uptime : 00:57:32Expires : never2.    配置loopback1接口加入起始组地址为ff33::1，递增掩码步长为::2，组地址数量为4的批量组播组：ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mld ZXROSNG(config-mcast-ipv6-vrf-zte-mld)# interface loopback1ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-loopback1)# join-group ff33::1 inc-mask ::2 count 4ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-loopback1)show ipv6 mld groups vrf zteTotal: 4 groupsGroup Address : ff33::1Last Reporter : fe80::216:3eff:fe64:105Interface : loopback1Uptime : 00:00:06Expire : neverGroup Address : ff33::3Last Reporter : fe80::216:3eff:fe64:105Interface : loopback1Uptime : 00:00:06Expire : neverGroup Address : ff33::5Last Reporter : fe80::216:3eff:fe64:105Interface : loopback1Uptime : 00:00:06Expire : neverGroup Address : ff33::7Last Reporter : fe80::216:3eff:fe64:105Interface : loopback1Uptime : 00:00:06Expire : never3.配置接口组成员，组地址为ffee::10,源地址为2002::10,源模式为include模式ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/20/0/2ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/20/0/2)#join-group ffee::10 source 2002::10 include查看配置结果信息：ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/20/0/2)#show ipv6 mld groups vrf zteTotal: 1 groupsGroup Address : ffee::10Last Reporter : fe80::216:3eff:fe64:305    Interface : gei-0/20/0/2       Uptime : 00:01:04       Expire : neverZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/20/0/2)#show ipv6 mld groups vrf zte detailFlags: S - Static Group, SSM - SSM Group, M - MDT GroupInterface:      gei-0/20/0/2Group:          ffee::10Flags:Uptime:         00:01:05Group mode:     INCLUDELast reporter:  fe80::216:3eff:fe64:305Group source list: (M - SSM Mapping, S - Static, R - Report)  Source addr                             Present   Expire   Fwd  Flag  2002::10                                00:01:05  Never     Yes  S






相关命令 :

pimsm，pimdm，version 




## join-prune-holdtime 


join-prune-holdtime 




命令功能 :

设置发送Join/Prune报文的holdtime值。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

设置发Join/Prune报文的holdtime值为270秒：ZXROSNG(config#ipv6 multicast-routing ZXR10 (config-mcast-ipv6)#route pimZXROSNG(config-mcast-ipv6-pim)#join-prune-holdtime 270 ZXROSNG(config-mcast-ipv6-pim)#





相关命令 :

无 




## join-prune-holdtime 


join-prune-holdtime 




命令功能 :

设置发送Join/Prune报文的holdtime值。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

设置发Join/Prune报文的holdtime值为270秒：ZXROSNG(config#ipv6 multicast-routing ZXR10 (config-mcast-ipv6)#route pimZXROSNG(config-mcast-ipv6-pim)#join-prune-holdtime 270 





相关命令 :

无 




## join-prune-interval 


join-prune-interval 




命令功能 :

设置发送Join/Prune报文的周期，使用no命令恢复默认值。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

发送Join/Prune报文的周期缺省60秒。 






使用说明 :

此命令设置周期性的向上游路由器发送Join/Prune报文的时间间隔，上游路由器收到下游的Join/Prune报文，会更新下游接口状态，维护(*,G)和（S,G）表项。





范例 :

设置发送Join/Prune报文的时间间隔为270秒：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#route pimZXROSNG(config-mcast-ipv6-pim)#join-prune-interval 270





相关命令 :

无 




## join-prune-interval 


join-prune-interval 




命令功能 :

设置发送Join/Prune报文的周期，使用no命令恢复默认值。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

发送Join/Prune报文的周期缺省60秒。 






使用说明 :

此命令设置周期性的向上游路由器发送Join/Prune报文的时间间隔，上游路由器收到下游的Join/Prune报文，会更新下游接口状态，维护(*,G)和（S,G）表项。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#join-prune-interval 270






相关命令 :

无 




## join-prune-speed 


join-prune-speed 




命令功能 :

配置PIM JP报文每秒发送的表项个数。使用no命令恢复默认值。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

配置 join-prune-speed：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)# join-prune-speed 2000






相关命令 :

router pim：使能PIM。 




## join-prune-speed 


join-prune-speed 




命令功能 :

配置PIM JP报文每秒发送的表项个数。使用no命令恢复默认值。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

配置 join-prune-speed：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#join-prune-speed 2000






相关命令 :

router pim：使能PIM。 




## jp-max-packet-length 


jp-max-packet-length 




命令功能 :

配置IPv6 PIM发送的Join/Prune报文的最大长度。使用no命令取消配置。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



jp-max-packet-length 
  ＜bytes 
＞

no jp-max-packet-length 








命令参数解释 :



参数|描述
---|---
＜bytes＞|IPv6 PIM发送的Join/Prune报文的最大长度，范围：100-8100，单位：字节








缺省 :

IPv6 PIM发送的Join/Prune报文的最大长度，缺省为1400字节。 






使用说明 :

接口下需先使能IPv6 PIM才能配置此命令。jp-max-packet-length命令配置的报文长度如果大于接口IPv6 MTU值，则实际报文发送最大长度为接口IPv6 MTU值。实际报文最小长度小于此配置，则按照实际报文长度发送。对于(S,G,rpt)剪枝的场景，命令配置的报文长度小于1400，如果该大小能装下该组所有的(S,G,rpt)剪枝，则用当前报文大小，如果装不下，则按照1400发包，配置长度大于1400则按照命令配置发包。 






范例 :

ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#jp-max-packet-length 100






相关命令 :

ipv6 mtu：配置接口上的IPv6 MTU。pimsm：配置接口上的IPv6 PIM-SM。pimdm：配置接口上的IPv6 PIM-DM。




## jp-max-packet-length 


jp-max-packet-length 




命令功能 :

配置IPv6 PIM发送的Join/Prune报文的最大长度。使用no命令取消配置。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



jp-max-packet-length 
  ＜bytes 
＞

no jp-max-packet-length 








命令参数解释 :



参数|描述
---|---
＜bytes＞|IPv6 PIM发送的Join/Prune报文的最大长度，范围：100-8100，单位：字节








缺省 :

IPv6 PIM发送的Join/Prune报文的最大长度，缺省为1400字节。 






使用说明 :

接口下需先使能IPv6 PIM才能配置此命令。jp-max-packet-length命令配置的报文长度如果大于接口IPv6 MTU值，则实际报文发送最大长度为接口IPv6 MTU值。实际报文最小长度小于此配置，则按照实际报文长度发送。对于(S,G,rpt)剪枝的场景，命令配置的报文长度小于1400，如果该大小能装下该组所有的(S,G,rpt)剪枝，则用当前报文大小，如果装不下，则按照1400发包，配置长度大于1400则按照命令配置发包。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#jp-max-packet-length 100






相关命令 :

ipv6 mtu：配置接口上的IPv6 MTU。pimsm：配置接口上的IPv6 PIM-SM。pimdm：配置接口上的IPv6 PIM-DM。




## last-member-query-interval 


last-member-query-interval 




命令功能 :

配置路由器发送特定组查询间隔，使用no命令恢复缺省值。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






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

缺省为1秒 






使用说明 :

可以在以下模式下配置last-member-query-interval：1. MLD模式/MLD-VRF模式2. MLD接口模式/MLD-VRF接口模式1、2模式下都配置last-member-query-interval，则以接口模式下配置的值为准






范例 :

配置MLD特定组查询间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#last-member-query-interval 10





相关命令 :

无 




## last-member-query-interval 


last-member-query-interval 




命令功能 :

配置路由器发送特定组查询间隔，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






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

缺省为1秒 






使用说明 :

可以在以下模式下配置last-member-query-interval：1. MLD模式/MLD-VRF模式2. MLD接口模式/MLD-VRF接口模式1、2模式下都配置last-member-query-interval，则以接口模式下配置的值为准






范例 :

配置MLD特定组查询间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#last-member-query-interval 10





相关命令 :

无 




## last-member-query-interval 


last-member-query-interval 




命令功能 :

配置路由器发送特定组查询间隔，使用no命令恢复缺省值。 






命令模式 :

 MLD模式  






命令默认权限级别 :

15 






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

MLD接口模式下也有last-member-query-interval命令，当MLD接口模式下没有配置这条命令，则MLD模式下的配置生效。 






范例 :

配置MLD特定组查询间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#last-member-query-interval 10






相关命令 :

无 




## last-member-query-interval 


last-member-query-interval 




命令功能 :

配置路由器发送特定组查询间隔，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF模式  






命令默认权限级别 :

15 






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

缺省为1秒 






使用说明 :

一般会依据MLD-VRF接口模式下配置的last-member-query-interval,但是若MLD-VRF接口模式下没有配置last-member-query-interval,MLD-VRF模式下配置了last-member-query-interval,则MLD-VRF模式下配置的last-member-query-interval会生效.否则会选择默认值。 






范例 :

配置MLD特定组查询间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#last-member-query-interval 10





相关命令 :

无 




## longest-match 


longest-match 




命令功能 :

设置组播查找单播路由按照掩码最长匹配规则。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



longest-match 
 

no longest-match 








命令参数解释 :


					无
				 






缺省 :

没有配置 






使用说明 :

1.配置后组播按照掩码最长匹配规则选择单播路由。 






范例 :

设置组播按照掩码最长匹配规则查找单播路由：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#longest-match






相关命令 :

ipv6 multicast-routing 




## longest-match 


longest-match 




命令功能 :

设置组播查找单播路由按照掩码最长匹配规则。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



longest-match 
 

no longest-match 








命令参数解释 :


					无
				 






缺省 :

没有配置 






使用说明 :

1.配置后组播按照掩码最长匹配规则选择单播路由。 






范例 :

设置组播按照掩码最长匹配规则查找单播路由：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#longest-match






相关命令 :

ipv6 multicast-routing 




## maximum-joins 


maximum-joins 




命令功能 :

配置MLD接口允许的最大加入数，使用no命令取消限制。 






命令模式 :

 MLD-VRF接口模式,MLD接口模式  






命令默认权限级别 :

MLD接口模式:15,MLD-VRF接口模式:15 






命令格式 :



maximum-joins 
  ＜number 
＞

no maximum-joins 








命令参数解释 :



参数|描述
---|---
＜number＞|MLD接口允许的最大加入数，范围：1-40000








缺省 :

无 






使用说明 :

限制此命令生效之后的动态组加入。 






范例 :

配置MLD最大加入数：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/7/1/2ZXROSNG(config-mcast-ipv6-mld-if-gei-0/7/1/2)#maximum-joins 100






相关命令 :

无 




## mofrr 


mofrr 




命令功能 :

开启MoFRR功能，只有符合ACL规则的(S,G)路由条目才能开启，使用no命令恢复缺省状态。 






命令模式 :

 IPv6-PIM-VRF模式,IPv6-PIM模式  






命令默认权限级别 :

IPv6-PIM模式:15,IPv6-PIM-VRF模式:15 






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

开启MoFRR功能：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#route pimZXROSNG(config-mcast--ipv6-pim)#mofrr zte





相关命令 :

show ipv6 pim mroute 




## mroute6-limit p-instance 


mroute6-limit p-instance 




命令功能 :

根据实际组网情况和业务性能要求，配置IPv6组播公网路由条目数量限制。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



mroute6-limit p-instance 
  ＜limit 
＞

no mroute6-limit p-instance 








命令参数解释 :



参数|描述
---|---
＜limit＞|配置公网路由条目数量限制，范围1~$#134348843#$。








缺省 :

没有配置IPv6组播公网路由条目数量限制。 






使用说明 :

1．命令配置不设置约束，即单实例数量限制可以大于全局数量限制。2．limit的配置范围，从1到版本中性能参数规定的值。





范例 :

配置IPv6组播公网路由条目数量限制ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#mroute6-limit p-instance 100%Info 20012: Reload or use 'clear ipv6 mroute' command, this command may take effect.





相关命令 :

mroute6-limit 




## mroute6-limit 


mroute6-limit 




命令功能 :

根据实际组网情况和业务性能要求，配置IPv6组播路由条目数量限制。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



mroute6-limit 
  ＜limit 
＞

no mroute6-limit 








命令参数解释 :



参数|描述
---|---
＜limit＞|配置路由条目数目限制，范围1~$#134348843#$。








缺省 :

没有配置IPv6组播路由条目限制。 






使用说明 :

1．IPv6-组播模式下，配置此命令，控制全局路由条目数量限制。2．命令配置不设置约束，即单实例数量限制可以大于全局数量限制。3．limit的配置范围，从1到版本中性能参数规定的值。





范例 :

配置IPv6组播全局路由条目数量限制ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#mroute6-limit 1024%Info 20012: Reload or use 'clear ipv6 mroute' command, this command may take effect.





相关命令 :

mroute6-limit p-instance 




## mroute6-limit 


mroute6-limit 




命令功能 :

根据实际组网情况和业务性能要求，配置IPv6组播路由条目数量限制。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



mroute6-limit 
  ＜limit 
＞

no mroute6-limit 








命令参数解释 :



参数|描述
---|---
＜limit＞|配置路由条目数目限制，范围1~$#134348843#$。








缺省 :

没有配置IPv6组播路由条目限制。 






使用说明 :

1．MULTICAST6-VRF模式下，配置此命令，控制此VRF实例下路由条目数量限制。2．命令配置不设置约束，即单实例数量限制可以大于全局数量限制。3．limit的配置范围，从1到版本中性能参数规定的值。





范例 :

配置vrf1实例下路由条目数量限制ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf vrf1ZXROSNG(config-mcast-ipv6-vrf-vrf1)#mroute6-limit 100%Info 20012: Reload or use 'clear ipv6 mroute' command, this command may take effect.





相关命令 :

mroute6-limit p-instance 




## mroute-downstream-limit 


mroute-downstream-limit 




命令功能 :

用户可以根据实际组网情况和业务性能要求对组播转发表中单条表项的下行节点数目（即出接口数目）进行限制，以缓解路由器的复制压力。 






命令模式 :

 IPv6-组播模式  






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
＜limit＞|配置出接口数目，范围最大值通过性能参数动态获取，范围1-$#134348834#$








缺省 :

正常生成出接口条目。 






使用说明 :

1.通过配置limit参数设置出接口的数目范围，范围最大值通过性能参数动态获取。 






范例 :

配置组播转发表中单条表项的下行节点数目限制ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#mroute-downstream-limit 20






相关命令 :

ipv6 multicast-routing 




## multicast-address compatible-rfc7371 


multicast-address compatible-rfc7371 




命令功能 :

配置IPv6组播地址兼容RFC7371。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



multicast-address compatible-rfc7371 
 

no multicast-address compatible-rfc7371 








命令参数解释 :


					无
				 






缺省 :

不放开。 






使用说明 :

default ssm的地址范围默认为FF3X::/32，此命令生效后地址范围为FF3X::/32或FFBX::/32。embedded rp的地址范围默认为FF7X/12，此命令生效后地址范围为FF7X/12或FFFX/12。






范例 :

配置组播地址兼容RFC7371：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#multicast-address compatible-rfc7371






相关命令 :

ssm rangeembedded-rp disable




## multicast-boundary 


multicast-boundary 




命令功能 :

在接口上配置组播转发边界，以形成一个封闭的组播转发区域。 






命令模式 :

 IPv6-组播模式  






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
＜access-list-name＞|ACL名称,长度1–31个字符
＜interface-name＞|接口名称








缺省 :

接口未设置组播转发边界 






使用说明 :

1.通过用户命令，在接口上配置组播转发边界，以形成一个封闭的组播转发区域，符合规则的组播组将不会被转发。2.如果边界配置在入接口上则停止转发这条路由的流量，配置在出接口上则停止该接口流量。






范例 :

在接口上配置组播转发边界ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#multicast-boundary zte gei-0/1/0/1






相关命令 :

ipv6 multicast-routing 




## multipath 


multipath 




命令功能 :

配置组播负荷分担模式。使用no命令取消配置。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






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

关闭组播负荷分担 






使用说明 :

1. 如果没有参数选项，则使用基于源的哈希算法分担负荷。2. 如果选择basic选项，则使用基于源组的哈希算法分担负荷。3. 如果选择next-hop-based选项，则使用基于下一跳的哈希算法分担负荷。4. 如果选择balance选项，则使用基于接口上ecmp-cost的哈希算法分担负荷。






范例 :

1.配置基于源的组播负荷分担模式：ZXROSNG(config-mcast-ipv6)#multipath 2.配置基于源组的组播负荷分担模式：ZXROSNG(config-mcast-ipv6)#multipath s-g-hash basic3.配置基于下一跳的组播负荷分担模式：ZXROSNG(config-mcast-ipv6)#multipath s-g-hash next-hop-based4.配置基于接口上ecmp-cost的组播负荷分担模式：ZXROSNG(config-mcast)#multipath s-g-hash balance






相关命令 :

无 




## multipath 


multipath 




命令功能 :

配置组播负荷分担模式。使用no命令取消配置。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






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

关闭组播负荷分担 






使用说明 :

1. 如果没有参数选项，则使用基于源的哈希算法分担负荷。2. 如果选择basic选项，则使用基于源组的哈希算法分担负荷。3. 如果选择next-hop-based选项，则使用基于下一跳的哈希算法分担负荷。4. 如果选择balance选项，则使用基于接口上ecmp-cost的哈希算法分担负荷。





范例 :

1.配置基于源的组播负荷分担模式：ZXROSNG(config-mcast-ipv6)#multipath 2.配置基于源组的组播负荷分担模式：ZXROSNG(config-mcast-ipv6)#multipath s-g-hash basic3.配置基于下一跳的组播负荷分担模式：ZXROSNG(config-mcast-ipv6)#multipath s-g-hash next-hop-based4.配置基于接口上ecmp-cost的组播负荷分担模式：ZXROSNG(config-mcast)#multipath s-g-hash balance






相关命令 :

无 




## mvpn receive-site-only 


mvpn receive-site-only 




命令功能 :

配置MVPN 为receive site only模式。 






命令模式 :

 MULTICAST6-VRF模式  






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

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#mvpn receive-site-only






相关命令 :

本命令与mvpn send-site-only互斥 




## mvpn send-site-only 


mvpn send-site-only 




命令功能 :

配置MVPN 为send site only模式。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



mvpn send-site-only 
 

no mvpn send-site-only 








命令参数解释 :


					无
				 






缺省 :

缺省情况下MVPN为send site和receive site共存模式。 






使用说明 :

1. 配置为send site only模式下，本地PE只发送私网数据，不再向上游PE发送XG和SG加入路由。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#mvpn send-site-only






相关命令 :

本命令与mvpn receive-site-only互斥 




## mvpn spmsi aggregation 


mvpn spmsi aggregation 




命令功能 :

配置MVPN SPMSI隧道聚合。 






命令模式 :

 MULTICAST6-VRF模式  






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
＜count＞|每MVPN SPMSI隧道聚合组播路由条目数量，范围：1~$#134348832#$








缺省 :

每MVPN SPMSI隧道最多可聚合200条组播路由条目。 






使用说明 :

1. 如果没有配置此命令，每MVPN SPMSI隧道最多可聚合200条组播路由条目。2. 如果选择source-based选项，则相同源的组播路由聚合到相同的MVPN SPMSI隧道。3. 如果选择count选项，每MVPN SPMSI隧道最多可聚合<count>条组播路由条目。 4. 单播隧道不适用以上规则，按照每路由每隧道聚合。5. 此命令只对新建SPMSI生效，已有的SPMSI隧道不响应此命令变更。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)# mvpn spmsi aggregation source-based






相关命令 :

无 




## mvpn spt-only 


mvpn spt-only 




命令功能 :

配置MVPN 为SPT only模式，即私网只有SPT才能穿越公网 






命令模式 :

 MULTICAST6-VRF模式  






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

1. 配置为spt-only模式下，私网XG将不再穿越公网 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)# mvpn spt-only






相关命令 :

无 




## mvpn switchover interval 


mvpn switchover interval 




命令功能 :

配置IPv6 MVPN隧道切换间隔。 






命令模式 :

 MULTICAST6-VRF模式  






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

配置IPv6 MVPN 切换延时。MVPN场景为I-PMSI向S-PMSI切换延时。 






范例 :

ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)# mvpn switchover interval 10






相关命令 :

无 




## mvpn switchover threshold-infinity 


mvpn switchover threshold-infinity 




命令功能 :

配置IPv6 MVPN隧道永不切换。 






命令模式 :

 MULTICAST6-VRF模式  






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

配置IPv6 MVPN永不切换ACL。当该ACL规则permit时，MVPN隧道不向S-PMSI切换。配置ACL规则是来过滤(*,G)或者(S,G)路由条目的源地址和组地址的。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)# mvpn switchover threshold-infinity group-list aaa





相关命令 :

无 




## neighbor-filter 


neighbor-filter 




命令功能 :

限制某些路由器成为PIM邻居，使用no命令取消限制。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



neighbor-filter 
  ＜access-list-name 
＞

no neighbor-filter 








命令参数解释 :



参数|描述
---|---
＜access-list-name＞|定义了一个地址范围，该范围是对成为PIM邻居的路由器的限定








缺省 :

缺省情况下不限制其它路由器成为PIM邻居。 






使用说明 :

配置此命令后，满足ACL过滤规则的邻居将被过滤掉，不能成为路由器的邻居。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6-pim)# interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#neighbor-filter zte






相关命令 :

show ipv6 pim neighbor：查看接口邻居信息。 




## neighbor-filter 


neighbor-filter 




命令功能 :

限制某些路由器成为PIM邻居，使用no命令取消限制。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



neighbor-filter 
  ＜access-list-name 
＞

no neighbor-filter 








命令参数解释 :



参数|描述
---|---
＜access-list-name＞|定义了一个地址范围，该范围是对成为PIM邻居的路由器的限定








缺省 :

缺省情况下不限制其它路由器成为PIM邻居。 






使用说明 :

配置此命令后，满足ACL过滤规则的邻居将被过滤掉，不能成为路由器的邻居。





范例 :

ZXROSNG(config)#ipv6-access-list zteZXROSNG(config-ipv6-acl)#rule 1 deny ipv6 fe80::2ee:ffff:fe10:1000/128 anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#show ipv6 pim neighbor gei-0/1/0/1Neighbor Address(es): fe80::2ee:ffff:fe10:1000  Interface: gei-0/1/0/1  Uptime: 01:54:02  Expire: 00:01:25  DR Pri: 1  Attr: N/AZXROSNG(config-mcast-ipv6-pim)#
ZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#neighbor-filter zteZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#exitZXROSNG(config-mcast-ipv6-pim)#show ipv6 pim neighbor gei-0/1/0/1Neighbor Address(es)       Interface            Uptime     Expires    DR PriZXROSNG(config-mcast-ipv6-pim)#






相关命令 :

show ipv6 pim neighbor：查看接口邻居信息。 




## nexthop 


nexthop 




命令功能 :

配置单播路由静态下一跳。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :


nexthop 
  ＜ipv6-address-mask 
＞ {＜interface-name 
＞ ＜nexthop 
＞ [slave 
]|fallback-lookup 
 vrf 
 ＜vrf-name 
＞|path-list 
 ＜path-list-name 
＞}
no nexthop 
  ＜ipv6-address-mask 
＞ [＜interface-name 
＞ ＜nexthop 
＞]
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address-mask＞|IPv6地址，格式：X:X::X:X/<1-128>。X:X::X:X表示目的地址，遵循RFC2373中的规定，以16位为一组，中间用“:”格开。<1-128>表示IPv6地址的前缀长度。配置范围为1-128。 默认值：无。
＜interface-name＞|下一跳出接口
＜nexthop＞|下一跳地址，IPv6地址，为X:X::X:X形式
slave|备下一跳标记
＜vrf-name＞|fallback私网实例VRF名称，长度1-32字符
＜path-list-name＞|RPF路径列表名称，长度1-31字符








缺省 :

不配置静态下一跳 






使用说明 :

1. 对于一个目的地址或网段可以配置多个静态下一跳。指定下一跳出接口和下一跳地址。2. 对于同一个目的地址或网段，只能有一条nexthop带slave参数，带slave参数的nexthop存在时，另外只能有一条不带slave参数的nexthop，此时形成FRR，并且和ECMP互斥。3. 静态配置path-list功能和fallback功能和具体路径功能（ECMP和FRR）互斥，同一目的网段的fallback配置不能直接修改，必须先删除再重新配置，且不能配置fallback到当前实例。






范例 :

1. 配置到目的地址3::3/128的单播路由下一跳出接口为gei-0/1/0/1，下一跳地址为4::5：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#nexthop 3::3/128 gei-0/1/0/1 4::52. 配置到目的地址3::3/128的单播路由下一跳出接口为gei-0/1/0/1，下一跳地址为4::6为备下一跳：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#nexthop 3::3/128 gei-0/1/0/1 4::6 slave3. 配置到目的地址2::2/128的单播路由fallback到私网实例vrf1：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)# nexthop 2::2/128 fallback-lookup vrf vrf16. 配置到目的地址2::2/128的单播路由下一跳迭代查找RPF路径列表abc的单播下一跳：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)# nexthop 2::2/128 path-list abc






相关命令 :

static-firstrpf-proxy-vector path-list




## nexthop 


nexthop 




命令功能 :

配置单播路由静态下一跳。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :


nexthop 
  ＜ipv6-address-mask 
＞ {＜interface-name 
＞ ＜nexthop 
＞ [slave 
]|fallback-lookup 
 {global 
|vrf 
 ＜vrf-name 
＞}}
no nexthop 
  ＜ipv6-address-mask 
＞ [＜interface-name 
＞ ＜nexthop 
＞]
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address-mask＞|IPv6地址，格式：X:X::X:X/<1-128>。X:X::X:X表示目的地址，遵循RFC2373中的规定，以16位为一组，中间用“:”格开。<1-128>表示IPv6地址的前缀长度。配置范围为1-128。 默认值：无。
＜interface-name＞|下一跳出接口
＜nexthop＞|下一跳地址，IPv6地址，为X:X::X:X形式
slave|备下一跳标记
global|fallback公网实例
＜vrf-name＞|fallback私网实例VRF名称，长度1-32字符








缺省 :

不配置静态下一跳 






使用说明 :

1. 对于一个目的地址或网段可以配置多个静态下一跳。指定下一跳出接口和下一跳地址。2. 对于同一个目的地址或网段，只能有一条nexthop带slave参数，带slave参数的nexthop存在时，另外只能有一条不带slave参数的nexthop，此时形成FRR，并且和ECMP互斥。3. 静态配置fallback功能和具体路径功能（ECMP和FRR）互斥，同一目的网段的fallback配置不能直接修改，必须先删除再重新配置，且不能配置fallback到当前实例。





范例 :

1. 私网vrf1实例下配置到目的地址3::3/128的单播路由下一跳出接口为gei-0/1/0/1，下一跳地址为4::5：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf vrf1ZXROSNG(config-mcast-ipv6-vrf-vrf1)# nexthop 3::3/128 gei-0/1/0/1 4::52. 私网vrf1实例下配置到目的地址3::3/128的单播路由下一跳出接口为gei-0/1/0/1，下一跳地址为4::6为备下一跳：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf vrf1ZXROSNG(config-mcast-ipv6-vrf-vrf1)# nexthop 3::3/128 gei-0/1/0/1 4::6 slave3. 私网vrf1实例下配置到目的地址1::2/128的单播路由fallback到公网实例：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf vrf1ZXROSNG(config-mcast-ipv6-vrf-vrf1)# nexthop 1::2/128 fallback-lookup global






相关命令 :

无 




## nsf-lifetime 


nsf-lifetime 




命令功能 :

通过用户配置此命令，预估备板倒换后路由收敛时间后，组播重新开始生成路由。 






命令模式 :

 IPv6-组播模式  






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

1.一般配置此命令值尽量配大一点，保证备板倒换完成。2.在倒换时间之内一般无法配置组播相关命令。                    






范例 :

ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast-ipv6)# nsf-lifetime 600





相关命令 :

ipv6 multicast-routing 




## override-interval 


override-interval 




命令功能 :

配置IPv6 PIM接口的否决间隔。使用no命令取消配置。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



override-interval 
  ＜100 milliseconds 
＞

no override-interval 








命令参数解释 :



参数|描述
---|---
＜100 milliseconds＞|IPv6 PIM接口的否决间隔，范围：1-600，单位：一百毫秒








缺省 :

IPv6 PIM接口的否决间隔，缺省为25百毫秒 






使用说明 :

接口下需先使能IPv6 PIM才能配置此命令 






范例 :

在路由器接口gei-0/1/0/1上配置override-interval：ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)# override-interval 100





相关命令 :

pimsm：配置接口上的IPv6 PIM-SM。配置IPv6 PIM接口的否决间隔与配置接口上IPv6 PIM-SM前置依赖。pimdm：配置接口上的IPv6 PIM-DM。配置IPv6 PIM接口的否决间隔与配置接口上IPv6 PIM-DM前置依赖。



## override-interval 


override-interval 




命令功能 :

配置IPv6 PIM接口的否决间隔。使用no命令取消配置。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



override-interval 
  ＜100 milliseconds 
＞

no override-interval 








命令参数解释 :



参数|描述
---|---
＜100 milliseconds＞|IPv6 PIM接口的否决间隔，范围：1-600，单位：一百毫秒








缺省 :

IPv6 PIM接口的否决间隔，缺省为25百毫秒 






使用说明 :

接口下需先使能IPv6 PIM才能配置此命令。 






范例 :

在交换机接口vlan1上配置override-interval：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#override-interval 100






相关命令 :

pimsm：配置接口上的IPv6 PIM-SM。配置IPv6 PIM接口的否决间隔与配置接口上IPv6 PIM-SM前置依赖。pimdm：配置接口上的IPv6 PIM-DM。配置IPv6 PIM接口的否决间隔与配置接口上IPv6 PIM-DM前置依赖。



## pimdm 


pimdm 




命令功能 :

在接口上使能IPv6组播PIM-DM协议，使用no命令删除配置。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



pimdm 
 

no pimdm 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，接口不使能IPv6组播PIM-DM协议。 






使用说明 :

接口上启动IPv6组播路由协议PIM-DM时，会自动在该接口上启动MLD。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimdm






相关命令 :

interface：必须先进入PIM6接口模式。show ipv6 pim interface：显示PIM6接口信息。




## pimdm 


pimdm 




命令功能 :

在接口上使能IPv6组播PIM-DM协议，使用no命令删除配置。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



pimdm 
 

no pimdm 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，接口不使能IPv6组播PIM-DM协议。 






使用说明 :

接口上启动IPv6组播路由协议PIM-DM时，会自动在该接口上启动MLD。 






范例 :

ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimdm






相关命令 :

interface：必须先进入PIM6接口模式。show ipv6 pim interface：显示PIM6接口信息。




## pimdm-reg 


pimdm-reg 




命令功能 :

入接口配置为PIM-DM模式时，配置该命令，设备收到非直连流量也需要向RP注册。 






命令模式 :

 IPv6-PIM模式  






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

配置pimdm-reg命令，设备收到非直连流量向RP注册：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#pimdm-reg





相关命令 :

无 




## pim-silent 


pim-silent 




命令功能 :

配置接口禁止发送和接收PIM协议报文，使用no命令删除配置。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



pim-silent 
 

no pim-silent 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，接口不启动pim-silent。 






使用说明 :

为了防止恶意主机模拟发送PIM hello报文导致路由器瘫痪，可以配置pim-silent命令，禁止接收和转发任何PIM协议报文。





范例 :

ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pim-silent ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#!ZXROSNG(config)#show ipv6 pim interface Interface                        State Nbr   Hello  DR         PIM      Mode                                       Count Period Priority   Silent  gei-0/1/0/1                      Up    0     200    72         Enabled    S    Address: fe80::2ee:ffff:fe10:2000    DR     : fe80::2ee:ffff:fe10:2000






相关命令 :

show ipv6 pim interface：显示PIM6接口信息。 




## pim-silent 


pim-silent 




命令功能 :

配置接口禁止发送和接收PIM协议报文，使用no命令删除配置。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



pim-silent 
 

no pim-silent 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，接口不启动pim-silent。 






使用说明 :

为了防止恶意主机模拟发送PIM hello报文导致路由器瘫痪，可以配置pim-silent命令，禁止接收和转发任何PIM协议报文。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pim-silent 






相关命令 :

show ipv6 pim interface：显示PIM6接口信息。 




## pimsm 


pimsm 




命令功能 :

配置路由器在接口上使能IPv6组播PIM-SM协议，使用no命令删除配置。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



pimsm 
 

no pimsm 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，接口不使能IPv6组播PIM-SM协议。 






使用说明 :

接口上启动IPv6组播路由协议PIM-SM时，会自动在该接口上启动MLD。 






范例 :

ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pim ZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#!ZXROSNG(config)#show ipv6 pim interface Interface                        State Nbr   Hello  DR         PIM      Mode                                       Count Period Priority   Silent  gei-0/1/0/1                      Up    1     200    72         Disabled   S    Address: fe80::2ee:ffff:fe10:2000    DR     : fe80::2ee:ffff:fe10:2000






相关命令 :

interface：必须先进入PIM6接口模式。show ipv6 pim interface：显示PIM6接口信息。




## pimsm 


pimsm 




命令功能 :

配置路由器在接口上使能IPv6组播PIM-SM协议，使用no命令删除配置。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



pimsm 
 

no pimsm 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，接口不使能IPv6组播PIM-SM协议。 






使用说明 :

接口上启动IPv6组播路由协议PIM-SM时，会自动在该接口上启动MLD。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsm






相关命令 :

interface：必须先进入PIM6接口模式。show ipv6 pim interface：显示PIM6接口信息。




## propagation-delay 


propagation-delay 




命令功能 :

配置IPv6 PIM接口的传输时延。使用no命令取消配置。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






命令格式 :



propagation-delay 
  ＜100 milliseconds 
＞

no propagation-delay 








命令参数解释 :



参数|描述
---|---
＜100 milliseconds＞|IPv6 PIM接口的传输时延，范围：1-100，单位：一百毫秒








缺省 :

IPv6 PIM接口的传输时延，缺省为5百毫秒。 






使用说明 :

接口下需先使能IPv6 PIM才能配置此命令 






范例 :

在路由器接口gei-0/1/0/1上配置propagation-delay：ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)# propagation-delay 100





相关命令 :

pimsm：配置接口上的IPv6 PIM-SM。配置IPv6 PIM接口的传输时延与配置接口上IPv6 PIM-SM前置依赖。pimdm：配置接口上的IPv6 PIM-DM。配置IPv6 PIM接口的传输时延与配置接口上IPv6 PIM-DM前置依赖。



## propagation-delay 


propagation-delay 




命令功能 :

配置IPv6 PIM接口的传输时延。使用no命令取消配置。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



propagation-delay 
  ＜100 milliseconds 
＞

no propagation-delay 








命令参数解释 :



参数|描述
---|---
＜100 milliseconds＞|IPv6 PIM接口的传输时延，范围：1-100，单位：一百毫秒








缺省 :

IPv6 PIM接口的传输时延，缺省为5百毫秒。 






使用说明 :

接口下需先使能IPv6 PIM才能配置此命令。 






范例 :

在交换机接口vlan1上配置propagation-delay：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#pimsmZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#propagation-delay 100






相关命令 :

pimsm：配置接口上的IPv6 PIM-SM。配置IPv6 PIM接口的传输时延与配置接口上IPv6 PIM-SM前置依赖。pimdm：配置接口上的IPv6 PIM-DM。配置IPv6 PIM接口的传输时延与配置接口上IPv6 PIM-DM前置依赖。



## provider-tunnel 


provider-tunnel 




命令功能 :

配置IPv6 MVPN 的隧道转发模式 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



provider-tunnel 
  {mldp-p2mp 
|ingress-replication 
|rsvp-te 
}

no provider-tunnel 








命令参数解释 :



参数|描述
---|---
mldp-p2mp|设置隧道模式走mLDP标签转发
ingress-replication|设置隧道走ingress-replication单播隧道转发
rsvp-te|设置隧道走TE标签转发








缺省 :

无 






使用说明 :

通过配置mldp-p2mp，rsvp-te和ingress-replication参数设置隧道走不同的标签转发。 






范例 :

组播隧道配置：ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#vrf zte1ZXROSNG(config-mcast-ipv6-vrf-zte1)#provider-tunnel mldp-p2mp





相关命令 :

无 




## querier-election disable 


querier-election disable 




命令功能 :

配置MLD的查询者选举限制，使用no命令恢复缺省值。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






命令格式 :



querier-election disable 
 

no querier-election disable 








命令参数解释 :


					无
				 






缺省 :

缺省有MLD查询者选举。 






使用说明 :

配置MLD的查询者选举限制 






范例 :

配置MLD查询者选举规避：ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#querier-election disable





相关命令 :

无 




## querier-election disable 


querier-election disable 




命令功能 :

配置MLD的查询者选举限制，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



querier-election disable 
 

no querier-election disable 








命令参数解释 :


					无
				 






缺省 :

缺省有MLD查询者选举。 






使用说明 :

配置MLD的查询者选举限制 






范例 :

配置MLD查询者选举规避：ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#querier-election disable





相关命令 :

无 




## querier-timeout 


querier-timeout 




命令功能 :

配置查询器超时时间，使用no命令恢复缺省值。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






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

缺省情况下MLD查询器超时时间为两倍MLD查询间隔加查询响应间隔的一半，即（查询间隔×2＋查询响应间隔/2）秒。 






使用说明 :

配置querier-timeout在以下两种模式下：1. MLD模式/MLD-VRF模式;2. MLD接口模式/MLD-VRF接口模式;在1,2两种模式下都配置了querier-timeout的情况下，以MLD接口模式配置的querier-timeout为准





范例 :

配置MLD查询器超时时间：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#querier-timeout 80 





相关命令 :

无 




## querier-timeout 


querier-timeout 




命令功能 :

配置查询器超时时间，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






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

缺省情况下MLD查询器超时时间为两倍MLD查询间隔加查询响应间隔的一半，即（查询间隔×2＋查询响应间隔/2）秒。 






使用说明 :

配置querier-timeout在以下两种模式下：1. MLD模式/MLD-VRF模式;2. MLD接口模式/MLD-VRF接口模式;在1,2两种模式下都配置了querier-timeout的情况下，以接口模式配置的querier-timeout为准





范例 :

配置MLD查询器超时时间：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#querier-timeout 80 





相关命令 :

无 




## querier-timeout 


querier-timeout 




命令功能 :

配置查询器超时时间，使用no命令恢复缺省值。 






命令模式 :

 MLD模式  






命令默认权限级别 :

15 






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

缺省情况下MLD查询器超时时间为两倍MLD查询间隔加查询响应间隔的一半，即（查询间隔×2＋查询响应间隔/2）秒。 






使用说明 :

MLD接口模式下也有querier-timeout 命令，当MLD接口模式下没有配置这条命令，则MLD模式下的配置生效。 






范例 :

配置MLD查询器超时时间：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#querier-timeout 80 





相关命令 :

无 




## querier-timeout 


querier-timeout 




命令功能 :

配置查询器超时时间，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF模式  






命令默认权限级别 :

15 






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

缺省情况下MLD查询器超时时间为两倍MLD查询间隔加查询响应间隔的一半，即（查询间隔×2＋查询响应间隔/2）秒。 






使用说明 :

MLD-VRF接口模式下也有querier-timeout 命令，当MLD-VRF接口模式下没有配置这条命令，则MLD-VRF模式下的配置生效。 






范例 :

配置MLD查询器超时时间：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#querier-timeout 80 






相关命令 :

无 




## query-interval 


query-interval 




命令功能 :

配置路由器发送MLD协议普通查询报文的间隔，使用no命令恢复缺省 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






命令格式 :



query-interval 
  ＜seconds 
＞

no query-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|发送普通查询的间隔，缺省为125秒，范围：1–65535，单位：秒








缺省 :

缺省为125秒 






使用说明 :

配置query-interval在以下两种模式下：1. MLD模式/MLD-VRF模式;2. MLD接口模式/MLD-VRF接口模式;在1,2两种模式下都配置了query-interval的情况下，以MLD接口模式/MLD-VRF接口模式下配置的query-interval为准;该准则并不适用于接口是非查询器的情况。






范例 :

配置MLD发送普通查询报文的间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#query-interval 80





相关命令 :

无 




## query-interval 


query-interval 




命令功能 :

配置路由器发送MLD协议普通查询报文的间隔，使用no命令恢复缺省 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



query-interval 
  ＜seconds 
＞

no query-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|发送普通查询的间隔，缺省为125秒，范围：1–65535，单位：秒








缺省 :

缺省为125秒 






使用说明 :

配置query-interval在以下两种模式下：1. MLD模式/MLD-VRF模式;2. MLD接口模式/MLD-VRF接口模式;在1,2两种模式下都配置了query-interval的情况下，以接口模式配置的query-interval为准;该准则并不适用于接口是非查询器的情况。






范例 :

配置MLD发送普通查询报文的间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#query-interval 80





相关命令 :

无 




## query-interval 


query-interval 




命令功能 :

配置路由器发送MLD协议普通查询报文的间隔，使用no命令恢复缺省 






命令模式 :

 MLD模式  






命令默认权限级别 :

15 






命令格式 :



query-interval 
  ＜seconds 
＞

no query-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|发送普通查询的间隔，缺省为125秒，范围：1–65535，单位：秒








缺省 :

无 






使用说明 :

MLD接口模式下也有query-interval命令，当MLD接口模式下没有配置这条命令，则MLD模式下的配置生效。 






范例 :

配置MLD发送普通查询报文的间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#query-interval 80





相关命令 :

无 




## query-interval 


query-interval 




命令功能 :

配置路由器发送MLD协议普通查询报文的间隔，使用no命令恢复缺省 






命令模式 :

 MLD-VRF模式  






命令默认权限级别 :

15 






命令格式 :



query-interval 
  ＜seconds 
＞

no query-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|发送普通查询的间隔，缺省为125秒，范围：1–65535，单位：秒








缺省 :

缺省为125秒 






使用说明 :

MLD-VRF接口模式下也有query-interval命令，当MLD-VRF接口模式下没有配置这条命令，则MLD-VRF模式下的配置生效。 






范例 :

配置MLD发送普通查询报文的间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#query-interval 80





相关命令 :

无 




## query-max-response-time 


query-max-response-time 




命令功能 :

配置MLD协议发送查询消息时携带的max response time时间值，使用no命令恢复缺省值。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






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

缺省为10秒 






使用说明 :

可以在以下模式下配置query-max-response-time：1. MLD模式/MLD-VRF模式2. MLD接口模式/MLD-VRF接口模式1、2模式下都配置query-max-response-time，则以接口模式下配置的值为准





范例 :

配置MLD协议发送查询消息时携带的max response time时间值：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#query-max-response-time 20





相关命令 :

无 




## query-max-response-time 


query-max-response-time 




命令功能 :

配置MLD协议发送查询消息时携带的max response time时间值，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






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

缺省为10秒 






使用说明 :

可以在以下模式下配置query-max-response-time：1. MLD模式/MLD-VRF模式2. MLD接口模式/MLD-VRF接口模式1、2模式下都配置query-max-response-time，则以接口模式下配置的值为准





范例 :

配置MLD协议发送查询消息时携带的max response time时间值：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#query-max-response-time 20





相关命令 :

无 




## query-max-response-time 


query-max-response-time 




命令功能 :

配置MLD协议发送查询消息时携带的max response time时间值，使用no命令恢时间值。 






命令模式 :

 MLD模式  






命令默认权限级别 :

15 






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

缺省为10秒 






使用说明 :

MLD接口配置模式下也有query-max-response-time命令，当MLD接口模式下没有配置这条命令，则MLD模式下的配置生效。





范例 :

配置MLD协议发送查询消息时携带的max response time时间值：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#query-max-response-time 20





相关命令 :

无 




## query-max-response-time 


query-max-response-time 




命令功能 :

配置MLD协议发送查询消息时携带的max response time时间值，使用no命令恢时间值。 






命令模式 :

 MLD-VRF模式  






命令默认权限级别 :

15 






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

MLD-VRF接口配置模式下也有query-max-response-time命令，当MLD-VRF接口模式下没有配置这条命令，则MLD-VRF模式下的配置生效。





范例 :

配置MLD协议发送查询消息时携带的max response time时间值：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#query-max-response-time 20





相关命令 :

无 




## register-holdtime 


register-holdtime 




命令功能 :

设置路由器收不到注册停止保持注册状态的时间，使用no命令关闭。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

设置路由器收不到注册停止保持注册状态的时间为70秒： ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#route pim ZXROSNG(config-mcast-ipv6-pim)#register-holdtime 70





相关命令 :

无 




## register-holdtime 


register-holdtime 




命令功能 :

设置路由器收不到注册停止保持注册状态的时间，使用no命令关闭。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#register-holdtime 70






相关命令 :

无 




## register-probe-interval 


register-probe-interval 




命令功能 :

设置路由器向RP发送注册探索消息的时间间隔。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



register-probe-interval 
  ＜seconds 
＞

no register-probe-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|设置向RP发送注册探索消息的时间间隔，范围：1–210，单位：秒, 默认5秒








缺省 :

不设置发送注册探索消息的时间间隔。 






使用说明 :

此命令用来配置组播源侧DR向RP发送注册探索（空注册）消息的时间间隔。设置的发送注册探索消息的时间间隔必须小于保持注册抑制状态的时间间隔的一半。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#register-probe-interval 10






相关命令 :

register-suppression-interval：设置路由器保持注册抑制状态。 




## register-probe-interval 


register-probe-interval 




命令功能 :

设置路由器向RP发送注册探索消息的时间间隔。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



register-probe-interval 
  ＜seconds 
＞

no register-probe-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|设置向RP发送注册探索消息的时间间隔，范围：1–210，单位：秒, 默认5秒








缺省 :

不设置发送注册探索消息的时间间隔。 






使用说明 :

此命令用来配置组播源侧DR向RP发送注册探索（空注册）消息的时间间隔。设置的发送注册探索消息的时间间隔必须小于保持注册抑制状态的时间间隔的一半。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#register-probe-interval 10






相关命令 :

register-suppression-interval：设置路由器保持注册抑制状态。 




## register-source 


register-source 




命令功能 :

通过配置此命令，修改注册报文的源地址。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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

没有配置register-source 






使用说明 :

1.如果配置的接口没有global地址或接口down或no ipv6 enable，则注册报文的源地址采用默认值，即直连源的DR地址。2.如果配置的接口是up且ipv6 enable，且有多个global地址，则取该接口上最小的global地址。3.在配置register-source命令时，会校验指定接口绑定的vpn与当前实例的vpn是否一致，如果不一致，则配置不成功。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#register-source gei-0/1/0/7





相关命令 :

router pim 




## register-source 


register-source 




命令功能 :

通过配置此命令，修改注册报文的源地址。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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

没有配置register-source 






使用说明 :

1.如果配置的接口没有global地址或接口down或no ipv6 enable，则注册报文的源地址采用默认值，即直连源的DR地址。2.如果配置的接口是up且ipv6 enable，且有多个global地址，则取该接口上最小的global地址。3.在配置register-source命令时，会校验指定接口绑定的vpn与当前实例的vpn是否一致，如果不一致，则配置不成功。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#register-source gei-0/1/0/7






相关命令 :

router pim 




## register-suppression-interval 


register-suppression-interval 




命令功能 :

设置路由器保持注册抑制状态的时间间隔。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



register-suppression-interval 
  ＜seconds 
＞

no register-suppression-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|设置路由器保持注册抑制状态的时间间隔，范围：60–3600，单位：秒, 默认60秒








缺省 :

不设置保持注册抑制状态的时间间隔。 






使用说明 :

当组播源测DR收到RP发来的注册停止报文后，会立即停止发送注册报文，进入注册抑制状态。此命令就是用来配置保持注册抑制状态的超时时间。设置的保持注册抑制状态的时间间隔必须大于发送注册探索消息的时间间隔的两倍。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#register-suppression-interval 70






相关命令 :

register-probe-interval：路由器向RP发送注册探索消息的时间间隔。 




## register-suppression-interval 


register-suppression-interval 




命令功能 :

设置路由器保持注册抑制状态的时间间隔。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



register-suppression-interval 
  ＜seconds 
＞

no register-suppression-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|设置路由器保持注册抑制状态的时间间隔，范围：60–3600，单位：秒, 默认60秒








缺省 :

不设置保持注册抑制状态的时间间隔。 






使用说明 :

当组播源测DR收到RP发来的注册停止报文后，会立即停止发送注册报文，进入注册抑制状态。此命令就是用来配置保持注册抑制状态的超时时间。设置的保持注册抑制状态的时间间隔必须大于发送注册探索消息的时间间隔的两倍。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#register-suppression-interval 70






相关命令 :

register-probe-interval：路由器向RP发送注册探索消息的时间间隔。 




## reject-inbound-data 


reject-inbound-data 




命令功能 :

禁止转发面接收组播数据报文，组播路由器不能在指定接口上接收组播数据报文。 






命令模式 :

 IPv6-组播模式  






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

1.通过配置<interface-name>指定接口不接收组播数据报文。 






范例 :

配置禁止转发面在接口上接收组播数据报文ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#reject-inbound-data gei-0/1/0/1






相关命令 :

ipv6 multicast-routing 




## require-alert-options 


require-alert-options 




命令功能 :

丢弃IPv6头中不包含Router_Alert_Options告警选项的MLD报文。通过no命令取消限制，恢复默认状态。 






命令模式 :

 MLD模式  






命令默认权限级别 :

15 






命令格式 :



require-alert-options 
 

no require-alert-options 








命令参数解释 :


					无
				 






缺省 :

缺省状态下，不检查IPv6报文头中的Router_Alert_Options告警选项，即路由器可以处理IPv6头部不包含Router_Alert_Options告警选项的MLD报文。 






使用说明 :

使用该命令让路由器丢弃IPv6头中不包含Router_Alert_Options告警选项的MLD报文 






范例 :

ZXROSNG(config)#ipv6 multicast-routing ZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#require-alert-options





相关命令 :

无 




## require-alert-options 


require-alert-options 




命令功能 :

丢弃IPv6头中不包含Router_Alert_Options告警选项的MLD报文。通过no命令取消限制，恢复默认状态。 






命令模式 :

 MLD-VRF模式  






命令默认权限级别 :

15 






命令格式 :



require-alert-options 
 

no require-alert-options 








命令参数解释 :


					无
				 






缺省 :

缺省状态下，不检查IPv6报文头中的Router_Alert_Options告警选项，即路由器可以处理IPv6头部不包含Router_Alert_Options告警选项的MLD报文。 






使用说明 :

使用该命令让路由器丢弃IPv6头中不包含Router_Alert_Options告警选项的MLD报文 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#require-alert-options





相关命令 :

无 




## robustness-count 


robustness-count 




命令功能 :

配置允许子网丢包的次数，使用no命令恢复缺省值。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






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

1.当鲁棒变量为n，允许丢包的次数为n-1。2.MLD模式下也有robustness-count命令，当MLD接口模式下没有配置这条命令，则MLD模式下的配置生效。






范例 :

配置允许丢包的次数为4：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#robustness-count 5





相关命令 :

无 




## robustness-count 


robustness-count 




命令功能 :

配置允许子网丢包的次数，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






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

无 






使用说明 :

1.当鲁棒变量为n，允许丢包的次数为n-1。2.MLD-VRF配置模式下也有robustness-count命令，当MLD-VRF接口模式下没有配置这条命令，则MLD-VRF模式下的配置生效。






范例 :

配置允许丢包的次数为4：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#robustness-count 5





相关命令 :

无 




## robustness-count 


robustness-count 




命令功能 :

配置允许子网丢包的次数，使用no命令恢复缺省值 






命令模式 :

 MLD模式  






命令默认权限级别 :

15 






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

无 






使用说明 :

1.当鲁棒变量为n，允许丢包的次数为n-1。2.MLD接口配置模式下也有robustness-count命令，当MLD接口模式下没有配置这条命令，则MLD模式下的配置生效。






范例 :

配置允许丢包的次数为4：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#robustness-count 5





相关命令 :

无 




## robustness-count 


robustness-count 




命令功能 :

配置允许子网丢包的次数，使用no命令恢复缺省值 






命令模式 :

 MLD-VRF模式  






命令默认权限级别 :

15 






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

1.当鲁棒变量为n，允许丢包的次数为n-1。2.MLD-VRF接口配置模式下也有robustness-count命令，当MLD-VRF接口模式下没有配置这条命令，则MLD-VRF模式下的配置生效。






范例 :

配置允许丢包的次数为4：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#robustness-count 5





相关命令 :

无 




## router mld 


router mld 




命令功能 :

进入MLD配置模式，与MLD协议开启无关，协议开启由ipv6 multicast-routing控制，使用no命令删除MLD所有配置，使用默认配置。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



router mld 
 

no router mld 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

没有配置ipv6 multicast-routing，router mld命令无效。 






范例 :

进入MLD组播配置模式：ZXROSNG(config-mcast-ipv6)#router mld





相关命令 :

无 




## router mld 


router mld 




命令功能 :

进入MLD-VRF配置模式，与MLD协议开启无关，协议开启由ipv6 multicast-routing控制，使用no命令删除MLD所有配置，使用默认配置。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



router mld 
 

no router mld 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

没有配置ipv6 multicast-routing，router mld命令无效。 






范例 :

进入MLD-VRF配置模式：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mld






相关命令 :

无 




## router pim 


router pim 




命令功能 :

启用IPv6组播协议PIM，使用no命令关闭IPv6 PIM。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



router pim 
 

no router pim 








命令参数解释 :


					无
				 






缺省 :

不启用IPv6组播协议PIM。 






使用说明 :

1. 默认不启用IPv6 PIM，没有启用IPv6 PIM时IPv6 PIM相关命令将不可用。2. 启用IPv6 PIM后进入PIM6配置模式。3. 没有配置ipv6 multicast-routing，IPv6 PIM路由协议无法运行。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim 






相关命令 :

interface：进入PIM6接口配置模式。 




## router pim 


router pim 




命令功能 :

启用IPv6组播协议PIM，使用no命令关闭IPv6 PIM。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



router pim 
 

no router pim 








命令参数解释 :


					无
				 






缺省 :

不启用IPv6组播协议PIM。 






使用说明 :

1. 默认不启用IPv6 PIM，没有启用IPv6 PIM时IPv6 PIM相关命令将不可用。2. 启用IPv6 PIM后进入PIM6配置模式。3. 没有配置ipv6 multicast-routing，IPv6 PIM路由协议无法运行。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pim






相关命令 :

interface：进入PIM6接口配置模式。 




## rp-candidate 


rp-candidate 




命令功能 :

配置路由器使其通告自己为候选RP，使用no命令取消该路由器作为RP的候选者。 






命令模式 :

 IPv6-PIM-VRF模式,IPv6-PIM模式  






命令默认权限级别 :

IPv6-PIM模式:15,IPv6-PIM-VRF模式:15 






命令格式 :


rp-candidate 
  ＜ipv6-address 
＞ [{[group-list 
 ＜prefix-list-name 
＞],[priority 
 ＜priority 
＞],[holdtime 
 ＜seconds 
＞]}]
no rp-candidate 
  ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|接口的地址，为X:X::X:X形式
＜prefix-list-name＞|定义了一个组范围，该范围是被通告RP服务范围
＜priority＞|候选RP优先级，缺省为192，范围：0–255
＜seconds＞|保持时间，范围：150–65535，单位：秒。








缺省 :

本地不为候选RP，holdtime默认值150秒。 






使用说明 :

1. 候选RP的缺省优先级为192，优先级数值较小的候选RP优先；如果优先级数值相同，则比较hash值，hash值大的RP优先；如果hash值相同，则比较地址，地址大的RP优先。2. 推荐用户将候选RP配置在loopback接口上，从而减少由于物理接口up/down造成的网络震荡。3. 如果该命令不带 <prefix-list-name >参数，表明该候选RP为所有组服务。4．候选RP的holdtime配置的时间必须大于或等于BSM消息发送周期的2.5倍。






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#rp-candidate 2::2 priority 180 holdtime 190






相关命令 :

show ipv6 pim bsr：查看BSR配置信息。 




## rpf-proxy-vector path-list 


rpf-proxy-vector path-list 




命令功能 :

配置RPF迭代路径列表。 






命令模式 :

 IPv6-组播模式  






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
＜path-address＞|路径地址，X:X::X:X形式
loose|稀疏模式
strict|严格模式








缺省 :

无 






使用说明 :

1. 同一实例下最多配置100个路径列表名称。2. 同一路径列表名称下最多配置10条路径地址。3. 同一路径列表名称下不能配置相同的路径地址。4. RPF向量路径列表功能生效需要在PIM实例下使能hello-join-attribute命令。






范例 :

ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast-ipv6)# rpf-proxy-vector path-list a index 1 10::20 strict  






相关命令 :

nexthophello-join-attribute




## rp-proxy 


rp-proxy 




命令功能 :

配置rp-proxy的路由器在本地RP信息与J/P报文中的RP不一致时也正常处理J/P报文。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



rp-proxy 
 

no rp-proxy 








命令参数解释 :


					无
				 






缺省 :

默认处理J/P报文时检查RP信息，若与本地RP信息不一致，则丢弃J/P报文。





使用说明 :

1.配置rp-proxy的路由器在本地RP信息与J/P报文中的RP不一致时也正常处理J/P报文；不配置此命令则发现本地RP信息与J/P报文中的RP不一致时就丢弃J/P报文。 






范例 :

配置rp-proxy：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#rp-proxy






相关命令 :

无 




## rp-proxy 


rp-proxy 




命令功能 :

配置rp-proxy的路由器在本地RP信息与J/P报文中的RP不一致时也正常处理J/P报文。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



rp-proxy 
 

no rp-proxy 








命令参数解释 :


					无
				 






缺省 :

默认处理J/P报文时检查RP信息，若与本地RP信息不一致，则丢弃J/P报文。





使用说明 :

1.配置rp-proxy的路由器在本地RP信息与J/P报文中的RP不一致时也正常处理J/P报文；不配置此命令则发现本地RP信息与J/P报文中的RP不一致时就丢弃J/P报文。 






范例 :

配置rp-proxy：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#rp-proxy






相关命令 :

无 




## rp-smart 


rp-smart 




命令功能 :

启用RP智能切换。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



rp-smart 
 

no rp-smart 








命令参数解释 :


					无
				 






缺省 :

不启用RP智能切换。 






使用说明 :

1.如果配置了rp-smart，则配置静态RP时要检查到这个地址有没有单播路由，没有就不创建这个静态RP。 






范例 :

配置rp-smart：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#rp-smart






相关命令 :

无 




## rp-smart 


rp-smart 




命令功能 :

启用RP智能切换。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



rp-smart 
 

no rp-smart 








命令参数解释 :


					无
				 






缺省 :

不启用RP智能切换。 






使用说明 :

1.如果配置了rp-smart，则配置静态RP时要检查到这个地址有没有单播路由，没有就不创建这个静态RP。 






范例 :

配置rp-smart：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#rp-smart






相关命令 :

无 




## set-dscp-outer 


set-dscp-outer 




命令功能 :

设置组播协议数据包TOS优先级。 






命令模式 :

 IPv6-组播模式  






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

把组播协议数据包tos优先级设置为1：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#set-dscp-outer 1  





相关命令 :

无 




## show debug ipv6-mvpn 


show debug ipv6-mvpn 




命令功能 :

显示开启的ipv6-mvpn debug开关。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug ipv6-mvpn 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

查看开启了哪些ipv6-mvpn debug开关。 






范例 :

显示开启的ipv6-mvpn debug开关：ZXROSNG#show debug ipv6-mvpnIPv6 MVPN:  IPv6 MVPN debugging is on  IPv6 MVPN (VPN zte) debugging is on





相关命令 :

debug ipv6 mvpn alldebug ipv6 mvpn



## show debug mld 


show debug mld 




命令功能 :

查看MLD协议所有打印消息开关是否开启。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug mld 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

查看MLD协议所有打印消息开关是否开启:show debug mld;






范例 :

查看MLD的debug开关开启的情况：ZXROSNG#show debug mldMLD:  MLD debugging is on  MLD permit group (ff88::1) debugging is on  MLD permit interface (loopback1) debugging is on





相关命令 :

无 




## show debug mroute6 


show debug mroute6 




命令功能 :

显示IPv6组播debug选项状态。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug mroute6 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令会将包括私网和公网的所有打开的debug信息全部显示出来。 






范例 :

显示IPv6组播debug选项状态：ZXROSNG#show debug mroute6MROUTE6:  MROUTE6 debugging is on





相关命令 :

无 




## show debug pim6 


show debug pim6 




命令功能 :

显示开启的IPv6 PIM debug开关。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug pim6 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

查看开启了哪些IPv6 PIM debug开关。 






范例 :

ZXROSNG#show debug pim6IPv6 PIM:  IPv6 PIM register debugging is on  IPv6 PIM packet send debugging is on






相关命令 :

debug ipv6 pim：设置IPv6 PIM相关信息的调试开关。 




## show error packet ipv6 pim statistics 


show error packet ipv6 pim statistics 




命令功能 :

显示IPv6 PIM协议模块收到的错误报文统计信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show error packet ipv6 pim statistics 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

显示IPv6 PIM各协议报文在所有实例下分别累计的错误报文计数。 






范例 :

1.显示PIM协议模块收到的错误报文统计信息：ZXROSNG(config)#sho error packet ipv6 pim statistics IPv6 PIM error packets:Hello:2Register:413Register-Stop:0Join/Prune:0Bootstrap:0Assert:0Graft:0Graft-Ack:0C-RP-Ad:0State-Refresh:0DF-Election:0ECMP-Redirect:0PFM-GSH-TLV:0显示信息说明：Hello：错误Hello报文的累计个数；Register：错误Register报文的累计个数；Register-Stop：错误Register-Stop报文的累计个数；Join/Prune：错误Join/Prune报文的累计个数；Bootstrap：错误BSM报文的累计个数；Assert：错误Assert报文的累计个数；Graft：错误Graft报文的累计个数；Graft-Ack：错误Graft-Ack报文的累计个数；C-RP-Ad：错误C-RP通告报文的累计个数；State-Refresh：错误State-Refresh报文的累计个数；DF-Election：错误DF-Election报文的累计个数；ECMP-Redirect：错误ECMP重定向报文的累计个数；PFM-GSH-TLV：错误PFM-GSH报文的累计个数；






相关命令 :

error packet ipv6 pim record{disable|enable[<number>]} 




## show error packet ipv6 pim 


show error packet ipv6 pim 




命令功能 :

显示IPv6 PIM协议模块最近收到的错误报文。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show error packet ipv6 pim 
  [vrf 
 ＜vrf-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1-32个字符








缺省 :

无 






使用说明 :

1.不指定参数。显示所有实例的IPv6 PIM协议模块最近收到的错误报文。2.指定vrf-name，显示实例名为vrf-name的IPv6 PIM协议模块最近收到的错误报文。






范例 :

1.不指定参数显示所有的IPv6 PIM协议模块最近收到的错误报文：ZXROSNG(config)#show error packet ipv6 pim Packet Index : 1Record Time  : 2016-3-17 23:30:32Interface    : gei-0/20/0/1Instance     : vrf zte1Length       : 28Error Reason : Register multicast address error0000: 21  00  be  ff  00  00  00  00  65  00  00  64  7c  28  00  00 0010: 1f  11  33  5d  0a  01  01  01  e0  01  01  01---------------------------------------------------------------------Packet Index : 2Record Time  : 2016-3-17 23:30:31Interface    : gei-0/20/0/1Instance     : vrf zte1Length       : 6Error Reason : Register packet length error0000: 21  00  de  ff  00  00 ---------------------------------------------------------------------Packet Index : 3Record Time  : 2016-3-17 22:57:35Interface    : gei-0/20/0/2Instance     : globalLength       : 2Length       : 70Error Reason : Hello checksum error0000: 20  00  00  00  00  01  00  02  00  46  00  02  00  04  01  f4 0010: 09  c4  00  13  00  04  00  00  00  0a  00  14  00  04  63  de 0020: f0  02  00  15  00  04  01  3c  00  00  00  16  00  00  00  1a 0030: 00  00  ff  dd  00  06  01  00  64  01  01  0a  00  18  00  06 0040: 01  00  01  02  03  04  ---------------------------------------------------------------------2.指定vrf-name显示IPv6 PIM协议模块最近收到的错误报文：ZXROSNG(config)#show error packet ipv6 pim vrf zte1Packet Index : 1Record Time  : 2016-3-17 23:30:32Interface    : gei-0/20/0/1Instance     : vrf zte1Length       : 28Error Reason : Register multicast address error0000: 21  00  be  ff  00  00  00  00  65  00  00  64  7c  28  00  00 0010: 1f  11  33  5d  0a  01  01  01  e0  01  01  01---------------------------------------------------------------------Packet Index : 2Record Time  : 2016-3-17 23:30:31Interface    : gei-0/20/0/1Instance     : vrf zte1Length       : 6Error Reason : Register packet length error0000: 21  00  de  ff  00  00 ---------------------------------------------------------------------显示信息说明：Packet Index：报文序号；Record Time：记录时间；Interface：收到错误报文的接口名称；Instance：收到错误报文的实例名称；Length：从PIM头开始计算的错误报文长度；Error Reason：错误原因；0000：该字段后面的内容是从PIM头开始记录的错误报文内容。






相关命令 :

error packet ipv6 pim record{disable|enable[<number>]} 




## show ipv6 mld groups summary 


show ipv6 mld groups summary 




命令功能 :

查看各个接口上MLD动态组和静态组数目的总和。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mld groups summary 
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

查看公网各个接口上MLD动态组和静态组数目的总和：show ipv6 mld groups summary;查看私网各个接口上MLD动态组和静态组数目的总和：show ipv6 mld groups summary <vrf-name>;






范例 :

显示各个接口上MLD动态组和静态组数目的总和： ZXROSNG#show ipv6 mld groups summary MLD groups summary:Interface           Static    Joined    Total     gei-0/1/0/1         0         0         0         gei-0/1/0/2         6         0         6         Summary             6         0         6





相关命令 :

无 




## show ipv6 mld groups 


show ipv6 mld groups 




命令功能 :

显示通过MLD协议学习到和路由器直连的组播组加入情况。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mld groups 
  [vrf 
 ＜vrf-name 
＞] [{[＜interface-name 
＞],[＜group-address 
＞]}] [detail 
] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜interface-name＞|接口的名称
＜group-address＞|IPv6格式的组播组地址，X:X::X:X形式
detail|显示MLD v2的源列表等细节信息








缺省 :

无 






使用说明 :

查看私网MLD组加入情况：show ipv6 mld groups vrf[<vrf-name>];查看私网指定接口上的MLD组加入情况： show ipv6 mld groups vrf[<vrf-name>][<interface-name>];查看私网MLD组加入的源列表等细节信息：show ipv6 mld groups vrf[<vrf-name>] detail;查看私网指定接口上的MLD组加入的源列表等细节信息：show ipv6 mld groups vrf[<vrf-name>][<interface-name>] detail;查看公网MLD组加入情况：show ipv6 mld groups;查看公网指定接口上的MLD组加入情况：show ipv6 mld groups [<interface-name>];查看公网MLD组加入的源列表等细节信息：show ipv6 mld groups detail;查看公网指定接口上的MLD组加入的源列表等细节信息：show ipv6 mld groups [<interface-name>] detail;





范例 :

查看接口上MLD组加入情况：ZXROSNG(config)#show ipv6 mld groups Total: 2 groupsGroup Address : ff84::1Last Reporter : ::             --最近一次的通告成员    Interface : gei-0/1/0/1       Uptime : 00:02:14       --存在时间         Expire : never          --超时时间Group Address : ff84::2Last Reporter : fe80::2ee:ffff:fe30:1000    Interface : gei-0/1/0/2       Uptime : 00:00:08       Expire : never





相关命令 :

无 




## show ipv6 mld interface 


show ipv6 mld interface 




命令功能 :

查看接口上MLD配置情况。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mld interface 
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

查看公网所有接口的MLD配置情况：show ipv6 mld interface；查看公网指定接口的MLD配置情况：show ipv6 mld interface [＜interface-name＞]；查看私网指定vrf实例下所有接口的MLD配置情况：show ipv6 mld interface vrf[<vrf-name>]；查看私网指定vrf实例下指定接口的MLD配置情况：show ipv6 mld interface vrf[<vrf-name>][＜interface-name＞]；





范例 :

查看接口上MLD配置情况：ZXROSNG#show ipv6 mld interfacegei-0/1/0/10Internet address is fe80::2e0:d0ff:fe21:203MLD is enabled on interfaceCurrent MLD version is 2     --MLD版本MLD query interval is 125 seconds  --查询间隔MLD last member query interval is 1 seconds --最后成员查询间隔MLD query max response time is 10 seconds  --最大响应时间MLD querier timeout period is 255 seconds  --查询器超时时间MLD robustness variable is 2  --鲁棒变量MLD querier is fe80::2e0:d0ff:fe21:203, never  expire  --当前查询器Inbound MLD access group is not setMLD immediate leave control is not set --是否启用立即离开机制MLD maximum joins is not setMLD access IP source is not setZXROSNG(config)#sho ipv6 mld interface vrf ztemvpn_tunnel1  Internet address is ::ffff:1.1.1.20  MLD is enabled on interface  Current MLD version is 2  MLD query interval is 125 seconds  MLD last member query interval is 1 seconds  MLD query max response time is 10 seconds  MLD querier timeout period is 255 seconds  MLD robustness variable is 2  MLD querier is ::ffff:1.1.1.20, never expire  Inbound MLD access group is not set  MLD immediate leave control is not set  MLD maximum joins is not set  MLD access IP source is not set





相关命令 :

versionquery-intervallast-member-query-intervalquery-max-response-timequerier-timeoutrobustness-variablequerier-electionaccess-groupimmediate-leave



## show ipv6 mld packet-count 


show ipv6 mld packet-count 




命令功能 :

查看MLD协议报文接收和发送的统计计数。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mld packet-count 
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

查看公网所有使能PIM协议的接口，MLD协议报文接收和发送统计计数：show ipv6 mld packet-count；查看公网指定接口MLD协议报文接收和发送统计计数：show ipv6 mld packet-count <interface-name>;查看私网所有使能PIM协议的接口接口MLD协议报文接收和发送统计计数：show ipv6 mld packet-count <vrf-name>查看私网指定接口MLD协议报文接收和发送统计计数：show ipv6 mld packet-count <vrf-name> <interface-name>





范例 :

查看指定接口vlan23上MLD协议报文接收和发送的统计计数：ZXROSNG#show ipv6 mld packet-count vlan23                                                                                      MLD Packet Counts:Received/Sent                                                                                                     Interface:vlan23                                                                                                                      Query:1558/319  Done:0/0                                                                                                            ReportV1:0/0  ReportV2:0/0                                                                                                          Spec-Query:0/0  Grp-Src-Query:0/0                                                                                                   Dropped:0/0  Invalid:0/0                                                                                                            Total:1558/319   Current Time:  2019-09-25 18:17:38






相关命令 :

无 




## show ipv6 mroute brief 


show ipv6 mroute brief 




命令功能 :

显示IP组播路由表的简要情况。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mroute brief 
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

1.查看具体哪个VRF实例下的组播路由情况，可采用<vrf-name>来指定，不指定则显示公网的； 






范例 :

 显示IP组播路由表的简要情况：ZXROSNG#show ipv6 mroute brief IPv6 Multicast Routing Table Brief(*, ff88::1), TYPE: DYNAMIC(*, ff88::2), TYPE: DYNAMIC(*, ff88::3), TYPE: DYNAMIC(*, ff88::4), TYPE: DYNAMIC(*, ff88::5), TYPE: DYNAMIC(*, ff88::6), TYPE: DYNAMIC





相关命令 :

无 




## show ipv6 mroute nexthop 


show ipv6 mroute nexthop 




命令功能 :

显示组播传输方向下一跳信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mroute nexthop 
  [vrf 
 ＜vrf-name 
＞] [＜ipv6-address 
＞] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜ipv6-address＞|目的地址








缺省 :

无 






使用说明 :

1.查看具体哪个VRF实例下的下一跳情况，可采用<vrf-name>来指定，不指定则显示公网的；2.查看到到某一特定目的地址的下一跳情况，可采用<ipv6-address>来指定






范例 :

ZXROSNG(config)# show ipv6 mroute nexthopIPv6 Multicast Nexthop TableNexthop flags and user: L:Local, C:Connect, CTOP:Across the backbone,UNR:Unreachable unicast, MSN:Multicast static nexthop, M:Master, S:SlaveDest address:1::1 00:27:40 PIM(RTM)MSTATIC nexthop:  Metric:1, Preference:1, Masklen:32, Flags:  RPF path list: abcMBGP nexthop:Metric:4294967295, Preference:0, Masklen:0, Flags:UNRECMP list:RTM nexthop:Metric:0, Preference:0, Masklen:128, Flags:LECMP list:Nexthop:1::1Oif:gei-0/1/0/1(M)Nhp:RelNhp:Dest address:3::3 00:02:04 PIM(MSN)MSTATIC nexthop:Metric:1, Preference:1, Masklen:64, Flags:Fallback: vrf zteMBGP nexthop:Metric:4294967295, Preference:0, Masklen:0, Flags:UNRECMP list:RTM nexthop:Metric:4294967295, Preference:0, Masklen:0, Flags:UNRECMP list:ZXROSNG#show ipv6 mroute nexthop vrf zteIPv6 Multicast Nexthop TableNexthop flags and user: L:Local, C:Connect, CTOP:Across the backbone,UNR:Unreachable unicast, MSN:Multicast static nexthop, M:Master, S:SlaveDest address:1::1 00:13:14 PIM(MSN)MSTATIC nexthop:Metric:1, Preference:1, Masklen:64, Flags:Fallback: IP globalMBGP nexthop:Metric:4294967295, Preference:0, Masklen:0, Flags:UNRECMP list:RTM nexthop:Metric:4294967295, Preference:0, Masklen:0, Flags:UNRECMP list:ZXROSNG(config)# show ipv6 mroute nexthop vrf zteIPv6 Multicast Nexthop TableNexthop flags and user: L:Local, C:Connect, CTOP:Across the backbone,UNR:Unreachable unicast, MSN:Multicast static nexthop, M:Master, S:SlaveDest address:80::2 14:27:12 PIM(RTM)  MBGP nexthop:  Metric:4294967295, Preference:200, Masklen:120, Flags:UNR  ECMP list:  RTM nexthop:  Metric:0, Preference:200, Masklen:120, Flags:CTOP  ECMP list:    Nexthop:::ffff:1.1.1.10    Oif:mvpn_tunnel1(M)    Nhp:::    RelNhp:::显示信息说明：L：表示本地。C：表示连接。CTOP：表示跨主干网。UNR：单播不可达。MSN：组播静态配置的下一跳。M：主路由。S：备路由。Dest address：目的地址。Metric：下一跳的路由度量值。Preference：下一跳的路由优先级。Masklen：掩码。Flags：标记位。ECMP list：ECMP列表。Fallback：IP global表示下一跳是公网实例，vrf zte表示下一跳是私网zte实例。RPF path list：RPF路径列表。






相关命令 :

无 




## show ipv6 mroute summary all-instance 


show ipv6 mroute summary all-instance 




命令功能 :

显示IPv6组播所有实例的路由表总数的具体数目。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mroute summary all-instance 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

显示IPv6组播所有实例的路由表总数的具体数目：ZXROSNG#show ipv6 mroute summary all-instanceIPv6 multicast routing table summary(*,G): 6 routes(S,G): 0 routesTotal: 6 routes显示信息说明：(*,G)：表示配置的组播(*,G)条目数；(S,G)：表示配置的组播(S,G)条目数；Total：表示配置的组播(*,G) 和(S,G)条目数总和。






相关命令 :

show ipv6 mroute summary 




## show ipv6 mroute summary 


show ipv6 mroute summary 




命令功能 :

显示IP组播路由表的具体数目。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mroute summary 
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
＜vrf-name＞|VRF名称，长度为1–32个字符
＜in-interface-name＞|入接口名
＜out-interface-name＞|出接口名








缺省 :

无 






使用说明 :

1.查看具体哪个VRF实例下的路由数目，可采用<vrf-name>来指定，不指定则显示公网的；2.可指定入接口或出接口查询路由数目。






范例 :

 显示IP组播路由表的具体数目：ZXROSNG#show ipv6 mroute summary IPv6 multicast routing table summary   (*,G): 6 routes   (S,G): 0 routes   Total: 6 routes





相关命令 :

无 




## show ipv6 mroute 


show ipv6 mroute 




命令功能 :

显示IP组播路由表的内容。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mroute 
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
＜vrf-name＞|VRF名称，长度为1–32个字符
＜group-address＞|组地址，X:X::X:X 形式
＜source-address＞|源地址，X:X::X:X形式
＜source-address＞|源地址，X:X::X:X形式
＜in-interface-name＞|入接口名
＜out-interface-name＞|出接口名








缺省 :

无 






使用说明 :

1. 如果没有可选项，则显示所有的组播路由表。2. 如果增加组选项，则显示该组（*，g）和所有相关的（s，g）路由条目。3. 如果增加组和源地址选项，则显示特定的（s，g）路由条目。4. 如果使用vrf-name参数，可以指定显示某个vrf下的路由条目5. 如果增加入接口或出接口选项，则显示特定入接口或出接口的路由条目。






范例 :

显示IP组播路由表的内容：ZXROSNG(config)#show ipv6 mrouteIPv6 Multicast Routing TableFlags:NS:SPT upsend,RT:Reg upsend,F:Forward,NTP:NTP join,DPU:Damping enable,DPD:Damping del,SU:Slave in use,(*, ff88::1)  TYPE: DYNAMIC, FLAGS:  RP: 1::1  Incoming interface: NULL, flags:  Outgoing interface list: 1    gei-0/1/0/1.3, flags: F(*, ff88::2)  TYPE: DYNAMIC, FLAGS:  RP: 1::1  Incoming interface: NULL, flags:  Outgoing interface list: 1    gei-0/1/0/1.3, flags: F(*, ff88::3)  TYPE: STATIC, FLAGS: SU  RP: ::  Incoming interface: gei-0/1/0/1, flags:  Secondary RPF interface: gei-0/1/0/2  Outgoing interface list: 2    gei-0/1/0/3, flags: F    gei-0/1/0/1, flags: F(3::3, ffe7::1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: using vrf zte, flags: NS  Outgoing interface list: 1    loopback1, flags: F/S(1::1, ffee::1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: loopback1, flags: NS  Outgoing interface list: 0  Fallback extranet receivers: 1    vrf zteZXROSNG#show ipv6 mroute vrf zteIPv6 Multicast Routing TableFlags:NS:SPT upsend,RT:Reg upsend,F:Forward,NTP:NTP join,DPU:Damping enable,DPD:Damping del,SU:Slave in use,(3::3, ffe7::1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: gei-0/20/0/3, flags: NS  Outgoing interface list: 0  Fallback extranet receivers: 1    IP global(1::1, ffee::1)  TYPE: DYNAMIC, FLAGS: NS  Incoming interface: using global, flags: NS  Outgoing interface list: 1    gei-0/20/0/3, flags: F/S显示信息说明：TYPE：条目类型，DYNAMIC表示动态，STATIC表示静态；FLAGS：表示路由上标记位；RP：表示路由条目对应的RP地址；Incoming interface：表示条目入接口，后面flags表示接口标记位；Secondary RPF interface：表示条目备入接口；Outgoing interface list：表示条目出接口列表，后面flags表示接口标记位。using global：表示组播路由上游实例名称。当上游是公网实例，显示using global。using vrf zte：表示组播路由上游实例名称。当上游是私网实例zte，显示using vrf zte。Fallback extranet receivers：表示Fallback扩展的接收者信息，后面接IP global表示是公网实例，接vrf zte表示是私网zte。






相关命令 :

无 




## show ipv6 multicast-static-interface 


show ipv6 multicast-static-interface 




命令功能 :

显示IPv6静态组播出接口列表 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 multicast-static-interface 
  [vrf 
 ＜vrf-name 
＞] [index 
 ＜index 
＞] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|实例名，长度1–32字符
＜index＞|显示指定索引号的出接口列表，范围1-100








缺省 :

缺省显示所有出接口列表 






使用说明 :

1.查看指定VRF实例的出接口情况，可以通过vrf-name来指定。2.查看指定索引号的出接口情况，可以通过index来指定。3.没有指定索引号则显示所有出接口。






范例 :

1．显示公网静态组播出接口列表：ZXROSNG#show ipv6 multicast-static-interfaceStatic6 multicast out port index 1:  Outgoing Interface:    gei-0/1/0/1Static6 multicast out port index 2:  Outgoing Interface:loopback12． 显示公网指定出接口索引号为1的出接口列表：ZXROSNG#show ipv6 multicast-static-interface index 1Static6 multicast out port index 1:  Outgoing Interface:    gei-0/1/0/13．显示私网静态组播出接口列表：ZXROSNG#show ipv6 multicast-static-interface vrf zteStatic6 multicast out port index 1:  Outgoing Interface:    gei-0/1/0/7
Static6 multicast out port index 2:  Outgoing Interface:    Loopback24．显示私网指定出接口索引号为1的出接口列表：ZXROSNG#show ipv6 multicast-static-interface vrf zte  index 1Static6 multicast out port index 1:  Outgoing Interface:    gei-0/1/0/7






相关命令 :

ipv6 multicast-static-interface 




## show ipv6 multicast-static-route 


show ipv6 multicast-static-route 




命令功能 :

显示IPv6静态组播路由表和路由表统计信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 multicast-static-route 
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
＜group-address＞|组播组地址，为X:X::X:X形式
＜source-address＞|组播源地址，为X:X::X:X形式
＜source-address＞|组播源地址，为X:X::X:X形式
summary|显示路由表统计信息








缺省 :

缺省显示所有静态组播路由表。 






使用说明 :

可以通过此命令查看指定VRF实例、指定源静态组播路由、指定组静态组播路由和指定源组静态组播路由，及静态组播路由表统计信息。 






范例 :

1. 显示公网静态组播路由表：ZXROSNG#show ipv6 multicast-static-routeThe Capability of Static Multicast6 Route(*, g) 10, (s, g) 10IPv6 Multicast Static Routing TableFlags: A- Available, F- Forward, N- Not available, W- Wait to restore(1::1，ff88::1)  Incoming interface: gei-0/1/0/1  A/W  Track name: a  Secondary RPF interface: gei-0/1/0/2  A  Track name: b  Outgoing interface list:loopback1  F显示信息说明：(*, g)：表示(*, g)最大可配条目数；(s, g)：表示(s, g)最大可配条目数；Incoming interface：表示条目主入接口；Secondary RPF interface：表示条目备入接口；Track name：表示条目主备入接口关联检测的track名；Outgoing interface list：表示条目出接口列表。2. 显示公网静态组播路由表统计信息：ZXROSNG#show ipv6 multicast-static-route summaryIPv6 Static Multicast Routing Table Summary(*,G): 0 routes(S,G): 1 routesTotal: 1 routes
显示信息说明：(*,G)：表示配置的(*,G)条目数；(S,G)：表示配置的(S,G)条目数；Total：表示配置的(*,G) 和(S,G)条目数总和。3. 显示私网静态组播路由表：ZXROSNG#show ipv6 multicast-static-route vrf zteThe Capability of Static Multicast6 Route(*, g) 10, (s, g) 10IPv6 Multicast Static Routing TableFlags: A- Available, F- Forward, N- Not available, W- Wait to restore(1::1，ff88::1)  Incoming interface: gei-0/1/0/7  A/W  Track name: a  Secondary RPF interface: gei-0/1/0/8  A  Track name: b  Outgoing interface list:    loopback2  FZXROSNG#4. 显示私网静态组播路由表统计信息：ZXROSNG#show ipv6 multicast-static-route  vrf zte summaryIPv6 Static Multicast Routing Table Summary(*,G): 0 routes(S,G): 1 routesTotal: 1 routes






相关命令 :

ipv6 multicast-static-route 




## show ipv6 mvpn ad-route summary 


show ipv6 mvpn ad-route summary 




命令功能 :

显示IPv6 MVPN AD路由统计信息 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mvpn ad-route summary 
 vrf 
 ＜vrf-name 
＞ 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称,1-32个字符








缺省 :

无 






使用说明 :

1.可以指定VRF实例查看AD路由统计信息，使用<vrf-name>来指定实例，如果不指定，则显示公网的AD路由统计信息。 






范例 :

ZXROSNG#show ipv6 mvpn ad-route summary vrf zteType            Local     Received  Total     Intra-AS        1         0         1         Inter-AS        0         1         1         Spmsi-AD        0         0         0         Leaf-AD         0         0         0         Source Active   0         0         0         XG Join         0         10        10        SG Join         0         0         0         Total           1         11        12显示信息说明Type:AD路由类型Local:本地的路由个数Received:接收到的路由个数Intra-AS,Inter-AS,Spmsi-AD, Leaf-AD, Source Active, XG Join, SG Join:1~7型AD路由






相关命令 :

无 




## show ipv6 mvpn ad-route 


show ipv6 mvpn ad-route 




命令功能 :

显示IPv6 MVPN AD路由信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mvpn ad-route 
 vrf 
 ＜vrf-name 
＞ [{[group 
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
＜vrf-name＞|实例名，长度1–32字符
＜group-address＞|组地址，为X:X::X:X形式
＜source-address＞|源地址，为X:X::X:X形式
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

该命令显示相关隧道标签信息，可以在显示命令后面参数选项中指定需要的过滤信息，直接显示出来指定的路由信息 






范例 :

显示IPv6 MVPN路由信息：ZXROSNG#show ipv6 mvpn ad-route vrf zte1Flags: L- Local,R- Remote,J- Join Ptnl,S- Start Ptnl,T0- No PtnlT1- RSVP-TE,T2- mLDP-P2MP,T3- PIM-SSM,T4- PIM-SM,T5- PIM-BidirT6- Ingress-Replication,T7- mLDP-MP2MP,T11- BIERNLRI                                (P-tunl|Next Hop)/Flags[Type][Key]                         ((flags/type/label/id)|Next Hop)/Flags[1][1:1][1.1.1.1]                   (0/2/0/2:1001:1.1.1.1)/(S/T2/L)[1][1:1][2.2.2.2]                   (0/2/0/2:1000:2.2.2.2)/(J/T2/R)[6][1:1][108::20,ff88::1]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::2]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::3]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::4]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::5]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::6]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::7]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::8]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::9]           (2.2.2.2)/(R)[6][1:1][108::20,ff88::10]          (2.2.2.2)/(R)显示信息说明:参数    描述NLRI：网络层可达信息[Type]：AD路由类型[Key]： AD路由Key值, 对于不同类型的AD路由key值不同，1#路由key为[RD][origin IP]，2#路由key为[RD][AS]，3#路由key为[RD] [multicast source][multicast group] [origin IP]，4#路由key为[route key][origin IP]，5#路由key为[RD] [multicast source][multicast group],6#和7#的key都为[RD] [AS] [multicast source][multicast group]flags/type/label/id：flags表示是否需要生成4#路由，type表示隧道类型，label表示隧道标签，id表示隧道ID，只有1-4#路由才显示Next Hop：下一跳，只有5-7#路由才显示Flags：标记隧道类型以及AD路由相关属性L:本地路由R:远端路由J:标记是否加入远端隧道S:标记为隧道头节点T0--T11：隧道的8种类型






相关命令 :

provider-tunnel 




## show ipv6 mvpn instance 


show ipv6 mvpn instance 




命令功能 :

显示IPv6 MVPN的实例信息 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mvpn instance 
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

1.显示具体哪个VRF实例的MVPN信息，可采用<vrf-name>来指定，如果没有<vrf-name>选项，则设置所有私网的MVPN信息的调试开关； 






范例 :

显示IPv6 MVPN实例信息：ZXROSNG#show ipv6 mvpn instance vrf zte1MVPN name zte1     RD: 10:10     Import mcast RT: 1.1.1.20:40      Provider tunnel: mLDP-P2MP      Origin IP: 1.1.1.20  Routable,Local    TE ID: 1.1.1.20 in-use  Protocol State:         Route State:  Enable       mLDP State:  Enable       P-PIM State:  Disable      C-PIM State:  Enable       Upstream Protocol: BGP    PIM-MDT Info:         MDT tunnel:       MDT source: ::      MDT tunnel state:       Default group: ::  Data group is: ::/0显示信息说明:                        参数    描述 Import mcast RT：导入组播路由目标Provider tunnel：支持隧道模式  P-PIM State： 公网PIM状态C-PIM State： 私网PIM状态 





相关命令 :

无 




## show ipv6 mvpn mrib 


show ipv6 mvpn mrib 




命令功能 :

显示IPv6 MVPN的route infomation base 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mvpn mrib 
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
＜vrf-name＞|实例名，长度1–32字符
＜group-address＞|组地址，为X:X::X:X形式
＜source-address＞|源地址，为X:X::X:X形式








缺省 :

无 






使用说明 :

1.显示时需指定<vrf-name>组播VPN的路由信息，可以使用<source-address>和<group-address>作为过滤条件来显示指定的路由信息 






范例 :

显示IPv6 MVPN路由信息：ZXROSNG#show ipv6 mvpn mrib vrf zte1Legend for MVPN routes properties    LO -- Local VPN route  RM -- remote VPN route   IFT -- Receive from P-tunnel  OFT -- Send to P-tunnel   OFNL -- Downstream join state(13::1,ff88::1)  Flags: /OFT/OFNL  Upstream Status:    Upstream PE: Local     Upstream tunnel:-    RPF Tunnel:-  Downstream Status:    Downstream tunnel: mLDP-P2MP,1003,1.1.1.20    Switch tunnel:     Switch timer:   Correlative discovery route table  Type:3, RD:10:10, Uptime:00:11:40, Properties: LO          Nlri:(13::1,ff88::1):1.1.1.20          Ptnl:mLDP-P2MP,1003,1.1.1.20  Type:5, RD:10:10, Uptime:00:11:43, Properties: LO          Nlri:(13::1,ff88::1), Probe: 00:00:00  Type:7, RD:10:10, Uptime:00:11:41, Properties: RM          Nlri:(13::1,ff88::1)显示信息说明:                        参数    描述Upstream Status：上游状态Upstream PE：上游PE                             Upstream tunnel：上游隧道RPF Tunnel：RPF隧道 Downstream Status：下游状态Downstream tunnel：下游隧道Switch tunnel：待切换隧道     Switch timer：隧道切换延时定时器                        Correlative discovery route table                            Type：AD路由类型





相关命令 :

无 




## show ipv6 mvpn mtib 


show ipv6 mvpn mtib 




命令功能 :

显示IPv6 MVPN的tunnel infomation base  






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mvpn mtib 
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

1.可以指定vrf实例查看隧道信息，使用<vrf-name>来指定实例，如果不指定就会显示当前所有私网实例的隧道信息。 






范例 :

显示IPv6 MVPN隧道信息：ZXROSNG#show ipv6 mvpn mtib vrf zte1Name: mLDP-P2MP Root Tunnel 1002  Properties:    Leaf required: 0, Label: 0, Type: 2     Opaque ID: 1002, Root ID: 1.1.1.20  Status:    Oper: Create, Protocol: Up, PriVRF: zte1  All VPN Info:    VRF name: zte1      VPN label: 0, C-Flow Num: 0, Send Num: 0, Switch Num: 0显示信息说明:参数    描述Name：隧道名称     Properties：隧道属性        Leaf required：叶子路由标记Label：标签Type：隧道类型Opaque ID：隧道IDRoot ID：BGP建链根地址Status：隧道状态Oper：操作状态    Protocol：协议状态PriVRF：主VPN名称All VPN Info：隧道下所有VPN信息VPN label：VPN标签C-Flow Num：隧道绑定SPMSI-AD路由条目计数Send Num：隧道绑定私网路由条目计数Switch Num：隧道切换次数





相关命令 :

无 




## show ipv6 mvpn mtunnel 


show ipv6 mvpn mtunnel 




命令功能 :

显示IPv6 MVPN的PMSI隧道信息。  






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mvpn mtunnel 
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

显示全局IPv6 MVPN隧道信息：ZXROSNG(config)#show ipv6 mvpn mtunnelName: TE-P2MP Root Tunnel 202Main VRF: zte2All MRT information:    VRF name: zte2        (*,ff99::1)        (*,ff99::2)        (*,ff99::3)        (*,ff99::4)        (*,ff99::5)        (*,ff99::6)        (*,ff99::7)        (*,ff99::8)        (*,ff99::9)        (*,ff99::10)Name: TE-P2MP Leaf Tunnel 62002Main VRF: zte2All MRT information:Name: mLDP-P2MP Root Tunnel 1001Main VRF: zte1All MRT information:    VRF name: zte1        (*,ff88::1)        (*,ff88::2)        (*,ff88::3)        (*,ff88::4)        (*,ff88::5)        (*,ff88::6)        (*,ff88::7)        (*,ff88::8)        (*,ff88::9)        (*,ff88::10)        (*,ff88:1111:1111:1111:1111:1111:1111:1111)Name: mLDP-P2MP Leaf Tunnel 60005Main VRF: zte1All MRT information:显示信息说明Name:隧道名称Type:隧道类型Main VRF:主VPN名称All MRT information:所有关联此隧道的组播路由信息VRF name:VPN名称






相关命令 :

无 




## show ipv6 mvpn segment 


show ipv6 mvpn segment 




命令功能 :

显示IPv6 MVPN 隧道的分段信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 mvpn segment 
  [＜index 
＞] 







命令参数解释 :



参数|描述
---|---
＜index＞|分段索引号，范围：1-4294967295








缺省 :

无 






使用说明 :

不指定index的情况显示所有分段索引的隧道分段信息 






范例 :

ZXROSNG#show ipv6 mvpn segmentSegment 1  Upstream Info:  Downstream Info:    Ingress-Replication Root Tunnel 1001      Leaf Required: 1, Label: 0, Type: 6      Tunnel ID: 1001    Leaf AD list:      Originating Router: 2.3.4.5, Label: 205826显示信息说明Segment:分段序号Upstream Info:上游隧道信息Downstream Info:下游隧道信息Leaf Required:标记是否需要创建叶子路由Label:标签（固定填0）Type:隧道类型 1:rsvp-te,2:mldp-p2mp,6:ingress-replicationTunnel ID: 隧道IDLeaf AD list:叶子节点信息Originating Router:根地址Label:隧道标签






相关命令 :

无 




## show ipv6 pim bfd 


show ipv6 pim bfd 




命令功能 :

显示IPv6 PIM BFD信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 pim bfd 
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

1.查看具体哪个VRF实例下的IPv6 PIM BFD信息，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个接口的IPv6 PIM BFD信息，可采用<interface-name>来指定，不指定则显示所有接口的BFD信息。






范例 :

ZXROSNG(config)#show ipv6 pim bfd Interface: gei-0/1/0/1   State: CONNECT  BFD Local-Addr: fe80::2ee:ffff:fe10:1000(BDR)  BFD Peer-Addr: fe80::2ee:ffff:fe10:2000(DR) 显示信息说明：Interface：接口地址；BFD Local_Addr：本端配置BFD的接口地址；BFD Peer_Addr：对端配置BFD的接口地址；State：BFD链接状态。






相关命令 :

bfd-enable：在接口上启用BFD。 




## show ipv6 pim bsr 


show ipv6 pim bsr 




命令功能 :

显示自举路由器（BSR）的信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 pim bsr 
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

ZXROSNG(config)#show ipv6 pim bsr BSR address: 101::20Uptime: 00:14:19, BSR Priority :0, Hash mask length:126Expires:00:00:40This system is a candidate BSR!  candidate BSR address: 101::20,                priority: 0,                hash mask length: 126This system is a candidate RP!  candidate RP address: 101::20,priority:72ZXROSNG(config)#显示信息说明：参数                    描述BSR address             BSR的IPv6地址Uptime                  BSR的存活时间BSR Priority            BSR优先级Hash mask length        BSR 掩码长度Expires                 BSR的过期时间或者是发送BSR消息的过期时间candidate RP address    本地配置的候选RP的IPv6地址priority                本地配置的候选RP优先级






相关命令 :

bsr-candidate：配置候选BSR。 




## show ipv6 pim interface brief 


show ipv6 pim interface brief 




命令功能 :

查看IPv6 PIM接口概要信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 pim interface brief 
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

1.查看具体哪个VRF实例下的IPv6 PIM接口概要信息，可采用<vrf-name>来指定，不指定则显示公网的。 






范例 :

ZXROSNG(config)#show ipv6 pim interface briefTotal: 2Interface                        State Nbr   Hello  DR                                       Count Period PriorityDR-Addressgei-0/1/0/1                      Up    1     30     1fe80::216:3eff:fe64:305loopback1                        Up    0     30     1fe80:5624:7895:5858:2454:1245:1584:1122(local)ZXROSNG(config)#显示信息说明：Total：接口数目统计；Interface：接口名称；State：接口状态up/down；Nbr Count：邻居个数；Hello Period：HELLO报文的发送时间间隔；DR Priority：该接口的DR优先级；DR-Address：该接口的DR地址。






相关命令 :

show ipv6 pim interface 




## show ipv6 pim interface 


show ipv6 pim interface 




命令功能 :

显示配置的IPv6 PIM接口情况。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 pim interface 
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

1.查看具体哪个VRF实例下的IPv6 PIM接口情况，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个IPv6 PIM接口情况，可采用<interface-name>来指定，不指定则显示所有IPv6 PIM接口。





范例 :

ZXROSNG(config)#show ipv6 pim interfaceTotal: 3Interface                        State Nbr   Hello  DR         PIM      Mode                                       Count Period Priority   Silentgei-0/20/0/1                     Up    0     30     1          Disabled   DAddress: fe80::216:3eff:fe64:305DR     : fe80::216:3eff:fe64:305gei-0/20/0/2                     Up    0     30     1          Disabled   SAddress: fe80::216:3eff:fe64:305DR     : fe80::216:3eff:fe64:305loopback2                        Up    0     30     1          Disabled   SAddress: fe80::216:3eff:fe64:305DR     : fe80::216:3eff:fe64:305ZXROSNG(config)#show ipv6 pim interface vrf zteTotal: 1Interface                        State Nbr   Hello  DR         PIM      Mode                                       Count Period Priority   Silentmvpn_tunnel1                     Up    1     30     1          Disabled   S    Address: ::ffff:1.1.1.20    DR     : ::ffff:1.1.1.20ZXROSNG(config)#显示信息说明：Total：接口数目统计；Interface：接口名称；State：接口状态up/down；Nbr Count：邻居个数；Hello Period：HELLO报文的发送时间间隔；DR Priority：该接口的DR优先级；PIMSilent：是否启用PIM silent；Mode：接口使能的是哪些PIM模式(SM和DM)；Address：接口配置的接口地址；DR：该接口的DR。





相关命令 :

dr-priority：配置IPv6 PIM接口DR优先级。hello-interval：配置接口IPv6 PIM hello报文发送间隔。pim-silent：接口禁止发送和接收IPv6 PIM协议报文。pimsm：接口上使能IPv6组播PIM-SM协议。pimdm：接口上使能IPv6组播PIM-DM协议。




## show ipv6 pim mroute summary all-instance 


show ipv6 pim mroute summary all-instance 




命令功能 :

显示IPv6 组播所有实例的PIM路由表总数的具体数目。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 pim mroute summary all-instance 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

显示IPv6组播所有实例的PIM路由表总数的具体数目：ZXROSNG(config)#show ipv6 pim mroute summary all-instanceIPv6 PIM Multicast Routing Table Summary(*, G):4 , (S, G):3, (S, G, rpt):0, Register:3显示信息说明：(*,G)：表示配置的组播PIM (*,G)条目数；(S,G)：表示配置的组播PIM (S,G)条目数；(S, G, rpt)：表示配置的组播PIM (S, G, rpt)条目数；Register：表示配置的组播PIM注册条目数。






相关命令 :

show ipv6 pim mroute summary 




## show ipv6 pim mroute summary 


show ipv6 pim mroute summary 




命令功能 :

显示组播IPv6 PIM路由表的统计信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 pim mroute summary 
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

查看特定VRF实例下的IPv6 PIM路由表的路由条目统计信息，可采用<vrf-name>来指定，不指定则显示公网的路由条目统计信息。 






范例 :

ZXROSNG(config)#show ipv6 pim mroute su                             ZXROSNG(config)#show ipv6 pim mroute summary IPv6 PIM Multicast Routing Table Summary(*, G):1 , (S, G):0, (S, G, rpt):0, Register:0(*, ff07:1::1) (JOINED), RP: 101::20ZXROSNG(config)#






相关命令 :

无 




## show ipv6 pim mroute 


show ipv6 pim mroute 




命令功能 :

显示组播IPv6 PIM路由表的内容。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 pim mroute 
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
＜group-address＞|组地址，为X:X::X:X形式
＜source-address＞|源地址，为X:X::X:X形式








缺省 :

无 






使用说明 :

1.查看具体哪个VRF实例下的组播路由表，可采用<vrf-name>来指定，不指定则显示所有公网的组播路由表；2.如果没有组和源地址选项，则显示所有的组播路由表；3.如果增加组选项，则显示该组(*，G)和所有相关的(S，G)路由条目；4.如果增加组和源地址选项，则显示特定的(S，G)路由条目。






范例 :

1.组播路由条目显示：ZXROSNG#show ipv6 pim mroute IPv6 PIM Multicast Routing TableFlags: T- SPT-bit set,A- Forward,J- Join SPT,U- Upsend,S- PIM-SM,D- PIM-DM, Macro state: Ind- Pim Include Macro,Exd- Pim Exclude Macro,       Jns- Pim Joins Macro,LAst- Pim Lost_assert Macro,       Imo- Pim Immediate_olist Macro,Ino- Pim Inherited_olist Macro,       Lcd- Pim Local_receiver_include Macro,       Fbk- Fallback extranet receiver number Timers:UpTime/Expire(Upstream State)/KAT (*, ffee::1)  00:00:12/00:00:48(JOINED)/00:00:00  RP address: 1000::1  Ind:0/Jns:1/LAst:0/Imo:1/Lcd:0/Fbk:0  Iif: NULL, RPF nbr: 0::0  Oif: 1    gei-0/20/0/1,     Joins  /  ImoXG  /  UpTime: 00:00:12, Expire: 00:03:18(8000::10, ffee::1)  00:00:03/00:00:00(JOINED)/00:03:28  RP:1000::1;   Reg:NO INFO; RT:NULL;   Ind:0/Exd:0/Jns:1/LAst:0/Imo:1/Ino:1/Fbk:0  Iif: gei-0/20/0/8, RPF nbr:0::0(S); AT       RPF nbr:0::0(D); 00:00:00(FORWARD); (8000::10, ffee::1, rpt)  00:00:02/00:00:00(PRUNED),   Pru:1/LAst:0/Ino:0  Iif:NULL; RPF nbr:0::0;   Oif: 2     gei-0/20/0/1,   PrunesSGRpt  /  InheritedFromXG      gei-0/20/0/2,   JoinsSG  /  InoSG  /  UpTime: 00:00:03, Expire: 00:03:27         (*, ffee::2)  00:00:12/00:00:48(JOINED)/00:00:00  RP address: 1000::1  Ind:0/Jns:1/LAst:0/Imo:1/Lcd:0/Fbk:0  Iif: NULL, RPF nbr: 0::0  Oif: 1     gei-0/20/0/1,     Joins  /  ImoXG  /  UpTime: 00:00:12, Expire: 00:03:18ZXROSNG#   ZXROSNG#show ipv6 pim mroute group ffee::2                                       IPv6 PIM Multicast Routing TableFlags: T- SPT-bit set,A- Forward,J- Join SPT,U- Upsend,S- PIM-SM,D- PIM-DM, Macro state: Ind- Pim Include Macro,Exd- Pim Exclude Macro,       Jns- Pim Joins Macro,LAst- Pim Lost_assert Macro,       Imo- Pim Immediate_olist Macro,Ino- Pim Inherited_olist Macro,       Lcd- Pim Local_receiver_include Macro,       Fbk- Fallback extranet receiver number Timers:UpTime/Expire(Upstream State)/KAT (*, ffee::2)  00:00:25/00:00:35(JOINED)/00:00:00  RP address: 1000::1  Ind:0/Jns:1/LAst:0/Imo:1/Lcd:0/Fbk:0  Iif: NULL, RPF nbr: 0::0  Oif: 1    gei-0/20/0/1,     Joins  /  ImoXG  /  UpTime: 00:00:25, Expire: 00:03:05ZXROSNG#2.支持fallback功能的组播路由条目显示：ZXROSNG(config)#show ipv6 pim mroute IPv6 PIM Multicast Routing TableFlags: T- SPT-bit set,A- Forward,J- Join SPT,U- Upsend,S- PIM-SM,D- PIM-DM, Macro state: Ind- Pim Include Macro,Exd- Pim Exclude Macro,       Jns- Pim Joins Macro,LAst- Pim Lost_assert Macro,       Imo- Pim Immediate_olist Macro,Ino- Pim Inherited_olist Macro,       Lcd- Pim Local_receiver_include Macro,       Fbk- Fallback extranet receiver number Timers:UpTime/Expire(Upstream State)/KAT (*, ffe8::1)  00:00:20/00:00:40(JOINED)/00:00:00  RP address: 100::100  Ind:2/Jns:0/LAst:0/Imo:2/Lcd:2/Fbk:0  Iif: NULL, RPF nbr: 0::0  Oif: 2    loopback1,     LocalIn  /  ImoXG  /  UpTime: 00:00:20, Expire: 00:00:00    loopback10,     LocalIn  /  ImoXG  /  UpTime: 00:00:08, Expire: 00:00:00(1000::10, ffe8::1)  00:00:14/00:00:00(JOINED)/00:00:00  RP:100::100;   Reg:NO INFO; RT:NULL;   Ind:1/Exd:0/Jns:0/LAst:0/Imo:1/Ino:2/Fbk:0  Iif: gei-0/20/0/1, RPF nbr:0::0(S); AU       RPF nbr:0::0(D); 00:00:00(FORWARD);   Oif: 2     loopback1,   LocalInSG  /  InheritedFromXG  /  InoSGRpt  /  InoSG  /  UpTime: 00:00:14, Expire: 00:00:00    loopback10,   InheritedFromXG  /  InoSGRpt  /  InoSG           (*, ffee::1)  00:02:21/00:00:44(JOINED)/00:00:00  RP address: 100::100  Ind:2/Jns:0/LAst:0/Imo:2/Lcd:2/Fbk:1  Iif: NULL, RPF nbr: 0::0  Oif: 1     loopback1,     LocalIn  /  ImoXG  /  UpTime: 00:02:21, Expire: 00:00:00         (1000::10, ffee::1)  00:02:21/00:00:00(JOINED)/00:00:00  RP:100::100;   Reg:NO INFO; RT:NULL;   Ind:2/Exd:0/Jns:0/LAst:0/Imo:2/Ino:2/Fbk:1  Iif: gei-0/20/0/1, RPF nbr:0::0(S); AU       RPF nbr:0::0(D); 00:00:00(FORWARD);   Oif: 1     loopback1,   LocalInSG  /  InheritedFromXG  /  InoSGRpt  /  InoSG  /  UpTime: 00:02:26, Expire: 00:00:00ZXROSNG(config)#ZXROSNG(config)#show ipv6 pim mroute vrf zte_mcast1IPv6 PIM Multicast Routing TableFlags: T- SPT-bit set,A- Forward,J- Join SPT,U- Upsend,S- PIM-SM,D- PIM-DM, Macro state: Ind- Pim Include Macro,Exd- Pim Exclude Macro,       Jns- Pim Joins Macro,LAst- Pim Lost_assert Macro,       Imo- Pim Immediate_olist Macro,Ino- Pim Inherited_olist Macro,       Lcd- Pim Local_receiver_include Macro,       Fbk- Fallback extranet receiver number Timers:UpTime/Expire(Upstream State)/KAT (*, ffee::1)  00:02:37/00:00:00(JOINED)/00:00:00  RP address: 100::100  Ind:1/Jns:0/LAst:0/Imo:1/Lcd:1/Fbk:0  Iif: using global, RPF nbr:0::0; J  Oif: 1    loopback2,     LocalIn  /  ImoXG  /  UpTime: 00:02:37, Expire: 00:00:00(1000::10, ffee::1)  00:02:37/00:00:00(JOINED)/00:00:00  RP:100::100;   Reg:NO INFO; RT:NULL;   Ind:1/Exd:0/Jns:0/LAst:0/Imo:1/Ino:1/Fbk:0  Iif: using global, RPF nbr:0::0(S); AU       RPF nbr:0::0(D); 00:00:00(FORWARD);   Oif: 1     loopback2,   LocalInSG  /  InheritedFromXG  /  InoSGRpt  /  InoSG  /  UpTime: 00:02:37, Expire: 00:00:00ZXROSNG(config)#显示信息说明：T：表示此路由条目接收到来自SPT树的组播包A：表示此路由条目的入接口有效U：表示向该条目上送组播包J：表示接收到数据流向SPT树切换Ind: 表示有本地IGMP加入接收数据流的接口数Exd: 表示有本地IGMP加入不接收数据流的接口数LAst: 表示接收数据流但是asser失败的接口数Imo: 表示直接根据路由类型建立的出接口数Ino: 表示继承其他路由类型的出接口数Fbk：表示fallback扩展的接收者个数UpTime/Expire: 表示此路由条目的运行时间和过期时间RP address: 表示PIM-SM产生的（*，G）条目对应的RPIif: 表示条目入接口RPF nbr: 表示条目相应的RPF邻居Oif：表示出接口列表，后面数字表示出接口个数，UpTime表示该接口作为路由出接口的时间，Expire表示PIM协议状态到期时间的倒计时using global：表示组播路由上游实例名称。当上游是公网实例，显示using globalusing vrf zte：表示组播路由上游实例名称。当上游是私网实例zte，显示using vrf zte





相关命令 :

无 




## show ipv6 pim neighbor 


show ipv6 pim neighbor 




命令功能 :

显示配置的IPv6 PIM接口的邻居情况。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ipv6 pim neighbor 
  [vrf 
 ＜vrf-name 
＞] [＜interface-name 
＞] [detail 
] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜interface-name＞|接口的名称
detail|接口邻居的详细信息








缺省 :

无 






使用说明 :

1.查看具体哪个VRF实例下的IPv6 PIM接口邻居情况，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个IPv6 PIM接口的邻居情况，可采用<interface-name>来指定，不指定则显示所有IPv6 PIM接口的邻居情况。






范例 :

1. 显示配置的IPv6 PIM接口的邻居信息：ZXROSNG(config)#show ipv6 pim neighbor Neighbor Address(es): fe80::2ee:ffff:fe10:2000  Interface: gei-0/1/0/1  Uptime: 00:00:04  Expire: 00:01:44  DR Pri: 1  Attr: N/A2. 显示配置的IPv6 PIM接口的邻居详细信息：ZXROSNG(config)#show ipv6 pim neighbor detail Neighbor Address(es): fe80::2ee:ffff:fe10:2000  Interface: gei-0/1/0/1  Uptime: 00:33:04  Expire: 00:01:43  DR Pri: 1  Attr: N/A  Address-list Hello option: 101::203. 显示信息说明：参数    描述Neighbor Address：邻居IPv6地址；Interface：接口名称；Uptime：邻居的存活时间；Expires：邻居的过期时间；DR Pri：邻居的DR优先级；Attr：hello报文中的JOIN选项，N/A表示报文中没有此选项，P表示使用了此选项；Address-list Hello option：邻居的地址列表信息。






相关命令 :

dr-priority：配置IPv6 PIM接口DR优先级。pimsm：接口上使能IPv6组播PIM-SM协议。pimdm：接口上使能IPv6组播PIM-DM协议。




## show ipv6 pim nexthop 


show ipv6 pim nexthop 




命令功能 :

显示IPv6 PIM下一跳的信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 pim nexthop 
  [vrf 
 ＜vrf-name 
＞] [dest-address 
 ＜ipv6-address 
＞] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜ipv6-address＞|目的IPv6地址，为X:X::X:X形式








缺省 :

无 






使用说明 :

1.查看具体哪个VRF实例下的IPv6 PIM下一跳信息，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体到哪个目的地址的IPv6 PIM下一跳信息，可采用dest-address<ipv6-address>来指定，不指定则显示所有IPv6 PIM下一跳信息。





范例 :

显示IPv6 PIM下一跳的信息：ZXROSNG(config-mcast-ipv6-pim)#show ipv6 pim nexthopIPv6 PIM Nexthop TableNexthop state: R- Nexthop to RP,S- Nexthop to Source,O- Related with Unicast,U- No Unicast Route,L- Local Route,C- Connect to Dest,Dest:2::2                                    (00:01:24)Type:.R. .O. .L.Metric:0Preference:0ECMP list:Nexthop:::(is Local)Port:Dest:105::100                                (00:02:47)Type:. .S.O. . .Metric:0Preference:1ECMP list:Nexthop:101::10(PIM neighbor fe80::2ee:ffff:fe10:1000)Port:gei-0/1/0/1Dest:3::3                                    (00:02:26)Type:. .S.O. . .Metric:1Preference:1Fallback: vrf zteDest:4::4                                    (00:01:26)Type:. .S.O. . .Metric:1Preference:1RPF path list: abcZXROSNG#show ipv6 pim nexthop vrf zteIPv6 PIM Nexthop TableNexthop state: R- Nexthop to RP,S- Nexthop to Source,O- Related with Unicast,U- No Unicast Route,L- Local Route,C- Connect to Dest,Dest:1::1                                    (00:01:56)Type:. .S.O. . .Metric:1Preference:1Fallback: IP globalDest:80::2                                   (00:02:22)  Type:. .S.O. . .  Metric:0  Preference:200  ECMP list:      Nexthop:::ffff:1.1.1.10(PIM neighbor ::ffff:1.1.1.10)      Port:mvpn_tunnel1显示信息说明：参数             描述Nexthop：下一跳IPv6地址（下一跳的到期时间）Type：下一跳路由的类型Metric：下一跳的路由度量值Preference：下一跳的路由优先级Nexthop address：下一跳地址Nexthop port：单播路由的出接口Fallback：IP global表示下一跳是公网实例，vrf zte表示下一跳是私网zte实例RPF path list：RPF路径列表。






相关命令 :

pimsm：接口上使能IPv6组播PIM-SM协议。pimdm：接口上使能IPv6组播PIM-DM协议。




## show ipv6 pim rp hash 


show ipv6 pim rp hash 




命令功能 :

显示特定组播组选择的RP信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 pim rp hash 
  [vrf 
 ＜vrf-name 
＞] ＜group-address 
＞ 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
＜group-address＞|组地址，为X:X::X:X形式








缺省 :

无 






使用说明 :

1.查看具体哪个VRF实例下的特定组播组选择的RP信息，可采用<vrf-name>来指定，不指定则显示公网的；2.必选参数＜group-address＞显示特定组播组选择的RP信息。





范例 :

显示组ff07:1::1选择的RP信息：ZXROSNG(config-mcast-ipv6-pim)#show ipv6 pim rp hash ff07:1::1RP address: 101::20  






相关命令 :

rp-candidate：配置候选RP。static-rp：配置静态RP。




## show ipv6 pim rp mapping 


show ipv6 pim rp mapping 




命令功能 :

显示所有的RP集信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 pim rp mapping 
  [vrf 
 ＜vrf-name 
＞] [{default 
|bsr 
|static 
|embedded 
}] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1–32个字符
default|默认通告
bsr|bsr通告
static|静态通告
embedded|embedded通告








缺省 :

无 






使用说明 :

1.查看特定VRF实例下的RP集信息，可采用<vrf-name>来指定，不指定则显示公网的RP集信息。2.没有参数时显示所有的RP集信息，可通过选项指定查看各个信息源的RP集信息。






范例 :

ZXROSNG(config)#show ipv6 pim rp mapping bsr ff00::/8    RP         : 101::10       Protocol   : SM    Info source: BSR From: 101::20, Priority: 192    Uptime     : 00:14:52    Expires    : 00:01:44ff00::/8    RP         : 101::20       Protocol   : SM    Info source: BSR From: 101::20, Priority: 72    Uptime     : 00:16:37    Expires    : 00:01:55ZXROSNG(config)#显示信息说明：参数            描述Group           选择RP的组播组地址和掩码RP              该组播组通告的候选RP地址Protocol        协议Info source     RP信息源Uptime          候选RP的存活时间Expires         候选RP的过期时间






相关命令 :

无 




## show ipv6 pim traffic 


show ipv6 pim traffic 




命令功能 :

显示IPv6 PIM协议流量统计信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ipv6 pim traffic 
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

1.查看具体哪个VRF实例下的IPv6 PIM流量统计信息，可采用<vrf-name>来指定，不指定则显示公网的；2.查看具体哪个IPv6 PIM接口的流量统计信息，可采用<interface-name>来指定，不指定则显示所有IPv6 PIM接口的流量统计信息。





范例 :

ZXROSNG(config)#show ipv6 pim trafficIPv6 PIM packet  Received   Sent       Filter     ErrorInterface: gei-0/1/0/1Hello:         0          2          0          0Join/Prune:    0          0          0          0Register:      0          0          0          0Register-Stop: 0          0          0          0Bootstrap:     0          0          0          0C-RP-Ad:       0          0          0          0Assert:        0          0          0          0State-Refresh: 0          0          0          0Graft:         0          0          0          0Graft-Ack:     0          0          0          0DF-Election:   0          0          0          0PFM-TLV:   0          0          0          0Total traffic in current PIM instance:Total:         0          2          0          0Hello:         0          2          0          0Join/Prune:    0          0          0          0Register:      0          0          0          0Register-Stop: 0          0          0          0Bootstrap:     0          0          0          0C-RP-Ad:       0          0          0          0Assert:        0          0          0          0State-Refresh: 0          0          0          0Graft:         0          0          0          0Graft-Ack:     0          0          0          0DF-Election:   0          0          0          0PFM-TLV:   0          0          0          0Current Time:  2017-09-26 00:45:49显示信息说明：1. 接口下协议报文收发信息显示说明，分发送，接收，接收过滤和接收错误四部分：Interface：接口名；Hello：Hello报文个数；Join/Prune：J/P报文个数；Register：注册报文个数；Register-Stop：注册停止报文个数；Bootstrap：BSM报文个数；C-RP-Ad：C-RP通告报文个数；Assert：Assert报文个数；State-Refresh：State-Refresh报文个数；Graft：Graft报文个数；Graft-Ack：Graft-Ack报文个数。DF-Election：DF-Election报文个数。PFM-TLV：PFM-TLV报文个数。2. IPv6 PIM实例下信息显示说明：Total：汇总所有接口流量信息，具体报文同上；3. 当前系统时间显示说明：Current time：显示当前时间。






相关命令 :

clear ipv6 pim traffic：清除PIM流量统计信息。 




## spt-threshold 


spt-threshold 




命令功能 :

配置有直连接收者的路由器从共享树RP树到SPT树为永不切换，使用no命令禁止这一特性。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






命令格式 :



spt-threshold 
 infinity 


no spt-threshold 








命令参数解释 :



参数|描述
---|---
infinity|永不切换配置








缺省 :

缺省情况下，从共享树切换到源最短路径树的阀值为0。 






使用说明 :

infinity表示永不切换。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#spt-threshold infinity 






相关命令 :

无 




## spt-threshold 


spt-threshold 




命令功能 :

配置有直连接收者的路由器从共享树RP树到SPT树为永不切换，使用no命令禁止这一特性。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






命令格式 :



spt-threshold 
 infinity 


no spt-threshold 








命令参数解释 :



参数|描述
---|---
infinity|永不切换配置








缺省 :

缺省情况下，从共享树切换到源最短路径树的阀值为0。 






使用说明 :

infinity表示永不切换。 






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#spt-threshold infinity 






相关命令 :

无 




## ssm range 


ssm range 




命令功能 :

配置SSM组地址范围。 






命令模式 :

 IPv6-PIM模式  






命令默认权限级别 :

15 






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
default|默认SSM支持的组范围是FF3X::/32
＜access-list-name＞|ACL名，长度1-31个字符








缺省 :

无 






使用说明 :

1.group-list配置SSM组范围；2.IPv6默认使能SSM。3.multicast-address compatible-rfc7371命令使能情况，默认SSM支持的组范围是FF3X::/32或FFBX::/32






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#ssm range default






相关命令 :

multicast-address compatible-rfc7371 




## ssm range 


ssm range 




命令功能 :

配置SSM组地址范围。 






命令模式 :

 IPv6-PIM-VRF模式  






命令默认权限级别 :

15 






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
default|默认SSM支持的组范围是FF3X::/32
＜access-list-name＞|ACL名，长度1-31个字符








缺省 :

无 






使用说明 :

1.group-list配置SSM组范围；2.IPv6默认使能SSM。3.multicast-address compatible-rfc7371命令使能情况，默认SSM支持的组范围是FF3X::/32或FFBX::/32






范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#ssm range default






相关命令 :

multicast-address compatible-rfc7371 




## ssm-map static 


ssm-map static 




命令功能 :

配置特定范围组向源地址的映射，使用no命令取消限制。 






命令模式 :

 MLD模式  






命令默认权限级别 :

15 






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
default|映射default的组，default组是ff3x::/32
＜acl-name＞|SSM组访问列表名，范围1–31字符
＜source-address＞|IPv6格式的地址，X:X::X:X形式








缺省 :

IPv6 PIM模式下默认开启ssm enable;默认映射范围组ff3x::/32






使用说明 :

配置特定范围组向源地址的映射使用：ssm-map static {default|group-list ＜acl-name＞} ＜source-address＞;除非是默认映射范围组，否则用于映射的组地址必须在ssm range配置的group-list <acl-name>范围内才会map上源






范例 :

配置MLD源地址的映射：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#ssm-map static group-list zte 200::200 ZXROSNG(config-mcast-ipv6-mld)#exitZXROSNG(config-mcast-ipv6)#router pimR1(config-mcast-ipv6-pim)#ssm range group-list zte R1(config-mcast-ipv6-pim)#show ipv6 mld groups detail Flags: S - Static Group, SSM - SSM Group, M - MDT GroupInterface:      gei-0/1/0/1Group:          ff1e::100Flags:          S SSM Uptime:         00:21:57Group mode:     INCLUDELast reporter:  fe80::2ee:ffff:fe10:1000Group source list: (M - SSM Mapping, S - Static, R - Report)  Source addr                             Present   Expires   Fwd  Flag  200::200                                00:00:11  Never     Yes  S M  






相关命令 :

ssm range static-group 



## ssm-map static 


ssm-map static 




命令功能 :

配置特定范围组向源地址的映射，使用no命令取消限制。 






命令模式 :

 MLD-VRF模式  






命令默认权限级别 :

15 






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
default|映射default的组，default组是ff3x::/32
＜acl-name＞|SSM组访问列表名，范围1–31字符
＜source-address＞|IPv6格式的地址，X:X::X:X形式








缺省 :

IPv6 PIM模式下默认开启ssm enable;默认映射范围组ff3x::/32






使用说明 :

配置特定范围组向源地址的映射使用：ssm-map static {default|group-list ＜acl-name＞} ＜source-address＞;除非是默认映射范围组，否则用于映射的组地址必须在ssm range配置的group-list <acl-name>范围内才会map上源






范例 :

配置MLD源地址的映射：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#ssm-map static group-list zte 200::200 ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#ssm range group-list zte ZXROSNG(config-mcast-ipv6-vrf-zte-pim)#show ipv6 mld groups vrf zte detail Flags: S - Static Group, SSM - SSM Group, M - MDT GroupInterface:      gei-0/1/0/1Group:          ff1e::100Flags:          S SSM Uptime:         00:21:57Group mode:     INCLUDELast reporter:  fe80::2ee:ffff:fe10:1000Group source list: (M - SSM Mapping, S - Static, R - Report)  Source addr                             Present   Expires   Fwd  Flag  200::200                                00:00:11  Never     Yes  S M  






相关命令 :

ssm range static-group 



## startup-query-count 


startup-query-count 




命令功能 :

配置MLD发送接口UP初始查询报文的次数，使用no命令恢复缺省值。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






命令格式 :



startup-query-count 
  ＜number 
＞

no startup-query-count 








命令参数解释 :



参数|描述
---|---
＜number＞|MLD接口UP初始查询报文次数，缺省为2次，范围：1–10








缺省 :

缺省为2 






使用说明 :

以初始查询间隔为周期发送查询报文startup-query-count次后，使用query-interval为周期发送查询报文。 






范例 :

配置MLD接口UP初始查询报文次数：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast)#router mldZXROSNG(config-mcast-mld)#interface gei-0/1/0/1ZXROSNG(config-mcast-mld-if-gei-0/1/0/1)#startup-query-count 5






相关命令 :

startup-query-intervalquery-interval




## startup-query-count 


startup-query-count 




命令功能 :

配置MLD发送接口UP初始查询报文的次数，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



startup-query-count 
  ＜number 
＞

no startup-query-count 








命令参数解释 :



参数|描述
---|---
＜number＞|MLD接口UP初始查询报文次数，缺省为2次，范围：1–10








缺省 :

缺省为2 






使用说明 :

以初始查询间隔为周期发送查询报文startup-query-count次后，使用query-interval为周期发送查询报文。 






范例 :

配置MLD接口UP初始查询报文次数：ZXROSNG(config)#ip multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/1)#startup-query-count 5






相关命令 :

startup-query-intervalquery-interval




## startup-query-interval 


startup-query-interval 




命令功能 :

配置MLD发送接口UP初始查询报文的间隔，使用no命令恢复缺省值。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






命令格式 :



startup-query-interval 
  ＜seconds 
＞

no startup-query-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|MLD接口UP初始查询间隔，缺省为31秒，范围：1–18000，单位：秒








缺省 :

缺省为31秒 






使用说明 :

当接口UP后，查询路由器会发送一定次数（可以通过startup-query-count命令配置，默认值为2）的普通查询报文，查询报文发送间隔为此命令配置值和query-interval命令配置值/4中的较小值。一定次数发送结束后恢复以query-interval命令配置值为周期发送普通查询报文。 






范例 :

配置MLD接口UP初始查询间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/1)#startup-query-interval 10






相关命令 :

startup-query-countquery-interval




## startup-query-interval 


startup-query-interval 




命令功能 :

配置MLD发送接口UP初始查询报文的间隔，使用no命令恢复缺省值。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



startup-query-interval 
  ＜seconds 
＞

no startup-query-interval 








命令参数解释 :



参数|描述
---|---
＜seconds＞|MLD接口UP初始查询间隔，缺省为31秒，范围：1–18000，单位：秒








缺省 :

缺省为31秒 






使用说明 :

当接口UP后，查询路由器会发送一定次数（可以通过startup-query-count命令配置，默认值为2）的普通查询报文，查询报文发送间隔为此命令配置值和query-interval命令配置值/4中的较小值。一定次数发送结束后恢复以query-interval命令配置值为周期发送普通查询报文。 






范例 :

配置MLD接口UP初始查询间隔：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/1)#startup-query-interval 10






相关命令 :

startup-query-countquery-interval




## static-first 


static-first 




命令功能 :

设置组播查找单播路由静态下一跳优先。 






命令模式 :

 IPv6-组播模式  






命令默认权限级别 :

15 






命令格式 :



static-first 
 

no static-first 








命令参数解释 :


					无
				 






缺省 :

静态下一跳优先级小于直连路由和本地路由 






使用说明 :

1.配置后静态下一跳优先级大于直连路由和本地路由。 






范例 :

设置组播查找单播路由静态下一跳优先：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#static-first






相关命令 :

nexthop 




## static-first 


static-first 




命令功能 :

设置组播查找单播路由静态下一跳优先。 






命令模式 :

 MULTICAST6-VRF模式  






命令默认权限级别 :

15 






命令格式 :



static-first 
 

no static-first 








命令参数解释 :


					无
				 






缺省 :

静态下一跳优先级小于直连路由和本地路由 






使用说明 :

1.配置后静态下一跳优先级大于直连路由和本地路由。 






范例 :

设置组播查找单播路由静态下一跳优先：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#static-first






相关命令 :

nexthop 




## static-group 


static-group 




命令功能 :

配置MLD协议接口上的静态组成员，使用no命令删除接口上的静态组成员。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






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
＜group-address＞|IPv6格式的组播组地址，X:X::X:X形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，X:X::X:X形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜source-address＞|IPv6格式的单播源地址，X:X::X:X形式
include|切换到include模式
exclude|切换到exclude模式
ssm-map|通过ssm mapping获取源列表








缺省 :

配置静态带源列表不带过滤模式的组加入默认模式是include。IPv6 PIM模式下默认开启ssm enable;






使用说明 :

配置不带源的静态组加入使用：static group <group-address>;配置带源的静态组加入使用：static group <group-address> source {＜source-address＞ [{include|exclude}]|ssm-map}];RFC规定通过ssm-map源列表的模式默认是include，命令中ssm-map后模式参数不让配置。配置批量的静态组加入：static-group  ＜group-address＞[  inc-mask <mask-address>  count <number>  ] [source {＜source-address＞ [{include|exclude}]|ssm-map}];批量配置静态组的时候，需要先使能PIM接口；反之，在删除PIM接口的时候，检查批量静态组是否存在，不存在才能执行no命令。接口上批量配置静态组时，组地址和掩码步长的最高字节位都不参与计算。






范例 :

配置MLD接口上的静态组成员：ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/100     ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/100)#static-group ff88::2ZXROSNG(config-mcast-ipv6)#show ipv6 mrouteIPv6 Multicast Routing TableFlags:NS:SPT upsend,RT:Reg upsend,F:Forward,NTP:NTP join,DPU:Damping enable,DPD:Damping del,SU:Slave in use,(*, ff88::2)  TYPE: DYNAMIC, FLAGS: NS  RP: 2001::20  Incoming interface: gei-0/1/0/10, flags: NS  Outgoing interface list: 1    gei-0/1/0/100, flags: F配置loopback1接口加入起始组地址为ff33::1，递增掩码步长为::2，组地址数量为4的批量组播组：ZXROSNG(config)# ipv6 multicast-routingZXROSNG(config-mcast)#router mldZXROSNG(config-mcast-ipv6-mld)#interface loopback1ZXROSNG(config-mcast-ipv6-mld-if-loopback1)# static-group ff33::1 inc-mask ::2 count 4ZXROSNG(config-mcast-ipv6-mld-if-loopback1)#show ipv6 mld groups Total: 4 groupsGroup Address : ff33::1Last Reporter : fe80::2ee:ffff:fe10:1000    Interface : loopback1       Uptime : 00:10:06       Expire : never
Group Address : ff33::3Last Reporter : fe80::2ee:ffff:fe10:1000    Interface : loopback1       Uptime : 00:10:06       Expire : never
Group Address : ff33::5Last Reporter : fe80::2ee:ffff:fe10:1000    Interface : loopback1       Uptime : 00:10:06       Expire : never
Group Address : ff33::7Last Reporter : fe80::2ee:ffff:fe10:1000    Interface : loopback1       Uptime : 00:10:06       Expire : never






相关命令 :

ssm-map static  




## static-group 


static-group 




命令功能 :

配置MLD协议接口上的静态组成员，使用no命令删除接口上的静态组成员。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






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
＜group-address＞|IPv6格式的组播组地址，X:X::X:X形式
＜mask-address＞|指定批量配置中的组地址掩码，即组地址序列中相邻两个组地址的间隔，X:X::X:X形式
＜number＞|指定批量配置方式中的组地址个数，取值范围：1-512
＜source-address＞|IPv6格式的单播源地址，X:X::X:X形式
include|切换到include模式
exclude|切换到exclude模式
ssm-map|通过ssm mapping获取源列表








缺省 :

配置静态带源列表不带过滤模式的组加入默认模式是include。 






使用说明 :

配置不带源的静态组加入使用：static group <group-address>;配置带源的静态组加入使用：static group <group-address> source {＜source-address＞ [{include|exclude}]|ssm-map}];RFC规定通过ssm-map源列表的模式默认是include，命令中ssm-map后模式参数不让配置。配置批量的静态组加入：static-group  ＜group-address＞[  inc-mask <mask-address>  count <number>  ] [source {＜source-address＞ [{include|exclude}]|ssm-map}];批量配置静态组的时候，需要先使能PIM接口；反之，在删除PIM接口的时候，检查批量静态组是否存在，不存在才能执行no命令。接口上批量配置静态组时，组地址和掩码步长的最高字节位都不参与计算。





范例 :

配置MLD接口上的静态组成员：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/100ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/100)#static-group ff88::2ZXROSNG(config-mcast-ipv6)#show ipv6 mroute vrf zteIPv6 Multicast Routing TableFlags:NS:SPT upsend,RT:Reg upsend,F:Forward,NTP:NTP join,DPU:Damping enable,DPD:Damping del,SU:Slave in use,(*, ff88::2)  TYPE: DYNAMIC, FLAGS: NS  RP: 2001::20  Incoming interface: gei-0/1/0/10, flags: NS  Outgoing interface list: 1    gei-0/1/0/100, flags: F配置loopback1接口加入起始组地址为ff33::1，递增掩码步长为::2，组地址数量为4的批量组播组：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface loopback1ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-loopback1)# static-group ff33::1 inc-mask ::2 count 4ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-loopback1)#show ipv6 mld groups vrf zteTotal: 4 groupsGroup Address : ff33::1Last Reporter : fe80::216:3eff:fe64:305    Interface : loopback1       Uptime : 00:00:19       Expire : never
Group Address : ff33::3Last Reporter : fe80::216:3eff:fe64:305    Interface : loopback1       Uptime : 00:00:19       Expire : never
Group Address : ff33::5Last Reporter : fe80::216:3eff:fe64:305    Interface : loopback1       Uptime : 00:00:19       Expire : never
Group Address : ff33::7Last Reporter : fe80::216:3eff:fe64:305    Interface : loopback1       Uptime : 00:00:19       Expire : never






相关命令 :

ssm-map static  




## static-rp override 


static-rp override 




命令功能 :

配置静态RP优先。 






命令模式 :

 IPv6-PIM-VRF模式,IPv6-PIM模式  






命令默认权限级别 :

IPv6-PIM-VRF模式:15,IPv6-PIM模式:15 






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

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)router pim ZXROSNG(config-mcast-ipv6-pim)#static-rp override 






相关命令 :

show ipv6 pim rp hash：显示特定组播组选择的RP信息。 




## static-rp 


static-rp 




命令功能 :

配置静态RP地址，使用no命令删除配置。 






命令模式 :

 IPv6-PIM-VRF模式,IPv6-PIM模式  






命令默认权限级别 :

IPv6-PIM-VRF模式:15,IPv6-PIM模式:15 






命令格式 :


static-rp 
  ＜ipv6-address 
＞ [{[group-list 
 ＜prefix-list-name 
＞],[priority 
 ＜priority 
＞]}]
no static-rp 
  ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|静态RP地址，为X:X::X:X形式
＜prefix-list-name＞|定义了一个组范围，该范围是被通告rp服务范围
＜priority＞|静态RP优先级，缺省为192，范围：0–255








缺省 :

没有静态RP配置。 






使用说明 :

1.静态RP配置后即进入RP集参加选择，即使这个路由器没有收到任何BSR的RP信息通告；2.<prefix-list-name>参数配置RP服务范围，如果不带 <prefix-list-name>参数，静态RP适用于所有组播组；3.静态RP的缺省优先级为192，优先级数值较小的静态RP优先；如果优先级数值相同，则比较地址，地址大的RP优先。





范例 :

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#static-rp 2::2





相关命令 :

show ipv6 pim rp mapping：显示所有的RP集信息。 




## triggered-hello-delay 


triggered-hello-delay 




命令功能 :

配置triggered hello报文的延时时间，使用no命令恢复缺省值。 






命令模式 :

 IPv6-PIM接口模式  






命令默认权限级别 :

15 






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

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-pim-if-gei-0/1/0/1)#triggered-hello-delay 3






相关命令 :

无 




## triggered-hello-delay 


triggered-hello-delay 




命令功能 :

配置triggered hello报文的延时时间，使用no命令恢复缺省值。 






命令模式 :

 IPv6-PIM-VRF接口模式  






命令默认权限级别 :

15 






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

ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router pimZXROSNG(config-mcast-ipv6-vrf-zte-pim)#interface gei-0/1/0/1ZXROSNG(config-mcast-ipv6-vrf-zte-pim-if-gei-0/1/0/1)#triggered-hello-delay 3






相关命令 :

无 




## version 


version 




命令功能 :

配置接口上MLD协议版本号，使用no命令恢复缺省状态。 






命令模式 :

 MLD接口模式  






命令默认权限级别 :

15 






命令格式 :



version 
  {1 
|2 
}

no version 








命令参数解释 :



参数|描述
---|---
1|MLD v1版本号
2|MLD v2版本号








缺省 :

默认是MLD v2版本 






使用说明 :

配置version可以在以下模式下：1.MLD模式/MLD-VRF模式2.MLD接口模式/MLD-VRF接口模式在1,2都有配置的情况下，接口模式下配置的值生效。






范例 :

配置接口上MLD协议版本号：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-mld-if-gei-0/1/0/10)#version 2





相关命令 :

无 




## version 


version 




命令功能 :

配置接口上MLD协议版本号，使用no命令恢复缺省状态。 






命令模式 :

 MLD-VRF接口模式  






命令默认权限级别 :

15 






命令格式 :



version 
  {1 
|2 
}

no version 








命令参数解释 :



参数|描述
---|---
1|MLD v1版本号
2|MLD v2版本号








缺省 :

默认是MLD v2版本 






使用说明 :

配置version可以在以下模式下：1.MLD模式/MLD-VRF模式2.MLD接口模式/MLD-VRF接口模式在1,2都有配置的情况下，接口模式下配置的值生效。






范例 :

配置接口上MLD协议版本号：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#interface gei-0/1/0/10ZXROSNG(config-mcast-ipv6-vrf-zte-mld-if-gei-0/1/0/10)#version 2





相关命令 :

无 




## version 


version 




命令功能 :

配置接口上MLD协议版本号，使用no命令恢复缺省状态。 






命令模式 :

 MLD模式  






命令默认权限级别 :

15 






命令格式 :



version 
  {1 
|2 
}

no version 








命令参数解释 :



参数|描述
---|---
1|MLD v1版本号
2|MLD v2版本号








缺省 :

默认是MLD v2版本 






使用说明 :

MLD接口模式下也有version命令，当MLD接口模式下没有配置这条命令，则MLD模式下的配置生效。 






范例 :

配置接口上MLD协议版本号：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router mldZXROSNG(config-mcast-ipv6-mld)#version 2





相关命令 :

无 




## version 


version 




命令功能 :

配置接口上MLD协议版本号，使用no命令恢复缺省状态。 






命令模式 :

 MLD-VRF模式  






命令默认权限级别 :

15 






命令格式 :



version 
  {1 
|2 
}

no version 








命令参数解释 :



参数|描述
---|---
1|MLD v1版本号
2|MLD v2版本号








缺省 :

无 






使用说明 :

MLD-VRF接口模式下也有version命令，当MLD-VRF接口模式下没有配置这条命令，则MLD-VRF模式下的配置生效。 






范例 :

配置接口上MLD协议版本号：ZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#router mldZXROSNG(config-mcast-ipv6-vrf-zte-mld)#version 2





相关命令 :

无 




## vrf 


vrf 




命令功能 :

配置组播VRF模式。使用no命令取消配置 






命令模式 :

 IPv6-组播模式  






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
＜vrf-name＞|VRF的名称








缺省 :

关闭VRF模式。 






使用说明 :

需要先配置VRF实例，才能在组播配置模式下通过此命令配置组播VRF模式 






范例 :

配置组播VRF模式：ZXROSNG(config)# ip vrf zteZXROSNG(config-vrf-zte)#rd 1：2ZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv4)#exitZXROSNG(config-vrf-zte)#exitZXROSNG(config)#ipv6 multicast-routingZXROSNG(config-mcast-ipv6)#router pimZXROSNG(config-mcast-ipv6-pim)#exitZXROSNG(config-mcast-ipv6)#vrf zteZXROSNG(config-mcast-ipv6-vrf-zte)#





相关命令 :

ip vrfaddress-familyrd：在VRF实例创建后需要进一步配置rd，才能使能实例供vrf等其他命令使用。



# NDP配置命令 
## clear nd-cache 


clear nd-cache 




命令功能 :

该命令用于清除IPv6的邻居缓存表中动态学习到的邻居缓存条目。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear nd-cache 
  [＜interface-name 
＞]







命令参数解释 :



参数|描述
---|---
＜interface-name＞|邻居缓存表中的条目对应的出接口。路由器支持：以太接口和以太子接口、sg接口和sg子接口、supervlan口、ulei口和ulei子接口、eth_dslgroup接口、qx接口和qx子接口、bvi接口和bvi子接口、dsl接口、管理口、gpon_vport接口和gpon_vport子接口、svi接口和svi子接口，dcn接口，gtunnel_group接口和te_gtunnel接口。








缺省 :

无。





使用说明 :

该命令工作于特权模式。不指定接口名使用本命令，将删除邻居缓存中所有的动态条目；如果指定接口名执行本命令，则仅删除所属接口为指定接口的动态缓存条目。






范例 :

执行显示IPv6邻居缓存条目命令，结果如下：ZXROSNG#show nd6 cacheTotal Cache Number Is:3Only Current Valid Items Are Shown Below:Address                               Link-Address     Age        Status        Interfacefe80::c800:7bff:fe74:8                ca00.7b74.0008   21h12m43s   Stale        gei-0/1/0/51::1                                  ca00.7b74.0008   21h12m33s   Stale        gei-0/1/0/54ffe::1                               ce03.2220.0001   static      Reachable    gei-0/1/0/5执行清除动态邻居缓存条目后再执行显示命令，结果如下：ZXROSNG#clear nd-cacheZXROSNG#show nd6 cacheTotal Cache  Number Is:1Only Current Valid Items Are Shown Below:Address                                 Link-Address     Age         Status        Interface4ffe::1                                  ce03.2220.0001   static      Reachable    gei-0/1/0/5





相关命令 :

show nd6 cache  [<interface-name>] 




## debug ipv6 nd6 


debug ipv6 nd6 




命令功能 :

该命令用于打开有关ND(Neighbor Discover，邻居发现)协议报文的调试功能开关。可以查看ND报文的收发情况。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 nd6 
  [interface 
 ＜Interface-name 
＞]

no debug ipv6 nd6 








命令参数解释 :



参数|描述
---|---
＜Interface-name＞|邻居缓存表中的条目对应的出接口。路由器上支持：以太接口和以太子接口、sg口和sg子接口、supervlan口、ulei口和ulei子接口、eth_dslgroup接口、qx接口和qx子接口、bvi接口和bvi子接口、三层VLAN接口、dsl接口、pos口、posgroup接口、gre隧道接口、v6隧道接口、dialer口、vbui接口、serial接口、multilink接口、virtual_template虚接口、gpon_vport接口和gpon_vport子接口、svi接口和svi子接口，dcn接口、gtunnel_group接口和te_gtunnel接口、vxlan_tunnel接口。








缺省 :

缺省情况下该调试功能关闭。 






使用说明 :

该命令工作于特权模式。执行该命令打开调试功开关，可以实时打印所有收发的ND报文信息。不指定接口名使用本命令，将打印设备上所有的ND报文；如果指定接口名执行该命令，则仅打印该接口的收发的ND报文。





范例 :

打开该调试命令命令，设备收到ND相关报文，显示如下：ZXROSNG#debug ipv6 nd6IPv6 Neighbor Discovery debugging is onZXR10 PFU-0/20/0 2011-1-23 19:05:03 ICMPv6-ND: NOSTAT -> INCOM: 1::1ZXR10 PFU-0/20/0 2011-1-23 19:05:03 ICMPv6-ND: Sending NS on gei-0/1/0/5 for 1::1ZXR10 PFU-0/20/0 2011-1-23 19:05:03 ICMPv6-ND: Received NA on gei-0/1/0/5 for 1::1ZXR10 PFU-0/20/0 2011-1-23 19:05:03 ICMPv6-ND: INCOM -> REACH: 1::1ZXR10 PFU-0/20/0 2011-1-23 19:05:04 ICMPv6-ND: Sending RA on gei-0/1/0/5:M=0，O=0，lifetime=1800，reachable=0，retransmit=0ZXR10 PFU-0/20/0 2011-1-23 19:05:04 ICMPv6-ND:     MTU = 1500ZXR10 PFU-0/20/0 2011-1-23 19:05:04 ICMPv6-ND:     prefix = 1::/64 onlink autoconfigZXR10 PFU-0/20/0 2011-1-23 19:05:04 ICMPv6-ND:        604800/86400(valid/preferred)ZXR10 PFU-0/20/0 2011-1-23 19:05:04 ICMPv6-ND:     prefix = 400::/64 offlink not autoconfigZXR10 PFU-0/20/0 2011-1-23 19:05:04 ICMPv6-ND:        200/100(valid/preferred)






相关命令 :

show debug nd6 




## debug nd6 trace 


debug nd6 trace 




命令功能 :

该命令用于控制ND trace信息打印调试功能，是ND trace信息打印的调试开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug nd6 trace 
  [interface 
 ＜interface-name 
＞] [limit-count 
 ＜count 
＞]

no debug nd6 trace 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|支持ND协议的所有接口。
＜count＞|trace信息打印数量，取值范围1-65535








缺省 :

缺省情况下该调试功能关闭。 






使用说明 :

执行该命令打开ND trace调试功能开关，不加参数时可以实时打印所有ND trace信息。指定接口时，只打印该接口的ND trace信息。配置打印数量时，仅打印配置数量的ND trace信息。





范例 :

打开该调试命令，设备收到ND相关报文：ZXROSNG#debug nd6 trace limit-count 10000ND6 trace debugging is on显示debug命令配置情况：ZXROSNG#show debug nd6ND6:  ND6 trace debugging is on,remaining number is 10000收发报文时显示实时trace信息：ZXR10 MPU-0/20/0 2017-2-9 02:16:20 Receive NS packet on gei-0/1/0/1src ip: 100::2dst ip: ff02::1:ff00:1target ip: 100::1The packet is dealt successfullyZXR10 MPU-0/20/0 2017-2-9 02:16:20 Send NA packet on gei-0/1/0/1target ip: 100::1Send the packet successfullyZXR10 MPU-0/20/0 2017-2-9 02:16:25 Send NS packet on gei-0/1/0/1target ip: 100::2Send the packet successfullyZXR10 MPU-0/20/0 2017-2-9 02:16:25 Receive NA packet on gei-0/1/0/1src ip: 100::2dst ip: 100::1target ip: 100::2The packet is dealt successfully





相关命令 :

show debug nd6 




## ipv6 dad-attempts 


ipv6 dad-attempts 




命令功能 :

该命令用于设置对接口的IPv6地址进行DAD（Duplicate Address Detection，重复地址检测）的次数。no命令恢复为默认值。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 dad-attempts 
  ＜dad-number 
＞

no ipv6 dad-attempts 








命令参数解释 :



参数|描述
---|---
＜dad-number＞|作用：配置的DAD报文探测次数取值范围：0-10。默认值：3。配置为0时，表示该接口下的IPv6地址不需要进行DAD。








缺省 :

缺省情况下DAD数值为3次。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。地址重复地址检测（DAD）发送邻居请求报文给链路上的组播地址，如果没有收到回应的邻居通告报文，则认为地址是可以使用的。






范例 :

设置接口gei-0/1/0/1的DAD发送探测报文次数为5：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config- if-gei-0/1/0/1)#ipv6 dad-attempts 5
恢复接口gei-0/1/0/1的DAD发送探测报文次数为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config- if-gei-0/1/0/1)#ipv6 dad-attempts 5






相关命令 :

无 




## ipv6 dad-attempts 


ipv6 dad-attempts 




命令功能 :

该命令用于设置对接口的IPv6地址进行DAD（Duplicate Address Detection，重复地址检测）的次数。no命令恢复为默认值。






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 dad-attempts 
  ＜dad-number 
＞

no ipv6 dad-attempts 








命令参数解释 :



参数|描述
---|---
＜dad-number＞|作用：配置的DAD报文探测次数取值范围：0-10。默认值：3。配置为0时，表示该接口下的IPv6地址不需要进行DAD。








缺省 :

缺省情况下DAD数值为3次。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。地址重复地址检测（DAD）发送邻居请求报文给链路上的组播地址，如果没有收到回应的邻居通告报文，则认为地址是可以使用的。






范例 :

设置接口gei-0/1/0/1的DAD发送探测报文次数为5：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config- if-gei-0/1/0/1)#ipv6 dad-attempts 5
恢复接口gei-0/1/0/1的DAD发送探测报文次数为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config- if-gei-0/1/0/1)#ipv6 dad-attempts 5






相关命令 :

无 




## ipv6 dad-attempts 


ipv6 dad-attempts 




命令功能 :

该命令用于设置对接口的IPv6地址进行DAD（Duplicate Address Detection，重复地址检测）的次数。no命令恢复为默认值。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,以太接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15 






命令格式 :


ipv6 dad-attempts 
  ＜dad-number 
＞

no ipv6 dad-attempts 








命令参数解释 :



参数|描述
---|---
＜dad-number＞|作用：配置的DAD报文探测次数取值范围：0-10。默认值：3。配置为0时，表示该接口下的IPv6地址不需要进行DAD。








缺省 :

缺省情况下DAD数值为3次。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。地址重复地址检测（DAD）发送邻居请求报文给链路上的组播地址，如果没有收到回应的邻居通告报文，则认为地址是可以使用的。






范例 :

设置接口gei-0/1/0/1的DAD发送探测报文次数为5：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config- if-gei-0/1/0/1)#ipv6 dad-attempts 5
恢复接口gei-0/1/0/1的DAD发送探测报文次数为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config- if-gei-0/1/0/1)#ipv6 dad-attempts 5






相关命令 :

无 




## ipv6 dad-attempts 


ipv6 dad-attempts 




命令功能 :

该命令用于设置对接口的IPv6地址进行DAD（Duplicate Address Detection，重复地址检测）的次数。no命令恢复为默认值。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 dad-attempts 
  ＜dad-number 
＞

no ipv6 dad-attempts 








命令参数解释 :



参数|描述
---|---
＜dad-number＞|作用：配置的DAD报文探测次数取值范围：0-10。默认值：3。配置为0时，表示该接口下的IPv6地址不需要进行DAD。








缺省 :

缺省情况下DAD数值为3次。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。地址重复地址检测（DAD）发送邻居请求报文给链路上的组播地址，如果没有收到回应的邻居通告报文，则认为地址是可以使用的。






范例 :

设置接口gei-0/1/0/1的DAD发送探测报文次数为5：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config- if-gei-0/1/0/1)#ipv6 dad-attempts 5
恢复接口gei-0/1/0/1的DAD发送探测报文次数为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config- if-gei-0/1/0/1)#ipv6 dad-attempts 5






相关命令 :

无 




## ipv6 nd dad-proxy 


ipv6 nd dad-proxy 




命令功能 :

该命令用于开启接口的link local类型地址的DAD代理功能。no命令关闭该功能。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,supervlan接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

qx子接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,supervlan接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd dad-proxy 
 link-local 


no ipv6 nd dad-proxy 
 link-local 








命令参数解释 :



参数|描述
---|---
link-local|表示针对link-local地址








缺省 :

缺省情况下link local地址不启用DAD代理功能。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能关闭。





范例 :

开启gei-0/1/0/1接口的link local类型地址的DAD代理功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd dad-proxy link-local关闭gei-0/1/0/1接口的link local类型地址的DAD代理功能ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd dad-proxy link-locall





相关命令 :

无 




## ipv6 nd dad-proxy 


ipv6 nd dad-proxy 




命令功能 :

该命令用于开启接口的link local类型地址的DAD代理功能。no命令关闭该功能。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,smartgroup子接口模式:15,以太接口模式:15,千兆以太接口模式:15,10G以太接口模式:15,smartgroup接口模式:15 






命令格式 :


ipv6 nd dad-proxy 
 link-local 


no ipv6 nd dad-proxy 
 link-local 








命令参数解释 :



参数|描述
---|---
link-local|表示针对link-local地址








缺省 :

缺省情况下link local地址不启用DAD代理功能。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能关闭。





范例 :

开启gei-0/1/0/1接口的link local类型地址的DAD代理功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd dad-proxy link-local关闭gei-0/1/0/1接口的link local类型地址的DAD代理功能ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd dad-proxy link-locall





相关命令 :

无 




## ipv6 nd default-route-priority 


ipv6 nd default-route-priority 




命令功能 :

主机协议栈功能开启时，该命令用于配置自动产生的默认路由的优先级。no命令恢复默认值。





命令模式 :

 IPv6隧道接口模式,dialer接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,serial接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,ulei接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,IPv6隧道接口模式:15,dialer接口模式:15,multilink接口模式:15,pos接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd default-route-priority 
  ＜default-route-priority 
＞

no ipv6 nd default-route-priority 








命令参数解释 :



参数|描述
---|---
＜default-route-priority＞|作用：配置自动产生的默认路由的优先级。取值范围：1-254。无效值：0，表示使用平台默认值200。值越小，优先级越高。








缺省 :

缺省情况下，自动产生的默认路由的优先级是200。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。该命令需要开启主机协议栈功能，配置才生效。该命令暂时只用于路由器设备，交换机上不支持。





范例 :

在gei-0/1/0/1接口上配置自动产生的默认路由的优先级为10：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd default-route- priority 10在gei-0/1/0/1接口上恢复自动产生的默认路由的优先级：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd default-route- priority





相关命令 :

ipv6 nd host 




## ipv6 nd default-route-priority 


ipv6 nd default-route-priority 




命令功能 :

主机协议栈功能开启时，该命令用于配置自动产生的默认路由的优先级。no命令恢复默认值。





命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太接口模式:15,千兆以太接口模式:15,10G以太接口模式:15,smartgroup子接口模式:15,smartgroup接口模式:15,以太子接口模式:15 






命令格式 :


ipv6 nd default-route-priority 
  ＜default-route-priority 
＞

no ipv6 nd default-route-priority 








命令参数解释 :



参数|描述
---|---
＜default-route-priority＞|作用：配置自动产生的默认路由的优先级。取值范围：1-254。无效值：0，表示使用平台默认值200。值越小，优先级越高。








缺省 :

缺省情况下，自动产生的默认路由的优先级是200。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。该命令需要开启主机协议栈功能，配置才生效。该命令暂时只用于路由器设备，交换机上不支持。





范例 :

在gei-0/1/0/1接口上配置自动产生的默认路由的优先级为10：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd default-route- priority 10在gei-0/1/0/1接口上恢复自动产生的默认路由的优先级：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd default-route- priority





相关命令 :

ipv6 nd host 




## ipv6 nd host 


ipv6 nd host 




命令功能 :

该命令用于使能IPv6协议的ND主机协议栈功能，该功能可以使设备具备主机性质，发送RS报文，接收RA报文，通过收到的RA报文添加默认路由和ipv6地址。no命令关闭该功能。






命令模式 :

 IPv6隧道接口模式,dialer接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,serial接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,ulei接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,IPv6隧道接口模式:15,dialer接口模式:15,multilink接口模式:15,pos接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd host 
 

no ipv6 nd host 








命令参数解释 :


					无
				 






缺省 :

默认情况下该功能无效，设备使能路由协议功能，不能发送RS报文和接收RA报文。因此设备在关闭抑制发送RA报文开关后，不能使能该功能。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下该功能无效，设备使能路由协议功能，不能发送RS报文和接收RA报文。因此设备在关闭抑制发送RA报文开关后，不能使能该功能。由于主机协议栈功能与路由功能是互斥的，因此该命令同no ipv6 nd suppress-ra命令互斥。该功能只在路由器设备上使用，交换机设备不用。该功能主要是ZSR项目使用。





范例 :

在gei-0/1/0/1接口上开启ND主机协议栈功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd host在gei-0/1/0/1接口上关闭ND主机协议栈功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd host





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra 



## ipv6 nd host 


ipv6 nd host 




命令功能 :

该命令用于使能IPv6协议的ND主机协议栈功能，该功能可以使设备具备主机性质，发送RS报文，接收RA报文，通过收到的RA报文添加默认路由和ipv6地址。no命令关闭该功能。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

smartgroup子接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太接口模式:15,以太子接口模式:15,千兆以太接口模式:15 






命令格式 :


ipv6 nd host 
 

no ipv6 nd host 








命令参数解释 :


					无
				 






缺省 :

默认情况下该功能无效，设备使能路由协议功能，不能发送RS报文和接收RA报文。因此设备在关闭抑制发送RA报文开关后，不能使能该功能。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下该功能无效，设备使能路由协议功能，不能发送RS报文和接收RA报文。因此设备在关闭抑制发送RA报文开关后，不能使能该功能。由于主机协议栈功能与路由功能是互斥的，因此该命令同no ipv6 nd suppress-ra命令互斥。该功能只在路由器设备上使用，交换机设备不用。该功能主要是ZSR项目使用。





范例 :

在gei-0/1/0/1接口上开启ND主机协议栈功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd host在gei-0/1/0/1接口上关闭ND主机协议栈功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd host





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra 



## ipv6 nd inner-vlan-proxy 


ipv6 nd inner-vlan-proxy 




命令功能 :

该命令用于开启相同接口相同VLAN内的ND代理功能。如果两个用户属于相同的VLAN，但VLAN内配置了用户隔离。用户间要互通，需要在关联了VLAN的接口上启动VLAN内ND代理功能。这时需要在代理接口上配置该命令。no命令关闭该功能。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

qx子接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd inner-vlan-proxy 
 

no ipv6 nd inner-vlan-proxy 








命令参数解释 :


					无
				 






缺省 :

缺省情况接口下不开启vlan内ND代理 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能关闭。对于BRAS设备，在VCC接口上设置该功能。





范例 :

配置gei-0/1/0/1.10接口上相同VLAN内ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) ipv6 nd inner-vlan-proxy关闭gei-0/1/0/1.10接口上相同VLAN内ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) no ipv6 nd inner-vlan-proxy





相关命令 :

无 




## ipv6 nd inner-vlan-proxy 


ipv6 nd inner-vlan-proxy 




命令功能 :

该命令用于开启相同接口相同VLAN内的ND代理功能。如果两个用户属于相同的VLAN，但VLAN内配置了用户隔离。用户间要互通，需要在关联了VLAN的接口上启动VLAN内ND代理功能。这时需要在代理接口上配置该命令。no命令关闭该功能。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,smartgroup接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,以太接口模式:15,以太子接口模式:15 






命令格式 :


ipv6 nd inner-vlan-proxy 
 

no ipv6 nd inner-vlan-proxy 








命令参数解释 :


					无
				 






缺省 :

缺省情况接口下不开启vlan内ND代理 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能关闭。对于BRAS设备，在VCC接口上设置该功能。





范例 :

配置gei-0/1/0/1.10接口上相同VLAN内ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) ipv6 nd inner-vlan-proxy关闭gei-0/1/0/1.10接口上相同VLAN内ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) no ipv6 nd inner-vlan-proxy





相关命令 :

无 




## ipv6 nd inner-vlan-proxy 


ipv6 nd inner-vlan-proxy 




命令功能 :

该命令用于开启相同接口相同VLAN内的ND代理功能。如果两个用户属于相同的VLAN，但VLAN内配置了用户隔离。用户间要互通，需要在关联了VLAN的接口上启动VLAN内ND代理功能。这时需要在代理接口上配置该命令。no命令关闭该功能。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd inner-vlan-proxy 
 

no ipv6 nd inner-vlan-proxy 








命令参数解释 :


					无
				 






缺省 :

缺省情况接口下不开启vlan内ND代理 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能关闭。对于BRAS设备，在VCC接口上设置该功能。





范例 :

配置gei-0/1/0/1.10接口上相同VLAN内ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) ipv6 nd inner-vlan-proxy关闭gei-0/1/0/1.10接口上相同VLAN内ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) no ipv6 nd inner-vlan-proxy





相关命令 :

无 




## ipv6 nd inter-vlan-proxy 


ipv6 nd inter-vlan-proxy 




命令功能 :

该命令用于开启相同接口，不同vlan间ND代理功能。如果两个用户属于不同的VLAN，用户间要进行二层互通，需要在关联了VLAN 的接口上启动VLAN 间ND 代理功能。no命令关闭该功能。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

qx子接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd inter-vlan-proxy 
 

no ipv6 nd inter-vlan-proxy 








命令参数解释 :


					无
				 






缺省 :

缺省情况接口下不开启vlan间ND代理。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能关闭。对于BRAS设备，在VCC接口上设置该功能。





范例 :

配置gei-0/1/0/1.10接口上不同VLAN之间 的ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) ipv6 nd inter-vlan-proxy关闭gei-0/1/0/1.10接口上 不同VLAN之间ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) no ipv6 nd inter-vlan-proxy





相关命令 :

无 




## ipv6 nd inter-vlan-proxy 


ipv6 nd inter-vlan-proxy 




命令功能 :

该命令用于开启相同接口，不同vlan间ND代理功能。如果两个用户属于不同的VLAN，用户间要进行二层互通，需要在关联了VLAN 的接口上启动VLAN 间ND 代理功能。no命令关闭该功能。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

千兆以太接口模式:15,以太接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,10G以太接口模式:15,smartgroup接口模式:15 






命令格式 :


ipv6 nd inter-vlan-proxy 
 

no ipv6 nd inter-vlan-proxy 








命令参数解释 :


					无
				 






缺省 :

缺省情况接口下不开启vlan间ND代理。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能关闭。对于BRAS设备，在VCC接口上设置该功能。





范例 :

配置gei-0/1/0/1.10接口上不同VLAN之间 的ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) ipv6 nd inter-vlan-proxy关闭gei-0/1/0/1.10接口上 不同VLAN之间ND代理功能：ZXROSNG(config)# interface gei-0/1/0/1.10ZXROSNG(config-if- gei-0/1/0/1.10) no ipv6 nd inter-vlan-proxy





相关命令 :

无 




## ipv6 nd managed-config-flag 


ipv6 nd managed-config-flag 




命令功能 :

该命令用于设置接口发送的RA（路由器通告）报文中“管理地址配置”字段，即设置RA报文中M位的值为1，默认值为0。no命令将该字段恢复为默认值。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd managed-config-flag 
 

no ipv6 nd managed-config-flag 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，RA报文中的“管理地址配置”字段为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在RA报文中设置“管理地址配置”字段为1，表明连接在链路上的主机收到这个RA报文后，应该采用有状态的自动配置以获得地址。如果该字段没有设置，即为0，表明所连的主机不使用有状态的自动配置获得地址（可能采用无状态的地址自动配置）。默认情况下，RA报文中的“管理地址配置”字段为0。






范例 :

配置接口gei-0/1/0/1发送的RA报文中的“管理地址配置”字段为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd managed-config-flag恢复接口gei-0/1/0/1发送的RA报文中的“管理地址配置”字段为默认值：ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd managed-config-flag





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd managed-config-flag 


ipv6 nd managed-config-flag 




命令功能 :

该命令由于配置接口发送的RA报文的“其它已规定配置”字段即RA报文的O位值为1。no命令可以清除该设置，恢复默认值即0。






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd managed-config-flag 
 

no ipv6 nd managed-config-flag 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，RA报文中的“其它已规定配置”字段为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在RA报文中设置“其它已规定配置”字段可以指示连接在链路上的主机怎样获得地址以外的自动配置信息。如果该字段置位了，表明所连的主机使用有状态的自动配置获得其他信息。如果“管理地址配置”标记置位了，不管“其它已规定配置”标记是否设置，所连的主机都将使用有状态的自动配置获得其它信息。默认情况下，RA报文中的“其它已规定配置”字段为0。






范例 :

在gei-0/1/0/1接口上设置“其它已规定配置”字段为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd other-config-flag恢复接口gei-0/1/0/1发送的RA报文中的“其它已规定配置”字段为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd other-config-flag





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd managed-config-flag 


ipv6 nd managed-config-flag 




命令功能 :

该命令用于设置接口发送的RA（路由器通告）报文中“管理地址配置”字段，即设置RA报文中M位的值为1，默认值为0。no命令将该字段恢复为默认值。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

smartgroup子接口模式:15,smartgroup接口模式:15,10G以太接口模式:15,以太子接口模式:15,以太接口模式:15,千兆以太接口模式:15 






命令格式 :


ipv6 nd managed-config-flag 
 

no ipv6 nd managed-config-flag 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，RA报文中的“管理地址配置”字段为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在RA报文中设置“管理地址配置”字段为1，表明连接在链路上的主机收到这个RA报文后，应该采用有状态的自动配置以获得地址。如果该字段没有设置，即为0，表明所连的主机不使用有状态的自动配置获得地址（可能采用无状态的地址自动配置）。默认情况下，RA报文中的“管理地址配置”字段为0。






范例 :

配置接口gei-0/1/0/1发送的RA报文中的“管理地址配置”字段为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd managed-config-flag恢复接口gei-0/1/0/1发送的RA报文中的“管理地址配置”字段为默认值：ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd managed-config-flag





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd managed-config-flag 


ipv6 nd managed-config-flag 




命令功能 :

该命令用于设置接口发送的RA（路由器通告）报文中“管理地址配置”字段，即设置RA报文中M位的值为1，默认值为0。no命令将该字段恢复为默认值。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd managed-config-flag 
 

no ipv6 nd managed-config-flag 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，RA报文中的“管理地址配置”字段为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在RA报文中设置“管理地址配置”字段为1，表明连接在链路上的主机收到这个RA报文后，应该采用有状态的自动配置以获得地址。如果该字段没有设置，即为0，表明所连的主机不使用有状态的自动配置获得地址（可能采用无状态的地址自动配置）。默认情况下，RA报文中的“管理地址配置”字段为0。






范例 :

配置接口gei-0/1/0/1发送的RA报文中的“管理地址配置”字段为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd managed-config-flag恢复接口gei-0/1/0/1发送的RA报文中的“管理地址配置”字段为默认值：ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd managed-config-flag





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd na-parse 


ipv6 nd na-parse 




命令功能 :

该命令用于开启解析NA报文功能，当不存在ND条目时，设备也可以解析NA报文并添加ND缓存条目。no命令关闭该功能。该命令主要是用于ND双发功能，当本端PE设备根据双发条目定时向对端PE主备设备发送组播NA报文时，这时备设备可能不存在对应的ND缓存条目，因此需要配置该命令，使备设备在收到NA报文时，也可以解析并添加ND缓存条目。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

qx子接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd na-parse 
 

no ipv6 nd na-parse 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，该开关默认是关闭的。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认该功能是关闭的，当相应ND缓存不存在时，不会解析收到的NA 报文。





范例 :

在gei-0/1/0/1接口上，打开ND解析NA报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd na-parse在gei-0/1/0/1接口上，关闭ND解析NA报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd na-parse





相关命令 :

show nd6 cache 




## ipv6 nd na-parse 


ipv6 nd na-parse 




命令功能 :

该命令用于开启解析NA报文功能，当不存在ND条目时，设备也可以解析NA报文并添加ND缓存条目。no命令关闭该功能。该命令主要是用于ND双发功能，当本端PE设备根据双发条目定时向对端PE主备设备发送组播NA报文时，这时备设备可能不存在对应的ND缓存条目，因此需要配置该命令，使备设备在收到NA报文时，也可以解析并添加ND缓存条目。






命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd na-parse 
 

no ipv6 nd na-parse 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，该开关默认是关闭的。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认该功能是关闭的，当相应ND缓存不存在时，不会解析收到的NA 报文。





范例 :

在gei-0/1/0/1接口上，打开ND解析NA报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd na-parse在gei-0/1/0/1接口上，关闭ND解析NA报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd na-parse





相关命令 :

show nd6 cache 




## ipv6 nd na-parse 


ipv6 nd na-parse 




命令功能 :

该命令用于开启解析NA报文功能，当不存在ND条目时，设备也可以解析NA报文并添加ND缓存条目。no命令关闭该功能。该命令主要是用于ND双发功能，当本端PE设备根据双发条目定时向对端PE主备设备发送组播NA报文时，这时备设备可能不存在对应的ND缓存条目，因此需要配置该命令，使备设备在收到NA报文时，也可以解析并添加ND缓存条目。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

smartgroup接口模式:15,以太接口模式:15,千兆以太接口模式:15,smartgroup子接口模式:15,10G以太接口模式:15,以太子接口模式:15 






命令格式 :


ipv6 nd na-parse 
 

no ipv6 nd na-parse 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，该开关默认是关闭的。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认该功能是关闭的，当相应ND缓存不存在时，不会解析收到的NA 报文。





范例 :

在gei-0/1/0/1接口上，打开ND解析NA报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd na-parse在gei-0/1/0/1接口上，关闭ND解析NA报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd na-parse





相关命令 :

show nd6 cache 




## ipv6 nd na-parse 


ipv6 nd na-parse 




命令功能 :

该命令用于开启解析NA报文功能，当不存在ND条目时，设备也可以解析NA报文并添加ND缓存条目。no命令关闭该功能。该命令主要是用于ND双发功能，当本端PE设备根据双发条目定时向对端PE主备设备发送组播NA报文时，这时备设备可能不存在对应的ND缓存条目，因此需要配置该命令，使备设备在收到NA报文时，也可以解析并添加ND缓存条目。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd na-parse 
 

no ipv6 nd na-parse 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，该开关默认是关闭的。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认该功能是关闭的，当相应ND缓存不存在时，不会解析收到的NA 报文。





范例 :

在gei-0/1/0/1接口上，打开ND解析NA报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd na-parse在gei-0/1/0/1接口上，关闭ND解析NA报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd na-parse





相关命令 :

show nd6 cache 




## ipv6 nd nud-switch 


ipv6 nd nud-switch 




命令功能 :

该命令用于在接口下配置ND条目邻居不可达探测开关，从而控制该接口是否开启邻居不可达探测功能。该功能开启时，当接口上的ND缓存条目处于stale状态时，如果有报文需要从控制面发送，则首先要进行ND不可达探测，判断邻居是否存在，探测成功，对应ND条目会切换成reachable状态，然后将报文发送。该功能默认是打开的。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

qx子接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd nud-switch 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|使能ipv6 nd nud-switch，表示开关打开，可以进行邻居可达性探测
disable|去使能ipv6 nd nud-switch，表示开关关闭，不可以进行邻居可达性探测








缺省 :

缺省情况下无配置，该开关是打开的，会进行邻居可达性探测 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。缺省情况下无配置，该开关是打开的，平台会进行邻居不可达性探测。在接口上关闭邻居不可达性探测开关，该接口下的ND缓存条目不可以进行邻居不可达探测，缺省情况下该开关是打开的。接口上邻居不可达性探测开关关闭时，无论全局配置是打开还是关闭，该接口上的ND缓存条目都不能进行邻居不可达探测。






范例 :

在gei-0/1/0/1接口上，使能ND邻居不可达探测功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd nud-switch enabe在gei-0/1/0/1接口上，关闭ND邻居不可达探测功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd nud-switch disable





相关命令 :

nd nud-switch 




## ipv6 nd nud-switch 


ipv6 nd nud-switch 




命令功能 :

该命令用于在接口下配置ND条目邻居不可达探测开关，从而控制该接口是否开启邻居不可达探测功能。该功能开启时，当接口上的ND缓存条目处于stale状态时，如果有报文需要从控制面发送，则首先要进行ND不可达探测，判断邻居是否存在，探测成功，对应ND条目会切换成reachable状态，然后将报文发送。该功能默认是打开的。






命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd nud-switch 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|使能ipv6 nd nud-switch，表示开关打开，可以进行邻居可达性探测
disable|去使能ipv6 nd nud-switch，表示开关关闭，不可以进行邻居可达性探测








缺省 :

缺省情况下无配置，该开关是打开的，会进行邻居可达性探测 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。缺省情况下无配置，该开关是打开的，平台会进行邻居不可达性探测。在接口上关闭邻居不可达性探测开关，该接口下的ND缓存条目不可以进行邻居不可达探测，缺省情况下该开关是打开的。接口上邻居不可达性探测开关关闭时，无论全局配置是打开还是关闭，该接口上的ND缓存条目都不能进行邻居不可达探测。






范例 :

在gei-0/1/0/1接口上，使能ND邻居不可达探测功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd nud-switch enabe在gei-0/1/0/1接口上，关闭ND邻居不可达探测功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd nud-switch disable





相关命令 :

nd nud-switch 




## ipv6 nd nud-switch 


ipv6 nd nud-switch 




命令功能 :

该命令用于在接口下配置ND条目邻居不可达探测开关，从而控制该接口是否开启邻居不可达探测功能。该功能开启时，当接口上的ND缓存条目处于stale状态时，如果有报文需要从控制面发送，则首先要进行ND不可达探测，判断邻居是否存在，探测成功，对应ND条目会切换成reachable状态，然后将报文发送。该功能默认是打开的。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,以太接口模式:15,千兆以太接口模式:15,smartgroup子接口模式:15,smartgroup接口模式:15,10G以太接口模式:15 






命令格式 :


ipv6 nd nud-switch 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|使能ipv6 nd nud-switch，表示开关打开，可以进行邻居可达性探测
disable|去使能ipv6 nd nud-switch，表示开关关闭，不可以进行邻居可达性探测








缺省 :

缺省情况下无配置，该开关是打开的，会进行邻居可达性探测 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。缺省情况下无配置，该开关是打开的，平台会进行邻居不可达性探测。在接口上关闭邻居不可达性探测开关，该接口下的ND缓存条目不可以进行邻居不可达探测，缺省情况下该开关是打开的。接口上邻居不可达性探测开关关闭时，无论全局配置是打开还是关闭，该接口上的ND缓存条目都不能进行邻居不可达探测。






范例 :

在gei-0/1/0/1接口上，使能ND邻居不可达探测功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd nud-switch enabe在gei-0/1/0/1接口上，关闭ND邻居不可达探测功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd nud-switch disable





相关命令 :

nd nud-switch 




## ipv6 nd nud-switch 


ipv6 nd nud-switch 




命令功能 :

该命令用于在接口下配置ND条目邻居不可达探测开关，从而控制该接口是否开启邻居不可达探测功能。该功能开启时，当接口上的ND缓存条目处于stale状态时，如果有报文需要从控制面发送，则首先要进行ND不可达探测，判断邻居是否存在，探测成功，对应ND条目会切换成reachable状态，然后将报文发送。该功能默认是打开的。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd nud-switch 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|使能ipv6 nd nud-switch，表示开关打开，可以进行邻居可达性探测
disable|去使能ipv6 nd nud-switch，表示开关关闭，不可以进行邻居可达性探测








缺省 :

缺省情况下无配置，该开关是打开的，会进行邻居可达性探测 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。缺省情况下无配置，该开关是打开的，平台会进行邻居不可达性探测。在接口上关闭邻居不可达性探测开关，该接口下的ND缓存条目不可以进行邻居不可达探测，缺省情况下该开关是打开的。接口上邻居不可达性探测开关关闭时，无论全局配置是打开还是关闭，该接口上的ND缓存条目都不能进行邻居不可达探测。






范例 :

在gei-0/1/0/1接口上，使能ND邻居不可达探测功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd nud-switch enabe在gei-0/1/0/1接口上，关闭ND邻居不可达探测功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd nud-switch disable





相关命令 :

nd nud-switch 




## ipv6 nd other-config-flag 


ipv6 nd other-config-flag 




命令功能 :

该命令由于配置接口发送的RA报文的“其它已规定配置”字段即RA报文的O位值为1。no命令可以清除该设置，恢复默认值即0。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd other-config-flag 
 

no ipv6 nd other-config-flag 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，RA报文中的“其它已规定配置”字段为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在RA报文中设置“其它已规定配置”字段可以指示连接在链路上的主机怎样获得地址以外的自动配置信息。如果该字段置位了，表明所连的主机使用有状态的自动配置获得其他信息。如果“管理地址配置”标记置位了，不管“其它已规定配置”标记是否设置，所连的主机都将使用有状态的自动配置获得其它信息。默认情况下，RA报文中的“其它已规定配置”字段为0。






范例 :

在gei-0/1/0/1接口上设置“其它已规定配置”字段为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd other-config-flag恢复接口gei-0/1/0/1发送的RA报文中的“其它已规定配置”字段为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd other-config-flag





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd other-config-flag 


ipv6 nd other-config-flag 




命令功能 :

设置接口发送的路由器通告报文的“其它已规定配置”字段报文的O位的值为1。no命令可以清除该设置，恢复默认值。 






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :



ipv6 nd other-config-flag 
 

no ipv6 nd other-config-flag 








命令参数解释 :


					无
				 






缺省 :

缺省路由通告报文的O位为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在RA报文中设置“其它已规定配置”字段可以指示连接在链路上的主机怎样获得地址以外的自动配置信息。如果该字段置位了，表明所连的主机使用有状态的自动配置获得其他信息。如果“管理地址配置”标记置位了，不管“其它已规定配置”标记是否设置，所连的主机都将使用有状态的自动配置获得其它信息。默认情况下，RA报文中的“其它已规定配置”字段为0。





范例 :

设置“其它已规定配置”字段为1：ZXROSNG(config-if)#ipv6 nd other-config-flag





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd other-config-flag 


ipv6 nd other-config-flag 




命令功能 :

该命令由于配置接口发送的RA报文的“其它已规定配置”字段即RA报文的O位值为1。no命令可以清除该设置，恢复默认值即0。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,以太接口模式:15,以太子接口模式:15,smartgroup接口模式:15 






命令格式 :


ipv6 nd other-config-flag 
 

no ipv6 nd other-config-flag 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，RA报文中的“其它已规定配置”字段为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在RA报文中设置“其它已规定配置”字段可以指示连接在链路上的主机怎样获得地址以外的自动配置信息。如果该字段置位了，表明所连的主机使用有状态的自动配置获得其他信息。如果“管理地址配置”标记置位了，不管“其它已规定配置”标记是否设置，所连的主机都将使用有状态的自动配置获得其它信息。默认情况下，RA报文中的“其它已规定配置”字段为0。






范例 :

在gei-0/1/0/1接口上设置“其它已规定配置”字段为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd other-config-flag恢复接口gei-0/1/0/1发送的RA报文中的“其它已规定配置”字段为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd other-config-flag





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd other-config-flag 


ipv6 nd other-config-flag 




命令功能 :

该命令由于配置接口发送的RA报文的“其它已规定配置”字段即RA报文的O位值为1。no命令可以清除该设置，恢复默认值即0。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd other-config-flag 
 

no ipv6 nd other-config-flag 








命令参数解释 :


					无
				 






缺省 :

缺省情况下，RA报文中的“其它已规定配置”字段为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在RA报文中设置“其它已规定配置”字段可以指示连接在链路上的主机怎样获得地址以外的自动配置信息。如果该字段置位了，表明所连的主机使用有状态的自动配置获得其他信息。如果“管理地址配置”标记置位了，不管“其它已规定配置”标记是否设置，所连的主机都将使用有状态的自动配置获得其它信息。默认情况下，RA报文中的“其它已规定配置”字段为0。






范例 :

在gei-0/1/0/1接口上设置“其它已规定配置”字段为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd other-config-flag恢复接口gei-0/1/0/1发送的RA报文中的“其它已规定配置”字段为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd other-config-flag





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd prefix 


ipv6 nd prefix 




命令功能 :

该命令用于在接口上配置发送的路由器通告报文中的前缀选项。可以指定每个前缀的有效生存时间、首先生存时间、在线标志和自动配置标志。可以通过no命令清除该接口下指定的前缀选项。





命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,qx子接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd prefix 
  ＜ipv6-address 
＞ [＜valid-lifetime 
＞ ＜preferred-lifetime 
＞] [{[off-link 
],[no-autoconfig 
]}]
no ipv6 nd prefix 
  ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|包含在路由器通告中的网络前缀。前缀长度的范围：1-128。
＜valid-lifetime＞|前缀的有效生存时间，单位秒。默认值：2592000。配置范围是0-4294967295。
＜preferred-lifetime＞|首选生存时间，单位秒。默认值：604800。配置范围：0-4294967295。
off-link|配置这个标记表明前缀的L位（在线标志）没有置位。L位如果置位，表示前缀可以用于在线确定，就是说，属于此前缀的所有地址都在线，没有置位时，一些地址可以在线，一些则离线。默认该标记不配置，L位标记置位。
no-autoconfig|配置这个标记表明前缀的A位（自动产生地址标志）没有置位，表示链路上的主机不能用本前缀作IPv6地址自动配置。默认该标记不配置，A位标志置位。








缺省 :

缺省情况下，所有接口上配置的地址前缀在IPV6路由器通告报文中的有效生存时间是2592000秒（30天），首选生存时间是604800秒（7天），“在线”和“自动配置”标记置1。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。本命令可以修改已有的前缀选项的参数，也可以在路由器通告中增加新的前缀选项。每个接口最多配置16个前缀。如果不指定参数配置前缀，则参数使用其默认值。配置的前缀地址不能为LinkLocal地址、组播地址、回环地址和不确定地址。相同接口下不能配置前缀地址相同，但是前缀长度不同的前缀。同一个VRF内的不同接口不能配置相同的前缀。接口上的地址与配置的前缀也会有冲突检查。相同接口下，不能出现前缀地址相同，但是前缀不同的地址和前缀；同一VRF内的不同接口不能配置前缀相同的地址和前缀。接口上如果配置了前缀，则接口不能绑定VRF，必须先删除前缀才能绑定VRF；同时在接口上解绑VRF前，需要先删除接口上的前缀配置。配置前缀的首选生存时间不能大于有效生存时间。






范例 :

在gei-0/1/0/1接口上配置网络前缀为400::，长度为64，有效生存时间为200秒，首选生存时间为100秒，L位、A位不置位：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd prefix 400::/64  200 100 off-link no-autoconfig关闭抑制发送RA报文的开关，并打开debug开关打印RA报文：ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd suppress-raZXROSNG(config-if-gei-0/1/0/1)#endZXROSNG#debug ipv6 ndIPv6 Neighbor Discovery debugging is onZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND: Sending RA on gei-0/1/0/1:M=0，O=0，lifetime=1800，reachable=0，retransmit=0ZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND:     MTU = 1500ZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND:     prefix = 400::/64 offlink not autoconfigICMPv6-ND:        200/100(valid/preferred)在gei-0/1/0/1接口上删除配置的网络前缀：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd prefix 400::/64





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd prefix 


ipv6 nd prefix 




命令功能 :

该命令用于在接口上配置发送的路由器通告报文中的前缀选项。可以指定每个前缀的有效生存时间、首先生存时间、在线标志和自动配置标志。可以通过no命令清除该接口下指定的前缀选项。





命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd prefix 
  ＜ipv6-address 
＞ [＜valid-lifetime 
＞ ＜preferred-lifetime 
＞] [{[off-link 
],[no-autoconfig 
]}]
no ipv6 nd prefix 
  ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|包含在路由器通告中的网络前缀。前缀长度的范围：1-128。
＜valid-lifetime＞|前缀的有效生存时间，单位秒。默认值：2592000。配置范围是0-4294967295。
＜preferred-lifetime＞|首选生存时间，单位秒。默认值：604800。配置范围：0-4294967295。
off-link|配置这个标记表明前缀的L位（在线标志）没有置位。L位如果置位，表示前缀可以用于在线确定，就是说，属于此前缀的所有地址都在线，没有置位时，一些地址可以在线，一些则离线。默认该标记不配置，L位标记置位。
no-autoconfig|配置这个标记表明前缀的A位（自动产生地址标志）没有置位，表示链路上的主机不能用本前缀作IPv6地址自动配置。默认该标记不配置，A位标志置位。








缺省 :

缺省情况下，所有接口上配置的地址前缀在IPV6路由器通告报文中的有效生存时间是2592000秒（30天），首选生存时间是604800秒（7天），“在线”和“自动配置”标记置1。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。本命令可以修改已有的前缀选项的参数，也可以在路由器通告中增加新的前缀选项。每个接口最多配置16个前缀。如果不指定参数配置前缀，则参数使用其默认值。配置的前缀地址不能为LinkLocal地址、组播地址、回环地址和不确定地址。相同接口下不能配置前缀地址相同，但是前缀长度不同的前缀。同一个VRF内的不同接口不能配置相同的前缀。接口上的地址与配置的前缀也会有冲突检查。相同接口下，不能出现前缀地址相同，但是前缀不同的地址和前缀；同一VRF内的不同接口不能配置前缀相同的地址和前缀。接口上如果配置了前缀，则接口不能绑定VRF，必须先删除前缀才能绑定VRF；同时在接口上解绑VRF前，需要先删除接口上的前缀配置。配置前缀的首选生存时间不能大于有效生存时间。






范例 :

在gei-0/1/0/1接口上配置网络前缀为400::，长度为64，有效生存时间为200秒，首选生存时间为100秒，L位、A位不置位：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd prefix 400::/64  200 100 off-link no-autoconfig关闭抑制发送RA报文的开关，并打开debug开关打印RA报文：ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd suppress-raZXROSNG(config-if-gei-0/1/0/1)#endZXROSNG#debug ipv6 ndIPv6 Neighbor Discovery debugging is onZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND: Sending RA on gei-0/1/0/1:M=0，O=0，lifetime=1800，reachable=0，retransmit=0ZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND:     MTU = 1500ZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND:     prefix = 400::/64 offlink not autoconfigICMPv6-ND:        200/100(valid/preferred)在gei-0/1/0/1接口上删除配置的网络前缀：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd prefix 400::/64





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd prefix 


ipv6 nd prefix 




命令功能 :

该命令用于在接口上配置发送的路由器通告报文中的前缀选项。可以指定每个前缀的有效生存时间、首先生存时间、在线标志和自动配置标志。可以通过no命令清除该接口下指定的前缀选项。





命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太接口模式:15,千兆以太接口模式:15,smartgroup子接口模式:15,smartgroup接口模式:15,10G以太接口模式:15,以太子接口模式:15 






命令格式 :


ipv6 nd prefix 
  ＜ipv6-address 
＞ [＜valid-lifetime 
＞ ＜preferred-lifetime 
＞] [{[off-link 
],[no-autoconfig 
]}]
no ipv6 nd prefix 
  ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|包含在路由器通告中的网络前缀。前缀长度的范围：1-128。
＜valid-lifetime＞|前缀的有效生存时间，单位秒。默认值：2592000。配置范围是0-4294967295。
＜preferred-lifetime＞|首选生存时间，单位秒。默认值：604800。配置范围：0-4294967295。
off-link|配置这个标记表明前缀的L位（在线标志）没有置位。L位如果置位，表示前缀可以用于在线确定，就是说，属于此前缀的所有地址都在线，没有置位时，一些地址可以在线，一些则离线。默认该标记不配置，L位标记置位。
no-autoconfig|配置这个标记表明前缀的A位（自动产生地址标志）没有置位，表示链路上的主机不能用本前缀作IPv6地址自动配置。默认该标记不配置，A位标志置位。








缺省 :

缺省情况下，所有接口上配置的地址前缀在IPV6路由器通告报文中的有效生存时间是2592000秒（30天），首选生存时间是604800秒（7天），“在线”和“自动配置”标记置1。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。本命令可以修改已有的前缀选项的参数，也可以在路由器通告中增加新的前缀选项。每个接口最多配置16个前缀。如果不指定参数配置前缀，则参数使用其默认值。配置的前缀地址不能为LinkLocal地址、组播地址、回环地址和不确定地址。相同接口下不能配置前缀地址相同，但是前缀长度不同的前缀。同一个VRF内的不同接口不能配置相同的前缀。接口上的地址与配置的前缀也会有冲突检查。相同接口下，不能出现前缀地址相同，但是前缀不同的地址和前缀；同一VRF内的不同接口不能配置前缀相同的地址和前缀。接口上如果配置了前缀，则接口不能绑定VRF，必须先删除前缀才能绑定VRF；同时在接口上解绑VRF前，需要先删除接口上的前缀配置。配置前缀的首选生存时间不能大于有效生存时间。






范例 :

在gei-0/1/0/1接口上配置网络前缀为400::，长度为64，有效生存时间为200秒，首选生存时间为100秒，L位、A位不置位：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd prefix 400::/64  200 100 off-link no-autoconfig关闭抑制发送RA报文的开关，并打开debug开关打印RA报文：ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd suppress-raZXROSNG(config-if-gei-0/1/0/1)#endZXROSNG#debug ipv6 ndIPv6 Neighbor Discovery debugging is onZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND: Sending RA on gei-0/1/0/1:M=0，O=0，lifetime=1800，reachable=0，retransmit=0ZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND:     MTU = 1500ZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND:     prefix = 400::/64 offlink not autoconfigICMPv6-ND:        200/100(valid/preferred)在gei-0/1/0/1接口上删除配置的网络前缀：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd prefix 400::/64





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd prefix 


ipv6 nd prefix 




命令功能 :

该命令用于在接口上配置发送的路由器通告报文中的前缀选项。可以指定每个前缀的有效生存时间、首先生存时间、在线标志和自动配置标志。可以通过no命令清除该接口下指定的前缀选项。





命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd prefix 
  ＜ipv6-address 
＞ [＜valid-lifetime 
＞ ＜preferred-lifetime 
＞] [{[off-link 
],[no-autoconfig 
]}]
no ipv6 nd prefix 
  ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|包含在路由器通告中的网络前缀。前缀长度的范围：1-128。
＜valid-lifetime＞|前缀的有效生存时间，单位秒。默认值：2592000。配置范围是0-4294967295。
＜preferred-lifetime＞|首选生存时间，单位秒。默认值：604800。配置范围：0-4294967295。
off-link|配置这个标记表明前缀的L位（在线标志）没有置位。L位如果置位，表示前缀可以用于在线确定，就是说，属于此前缀的所有地址都在线，没有置位时，一些地址可以在线，一些则离线。默认该标记不配置，L位标记置位。
no-autoconfig|配置这个标记表明前缀的A位（自动产生地址标志）没有置位，表示链路上的主机不能用本前缀作IPv6地址自动配置。默认该标记不配置，A位标志置位。








缺省 :

缺省情况下，所有接口上配置的地址前缀在IPV6路由器通告报文中的有效生存时间是2592000秒（30天），首选生存时间是604800秒（7天），“在线”和“自动配置”标记置1。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。本命令可以修改已有的前缀选项的参数，也可以在路由器通告中增加新的前缀选项。每个接口最多配置16个前缀。如果不指定参数配置前缀，则参数使用其默认值。配置的前缀地址不能为LinkLocal地址、组播地址、回环地址和不确定地址。相同接口下不能配置前缀地址相同，但是前缀长度不同的前缀。同一个VRF内的不同接口不能配置相同的前缀。接口上的地址与配置的前缀也会有冲突检查。相同接口下，不能出现前缀地址相同，但是前缀不同的地址和前缀；同一VRF内的不同接口不能配置前缀相同的地址和前缀。接口上如果配置了前缀，则接口不能绑定VRF，必须先删除前缀才能绑定VRF；同时在接口上解绑VRF前，需要先删除接口上的前缀配置。配置前缀的首选生存时间不能大于有效生存时间。






范例 :

在gei-0/1/0/1接口上配置网络前缀为400::，长度为64，有效生存时间为200秒，首选生存时间为100秒，L位、A位不置位：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd prefix 400::/64  200 100 off-link no-autoconfig关闭抑制发送RA报文的开关，并打开debug开关打印RA报文：ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd suppress-raZXROSNG(config-if-gei-0/1/0/1)#endZXROSNG#debug ipv6 ndIPv6 Neighbor Discovery debugging is onZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND: Sending RA on gei-0/1/0/1:M=0，O=0，lifetime=1800，reachable=0，retransmit=0ZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND:     MTU = 1500ZXR10 PFU-0/20/0 2011-1-21 21:36:46 ICMPv6-ND:     prefix = 400::/64 offlink not autoconfigICMPv6-ND:        200/100(valid/preferred)在gei-0/1/0/1接口上删除配置的网络前缀：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd prefix 400::/64





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd proxy 


ipv6 nd proxy 




命令功能 :

该命令用于开启接口间ND代理功能，no命令关闭接口间ND代理功能。接口间ND代理功能解决同一网段不同物理网络上设备的互通问题。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,ulei子接口模式,ulei接口模式,vbui接口模式  






命令默认权限级别 :

qx子接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,vbui接口模式:15,qx接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd proxy 
 

no ipv6 nd proxy 








命令参数解释 :


					无
				 






缺省 :

缺省情况接口下不开启接口间ND代理 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。接口间ND代理功能默认关闭。






范例 :

在接口gei-0/1/0/1上开启接口间ND代理功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if- gei-0/1/0/1)# ipv6 nd proxy在接口gei-0/1/0/1上关闭接口间ND代理功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if- gei-0/1/0/1)# no ipv6 nd proxy





相关命令 :

无 




## ipv6 nd proxy 


ipv6 nd proxy 




命令功能 :

该命令用于开启接口间ND代理功能，no命令关闭接口间ND代理功能。接口间ND代理功能解决同一网段不同物理网络上设备的互通问题。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

smartgroup接口模式:15,10G以太接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,以太接口模式:15,以太子接口模式:15 






命令格式 :


ipv6 nd proxy 
 

no ipv6 nd proxy 








命令参数解释 :


					无
				 






缺省 :

缺省情况接口下不开启接口间ND代理 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。接口间ND代理功能默认关闭。






范例 :

在接口gei-0/1/0/1上开启接口间ND代理功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if- gei-0/1/0/1)# ipv6 nd proxy在接口gei-0/1/0/1上关闭接口间ND代理功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if- gei-0/1/0/1)# no ipv6 nd proxy





相关命令 :

无 




## ipv6 nd ra-curhoplimit 


ipv6 nd ra-curhoplimit 




命令功能 :

该命令用于配置在路由器通告中的curhoplimit字段的值。no命令使curhoplimit字段恢复默认值。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd ra-curhoplimit 
  ＜current-hoplimit 
＞

no ipv6 nd ra-curhoplimit 








命令参数解释 :



参数|描述
---|---
＜current-hoplimit＞|配置路由器通告中的curhoplimit字段的值。默认值：64。取值范围：0-255。0表示该路由器没有规定curhoplimit字段的值。








缺省 :

缺省情况下路由器通告中的curhoplimit字段的值为64 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。 






范例 :

设置接口gei-0/1/0/1的curhoplimit为200：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-curhoplimit 200恢复接口gei-0/1/0/1的curhoplimit为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-curhoplimit 





相关命令 :

no ipv6 nd supress-ra 




## ipv6 nd ra-curhoplimit 


ipv6 nd ra-curhoplimit 




命令功能 :

该命令用于配置在路由器通告中的curhoplimit字段的值。no命令使curhoplimit字段恢复默认值。






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd ra-curhoplimit 
  ＜current-hoplimit 
＞

no ipv6 nd ra-curhoplimit 








命令参数解释 :



参数|描述
---|---
＜current-hoplimit＞|配置路由器通告中的curhoplimit字段的值。默认值：64。取值范围：0-255。0表示该路由器没有规定curhoplimit字段的值。








缺省 :

缺省情况下路由器通告中的curhoplimit字段的值为64 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。 






范例 :

设置接口gei-0/1/0/1的curhoplimit为200：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-curhoplimit 200恢复接口gei-0/1/0/1的curhoplimit为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-curhoplimit 





相关命令 :

no ipv6 nd supress-ra 




## ipv6 nd ra-curhoplimit 


ipv6 nd ra-curhoplimit 




命令功能 :

该命令用于配置在路由器通告中的curhoplimit字段的值。no命令使curhoplimit字段恢复默认值。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,以太接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,10G以太接口模式:15,smartgroup接口模式:15 






命令格式 :


ipv6 nd ra-curhoplimit 
  ＜current-hoplimit 
＞

no ipv6 nd ra-curhoplimit 








命令参数解释 :



参数|描述
---|---
＜current-hoplimit＞|配置路由器通告中的curhoplimit字段的值。默认值：64。取值范围：0-255。0表示该路由器没有规定curhoplimit字段的值。








缺省 :

缺省情况下路由器通告中的curhoplimit字段的值为64 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。 






范例 :

设置接口gei-0/1/0/1的curhoplimit为200：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-curhoplimit 200恢复接口gei-0/1/0/1的curhoplimit为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-curhoplimit 





相关命令 :

no ipv6 nd supress-ra 




## ipv6 nd ra-curhoplimit 


ipv6 nd ra-curhoplimit 




命令功能 :

该命令用于配置在路由器通告中的curhoplimit字段的值。no命令使curhoplimit字段恢复默认值。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd ra-curhoplimit 
  ＜current-hoplimit 
＞

no ipv6 nd ra-curhoplimit 








命令参数解释 :



参数|描述
---|---
＜current-hoplimit＞|配置路由器通告中的curhoplimit字段的值。默认值：64。取值范围：0-255。0表示该路由器没有规定curhoplimit字段的值。








缺省 :

缺省情况下路由器通告中的curhoplimit字段的值为64 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。 






范例 :

设置接口gei-0/1/0/1的curhoplimit为200：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-curhoplimit 200恢复接口gei-0/1/0/1的curhoplimit为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-curhoplimit 





相关命令 :

no ipv6 nd supress-ra 




## ipv6 nd ra-interval 


ipv6 nd ra-interval 




命令功能 :

该命令用于配置接口发送路由器通告的时间间隔。no命令恢复默认的通告间隔时间。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd ra-interval 
  ＜ra-interval 
＞

no ipv6 nd ra-interval 








命令参数解释 :



参数|描述
---|---
＜ra-interval＞|路由器通告时间间隔，单位为秒。默认值：600。取值范围：3-1800。








缺省 :

缺省情况下，发送路由器通告的时间间隔600秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。设置ra-interval字段可以控制接口发送路由器通告的时间间隔，但是前提是要关闭路由器通告抑制开关，该配置才有意义。





范例 :

设置路由通告的间隔为200秒：ZXROSNG(config-if-gei-0/1/0/2)#ipv6 nd ra-interval 200





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-interval 


ipv6 nd ra-interval 




命令功能 :

该命令用于配置接口发送路由器通告的时间间隔。no命令恢复默认的通告间隔时间。






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd ra-interval 
  ＜ra-interval 
＞

no ipv6 nd ra-interval 








命令参数解释 :



参数|描述
---|---
＜ra-interval＞|路由器通告时间间隔，单位为秒。默认值：600。取值范围：3-1800。








缺省 :

缺省情况下，发送路由器通告的时间间隔600秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。设置ra-interval字段可以控制接口发送路由器通告的时间间隔，但是前提是要关闭路由器通告抑制开关，该配置才有意义。





范例 :

设置路由通告的间隔为200秒：ZXROSNG(config-if-gei-0/1/0/2)#ipv6 nd ra-interval 200





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-interval 


ipv6 nd ra-interval 




命令功能 :

该命令用于配置接口发送路由器通告的时间间隔。no命令恢复默认的通告间隔时间。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

smartgroup子接口模式:15,以太接口模式:15,以太子接口模式:15,千兆以太接口模式:15,10G以太接口模式:15,smartgroup接口模式:15 






命令格式 :


ipv6 nd ra-interval 
  ＜ra-interval 
＞

no ipv6 nd ra-interval 








命令参数解释 :



参数|描述
---|---
＜ra-interval＞|路由器通告时间间隔，单位为秒。默认值：600。取值范围：3-1800。








缺省 :

缺省情况下，发送路由器通告的时间间隔600秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。设置ra-interval字段可以控制接口发送路由器通告的时间间隔，但是前提是要关闭路由器通告抑制开关，该配置才有意义。





范例 :

设置路由通告的间隔为200秒：ZXROSNG(config-if-gei-0/1/0/2)#ipv6 nd ra-interval 200





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-interval 


ipv6 nd ra-interval 




命令功能 :

该命令用于配置接口发送路由器通告的时间间隔。no命令恢复默认的通告间隔时间。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd ra-interval 
  ＜ra-interval 
＞

no ipv6 nd ra-interval 








命令参数解释 :



参数|描述
---|---
＜ra-interval＞|路由器通告时间间隔，单位为秒。默认值：600。取值范围：3-1800。








缺省 :

缺省情况下，发送路由器通告的时间间隔600秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。设置ra-interval字段可以控制接口发送路由器通告的时间间隔，但是前提是要关闭路由器通告抑制开关，该配置才有意义。





范例 :

设置路由通告的间隔为200秒：ZXROSNG(config-if-gei-0/1/0/2)#ipv6 nd ra-interval 200





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-lifetime 


ipv6 nd ra-lifetime 




命令功能 :

该命令用于配置接口发送路由器通告中的“路由器存活时间”字段的值。no命令恢复路由器存活时间为默认值。主机收到路由器通告报文后，根据ra-lifetime字段可以设置该路由器在其默认路由器列表中的时间。





命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd ra-lifetime 
  ＜ra-lifetime 
＞

no ipv6 nd ra-lifetime 








命令参数解释 :



参数|描述
---|---
＜ra-lifetime＞|路由器存活时间，秒为单位。默认值为1800。取值范围：0-9000。








缺省 :

缺省情况下，路由器存活时间为1800秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。主机收到路由器通告报文后，根据ra-lifetime字段可以设置该路由器在其默认路由器列表中的时间。






范例 :

配置接口gei-0/1/0/1的路由器存活时间为1000秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd ra-lifetime 1000恢复接口gei-0/1/0/1的路由器存活时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-lifetime





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-lifetime 


ipv6 nd ra-lifetime 




命令功能 :

该命令用于配置接口发送路由器通告中的“路由器存活时间”字段的值。no命令恢复路由器存活时间为默认值。主机收到路由器通告报文后，根据ra-lifetime字段可以设置该路由器在其默认路由器列表中的时间。





命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd ra-lifetime 
  ＜ra-lifetime 
＞

no ipv6 nd ra-lifetime 








命令参数解释 :



参数|描述
---|---
＜ra-lifetime＞|路由器存活时间，秒为单位。默认值为1800。取值范围：0-9000。








缺省 :

缺省情况下，路由器存活时间为1800秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。主机收到路由器通告报文后，根据ra-lifetime字段可以设置该路由器在其默认路由器列表中的时间。






范例 :

配置接口gei-0/1/0/1的路由器存活时间为1000秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd ra-lifetime 1000恢复接口gei-0/1/0/1的路由器存活时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-lifetime





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-lifetime 


ipv6 nd ra-lifetime 




命令功能 :

该命令用于配置接口发送路由器通告中的“路由器存活时间”字段的值。no命令恢复路由器存活时间为默认值。主机收到路由器通告报文后，根据ra-lifetime字段可以设置该路由器在其默认路由器列表中的时间。





命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,smartgroup接口模式:15,10G以太接口模式:15,千兆以太接口模式:15,以太接口模式:15,smartgroup子接口模式:15 






命令格式 :


ipv6 nd ra-lifetime 
  ＜ra-lifetime 
＞

no ipv6 nd ra-lifetime 








命令参数解释 :



参数|描述
---|---
＜ra-lifetime＞|路由器存活时间，秒为单位。默认值为1800。取值范围：0-9000。








缺省 :

缺省情况下，路由器存活时间为1800秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。主机收到路由器通告报文后，根据ra-lifetime字段可以设置该路由器在其默认路由器列表中的时间。






范例 :

配置接口gei-0/1/0/1的路由器存活时间为1000秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd ra-lifetime 1000恢复接口gei-0/1/0/1的路由器存活时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-lifetime





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-lifetime 


ipv6 nd ra-lifetime 




命令功能 :

该命令用于配置接口发送路由器通告中的“路由器存活时间”字段的值。no命令恢复路由器存活时间为默认值。主机收到路由器通告报文后，根据ra-lifetime字段可以设置该路由器在其默认路由器列表中的时间。





命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd ra-lifetime 
  ＜ra-lifetime 
＞

no ipv6 nd ra-lifetime 








命令参数解释 :



参数|描述
---|---
＜ra-lifetime＞|路由器存活时间，秒为单位。默认值为1800。取值范围：0-9000。








缺省 :

缺省情况下，路由器存活时间为1800秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。主机收到路由器通告报文后，根据ra-lifetime字段可以设置该路由器在其默认路由器列表中的时间。






范例 :

配置接口gei-0/1/0/1的路由器存活时间为1000秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd ra-lifetime 1000恢复接口gei-0/1/0/1的路由器存活时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-lifetime





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-linkmtu 


ipv6 nd ra-linkmtu 




命令功能 :

该命令用于配置路由器通告中的MTU选项字段的值。no命令恢复路由器通告中的MTU选项字段的默认值。 






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :



ipv6 nd ra-linkmtu 
  ＜ra-linkmtu 
＞

no ipv6 nd ra-linkmtu 








命令参数解释 :



参数|描述
---|---
＜ra-linkmtu＞|路由器通告中的MTU选项字段的值，以字节为单位。取值范围：0-1500。默认值：1500。








缺省 :

缺省情况下路由器通告中的mtu字段的值为1500。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在有可变MTU的链路上应当按路由器通告中的MTU选项字段的值发送流量。当配置不为0时，设备发送的路由器通告报文中携带MTU选项字段，当配置为0时，设备发送的路由器通告报文中不能携带MTU选项字段。





范例 :

在gei-0/1/0/1接口上配置LinkMtu为1300：ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-linkmtu 1300在gei-0/1/0/1接口上恢复LinkMtu为默认值：ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd ra-linkmtu





相关命令 :

无 




## ipv6 nd ra-linkmtu 


ipv6 nd ra-linkmtu 




命令功能 :

该命令用于配置路由器通告中的MTU选项字段的值。no命令恢复路由器通告中的MTU选项字段的默认值。 






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :



ipv6 nd ra-linkmtu 
  ＜ra-linkmtu 
＞

no ipv6 nd ra-linkmtu 








命令参数解释 :



参数|描述
---|---
＜ra-linkmtu＞|路由器通告中的MTU选项字段的值，以字节为单位。取值范围：0-1500。默认值：1500。








缺省 :

缺省情况下路由器通告中的mtu字段的值为1500。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在有可变MTU的链路上应当按路由器通告中的MTU选项字段的值发送流量。当配置不为0时，设备发送的路由器通告报文中携带MTU选项字段，当配置为0时，设备发送的路由器通告报文中不能携带MTU选项字段。





范例 :

在gei-0/1/0/1接口上配置LinkMtu为1300：ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-linkmtu 1300在gei-0/1/0/1接口上恢复LinkMtu为默认值：ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd ra-linkmtu





相关命令 :

无 




## ipv6 nd ra-linkmtu 


ipv6 nd ra-linkmtu 




命令功能 :

该命令用于配置路由器通告中的MTU选项字段的值。no命令恢复路由器通告中的MTU选项字段的默认值。 






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,smartgroup接口模式:15,smartgroup子接口模式:15,以太子接口模式:15,以太接口模式:15,千兆以太接口模式:15 






命令格式 :



ipv6 nd ra-linkmtu 
  ＜ra-linkmtu 
＞

no ipv6 nd ra-linkmtu 








命令参数解释 :



参数|描述
---|---
＜ra-linkmtu＞|路由器通告中的MTU选项字段的值，以字节为单位。取值范围：0-1500。默认值：1500。








缺省 :

缺省情况下路由器通告中的mtu字段的值为1500。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在有可变MTU的链路上应当按路由器通告中的MTU选项字段的值发送流量。当配置不为0时，设备发送的路由器通告报文中携带MTU选项字段，当配置为0时，设备发送的路由器通告报文中不能携带MTU选项字段。





范例 :

在gei-0/1/0/1接口上配置LinkMtu为1300：ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-linkmtu 1300在gei-0/1/0/1接口上恢复LinkMtu为默认值：ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd ra-linkmtu





相关命令 :

无 




## ipv6 nd ra-linkmtu 


ipv6 nd ra-linkmtu 




命令功能 :

该命令用于配置路由器通告中的MTU选项字段的值。no命令恢复路由器通告中的MTU选项字段的默认值。 






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 nd ra-linkmtu 
  ＜ra-linkmtu 
＞

no ipv6 nd ra-linkmtu 








命令参数解释 :



参数|描述
---|---
＜ra-linkmtu＞|路由器通告中的MTU选项字段的值，以字节为单位。取值范围：0-1500。默认值：1500。








缺省 :

缺省情况下路由器通告中的mtu字段的值为1500。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在有可变MTU的链路上应当按路由器通告中的MTU选项字段的值发送流量。当配置不为0时，设备发送的路由器通告报文中携带MTU选项字段，当配置为0时，设备发送的路由器通告报文中不能携带MTU选项字段。





范例 :

在gei-0/1/0/1接口上配置LinkMtu为1300：ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-linkmtu 1300在gei-0/1/0/1接口上恢复LinkMtu为默认值：ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd ra-linkmtu





相关命令 :

无 




## ipv6 nd ra-route-information 


ipv6 nd ra-route-information 




命令功能 :

该命令用于配置IPv6协议的RA报文中的路由信息选项。配置时必须指定每个路由信息选项的前缀和前缀长度，也可以选择指定路由寿命和优先级。no命令删除该路由信息选项配置。





命令模式 :

 IPv6隧道接口模式,bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,supervlan接口模式,ulei子接口模式,ulei接口模式,vbui接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,vbui接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,IPv6隧道接口模式:15,qx接口模式:15,virtual_template接口模式:15,supervlan接口模式:15,multilink接口模式:15,pos接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd ra-route-information 
 prefix 
 ＜ipv6-address 
＞ [route-lifetime 
 ＜0-4294967295 
＞ [preferences 
 ＜0-3 
＞]]
no ipv6 nd ra-route-information 
 prefix 
 ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|包含在路由器通告中网络前缀地址及前缀长度。其中前缀长度的取值范围是0-128。只有当前缀地址为不确定地址时，其前缀长度才能为0。
＜0-4294967295＞|配置路由信息选项中的路由寿命，单位是秒。配置范围：0-4294967295。默认值：4294967295。
＜0-3＞|配置路由信息选项中的路由优先级。配置范围：0-3。默认值：0。








缺省 :

缺省情况下，接口上配置的RA报文中的路由信息选项的路由生存时间是4294967295秒，路由优先级为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。本命令可以修改已有的路由信息选项的参数，也可以在路由器通告中增加新的前缀选项。每个接口最多支持配置1个路由信息选项。如果不指定参数配置路由信息选项，则参数使用默认值。配置的路由信息选项中的前缀地址不能为LinkLocal地址、组播地址和回环地址。如果前缀地址是不确定地址，其前缀长度必须为0。相同接口下不能配置前缀地址相同，但是前缀长度不同的路由信息选项。不同接口不能配置相同前缀地址的路由信息选项。






范例 :

在gei-0/1/0/1接口上配置RA报文中的路由信息选项，前缀地址为1::1/64，路由生存时间10000秒，路由优先级为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-route-information prefix 1::1/64 route-lifetime 1000 preferences 1在gei-0/1/0/1接口上删除RA报文中的路由信息选项配置：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-route-information prefix 1::1/64





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd ra-route-information 


ipv6 nd ra-route-information 




命令功能 :

该命令用于配置IPv6协议的RA报文中的路由信息选项。配置时必须指定每个路由信息选项的前缀和前缀长度，也可以选择指定路由寿命和优先级。no命令删除该路由信息选项配置。





命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

smartgroup接口模式:15,smartgroup子接口模式:15,以太接口模式:15,以太子接口模式:15,千兆以太接口模式:15,10G以太接口模式:15 






命令格式 :


ipv6 nd ra-route-information 
 prefix 
 ＜ipv6-address 
＞ [route-lifetime 
 ＜0-4294967295 
＞ [preferences 
 ＜0-3 
＞]]
no ipv6 nd ra-route-information 
 prefix 
 ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|包含在路由器通告中网络前缀地址及前缀长度。其中前缀长度的取值范围是0-128。只有当前缀地址为不确定地址时，其前缀长度才能为0。
＜0-4294967295＞|配置路由信息选项中的路由寿命，单位是秒。配置范围：0-4294967295。默认值：4294967295。
＜0-3＞|配置路由信息选项中的路由优先级。配置范围：0-3。默认值：0。








缺省 :

缺省情况下，接口上配置的RA报文中的路由信息选项的路由生存时间是4294967295秒，路由优先级为0。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。本命令可以修改已有的路由信息选项的参数，也可以在路由器通告中增加新的前缀选项。每个接口最多支持配置1个路由信息选项。如果不指定参数配置路由信息选项，则参数使用默认值。配置的路由信息选项中的前缀地址不能为LinkLocal地址、组播地址和回环地址。如果前缀地址是不确定地址，其前缀长度必须为0。相同接口下不能配置前缀地址相同，但是前缀长度不同的路由信息选项。不同接口不能配置相同前缀地址的路由信息选项。






范例 :

在gei-0/1/0/1接口上配置RA报文中的路由信息选项，前缀地址为1::1/64，路由生存时间10000秒，路由优先级为1：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd ra-route-information prefix 1::1/64 route-lifetime 1000 preferences 1在gei-0/1/0/1接口上删除RA报文中的路由信息选项配置：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd ra-route-information prefix 1::1/64





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd reachable-time 


ipv6 nd reachable-time 




命令功能 :

该命令用于配置ND邻居缓存可达时间。该时间的作用是远端邻居确认可达后多少时间内认为远端邻居是可达的。no命令可以恢复ND邻居缓存可达时间为默认值。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,qx子接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd reachable-time 
  ＜reachable-time 
＞

no ipv6 nd reachable-time 








命令参数解释 :



参数|描述
---|---
＜reachable-time＞|配置认为远端邻居的可达时间，以毫秒为单位。取值范围：0-3600000。默认值:30000。








缺省 :

缺省情况下ND邻居缓存可达时间为30000毫秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在确认邻居可达后的可达时间内，当路由器向该邻居发送报文时候，无需重新进行ND学习。配置的可达时间越短，消耗的网络带宽和处理时间越多，因此不建议将可达时间配置较短。






范例 :

在gei-0/1/0/1接口上配置远端邻居的可达时间为50000毫秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd reachable-time 50000在gei-0/1/0/1接口上恢复远端邻居的可达时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd reachable-time





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd reachable-time 


ipv6 nd reachable-time 




命令功能 :

该命令用于配置ND邻居缓存可达时间。该时间的作用是远端邻居确认可达后多少时间内认为远端邻居是可达的。no命令可以恢复ND邻居缓存可达时间为默认值。





命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd reachable-time 
  ＜reachable-time 
＞

no ipv6 nd reachable-time 








命令参数解释 :



参数|描述
---|---
＜reachable-time＞|配置认为远端邻居的可达时间，以毫秒为单位。取值范围：0-3600000。默认值:30000。








缺省 :

缺省情况下ND邻居缓存可达时间为30000毫秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在确认邻居可达后的可达时间内，当路由器向该邻居发送报文时候，无需重新进行ND学习。配置的可达时间越短，消耗的网络带宽和处理时间越多，因此不建议将可达时间配置较短。





范例 :

在gei-0/1/0/1接口上配置远端邻居的可达时间为50000毫秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd reachable-time 50000在gei-0/1/0/1接口上恢复远端邻居的可达时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd reachable-time





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd reachable-time 


ipv6 nd reachable-time 




命令功能 :

该命令用于配置ND邻居缓存可达时间。该时间的作用是远端邻居确认可达后多少时间内认为远端邻居是可达的。no命令可以恢复ND邻居缓存可达时间为默认值。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

千兆以太接口模式:15,以太接口模式:15,smartgroup子接口模式:15,smartgroup接口模式:15,以太子接口模式:15,10G以太接口模式:15 






命令格式 :


ipv6 nd reachable-time 
  ＜reachable-time 
＞

no ipv6 nd reachable-time 








命令参数解释 :



参数|描述
---|---
＜reachable-time＞|配置认为远端邻居的可达时间，以毫秒为单位。取值范围：0-3600000。默认值:30000。








缺省 :

缺省情况下ND邻居缓存可达时间为30000毫秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在确认邻居可达后的可达时间内，当路由器向该邻居发送报文时候，无需重新进行ND学习。配置的可达时间越短，消耗的网络带宽和处理时间越多，因此不建议将可达时间配置较短。






范例 :

在gei-0/1/0/1接口上配置远端邻居的可达时间为50000毫秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd reachable-time 50000在gei-0/1/0/1接口上恢复远端邻居的可达时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd reachable-time





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd reachable-time 


ipv6 nd reachable-time 




命令功能 :

该命令用于配置ND邻居缓存可达时间。该时间的作用是远端邻居确认可达后多少时间内认为远端邻居是可达的。no命令可以恢复ND邻居缓存可达时间为默认值。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd reachable-time 
  ＜reachable-time 
＞

no ipv6 nd reachable-time 








命令参数解释 :



参数|描述
---|---
＜reachable-time＞|配置认为远端邻居的可达时间，以毫秒为单位。取值范围：0-3600000。默认值:30000。








缺省 :

缺省情况下ND邻居缓存可达时间为30000毫秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在确认邻居可达后的可达时间内，当路由器向该邻居发送报文时候，无需重新进行ND学习。配置的可达时间越短，消耗的网络带宽和处理时间越多，因此不建议将可达时间配置较短。






范例 :

在gei-0/1/0/1接口上配置远端邻居的可达时间为50000毫秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd reachable-time 50000在gei-0/1/0/1接口上恢复远端邻居的可达时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd reachable-time





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd redirect 


ipv6 nd redirect 




命令功能 :

该命令用于开启平台ND重定向功能。重定向报文由路由器发送，以便针对具体的目的地，主机重定向到较好的第一跳路由器，或通知主机某个目的地事实上是邻居。no命令关闭ND重定向功能。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,dsl接口模式:15,serial接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,ulei接口模式:15,bvi接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd redirect 
 

no ipv6 nd redirect 








命令参数解释 :


					无
				 






缺省 :

缺省情况下该开关是关闭的，设备不发送nd重定向报文。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在默认情况下，平台不支持ND重定向功能。当微码上行发现IPv6报文出接口和入接口相同，而且平台有下发同意重定向标记，则将报文上送平台，平台转发该报文，并向源主机发送重定向报文。






范例 :

在gei-0/1/0/1接口上使能ND重定向功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd redirect在gei-0/1/0/1接口上关闭ND重定向功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd redirect






相关命令 :

无 




## ipv6 nd redirect 


ipv6 nd redirect 




命令功能 :

该命令用于开启平台ND重定向功能。重定向报文由路由器发送，以便针对具体的目的地，主机重定向到较好的第一跳路由器，或通知主机某个目的地事实上是邻居。no命令关闭ND重定向功能。






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd redirect 
 

no ipv6 nd redirect 








命令参数解释 :


					无
				 






缺省 :

缺省情况下该开关是关闭的，设备不发送nd重定向报文。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在默认情况下，平台不支持ND重定向功能。当微码上行发现IPv6报文出接口和入接口相同，而且平台有下发同意重定向标记，则将报文上送平台，平台转发该报文，并向源主机发送重定向报文。






范例 :

在gei-0/1/0/1接口上使能ND重定向功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd redirect在gei-0/1/0/1接口上关闭ND重定向功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd redirect






相关命令 :

无 




## ipv6 nd redirect 


ipv6 nd redirect 




命令功能 :

该命令用于开启平台ND重定向功能。重定向报文由路由器发送，以便针对具体的目的地，主机重定向到较好的第一跳路由器，或通知主机某个目的地事实上是邻居。no命令关闭ND重定向功能。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

smartgroup子接口模式:15,以太接口模式:15,千兆以太接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15 






命令格式 :


ipv6 nd redirect 
 

no ipv6 nd redirect 








命令参数解释 :


					无
				 






缺省 :

缺省情况下该开关是关闭的，设备不发送nd重定向报文。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在默认情况下，平台不支持ND重定向功能。当微码上行发现IPv6报文出接口和入接口相同，而且平台有下发同意重定向标记，则将报文上送平台，平台转发该报文，并向源主机发送重定向报文。






范例 :

在gei-0/1/0/1接口上使能ND重定向功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd redirect在gei-0/1/0/1接口上关闭ND重定向功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd redirect






相关命令 :

无 




## ipv6 nd redirect 


ipv6 nd redirect 




命令功能 :

该命令用于开启平台ND重定向功能。重定向报文由路由器发送，以便针对具体的目的地，主机重定向到较好的第一跳路由器，或通知主机某个目的地事实上是邻居。no命令关闭ND重定向功能。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd redirect 
 

no ipv6 nd redirect 








命令参数解释 :


					无
				 






缺省 :

缺省情况下该开关是关闭的，设备不发送nd重定向报文。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在默认情况下，平台不支持ND重定向功能。当微码上行发现IPv6报文出接口和入接口相同，而且平台有下发同意重定向标记，则将报文上送平台，平台转发该报文，并向源主机发送重定向报文。






范例 :

在gei-0/1/0/1接口上使能ND重定向功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd redirect在gei-0/1/0/1接口上关闭ND重定向功能：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd redirect






相关命令 :

无 




## ipv6 nd retransmit-time 


ipv6 nd retransmit-time 




命令功能 :

该命令用于配置在路由器通告中的“重传计时器”字段的值，用于控制路由器地址重复地址检测报文和邻居请求报文发送的时间间隔。no命令恢复路由器通告中的“重传计时器”字段的默认值。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,qx子接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd retransmit-time 
  ＜retransmit-time 
＞

no ipv6 nd retransmit-time 








命令参数解释 :



参数|描述
---|---
＜retransmit-time＞|配置在路由器通告中的“重传计时器”字段的值，单位为毫秒。取值范围：1000-4294967295。默认值：1000。








缺省 :

缺省情况下路由器地址重复检测报文和邻居请求报文的发送间隔为1000毫秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。“重传计时器”字段的值是用于控制路由器地址重复地址检测报文和邻居请求报文发送的时间间隔，完成DAD、邻居不可达性探测和地址解析功能。





范例 :

在gei-0/1/0/1接口上配置重传计时器时间为10000毫秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd retransmit-time 10000在gei-0/1/0/1接口上恢复重传计时器时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd retransmit-time





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd retransmit-time 


ipv6 nd retransmit-time 




命令功能 :

该命令用于配置在路由器通告中的“重传计时器”字段的值，用于控制路由器地址重复地址检测报文和邻居请求报文发送的时间间隔。no命令恢复路由器通告中的“重传计时器”字段的默认值。






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd retransmit-time 
  ＜retransmit-time 
＞

no ipv6 nd retransmit-time 








命令参数解释 :



参数|描述
---|---
＜retransmit-time＞|配置在路由器通告中的“重传计时器”字段的值，单位为毫秒。取值范围：1000-4294967295。默认值：1000。








缺省 :

缺省情况下路由器地址重复检测报文和邻居请求报文的发送间隔为1000毫秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。“重传计时器”字段的值是用于控制路由器地址重复地址检测报文和邻居请求报文发送的时间间隔，完成DAD、邻居不可达性探测和地址解析功能。





范例 :

在gei-0/1/0/1接口上配置重传计时器时间为10000毫秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd retransmit-time 10000在gei-0/1/0/1接口上恢复重传计时器时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd retransmit-time





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd retransmit-time 


ipv6 nd retransmit-time 




命令功能 :

该命令用于配置在路由器通告中的“重传计时器”字段的值，用于控制路由器地址重复地址检测报文和邻居请求报文发送的时间间隔。no命令恢复路由器通告中的“重传计时器”字段的默认值。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,smartgroup接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,以太接口模式:15,10G以太接口模式:15 






命令格式 :


ipv6 nd retransmit-time 
  ＜retransmit-time 
＞

no ipv6 nd retransmit-time 








命令参数解释 :



参数|描述
---|---
＜retransmit-time＞|配置在路由器通告中的“重传计时器”字段的值，单位为毫秒。取值范围：1000-4294967295。默认值：1000。








缺省 :

缺省情况下路由器地址重复检测报文和邻居请求报文的发送间隔为1000毫秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。“重传计时器”字段的值是用于控制路由器地址重复地址检测报文和邻居请求报文发送的时间间隔，完成DAD、邻居不可达性探测和地址解析功能。





范例 :

在gei-0/1/0/1接口上配置重传计时器时间为10000毫秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd retransmit-time 10000在gei-0/1/0/1接口上恢复重传计时器时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd retransmit-time





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd retransmit-time 


ipv6 nd retransmit-time 




命令功能 :

该命令用于配置在路由器通告中的“重传计时器”字段的值，用于控制路由器地址重复地址检测报文和邻居请求报文发送的时间间隔。no命令恢复路由器通告中的“重传计时器”字段的默认值。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd retransmit-time 
  ＜retransmit-time 
＞

no ipv6 nd retransmit-time 








命令参数解释 :



参数|描述
---|---
＜retransmit-time＞|配置在路由器通告中的“重传计时器”字段的值，单位为毫秒。取值范围：1000-4294967295。默认值：1000。








缺省 :

缺省情况下路由器地址重复检测报文和邻居请求报文的发送间隔为1000毫秒。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。“重传计时器”字段的值是用于控制路由器地址重复地址检测报文和邻居请求报文发送的时间间隔，完成DAD、邻居不可达性探测和地址解析功能。





范例 :

在gei-0/1/0/1接口上配置重传计时器时间为10000毫秒：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 nd retransmit-time 10000在gei-0/1/0/1接口上恢复重传计时器时间为默认值：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd retransmit-time





相关命令 :

debug ipv6 nd6no ipv6 nd suppress-ra



## ipv6 nd staled-time 


ipv6 nd staled-time 




命令功能 :

该命令用于配置接口上的ND缓存条目中的老化时间。no命令恢复ND缓存条目中的老化时间为默认值。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

dsl接口模式:15,qx子接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd staled-time 
  ＜staled-time 
＞

no ipv6 nd staled-time 








命令参数解释 :



参数|描述
---|---
＜staled-time＞|ND缓存条目老化时间，以分为单位。取值范围：1-14400。无效值0，表示取协议默认值1440。








缺省 :

缺省时无配置，如果全局上也没有该配置，则协议默认缺省值为1440分钟即24小时。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下无配置，如果全局上也没有该配置，则协议默认值为1440分钟即24小时。控制接口上ND缓存条目在平台的老化时间，接口上该配置优先级高于全局配置。






范例 :

在gei-0/1/0/1接口上配置ND缓存条目老化时间为1000分钟：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd staled-time 1000在gei-0/1/0/1接口上删除ND缓存条目老化时间配置：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd staled-time 





相关命令 :

ipv6 nd stale-switchnd stale-switchnd staled-time



## ipv6 nd staled-time 


ipv6 nd staled-time 




命令功能 :

该命令用于配置接口上的ND缓存条目中的老化时间。no命令恢复ND缓存条目中的老化时间为默认值。






命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd staled-time 
  ＜staled-time 
＞

no ipv6 nd staled-time 








命令参数解释 :



参数|描述
---|---
＜staled-time＞|ND缓存条目老化时间，以分为单位。取值范围：1-14400。无效值0，表示取协议默认值1440。








缺省 :

缺省时无配置，如果全局上也没有该配置，则协议默认缺省值为1440分钟即24小时。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下无配置，如果全局上也没有该配置，则协议默认值为1440分钟即24小时。控制接口上ND缓存条目在平台的老化时间，接口上该配置优先级高于全局配置。






范例 :

在gei-0/1/0/1接口上配置ND缓存条目老化时间为1000分钟：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd staled-time 1000在gei-0/1/0/1接口上删除ND缓存条目老化时间配置：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd staled-time 





相关命令 :

ipv6 nd stale-switchnd stale-switchnd staled-time



## ipv6 nd staled-time 


ipv6 nd staled-time 




命令功能 :

该命令用于配置接口上的ND缓存条目中的老化时间。no命令恢复ND缓存条目中的老化时间为默认值。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

smartgroup子接口模式:15,以太接口模式:15,以太子接口模式:15,smartgroup接口模式:15,10G以太接口模式:15,千兆以太接口模式:15 






命令格式 :


ipv6 nd staled-time 
  ＜staled-time 
＞

no ipv6 nd staled-time 








命令参数解释 :



参数|描述
---|---
＜staled-time＞|ND缓存条目老化时间，以分为单位。取值范围：1-14400。无效值0，表示取协议默认值1440。








缺省 :

缺省时无配置，如果全局上也没有该配置，则协议默认缺省值为1440分钟即24小时。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下无配置，如果全局上也没有该配置，则协议默认值为1440分钟即24小时。控制接口上ND缓存条目在平台的老化时间，接口上该配置优先级高于全局配置。






范例 :

在gei-0/1/0/1接口上配置ND缓存条目老化时间为1000分钟：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd staled-time 1000在gei-0/1/0/1接口上删除ND缓存条目老化时间配置：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd staled-time 





相关命令 :

ipv6 nd stale-switchnd stale-switchnd staled-time



## ipv6 nd staled-time 


ipv6 nd staled-time 




命令功能 :

该命令用于配置接口上的ND缓存条目中的老化时间。no命令恢复ND缓存条目中的老化时间为默认值。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd staled-time 
  ＜staled-time 
＞

no ipv6 nd staled-time 








命令参数解释 :



参数|描述
---|---
＜staled-time＞|ND缓存条目老化时间，以分为单位。取值范围：1-14400。无效值0，表示取协议默认值1440。








缺省 :

缺省时无配置，如果全局上也没有该配置，则协议默认缺省值为1440分钟即24小时。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下无配置，如果全局上也没有该配置，则协议默认值为1440分钟即24小时。控制接口上ND缓存条目在平台的老化时间，接口上该配置优先级高于全局配置。






范例 :

在gei-0/1/0/1接口上配置ND缓存条目老化时间为1000分钟：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd staled-time 1000在gei-0/1/0/1接口上删除ND缓存条目老化时间配置：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd staled-time 





相关命令 :

ipv6 nd stale-switchnd stale-switchnd staled-time



## ipv6 nd stale-switch 


ipv6 nd stale-switch 




命令功能 :

该命令用于在接口上打开ND缓存条目老化时间到达后进行邻居不可达探测开关。no命令关闭该开关。该命令仅针对该接口上的ND缓存条目生效。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

qx子接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd stale-switch 
 

no ipv6 nd stale-switch 








命令参数解释 :


					无
				 






缺省 :

情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。配置该命令后，该开关打开，当ND条目老化后会进行三次探测，如收不到对端的回应信息，则删除条目，默认情况下该开关是关闭的。接口下配置该命令，无论全局配置是否打开该开关，该接口上的ND缓存条目老化后都需要进行邻居不可达探测。






范例 :

在gei-0/1/0/1接口上打开ND缓存条目老化后的邻居不可达探测开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd stale-switch在gei-0/1/0/1接口上关闭ND缓存条目老化后的邻居不可达探测开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd stale-switch





相关命令 :

ipv6 nd staled-timend staled-timeipv6 nd stale-switch



## ipv6 nd stale-switch 


ipv6 nd stale-switch 




命令功能 :

该命令用于在接口上打开ND缓存条目老化时间到达后进行邻居不可达探测开关。no命令关闭该开关。该命令仅针对该接口上的ND缓存条目生效。






命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd stale-switch 
 

no ipv6 nd stale-switch 








命令参数解释 :


					无
				 






缺省 :

情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。配置该命令后，该开关打开，当ND条目老化后会进行三次探测，如收不到对端的回应信息，则删除条目，默认情况下该开关是关闭的。接口下配置该命令，无论全局配置是否打开该开关，该接口上的ND缓存条目老化后都需要进行邻居不可达探测。






范例 :

在gei-0/1/0/1接口上打开ND缓存条目老化后的邻居不可达探测开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd stale-switch在gei-0/1/0/1接口上关闭ND缓存条目老化后的邻居不可达探测开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd stale-switch





相关命令 :

ipv6 nd staled-timend staled-timeipv6 nd stale-switch



## ipv6 nd stale-switch 


ipv6 nd stale-switch 




命令功能 :

该命令用于在接口上打开ND缓存条目老化时间到达后进行邻居不可达探测开关。no命令关闭该开关。该命令仅针对该接口上的ND缓存条目生效。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太接口模式:15,10G以太接口模式:15,千兆以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,smartgroup子接口模式:15 






命令格式 :


ipv6 nd stale-switch 
 

no ipv6 nd stale-switch 








命令参数解释 :


					无
				 






缺省 :

情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。配置该命令后，该开关打开，当ND条目老化后会进行三次探测，如收不到对端的回应信息，则删除条目，默认情况下该开关是关闭的。接口下配置该命令，无论全局配置是否打开该开关，该接口上的ND缓存条目老化后都需要进行邻居不可达探测。






范例 :

在gei-0/1/0/1接口上打开ND缓存条目老化后的邻居不可达探测开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd stale-switch在gei-0/1/0/1接口上关闭ND缓存条目老化后的邻居不可达探测开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd stale-switch





相关命令 :

ipv6 nd staled-timend staled-timeipv6 nd stale-switch



## ipv6 nd stale-switch 


ipv6 nd stale-switch 




命令功能 :

该命令用于在接口上打开ND缓存条目老化时间到达后进行邻居不可达探测开关。no命令关闭该开关。该命令仅针对该接口上的ND缓存条目生效。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd stale-switch 
 

no ipv6 nd stale-switch 








命令参数解释 :


					无
				 






缺省 :

情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。配置该命令后，该开关打开，当ND条目老化后会进行三次探测，如收不到对端的回应信息，则删除条目，默认情况下该开关是关闭的。接口下配置该命令，无论全局配置是否打开该开关，该接口上的ND缓存条目老化后都需要进行邻居不可达探测。






范例 :

在gei-0/1/0/1接口上打开ND缓存条目老化后的邻居不可达探测开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd stale-switch在gei-0/1/0/1接口上关闭ND缓存条目老化后的邻居不可达探测开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# no ipv6 nd stale-switch





相关命令 :

ipv6 nd staled-timend staled-timeipv6 nd stale-switch



## ipv6 nd suppress-ra 


ipv6 nd suppress-ra 




命令功能 :

该命令用于控制抑制发送路由器通告报文开关。正向命令为打开抑制发送路由器通告报文开关。no命令关闭抑制发送路由器通告报文开关。






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,gre隧道接口模式,multilink接口模式,posgroup接口模式,pos接口模式,qx子接口模式,qx接口模式,serial接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

qx子接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,pos接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15,qx接口模式:15,virtual_template接口模式:15,multilink接口模式:15,dsl子接口模式:15 






命令格式 :


ipv6 nd suppress-ra 
  [disable 
]

no ipv6 nd suppress-ra 








命令参数解释 :



参数|描述
---|---
disable|去使能ipv6 nd suppress-ra，等价于no ipv6 nd suppress-ra








缺省 :

缺省情况下，抑制发送路由器通告报文的开关是打开的，路由器不能发送RA报文。因此，对收到的路由器请求，也不作回应。建议用户在确认本接口需要处理路由器请求以及需要发送路由器通告的情况下，关闭抑制发送路由器通告报文开关。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，抑制发送路由器通告报文的开关是打开的，路由器不能发送RA报文。因此，对收到的路由器请求，也不作回应。建议用户在确认本接口需要处理路由器请求以及需要发送路由器通告的情况下，关闭抑制发送路由器通告报文开关。抑制发送路由器通告报文开关与使能主机协议栈开关ipv6 nd host是互斥的。主机协议栈功能打开时，不能关闭抑制发送路由器通告报文开关；只有当主机协议栈关闭时，才能关闭抑制发送路由器通告报文开关。





范例 :

在gei-0/1/0/1接口上关闭抑制路由器发送路由器通告报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd suppress-ra在接口上打开抑制路由器发送路由器通告报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd suppress-ra





相关命令 :

debug ipv6 nd6 




## ipv6 nd suppress-ra 


ipv6 nd suppress-ra 




命令功能 :

该命令用于控制抑制发送路由器通告报文开关。正向命令为打开抑制发送路由器通告报文开关。no命令关闭抑制发送路由器通告报文开关。






命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


ipv6 nd suppress-ra 
  [disable 
]

no ipv6 nd suppress-ra 








命令参数解释 :



参数|描述
---|---
disable|去使能ipv6 nd suppress-ra，等价于no ipv6 nd suppress-ra








缺省 :

缺省情况下，抑制发送路由器通告报文的开关是打开的，路由器不能发送RA报文。因此，对收到的路由器请求，也不作回应。建议用户在确认本接口需要处理路由器请求以及需要发送路由器通告的情况下，关闭抑制发送路由器通告报文开关。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，抑制发送路由器通告报文的开关是打开的，路由器不能发送RA报文。因此，对收到的路由器请求，也不作回应。建议用户在确认本接口需要处理路由器请求以及需要发送路由器通告的情况下，关闭抑制发送路由器通告报文开关。抑制发送路由器通告报文开关与使能主机协议栈开关ipv6 nd host是互斥的。主机协议栈功能打开时，不能关闭抑制发送路由器通告报文开关；只有当主机协议栈关闭时，才能关闭抑制发送路由器通告报文开关。





范例 :

在gei-0/1/0/1接口上关闭抑制路由器发送路由器通告报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd suppress-ra在接口上打开抑制路由器发送路由器通告报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd suppress-ra





相关命令 :

debug ipv6 nd6 




## ipv6 nd suppress-ra 


ipv6 nd suppress-ra 




命令功能 :

该命令用于控制抑制发送路由器通告报文开关。正向命令为打开抑制发送路由器通告报文开关。no命令关闭抑制发送路由器通告报文开关。






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

千兆以太接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,以太接口模式:15,smartgroup子接口模式:15 






命令格式 :


ipv6 nd suppress-ra 
  [disable 
]

no ipv6 nd suppress-ra 








命令参数解释 :



参数|描述
---|---
disable|去使能ipv6 nd suppress-ra，等价于no ipv6 nd suppress-ra








缺省 :

缺省情况下，抑制发送路由器通告报文的开关是打开的，路由器不能发送RA报文。因此，对收到的路由器请求，也不作回应。建议用户在确认本接口需要处理路由器请求以及需要发送路由器通告的情况下，关闭抑制发送路由器通告报文开关。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，抑制发送路由器通告报文的开关是打开的，路由器不能发送RA报文。因此，对收到的路由器请求，也不作回应。建议用户在确认本接口需要处理路由器请求以及需要发送路由器通告的情况下，关闭抑制发送路由器通告报文开关。抑制发送路由器通告报文开关与使能主机协议栈开关ipv6 nd host是互斥的。主机协议栈功能打开时，不能关闭抑制发送路由器通告报文开关；只有当主机协议栈关闭时，才能关闭抑制发送路由器通告报文开关。





范例 :

在gei-0/1/0/1接口上关闭抑制路由器发送路由器通告报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd suppress-ra在接口上打开抑制路由器发送路由器通告报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd suppress-ra





相关命令 :

debug ipv6 nd6 




## ipv6 nd suppress-ra 


ipv6 nd suppress-ra 




命令功能 :

该命令用于控制抑制发送路由器通告报文开关。正向命令为打开抑制发送路由器通告报文开关。no命令关闭抑制发送路由器通告报文开关。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 nd suppress-ra 
  [disable 
]

no ipv6 nd suppress-ra 








命令参数解释 :



参数|描述
---|---
disable|去使能ipv6 nd suppress-ra，等价于no ipv6 nd suppress-ra








缺省 :

缺省情况下，抑制发送路由器通告报文的开关是打开的，路由器不能发送RA报文。因此，对收到的路由器请求，也不作回应。建议用户在确认本接口需要处理路由器请求以及需要发送路由器通告的情况下，关闭抑制发送路由器通告报文开关。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。默认情况下，抑制发送路由器通告报文的开关是打开的，路由器不能发送RA报文。因此，对收到的路由器请求，也不作回应。建议用户在确认本接口需要处理路由器请求以及需要发送路由器通告的情况下，关闭抑制发送路由器通告报文开关。抑制发送路由器通告报文开关与使能主机协议栈开关ipv6 nd host是互斥的。主机协议栈功能打开时，不能关闭抑制发送路由器通告报文开关；只有当主机协议栈关闭时，才能关闭抑制发送路由器通告报文开关。





范例 :

在gei-0/1/0/1接口上关闭抑制路由器发送路由器通告报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 nd suppress-ra在接口上打开抑制路由器发送路由器通告报文开关：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# ipv6 nd suppress-ra





相关命令 :

debug ipv6 nd6 




## nd nud-switch 


nd nud-switch 




命令功能 :

该命令用于ND配置模式下配置ND邻居缓存条目邻居不可达探测开关，从而控制所有动态ND邻居缓存条目是否开启邻居不可达探测功能。该功能开启时， ND缓存条目处于stale状态时，如果有报文需要从控制面发送，则首先要进行ND不可达探测，判断邻居是否存在，探测成功，对应ND条目会切换成reachable状态，然后将报文发送。该功能默认是打开的。






命令模式 :

 ND模式  






命令默认权限级别 :

15 






命令格式 :


nd nud-switch 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|使能nd nud-switch，表示开关打开，可以进行邻居可达性探测
disable|去使能nd nud-switch，表示开关关闭，不可以进行邻居可达性探测








缺省 :

该功能开关默认$#67240102:0/关闭;1/打开#$ 






使用说明 :

该命令工作于ND模式下，需要先进入ND配置模式，才能使用。默认情况下无配置，该开关是打开的，平台会进行邻居不可达性探测。在ND配置模式下关闭全局ND邻居不可达性探测开关，所有的 ND缓存条目不可以进行邻居不可达探测，默认情况下该开关是打开的。全局配置关闭邻居不可达性探测开关时，各个接口配置邻居不可达性探测开关是否关闭，所有接口都按照关闭邻居不可达性探测处理。






范例 :

在ND配置模式下，配置ND条目邻居可达性探测开关：ZXROSNG(config)#ndZXROSNG(config-nd)#nd nud-switch enable





相关命令 :

ipv6 nd nud-switch 




## nd staled-time 


nd staled-time 




命令功能 :

该命令用于在ND全局配置模式上配置ND缓存条目中的老化时间。no命令恢复ND缓存条目中的老化时间为默认值。该命令对所用动态ND缓存条目生效。






命令模式 :

 ND模式  






命令默认权限级别 :

15 






命令格式 :


nd staled-time 
  ＜staled-time 
＞

no nd staled-time 








命令参数解释 :



参数|描述
---|---
＜staled-time＞|ND缓存条目老化时间，以分为单位。取值范围：1-14400。无效值0，表示取协议默认值1440。








缺省 :

缺省情况下无配置，如果接口上也没有相应配置，则协议默认缺省值为1440分钟即24小时。 






使用说明 :

该命令工作于ND模式下，需要先进入ND配置模式，才能使用默认情况下无配置，如果接口上也没有该配置，则协议默认值为1440分钟即24小时。控制所有ND缓存条目在平台的老化时间，接口上该配置优先级高于全局配置。





范例 :

在ND配置模式下，配置ND缓存条目老化时间为1000分钟：ZXROSNG(config)#ndZXROSNG(config-nd)#nd staled-time 1000在ND配置模式下，删除ND缓存条目老化时间配置：ZXROSNG(config)#ndZXROSNG(config-nd)#no nd staled-time 





相关命令 :

nd stale-switch 




## nd stale-switch 


nd stale-switch 




命令功能 :

该命令用于ND配置模式下打开ND缓存条目老化时间到达后进行邻居不可达探测开关。该命令对所有动态ND缓存条目生效。






命令模式 :

 ND模式  






命令默认权限级别 :

15 






命令格式 :


nd stale-switch 
  [disable 
]






命令参数解释 :



参数|描述
---|---
disable|去使能nd stale-switch，表示开关关闭








缺省 :

该功能开关默认$#67240103:0/关闭;1/打开#$ 






使用说明 :

该命令工作于ND模式下，需要先进入ND配置模式，才能使用。默认情况下，该功能是关闭的，ND缓存条目老化时间到后直接删除。配置该命令后，该开关打开，当ND条目老化后会进行三次探测，如收不到对端的回应信息，则删除条目。ND全局配置模式下配置该命令，无论各个接口上是否打开该开关，所有的ND缓存条目老化后都需要进行邻居不可达探测。






范例 :

在ND配置模式下，配置ND条目老化后的探测开关：ZXROSNG(config)#ndZXROSNG(config-nd)#nd stale-switch





相关命令 :

nd staled-timeipv6 nd staled-timeipv6 nd stale-switch



## nd6 add 


nd6 add 




命令功能 :

该命令用于接口配置模式下配置一条静态ND邻居缓存条目。 






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

dsl接口模式:15,qx子接口模式:15,ulei子接口模式:15,eth_dslgroup接口模式:15,bvi子接口模式:15,ulei接口模式:15,bvi接口模式:15,qx接口模式:15,dsl子接口模式:15 






命令格式 :



nd6 add 
  ＜ipv6-address 
＞ ＜mac-address 
＞ [＜external-vlan-id 
＞ [＜internal-vlan-id 
＞]]







命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|邻居缓存表中的目的地址
＜mac-address＞|邻居缓存表中对应目的地址的MAC地址。48位的值，采用XXXX.XXXX.XXXX的形式，16位为1组，中间以“.”隔开
＜external-vlan-id＞|配置外层VLAN ID 。取值范围是1-4094。
＜internal-vlan-id＞|配置内层VLAN ID 。取值范围是1-4094。








缺省 :

无 






使用说明 :

该命令工作于接口模式下，配置该命令前需要进入相应接口模式。nd6 add命令在邻居缓存表中创建一个静态条目，在邻居缓存表中，标记为“static”，表示永远有效，其状态为“reachable”。静态条目的优先级高于动态条目，即如果已存在同样地址的动态邻居缓存条目，本命令将直接覆盖动态条目。在子接口上配置该命令时，该子接口的VLAN封装类型如果是dot1q range类型，则需要配置外层VLAN ID；如果VLAN封装类型是QINQ range类型，则需要配置外层和内层VLAN ID；其他VLAN类型不需要配置VLAN ID。父接口不需要配置VLAN ID。





范例 :

在gei-0/1/0/1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if- gei-0/1/0/1)#nd6 add 4ffe::2 0001.0002.0003 在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1.1封装的VLAN是dot1q range 1-10，指定外层VLAN为5配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 5在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003， gei-0/1/0/1.1封装的VLAN是QINQ range 1-10 1-10，指定外层VLAN为，内层VLAN为8配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 gei-0/1/0/1.1 5 8





相关命令 :

nd6 delete <ipv6-address> 




## nd6 add 


nd6 add 




命令功能 :

该命令用于接口配置模式下配置一条静态ND邻居缓存条目。 






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15 






命令格式 :



nd6 add 
  ＜ipv6-address 
＞ ＜mac-address 
＞ [＜external-vlan-id 
＞ [＜internal-vlan-id 
＞]]







命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|邻居缓存表中的目的地址
＜mac-address＞|邻居缓存表中对应目的地址的MAC地址。48位的值，采用XXXX.XXXX.XXXX的形式，16位为1组，中间以“.”隔开
＜external-vlan-id＞|配置外层VLAN ID 。取值范围是1-4094。
＜internal-vlan-id＞|配置内层VLAN ID 。取值范围是1-4094。








缺省 :

无 






使用说明 :

该命令工作于接口模式下，配置该命令前需要进入相应接口模式。nd6 add命令在邻居缓存表中创建一个静态条目，在邻居缓存表中，标记为“static”，表示永远有效，其状态为“reachable”。静态条目的优先级高于动态条目，即如果已存在同样地址的动态邻居缓存条目，本命令将直接覆盖动态条目。在子接口上配置该命令时，该子接口的VLAN封装类型如果是dot1q range类型，则需要配置外层VLAN ID；如果VLAN封装类型是QINQ range类型，则需要配置外层和内层VLAN ID；其他VLAN类型不需要配置VLAN ID。父接口不需要配置VLAN ID。





范例 :

在gei-0/1/0/1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if- gei-0/1/0/1)#nd6 add 4ffe::2 0001.0002.0003 在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1.1封装的VLAN是dot1q range 1-10，指定外层VLAN为5配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 5在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003， gei-0/1/0/1.1封装的VLAN是QINQ range 1-10 1-10，指定外层VLAN为，内层VLAN为8配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 gei-0/1/0/1.1 5 8





相关命令 :

nd6 delete <ipv6-address> 




## nd6 add 


nd6 add 




命令功能 :

该命令用于接口配置模式下配置一条静态ND邻居缓存条目。 






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



nd6 add 
  ＜ipv6-address 
＞ ＜mac-address 
＞ [＜external-vlan-id 
＞ [＜internal-vlan-id 
＞]]







命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|邻居缓存表中的目的地址
＜mac-address＞|邻居缓存表中对应目的地址的MAC地址。48位的值，采用XXXX.XXXX.XXXX的形式，16位为1组，中间以“.”隔开
＜external-vlan-id＞|配置外层VLAN ID 。取值范围是1-4094。
＜internal-vlan-id＞|配置内层VLAN ID 。取值范围是1-4094。








缺省 :

无 






使用说明 :

该命令工作于接口模式下，配置该命令前需要进入相应接口模式。nd6 add命令在邻居缓存表中创建一个静态条目，在邻居缓存表中，标记为“static”，表示永远有效，其状态为“reachable”。静态条目的优先级高于动态条目，即如果已存在同样地址的动态邻居缓存条目，本命令将直接覆盖动态条目。在子接口上配置该命令时，该子接口的VLAN封装类型如果是dot1q range类型，则需要配置外层VLAN ID；如果VLAN封装类型是QINQ range类型，则需要配置外层和内层VLAN ID；其他VLAN类型不需要配置VLAN ID。父接口不需要配置VLAN ID。





范例 :

在gei-0/1/0/1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if- gei-0/1/0/1)#nd6 add 4ffe::2 0001.0002.0003 在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1.1封装的VLAN是dot1q range 1-10，指定外层VLAN为5配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 5在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003， gei-0/1/0/1.1封装的VLAN是QINQ range 1-10 1-10，指定外层VLAN为，内层VLAN为8配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 gei-0/1/0/1.1 5 8





相关命令 :

nd6 delete <ipv6-address> 




## nd6 add 


nd6 add 




命令功能 :

该命令用于在 supervlan接口配置模式下配置一条静态ND邻居缓存条目。 






命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :



nd6 add 
  ＜ipv6-address 
＞ ＜mac-address 
＞ ＜interface-name 
＞ [＜external-vlan-id 
＞ [＜internal-vlan-id 
＞]]







命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|邻居缓存表中的目的地址
＜mac-address＞|邻居缓存表中对应目的地址的MAC地址。48位的值，采用XXXX.XXXX.XXXX的形式，16位为1组，中间以“.”隔开。
＜interface-name＞|指定成员接口，仅对于supervlan接口配置模式可见且必须配置，其他接口配置模式下该参数不可见。
＜external-vlan-id＞|配置外层VLAN ID。取值范围是1-4094。
＜internal-vlan-id＞|配置内层VLAN ID。取值范围是1-4094。








缺省 :

无 






使用说明 :

该命令工作于supervlan接口模式下。nd6 add命令在邻居缓存表中创建一个静态条目，在邻居缓存表中，标记为“static”，表示永远有效，其状态为“reachable”。静态条目的优先级高于动态条目，即如果已存在同样地址的动态邻居缓存条目，本命令将直接覆盖动态条目。supervlan接口模式上配置静态ND邻居缓存条目需要指定成员口，且不支持同样地址的静态条目跨越多个成员接口。对于成员口是range子接口的情况，还需要指定VLAN配置。若其VLAN封装类型是dot1q range类型，则需要配置外层VLAN ID；若其VLAN封装类型是QINQ range类型，则需要配置外层和内层VLAN ID。成员口是非range接口，则不需要指定VLAN配置静态ND邻居缓存条目。





范例 :

在supervlan1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1为绑定在supervlan1接口下的成员接口：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#nd6 add 4ffe::2 0001.0002.0003 gei-0/1/0/1在supervlan1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1.1为绑定在supervlan1接口下的成员接口，且gei-0/1/0/1.1封装的VLAN是dot1q range 1-10，指定外层VLAN为5配置：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#nd6 add 4ffe::2 0001.0002.0003 gei-0/1/0/1.1 5在supervlan1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1.1为绑定在supervlan1接口下的成员接口，且gei-0/1/0/1.1封装的VLAN是QINQ range 1-10 1-10，指定外层VLAN为，内层VLAN为8配置：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#nd6 add 4ffe::2 0001.0002.0003 gei-0/1/0/1.1 5 8





相关命令 :

nd6 delete <ipv6-address> 




## nd6 delete 


nd6 delete 




命令功能 :

该命令用于接口模式删除ND邻居缓存表中一个静态缓存条目。 






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



nd6 delete 
  ＜ipv6-address 
＞







命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|邻居缓存表中的目的IPv6地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。 






范例 :

在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1.1封装的VLAN是dot1q range 1-10，指定外层VLAN为5配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 5删除gei-0/1/0/1.1接口上的IPv6地址为4ffe::2的静态ND邻居缓存条目ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 delete 4ffe::2 





相关命令 :

nd6 add <ipv6-address> <hardware-address> 




## nd6 delete 


nd6 delete 




命令功能 :

该命令用于接口模式删除ND邻居缓存表中一个静态缓存条目。 






命令模式 :

 bvi子接口模式,bvi接口模式,dsl子接口模式,dsl接口模式,eth_dslgroup接口模式,qx子接口模式,qx接口模式,supervlan接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

qx子接口模式:15,ulei子接口模式:15,eth_dslgroup接口模式:15,dsl接口模式:15,bvi子接口模式:15,ulei接口模式:15,bvi接口模式:15,qx接口模式:15,supervlan接口模式:15,dsl子接口模式:15 






命令格式 :



nd6 delete 
  ＜ipv6-address 
＞







命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|邻居缓存表中的目的IPv6地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。 






范例 :

在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1.1封装的VLAN是dot1q range 1-10，指定外层VLAN为5配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 5删除gei-0/1/0/1.1接口上的IPv6地址为4ffe::2的静态ND邻居缓存条目ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 delete 4ffe::2 





相关命令 :

nd6 add <ipv6-address> <hardware-address> 




## nd6 delete 


nd6 delete 




命令功能 :

该命令用于接口模式删除ND邻居缓存表中一个静态缓存条目。 






命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,smartgroup接口模式:15,10G以太接口模式:15,以太子接口模式:15 






命令格式 :



nd6 delete 
  ＜ipv6-address 
＞







命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|邻居缓存表中的目的IPv6地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。 






范例 :

在gei-0/1/0/1.1接口添加静态ND邻居缓存条目，其目的地址为4ffe::2，MAC地址为0001.0002.0003，gei-0/1/0/1.1封装的VLAN是dot1q range 1-10，指定外层VLAN为5配置：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 add 4ffe::2 0001.0002.0003 5删除gei-0/1/0/1.1接口上的IPv6地址为4ffe::2的静态ND邻居缓存条目ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if- gei-0/1/0/1.1)#nd6 delete 4ffe::2 





相关命令 :

nd6 add <ipv6-address> <hardware-address> 




## nd 


nd 




命令功能 :

本命令用于从全局配置模式进入ND配置模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



nd 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

从全局配置模式进入ND配置模式。 






范例 :

从全局配置模式进入ND配置模式。ZXROSNG(config)#ndZXROSNG(config-nd)#





相关命令 :

无 




## show debug nd6 


show debug nd6 




命令功能 :

该命令用于查看ND的调试信息开关是否已经打开。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug nd6 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于查看ND调试功能是否开启。 






范例 :

不指定接口打开ND协议报文的调试功能后，查看ND的debug开关：ZXROSNG#debug ipv6 nd6IPv6 Neighbor Discovery debugging is onZXROSNG#show debug nd6ND6:IPv6 Neighbor Discovery events debugging is on指定接口打开ND协议报文的调试功能后，查看ND的debug开关：ZXROSNG#debug ipv6 nd6 interface gei-0/1/0/4IPv6 Neighbor Discovery debugging is onZXROSNG#show debug nd6ND6:  IPv6 Neighbor Discovery events debugging of the interface gei-0/1/0/4 is on打开ND的trace信息调试开关ZXROSNG#debug nd6 traceND6 trace debugging is on ZXROSNG#show debug nd6ND6:  ND6 trace debugging is onZXROSNG#debug nd6 trace interface gei-0/1/0/4ND6 trace debugging is on ZXROSNG#show debug nd6ND6:  ND6 trace debugging of the interface gei-0/1/0/4 is onZXROSNG#debug nd6 trace interface gei-0/1/0/4 limit-count 10000ND6 trace debugging is on ZXROSNG#show debug nd6ND6:  ND6 trace debugging of the interface fei-0/1/0/1 is on,remaining number is 10000打开ND协议报文的调试功能和ND trace调试功能，并查看ZXROSNG#debug ipv6 nd6 interface gei-0/1/0/4IPv6 Neighbor Discovery debugging is onZXROSNG#debug nd6 trace interface gei-0/1/0/4 limit-count 10000ND6 trace debugging is on ZXROSNG#show debug nd6ND6:IPv6 Neighbor Discovery events debugging of the interface gei-0/1/0/4 is on  ND6 trace debugging of the interface fei-0/1/0/1 is on,remaining number is 10000





相关命令 :

debug ipv6 nd6debug nd6 trace



## show nd6 cache 


show nd6 cache 




命令功能 :

该命令用于显示ND邻居缓存表的信息。显示的内容包括下一跳IPv6地址，MAC地址，ND邻居缓存条目状态，当前状态剩余时间和出接口名。






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :


show nd6 cache 
  [＜interface-name 
＞] 






命令参数解释 :



参数|描述
---|---
＜interface-name＞|邻居缓存表中的条目对应的出接口。路由器上支持：以太接口和以太子接口、sg接口和sg子接口、supervlan口、ulei口和ulei子接口、eth_dslgroup接口、qx接口和qx子接口、bvi接口和bvi子接口、dsl接口、管理口、gpon_vport接口和gpon_vport子接口、svi接口和svi子接口,dcn接口,gtunnel_group接口和te_gtunnel接口。








缺省 :

无 






使用说明 :

该命令工作于除用户模式外的其他所有模式。不指定接口名使用本命令，将显示邻居缓存中所有的条目，包含动态学习的和静态添加的；如果指定接口名执行本命令，则回显邻居缓存条目中对应出接口为指定接口的条目。





范例 :

显示ND邻居缓存条目：ZXROSNG#show nd cacheTotal Cache Number Is:3Only Current Valid Items Are Shown Below:Address                           Link-Address       Age       Status        Interface4ffe::1                           ce03.2220.0001    static     Reachable    gei-0/1/0/5fe80::c800:7bff:fe74:8            ca00.7b74.0008   23h41m27s   Stale        gei-0/1/0/51::1                              ca00.7b74.0008   23h41m17s   Stale        gei-0/1/0/5





相关命令 :

nd6 add <ipv6-address> <hardware-address>clear nd-cache <interface>



# OSPFv3配置命令 
## area 


area 




命令功能 :

创建一个OSPFv3区域。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


area 
  {＜area-id-ip 
＞|＜area-id 
＞}
no area 
  {＜area-id-ip 
＞|＜area-id 
＞}
				






命令参数解释 :



参数|描述
---|---
＜area-id-ip＞|区域号，IP地址格式，范围：0.0.0.0-255.255.255.255
＜area-id＞|区域号，数值格式，范围：0-4294967295








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5





相关命令 :

无 




## authentication 


authentication 




命令功能 :

配置OSPFv3的区域下所有接口认证密钥。使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



authentication 
  {ipsec 
 spi 
 ＜_spi-id 
＞ {md5 
 {＜_md5_key 
＞|encrypted 
 ＜_md5_key_encrypted 
＞}|sha1 
 {＜_sha1_key 
＞|encrypted 
 ＜_sha1_key_encrypted 
＞}|keychain 
 ＜Keychain name 
＞} [rollover-interval 
 ＜rollover-interva 
＞]|keychain 
 ＜Keychain_name 
＞}

no authentication 








命令参数解释 :



参数|描述
---|---
ipsec|IPSEC认证
＜_spi-id＞|安全策略索引(security policy index)值，合法的十进制值范围：256-32767。
＜_md5_key＞|MD5认证密钥，为十六进制字符串，用户必须输入32个字符。
＜_md5_key_encrypted＞|加密的MD5认证密钥，为十六进制字符串，用户必须输入64个字符。
＜_sha1_key＞|SHA1认证密钥，为十六进制字符串,用户必须输入40个字符。
＜_sha1_key_encrypted＞|加密的SHA1认证密钥,为十六进制字符串，用户必须输入64个字符。
＜Keychain name＞|IPSEC认证的keychain名称, 长度范围：1-31字符。
＜rollover-interva＞|密钥生效延迟时间,此参数主要是为了当用户修改key值时，由于修改所有路由器上的key需要花费比较长的时间，因此需要进行一个平滑过渡的时期。此参数就是平滑过渡的间隔时间，单位为分钟。
keychain|keychain认证
＜Keychain_name＞|keychain认证的名称，长度范围：1-31字符。








缺省 :

无认证 






使用说明 :

区域加密和区域认证不能同时配置 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 1 ZXROSNG(config-ospfv3-1-area-1)#authentication ipsec spi 256 md5 12345678901234567890123456789012





相关命令 :

无 




## auto-cost 


auto-cost 




命令功能 :

配置该实例下接口的参考带宽。 






命令模式 :

 IPv6-OSPF模式  






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
＜ref-bw＞|接口的参考带宽，范围1-4000000，单位：Mbps。








缺省 :

100 






使用说明 :

该配置对loopback接口不生效 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXR10 (config-ospfv3-1)#auto-cost reference-bandwidth 200ZXR10 (config-ospfv3-1)#





相关命令 :

无 




## bfd 


bfd 




命令功能 :

配置所有接口的双向转发检测（bfd）功能。使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



bfd 
 enable 


no bfd 








命令参数解释 :



参数|描述
---|---
enable|使能bfd功能








缺省 :

无 






使用说明 :

实例下配置bfd，可以使能实例中所有有效的接口。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#bfd enable





相关命令 :

area bfd 




## bfd 


bfd 




命令功能 :

配置区域下所有接口的双向转发检测（BFD, bidirection forwarding detect）属性。使用no命令恢复缺省值 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



bfd 
  {enable 
|disable 
}

no bfd 








命令参数解释 :



参数|描述
---|---
enable|使能区域BFD功能
disable|去使能区域BFD功能








缺省 :

无 






使用说明 :

当配置bfd enable时，表示使能区域BFD功能；当配置bfd disable时，表示去使能区域BFD功能；当无配置或者no bfd时，区域是否使能BFD功能取决于OSPFv3实例下的BFD配置。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 1 ZXROSNG(config-ospfv3-1-area-1)#bfd disable





相关命令 :

无 




## bfd 


bfd 




命令功能 :

配置接口的双向转发检测（bfd, bidirection forwarding detect）属性。使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



bfd 
  {enable 
|disable 
}

no bfd 








命令参数解释 :



参数|描述
---|---
enable|双向转发检测有效
disable|双向转发检测无效








缺省 :

双向转发检测有效。 






使用说明 :

无 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#bfd disable





相关命令 :

无 




## bgp link-state 


bgp link-state 




命令功能 :

使用BGP来分发链路状态信息。 






命令模式 :

 IPv6-OSPF模式  






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
instance-id|用于标识BGP-LS信息所属的routing universe,范围：0-65535，默认值：0








缺省 :

如果没有配置该命令，缺省是不使能该功能的。如果配置了bgp link-state，instance-id的缺省值是0






使用说明 :

使用场景汇总OSPF协议收集的拓扑信息上送给上层控制器时，使用该命令。






范例 :

使能BGP-LS功能，所属routing universe为1.ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#bgp link-state instance-id 1






相关命令 :

无 




## capability vrf-lite 


capability vrf-lite 




命令功能 :

用来使路由忽略OSPF VRF环路抑制，使用no命令表示不忽略。 






命令模式 :

 IPv6-OSPF模式  






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

1.该命令只有VRF实例可以配置。2.该命令默认不配置，表示使能OSPF VRF环路抑制功能。配置该命令表示环路抑制功能被忽略。





范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)# capability vrf-lite





相关命令 :

无 




## clear ipv6 ospf process 


clear ipv6 ospf process 




命令功能 :

将OSPFv3进程重启动。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear ipv6 ospf process 
  ＜process-id 
＞







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPFv3进程号，范围：1-65535








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#endZXROSNG#clear ipv6 ospf process 1





相关命令 :

ipv6 router ospfrouter-id



## cost link-damping 


cost link-damping 




命令功能 :

接口下第一个邻居FULL后开始调整接口的花费来抑制该链路。 






命令模式 :

 IPv6-OSPF接口模式  






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
increase|当damping状态生效的情况下调整该接口的花费，在原有花费的基础上新增一个花费值。
＜increase-value＞|花费调整值，范围是100-10000。
maximum|当damping状态生效的情况下直接调整该接口的花费到最大值65535。
＜damping-time＞|Damping状态持续的时间。范围是1-3600000，单位是毫秒








缺省 :

如果没有配置该命令，缺省是不使能该功能的。 






使用说明 :

无 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXR10 (config-ospfv3-1)#area 1ZXR10 (config-ospfv3-1-area-1)#interface gei-0/1/0/1ZXR10 (config-ospfv3-1-area-1-if- gei-0/1/0/1)# cost link-damping increase 3001 damping-time 200000





相关命令 :

无 




## cost 


cost 




命令功能 :

设置接口的代价。使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



cost 
  ＜cost-value 
＞

no cost 








命令参数解释 :



参数|描述
---|---
＜cost-value＞|接口费用值，范围：1-65535；接口的缺省代价为1








缺省 :

没有配置。 






使用说明 :

该命令用于修改接口的代价。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#cost 100





相关命令 :

无 




## dead-interval 


dead-interval 




命令功能 :

指定接口上邻居的死亡时间。使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



dead-interval 
  ＜dead-interval 
＞

no dead-interval 








命令参数解释 :



参数|描述
---|---
＜dead-interval＞|接口上邻居的死亡时间，单位：秒，范围：1-65535，point-to-point与broadcast类型接口的默认值为40秒，non-broadcast与point-to-multipoint类型接口的默认值为120秒，dead-interval 的默认时间会随着修改hello-interval时间而改变（为hello-interval的4倍）








缺省 :

point-to-point与broadcast类型接口的默认值为40秒，non-broadcast与point-to-multipoint类型接口的默认值为120秒。 






使用说明 :

该命令用于修改接口邻居的死亡时间。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)dead-interval 100





相关命令 :

无 




## debug ipv6 ospfv3 all 


debug ipv6 ospfv3 all 




命令功能 :

打开所有OSPFv3调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 all 
  ＜process-id 
＞
no debug ipv6 ospfv3 all 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围:1-65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 all 1 






相关命令 :

无 




## debug ipv6 ospfv3 events abr 


debug ipv6 ospfv3 events abr 




命令功能 :

打开所有abr调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 events abr 
  ＜process-id 
＞
no debug ipv6 ospfv3 events abr 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 events abr 1 






相关命令 :

无 




## debug ipv6 ospfv3 events asbr 


debug ipv6 ospfv3 events asbr 




命令功能 :

打开所有asbr调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 events asbr 
  ＜process-id 
＞
no debug ipv6 ospfv3 events asbr 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 events asbr 1 






相关命令 :

无 




## debug ipv6 ospfv3 events os 


debug ipv6 ospfv3 events os 




命令功能 :

打开所有os调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 events os 
  ＜process-id 
＞
no debug ipv6 ospfv3 events os 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospf events os 1 






相关命令 :

无 




## debug ipv6 ospfv3 events router 


debug ipv6 ospfv3 events router 




命令功能 :

打开所有router调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 events router 
  ＜process-id 
＞
no debug ipv6 ospfv3 events router 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 events router 1 






相关命令 :

无 




## debug ipv6 ospfv3 events vlink 


debug ipv6 ospfv3 events vlink 




命令功能 :

打开所有vlink调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 events vlink 
  ＜process-id 
＞
no debug ipv6 ospfv3 events vlink 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 events vlink 1 






相关命令 :

无 




## debug ipv6 ospfv3 events 


debug ipv6 ospfv3 events 




命令功能 :

打开所有调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 events 
  ＜process-id 
＞
no debug ipv6 ospfv3 events 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

无 






使用说明 :

无 






范例 :

无 






相关命令 :

无 




## debug ipv6 ospfv3 ifsm event 


debug ipv6 ospfv3 ifsm event 




命令功能 :

打开ifsm(接口状态机)事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 ifsm event 
  ＜process-id 
＞
no debug ipv6 ospfv3 ifsm event 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 ifsm event 1 






相关命令 :

无 




## debug ipv6 ospfv3 ifsm status 


debug ipv6 ospfv3 ifsm status 




命令功能 :

打开ifsm(接口状态机)状态调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 ifsm status 
  ＜process-id 
＞
no debug ipv6 ospfv3 ifsm status 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 ifsm status 1 






相关命令 :

无 




## debug ipv6 ospfv3 ifsm timer 


debug ipv6 ospfv3 ifsm timer 




命令功能 :

打开ifsm(接口状态机) timer调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 ifsm timer 
  ＜process-id 
＞
no debug ipv6 ospfv3 ifsm timer 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 ifsm timer 1 






相关命令 :

无 




## debug ipv6 ospfv3 ifsm 


debug ipv6 ospfv3 ifsm 




命令功能 :

打开ifsm调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 ifsm 
  ＜process-id 
＞
no debug ipv6 ospfv3 ifsm 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

无 






范例 :

无 






相关命令 :

无 




## debug ipv6 ospfv3 level abnormal 


debug ipv6 ospfv3 level abnormal 




命令功能 :

打开abnormal调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 ospfv3 level abnormal 
 

no debug ipv6 ospfv3 level abnormal 








命令参数解释 :


					无
				 






缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 level abnormal 






相关命令 :

无 




## debug ipv6 ospfv3 level detail 


debug ipv6 ospfv3 level detail 




命令功能 :

打开detail调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 ospfv3 level detail 
 

no debug ipv6 ospfv3 level detail 








命令参数解释 :


					无
				 






缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 level detail 






相关命令 :

无 




## debug ipv6 ospfv3 level flow 


debug ipv6 ospfv3 level flow 




命令功能 :

打开flow调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 ospfv3 level flow 
 

no debug ipv6 ospfv3 level flow 








命令参数解释 :


					无
				 






缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 level flow 






相关命令 :

无 




## debug ipv6 ospfv3 lsa fld 


debug ipv6 ospfv3 lsa fld 




命令功能 :

打开lsa洪泛调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 lsa fld 
  ＜process-id 
＞
no debug ipv6 ospfv3 lsa fld 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 lsa fld 1 






相关命令 :

无 




## debug ipv6 ospfv3 lsa gen 


debug ipv6 ospfv3 lsa gen 




命令功能 :

打开LSAs生成调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 lsa gen 
  ＜process-id 
＞
no debug ipv6 ospfv3 lsa gen 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 lsa gen 1 






相关命令 :

无 




## debug ipv6 ospfv3 lsa install 


debug ipv6 ospfv3 lsa install 




命令功能 :

打开lsa安装调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 lsa install 
  ＜process-id 
＞
no debug ipv6 ospfv3 lsa install 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 lsa install 1 






相关命令 :

无 




## debug ipv6 ospfv3 lsa maxage 


debug ipv6 ospfv3 lsa maxage 




命令功能 :

打开lsa 老化调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 lsa maxage 
  ＜process-id 
＞
no debug ipv6 ospfv3 lsa maxage 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 lsa maxage 1 






相关命令 :

无 




## debug ipv6 ospfv3 lsa refresh 


debug ipv6 ospfv3 lsa refresh 




命令功能 :

打开lsa更新调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 lsa refresh 
  ＜process-id 
＞
no debug ipv6 ospfv3 lsa refresh 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfvs lsa refresh 1 






相关命令 :

无 




## debug ipv6 ospfv3 lsa 


debug ipv6 ospfv3 lsa 




命令功能 :

打开lsa调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 lsa 
  ＜process-id 
＞
no debug ipv6 ospfv3 lsa 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 lsa fld 1 






相关命令 :

无 




## debug ipv6 ospfv3 mode debug 


debug ipv6 ospfv3 mode debug 




命令功能 :

打开debug模式的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 ospfv3 mode debug 
 

no debug ipv6 ospfv3 mode debug 








命令参数解释 :


					无
				 






缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 mode debug 






相关命令 :

无 




## debug ipv6 ospfv3 mode trace 


debug ipv6 ospfv3 mode trace 




命令功能 :

打开trace模式的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 ospfv3 mode trace 
 

no debug ipv6 ospfv3 mode trace 








命令参数解释 :


					无
				 






缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 mode trace 






相关命令 :

无 




## debug ipv6 ospfv3 nfsm event 


debug ipv6 ospfv3 nfsm event 




命令功能 :

打开nfsm(邻居状态机)事件调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 nfsm event 
  ＜process-id 
＞
no debug ipv6 ospfv3 nfsm event 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 nfsm event 1 






相关命令 :

无 




## debug ipv6 ospfv3 nfsm status 


debug ipv6 ospfv3 nfsm status 




命令功能 :

打开nfsm(邻居状态机)状态调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 nfsm status 
  ＜process-id 
＞
no debug ipv6 ospfv3 nfsm status 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 nfsm status 1 






相关命令 :

无 




## debug ipv6 ospfv3 nfsm timer 


debug ipv6 ospfv3 nfsm timer 




命令功能 :

打开nfsm(邻居状态机) timer调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 nfsm timer 
  ＜process-id 
＞
no debug ipv6 ospfv3 nfsm timer 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 nfsm timer 1 






相关命令 :

无 




## debug ipv6 ospfv3 nfsm 


debug ipv6 ospfv3 nfsm 




命令功能 :

打开nfsm调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 nfsm 
  ＜process-id 
＞
no debug ipv6 ospfv3 nfsm 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

无 






使用说明 :

无 






范例 :

无 






相关命令 :

无 




## debug ipv6 ospfv3 nsm intf 


debug ipv6 ospfv3 nsm intf 




命令功能 :

打开nsm(邻居状态机)接口调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 nsm intf 
  ＜process-id 
＞
no debug ipv6 ospfv3 nsm intf 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 nsm intf 1 






相关命令 :

无 




## debug ipv6 ospfv3 nsm rdst 


debug ipv6 ospfv3 nsm rdst 




命令功能 :

打开nsm重分发调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 nsm rdst 
  ＜process-id 
＞
no debug ipv6 ospfv3 nsm rdst 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 nsm rdst 1 






相关命令 :

无 




## debug ipv6 ospfv3 nsm 


debug ipv6 ospfv3 nsm 




命令功能 :

打开nsm(邻居状态机)调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 nsm 
  ＜process-id 
＞
no debug ipv6 ospfv3 nsm 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

无 






使用说明 :

无 






范例 :

无 






相关命令 :

无 




## debug ipv6 ospfv3 pkt ack 


debug ipv6 ospfv3 pkt ack 




命令功能 :

打开确认包调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 pkt ack 
  ＜process-id 
＞
no debug ipv6 ospfv3 pkt ack 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 pkt ack 1 






相关命令 :

无 




## debug ipv6 ospfv3 pkt dd 


debug ipv6 ospfv3 pkt dd 




命令功能 :

打开DD包调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 pkt dd 
  ＜process-id 
＞
no debug ipv6 ospfv3 pkt dd 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 pkt dd 1 






相关命令 :

无 




## debug ipv6 ospfv3 pkt detail 


debug ipv6 ospfv3 pkt detail 




命令功能 :

打开OSPFv3报文详细调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 pkt detail 
  ＜process-id 
＞
no debug ipv6 ospfv3 pkt detail 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 pkt detail 1 






相关命令 :

无 




## debug ipv6 ospfv3 pkt hello 


debug ipv6 ospfv3 pkt hello 




命令功能 :

打开hello包调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 pkt hello 
  ＜process-id 
＞
no debug ipv6 ospfv3 pkt hello 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 pkt hello 1 






相关命令 :

无 




## debug ipv6 ospfv3 pkt req 


debug ipv6 ospfv3 pkt req 




命令功能 :

打开请求报文调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 pkt req 
  ＜process-id 
＞
no debug ipv6 ospfv3 pkt req 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 pkt req 1 






相关命令 :

无 




## debug ipv6 ospfv3 pkt upd 


debug ipv6 ospfv3 pkt upd 




命令功能 :

打开更新包调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 pkt upd 
  ＜process-id 
＞
no debug ipv6 ospfv3 pkt upd 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 pkt upd 1 






相关命令 :

无 




## debug ipv6 ospfv3 pkt 


debug ipv6 ospfv3 pkt 




命令功能 :

打开报文调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 pkt 
  ＜process-id 
＞
no debug ipv6 ospfv3 pkt 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

无 






使用说明 :

无 






范例 :

无 






相关命令 :

无 




## debug ipv6 ospfv3 rt external 


debug ipv6 ospfv3 rt external 




命令功能 :

打开外部路由调试信息的开关。使用no命令关闭开关 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 rt external 
  ＜process-id 
＞
no debug ipv6 ospfv3 rt external 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 rt external 1 






相关命令 :

无 




## debug ipv6 ospfv3 rt install 


debug ipv6 ospfv3 rt install 




命令功能 :

打开rt安装调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 rt install 
  ＜process-id 
＞
no debug ipv6 ospfv3 rt install 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 rt install 1 






相关命令 :

无 




## debug ipv6 ospfv3 rt inter 


debug ipv6 ospfv3 rt inter 




命令功能 :

打开inter路由调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 rt inter 
  ＜process-id 
＞
no debug ipv6 ospfv3 rt inter 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 rt inter 1 






相关命令 :

无 




## debug ipv6 ospfv3 rt intra 


debug ipv6 ospfv3 rt intra 




命令功能 :

打开内部路由调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 rt intra 
  ＜process-id 
＞
no debug ipv6 ospfv3 rt intra 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 rt intra 1 






相关命令 :

无 




## debug ipv6 ospfv3 rt range 


debug ipv6 ospfv3 rt range 




命令功能 :

打开路由区域调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 rt range 
  ＜process-id 
＞
no debug ipv6 ospfv3 rt range 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 rt range 1 






相关命令 :

无 




## debug ipv6 ospfv3 rt summary 


debug ipv6 ospfv3 rt summary 




命令功能 :

打开路由概况调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 rt summary 
  ＜process-id 
＞
no debug ipv6 ospfv3 rt summary 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

关闭 






使用说明 :

本命令属于管理类命令，命令配置不保存，不在show running-config中显示。 






范例 :

ZXROSNG#debug ipv6 ospfv3 rt summary 1 






相关命令 :

无 




## debug ipv6 ospfv3 rt 


debug ipv6 ospfv3 rt 




命令功能 :

打开路由调试信息的开关。使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ipv6 ospfv3 rt 
  ＜process-id 
＞
no debug ipv6 ospfv3 rt 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1~65535








缺省 :

无 






使用说明 :

无 






范例 :

无 






相关命令 :

无 




## default-cost 


default-cost 




命令功能 :

配置stub区域的默认路由的花费值。使用no命令恢复默认值。 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



default-cost 
  ＜cost 
＞

no default-cost 








命令参数解释 :



参数|描述
---|---
＜cost＞|stub区域默认路由的花费值，范围是0-16777215








缺省 :

1 






使用说明 :

当区域不是stub区域的时候，无法配置该命令 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 3 ZXROSNG(config-ospfv3-1-area-3)#stubZXROSNG(config-ospfv3-1-area-3)#default-cost 5





相关命令 :

area stub 




## default-metric 


default-metric 




命令功能 :

设置OSPFv3协议引入外部路由的缺省度量值，使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF模式  






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
＜metric-value＞|设置系统的外部路由缺省度量值，范围：1-16777214








缺省 :

缺省值为20 






使用说明 :

该命令的设置值只有在没有设置外部路由的度量值时生效。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#default-metric 100





相关命令 :

redistribute 




## distance ospfv3 


distance ospfv3 




命令功能 :

配置OSPFv3路由的优先级。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


distance ospfv3 
  {[external 
 ＜distance 
＞],[inter-area 
 ＜distance 
＞],[intra-area 
 ＜distance 
＞]}
no distance ospfv3 
  [{[external 
],[inter-area 
],[intra-area 
]}]
				






命令参数解释 :



参数|描述
---|---
＜distance＞|外部路由的优先级，范围<1-255>
＜distance＞|外部路由的优先级，范围<1-255>
＜distance＞|外部路由的优先级，范围<1-255>






No参数|描述
---|---
external|清除外部路由的管理距离
inter-area|清除区域间路由的管理距离
intra-area|清除区域内路由的管理距离








缺省 :

110 






使用说明 :

无 






范例 :

ZXROSNG(config-ospfv3-1)#distance ospfv3 external 122ZXROSNG(config-ospfv3-1)#






相关命令 :

无 




## distribute-list 


distribute-list 




命令功能 :

distribute-list的in命令，用于过滤owner为OSPF的路由。使用no命令恢复缺省值。





命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


distribute-list 
  {access-list 
 ＜access-list-name 
＞|route-map 
 ＜route-map 
＞} in 


no distribute-list 
 in 








命令参数解释 :



参数|描述
---|---
＜access-list-name＞|名字型的acl，第一个字符不能是数字，且必须使用当前已经存在的acl
＜route-map＞|借用route-map模板的名字
in|In表示指定的模板用于路由的过滤








缺省 :

不配置该命令，即不进行路由的过滤和externalLSA的导入控制。 






使用说明 :

ACL：策略模板决策为permit时，返回permit，否则返回deny；策略模板不存在时，返回deny；route-map：策略模板决策为permit时，返回permit，否则返回deny；策略模板不存在时，返回permit





范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)# distribute-list access-list zxr10 in





相关命令 :

无 




## domain-id 


domain-id 




命令功能 :

配置OSPFv3实例下的Domain ID。使用no命令可以删除配置。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


domain-id 
 type 
 {0005 
|0105 
|0205 
} value 
 ＜value 
＞ [secondary 
]
no domain-id 
  {type 
 {0005 
|0105 
|0205 
} value 
 ＜value 
＞|all 
}
				






命令参数解释 :



参数|描述
---|---
0005|BGP中Domain ID扩展团体属性的编码类型为0x0005
0105|BGP中Domain ID扩展团体属性的编码类型为0x0105
0205|BGP中Domain ID扩展团体属性的编码类型为0x0205
＜value＞|十六进制字符串，长度为12
secondary|辅Domain ID标识






No参数|描述
---|---
all|删除所有的Domain ID








缺省 :

无 






使用说明 :

1.该命令只有VRF实例可以配置。2.不能配置value为全零的Domain ID.3.每个实例最多配置1个主Domain ID.4.每个实例最多配置15个辅Domain ID.





范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#domain-id type 0105 value aabbccdddddd secondary





相关命令 :

无 




## encryption 


encryption 




命令功能 :

配置OSPFv3的接口加密。使用no命令恢复缺省值 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



encryption 
 ipsec 
 spi 
 ＜_spi-id 
＞ esp 
 {{aes-cbc 
 128 
 {＜_aes_cbc_128_key 
＞|encrypted 
 ＜aes_cbc_128_key_encrypted 
＞}|3des 
 {＜_3des_key 
＞|encrypted 
 ＜3des_key_encrypted 
＞}|des 
 {＜_des_key 
＞|encrypted 
 ＜des_key_encrypted 
＞}|null 
} {md5 
 {＜_md5_key 
＞|encrypted 
 ＜md5_key_encrypted 
＞}|sha1 
 {＜_sha1_key 
＞|encrypted 
 ＜sha1_key_encrypted 
＞}}|keychain-encryption 
 ＜Keychain name 
＞ keychain 
 ＜Keychain name 
＞} [rollover-interval 
 ＜rollover-interva 
＞]

no encryption 








命令参数解释 :



参数|描述
---|---
ipsec|IPSEC认证。
＜_spi-id＞|安全策略索引(security policy index)值，合法的十进制值范围： 256-32767。
128|AES-CBC加密方式。
＜_aes_cbc_128_key＞|128位密钥，为十六进制字符串，用户必须输入32个字符。
＜aes_cbc_128_key_encrypted＞|加密的128位密钥，为十六进制字符串，用户必须输入64个字符。
3des|3DES加密方式。
＜_3des_key＞|192位密钥，为十六进制字符串，用户必须输入48个字符。
＜3des_key_encrypted＞|加密的192位密钥，为十六进制字符串，用户必须输入64个字符。
des|DES加密方式。
＜_des_key＞|64位密钥，为十六进制字符串，用户必须输入16个字符。
＜des_key_encrypted＞|加密的64位密钥,为十六进制字符串，用户必须输入64个字符。
null|没有加密。
＜_md5_key＞|MD5密钥，为十六进制字符串，用户必须输入40个字符。
＜md5_key_encrypted＞|加密的MD5密钥,为十六进制字符串，用户必须输入64个字符。
＜_sha1_key＞|SHA1密钥，为十六进制字符串，用户必须输入40个字符。
＜sha1_key_encrypted＞|加密的SHA1密钥,为十六进制字符串，用户必须输入64个字符。
keychain-encryption|使用keychain进行IPSEC加密
＜Keychain name＞|认证的keychain名称, 长度范围：1-31字符。
＜Keychain name＞|认证的keychain名称, 长度范围：1-31字符。
＜rollover-interva＞|密钥生效延迟时间,此参数主要是为了当用户修改key值时，由于修改所有路由器上的key需要花费比较长的时间，因此需要进行一个平滑过渡的时期。此参数就是平滑过渡的间隔时间，单位为分钟。








缺省 :

无 






使用说明 :

区域加密和区域认证不能同时配置。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 1 ZXROSNG(config-ospfv3-1-area-1)encryption ipsec spi 256 esp des 1234567890123456 md5 12345678901234567890123456789012





相关命令 :

无 




## fast-reroute policy-type 


fast-reroute policy-type 




命令功能 :

配置FRR备份路由策略。 






命令模式 :

 IPv6-OSPF模式  






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




## fast-reroute 


fast-reroute 




命令功能 :

使能OSPFv3的FRR功能。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute 
 per-prefix 


no fast-reroute 








命令参数解释 :



参数|描述
---|---
per-prefix|在每个前缀上实现FRR。








缺省 :

不开启FRR。 






使用说明 :

无 






范例 :

ZXROSNG(config-ospfv3-1)#fast-reroute per-prefix ZXROSNG(config-ospfv3-1)#






相关命令 :

show ipv6 ospf vertex backup 




## fast-reroute 


fast-reroute 




命令功能 :

去使能OSPFv3接口的FRR功能。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



fast-reroute 
 disable 


no fast-reroute 








命令参数解释 :



参数|描述
---|---
disable|去使能OSPFv3接口的FRR功能。








缺省 :

OSPFv3的接口的FRR功能和OSPFv3实例的FRR功能的使能状态是相同的。 






使用说明 :

该命令可以在OSPFv3实例使能了FRR功能的情况下，把某些接口不参与FRR。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#fast-reroute disable






相关命令 :

show ipv6 ospf vertex backup 




## grace-period 


grace-period 




命令功能 :

配置gr超时时间 






命令模式 :

 IPv6-OSPF模式  






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
＜period＞|gr超时时间，范围1-1800








缺省 :

120 






使用说明 :

配置了超时时间，gr如果在这个时间内没有完成，会退出gr。 






范例 :

ZXROSNG(config-ospfv3-1)#grace period 121 






相关命令 :

nsf 




## hello-interval 


hello-interval 




命令功能 :

指定接口上hello报文时间间隔。使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



hello-interval 
  ＜hello_interval 
＞

no hello-interval 








命令参数解释 :



参数|描述
---|---
＜hello_interval＞|接口上hello报文时间间隔，单位：秒，范围:1-65535，point-to-point与broadcast类型接口的默认值为10秒，non-broadcast与point-to-multipoint类型接口的默认值为30秒








缺省 :

point-to-point与broadcast类型接口的默认值为10秒，non-broadcast与point-to-multipoint类型接口的默认值为30秒。 






使用说明 :

该命令用于修改接口上发送hello报文的时间间隔。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#hello-interval 25





相关命令 :

无 




## instance 


instance 




命令功能 :

配置接口的实例号。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



instance 
  ＜instance-id 
＞

no instance 








命令参数解释 :



参数|描述
---|---
＜instance-id＞|接口的实例号，范围：0-255








缺省 :

0 






使用说明 :

建链的两端的接口实例号相同时才能建链成功 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if- gei-0/1/0/1)#instance 2





相关命令 :

无 




interface :

interface (IPv6-OSPF区域模式) 




命令功能 :

将接口启用到OSPFv3实例中。使用no命令将接口从OSPFv3实例中删除。 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


interface 
  ＜interface-name 
＞ [instance 
 ＜instance-id 
＞]
no interface 
  ＜interface-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|具体的接口名称
＜instance-id＞|接口实例号，范围：0-255，默认值为0








缺省 :

无 






使用说明 :

一个接口在一个OSPFv3进程中只能配置一次，但是可以配置到多个OSPFv3进程中，并且在多个OSPFv3进程中的实例号不能相同。只有实例号相同的接口才能建立邻接关系。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1





相关命令 :

router-id 




## ipv6 router ospf 


ipv6 router ospf 




命令功能 :

启动一个OSPFv3实例。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 router ospf 
  ＜process-id 
＞ [vrf 
 ＜vrf-name 
＞]
no ipv6 router ospf 
  ＜process-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPFv3进程号，范围：1-65535
＜vrf-name＞|VRF名称，长度1-32字节字符








缺省 :

无 






使用说明 :

只有通过router-id命令配置了路由器标识符后，该OSPFv3实例才能正常运行。 






范例 :

ZXROSNG(config)#ipv6 router ospf ?  <1-65535>  OSPF process IDZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#





相关命令 :

router-id 




## ipv6-mtu-ignore 


ipv6-mtu-ignore 




命令功能 :

当DD交换时，忽略mtu不匹配属性，即收到DD包时，不检查mtu。使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



ipv6-mtu-ignore 
 

no ipv6-mtu-ignore 








命令参数解释 :


					无
				 






缺省 :

DD报文交换时检查MTU。





使用说明 :

无 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#ipv6-mtu-ignore 





相关命令 :

无 




## ispf 


ispf 




命令功能 :

使能OSPFv3实例的增量SPF计算功能。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



ispf 
 

no ispf 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

1.使能ispf功能ZXROSNG(config-ospfv3-1)# ispf2.去使能ispf功能ZXROSNG(config-ospfv3-1)#no ispf





相关命令 :

无 




## linklsa-suppress 


linklsa-suppress 




命令功能 :

抑制接口产生8型link LSA。使用no命令恢复缺省值，即不抑制接口产生8型link LSA。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



linklsa-suppress 
 enable 


no linklsa-suppress 








命令参数解释 :



参数|描述
---|---
enable|指定接口下使能linklsa-suppress，即使接口不能产生8型link LSA








缺省 :

接口未使能linklsa-suppress，即不抑制接口产生8型link LSA 






使用说明 :

该命令用于控制点到点接口是否能产生8型link LSA。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#linklsa-suppress enable





相关命令 :

无 




## maximum-paths 


maximum-paths 




命令功能 :

设置OSPF协议负载均衡时支持的最大路由数目。使用no命令恢复缺省值。 






命令模式 :

 IPv6-OSPF模式  






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
＜path-number＞|设置OSPF协议负载均衡时支持的最大路由数目，性能参数定制范围：1~$#184680464#$








缺省 :

负载均衡最大路由数目缺省值是1。 






使用说明 :

1．    当路由器有了一个完整的链路状态数据库时，它就准备好要创建它的路由表以便能够转发数据流。缺省的开销度量是基于网络介质的带宽。要计算到达目的地的最低开销，路由表中最多保存64条等开销路由条目以进行负载均衡，可以通过maximum-paths进行配置。2．    路由器一般选择具有最小度量值的路径；如果同时出现了多条度量值最低且相同的路径，那么在这多条路径上将启用负载均衡，通过使用maximum-paths命令可以支持最多达64条相同度量值路径。3．    该命令立刻生效，分时处理，无需用户手工干预，但需要等待一定的时间。





范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#maximum-paths 4





相关命令 :

无 




## mpls ldp sync set-max-distance 


mpls ldp sync set-max-distance 




命令功能 :

使能LDP-IGP未同步时设置最大路由管理距离功能 






命令模式 :

 IPv6-OSPF模式  






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

OSPF实例下使能LDP-IGP同步功能后(即配置mpls ldp sync enable)，该命令才能生效 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#mpls ldp sync set-max-distance ZXROSNG(config-ospfv3-1)#






相关命令 :

mpls ldp sync  {enable|disable} 




## mpls ldp sync 


mpls ldp sync 




命令功能 :

实例下使能LDP IGP同步功能，使用no命令取消配置。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp sync 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|实例下使能LDP IGP同步功能。
disable|实例下去使能LDP IGP同步功能。








缺省 :

无 






使用说明 :

1.如果不配置，实例下LDP IGP同步功能是关闭的，相当于默认为去使能状态。2. 接口下LDP IGP的相关配置优先级最高，如果接口下没有配置继承区域的，如果区域下没有配置继承实例的。






范例 :

1.    实例使能LDP IGP同步功能。ZXROSNG(config#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#mpls ldp sync enable2.    实例下去使能动态lfa功能。ZXROSNG(config#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#mpls ldp sync disable






相关命令 :

区域和接口下配置LDP IGP同步功能ZXROSNG(config#ipv6 router ospf 1ZXR10 (config-ospfv3-1)#area 0ZXROSNG(config-ospfv3-1-area-0)#mpls ldp sync enable ZXROSNG(config-ospfv3-1-area-0)#mpls ldp sync disable ZXROSNG(config-ospfv3-1-area-0)#interface gei-0/1/0/6ZXROSNG(config-ospfv3-1-area-0-if-gei-0/1/0/6)#mpls ldp sync enable ZXROSNG(config-ospfv3-1-area-0-if-gei-0/1/0/6)#mpls ldp sync disable 




## mpls ldp sync 


mpls ldp sync 




命令功能 :

区域下使能LDP IGP同步功能，使用no命令取消配置。 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp sync 
  {enable 
|disable 
}

no mpls ldp sync 








命令参数解释 :



参数|描述
---|---
enable|enable表示区域下使能LDP IGP同步功能。
disable|disable表示区域下去使能LDP IGP同步功能。








缺省 :

无 






使用说明 :

接口下LDP IGP的相关配置优先级最高，如果接口下没有配置继承区域的，如果区域下没有配置继承实例的。 






范例 :

1.    区域下使能LDP IGP同步功能ZXROSNG(config#ipv6 router ospf 1ZXR10 (config-ospfv3-1)#area 0ZXROSNG(config-ospfv3-1-area-0)#mpls ldp sync enable 2.    区域下去使能LDP IGP同步功能ZXROSNG(config#ipv6 router ospf 1ZXR10 (config-ospfv3-1)#area 0ZXROSNG(config-ospfv3-1-area-0)#mpls ldp sync disable 






相关命令 :

实例和接口下配置LDP IGP同步功能ZXROSNG(config#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)# mpls ldp sync enableZXROSNG(config-ospfv3-1)# mpls ldp sync disableZXR10 (config-ospfv3-1)#area 0ZXROSNG(config-ospfv3-1-area-0)#interface gei-0/1/0/6ZXROSNG(config-ospfv3-1-area-0-if-gei-0/1/0/6)#mpls ldp sync enable ZXROSNG(config-ospfv3-1-area-0-if-gei-0/1/0/6)#mpls ldp sync disable 




## mpls ldp sync 


mpls ldp sync 




命令功能 :

接口下使能LDP IGP同步功能，使用no命令取消配置。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



mpls ldp sync 
  {enable 
|disable 
}

no mpls ldp sync 








命令参数解释 :



参数|描述
---|---
enable|enable表示接口下使能LDP IGP同步功能。
disable|disable表示接口下去使能LDP IGP同步功能。








缺省 :

无 






使用说明 :

接口下LDP IGP的相关配置优先级最高，如果接口下没有配置继承区域的，如果区域下没有配置继承实例的 






范例 :

1，    接口下使能LDP IGP同步功能ZXROSNG(config#ipv6 router ospf 1ZXR10 (config-ospfv3-1)#area 0ZXROSNG(config-ospfv3-1-area-0)#interface gei-0/1/0/6ZXROSNG(config-ospfv3-1-area-0-if-gei-0/1/0/6)#mpls ldp sync enable 2，接口下去使能LDP IGP同步功能ZXROSNG(config#ipv6 router ospf 1ZXR10 (config-ospfv3-1)#area 0ZXROSNG(config-ospfv3-1-area-0)#interface gei-0/1/0/6ZXROSNG(config-ospfv3-1-area-0-if-gei-0/1/0/6)#mpls ldp sync disable 






相关命令 :

实例和区域下配置LDP IGP同步功能ZXROSNG(config#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)# mpls ldp sync enableZXROSNG(config-ospfv3-1)# mpls ldp sync disableZXR10 (config-ospfv3-1)#area 0ZXROSNG(config-ospfv3-1-area-0)#mpls ldp sync enable ZXROSNG(config-ospfv3-1-area-0)#mpls ldp sync disable 




## neighbor 


neighbor 




命令功能 :

配置接口类型为non-broadcast或point-to-multipoint non-broadcast的网络中的相邻路由器。使用no命令删除该相邻路由器。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :


neighbor 
  ＜ipv6-address 
＞ [{[priority 
 ＜priority 
＞],[poll-interval 
 ＜poll-interval 
＞],[cost 
 ＜cost 
＞]}]
no neighbor 
  ＜ipv6-address 
＞ [{[priority 
],[poll-interval 
],[cost 
]}]
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|相邻路由器接口的link-local地址
＜priority＞|相邻路由器的优先级。仅对non-broadcast接口类型有效，范围:0-255，缺省值为1
＜poll-interval＞|相邻路由器的轮询间隔。仅对non-broadcast接口类型有效，范围:120-65535，缺省值为120
＜cost＞|到相邻路由器的代价。仅对point-to-multipoint non-broadcast接口类型有效，范围:1-65535，缺省值取决于接口自动计算






No参数|描述
---|---
priority|清除邻居优先级
poll-interval|清除邻居轮询时间
cost|清除邻居花费值








缺省 :

没有配置邻居 






使用说明 :

non-broadcast或point-to-multipoint non-broadcast接口类型的网络中，只有通过配置相邻路由器才能建立邻居关系。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#network non-broadcastZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#neighbor fe80::2f0:e0ff:fe21:203 priority 25





相关命令 :

network 




network :

network 




命令功能 :

设置接口网络类型。使用no命令恢复缺省类型。 






命令模式 :

 IPv6-OSPF接口模式  






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

缺省类型取决于接口所属网络的属性。 






使用说明 :

non-broadcast类型与带有参数non-broadcast的point-to-multipoint类型，需要配合neighbor命令使用，才能正常运行。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 1ZXROSNG(config-ospfv3-1-area-1)#interface gei-0/1/0/1 instance 1ZXROSNG(config-ospfv3-1-area-1-if-gei-0/1/0/1)#network point-to-point





相关命令 :

neighbor 




## notify default route 


notify default route 




命令功能 :

当本路由器通过其他协议或配置静态路由方式获得一条缺省路由::/0时，需要将其通告；没有缺省路由时，则按正常方式通告具体的可达路由；使用该命令后路由器成为一个ASBR 






命令模式 :

 IPv6-OSPF模式  






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
ext-2|设置重分配后的lsa的metric-type为ext-2
ext-1|设置重分配后的lsa的metric-type为ext-1
＜map-tag＞|产生该缺省路由的路由映射名称，长度1–31个字符






No参数|描述
---|---
metric|清除默认路由的花费值
metric-type|清除默认路由的花费类型
route-map|清除默认路由的映射表








缺省 :

无 






使用说明 :

无 






范例 :

无论本路由器是否存在缺省路由，都通告一条缺省路由，且该缺省路由的费用为20，缺省路由类型为ext-1，使用的route-map为map：ZXROSNG(config)#ipv6 router ospf 1ZXR10 (config-ospfv3-1)#notify default route always metric 20 metric-typeext-1 route-map map





相关命令 :

无 




## nsf 


nsf 




命令功能 :

使能ospfv3的GR功能 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



nsf 
 

no nsf 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

使能nsf之后，会在下次重启后生效 






范例 :

ZXROSNG(config-ospfv3-1)#nsf 






相关命令 :

grace period 




## passive 


passive 




命令功能 :

配置被动接口功能。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



passive 
 

no passive 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if- gei-0/1/0/1)#passive





相关命令 :

无 




## prefix-priority 


prefix-priority 




命令功能 :

配置OSPF的前缀优先级收敛命令，使匹配命令的LSA优先得到计算。 






命令模式 :

 IPv6-OSPF模式  






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
critical|配置critical级别的优先级
high|配置high级别的优先级
medium|配置medium级别的优先级
prefix-name|匹配prefix-list
＜prefix-name＞|匹配的prefix-list的名称，长度为1-31个字符
tag|匹配tag
＜tag-number＞|匹配的tag值，范围为0-4294967295








缺省 :

无 






使用说明 :

1.每个优先级只能配置一个带prefix-name的命令，继续配置新的带prefix-name的命令会覆盖之前的配置。每个优先级最多可以配置20个带tag的命令。2. no命令是只针对已配置的prefix-priority命令的反操作，如果不存在相应prefix-priority命令，则no命令无效。如果是no带prefix-name的命令，则不需要带prefix-list的名称；如果是no到tag的命令，则需要带tag的数值大小.





范例 :

1.配置一个critical优先级的匹配prefix-list的命令，其prefix-list名称为zxr10ZXROSNG(config-ospfv3-1)# prefix-priority critical prefix-name zxr102.配置一个匹配critical优先级的匹配tag的命令，tag的值为1ZXROSNG(config-ospfv3-1)#prefix-priority critical tag 13. no掉critical优先级的匹配prefix-list的命令ZXROSNG(config-ospfv3-1)# no prefix-priority critical prefix-name4. no掉匹配critical优先级的匹配tag的值为1的命令ZXROSNG(config-ospfv3-1)#no prefix-priority critical tag 1





相关命令 :

无 




## priority 


priority 




命令功能 :

设置接口优先级。使用no命令使接口优先级恢复到缺省值。 






命令模式 :

 IPv6-OSPF接口模式  






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
＜priority＞|接口优先级，范围：0-255，缺省为1








缺省 :

缺省值为1 






使用说明 :

1．该命令用于修改接口优先级值。2．接口优先级设置为0的时候，该路由器不能作为DR和BDR。





范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#priority 20





相关命令 :

无 




## range 


range 




命令功能 :

配置区域内的汇总地址范围。使用no命令使配置的汇总地址范围失效。 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


range 
  ＜ipv6-address-mask 
＞ [{advertise 
|not-advertise 
}]
no range 
  ＜ipv6-address-mask 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address-mask＞|汇总的v6路由前缀及前缀长度
advertise|通告汇总3-type链路状态通告
not-advertise|禁止通告汇总3-type链路状态通告








缺省 :

没有指定区域的汇总地址范围。 






使用说明 :

此命令只能用在区域边界路由器（ABR）上，它用作对一个区域进行合并计算和汇总路由，其结果是一个概要路由被区域边界路由器通告到其他区域，路由选择信息在区域边界被压缩。若指定区域不存在则自动创建。





范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 3 ZXROSNG(config-ospfv3-1-area-3)#range 1:2::2:5/128 not-advertise





相关命令 :

无 




redistribute :

redistribute 




命令功能 :

重分配其他协议的路由到OSPFv3中。使用no命令则取消对该协议的重分配。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


redistribute 
  {static 
|connected 
|rip 
|ospf 
 ＜process-id 
＞|isis 
 ＜process-id 
＞|bgp 
|subscriber-host 
|aftr 
|sf-nat64 
|sl-nat64 
|dhcp-pd 
|subscriber-aggregation 
|user-special 
|ps-busi-addr 
|ps-user-addr 
|zenic-local 
|bras-pool 
|dyn-leasedline 
} [{[with-originate-metric 
],[tag 
 ＜tag-value 
＞],[metric 
 ＜metric-value 
＞],[metric-type 
 {ext-2 
|ext-1 
}],[route-map 
 ＜routemap 
＞],[host-only 
]}]
no redistribute 
  {static 
|connected 
|rip 
|ospf 
 ＜process-id 
＞|isis 
 ＜process-id 
＞|bgp 
|subscriber-host 
|aftr 
|sf-nat64 
|sl-nat64 
|dhcp-pd 
|subscriber-aggregation 
|user-special 
|ps-busi-addr 
|ps-user-addr 
|zenic-local 
|bras-pool 
|dyn-leasedline 
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
static|重分配静态路由
connected|重分配直连路由
rip|重分配RIP路由
ospf|重分配OSPF路由
＜process-id＞|OSPF路由的实例ID
isis|重分配ISIS路由
＜process-id＞|OSPF路由的实例ID
bgp|重分配BGP路由
subscriber-host|重分配subscriber-host路由
aftr|重分配aftr路由
sf-nat64|重分配sf-nat64路由
sl-nat64|重分配sl-nat64路由
dhcp-pd|重分配DHCP-PD路由
subscriber-aggregation|重分配subscriber-aggregation路由
user-special|重分配user-special路由
ps-busi-addr|重分配PS-BUSI-ADDR路由
ps-user-addr|重分配PS-USER-ADDR路由
zenic-local|重分配zenic-local路由
bras-pool|重分发BRAS-pool路由
dyn-leasedline|重分配dyn-leasedline路由
with-originate-metric|使用原始路由的花费值
＜tag-value＞|重分配BGP路由的tag值
＜metric-value＞|重分配路由的metric值
ext-2|设置重分配后的lsa的metric-type为ext-2
ext-1|设置重分配后的lsa的metric-type为ext-1
＜routemap＞|重分配该协议所使用的路由图
host-only|仅重分配主机路由






No参数|描述
---|---
tag|清除重分配的tag
metric|清除重分配的花费值
metric-type|清除重分配的花费类型
route-map|清除重分配的映射表








缺省 :

无 






使用说明 :

使用该命令可以从其他协议路由重分配路由到OSPFv3中，并可以使用metric、metric-type、route-map等手段进行调整控制。配置此命令生效后，该路由器成为自治系统边界路由器（ASBR）。





范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#redistribute bgp metric 12 metric-type ext-1





相关命令 :

default-metric 




## retransmit-interval 


retransmit-interval 




命令功能 :

指定接口重传LSA的时间间隔。使用no命令使接口重传LSA的时间间隔恢复到缺省值。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



retransmit-interval 
  ＜retransmit-interval 
＞

no retransmit-interval 








命令参数解释 :



参数|描述
---|---
＜retransmit-interval＞|接口重传LSA的时间间隔，单位：秒，范围：1-65535，缺省为5秒








缺省 :

缺省值为5s 






使用说明 :

该命令用于修改接口重传LSA的时间间隔。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#retransmit-interval 20





相关命令 :

无 




## router-id 


router-id 




命令功能 :

指定一个OSPFv3实例的路由器标识符。使用no命令删除指定的路由器标识符。 






命令模式 :

 IPv6-OSPF模式  






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

无 






使用说明 :

使用该命令可以设置该OSPFv3实例的路由器标识符，从而使协议开始正常运行。使用no命令后，协议实例不能进行正常的运行。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#router-id 10.80.52.103





相关命令 :

ipv6 router ospf 




## segment-routing mpls 


segment-routing mpls 




命令功能 :

配置路由器OSPFv3模块的SR功能。 






命令模式 :

 IPv6-OSPF模式  






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
enable|使能设备SR功能
disable|去使能设备SR功能








缺省 :

默认不使能 






使用说明 :

使用场景当需要使用OSPF报文携带SR标签时，可以使能该配置。






范例 :

配置IPv6 OSPF实例1先使能SR再去使能SR。ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#segment-routing mpls enableZXROSNG(config-ospfv3-1) #segment-routing mpls disable






相关命令 :

无 




## show debug ospfv3 


show debug ospfv3 




命令功能 :

显示OSPFv3实例的debug配置情况 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug ospfv3 
  [＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPF进程号，范围1-16777215








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show debug ospfv3 OSPFv3 process 1:   OSPFv3 events ABR debugging is on  OSPFv3 events ASBR debugging is on  OSPFv3 events os debugging is on  OSPFv3 events router debugging is on  OSPFv3 events vlink debugging is on  OSPFv3 ifsm status debugging is on  OSPFv3 ifsm event debugging is on  OSPFv3 ifsm timer debugging is on  OSPFv3 lsa generate debugging is on  OSPFv3 lsa flooding debugging is on  OSPFv3 lsa install debugging is on  OSPFv3 lsa refresh debugging is on  OSPFv3 lsa maxage debugging is on  OSPFv3 nfsm status debugging is on  OSPFv3 nfsm event debugging is on  OSPFv3 nfsm timer debugging is on  OSPFv3 nsm intf debugging is on  OSPFv3 nsm rdst debugging is on  OSPFv3 packet hello debugging is on  OSPFv3 packet dd debugging is on  OSPFv3 packet req debugging is on  OSPFv3 packet upd debugging is on  OSPFv3 packet ack debugging is on  OSPFv3 packet detail debugging is on  OSPFv3 rt intra debugging is on  OSPFv3 rt inter debugging is on  OSPFv3 rt external debugging is on  OSPFv3 rt install debugging is on  OSPFv3 rt range debugging is on  OSPFv3 rt summary debugging is onOSPFv3 process 2:   OSPFv3 events abr debugging is on  OSPFv3 events asbr debugging is on  OSPFv3 events os debugging is on  OSPFv3 events router debugging is on  OSPFv3 events vlink debugging is on  OSPFv3 ifsm status debugging is on  OSPFv3 ifsm event debugging is on  OSPFv3 ifsm timer debugging is on  OSPFv3 lsa generate debugging is on  OSPFv3 lsa flooding debugging is on  OSPFv3 lsa install debugging is on  OSPFv3 lsa refresh debugging is on  OSPFv3 lsa maxage debugging is on  OSPFv3 nfsm status debugging is on  OSPFv3 nfsm event debugging is on  OSPFv3 nfsm timer debugging is on  OSPFv3 nsm intf debugging is on  OSPFv3 nsm rdst debugging is on  OSPFv3 packet hello debugging is on  OSPFv3 packet dd debugging is on  OSPFv3 packet req debugging is on  OSPFv3 packet upd debugging is on  OSPFv3 packet ack debugging is on  OSPFv3 packet detail debugging is on  OSPFv3 rt intra debugging is on  OSPFv3 rt inter debugging is on  OSPFv3 rt external debugging is on  OSPFv3 rt install debugging is on  OSPFv3 rt range debugging is on  OSPFv3 rt summary debugging is onOSPFv3 process 3:   OSPFv3 events abr debugging is on  OSPFv3 events asbr debugging is on  OSPFv3 events os debugging is on  OSPFv3 events router debugging is on  OSPFv3 events vlink debugging is on  OSPFv3 ifsm status debugging is on  OSPFv3 ifsm event debugging is on  OSPFv3 ifsm timer debugging is on  OSPFv3 lsa generate debugging is on  OSPFv3 lsa flooding debugging is on  OSPFv3 lsa install debugging is on  OSPFv3 lsa refresh debugging is on  OSPFv3 lsa maxage debugging is on  OSPFv3 nfsm status debugging is on  OSPFv3 nfsm event debugging is on  OSPFv3 nfsm timer debugging is on  OSPFv3 nsm intf debugging is on  OSPFv3 nsm rdst debugging is on  OSPFv3 packet hello debugging is on  OSPFv3 packet dd debugging is on  OSPFv3 packet req debugging is on  OSPFv3 packet upd debugging is on  OSPFv3 packet ack debugging is on  OSPFv3 packet detail debugging is on  OSPFv3 rt intra debugging is on  OSPFv3 rt inter debugging is on  OSPFv3 rt external debugging is on  OSPFv3 rt install debugging is on  OSPFv3 rt range debugging is on  OSPFv3 rt summary debugging is onOSPFv3 process 4:   OSPFv3 events abr debugging is on  OSPFv3 events asbr debugging is on  OSPFv3 events os debugging is on  OSPFv3 events router debugging is on  OSPFv3 events vlink debugging is on  OSPFv3 ifsm status debugging is on  OSPFv3 ifsm event debugging is on  OSPFv3 ifsm timer debugging is on  OSPFv3 lsa generate debugging is on  OSPFv3 lsa flooding debugging is on  OSPFv3 lsa install debugging is on  OSPFv3 lsa refresh debugging is on  OSPFv3 lsa maxage debugging is on  OSPFv3 nfsm status debugging is on  OSPFv3 nfsm event debugging is on  OSPFv3 nfsm timer debugging is on  OSPFv3 nsm intf debugging is on  OSPFv3 nsm rdst debugging is on  OSPFv3 packet hello debugging is on  OSPFv3 packet dd debugging is on  OSPFv3 packet req debugging is on  OSPFv3 packet upd debugging is on  OSPFv3 packet ack debugging is on  OSPFv3 packet detail debugging is on  OSPFv3 rt intra debugging is on  OSPFv3 rt inter debugging is on  OSPFv3 rt external debugging is on  OSPFv3 rt install debugging is on  OSPFv3 rt range debugging is on  OSPFv3 rt summary debugging is on





相关命令 :

无 




## show error packet ospfv3 


show error packet ospfv3 




命令功能 :

OSPFv3显示协议的错误报文信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show error packet ospfv3 
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
＜process-id＞|指定实例查询，范围1-16777215
＜interface-name＞|指定接口查询
＜number＞|查询最新异常报文的数目，范围1-200
detail|是否需要显示具体报文详细信息








缺省 :

无 






使用说明 :

1.指定实例或接口的时候不能加上显示数目。 






范例 :

OSPFv3显示协议错误报文统计信息：ZXROSNG(config)# show error packet ospfv3 statisticsPacket Type                 NumberUnknown Type Packet         0Hello                       17Database Description        0Link State Request          0Link State Update           0Link State Acknowledgment   0Total                       17域    描述Hello    Hello错误报文数目Database Description    DD错误报文数目Link State Reques    LSR错误报文数目Link State Update    LSU错误报文数目Link State Acknowledgment    LSA错误报文数目Total    所有错误报文总数OSPFv3显示协议错误报文详细的统计信息：ZXROSNG#show error packet ospfv3 statistics detail   Hello:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Bad option:                      0    DR or BDR error:                 0    Hello interval mismatch:         0    Dead interval mismatch:          0    Total                            0  Database Description:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Local MRU mismatch neighbor MTU: 0    Bad option:                      0    Total                            0  Link State Request:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Total                            0  Link State Update:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Total                            0  Link State Acknowledgment:    Bad checksum:                    0    Bad authentication type:         0    Bad authentication key:          0    Bad authentication sequence:     0    Bad digest:                      0    VPN ID mismatch:                 0    Bad TTL:                         0    Bad packet length:               0    Bad router id:                   0    Local interface invalid:         0    Neighbor invalid:                0    Bad source address:              0    Bad dest address:                0    Area mismatch:                   0    Bad version:                     0    Total                            0域    描述Bad checksum: 验证码不对，报文里携带的checksum和计算出的不一致Bad authentication type: 报文里携带的认证类型和收报接口的认证类型不匹配Bad authentication key： 认证的key不匹配  Bad authentication sequence：认证的seq不正确，比如没有递增Bad digest:报文里携带的摘要和本地根据报文计算出的不一致VPN ID mismatch:socket报文解析出的vpn id和本地收报接口所在的vpn id不一致Bad TTL:解析出来的TTL错误Bad packet length:：报文长度不对，比如ospf的报文长度大于ip的报文长度，比如小于报文的最小长度等等Bad router id:报文里携带的router id不对，比如为0，比如和收报接口所在实例的router id一致Local interface invalid：收报接口异常，比如找不到，比如接口状态是down，比如是passiveNeighbor invalid:邻居不对，比如邻居状态是downBad source address:报文发送的源地址有错误Bad dest address:收报的目的地址有错误Area mismatch:报文发送端和接收端区域不一致Bad version:    报文里携带的version字段不对Local MRU mismatch neighbor MTU:DD报文本地的MRU小于报文里携带的MTU Bad option:  DD报文和HELLO报文中携带的option字段与本地检查冲突，比如携带了Nbit，但是本地接口不在nssa区域    DR or BDR error:  hello报文中携带的dr，bdr信息异常    Hello interval mismatch:        hello报文中携带的hello interval和收报接口不一致    Dead interval mismatch:         hello报文中携带的dead inteval和收报接口的不一致OSPFv3显示实例1的协议错误报文详细信息：ZXROSNG(config)# show error packet ospfv3 process 1 detailPacket index  : 1Record time   : 2016-05-18 20:16:57Process ID    : 1Area ID       : 0.0.0.1Interface     : gei-0/1/0/1PDU type      : HelloError reason  : Bad HelloInterval expected:1, received:10Packet length : 360x00000000: 03 01 00 24 02 02 02 02 00 00 00 01 00 00 00 000x00000010: 00 00 00 06 01 00 00 13 00 0a 00 28 00 00 00 000x00000020: 00 00 00 00域    描述Packet index      错误报文记录索引Record time     错误报文记录时间Process ID    错误报文接收所在实例Area ID      错误报文接收所在区域Interface    错误报文接收接口PDU type    错误报文类型Error reason    错误报文原因Packet length    错误报文长度0x000000000x00000010..    错误报文内容





相关命令 :

无 




## show ipv6 ospf database 


show ipv6 ospf database 




命令功能 :

显示OSPFv3实例的数据库信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf database 
  [{[process 
 ＜process-id 
＞],[{router 
|network 
|external 
|inter-prefix 
|intra-prefix 
|intra-te 
|inter-router 
|link 
|router-info 
|srv6-locator 
|[extended 
 {intra-prefix 
|inter-prefix 
|external 
|router 
}]}],[adv-router 
 ＜router-id 
＞]}] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPFv3进程号，范围：1-16777215
router|表示router-lsa
network|表示network-lsa
external|表示as-external-lsa
inter-prefix|表示inter-area-prefix-lsa
intra-prefix|表示intra-area-prefix-lsa
intra-te|表示Intra-Area-TE-LSA
inter-router|表示inter-area-router-lsa
link|表示link-lsa
router-info|表示router-info-lsa
srv6-locator|表示srv6-locator-lsa
intra-prefix|表示intra-area-prefix-lsa
inter-prefix|表示inter-area-prefix-lsa
external|表示as-external-lsa
router|表示router-lsa
＜router-id＞|表示通告lsa的路由器标识符（IP地址形式）








缺省 :

无 






使用说明 :

使用show ipv6 ospf database可以显示所有的lsa数据库信息。 






范例 :

ZXROSNG(config-ospfv3-1)#show ipv6 ospf database             OSPFv3 Router with ID (1.1.1.1) (Process ID 1)                Router Link States (Area 0.0.0.0)ADV Router       Age        Seq#        Link count         Bits1.1.1.1         1391        0x80000040           1      -|-|E|-2.2.2.2         1396        0x8000003c           1      -|-|-|-                Net Link States (Area 0.0.0.0)ADV Router       Age        Seq#           Link ID    Rtr count2.2.2.2         1396        0x8000004f           3            2                Link (Type-8) Link States (Area 0.0.0.0)ADV Router       Age        Seq#          Link ID    Interface1.1.1.1          970        0x80000033          3    gei-0/1/0/12.2.2.2          857        0x80000033          3    gei-0/1/0/1






相关命令 :

无 




## show ipv6 ospf interface 


show ipv6 ospf interface 




命令功能 :

显示OSPFv3实例的接口信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf interface 
  [＜interface-name 
＞] [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|需要单独显示的接口名称
＜process-id＞|OSPFv3进程号，范围：1-16777215








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-ospfv3-1)#show ipv6 ospf interface gei-0/1/0/1 is up, line protocol is up  Link Local Address fe80::2f0:e0ff:fe21:201, Interface ID 2  Area 127.255.255.253, Process ID 1, Instance ID 1, Router ID 1.1.11.11  Network Type POINT_TO_MULTIPOINT, Cost: 65535  Transmit Delay is 65535 sec, State POINT_TO_POINT,  No designated router on this network  No backup designated router on this network  Timer intervals configured, Hello 65535, Dead 65535, Wait 65535, Retransmit 65535    Hello due in 17:05:17  Neighbor Count is 0, Adjacent neighbor count is 0gei-0/1/0/2 is up, line protocol is up  Link Local Address fe80::2f0:e0ff:fe21:201, Interface ID 3  Area 0.0.0.0, Process ID 1, Instance ID 1, Router ID 1.1.11.11  Network Type BROADCAST, Cost: 10  Transmit Delay is 1 sec, State DR, Priority 1  Designated Router (ID) 1.1.11.11, local address fe80::2f0:e0ff:fe21:201  No backup designated router on this network  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5    Hello due in 00:00:03  Neighbor Count is 0, Adjacent neighbor count is 0





相关命令 :

无 




## show ipv6 ospf neighbor 


show ipv6 ospf neighbor 




命令功能 :

显示OSPFv3实例的邻居信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf neighbor 
  {[interface 
 ＜interface-name 
＞] [＜neighbor-id 
＞] [process 
 ＜process-id 
＞] [detail 
]|summary 
 [process 
 ＜process-id 
＞]} 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|需要显示的接口名称
＜neighbor-id＞|需要显示的邻居的路由器标识符（IP地址形式）
＜process-id＞|OSPFv3进程号，范围：1-16777215
detail|需要显示的邻居具体内容
summary|需要显示的邻居数量统计内容
＜process-id＞|OSPFv3进程号，范围：1-16777215








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ipv6 ospf neighbor OSPFv3 Process 1Neighbor ID     Pri   State           Dead Time   Interface ID    Interface1.1.11.13         1   EXCHANGE/DR     00:00:35               2     gei-0/1/0/1ZXROSNG(config)#show ipv6 ospf neighbor detaZXROSNG(config)#show ipv6 ospf neighbor detail  Neighbor 1.1.11.13    In the area 127.255.255.253 via interface gei-0/1/0/1    Neighbor interface-id 2, link-local address fe80::2f0:e0ff:fe21:203    Neighbor priority is 1, State is EXSTART, 34 state changes    DR is 1.1.11.13 BDR is 1.1.11.11    Options is 0x000013    Dead timer due in 00:00:00    Neighbor is up for 00:02:49





相关命令 :

无 




## show ipv6 ospf request-list 


show ipv6 ospf request-list 




命令功能 :

显示路由器请求的所有链路状态通告列表。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf request-list 
  {[interface 
 ＜interface-name 
＞]|＜neighbor-id 
＞|[process 
 ＜process-id 
＞]} 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|显示所有在该接口上等待请求的链路状态通告
＜neighbor-id＞|显示所有等待向该邻居请求的链路状态通告
＜process-id＞|OSPF进程号，范围1-16777215








缺省 :

无 






使用说明 :

无 






范例 :

R4#show ipv6 ospf request-list interface gei-0/1/0/1.2            OSPFv3 Router with ID (4.4.4.4) (Process ID 1) Neighbor 5.5.5.5, interface gei-0/1/0/1.2Type      LS ID           ADV RTR         Seq NO      Age    Checksum0x0008    0.0.0.13        4.4.4.4         0x80000021  17     0xbcf70x0008    0.0.0.13        5.5.5.5         0x80000020  1248   0x7e110x2001    0.0.0.0         3.3.3.3         0x8000003a  949    0x1aa8






相关命令 :

无 




## show ipv6 ospf retransmission-list 


show ipv6 ospf retransmission-list 




命令功能 :

显示路由器重传的所有链路状态通告列表。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf retransmission-list 
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
＜process-id＞|OSPF进程号，范围1-16777215








缺省 :

无 






使用说明 :

无 






范例 :

R4#show ipv6 ospf retransmission-list interface gei-0/1/0/1.2            OSPFv3 Router with ID (4.4.4.4) (Process ID 1) Neighbor 5.5.5.5, interface gei-0/1/0/1.2Type      LS ID           ADV RTR         Seq NO      Age    Checksum0x0008    0.0.0.13        4.4.4.4         0x80000023  0      0xb8f90x2001    0.0.0.0         4.4.4.4         0x80000025  0      0xe8d10x2009    0.0.0.1         4.4.4.4         0x80000001  3600   0xf46b






相关命令 :

无 




## show ipv6 ospf route 


show ipv6 ospf route 




命令功能 :

显示OSPFv3进程的路由信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf route 
  [{summary 
 [process 
 ＜process-id 
＞]|[{{[process 
 ＜process-id 
＞],[adv-router 
 ＜adv-router 
＞]}|[network 
 {＜ipv6-address 
＞|＜ipv6-address-mask 
＞}]}] [detail 
]}] 







命令参数解释 :



参数|描述
---|---
summary|显示路由统计信息
＜process-id＞|OSPFv3进程号，范围：1-16777215
＜process-id＞|OSPFv3进程号，范围：1-16777215
＜adv-router＞|通告路由器ID
＜ipv6-address＞|IPv6地址前缀
＜ipv6-address-mask＞|IPv6地址前缀和掩码，范围0-128
detail|显示路由详细信息








缺省 :

无 






使用说明 :

使用show ipv6 ospf route命令可以显示所有实例的统计信息，或者指定实例的统计信息，也可以按照通告路由器ID和实例号的组合情况显示路由信息，带了detail表示显示详细信息，否则显示摘要信息。 






范例 :

ZXROSNG(config-ospfv3-1)#show ipv6 ospf routeOSPF Local Ipv6 Routing TableCodes: D3 - OSPF type3 discard, D5 - OSPF type5 discard, O - OSPF intra,        OI - OSPF inter, E1 - OSPF ext 1, E2 - OSPF ext 2Process ID: 1 There is totally 1 route.OSPF 1.1.1.1/32 [2/110]   via fe80::12c1:ffff:feab:2100, gei-0/1/0/2   via 22:2::0:1, gei-0/1/0/3   Advertised information:   LS Type: 1, LS ID: 255.255.255.255, adv-router: 255.255.255.255    Area 255.255.255.255, metric 16777215,critical priority, best, 0h1m44s    nexthop: fe80:fe80:12c1:ffff:feab:2100:fe80:fe80    nexthop: fe80:fe80:12c1:ffff:feab:2100:fe80:fe80   LS Type: 1, LS ID: 255.255.255.255, adv-router: 255.255.255.255    Area 255.255.255.255, metric 16777215,critical priority, best, 0h1m44s    nexthop: fe80:fe80:12c1:ffff:feab:2100:fe80:fe80    nexthop: fe80:fe80:12c1:ffff:feab:2100:fe80:fe80 





相关命令 :

无 




## show ipv6 ospf vertex 


show ipv6 ospf vertex 




命令功能 :

显示OSPFv3的节点路由信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf vertex 
  [{[backup 
],[process 
 ＜process-id 
＞]}] 







命令参数解释 :



参数|描述
---|---
backup|是否显示节点备份路由信息
＜process-id＞|OSPFv3实例号








缺省 :

显示所有OSPFv3实例的节点主路由信息。 






使用说明 :

可以指定实例ID，显示某个实例的节点信息。也可以指定显示备份路由信息。当显示备份路由信息的时候，会显示保护类型和保护路径。 






范例 :

ZXROSNG(config)#show ipv6 ospf vertex backup process 1 






相关命令 :

fast-reroute 




## show ipv6 ospf virtual-links 


show ipv6 ospf virtual-links 




命令功能 :

显示OSPFv3实例的虚链信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf virtual-links 
  [process 
 ＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPFv3进程号，范围：1-16777215








缺省 :

无 






使用说明 :

使用该命令显示所有的虚链信息，包括建链情况等。 






范例 :

ZXROSNG(config-ospfv3-1)#show ipv6 ospf virtual-links Virtual Link OSPF_VL0 to router 1.1.11.13 is down  Interface ID 2147483648, IPv6 address ::  Run as demand circuit  Transit area 0.0.0.1, Cost of using 65535  Transmit Delay is 1 sec, State DOWN,  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5





相关命令 :

无 




## show ipv6 ospf 


show ipv6 ospf 




命令功能 :

显示OSPFv3的实例信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 ospf 
  [＜process-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜process-id＞|OSPFv3进程号，范围：1-16777215








缺省 :

无 






使用说明 :

使用show ipv6 ospf命令可以显示已经启动的所有OSPFv3实例信息；后面加上OSPFv3进程号可以显示特定的OSPFv3实例信息。 






范例 :

ZXROSNG(config-ospfv3-1)#show ipv6 ospfRouting Process "ospfv3 1" with ID 1.1.1.1 socket enable SPF schedule delay 5 secs. Hold time between two SPFs 10 secs Minimum LSA interval 5 secs. Minimum LSA arrival 1 secs Number of external LSA 0. Checksum Sum 0x000000 The number of ospfv3 routes is 0 Default metric is 0 Number of areas in this router is 1. 1 normal 0 stub    Area BACKBONE(0)        Number of interfaces in this area is 1        SPF algorithm executed 64 times        Number of LSA 5. Checksum Sum 0x03F22E        Number of Unknown LSA 0






相关命令 :

无 




## snmp context 


snmp context 




命令功能 :

设置OSPFv3实例的SNMP标识以支持MIB多实例显示 






命令模式 :

 IPv6-OSPF模式  






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

不同OSPFv3实例不能配置相同的snmp context。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#snmp context zteZXROSNG(config-ospfv3-1)#exit





相关命令 :

snmp-server context 




## stub 


stub 




命令功能 :

定义一个区域为stub区域。使用no命令取消配置。 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


stub 
  [{[no-summary 
],[default-information-originate 
]}]
no stub 
  [{[no-summary 
],[default-information-originate 
]}]
				






命令参数解释 :



参数|描述
---|---
no-summary|禁止区域边界路由器（ABR）将汇总路由信息发送到该stub区域
default-information-originate|向stub区域通告静态缺省路由








缺省 :

1）    区域默认不是stub区域。2）    对于stub区域来说:    不配置no-summary选项的情况下，允许ABR向stub区域通告其它区域的汇总信息。    不配置default-information-originate选项的情况下，如果stub区域不是协议规定的ABR，不会向stub区域通告缺省路由。





使用说明 :

不让ABR往stub区域通告汇总路由信息可以配置no-summary选项；如果想向stub区域通告静态缺省路由可以通过配置default-information-originate选项。





范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 3 ZXROSNG(config-ospfv3-1-area-3)#stub





相关命令 :

default-cost 




## summary-prefix 


summary-prefix 




命令功能 :

为OSPF建立汇聚地址，汇总正重新分配到OSPF的其他路由选择协议路径。使用no命令取消配置。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :


summary-prefix 
  ＜ipv6-address-mask 
＞
no summary-prefix 
  ＜ipv6-address-mask 
＞
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address-mask＞|汇总的v6路由前缀及前缀长度








缺省 :

OSPF无汇聚地址。 






使用说明 :

此命令有助于减少路由表的大小。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#summary-prefix 10::0/120 





相关命令 :

无 




## timers spf 


timers spf 




命令功能 :

设置收到变化后导致路由重新计算的时间间隔，及路由计算中的时间间隔。使用no命令恢复默认值。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers spf 
 delay 
 ＜delay 
＞ hold-time 
 ＜holdtime 
＞

no timers spf 








命令参数解释 :



参数|描述
---|---
＜delay＞|设置收到变化后导致路由重新计算的时间间隔，单位：秒，取值范围:0-65535，缺省值为5秒
＜holdtime＞|路由计算中的时间间隔，单位：秒，取值范围:0-65535，缺省值为10秒








缺省 :

缺省的delay值为5s,缺省的hold-time值为10s 






使用说明 :

使用该命令可修改上述两个定时器的值，从而影响路由计算及最终路由生成的时间。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#timers spf delay 2009 hold-time 65535






相关命令 :

无 




## timers throttle lsa 


timers throttle lsa 




命令功能 :

配置OSPF的LSA更新退避，当网络变化频繁时，LSA更新间隔时间会自动延长，避免过度占用CPU资源。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers throttle lsa 
  ＜start time 
＞ ＜dealy time 
＞ ＜max delay time 
＞

no timers throttle lsa 








命令参数解释 :



参数|描述
---|---
＜start time＞|第一次更新LSA的时延，范围：1-600000，单位：毫秒
＜dealy time＞|连续两次LSA更新的最小延迟时间，范围：1-600000，单位：毫秒
＜max delay time＞|连续两次LSA更新的最大延迟时间，范围：1-600000，单位：毫秒








缺省 :

无 






使用说明 :

1.min-delay-time必须大于等于hold-time，如果不满足，将自动调整为和hold-time相等。2.max-delay-time必须大于等于min-delay-time，如果不满足，将自动调整为和min-delay-time相等。






范例 :

1配置LSA更新退避命令，其hold-time为10毫秒，min-delay-time为20毫秒，max-delay-time为30毫秒。ZXROSNG(config-ospfv3-1)# timers throttle lsa 10 20 302删除LSA更新退避配置ZXROSNG(config-ospfv3-1)# no timers throttle lsa






相关命令 :

无 




## timers throttle lsa-arrival 


timers throttle lsa-arrival 




命令功能 :

配置OSPF的LSA接收退避，当网络变化频繁时，接收LSA的间隔时间会自动延长，避免过度占用CPU资源 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers throttle lsa-arrival 
  ＜hold time 
＞ ＜delay time 
＞ ＜max delay time 
＞

no timers throttle lsa-arrival 








命令参数解释 :



参数|描述
---|---
＜hold time＞|第一次接收LSA的时延，范围：1-600000，单位：毫秒
＜delay time＞|连续两次LSA接收的最小延迟时间，范围：1-600000，单位：毫秒
＜max delay time＞|连续两次LSA接收的最大延迟时间，范围：1-600000，单位：毫秒








缺省 :

无 






使用说明 :

1.min-delay-time必须大于等于hold-time，如果不满足，将自动调整为和hold-time相等。2.max-delay-time必须大于等于min-delay-time，如果不满足，将自动调整为和min-delay-time相等





范例 :

1配置LSA接收退避命令，其hold-time为10毫秒，min-delay-time为20毫秒，max-delay-time为30毫秒。ZXROSNG(config-ospfv3-1)# timers throttle lsa-arrive 10 20 302删除LSA接收退避配置ZXROSNG(config-ospfv3-1)# no timers throttle lsa-arrive





相关命令 :

无 




## timers throttle spf 


timers throttle spf 




命令功能 :

配置OSPF的SPF指数退避命令，减小SPF计算响应时间（毫秒级），加快网络的收敛速度。 






命令模式 :

 IPv6-OSPF模式  






命令默认权限级别 :

15 






命令格式 :



timers throttle spf 
  ＜start time 
＞ ＜dealy time 
＞ ＜max delay time 
＞

no timers throttle spf 








命令参数解释 :



参数|描述
---|---
＜start time＞|接收到变化时到第一次SPF计算之间的保持时间，范围：1-600000，单位：毫秒
＜dealy time＞|连续触发SPF计算时的最小延迟时间，范围：1-600000，单位：毫秒
＜max delay time＞|连续触发SPF计算时的最大延迟时间，范围：1-600000，单位：毫秒








缺省 :

无 






使用说明 :

1.delay-time必须大于等于hold-time，如果不满足，将自动调整为和hold-time相等。2.max-delay-time必须大于等于delay-time，如果不满足，将自动调整为和delay-time相等。





范例 :

1.配置spf指数退避命令，其hold-time为10毫秒，delay-time为20毫秒，max-delay-time为30毫秒：ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#timers throttle spf 10 20 30ZXROSNG(config-ospfv3-1)#exit2.删除spf指数退避配置ZXROSNG(config-ospfv3-1)# no timers throttle spf





相关命令 :

无 




## transmit-delay 


transmit-delay 




命令功能 :

指定接口传输一个链路状态更新数据包的迟延。使用no命令使接口传输一个链路状态更新数据包的迟延恢复到缺省值。 






命令模式 :

 IPv6-OSPF接口模式  






命令默认权限级别 :

15 






命令格式 :



transmit-delay 
  ＜transmit-delay 
＞

no transmit-delay 








命令参数解释 :



参数|描述
---|---
＜transmit-delay＞|接口传输一个链路状态更新数据包的迟延，单位：秒，范围:1-65535，缺省为1秒








缺省 :

缺省值为1s 






使用说明 :

该命令用于修改接口传输一个链路状态更新数据包的迟延。 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5) #interface gei-0/1/0/1ZXROSNG(config-ospfv3-1-area-5-if-gei-0/1/0/1)#transmit-delay 20





相关命令 :

无 




## virtual-link 


virtual-link 




命令功能 :

定义OSPF虚拟链路。使用no命令删除指定虚拟链路。 






命令模式 :

 IPv6-OSPF区域模式  






命令默认权限级别 :

15 






命令格式 :


virtual-link 
  ＜_neighbor_id 
＞ [{[hello-interval 
 ＜_hello 
＞],[retransmit-interval 
 ＜_retran 
＞],[transmit-delay 
 ＜_transmit 
＞],[dead-interval 
 ＜_dead 
＞]}] [{authentication 
 ipsec 
 spi 
 ＜_spi-id 
＞ {md5 
 {＜_md5_key 
＞|encrypted 
 ＜md5_key_encrypted 
＞}|sha1 
 {＜_sha1_key 
＞|encrypted 
 ＜sha1_key_encrypted 
＞}|keychain 
 ＜Keychain name 
＞}|encryption 
 ipsec 
 spi 
 ＜_spi-id 
＞ esp 
 {{aes-cbc 
 128 
 {＜_aes_cbc_128_key 
＞|encrypted 
 ＜aes_cbc_128_key_encrypted 
＞}|3des 
 {＜_3des_key 
＞|encrypted 
 ＜3des_key_encrypted 
＞}|des 
 {＜_des_key 
＞|encrypted 
 ＜des_key_encrypted 
＞}|null 
} {md5 
 {＜_md5_key 
＞|encrypted 
 ＜md5_key_encrypted 
＞}|sha1 
 {＜_sha1_key 
＞|encrypted 
 ＜sha1_key_encrypted 
＞}}|keychain-encryption 
 ＜Keychain name 
＞ keychain 
 ＜Keychain name 
＞}} [rollover-interval 
 ＜rollover-interva 
＞]]
no virtual-link 
  ＜para 
＞ [{[hello-interval 
],[retransmit-interval 
],[transmit-delay 
],[dead-interval 
],[authentication 
],[encryption 
]}]
				






命令参数解释 :



参数|描述
---|---
＜_neighbor_id＞|邻居路由器的router-id。
＜_hello＞|接口上hello报文时间间隔，单位：秒，范围:1-8192。
＜_retran＞|接口重传LSA的时间间隔，单位：秒，范围：1-8192。
＜_transmit＞|接口传输一个链路状态更新数据包的迟延，单位：秒，范围:1-8192。
＜_dead＞|接口上邻居的死亡时间，单位：秒，范围：1-8192。
ipsec|IPSEC加密。
＜_spi-id＞|安全策略索引(security policy index)值，合法的十进制值范围： 256-32767。
＜_md5_key＞|MD5密钥，为十六进制字符串，用户必须输入32个字符。
＜md5_key_encrypted＞|加密的MD5密钥,为十六进制字符串，用户必须输入64个字符。
＜_sha1_key＞|SHA1密钥，为十六进制字符串，用户必须输入40个字符。
＜sha1_key_encrypted＞|加密的SHA1密钥,为十六进制字符串，用户必须输入64个字符。
＜Keychain name＞|认证的keychain名称, 长度范围：1-31字符。
ipsec|IPSEC加密。
＜_spi-id＞|安全策略索引(security policy index)值，合法的十进制值范围： 256-32767。
128|AES-CBC加密方式。
＜_aes_cbc_128_key＞|128位密钥，为十六进制字符串，用户必须输入32个字符。
＜aes_cbc_128_key_encrypted＞|加密的128位密钥，为十六进制字符串，用户必须输入64个字符。
3des|3DES加密方式
＜_3des_key＞|192位密钥，为十六进制字符串，用户必须输入48个字符。
＜3des_key_encrypted＞|加密的192位密钥，为十六进制字符串，用户必须输入64个字符。
des|DES加密方式
＜_des_key＞|64位密钥，为十六进制字符串，用户必须输入16个字符。
＜des_key_encrypted＞|加密的64位密钥,为十六进制字符串，用户必须输入64个字符。
null|无加密
＜_md5_key＞|MD5密钥，为十六进制字符串，用户必须输入32个字符。
＜md5_key_encrypted＞|加密的MD5密钥,为十六进制字符串，用户必须输入64个字符。
＜_sha1_key＞|SHA1密钥，为十六进制字符串，用户必须输入40个字符。
＜sha1_key_encrypted＞|加密的SHA1密钥,为十六进制字符串，用户必须输入64个字符。
keychain-encryption|使用keychain进行IPSEC加密
＜Keychain name＞|认证的keychain名称, 长度范围：1-31字符。
＜Keychain name＞|认证的keychain名称, 长度范围：1-31字符。
＜rollover-interva＞|密钥生效延迟时间,此参数主要是为了当用户修改key值时，由于修改所有路由器上的key需要花费比较长的时间，因此需要进行一个平滑过渡的时期。此参数就是平滑过渡的间隔时间，单位为分钟。






No参数|描述
---|---
＜para＞|邻居ID
hello-interval|清除发送HELLO报文的时间间隔
retransmit-interval|清除重传报文的时间间隔
transmit-delay|清除更新数据包的迟延
dead-interval|清除邻居的死亡时间
authentication|清除虚链的认证
encryption|清除虚链的加密








缺省 :

没有定义虚拟链路。 






使用说明 :

虚链的加密和认证不能同时配置 






范例 :

ZXROSNG(config)#ipv6 router ospf 1ZXROSNG(config-ospfv3-1)#area 5ZXROSNG(config-ospfv3-1-area-5)virtual-link 1.1.1.1 encryption ipsec spi 256 esp des 1234567890123456 md5 12345678901234567890123456789012






相关命令 :

无 




# TCPv6配置命令 
## clear tcp6 connect 


clear tcp6 connect 




命令功能 :

该命令工作于特权模式，用于手动清除指定五元组(源地址、源端口、vrf域、远端地址、远端端口)的TCP6连接。当系统中有不需要的TCP6连接或者某个TCP6连接存在异常时，可使用该命令进行清除。清除命令执行后，TCP6首先发送RST重置报文通知对端清除相应的TCP6连接，然后再清除本端的TCP6连接信息。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear tcp6 connect 
  {＜local-ip-address 
＞|vrf 
 ＜vrf-name 
＞ ＜local-ip-address 
＞} ＜local-port 
＞ ＜remote-ip-address 
＞ ＜remote-port 
＞







命令参数解释 :



参数|描述
---|---
＜local-ip-address＞|本地IP地址，为十六进制点分形式
＜vrf-name＞|IP地址所属的VRF名称，长度为1-32个字符
＜local-ip-address＞|本地IP地址，为十六进制点分形式
＜local-port＞|本地端口号，范围1-65535
＜remote-ip-address＞|远端IP地址，为十六进制点分形式
＜remote-port＞|远端端口号，范围1-65535








缺省 :

无 






使用说明 :

清除TCP6连接的同时，会通知上层业务模块删除与该连接对应的邻居信息。对于BGP协议来说，会撤销之前在该邻居上学习的路由，导致路由振荡；对于FTP协议来说，会删除之前传输的数据，FTP拷贝终止。命令执行清除时，没有确认提示，请慎用该清除命令。





范例 :

通过clear命令清除系统中指定五元组的TCP6连接，则输入以下命令：ZXROSNG#show tcp6 briefTCB Index     Local Address             Foreign Address           State12295         3::1:50053                3::2:179                  ESTABZXROSNG#clear tcp6 connect 3::1 50053 3::2 179 





相关命令 :

show tcp6 brief  




## clear tcp6 statistics 


clear tcp6 statistics 




命令功能 :

该命令工作于特权模式，用于清除系统TCP6的统计信息。当需要观察系统在一段时间内TCP6的统计信息时，使用该命令清除当前的统计信息，以方便收集一段时间段内TCP6统计信息情况。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear tcp6 statistics 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

清除命令执行后，TCP6的统计信息（参见操作命令show tcp6 statistics）将全部清零，并开始重新的统计过程。清除命令执行后，将不能恢复之前的统计信息，请慎用该清除命令。





范例 :

统计信息显示参见操作命令show tcp6 statistics，则输入以下命令：ZXROSNG#show tcp6 statistics Rcvd: 8479 Total      0 checksum error, 0 bad offset, 0 too short      4398 packets (82532 bytes) in sequence      5 dup packets (38 bytes)      1 partially dup packets (19 bytes)      7 out-of-order packets (76 bytes)      0 packets (0 bytes) with data after window      0 packets after close      0 window probe packets, 0 window update packets      12 dup ack packets, 0 ack packets with unsend data      4378 ack packets (82167 bytes)Sent: 8768 Total      22 control packets (including 26 retransmitted)       4374 data packets (82161 bytes)      26 data packets (265 bytes) retransmitted      4359 ack only packets (4340 delayed)      0 window probe packets, 0 window update packets4 Connections initiated, 3 connections accepted, 6 connections established7 Connections closed (including 3 dropped, 0 embryonic dropped)24 Total rxmt timeout, 0 connections dropped in rxmt timeout1 Keepalive timeout, 0 keepalive probe, 1 connections dropped in keepalive通过clear命令清除系统TCP6统计信息，则输入以下命令： ZXROSNG#clear tcp6 statistics ZXROSNG#show tcp6 statistics  Rcvd: 0 Total      0 checksum error, 0 bad offset, 0 too short      0 packets (0 bytes) in sequence      0 dup packets (0 bytes)      0 partially dup packets (0 bytes)      0 out-of-order packets (0 bytes)      0 packets (0 bytes) with data after window      0 packets after close      0 window probe packets, 0 window update packets      0 dup ack packets, 0 ack packets with unsend data      0 ack packets (0 bytes)Sent: 0 Total      0 control packets (including 0 retransmitted)       0 data packets (0 bytes)      0 data packets (0 bytes) retransmitted      0 ack only packets (0 delayed)      0 window probe packets, 0 window update packets0 Connections initiated, 0 connections accepted, 0 connections established0 Connections closed (including 0 dropped, 0 embryonic dropped)0 Total rxmt timeout, 0 connections dropped in rxmt timeout0 Keepalive timeout, 0 keepalive probe, 0 connections dropped in keepalive





相关命令 :

show tcp6 statistics 




## clear tcp6 tcb 


clear tcp6 tcb 




命令功能 :

该命令工作于特权模式，用于手动清除指定索引号的TCP6连接。当系统中有不需要的TCP6连接或者某个TCP6连接存在异常时，可使用该命令进行清除。清除命令执行后，TCP6首先发送RST重置报文通知对端清除相应的TCP6连接，然后再清除本端的TCP6连接信息。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear tcp6 tcb 
  ＜tcb-index 
＞







命令参数解释 :



参数|描述
---|---
＜tcb-index＞|TCB索引，取值范围为1-4294967295








缺省 :

无 






使用说明 :

清除TCP6连接的同时，会通知上层业务模块删除与该连接对应的邻居信息。对于BGP协议来说，会撤销之前在该邻居上学习的路由，导致路由振荡；对于FTP协议来说，会删除之前传输的数据，FTP拷贝终止。命令执行清除时，没有确认提示，请慎用该清除命令。





范例 :

通过show tcp6 brief 命令查询TCB索引号，然后执行clear命令清除系统中指定索引号的TCP6连接，则输入以下命令：ZXROSNG#show tcp6 briefTCB Index     Local Address             Foreign Address           State12295         3::1:50053                3::2:179    ZXROSNG#clear tcp6 tcb 12295 





相关命令 :

show tcp6 brief 




## debug ipv6 tcp all 


debug ipv6 tcp all 




命令功能 :

该命令工作于特权模式，用于开启TCP6所有的打印开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 tcp all 
 

no debug ipv6 tcp all 








命令参数解释 :


					无
				 






缺省 :

关闭该调试功能 






使用说明 :

使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面TCP6控制事件信息。开启的TCP6打印开关包括报文收发打印开关（参见操作命令debug ipv6 tcp packet）、控制信息打印开关（参见操作命令debug ipv6 tcp driver））、重要处理信息打印开关（参见操作命令debug ipv6 tcp transactions）。可使用no debug ipv6 tcp all或者no debug all命令关闭该debug开关。





范例 :

打开TCP6所有的debug开关，则输入以下命令：ZXROSNG#terminal monitorZXROSNG#debug ipv6 tcp allAll IPv6 TCP debugging has been turned on关闭TCP6所有的debug开关，则输入以下命令：ZXROSNG#debug ipv6 tcp allAll IPv6 TCP debugging has been turned on打开TCP6所有打印开关后，输出的信息参见debug ipv6 tcp packet、debug ipv6 tcp driver、debug ipv6 tcp transactions这三个命令的输出信息。





相关命令 :

terminal monitor    show debug tcp6




## debug ipv6 tcp driver 


debug ipv6 tcp driver 




命令功能 :

该命令工作于特权模式，用于开启TCP6控制信息的打印开关。当需要查看TCP6连接建链和关闭等控制事件信息时，使用该命令。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 tcp driver 
 

no debug ipv6 tcp driver 








命令参数解释 :


					无
				 






缺省 :

关闭该调试功能 






使用说明 :

使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面TCP6控制事件信息。打印的信息包括TCP6连接主动建链成功信息、被动建链成功信息、启动SYNWAIT超时定时器信息、正常关闭TCP6连接的信息、异常终止TCP6连接的信息。可使用no debug ipv6 tcp driver、no debug ipv6 tcp all或者no debug all命令关闭该debug开关。为了避免该类debug信息的循环打印，TELNET应用对应TCP6连接的控制信息不予打印。





范例 :

打开TCP6控制信息的debug开关，则输入以下命令：ZXROSNG#terminal monitor ZXROSNG#debug ipv6 tcp driver IPv6 TCP driver events debugging is on关闭TCP6控制信息的debug开关，则输入以下命令：ZXROSNG#no debug ipv6 tcp driver IPv6 TCP driver events debugging is off在打开TCP6控制信息的debug开关后，OAM界面会显示TCP6控制事件的详细信息，如下：ZXR10 MPU-0/20/0 2014-7-1 03:09:47 IPv6 TCB[6148]: Passive open 12::1:179<--12::2:50002 OK输出信息中的参数信息解释如下：参数名称                                           参数说明ZXR10                                              设备系列MPU-0/20/0                                         产生该打印信息的单板及槽位信息2014-7-1 03:09:47                                  产生该打印的时间TCB[6148]: Passive open 12::1:179<--12::2:50002 OK 索引号为6148，本端地址为12::1，本端端口为179，远端地址为12::2，远端端口为50002的TCP6连接被动建立。





相关命令 :

terminal monitor    show debug tcp6




## debug ipv6 tcp packet 


debug ipv6 tcp packet 




命令功能 :

该命令工作于特权模式，用于开启TCP6收发报文的打印开关。当需要查看TCP6连接报文收发情况时，使用该命令。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 tcp packet 
  [port 
 ＜port-num 
＞] [address 
 ＜ipv6-address 
＞]

no debug ipv6 tcp packet 








命令参数解释 :



参数|描述
---|---
＜port-num＞|指定端口号（源端口或目的端口）
＜ipv6-address＞|指定IPv6地址（源地址或目的地址）








缺省 :

关闭该调试功能 






使用说明 :

使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面打印报文收发信息。可使用no debug ipv6 tcp packet、no debug ipv6 tcp all或者no debug all命令关闭该debug开关。为了避免报文收发debug信息的循环打印，TELNET应用对应TCP6连接的报文收发情况不予打印。





范例 :

打开TCP6报文收发的debug开关，则输入以下命令：ZXROSNG#terminal monitor ZXROSNG#debug ipv6 tcp packet IPv6 TCP packets debugging is on关闭TCP6报文收发的debug开关，则输入以下命令：ZXROSNG#no debug ipv6 tcp packet                                                   IPv6 TCP packet debugging is off在打开TCP6报文收发的debug开关后，OAM界面会显示TCP6报文收发的详细信息，如下：ZXROSNG#ZXR10 MPU-0/20/0 2014-7-1 02:54:35 IPv6 TCB[6148]: O ESTAB 12::1:40053-->12::2:179 seq 1571343317 DATA 19 ACK 1774910855 <ACK><PSH>  WIN 33120ZXR10 MPU-0/20/0 2014-7-1 02:54:35 IPv6 TCB[6148]: I ESTAB 12::1:40053<--12::2:179 seq 1774910855 ACK 1571343336 <ACK>  WIN 33120ZXR10 MPU-0/20/0 2014-7-1 02:54:49 IPv6 TCB[6148]: I ESTAB 12::1:40053<--12::2:179 seq 1774910855 DATA 19 ACK 1571343336 <ACK><PSH>  WIN 33120ZXR10 MPU-0/20/0 2014-7-1 02:54:49 IPv6 TCB[6148]: O ESTAB 12::1:40053-->12::2:179 seq 1571343336 ACK 1774910874 <ACK>  WIN 33120输出信息中的参数信息解释如下：参数名称                        参数说明ZXR10                           设备系列MPU-0/20/0                      产生该打印信息的单板及槽位信息2014-7-1 02:54:35               产生该打印的时间TCB[6148]                       TCP6连接在本地的索引信息，6148为索引值，可通过show tcp6 brief命令查看到O                               表示TCP6发送的报文：OUTI                               表示TCP6接收的报文：INESTAB                           表示TCP6连接状态，当前处于ESTAB状态，TCP6连接的状态包括LISTEN、SYNSENT、SYNRCVD、ESTAB、FINWAIT-1、FINWAIT-2、CLOSEWAIT、CLOSING、LASTACK、TIMEWAIT、CLOSED等等，具体参见RFC79312::1:40053-->12::2:179    12::1   表示TCP6连接本端地址，40053为本端端口，12::2为远端地址，179为远端端口；右向箭头表示报文的方向从12::1发送至12::2，左向箭头表示报文的发送方向从12::2发送至12::1seq                             TCP6发送报文的序列号DATA                            TCP6报文中携带的数据长度ACK                             TCP6发送报文的确认号<ACK><PSH>                      TCP6发送报文的标记位，TCP6报文头部的标记未有<ACK><PSH><SYN><FIN><RST><URG>，具体参见RFC793第3.1节WIN                             TCP6发送报文中携带的接收窗口大小






相关命令 :

terminal monitor    show debug tcp6




## debug ipv6 tcp transactions 


debug ipv6 tcp transactions 




命令功能 :

该命令工作于特权模式，用于开启TCP6重要处理信息的打印开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 tcp transactions 
 

no debug ipv6 tcp transactions 








命令参数解释 :


					无
				 






缺省 :

关闭该调试功能 






使用说明 :

使用该命令，需要先开启terminal monitor命令（参见操作命令terminal monitor），否则无法在OAM界面TCP6控制事件信息。打印的重要处理信息包括TCP6状态迁移、TCP6重传信息、TCP6建链信息、TCP6连接清除信息。可使用no debug ipv6 tcp transactions、no debug ipv6 tcp all或者no debug all命令关闭该debug开关。为了避免该类debug信息的循环打印，TELNET应用对应TCP6连接的重要处理信息不予打印。





范例 :

打开TCP6重要处理信息的debug开关，则输入以下命令：ZXROSNG#terminal monitor ZXROSNG#debug ipv6 tcp transactions IPv6 TCP special events debugging is on关闭TCP6重要处理信息的debug开关，则输入以下命令：ZXROSNG#no debug ipv6 tcp transactions                                                   IPv6 TCP special events debugging is off在打开TCP6重要处理信息的debug开关后，OAM界面会显示信息如下：ZXROSNG#ZXR10 MPU-0/20/0 2014-7-1 03:16:57 IPv6 TCB[6148]: start retransmit timer in 3输出信息中的参数信息解释如下：参数名称                                       参数说明ZXR10                                          设备系列MPU-0/20/0                                     产生该打印信息的单板及槽位信息2014-7-1 03:16:57                              产生该打印信息的时间IPv6 TCB[6148]: start retransmit timer in 3    索引号为6148的TCP6连接开启重传定时器





相关命令 :

terminal monitor    show debug tcp6




## debug ipv6 udp 


debug ipv6 udp 




命令功能 :

该命令工作于特权模式，用于开启UDP6收发报文的打印开关。当需要查看UDP6报文收发情况时，使用该命令。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ipv6 udp 
 

no debug ipv6 udp 








命令参数解释 :


					无
				 






缺省 :

关闭该调试功能 






使用说明 :

该命令需要伴随terminal monitor命令使用（参见操作命令terminal monitor），否则无法在OAM界面打印报文收发信息。可使用no debug ipv6 udp或者no debug all命令关闭该debug开关。





范例 :

打开UDP6报文收发的debug开关，则输入以下命令：ZXROSNG#terminal monitor ZXROSNG#debug ipv6 udp IPv6 UDP debugging is on关闭UDP6报文收发的debug开关，则输入以下命令：ZXROSNG#no debug ipv6 udp                                                   IPv6  UDP packet debugging is off在打开UDP报文收发的debug开关后，OAM界面会显示UDP报文收发的详细信息，如下：ZXROSNG#ZXR10 MPU-0/20/0 2014-7-1 03:42:56   IPv6 UDP: send src=fe80::2ee:ffff:fe10:1000(646),                          dst=ff02::2(646), len=62                                                    输出信息中的参数信息解释如下：参数名称          参数说明ZXR10             设备系列MPU-0/20/0        产生该打印信息的单板及槽位信息2014-7-1 03:42:56 产生该打印信息的时间IPv6 UDP          表示是UDP6模块的debug打印信息send              表示UDP6模块发送的报文rcvd              表示UDP6模块接收的报文src=1.1.1.1(123)  UDP6本端IP地址为fe80::2ee:ffff:fe10:1000，本端端口号为646dst=1.1.1.2(123)  UDP6远端IP地址为1.1.1.1，远端端口号为646len=62            UDP6报文长度（包括UDP6头）






相关命令 :

terminal monitor    show debug udp6




## ipv6 tcp finwait-time 


ipv6 tcp finwait-time 




命令功能 :

该命令工作于全局配置模式，用于设置TCP6 FINWAIT-2超时时间。配置成功后，当系统关闭TCP6连接时，TCP6连接处于FINWAIT-2状态的超时时间为该设置值，超过该超时时间而没有收到对方回应的FIN报文，本端TCP6将强行关闭该TCP6连接。TCP6 FINWAIT-2状态为TCP6主动关闭一方可能经过的一个中间状态，处于该状态下的TCP6连接等待对端发送FIN报文，如果等待一段时间本端依然没有接收到对端的FIN报文，本端TCP6将强行关闭该TCP6连接，所等待的时间就是本条命令配置的时间。TCP6状态迁移及FINWAIT-2状态介绍参见RFC793第3.2节。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 tcp finwait-time 
  ＜seconds 
＞

no ipv6 tcp finwait-time 








命令参数解释 :



参数|描述
---|---
＜seconds＞|关闭TCP连接的时长，单位：秒，范围300-675，缺省为675秒








缺省 :

关闭一个tcp连接的等待时间为675秒 






使用说明 :

TCP6 FINWAIT-2超时时间默认值是675秒，拥有管理员权限的操作员可以使用这条命令变更TCP6 FINWAIT-2超时时间。配置变更后，TCP6 FINWAIT-2超时时间只对新进入FINWAIT-2状态的TCP6连接生效，之前已经处于FINWAIT-2状态的TCP6连接的超时时间不会变化。





范例 :

设置TCP6 FINWAIT-2超时时间为300秒，则输入以下命令：ZXROSNG(config)# ipv6 tcp finwait-time 300去除设置TCP6 FINWAIT-2超时时间，恢复为默认值675秒，则输入以下命令：ZXROSNG(config)# no ipv6 tcp finwait-time





相关命令 :

show tcp6 config 




## ipv6 tcp queuemax 


ipv6 tcp queuemax 




命令功能 :

该命令工作于全局配置模式，用于设置TCP6输出报文最大队列长度。当需要提高TCP6传输性能，可以使用该命令设置输出报文最大队列长度。配置成功后，新建立的TCP6连接的输出报文最大队列长度为该配置值。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 tcp queuemax 
  ＜packets 
＞

no ipv6 tcp queuemax 








命令参数解释 :



参数|描述
---|---
＜packets＞|TCP最大输出队列长度，单位：包，范围5-50，缺省为5个








缺省 :

TCP6连接最大输出队列为5个包 






使用说明 :

TCP6 最大输出队列长度默认值是50，拥有管理员权限的操作员可以使用这条命令变更TCP6最大输出队列长度，以调整TCP6连接的传输能力。配置变更后，TCP6最大输出队列长度只对新建的TCP6连接生效，正在建链或者已经建链成功的TCP6连接不会改变接收窗口值。





范例 :

设置TCP6输出报文最大队列长度为50个，则输入以下命令：ZXROSNG(config)# ipv6 tcp queuemax 50去除设置TCP6输出报文最大队列长度，恢复为默认值5，则输入以下命令：ZXROSNG(config)# no ipv6 tcp queuemax





相关命令 :

show tcp6 config 




## ipv6 tcp synwait-time 


ipv6 tcp synwait-time 




命令功能 :

该命令工作于全局配置模式，用于设置TCP6 SYNWAIT超时时间。配置成功后，当系统发起TCP6建链请求，TCP6连接处于SYNSENT状态的时间超过该设置的超时时间而没有收到对方回应的SYN+ACK报文，本端TCP6将强行关闭该TCP6连接；或者当系统被动响应TCP6建链请求，TCP6连接处于SYNRCVD状态的时间超过该设置的超时时间而没有收到对方回应的ACK报文，本端TCP6将强行关闭该TCP6连接。TCP6 SYNWAIT超时时间用于控制TCP6三次握手的超时时间，超过该设置时间而没有完成三次握手过程的将强行关闭处于半连接状态(SYNSENT和SYNRCVD)的TCP6连接。TCP6状态迁移及SYNSENT、SYNRCVD状态介绍参见RFC793第3.2节。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 tcp synwait-time 
  ＜seconds 
＞

no ipv6 tcp synwait-time 








命令参数解释 :



参数|描述
---|---
＜seconds＞|TCP连接时间，单位：秒，范围30-80，缺省为75秒








缺省 :

建立tcp连接的等待时间为75秒 






使用说明 :

TCP6 SYNWAIT超时时间默认值是75秒，拥有管理员权限的操作员可以使用这条命令变更TCP6 SYNWAIT超时时间。配置变更后，TCP6 SYNWAIT超时时间只对新进入SYNSENT和SYNRCVD状态的TCP6半连接生效，之前已经处于SYNSENT或SYNRCVD状态的TCP6半连接的超时时间不会变化，依然使用配置前的超时时间。





范例 :

设置TCP6 SYNWAIT超时时间为60秒，则输入以下命令：ZXROSNG(config)# ipv6 tcp synwait-time 60去除设置TCP6 SYNWAIT超时时间，恢复为默认值75秒，则输入以下命令：ZXROSNG(config)# no ipv6 tcp synwait-time





相关命令 :

show tcp6 config 




## ipv6 tcp window-size 


ipv6 tcp window-size 




命令功能 :

该命令工作于全局配置模式，用于设置TCP6接收窗口的大小。当需要提高TCP6传输性能，可以使用该命令设置较大的接收窗口。配置成功后，新建立的TCP6连接的接收窗口为该配置值，并在SYN报文中通告给TCP6连接的对端。TCP6接收窗口实现TCP6的流量控制，TCP6通过在交互报文中携带的接收窗口字段，通告TCP6连接的对端：本端的接收能力。TCP6连接的对端不能发送超过本端接收窗口大小的报文。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 tcp window-size 
  ＜bytes 
＞

no ipv6 tcp window-size 








命令参数解释 :



参数|描述
---|---
＜bytes＞|TCP侦听方窗口大小，单位：字节，范围100-1048560，缺省为32768字节








缺省 :

tcp连接的侦听方窗口为32768字节 






使用说明 :

TCP6 接收窗口默认值是32768字节，拥有管理员权限的操作员可以使用这条命令变更TCP6接收窗口大小，以调整TCP6连接的传输能力。配置变更后，TCP6接收窗口只对新建的TCP6连接生效，正在建链或者已经建链成功的TCP6连接不会改变接收窗口值。





范例 :

设置TCP6 接收窗口为65535字节，则输入以下命令：ZXROSNG(config)# ipv6 tcp window-size 65535去除设置TCP6 接收窗口，恢复为默认值32768字节，则输入以下命令：ZXROSNG(config)# no ipv6 tcp window-size





相关命令 :

show tcp6 config 




## show debug tcp6 


show debug tcp6 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于显示系统中TCP6 debug的开启情况 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug tcp6 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

当需要显示当前系统的TCP6 debug开启情况时，使用该命令。 






范例 :

通过show命令显示系统TCP6 debug开启情况，则输入以下命令：ZXROSNG#show debug tcp6   IPv6 TCP:  IPv6 TCP driver events debugging is on  IPv6 TCP packets debugging is on  IPv6 TCP special events debugging is on    输出信息中的参数信息解释如下：参数名称   参数说明IPV6 TCP   表示显示的是TCP6模块的debug信息IPV6 TCP   driver event debugging is on    TCP6控制信息debug开关（参见操作命令debug ipv6 tcp driver）打开IPV6 TCP   packet debugging is on    TCP6报文收发debug开关（参见操作命令debug ipv6 tcp packet）打开IPv6 TCP   special events debugging is on    TCP6重要处理信息debug开关（参见操作命令debug ipv6 tcp transactions）打开






相关命令 :

debug ipv6 tcp alldebug ipv6 tcp driverdebug ipv6 tcp packetdebug ipv6 tcp transactions




## show debug udp6 


show debug udp6 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于显示系统中UDP6 debug的开启情况。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug udp6 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

通过show命令显示系统UDP6 debug开启情况，则输入以下命令：show debug udp6IPv6 UDP:  IPv6 UDP packet debugging is on    输出信息中的参数信息解释如下：参数名称                         参数说明UDP6                             表示显示的是UDP6模块的debug信息IPv6 UDP packet debugging is on  UDP6报文收发debug开关（参见操作命令debug ipv6 udp）打开






相关命令 :

debug ipv6 udp 




## show tcp6 brief 


show tcp6 brief 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于显示系统中所有TCP6连接的简要信息，包括本地地址和端口、远端地址和端口、TCP6连接状态等信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show tcp6 brief 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

通过show命令显示系统所有TCP6连接简要信息，则输入以下命令：ZXROSNG(config)#sho tcp6 briefTCB Index     Local Address             Foreign Address           State12295         3::1:50053                3::2:179                  ESTAB6148          12::1:40053               12::2:179                 ESTAB3075          12::1:646                 12::2:53063               ESTAB输出信息中的参数信息解释如下：参数名称        参数说明TCB Index       TCP6连接在本地的索引值Local Address   TCP6连接本端地址和端口号，中间用分号隔开Foreign Address TCP6连接远端地址和端口号，中间用分号隔开State           TCP6连接状态，包括LISTEN、SYNSENT、SYNRCVD、ESTAB、FINWAIT-1、FINWAIT-2、CLOSEWAIT、CLOSING、LASTACK、TIMEWAIT、CLOSED等等，具体参见RFC793第3.2节






相关命令 :

无 




## show tcp6 config 


show tcp6 config 




命令功能 :

该命令除用户模式外的其他所有模式，用于显示系统TCP6的配置信息，包括FINWAIT-2老化时间配置（参见配置命令ipv6 tcp finwait-time）、SYNWAIT老化时间配置（参见配置命令ipv6 tcp synwait-time）、接收窗口配置（参见配置命令ipv6 tcp window-size）。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show tcp6 config 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于显示系统TCP6的配置信息，当未配置数据时，显示系统默认值。 






范例 :

通过show命令显示系统TCP6配置信息，则输入以下命令：ZXROSNG(config)#ipv6 tcp finwait-time 300ZXROSNG(config)#ipv6 tcp synwait-time 40ZXROSNG(config)#ipv6 tcp window-size 65535ZXROSNG(config)#show tcp6 config IPv6 TCP SYNWAIT:          40IPv6 TCP FINWAIT:          300IPv6 TCP QUEUEMAX         5IPv6 TCP WINDOWSIZE:     65535输出信息中的参数信息解释如下：参数名称            参数说明IPv6 TCP SYNWAIT    ipv6 tcp synwait-time配置值，未配置时默认为75秒IPv6 TCP FINWAIT    ipv6 tcp finwait-time配置值，未配置时默认为675秒IPv6 TCP WINDOWSIZE ipv6 tcp window-size配置值，未配置时默认为32768IPv6 TCP QUEUEMAX   ipv6 tcp queue-max配置值，未配置时默认为5






相关命令 :

ipv6 tcp finwait-time ＜wait-time＞ipv6 tcp window-size ＜wait-size＞ipv6 tcp synwait-time ＜wait-time＞ipv6 tcp queuemax ＜packet-numbers＞




## show tcp6 statistics 


show tcp6 statistics 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于显示系统TCP6统计信息，包括收发报文信息、连接建立情况等统计信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show tcp6 statistics 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

通过show命令显示系统TCP6统计信息，则输入如下命令：ZXROSNG#show tcp6 statistics Rcvd: 8479 Total      0 checksum error, 0 bad offset, 0 too short      4398 packets (82532 bytes) in sequence      5 dup packets (38 bytes)      1 partially dup packets (19 bytes)      7 out-of-order packets (76 bytes)      0 packets (0 bytes) with data after window      0 packets after close      0 window probe packets, 0 window update packets      12 dup ack packets, 0 ack packets with unsend data      4378 ack packets (82167 bytes)Sent: 8768 Total      22 control packets (including 26 retransmitted)       4374 data packets (82161 bytes)      26 data packets (265 bytes) retransmitted      4359 ack only packets (4340 delayed)      0 window probe packets, 0 window update packets4 Connections initiated, 3 connections accepted, 6 connections established7 Connections closed (including 3 dropped, 0 embryonic dropped)24 Total rxmt timeout, 0 connections dropped in rxmt timeout1 Keepalive timeout, 0 keepalive probe, 1 connections dropped in keepalive输出信息中的参数信息解释如下：参数名称                                 参数说明Rcvd                                     TCP6接收报文统计情况Total                                    TCP6接收报文总数checksum error                           TCP6接收校验和错误的报文个数bad offset                               TCP6接收包头长度错误的报文个数too short                                TCP6接收长度错误的报文个数packets (bytes) in sequence              TCP6接收符合预期序列号报文个数以及对应的字节数，例如4398 packets (82532 bytes) in sequence，表示TCP6接收符合预期序列号报文4398个，对应的字节数为82532 bytes。dup packets                              接收到重传的报文个数，例如1 dup packets (0 bytes)，表示有一个重传报文，对应字节数是0.partially dup packets                    接收到部分重传数据的报文个数，例如0 partially dup packets (0 bytes)，表示有一个重传报文，对应字节数是0.out-of-order packets(bytes)              TCP6接收失序的报文个数以及对应的字节数，例如1 out-of-order packets (0 bytes)，表示TCP6接收失序的报文个数为1，对应的字节数为0。packets (bytes) with data after window   TCP6接收序列号在接收窗口之外的报文个数以及对应的字节数，例如0 packets (0 bytes) with data after window，表示TCP6接收序列号在接收窗口之外的报文个数为0个，对应的字节数为0。packets after close                      TCP6处于CLOSED状态接收的报文个数window probe packets                     TCP6接收的窗口探测报文个数window update packets                    TCP6接收的窗口更新报文个数dup ack packets                          TCP6接收的重复ACK个数ack packets with unsend data             TCP6接收的未发送数据的ACK报文个数ack packets ( bytes)                     TCP6接收的ACK报文个数以及确认的字节数，例如361 ack packets (6881 bytes)，表示TCP6接收到ack确认报文361个，确认6881个字节。Sent                                     TCP6发送报文统计情况Total                                    TCP6发送的报文总个数control packets(including retransmitted) TCP6发送的控制报文个数（包括SYN、FIN、RST），包含重传的控制报文个数。例如2 control packets (including 6 retransmitted)，表示TCP6发送的控制报文2个，重传的控制报文个数为6个。data packets (bytes)                     TCP6发送的携带数据的报文个数以及对应的字节数，例如359 data packets (6878 bytes)，表示TCP6发送鞋带数据的报文个数359个，携带的字节数为6878 bytes。data packets (bytes)retransmitted        TCP6重传的数据报文个数以及对应的字节数，例如6 data packets (63 bytes) retransmitted，表示TCP6重传的数据报文个数为6，重传字节数为63 bytes。ack only packets(delayed)                TCP6发送的纯ACK报文个数以及延时确认的ACK报文个数，例如303 ack only packets (299 delayed)，表示TCP6发送的纯ACK报文个数为303个，延时确认的ACK报文个数为299个。window probe packets                     TCP6发送的窗口探测报文个数window update packets                    TCP6发送的窗口更新报文个数Connections initiated                    TCP6主动建链的连接个数connections accepted                     TCP6被动建链的连接个数Connections established                  TCP6建链成功的连接个数connections closed                       TCP6关闭的连接个数dropped                                  关闭的连接数embryonic dropped                        关闭未建立的连接数Total rxmt timeout                       TCP6重传的次数connections dropped in rxmt timeout     TCP6 因为重传超时关闭的连接个数Keepalive timeout                     TCP6 Keepalive超时次数keepalive probe                          TCP6 Keepalive探测次数Connections dropped in keepalive         TCP6因为Keepalive探测失败而关闭的连接个数






相关命令 :

无 




## show tcp6 tcb 


show tcp6 tcb 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于显示系统中指定TCP6的连接信息，包括本地地址和端口、远端地址和端口、TCP6连接状态、序列号和确认号、收发报文个数等信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show tcp6 tcb 
  ＜tcb-index 
＞ 







命令参数解释 :



参数|描述
---|---
＜tcb-index＞|TCB索引，取值范围为1-4294967295








缺省 :

无 






使用说明 :

可以先通过show tcp6 brief 查看需要显示的tcp连接的tcb索引 






范例 :

首先通过show tcp6 brief命令显示系统所有TCP6连接简要信息，再根据show tcp6 brief显示出的TCP6索引号显示指定TCP6连接的信息，输入命令如下：ZXROSNG#show tcp6 briefTCB Index     Local Address             Foreign Address           State12295         3::1:50053                3::2:179                  ESTAB6148          12::1:40053               12::2:179                 ESTAB3075          12::1:646                 12::2:53063               ESTABZXROSNG#show tcp6 tcb 3075Connection state is ESTABLocal host: 12::1, Local port: 646 Foreign host: 12::2, Foreign port: 53063iss: 1557366682  snduna: 1557373099  sndnxt: 1557373099  sndwnd: 33120irs: 1756868648  rcvnxt: 1756875075  rcvwnd: 33120  SRTT: 7 ms, RTTO:  3 ms, RTV: 3 msminRTT: 2 ms,  maxRTT: 128 ms,  ACK hold: 200 ms输出信息中的参数信息解释如下：参数名称                       参数说明Connection state is ESTAB      TCP6连接状态，包括LISTEN、SYNSENT、SYNRCVD、ESTAB、FINWAIT-1、FINWAIT-2、CLOSEWAIT、CLOSING、LASTACK、TIMEWAIT、CLOSED等等，具体参见RFC793第3.2节Local host                     TCP6连接本端地址Local port                     TCP6连接本端端口Foreign host                   TCP6连接远端地址Foreign port                   TCP6连接远端端口iss    TCP6                       发送初始序列号（Initial send sequence number）snduna                         TCP6发送并且得到对方ACK确认的序列号（Last send sequence number that the local host sent but has not received an acknowledgment for）sndnxt                         TCP6下次发送新数据的序列号（Sequence number the local host will send next）sndwnd                         TCP6发送窗口值，表示TCP能发送的最大字节数irs                            TCP6接收初始序列号（Initial receive sequence number）rcvnxt                         TCP6接收并且已经确认的序列号（Last receive sequence number that the local host has acknowledged）rcvwnd                         TCP6本端接收窗口大小，可通过配置命令ipv6 tcp window-size配置其最大值SRTT                           TCP6报文传输的平滑往返时间（SRTT：Smoothed Round-Trip Timeout）RTTO                           TCP6报文传输的往返时间，用于重传定时器设置重传超时时间（RTTO：Round-Trip Timeout）RTV                            记录TCP6上次重传的超时时间minRTT                         TCP6计算得到的往返时间最小值maxRTT                         TCP6计算得到的往返时间最大值ACK hold                       延时ACK的延时等待时间






相关命令 :

show tcp6 brief 




