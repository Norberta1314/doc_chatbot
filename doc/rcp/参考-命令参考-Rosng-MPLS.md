# APS配置命令 
## active-state 

active-state 
命令功能 : 
配置线性保护的APS运行状态。 
命令模式 : 
 APS端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
active-state 
  {pause 
|restore-run 
}
命令参数解释 : 
参数|描述
---|---
pause|APS暂停状态
restore-run|APS恢复运行状态
缺省 : 
restore-run 
使用说明 : 
在APS端口保护模式下执行改命令，设置该端口保护APS实例的运行状态。默认为restore-run。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)# port-group  1 1ZXROSNG(config-aps-linear-protect-portgroup-11)#active-state pause ZXROSNG(config-aps-linear-protect-portgroup-11)#
相关命令 : 
相关SHOW命令：show aps linear-protect port-group 11
## active-state 

active-state 
命令功能 : 
配置线性保护的APS运行状态。 
命令模式 : 
 APS OTN端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
active-state 
  {pause 
|restore-run 
}
命令参数解释 : 
参数|描述
---|---
pause|APS暂停状态
restore-run|APS恢复运行状态
缺省 : 
restore-run 
使用说明 : 
在APS OTN端口保护模式下执行命令，设置该端口保护APS实例的运行状态。默认为restore-run。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps)#port-group otn 11ZXROSNG(config-aps-linear-protect-portgroup-otn-11)#active-state pause 
相关命令 : 
相关SHOW命令：show aps linear-protect port-group otn
## active-state 

active-state 
命令功能 : 
配置线性保护的APS运行状态。 
命令模式 : 
 APS FlexE端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
active-state 
  {pause 
|restore-run 
}
命令参数解释 : 
参数|描述
---|---
pause|APS暂停状态
restore-run|APS恢复运行状态
缺省 : 
restore-run 
使用说明 : 
在APS FlexE端口保护模式下执行命令，设置该端口保护APS实例的运行状态。默认为restore-run。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps)#port-group flexe 11ZXROSNG(config-aps-linear-protect-portgroup-flexe-11)#active-state pause 
相关命令 : 
相关SHOW命令：show aps linear-protect port-group flexe 
## active-state 

active-state 
命令功能 : 
配置线性保护的APS运行状态。 
命令模式 : 
 APS隧道保护模式  
命令默认权限级别 : 
15 
命令格式 : 
active-state 
  {pause 
|restore-run 
}
命令参数解释 : 
参数|描述
---|---
pause|APS暂停状态
restore-run|APS恢复运行状态
缺省 : 
restore-run 
使用说明 : 
在APS隧道保护模式下执行改命令，设置该隧道保护APS实例的运行状态。默认为restore-run。 
范例 : 
ZXROSNG(config-aps-linear-protect-tunnelgroup11)#active-state pause ZXROSNG(config-aps-linear-protect-tunnelgroup11)#
相关命令 : 
相关SHOW命令：show aps linear-protect tunnel-group 11
## active-state 

active-state 
命令功能 : 
配置线性保护的APS运行状态。 
命令模式 : 
 APS伪线保护模式  
命令默认权限级别 : 
15 
命令格式 : 
active-state 
  {pause 
|restore-run 
}
命令参数解释 : 
参数|描述
---|---
pause|APS暂停状态
restore-run|APS恢复运行状态
缺省 : 
restore-run 
使用说明 : 
在APS伪线保护模式下执行改命令，设置该伪线保护APS实例的运行状态。默认为restore-run。 
范例 : 
ZXROSNG(config-aps-linear-protect-pwprotector-pw1)#active-state pause ZXROSNG(config-aps-linear-protect-pwprotector-pw1)#
相关命令 : 
相关SHOW命令：show aps linear-protect tunnel-group 11
## active-state 

active-state 
命令功能 : 
配置线性保护的APS运行状态。 
命令模式 : 
 APS multicast端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
active-state 
  {pause 
|restore-run 
}
命令参数解释 : 
参数|描述
---|---
pause|APS暂停状态
restore-run|APS恢复运行状态
缺省 : 
restore-run 
使用说明 : 
在APS  multicast端口保护模式下执行命令，设置该端口保护APS实例的运行状态。默认为restore-run。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group multicast 11ZXROSNG(config-aps-linear-protect-portgroup-mc-11)#active-state pause 
相关命令 : 
相关SHOW命令：show aps linear-protect port-group multicast 
## aps 

aps 
命令功能 : 
跳转到APS全局模式下。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
aps 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
在配置模式下，配置改命令，跳转到APS全局模式 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#
相关命令 : 
无 
## debug linear-aps alarm port-group ether-service 

debug linear-aps alarm port-group ether-service 
命令功能 : 
打开某个以太端口APS实例的告警通知DEBUG开关。相关的no命令是关闭某个以太端口线性APS实例的告警通知DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps alarm port-group ether-service 
  ＜group-id 
＞
no debug linear-aps alarm port-group ether-service 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组号，范围为1~$#67305528#$
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用 terminal monitor后才能看到DEBUG信息；2、当指定的某个以太端口APS实例不存在时，报错；3、使用该命令，打开某个以太端口APS实例的告警通知DEBUG开关，此时可以看到告警通知动态信息；相关的no命令是关闭某个以太端口APS实例的告警通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps alarm port-group ether-service 1Linear APS debugging receiving alarm message has been turned on
相关命令 : 
show debug linear-aps 
## debug linear-aps alarm port-group flexe 

debug linear-aps alarm port-group flexe 
命令功能 : 
打开某个FlexE端口APS实例的告警通知DEBUG开关。相关的no命令是关闭某个FlexE端口APS实例的告警通知DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps alarm port-group flexe 
  ＜group-id 
＞
no debug linear-aps alarm port-group flexe 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组号，范围为1~8192
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用 terminal monitor后才能看到DEBUG信息；2、当指定的某个FlexE端口APS实例不存在时，报错；3、使用该命令，打开某个FlexE端口APS实例的告警通知DEBUG开关，此时可以看到告警通知动态信息；相关的no命令是关闭某个FlexE端口APS实例的告警通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps alarm port-group flexe 1Linear APS debugging receiving alarm message has been turned on
相关命令 : 
show debug linear-aps 
## debug linear-aps alarm port-group otn 

debug linear-aps alarm port-group otn 
命令功能 : 
打开某个OTN端口APS实例的告警通知DEBUG开关。相关的no命令是关闭某个OTN端口APS实例的告警通知DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps alarm port-group otn 
  ＜group-id 
＞
no debug linear-aps alarm port-group otn 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组号，范围为1~$#67305527#$
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用 terminal monitor后才能看到DEBUG信息；2、当指定的某个OTN端口APS实例不存在时，报错；3、使用该命令，打开某个OTN端口APS实例的告警通知DEBUG开关，此时可以看到告警通知动态信息；相关的no命令是关闭某个OTN端口APS实例的告警通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps alarm port-group otn 1Linear APS debugging receiving alarm message has been turned on
相关命令 : 
show debug linear-aps 
## debug linear-aps alarm port-group 

debug linear-aps alarm port-group 
命令功能 : 
打开某个MSP端口APS实例的告警通知DEBUG开关。相关的no命令是关闭某个MSP端口APS实例的告警通知DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps alarm port-group 
  [msp 
 ] ＜group-id 
＞
no debug linear-aps alarm port-group 
  [msp 
 ] ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组号，范围为1~256
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用 terminal monitor后才能看到DEBUG信息；2、当指定的某个线性MSP端口APS实例不存在时，报错；3、使用该命令，打开某个MSP端口APS实例的告警通知DEBUG开关，此时可以看到告警通知动态信息；相关的no命令是关闭某个MSP端口APS实例的告警通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps alarm port-group 1Linear APS debugging receiving alarm message has been turned on
ZXROSNG#debug linear-aps alarm port-group msp 1Linear APS debugging receiving alarm message has been turned on
相关命令 : 
show debug linear-aps 
## debug linear-aps alarm 

debug linear-aps alarm 
命令功能 : 
打开所有或是某个线性APS实例的告警通知DEBUG开关。相关的no命令是关闭所有或是某个线性APS实例的告警通知DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps alarm 
  [{lsp-group 
 ＜group-id 
＞|mc-selection 
 ＜mc-selection 
＞|pw-protector 
 ＜pwg-name 
＞|tunnel-group 
 ＜group-id 
＞|ac-pw-protector 
 ＜pwg-name 
＞}]
no debug linear-aps alarm 
  [{lsp-group 
 ＜group-id 
＞|mc-selection 
 ＜mc-selection 
＞|pw-protector 
 ＜pwg-name 
＞|tunnel-group 
 ＜group-id 
＞|ac-pw-protector 
 ＜pwg-name 
＞}]
				
命令参数解释 : 
参数|描述
---|---
lsp-group|LSP保护组的告警通知DEBUG开关
＜group-id＞|隧道保护组ID，范围为1~$#67305513#$
mc-selection|mc-selection保护组的告警通知DEBUG开关
＜mc-selection＞|mc-selection保护组的保护组名，如pw1
pw-protector|伪线保护组的告警通知DEBUG开关
＜pwg-name＞|ac保护组名，如pw1
tunnel-group|隧道保护组的告警通知DEBUG开关
＜group-id＞|隧道保护组ID，范围为1~$#67305513#$
ac-pw-protector|ac保护组的告警通知DEBUG开关
＜pwg-name＞|ac保护组名，如pw1
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用terminal monitor后才能看到DEBUG信息；2、当指定的某个线性APS实例不存在时，报错；3、使用该命令，打开所有或是某个线性APS实例的告警通知DEBUG开关，此时可以看到告警通知动态信息；相关的no命令是关闭所有或是某个线性APS实例的告警通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps alarm pw-protector pw1Linear APS debugging receiving alarm message has been turned on
相关命令 : 
show debug linear-aps 
## debug linear-aps all 

debug linear-aps all 
命令功能 : 
debug线性APS保护所有属性，包括协议报文的收发、告警的接收、通知切换等。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps all 
 
no debug linear-aps all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
特权模式下，该命令用于打开或关闭所有的APS debug开关。这时，就可以看到APS所有的动态信息，包括APS协议报文的收发、告警的接收、通知切换等。 
范例 : 
ZXROSNG#debug linear-aps allAll linear APS debugging has been turned onZXROSNG#
相关命令 : 
show debug linear-aps 
## debug linear-aps lsp-group 

debug linear-aps lsp-group 
命令功能 : 
显示某个LSP保护组的APS实例的所有的debug信息。相关的no命令是关闭该LSP保护组的APS实例的所有的debug信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps lsp-group 
  ＜group-id 
＞
no debug linear-aps lsp-group 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|LSP保护组id，范围为1~$#100794373#$
缺省 : 
无 
使用说明 : 
1、该命令用于显示或关闭某个LSP保护组的APS实例的所有的debug信息。这时，就可以看到该APS实例的所有动态信息，包括APS协议报文的收发、告警的接收、状态切换等。2、在使用该命令时，一定要在特权模式下，使用terminal monitor, 否则无法打印debug信息。3、10分钟后，debug开关会自动关闭。如需长时间显示，需重新打开。4、可用show debug linear-aps命令查看是否成功配置上。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps lsp-group 1Linear APS debugging the seleceted lsp-group has been turned onZXROSNG#no debug linear-aps lsp-group 1Linear APS debugging the seleceted lsp-group has been turned offZXROSNG#
相关命令 : 
show debug linear-aps  
## debug linear-aps mc-selection 

debug linear-aps mc-selection 
命令功能 : 
 打开某个mc-selection保护组的APS实例的所有的debug信息。相关的no命令是关闭某个mc-selection保护组的APS实例的所有的debug信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps mc-selection 
  ＜pw-name 
＞
no debug linear-aps mc-selection 
  ＜pw-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜pw-name＞|mc-selection保护组名称
缺省 : 
无 
使用说明 : 
1．    该命令用于打开或关闭某个mc-selection保护组的APS实例的所有debug信息，包括告警接收以及切换事件通知。2、在使用该命令时，一定要在特权模式下，使用terminal monitor, 否则无法打印debug信息。3、10分钟后，debug开关会自动关闭。如需长时间显示，需重新打开。4、可用show debug linear-aps命令查看是否成功配置上。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps mc-selection pw1Linear APS debugging of the seleceted mc-selection group has been turned onZXROSNG#no debug linear-aps alarm mc-selection pw1Linear APS debugging of the seleceted mc-selection group has been turned off
相关命令 : 
show debug linear-aps 
## debug linear-aps mtunnel-group 

debug linear-aps mtunnel-group 
命令功能 : 
打开/关闭某个P2MP隧道保护组APS实例的所有DEBUG开关。包括报文收发，告警通知，倒换事件通知等DEBUG开关 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps mtunnel-group 
  ＜group-id 
＞
no debug linear-aps mtunnel-group 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|P2MP隧道保护组ID，范围1~$#67305543#$
缺省 : 
无 
使用说明 : 
1、使用该命令需要在特权模式下敲terminal monitor 2、该命令10分钟后会自动关闭。如果需要继续使用，需要重新打开3、打开某个不存在保护组的debug开关会报错
范例 : 
ZXROSNG#debug linear-aps mtunnel-group 1Linear APS debugging the selected P2MP tunnel group has been turned onZXROSNG#
ZXROSNG#debug linear-aps mtunnel-group 22%Error 120421: The APS instance hasn't been configured or has been deletedZXROSNG#
相关命令 : 
show debug linear-aps 
## debug linear-aps packet port-group ether-service 

debug linear-aps packet port-group ether-service 
命令功能 : 
打开某个以太端口APS实例的报文收发DEBUG开关。相应的no命令是关闭某个以太端口APS实例的报文收发DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps packet port-group ether-service 
  ＜group-id 
＞
no debug linear-aps packet port-group ether-service 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组号，范围为1~$#67305528#$
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用terminal monitor后才能看到DEBUG信息；2、当指定的某个以太端口APS实例不存在时，报错；3、使用该命令，打开某个以太端口APS实例的报文收发DEBUG开关，此时可以看到报文收发动态信息；相关的no命令是关闭某个以太端口APS实例的报文收发DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps packet  port-group ether-service 1Linear APS debugging packet has been turned on
相关命令 : 
无 
## debug linear-aps packet 

debug linear-aps packet 
命令功能 : 
打开所有或是某个线性APS实例的报文收发DEBUG开关。相应的no命令是关闭所有或是某个线性APS实例的报文收发DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps packet 
  [{lsp-group 
 ＜group-id 
＞|pw-protector 
 ＜pwg-name 
＞|tunnel-group 
 ＜group-id 
＞|ac-pw-protector 
 ＜ac-pwg-name 
＞}]
no debug linear-aps packet 
  [{lsp-group 
 ＜group-id 
＞|pw-protector 
 ＜pwg-name 
＞|tunnel-group 
 ＜group-id 
＞|ac-pw-protector 
 ＜ac-pwg-name 
＞}]
				
命令参数解释 : 
参数|描述
---|---
lsp-group|LSP保护组的报文收发DEBUG开关
＜group-id＞|隧道保护组ID，范围为1~$#67305513#$
pw-protector|伪线保护组的报文收发DEBUG开关
＜pwg-name＞|伪线保护组的保护组名，如pw1
tunnel-group|隧道保护组的报文收发DEBUG开关
＜group-id＞|隧道保护组ID，范围为1~$#67305513#$
ac-pw-protector|ac保护组的报文收发DEBUG开关
＜ac-pwg-name＞|ac保护组名，如pw1
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用terminal monitor后才能看到DEBUG信息；2、当指定的某个线性APS实例不存在时，报错；3、使用该命令，打开所有或是某个线性APS实例的报文收发DEBUG开关，此时可以看到报文收发动态信息；相关的no命令是关闭所有或是某个线性APS实例的报文收发DEBUG开关。
范例 : 
ZXROSNG#debug linear-aps packet Linear APS debugging packet has been turned onZXROSNG#
相关命令 : 
show debug linear-aps 
## debug linear-aps port-group 

debug linear-aps port-group 
命令功能 : 
显示某个端口保护组的APS实例的所有的debug信息。相关的no命令是关闭该端口保护组的APS实例的所有debug信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps port-group 
  {otn 
 ＜group-id 
＞|[msp 
] ＜group-id 
＞|ether-service 
 ＜group-id 
＞|flexe 
 ＜group-id 
＞}
no debug linear-aps port-group 
  {otn 
 ＜group-id 
＞|[msp 
] ＜group-id 
＞|ether-service 
 ＜group-id 
＞|flexe 
 ＜group-id 
＞}
				
命令参数解释 : 
参数|描述
---|---
otn|OTN 端口保护组的报文收发DEBUG开关
＜group-id＞|端口保护组号，范围为 1~$#67305527#$
msp|MSP:Multiplex Section Protection.msp端口保护组的报文收发DEBUG开关 ，不带msp时表示同一端口保护组
＜group-id＞|端口保护组号，范围为 1~256
ether-service|以太端口保护组的报文收发DEBUG开关
＜group-id＞|端口保护组号，范围为 1~$#67305528#$
flexe|FlexE端口保护组的报文收发DEBUG开关
＜group-id＞|端口保护组号，范围为 1~8192
缺省 : 
无 
使用说明 : 
1、该命令用于显示或关闭某个端口保护组的APS实例的所有的debug信息。这时，就可以看到该APS的所有动态信息，包括APS协议报文的收发、告警的接收、状态切换等。2、在使用该命令时，一定要在特权模式下，使用terminal monitor, 否则无法打印debug信息。3、10分钟后，debug开关会自动关闭。如需长时间显示，需重新打开。4、可用show debug linear-aps命令查看是否成功配置上。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps port-group 1Linear APS debugging the seleceted port-group has been turned onZXROSNG#no debug linear-aps port-group 1Linear APS debugging the seleceted port-group has been turned off
ZXROSNG#debug linear-aps port-group  msp 1Linear APS debugging the seleceted port-group has been turned onZXROSNG#no debug linear-aps port-group msp  1Linear APS debugging the seleceted port-group has been turned off
ZXROSNG#debug linear-aps port-group  otn 1Linear APS debugging the seleceted port-group has been turned onZXROSNG#no debug linear-aps port-group otn  1Linear APS debugging the seleceted port-group has been turned off
ZXROSNG#debug linear-aps port-group  multicast 1Linear APS debugging the seleceted port-group has been turned onZXROSNG#no debug linear-aps port-group multicast  1Linear APS debugging the seleceted port-group has been turned off
ZXROSNG#debug linear-aps port-group  flexe 1Linear APS debugging the seleceted port-group has been turned onZXROSNG#no debug linear-aps port-group flexe  1Linear APS debugging the seleceted port-group has been turned off
ZXROSNG#debug linear-aps port-group  ether-service 1Linear APS debugging the seleceted port-group has been turned onZXROSNG#no debug linear-aps port-group ether-service  1Linear APS debugging the seleceted port-group has been turned off
相关命令 : 
show debug linear-aps  
## debug linear-aps pw-protector 

debug linear-aps pw-protector 
命令功能 : 
打开某个伪线保护组APS实例的所有的DEBUG开关，此时可以看到该实例的报文收发、告警接收，倒换事件通知等动态信息。相应的no命令则是关闭该伪线保护组APS实例的所有DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps pw-protector 
  ＜pwg-name 
＞
no debug linear-aps pw-protector 
  ＜pwg-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜pwg-name＞|pw保护组名称，之前仅支持PW接口，现在增加支持AC接口类型
缺省 : 
无 
使用说明 : 
1、在特权模式下，该命令可以打开/关闭某个伪线保护组APS实例的所有DEBUG开关。此时，可以看到该APS实例的报文收发、告警接收，倒换事件通知等信息。2、需要在特权模式下输入terminal monitor，在DEBUG开关打开时，才可以看到动态信息；3、10分钟后，DEBUG开关会自动关闭，如需长时间使用，需要重复打开。
范例 : 
ZXROSNG#debug linear-aps pw-protector pw1Linear APS debugging the seleceted pw-protector has been turned onZXROSNG#
相关命令 : 
show debug linear-aps 
## debug linear-aps switch port-group ether-service 

debug linear-aps switch port-group ether-service 
命令功能 : 
打开某个以太端口APS实例的倒换事件通知DEBUG开关。相关的no命令是关闭某个以太端口线性APS实例的倒换事件通知DEBUG开关 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps switch port-group ether-service 
  ＜group-id 
＞
no debug linear-aps switch port-group ether-service 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组ID 1~$#67305528#$
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用 terminal monitor后才能看到DEBUG信息；2、当指定的某个以太端口APS实例不存在时，报错；3、使用该命令，打开某个以太端口APS实例的倒换事件通知DEBUG开关，此时可以看到倒换事件通知动态信息；相关的no命令是关闭某个以太端口APS实例的倒换事件通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps switch port-group  ether-service 1Linear APS debugging switching notify has been turned on
相关命令 : 
show debug linear-aps  
## debug linear-aps switch port-group flexe 

debug linear-aps switch port-group flexe 
命令功能 : 
打开某个FlexE端口APS实例的倒换事件通知DEBUG开关。相关的no命令是关闭某个FlexE端口APS实例的倒换事件通知DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps switch port-group flexe 
  ＜group-id 
＞
no debug linear-aps switch port-group flexe 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组ID 1~8192
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用 terminal monitor后才能看到DEBUG信息；2、当指定的某个FlexE端口APS实例不存在时，报错；3、使用该命令，打开某个FlexE端口APS实例的倒换事件通知DEBUG开关，此时可以看到倒换事件通知动态信息；相关的no命令是关闭某个FlexE端口APS实例的倒换事件通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps switch port-group  flexe 1Linear APS debugging switching notify has been turned on
相关命令 : 
show debug linear-aps 
## debug linear-aps switch port-group otn 

debug linear-aps switch port-group otn 
命令功能 : 
打开某个OTN端口APS实例的倒换事件通知DEBUG开关。相关的no命令是关闭某个OTN端口APS实例的倒换事件通知DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps switch port-group otn 
  ＜group-id 
＞
no debug linear-aps switch port-group otn 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组ID ,1~$#67305527#$
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用 terminal monitor后才能看到DEBUG信息；2、当指定的某个OTN端口APS实例不存在时，报错；3、使用该命令，打开某个OTN端口APS实例的倒换事件通知DEBUG开关，此时可以看到倒换事件通知动态信息；相关的no命令是关闭某个OTN端口APS实例的倒换事件通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps switch port-group  otn 1Linear APS debugging switching notify has been turned on
相关命令 : 
show debug linear-aps  
## debug linear-aps switch port-group 

debug linear-aps switch port-group 
命令功能 : 
打开某个MSP端口APS实例的倒换事件通知DEBUG开关。相应的no命令是关闭某个MSP端口APS实例的倒换事件通知DEBUG开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps switch port-group 
  [msp 
 ] ＜group-id 
＞
no debug linear-aps switch port-group 
  [msp 
 ] ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|保护组号，范围为1~256
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用 terminal monitor后才能看到DEBUG信息；2、当指定的某个MSP端口APS实例不存在时，报错；3、使用该命令，打开某个MSP端口APS实例的倒换事件通知DEBUG开关，此时可以看到倒换事件通知动态信息；相关的no命令是关闭某个MSP端口APS实例的倒换事件通知DEBUG开关。
范例 : 
ZXROSNG#terminal monitor ZXROSNG#debug linear-aps switch port-group 1Linear APS debugging switching notify has been turned on
ZXROSNG#debug linear-aps switch port-group msp 1Linear APS debugging switching notify has been turned on
相关命令 : 
show debug linear-aps  
## debug linear-aps switch 

debug linear-aps switch 
命令功能 : 
打开所有或是某个线性APS实例的倒换事件通知DEBUG开关。相应的no命令是关闭所有或是某个线性APS实例的倒换事件通知DEBUG开关。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps switch 
  [{lsp-group 
 ＜group-id 
＞|mc-selection 
 ＜mc-selection 
＞|pw-protector 
 ＜pwg-name 
＞|tunnel-group 
 ＜group-id 
＞|ac-pw-protector 
 ＜ac-pwg-name 
＞}]
no debug linear-aps switch 
  [{lsp-group 
 ＜group-id 
＞|mc-selection 
 ＜mc-selection 
＞|pw-protector 
 ＜pwg-name 
＞|tunnel-group 
 ＜group-id 
＞|ac-pw-protector 
 ＜ac-pwg-name 
＞}]
				
命令参数解释 : 
参数|描述
---|---
lsp-group|LSP保护组的倒换事件DEBUG开关
＜group-id＞|LSP保护组ID，范围为1~$#100794373#$
mc-selection|mc-selection保护组的倒换事件通知DEBUG开关
＜mc-selection＞|mc-selection保护组的保护组名，如pw1
pw-protector|伪线保护组的倒换事件通知DEBUG开关
＜pwg-name＞|伪线保护组的保护组名，如pw1
tunnel-group|隧道保护组的倒换事件通知DEBUG开关
＜group-id＞|隧道保护组ID，范围为1~4294967295
ac-pw-protector|ac保护组的倒换事件通知DEBUG开关
＜ac-pwg-name＞|ac保护组名，如pw1
缺省 : 
无 
使用说明 : 
1、在特权模式下，使用terminal monitor后才能看到DEBUG信息；2、当指定的某个线性APS实例不存在时，报错；3、使用该命令，打开所有或是某个线性APS实例的倒换事件通知DEBUG开关，此时可以看到倒换事件通知动态信息；相关的no命令是关闭所有或是某个线性APS实例的倒换事件通知DEBUG开关。
范例 : 
ZXROSNG#debug linear-aps switch Linear APS debugging switching notify has been turned onZXROSNG#
相关命令 : 
show debug linear-aps  
## debug linear-aps tunnel-group 

debug linear-aps tunnel-group 
命令功能 : 
显示某个隧道保护组的APS实例的所有的debug信息，包括协议报文的收发、告警的接收、通知切换等。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug linear-aps tunnel-group 
  ＜group-id 
＞
no debug linear-aps tunnel-group 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|隧道保护组号，范围为1~4294967295
缺省 : 
无 
使用说明 : 
特权模式下，该命令用于显示或关闭某个隧道保护组的APS实例的协议报文收发、告警接收、通知切换等信息。 
范例 : 
ZXROSNG#debug linear-aps tunnel-group 11Linear APS debugging the seleceted tunnel group has been turned onZXROSNG#
相关命令 : 
show debug linear-aps  
## hold-off 

hold-off 
命令功能 : 
设置aps保护的hold-off时间。 
命令模式 : 
 APS端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
hold-off 
  ＜HoldoffTime 
＞ [precise 
 ＜HoldoffpreciseTime 
＞]
命令参数解释 : 
参数|描述
---|---
＜HoldoffTime＞|配置hold-off时间，范围为0~100，单位为100ms
＜HoldoffpreciseTime＞|配置hold-off 10ms精度时间，范围为1~9，单位为10ms
缺省 : 
0ms 
使用说明 : 
进入APS端口保护模式，可以设置该端口保护组APS实例的HOLDOFF时间。不配置该命令时，hold-off 时间默认为0。如果要配置10ms精度，在配置第一个参数后追加10ms精度参数，范围为<10~90>ms。两个参数叠加后为最终holdoff时间。只配置100ms精度参数，可覆盖10ms精度参数。Holdoff时间最大值为10s，此时参数hold-off 配置为100，不能配置precise-time参数。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)# port-group  11ZXROSNG(config-aps-linear-protect-portgroup-11)#hold-off 100ZXROSNG(config-aps-linear-protect-portgroup-11)#hold-off 100 precise 5
相关命令 : 
相关SHOW命令为show aps linear-protect
## hold-off 

hold-off 
命令功能 : 
设置aps保护的hold-off时间。 
命令模式 : 
 APS OTN端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
hold-off 
  ＜HoldoffTime 
＞ [precise 
 ＜HoldoffpreciseTime 
＞]
命令参数解释 : 
参数|描述
---|---
＜HoldoffTime＞|配置hold-off时间，范围为0~100，单位为100ms
＜HoldoffpreciseTime＞|配置hold-off 10ms精度时间，范围为1~9，单位为10ms
缺省 : 
0ms 
使用说明 : 
进入APS otn端口保护模式，可以设置该端口保护组APS实例的HOLDOFF时间。不配置该命令时，hold-off 时间默认为0。如果要配置10ms精度，在配置第一个参数后追加10ms精度参数，范围为<10~90>ms。两个参数叠加后为最终holdoff时间。只配置100ms精度参数，可覆盖10ms精度参数。Holdoff时间最大值为10s，此时参数hold-off 配置为100，不能配置precise-time参数。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group otn 11ZXROSNG(config-aps-linear-protect-port-group-otn11)#hold-off 100ZXROSNG(config-aps-linear-protect-port-group-otn11)#hold-off 100 precise 5
相关命令 : 
相关SHOW命令为show aps linear-protect port-group otn
## hold-off 

hold-off 
命令功能 : 
设置aps保护的hold-off时间。 
命令模式 : 
 APS FlexE端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
hold-off 
  ＜HoldoffTime 
＞ [precise 
 ＜HoldoffpreciseTime 
＞]
命令参数解释 : 
参数|描述
---|---
＜HoldoffTime＞|配置hold-off时间，范围为0~100，单位为100ms
＜HoldoffpreciseTime＞|配置hold-off 10ms精度时间，范围为1~9，单位为10ms
缺省 : 
0ms 
使用说明 : 
进入APS flexe端口保护模式，可以设置该端口保护组APS实例的HOLDOFF时间。不配置该命令时，hold-off 时间默认为0。如果要配置10ms精度，在配置第一个参数后追加10ms精度参数，范围为<10~90>ms。两个参数叠加后为最终holdoff时间。只配置100ms精度参数，可覆盖10ms精度参数。Holdoff时间最大值为10s，此时参数hold-off 配置为100，不能配置precise-time参数。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group flexe 11ZXROSNG(config-aps-linear-protect-port-group-flexe11)#hold-off 100ZXROSNG(config-aps-linear-protect-port-group-flexe11)#hold-off 100 precise 5
相关命令 : 
相关SHOW命令为show aps linear-protect port-group flexe
## hold-off 

hold-off 
命令功能 : 
设置aps保护的hold-off时间。 
命令模式 : 
 APS隧道保护模式  
命令默认权限级别 : 
15 
命令格式 : 
hold-off 
  ＜HoldoffTime 
＞ [precise 
 ＜HoldoffpreciseTime 
＞]
命令参数解释 : 
参数|描述
---|---
＜HoldoffTime＞|配置hold-off时间，范围为0~100，单位为100ms
＜HoldoffpreciseTime＞|配置hold-off 10ms精度时间，范围为1~9，单位为10ms
缺省 : 
0ms 
使用说明 : 
进入APS隧道保护模式，可以设置该隧道保护组APS实例的HOLDOFF时间。不配置该命令时，hold-off 时间默认为0。如果要配置10ms精度，在配置第一个参数后追加10ms精度参数，范围为<10~90>ms。两个参数叠加后为最终holdoff时间。只配置100ms精度参数，可覆盖10ms精度参数。Holdoff时间最大值为10s，此时参数hold-off 配置为100，不能配置precise-time参数。 
范例 : 
ZXROSNG(config-aps-linear-protect-tunnelgroup11)#hold-off 100ZXROSNG(config-aps-linear-protect-tunnelgroup11)#hold-off 100 precise 5
相关命令 : 
相关SHOW命令为show aps linear-protect tunnel-group 11
## hold-off 

hold-off 
命令功能 : 
设置aps保护的hold-off时间。 
命令模式 : 
 APS伪线保护模式  
命令默认权限级别 : 
15 
命令格式 : 
hold-off 
  ＜HoldoffTime 
＞ [precise 
 ＜HoldoffpreciseTime 
＞]
命令参数解释 : 
参数|描述
---|---
＜HoldoffTime＞|配置hold-off时间，范围为0~100，单位为100ms
＜HoldoffpreciseTime＞|配置hold-off 10ms精度时间，范围为1~9，单位为10ms
缺省 : 
0ms 
使用说明 : 
进入APS伪线保护模式，可以设置该伪线保护组APS实例的HOLDOFF时间。不配置该命令时，hold-off 时间默认为0。如果要配置10ms精度，在配置第一个参数后追加10ms精度参数，范围为<10~90>ms。两个参数叠加后为最终holdoff时间。只配置100ms精度参数，可覆盖10ms精度参数。Holdoff时间最大值为10s，此时参数hold-off 配置为100，不能配置precise-time参数。 
范例 : 
ZXROSNG(config-aps-linear-protect-pwprotector-pw1)#hold-off 100ZXROSNG(config-aps-linear-protect-pwprotector-pw1)#hold-off 100 precise 5
相关命令 : 
相关SHOW命令为show aps linear-protect
## hold-off 

hold-off 
命令功能 : 
设置aps保护的hold-off时间。 
命令模式 : 
 APS multicast端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
hold-off 
  ＜HoldoffTime 
＞ [precise 
 ＜HoldoffpreciseTime 
＞]
命令参数解释 : 
参数|描述
---|---
＜HoldoffTime＞|配置hold-off时间，范围为0~100，单位为100ms
＜HoldoffpreciseTime＞|配置hold-off 10ms精度时间，范围为1~9，单位为10ms
缺省 : 
0ms 
使用说明 : 
进入APS mutilcast端口保护模式，可以设置该端口保护组APS实例的HOLDOFF时间。不配置该命令时，hold-off 时间默认为0。如果要配置10ms精度，在配置第一个参数后追加10ms精度参数，范围为<10~90>ms。两个参数叠加后为最终holdoff时间。只配置100ms精度参数，可覆盖10ms精度参数。Holdoff时间最大值为10s，此时参数hold-off 配置为100，不能配置precise-time参数。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group multicast 11ZXROSNG(config-aps-linear-protect-port-group-mc-11)#hold-off 100ZXROSNG(config-aps-linear-protect-port-group-mc-11)#hold-off 100 precise 5
相关命令 : 
相关SHOW命令为show aps linear-protect port-group multicast
## linear-protect 

linear-protect 
命令功能 : 
跳转到APS线性保护模式下 
命令模式 : 
 APS全局模式  
命令默认权限级别 : 
15 
命令格式 : 
linear-protect 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
在APS全局模式下，配置该命令，进入到APS线性保护模式 
范例 : 
ZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#
相关命令 : 
无 
## port-group ether-service 

port-group ether-service 
命令功能 : 
1、建立新的以太端口保护组类型的APS实例并进入模式；2、如果该端口保护组类型的APS实例已经存在，则仅进入模式，在该模式下，可以对配置该实例的一些属性。
命令模式 : 
 APS线性保护模式  
命令默认权限级别 : 
15 
命令格式 : 
port-group ether-service 
  ＜LinearProtectId 
＞
命令参数解释 : 
参数|描述
---|---
＜LinearProtectId＞|端口保护组ID，范围为1~$#67305528#$
缺省 : 
无 
使用说明 : 
在配置端口保护组类型的APS实例时，必须保证该以太端口保护组实例已经存在 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#port-group ether-service 1ZXROSNG(config-aps-linear-protect-portgroup-es-1)#
相关命令 : 
无 
## port-group flexe 

port-group flexe 
命令功能 : 
1、建立新的FlexE端口保护组类型的APS实例并进入模式；2、如果该端口保护组类型的APS实例已经存在，则仅进入模式，在该模式下，可以对配置该实例的一些属性。
命令模式 : 
 APS线性保护模式  
命令默认权限级别 : 
15 
命令格式 : 
port-group flexe 
  ＜LinearProtectId 
＞
命令参数解释 : 
参数|描述
---|---
＜LinearProtectId＞|端口保护组ID，范围为1~8192
缺省 : 
无 
使用说明 : 
在配置端口保护组类型的APS实例时，必须保证该FlexE端口保护组实例已经存在 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#port-group flexe 1ZXROSNG(config-aps-linear-protect-portgroup-flexe-1)#
相关命令 : 
无 
## port-group msp 

port-group msp 
命令功能 : 
1、建立新的MSP端口保护组类型的APS实例并进入模式；2、如果该端口保护组类型的APS实例已经存在，则仅进入模式，在该模式下，可以对配置该实例的一些属性。
命令模式 : 
 APS线性保护模式  
命令默认权限级别 : 
15 
命令格式 : 
port-group msp 
  ＜LinearProtectId 
＞
命令参数解释 : 
参数|描述
---|---
＜LinearProtectId＞|端口保护组ID，范围为1~256
缺省 : 
无 
使用说明 : 
在配置端口保护组类型的APS实例时，必须保证该MSP端口保护组实例已经存在 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#port-group msp 1ZXROSNG(config-aps-linear-protect-portgroup-1)#
相关命令 : 
无 
## port-group otn 

port-group otn 
命令功能 : 
1、建立新的OTN端口保护组类型的APS实例并进入模式；2、如果该端口保护组类型的APS实例已经存在，则仅进入模式，在该模式下，可以对配置该实例的一些属性。
命令模式 : 
 APS线性保护模式  
命令默认权限级别 : 
15 
命令格式 : 
port-group otn 
  ＜LinearProtectId 
＞
命令参数解释 : 
参数|描述
---|---
＜LinearProtectId＞|端口保护组ID，范围为1~$#67305527#$
缺省 : 
无 
使用说明 : 
在配置端口保护组类型的APS实例时，必须保证该OTN端口保护组实例已经存在 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#port-group otn 1ZXROSNG(config-aps-linear-protect-portgroup-otn-1)#
相关命令 : 
无 
## port-group 

port-group 
命令功能 : 
1、建立新的端口保护组类型的APS实例并进入模式；2、如果该端口保护组类型的APS实例已经存在，则仅进入模式，在该模式下，可以对配置该实例的一些属性。
命令模式 : 
 APS线性保护模式  
命令默认权限级别 : 
15 
命令格式 : 
port-group 
  ＜LinearProtectId 
＞
命令参数解释 : 
参数|描述
---|---
＜LinearProtectId＞|端口保护组ID，范围为1~256
缺省 : 
无 
使用说明 : 
在配置端口保护组类型的APS实例时，必须保证该端口保护组实例已经存在 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#port-group 1ZXROSNG(config-aps-linear-protect-portgroup1)#
相关命令 : 
无 
## protect-mode 

protect-mode 
命令功能 : 
用来配置线性保护的报文发送开关。 
命令模式 : 
 APS隧道保护模式  
命令默认权限级别 : 
15 
命令格式 : 
protect-mode 
  {remote 
|local 
}
命令参数解释 : 
参数|描述
---|---
remote|远端模式，APS协议发送报文(默认为此模式)
local|本地模式，APS协议不发送报文
缺省 : 
remote 
使用说明 : 
进入APS线性保护模式，可以设置该保护组APS实例的报文发送开关。不配置该命令时，protect-mode默认为remote。 
范例 : 
ZXROSNG(config-aps-linear-protect-tunnelgroup11)#protect-mode local ZXROSNG(config-aps-linear-protect-tunnelgroup11)#
相关命令 : 
show aps linear-protect 
## protect-mode 

protect-mode 
命令功能 : 
用来配置线性保护的报文发送开关。 
命令模式 : 
 APS伪线保护模式  
命令默认权限级别 : 
15 
命令格式 : 
protect-mode 
  {remote 
|local 
}
命令参数解释 : 
参数|描述
---|---
remote|远端模式，APS协议发送报文(默认为此模式)
local|本地模式，APS协议不发送报文
缺省 : 
remote 
使用说明 : 
进入特定的APS线性保护模式，可以设置该保护组APS实例的报文发送开关。不配置该命令时，protect-mode默认为remote。 
范例 : 
ZXROSNG(config-aps-linear-protect-tunnelgroup11)#protect-mode local ZXROSNG(config-aps-linear-protect-tunnelgroup11)#
相关命令 : 
show aps linear-protect 
## pw-protector 

pw-protector 
命令功能 : 
创建伪线保护组APS实例或者进入APS伪线保护模式 
命令模式 : 
 APS线性保护模式  
命令默认权限级别 : 
15 
命令格式 : 
pw-protector 
  ＜pwg_name 
＞
命令参数解释 : 
参数|描述
---|---
＜pwg_name＞|伪线保护组name
缺省 : 
无 
使用说明 : 
先创建伪线保护组，并且在该保护组下配置APS策略。进入APS线性保护模式，第一次执行该命令，就为对应的伪线保护组创建了一个线性保护APS实例，执行完该命令后，进入到APS伪线保护模式。如果之前已经配置过该命令，就直接进入APS伪线保护模式。
范例 : 
ZXROSNG(config-aps-linear-protect)#pw-protector pw1ZXROSNG(config-aps-linear-protect-pwprotector-pw1)#
相关命令 : 
前置命令vpls test1pseudo-wire   spoke pw1 neighbour 22.19.19.19 vcid 1000 control-word preferred signal static local 10001 remote 10001 tunnel-policy hj1commitexredundancy-manager protect-type 1:1 protect-strategy apsexexbackup-pw pw2 protect pw1neighbour 22.19.19.19 vcid 1001 signal static local  10002 remote 10002control-word preferred tunnel-policy hj2commit exexex相关SHOW命令为：show aps linear-protect pw-protector pw1
## revertive-mode 

revertive-mode 
命令功能 : 
设置线性保护的保护模式。 
命令模式 : 
 APS隧道保护模式  
命令默认权限级别 : 
15 
命令格式 : 
revertive-mode 
  {non-revertive 
|revertive 
 wtr 
 {default 
|＜WtrTime 
＞}}
命令参数解释 : 
参数|描述
---|---
non-revertive|设置线性保护组的aps保护模式为不可返回的
revertive|设置线性保护组的aps保护模式为可返回的
default|当保护模式为可返回式时，默认WTR时间，为5分钟
＜WtrTime＞|wtr时间，范围为0~12，单位为5分钟
缺省 : 
revertive wtr default 
使用说明 : 
进入APS隧道保护模式，可以设置该隧道保护组APS实例的保护模式。当为非返回式时，主链路故障时切换到备隧道，主链路OK时，仍然在备上面，不回切到主。当为返回式时，主链路故障切换到备，当主链路OK时，进入WTR时间，WTR时间超时就回切到主。 
范例 : 
ZXROSNG(config-aps-linear-protect-tunnelgroup11)#revertive-mode non-revertive ZXROSNG(config-aps-linear-protect-tunnelgroup11)#
相关命令 : 
相关SHOW命令为show aps linear-protect tunnel-group 11
## revertive-mode 

revertive-mode 
命令功能 : 
设置线性保护的保护模式。 
命令模式 : 
 APS端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
revertive-mode 
  {non-revertive 
|revertive 
 wtr 
 {default 
|＜WtrTime 
＞}}
命令参数解释 : 
参数|描述
---|---
non-revertive|设置线性保护组的aps保护模式为不可返回的
revertive|设置线性保护组的aps保护模式为可返回的
default|当保护模式为可返回式时，默认WTR时间，为5分钟
＜WtrTime＞|wtr时间，范围为0~12，单位为5分钟
缺省 : 
revertive wtr default 
使用说明 : 
进入APS端口保护模式，可以设置该端口保护组APS实例的保护模式。当为非返回式时，主链路故障时切换到备隧道，主链路OK时，仍然在备上面，不回切到主。当为返回式时，主链路故障切换到备，当主链路OK时，进入WTR时间，WTR时间超时就回切到主。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)# port-group  11ZXROSNG(config-aps-linear-protect-portgroup-11)#revertive-mode non-revertive ZXROSNG(config-aps-linear-protect-portgroup-11)#
相关命令 : 
相关SHOW命令为show aps linear-protect port-group 11
## revertive-mode 

revertive-mode 
命令功能 : 
设置线性保护的保护模式。 
命令模式 : 
 APS伪线保护模式  
命令默认权限级别 : 
15 
命令格式 : 
revertive-mode 
  {non-revertive 
|revertive 
 wtr 
 {default 
|＜WtrTime 
＞}}
命令参数解释 : 
参数|描述
---|---
non-revertive|设置线性保护组的aps保护模式为不可返回的
revertive|设置线性保护组的aps保护模式为可返回的
default|当保护模式为可返回式时，默认WTR时间，为5分钟
＜WtrTime＞|wtr时间，范围为0~$#35520521#$，单位为分钟
缺省 : 
revertive wtr default 
使用说明 : 
进入APS隧道保护模式，可以设置该隧道保护组APS实例的保护模式。当为非返回式时，主链路故障时切换到备隧道，主链路OK时，仍然在备上面，不回切到主。当为返回式时，主链路故障切换到备，当主链路OK时，进入WTR时间，WTR时间超时就回切到主。 
范例 : 
ZXROSNG(config-aps-linear-protect-tunnelgroup11)#revertive-mode non-revertive ZXROSNG(config-aps-linear-protect-tunnelgroup11)#
相关命令 : 
相关SHOW命令为show aps linear-protect tunnel-group 11
## revertive-mode 

revertive-mode 
命令功能 : 
设置线性保护的保护模式。 
命令模式 : 
 APS multicast端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
revertive-mode 
  {non-revertive 
|revertive 
 wtr 
 {default 
|＜WtrTime 
＞}}
命令参数解释 : 
参数|描述
---|---
non-revertive|设置线性保护组的aps保护模式为不可返回的
revertive|设置线性保护组的aps保护模式为可返回的
default|当保护模式为可返回式时，默认WTR时间，为5分钟
＜WtrTime＞|wtr时间，范围为0~12，单位为5分钟
缺省 : 
revertive wtr default 
使用说明 : 
进入APS multicast端口保护模式，可以设置该端口保护组APS实例的保护模式。当为非返回式时，主链路故障时切换到备隧道，主链路OK时，仍然在备上面，不回切到主。当为返回式时，主链路故障切换到备，当主链路OK时，进入WTR时间，WTR时间超时就回切到主。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group multicast 11ZXROSNG(config-aps-linear-protect-portgroup-mc-11)#revertive-mode non-revertive 
相关命令 : 
相关SHOW命令为show aps linear-protect port-group multicast
## revertive-mode 

revertive-mode 
命令功能 : 
设置线性保护的保护模式。 
命令模式 : 
 APS OTN端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
revertive-mode 
  {non-revertive 
|revertive 
 wtr 
 {default 
|＜WtrTime 
＞}}
命令参数解释 : 
参数|描述
---|---
non-revertive|设置线性保护组的aps保护模式为不可返回的
revertive|设置线性保护组的aps保护模式为可返回的
default|当保护模式为可返回式时，默认WTR时间，为5分钟
＜WtrTime＞|wtr时间，范围为0~12，单位为5分钟
缺省 : 
revertive wtr default 
使用说明 : 
进入APS OTN端口保护模式，可以设置该端口保护组APS实例的保护模式。当为非返回式时，主链路故障时切换到备隧道，主链路OK时，仍然在备上面，不回切到主。当为返回式时，主链路故障切换到备，当主链路OK时，进入WTR时间，WTR时间超时就回切到主。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group otn 11ZXROSNG(config-aps-linear-protect-portgroup-otn11)#revertive-mode non-revertive ZXROSNG(config-aps-linear-protect-portgroup-otn11)#
相关命令 : 
相关SHOW命令为show aps linear-protect port-group otn
## revertive-mode 

revertive-mode 
命令功能 : 
设置线性保护的保护模式。 
命令模式 : 
 APS FlexE端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
revertive-mode 
  {non-revertive 
|revertive 
 wtr 
 {default 
|＜WtrTime 
＞}}
命令参数解释 : 
参数|描述
---|---
non-revertive|设置线性保护组的aps保护模式为不可返回的
revertive|设置线性保护组的aps保护模式为可返回的
default|当保护模式为可返回式时，默认WTR时间，为5分钟
＜WtrTime＞|wtr时间，范围为0~12，单位为5分钟
缺省 : 
revertive wtr default 
使用说明 : 
进入APS FlexE端口保护模式，可以设置该端口保护组APS实例的保护模式。当为非返回式时，主链路故障时切换到备隧道，主链路OK时，仍然在备上面，不回切到主。当为返回式时，主链路故障切换到备，当主链路OK时，进入WTR时间，WTR时间超时就回切到主。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group flexe 11ZXROSNG(config-aps-linear-protect-portgroup-flexe11)#revertive-mode non-revertive ZXROSNG(config-aps-linear-protect-portgroup-flexe11)#
相关命令 : 
相关SHOW命令为show aps linear-protect port-group flexe
## sd-preferred 

sd-preferred 
命令功能 : 
配置线性保护APS全局的SD优先功能。 
命令模式 : 
 APS线性保护模式  
命令默认权限级别 : 
15 
命令格式 : 
sd-preferred 
 
no sd-preferred 
命令参数解释 : 
					无
				 
缺省 : 
默认按照SD-P相同于SD优先级处理。(SD：Signal degrade---信号劣化。本文中SD表示工作SD，SD-P表示保护SD) 
使用说明 : 
在APS线性保护模式下执行该命令，设置该保护APS线性全局的SD-P优先或相同于SD。如果实例下有sd-preferred配置，则优先用实例下的配置。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#sd-preferredZXROSNG(config-aps-linear-protect)#no sd-preferred
相关命令 : 
保护实例下配置（tunnel-group，pw-group、ac-pw-group、mtunnel-group、以太port-group）：1、sd-preferred  enable2、sd-preferred  disable3、no sd-preferred
## sd-preferred 

sd-preferred 
命令功能 : 
配置线性保护APS实例的SD优先功能。 
命令模式 : 
 APS伪线保护模式  
命令默认权限级别 : 
15 
命令格式 : 
sd-preferred 
  {enable 
|disable 
}
no sd-preferred 
命令参数解释 : 
参数|描述
---|---
enable|配置SD-P优先级高于SD
disable|配置SD-P、SD相同优先级
缺省 : 
无配置，默认按照全局sd-preferred配置。 
使用说明 : 
在APS伪线保护模式下执行该命令，设置该保护APS实例的SD-P优先或相同于SD。实例下配置优先级高于全局sd-preferred配置，当实例下无配置或no配置后，按照全局配置执行。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#pw-protector pw1ZXROSNG(config-aps-linear-protect-pwprotector-pw1)#sd-preferred enable 
相关命令 : 
相关SHOW命令：show aps linear-protect pw-protector pw1全局配置，即APS线性保护模式下配置：sd-preferredno sd-preferred
## sd-preferred 

sd-preferred 
命令功能 : 
配置线性保护APS实例的SD优先功能。 
命令模式 : 
 APS隧道保护模式  
命令默认权限级别 : 
15 
命令格式 : 
sd-preferred 
  {enable 
|disable 
}
no sd-preferred 
命令参数解释 : 
参数|描述
---|---
enable|配置SD-P优先级高于SD
disable|配置SD-P、SD相同优先级
缺省 : 
无配置，默认按照全局sd-preferred配置。 
使用说明 : 
在APS隧道保护模式下执行该命令，设置该保护APS实例的SD-P优先或相同于SD。实例下配置优先级高于全局sd-preferred配置，当实例下无配置或no配置后，按照全局配置执行。 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#tunnel-group 1ZXROSNG(config-aps-linear-protect-tunnelgroup1)#sd-preferred enable 
相关命令 : 
相关SHOW命令：show aps linear-protect tunnel-group 1全局配置，即APS线性保护模式下配置：sd-preferredno sd-preferred
## show aps linear-protect port-group ether-service 

show aps linear-protect port-group ether-service 
命令功能 : 
显示某个特定的以太端口保护组APS实例的相关信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show aps linear-protect port-group ether-service 
  ＜group-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜group-id＞|端口保护组号，范围是1~$#67305528#$
缺省 : 
无 
使用说明 : 
除用户模式以外，可以执行该命令来查看某个特定的以太端口保护组APS实例的相关信息。 
范例 : 
除用户模式外执行命令show aps linear-protect port-group ether-service 1，查看端口保护组APS实例的相关信息。 ZXROSNG#show aps linear-protect port-group ether-service 1----------[APS Linear Instance]----------  Protection group type: port-group-ether-service  Protection group id: 1  Protection type: 1+1 bidirectional receiving selective  APS is enabled  APS state: MANUAL_SWITCH  APS packet request: NO_REQUEST_NORMAL  Protection mode: remote  Active-state: restore-run  Revertive mode: revertive, WTR time: 5min  Hold-off time: 0ms,valid hold-off time: 0ms  Switch command: manual-switch  Bridge type: selector  MEG level: 7  SD preferred: disabled域信息：Protection group type: 保护组类型 Protection group id:保护组IDProtection type：保护组类型信息。APS is not enabled：APS协议使能信息，APS is not enabled或者APS is enabled APS state：协议状态信息 APS packet request：报文请求信息。Active-state：激活状态。包含restore-run， pause两种状态。Revertive mode：反转模式。包含WTR：wtr时间配置显示 Hold-off time：hold-off时间配置显示Switch command：倒换命令配置信息显示。  Protection mode: 保护模式，包含remote和localBridge type:桥接类型，selector或broadcast。port-group不显示此字段。SD preferred: enabled 表示开启SD-P优先,disabled表示关闭SD-P优先MEG level：MEG 信息，0-7。
相关命令 : 
无 
## show aps linear-protect port-group flexe 

show aps linear-protect port-group flexe 
命令功能 : 
显示某个特定的FlexE端口保护组APS实例的相关信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show aps linear-protect port-group flexe 
  ＜group-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜group-id＞|端口保护组号，范围是1~8192
缺省 : 
无 
使用说明 : 
除用户模式以外，可以执行该命令来查看某个特定的FlexE端口保护组APS实例的相关信息。 
范例 : 
除用户模式外执行命令show aps linear-protect port-group flexe 1，查看端口保护组APS实例的相关信息。 ZXROSNG#show aps linear-protect port-group flexe 1----------[APS Linear Instance]----------  Protection group type: port-group-flexe  Protection group id: 1  Protection type: 1+1 bidirectional receiving selective  APS is not enabled  APS state: NO_REQUEST_NULL  APS packet request: NULL  Active-state: restore-run  Revertive mode: revertive, WTR time: 5min  Hold-off time: 0ms,valid hold-off time: 0ms  Switch command: null域信息：Protection group type: 保护组类型 Protection group id:保护组IDProtection type：保护组类型信息。APS is not enabled： APS协议使能信息，APS is not enabled或者APS is enabled APS state：协议状态信息 APS packet request：报文请求信息。Active-state：激活状态。包含restore-run， pause两种状态。Revertive mode：反转模式。包含WTR：wtr时间配置显示 Hold-off time：hold-off时间配置显示Switch command：倒换命令配置信息显示。
相关命令 : 
无 
## show aps linear-protect port-group otn 

show aps linear-protect port-group otn 
命令功能 : 
显示某个特定的OTN端口保护组APS实例的相关信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show aps linear-protect port-group otn 
  ＜group-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜group-id＞|端口保护组号，范围是1~$#67305527#$
缺省 : 
无 
使用说明 : 
除用户模式以外，可以执行该命令来查看某个特定的OTN端口保护组APS实例的相关信息。 
范例 : 
除用户模式外执行命令show aps linear-protect port-group otn 1，查看端口保护组APS实例的相关信息。 ZXROSNG#show aps linear-protect port-group otn 1----------[APS Linear Instance]----------  Protection group type: port-group-otn  Protection group id: 1  Protection type: 1+1 bidirectional receiving selective  APS is not enabled  APS state: NO_REQUEST_NULL  APS packet request: NULL  Active-state: restore-run  Revertive mode: revertive, WTR time: 5min  Hold-off time: 0ms,valid hold-off time: 0ms  Switch command: null域信息：Protection group type: 保护组类型 Protection group id:保护组IDProtection type：保护组类型信息。APS is not enabled： APS协议使能信息，APS is not enabled或者APS is enabled APS state：协议状态信息 APS packet request：报文请求信息。Active-state：激活状态。包含restore-run， pause两种状态。Revertive mode：反转模式。包含WTR：wtr时间配置显示 Hold-off time：hold-off时间配置显示Switch command：倒换命令配置信息显示。
相关命令 : 
无 
## show aps linear-protect port-group 

show aps linear-protect port-group 
命令功能 : 
显示某个特定的MSP端口保护组APS实例的相关信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show aps linear-protect port-group 
  [msp 
 ] ＜group-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜group-id＞|端口保护组号，范围是1~256
缺省 : 
无 
使用说明 : 
除用户模式以外，可以执行该命令来查看某个特定的MSP端口保护组APS实例的相关信息。 
范例 : 
除用户模式外执行命令show aps linear-protect port-group 1，查看端口保护组APS实例的相关信息。 ZXROSNG(config)#show aps linear-protect port-group 1ZXROSNG#show aps linear-protect port-group 1----------[APS Linear Instance]----------  Protection group type: port-group  Protection group id: 1  Protection type: 1+1 bidirectional receiving selective  APS is not enabled  APS state: NO_REQUEST_NULL  APS packet request: NULL  Active-state: restore-run  Revertive mode: revertive, WTR time: 5min  Hold-off time: 0ms,valid hold-off time: 0ms  Switch command: null域信息：Protection group type: 保护组类型Protection group id:保护组IDProtection type：保护组类型信息。APS is not enabled： APS协议使能信息，APS is not enabled或者APS is enabled APS state：协议状态信息 APS packet request：报文请求信息。Active-state：激活状态。包含restore-run， pause两种状态。Revertive mode：反转模式。包含WTR：wtr时间配置显示 Hold-off time：hold-off时间配置显示Switch command：倒换命令配置信息显示。
相关命令 : 
无 
## show aps linear-protect 

show aps linear-protect 
命令功能 : 
显示所有或者某个特定的线性APS实例的相关信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show aps linear-protect 
  [{tunnel-group 
 ＜group-id 
＞|pw-protector 
 ＜pwg-name 
＞|lsp-group 
 ＜group-id 
＞|mc-selection 
 ＜pwg-name 
＞|ac-pw-protector 
 ＜ac-pwg-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
tunnel-group|隧道保护组的APS实例的配置状态信息
＜group-id＞|LSP保护组ID，范围为1~$#100794373#$
pw-protector|伪线保护组的APS实例的配置状态信息
＜pwg-name＞|mc-selection保护组名，如pw1
lsp-group|LSP保护组的APS实例的配置状态信息
＜group-id＞|LSP保护组ID，范围为1~$#100794373#$
mc-selection|mc-selection保护组的APS实例的配置状态信息
＜pwg-name＞|mc-selection保护组名，如pw1
ac-pw-protector|ac保护组的APS实例的配置状态信息
＜ac-pwg-name＞|ac保护组名，如pw1
缺省 : 
无 
使用说明 : 
在任意模式下，可以执行该命令来查看所有或者某个特定的线性APS实例的相关信息。 
范例 : 
在任意模式下执行命令show aps linear-protect，查看所有线性APS实例的相关信息。 ZXROSNG(config)#show aps linear-protect ----------[APS Linear Instance]----------  Protection group type: tunnel   Protection group id: 11   Protection group name:    Protection type: 1:1 bidirection  APS is enabled  APS state: NO_REQUEST_NULL  Protection mode: local  Active-state: restore-run  Rdi-switch: enable  Revertive mode: revertive, WTR time: 1min  Hold-off time: 0ms  Switch command: null  Bridge type: selector  SD preferred: enabled----------[APS Linear Instance]----------  Protection group type: pw   Protection group id: 1   Protection group name: pw1   Protection type: 1:1 unidirection  APS is enabled  APS state: NO_REQUEST_NULL  Protection mode: remote  Active-state: restore-run  Rdi-switch: enable  Revertive mode: revertive, WTR time: 5min  Hold-off time: 0ms  Switch command: null  Bridge type: selector  SD preferred: enabled执行命令show aps linear-protect tunnel-group 11，查看隧道保护组11下的APS实例的相关信息。ZXROSNG(config)#show aps linear-protect tunnel-group 11----------[APS Linear Instance]----------  Protection group type: tunnel   Protection group id: 11   Protection group name:    Protection type: 1:1 bidirection  APS is enabled  APS state: NO_REQUEST_NULL  Protection mode: local  Active-state: restore-run  Rdi-switch: enabled  Revertive mode: revertive, WTR time: 1min  Hold-off time: 0ms  Switch command: null  Bridge type: selector  SD preferred: enabledZXROSNG(config)#Bridge type:桥接类型，selector或broadcast。port-group不显示此字段。SD preferred: enabled 表示开启SD-P优先,disabled表示关闭SD-P优先
相关命令 : 
无 
## show debug linear-aps 

show debug linear-aps 
命令功能 : 
显示线性APS的debug开关信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug linear-aps 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
在任意模式下执行该命令，显示所有线性APS的所有debug开关信息 
范例 : 
ZXROSNG#show debug linear-aps LINEAR-APS:   Linear APS debugging receiving alarm message is on   Linear APS debugging of the seleceted tunnel group 11 has been turned on ZXROSNG#
相关命令 : 
无 
## switch 

switch 
命令功能 : 
APS命令切换配置。 
命令模式 : 
 APS隧道保护模式  
命令默认权限级别 : 
15 
命令格式 : 
switch 
  {clear 
|force-switch 
|lockout 
|manual-switch 
|exercise 
|manual-switch-work 
}
命令参数解释 : 
参数|描述
---|---
clear|清除之前配置的切换命令，或者清除WTR状态
force-switch|强制业务倒换到保护链路
lockout|锁定保护链路，业务只允许在主链路上传输
manual-switch|人工倒换命令，倒换到保护链路上
exercise|练习命令，不作任何倒换
manual-switch-work|人工倒换到工作，流量到工作链路上
缺省 : 
无 
使用说明 : 
Clear可以清除所有倒换命令，还可以清楚WTR状态。其他命令之间有先后秩序，高优先级的命令可以抢占低优先级的命令，之间的优先级如下：lock-out > force-switch > manual-switch(manual-switch-work) > exercise manual-switch与manual-switch-work互斥。
范例 : 
ZXROSNG(config-aps-linear-protect-tunnelgroup11)#switch lockout ZXROSNG(config-aps-linear-protect-tunnelgroup11)#
相关命令 : 
show aps linear-protect 
## switch 

switch 
命令功能 : 
APS命令切换配置。 
命令模式 : 
 APS伪线保护模式  
命令默认权限级别 : 
15 
命令格式 : 
switch 
  {clear 
|force-switch 
|lockout 
|manual-switch 
|exercise 
|manual-switch-work 
}
命令参数解释 : 
参数|描述
---|---
clear|清除之前配置的切换命令，或者清除WTR状态
force-switch|强制业务倒换到保护链路
lockout|锁定保护链路，业务只允许在主链路上传输
manual-switch|人工倒换命令，倒换到保护链路上
exercise|练习命令，不作任何倒换
manual-switch-work|人工倒换到工作，流量到工作链路上
缺省 : 
无 
使用说明 : 
Clear可以清除所有倒换命令，还可以清除WTR状态。其他命令之间有先后秩序，高优先级的命令可以抢占低优先级的命令，之间的优先级如下：lock-out > force-switch > manual-switch(manual-switch-work) > exercise manual-switch与manual-switch-work互斥。
范例 : 
ZXROSNG(config-aps-linear-protect-pwprotector-pw1)#switch lockout ZXROSNG(config-aps-linear-protect-pwprotector-pw1)#
相关命令 : 
show aps linear-protect 
## switch 

switch 
命令功能 : 
用于配置APS命令切换 
命令模式 : 
 APS multicast端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
switch 
  {clear 
|force-switch 
|lockout 
|manual-switch 
|exercise 
|force-switch-work 
|manual-switch-work 
}
命令参数解释 : 
参数|描述
---|---
clear|清除之前配置的切换命令，或者清除WTR状态
force-switch|强制业务倒换到保护链路。
lockout|锁定保护链路，业务只允许在主链路上传输
manual-switch|人工倒换命令，倒换到保护链路上。
exercise|练习命令，不作任何倒换。
force-switch-work|强制业务到工作
manual-switch-work|人工倒换命令，业务走工作。
缺省 : 
无 
使用说明 : 
使用本命令前需要先配置组播端口保护的APS实例；本命令与同一模式下的其他命令无依赖关系，但本命令的不同参数之间存在先后次序，即高优先级的命令可以抢占低优先级的命令，不同参数之间的优先级：lock-out > force-switch > manual-switch(manual-switch-work) > exercise，其中manual-switch与manual-switch-work是互斥的；在APS以太端口保护模式下执行该命令，配置倒换命令触发APS状态变化，默认无配置。各参数之间按照优先级高级进行抢占，命令说明见命令参数解释；一个APS实例仅支持一条switch命令。
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group multicast 11ZXROSNG(config-aps-linear-protect-portgroup-mc-11)#switch lockout 
相关命令 : 
show aps linear-protect multicast 
## switch 

switch 
命令功能 : 
用于配置APS命令切换 
命令模式 : 
 APS OTN端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
switch 
  {clear 
|force-switch 
|lockout 
|manual-switch 
|exercise 
|force-switch-work 
|manual-switch-work 
}
命令参数解释 : 
参数|描述
---|---
clear|清除之前配置的切换命令，或者清除WTR状态。
force-switch|强制业务倒换到保护链路。
lockout|锁定保护链路，业务只允许在主链路上传输
manual-switch|人工倒换命令，倒换到保护链路上。
exercise|练习命令，不作任何倒换。
force-switch-work|强制业务到工作
manual-switch-work|人工倒换命令，业务走工作
缺省 : 
无 
使用说明 : 
使用本命令前需要先配置OTN端口保护的APS实例；本命令与同一模式下的其他命令无依赖关系，但本命令的不同参数之间存在先后次序，即高优先级的命令可以抢占低优先级的命令，不同参数之间的优先级：lock-out > force-switch > manual-switch(manual-switch-work) > exercise，其中manual-switch与manual-switch-work是互斥的；在APS以太端口保护模式下执行该命令，配置倒换命令触发APS状态变化，默认无配置。各参数之间按照优先级高级进行抢占，命令说明见命令参数解释；一个APS实例仅支持一条switch命令。
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group otn 11ZXROSNG(config-aps-linear-protect-portgroup-otn-11)#switch lockout ZXROSNG(config-aps-linear-protect-portgroup-otn-11)#
相关命令 : 
show aps linear-protect otn 
## switch 

switch 
命令功能 : 
用于配置APS命令切换 
命令模式 : 
 APS FlexE端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
switch 
  {clear 
|force-switch 
|lockout 
|manual-switch 
|exercise 
|force-switch-work 
|manual-switch-work 
}
命令参数解释 : 
参数|描述
---|---
clear|清除之前配置的切换命令，或者清除WTR状态。
force-switch|强制业务倒换到保护链路。
lockout|锁定保护链路，业务只允许在主链路上传输
manual-switch|人工倒换命令，倒换到保护链路上。
exercise|练习命令，不作任何倒换。
force-switch-work|强制业务到工作
manual-switch-work|人工倒换命令，业务走工作。
缺省 : 
无 
使用说明 : 
使用本命令前需要先配置FlexE端口保护的APS实例；本命令与同一模式下的其他命令无依赖关系，但本命令的不同参数之间存在先后次序，即高优先级的命令可以抢占低优先级的命令，不同参数之间的优先级：lock-out > force-switch > manual-switch(manual-switch-work) > exercise，其中manual-switch与manual-switch-work是互斥的；在APS以太端口保护模式下执行该命令，配置倒换命令触发APS状态变化，默认无配置。各参数之间按照优先级高级进行抢占，命令说明见命令参数解释；一个APS实例仅支持一条switch命令。
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)#port-group flexe 11ZXROSNG(config-aps-linear-protect-portgroup-flexe-11)#switch lockout 
相关命令 : 
show aps linear-protect flexe 
## switch 

switch 
命令功能 : 
配置APS命令切换 
命令模式 : 
 APS端口保护模式  
命令默认权限级别 : 
15 
命令格式 : 
switch 
  {clear 
|force-switch 
|lockout 
|manual-switch 
|exercise 
|force-switch-work 
|manual-switch-work 
}
命令参数解释 : 
参数|描述
---|---
clear|清除之前配置的切换命令，或者清除WTR状态
force-switch|强制业务倒换到保护链路
lockout|锁定保护链路，业务只允许在主链路上传输
manual-switch|人工倒换命令，倒换到保护链路上
exercise|练习命令，不作任何倒换
force-switch-work|强制业务到工作
manual-switch-work|人工倒换命令，业务走工作
缺省 : 
无 
使用说明 : 
Clear可以清除所有倒换命令，还可以清楚WTR状态。其他命令之间有先后秩序，高优先级的命令可以抢占低优先级的命令，之间的优先级如下：lock-out > force-switch-work >force-switch > manual-switch-work > manual-switch > exercise 
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protectZXROSNG(config-aps-linear-protect)# port-group  11ZXROSNG(config-aps-linear-protect-portgroup-11)#switch lockout ZXROSNG(config-aps-linear-protect-portgroup-11)#
相关命令 : 
show aps linear-protect 
## tunnel-group 

tunnel-group 
命令功能 : 
创建隧道保护组APS实例或者进入APS隧道保护模式 
命令模式 : 
 APS线性保护模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel-group 
  ＜LinearProtectId 
＞
命令参数解释 : 
参数|描述
---|---
＜LinearProtectId＞|隧道保护组ID，范围为1~$#67305513#$
缺省 : 
无 
使用说明 : 
1、在某个隧道保护组还没有配置APS策略时，使用该命令报错；2、在某个隧道保护组已配置APS策略时，使用该命令进入APS端口保护模式
范例 : 
ZXROSNG(config)#apsZXROSNG(config-aps)#linear-protect ZXROSNG(config-aps-linear-protect)#tunnel-group 1%Error 120420: The switching strategy of this protection group instance has not been configured
相关命令 : 
前置配置为tunnel-group 11protect-type 1:1 bidirectional receiving bothworking-tunnel 811protect-tunnel 812protect-strategy aps commitex相关SHOW命令为：show aps linear-protect tunnel-group 11
# LDP配置命令 
## access-fec 

access-fec 
命令功能 : 
控制LDP实例可以为本VPN域中的哪些目的网段创建FEC项以及是否为通过BGP方式获取的路由网段创建FEC，即FEC过滤策略。使用no命令禁止这一特性。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
access-fec 
  {bgp 
|ipv6-bgp 
|ip-prefix 
 {host-route-only 
|for 
 ＜acl-name 
＞}|ipv6-prefix 
 {host-route-only 
|for 
 ＜acl-name 
＞}|cgn 
|ipv6-cgn 
}
no access-fec 
  {bgp 
|ipv6-bgp 
|ip-prefix 
|ipv6-prefix 
|cgn 
|ipv6-cgn 
}
				
命令参数解释 : 
参数|描述
---|---
bgp|指定为通过BGP获得的路由网段创建FEC
ipv6-bgp|指定为通过BGP IPv6获得的路由网段创建FEC
host-route-only|指定仅为32位掩码的目的网段即主机地址创建FEC
for|指定目的网段
＜acl-name＞|指定过滤哪些目的网段
host-route-only|指定仅为32位掩码的目的网段即主机地址创建FEC
for|指定目的网段
＜acl-name＞|指定过滤哪些目的网段
cgn|指定为通过CGN获得的路由网段创建FEC
ipv6-cgn|指定为通过CGN IPv6获得的路由网段创建FEC
No参数|描述
---|---
ip-prefix|指定IP前缀
ipv6-prefix|指定IPv6前缀
缺省 : 
缺省情况下，LDP实例为本VPN域中的所有目的网段创建FEC项。但是不为通过BGP和CGN方式获取的路由网段创建FEC。 
使用说明 : 
使用场景1、缺省情况下，LDP实例为本VPN域中的所有目的网段创建FEC项, 除了通过BGP获取的路由网段外。但是网络中网段数量可能过于庞大，需要对不必创建FEC的网段进行过滤；或者网络管理者可能希望将FEC项的创建置于控制之中，即只为得到许可的网段创建FEC项，本命令即提供了这样的手段。2、access-fec ip-prefix|ipv6-prefix for < acl-name <prefix-access-list>命令可以将策略配置成按访问列表过滤，所有为访问列表“permit”的目的地址均可创建FEC，否则不创建FEC。3、access-fec ip-prefix |ipv6-prefix host-route-only命令将配置策略配置成仅为32位掩码(IPv4)或128位掩码(IPv6)的目的地址创建FEC。access-fec ip-prefix ipv6-prefix host-route-only命令在开展MPLS/BGP VPN业务的应用中很有效，因为在该应用场合，LDP的目的只是交换VPN路由的“下一跳地址”的标签（即外层标签，到达PE的标签），使用access-fec {ip-prefix|ipv6-prefix }host-route-only命令可以有效地减少FEC的数量。4、access-fec {bgp|ipv6-bgp}命令跟上述两种策略不冲突。系统默认是不为通过BGP方式获取的路由网段创建FEC的。此命令可使系统为BGP方式获取的路由网段也创建FEC。注意事项for < acl-name <prefix-access-list>和host-route-only两种策略模式是互斥的，任何时候网络管理者只能选择一种控制策略。
范例 : 
路由器上的LDP实例被配置成仅为32位掩码的目的地址创建FEC：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#access-fec ip-prefix host-route-only路由器上的LDP实例被配置成仅为128位掩码的目的地址创建FEC：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#access-fec ipv6-prefix host-route-only配置路由器上的LDP实例仅创建10.101.0.0和10.221.0.0网段的标签：ZXROSNG(config)#ipv4-access-list 10ZXROSNG(config-ipv4-acl)#rule 1 permit 10.101.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#rule 2 permit 10.221.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#rule 3 deny anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#access-fec ip-prefix for 10配置路由器上的LDP实例仅创建1:1::1:1和2:2::2:2目的地址的标签：ZXROSNG(config)#ipv6-access-list 6ZXROSNG(config-ipv6-acl)#rule 1 permit ipv6 1:1::1:1/64 anyZXROSNG(config-ipv6-acl)#rule 2 permit ipv6 2:2::2:2/64 anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#access-fec ipv6-prefix for 6路由器上的LDP实例被配置成为通过BGP IPv4获取的路由网段创建FEC：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#access-fec bgp路由器上的LDP实例被配置成为通过BGP IPv6获取的路由网段创建FEC：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#access-fec ipv6-bgp路由器上的LDP实例被配置成为通过CGN IPv4获取的路由网段创建FEC：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#access-fec cgn路由器上的LDP实例被配置成为通过CGN IPv6获取的路由网段创建FEC：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#access-fec ipv6-cgn
相关命令 : 
show mpls ldp bindings 
## apply arp 

apply arp 
命令功能 : 
使该冗余组应用于某种应用。该应用可以在iccp会话上传递应用冗余数据。 
命令模式 : 
 冗余组模式  
命令默认权限级别 : 
15 
命令格式 : 
apply arp 
 
no apply arp 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景冗余配置模式下输入该命令。
范例 : 
配置冗余组分别应用于arp：ZXROSNG(config)#redundancy interchassis group 1ZXROSNG(config-rg-1)#peer 2.2.2.2ZXROSNG(config-rg-1)#apply arp查看配置结果信息：ZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 2.2.2.2      IccpState: ICCP_NONCONNECT    AppType: arp      AppState: APP_NONCONNECT删除配置：ZXROSNG(config-rg-1)#no apply arp命令及参数注释显示：ZXROSNG(config-rg-1)#apply ?mc-port   Apply mc-port mc-pw     Apply mc-pw mlacp     Apply mlacparp       Apply arp
相关命令 : 
redundancy interchassis groupshow mpls ldp iccp
## apply mac 

apply mac 
命令功能 : 
使该冗余组应用于MAC。MAC可以在ICCP会话上传递应用冗余数据。 
命令模式 : 
 冗余组模式  
命令默认权限级别 : 
15 
命令格式 : 
apply mac 
 
no apply mac 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
前提要求配置冗余组。使用场景在冗余组下应用MAC，该MAC主要在ICCP会话上传递冗余数据。
范例 : 
配置冗余组应用于MAC：ZXROSNG(config)#redundancy interchassis group 1ZXROSNG(config-rg-1)#peer 2.2.2.2ZXROSNG(config-rg-1)#apply mac查看配置结果信息：ZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 2.2.2.2      IccpState: ICCP_NONCONNECT    AppType: mLACP      AppState: APP_NONCONNECT    AppType: mc-port      AppState: APP_NONCONNECT    AppType: mc-pw      AppState: APP_NONCONNECT    AppType: ARP      AppState: APP_NONCONNECT    AppType:MAC      AppState: APP_NONCONNECTZXROSNG(config-rg-1)#删除配置：ZXROSNG(config-rg-1)#no apply macZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 2.2.2.2      IccpState: ICCP_NONCONNECT    AppType: mLACP      AppState: APP_NONCONNECT    AppType: mc-port      AppState: APP_NONCONNECT    AppType: mc-pw      AppState: APP_NONCONNECT    AppType: ARP      AppState: APP_NONCONNECTZXROSNG(config-rg-1)#
相关命令 : 
redundancy interchassis groupshow mpls ldp iccp
## apply mc-port 

apply mc-port 
命令功能 : 
使该冗余组应用于某种应用。该应用可以在iccp会话上传递应用冗余数据。 
命令模式 : 
 冗余组模式  
命令默认权限级别 : 
15 
命令格式 : 
apply mc-port 
 
no apply mc-port 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景冗余配置模式下输入该命令。
范例 : 
配置冗余组分别应用于mc-port、mc-pw：ZXROSNG(config)#redundancy interchassis group 1ZXROSNG(config-rg-1)#peer 2.2.2.2ZXROSNG(config-rg-1)#apply mc-portZXROSNG(config-rg-1)#apply mc-pw查看配置结果信息：ZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 2.2.2.2      IccpState: ICCP_NONCONNECT    AppType: mc-port      AppState: APP_NONCONNECT    AppType: mc-pw      AppState: APP_NONCONNECTZXROSNG(config-rg-1)#删除配置：ZXROSNG(config-rg-1)#no apply mc-port ZXROSNG(config-rg-1)#no apply mc-pw ZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 2.2.2.2      IccpState: ICCP_NONCONNECTZXROSNG(config-rg-1)#命令及参数注释显示：ZXROSNG(config-rg-1)#apply ?mc-port   Apply mc-port mc-pw     Apply mc-pw
相关命令 : 
redundancy interchassisshow mpls ldp iccp
## apply mc-pw 

apply mc-pw 
命令功能 : 
使该冗余组应用于某种应用。该应用可以在iccp会话上传递应用冗余数据。 
命令模式 : 
 冗余组模式  
命令默认权限级别 : 
15 
命令格式 : 
apply mc-pw 
 
no apply mc-pw 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景冗余配置模式下输入该命令。
范例 : 
配置冗余组分别应用于mc-port、mc-pw：ZXROSNG(config)#redundancy interchassis group 1ZXROSNG(config-rg-1)#peer 2.2.2.2ZXROSNG(config-rg-1)#apply mc-portZXROSNG(config-rg-1)#apply mc-pw查看配置结果信息：ZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 2.2.2.2      IccpState: ICCP_NONCONNECT    AppType: mc-port      AppState: APP_NONCONNECT    AppType: mc-pw      AppState: APP_NONCONNECTZXROSNG(config-rg-1)#删除配置：ZXROSNG(config-rg-1)#no apply mc-port ZXROSNG(config-rg-1)#no apply mc-pw ZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 2.2.2.2      IccpState: ICCP_NONCONNECTZXROSNG(config-rg-1)#命令及参数注释显示：ZXROSNG(config-rg-1)#apply ?mc-port   Apply mc-port mc-pw     Apply mc-pw
相关命令 : 
redundancy interchassis groupshow mpls ldp iccp
## apply mlacp 

apply mlacp 
命令功能 : 
使该冗余组应用于某种应用。该应用可以在iccp会话上传递应用冗余数据。 
命令模式 : 
 冗余组模式  
命令默认权限级别 : 
15 
命令格式 : 
apply mlacp 
 
no apply mlacp 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景冗余配置模式下输入该命令。
范例 : 
配置冗余组分别应用于mlacp：ZXROSNG(config)#redundancy interchassis group 1ZXROSNG(config-rg-1)#peer 2.2.2.2ZXROSNG(config-rg-1)#apply mlacp查看配置结果信息：ZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 2.2.2.2      IccpState: ICCP_NONCONNECT    AppType: mlacp      AppState: APP_NONCONNECT删除配置：ZXROSNG(config-rg-1)#no apply mlacp命令及参数注释显示：ZXROSNG(config-rg-1)#apply ?mc-port   Apply mc-port mc-pw     Apply mc-pw mlacp     Apply mlacp
相关命令 : 
redundancy interchassis groupshow mpls ldp iccp
## auto-config interface global 

auto-config interface global 
命令功能 : 
对应LDP实例下的所有LDP IPv4接口去使能LDP自动配置功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
auto-config interface global 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能全局IPv4自动配置功能
disable|去使能全局IPv4自动配置功能
缺省 : 
默认状态LDP接口的自动配置功能为使能状态 
使用说明 : 
使用场景该命令去使能实例下所有LDP IPv4接口的自动配置功能。注意事项1、默认状态LDP接口的自动配置功能为使能状态。配置enable后为默认状态，show  run不显示enable命令。2、该命令是个全局的配置命令，在去使能LDP自动配置功能之后，将不会进行LDP接口的自动创建。3、所有接口上的LDP Hello收发、LDP会话创建将不再受该接口上的IGP状态影响，由LDP接口配置决定。
范例 : 
去使能实例1下所有接口的自动配置功能：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# auto-config interface global disable删除配置：ZXROSNG(config-ldp-1)# auto-config interface global enable
相关命令 : 
auto-config interface <interface> disable 
## auto-config interface 

auto-config interface 
命令功能 : 
去使能LDP实例下的特定LDP IPv4接口的自动配置功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
auto-config interface 
  ＜interface-name 
＞ {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
enable|使能接口IPv4自动配置功能
disable|去使能接口IPv4自动配置功能
缺省 : 
默认状态LDP接口的自动配置功能为使能状态。 
使用说明 : 
使用场景该命令去使能实例下单个LDP IPv4接口的自动配置功能。如果实例下配置了全局的去使能自动配置功能，则不管针对接口是否有使能、去使能自动配置功能，都以全局的去使能配置为最高优先级。注意事项1、默认状态LDP接口的自动配置功能为使能状态。配置enable后为默认状态，show  run不显示enable命令。2、当实例下没有配置全局的去使能自动配置功能，也就是默认使能自动配置时，再检查单个接口是否去使能自动配置，有单个接口的配置，则表示该接口不会被自动创建。
范例 : 
当gei-0/1/0/3、gei-0/1/0/4口都属于公网时，在LDP公网实例下配置gei-0/1/0/3接口去使能自动配置和全局去使能自动配置，则以全局配置为最高优先级。所有接口，包括gei-0/1/0/3、gei-0/1/0/4接口，都不会自动被创建为LDP接口。配置如下：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# auto-config interface gei-0/1/0/3 disableZXROSNG(config-ldp-1)# auto-config interface global disable当使能全局配置后，相当于恢复为默认配置。则之前配置的gei-0/1/0/3接口的去使能生效，即不会为gei-0/1/0/3接口自动创建LDP接口，配置如下：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# auto-config interface global enable当使能接口自动配置后，相当于恢复接口的默认配置。则如果有IGP协议触发需要为接口gei-0/1/0/3自动创建LDP接口，则LDP协议会自动为该接口使能LDP功能，通过该接口发送hello。ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# auto-config interface gei-0/1/0/3 enable
相关命令 : 
auto-cofing interface global disable 
## auto-config ipv6 interface global 

auto-config ipv6 interface global 
命令功能 : 
对应LDP实例下的所有LDP IPv6接口去使能LDP自动配置功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
auto-config ipv6 interface global 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能全局IPv6自动配置功能
disable|去使能全局IPv6自动配置功能
缺省 : 
默认状态LDP IPv6接口的自动配置功能为使能状态。 
使用说明 : 
使用场景该命令去使能实例下所有LDP IPv6接口的自动配置功能。注意事项1、默认状态LDP接口的自动配置功能为使能状态。配置enable后为默认状态，show  run不显示enable命令。2、该命令是个全局的配置命令，在去使能LDP IPv6自动配置功能之后，将不会进行LDP IPv6接口的自动创建。3、所有接口上的LDP Hello收发、LDP会话创建将不再受该接口上的IGP状态影响，由LDP接口配置决定。
范例 : 
去使能实例1下所有ipv6接口的自动配置功能：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# auto-config ipv6 interface global disable使能配置：ZXROSNG(config-ldp-1)# auto-config ipv6 interface global enable
相关命令 : 
auto-config interface <interface> disableauto-config interface global disableauto-config ipv6 interface <interface> disable
## auto-config ipv6 interface 

auto-config ipv6 interface 
命令功能 : 
去使能LDP实例下的特定LDP IPv6接口的自动配置功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
auto-config ipv6 interface 
  ＜interface-name 
＞ {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
enable|使能接口IPv6自动配置功能
disable|去使能接口IPv6自动配置功能
缺省 : 
默认状态LDP IPv6接口的自动配置功能为使能状态。 
使用说明 : 
使用场景该命令去使能实例下单个LDP IPv6接口的自动配置功能。如果实例下配置了全局的IPv6去使能自动配置功能，则不管针对接口是否有使能、去使能自动配置功能，都以全局的去使能配置为最高优先级。注意事项1、默认状态LDP IPv6接口的自动配置功能为使能状态。配置enable后为默认状态，show  run不显示enable命令。2、当实例下没有配置全局的去使能自动配置功能，也就是默认使能自动配置时，再检查单个接口是否去使能自动配置，有单个接口的配置，则表示该接口不会被自动创建。
范例 : 
当gei-0/1/0/3、gei-0/1/0/4口都属于公网时，在LDP公网实例下配置gei-0/1/0/3接口去使能IPv6自动配置和全局去使能IPv6自动配置，则以全局配置为最高优先级。所有接口，包括gei-0/1/0/3、gei-0/1/0/4接口，都不会自动被创建为LDP接口。配置如下：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# auto-config ipv6 interface gei-0/1/0/3 disableZXROSNG(config-ldp-1)# auto-config ipv6 interface global disable当使能全局配置后，相当于恢复为默认配置。则之前配置的gei-0/1/0/3接口的去使能生效，即不会为gei-0/1/0/3接口自动创建LDP接口，配置如下：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# auto-config ipv6 interface global enable当使能接口IPv6自动配置后，相当于恢复接口的默认配置。则如果有IGP协议触发需要为接口gei-0/1/0/3自动创建LDP接口，则LDP协议会自动为该接口使能IPv6 LDP功能，通过该接口发送hello。ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# auto-config ipv6 interface gei-0/1/0/3 enable
相关命令 : 
auto-cofing interface global disableauto-config interface <interface> disableauto-config ipv6 interface global disable
## auto-relocalization 

auto-relocalization 
命令功能 : 
该命令工作于标签管理模式下，用于配置自动调度空闲标签资源的能力。标签管理模块处于共享模式时（由产品规格确定），可实现各个动态协议标签池（如，LDP、PWE3、RSVP等等）之间标签资源的自动调度。即，一个标签池中存在多余的空闲标签时，这些空闲标签可以调度到其他标签池中（存在多余的空闲标签是指本标签池的标签总数大于预留标签数量，且存在本协议暂未使用的标签）。本命令可控制该自动调度能力的关闭或者开启。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
auto-relocalization 
  {disable 
|enable 
}
命令参数解释 : 
参数|描述
---|---
disable|使能自动调度能力。
enable|开启自动调度空闲标签资源功能。
缺省 : 
关闭自动调度能力。 
使用说明 : 
    拥有管理员权限的操作员可以使用这条命令。    使能自动调度能力，只要标签池中还有空闲标签，无论哪个业务申请标签，都应该能够获得标签资源，因为即使空闲标签被分配到别的动态协议中，也能通过调度使其流动过来，但这种流动无法保证是实时的。系统默认使能自动调度能力。    关闭自动调度能力，即不支持这种智能的空闲标签调度方式。    最多可以配置1条
范例 : 
开启自动调度能力，则输入以下命令：ZXROSNG(config-lm)# auto-relocalization enable关闭自动调度能力，则输入以下命令：ZXROSNG(config-lm)# auto-relocalization disable
相关命令 : 
show mpls label managempls label manage
## backoff 

backoff 
命令功能 : 
配置实例的LDP会话退避重建机制的参数，使用no命令恢复缺省值。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
backoff 
  ＜initial-backoff-time 
＞ ＜maximum-backoff-time 
＞
no backoff 
命令参数解释 : 
参数|描述
---|---
＜initial-backoff-time＞|最初退避时间，范围：10–65535，单位：秒
＜maximum-backoff-time＞|最大退避时间，范围：10–65535，单位：秒
缺省 : 
缺省情况下，指定最初的退避时间是15秒，指定最大的退避时间是120秒。 
使用说明 : 
使用场景LDP会话退避重建机制防止两个配置不兼容的LSR陷入无休止的会话建立-失败的循环，如果LSR由于配置不兼容会话建立失败，两个LSR都推迟下一次建立会话的尝试（即退避），退避时间按指数增加直至达到最大的退避时间。注意事项LDP会话退避重建机制参数的缺省值是由LDP协议规范规定的，只有缺省参数确实导致了不良的行为，才有必要改变缺省配置。
范例 : 
配置最初的退避时间是30秒，指定最大的退避时间是240秒：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#backoff 30 240ZXROSNG(config-ldp-1)#show mpls ldp backoff instance 1LDP initial/maximum backoff: 30/240 secZXROSNG(config-ldp-1)#no backoff ZXROSNG(config-ldp-1)#show mpls ldp backoff instance 1LDP initial/maximum backoff: 15/120 sec
相关命令 : 
show mpls ldp backoff  
## bfd ipv6 

bfd ipv6 
命令功能 : 
配置LDP IPv6 LSP BFD相关参数，并触发创建IPv6 LSP的BFD会话。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
bfd ipv6 
  ＜ipv6-address 
＞ ＜mask-length 
＞ interval 
 ＜minimum-send-interval 
＞ min-rx 
 ＜minimum-receive-interval 
＞ multiplier 
 ＜multiplier 
＞ [[source 
 ＜source ipv6-address 
＞] [protect-unbinding 
]]
no bfd ipv6 
  ＜ipv6-address 
＞ ＜mask-length 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|指定建立BFD的IPv6 LSP地址，一般为一个远端地址网段
＜mask-length＞|指定远端网址的子网掩码长度，范围：0–128
＜minimum-send-interval＞|指定期望的报文最小发送间隔时间，范围：$#35389448#$-$#35389449#$，单位：ms
＜minimum-receive-interval＞|指定期望的报文最小接收间隔时间，范围：$#35389450#$-$#35389451#$，单位：ms
＜multiplier＞|指定检测超时的倍数，范围：3–50
＜source ipv6-address＞|指定源IPv6地址
protect-unbinding|保护不绑定标记。配置了该选项表征不绑定；否则表征绑定
缺省 : 
无 
使用说明 : 
使用场景该命令触发IPv6 LSP BFD的创建，并且指定IPv6 LSP的网段地址。
范例 : 
配置触发创建2:2::2:2 LSP的BFD的建立：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#bfd ipv6 2:2::2:2 128 interval 50 min-rx 50 multiplier 3 source 12::2 protect-unbinding删除配置：ZXROSNG(config-ldp-1)#no bfd ipv6 2:2::2:2 128
相关命令 : 
无 
## bfd 

bfd 
命令功能 : 
配置LDP LSP BFD相关参数，并触发创建LSP的BFD会话。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
bfd 
  ＜ip-address 
＞ ＜mask-length 
＞ interval 
 ＜minimum-send-interval 
＞ min-rx 
 ＜minimum-receive-interval 
＞ multiplier 
 ＜multiplier 
＞ [[source 
 ＜source ip-address 
＞] [protect-unbinding 
]]
no bfd 
  ＜ip-address 
＞ ＜mask-length 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|指定建立BFD的LSP地址，一般为一个远端地址网段
＜mask-length＞|指定远端网址的子网掩码长度，范围：0–32
＜minimum-send-interval＞|指定期望的报文最小发送间隔时间，范围：$#35389448#$-$#35389449#$，单位：ms
＜minimum-receive-interval＞|指定期望的报文最小接收间隔时间，范围：$#35389450#$-$#35389451#$，单位：ms
＜multiplier＞|指定检测超时的倍数，范围：3–50
＜source ip-address＞|指定源地址
protect-unbinding|FRR或ECMP保护切换开关
缺省 : 
无 
使用说明 : 
使用场景该命令触发LSP BFD的创建，并且指定LSP的网段地址。
范例 : 
配置触发创建2.2.2.2 LSP的BFD的建立：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#bfd 2.2.2.2 32 interval 50 min_rx 50 multiplier 3ZXROSNG(config-ldp-1)#bfd 2.2.2.2 32 interval 50 min_rx 50 multiplier 3 source 10.10.10.1删除配置：ZXROSNG(config-ldp-1)#no bfd 6.6.6.6 32
相关命令 : 
无 
## bier-label-range 

bier-label-range 
命令功能 : 
用于配置BIER标签范围。标签管理模块处于共享模式时（本产品为$#117571622:0/非共享模式;1/共享模式#$），可通过该命令设置全局标签范围内某段标签范围被BIER业务使用。可通过该命令实现BIER标签范围的新建、修改、删除。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
bier-label-range 
  ＜label-min 
＞ ＜label-max 
＞
no bier-label-range 
命令参数解释 : 
参数|描述
---|---
＜label-min＞|用于配置BIER标签范围最小值。 取值范围：标签范围大小16-1048575。默认值为$#117571658#$。
＜label-max＞|用于配置BIER标签范围最大值。 取值范围：标签范围大小16-1048575。默认值为$#117571659#$。
缺省 : 
BIER段配置范围为$#117571658#$- $#117571659#$。如果是0-0，表示不支持BIER标签段。 
使用说明 : 
1）本命令可以设置BIER业务的标签范围，该标签范围不可超过全局标签值范围（$#117571585#$ - $#117571586#$），该配置范围不可与动态锁定范围，静态业务，kompella等业务标签范围有重叠。2） 使用no命令删除BIER标签范围，让其恢复默认值。
范例 : 
配置BIER标签范围，最小值为100，最大值为200，则输入以下命令：ZXROSNG(config-lm)#bier-label-range 100 200删除配置的BIER标签范围：ZXROSNG(config-lm)#no bier-label-range
相关命令 : 
show mpls label manage 
## capability mbb 

capability mbb 
命令功能 : 
使能MLDP的make before break功能。进入MLDP MBB模式 
命令模式 : 
 MLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
capability mbb 
 
no capability mbb 
命令参数解释 : 
					无
				 
缺省 : 
使能了MBB功能缺省情况下，等待时间为5秒，5秒后如果新的LSP还没有建立，直接切换到达到根节点的新P2MP LSP。 
使用说明 : 
使用场景MBB功能是MLDP的辅助功能，缺省情况下不使能，该功能主要是为了减少由于路由变化等原因引起的丢包。使能MBB后，在新的LSP建立前仍然在旧的LSP上进行报文转发，直到新的LSP建立或者等待时间到达。
范例 : 
路由器上使能MBB：ZXROSNG(config)#mpls ldp instance 1  ZXROSNG(config-ldp-1)#mldpZXROSNG(config-ldp-1-mldp)#capability mbb ZXROSNG(config-ldp-1-mldp-mbb)#
相关命令 : 
show running-config 
## capability 

capability 
命令功能 : 
配置对端routerid过滤策略，来判断LDP会话初始化消息是否携带能力参数。
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
capability 
 for 
 ＜acl-name 
＞
no capability 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|acl策略名
缺省 : 
默认初始化消息携带能力参数 
使用说明 : 
使用场景该命令触发对满足acl策略的remote-routerid会话建立时，初始化消息携带能力参数；注意事项1、对后续建立的会话生效，如有session已经UP则提示告警%Info 129: The sessions which are already up should be restarted to make this config take effect。2、对ACL策略内容的变化不提示告警。3、ICCP会话不做过滤。
范例 : 
配置触发remote-router id为2.2.2.2的会话初始化消息携带能力参数，其它会话不携带能力参数：ZXROSNG(config)#ipv4-access-list 1ZXROSNG(config-ipv4-acl)#rule 1 permit 2.2.2.2ZXROSNG(config-ipv4-acl)#rule 2 deny anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#capability for 1 
相关命令 : 
无 
## clear mpls ldp 

clear mpls ldp 
命令功能 : 
重置路由器上LDP实例的所有连接或与某邻居的连接。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear mpls ldp 
 instance 
 ＜instance-id 
＞ [neighbor 
 ＜lsr-id 
＞]
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待重置实例的实例号
＜lsr-id＞|重置与指定邻居的连接，十进制点分形式
缺省 : 
无 
使用说明 : 
使用场景路由器重置中断并重建LDP实例的所有LDP会话，进行advertise和request策略重查，进行显式弹出标签通告策略重查；重置与LDP实例指定邻居的会话仅中断并重建与该邻居LDP会话。只进行与该邻居有关的策略(advertise、request和exp-null策略)重查。
范例 : 
重置LDP实例1的所有会话，输入yes为确定重置，no为不重置：ZXROSNG#clear mpls ldp instance 1Are you sure to clear the MPLS LDP neighbors? [yes/no]:no重置LDP实例1下邻居为100.1.1.1的会话：ZXROSNG#clear mpls ldp instance 1  neighbor 100.1.1.1Are you sure to clear the MPLS LDP neighbors? [yes/no]:yes
相关命令 : 
无 
## debug ldp advertisements 

debug ldp advertisements 
命令功能 : 
监视LDP实例向LDP邻居通告的地址和标签。使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp advertisements 
 instance 
 ＜instance-id 
＞
no debug ldp advertisements 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景监视向LDP邻居通告的标签和地址信息。
范例 : 
监视向LDP邻居通告的地址和标签：ZXROSNG#debug ldp advertisements instance 1MPU-0/20/0 2010-7-19 08:55:49 mpls_ldp_1: tagcon: peer 64.64.64.2:0: advertise 64.64.64.0/24, label 3MPU-0/20/0 2010-7-19 08:55:49 mpls_ldp_1: tagcon: peer 64.64.64.2:0: advertise 100.0.0.255/32, label 16384MPU-0/20/0 2010-7-19 08:55:49 mpls_ldp_1: tagcon: peer 64.64.64.2:0: advertise 100.0.0.254/32, label 16385MPU-0/20/0 2010-7-19 08:55:49 mpls_ldp_1: tagcon: peer 64.64.64.2:0: advertise 100.0.0.253/32, label 16386MPU-0/20/0 2010-7-19 08:55:49 mpls_ldp_1: tagcon: peer 64.64.64.2:0: advertise 100.0.0.252/32, label 16387域信息描述表：域    描述tagcon    表明调试信息来自标签控制子系统peer a.b.c.d:e    对端的LDP标识advertise    通告的标签和地址
相关命令 : 
show debug ldp 
## debug ldp all 

debug ldp all 
命令功能 : 
打开LDP相关的所有debug开关。使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp all 
  [instance 
 ＜instance-id 
＞]
no debug ldp all 
  [instance 
 ＜instance-id 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景该命令用来打开LDP实例下所有监视开关。
范例 : 
打开所有LDP实例相关的所有debug开关：ZXROSNG#debug ldp all instance 1All LDP debugging has been turned on查看配置结果信息：ZXROSNG#show debug ldpLDP:  Instance 1:    LDP label and address advertisements debugging is on    LDP Label Information Base (LIB) changes debugging is on    LDP received messages debugging is on    LDP sent messages debugging is on    LDP session I/O debugging is on    LDP session state machine (low level) debugging is on    LDP transport connection events debugging is on    LDP transport events debugging is on    LDP GR events debugging is on
相关命令 : 
show debug ldp 
## debug ldp bindings 

debug ldp bindings 
命令功能 : 
监视LDP邻居通告的地址和标签。使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp bindings 
 instance 
 ＜instance-id 
＞
no debug ldp bindings 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景该命令主要用来监视LDP邻居通告的地址和标签信息。
范例 : 
打开监视LDP邻居通告的地址和标签开关：ZXROSNG#debug ldp bindings instance 1MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(34.0.0.0/8): created; find route tags requestMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(34.0.0.0/8): label 3 assignedMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(203.0.7.7/32): created; find route tags requestMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(203.0.7.7/32): label 24 assignedMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(144.0.0.44/32): created; find route tags requestMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(144.0.0.44/32): label 33 assignedMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: Assign peer id; 144.0.0.44:0:id 0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: 144.0.0.44:0:144.0.0.44 added to addr<->ldp ident mapMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: 144.0.0.44:0:34.0.0.44 added to addr<->ldp ident mapMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: 144.0.0.44:0:45.0.0.44 added to addr<->ldp ident mapMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(144.0.0.44/32): label 3 from 144.0.0.44:0 addedMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(34.0.0.0/8): label 3 from 144.0.0.44:0 addedMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(45.0.0.0/8): label 3 from 144.0.0.44:0 addedMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(107.0.0.0/8): created; remote label learnedMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: tagcon: tibent(107.0.0.0/8): label 55 from 144.0.0.44:0 added查看配置结果信息：ZXROSNG#show debug ldp instance 1LDP:  Instance 1:    LDP label and address advertisements debugging is on    LDP Label Information Base (LIB) changes debugging is on域信息描述表：域    描述tagcon    表明调试信息来自标签控制子系统tibent    发生绑定事件的LIB项created；（reason）    LIB项因为给出的原因而创建a.b.c.d:e    对端的LDP标识
相关命令 : 
show debug ldp 
## debug ldp graceful-restart 

debug ldp graceful-restart 
命令功能 : 
监视LDP GR的详细信息。使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp graceful-restart 
 instance 
 ＜instance-id 
＞
no debug ldp graceful-restart 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景该命令主要用来监视LDP GR的相关信息。
范例 : 
监视LDP实例1下GR的具体相关信息：ZXROSNG#debug ldp graceful-restart instance 1MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1:GR: GR session 20.20.0.3:1:: established\nMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1:GR: ptcl_adj: 20.20.0.3:1:: reconnect timer stopped MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: GR: GR session 20.20.0.3:1:: recovery timer expiredMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: GR: GR session 20.20.0.3:1:: state change (Reconnect-Wait -> Recovering)MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: GR: ptcl_adj: 20.20.0.3:1:: recovery timer started,150 secsMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: GR: GR session 20.20.0.3:1: lostMPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: GR: down neighbor 20.20.0.3:1::  reconnect timer started [150 secs]MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: GR: GR session 20.20.0.3:1:: bindings retained查看配置结果信息：ZXROSNG#show debug ldp instance 1LDP:  Instance 1:    LDP GR events debugging is on 
相关命令 : 
show debug ldp 
## debug ldp messages received 

debug ldp messages received 
命令功能 : 
监视从LDP邻居接收的消息。使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp messages received 
 instance 
 ＜instance-id 
＞
no debug ldp messages received 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景监视从LDP邻居接收的相关消息。
范例 : 
监视从LDP邻居接受的消息，包括周期性Keep Alive消息：ZXROSNG#debug ldp messages received instance 1MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd init msg from 144.0.0.44:0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd keepalive msg from 144.0.0.44:0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd address msg from 144.0.0.44:0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd label mapping msg from 144.0.0.44:0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd label mapping msg from 144.0.0.44:0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd label mapping msg from 144.0.0.44:0域信息描述表：域    描述ldp    表明调试信息来自LDP模块Rcvd xxx msg    消息类型from a.b.c.d    从某个路由器收到的消息，用于会话建立的初期，LDP标识未知from a.b.c.d:e to a.b.c.d:e    给出目的/源LDP标识
相关命令 : 
show debug ldp 
## debug ldp messages sent 

debug ldp messages sent 
命令功能 : 
监视向LDP邻居发送的消息。使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp messages sent 
 instance 
 ＜instance-id 
＞
no debug ldp messages sent 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景该命令主要用来监视向LDP邻居发送的消息，主要包括初始化消息、保活消息、地址消息等。
范例 : 
监视向LDP邻居发送的消息，包括周期性Keep Alive消息：ZXROSNG#debug ldp messages sent instance 1MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Sent init msg to 144.0.0.44:0:0 with socket-id(0xb12614d0)MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Sent keepalive msg to 144.0.0.44:0 with socket-id(0xb12614d0)MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Sent address msg to 144.0.0.44:0 with socket-id(0xb12614d0)MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Sent label mapping msg to 144.0.0.44:0 with socket-id(0xb12614d0)域信息描述表：域    描述ldp    表明调试信息来自LDP模块Sent xxx msg    消息类型from a.b.c.d    从某个路由器收到的消息，用于会话建立的初期，LDP标识未知from a.b.c.d:e to a.b.c.d:e    给出目的/源LDP标识
相关命令 : 
show debug ldp 
## debug ldp session io 

debug ldp session io 
命令功能 : 
监视LDP会话活动。监视会话上接收/发送的消息的详细内容，使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp session io 
 instance 
 ＜instance-id 
＞
no debug ldp session io 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景监视会话上收到/发送的相关消息。
范例 : 
监视会话上接收/发送的消息的详细内容：ZXROSNG#debug ldp session io instance 1MPU-0/20/0 2010-3-2 03:53:32 mpls_ldp_1: Sent init msg to 204.1.1.200:0 with socket-id(0x8f77b68)MPU-0/20/0 2010-3-2 03:53:32 mpls_ldp_1: baseMsg: uBit = 0; msgType = 0x200; msgLength = 22; msgId = 0x4MPU-0/20/0 2010-3-2 03:53:32 mpls_ldp_1: CSP: MPU-0/20/0 2010-3-2 03:53:32 mpls_ldp_1:     uBit = 0; fBit = 0; type = 0x500; length = 14MPU-0/20/0 2010-3-2 03:53:32 mpls_ldp_1:     Ver = 1; time = 60; PduLen = 4096; Lsrid = 0xcc0101c8; LblSp = 0MPU-0/20/0 2010-3-2 03:53:32 mpls_ldp_1:     lad = 0; ld = 0; pvl = 0; res = 0MPU-0/20/0 2010-3-2 03:53:33 mpls_ldp_1: Rcvd init msg from 177.1.1.1:0MPU-0/20/0 2010-3-2 03:53:33 mpls_ldp_1: baseMsg: uBit = 0; msgType = 0x200; msgLength = 22; msgId = 0x1f3MPU-0/20/0 2010-3-2 03:53:33 mpls_ldp_1: CSP: MPU-0/20/0 2010-3-2 03:53:33 mpls_ldp_1:     uBit = 0; fBit = 0; type = 0x500; length = 14MPU-0/20/0 2010-3-2 03:53:33 mpls_ldp_1:     Ver = 1; time = 60; PduLen = 4096; Lsrid = 0xcc010164; LblSp = 0MPU-0/20/0 2010-3-2 03:53:33 mpls_ldp_1:     lad = 0; ld = 0; pvl = 0; res = 0……域信息描述表：域    描述ldp    表明调试信息来自LDP模块ptcl_adj:a.b.c.d    给出LDP对端的LDP Idstate    会话状态（参阅状态表）event    会话状态机事件（参阅事件表）
相关命令 : 
show debug ldp 
## debug ldp session state-machine 

debug ldp session state-machine 
命令功能 : 
监视LDP会话活动。监视会话状态机接收的内/外部事件，使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp session state-machine 
 instance 
 ＜instance-id 
＞
no debug ldp session state-machine 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景该命令主要用来监视会话状态机接收的内/外部事件。
范例 : 
监视会话状态机接收的内/外部事件：ZXROSNG#debug ldp session state-machine instance 1MPU-0/20/0 2010-3-2 06:07:40 mpls_ldp_1: ptcl_adj: 204.1.1.200:0: state 1, event: 0xeMPU-0/20/0 2010-3-2 06:07:40 mpls_ldp_1: ptcl_adj: 204.1.1.200:0: state 1 to 6, event: 0xeMPU-0/20/0 2010-3-2 06:07:40 mpls_ldp_1: ptcl_adj: 204.1.1.200:0: state 6, event: 0x12MPU-0/20/0 2010-3-2 06:07:40 mpls_ldp_1: ptcl_adj: 204.1.1.200:0: state 6 to 4, event: 0x12MPU-0/20/0 2010-3-2 06:07:40 mpls_ldp_1: ptcl_adj: 204.1.1.200:0: state 4, event: 0x200MPU-0/20/0 2010-3-2 06:07:40 mpls_ldp_1: ptcl_adj: 204.1.1.200:0: state 4 to 3, event: 0x200MPU-0/20/0 2010-3-2 06:07:40 mpls_ldp_1: ptcl_adj: 204.1.1.200:0: state 3, event: 0x201MPU-0/20/0 2010-3-2 06:07:40 mpls_ldp_1: ptcl_adj: 204.1.1.200:0: state 3 to 5, event: 0x201……域信息描述表：域    描述ldp    表明调试信息来自LDP模块ptcl_adj:a.b.c.d    给出LDP对端的LDP Idstate    会话状态（参阅状态表）event    会话状态机事件（参阅事件表）
相关命令 : 
show debug ldp 
## debug ldp transport connections 

debug ldp transport connections 
命令功能 : 
监视LDP发现的信息。监视和建立TCP连接有关的事件，使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp transport connections 
 instance 
 ＜instance-id 
＞
no debug ldp transport connections 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景监视和建立TCP连接有关的事件。
范例 : 
监视和建立TCP连接有关的事件：ZXROSNG#debug ldp transport connections instance 1MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Opening ldp conn; 204.1.1.100:0<-->177.1.1.1:0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: ldp conn is up; 204.1.1.100:1028<-->177.1.1.1:646……
相关命令 : 
show debug ldp 
## debug ldp transport events 

debug ldp transport events 
命令功能 : 
监视LDP发现的信息。建立和发现机制有关的事件，包括收/发hello消息，使用no命令取消监视。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug ldp transport events 
 instance 
 ＜instance-id 
＞
no debug ldp transport events 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
No参数|描述
---|---
instance|
缺省 : 
无 
使用说明 : 
使用场景主要使用该命令查看Hello消息的收发。
范例 : 
建立和发现机制有关的事件：ZXROSNG#debug ldp transport events instance 1MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd init msg from 144.0.0.44: 0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Send ldp hello; gei-0/1/0/1, scr/dst 204.1.1.100(0.0.0.0)/224.0.0.2MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Send ldp hello; gei-0/1/0/2, scr/dst 196.1.1.100(0.0.0.0)/224.0.0.2MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd ldp hello; gei-0/1/0/1, from 177.1.1.1(204.1.1.200:0)MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: New adj 0 from 177.1.1.1(204.1.1.200:0), 177.1.1.1MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Opening ldp conn; 204.1.1.100:0<-->177.1.1.1:0MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: ldp conn is up; 204.1.1.100:1027<-->177.1.1.1:646MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Send ldp hello; gei-0/1/0/1, scr/dst 204.1.1.100(0.0.0.0)/224.0.0.2MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Send ldp hello; gei-0/1/0/2, scr/dst 196.1.1.100(0.0.0.0)/224.0.0.2MPU-0/20/0 2010-3-2 03:39:39 mpls_ldp_1: Rcvd ldp hello; gei-0/1/0/1, from 177.1.1.1(204.1.1.200:0) 
相关命令 : 
show debug ldp 
## discovery hello 

discovery hello 
命令功能 : 
配置LDP实例的 HELLO发现消息发送间隔，及发现的LDP邻居超时的时间。使用no命令可恢复缺省值。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
discovery hello 
  {holdtime 
 ＜holdtime 
＞|interval 
 ＜interval-time 
＞}
no discovery hello 
  {holdtime 
|interval 
}
				
命令参数解释 : 
参数|描述
---|---
＜holdtime＞|指定LDP实例发现的邻居在收不到后续hello消息的情况下的状态保持时间，范围：1–65535，单位：秒
＜interval-time＞|指定LDP实例周期性发送hello消息的间隔，范围：1–65535，单位：秒
缺省 : 
缺省情况下，指定hello发送间隔是5秒，邻居保持时间是15秒。 
使用说明 : 
使用场景该命令配置LDP实例的 hello发现消息发送间隔，及发现的LDP邻居超时的时间。
范例 : 
设置状态保持时间为100秒，hello发送间隔为20秒：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#discovery hello holdtime 100ZXROSNG(config-ldp-1)#discovery hello interval 20查看配置结果信息：ZXROSNG(config-ldp-1)#show mpls ldp parameters instance 1Protocol version: 1Session holdtime: 180 sec; keep alive interval: 60 secDiscovery hello: holdtime: 100 sec; interval: 20 secDiscovery targeted hello: holdtime: 45 sec; interval: 15 secLDP for targeted sessionsDownstream on Demand max hop count: 255LDP initial/maximum backoff: 15/120 secLDP used lsp control mode: IndependentLDP configred lsp control mode: IndependentLDP used label retention mode: LiberalLDP configred label retention mode: LiberalLDP loop detection: offLDP IGP sync delay: 5 sec
删除配置：ZXROSNG(config-ldp-1)#no discovery hello interval ZXROSNG(config-ldp-1)#no discovery hello holdtime ZXROSNG(config-ldp-1)#show mpls ldp parameters instance 1Protocol version: 1Session holdtime: 180 sec; keep alive interval: 60 secDiscovery hello: holdtime: 15 sec; interval: 5 secDiscovery targeted hello: holdtime: 45 sec; interval: 15 secLDP for targeted sessionsDownstream on Demand max hop count: 255LDP initial/maximum backoff: 15/120 secLDP used lsp control mode: IndependentLDP configred lsp control mode: IndependentLDP used label retention mode: LiberalLDP configred label retention mode: LiberalLDP loop detection: offLDP IGP sync delay: 5 sec
相关命令 : 
show mpls ldp parametersdiscovery targeted-hello
## discovery hello 

discovery hello 
命令功能 : 
配置LDP接口下的 hello发现消息发送间隔，及与此接口相关hello节点超时的时间。使用no命令可恢复缺省值。 
命令模式 : 
 LDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
discovery hello 
  {holdtime 
 ＜holdtime 
＞|interval 
 ＜interval-time 
＞}
no discovery hello 
  {holdtime 
|interval 
}
				
命令参数解释 : 
参数|描述
---|---
＜holdtime＞|指定与此接口相关的hello节点的保持时间，范围：1–65535，单位：秒
＜interval-time＞|指定此接口发送hello消息的间隔，范围：1–65535，单位：秒
缺省 : 
无 
使用说明 : 
使用场景该命令配置接口的 hello发现消息发送间隔，及与此接口相关hello节点超时的时间。注意事项1、如果接口下存在hello发现消息发送间隔，及与此接口相关hello节点超时的时间配置，则接口下的配置生效；2、如果接口下不存在hello发现消息发送间隔，及与此接口相关hello节点超时的时间配置，则LDP模式下对应命令的配置生效；3、如果LDP模式下对应命令也没有配置，则LDP模式下对应命令的默认值生效。
范例 : 
设置保持时间为100秒，hello发送间隔为20秒：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface gei-0/1/0/1ZXROSNG(config-ldp-1-if-gei-0/1/0/1)#discovery hello holdtime 100ZXROSNG(config-ldp-1-if-gei-0/1/0/1)#discovery hello interval 20删除配置：ZXROSNG(config-ldp-1-if-gei-0/1/0/1)#no discovery hello intervalZXROSNG(config-ldp-1-if-gei-0/1/0/1)#no discovery hello holdtime
相关命令 : 
interfaceLDP模式 discovery hello
## discovery hello 

discovery hello 
命令功能 : 
配置LDP  IPv6接口下的 hello发现消息发送间隔，及发现的LDP邻居超时的时间。使用no命令可恢复缺省值。 
命令模式 : 
 LDP-V6接口模式  
命令默认权限级别 : 
15 
命令格式 : 
discovery hello 
  {holdtime 
 ＜holdtime 
＞|interval 
 ＜interval-time 
＞}
no discovery hello 
  {holdtime 
|interval 
}
				
命令参数解释 : 
参数|描述
---|---
＜holdtime＞|指定与此接口相关的hello节点的保持时间，范围：1–65535，单位：秒
＜interval-time＞|指定此接口发送hello消息的间隔，范围：1–65535，单位：秒
缺省 : 
无 
使用说明 : 
使用场景该命令配置接口的 hello发现消息发送间隔，及与此接口相关hello节点超时的时间。注意事项1、如果接口下存在hello发现消息发送间隔，及发现的LDP邻居超时的时间配置，则接口下的配置生效；2、如果接口下不存在hello发现消息发送间隔，及发现的LDP邻居超时的时间配置，则LDP模式下对应命令的配置生效；3、如果LDP模式下对应命令也没有配置，则LDP模式下对应命令的默认值生效。
范例 : 
设置保持时间为100秒，hello发送间隔为20秒：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface ipv6 gei-0/1/0/1ZXROSNG(config-ldp-1-ifv6-gei-0/1/0/1)# discovery hello holdtime 100ZXROSNG(config-ldp-1-ifv6-gei-0/1/0/1)# discovery hello interval 20删除配置：ZXROSNG(config-ldp-1-ifv6-gei-0/1/0/1)# no discovery hello intervalZXROSNG(config-ldp-1-ifv6-gei-0/1/0/1)# no discovery hello holdtime
相关命令 : 
interface ipv6LDP模式 discovery hello
## discovery targeted-hello accept 

discovery targeted-hello accept 
命令功能 : 
配置本端接受远端发送来的target-hello。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
discovery targeted-hello accept 
  [for 
 ＜acl-name 
＞]
no discovery targeted-hello accept 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|指定接受远端target-hello的lsrid 的acl过滤策略
缺省 : 
缺省情况下，在本端没有配置触发建立target会话的配置情况下，不接受远端target-hello。 
使用说明 : 
使用场景该命令在没有带acl参数情况下配置，表示接受所有远端target-hello，并建立target会话，如果配置acl过滤策略，表示只接受或者拒绝指定lsrid的对端发来的target-hello.
范例 : 
配置接受所有target-hello：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#discovery targeted-hello accept  配置acl过滤策略，只接受或者拒绝指定lsrid的对端发来的target-hello：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#discovery targeted-hello accept  for zte删除配置：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#no discovery targeted-hello accept 
相关命令 : 
无 
## discovery targeted-hello holdtime 

discovery targeted-hello holdtime 
命令功能 : 
配置非直连LSR间发现的LDP邻居超时的时间。使用no命令恢复缺省值。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
discovery targeted-hello holdtime 
  ＜target-holdtime 
＞
no discovery targeted-hello holdtime 
命令参数解释 : 
参数|描述
---|---
＜target-holdtime＞|指定LDP实例发现的邻居在收不到后续hello消息的情况下的状态保持时间，范围：1–65535，单位：秒
缺省 : 
缺省情况下邻居保持时间是45秒。 
使用说明 : 
使用场景该命令用来配置非直连LDP实例发现的LDP邻居超时的时间。
范例 : 
设置状态保持时间为110秒：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#discovery targeted-hello holdtime 110查看配置结果信息：ZXROSNG(config-ldp-1)#show mpls ldp parameters instance 1Protocol version: 1Session holdtime: 180 sec; keep alive interval: 60 secDiscovery hello: holdtime: 15 sec; interval: 5 secDiscovery targeted hello: holdtime: 110 sec; interval: 15 secLDP for targeted sessionsDownstream on Demand max hop count: 255LDP initial/maximum backoff: 15/120 secLDP used lsp control mode: IndependentLDP configred lsp control mode: IndependentLDP used label retention mode: LiberalLDP configred label retention mode: LiberalLDP loop detection: offLDP IGP sync delay: 5 sec删除配置：ZXROSNG(config-ldp-1)#no discovery targeted-hello holdtimeZXROSNG(config-ldp-1)#show mpls ldp parameters in 1Protocol version: 1Session holdtime: 180 sec; keep alive interval: 60 secDiscovery hello: holdtime: 15 sec; interval: 5 secDiscovery targeted hello: holdtime: 45 sec; interval: 15 secLDP for targeted sessionsDownstream on Demand max hop count: 255LDP initial/maximum backoff: 15/120 secLDP used lsp control mode: IndependentLDP configred lsp control mode: IndependentLDP used label retention mode: LiberalLDP configred label retention mode: LiberalLDP loop detection: offLDP IGP sync delay: 5 sec
相关命令 : 
show mpls ldp parametersdiscovery hello
## discovery targeted-hello interval 

discovery targeted-hello interval 
命令功能 : 
配置非直连LSR间，LDP hello发现消息发送间隔。使用no命令恢复缺省值。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
discovery targeted-hello interval 
  ＜target-interval-time 
＞
no discovery targeted-hello interval 
命令参数解释 : 
参数|描述
---|---
＜target-interval-time＞|指定LDP实例周期性发送hello消息的间隔，范围：1–65535，单位：秒
缺省 : 
缺省情况下，指定hello发送间隔是15秒。 
使用说明 : 
使用场景该命令配置非直连LDP实例的 hello发现消息发送间隔时间。
范例 : 
设置hello发送间隔为20秒：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#discovery targeted-hello interval 20查看配置结果信息：ZXROSNG(config-ldp-1)#show mpls ldp parameters instance 1Protocol version: 1Session holdtime: 180 sec; keep alive interval: 60 secDiscovery hello: holdtime: 15 sec; interval: 5 secDiscovery targeted hello: holdtime: 45 sec; interval: 20 secLDP for targeted sessionsDownstream on Demand max hop count: 255LDP initial/maximum backoff: 15/120 secLDP used lsp control mode: IndependentLDP configred lsp control mode: IndependentLDP used label retention mode: LiberalLDP configred label retention mode: LiberalLDP loop detection: offLDP IGP sync delay: 5 sec删除配置：ZXROSNG(config-ldp-1)#no discovery targeted-hello intervalZXROSNG(config-ldp-1)#show mpls ldp parameters in 1Protocol version: 1Session holdtime: 180 sec; keep alive interval: 60 secDiscovery hello: holdtime: 15 sec; interval: 5 secDiscovery targeted hello: holdtime: 45 sec; interval: 15 secLDP for targeted sessionsDownstream on Demand max hop count: 255LDP initial/maximum backoff: 15/120 secLDP used lsp control mode: IndependentLDP configred lsp control mode: IndependentLDP used label retention mode: LiberalLDP configred label retention mode: LiberalLDP loop detection: offLDP IGP sync delay: 5 sec
相关命令 : 
show mpls ldp parametersdiscovery hello
## discovery transport-address 

discovery transport-address 
命令功能 : 
该命令在LDP IPv4接口配置模式下配置hello消息中携带的传输地址参数，禁止该特性使用本命令的no格式。 
命令模式 : 
 LDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
discovery transport-address 
  {interface 
|＜ip-address 
＞|ipv6 
 ＜ipv6-address 
＞}
no discovery transport-address 
命令参数解释 : 
参数|描述
---|---
interface|指定使用接口地址作为hello消息通告的传输地址
＜ip-address＞|指定使用某个IPv4地址作为hello消息通告的传输地址
＜ipv6-address＞|指定使用某个IPv6地址作为hello消息通告的传输地址
缺省 : 
缺省情况下，LDP实例将router ID作为传输地址在hello消息中通告。 
使用说明 : 
使用场景1、LDP路由器间建立LDP会话，首先要建TCP 连接，这就要求每个路由器都知道对方的传输地址（IP地址），LDP发现机制提供了LDP实例向对方通告本方使用的建立TCP连接的传输地址的措施。传输地址的通告可以是显式的，即传输地址出现在hello消息中，也可以是隐式的，即传输地址不出现在hello消息中，hello消息的接收者使用hello消息的源IP地址作为与发送方建立TCP连接的传输地址。2、discovery transport-address提供了一个改变LDP实例缺省行为的方法，当二选一的interface参数出现时，LDP在接口上的hello消息中通告接口的IP地址；当IP address参数出现时，LDP在接口上的hello消息中通告指定的IP地址。3、如果在接口运行过程中改变传输地址的配置，LDP实例将解除接口上当前的邻接关系，如果由接口上当前的邻接关系维持的会话没有其它的邻接关系维护（不存在多链路），则会话关闭。邻接关系（和会话）将在下一次收到对端的hello消息后重建。注意事项如果路由器间存在多条链路，那么路由器必须在这些接口上通告同样的传输地址。
范例 : 
在接口gei-0/3/1/8上通告传输地址使用接口的IP地址，在接口gei-0/3/1/8上通告传输地址145.22.0.56，在接口gei-0/3/1/8上通告传输地址5::6，在接口gei-0/3/1/8上通告传输地址fe80::216:3eff:fe64:105：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface gei-0/3/1/8ZXROSNG(config-ldp-1-if-gei-0/3/1/8)#discovery transport-address interfaceZXROSNG(config-ldp-1-if-gei-0/3/1/8)#exitZXROSNG(config-ldp-1)#interface gei-0/3/1/8ZXROSNG(config-ldp-1-if-gei-0/3/1/8)#discovery transport-address 145.22.0.56ZXROSNG(config-ldp-1)#interface gei-0/3/1/8ZXROSNG(config-ldp-1-if-gei-0/3/1/8)#discovery transport-address ipv6 5::6ZXROSNG(config-ldp-1)#interface gei-0/3/1/8ZXROSNG(config-ldp-1-if-gei-0/3/1/8)#discovery transport-address ipv6 fe80::216:3eff:fe64:105
相关命令 : 
无 
## discovery transport-address 

discovery transport-address 
命令功能 : 
该命令在LDP IPv6接口配置模式下配置hello消息中携带的传输地址参数，禁止该特性使用本命令的no格式。 
命令模式 : 
 LDP-V6接口模式  
命令默认权限级别 : 
15 
命令格式 : 
discovery transport-address 
  {＜ip-address 
＞|ipv6 
 ＜ipv6-address 
＞}
no discovery transport-address 
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|指定使用某个IPv4地址作为hello消息通告的传输地址
＜ipv6-address＞|指定使用某个IPv6地址作为hello消息通告的传输地址
缺省 : 
缺省情况下，LDP实例将router ID作为传输地址在hello消息中通告。 
使用说明 : 
使用场景1、LDP路由器间建立LDP会话，首先要建TCP 连接，这就要求每个路由器都知道对方的传输地址（IP地址），LDP发现机制提供了LDP实例向对方通告本方使用的建立TCP连接的传输地址的措施。传输地址的通告可以是显式的，即传输地址出现在hello消息中，也可以是隐式的，即传输地址不出现在hello消息中，hello消息的接收者使用hello消息的源IP地址作为与发送方建立TCP连接的传输地址。2、discovery transport-address提供了一个改变LDP实例缺省行为的方法，当二选一的interface参数出现时，LDP在接口上的hello消息中通告接口的IP地址；当IP address参数出现时，LDP在接口上的hello消息中通告指定的IP地址。3、如果在接口运行过程中改变传输地址的配置，LDP实例将解除接口上当前的邻接关系，如果由接口上当前的邻接关系维持的会话没有其它的邻接关系维护（不存在多链路），则会话关闭。邻接关系（和会话）将在下一次收到对端的hello消息后重建。注意事项如果路由器间存在多条链路，那么路由器必须在这些接口上通告同样的传输地址。
范例 : 
在接口gei-0/3/1/8上通告传输地址145.22.0.56，在接口gei-0/3/1/8上通告传输地址5::6，在接口gei-0/3/1/8上通告传输地址fe80::216:3eff:fe64:105：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface ipv6 gei-0/3/1/8ZXROSNG(config-ldp-1-ifv6-gei-0/3/1/8)#discovery transport-address 145.22.0.56ZXROSNG(config-ldp)#interface ipv6 gei-0/3/1/8ZXROSNG(config-ldp-1-ifv6-gei-0/3/1/8)#discovery transport-address ipv6 5::6ZXROSNG(config-ldp)#interface ipv6 gei-0/3/1/8ZXROSNG(config-ldp-1-ifv6-gei-0/3/1/8)#discovery transport-address ipv6 fe80::216:3eff:fe64:105
相关命令 : 
无 
## egress ipv6 

egress ipv6 
命令功能 : 
控制LDP实例为特定的非直连的目的ipv6网段分配弹出标签，即egress ipv6控制策略。使用no命令禁止这一特性。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
egress ipv6 
  {for 
 ＜acl-name 
＞|nexthop 
 ＜acl-name 
＞}
no egress ipv6 
  {for 
|nexthop 
}
				
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|指定为哪些目的网段分配弹出标签，长度1–31个字符
＜acl-name＞|指定为哪些目的网段分配弹出标签，长度1–31个字符
缺省 : 
缺省情况下，LDP实例只为直连网段分配弹出标签，并向对等LSR通告。 
使用说明 : 
使用场景缺省情况下，LDP实例只为直连网段分配弹出标签，并向对等LSR通告。对于非直连的目的网段，LDP从标签池中取得空闲标签分配作为入标签，并选择路由下一跳发来的mapping消息中的标签值作为出标签。当本LDP实例所在的路由器是边缘LSR时，下一跳路由器可能是非MPLS路由器，则本LSR不能绑定出标签，而数据层面根据MPLS框架协议没有出标签时，丢弃收到的标签分组。这种情况下需要配置egress控制策略，将所有经本LSR流出MPLS网络的目的网段指定LDP分配弹出标签，并向上游通告。使上游LSR以IP包（或显式弹出标签包）形式转发这些流出MPLS网络的流量。注意事项可以选择基于目的网段和基于下一跳两种控制策略。1. 基于ipv6目的网段的egress控制策略（egress ipv6 for <prefix-access-list>）直接指定到哪些目的网段终结于本LSR；2. 基于ipv6下一跳的egress控制策略（egress ipv6 nexthop <nexthop-access-list>）指定哪些邻居是非MPLS路由器，因此以这些邻居为路由下一跳的流量均为流出MPLS域的流量，本路由器为这些流量分配弹出标签。一条路由只要符合这两种策略之一，即目的前缀被<prefix-access-list>所允许（permit）或路由下一跳为<nexthop-access-list>所允许（permit），则LDP为之分配弹出标签。
范例 : 
LDP实例为33::/64网段的子网路由分配弹出标签：ZXROSNG(config)# ipv6-access-list 33ZXROSNG(config-ipv6-acl)# rule 1 permit ipv6 33::/64 anyZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#egress ipv6 for 33LDP实例为所有以fe80::2ee:ffff:fe10:1000/128为下一跳的目的网段分配弹出标签：ZXROSNG(config)# ipv6-access-list hop1ZXROSNG(config-ipv6-acl)# rule 1 permit ipv6 fe80::2ee:ffff:fe10:1000/128 anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#egress ipv6 nexthop hop1删除配置：ZXROSNG(config-ldp-1)#no egress ipv6 forZXROSNG(config-ldp-1)#no egress ipv6 nexthop
相关命令 : 
show mpls ldp bindings 
## egress 

egress 
命令功能 : 
控制LDP实例为特定的非直连的目的网段分配弹出标签，即egress控制策略。使用no命令禁止这一特性。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
egress 
  {for 
 ＜acl-name 
＞|nexthop 
 ＜acl-name 
＞}
no egress 
  {for 
|nexthop 
}
				
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|指定为哪些目的网段分配弹出标签，长度1–31个字符
＜acl-name＞|指定为哪些目的网段分配弹出标签，长度1–31个字符
缺省 : 
缺省情况下，LDP实例只为直连网段分配弹出标签，并向对等LSR通告。 
使用说明 : 
使用场景缺省情况下，LDP实例只为直连网段分配弹出标签，并向对等LSR通告。对于非直连的目的网段，LDP从标签池中取得空闲标签分配作为入标签，并选择路由下一跳发来的mapping消息中的标签值作为出标签。当本LDP实例所在的路由器是边缘LSR时，下一跳路由器可能是非MPLS路由器，则本LSR不能绑定出标签，而数据层面根据MPLS框架协议没有出标签时，丢弃收到的标签分组。这种情况下需要配置egress控制策略，将所有经本LSR流出MPLS网络的目的网段指定LDP分配弹出标签，并向上游通告。使上游LSR以IP包（或显式弹出标签包）形式转发这些流出MPLS网络的流量。注意事项可以选择基于目的网段和基于下一跳两种控制策略。1. 基于目的网段的egress控制策略（egress for <prefix-access-list>）直接指定到哪些目的网段终结于本LSR；2. 基于下一跳的egress控制策略（egress nexthop <nexthop-access-list>）指定哪些邻居是非MPLS路由器，因此以这些邻居为路由下一跳的流量均为流出MPLS域的流量，本路由器为这些流量分配弹出标签。一条路由只要符合这两种策略之一，即目的前缀被<prefix-access-list>所允许（permit）或路由下一跳为<nexthop-access-list>所允许（permit），则LDP为之分配弹出标签。
范例 : 
LDP实例为所有10.101.0.0/16和10.221.0.0/16网段的子网路由分配弹出标签，为所有非10.222.1.0/24网段的子网而且是10.222.0.0/16网段的子网的子网路由分配弹出标签：ZXROSNG(config)#ipv4-access-list 10ZXROSNG(config-ipv4-acl)#rule 1 permit 10.101.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#rule 2 permit 10.221.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#rule 3 deny 10.222.1.0 0.0.0.255ZXROSNG(config-ipv4-acl)#rule 4 permit 10.222.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#egress for 10LDP实例为所有以100.1.1.3为下一跳的目的网段分配弹出标签：ZXROSNG(config)#ipv4-access-list 11ZXROSNG(config-ipv4-acl)#rule 6 permit 100.1.1.3 0.0.0.0ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#egress nexthop 11删除配置：ZXROSNG(config-ldp-1)#no egress for ZXROSNG(config-ldp-1)#no egress nexthop
相关命令 : 
show mpls ldp bindings  
## entropy-label 

entropy-label 
命令功能 : 
LDP实例下使能或者去使能熵标签功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
entropy-label 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能LDP熵标签功能
disable|去使能LDP熵标签功能
缺省 : 
$#67240105#$:0/不开启该功能;1/开启该功能
使用说明 : 
使用场景LDP实例下使能熵标签功能，发送的标签消息中支持携带熵标签能力标志；去使能，发送的标签消息中不支持携带熵标签能力标志。后续操作可以通过show mpls ldp parameters查看当前LDP实例是否使能熵标签功能。
范例 : 
LDP实例下，使能LDP熵标签功能：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# entropy-label enable通过show命令可以查看当前LDP实例是否使能熵标签功能：ZXROSNG(config-ldp-1)#show mpls ldp parameters instance 1Protocol version: 1Session holdtime: 180 sec; Keep alive interval: 60 secDiscovery hello: holdtime: 15 sec; interval: 5 secDiscovery targeted hello: holdtime: 45 sec; interval: 15 secLDP for targeted sessionsDownstream on Demand max hop count: 255LDP initial/maximum backoff: 15/120 secLDP used lsp control mode: IndependentLDP configured lsp control mode: IndependentLDP used label retention mode: LiberalLDP configured label retention mode: LiberalLDP loop detection: offLDP IGP sync delay: 5 secLDP entropy label capability: DisableLDP LSP dod request queue mode: DisableLDP over TE lsp: Disable去使能LDP熵标签功能ZXROSNG(config-ldp-1)# entropy-label disable
相关命令 : 
show mpls ldp parameter 
## error packet ldp tcp record 

error packet ldp tcp record 
命令功能 : 
LDP错误报文记录TCP使能或去使能配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
error packet ldp tcp record 
  {disable 
|enable 
 [record-number 
 ＜number 
＞]}
命令参数解释 : 
参数|描述
---|---
disable|错误报文记录去使能标记
enable|错误报文记录使能标记（默认使能）
＜number＞|使能的错误报文记录数量，范围：10–200（默认值10）
缺省 : 
缺省情况下错误报文记录TCP使能，记录数为10。 
使用说明 : 
使用场景用来记录LDP TCP错误报文，默认此功能打开，可通过error packet ldp tcp record disable  关闭该功能
范例 : 
配置TCP记录数为100：ZXROSNG(config)# error packet ldp tcp record enable record-number 100去使能错误报文记录TCP：ZXROSNG(config)# error packet ldp tcp record disable去错误报文记录TCP配置，恢复默认值：ZXROSNG(config)# error packet ldp tcp record enable
相关命令 : 
show error packet ldp statistics 
## error packet ldp udp record 

error packet ldp udp record 
命令功能 : 
LDP错误报文记录UDP使能或去使能配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
error packet ldp udp record 
  {disable 
|enable 
 [record-number 
 ＜number 
＞]}
命令参数解释 : 
参数|描述
---|---
disable|错误报文记录去使能标记
enable|错误报文记录使能标记
＜number＞|使能的错误报文记录数量，范围：10–200（默认值10）
缺省 : 
缺省情况下错误报文记录UDP使能，记录数为10。 
使用说明 : 
使用场景用来记录LDP UDP错误报文，默认此功能打开，可通过error packet ldp udp record disable  关闭该功能
范例 : 
配置UDP记录数为100：ZXROSNG(config)# error packet ldp udp record enable record-number 100去使能错误报文记录UDP：ZXROSNG(config)# error packet ldp udp record disable去错误报文记录UDP配置，恢复默认值：ZXROSNG(config)# error packet ldp udp record enable
相关命令 : 
show error packet ldp statistics 
## explicit-null ipv6 

explicit-null ipv6 
命令功能 : 
使LDP实例在本该通告隐式空标签的时候通告显式空标签。默认情况使用的是隐式空标签。使用no命令恢复默认情况。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
explicit-null ipv6 
  [for 
 ＜acl-name 
＞] [to 
 ＜acl-name 
＞]
no explicit-null ipv6 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|指定用显式空标签通告代替隐式标签通告的前缀，长度1–31个字符
＜acl-name＞|指定用显式空标签通告代替隐式标签通告的前缀，长度1–31个字符
缺省 : 
缺省情况下，LDP实例总是向所有邻居以隐式空标签通告ipv6直连网段。 
使用说明 : 
使用场景1、缺省情况下总是向所有邻居通告ipv6直连网段的标签是隐式空标签，隐式空标签引起倒数第二跳路由器作倒数第二跳弹出，但有时需要禁止倒数第二跳路由器作倒数第二跳弹出，而要求其用显式空标签作出标签转发包。2、explicit-null ipv6命令使得路由器向<peer-acl>允许的邻居对<prefix-acl>允许的ipv6直连网段通告显式空标签。3、如果命令中没有带<prefix-acl>参数，则所有ipv6直连网段都以显式空标签通告。4、如果命令中没有带<peer-acl>参数，则向所有邻居通告ipv6直连网段显式空标签。注意事项本命令仅对命令配置以后的标签通告消息生效，如果策略匹配的网段和邻居在策略配置之前已经通告过标签，则不会发生改变，除非会话中断重建。因此建议不要在运行中配置该命令，以免发生不一致的情形。
范例 : 
配置LDP实例向所有的邻居以显式空标签通告所有ipv6直连路由：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#explicit-null ipv6对直连网段33::/64以显式空标签通告，其它直连网段以隐式空标签通告：ZXROSNG(config)# ipv6-access-list 33ZXROSNG(config-ipv6-acl)# rule 1 permit ipv6 33::/64 anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#explicit-null ipv6 for 33对直连网段33::/64以显式空标签并仅对peer 6.6.6.1/32邻居通告，其它直连网段以隐式空标签通告：ZXROSNG(config)# ipv4-access-list peerZXROSNG(config-ipv4-acl)#rule 1 permit 6.6.6.1ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#explicit-null ipv6 for 33 to peer删除配置：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#no explicit-null ipv6
相关命令 : 
show mpls ldp bindings 
## explicit-null 

explicit-null 
命令功能 : 
使LDP实例在本该通告隐式空标签的时候通告显式空标签。默认情况使用的是隐式空标签。使用no命令恢复默认情况。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
explicit-null 
  [for 
 ＜acl-name 
＞] [to 
 ＜acl-name 
＞]
no explicit-null 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|指定用显式空标签通告代替隐式标签通告的前缀
＜acl-name＞|指定用显式空标签通告代替隐式标签通告的前缀
缺省 : 
缺省情况下，LDP实例总是向所有邻居以隐式空标签通告直连网段。 
使用说明 : 
使用场景1、缺省情况下总是向所有邻居通告直连网段的标签是隐式空标签，隐式空标签引起倒数第二跳路由器作倒数第二跳弹出，但有时需要禁止倒数第二跳路由器作倒数第二跳弹出，而要求其用显式空标签作出标签转发包。2、explicit-null命令使得路由器向<peer-acl>允许的邻居对<prefix-acl>允许的直连网段通告显式空标签。3、如果命令中没有带<prefix-acl>参数，则所有直连网段都以显式空标签通告。4、如果命令中没有带<peer-acl>参数，则向所有邻居通告显式空标签。注意事项本命令仅对命令配置以后的标签通告消息生效，如果策略匹配的网段和邻居在策略配置之前已经通告过标签，则不会发生改变，除非会话中断重建。因此建议不要在运行中配置该命令，以免发生不一致的情形。
范例 : 
配置LDP实例向所有的邻居以显式空标签通告所有直连路由：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#explicit-null对直连网段137.5.0.0以显式空标签通告，其它直连网段以隐式空标签通告：ZXROSNG(config)#ipv4-access-list 10ZXROSNG(config-ipv4-acl)#permit 137.5.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#explicit-null for 10删除配置：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#no explicit-null
相关命令 : 
show mpls ldp bindings  
## filter 

filter 
命令功能 : 
配置报文过滤策略，使用no命令删除该功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
filter 
 packet 
 for 
 ＜acl-name 
＞
no filter 
 packet 
 for 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|acl名称，名称支持的最大长度为31个字符
缺省 : 
无 
使用说明 : 
使用场景过滤指定规则的报文数据。
范例 : 
过滤ACL名为5的报文数据：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# filter packet for 5
相关命令 : 
无 
## forbidden-label-range 

forbidden-label-range 
命令功能 : 
用于配置禁用标签范围。标签管理模块处于共享模式时（本产品为$#117571622:0/非共享模式;1/共享模式#$），可通过该命令设置全局标签范围内某段标签范围的禁用与取消。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
forbidden-label-range 
  ＜label-min 
＞ ＜label-max 
＞
no forbidden-label-range 
  ＜label-min 
＞ ＜label-max 
＞
				
命令参数解释 : 
参数|描述
---|---
＜label-min＞|用于配置禁用标签范围最小值。 取值范围：标签范围大小16-1048575。 默认值：0。
＜label-max＞|用于配置禁用标签范围最大值。 取值范围：标签范围大小16-1048575。 默认值：0。
缺省 : 
平台缺省情况下无禁用段范围。 
使用说明 : 
 本命令可以设置某段范围为禁用范围，该标签范围不可超过全局标签值范围（$#117571585#$ - $#117571586#$），这个范围内标签不可被业务申请。    可以配置多个禁用段范围，可以配置的最大禁用段范围个数为$#117571657#$。    使用no命令删除禁用段标签范围。
范例 : 
配置禁用标签范围，最小值为100，最大值为200，则输入以下命令：ZXROSNG(config-lm)#forbidden-label-range 100 200删除配置的禁用标签范围：ZXROSNG(config-lm)#no forbidden-label-range 100 200
相关命令 : 
show mpls label manage 
## graceful-restart timer 

graceful-restart timer 
命令功能 : 
通过配置该命令使路由器支持LDP 的Graceful Restart功能，它使路由器在协议控制层面发生重启/中断过程中，能够继续保持原有的转发信息，并在neighbor-liveness时间内重启成功后能根据底层转发信息进行上层信息的恢复。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
graceful-restart timer 
  {max-recovery 
 ＜max-recovery-time 
＞|neighbor-liveness 
 ＜neighbor-Liveness-time 
＞}
no graceful-restart timer 
  {max-recovery 
|neighbor-liveness 
}
				
命令参数解释 : 
参数|描述
---|---
＜max-recovery-time＞|LSR等待对端邻居进行标记恢复的最长时间（单位：秒），缺省值为120，该参数需要协商，参数范围15-3600。
＜neighbor-Liveness-time＞|LSR等待LDP session会话恢复的最长时间（单位：秒），缺省值为120，该参数需要协商，参数范围5-3600。
缺省 : 
无 
使用说明 : 
使用场景该命令用来设置GR的会话重建定时器和恢复定时器时间，两个定时器时间默认都是120s。注意事项缺省情况下，LDP不支持GR功能，需要配置触发。但以上命令的生效均需要ldp的邻居重建或者协议重启。因为相关参数将在初始化消息中进行协商。
范例 : 
配置使路由器支持LDP GR，并设置其neighbor-liveness为30（secs），max-recovery为40（secs）：router(config)#mpls ldp instance 1router(config-ldp-1)#graceful-restartrouter(config-ldp-1)#graceful-restart timer neighbor-liveness 30router(config-ldp-1)#graceful-restart timer max-recovery 40
相关命令 : 
show mpls ldp graceful-restartshow mpls ldp neighbor graceful-restart
## graceful-restart 

graceful-restart 
命令功能 : 
通过配置该命令使路由器支持LDP 的Graceful Restart功能，它使路由器在协议控制层面发生重启/中断过程中，能够继续保持原有的转发信息，并在neighbor-liveness时间内重启成功后能根据底层转发信息进行上层信息的恢复。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
graceful-restart 
 
no graceful-restart 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景通过配置该命令使路由器支持LDP 的Graceful Restart功能，它使路由器在协议控制层面发生重启/中断过程中，能够继续保持原有的转发信息。注意事项缺省情况下，LDP不支持GR功能，需要配置触发。但以上命令的生效均需要ldp的邻居重建或者协议重启。因为相关参数将在初始化消息中进行协商。
范例 : 
配置使路由器支持LDP GR，并设置其neighbor-liveness为30（secs），max-recovery为40（secs）：router(config)#mpls ldp instance 1router(config-ldp-1)#graceful-restartrouter(config-ldp-1)#graceful-restart timer neighbor-liveness 30router(config-ldp-1)#graceful-restart timer max-recovery 40
相关命令 : 
show mpls ldp graceful-restartshow mpls ldp neighbor graceful-restart
## gtsm 

gtsm 
命令功能 : 
使能LDP 直连会话GTSM功能 
命令模式 : 
 LDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
gtsm 
 
no gtsm 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景在LDP的接口配置模式下，使能GTSM功能。
范例 : 
LDP实例下使能接口smartgroup1，并配置gtsm：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface smartgroup1ZXROSNG(config-ldp-1-if-smartgroup1)#gtsmZXROSNG(config-ldp-1-if-smartgroup1)#
相关命令 : 
无 
## gtsm 

gtsm 
命令功能 : 
通过配置该命令使路由器启动检查对端发送来的LDP报文的ttl跳数，默认不使能该功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
gtsm 
 target-neighbor 
 ＜ip-address 
＞ hop-count 
 ＜hop-num 
＞
no gtsm 
 target-neighbor 
 ＜ip-address 
＞ hop-count 
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|对端LSR地址。
＜hop-num＞|TTL跳数
缺省 : 
无 
使用说明 : 
使用场景缺省情况下，LDP不支持GTSM功能，需要配置触发。配置后需要对接收的该邻居的报文进行TTL范围校验，TTL必须大于或等于255 – n+1。
范例 : 
配置使路由器支持LDP GTSM，并设置其neighbor 20.20.0.3 发送过来的跳数间隔为2：router(config)#mpls ldp instance 1router(config-ldp-1)# gtsm target-neighbor 20.20.0.3 hop-count 2
相关命令 : 
show mpls ldp neighbor 
## holdtime 

holdtime 
命令功能 : 
配置LDP会话在收不到后续LDP消息的情况下的保持时间，使用no命令恢复默认值。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
holdtime 
  ＜holdtime 
＞
no holdtime 
命令参数解释 : 
参数|描述
---|---
＜holdtime＞|指定会话在收不到后续ldp消息的情况下的保持时间，范围：15–65535，单位：秒
缺省 : 
缺省情况下，指定会话维持时间是180秒。 
使用说明 : 
使用场景当两个LSR建立会话时，协商维持时间为二者的配置参数的较小值。
范例 : 
配置保持时间是200秒：ZXROSNG(config)#mpls ldp  instance 1ZXROSNG(config-ldp-1)#holdtime 200查看配置结果信息：ZXROSNG(config-ldp-1)#show mpls ldp parameters instance 1Protocol version: 1Session holdtime: 200 sec; keep alive interval: 66 secDiscovery hello: holdtime: 15 sec; interval: 5 secDiscovery targeted hello: holdtime: 45 sec; interval: 15 secLDP for targeted sessionsDownstream on Demand max hop count: 255LDP initial/maximum backoff: 30/240 secLDP used lsp control mode: IndependentLDP configred lsp control mode: IndependentLDP used label retention mode: LiberalLDP configred label retention mode: LiberalLDP loop detection: off LDP IGP sync delay: 5 sec
相关命令 : 
show mpls ldp parameters 
## holdtime 

holdtime 
命令功能 : 
在LDP接口下配置LDP会话在收不到后续LDP消息的情况下的保持时间，使用no命令恢复默认值。 
命令模式 : 
 LDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
holdtime 
  ＜holdtime 
＞
no holdtime 
命令参数解释 : 
参数|描述
---|---
＜holdtime＞|指定会话在收不到后续LDP消息的情况下的保持时间，范围：15–65535，单位：秒
缺省 : 
无 
使用说明 : 
使用场景当两个LSR建立会话时，协商维持时间为二者接收到的第一个hello消息中携带的保持时间的较小者。注意事项发送hello消息中携带的保持时间选择规则是，优先选择接口下配置的保持时间，如果接口下不存在此配置，则选择LDP模式下配置的保持时间，如果LDP模式也不存在此配置，则选取LDP模式下保持时间配置的默认值。
范例 : 
配置保持时间是200秒：ZXROSNG(config)#mpls ldp  instance 1ZXROSNG(config-ldp-1)#interface gei-0/1/0/1ZXROSNG(config-ldp-1-if-gei-0/1/0/1)#holdtime 200删除配置：ZXROSNG(config-ldp-1-if-gei-0/1/0/1)#no holdtime
相关命令 : 
interfaceLDP模式 holdtime
## holdtime 

holdtime 
命令功能 : 
在LDP IPv6接口下配置LDP会话在收不到后续LDP消息的情况下的保持时间，使用no命令恢复默认值。 
命令模式 : 
 LDP-V6接口模式  
命令默认权限级别 : 
15 
命令格式 : 
holdtime 
  ＜holdtime 
＞
no holdtime 
命令参数解释 : 
参数|描述
---|---
＜holdtime＞|指定会话在收不到后续ldp消息的情况下的保持时间，范围：15–65535，单位：秒
缺省 : 
无 
使用说明 : 
使用场景当两个LSR建立会话时，协商维持时间为二者接收到的第一个hello消息中携带的保持时间的较小者。注意事项发送hello消息中携带的保持时间选择规则是，优先选择接口下配置的保持时间，如果接口下不存在此配置，则选择LDP模式下配置的保持时间，如果LDP模式也不存在此配置，则选取LDP模式下保持时间配置的默认值。
范例 : 
配置保持时间是200秒：ZXROSNG(config)#mpls ldp  instance 1ZXROSNG(config-ldp-1)#interface ipv6 gei-0/1/0/1ZXROSNG(config-ldp-1-ifv6-gei-0/1/0/1)#holdtime 200删除配置：ZXROSNG(config-ldp-1-ifv6-gei-0/1/0/1)#no holdtime
相关命令 : 
interface ipv6LDP模式 holdtime
## hostname 

hostname 
命令功能 : 
配置冗余组的主机名。使用no命令删除主机名。 
命令模式 : 
 冗余组模式  
命令默认权限级别 : 
15 
命令格式 : 
hostname 
  ＜rg-hostname 
＞
no hostname 
命令参数解释 : 
参数|描述
---|---
＜rg-hostname＞|冗余组本地主机名，最大长度为80字符
缺省 : 
无 
使用说明 : 
使用场景该命令用来配置冗余组的主机名称。
范例 : 
配置冗余组本地主机名：ZXROSNG(config)# redundancy interchassis group 1ZXROSNG(config-rg-1)#hostname abc查看配置结果信息：ZXROSNG(config-rg-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1  hostname: abc 
相关命令 : 
redundancy interchassisshow mpls ldp iccp
## igp sync delay 

igp sync delay 
命令功能 : 
设定LDP IGP同步延时定时器超时时间。
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
igp sync delay 
  ＜para 
＞ [force 
]
no igp sync delay 
命令参数解释 : 
参数|描述
---|---
＜para＞|指定延迟时间，单位秒
force|强制以延时定时器超时事件触发通知IGP同步流程结束
缺省 : 
缺省情况下，指定延迟时间为5秒
使用说明 : 
使用场景设定LDP IGP同步延时定时器超时时间，故障链路的LDP会话重新建立以后，LDP会启动延时定时器等待LSP的建立。注意事项1、延时定时器超时事件或者end-of-lib事件均会触发通知IGP同步流程结束，原则是哪个事件先发生哪个事件触发通知IGP同步流程结束。2、如果配置force可选项，即强制以延时定时器超时事件触发通知IGP同步流程结束，不响应end-of-lib事件。
范例 : 
LDP实例下设置igp同步延时时间为5s：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp)#igp sync delay 5强制以延时定时120秒触发igp同步结束：ZXROSNG(config-ldp)#igp sync delay 120 force
相关命令 : 
无 
## igp sync interface 

igp sync interface 
命令功能 : 
使能Target会话的接口的LDP IGP同步功能。当前支持te_tunnel类型接口的配置。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
igp sync interface 
  ＜interface-name 
＞
no igp sync interface 
  ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
缺省 : 
无 
使用说明 : 
使用场景当前支持te_tunnel类型接口的配置。
范例 : 
使能igp sync同步功能，并配置te_trnnel类型接口：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp)#igp sync interface te_tunnel1
相关命令 : 
show mpls ldp igp sync  
## interface ipv6 

interface ipv6 
命令功能 : 
使能该接口的LDP属性，并进入到LDP ipv6接口配置模式。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
interface ipv6 
  ＜interface-name 
＞
no interface ipv6 
  ＜interface-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
缺省 : 
无 
使用说明 : 
使用场景实例下使能ipv6接口，然后可以在接口下配置相关信息。
范例 : 
配置使能接口gei–0/1/0/1的LDP属性，并进入LDP接口配置模式：ZXROSNG(config-ldp-1)#interface ipv6 gei-0/1/0/5ZXROSNG(config-ldp-1-ifv6-gei-0/1/0/5)#查看配置结果信息：ZXROSNG(config-ldp-1)#show running-config ldp! <MPLS>mpls ldp instance 1  explicit-null for 2  router-id loopback1  interface gei-0/1/0/1  $  interface ipv6 gei-0/1/0/5! </MPLS>删除配置：ZXROSNG(config-ldp-1)#no interface ipv6 gei-0/1/0/5ZXROSNG(config-ldp-1)#show running-config ldp! <MPLS>mpls ldp instance 1  explicit-null for 2  router-id loopback1! </MPLS>
相关命令 : 
show running-config ldp 
interface : 

interface (LDP模式) 
命令功能 : 
使能该接口的LDP属性，并进入到LDP接口配置模式。 
命令模式 : 
 LDP模式  
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
使用场景实例下使能接口，然后进入到接口配置模式，能够配置接口相关信息。
范例 : 
配置使能接口gei–0/1/0/1的LDP属性，并进入LDP接口配置模式：ZXROSNG(config-ldp-1)#interface gei-0/1/0/1ZXROSNG(config-ldp-1-if-gei-0/1/0/1)#查看配置结果信息：ZXROSNG(config-ldp-1)#show running-config ldp! <MPLS>mpls ldp instance 1  explicit-null for 2  router-id loopback1  interface gei-0/1/0/1  $  interface ipv6 gei-0/1/0/5! </MPLS>删除配置：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#no interface gei-0/1/0/1ZXROSNG(config-ldp-1)#show running-config ldp! <MPLS>mpls ldp instance 1  explicit-null for 2  router-id loopback1! </MPLS>
相关命令 : 
show running-config ldp 
## kompella-range-size 

kompella-range-size 
命令功能 : 
该命令工作于标签管理模式下，用于配置Kompella标签范围大小。Kompella是指L2VPN中的一种信令方式，其标签分配特点是以一段连续标签作为基本分配单元。标签管理模块处于共享模式时（由产品规格确定），Kompella标签位于全局标签资源池的尾部，即明确标签范围大小，便可推断出Kompella标签范围。全局标签资源是指设备上可分配标签资源总范围，由产品规格确定。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
kompella-range-size 
  ＜label-range-size 
＞
no kompella-range-size 
命令参数解释 : 
参数|描述
---|---
＜label-range-size＞|用于配置Kompella标签范围大小。取值范围：标签范围大小0-65536。默认值：由产品规格确定。
缺省 : 
缺省情况下，标签范围取缺省值。 
使用说明 : 
    拥有管理员权限的操作员可以使用这条命令。    Kompella的标签范围坐落在全局标签范围尾部，这里只是配置了Kompella范围的大小。假设全局标签范围为16－1048575（全局范围由产品规格确定），如果kompella-range-size 1000，那Kompella协议的范围为1047576－1048575。    该标签范围不可超过全局标签值范围（由产品规格确定），若Kompella标签范围的锁定状态（由产品规格确定）取值为1时，表示其为锁定状态，该范围大小不可配置。    该标签范围不可与静态标签范围相重叠。Kompella标签范围大小、静态标签范围大小、静态标签预备范围大小、动态协议预留标签数量，四者之和不应超过全局标签范围大小。    最多可以配置1条。    使用no命令可以删除Kompella标签范围。
范例 : 
配置Kompella标签范围大小1000，则输入以下命令：ZXROSNG(config-lm)# kompella-range-size 1000
相关命令 : 
show mpls label managempls label manage
## label-advertise disable 

label-advertise disable 
命令功能 : 
使用本命令控制本地分配的标签（入标签）通过LDP分发，这条命令阻止分发本地分配的标签。使用no命令恢复默认情况。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-advertise disable 
 
no label-advertise disable 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下，向实例的所有邻居通告所有标签。 
使用说明 : 
使用场景label-advertise disable命令用来阻止分发任何本地分配的配置规则外的标签
范例 : 
配置LDP实例禁止向任何邻居通告任何标签：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-advertise disable
相关命令 : 
无 
## label-advertise ipv6 

label-advertise ipv6 
命令功能 : 
使用本命令控制本地ipv6前缀分配的标签（入标签）通过LDP分发，这条命令控制哪些目的ipv6网段的标签向哪些邻居通告。使用no命令恢复默认情况。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-advertise ipv6 
  {for 
 ＜for-acl-name 
＞ [to 
 ＜to-acl-name 
＞]}
no label-advertise ipv6 
  {for 
 ＜acl-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜for-acl-name＞|指定通告哪些ipv6目的网段的标签，长度1–31个字符
＜to-acl-name＞|指定向哪些邻居通告那些标签，LSR用其路由器ID标识，也就是LDP Id的前四字节，长度1–31个字符
缺省 : 
缺省情况下，向实例的所有邻居通告所有标签。 
使用说明 : 
使用场景执行for <prefix-access-list>[ to <peer-access-list>]规则来决定LSR如何通告本地标签，disable命令阻止分发任何本地分配的配置规则外的标签，配多条时按下面的规则处理：1. 没配置规则时，相应的access list对是(none,none)；每条for <prefix-access-list> to <peer-access-list> 有一个(prefix acl,peer acl)对， for命令（不带to关键字）相应的access list对是(prefix-acl,none)。2. 每个前缀可以有（也只能有）一个(prefix acl,peer acl)对“应用”于它，规则是：i. 一个(prefix acl,peer acl)对“应用”于一个前缀，仅当prefix acl与前缀“匹配”，匹配的条件是prefix acl允许（permit）该前缀。ii. 如果多于一个(prefix acl,peer acl)对“匹配”一个前缀，第一个(prefix acl,peer acl)对（按show running中的顺序）“应用”于一个前缀。3. 当LSR要通告一个前缀的标签时，LSR：i. 找出“应用”于前缀的(prefix acl,peer acl)对。ii. 没有“应用”于前缀的(prefix acl,peer acl)对时，如果配置了disable，该标签不通告给任何邻居；否则就通告给所有邻居。iii. 如果一个(prefix acl,peer acl)对“应用”于前缀，如果prefix acl拒绝(deny)前缀，则该标签不向任何邻居通告。iv. 如果prefix acl“permit”前缀，而没有peer acl（即none），则该标签通告给所有邻居。v. 如果prefix acl“permit”前缀，有一个peer acl，则该标签通告给所有peer acl “permit”的邻居。
范例 : 
配置LDP实例向任何邻居通告33::/128网段的标签：ZXROSNG(config)# ipv6-access-list 33ZXROSNG(config-ipv6-acl)# rule 1 permit ipv6 33::/64 anyZXROSNG(config-ipv6-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-advertise ipv6 for 33配置LDP实例只向LSR 6.6.6.1通告33::/64的标签， ZXROSNG(config)# ipv4-access-list peerZXROSNG(config-ipv4-acl)#rule 1 permit 6.6.6.1ZXROSNG(config-ipv4-acl)#exZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-advertise ipv6 for 33 to peer
相关命令 : 
show mpls ldp bindings 
## label-advertise old-style 

label-advertise old-style 
命令功能 : 
使用本命令控制本地分配的标签（入标签）通过LDP分发，这条命令按照cisco早期规则解释来处理access list，使用no命令恢复默认情况。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-advertise old-style 
 
no label-advertise old-style 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下，向实例的所有邻居通告所有标签。 
使用说明 : 
使用场景按照cisco早期规则解释来处理access list。
范例 : 
按照cisco早期规则解释来处理access list：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-advertise old-style 
相关命令 : 
无 
## label-advertise 

label-advertise 
命令功能 : 
使用本命令控制本地分配的标签（入标签）通过LDP分发，这条命令控制哪些目的网段的标签向哪些邻居通告。使用no命令恢复默认情况。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-advertise 
  {for 
 ＜for-acl-name 
＞ [to 
 ＜to-acl-name 
＞]}
no label-advertise 
  {for 
 ＜acl-name 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜for-acl-name＞|指定通告哪些目的网段的标签
＜to-acl-name＞|指定向哪些邻居通告那些标签，LSR用其路由器ID标识，也就是LDP Id的前四字节
缺省 : 
缺省情况下，向实例的所有邻居通告所有标签。 
使用说明 : 
使用场景执行for <prefix-access-list>[ to <peer-access-list>]规则来决定LSR如何通告本地标签，disable命令阻止分发任何本地分配的配置规则外的标签，配多条时按下面的规则处理：1. 没配置规则时，相应的access list对是(none,none)；每条for <prefix-access-list> to <peer-access-list> 有一个(prefix acl,peer acl)对， for命令（不带to关键字）相应的access list对是(prefix-acl,none)。2. 每个前缀可以有（也只能有）一个(prefix acl,peer acl)对“应用”于它，规则是：i. 一个(prefix acl,peer acl)对“应用”于一个前缀，仅当prefix acl与前缀“匹配”，匹配的条件是prefix acl允许（permit）该前缀。ii. 如果多于一个(prefix acl,peer acl)对“匹配”一个前缀，第一个(prefix acl,peer acl)对（按show running中的顺序）“应用”于一个前缀。3. 当LSR要通告一个前缀的标签时，LSR：i. 找出“应用”于前缀的(prefix acl,peer acl)对。ii. 没有“应用”于前缀的(prefix acl,peer acl)对时，如果配置了disable，该标签不通告给任何邻居；否则就通告给所有邻居。iii. 如果一个(prefix acl,peer acl)对“应用”于前缀，如果prefix acl拒绝(deny)前缀，则该标签不向任何邻居通告。iv. 如果prefix acl“permit”前缀，而没有peer acl（即none），则该标签通告给所有邻居。v. 如果prefix acl“permit”前缀，有一个peer acl，则该标签通告给所有peer acl “permit”的邻居。
范例 : 
配置LDP实例禁止向任何邻居通告任何标签：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-advertise disable配置LDP实例向任何邻居通告10.101.0.0和10.221.0.0网段的标签：ZXROSNG(config)#ipv4-access-list 10ZXROSNG(config-ipv4-acl)#rule 2 permit 10.101.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#rule 3 permit 10.221.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#rule 4 deny anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-advertise for 10ZXROSNG(config-ldp-1)#label-advertise disable配置LDP实例只向LSR 155.0.0.55通告59.0.0.0的标签，只向LSR 133.0.0.33通告35.0.0.0的标签；如果不允许向规则外的任何其它LSR通告规则外的任何其它网段标签，可加上disable配置：ZXROSNG(config)#ipv4-access-list 10ZXROSNG(config-ipv4-acl)#rule 8 permit 59.0.0.0 0.255.255.255ZXROSNG(config-ipv4-acl)#rule 9 deny anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ipv4-access-list 11ZXROSNG(config-ipv4-acl)#rule 11 permit 155.0.0.55 0.0.0.0ZXROSNG(config-ipv4-acl)#rule 12 deny anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ipv4-access-list 20ZXROSNG(config-ipv4-acl)#rule 13 permit 35.0.0.0 0.255.255.255ZXROSNG(config-ipv4-acl)#rule 14 deny anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#ipv4-access-list 21ZXROSNG(config-ipv4-acl)#rule 20 permit 133.0.0.33 0.0.0.0ZXROSNG(config-ipv4-acl)#rule 21 deny anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-advertise for 10 to 11ZXROSNG(config-ldp-1)#label-advertise for 20 to 21ZXROSNG(config-ldp-1)#label-advertise disable
相关命令 : 
show mpls ldp bindings 
## label-distribution 

label-distribution 
命令功能 : 
LDP接口配置模式下控制LDP接口使能下游按需标签分发。使用no命令禁止这一特性。 
命令模式 : 
 LDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
label-distribution 
 dod 
no label-distribution 
 dod 
命令参数解释 : 
参数|描述
---|---
dod|下游按需标签分发模式下游按需标签分发模式
缺省 : 
缺省情况下，LDP接口为下游自主标签分发。 
使用说明 : 
使用场景该命令触发使能下游按需标签分发，需要重置LDP实例才能生效
范例 : 
接口使能下游按需标签分发：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface gei-0/3/1/8ZXROSNG(config-ldp-if-gei-0/3/1/8)#label-distribution dod
相关命令 : 
show mpls ldp interfacereset mpls ldp instance
## label-distribution 

label-distribution 
命令功能 : 
控制LDP接口使能下游按需标签分发。使用no命令禁止这一特性。 
命令模式 : 
 LDP-V6接口模式  
命令默认权限级别 : 
15 
命令格式 : 
label-distribution 
 dod 
no label-distribution 
 dod 
命令参数解释 : 
参数|描述
---|---
dod|下游按需标签分发
缺省 : 
缺省情况下，LDP接口为下游自主标签分发。 
使用说明 : 
使用场景该命令触发使能下游按需标签分发，需要重置LDP实例才能生效
范例 : 
ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface ipv6 gei-0/3/1/8ZXROSNG(config-ldp-1-ifv6-gei-0/3/1/8)#label-distribution dod
相关命令 : 
show mpls ldp interfacereset mpls ldp instance
## label-request ipv6 

label-request ipv6 
命令功能 : 
配置LDP实例需要发送request消息的IPv6前缀和下游邻居，使用no命令禁止该特性。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-request ipv6 
 for 
 ＜acl-name 
＞
no label-request ipv6 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|需要发送request消息的IPv6前缀访问列表, 长度1–31个字符
缺省 : 
缺省情况下，不发送request消息。 
使用说明 : 
使用场景本命令可以指定针对某些IPv6前缀发送标签请求消息，如果配置了<prefix-access-list>参数，则对该列表permit的前缀，LDP实例将向其下游发送标签请求消息。注意事项本命令仅对配置以后创建的FEC或在配置以后发现其下游LSR的FEC生效, 并以返回码方式提示.因此建议不要在运行（即会话UP时）中配置该命令，以免发生不一致的情形。重启会话，按照当前的配置重新生效。
范例 : 
配置对33::/64网段的FEC发送标签请求消息：ZXROSNG(config)# ipv6-access-list 33ZXROSNG(config-ipv6-acl)# rule 1 permit ipv6 33::/64 anyZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# label-request ipv6 for 33
相关命令 : 
无 
## label-request 

label-request 
命令功能 : 
配置LDP实例需要发送request消息的前缀和下游邻居，使用no命令禁止该特性。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-request 
 for 
 ＜acl-name 
＞
no label-request 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|需要发送request消息的前缀访问列表
缺省 : 
缺省情况下，LDP实例针对本VPN域中的所有目的网段如果没有下游标签，则发送标签request。 
使用说明 : 
使用场景通过该命令可对不必发送标签请求的网段进行过滤，或者网络管理者可能希望是否向下游发送标签请求置于控制之中,即只为得到许可的网段发送request，本命令即提供了这样的手段。注意事项本命令仅对配置以后创建的FEC或在配置以后发现其下游LSR的FEC生效。因此建议不要在运行中配置该命令，以免发生不一致的情形。
范例 : 
配置对10.1.1.0/16网段的FEC发送标签请求消息：ZXROSNG(config)#ipv4-access-list 10ZXROSNG(config-ipv4-acl)#rule 1 permit 10.1.1.0 0.0.255.255ZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-request for 10
相关命令 : 
无 
## label-reservation 

label-reservation 
命令功能 : 
该命令工作于标签管理模式下，用于配置各个动态协议的预留标签数量。标签管理模块处于共享模式时（由产品规格确定），可以为各个动态协议预留一定数量的标签资源，保证其至少能得到该数量的标签。各个动态协议的基本含义如下：    LDP：标记分发协议，是一个动态分发标签的协议，采用TCP报文在设备之间传递标签信息。    PWE3：是一种L2VPN协议，在分组交换网上提供隧道以便仿真一些二层业务。    RSVP：是一种基于IP协议的资源预留协议。    BGP：即边界网关协议，是一种自治系统之间的无环路域间路由协议。    BGPv6：一种支持IPv6的BGP协议。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
label-reservation 
  {[ldp 
 ＜ldp-label-range-size 
＞],[pwe3 
 ＜pwe3-label-range-size 
＞],[rsvp 
 ＜rsvp-label-range-size 
＞],[bgp 
 ＜bgp-label-range-size 
＞],[bgpv6 
 ＜bgpv6-label-range-size 
＞]}
no label-reservation 
命令参数解释 : 
参数|描述
---|---
＜ldp-label-range-size＞|用于配置LDP预留标签数量。取值范围：标签数量0-1048560。默认值：由产品规格确定。
＜pwe3-label-range-size＞|用于配置PWE3预留标签数量。取值范围：标签数量0-1048560。默认值：由产品规格确定。
＜rsvp-label-range-size＞|用于配置RSVP预留标签数量。取值范围：标签数量0-1048560。默认值：由产品规格确定。
＜bgp-label-range-size＞|用于配置BGP预留标签数量。取值范围：标签数量0-1048560。默认值：由产品规格确定。
＜bgpv6-label-range-size＞|用于配置BGPV6预留标签数量。取值范围：标签数量0-1048560。默认值：由产品规格确定。
缺省 : 
缺省情况下，各标签范围使用产规格中的默认值。 
使用说明 : 
    有拥有管理员权限的操作员可以使用这条命令。    若对应动态协议标签范围的锁定状态（由产品规格确定）取值为1时，表示其为锁定状态，则对应协议的预留数量不可配置。    Kompella标签范围大小、静态标签范围大小、静态标签预备范围大小、动态协议预留标签数量，四者之和不应超过全局标签范围大小。    ldp、pwe3等等参数取值也可以由兼容加载旧配置中mpls label range  global ＜global-min-value＞ ＜global-max-value＞ static ＜static-min-value＞ ＜static-max-value＞ ldp ＜ldp-min-value＞ ＜ldp-max-value＞ pwe3 ＜pwe3-min-value＞ ＜pwe3-max-value＞ rsvp ＜rsvp-min-value＞ ＜rsvp-max-value＞ bgp ＜bgp-min-value＞ ＜bgp-max-value＞ bgpv6 ＜bgpv6-min-value＞ ＜bgpv6-max-value＞[kompella ＜kompella-min-value＞ ＜kompella-max-value＞]而得到，其为原来范围标签个数。    最多可以配置1条。    使用no命令删除各个动态协议的预留标签数量。
范例 : 
配置LDP、PWE3的预留标签数量，LDP预留100个标签，PWE3预留200个标签，则输入以下命令：ZXROSNG(config-lm)# label-reservation ldp 100 pwe3 200
相关命令 : 
show mpls label managempls label manage
## label-retention 

label-retention 
命令功能 : 
控制LDP实例使能保守的标签保持模式。使用no命令禁止这一特性。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-retention 
 conservative 
no label-retention 
 conservative 
命令参数解释 : 
参数|描述
---|---
conservative|保守的标签保持模式
缺省 : 
缺省情况下，LDP实例为自由的标签保持模式。 
使用说明 : 
使用场景该命令触发使能保守的标签保持模式需要重置LDP实例才能生效
范例 : 
配置使能保守的标签保持模式：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-retention conservative
相关命令 : 
show mpls ldp interfacereset mpls ldp instance
## label-withdraw-delay timer 

label-withdraw-delay timer 
命令功能 : 
配置标签撤销延迟发送功能的延迟时间。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-withdraw-delay timer 
  ＜time 
＞
no label-withdraw-delay timer 
命令参数解释 : 
参数|描述
---|---
＜time＞|可配置的延迟时间，范围1-65535，单位s
缺省 : 
默认延迟时间是5s 
使用说明 : 
使用场景需要按照配置的延迟时间来延迟发送标签撤销消息，首先要使能标签撤销消息延迟发送功能，再配置具体的延迟时间才能生效。
范例 : 
配置标签撤销消息延迟时间为120sZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-withdraw-delay timer 120去配置延迟时间ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#no label-withdraw-delay timer
相关命令 : 
label-withdraw-delayshow mpls ldp bindings
## label-withdraw-delay 

label-withdraw-delay 
命令功能 : 
通过配置该命令使能标签撤销消息延迟发送功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
label-withdraw-delay 
 
no label-withdraw-delay 
命令参数解释 : 
					无
				 
缺省 : 
缺省情况下，除了路由删除需等待320s发送标签撤销消息的情况，其他均立即发送标签撤销消息。 
使用说明 : 
使用场景使能了标签撤销消息延迟发送功能后，均按照配置的延迟时间来延迟发送标签撤销消息。
范例 : 
使能标签撤销消息延迟发送功能ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#label-withdraw-delay去使能标签撤销消息延迟发送功能ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#no label-withdraw-delay
相关命令 : 
label-withdraw-delay timershow mpls ldp bindings
## ldp-debug-policy hello interface 

ldp-debug-policy hello interface 
命令功能 : 
直连hello相关debug进行策略控制功能。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
ldp-debug-policy hello interface 
  ＜interface-name 
＞ instance 
 ＜instance-id 
＞
no ldp-debug-policy hello interface 
  ＜interface-name 
＞ instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
＜instance-id＞|LDP实例号
缺省 : 
默认状态hello相关debug显示所有直连及目标hello的信息。 
使用说明 : 
使用场景配置该命令后，符合配置的接口直连hello报文信息会在特权模式下debug总开关打开后打印，不符合的所有hello（包括目标hello）会被过滤掉。注意事项该命令在一个实例下可以配置8条过滤策略。
范例 : 
只打印实例1下来自接口gei-0/1/0/1的直连Hello消息：ZXROSNG#ldp-debug-policy hello interface gei-0/1/0/1 instance 1开始打印：ZXROSNG#terminal monitor删除配置：ZXROSNG# no ldp-debug-policy hello interface gei-0/1/0/1 instance 1停止打印：ZXROSNG#no terminal monitor
相关命令 : 
debug ldp transport events  instance <instance-id>debug ldp session io  instance <instance-id>debug-policy target-hello  <A.B.C.D>debug-policy target-hello ipv6  <ipv6-address>
## ldp-debug-policy session 

ldp-debug-policy session 
命令功能 : 
对应会话相关debug进行策略控制功能。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
ldp-debug-policy session 
 remote-routeid 
 ＜A.B.C.D 
＞ [labelspace 
 ＜labelspace 
＞] instance 
 ＜instance-id 
＞
no ldp-debug-policy session 
 remote-routeid 
 ＜A.B.C.D 
＞ instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜A.B.C.D＞|对端routerid
＜labelspace＞|LDP会话对端标签空间，范围0-65535
＜instance-id＞|ldp实例号
缺省 : 
默认状态会话相关debug显示所有会话报文信息。标签空间不配置的情况下默认对端标签空间值为0。
使用说明 : 
使用场景该命令一个实例下可以配置8条过滤策略，配置一条过滤策略后，符合配置的对端routeid的会话的报文信息会在debug开关打开后打印，不符合的会被过滤掉。
范例 : 
打印实例1下，对端router-id为2.3.4.71的会话相关信息：ZXROSNG#ldp- debug-policy session remote-routeid 2.3.4.71 instance 1 开始打印：ZXROSNG#terminal monitor删除配置：ZXROSNG# no ldp-debug-policy session remote-routeid 2.3.4.71 instance 1关闭打印：ZXROSNG#no terminal monitor
相关命令 : 
debug ldp messages received  instance <instance-id>debug ldp messages sent  instance <instance-id>debug ldp session io  instance <instance-id>debug ldp session state-machine  instance <instance-id>debug ldp bindings  instance <instance-id>debug ldp advertisements  instance <instance-id>debug ldp graceful-restart  instance <instance-id>
## ldp-debug-policy target-hello ipv6 

ldp-debug-policy target-hello ipv6 
命令功能 : 
IPv6类型目标hello相关debug进行策略控制功能。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
ldp-debug-policy target-hello ipv6 
  ＜ipv6-address 
＞ instance 
 ＜instance-id 
＞
no ldp-debug-policy target-hello ipv6 
  ＜ipv6-address 
＞ instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|远端邻居的IP地址，IPv6的地址
＜instance-id＞|LDP实例号
缺省 : 
默认状态hello相关debug显示所有直连及目标hello的信息。 
使用说明 : 
使用场景该配置命令用来在特权模式下当debug总开关打开后打印符合配置的目标hello报文信息，不符合的所有hello（包括直连hello）会被过滤掉。注意事项该配置命令以及IPv4的目标hello的过滤配置命令在一个实例下最多可以配置8条过滤策略。
范例 : 
仅打印实例1下，对端ipv6地址为20::1的目标Hello消息：ZXROSNG#ldp- debug-policy target-hello ipv6 20::1 instance 1开始打印：ZXROSNG#terminal monitor删除配置：ZXROSNG# no ldp-debug-policy target-hello ipv6 20::1 instance 停止打印：ZXROSNG#no terminal monitor
相关命令 : 
debug ldp transport events  instance <instance-id>debug ldp session io  instance <instance-id>debug-policy hello interface  <interface-name>debug-policy target-hello ipv6  <ipv6-address>
## ldp-debug-policy target-hello 

ldp-debug-policy target-hello 
命令功能 : 
IPv4类型目标hello相关debug进行策略控制功能。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
ldp-debug-policy target-hello 
  ＜A.B.C.D 
＞ instance 
 ＜instance-id 
＞
no ldp-debug-policy target-hello 
  ＜A.B.C.D 
＞ instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜A.B.C.D＞|对端routerid
＜instance-id＞|LDP实例号
缺省 : 
默认状态hello相关debug显示所有直连及目标hello的信息。 
使用说明 : 
使用场景该配置命令用来在特权模式下当debug总开关打开后打印符合配置的目标hello报文信息，不符合的所有hello（包括直连hello）会被过滤掉。注意事项该配置命令以及IPv6的目标hello的过滤配置命令一个实例下最多可以配置8条过滤策略。
范例 : 
仅打印实例1下，对端router-id为1.2.3.4的target-hello消息：ZXROSNG# ldp-debug-policy target-hello 1.2.3.4 instance 1开始打印：ZXROSNG#terminal monitor删除配置：ZXROSNG# no ldp-debug-policy target-hello 1.2.3.4 instance 1关闭打印：ZXROSNG#no terminal monitor
相关命令 : 
debug ldp transport events  instance <instance-id>debug ldp session io  instance <instance-id>debug-policy hello interface  <interface-name>debug-policy target-hello  <A.B.C.D>
## ldp-debug-policy transport connections peertransaddr 

ldp-debug-policy transport connections peertransaddr 
命令功能 : 
对应TCP链接相关debug进行策略控制功能。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
ldp-debug-policy transport connections peertransaddr 
  {ipv4 
 ＜ipv4-address 
＞ instance 
 ＜instance-id 
＞|ipv6 
 ＜ipv6-address 
＞ instance 
 ＜instance-id 
＞}
no ldp-debug-policy transport connections peertransaddr 
  {ipv4 
 ＜ipv4-address 
＞ instance 
 ＜instance-id 
＞|ipv6 
 ＜ipv6-address 
＞ instance 
 ＜instance-id 
＞}
				
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|对端ipv4传输层地址
＜instance-id＞|LDP实例号
＜ipv6-address＞|对端ipv6传输层地址
＜instance-id＞|LDP实例号
缺省 : 
默认状态显示所有TCP连接有关的信息。 
使用说明 : 
使用场景配置该命令后，符合配置的对端传输层地址相关的TCP链接信息会在特权模式下debug总开关打开后打印，不符合的TCP链接信息会被过滤掉。注意事项该配置命令在一个实例下最多可以配置8条过滤策略。
范例 : 
仅打印实例1下，对端传输层地址为1.2.3.4和1::2的TCP链接信息：ZXROSNG#ldp-debug-policy transport connections peertransaddr ipv4 1.2.3.4 instance 1ZXROSNG# ldp-debug-policy transport connections peertransaddr ipv6 1::2 instance 1删除配置：ZXROSNG# no ldp-debug-policy transport connections peertransaddr ipv4 1.2.3.4 instance 1ZXROSNG# no ldp-debug-policy transport connections peertransaddr ipv6 1::2 instance 1
相关命令 : 
debug ldp transport connections instance  <instance-id> 
## ldp-over-te 

ldp-over-te 
命令功能 : 
LDP实例下打开或关闭LDP over TE标签下发功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
ldp-over-te 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开LDP over TE标签下发功能
disable|关闭LDP over TE标签下发功能
缺省 : 
该功能默认 
使用说明 : 
使用场景在路由是over TE的情况下，标签不走LDP over TE，如果设备对标签栈的深度有要求，可以通过配置命令ldp-over-te disable直接关闭LDP over TE类型标签的下发，这样标签直接走单层TE。默认行为可以通过show mpls ldp parameter命令查看。
范例 : 
进入LDP实例1：ZXROSNG(config)#mpls ldp instance 1关闭LDP over TE的标签下发：ZXROSNG(config-ldp-1)# ldp-over-te disable打开LDP over TE的标签下发：ZXROSNG(config-ldp-1)# ldp-over-te enable
相关命令 : 
show mpls ldp parameter 
## longest-match 

longest-match 
命令功能 : 
配置最长匹配LSP的建立拆除等功能，禁止该特性使用本命令的no格式。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
longest-match 
  {ipv4 
 for 
 ＜acl-name 
＞|ipv6 
 for 
 ＜acl-name 
＞}
no longest-match 
  {ipv4 
|ipv6 
}
				
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|acl名称，名称支持的最大长度为31个字符
＜acl-name＞|acl名称，名称支持的最大长度为31个字符
缺省 : 
无 
使用说明 : 
使用场景只有满足条件的FEC才会进行跨域最长匹配请求，反之，如果条件不满足则不会进行请求，对于已经发送过请求的情况，会发送跨域最长匹配删除请求。
范例 : 
设置ACL名为route1的ipv4和ipv6最长匹配LSP：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# longest-match ipv4 for route1ZXROSNG(config-ldp-1)# longest-match ipv6 for route1
相关命令 : 
无 
## lsp-control 

lsp-control 
命令功能 : 
控制LDP实例使能有序的LSP控制模式。使用no命令禁止这一特性。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
lsp-control 
  {ordered 
|independent 
}
no lsp-control 
命令参数解释 : 
参数|描述
---|---
ordered|有序的LSP控制模式
independent|独立的LSP控制模式
缺省 : 
由产品性能参数控制LPS控制模式，从平台角度默认是独立的LSP控制模式，是兼容的$#100728848: 0/independent模式;1/order模式#$
使用说明 : 
使用场景该命令触发改变LSP控制模式需要重置LDP实例才能生效，no命令恢复缺省值。
范例 : 
配置使能有序的LSP控制模式：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#lsp-control ordered配置使能独立的LSP控制模式：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#lsp-control independent  
相关命令 : 
show mpls ldp neighborreset mpls ldp instance
## lsp-dod-request ipv6 

lsp-dod-request ipv6 
命令功能 : 
配置LDP支持触发发送标签请求消息，通过配置明细，对指定的IPv6地址前缀向下游发送标签请求消息。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
lsp-dod-request ipv6 
  ＜ipv6-address 
＞ ＜mask-length 
＞
no lsp-dod-request ipv6 
  ＜ipv6-address 
＞ ＜mask-length 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|发起主动DoD请求的前缀地址
＜mask-length＞|发起主动DoD请求的前缀地址掩码长度，范围0-128
缺省 : 
默认不支持 
使用说明 : 
使用场景在无缝MPLS等场景，接入侧边缘低端设备部署LDP时，为了避免资源浪费和性能不同等问题，可部署LDP DoD实现标签按需请求。而在通常的组网中，为了减少接入层设备的路由动荡，避免接入设备学习或者其他设备发布大量的路由，通常会采用静态/动态Default路由，这种情况下可以通过配置本命令触发向下游请求并建立LSP。前提要求配置本命令前，需要配置label-distribution dod以建立与下游的DoD会话，跨域场景需要配置最长匹配命令longest-match。注意事项默认配置时，DoD模式下，LDP依据FEC向下游发送标签请求消息。配置该命令后，可以不依据是否有FEC，而自主触发向下游发送标签请求消息。
范例 : 
配置对10::1/128网段的FEC发送标签请求消息：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# lsp-dod-request ipv6 10::1 128
相关命令 : 
label-distribution dodlongest-match
## lsp-dod-request queue 

lsp-dod-request queue 
命令功能 : 
配置LDP支持使能标签请求队列保持功能，no命令去使能该功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
lsp-dod-request queue 
 
no lsp-dod-request queue 
命令参数解释 : 
					无
				 
缺省 : 
默认不支持 
使用说明 : 
使用场景配置该命令后，支持标签请求队列保持功能，发送标签请求消息中携带RF7032中描述的Queue Request TLV。接收到标签请求消息时，如果携带此TLV，则本地无路由时，不返回NO ROUTE通知，而保存请求，待路由生成时立即向上游发送标签通告消息，加速DoD场景下的收敛。
范例 : 
配置请求队列保持功能：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# lsp-dod-request queue
相关命令 : 
无 
## lsp-dod-request 

lsp-dod-request 
命令功能 : 
配置LDP支持触发发送标签请求消息，通过配置明细，对指定的IPv4地址前缀向下游发送标签请求消息。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
lsp-dod-request 
  ＜ip-address 
＞ ＜mask-length 
＞
no lsp-dod-request 
  ＜ip-address 
＞ ＜mask-length 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|发起主动DoD请求的前缀地址
＜mask-length＞|发起主动DoD请求的前缀地址掩码长度，范围0-32
缺省 : 
默认不支持 
使用说明 : 
使用场景在无缝MPLS等场景，接入侧边缘低端设备部署LDP时，为了避免资源浪费和性能不同等问题，可部署LDP DoD实现标签按需请求。而在通常的组网中，为了减少接入层设备的路由动荡，避免接入设备学习或者其他设备发布大量的路由，通常会采用静态/动态Default路由，这种情况下可以通过配置本命令触发向下游请求并建立LSP。前提要求配置本命令前，需要配置label-distribution dod以建立与下游的DoD会话，跨域场景需要配置最长匹配命令longest-match。注意事项默认配置时，DoD模式下，LDP依据FEC向下游发送标签请求消息。配置该命令后，可以不依据是否有FEC，而自主触发向下游发送标签请求消息。
范例 : 
配置对1.2.3.4/32网段的FEC发送标签请求消息：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# lsp-dod-request 1.2.3.4 32
相关命令 : 
label-distribution dodlongest-match 
## lsp-policy 

lsp-policy 
命令功能 : 
通过本命令配置LSP下发策略，控制LDP只会下发有入标签且有出标签的LSP。使用no命令恢复默认情况。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
lsp-policy 
  {transit-only 
}
no lsp-policy 
命令参数解释 : 
参数|描述
---|---
transit-only|使能LDP只会下发有入标签且有出标签的LSP功能
缺省 : 
没具体策略，默认都下发 
使用说明 : 
使用场景配置该命令后，LDP只会下发有入标签且有出标签的LSP，有入标签无出标签或无入标签有出标签的LSP均不下发。
范例 : 
配置使能LDP只会下发有入标签且有出标签的LSP功能：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# lsp-policy transit-onlyno命令去使能下发策略：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#no lsp-policy
相关命令 : 
无 
## mldp 

mldp 
命令功能 : 
使能MLDP性能，进入MLDP配置模式。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
mldp 
 
no mldp 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景本命令使能MLDP，并且进入MLDP配置模式，该命令是进行MLDP各项配置的前提。使用no命令禁止MLDP，删除存在的各项MLDP配置
范例 : 
路由器上使能MLDP：ZXROSNG(config)# mpls ldp instance 1ZXROSNG(config-ldp-1)#mldpZXROSNG(config-ldp-1-mldp)#
相关命令 : 
show running-config 
## mpls label manage 

mpls label manage 
命令功能 : 
该命令工作于全局配置模式下，用于进入标签管理模式。标签管理模块处于共享模式时（由产品规格确定），可进入标签管理模式进行共享模式下的相关命令配置。
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls label manage 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
    拥有管理员权限的操作员可以使用这条命令。    最多可以配置1条。
范例 : 
进入标签管理配置模式，则输入以下命令：ZXROSNG(config)#mpls label  manage
相关命令 : 
show mpls label manage 
## mpls ldp 

mpls ldp 
命令功能 : 
使能LDP沿着普通的逐跳路由路径建立LSP，并进入LDP配置模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls ldp 
 instance 
 ＜instance-id 
＞ [vrf 
 ＜vrf-name 
＞]
no mpls ldp 
 instance 
 ＜instance-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待创建实例的实例号
＜vrf-name＞|实例绑定的VRF名
缺省 : 
没有启动LDP协议和配置LDP实例，没有进入LDP配置模式。 
使用说明 : 
使用场景本命令使能LDP沿着普通的逐跳路由路径建立LSP，并且进入LDP配置模式，该命令是进行LDP各项配置的前提。使用no命令禁止LDP沿着普通的逐跳路由路径建立LSP，删除存在的各项LDP配置。本命令只支持M6000系列产品。89系列产品该配置命令为mpls ldp instance <1-65535>
范例 : 
配置公网实例和私网实例：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#exitZXROSNG(config)#no mpls ldp instance 1ZXROSNG(config)#ip vrf a  ZXROSNG(config-vrf)#rd 1:1ZXROSNG(config-vrf)#address-family ipv4 ZXROSNG(config-vrf-af)#exitZXROSNG(config-vrf)#exitZXROSNG(config)#mpls ldp instance 2 vrf aZXROSNG(config-ldp-2)#exitZXROSNG(config)#no mpls ldp instance 2
相关命令 : 
无 
## neighbor dual-stack transport-connection prefer 

neighbor dual-stack transport-connection prefer 
命令功能 : 
配置LDP接口下的hello发送消息中携带双栈传输连接优先地址族参数。使用no命令可恢复缺省值。 
命令模式 : 
 LDP接口模式  
命令默认权限级别 : 
15 
命令格式 : 
neighbor dual-stack transport-connection prefer 
  {ipv4 
|ipv6 
}
no neighbor dual-stack transport-connection prefer 
命令参数解释 : 
参数|描述
---|---
ipv4|指定IPv4直连hello发送消息中携带双栈传输连接IPv4优先参数
ipv6|指定IPv4直连hello发送消息中携带双栈传输连接IPv6优先参数
缺省 : 
缺省情况下，指定LDP IPv4接口下的hello发送消息中携带双栈传输连接IPv4优先参数 
使用说明 : 
前提要求LDP路由器间建立LDP会话，首先需要建立TCP 连接，这就要求每个路由器都知道对端的传输地址。若每个路由器均给对端通告了IPv4和IPv6类型的传输地址，则TCP连接类型依赖于传输地址通告的时间。使用场景neighbor dual-stack transport-connection prefer命令提供了指定hello发送消息中双栈TCP传输连接优先地址族的手段，该命令只在路由器本地双栈情况下生效。注意事项1、本地双栈时若配置了双栈传输连接优先地址族参数，必须满足两个条件才允许建立TCP连接：（1）.接口下的hello发送消息中携带双栈传输连接优先地址族参数必须和同一接口下的hello接收消息参数协商一致；（2）.接口下的hello发送消息中携带的双栈传输连接优先地址族参数必须和接口下实际通告给对端的传输地址类型一致。2、本地双栈时若和对端成功协商了双栈传输连接优先地址族参数，则建立TCP连接，如果在接口运行过程中改变建立双栈参数连接优先地址族参数，导致和hello接收消息中的双栈传输连接参数协商失败，LDP实例将解除接口上的当前邻接关系。3、如果路由器上存在多链路，那么路由器必须在这些接口上通告相同的双栈传输连接优先地址族。
范例 : 
在接口gei-0/1/0/1上配置hello发送消息中携带双栈传输连接IPv6优先参数：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface gei-0/1/0/1ZXROSNG(config-ldp-1-if-gei-0/1/0/1)#neighbor dual-stack transport-connection prefer ipv6删除配置：ZXROSNG(config-ldp-1-if-gei-0/1/0/1)#no neighbor dual-stack transport-connection prefer
相关命令 : 
无 
## neighbor dual-stack transport-connection prefer 

neighbor dual-stack transport-connection prefer 
命令功能 : 
配置LDP IPv6接口下的hello发送消息中携带双栈传输连接优先地址族参数。使用no命令可恢复缺省值。 
命令模式 : 
 LDP-V6接口模式  
命令默认权限级别 : 
15 
命令格式 : 
neighbor dual-stack transport-connection prefer 
  {ipv4 
|ipv6 
}
no neighbor dual-stack transport-connection prefer 
命令参数解释 : 
参数|描述
---|---
ipv4|指定IPv6直连hello发送消息中携带双栈传输连接IPv4优先参数
ipv6|指定IPv6直连hello发送消息中携带双栈传输连接IPv6优先参数
缺省 : 
使用场景缺省情况下，指定LDP IPv6接口下的hello发送消息中携带双栈传输连接IPv4优先参数
使用说明 : 
LDP路由器间建立LDP会话，首先需要建立TCP 连接，这就要求每个路由器都知道对端的传输地址。若每个路由器均给对端通告了IPv4和IPv6类型的传输地址，则TCP连接类型依赖于传输地址通告的时间。neighbor dual-stack transport-connection prefer命令提供了指定hello发送消息中双栈TCP传输连接优先地址族的手段，该命令只在路由器本地双栈情况下生效。本地双栈时若配置了双栈传输连接优先地址族参数，必须满足两个条件才允许建立TCP连接：1.接口下的hello发送消息中携带双栈传输连接优先地址族参数必须和同一接口下的hello接收消息参数协商一致；2.接口下的hello发送消息中携带的双栈传输连接优先地址族参数必须和接口下实际通告给对端的传输地址类型一致。本地双栈时若和对端成功协商了双栈传输连接优先地址族参数，则建立TCP连接，如果在接口运行过程中改变建立双栈参数连接优先地址族参数，导致和hello接收消息中的双栈传输连接参数协商失败，LDP实例将解除接口上的当前邻接关系。注意：如果路由器上存在多链路，那么路由器必须在这些接口上通告相同的双栈传输连接优先地址族。
范例 : 
在IPv6接口gei-0/1/0/1上配置hello发送消息中携带双栈传输连接IPv6优先参数：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#interface ipv6 gei-0/1/0/1ZXROSNG(config-ldp-1-ifv6-gei-0/1/0/1)#neighbor dual-stack transport-connection prefer ipv6删除配置：ZXROSNG(config-ldp-1-ifv6-gei-0/1/0/1)#no neighbor dual-stack transport-connection prefer
相关命令 : 
无 
## neighbor password 

neighbor password 
命令功能 : 
配置LDP实例与邻居建立TCP连接会话的全局密钥，使用no命令禁止该特性。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
neighbor password 
  {sealed 
 ＜sealed-password 
＞|＜clear-password 
＞}
no neighbor password 
命令参数解释 : 
参数|描述
---|---
sealed|明文反配置。
＜sealed-password＞|与邻居TCP连接会话的MD5密文密钥，长度为108的字符串。
＜clear-password＞|与邻居TCP连接会话的MD5明文密钥，长度为3–80的字符串。
缺省 : 
缺省情况下，LDP实例不存在全局MD5密钥。 
使用说明 : 
使用场景在两台LSR之间引入LDP全局MD5认证，对LDP实例下的每个TCP连接进行认证。注意事项全局MD5认证的生效条件为，不存在指定邻居IP地址的MD5或KeyChain密钥认证。若全局MD5认证启动生效，要在两个LSR上都配置全局MD5认证并使用相同的密钥，否则会话不能建立。MD5属于不安全的认证算法，为了保证更好的安全性，建议使用更安全的Keychain算法作为LDP的认证算法。
范例 : 
配置与邻居LSR使用zte作为全局MD5认证密钥建立会话：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#neighbor password zteZXROSNG(config-ldp-1)#neighbor password sealed GLu+q/2g9AcP3OnYqpsE9mhTLGtENV6ri2lYUjTKK1xgBpt86KOGdTCf0fHodPUyxrBJp4FhqV1NSrSWUaFNKgczU6O0U9GIeajuRYNyFhU=删除配置：ZXROSNG(config-ldp-1)#no neighbor password
相关命令 : 
无 
## peer ipv6 

peer ipv6 
命令功能 : 
配置IPv6冗余组成员，触发与冗余组成员之间自动创建ICCP IPv6会话。使用no命令可删除冗余组成员。 
命令模式 : 
 冗余组模式  
命令默认权限级别 : 
15 
命令格式 : 
peer ipv6 
  ＜ipv6-address 
＞
no peer ipv6 
  ＜ipv6-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|冗余组成员用于建链的对端IPv6传输层地址
缺省 : 
无 
使用说明 : 
使用场景冗余配置模式下输入该命令，两端在相同的冗余组下分别配置对端的用于建链的IPv6传输层地址，且本端LDP实例下需要配置用于建立target会话的本地IPv6传输层地址，且两端的LDP IPv6对端地址路由可达，两端的公网LDP实例均存在，才能建立ICCP的IPv6 LDP会话和冗余组连接。
范例 : 
两台机架分别配置冗余组1，在冗余组下分别配置冗余组远端成员：机架1上的配置：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#router-id loopback1ZXROSNG(config-ldp-1)#target ipv6 transport-address 128::1ZXROSNG(config-ldp-1)#exitZXROSNG(config)# redundancy interchassis group 1ZXROSNG(config-red-1)#peer ipv6 128::2在机架2上的配置：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#router-id loopback1ZXROSNG(config-ldp-1)#target ipv6 transport-address 128::2ZXROSNG(config-ldp-1)#exitZXROSNG(config)# redundancy interchassis group 1ZXROSNG(config-red-1)#peer ipv6 128::1R1查看配置结果信息：ZXROSNG(config-red-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 128::2    Active Mode: STANDARD      IccpState: ICCP_NONCONNECT删除配置：ZXROSNG(config-red-1)#no peer ipv6 128::2ZXROSNG(config-red-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:ID: 1ZXROSNG(config-red-1)#
相关命令 : 
redundancy interchassis groupshow mpls ldp iccp
## peer 

peer 
命令功能 : 
配置LDP peer bfd相关参数，LDP会话up后，会触发创建与指定邻居的peer bfd会话，根据配置来确定是否LDP会话up后延迟一段时间，触发创建BFD会话，使用no命令删除。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
peer 
 bfd 
 remote-routerid 
 ＜ip-address 
＞ [delay 
 [＜time 
＞]]
no peer 
 bfd 
 remote-routerid 
 ＜ip-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|指定建立bfd的邻居router id地址
delay|是否配置延迟
＜time＞|具体延迟创建时间，范围0-720，单位秒
缺省 : 
默认不创建peer bfd保护 
使用说明 : 
使用场景1、该命令触发peer bfd的创建，两端都配置相应的peer bfd。2、可配置延迟创建BFD会话3、不配置delay时，LDP会话up后立即触发创建BFD会话4、当只配置delay时，默认LDP会话up后延迟时间60秒，触发创建BFD会话，60秒为延迟默认值5、当配置具体延迟创建时间时，则LDP会话up后延迟配置时间，触发创建BFD会话
范例 : 
配置触发创建router id为2.2.2.2的peer bfd会话，立即创建：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# peer bfd remote-routeid 2.2.2.2配置触发创建router id为2.2.2.2的peer bfd会话，延迟默认时间创建：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# peer bfd remote-routeid 2.2.2.2 delay配置触发创建router id为2.2.2.2的peer bfd会话，延迟120秒后创建：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)# peer bfd remote-routeid 2.2.2.2 delay 120
相关命令 : 
无 
## peer 

peer 
命令功能 : 
配置冗余组成员，触发与冗余组成员之间自动创建ICCP会话。使用no命令可删除冗余组成员。 
命令模式 : 
 冗余组模式  
命令默认权限级别 : 
15 
命令格式 : 
peer 
  ＜ip-address 
＞
no peer 
  ＜ip-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|冗余组成员的router id
缺省 : 
无 
使用说明 : 
使用场景冗余配置模式下输入该命令，两端在相同的冗余组下分别配置对端的LDP router id，且两端的LDP router id路由可达，两端的公网LDP实例均存在，才能建立ICCP的LDP会话和冗余组连接。
范例 : 
两台机架分别配置冗余组1，在冗余组下分别配置冗余组远端成员：机架1上的配置，机架2的router id为2.2.2.2：ZXROSNG(config)# redundancy interchassis group 1ZXROSNG(config-red-1)#peer 2.2.2.2在机架2上的配置，机架1的router id为1.1.1.1：ZXROSNG(config)# redundancy interchassis group 1ZXROSNG(config-red-1)#peer 1.1.1.1查看配置结果信息：ZXROSNG(config-red-1)#show mpls ldp iccp    RGID Table total ICCP sessions:0RGID Table:  ID: 1    PeerAddr: 1.1.1.1      IccpState: ICCP_NONCONNECT 删除配置：ZXROSNG(config-red-1)#no peer 1.1.1.1ZXROSNG(config-red-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1ZXROSNG(config-red-1)#
相关命令 : 
redundancy interchassis groupshow mpls ldp iccp
## prepare new-label-range 

prepare new-label-range 
命令功能 : 
该命令工作于标签管理模式下，用于配置静态标签预备范围。标签管理模块处于共享模式时（由产品规格确定），若需要新建或者扩大静态标签范围，则需要先使用本命令事先准备好标签资源，等标签资源准备就绪之后才能进行静态标签范围配置。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
prepare new-label-range 
  ＜label-min 
＞ ＜label-max 
＞ [cancel 
]
命令参数解释 : 
参数|描述
---|---
＜label-min＞|用于配置静态标签预备范围最小值。取值范围：标签范围大小16-1048575。默认值：无。
＜label-max＞|用于配置静态标签预备范围最大值。取值范围：标签范围大小16-1048575。默认值：无。
cancel|用于标识该命令操作为删除之前配置的静态标签预备范围。默认值：无。
缺省 : 
无 
使用说明 : 
    拥有管理员权限的操作员可以使用这条命令。    该命令为操作命令，show runnning无显示。    该命令主要是为了新建一个标签范围，或者对当前标签范围大小进行扩大所需，预先回收prepare范围内的标签。    最多可以配置1条。
范例 : 
删除上一次配置的静态标签预备范围，最小值为100，最大值为200，则输入以下命令：ZXROSNG(config-lm)# prepare new-label-range 100 200 cancel配置静态标签预备范围，最小值为100，最大值为200，则输入以下命令：ZXROSNG(config)#mpls label  manageZXROSNG(config-lm)# prepare new-label-range 100 200
相关命令 : 
show mpls label  managempls label managestatic-label-range <label-min> <label-max>
## recursor 

recursor 
命令功能 : 
使能MLDP的递归MFEC功能。 
命令模式 : 
 MLDP模式  
命令默认权限级别 : 
15 
命令格式 : 
recursor 
 mfec 
no recursor 
 mfec 
命令参数解释 : 
No参数|描述
---|---
mfec|
缺省 : 
缺省情况下不使能递归MFEC。
使用说明 : 
使用场景MBB功能是MLDP的辅助功能，缺省情况下不使能，该功能主要是为在跨域情况下依然能够建立LSP。
范例 : 
路由器上使能MBB：ZXROSNG(config)#mpls ldp instance 1  ZXROSNG(config-ldp-1)#mldpZXROSNG(config-ldp-1-mldp)#recursor mfec 
相关命令 : 
show running-config 
## redundancy interchassis group 

redundancy interchassis group 
命令功能 : 
设备间配置冗余组。使用no命令删除配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
redundancy interchassis group 
  ＜group-id 
＞
no redundancy interchassis group 
  ＜group-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜group-id＞|冗余组号，范围：1-$#100728843#$
缺省 : 
无 
使用说明 : 
使用场景全局配置模式下输入该命令，配置完成后进入冗余配置模式。目前最多支持配置4096个冗余组。
范例 : 
配置冗余组1：ZXROSNG(config)# redundancy interchassis group 1ZXROSNG(config-red-1)#查看配置结果信息：ZXROSNG(config-red-1)#show mpls ldp iccpRGID Table total ICCP sessions:0RGID Table:  ID: 1删除配置：ZXROSNG(config)#no redundancy interchassis group 1ZXROSNG(config)#
相关命令 : 
show mpls ldp iccppeerhostnameapply mc-pw apply mc-port
## redundancy interchassis peer-mode standard 

redundancy interchassis peer-mode standard 
命令功能 : 
配置与对端设备建链使用的模式是按照标准模式，还是私有模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
redundancy interchassis peer-mode standard 
  ＜acl-name 
＞
no redundancy interchassis peer-mode standard 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|对端Router-ID地址ACL集合名，长度为1-31个字符
缺省 : 
默认模式是private模式，no命令恢复默认模式。 
使用说明 : 
使用场景配置与对端设备建链使用的模式是按照标准模式，还是私有模式。注意事项1、全局配置模式下配置该命令，如果模式与前次不同且LDP会话已经发起建链，则给出提示，下次才能生效，The sessions which are already up should be restarted to make this config take effect。2、删除模式配置时，模式自动恢复为private配置，如果模式与前次不同且LDP会话已经发起建链，则给出返回码提示，下次才能生效，The sessions which are already up should be restarted to make this config take effect。
范例 : 
配置标准模式：ZXROSNG(config)#ipv4-access-list zteZXROSNG(config-ipv4-acl)#rule 1 permit any ZXROSNG(config-ipv4-acl)#!ZXROSNG(config)#redundancy interchassis peer-mode standard zte%Info 129: The sessions which are already up should be restarted to make this config take effect查看配置结果信息：ZXROSNG(config)#show mpls ldp iccp RGID Table total ICCP sessions:1RGID Table:  ID: 1    PeerAddr: 111.111.111.111    Active Mode: STANDARD      IccpState: ICCP_CONNECTED删除配置：ZXROSNG(config)#no redundancy interchassis peer-mode standardZXROSNG(config)#
相关命令 : 
show mpls ldp iccpredundancy interchassis group
## reset mpls ldp 

reset mpls ldp 
命令功能 : 
重置LDP实例，清空实例相关的所有的数据表项，包括FEC、会话、接口等。根据实例的配置信息重新加载生成数据表项。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
reset mpls ldp 
  {instance 
 ＜instance-id 
＞|all 
}
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待重置实例的实例号
缺省 : 
无 
使用说明 : 
使用场景重置LDP实例，配置该命令，因为数据表项要清空，需要用户操作确认。
范例 : 
重置实例1：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#exitZXROSNG(config)# reset mpls ldp instance allAre you sure to reset the MPLS LDP instances? [yes/no]:noZXROSNG(config)# reset mpls ldp instance 1Are you sure to reset the MPLS LDP instances? [yes/no]:yes
相关命令 : 
无 
## session protection 

session protection 
命令功能 : 
配置会话保护功能，使用no命令恢复默认情况。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
session protection 
  [{duration 
 ＜duration-time 
＞|infinite 
}] [for 
 ＜peer-acl 
＞]
no session protection 
命令参数解释 : 
参数|描述
---|---
＜duration-time＞|当会话上基本发现机制失效时，会话保护生成的扩展发现机制的保持时间
infinite|当会话上基本发现机制失效时，会话保护生成的扩展发现机制的保持时间为无限
＜peer-acl＞|会话保护功能的对端router id过滤规则，对符合规则的会话进行保护，长度1–31个字符
缺省 : 
缺省情况下， LDP实例的会话保护功能不开启。不指定duration time或者不配置infinite的情况下，默认的duration保持时间为86400秒(24小时)。 
使用说明 : 
使用场景配置会话保护功能，对符合规则的直连会话创建非直连保护，当LDP邻居的直连链路出现故障，基本发现机制失效时，利用LDP的扩展发现机制来保持与LDP邻居之间的会话，确保当LDP基本发现机制恢复时，LDP协议能够快速收敛，减少了流量的损失。注意事项配置命令参数为可选，每次重新配置命令时，覆盖前次配置。未配置保护保持时间时，默认参数为86400秒，默认值可在show running-config ldp all 中显示。
范例 : 
LDP实例下使能会话保护功能：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#session protectionZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#show running-config ldp! <MPLS>mpls ldp instance 1session protectionrouter-id gei-0/1/0/1interface gei-0/1/0/1$! </MPLS>ZXROSNG(config-ldp-1)#show running-config ldp all !<ldp>#error packet ldp tcp record enable record-number 10#error packet ldp udp record enable record-number 10mpls ldp instance 1  #auto-config interface global enable  #auto-config ipv6 interface global enable  #backoff 15 120  #discovery hello holdtime 15  #discovery hello interval 5  #discovery targeted-hello holdtime 45  #discovery targeted-hello interval 15  #graceful-restart timer max-recovery 120  #graceful-restart timer neighbor-liveness 120  #holdtime 180  #igp sync delay 5  interface gei-0/1/0/1  $  #lsp-control independent  router-id loopback1  session protection duration 86400$!</ldp>
相关命令 : 
show running-config ldpshow running-config ldp all
## show debug ldp 

show debug ldp 
命令功能 : 
检查当前设备LDP debugging信息开启情况。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug ldp 
  [instance 
 ＜instance-id 
＞] 
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景检查当前设备LDP debugging信息开启情况。
范例 : 
检查当前设备LDP debugging信息开启情况：ZXROSNG#show debug ldpLDP:  Instance 1:    LDP label and address advertisements debugging is on    LDP Label Information Base (LIB) changes debugging is on    LDP received messages debugging is on    LDP sent messages debugging is on    LDP session I/O debugging is on    LDP session state machine (low level) debugging is on    LDP transport connection events debugging is on    LDP transport events debugging is on    LDP GR events debugging is on
相关命令 : 
无 
## show error packet ldp statistics 

show error packet ldp statistics 
命令功能 : 
显示LDP错误报文统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show error packet ldp statistics 
  [instance 
 ＜instance-id 
＞] [interface 
 ＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|实例号，范围[1,65535],显示该实例的错误报文统计
＜interface-name＞|接口名，显示该接口对应会话的错误报文统计
缺省 : 
无 
使用说明 : 
使用场景该命令用来查看LDP错误报文的统计信息。
范例 : 
查看ldp错误报文的统计信息：ZXROSNG#show error packet ldp statistics   Error UDP packet state                    : OFF  Max UDP error packet number       : 10  Current UDP error packet number   : 0  Error TCP packet state            : OFF  Max TCP error packet number       : 10  Current TCP error packet number   : 0域    描述Error UDP packet state    UDP 错误报文使能状态Max UDP error packet number    支持的最大UDP错误报文记录数Current UDP error packet number    当前UDP错误报文记录数Error TCP packet state    TCP 错误报文使能状态Max TCP error packet number    支持的最大TCP错误报文记录数Current TCP error packet number    当前TCP错误报文记录数
相关命令 : 
无 
## show error packet ldp 

show error packet ldp 
命令功能 : 
显示LDP错误报文统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show error packet ldp 
  {udp 
|tcp 
} [{instance 
 ＜instance-id 
＞|number 
 ＜number 
＞|interface 
 ＜interface-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
udp|报文类型    udp:显示UDP错误报文信息tcp:显示TCP报文信息
tcp|报文类型    udp:显示UDP错误报文信息tcp:显示TCP报文信息
＜instance-id＞|实例号，显示该实例的错误报文信息
＜number＞|序列号，显示指定序列号的错误报文信息
＜interface-name＞|接口名，显示该接口对应的错误报文信息
缺省 : 
无 
使用说明 : 
使用场景该命令主要用来查看LDP实例下TCP/UDP类型的错误报文统计信息。
范例 : 
查看LDP实例1下，TCP类型错误报文的统计信息：ZXROSNG#show error packet ldp tcp instance 1Packet Index : 2Record Time  : 2015-10-26 14:55:50Interface    : gei-0/1/0/1Instance ID  : 1Peer LDP ID  : 20.20.20.100:0Length       : 32Error Reason : LDP PACKET TLV VALUE ERROR0000: 00  01  00  1c  14  14  14  64  00  00  00  01  00  12  00  00 0010: 00  7f  03  00  00  0a  80  00  00  14  00  00  00  00  00  00 ---------------------------------------------------------------------查看LDP实例1下，UDP类型错误报文的统计信息：ZXROSNG#show error packet ldp udp instance 1Packet Index : 3Record Time  : 2015-10-26 14:54:39Interface    : gei-0/1/0/1Instance ID  : 1Peer LDP ID  : 20.20.20.100:0Length       : 32Error Reason : LDP PACKET TLV VALUE ERROR0000: 00  01  00  1c  14  14  14  64  00  00  00  01  00  12  00  00 0010: 00  77  03  00  00  0a  80  00  00  14  00  00  00  00  00  00 ---------------------------------------------------------------------域    描述Packet index    错误报文序列号Record Time    记录错误报文的时间Interface    接收错误报文的接口Instance ID    LDP实例IDPeer LDP ID    邻居会话的LDP标识Length           错误报文的长度Error Reason    错误报文错误的原因
相关命令 : 
无 
## show mpls label manage 

show mpls label manage 
命令功能 : 
该命令工作于除用户模式外的其他所有模式下，用于查询标签资源共享情况。标签管理模块处于共享模式时（由产品规格确定），该命令显示了各个协议标签池对标签资源的使用情况。
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls label manage 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
    拥有管理员权限的操作员可以使用这条命令。    可显示各个标签池的名称 、标签池出错标识、标签池锁定标识、预留的标签数量、本地化的标签数量、显示各协标签范围最小值、标签范围最大值、静态标签空洞数量、Kompella标签空洞数量、遗留标签数量、 采样时刻的已用标签数量。
范例 : 
查询标签资源共享情况，则输入以下命令：ZXROSNG#show mpls label manageHeaders: F - Label Range Fixed; E - JOB status Error;S-Hole - Static Label Holes; K-Hole - Kompella Label Holes;S-LDP - Static LDP; S-PW - Static Pseudo Wire;S-TE - Static TE; S-VRF - Static VRF;Marks: /Irrelevant; *Fixed; +Error; ?Unknown-------------------------------------------------------------------------------Service  E Localized Reserved F Label-Range     S-Hole  K-Hole  Legacy  Used-------- - --------- -------- - --------------- ------- ------- ------- -------S-LDP      10000     /        * 290000-299999   /       /       0       /S-PW       100001    /        * 300000-400000   /       /       0       /Static     1001      /          500-1500        /       /       0       /Static     1500      /          1501-3000       /       /       0       /Static     93306      /         4000-97305      /       /       0       /LDP        42727     2000       /               /       /       0       ?PWE3       170910    8000       /               /       /       0       ?RSVP       21365     1000       /               /       /       0       ?BGP        149335    0          /               /       /       0       ?BGPv6      149335    0          /               /       /       0       ?Kompella   24576     0          954368-978943   0       /       0       ?AC         149336    0          /               /       /       0       ?Forbid     101       /          800000-800100   0       0       /       ?      Forbid     100       /          800101-800200   0       0       /       ?   SRGB       65536     /        * 978944-1044479  0       /       /       ?SRLB       4096      /        * 1044480-1048575 0       /       /       ?Prepared   0         /          /               /       /       /       /Free       65536     /          /               /       /       /       /GLOBAL     1048560   11000    * 16-1048575      0       0       0       ?输出项名称    输出结果解释Service        “Service”为“GLOBAL”时，表示全局标签池，因此“Localized”、“Reserved”、“S-Hole”、“K-Hole”和“Legacy”都显示为本列数据的统计值，其中“Localized”包括“NULL Localized”，且其值应当与“Label-Range”的区间长度加上“Legacy”的和相等。    当“Service”为“Free”时，只有“Localized”有效，表示那些没有本地化的标签，这些标签还没有被推送到任何业务的本地标签池，处于空闲状态，待其他业务发生标签短缺时，直接分配给它；当“Service”为“Prepared”时，表示用户通过“prepare new-label-range”命令给静态业务准备的标签段。         当“Service”为“Forbid”时，表示用户通过“forbidden-label-range”命令设置了禁用标签段，本段范围内的标签不被任何业务使用。Localized    显示相应业务的本地化标签总数，当“Label-Range”一列有效时，此处的值就是标签范围内标签总数减去标签空洞的数量。Reserved    显示相应业务的预留标签的值，当“Label-Range”一列有效时，本列的值就是该区间的长度。Fixed    显示相应业务的标签池是否被严格锁定在某一指定（通过性能参数）区间内，且不可通过命令行调整，对于动态业务（Kompella除外）来说，只有当此列为“YES”时，“Label-Range”才有效；对于所有业务来说，当此列为“YES”时，“Legacy（遗留标签数）”、“S-Hole（静态标签空洞数）”和“K-Hole（Kompella标签空洞数）”无效。Label-Range    显示各业务的标签范围，对于LDP等标签共享的业务来说，这一列一般不相关，但是，比如，当LABMGR_LDP_LOCK设置为“YES”时，LDP就不再是标签共享的业务，这一列就要显示实际的标签范围。S-Hole    表示Service类型中存在多少个被静态标签占用。K-Hole    表示Service类型中存在多少个被Kompella协议占用。Legacy    表示有多少标签已经被本协议占用，但目前这些标签被其他协议所有。Used    表示业务使用了多少标签，如果显示“？”，表示不确定数，这个数据通过采样得到的。
相关命令 : 
1）kompella-range-size <label-range-size> 2）static-label-range <label-min> <label-max> 3）label-reservation {[ldp < ldp-label-range-size >], [pwe3 < pwe3-label-range-size >], [rsvp < rsvp-label-range-size >], [bgp < bgp-label-range-size >], [bgpv6 <bgpv6-label-range-size >]}4）prepare new-label-range <label-min> <label-max>
## show mpls label manage-mode 

show mpls label manage-mode 
命令功能 : 
该命令工作于除用户模式外的其他所有模式下，用于查询本系统标签管理模式，是共享模式还是非共享模式。标签管理模块模式由产品规格确定。
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls label manage-mode 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
    拥有管理员权限的操作员可以使用这条命令。    显示系统标签管理是以共享模式启动，还是非共享模式启动。
范例 : 
查询本系统标签管理模式，则输入以下命令：ZXROSNG(config)# show mpls label manage-mode The system is unshared label management mode.输出项名称    输出结果解释标签管理模式    unshared label management mode ：非共享模式，各个标签池独享相互不重叠的标签范围。shared label management mode ：共享模式，部分动态标签池共享一个大的标签范围。
相关命令 : 
无 
## show mpls label usage detail 

show mpls label usage detail 
命令功能 : 
用于查询标签资源详细使用情况。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls label usage detail 
  ＜label-min 
＞ ＜label-max 
＞ [{free 
|allocated 
 [＜service-type 
＞]}] 
命令参数解释 : 
参数|描述
---|---
＜label-min＞|用于配置标签范围下限。取值范围：标签值16-1048575。
＜label-max＞|用于配置标签范围上限。取值范围：标签值16-1048575。
free|显示空闲标签。
allocated|显示已分配给业务和特殊标签池的标签。
＜service-type＞|显示已分配给某业务或者某特殊标签池的标签。
缺省 : 
无 
使用说明 : 
    可显示当前标签范围中的每个标签值，以及各个标签所属的标签池名称。    通过可选参数free、allocated可选择查询内容，free表示只查询标签范围中的空闲标签； allocated 表示只查询标签范围中的已分配标签；allocated之后携带业务类型或者特殊标签池类型，表示只查询标签范围中的已分配给该业务或者该标签池的标签 。
范例 : 
查询标签资源详细使用情况，则输入以下命令：ZXROSNG#show mpls label usage detail 16 20Marks: --Unavailable--------------------Label   Service------- ------------16      Static17      Static18      Static19      Static20      StaticZXROSNG#查询标签范围中的空闲标签，则输入以下命令：ZXROSNG#show mpls label usage detail 800000 800004 freeMarks: --Unavailable--------------------Label   Service------- ------------800000      Free800001      Free800002      Free800003      Free800004      Free查询标签范围中的已分配标签，则输入以下命令：ZXROSNG#show mpls label usage detail 16 20 allocatedMarks: --Unavailable--------------------Label   Service------- ------------16      Static17      Static18      Static19      Static20      Static输出项名称           输出结果解释Label                 标签值Service               标签所属的标签池名称
相关命令 : 
1）kompella-range-size <label-range-size>2）static-label-range <label-min> <label-max>3）label-reservation {[ldp < ldp-label-range-size >], [pwe3 < pwe3-label-range-size >], [rsvp < rsvp-label-range-size >], [bgp < bgp-label-range-size >], [bgpv6 <bgpv6-label-range-size >]}4）prepare new-label-range <label-min> <label-max>
## show mpls label usage 

show mpls label usage 
命令功能 : 
用于查询标签资源使用情况(目前静态和SRGB两标签池无法查看)。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls label usage 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
可显示每个标签池的名称，获取从每个标签池采样标签使用情况的时间、每个标签池的标签总数、每个标签池标签使用个数、每个标签池使用标签比例。 
范例 : 
查询标签资源使用情况，则输入以下命令：ZXROSNG(config)#show mpls label usage Sample time: 2016-10-10 23:26:44Sample period: 60(s)------------------------------------Service  Localized Used      Percent -------- --------- --------- -------LDP      2000      0         0.0    PWE3     200       65        32.5%  RSVP     1000      0         0.0    BGP      0         0         0.0    BGPv6    0         0         0.0    Kompella 720000    0         0.0    AC       0         0         0.0    SRLB     4096      0         0.0    ZXROSNG(config)#输出项名称                  输出结果解释Sample time       采样时间Sample period     采样周期Service                          表示每个需要标签资源的业务，其中静态业务与SRGB业务标签管理模块只负责分配一段标签资源，不负责标签资源分配情况，所以无法获取其使用情况，这里不显示这两个业务；Localized      显示相应业务的本地化标签总数；Used              显示相应业务已使用标签的总数； Percent       显示标签资源使用情况百分比，是Used的个数占Total个数比例；
相关命令 : 
1）kompella-range-size <label-range-size>2）static-label-range <label-min> <label-max>3）label-reservation {[ldp < ldp-label-range-size >], [pwe3 < pwe3-label-range-size >], [rsvp < rsvp-label-range-size >], [bgp < bgp-label-range-size >], [bgpv6 <bgpv6-label-range-size >]}4）prepare new-label-range <label-min> <label-max>
## show mpls ldp backoff 

show mpls ldp backoff 
命令功能 : 
显示LDP实例的会话退避重建参数的配置，及处于退避重建状态的会话。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp backoff 
 instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景查看实例下会话重建的退避参数。
范例 : 
查看实例1下会话的退避重建参数：ZXROSNG#show mpls ldp backoff instance 1LDP initial/maximum backoff: 30/240 secBackoff table: 2 entriesLDP Id                Backoff(sec)  Waiting(sec)  Local LDP Id100.0.0.44:0          60            30            100.0.0.11:0          100.0.0.55:0          120           90            100.0.0.22:0域    描述LDP initial/maximum backoff    显示秒为单位的退避参数LDP Id    LDP邻居标识Backoff(sec)    显示退避时间Waiting(sec)    显示已经退避的时间Local LDP Id   LDP会话本地标识
相关命令 : 
backoff 
## show mpls ldp bindings summary 

show mpls ldp bindings summary 
命令功能 : 
检查LDP的学习到的标签统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp bindings summary 
  [{ipv4 
|ipv6 
}] instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景查看实例下，LDP协议学习到的标签统计信息。
范例 : 
查看实例1下，标签统计信息：ZXROSNG(config)#show mpls ldp bindings summary instance 1The total number of prefixes: 4The total number of upstream LSP control blocks: 4The total number of downstream LSP control blocks: 4Generic label bindings                      Assigned         Learned       Prefixes      in labels      out labels              4              4               1
相关命令 : 
label-advertiseexplicit-nullegress
## show mpls ldp bindings 

show mpls ldp bindings 
命令功能 : 
检查LDP的学习到的标签绑定。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp bindings 
  [{brief 
|[{ipv6 
 [＜ipv6-address 
＞ ＜mask-length 
＞]|ipv4 
 [＜ip-address 
＞ {＜mask 
＞|＜mask-length 
＞} [longer-prefixes 
]]|＜ipv6-address 
＞ ＜mask-length 
＞|＜ip-address 
＞ {＜mask 
＞|＜mask-length 
＞} [longer-prefixes 
]}] [{[local-label 
 ＜local-label-from 
＞ [- 
 ＜local-label-to 
＞]] [remote-label 
 ＜remote-label-from 
＞ [- 
 ＜remote-label-to 
＞]] [neighbor 
 ＜ip-address 
＞]|local-only 
|remote-only 
}] [detail 
]}] instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
brief|带该选项：列表方式显示FEC简要信息不带该选项：普通方式显示FEC相关信息
＜ipv6-address＞|IPv6类型的地址前缀
＜mask-length＞|指定掩码长度，范围：0–32
＜ip-address＞|对端地址
＜mask＞|指定网络掩码，为十进制点分形式
＜mask-length＞|指定掩码长度，范围：0–32
longer-prefixes|显示所有指定网络匹配而掩码更长的网络的标签绑定
＜ipv6-address＞|IPv6类型的地址前缀
＜mask-length＞|指定掩码长度，范围：0–32
＜ip-address＞|对端地址
＜mask＞|指定网络掩码，为十进制点分形式
＜mask-length＞|指定掩码长度，范围：0–32
longer-prefixes|显示所有指定网络匹配而掩码更长的网络的标签绑定
local-label|显示与本地标签值匹配的条目，使用label-label参数指定标签范围，范围：0–1048575
＜local-label-from＞|本地标签上限
＜local-label-to＞|本地标签下限
remote-label|显示与邻居分配的标签值匹配的条目，使用label–label参数指定标签范围，范围：0–1048575
＜remote-label-from＞|邻居分配的标签值上限
＜remote-label-to＞|邻居分配的标签值下限
＜ip-address＞|对端地址
local-only|显示只有本地标签的FEC信息
remote-only|显示只有远端标签的FEC信息
detail|详细信息
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景如果不带任何参数，本命令显示本实例的LDP FEC表中所有条目及下游绑定。
范例 : 
显示本实例的LDP FEC表中所有条目及下游绑定：ZXROSNG#show mpls ldp bindings instance 1144.0.0.0/8local binding: label: imp-nullremote binding:155.0.0.55:0->155.0.0.66:0, label: 1766.66.0.66:0->66.66.0.77:0, label: 18144.0.0.44:0->144.0.0.55, label: imp-null155.0.0.0/8local binding: label: 19remote binding:155.0.0.55:0->155.0.0.66:0, label: imp-null(inuse)66.66.0.66:0->66.66.0.77:0, label: 16144.0.0.44:0->144.0.0.55, label: imp-null166.66.0.66/32local binding: label: 20remote binding:155.0.0.55:0->155.0.0.66:0, label: 1966.66.0.66:0->66.66.0.77:0, label: imp-null(inuse)144.0.0.44:0->144.0.0.55, label: 18177.0.0.0/8local binding: label: imp-null188.0.0.55/32local binding: label: 25remote binding:155.0.0.55:0->155.0.0.66:0, label: imp-null(inuse)144.0.0.44:0->144.0.0.55, label: 2466.66.0.66:0->66.66.0.77:0, label: 24……显示从LSR 144.0.0.44学到的关于网络166.0.0.0及其子网的标签绑定：ZXROSNG#show mpls ldp bindings 166.0.0.0 8 longer-prefixes neighbor 144.0.0.44 instance 1166.44.0.0/16local binding: label: 29remote binding:144.0.0.44:0->144.0.0.55, label: 25166.246.0.0/16local binding: label: 32remote binding:144.0.0.44:0->144.0.0.55, label: 46. . .显示一条具体FEC的标签绑定信息：ZXROSNG#show mpls ldp bindings 166.0.0.0 8 detail instance 1144.0.0.0/8local binding: label: imp-nulladvertised:155.0.0.66:0->155.0.0.55:0label withdraw delay remaining: 65533 s66.66.0.77:0->66.66.0.66:0144.0.0.55:0->144.0.0.44:0remote binding:155.0.0.55:0->155.0.0.66:0, label: 1766.66.0.66:0->66.66.0.77:0, label: 18144.0.0.44:0->144.0.0.55, label: imp-null域信息描述表：域                 描述a.b.c.d/e        IP前缀及掩码local binding    本地标签绑定advertised        向邻居通告，->左侧表示本地route-id，右侧标识远端route-idlabel withdraw delay remaining    发送标签撤销消息的剩余时间（倒计时）remote binding   从邻居学习到的标签绑定，->左侧表示远端route-id，右侧表示本地route-id以列表方式显示本实例的LDP FEC表中所有条目及简要信息：ZXROSNG(config)#show mpls ldp bindings brief instance 1Headers: Adv:Count of advertised peers,Rmt:Count of bindings from remote peersPrefix              Local     Adv   RmtLabel1.1.1.0/24          imp-null  1     11.1.1.1/32          UnAsgnd   0     11.1.1.2/32          imp-null  1     01.9.9.0/24          imp-null  1     11.9.9.1/32          imp-null  1     02.9.9.0/24          205824    1     12.9.9.1/32          UnAsgnd   0     110.10.10.10/32      205825    1     120.20.20.20/32      imp-null  1     1…域信息描述表：域                 描述Prefix        IP前缀及掩码Local Label    本地标签绑定，其中UnTag代表无本地标签，UnAsgnd代表还未分配本地标签，imp-null代表隐式空标签，exp-null代表显式空标签Adv        向不同对端通告的数目Rmt       从邻居学习到的标签绑定数
相关命令 : 
label-advertiseexplicit-nullegresslabel-withdraw-delay
## show mpls ldp debug-policy 

show mpls ldp debug-policy 
命令功能 : 
显示LDP当前debug控制策略。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp debug-policy 
 instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景该命令用来查看LDP实例下设置的所有debug-policy策略。debug-policy是一种debug的控制策略，主要用来针对性的监控debug的内容。
范例 : 
查看LDP实例1下debug-policy的控制策略：ZXROSNG#show mpls ldp debug-policy instance 1debug-policy:   hello:       hello interface gei-0/1/0/1       target-hello 1.1.1.2       target-hello ipv6 20::2   transport connections:       peertransaddr ipv4 1.1.1.2       peertransaddr ipv6 20::2   session:       remote-routeid 2.2.2.2 labelspace 65535       remote-routeid 1.1.1.2 labelspace 0域                                                  描述debug-policy                             debug策略显示hello                                             hello相关debug策略transport connections            tcp链接相关debug策略session                                        session相关debug策略
相关命令 : 
无 
## show mpls ldp discovery 

show mpls ldp discovery 
命令功能 : 
检查LDP发现信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp discovery 
  [{brief 
|detail 
}] instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
brief|列表方式显示LDP发现信息简要信息
detail|显示LDP发现信息相关详细信息
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景本命令支持显示实例下所有LDP发现信息包括接口，直链非直链hello收发情况、通过[detail]选项可以增加显示发现信息的详细信息，本地通告的传输地址，hello收发的源地址和目的地址，hello收发的报文计数，邻居指示的双栈传输连接优先地址族，通过[brief]选项可以列表方式显示LDP发现信息的简要信息和LDP发现信息的统计信息。
范例 : 
显示LDP发现信息普通信息：ZXROSNG(config-ldp-1)#show mpls ldp discovery instance 1Target Hello Types:  I : ICCP, P : PW, C : LDP config,                      A : LDP accept, T : APP triggerInterfaces:gei-0/1/0/1: xmit/recvPeer  LDP ID: 3.3.3.3:0; Local LDP ID:6.6.6.6:0IP addr: 3.3.3.3Targeted Hellos:6.6.6.6 --> 3.3.3.3 (C): xmit/recvPeer LDP ID: 3.3.3.3:0; Local LDP ID:6.6.6.6:0IP addr: 3.3.3.36.6.6.6 --> 3.3.3.3(I): xmitLocal LDP ID:6.6.6.6:65535Peer LDP ID: 3.3.3.3:65535; IP addr: 3.3.3.3域                            描述Local LDP ID      本地LDP标识Peer  LDP ID                        远端LDP标识Interface                  参与LDP发现的接口列表Xmit                       指出接口上正发送hello报文Recv                       指出接口上正接收hello报文Src IP addr                邻居发送hello报文的源地址Transport IP addr          邻居指示的TCP连接传输地址显示LDP发现信息详细信息：ZXROSNG(config-ldp-1)#show mpls ldp discovery detail instance 1Target Hello Types:  I : ICCP, P : PW, C : LDP config,                      A : LDP accept, T : APP triggerInterfaces:gei-0/1/0/1: xmit/recvPeer  LDP ID: 3.3.3.3:0Local LDP ID: 6.6.6.6:0Src IP addr: 12.12.1.1; Transport IP addr: 3.3.3.3Targeted Hellos:6.6.6.6 --> 3.3.3.3: xmit/recvPeer  LDP ID: 3.3.3.3:0Local LDP ID: 6.6.6.6:0Src IP addr: 3.3.3.3; Transport IP addr: 3.3.3.36.6.6.6 --> 1111:2222:3333:4444:5555:6666:7777:8888: xmit6.6.6.6 --> 3.3.3.3 (I): xmit/recvPeer  LDP ID: 3.3.3.3:65535Local LDP ID: 6.6.6.6:65535Src IP addr: 3.3.3.3; Transport IP addr: 3.3.3.3域                            描述Local LDP ID        本地LDP标识Peer  LDP ID         远端LDP标识Interface                  参与LDP发现的接口列表Xmit                       指出接口上正发送hello报文Recv                       指出接口上正接收hello报文LDP IDd                   对端LDP标识Src IP addr                邻居发送hello报文的源地址Transport IP addr          邻居指示的TCP连接传输地址显示LDP发现信息列表信息：ZXROSNG(config-ldp-1)#show mpls ldp discovery brief instance 1Discovery Source    Peer LDP ID           Local LDP ID          Holdtime Sessiongei-0/1/0/1         3.3.3.3:0             6.6.6.6:0             15       YTarget:3.3.3.3      3.3.3.3:0             6.6.6.6:0             45       Y Target: 1.1.1.1     -                     -                     -        N                                                                     Target:3.3.3.3      3.3.3.3:65535         6.6.6.6:65535         45       Y域                            描述Local LDP ID       本地LDP标识，标签空间0和65535分别显示Discovery Source    参与LDP发现的接口，或非直链时的target地址Peer LDP ID             对端LDP标识，有hello显示，无hello时显示“-”Holdtime                  保活时间，有hello显示hello当前时间，单位s，无时显示“-”Session                     显会话状态，Oper状态时显示“Y”,其他情况显示“N”
相关命令 : 
无 
## show mpls ldp graceful-restart 

show mpls ldp graceful-restart 
命令功能 : 
检查路由器当前LDP实例的LDP Graceful Restart 配置情况。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp graceful-restart 
 instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|LDP实例号
缺省 : 
无 
使用说明 : 
使用场景查看当前实例下GR的具体配置信息。
范例 : 
查看实例1下GR的具体配置信息：router#show mpls ldp graceful-restart instance 1LDP Graceful Restart is enabledNeighbor Liveness Timer: 30 secondsMax Recovery Timer: 40 secondsGraceful Restart-enabled Sessions:Peer LDP Ident: 11.1.1.2:0;State:Oper ;Loc-ID: 11.11. 11.1:0Peer LDP Ident: 11.1.1.2:0;State:Oper ;Loc-ID: 11.11.11.3:0域    描述LDP Graceful Restart is enabled    显示是否使能GRNeighbor Liveness Timer  LSR等待LDP session会话恢复的最长时间（单位：秒）Max Recovery Timer  LSR等待对端邻居进行标记恢复的最长时间（单位：秒）Peer LDP Ident   LDP会话邻居标识State   LDP会话状态Loc-ID   LDP会话本地标识
相关命令 : 
graceful-restart 
## show mpls ldp iccp 

show mpls ldp iccp 
命令功能 : 
显示ICCP相关的LDP会话及冗余组链接、应用链接状态信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp iccp 
  [detail 
] [rg 
 ＜group-id 
＞] 
命令参数解释 : 
参数|描述
---|---
detail|带该选项显示冗余组详细信息
＜group-id＞|冗余组号，范围：1-$#100728843#$
缺省 : 
无 
使用说明 : 
使用场景show mpls ldp iccp，不带参数，显示所有的与ICCP相关的冗余组信息和LDP会话信息。带可选参数detail，可显示冗余组详细信息；带可选参数rg <group-id>，显示特定的冗余组信息和LDP会话信息。
范例 : 
显示机架上冗余组1的ICCP相关冗余组信息和LDP会话信息：ZXROSNG(config-red-1)#show mpls ldp iccp rg 1RGID Table total ICCP sessions:1RGID Table:  ID: 1  hostname: abc    PeerAddr: 2.2.2.2      IccpState: ICCP_CONNECTED    AppType: Mc_aps      AppState:  APP_CONNECTEDZXROSNG(config-red-1)show mpls ldp iccp detailRGID Table total ICCP sessions:1RGID Table:  ID: 1    PeerAddr: 2.2.2.2    Active Mode: PRIVATE      IccpState: ICCP_CONNECTED      Msgs sent/rcvd: 35/20    AppType: VLAN      AppState: APP_CONNECTED      Msgs sent/rcvd: 35/20域                                    描述RGID Table total ICCP sessions     冗余组ID表相关联的ICCP会话数RGID Table                        冗余组ID表，显示冗余组的相关信息，ICCP状态，应用协议类型，应用协议状态ID                               冗余组IDhostname                         冗余组本地主机名PeerAddr                         冗余组对端成员的router-idIccpState                       ICCP连接状态AppType                        应用协议类型AppState                        应用连接状态Msgs sent/rcvd:                   消息收发计数
相关命令 : 
redundancy interchassis grouppeerapply mc-pwapply mc-port hostname
## show mpls ldp igp sync 

show mpls ldp igp sync 
命令功能 : 
显示LDP IGP同步状态信息
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp igp sync 
  [{brief 
|[interface 
 [ipv6 
] ＜ifname 
＞] [detail 
]}] instance 
 ＜para 
＞ 
命令参数解释 : 
参数|描述
---|---
brief|带该选项：列表方式显示IGP同步简要信息不带该选项：普通方式显示IGP同步信息
＜ifname＞|待显示的接口名
detail|带该选项：显示IGP同步的会话相关信息不带该选项：不显示IGP同步的会话相关信息
＜para＞|待显示的实例号
缺省 : 
无
使用说明 : 
使用场景本命令支持显示实例下所有接口的LDP同步状态，也可显示实例下指定接口的LDP同步状态。通过带[interface]选项可以显示指定接口信息，通过[ipv6]选项只显示IPv6的接口信息，不带[ipv6]选项只显示IPv4的接口信息，通过[detail]选项可以增加显示会话相关的信息，通过[brief]选项可以列表方式显示IGP同步简要信息。
范例 : 
显示所有IPv4和IPv6接口且不带会话内容的信息：ZXROSNG#show mpls ldp igp sync instance 1gei-0/1/0/1:LDP configured; LDP-IGP Synchronization enabled.gei-0/1/0/1:LDP IPv6 configured; LDP-IGP IPv6 Synchronization enabled.te_tunnel1:LDP Interface IGP Sync configured; LDP-IGP Synchronization enabled.显示指定IPv4接口且不带会话内容的信息：ZXROSNG#show mpls ldp igp sync interface gei-0/1/0/1 instance 1gei-0/1/0/1:LDP configured; LDP-IGP Synchronization enabled.显示指定IPv6接口且不带会话内容的信息：ZXROSNG#show mpls ldp igp sync interface ipv6 gei-0/1/0/1 instance 1gei-0/1/0/1:LDP V6 configured; LDP-IGP V6 Synchronization enabled.显示所有IPv4和IPv6接口且带会话内容的信息：ZXROSNG#show mpls ldp igp sync detail instance 1gei-0/1/0/1:LDP configured; LDP-IGP Synchronization enabled.Sync status: ReadyLocal: 11.1.1.1:0Peers:20.20.20.100:0 (Fully Operational)gei-0/1/0/1:LDP IPv6 configured; LDP-IGP IPv6 Synchronization enabled.Sync status: ReadyLocal: 11.1.1.2:0Peers:20.20.20.100:0 (Fully Operational)te_tunnel1:LDP Interface IGP Sync configured; LDP-IGP Synchronization enabled.Sync status: ReadyLocal: 11.1.1.3:0Peers:20.20.20.100:0 (Fully Operational)显示指定IPv4接口且带会话内容的信息：ZXROSNG#show mpls ldp igp sync interface gei-0/1/0/1 detail instance 1gei-0/1/0/1:LDP configured; LDP-IGP Synchronization enabled.Sync status: ReadyLocal: 11.1.1.1:0Peers:20.20.20.100:0 (Fully Operational)显示指定IPv6接口且带会话内容的信息：ZXROSNG#show mpls ldp igp sync interface ipv6 gei-0/1/0/1 detail instance 1gei-0/1/0/1:LDP V6 configured; LDP-IGP V6 Synchronization enabled.Sync status: ReadyLocal: 11.1.1.2:0Peers:20.20.20.100:0 (Fully Operational)列表方式显示IGP同步简要信息：ZXROSNG# show mpls ldp igp sync brief instance 1Interface of LDP IGP synchronization:Headers: AF:Address FamilyCoders : LDP:LDP interface enabled or LDP IGP sync interface enabledIGP:IGP LDP sync enabledSync:IGP sync state,Y(Full Operational)/N(Not Ready)Interface                         AF        LDP    IGP   Syncgei-0/1/0/1                    IPv4       Y      Y     Yte_tunnel1                      IPv4       Y      N     N显示各域说明：域 描述LDP configured; LDP-IGP Synchronization enabled. 显示IPv4接口LDP配置状态和LDP-IGP同步使能配置状态LDP IPv6 configured; LDP-IGP IPv6 Synchronization enabled. 显示IPv6接口LDP配置状态和LDP-IGP同步使能配置状态LDP Interface IGP Sync configured; LDP-IGP Synchronization enabled. 显示te_tunnel类型接口IGP同步使能状态和LDP-IGP同步使能配置状态Sync status:  显示同步是否完成Local:LDP会话本地标识Peers: LDP邻居，(Fully Operational)表示会话处于up状态，还有可能是(GR Process)表示会话处于GR过程中。Interface    接口名称AF          接口的地址类型LDP       “Y”表示LDP接口使能LDP IGP同步 “N”表示未使能LDP IGP同步IGP       “Y”表示IGP使能LDP IGP同步 “N”表示未使能LDP IGP同步Sync     “Y”表示IGP同步达到Full Operational状态，“N”表示未达到
相关命令 : 
interface
## show mpls ldp instance statistic 

show mpls ldp instance statistic 
命令功能 : 
以列表方式显示所有LDP实例统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp instance statistic 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
使用场景显示所有LDP实例统计信息。
范例 : 
显示所有LDP实例统计信息：ZXROSNG(config)#show mpls ldp instance statistic Instance  Sessions(Oper) Hellos  Bindings1         1(1)           2       2  域            描述Instance  LDP实例号Sessions实例下会话个数Oper          实例下会话状态为Oper个数Hellos       实例下hello个数Bindings实例下接收标签个数
相关命令 : 
无 
## show mpls ldp interface 

show mpls ldp interface 
命令功能 : 
检查启动的LDP的接口。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp interface 
  [＜interface-name 
＞] instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口名称
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景如没有<interface-name>的可选参数，则显示实例下所有启动的LDP的接口的相关信息
范例 : 
查看实例1下使能的接口：ZXROSNG#show mpls ldp interface instance 1interface of LDP:Interface            AF          IP               Operationalgei-0/1/0/1         IPV4        Yes(ldp)        Nogei-0/1/0/2         IPV4        Yes(ldp)        Nogei-0/1/0/3         IPV6        Yes(ldp)        Yesgei–0/3/0/1         IPV6        Yes(ldp)        No域            描述Interface    接口名称AF          接口的地址类型IP          “Yes”表示支持MPLS隧道标签交换Operational    接口状态
相关命令 : 
interface 
## show mpls ldp log hello-down 

show mpls ldp log hello-down 
命令功能 : 
显示LDP hello邻接体断链原因等信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp log hello-down 
 instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
instance|LDP实例
＜instance-id＞|待显示实例的实例号，范围1-65535
缺省 : 
无 
使用说明 : 
使用场景本命令支持显示当前实例下记录的hello邻接体断链的条目数以及列表方式显示实例下LDP hello邻接体断链的原因等信息。
范例 : 
显示LDP hello down相关信息：ZXROSNG(config)#show mpls ldp log hello-down instance 1Total number of LDP hello down: 3Discovery Source    Peer-LDP-ID     Local-LDP-ID    Down-date Down-timeDuration-time  Reasongei-0/1/0/1         11.1.1.1:0      11.1.1.2:0      2018-8-15 06:28:3800:14:58       Router-id changedgei-0/1/0/1         11.1.1.1:0      11.1.1.2:0      2018-8-15 06:13:3300:00:03       LDP interface config deletedgei-0/1/0/1         11.1.1.1:0      11.1.1.2:0      2018-8-15 06:13:2400:01:53       Interface down域信息描述：表头统计部分：Total number of LDP hello down     当前LDP hello邻接体断链日志条目数表格内容部分：Discovery Source    参与LDP邻接体发现的接口，或非直链时的target地址Peer LDP ID             对端LDP标识Local LDP ID           本地LDP标识，标签空间0和65535分别显示Down-date              LDP hello邻接体断链的具体日期Down-time              LDP hello邻接体断链的具体时间Duration-time        LDP hello邻接体从发现到断链经历的时间Reason                    LDP hello 邻接体断链的具体原因
相关命令 : 
无 
## show mpls ldp log neighbor-down 

show mpls ldp log neighbor-down 
命令功能 : 
显示LDP 会话断链原因等信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp log neighbor-down 
 instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
instance|LDP实例
＜instance-id＞|待显示实例的实例号，范围1-65535
缺省 : 
无 
使用说明 : 
使用场景本命令支持显示当前实例下记录的会话断链的条目数以及通过列表方式显示实例下LDP会话断链的原因等信息。
范例 : 
显示LDP会话down相关信息：ZXROSNG(config)#show mpls ldp log neighbor-down instance 1Total number of LDP session down: 5Peer-LDP-ID     Local-LDP-ID    Down-date Down-time Duration-                                                    timeReason11.1.1.2:0      10.1.1.1:0      2018-8-3  00:36:56  15:22:31Router-id changed11.1.1.2:0      11.1.1.1:0      2018-8-3  00:36:56  15:22:23Interface down11.1.1.2:0      11.1.1.1:0      2018-8-2  09:14:29  00:00:03LDP interface config deleted11.1.1.2:0      11.1.1.1:0      2018-8-2  09:14:21  00:02:53Clear LDP session11.1.1.2:0      10.1.1.1:0      2018-8-2  09:14:21  00:00:06Clear LDP session域信息描述：表头统计部分：Total number of LDP session down     当前LDP会话down日志条目数表格内容部分：Peer LDP ID             对端LDP标识Local LDP ID           本地LDP标识，标签空间0和65535分别显示Down-date              LDP会话down的具体日期Down-time              LDP会话down的具体时间Duration-time        LDP会话从up到down经历的时间Reason                    LDP会话down的具体原因
相关命令 : 
无 
## show mpls ldp neighbor 

show mpls ldp neighbor 
命令功能 : 
检查LDP会话信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp neighbor 
  {brief 
|{graceful-restart 
|[＜ip-address 
＞ [{detail 
|msg-counter 
}]]|[＜interface-name 
＞ [detail 
]]|[detail 
]|[msg-counter 
]}} instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
brief|带该选项：列表方式显示会话简要信息不带该选项：普通方式显示会话信息
graceful-restart|显示LDP 邻居GR相关信息。
＜ip-address＞|邻居IP地址，为十进制点分形式
detail|带该选项显示指定地址的LDP邻居详细信息。
msg-counter|LDP TCP消息计数统计
＜interface-name＞|接口名称，显示从指定接口接受的邻居
detail|带该选项显示指定接口的LDP邻居详细信息。
detail|带该选项显示LDP邻居详细信息。
msg-counter|LDP TCP消息计数统计
instance|LDP实例。
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景该命令主要用来显示LDP实例下的会话信息。
范例 : 
显示LDP实例的会话信息详细信息：ZXROSNG#show mpls ldp neighbor detail instance 1Peer LDP Ident: 172.1.1.1:0; Local LDP Ident 200.1.1.1:0        TCP connection: 204.1.1.100.1025 - 200.1.1.1.646        State: Oper; Msgs sent/rcvd: 257/222; Downstream        Up time: 01:09:15        LDP discovery sources:          gei-0/1/0/1; Src IP addr: 204.1.1.100            holdtime: 15000 ms, hello interval: 5000 ms          gei-0/1/0/2; Src IP addr: 196.1.1.100            holdtime: 15000 ms, hello interval: 5000 ms        Addresses bound to peer LDP Ident:           196.1.1.100     204.1.1.100     180.1.1.100        Session holdtime: 60000 ms; KA interval: 20000 msLDP Peer BFD state up.LDP dynamic capability enable:    LDP send capability:     LDP dynamic capability    LDP received capability:     LDP dynamic capability negotiate success显示从指定接口gei-0/1/0/1接收的邻居：ZXROSNG#show mpls ldp neighbor gei-0/1/0/1 instance 1Peer LDP Ident: 172.1.1.1:0; Local LDP Ident 200.1.1.1:0        TCP connection: 204.1.1.100.1025 - 200.1.1.1.646        State: Oper; Msgs sent/rcvd: 262/226; Downstream        Up time: 01:10:35        LDP discovery sources:          gei-0/1/0/1, Src IP addr: 204.1.1.100          gei-0/1/0/2, Src IP addr: 196.1.1.100        Addresses bound to peer LDP Ident:           196.1.1.100     204.1.1.100     180.1.1.100域信息描述表：域                      描述Peer LDP Ident      邻居该会话的LDP标识Local LDP Ident      本路由器该会话的LDP标识TCP connection      支持该会话的TCP连接State                   会话的状态Msgs sent/rcvd      通过会话接收和发送的ldp消息数Downstream            指示会话采用下游自主标签分发控制方式Downstream on demand 指示会话采用下游按需标签分发控制方式Up time            会话在当前状态存在时间LDP discovery sources维护会话的邻接关系列表interface            邻接关系建立的接口Src IP addr            建立邻接关系的对端hello报文源IP地址holdtime            邻接关系收不到hello包的保持时间hello interval      邻接关系协商的hello发送间隔Addresses bound to peer LDP Ident    邻居在此会话上通告的所有接口的ip地址，这些ip地址可能是本地路由条目中的下一跳Session holdtime      邻居收不到ldp消息后会话维持时间KA interval    KeepAlive消息发送间隔
相关命令 : 
interface 
## show mpls ldp parameters 

show mpls ldp parameters 
命令功能 : 
检查LDP当前参数信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp parameters 
 instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜instance-id＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景查看实例下具体的参数信息，如果没有配置则显示默认值。
范例 : 
查看实例1下的配置参数信息：ZXROSNG#show mpls ldp parameters  instance 1Protocol version: 1Session holdtime: 180 sec; keep alive interval: 60 secDiscovery hello: holdtime: 15 sec; interval: 5 secDiscovery targeted hello: holdtime: 45 sec; interval: 15 secLDP for targeted sessionsDownstream On Demand max hop count: 255LDP initial/maximum backoff: 15/120 secLDP used lsp control mode: IndependentLDP configred lsp control mode: IndependentLDP used label retention mode: LiberalLDP configred label retention mode: LiberalLDP loop detection: offLDP IGP sync delay: 5 secLDP entropy label capability: EnableLDP LSP DoD request queue mode: EnableLDP over TE LSP: Enable域                                    描述Protocol version                      版本Session hold time                     会话保持时间设置keep alive interval    KeepAlive      发送时间Discovery hello                       基本发现机制参数设置Downstream on Demand max hop count 预留版本升级LDP initial/maximum backoff          LDP会话退避重建机制参数设置LDP loop detection                    预留版本升级Discovery targeted hello              扩展发现机制参数设置LDP for targeted sessions              LDP远端会话LDP used lsp control mode          当前使用的lsp控制方式LDP configred lsp control mode     当前配置的的lsp控制方式LDP used label retention mode      当前使用的标签保持模式LDP configred label retention mode 当前配置的标签保持模式LDP entropy label capability  当前是否支持熵标签能力LDP LSP DoD request queue mode 请求队列保存功能是否使能LDP over TE LSP                     当前是否使能LDP over TE标签下发
相关命令 : 
无 
## show mpls ldp traffic-count 

show mpls ldp traffic-count 
命令功能 : 
检查LDP LSP的性能统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls ldp traffic-count 
  [{ipv6 
 [＜ipv6-address 
＞ ＜mask-length 
＞]|ipv4 
 [＜ip-address 
＞ {＜mask 
＞|＜mask-length 
＞}]|＜ipv6-address 
＞ ＜mask-length 
＞|＜ip-address 
＞ {＜mask 
＞|＜mask-length 
＞}}] instance 
 ＜instance-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|指定网段IPv6地址
＜mask-length＞|指定IPv4掩码长度，范围为0-32
＜ip-address＞|指定网段IPv4地址
＜mask＞|指定IPv4网络掩码
＜mask-length＞|指定IPv4掩码长度，范围为0-32
＜ipv6-address＞|指定网段IPv6地址
＜mask-length＞|指定IPv4掩码长度，范围为0-32
＜ip-address＞|指定网段IPv4地址
＜mask＞|指定IPv4网络掩码
＜mask-length＞|指定IPv4掩码长度，范围为0-32
＜instance-id＞|待显示的LDP实例号
缺省 : 
无 
使用说明 : 
使用场景输入可选参数目的网段及网络掩码，则显示该可选参数对应的FEC的性能统计信息。不输入可选参数，则显示当前LDP实例下的所有符合统计策略的FEC的性能统计信息。
范例 : 
显示本实例的指定网段的fec的性能统计信息：ZXROSNG#show mpls ldp traffic-count 131.131.131.131 255.255.255.255 instance 1131.131.131.131/32     Inflow:      18446744073709551615 Byte(s),                     2 Packet(s)     Outflow:              25769742763 Byte(s),                     3 Packet(s)     LostInflow:  18446744073709551614 Byte(s),                     5 Packet(s)     LostOutflow:          25769742830 Byte(s),                     3 Packet(s)ZXROSNG#show mpls ldp traffic-count ipv6 128:: 64 instance 1 128::/64    Inflow:                    9551615 Byte(s),                48930  Packet(s)    Outflow:                   8551615 Byte(s),                 47456 Packet(s)    LostInflow:                      0 Byte(s),                     0 Packet(s)    LostOutflow:                     0 Byte(s),                     0 Packet(s)域信息描述表：域    描述a.b.c.d/e    IP地址及掩码Inflow    入方向流量Outflow    出方向流量LostInflow    入方向丢失流量LostOutflow    出方向丢失流量
相关命令 : 
traffic-count-fectraffic-count-fec ipv6
## show mpls mldp bindings summary 

show mpls mldp bindings summary 
命令功能 : 
检查mLDP的学习到的标签统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls mldp bindings summary 
 instance 
 ＜<1-65535> 
＞ 
命令参数解释 : 
参数|描述
---|---
＜<1-65535>＞|待显示实例的实例号
缺省 : 
无 
使用说明 : 
使用场景用来查看mLDP学习到的标签统计信息。
范例 : 
显示实例1下mLDP学习到的标签统计信息：ZXROSNG(config)#show mpls mldp bindings summary instance 1The total number of each type of mFECs:Tunnel ID(TI):     0         IPv4 Source(4S):   0    IPv6 Source(6S):   0         IPv4 Bidir(4B):    0  IPv6 Bidir(6B):    0         VPNv4 Source(V4S): 0  VPNv6 Source(V6S): 0         VPNv4 Bidir(V4B):  0 VPNv6 Bidir(V6B):  0         Rosen MDT(RM):     6Pub Recursive(PR): 0         VPN Recursive(VR): 0    The total number of upstream LSP control blocks: 0The total number of downstream LSP control blocks: 6Generic label bindings                 Assigned         Learned       mFEC     in labels      out labels          6             0               6域信息描述表：域                 描述mFEC                  mFEC总个数Assigned in labels    为mFEC分配的入标签Learned out labels     本端mFEC学习到的出标签
相关命令 : 
show mpls mldp bindings 
## show mpls mldp bindings 

show mpls mldp bindings 
命令功能 : 
检查mLDP的学习到的标签绑定。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls mldp bindings 
  [＜ip_address 
＞ {[＜<0-4294967295> 
＞]|[＜source-address 
＞ ＜group-address 
＞ [{<0-65535>:<0-4294967295> 
|<1-65535>.<0-65535>:<0-65535> 
|A.B.C.D:<0-65535> 
}]]|[recursor 
]|[＜vnp-id 
＞ ＜mdt-number 
＞]}] [local-label 
 ＜local-label-min 
＞ [- 
 ＜local-label-max 
＞]] [remote-label 
 ＜remoter-label-min 
＞ [- 
 ＜remoter-label-max 
＞]] [neighbor 
 ＜ip_address 
＞] [{brief 
|detail 
}] instance 
 ＜<1-65535> 
＞ 
命令参数解释 : 
参数|描述
---|---
＜ip_address＞|邻居地址
＜<0-4294967295>＞|mLSP ID。范围0-4294967295
＜source-address＞|指定源地址
＜group-address＞|指定组地址
<0-65535>:<0-4294967295>|ASN_NN格式的路由标识符
<1-65535>.<0-65535>:<0-65535>|ASND_NN格式的路由标识符
A.B.C.D:<0-65535>|IPADD_NN格式的路由标识符
recursor|递归mfec标记
＜vnp-id＞|VPN ID，格式<3 bytes OUI:4 bytes VPN_Index>
＜mdt-number＞|MDT组播树编号0-5000
local-label|本地标签
＜local-label-min＞|显示与本地标签值匹配的条目，标签范围最小值
＜local-label-max＞|显示与本地标签值匹配的条目，标签范围最大值
remote-label|远端标签
＜remoter-label-min＞|显示与邻居分配的标签值匹配的条目，标签范围最小值
＜remoter-label-max＞|显示与邻居分配的标签值匹配的条目，标签范围最大值
neighbor|对端邻居
＜ip_address＞|邻居地址
brief|带该选项：列表方式显示mFEC简要信息 不带该选项：普通方式显示mFEC相关信息
detail|显示详细信息
＜<1-65535>＞|LDP实例号
缺省 : 
无 
使用说明 : 
使用场景如果不带任何参数，本命令显示mLDP  mFEC表中所有条目及下游绑定。
范例 : 
显示本实例的mLDP mFEC表中所有条目及下游绑定：ZXROSNG#show mpls mldp bindings instance 11.1.1.1/1001local binding:  label: 16384remote binding: lsr: 3.3.3.3:0, label: 16388(inuse)ZXROSNG(config)#show mpls mldp bindings detail instance 11.1.1.1/1001local binding:  label: 16384advertised to:2.2.2.2:0域信息描述表：域    描述a.b.c.d/e    mFElocal binding    本地标签绑定advertise to    向邻居通告remote binding    从邻居学习到的标签绑定以列表方式显示本实例的mLDP mFEC表中所有条目及简要信息：ZXROSNG(config)#show mpls mldp bindings brief instance 1Headers: Adv:Count of advertised peers         Rmt:Count of bindings from remote peers         Opaque value type codes : TI:  Tunnel ID,     RM:  Rosen MDT                                   4S:  IPv4 Source,   6S:  IPv6 Source                                   4B:  IPv4 Bidir,    6B:  IPv6 Bidir                                   V4S: VPNv4 Source,  V6S: VPNv6 Source                                   V4B: VPNv4 Bidir,   V6B: VPNv6 Bidir                                   PR:  Pub Recursive, VR:  VPN RecursivePrefix                              OpqType           Local     Adv   Rmt                                                      Label1.1.1.1/1:100,0                     RM                UnTag     0     11.1.1.2/1:100,0                     RM                UnTag     0     11.1.1.3/1:100,0                     RM                UnTag     0     11.1.1.4/1:100,0                     RM                UnTag     0     11.1.1.5/1:100,0                     RM                UnTag     0     11.1.1.6/1:100,0                     RM                UnTag     0     1域信息描述表：域                 描述Prefix        IP前缀及Opq valueOpqType  Opq类型Local Label    本地标签绑定，其中UnTag代表无本地标签，UnAsgnd代表还未分配本地标签，imp-null代表隐式空标签，exp-null代表显式空标签Adv        向不同对端通告的数目Rmt       从邻居学习到的标签绑定数
相关命令 : 
show mpls mldp bindings summary 
## show mpls mldp parameters 

show mpls mldp parameters 
命令功能 : 
检查MLDP能力等信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls mldp parameters 
 instance 
 ＜<1-65535> 
＞ 
命令参数解释 : 
参数|描述
---|---
＜<1-65535>＞|LDP实例号
缺省 : 
无 
使用说明 : 
使用场景查看MLDP能力等信息。
范例 : 
查看MLDP能力等信息：ZXROSNG(config-ldp-1-mldp)#show mpls mldp parameters instance 1Capability:     P2MP : Enable    MP2MP: Disable    MBB  : Enable         Wait time: 5 sec
相关命令 : 
无 
## srgb-label-range 

srgb-label-range 
命令功能 : 
用于配置SRGB标签范围。标签管理模块处于共享模式时（本产品为$#117571622:0/非共享模式;1/共享模式#$），可通过该命令设置全局标签范围内某段标签范围被SRGB业务使用。可通过该命令实现SRGB标签范围的新建、修改、删除。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
srgb-label-range 
  ＜label-min 
＞ ＜label-max 
＞
no srgb-label-range 
命令参数解释 : 
参数|描述
---|---
＜label-min＞|用于配置SRGB标签范围最小值。 取值范围：标签范围大小16-1048575。默认值为$#117571658#$。
＜label-max＞|用于配置SRGB标签范围最大值。 取值范围：标签范围大小16-1048575。默认值为$#117571659#$。
缺省 : 
SRGB段配置范围为$#117571658#$- $#117571659#$。如果是0-0，表示不支持SRGB标签段。 
使用说明 : 
1）本命令可以设置SRGB业务的标签范围，该标签范围不可超过全局标签值范围（$#117571650#$ - $#117571651#$），该配置范围不可与动态锁定范围，静态业务，kompella等业务标签范围有重叠。2) 如果修改的SRGB范围是在原来SRGB范围之内，直接配置，立即生效。3）如果修改的SRGB范围超出原来SRGB范围，可以事先执行prepare new-label-range  ＜label-min＞ ＜label-max＞ 命令回收此范围内被其他业务占用的标签，也可以不执行该prepare命令。若事先执行了prepare命令，则SRGB范围配置立即生效；否则，可能出现SRGB范围配置延迟生效。4） SRGB标签范围与 segment-routing 配置模式下 SID 配置相互冲突时，会导致配置不成功。互斥条件：SRGB标签总数必须大于或等于SID最大值加一。该互斥条件只在配置过程中校验，加载过程中不校验。5）no srgb-label-range支持不重启生效，即，若no命令执行后没有提示或者报错信息，则表明已经立即生效；若no命令执行后提示稍后生效，则按照以下步骤查询确认no命令生效。a）show running-config  label-mgr all 查看默认SRGB范围。ZXROSNG#show running-config  label-mgr all!<label-mgr>mpls label manage#auto-relocalization enable#srlb-label-range 500000 504095#srgb-label-range 900000 965535b）show mpls label manage查看当前生效的SRGB范围，关注“Service”等于“SRGB”的显示行，该行的“Label-Range”列显示即为当前生效范围，“Localized”列为SRGB当前可本地化的标签数量。在产品规格支持SRGB的情况下，若“SRGB”的“Label-Range”显示为“0-0”，则表明no命令未生效；若“SRGB”的“Label-Range”显示为SRGB默认范围，则表明no操作已生效。ZXROSNG#show mpls label manageHeaders: F - Label Range Fixed; E - JOB status Error;S-Hole - Static Label Holes; K-Hole - Kompella Label Holes;S-LDP - Static LDP; S-PW - Static Pseudo Wire;S-TE - Static TE; S-VRF - Static VRF;Marks: /Irrelevant; *Fixed; +Error; ?Unknown-------------------------------------------------------------------------------Service  E Localized Reserved F Label-Range     S-Hole  K-Hole  Legacy  Used-------- - --------- -------- - --------------- ------- ------- ------- -------Static     205808    /          16-205823       /       /       0       /LDP        27202     2000       /               0       /       0       ?PWE3       108511    8000       /               0       /       0       ?RSVP       13653     1000       /               0       /       0       ?BGP(1)     34078     2500       /               0       /       0       ?BGP(2)     36478     2500       /               0       /       0       ?BGPv6(1)   100413    0          /               0       /       0       ?BGPv6(2)   100411    0          /               0       /       0       ?Kompella   24576     0          1024000-1048575 0       /       0       ?AC         100411    0          /               0       /       0       ?SRGB       65500     /          0-0             0       /       0       ?SRLB       100411    0          /               /       /       0       ?BIER       65536     0          600000-665535   0       0       0       ?Prepared   0         /          /               /       /       /       /Free       65536     /          /               /       /       /       /GLOBAL     1048560   16000    * 16-1048575      0       0       0       ?c）若第二步中表明no命令未生效，则查看 show mpls label usage detail ＜label-min＞ ＜label-max＞ ，关注默认SRGB范围中各个标签的目前归属的业务标签池。“Service”列表示标签当前归属的标签池，其中“Free”表示未被任何业务标签池本地化，可由标签管理自由分配。若标签显示归属于某业务标签池，且未被业务实际使用，则稍等30秒后，再次查看该命令，标签将显示为“Free”。ZXROSNG#show mpls label usage detail 900000 900002Marks: --Unavailable--------------------Label   Service------- ------------900000  PWE3900001  LDP900002  Freed）若第c步查询后，发现有些标签一直归属于某业务标签池，则可能此标签被业务实际占用，则需要业务主动释放该标签，标签才能调度回到标签管理服务端。待SRGB默认范围内所有标签都调试回到服务端，则no srgb-label-range的操作生效。show mpls label manage查看当前生效的SRGB范围，关注“Service”等于“SRGB”的显示行，该行的“Label-Range”列显示即为当前生效范围。
范例 : 
配置SRGB标签范围，最小值为100，最大值为200，则输入以下命令：ZXROSNG(config-lm)#repare new-label-range 100 200ZXROSNG(config-lm)#srgb-label-range 100 200删除配置的srgb标签范围：ZXROSNG(config-lm)#no srgb-label-range
相关命令 : 
prepare new-label-rangeshow mpls label manage
## srlb-label-range 

srlb-label-range 
命令功能 : 
用于配置SRLB标签范围。标签管理模块处于共享模式时（本产品为$#117571622:0/非共享模式;1/共享模式#$），可通过该命令设置全局标签范围内某段标签范围被SRLB业务使用。可通过该命令实现SRLB标签范围的新建、修改、删除。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
srlb-label-range 
  ＜label-min 
＞ ＜label-max 
＞
no srlb-label-range 
命令参数解释 : 
参数|描述
---|---
＜label-min＞|用于配置SRLB标签范围最小值。 取值范围：标签范围大小16-1048575。默认值为$#117571653#$。
＜label-max＞|用于配置SRLB标签范围最大值。 取值范围：标签范围大小16-1048575。默认值为$#117571654#$。
缺省 : 
SRLB段配置范围为$#117571653#$- $#117571654#$。如果是0-0，表示不支持SRLB标签段。 
使用说明 : 
1）本命令可以设置SRLB业务的标签范围，该标签范围不可超过全局标签值范围（$#117571650#$ - $#117571651#$），该配置范围不可与动态锁定范围，静态业务，kompella等业务标签范围有重叠。2）label-reservation  {[srlb ＜srlb-label-range-size＞]}中srlb选项在后继项目仍存在，因此会同时存在srlb-label-range  ＜label-min＞ ＜label-max＞和label-reservation  {[srlb ＜srlb-label-range-size＞]}两条命令，具体哪个命令生效，由SRLB模式（$#117571662:0/非共享模式;1/共享模式#$）确定。当前系统为$#117571662:0/非共享模式，label-reservation  {[srlb ＜srlb-label-range-size＞]}命令有效，配置srlb-label-range命令时会报错;1/共享模式，srlb-label-range命令有效，则配置label-reservation  {[srlb ＜srlb-label-range-size＞]}时报错#$。3) 如果修改的SRLB范围是在原来SRLB范围之内，直接配置，立即生效。4）如果修改的SRLB范围超出原来SRLB范围，可以事先执行prepare new-label-range  ＜label-min＞ ＜label-max＞ 命令回收此范围内被其他业务占用的标签，也可以不执行该prepare命令。若事先执行了prepare命令，则SRLB范围配置立即生效；否则，可能出现SRLB范围配置延迟生效。5) no srlb-label-range支持不重启生效，即，若no命令执行后没有提示或者报错信息，则表明已经立即生效；若no命令执行后提示稍后生效，则按照以下步骤查询确认no命令生效。a）show running-config  label-mgr all 查看默认SRLB范围。ZXROSNG#show running-config  label-mgr all!<label-mgr>mpls label manage#auto-relocalization enable#srlb-label-range 965536 969631#srlb-label-range 900000 965535b）show mpls label manage查看当前生效的SRLB范围，关注“Service”等于“SRLB”的显示行，该行的“Label-Range”列显示即为当前生效范围，“Localized”列为SRLB当前可本地化的标签数量。在产品规格支持SRLB的情况下，若“SRLB”的“Label-Range”显示为“0-0”，则表明no命令未生效；若“SRLB”的“Label-Range”显示为SRLB默认范围，则表明no操作已生效。ZXROSNG#show mpls label manageHeaders: F - Label Range Fixed; E - JOB status Error;S-Hole - Static Label Holes; K-Hole - Kompella Label Holes;S-LDP - Static LDP; S-PW - Static Pseudo Wire;S-TE - Static TE; S-VRF - Static VRF;Marks: /Irrelevant; *Fixed; +Error; ?Unknown-------------------------------------------------------------------------------Service  E Localized Reserved F Label-Range     S-Hole  K-Hole  Legacy  Used-------- - --------- -------- - --------------- ------- ------- ------- -------Static     205808    /          16-205823       /       /       0       /LDP        27202     2000       /               0       /       0       ?PWE3       108511    8000       /               0       /       0       ?RSVP       13653     1000       /               0       /       0       ?BGP(1)     34078     2500       /               0       /       0       ?BGP(2)     36478     2500       /               0       /       0       ?BGPv6(1)   100413    0          /               0       /       0       ?BGPv6(2)   100411    0          /               0       /       0       ?Kompella   24576     0          1024000-1048575 0       /       0       ?AC         100411    0          /               0       /       0       ?SRGB       65536     /          900000-965535             0       /       0       ?SRLB       4093    0          /               0-0       /       0       ?BIER       65536     0          600000-665535   0       0       0       ?Prepared   0         /          /               /       /       /       /Free       65536     /          /               /       /       /       /GLOBAL     1048560   16000    * 16-1048575      0       0       0       ?c）若第二步中表明no命令未生效，则查看 show mpls label usage detail ＜label-min＞ ＜label-max＞ ，关注默认SRLB范围中各个标签的目前归属的业务标签池。“Service”列表示标签当前归属的标签池，其中“Free”表示未被任何业务标签池本地化，可由标签管理自由分配。若标签显示归属于某业务标签池，且未被业务实际使用，则稍等30秒后，再次查看该命令，标签将显示为“Free”。ZXROSNG#show mpls label usage detail 969629 969631Marks: --Unavailable--------------------Label   Service------- ------------969629  PWE3969630  LDP969631  Freed）若第c步查询后，发现有些标签一直归属于某业务标签池，则可能此标签被业务实际占用，则需要业务主动释放该标签，标签才能调度回到标签管理服务端。待SRLB默认范围内所有标签都调度回到服务端，则no srlb-label-range的操作生效。show mpls label manage查看当前生效的SRLB范围，关注“Service”等于“SRLB”的显示行，该行的“Label-Range”列显示即为当前生效范围。
范例 : 
配置SRLB标签范围，最小值为100，最大值为200，则输入以下命令：ZXROSNG(config-lm)#repare new-label-range 100 200ZXROSNG(config-lm)#srlb-label-range 100 200删除配置的SRLB标签范围：ZXROSNG(config-lm)#no srlb-label-range
相关命令 : 
prepare new-label-rangeshow mpls label manage
## static-label-range 

static-label-range 
命令功能 : 
该命令工作于标签管理模式下，用于配置静态标签范围。标签管理模块处于共享模式时（由产品规格确定），可通过该命令实现各标签段的新建、扩大、缩小、删除。
命令模式 : 
 标签管理模式  
命令默认权限级别 : 
15 
命令格式 : 
static-label-range 
  ＜label-min 
＞ ＜label-max 
＞
no static-label-range 
  ＜label-min 
＞
				
命令参数解释 : 
参数|描述
---|---
＜label-min＞|用于配置静态标签范围最小值。取值范围：标签范围大小16-1048575。默认值：由产品规格确定。
＜label-max＞|用于配置静态标签预备范围最大值。取值范围：标签范围大小16-1048575。默认值：由产品规格确定。
缺省 : 
缺省情况下，各标签范围使用产品规格的默认值。 
使用说明 : 
拥有管理员权限的操作员可以使用这条命令。    该标签范围不可超过全局标签值范围（由产品规格确定），若静态标签范围的锁定状态（由产品规格确定）取值为1时，表示其为锁定状态，该范围不可配置。    静态标签范围支持扩大，但是扩大只支持向后扩大，不支持向前扩大，必须新扩标签段中所有标签都空闲时（除静态标签占用之外）配置才能成功。 静态标签范围可以删除或缩小，但删除或缩小必须写盘重启才能生效。    对于标签共享模式:1）若要扩大静态标签范围，可以事先使用操作命令prepare new-label-range <label-min> <label-max>，为其准备标签资源，也可以不使用该prepare命令。若使用该命令，则其中<label-min>值为当前生效的静态范围最大值＋1。2）扩大静态范围时，若事先使用了prepare操作命令，则static-label-range <label-min> <label-max> 中<label-max>必须为之前执行prepare new-label-range <label-min> <label-max>命令中<label-max>，且静态范围立即生效。若事先未使用prepare操作命令，则可能出现该扩大静态范围配置延迟生效。3）若要新增静态标签范围，可以事先使用操作命令prepare new-label-range <label-min> <label-max>，为其准备标签资源，也可以不使用该prepare命令。4）新增静态范围时，若事先使用了prepare操作命令，则static-label-range <label-min> <label-max> 中的最小值、最大值必须与之前执行的prepare new-label-range <label-min> <label-max>命令相一致，且静态范围立即生效。若事先未使用prepare操作命令，则可能出现该新增静态范围配置延迟生效。       对于非共享模式，新增静态范围，扩大静态范围，直接使用本命令配置新范围即可。    该标签范围不可与Kompella标签范围相重叠。Kompella标签范围大小、静态标签范围大小、动态协议预留标签数量，三者之和不应超过全局标签范围大小（由产品规格确定）。    静态范围可以由之前版本中mpls label range  global ＜global-min-value＞ ＜global-max-value＞ static ＜static-min-value＞ ＜static-max-value＞ ldp ＜ldp-min-value＞ ＜ldp-max-value＞ pwe3 ＜pwe3-min-value＞ ＜pwe3-max-value＞ rsvp ＜rsvp-min-value＞ ＜rsvp-max-value＞ bgp ＜bgp-min-value＞ ＜bgp-max-value＞ bgpv6 ＜bgpv6-min-value＞ ＜bgpv6-max-value＞[kompella ＜kompella-min-value＞ ＜kompella-max-value＞] ac-label <ac-min-value> <ac-max-value>兼容加载而得到。    最多可以配置数量有产品规格确定。    使用no命令删除静态标签范围。
范例 : 
配置静态标签范围，最小值为100，最大值为200，则输入以下命令：ZXROSNG(config-lm)# static-label-range 100 200
相关命令 : 
show mpls label managempls label manageprepare new-label-range <label-min> <label-max> [cancel]
## style 

style 
命令功能 : 
采取一种新的LDP session的保活机制，每收到一个hello消息报文，将该hello所维护的session的保活时间复位。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
style 
 
no style 
命令参数解释 : 
					无
				 
缺省 : 
在缺省情况下，实例每收到一个LDP 的TCP 协议报文将session的保活计时器进行更新。 
使用说明 : 
使用场景配置该命令后，实例每收到一个LDP的PDU都会将计时器复位，包括TCP与UDP报文。
范例 : 
触发使用新的LDP session的保活机制：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#style
相关命令 : 
无 
## target 

target 
命令功能 : 
该命令配置非直连的IPv6本地传输地址，使用no命令删除。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
target 
 ipv6 
 transport-address 
 {interface 
 ＜interface-name 
＞|＜ipv6-address 
＞}
no target 
 ipv6 
 transport-address 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|指定接口的IPv6地址作为非直连hello消息通告的传输地址
＜ipv6-address＞|指定使用某个地址作为非直连hello消息通告的传输地址
缺省 : 
缺省情况下，LDP将router ID作为传输地址在hello消息中通告。 
使用说明 : 
使用场景配置非直连即target session，使用该命令配置传输地址，才能建立IPv6的target session。注意事项1、配置指定接口的IPv6地址作为传输地址时，优先获取接口的v6 global地址，不存在v6 global地址时，获取v6 linklocal地址。2、配置IPv6-address选项时，会清除interface-name选项配置；3、配置interface-name选项时，会清除IPv6-address选项配置。
范例 : 
使用1000::1作为传输地址，指定gei-0/1/0/1接口绑定地址作为传输地址：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target ipv6 transport-address 1000::1ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target ipv6 transport-address interface gei-0/1/0/1
相关命令 : 
show mpls ldp neighbor 
## target-session ipv6 

target-session ipv6 
命令功能 : 
配置非直连远端目标Session的IPv6地址，建立目标Session。使用no命令删除该Session。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
target-session ipv6 
  ＜ipv6-address 
＞ [{dod 
|local-router-id 
 ＜interface-name 
＞|holdtime 
 ＜holdtime 
＞|hello-interval 
 ＜target-interval-time 
＞|hello-holdtime 
 ＜target-holdtime 
＞|dual-stack 
 transport-connection 
 prefer 
 {ipv4 
|ipv6 
}}]
no target-session ipv6 
  ＜ipv6-address 
＞ [{dod 
|local-router-id 
|holdtime 
|hello-interval 
|hello-holdtime 
|dual-stack 
 transport-connection 
 prefer 
}]
				
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|远端邻居的IP地址，IPv6的地址
dod|下游请求标签分发模式
local-router-id|指定本地的router-id
＜interface-name＞|接口名称，最长31个字符，指定该接口的接口地址为Target会话的本地router-id
＜holdtime＞|指定维护的会话在收不到后续LDP消息的情况下的保持时间，范围：15–65535，单位：秒
＜target-interval-time＞|指定此接口发送hello消息的间隔，范围：1–65535，单位：秒
＜target-holdtime＞|指定与此接口相关的hello节点的保持时间，范围：1–65535，单位：秒
ipv4|指定此接口下的hello发送消息中携带双栈传输连接 IPv4优先参数
ipv6|指定此接口下的hello发送消息中携带双栈传输连接 IPv6优先参数
No参数|描述
---|---
holdtime|指定target-session 的会话保活时间。
hello-interval|指定此接口相关的hello 发送间隔。
hello-holdtime|指定此接口相关的hello保活时间。
prefer|指定此接口下的hello发送消息中携带双栈传输连接优先地址族参数
缺省 : 
无 
使用说明 : 
使用场景配置非直连远端目标Session的地址，建立目标Session。支持配置对端可选项local-router-id的配置，可指定与对端建立目标Session时使用该接口地址作为本地的router-id。后续操作1、支持配置维护的会话在收不到后续LDP消息的情况下的保持时间。2、指定发送hello消息的间隔。3、指定与此target-session ipv6配置相关的hello节点的保持时间。4、支持配置指定IPv6 target hello发送消息中携带双栈传输连接优先地址族参数。配置后只在路由器本地双栈情况下生效。默认双栈传输连接IPv4优先。
范例 : 
与router-id为1.1.1.1的路由器建立目标Session，支持配置本地的router-id作为与指定远端邻居建链时使用的router-id。：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session ipv6 10:10::0ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session ipv6 fe80::216:3eff:fe64:305使用接口gei-0/1/0/1的地址作为本地的router-id与对端建立目标会话。ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session ipv6 10:10::0 local-router-id gei-0/1/0/1配置维护的会话在收不到后续LDP消息的情况下的保持时间为100秒ZXROSNG(config-ldp-1)# target-session ipv6 10:10::0 holdtime 100配置发送hello消息的间隔为20秒ZXROSNG(config-ldp-1)# target-session ipv6 10:10::0 hello-interval 20配置与此target-session ipv6配置相关的hello节点的保持时间为80秒ZXROSNG(config-ldp-1)# target-session ipv6 10:10::0 hello-holdtime 80与router-id为1.1.1.1的路由器建立目标Session，支持配置IPv6 target hello发送消息中携带双栈传输连接IPv6优先参数ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session ipv6 10:10::0 dual-stack transport-connection prefer ipv6
相关命令 : 
show mpls ldp neighborLDP模式 discovery target-helloLDP模式 holdtime
## target-session 

target-session 
命令功能 : 
配置非直连远端目标Session的地址，建立目标Session。使用no命令删除该Session。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
target-session 
  ＜ip-address 
＞ [{dod 
|pw-only 
|update-source 
 {＜source-ip-address 
＞|interface 
 ＜interface-name 
＞}|local-router-id 
 ＜lcl-rid-interface-name 
＞|holdtime 
 ＜holdtime 
＞|hello-interval 
 ＜target-interval-time 
＞|hello-holdtime 
 ＜target-holdtime 
＞|dual-stack 
 transport-connection 
 prefer 
 {ipv4 
|ipv6 
}}]
no target-session 
  ＜ip-address 
＞ [{pw-only 
|dod 
|update-source 
|local-router-id 
|holdtime 
|hello-interval 
|hello-holdtime 
|dual-stack 
 transport-connection 
 prefer 
}]
				
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|远端邻居的IP地址，是IPV4的地址
dod|标签分发方式
pw-only|指定此target-sesson 仅应用于PW。
update-source|携带源地址
＜source-ip-address＞|Target hello携带的源地址
＜interface-name＞|接口名称，最长31个字符，Target hello使用接口地址作为源地址
local-router-id|指定本地的router-id
＜lcl-rid-interface-name＞|接口名称，最长31个字符，指定该接口的接口地址为Target会话的本地router-id
＜holdtime＞|指定维护的会话在收不到后续LDP消息的情况下的保持时间，范围：15–65535，单位：秒
＜target-interval-time＞|指定此接口发送hello消息的间隔，范围：1–65535，单位：秒
＜target-holdtime＞|指定与此接口相关的hello节点的保持时间，范围：1–65535，单位：秒
ipv4|指定此接口下的hello发送消息中携带双栈传输连接 IPv4优先参数
ipv6|指定此接口下的hello发送消息中携带双栈传输连接 IPv6优先参数
No参数|描述
---|---
holdtime|指定target-session 的会话保活时间。
hello-interval|指定此接口相关的hello 发送间隔。
hello-holdtime|指定此接口相关的hello保活时间。
prefer|指定此接口下的hello发送消息中携带双栈传输连接优先地址族参数
缺省 : 
无 
使用说明 : 
使用场景配置非直连远端目标Session的地址，建立目标Session。支持配置对端可选项update-source源地址的配置，可指定地址也可指定出接口作为update-source源地址，hello报文中将携带该源地址进行发送。支持配置对端可选项local-router-id的配置，可指定与对端建立目标Session时使用该接口地址作为本地的router-id。后续操作1、支持配置维护的会话在收不到后续LDP消息的情况下的保持时间。2、指定发送hello消息的间隔。3、指定与此target-session配置相关的hello节点的保持时间。4、支持配置远端目标会话只作为PW会话使用，生效后不进行LDP协议消息的交互。配置后仅对后续建立的会话生效。5、支持配置指定hello消息中携带双栈传输连接优先地址族参数。配置后只在路由器本地双栈情况下生效。默认双栈传输连接 IPv4优先。
范例 : 
与router-id为1.1.1.1的路由器建立目标Session：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session 1.1.1.1支持配置远端邻居的任意接口ip地址为对端地址，同时支持配置源地址作为hello报文中携带的源地址，支持配置本地的router-id作为与指定远端邻居建链时使用的router-id。与某接口地址为10.1.1.2的对端建立目标会话，同时使用接口地址10.1.1.1作为源地址发送hello消息。ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session 10.1.1.2 update-source 10.1.1.1与某接口地址为10.1.1.2的对端建立目标会话，同时使用gei-0/1/0/1接口作为源地址发送hello消息。ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session 10.1.1.2 update-source interface gei-0/1/0/1与10.1.1.2的对端建立目标会话，同时使用接口gei-0/1/0/1的地址作为本地的router-id与对端建立目标会话。ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session 10.1.1.2 local-router-id gei-0/1/0/1配置维护的会话在收不到后续LDP消息的情况下的保持时间为100秒ZXROSNG(config-ldp-1)# target-session 10.1.1.2 holdtime 100配置发送hello消息的间隔为20秒ZXROSNG(config-ldp-1)# target-session 10.1.1.2 hello-interval 20配置与此target-session ipv6配置相关的hello节点的保持时间为80秒ZXROSNG(config-ldp-1)# target-session 10.1.1.2 hello-holdtime 80与10.1.1.2的对端建立目标会话，该会话只作为PW会话使用。ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session 10.1.1.2 pw-only%Info 129: The sessions which are already up should be restarted to make this config take effect与10.1.1.2的对端建立目标会话，并配置此target hello发送消息中携带双栈传输连接 IPv6优先参数。ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)#target-session 10.1.1.2 dual-stack transport-connection prefer ipv6
相关命令 : 
show mpls ldp neighborLDP模式 discovery target-helloLDP模式 holdtime
## traffic-count-fec ipv6 

traffic-count-fec ipv6 
命令功能 : 
配置LDP实例需要进行IPv6 LSP性能统计的网段，使用no命令删除该功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
traffic-count-fec ipv6 
  ＜acl-name 
＞
no traffic-count-fec ipv6 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度为1-31个字符
缺省 : 
不开启。 
使用说明 : 
使用场景设置LDP实例下，需要进行ipv6 LSP性能统计的网段。注意事项网段通过设置ACL规则进行限制。
范例 : 
设置名为test-list的ACL，ACL规则为允许ipv6所有网段：ZXROSNG(config)#ipv6-access-list test-listZXROSNG(config-ipv4-acl)#rule 1 permit ipv6 any anyZXROSNG(config-ipv4-acl)#exit实例1下设置ACL名为test-list的LSP性能统计：ZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)traffic-count-fec ipv6 test-list
相关命令 : 
show mpls ldp traffic-count 
## traffic-count-fec 

traffic-count-fec 
命令功能 : 
配置LDP实例需要进行LSP性能统计的网段，使用no命令删除该功能。 
命令模式 : 
 LDP模式  
命令默认权限级别 : 
15 
命令格式 : 
traffic-count-fec 
  ＜acl-name 
＞
no traffic-count-fec 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|ACL名称，长度为1-31个字符
缺省 : 
不开启。 
使用说明 : 
使用场景该命令可以设置指定网段进行LSP的性能统计，通过设置ACL限制网段区间。
范例 : 
ZXROSNG(config)#ipv4-access-list test-listZXROSNG(config-ipv4-acl)#rule 1 permit 10.10.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#rule 2 permit 10.20.0.0 0.0.255.255ZXROSNG(config-ipv4-acl)#rule 3 deny anyZXROSNG(config-ipv4-acl)#exitZXROSNG(config)#mpls ldp instance 1ZXROSNG(config-ldp-1)traffic-count-fec test-list
相关命令 : 
show mpls ldp traffic-count 
## wait-time 

wait-time 
命令功能 : 
配置等待新LSP建立的时间。 
命令模式 : 
 MLDP-MBB模式  
命令默认权限级别 : 
15 
命令格式 : 
wait-time 
  ＜wait-time 
＞
no wait-time 
命令参数解释 : 
参数|描述
---|---
＜wait-time＞|等待新LSP建立的时间
缺省 : 
缺省情况下，等待时间为5秒。 
使用说明 : 
使用场景当MLDP使能了MBB功能后，可以用wait-time命令配置等待新LSP建立的时间
范例 : 
路由器上配置MBB等待时间：ZXROSNG(config)#mpls ldp instance 1  ZXROSNG(config-ldp-1)#mldpZXROSNG(config-ldp-1-mldp)#capability mbb ZXROSNG(config-ldp-1-mldp-mbb)# wait-time 10
相关命令 : 
show running-config 
# MPLS OAM配置命令 
## adapt 

adapt 
命令功能 : 
修改静态隧道lsp-id的值 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
adapt 
 lsp-id 
 ＜Lsp_ID 
＞
命令参数解释 : 
参数|描述
---|---
＜Lsp_ID＞|作用：配置静态隧道lsp-id的适配值。范围：0-1。默认值：1。
缺省 : 
lsp-id 的缺省值为1 
使用说明 : 
对接时，在配置检测实例之前，需要先行配置该lspid的适配值。rosng30版本，默认值是1 
范例 : 
ZXROSNG(config-mpls-oam)#adapt lsp-id 0ZXROSNG(config-mpls-oam)#adapt lsp-id 1
相关命令 : 
mpls oam 
## clear mpls oam statistics local_tunnel 

clear mpls oam statistics local_tunnel 
命令功能 : 
头结点上，清除本地指定隧道下MPLS-OAM报文统计计数 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear mpls oam statistics local_tunnel 
  {＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ {all 
|cv 
|ffd 
|bdi 
|fdi 
}|{all 
|cv 
|ffd 
|bdi 
|fdi 
}}
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|作用：实例的tunnelId参数。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：实例的ingressId参数。范围：无。默认值：无。
all|作用：清除所有节点的所有类型报文统计计数。范围：无。默认值：无。
cv|作用：清除所有节点的CV类型报文统计计数。范围：无。默认值：无。
ffd|作用：清除所有节点的FFD类型报文统计计数。范围：无。默认值：无。
bdi|作用：清除所有节点的BDI类型报文统计计数。范围：无。默认值：无。
fdi|作用：清除所有节点的FDI类型报文统计计数。范围：无。默认值：无。
all|作用：清除所有节点的所有类型报文统计计数。范围：无。默认值：无。
cv|作用：清除所有节点的CV类型报文统计计数。范围：无。默认值：无。
ffd|作用：清除所有节点的FFD类型报文统计计数。范围：无。默认值：无。
bdi|作用：清除所有节点的BDI类型报文统计计数。范围：无。默认值：无。
fdi|作用：清除所有节点的FDI类型报文统计计数。范围：无。默认值：无。
缺省 : 
无 
使用说明 : 
此命令头结点适用，用于清除本地指定隧道下MPLS-OAM报文统计信息，便于观察报文收发是否正常 
范例 : 
ZXROSNG# clear mpls oam statistics local_tunnel 1 ingress 1.2.3.4 allZXROSNG(config-mpls-oam)#show mpls oam statistics local_tunnel all TunnelId: 1     cv : 0     ffd: 0     bdi: 0     fdi: 0
相关命令 : 
无 
## clear mpls oam statistics remote_tunnel 

clear mpls oam statistics remote_tunnel 
命令功能 : 
头结点上，清除指定远端隧道下MPLS-OAM报文统计计数  
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear mpls oam statistics remote_tunnel 
  {＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ {all 
|cv 
|ffd 
|bdi 
|fdi 
}|{all 
|cv 
|ffd 
|bdi 
|fdi 
}}
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|作用：实例的tunnelId参数。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：实例的ingressId参数。范围：无。默认值：无。
all|作用：清除所有节点的所有类型报文统计计数。范围：无。默认值：无。
cv|作用：清除所有节点的CV类型报文统计计数。范围：无。默认值：无。
ffd|作用：清除所有节点的FFD类型报文统计计数。范围：无。默认值：无。
bdi|作用：清除所有节点的BDI类型报文统计计数。范围：无。默认值：无。
fdi|作用：清除所有节点的FDI类型报文统计计数。范围：无。默认值：无。
all|作用：清除所有节点的所有类型报文统计计数。范围：无。默认值：无。
cv|作用：清除所有节点的CV类型报文统计计数。范围：无。默认值：无。
ffd|作用：清除所有节点的FFD类型报文统计计数。范围：无。默认值：无。
bdi|作用：清除所有节点的BDI类型报文统计计数。范围：无。默认值：无。
fdi|作用：清除所有节点的FDI类型报文统计计数。范围：无。默认值：无。
缺省 : 
无 
使用说明 : 
此命令头结点适用，用于清除远端指定隧道下MPLS-OAM报文统计信息，便于观察报文收发是否正常 
范例 : 
ZXROSNG# clear mpls oam statistics remote_tunnel 1 ingress 1.2.3.4 allZXROSNG(config-mpls-oam)#show mpls oam statistics remote_tunnel all TunnelId: 1 ingressId ： 1.2.3.4     cv : 0     ffd: 0     bdi: 0     fdi: 0
相关命令 : 
无 
## debug mpls oam all 

debug mpls oam all 
命令功能 : 
开启MPLS-OAM调试功能开关，打印所有节点的所有类型的报文 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls oam all 
 
no debug mpls oam all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令用于打开MPLS-OAM调试开关功能，可以观察平台收发包的情况：例如慢包检测（CV检测）时，头结点、中间节点和尾节点平台收发的CV、BDI、FDI；快包检测（FFD检测）时，中间节点和尾节点FDI收发情况  
范例 : 
ZXROSNG#debug mpls oam all MPLSOAM debugging all is onZXROSNG#show debug mplsoam MPLS-OAM:  MPLS-OAM CV  debugging is on  MPLS-OAM BDI debugging is on  MPLS-OAM FDI debugging is onZXROSNG#
相关命令 : 
无 
## debug mpls oam bdi 

debug mpls oam bdi 
命令功能 : 
开启MPLS-OAM调试BDI报文的功能开关 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls oam bdi 
 
no debug mpls oam bdi 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令用于打开MPLS-OAM调试开关功能，可以观察平台收发BDI报文的情况。 
范例 : 
ZXROSNG#debug mpls oam bdiMPLSOAM debugging bdi is onZXROSNG#sho debug mpls-oamMPLS-OAM: MPLS-OAM BDI debugging is onZXROSNG#
相关命令 : 
无 
## debug mpls oam cv 

debug mpls oam cv 
命令功能 : 
开启MPLS-OAM调试CV报文功能开关 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls oam cv 
 
no debug mpls oam cv 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令用于打开MPLS-OAM调试CV开关功能，可以观察平台收发CV报文的情况。 
范例 : 
ZXROSNG#debug mpls oam cvMPLSOAM debugging cv is onZXROSNG#sho debug mpls-oamMPLS-OAM: MPLS-OAM CV debugging is onZXROSNG#
相关命令 : 
无 
## debug mpls oam fdi 

debug mpls oam fdi 
命令功能 : 
开启MPLS-OAM调试FDI报文功能开关 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls oam fdi 
 
no debug mpls oam fdi 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令用于打开MPLS-OAM调试FDI开关功能，可以观察平台收发FDI报文的情况。 
范例 : 
ZXROSNG#debug mpls oam fdiMPLSOAM debugging fdi is onZXROSNG#sho debug mpls-oamMPLS-OAM: MPLS-OAM FDI debugging is onZXROSNG#
相关命令 : 
无 
## debug mpls oam te-tunnel 

debug mpls oam te-tunnel 
命令功能 : 
按指定测试实例显示相关报文的debug信息。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls oam te-tunnel 
  ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ {all 
|cv 
|bdi 
|fdi 
}
no debug mpls oam te-tunnel 
  ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ {all 
|cv 
|bdi 
|fdi 
}
				
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|作用：关闭该隧道ID的debug开关。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：关闭该Ingress ID的debug开关。范围：无。默认值：无。
all|作用：关闭所有类型的报文打印。范围：无。默认值：无。
cv|作用：关闭cv报文类型的打印。范围：无。默认值：无。
bdi|作用：关闭bdi报文类型的打印。范围：无。默认值：无。
fdi|作用：关闭 fdi报文类型的打印。范围：无。默认值：无。
缺省 : 
无 
使用说明 : 
该命令可以打开或者关闭指定测试实例和指定报文类型的debug开关。使用该命令前要保证指定的测试实例已经存在。
范例 : 
ZXROSNG#debug mpls oam te-tunnel 1 ingress 1.1.1.1 allZXROSNG#ZXR10 PFU-0/1/0 2012-5-11 03:26:38 MPLS OAM TunnelId = 1, LspId = 1, IngressId = 1.1.1.1 Send CV Packet:01 00 00 00 00 00 00 00 00 00 00 00 00 00 FF FF 01 01 01 01 00 01 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
相关命令 : 
debug mpls oam  
## egress 

egress 
命令功能 : 
尾节点开启MPLS-OAM检测功能，配置该命令后在隧道尾节点开始接收MPLS-OAM检测报文 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
egress 
 te_tunnel 
 ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ backward-tunnel 
 ＜back-forward-tunnel-id 
＞ [share 
] type 
 {cv 
|ffd 
 frequence 
 {3.3 
|10 
|20 
|50 
|100 
|200 
|500 
}}
no egress 
 te_tunnel 
 ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|作用：删除实例的tunnel Id参数。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：删除实例的ingress Id参数。范围：无。默认值：无。
＜back-forward-tunnel-id＞|作用：实例的反向隧道tunnel Id参数。范围：1-$#100794374#$。默认值：无。
share|作用：以共享方式使用反向隧道。范围：无。默认值：无。
cv|作用：配置检测报文类型为CV（慢包检测）。范围：无。默认值：无。
ffd|作用：配置检测报文类型为FFD（快包检测）。范围：无。默认值：无。
3.3|作用：快包检测的报文频率为3.3ms。范围：无。默认值：无。
10|作用：快包检测的报文频率为10ms。范围：无。默认值：无。
20|作用：快包检测的报文频率为20ms。范围：无。默认值：无。
50|作用：快包检测的报文频率为50ms。范围：无。默认值：无。
100|作用：快包检测的报文频率为100ms。范围：无。默认值：无。
200|作用：快包检测的报文频率为200ms。范围：无。默认值：无。
500|作用：快包检测的报文频率为500ms。范围：无。默认值：无。
缺省 : 
无 
使用说明 : 
此命令用于尾节点开启MPLS-OAM检测功能，在隧道尾节点开始接收MPLS-OAM检测报文 ，需要在MPLS-OAM配置模式下进行使用。使用该命令前，要保证使用的隧道接口ID存在。反向隧道若不是共享模式，则该隧道ID只能被一个远端节点实例作为反向隧道使用，其他实例不可使用。反向隧道若是共享模式，则该隧道ID可以被多个远端节点实例作为共享反向隧道使用。
范例 : 
ZXROSNG(config_mpls_oam)#egress te_tunnel 3 ingress 5.6.7.8 backward_tunnel 2 share type ffd frequence 3.3 ZXROSNG(config_mpls_oam)#no egress te_tunnel 3 ingress 5.6.7.8 
相关命令 : 
mpls oam 
## local 

local 
命令功能 : 
配置MPLS-OAM头结点的实例信息，当需要配置头结点实例时使用该命令 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
local 
 te_tunnel 
 ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞
no local 
 te_tunnel 
 ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|作用：删除的MPLS-OAM实例的tunnelId信息。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：删除MPLS-OAM实例的ingerssId信息。范围：无。默认值：无。
缺省 : 
无 
使用说明 : 
命令执行后，进入MPLS-OAM隧道接口配置模式，可以进行MPLS-OAM实例检测开启和关闭配置，需要在MPLS-OAM配置模式下使用此命令。使用该命令前，要保证使用的隧道接口ID存在。
范例 : 
ZXROSNG(config)#mpls oamZXROSNG(config-mpls-oam)#local te_tunnel 1 ingress 1.2.3.4 ZXROSNG(config-mpls-oam-if)#
相关命令 : 
mpls oam 
## mpls oam enable 

mpls oam enable 
命令功能 : 
头结点开启MPLS-OAM检测命令，开始发送检测报文，使用no命令删除该命令配置  
命令模式 : 
 MPLSOAM隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls oam enable 
 
no mpls oam enable 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
配置隧道MPLS-OAM检测开启命令，命令配置成功后开始发送检测报文。使用该命令前，需要先保证实例的检测类型已经配置。
范例 : 
ZXROSNG(config)#mpls oamZXROSNG(config-mpls-oam)#local te_tunnel 1 ingress 1.2.3.4ZXROSNG(config-mpls-oam-if)#mpls oam enable ZXROSNG(config-mpls-oam-if)#
ZXROSNG(config-mpls-oam-if)#no mpls oam enable ZXROSNG(config-mpls-oam-if)#
相关命令 : 
mpls oamLocal
## mpls oam 

mpls oam 
命令功能 : 
开启MPLS-OAM全局开关，然后可以进行MPLS-AOM相关配置 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls oam 
 
no mpls oam 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
开启MPLS-OAM全局开关，然后可以进行MPLS-AOM相关配置 
范例 : 
ZXROSNG(config)#mpls oam ZXROSNG(config-mpls-oam)#
相关命令 : 
无 
## show debug mpls-oam 

show debug mpls-oam 
命令功能 : 
该命令用来显示MPLS-OAM的debug开关状态 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug mpls-oam 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
此命令用于显示MPLS-OAM功能debug打开或关闭信息，当需要查看debug开关情况时使用该命令 
范例 : 
打开debug开关后，show debug信息：ZXROSNG#show debug mpls-oamMPLSOAM:MPLS-OAM:MPLS-OAM CV  debugging is onMPLS-OAM BDI debugging is onMPLS-OAM FDI debugging is onZXROSNG#
相关命令 : 
debug mpls oam 
## show mpls oam 

show mpls oam 
命令功能 : 
该命令用来显示MPLS-OAM的实例信息，如配置信息、统计信息等 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls oam 
  {information 
 {local_tunnel 
|remote_tunnel 
} [＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞]|statistics 
 {local_tunnel 
 {＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ {all 
|cv 
|ffd 
|bdi 
|fdi 
}|{all 
|cv 
|ffd 
|bdi 
|fdi 
}}|remote_tunnel 
 {＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ {all 
|cv 
|ffd 
|bdi 
|fdi 
}|{all 
|cv 
|ffd 
|bdi 
|fdi 
}}}} 
命令参数解释 : 
参数|描述
---|---
information|作用：显示MPLS-OAM的节点信息。范围：无。默认值：无。
local_tunnel|作用：头结点选用参数，用来显示本地的MPLS-OAM实例信息。范围：无。默认值：无。
remote_tunnel|作用：非头结点选用参数，用来显示MPLS-OAM远端实例信息。范围：无。默认值：无。
＜tunnel-id＞|作用：隧道ID。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：入节点ID。范围：无。默认值：无。
statistics|作用：显示MPLS-OAM实例的统计信息。范围：无。默认值：无。
local_tunnel|作用：头结点选用参数，用来显示本地的MPLS-OAM实例信息。范围：无。默认值：无。
＜tunnel-id＞|作用：隧道ID。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：入节点ID。范围：无。默认值：无。
all|作用：显示所有远端结点的所有类型报文信息。范围：无。默认值：无。
cv|作用：显示所有远端结点的CV类型报文信息。范围：无。默认值：无。
ffd|作用：显示所有远端结点的FFD类型报文信息。范围：无。默认值：无。
bdi|作用：显示所有远端结点的BDI类型报文信息。范围：无。默认值：无。
fdi|作用：显示所有远端结点的FDI类型报文信息。范围：无。默认值：无。
all|作用：显示所有远端结点的所有类型报文信息。范围：无。默认值：无。
cv|作用：显示所有远端结点的CV类型报文信息。范围：无。默认值：无。
ffd|作用：显示所有远端结点的FFD类型报文信息。范围：无。默认值：无。
bdi|作用：显示所有远端结点的BDI类型报文信息。范围：无。默认值：无。
fdi|作用：显示所有远端结点的FDI类型报文信息。范围：无。默认值：无。
remote_tunnel|作用：非头结点选用参数，用来显示MPLS-OAM远端实例信息。范围：无。默认值：无。
＜tunnel-id＞|作用：隧道ID。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：入节点ID。范围：无。默认值：无。
all|作用：显示所有远端结点的所有类型报文信息。范围：无。默认值：无。
cv|作用：显示所有远端结点的CV类型报文信息。范围：无。默认值：无。
ffd|作用：显示所有远端结点的FFD类型报文信息。范围：无。默认值：无。
bdi|作用：显示所有远端结点的BDI类型报文信息。范围：无。默认值：无。
fdi|作用：显示所有远端结点的FDI类型报文信息。范围：无。默认值：无。
all|作用：显示所有远端结点的所有类型报文信息。范围：无。默认值：无。
cv|作用：显示所有远端结点的CV类型报文信息。范围：无。默认值：无。
ffd|作用：显示所有远端结点的FFD类型报文信息。范围：无。默认值：无。
bdi|作用：显示所有远端结点的BDI类型报文信息。范围：无。默认值：无。
fdi|作用：显示所有远端结点的FDI类型报文信息。范围：无。默认值：无。
缺省 : 
无 
使用说明 : 
此命令用于显示头结点MPLS-OAM实例详细信息，可以显示出所有本地隧道下的MPLS-OAM配置相关信息或者实例的统计信息。显示实例统计信息前，请先配置好实例信息，并且用statistc命令打开统计开关。 
范例 : 
show指定头结点的实例信息：ZXROSNG#show mpls oam informations local_tunnel 1 ingress 1.1.1.1TunnelId    : 1LspId       : 1IngressId   : 1.1.1.1Node-Role   : HeadAscription  : YesPacket      : CV, Priority: 7BkTunnel    : 0Share       : NoEnable      : YesTrans-State : OK(hex:0000)Detect-State: OK(hex:0000)Statistic   : AllDebug:      : AllShow所有头结点的实例信息：ZXROSNG(config)#show mpls oam informations local_tunnelLocal tunnel Num : 1State init Num : 0State up Num   : 1State down Num : 0TunnelId    : 1LspId       : 0IngressId   : 1.2.3.4Node-Role   : HeadAscription  : YesPacket      : FFD, Frequencey: 200, Priority: 5BkTunnel    : 0Share       : NoEnable      : YesTrans-State : 0(hex)Detect-State: 0(hex)开启所有节点的统计开关后，show所有头结点的统计信息：ZXROSNG(config)#mpls oamZXROSNG(config-mpls-oam)#statistics allZXROSNG(config-mpls-oam)#show mpls oam statistics local_tunnel allTunnelId: 1cv : 15ffd: 0bdi: 0fdi: 0
相关命令 : 
statistics 
## statistics all 

statistics all 
命令功能 : 
打开全部MPLS-OAM实例的所有报文类型的统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics all 
 
no statistics all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开所有本地和远端的MPLS-OAM实例所有报文的统计开关，开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam)#statistics allZXROSNG(config-mpls-oam)#show mpls oam statistics local_tunnel all TunnelId: 1     cv  : 10     bdi : 0     fdi : 0     ffd : 0ZXROSNG(config-mpls-oam)#show mpls oam statistics remote_tunnel cv Tunnelid: 20, Ingressid: 1.5.6.7     cv  : 10Tunnelid: 2, Ingressid: 1.5.6.7     cv  : 15
相关命令 : 
mpls oam 
## statistics all 

statistics all 
命令功能 : 
打开指定MPLS-OAM头结点的全部报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics all 
 
no statistics all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于打开指定MPLS-OAM头结点的全部报文统计开关，开关打开后开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam-if)#statistics allZXROSNG(config-mpls-oam-if)#show mpls oam statistics local_tunnel all TunnelId: 1     bdi : 10     cv  : 0     fdi : 0     ffd : 0ZXROSNG(config-mpls-oam-if)#show mpls oam statistics remote_tunnel all Tunnelid: 20, Ingressid: 1.5.6.7     bdi : 10     cv  : 0     fdi : 0     ffd : 0Tunnelid: 2, Ingressid: 1.5.6.7     bdi : 10     cv  : 0     fdi : 0     ffd : 0
相关命令 : 
mpls oamlocal
## statistics bdi 

statistics bdi 
命令功能 : 
打开全部MPLS-OAM实例的BDI报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics bdi 
 
no statistics bdi 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开所有本地和远端MPLS-OAM实例的BDI报文统计开关，开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam)#statistics bdiZXROSNG(config-mpls-oam)#show mpls oam statistics local_tunnel bdi TunnelId: 1     bdi : 10ZXROSNG(config-mpls-oam)#show mpls oam statistics remote_tunnel bdi Tunnelid: 20, Ingressid: 1.5.6.7     bdi : 10Tunnelid: 2, Ingressid: 1.5.6.7     bdi : 10
相关命令 : 
mpls oam 
## statistics bdi 

statistics bdi 
命令功能 : 
打开指定MPLS-OAM头结点的BDI报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics bdi 
 
no statistics bdi 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于打开指定MPLS-OAM头结点的BDI报文统计开关，开关打开后开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam-if)#statistics bdiZXROSNG(config-mpls-oam-if)#show mpls oam statistics local_tunnel bdi TunnelId: 1     bdi  : 10ZXROSNG(config-mpls-oam-if)#show mpls oam statistics remote_tunnel bdi Tunnelid: 20, Ingressid: 1.5.6.7     bdi  : 10Tunnelid: 2, Ingressid: 1.5.6.7     bdi  : 5
相关命令 : 
mpls oamlocal
## statistics cv 

statistics cv 
命令功能 : 
打开全部MPLS-OAM实例的CV报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics cv 
 
no statistics cv 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开所有本地和远端的MPLS-OAM实例的CV报文统计开关，开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam)#statistics cvZXROSNG(config-mpls-oam)#show mpls oam statistics local_tunnel cv TunnelId: 1     cv : 10ZXROSNG(config-mpls-oam)#show mpls oam statistics remote_tunnel cv Tunnelid: 20, Ingressid: 1.5.6.7     cv : 10Tunnelid: 2, Ingressid: 1.5.6.7     cv : 10
相关命令 : 
mpls oam 
## statistics cv 

statistics cv 
命令功能 : 
打开指定MPLS-OAM头结点的CV报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics cv 
 
no statistics cv 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于打开指定MPLS-OAM头结点的CV报文统计开关，开关打开后开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam-if)#statistics cvZXROSNG(config-mpls-oam-if)#show mpls oam statistics local_tunnel cv TunnelId: 1     cv  : 10ZXROSNG(config-mpls-oam-if)#show mpls oam statistics remote_tunnel cv Tunnelid: 20, Ingressid: 1.5.6.7     cv  : 10Tunnelid: 2, Ingressid: 1.5.6.7     cv  : 5
相关命令 : 
mpls oamlocal
## statistics fdi 

statistics fdi 
命令功能 : 
打开全部MPLS-OAM实例的FDI报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics fdi 
 
no statistics fdi 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开所有本地和远端MPLS-OAM实例的FDI报文统计开关，开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam)#statistics fdiZXROSNG(config-mpls-oam)#show mpls oam statistics local_tunnel fdi TunnelId: 1     fdi : 10ZXROSNG(config-mpls-oam)#show mpls oam statistics remote_tunnel fdi Tunnelid: 20, Ingressid: 1.5.6.7     fdi : 10Tunnelid: 2, Ingressid: 1.5.6.7     fdi : 10
相关命令 : 
mpls oam 
## statistics fdi 

statistics fdi 
命令功能 : 
打开指定MPLS-OAM头结点的FDI报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics fdi 
 
no statistics fdi 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于打开指定MPLS-OAM头结点的FDI报文统计开关，开关打开后开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam-if)#statistics fdiZXROSNG(config-mpls-oam-if)#show mpls oam statistics local_tunnel fdi TunnelId: 1     fdi  : 10ZXROSNG(config-mpls-oam-if)#show mpls oam statistics remote_tunnel fdiTunnelid: 20, Ingressid: 1.5.6.7     fdi  : 10Tunnelid: 2, Ingressid: 1.5.6.7     fdi  : 5
相关命令 : 
mpls oamlocal
## statistics ffd 

statistics ffd 
命令功能 : 
打开全部MPLS-OAM实例的FFD报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics ffd 
 
no statistics ffd 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
打开所有本地和远端MPLS-OAM实例的FFD报文统计开关，开始对报文进行统计计数，报文计数情况每5s更新一次
范例 : 
ZXROSNG(config-mpls-oam)#statistics ffdZXROSNG(config-mpls-oam)#show mpls oam statistics local_tunnel ffd TunnelId: 1     ffd : 100ZXROSNG(config-mpls-oam)#show mpls oam statistics remote_tunnel ffd Tunnelid: 20, Ingressid: 1.5.6.7     ffd : 100Tunnelid: 2, Ingressid: 1.5.6.7     ffd : 100
相关命令 : 
mpls oam 
## statistics ffd 

statistics ffd 
命令功能 : 
打开指定MPLS-OAM头结点的FFD报文统计开关，使用no命令清除该配置 
命令模式 : 
 MPLSOAM隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics ffd 
 
no statistics ffd 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
该命令用于打开指定MPLS-OAM头结点的FFD报文统计开关，开关打开后开始对报文进行统计计数，报文计数情况每5s更新一次
范例 : 
ZXROSNG(config-mpls-oam-if)#statistics ffdZXROSNG(config-mpls-oam-if)#show mpls oam statistics local_tunnel ffdTunnelId: 1     ffd  : 100ZXROSNG(config-mpls-oam-if)#show mpls oam statistics remote_tunnel ffdTunnelid: 20, Ingressid: 1.5.6.7     ffd  : 100Tunnelid: 2, Ingressid: 1.5.6.7     ffd  : 5
相关命令 : 
mpls oamlocal
## statistics 

statistics 
命令功能 : 
打开指定的MPLS-OAM远端实例的报文统计功能，使用no命令清除该配置 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics 
 remote_tunnel 
 ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ {all 
|cv 
|ffd 
|bdi 
|fdi 
}
no statistics 
 remote_tunnel 
 ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ {all 
|cv 
|ffd 
|bdi 
|fdi 
}
				
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|作用：删除实例的tunnelId参数。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：删除实例的ingressId参数。范围：无。默认值：无。
all|作用：统计所有类型报文。范围：无。默认值：无。
cv|作用：统计CV类型报文。范围：无。默认值：无。
ffd|作用：统计FFD类型报文。范围：无。默认值：无。
bdi|作用：统计BDI类型报文。范围：无。默认值：无。
fdi|作用：统计FDI类型报文。范围：无。默认值：无。
缺省 : 
无 
使用说明 : 
该命令用于打开指定MPLS-OAM远端结点的全部报文或者部分报文统计开关，开关打开后开始对报文进行统计计数，报文计数情况每5s更新一次 
范例 : 
ZXROSNG(config-mpls-oam)#statistics remote_tunnel 3 ingress 5.6.7.8 allZXROSNG(config-mpls-oam)#show mpls oam statistics remote_tunnel 3 ingress 5.6.7.8 allTunnelid: 3, Ingressid:  5.6.7.8     cv : 0     ffd: 100     bdi: 0     fdi: 0
相关命令 : 
mpls oam
## transit 

transit 
命令功能 : 
中间节点开启MPLS-OAM检测功能，配置该命令后在隧道中间节点开始传递MPLS-OAM检测报文 
命令模式 : 
 MPLSOAM模式  
命令默认权限级别 : 
15 
命令格式 : 
transit 
 te_tunnel 
 ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞ backward-tunnel 
 ＜back-forward-tunnel-id 
＞ [share 
] type 
 {cv 
|ffd 
 frequence 
 {3.3 
|10 
|20 
|50 
|100 
|200 
|500 
}}
no transit 
 te_tunnel 
 ＜tunnel-id 
＞ ingress 
 ＜ip-address 
＞
				
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|作用：删除实例的tunnel Id参数。范围：1-$#100794374#$。默认值：无。
＜ip-address＞|作用：删除实例的ingress Id参数。范围：无。默认值：无。
＜back-forward-tunnel-id＞|作用：配置实例反向隧道的tunnelId参数。范围：1-$#100794374#$。默认值：无。
share|作用：以共享方式使用反向隧道。范围：无。默认值：无。
cv|作用：配置检测报文类型为CV（慢包检测）。范围：无。默认值：无。
ffd|作用：配置检测报文类型为FFD（快包检测）。范围：无。默认值：无。
3.3|作用：快包检测的报文频率为3.3ms。范围：无。默认值：无。
10|作用：快包检测的报文频率为10ms。范围：无。默认值：无。
20|作用：快包检测的报文频率为20ms。范围：无。默认值：无。
50|作用：快包检测的报文频率为50ms。范围：无。默认值：无。
100|作用：快包检测的报文频率为100ms。范围：无。默认值：无。
200|作用：快包检测的报文频率为200ms。范围：无。默认值：无。
500|作用：快包检测的报文频率为500ms。范围：无。默认值：无。
缺省 : 
无 
使用说明 : 
此命令用于中间节点开启MPLS-OAM检测功能，在隧道中间节点开始传递MPLS-OAM检测报文 ，需要在MPLS-OAM配置模式下进行使用。使用该命令前，要保证使用的隧道接口ID存在。反向隧道若不是共享模式，则该隧道ID只能被一个远端节点实例作为反向隧道使用，其他实例不可使用。反向隧道若是共享模式，则该隧道ID可以被多个远端节点实例作为共享反向隧道使用。
范例 : 
ZXROSNG(config_mpls_oam)#transit te_tunnel 3 ingress 5.6.7.8 backward_tunnel 2 share type ffd frequence 3.3 ZXROSNG(config_mpls_oam)#no transit te_tunnel 3 ingress 5.6.7.8 
相关命令 : 
mpls oam 
## type 

type 
命令功能 : 
配置MPLS-OAM功能检测报文的类型和优先级，头结点需要配置报文类型和优先级时使用该命令，使用no命令清除该配置 
命令模式 : 
 MPLSOAM隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
type 
  {cv 
|ffd 
 frequence 
 {3.3 
|10 
|20 
|50 
|100 
|200 
|500 
}} [exp 
 ＜priority 
＞]
no type 
命令参数解释 : 
参数|描述
---|---
cv|作用：配置检测报文类型为CV（慢包检测）。范围：无。默认值：无。
ffd|作用：配置检测报文类型为FFD（快包检测）。范围：无。默认值：无。
3.3|作用：快包检测的报文频率为3.3ms。范围：无。默认值：无。
10|作用：快包检测的报文频率为10ms。范围：无。默认值：无。
20|作用：快包检测的报文频率为20ms。范围：无。默认值：无。
50|作用：快包检测的报文频率为50ms。范围：无。默认值：无。
100|作用：快包检测的报文频率为100ms。范围：无。默认值：无。
200|作用：快包检测的报文频率为200ms。范围：无。默认值：无。
500|作用：快包检测的报文频率为500ms。范围：无。默认值：无。
＜priority＞|作用：配置检测报文优先级。范围：0-7。默认值：0。
缺省 : 
exp的缺省值是0 
使用说明 : 
此命令用于配置MPLS-OAM检测报文的类型和优先级，命令需要在MPLS OAM 的隧道模式下使用。该命令需要在MPLS-OAM实例未使能条件下配置，如果实例已经使能过，需要去使能之后再配置。 
范例 : 
ZXROSNG(config-mpls-oam)#local te_tunnel 1 ingress 1.2.3.4ZXROSNG(config-mpls-oam-te_tunnel-1)#type ffd frequence 20  exp 2ZXROSNG(config-mpls-oam-te_tunnel-1)#mpls oam enableZXROSNG(config-mpls-oam-te_tunnel-1)#show mpls oam informations local_tunnel TunnelId    : 1LspId       : 0IngressId   : 1.2.3.4Node-Role   : HeadAscription  : YesPacket      : FFD, Frequencey: 20, Priority: 2BkTunnel    : 0Share       : NoEnable      : YesTrans-State : 0(hex)Detect-State: 0(hex)
相关命令 : 
mpls oamlocal
# MPLS TE配置命令 
## advertise administrative-weight implicit-ability 

advertise administrative-weight implicit-ability 
命令功能 : 
全局控制开关，控制TE metric TLV是否发送 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
advertise administrative-weight implicit-ability 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启metric_tlv默认发送功能
disable|关闭metric_tlv默认发送功能
缺省 : 
该功能默认开启 
使用说明 : 
该功能默认开启，如果其他设备默认不发送TE metric TLV，对接发送算路和预期不一致，需要关闭这个开关 
范例 : 
ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)# advertise administrative-weight implicit-ability disable
相关命令 : 
无 
## advertise explicit-null 

advertise explicit-null 
命令功能 : 
配置MPLS TE倒数第二跳标签显示空功能，no命令关闭显示空功能。
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
advertise explicit-null 
 
no advertise explicit-null 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
倒数第二跳标签默认为隐式空，配置显示空功能后执行no命令恢复成隐式空
范例 : 
ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#advertise explicit-null 
相关命令 : 
无 
## advertise none-null 

advertise none-null 
命令功能 : 
配置MPLS TE倒数第二跳标签非空功能，no命令关闭显示空功能。
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
advertise none-null 
 
no advertise none-null 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
倒数第二跳标签默认为隐式空，配置显示空功能后执行no命令恢复成隐式空。
范例 : 
ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#advertise none-null
相关命令 : 
无 
## associated-tunnel 

associated-tunnel 
命令功能 : 
使能静态隧道的关联双向功能，用no命令关闭该功能。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
associated-tunnel 
  ＜associated tnnlid 
＞
no associated-tunnel 
命令参数解释 : 
参数|描述
---|---
＜associated tnnlid＞|头节点隧道关联的尾节点接入隧道ID，范围：$#100794390#$~$#100794387#$
缺省 : 
无 
使用说明 : 
1.只有头节点单向隧道可以配置关联双向隧道；2.配置关联的静态隧道必须存在，且必须是尾节点单向静态隧道；3.配置关联的尾节点静态隧道的ingress的值必须和使能关联双向的头节点静态隧道的egress一致； 4.配置关联的尾节点静态隧道不能配置0,3入标签；5.删除或修改尾节点静态隧道时需要检查该隧道是否已被头节点静态隧道关联，如果被关联，则不允许删除或修改。
范例 : 
使能静态隧道关联双向功能，配置关联的尾节点接入隧道ID为60101ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel102ZXROSNG(config-mpls-te-static-te_tunnel102)#associated-tunnel 60101去使能静态隧道关联双向功能ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel102ZXROSNG(config-mpls-te-static-te_tunnel102)#no associated-tunnel
相关命令 : 
show mpls traffic-eng static | include Associated Bidirect  
## autoroute announce 

autoroute announce 
命令功能 : 
使能MPLS自动路由功能，使用no命令关闭该功能。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
autoroute announce 
 
no autoroute announce 
命令参数解释 : 
					无
				 
缺省 : 
隧道默认不支持自动路由。 
使用说明 : 
该功能与静态隧道FA功能互斥。 
范例 : 
使能MPLS自动路由功能:ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#autoroute announce去使能MPLS自动路由功能:ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#no autoroute announce
相关命令 : 
forwarding-adjacency  [ holdtime ＜mpls-te-down-holdtime＞]show mpls traffic-eng static | include AutoRoute 
## autoroute include-ipv6 

autoroute include-ipv6 
命令功能 : 
使能MPLS静态隧道自动路由的IPv6属性，使用no命令，删除IPv6配置。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
autoroute include-ipv6 
 
no autoroute include-ipv6 
命令参数解释 : 
					无
				 
缺省 : 
不使能 
使用说明 : 
该功能与静态隧道FA功能互斥。配置该条属性，必须先使能autoroute announce
范例 : 
使能MPLS静态隧道自动路由IPv6属性ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)# static te_tunnel1ZXROSNG(config-mpls-te- static -te_tunnel1)# autoroute include-ipv6
相关命令 : 
forwarding-adjacency  [ holdtime ＜mpls-te-down-holdtime＞]show mpls traffic-eng static autoroute
## autoroute metric 

autoroute metric 
命令功能 : 
配置隧道的自动路由metric类型和metric值，使用no删除metric配置。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
autoroute metric 
  {absolute 
 ＜absolute-metric-value 
＞|relative 
 ＜relative-metric-value 
＞|＜metric number 
＞}
no autoroute metric 
命令参数解释 : 
参数|描述
---|---
absolute|绝对metric类型
＜absolute-metric-value＞|绝对metric值，范围：1~4294967295
relative|相对metric类型
＜relative-metric-value＞|相对于IGP的metric值，范围：-10~10
＜metric number＞|配置静态隧道的自动路由metric值，范围：1~4294967295
缺省 : 
隧道默认自动路由metric类型为relative，metric值为0，也就是自动路由类型为IGP。 
使用说明 : 
只有在使能了自动路由功能后，才能配置该命令。 
范例 : 
1.配置静态隧道的自动路由metric值为2：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#autoroute metric 22.配置静态隧道的自动路由metric为绝对metric，值为2：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#autoroute metric absolute 23.配置隧道的自动路由metric为相对metric，值为-2：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#autoroute metric relative -24.去使能隧道的自动路由metricZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#no autoroute metric
相关命令 : 
autoroute announceshow mpls traffic-eng static | include AutoRouteMetricType
## avoid-address 

avoid-address 
命令功能 : 
显示路径下配置尽力排除地址 
命令模式 : 
 MPLS-TE显式路径ID模式  
命令默认权限级别 : 
15 
命令格式 : 
avoid-address 
  {interface 
 ＜ip-address 
＞|router-id 
 ＜ip-address 
＞}
命令参数解释 : 
参数|描述
---|---
interface|需要排除接口
＜ip-address＞|指定要排除的节点IP地址
router-id|需要排除 router-id
＜ip-address＞|指定要排除的节点IP地址
缺省 : 
无 
使用说明 : 
在显示路径配置模式下配置尽力排除地址，使用此显示路径的LSP在算路时尽力排除此地址。此命令正向配置后，协议会自动为本跳地址增加索引，去配置时采用如下形式ZXROSNG(config-mpls-te-expl-path-id-1)# no index <index-num>
范例 : 
显示路径模式下配置尽力排除IP地址为192.168.0.1的接口ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path identifier 1 ZXROSNG(config-mpls-te-expl-path-id-1)#avoid-address interface 192.168.0.1
相关命令 : 
exclude-address interface  
## avoid-address 

avoid-address 
命令功能 : 
显示路径下配置尽力排除地址 
命令模式 : 
 MPLS-TE显式路径NAME模式  
命令默认权限级别 : 
15 
命令格式 : 
avoid-address 
  {interface 
 ＜ip-address 
＞|router-id 
 ＜ip-address 
＞}
命令参数解释 : 
参数|描述
---|---
interface|需要排除接口
＜ip-address＞|指定要排除的节点IP地址
router-id|需要排除 router-id
＜ip-address＞|指定要排除的节点IP地址
缺省 : 
无 
使用说明 : 
在显示路径配置模式下配置尽力排除地址，使用此显示路径的LSP在算路时尽力排除此地址。此命令正向配置后，协议会自动为本跳地址增加索引，去配置时采用如下形式ZXROSNG(config-mpls-te-expl-path-id-1)# no index <index-num>
范例 : 
显示路径模式下配置尽力排除IP地址为192.168.0.1的接口ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)# explicit-path name lsp123 ZXROSNG(config-mpls-te-expl-path-name)#avoid-address interface 192.168.0.1
相关命令 : 
exclude-address interface  
## backup-path te_tunnel 

backup-path te_tunnel 
命令功能 : 
在保护链路上，指定一个备份隧道 
命令模式 : 
 MPLS-TE接口模式  
命令默认权限级别 : 
15 
命令格式 : 
backup-path te_tunnel 
  ＜backup-tunnel-id 
＞
no backup-path te_tunnel 
  [＜para 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜backup-tunnel-id＞|备份隧道的隧道ID号，范围：1~$#100794374#$
缺省 : 
无备份隧道配置 
使用说明 : 
对同一个接口最多可以配置16条备份隧道 
范例 : 
ZXROSNG(config-mpls-te-if-gei-0/1/0/1)# backup-path te_tunnel 1 
相关命令 : 
无 
## bandwidth model 

bandwidth model 
命令功能 : 
配置ds-te带宽模型。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
bandwidth model 
  {mpls-te 
|extend-mam 
|mam 
|rdm 
|non-te 
}
no bandwidth model 
命令参数解释 : 
参数|描述
---|---
mpls-te|普通TE模型，非ds-te模型
extend-mam|扩展的最大预留模型
mam|最大预留模型
rdm|俄罗斯套娃模型
non-te|无模型模式
缺省 : 
mpls-te模型配置。 
使用说明 : 
无 
范例 : 
1.配置ds-te带宽模型为mpls-teZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#bandwidth model mpls-te2.配置ds-te带宽模型为extend-mamZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#bandwidth model extend-mam3.配置ds-te带宽模型为mamZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#bandwidth model mam4.配置ds-te带宽模型为rdmZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#bandwidth model rdm5.配置ds-te带宽模型为non-teZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#bandwidth model non-te6.去使能ds-te带宽模型ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#no bandwidth model
相关命令 : 
show rsvp bandwidth model 
## bandwidth reserve mode 

bandwidth reserve mode 
命令功能 : 
配置静态隧道的资源预留模型。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
bandwidth reserve mode 
  {reserve 
|no-reserve 
}
no bandwidth reserve mode 
命令参数解释 : 
参数|描述
---|---
reserve|预留方式，该方式下允许静态LSP配置普通带宽/共享隧道
no-reserve|不预留方式，该方式下只允许静态LSP配置普通带宽
缺省 : 
静态隧道默认预留方式。 
使用说明 : 
配置静态LSP的带宽/共享隧道前，先配置静态隧道资源预留方式，静态LSP带宽/共享隧道配置完成后，不允许修改静态隧道资源预留方式，请参见命令out-seg-info/rvs-out-seg-info。 
范例 : 
1.设置接口带宽预留模式为不预留模式：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#bandwidth reserve mode no-reserve2.去使能接口带宽的不预留模式，即恢复到预留模式：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#no bandwidth reserve mode 
相关命令 : 
out-seg-info out-portrvs-out-seg-info out-portshow mpls traffic-eng static | include Bandwidth Reserve Mode 
## bandwidth 

bandwidth 
命令功能 : 
配置静态P2MP隧道的带宽信息，包括承诺带宽、承诺突发尺寸、超额速率、超额突发尺寸。使用no命令清除该配置。 
命令模式 : 
 MPLS-TE静态P2MP隧道LSP模式  
命令默认权限级别 : 
15 
命令格式 : 
bandwidth 
  {[cir 
 ＜committed-information-rate 
＞ [{kbps 
|mbps 
|gbps 
}]],[cbs 
 ＜committed-burst-size 
＞ [{byte 
|kb 
|mb 
}]],[eir 
 ＜excess-information-rate 
＞ [{kbps 
|mbps 
|gbps 
}]],[ebs 
 ＜excess-burst-size 
＞ [{byte 
|kb 
|mb 
}]]}
no bandwidth 
命令参数解释 : 
参数|描述
---|---
＜committed-information-rate＞|隧道承诺速率，默认单位：kbit/s，范围为$#100794375#$~$#100794376#$
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜committed-burst-size＞|隧道承诺突发尺寸，单位：byte，范围为$#100794381#$~$#100794382#$
byte|以BYTE为单位
kb|以KB为单位
mb|以MB为单位
＜excess-information-rate＞|隧道超额速率，单位：kbps，范围为$#100794407#$~$#100794408#$
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜excess-burst-size＞|隧道超额突发尺寸，单位：byte，范围为$#100794384#$~$#100794385#$
byte|以BYTE为单位
kb|以KB为单位
mb|以MB为单位
缺省 : 
无 
使用说明 : 
与P2MP静态隧道下rate-limit命令会相互覆盖。 
范例 : 
1.配置带宽ZXROSNG(config#mpls traffic-engZXROSNG(config-mpls-te)# static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static-mte_tunnel1)# bandwidth 10000 cbs 1000 pir 15000 ebs 15002.与rate-limit配置会相互覆盖1）原先配置了带宽，后来配置rate-limit，rate-limit配置生效，带宽配置删除配置rate-limit前：ZXROSNG(config)#show running-config mpls-te !＜mpls-te＞mpls traffic-eng  router-id 1.2.3.4  static-mtunnel mte_tunnel1    role root    lsp 1      bandwidth cbs 100    $  $$!＜/mpls-te＞配置rate-limit之后：ZXROSNG(config-mpls-te-static-mte_tunnel1)#  rate-limit mode aware cir 10 cbs 10 pir 20 pbs 20ZXROSNG#show running-config mpls-te!＜mpls-te＞mpls traffic-eng  router-id 1.2.3.4  static-mtunnel mte_tunnel1    role root    rate-limit mode aware cir 10 cbs 10 pir 20 pbs 20    lsp 1    $  $$!＜/mpls-te＞2）原先配置了rate-limit，后配置带宽，带宽生效，rate-limit配置删除配置带宽前：ZXROSNG#show running-config mpls-te!＜mpls-te＞mpls traffic-eng  router-id 1.2.3.4  static-mtunnel mte_tunnel1    role root    rate-limit mode aware cir 10 cbs 10 pir 20 pbs 20    lsp 1    $  $$!＜/mpls-te＞配置带宽后：ZXROSNG(config-mpls-te-static-mte_tunnel1-lsp)#bandwidth cbs 200 cir 200ZXROSNG#show running-config mpls-te!＜mpls-te＞mpls traffic-eng  router-id 1.2.3.4  static-mtunnel mte_tunnel1    role root    lsp 1      bandwidth cir 200 cbs 200    $  $$!＜/mpls-te＞
相关命令 : 
show rsvp bandwidth interface 
## bandwidth 

bandwidth 
命令功能 : 
配置TE接口分类带宽。 
命令模式 : 
 MPLS-TE接口模式  
命令默认权限级别 : 
15 
命令格式 : 
bandwidth 
  [{static 
|dynamic 
}] ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}] [＜perflow bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]] [{[bc0 
 ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]],[bc1 
 ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]],[bc2 
 ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]],[bc3 
 ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]],[bc4 
 ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]],[bc5 
 ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]],[bc6 
 ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]],[bc7 
 ＜bandwidth value 
＞ [{kbps 
|mbps 
|gbps 
}]]}] [percent 
 ＜percent value 
＞] [speed-blind 
] [eir 
 ＜excess information rate 
＞ [{kbps 
|mbps 
|gbps 
}]]
no bandwidth 
  {static 
|dynamic 
} [{[bc0 
],[bc1 
],[bc2 
],[bc3 
],[bc4 
],[bc5 
],[bc6 
],[bc7 
]}] [percent 
] [speed-blind 
] [eir 
]
				
命令参数解释 : 
参数|描述
---|---
static|静态预留类型
dynamic|动态预留类型
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜perflow bandwidth value＞|接口支持每流带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜bandwidth value＞|接口的bc7带宽，范围：1–4294967295 ，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜percent value＞|占用接口speed的百分比，范围：0-100。默认值由产品规格确定，平台默认的动态和静态的占用比都是40.
speed-blind|允许接口最大可用带宽大于接口speed。
＜excess information rate＞|接口超额预留带宽，范围：0–4294967295 ，默认值0，默认单位：kbit/s。接口超额预留带宽加上接口保证预留带宽等于接口峰值预留带宽。接口保证预留带宽即上述命令参数解释的第三个参数“接口支持流量工程的最大带宽”。
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
No参数|描述
---|---
bc0|bc0带宽
bc1|bc1带宽
bc2|bc2带宽
bc3|bc3带宽
bc4|bc4带宽
bc5|bc5带宽
bc6|bc6带宽
bc7|bc7带宽
percent|百分比
eir|eir
缺省 : 
缺省无带宽配置。 
使用说明 : 
1.该命令依赖于带宽预留模型2.接口带宽和每流带宽必须依赖于模型配置3.bc配置依赖于非MPLS-TE模型,bc总带宽不能大于接口总预留带宽。4.动态预留接口speed占用比与静态隧道接口speed占用比之和不能大于100。预留类型如果不输入，表征动态预留类型。配置了speed-blind后，接口最大可用带宽不再受接口speed限制，隧道能够预留的带宽就可以大于接口的speed，接口speed占用比对接口最大可用带宽也没有作用。5.与lmp data link命令互斥
范例 : 
1.配置动态预留类型带宽1000，每流带宽100，bc0带宽10：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface smartgroup1ZXROSNG(config-mpls-te-if-smartgroup1)#bandwidth dynamic 1000 100 bc0 102.配置静态预留类型带宽1000，每流带宽100，bc带宽10，百分比50：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface smartgroup1ZXROSNG(config-mpls-te-if-smartgroup1)#bandwidth static 1000 100 bc0 10 percent 503.去使能动态隧道bc0带宽和百分比：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface smartgroup1ZXROSNG(config-mpls-te-if-smartgroup1)#no bandwidth dynamic bc0 percent4.去使能静态隧道带宽：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface smartgroup1ZXROSNG(config-mpls-te-if-smartgroup1)#no bandwidth static 5.配置动态预留类型带宽1000，每流带宽100，bc带宽10，并且允许隧道预留带宽大于接口speed：ZXROSNG(config-mpls-te-if-smartgroup1)#bandwidth dynamic 1000 100 bc0 10speed-blind6.与lmp data link命令互斥ZXROSNG(config-lmp-neighbor-abc-te-link-1)#show this!<lmp>data-link  interface gei-0/1/0/2!</lmp>ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#interface gei-0/1/0/2ZXROSNG(config-mpls-te-if-gei-0/1/0/2)#bandwidth 1000%Error 99724: LMP and TE interface bandwidth configuration are mutually exclusive at one interface.7.配置动态预留类型带宽1000，每流带宽1000，bc带宽1000 （带非默认单位）ZXROSNG(config-mpls-te-if-smartgroup1)#bandwidth dynamic 1 mbps 1 mbps bc0 1 mbpsZXROSNG(config-mpls-te-if-smartgroup1)#show thisbandwidth dynamic 1000 1000 bc0 1000
相关命令 : 
bandwidth model {mpls-te|extend-mam|mam|rdm|non-te}show rsvp bandwidth interface [<interface name>]
## bfd 

bfd 
命令功能 : 
在本设备的MPLS-TE静态隧道上配置LSP BFD功能，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
bfd 
 interval 
 ＜min-send-interval 
＞ min-rx 
 ＜min-receive-interval 
＞ multiplier 
 ＜multiplier 
＞
no bfd 
命令参数解释 : 
参数|描述
---|---
＜min-send-interval＞|指定期望的报文最小发送间隔时间，范围：$#35389448#$~$#35389449#$，单位：ms
＜min-receive-interval＞|指定期望的报文最小接收间隔时间，范围：$#35389450#$~$#35389451#$，单位：ms
＜multiplier＞|指定检测超时的倍数，范围：3–50
缺省 : 
无 
使用说明 : 
1.只有首节点或双向尾节点才能配置BFD功能。当BFD配置存在时，不允许删除或修改该隧道的role和type。2.每个静态隧道只能配置一条该命令。
范例 : 
1.配置最小发送间隔时间200，最小接收间隔时间300，超时的倍数5：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel64511ZXROSNG(config-mpls-te-static-te_tunnel64511)#role egress type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel64511)#bfd interval 200 min-rx 300 multiplier 52.去使能BFD：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel64511ZXROSNG(config-mpls-te-static-te_tunnel64511)#no bfd
相关命令 : 
role {ingress|transit|egress} type {unidirectional|bidirectional}show mpls traffic-eng static | include BFDshow mpls traffic-eng static | include min-tx
## clear mpls rsvp 

clear mpls rsvp 
命令功能 : 
在本设备上重启TE功能 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear mpls rsvp 
 
命令参数解释 : 
					无
				 
缺省 : 
设备上无此项配置 
使用说明 : 
在路由器上重置TE属性，并删除通过配置TE生成的一系列结果，例如隧道，TE接口等，然后重新加载配置信息，重新生成这些结果 
范例 : 
在本设备上重启TE：ZXROSNG#clear mpls rsvp
相关命令 : 
无 
## clear te mtunnel 

clear te mtunnel 
命令功能 : 
在本设备上重置指定的P2MP隧道 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear te mtunnel 
  ＜tunnel-id 
＞
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|隧道ID，整数，范围1-65535，$#100794374#$（P2MP隧道不使用性能参数）
缺省 : 
设备上无此项配置 
使用说明 : 
在设备上重置指定的P2MP隧道 
范例 : 
ZXROSNG#clear te mtunnel 1Are you sure to clear the MTE tunnel? [yes/no]:
相关命令 : 
无 
## clear te tunnel 

clear te tunnel 
命令功能 : 
在本设备上重置指定的P2P或者SR隧道 
命令模式 : 
 特权模式  
命令默认权限级别 : 
15 
命令格式 : 
clear te tunnel 
  ＜tunnel-id 
＞
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|隧道ID，范围：1–32768,最大值由本地隧道的性能参数决定，范围1~$#100794374#$
缺省 : 
设备上无此项配置 
使用说明 : 
在设备上重置指定的P2P或者SR隧道 
范例 : 
ZXROSNG#clear te tunnel 1Are you sure to clear the TE tunnel? [yes/no]:
相关命令 : 
无 
## convergence-ratio value 

convergence-ratio value 
命令功能 : 
在本设备的MPLS-TE接口上配置收敛比数值，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE接口模式  
命令默认权限级别 : 
15 
命令格式 : 
convergence-ratio value 
  ＜value 
＞
no convergence-ratio value 
命令参数解释 : 
参数|描述
---|---
＜value＞|TE接口收敛比数值，范围：1-100，单位：percent
缺省 : 
默认收敛比为100
使用说明 : 
只有隧道绑定该接口为出接口时且隧道的收敛比模式为继承模式时，该配置才有意义。
范例 : 
1.配置TE接口的收敛比数值为90：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#convergence-ratio value 902.删除TE接口的收敛比数值：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#no convergence-ratio value
相关命令 : 
out-seg convergence-ratio mode inherit
## cspf delay link-up 

cspf delay link-up 
命令功能 : 
开启链路UP延迟响应功能 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
cspf delay link-up 
  ＜link-up delay 
＞
no cspf delay link-up 
命令参数解释 : 
参数|描述
---|---
＜link-up delay＞|链路UP延迟响应的时长，范围0～120，单位为秒
缺省 : 
默认0s，表示关闭链路UP延迟响应功能 
使用说明 : 
配置参数0或者使用no命令关闭链路UP延迟响应功能，配置其它值表示延迟时长。 
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#cspf delay link-up 5
相关命令 : 
无 
## cspf delay reactive 

cspf delay reactive 
命令功能 : 
开启第二次重建延迟功能 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
cspf delay reactive 
  ＜reactive delay 
＞ [precise 
 ＜preciseTime 
＞]
no cspf delay reactive 
命令参数解释 : 
参数|描述
---|---
＜reactive delay＞|第二次重建延迟的时长，范围0～30，单位为秒
＜preciseTime＞|配置100ms精度时间，范围为1~9，单位为100ms
缺省 : 
默认为10s，表示开启第二次重建延迟功能 
使用说明 : 
配置参数0或者使用no命令关闭第二次重建延迟功能，配置其它值表示延迟时长。该命令只对第二次重建起作用，第三次及其以后的重建依靠命令unactive timer来决定。如果要配置100ms精度，在配置第一个参数后追加100ms精度参数，范围为<100~900>ms。两个参数叠加后为最终时间。只配置第一个参数，可覆盖100ms精度参数。配置最大值30s后，高精度参数不能配置，否则会报错。
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#cspf delay reactive 5ZXROSNG(config-mpls-te)#cspf delay reactive 5 precisetime 5 
相关命令 : 
无 
## cspf delay switch-over 

cspf delay switch-over 
命令功能 : 
开启HSB/FRR延迟回切功能 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
cspf delay switch-over 
  ＜switch-over delay 
＞
no cspf delay switch-over 
命令参数解释 : 
参数|描述
---|---
＜switch-over delay＞|HSB/FRR延迟回切的时长，范围0～90，单位为秒
缺省 : 
默认0s，表示关闭HSB/FRR延迟回切功能 
使用说明 : 
配置参数0或者使用no命令关闭HSB/FRR延迟回切功能，配置其它值表示延迟时长。
范例 : 
范例ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#cspf delay switch-over 5
相关命令 : 
无 
## cspf delay topo-change 

cspf delay topo-change 
命令功能 : 
配置路由拓扑变化延迟通告TE的时间 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
cspf delay topo-change 
  ＜topology-change delay 
＞
no cspf delay topo-change 
命令参数解释 : 
参数|描述
---|---
＜topology-change delay＞|路由拓扑变化延迟通告TE时长，范围0～30，单位为秒
缺省 : 
默认5s，表示默认开启路由拓扑变化延迟通告功能 
使用说明 : 
No掉配置路由拓扑变化延迟通告时间是5s，只有配置为0，才没有延迟时间。 
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#cspf delay topo-change 5
相关命令 : 
无 
## cspf preferred-igp 

cspf preferred-igp 
命令功能 : 
指定路由优先使用某种IGP算路协议进行CSPF算路。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
cspf preferred-igp 
  {ospf 
 [process 
 ＜OSPF process ID 
＞ [area 
 ＜OSPF area ID 
＞]]|isis 
 [process 
 ＜ISIS process ID 
＞ [{level-1 
|level-2 
}]]}
no cspf preferred-igp 
命令参数解释 : 
参数|描述
---|---
ospf|优先使用OSPF协议进行CSPF算路。
process|配置优先使用的IGP协议的实例。
＜OSPF process ID＞|优先使用的IGP协议的实例号。OSPF协议的范围为1~65535。
area|配置优先使用的OSPF协议的区域。
＜OSPF area ID＞|区域标识符。范围为0.0.0.0~ff.ff.ff.ff。
isis|优先使用ISIS协议进行CSPF算路。
process|配置优先使用的IGP协议的实例。
＜ISIS process ID＞|优先使用的IGP协议的实例号。ISIS协议的范围为0~65535。
level-1|优先使用处于level-1区域的路径。
level-2|优先使用处于level-2区域的路径。
缺省 : 
不指定路由优先使用的算路协议，按照原有的实现方式选择算路协议 
使用说明 : 
若指定路由优先使用OSPF算路协议，则进行CSPF算路时，优先选用OSPF协议进行算路，算路失败后再尝试ISIS协议进行算路若指定路由优先使用ISIS算路协议，则进行CSPF算路时，优先选用ISIS协议进行算路，算路失败后再尝试OSPF协议进行算路若不配置该命令，路由则按照原有的实现方式选择算路协议
范例 : 
配置CSPF算路OSPF协议优先ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#cspf preferred-igp ospf 
相关命令 : 
tunnel mpls traffic-eng preferred-igptunnel mpls traffic-eng hot-standby preferred-igp 
## cspf tie-breaking 

cspf tie-breaking 
命令功能 : 
开启TE所有动态隧道CSPF算路带宽占比仲裁功能。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
cspf tie-breaking 
  {least-fill 
|most-fill 
}
no cspf tie-breaking 
命令参数解释 : 
参数|描述
---|---
least-fill|优先选择可用带宽占比大的路径
most-fill|优先选择可用带宽占比小的路径
缺省 : 
无 
使用说明 : 
使用场景隧道CSPF算路时，在多条路径权值相同的情况下，可通过该配置指定根据可用带宽比例大小进行优选的一个策略，least-fill为优先选择可用带宽占比大的路径，most-fill为优先选择可用带宽占比小的路径。
范例 : 
配置优先选择可用带宽占比小的路径：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#cspf tie-breaking most-fill
相关命令 : 
无 
## debug mpls-te all 

debug mpls-te all 
命令功能 : 
打开TE_MP相关的所有的debug开关，使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te all 
 
no debug mpls-te all 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te allAll MPLS-TE debugging has been turned on
相关命令 : 
show debug te-mp 
## debug mpls-te associated-tunnel 

debug mpls-te associated-tunnel 
命令功能 : 
打开associated-tunnel的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te associated-tunnel 
 
no debug mpls-te associated-tunnel 
命令参数解释 : 
					无
				 
缺省 : 
不开启associated-tunnel的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te associated-tunnel 
相关命令 : 
无
## debug mpls-te authentication 

debug mpls-te authentication 
命令功能 : 
打开或关闭MPLS-TE的authentication调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te authentication 
 
no debug mpls-te authentication 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的authentication debug开关
使用说明 : 
打开：ZXROSNG#debug mpls-te authentication MPLS-TE authentication debugging is on关闭：ZXROSNG#no debug mpls-te authentication                                          MPLS-TE authentication debugging is off
范例 : 
ZXROSNG#debug mpls-te authentication MPLS-TE authentication debugging is onZXROSNG#no debug mpls-te authentication                                          MPLS-TE authentication debugging is off
相关命令 : 
无
## debug mpls-te auto-backup 

debug mpls-te auto-backup 
命令功能 : 
打开MPLS-TE自动备份隧道功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te auto-backup 
 
no debug mpls-te auto-backup 
命令参数解释 : 
					无
				 
缺省 : 
无
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te auto-backup                                                MPLS-TE auto-backup debugging is onZXROSNG#no debug mpls-te auto-backup                                             MPLS-TE auto-backup debugging is off
相关命令 : 
无
## debug mpls-te auto-bw 

debug mpls-te auto-bw 
命令功能 : 
打开MPLS-TE自动带宽调节功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te auto-bw 
 
no debug mpls-te auto-bw 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te auto-bw MPLS-TE auto-bw debugging is onZXROSNG#no debug mpls-te auto-bw                                                 MPLS-TE auto-bw debugging is off
相关命令 : 
无 
## debug mpls-te bfd 

debug mpls-te bfd 
命令功能 : 
打开MPLS-TE 隧道BFD功能的调试信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te bfd 
 
no debug mpls-te bfd 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te bfdMPLS-TE BFD debugging is on
相关命令 : 
无 
## debug mpls-te bundle 

debug mpls-te bundle 
命令功能 : 
开启/关闭bundle的debug信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te bundle 
 
no debug mpls-te bundle 
命令参数解释 : 
					无
				 
缺省 : 
关闭bundle的debug信息
使用说明 : 
在特权模式下输入debug mpls-te bundle，开启bundle的debug信息；输入no debug mpls-te bundle，关闭bundle的debug信息。
范例 : 
ZXROSNG#debug mpls-te bundle MPLS-TE bundle debugging is onZXROSNG#no debug mpls-te bundle                                                  MPLS-TE bundle debugging is off
相关命令 : 
无 
## debug mpls-te cac 

debug mpls-te cac 
命令功能 : 
打开MPLS-TE cac功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te cac 
 
no debug mpls-te cac 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te cac MPLS-TE CAC debugging is on
相关命令 : 
无 
## debug mpls-te config 

debug mpls-te config 
命令功能 : 
打开或关闭MPLS-TE的config调试信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te config 
 
no debug mpls-te config 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的config debug开关 
使用说明 : 
无 
范例 : 
打开config的debug开关ZXROSNG#debug mpls-te configMPLS-TE config debugging is on
相关命令 : 
无 
## debug mpls-te detour 

debug mpls-te detour 
命令功能 : 
MPLS-TE detour消息调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te detour 
 
no debug mpls-te detour 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te detour MPLS-TE detour debugging is onZXROSNG#no debug mpls-te detour                                                  MPLS-TE detour debugging is off
相关命令 : 
无
## debug mpls-te fa 

debug mpls-te fa 
命令功能 : 
打开MPLS-TE fa功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te fa 
 
no debug mpls-te fa 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te faMPLS-TE FA debugging is on
相关命令 : 
无
## debug mpls-te fast-reroute 

debug mpls-te fast-reroute 
命令功能 : 
MPLS-TE fast-reroute消息调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te fast-reroute 
 
no debug mpls-te fast-reroute 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te fast-reroute MPLS-TE fast-reroute debugging is on
相关命令 : 
无
## debug mpls-te filter tunnel 

debug mpls-te filter tunnel 
命令功能 : 
该命令开启某条隧道的debug打印，最多可以配置16条隧道，使用no命令关闭过滤功能。
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te filter tunnel 
  ＜filter tunnel-id 
＞
no debug mpls-te filter tunnel 
  [＜filter tunnel-id 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜filter tunnel-id＞|指定开启debug打印的隧道ID
缺省 : 
默认开启所有隧道的debug打印。
使用说明 : 
打开：ZXROSNG#debug mpls-te filter tunnel 1                                          关闭：ZXROSNG#no debug mpls-te filter tunnel 1                                         MPLS-TE filter tunnel debugging is off
范例 : 
ZXROSNG#debug mpls-te filter tunnel 1MPLS-TE filter tunnel debugging is onZXROSNG#no debug mpls-te filter tunnel 1MPLS-TE filter tunnel debugging is off
相关命令 : 
无 
## debug mpls-te forwarding-management 

debug mpls-te forwarding-management 
命令功能 : 
打开MPLS-TE 转发管理的相关调试信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te forwarding-management 
 
no debug mpls-te forwarding-management 
命令参数解释 : 
					无
				 
缺省 : 
不打开forwarding-management的调试信息 
使用说明 : 
无 
范例 : 
开启forwarding-management的debug开关：ZXROSNG#debug mpls-te forwarding-managementMPLS-TE forwarding-management debugging is on
相关命令 : 
无 
## debug mpls-te graceful-deletion 

debug mpls-te graceful-deletion 
命令功能 : 
打开MPLS-TE优雅删除功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te graceful-deletion 
 
no debug mpls-te graceful-deletion 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te graceful-deletion MPLS-TE graceful deletion message debugging is onZXROSNG#no debug mpls-te graceful-deletion                                       MPLS-TE graceful deletion message debugging is off
相关命令 : 
无
## debug mpls-te graceful-restart 

debug mpls-te graceful-restart 
命令功能 : 
打开或关闭MPLS-TE的graceful-restart调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te graceful-restart 
 
no debug mpls-te graceful-restart 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的graceful-restart debug开关
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te graceful-restart MPLS-TE graceful-restart debugging is on
相关命令 : 
无
## debug mpls-te hello 

debug mpls-te hello 
命令功能 : 
打开或关闭MPLS-TE hello的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te hello 
 
no debug mpls-te hello 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的hello debug开关
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te hello MPLS-TE hello debugging is on
相关命令 : 
无
## debug mpls-te hot-standby 

debug mpls-te hot-standby 
命令功能 : 
打开MPLS-TE hot_standby功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te hot-standby 
 
no debug mpls-te hot-standby 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te hot-standby MPLS-TE hot-standby debugging is onZXROSNG#no debug mpls-te hot-standby                                             MPLS-TE hot-standby debugging is off
相关命令 : 
无 
## debug mpls-te interactive 

debug mpls-te interactive 
命令功能 : 
打开MPLS-TE interactive功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te interactive 
 
no debug mpls-te interactive 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te interactive                                                MPLS-TE interactive debugging is on
相关命令 : 
无
## debug mpls-te inter-as 

debug mpls-te inter-as 
命令功能 : 
打开MPLS-TE跨域功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te inter-as 
 
no debug mpls-te inter-as 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te inter-as MPLS-TE inter-as debugging is onZXROSNG#no debug mpls-te inter-as                                                MPLS-TE inter-as debugging is off
相关命令 : 
无 
## debug mpls-te message 

debug mpls-te message 
命令功能 : 
打开MPLS-TE接收和发送进程间消息的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te message 
 
no debug mpls-te message 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te messageMPLS-TE message debugging is on
相关命令 : 
无 
## debug mpls-te notify 

debug mpls-te notify 
命令功能 : 
MPLS-TE notify消息调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te notify 
 
no debug mpls-te notify 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的notify调试信息
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te notify MPLS-TE notify debugging is on
相关命令 : 
无 
## debug mpls-te p2mp all 

debug mpls-te p2mp all 
命令功能 : 
P2MP打开MPLS-TE所有debug命令
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp all 
 
no debug mpls-te p2mp all 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp all  P2MP-TE ALL MPLS-TE debugging has been turned on关闭：ZXROSNG#no debug mpls-te p2mp all                                                P2MP-TE ALL MPLS-TE debugging has been turned off
范例 : 
ZXROSNG#debug mpls-te p2mp all  P2MP-TE ALL MPLS-TE debugging has been turned onZXROSNG#no debug mpls-te p2mp all                                                P2MP-TE ALL MPLS-TE debugging has been turned off
相关命令 : 
无
## debug mpls-te p2mp bandwidth 

debug mpls-te p2mp bandwidth 
命令功能 : 
P2MP 打印带宽流程的信息的debug命令
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp bandwidth 
 
no debug mpls-te p2mp bandwidth 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp bandwidth P2MP-TE bandwidth debugging is on关闭：ZXROSNG#no debug mpls-te p2mp bandwidth                                          P2MP-TE bandwidth debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp bandwidth P2MP-TE bandwidth debugging is onZXROSNG#no debug mpls-te p2mp bandwidth                                          P2MP-TE bandwidth debugging is off
相关命令 : 
无
## debug mpls-te p2mp exec-brief 

debug mpls-te p2mp exec-brief 
命令功能 : 
打开或关闭exec-brief debug信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp exec-brief 
 
no debug mpls-te p2mp exec-brief 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
1.开启exec-brief的debug开关：ZXROSNG#debug mpls-te p2mp  exec-briefP2MP-TE tunnel execution brief debugging is on2.关闭exec-brief的debug开关ZXROSNG#no debug mpls-te p2mp  exec-briefP2MP-TE tunnel execution brief debugging is off
相关命令 : 
无 
## debug mpls-te p2mp exec-detail 

debug mpls-te p2mp exec-detail 
命令功能 : 
打开或关闭 执行详细 debug信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp exec-detail 
 
no debug mpls-te p2mp exec-detail 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
1.开启p2mp  exec-detail的debug开关：ZXROSNG#debug mpls-te p2mp  exec-detailMPLS-TE tunnel execution detail debugging is on2.关闭p2mp  exec-detail的debug开关：ZXROSNG#no debug mpls-te p2mp  exec-detailMPLS-TE tunnel execution detail debugging is off
相关命令 : 
无 
## debug mpls-te p2mp fast-reroute 

debug mpls-te p2mp fast-reroute 
命令功能 : 
P2MP 打印FRR流程的debug命令
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp fast-reroute 
 
no debug mpls-te p2mp fast-reroute 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp fast-reroute P2MP-TE fast-reroute debugging is on关闭：ZXROSNG#no debug mpls-te p2mp fast-reroute                                       P2MP-TE fast-reroute debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp fast-reroute P2MP-TE fast-reroute debugging is onZXROSNG#no debug mpls-te p2mp fast-reroute                                       P2MP-TE fast-reroute debugging is off
相关命令 : 
无
## debug mpls-te p2mp forwarding 

debug mpls-te p2mp forwarding 
命令功能 : 
打开或关闭 组件转发相关流程的debug 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp forwarding 
 
no debug mpls-te p2mp forwarding 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
1.开启p2mp forwarding的debug开关：ZXROSNG#debug mpls-te p2mp  forwardingP2MP-TE forwarding debugging is on2. 关闭p2mp forwarding的debug开关：ZXROSNG#no debug mpls-te p2mp  forwardingP2MP-TE forwarding debugging is off
相关命令 : 
无 
## debug mpls-te p2mp hello 

debug mpls-te p2mp hello 
命令功能 : 
P2MP 打印HELLO流程信息的debug功能
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp hello 
 
no debug mpls-te p2mp hello 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp hello P2MP-TE hello debugging is on关闭：ZXROSNG#no debug mpls-te p2mp hello                                              P2MP-TE hello debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp hello P2MP-TE hello debugging is onZXROSNG#no debug mpls-te p2mp hello                                              P2MP-TE hello debugging is off
相关命令 : 
无
## debug mpls-te p2mp message 

debug mpls-te p2mp message 
命令功能 : 
打印P2MP各组件，进程间消息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp message 
 
no debug mpls-te p2mp message 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp message P2MP-TE message debugging is on关闭：ZXROSNG#no debug mpls-te p2mp message                                            P2MP-TE message debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp message P2MP-TE message debugging is onZXROSNG#no debug mpls-te p2mp message                                            P2MP-TE message debugging is off
相关命令 : 
无
## debug mpls-te p2mp notify 

debug mpls-te p2mp notify 
命令功能 : 
P2MP 打印notify消息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp notify 
 
no debug mpls-te p2mp notify 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：debug mpls-te p2mp notify 关闭：no debug mpls-te p2mp notify
范例 : 
ZXROSNG#debug mpls-te p2mp notify P2MP-TE notify debugging is onZXROSNG#no debug mpls-te p2mp notify                                             P2MP-TE notify debugging is off
相关命令 : 
无 
## debug mpls-te p2mp path 

debug mpls-te p2mp path 
命令功能 : 
P2MP 打印path报文处理信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp path 
 
no debug mpls-te p2mp path 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp pathP2MP-TE path debugging is on关闭：ZXROSNG#no debug mpls-te p2mp path                                               P2MP-TE path debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp pathP2MP-TE path debugging is onZXROSNG#no debug mpls-te p2mp path                                               P2MP-TE path debugging is off
相关命令 : 
无
## debug mpls-te p2mp path-err 

debug mpls-te p2mp path-err 
命令功能 : 
P2MP 打印path error报文处理信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp path-err 
 
no debug mpls-te p2mp path-err 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp path-err P2MP-TE path error debugging is on关闭：ZXROSNG#no debug mpls-te p2mp path-err                                           P2MP-TE path error debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp path-err P2MP-TE path error debugging is onZXROSNG#no debug mpls-te p2mp path-err                                           P2MP-TE path error debugging is off
相关命令 : 
无 
## debug mpls-te p2mp path-tear 

debug mpls-te p2mp path-tear 
命令功能 : 
P2MP 打印path tear报文处理信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp path-tear 
 
no debug mpls-te p2mp path-tear 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp path-tear P2MP-TE path tear debugging is on关闭：ZXROSNG#no debug mpls-te p2mp path-tear                                          P2MP-TE path tear debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp path-tear P2MP-TE path tear debugging is onZXROSNG#no debug mpls-te p2mp path-tear                                          P2MP-TE path tear debugging is off
相关命令 : 
无 
## debug mpls-te p2mp policy 

debug mpls-te p2mp policy 
命令功能 : 
打开或关闭policy debug信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp policy 
 
no debug mpls-te p2mp policy 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
1.开启p2mp policy的debug开关：ZXROSNG#debug mpls-te p2mp policyP2MP-TE policy debugging is on2.关闭p2mp policy的debug开关：ZXROSNG#no debug mpls-te p2mp policyP2MP-TE policy debugging is off
相关命令 : 
无 
## debug mpls-te p2mp proc-control 

debug mpls-te p2mp proc-control 
命令功能 : 
打开或关闭 处理控制debug信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp proc-control 
 
no debug mpls-te p2mp proc-control 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
1.开启p2mp  proc-control的debug开关：ZXROSNG#debug mpls-te p2mp  proc-controlP2MP-TE tunnel process control debugging is on2.关闭p2mp  proc-control的debug开关：ZXROSNG#no debug mpls-te p2mp  proc-controlP2MP-TE tunnel process control debugging is off
相关命令 : 
无 
## debug mpls-te p2mp refresh 

debug mpls-te p2mp refresh 
命令功能 : 
P2MP 打印摘要刷新流程信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp refresh 
 
no debug mpls-te p2mp refresh 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp refresh P2MP-TE refresh debugging is on关闭：ZXROSNG#no debug mpls-te p2mp refresh                                            P2MP-TE refresh debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp refresh P2MP-TE refresh debugging is onZXROSNG#no debug mpls-te p2mp refresh                                            P2MP-TE refresh debugging is off
相关命令 : 
无 
## debug mpls-te p2mp resv 

debug mpls-te p2mp resv 
命令功能 : 
P2MP 打印resv报文处理信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp resv 
 
no debug mpls-te p2mp resv 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp resv       P2MP-TE resv debugging is on关闭：ZXROSNG#no debug mpls-te p2mp resv                                               P2MP-TE resv debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp resv       P2MP-TE resv debugging is onZXROSNG#no debug mpls-te p2mp resv                                               P2MP-TE resv debugging is off
相关命令 : 
无 
## debug mpls-te p2mp resv-err 

debug mpls-te p2mp resv-err 
命令功能 : 
P2MP 打印resv error报文处理信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp resv-err 
 
no debug mpls-te p2mp resv-err 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp resv-err P2MP-TE resv error debugging is on关闭：ZXROSNG#no debug mpls-te p2mp resv-err                                           P2MP-TE resv error debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp resv-err P2MP-TE resv error debugging is onZXROSNG#no debug mpls-te p2mp resv-err                                           P2MP-TE resv error debugging is off
相关命令 : 
无 
## debug mpls-te p2mp resv-tear 

debug mpls-te p2mp resv-tear 
命令功能 : 
P2MP 打印resv tear报文处理信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp resv-tear 
 
no debug mpls-te p2mp resv-tear 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te p2mp resv-tear P2MP-TE resv tear debugging is on关闭：ZXROSNG#no debug mpls-te p2mp resv-tear                                          P2MP-TE resv tear debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp resv-tear P2MP-TE resv tear debugging is onZXROSNG#no debug mpls-te p2mp resv-tear                                          P2MP-TE resv tear debugging is off
相关命令 : 
无 
## debug mpls-te p2mp route-query 

debug mpls-te p2mp route-query 
命令功能 : 
打开或关闭 MPC组件路由查询相关流程的debug信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp route-query 
 
no debug mpls-te p2mp route-query 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
1.开启p2mp route-query的debug开关：ZXROSNG#debug mpls-te p2mp route-queryP2MP-TE route query debugging is on2.关闭p2mp route-query的debug开关：ZXROSNG#no debug mpls-te p2mp route-queryP2MP-TE route query debugging is off
相关命令 : 
无 
## debug mpls-te p2mp static-bandwidth 

debug mpls-te p2mp static-bandwidth 
命令功能 : 
控制静态P2MP隧道带宽功能调试信息打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp static-bandwidth 
 
no debug mpls-te p2mp static-bandwidth 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
开启后可以看到静态P2PM隧道带宽的调试信息。 
范例 : 
1.开启ZXROSNG#debug mpls-te p2mp static-bandwidthP2MP-TE static bandwidth debugging is on2.关闭ZXROSNG#no debug mpls-te p2mp static-bandwidthP2MP-TE static bandwidth debugging is off
相关命令 : 
无 
## debug mpls-te p2mp static-forwarding 

debug mpls-te p2mp static-forwarding 
命令功能 : 
控制静态P2MP隧道转发功能调试信息打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp static-forwarding 
 
no debug mpls-te p2mp static-forwarding 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
开启后可以看到静态P2PM隧道下转发的调试信息。 
范例 : 
1.开启ZXROSNG#debug mpls-te p2mp static-forwardingP2MP-TE static forwarding debugging is on2.关闭ZXROSNG#no debug mpls-te p2mp static-forwardingP2MP-TE static forwarding debugging is off
相关命令 : 
无 
## debug mpls-te p2mp static-tunnel 

debug mpls-te p2mp static-tunnel 
命令功能 : 
控制静态P2MP隧道配置管理功能调试信息打印开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp static-tunnel 
 
no debug mpls-te p2mp static-tunnel 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
开启后可以看到静态P2PM隧道的调试信息。 
范例 : 
1.开启ZXROSNG#debug mpls-te p2mp static-tunnelP2MP-TE static tunnel debugging is on2.关闭ZXROSNG#no debug mpls-te p2mp static-tunnelP2MP-TE static tunnel debugging is off
相关命令 : 
无 
## debug mpls-te p2mp timer 

debug mpls-te p2mp timer 
命令功能 : 
P2MP 打印定时器相关信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp timer 
 
no debug mpls-te p2mp timer 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
ZXROSNG#debug mpls-te p2mp timer P2MP-TE timer debugging is onZXROSNG#no debug mpls-te p2mp timer                                              P2MP-TE timer debugging is off
范例 : 
ZXROSNG#debug mpls-te p2mp timer P2MP-TE timer debugging is onZXROSNG#no debug mpls-te p2mp timer                                              P2MP-TE timer debugging is off
相关命令 : 
无 
## debug mpls-te p2mp up-call 

debug mpls-te p2mp up-call 
命令功能 : 
打开或关闭 up-call流程的debug信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te p2mp up-call 
 
no debug mpls-te p2mp up-call 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
1.开启p2mp up-call的debug开关：ZXROSNG#debug mpls-te p2mp up-callP2MP-TE upcall debugging is on2.关闭p2mp up-call的debug开关：ZXROSNG#no debug mpls-te p2mp up-callP2MP-TE upcall debugging is off
相关命令 : 
无 
## debug mpls-te packet 

debug mpls-te packet 
命令功能 : 
打开或关闭MPLS-TE的packet调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet 
 
no debug mpls-te packet 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的packet debug开关
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te packet MPLS-TE packet debugging is on
相关命令 : 
无 
## debug mpls-te packet-content ack 

debug mpls-te packet-content ack 
命令功能 : 
打开或关闭MPLS-TE的ACK  报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content ack 
 
no debug mpls-te packet-content ack 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content ack MPLS-TE ACK  message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content all 

debug mpls-te packet-content all 
命令功能 : 
开或关闭MPLS-TE所有报文的packet-content信息打
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content all 
 
no debug mpls-te packet-content all 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content all MPLS-TE all message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content bundle 

debug mpls-te packet-content bundle 
命令功能 : 
打开或关闭MPLS-TE的Bundle报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content bundle 
 
no debug mpls-te packet-content bundle 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content bundle MPLS-TE Bundle message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content challenge 

debug mpls-te packet-content challenge 
命令功能 : 
打开或关闭MPLS-TE的Integrity Challenge报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content challenge 
 
no debug mpls-te packet-content challenge 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content challengeMPLS-TE Integrity Challenge message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content hello 

debug mpls-te packet-content hello 
命令功能 : 
打开或关闭MPLS-TE的Hello报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content hello 
 
no debug mpls-te packet-content hello 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content helloMPLS-TE Hello message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content notify 

debug mpls-te packet-content notify 
命令功能 : 
打开或关闭MPLS-TE的Notify报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content notify 
 
no debug mpls-te packet-content notify 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content notifyMPLS-TE Notify message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content path 

debug mpls-te packet-content path 
命令功能 : 
打开或关闭MPLS-TE的Path报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content path 
 
no debug mpls-te packet-content path 
命令参数解释 : 
					无
				 
缺省 : 
不打开开关 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content path MPLS-TE Path message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content path-err 

debug mpls-te packet-content path-err 
命令功能 : 
打开或关闭MPLS-TE的PathErr报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content path-err 
 
no debug mpls-te packet-content path-err 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te packet-content path-errMPLS-TE path error message content debugging is onZXROSNG#no debug mpls-te packet-content path-errMPLS-TE path error message content debugging is off
相关命令 : 
关闭 
## debug mpls-te packet-content path-tear 

debug mpls-te packet-content path-tear 
命令功能 : 
打开或关闭MPLS-TE的PathTear报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content path-tear 
 
no debug mpls-te packet-content path-tear 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content path-tearMPLS-TE PathTear  message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content rec-path 

debug mpls-te packet-content rec-path 
命令功能 : 
打开或关闭MPLS-TE的RecoveryPath报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content rec-path 
 
no debug mpls-te packet-content rec-path 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content rec-pathMPLS-TE RecoveryPath message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content response 

debug mpls-te packet-content response 
命令功能 : 
打开或关闭MPLS-TE的Integrity Response报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content response 
 
no debug mpls-te packet-content response 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content responseMPLS-TE Integrity Response message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content resv 

debug mpls-te packet-content resv 
命令功能 : 
打开或关闭MPLS-TE的Resv报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content resv 
 
no debug mpls-te packet-content resv 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content resvMPLS-TE Resv  message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content resv-conf 

debug mpls-te packet-content resv-conf 
命令功能 : 
打开或关闭MPLS-TE的ResvConf报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content resv-conf 
 
no debug mpls-te packet-content resv-conf 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content resv-confMPLS-TE ResvConf message content debugging is on
相关命令 : 
关闭 
## debug mpls-te packet-content resv-err 

debug mpls-te packet-content resv-err 
命令功能 : 
打开或关闭MPLS-TE的ResvErr报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content resv-err 
 
no debug mpls-te packet-content resv-err 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content resv-errMPLS-TE ResvErr  message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content resv-tear 

debug mpls-te packet-content resv-tear 
命令功能 : 
打开或关闭MPLS-TE的ResvTear报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content resv-tear 
 
no debug mpls-te packet-content resv-tear 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content resv-tearMPLS-TE ResvTear  message content debugging is on
相关命令 : 
无 
## debug mpls-te packet-content srefresh 

debug mpls-te packet-content srefresh 
命令功能 : 
打开或关闭MPLS-TE的Srefresh报文的packet-content信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te packet-content srefresh 
 
no debug mpls-te packet-content srefresh 
命令参数解释 : 
					无
				 
缺省 : 
关闭 
使用说明 : 
无 
范例 : 
ZXROSNG#debug  mpls-te packet-content srefreshMPLS-TE Srefresh message content debugging is on
相关命令 : 
无 
## debug mpls-te path 

debug mpls-te path 
命令功能 : 
打开或关闭MPLS-TE的path调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te path 
 
no debug mpls-te path 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的path debug开关
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te path MPLS-TE path debugging is on
相关命令 : 
无
## debug mpls-te path-compute 

debug mpls-te path-compute 
命令功能 : 
打开MPLS-TE路径计算功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te path-compute 
 
no debug mpls-te path-compute 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te path-compute MPLS-TE path compute debugging is on
相关命令 : 
无
## debug mpls-te path-err 

debug mpls-te path-err 
命令功能 : 
打开或关闭MPLS-TE的path-err调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te path-err 
 
no debug mpls-te path-err 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的path-err debug开关
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te path-err MPLS-TE path error debugging is on
相关命令 : 
无
## debug mpls-te path-tear 

debug mpls-te path-tear 
命令功能 : 
打开或关闭MPLS-TE path-tear的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te path-tear 
 
no debug mpls-te path-tear 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的path-tear debug开关
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te path-tear MPLS-TE path tear debugging is on
相关命令 : 
无
## debug mpls-te pcep 

debug mpls-te pcep 
命令功能 : 
打开MPLS-TE  与PCC交互以及其它PCEP协议相关调试信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te pcep 
 
no debug mpls-te pcep 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE PCEP相关的调试信息 
使用说明 : 
无 
范例 : 
开启PCEP的debug开关：ZXROSNG#debug mpls-te pcepMPLS-TE PCEP debugging is on
相关命令 : 
无 
## debug mpls-te preempt 

debug mpls-te preempt 
命令功能 : 
MPLS-TE preempt消息的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te preempt 
 
no debug mpls-te preempt 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
打开：ZXROSNG#debug mpls-te preempt MPLS-TE preempt debugging is on关闭：ZXROSNG#no debug mpls-te preempt                                                 MPLS-TE preempt debugging is off
范例 : 
ZXROSNG#debug mpls-te preempt MPLS-TE preempt debugging is onZXROSNG#no debug mpls-te preempt                                                 MPLS-TE preempt debugging is off
相关命令 : 
无
## debug mpls-te refresh-reduction 

debug mpls-te refresh-reduction 
命令功能 : 
打开或关闭RSVP的refresh-reduction调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te refresh-reduction 
 
no debug mpls-te refresh-reduction 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的refresh-reduction debug开关
使用说明 : 
无
范例 : 
打开：ZXROSNG#debug mpls-te refresh-reduction MPLS-TE refresh-reduction debugging is on关闭：ZXROSNG#no debug mpls-te refresh-reduction                                       MPLS-TE refresh-reduction debugging is off
相关命令 : 
无
## debug mpls-te reoptimize 

debug mpls-te reoptimize 
命令功能 : 
打开MPLS-TE隧道重优化功能的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te reoptimize 
 
no debug mpls-te reoptimize 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te reoptimizeMPLS-TE reoptimize debugging is on
相关命令 : 
无
## debug mpls-te resv 

debug mpls-te resv 
命令功能 : 
打开或关闭MPLS-TE的resv调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te resv 
 
no debug mpls-te resv 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的resv debug开关
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te resv MPLS-TE resv debugging is on
相关命令 : 
无
## debug mpls-te resv-confirm 

debug mpls-te resv-confirm 
命令功能 : 
打开RESV CONFIRM功能的debug命令
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te resv-confirm 
 
no debug mpls-te resv-confirm 
命令参数解释 : 
					无
				 
缺省 : 
关闭
使用说明 : 
打开：ZXROSNG#debug mpls-te resv-confirm MPLS-TE resv-confirm debugging is on关闭：ZXROSNG#no debug mpls-te resv-confirm                                            MPLS-TE resv-confirm debugging is off
范例 : 
ZXROSNG#debug mpls-te resv-confirm MPLS-TE resv-confirm debugging is onZXROSNG#no debug mpls-te resv-confirm                                            MPLS-TE resv-confirm debugging is off
相关命令 : 
无
## debug mpls-te resv-err 

debug mpls-te resv-err 
命令功能 : 
打开或关闭MPLS-TE的resv-err调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te resv-err 
 
no debug mpls-te resv-err 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的resv-err debug开关
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te resv-err MPLS-TE resv error debugging is on
相关命令 : 
无
## debug mpls-te resv-tear 

debug mpls-te resv-tear 
命令功能 : 
打开或关闭MPLS-TE的resv-tear调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te resv-tear 
 
no debug mpls-te resv-tear 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的resv-tear debug开关
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te resv-tear MPLS-TE resv tear debugging is on
相关命令 : 
无
## debug mpls-te signalling 

debug mpls-te signalling 
命令功能 : 
MPLS-TE signalling消息的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te signalling 
 
no debug mpls-te signalling 
命令参数解释 : 
					无
				 
缺省 : 
不打开RSVP的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te signalling MPLS-TE signalling debugging is on
相关命令 : 
无
## debug mpls-te state 

debug mpls-te state 
命令功能 : 
打开TE_MP STEMG组件的debug开关，使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te state 
 
no debug mpls-te state 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te stateMPLS-TE state debugging is on
相关命令 : 
show debug te-mp 
## debug mpls-te static-forwarding-management 

debug mpls-te static-forwarding-management 
命令功能 : 
打开MPLS-TE  静态隧道转发管理的相关调试信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te static-forwarding-management 
 
no debug mpls-te static-forwarding-management 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息 
使用说明 : 
无 
范例 : 
开启static-forwarding-management的debug开关：ZXROSNG#debug mpls-te static-forwarding-managementMPLS-TE static forwarding management debugging is on
相关命令 : 
无 
## debug mpls-te static-tunnel-management 

debug mpls-te static-tunnel-management 
命令功能 : 
打开MPLS-TE  静态隧道管理的相关调试信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te static-tunnel-management 
 
no debug mpls-te static-tunnel-management 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息 
使用说明 : 
无 
范例 : 
开启static-tunnel-management的debug开关：ZXROSNG#debug mpls-te static-tunnel-managementMPLS-TE static tunnel management debugging is on
相关命令 : 
无 
## debug mpls-te temib 

debug mpls-te temib 
命令功能 : 
打开MPLS-TE TEMIB组件的相关调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te temib 
 
no debug mpls-te temib 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te temib     MPLS-TE temib message debugging is onZXROSNG#no debug mpls-te temib                                                   MPLS-TE temib message debugging is off
相关命令 : 
无 
## debug mpls-te timer 

debug mpls-te timer 
命令功能 : 
MPLS-TE timer消息的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te timer 
 
no debug mpls-te timer 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的调试信息
使用说明 : 
无 
范例 : 
ZXROSNG#debug mpls-te timer MPLS-TE timer debugging is on
相关命令 : 
无
## debug mpls-te topology-change 

debug mpls-te topology-change 
命令功能 : 
MPLS-TE topology change事件的调试信息
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te topology-change 
 
no debug mpls-te topology-change 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE的topology-change调试信息
使用说明 : 
无
范例 : 
ZXROSNG#debug mpls-te topology-change RSVP topology-change debugging is on
相关命令 : 
无
## debug mpls-te tunnel-management 

debug mpls-te tunnel-management 
命令功能 : 
打开MPLS-TE  隧道管理的相关调试信息 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug mpls-te tunnel-management 
 
no debug mpls-te tunnel-management 
命令参数解释 : 
					无
				 
缺省 : 
不打开MPLS-TE tunnel-management的调试信息 
使用说明 : 
无 
范例 : 
开启tunnel-management的debug开关：ZXROSNG#debug mpls-te tunnel-managementMPLS-TE tunnel-management debugging is on
相关命令 : 
无 
## debug rsmgr all 

debug rsmgr all 
命令功能 : 
打开RSMGR相关的所有的debug开关，使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug rsmgr all 
 
no debug rsmgr all 
命令参数解释 : 
					无
				 
缺省 : 
默认情况下不打开RSMGR相关的所有的debug开关。 
使用说明 : 
无 
范例 : 
ZXROSNG#debug rsmgr allAll RSMGR debugging has been turned on
相关命令 : 
show debug rsmgr 
## debug rsmgr interface 

debug rsmgr interface 
命令功能 : 
打开RSMGR接口相关功能的debug开关，使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug rsmgr interface 
 
no debug rsmgr interface 
命令参数解释 : 
					无
				 
缺省 : 
默认情况下不打开RSMGR接口相关功能的debug开关。 
使用说明 : 
无 
范例 : 
ZXROSNG#debug rsmgr interfaceRSMGR interface debugging is on
相关命令 : 
show debug rsmgr 
## debug rsmgr pw 

debug rsmgr pw 
命令功能 : 
打开RSMGR PW相关功能的debug开关，使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug rsmgr pw 
 
no debug rsmgr pw 
命令参数解释 : 
					无
				 
缺省 : 
默认情况下不打开RSMGR PW相关功能的debug开关。 
使用说明 : 
无 
范例 : 
ZXROSNG#debug rsmgr pwRSMGR PW debugging is on
相关命令 : 
show debug rsmgr 
## debug rsmgr section 

debug rsmgr section 
命令功能 : 
打开RSMGR section相关功能的debug开关，使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug rsmgr section 
 
no debug rsmgr section 
命令参数解释 : 
					无
				 
缺省 : 
默认情况下不打开RSMGR section相关功能的debug开关。 
使用说明 : 
无 
范例 : 
ZXROSNG#debug rsmgr sectionRSMGR section debugging is on
相关命令 : 
ZXROSNG#debug rsmgr sectionRSMGR section debugging is on
## debug rsmgr tunnel 

debug rsmgr tunnel 
命令功能 : 
打开RSMGR 隧道相关功能的debug开关，使用no命令关闭开关。 
命令模式 : 
 特权模式  
命令默认权限级别 : 
2 
命令格式 : 
debug rsmgr tunnel 
 
no debug rsmgr tunnel 
命令参数解释 : 
					无
				 
缺省 : 
默认情况下不打开RSMGR 隧道相关功能的debug开关。 
使用说明 : 
无 
范例 : 
ZXROSNG#debug rsmgr tunnelRSMGR tunnel debugging is on
相关命令 : 
show debug rsmgr 
## ds-te te-class 

ds-te te-class 
命令功能 : 
配置TE-CLASS映射关系，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
ds-te te-class 
  ＜te-class map id 
＞ class-type 
 ＜class type value 
＞ priority 
 ＜preemption priority value 
＞
no ds-te te-class 
  ＜te-class map id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜te-class map id＞|用户配置的te-class，范围：0–7
＜class type value＞|用户配置的class type，范围：0–7
＜preemption priority value＞|用户配置的优先级，范围：0–7
缺省 : 
无映射关系。 
使用说明 : 
该命令依赖于ds-te模型，只有配置了模型（除MPLS-TE模型），才能进行配置。 
范例 : 
1.配置ct为0优先级为1的te-class：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#ds-te te-class 0 class-type 0 priority 12.去使能ct为0的te-class：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#no ds-te te-class 0
相关命令 : 
bandwidth model {mpls-te|extend-mam|mam|rdm|non-te}show te-class-mapping
## exclude-address 

exclude-address 
命令功能 : 
配置流量工程某条显式路径的下一跳排除地址 
命令模式 : 
 MPLS-TE显式路径ID模式  
命令默认权限级别 : 
15 
命令格式 : 
exclude-address 
  {interface 
 ＜ip-address 
＞|router-id 
 ＜ip-address 
＞}
命令参数解释 : 
参数|描述
---|---
interface|配置排除的接口
＜ip-address＞|配置排除的地址，十进制点分形式
router-id|配置排除的router_id
＜ip-address＞|配置排除的地址，十进制点分形式
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
配置一条ID为1的显式路径，进入显示路径ID模式 ，配置排除router_id地址ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path id 1ZXROSNG(config-mpls-te-expl-path-id-1)#ZXROSNG(config-mpls-te-expl-path-id-1)#exclude-address router-id 100.1.1.1
相关命令 : 
无 
## exclude-address 

exclude-address 
命令功能 : 
配置流量工程某条显式路径的下一跳排除地址 
命令模式 : 
 MPLS-TE显式路径NAME模式  
命令默认权限级别 : 
15 
命令格式 : 
exclude-address 
  {interface 
 ＜ip-address 
＞|router-id 
 ＜ip-address 
＞}
命令参数解释 : 
参数|描述
---|---
interface|配置排除的接口
＜ip-address＞|配置排除的地址，十进制点分形式
router-id|配置排除的router_id
＜ip-address＞|配置排除的地址，十进制点分形式
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
配置一条名字为test的显式路径，进入显示路径name模式 ，配置排除router_id地址ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path name testZXROSNG(config-mpls-te-expl-path-name)#ZXROSNG(config-mpls-te-expl-path-name)#exclude-address router-id 100.1.1.1
相关命令 : 
无 
## explicit-path identifier 

explicit-path identifier 
命令功能 : 
配置流量工程某条显式路径的ID 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
explicit-path identifier 
  ＜explicit-path-identifier-id 
＞
no explicit-path identifier 
  ＜explicit-path-identifier-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜explicit-path-identifier-id＞|显示路径标记，范围：1–65535，进入显示路径identity模式
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path id 1ZXROSNG(config-mpls-te-expl-path-id-1)#
相关命令 : 
无 
## explicit-path name 

explicit-path name 
命令功能 : 
配置流量工程某条显式路径的NAME 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
explicit-path name 
  ＜explicit-path-name 
＞
no explicit-path name 
  ＜explicit-path-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜explicit-path-name＞|显示路径名称，长度1-64个字符，进入显示路径name模式
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path name testZXROSNG(config-mpls-te-expl-path-name)#
相关命令 : 
无 
## forwarding-adjacency holdtime 

forwarding-adjacency holdtime 
命令功能 : 
在静态隧道上，使能FA并设置保存时间。使用no命令去使能FA。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
forwarding-adjacency holdtime 
  ＜mpls-te-down-holdtime 
＞
命令参数解释 : 
参数|描述
---|---
＜mpls-te-down-holdtime＞|保持时间，范围：0–4294967295
缺省 : 
静态隧道没有使能fa功能。 
使用说明 : 
该命令与静态隧道autoroute功能互斥。 
范例 : 
1.使能静态隧道te_tunnel1的FA功能，并设置保存时间为300：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#forwarding-adjacency holdtime 3002.去使能静态隧道te_tunnel1的FA功能：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#no forwarding-adjacency
相关命令 : 
autoroute announceshow mpls traffic-eng static | include Forwarding adjacency
## forwarding-adjacency include-ipv6 

forwarding-adjacency include-ipv6 
命令功能 : 
在静态隧道的FA  IPv6属性。使用no命令关闭FA IPv6属性。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
forwarding-adjacency include-ipv6 
 
no forwarding-adjacency include-ipv6 
命令参数解释 : 
					无
				 
缺省 : 
不使能 
使用说明 : 
该命令与静态态隧道autoroute功能互斥。配置了该条命令也同时使能了FA属性。
范例 : 
使能静态隧道te_tunnel1的FA  IPv6功能：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te- static te_tunnel1)#forwarding-adjacency include-ipv6
相关命令 : 
autoroute announceshow mpls traffic-eng static forwarding adjacency
## forwarding-adjacency 

forwarding-adjacency 
命令功能 : 
在静态隧道上，使能fa功能，使用no命令关闭fa功能。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
forwarding-adjacency 
 
no forwarding-adjacency 
命令参数解释 : 
					无
				 
缺省 : 
静态隧道没有使能fa功能。 
使用说明 : 
该命令与静态隧道autoroute功能互斥。 
范例 : 
1.使能静态隧道te_tunnel1的fa功能：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#forwarding-adjacency2.去使能静态隧道te_tunnel1的fa功能：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#no forwarding-adjacency
相关命令 : 
autoroute announceshow mpls traffic-eng static | include Forwarding adjacency
## index 

index 
命令功能 : 
配置流量工程某条显式路径按索引配置下一跳地址 
命令模式 : 
 MPLS-TE显式路径ID模式  
命令默认权限级别 : 
15 
命令格式 : 
index 
  ＜index-number 
＞ {next-address 
 {loose 
 ＜ip-address 
＞|strict 
 ＜ip-address 
＞} [if-id 
 ＜ip-address 
＞]|exclude-address 
 {interface 
 ＜ip-address 
＞|router-id 
 ＜ip-address 
＞}|avoid-address 
 {interface 
 ＜ip-address 
＞|router-id 
 ＜ip-address 
＞}}
no index 
  ＜index-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜index-number＞|显示路径某一跳的索引值，取值范围：1-64
next-address|配置下一跳的地址
loose|松散方式通过
＜ip-address＞|配置的地址，十进制点分形式
strict|严格方式通过
＜ip-address＞|配置的地址，十进制点分形式
＜ip-address＞|配置的地址，十进制点分形式
exclude-address|配置排除地址
interface|排除的是接口地址
＜ip-address＞|配置的地址，十进制点分形式
router-id|排除的是router id地址
＜ip-address＞|配置的地址，十进制点分形式
avoid-address|尽力排除地址
interface|排除的是接口地址
＜ip-address＞|配置的地址，十进制点分形式
router-id|排除的是router id地址
＜ip-address＞|配置的地址，十进制点分形式
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
配置一条ID为1的显式路径，进入显示路径ID模式 ，index方式配置地址ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path id 1ZXROSNG(config-mpls-te-expl-path-id-1)#ZXROSNG(config-mpls-te-expl-path-id-1)#index 5 next-address strict 10.1.1.1
相关命令 : 
无 
## index 

index 
命令功能 : 
配置流量工程某条显式路径按索引配置下一跳地址 
命令模式 : 
 MPLS-TE显式路径NAME模式  
命令默认权限级别 : 
15 
命令格式 : 
index 
  ＜index-number 
＞ {next-address 
 {loose 
 ＜ip-address 
＞|strict 
 ＜ip-address 
＞} [if-id 
 ＜ip-address 
＞]|exclude-address 
 {interface 
 ＜ip-address 
＞|router-id 
 ＜ip-address 
＞}|avoid-address 
 {interface 
 ＜ip-address 
＞|router-id 
 ＜ip-address 
＞}}
no index 
  ＜index-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜index-number＞|显示路径某一跳的索引值，取值范围：1-64
next-address|配置下一跳的地址
loose|松散方式通过
＜ip-address＞|配置的地址，十进制点分形式
strict|严格方式通过
＜ip-address＞|配置的地址，十进制点分形式
＜ip-address＞|配置的地址，十进制点分形式
exclude-address|配置排除地址
interface|排除的是接口地址
＜ip-address＞|配置的地址，十进制点分形式
router-id|排除的是router id地址
＜ip-address＞|配置的地址，十进制点分形式
avoid-address|尽力排除地址
interface|排除的是接口地址
＜ip-address＞|配置的地址，十进制点分形式
router-id|排除的是router id地址
＜ip-address＞|配置的地址，十进制点分形式
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
配置一条名字为test的显式路径，进入显示路径name模式 ，index方式配置地址ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path name testZXROSNG(config-mpls-te-expl-path-name)#ZXROSNG(config-mpls-te-expl-path-name)# index 5 next-address strict 10.1.1.1
相关命令 : 
无 
## ingress-tunnel-id 

ingress-tunnel-id 
命令功能 : 
配置MPLS-TE静态隧道基本信息。使用no命令删除该隧道的基本信息配置。
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ingress-tunnel-id 
  ＜ingress-static-tunnel-id 
＞ ingress 
 ＜ip-address 
＞ egress 
 ＜ip-address 
＞
no ingress-tunnel-id 
命令参数解释 : 
参数|描述
---|---
＜ingress-static-tunnel-id＞|头节点静态隧道Tunnel ID，范围：1~264192
＜ip-address＞|尾节点LSR ID
＜ip-address＞|尾节点LSR ID
缺省 : 
无 
使用说明 : 
(1)未配置router ID，不能配置隧道三元组。(2)只有配置了隧道类型之后，才能配置隧道三元组。
范例 : 
1.创建隧道三元组：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.32.删除隧道三元组：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#no ingress-tunnel-id
相关命令 : 
role {ingress|transit|egress} type {unidirectional|bidirectional}show mpls traffic-eng static
## in-seg 

in-seg 
命令功能 : 
配置静态P2MP隧道LSP的入段转发信息。使用no命令删除入段转发信息配置 
命令模式 : 
 MPLS-TE静态P2MP隧道LSP模式  
命令默认权限级别 : 
15 
命令格式 : 
in-seg 
 in-port 
 ＜in-port 
＞ in-label 
 ＜in-label 
＞
no in-seg 
命令参数解释 : 
参数|描述
---|---
＜in-port＞|静态P2MP隧道LSP入接口名
＜in-label＞|静态P2MP隧道LSP入标签 ，范围：16-1048575
缺省 : 
无 
使用说明 : 
根节点静态P2MP隧道不能配置LSP的入段转发信息。 
范例 : 
配置静态P2MP隧道的入段，入接口为gei-0/1/0/1，入标签为55：ZXROSNG(config#mpls traffic-engZXROSNG(config-mpls-te)# static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static -mte_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static -mte_tunnel1-lsp)#in-seg in-port gei-0/1/0/1 in-label 55 
相关命令 : 
无 
## in-seg-info 

in-seg-info 
命令功能 : 
配置MPLS-TE静态隧道LSP的正向入段转发信息。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
in-seg-info 
 in-port 
 ＜in-port 
＞ in-label 
 ＜in-label 
＞ [prev-hop 
 ＜ip-address 
＞]
no in-seg-info 
命令参数解释 : 
参数|描述
---|---
＜in-port＞|隧道LSP正向入接口名称
＜in-label＞|隧道LSP正向入标签，范围：<16-1048575,or 0,3>
＜ip-address＞|隧道LSP正向入接口的上一跳IP地址
缺省 : 
无 
使用说明 : 
1.只有在配置了隧道类型和三元组之后，才能创建LSP，配置正向入端信息。2. 如果2条TE静态隧道在同一个保护组中，不能配置嵌套关系。
范例 : 
1.设置正向入接口为gei-0/1/0/1，正向入标签为55：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#in-seg-info in-port gei-0/1/0/1 in-label 552.删除正向入端：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#no in-seg-info
相关命令 : 
role {ingress|transit|egress} type {unidirectional|bidirectional}ingress-tunnel-id <access-tunnel-id-ingress> ingress <ip-address> egress <ip-address>show mpls traffic-eng static
interface : 

interface (MPLS-TE模式) 
命令功能 : 
使能该接口的TE属性，并进入到TE接口配置模式。使用no命令清除该接口的TE属性。 
命令模式 : 
 MPLS-TE模式  
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
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#
相关命令 : 
无 
## ipv6-router-id 

ipv6-router-id 
命令功能 : 
配置TE_MP的IPv6 router ID，使用no 命令清除TE_MP的IPv6 router ID。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6-router-id 
  ＜ipv6-address 
＞
no ipv6-router-id 
命令参数解释 : 
参数|描述
---|---
＜ipv6-address＞|IPv6 router ID
缺省 : 
无 
使用说明 : 
隧道配置了IPv6类型的三元组后，不能修改或者删除IPv6 router ID。 
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#ipv6-router-id 11::11
相关命令 : 
无 
## leaf 

leaf 
命令功能 : 
使能静态P2MP隧道叶子节点功能。使用no命令去使能静态P2MP隧道叶子节点功能。 
命令模式 : 
 MPLS-TE静态P2MP隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
leaf 
 
no leaf 
命令参数解释 : 
					无
				 
缺省 : 
没有配置leaf。 
使用说明 : 
只有非根节点静态P2MP隧道可以使能叶子节点功能。 
范例 : 
配置静态P2MP隧道的leaf功能：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static -mte_tunnel1)#role unrootZXROSNG(config-mpls-te-static -mte_tunnel1)#leaf
相关命令 : 
role 
## list 

list 
命令功能 : 
将显式路径的配置显示出来 
命令模式 : 
 MPLS-TE显式路径ID模式  
命令默认权限级别 : 
15 
命令格式 : 
list 
  [＜index-num 
＞]
命令参数解释 : 
参数|描述
---|---
＜index-num＞|显示具体某个索引值的显式路径配置
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
配置一条ID为1的显式路径，其下有2个地址的配置，进入显示路径ID模式 ，list命令显示当前配置：ZXROSNG(config-mpls-te-expl-path-id-1)#list PATH identifier 1   1: next-address 30.40.1.4 strict  2: next-address 30.40.3.4 strictZXROSNG(config-mpls-te-expl-path-id-1)#list 1 PATH identifier 1   1: next-address 30.40.1.4 strictZXROSNG(config-mpls-te-expl-path-id-1)#list ?  <1-64>  List starting at entry index num  <cr>ZXROSNG(config-mpls-te-expl-path-id-1)#list 2 PATH identifier 1   2: next-address 30.40.3.4 strict
相关命令 : 
无 
## list 

list 
命令功能 : 
将显式路径的配置显示出来 
命令模式 : 
 MPLS-TE显式路径NAME模式  
命令默认权限级别 : 
15 
命令格式 : 
list 
  [＜index-num 
＞]
命令参数解释 : 
参数|描述
---|---
＜index-num＞|显示具体某个索引值的显式路径配置
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
配置一条名字为lsp1232的显式路径，其下有2个地址的配置，进入显示路径NAME模式 ，list命令显示当前配置：ZXROSNG(config-mpls-te-expl-path-name)#list PATH name lsp1232   1: next-address 30.40.1.4 strict  2: next-address 30.40.3.4 strict
ZXROSNG(config-mpls-te-expl-path-name)#list 1 PATH name lsp1232   1: next-address 30.40.1.4 strictZXROSNG(config-mpls-te-expl-path-name)#list 2 PATH name lsp1232   2: next-address 30.40.3.4 strict
相关命令 : 
无 
## lsp 

lsp 
命令功能 : 
配置MPLS-TE静态隧道LSP。使用no命令删除该隧道LSP配置。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
lsp 
  ＜lsp-id 
＞
no lsp 
  ＜lsp-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜lsp-id＞|LSP ID，LSP ID的值固定为1
缺省 : 
无 
使用说明 : 
只有在配置了隧道类型和三元组之后，才能创建LSP。 
范例 : 
1.创建LSP：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 12.删除LSP：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#no lsp 1
相关命令 : 
role {ingress|transit|egress} type {unidirectional|bidirectional}ingress-tunnel-id <access-tunnel-id-ingress> ingress <ip-address> egress <ip-address>show mpls traffic-eng static
## lsp 

lsp 
命令功能 : 
配置静态P2MP隧道LSP。使用no命令删除LSP配置。 
命令模式 : 
 MPLS-TE静态P2MP隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
lsp 
  ＜lsp-id 
＞
no lsp 
  ＜lsp-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜lsp-id＞|静态P2MP隧道LSP ID，LSP ID的值固定为1
缺省 : 
无 
使用说明 : 
配置LSP后进入静态P2MP隧道LSP模式。 
范例 : 
配置静态P2MP隧道LSP：ZXROSNG(config#mpls traffic-engZXROSNG(config-mpls-te)# static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static -mte_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static -mte_tunnel1-lsp)#
相关命令 : 
无 
## mpls traffic-eng 

mpls traffic-eng 
命令功能 : 
全局使能TE功能，使用no命令清除该配置。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
mpls traffic-eng 
 
no mpls traffic-eng 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
在使用隧道之前，首先要使用该命令在设备上全局使能TE功能，命令成功后，进入全局TE配置模式。 
范例 : 
ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#
相关命令 : 
无 
## next-address 

next-address 
命令功能 : 
配置流量工程某条显式路径的下一跳 
命令模式 : 
 MPLS-TE显式路径ID模式  
命令默认权限级别 : 
15 
命令格式 : 
next-address 
  {loose 
 ＜ip-address 
＞|strict 
 ＜ip-address 
＞} [if-id 
 ＜ip-address 
＞]
命令参数解释 : 
参数|描述
---|---
loose|表示配置的显式路径可以按照松散的方式到达这个地址
＜ip-address＞|配置的地址，十进制点分形式
strict|表示配置的显式路径必须严格通过这个地址
＜ip-address＞|配置的地址，十进制点分形式
＜ip-address＞|配置的地址，十进制点分形式
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
配置一条ID为1的显式路径，进入显示路径ID模式 ，配置严格下一跳地址ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path id 1ZXROSNG(config-mpls-te-expl-path-id-1)#ZXROSNG(config-mpls-te-expl-path-id-1)#next-address strict 10.1.1.1
相关命令 : 
无 
## next-address 

next-address 
命令功能 : 
配置流量工程某条显式路径的下一跳 
命令模式 : 
 MPLS-TE显式路径NAME模式  
命令默认权限级别 : 
15 
命令格式 : 
next-address 
  {loose 
 ＜ip-address 
＞|strict 
 ＜ip-address 
＞} [if-id 
 ＜ip-address 
＞]
命令参数解释 : 
参数|描述
---|---
loose|表示配置的显式路径可以按照松散的方式到达这个地址
＜ip-address＞|配置的地址，十进制点分形式
strict|表示配置的显式路径必须严格通过这个地址
＜ip-address＞|配置的地址，十进制点分形式
＜ip-address＞|配置的地址，十进制点分形式
缺省 : 
缺省情况下没有任何显式路径 
使用说明 : 
无 
范例 : 
配置一条名字为test的显式路径，进入显示路径name模式 ，配置严格下一跳地址ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#explicit-path name testZXROSNG(config-mpls-te-expl-path-name)#ZXROSNG(config-mpls-te-expl-path-name)#next-address strict 10.1.1.1
相关命令 : 
无 
## next-hop routing without-cspf 

next-hop routing without-cspf 
命令功能 : 
开启MPLS TE隧道中间节点对于严格下一跳路径，不需要CSPF路由计算，直接生成ERO功能 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
next-hop routing without-cspf 
 
no next-hop routing without-cspf 
命令参数解释 : 
					无
				 
缺省 : 
关闭该功能（即MPLS-TE动态隧道的中间节点依赖CSPF路由计算的结果来生成ERO信息） 
使用说明 : 
开启该功能后，MPLS-TE动态隧道的中间节点对于严格下一跳路径，不需要CSPF路由计算，直接生成ERO。 关闭该功能后，MPLS-TE动态隧道的中间节点则依赖CSPF路由计算的结果来生成ERO信息。
范例 : 
开启MPLS-TE动态隧道中间节点对于严格下一跳路径，不需要CSPF路由计算，直接生成ERO功能ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#next-hop routing without-cspf
相关命令 : 
无 
## out-seg convergence-ratio mode 

out-seg convergence-ratio mode 
命令功能 : 
配置MPLS-TE静态隧道LSP正向出段的收敛比模式，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
out-seg convergence-ratio mode 
  {inherit 
|config 
}
no out-seg convergence-ratio mode 
命令参数解释 : 
参数|描述
---|---
inherit|继承模式
config|配置模式
缺省 : 
无 
使用说明 : 
1.区分正反向，即双向隧道正反两个方向可以各自配置收敛模式；2.继承模式下，隧道的收敛比继承自它的出接口上的收敛比；3.模式切换时，如果该隧道有带宽预留或者可以进行带宽预留，则需发起带宽CAC校验流程；校验成功则模式切换成功，否则失败，并由MIM回滚之前的配置。
范例 : 
1.配置静态隧道LSP正向出段的收敛比模式为继承模式：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg convergence-ratio mode inherit2.删除静态隧道LSP正向出段的收敛比模式：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#no out-seg convergence-ratio mode
相关命令 : 
out-seg convergence-ratio valueshow mpls traffic-eng static [tunnel-id <tunnel-id>] | include Convergence-Ratio
## out-seg convergence-ratio value 

out-seg convergence-ratio value 
命令功能 : 
配置MPLS-TE静态隧道LSP正向出段的收敛比值，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
out-seg convergence-ratio value 
  ＜value 
＞
no out-seg convergence-ratio value 
命令参数解释 : 
参数|描述
---|---
＜value＞|静态隧道收敛比数值，范围：1-100，单位: percent
缺省 : 
默认收敛比为100。 
使用说明 : 
1.若收敛比模式为配置模式时，各自配置LSP正反两个方向的收敛比值。若为继承模式，则两个方向的收敛比分别继承各自的出接口。2.只有在配置模式下才能配置收敛比数值。继承模式或未指定模式时，如果配置则报错。3.no掉收敛比模式时收敛比数值恢复默认100。4.不配置模式时或配置模式不配置收敛比值时，隧道收敛比为默认100。5.收敛比数值改变时，如果该隧道有带宽预留或者可以进行带宽预留，则需发起带宽CAC校验流程；校验成功则收敛比数值修改成功，否则失败。
范例 : 
1.配置静态隧道的收敛比数值为90：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg convergence-ratio mode configZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg convergence-ratio value 902.删除静态隧道的收敛比数值：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#no out-seg convergence-ratio value
相关命令 : 
out-seg convergence-ratio mode configshow mpls traffic-eng static [tunnel-id <tunnel-id>] | include Convergence-Ratio
## out-seg 

out-seg 
命令功能 : 
配置静态P2MP隧道LSP的出段转发信息。 
命令模式 : 
 MPLS-TE静态P2MP隧道LSP模式  
命令默认权限级别 : 
15 
命令格式 : 
out-seg 
  ＜out-seg-id 
＞ out-port 
 ＜out-port 
＞ out-label 
 ＜out-label 
＞ [next-hop 
 ＜ip-address 
＞]
no out-seg 
  ＜out-seg-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜out-seg-id＞|静态P2MP隧道LSP出段ID，范围：1-32
＜out-port＞|静态P2MP隧道LSP出接口名
＜out-label＞|静态P2MP隧道LSP出标签，范围：16-1048575
＜ip-address＞|静态P2MP隧道LSP下一跳IP地址
缺省 : 
无 
使用说明 : 
静态P2MP隧道最多可以配置32个出段。 
范例 : 
配置静态P2MP隧道的出段，出段ID为1，出接口为gei-0/1/0/1，出标签为17，下一跳为102.3.4.5：ZXROSNG(config#mpls traffic-engZXROSNG(config-mpls-te)# static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static -mte_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static -mte_tunnel1-lsp)#out-seg 1 out-port gei-0/1/0/1 out-label 17 next-hop 102.3.4.5
相关命令 : 
无 
## out-seg-ct 

out-seg-ct 
命令功能 : 
配置静态隧道的正向出段CT带宽。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
out-seg-ct 
 class-type 
 ＜class-type 
＞ bandwidth 
 ＜ct-bandwidth 
＞ [{kbps 
|mbps 
|gbps 
}]
no out-seg-ct 
 class-type 
 ＜class-type 
＞
				
命令参数解释 : 
参数|描述
---|---
＜class-type＞|CT类型，范围：0-7
＜ct-bandwidth＞|CT类型下的带宽值，范围：1-4294967295，默认单位kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
缺省 : 
静态隧道默认没有CT带宽。 
使用说明 : 
1.要配置静态LSP的CT带宽，必须先配置其出接口，请参见命令out-seg-info；2.静态隧道能否配置CT带宽及配置的个数，请参见命令bandwidth model；3.静态隧道的建立优先级和保持优先级默认为0，隧道建立优先级和保持优先级分别和其下的CT配置两两组合，在te-class映射配置中查找必须要有匹配项。请参见命令ds-te te-class；4.CT带宽配置与普通带宽配置/带宽共享隧道配置普通带宽和CT带宽配置是互斥的，请参见命令out-seg-info。
范例 : 
1.配置ct带宽（不带单位）：ZXROSNG(config)#mpls trafficZXROSNG(config-mpls-te)#bandwidth model extend-mamZXROSNG(config-mpls-te)#ds-te te-class 0 class-type 0 priority 0ZXROSNG(config-mpls-te)#ds-te te-class 1 class-type 1 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 2 class-type 2 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 3 class-type 3 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 4 class-type 4 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 5 class-type 5 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 6 class-type 6 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 7 class-type 7 priority 0                 ZXROSNG(config-mpls-te)#router-id 1.1.1.1ZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#bandwidth static 40000 bc0 10000 bc1 10000 bc2 10000 bc3 10000ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#exitZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#role ingress type unidirectionalZXROSNG(config-mpls-te-static-te_tunnel1)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg-info out-port gei-0/1/0/1 out-label 20ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg-ct class-type 0 bandwidth 10000ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg-ct class-type 1 bandwidth 10000ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg-ct class-type 2 bandwidth 10000ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg-ct class-type 3 bandwidth 100002.删除ct带宽：ZXROSNG(config)#mpls trafficZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#no out-seg-ct class-type 03.配置ct带宽（带非默认单位）：ZXROSNG(config)#mpls trafficZXROSNG(config-mpls-te)#bandwidth model extend-mamZXROSNG(config-mpls-te)#ds-te te-class 0 class-type 0 priority 0      ZXROSNG(config-mpls-te)#router-id 1.1.1.1ZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#bandwidth static 40000 bc0 10000 ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#exitZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#role ingress type unidirectionalZXROSNG(config-mpls-te-static-te_tunnel1)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg-info out-port gei-0/1/0/1 out-label 20ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg-ct class-type 0 bandwidth 10 mbpsZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#show thisout-seg-ct class-type 0 bandwidth 10000
相关命令 : 
1.bandwidth model2.out-seg-info out-port3.ds-te te-class4.show rsvp bandwidth interface
## out-seg-info 

out-seg-info 
命令功能 : 
配置MPLS-TE静态隧道LSP的正向出段转发信息。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
out-seg-info 
 out-port 
 ＜out-port 
＞ out-label 
 ＜out-label 
＞ [next-hop 
 ＜ip-address 
＞] [bandwidth-share 
 ＜bandwidth-share tunnel 
＞] [bandwidth 
 {＜committed-information-rate 
＞|＜committed-information-rate 
＞} [{kbps 
|mbps 
|gbps 
}] [{[burst 
 ＜committed-burst-size 
＞ [{byte 
|kb 
|mb 
}]],[peak 
 ＜peak-information-rate 
＞ [{kbps 
|mbps 
|gbps 
}]],[excess-burst 
 ＜excess-burst-size 
＞ [{byte 
|kb 
|mb 
}]]}]]
no out-seg-info 
命令参数解释 : 
参数|描述
---|---
＜out-port＞|隧道LSP正向出接口名称
＜out-label＞|隧道LSP正向出标签，范围：<16-1048575,or 0,3>
＜ip-address＞|隧道LSP正向下一跳地址
＜bandwidth-share tunnel＞|共享带宽的静态隧道接口名称，隧道ID范围在运行的时候从项目的性能参数中取值
＜committed-information-rate＞|隧道LSP承诺带宽，范围：$#100794375#$~$#100794376#$，默认单位：kbit/s
＜committed-information-rate＞|隧道LSP承诺带宽，范围：$#100794375#$~$#100794376#$，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜committed-burst-size＞|隧道LSP承诺突发尺寸，范围：$#100794381#$~$#100794382#$，默认单位：byte
byte|以BYTE为单位
kb|以KB为单位
mb|以MB为单位
＜peak-information-rate＞|隧道LSP峰值速率，范围：$#100794378#$~$#100794379#$，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜excess-burst-size＞|隧道LSP超额突发尺寸，范围：$#100794384#$~$#100794385#$，默认单位：byte
byte|以BYTE为单位
kb|以KB为单位
mb|以MB为单位
缺省 : 
无
使用说明 : 
1.只有在配置了隧道类型和三元组之后，才能创建LSP，配置正向出段信息。2.如果2条TE静态隧道在同一个保护组中，不能配置嵌套关系。
范例 : 
1.设置正向出接口为gei-0/1/0/3，正向出标签为75：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#out-seg-info out-port gei-0/1/0/3 out-label 752.删除正向出段：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#no out-seg-info3.配置te_tunnel1正向出段带宽(带非默认单位)：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#role ingress type unidirectionalZXROSNG(config-mpls-te-static-te_tunnel1)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#out-seg-info out-port gei-0/1/0/3 out-label 75 bandwidth 10 gbpsZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#show thisout-seg-info out-port gei-0/1/0/3 out-label 75 bandwidth 10000000
相关命令 : 
role {ingress|transit|egress} type {unidirectional|bidirectional}ingress-tunnel-id <access-tunnel-id-ingress> ingress <ip-address> egress <ip-address>show mpls traffic-eng static
## passive-interface 

passive-interface 
命令功能 : 
配置接口的passive-interface跨域属性；使用no命令取消该设置。 
命令模式 : 
 MPLS-TE接口模式  
命令默认权限级别 : 
15 
命令格式 : 
passive-interface 
 nbr-te-id 
 ＜neighbor id 
＞ [{[nbr-if-addr 
 ＜neighbor ip 
＞],[nbr-igp-id 
 {ospf 
 ＜ospf id 
＞|isis 
 ＜isis id 
＞}]}]
no passive-interface 
 nbr-te-id 
 ＜neighbor id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜neighbor id＞|nbr-te-id 链路对端的邻居路由器的TE RouterID
＜neighbor ip＞|nbr-igp-id 远程ASBR的接口地址（不配置时，默认为邻居路由器的TE RouterID）
＜ospf id＞|ospf邻居的OSPF的RouterID
＜isis id＞|isis邻居的ISIS的sysID
缺省 : 
无 
使用说明 : 
无 
范例 : 
1.配置接口的passive-interface跨域属性:ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#passive-interface nbr-te-id  1.1.1.1 nbr-if-addr 10.10.10.1 nbr-igp-id isis aaaa.aaaa.aaaa2.去配置接口的passive-interface跨域属性:ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#no passive-interface nbr-te-id 1.1.1.1
相关命令 : 
无 
## pce-path-compute 

pce-path-compute 
命令功能 : 
所有隧道使能PCE算路功能，通过no命令关闭该功能。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
pce-path-compute 
 
no pce-path-compute 
命令参数解释 : 
					无
				 
缺省 : 
默认没有开启PCE算路功能。 
使用说明 : 
如果使能了PCE算路，但是没有算路结果的时候，也不会再启用本地算路。 
范例 : 
ZXROSNG(config)#ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#pce-path-compute 
相关命令 : 
无 
## perf-switch 

perf-switch 
命令功能 : 
打开或关闭静态隧道性能统计开关。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
perf-switch 
  {on 
|off 
}
命令参数解释 : 
参数|描述
---|---
on|打开静态隧道性能统计开关
off|关闭静态隧道性能统计开关
缺省 : 
关闭静态隧道性能统计开关。 
使用说明 : 
无 
范例 : 
1.打开静态隧道性能统计开关：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#perf-switch on2.关闭静态隧道性能统计开关：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#perf-switch off
相关命令 : 
show mpls traffic-eng resource static-tunnel perf-switchshow mpls traffic-eng static [tunnel-id <tunnel-id>] | include Perf Switch
## policy-class 

policy-class 
命令功能 : 
配置TE静态隧道策略类别，使用no命令关闭该功能。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
policy-class 
  {default 
|*(＜policy-class 
＞)}
no policy-class 
  [*(＜policy-class 
＞)]
				
命令参数解释 : 
参数|描述
---|---
default|一种特殊的策略类别。用于转发“没有匹配到对应策略类别的TE隧道”的报文。
＜policy-class＞|0~7的整数，设置当前TE隧道的策略类别。用于转发类别（IP报文使用IP优先级，MPLS报文使用EXP值）为该值的报文。
缺省 : 
无
使用说明 : 
必须在静态隧道配置了类型和角色之后，才能设置策略类别，且和DSTE配置互斥。 
范例 : 
1.配置TE隧道的策略类别为1 5：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#role ingress type unidirectional ZXROSNG(config-mpls-te-static-te_tunnel1)#policy-class 1 52.删除TE隧道的策略类别5：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#no policy-class 53.删除所有TE隧道的策略类别：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#no policy-class
相关命令 : 
role {transit|egress} type {unidirectional|bidirectional}show mpls traffic-eng static [tunnel-id <tunnel-id>]| include Policy Classshow mpls traffic-eng tunnels policy-class
## rate-limit 

rate-limit 
命令功能 : 
配置静态隧道的限速，使用no命令取消该配置。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
rate-limit 
 mode 
 {blind 
|aware 
} cir 
 ＜cir 
＞ [{kbps 
|mbps 
|gbps 
}] cbs 
 ＜cbs 
＞ [{kb 
|mb 
|gb 
}] pir 
 ＜pir 
＞ [{kbps 
|mbps 
|gbps 
}] pbs 
 ＜pbs 
＞ [{kb 
|mb 
|gb 
}]
no rate-limit 
命令参数解释 : 
参数|描述
---|---
blind|色盲模式
aware|色敏感模式
＜cir＞|允诺令牌速率，取值范围：$#100794399#$~$#100794400#$，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜cbs＞|允诺令牌桶尺寸，范围：$#100794401#$~$#100794402#$，默认单位：KB
kb|以KB为单位
mb|以MB为单位
gb|以GB为单位
＜pir＞|峰值令牌速率，范围：$#100794403#$~$#100794404#$，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜pbs＞|峰值令牌桶尺寸，范围：$#100794405#$~$#100794406#$，默认单位：KB
kb|以KB为单位
mb|以MB为单位
gb|以GB为单位
缺省 : 
无 
使用说明 : 
1.只有头节点隧道或双向尾节点隧道可以配置限速。2.rate-limit命令依赖隧道role type的配置。3.与静态隧道lsp下的bandwdith相互覆盖，和class-type bandwidth配置互斥
范例 : 
1.将通过隧道tunnel1的流量控制在100Mbps，允许突发到150Mbps（不带单位）：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#rate-limit mode blind cir 100000 cbs 200 pir 150000 pbs 3002.删除隧道tunnel1限速配置：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#no rate-limit3.与静态隧道下lsp带宽相互覆盖(与class-type bandwidth是互斥)先配置了带宽ZXROSNG(config)#show running-config-interface te_tunnel1!<if-intf>interface te_tunnel1$!</if-intf>!<mpls-te>mpls traffic-enginterface gei-0/1/0/1bandwidth static 100$static te_tunnel1role ingress type unidirectionalingress-tunnel-id 1 ingress 1.2.3.4 egress 4.3.2.1lsp 1out-seg-info out-port gei-0/1/0/1 out-label 20 bandwidth 20$$$!</mpls-te>再配置限速ZXROSNG(config-mpls-te-static-te_tunnel1)# rate-limit mode aware cir 8 cbs 8 pir 8 pbs 8带宽被删除ZXROSNG#show running-config-interface te_tunnel1!<if-intf>interface te_tunnel1$!</if-intf>!<mpls-te>mpls traffic-enginterface gei-0/1/0/1bandwidth static 100$static te_tunnel1role ingress type unidirectionalingress-tunnel-id 1 ingress 1.2.3.4 egress 4.3.2.1rate-limit mode aware cir 8 cbs 8 pir 8 pbs 8lsp 1out-seg-info out-port gei-0/1/0/1 out-label 20$$$!</mpls-te>4.将通过隧道tunnel1的流量控制在100Mbps，允许突发到150Mbps（带非默认单位）：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#rate-limit mode blind cir 100 mbps cbs 200 pir 150 mbps pbs 300ZXROSNG(config-mpls-te-static-te_tunnel1)#show thisrate-limit mode blind cir 100000 cbs 200 pir 150000 pbs 300
相关命令 : 
show mpls traffic-eng static 
## role 

role 
命令功能 : 
配置MPLS-TE静态隧道角色和类型，使用no命令删除该隧道的角色和类型配置。
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
role 
  {ingress 
|transit 
|egress 
} type 
 {unidirectional 
|bidirectional 
}
no role 
命令参数解释 : 
参数|描述
---|---
ingress|静态隧道头节点。
transit|静态隧道中间（传输）节点。
egress|静态隧道尾节点。
unidirectional|单向隧道。
bidirectional|双向隧道。
缺省 : 
无 
使用说明 : 
无 
范例 : 
1.创建隧道类型为双向隧道，角色为中间节点：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectional2.删除隧道类型和角色：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#no role
相关命令 : 
show mpls traffic-eng static 
## role 

role 
命令功能 : 
配置静态P2MP隧道角色，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE静态P2MP隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
role 
  {root 
|unroot 
}
no role 
命令参数解释 : 
参数|描述
---|---
root|静态P2MP隧道根节点。
unroot|静态P2MP隧道非根节点。
缺省 : 
无 
使用说明 : 
配置静态P2MP隧道角色为根后不能再配置leaf。 
范例 : 
配置静态P2MP隧道的角色为根：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static -mte_tunnel1)#role root
相关命令 : 
无 
## router-id 

router-id 
命令功能 : 
配置TE_MP的router ID，使用no 命令清除TE_MP的router ID。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
router-id 
  ＜ip-address 
＞
no router-id 
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|router ID
缺省 : 
无 
使用说明 : 
隧道配置了IPv4类型的三元组后，不能修改或者删除IPv4 router ID。 
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2
相关命令 : 
无 
## rvs-in-seg-info 

rvs-in-seg-info 
命令功能 : 
配置MPLS-TE静态隧道LSP的反向入段转发信息。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
rvs-in-seg-info 
 in-port 
 ＜in-port 
＞ in-label 
 ＜in-label 
＞ [prev-hop 
 ＜ip-address 
＞]
no rvs-in-seg-info 
命令参数解释 : 
参数|描述
---|---
＜in-port＞|隧道LSP反向入接口名称
＜in-label＞|隧道LSP反向入标签，范围：<16-1048575,or 0,3>
＜ip-address＞|隧道LSP反向入接口的上一跳IP地址
缺省 : 
无 
使用说明 : 
1.只有在配置了隧道类型和三元组之后，才能创建LSP，配置反向入端信息。2.如果2条TE静态隧道在同一个保护组中，不能配置嵌套关系。
范例 : 
1.设置反向入接口为gei-0/1/0/2，反向入标签为65：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-in-seg-info in-port gei-0/1/0/2 in-label 652.删除反向入端：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#no rvs-in-seg-info
相关命令 : 
role {ingress|transit|egress} type {unidirectional|bidirectional}ingress-tunnel-id <access-tunnel-id-ingress> ingress <ip-address> egress <ip-address>show mpls traffic-eng static
## rvs-out-seg convergence-ratio mode 

rvs-out-seg convergence-ratio mode 
命令功能 : 
配置MPLS-TE静态隧道LSP反向出段的收敛比模式，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
rvs-out-seg convergence-ratio mode 
  {inherit 
|config 
}
no rvs-out-seg convergence-ratio mode 
命令参数解释 : 
参数|描述
---|---
inherit|继承模式
config|配置模式
缺省 : 
无 
使用说明 : 
1.区分正反向，即双向隧道正反两个方向的收敛模式可以各自配置；2.继承模式下，隧道的收敛比继承自它的出接口上的收敛比；3.模式切换时，如果该隧道有带宽预留或者可以进行带宽预留，则需发起带宽CAC校验流程；校验成功则模式切换成功，否则失败，并由MIM回滚之前的配置。
范例 : 
1.配置静态隧道LSP的反向出段收敛比模式为继承模式：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#rvs-out-seg convergence-ratio mode inherit2.删除静态隧道LSP的反向出段收敛比模式：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#no rvs-out-seg convergence-ratio mode
相关命令 : 
rvs-out-seg convergence-ratio valueshow mpls traffic-eng static [tunnel-id <tunnel-id>] | include Convergence-Ratio
## rvs-out-seg convergence-ratio value 

rvs-out-seg convergence-ratio value 
命令功能 : 
配置MPLS-TE静态隧道LSP反向出段的收敛比值，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
rvs-out-seg convergence-ratio value 
  ＜value 
＞
no rvs-out-seg convergence-ratio value 
命令参数解释 : 
参数|描述
---|---
＜value＞|静态隧道收敛比数值，范围：1-100，单位: percent
缺省 : 
默认收敛比为100。 
使用说明 : 
1.若收敛比模式为配置模式时，各自配置LSP正反两个方向的收敛比值。若为继承模式，则两个方向的收敛比分别继承各自的出接口。2.只有在配置模式下才能配置收敛比数值。继承模式或未指定模式时，如果配置则报错。3.no掉收敛比模式时收敛比数值恢复默认100。4.不配置模式时或配置模式不配置收敛比值时，隧道收敛比为默认100。5.收敛比数值改变时，如果该隧道有带宽预留或者可以进行带宽预留，则需发起带宽CAC校验流程；校验成功则收敛比数值修改成功，否则失败。
范例 : 
1.配置静态隧道的收敛比数值为90：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#rvs-out-seg convergence-ratio mode configZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#rvs-out-seg convergence-ratio value 902.删除静态隧道的收敛比数值：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel1-lsp)#no rvs-out-seg convergence-ratio value
相关命令 : 
rvs-out-seg convergence-ratio mode configshow mpls traffic-eng static [tunnel-id <tunnel-id>] | include Convergence-Ratio
## rvs-out-seg-ct 

rvs-out-seg-ct 
命令功能 : 
配置静态隧道的反向出段CT带宽。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
rvs-out-seg-ct 
 class-type 
 ＜class-type 
＞ bandwidth 
 ＜ct-bandwidth 
＞ [{kbps 
|mbps 
|gbps 
}]
no rvs-out-seg-ct 
 class-type 
 ＜class-type 
＞
				
命令参数解释 : 
参数|描述
---|---
＜class-type＞|CT类型，范围：0-7
＜ct-bandwidth＞|CT类型下的带宽值，范围：1-4294967295，默认单位kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
缺省 : 
静态隧道默认没有CT带宽。 
使用说明 : 
1.要配置静态LSP的CT带宽，必须先配置其出接口，请参见命令rvs-out-seg-info；2.静态隧道能否配置CT带宽及配置的个数，请参见命令bandwidth model；3.静态隧道的建立优先级和保持优先级默认为0，隧道建立优先级和保持优先级分别和其下的CT配置两两组合，在te-class映射配置中查找必须要有匹配项。请参见命令ds-te te-class；4.CT带宽配置与普通带宽配置/带宽共享隧道配置普通带宽和CT带宽配置是互斥的，请参见命令rvs-out-seg-info。
范例 : 
1.配置ct带宽(不带单位)：ZXROSNG(config)#mpls trafficZXROSNG(config-mpls-te)#bandwidth model extend-mamZXROSNG(config-mpls-te)#ds-te te-class 0 class-type 0 priority 0ZXROSNG(config-mpls-te)#ds-te te-class 1 class-type 1 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 2 class-type 2 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 3 class-type 3 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 4 class-type 4 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 5 class-type 5 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 6 class-type 6 priority 0                 ZXROSNG(config-mpls-te)#ds-te te-class 7 class-type 7 priority 0                 ZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#bandwidth static 40000 bc0 10000 bc1 10000 bc2 10000 bc3 10000ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#exitZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-info out-port gei-0/1/0/1 out-label 20ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-ct class-type 0 bandwidth 10000ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-ct class-type 1 bandwidth 10000ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-ct class-type 2 bandwidth 10000ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-ct class-type 3 bandwidth 100002.删除ct带宽：ZXROSNG(config)#mpls trafficZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#no rvs-out-seg-ct class-type 03.配置ct带宽（带非默认单位）：ZXROSNG(config)#mpls trafficZXROSNG(config-mpls-te)#bandwidth model extend-mamZXROSNG(config-mpls-te)#ds-te te-class 0 class-type 0 priority 0ZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#interface gei-0/1/0/1ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#bandwidth static 40000 bc0 10000ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#exitZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-info out-port gei-0/1/0/1 out-label 20ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-ct class-type 0 bandwidth 10 mbpsZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#show thisrvs-out-seg-ct class-type 0 bandwidth 10000
相关命令 : 
1.bandwidth model2.rvs-out-seg-info out-port3.ds-te te-class4.show rsvp bandwidth interface
## rvs-out-seg-info 

rvs-out-seg-info 
命令功能 : 
配置MPLS-TE静态隧道LSP的反向出段转发信息。 
命令模式 : 
 MPLS-TE静态隧道LSP配置模式  
命令默认权限级别 : 
15 
命令格式 : 
rvs-out-seg-info 
 out-port 
 ＜out-port 
＞ out-label 
 ＜out-label 
＞ [next-hop 
 ＜ip-address 
＞] [bandwidth-share 
 ＜bandwidth-share tunnel 
＞] [bandwidth 
 {＜committed-information-rate 
＞|＜committed-information-rate 
＞} [{kbps 
|mbps 
|gbps 
}] [{[burst 
 ＜committed-burst-size 
＞ [{byte 
|kb 
|mb 
}]],[peak 
 ＜peak-information-rate 
＞ [{kbps 
|mbps 
|gbps 
}]],[excess-burst 
 ＜excess-burst-size 
＞ [{byte 
|kb 
|mb 
}]]}]]
no rvs-out-seg-info 
命令参数解释 : 
参数|描述
---|---
＜out-port＞|隧道LSP反向出接口名称
＜out-label＞|隧道LSP反向出标签，范围：<16-1048575,or 0,3>
＜ip-address＞|隧道LSP反向下一跳地址
＜bandwidth-share tunnel＞|共享带宽的静态隧道接口名称，隧道ID范围在运行的时候从项目的性能参数中取值。
＜committed-information-rate＞|隧道LSP承诺速率，范围：$#100794375#$~$#100794376#$，默认单位：kbit/s
＜committed-information-rate＞|隧道LSP承诺速率，范围：$#100794375#$~$#100794376#$，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜committed-burst-size＞|隧道LSP承诺突发尺寸，范围：$#100794381#$~$#100794382#$，默认单位：byte
byte|以BYTE为单位
kb|以KB为单位
mb|以MB为单位
＜peak-information-rate＞|隧道LSP峰值速率，范围：$#100794378#$~$#100794379#$，默认单位：kbit/s
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜excess-burst-size＞|隧道LSP超额突发尺寸，范围：$#100794384#$~$#100794385#$，默认单位：byte
byte|以BYTE为单位
kb|以KB为单位
mb|以MB为单位
缺省 : 
无 
使用说明 : 
1.只有在配置了隧道类型和三元组之后，才能创建LSP，配置反向出段信息。2.如果2条TE静态隧道在同一个保护组中，不能配置嵌套关系。
范例 : 
1.设置反向出接口为gei-0/1/0/4，反向出标签为85：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-info out-port gei-0/1/0/4 out-label 852.删除反向出段：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#no rvs-out-seg-info3.设置te_tunnel40000反向出接口为gei-0/1/0/4，反向出标签为85，带宽值为1000kbit/s：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#router-id 2.2.2.2ZXROSNG(config-mpls-te)#interface gei-0/1/0/4ZXROSNG(config-mpls-te-if-gei-0/1/0/4)#bandwidth static 10000ZXROSNG(config-mpls-te-if-gei-0/1/0/4)#exitZXROSNG(config-mpls-te)#ZXROSNG(config-mpls-te)#static te_tunnel40000ZXROSNG(config-mpls-te-static-te_tunnel40000)#role transit type bidirectionalZXROSNG(config-mpls-te-static-te_tunnel40000)#ingress-tunnel-id 1 ingress 1.1.1.1 egress 3.3.3.3ZXROSNG(config-mpls-te-static-te_tunnel40000)#lsp 1ZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#rvs-out-seg-info out-port gei-0/1/0/4 out-label 85 bandwidth 1 mbpsZXROSNG(config-mpls-te-static-te_tunnel40000-lsp)#show thisrvs-out-seg-info out-port gei-0/1/0/4 out-label 85 bandwidth 1000
相关命令 : 
role {ingress|transit|egress} type {unidirectional|bidirectional}ingress-tunnel-id <access-tunnel-id-ingress> ingress <ip-address> egress <ip-address>show mpls traffic-eng static
## sd 

sd 
命令功能 : 
静态隧道SD开关。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
sd 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开SD开关
disable|关闭SD开关
缺省 : 
关闭SD开关。 
使用说明 : 
无 
范例 : 
1.打开SD开关：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#sd enable2.关闭SD开关：ZXROSNG(config)#mpls traffic-eng ZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#sd disable
相关命令 : 
show mpls traffic-eng static [tunnel-id <tunnel-id>] | include SD Switch 
## show debug mpls-te 

show debug mpls-te 
命令功能 : 
显示TE_MP的调试信息是否打开。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug mpls-te 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show debug mpls-teMPLS-TE:  MPLS-TE bfd debugging is on  MPLS-TE cac debugging is on  MPLS-TE fa debugging is on  MPLS-TE static forwarding management debugging is on
相关命令 : 
无 
## show debug rsmgr 

show debug rsmgr 
命令功能 : 
显示RSMGR的调试信息是否打开。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show debug rsmgr 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show debug rsmgr RSMGR:  RSMGR interface debugging is on  RSMGR tunnel debugging is on  RSMGR PW debugging is on  RSMGR section debugging is on
相关命令 : 
debug rsmgr alldebug rsmgr interfacedebug rsmgr pwdebug rsmgr sectiondebug rsmgr tunnel
## show ip explicit-path 

show ip explicit-path 
命令功能 : 
显示显式路径的详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip explicit-path 
  [{name 
 ＜explicit-name 
＞|identifier 
 ＜explicit-identifier 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜explicit-name＞|显示路径名称，长度1-64个字符
＜explicit-identifier＞|显示路径标记，范围：1–65535
缺省 : 
无 
使用说明 : 
显示显式路径信息，如果本台路由器不支持MPLS流量工程，则不显示内容。可选择显示某一具体名称或数字标识的路径 
范例 : 
ZXROSNG(config-mpls-te-if-gei-1/1)#show ip explicit-path identifier 1PATH identifier 1      1: next-address 192.168.11.1 strict
相关命令 : 
无 
## show ip rsvp authentication 

show ip rsvp authentication 
命令功能 : 
显示所有或者某个邻居的状态和配置信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip rsvp authentication 
  [＜ip-address 
＞] 
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|邻居IP地址
缺省 : 
无 
使用说明 : 
不带邻居IP地址时显示接口的所有SA的信息 
范例 : 
ZXROSNG#show ip rsvp authenticationNeighbor: 192.168.10.2  Key ID (hex): c0a80a020000 From: 192.168.10.2 To 192.168.10.1 Interface: gei-0/1/0/1 Direction: Receive       Last valid seq # rcvd:  0x4372fbec08 Challenge: Configured Windowsize: 5 Integriy HF flag: Set Sequence window: 0x4372fbec07 0x4372fbec08 0x4372fbec04 0x4372fbec05 0x4372fbec06Neighbor: 192.168.10.2  Key ID (hex): c0a80a010000 From: 192.168.10.1 To 192.168.10.2 Interface: gei-0/1/0/1 Direction: Send          Last valid seq # sent:  0x4473d1e802 Windowsize: 5 Integriy HF flag: Set
相关命令 : 
无 
## show ip rsvp hello bfd 

show ip rsvp hello bfd 
命令功能 : 
显示接口BFD信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip rsvp hello bfd 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-mpls-te-if-gei-0/1/0/1)#bfdZXROSNG#show ip rsvp hello bfd I/F            Neighbor            State               LSPsZXROSNG#
相关命令 : 
无 
## show ip rsvp hello graceful-restart 

show ip rsvp hello graceful-restart 
命令功能 : 
显示RSVP graceful-restart hello实例的详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip rsvp hello graceful-restart 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
U39(config-mpls-te)#show ip rsvp hello graceful-restart                                                                             MPLS-TE: Enabled                                                                                                                    Graceful Restart: Disabled                                                                                                              Node gr hello: Disabled                                                                                                             Refresh interval: 1000 msecs                                                                                                        Refresh misses: 4                                                                                                                   Advertised restart time: 120000 msecs                                                                                               Advertised recovery time: 120000 msecs     Restarter: Graceful restart in processing    Helper: Graceful restart complete Restarter:表示GR重启方目前的GR状态，是GR过程中，还是已经GR结束Helper：表示GR辅助方目前的GR状态，是GR过程中，还是已经GR结束
相关命令 : 
无 
## show ip rsvp hello instance detail 

show ip rsvp hello instance detail 
命令功能 : 
显示RSVP hello实例的详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip rsvp hello instance detail 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
U52(config-mpls-te)#show ip rsvp hello instance detail                                                                              Hello Graceful Restart globally disabled                                                                                            Fast-Hello globally enabled                                                                                                         Neighbor 115.116.104.39 Source 115.116.104.52                                                                                       Clients:Fast Reroute                                                                                                                  State:UP                                                                                                                            Type:PASSIVE                                                                                                                        I/F:smartgroup51                                                                                                                    LSP num:9                                                                                                                           Src_instance 98695774, Dst_instance 184639855                                                                                     GR HELLO parameters                                                                                                                   Refresh Misses Configured:4                                                                                                         Refresh Interval (msec)                                                                                                               Configured:1000                                                                                                                     Current   :0                                                                                                                      Local restart time (msec):120000                                                                                                    Local recovery time (msec):120000                                                                                                   Nbr restart time (msec):0                                                                                                           Nbr recovery time (msec):0                                                                                                          Lost count:0                                                                                                                        intf hello                                                                                                                        FRR HELLO parameters                                                                                                                  Fast_hello_period (msec):10000                                                                                                      Fast_hello_miss:4                                                                                                                   Fast_hello_protect_lsps:0                                                                                                           Fast_hello_del_time (msec):4800                                                                                                     Fast_hello_reroute_time (msec):0 
相关命令 : 
无 
## show ip rsvp hello instance summary 

show ip rsvp hello instance summary 
命令功能 : 
显示RSVP HELLO实例的概要信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip rsvp hello instance summary 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show ip rsvp hello instance summaryHello globally enabledClient I/F            Neighbor  Type   State LostCnt LspsGR      gei-0/3/0/6  1.1.1.34  ACTIVE LOST  0        1GR      gei-0/3/0/5  1.1.1.35  ACTIVE LOST  0        104
相关命令 : 
无 
## show ip rsvp refresh parameter 

show ip rsvp refresh parameter 
命令功能 : 
显示本路由器的信令刷新时间和丢失数目的配置信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip rsvp refresh parameter 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show ip rsvp refresh parameterRSVP-TE: EnabledRSVP signalling refresh interval: 30000 msecsRSVP signalling refresh misses : 4
相关命令 : 
无 
## show ip rsvp refresh reduction 

show ip rsvp refresh reduction 
命令功能 : 
显示摘要刷新和重传相关信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show ip rsvp refresh reduction 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-mpls-te)#show ip rsvp refresh reductionRetransmit:disabledInitial retransmit delay:1000msRetransmit limit:3Refresh Reduction:disabledP2P Items:Next-hop        Type Tunnel-ID LSP-ID Ingress         EgressP2MP Items:Next-hop        Type Tunnel-ID LSP-ID Ingress         Originator-ID   GRP-ID
相关命令 : 
无 
## show mpls traffic-eng auto-backup parameter 

show mpls traffic-eng auto-backup parameter 
命令功能 : 
显示自动备份隧道的配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng auto-backup parameter 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-mpls-te)#show mpls traffic-eng auto-backup parameter RSVP-TE: EnabledThe setting of auto-tunnel minID is: 4001The setting of auto-tunnel maxID is: 5000Auto-tunnel minID in used is: No usedAuto-tunnel maxID in used is: No usedAuto-tunnel backup srlg exclude:  None
相关命令 : 
无 
## show mpls traffic-eng auto-backup tunnels band 

show mpls traffic-eng auto-backup tunnels band 
命令功能 : 
显示自动备份隧道保护的主隧道的信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng auto-backup tunnels band 
  [te_tunnel 
 ＜tunnel-id 
＞] 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|指定具体的自动备份隧道tunnel_id, tunnel-id取值范围$#100794388#$~$#100794389#$
缺省 : 
无 
使用说明 : 
范例中Auto-tunnel条目中的隧道id取值范围由项目性能参数决定 
范例 : 
ZXROSNG#show mpls traffic-eng auto-backup tunnels band The information of being protected primary tunnel by auto-tunnel:Auto-tunnel   Protect_pri     IngressID        EgressID         Protect_stateTun32999      (1,25)          1.1.1.41         10.10.10.54      READY
相关命令 : 
无 
## show mpls traffic-eng auto-backup tunnels brief 

show mpls traffic-eng auto-backup tunnels brief 
命令功能 : 
显示自动备份隧道的简略信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng auto-backup tunnels brief 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show mpls traffic-eng auto-backup tunnels briefSignalling Summary:LSP Tunnels Process:runningRSVP Process:runningForwarding:enabledTUNNEL NAME           DESTINATION     UP IF          DOWN IF        STATE/PROTtunnel_65535          22.2.2.2        -              xgei-0/1/0/2   up/uptunnel_65535          11.1.1.1        xgei-0/1/0/3   -              up/uptunnel_65531 (MBK)    100.1.1.3       -              gei-0/1/0/7    up/up      tunnel_65531 (MBKHOT) 100.1.1.3       -              gei-0/1/0/5    up/uptunnel_65532 (MBFD)   100.1.1.3       -              gei-0/1/0/1    up/up域信息描述表：域    描述TUNNEL NAME    隧道名称DESTINATION        隧道的目的地UP IF    隧道的入接口DOWN IF    隧道的出接口STATE/PROT    隧道的状态：接口状态/协议状态(MBK)    带有此标记的P2P LSP，是P2MP Sub-LSP的端到端保护的备份隧道LSP(MBKHOT)    带有此标记的P2P LSP，是P2MP Sub-LSP的端到端保护的备份隧道的hot LSP(MBFD)    带有此标记的P2P LSP，是P2MP Sub-LSP的BFD检测LSP
相关命令 : 
show mpls traffic-eng auto-backup tunnelsshow mpls traffic-eng tunnels briefshow mpls traffic-eng auto-backup tunnels summary
## show mpls traffic-eng auto-backup tunnels remote-tunnel 

show mpls traffic-eng auto-backup tunnels remote-tunnel 
命令功能 : 
显示远端自动备份隧道的详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng auto-backup tunnels remote-tunnel 
  [tunnel-id 
 ＜tunnel-id 
＞ lsp-id 
 ＜lsp-id 
＞ ingress-id 
 ＜ingress-id-address 
＞ egress-id 
 ＜egress-ip-address 
＞] 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|需要显示的远端隧道的隧道号，具体范围为：$#100794388#$~$#100794389#$
＜lsp-id＞|需要显示的远端隧道的LSP ID号，即隧道实例号
＜ingress-id-address＞|需要显示的远端隧道的头节点地址
＜egress-ip-address＞|需要显示的远端隧道的尾节点地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show mpls traffic-eng auto-backup tunnels remote-tunnelName: tunnel_65533      (P2MP BFD)(Tunnel65533) Destination: 100.1.1.3  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/6, 642494    OutLabel: -    Rvs-InLabel: -, -    Rvs-OutLabel: gei-0/1/0/6, 423429    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65533, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: 100.1.1.2 10.1.6.2 100.1.1.1                    10.1.1.1      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 0 minute, 16 second    Current LSP: Uptime:0 day, 0 hour, 0 minute, 16 secondName: tunnel_65535      (P2MP backup)(Tunnel65535) Destination: 100.1.1.3  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/7, 642491    OutLabel: -    Rvs-InLabel: -, -    Rvs-OutLabel: gei-0/1/0/7, 622904    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65535, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.7.3 100.1.1.3      Exclude Route: NULL      Record Route: 100.1.1.1 10.1.7.1      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 11 minute, 8 second    Current LSP: Uptime:0 day, 0 hour, 11 minute, 8 second域信息描述表：域    描述Name        隧道名称Status    隧道当前状态RSVP Signalling Info    隧道目前的信令信息RSVP Path Info    Path    报文的相关信息RSVP Resv Info    Resv    报文的相关信息History    隧道的历史记录Time Since Created    隧道已经up了多长时间Current LSP    隧道正在使用的LSP的信息(P2MP BFD)    隧道是P2MP Sub-LSP的BFD检测隧道,则显示该字段，否则不显示(P2MP backup)    隧道是P2MP Sub-LSP的端到端备份隧道，则显示该字段，否则不显示Association P2MP tunnel ID    该隧道关联的P2MP 隧道ID, P2MP Sub-LSP的端到端备份隧道和BFD检测隧道才显示该字段
相关命令 : 
show mpls traffic-eng auto-backup tunnelsshow mpls traffic-eng tunnels remote-tunnelshow mpls traffic-eng auto-backup tunnels summary
## show mpls traffic-eng auto-backup tunnels summary 

show mpls traffic-eng auto-backup tunnels summary 
命令功能 : 
显示自动备份隧道的统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng auto-backup tunnels summary 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show mpls traffic-eng auto-backup tunnels summaryMPLS-TE: EnabledSignalling Summary:   LSP Tunnels Process:            running   RSVP Process:                   running   Forwarding:                     enabled   Head: 1 interfaces, 1 active signalling attempts, 1 established   Auto-tunnel not care of midpoint and tail
相关命令 : 
无 
## show mpls traffic-eng auto-backup tunnels 

show mpls traffic-eng auto-backup tunnels 
命令功能 : 
显示自动备份隧道的详细信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng auto-backup tunnels 
  [te-tunnel 
 ＜Tunnel ID 
＞] [hot-standby 
] 
命令参数解释 : 
参数|描述
---|---
＜Tunnel ID＞|指定具体的自动备份隧道tunnel_id，范围：$#100794388#$~$#100794389#$
hot-standby|要求显示的是相关隧道的hot-standby信息
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show mpls traffic-eng auto-backup tunnelsName: tunnel_65530      (remote)(Tunnel65530) Destination: 22.2.2.2  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/5, 3    OutLabel: -    Src 11.1.1.1, Dst 22.2.2.2, Tun-ID 1, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.20.9.2 22.2.2.2      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 2 day, 15 hour, 49 minute, 26 second    Current LSP: Uptime:2 day, 15 hour, 49 minute, 26 secondName: tunnel_65533      (P2MP BFD)(Tunnel65533) Destination: 100.1.1.3  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected    No path options defined    Actual Bandwidth: N/A    Hot-standby protection:      No path options protected    PCE-authorized: NO  Config Parameters:    Resv-Style: SE    Metric Type: IGP (default)   Upper Limit: 4294967295    Hop Prior: disabled         Upper Limit: -    Record-Route: disabled    Facility Fast-reroute: disabled    Detour Fast-reroute: disabled    Bandwidth Protection: disabled    Hot-standby-lsp Fast-reroute: disabled    E2E: disabled    BFD: enabled         connect         up                      min_tx: 900     min_rx: 900     mult: 10         Policy Class: N/A    Track Name:     Auto-reoptimize: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Reference Hot-standby: disabled    Tunnel-Status: disabled    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: enabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled  InLabel: -  OutLabel: gei-0/1/0/1, 423428  Rvs-InLabel: gei-0/1/0/1, 622905  Rvs-OutLabel: -  RSVP Signalling Info :    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65533, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.1.1 10.1.1.2 10.1.6.2                      10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1    RSVP Resv Info:      Record Route: 100.1.1.2(423428) 10.1.1.2(423428)                    100.1.1.3(642494) 10.1.6.3(642494)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 25 minute, 55 second    Prior LSP: path option 0    Current LSP: Uptime:0 day, 0 hour, 25 minute, 55 second    Last LSP Error Information:Name: tunnel_65535      (P2MP backup)(Tunnel65535) Destination: 100.1.1.3  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected    No path options defined    Actual Bandwidth: N/A    Hot-standby protection:      No path options protected    PCE-authorized: NO  Config Parameters:    Resv-Style: SE    Metric Type: IGP (default)   Upper Limit: 4294967295    Hop Prior: disabled         Upper Limit: -    Record-Route: disabled    Facility Fast-reroute: disabled    Detour Fast-reroute: disabled    Bandwidth Protection: disabled    Hot-standby-lsp Fast-reroute: disabled    E2E: disabled    BFD: enabled         connect         up                      min_tx: 900     min_rx: 900     mult: 10         Policy Class: N/A    Track Name:     Auto-reoptimize: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Reference Hot-standby: disabled    Tunnel-Status: disabled    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: enabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled  InLabel: -  OutLabel: gei-0/1/0/7, 642491  Rvs-InLabel: gei-0/1/0/7, 622904  Rvs-OutLabel: -  RSVP Signalling Info :    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65535, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.7.1 10.1.7.3 100.1.1.3      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1RSVP Resv Info:      Record Route: 100.1.1.3(642491) 10.1.7.3(642491)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 37 minute, 17 second    Prior LSP: path option 0    Current LSP: Uptime:0 day, 0 hour, 37 minute, 16 second    Last LSP Error Information:Name: tunnel_65535      (P2MP backup hot)(Tunnel65535) Destination: 100.1.1.3  Status:    Signalling: up    Actual Bandwidth: N/A    Hot-standby protection:    PCE-authorized: NO  Config Parameters:    BFD: disabled    Hot-standby-lsp Fast-reroute: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: enabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled  InLabel: -  OutLabel: gei-0/1/0/5, 423430  Rvs-InLabel: gei-0/1/0/5, 622904  Rvs-OutLabel: -  RSVP Signalling Info :    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65533, Tun-Instance 2    RSVP Path Info:      Explicit Route: 10.1.5.1 10.1.5.2 10.1.6.2                      10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1    RSVP Resv Info:      Record Route: 100.1.1.2(423430) 10.1.5.2(423430)                    100.1.1.3(642495) 10.1.6.3(642495)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 5 minute, 39 second    Prior LSP: path option 0    Current LSP: Uptime:0 day, 0 hour, 0 minute, 14 second    Last LSP Error Information:Name: tunnel_65532      (remote P2MP backup)(Tunnel65532) Destination: 100.1.1.3  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/7, 642493    OutLabel: -    Rvs-InLabel: -, -    Rvs-OutLabel: gei-0/1/0/7, 622905    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65533, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.7.3 100.1.1.3      Exclude Route: NULL      Record Route: 100.1.1.1 10.1.7.1      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 1 minute, 32 second    Current LSP: Uptime:0 day, 0 hour, 1 minute, 32 secondName: tunnel_65534      (remote P2MP BFD)(Tunnel65534) Destination: 100.1.1.3  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/6, 642494    OutLabel: -    Rvs-InLabel: -, -    Rvs-OutLabel: gei-0/1/0/6, 423429    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65534, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: 100.1.1.2 10.1.6.2 100.1.1.1                    10.1.1.1      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 1 minute, 33 second    Current LSP: Uptime:0 day, 0 hour, 1 minute, 33 secondZXROSNG#show mpls traffic-eng auto-backup tunnels hot-standby Name: tunnel_65535      (P2MP backup)(Tunnel65535) Destination: 100.1.1.3  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected  Fast Reroute Protection: disabled  Hot-standby Protection: ready  Config Parameters:    BFD: disabled    Hot-standby-lsp Fast-reroute: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL  InLabel: -  OutLabel: gei-0/1/0/5, 426442  Rvs-InLabel: gei-0/1/0/5, 604433  Rvs-OutLabel: -  RSVP Signalling Info :    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65535, Tun-Instance 2    RSVP Path Info:      Explicit Route: 10.1.5.1 10.1.5.2 10.1.6.2                      10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1    RSVP Resv Info:      Record Route: 100.1.1.2(426442) 10.1.5.2(426442)                    100.1.1.3(491827) 10.1.6.3(491827)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb域信息描述表：域    描述Name        隧道名称(remote)    表示远端隧道Status        隧道当前状态Config Parameters    隧道下相关的配置信息InLabel    隧道的入标签状况OutLabel    隧道的出标签状况RSVP Signalling Info    隧道目前的信令信息RSVP Path Info    Path    报文的相关信息，Tspec: SENDER_TSPECRSVP Resv Info    Resv    报文的相关信息，Fspec：FLOWSPECHistory    隧道的历史down记录Time Since Created    隧道已经up了多长时间Current LSP    隧道正在使用的LSP的信息Last LSP Error Information    LSP的删除记录(P2MP BFD)    隧道是P2MP Sub-LSP的BFD检测隧道,则显示该字段，否则不显示(remote P2MP BFD)    远端隧道是P2MP Sub-LSP的BFD检测隧道,则显示该字段，否则不显示(P2MP backup)    隧道是P2MP Sub-LSP的端到端备份隧道，则显示该字段，否则不显示(P2MP backup hot)    隧道是P2MP Sub-LSP的端到端备份隧道hot LSP，则显示该字段，否则不显示(remote P2MP backup)    远端隧道是P2MP Sub-LSP的端到端备份隧道，则显示该字段，否则不显示Association P2MP tunnel ID    该隧道关联的P2MP 隧道ID, P2MP Sub-LSP的端到端备份隧道和BFD检测隧道才显示该字段
相关命令 : 
show mpls traffic-eng auto-backup tunnels briefshow mpls traffic-eng tunnelsshow mpls traffic-eng auto-backup tunnels summary
## show mpls traffic-eng autoroute 

show mpls traffic-eng autoroute 
命令功能 : 
显示所有配置了自动路由的隧道的状态和配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng autoroute 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show mpls traffic-eng autorouteMPLS TE autorouting enabled     destination 20.20.20.20 has 1 tunnels TunnelName   Destination      State   Nexthop          MetricType  MetricValuetunnel_1     20.20.20.20      Up      192.168.10.2     Absolute    1000
相关命令 : 
无 
## show mpls traffic-eng crankback p2p 

show mpls traffic-eng crankback p2p 
命令功能 : 
显示TE下所有隧道或指定隧道的crankback相关条目信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng crankback p2p 
  [tunnel-id 
 ＜tunnel-id 
＞ ingress-id 
 ＜ingress-id-address 
＞ egress-id 
 ＜egress-ip-address 
＞] 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|指定的具体tunnel ID，1~$#100794374#$
＜ingress-id-address＞|指定隧道的头结点route ID
＜egress-ip-address＞|指定隧道的尾节点route ID
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG# show mpls traffic-eng crankback p2pTunnel_1        Source: 22.2.2.2            Destination: 11.1.1.1                Extended_tunnel_id: 22.2.2.2  Tunnel_Instance 2  Crankback Address: 192.168.10.1  192.168.10.2  20.20.20.20  Crankback Counts: 4                 Crankback TTL: 60 seconds    Tunnel_Instance 4  Crankback Address: 192.168.10.5  192.168.10.7  20.20.20.29  Crankback Counts: 5                 Crankback TTL: 57 secondsTunnel_2        Source: 22.2.2.2            Destination: 11.1.1.1                Extended_tunnel_id: 22.2.2.2  Tunnel_Instance 1  Crankback Address: 192.168.10.1  Crankback Counts: 1                 Crankback TTL: 49 secondsZXROSNG#ZXROSNG#ZXROSNG# show mpls traffic-eng crankback p2p tunnel-id 2 ingress-id 22.2.2.2 egress-id 11.1.1.1Tunnel_2        Source: 22.2.2.2            Destination: 11.1.1.1                Extended_tunnel_id: 22.2.2.2  Tunnel_Instance 1  Crankback Address: 192.168.10.1  Crankback Counts: 1                 Crankback TTL: 44 seconds域信息描述：Source    隧道头结点route IDDestination    隧道 尾节点route IDExtended tunnel id    Extended tunnel IDTunnel Instance    隧道LSP IDCrankback Address    表示相关LSP键值所对应存储的排除地址序列Crankback Counts    表示相关crankback条目已经几次用于crankback重试Crankback TTL    表示相关crankback条目的保活时间
相关命令 : 
无 
## show mpls traffic-eng crankback parameter 

show mpls traffic-eng crankback parameter 
命令功能 : 
显式TE全局crankback配置参数。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng crankback parameter 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG# show mpls traffic-eng crankback parameterCrankback retry-limit: 7Crankback TTL:   60 seconds
相关命令 : 
无 
## show mpls traffic-eng fast-reroute bw-protect 

show mpls traffic-eng fast-reroute bw-protect 
命令功能 : 
显示本地被配置为TE-FRR备份隧道的统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng fast-reroute bw-protect 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels backup Name: tunnel_7   LSP Head: Tunnel7   Admin: up  Oper: up   Src:100.1.1.1,Dest: 100.1.1.3,Instance:1   Fast Reroute Backup Provided:       Protected i/fs: gei-0/1/0/2       Protected lsps: 0       Backup BW: 0kbps;inuse: 0kbps
相关命令 : 
show mpls traffic-eng tunnels [{brief|summary|te_tunnel <tunnel_id> }] 
## show mpls traffic-eng fast-reroute promotion 

show mpls traffic-eng fast-reroute promotion 
命令功能 : 
显示FRR提升的内容信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng fast-reroute promotion 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-mpls-te)#show mpls traffic-eng fast-reroute promotion MPLS-TE: Enabled   Periodic FRR Promotion:         every 300 seconds, next in 284 seconds
相关命令 : 
无 
## show mpls traffic-eng fast-reroute 

show mpls traffic-eng fast-reroute 
命令功能 : 
显示快速重路由数据库的内容信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng fast-reroute 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
1.不带参数，显示FRR关系2.带参数bw-protect，显示FRR带宽保护关系
范例 : 
ZXROSNG#show mpls traffic-eng fast-rerouteTunnel head end item informationProtected Tunnel   LspID    In-label Out intf/label     FRR intf/label  StatusTunnel1               23    Tun hd   smartgroup12:1474  Tu1:147462      readyLSP midpoint frr information:LSP identifier    In-label Out intf/label      FRR intf/label Status
相关命令 : 
show mpls traffic-eng tunnels backup域信息描述表：域    描述P2P local FRR       :     本地P2P隧道TE-FRR条目统计P2P local HSB       :     本地P2P隧道HSB条目统计P2P remote FRR  :     远端P2P隧道TE-FRR条目统计P2P tail HSB          :     P2P隧道尾结点HSB条目统计P2MP local FRR     :    本地P2MP隧道TE-FRR条目统计P2MP remote FRR:     远端P2MP隧道 TE-FRR条目统计(HSB)    带有此标记的保护关系，是HSB保护(FRR)    带有此标记的保护关系，是LSP形成的TE-FRR保护(FRR2)   带有此标记的保护关系，是LSP形成的SECOND TE-FRR保护(H-FRR)   带有此标记的保护关系，是头结点HOT-LSP形成的TE-FRR保护(H-FRR2)  带有此标记的保护关系，是头结点HOT-LSP形成的SECOND TE-FRR保护(p2mp)    带有此标记的保护关系，是P2MP Sub-LSP形成的TE-FRR保护
## show mpls traffic-eng forwarding-adjacency 

show mpls traffic-eng forwarding-adjacency 
命令功能 : 
显示使能了FA功能的隧道信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng forwarding-adjacency 
  [＜ip-address 
＞] 
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|隧道的目的地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show mpls traffic-eng forwarding-adjacency  MPLS TE forwarding-adjacency enabled    Destination 1.1.1.35 has 2 tunnels    TunnelName   Destination      State   Nexthop          Holdtime    tunnel_1     20.20.20.20      Up       192.168.10.2    60
相关命令 : 
无 
## show mpls traffic-eng graceful-shutdown 

show mpls traffic-eng graceful-shutdown 
命令功能 : 
显示某个设备的本地及远端Graceful shutdown地址信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng graceful-shutdown 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
查看graceful-shutdown信息：ZXROSNG(config#show mpls traffic-eng graceful-shutdown Graceful shutdown local node: enabledGraceful shutdown local Interface:    Address          Name                                10.30.4.3        gei-0/1/0/4                     Graceful shutdown remote address:    99.9.8.1(I)        99.9.9.1(I)        100.200.200.201(N) 100.200.200.202(N)信息描述表：域    描述Graceful shutdown local node:    本节点是否全局使能graceful shutdownGraceful shutdown local Interface:    本节点接口使能graceful shutdown信息Address    本节点使能graceful shutdown的接口地址Name    本节点使能graceful shutdown的接口名称Graceful shutdown remote address:    远端graceful shutdown地址信息(I:接口地址，N:节点地址)
相关命令 : 
无 
## show mpls traffic-eng interface brief 

show mpls traffic-eng interface brief 
命令功能 : 
显示MPLS TE接口的内容摘要信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng interface brief 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
显示信息说明：信息    描述I/F    RSVP TE接口Hello    是否配置RSVP hello功能interval    接口发送RSVP hello请求的时间间隔misses    节点多少RSVP hello ack报文没有接收到，认为与邻居的通信是DOWNBK-PATH    接口是否配置备份隧道state    接口状态
范例 : 
ZXROSNG(config-mpls-te)#show mpls traffic-eng interface brief I/F         Hello interval(ms)  misses  BK-PATH stategei-0/1/0/  NO    30000         4       NO      EN1                                            gei-0/1/0/  NO    30000         4       NO      EN2                                            gei-0/1/0/  NO    30000         4       NO      DIS3  
相关命令 : 
无 
## show mpls traffic-eng interface detail 

show mpls traffic-eng interface detail 
命令功能 : 
显示MPLS TE接口的详细信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng interface detail 
  [＜Interface number 
＞] 
命令参数解释 : 
参数|描述
---|---
＜Interface number＞|接口的名称
缺省 : 
缺省<para>参数的情况下显示所有具有MPLS TE功能的接口的详细信息 
使用说明 : 
显示信息说明：信息    描述State    接口状态Traffic-eng metric:    链路度量Authentication    接口是否使能认证功能Key    接口认证密钥Type    接口认证类型Challenge    接口认证接收方支持challengeChallenge-imp    接口认证发送方支持challengeWindow size    窗口大小BFD    接口BFD状态Second fast-reroute    是否配置第二FRR备份保护功能Backup path    备份隧道SRLGs    共享风险链路组Intf Fast-Hello    是否配置RSVP hello功能Fast-Hello interval    接口发送RSVP hello请求的时间间隔Fast-Hello miss    节点多少RSVP hello ack报文没有接收到，认为与邻居的通信是DOWNAffinity attributes：接口亲和力属性，配置name类型，显示为Affinity attributes(Name)，name类型显示和bit-position的映射关系；配置bit-position类型，显示为Affinity attributes(Bit position)，没有配置就不显示Undefined Affinity Names:显示接口下配置的没有映射的亲和力name类型
范例 : 
ZXROSNG(config-mpls-te)#show mpls traffic-eng interface detail gei-0/1/0/1 gei-0/1/0/1:   State:    ENABLE   Traffic-eng metric: 0     Authentication: disabled    Key:           RSVP-AUTH    Type:          md5    Challenge:     disabled    Challenge-imp: Not implemented(simulated)    Window size:   32   BFD: disabled          Backup path:    None   SRLGs: None   Affinity attributes(Name):    red(0) blue(1)   Undefined Affinity Names:     green black   Intf Fast-Hello: DISABLE    Fast-Hello interval: 10000       Fast-Hello miss: 4
相关命令 : 
无 
## show mpls traffic-eng interface packet-counters 

show mpls traffic-eng interface packet-counters 
命令功能 : 
显示接口上的报文计数 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng interface packet-counters 
  [＜interface-name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|接口的名称
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show mpls traffic-eng interface packet-counters gei-0/1/0/1:                   Tx             Rx             TxErr          RxErr    Path           0              0              0              0             Resv           0              0              0              0             PathErr        0              0              0              0             ResvErr        0              0              0              0             PathTear       0              0              0              0             ResvTear       0              0              0              0             Hello          0              0              0              0             Srefresh       0              0              0              0             RecoveryPath   0              0              0              0             Notify         0              0              0              0             Challenge      0              0              0              0             Response       0              0              0              0             Ack            0              0              0              0             UnKnown        0              0              0              0     
相关命令 : 
无 
## show mpls traffic-eng local-tunnels free-id 

show mpls traffic-eng local-tunnels free-id 
命令功能 : 
显示本节点当前空闲的local tunnel id，最多显示5个。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng local-tunnels free-id 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show mpls traffic-eng local-tunnels free-idUNUSED LOCAL TUNNEL ID3276932770327713277232773ZXROSNG(config)#
相关命令 : 
无 
## show mpls traffic-eng local-tunnels ingress-tunnel-id 

show mpls traffic-eng local-tunnels ingress-tunnel-id 
命令功能 : 
根据头结点远端隧道ID显示本节点的local tunnel id使用分配情况(主要是和哪条远端过来的隧道相匹配)。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng local-tunnels ingress-tunnel-id 
  ＜te-tunnel-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜te-tunnel-id＞|显示某个远端隧道ID对应的本地local tnnlid使用情况，取值范围为头结点隧道范围，范围：1~$#100794374#$
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-mpls-te)#show mpls traffic-eng local-tunnels ingress-tunnel-id 1===========================================================================Headers:LT ID       :LOCAL TUNNEL IDIT ID       :INGRESS TUNNEL ID===========================================================================LT ID     IT ID     LSP ID    INGRESS ID       EGRESS ID        PRE HOP
相关命令 : 
无 
## show mpls traffic-eng local-tunnels 

show mpls traffic-eng local-tunnels 
命令功能 : 
显示本节点的local tunnel id使用分配情况(主要是和哪条远端过来的隧道相匹配) 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng local-tunnels 
  [tunnel-id 
 ＜tunnel_id 
＞] 
命令参数解释 : 
参数|描述
---|---
＜tunnel_id＞|显示某个具体的local tunnel id的使用、分配情况，范围：$#100794390#$~$#100794387#$
缺省 : 
无 
使用说明 : 
本命令在指定可选参数[tunnel-id ＜tunnel_id＞]时，如果指定的id是用户配置的接入隧道，将显示指定接入隧道的详细配置情况和状态，否则显示格式仍与不带参数时一致。两种格式范例如下。
范例 : 
ZXROSNG(config-mpls-te)#show mpls traffic-eng local-tunnels ===========================================================================    Headers:                                                                       LT ID       :LOCAL TUNNEL ID                                                   IT ID       :INGRESS TUNNEL ID                                                 ===========================================================================    LT ID     IT ID     LSP ID    INGRESS ID       EGRESS ID        PRE HOP       64510     0         -         0.0.0.0          0.0.0.0          -              ZXROSNG#show mpls traffic-eng local-tunnels tunnel-id 32769Name: tunnel_32769  Status:     Protocol Status: down  Basic Config Parameters:     Ingress-TnnlID: -     IngressID: -               EgressID: -                 Tunnel Type: -             Role: -    Policy Class: defaultZXROSNG#显示信息说明：Name：隧道名称Protocol Status：协议状态up/downBasic Config Parameters：配置信息Ingress-TnnlID：隧道三元组中的头结点隧道IDIngressID：隧道三元组中的头结点router IDEgressID: 隧道三元组中的尾结点router IDTunnel Type：隧道单双向Role： 隧道角色，头结点，中间结点，尾结点。Policy Class：隧道PBTS属性其中，“-”代表未配置或者本功能无效
相关命令 : 
无 
## show mpls traffic-eng mtunnels brief 

show mpls traffic-eng mtunnels brief 
命令功能 : 
显示所有P2MP隧道的简要信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng mtunnels brief 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
show mpls traffic-eng mtunnels brief 显示所有本地隧道和远端隧道的简要信息，不包括接入隧道
范例 : 
ZXROSNG#show mpls traffic-eng mtunnels brief Signaling Summary:  LSP Tunnels Process:    running  RSVP-TE P2MP Process:   running  Forwarding:             enabledTUNNEL ID  P2MP ID    INGRESS ID      LSP ID     DESTINATION     UP IF            DOWN IF          STATE/PROT1          1          100.1.1.1       1          100.1.1.2       -                gei-0/1/0/5      up200        200        100.1.1.2       1          100.1.1.1       gei-0/1/0/5      -                up
相关命令 : 
无 
## show mpls traffic-eng mtunnels leaf-tunnel 

show mpls traffic-eng mtunnels leaf-tunnel 
命令功能 : 
1，显示所有接入隧道详细信息2，显示指定的接入隧道详细信息
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng mtunnels leaf-tunnel 
  {[＜tunnel-id 
＞]} 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|指定的接入隧道ID 整数，范围1-65535
缺省 : 
无 
使用说明 : 
1，显示所有接入隧道详细信息show mpls traffic-eng mtunnels leaf-tunnel2，显示指定的接入隧道详细信息show mpls traffic-eng mtunnels leaf-tunnel 60001
范例 : 
ZXROSNG#show mpls traffic-eng mtunnels leaf-tunnelName: P2MP tunnel_60001 (leaf)                          Status: up             Admin: up            Recovering: no  VPN ID: 1  Root tunnel ID: 1      P2MP ID: 1           Ingress ID: 100.1.1.1  Bound P2P LSPs:    Tunnel-ID        Ingress-ID       Destination      LSP-ID    65530            100.1.1.1        100.1.1.2        1  Name: P2MP tunnel_60002 (leaf)                          Status: up             Admin: up            Recovering: no  VPN ID: 1  Root tunnel ID: 2      P2MP ID: 2           Ingress ID: 100.1.1.1  Bound P2P LSPs:    Tunnel-ID        Ingress-ID       Destination      LSP-ID    65534            100.1.1.1        100.1.1.2        1  ZXROSNG#ZXROSNG#show mpls traffic-eng mtunnels leaf-tunnel 60001Name: P2MP tunnel_60001 (leaf)                          Status: up             Admin: up            Recovering: no  VPN ID: 1  Root tunnel ID: 1      P2MP ID: 1           Ingress ID: 100.1.1.1  Bound P2P LSPs:    Tunnel-ID        Ingress-ID       Destination      LSP-ID    65530            100.1.1.1        100.1.1.2        1域信息描述表：    域    描述Status:    叶子隧道协议状态 ,取值为up或downAdmin:    叶子隧道管理状态，取值为up或downRecovering:    叶子隧道是否正在恢复,取值为yes或noRoot tunnel ID:    绑定的根隧道IDP2MP ID    绑定的根隧道P2MP IDIngress ID    绑定的根隧道route IDVPN ID     叶子隧道接口上的VPN IDBound P2P LSPs    绑定到P2MP叶子隧道上的P2P 备份隧道LSP信息Tunnel-ID    绑定到P2MP叶子隧道上的P2P 备份隧道IDIngress-ID    绑定到P2MP叶子隧道上的P2P 备份隧道头结点router IDDestination    绑定到P2MP叶子隧道上的P2P 备份隧道目的IP地址LSP-ID    绑定到P2MP叶子隧道上的P2P 备份隧道LSP ID
相关命令 : 
无 
## show mpls traffic-eng mtunnels local-tunnel 

show mpls traffic-eng mtunnels local-tunnel 
命令功能 : 
1，显示所有本地隧道详细信息2，显示指定的本地隧道详细信息
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng mtunnels local-tunnel 
  {[＜tunnel-id 
＞]} 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|指定的本地隧道ID 整数，范围1-65535
缺省 : 
无 
使用说明 : 
1，显示所有本地隧道详细信息show mpls traffic-eng mtunnels local-tunnel2，显示指定的本地隧道详细信息ZXROSNG#show mpls traffic-eng mtunnels local-tunnel 1
范例 : 
ZXROSNG#show mpls traffic-eng mtunnels local-tunnel Name: P2MP tunnel_1                                   P2MP ID: 1  Status:    Admin: up  Oper: up    Path: valid      Signalling: connected    P2MP Template: loose-to-3    Dest-list identifier: 1    Escape Path: type dynamic  Config Parameters:    Bandwidth: 0 kbps (Global) Priority: 7  7  Affinity: 0x0/0x0    Resv-Style: SE    Metric Type: IGP (default)  Upper Limit: 4294967295    Integrity: disabled    Record Route: enabled    Reoptimize: disabled    Crankback: disabled    Fast-Reroute: disabled                  BFD: enabled  min_tx: 100 min_rx: 100 mult: 10     E2E: enabled  LSP Signalling Info: (in use LSP)    Source: 100.1.1.1          LSP ID: 31       Status: up    Sub-LSP to 100.1.1.2                        Recovering: no   Status: up      Upstream Subgroup Originator: - Subgroup ID: -      Downstream Subgroup Originator: 100.1.1.1 Subgroup ID: 1      Path Option: 1, explicit identifier:1      Forwarding Info:        InLabel: -, -        Prev Hop: -        OutLabel: gei-0/1/0/5, 670584        Next Hop: 10.1.5.2      RSVP Path Info:        Explicit Route: 10.1.5.1 10.1.5.2 100.1.1.2        Exclude Route: NULL        Record Route: NULL        Tspec: ave rate= 0 kbits, burst= 1000 bytes, peak rate= 0 kbits      RSVP Resv Info:        Record Route: 100.1.1.2 10.1.5.2        Fspec: ave rate= 0 kbits, burst= 1000 bytes, peak rate= 0 kbits      BFD status: up       BFD tunnel: 65535      E2E status: ready    Backup tunnel: 65534    History:      Sub-LSP:      Time since created: 0 days, 0 hours, 27 minutes, 55 seconds      Sub-LSP Uptime: 0 days, 0 hours, 27 minutes, 54 seconds      History:    Tunnel:    Time since created: 1 days, 5 hours, 48 minutes, 32 seconds    Current LSP: 31, Uptime: 0 days, 0 hours, 27 minutes, 55 seconds域信息描述表：    域    描述Recovering    Sub-LSP是否处于恢复状态,取值为yes或noEscape Path    表示是否使能了逃生路径，该目的地是否用逃生路径建立的BFD    是否使能BFD检测，取值为disabled或enabledE2E    是否使能端到端保护，取值为disabled或enabledmin_tx    BFD 发送检测报文时间间隔，单位毫秒min_rx    BFD 接收检测报文时间间隔，单位毫秒mult    BFD 检测报文检测间隔个数BFD status    Sub-LSP的BFD检测状态，                取值为none（无BFD检测），                creating（正在创建BFD检测），                up（BFD检测建立成功）BFD tunnel    为Sub-LSP提供BFD检测的P2P隧道IDE2E status    Sub-LSP的端到端保护状态，                取值为none（无保护关系），                creating（正在创建保护关系），                ready（形成保护关系），                active（保护发生切换）Backup tunnel    为Sub-LSP提供端到端保护的P2P隧道IDP2MP Template  隧道引用的模板名称Path Option   模板下具体配置的路径信息
相关命令 : 
无 
## show mpls traffic-eng mtunnels protection 

show mpls traffic-eng mtunnels protection 
命令功能 : 
显示当前P2MP隧道的FRR保护和端到端(E2E)保护状态信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng mtunnels protection 
  {[mte_tunnel 
 ＜tunnel-id 
＞]} 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|无
缺省 : 
无 
使用说明 : 
show mpls traffic-eng mtunnels protection显示本地P2MP隧道FRR关系状态的详细信息
范例 : 
ZXROSNG#show mpls traffic-eng mtunnels protectionName: P2MP tunnel_1                                   P2MP ID: 1  LSP Protection Info: (in use LSP)    Source: 11.1.1.1                    LSP ID: 10    Fast-Reroute: facility enabled      FRR State: ready    E2E: disabled    Sub-LSP to 22.2.2.2      PLR               PROT-TYPE       STATE      11.1.1.1          link            ready      22.2.2.2          link            ready    Sub-LSP to 33.3.3.3      PLR               PROT-TYPE       STATE      11.1.1.1          link            readyName: P2MP tunnel_2                                   P2MP ID: 2  LSP Protection Info: (in use LSP)    Source: 100.1.1.1                   LSP ID: 3    Fast-Reroute: disabled                  E2E: enabled    Sub-LSP to 100.1.1.2 (path overlap)      Backup tunnel: 65533 (hot-standby ready)       State: ready域信息描述表：域    描述Name    P2MP隧道名P2MP ID    P2MP ID号Source    LSP的源地址LSP ID    LSP ID号Fast-Reroute    FRR使能类型FRR State    整个LSP的FRR状态Sub-LSP    Sub-LSP目的地PLR    PLR点地址PROT-TYPE    保护类型：link 或者 nodeSTATE    Sub-LSP FRR状态E2E      端到端保护是否使能，取值为enabled或disabled(path overlap)    表示Sub-LSP主路径和备份隧道路径有部分重合，无重合时不显示该字段Backup tunnel    备份隧道ID，备份隧道不存在时填-(hot-standby ready)    备份隧道hot-standby状态，取值为                         hot-standby signal（创建）                          hot-standby ready（已经形成），                         hot-standby active（发生切换）                         hot-standby del（删除）。                         当备份隧道没有创建hot-standby                    LSP时，不显示该字段State    Sub-LSP的端到端保护状态，        取值为none（无保护关系），        creating（正在创建保护关系），        ready（形成保护关系），        active（保护发生切换）
相关命令 : 
无 
## show mpls traffic-eng mtunnels remote-tunnel 

show mpls traffic-eng mtunnels remote-tunnel 
命令功能 : 
1，显示所有P2MP远端隧道的详细信息2，显示指定的P2MP远端隧道的详细信息3，显示指定的P2MP远端隧道的LSP详细信息
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng mtunnels remote-tunnel 
  [tunnel-id 
 ＜tunnel-id 
＞ p2mp-id 
 ＜p2mp-id 
＞ ingress-id 
 ＜ingress-id 
＞ [lsp-id 
 ＜lsp-id 
＞]] 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|指定隧道的 tunnel-id,整数，取值范围1-65535
＜p2mp-id＞|指定隧道的p2mp-id  整数，取值范围1-4294967295，当前的实现是p2mp-id字段填的都是tunnel-id字段的值
＜ingress-id＞|指定隧道的ingress-id 远端隧道头结点的route_id,ip地址A.B.C.D
＜lsp-id＞|指定隧道的指定LSP的lsp-id，整数，取值范围1-65535
缺省 : 
无 
使用说明 : 
1，显示所有P2MP远端隧道的详细信息   ZXROSNG#show mpls traffic-eng mtunnels remote-tunnel2，显示指定的P2MP远端隧道的详细信息ZXROSNG#show mpls traffic-eng mtunnels remote-tunnel tunnel-id 200 p2mp-id 200 ingress-id 100.1.1.2  3，显示指定的P2MP远端隧道的LSP详细信息ZXROSNG#show mpls traffic-eng mtunnels remote-tunnel tunnel-id 200 p2mp-id 200 ingress-id 100.1.1.2 lsp-id 1
范例 : 
1，显示所有P2MP远端隧道的详细信息   ZXROSNG#show mpls traffic-eng mtunnels remote-tunnelName: P2MP tunnel_1 (remote)                          P2MP ID: 1  Leaf tunnel: 60001  VPN ID: 1  LSP Signalling Info:    Source: 100.1.1.1          LSP ID: 34           Integrity: disabled    Priority: 7  7    Resv-Style: SE    Crankback: disabled    Fast-Reroute: disabled                  Sub-LSP to 100.1.1.2                        Recovering: no   Status: up      Upstream Subgroup Originator: 100.1.1.1 Subgroup ID: 1      Downstream Subgroup Originator: - Subgroup ID: -      Forwarding Info:        InLabel: gei-0/1/0/5, 670584        Prev Hop: 10.1.5.1        OutLabel: -, -        Next Hop: -      RSVP Path Info:        Explicit Route: 10.1.5.2 100.1.1.2        Exclude Route: 100.1.1.1        Record Route: 100.1.1.1 10.1.5.1        Tspec: ave rate= 0 kbits, burst= 1000 bytes, peak rate= 0 kbits      RSVP Resv Info:        Record Route: NULL        Fspec: ave rate= 0 kbits, burst= 1000 bytes, peak rate= 0 kbits    History:      Sub-LSP:      Time since created: 0 days, 0 hours, 2 minutes, 50 seconds      Sub-LSP Uptime: 0 days, 0 hours, 2 minutes, 50 seconds  History:    Tunnel:    Time since created: 0 days, 0 hours, 2 minutes, 50 seconds域信息描述表：域    描述Recovering    Sub-LSP是否处于恢复状态,取值为yes或no
相关命令 : 
无 
## show mpls traffic-eng mtunnels summary 

show mpls traffic-eng mtunnels summary 
命令功能 : 
显示当前P2MP隧道的统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng mtunnels summary 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
show mpls traffic-eng mtunnels summary 显示当前本地和远端P2MP隧道的统计信息
范例 : 
ZXROSNG#show mpls traffic-eng mtunnels summarySignalling Summary:  LSP Tunnels Process:            running  RSVP-TE P2MP Process:           running  Forwarding:                     enabled  Reoptimization timer: disabled  Reoptimization events link-up: disabled  Reoptimization cleanup-delay-time: 15s  Reoptimization installation-delay-time(WTR): 10s  Unactive rebuilding frequency: 30s  FRR PLR status: 1 in ready, 0 in active  FRR Promotion: disabled  E2E status: 1 in ready, 0 in active  BFD status: 1 in up             Total  signalling  established  Tunnel:    Local:       2           0            2    Remote:      0    Leaf:        0  LSP:    Local:       2           0            2    Remote:      0  Sub-LSP:    Local:       2           0            2    Remote:      0           0            0Tunnel ID range:  Configurable root tunnel ID: 1 - 200  Configurable leaf tunnel ID: 60001 - 62000  MVPN root tunnel ID: 201 - 400  MVPN leaf tunnel ID: 62001 - 64000域信息描述表：域                                     描述Reoptimization timer           重优化定时时间使能Reoptimization events link-up     重优化事件响应使能Reoptimization cleanup-delay-time     重优化延迟时间Reoptimization installation-delay-time(WTR)重优化延迟切换时间Unactive rebuilding frequency     隧道down定时重建时间FRR PLR status         FRR PLR点的形成保护关系的个数FRR Promotion    FRR         是否使能，使能情况下定时时间。Tunnel ID range          隧道ID范围Configurable root tunnel ID 可由配置界面配置的根隧道ID范围，                                  如范围为0，则显示为noneConfigurable leaf tunnel ID 可由配置界面配置的叶子隧道ID范                                   围，如范围为0，则显示为noneMVPN root tunnel ID            可由MVPN动态创建的根隧道ID范围，                                  如范围为0，则显示为noneMVPN leaf tunnel ID          可由MVPN动态创建的叶子隧道ID范围，                                如范围为0，则显示为noneE2E status      显示Sub-LSP端到端保护状态统计信息 ,                in ready的个数表示保护关系处于                  ready(保护关系创建成功)状态的个数。                  in active的个数表示保护关系处于                  active(切换)状态的个数。BFD status    显示Sub-LSP BFD态统计信息                in up的个数表示BFD检测会话处于                up(BFD 检测会话创建成功)状态的个数。
相关命令 : 
无 
## show mpls traffic-eng mtunnels 

show mpls traffic-eng mtunnels 
命令功能 : 
显示P2MP隧道的详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng mtunnels 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
show mpls traffic-eng mtunnels 命令显示所有的P2MP隧道的信息，包括本地隧道，远端隧道和接入隧道。 
范例 : 
ZXROSNG#show mpls traffic-eng mtunnelsName: P2MP tunnel_1                                   P2MP ID: 1Status:Admin: up  Oper: up    Path: valid      Signalling: connectedP2MP Template: loose-to-3Dest-list identifier: 1Config Parameters:Bandwidth: 0 kbps (Global) Priority: 7  7  Affinity: 0x0/0x0Resv-Style: SEBFD: enabled  min_tx: 900 min_rx: 900 mult: 20 E2E: enabledLSP Signalling Info:Source: 100.1.1.1          LSP ID: 1        Status: upSub-LSP to 100.1.1.2        Recovering: no                          Status: upUpstream Subgroup Originator: - Subgroup ID: -Downstream Subgroup Originator: 100.1.1.1 Subgroup ID: 1Path Option: 1, explicit identifier:1Forwarding Info:InLabel: -, -Prev Hop: -OutLabel: gei-0/1/0/5, 147456Next Hop: 10.1.5.2RSVP Path Info:Explicit Route: 10.1.5.1 10.1.5.2 100.1.1.2Record Route: NULLTspec: ave rate= 0 kbits, burst= 1000 bytes, peak rate= 0 kbitsRSVP Resv Info:Record Route: NULLFspec: ave rate= 0 kbits, burst= 1000 bytes, peak rate= 0 kbitsBFD status: up       BFD tunnel: 65534E2E status: ready    Backup tunnel: 65533History:Sub-LSP:Time since created: 0 days, 0 hours, 1 minutes, 21 secondsSub-LSP Uptime: 0 days, 0 hours, 1 minutes, 19 secondsHistory:Tunnel:Time since created: 0 days, 0 hours, 2 minutes, 4 secondsCurrent LSP: 1 Uptime: 0 days, 0 hours, 1 minutes, 19 secondsName: P2MP tunnel_60001 (leaf)Status: down           Admin: up            Recovering: no       VPN ID: 1Root tunnel ID: 1      P2MP ID: 1           Ingress ID: 100.1.0.0Bound P2P LSPs:  Tunnel-ID        Ingress-ID       Destination      LSP-ID  65530            100.1.1.1        100.1.1.2        1  Name: P2MP tunnel_200 (remote)                        P2MP ID: 200Status:Signalling: upLeaf tunnel: NULLLSP Signalling Info:Source: 100.1.1.2          LSP ID: 1Sub-LSP to 100.1.1.1        Recovering: no                           Status: upUpstream Subgroup Originator: 100.1.1.2 Subgroup ID: 1Downstream Subgroup Originator: 100.1.1.2 Subgroup ID: 1Forwarding Info:InLabel: gei-0/1/0/5, 147456Prev Hop: 10.1.5.2OutLabel: -, 0Next Hop: -RSVP Path Info:Explicit Route: 100.1.1.1Record Route: NULLTspec: ave rate= 0 kbits, burst= 1000 bytes, peak rate= 0 kbitsRSVP Resv Info:Record Route: NULLFspec: ave rate= 0 kbits, burst= 1000 bytes, peak rate= 0 kbitsHistory:Sub-LSP:Time since created: 0 days, 0 hours, 0 minutes, 38 secondsSub-LSP Uptime: 0 days, 0 hours, 0 minutes, 38 secondsHistory:Tunnel:Time since created: 0 days, 0 hours, 0 minutes, 38 secondsCurrent LSP: 1, Uptime: 0 days, 0 hours, 0 minutes, 38 seconds域信息描述表：    根隧道:域    描述Recovering    Sub-LSP是否处于恢复状态, 取值为yes或noBFD    是否使能BFD检测，取值为disabled或enabledE2E    是否使能端到端保护，取值为disabled或enabledmin_tx    BFD 发送检测报文时间间隔，单位毫秒min_rx    BFD接收检测报文时间间隔，单位毫秒mult    BFD检测报文检测间隔个数BFD status    Sub-LSP的BFD检测状态，取值为none（无BFD检测），creating（正在创建BFD检测），up（BFD检测建立成功）BFD tunnel    为Sub-LSP提供BFD检测的P2P隧道IDE2E status    Sub-LSP的端到端保护状态，取值为none（无保护关系），creating（正在创建保护关系），ready（形成保护关系），active（保护发生切换）Backup tunnel    为Sub-LSP提供端到端保护的P2P隧道ID叶子隧道：域    描述Status:    叶子隧道协议状态 ,取值为up或downAdmin:    叶子隧道管理状态，取值为up或downRecovering:    叶子隧道是否正在恢复,取值为yes或noRoot tunnel ID:    绑定的根隧道IDP2MP ID    绑定的根隧道P2MP IDIngress ID    绑定的根隧道route IDVPN ID     叶子隧道接口上的VPN IDBound P2P LSPs    绑定到P2MP叶子隧道上的P2P 备份隧道LSP信息Tunnel-ID    绑定到P2MP叶子隧道上的P2P 备份隧道IDIngress-ID    绑定到P2MP叶子隧道上的P2P 备份隧道头结点router IDDestination    绑定到P2MP叶子隧道上的P2P 备份隧道目的IP地址LSP-ID    绑定到P2MP叶子隧道上的P2P 备份隧道LSP IDP2MP Template  隧道引用的模板名称Path Option   模板下具体配置的路径信息
相关命令 : 
无 
## show mpls traffic-eng resource static-lsp 

show mpls traffic-eng resource static-lsp 
命令功能 : 
显示静态LSP设备资源统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng resource static-lsp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show mpls traffic-eng resource static-lspLSP-Configured     Remainder-Sum4                                 3996
相关命令 : 
无 
## show mpls traffic-eng resource static-tunnel perf-switch 

show mpls traffic-eng resource static-tunnel perf-switch 
命令功能 : 
显示静态隧道流量统计数目 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng resource static-tunnel perf-switch 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show mpls traffic-eng resource static-tunnel perf-switchConfigured      Remainder-Sum5                         995
相关命令 : 
perf-switch on 
## show mpls traffic-eng sd 

show mpls traffic-eng sd 
命令功能 : 
显示当前设备的SD配置信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng sd 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
TE全局下使能SD，配置SD刷新间隔为20秒，通过show命令查看SD配置信息：ZXROSNG(config-mpls-te)#show mpls traffic-eng sd MPLS-TE: EnabledTE SD: EnabledTE SD interval: 20s
相关命令 : 
无 
## show mpls traffic-eng soft-preemption 

show mpls traffic-eng soft-preemption 
命令功能 : 
显示某个设备的软抢占配置和当前发生软抢占的LSP状态 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng soft-preemption 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
TE全局下配置软抢占保活时间为30秒，有一条LSP发生软抢占，在该节点查看软抢占信息：ZXROSNG(config)#show mpls traffic-eng soft-preemption Soft-preemption time-out: 30sThe number of current soft-preempted LSPs: 1TunID LSPID Source         Destination     Pri-S/H Timeout Out-if         1     9     100.1.1.10     100.1.1.30      7/7     29      gei-0/1/0/6
相关命令 : 
无 
## show mpls traffic-eng static autoroute 

show mpls traffic-eng static autoroute 
命令功能 : 
显示所有具有自动路由隧道的状态和配置信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng static autoroute 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示静态隧道自动路由状态及配置:ZXROSNG#show mpls traffic-eng static autorouteMPLS TE static tunnel autorouting enabled     destination 20.20.20.20 has 1 tunnel TunnelName   Destination      State   Nexthop          MetricType  MetricValuetunnel_1     20.20.20.20      Up      20.20.20.20     Absolute    1000
相关命令 : 
无 
## show mpls traffic-eng static brief 

show mpls traffic-eng static brief 
命令功能 : 
显示所有静态隧道的brief信息。
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng static brief 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show mpls traffic-eng static brief ===========================================================================Headers:PU IF      :POSITIVE UP IFPD IF      :POSITIVE DOWN IFRU IF      :REVERSE UP IFRD IF      :REVERSE DOWN IFPROT       :PROTOCOL STATUS===========================================================================Signalling Summary:TUNNEL NAME   PU IF        PD IF        RU IF        RD IF        ADMIN/PROTtunnel_1      -            gei-0/1/0/7  -            -            up/down   tunnel_2      -            gei-0/1/0/7  gei-0/1/0/7  -            up/down   tunnel_40001  gei-0/1/0/8  gei-0/1/0/7  -            -            up/down   tunnel_40002  gei-0/1/0/7  gei-0/1/0/8  gei-0/1/0/8  gei-0/1/0/7  up/down   tunnel_40003  gei-0/1/0/7  -            -            -            up/down   tunnel_40004  gei-0/1/0/7  -            -            gei-0/1/0/7  up/down  ZXROSNG(config)#
相关命令 : 
无 
## show mpls traffic-eng static forwarding-adjacency 

show mpls traffic-eng static forwarding-adjacency 
命令功能 : 
显示静态隧道FA的信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng static forwarding-adjacency 
  [＜dest 
＞] 
命令参数解释 : 
参数|描述
---|---
＜dest＞|静态隧道目的地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show mpls traffic-eng static forwarding-adjacencyMPLS TE forwarding-adjacency enabled   Destination 2.2.2.2 has 1 tunnels   TunnelName  Destination  State  Nexthop       Holdtime  tunnel_1      2.2.2.2     Up    2.2.2.2        300s
相关命令 : 
无 
## show mpls traffic-eng static summary 

show mpls traffic-eng static summary 
命令功能 : 
显示静态隧道的统计信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng static summary 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
Head: 以本节点为头节点的静态隧道的LSP总数（established指协议状态up）。Midpoint:以本节点为中间节点的静态隧道的LSP总数。Tail:以本节点为尾节点的静态隧道的LSP总数。
范例 : 
ZXROSNG#show mpls traffic-eng static summary Signalling Summary:   Head: 6 interface(s), 6 established   Midpoint: 1, Tail: 1
相关命令 : 
无 
## show mpls traffic-eng static 

show mpls traffic-eng static 
命令功能 : 
显示所有静态隧道的信息或只显示指定tunnel-id的单个静态隧道的信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng static 
  [tunnel-id 
 ＜tunnel-id 
＞] 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|tunnel ID 范围1~$#100794387#$
缺省 : 
缺省tunnel-id ＜tunnel-id＞参数，会显示所有静态隧道的信息。 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show mpls traffic-eng static tunnel-id 2001Name: tunnel_2001  Status:     Admin Status: up  Protocol Status: up    Actual Bandwidth： 1,024 kbps  Basic Config Parameters:     Ingress-TnnlID:2001  IngressID:2.2.2.2          EgressID:3.3.3.3            Tunnel Type: Unidirect     Role: Ingress    Policy Class: 6    Tunnel Status: enable  Binded LSP 1  Positive Forward Info:    in-port:     in-label:    out-port: gei-0/1/0/1    out-label: 2001    next-hop: 10.10.10.3              bandwidth: 0
相关命令 : 
无 
## show mpls traffic-eng static-mtunnels brief 

show mpls traffic-eng static-mtunnels brief 
命令功能 : 
显示单条或所有静态P2MP隧道的简要信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng static-mtunnels brief 
  [tunnel-id 
 ＜tunnel-id 
＞] 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|单条静态P2MP隧道的ID，范围为1-4294967295
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示所有静态P2MP隧道的简要信息：ZXROSNG(config-mpls-te)#show mpls traffic-eng static-mtunnels brief TUNNEL NAME         UP IF                 DOWN IF              ADMIN/PROTmte_tunnel1          unknown              unknown              down/down mte_tunnel12         gei-0/1/0/1            gei-0/1/0/7             down/up   mte_tunnel12         gei-0/1/0/1            gei-0/1/0/8             down/up   mte_tunnel13         unknown              unknown              down/down显示单条静态P2MP隧道的简要信息：ZXROSNG(config-mpls-te)#show mpls traffic-eng static-mtunnels brief tunnel-id 2TUNNEL NAME         UP IF                 DOWN IF              ADMIN/PROTmte_tunnel12        gei-0/1/0/1           gei-0/1/0/7          down/upmte_tunnel12        gei-0/1/0/1           gei-0/1/0/8          down/up域信息描述表：信息            描述TUNNEL NAME    静态P2MP隧道名UP IF           上游接口名DOWN IF    下游接口名ADMIN/PROT    管理状态/协议状态
相关命令 : 
show mpls traffic-eng static-mtunnels 
## show mpls traffic-eng static-mtunnels summary 

show mpls traffic-eng static-mtunnels summary 
命令功能 : 
显示静态P2MP隧道的摘要信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng static-mtunnels summary 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
在使能TE的情况下使用该命令。 
范例 : 
显示静态P2MP隧道的摘要信息：ZXROSNG(config-mpls-te)#show mpls traffic-eng static-mtunnels summary Static P2MP Tunnel ID Range:  1-200  401-62000  64001-1000000  1200001-4294967295Static P2MP Tunnel Max Number: 65535Static P2MP Tunnel Remained Number: 65535域                                    描述Static P2MP Tunnel ID Range    静态P2MP隧道ID范围。Static P2MP Tunnel Max Number   静态P2MP隧道可配置最大数目Static P2MP Tunnel Remained Number 静态P2MP隧道剩余可配置最大数目
相关命令 : 
static-mtunnel 
## show mpls traffic-eng static-mtunnels 

show mpls traffic-eng static-mtunnels 
命令功能 : 
显示单条或所有静态P2MP隧道的详细信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng static-mtunnels 
  [tunnel-id 
 ＜tunnel-id 
＞] 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|单条静态P2MP隧道的ID
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示所有静态P2MP隧道的详细信息：ZXROSNG(config-mpls-te)#show mpls traffic-eng static-mtunnels Name: mte_tunnel1  Status:     Admin Status: down  Protocol Status: down  Basic Config Parameters:     Role: unroot    Rate-limit:        Mode: aware             Red: discard        CIR:          9 kbps    CBS:          1 KB        PIR:         10 kbps    PBS:          1 KB    Leaf:      Leaf-tunnel-ID:0                    VPN-ID:0  Binded LSP 1  Forward Info:    In-seg: unknown    Out-seg: unknownName: mte_tunnel12  Status:     Admin Status: down  Protocol Status: up  Basic Config Parameters:     Role: unroot    Leaf:      Leaf-tunnel-ID:12                   VPN-ID:0  Binded LSP 1  Forward Info:    In-seg:      Port:gei-0/1/0/1                    Label:17         Out-seg 1:      Port:gei-0/1/0/7                    Label:112     Next-hop:10.1.1.8    Out-seg 7:      Port:gei-0/1/0/8                    Label:113     Next-hop:20.1.1.9Name: mte_tunnel13  Status:     Admin Status: down  Protocol Status: down  Basic Config Parameters:     Role: unroot  There is no binded LSP
相关命令 : 
show mpls traffic-eng static-mtunnels brief 
## show mpls traffic-eng tunnels backup 

show mpls traffic-eng tunnels backup 
命令功能 : 
显示本地被配置为TE-FRR备份隧道的统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng tunnels backup 
  [te-tunnel 
 ＜te-tunnel-id 
＞] 
命令参数解释 : 
参数|描述
---|---
＜te-tunnel-id＞|隧道ID
缺省 : 
无 
使用说明 : 
无 
范例 : 
[M6000\M6000-S]:ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels backupName: tunnel_7LSP Head: Tunnel7   Admin: up  Oper: upSrc:100.1.1.1,Dest: 100.1.1.3,Instance:1Fast Reroute Backup Provided:Protected i/fs: gei-0/1/0/2Protected lsps: 0Backup BW: 0kbps;inuse: 0kbps[ZSR]:ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels backupName: tunnel_7LSP Head: Tunnel7   Admin: up  Oper: upSrc:100.1.1.1,Dest: 100.1.1.3,Instance:1Fast Reroute Backup Provided:Protected i/fs: gei-1/2Protected lsps: 0Backup BW: 0kbps;inuse: 0kbps[89\9900]:ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels backupName: tunnel_7LSP Head: Tunnel7   Admin: up  Oper: upSrc:100.1.1.1,Dest: 100.1.1.3,Instance:1Fast Reroute Backup Provided:Protected i/fs: gei-0/1/0/2Protected lsps: 0Backup BW: 0kbps;inuse: 0kbps
相关命令 : 
show mpls traffic-eng tunnels [{brief|summary|te_tunnel <tunnel_id> }] 
## show mpls traffic-eng tunnels brief 

show mpls traffic-eng tunnels brief 
命令功能 : 
显示TE隧道的简要信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng tunnels brief 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show mpls traffic-eng tunnels brief Signalling Summary:    LSP Tunnels Process:            running    RSVP Process:                   running    Forwarding:                     enabledTUNNEL NAME           DESTINATION     UP IF          DOWN IF        STATE/PROTtunnel_1              20.20.20.20     -              gei-0/1/0/2    up/uptunnel_2              20.20.20.20     -              gei-0/1/0/1    up/uptunnel_65531 (MBK)    100.1.1.3       -              gei-0/1/0/7    up/up      tunnel_65531 (MBKHOT) 100.1.1.3       -              gei-0/1/0/5    up/uptunnel_65532 (MBFD)   100.1.1.3       -              gei-0/1/0/1    up/up域信息描述表：域    描述(MBK)    带有此标记的P2P LSP，是P2MP Sub-LSP的端到端保护的备份隧道LSP(MBKHOT)    带有此标记的P2P LSP，是P2MP Sub-LSP的端到端保护的备份隧道的hot LSP(MBFD)    带有此标记的P2P LSP，是P2MP Sub-LSP的BFD检测LSP
相关命令 : 
show mpls traffic-eng tunnels [{brief|summary|te_tunnel <tunnel_id> | backup}] 
## show mpls traffic-eng tunnels interface 

show mpls traffic-eng tunnels interface 
命令功能 : 
动态TE显示指定接口已承载的所有TE LSP信息的功能 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng tunnels interface 
  ＜interface-name 
＞ 
命令参数解释 : 
参数|描述
---|---
＜interface-name＞|需要显示的隧道的出接口名
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show mpls traffic-eng tunnels interface smartgroup1Tunnel-ID     LSP-ID        Ingress-ID          Egress-ID           33            1             11.1.1.1            22.2.2.2            34            1             11.1.1.1            22.2.2.2            35            1             11.1.1.1            22.2.2.2            36            1             11.1.1.1            22.2.2.2            37            1             11.1.1.1            22.2.2.2            38            1             11.1.1.1            22.2.2.2            39            1             11.1.1.1            22.2.2.2            40            1             11.1.1.1            22.2.2.2            41            1             11.1.1.1            22.2.2.2            42            1             11.1.1.1            22.2.2.2            43            1             11.1.1.1            22.2.2.2            44            1             11.1.1.1            22.2.2.2            45            1             11.1.1.1            22.2.2.2            46            1             11.1.1.1            22.2.2.2   域信息描述表：域    描述Tunnel-ID    隧道号LSP-ID    LSP号Ingress-ID    隧道头节点Egress-ID    隧道尾节点
相关命令 : 
无 
## show mpls traffic-eng tunnels pce-auto-init brief 

show mpls traffic-eng tunnels pce-auto-init brief 
命令功能 : 
显示PCE自动生成隧道的简要信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng tunnels pce-auto-init brief 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show mpls traffic-eng tunnels pce-auto-init briefSignalling Summary:LSP Tunnels Process:runningRSVP Process:runningForwarding:enabledTUNNEL-NAME           TUNNEL-ID      DESTINATION     DOWN IF        STATE/PROTpce_test1             32768           22.2.2.2       gei-0/1/0/1        up/uppce_test1 (hot)       32768           22.2.2.2       gei-0/1/0/1        up/up域信息描述表：域    描述LSP Tunnels Process: 表示隧道正在运行过程中RSVP Process:        表示RSVP模块正在运行过程中Forwarding:          表示转发正在运行过程中TUNNEL NAME          隧道名TUNNEL-ID            隧道IDDESTINATION          隧道目的地DOWN IF              隧道本节点出接口STATE/PROT           隧道状态(hot)                PCE自动生成的hot LSP
相关命令 : 
show mpls traffic-eng tunnels [{brief|summary|te_tunnel <tunnel_id> }] 
## show mpls traffic-eng tunnels policy-class 

show mpls traffic-eng tunnels policy-class 
命令功能 : 
显示所有已配置的TE隧道策略类别或只显示指定tunnel-id的单个TE隧道的策略类别配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng tunnels policy-class 
  [te-tunnel 
 ＜te-tunnel-id 
＞] 
命令参数解释 : 
参数|描述
---|---
＜te-tunnel-id＞|隧道ID，取值范围:1~$#100794387#$
缺省 : 
缺省te-tunnel ＜para＞参数，会显示所有已配置的TE隧道策略类别。 
使用说明 : 
无 
范例 : 
ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels policy-class TUNNEL NAME     POLICY CLASStunnel_1        3           tunnel_2        defaulttunnel_2001     6ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels policy-class te-tunnel 1             TUNNEL NAME     POLICY CLASStunnel_1        3 
相关命令 : 
无 
## show mpls traffic-eng tunnels remote-tunnel 

show mpls traffic-eng tunnels remote-tunnel 
命令功能 : 
显示远程MPLS隧道的详细信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng tunnels remote-tunnel 
  [tunnel-id 
 ＜tunnel-id 
＞ lsp-id 
 ＜lsp-id 
＞ ingress-id 
 ＜ingress-id-address 
＞ egress-id 
 ＜egress-ip-address 
＞] 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|需要显示的远程隧道的隧道号,ID范围为：1~$#100794374#$
＜lsp-id＞|需要显示的远程隧道的实例号
＜ingress-id-address＞|需要显示的远程隧道的头节点地址
＜egress-ip-address＞|需要显示的远程隧道的尾节点地址
缺省 : 
无 
使用说明 : 
无 
范例 : 
1、P2MP隧道show命令显示ZXROSNG# show mpls traffic-eng tunnels remote-tunnelName: tunnel_65533      (P2MP BFD)(Tunnel65533) Destination: 100.1.1.3  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/6, 642494    OutLabel: -    Rvs-InLabel: -, -    Rvs-OutLabel: gei-0/1/0/6, 423429    Lsp_is_recovery: FALSE    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65533, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: 100.1.1.2 10.1.6.2 100.1.1.1                    10.1.1.1      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 0 minute, 16 second    Current LSP: Uptime:0 day, 0 hour, 0 minute, 16 secondName: tunnel_65535      (P2MP backup)(Tunnel65535) Destination: 100.1.1.3  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/7, 642491    OutLabel: -    Rvs-InLabel: -, -    Rvs-OutLabel: gei-0/1/0/7, 622904    Lsp_is_recovery: FALSE    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65535, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.7.3 100.1.1.3      Exclude Route: NULL      Record Route: 100.1.1.1 10.1.7.1      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 11 minute, 8 second    Current LSP: Uptime:0 day, 0 hour, 11 minute, 8 second域信息描述表：域    描述(P2MP BFD)    隧道是P2MP Sub-LSP的BFD检测隧道,则显示该字段，否则不显示(P2MP backup)    隧道是P2MP Sub-LSP的端到端备份隧道，则显示该字段，否则不显示Association P2MP tunnel ID    该隧道关联的P2MP 隧道ID, P2MP Sub-LSP的端到端备份隧道和BFD检测隧道才显示该字段2、P2P GMPLS隧道源N侧该show命令显示ZXROSNG#show mpls traffic-eng tunnels remote-tunnelName: 123     (Tunnel5) Destination: 100.1.1.40  Status:    Signalling: up  RSVP Signalling Info :    Switch Type: EVPL    InLabel: gei-0/20/0/1, 1    OutLabel: gei-0/20/0/3, 2    Rvs-InLabel: gei-0/20/0/3, 2    Rvs-OutLabel: gei-0/20/0/1, 1    Lsp_is_recovery: FALSESrc 100.1.1.10, Dst 100.1.1.40, Tun-ID 5, Tun-Instance 65500    UL(Upstream Label) DL(Downstream Label) UI(Unnumbered If)    RSVP Path Info:      Explicit Route: 100.1.1.20(UI:501) 100.1.1.20(UI:502)                      100.1.1.30(UL:77 DL:77 UI:504) 100.1.1.40(UI:505)      Exclude Route: 100.1.1.20(UI:601)      Record Route: 100.1.1.10  100.1.1.10(UI:500)       Tspec: CIR= 2 kb, CBS= 6 byte, EIR= 3 kb, EBS= 8 byte      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: 100.1.1.30(UL:2 DL:2)  100.1.1.30(UL:2 DL:2 UI:503)                     100.1.1.40(UL:77 DL:77)  100.1.1.40(UL:77 DL:77 UI:505)       Fspec: CIR= 2 kb, CBS= 6 byte, EIR= 3 kb, EBS= 8 byte  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 0 minute, 37 second    Current LSP: Uptime:0 day, 0 hour, 0 minute, 36 second域信息描述表：域    描述UL(Upstream Label) DL(Downstream Label) UI(Unnumbered If)：缩写注释，UL(Upstream Label)上游标签、DL(Downstream Label)下游标签、UI(Unnumbered If)未编号接口，上述缩写在Explicit Route、Exclude Route、Record Route字段中使用。Switch Type: 隧道交换类型，如EVPL。Explicit Route: 隧道本节点ERO信息，中间点源N侧格式：本地入接口+本地出接口+目的N侧出接口（建议标签）+目的C侧入接口；中间点目的N侧格式：本地入接口+目的N侧出接口（建议标签）+目的C侧入接口。PATH方向Record Route: PATH报文经过节点信息，格式：经过节点的RouterID+出接口。Resv方向Record Route: RESV报文经过节点信息，格式：经过节点的RouterID（出、入标签）+出接口（出、入标签）。Tspec：Sender_Tspec，path方向携带带宽内容，包括CIR（承诺信息速率）、CBS（承诺突发尺寸）、EIR（超额速率）、EBS（超额突发尺寸）。Fspec：Flowspec，resv方向携带带宽内容，包括CIR（承诺信息速率）、CBS（承诺突发尺寸）、EIR（超额速率）、EBS（超额突发尺寸）。注：GMPLS隧道中接口均使用（Router id+Local if id）表示，如接口100.1.1.20(UI:501)。Lsp_is_recovery:表示这条LSP是否是GR恢复出来的，是GR恢复的就是TRUE，否则就是FALSE。
相关命令 : 
无 
## show mpls traffic-eng tunnels summary 

show mpls traffic-eng tunnels summary 
命令功能 : 
显示TE隧道的统计信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng tunnels summary 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
范例中Tunnel ID Range:部分几个字段的取值由不同项目的性能参数决定，范例中的显示仅供参考。 
范例 : 
[M6000\M6000-S\ZSR]ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels summary MPLS-TE: EnabledSignalling Summary:   LSP Tunnels Process:            running   RSVP Process:                   running   Forwarding:                     enabled   Head: 1000 interface(s), 0 active signalling attempt(s), 0 established   Midpoint: 0, Tail: 0   Reoptimization timer frequency:0s   Reoptimization cleanup-delay-time:15s   Reoptimization installation-delay-time(WTR):10s   FRR Promotion: disabled, Frequency:300s   AutoBW Sample Timer: enabled, Frequency:300sTunnel ID Range:   Ingress tunnel id: 1 - 32768   Access tunnel id: 32769 - 64511   Auto backup tunnel id: 64512 - 65535[89\9900]ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels summaryMPLS-TE: EnabledSignalling Summary:LSP Tunnels Process:            runningRSVP Process:                   runningForwarding:                     enabledHead: 5 interfaces, 6 active signalling attempts, 6 establishedMidpoints: 0, Tails: 1域信息描述表：域    描述Next-hop Routing Without-CSPF ：表示MPLS-TE隧道中间节点是否使能不依赖CSPF算路直接生成ERO功能enabled ：已配置使能中间节点不依赖CSPF算路直接生成ERO功能disabled ：未配置使能中间节点不依赖CSPF算路直接生成ERO功能CSPF Best-effort Without-BW ：表示MPLS-TE隧道是否使能针对带宽条件的尽力算路功能enabled ：已配置使能针对带宽条件的尽力算路功能（即针对有带宽要求的SE预留风格TE隧道算路，首先按照满足带宽条件的要求进行算路，如果失败的话，则继续按照无带宽条件的要求进行算路。）disabled ：未配置使能针对带宽条件的尽力算路功能CSPF Preferred-IGP ：表示MPLS-TE隧道是否指定某种IGP算路协议进行CSPF算路功能OSPF ：已配置指定使用OSPF算路协议进行CSPF算路功能ISIS ：已配置指定使用ISIS算路协议进行CSPF算路功能disabled ：未配置指定使用某种IGP算路协议进行CSPF算路功能
相关命令 : 
show mpls traffic-eng tunnels [{brief|summary|te_tunnel <tunnel_id> | backup}] 
## show mpls traffic-eng tunnels 

show mpls traffic-eng tunnels 
命令功能 : 
显示相关TE隧道的指定信息 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show mpls traffic-eng tunnels 
  [te_tunnel 
 ＜tunnel_id 
＞] {[hot-standby 
]|[pre-setup 
]} 
命令参数解释 : 
参数|描述
---|---
＜tunnel_id＞|指定的具体tunnel id,取值范围：1~$#100794374#$
hot-standby|要求显示的是相关隧道的hot-standby信息
pre-setup|要求显示的是相关隧道的pre-setup LSP信息
缺省 : 
无 
使用说明 : 
如果指定tunnel id，则只显示对应tunnel id的隧道。如果带hot-standby字段，则显示的是相关隧道的HSB保护情况。如果带pre-setup字段，则显示的是相关隧道的预建立LSP的信息。
范例 : 
1、该show命令显示普通动态隧道ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnelsName: tunnel_2      (Tunnel2) Destination: 44.4.4.4  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected    Path option: 1, type dynamic (Basis for Setup)    Pre-setup Path: explicit identifier: 1 (Basis for Setup)    Actual Bandwidth: N/A    Hot-standby protection:      protect option: 1, type dynamic (Basis for Setup)    PCE-authorized: NO    PCE-auto-init tunnel: NO    Active-MPLS-binding-SID: 965536  Config Parameters:    Resv-Style: SE    Metric Type: IGP (default)   Upper Limit: 4294967295    Hop Prior: disabled         Upper Limit: -    Record-Route: enabled    Facility Fast-reroute: disabled    Detour Fast-reroute: disabled    Protect Coexist: disabled    Protect Nest: enabled    Main LSP Fast-reroute Block: enabled    Bandwidth Protection: disabled    Hot-standby-lsp Fast-reroute: disabled    E2E: disabled    BFD: disabled    Policy Class: Default    Track Name:     Auto-reoptimize: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Reference Hot-standby: disabled    Tunnel-Status: enabled    SRLG Collect Type: force    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    Main affinity(Name):      Exclude-any: 0aad3(0) 1aad3(1) 2aad3(2) 3aad3(3) 4aad3(4) 5aad3(5)                   6aad3(6) 7aad3(7) 8aad3(8)      Include-any: 9aad3(9) aaad3(10) baad3(11) caad3(12) daad3(13) eaad3(14)                   faad3(15) gaad3(16) haad3(17) iaad3(18) jaad3(19)      Include-all: kaad3(20) laad3(21) maad3(22) naad3(23) oaad3(24) paad3(25)                   qaad3(26) raad3(27) saad3(28) taad3(29) uaad3(30) vaad3(31)      Undefined : HSB affinity(Name):      Exclude-any: 0aad3(0) 1aad3(1) 2aad3(2) 3aad3(3) 4aad3(4) 5aad3(5)                   6aad3(6) 7aad3(7) 8aad3(8)      Include-any: 9aad3(9) aaad3(10) baad3(11) caad3(12) daad3(13) eaad3(14)                   faad3(15) gaad3(16) haad3(17) iaad3(18) jaad3(19)      Include-all: kaad3(20) laad3(21) maad3(22) naad3(23) oaad3(24) paad3(25)                   qaad3(26) raad3(27) saad3(28) taad3(29) uaad3(30)      Undefined : a2    FRR affinity(Name):      Exclude-any: red(3)      Include-any:      Include-all:      Undefined:   green    AutoRoute: disabled    AUTO-BW:(86400/86378)    Samples Collected Times: 0   Next: 30s    Sampling-bw:0kbps  Requested-bw:0kbps    Adjust Range(kbps):0-unconstrained(0) Multiple:100%    Overflow: Enable  Limit: 0/10  Percent:10% Bandwidth:100kbps          Total AdjCount:0  Last AdjBw:0kbps    Underflow: Enable  Limit: 0/10  Percent: 10%  Bandwidth: 100kbps           Total AdjCount: 0  Last AdjBw: 0kbps    Forwarding-adjacency: disabled    Co-routed Bidirect: disabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled  InLabel: -  OutLabel: gei-0/1/0/5, 3  Lsp_is_recovery: FALSE  RSVP Signalling Info :    Src 11.1.1.1, Dst 44.4.4.4, Tun-ID 2, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.20.5.1 10.20.5.4 44.4.4.4      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb    RSVP Resv Info:      Record Route: 44.4.4.4(3) 10.20.5.4(3)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hour, 0 minute, 59 second    Prior LSP: path option 1    Current LSP: Uptime:0 day, 0 hour, 0 minute, 46 second    Last LSP Error Information:Name: tunnel_2      (Tunnel2) Destination: 44.4.4.4  Status:    Signalling: up    Actual Bandwidth: N/A    Hot-standby protection:    PCE-authorized: NO    PCE-auto-init tunnel: NO    Active-MPLS-binding-SID: 965535  Config Parameters:    BFD: disabled    Hot-standby-lsp Fast-reroute: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    Main affinity(Bit position):      Exclude-any: 3      Include-any: None      Include-all: None    HSB affinity(Bit position):      Exclude-any: None      Include-any: None      Include-all: None    FRR affinity(Bit position):      Exclude-any: 10      Include-any: None      Include-all: None    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: disabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled  InLabel: -  OutLabel: gei-0/1/0/2, 208221  Lsp_is_recovery: FALSE  RSVP Signalling Info :    Src 11.1.1.1, Dst 44.4.4.4, Tun-ID 2, Tun-Instance 2    RSVP Path Info:      Explicit Route: 10.20.2.1 10.20.2.2 10.20.9.2                      10.20.9.4 44.4.4.4      Exclude Route: 10.20.5.4      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb    RSVP Resv Info:      Record Route: 22.2.2.2(208221) 10.20.2.2(208221)                    44.4.4.4(3) 10.20.9.4(3)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 day, 0 hours, 1 minutes, 20 seconds    Time Since Up    : 0 days, 0 hours, 0 minutes,55 seconds    Prior LSP: path option 1    Current LSP: Uptime:0 days, 0 hours, 0 minutes, 55 seconds    Last LSP Error Information:Name: tunnel_1      (pre-setup)(Tunnel1) Destination: 22.2.2.2  Status:    Signalling: up    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    Without-CSPF: disabled  InLabel: -  OutLabel: gei-0/1/0/2, 3  LSP recoverd from GR: NO  RSVP Signalling Info :    Src 11.1.1.1, Dst 22.2.2.2, Tun-ID 1, Tun-Instance 3    RSVP Path Info:      Explicit Route: 20.1.1.1 20.1.1.2 22.2.2.2      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kbps, burst= 1000 byte, peak rate= 0 kbps    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kbps, burst= 1000 byte, peak rate= 0 kbps  History:    Tunnel:    Time Since Created: 0 days, 1 hours, 16 minutes, 52 seconds    Time Since Up     : 0 days, 0 hours, 39 minutes, 56 seconds    Prior LSP(pre-setup): explicit ID 1    Current LSP: Uptime:0 days, 0 hours, 38 minutes, 26 secondsLast LSP Error Information:Name: tunnel_1      (remote)(Tunnel1) Destination: 22.2.2.2  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/5, 3    OutLabel: -    Lsp_is_recovery: FALSE    Src 11.1.1.1, Dst 22.2.2.2, Tun-ID 1, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.20.9.2 22.2.2.2      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 2 days, 15 hours, 49 minutes, 26 seconds    Current LSP: Uptime:2 days, 15 hours, 49 minutes, 26 secondsName: tunnel_65531      (P2MP backup)(Tunnel65531) Destination: 100.1.1.3  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected    No path options defined    Actual Bandwidth: N/A    Hot-standby protection:      No path options protected    PCE-authorized: NO  Config Parameters:    Resv-Style: SE    Metric Type: IGP (default)   Upper Limit: 4294967295    Hop Prior: disabled         Upper Limit: -    Record-Route: disabled    Facility Fast-reroute: disabled    Detour Fast-reroute: disabled    Bandwidth Protection: disabled    Hot-standby-lsp Fast-reroute: disabled    E2E: disabled    BFD: enabled         connect         up                      min_tx: 900     min_rx: 900     mult: 20         Policy Class: N/A    Track Name:     Auto-reoptimize: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Reference Hot-standby: disabled    Tunnel-Status: disabled    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: enabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled  InLabel: -  OutLabel: gei-0/1/0/7, 642493  Rvs-InLabel: gei-0/1/0/7, 622907  Rvs-OutLabel: -  Lsp_is_recovery: FALSE  RSVP Signalling Info :    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65531, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.7.1 10.1.7.3 100.1.1.3      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1    RSVP Resv Info:      Record Route: 100.1.1.3(642493) 10.1.7.3(642493)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 days, 0 hours, 31 minutes, 58 seconds    Time Since Up    : 0 days, 0 hours, 31 minutes,57 seconds    Prior LSP: path option 0    Current LSP: Uptime:0 days, 0 hours, 31 minutes, 57 secondsLast LSP Error Information:Name: tunnel_65531      (P2MP backup hot)(Tunnel65531) Destination: 100.1.1.3  Status:    Signalling: up    Actual Bandwidth: N/A    Hot-standby protection:    PCE-authorized: NO  Config Parameters:    BFD: disabled    Hot-standby-lsp Fast-reroute: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: enabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled  InLabel: -  OutLabel: gei-0/1/0/5, 423430  Rvs-InLabel: gei-0/1/0/5, 622904  Rvs-OutLabel: -  Lsp_is_recovery: FALSE  RSVP Signalling Info :    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65533, Tun-Instance 2    RSVP Path Info:      Explicit Route: 10.1.5.1 10.1.5.2 10.1.6.2                      10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1    RSVP Resv Info:      Record Route: 100.1.1.2(423430) 10.1.5.2(423430)                    100.1.1.3(642495) 10.1.6.3(642495)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 days, 0 hours, 5 minutes, 39 seconds    Time Since Up    : 0 days, 0 hours, 0 minutes,14 seconds    Prior LSP: path option 0    Current LSP: Uptime:0 days, 0 hours, 0 minutes, 14 seconds    Last LSP Error Information:Name: tunnel_65533      (P2MP BFD)(Tunnel65533) Destination: 100.1.1.3  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected    No path options defined    Actual Bandwidth: N/A    Hot-standby protection:      No path options protected    PCE-authorized: NO  Config Parameters:    Resv-Style: SE    Metric Type: IGP (default)   Upper Limit: 4294967295    Hop Prior: disabled         Upper Limit: -    Record-Route: disabled    Facility Fast-reroute: disabled    Detour Fast-reroute: disabled    Bandwidth Protection: disabled    Hot-standby-lsp Fast-reroute: disabled    E2E: disabled    BFD: enabled         connect         up                      min_tx: 900     min_rx: 900     mult: 10         Policy Class: N/A    Track Name:     Auto-reoptimize: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Reference Hot-standby: disabled    Tunnel-Status: disabled    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: enabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled  InLabel: -  OutLabel: gei-0/1/0/1, 423428  Rvs-InLabel: gei-0/1/0/1, 622905  Rvs-OutLabel: -  Lsp_is_recovery: FALSE  RSVP Signalling Info :    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65533, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.1.1 10.1.1.2 10.1.6.2                      10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1    RSVP Resv Info:      Record Route: 100.1.1.2(423428) 10.1.1.2(423428)                    100.1.1.3(642494) 10.1.6.3(642494)      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 days, 0 hours, 25 minutes, 55 seconds    Time Since Up    : 0 days, 0 hours, 25 minutes,55 seconds    Prior LSP: path option 0    Current LSP: Uptime:0 days, 0 hours, 25 minutes, 55 seconds    Last LSP Error Information:Name: tunnel_65532      (remote P2MP backup)(Tunnel65532) Destination: 100.1.1.3  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/7, 642493    OutLabel: -    Rvs-InLabel: -, -    Rvs-OutLabel: gei-0/1/0/7, 622905    Lsp_is_recovery: FALSE    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65533, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.7.3 100.1.1.3      Exclude Route: NULL      Record Route: 100.1.1.1 10.1.7.1      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 days, 0 hours, 1 minutes, 32 seconds    Current LSP: Uptime:0 days, 0 hours, 1 minutes, 32 secondsName: tunnel_65534      (remote P2MP BFD)(Tunnel65534) Destination: 100.1.1.3  Status:    Signalling: up  RSVP Signalling Info :    InLabel: gei-0/1/0/6, 642494    OutLabel: -    Rvs-InLabel: -, -    Rvs-OutLabel: gei-0/1/0/6, 423429    Lsp_is_recovery: FALSE    Src 100.1.1.1, Dst 100.1.1.3, Tun-ID 65534, Tun-Instance 1    RSVP Path Info:      Explicit Route: 10.1.6.3 100.1.1.3      Exclude Route: NULL      Record Route: 100.1.1.2 10.1.6.2 100.1.1.1                    10.1.1.1      Tspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb      Association P2MP tunnel ID: 1      Affinity(Bit position):        Exclude-any: None        Include-any: None        Include-all: None    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 1000 byte, peak rate= 0 kb  History:    Tunnel:    Time Since Created: 0 days, 0 hours, 1 minutes, 33 seconds    Current LSP: Uptime:0 days, 0 hours, 1 minutes, 33 seconds分段路由隧道显示ZXROSNG(config-mpls-te)#show mpls traffic-eng tunnels te_tunnel 1Name: tunnel_1      (Tunnel1) Destination: 33.3.3.3  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected    Path option: 1, type dynamic (Basis for Setup)    Actual Bandwidth:                N/A      Tunnel Utilize:              N/A    Actual Bandwidth In:             N/A      Tunnel Utilize In:           N/A    Hot-standby protection:      No path options protected    PCE-authorized: NO  Config Parameters:    Resv-Style: SE    Metric Type: IGP (default)   Upper Limit: 4294967295    Hop Prior: disabled         Upper Limit: -    Record-Route: disabled    Facility Fast-reroute: disabled    Detour Fast-reroute: disabled    Bandwidth Protection: disabled    Hot-standby-lsp Fast-reroute: disabled    E2E: disabled    BFD: disabled    Policy Class: Default    Track Name:     Auto-reoptimize: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Reference Hot-standby: disabled    Tunnel-Status: enabled    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    Affinity(Bit position):      Exclude-any: None      Include-any: None      Include-all: None    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: disabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: disabled    Advertise None-null: disabled    Segment-routing: enabled  InLabel: -  OutLabel: -, -  Lsp_is_recovery: FALSE  RSVP Signalling Info :    Src 10.1.1.2, Dst 33.3.3.3, Tun-ID 1, Tun-Instance 1    RSVP Path Info:      Explicit Route: NULL      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kb, burst= 0 byte, peak rate= 0 kb    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kb, burst= 0 byte, peak rate= 0 kb  SR Segment ID Info :    SID[1]:      UNNUMB_ADJv4: 10.1.1.2 20.30.1.1 20.30.1.2 33.3.3.3    Splice-label: N/A  History:    Tunnel:    Time Since Created: 0 days, 7 hours, 13 minutes, 24 seconds    Time Since Up    : 0 days, 7 hours, 13 minutes,22 seconds    Prior LSP: path option 1    Current LSP: Uptime:0 days, 7 hours, 13 minutes, 22 seconds    Last LSP Error Information:域信息描述表：域    描述(hot)    隧道hot LSP(remote)    远端隧道PCE-authorized    隧道是否授权成功YES：成功NO： 不成功PCE-auto-init tunnel  是否是PCE自动生成隧道YES：是PCE自动生成隧道NO： CLI手工配置的隧道Active-MPLS-binding-SID: 当前实际分配的MPLS-binding-SIDPCE-initiate    隧道下是否使能了PCE主动创建TE LSP功能enabled：使能disabled：不使能(P2MP BFD)    隧道是P2MP Sub-LSP的BFD检测隧道,则显示该字段，否则不显示(remote P2MP BFD)    远端隧道是P2MP Sub-LSP的BFD检测隧道,则显示该字段，否则不显示(P2MP backup)    隧道是P2MP Sub-LSP的端到端备份隧道，则显示该字段，否则不显示(P2MP backup hot)    隧道是P2MP Sub-LSP的端到端备份隧道hot LSP，则显示该字段，否则不显示(remote P2MP backup)    远端隧道是P2MP Sub-LSP的端到端备份隧道，则显示该字段，否则不显示Association P2MP tunnel ID    该隧道关联的P2MP 隧道ID, P2MP Sub-LSP的端到端备份隧道和BFD检测隧道才显示该字段Segment-routing 表示是否是分段路由隧道SR Segment ID Info 当隧道类型为分段路由隧道时，显示每一跳分段路由信息。                                     SID，分段ID；UNNUMB_ADJv4: 隧道所经过节点的router ID和接口地址Splice-label 拼接标签相关信息Lsp_is_recovery:表示这条lsp是否是gr恢复出来的，是gr恢复的就是TRUE，否则就是FALSE。SRLG Collect Type:隧道头节点显示隧道使能SRLG收集类型，如未使能则该字段不显示。2、P2P GMPLS隧道该show命令显示ZXROSNG# show mpls traffic-eng tunnelsName: 123      (Tunnel5) Destination: 100.1.1.40  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected    No path options defined    Actual Bandwidth:                N/A      Tunnel Utilize:              N/A    Actual Bandwidth In:             N/A      Tunnel Utilize In:           N/A    Hot-standby protection:      No path options protected    PCE-authorized: YES  Config Parameters:    Resv-Style: SE    Metric Type: IGP (default)   Upper Limit: 4294967295    Hop Prior: disabled         Upper Limit: -    Record-Route: disabled    Facility Fast-reroute: disabled    Detour Fast-reroute: disabled    Bandwidth Protection: disabled    Hot-standby-lsp Fast-reroute: disabled    E2E: disabled    BFD: disabled    Policy Class: Default    Track Name:     Auto-reoptimize: disabled    Hot-standby-lsp Auto-reoptimize: disabled    Reference Hot-standby: disabled    Tunnel-Status: enabled    SRLG Collect Type: best-effort    Bandwidth: 0 kbps (Global) Priority: 7  7    CBS: 0 byte  EIR: 0 kbps  EBS: 0 byte    Affinity(Bit position):      Exclude-any: None      Include-any: None      Include-all: None    AutoRoute: disabled    AUTO-BW: disabled    Forwarding-adjacency: disabled    Co-routed Bidirect: disabled    Associated Bidirect: disabled    Rate-limit: disabled    Crankback: disabled    Soft Preemption: disabled    Soft Preemption Status: not pending    Addresses of preempting links: 0.0.0.0    Graceful shutdown address: NULL    Without-CSPF: disabled    Ultralimit discard: disabled    PCE-initiate: enabled    Advertise None-null: disabled    Segment-routing: disabled  Switch Type: EVPL  InLabel: -  OutLabel: gei-0/20/0/1, 1  Rvs-InLabel: gei-0/20/0/1, 1  Rvs-OutLabel: -  Lsp_is_recovery: FALSE  RSVP Signalling Info :     Src 100.1.1.10, Dst 100.1.1.40, Tun-ID 5, Tun-Instance 65500     UL(Upstream Label) DL(Downstream Label) UI(Unnumbered If)    RSVP Path Info:      Explicit Route: 100.1.1.10(UI:500) 100.1.1.20(UI:501)                      100.1.1.30(UI:504) 100.1.1.40(UI:505)      Exclude Route: 100.1.1.20(UI:601)      Record Route: NULL      Tspec: CIR= 0 kb, CBS= 0 byte, EIR= 0 kb, EBS= 0 byte    RSVP Resv Info:      Record Route: 100.1.1.20(UL:1 DL:1)  100.1.1.20(UL:1 DL:1 UI:501)                     100.1.1.30(UL:2 DL:2)  100.1.1.30(UL:2 DL:2 UI:503)                     100.1.1.40(UL:77 DL:77)  100.1.1.40(UL:77 DL:77 UI:505)       Fspec: CIR= 0 kb, CBS= 0 byte, EIR= 0 kb, EBS= 0 byte  History:    Tunnel:    Time Since Created: 0 days, 0 hours, 2 minutes, 21 seconds    Time Since Up    : 0 days, 0 hours, 2 minutes,21 seconds    Prior LSP: path option 0    Current LSP: Uptime:0 day, 0 hours, 0 minutes, 5 seconds    Last LSP Error Information:域信息描述表：域    描述Switch Type: 隧道交换类型，如EVPL。UL(Upstream Label) DL(Downstream Label) UI(Unnumbered If)：缩写注释，UL(Upstream Label)上游标签、DL(Downstream Label)下游标签、UI(Unnumbered If)未编号接口，上述缩写在Explicit Route、Exclude Route、Record Route字段回显内容中使用。Explicit Route: 隧道本节点ERO信息，头节点源C侧格式：源C侧出接口+源N侧入接口+目的N侧出接口+目的C侧入接口；中间点源N侧格式：本地入接口+本地出接口+目的N侧出接口（建议标签）+目的C侧入接口；目的N侧格式：本地入接口+目的N侧出接口（建议标签）+目的C侧入接口。PATH方向Record Route:  PATH报文经过节点信息，格式：经过节点的RouterID+出接口。Resv方向Record Route:：RESV报文经过节点信息，格式：经过节点的RouterID（出、入标签）+出接口（出、入标签）。Tspec：Sender_Tspec，path方向携带带宽内容，包括CIR（承诺信息速率）、CBS（承诺突发尺寸）、EIR（超额速率）、EBS（超额突发尺寸）。Fspec：Flowspec，resv方向携带带宽内容，包括CIR（承诺信息速率）、CBS（承诺突发尺寸）、EIR（超额速率）、EBS（超额突发尺寸）。
Protect Coexist :  隧道是否使能保护共存Protect Nest     :  隧道是否使能嵌套保护Main LSP Fast-reroute Block: 隧道是否使能主LSP FRR禁用注：GMPLS隧道中接口均使用（Router id+Local if id）表示，如接口100.1.1.20(UI:501)。Lsp_is_recovery:表示这条lsp是否是gr恢复出来的，是gr恢复的就是TRUE，否则就是FALSE。SRLG Collect Type:隧道头节点显示隧道使能SRLG收集类型，如未使能则该字段不显示。Pre-setup Path: 隧道显示配置的pre-setup的路径信息3、P2P 隧道 pre-setup LSP显示命令ZXROSNG# show mpls traffic-eng tunnels pre-setupName: tunnel_1      (Tunnel1) Destination: 22.2.2.2  Status:    Admin: up  Oper: up  Path:  valid  Signalling: connected  Config Parameters:    Pre-setup Path: explicit identifier: 1 (Basis for Setup)  InLabel: -  OutLabel: gei-0/1/0/2, 3  LSP recoverd from GR: NO  RSVP Signalling Info :    Src 11.1.1.1, Dst 22.2.2.2, Tun-ID 1, Tun-Instance 3    RSVP Path Info:      Explicit Route: 20.1.1.1 20.1.1.2 22.2.2.2      Exclude Route: NULL      Record Route: NULL      Tspec: ave rate= 0 kbps, burst= 1000 byte, peak rate= 0 kbps    RSVP Resv Info:      Record Route: NULL      Fspec: ave rate= 0 kbps, burst= 1000 byte, peak rate= 0 kbpsName: 隧道名称Destination: 隧道目的地IPStatus:Admin: 隧道管理状态  Oper: 隧道运行状态 Path: 路径是否有效  Signalling: 信令状态Config Parameters: 配置参数Pre-setup Path: pre-lsp关联的路径信息InLabel: 入标签OutLabel: 出接口，出标签LSP recoverd from GR: 是否从GR恢复RSVP Signalling Info :信令信息Src: 源地址IPDst： 目的地IPTun-ID：隧道IDTun-Instance: LSP IDExplicit Route: 隧道本节点ERO信息PATH方向Record Route:  PATH报文经过节点信息。Resv方向Record Route:：RESV报文经过节点信息。Tspec：Sender_Tspec，path方向携带带宽内容，包括CIR（承诺信息速率）、CBS（承诺突发尺寸）、EIR（超额速率）、EBS（超额突发尺寸）。Fspec：Flowspec，resv方向携带带宽内容，包括CIR（承诺信息速率）、CBS（承诺突发尺寸）、EIR（超额速率）、EBS（超额突发尺寸）。
相关命令 : 
show mpls traffic-eng tunnels [{brief|summary|te_tunnel <tunnel_id> | backup}] 
## show rsvp bandwidth interface 

show rsvp bandwidth interface 
命令功能 : 
显示接口带宽信息。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show rsvp bandwidth interface 
  [＜interface name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜interface name＞|接口名
缺省 : 
无 
使用说明 : 
无 
范例 : 
1.显示接口带宽信息，动态预留类型、接口带宽为1000、bc0为10：ZXROSNG(config-mpls-te-if-smartgroup1)#show rsvp bandwidth interface config: Reserved bandwidth is defined for the future TE-LSP (kbps)maxAvail: Maximum bandwidth can be allocated (kbps)used: Bandwidth is allocated for the existed TE-LSP (kbps)Interface smartgroup1               config     maxAvail         usedStaticreserve            0bc0                0            0            0bc1                0            0            0bc2                0            0            0bc3                0            0            0bc4                0            0            0bc5                0            0            0bc6                0            0            0bc7                0            0            0Dynamicreserve         1000bc0               10            0            0bc1                0            0            0bc2                0            0            0bc3                0            0            0bc4                0            0            0bc5                0            0            0bc6                0            0            0bc7                0            0            02. 仅配置lmp data link命令以及全局te（非non-te带宽预留模型），不配置te接口带宽，也有回显。lmp接口的最大可以带宽直接就是接口speed 100G，配置最大值默认为4294967295，且只分配为动态带宽ZXROSNG(config)#show rsvp bandwidth interface  gei-0/1/0/2config: Reserved bandwidth is defined for the future TE-LSP (kbps)maxAvail: Maximum bandwidth can be allocated (kbps)used: Bandwidth is allocated for the existed TE-LSP (kbps)Interface: gei-0/1/0/2 Static perflow: 0            Dynamic perflow: 0 Static percent: 0            Dynamic percent: 100 Static EIR: 0                Dynamic EIR: 0 Static speed blind: disabled Dynamic speed blind: disabled               Config     MaxAvail         UsedStaticreserve            0            0            0Dynamicreserve   4294967295      1000000            0
相关命令 : 
无 
## show rsvp bandwidth model 

show rsvp bandwidth model 
命令功能 : 
显示带宽模型。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show rsvp bandwidth model 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示配置的ds-te模型：ZXROSNG(config-mpls-te-if-smartgroup1)#show rsvp bandwidth model RSVP bandwidth model: RDM
相关命令 : 
无 
## show rsvp bandwidth occupied-information 

show rsvp bandwidth occupied-information 
命令功能 : 
显示带宽资源管理模块的带宽占用情况。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show rsvp bandwidth occupied-information 
  [＜Interface name 
＞] 
命令参数解释 : 
参数|描述
---|---
＜Interface name＞|接口名
缺省 : 
无 
使用说明 : 
1、对于普通的TE接口（如vlan、以太口等非隧道类型接口），显示在接口上预留了带宽的隧道；2、对于隧道接口，打印TE OVER TE功能中在隧道接口上预留了带宽的隧道，以及打印PW OVER TE功能中在隧道接口上预留了带宽的伪线：3、对于接口下预留的静态隧道，打印的隧道名是本地隧道名，即localtunnelid对应的隧道名，因为静态隧道的带宽是配置在本地隧道上的。4、对于接口下预留的动态隧道，打印的隧道名是头结点的隧道名，即ingresstunnelid对应的隧道名，因为动态隧道的带宽是配置在头结点隧道上的。5、MPLS-TE模式隧道在接口预留的是普通带宽，DS-TE模式隧道在接口上预留的是CT带宽，所以在打印接口上预留的隧道信息时，非DS-TE（MPLS-TE模式）和DS-TE打印的带宽格式略有不同。
范例 : 
1、DS-TE模式显示所有接口和隧道上的带宽占用情况：ZXROSNG(config)#show rsvp bandwidth occupied-informationInterface: vlan1  Static te_tunnel1    ClassType 0 Bandwidth: 1000 kbps  Dynamic mte_tunnel1    IngressID 11.1.1.1, EgressID 22.2.2.2, LSPID 2    ClassType 1 Bandwidth: 1000 kbps    ClassType 5 Bandwidth: 1000 kbps    Interface: gei-0/1/0/1  Dynamic te_tunnel10    IngressID 11.1.1.1, EgressID 22.2.2.2, LSPID 1    ClassType 2 Bandwidth: 1000 kbps    ClassType 4 Bandwidth: 1000000 kbps  Dynamic mte_tunnel20    IngressID 11.1.1.1, EgressID 22.2.2.2, LSPID 2    ClassType 0 Bandwidth: 1000 kbps    ClassType 7 Bandwidth: 1000 kbpsInterface: te_tunnel1  TunnelName          Bandwidth  te_tunnel2          1000 kbps  te_tunnel4          1000 kbps  PWName              Bandwidth  pw1                 1000 kbps  pw6                 1000 kbps2、DS-TE模式显示vlan1接口上的带宽占用情况：ZXROSNG(config)#show rsvp bandwidth occupied-information vlan1Interface: vlan1  Static te_tunnel1    ClassType 0 Bandwidth: 1000 kbps  Dynamic mte_tunnel1    IngressID 11.1.1.1, EgressID 22.2.2.2, LSPID 2    ClassType 1 Bandwidth: 1000 kbps    ClassType 5 Bandwidth: 1000 kbps3、MPLS-TE模式显示所有接口和隧道上的带宽占用情况：ZXROSNG(config)#show rsvp bandwidth occupied-informationInterface: vlan1  Static te_tunnel1    Bandwidth: 1000 kbps  Dynamic mte_tunnel1    IngressID 11.1.1.1, EgressID 22.2.2.2, LSPID 2    Bandwidth: 1000 kbps    Interface: gei-0/1/0/1  Dynamic te_tunnel10    IngressID 11.1.1.1, EgressID 22.2.2.2, LSPID 1    Bandwidth: 1000 kbps  Dynamic mte_tunnel20    IngressID 11.1.1.1, EgressID 22.2.2.2, LSPID 2    Bandwidth: 1000 kbpsInterface: te_tunnel1  TunnelName          Bandwidth  te_tunnel2          1000 kbps  te_tunnel4          1000 kbps  PWName              Bandwidth  pw1                 1000 kbps  pw6                 1000 kbps4、MPLS-TE模式显示vlan1接口上的带宽占用情况：ZXROSNG(config)#show rsvp bandwidth occupied-information vlan1Interface: vlan1  Static te_tunnel1    Bandwidth: 1000 kbps  Dynamic mte_tunnel1    IngressID 11.1.1.1, EgressID 22.2.2.2, LSPID 2    Bandwidth: 1000 kbps域信息描述表：信息        描述Interface   接口名，受带宽管理接口的接口名。Static      静态隧道名，包括在接口上预留的静态P2P隧道和静态P2MP隧道。Dynamic     动态隧道名，包括在接口上预留的动态P2P隧道和动态P2MP隧道。IngressID   隧道头结点的router ID。EgressID    隧道尾节点的router ID。LSPID       隧道的LSPID。ClassType   带宽的级别类型，DS-TE模式隧道可以配置八种类型带宽。Bandwidth   带宽值，隧道或者伪线业务上预留的带宽值。TunnelName  隧道名，TE OVER TE业务中，OVER在隧道接口上的隧道名。PWName      伪线名，伪线绑定隧道场景中，绑定在隧道接口上的伪线名。
相关命令 : 
无 
## show te-class-mapping 

show te-class-mapping 
命令功能 : 
显示全局配置的TE-CLASS映射关系。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show te-class-mapping 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
显示te-class映射关系：ZXROSNG(config-mpls-te-if-smartgroup1)#show te-class-mapping te-class-mapping 0 class-type 0 preemption-priority 1
相关命令 : 
无 
## signalling refresh interval 

signalling refresh interval 
命令功能 : 
配置发送刷新报文时间间隔。使用no命令恢复默认时间间隔 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
signalling refresh interval 
  ＜refresh-interval 
＞
no signalling refresh interval 
命令参数解释 : 
参数|描述
---|---
＜refresh-interval＞|发送刷新报文的时间，范围：5000–65535000，单位：毫秒
缺省 : 
默认刷新时间为30000毫秒 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)# signalling refresh interval 60000ZXROSNG(config-mpls-te)#show ip rsvp refresh parameter RSVP-TE: Enabled    RSVP signalling refresh interval: 60000 msecs    RSVP signalling refresh misses  : 4
相关命令 : 
无 
## signalling refresh misses 

signalling refresh misses 
命令功能 : 
配置丢失刷新报文的数目，如果丢失了指定数目的刷新报文，则RSVP将删除对应的消息保存状态 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
signalling refresh misses 
  ＜refresh-misses-number 
＞
no signalling refresh misses 
命令参数解释 : 
参数|描述
---|---
＜refresh-misses-number＞|丢失刷新报文的数目，范围：2–10
缺省 : 
缺省为4 
使用说明 : 
无
范例 : 
配置MPLS流量工程丢失刷新报文的数目为6个：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)# signalling refresh misses 6查看配置结果信息：ZXROSNG(config-mpls-te)#show ip rsvp refresh parameter RSVP-TE: Enabled    RSVP signalling refresh interval: 60000 msecs    RSVP signalling refresh misses  : 6
相关命令 : 
无 
## signalling refresh reduction 

signalling refresh reduction 
命令功能 : 
使能摘要刷新，可减少刷新报文数目 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
signalling refresh reduction 
 
no signalling refresh reduction 
命令参数解释 : 
					无
				 
缺省 : 
不使能 
使用说明 : 
使能此功能前需使能重传
范例 : 
使能摘要刷新：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)# signalling refresh reduction
相关命令 : 
signalling retransmit 
## signalling retransmit interval 

signalling retransmit interval 
命令功能 : 
配置发送报文重传时间间隔。使用no命令恢复默认时间间隔 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
signalling retransmit interval 
  ＜retransmit-interval 
＞
no signalling retransmit interval 
命令参数解释 : 
参数|描述
---|---
＜retransmit-interval＞|报文重传的时间，范围：500–60000，单位：毫秒
缺省 : 
默认重传时间为1000毫秒 
使用说明 : 
无 
范例 : 
配置MPLS流量工程发送重传报文时间间隔为2000毫秒：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)# signalling retransmit interval 2000
相关命令 : 
无 
## signalling retransmit limit 

signalling retransmit limit 
命令功能 : 
配置重传报文次数，超过此次数后不再重传。使用no命令恢复默认次数 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
signalling retransmit limit 
  ＜retransmit-misses-number 
＞
no signalling retransmit limit 
命令参数解释 : 
参数|描述
---|---
＜retransmit-misses-number＞|重传报文的次数，范围：2–10
缺省 : 
缺省为3个消息 
使用说明 : 
无 
范例 : 
配置MPLS流量工程重传报文次数为6个：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)# signalling retransmit limit 6
相关命令 : 
无 
## signalling retransmit 

signalling retransmit 
命令功能 : 
使能RSVP 重传，如果收不到确认消息，将报文重传。使用no命令取消该功能 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
signalling retransmit 
 
no signalling retransmit 
命令参数解释 : 
					无
				 
缺省 : 
默认无配置 
使用说明 : 
no此功能时会关联删除摘要刷新功能 
范例 : 
配置RSVP 重传功能：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#signalling retransmit
相关命令 : 
signalling refresh reduction 
## static 

static 
命令功能 : 
配置MPLS-TE静态隧道节点。使用no命令删除该隧道节点配置。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
static 
  ＜para 
＞
no static 
  ＜para 
＞
				
命令参数解释 : 
参数|描述
---|---
＜para＞|隧道名称，隧道ID范围在运行的时候从项目的性能参数中取值
缺省 : 
无 
使用说明 : 
无 
范例 : 
1.配置静态隧道节点：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#2.删除静态隧道节点：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#no static te_tunnel1
相关命令 : 
router-id <ip-address>show mpls traffic-eng static [tunnel-id <tunnel-id>]
## static-mtunnel 

static-mtunnel 
命令功能 : 
配置静态P2MP隧道，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
static-mtunnel 
  ＜mte-tunnel-interface 
＞
no static-mtunnel 
  ＜mte-tunnel-interface 
＞
				
命令参数解释 : 
参数|描述
---|---
＜mte-tunnel-interface＞|静态P2MP隧道ID，隧道ID取值范围由接口性能参数控制，同时要排除以下几个范围：201~400、62001~64000、1000001~1200000
缺省 : 
无 
使用说明 : 
配置该命令后进入静态P2MP隧道模式。 
范例 : 
配置静态P2MP隧道：ZXROSNG(config#mpls traffic-engZXROSNG(config-mpls-te)#static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static-mte_tunnel1)#
相关命令 : 
无 
track : 

track 
命令功能 : 
配置MPLS-TE静态隧道关联检测告警对象，使用no命令删除配置的track对象。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
track 
  ＜track name 
＞
no track 
命令参数解释 : 
参数|描述
---|---
＜track name＞|track对象名，用1-31个字符表示
缺省 : 
不配置MPLS-TE静态隧道关联检测告警对象。 
使用说明 : 
track对象名要求1到31个字符。 
范例 : 
1.设置静态隧道1的track名称为ffff：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#track ffff2.删除静态隧道1的track名称：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)#no track
相关命令 : 
show mpls traffic-eng static [tunnel-id <tunnel-id>] | include Track Name 
## tunnel destination 

tunnel destination 
命令功能 : 
在隧道接口下配置隧道的目的地址，使用no命令清除该配置。 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel destination 
 ipv4 
 ＜ip-address 
＞
no tunnel destination 
命令参数解释 : 
参数|描述
---|---
＜ip-address＞|IPv4地址，作为隧道的目的地址
缺省 : 
隧道无目的地址 
使用说明 : 
无 
范例 : 
配置隧道的目的为100.1.1.2ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)# tunnel destination ipv4 100.1.1.2
相关命令 : 
无 
## tunnel mpls traffic-eng bandwidth 

tunnel mpls traffic-eng bandwidth 
命令功能 : 
配置隧道的带宽信息，包括承诺带宽、承诺突发尺寸、超额速率、超额突发尺寸。使用no命令清除该配置。 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mpls traffic-eng bandwidth 
  ＜bandwidth 
＞ [{kbps 
|mbps 
|gbps 
}] [{[cbs 
 ＜cbs 
＞ [{byte 
|kb 
|mb 
}]],[eir 
 ＜eir 
＞ [{kbps 
|mbps 
|gbps 
}]],[ebs 
 ＜ebs 
＞ [{byte 
|kb 
|mb 
}]]}]
no tunnel mpls traffic-eng bandwidth 
命令参数解释 : 
参数|描述
---|---
＜bandwidth＞|用户配置的隧道承诺带宽，范围：1–4294967295，默认单位：kbit/s，无效值：0。
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜cbs＞|用户配置的隧道承诺突发尺寸，范围：1–4294967295，单位：byte，无效值：0。
byte|以BYTE为单位
kb|以KB为单位
mb|以MB为单位
＜eir＞|用户配置的隧道超额速率，范围：1–4294967295，默认单位：kbit/s，无效值：0。
kbps|以kbit/s为单位
mbps|以Mbit/s为单位
gbps|以Gbit/s为单位
＜ebs＞|用户配置的隧道超额突发尺寸，范围：1–4294967295，默认单位：byte，无效值：0。
byte|以BYTE为单位
kb|以KB为单位
mb|以MB为单位
缺省 : 
无 
使用说明 : 
1.配置隧道的预留带宽，限制通过隧道的最大流量。支持当链路拥塞的时候，TE流量区分业务丢弃。根据流量的的QoS优先级确定转发优先级：优先级1>优先级2>优先级3>其他。没有带宽预留的隧道也会执行这个动作。2.与隧道限速功能互斥
范例 : 
1.配置隧道te_tunnel1的承诺带宽为20000kbps，承诺突发尺寸为2000byte，超额速率为10000kbps，超额突发尺寸为1000byte（带默认单位）：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng bandwidth 20000 cbs 2000 eir 10000 ebs 10002.删除隧道的带宽配置：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#no tunnel mpls traffic-eng bandwidth3.配置隧道 te_tunnel1的承诺带宽为20000kbit/s，承诺突发尺寸为2000byte，超额速率为10000kbit/s，超额突发尺寸为1000byte（带非默认单位）：ZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng bandwidth 20 mbps cbs 2 mb eir 10mbps ebs 1 mbZXROSNG(config-mpls-te-tunnel-te_tunnel1)#show thistunnel mpls traffic-eng bandwidth 20000 cbs 2000 eir 10000 ebs 1000
相关命令 : 
show mpls traffic-eng tunnels 
## tunnel mpls traffic-eng fast-reroute 

tunnel mpls traffic-eng fast-reroute 
命令功能 : 
配置TE隧道支持fast reroute功能。 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mpls traffic-eng fast-reroute 
  {facility 
|one-to-one 
} [bw-protect 
]
no tunnel mpls traffic-eng fast-reroute 
命令参数解释 : 
参数|描述
---|---
facility|配置FRR方式为facility
one-to-one|配置FRR方式为one-to-one (Detour)
bw-protect|使能FRR带宽保护
缺省 : 
隧道默认不使能FRR方式及FRR带宽保护 
使用说明 : 
1、两种方式的FRR不可以直接切换，是互斥关系。必须将一种先NO掉，才可以配置另一种。FRR的使能需要依赖于RRO的使能。2、只有配置了FRR方式，才能配置FRR带宽保护；3、FRR方式：facility和one-to-one是互斥的；4、no命令表征：删除掉所有FRR功能，保括FRR方式和FRR带宽保护；5、本命令采用覆盖方式配置，参见“范例4”；6、在配置了FRR带宽保护的场景下，如果仅仅去掉带宽保护，而要保留FRR方式的配置：不能使用no命令，仅配置FRR方式即可。参见“范例4”。
范例 : 
1、隧道配置 one-to-one方式的FRRZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te)# tunnel mpls traffic-eng record-routeZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng fast-reroute one-to-one2、隧道配置facility 方式的FRR ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)# tunnel mpls traffic-eng fast-reroute facilityZXROSNG(config-mpls-te-tunnel-te_tunnel1)#3、隧道配置facility 方式的FRR及FRR带宽保护方法1ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)# tunnel mpls traffic-eng fast-reroute facilityZXROSNG(config-mpls-te-tunnel-te_tunnel1)# tunnel mpls traffic-eng fast-reroute facility bw-protect方法2ZXROSNG(config-mpls-te-tunnel-te_tunnel1)# tunnel mpls traffic-eng fast-reroute facility bw-protect4、在配置了FRR带宽保护的场景下，如果仅仅去掉带宽保护，而要保留FRR方式的配置ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)# tunnel mpls traffic-eng fast-reroute facility bw-protectZXROSNG(config-mpls-te-tunnel-te_tunnel1)# tunnel mpls traffic-eng fast-reroute facility5、清除隧道的所有FRR功能（包括FRR方式及FRR带宽保护）ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)# no tunnel mpls traffic-eng fast-reroute
相关命令 : 
tunnel mpls traffic-eng record-routeshow mpls traffic-eng fast-rerouteshow mpls traffic-eng tunnels backup
## tunnel mpls traffic-eng hot-standby preferred-igp 

tunnel mpls traffic-eng hot-standby preferred-igp 
命令功能 : 
指定隧道HSB路由优先使用某种IGP路由进行CSPF算路。 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mpls traffic-eng hot-standby preferred-igp 
  {ospf 
 [process 
 ＜OSPF process ID 
＞ [area 
 ＜OSPF area ID 
＞]]|isis 
 [process 
 ＜ISIS process ID 
＞ [{level-1 
|level-2 
}]]}
no tunnel mpls traffic-eng hot-standby preferred-igp 
命令参数解释 : 
参数|描述
---|---
ospf|优先使用OSPF协议进行CSPF算路。
process|配置优先使用的IGP协议的实例。
＜OSPF process ID＞|优先使用的IGP协议的实例号。OSPF协议的范围为1~65535。
area|配置优先使用的OSPF协议的区域。
＜OSPF area ID＞|区域标识符。范围为0.0.0.0~ff.ff.ff.ff。
isis|优先使用ISIS协议进行CSPF算路。
process|配置优先使用的IGP协议的实例。
＜ISIS process ID＞|优先使用的IGP协议的实例号。ISIS协议的范围为0~65535。
level-1|优先使用处于level-1区域的路径。
level-2|优先使用处于level-2区域的路径。
缺省 : 
不使能该功能 
使用说明 : 
若指定路由优先使用的协议路由存在时，则按照配置的路由进行隧道HSB算路。如果指定路由优先使用的协议路由不存在时，按原有的实现方式选择算路。若不配置该命令，隧道HSB路由则按照全局配置的优先算路路由进行CSPF算路。
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng hot-standby  preferred-igp isis process 33 level-1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#no tunnel mpls traffic-eng hot-standby preferred-igp
相关命令 : 
cspf preferred-igp 
## tunnel mpls traffic-eng path-option 

tunnel mpls traffic-eng path-option 
命令功能 : 
在TE隧道下配置一个路径选项 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mpls traffic-eng path-option 
  ＜path-option-id 
＞ {explicit-path 
 {name 
 ＜explicit-path-of-name 
＞|identifier 
 ＜explici-path-of-id 
＞}|dynamic 
} [lockdown 
]
no tunnel mpls traffic-eng path-option 
  ＜path-option-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜path-option-id＞|选项编号，范围：1–16
name|关联的显式路径是名称方式
＜explicit-path-of-name＞|使用的显式路径名称，长度1-64个字符
identifier|关联的显式路径是ID方式
＜explici-path-of-id＞|使用的显式路径的数字标识，范围：1–65535
dynamic|使用的显式路径为动态计算路径方式
lockdown|在此路径选项上开启防范禁闭功能，如果隧道使用此path_option建立起来，则不会进行重优化操作，除非隧道变DOWN。
缺省 : 
隧道无该配置 
使用说明 : 
无 
范例 : 
配置隧道的路径选项1为动态建路：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)# tunnel mpls traffic-eng path-option 1 dynamic
相关命令 : 
无 
## tunnel mpls traffic-eng preferred-igp 

tunnel mpls traffic-eng preferred-igp 
命令功能 : 
指定隧道路由优先使用某种IGP路由进行CSPF算路。 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mpls traffic-eng preferred-igp 
  {ospf 
 [process 
 ＜OSPF process ID 
＞ [area 
 ＜OSPF area ID 
＞]]|isis 
 [process 
 ＜ISIS process ID 
＞ [{level-1 
|level-2 
}]]}
no tunnel mpls traffic-eng preferred-igp 
命令参数解释 : 
参数|描述
---|---
ospf|优先使用OSPF协议进行CSPF算路。
process|配置优先使用的IGP协议的实例。
＜OSPF process ID＞|优先使用的IGP协议的实例号。OSPF协议的范围为1~65535。
area|配置优先使用的OSPF协议的区域。
＜OSPF area ID＞|区域标识符。范围为0.0.0.0~ff.ff.ff.ff。
isis|优先使用ISIS协议进行CSPF算路。
process|配置优先使用的IGP协议的实例。
＜ISIS process ID＞|优先使用的IGP协议的实例号。ISIS协议的范围为0~65535。
level-1|优先使用处于level-1区域的路径。
level-2|优先使用处于level-2区域的路径。
缺省 : 
不使能该功能 
使用说明 : 
若指定路由优先使用的协议路由存在时，则按照配置的路由进行隧道算路。如果指定路由优先使用的协议路由不存在时，按原有的实现方式选择算路。若不配置该命令，隧道路由则按照全局配置的优先算路路由进行CSPF算路。
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng preferred-igp ospf process 1 area 1.1.1.1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#no tunnel mpls traffic-eng preferred-igp
相关命令 : 
cspf preferred-igp 
## tunnel mpls traffic-eng record-route 

tunnel mpls traffic-eng record-route 
命令功能 : 
使能tunnel的路径记录功能（RRO）。使用no命令关闭tunnel的路径记录功能。 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mpls traffic-eng record-route 
 
no tunnel mpls traffic-eng record-route 
命令参数解释 : 
					无
				 
缺省 : 
无该配置 
使用说明 : 
默认情况下关闭tunnel的路径记录功能，使能fast reroute 功能时必须先使能此功能，否则配置不成功，no此功能时会关联删除fast reroute 功能和配置。 
范例 : 
ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng record-route
相关命令 : 
tunnel mpls traffic-eng fast-reroute{facility | one-to-one} 
## tunnel mpls traffic-eng resv-style 

tunnel mpls traffic-eng resv-style 
命令功能 : 
配置隧道资源预留风格 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mpls traffic-eng resv-style 
  {se 
|ff 
}
no tunnel mpls traffic-eng resv-style 
命令参数解释 : 
参数|描述
---|---
se|配置资源预留SE（Shared Explicit）风格
ff|配置资源预留FF（Fixed Filter）风格
缺省 : 
缺省情况下资源预留风格为SE风格 
使用说明 : 
配置FF风格，为每个发送端单独预留资源；配置SE风格，为指定发送端共享资源。FF风格和FRR配置互斥：若隧道下先使能了FRR功能，则FF风格不能配置；若隧道下先配置了FF风格，则FRR功能不能配置。
范例 : 
配置FF风格：ZXROSNG(config)# mpls traffic-engZXROSNG(config-mpls-te)# tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng resv-style ff 配置SE风格：ZXROSNG(config)# mpls traffic-engZXROSNG(config-mpls-te)# tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng resv-style se
相关命令 : 
tunnel mpls traffic-eng fast-reroute {facility | one-to-one} 
## tunnel mpls traffic-eng without-cspf 

tunnel mpls traffic-eng without-cspf 
命令功能 : 
开启MPLS TE隧道模式下不依赖CSPF路由计算，直接生成TE隧道建路所需要的PATH报文的显式路径对象(即ERO:Explicit Route Object)的功能。 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel mpls traffic-eng without-cspf 
 
no tunnel mpls traffic-eng without-cspf 
命令参数解释 : 
					无
				 
缺省 : 
关闭该功能（即需要进行CSPF计算，生成TE隧道建路所需要的PATH报文ERO信息） 
使用说明 : 
开启该功能后，MPLS-TE动态隧道可以根据Path option关联的显式路径信息，直接生成ERO，并且将PATH报文按照此ERO中的路径描述发送到下一个节点。关闭该功能后，MPLS-TE动态隧道则依赖CSPF路由计算的结果来生成ERO信息。
范例 : 
Tunnel 1开启不依赖CSPF路由计算，根据Path option关联的显式路径信息直接生成ERO的功能ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel mpls traffic-eng without-cspf
相关命令 : 
无 
## tunnel 

tunnel 
命令功能 : 
进入到隧道配置的子模式，配置该隧道接口 
命令模式 : 
 MPLS-TE模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel 
  ＜te-tunnel-interface 
＞
no tunnel 
  ＜te-tunnel-interface 
＞
				
命令参数解释 : 
参数|描述
---|---
＜te-tunnel-interface＞|隧道ID，范围在运行的时候从项目的性能参数中取值。
缺省 : 
默认无该配置 
使用说明 : 
配置tunnel之前，需要先在全局模式创建tunnel逻辑接口 
范例 : 
配置进入隧道te_tunnel1的接口配置子模式ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1
相关命令 : 
无 
## tunnel 

tunnel 
命令功能 : 
动态隧道激活/去激活。 
命令模式 : 
 MPLS-TE隧道接口模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|隧道激活
disable|隧道去激活
缺省 : 
隧道激活。 
使用说明 : 
动态隧道配置去激活，转发不通，但不影响隧道信令状态，默认是隧道激活。 
范例 : 
1.激活动态隧道：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel enable2.去激活动态隧道：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#tunnel te_tunnel1ZXROSNG(config-mpls-te-tunnel-te_tunnel1)#tunnel disable
相关命令 : 
show mpls traffic-eng tunnels [tunnel-id <tunnel-id>] | include Tunnel-Status 
## tunnel 

tunnel 
命令功能 : 
静态隧道激活/去激活。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|隧道激活
disable|隧道去激活
缺省 : 
隧道激活。 
使用说明 : 
静态隧道配置去激活，转发不通，但不影响隧道信令状态，默认是隧道激活。 
范例 : 
1.激活静态隧道：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1 ZXROSNG(config-mpls-te-static-te_tunnel1)#tunnel enable 2.去激活静态隧道：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1 ZXROSNG(config-mpls-te-static-te_tunnel1)#tunnel disable
相关命令 : 
show mpls traffic-eng static [tunnel-id <tunnel-id>] | include Tunnel-Status 
## tunnel 

tunnel 
命令功能 : 
静态P2MP隧道激活/去激活。 
命令模式 : 
 MPLS-TE静态P2MP隧道模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|隧道激活
disable|隧道去激活
缺省 : 
隧道激活。 
使用说明 : 
静态P2MP隧道去激活后转发不通，但不影响隧道协议状态。 
范例 : 
1.激活静态P2MP隧道：ZXROSNG(config)#mpls traffic-engZZXROSNG(config-mpls-te)#static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static-mte_tunnel1)#tunnel enable ZXROSNG(config-mpls-te-static-mte_tunnel1)#2.去激活静态P2MP隧道：ZXROSNG(config)#mpls traffic-engZZXROSNG(config-mpls-te)#static-mtunnel mte_tunnel1ZXROSNG(config-mpls-te-static-mte_tunnel1)#tunnel disableZXROSNG(config-mpls-te-static-mte_tunnel1)#
相关命令 : 
show mpls traffic-eng static-mtunnel [tunnel-id <tunnel-id>] | include Tunnel-Status 
## ultralimit 

ultralimit 
命令功能 : 
配置静态隧道支持流量超限丢弃功能。 
命令模式 : 
 MPLS-TE静态隧道配置模式  
命令默认权限级别 : 
15 
命令格式 : 
ultralimit 
 discard 
no ultralimit 
 discard 
命令参数解释 : 
参数|描述
---|---
discard|使能流量超限丢弃
缺省 : 
默认流量超限不丢弃 
使用说明 : 
无 
范例 : 
使能流量超限丢弃功能：ZXROSNG(config)#mpls traffic-engZXROSNG(config-mpls-te)#static te_tunnel1ZXROSNG(config-mpls-te-static-te_tunnel1)# ultralimit discard
相关命令 : 
show mpls traffic-eng static 
# MPLS-TP OAM配置命令 
## lm on-demand 

lm on-demand 
命令功能 : 
配置该MEG的按需LM功能。lm功能包括按需和预激活模式，两模式能同时开启。按需的LM检测实现单向的丢包率测量，需要实现丢包率计算并根据计算结果判断是否产生告警，按需LM时需要实现LMM/ LMR报文的生成、发送和接收。 
命令模式 : 
 TPOAM-MEG模式  
命令默认权限级别 : 
15 
命令格式 : 
lm on-demand 
 phb-name 
 {be 
|af11 
|af12 
|af21 
|af22 
|af31 
|af32 
|af41 
|af42 
|cs6 
|cs7 
|ef 
} [{[sendtime 
 ＜send-time-value 
＞],[period 
 ＜period-value 
＞]}]
no lm on-demand 
命令参数解释 : 
参数|描述
---|---
be|作用：PHB类型：Best effort范围：无默认值：cs7
af11|作用：PHB类型：Assured forwarding 11范围：无默认值：cs7
af12|作用：PHB类型：Assured forwarding 11范围：无默认值：cs7
af21|作用：PHB类型：Assured forwarding 11范围：无默认值cs7
af22|作用：PHB类型：Assured forwarding 11范围：无默认值：cs7
af31|作用：PHB类型：Assured forwarding 11范围：无默认值：cs7
af32|作用：PHB类型：Assured forwarding 11范围:无默认值：cs7
af41|作用：PHB类型：Assured forwarding 11范围：无默认值：cs7
af42|作用：PHB类型：Assured forwarding 11范围：无默认值：cs7
cs6|作用：PHB类型：Class selector 6范围：无默认值：cs7
cs7|作用：PHB类型：Class selector 7范围：无默认值：cs7
ef|作用：PHB类型：Expedited forwarding范围：无默认值：cs7
＜send-time-value＞|作用：按需LM功能执行时间范围：10-86400，单位秒默认值：无限长
＜period-value＞|作用：按需LM功能的发包周期范围：1-100，单位100毫秒默认值：1秒
缺省 : 
无 
使用说明 : 
当需要配置特定MEG的按需LM功能时使用。配置该命令前需要保证链路的建立。当使能按需lm时，为了保证采集的数据不异常，开启远端的计数器，需要两端同时使能按需lm功能。按需lm结果去使能时不清掉，当下次再使能时才重新清掉记录新的结果。
范例 : 
ZXROSNG(config-tp-oam-section-1-meg-1)#lm on-demand phb-name ef g8114        ZXROSNG(config-tp-oam-section-1-meg-1)#
相关命令 : 
可以通过show mpls-tp oam meg 1 lm-info来查看按需LM功能的结果 
## lm proactive 

lm proactive 
命令功能 : 
对该MEG配置预激活LM功能。lm功能包括按需和预激活模式。两模式能同时开启。主动的LM检测实现双向的丢包率测量，需要实现丢包率计算并根据计算结果判断是否需要产生告警，支持主动LM时必须以支持CCM功能为基础。CCM报文发送周期和CC功能配置的报文发送周期一致。 
命令模式 : 
 TPOAM-MEG模式  
命令默认权限级别 : 
15 
命令格式 : 
lm proactive 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|作用：预激活LM功能使能范围：无默认值：去使能
disable|作用：预激活LM功能去使能范围：无默认值：去使能
缺省 : 
缺省的预激活LM功能为去使能 
使用说明 : 
当需要配置特定MEG的预激活LM功能使能和去使能时使用。配置该命令前需要保证链路的建立。配置该命令前需要两端cv都使能。当cv周期是慢包时，lm报文由平台处理；当cv周期是快包时，由项目上报统计结果及相关告警。
范例 : 
ZXROSNG(config-tp-oam-section-1-meg-1)#lm proactive enable g8114ZXROSNG(config-tp-oam-section-1-meg-1)#
相关命令 : 
在配置预激活LM功能前，需要先使能CV功能。 
# 繁殖配置命令 
## oam-propagate phb-name 

oam-propagate phb-name 
命令功能 : 
在Section实体下指定客户层FDI报文的phb值。 
命令模式 : 
 繁殖section实体模式  
命令默认权限级别 : 
15 
命令格式 : 
oam-propagate phb-name 
  {be 
|af11 
|af12 
|af21 
|af22 
|af31 
|af32 
|af41 
|af42 
|cs6 
|cs7 
|ef 
}
no oam-propagate phb-name 
命令参数解释 : 
参数|描述
---|---
be|尽力转发
af11|确保转发等级11
af12|确保转发等级12
af21|确保转发等级21
af22|确保转发等级22
af31|确保转发等级31
af32|确保转发等级32
af41|确保转发等级41
af42|确保转发等级42
cs6|服务等级6，代表网络内协议
cs7|服务等级7，代表网络间协议
ef|加速转发
缺省 : 
cs7 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#propagate ZXROSNG(config-propagate)#section 1ZXROSNG(config-propagate-section-1)#oam-propagate phb-name ef   
相关命令 : 
show propagate section 
## oam-propagate phb-name 

oam-propagate phb-name 
命令功能 : 
在LSP实体下指定客户层FDI报文的phb值。 
命令模式 : 
 繁殖LSP实体模式  
命令默认权限级别 : 
15 
命令格式 : 
oam-propagate phb-name 
  {be 
|af11 
|af12 
|af21 
|af22 
|af31 
|af32 
|af41 
|af42 
|cs6 
|cs7 
|ef 
}
no oam-propagate phb-name 
命令参数解释 : 
参数|描述
---|---
be|Best effort
af11|Assured forwarding 11
af12|Assured forwarding 12
af21|Assured forwarding 21
af22|Assured forwarding 22
af31|Assured forwarding 31
af32|Assured forwarding 32
af41|Assured forwarding 41
af42|Assured forwarding 42
cs6|Class selector 6
cs7|Class selector 7
ef|Expedited forwarding
缺省 : 
cs7 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#propagate ZXROSNG(config-propagate)#tunnel 1 lsp 1 ZXROSNG(config-propagate-tunnel-1-lsp-1)#oam-propagate phb-name ef   
相关命令 : 
show propagate lsp 
## oam-propagate pw 

oam-propagate pw 
命令功能 : 
在LSP实体下配置指定繁殖到某些PW。 
命令模式 : 
 繁殖LSP实体模式  
命令默认权限级别 : 
15 
命令格式 : 
oam-propagate pw 
  ＜pw-name 
＞
no oam-propagate pw 
  ＜pw-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜pw-name＞|PW名称
缺省 : 
无 
使用说明 : 
1.lsp层配置指定繁殖，当LSP层故障时，只繁殖到指定的PW;2.当配置指定繁殖时，本实体自动繁殖功能失效。
范例 : 
ZXROSNG(config)#propagate ZXROSNG(config-propagate)#tunnel 1 lsp 1 ZXROSNG(config-propagate-tunnel-1-lsp-1)#oam-propagate pw pw100 
相关命令 : 
propagteshow propagate relation tunnel
## oam-propagate tunnel 

oam-propagate tunnel 
命令功能 : 
在section实体下配置指定繁殖到某些隧道。 
命令模式 : 
 繁殖section实体模式  
命令默认权限级别 : 
15 
命令格式 : 
oam-propagate tunnel 
  ＜tunnel-number 
＞ lsp 
 ＜lsp-id 
＞
no oam-propagate tunnel 
  ＜tunnel-number 
＞ lsp 
 ＜lsp-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜tunnel-number＞|隧道号，范围：1~$#100794387#$
＜lsp-id＞|LSP号，范围：1-65535
缺省 : 
无 
使用说明 : 
1.Section层配置指定繁殖，当section 层故障时，只繁殖到指定的LSP；2.当配置指定繁殖时，本实体自动繁殖功能失效
范例 : 
ZXROSNG(config)#propagate ZXROSNG(config-propagate)#section 1ZXROSNG(config-propagate-section-1)#oam-propagate tunnel 1 lsp 1
相关命令 : 
propagateshow propagate relation section
## oam-propagate 

oam-propagate 
命令功能 : 
配置繁殖功能。 
命令模式 : 
 繁殖section实体模式  
命令默认权限级别 : 
15 
命令格式 : 
oam-propagate 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启繁殖功能
disable|关闭繁殖功能
缺省 : 
繁殖功能开启 
使用说明 : 
开启繁殖功能时，Section的状态会繁殖到上层，从而可以在上层不配置检测的情况下引起上层的切换；关闭繁殖功能时，Section的状态不向上繁殖。
范例 : 
ZXROSNG(config-propagate)#section 1ZXROSNG(config-propagate-section-1)#oam-propagate disable ZXROSNG(config-propagate-section-1)#oam-propagate enable
相关命令 : 
propagatesection
## oam-propagate 

oam-propagate 
命令功能 : 
配置繁殖功能。 
命令模式 : 
 繁殖LSP实体模式  
命令默认权限级别 : 
15 
命令格式 : 
oam-propagate 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启繁殖功能
disable|关闭繁殖功能
缺省 : 
繁殖功能开启 
使用说明 : 
开启繁殖功能时，隧道的状态会繁殖到上层，从而可以在上层不配置检测的情况下引起上层的切换；关闭繁殖功能时，隧道的状态不向上繁殖。
范例 : 
ZXROSNG(config-propagate)#tunnel 1 lsp 1ZXROSNG(config-propagate-tunnel-1-lsp-1)#oam-propagate disable ZXROSNG(config-propagate-tunnel-1-lsp-1)#oam-propagate enable 
相关命令 : 
propagatetunnel
## propagate 

propagate 
命令功能 : 
进入繁殖配置模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
propagate 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#propagateZXROSNG(config-propagate)#
相关命令 : 
无 
## section 

section 
命令功能 : 
进入繁殖Section实体配置模式。 
命令模式 : 
 繁殖模式  
命令默认权限级别 : 
15 
命令格式 : 
section 
  ＜section-id 
＞
no section 
  ＜section-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜section-id＞|Section实例号，范围：1~$#67305544#$
缺省 : 
无 
使用说明 : 
进入相应的Section，对其进行繁殖配置，no命令删除Section上的繁殖配置。 
范例 : 
ZXROSNG(config)#propagateZXROSNG(config-propagate)#section 1ZXROSNG(config-propagate-section-1)#ZXROSNG(config)#propagateZXROSNG(config-propagate)#no section 1 
相关命令 : 
propagate 
## show propagate lsp 

show propagate lsp 
命令功能 : 
显示lsp的繁殖配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show propagate lsp 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-propagate)#show propagate lspTunnel    LSP     Propagate PhbName----------------------------------------------2         1       Enable    cs71         1       Disable   cs7
相关命令 : 
propagatetunnelshow propagate section
## show propagate relation section 

show propagate relation section 
命令功能 : 
查看section实体上配置的指定繁殖实例 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show propagate relation section 
  ＜section-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜section-id＞|Section 实例号，范围：1~$#67305544#$
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show propagate relation section 1Tunnel     LSP      ----------------------1          1       40000      1       6          1   
相关命令 : 
propagatesection
## show propagate relation tunnel 

show propagate relation tunnel 
命令功能 : 
查看LSP实体上配置的指定繁殖实例 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show propagate relation tunnel 
  ＜tunnel-id 
＞ lsp 
 ＜lsp-id 
＞ 
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|隧道号,范围1~$#100794387#$
＜lsp-id＞|LSP号，范围：1-65535
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show propagate relation tunnel 1 lsp 1 PWName --------------pw100 pw5 pw4 pw3 pw2   
相关命令 : 
propagatetunnel
## show propagate section 

show propagate section 
命令功能 : 
显示Section的繁殖配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show propagate section 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-propagate)#show propagate sectionSection         Propagate PhbName----------------------------------------2               Enable    cs71               Disable   cs6
相关命令 : 
propagatesectionshow propagate lsp
## tunnel 

tunnel 
命令功能 : 
进入繁殖的LSP实体配置模式。 
命令模式 : 
 繁殖模式  
命令默认权限级别 : 
15 
命令格式 : 
tunnel 
  ＜tunnel-id 
＞ lsp 
 ＜lsp-id 
＞
no tunnel 
  ＜tunnel-id 
＞ lsp 
 ＜lsp-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜tunnel-id＞|隧道号，范围:1~$#100794387#$
＜lsp-id＞|LSP号，范围1-65535
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#propagate ZXROSNG(config-propagate)#tunnel 1 lsp 1ZXROSNG(config-propagate-tunnel-1-lsp-1)#ZXROSNG(config)#propagate ZXROSNG(config-propagate)#no tunnel 1 lsp 1
相关命令 : 
propagate 
