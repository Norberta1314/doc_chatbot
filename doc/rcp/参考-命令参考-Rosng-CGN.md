# CGN配置命令 
## address-policy 

address-policy 
命令功能 : 
模式跳转命令，进入地址策略配置模式。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
address-policy 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#address-policyZXROSNG(config-cgn-zte-domain-addr-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## address-user-share-ratio 

address-user-share-ratio 
命令功能 : 
一个公网地址可以被多少个用户使用。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
address-user-share-ratio 
  ＜address-user-ratio 
＞
no address-user-share-ratio 
命令参数解释 : 
参数|描述
---|---
＜address-user-ratio＞|私网地址地址数，默认值为1000。范围1~1000
缺省 : 
无 
使用说明 : 
配置PAT类型的地址池一个公网地址可以被多少个用户使用，no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#pat-pool zte poolid 0ZXROSNG(config-cgn-zte-patpool)# address-user-share-ratio 100ZXROSNG(config-cgn-zte-patpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## advanced-service 

advanced-service 
命令功能 : 
模式跳转命令，进入高级CGN功能配置模式 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
advanced-service 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#advanced-serviceZXROSNG(config-cgn-zte-adv-srv)# 
相关命令 : 
show running-config cgnshow cgn instance
## alarm 

alarm 
命令功能 : 
开启/关闭port range块告警功能 
命令模式 : 
 NAT告警模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm 
  {[port-range-block 
 {enable 
|disable 
}]}
命令参数解释 : 
参数|描述
---|---
enable|开启port range块告警功能
disable|关闭port range块告警功能
缺省 : 
alarm port-range-block disable 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test)#alarm ZXROSNG(config-cgn-test-alarm)#alarm port-range-block enable 
相关命令 : 
show running-config cgnshow cgn instance
## alarm 

alarm 
命令功能 : 
进入业务的告警配置。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#alarmZXROSNG(config-cgn-zte-alarm)#
相关命令 : 
show running-config cgnshow cgn instance
## alarm-threshold ip-resource 

alarm-threshold ip-resource 
命令功能 : 
达到单个SPU所有NAT地址池的ip资源总量的某一百分比则产生告警。 
命令模式 : 
 NAT告警模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold ip-resource 
  ＜ip-alarm-value 
＞
no alarm-threshold ip-resource 
命令参数解释 : 
参数|描述
---|---
＜ip-alarm-value＞|告警阈值，到达该百分比则产生告警，默认值为80。配置范围 <1-100>（%）
缺省 : 
80 
使用说明 : 
1. 单个SPU所有NAT地址池的ip使用率告警，No命令恢复默认值2. 仅针对NAT地址池告警，PAT地址池不生效告警码：303122 告警样例：An alarm 303122 ID 120 level 5 occurred at 00:17:16 09-20-2018 sent by ZXR10 SPU-0/2/0%CGN% IP utilization in nat pool reached the threshold.  Current=100%; Threshold=1%An alarm 303122 ID 120 level 5 cleared at 00:19:16 09-20-2018 sent by ZXR10 SPU-0/2/0%CGN% IP utilization in nat pool reached the threshold.  Current=0%; Threshold=1%
范例 : 
ZXROSNG(config-cgn-zte)#alarmZXROSNG(config-cgn-zte-alarm)#alarm-threshold ip-resource 10ZXROSNG(config-cgn-zte-alarm)#
相关命令 : 
show running-config cgnshow cgn instance
## alarm-threshold local-ip 

alarm-threshold local-ip 
命令功能 : 
配置达到单个SP-CPU最大私网IP管理节点数的某一百分比则产生告警 
命令模式 : 
 NAT告警模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold local-ip 
  {[low-level 
 ＜alarm-value 
＞],[middle-level 
 ＜alarm-value 
＞],[high-level 
 ＜alarm-value 
＞]}
no alarm-threshold local-ip 
命令参数解释 : 
参数|描述
---|---
＜alarm-value＞|低级告警阈值，到达该百分比则产生高级告警，没有默认值。配置范围 1~100
＜alarm-value＞|中级告警阈值，到达该百分比则产生高级告警，没有默认值。配置范围 1~100
＜alarm-value＞|高级告警阈值，到达该百分比则产生高级告警，没有默认值。配置范围 1~100
缺省 : 
不配置命令的情况下，默认达到80%告警，采用low-level 
使用说明 : 
低级配置阈值 < 中级配置阈值 < 高级配置阈值。告警码：303136告警样例：ZXROSNG(config-cgn-alarm)#An alarm 303136 ID 63 level 5 occurred at 00:01:07 09-19-2018 sent by ZXR10 SPU-0/2/0%CGN% The number of local ip exhausted.  Current=1%, Threshold=1%ZXROSNG(config-cgn-alarm)#An alarm 303136 ID 63 level 5 cleared at 00:02:57 09-19-2018 sent by ZXR10 SPU-0/2/0%CGN% The number of local ip exhausted.  Current=2%, Threshold=1%ZXROSNG(config-cgn-alarm)#An alarm 303136 ID 64 level 3 occurred at 00:02:57 09-19-2018 sent by ZXR10 SPU-0/2/0%CGN% The number of local ip exhausted.  Current=2%, Threshold=2%ZXROSNG(config-cgn-alarm)#ZXROSNG(config-cgn-alarm)#An alarm 303136 ID 64 level 3 cleared at 00:22:57 09-19-2018 sent by ZXR10 SPU-0/2/0%CGN% The number of local ip exhausted.  Current=0%, Threshold=2%
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#alarmZXROSNG(config-cgn-zte-alarm)#alarm-threshold local-ip low-level 10 middle-level 20 high-level 30ZXROSNG(config-cgn-zte-alarm)#ZXROSNG(config-cgn-zte-alarm)# show this!<cgn>    alarm-threshold local-ip low-level 10 middle-level 20 high-level 30!</cgn>
相关命令 : 
show running-config cgn 
## alarm-threshold pool-port-utilization 

alarm-threshold pool-port-utilization 
命令功能 : 
达到单个SPU单个pool的端口资源总量的某一百分比则产生告警。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold pool-port-utilization 
  ＜pool-port-utilization-alarm 
＞
no alarm-threshold pool-port-utilization 
命令参数解释 : 
参数|描述
---|---
＜pool-port-utilization-alarm＞|设置的告警值，默认值为80。配置范围 <1-100>（%）
缺省 : 
80 
使用说明 : 
1. 区分协议告警，No命令恢复默认值。2. 示例：ZXROSNG(config-cgn-patpool)#show this!<cgn>    alarm-threshold pool-port-utilization 1    section 1 10.1.1.1!</cgn>ZXROSNG(config-cgn-patpool)#发送823条UDP流量，占65535端口比例约为1.26，此时显示告警An alarm 303123 ID 172 level 5 occurred at 01:00:20 09-21-2018 sent by ZXR10 SPU-0/2/0%CGN% Ports utilization in pat pool reached the threshold.  Pool-name=1; Pool-id=1; Protocol=UDP; Current=1%; Threshold=1%删除条目告警消除：An alarm 303123 ID 172 level 5 cleared at 01:04:26 09-21-2018 sent by ZXR10 SPU-0/2/0%CGN% Ports utilization in pat pool reached the threshold.  Pool-name=1; Pool-id=1; Protocol=UDP; Current=0%; Threshold=1%3. 可通过下面命令查看使用率ZXROSNG(config-cgn-patpool)#show cgn pool-utilization pat-pool 1================================================================================Global          Number(Percent)    Number(Percent)    Number(Percent)    Dynamic                  of used            of used            of used           ShareAddress          TCP ports          UDP ports           ICMP ID           Ratio================================================================================10.1.1.1        0(0.00%)           823(1.26%)         0(0.00%)           -----------------------------------------------------------------------------------
范例 : 
ZXROSNG(config-cgn-zte)# cgn-pool dpat poolid 0 mode patZXROSNG(config-cgn-zte-patpool)#alarm-threshold pool-port-utilization 90ZXROSNG(config-cgn-zte-patpool)#告警码：303123告警样例：告警产生：An alarm 303123 level 5 occurred at 01:14:45 01-08-2012 sent by ZXR10 SPU-0/1/0%CGN% Ports utilization in pat pool reached the threshold. Pool-name=dpat; Pool-id=0; Protocol=TCP; Current=80%; Threshold=80%
告警消失：An alarm 303123 level 5 cleared at 01:14:45 01-08-2012 sent by ZXR10 SPU-0/1/0%CGN% Ports utilization in pat pool reached the threshold. Pool-name=dpat; Pool-id=0; Protocol=TCP; Current=80%; Threshold=80%
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-poolshow cgn pool-utilization pat-pool
## alarm-threshold port-range 

alarm-threshold port-range 
命令功能 : 
port-range端口使用情况告警通知，基于每一个port-range，基于协议 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold port-range 
  ＜port-range-port-alarm 
＞
no alarm-threshold port-range 
命令参数解释 : 
参数|描述
---|---
＜port-range-port-alarm＞|设置的通知值，默认值为80。配置范围 <1-100>
缺省 : 
alarm-threshold port-range 80 
使用说明 : 
1. 打开通知开关2. 配置通知阀值ZXROSNG(config-cgn-patpool)#show this!<cgn>    alarm-threshold port-range 1    port-range enable 256    section 1 10.1.1.1!</cgn>每个portrange块有256个端口（第一块有255个）发送5条私网IP相同的TCP流量，5条私网IP相同的UDP流量，产生如下通知：A notification 303102 ID 247 level 8 occurred at 17:30:47 09-21-2018 sent by ZXR10 SPU-0/2/0%CGN% Port range utilization.  IP=10.1.1.1; Protocol=UDP; Port-Used=5; Port-Range-Size=255A notification 303102 ID 248 level 8 occurred at 17:31:53 09-21-2018 sent by ZXR10 SPU-0/2/0%CGN% Port range utilization.  IP=10.1.1.1; Protocol=TCP; Port-Used=5; Port-Range-Size=2553. 该端口占用情况还可以通过下面命令查看：ZXROSNG(config-cgn-patpool)#show cgn subscriber-port-range all================================================================================SubscriberLocal IP     Global IP        StartPort   EndPort  TCP Used(%)  UDP Used(%) ICMP Used(%)================================================================================Loading data from SPU-0/2/0 ...================================================================================31.1.1.2     10.1.1.1                 1       255        5(1%)        5(1%)        0(0%)--------------------------------------------------------------------------------
范例 : 
ZXROSNG(config-cgn-test)#cgn-pool test poolid 0 mode patZXROSNG(config-cgn-test-patpool)#alarm-threshold port-range 50
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool 
## alarm-threshold port-range-block 

alarm-threshold port-range-block 
命令功能 : 
配置port range块告警通知 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold port-range-block 
  ＜port-range-block-alarm 
＞
no alarm-threshold port-range-block 
命令参数解释 : 
参数|描述
---|---
＜port-range-block-alarm＞|设置的通知值，默认值为80。配置范围 <1-100>
缺省 : 
alarm-threshold port-range-block 80 
使用说明 : 
1. 要产生此通知，除了打开通知开关，还需要打开alarm port-range-block enable。如下所示ZXROSNG(config-cgn-alarm)#show this!<cgn>    alarm port-range-block enable    warning disable    enable!</cgn>ZXROSNG(config-cgn-alarm)#2. 配置  cgn-pool 1 poolid 1 mode pat    alarm-threshold port-range-block 1    port-range enable 256    section 1 10.1.1.1共256块端口块，发送私网IP不同的120条流量，产生通知A notification 303118 ID 235 level 8 occurred at 17:07:05 09-21-2018 sent by ZXR10 SPU-0/2/0%CGN% Port range utilization of IP.  IP=10.1.1.1; Port-range-used=46%; Threshold=1%3. 次端口块占用率还可以通过下面命令查看ZXROSNG(config-cgn)#show cgn subscriber-port-range pool 1 summary================================================================================CPU                STA-Blocks(%)      DYN-Blocks(%) Total-Blocks================================================================================SPU-0/2/0               0(0.00%)        120(46.88%)          256--------------------------------------------------------------------------------Total                   0(0.00%)        120(46.88%)          256--------------------------------------------------------------------------------
范例 : 
ZXROSNG(config-cgn-test)#cgn-pool test poolid 0 mode patZXROSNG(config-cgn-test-patpool)#alarm-threshold port-range-block 50
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool alarm port-range-block enable
## alarm-threshold port-resource 

alarm-threshold port-resource 
命令功能 : 
达到单个SPU所有PAT地址池端口资源总量的某一百分比则产生告警。 
命令模式 : 
 NAT告警模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold port-resource 
  ＜alarm-value 
＞
no alarm-threshold port-resource 
命令参数解释 : 
参数|描述
---|---
＜alarm-value＞|告警阈值，到达该百分比则产生告警，默认值为80。配置范围 1~100（%）
缺省 : 
80 
使用说明 : 
1. 配置CPU总端口资源使用率告警值。No命令恢复默认值。2. PAT的所有端口资源包括TCP/UDP/ICMP。如只有一个公网IP地址，则端口资源总数为65535*3告警码：303101 告警样例：An alarm 303101 ID 116 level 5 occurred at 23:34:51 09-19-2018 sent by ZXR10 SPU-0/2/0%CGN% Ports utilization.  Current=10%; Threshold=1%An alarm 303101 ID 116 level 5 cleared at 23:35:51 09-19-2018 sent by ZXR10 SPU-0/2/0%CGN% Ports utilization.  Current=0%; Threshold=1%
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#alarmZXROSNG(config-cgn-zte-alarm)#alarm-threshold port-resource 10ZXROSNG(config-cgn-zte-alarm)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## alarm-threshold port-utilization 

alarm-threshold port-utilization 
命令功能 : 
pat地址池端口使用率告警通知。基于ip地址。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold port-utilization 
  ＜port-utilization-alarm 
＞
no alarm-threshold port-utilization 
命令参数解释 : 
参数|描述
---|---
＜port-utilization-alarm＞|设置的告警值，默认值为80。配置范围 <1-100>
缺省 : 
alarm-threshold port-utilization 80 
使用说明 : 
1. 打开通知开关，配置如下：（与是否portrange无关，仅基于IP和协议）!<cgn>    alarm-threshold port-utilization 1    section 1 10.1.1.1!</cgn>ZXROSNG(config-cgn-patpool)#2. 发送840条流，遍布120个私网IP，生成840条目，发送该通知A notification 303103 ID 249 level 8 occurred at 17:51:42 09-21-2018 sent by ZXR10 SPU-0/2/0%CGN% Ports utilization of IP.  IP=10.1.1.1; Protocol=UDP; Port-used=1%; Threshold=1%
范例 : 
ZXROSNG(config-cgn-test)#cgn-pool test poolid 0 mode patalarm-threshold port-utilization 50
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool 
## alarm-threshold sharing-ratio 

alarm-threshold sharing-ratio 
命令功能 : 
地址用户共享比率告警通知。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold sharing-ratio 
  ＜sharing-alarm 
＞
no alarm-threshold sharing-ratio 
命令参数解释 : 
参数|描述
---|---
＜sharing-alarm＞|地址共享比率通知，默认值为80。范围<1-100>
缺省 : 
alarm-threshold sharing-ratio 80 
使用说明 : 
1. 和PAT地址池下的 address-user-share-ratio相关。address-user-share-ratio配置一个IP可以被多少个用户使用（默认1000）。alarm-threshold sharing-ratio配置阈值，超过配置百分比后发通知。2. 例如ZXROSNG(config-cgn-patpool)#show this!<cgn>    address-user-share-ratio 10    alarm-threshold sharing-ratio 1    section 1 10.1.1.1!</cgn>用户共享地址数为10，发10条私网IP不同的流量，生成10个条目，出现如下通知A notification 303105 ID 171 level 8 occurred at 00:31:55 09-21-2018 sent by ZXR10 SPU-0/2/0%CGN% User sharing ratio of IP.  IP=10.1.1.1; Protocol=UDP; Current=100%; Share-ratio=1%
范例 : 
ZXROSNG(config-cgn)#cgn-pool test poolid 0 mode patZXROSNG(config-cgn-patpool)#alarm-threshold sharing-ratio 50告警码：303105告警样例：      A notification 303105 ID 171 level 8 occurred at 00:31:55 09-21-2018 sent by ZXR10 SPU-0/2/0%CGN% User sharing ratio of IP.  IP=10.1.1.1; Protocol=UDP; Current=100%; Share-ratio=1%
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool 
## alarm-threshold static-port-range-block 

alarm-threshold static-port-range-block 
命令功能 : 
配置静态port-range告警阈值。当portrange地址池的端口块使用率达到配置的阈值时，产生告警；低于配置值时，告警消除。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold static-port-range-block 
  ＜static-pr-block-alarm 
＞
no alarm-threshold static-port-range-block 
命令参数解释 : 
参数|描述
---|---
＜static-pr-block-alarm＞|告警阈值，到达该百分比则产生告警，默认值为80。配置范围 <1-100>
缺省 : 
alarm-threshold static-port-range-block 80 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test-patpool)#alarm-threshold static-port-range-block 50 告警范例：告警产生：An alarm 303121 level 5 occurred at 01:14:45 01-08-2012 sent by ZXR10 MPU-0/20/0 %CGN% Static port range utilization of PAT pool. Pool-name = pat;Port-range-used = 100%;Threshold = 100%告警消失：An alarm 303121 level 5 cleared at 01:20:45 01-08-2012 sent by ZXR10 MPU-0/20/0 %CGN% Static port range utilization of PAT pool. Pool-name = pat;Port-range-used = 100%;Threshold = 100%
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool 
## alarm-threshold translations 

alarm-threshold translations 
命令功能 : 
配置达到单个SP-CPU最大转换条目数的某一百分比则产生告警。 
命令模式 : 
 NAT告警模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold translations 
  {＜alarm-value 
＞ [{[middle-level 
 ＜alarm-value 
＞],[high-level 
 ＜alarm-value 
＞]}]|{[middle-level 
 ＜alarm-value 
＞],[high-level 
 ＜alarm-value 
＞]}}
no alarm-threshold translations 
命令参数解释 : 
参数|描述
---|---
＜alarm-value＞|低级告警阈值，到达该百分比则产生高级告警，没有默认值。配置范围 1~100
＜alarm-value＞|中级告警阈值，到达该百分比则产生高级告警，没有默认值。配置范围 1~100
＜alarm-value＞|高级告警阈值，到达该百分比则产生高级告警，没有默认值。配置范围 1~100
＜alarm-value＞|中级告警阈值，到达该百分比则产生高级告警，没有默认值。配置范围 1~100
＜alarm-value＞|高级告警阈值，到达该百分比则产生高级告警，没有默认值。配置范围 1~100
缺省 : 
命令不配置，默认80%告低级告警 
使用说明 : 
低级配置阈值 < 中级配置阈值 < 高级配置阈值。告警码：303106告警样例：An alarm 303106 ID 111 level 2 occurred at 22:07:00 09-19-2018 sent by ZXR10 SPU-0/2/0%CGN% NAT Translation entries reached threshold.  Current=6%; Threshold=3%An alarm 303106 ID 111 level 2 cleared at 22:12:00 09-19-2018 sent by ZXR10 SPU-0/2/0%CGN% NAT Translation entries reached threshold.  Current=0%; Threshold=3%
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#alarmZXROSNG(config-cgn-zte-alarm)#alarm-threshold translations 10 middle-level 20 high-level 30ZXROSNG(config-cgn-zte-alarm)# show this!<cgn>    alarm-threshold translations 10 middle-level 20 high-level 30!</cgn>  
相关命令 : 
show running-config cgn 
## alarm-threshold 

alarm-threshold 
命令功能 : 
配置NAT地址池IP使用率告警阀值。当使用IP超过地址池IP数*使用率时，产生告警
命令模式 : 
 NAT-NAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
alarm-threshold 
 ip-utilization 
 ＜ip-utilization-alarm 
＞
no alarm-threshold 
命令参数解释 : 
参数|描述
---|---
＜ip-utilization-alarm＞|设置的告警值，默认值为80。配置范围 <1-100>
缺省 : 
alarm-threshold ip-utilization 80 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test-natpool)#alarm-threshold ip-utilization 50 
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool 
## alg 

alg 
命令功能 : 
ALG功能配置。 
命令模式 : 
 NAT高级模式  
命令默认权限级别 : 
15 
命令格式 : 
alg 
  {[ftp 
 {enable 
|disable 
}],[icmp 
 {enable 
|disable 
}],[dns 
 {enable 
|disable 
}],[rtsp 
 {enable 
|disable 
}],[h323 
 {enable 
|disable 
}],[sip 
 {enable 
|disable 
}],[pptp 
 {enable 
|disable 
}],[dhcp 
 {enable 
|disable 
}]}
命令参数解释 : 
参数|描述
---|---
enable|开启DHCP ALG功能
disable|关闭DHCP ALG功能
enable|开启DHCP ALG功能
disable|关闭DHCP ALG功能
enable|开启DHCP ALG功能
disable|关闭DHCP ALG功能
enable|开启DHCP ALG功能
disable|关闭DHCP ALG功能
enable|开启DHCP ALG功能
disable|关闭DHCP ALG功能
enable|开启DHCP ALG功能
disable|关闭DHCP ALG功能
enable|开启DHCP ALG功能
disable|关闭DHCP ALG功能
enable|开启DHCP ALG功能
disable|关闭DHCP ALG功能
缺省 : 
alg ftp disable icmp disable dns disable rtsp disable h323 disable sip disable pptp disable dhcp disable 
使用说明 : 
只有当NAT高级模式下配置了enable，该命令才有效 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#advanced-serviceZXROSNG(config-cgn-zte-adv-srv)#alg ftp enableZXROSNG(config-cgn-zte-adv-srv)#
相关命令 : 
show running-config cgnshow cgn instance 
## allocate-diff-address 

allocate-diff-address 
命令功能 : 
对于用户的ICMP或DNS请求尽量分配不同的公网地址。 
命令模式 : 
 NAT地址策略模式  
命令默认权限级别 : 
15 
命令格式 : 
allocate-diff-address 
  ＜description 
＞ {tcp 
 ＜port 
＞|udp 
 ＜port 
＞|icmp 
}
no allocate-diff-address 
  {tcp 
 ＜port 
＞|udp 
 ＜port 
＞|icmp 
}
				
命令参数解释 : 
参数|描述
---|---
＜description＞|不同地址策略描述，可配置范围为1-31个字符
tcp|TCP协议类型
＜port＞|UDP端口号，范围<1-65535>
udp|UDP协议类型
＜port＞|UDP端口号，范围<1-65535>
icmp|ICMP协议类型
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#address-policyZXROSNG(config-cgn-zte-domain-addr-policy)#allocate-diff-address test udp 200ZXROSNG(config-cgn-zte-domain-addr-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## allowed-port-range 

allowed-port-range 
命令功能 : 
允许使用的端口范围配置。 
命令模式 : 
 NAT-UDP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
allowed-port-range 
  ＜start-port 
＞ ＜end-port 
＞
no allowed-port-range 
命令参数解释 : 
参数|描述
---|---
＜start-port＞|起始值范围<1-65535>
＜end-port＞|终止值取值范围<1-65535>
缺省 : 
start-port: 1end-port: 65535
使用说明 : 
no命令恢复默认值, 与forbidden-port-range成对使用。禁用的端口范围与允许使用的端口范围二者只能选其一进行配置。默认情况下是allowed-port-range。start-port要小于end-port。
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policy ZXROSNG(config-cgn-zte-domain-udp-policy)#allowed-port-range 100 1000ZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## allowed-port-range 

allowed-port-range 
命令功能 : 
TCP策略允许使用的端口范围配置。 
命令模式 : 
 NAT-TCP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
allowed-port-range 
  ＜start-port 
＞ ＜end-port 
＞
no allowed-port-range 
命令参数解释 : 
参数|描述
---|---
＜start-port＞|起始值范围1~65535
＜end-port＞|终止值取值范围1~65535
缺省 : 
start-port: 1end-port: 65535
使用说明 : 
no命令恢复默认值, forbidden-port-range：禁用的端口范围与允许使用的端口范围二者只能选其一进行配置。默认情况下是allowed-port-range。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#tcp-policy ZXROSNG(config-cgn-zte-domain-tcp-policy)# allowed-port-range 100 1000ZXROSNG(config-cgn-zte-domain-tcp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## bind-pool 

bind-pool 
命令功能 : 
CGN domain域下绑定地址池，用于当BRAS用户从此域上线时，从绑定的这些地址池中分配地址段。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
bind-pool 
  ＜pool-name 
＞
no bind-pool 
  ＜pool-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜pool-name＞|地址池名
缺省 : 
无 
使用说明 : 
命令对半静态portrange用户有效：1，当CGN domain下不绑定任何地址池，用户上线会从CGN实例下所有地址池中遍历分配地址段。2，当CGN domain下绑定地址池，则用户上线时，会根据携带的sib属性与地址池的sib属性比较，如果一致则从此地址池分配；如果不一致，则从CGN实例下的地址池中分配地址段；如果此地址池资源耗尽，那么具有相同sib属性的新用户再上线会上线失败，不会从CGN实例下的地址池中再分配地址段。3，不同的CGN domain下可以绑定相同的地址池，每个CGN domain下最多可以绑定200个。
范例 : 
ZXROSNG(config)#cgn 1 1ZXROSNG(config-cgn)#cgn-pool 1 poolid 1 mode patZXROSNG(config-cgn-patpool)#port-range enable 1024ZXROSNG(config-cgn-patpool)#section 1 100.1.1.1ZXROSNG(config-cgn-patpool)#exitZXROSNG(config-cgn)#domain  1 1 type bras ipv4-issuedZXROSNG(config-cgn-domain)#bind-pool 1ZXROSNG(config-cgn-domain)#
相关命令 : 
show running-config cgn。 
## bind-vrf 

bind-vrf 
命令功能 : 
NAT 地址池绑定VRF。 
命令模式 : 
 NAT-NAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
bind-vrf 
  ＜vrf-name 
＞
no bind-vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|VRF名称，可输入字符串长度根据VRF之限制
缺省 : 
无 
使用说明 : 
绑定已经配置的VRF的名称，若VRF不存在，则该命令不可配。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#nat-pool zte poolid 0ZXROSNG(config-cgn-zte-natpool)#bind-vrf vrftmpZXROSNG(config-cgn-zte-natpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## bind-vrf 

bind-vrf 
命令功能 : 
PAT地址池绑定VRF。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
bind-vrf 
  ＜vrf-name 
＞
no bind-vrf 
命令参数解释 : 
参数|描述
---|---
＜vrf-name＞|绑定VRF名称，可输入字符串长度根据VRF之限制
缺省 : 
无 
使用说明 : 
绑定已经配置的VRF的名称，若VRF不存在，则该命令不可配。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#pat-pool zte poolid 0ZXROSNG(config-cgn-zte-patpool)#bind-vrf vrftmpZXROSNG(config-cgn-zte-patpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## buffer-size 

buffer-size 
命令功能 : 
配置日志缓存大小。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
buffer-size 
  ＜buffer-size 
＞
命令参数解释 : 
参数|描述
---|---
＜buffer-size＞|配置日志缓存大小，范围10-64，单位MB
缺省 : 
16 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)#buffer-size 20ZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## car-policy-template 

car-policy-template 
命令功能 : 
进入限速策略配置模式。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
car-policy-template 
  ＜car-name 
＞
no car-policy-template 
  ＜car-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜car-name＞|限速策略模板名称，可配置范围为1-31个字节
缺省 : 
无 
使用说明 : 
当car策略被其他命令绑定时，不可以删除。若想删除，必须先解除绑定关系 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#car-policy-template testZXROSNG(config-cgn-zte-car-tmpl)#
相关命令 : 
show running-config cgnshow cgn instance show cgn car-policy
## cgn 

cgn 
命令功能 : 
进入cgn配置模式。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
cgn 
  [＜instance-name 
＞ ＜instance-id 
＞]
no cgn 
  [＜instance-name 
＞]
				
命令参数解释 : 
参数|描述
---|---
＜instance-name＞|CGN实例名称，范围1~31字节
＜instance-id＞|CGN实例id，范围1-63
缺省 : 
cgn直接回车进入cgn默认实例 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#
相关命令 : 
show running-config cgnshow cgn instance 
## cgn-alarm-threshold all-translations 

cgn-alarm-threshold all-translations 
命令功能 : 
配置license告警，整机会话数超过license限制则产生告警。 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
cgn-alarm-threshold all-translations 
  ＜all-alarm-value 
＞
no cgn-alarm-threshold all-translations 
命令参数解释 : 
参数|描述
---|---
＜all-alarm-value＞|告警阈值，到达该百分比则产生告警，默认值为100。配置范围 <1-100>
缺省 : 
cgn-alarm-threshold all-translations 100 
使用说明 : 
告警码：303119，303120告警样例：告警产生：An alarm 303119 level 5 occurred at 01:14:45 01-08-2012 sent by ZXR10 MPU-0/20/0%CGN% License NAT44 session count threshold detection. Current = 100%, Threshold = 100%告警消失：An alarm 303119 level 5 occurred at 01:14:45 01-08-2012 sent by ZXR10 MPU-0/20/0%CGN% License NAT44 session count threshold detection.Current = 100%, Threshold = 100%告警产生：An alarm 303120 level 5 occurred at 01:14:45 01-08-2012 sent by ZXR10 MPU-0/20/0%CGN% License DSLITE/NAT64 session count threshold detection. Current = 100%, Threshold = 100%
告警消失：An alarm 303120 level 5 occurred at 01:14:45 01-08-2012 sent by ZXR10 MPU-0/20/0%CGN% License DSLITE/NAT64 session count threshold detection. Current = 100%, Threshold = 100%
范例 : 
ZXROSNG(config)#cgn-alarm-threshold all-translations 50 
相关命令 : 
show running-config cgn 
## cgn-ipflow-templates-nat44 

cgn-ipflow-templates-nat44 
命令功能 : 
配置nat44模板 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
cgn-ipflow-templates-nat44 
  {[create-translation 
 {enable 
|disable 
}],[create-session 
 {enable 
|disable 
}],[create-portrange 
 {enable 
|disable 
}],[delete-translation 
 {enable 
|disable 
}],[delete-session 
 {enable 
|disable 
}],[delete-portrange 
 {enable 
|disable 
}]}
命令参数解释 : 
参数|描述
---|---
enable|创建translation ipflow 模板打开
disable|创建translation ipflow 模板关闭
enable|创建session ipflow 模板打开
disable|创建session ipflow 模板关闭
enable|创建portrange ipflow 模板打开
disable|创建portrange ipflow 模板关闭
enable|删除translation ipflow 模板打开
disable|删除translation ipflow 模板关闭
enable|删除session ipflow 模板打开
disable|删除session ipflow 模板关闭
enable|删除portrange ipflow 模板打开
disable|删除portrange ipflow 模板关闭
缺省 : 
缺省状态所有开关为打开状态。
使用说明 : 
使用场景NAT44的环境下，配置发送日志格式为ipflow,需要对发送的ipflow日志模板控制，可以使用此命令。注意事项该命令仅仅控制模板报文是否发送，数据报文的发送不受该命令控制。
范例 : 
配置NAT44创建translation ipflow 模板关闭。ZXROSNG(config)#
ZXROSNG(config)#cgn-ipflow-templates-nat44 create-translation disableZXROSNG(config)#
相关命令 : 
show running-config cgn 
## cgn-ipflow-templates-nat64 

cgn-ipflow-templates-nat64 
命令功能 : 
配置nat64模板 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
cgn-ipflow-templates-nat64 
  {[create-translation 
 {enable 
|disable 
}],[create-session 
 {enable 
|disable 
}],[create-portrange 
 {enable 
|disable 
}],[delete-translation 
 {enable 
|disable 
}],[delete-session 
 {enable 
|disable 
}],[delete-portrange 
 {enable 
|disable 
}]}
命令参数解释 : 
参数|描述
---|---
enable|创建translation ipflow 模板打开
disable|创建translation ipflow 模板关闭
enable|创建session ipflow 模板打开
disable|创建session ipflow 模板关闭
enable|创建portrange ipflow 模板打开
disable|创建portrange ipflow 模板关闭
enable|删除translation ipflow 模板打开
disable|删除translation ipflow 模板关闭
enable|删除session ipflow 模板打开
disable|删除session ipflow 模板关闭
enable|删除portrange ipflow 模板打开
disable|删除portrange ipflow 模板关闭
缺省 : 
缺省状态所有开关为打开状态。 
使用说明 : 
使用场景NAT64的环境下，配置发送日志格式为ipflow,需要对发送的ipflow日志模板控制，可以使用此命令。注意事项该命令仅仅控制模板报文是否发送，数据报文的发送不受该命令控制。
范例 : 
配置NAT64创建translation ipflow 模板关闭。ZXROSNG(config)#
ZXROSNG(config)#cgn-ipflow-templates-nat64 create-translation disableZXROSNG(config)#
相关命令 : 
show running-config cgn 
## cgn-pool 

cgn-pool 
命令功能 : 
创建NAT地址池。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
cgn-pool 
  ＜pool-name 
＞ poolid 
 ＜pool-id 
＞ mode 
 {nat 
|pat 
}
no cgn-pool 
  ＜pool-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜pool-name＞|地址池名字，范围1~31字节
＜pool-id＞|地址池编号，范围为0~1999
nat|NAT地址池
pat|PAT地址池
缺省 : 
无 
使用说明 : 
配置NAT地址池，可供业务分配公网IP地址，具体由cgn-domain下的ACL规则使用。已被使用的地址池不可以删除。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#cgn-pool zte poolid 0 mode patZXROSNG(config-cgn-zte-patpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## cgn-spu-auto-add 

cgn-spu-auto-add 
命令功能 : 
自动添加CPU 
命令模式 : 
 全局配置模式  
命令默认权限级别 : 
15 
命令格式 : 
cgn-spu-auto-add 
  {on 
|off 
}
命令参数解释 : 
参数|描述
---|---
on|打开自动添加CPU开关
off|关闭自动添加CPU开关
缺省 : 
off 
使用说明 : 
1. 只有默认实例存在时才可以打开开关2. 打开开关后，所有SPU自动加入默认实例
范例 : 
ZXROSNG(config)#
ZXROSNG(config)#cgn-spu-auto-add onZXROSNG(config)#
相关命令 : 
show running-config cgn 
description : 

description 
命令功能 : 
域描述信息，可对domain进行1-63字符的描述 
命令模式 : 
 NAT-DOMAIN模式  
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
＜description＞|描述内容1~63字节
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#description test
相关命令 : 
show running-config cgnshow cgn instanceshow cgn domain
description : 

description 
命令功能 : 
NAT地址池描述。 
命令模式 : 
 NAT-NAT地址池模式  
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
＜description＞|描述内容1~63字节
缺省 : 
无 
使用说明 : 
配置NAT地址池描述信息。no命令删除描述。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#nat-pool zte poolid 0ZXROSNG(config-cgn-zte-natpool)# description testZXROSNG(config-cgn-zte-natpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
description : 

description 
命令功能 : 
PAT地址池描述。 
命令模式 : 
 NAT-PAT地址池模式  
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
＜description＞|描述内容1~63字节
缺省 : 
无 
使用说明 : 
配置PAT地址池描述信息。no命令删除描述。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#pat-pool zte poolid 0ZXROSNG(config-cgn-zte-patpool)# description testZXROSNG(config-cgn-zte-patpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## destination 

destination 
命令功能 : 
配置日志上传方式。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
destination 
  {local 
|syslog 
|ipflow 
 ＜flow exporter name 
＞}
命令参数解释 : 
参数|描述
---|---
local|日志存放在机架硬盘中
syslog|日志信息上传syslog服务器
ipflow|日志信息上传ipflow服务器
＜flow exporter name＞|输出器名称
缺省 : 
local 
使用说明 : 
当配置日志格式为binary类型时，destination不能配置为syslog。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)#destination syslog ZXROSNG(config-cgn-zte-log)# 
相关命令 : 
show running-config cgnshow cgn instance
## disable 

disable 
命令功能 : 
关闭高级CGN功能。 
命令模式 : 
 NAT高级模式  
命令默认权限级别 : 
15 
命令格式 : 
disable 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#advanced-serviceZXROSNG(config-cgn-zte-adv-srv)#disable
相关命令 : 
show running-config cgnshow cgn instance 
## disable 

disable 
命令功能 : 
关闭日志功能。关闭后整个日志功能不可用，日志模式中的命令均不生效 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
disable 
 
命令参数解释 : 
					无
				 
缺省 : 
disable 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)#disableZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## disable 

disable 
命令功能 : 
关闭CGN业务的通知功能。 
命令模式 : 
 NAT告警模式  
命令默认权限级别 : 
15 
命令格式 : 
disable 
 
命令参数解释 : 
					无
				 
缺省 : 
disable 
使用说明 : 
和enable成对使用，控制CGN通知notification业务，而不是告警warning业务 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#alarmZXROSNG(config-cgn-zte-alarm)#disableZXROSNG(config-cgn-zte-alarm)#
相关命令 : 
show running-config cgnshow cgn instance 
## disable 

disable 
命令功能 : 
关闭PCP功能。 
命令模式 : 
 NAT-PCP模式  
命令默认权限级别 : 
15 
命令格式 : 
disable 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-zte)# pcp-serviceZXROSNG(config-cgn-zte-pcp-service)# disable
相关命令 : 
show running-config cgnshow cgn instance 
## dns-exclude-session-limit 

dns-exclude-session-limit 
命令功能 : 
配置DNS连接数目限制。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
dns-exclude-session-limit 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开DNS连接数目限制功能
disable|关闭DNS连接数目限制功能
缺省 : 
disable 
使用说明 : 
与配额命令共同使用。当该命令配置disable时，关闭DNS连接数目限制功能，dns条目不受配额限制，当该命令配置enable时，打开dns连接数目限制功能，dns条目受配额限制。如果没有配置配额命令，此条命令无实际意义，条目按照性能参数来
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#dns-exclude-session-limit enableZXROSNG(config-cgn-zte-domain)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## domain 

domain 
命令功能 : 
配置CGN domain。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
domain 
  ＜domain-name 
＞ ＜domain-id 
＞ type 
 {standalone 
|sr 
|bras 
|xgw 
} {ipv6-issued 
|ipv4-issued 
}
no domain 
  ＜domain-name 
＞
				
命令参数解释 : 
参数|描述
---|---
＜domain-name＞|域名称，可配置范围1~31个字符
＜domain-id＞|域ID，可配置范围1~4000
standalone|域类型为standalone
sr|域类型为SR
bras|域类型为BRAS
xgw|域类型为XGW
ipv6-issued|域技术形态为ipv6-issued
ipv4-issued|域技术形态为ipv4-issued
缺省 : 
无 
使用说明 : 
创建CGN域。domain type配置成sr，则技术形态只允许配置ipv4-issued，配置ipv6-issued提示错误码返回。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn domain
## dynamic 

dynamic 
命令功能 : 
配置动态映射规则。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
dynamic 
 source 
 rule-id 
 ＜rule-id 
＞ {ipv4-list 
|ipv6-list 
} ＜acl-name 
＞ {deny 
 [＜intf-name 
＞]|drop 
 [＜intf-name 
＞]|permit 
 [pool 
 ＜pool-name 
＞ [flow 
 ＜flow-ip 
＞] [＜intf-name 
＞]]}
no dynamic 
 source 
 rule-id 
 ＜rule-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜rule-id＞|NAT规则编号，范围<1-2000>
ipv4-list|技术形态为ipv4-issued
ipv6-list|技术形态为ipv6-issued
＜acl-name＞|ACL规则名，范围<1-31>字符
deny|对匹配到ACL规则的报文做转发处理，不做NAT转换
＜intf-name＞|接口名称
drop|对匹配到ACL规则的报文做丢弃处理
＜intf-name＞|接口名称
permit|对匹配到ACL规则的报文需要做NAT转换
＜pool-name＞|做NAT的转换的公网地址池名，范围<1-31>字符
＜flow-ip＞|Flow IP地址，配置后匹配该规则的流量都引到该IP资源所在的单板
＜intf-name＞|接口名称
缺省 : 
无 
使用说明 : 
1）acl list可以空绑，空绑后规则不生效2）action动作采用本规则中配置的permit、deny、drop动作，引用的acl list里的动作不使用。3）绑定的pool必须是已经存在的pool，不能空绑
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#dynamic source rule-id 1 ipv4-list zte permit pool patZXROSNG(config-cgn-zte-domain)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## enable 

enable 
命令功能 : 
打开高级CGN功能。 
命令模式 : 
 NAT高级模式  
命令默认权限级别 : 
15 
命令格式 : 
enable 
 
命令参数解释 : 
					无
				 
缺省 : 
disable 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#advanced-serviceZXROSNG(config-cgn-zte-adv-srv)#enable 
相关命令 : 
show running-config cgnshow cgn instance
## enable 

enable 
命令功能 : 
开启日志功能。当开启后，日志模式下的命令才有效。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
enable 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)#enableZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## enable 

enable 
命令功能 : 
开启CGN业务的通知功能。 
命令模式 : 
 NAT告警模式  
命令默认权限级别 : 
15 
命令格式 : 
enable 
 
命令参数解释 : 
					无
				 
缺省 : 
缺省disable 
使用说明 : 
打开的是通知notification业务，不是告警warning 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#alarmZXROSNG(config-cgn-zte-alarm)#enableZXROSNG(config-cgn-zte-alarm)#
相关命令 : 
show running-config cgnshow cgn instance
## enable 

enable 
命令功能 : 
开启PCP功能。 
命令模式 : 
 NAT-PCP模式  
命令默认权限级别 : 
15 
命令格式 : 
enable 
 
命令参数解释 : 
					无
				 
缺省 : 
disable 
使用说明 : 
无 
范例 : 
XR10(config-cgn-zte)# pcp-serviceZXROSNG(config-cgn-zte-pcp-service)# enable
相关命令 : 
show running-config cgnshow cgn instance 
## filtering-mode 

filtering-mode 
命令功能 : 
TCP策略的条目过滤模式配置。 
命令模式 : 
 NAT-TCP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
filtering-mode 
  {endpoint-independent 
|address-dependent 
|address-and-port-dependent 
}
no filtering-mode 
命令参数解释 : 
参数|描述
---|---
endpoint-independent|端点无关过滤模式
address-dependent|地址相关过滤模式
address-and-port-dependent|地址和端口相关过滤模式
缺省 : 
endpoint-independent 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#tcp-policy ZXROSNG(config-cgn-zte-domain-tcp-policy)#filtering-mode address-and-port-dependentZXROSNG(config-cgn-zte-domain-tcp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## filtering-mode 

filtering-mode 
命令功能 : 
UDP策略的条目过滤模式配置。 
命令模式 : 
 NAT-UDP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
filtering-mode 
  {endpoint-independent 
|address-dependent 
|address-and-port-dependent 
}
no filtering-mode 
命令参数解释 : 
参数|描述
---|---
endpoint-independent|端点无关过滤模式
address-dependent|地址相关过滤模式
address-and-port-dependent|地址和端口相关过滤模式
缺省 : 
endpoint-independent 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policy ZXROSNG(config-cgn-zte-domain-udp-policy)#filtering-mode address-and-port-dependentZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## filtering-mode 

filtering-mode 
命令功能 : 
ICMP策略的过滤模式配置。 
命令模式 : 
 NAT-ICMP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
filtering-mode 
  {endpoint-independent 
|address-dependent 
}
no filtering-mode 
命令参数解释 : 
参数|描述
---|---
endpoint-independent|端点无关过滤模式
address-dependent|地址相关过滤模式
缺省 : 
endpoint-independent 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#icmp-policyZXROSNG(config-cgn-zte-domain-icmp-policy)#filtering-mode address-dependentZXROSNG(config-cgn-zte-domain-icmp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## filtering-mode 

filtering-mode 
命令功能 : 
NAT策略的过滤模式配置。 
命令模式 : 
 NAT-NAT策略模式  
命令默认权限级别 : 
15 
命令格式 : 
filtering-mode 
  {endpoint-independent 
|address-dependent 
}
no filtering-mode 
命令参数解释 : 
参数|描述
---|---
endpoint-independent|端点无关过滤模式
address-dependent|地址相关过滤模式
缺省 : 
endpoint-independent 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#nat-policy  ZXROSNG(config-cgn-zte-domain-nat-policy)#filtering-mode address-dependentZXROSNG(config-cgn-zte-domain-nat-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## forbidden-port-range 

forbidden-port-range 
命令功能 : 
UDP禁用的端口范围配置。 
命令模式 : 
 NAT-UDP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
forbidden-port-range 
  ＜start-port 
＞ ＜end-port 
＞
no forbidden-port-range 
命令参数解释 : 
参数|描述
---|---
＜start-port＞|起始值范围<1-65535>
＜end-port＞|终止值取值范围<1-65535>
缺省 : 
无 
使用说明 : 
no命令删除禁用的端口范围，与allowed-port-range成对使用。禁用的端口范围与允许使用的端口范围二者只能选其一进行配置，默认状态为allowed-port-range。start-port要小于end-port。
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policy ZXROSNG(config-cgn-zte-domain-udp-policy)# forbidden-port-range 100 1000ZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## forbidden-port-range 

forbidden-port-range 
命令功能 : 
TCP禁用的端口范围配置。 
命令模式 : 
 NAT-TCP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
forbidden-port-range 
  ＜start-port 
＞ ＜end-port 
＞
no forbidden-port-range 
命令参数解释 : 
参数|描述
---|---
＜start-port＞|起始值范围1~65535
＜end-port＞|终止值取值范围1~65535
缺省 : 
无 
使用说明 : 
no命令删除禁用的端口范围，allowed-port-range：禁用的端口范围与允许使用的端口范围二者只能选其一进行配置，默认状态为allowed-port-range。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#tcp-policy ZXROSNG(config-cgn-zte-domain-tcp-policy)# forbidden-port-range 100 1000ZXROSNG(config-cgn-zte-domain-tcp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## format 

format 
命令功能 : 
配置日志发送方式。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
format 
  {binary 
|text 
}
命令参数解释 : 
参数|描述
---|---
binary|日志以二进制方式发送
text|日志以文本方式发送
缺省 : 
text 
使用说明 : 
当配置日志格式为binary类型时，destination不能配置为syslog。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)#format binaryZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## hot-standby-policy 

hot-standby-policy 
命令功能 : 
NAT地址池支持hot-standby-policy。配置备份条目的老化时间，条目老化时间大于配置值的，进行备份，不配置则所有都不备份， 
命令模式 : 
 NAT-NAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
hot-standby-policy 
  {all 
 ＜all-long-lived 
＞|protocol 
 {[ip 
 ＜ip-long-lived 
＞],[alg 
 ＜alg-long-lived 
＞]}}
no hot-standby-policy 
  {all 
|protocol 
 {ip 
|alg 
}}
				
命令参数解释 : 
参数|描述
---|---
＜all-long-lived＞|设置所有协议的NAT POOL热备策略参数
＜ip-long-lived＞|设置IP协议的NAT POOL热备策略参数
＜alg-long-lived＞|设置ALG协议的NAT POOL热备策略参数
No参数|描述
---|---
all|设置所有协议
ip|设置IP
alg|设置ALG
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test)#cgn-pool test poolid 0 mode natZXROSNG(config-cgn-test-natpool)# hot-standby-policy allZXROSNG(config-cgn-test-natpool)# 
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## hot-standby-policy 

hot-standby-policy 
命令功能 : 
PAT地址池支持hot-standby-policy。配置备份条目的老化时间，条目老化时间大于配置值的，进行备份，不配置则所有都不备份， 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
hot-standby-policy 
  {all 
 ＜all-long-lived 
＞|protocol 
 {[tcp 
 ＜tcp-long-lived 
＞],[udp 
 ＜udp-long-lived 
＞],[icmp 
 ＜icmp-long-lived 
＞],[pcp 
 ＜pcp-long-lived 
＞],[alg 
 ＜alg-long-lived 
＞]}}
no hot-standby-policy 
  {all 
|protocol 
 {tcp 
|udp 
|icmp 
|pcp 
|alg 
}}
				
命令参数解释 : 
参数|描述
---|---
＜all-long-lived＞|设置所有协议的PAT POOL热备策略参数
＜tcp-long-lived＞|设置TCP协议的PAT POOL热备策略参数
＜udp-long-lived＞|设置UDP协议的PAT POOL热备策略参数
＜icmp-long-lived＞|设置ICMP协议的PAT POOL热备策略参数
＜pcp-long-lived＞|设置PCP协议的PAT POOL热备策略参数
＜alg-long-lived＞|设置ALG协议的PAT POOL热备策略参数
No参数|描述
---|---
all|设置所有协议
tcp|设置TCP协议
udp|设置UDP协议
icmp|设置ICMP协议
pcp|设置PCP
alg|设置ALG
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test)#cgn-pool test poolid 0 mode patZXROSNG(config-cgn-test-patpool)# hot-standby-policy allZXROSNG(config-cgn-test-patpool)# 
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## hot-standby-route-metric 

hot-standby-route-metric 
命令功能 : 
配置双机热备备机地址池路由量度。 
命令模式 : 
 NAT-NAT地址池模式,NAT-PAT地址池模式  
命令默认权限级别 : 
NAT-PAT地址池模式:15,NAT-NAT地址池模式:15 
命令格式 : 
hot-standby-route-metric 
  ＜route-metric 
＞
no hot-standby-route-metric 
命令参数解释 : 
参数|描述
---|---
＜route-metric＞|双机热备备状态或初始化状态的地址池路由量度，范围为0- 4261412864
缺省 : 
值为50。 
使用说明 : 
配置双机热备备状态或初始化状态的pool路由metric。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn)#cgn pat poolid 1 mode pat ZXROSNG(config-cgn-patpool)# hot-standby-route-metric 100
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## hot-standby-route-priority 

hot-standby-route-priority 
命令功能 : 
配置双机热备备机地址池路由优先级。 
命令模式 : 
 NAT-NAT地址池模式,NAT-PAT地址池模式  
命令默认权限级别 : 
NAT-PAT地址池模式:15,NAT-NAT地址池模式:15 
命令格式 : 
hot-standby-route-priority 
  ＜route-priority 
＞
no hot-standby-route-priority 
命令参数解释 : 
参数|描述
---|---
＜route-priority＞|双机热备备状态或初始化状态的地址池路由优先级，范围为0-254
缺省 : 
值为50。 
使用说明 : 
配置双机热备备状态或初始化状态的地址池路由优先级。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn)#cgn pat poolid 1 mode pat ZXROSNG(config-cgn-patpool)# hot-standby-route-priority 100
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## icmp-policy 

icmp-policy 
命令功能 : 
模式跳转命令，进入ICMP策略配置模式。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
icmp-policy 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#icmp-policyZXROSNG(config-cgn-zte-domain-icmp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## inbound 

inbound 
命令功能 : 
配置入向限速策略。 
命令模式 : 
 NAT-CAR限速模式  
命令默认权限级别 : 
15 
命令格式 : 
inbound 
 cir 
 ＜cir 
＞ cbs 
 ＜cbs 
＞ pir 
 ＜pir 
＞ pbs 
 ＜pbs 
＞
no inbound 
命令参数解释 : 
参数|描述
---|---
＜cir＞|配置承诺访问速率，取值范围： 66-16777215，单位kbps
＜cbs＞|配置承诺突发尺寸，取值范围：15-2000000，单位KB
＜pir＞|配置峰值信息速率，取值范围：66-16777215，单位kbps
＜pbs＞|配置峰值突发尺寸，取值范围：15-2000000，单位KB
缺省 : 
无。不配置则不进行限速 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgnZXROSNG(config-cgn-?)#car-policy-template testZXROSNG(config-cgn-?-car-tmpl)#inbound cir 66 cbs 660 pir 66 pbs 660ZXROSNG(config-cgn-?-car-tmpl)#
相关命令 : 
show running-config cgnshow cgn instance summaryshow cgn instance verbose show cgn car-policy
interface : 

interface (NAT-PAT地址池模式) 
命令功能 : 
地址池绑定SG接口，配置后支持SG接口。绑定SG接口的地址池资源会分配到SG口绑定的单板上。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
interface 
  ＜intf-name 
＞
no interface 
命令参数解释 : 
参数|描述
---|---
＜intf-name＞|SG接口名，1-32字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgnZXROSNG(config-cgn-?)#cgn-pool zte poolid 1999 mode natZXROSNG(config-cgn-?-patpool)#interface smartgroup1ZXROSNG(config-cgn-?-patpool)#
相关命令 : 
show running-config cgnshow cgn-pool 
interface : 

interface (NAT-NAT地址池模式) 
命令功能 : 
地址池绑定SG接口，配置后支持SG接口。绑定SG接口的地址池资源会分配到SG口绑定的单板上。 
命令模式 : 
 NAT-NAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
interface 
  ＜intf-name 
＞
no interface 
命令参数解释 : 
参数|描述
---|---
＜intf-name＞|SG接口名，1-32字符
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgnZXROSNG(config-cgn-?)#cgn-pool zte poolid 1999 mode natZXROSNG(config-cgn-?-natpool)#interface smartgroup1ZXROSNG(config-cgn-?-natpool)#
相关命令 : 
show running-config cgnshow cgn-pool
## ipv4-access-list 

ipv4-access-list 
命令功能 : 
配置PCP的IPV4 ACL过滤。 
命令模式 : 
 NAT-PCP模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv4-access-list 
  ＜acl-name 
＞
no ipv4-access-list 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|使用的acl-name，范围1-31字符
缺省 : 
无。如不配置acl list，则不允许PCP报文通过
使用说明 : 
引用acl 模块的acl list，如空绑或者引用的list为空，不允许PCP报文通过
范例 : 
ZXROSNG(config-cgn)#pcp-serviceZXROSNG(config-cgn-pcp-service)# ipv4-access-list ?WORD Name of an IPv4 access list (1-31 characters)
相关命令 : 
show running-config cgn
## ipv6-access-list 

ipv6-access-list 
命令功能 : 
配置PCP的IPV6 ACL过滤。
命令模式 : 
 NAT-PCP模式  
命令默认权限级别 : 
15 
命令格式 : 
ipv6-access-list 
  ＜acl-name 
＞
no ipv6-access-list 
命令参数解释 : 
参数|描述
---|---
＜acl-name＞|使用的acl-name，范围1-31字符
缺省 : 
无。如不配置acl list，则不允许PCP报文通过
使用说明 : 
引用acl 模块的acl list，如空绑或者引用的list为空，不允许PCP报文通过
范例 : 
ZXROSNG(config-cgn)#pcp-serviceZXROSNG(config-cgn-pcp-service)# ipv6-access-list ?WORD Name of an IPv6 access list (1-31 characters)
相关命令 : 
show running-config cgn
## location 

location 
命令功能 : 
配置地址池静态分流node。 
命令模式 : 
 NAT-NAT地址池模式,NAT-PAT地址池模式  
命令默认权限级别 : 
NAT-PAT地址池模式:15,NAT-NAT地址池模式:15 
命令格式 : 
location 
 node 
 ＜nodeid 
＞
no location 
 node 
命令参数解释 : 
参数|描述
---|---
＜nodeid＞|CGN实例下node ID，有效范围1-64
No参数|描述
---|---
node|配置node
缺省 : 
动态分流，node ID值为0。 
使用说明 : 
配置地址池静态分流所属的node。该命令支持空绑一个不存在的nodeID，但不支持直接修改，需要修改的情况下，要先删除原有配置，再配置新值。与地址池下interface smartgroup命令互斥，不能同时配置。配置有section的情况下，不能配置该命令。
范例 : 
配置静态分流所属node为node1ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn)#cgn pat poolid 1 mode pat ZXROSNG(config-cgn-patpool)#location node 1   
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-poolinterface smartgroupsection
## location 

location 
命令功能 : 
模式跳转命令，进入CGN实例位置模式 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
location 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test)#location ZXROSNG(config-cgn-test-location)#
相关命令 : 
show running-config cgnshow cgn instance
## log 

log 
命令功能 : 
进入日志配置模式。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
log 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
进入日志配置模式后，所有命令均为16级。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## logging-content 

logging-content 
命令功能 : 
日志中显示条目创建删除时间、年份、带时区的创建删除时间、时长的开关。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
logging-content 
  {[{start-end-time 
|start-end-time-with-zone 
}],[duration 
],[year 
]}
no logging-content 
  {[{start-end-time 
|start-end-time-with-zone 
}],[duration 
],[year 
]}
				
命令参数解释 : 
参数|描述
---|---
start-end-time|日志显示条目创建删除时间
start-end-time-with-zone|日志显示带时区的条目创建删除时间
duration|日志显示条目时长
year|日志显示条目创建删除年份
缺省 : 
不显示条目创建删除时间、年份、带时区的创建删除时间、时长 
使用说明 : 
只在配置了log-style style1（电信格式）时命令生效；log-style style2（联通格式）时，命令可配置，但不生效 
范例 : 
ZXROSNG(config-cgn-log)#logging-content ?  start-end-time  Record start and end time of the log in style1  year            Record year of the log in style1start-end-time-with-zone  Record start end time with zone of log in style1duration                  Record duration of the log in style1
相关命令 : 
show cgn instance summaryshow running-config cgn
## logging-duration 

logging-duration 
命令功能 : 
会话日志过滤时间 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
logging-duration 
  ＜logging-duration 
＞
no logging-duration 
命令参数解释 : 
参数|描述
---|---
＜logging-duration＞|配置的过滤时长，单位S
缺省 : 
0s，表示不过滤 
使用说明 : 
配置该命令后，当会话持续时间大于配置时长，发送日志，否则不发送 
范例 : 
ZXCTN(config)#cgnZXCTN(config-cgn)#logZXCTN(config-cgn-log)#logging-duration ?  <0-10>  Seconds (defalut:0)ZXCTN(config-cgn-log)#logging-duration 1ZXCTN(config-cgn-log)#show running-config cgn!<cgn>cgn  log    logging-duration 1  $
相关命令 : 
show running-config cgn
## logging-portrange-detail 

logging-portrange-detail 
命令功能 : 
开启/关闭portrange 明细日志开关。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
logging-portrange-detail 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启portrange 明细日志开关
disable|关闭portrange 明细日志开关
缺省 : 
disable 
使用说明 : 
1. 关闭后，只记录portrange块信息，不记录portrange条目时间、地址、端口等等具体条目信息。2. 打开后，除了记录portrange块信息外，还要记录portrange条目的时间、地址、端口、映射模式、过滤模式等具体条目信息。
范例 : 
ZXROSNG(config)#cgn test 1ZXROSNG(config-cgn-test)#logZXROSNG(config-cgn-test-log)#logging-portrange-detail enableZXROSNG(config-cgn-test-log)#
相关命令 : 
show running-config cgnshow cgn instance
## logging-portrange-when 

logging-portrange-when 
命令功能 : 
配置portrange 日志产生的时机。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
logging-portrange-when 
  {[created 
],[deleted 
],[first-session-create 
],[last-session-delete 
]}
no logging-portrange-when 
  {[created 
],[deleted 
],[first-session-create 
],[last-session-delete 
]}
				
命令参数解释 : 
参数|描述
---|---
created|portrange的端口块创建的时候产生portrange端口块创建日志
deleted|portrange端口块删除的时候产生portrange端口块删除日志
first-session-create|portrange端口块内的端口被使用生成第一个映射条目时产生portrange创建日志
last-session-delete|portrange端口块内的被使用的端口删除最后一个映射条目时产生portrange删除日志
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn test 1ZXROSNG(config-cgn-test)#logZXROSNG(config-cgn-test-log)#logging-portrange-when createdZXROSNG(config-cgn-test-log)#
相关命令 : 
show running-config cgnshow cgn instance
## logging-protocol 

logging-protocol 
命令功能 : 
基于session生成log，可以指定协议类型（tcp,udp,icmp）发送 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
logging-protocol 
  {[tcp 
 {enable 
|disable 
}],[udp 
 {enable 
|disable 
}],[icmp 
 {enable 
|disable 
}]}
命令参数解释 : 
参数|描述
---|---
enable|使能记录icmp协议的日志，使能之后会记录icmp协议的日志
disable|去使能记录icmp协议的日志，去使能之后不会记录icmp协议的日志
enable|使能记录icmp协议的日志，使能之后会记录icmp协议的日志
disable|去使能记录icmp协议的日志，去使能之后不会记录icmp协议的日志
enable|使能记录icmp协议的日志，使能之后会记录icmp协议的日志
disable|去使能记录icmp协议的日志，去使能之后不会记录icmp协议的日志
缺省 : 
logging-protocol tcp enable udp enable icmp enable 
使用说明 : 
1．    只有当NAT日志模式下打开了enable开关，该命令才生效2．    tcp、udp、icmp协议可同时配置也可单独配置如 logging-protocol tcp disable udp enable icmp enablelogging-protocol icmp enable
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)# logging-protocol udp disable icmp disableZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## logging-translation-when 

logging-translation-when 
命令功能 : 
配置条目转换日志产生的时机。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
logging-translation-when 
  {created 
|deleted 
|created-and-deleted 
}
命令参数解释 : 
参数|描述
---|---
created|条目生成映射条目时产生日志
deleted|条目删除映射条目时产生日志
created-and-deleted|条目生成和删除时都产生日志
缺省 : 
created-and-deleted 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)#logging-translation-when createdZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## log-merging 

log-merging 
命令功能 : 
日志支持多条日志合并打包发送的开关 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
log-merging 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|日志支持多条日志合并打包发送开启
disable|日志支持多条日志合并打包发送关闭
缺省 : 
disable 
使用说明 : 
enable 后，表明开启日志并包功能
范例 : 
ZXROSNG(config-cgn-log)#log-merging ?disable Log merging disableenable Log merging enable
相关命令 : 
无 
## log-style 

log-style 
命令功能 : 
配置CGN日志规范方式。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
log-style 
  {style1 
|style2 
|style3 
}
命令参数解释 : 
参数|描述
---|---
style1|配置日志规范为style1
style2|配置日志规范为style2
style3|配置日志规范为style3
缺省 : 
log-style style1 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test-log)#log-style style2 
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool 
## mapping-mode 

mapping-mode 
命令功能 : 
TCP策略的条目映射模式配置。 
命令模式 : 
 NAT-TCP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
mapping-mode 
  {endpoint-independent 
|address-dependent 
|address-and-port-dependent 
}
no mapping-mode 
命令参数解释 : 
参数|描述
---|---
endpoint-independent|端点无关映射模式
address-dependent|地址相关映射模式
address-and-port-dependent|地址和端口相关映射模式
缺省 : 
endpoint-independent 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#tcp-policy ZXROSNG(config-cgn-zte-domain-tcp-policy)#mapping-mode address-and-port-dependentZXROSNG(config-cgn-zte-domain-tcp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## mapping-mode 

mapping-mode 
命令功能 : 
UDP策略的条目映射模式配置。 
命令模式 : 
 NAT-UDP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
mapping-mode 
  {endpoint-independent 
|address-dependent 
|address-and-port-dependent 
}
no mapping-mode 
命令参数解释 : 
参数|描述
---|---
endpoint-independent|端点无关映射模式
address-dependent|地址相关映射模式
address-and-port-dependent|地址和端口相关映射模式
缺省 : 
endpoint-independent 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policy ZXROSNG(config-cgn-zte-domain-udp-policy)#mapping-mode address-and-port-dependentZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## mapping-mode 

mapping-mode 
命令功能 : 
ICMP策略的映射模式配置。 
命令模式 : 
 NAT-ICMP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
mapping-mode 
  {endpoint-independent 
|address-dependent 
}
no mapping-mode 
命令参数解释 : 
参数|描述
---|---
endpoint-independent|端点无关映射模式
address-dependent|地址相关映射模式
缺省 : 
endpoint-independent 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#icmp-policyZXROSNG(config-cgn-zte-domain-icmp-policy)#mapping-mode address-dependentZXROSNG(config-cgn-zte-domain-icmp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## mapping-mode 

mapping-mode 
命令功能 : 
NAT策略的映射模式配置。 
命令模式 : 
 NAT-NAT策略模式  
命令默认权限级别 : 
15 
命令格式 : 
mapping-mode 
  {endpoint-independent 
|address-dependent 
}
no mapping-mode 
命令参数解释 : 
参数|描述
---|---
endpoint-independent|端点无关映射模式
address-dependent|地址相关映射模式
缺省 : 
endpoint-independent 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#nat-policy  ZXROSNG(config-cgn-zte-domain-nat-policy)# mapping-mode address-dependentZXROSNG(config-cgn-zte-domain-nat-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## max-lifetime 

max-lifetime 
命令功能 : 
配置PCP映射条目的最大生存时间。 
命令模式 : 
 NAT-PCP模式  
命令默认权限级别 : 
15 
命令格式 : 
max-lifetime 
  ＜max-life-time 
＞
no max-lifetime 
命令参数解释 : 
参数|描述
---|---
＜max-life-time＞|PCP映射条目的最大生存时间的范围，范围120~86400秒
缺省 : 
max-lifetime 86400 
使用说明 : 
无 
范例 : 
XR10(config-cgn-zte)# pcp-serviceZXROSNG(config-cgn-zte-pcp-service)# max-lifetime 500
相关命令 : 
show running-config cgnshow cgn instance 
## max-ports-per-address 

max-ports-per-address 
命令功能 : 
一个公网地址可以使用多少个端口。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
max-ports-per-address 
  ＜max-ports-per-address 
＞
no max-ports-per-address 
命令参数解释 : 
参数|描述
---|---
＜max-ports-per-address＞|一个IP地址端口使用数，默认值为65535。配置范围为1~65535
缺省 : 
65535 
使用说明 : 
一个公网地址可以使用多少个端口。no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#pat-pool zte poolid 0ZXROSNG(config-cgn-zte-patpool)#max-ports-per-address 1000ZXROSNG(config-cgn-zte-patpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## min-lifetime 

min-lifetime 
命令功能 : 
配置PCP映射条目的最小生存时间。 
命令模式 : 
 NAT-PCP模式  
命令默认权限级别 : 
15 
命令格式 : 
min-lifetime 
  ＜min-life-time 
＞
no min-lifetime 
命令参数解释 : 
参数|描述
---|---
＜min-life-time＞|PCP映射条目的最小生存时间的范围，范围120~86400秒
缺省 : 
min-lifetime 120 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-zte)# pcp-serviceZXROSNG(config-cgn-zte-pcp-service)# min-lifetime 500
相关命令 : 
show running-config cgnshow cgn instance 
## nat-policy 

nat-policy 
命令功能 : 
模式跳转命令，进入NAT策略配置模式。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
nat-policy 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#nat-policy  ZXROSNG(config-cgn-zte-domain-nat-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## new-session-create-speed 

new-session-create-speed 
命令功能 : 
配置新建会话 no NAT 上送限速，不配置则默认为不限速。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
new-session-create-speed 
  ＜session-speed 
＞
no new-session-create-speed 
命令参数解释 : 
参数|描述
---|---
＜session-speed＞|限速大小配置，范围1-50000，单位pps
缺省 : 
不配置则默认为不限速 
使用说明 : 
无 
范例 : 
XR10(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)# new-session-create-speed 500ZXROSNG(config-cgn-zte-domain)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## node 

node 
命令功能 : 
配置实例下的节点。 
命令模式 : 
 NAT-CGN实例位置模式  
命令默认权限级别 : 
15 
命令格式 : 
node 
  ＜node-id 
＞ ＜cpu-information 
＞ [＜cpu-information 
＞]
no node 
  ＜node-id 
＞
				
命令参数解释 : 
参数|描述
---|---
＜node-id＞|节点id，范围1~64
＜cpu-information＞|配置节点下的备CPU，可选
＜cpu-information＞|配置节点下的备CPU，可选
缺省 : 
无 
使用说明 : 
1) 主CPU和备CPU不能重复2) 不同node间CPU不能重复
范例 : 
ZXROSNG(config-cgn-test)#location ZXROSNG(config-cgn-test-location)#node 1 SPU-0/3/0 SPU-0/3/1
相关命令 : 
show running-config cgnshow cgn instance
## outbound 

outbound 
命令功能 : 
配置出向限速策略。 
命令模式 : 
 NAT-CAR限速模式  
命令默认权限级别 : 
15 
命令格式 : 
outbound 
 cir 
 ＜cir 
＞ cbs 
 ＜cbs 
＞ pir 
 ＜pir 
＞ pbs 
 ＜pbs 
＞
no outbound 
命令参数解释 : 
参数|描述
---|---
＜cir＞|配置承诺访问速率，取值范围： 66-16777215，单位kbps
＜cbs＞|配置承诺突发尺寸，取值范围：15-2000000，单位KB
＜pir＞|配置峰值信息速率，取值范围：66-16777215，单位kbps
＜pbs＞|配置峰值突发尺寸，取值范围：15-2000000，单位KB
缺省 : 
无。不配置则不进行限速。 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgnZXROSNG(config-cgn-?)#car-policy-template testZXROSNG(config-cgn-?-car-tmpl)#outbound cir 66 cbs 660 pir 66 pbs 660ZXROSNG(config-cgn-?-car-tmpl)#
相关命令 : 
show running-config cgnshow cgn instance summaryshow cgn instance verboseshow cgn car-policy
## pcp-service 

pcp-service 
命令功能 : 
模式跳转命令，进入PCP配置模式 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
pcp-service 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test)#pcp-service ZXROSNG(config-cgn-test-pcp-service)#
相关命令 : 
show running-config cgnshow cgn instance
## port-allowed-range 

port-allowed-range 
命令功能 : 
portrange允许使用的端口范围。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
port-allowed-range 
  ＜start-port 
＞ ＜end-port 
＞
no port-allowed-range 
命令参数解释 : 
参数|描述
---|---
＜start-port＞|起始端口，1或者是portrange size大小的整数倍
＜end-port＞|结束端口，必须是portrange size大小的整数倍减1，end-port必须大于start-port
缺省 : 
1-65535 
使用说明 : 
portrange允许使用的端口范围。no命令恢复默认值。与NAT-PAT地址池模式下port-range命令有关联。只有当port-range命令配置enable，才能配置port-allowed-range命令。且allowed-range命令配置的端口范围和port-range enable的port-range size相关
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#pat-pool zte poolid 0ZXROSNG(config-cgn-zte-patpool)#port-allowed-range 128 255ZXROSNG(config-cgn-zte-patpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## port-randomization 

port-randomization 
命令功能 : 
开启/关闭端口随机性配置。 
命令模式 : 
 NAT-UDP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
port-randomization 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启端口随机性策略
disable|关闭端口随机性策略
缺省 : 
disable 
使用说明 : 
不开启端口随机性功能，从小到大寻找可用端口分配；开启端口随机功能，则随机分配可用端口。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policy ZXROSNG(config-cgn-zte-domain-udp-policy)# port-randomization enableZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## port-randomization 

port-randomization 
命令功能 : 
TCP策略开启/关闭端口随机性配置。 
命令模式 : 
 NAT-TCP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
port-randomization 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能端口随机性策略
disable|去使能端口随机性策略
缺省 : 
disable 
使用说明 : 
不开启端口随机性功能，从小到大寻找可用端口分配；开启端口随机功能，则随机分配可用端口。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#tcp-policy ZXROSNG(config-cgn-zte-domain-tcp-policy)# port-randomization enableZXROSNG(config-cgn-zte-domain-tcp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## port-range max-blocks 

port-range max-blocks 
命令功能 : 
该命令用于修改配置用户可使用的动态portrange块数 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
port-range max-blocks 
  ＜num 
＞
no port-range max-blocks 
命令参数解释 : 
参数|描述
---|---
＜num＞|可配置的块数，范围<0-3>。其中0表示不限制用户使用的portrange块数
缺省 : 
缺省值为0，表示不限制用户使用portrange块数 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-?)#port-range max-blocks 3           ZXROSNG(config-cgn-?)#show runnZXROSNG(config-cgn-?)#show running-config cgn!<cgn>cgn  port-range max-blocks 3$!</cgn>ZXROSNG(config-cgn-?)#
相关命令 : 
show running-config cgn可显示show cgn instance也可以显示ZXROSNG(config-cgn-?)#port-range max-blocks 3           ZXROSNG(config-cgn-?)#show runnZXROSNG(config-cgn-?)#show running-config cgn!<cgn>cgn  port-range max-blocks 3$!</cgn>
## port-range 

port-range 
命令功能 : 
开启portrange配置功能，并且配置portrange大小。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
port-range 
  {enable 
 ＜port-range-size 
＞|disable 
}
命令参数解释 : 
参数|描述
---|---
＜port-range-size＞|使能portrange功能并配置portrange大小，范围$#35192841#$~65536
disable|去使能portrange功能
缺省 : 
无 
使用说明 : 
portrange大小配置必须能被65536整除。no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#pat-pool zte poolid 0ZXROSNG(config-cgn-zte-patpool)#port-range 1024ZXROSNG(config-cgn-zte-patpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## protocol-session-timeout 

protocol-session-timeout 
命令功能 : 
配置TCP、UDP协议的老化时间。 
命令模式 : 
 NAT高级模式  
命令默认权限级别 : 
15 
命令格式 : 
protocol-session-timeout 
  ＜description 
＞ {tcp 
|udp 
} ＜destination-port 
＞ ＜timeout-value 
＞
no protocol-session-timeout 
  {tcp 
|udp 
} ＜destination-port 
＞
				
命令参数解释 : 
参数|描述
---|---
＜description＞|对该配置的功能进行文字描述，范围1~63字节
tcp|TCP协议
udp|UDP协议
＜destination-port＞|协议端口号，范围1-65535
＜timeout-value＞|老化时间，范围1-7200，单位秒
缺省 : 
无 
使用说明 : 
优先于TCP/UDP协议老化时间。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#advanced-serviceZXROSNG(config-cgn-zte-adv-srv)# protocol-session-timeout bjt tcp 1024 3600ZXROSNG(config-cgn-zte-adv-srv)#
相关命令 : 
show running-config cgnshow cgn instance
## quota-exceed-action 

quota-exceed-action 
命令功能 : 
配置quota策略。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
quota-exceed-action 
  {discard 
|send-icmp-error 
}
命令参数解释 : 
参数|描述
---|---
discard|如果发送的包数量超过最大转换条目数则做丢弃处理
send-icmp-error|如果发送的包数量超过最大转换条目数则做发送icmp错误报告
缺省 : 
quota-exceed-action discard 
使用说明 : 
无 
范例 : 
ZXROSNG(config-cgn-test)#domain test 1 type sr ipv4-issued ZXROSNG(config-cgn-test-domain)#quota-exceed-action send-icmp-error 
相关命令 : 
show running-config cgnshow cgn instanceshow cgn domain 
## rate-limiting 

rate-limiting 
命令功能 : 
绑定限速策略。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
rate-limiting 
  {tcp 
 car-policy 
 ＜car-name 
＞|udp 
 car-policy 
 ＜car-name 
＞|icmp 
 car-policy 
 ＜car-name 
＞|subscriber 
 car-policy 
 ＜car-name 
＞}
no rate-limiting 
  {tcp 
|udp 
|icmp 
|subscriber 
}
				
命令参数解释 : 
参数|描述
---|---
tcp|对TCP类型的报文限速
＜car-name＞|car策略名称，范围1~31字节
udp|对UDP类型的报文限速
＜car-name＞|car策略名称，范围1~31字节
icmp|对ICMP类型的报文限速
＜car-name＞|car策略名称，范围1~31字节
subscriber|对用户类型的报文限速
＜car-name＞|car策略名称，范围1~31字节
缺省 : 
无 
使用说明 : 
引用的CAR策略必须是已存在的，且当rate-limiting命令引用CAR策略时，该策略不可删除。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-zte-cgn)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#rate-limiting tcp car-policy testZXROSNG(config-cgn-zte-domain)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## reference 

reference 
命令功能 : 
配置sib instance，绑定sib instance，把当前地址池加入到sib instance中，热备功能使用。 
命令模式 : 
 NAT-NAT地址池模式,NAT-PAT地址池模式  
命令默认权限级别 : 
NAT-NAT地址池模式:15,NAT-PAT地址池模式:15 
命令格式 : 
reference 
 sib-instance 
 ＜instanceid 
＞
no reference 
 sib-instance 
命令参数解释 : 
参数|描述
---|---
＜instanceid＞|Sib instance id，范围为1-255
No参数|描述
---|---
sib-instance|配置sib instance
缺省 : 
无 
使用说明 : 
一个地址池只能添加到一个sib instance中去 
范例 : 
ZXROSNG(config-cgn-test-patpool)#reference sib-instance 200 
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool 
## refreshing-mode 

refreshing-mode 
命令功能 : 
TCP策略转换条目的刷新模式。 
命令模式 : 
 NAT-TCP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
refreshing-mode 
  {outbound 
|both-bounds 
|inbound 
}
no refreshing-mode 
命令参数解释 : 
参数|描述
---|---
outbound|仅outbound流量能够触发映射条目刷新
both-bounds|inbound和outbound双向流量均能触发映射条目刷新
inbound|仅inbound流量能够触发映射条目刷新
缺省 : 
outbound 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#tcp-policyZXROSNG(config-cgn-zte-domain-tcp-policy)#refreshing-mode inbound ZXROSNG(config-cgn-zte-domain-tcp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## refreshing-mode 

refreshing-mode 
命令功能 : 
UDP策略转换条目的刷新模式。 
命令模式 : 
 NAT-UDP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
refreshing-mode 
  {outbound 
|both-bounds 
|inbound 
}
no refreshing-mode 
命令参数解释 : 
参数|描述
---|---
outbound|仅outbound流量能够触发映射条目刷新
both-bounds|inbound和outbound双向流量均能触发映射条目刷新
inbound|仅inbound流量能够触发映射条目刷新
缺省 : 
outbound 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policyZXROSNG(config-cgn-zte-domain-udp-policy)#refreshing-mode inbound ZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## refreshing-mode 

refreshing-mode 
命令功能 : 
ICMP策略转换条目的刷新模式。 
命令模式 : 
 NAT-ICMP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
refreshing-mode 
  {outbound 
|both-bounds 
|inbound 
}
no refreshing-mode 
命令参数解释 : 
参数|描述
---|---
outbound|仅outbound流量能够触发映射条目刷新
both-bounds|inbound和outbound双向流量均能触发映射条目刷新
inbound|仅inbound流量能够触发映射条目刷新
缺省 : 
outbound 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgnZXROSNG(config-cgn-?)#domain 1 1 type sr ipv4-issuedZXROSNG(config-cgn-?)#icmp-policyZXROSNG(config-cgn-?-domain-icmp-policy)#refreshing-mode both-bounds ZXROSNG(config-cgn-?-domain-icmp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## refreshing-mode 

refreshing-mode 
命令功能 : 
NAT策略转换条目的刷新模式。 
命令模式 : 
 NAT-NAT策略模式  
命令默认权限级别 : 
15 
命令格式 : 
refreshing-mode 
  {outbound 
|both-bounds 
|inbound 
}
no refreshing-mode 
命令参数解释 : 
参数|描述
---|---
outbound|仅outbound流量能够触发映射条目刷新
both-bounds|inbound和outbound双向流量均能触发映射条目刷新
inbound|仅inbound流量能够触发映射条目刷新
缺省 : 
outbound 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#nat-policy  ZXROSNG(config-cgn-zte-domain-nat-policy)# refreshing-mode inboundZXROSNG(config-cgn-zte-domain-nat-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## resource-exhaust-action 

resource-exhaust-action 
命令功能 : 
配置资源耗尽时的操作。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
resource-exhaust-action 
  {drop 
|send-icmp-error 
}
命令参数解释 : 
参数|描述
---|---
drop|资源耗尽，丢弃报文
send-icmp-error|资源耗尽，发送icmp差错报文
缺省 : 
drop 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#resource-exhaust-action drop ZXROSNG(config-cgn-zte)#
相关命令 : 
show running-config cgnshow cgn instance
## resource-exhaust-action 

resource-exhaust-action 
命令功能 : 
配置资源耗尽时的处理操作。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
resource-exhaust-action 
  {stop-cgn-service 
|stop-logging 
}
命令参数解释 : 
参数|描述
---|---
stop-cgn-service|停止CGN功能。配置后不进行NAT转换
stop-logging|停止发送日志功能。配置后不再记录日志，伴随会有日志丢失。
缺省 : 
stop-logging 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)# resource-exhaust-action stop-loggingZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## resume-delay 

resume-delay 
命令功能 : 
设置当前实例第一个SPU up后，实例恢复工作状态的时延。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
resume-delay 
  ＜num 
＞
no resume-delay 
命令参数解释 : 
参数|描述
---|---
＜num＞|无默认值，单位：分钟，配置范围 1~10
缺省 : 
无 
使用说明 : 
该命令一般用在独立式保护分布式场景中，如果实例中存在多个SPU时，建议配置恢复时延，尽量使得该时间范围内，实例下所有SPU，均能够UP，避免因SPU up导致流量震荡。对于非独立式保护分布式场景，无需配置该命令，如果配置了，实例开始正常工作的时间会有相应的延时。
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)# resume-delay 10
相关命令 : 
无 
## section 

section 
命令功能 : 
配置NAT地址池地址范围。 
命令模式 : 
 NAT-NAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
section 
  ＜section-num 
＞ {＜start-ipv4-address 
＞ [＜end-ipv4-address 
＞]|＜ip-address/mask-length 
＞}
no section 
  ＜section-num 
＞
				
命令参数解释 : 
参数|描述
---|---
＜section-num＞|用来标识子地址池。配置范围1~200
＜start-ipv4-address＞|子地址池的起始地址(必选)
＜end-ipv4-address＞|子地址池的结束地址(可选)
＜ip-address/mask-length＞|配置ip/mask，mask参数范围19~32
缺省 : 
无 
使用说明 : 
配置地址池IP范围。当一个 section中只配置一个ip时，起始IP与终止IP相同。所配置的section中起始IP和终止IP中不能包含全0地址、组播地址、环回地址、保留地址、0.x.x.x。当section中的IP地址被静态规则使用时，section不可以删除
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#nat-pool zte poolid 0ZXROSNG(config-cgn-zte-natpool)# section 1 10.10.10.1 10.10.10ZXROSNG(config-cgn-zte-natpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## section 

section 
命令功能 : 
配置PAT地址池地址段。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
section 
  ＜section-number 
＞ {＜start-ipv4-address 
＞ [＜end-ipv4-address 
＞]|＜ip-address/mask-length 
＞}
no section 
  ＜section-number 
＞
				
命令参数解释 : 
参数|描述
---|---
＜section-number＞|用来标识子地址池。配置范围1~200
＜start-ipv4-address＞|子地址池的起始地址(必选)
＜end-ipv4-address＞|子地址池的结束地址(可选)
＜ip-address/mask-length＞|配置ip/mask，mask参数范围19~32
缺省 : 
无 
使用说明 : 
配置地址池IP范围。当一个 section中只配置一个ip时，起始IP与终止IP相同。所配置的section中起始IP和终止IP中不能包含全0地址、组播地址、环回地址、保留地址、0.x.x.x。
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#pat-pool zte poolid 0ZXROSNG(config-cgn-zte-patpool)# section 1 10.10.10.1 10.10.10ZXROSNG(config-cgn-zte-patpool)#
相关命令 : 
show running-config cgnshow cgn instanceshow cgn-pool
## session-mode 

session-mode 
命令功能 : 
配置是否开启全session模式 
命令模式 : 
 NAT高级模式  
命令默认权限级别 : 
15 
命令格式 : 
session-mode 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|使能全session模式
disable|去使能全session模式
缺省 : 
session-mode disable 
使用说明 : 
当在session模式之间切换时，条目会全部删除，重新生成。 
范例 : 
ZXROSNG(config-cgn-adv-srv)#session-mode ?  disable  Disable session mode  enable   Enable session mode
相关命令 : 
show cgn instance summaryshow running-config cgn
## show cgn car-policy 

show cgn car-policy 
命令功能 : 
显示cgn car-policy的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn car-policy 
  [{instance 
 ＜instance-name 
＞|car-name 
 ＜car-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜instance-name＞|CGN实例名称，范围1~31个字节
＜car-name＞|car策略名称，范围1~31个字节
缺省 : 
无 
使用说明 : 
如果不输入car-policy和instance名称的话，则显示所有car-policy的配置信息。 
范例 : 
ZXROSNG(config)#show cgn car-policy car-name test                                                 car-policy-template test                                                                                                              inbound cir 0 cbs 0 pir 0 pbs 0                                                                                                     outbound cir 0 cbs 0 pir 0 pbs 0                                                                                                  ZXROSNG(config)# 
相关命令 : 
无 
## show cgn domain 

show cgn domain 
命令功能 : 
显示cgn instance的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn domain 
  [{instance 
 ＜instance-name 
＞|domain-name 
 ＜domain-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜instance-name＞|CGN实例名称，范围1~31个字节
＜domain-name＞|域名称，范围1~31个字节
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show cgn domain domain-name test                                      cgn=======================================================================domain test 1 type sr ipv4-issued  quota-exceed-action discard  alarm-threshold softwire-error 4294967295  max-static-rule-num 2000  max-translations per-ipv4 tcp dynamic 1500000 pcp 1500000  max-translations per-ipv4 udp dynamic 1500000 pcp 1500000  max-translations per-ipv4 icmp dynamic 1500000  max-translations per-ipv4 nat dynamic 1500000  max-translations per-ipv4 all dynamic 1500000 pcp 1500000  max-translations per-softwire tcp dynamic 1500000 pcp 1500000  max-translations per-softwire udp dynamic 1500000 pcp 1500000  max-translations per-softwire icmp dynamic 1500000  max-translations per-softwire nat dynamic 1500000  max-translations per-softwire all dynamic 1500000 pcp 1500000  max-translations per-subscriber tcp dynamic 1500000 pcp 1500000  max-translations per-subscriber udp dynamic 1500000 pcp 1500000  max-translations per-subscriber icmp dynamic 1500000  max-translations per-subscriber nat dynamic 1500000  max-translations per-subscriber all dynamic 1500000 pcp 1500000  dns-exclude-session-limit disable  max-private-address 200000  address-policy    same-address-allocate for-same-ipv4: random    same-address-allocate for-same-softwire: random    same-address-allocate for-same-user: random  icmp-policy    filtering-mode endpoint-independent    mapping-mode endpoint-independent    refreshing-mode outbound    timeout 60  nat-policy    filtering-mode endpoint-independent    mapping-mode endpoint-independent    refreshing-mode outbound    timeout 120  tcp-policy    filtering-mode endpoint-independent    mapping-mode endpoint-independent    refreshing-mode outbound    timeout unwell-known-port tcp 120 tcp-syn 60 tcp-fin-rst 120    timeout well-known-port tcp 120 tcp-syn 60 tcp-fin-rst 120    port-parity-preserve disable    port-randomization disable  udp-policy    filtering-mode endpoint-independent    mapping-mode endpoint-independent    refreshing-mode outbound    timeout unknown-port 180    timeout wellknown-port 180    port-parity-preserve disable    port-randomization disable  dynamic source rule-id 1 ipv4-list zte permit pool-id 1           ZXROSNG(config)#   
相关命令 : 
无 
## show cgn instance 

show cgn instance 
命令功能 : 
显示cgn instance的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn instance 
  {summary 
|verbose 
} [＜instance-name 
＞] 
命令参数解释 : 
参数|描述
---|---
summary|显示CGN实例的概要信息
verbose|显示CGN实例的详细信息
＜instance-name＞|CGN实例名称，范围1~31个字节
缺省 : 
无 
使用说明 : 
summary和verbose的区别在于domain显示上，verbose会显示没有配置的缺省值，summary不会 
范例 : 
ZXROSNG(config)#show cgn instance summary                                                                              cgn instance test 1----------------------------------------------------------------------  resource-exhaust-action drop  statistics off  advanced-service    disable    tcp-mss-clamping disable    tcp-mss-clamping new-mss-value 0    tcp-state-tracking disable     alg FTP disable    alg DNS disable    alg RTSP disable    alg SIP disable    alg ICMP disable    alg H323 disable    alg PPTP disable  alarm    disable    alarm-threshold resource 80    alarm-threshold translations 80  log    buffer-size 16    destination local    disable    format text    logging-portrange-detail disable    logging-translation-when created-and-deleted    resource-exhaust-action stop-logging    stop-service-on-err disable  cgn-pool test poolid 1 mode pat  car-policy-template test  domain test 1 type sr ipv4-issued                                                                                                                            ZXROSNG(config)#
相关命令 : 
无 
## show cgn performance 

show cgn performance 
命令功能 : 
CGN性能项显示。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn performance 
  {session-utilization 
|create-session-num 
|delete-session-num 
|session-num 
|create-session-rate 
|delete-session-rate 
|local-ip-num 
|subscriber-num 
|total-session-log 
|create-session-log 
|delete-session-log 
|total-portrange-log 
|create-portrange-log 
|delete-portrange-log 
|syslog-packet 
|ipflow-packet 
} [{board 
 ＜board-name 
＞|cpu 
 ＜cpu-info 
＞}] 
命令参数解释 : 
参数|描述
---|---
session-utilization|条目使用率
create-session-num|创建条目数
delete-session-num|删除条目数
session-num|条目数
create-session-rate|创建条目速率
delete-session-rate|删除条目速率
local-ip-num|私网IP数
subscriber-num|用户数
total-session-log|总的会话日志
create-session-log|新建会话日志
delete-session-log|删除会话日志
total-portrange-log|总的PORTRANGE日志
create-portrange-log|新建PORTRANGE日志
delete-portrange-log|删除PORTRANGE日志
syslog-packet|SYSLOG报文数
ipflow-packet|IPFLOW报文数
＜board-name＞|单板名称
＜cpu-info＞|CPU名称
缺省 : 
无 
使用说明 : 
CGN性能项开关performance-statistics打开才会有数据显示。条目使用率是基于CPU的，没有整机的统计。 
范例 : 
ZXROSNG# show cgn performance local-ip-num================================================================================Location          =   SPU-0/2/0Current           =   115min-average     =   015min-peak        =   115min-valley      =   024h-average       =   024h-peak          =   024h-valley        =   0--------------------------------------------------------------------------------Location          =   TotalCurrent           =   115min-average     =   015min-peak        =   115min-valley      =   024h-average       =   024h-peak          =   024h-valley        =   0--------------------------------------------------------------------------------ZXROSNG#参数    描述Location    CPU信息，命令既不配置board，又不配置CPU时，显示Total表示整机数值；配置board时，显示Total表示单板数值；配置CPU时，没有TotalCurrent    显示性能项属性的当前值15min-average    显示性能项属性的15分钟内均值15min-peak    显示性能项属性的15分钟内峰值15min-valley    显示性能项属性的15分钟内谷值24h-average    显示性能项属性的值24小时内均值24h-peak    显示性能项属性的值24小时内峰值 24h-valley    显示性能项属性的值24小时内谷值 
相关命令 : 
performance-statistics on 
## show cgn pool-utilization 

show cgn pool-utilization 
命令功能 : 
显示CGN地址池利用率。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn pool-utilization 
  {pat-pool 
 ＜pool-name 
＞ [＜ipv4-address 
＞]|pool 
 ＜pool-name 
＞ verbose 
|all 
 {verbose 
|summary 
}} [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
pat-pool|关键字，表明是PAT地址池
＜pool-name＞|地址池名称，范围1~31个字节
＜ipv4-address＞|IPv4地址。可选项，不配置则显示指定pool的资源利用率
pool|关键字，表明地址池，不区分PAT和NAT
＜pool-name＞|地址池名称，范围1~31个字节
verbose|显示所有地址池利用率的详细信息
verbose|显示所有地址池利用率的详细信息
summary|显示所有地址池利用率的概要信息
＜spu＞|指定CPU
＜instance-name＞|指定实例名称
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show cgn pool-utilization pat-pool pat                                                                                ================================================================================                                                    Global          Number(Percent)    Number(Percent)    Number(Percent)    Dynamic                                                                      of used            of used            of used           Share                                                     Address          TCP ports          UDP ports           ICMP ID           Ratio                                                     ================================================================================                                                    16.1.1.1        1(0.00%)           65,535(100.00%)    0(0.00%)                                                                  --------------------------------------------------------------------------------                                                    ZXROSNG(config)#
相关命令 : 
无 
## show cgn static-port-range 

show cgn static-port-range 
命令功能 : 
显示cgn static-port-range的配置。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn static-port-range 
 all 
 {verbose 
|summary 
} 
命令参数解释 : 
参数|描述
---|---
verbose|显示静态portrange的详细信息
summary|显示静态portrange的概要信息
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#show cgn static-port-range all summary                                                                            ===============================================================================                                                     Static Port Range Information Of Public:                                                                                            ===============================================================================                                                     Local IP                                      Global IP         Port Range                                                          ===============================================================================                                                     10.1.1.1                                      150.0.0.1         1~127                                                               10.1.1.2                                      150.0.0.1         128~255                                                             10.1.1.3                                      150.0.0.1         256~383                                                             10.1.1.4                                      150.0.0.1         384~511                                                             10.1.1.5                                      150.0.0.1         512~639                                                             10.1.1.6                                      150.0.0.1         640~767                                                             10.1.1.7                                      150.0.0.1         768~895                                                             10.1.1.8                                      150.0.0.1         896~1023                                                            10.1.1.9                                      150.0.0.1         1024~1151                                                           10.1.1.10                                     150.0.0.1         1152~1279                                                           -------------------------------------------------------------------------------                                                     ZXROSNG(config)#                                                                                                                   
相关命令 : 
无 
## show cgn subscriber-port-range 

show cgn subscriber-port-range 
命令功能 : 
显示cgn 用户的portrange端口分配情况配置。静态和动态的都会显示。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn subscriber-port-range 
  {all 
 [summary 
]|exhaust 
 [subscriber 
 [vrf 
 ＜vrf-name 
＞] {＜ipv4-address 
＞|＜cpe-ipv6-prefix 
＞}]|subscriber 
 [vrf 
 ＜vrf-name 
＞] {＜ipv4-address 
＞|＜cpe-ipv6-prefix 
＞}|pool 
 ＜pool-name 
＞ summary 
} [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
all|显示所有用户portrange信息
summary|显示所有用户概要portrange信息
exhaust|显示cgn用户的portrange资源耗尽和恢复的记录
＜vrf-name＞|指定VRF
＜ipv4-address＞|指定用户IPv4 地址
＜cpe-ipv6-prefix＞|指定用户CPE IPv6前缀
＜vrf-name＞|指定VRF
＜ipv4-address＞|指定用户IPv4 地址
＜cpe-ipv6-prefix＞|指定用户CPE IPv6前缀
＜pool-name＞|指定地址池
summary|显示所有用户概要portrange信息
＜spu＞|指定CPU
＜instance-name＞|指定实例名称
缺省 : 
无 
使用说明 : 
1）当指定的pool-name不存在，或者不是pat地址池，或者不是portrange地址池时，该命令无回显。 
范例 : 
显示每个portrange块当前使用率，分TCP、UDP、ICMPZXROSNG(config)#show cgn subscriber-port-range all================================================================================Subscriber                                    Local IP           Global IP       StartPort EndPort   TCP    UDP   ICMP================================================================================Loading data from SPU-0/2/0 ... ================================================================================10.1.1.1                                                        100.111.111.128 65536     66255     60%    50%    10%--------------------------------------------------------------------------------10.1.1.2                                                 100.1.1.28      256       511       10%    2%     1%-------------------------------------------------------------------------------
相关命令 : 
无 
## show cgn translations aftr-address 

show cgn translations aftr-address 
命令功能 : 
指定AFTR（Address Family Transition Router）地址显示NAT转换条目，可具体指定如某个协议（TCP、UDP、ICMP）条目，某种转换类型（动静态、alg、pcp）条目，某个公网IP条目，某个私网IP条目，某个SPU条目，某个接口条目，某个实例条目等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn translations aftr-address 
  ＜aftr-ipv6-adress 
＞ {all 
 [verbose 
]|protocol 
 {tcp 
|udp 
|icmp 
} [verbose 
]|translation-type 
 {static 
|pcp 
|dynamic 
|alg 
} [verbose 
]|{local-ip 
|global-ip 
} ＜ipv4-address 
＞ [{verbose 
|＜port-or-start-port 
＞ [{verbose 
|＜end-port 
＞ [verbose 
]}]}]} [interface 
 ＜smgr-name 
＞] [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜aftr-ipv6-adress＞|显示指定AFTR IPv6地址的详细NAT条目
all|显示所有相关NAT转换条目信息
verbose|显示详细信息
tcp|TCP协议类型
udp|UDP协议类型
icmp|ICMP协议类型
verbose|显示详细信息
static|静态条目类型
pcp|PCP条目类型
dynamic|动态条目类型
alg|ALG条目类型
verbose|显示详细信息
local-ip|私网地址
global-ip|公网地址
＜ipv4-address＞|IPv4地址
verbose|显示详细信息
＜port-or-start-port＞|端口或者起始端口
verbose|显示详细信息
＜end-port＞|结束端口
verbose|显示详细信息
＜smgr-name＞|指定SG接口显示条目
＜spu＞|显示指定SPU条目
＜instance-name＞|显示指定实例条目
缺省 : 
无 
使用说明 : 
无 
范例 : 
EIM+EIF也显示目的地址和目的端口，只是在后面加*表示任意地址，便于信息展示ZXROSNG#show cgn translations aftr-address 6000::1 all  ================================================================================Subscriber VPN  Pro  Type Inside Local          Inside Global         Destination================================================================================Loading data from SPU-0/2/0 ... ================================================================================6000::2  UDP  dyn  55.1.1.1:1000         198.216.90.129:1      132.1.1.2*:1000*--------------------------------------------------------------------------------ZXROSNG#                 
相关命令 : 
无 
## show cgn translations all-sessions 

show cgn translations all-sessions 
命令功能 : 
显示所有的NAT转换条目，可具体指定如显示概要信息，显示详细信息，某个SPU条目，某个接口条目，某个实例条目等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn translations all-sessions 
  [{summary 
 [extended 
]|verbose 
}] [interface 
 ＜smgr-name 
＞] [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
summary|显示概要信息
extended|所有条目汇总的报文扩展概要计数信息
verbose|显示详细信息
＜smgr-name＞|指定SG接口显示条目
＜spu＞|显示指定SPU条目
＜instance-name＞|显示指定实例条目
缺省 : 
无 
使用说明 : 
无 
范例 : 
EIM+EIF也显示目的地址和目的端口，只是在后面加*表示任意地址，便于信息展示ZXROSNG#show cgn translations all-sessions ================================================================================Subscriber VPN  Pro  Type Inside Local          Inside Global         Destination================================================================================Loading data from SPU-0/2/0 ... ================================================================================6000::2  UDP  dyn  55.1.1.1:1000         198.216.90.129:1      132.1.1.2*:1000*--------------------------------------------------------------------------------ZXROSNG#
相关命令 : 
无 
## show cgn translations cpe-address 

show cgn translations cpe-address 
命令功能 : 
指定CPE地址显示NAT转换条目，可具体指定如某个协议（TCP、UDP、ICMP）条目，某种转换类型（动静态、alg、pcp）条目，某个公网IP条目，某个私网IP条目，某个SPU条目，某个接口条目，某个实例条目等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn translations cpe-address 
  ＜cpe-ipv6-address 
＞ {all 
 [verbose 
]|protocol 
 {tcp 
|udp 
|icmp 
} [verbose 
]|translation-type 
 {static 
|pcp 
|dynamic 
|alg 
} [verbose 
]|{local-ip 
|global-ip 
} ＜ipv4-address 
＞ [{verbose 
|＜port-or-start-port 
＞ [{verbose 
|＜end-port 
＞ [verbose 
]}]}]} [interface 
 ＜smgr-name 
＞] [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜cpe-ipv6-address＞|指定CPE IPv6地址
all|显示所有相关NAT转换条目信息
verbose|显示详细信息
tcp|TCP协议类型
udp|UDP协议类型
icmp|ICMP协议类型
verbose|显示详细信息
static|静态条目类型
pcp|PCP条目类型
dynamic|动态条目类型
alg|ALG条目类型
verbose|显示详细信息
local-ip|私网地址
global-ip|公网地址
＜ipv4-address＞|IPv4地址
verbose|显示详细信息
＜port-or-start-port＞|端口或者起始端口
verbose|显示详细信息
＜end-port＞|结束端口
verbose|显示详细信息
＜smgr-name＞|指定SG接口显示条目
＜spu＞|显示指定SPU条目
＜instance-name＞|显示指定实例条目
缺省 : 
无 
使用说明 : 
无 
范例 : 
EIM+EIF也显示目的地址和目的端口，只是在后面加*表示任意地址，便于信息展示ZXROSNG#show cgn translations cpe-address 6000::2 all                                                                                                         ================================================================================Subscriber VPN  Pro  Type Inside Local          Inside Global         Destination================================================================================Loading data from SPU-0/2/0 ... ================================================================================6000::2  UDP  dyn  55.1.1.1:1000         198.216.90.129:1      132.1.1.2*:1000*--------------------------------------------------------------------------------ZXROSNG#
相关命令 : 
无 
## show cgn translations global-ip 

show cgn translations global-ip 
命令功能 : 
指定公网地址显示NAT转换条目，可具体指定如某个端口条目，某个SPU条目，某个接口条目，某个实例条目等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn translations global-ip 
  ＜ipv4-address 
＞ [{verbose 
|＜port-or-start-port 
＞ [{verbose 
|＜end-port 
＞ [verbose 
]}]}] [interface 
 ＜smgr-name 
＞] [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|IPv4地址
verbose|显示详细信息
＜port-or-start-port＞|端口或者起始端口
verbose|显示详细信息
＜end-port＞|结束端口
verbose|显示详细信息
＜smgr-name＞|指定SG接口显示条目
＜spu＞|显示指定SPU条目
＜instance-name＞|显示指定实例条目
缺省 : 
无 
使用说明 : 
无 
范例 : 
EIM+EIF也显示目的地址和目的端口，只是在后面加*表示任意地址，便于信息展示ZXROSNG#show cgn translations global-ip 198.216.90.129 ================================================================================Subscriber VPN  Pro  Type Inside Local          Inside Global         Destination================================================================================Loading data from SPU-0/2/0 ... ================================================================================6000::2  UDP  dyn  55.1.1.1:1000         198.216.90.129:1      132.1.1.2*:1000*--------------------------------------------------------------------------------ZXROSNG#
相关命令 : 
无 
## show cgn translations local-ip 

show cgn translations local-ip 
命令功能 : 
指定私网地址显示NAT转换条目，可具体指定如显示概要信息，显示详细信息，某个端口条目，某个SPU条目，某个接口条目，某个实例条目等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn translations local-ip 
  ＜ipv4-address 
＞ [{summary 
|verbose 
|＜port-or-start-port 
＞ [{verbose 
|＜end-port 
＞ [verbose 
]}]}] [interface 
 ＜smgr-name 
＞] [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜ipv4-address＞|IPv4地址
summary|显示概要信息
verbose|显示详细信息
＜port-or-start-port＞|端口或者起始端口
verbose|显示详细信息
＜end-port＞|结束端口
verbose|显示详细信息
＜smgr-name＞|指定SG接口显示条目
＜spu＞|显示指定SPU条目
＜instance-name＞|显示指定实例条目
缺省 : 
无 
使用说明 : 
无 
范例 : 
EIM+EIF也显示目的地址和目的端口，只是在后面加*表示任意地址，便于信息展示ZXROSNG#show cgn translations local-ip 55.1.1.1 summary ================================================================================CPU                 TCP-PAT       UDP-PAT      ICMP-PAT           ALG================================================================================SPU-0/2/0                 0             1             0             0--------------------------------------------------------------------------------Total                     0             1             0             0--------------------------------------------------------------------------------ZXROSNG#
相关命令 : 
无 
## show cgn translations protocol 

show cgn translations protocol 
命令功能 : 
指定协议显示NAT转换条目，可具体指定如某个协议（TCP、UDP、ICMP）条目，某种转换类型（动静态、alg、pcp）条目，某个SPU条目，某个接口条目，某个实例条目等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn translations protocol 
  {tcp 
|udp 
|icmp 
} [translation-type 
 {static 
|pcp 
|dynamic 
|alg 
}] [verbose 
] [interface 
 ＜smgr-name 
＞] [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
tcp|TCP协议类型
udp|UDP协议类型
icmp|ICMP协议类型
static|静态条目类型
pcp|PCP条目类型
dynamic|动态条目类型
alg|ALG条目类型
verbose|显示详细信息
＜smgr-name＞|指定SG接口显示条目
＜spu＞|显示指定SPU条目
＜instance-name＞|显示指定实例条目
缺省 : 
无 
使用说明 : 
无 
范例 : 
EIM+EIF也显示目的地址和目的端口，只是在后面加*表示任意地址，便于信息展示ZXROSNG#show cgn translations protocol udp ================================================================================Subscriber VPN  Pro  Type Inside Local          Inside Global         Destination================================================================================Loading data from SPU-0/2/0 ... ================================================================================6000::2  UDP  dyn  55.1.1.1:1000         197.143.206.47:1      132.1.1.2*:1000*--------------------------------------------------------------------------------ZXROSNG#
相关命令 : 
无 
## show cgn translations translation-type 

show cgn translations translation-type 
命令功能 : 
指定转换类型显示NAT转换条目，可具体指定如某个协议（TCP、UDP、ICMP）条目，某种转换类型（动静态、alg、pcp）条目，某个SPU条目，某个接口条目，某个实例条目等。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn translations translation-type 
  {static 
|pcp 
|dynamic 
|alg 
} [protocol 
 {tcp 
|udp 
|icmp 
}] [verbose 
] [interface 
 ＜smgr-name 
＞] [{＜spu 
＞|instance 
 ＜instance-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
static|静态条目类型
pcp|PCP条目类型
dynamic|动态条目类型
alg|ALG条目类型
tcp|TCP协议类型
udp|UDP协议类型
icmp|ICMP协议类型
verbose|显示详细信息
＜smgr-name＞|指定SG接口显示条目
＜spu＞|显示指定SPU条目
＜instance-name＞|显示指定实例条目
缺省 : 
无 
使用说明 : 
无 
范例 : 
EIM+EIF也显示目的地址和目的端口，只是在后面加*表示任意地址，便于信息展示ZXROSNG#show cgn  translations translation-type dynamic  ================================================================================Subscriber VPN  Pro  Type Inside Local          Inside Global         Destination================================================================================Loading data from SPU-0/2/0 ... ================================================================================6000::2  UDP  dyn  55.1.1.1:1000         197.143.206.47:1      132.1.1.2*:1000*--------------------------------------------------------------------------------ZXROSNG#
相关命令 : 
无 
## show cgn translation-top 

show cgn translation-top 
命令功能 : 
显示占用条目最多的私网用户 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn translation-top 
  ＜top-value 
＞ 
命令参数解释 : 
参数|描述
---|---
＜top-value＞|占用条目最多的私网用户的个数，范围1~10
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG#show cgn translation-top 1================================================================================Loading data from SPU-0/2/0 ... ================================================================================SEQ-NUM     = 1CPE-ADDRESS = VRF-NAME    = LOCAL-IP    = 10.1.1.3TRANS-NUM   = 3--------------------------------------------------------------------------------ZXROSNG#
相关命令 : 
无 
## show cgn-pool 

show cgn-pool 
命令功能 : 
显示CGN pool的配置情况。 
命令模式 : 
 除用户模式外的其他所有模式  
命令默认权限级别 : 
15 
命令格式 : 
show cgn-pool 
  [{instance 
 ＜instance-name 
＞|pool-name 
 ＜pool-name 
＞}] 
命令参数解释 : 
参数|描述
---|---
＜instance-name＞|实例名称，范围1~31字节
＜pool-name＞|地址池名称，范围1~31字节
缺省 : 
无 
使用说明 : 
如果不配置地址池名称，则显示所有地址池信息。 
范例 : 
ZXROSNG(config)#show cgn-pool pool-name test    cgn-pool test poolid 1 mode pat  max-ports-per-address 65535  alarm-threshold port-range 80  alarm-threshold port-range-block 80  alarm-threshold port-utilization 80  alarm-threshold sharing-ratio 80  section 1 1.1.1.10ZXROSNG(config)#
相关命令 : 
无 
## static-port-range 

static-port-range 
命令功能 : 
配置静态port-range。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
static-port-range 
  {vrf 
 ＜vrf-name 
＞|public 
} {＜start-ipv4-address 
＞ ＜end-ipv4-address 
＞|＜start-ipv6-prefix 
＞ ＜end-ipv6-prefix 
＞} cgn-pool 
 ＜pool-id 
＞ [nat-domain 
 ＜domain-id 
＞]
no static-port-range 
  {cgn-pool 
 ＜pool-id 
＞|{vrf 
 ＜vrf-name 
＞|public 
} {＜start-ipv4-address 
＞|＜start-ipv6-prefix 
＞}}
				
命令参数解释 : 
参数|描述
---|---
vrf|关键字，表明是VRF接口
＜vrf-name＞|VRF名称，根据配置的VRF确定
public|public接口
＜start-ipv4-address＞|V4用户私网IP起始地址
＜end-ipv4-address＞|V4用户私网IP结束地址
＜start-ipv6-prefix＞|V6用户私网前缀起始地址和掩码
＜end-ipv6-prefix＞|V6用户私网前缀结束地址和掩码
＜pool-id＞|pool ID，取值范围0~1999
＜domain-id＞|domain ID，取值范围1~4000
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1 ZXROSNG(config-cgn-zte)# static-port-range public 1.1.1.1 1.1.1.10 cgn-pool 1  nat-domain 1ZXROSNG(config-cgn-zte)#
相关命令 : 
show running-config cgn 
## statistics 

statistics 
命令功能 : 
打开/关闭统计开关。 
命令模式 : 
 NAT模式  
命令默认权限级别 : 
15 
命令格式 : 
statistics 
  {on 
|off 
}
命令参数解释 : 
参数|描述
---|---
on|打开统计开关
off|关闭统计开关
缺省 : 
off 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#statistics on ZXROSNG(config-cgn-zte)#
相关命令 : 
show running-config cgnshow cgn instance show cgn statistics clear cgn statistics
## stop-service-on-err 

stop-service-on-err 
命令功能 : 
开启/关闭CGN日志，故障则停止CGN业务功能 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
stop-service-on-err 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启CGN日志故障则停止CGN业务功能。日志通道出现错误时候，不发送日志，通常的日志故障会有日志磁盘满等情况
disable|关闭CGN日志故障则停止CGN业务功能。配置后，日志通道出现错误时候，仍然继续发送日志
缺省 : 
disable 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#logZXROSNG(config-cgn-zte-log)#stop-service-on-err enableZXROSNG(config-cgn-zte-log)#
相关命令 : 
show running-config cgnshow cgn instance
## tcp-mss-clamping 

tcp-mss-clamping 
命令功能 : 
配置tcp mss clamping功能。配置后可对TCP报文选项字段的Maximum Segment Size(MSS)值进行修改，大于设置值的改成设置值，从而保证后续客户端/服务器不会发送超大报文。 
命令模式 : 
 NAT高级模式  
命令默认权限级别 : 
15 
命令格式 : 
tcp-mss-clamping 
  {disable 
|new-mss-value 
 {auto 
|＜tcp-mss-value 
＞}}
命令参数解释 : 
参数|描述
---|---
disable|关闭tcp mss clamping功能
new-mss-value|开启tcp mss clamping功能并且设置值
auto|根据用户接入接口和软线自动计算MSS值
＜tcp-mss-value＞|配置具体的tcp-mss-clamping值，范围64~9216
缺省 : 
disable 
使用说明 : 
该配置只在高级模式下打开enable开关时生效。如果配置disable开关，则不管配置何值，都不会生效。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#advanced-serviceZXROSNG(config-cgn-zte-adv-srv)#tcp-mss-clamping disableZXROSNG(config-cgn-zte-adv-srv)#
相关命令 : 
show running-config cgnshow cgn instance
## tcp-policy 

tcp-policy 
命令功能 : 
模式跳转命令，进入TCP策略配置模式配置。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
tcp-policy 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#tcp-policy ZXROSNG(config-cgn-zte-domain-tcp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## tcp-state-tracking 

tcp-state-tracking 
命令功能 : 
开启/关闭tcp state tracking功能。开启该功能后，ALG会跟踪TCP SYN、SYN ACK、 FIN/RST报文，并且动态刷新NAT转换条目的老化时间。 
命令模式 : 
 NAT高级模式  
命令默认权限级别 : 
15 
命令格式 : 
tcp-state-tracking 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|开启tcp state tracking功能
disable|关闭tcp state tracking功能
缺省 : 
disable 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#advanced-serviceZXROSNG(config-cgn-zte-adv-srv)#tcp-state-tracking enableZXROSNG(config-cgn-zte-adv-srv)#
相关命令 : 
show running-config cgnshow cgn instance
## timeout unwell-known-port 

timeout unwell-known-port 
命令功能 : 
TCP策略非知名端口转换条目的老化时长配置。 
命令模式 : 
 NAT-TCP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
timeout unwell-known-port 
  {[tcp 
 ＜timeout 
＞],[tcp-syn 
 ＜timeout-syn 
＞],[tcp-fin-rst 
 ＜timeout-fin 
＞],[tcp-fin-wait 
 ＜timeout-fin-wait 
＞]}
no timeout unwell-known-port 
命令参数解释 : 
参数|描述
---|---
＜timeout＞|tcp数据报文映射条目超时时间，可配置范围为<1-7200>s
＜timeout-syn＞|tcp-syn映射条目超时时间，可配置范围为<1-7200>s
＜timeout-fin＞|tcp-fin映射条目超时时间，可配置范围为<1-7200>s
＜timeout-fin-wait＞|tcp-fin-wait映射条目老化时间，可配置范围为<0-7200>s
缺省 : 
timeout unwell-known-port tcp 120 tcp-syn 60 tcp-fin-rst 120 tcp-fin-wait 0 
使用说明 : 
tcp-fin-wait配置tcp非知名端口的tcp半关闭老化时间，当收到单个方向的fin报文时，修改条目的老化时间为半关闭老化时间，该命令可以配置为0，当配置为0时，该命令不生效，即收到单向fin时，老化时间不做修改。 
范例 : 
ZXROSNG(config)#cgnZXROSNG(config-cgn-?)#domain 1 1 type sr ipv4-issuedZXROSNG(config-cgn-?-domain)#tcp-policy ZXROSNG(config-cgn-?-domain-tcp-policy)#timeout unwell-known-port tcp 500ZXROSNG(config-cgn-?-domain-tcp-policy)#ZXROSNG(config-cgn-?-domain-tcp-policy)#timeout unwell-known-port tcp-fin-wait 60 
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## timeout unwell-known-port 

timeout unwell-known-port 
命令功能 : 
UDP策略非知名端口转换条目的老化时长配置。 
命令模式 : 
 NAT-UDP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
timeout unwell-known-port 
  ＜timeout 
＞
no timeout unwell-known-port 
命令参数解释 : 
参数|描述
---|---
＜timeout＞|老化时间，范围1~7200秒
缺省 : 
timeout unwell-known-port 180 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policyZXROSNG(config-cgn-zte-domain-udp-policy)# timeout unwell-known-port 100ZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## timeout well-known-port 

timeout well-known-port 
命令功能 : 
TCP策略知名端口转换条目的老化时长配置。 
命令模式 : 
 NAT-TCP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
timeout well-known-port 
  {[tcp 
 ＜timeout 
＞],[tcp-syn 
 ＜timeout-syn 
＞],[tcp-fin-rst 
 ＜timeout-fin 
＞],[tcp-fin-wait 
 ＜timeout-single-fin 
＞]}
no timeout well-known-port 
命令参数解释 : 
参数|描述
---|---
＜timeout＞|TCP数据报文映射条目老化时间，可配置范围为<1-7200>s
＜timeout-syn＞|tcp-syn映射条目老化时间，可配置范围为<1-7200>s
＜timeout-fin＞|tcp-fin映射条目老化时间，可配置范围为<1-7200>s
＜timeout-single-fin＞|tcp-fin-wait映射条目老化时间，可配置范围为<0-7200>s
缺省 : 
timeout well-known-port  tcp 120 tcp-syn 60 tcp-fin-rst 120 tcp-fin-wait 0 
使用说明 : 
tcp-fin-wait配置tcp知名端口的tcp半关闭老化时间，当收到单个方向的fin报文时，修改条目的老化时间为半关闭老化时间，该命令可以配置为0，当配置为0时，该命令不生效，即收到单向fin时，老化时间不做修改。 
范例 : 
ZXROSNG(config)#cgnZXROSNG(config-cgn-?)#domain 1 1 type sr ipv4-issuedZXROSNG(config-cgn-?-domain)#tcp-policy ZXROSNG(config-cgn-?-domain-tcp-policy)#timeout well-known-port tcp 500ZXROSNG(config-cgn-?-domain-tcp-policy)#ZXROSNG(config-cgn-?-domain-tcp-policy)#timeout well-known-port tcp-fin-wait 60
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## timeout well-known-port 

timeout well-known-port 
命令功能 : 
UDP策略知名端口转换条目的老化时长配置。 
命令模式 : 
 NAT-UDP策略模式  
命令默认权限级别 : 
15 
命令格式 : 
timeout well-known-port 
  ＜timeout 
＞
no timeout well-known-port 
命令参数解释 : 
参数|描述
---|---
＜timeout＞|老化时间，可配置范围1~7200秒
缺省 : 
timeout well-known-port  180 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policyZXROSNG(config-cgn-zte-domain-udp-policy)# timeout well-known-port100ZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## timeout 

timeout 
命令功能 : 
ICMP策略转换条目的老化时长配置。 
命令模式 : 
 NAT-ICMP策略模式  
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
＜timeout＞|老化时间，取值范围1~7200秒
缺省 : 
timeout 60 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#icmp-policyZXROSNG(config-cgn-zte-domain-icmp-policy)#timeout 100ZXROSNG(config-cgn-zte-domain-icmp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## timeout 

timeout 
命令功能 : 
NAT策略转换条目的老化时长配置。 
命令模式 : 
 NAT-NAT策略模式  
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
＜timeout＞|超时时间，取值范围1~7200秒
缺省 : 
timeout 120 
使用说明 : 
no命令恢复默认值。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#nat-policy  ZXROSNG(config-cgn-zte-domain-nat-policy)# timeout 100ZXROSNG(config-cgn-zte-domain-nat-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## translation-logging-fields bras 

translation-logging-fields bras 
命令功能 : 
配置生成BRAS日志的NAT条目字段，默认关闭所有字段 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
translation-logging-fields bras 
  {[inside-port 
],[mapping-mode 
],[filtering-mode 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
]}
no translation-logging-fields bras 
  {[inside-port 
],[mapping-mode 
],[filtering-mode 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
]}
				
命令参数解释 : 
参数|描述
---|---
inside-port|私网源端口号
mapping-mode|映射类型
filtering-mode|过滤模式
inbound-packets|入向报文个数
outbound-packets|出向报文个数
inbound-bytes|入向字节数
outbound-bytes|出向字节数
缺省 : 
无 
使用说明 : 
文本格式日志有效。配置的字段为除了基本日志字段外，需要记录和显示的字段，如不配置，则只显示基本字段。
范例 : 
ZXROSNG(config)#cgn test 1ZXROSNG(config-cgn-test)#logZXROSNG(config-cgn-test-log)#translation-logging-fileds bras filtering-modeZXROSNG(config-cgn-test-log)#
相关命令 : 
show running-config cgnshow cgn instance
## translation-logging-fields ipflow session-create 

translation-logging-fields ipflow session-create 
命令功能 : 
ipflow创建模板中增加start-time可选字段 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
translation-logging-fields ipflow session-create 
 start-time 
no translation-logging-fields ipflow session-create 
 start-time 
命令参数解释 : 
参数|描述
---|---
start-time|在ipflow发送模板中会话创建时间字段
缺省 : 
start-time字段不在日志模板中 
使用说明 : 
配置该命令，表示在ipflow发送创建模板中增加会话创建时间字段；No掉该命令，表示在ipflow发送创建模板中不增加会话创建时间字段，保持原来模板。 
范例 : 
ZXROSNG(config)#cgn 1 1ZXROSNG(config-cgn)#logZXROSNG(config-cgn-log)#translation-logging-fields ipflow session-create ?  start-time  Logging start timeZXROSNG(config-cgn-log)#translation-logging-fields ipflow session-create start-timeZXROSNG(config-cgn-log)#show this!<cgn>    translation-logging-fields ipflow session-create start-time!</cgn>ZXROSNG(config-cgn-log)#
相关命令 : 
show running-config cgn 
## translation-logging-fields ipflow session-delete 

translation-logging-fields ipflow session-delete 
命令功能 : 
Ipflow删除模板中增加cgn-ip, cgn-port, inbound-bytes, inbound-packets, outbound-bytes, outbound-packets, vpn-id, start-time, end-time可选字段 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
translation-logging-fields ipflow session-delete 
  {[cgn-ip 
],[cgn-port 
],[inbound-bytes 
],[inbound-packets 
],[outbound-bytes 
],[outbound-packets 
],[vpn-id 
],[start-time 
],[end-time 
]}
no translation-logging-fields ipflow session-delete 
  {[cgn-ip 
],[cgn-port 
],[inbound-bytes 
],[inbound-packets 
],[outbound-bytes 
],[outbound-packets 
],[vpn-id 
],[start-time 
],[end-time 
]}
				
命令参数解释 : 
参数|描述
---|---
cgn-ip|在ipflow发送删除模板中增加转换公网地址字段
cgn-port|在ipflow发送删除模板中增加转换公网端口字段
inbound-bytes|在ipflow发送删除模板中增加入向字节数字段
inbound-packets|在ipflow发送删除模板中增加入向报文数字段
outbound-bytes|在ipflow发送删除模板中增加出向字节数字段
outbound-packets|在ipflow发送删除模板中增加出向报文数字段
vpn-id|在ipflow发送删除模板中增加公网VPN ID字段
start-time|在ipflow发送删除模板中增加会话创建时间字段
end-time|在ipflow发送删除模板中增加会话删除时间字段
缺省 : 
cgn-ip, cgn-port, inbound-bytes, inbound-packets, outbound-bytes, outbound-packets, vpn-id, start-time, end-time可选字段不在日志模板中。 
使用说明 : 
配置该命令，表示在ipflow发送创建模板中增加会话删除的cgn-ip, cgn-port, inbound-bytes, inbound-packets, outbound-bytes, outbound-packets, vpn-id, start-time, end-time可选字段；No掉该命令，表示在ipflow发送创建模板中没有会话删除的cgn-ip, cgn-port, inbound-bytes, inbound-packets, outbound-bytes, outbound-packets, vpn-id, start-time, end-time可选字段，保持原来模板。 
范例 : 
ZXROSNG(config)#cgn 1 1ZXROSNG(config-cgn)#logZXROSNG(config-cgn-log)# translation-logging-fields ipflow session-delete cgn-ip cgn-port inbound-bytes inbound-packets outbound-bytes outbound-packets vpn-id start-time end-timeZXROSNG(config-cgn-log)# show this!<cgn>    translation-logging-fields ipflow session-delete cgn-ip cgn-port inbound-bytes inbound-packets outbound-bytes outbound-packets vpn-id start-time end-time!</cgn>ZXROSNG(config-cgn-log)# no translation-logging-fields ipflow session-delete vpn-id start-time end-timeZXROSNG(config-cgn-log)# show this!<cgn>    translation-logging-fields ipflow session-delete cgn-ip cgn-port inbound-bytes inbound-packets outbound-bytes outbound-packets!</cgn>ZXROSNG(config-cgn-log)#
相关命令 : 
show running-config cgn 
## translation-logging-fields sr 

translation-logging-fields sr 
命令功能 : 
配置生成SR日志的NAT条目字段，默认关闭所有字段。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
translation-logging-fields sr 
  {[inside-port 
],[mapping-mode 
],[filtering-mode 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
]}
no translation-logging-fields sr 
  {[inside-port 
],[mapping-mode 
],[filtering-mode 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
]}
				
命令参数解释 : 
参数|描述
---|---
inside-port|私网源端口号
mapping-mode|映射类型
filtering-mode|过滤模式
inbound-packets|入向报文个数
outbound-packets|出向报文个数
inbound-bytes|入向字节个数
outbound-bytes|出向字节个数
缺省 : 
无 
使用说明 : 
仅对文本格式日志有效。配置的字段为除了基本日志字段外，需要记录和显示的字段，如不配置，则只显示基本字段。
范例 : 
ZXROSNG(config)#cgn test 1ZXROSNG(config-cgn-test)#logZXROSNG(config-cgn-test-log)#translation-logging-fileds sr filtering-modeZXROSNG(config-cgn-test-log)#
相关命令 : 
show running-config cgnshow cgn instance
## translation-logging-fields standalone 

translation-logging-fields standalone 
命令功能 : 
配置生成STANDALONE日志的NAT条目字段，默认关闭所有字段。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
translation-logging-fields standalone 
  {[cpe-ipv6-address 
],[inside-port 
],[mapping-mode 
],[filtering-mode 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
]}
no translation-logging-fields standalone 
  {[cpe-ipv6-address 
],[inside-port 
],[mapping-mode 
],[filtering-mode 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
]}
				
命令参数解释 : 
参数|描述
---|---
cpe-ipv6-address|CPE的Ipv6地址
inside-port|私网源端口
mapping-mode|映射模式
filtering-mode|过滤模式
inbound-packets|入向报文个数
outbound-packets|出向报文格式
inbound-bytes|入向字节数
outbound-bytes|出向字节数
缺省 : 
无 
使用说明 : 
文本格式日志有效。配置的字段为除了基本日志字段外，需要记录和显示的字段，如不配置，则只显示基本字段。
范例 : 
ZXROSNG(config)#cgn test 1ZXROSNG(config-cgn-test)#logZXROSNG(config-cgn-test-log)#translation-logging-fields standalone cpe-ipv6-address
相关命令 : 
show running-config cgnshow cgn instance
## translation-logging-fields syslog 

translation-logging-fields syslog 
命令功能 : 
配置生成SYSLOG日志的NAT条目字段，默认关闭所有字段。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
translation-logging-fields syslog 
  {[vrf-name 
],[destination-ip 
],[destination-port 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
],[cgn-ip 
]}
no translation-logging-fields syslog 
  {[vrf-name 
],[destination-ip 
],[destination-port 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
],[cgn-ip 
]}
				
命令参数解释 : 
参数|描述
---|---
vrf-name|VRF名称
destination-ip|目的地址
destination-port|目的端口
inbound-packets|入向包数
outbound-packets|出向包数
inbound-bytes|入向字节数
outbound-bytes|出向字节数
cgn-ip|管理口地址
缺省 : 
无 
使用说明 : 
syslog日志有效。配置的字段为除了基本日志字段外，需要记录和显示的字段，如不配置，则只显示基本字段。相关命令log-style，cgn-ip字段只有在配置log-style style2的时候，才会生效；其他的字段是在log-style style1的时候生效。无互斥关系。 
范例 : 
ZXROSNG(config)#cgn 1 1ZXROSNG(config-cgn)#logZXROSNG(config-cgn-log)#log-style style2ZXROSNG(config-cgn-log)#destination syslogZXROSNG(config-cgn-log)#translation-logging-fields syslog cgn-ip
相关命令 : 
show running-config cgnshow cgn instance
## translation-logging-fields xgw 

translation-logging-fields xgw 
命令功能 : 
配置生成XGW日志的NAT条目字段，默认关闭所有字段。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
translation-logging-fields xgw 
  {[inside-port 
],[mapping-mode 
],[filtering-mode 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
]}
no translation-logging-fields xgw 
  {[inside-port 
],[mapping-mode 
],[filtering-mode 
],[inbound-packets 
],[outbound-packets 
],[inbound-bytes 
],[outbound-bytes 
]}
				
命令参数解释 : 
参数|描述
---|---
inside-port|私网源端口
mapping-mode|映射模式
filtering-mode|过滤模式
inbound-packets|入向报文数
outbound-packets|出向报文数
inbound-bytes|入向字节数
outbound-bytes|出向字节数
缺省 : 
无 
使用说明 : 
文本格式日志有效。配置的字段为除了基本日志字段外，需要记录和显示的字段，如不配置，则只显示基本字段。
范例 : 
ZXROSNG(config)#cgn test 1ZXROSNG(config-cgn-test)#logZXROSNG(config-cgn-test-log)#translation-logging-fields xgw filtering-mode
相关命令 : 
show running-config cgnshow cgn instance
## udp-policy 

udp-policy 
命令功能 : 
模式跳转命令，进入UDP策略配置模式配置。 
命令模式 : 
 NAT-DOMAIN模式  
命令默认权限级别 : 
15 
命令格式 : 
udp-policy 
 
命令参数解释 : 
					无
				 
缺省 : 
无 
使用说明 : 
无 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn-zte)#domain test 1 type sr ipv4-issuedZXROSNG(config-cgn-zte-domain)#udp-policy ZXROSNG(config-cgn-zte-domain-udp-policy)#
相关命令 : 
show running-config cgnshow cgn instance show cgn domain
## url-log 

url-log 
命令功能 : 
配置打开或者关闭URL日志功能；如果打开URL日志功能时，含有主机和网页信息的报文会通过syslog发送日志，关闭不发送。 
命令模式 : 
 NAT日志模式  
命令默认权限级别 : 
15 
命令格式 : 
url-log 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开URL log功能
disable|关闭URL log功能
缺省 : 
默认为disable。 
使用说明 : 
该命令跟log模式下的enable和disable命令无关，可以单独开，单独生效。 
范例 : 
ZXROSNG(config)#cgn zte 1ZXROSNG(config-cgn)#log ZXROSNG(config-cgn-log)#url-log enable ZXROSNG(config-cgn-log)#rul-log disable 
相关命令 : 
show running-config cgn 
## warning 

warning 
命令功能 : 
该命令用于打开关闭告警开关 
命令模式 : 
 NAT告警模式  
命令默认权限级别 : 
15 
命令格式 : 
warning 
  {enable 
|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|打开告警开关
disable|关闭告警开关
缺省 : 
enable 
使用说明 : 
打开后告警生效 
范例 : 
ZXROSNG(config-cgn-alarm)#warning enable ZXROSNG(config-cgn-alarm)#
ZXROSNG(config-cgn-alarm)#warning disable ZXROSNG(config-cgn-alarm)#
ZXROSNG(config-cgn-alarm)#show running-config cgn!<cgn>cgn  alarm    warning disable  $$!</cgn>ZXROSNG(config-cgn-alarm)#
相关命令 : 
show running-config cgn 显示ZXROSNG(config-cgn-alarm)#show running-config cgn!<cgn>cgn  alarm    warning disable  $$!</cgn>ZXROSNG(config-cgn-alarm)#
## well-known-port-forbidden 

well-known-port-forbidden 
命令功能 : 
地址池中控制知名端口是否禁止的开关。 
命令模式 : 
 NAT-PAT地址池模式  
命令默认权限级别 : 
15 
命令格式 : 
well-known-port-forbidden 
  {enable 
 [＜start-port 
＞]|disable 
}
命令参数解释 : 
参数|描述
---|---
enable|知名端口禁止功能使能，该地址池不再分配ALG协议使用的知名端口
＜start-port＞|使能知名端口禁止后，允许使用的起始端口号，取值范围<64-8192>,必须是64的整数倍，默认对范围不加限制，仅限制离散端口
disable|知名端口禁止功能去使能，该地址池可以分配1-65535范围内的任意端口，默认disable
缺省 : 
知名端口禁止功能去使能 
使用说明 : 
配置了section后，该命令不能修改;配置了well-known-port-forbidden enable后只限制离散端口：FTP(21), DNS(53), HTTP(80), RTSP(554), H323(1718, 1719, 1720), PPTP(1723), SIP(5060);配置了well-known-port-forbidden enable[port] 后会同时限制上述离散端口和port之前的一段端口范围;配置了well-known-port-forbidden disable后所有端口可用
范例 : 
ZXROSNG(config-cgn-patpool)# well-known-port-forbidden ?enable                 Enable well known port forbiddendisable                  Disable well known port forbidden
相关命令 : 
show cgn instance summaryshow running-config cgn
