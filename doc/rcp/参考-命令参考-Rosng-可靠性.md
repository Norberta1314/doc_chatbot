# BFD配置命令 
## backpath-check exclude 


backpath-check exclude 




命令功能 :

当使能或者去使能来回路径一致检测后，某些隧道不希望通过使能或者是去使能开关对其产生作用时，可以通过该命令选择不收使能或者是去使能开关的影响 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :


backpath-check exclude 
 tunnel-id 
 ＜tunnel-id 
＞
no backpath-check exclude 
 tunnel-id 
 ＜tunnel-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜tunnel-id＞|不受使能或者去使能来回路径检测一致开关影响的隧道ID，范围:1-$#100794374#$








缺省 :

无 






使用说明 :

当使能或者去使能开关打开后，某些隧道不希望来回路径检测一致开关影响，选择不收使能或者去使能来回路径检测一致开关的隧道 






范例 :

ZXROSNG(config-bfd)#backpath-check exclude tunnel-id 1 






相关命令 :

无 




## backpath-check 


backpath-check 




命令功能 :

使能或者是去使能RSVP BFD实例来回路径检测一致功能 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



backpath-check 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能RSVP BFD来回检测路径一致功能
disable|去使能RSVP BFD来回检测路径一致功能








缺省 :

disable 






使用说明 :

该命令在BFD模式下配置使能或者去使能BFD来回路径检测一致功能 






范例 :

ZXROSNG(config-bfd)#backpath-check enableZXROSNG(config-bfd)#backpath-check disable





相关命令 :

无 




## bfd 


bfd 




命令功能 :

进入BFD配置模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



bfd 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该配置命令用于进入BFD配置模式。 






范例 :

ZXROSNG(config)#bfdZXROSNG(config-bfd)#






相关命令 :

show running-config bfd 




## cv-stop 


cv-stop 




命令功能 :

配置BFD会话TRACK方式。 






命令模式 :

 L2-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



cv-stop 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启CV-Stop跟踪模式
disable|关闭CV-Stop跟踪模式








缺省 :

disable 






使用说明 :

该配置命令用于修改track bfd时，bfd会话传递远端状态的规则，是传递diag变化还是直接使会话down。 






范例 :

ZXROSNG(config-bfd)#session pw pw-bfd pw-name pw1ZXROSNG(config-bfd-pw-pw)#cv-stop enableZXROSNG(config-bfd-pw-pw)#





相关命令 :

show running-config bfdshow bfd neighbor pw detail




## cv-stop 


cv-stop 




命令功能 :

配置BFD会话track类型。 






命令模式 :

 LDP-BFD实例模式,LINK-BFD实例模式,PEER-BFD实例模式,PW-BFD实例模式,RSVP-BFD实例模式  






命令默认权限级别 :

LINK-BFD实例模式:15,PEER-BFD实例模式:15,LDP-BFD实例模式:15,RSVP-BFD实例模式:15,PW-BFD实例模式:15 






命令格式 :



cv-stop 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启CV-Stop跟踪模式
disable|关闭CV-Stop跟踪模式








缺省 :

disable 






使用说明 :

该配置命令用于修改track bfd时，bfd会话传递远端状态的规则，是传递diag变化还是直接使会话down。 






范例 :

ZXROSNG(config-bfd)#session pw pw-bfd pw-name pw1ZXROSNG(config-bfd-pw-pw)#cv-stop enableZXROSNG(config-bfd-pw-pw)#





相关命令 :

show running-config bfdshow bfd neighbor pw detail




## dampen 


dampen 




命令功能 :

使能BFD会话阻尼功能或者修改BFD会话阻尼参数 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :


dampen 
  {ip-bfd 
|ldp-bfd 
|tunnel-bfd 
|tunnel-lsp-bfd 
|l2-bfd 
|pw-bfd 
} [{[half-life 
 ＜half life period 
＞],[reuse 
 ＜reuse 
＞],[suppress 
 ＜suppress 
＞],[max-suppress-time 
 ＜max suppress time 
＞]}]
no dampen 
  {ip-bfd 
|ldp-bfd 
|tunnel-bfd 
|tunnel-lsp-bfd 
|l2-bfd 
|pw-bfd 
}
				






命令参数解释 :



参数|描述
---|---
ip-bfd|去使能ip-bfd类型会话阻尼功能
ldp-bfd|去使能ldp-bfd类型会话阻尼功能
tunnel-bfd|去使能tunnel-bfd类型会话阻尼功能
tunnel-lsp-bfd|去使能tunnel-lsp-bfd类型会话阻尼功能
l2-bfd|去使能l2-bfd类型会话阻尼功能
pw-bfd|去使能pw-bfd类型会话阻尼功能
＜half life period＞|BFD会话阻尼半衰期，范围1-$#35389454#$
＜reuse＞|BFD会话阻尼可重用阀值，范围1-$#35389457#$
＜suppress＞|BFD会话阻尼抑制值，范围1-$#35389460#$
＜max suppress time＞|BFD会话阻尼抑制值，范围1-$#35389463#$








缺省 :

无 






使用说明 :

该命令可以使能BFD会话阻尼功能或者设置不同BFD会话类型的阻尼参数信息。该命令必须在BFD模式配置。 






范例 :

ZXROSNG(config-bfd)#dampen ip-bfd half-life 2000 max-suppress-time 15000 reuse 3000 suppress 5000 






相关命令 :

show bfd dampen-parameters 




## debug bfd all 


debug bfd all 




命令功能 :

该命令用于打开BFD会话所有诊断开关。当BFD建链或检测过程中发生异常时，如果想查看BFD所有诊断信息，可以使用该命令。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug bfd all 
 

no debug bfd all 








命令参数解释 :


					无
				 






缺省 :

关闭 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令工作在特权模式下。打开该诊断开关后，所有BFD会话所有诊断将输出该用户。当BFD会话较多时，可能会占用较多的CPU资源。在打开该诊断开关之前，用户需要根据BFD 会话的数量，来评估打开该诊断开关对系统的影响。在非故障的情况下，建议不要打开该开关。用户可以通过ctrl+d 组合键来关闭该诊断开关。





范例 :

ZXROSNG#debug bfd allAll BFD debugging has been turned onZXR10 PFU-0/20/0 2011-4-26 05:05:19 BFD: [IN: INIT] localAddr: 100.0.0.25; peerAddr: 100.0.0.15; ver: 1; diag: 0; P/F/C/A/D/M: 0/0/0/0/0/0; mult: 3; len: 24; LD/RD: 4097/4097;tx: 4797; rx: 50ZXR10 PFU-0/20/0 2011-4-26 05:05:19 BFD: IN,20 80 03 18 00 00 10 01 00 00 10 01 00 49 32 48 00 00 C3 50 00 00 00 00 ZXR10 PFU-0/20/0 2011-4-26 05:05:20 BFD: [OUT: UP] src:100.0.0.15; dst:100.0.0.25; ver: 1; diag: 0; P/F/C/A/D/M: 0/0/0/0/0/0 ; mult: 3; len: 24; LD/RD: 4097/4097;tx: 4347; rx: 50ZXR10 PFU-0/20/0 2011-4-26 05:05:20 BFD: OUT,20 C0 03 18 00 00 10 01 00 00 10 01 00 42 54 78 00 00 C3 50 00 00 00 00 ZXR10 PFU-0/20/0 2011-4-26 05:05:20 BFD: IP: [100.0.0.15/100.0.0.25]LD/RD: 4097/4097 StateChg: DOWN-->UP, Diag: 0ZXR10 PFU-0/20/0 2011-4-26 05:05:20 BFD: [IN: UP] localAddr: 100.0.0.25; peerAddr: 100.0.0.15; ver: 1; diag: 0; P/F/C/A/D/M: 1/0/0/0/0/0; mult: 3; len: 24; LD/RD: 4097/4097;tx: 50; rx: 50ZXR10 PFU-0/20/0 2011-4-26 05:05:20 BFD: IN,20 E0 03 18 00 00 10 01 00 00 10 01 00 00 C3 50 00 00 C3 50 00 00 00 00






相关命令 :

show debug bfd 




## debug bfd byte 


debug bfd byte 




命令功能 :

该命令用于打开BFD会话报文诊断开关。当BFD建链过程中发生异常时，用户可以通过该命令打开BFD报文开关，来查看BFD建链过程中报文交互过程。当该开关打开时，BFD建链报文将以字节的形式呈现给用户。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug bfd byte 
  [ {ld 
 ＜local-discriminator 
＞|peer 
 {＜peer-IPv4-address 
＞|＜peer-IPv6-address 
＞}|tunnel-id 
 ＜tunnel ID 
＞|pw-name 
 ＜pw-name 
＞|interface 
 ＜interface-name 
＞|vrf 
 ＜vrf-name 
＞} {on 
|off 
}]
no debug bfd byte 
  [{ld 
 ＜local-discriminator 
＞|peer 
 {＜peer-IPv4-address 
＞|＜peer-IPv6-address 
＞}|tunnel-id 
 ＜tunnel ID 
＞|pw-name 
 ＜pw-name 
＞|interface 
 ＜interface-name 
＞|vrf 
 ＜vrf-name 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜local-discriminator＞|会话本地标识符
＜peer-IPv4-address＞|会话远端ipv4地址
＜peer-IPv6-address＞|会话远端ipv6地址
＜tunnel ID＞|隧道实例ID，范围1-$#100794374#$
＜pw-name＞|pw实例名称
＜interface-name＞|会话出接口名称
＜vrf-name＞|vrf名称
on|开启debug
off|关闭debug








缺省 :

关闭 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。该命令工作在特权模式下。打开该诊断开关后，所有BFD会话的建链报文将以字节的形式输出该用户。当BFD会话较多时，可能会占用较多的CPU资源。在打开该诊断开关之前，用户需要根据BFD会话的数量，来评估打开该诊断开关后对系统的影响。在非故障的情况下，建议不要打开该开关。用户可以通过ctrl+d组合键来关闭该诊断开关。





范例 :

ZXROSNG#debug bfd byte BFD byte debugging has been turned onZXROSNG#ZXR10 PFU-0/20/0 2010-1-8 01:05:52 app_bfd: OUT,20 40 03 18 00 00 00 09 00 00 00 00 00 37 6B 80 00 00 C3 50 00 00 00 00






相关命令 :

show debug bfd 




## debug bfd error 


debug bfd error 




命令功能 :

该命令用于打开BFD会话建链过程中的错误诊断开关。当BFD建链过程中发生异常时，用户可以通过该命令打开BFD错误开关，来查看BFD建链过程中是否有错误的发生。当该开关打开时，如果BFD在建链过程中出现异常，将可能错误提示输出给用户。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug bfd error 
  [ {ld 
 ＜local-discriminator 
＞|peer 
 {＜peer-IPv4-address 
＞|＜peer-IPv6-address 
＞}|tunnel-id 
 ＜tunnel ID 
＞|pw-name 
 ＜pw-name 
＞|interface 
 ＜interface-name 
＞|vrf 
 ＜vrf-name 
＞} {on 
|off 
}]
no debug bfd error 
  [{ld 
 ＜local-discriminator 
＞|peer 
 {＜peer-IPv4-address 
＞|＜peer-IPv6-address 
＞}|tunnel-id 
 ＜tunnel ID 
＞|pw-name 
 ＜pw-name 
＞|interface 
 ＜interface-name 
＞|vrf 
 ＜vrf-name 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜local-discriminator＞|会话本地标识符
＜peer-IPv4-address＞|会话远端ipv4地址
＜peer-IPv6-address＞|会话远端ipv6地址
＜tunnel ID＞|隧道实例ID范围:1-$#100794374#$
＜pw-name＞|pw实例名称
＜interface-name＞|会话指定的出接口名称
＜vrf-name＞|vrf名称
on|开启debug
off|关闭debug








缺省 :

关闭 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。该命令工作在特权模式下。打开该诊断开关后，所有BFD会话的在建链过程中的错误将输出给用户。当BFD会话较多时，可能会占用较多的CPU资源。在打开该诊断开关之前，用户需要根据BFD会话的数量，来评估打开该诊断开关对系统的影响。在非故障的情况下，建议不要打开该开关。用户可以通过ctrl+d 组合键来关闭该诊断开关。





范例 :

ZXROSNG#debug bfd errorBFD error debugging has been turned onZXROSNG#debug bfd error ld 1 onBFD error debugging ld 1 on





相关命令 :

show debug bfd 




## debug bfd event 


debug bfd event 




命令功能 :

该命令用于打开BFD会话事件开关。当BFD建链或检测过程中发生异常时，用户可以通过该命令打开BFD事件开关，来查看BFD建链或检测过程中的状态迁移过程。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug bfd event 
  [ {ld 
 ＜local-discriminator 
＞|peer 
 {＜peer-IPv4-address 
＞|＜peer-IPv6-address 
＞}|tunnel-id 
 ＜tunnel ID 
＞|pw-name 
 ＜pw-name 
＞|interface 
 ＜interface-name 
＞|vrf 
 ＜vrf-name 
＞} {on 
|off 
}]
no debug bfd event 
  [{ld 
 ＜local-discriminator 
＞|peer 
 {＜peer-IPv4-address 
＞|＜peer-IPv6-address 
＞}|tunnel-id 
 ＜tunnel ID 
＞|pw-name 
 ＜pw-name 
＞|interface 
 ＜interface-name 
＞|vrf 
 ＜vrf-name 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜local-discriminator＞|会话本地标识符
＜peer-IPv4-address＞|会话远端ipv4地址
＜peer-IPv6-address＞|会话远端ipv6地址
＜tunnel ID＞|隧道实例ID范围:1-$#100794374#$
＜pw-name＞|pw实例名称
＜interface-name＞|会话指定的出接口
＜vrf-name＞|vrf名称
on|开启debug
off|关闭debug








缺省 :

关闭 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。该命令工作在特权模式下。打开该诊断开关后，所有BFD会话建链或检测过程中的事件将输出该用户。当BFD会话较多时，可能会占用较多的CPU资源。在打开该诊断开关之前，用户需要根据BFD会话的数量，来评估打开该诊断开关对系统的影响。在非故障的情况下，建议不要打开该开关。用户可以通过ctrl+d 组合键来关闭该诊断开关。





范例 :

ZXROSNG#debug bfd event BFD event debugging has been turned onZXR10 PFU-0/20/0 2010-1-1 00:06:01 app_bfd: IP: [100.0.0.15/100.0.0.20]LD/RD: 2/2 StateChg: DOWN-->UP, Diag: 0ZXR10 PFU-0/20/0 2010-1-1 00:06:16 app_bfd: IP: [100.0.0.15/100.0.0.20]LD/RD: 2/2 StateChg: UP-->DOWN, Diag: 7, Reason: [RCV_ADMINDOWN]






相关命令 :

show debug bfd 




## debug bfd packet 


debug bfd packet 




命令功能 :

该命令用于打开BFD会话报文诊断开关。当BFD建链过程中发生异常时，用户可以通过该命令打开BFD报文开关，来查看BFD建链过程中报文交互过程。当该开关打开时，BFD建链报文将以解析报文的形式呈现给用户。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug bfd packet 
  [ {ld 
 ＜local-discriminator 
＞|peer 
 {＜peer-IPv4-address 
＞|＜peer-IPv6-address 
＞}|tunnel-id 
 ＜tunnel ID 
＞|pw-name 
 ＜pw-name 
＞|interface 
 ＜interface-name 
＞|vrf 
 ＜vrf-name 
＞} {on 
|off 
}]
no debug bfd packet 
  [{ld 
 ＜local-discriminator 
＞|peer 
 {＜peer-IPv4-address 
＞|＜peer-IPv6-address 
＞}|tunnel-id 
 ＜tunnel ID 
＞|pw-name 
 ＜pw-name 
＞|interface 
 ＜interface-name 
＞|vrf 
 ＜vrf-name 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜local-discriminator＞|会话本地标识符
＜peer-IPv4-address＞|会话远端ipv4地址
＜peer-IPv6-address＞|会话远端ipv6地址
＜tunnel ID＞|隧道实例ID范围:1-$#100794374#$
＜pw-name＞|pw实例名称
＜interface-name＞|会话指定的出接口名称
＜vrf-name＞|vrf名称
on|开启debug
off|关闭debug








缺省 :

关闭 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。该命令工作在特权模式下。打开该诊断开关后，所有BFD会话的建链报文将以解析报文的形式输出该用户。当BFD会话较多时，可能会占用较多的CPU资源。在打开该诊断开关之前，用户需要根据BFD会话的数量，来评估打开该诊断开关对系统的影响。在非故障的情况下，建议不要打开该开关。用户可以通过ctrl+d组合键来关闭该诊断开关。





范例 :

ZXROSNG#debug bfd packet BFD packet debugging has been turned onZXR10 PFU-0/20/0 2010-1-8 00:50:44 app_bfd: [IN: DOWN] localAddr: 100.0.0.20; peerAddr: 127.0.0.1; ver: 1; diag: 0; P/F/C/A/D/M: 0/0/0/0/0/0; mult: 3; len: 24; LD/RD: 5/0;tx: 3310; rx: 50
ZXR10 PFU-0/20/0 2010-1-8 00:50:46 app_bfd: [OUT: DOWN] ver: 1; diag: 0; P/F/C/A/D/M: 0/0/0/0/0/0 ; mult: 3; len: 24; LD/RD: 5/0;tx: 4804; rx: 50ZXR10 PFU-0/20/0 2010-1-8 00:50:47 app_bfd: [IN: DOWN] localAddr: 100.0.0.20; peerAddr: 127.0.0.1; ver: 1; diag: 0; P/F/C/A/D/M: 0/0/0/0/0/0; mult: 3; len: 24; LD/RD: 5/0;tx: 3310; rx: 50
ZXR10 PFU-0/20/0 2010-1-8 00:50:50 app_bfd: [IN: DOWN] localAddr: 100.0.0.20; peerAddr: 127.0.0.1; ver: 1; diag: 0; P/F/C/A/D/M: 0/0/0/0/0/0; mult: 3; len: 24; LD/RD: 5/0;tx: 3310; rx: 50






相关命令 :

show debug bfd 




## default 


default 




命令功能 :

该命令用于配置BFD二层组播IP地址。当使用BFD检测链路的物理状态时，可能无法指定对端的IP地址（某些情况下，对端甚至没有IP 地址，例如SmartGroup成员链路），这时，需要将BFD会话绑定到一个组播地址，以这个组播地址为目的地址发送BFD控制报文。当需要修改二层BFD 组播地址时，使用该命令。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



default 
 destination 
 ＜multicast-ipv4-address 
＞

no default 








命令参数解释 :



参数|描述
---|---
＜multicast-ipv4-address＞|作用：配置二层BFD的目的组播IP 地址。取值范围：224.0.0.111~224.0.0.250。默认值：224.0.0.250。








缺省 :

224.0.0.250 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令在BFD配置模式下执行。配置完成后，所有的二层BFD将使用这个组播地址来发送控制报文。当多次进行配置时，BFD以最后一次配置的值为准。已经UP 的BFD会话，不受该值变化的影响。BFD会话仍以第一次配置的默认组播地址来发送报文。当BFD会话在DOWN掉后，重新协商建链时，将采用最后一次配置的组播地址来发包建链和检测。





范例 :

ZXROSNG(config-bfd)#default destination 224.0.0.120ZXROSNG(config-bfd)#






相关命令 :

show running-config bfd 




## delay-up 


delay-up 




命令功能 :

该命令用来使能延迟BFD会话UP的功能。在特殊场景中，需要BFD会话在建立并协商UP前延迟一段时间，以弥补某些应用忽视重要的前提条件（例如路由是否生成）而只根据BFD状态进行操作所带来的缺陷。本命令只影响系统中所有未创建会话的BFD配置，已创建的会话不受影响。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



delay-up 
  ＜delay time 
＞







命令参数解释 :



参数|描述
---|---
＜delay time＞|作用：指定延迟BFD会话UP的时间间隔。取值范围：1～3600，单位是秒。缺省值是0，表示会话立即UP。








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令在BFD 配置模式下执行。配置完成后，所有新创建的BFD会话将会延时发包建链。当多次进行配置时，BFD以最后一次配置的值为准。本命令只影响系统中所有未创建会话的BFD配置，已创建的会话不受影响。1)对于即将创建的BFD会话，在会话Up前会延迟用户配置的时间间隔。2)对于已经创建的BFD会话，会话状态变化时如果要再次协商Up，则会延迟用户配置的时间间隔。






范例 :

ZXROSNG#conf tEnter configuration commands, one per line.  End with CTRL/Z.ZXROSNG(config)#bfdZXROSNG(config-bfd)#delay-up 300ZXROSNG(config-bfd)#





相关命令 :

show running-config bfd 




## destination-address-check 


destination-address-check 




命令功能 :

检查所有会话的目的ip地址是否为环回口地址。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



destination-address-check 
  {disable 
|enable 
}







命令参数解释 :



参数|描述
---|---
disable|不检查目的ip地址是环回口地址
enable|检查目的ip地址是环回口地址








缺省 :

不检查目的ip地址 






使用说明 :

检查所有会话的目的ip地址是否为环回口地址。 






范例 :

ZXROSNG(config-bfd)#destination-address-check enable 






相关命令 :

show running-config bfd 




## discriminator 


discriminator 




命令功能 :

该命令用来配置静态L2-BFD的本端标识符（Local Discriminator）和远端标识符（Remote Discriminator）。当配置静态L2-BFD实例的标识符时，使用该命令。 






命令模式 :

 L2-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



discriminator 
 ld 
 ＜local-discriminator 
＞ rd 
 ＜remote-discriminator 
＞







命令参数解释 :



参数|描述
---|---
＜local-discriminator＞|会话本端标识符，范围：1-$#35389446#$
＜remote-discriminator＞|会话远端标识符，范围：1-4294967295








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。配置前，需要配置相应静态L2-BFD实例。在配置L2-BFD实例时，必须静态指定本地标识符和远端标识符，否则L2-BFD会话无法UP。当静态指定L2-BFD实例的本地标识符和远端标识符时，BFD 会话两端设备的本地标识符和远端标识符需要分别对应，即，本端的本地标识符与对端的远端标识符相同，否则会话无法正确建立。并且，本地标识符和远端标识符配置成功后不可修改。





范例 :

ZXROSNG(config-bfd-l2-l2)#discriminator ld 1 rd 1 ZXROSNG(config-bfd-l2-l2)#






相关命令 :

show running-config bfd 




## dscp 


dscp 




命令功能 :

该命令用于配置静态BFD 检测报文的DSCP（Differentiated Services Codepoint 【RFC2474】）值。当需要调整BFD检测报文的优先级时，可以用该命令。 






命令模式 :

 LINK-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



dscp 
  ＜DSCP value 
＞

no dscp 








命令参数解释 :



参数|描述
---|---
＜DSCP value＞|作用：用于设置BFD检测报文的优先级。取值范围：0-63的数字。默认值：56 。








缺省 :

缺省值为56 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。将 BFD 报文设置为高优先级报文后，优先保证 BFD 报文的转发。该命令可以在L2-BFD 模式、LINK-BFD模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在配置BFD实例的优先级前，需要配置具体的BFD 实例。





范例 :

ZXROSNG(config-bfd-link-zte)#dscp 60ZXROSNG(config-bfd-link-zte)#






相关命令 :

show running-config bfd 




## dscp 


dscp 




命令功能 :

该命令用于配置静态BFD 检测报文的DSCP（Differentiated Services Codepoint 【RFC2474】）值。当需要调整BFD检测报文的优先级时，可以用该命令。





命令模式 :

 PEER-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :


dscp 
  ＜DSCP value 
＞

no dscp 








命令参数解释 :



参数|描述
---|---
＜DSCP value＞|作用：用于设置BFD检测报文的优先级。取值范围：0-63的数字。默认值：56 。








缺省 :

缺省值为56 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。将 BFD 报文设置为高优先级报文后，优先保证 BFD 报文的转发。该命令可以在L2-BFD 模式、LINK-BFD模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在配置BFD实例的优先级前，需要配置具体的BFD 实例。





范例 :

ZXROSNG(config-bfd-peer-zte)#dscp 60ZXROSNG(config-bfd-peer-zte)#






相关命令 :

show running-config bfd 




## dscp 


dscp 




命令功能 :

该命令用于配置静态BFD 检测报文的DSCP（Differentiated Services Codepoint 【RFC2474】）值。当需要调整BFD检测报文的优先级时，可以用该命令。





命令模式 :

 LDP-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :


dscp 
  ＜DSCP value 
＞

no dscp 








命令参数解释 :



参数|描述
---|---
＜DSCP value＞|作用：用于设置BFD检测报文的优先级。取值范围：0-63的数字。默认值：56 。








缺省 :

缺省值为56 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。将 BFD 报文设置为高优先级报文后，优先保证 BFD 报文的转发。该命令可以在L2-BFD 模式、LINK-BFD模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在配置BFD实例的优先级前，需要配置具体的BFD 实例。





范例 :

ZXROSNG(config-bfd-ldp-zte)#dscp 60ZXROSNG(config-bfd-ldp-zte)#






相关命令 :

show running-config bfd 




## dscp 


dscp 




命令功能 :

该命令用于配置静态BFD 检测报文的DSCP（Differentiated Services Codepoint 【RFC2474】）值。当需要调整BFD检测报文的优先级时，可以用该命令。





命令模式 :

 RSVP-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :


dscp 
  ＜DSCP value 
＞

no dscp 








命令参数解释 :



参数|描述
---|---
＜DSCP value＞|作用：用于设置BFD检测报文的优先级。取值范围：0-63的数字。默认值：56 。








缺省 :

缺省值为56 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。将 BFD 报文设置为高优先级报文后，优先保证 BFD 报文的转发。该命令可以在L2-BFD 模式、LINK-BFD模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在配置BFD实例的优先级前，需要配置具体的BFD 实例。





范例 :

ZXROSNG(config-bfd-rsvp-zte)#dscp 60ZXROSNG(config-bfd-rsvp-zte)#






相关命令 :

show running-config bfd 




## dscp 


dscp 




命令功能 :

该命令用于配置静态BFD 检测报文的DSCP（Differentiated Services Codepoint 【RFC2474】）值。当需要调整BFD检测报文的优先级时，可以用该命令。





命令模式 :

 PW-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :


dscp 
  ＜DSCP value 
＞

no dscp 








命令参数解释 :



参数|描述
---|---
＜DSCP value＞|作用：用于设置BFD检测报文的优先级。取值范围：0-63的数字。默认值：56 。








缺省 :

缺省值为56 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。将 BFD 报文设置为高优先级报文后，优先保证 BFD 报文的转发。该命令可以在L2-BFD 模式、LINK-BFD模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在配置BFD实例的优先级前，需要配置具体的BFD 实例。





范例 :

ZXROSNG(config-bfd-pw-zte)#dscp 60ZXROSNG(config-bfd-pw-zte)#






相关命令 :

show running-config bfd 




## dscp 


dscp 




命令功能 :

该命令用于配置静态BFD 检测报文的DSCP（Differentiated Services Codepoint 【RFC2474】）值。当需要调整BFD检测报文的优先级时，可以用该命令。





命令模式 :

 L2-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :


dscp 
  ＜DSCP value 
＞

no dscp 








命令参数解释 :



参数|描述
---|---
＜DSCP value＞|作用：用于设置BFD检测报文的优先级。取值范围：0-63的数字。默认值：56 。








缺省 :

缺省值为56 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。将 BFD 报文设置为高优先级报文后，优先保证 BFD 报文的转发。该命令可以在L2-BFD 模式、LINK-BFD模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在配置BFD实例的优先级前，需要配置具体的BFD 实例。





范例 :

ZXROSNG(config-bfd-l2-zte)#dscp 60ZXROSNG(config-bfd-l2-zte)#






相关命令 :

show running-config bfd 




## echo source ipv4 


echo source ipv4 




命令功能 :

配置单臂回声BFD的IPv4源地址。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



echo source ipv4 
  ＜specify ipv4 address 
＞

no echo source ipv4 








命令参数解释 :



参数|描述
---|---
＜specify ipv4 address＞|ECHO BFD会话的IPv4源地址








缺省 :

无 






使用说明 :

用于配置ECHO BFD的源地址 






范例 :

ZXROSNG(config-bfd)#echo source ipv4 1.1.1.1 






相关命令 :

无 




## echo source ipv6 


echo source ipv6 




命令功能 :

配置echo源ipv6地址 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



echo source ipv6 
  ＜specify ipv6 address 
＞

no echo source ipv6 








命令参数解释 :



参数|描述
---|---
＜specify ipv6 address＞|ipv6地址








缺省 :

无 






使用说明 :

配置echo源ipv6地址 






范例 :

ZXROSNG(config-bfd)#echo source ipv6 1::1 






相关命令 :

无 




## gr 


gr 




命令功能 :

配置BFD的GR功能。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



gr 
  {disable 
|enable 
}







命令参数解释 :



参数|描述
---|---
disable|关闭GR功能
enable|开启GR功能








缺省 :

关闭GR功能 






使用说明 :

本命令用于开启或关闭GR功能 






范例 :

开启BFD的GR功能ZXROSNG(config-bfd)#gr enable 





相关命令 :

无 




## gr-time 


gr-time 




命令功能 :

配置GR超时的时间 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



gr-time 
  ＜gr time 
＞

no gr-time 








命令参数解释 :



参数|描述
---|---
＜gr time＞|GR超时的时间








缺省 :

300s 






使用说明 :

本命令用于配置GR超时的时间，单位为秒 






范例 :

配置GR超时时间为400秒ZXROSNG(config-bfd)#gr-time 400






相关命令 :

无 




interface :

interface (BFD模式) 




命令功能 :

该命令用于进入BFD接口配置模式。当需要进行BFD接口参数配置时，使用该命令。 






命令模式 :

 BFD模式  






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
＜interface-name＞|作用：配置BFD 检测参数的接口名字。取值范围：BFD支持的有效接口名。默认值：无








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令在BFD 配置模式下执行。该命令执行后，进入BFD 接口配置模式，进行BFD 接口检测参数配置。





范例 :

ZXROSNG(config-bfd)#interface fei-0/1/0/1 ZXROSNG(config-bfd-if-fei-0/1/0/1)#






相关命令 :

无 




## lag ipv6-source 


lag ipv6-source 




命令功能 :

配置LAG BFD会话全局的IPv6源地址。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



lag ipv6-source 
  ＜ipv6-address 
＞

no lag ipv6-source 








命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|LAG BFD会话全局IPv6源地址








缺省 :

无 






使用说明 :

配置LAG BFD会话全局IPv6源地址 






范例 :

ZXROSNG(config-bfd)#lag ipv6-source 1:1::1:1 






相关命令 :

无 




## lag source 


lag source 




命令功能 :

配置lagBFD会话全局的源地址 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



lag source 
  ＜ipv4-address 
＞

no lag source 








命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|lagBFD会话全局ipv4源地址








缺省 :

无 






使用说明 :

配置全局lag bfd会话源地址 






范例 :

ZXROSNG(config-bfd)#lag source 10.1.1.1 






相关命令 :

无 




## min-echo-rx-interval 


min-echo-rx-interval 




命令功能 :

配置单臂回声BFD会话的最小收包间隔。 






命令模式 :

 BFD接口模式  






命令默认权限级别 :

15 






命令格式 :



min-echo-rx-interval 
  ＜echo-interval 
＞

no min-echo-rx-interval 








命令参数解释 :



参数|描述
---|---
＜echo-interval＞|作用：配置单臂回声BFD会话的最小收包间隔。取值范围:$#35389450#$~$#35389451#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50。








缺省 :

50 






使用说明 :

本命令用于配置单臂回声BFD会话的最小收包间隔，缺省值为50ms 






范例 :

ZXROSNG(config-bfd-if-gei-0/1/0/1)#min-echo-rx-interval 100 






相关命令 :

无 




## mode 


mode 




命令功能 :

配置BFD建链模式 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



mode 
  {software 
|hardware 
}







命令参数解释 :



参数|描述
---|---
software|使用软件模式
hardware|使用硬件模式








缺省 :

mode software 






使用说明 :

软件模式是平台参与bfd会话的协商，硬件模式是bfd的建链协商完全由设备的项目端完成 






范例 :

ZXROSNG(config-bfd)#mode software 






相关命令 :

show running-config bfd 




## multiport 


multiport 




命令功能 :

该命令用来配置静态多跳BFD的目的UDP 端口号，BFD RFC文档中，对于多跳BFD，用4784作为BFD 报文的目的UDP端口号。由于有些设备厂商用3784作为多跳BFD的目的UDP 端口号。当和其他厂商存在差异时，用该命令调整BFD的目的UDP 端口号。 






命令模式 :

 PEER-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



multiport 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|作用：用于配置BFD报文目的UDP 端口号为3784。取值范围：无默认值：无
disable|作用：用于配置BFD报文目的UDP 端口号为4784，该选项为默认配置。取值范围：无默认值：无








缺省 :

disable 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。配置前，需要配置相应静态PEER-BFD实例。配置后，建议不要对改值进行修改。对于已经UP的BFD 会话，修改该值，不会对BFD的检测状态产生影响，BFD仍以之前配置的值进行发包检测。当BFD会话DOWN 掉后，会选择最后一次配置的值，进行建链和检测。





范例 :

ZXROSNG(config-bfd-peer-peer)#multiport disable ZXROSNG(config-bfd-peer-peer)#






相关命令 :

show running-config bfd 




## negotiate-fail-notify 


negotiate-fail-notify 




命令功能 :

配置BFD会话是否开启协商失败通知客户端全局开关 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



negotiate-fail-notify 
  {instance 
|static-route 
|static-rsvp-lsp 
|l2vpn 
} {disable 
|enable 
}







命令参数解释 :



参数|描述
---|---
instance|实力创建的BFD会话
static-route|静态路由协议创建的会话
static-rsvp-lsp|RSVP 创建的会话
l2vpn|L2VPN创建的会话
disable|关闭协商失败通知客户端
enable|开启协商失败通知客户端








缺省 :

disable 






使用说明 :

通过该命令开启或关闭指定协议BFD会话协商失败通知客户端功能 






范例 :

ZXROSNG(config-bfd)#negotiate-fail-notify instance enable 






相关命令 :

无 




## negotiate-fail-notify 


negotiate-fail-notify 




命令功能 :

配置BFD会话是否开启协商失败通知客户端。 






命令模式 :

 LINK-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



negotiate-fail-notify 
  {enable 
|disable 
|default 
}







命令参数解释 :



参数|描述
---|---
enable|会话协商失败通知客户端功能开启
disable|会话协商失败通知客户端功能关闭
default|会话协商失败通知客户端功能根据默认值判定








缺省 :

default 






使用说明 :

通过该命令开启或关闭BFD会话协商失败通知客户端功能。 






范例 :

关闭会话下的BFD会话协商失败通知客户端功能：ZXROSNG(config-bfd)#session peer peer-bfd ipv4 10.1.1.1 10.1.1.3ZXROSNG(config-bfd-peer-peer)#negotiate-fail-notify disable





相关命令 :

无 




## negotiate-fail-notify 


negotiate-fail-notify 




命令功能 :

配置BFD会话是否开启协商失败通知客户端。 






命令模式 :

 PEER-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



negotiate-fail-notify 
  {enable 
|disable 
|default 
}







命令参数解释 :



参数|描述
---|---
enable|会话协商失败通知客户端功能开启
disable|会话协商失败通知客户端功能关闭
default|协商失败通知客户端功能根据默认值判定








缺省 :

defaul 






使用说明 :

通过该命令开启或关闭BFD会话协商失败通知客户端功能。 






范例 :

关闭会话下的BFD会话协商失败通知客户端功能：ZXROSNG(config-bfd)#session peer peer-bfd ipv4 10.1.1.1 10.1.1.3ZXROSNG(config-bfd-peer-peer)#negotiate-fail-notify disable





相关命令 :

无 




## negotiate-fail-notify 


negotiate-fail-notify 




命令功能 :

配置BFD会话是否开启协商失败通知客户端。 






命令模式 :

 LDP-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



negotiate-fail-notify 
  {enable 
|disable 
|default 
}







命令参数解释 :



参数|描述
---|---
enable|会话协商失败通知客户端功能开启
disable|会话协商失败通知客户端功能关闭
default|会话协商失败通知客户端功能使用全局默认值








缺省 :

default 






使用说明 :

通过该命令开启或关闭BFD会话协商失败通知客户端功能。 






范例 :

关闭会话下的BFD会话协商失败通知客户端功能：ZXROSNG(config-bfd)#session peer peer-bfd ipv4 10.1.1.1 10.1.1.3ZXROSNG(config-bfd-peer-peer)#negotiate-fail-notify disable





相关命令 :

无 




## negotiate-fail-notify 


negotiate-fail-notify 




命令功能 :

配置BFD会话是否开启协商失败通知客户端。 






命令模式 :

 RSVP-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



negotiate-fail-notify 
  {enable 
|disable 
|default 
}







命令参数解释 :



参数|描述
---|---
enable|会话协商失败通知客户端功能开启
disable|会话协商失败通知客户端功能关闭
default|会话协商失败通知客户端功能很具全局配置判断








缺省 :

default 






使用说明 :

通过该命令开启或关闭BFD会话协商失败通知客户端功能。 






范例 :

关闭会话下的BFD会话协商失败通知客户端功能：ZXROSNG(config-bfd)#session peer peer-bfd ipv4 10.1.1.1 10.1.1.3ZXROSNG(config-bfd-peer-peer)#negotiate-fail-notify disable





相关命令 :

无 




## negotiate-fail-notify 


negotiate-fail-notify 




命令功能 :

配置BFD会话是否开启协商失败通知客户端。 






命令模式 :

 PW-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



negotiate-fail-notify 
  {enable 
|disable 
|default 
}







命令参数解释 :



参数|描述
---|---
enable|会话协商失败通知客户端功能开启
disable|会话协商失败通知客户端功能关闭
default|会话协商失败通知客户端功能使用全局默认配置








缺省 :

default 






使用说明 :

通过该命令开启或关闭BFD会话协商失败通知客户端功能。 






范例 :

关闭会话下的BFD会话协商失败通知客户端功能：ZXROSNG(config-bfd)#session peer peer-bfd ipv4 10.1.1.1 10.1.1.3ZXROSNG(config-bfd-peer-peer)#negotiate-fail-notify disable





相关命令 :

无 




## negotiate-fail-notify 


negotiate-fail-notify 




命令功能 :

配置BFD会话协商失败通知客户端功能。 






命令模式 :

 L2-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



negotiate-fail-notify 
  {enable 
|disable 
|default 
}







命令参数解释 :



参数|描述
---|---
enable|开启协商失败通知客户端功能
disable|关闭协商失败通知客户端功能
default|协商失败通知客户端功能使用全局配置








缺省 :

default 






使用说明 :

通过该命令开启或关闭BFD会话协商失败通知客户端功能。 






范例 :

关闭会话下的BFD会话协商失败通知客户端功能：ZXROSNG(config-bfd)#session 1 l2-bfd interface gei-0/1/0/1 source 1.1.1.1ZXROSNG(config-bfd-l2-1)##negotiate-fail-notify disable





相关命令 :

无 




## negotiate-fail-notify-time 


negotiate-fail-notify-time 




命令功能 :

配置BFD协商失败后多久通知客户端。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



negotiate-fail-notify-time 
  ＜negotiate fail notify time 
＞

no negotiate-fail-notify-time 








命令参数解释 :



参数|描述
---|---
＜negotiate fail notify time＞|BFD协商失败通知客户端的时间，范围：1-10000，单位：秒








缺省 :

300 






使用说明 :

通过该命令配置BFD会话多久协商失败通知客户端。 






范例 :

配置会话500秒协商失败通知客户端：ZXROSNG(config-bfd)#negotiate-fail-notify-time 500





相关命令 :

无 




## periodic-lsp-ping interval 


periodic-lsp-ping interval 




命令功能 :

需要发LSP PING报文的单播BFD会话，配置UP之后定时发送LSP PING的发送间隔。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



periodic-lsp-ping interval 
  ＜interval 
＞

no periodic-lsp-ping interval 








命令参数解释 :



参数|描述
---|---
＜interval＞|发送LSP-PING报文的时间间隔，单位：秒（s）








缺省 :

periodic-lsp-ping interval 5 






使用说明 :

需要发LSP PING报文的单播BFD会话，配置UP之后发LSP PING的间隔。 






范例 :

ZXROSNG(config-bfd)#periodic-lsp-ping interval 10ZXROSNG(config-bfd)#






相关命令 :

show running-config bfdperiodic-lsp-ping




## periodic-lsp-ping 


periodic-lsp-ping 




命令功能 :

需要发LSP PING报文的单播BFD会话，配置UP之后是否继续定时发送LSP PING。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



periodic-lsp-ping 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|会话up之后，继续发送lsp-ping报文。
disable|会话up之后，停止发送lsp-ping报文。








缺省 :

periodic-lsp-ping enable 






使用说明 :

需要发LSP PING报文的单播BFD会话，配置UP之后是否继续定时发送LSP PING。 






范例 :

ZXROSNG(config-bfd)#periodic-lsp-ping enableZXROSNG(config-bfd)#






相关命令 :

periodic-lsp-ping interval 




## pkt-len 


pkt-len 




命令功能 :

该命令用来配置BFD 检测报文的长度。在网络传输的过程中，网络节点可能会丢弃长度较大的报文。当需要用BFD 来检测网络传输过程中是否丢弃长度较大的报文时，可以使用该命令来配置BFD检测报文的长度。 






命令模式 :

 LINK-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



pkt-len 
 min 
 ＜min-pkt-length 
＞ max 
 ＜max-pkt-length 
＞

no pkt-len 








命令参数解释 :



参数|描述
---|---
＜min-pkt-length＞|作用：用于配置BFD最大检测报文长度。取值范围：24-512 的数字，单位为字节（Byte）取值规则：配置的最大报文长度不能小于最小报文长度值。默认值：24
＜max-pkt-length＞|作用：用于配置BFD最大检测报文长度。取值范围：24-512 的数字，单位为字节（Byte）取值规则：配置的最大报文长度不能小于最小报文长度值。默认值：24








缺省 :

minimum-pkt-len缺省值24maximum-pkt-len缺省值24






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令只能在LINK-BFD 模式和PEER-BFD 模式下执行。配置前，需要配置相应的BFD 实例。配置后，该BFD实例将有一个检测报文的长度范围，系统将根据配置的长度范围发送不同长度的BFD 检测报文。注意：配置的长度范围只对BFD 检测报文有效，对于BFD 建链报文（BFD会话建链期间发送的报文），不使用该范围。





范例 :

ZXROSNG(config-bfd-link-link)#pkt-len min 52 max 512ZXROSNG(config-bfd-link-link)#






相关命令 :

show running-config bfd 




## pkt-len 


pkt-len 




命令功能 :

该命令用来配置BFD 检测报文的长度。在网络传输的过程中，网络节点可能会丢弃长度较大的报文。当需要用BFD 来检测网络传输过程中是否丢弃长度较大的报文时，可以使用该命令来配置BFD检测报文的长度。 






命令模式 :

 PEER-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



pkt-len 
 min 
 ＜min-pkt-length 
＞ max 
 ＜max-pkt-length 
＞

no pkt-len 








命令参数解释 :



参数|描述
---|---
＜min-pkt-length＞|作用：用于配置BFD最大检测报文长度。取值范围：24-512 的数字，单位为字节（Byte）取值规则：配置的最大报文长度不能小于最小报文长度值。默认值：24
＜max-pkt-length＞|作用：用于配置BFD最大检测报文长度。取值范围：24-512 的数字，单位为字节（Byte）取值规则：配置的最大报文长度不能小于最小报文长度值。默认值：24








缺省 :

minimum-pkt-len缺省值24maximum-pkt-len缺省值24






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令只能在LINK-BFD 模式和PEER-BFD 模式下执行。配置前，需要配置相应的BFD 实例。配置后，该BFD实例将有一个检测报文的长度范围，系统将根据配置的长度范围发送不同长度的BFD 检测报文。注意：配置的长度范围只对BFD 检测报文有效，对于BFD 建链报文（BFD会话建链期间发送的报文），不使用该范围。。






范例 :

ZXROSNG(config-bfd-peer-peer)#pkt-len min 52 max 512ZXROSNG(config-bfd-peer-peer)#






相关命令 :

show running-config bfd 




## protect-binding 


protect-binding 




命令功能 :

指定切换策略，enable时表示BFD关联LDP FRR/ECMP快切，disable时表示BFD不关联LDP FRR/ECMP快切。 






命令模式 :

 LDP-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



protect-binding 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|BFD关联LDP FRR/ECMP快切
disable|BFD不关联LDP FRR/ECMP快切








缺省 :

enable 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。必须在LDP-BFD模式下配置该命令。该命令用于指示FTM是否关联LDP FRR/ECMP快切。enable时，表示BFD关联LDP FRR/ECMP快切；disable时表示BFD不关联LDP FRR/ECMP快切。





范例 :

ZXR10 (config-bfd-ldp-zte)# protect-binding disableZXR10 (config-bfd-ldp-zte)#





相关命令 :

show running-config bfd 




## session &amp;lt;mid&amp;gt; l2-bfd 


session <mid> l2-bfd 




命令功能 :

该命令用于配置二层BFD。当两个直连设备的一对二层接口需要部署BFD检测时，使用该命令。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



session  
 ＜instance-name 
＞ l2-bfd 
 interface 
 ＜interface-name 
＞ [source 
 ＜source-ipv4-address 
＞]







命令参数解释 :



参数|描述
---|---
＜instance-name＞|BFD实例名，长度为1~32个字符
＜interface-name＞|作用：用于指定BFD实例绑定的出接口取值范围：实际存在接口名字，不存在的接口无法配置。默认值：无
＜source-ipv4-address＞|作用：用于指定BFD 实例的源IP 地址。取值范围：任意合法单播IP地址。默认值：无。








缺省 :

无 






使用说明 :

该配置命令用于配置l2-bfd会话实例。L2-BFD需要指定LD和RD，因此该命令和LD RD指定命令配合使用。 






范例 :

ZXROSNG(config-bfd)#session l2 l2-bfd interface fei-0/1/0/1 source 1.1.1.1 ZXROSNG(config-bfd-l2-l2)#






相关命令 :

show running-config bfdshow bfd neighbor l2 briefshow bfd neighbor l2 detail




## session &amp;lt;mid&amp;gt; ldp-bfd 


session <mid> ldp-bfd 




命令功能 :

该命令用于配置LDP LSP 静态BFD。当需要在LDP LSP 链路上部署BFD检测时，使用该命令。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



session  
 ＜instance-name 
＞ ldp-bfd 
  {fec-address 
 ＜ipv4-address 
＞ mask-length 
 ＜mask-length 
＞ [source 
 ＜ipv4-address 
＞]|fec-address-v6 
 ＜ipv6-address 
＞ mask-length 
 ＜mask-length 
＞ [source 
 ＜ipv6-address 
＞]} [vrf 
 ＜vrf-name 
＞] [ld 
 ＜local-discriminator 
＞ rd 
 ＜remote-discriminator 
＞]







命令参数解释 :



参数|描述
---|---
＜instance-name＞|BFD实例名，长度为1~32个字符
fec-address|ipv4类型LDPBFD会话FEC，由LDP协议生成
＜ipv4-address＞|ipv4类型LDPBFD的远端地址
＜mask-length＞|LDP的掩码长度，范围：0-32
＜ipv4-address＞|ipv4类型LDPBFD的本端地址
fec-address-v6|ipv6类型LDPBFD会话FEC，由LDP协议生成
＜ipv6-address＞|ipv6类型LDPBFD的远端地址
＜mask-length＞|LDP的掩码长度，范围：0-32
＜ipv6-address＞|ipv6类型LDPBFD的本端地址
＜vrf-name＞|VRF名称，长度为1~32个字符
＜local-discriminator＞|本地标识符，范围:1-$#35389446#$
＜remote-discriminator＞|远端标识符，范围：1-4294967295








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。只能在 LDP LSP 的 Ingress 进行 BFD 绑定。一条 LSP 只能与一个 BFD 会话绑定。    在创建 BFD 配置项时，系统只检查 IP 地址是否符合 IP 地址格式，不检查其正确性。绑定错误的对端 IP 地址将导致 BFD 会话无法建立。该命令正确执行后，将创建一个静态LDP-BFD 实例，并进入LDP-BFD配置模式，进行会话参数配置。





范例 :

ZXROSNG(config-bfd)#session ldp ldp-bfd fec-address 22.2.2.2 mask-length 32 vrf zteZXROSNG(config-bfd-ldp-ldp)#






相关命令 :

show running-config bfdshow bfd neighbor ldp briefshow bfd neighbor ldp detail




## session &amp;lt;mid&amp;gt; link-bfd 


session <mid> link-bfd 




命令功能 :

该命令用于配置单跳静态BFD。当在两个设备间的直连链路上部署BFD检测时，使用该命令。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



session  
 ＜instance-name 
＞ link-bfd 
  {ipv4 
 ＜local-ipv4-address 
＞ ＜remote-ipv4-address 
＞ interface 
 ＜interface-name 
＞ [vrf 
 ＜vrf-name 
＞] [{[ld 
 ＜local-discriminator 
＞ rd 
 ＜remote-discriminator 
＞],[{asynchronous 
|single-arm-echo 
}]}]|ipv6 
 ＜local-ipv6-address 
＞ ＜remote-ipv6-address 
＞ interface 
 ＜interface-name 
＞ [vrf 
 ＜vrf-name 
＞] [{asynchronous 
|single-arm-echo 
}]}







命令参数解释 :



参数|描述
---|---
＜instance-name＞|BFD实例名，长度为1~32个字符
＜local-ipv4-address＞|建立会话的源ipv4地址，需用户配置保证该地址为本机存在有路由的地址
＜remote-ipv4-address＞|建立会话的目的ipv4地址
＜interface-name＞|会话的出接口名称
＜vrf-name＞|VRF名称，长度为1~32个字符
＜local-discriminator＞|本地标识符，范围1-$#35389446#$
＜remote-discriminator＞|远端标识符，范围1-4294967295
asynchronous|异步模式
single-arm-echo|单臂回声模式
＜local-ipv6-address＞|建立会话的源ipv6地址，需用户配置保证该地址为本机存在有路由的地址
＜remote-ipv6-address＞|建立会话的目的ipv6地址
＜interface-name＞|会话的出接口名称
＜vrf-name＞|VRF名称，长度为1~32个字符
asynchronous|异步模式
single-arm-echo|单臂回声模式








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。配置之前，要保证接口存在并正确连接各接口。对于三层接口，正确配置接口IP 地址。在创建 BFD 配置项时，系统只检查 IP 地址是否符合 IP 地址格式，不检查其正确性。用户应正确指定直连接口上的IP地址，如果绑定错误的地址，将导致会话无法建立或会话无法正确检测期望的直连链路。当BFD会话关联的接口删除时，对应的BFD的会话也会关联删除。如果在配置会话时，需要指定VRF，那么该VRF必须存在。当删除VRF时，会关联删除与之关联的BFD会话。该命令正确执行后，将创建一个静态LINK-BFD 实例，并进入LINK-BFD配置模式，进行会话参数配置。





范例 :

ZXROSNG(config-bfd)#session zte link-bfd ipv4 100.0.0.1 100.0.0.2 interface fei-0/1/0/1ZXROSNG(config-bfd-link-zte)#






相关命令 :

show running-config bfdshow bfd neighbor ip briefshow bfd neighbor ip detail




## session &amp;lt;mid&amp;gt; peer-bfd 


session <mid> peer-bfd 




命令功能 :

该命令用于配置多跳静态BFD。当需要快速检测和监控 IP 路由的转发连通状况，可以配置 BFD 多跳检测。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



session  
 ＜instance-name 
＞ peer-bfd 
  {ipv4 
 ＜local-ipv4-address 
＞ ＜remote-ipv4-address 
＞ [vrf 
 ＜vrf-name 
＞] [ld 
 ＜local-discriminator 
＞ rd 
 ＜remote-discriminator 
＞]|ipv6 
 ＜local-ipv6-address 
＞ ＜remote-ipv6-address 
＞ [vrf 
 ＜vrf-name 
＞]}







命令参数解释 :



参数|描述
---|---
＜instance-name＞|BFD实例名，长度为1~32个字符
＜local-ipv4-address＞|建立会话的源ipv4地址，需用户配置保证该地址为本机存在有路由的地址
＜remote-ipv4-address＞|建立会话的目的ipv4地址
＜vrf-name＞|VRF名称，长度为1~32个字符
＜local-discriminator＞|本地标识符，范围:1-$#35389446#$
＜remote-discriminator＞|远端标识符，范围1-4294967295
＜local-ipv6-address＞|建立会话的源ipv6地址，需用户配置保证该地址为本机存在有路由的地址
＜remote-ipv6-address＞|建立会话的目的ipv6地址
＜vrf-name＞|VRF名称，长度为1~32个字符








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。正确连接各接口并配置 IP 地址。配置路由协议，保证网络层可达。在第一次创建 BFD 会话时，必须绑定对端的 IP 地址和本地IP 地址，且创建后不可修改。在创建 BFD 配置项时，系统只检查 IP 地址是否符合 IP 地址格式，不检查其正确性。绑定错误的IP 地址将导致 BFD 会话无法建立。当静态指定PEER-BFD实例的本地标识符和远端标识符时，BFD 会话两端设备的本地标识符和远端标识符需要分别对应，即，本端的本地标识符与对端的远端标识符相同，否则会话无法正确建立。并且，本地标识符和远端标识符配置成功后不可修改。如果在配置会话时，需要指定VRF，那么该VRF必须存在。当删除VRF时，会关联删除与之关联的BFD会话。该命令正确执行后，将创建一个静态PEER-BFD 实例，并进入PEER-BFD配置模式，进行会话参数配置。





范例 :

ZXROSNG(config-bfd)#session peer peer-bfd ipv4 100.0.0.20 100.0.0.15 ZXROSNG(config-bfd-peer-peer)#






相关命令 :

show running-config bfdshow bfd neighbor ip briefshow bfd neighbor ip detail




## session &amp;lt;mid&amp;gt; pw-bfd 


session <mid> pw-bfd 




命令功能 :

该命令用于配置PW静态BFD检测。在基于 MPLS 的 L2VPN 网络应用中，如果 PE 之间使用 PW 连接，可以使用 BFD 检测 PW 的故障，加快感知故障链路的速度，促使上层应用的快速切换。当配置伪线BFD检测时，使用该命令。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



session  
 ＜instance-name 
＞ pw-bfd 
 pw-name 
 ＜pw-name 
＞ [{[local-ip 
 ＜ipv4-address 
＞],[remote-ip 
 ＜ipv4-address 
＞],[pw-ttl 
 ＜ttl 
＞],[ld 
 ＜local-discriminator 
＞ rd 
 ＜remote-discriminator 
＞],[lsp-ping-enable 
 [peer-router-ip 
 ＜ipv4-address 
＞ vc-id 
 ＜vc-id 
＞]]}]







命令参数解释 :



参数|描述
---|---
＜instance-name＞|BFD实例名，长度为1~32个字符
＜pw-name＞|作用：用于配置BFD 绑定的PW实例名。取值范围：实际存在的PW实例名。默认值：无
＜ipv4-address＞|作用：用于配置最后一段PW远端IP地址取值范围：远端有效IP 地址。注意事项：系统只检查 IP 地址是否符合 IP 地址格式，不检查其正确性。绑定错误的IP 地址将导致 BFD 会话无法建立。默认值：无
＜ipv4-address＞|作用：用于配置最后一段PW远端IP地址取值范围：远端有效IP 地址。注意事项：系统只检查 IP 地址是否符合 IP 地址格式，不检查其正确性。绑定错误的IP 地址将导致 BFD 会话无法建立。默认值：无
＜ttl＞|作用：用于配置多段伪线（MS-PW）TTL值。取值范围：1-255。默认值：无
＜local-discriminator＞|会话本端标识符，范围1-$#35389446#$
＜remote-discriminator＞|会话远端标识符，范围：1-4294967295
lsp-ping-enable|是否通过LSP ping启动BFD协商
＜ipv4-address＞|作用：用于配置最后一段PW远端IP地址取值范围：远端有效IP 地址。注意事项：系统只检查 IP 地址是否符合 IP 地址格式，不检查其正确性。绑定错误的IP 地址将导致 BFD 会话无法建立。默认值：无
＜vc-id＞|最后一段PW的VC ID








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。在该命令之前，需要配置网络层参数，使各节点之间可达。正确配置PW。如果配置的是MS-PW BFD检测实例，则需要指定MS-PW的跳数，该跳数不能小于MS-PW的实际跳数。对于MS-PW，可以配置端到端MS-PW BFD 检测，也可以在MS-PW的各段配置SS-PW BFD检测。如果想进行MS-PW BFD 和SS-PW BFD嵌套配置时，需要分别指定本地地址和远端地址。除此之外，不需要指定地址对。当被检测的PW实例删除时，会关联删除与之绑定的PW BFD实例。该命令正确执行后，将创建一个静态PW-BFD 实例，并进入PW-BFD配置模式，进行会话参数配置。





范例 :

ZXROSNG(config-bfd)#session pw pw-bfd pw-name pw1ZXROSNG(config-bfd-pw-pw)#






相关命令 :

show running-config bfdshow bfd neighbor pw briefshow bfd neighbor pw detail




## session &amp;lt;mid&amp;gt; rsvp-bfd 


session <mid> rsvp-bfd 




命令功能 :

该命令用于配置MPLS TE 隧道静态BFD。当需要在MPLS TE隧道上部署BFD 检测时，使用该命令。 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



session  
 ＜instance-name 
＞ rsvp-bfd 
 te_tunnel 
 ＜tunnel-id 
＞ [{[source 
 ＜ipv4-address 
＞],[ld 
 ＜local-discriminator 
＞ rd 
 ＜remote-discriminator 
＞]}]







命令参数解释 :



参数|描述
---|---
＜instance-name＞|BFD实例名，长度为1~32个字符
＜tunnel-id＞|隧道的ID，范围由性能参数决定，范围:1-$#100794374#$
＜ipv4-address＞|本地ip地址
＜local-discriminator＞|本地标识符，范围:1-$#35389446#$
＜remote-discriminator＞|远端标识符，范围：1-4294967295








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。配置前，需要配置MPLS TE隧道。BFD 检测 TE 隧道时，如果 TE 隧道的状态为 Down，能够创建 BFD 会话，但 BFD会话不能 Up。当被检测的TE隧道删除时，配置的BFD实例也会关联删除。该命令正确执行后，将创建一个静态RSVP-BFD 实例，并进入RSVP-BFD配置模式，进行会话参数配置。





范例 :

ZXROSNG(config-bfd)#session rsvp rsvp-bfd te_tunnel 1 ZXROSNG(config-bfd-rsvp-rsvp)#






相关命令 :

show running-config bfdshow bfd neighbor rsvp tunnel briefshow bfd neighbor rsvp tunnel detail




## show bfd dampen-parameters 


show bfd dampen-parameters 




命令功能 :

查看BFD阻尼功能设置参数信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd dampen-parameters 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

在BFD模式下设置阻尼参数后，可以根据该指令查看设置的阻尼参数信息 






范例 :

ZXROSNG(config-bfd)#show bfd dampen-parameters =============================================Dampen Type: IPDampen Half Life Time: 2000(s)Dampen Reuse Threshold: 3000Dampen Suppress Threshold: 5000Dampen Max Suppress Time: 15000(s)Dampen Increase: 1000ZXROSNG(config-bfd)#





相关命令 :

无 




## show bfd global-parameters 


show bfd global-parameters 




命令功能 :

显示bfd模块部分全局信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd global-parameters 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

显示bfd模块部分全局信息 






范例 :

范例 ZXROSNG#show bfd global-parameters =============================================L2 BFD default destination: 224.0.0.111Static route negotiate fail notify: OFFInstance negotiate fail notify: OFFStatic RSVP LSP negotiate fail notify: OFFNegotiate fail notify time: 20Backpath check:OFF





相关命令 :

无 




## show bfd neighbors all brief 


show bfd neighbors all brief 




命令功能 :

显示所有的bfd会话的简要信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors all brief 
  [{link 
|peer 
|l2 
|ldp 
|ldp-passive 
|pw 
|te-tunnel 
|te-passive 
|te-lsp 
|lag 
|sub-link 
|sr-be 
|mldp 
|mldp-passive 
|mte 
|mte-passive 
|srv6-te-tunnel 
|srv6-te-lsp 
|srv6-policy-sl 
}] 







命令参数解释 :



参数|描述
---|---
link|Single-hop IP BFD information
peer|Multi-hop IP BFD information
l2|L2 BFD information
ldp|LDP LSP BFD information
ldp-passive|LDP LSP passive BFD information
pw|PW BFD information
te-tunnel|RSVP tunnel BFD active information
te-passive|RSVP BFD passive information
te-lsp|RSVP LSP BFD active information
lag|LAG BFD information
sub-link|Single-hop bundle BFD information
sr-be|SR-BE BFD information
mldp|MLDP BFD information
mldp-passive|MLDP BFD passive information
mte|MTE BFD information
mte-passive|LAG BFD passive information
srv6-te-tunnel|SRv6-TE tunnel 类型BFD信息
srv6-te-lsp|SRv6-TE lsp类型BFD信息
srv6-policy-sl|SRv6-POLICY-SL 类型BFD信息








缺省 :

无 






使用说明 :

显示所有的bfd会话简要信息 






范例 :

显示所有的bfd会话简要信息：ZXROSNG#show bfd neighbors all briefSessions Up:2   Down:0  Init:0  Admindown:0  Total:2-----------------------------------------------------------------------------------------Local           Neighbor        LD         RD         State     Interface       Type100.1.12.1      100.1.12.2      2050       2050       UP        fei-0/1/0/1     LINK11.19.19.19     22.19.19.19     2051       2051       UP           ---          PEER





相关命令 :

无 




## show bfd neighbors all detail 


show bfd neighbors all detail 




命令功能 :

显示所有的bfd会话的简要信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors all detail 
  [{link 
|peer 
|l2 
|ldp 
|ldp-passive 
|pw 
|te-tunnel 
|te-passive 
|te-lsp 
|lag 
|sub-link 
|sr-be 
|mldp 
|mldp-passive 
|mte 
|mte-passive 
|srv6-te-tunnel 
|srv6-te-lsp 
|srv6-policy-sl 
}] 







命令参数解释 :



参数|描述
---|---
link|Single-hop IP类型BFD会话信息
peer|Multi-hop IP类型BFD会话信息
l2|L2类型BFD会话信息
ldp|LDP LSP类型BFD会话信息
ldp-passive|LDP LSP类型BFD被动端会话信息
pw|PW类型BFD会话信息
te-tunnel|RSVP tunnel类型BFD主动端会话信息
te-passive|RSVP类型BFD被动端会话信息
te-lsp|RSVP LSP类型BFD主动端会话信息
lag|LAG类型BFD会话信息
sub-link|Single-hop bundle类型BFD会话信息
sr-be|SR-BE类型BFD会话信息
mldp|MLDP类型BFD会话信息
mldp-passive|MLDP类型BFD被动端会话信息
mte|MTE类型BFD会话信息
mte-passive|MTE BFD类型BFD被动端会话信息
srv6-te-tunnel|SRv6 TE tunnel类型BFD会话信息
srv6-te-lsp|SRv6 TE lsp类型BFD会话信息
srv6-policy-sl|SRv6 policy SL类型BFD会话信息








缺省 :

无 






使用说明 :

显示所有的bfd会话详细信息 






范例 :

范例1：ZXROSNG#show bfd neighbors all detailSessions Up:32      Down:63      Init:0       Admindown:0       Total:95----------------------------------------------------------------------------LocalAddr:10.10.1.1PeerAddr :10.10.1.11Interface:gei-0/1/0/1VpnId:0                   VRF Name:Min BFD Length:24         Max BFD Length:24Track Action:---Local Discr:2058          Remote Discr:0            State:DOWNHolddown(ms):0BFD Type:SingleHopInstance Name:link11Detect Mode:AsynchronousSeamless Mode:Disable      Seamless Role:-------------------------------------------------------------------------------Version:1                 Dest UDP Port:3784        Final Bit:0Length:24                 Demand Mode:0             Poll Bit: 0MinTxInt:3014             MinRxInt:50               Multiplier:3Received MinTxInt:0       Received MinRxInt:0       Received Multiplier:0Min Echo Interval:0Local Diag:0(No Diagnostic)Rx Count:0                Rx Interval (ms) min/max/avg:0     /0     /0Tx Count:0                Tx Interval (ms) min/max/avg:0     /0     /0Local    AuthType/ID:---/0Received AuthType/ID:---/0Hold Left:Penalty:0Dampen state:NDampen Left:---Negotiate fail notify:OFFNegotiate fail notify time:300(s)Registered Protocols:INSTANCEDelay Up Time Left(s):0Uptime:Control Plane Rcv Phy Interface Name:---Debug packet/byte/error/event:OFF/OFF/OFF/OFF============================================================================
范例2：ZXROSNG(config-bfd-peer-peer)#show bfd neighbors all detailSessions Up:1       Down:0       Init:0       Admindown:0       Total:1----------------------------------------------------------------------------LocalAddr:10.1.1.1PeerAddr :10.1.1.2VpnId:0                   VRF Name:Min BFD Length:24         Max BFD Length:24Track Action:---Local Discr:2049          Remote Discr:2049         State:UPHolddown(ms):150BFD Type:MultiHopInstance Name:peerDetect Mode:AsynchronousSeamless Mode:Disable      Seamless Role:-------------------------------------------------------------------------------Version:1                 Dest UDP Port:4784        Final Bit:0Length:24                 Demand Mode:0             Poll Bit: 0MinTxInt:50               MinRxInt:50               Multiplier:3Received MinTxInt:50      Received MinRxInt:50      Received Multiplier:3Min Echo Interval:0Local Diag:0(No Diagnostic)Template Name:1Rx Count:10               Rx Interval (ms) min/max/avg:0     /60    /49Tx Count:990              Tx Interval (ms) min/max/avg:50    /50    /50Local    AuthType/ID:---/0Received AuthType/ID:---/0Hold Left:---Penalty:0Dampen state:NDampen Left:---Negotiate fail notify:OFFNegotiate fail notify time:300(s)Registered Protocols:INSTANCEDelay Up Time Left(s):0Uptime:0 day(s),0 hour(s),0 minute(s),53 second(s)Control Plane Rcv Phy Interface Name:fei-0/1/0/1Working Board:PFU-0/1                   Standby Board:---             Debug packet/byte/error/event:OFF/OFF/OFF/OFF============================================================================
范例3：ZXROSNG#sho bfd nei all detail srv6-te-tunnelSessions Up:0       Down:1       Init:0       Admindown:0       Total:1----------------------------------------------------------------------------TunnelId:te_tunnel1Track Action:---Local Discr:2049          Remote Discr:0            State:DOWNHolddown(ms):0BFD Type:SRv6 TE TunnelInstance Name:1Detect Mode:AsynchronousSeamless Mode:Enable      Seamless Role:Initiator----------------------------------------------------------------------------Version:1                 Dest UDP Port:7784        Final Bit:0Length:24                 Demand Mode:1             Poll Bit: 0MinTxInt:3484             MinRxInt:0                Multiplier:3Received MinTxInt:0       Received MinRxInt:0       Received Multiplier:0Min Echo Interval:0Local Diag:0(No Diagnostic)Template Name:Rx Count:0                Rx Interval (ms) min/max/avg:0     /0     /0Tx Count:0                Tx Interval (ms) min/max/avg:0     /0     /0Local    AuthType/ID:---/0Received AuthType/ID:---/0Hold Left:Penalty:0Dampen state:NDampen Left:---Negotiate fail notify:OFFNegotiate fail notify time:300(s)Registered Protocols:INSTANCEDelay Up Time Left(s):0Uptime:Control Plane Rcv Phy Interface Name:---Working Board:---                       Standby Board:---Debug packet/byte/error/event:OFF/OFF/OFF/OFF============================================================================
范例4：ZXROSNG#sho bfd nei all detail srv6-te-lspSessions Up:0       Down:1       Init:0       Admindown:0       Total:1----------------------------------------------------------------------------TunnelId:te_tunnel1LspId:1LspRole:masterTrack Action:---Local Discr:2051          Remote Discr:100          State:DOWNHolddown(ms):0BFD Type:SRv6 TE LSPInstance Name:Detect Mode:AsynchronousSeamless Mode:Enable      Seamless Role:Initiator----------------------------------------------------------------------------Version:1                 Dest UDP Port:7784        Final Bit:0Length:24                 Demand Mode:1             Poll Bit: 0MinTxInt:4133             MinRxInt:0                Multiplier:4Received MinTxInt:0       Received MinRxInt:0       Received Multiplier:0Min Echo Interval:0Local Diag:0(No Diagnostic)Template Name:Rx Count:0                Rx Interval (ms) min/max/avg:0     /0     /0Tx Count:0                Tx Interval (ms) min/max/avg:0     /0     /0Local    AuthType/ID:---/0Received AuthType/ID:---/0Hold Left:Penalty:0Dampen state:NDampen Left:---Negotiate fail notify:OFFNegotiate fail notify time:300(s)Registered Protocols:RSVP LSPDelay Up Time Left(s):0Uptime:Control Plane Rcv Phy Interface Name:---Working Board:---                       Standby Board:---Debug packet/byte/error/event:OFF/OFF/OFF/OFF============================================================================
范例5：ZXROSNG#sho bfd nei all detail srv6-policy-slSessions Up:0       Down:1       Init:0       Admindown:0       Total:1----------------------------------------------------------------------------Color: 1                   End-point: 22::22Segment-List:1Track Action:---Local Discr:2052          Remote Discr:100          State:DOWNHolddown(ms):0BFD Type:SRv6 Policy Segment ListInstance Name:Detect Mode:AsynchronousSeamless Mode:Enable      Seamless Role:Initiator----------------------------------------------------------------------------Version:1                 Dest UDP Port:7784        Final Bit:0Length:24                 Demand Mode:1             Poll Bit: 0MinTxInt:4962             MinRxInt:400              Multiplier:10Received MinTxInt:0       Received MinRxInt:0       Received Multiplier:0Min Echo Interval:0Local Diag:0(No Diagnostic)Template Name:xRx Count:0                Rx Interval (ms) min/max/avg:0     /0     /0Tx Count:0                Tx Interval (ms) min/max/avg:0     /0     /0Local    AuthType/ID:---/0Received AuthType/ID:---/0Hold Left:Penalty:0Dampen state:NDampen Left:---Negotiate fail notify:OFFNegotiate fail notify time:300(s)Registered Protocols:SR PolicyDelay Up Time Left(s):0Uptime:Control Plane Rcv Phy Interface Name:---Working Board:---                       Standby Board:---Debug packet/byte/error/event:OFF/OFF/OFF/OFF============================================================================






相关命令 :

无 




## show bfd neighbors dampen 


show bfd neighbors dampen 




命令功能 :

查看震荡过程中开启阻尼功能后抑制的会话信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors dampen 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

当开启会话阻尼功能后，在震荡过程中会话有可能被抑制，通过该命令查看因震荡导致会话抑制的信息 






范例 :

DUT6#show bfd neighbors dampen ============================================================================BFD Type:SingleHop LocalAddr:16.1.17.6PeerAddr :16.1.17.2Interface:gei-0/1/0/6.16VpnId:0                   VRF Name:Min BFD Length:24         Max BFD Length:24Local Discr:5551      Penalty:2666      Dampen Left:0 day(s),0 hour(s),24 minute(s),50 second(s)============================================================================BFD Type:SingleHop LocalAddr:FE80:0:0:0:12C1:88FF:FEAA:BB25PeerAddr :FE80:0:0:0:12C1:F0FF:FEAA:BB25Interface:gei-0/1/0/6.11VpnId:0                   VRF Name:Min BFD Length:24         Max BFD Length:24Local Discr:5546      Penalty:1333      Dampen Left:0 day(s),0 hour(s),9 minute(s),15 second(s)============================================================================





相关命令 :

无 




## show bfd neighbors deleting 


show bfd neighbors deleting 




命令功能 :

显示所有待删除会话信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors deleting 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于显示所有待删除会话信息。





范例 :

ZXROSNG(config-bfd)#show bfd neighbors deleting LocalAddr:10.1.1.1PeerAddr :10.1.1.2Interface:gei-0/1/0/1VpnId:0                   VRF Name:Min BFD Length:24         Max BFD Length:24Local Discr:2053          Remote Discr:2050      BFD Type:SingleHop 





相关命令 :

无 




## show bfd neighbors ip brief 


show bfd neighbors ip brief 




命令功能 :

显示IP类型BFD会话的概要信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors ip brief 
  [{[ip-type 
 {ipv4 
|ipv6 
}],[location 
 ＜board-name 
＞],[peer 
 {＜peer-ipv4-address 
＞|＜peer-ipv6-address 
＞}],[interface 
 ＜interface-name 
＞],[vrf 
 ＜vrf-name 
＞],[state 
 {down 
|init 
|up 
}],[deleting 
]}] 







命令参数解释 :



参数|描述
---|---
ipv4|会话地址类型为ipv4
ipv6|会话地址类型为ipv6
＜board-name＞|单板名称
＜peer-ipv4-address＞|会话远端的ipv4地址
＜peer-ipv6-address＞|会话远端ipv6地址
＜interface-name＞|会话的出接口名称
＜vrf-name＞|vrf名称
down|会话状态为down
init|会话状态为init
up|会话状态为up
deleting|待删除会话过滤条件








缺省 :

无 






使用说明 :

该命令用于显示IP类型BFD会话的概要信息。 






范例 :

[M6000\M6000-S]:ZXROSNG#show bfd neighbors ip brief state upLocalAddr       PeerAddr        LD        RD        Hold   State     Interface100.0.0.15      100.0.0.20      2049      2049      180    UP        fei-0/1/0/5[ZSR]:ZXROSNG#show bfd neighbors ip briefLocalAddr       PeerAddr        LD        RD        Hold   State     Interface100.0.0.15      100.0.0.20      2049      2049      180    UP        gei-1/5[89\9900]:ZXROSNG#show bfd neighbors ip briefLocalAddr       PeerAddr        LD        RD        Hold   State     Interface100.0.0.15      100.0.0.20      2049      2049      180    UP        fei-0/1/0/5





相关命令 :

无 




## show bfd neighbors ip detail 


show bfd neighbors ip detail 




命令功能 :

该命令用于查看IP类型BFD会话的详细信息。当需要查看IP类型BFD会话详细信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors ip detail 
  [{[ip-type 
 {ipv4 
|ipv6 
}],[location 
 ＜board-name 
＞],[peer 
 {＜peer-ipv4-address 
＞|＜peer-ipv6-address 
＞}],[interface 
 ＜interface-name 
＞],[vrf 
 ＜vrf-name 
＞],[state 
 {down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
ipv4|会话地址类型为IPv4
ipv6|会话地址类型为IPv6
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜peer-ipv4-address＞|会话远端IPv4地址
＜peer-ipv6-address＞|会话远端IPv6地址
＜interface-name＞|会话出接口名称
＜vrf-name＞|VRF名称
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。该命令可以显示各路由协议BFD实例和静态LINK-BFD、PEER-BFD实例的详细信息。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD的配置，将不显示任何信息。





范例 :

实例1 显示IP类型BFD实例的详细信息。ZXROSNG#show bfd nei ip detail ----------------------------------------------------------------------------LocalAddr:20.1.1.1            PeerAddr :20.1.1.2Local Discr:2054          Remote Discr:2055         State:UP                 Holddown(ms):150          Interface:gei-0/1/0/6Vpnid:0                   VRF Name:BFD Type:SingleHop Instance Name:----------------------------------------------------------------------------Version:1                 Dest UDP Port:3784        Final Bit:1         Local Diag:0              Demand Mode:0             Poll Bit:0         MinTxInt:50               MinRxInt:50               Multiplier:3         Received MinTxInt:50      Received MinRxInt:50      Received Multiplier:3       Length:24                 Min Echo Interval:0         Min BFD Length:24         Max BFD Length:24      Rx Count:89844            Rx Interval (ms) min/max/avg:40    /180   /99     Tx Count:89659            Tx Interval (ms) min/max/avg:60    /150   /99     Registered Protocols:OSPF Uptime:0 day(s),2 hour(s),33 minute(s)Control Plane Rcv Phy Interface Name:gei-0/1/0/6ZXROSNG#实例2 显示单板PFU-0/1上的IP 类型的BFD实例详细信息。ZXROSNG#show bfd nei ip detail location PFU-0/1----------------------------------------------------------------------------LocalAddr:20.1.1.1            PeerAddr :20.1.1.2Local Discr:2054          Remote Discr:2055         State:UP                 Holddown(ms):150          Interface:gei-0/1/0/6Vpnid:0                   VRF Name:BFD Type:SingleHop Instance Name:----------------------------------------------------------------------------Version:1                 Dest UDP Port:3784        Final Bit:1         Local Diag:0              Demand Mode:0             Poll Bit:0         MinTxInt:50               MinRxInt:50               Multiplier:3         Received MinTxInt:50      Received MinRxInt:50      Received Multiplier:3       Length:24                 Min Echo Interval:0         Min BFD Length:24         Max BFD Length:24      Rx Count:93205            Rx Interval (ms) min/max/avg:40    /180   /99     Tx Count:93069            Tx Interval (ms) min/max/avg:60    /150   /99     Registered Protocols:OSPF Uptime:0 day(s),2 hour(s),39 minute(s)Control Plane Rcv Phy Interface Name:gei-0/1/0/6





相关命令 :

无 




## show bfd neighbors l2 brief 


show bfd neighbors l2 brief 




命令功能 :

该命令用于查看静态L2-BFD会话的概要信息。当需要查看静态L2-BFD会话的概要信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors l2 brief 
  [{[location 
 ＜board-name 
＞],[interface 
 ＜interface-name 
＞],[state 
 {admindown 
|down 
|init 
|up 
}],[deleting 
]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜interface-name＞|会话指定的出接口名称
admindown|会话状态为admindown
down|会话状态为down
init|会话状态为init
up|会话状态为up
deleting|待删除会话过滤条件








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

实例1 查看L2-BFD实例的概要信息。ZXROSNG#show bfd neighbors l2 brief  LocalAddr       PeerAddr        LD        RD        Hold   State     Interface10.1.1.1        224.0.0.250     1         1         0      DOWN      gei-0/1/0/1ZXROSNG#实例2 查看单板PFU-0/1上的L2-BFD实例的概要信息。ZXROSNG#show bfd neighbors l2 brief location PFU-0/1LocalAddr       PeerAddr        LD        RD        Hold   State     Interface10.1.1.1        224.0.0.250     1         1         150    UP        gei-0/1/0/1ZXROSNG#





相关命令 :

无 




## show bfd neighbors l2 detail 


show bfd neighbors l2 detail 




命令功能 :

显示L2类型BFD会话的详细信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors l2 detail 
  [{[location 
 ＜board-name 
＞],[interface 
 ＜interface-name 
＞],[state 
 {admindown 
|down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|单板名称
＜interface-name＞|会话指定的出接口名称
admindown|会话状态为admindown
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

该命令用于显示L2类型BFD会话的详细信息。 






范例 :

ZXROSNG#show bfd neighbors l2 detail----------------------------------------------------------------------------LocalAddr:1.1.1.1PeerAddr :224.0.0.250Track Action:---Local Discr:1             Remote Discr:1            State:DOWNHolddown(ms):0            Interface:gei-0/1/0/1BFD Type:L2linkInstance Name:3Detect Mode:Asynchronous----------------------------------------------------------------------------Version:1                 Dest UDP Port:3784        Final Bit:0Local Diag:0              Demand Mode:0             Poll Bit:0MinTxInt:3642             MinRxInt:50               Multiplier:3Received MinTxInt:0       Received MinRxInt:0       Received Multiplier:0Length:24                 Min Echo Interval:0Rx Count:0                Rx Interval (ms) min/max/avg:0     /0     /0Tx Count:0                Tx Interval (ms) min/max/avg:0     /0     /0Penalty:0Dampen state:NDampen Left:---Negotiate fail notify:OFFNegotiate fail notify time:300(s)Registered Protocols:INSTANCEDelay Up Time Left(s):0Uptime:Control Plane Rcv Phy Interface Name:---Debug packet/byte/error/event:OFF/OFF/OFF/OFF============================================================================






相关命令 :

无 




## show bfd neighbors lag brief 


show bfd neighbors lag brief 




命令功能 :

显示lag类型BFD会话的概要信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors lag brief 
  [{[location 
 ＜board-name 
＞],[interface 
 ＜interface-name 
＞],[state 
 {down 
|init 
|up 
}],[deleting 
]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|会话所在的单板名称
＜interface-name＞|会话出接口的名称
down|会话状态为down
init|会话状态为init
up|会话状态为up
deleting|待删除会话过滤条件








缺省 :

无





使用说明 :

该命令主要用于显示lag类型BFD会话的概要信息。 






范例 :

ZXROSNG(config-lacp-member-if-gei-0/1/0/1)#sho bfd n lag brief LocalAddr       PeerAddr        LD        RD        Hold   State     Interface10.1.1.2        10.1.1.1        2510      2113      150    UP        gei-0/1/0/1






相关命令 :

无 




## show bfd neighbors lag detail 


show bfd neighbors lag detail 




命令功能 :

显示lag类型BFD会话的详细信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors lag detail 
  [{[location 
 ＜board-name 
＞],[interface 
 ＜interface-name 
＞],[state 
 {down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|会话所在的单板名称
＜interface-name＞|会话的出接口名称
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

该命令用于显示lag类型BFD会话的详细信息。 






范例 :

ZXROSNG#show bfd neighbors lag detail----------------------------------------------------------------------------LocalAddr:10.1.1.2            PeerAddr :10.1.1.1Local Discr:2510          Remote Discr:2113         State:UP                 Holddown(ms):150          Interface:gei-0/1/0/1BFD Type:LAG Instance Name:----------------------------------------------------------------------------Version:1                 Dest UDP Port:6784        Final Bit:0         Local Diag:0              Demand Mode:0             Poll Bit:0         MinTxInt:50               MinRxInt:50               Multiplier:3         Received MinTxInt:50      Received MinRxInt:50      Received Multiplier:3       Hold Left:---Length:24                 Min Echo Interval:0         Rx Count:556              Rx Interval (ms) min/max/avg:0     /130   /98     Tx Count:531              Tx Interval (ms) min/max/avg:60    /110   /99     Local    AuthType/ID:---/0 Received AuthType/ID:---/0 Penalty:0         Dampen state:NDampen Left:---Registered Protocols:LACP Uptime:0 day(s),0 hour(s),0 minute(s),55 second(s)Control Plane Rcv Phy Interface Name:gei-0/1/0/1Debug packet/byte/error/event:ON/OFF/OFF/OFF============================================================================





相关命令 :

无 




## show bfd neighbors ldp brief 


show bfd neighbors ldp brief 




命令功能 :

该命令用于查看LDP LSP BFD实例的概要信息。当需要查看LDP LSP会话的概要信息时，使用该命令。   





命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :


show bfd neighbors ldp brief 
  [{[location 
 ＜board-name 
＞],[peer-address 
 {＜ipv4-address 
＞|＜ipv6-address 
＞}],[mask-length 
 ＜mask-length 
＞],[vrf 
 ＜vrf-name 
＞],[state 
 {down 
|init 
|up 
}],[deleting 
]}] 






命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称。默认值：无
＜ipv4-address＞|ipv4 FEC地址
＜ipv6-address＞|ipv6 FEC地址
＜mask-length＞|掩码长度
＜vrf-name＞|vrf名称
down|会话状态为down
init|会话状态为init
up|会话状态为up
deleting|待删除会话过滤条件








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

实例1 显示LDP LSP BFD实例的概要信息。ZXROSNG#show bfd neighbors ldp brief PeerAddr        PrefixLen  LD       RD        Hold   State     10.1.1.2        0          2056     2063      150    UP2.2.2.2         32         2055     2073      30     UPZXROSNG#实例2 显示单板PFU-0/1上的LDP LSP BFD实例的概要信息。ZXROSNG#show bfd neighbors ldp brief location PFU-0/1PeerAddr        PrefixLen  LD       RD        Hold   State     10.1.1.2        0          2056     2063      150    UPZXROSNG#





相关命令 :

无 




## show bfd neighbors ldp detail 


show bfd neighbors ldp detail 




命令功能 :

该命令用于查看LDP LSP BFD实例的详细信息。当需要查看LDP LSP会话的详细信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors ldp detail 
  [{[location 
 ＜board-name 
＞],[peer-address 
 {＜ipv4-address 
＞|＜ipv6-address 
＞}],[mask-length 
 ＜mask-length 
＞],[vrf 
 ＜vrf-name 
＞],[state 
 {down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称.默认值：无
＜ipv4-address＞|ipv4 类型会话的FEC地址
＜ipv6-address＞|ipv6类型的会话的FEC地址
＜mask-length＞|掩码长度
＜vrf-name＞|vrf名称
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

实例1 显示LDP LSP BFD实例的详细信息。ZXROSNG#show bfd neighbors ldp detail ----------------------------------------------------------------------------PeerAddr :2.2.2.2Prefixlen:32                    Local Discr:2055          Remote Discr:2117         State:UP                 Holddown(ms):30           Vpnid:0                   VRF Name:BFD Type:LDP[Active] Instance Name:----------------------------------------------------------------------------Version:1                 Dest UDP Port:3784        Final Bit:1         Local Diag:0              Demand Mode:0             Poll Bit:0         MinTxInt:10               MinRxInt:10               Multiplier:3         Received MinTxInt:10      Received MinRxInt:10      Received Multiplier:3       Length:24                 Min Echo Interval:0                  Rx Count:5                Rx Interval (ms) min/max/avg:60    /110   /0      Tx Count:7                Tx Interval (ms) min/max/avg:10    /100   /0      Registered Protocols:LDP LSP Uptime:0 day(s),0 hour(s),0 minute(s)Control Plane Rcv Phy Interface Name:gei-0/1/0/1=====================================================================实例2 显示单板PFU-0/1上的LDP LSP BFD实例的详细信息。ZXROSNG#show bfd neighbors ldp detail location PFU-0/1----------------------------------------------------------------------------PeerAddr :2.2.2.2Prefixlen:32                    Local Discr:2055          Remote Discr:2122         State:UP                 Holddown(ms):30           Vpnid:0                   VRF Name:BFD Type:LDP[Active] Instance Name:----------------------------------------------------------------------------Version:1                 Dest UDP Port:3784        Final Bit:1         Local Diag:0              Demand Mode:0             Poll Bit:0         MinTxInt:10               MinRxInt:10               Multiplier:3         Received MinTxInt:10      Received MinRxInt:10      Received Multiplier:3       Length:24                 Min Echo Interval:0         Rx Count:134              Rx Interval (ms) min/max/avg:40    /120   /0      Tx Count:56               Tx Interval (ms) min/max/avg:10    /110   /85     Registered Protocols:LDP LSP Uptime:0 day(s),0 hour(s),0 minute(s)Control Plane Rcv Phy Interface Name:gei-0/1/0/1





相关命令 :

无 




## show bfd neighbors local-disc 


show bfd neighbors local-disc 




命令功能 :

该命令用于根据BFD会话的本端标识符来查看该会话的详细信息。当需要查看某一个指定的BFD会话的详细信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors local-disc 
  ＜local-discriminator 
＞ [deleting 
] 







命令参数解释 :



参数|描述
---|---
＜local-discriminator＞|作用：用于指定BFD会话的本地标识符。取值范围： 1-4294967295的数字。默认值：无
deleting|待删除会话过滤条件








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

ZXROSNG#show bfd neighbors local-disc 2049 ----------------------------------------------------------------------------LocalAddr:192.0.2.1PeerAddr :192.0.2.2VpnId:0                   VRF Name:Min BFD Length:24         Max BFD Length:24Local Discr:2049          Remote Discr:2049         State:UP                 Holddown(ms):150          BFD Type:MultiHop Instance Name:3----------------------------------------------------------------------------Version:1                 Dest UDP Port:4784        Final Bit:1         Local Diag:0              Demand Mode:0             Poll Bit: 0         MinTxInt:50               MinRxInt:50               Multiplier:3         Received MinTxInt:50      Received MinRxInt:50      Received Multiplier:3       Length:24                 Min Echo Interval:0         Rx Count:39021            Rx Interval (ms) min/max/avg:0     /200   /98     Tx Count:39414            Tx Interval (ms) min/max/avg:50    /140   /97     Registered Protocols:INSTANCE Uptime:0 day(s),1 hour(s),6 minute(s)Control Plane Rcv Phy Interface Name:gei-0/1/0/2============================================================================






相关命令 :

无 




## show bfd neighbors parameters local-disc 


show bfd neighbors parameters local-disc 




命令功能 :

查看指定本端标识符的BFD会话参数信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors parameters local-disc 
  ＜local-discriminator 
＞ 







命令参数解释 :



参数|描述
---|---
＜local-discriminator＞|作用：用于指定BFD会话的本地标识符。取值范围： 1-4294967295的数字。默认值：无








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。该命令执行后，显示指定本端标识符的BFD会话参数信息。





范例 :

范例1：ZXROSNG#show bfd neighbors parameters local-disc 2049----------------------------------------------------------------------------FEC:10.2.2.2/32VpnId:0                   VRF Name:Local Discr:2049          Remote Discr:2051         State:UP                 Holddown(ms):300          BFD Type:LDP[Active] Instance Name:ldpDetect Mode:AsynchronousAuthentication Key Check:DisableNotify Port State:-------------------------------------------------------------------------------Session Parameters:LDP LSP Tx/Rx/Mult: 100/100/5INSTANCE Tx/Rx/Mult: 200/200/6Selected Tx/Rx/Mult: 100/100/5============================================================================
范例2：ZXROSNG(config-bfd-template-abc)#show bfd neighbors parameters local-disc 2049----------------------------------------------------------------------------LocalAddr:10.1.1.1PeerAddr :10.1.1.2VpnId:0                   VRF Name:Min BFD Length:24         Max BFD Length:24Local Discr:2049          Remote Discr:2049         State:UPHolddown(ms):150BFD Type:MultiHopInstance Name:peerDetect Mode:AsynchronousAuthentication Key Check:DisableNotify Port State:-------------------------------------------------------------------------------Session Parameters:INSTANCE Tx/Rx/Mult/TemplateName: 0/0/0/1Selected Template:1 Tx/Rx/Mult: 0/0/0Selected Tx/Rx/Mult/EchoRx: 50/50/3/50[Default]Board Parameters:                                                                Total Num:1            Valid Num:1            Policy:standalone                   ----------------------------------------------------------------------------      Name        Status      Interface           Capability   Role    SourcePFU-0/1     working     fei-0/1/0/1         INTF_ONLY    master  FROM_INPORT============================================================================






相关命令 :

无 




## show bfd neighbors pw brief 


show bfd neighbors pw brief 




命令功能 :

该命令用于查看PW  BFD实例的概要信息。当需要查看PW  BFD会话的概要信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors pw brief 
  [{[location 
 ＜board-name 
＞],[pw-name 
 ＜pw-name 
＞],[state 
 {down 
|init 
|up 
}],[deleting 
]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜pw-name＞|pw存在的有效实例名称
down|会话状态为down
init|会话状态为init
up|会话状态为up
deleting|待删除会话过滤条件








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

ZXROSNG#show bfd neighbors pw brief Pwname    LD        RD        Hold        State   pw1       4097      0         0           DOWN






相关命令 :

无 




## show bfd neighbors pw detail 


show bfd neighbors pw detail 




命令功能 :

该命令用于查看PW BFD 实例的详细信息。当需要查看PW  BFD会话的详细信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors pw detail 
  [{[location 
 ＜board-name 
＞],[pw-name 
 ＜pw-name 
＞],[state 
 {down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜pw-name＞|pw存在有效的实例名称
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD的配置，将不显示任何信息。





范例 :

实例1 显示PW BFD实例的详细信息。ZXROSNG#show bfd neighbors pw detail ----------------------------------------------------------------------------Pw Name: pw1001             Pw TTL:1         LocalAddr:---            PeerAddr :---Local Discr:2076          Remote Discr:0            State:DOWN                 Holddown(ms):0            BFD Type:PwType Instance Name:pwbfd----------------------------------------------------------------------------Version:1                 Dest UDP Port:3784        Final Bit:0         Local Diag:0              Demand Mode:0             Poll Bit: 0         MinTxInt:4036             MinRxInt:50               Multiplier:3         Received MinTxInt:0       Received MinRxInt:0       Received Multiplier:0       Length:24                 Min Echo Interval:0         Rx Count:0                Rx Interval (ms) min/max/avg:0     /0     /0      Tx Count:0                Tx Interval (ms) min/max/avg:0     /0     /0      Registered Protocols:INSTANCE Uptime:Control Plane Rcv Phy Interface Name:---=====================================================================ZXROSNG#





相关命令 :

无 




## show bfd neighbors rsvp lsp brief 


show bfd neighbors rsvp lsp brief 




命令功能 :

该命令用于查看RSVP LSP BFD实例的概要信息。当需要查看RSVP LSP BFD会话的概要信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors rsvp lsp brief 
  [{[location 
 ＜board-name 
＞],[tunnel-id 
 ＜tunnel-id 
＞],[state 
 {down 
|init 
|up 
}],[deleting 
]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜tunnel-id＞|隧道实例ID:范围1-$#100794374#$
down|会话状态为down
init|会话状态为init
up|会话状态为up
deleting|待删除会话过滤条件








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

实例1 显示RSVP LSP BFD实例的概要信息。ZXROSNG(config)#show bfd neighbors rsvp lsp brief TunnelId        LspId         LD        RD        Hold      State     te_tunnel1      1             2063      0         0         DOWNZXROSNG(config)#





相关命令 :

无 




## show bfd neighbors rsvp lsp detail 


show bfd neighbors rsvp lsp detail 




命令功能 :

该命令用于查看RSVP LSP BFD实例的详细信息。当需要查看RSVP LSP BFD会话的详细信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors rsvp lsp detail 
  [{[location 
 ＜board-name 
＞],[tunnel-id 
 ＜tunnel-id 
＞],[state 
 {down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜tunnel-id＞|隧道实例ID:范围1-$#100794374#$
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

实例1 显示RSVP LSP BFD实例的详细信息。ZXROSNG(config)#show bfd neighbors rsvp lsp detail ----------------------------------------------------------------------------TunnelId:te_tunnel1LspId:1         LspRole:---Local Discr:2063           Remote Discr:0             State:DOWN                 Holddown(ms):0             BFD Type:Bidirection RSVP LSP Instance Name:----------------------------------------------------------------------------Version:1                  Dest UDP Port:3784         Final Bit:0         Local Diag: 0              Demand Mode:0              Poll Bit:0         MinTxInt: 3759             MinRxInt:10                Multiplier:3         Received MinTxInt: 0       Received MinRxInt:0        Received Multiplier:0       Length:24                  Min Echo Interval:0         Rx Count:0                 Rx Interval (ms) min/max/avg:0     /0     /0      Tx Count:0                 Tx Interval (ms) min/max/avg:0     /0     /0      Registered Protocols:Bidirection RSVP LSP Uptime:Control Plane Rcv Phy Interface Name:---===============================================================ZXROSNG(config)#





相关命令 :

无 




## show bfd neighbors rsvp passive brief 


show bfd neighbors rsvp passive brief 




命令功能 :

该命令用于查看RSVP LSP BFD会话被动端的概要信息。当需要查看RSVP LSP BFD被动端会话的概要信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors rsvp passive brief 
  [{[location 
 ＜board-name 
＞],[peer-address 
 ＜ipv4-address 
＞],[state 
 {down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜ipv4-address＞|会话远端IPv4地址
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD数据。如果没有该类型BFD数据，将不显示任何信息。该命令只显示RSVP LSP BFD 被动端会话信息。





范例 :

实例1 显示RSVP LSP BFD实例的概要信息。ZXROSNG(config)#show bfd neighbors rsvp passive brief    PeerAddr/Tunnel  LD        RD        Hold      State     10.1.1.1         2505      2090      300       UPZXROSNG(config)#





相关命令 :

无 




## show bfd neighbors rsvp passive detail 


show bfd neighbors rsvp passive detail 




命令功能 :

该命令用于查看RSVP LSP BFD会话被动端的详细信息。当需要查看RSVP LSP BFD被动端会话的详细信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors rsvp passive detail 
  [{[location 
 ＜board-name 
＞],[peer-address 
 ＜ipv4-address 
＞],[state 
 {down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜ipv4-address＞|会话远端IPv4地址
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型数据。如果没有该类型BFD数据，将不显示任何信息。该命令只显示RSVP LSP BFD被动端会话信息。





范例 :

实例1 显示RSVP LSP BFD实例的详细信息。ZXROSNG(config)#show bfd neighbors rsvp passive detail    ----------------------------------------------------------------------------PeerAddr:1.1.1.1Local Discr:2415           Remote Discr:2049          State:UPHolddown(ms):150           BFD Type:RSVP[Passive]Instance Name:Detect Mode:Asynchronous----------------------------------------------------------------------------Version:1                  Dest UDP Port:3784         Final Bit:0         Local Diag: 0              Demand Mode:0              Poll Bit:0         MinTxInt: 10               MinRxInt:10                Multiplier:3         Received MinTxInt: 50      Received MinRxInt:50       Received Multiplier:3       Length:52                  Min Echo Interval:0         Rx Count:418               Rx Interval (ms) min/max/avg:0     /140   /98    Tx Count:393               Tx Interval (ms) min/max/avg:70    /110   /99    Local    AuthType/ID:Meticulous SHA1/1Received AuthType/ID:Meticulous SHA1/1Hold Left:---Registered Protocols:---Delay Up Time Left(s):0Uptime:0 day(s),0 hour(s),0 minute(s),38 second(s)Control Plane Rcv Phy Interface Name:gei-0/1/0/1Debug packet/byte/error/event:OFF/OFF/OFF/OFF============================================================================






相关命令 :

无 




## show bfd neighbors rsvp tunnel brief 


show bfd neighbors rsvp tunnel brief 




命令功能 :

该命令用于查看RSVP TUNNEL BFD实例的概要信息。当需要查看RSVP TUNNEL BFD会话的概要信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors rsvp tunnel brief 
  [{[location 
 ＜board-name 
＞],[tunnel-id 
 ＜tunnel-id 
＞],[state 
 {down 
|init 
|up 
}],[deleting 
]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜tunnel-id＞|隧道实例ID:范围1-$#100794374#$
down|会话状态为down
init|会话状态为init
up|会话状态为up
deleting|待删除会话过滤条件








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

实例1 显示RSVP TUNNEL BFD实例的概要信息。ZXROSNG#show bfd neighbors rsvp tunnel brief TunnelId         LD        RD        Hold      State     te_tunnel2       2067      0         0         DOWNZXROSNG#





相关命令 :

无 




## show bfd neighbors rsvp tunnel detail 


show bfd neighbors rsvp tunnel detail 




命令功能 :

该命令用于查看RSVP TUNNEL BFD实例的详细信息。当需要查看RSVP TUNNEL BFD会话的详细信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd neighbors rsvp tunnel detail 
  [{[location 
 ＜board-name 
＞],[tunnel-id 
 ＜tunnel-id 
＞],[state 
 {down 
|init 
|up 
}]}] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无
＜tunnel-id＞|隧道实例ID:范围1-$#100794374#$
down|会话状态为down
init|会话状态为init
up|会话状态为up








缺省 :

无 






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。使用该命令前，要有相应类型BFD实例配置。如果没有该类型BFD 的配置，将不显示任何信息。





范例 :

ZXROSNG#show bfd neighbors rsvp tunnel detail ----------------------------------------------------------------------------TunnelId:te_tunnel1            Local Discr:2050           Remote Discr:2355            State:UP                 Holddown(ms):150           BFD Type:RSVP TUNNEL[Active]Instance Name:zte----------------------------------------------------------------------------Version:1                  Dest UDP Port:3784         Final Bit:1         Local Diag: 0              Demand Mode:0              Poll Bit:0         MinTxInt: 50               MinRxInt:50                Multiplier:3         Received MinTxInt: 10      Received MinRxInt:10       Received Multiplier:3       Length:24                  Min Echo Interval:0         Rx Count:74582             Rx Interval (ms) min/max/avg:40    /200   /98     Tx Count:74715             Tx Interval (ms) min/max/avg:50    /200   /98     Registered Protocols:INSTANCE Uptime:0 day(s),2 hour(s),7 minute(s)Control Plane Rcv Phy Interface Name:gei-0/1/0/1============================================================================






相关命令 :

无 




## show bfd statistics 


show bfd statistics 




命令功能 :

该命令用来查看设备上BFD基本信息。当需要查看某一设备上BFD会话的基本统计信息时，使用该命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bfd statistics 
  [location 
 ＜board-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜board-name＞|作用：用于设置BFD所在单板的名称，当选择该参数时，将只显示该单板上的BFD实例信息。取值范围：有效的单板名称默认值：无








缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。该命令执行后，系统将根据BFD会话的类型，统计BFD各种状态下的BFD会话数目及该类BFD会话总数。如果在会话执行之前没有BFD实例的配置，那么对应的BFD会话统计信息将显示为0。






范例 :

ZXROSNG(config-bfd)#show bfd statistics[SingleHop]:Sessions Up:0       Down:1       Init:0       Admindown:0       Total:1[Sub SingleHop]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[MultiHop]:Sessions Up:0       Down:1       Init:0       Admindown:0       Total:1[L2link]:Sessions Up:0       Down:1       Init:0       Admindown:0       Total:1[LDP/Active]:Sessions Up:0       Down:1       Init:0       Admindown:0       Total:1[LDP/Passive]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[RSVP TUNNEL/Active]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[RSVP LSP/Active]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[RSVP/Passive]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[PW]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[LAG]:Sessions Up:0       Down:2       Init:0       Admindown:0       Total:2[SR-BE/Active]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[MLDP/Active]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[MLDP/Passive]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[MTE/Active]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0[MTE/Passive]:Sessions Up:0       Down:0       Init:0       Admindown:0       Total:0----------------------------------------------------------------------------[All]:Sessions Up:0       Down:6       Init:0       Admindown:0       Total:6The MAX num of BFD session on device:         16384The left num of BFD session can be configured:16378






相关命令 :

无 




## show debug bfd 


show debug bfd 




命令功能 :

查看BFD会话debug信息开关打开的情况。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug bfd 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

拥有管理员权限的操作员可以使用这条命令。该命令执行后，会显示bfd会话debug信息开关是否打开。





范例 :

ZXROSNG#show debug bfd BFD:   BFD event debugging is on  BFD packet debugging is on   BFD byte debugging is onZXROSNG#show debug bfd BFD:   BFD all debugging is on






相关命令 :

debug bfd eventdebug bfd errordebug bfd bytedebug bfd packetdebug bfd all




## single-arm-echo 


single-arm-echo 




命令功能 :

配置BFD会话单臂回声功能。 






命令模式 :

 BFD接口模式  






命令默认权限级别 :

15 






命令格式 :



single-arm-echo 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启BFD会话单臂回声功能
disable|关闭BFD会话单臂回声功能








缺省 :

会话单臂回声功能关闭 






使用说明 :

本命令用于开启或关闭BFD会话的单臂echo功能 






范例 :

ZXROSNG(config-bfd-if-gei-0/1/0/1)#single-arm-echo enable 






相关命令 :

无 




## single-arm-echo-ipv6 


single-arm-echo-ipv6 




命令功能 :

ipv6的echo bfd功能使能。 






命令模式 :

 BFD接口模式  






命令默认权限级别 :

15 






命令格式 :



single-arm-echo-ipv6 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能。
disable|不使能








缺省 :

无 






使用说明 :

ipv6的echo bfd功能使能。该命令在bfd接口模式下使用。






范例 :

ZXROSNG(config-bfd-if-gei-0/1/0/1)#single-arm-echo-ipv6 enableZXROSNG(config-bfd-if-gei-0/1/0/1)#





相关命令 :

single-arm-echo enable 




## suppress 


suppress 




命令功能 :

P2MP被动端是否可以创建bfd 






命令模式 :

 BFD模式  






命令默认权限级别 :

15 






命令格式 :



suppress 
 p2mp-passive 


no suppress 
 p2mp-passive 








命令参数解释 :



参数|描述
---|---
p2mp-passive|P2MP的被动端








缺省 :

无 






使用说明 :

P2MP被动端是否可以创建bfd 






范例 :

ZXROSNG(config-bfd)#suppress p2mp-passiveZXROSNG(config-bfd)#






相关命令 :

无 




## time-negotiation 


time-negotiation 




命令功能 :

该命令用于配置BFD 的检测参数，包括最小发包间隔，最小收包间隔，和检测倍数。在建立BFD会话时，可以根据网络状况和性能要求，调整设备的BFD 报文发送间隔、接收间隔以及本地检测倍数。 






命令模式 :

 PEER-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



time-negotiation 
 interval 
 ＜tx-interval 
＞ min-rx 
 ＜rx-interval 
＞ multiplier 
 ＜detect-multiplier 
＞

no time-negotiation 








命令参数解释 :



参数|描述
---|---
＜tx-interval＞|作用：配置BFD实例检测报文期望的最小发包间隔。取值范围:$#35389448#$~$#35389449#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50。
＜rx-interval＞|作用：配置BFD实例检测报文期望的最小收包间隔。取值范围：$#35389450#$~$#35389451#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50 。
＜detect-multiplier＞|作用：配置BFD实例的本地检测倍数。取值范围：3-50 的数字。默认值：3。








缺省 :

interval缺省值为50min-rx缺省值为50multiplier缺省值为3






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令可以在BFD接口模式、L2-BFD 模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在BFD接口模式下配置参数后，所有与该接口绑定的LINK-BFD（单跳BFD）都将使用该接口下配置的BFD 参数进行发包和检测。对该接口BFD 检测参数的调整，将改变所有与该接口绑定的LINK-BFD的检测参数。 在非BFD接口模式下配置BFD检测参数前，需要配置相应的BFD实例，然后进入具体的实例模式进行参数配置。例如：需要对某一L2-BFD实例进行BFD 检测参数调整时，首先要创建该L2-BFD 实例，然后进入L2-BFD模式进行BFD检测参数配置。BFD检测参数有默认值，当不对BFD检测参数配置时，BFD实例将以默认的检测参数进行发包和检测。为满足快速检测的需求，BFD 协议规定发送间隔和接收间隔的时间单位是微秒。但限于目前的设备处理能力，大部分厂商的设备在配置 BFD 时只能达到毫秒级，在进行内部处理时再转换到微秒级。为降低对系统资源的占用，在BFD会话UP之前，BFD以3000 毫秒～5000 毫秒之间的一个随机值来发送报文，当BFD 会话UP 后，再恢复成用户配置的时间间隔。一旦检测到 BFD 会话 Down，系统自动将本端的收包间隔和发包间隔调整为 3000 毫秒～5000 毫秒之间的一个随机值，当 BFD 会话的状态重新变为 Up后，再恢复成用户配置的时间间隔。如果想要详细了解该命令各参数的含义，可参考RFC5880。





范例 :

ZXROSNG(config-bfd-peer-peer)#time-negotiation interval 50 min-rx 50 multiplier 3ZXROSNG(config-bfd-peer-peer)#






相关命令 :

show running-config bfd 




## time-negotiation 


time-negotiation 




命令功能 :

该命令用于配置BFD 的检测参数，包括最小发包间隔，最小收包间隔，和检测倍数。在建立BFD会话时，可以根据网络状况和性能要求，调整设备的BFD 报文发送间隔、接收间隔以及本地检测倍数。 






命令模式 :

 LDP-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :



time-negotiation 
 interval 
 ＜tx-interval 
＞ min-rx 
 ＜rx-interval 
＞ multiplier 
 ＜detect-multiplier 
＞

no time-negotiation 








命令参数解释 :



参数|描述
---|---
＜tx-interval＞|作用：配置BFD实例检测报文期望的最小发包间隔。取值范围:$#35389448#$~$#35389449#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50。
＜rx-interval＞|作用：配置BFD实例检测报文期望的最小收包间隔。取值范围：$#35389450#$~$#35389451#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50 。
＜detect-multiplier＞|作用：配置BFD实例的本地检测倍数。取值范围：3-50 的数字。默认值：3。








缺省 :

interval缺省值为50min-rx缺省值为50multiplier缺省值为3





使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令可以在BFD接口模式、L2-BFD 模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在BFD接口模式下配置参数后，所有与该接口绑定的LINK-BFD（单跳BFD）都将使用该接口下配置的BFD 参数进行发包和检测。对该接口BFD 检测参数的调整，将改变所有与该接口绑定的LINK-BFD的检测参数。 在非BFD接口模式下配置BFD检测参数前，需要配置相应的BFD实例，然后进入具体的实例模式进行参数配置。例如：需要对某一L2-BFD实例进行BFD 检测参数调整时，首先要创建该L2-BFD 实例，然后进入L2-BFD模式进行BFD检测参数配置。BFD检测参数有默认值，当不对BFD检测参数配置时，BFD实例将以默认的检测参数进行发包和检测。为满足快速检测的需求，BFD 协议规定发送间隔和接收间隔的时间单位是微秒。但限于目前的设备处理能力，大部分厂商的设备在配置 BFD 时只能达到毫秒级，在进行内部处理时再转换到微秒级。为降低对系统资源的占用，在BFD会话UP之前，BFD以3000 毫秒～5000 毫秒之间的一个随机值来发送报文，当BFD 会话UP 后，再恢复成用户配置的时间间隔。一旦检测到 BFD 会话 Down，系统自动将本端的收包间隔和发包间隔调整为 3000 毫秒～5000 毫秒之间的一个随机值，当 BFD 会话的状态重新变为 Up后，再恢复成用户配置的时间间隔。如果想要详细了解该命令各参数的含义，可参考RFC5880。





范例 :

ZXROSNG(config-bfd-ldp-zte)#time-negotiation interval 50 min-rx 50 multiplier 3ZXROSNG(config-bfd-ldp-zte)#





相关命令 :

show running-config bfd 




## time-negotiation 


time-negotiation 




命令功能 :

该命令用于配置BFD 的检测参数，包括最小发包间隔，最小收包间隔，和检测倍数。在建立BFD会话时，可以根据网络状况和性能要求，调整设备的BFD 报文发送间隔、接收间隔以及本地检测倍数。





命令模式 :

 RSVP-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :


time-negotiation 
 interval 
 ＜tx-interval 
＞ min-rx 
 ＜rx-interval 
＞ multiplier 
 ＜detect-multiplier 
＞

no time-negotiation 








命令参数解释 :



参数|描述
---|---
＜tx-interval＞|作用：配置BFD实例检测报文期望的最小发包间隔。取值范围:$#35389448#$~$#35389449#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50。
＜rx-interval＞|作用：配置BFD实例检测报文期望的最小收包间隔。取值范围：$#35389450#$~$#35389451#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50 。
＜detect-multiplier＞|作用：配置BFD实例的本地检测倍数。取值范围：3-50 的数字。默认值：3。








缺省 :

interval缺省值为50min-rx缺省值为50multiplier缺省值为3






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令可以在BFD接口模式、L2-BFD 模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在BFD接口模式下配置参数后，所有与该接口绑定的LINK-BFD（单跳BFD）都将使用该接口下配置的BFD 参数进行发包和检测。对该接口BFD 检测参数的调整，将改变所有与该接口绑定的LINK-BFD的检测参数。 在非BFD接口模式下配置BFD检测参数前，需要配置相应的BFD实例，然后进入具体的实例模式进行参数配置。例如：需要对某一L2-BFD实例进行BFD 检测参数调整时，首先要创建该L2-BFD 实例，然后进入L2-BFD模式进行BFD检测参数配置。BFD检测参数有默认值，当不对BFD检测参数配置时，BFD实例将以默认的检测参数进行发包和检测。为满足快速检测的需求，BFD 协议规定发送间隔和接收间隔的时间单位是微秒。但限于目前的设备处理能力，大部分厂商的设备在配置 BFD 时只能达到毫秒级，在进行内部处理时再转换到微秒级。为降低对系统资源的占用，在BFD会话UP之前，BFD以3000 毫秒～5000 毫秒之间的一个随机值来发送报文，当BFD 会话UP 后，再恢复成用户配置的时间间隔。一旦检测到 BFD 会话 Down，系统自动将本端的收包间隔和发包间隔调整为 3000 毫秒～5000 毫秒之间的一个随机值，当 BFD 会话的状态重新变为 Up后，再恢复成用户配置的时间间隔。如果想要详细了解该命令各参数的含义，可参考RFC5880。





范例 :

ZXROSNG(config-bfd-rsvp-5)#time-negotiation interval 50 min-rx 50 multiplier 3ZXROSNG(config-bfd-rsvp-5)#






相关命令 :

show running-config bfd 




## time-negotiation 


time-negotiation 




命令功能 :

该命令用于配置BFD 的检测参数，包括最小发包间隔，最小收包间隔，和检测倍数。在建立BFD会话时，可以根据网络状况和性能要求，调整设备的BFD 报文发送间隔、接收间隔以及本地检测倍数。





命令模式 :

 PW-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :


time-negotiation 
 interval 
 ＜tx-interval 
＞ min-rx 
 ＜rx-interval 
＞ multiplier 
 ＜detect-multiplier 
＞

no time-negotiation 








命令参数解释 :



参数|描述
---|---
＜tx-interval＞|作用：配置BFD实例检测报文期望的最小发包间隔。取值范围:$#35389448#$~$#35389449#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50。
＜rx-interval＞|作用：配置BFD实例检测报文期望的最小收包间隔。取值范围：$#35389450#$~$#35389451#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50 。
＜detect-multiplier＞|作用：配置BFD实例的本地检测倍数。取值范围：3-50 的数字。默认值：3。








缺省 :

interval缺省值为50min-rx缺省值为50multiplier缺省值为3






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令可以在BFD接口模式、L2-BFD 模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在BFD接口模式下配置参数后，所有与该接口绑定的LINK-BFD（单跳BFD）都将使用该接口下配置的BFD 参数进行发包和检测。对该接口BFD 检测参数的调整，将改变所有与该接口绑定的LINK-BFD的检测参数。 在非BFD接口模式下配置BFD检测参数前，需要配置相应的BFD实例，然后进入具体的实例模式进行参数配置。例如：需要对某一L2-BFD实例进行BFD 检测参数调整时，首先要创建该L2-BFD 实例，然后进入L2-BFD模式进行BFD检测参数配置。BFD检测参数有默认值，当不对BFD检测参数配置时，BFD实例将以默认的检测参数进行发包和检测。为满足快速检测的需求，BFD 协议规定发送间隔和接收间隔的时间单位是微秒。但限于目前的设备处理能力，大部分厂商的设备在配置 BFD 时只能达到毫秒级，在进行内部处理时再转换到微秒级。为降低对系统资源的占用，在BFD会话UP之前，BFD以3000 毫秒～5000 毫秒之间的一个随机值来发送报文，当BFD 会话UP 后，再恢复成用户配置的时间间隔。一旦检测到 BFD 会话 Down，系统自动将本端的收包间隔和发包间隔调整为 3000 毫秒～5000 毫秒之间的一个随机值，当 BFD 会话的状态重新变为 Up后，再恢复成用户配置的时间间隔。如果想要详细了解该命令各参数的含义，可参考RFC5880。





范例 :

ZXROSNG(config-bfd-pw-pw)#time-negotiation interval 50 min-rx 50 multiplier 3ZXROSNG(config-bfd-pw-pw)#






相关命令 :

show running-config bfd 




## time-negotiation 


time-negotiation 




命令功能 :

该命令用于配置BFD的检测参数，包括最小发包间隔，最小收包间隔和检测倍数。在建立BFD会话时，可以根据网络状况和性能要求，调整设备的BFD报文发送间隔、接收间隔以及本地检测倍数。





命令模式 :

 L2-BFD实例模式  






命令默认权限级别 :

15 






命令格式 :


time-negotiation 
 interval 
 ＜tx-interval 
＞ min-rx 
 ＜rx-interval 
＞ multiplier 
 ＜detect-multiplier 
＞

no time-negotiation 








命令参数解释 :



参数|描述
---|---
＜tx-interval＞|作用：配置BFD实例检测报文期望的最小发包间隔。取值范围:$#35389448#$~$#35389449#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50。
＜rx-interval＞|作用：配置BFD实例检测报文期望的最小收包间隔。取值范围：$#35389450#$~$#35389451#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50 。
＜detect-multiplier＞|作用：配置BFD实例的本地检测倍数。取值范围：3-50 的数字。默认值：3。








缺省 :

interval缺省值为50min-rx缺省值为50multiplier缺省值为3






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令可以在BFD接口模式、L2-BFD 模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在BFD接口模式下配置参数后，所有与该接口绑定的LINK-BFD（单跳BFD）都将使用该接口下配置的BFD 参数进行发包和检测。对该接口BFD 检测参数的调整，将改变所有与该接口绑定的LINK-BFD的检测参数。 在非BFD接口模式下配置BFD检测参数前，需要配置相应的BFD实例，然后进入具体的实例模式进行参数配置。例如：需要对某一L2-BFD实例进行BFD 检测参数调整时，首先要创建该L2-BFD 实例，然后进入L2-BFD模式进行BFD检测参数配置。BFD检测参数有默认值，当不对BFD检测参数配置时，BFD实例将以默认的检测参数进行发包和检测。为满足快速检测的需求，BFD协议规定发送间隔和接收间隔的时间单位是微秒。但限于目前的设备处理能力，大部分厂商的设备在配置BFD时只能达到毫秒级，在进行内部处理时再转换到微秒级。为降低对系统资源的占用，在BFD会话UP之前，BFD以3000 毫秒～5000 毫秒之间的一个随机值来发送报文，当BFD会话UP 后，再恢复成用户配置的时间间隔。一旦检测到BFD会话Down，系统自动将本端的收包间隔和发包间隔调整为3000毫秒～5000 毫秒之间的一个随机值，当BFD会话的状态重新变为 Up后，再恢复成用户配置的时间间隔。如果想要详细了解该命令各参数的含义，可参考RFC5880。





范例 :

ZXROSNG(config-bfd-l2-l2)#time-negotiation interval 50 min-rx 50 multiplier 3ZXROSNG(config-bfd-l2-l2)#






相关命令 :

show running-config bfd 




## time-negotiation 


time-negotiation 




命令功能 :

该命令用于配置BFD的检测参数，包括最小发包间隔，最小收包间隔和检测倍数。在建立BFD会话时，可以根据网络状况和性能要求，调整设备的BFD报文发送间隔、接收间隔以及本地检测倍数。 






命令模式 :

 BFD接口模式  






命令默认权限级别 :

15 






命令格式 :



time-negotiation 
 interval 
 ＜tx-interval 
＞ min-rx 
 ＜rx-interval 
＞ multiplier 
 ＜detect-multiplier 
＞

no time-negotiation 








命令参数解释 :



参数|描述
---|---
＜tx-interval＞|作用：配置BFD实例检测报文期望的最小发包间隔。取值范围:$#35389448#$~$#35389449#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50。
＜rx-interval＞|作用：配置BFD实例检测报文期望的最小收包间隔。取值范围：$#35389450#$~$#35389451#$的数字，单位为毫秒，由于该范围由设备性能参数控制，不同的设备取值范围有所不同。默认值：50 。
＜detect-multiplier＞|作用：配置BFD实例的本地检测倍数。取值范围：3-50 的数字。默认值：3。








缺省 :

interval缺省值为50min-rx缺省值为50multiplier缺省值为3






使用说明 :

有拥有管理员权限的操作员可以使用这条命令。该命令可以在BFD接口模式、L2-BFD 模式、LDP-BFD模式、PEER-BFD模式、PW-BFD模式、RSVP-BFD模式下执行。在BFD接口模式下配置参数后，所有与该接口绑定的LINK-BFD（单跳BFD）都将使用该接口下配置的BFD参数进行发包和检测。对该接口BFD检测参数的调整，将改变所有与该接口绑定的LINK-BFD的检测参数。 在非BFD接口模式下配置BFD检测参数前，需要配置相应的BFD实例，然后进入具体的实例模式进行参数配置。例如：需要对某一L2-BFD实例进行BF 检测参数调整时，首先要创建该L2-BFD实例，然后进入L2-BFD模式进行BFD检测参数配置。BFD检测参数有默认值，当不对BFD检测参数配置时，BFD实例将以默认的检测参数进行发包和检测。为满足快速检测的需求，BFD协议规定发送间隔和接收间隔的时间单位是微秒。但限于目前的设备处理能力，大部分厂商的设备在配置BFD时只能达到毫秒级，在进行内部处理时再转换到微秒级。为降低对系统资源的占用，在BFD会话UP之前，BFD以3000毫秒～5000毫秒之间的一个随机值来发送报文，当BFD会话UP后，再恢复成用户配置的时间间隔。一旦检测到BFD会话Down，系统自动将本端的收包间隔和发包间隔调整为3000毫秒～5000毫秒之间的一个随机值，当BFD会话的状态重新变为Up后，再恢复成用户配置的时间间隔。如果想要详细了解该命令各参数的含义，可参考RFC5880。






范例 :

ZXROSNG(config-bfd-if-gei-0/1/0/1)#time-negotiation interval 50 min-rx 50 multiplier 3 






相关命令 :

show running-config bfd 




# PING DETECT配置命令 
## detect-group 


detect-group 




命令功能 :

该命令工作于全局配置模式，用来配置一个检测组（Detect-Group）。每个检测组中可以配置多个检测列表（Detect-List）。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


detect-group 
  ＜group-number 
＞
no detect-group 
  ＜group-number 
＞
				






命令参数解释 :



参数|描述
---|---
＜group-number＞|检测组号，范围：1-$#34209793#$








缺省 :

无 






使用说明 :

具有管理员权限的操作员可以使用这条命令。该命令执行后，进入检测组配置模式，可进行检测组参数配置或组内检测列表配置等。没有配置检测列表的检测组，不具备检测能力。因此无法响应链路的故障。






范例 :

配置检测组号为1 。1. 进入1号检测组配置模式：ZXUN#configure terminalEnter configuration commands, one per line. End with CTRL/Z.ZXUN(config)#detect-group 1ZXUN(config-detect-group-1)#
2. 检查配置结果：ZXUN(config-detect-group-1)#show running-config ping-detect!<ping-detect>detect-group 1$!</ping-detect>ZXUN(config-detect-group-1)#






相关命令 :

show running-config ping-detect 




## interval 


interval 




命令功能 :

配置每次探测连续发包的间隔 






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :



interval 
  ＜packet interval 
＞

no interval 








命令参数解释 :



参数|描述
---|---
＜packet interval＞|每次探测连续发包的间隔，单位为100ms，范围1-50








缺省 :

1 






使用说明 :

单位为100ms，根据检测条目数和设备性能调整该参数以达到较好的检测效果 






范例 :

ZXROSNG(config)#ZXROSNG(config)#detect-group 1ZXROSNG(config-detect-group-1)# interval 10






相关命令 :

无 




## item 


item 




命令功能 :

配置DETCT LIST的具体检测条目。 






命令模式 :

 检测组list模式  






命令默认权限级别 :

15 






命令格式 :


item 
  ＜item-number 
＞ [vrf 
 ＜vrf-name 
＞] {＜ip-address 
＞ [＜ip-address 
＞ interface 
 ＜interface-name 
＞] [source 
 ＜ip-address 
＞]|＜ipv6-address 
＞ [interface 
 ＜interface-name 
＞] [source 
 ＜ipv6-address 
＞]}
no item 
  ＜item-number 
＞
				






命令参数解释 :



参数|描述
---|---
＜item-number＞|检测条目号，范围 1-10
＜vrf-name＞|vrf 名称，1-32个字符串
＜ip-address＞|检测目的地址
＜ip-address＞|检测目的地址
＜interface-name＞|指定检测条目的出接口
＜ip-address＞|检测目的地址
＜ipv6-address＞|V6 检测的目的地址
＜interface-name＞|指定检测条目的出接口
＜ipv6-address＞|V6 检测的目的地址








缺省 :

无 






使用说明 :

item命令设置检测组的检测条目，item号范围：1-10。该条目中的VRF指定特定的VPN，最大长度32。该条目中的目的IP地址为用户需要检测的目的IP地址。该条目中的下一跳地址和出接口为目的IP地址路由表项中的出接口和下一跳，这两个选项必须一起指定。检测条目后接的目的地址称之为item，同一个检测条目下最多可以配置10个不同的item.





范例 :

在检测组1内，配置两个检测列表，每个检测列表内分别配置两个检测项。1. 配置检测组号为1：ZXROSNG#configure terminalEnter configuration commands, one per line. End with CTRL/Z.ZXROSNG(config)#detect-group 1ZXROSNG(config-detect-group-1)#2. 在1号检测组下配置检测列表1，在列表1下配置条目1和条目2ZXROSNG(config-detect-group-1)#list 1ZXROSNG(config-detect-group-1-list-1)#ZXROSNG(config-detect-group-1-list-1)#item 1 10.1.1.1ZXROSNG(config-detect-group-1-list-1)#item 2 20.1.1.1ZXROSNG(config-detect-group-1-list-1)#3. 在1号检测组下配置检测列表2，在列表2下配置条目1和条目2ZXROSNG(config-detect-group-1)#list 2ZXROSNG(config-detect-group-1-list-2)#item 1 30.1.1.1ZXROSNG(config-detect-group-1-list-2)#item 2 40.1.1.1ZXROSNG(config-detect-group-1-list-2)#






相关命令 :

show running-config ping-detect 




## list 


list 




命令功能 :

配置检测组下的一个检测列表，并进入检测组List配置模式。在List配置模式下继续配置具体的检测项。 






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :


list 
  ＜list-number 
＞
no list 
  ＜list-number 
＞
				






命令参数解释 :



参数|描述
---|---
＜list-number＞|检测条目号，范围：1-10








缺省 :

无 






使用说明 :

list命令创建一个list，进入检测组List模式，每个组最多可以配置10个检测List。拥有管理员权限的操作员可以使用这条命令。该命令只能在检测组配置模式下执行。在执行该命令之前，需要配置Detect-Group。可以为检测列表中的检测项配置一个逻辑“与”或逻辑“或”关系。当检测项间配置为逻辑“与”关系时，当列表内所有检测项的连通性状态都可达时，整个检测列表的连通性状态才可达。相反，当配置为逻辑“或”关系时，只要有一个检测项的连通性状态可达，整个检测列表的连通性状态就可达。具体配置过程可参考list下option 命令。






范例 :

ZXROSNG(config-detect-group-1)#list 1ZXROSNG(config-detect-group-1-list-1)#





相关命令 :

show running-config ping-detect



## loop-time 


loop-time 




命令功能 :

该命令工作于ping-detect模式，用来配置检测组内检测项的循环检测时间，即系统周期性发起ping检测请求的时间间隔。链路检测每隔一个循环检测周期，就会发起一次探测，一旦链路发生故障，就能及时检测到该故障。当需要修改循环检测时间时，使用该命令。此参数仅在cc模式有效。 






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :



loop-time 
  ＜loop-time 
＞

no loop-time 








命令参数解释 :



参数|描述
---|---
＜loop-time＞|配置检测组的循环检测时间，范围：2-86400，单位：秒








缺省 :

loop-time缺省值为15 






使用说明 :

loop-time 命令设置检测组的循环检测时间，即每隔该时间就向PING模块发起检测请求。单位秒，默认值是15秒。该值有约束条件，即：loop-time>=retry-times*(timeout+1)no loop-time恢复为默认值15秒。不满足该条件时，报提示类错误，但是配置能配下去，内部动态调整loop-time=retry-times*(timeout+1)此参数仅在cc模式有效，lm模式下每个item自己控制，结束2s后发起下次探测。






范例 :

配置循环检测时间为20秒ZXROSNG(config-detect-group-1)#loop-time 20ZXROSNG(config-detect-group-1)#





相关命令 :

show running-config ping-detect 




## loss-threshold 


loss-threshold 




命令功能 :

告警阈值配置，丢包率达到严重阈值时产生严重告警，丢包率达到一般阈值时产生一般告警。 






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :



loss-threshold 
 medium 
 ＜medium_loss 
＞ high 
 ＜high_loss 
＞

no loss-threshold 








命令参数解释 :



参数|描述
---|---
＜medium_loss＞|一般告警阈值，范围：1-99
＜high_loss＞|严重告警阈值，范围：2-100








缺省 :

medium 默认值为 10， high 默认值为 20 






使用说明 :

1、进入ping-detect模式，可以使用这个命令配置告警阈值2、使用no loss-threshold命令，可清除用户的配置。恢复为默认值





范例 :

ZXROSNG(config)#ZXROSNG(config)#detect-group 1ZXROSNG(config-detect-group-1)# loss-threshold medium 88 high 99ZXROSNG(config-detect-group-1)# no loss-threshold






相关命令 :

无 




## mode 


mode 




命令功能 :

配置检测类型 






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :



mode 
  {cc 
|lm-cc 
}







命令参数解释 :



参数|描述
---|---
cc|通断检测模式，无丢包统计和告警功能
lm-cc|除通断检测外，还进行丢包统计和告警功能








缺省 :

cc 






使用说明 :

1、进入ping-detect模式，可以使用这个命令配置检测类型2、使用show命令可以看到检测类型是否被配置上






范例 :

ZXROSNG(config)#detect-group 1ZXROSNG(config-detect-group-1)# mode lm-ccZXROSNG(config-detect-group-1)#mode ccZXROSNG(config-detect-group-1)#






相关命令 :

无 




## option 


option 




命令功能 :

用来配置同一个检测组内检测列表间的逻辑关系。当需要修改检测列表间逻辑关系时，可以使用该命令。配置为逻辑“或”，则检测组内只要有一个检测列表的连通性状态为可达，则整个检测组的连通状态就为可达；配置为逻辑“与”，则检测组内只有所有检测列表的连通性状态为可达，整个检测组的连通状态才为可达。






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :


option 
  {or 
|and 
}

no option 








命令参数解释 :



参数|描述
---|---
or|同一检测列表内检测条目之间的关系为“或”，任一检测条目通就算检测列表通
and|同一检测列表内检测条目之间的关系为“与”，所有检测条目通才算列表通








缺省 :

and为缺省值 






使用说明 :

option 命令设置检测组内各个检测列表之间的关系，默认值是and。当配置组的选项为and时，需要组内的所有列表全通的情况下，才算是组通；而当配置成or只要组内有一个列表通了则就认为组通。no option恢复为默认值and。





范例 :

ZXROSNG(config-detect-group-1)#option andZXROSNG(config-detect-group-1)#option or





相关命令 :

show running-config ping-detect 




## option 


option 




命令功能 :

配置检测列表内不同检测条目之间的逻辑关系。配置为逻辑“或”，则检测组列表内只要有一个检测条目的连通性状态为可达，则整个检测列表的连通状态就为可达；配置为逻辑“与”，则检测列表内只有所有检测条目的连通性状态为可达，整个检测列表的连通状态才为可达。 






命令模式 :

 检测组list模式  






命令默认权限级别 :

15 






命令格式 :



option 
  {or 
|and 
}

no option 








命令参数解释 :



参数|描述
---|---
or|同一检测列表内检测条目之间的关系为“或”，任一检测条目通就算检测列表通
and|同一检测列表内检测条目之间的关系为“与”，所有检测条目通才算列表通








缺省 :

默认关系为“与”。 






使用说明 :

option 命令设置检测列表内各个检测条目之间的关系，默认值是and。当配置某检测列表的选项为and时，需要改列表内的所有条目全通的情况下，才算是通；而当配置成or只要列表内有一个条目通了则就认为通。no option恢复为默认值and。





范例 :

ZXROSNG(config-detect-group-1-list-1)#option and ZXROSNG(config-detect-group-1-list-1)#






相关命令 :

show running-config ping-detect 




## retry-times 


retry-times 




命令功能 :

用来配置系统发送ping检测请求失败后的重传次数。当系统忙或其它原因导致ping检测请求失败时，需要重传该请求。最大限度降低由于非链路故障导致的故障误报的情况。当需要修改重传次数时，可以使用该命令。






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :


retry-times 
  ＜retry-time 
＞

no retry-times 








命令参数解释 :



参数|描述
---|---
＜retry-time＞|配置ping请求重传次数。范围：1-100








缺省 :

retry-times的缺省值为2 






使用说明 :

对于cc模式（仅检测通断），retry-times命令设置检测组的失败重传次数，重试完retry-times后，如果还是失败，则认为链路故障；对于lm-cc模式（检测通断，同时计算丢包率），retry-times命令表示每次探测的发包数目，发完retry-times后，只要有一个包成功就认为链路正常，所以包都不成功才认为链路故障，同时根据收到的应答数和retry-times的比例计算丢包率。no retry-times恢复为默认值2次。





范例 :

ZXROSNG(config-detect-group-1)#retry-times 2ZXROSNG(config-detect-group-1)#no retry-times






相关命令 :

show running-config ping-detect 




## show ping-detect brief 


show ping-detect brief 




命令功能 :

显示侦测组的简要信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ping-detect brief 
  [[group 
 ＜group-number 
＞]] 







命令参数解释 :



参数|描述
---|---
＜group-number＞|检测组ID，范围：1-$#34209793#$








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show ping-detect briefGroup: 100/110(Configured/Max)List:  0/1100(Configured/Max)Item:  0/2000(Configured/Max)==============================================================================ID   State      Mode    Option   List-count   Item-count1    Unknown    CC      And      0            02    Unknown    CC      And      0            03    Unknown    CC      And      0            04    Unknown    CC      And      0            05    Unknown    CC      And      0            06    Unknown    CC      And      0            07    Unknown    CC      And      0            0






相关命令 :

无 




## show ping-detect detail 


show ping-detect detail 




命令功能 :

显示侦测组的详细信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ping-detect detail 
 group 
 {all 
|＜group-number 
＞ [list 
 {all 
|＜list-number 
＞ [item 
 {all 
|＜item-number 
＞}]}]} 







命令参数解释 :



参数|描述
---|---
all|显示某个组的某个list的所有item的配置状态详细信息
＜group-number＞|检测组ID，范围：1-$#34209793#$
all|显示某个组的某个list的所有item的配置状态详细信息
＜list-number＞|List ID，范围：1-10
all|显示某个组的某个list的所有item的配置状态详细信息
＜item-number＞|Item ID，范围：1-10








缺省 :

无 






使用说明 :

1、使用该命令可以分别看到几个层次上的详细配置状态信息2、使用show ping-detect detail group all| group_id命令，可以显示某个或是所有组的详细配置状态信息及其list状态信息3、使用 show ping-detect detail group group_id list all |list_id命令，可以显示某个组下某个或是所有list的详细配置状态信息及其item状态信息4、使用show ping-detect detail group group_id list list_id item all|item_id命令，可以显示某个组下某个list的某个或是所有item的详细配置状态信息






范例 :

显示某个组的详细配置状态信息及list状态信息ZXROSNG(config-detect-group-1)#show ping-detect detail group 1Group 1 Loop Time:        15/15(configured/actual) Loss-threshold:   medium 10 high 20 Mode:             CC Retry Times:      2 Timeout:          2 Option:           And State:            Unknown List 1            State: Unknown List 2            State: Unknown显示某个组的所有list的详细配置状态信息及list状态信息ZXROSNG(config-detect-group-1)#show ping-detect detail group 1 list allGroup 1   List 1 Option:           And State:            Down
 Item 1            State: DownGroup 1   List 2 Option:           And State:            UnknownGroup 1   List 4 Option:           And State:            Down
 Item 2            State: DownGroup 1   List 5 Option:           And State:            Down
 Item 3            State: Down显示某个组的某个list的所有item详细配置状态信息ZXROSNG#show ping-detect detail group 1 list 2 item allGroup 1   List 2   Item 3 Destination:      10.10.10.3 VRF Name: Interface:        --- Source:           --- Next Hop:         --- State:            Down
Group 1   List 2   Item 5 Destination:      10.10.10.5 VRF Name: Interface:        --- Source:           --- Next Hop:         --- State:            Down
Group 1   List 2   Item 7 Destination:      10.10.10.7 VRF Name: Interface:        --- Source:           --- Next Hop:         --- State:            Down






相关命令 :

无 




## size 


size 




命令功能 :

配置报文大小 






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :



size 
  ＜pkt_size 
＞

no size 








命令参数解释 :



参数|描述
---|---
＜pkt_size＞|报文大小的范围，默认100，范围：36-8192








缺省 :

100 






使用说明 :

1、进入ping-detect模式，可以使用这个命令配置报文大小。2、当目的地址是IPV6地址时，如果配置的size小于64，则实际生效的值为64；3、使用no size命令，可清除用户的配置。no 命令生效后size恢复为默认值100






范例 :

ZXROSNG(config)#ZXROSNG(config)#detect-group 1ZXROSNG(config-detect-group-1)#size 88ZXROSNG(config-detect-group-1)#no size






相关命令 :

无 




## time-out 


time-out 




命令功能 :

该命令工作于ping-detect模式，用来配置检测组发起ping检测请求的超时时间。如果在超时内未收到ping请求的应答消息，检测组将根据配置的重传次数，再次发送请求。当需要修改超时时间时，使用该命令。 






命令模式 :

 ping-detect模式  






命令默认权限级别 :

15 






命令格式 :



time-out 
  ＜timeout 
＞

no time-out 








命令参数解释 :



参数|描述
---|---
＜timeout＞|设置发起ping检测请求的超时时间，单位为秒。取值范围： 1~20 秒。默认值：2 秒。








缺省 :

time-out缺省值为2秒 






使用说明 :

time-out命令设置检测组传递给PING模块的超时时间，默认值为2秒。no time-out恢复为默认值2秒。





范例 :

ZXROSNG(config-detect-group-1)#time-out 2ZXROSNG(config-detect-group-1)#





相关命令 :

show running-config ping-detect 




# 业务可靠性管理配置命令 
## inactive-number 


inactive-number 




命令功能 :

该命令用来配置检测组状态的计算策略，当配置检测组时用该命令来确定检测组状态产生方法。 






命令模式 :

 SAMGR管理组模式  






命令默认权限级别 :

15 






命令格式 :



inactive-number 
  ＜inactive-number 
＞

no inactive-number 








命令参数解释 :



参数|描述
---|---
＜inactive-number＞|作用：配置检测组的策略值范围：1-10默认值：不配置，检测组中配置的所有检测为down时检测组状态为down








缺省 :

当不配置该命令时，检测组的状态由检测组下的所有检测成员确定，组里面的所有成员down，group组down。因为track成员有unknow状态，如果组里面的成员是unknown的话，不满足所有都down，group也是UP的。






使用说明 :

配置检测组策略值，策略值是指的检测组下成员检测报状态down的个数，如果检测组下的成员检测报down个数达到所配置检测组策略值。检测组状态转换为down。检测组默认状态为up。检测组默认策略为不配置策略值。当检测组成员检测状态都为down时检测组状态转换为down






范例 :

ZXR(config-samgr-group-1)#inactive-number 1  






相关命令 :

track-group 




## sa-bind 


sa-bind 




命令功能 :

该命令是绑定关系配置命令，当存在检测状态要传递到指定检测时配置该命令。 






命令模式 :

 SAMGR模式  






命令默认权限级别 :

15 






命令格式 :


sa-bind 
 track 
 ＜passive-track-name 
＞ to 
 {track 
 ＜active-track-name 
＞|track-group 
 ＜active-track-group-name 
＞}
no sa-bind 
 track 
 ＜passive-track-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜passive-track-name＞|作用：用于指定被动检测对象的名称。取值范围：长度1-31个字符。默认值：无。
＜active-track-name＞|作用：用于指定主动检测对象的名称。取值范围：长度1-31个字符。默认值：无。
＜active-track-group-name＞|作用：用于指定主动检测组的名称。取值范围：长度1-31个字符。默认值：无。








缺省 :

无 






使用说明 :

当检测状态需要发生传递时，配置该命令。状态支持一对多的传递，即多个被动检测可以接收一个主动检测的状态传递；主动检测可以向多个被动检测进行状态传递；当前环境已存在oam maping配置时，不能进行绑定配置；支持检测组向检测对象传递，已经成为检测组成员的检测，不能与该检测组建立绑定。






范例 :

ZXROSNG(config-samgr)#sa-bind track aaa to track bbb 






相关命令 :

show samgr track show samgr track-group



## samgr 


samgr 




命令功能 :

该命令是模式跳转命令，用于进入SAMGR配置模式。当需要进行SAMGR配置时，使用该命令。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



samgr 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

必须先进入SAMGR模式，才能进行SAGMR命令相关配置。该命令执行后，将进入SAMGR模式进行检测和检测组的相关配置。






范例 :

ZXROSNG(config)#samgrZXROSNG(config-samgr)#





相关命令 :

无 




## show samgr bind track 


show samgr bind track 




命令功能 :

显示当前配置检测下的绑定关系，当配置了绑定关系时可以使用该命令查看指定检测的绑定关系。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show samgr bind track 
  [＜CurrentName 
＞] 







命令参数解释 :



参数|描述
---|---
＜CurrentName＞|作用：用于指定检测的名称。取值范围：长度1-31个字符。默认值：不指定检测名称。








缺省 :

不指定检测名称时则显示当前环境下全部检测存在的绑定关系。 






使用说明 :

配置完检测组的绑定关系后使用该命令检测配置情况。 






范例 :

ZXROSNG(config-samgr)#show samgr bind track  Current track name  : sqa  Passive track number: 1       Track name: bfd                               -------------------------------  Current track name  : bfd  Active  track       : sqa  Passive track number: 0ZXROSNG(config-samgr)#show samgr bind track bfd  Current track name  : bfd  Active  track       : sqa  Passive track number: 0输出参数说明参数                       描述Current track name      当前检测名称Active  track           主动检测名称Passive track number    被动检测个数Track name              被动检测个数名称






相关命令 :

show samgr bind track-group [＜CurrentName＞] 




## show samgr brief 


show samgr brief 




命令功能 :

显示当前配置检测的简要信息，当配置了检测时可以使用该命令查看指定检测组简要信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show samgr brief 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

显示当前配置所有检测的简要信息。





范例 :

ZXROSNG(config-samgr)#show samgr briefThe total of track at this Router is 1. =================================================================Track-name                    Detect-type         App-num      State aaa                           link-bfd             0           unknown





相关命令 :

无 




## show samgr track 


show samgr track 




命令功能 :

显示当前配置检测的详细信息，当配置了检测时可以使用该命令查看指定检测详细信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show samgr track 
  [＜track-name 
＞ [verbose 
]] 







命令参数解释 :



参数|描述
---|---
＜track-name＞|作用：用于指定检测的名称。取值范围：长度1-31个字符。默认值：不指定检测名称。
verbose|作用：显示指定检测的状态变化情况记录。取值范围：无。默认值：无。








缺省 :

无 






使用说明 :

显示配置的检测详细信息。当不指定检测名称时显示当前所有配置的检测详细信息。当指定检测名称时显示指定的检测详细信息。当指定检测名称同时带有verbose参数时显示指定的检测状态变化情况。






范例 :

ZXROSNG(config-samgr)#show samgr track aaaTrack name is aaa    Detect type  : peer-bfd    Track parameter      Local IP: 1.1.1.1  Remote IP: 1.1.1.3  Vrf name: zte    App number   : 0    Active track : none    Passive track: none    Track state  : unknow    State change : 0 state changes, last state change 00-00-00 00:00:00输出参数说明参数               描述Detect-type      检测类型Track parameter  检测参数App number       协议定阅次数Active track     绑定的主动检测    Passive track     绑定的被动检测Track state      检测对象名称State change     状态改变次数与最后一次改变时间ZXROSNG(config)#show samgr track sqa verbose Track name is sqaState change record:    old state         new state      change time1   unknown        local down      2011-07-19 02:57:282   local down      up             2011-07-19 03:05:163   up             local down      2011-07-19 03:06:244   local down      up             2011-07-19 03:08:005   up             local down      2011-07-19 03:08:13输出参数说明参数               描述old state        检测旧状态new state        检测新状态change time      检测状态改变时间






相关命令 :

无 




## track &amp;lt;mid&amp;gt; bfd 


track <mid> bfd 




命令功能 :

该命令是BFD类型检测配置命令，当有协议关注BFD状态时配置该命令。 






命令模式 :

 SAMGR模式  






命令默认权限级别 :

15 






命令格式 :



track  
 ＜track-name 
＞ bfd 
 session 
 ＜bfd-session-name 
＞







命令参数解释 :



参数|描述
---|---
＜track-name＞|作用：用于指定检测对象的名称。取值范围：长度1-31个字符。默认值：无。
＜bfd-session-name＞|作用：用于指定BFD检测名称。取值范围：长度1-32个字符。默认值：无。








缺省 :

无 






使用说明 :

当协议关注BFD状态时，在SAMGR模式下配置该命令，在协议下配置订阅该检测。当BFD状态发生变化时，BFD状态通知到协议。





范例 :

ZXROSNG(config-samgr)# track ddd bfd session bfdname 






相关命令 :

show samgr briefshow samgr track




## track &amp;lt;mid&amp;gt; ping-detect 


track <mid> ping-detect 




命令功能 :

该命令是ping detect类型检测配置命令，当有协议关注ping detect状态时配置该命令。 






命令模式 :

 SAMGR模式  






命令默认权限级别 :

15 






命令格式 :



track  
 ＜track-name 
＞ ping-detect 
 group 
 ＜group-number 
＞







命令参数解释 :



参数|描述
---|---
＜track-name＞|作用：用于指定检测对象的名称。取值范围：长度1-31个字符。默认值：无。
＜group-number＞|作用：用于指定Ping检测的组号。取值范围：1-$#34209793#$。默认值：无。








缺省 :

无 






使用说明 :

当协议关注ping detect状态时，在SAMGR模式下配置该命令，在协议下配置订阅该检测。当ping detect状态发生变化时，ping detect状态通知到协议。 






范例 :

ZXROSNG(config-samgr)#track aaa ping-detect group 1 






相关命令 :

show samgr briefshow samgr track



