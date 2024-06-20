# ATM接口配置命令 
## cell-transport 


cell-transport 




命令功能 :

设置接口的信元传输模式 






命令模式 :

 ATM接口模式  






命令默认权限级别 :

15 






命令格式 :



cell-transport 
 transparent 


no cell-transport 
 transparent 








命令参数解释 :



参数|描述
---|---
transparent|信元透传模式








缺省 :

无 






使用说明 :

(1)    物理接口配置cell-transport transparent。(2)    cell-transport 传输模式不允许修改，只能删除再重新配置。(3)    当接口绑定L2VPN后，不能配置cell-transport，也不能删除cell-transport。(4)    接口下若存在终结模式的PVC，则不能再配置cell-transport，反之亦然。





范例 :

配置物理口信元传输模式：XR10(config)#interface atm155-0/1/2/1ZXROSNG(config-if-atm155-0/1/2/1)#cell-transport  transparent





相关命令 :

1:1、N:1 PVC信元传输模式下的pvc1:1、N:1 PVP信元传输模式下的vpi



## cell-transport 


cell-transport 




命令功能 :

设置接口的信元传输模式 






命令模式 :

 ATM子接口模式  






命令默认权限级别 :

15 






命令格式 :


cell-transport 
  {vcc 
|vcc-group 
|vpc 
|vpc-group 
}
no cell-transport 
  {vcc 
|vcc-group 
|vpc 
|vpc-group 
}
				






命令参数解释 :



参数|描述
---|---
vcc|1:1  PVC传输模式
vcc-group|N:1  PVC传输模式
vpc|1:1  PVP传输模式
vpc-group|N:1  PVP传输模式








缺省 :

无 






使用说明 :

(1)    子接口配置cell-transport  vcc、vpc、vcc-group、vpc-group。(2)    cell-transport 传输模式不允许修改，只能删除再重新配置。(3)    当接口绑定L2VPN后，不能配置cell-transport，也不能删除cell-transport。(4)    接口下若存在终结模式的PVC，则不能再配置cell-transport，反之亦然。





范例 :

配置子接口的信元传输模式：ZXROSNG(config)#interface atm155-0/1/2/1.1ZXROSNG(config-if-atm155-0/1/2/1.1)#cell-transport  vcc ZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc)# ZXROSNG(config)#interface atm155-0/1/2/1.2ZXROSNG(config-if-atm155-0/1/2/1.2)#cell-transport  vcc-group ZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vcc)#ZXROSNG(config)#interface atm155-0/1/2/1.3ZXROSNG(config-if-atm155-0/1/2/1.3)#cell-transport  vpc ZXROSNG(config-if-atm155-0/1/2/1.3-atm-cell-vpc)#ZXROSNG(config)#interface atm155-0/1/2/1.4ZXROSNG(config-if-atm155-0/1/2/1.4)#cell-transport  vpc-group ZXROSNG(config-if-atm155-0/1/2/1.4-atm-cell-vpc)#





相关命令 :

1:1、N:1 PVC信元传输模式下的pvc1:1、N:1 PVP信元传输模式下的vpi



## debug atm all 


debug atm all 




命令功能 :

atm所有debug 开关开启或关闭 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug atm all 
 

no debug atm all 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

debug atm all 






相关命令 :

show debug atm  




## debug atm oam packet 


debug atm oam packet 




命令功能 :

ATM模块的debug 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug atm oam packet 
  [interface 
 ＜interface-name 
＞ [＜pvcno. 
＞ ＜vpi-value 
＞ ＜vci-value 
＞]]

no debug atm oam packet 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|指定的接口名称
＜pvcno.＞|PvcNum值，范围：1~4000
＜vpi-value＞|VPI值，范围0~255
＜vci-value＞|VCI值，范围32~65535








缺省 :

无 






使用说明 :

1、所有atm接口的debug2、指定接口的debug3、指定接口 + 指定PVC的debug





范例 :

ZXROSNG#show debug atm ATM:  ATM OAM packets debugging is on






相关命令 :

debug atm oam packetdebug atm all




## encapsulation 


encapsulation 




命令功能 :

配置PVC封装模式 






命令模式 :

 ATM-VC子接口模式,ATM-VC模式  






命令默认权限级别 :

ATM-VC子接口模式:15,ATM-VC模式:15 






命令格式 :



encapsulation 
  {aal5snap 
|aal5nlpid 
}

no encapsulation 








命令参数解释 :



参数|描述
---|---
aal5snap|ISO封装格式
aal5nlpid|SNAP封装格式








缺省 :

aal5snap 






使用说明 :

创建PVC后进入PVC配置模式进行配置 






范例 :

ZXROSNG(config-if-atm-vc)# encapsulation aal5nlpidZXROSNG(config-if-atm-vc)# no encapsulation 






相关命令 :

show atm configuration 




## map-to 


map-to 




命令功能 :

PVC下配置ULEI桥接 






命令模式 :

 ATM-VC子接口模式,ATM-VC模式  






命令默认权限级别 :

ATM-VC子接口模式:15,ATM-VC模式:15 






命令格式 :



map-to 
  ＜interface-name 
＞ [user-access 
]

no map-to 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|ulei接口名称
user-access|标识用户侧接入








缺省 :

无 






使用说明 :

PVC下配置ulei桥接 






范例 :

ZXROSNG(config-if)#pvc 20 30 40ZXROSNG(config-if-atm-vc)#map-to ulei-0/1/1/1ZXROSNG(config-if-atm-vc)#no map-toZXROSNG(config-if)#pvc 30 40 50ZXROSNG(config-if-atm-vc)#map-to ulei-0/1/1/2ZXROSNG(config-if-atm-vc)#map-to ulei-0/1/1/2 user-accessZXROSNG(config-if-atm-vc)#no map-to





相关命令 :

show atm configuration  




## oam-pvc 


oam-pvc 




命令功能 :

配置PVC的OAM功能 






命令模式 :

 ATM-VC子接口模式,ATM-VC模式  






命令默认权限级别 :

ATM-VC子接口模式:15,ATM-VC模式:15 






命令格式 :



oam-pvc 
 manage 
 [＜oam-loopback-frequency 
＞]

no oam-pvc 
 manage 








命令参数解释 :



参数|描述
---|---
manage|命令关键字
＜oam-loopback-frequency＞|oam f5管理信元的发送频率，单位：秒，范围1~600，缺省为5秒








缺省 :

不开启OAM功能 






使用说明 :

no oam-pvc manage时，禁止该功能, frequency恢复为5s 






范例 :

ZXROSNG(config-if-atm-vc)# oam-pvc manage 10ZXROSNG(config-if-atm-vc)# no oam-pvcZXROSNG(config-subif-atm-vc)# oam-pvc manage10ZXROSNG(config-subif-atm-vc)# no oam-pvc manage 






相关命令 :

show atm configuration  




## oam-retry 


oam-retry 




命令功能 :

配置PVC的重试次数 






命令模式 :

 ATM-VC子接口模式,ATM-VC模式  






命令默认权限级别 :

ATM-VC子接口模式:15,ATM-VC模式:15 






命令格式 :



oam-retry 
  ＜oam-retry-count 
＞ ＜oam-retry-count 
＞ ＜oam-retry-polling-frequency 
＞

no oam-retry 








命令参数解释 :



参数|描述
---|---
＜oam-retry-count＞|指定PVC连接从down状态转变为up状态前必须收到的端到端f5 oam回送信元的个数，范围1~600，缺省为3
＜oam-retry-count＞|指定PVC连接从down状态转变为up状态前必须收到的端到端f5 oam回送信元的个数，范围1~600，缺省为3
＜oam-retry-polling-frequency＞|指定一个PVC连接处于开状态且在oam-pvc命令所指定的frequency，单位：秒，之后未收到回送信元响应后管理信元的发送频率，范围1~1000，缺省为1秒








缺省 :

up-count：3sdown-count：5sretry-frequency：1s






使用说明 :

无 






范例 :

ZXROSNG(config-if-atm-vc)# oam retry 10 10 1ZXROSNG(config-if-atm-vc)# no oam retryZXROSNG(config-subif-atm-vc)# oam retry 10 10 1ZXROSNG(config-subif-atm-vc)# no oam retry






相关命令 :

无 




## protocol ip 


protocol ip 




命令功能 :

配置MAP，即IP和PVC之间的映射关系 






命令模式 :

 ATM-VC子接口模式,ATM-VC模式  






命令默认权限级别 :

ATM-VC子接口模式:15,ATM-VC模式:15 






命令格式 :


protocol ip 
  ＜ip-address 
＞
no protocol ip 
  [＜ip-address 
＞]
				






命令参数解释 :



参数|描述
---|---
＜ip-address＞|映射的IP地址








缺省 :

1、    下一跳IP地址和本端PVC之间的映射关系2、    No命令时如果不指定IP，则删除此PVC下所有的map条目






使用说明 :

ZXROSNG(config-if-atm-vc)# protocol ip 10.1.1.1ZXROSNG(config-if-atm-vc)# no tocol ipZXROSNG(config-subif-atm-vc)# protocol ip 11.1.1.1ZXROSNG(config-subif-atm-vc)# no protocol ip






范例 :

show atm map 






相关命令 :

无 




## pvc 


pvc 




命令功能 :

配置接口PVC信息 






命令模式 :

 ATM子接口模式,ATM接口模式,atm_dslgroup接口模式,dsl子接口模式,dsl接口模式  






命令默认权限级别 :

dsl子接口模式:15,ATM接口模式:15,ATM子接口模式:15,atm_dslgroup接口模式:15,dsl接口模式:15 






命令格式 :


pvc 
  ＜pvcno. 
＞ ＜vpi-value 
＞ ＜vci-value 
＞
no pvc 
  [＜pvcno. 
＞ ＜vpi-value 
＞ ＜vci-value 
＞]
				






命令参数解释 :



参数|描述
---|---
＜pvcno.＞|PvcNum值，范围：1~4000
＜vpi-value＞|VPI值，范围0~255
＜vci-value＞|VCI值，范围32~65535








缺省 :

无 






使用说明 :

1、    进入ATM接口，或ATM子接口，配置VPI,VCI，进入PVC配置模式2、    No命令时，如果不指定pvc，则no掉此接口下所有的pvc






范例 :

ZXROSNG(config)#interface atm155-0/1/1/1ZXROSNG(config-if)#pvc 20 30 40ZXROSNG(config-if)#no pvc 20 30 40 






相关命令 :

show atm pvc  




## pvc 


pvc 




命令功能 :

设置1:1 PVC信元传输模式的PVC参数。 






命令模式 :

 PVC 1:1仿真模式  






命令默认权限级别 :

15 






命令格式 :



pvc 
  ＜pvcno. 
＞ vcc 
 ＜vpi-value 
＞ ＜vci-value 
＞

no pvc 








命令参数解释 :



参数|描述
---|---
＜pvcno.＞|PVCNo.值，范围：1~4000
＜vpi-value＞|VPI值，范围0~255
＜vci-value＞|VCI值，范围0~65535








缺省 :

无 






使用说明 :

(1)    设置子接口的信元传输模式为cell-transport vcc后，再配置该信元传输模式的PVC参数。(2)     一个VCC下只能包含一条PVC。





范例 :

子接口的信元传输模式为cell-transport vcc时，设置相关的PVC参数：ZXROSNG(config)#interface atm155-0/1/2/1.1ZXROSNG(config-if-atm155-0/1/2/1.1)#cell-transport vccZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc)#pvc 20 vcc 30 40 ZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc-params)# 





相关命令 :

show atm cell-transport 




## pvc 


pvc 




命令功能 :

设置N:1 PVC信元传输模式的PVC参数。 






命令模式 :

 PVC N:1仿真模式  






命令默认权限级别 :

15 






命令格式 :


pvc 
  ＜pvcno. 
＞ vcc 
 ＜vpi-value 
＞ ＜vci-value 
＞
no pvc 
  [＜pvcno. 
＞ vcc 
 ＜vpi-value 
＞ ＜vci-value 
＞]
				






命令参数解释 :



参数|描述
---|---
＜pvcno.＞|PVCNo.值，范围：1~4000
＜vpi-value＞|VPI值，范围0~255
＜vci-value＞|VCI值，范围0~65535








缺省 :

无 






使用说明 :

(1)    设置子接口的信元传输模式为cell-transport vcc-group后，再配置该信元传输模式的PVC参数。(2)    一个VCC-GROUP下可以包含多条PVC。





范例 :

子接口的信元传输模式为cell-transport vcc-group时，设置相关的PVC参数：ZXROSNG(config)#interface atm155-0/1/2/1.2ZXROSNG(config-if-atm155-0/1/2/1.2)#cell-transport vcc-groupZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vcc)#pvc 30 vcc 40 50ZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vcc-params)# 





相关命令 :

show atm cell-transport 




## pvc-to-qinq 


pvc-to-qinq 




命令功能 :

配置PVC到QINQ的映射 






命令模式 :

 ATM-VC子接口模式,ATM-VC模式  






命令默认权限级别 :

ATM-VC模式:15,ATM-VC子接口模式:15 






命令格式 :



pvc-to-qinq 
  ＜external-vlan-id 
＞ ＜internal-vlan-id 
＞

no pvc-to-qinq 








命令参数解释 :



参数|描述
---|---
＜external-vlan-id＞|PVC所映射的外层vlan值
＜internal-vlan-id＞|PVC所映射的内层vlan值








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-if-atm-vc)# pvc-to-qinq  10 20ZXROSNG(config-if-atm-vc)# no pvc-to-qinq






相关命令 :

show atm configuration  




## pvc-to-vlan 


pvc-to-vlan 




命令功能 :

配置PVC到VLAN的映射 






命令模式 :

 ATM-VC子接口模式,ATM-VC模式  






命令默认权限级别 :

ATM-VC子接口模式:15,ATM-VC模式:15 






命令格式 :



pvc-to-vlan 
  ＜vlan-id 
＞

no pvc-to-vlan 








命令参数解释 :



参数|描述
---|---
＜vlan-id＞|PVC所映射的vlan值








缺省 :

无 






使用说明 :

无 






范例 :

XR10(config-if-atm-vc)# pvc-to-vlan  10ZXROSNG(config-if-atm-vc)# no pvc-to-vlan






相关命令 :

show atm configuration 




## qos 


qos 




命令功能 :

配置QoS带宽 






命令模式 :

 ATM-VC模式  






命令默认权限级别 :

15 






命令格式 :



qos 
  {cbr 
 ＜cbr-value 
＞|ubr 
 ＜ubr-value 
＞ [priority 
 ＜priority-value 
＞]|vbr-nrt 
 pcr 
 ＜ubr-value 
＞ scr 
 ＜ubr-value 
＞ mbs 
 ＜ubr-value 
＞|vbr-rt 
 pcr 
 ＜ubr-value 
＞ scr 
 ＜ubr-value 
＞ mbs 
 ＜ubr-value 
＞}

no qos 








命令参数解释 :



参数|描述
---|---
cbr|配置cbr带宽标志
＜cbr-value＞|cbr 带宽值
ubr|配置ubr带宽标志
＜ubr-value＞|ubr 带宽值
＜priority-value＞|优先级
vbr-nrt|配置vbr-nrt带宽标志
＜ubr-value＞|ubr 带宽值
＜ubr-value＞|ubr 带宽值
＜ubr-value＞|ubr 带宽值
vbr-rt|配置vbr-rt带宽标志
＜ubr-value＞|ubr 带宽值
＜ubr-value＞|ubr 带宽值
＜ubr-value＞|ubr 带宽值








缺省 :

类型：ubr带宽：2000优先级：类型为ubr是才有用，默认0





使用说明 :

无 






范例 :

ZXROSNG(config-if-atm-vc)# qos ubr 1000 10 






相关命令 :

show atm configuration  




## qos 


qos 




命令功能 :

配置QoS带宽 






命令模式 :

 ATM-VC子接口模式  






命令默认权限级别 :

15 






命令格式 :



qos 
  {cbr 
 ＜cbr-value 
＞|ubr 
 ＜ubr-value 
＞ [priority 
 ＜priority-value 
＞]}

no qos 








命令参数解释 :



参数|描述
---|---
cbr|带宽类型为CBR
＜cbr-value＞|带宽值
ubr|带宽类型为UBR
＜ubr-value＞|带宽值
＜priority-value＞|优先级








缺省 :

类型：ubr带宽：2000Kbps优先级：类型为ubr是才有用，默认0





使用说明 :

无 






范例 :

ZXROSNG(config-if-atm-vc)# qos ubr 1000 10 






相关命令 :

pvc <pvc_number> <vpi_value> < vci_value> 




## qos 


qos 




命令功能 :

配置QoS带宽 






命令模式 :

 PVC 1:1仿真参数模式,PVC N:1仿真参数模式,PVP 1:1仿真参数模式,PVP N:1仿真参数模式  






命令默认权限级别 :

PVC 1:1仿真参数模式:15,PVC N:1仿真参数模式:15,PVP 1:1仿真参数模式:15,PVP N:1仿真参数模式:15 






命令格式 :



qos 
  {cbr 
 ＜cbr-value 
＞|ubr 
 ＜ubr-value 
＞ [priority 
 ＜priority-value 
＞]}

no qos 








命令参数解释 :



参数|描述
---|---
cbr|带宽类型为CBR
＜cbr-value＞|带宽值
ubr|带宽类型为UBR
＜ubr-value＞|带宽值
＜priority-value＞|优先级








缺省 :

类型：ubr带宽：2000Kbps优先级：类型为ubr是才有用，默认0






使用说明 :

无 






范例 :

ZXROSNG(config)#interface atm155-0/1/2/1.1ZXROSNG(config-if-atm155-0/1/2/1.1)#cell-transport vccZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc)#pvc 20 vcc 30 40ZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc-params)#qos ubr 1000 10






相关命令 :

无 




## remote-vcc 


remote-vcc 




命令功能 :

设置1:1 PVC信元传输模式、N:1 PVC信元传输模式下的PVC翻译。 






命令模式 :

 PVC 1:1仿真参数模式,PVC N:1仿真参数模式  






命令默认权限级别 :

PVC 1:1仿真参数模式:15,PVC N:1仿真参数模式:15 






命令格式 :



remote-vcc 
  ＜vpi-value 
＞ ＜vci-value 
＞

no remote-vcc 








命令参数解释 :



参数|描述
---|---
＜vpi-value＞|远端翻译VPI值，范围0~255
＜vci-value＞|远端翻译VCI值，范围0~65535








缺省 :

无 






使用说明 :

无 






范例 :

设置1:1 PVC信元传输模式下的PVC翻译ZXROSNG(config)#interface atm155-0/1/2/1.1ZXROSNG(config-if-atm155-0/1/2/1.1)#cell-transport vccZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc)#pvc 20 vcc 30 40ZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc-params)#remote-vcc 50 60设置N:1 PVC信元传输模式下的PVC翻译ZXROSNG(config)#interface atm155-0/1/2/1.2ZXROSNG(config-if-atm155-0/1/2/1.2)#cell-transport vcc-groupZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vcc)#pvc 40 vcc 50 60ZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vcc-params)#remote-vcc 70 80






相关命令 :

show atm cell-transport 




## remote-vpi 


remote-vpi 




命令功能 :

设置1:1 PVP信元传输模式、N:1 PVP信元传输模式下的PVP翻译。 






命令模式 :

 PVP 1:1仿真参数模式,PVP N:1仿真参数模式  






命令默认权限级别 :

PVP 1:1仿真参数模式:15,PVP N:1仿真参数模式:15 






命令格式 :



remote-vpi 
  ＜vpi-value 
＞

no remote-vpi 








命令参数解释 :



参数|描述
---|---
＜vpi-value＞|远端翻译VPI值，范围0~255








缺省 :

无 






使用说明 :

无 






范例 :

设置1:1 PVP信元传输模式下的PVP翻译ZXROSNG(config)#interface atm155-0/1/2/1.1ZXROSNG(config-if-atm155-0/1/2/1.1)#cell-transport vpcZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc)#vpi 60ZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vcc-params)#remote-vpi 70设置N:1 PVP信元传输模式下的PVP翻译ZXROSNG(config)#interface atm155-0/1/2/1.2ZXROSNG(config-if-atm155-0/1/2/1.2)#cell-transport vpc-groupZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vcc)#vpi 90  ZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vcc-params)#remote-vpi 100






相关命令 :

show atm cell-transport 




## show atm cell-transport 


show atm cell-transport 




命令功能 :

显示配置的信元传输模式PVC/PVP数据 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show atm cell-transport 
  {vcc 
|vcc-group 
|vpc 
|vpc-group 
} [interface 
 ＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
vcc|1:1  PVC传输模式
vcc-group|N:1  PVC传输模式
vpc|1:1  PVP传输模式
vpc-group|N:1  PVP传输模式
＜interface-name＞|接口名字








缺省 :

无 






使用说明 :

根据输入的信元传输模式，查看该模式下配置的PVC（或PVP）数据，接口名是可选的。 






范例 :

查看1:1 PVP 传输模式下的PVP数据：ZXROSNG(config)#show atm cell-transport vpcInterface                        VPI    REMOTE-VPIatm155-0/1/2/1.1                  8      8  查看1:1 PVC 传输模式下的PVC数据：ZXROSNG(config)#show atm cell-transport vccInterface          PvcNo.   VPI    VCI    REMOTE-VPI    REMOTE-VCIatm155-0/1/2/1.2    20      30     40      50               60





相关命令 :

1:1、N:1 PVC信元传输模式下的pvc1:1、N:1 PVP信元传输模式下的vpi



## show atm configuration 


show atm configuration 




命令功能 :

显示ATM配置信息（内存中的信息） 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show atm configuration 
  [interface 
 ＜interface-name 
＞ [＜pvcno. 
＞ ＜vpi-value 
＞ ＜vci-value 
＞] ]







命令参数解释 :



参数|描述
---|---
＜interface-name＞|指定的接口名称
＜pvcno.＞|PvcNum值，范围：1~4000
＜vpi-value＞|VPI值，范围0~255
＜vci-value＞|VCI值，范围32~65535








缺省 :

无 






使用说明 :

1、显示 所有atm接口的ATM配置2、显示 指定接口的ATM配置





范例 :

ZXROSNG(config-if-atm-vc)#show atm configuration interface atm155-0/1/1/1  pvc 20 30 40    encapsulation aal5snap    oam-pvc manage 10    oam-retry 10 20 30    qos ubr 2000 priority 0






相关命令 :

无 




## show atm count 


show atm count 




命令功能 :

整机pvc/map数目查看，可具体到单个子卡上已配置的pvc/map数量 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show atm count 
  {pvc 
|map 
} 







命令参数解释 :



参数|描述
---|---
pvc|整机上以及各子卡上pvc计数
map|整机上以及各子卡上map计数








缺省 :

无 






使用说明 :

配置pvc和map，使用该命令显示整机和各子卡上的pvc/map数量 






范例 :

显示整机和各子卡上的pvc/map数量：ZXROSNG#show atm count pvcTotal PVC count: 4The maximum PVC count on a subcard: 3900SHELF-ID     SLOT-ID     SUBSLOT-ID     PVC-COUNT-------------------------------------------------0            1           2              4    ZXROSNG#show atm count mapTotal map count: 2The maximum map count on a subcard: 3900SHELF-ID     SLOT-ID     SUBSLOT-ID     MAP-COUNT-------------------------------------------------0            1           2              2    





相关命令 :

无 




## show atm map 


show atm map 




命令功能 :

显示MAP信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show atm map 
  [interface 
 ＜if-name 
＞ [＜pvcno. 
＞ ＜vpi-value 
＞ ＜vci-value 
＞] [＜ip-address 
＞]] 







命令参数解释 :



参数|描述
---|---
＜if-name＞|指定的接口名称
＜pvcno.＞|PvcNum值，范围：1~4000
＜vpi-value＞|VPI值，范围0~255
＜vci-value＞|VCI值，范围32~65535
＜ip-address＞|IP地址








缺省 :

无 






使用说明 :

1、    显示 所有map2、    显示 指定接口下的所有map3、    显示 指定接口+指定PVC4、    显示 指定接口+指定IP





范例 :

ZXROSNG(config-if-atm-vc)#show atm map Interface                        IPv4             PvcNo.   VPI    VCI    atm155-0/1/1/1                   1.1.1.1          20       30     40   ZXROSNG#show atm map interface atm155-0/1/1/1 Interface                        IPv4             PvcNo.   VPI    VCI    atm155-0/1/1/1                   1.1.1.1          20       30     40    





相关命令 :

protocol ip 




## show atm pvc 


show atm pvc 




命令功能 :

显示PVC信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show atm pvc 
  [{＜pvcno. 
＞ ＜vpi-value 
＞ ＜vci-value 
＞|interface 
 ＜interface-name 
＞ [＜pvcno. 
＞ ＜vpi-value 
＞ ＜vci-value 
＞]}] 







命令参数解释 :



参数|描述
---|---
＜pvcno.＞|PvcNum值，范围：1~4000
＜vpi-value＞|VPI值，范围0~255
＜vci-value＞|VCI值，范围32~65535
＜interface-name＞|指定的接口名称
＜pvcno.＞|PvcNum值，范围：1~4000
＜vpi-value＞|VPI值，范围0~255
＜vci-value＞|VCI值，范围32~65535








缺省 :

无 






使用说明 :

1、    显示 所有map2、    显示 指定接口下的所有map3、    显示 指定接口+指定PVC4、    显示 指定接口+指定IP 






范例 :

ZXROSNG#show atm pvc Interface                      PvcNo.   VPI    VCI    Encps   Statusatm155-0/1/1/1                 20       30     40     SNAP    INCTIVE 






相关命令 :

无 




## show debug atm 


show debug atm 




命令功能 :

显示atm 开启debug功能情况 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug atm 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

显示atm 是否开启debug功能 






范例 :

ZXROSNG#show debug atm ATM:  ATM OAM packets debugging is on






相关命令 :

无 




## vpi 


vpi 




命令功能 :

设置1:1 PVP信元传输模式的PVP参数。 






命令模式 :

 PVP 1:1仿真模式  






命令默认权限级别 :

15 






命令格式 :



vpi 
  ＜vpi 
＞

no vpi 








命令参数解释 :



参数|描述
---|---
＜vpi＞|VPI值，范围0~255








缺省 :

无 






使用说明 :

(1)    子接口的信元传输模式为cell-transport vpc后，再配置该传输模式下PVP相关的参数。(2)    一个VPC下只能包含一条PVP。





范例 :

子接口的信元传输模式为cell-transport vpc时，设置相关的PVP参数：ZXROSNG(config)#interface atm155-0/1/2/1.1ZXROSNG(config-if-atm155-0/1/2/1.1)#cell-transport vpcZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vpc)#vpi 40ZXROSNG(config-if-atm155-0/1/2/1.1-atm-cell-vpc-prams)# 





相关命令 :

show atm cell-transport 




## vpi 


vpi 




命令功能 :

设置N:1 PVP信元传输模式的PVP参数。 






命令模式 :

 PVP N:1仿真模式  






命令默认权限级别 :

15 






命令格式 :


vpi 
  ＜vpi 
＞
no vpi 
  [＜vpi 
＞]
				






命令参数解释 :



参数|描述
---|---
＜vpi＞|VPI值，范围0~255








缺省 :

无 






使用说明 :

(1)    子接口的信元传输模式为cell-transport vpc-group后，再配置该传输模式下PVP相关的参数。(2)    一个VPC-GROUP下可以包含多条PVP。





范例 :

子接口的信元传输模式为cell-transport vpc-group时，设置相关的PVP参数：ZXROSNG(config)#interface atm155-0/1/2/1.2ZXROSNG(config-if-atm155-0/1/2/1.2)#cell-transport vpcZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vpc)#vpi 50ZXROSNG(config-if-atm155-0/1/2/1.2-atm-cell-vpc-prams)#





相关命令 :

show atm cell-transport 




# FR配置命令 
## debug frame-relay lmi 


debug frame-relay lmi 




命令功能 :

打开FR lmi协议报文调试开关。使用no命令关闭开关 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug frame-relay lmi 
  [interface 
 ＜interface-name 
＞]
no debug frame-relay lmi 
  [interface 
 ＜interface-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|指定接口








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#debug frame-relay lmi FRAME-RELAY LMI debugging is onZXROSNG#debug frame-relay LMI interface pos12-0/11/1/8FRAME-RELAY LMI debugging is onDisplaying LMI data from interface pos12-0/11/1/8





相关命令 :

show debug frame-relay 




## frame-relay interface-dlci 


frame-relay interface-dlci 




命令功能 :

设置接口的DLCI值 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay interface-dlci 
  ＜dlci 
＞ [cisco 
] [broadcast 
]

no frame-relay interface-dlci 








命令参数解释 :



参数|描述
---|---
＜dlci＞|DLCI值,范围16~1007
cisco|CISCO封装
broadcast|支持广播包








缺省 :

fr封装类型为ietf 






使用说明 :

该命令配置的前提是配置了接口点到点模式 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay interface-mode point-to-point ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay interface-dlci 20 cisco broadcast ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay interface-dlci 21 cisco ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay interface-dlci 22 broadcast





相关命令 :

show frame-relay pvc 




## frame-relay interface-mode 


frame-relay interface-mode 




命令功能 :

配置FR的接口传输模式，使用no命令恢复默认配置 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay interface-mode 
  {point-to-point 
|point-to-multipoint 
}

no frame-relay interface-mode 








命令参数解释 :



参数|描述
---|---
point-to-point|点到点模式
point-to-multipoint|点到多点模式








缺省 :

点到点模式 






使用说明 :

无





范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay interface-mode point-to-multipoint






相关命令 :

无 




## frame-relay interface-type 


frame-relay interface-type 




命令功能 :

设置接口类型 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay interface-type 
  {dte 
|dce 
}

no frame-relay interface-type 








命令参数解释 :



参数|描述
---|---
dte|接口类型为dce
dce|接口类型为dte








缺省 :

dte 






使用说明 :

仅支持物理口配置 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay interface-type dce





相关命令 :

无 




## frame-relay lmi-n391dte 


frame-relay lmi-n391dte 




命令功能 :

配置FR DTE设备的全状态查询报文计数器，使用no命令恢复默认配置 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay lmi-n391dte 
  ＜lmi-n391dte 
＞

no frame-relay lmi-n391dte 








命令参数解释 :



参数|描述
---|---
＜lmi-n391dte＞|发送全状态查询报文的周期范围1~255








缺省 :

6 






使用说明 :

只在DTE上使用，设置full-status查询的时间间隔 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if)#frame-relay lmi-n391dte 10





相关命令 :

无 




## frame-relay lmi-n392dce 


frame-relay lmi-n392dce 




命令功能 :

设置DCE的N392计数器 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay lmi-n392dce 
  ＜lmi-n392dce 
＞

no frame-relay lmi-n392dce 








命令参数解释 :



参数|描述
---|---
＜lmi-n392dce＞|错误阈值,范围1~10








缺省 :

3 






使用说明 :

n392dce要小于DCE n393的值 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay lmi-n392dce 5





相关命令 :

无 




## frame-relay lmi-n392dte 


frame-relay lmi-n392dte 




命令功能 :

配置FR DTE设备的LMI错误门限值，使用no命令恢复默认配置 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay lmi-n392dte 
  ＜lmi-n392dte 
＞

no frame-relay lmi-n392dte 








命令参数解释 :



参数|描述
---|---
＜lmi-n392dte＞|错误门限值，范围1~10








缺省 :

3 






使用说明 :

n392dte配置值要小于DTE N393的值 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay lmi-n392dte 5





相关命令 :

无 




## frame-relay lmi-n393dce 


frame-relay lmi-n393dce 




命令功能 :

配置FR DCE设备 LMI错误门限值，使用no命令恢复默认配置 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay lmi-n393dce 
  ＜lmi-n393dce 
＞

no frame-relay lmi-n393dce 








命令参数解释 :



参数|描述
---|---
＜lmi-n393dce＞|被观察事件的总数,范围 1~10








缺省 :

5 






使用说明 :

n393dce要大于DCE n392的值 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if)#frame-relay lmi-n393dce 10





相关命令 :

无 




## frame-relay lmi-n393dte 


frame-relay lmi-n393dte 




命令功能 :

配置FR DTE设备成功事件计数，使用no命令恢复默认配置 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay lmi-n393dte 
  ＜lmi-n393dte 
＞

no frame-relay lmi-n393dte 








命令参数解释 :



参数|描述
---|---
＜lmi-n393dte＞|被观察事件的总数,范围 1~10








缺省 :

5 






使用说明 :

n393dte要大于lmi-n392dte的值 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay lmi-n393dte 10





相关命令 :

无 




## frame-relay lmi-t392dce 


frame-relay lmi-t392dce 




命令功能 :

配置FR DCE 接收报文时间间隔，使用no命令回复默认配置 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay lmi-t392dce 
  ＜lmi-t392dce 
＞

no frame-relay lmi-t392dce 








命令参数解释 :



参数|描述
---|---
＜lmi-t392dce＞|在t392dce应该收到来自DTE的状态查询报文,范围5~30，单位s








缺省 :

15s 






使用说明 :

t392dce要大于DTE keepalive的值 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay lmi-t392dce 30





相关命令 :

无 




## frame-relay lmi-type 


frame-relay lmi-type 




命令功能 :

设置LMI类型 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay lmi-type 
  {q933a 
|cisco 
|ansi 
}

no frame-relay lmi-type 








命令参数解释 :



参数|描述
---|---
q933a|Lmi类型为cisco
cisco|Lmi类型为q933a
ansi|Lmi类型为ansi








缺省 :

q933a 






使用说明 :

DCE和DTE的LMI类型必须一致；仅支持物理口配置 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay lmi-type cisco





相关命令 :

无 




## frame-relay map 


frame-relay map 




命令功能 :

配置点到多点模式的MAP映射关系，使用no命令取消具体配置条目 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :


frame-relay map 
 ip 
 ＜ip-address 
＞ ＜dlci-value 
＞ [cisco 
] [broadcast 
]
no frame-relay map 
 ip 
 ＜ip-address 
＞ ＜dlci-value 
＞
				






命令参数解释 :



参数|描述
---|---
ip|IPv4地址
＜ip-address＞|MAP映射的对端IP地址
＜dlci-value＞|MAP映射的本端的DLCI值
cisco|CISCO封装
broadcast|支持广播包








缺省 :

fr封装类型为ietf 






使用说明 :

该命令配置的前提是配置了接口点到多点模式 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay interface-mode point-to-multipointZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay map ip 10.1.1.1 20 cisco broadcastZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay map ip 20.1.1.1 21 ciscoZXROSNG(config-fr-if-pos12-0/11/1/8)#frame-relay map ip 30.1.1.1 22 broadcast






相关命令 :

show frame-relay map 




## frame-relay 


frame-relay 




命令功能 :

进入FR配置模式 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



frame-relay 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

进入FR配置模式，使用exit可以退出返回全局配置模式。 






范例 :

ZXROSNG(config)# frame-relayZXROSNG(config-fr)#





相关命令 :

无 




interface :

interface (FR模式) 




命令功能 :

进入FR接口配置模式 






命令模式 :

 FR模式  






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
＜interface-byname＞|接口的别名
＜interface-name＞|接口的名称








缺省 :

无 






使用说明 :

只能进入FR模块关注的端口pos接口，且接口封装类型为FR类型





范例 :

ZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if)#





相关命令 :

无 




## keepalive 


keepalive 




命令功能 :

配置FR链路保活报文的发送间隔时间，使用no命令关闭保活配置 






命令模式 :

 FR接口模式  






命令默认权限级别 :

15 






命令格式 :



keepalive 
  [{＜keepalive-time 
＞|disable 
}]

no keepalive 








命令参数解释 :



参数|描述
---|---
＜keepalive-time＞|保活报文时间间隔
disable|关闭保活报文








缺省 :

10 






使用说明 :

主要在POS接口配置成帧中继DTE接口时起作用；DTE的LMI需要通过设定发送keepalive 报文的定时器时间，来检测PVC的状态，并根据此定时器设定PVC的状态。 






范例 :

ZXROSNG(config)#frame-relayZXROSNG(config-fr)#interface pos12-0/11/1/8ZXROSNG(config-fr-if-pos12-0/11/1/8)#keepalive 5





相关命令 :

无 




## show debug frame-relay 


show debug frame-relay 




命令功能 :

显示是否开启FR debug 开关 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug frame-relay 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show debug frame-relay FRAME-RELAY:  FRAME-RELAY LMI debugging is on





相关命令 :

debug frame-relay lmi 




## show frame-relay lmi 


show frame-relay lmi 




命令功能 :

显示LMI统计信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show frame-relay lmi 
  [interface 
 ＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|指定接口








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show frame-relay lmi LMI Statistics for interface pos192-0/1/1/1 (Frame Relay DTE)  LMI TYPE = Q933A  Invalid Unnumbered info 0             Invalid Prot Disc     0           Invalid dummy Call Ref  0             Invalid Msg Type      0           Invalid Status Message  0             Invalid Lock Shift    0           Invalid Information ID  0             Invalid Report IE Len 0           Invalid Report Request  0             Invalid Keep IE Len   0           Num Status Enq. Sent    0             Num Status msgs Rcvd  0           Num Update Status Rcvd  0             Num Status Timeouts   0 





相关命令 :

无 




## show frame-relay map 


show frame-relay map 




命令功能 :

显示FR全局配置的MAP条目 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show frame-relay map 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-fr-if)#show frame-relay map pos192-0/1/1/1(down):   ip        10.10.1.1   dlci      100(0x64, 0x1841)   maptype   static  encaptype ietf, nobroadcast  status    inactive





相关命令 :

frame-relay map 




## show frame-relay pvc 


show frame-relay pvc 




命令功能 :

显示PVC状态信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show frame-relay pvc 
  [{＜dlci 
＞|interface 
 ＜interface-name 
＞ [＜dlci 
＞]}] 







命令参数解释 :



参数|描述
---|---
＜dlci＞|查找对应具体接口名下，具体DLCI值对应的PVC信息
＜interface-name＞|查找对应具体接口名下的PVC信息
＜dlci＞|查找对应具体接口名下，具体DLCI值对应的PVC信息








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config-fr)#show frame-relay pvc PVC Statistics for interface pos192-0/1/1/1 (Frame Relay DTE)Active         Inactive       DeletedLocal          0               1               0   Unused         0               0               0   DLCI = 100 , DLCI USAGE  = LOCAL ,PVC STATUS = INACTIVE, INTERFACE = pos192-0/1/1/1





相关命令 :

frame-relay interface-dlciframe-relay map 




# HDLC配置命令 
## bidirection local-info 


bidirection local-info 




命令功能 :

双向邻居发现功能中，设置本端信息。使用no命令删除设置的本端信息。 






命令模式 :

 HDLC接口模式  






命令默认权限级别 :

15 






命令格式 :



bidirection local-info 
  ＜local-info 
＞

no bidirection local-info 








命令参数解释 :



参数|描述
---|---
＜local-info＞|本端信息，范围1~63字符。








缺省 :

无 






使用说明 :

设置本端信息，最大可设置63个字符。 






范例 :

ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#interface pos192-0/1/1/1ZXROSNG(config-hdlc-if-pos192-0/1/1/1)#bidirection local-info dZXROSNG(config-hdlc-if-pos192-0/1/1/1)#no bidirection ?  local-info  Set local info  peer-info   Set peer infoZXROSNG(config-hdlc-if-pos192-0/1/1/1)#no bidirection local-info 






相关命令 :

无 




## bidirection mode 


bidirection mode 




命令功能 :

设置命令扩展模式 






命令模式 :

 HDLC接口模式  






命令默认权限级别 :

15 






命令格式 :



bidirection mode 
  {loose 
|expand 
|strict 
 {short 
|long 
}}







命令参数解释 :



参数|描述
---|---
loose|松散模式
expand|协议双向邻居扩展模式
strict|严格扩展模式
short|short：扩展4个字节
long|long：扩展6个字节








缺省 :

松散模式 






使用说明 :

设置协议模式，松散模式、双向邻居扩展模块和严格扩展模式三者互斥。 






范例 :

ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#interface pos192-0/1/1/1ZXROSNG(config-hdlc-if-pos192-0/1/1/1)#bidirection mode ?  expand  Set mode expand  loose   Set mode loose  strict  Set mode strictZXROSNG(config-hdlc-if-pos192-0/1/1/1)#bidirection mode expand ZXROSNG(config-hdlc-if-pos192-0/1/1/1)#bidirection mode strict ?  long   Set strict mode long  short  Set strict mode short






相关命令 :

无 




## bidirection peer-info 


bidirection peer-info 




命令功能 :

双向邻居发现功能中，设置对端信息。使用no命令删除本端设置的对端信息。 






命令模式 :

 HDLC接口模式  






命令默认权限级别 :

15 






命令格式 :



bidirection peer-info 
  ＜peer-info 
＞

no bidirection peer-info 








命令参数解释 :



参数|描述
---|---
＜peer-info＞|对端信息，范围1~63字符。








缺省 :

无 






使用说明 :

设置对端信息，最大可设置63个字符。 






范例 :

ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#interface pos192-0/1/1/1ZXROSNG(config-hdlc-if-pos192-0/1/1/1)#bidirection peer-info ?  WORD  Peer info (1-63 characters)ZXROSNG(config-hdlc-if-pos192-0/1/1/1)#bidirection peer-info dsaZXROSNG(config-hdlc-if-pos192-0/1/1/1)#no bidirection peer-info ?  <cr>ZXROSNG(config-hdlc-if-pos192-0/1/1/1)#no bidirection peer-info 






相关命令 :

无 




## clear illegal-info 


clear illegal-info 




命令功能 :

双向邻居发现功能中，清空非法邻居信息。 






命令模式 :

 HDLC接口模式  






命令默认权限级别 :

15 






命令格式 :



clear illegal-info 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

清空HDLC接口下保存的非法邻居信息。 






范例 :

ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#intZXROSNG(config-hdlc)#interface pos192-0/1/1/1ZXROSNG(config-hdlc-if-pos192-0/1/1/1)#clear illegal-info 






相关命令 :

无 




## debug hdlc all 


debug hdlc all 




命令功能 :

打开HDLC 所有调试开关。使用no命令关闭HDLC所有调试开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug hdlc all 
 

no debug hdlc all 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

配置了hdlc all调试命令，且要在特权模式下输入terminal monitor命令，才能够显示调试信息，使用 no命令关掉打开的调试开关。 






范例 :

ZXROSNG#debug hdlc allAll HDLC debugging has been turned on





相关命令 :

debug hdlc packet 




## debug hdlc packet 


debug hdlc packet 




命令功能 :

打开HDLC报文调试开关。使用no命令关闭HDLC报文调试开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug hdlc packet 
  [interface 
 ＜interface-name 
＞]
no debug hdlc packet 
  [interface 
 ＜interface-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|pos接口名称








缺省 :

无 






使用说明 :

配置了报文调试命令，且要在特权模式下输入terminal monitor命令，才能够显示报文调试信息，使用 no命令关掉打开的报文调试开关。 






范例 :

ZXROSNG#debug hdlc packet interface pos192-0/1/1/1HDLC packet debugging is onDisplaying packet on interface pos192-0/1/1/1ZXROSNG#debug hdlc packet interface pos192-0/1/1/1HDLC packet debugging is onDisplaying packet on interface pos192-0/1/1/1






相关命令 :

debug hdlc all 




## hdlc 


hdlc 




命令功能 :

进入HDLC模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



hdlc 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

进入HDLC模式，使用exit可以退出返回全局配置模式。





范例 :

ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#





相关命令 :

无 




interface :

interface (HDLC模式) 




命令功能 :

从HDLC模式进入HDLC接口模式。 






命令模式 :

 HDLC模式  






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
＜interface-byname＞|pos接口的别名
＜interface-name＞|pos接口的名称








缺省 :

无 






使用说明 :

只能进入HDLC模块关注的端口： pos接口或通道化的cpos口。 






范例 :

ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#interface pos12-0/11/1/8ZXROSNG(config-hdlc-if-pos12-0/11/1/8)#ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#interface pos12-0/11/1/8ZXROSNG(config-hdlc-if-pos12-0/11/1/8)#





相关命令 :

无 




## keepalive 


keepalive 




命令功能 :

配置HDLC链路保活报文的发送时间间隔。 






命令模式 :

 HDLC接口模式  






命令默认权限级别 :

15 






命令格式 :



keepalive 
  [{＜keepalive-period 
＞|disable 
}]

no keepalive 








命令参数解释 :



参数|描述
---|---
＜keepalive-period＞|保活报文发送时间间隔，范围：1–32767 单位：秒 默认：10秒
disable|与no keepalive命令等价，是关闭HDLC发送保活报文的命令








缺省 :

10秒 






使用说明 :

修改保活报文发送时间间隔，no keepalive 等价于keepalive disable，二者功能相同，都是关闭HDLC发送保活报文的命令。 






范例 :

ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#interface pos12-0/11/1/8ZXROSNG(config-hdlc-if-pos12-0/11/1/8)#keepalive 1ZXROSNG(config)#hdlcZXROSNG(config-hdlc)#interface pos12-0/11/1/8ZXROSNG(config-hdlc-if-pos12-0/11/1/8)#keepalive 1





相关命令 :

无 




## show bidirection-info 


show bidirection-info 




命令功能 :

双向邻居发现功能中，显示非法邻居信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bidirection-info 
 interface 
 ＜hdlc-interface 
＞







命令参数解释 :



参数|描述
---|---
＜hdlc-interface＞|POS接口名称








缺省 :

无 






使用说明 :

显示HDLC接口下保存的非法邻居信息。 






范例 :

ZXROSNG#show bidirection-info interface pos192-0/1/1/1HDLC bidirection expand info   illegal info:  ddZXROSNG#






相关命令 :

无 




## show debug hdlc 


show debug hdlc 




命令功能 :

显示已打开的HDLC调试命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug hdlc 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

显示hdlc已打开的调试开关信息 






范例 :

ZXROSNG#show debug hdlc HDLC:  HDLC packet debugging is on






相关命令 :

无 




# MHDLC配置命令 
interface :

interface (MHDLC模式) 




命令功能 :

从MHDLC模式进入MHDLC聚合接口模式或MHDLC成员接口模式。 






命令模式 :

 MHDLC模式  






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
＜interface-byname＞|pos接口、posgroup聚合口的别名
＜interface-name＞|pos接口、posgroup聚合口的名称








缺省 :

无 






使用说明 :

只能进入MHDLC模块关注的端口： pos接口、posgroup聚合口等 






范例 :

ZXROSNG(config)#mhdlcZXROSNG(config-mhdlc)#interface pos12-0/11/1/8ZXROSNG(config-mhdlc-member-if-pos12-0/11/1/8)#ZXROSNG(config)#mhdlcZXROSNG(config-mhdlc)#interface pos12-0/11/1/8ZXROSNG(config-mhdlc-member-if-pos12-0/11/1/8)#





相关命令 :

无 




## mhdlc load-balance 


mhdlc load-balance 




命令功能 :

设置posgroup聚合组的负荷分担方式。使用no命令恢复posgroup聚合组的负荷分担方式为缺省值。 






命令模式 :

 MHDLC聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



mhdlc load-balance 
  {per-packet 
|per-destination 
}

no mhdlc load-balance 








命令参数解释 :



参数|描述
---|---
per-packet|逐包的负荷分担模式，
per-destination|逐流的负荷分担模式，为缺省模式








缺省 :

per-destination 






使用说明 :

设置posgroup聚合负荷分担模式， 






范例 :

ZXROSNG(config)#mhdlcZXROSNG(config-mhdlc)#interface posgroup1ZXROSNG(config-mhdlc-pg-if-posgroup1)#mhdlc load-balance per-packet





相关命令 :

无 




## mhdlc minimum-member 


mhdlc minimum-member 




命令功能 :

配置posgroup接口up阈值门限。 






命令模式 :

 MHDLC聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



mhdlc minimum-member 
  ＜minimum-number 
＞

no mhdlc minimum-member 








命令参数解释 :



参数|描述
---|---
＜minimum-number＞|配置posgroup up的阈值，缺省为1，范围：1–$#84148226#$








缺省 :

1 






使用说明 :

配置posgroup接口up门限，缺省情况下，阈值是1，即只要有一个成员接口保持up状态，该posgroup接口就是up状态。 






范例 :

ZXROSNG(config)#mhdlcZXROSNG(config-mhdlc)#interface posgroup1ZXROSNG(config-mhdlc-pg-if-posgroup1)#mhdlc minimum-member 4





相关命令 :

无 




## mhdlc 


mhdlc 




命令功能 :

进入MHDLC模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



mhdlc 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

进入MHDLC模式，使用exit可以退出返回全局配置模式。 






范例 :

ZXROSNG(config)#mhdlc                   ZXROSNG(config-mhdlc)#





相关命令 :

无 




## posgroup 


posgroup 




命令功能 :

添加接口到posgroup聚合组。使用no命令把相应接口从posgroup聚合组删除。 






命令模式 :

 MHDLC成员接口模式  






命令默认权限级别 :

15 






命令格式 :



posgroup 
  ＜posgroup-id 
＞

no posgroup 








命令参数解释 :



参数|描述
---|---
＜posgroup-id＞|链路聚合组号，范围：1–$#84148225#$








缺省 :

无 






使用说明 :

添加接口到posgroup聚合组。添加的接口的封装类型必须是HDLC，否则不允许加入。 






范例 :

ZXROSNG(config)#mhdlcZXROSNG(config-mhdlc)#interface pos12-0/11/1/8ZXROSNG(config-mhdlc-member-if-pos12-0/11/1/8)#posgroup 1





相关命令 :

无 




## show mhdlc 


show mhdlc 




命令功能 :

查看posgroup接口信息。为方便定位问题，需要能显示posgroup相关信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mhdlc 
  ＜posgroup-id 
＞ 







命令参数解释 :



参数|描述
---|---
＜posgroup-id＞|pos聚合组名称，范围：1–$#84148225#$








缺省 :

无 






使用说明 :

查看posgroup接口信息 






范例 :

ZXROSNG(config-mhdlc-member-if-pos192-0/1/1/1)#show mhdlc 1pos-group-id       : 1load-balance       : per-destinationminimum-member     : 1Member links: 0  active,  0  inactive-------------------------pos12-0/11/1/8(inactive)ZXROSNG(config-mhdlc-member-if-pos192-0/1/1/1)#show mhdlc 1pos-group-id       : 1load-balance       : per-destinationminimum-member     : 1Member links: 0  active,  0  inactive-------------------------pos12-0/11/1/8(inactive)





相关命令 :

无 




# MPPP配置命令 
interface :

interface (MPPP模式) 




命令功能 :

从MPPP配置模式进入接口配置模式。 






命令模式 :

 MPPP模式  






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
＜interface-byname＞|接口的别名
＜interface-name＞|接口的名称








缺省 :

无 






使用说明 :

只能进入MPPP模块关注的端口： multilink接口。multilink接口必须存在。 






范例 :

进入MPPP配置模式：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)#





相关命令 :

interface <interface-name>interface byname ：用别名进入接口模式。




## mppp header 


mppp header 




命令功能 :

使能MPPP头格式功能 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp header 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能MPPP头格式功能
disable|去使能MPPP头格式功能








缺省 :

未使能MPPP头格式功能 






使用说明 :

无 






范例 :

使能MPPP头格式功能：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)#mppp header enable






相关命令 :

无 




## mppp ipcp neighbor-route disable 


mppp ipcp neighbor-route disable 




命令功能 :

配置MPPP关闭主机路由添加的功能。 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp ipcp neighbor-route disable 
 







命令参数解释 :


					无
				 






缺省 :

开启主机路由添加的功能。 






使用说明 :

要开启主机路由添加功能，必须配置mppp ipcp neighbor-route enable命令;要关闭主机路由添加功能，使用mppp ipcp neighbor-route disable命令。





范例 :

在multilink1接口上关闭主机路由添加功能：ZXROSNG(config)#mpppZXROSNG(config-ppp)#interface multilink1ZXROSNG(config-ppp-if- multilink1)#mppp ipcp neighbor-route disable





相关命令 :

mppp ipcp neighbor-route enable 




## mppp ipcp neighbor-route enable 


mppp ipcp neighbor-route enable 




命令功能 :

配置MPPP开启主机路由添加的功能。 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp ipcp neighbor-route enable 
 







命令参数解释 :


					无
				 






缺省 :

开启主机路由添加的功能。 






使用说明 :

要开启主机路由添加功能，必须配置mppp ipcp neighbor-route enable命令;要关闭主机路由添加功能，使用mppp ipcp neighbor-route disable命令。





范例 :

在multilink1接口上启用主机路由添加功能：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-ppp-if-multilink1)#mppp ipcp neighbor-route enable





相关命令 :

mppp ipcp neighbor-route disable 




## mppp load-balance 


mppp load-balance 




命令功能 :

配置MPPP的负荷分担方式，使用no命令恢复缺省配置。 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp load-balance 
  {per-packet 
|per-destination 
}

no mppp load-balance 








命令参数解释 :



参数|描述
---|---
per-packet|配置MPPP的负荷分担方式是逐包
per-destination|配置MPPP的负荷分担方式是逐目的








缺省 :

默认配置MPPP的负荷分担方式是逐目的。 






使用说明 :

缺省方式下，负荷分担是采用逐目的方式。 






范例 :

配置multilink1接口的MPPP负荷分担方式为逐包：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)#mppp load-balance per-packet





相关命令 :

mppp multilink fragmentation 




## mppp mplscp disable 


mppp mplscp disable 




命令功能 :

配置MPPP启用MPLSCP，使用enable开启，使用disable命令取消配置。 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp mplscp disable 
 







命令参数解释 :


					无
				 






缺省 :

未开启MPLSCP协议。 






使用说明 :

要开启MPLSCP协议，必须配置mppp mplscp enable命令;要关闭MPLSCP协议，使用mppp mplscp disable命令。





范例 :

在multilink1接口上启用MPLSCP协议：ZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)#mppp mplscp enable





相关命令 :

无 




## mppp mplscp enable 


mppp mplscp enable 




命令功能 :

配置MPPP启用MPLSCP，使用enable开启，使用disable命令取消配置。 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp mplscp enable 
 







命令参数解释 :


					无
				 






缺省 :

未开启MPLSCP协议。 






使用说明 :

要开启MPLSCP协议，必须配置mppp mplscp enable命令;要关闭MPLSCP协议，使用mppp mplscp disable命令。





范例 :

在multilink1接口上启用MPLSCP协议：ZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)#mppp mplscp enable





相关命令 :

无 




## mppp multilink fragmentation 


mppp multilink fragmentation 




命令功能 :

配置MPPP的分片功能。使用no命令恢复缺省配置。 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp multilink fragmentation 
 

no mppp multilink fragmentation 








命令参数解释 :


					无
				 






缺省 :

不分片。 






使用说明 :

修改分片参数的时候需要解除链路multilink绑定关系。 






范例 :

配置multilink1接口的MPPP分片模式：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)# mppp multilink fragmentation





相关命令 :

mppp load-balance 




## mppp ssnhf accept disable 


mppp ssnhf accept disable 




命令功能 :

配置MPPP的成员链路协商LCP时不接收对端的SSNHF协商请求 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp ssnhf accept disable 
 







命令参数解释 :


					无
				 






缺省 :

缺省disable，拒绝对端发来的SSNHF请求，以长序MP头格式进行报文传输 






使用说明 :

成员口协商LCP时，以MPPP接口上的此命令配置来确定不接受SSNHF选项 






范例 :

配置multilink1接口成员接受对端发送的SSNHF请求：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)# mppp ssnhf accept disable





相关命令 :

mppp ssnhf request 




## mppp ssnhf accept enable 


mppp ssnhf accept enable 




命令功能 :

配置MPPP的成员链路协商LCP时接收对端的SSNHF协商请求 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp ssnhf accept enable 
 







命令参数解释 :


					无
				 






缺省 :

缺省disable，拒绝对端发来的SSNHF请求，以长序MP头格式进行报文传输 






使用说明 :

成员口协商LCP时，以MPPP接口上的此命令配置来确定接受SSNHF选项 






范例 :

配置multilink1接口成员接受对端发送的SSNHF请求：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)# mppp ssnhf accept enable





相关命令 :

mppp ssnhf request 




## mppp ssnhf request disable 


mppp ssnhf request disable 




命令功能 :

配置MPPP的成员链路协商LCP时不带SSNHF请求 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp ssnhf request disable 
 







命令参数解释 :


					无
				 






缺省 :

缺省disable，协商LCP时不携带SSNHF选项，以长序MP头格式协商 






使用说明 :

成员口协商LCP时，以MPPP接口上的此命令配置来确定不携带SSNHF选项 






范例 :

配置multilink1接口成员链路协商LCP时不发送SSNHF请求：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)# mppp ssnhf request disable





相关命令 :

mppp ssnhf accept 




## mppp ssnhf request enable 


mppp ssnhf request enable 




命令功能 :

配置MPPP的成员链路协商LCP时带SSNHF请求 






命令模式 :

 MPPP接口模式  






命令默认权限级别 :

15 






命令格式 :



mppp ssnhf request enable 
 







命令参数解释 :


					无
				 






缺省 :

缺省disable，协商LCP时不携带SSNHF选项，以长序MP头格式协商 






使用说明 :

成员口协商LCP时，MPPP接口上的此命令配置来确定携带SSNHF选项。 






范例 :

配置multilink1接口成员链路协商LCP时发送SSNHF请求：ZXROSNG(config)#mpppZXROSNG(config-mppp)#interface multilink1ZXROSNG(config-mppp-if-multilink1)# mppp ssnhf request enable





相关命令 :

mppp ssnhf accept 




## mppp 


mppp 




命令功能 :

进入MPPP配置模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



mppp 
 







命令参数解释 :


					无
				 






缺省 :

无。 






使用说明 :

无。 






范例 :

进入MPPP配置模式：ZXROSNG(config)#mpppZXROSNG(config-mppp)#






相关命令 :

ppp 




## show ppp mcc 


show ppp mcc 




命令功能 :

显示多链路内的摘要信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ppp mcc 
  [＜interface-number 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-number＞|显示指定mcc的摘要信息，范围：65-$#84869121#$








缺省 :

显示所有多链信息 






使用说明 :

无 






范例 :

dcn_mcc65  Bundle name : 005a0d56789a  Load-balance: per-destination  Member links: 1 active, 0 inactive     dcn_pos2





相关命令 :

show ppp multilink  




## show ppp multilink 


show ppp multilink 




命令功能 :

显示多链路内的摘要信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ppp multilink 
  [＜interface-number 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-number＞|显示指定multilink的摘要信息，范围：1-$#84869121#$








缺省 :

显示所有多链信息。 






使用说明 :

无。 






范例 :

显示多链内的摘要信息：ZXROSNG(config)#show ppp multilink 1multilink1  Bundle name : N/A  Load-balance: per-destination  MRRU: 1500  Member links: 0 active, 0 inactive





相关命令 :

show running-configshow running-config-interface




# PPP配置命令 
## bind ipv4 


bind ipv4 




命令功能 :

配置绑定命令，绑定ipv4 VT口，使用no命令取消设置 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



bind ipv4 
  ＜interface-name 
＞

no bind ipv4 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|配置绑定的ipv4 VT口名，长度1–31个字符








缺省 :

未配置绑定的ipv4 VT口名 






使用说明 :

该命令只在VT接口下配置 






范例 :

在virtual_template 1接口上配置绑定ipv4 VT口名：ZXROSNG(config)#pppZXROSNG(config-ppp)#interface virtual_template1ZXROSNG(config-ppp-if-virtual_template1)#ip-access-type dual//双栈接入ZXROSNG(config-ppp-if-virtual_template1)#bind ipv4 virtual_template2





相关命令 :

无 




## bind ipv6 


bind ipv6 




命令功能 :

配置绑定命令，绑定ipv6 VT口，使用no命令取消设置 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



bind ipv6 
  ＜interface-name 
＞

no bind ipv6 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|配置绑定的ipv6 VT口名，长度1–31个字符








缺省 :

未配置绑定的ipv6 VT口名 






使用说明 :

该命令只在VT接口下配置 






范例 :

在virtual_template 1接口上配置绑定ipv6VT口名：ZXROSNG(config)#pppZXROSNG(config-ppp)#interface virtual_template1ZXROSNG(config-ppp-if-virtual_template1)#ip-access-type dual//双栈接入ZXROSNG(config-ppp-if-virtual_template1)#bind ipv6 virtual_template2






相关命令 :

无 




## bind-authen-template 


bind-authen-template 




命令功能 :

绑定AAA认证模版，使用no命令取消绑定。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



bind-authen-template 
  ＜aaa-authen-template-number 
＞

no bind-authen-template 








命令参数解释 :



参数|描述
---|---
＜aaa-authen-template-number＞|需要绑定的AAA认证模版号。范围：1–2128








缺省 :

AAA模版如果没有配置认证类型，缺省使用本地认证。 






使用说明 :

使用AAA配置的认证模版类型来认证对端用户 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#bind-authen-template 100






相关命令 :

无 




## bind-ip-pool 


bind-ip-pool 




命令功能 :

绑定IPv4地址池，使用no命令取消绑定。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



bind-ip-pool 
  ＜ip-pool-name 
＞

no bind-ip-pool 








命令参数解释 :



参数|描述
---|---
＜ip-pool-name＞|需要绑定的IP POOL名字。范围1–32个字符








缺省 :

不绑定IP POOL。 






使用说明 :

在协商IPCP协议时，如果对端接口没有配置IP地址，本地将从IP POOL中选择一个可用的IP地址分配给对端。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#bind-ip-pool zxr10






相关命令 :

无 




## bind-ipv6-pool 


bind-ipv6-pool 




命令功能 :

绑定IPV6 POOL 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



bind-ipv6-pool 
  ＜para 
＞

no bind-ipv6-pool 








命令参数解释 :



参数|描述
---|---
＜para＞|绑定IPV6 POOL， IPV6 POOL名字长度1-31字符








缺省 :

无缺省值 






使用说明 :

无 






范例 :

ZXROSNG(config)#ppp ZXROSNG(config-ppp)#interface pos192-0/1/1/1  ZXROSNG(config-ppp-if-pos192-0/1/1/1)#bind-ipv6-pool a






相关命令 :

无 




## debug ppp all 


debug ppp all 




命令功能 :

打开PPP功能所有调试开关，使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug ppp all 
 

no debug ppp all 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

配置了调试命令，且要在特权模式下输入terminal monitor命令，才能够显示调试信息，使用no命令关掉打开的调试开关。 






范例 :

ZXROSNG#debug ppp allAll PPP debugging has been turned on






相关命令 :

debug ppp authenticationdebug ppp errordebug ppp eventsdebug ppp lcpdebug ppp ncpdebug ppp packet




## debug ppp authentication 


debug ppp authentication 




命令功能 :

打开PPP认证信息调试开关，使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ppp authentication 
  [interface 
 ＜interface-name 
＞]
no debug ppp authentication 
  [interface 
 ＜interface-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

配置了调试命令，且要在特权模式下输入terminal monitor命令，才能够显示调试信息，使用no命令关掉打开的调试开关。 






范例 :

ZXROSNG#debug ppp authenticationPPP authentication debugging is on






相关命令 :

debug ppp all 




## debug ppp error 


debug ppp error 




命令功能 :

打开PPP错误信息调试开关，使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ppp error 
  [interface 
 ＜interface-name 
＞]
no debug ppp error 
  [interface 
 ＜interface-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

配置了调试命令，且要在特权模式下输入terminal monitor命令，才能够显示调试信息，使用no命令关掉打开的调试开关。 






范例 :

ZXROSNG#debug ppp errorPPP error debugging is on






相关命令 :

debug ppp all 




## debug ppp events 


debug ppp events 




命令功能 :

打开PPP事件信息调试开关，使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ppp events 
  [interface 
 ＜interface-name 
＞]
no debug ppp events 
  [interface 
 ＜interface-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

配置了调试命令，且要在特权模式下输入terminal monitor命令，才能够显示调试信息，使用no命令关掉打开的调试开关。 






范例 :

ZXROSNG#debug ppp eventsPPP events debugging is on






相关命令 :

debug ppp all 




## debug ppp lcp 


debug ppp lcp 




命令功能 :

打开PPP LCP报文解析输出调试开关，使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ppp lcp 
  [interface 
 ＜interface-name 
＞]
no debug ppp lcp 
  [interface 
 ＜interface-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

配置了调试命令，且要在特权模式下输入terminal monitor命令，才能够显示调试信息，使用no命令关掉打开的调试开关。 






范例 :

ZXROSNG#debug ppp lcpPPP LCP debugging is on






相关命令 :

debug ppp all 




## debug ppp ncp 


debug ppp ncp 




命令功能 :

打开PPP NCP报文解析输出调试开关，使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ppp ncp 
  [interface 
 ＜interface-name 
＞]
no debug ppp ncp 
  [interface 
 ＜interface-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

配置了调试命令，且要在特权模式下输入terminal monitor命令，才能够显示调试信息，使用no命令关掉打开的调试开关。 






范例 :

ZXROSNG#debug ppp ncpPPP NCP debugging is on






相关命令 :

debug ppp all 




## debug ppp packet 


debug ppp packet 




命令功能 :

打开PPP控制报文输出调试开关，使用no命令关闭开关。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug ppp packet 
  [interface 
 ＜interface-name 
＞]
no debug ppp packet 
  [interface 
 ＜interface-name 
＞]
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

配置了调试命令，且要在特权模式下输入terminal monitor命令，才能够显示调试信息，使用no命令关掉打开的调试开关。 






范例 :

ZXROSNG#debug ppp packetPPP packet debugging is on






相关命令 :

debug ppp all 




## default-router-priority 


default-router-priority 




命令功能 :

用于配置PPP模块自动添加默认路由的优先级 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



default-router-priority 
  ＜defaul-router-priority 
＞

no default-router-priority 








命令参数解释 :



参数|描述
---|---
＜defaul-router-priority＞|自动添加默认路由的优先级，1优先级最高，默认200，范围：1-254。








缺省 :

默认值为200 






使用说明 :

本命令用于配置在此接口生成的默认路由的优先级 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface virtual_template1ZXROSNG(config-ppp-if- virtual_template1)# default-router-priority 54





相关命令 :

无 




interface :

interface (PPP模式) 




命令功能 :

从PPP配置模式进入接口配置模式。 






命令模式 :

 PPP模式  






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
＜interface-byname＞|接口的别名
＜interface-name＞|接口的名称








缺省 :

无 






使用说明 :

只能进入PPP封装类型的端口：pos、cpos、ce1、virtual_template或同异步串口等接口。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#






相关命令 :

interface byname ：用别名进入接口模式。 




## ip-access-type 


ip-access-type 




命令功能 :

配置接口的接入类型 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ip-access-type 
  {dual 
|ipv4 
|ipv6 
}

no ip-access-type 








命令参数解释 :



参数|描述
---|---
dual|双栈接入
ipv4|IPv4接入
ipv6|IPv6接入








缺省 :

缺省双栈接入 






使用说明 :

无 






范例 :

ZXROSNG(config)#ppp ZXROSNG(config-ppp)#interface pos192-0/1/1/1  ZXROSNG(config-ppp-if-pos192-0/1/1/1)#ip-access-type ipv4





相关命令 :

无 




## ipv6 access-type 


ipv6 access-type 




命令功能 :

配置IPV6用户接入的地址分配方式 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ipv6 access-type 
  {slaac 
|dhcpv6 
|dhcpv6-slaac 
}

no ipv6 access-type 








命令参数解释 :



参数|描述
---|---
slaac|IPV6用户接入采用slaac方式，RA报文分配前缀
dhcpv6|IPV6用户接入采用dhcpv6方式获得地址
dhcpv6-slaac|IPV6用户混合接入，既支持slaac方式，又允许dhcpv6接入








缺省 :

无 






使用说明 :

IPV6用户上线，支持dhcpv6-slaac混合接入时必须配置此命令；此命令未配置时IPV6接入方式以接口下M位的配置为准 






范例 :

配置virtual_template2接口的接入方式为dhcpv6-slaac混合接入：ZXROSNG(config)#pppZXROSNG(config-ppp)#interface virtual_template2ZXROSNG(config-if-virtual_template2)# ipv6 access-type dhcpv6-slaac





相关命令 :

无 




## ipv6 dns-server 


ipv6 dns-server 




命令功能 :

配置IPV6 DNS地址 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 dns-server 
  ＜ipv6-address 
＞ [secondary 
]
no ipv6 dns-server 
  [secondary 
]
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|配置IPV6的主/辅DNS服务器地址
secondary|辅DNS服务器地址标识








缺省 :

无缺省值 






使用说明 :

无 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface virtual_template1ZXROSNG(config-ppp-if-virtual_template1)#ipv6 dns-server 2001::1 ZXROSNG(config-ppp-if-virtual_template1)#ipv6 dns-server 2003::1 secondary






相关命令 :

无 




## keepalive 


keepalive 




命令功能 :

配置PPP链路保活报文的发送时间间隔。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



keepalive 
  [{＜keepalive-period 
＞|disable 
}]

no keepalive 








命令参数解释 :



参数|描述
---|---
＜keepalive-period＞|保活报文发送时间间隔，范围：1–32767
disable|关闭PPP发送保活报文








缺省 :

保活报文发送时间隔：为10秒非virtual_template类型接口为10秒，virtual_template类型接口由性能参数决定，为$#84869129#$秒。 






使用说明 :

当链路需要快速收敛时，可以将<timeout>的值设置的小一些。但是<timeout>值过小可能导致链路不稳定。不稳定原因是，可能由于网络拥塞本端在一定时间内还没有收到keepalive报文，本端就认为对端已经协议down掉了，然后本端发出重新建链请求。no keepalive是关闭PPP发送保活报文的命令，如果对方发送保活请求报文，本地只回应保活应答，并不主动发送保活请求报文。keepalive disable功能与no keepalive相同，都是关闭PPP发送保活报文的命令。






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#keepalive 15ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#keepalive 15






相关命令 :

ppp max-echo 




## multilink-group 


multilink-group 




命令功能 :

将本链路捆绑入指定的MPPP接口，使用no命令取消绑定。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



multilink-group 
  ＜interface-name 
＞

no multilink-group 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|<number>多链路接口号；multilink<number>接口名，例如multilink3








缺省 :

不绑定。 






使用说明 :

绑定的multilink接口必须存在。 






范例 :

ZXROSNG(config-ppp)#interface cpos3_e1-1/1.1/1/1:1ZXROSNG(config-ppp-if-cpos3_e1-1/1.1/1/1:1)#multilink-group multilink3ZXROSNG(config-ppp)#interface cpos3_e1-1/1.1/1/1:1ZXROSNG(config-ppp-if-cpos3_e1-1/1.1/1/1:1)#multilink-group multilink3






相关命令 :

ppp multilink endpoint 




## nas-port-type 


nas-port-type 




命令功能 :

配置用户接入NAS的物理端口类型 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



nas-port-type 
  {async 
|sync 
|isdn-sync 
|isdn-async-v120 
|isdn-async-v110 
|virtual 
|piafs 
|hdlc 
|x.25 
|x.75 
|g.3-fax 
|sdsl 
|adsl-cap 
|adsl-dmt 
|idsl 
|ethernet 
|xdsl 
|cable 
|wireless-other 
|802.11 
|user-defined 
 ＜user-define nas-port-type 
＞}

no nas-port-type 








命令参数解释 :



参数|描述
---|---
async|配置接入类型为异步，取值为0
sync|配置接入类型为同步，取值为1
isdn-sync|配置接入类型为同步isdn，取值为2
isdn-async-v120|配置接入类型为异步isdn v120，取值为3
isdn-async-v110|配置接入类型为异步isdn v110，取值为4
virtual|配置接入类型为virtual，取值为5
piafs|配置接入类型为piafs，取值为6
hdlc|配置接入类型为hdlc-clear-channel，取值为7
x.25|配置接入类型为x.25，取值为8
x.75|配置接入类型为x.75，取值为9
g.3-fax|配置接入类型为g.3-fax，取值为10
sdsl|配置接入类型为sdsl，取值为11
adsl-cap|配置接入类型为adsl-cap，取值为12
adsl-dmt|配置接入类型为adsl-dmt，取值为13
idsl|配置接入类型为idsl，取值为14
ethernet|配置接入类型为ehernet，取值为15
xdsl|配置接入类型为xdsl，取值为16
cable|配置接入类型为有线电缆，取值为17
wireless-other|配置接入类型为无线，取值为18
802.11|配置接入类型为ieee802.11无线，取值为19
＜user-define nas-port-type＞|配置接入类型为用户自定义类型，参数范围是<20-255>








缺省 :

缺省类型为virtual。 






使用说明 :

默认类型为virtual，使用no命令恢复默认配置。 此命令配置用户radius认证、计费请求报文中Nas-Port-Type属性的取值。 






范例 :

配置NAS Port类型为ethernet：ZXROSNG(config-ppp-if-virtual_template1)#nas-port-type ethernet






相关命令 :

show running-config ppp 




## portrange-poolname 


portrange-poolname 




命令功能 :

配置portrange的地址池名 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



portrange-poolname 
  ＜Portrangepoolname 
＞

no portrange-poolname 








命令参数解释 :



参数|描述
---|---
＜Portrangepoolname＞|地址池名，长度为1~31个字符。








缺省 :

无缺省值 






使用说明 :

无 






范例 :

配置portrange的地址池名为a:ZXROSNG(config)#pppZXROSNG(config-ppp)#interface virtual_template1ZXROSNG(config-ppp-if-virtual_template1)#portrang-poolname a






相关命令 :

无 




## ppp authentication 


ppp authentication 




命令功能 :

配置PPP的认证方式，使用no命令取消设置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp authentication 
  {chap 
|pap 
|chap-pap 
}

no ppp authentication 








命令参数解释 :



参数|描述
---|---
chap|配置CHAP（Challenge Handshake Authentication Protocol）认证方式
pap|配置PAP（Password Authentication Protocol）认证方式
chap-pap|配置CHAP和PAP（Password Authentication Protocol）自适应认证方式








缺省 :

未配置认证方式。 






使用说明 :

1. PAP为两次握手验证，口令为明文。PAP验证过程如下：    被验证方发送用户名和口令到验证方。    验证方根据用户配置查看是否有此用户以及口令是否正确，然后返回不同的响应。2. CHAP为三次握手验证，口令为密钥。CHAP验证过程如下：    验证方向被验证方发送一些随机产生的报文(challenge)。    被验证方，用接收到的报文中的challenge加上报文中的ID，再加上自己的密钥作为材料，然后运用MD5单向hash算法，产生challenge response，发送到验证方。    验证方用自己保存的被验证方口令、challenge加上接收到的报文中的ID，然后运用MD5单向hash算法计算，产生本方的challenge response。比较本方的challenge response和接收到的报文中的challenge response，如果两者相等，则认证通过；如果两者不相等，则认证失败。3. chap-pap自适应认证方式。   在链路协商过程中，先以CHAP认证方式进行协商，如果另一端设备支持CHAP认证，则协商为CHAP认证方式；如果另一端设备不支持CHAP认证，而建议使用PAP认证，那么两台设备之间协商为PAP认证方式。





范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp authentication chap






相关命令 :

无 




## ppp bcp enable 


ppp bcp enable 




命令功能 :

配置PPP采用BCP（桥控制协议）。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp bcp enable 
 

no ppp bcp enable 








命令参数解释 :


					无
				 






缺省 :

未开启BCP协议。 






使用说明 :

BCP协议是桥接协议，通常用于VPLS异构功能，正常情况下是不启用的。使用BCP协议时，需要去掉接口的所有三层属性。比如，删除接口的IP地址、关闭IPCP协议等。接口启用了BCP协议，且与ULEI进行了绑定，如果要关闭BCP协议，必须先把接口与ULEI解绑定，才能关闭BCP协议，否则关闭协议的命令会执行不成功。要开启BCP协议，必须配置ppp bcp enable命令，用来启用BCP协议。要关闭BCP协议，使用no ppp bcp enable命令。






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/3/0/1ZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp enable






相关命令 :

ppp ipcp enable 




## ppp bcp management-inline 


ppp bcp management-inline 




命令功能 :

BCP支持Management-Inline功能。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp bcp management-inline 
 

no ppp bcp management-inline 








命令参数解释 :


					无
				 






缺省 :

未开启BCP协议。 






使用说明 :

BCP协议是桥接协议，通常用于VPLS异构功能，正常情况下是不启用的。使用BCP协议时，需要去掉接口的所有三层属性。比如，删除接口的IP地址、关闭IPCP协议等。接口启用了BCP协议，且与ULEI进行了绑定，如果要关闭BCP协议，必须先把接口与ULEI解绑定，才能关闭BCP协议，否则关闭协议的命令会执行不成功。要开启BCP协议，必须配置ppp bcp enable命令，用来启用BCP协议。要关闭BCP协议，使用no ppp bcp enable命令。





范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/3/0/1ZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp enableZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp packet-indicatorZXROSNG(config-ppp-if-pos12-0/3/0/1)#no ppp bcp tagged-frameZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp management-inline






相关命令 :

ppp ipcp enable 




## ppp bcp packet-indicator 


ppp bcp packet-indicator 




命令功能 :

BCP支持报文指示功能。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp bcp packet-indicator 
 

no ppp bcp packet-indicator 








命令参数解释 :


					无
				 






缺省 :

未开启BCP协议。 






使用说明 :

BCP协议是桥接协议，通常用于VPLS异构功能，正常情况下是不启用的。使用BCP协议时，需要去掉接口的所有三层属性。比如，删除接口的IP地址、关闭IPCP协议等。接口启用了BCP协议，且与ULEI进行了绑定，如果要关闭BCP协议，必须先把接口与ULEI解绑定，才能关闭BCP协议，否则关闭协议的命令会执行不成功。要开启BCP协议，必须配置ppp bcp enable命令，用来启用BCP协议。要关闭BCP协议，使用no ppp bcp enable命令。






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/3/0/1ZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp enableZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp packet-indicatorZXROSNG(config-ppp-if-pos12-0/3/0/1)#no ppp bcp tagged-frameZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp management-inline






相关命令 :

ppp ipcp enable 




## ppp bcp tagged-frame 


ppp bcp tagged-frame 




命令功能 :

BCP支持IEEE 802标记帧。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp bcp tagged-frame 
 

no ppp bcp tagged-frame 








命令参数解释 :


					无
				 






缺省 :

未开启BCP协议。 






使用说明 :

BCP协议是桥接协议，通常用于VPLS异构功能，正常情况下是不启用的。使用BCP协议时，需要去掉接口的所有三层属性。比如，删除接口的IP地址、关闭IPCP协议等。接口启用了BCP协议，且与ULEI进行了绑定，如果要关闭BCP协议，必须先把接口与ULEI解绑定，才能关闭BCP协议，否则关闭协议的命令会执行不成功。要开启BCP协议，必须配置ppp bcp enable命令，用来启用BCP协议。要关闭BCP协议，使用no ppp bcp enable命令。






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/3/0/1ZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp enableZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp packet-indicatorZXROSNG(config-ppp-if-pos12-0/3/0/1)#no ppp bcp tagged-frameZXROSNG(config-ppp-if-pos12-0/3/0/1)#ppp bcp management-inline






相关命令 :

ppp ipcp enable 




## ppp chap hostname 


ppp chap hostname 




命令功能 :

配置CHAP认证方式时本地路由器名，使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp chap hostname 
  ＜alternate-chap-hostname 
＞

no ppp chap hostname 








命令参数解释 :



参数|描述
---|---
＜alternate-chap-hostname＞|配置CHAP认证方式时本地路由器名，长度1–159个字符








缺省 :

未配置本地路由器名。 






使用说明 :

＜alternate-chap-hostname＞是区分大小写的。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp chap hostname ZXR10






相关命令 :

ppp chap password 




## ppp chap password 


ppp chap password 




命令功能 :

配置本地路由器CHAP认证密钥，使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp chap password 
  {encrypted 
 ＜The encryted password 
＞|＜The clear password 
＞}

no ppp chap password 








命令参数解释 :



参数|描述
---|---
encrypted|配置加密密钥
＜The encryted password＞|配置chap认证方式时本地路由器的加密形式的密钥，长度1-200个字符
＜The clear password＞|配置chap认证方式时本地路由器的明文密钥，长度1-31个字符








缺省 :

未配置本地路由器密钥。 






使用说明 :

＜password＞是区分大小写的。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp chap password ZXR10






相关命令 :

ppp chap hostname 




## ppp ipcp disable 


ppp ipcp disable 




命令功能 :

关闭PPP IPCP协议。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp disable 
 







命令参数解释 :


					无
				 






缺省 :

启用IPCP协议 






使用说明 :

当PPP启用BCP协议时，需要关闭IPCP协议，正常情况下需要进行IPCP协商。 






范例 :

ZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp disableZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp disable






相关命令 :

ppp ipcp enableppp bcp enable




## ppp ipcp dns accept 


ppp ipcp dns accept 




命令功能 :

配置接受对端的PPP IPCP DNS请求，使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp dns accept 
 

no ppp ipcp dns accept 








命令参数解释 :


					无
				 






缺省 :

不接受对端的PPP IPCP DNS请求。 






使用说明 :

无。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp dns accept






相关命令 :

ppp ipcp dns request 




## ppp ipcp dns ip 


ppp ipcp dns ip 




命令功能 :

配置PPP DNS IP地址，使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp dns ip 
  ＜primary-ip-address 
＞ [＜secondary-ip-address 
＞]

no ppp ipcp dns ip 








命令参数解释 :



参数|描述
---|---
＜primary-ip-address＞|配置的主DNS地址
＜secondary-ip-address＞|配置的辅DNS地址








缺省 :

不配置DNS地址。 






使用说明 :

无。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp dns ip 10.1.1.1 20.1.1.1






相关命令 :

ppp ipcp dns acceptppp ipcp dns request




## ppp ipcp dns request 


ppp ipcp dns request 




命令功能 :

配置发送PPP IPCP DNS请求，使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp dns request 
 

no ppp ipcp dns request 








命令参数解释 :


					无
				 






缺省 :

不配置发送PPP IPCP DNS请求。 






使用说明 :

无。 






范例 :

ZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp dns requestZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp dns request






相关命令 :

ppp ipcp dns accept 




## ppp ipcp enable 


ppp ipcp enable 




命令功能 :

配置PPP启用IPCP，使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp enable 
 

no ppp ipcp enable 








命令参数解释 :


					无
				 






缺省 :

启用IPCP协议。 






使用说明 :

当PPP启用BCP协议时，需要关闭IPCP协议，正常情况下需要进行IPCP协商。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp enable






相关命令 :

ppp bcp enable 




## ppp ipcp neighbor-route disable 


ppp ipcp neighbor-route disable 




命令功能 :

配置PPP关闭主机路由添加的功能。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp neighbor-route disable 
 







命令参数解释 :


					无
				 






缺省 :

开启主机路由添加的功能。 






使用说明 :

要开启主机路由添加功能，必须配置ppp ipcp neighbor-route enable命令;要关闭主机路由添加功能，使用ppp ipcp neighbor-route disable命令。





范例 :

在pos192-0/1/1/1接口上关闭主机路由添加功能：ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos192-0/1/1/1ZXROSNG(config-ppp-if-pos192-0/1/1/1)#ppp ipcp neighbor-route disable





相关命令 :

ppp ipcp neighbor-route enable 




## ppp ipcp neighbor-route enable 


ppp ipcp neighbor-route enable 




命令功能 :

配置PPP开启主机路由添加的功能。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp neighbor-route enable 
 







命令参数解释 :


					无
				 






缺省 :

开启主机路由添加的功能。 






使用说明 :

要开启主机路由添加功能，必须配置ppp ipcp neighbor-route enable命令;要关闭主机路由添加功能，使用ppp ipcp neighbor-route disable命令。





范例 :

在pos192-0/1/1/1接口上启用主机路由添加功能：ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos192-0/1/1/1ZXROSNG(config-ppp-if-pos192-0/1/1/1)#ppp ipcp neighbor-route enable





相关命令 :

ppp ipcp neighbor-route disable 




## ppp ipcp peer-address 


ppp ipcp peer-address 




命令功能 :

配置给对端分配的IP地址。使用no命令取消设置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp peer-address 
  ＜ipv4-address 
＞

no ppp ipcp peer-address 








命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|给对端分配的IP地址








缺省 :

无。 






使用说明 :

无。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos192-0/1/1/1ZXROSNG(config-ppp-if- pos192-0/1/1/1)# ppp ipcp peer-address 1.1.1.2





相关命令 :

无。 




## ppp ipcp wins accept 


ppp ipcp wins accept 




命令功能 :

配置接受对端的PPP IPCP WINS请求，使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp wins accept 
 

no ppp ipcp wins accept 








命令参数解释 :


					无
				 






缺省 :

不接受对端的PPP IPCP WINS请求。 






使用说明 :

无 






范例 :

ZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp wins acceptZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp wins accept






相关命令 :

ppp ipcp wins request 




## ppp ipcp wins ip 


ppp ipcp wins ip 




命令功能 :

配置PPP WINS地址。使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp wins ip 
  ＜primary-ip-address 
＞ [＜secondary-ip-address 
＞]

no ppp ipcp wins ip 








命令参数解释 :



参数|描述
---|---
＜primary-ip-address＞|配置的主WINS地址
＜secondary-ip-address＞|配置的辅WINS地址








缺省 :

不配置WINS地址。 






使用说明 :

无。 






范例 :

ZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp wins ip 10.1.1.1 20.1.1.1ZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp wins ip 10.1.1.1 20.1.1.1






相关命令 :

ppp ipcp wins requestppp ipcp wins accept




## ppp ipcp wins request 


ppp ipcp wins request 




命令功能 :

配置发送PPP IPCP WINS请求，使用no命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp ipcp wins request 
 

no ppp ipcp wins request 








命令参数解释 :


					无
				 






缺省 :

不配置发送PPP IPCP WINS请求。 






使用说明 :

无。 






范例 :

ZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp wins requestZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp ipcp wins request






相关命令 :

ppp ipcp wins accept 




## ppp max-echo 


ppp max-echo 




命令功能 :

配置PPP链路在没有收到对端的keepalive应答时，发送最大的keepalive报文请求数目。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp max-echo 
  {＜keepalive-granularity 
＞}

no ppp max-echo 








命令参数解释 :



参数|描述
---|---
＜keepalive-granularity＞|保活报文最大重发次数，范围：1–10








缺省 :

保活报文最大重发次数：非virtual_template类型接口为5次，virtual_template类型接口由性能参数决定，为$#84869128#$次。 






使用说明 :

当链路需要快速收敛时，可以将<max-count>的值设置的小一些。但是<max-count>值过小可能导致链路不稳定。不稳定原因是，可能由于网络拥塞本端在一定次数内还没有收到keepalive报文，本端就认为对端已经down掉了，然后本端发出重新建链请求。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp max-echo 10






相关命令 :

keepalive <timeout> 




## ppp mplscp disable 


ppp mplscp disable 




命令功能 :

配置PPP启用MPLSCP，使用enable命令开启，使用disable命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp mplscp disable 
 







命令参数解释 :


					无
				 






缺省 :

未开启MPLSCP协议。 






使用说明 :

要开启MPLSCP协议，必须配置ppp mplscp enable命令;要关闭MPLSCP协议，使用ppp mplscp disable命令。





范例 :

在pos192-0/1/1/1接口上启用MPLSCP协议：ZXROSNG(config-ppp)#interface pos192-0/1/1/1ZXROSNG(config-ppp-if-pos192-0/1/1/1)#ppp mplscp disable





相关命令 :

ppp ipcp disable 




## ppp mplscp enable 


ppp mplscp enable 




命令功能 :

配置PPP启用MPLSCP，使用enable命令开启，使用disable命令取消配置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp mplscp enable 
 







命令参数解释 :


					无
				 






缺省 :

未开启MPLSCP协议。 






使用说明 :

要开启MPLSCP协议，必须配置ppp mplscp enable命令;要关闭MPLSCP协议，使用ppp mplscp disable命令。





范例 :

在pos192-0/1/1/1接口上启用MPLSCP协议：ZXROSNG(config-ppp)#interface pos192-0/1/1/1ZXROSNG(config-ppp-if-pos192-0/1/1/1)#ppp mplscp enable 






相关命令 :

ppp bcp enable 




## ppp multilink endpoint 


ppp multilink endpoint 




命令功能 :

设定链路协商时MPPP EPD属性，用于区分子链路属于不同的MPPP链路。使用no命令取消设置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp multilink endpoint 
  ＜endpoint-discriminator 
＞

no ppp multilink endpoint 








命令参数解释 :



参数|描述
---|---
＜endpoint-discriminator＞|描述符字符串，长度为1~32个字符








缺省 :

按照一定规则自动生成。 






使用说明 :

缺省方式下，在同一个多链中的子链endpoint相同。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp multilink endpoint zxr10ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp multilink endpoint zxr10






相关命令 :

multilink-group multilink 




## ppp open 


ppp open 




命令功能 :

主动和对方路由器建立PPP链路。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp open 
 







命令参数解释 :


					无
				 






缺省 :

无。 






使用说明 :

触发LCP重新协商。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp open






相关命令 :

无 




## ppp pap sent-username 


ppp pap sent-username 




命令功能 :

配置本地路由器PAP认证的用户名和密码，使用no命令取消设置。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp pap sent-username 
  ＜outbound-pap-username 
＞ password 
 {encrypted 
 ＜The encryted password 
＞|＜The clear password 
＞}

no ppp pap sent-username 








命令参数解释 :



参数|描述
---|---
＜outbound-pap-username＞|配置PAP认证方式时的用户名，长度1–159个字符
encrypted|指定加密密码
＜The encryted password＞|配置PAP认证方式时的加密形式的口令，长度1–120个字符
＜The clear password＞|配置PAP认证方式时的明文口令，长度1–31个字符








缺省 :

未配置用户名和口令。 






使用说明 :

<username>和<password>都是区分大小写的。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)# ppp pap sent-username ZXR10 password zxr10






相关命令 :

ppp chap hostnameppp chap password




## ppp protocol-compress disable 


ppp protocol-compress disable 




命令功能 :

配置PPP关闭报文协议域压缩的功能。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp protocol-compress disable 
 







命令参数解释 :


					无
				 






缺省 :

不开启报文协议域压缩功能。 






使用说明 :

要开启报文协议域压缩功能，必须配置ppp protocol-compress enable命令;要关闭报文协议域压缩功能，使用ppp protocol-compress disable命令。





范例 :

在pos192-0/1/1/1接口上关闭报文协议域压缩功能：ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos192-0/1/1/1ZXROSNG(config-ppp-if-pos192-0/1/1/1)#ppp protocol-compress disable





相关命令 :

ppp protocol-compress enable 




## ppp protocol-compress enable 


ppp protocol-compress enable 




命令功能 :

配置PPP开启报文协议域压缩的功能。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp protocol-compress enable 
 







命令参数解释 :


					无
				 






缺省 :

不开启报文协议域压缩的功能。 






使用说明 :

要开启报文协议域压缩功能，必须配置ppp protocol-compress enable命令;要关闭报文协议域压缩功能，使用ppp protocol-compress disable命令。





范例 :

在pos192-0/1/1/1接口上启用报文协议域压缩功能：ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos192-0/1/1/1ZXROSNG(config-ppp-if-pos192-0/1/1/1)#ppp protocol-compress enable





相关命令 :

ppp protocol-compress disable 




## ppp timeout authentication 


ppp timeout authentication 




命令功能 :

配置PPP链路认证超时间隔。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp timeout authentication 
  [＜timeout-authen-seconds 
＞]

no ppp timeout authentication 








命令参数解释 :



参数|描述
---|---
＜timeout-authen-seconds＞|超时间隔，范围：1–30








缺省 :

认证超时间隔为5秒。 






使用说明 :

在链路比较拥塞的情况下，可以将该超时时间配置大一点，避免链路协商、认证时总是超时失败。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp timeout negotiation 20ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp timeout authentication 20






相关命令 :

ppp timeout negotiationppp timeout authenticationkeepalive <timeout>




## ppp timeout negotiation 


ppp timeout negotiation 




命令功能 :

配置PPP链路协商超时间隔。 






命令模式 :

 PPP接口模式  






命令默认权限级别 :

15 






命令格式 :



ppp timeout negotiation 
  [＜timeout-restart-seconds 
＞]

no ppp timeout negotiation 








命令参数解释 :



参数|描述
---|---
＜timeout-restart-seconds＞|超时间隔，范围：1–30








缺省 :

协商超时间隔为5秒。 






使用说明 :

在链路比较拥塞的情况下，可以将该超时时间配置大一点，避免链路协商、认证时总是超时失败。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#interface pos12-0/11/1/8ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp timeout negotiation 20ZXROSNG(config-ppp-if-pos12-0/11/1/8)#ppp timeout authentication 20






相关命令 :

ppp timeout negotiationppp timeout authenticationkeepalive <timeout>




## ppp 


ppp 




命令功能 :

进入PPP配置模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ppp 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

需要先进入全局配置模式。 






范例 :

ZXROSNG(config)#pppZXROSNG(config-ppp)#






相关命令 :

mppp 




## show debug ppp 


show debug ppp 




命令功能 :

显示已打开的PPP调试命令。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug ppp 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show debug pppPPP: PPP LCP debugging is on PPP NCP debugging is on PPP packet debugging is on PPP authentication debugging is on PPP events debugging is on PPP error debugging is on






相关命令 :

无 




# SmartGroup配置命令 
## clear lacp 


clear lacp 




命令功能 :

该命令工作于LACP模式，用于清除LACP收发包计数。 






命令模式 :

 LACP模式  






命令默认权限级别 :

15 






命令格式 :



clear lacp 
  [＜smartgroup-id 
＞] counters 








命令参数解释 :



参数|描述
---|---
＜smartgroup-id＞|<作用>需要清除收发包计数的聚合组组号。<取值范围>默认范围1–$#83951617#$，如果项目通过性能参数设置了最大值，则范围是1~项目性能参数值。
counters|<作用>清除收发包计数。








缺省 :

无 






使用说明 :

不携带参数smartgroup-id，表示清除所有聚合组成员口的收发包计数。携带参数smartgroup-id，表示清除某个聚合组的所有成员口的收发包计数。





范例 :

查看所有成员口的收发包计数：ZXROSNG(config-lacp)#show lacp counters Smartgroup:1Actor         LACPDUs             Marker    LACPDUs    MarkerPort          Tx         Rx         Tx  Rx    Err        Err-------------------------------------------------------------------gei-0/1/0/5   33         27         0   0     0          0gei-0/1/0/6   32         27         0   0     0          0Smartgroup:2Actor         LACPDUs             Marker    LACPDUs    MarkerPort          Tx         Rx         Tx  Rx    Err        Err-------------------------------------------------------------------gei-0/1/0/7   20         21         0   0     0          0清除名称为smartgroup1的聚合组下的所有成员口的收发包计数：ZXROSNG(config-lacp)#clear lacp 1 counters再次查看所有成员口的收发包计数：ZXROSNG(config-lacp)#show lacp 1 counters               Smartgroup:1Actor         LACPDUs               Marker    LACPDUs    MarkerPort          Tx         Rx         Tx  Rx    Err        Err-------------------------------------------------------------------gei-0/1/0/5   0          0          0   0     0          0gei-0/1/0/6   0          0          0   0     0          0清除所有成员口的收发包计数：ZXROSNG(config-lacp)#clear lacp counters 再次查看所有成员口的收发包计数：ZXROSNG(config-lacp)#show lacp counters  Smartgroup:1Actor         LACPDUs               Marker    LACPDUs    MarkerPort          Tx         Rx         Tx  Rx    Err        Err-------------------------------------------------------------------gei-0/1/0/5   0          0          0   0     0          0gei-0/1/0/6   0          0          0   0     0          0Smartgroup:2Actor         LACPDUs               Marker    LACPDUs    MarkerPort          Tx         Rx         Tx  Rx    Err        Err-------------------------------------------------------------------gei-0/1/0/7   0          0          0   0     0          0





相关命令 :

无 




## debug lacp 


debug lacp 




命令功能 :

该命令工作于特权模式下，用于打开LACP（Link Aggregation Control Protocol，链路聚合控制协议）状态机信息或报文收发信息打印开关。LACP模块的操作是由系统中数个状态机（State Machine）来控制完成的，每个状态机都有其独特的功能。各状态机状态的迁移是由事件引起的（如定时器超时、接收到LACP协议包以及端口状态的改变等），并触发相应动作。LACP状态机有如下几类：    RX状态机：该状态机负责从对端接受协议数据包，并做相应处理。    定期发送状态机：确定本端及其对端为了维持链路聚合，是否周期地交换协议数据包。    选择逻辑状态机：负责选择和该端口相关的聚合体。    MUX状态机：负责将某个端口绑定于选定的聚合体，或者把端口从聚合体拆离。同时还负责根据当前的协议信息需要，把该端口的接收或者发送功能使能或者关闭。    TX状态机：处理在其他状态机的要求下或者基于定期的协议数据包的发送。





命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug lacp 
  {packets 
 [interface 
 ＜interface-name 
＞]|fsm 
 [interface 
 ＜interface-name 
＞]|all 
}
no debug lacp 
  {packets 
|fsm 
|all 
}
				






命令参数解释 :



参数|描述
---|---
packets|所有端口报文内容
＜interface-name＞|接口的名称
fsm|所有端口状态机的变化信息
＜interface-name＞|接口的名称
all|所有调试开关








缺省 :

无 






使用说明 :

该命令需要配合terminal monitor命令一起使用，配置此命令后，还需要在特权模式下输入terminal monitor命令，才能够显示LACP状态机信息或报文收发信息。可使用no debug lacp命令关闭打印开关。





范例 :

ZXROSNG#terminal monitor 打开LACP全局打印开关：ZXROSNG#debug lacp allAll LACP debugging has been turned on关闭LACP全局打印开关：ZXROSNG#no debug lacp allAll LACP debugging has been turned off打开所有smartgroup成员口的LACP报文收发信息打印开关：ZXROSNG#debug lacp packets LACP packets debugging is on关闭所有smartgroup成员口的LACP报文收发信息打印开关：ZXROSNG#no debug lacp packets LACP packets debugging is off打开某个smartgroup成员口的LACP报文收发信息打印开关：ZXROSNG#debug lacp packets interface gei-0/1/0/5LACP packets debugging is onDisplaying LACP packets on interface gei-0/1/0/5打开所有smartgroup成员口的LACP状态机信息打印开关：ZXROSNG#debug lacp fsmLACP finite state machine debugging is on关闭所有smartgroup成员口的LACP状态机信息打印开关：ZXROSNG#no debug lacp fsmLACP finite state machine debugging is off打开某个smartgroup成员口的LACP状态机信息打印开关：ZXROSNG#debug lacp fsm interface gei-0/1/0/5LACP finite state machine debugging is onDisplaying LACP finite state machine on interface gei-0/1/0/5





相关命令 :

无 




interface :

interface (LACP模式) 




命令功能 :

从LACP模式进入LACP成员接口模式或LACP聚合接口模式。 






命令模式 :

 LACP模式  






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
＜interface-byname＞|<参数>接口别名
＜interface-name＞|<参数>指定的端口名








缺省 :

无 






使用说明 :

从LACP模式进入LACP成员接口模式或LACP聚合接口模式。 






范例 :

ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/1





相关命令 :

无 




## lacp active limitation 


lacp active limitation 




命令功能 :

该命令工作于LACP聚合接口模式，用于配置聚合组激活上限。某个聚合组下处于UP状态的链路数最多只能为此命令配置的聚合组激活上限值。在一个聚合组内，处于UP状态的成员链路数可以影响到聚合组的状态和带宽。聚合组的带宽是所有处于UP状态的成员接口的带宽之和。当状态处于UP的成员链路数目达到上限阈值后，之后再发生成员链路状态变为UP都不会使Eth-Trunk接口的带宽增加。设置状态为UP的链路数上限阈值的目的是在保证了带宽的情况下提高网络的可靠性。





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


lacp active limitation 
  ＜active-limitation-number 
＞

no lacp active limitation 








命令参数解释 :



参数|描述
---|---
＜active-limitation-number＞|<作用>配置聚合组最多可以激活多少成员。<取值范围>默认范围0–$#83951619#$，默认值是64。如果项目通过性能参数设置了最大值，则范围是1~项目性能参数值，默认值是项目性能参数值。








缺省 :

$#83951619#$ 






使用说明 :

在配置本命令之前，需要通过lacp mode命令，将聚合组的工作模式设置为支持802.3ad协议的聚合组。 






范例 :

配置聚合组激活上限值为2：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp active limitation 2清除聚合组激活上限：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#no lacp active limitation






相关命令 :

无 




## lacp aggregator timeout 


lacp aggregator timeout 




命令功能 :

smartgroup接口模式下配置聚合链路组超时时间，单位秒。当一个聚合链路组已经被选中但是在超时时间内仍然不能使聚合端口协议up，就要进行聚合链路重新选择。对应no命令恢复默认超时时间是30秒。ON模式不支持。在配置本命令之前，需要通过lacp mode命令，将聚合组的工作模式设置为支持802.3ad协议的聚合组。






命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


lacp aggregator timeout 
  ＜aggregator-timeout 
＞

no lacp aggregator timeout 








命令参数解释 :



参数|描述
---|---
＜aggregator-timeout＞|聚合链路组超时时间，范围10-500，单位秒。默认值为30秒。








缺省 :

30 






使用说明 :

只有协议模式支持，on模式不支持此功能。 






范例 :

ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp aggregator timeout 20 






相关命令 :

无 




## lacp backup 


lacp backup 




命令功能 :

配置smartgroup成员口的备属性。 






命令模式 :

 LACP成员接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp backup 
 

no lacp backup 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

这个命令主要用在主备端口的应用场景，配置备属性端口前，聚合组中不能存在其他备属性端口，且聚合组中的主属性端口个数不能大于两个；ON模式聚合组在存在备属性端口时，不能再绑定第三个成员端口。802.3ad协议模式的smartgroup成员不支持配置backup属性。 






范例 :

ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/1ZXROSNG(config-lacp-member-if-gei-0/1/0/1)#lacp backup






相关命令 :

无 




## lacp fast respond 


lacp fast respond 




命令功能 :

该命令作用于LACP聚合接口模式，用于设置LACP协商快速应答。配置本命令后，如果该聚合组下的某个成员接口收到LACP报文后，发现RX状态机信息有变化，会立即运行MUX状态机和TX状态机进行协商快速应答。





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


lacp fast respond 
 

no lacp fast respond 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

LACP聚合口下设置协商快速应答，供CE双归PE主备联动时使用。 






范例 :

配置LACP协商快速应答：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp fast respond清除LACP协商快速应答：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#no lacp fast respond 






相关命令 :

无 




## lacp force-switch 


lacp force-switch 




命令功能 :

smartgroup接口模式下命令强制切换





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


lacp force-switch 
 






命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

1)smartgroup接口模式下支持。2)存在满足基本切换条件的另一个聚合链路组。3)不存在满足基本切换条件的另一个聚合链路组，命令强制切换不会进行任何动作。4)ON模式不支持5)不支持no命令





范例 :

ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp force-switch






相关命令 :

无 




## lacp hold-off 


lacp hold-off 




命令功能 :

配置mc-lag延迟切换hold-off时间





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


lacp hold-off 
  ＜hold-off 
＞

no lacp hold-off 








命令参数解释 :



参数|描述
---|---
＜hold-off＞|时间参数，取值范围是0～65535（单位：s）,默认为0








缺省 :

0





使用说明 :

不配置该命令时，hold-off时间默认为0。当为默认值时，showrun不显示该信息





范例 :

配置hold-off时间是10：ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp hold-off 10





相关命令 :

无



## lacp load-balance 


lacp load-balance 




命令功能 :

该命令工作于LACP聚合接口模式，用于设置链路聚合组的负荷分担方式。 






命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp load-balance 
  {per-destination 
|per-packet 
|pri-label 
|pub-label 
|pub-pri-label 
}

no lacp load-balance 








命令参数解释 :



参数|描述
---|---
per-destination|<作用>基于流的负荷分担方式
per-packet|<作用>基于包的负荷分担方式
pri-label|<作用>基于私有标签的负荷分担方式
pub-label|<作用>基于公用标签的负荷分担方式
pub-pri-label|<作用>基于公用标签和私有标签的负荷分担方式








缺省 :

per-destination 






使用说明 :

只有smartgroup接口才能配置负荷分担方式 






范例 :

配置基于包的负荷分担方式：ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp load-balance per-packet清除负荷分担方式：ZXROSNG(config-lacp-sg-if-smartgroup1)#no lacp load-balance





相关命令 :

无 




## lacp mac 


lacp mac 




命令功能 :

配置smartgroup接口的主备MAC。 






命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp mac 
 master 
 ＜MAC address 
＞ backup 
 ＜MAC address 
＞

no lacp mac 








命令参数解释 :



参数|描述
---|---
＜MAC address＞|<作用>指定smartgroup接口的备MAC地址,不支持组播和广播MAC
＜MAC address＞|<作用>指定smartgroup接口的备MAC地址,不支持组播和广播MAC








缺省 :

无 






使用说明 :

此命令用于配置smartgroup接口的主备MAC地址，只在ON模式多主备环境生效。 






范例 :

配置smartgroup1的主备MAC：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp mac master  aaa.bbbb.cccc backup 1000. 0001.0001






相关命令 :

lacp modelacp multi-backup




## lacp minimum-member 


lacp minimum-member 




命令功能 :

该命令工作于LACP聚合接口模式，用于配置某个聚合组的状态为UP的接口成员链路数的上限阈值。某个聚合组下UP的链路数大于聚合组协议UP阈值时该聚合组才能成功聚合。





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


lacp minimum-member 
  ＜minimum-member 
＞

no lacp minimum-member 








命令参数解释 :



参数|描述
---|---
＜minimum-member＞|<作用>配置聚合组协议UP阈值。<取值范围>范围1–$#83951619#$，如果项目通过性能参数设置了最大值，则范围是1~项目性能参数值。<默认值>1。








缺省 :

1 






使用说明 :

配置聚合组的协议UP阈值 






范例 :

配置聚合组协议UP阈值：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp minimum-member 2删除聚合组协议UP阈值：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#no lacp minimum-member






相关命令 :

无 




## lacp mode 


lacp mode 




命令功能 :

设置链路聚合组的聚合模式。使用no命令恢复成默认配置，缺省配置是静态trunk模式（on模式）。 






命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp mode 
  {802.3ad 
|on 
}

no lacp mode 








命令参数解释 :



参数|描述
---|---
802.3ad|<作用>配置聚合组聚合模式是采用802.3ad标准的LACP协议。
on|<作用>配置聚合组聚合模式是静态trunk，此时不运行LACP协议。








缺省 :

on模式 






使用说明 :

只有smartgroup接口才能配置聚合模式。 






范例 :

配置聚合组聚合模式：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp mode 802.3ad清除聚合组聚合模式：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#no lacp mode





相关命令 :

无 




## lacp multi-backup 


lacp multi-backup 




命令功能 :

该命令用于配置smartgroup成员口的多备属性。 






命令模式 :

 LACP成员接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp multi-backup 
 

no lacp multi-backup 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

这个命令主要用在主备端口的应用场景，且聚合组中的主备属性端口个数大于两个。聚合组需要多个备属性端口时，每个端口须配置multi-backup属性。802.3ad协议模式的smartgroup成员不支持配置multi-backup属性。该命令和成员口的lacp backup互斥。






范例 :

配置成员口为多备属性：ZXROSNG(config-lacp)#ZXROSNG(config-lacp)#interface gei-0/1/0/1ZXROSNG(config-lacp-member-if-gei-0/1/0/1)#lacp multi-backup






相关命令 :

无 




## lacp port-priority 


lacp port-priority 




命令功能 :

配置LACP的接口优先级。 






命令模式 :

 LACP成员接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp port-priority 
  ＜port-priority 
＞

no lacp port-priority 








命令参数解释 :



参数|描述
---|---
＜port-priority＞|<作用>配置LACP端口优先级，缺省为32768，范围：1–65535








缺省 :

32768 






使用说明 :

配置了该命令后，选择端口加入聚合组时根据端口优先级的顺序加入。 






范例 :

配置成员的端口优先级为100：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/1ZXROSNG(config-lacp-member-if-gei-0/1/0/1)#lacp port-priority 100 






相关命令 :

无 




## lacp protocol-packet 


lacp protocol-packet 




命令功能 :

该命令用于配置控制面smartgroup接口发送报文的选路规则。 






命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp protocol-packet 
  {load-balance 
 {per-destination 
|per-packet 
}|random 
|ip-fixed 
}







命令参数解释 :



参数|描述
---|---
load-balance|负荷分担选路规则
per-destination|基于流的负荷分担方式
per-packet|基于包的负荷分担方式
random|随机选路规则
ip-fixed|基于IP地址的固定选路规则








缺省 :

由性能参数决定 






使用说明 :

使用场景仅需要变更控制面smartgroup接口发送报文的选路规则而又不影响转发面的选路规则时，可通过该命令配置。






范例 :

配置控制面的选路规则为基于IP地址的固定选路规则ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp protocol-packet ip-fixed






相关命令 :

lacp load-balance  




## lacp restore 


lacp restore 




命令功能 :

在smartgroup接口模式下配置聚合端口备向主恢复使能以及超时时间，单位秒。 






命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp restore 
  {revertive 
 ＜revertive-time 
＞|immediately 
|non-revertive 
}

no lacp restore 








命令参数解释 :



参数|描述
---|---
revertive|回切等待时间模式
＜revertive-time＞|回切等待时间(取值范围为1~65535S)
immediately|立即回切
non-revertive|不回切模式








缺省 :

立即回切 






使用说明 :

当主满足回切条件时会向主回切。 






范例 :

配置回切时间为10s:ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp restore revertive 10






相关命令 :

无 




## lacp sys-priority 


lacp sys-priority 




命令功能 :

进入Smartgroup接口配置模式，配置LACP的smartgroup系统优先级。对应no命令恢复smartgroup优先级默认值。 






命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp sys-priority 
  ＜sys-priority 
＞

no lacp sys-priority 








命令参数解释 :



参数|描述
---|---
＜sys-priority＞|配置smartgroup系统优先级，范围1~65535，缺省为32768








缺省 :

32768 






使用说明 :

如果smartgroup接口下配置了优先级就以接口配置为准，如果smartgroup接口下没有配置优先级就以全局配置为准。 






范例 :

ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#lacp sys-priority 100






相关命令 :

无 




## lacp system-priority 


lacp system-priority 




命令功能 :

该命令工作于LACP模式，用于配置LACP的全局系统优先级。 






命令模式 :

 LACP模式  






命令默认权限级别 :

15 






命令格式 :



lacp system-priority 
  ＜system-priority 
＞

no lacp system-priority 








命令参数解释 :



参数|描述
---|---
＜system-priority＞|<作用>LACP全局系统优先级。配置的数值越大，优先级越低。<取值范围>1~65535。<默认值>32768。








缺省 :

32768 






使用说明 :

LACP优先级包括全局优先级和聚合组优先级。    全局优先级是通过本命令来设置的    聚合组优先级是通过lacp sys-priority命令设置的设置LACP全局优先级是为了区分两端设备优先级的高低。全局优先级高的一端将被选作链路的主动端，按照主动端设备的接口来选择活动接口。设置LACP聚合组优先级是为了区别同一设备不同聚合接口的优先级，接口优先级高的将被选作活动接口。如果没有通过lacp sys-priority命令配置LACP的聚合组的优先级，则该聚合组使用本命令配置的全局系统优先级做为聚合组的默认优先级。





范例 :

配置全局系统优先级：ZXROSNG(config)#lacpZXROSNG(config-lacp)#lacp system-priority 1清除全局系统优先级：ZXROSNG(config)#lacpZXROSNG(config-lacp)#no lacp system-priority





相关命令 :

无 




## lacp timeout 


lacp timeout 




命令功能 :

配置成员接口的LACP长短超时。 






命令模式 :

 LACP成员接口模式  






命令默认权限级别 :

15 






命令格式 :



lacp timeout 
  {long 
|short 
}

no lacp timeout 








命令参数解释 :



参数|描述
---|---
long|<作用>配置端口LACP长超时
short|<作用>配置端口LACP短超时








缺省 :

long 






使用说明 :

本端配置了长超时，要求对端系统每过30秒发送一次LACP报文。本端配置了短超时，要求对端系统每过1秒发送一次LACP报文。





范例 :

配置成员gei-0/1/0/1的超时模式为短超时：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/1ZXROSNG(config-lacp-member-if-gei-0/1/0/1)#lacp timeout short 






相关命令 :

无 




## lacp 


lacp 




命令功能 :

该命令工作于全局配置模式，用于进入LACP模式。LACP（Link Aggregation Control Protocol，链路聚合控制协议）是一种实现链路动态汇聚的协议，在提高两端传输速率的同时也提供了较高的可靠性。链路两端通过发送LACP协议报文，通告彼此的参数，自动形成并启用一条聚合链路。聚合链路形成后，LACP负责实时维护链路状态，当检测到接收或者发送方向链路故障时，自动调整链路聚合使用的端口。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


lacp 
 






命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于进入LACP模式。 






范例 :

进入LACP模式，示例如下：ZXROSNG(config)#lacpZXROSNG(config-lacp)#





相关命令 :

无 




## lag-bfd ipv6 


lag-bfd ipv6 




命令功能 :

配置LAG使能IPv6 BFD检测，并可以配置源地址、目的地址、最小收发包时间间隔和检测倍数等参数。 






命令模式 :

 LACP成员接口模式  






命令默认权限级别 :

15 






命令格式 :



lag-bfd ipv6 
  [source 
 ＜source-ipv6-address 
＞] destination 
 ＜destination-ipv6-address 
＞ [min-tx 
 ＜min-send-interval 
＞ min-rx 
 ＜min-receive-interval 
＞ multiplier 
 ＜multiplier 
＞]

no lag-bfd ipv6 








命令参数解释 :



参数|描述
---|---
＜source-ipv6-address＞|源地址
＜destination-ipv6-address＞|目的地址
＜min-send-interval＞|最小发包时间间隔，范围:$#35389448#$ –$#35389449#$ ，单位:毫秒
＜min-receive-interval＞|最小收包时间间隔，范围:$#35389450#$ -$#35389451#$ ，单位:毫秒
＜multiplier＞|检测倍数，范围:3-50








缺省 :

无 






使用说明 :

此命令用于在成员口下配置LAG使能IPv6 BFD。源地址和目的地址请按照业务需要配置，源地址建议配置为loopback接口的地址。绑定同一个smartgroup的成员口下的track和lag-bfd ipv6做了互斥。





范例 :

配置源地址为1::1、目的地址为1::2、最小发包时间间隔为20毫秒、最小收包时间间隔为20毫秒、检测倍数为10的bfd检测：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/5ZXROSNG(config-lacp-member-if-gei-0/1/0/5)#lag-bfd ipv6 source 1::1 destination 1::2  min-tx 20 min-rx 20 multiplier 10





相关命令 :

无 




## lag-bfd 


lag-bfd 




命令功能 :

配置LAG使能BFD检测，并可以配置源地址、目的地址、最小收发包时间间隔和检测倍数等参数。 






命令模式 :

 LACP成员接口模式  






命令默认权限级别 :

15 






命令格式 :



lag-bfd 
  [source 
 ＜source-ip-address 
＞] destination 
 ＜destination-ip-address 
＞ [min-tx 
 ＜min-send-interval 
＞ min-rx 
 ＜min-receive-interval 
＞ multiplier 
 ＜multiplier 
＞]

no lag-bfd 








命令参数解释 :



参数|描述
---|---
＜source-ip-address＞|源地址
＜destination-ip-address＞|目的地址
＜min-send-interval＞|最小发包时间间隔，范围:$#35389448#$–$#35389449#$，单位:毫秒
＜min-receive-interval＞|最小收包时间间隔，范围:$#35389450#$-$#35389451#$，单位:毫秒
＜multiplier＞|检测倍数，范围:3-50








缺省 :

无 






使用说明 :

此命令用于在成员口下配置LAG使能BFD。源地址和目的地址请按照业务需要配置，源地址建议配置为loopback接口的地址。绑定同一个smartgroup的成员口下的track和lag-bfd做了互斥。





范例 :

配置源地址为1.1.1.1、目的地址为1.1.1.2、最小发包时间间隔为20毫秒、最小收包时间间隔为20毫秒、检测倍数为10的bfd检测：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface fei-0/1/0/5ZXROSNG(config-lacp-member-if-gei-0/1/0/5)#lag-bfd source 1.1.1.1 destination 1.1.1.2 min-tx 20 min-rx 20 multiplier 10





相关命令 :

无 




## mc-lag iccp 


mc-lag iccp 




命令功能 :

配置MC-LAG的ICCP绑定。no 命令删除配置





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


mc-lag iccp 
  ＜Mc-lag iccp 
＞

no mc-lag iccp 








命令参数解释 :



参数|描述
---|---
＜Mc-lag iccp＞|<作用>iccp的实例号








缺省 :

无





使用说明 :

设置mc-lag所绑定的iccp实例





范例 :

配置MC-LAG绑定的iccp实例为1：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#mc-lag iccp 1





相关命令 :

无



## mc-lag mode 


mc-lag mode 




命令功能 :

配置MC-LAG工作模式：自动模式、强制主用模式和强制备用模式。本命令只在802.3协议模式下生效。ON模式可以配置，但是无效





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


mc-lag mode 
  {auto 
|force-master 
|force-backup 
}

no mc-lag mode 








命令参数解释 :



参数|描述
---|---
auto|自动模式，主备根据优先级自动决策。默认模式
force-master|强制主用模式
force-backup|强制备用模式








缺省 :

自动模式





使用说明 :

如果需要工作在负荷分担模式，这两台设备都需要配置成强制主用模式





范例 :

配置MC-LAG的工作模式为强制主用模式：ZXROSNG(config-lacp-sg-if-smartgroup1)#mc-lag mode force-master





相关命令 :

无



## mc-lag priority 


mc-lag priority 




命令功能 :

配置mc-lag的优先级。no命令恢复优先级默认值。本命令只在802.3协议模式下生效。ON模式可以配置，但是无效命令模式





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


mc-lag priority 
  ＜Mc-lag priority 
＞

no mc-lag priority 








命令参数解释 :



参数|描述
---|---
＜Mc-lag priority＞|配置mc-lag优先级，范围1~65535，缺省为32768








缺省 :

32768





使用说明 :

该配置是为了选择mc-lag的主备，根据优先级来决策，优先级高的为主用设备，值越小优先级越高





范例 :

配置MC-LAG的优先级为3000：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#mc-lag priority 3000





相关命令 :

无



## mc-lag roid 


mc-lag roid 




命令功能 :

配置MC-LAG的标识符，包括node-id，roid。no 命令删除配置





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


mc-lag roid 
  ＜Mc-lag roid 
＞ node-id 
 ＜Mc-lag node-id 
＞

no mc-lag roid 








命令参数解释 :



参数|描述
---|---
＜Mc-lag roid＞|<作用>标识符。<取值范围>范围1-4294967293
＜Mc-lag node-id＞|<作用>节点ID。<取值范围>范围0-7。








缺省 :

无





使用说明 :

通过roid来标识同一个mc-lag组，通过node-id来保证相同mc-lag成员里面的actor number不重复。所以，组成mc-lag的两台设备的roid必须配置成一致，node-id需要配置成不一致





范例 :

配置MC-LAG的roid为1，node-id为2：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#mc-lag roid 1 node-id 2





相关命令 :

无



## mc-lag sys-id 


mc-lag sys-id 




命令功能 :

配置mc-lag的系统ID，包括系统优先级和系统MAC。no命令取消配置。本命令只在802.3协议模式下生效。on模式可以配置，但是无效。





命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :


mc-lag sys-id 
  ＜Mc-lag sys-mac 
＞ sys-priority 
 ＜Mc-lag system-priority 
＞

no mc-lag sys-id 








命令参数解释 :



参数|描述
---|---
＜Mc-lag sys-mac＞|<作用>配置MC-LAG系统MAC，不支持配置广播MAC和组播MAC。
＜Mc-lag system-priority＞|<作用>配置MC-LAG系统优先级。<取值范围>范围1~65535。








缺省 :

无





使用说明 :

本端会根据对端配置的系统MAC来对端口加入链路聚合组进行逻辑选择。直连的两端smartgroup接口下不能配置同一个系统MAC，否则报文交互状态协商认为其中的成员端口是环回连接，出现Agg State为unselected*状态。配置了mc-lag系统ID后，本端就会采用mc-lag的系统ID和对端进行LACP协商。no命令删除mc-lag系统ID后，本端会采用机架MAC和命令配置的LACP系统优先级和对端进行LACP协商。组成MC-LAG的两台设备的mc-lag的系统ID需要配置相同，否则mc-lag不进入工作状态，进入备用standby状态





范例 :

配置MC-LAG的系统优先级为1000和系统MAC为aaaa.bbbb.cccc：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#mc-lag sys-id aaaa.bbbb.cccc sys-priority 1000





相关命令 :

无



## mc-lag track 


mc-lag track 




命令功能 :

配置mc-lag与SAMgr的检测联动。 






命令模式 :

 LACP聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



mc-lag track 
  ＜track-name 
＞ pw-type 


no mc-lag track 








命令参数解释 :



参数|描述
---|---
＜track-name＞|<作用>指定跟踪的track对象名称
pw-type|<作用>指定检测的类型为pw-type








缺省 :

无 






使用说明 :

此配置用于配置mc-lag与pw侧的联动切换。需要通过SAMGR建立关联。 






范例 :

配置关联zte的对象：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface smartgroup1ZXROSNG(config-lacp-sg-if-smartgroup1)#mc-lag track zte pw-type 






相关命令 :

无 




## show debug lacp 


show debug lacp 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于查看LACP打印开关的开启情况。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug lacp 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

查看LACP debug开关打开情况。 






范例 :

如果之前配置了debug lacp all命令，查询结果如下：ZXROSNG#show debug lacpLACP:  LACP packets debugging is on   LACP finite state machine debugging is on如果之前配置了debug lacp packets命令，查询结果如下：ZXROSNG#show debug lacp    LACP:  LACP packets debugging is on如果之前配置了debug lacp fsm命令，查询结果如下：ZXROSNG#show debug lacp  LACP:  LACP finite state machine debugging is on如果之前配置了debug lacp packets interface gei-0/1/0/5命令，查询结果如下：ZXROSNG#show debug lacpLACP:  LACP packets debugging is enabled on interface gei-0/1/0/5如果之前配置了debug lacp fsm interface gei-0/1/0/5命令，查询结果如下：ZXROSNG#show debug lacpLACP:  LACP finite state machine debugging is enabled on interface gei-0/1/0/5





相关命令 :

debug lacp packets debug lacp fsm debug lacp all




## show lacp 


show lacp 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于聚合组当前的配置和状态，包括以下内容：    查看聚合组成员口的收/发包状态    显示成员口的聚合状态    查看对端邻居的成员口状态    查看LACP系统优先级和系统MAC





命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :


show lacp 
  {[＜smartgroup-id 
＞] {counters 
|internal 
|neighbors 
|mc-lag 
}|sys-id 
} 






命令参数解释 :



参数|描述
---|---
＜smartgroup-id＞|<作用>可选参数，链路聚合组组号，如果携带该参数表示需要查看某个聚合组的当前配置和状态，否则表示查看所有聚合组的当前配置和状态。<取值范围>$#83951634#$~$#83951635#$，如果项目通过性能参数设置了最小值和最大值，则范围是项目性能参数值（最小值）~项目性能参数值（最大值)。
counters|<作用>查看成员口LACP收发包状态。
internal|<作用>显示成员口的聚合状态。
neighbors|<作用>查看对端邻居的成员口状态。
mc-lag|<作用>查看mc-lag相关的信息
sys-id|<作用>查看LACP系统优先级和系统MAC。








缺省 :

 无 






使用说明 :

携带<smartgroup-id>参数，表示需要查看某个聚合组当前的配置和状态。不携带<smartgroup-id>参数，表示查看系统所有聚合组当前的配置和状态。





范例 :

查看所有成员口的收发包状态：ZXROSNG(config-lacp)#show lacp counters Smartgroup:1Actor         LACPDUs               Marker    LACPDUs    MarkerPort          Tx         Rx         Tx  Rx    Err        Err-------------------------------------------------------------------gei-0/1/0/5   15         10         0   0     0          0gei-0/1/0/6   14         10         0   0     0          0Smartgroup:2Actor         LACPDUs               Marker    LACPDUs    MarkerPort          Tx         Rx         Tx  Rx    Err        Err-------------------------------------------------------------------gei-0/1/0/7   3          4          0   0     0          0查看某个smartgroup的所有成员口的收发包状态：ZXROSNG(config-lacp)#show lacp 1 counters               Smartgroup:1Actor         LACPDUs               Marker    LACPDUs    MarkerPort          Tx         Rx         Tx  Rx    Err        Err-------------------------------------------------------------------gei-0/1/0/5   17         12         0   0     0          0gei-0/1/0/6   16         12         0   0     0          0查看所有成员口的聚合状态：ZXROSNG(config-lacp)#show lacp internal Smartgroup:1Flags:              * - Port is Active member Port                    S - Port is requested in Slow LACPDUs                    F - Port is requested in Fast LACPDUs                       A - Port is in Active mode                                 P - Port is in Passive mode      Actor               Agg      LACPDUs  Port  Oper   Port  RX            MuxPort[Flags]         State    Interval Pri   Key    State Machine       Machine--------------------------------------------------------------------------------gei-0/1/0/5[SA*]    ACTIVE   30       32768 0x109  0x3d  CURRENT       COLL&DISTgei-0/1/0/6[SA*]    ACTIVE   30       32768 0x109  0x3d  CURRENT       COLL&DISTSmartgroup:2Flags:              * - Port is Active member Port                    S - Port is requested in Slow LACPDUs                    F - Port is requested in Fast LACPDUs                       A - Port is in Active mode                                 P - Port is in Passive mode      Actor               Agg      LACPDUs  Port  Oper   Port  RX            MuxPort[Flags]         State    Interval Pri   Key    State Machine       Machine--------------------------------------------------------------------------------gei-0/1/0/7[SA*]    ACTIVE   30       32768 0x209  0x3d  CURRENT       COLL&DIST查看某个smartgroup的成员口的聚合状态：ZXROSNG(config-lacp)#show lacp 1 internal               Smartgroup:1Flags:              * - Port is Active member Port                    S - Port is requested in Slow LACPDUs                    F - Port is requested in Fast LACPDUs                       A - Port is in Active mode                                 P - Port is in Passive mode      Actor               Agg      LACPDUs  Port  Oper   Port  RX            MuxPort[Flags]         State    Interval Pri   Key    State Machine       Machine--------------------------------------------------------------------------------gei-0/1/0/5[SA*]    ACTIVE   30       32768 0x109  0x3d  CURRENT       COLL&DISTgei-0/1/0/6[SA*]    ACTIVE   30       32768 0x109  0x3d  CURRENT       COLL&DIST查看所有对端邻居的成员口状态：ZXROSNG(config-lacp)#show lacp neighbors                Smartgroup 1  neighborsActor         Partner               Partner   Port      Oper    Port     Port          System ID             Port No.  Priority  Key     State   ----------------------------------------------------------------------gei-0/1/0/5   0x8000,0019.8407.2310 14        32768     0x109   0x3dgei-0/1/0/6   0x8000,0019.8407.2310 15        32768     0x109   0x3dSmartgroup 2  neighborsActor         Partner               Partner   Port      Oper    Port     Port          System ID             Port No.  Priority  Key     State   ----------------------------------------------------------------------gei-0/1/0/7   0x8000,0019.8407.2310 16        32768     0x209   0x3d查看某个smartgroup的对端邻居的成员口状态：ZXROSNG(config-lacp)#show lacp 1 neighbors              Smartgroup 1  neighborsActor         Partner               Partner   Port      Oper    Port     Port          System ID             Port No.  Priority  Key     State   ----------------------------------------------------------------------gei-0/1/0/5   0x8000,0019.8407.2310 14        32768     0x109   0x3dgei-0/1/0/6   0x8000,0019.8407.2310 15        32768     0x109   0x3d查看mc-lag相关的信息：ZXROSNG#show lacp mc-lagSmartgroup id:              1Mc-lag iccp id:             0Mc-lag priority:            32768Mc-lag sys-priority:        0Mc-lag sys-mac:             0000.0000.0000Mc-lag restore mode:        MCLAG_IMMEDIATELY_MODEMc-lag restore delay time:  0Mc-lag mode:                AutoMc-lag work-mode:           N/AMc-lag roid:                0Mc-lag node-id:             0Mc-lag state:               NONEMc-lag actor smartgroup state:   DOWNMc-lag partner smartgroup state: UNKNOWN查看LACP系统优先级和系统MAC：ZXROSNG(config-lacp)#show lacp sys-id Actor System Priority: 32768     Actor System ID: 0019.8407.2300





相关命令 :

无 




## smartgroup 


smartgroup 




命令功能 :

该命令工作于LACP成员接口模式，用于将成员接口添加到链路聚合组，并设置接口的链路聚合模式。 






命令模式 :

 LACP成员接口模式  






命令默认权限级别 :

15 






命令格式 :



smartgroup 
  ＜smartgroup-id 
＞ mode 
 {passive 
|active 
|on 
}

no smartgroup 








命令参数解释 :



参数|描述
---|---
＜smartgroup-id＞|<作用>链路聚合组号。<取值范围>最大值由项目性能参数设置，平台默认最大值为64，默认范围1–$#83951617#$
passive|<作用>配置接口的LACP处于被动协商模式。
active|<作用>指接口的LACP处于主动协商模式
on|<作用>指静态trunk，此时不运行LACP，聚合的两端都需要设置成on模式








缺省 :

无 






使用说明 :

接口的聚合模式必须要与要加入的聚合组的聚合模式一致，否则不允许加入。可使用no命令把相应接口从链路聚合组删除。 






范例 :

配置链路聚合组号为3，接口的链路聚合模式为被动协商模式：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/8ZXROSNG(config-lacp-member-if-gei-0/1/0/8)#smartgroup 3 mode passive配置链路聚合组号为3，接口的链路聚合模式为主动协商模式：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/8ZXROSNG(config-lacp-member-if-gei-0/1/0/8)#smartgroup 3 mode active配置链路聚合组号为3，接口的链路聚合模式为静态trunk：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/8ZXROSNG(config-lacp-member-if-gei-0/1/0/8)#smartgroup 3 mode on将成员口从聚合组中解除绑定：ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/8ZXROSNG(config-lacp-member-if-gei-0/1/0/8)#no smartgroup






相关命令 :

无 




track :

track 




命令功能 :

配置LACP的成员关联SAMGR的track name，可以通过track name关联检测机制，来快速感知链路的状态变化。 






命令模式 :

 LACP成员接口模式  






命令默认权限级别 :

15 






命令格式 :



track 
  ＜track-name 
＞

no track 








命令参数解释 :



参数|描述
---|---
＜track-name＞|<参数>Smartgroup成员口关联的SAMGR的track name








缺省 :

无 






使用说明 :

在成员口模式下关联SAMGR的track name。no命令解除与SAMGR的关联。 






范例 :

ZXROSNG(config)#lacpZXROSNG(config-lacp)#interface gei-0/1/0/1ZXROSNG(config-lacp-member-if-gei-0/1/0/1)#track zte






相关命令 :

无 




# SuperVLAN配置命令 
## arp-broadcast 


arp-broadcast 




命令功能 :

使能或关闭SuperVLAN向其包含的所有成员接口进行ARP广播功能 






命令模式 :

 SuperVLAN聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



arp-broadcast 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启SuperVLAN向其所有成员的ARP广播功能
disable|关闭SuperVLAN向其所有成员的ARP广播功能








缺省 :

关闭SuperVLAN向其包含的所有成员接口进行ARP广播功能 






使用说明 :

SuperVLAN接口创建时，会默认开启该接口下的所有开关默认状态信息。缺省时，关闭SuperVLAN向其包含的所有成员接口进行ARP广播功能。若成员没有配置IP-POOL，建议开启该状态，即arp-broadcast enable。通过show running-config supervlan和show supervlan可以查看该开关的状态信息。





范例 :

创建SuperVLAN接口，开启SuperVLAN的arp-broadcastZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface supervlan10ZXROSNG(config-supervlan-superif)#arp-broadcast enableshow running-config查看配置值是否写数据库：ZXROSNG(config-supervlan-superif)#show running-config supervlan!<supervlan>supervlan  interface supervlan10    arp-broadcast enable    inter-subvlan-routing enable  $$!</supervlan>show supervlan查看协议实体数据是否生效ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast             : Enable     Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable----------------------------------------
关闭SuperVLAN的arp-broadcast，即恢复为默认配置ZXROSNG(config-supervlan-superif)#arp-broadcast disableshow running-config all查看配置值是否恢复为默认值：ZXROSNG(config-supervlan-superif)#show running-config supervlan all!<supervlan>supervlan  interface supervlan10    #arp-broadcast disable    #gratuitous-arp-broadcast enable    #inter-subvlan-routing enable    #ip-pool-filter enable    #ipv6-pool-filter enable    #nd-broadcast disable  $$!</supervlan>show supervlan查看协议实体数据是否也恢复为默认配置ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable----------------------------------------






相关命令 :

show supervlan 




## gratuitous-arp-broadcast 


gratuitous-arp-broadcast 




命令功能 :

使能或关闭SubVLAN向其包含的所有物理接口进行免费ARP广播功能。 






命令模式 :

 SuperVLAN-SubVLAN模式  






命令默认权限级别 :

15 






命令格式 :



gratuitous-arp-broadcast 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启SubVLAN向其所有物理接口的免费ARP广播功能
disable|关闭SubVLAN向其所有物理接口的免费ARP广播功能








缺省 :

打开SubVLAN向其所有物理接口的免费ARP广播 






使用说明 :

SubVLAN接口创建时，会默认开启该接口下的所有开关默认状态信息。缺省时，开启SubVLAN向其包含的所有物理接口进行免费ARP广播功能。配置该开关时，需要首先将SubVLAN绑入SuperVLAN。通过show running-config supervlan可以查看该开关的状态信息。





范例 :

创建SuperVLAN接口，SuperVLAN与SubVLAN绑定后，配置gratuitous-arp-broadcastZXROSNG(config)#switchvlan-configuration ZXROSNG(config-swvlan)#vlan 10ZXROSNG(config-swvlan-sub-10)#!ZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#exZXROSNG(config)#supervlanZXROSNG(config-supervlan)#subvlan 10ZXROSNG(config-supervlan-subvlan)#supervlan 10ZXROSNG(config-supervlan-subvlan)#gratuitous-arp-broadcast disableshow running-config查看配置值是否写数据库：ZXROSNG(config-supervlan-superif)#show running-config supervlan!<supervlan>supervlan  interface supervlan10    inter-subvlan-routing enable  $  subvlan 10    supervlan 10    gratuitous-arp-broadcast disable  $$!</supervlan>
创建SuperVLAN接口，SuperVLAN与SubVLAN不进行绑定，配置gratuitous-arp-broadcastZXROSNG(config)#switchvlan-configuration ZXROSNG(config-swvlan)#vlan 10ZXROSNG(config-swvlan-sub-10)#!ZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#exZXROSNG(config)#supervlanZXROSNG(config-supervlan)#subvlan 10ZXROSNG(config-supervlan-subvlan)#gratuitous-arp-broadcast disable%Error 11591: Please bind this interface to supervlan first将gratuitous-arp-broadcast enable，即恢复为默认值ZXROSNG(config-supervlan-subvlan)#gratuitous-arp-broadcast enable通过show running-config supervlan all查看是否恢复为默认值ZXROSNG(config-supervlan-subvlan)#show running-config supervlan all!<supervlan>supervlan  interface supervlan10    #arp-broadcast disable    #gratuitous-arp-broadcast enable    #inter-subvlan-routing enable    #ip-pool-filter enable    ipv6-pool-filter disable    #nd-broadcast disable  $  subvlan 10    supervlan 10    #gratuitous-arp-broadcast enable    #ipv6-dad enable  $$!</supervlan>






相关命令 :

show running-config supervlan 




interface :

interface (SuperVLAN模式) 




命令功能 :

模式跳转，从SUPERVLAN配置模式进入SUPERVLAN聚合接口配置模式或者SUPERVLAN_SUB_INTERFACE模式 






命令模式 :

 SuperVLAN模式  






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
＜interface-byname＞|接口别名，该接口别名必须已经创建
＜interface-name＞|接口名字，该接口已经创建








缺省 :

无 






使用说明 :

本命令只适用于M6000\M6000-S\ZSR系列产品。该命令用于模式跳转。进入SuperVLAN聚合接口模式的接口支持SuperVLAN类型。进入SuperVLAN成员接口模式的接口支持以太接口，ULEI接口，smartgroup接口，BVI接口；以太子接口，ULEI子接口，smartgroup子接口和BVI子接口。以上支持的接口均支持别名跳转。该命令用于从SuperVLAN模式进入SuperVLAN聚合接口模式和SuperVLAN成员接口模式。





范例 :

创建supervlan10，然后进入supervlan10的聚合接口模式。ZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface supervlan10ZXROSNG(config-supervlan-superif)#如果没有创建supervlan10，在SuperVLAN模式下输入interface supervlan10，会出现如下错误。ZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface supervlan10%Error 1001: No such interface.创建smartgroup10，然后进入SuperVLAN成员接口模式。ZXROSNG(config)#interface smartgroup10ZXROSNG(config-if-smartgroup10)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface smartgroup10ZXROSNG(config-supervlan-subif)#如果没有创建smartgroup10，在SuperVLAN模式下输入interface smartgroup10，会出现如下错误。ZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface smartgroup10%Error 1001: No such interface.输入以太接口，然后进入SuperVLAN成员接口模式。ZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface gei-0/1/0/1ZXROSNG(config-supervlan-subif)#在项目支持的版本上创建ulei接口，然后进入SuperVLAN成员接口模式。ZXROSNG(config)#interface ulei-0/1/1/1ZXROSNG(config-if-ulei-0/1/1/1)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface ulei-0/1/1/1ZXROSNG(config-supervlan-subif)#在项目支持的版本上创建bvi接口，然后进入SuperVLAN成员接口模式。ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface bvi1ZXROSNG(config-supervlan-subif)#创建以太子接口，然后进入SuperVLAN成员接口模式。ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface gei-0/1/0/1.1ZXROSNG(config-supervlan-subif)#以别名的方式进入SuperVLAN成员接口模式ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#byname gei-1.1ZXROSNG(config-if-gei-0/1/0/1.1)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface byname gei-1.1ZXROSNG(config-supervlan-subif)#以别名的方式进入SuperVLAN聚合接口模式ZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#byname su10ZXROSNG(config-if-supervlan10)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface byname su10ZXROSNG(config-supervlan-superif)#





相关命令 :

无 




## inter-subvlan-routing 


inter-subvlan-routing 




命令功能 :

使能或关闭SuperVLAN成员接口/子VLAN之间的子网路由功能。 






命令模式 :

 SuperVLAN聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



inter-subvlan-routing 
  {disable 
|enable 
 [{ipv4 
|ipv6 
}]}







命令参数解释 :



参数|描述
---|---
disable|关闭子VLAN之间的路由功能
enable|使能子VLAN之间的IPv4和IPv6路由功能
ipv4|使能子VLAN之间IPv4路由功能，需要结合enable一起使用
ipv6|使能子VLAN之间IPv6路由功能，需要结合enable一起使用








缺省 :

使能子VLAN之间的IPv4和IPv6路由功能 






使用说明 :

SuperVLAN接口创建时，会默认开启该接口下的所有开关默认状态信息。缺省时，开启SuperVLAN向其包含的所有成员接口/子VLAN的子网路由功能，适用于IPv4和IPv6协议。针对IPv4和IPv6，可以通过该命令单独开启IPv4和IPv6。通过show running-config supervlan和show supervlan可以查看该开关的状态信息。该命令的特殊性，默认值在show running-config supervlan的时候也会显示出来。





范例 :

创建SuperVLAN接口，关闭SuperVLAN的inter-subvlan-routingZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface supervlan10ZXROSNG(config-supervlan-superif)#inter-subvlan-routing disableshow running-config查看配置值是否写数据库：ZXROSNG(config-supervlan-superif)#show running-config supervlan!<supervlan>supervlan  interface supervlan10    inter-subvlan-routing disable  $$!</supervlan>show supervlan查看协议实体数据是否生效ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Disable    Inter-SubVLAN-Routing-IPv6: Disable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable----------------------------------------
开启SuperVLAN的inter-subvlan-routing的IPv4子网路由功能 ZXROSNG(config-supervlan-superif)#inter-subvlan-routing enable ipv4show running-config查看配置值是否写数据库：ZXROSNG(config-supervlan-superif)#show running-config supervlan!<supervlan>supervlan  interface supervlan10    inter-subvlan-routing enable ipv4  $$!</supervlan>show supervlan查看协议实体数据是否生效ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Disable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable----------------------------------------
开启SuperVLAN的inter-subvlan-routing，即恢复为默认配置ZXROSNG(config-supervlan-superif)#inter-subvlan-routing enableshow running-config all查看配置值是否恢复为默认值：ZXROSNG(config-supervlan-superif)#show running-config supervlan all!<supervlan>supervlan  interface supervlan10    #arp-broadcast disable    #gratuitous-arp-broadcast enable    #inter-subvlan-routing enable    #ip-pool-filter enable    #ipv6-pool-filter enable    #nd-broadcast disable  $$!</supervlan>show supervlan查看协议实体数据是否也恢复为默认配置ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable ND-Broadcast                  : Disable----------------------------------------






相关命令 :

show supervlan 




## ip-pool-filter 


ip-pool-filter 




命令功能 :

使能或关闭SuperVLAN对源IPv4地址的过滤功能。 






命令模式 :

 SuperVLAN聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



ip-pool-filter 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启SuperVLAN的源IPv4地址过滤功能
disable|关闭SuperVLAN的源IPv4地址过滤功能








缺省 :

使能SuperVLAN的IPv4-POOL过滤功能 






使用说明 :

SuperVLAN接口创建时，会默认开启该接口下的所有开关默认状态信息。缺省时，开启SuperVLAN对源IPv4地址的过滤功能。若成员没有配置IP-POOL，建议关闭该状态，即ip-pool-filter disable。通过show running-config supervlan和show supervlan可以查看该开关的状态信息。





范例 :

创建SuperVLAN接口，关闭SuperVLAN的ip-pool-filterZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface supervlan10ZXROSNG(config-supervlan-superif)#ip-pool-filter disableshow running-config查看配置值是否写数据库：ZXROSNG(config-supervlan-superif)#show running-config supervlan!<supervlan>supervlan  interface supervlan10    inter-subvlan-routing enable    ip-pool-filter disable  $$!</supervlan>show supervlan查看协议实体数据是否生效ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast             : Enable     Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Disable    ND-Broadcast              : Disable----------------------------------------
开启SuperVLAN的ip-pool-filter，即恢复为默认配置ZXROSNG(config-supervlan-superif)#ip-pool-filter enableshow running-config all查看配置值是否恢复为默认值：ZXROSNG(config-supervlan-superif)#show running-config supervlan all!<supervlan>supervlan  interface supervlan10    #arp-broadcast disable    #gratuitous-arp-broadcast enable    #inter-subvlan-routing enable    #ip-pool-filter enable    #ipv6-pool-filter enable    #nd-broadcast disable  $$!</supervlan>show supervlan查看协议实体数据是否也恢复为默认配置ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast               : Disable    Gratuitous-ARP-Broadcast    : Enable     Inter-SubVLAN-Routing-IPv4  : Enable    Inter-SubVLAN-Routing-IPv6  : Enable    IP-POOL-Filter              : Enable     ND-Broadcast                : Disable----------------------------------------






相关命令 :

show supervlan 




## nd-broadcast 


nd-broadcast 




命令功能 :

使能或关闭SuperVLAN向其包含的所有成员接口进行ND广播功能。 






命令模式 :

 SuperVLAN聚合接口模式  






命令默认权限级别 :

15 






命令格式 :



nd-broadcast 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|开启SuperVLAN向其所有成员的ND广播功能
disable|关闭SuperVLAN向其所有成员的ND广播功能








缺省 :

不允许向其包含的所有成员接口进行ND广播 






使用说明 :

SuperVLAN接口创建时，会默认开启该接口下的所有开关默认状态信息。缺省时，关闭SuperVLAN向其包含的所有成员接口进行ND广播功能。路由设备，若要实现ND代理，必须开启该状态，即nd-broadcast enable。交换设备，若成员没有配置IPv6-POOL，建议开启该状态，即nd-broadcast enable。通过show running-config supervlan和show supervlan可以查看该开关的状态信息。





范例 :

创建SuperVLAN接口，开启SuperVLAN的nd-broadcastZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#exitZXROSNG(config)#supervlanZXROSNG(config-supervlan)#interface supervlan10ZXROSNG(config-supervlan-superif)#nd-broadcast enableshow running-config查看配置值是否写数据库：ZXROSNG(config-supervlan-superif)#show running-config supervlan!<supervlan>supervlan  interface supervlan10    inter-subvlan-routing enable    nd-broadcast enable  $$!</supervlan>show supervlan查看协议实体数据是否生效ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1    SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable     ND-Broadcast              : Enable ----------------------------------------关闭SuperVLAN的nd-broadcast，即恢复为默认配置ZXROSNG(config-supervlan-superif)#nd-broadcast disableshow running-config all查看配置值是否恢复为默认值：ZXROSNG(config-supervlan-superif)#show running-config supervlan all!<supervlan>supervlan  interface supervlan10    #arp-broadcast disable    #gratuitous-arp-broadcast enable    #inter-subvlan-routing enable    #ip-pool-filter enable    #ipv6-pool-filter enable    #nd-broadcast disable  $$!</supervlan>show supervlan查看协议实体数据是否也恢复为默认配置ZXROSNG(config-supervlan-superif)#show supervlanThe total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast               : Disable    Gratuitous-ARP-Broadcast    : Enable     Inter-SubVLAN-Routing-IPv4  : Enable    Inter-SubVLAN-Routing-IPv6  : Enable    IP-POOL-Filter               : Enable     ND-Broadcast                 : Disable----------------------------------------





相关命令 :

show supervlan 




## show supervlan 


show supervlan 




命令功能 :

显示SuperVLAN的配置信息，包括整机所有存在的SuperVLAN接口数目，SuperVLAN接口的开关状态信息，SuperVLAN与成员接口/SubVLAN的绑定信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show supervlan 
  [＜supervlan-id 
＞] 







命令参数解释 :



参数|描述
---|---
＜supervlan-id＞|SuperVLAN的ID号，范围：1-$#84017922#$








缺省 :

无 






使用说明 :

本命令工作于除用户模式外的所有模式。该命令不带可选参数时，显示整机所有创建的SuperVLAN接口和绑定的信息。输入show supervlan <supervlan-id>，则显示指定SuperVLAN接口的配置信息。





范例 :

显示所有SuperVLAN接口的配置信息。ZXROSNG(config-supervlan)#show supervlanThe total SuperVLAN number:2  SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable    Member count              : 1----------------------------------------      SubIntf  :  gei-0/9/0/11
  SuperVLAN No: 20    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable    Member count              : 0----------------------------------------显示SuperVLAN 10的配置信息。ZXROSNG(config-supervlan)#show supervlan 10The total SuperVLAN number:2  SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable    Member count              : 1----------------------------------------      SubIntf  :  gei-0/9/0/11






相关命令 :

show supervlan-pool 




## show supervlan-pool 


show supervlan-pool 




命令功能 :

显示绑定到SuperVLAN的成员接口/SubVLAN的IPv4-POOL配置信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show supervlan-pool 
  [＜supervlan-id 
＞] [sort-by 
 addr-begin 
] 







命令参数解释 :



参数|描述
---|---
＜supervlan-id＞|SuperVLAN的ID号，范围：1-$#84017922#$
sort-by|指定排序方式
addr-begin|按照起始IP地址排序








缺省 :

无 






使用说明 :

本命令工作于除用户模式外的所有模式。该命令不带可选参数时，显示整机所有创建的SuperVLAN成员接口的IPv4-POOL信息。输入show supervlan-pool <supervlan-id>，则显示指定SuperVLAN成员接口的IPv4-POOL信息。





范例 :

Addr-Begin表示起始地址；Addr-End表示结束地址；SuperVLAN-Name表示SuperVLAN接口名；SubIntf-Name表示成员接口名。显示所有成员接口的IP POOL的配置信息。ZXROSNG(config-supervlan)#show supervlan-poolAddr-Begin       Addr-End       SuperVLAN-Name     SubIntf-Name192.168.1.10     192.168.1.20   supervlan10        gei-0/9/0/11
192.168.1.21     192.168.1.30   supervlan20        gei-0/8/0/11显示SuperVLAN 10成员接口的IP POOL的配置信息。ZXROSNG(config-supervlan)#show supervlan-pool 10Addr-Begin       Addr-End       SuperVLAN-Name     SubIntf-Name192.168.1.10     192.168.1.20   supervlan10        gei-0/9/0/11






相关命令 :

show supervlan 




## subvlan 


subvlan 




命令功能 :

进入SUPERVLAN_SUBVLAN配置模式 






命令模式 :

 SuperVLAN模式  






命令默认权限级别 :

15 






命令格式 :



subvlan 
  ＜subvlan-id 
＞







命令参数解释 :



参数|描述
---|---
＜subvlan-id＞|SubVLAN的ID号，范围：1-4094








缺省 :

无 






使用说明 :

进入SUPERVLAN_SUBVLAN配置模式，使用exit可以退出返回SUPERVLAN配置模式。需要注意，输入的<subvlan-id>对应的三层VLAN逻辑接口不能存在，并且对应的SubVLAN接口必须存在 






范例 :

进入SUPERVLAN_SUBVLAN配置模式。ZXROSNG(config-supervlan)#subvlan 10ZXROSNG(config-supervlan-subvlan)#





相关命令 :

无 




## supervlan 


supervlan 




命令功能 :

将某个接口绑定到指定的SuperVLAN接口；使用no命令从SuperVLAN中解除绑定 






命令模式 :

 SuperVLAN成员接口模式  






命令默认权限级别 :

15 






命令格式 :



supervlan 
  ＜supervlan-id 
＞

no supervlan 








命令参数解释 :



参数|描述
---|---
＜supervlan-id＞|SuperVLAN的ID号，范围：1-$#84017922#$








缺省 :

无 






使用说明 :

输入的SuperVLAN ID对应的SuperVLAN接口必须存在。将该接口/子接口（封装了VLAN信息）绑定某个SuperVLAN接口中；使用no supervlan命令则可以执行解绑操作。通过show running-config supervlan和show supervlan可以查看绑定信息。






范例 :

将gei-0/9/0/11绑入SuperVLAN 10中。ZXROSNG(config-supervlan)#interface gei-0/9/0/11ZXROSNG(config-supervlan-subif)#supervlan 10查看配置信息。ZXROSNG(config-supervlan)#show supervlan 10The total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable----------------------------------------      SubIntf  :  gei-0/9/0/11






相关命令 :

show supervlan 




## supervlan 


supervlan 




命令功能 :

将某个SubVLAN绑定到指定的SuperVLAN接口；使用no命令从SuperVLAN中解除绑定 






命令模式 :

 SuperVLAN-SubVLAN模式  






命令默认权限级别 :

15 






命令格式 :



supervlan 
  ＜supervlan-id 
＞

no supervlan 








命令参数解释 :



参数|描述
---|---
＜supervlan-id＞|SuperVLAN的ID号，范围：1-$#84017922#$








缺省 :

无 






使用说明 :

输入的SuperVLAN ID对应的SuperVLAN接口必须存在。通过show running-config supervlan和show supervlan可以查看绑定信息。





范例 :

将gei-0/9/0/11绑入SuperVLAN 10中。ZXROSNG(config-supervlan)#interface gei-0/9/0/11ZXROSNG(config-supervlan-subif)#supervlan 10查看配置信息。ZXROSNG(config-supervlan)#show supervlan 10The total SuperVLAN number:1  SuperVLAN No: 10    ARP-Broadcast             : Disable    Gratuitous-ARP-Broadcast  : Enable     Inter-SubVLAN-Routing-IPv4: Enable    Inter-SubVLAN-Routing-IPv6: Enable    IP-POOL-Filter            : Enable     ND-Broadcast              : Disable----------------------------------------      SubIntf  :  gei-0/9/0/11






相关命令 :

show supervlan 




## supervlan 


supervlan 




命令功能 :

进入SUPERVLAN配置模式 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



supervlan 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

进入SUPERVLAN配置模式，使用exit可以退出返回全局配置模式 






范例 :

进入SUPERVLAN配置模式。ZXROSNG(config)#supervlanZXROSNG(config-supervlan)#






相关命令 :

无 




## vlanpool 


vlanpool 




命令功能 :

绑定一段IPv4地址到SuperVLAN的某个成员接口上。 






命令模式 :

 SuperVLAN成员接口模式  






命令默认权限级别 :

15 






命令格式 :


vlanpool 
  ＜begin-ip-address 
＞ ＜end-ip-address 
＞
no vlanpool 
  {＜begin-ip-address 
＞ ＜end-ip-address 
＞|all 
}
				






命令参数解释 :



参数|描述
---|---
＜begin-ip-address＞|地址段开始IP地址，十进制点分形式。该地址必须为该成员接口已经配置的IP POOL的起始IP地址
＜end-ip-address＞|地址段结束IP地址，十进制点分形式。该地址必须为该成员接口已经配置的IP POOL的结束IP地址






No参数|描述
---|---
all|所有的IP POOL地址段








缺省 :

无 






使用说明 :

将一段IPv4地址绑入某个成员接口上。配置IPv4-POOL地址段时，特殊地址是不允许配置在成员接口上的。配置IPv4-POOL地址段时，起始地址应该小于结束地址。同一个成员接口上面不允许绑重叠的IPv4地址段。同一个SuperVLAN下的IPv4地址段数目由性能参数控制。整机支持的IPv4地址数目由性能参数控制。整机支持的IPv4-POOL条目数目由性能参数控制，与IPv4地址数目比，哪个先达到性能参数，则不允许配置了。配置IPv4-POOL时，该成员接口必须绑入SuperVLAN中。通过show running-config supervlan和show supervlan-pool可以查看该成员接口/SubVLAN的IP-POOL信息。





范例 :

在gei-0/9/0/11接口上绑定192.168.1.1 - 192.168.1.10、192.168.1.11 – 192.168.1.20和192.168.1.21 – 192.168.1.30三个地址段。ZXROSNG(config-supervlan)#interface gei-0/9/0/11ZXROSNG(config-supervlan-subif)#vlanpool 192.168.1.1 192.168.1.10ZXROSNG(config-supervlan-subif)#vlanpool 192.168.1.11 192.168.1.20ZXROSNG(config-supervlan-subif)#vlanpool 192.168.1.21 192.168.1.30查看配置信息。ZXROSNG(config-supervlan)#show supervlan-poolAddr-Begin       Addr-End       SuperVLAN-Name     SubIntf-Name192.168.1.1      192.168.1.10   supervlan10        gei-0/9/0/11192.168.1.11     192.168.1.20   supervlan10        gei-0/9/0/11192.168.1.21     192.168.1.30   supervlan10        gei-0/9/0/11删除gei-0/9/0/11接口上192.168.1.1 - 192.168.1.10地址段。ZXROSNG(config-supervlan)#interface gei-0/9/0/11ZXROSNG(config-supervlan-subif)#no vlanpool 192.168.1.1 192.168.1.10查看配置信息。ZXROSNG(config-supervlan)#show supervlan-poolAddr-Begin       Addr-End       SuperVLAN-Name     SubIntf-Name192.168.1.11     192.168.1.20   supervlan10        gei-0/9/0/11192.168.1.21     192.168.1.30   supervlan10        gei-0/9/0/11删除gei-0/9/0/11接口上所有的地址段。ZXROSNG(config-supervlan)#interface gei-0/9/0/11ZXROSNG(config-supervlan-subif)#no vlanpool all查看配置信息。ZXROSNG(config-supervlan)#show supervlan-poolZXROSNG(config-supervlan)#






相关命令 :

show supervlan-pool 




## vlanpool 


vlanpool 




命令功能 :

绑定一段IPv4地址到SuperVLAN的某个SubVLAN上。 






命令模式 :

 SuperVLAN-SubVLAN模式  






命令默认权限级别 :

15 






命令格式 :


vlanpool 
  ＜begin-ip-address 
＞ ＜end-ip-address 
＞
no vlanpool 
  {＜begin-ip-address 
＞ ＜end-ip-address 
＞|all 
}
				






命令参数解释 :



参数|描述
---|---
＜begin-ip-address＞|地址段开始IP地址，十进制点分形式。该地址必须为该成员接口已经配置的IP POOL的起始IP地址
＜end-ip-address＞|地址段结束IP地址，十进制点分形式。该地址必须为该成员接口已经配置的IP POOL的结束IP地址






No参数|描述
---|---
all|所有的IP POOL地址段








缺省 :

无 






使用说明 :

将一段IPv4地址绑入某个SubVLAN上。配置IPv4-POOL地址段时，特殊地址是不允许配置在SubVLAN上的。配置IPv4-POOL地址段时，起始地址应该小于结束地址。同一个SubVLAN上面不允许绑重叠的IPv4地址段。同一个SuperVLAN下的IPv4地址段数目由性能参数控制。整机支持的IPv4地址数目由性能参数控制。整机支持的IPv4-POOL条目数目由性能参数控制，与IPv4地址数目比，哪个先达到性能参数，则不允许配置了。配置IPv4-POOL时，该SubVLAN必须绑入SuperVLAN中。通过show running-config supervlan和show supervlan-pool可以查看该成员接口/SubVLAN的IP-POOL信息。





范例 :

创建SuperVLAN接口，SuperVLAN与SubVLAN绑定，配置IPv4-POOLZXROSNG(config)#switchvlan-configuration ZXROSNG(config-swvlan)#vlan 10ZXROSNG(config-swvlan-sub-10)#!ZXROSNG(config)#interface supervlan10ZXROSNG(config-if-supervlan10)#exZXROSNG(config)#supervlanZXROSNG(config-supervlan)#subvlan 10ZXROSNG(config-supervlan-subvlan)#supervlan 10ZXROSNG(config-supervlan-subvlan)#vlanpool 1.1.1.1 1.1.1.10show running-config查看配置值是否写数据库：ZXROSNG(config-supervlan-superif)#show running-config supervlan!<supervlan>supervlan  interface supervlan10    inter-subvlan-routing enable    ipv6-pool-filter disable  $  subvlan 10    supervlan 10    vlanpool 1.1.1.1 1.1.1.10  $$!</supervlan>show supervlan-pool查看协议实体数据是否生效ZXROSNG(config-supervlan-subif)#show supervlan-pool Addr-Begin       Addr-End         SuperVLAN-Name  SubIntf-Name1.1.1.1          1.1.1.10          supervlan10     subvlan10删除成员接口的IPv4-POOL条目ZXROSNG(config-supervlan-subvlan)#no vlanpool 1.1.1.1 1.1.1.10删除成员接口的所有IPv4-POOL条目ZXROSNG(config-supervlan-subvlan)#no vlanpool all






相关命令 :

show supervlan-pool 




# VLAN配置命令 
## clear statistics 


clear statistics 




命令功能 :

该命令工作于特权模式，作用为：通过该命令，清除用户侧PVV链路的流量信息。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear statistics 
  ＜IfName 
＞ exvlan 
 ＜ExVlanId 
＞ [invlan 
 ＜InVlanId 
＞]







命令参数解释 :



参数|描述
---|---
＜IfName＞|用户侧VCC子接口
＜ExVlanId＞|子接口支持的VLAN ID, 范围：1–4094
＜InVlanId＞|子接口支持的VLAN ID, 范围：1–4094








缺省 :

无 






使用说明 :

当子接口封装dot1q或者dot1q range时，命令只需要输入external VLAN即可。若输入接口为父接口，将会提示错误信息表示父接口上不支持显示流量。





范例 :

清除某条电路上的流量信息：ZXROSNG#clear statistics gei-0/1/0/1.1 exvlan 55清除后显示流量信息如下：ZXROSNG#show statistics gei-0/1/0/1.1 exvlan 55In_Bytes:0                               E_Bytes:0                         In_Packets:0                             E_Packets:0                         In_Discards:0                            E_Discards:0





相关命令 :

无 




## encapsulation-dot1q range 


encapsulation-dot1q range 




命令功能 :

为新创建的子接口封装单层VLAN range段标签，使用no命令取消封装。 






命令模式 :

 bvi子接口模式,eth_dslgroup子接口模式,gtunnel_group子接口模式,irb子接口模式,l3vi子接口模式,ptp子接口模式,smartgroup子接口模式,te_gtunnel子接口模式,ulei子接口模式,以太子接口模式  






命令默认权限级别 :

ptp子接口模式:15,bvi子接口模式:15,以太子接口模式:15,eth_dslgroup子接口模式:15,smartgroup子接口模式:15,ulei子接口模式:15,l3vi子接口模式:15,gtunnel_group子接口模式:15,te_gtunnel子接口模式:15,irb子接口模式:15 






命令格式 :


encapsulation-dot1q range 
  ＜vlan-range 
＞
no encapsulation-dot1q range 
  ＜vlan-range 
＞
				






命令参数解释 :



参数|描述
---|---
＜vlan-range＞|子接口支持的VLAN ID段, 范围：1–4094








缺省 :

无 






使用说明 :

在该子接口配置了VPN，ACL，NAT，QoS等属性后，在没有去掉上述属性之前，是不允许去掉封装（no命令）或改变封装的。新创建的子接口必须封装VLAN-ID号，否则该子接口不能收发报文，使用no命令，删除子接口下配置的VLAN信息，此时不能收发报文。同一个子接口下配置的VLAN range段，最多支持256段。同一接口下的子接口不能配置重叠的VLAN。不能跟dot1q、QinQ、QinQ range混配。






范例 :

配置命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#encapsulation-dot1q range 1-20通过show run命令查看：ZXROSNG(config)#show running-config vlan!<vlan>vlan-configurationinterface bvi1.1encapsulation-dot1q range 1-20  encapsulation-dot1q range 30-40$$!</vlan>删除所有的单层VLAN range段：ZXROSNG(config-if-bvi1.1)#no encapsulation-dot1q range allZXROSNG(config)#show running-config vlan





相关命令 :

show interface-vlan dot1q [<interface-name>] 




## encapsulation-dot1q range 


encapsulation-dot1q range 




命令功能 :

为新创建的子接口封装VLAN-ID号，使用no命令取消封装。 






命令模式 :

 VLAN子接口模式  






命令默认权限级别 :

15 






命令格式 :


encapsulation-dot1q range 
  ＜vlan-range 
＞
no encapsulation-dot1q range 
  {all 
|＜vlan-range 
＞}
				






命令参数解释 :



参数|描述
---|---
＜vlan-range＞|子接口支持的VLAN ID, 范围：1–4094






No参数|描述
---|---
all|删除所有VLAN range段








缺省 :

无 






使用说明 :

在该子接口配置了VPN，ACL，NAT，QoS等属性后，在没有去掉上述属性之前，是不允许去掉封装（no命令）或改变封装的。新创建的子接口必须封装VLAN-ID号，否则该子接口不能收发报文，使用no命令，删除子接口下配置的VLAN信息，此时不能收发报文。同一个子接口下配置的VLAN range段，最多支持256段。同一接口下的子接口不能配置重叠的VLAN。不能跟dot1q、QinQ、QinQ range混配。接口绑入vpls/vpws/vlss实例，并且接口的兄弟接口配置了动态qinq，并且qinq的外层VLAN和本配置的VLAN范围存在重叠，存在互斥；





范例 :

配置命令如下：ZXROSNG(config-vlan)#interface gei-0/1/0/1.1ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#encapsulation-dot1q range 1-20通过show run命令查看：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan!<vlan>vlan-configurationinterface gei-0/1/0/1.1encapsulation-dot1q range 1-20  encapsulation-dot1q range 30-40$$!</vlan>删除所有的单层VLAN range段：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#no encapsulation-dot1q range allZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan





相关命令 :

show interface-vlan dot1q [<interface-name>] 




## encapsulation-dot1q 


encapsulation-dot1q 




命令功能 :

该命令工作于VLAN子接口模式下，为创建的子接口封装VLAN，使用no命令取消封装。 






命令模式 :

 VLAN子接口模式  






命令默认权限级别 :

15 






命令格式 :



encapsulation-dot1q 
  ＜vlanid 
＞

no encapsulation-dot1q 








命令参数解释 :



参数|描述
---|---
＜vlanid＞|子接口支持的VLAN ID, 范围：1–4094








缺省 :

无 






使用说明 :

该命令用于在VLAN子接口模式下配置VLAN。在该子接口配置了VPN，ACL，NAT，QoS等属性后，在没有去掉上述属性之前，不允许去掉封装（no命令）或改变封装。新创建的子接口必须封装VLAN-ID号，否则该子接口不能收发报文，使用no命令，删除子接口下配置的VLAN信息，此时不能收发报文。不能跟dot1q range、QinQ、QinQ range混配。同一个接口上的子接口不能配置相同的VLAN。接口绑入vpls/vpws/vlss实例，并且接口的兄弟接口配置了动态qinq，并且qinq的外层VLAN和本配置的VLAN范围存在重叠，存在互斥；





范例 :

配置命令如下：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#encapsulation-dot1q 1通过show run命令查看：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan!<vlan>vlan-configuration  interface gei-0/1/0/1.1    encapsulation-dot1q 1  $$!</vlan>






相关命令 :

show interface-vlan dot1q [<interface-name>] 




interface :

interface (VLAN模式) 




命令功能 :

该命令工作于VLAN模式下，用于进入VLAN子接口模式。 






命令模式 :

 VLAN模式  






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
＜interface-byname＞|子接口别名
＜interface-name＞|子接口名称








缺省 :

无 






使用说明 :

该命令工作于VLAN模式下，用于进入VLAN子接口模式。 






范例 :

创建接口别名，并通过接口别名和接口名称从VLAN配置模式进入VLAN子接口模式，则输入以下命令：ZXROSNG(config)# interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#byname gei-1.1ZXROSNG(config-vlan)#interface gei-0/1/0/1.1ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#ZXROSNG(config-vlan)#interface byname fei1.1ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#





相关命令 :

无 




## pid-tag 


pid-tag 




命令功能 :

为新创建的子接口封装TPID，使用no命令取消封装。 






命令模式 :

 VLAN子接口模式  






命令默认权限级别 :

15 






命令格式 :



pid-tag 
  {[external 
 ＜external-tpid-value 
＞],[internal 
 ＜internal-tpid-value 
＞]}

no pid-tag 








命令参数解释 :



参数|描述
---|---
＜external-tpid-value＞|子接口支持的外层Tpid封装类型，分为88a8、88e8、8100、9100、9200、9300
＜internal-tpid-value＞|子接口支持的内层Tpid封装类型，分为88a8、88e8、8100、9100、9200、9300








缺省 :

内层8100，外层8100 






使用说明 :

子接口封装了VLAN ID后，TPID才会生效。TPID可以单独配置外层或者内层，也可以内层、外层同时配。对于封装dot1q或者dot1q range的子接口只对配置的外层TPID生效，即使同时配置了内外层TPID时，生效的只有外层TPID；若只配置了内层TPID，配置的TPID是无效的，此时外层TPID取默认值。TPID的默认值说明：封装dot1q或者dot1q range的子接口的TPID的默认值为8100，封装QinQ或者QinQ range的子接口的TPID的默认值外层为8100，内层为8100。同时配置TPID的内外层时，不能使用9200和9300同时配置。即内层9200外层9300或外层9200内层9300，这样是非法的，会提示错误。





范例 :

配置命令如下：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#pid-tag internal 9100 external 9200通过show run命令查看：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan!<vlan>vlan-configuration  interface gei-0/1/0/1.1    pid-tag external 9200 internal 9100    encapsulation-dot1q 1  $$!</vlan>通过no命令删除tpid：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#no pid-tagZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan!<vlan>vlan-configuration  interface gei-0/1/0/1.1    encapsulation-dot1q 1  $$!</vlan>





相关命令 :

show interface-vlan dot1q [<interface-name>]show interface-vlan qinq [<interface-name>]




## qinq range 


qinq range 




命令功能 :

为新创建的子接口封装内外层VLAN range段标签，使用no命令取消封装。 






命令模式 :

 bvi子接口模式,eth_dslgroup子接口模式,gtunnel_group子接口模式,irb子接口模式,l3vi子接口模式,ptp子接口模式,smartgroup子接口模式,te_gtunnel子接口模式,ulei子接口模式,以太子接口模式  






命令默认权限级别 :

ptp子接口模式:15,ulei子接口模式:15,eth_dslgroup子接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,bvi子接口模式:15,l3vi子接口模式:15,gtunnel_group子接口模式:15,te_gtunnel子接口模式:15,irb子接口模式:15 






命令格式 :


qinq range 
 internal-vlan-range 
 ＜internal-vlan-range 
＞ external-vlan-range 
 ＜external-vlan-range 
＞
no qinq range 
 internal-vlan-range 
 ＜internal-vlan-range 
＞ external-vlan-range 
 ＜external-vlan-range 
＞
				






命令参数解释 :



参数|描述
---|---
＜internal-vlan-range＞|子接口支持的内层VLAN ID段, 范围：1–4094
＜external-vlan-range＞|子接口支持的外层VLAN ID段, 范围：1–4094








缺省 :

无 






使用说明 :

新创建的子接口必须封装VLAN-ID号，否则该子接口不能收发报文，使用no命令，删除子接口下配置的VLAN信息，此时不能收发报文。不能跟dot1q、dot1q range、QinQ 混配。同一个接口子接口不能配置内外层同时重叠的VLAN。





范例 :

配置命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#qinq range internal-vlan-range 1-10 external-vlan-range 1-20通过show run命令查看：ZXROSNG(config)#show running-config vlan!<vlan>vlan-configurationinterface bvi1.1qinq range internal-vlan-range 1-10 external-vlan-range 1-20$$!</vlan>





相关命令 :

show interface-vlan qinq [<interface-name>] 




## qinq range 


qinq range 




命令功能 :

为创建的子接口封装内外层 VLAN range标签，使用no命令取消封装。 






命令模式 :

 VLAN子接口模式  






命令默认权限级别 :

15 






命令格式 :


qinq range 
 internal-vlan-range 
 ＜internal-vlan-range 
＞ external-vlan-range 
 ＜external-vlan-range 
＞
no qinq range 
  {internal-vlan-range 
 ＜internal-vlan-range 
＞ external-vlan-range 
 ＜external-vlan-range 
＞|all 
}
				






命令参数解释 :



参数|描述
---|---
＜internal-vlan-range＞|子接口支持的VLAN ID, 范围：1–4094
＜external-vlan-range＞|子接口支持的VLAN ID, 范围：1–4094






No参数|描述
---|---
all|删除所有VLAN range段








缺省 :

无 






使用说明 :

新创建的子接口必须封装VLAN-ID号，否则该子接口不能收发报文，使用no命令，删除子接口下配置的VLAN信息，此时不能收发报文。不能跟dot1q、dot1q range、QinQ 混配。同一个接口子接口不能配置内外层同时重叠的VLAN。接口配置动态qinq，该接口的兄弟接口绑入了vpls/vpws/vlss,并且配置了dot1q或者dot1q range类型的VLAN,并且VLAN范围和动态qinq的外层VLAN范围存在重叠，存在互斥；





范例 :

配置命令如下：ZXROSNG(config-vlan)#interface gei-0/1/0/1.1ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#qinq range internal-vlan-range 1-10 external-vlan-range 1-20通过show run命令查看：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan!<vlan>vlan-configurationinterface gei-0/1/0/1.1qinq range internal-vlan-range 1-10 external-vlan-range 1-20$$!</vlan>删除所有的双层VLAN range段：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#no qinq range allZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan





相关命令 :

show interface-vlan qinq [<interface-name>] 




## qinq 


qinq 




命令功能 :

配置子接口内外层VLAN ID，使用no命令取消封装。 






命令模式 :

 VLAN子接口模式  






命令默认权限级别 :

15 






命令格式 :



qinq 
 internal-vlanid 
 ＜internal-vlanid 
＞ external-vlanid 
 ＜external-vlanid 
＞

no qinq 








命令参数解释 :



参数|描述
---|---
＜internal-vlanid＞|子接口支持的内层VLAN ID, 范围：1–4094
＜external-vlanid＞|子接口支持的外层VLAN ID, 范围：1–4094








缺省 :

无 






使用说明 :

新创建的子接口必须封装VLAN-ID号，否则该子接口不能收发报文，使用no命令，删除子接口下配置的VLAN信息，此时不能收发报文。同一接口下的子接口内外层标签不能同时有重叠。不能跟dot1q、dot1q range、QinQ range、untag混配。





范例 :

配置命令如下：ZXROSNG(config)# vlan-configurationZXROSNG(config-vlan)#interface  gei-0/1/0/1.1ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#qinq internal-vlanid 1 external-vlanid 1通过show run命令进行查看如下：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan!<vlan>vlan-configuration  interface gei-0/1/0/1.1    qinq internal-vlanid 1 external-vlanid 1  $$!</vlan>






相关命令 :

show interface-vlan qinq [<interface-name>] 




## show interface-vlan dot1q 


show interface-vlan dot1q 




命令功能 :

该命令工作于除用户模式外的其它所有模式，作用为：显示所有子接口或者某个子接口下的VLAN dot1q配置信息。  






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show interface-vlan dot1q 
  [＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称，用于指定需要显示的接口。








缺省 :

无 






使用说明 :

显示该接口下的配置的VLAN dot1q配置信息。如果show命令后不加接口名，则表现显示所有接口的VLAN dot1q配置信息。针对bras项目，子接口上配置any-other-VLAN dot1q类型标记，使用该命令能够显示对应的配置。如果配置了encapsulation untag，使用该命令显示对应的配置。子接口上配置NNI VLAN，使用该命令能够显示对应的配置。如果show命令后加父接口名，遍历该父接口的所有子接口进行显示。






范例 :

该命令执行及结果如下：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show interface-vlan dot1qinterface: gei-0/1/0/1.1exter-tpid: 0x8100, inter-tpid: 0x8100untag: permittedVLAN range:    1 - 200VLAN range:  301 - 500interface: gei-0/1/0/1.2exter-tpid: 0x8100, inter-tpid: 0x8100VLAN ID: NNI 1000, leaf VLAN ID:2000ZXROSNG(config-vlan)#show interface-vlan dot1q smartgroup3interface: smartgroup3.1exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range:    3000 - 3001, exter-VLAN range:    2000-2001interface: smartgroup3.2exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range:    4000 - 4001, exter-VLAN range:    4000-4001






相关命令 :

无 




## show interface-vlan qinq 


show interface-vlan qinq 




命令功能 :

该命令工作于除用户模式外的其它所有模式，作用为：显示所有子接口或者某个子接口下的QinQ配置信息。  






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show interface-vlan qinq 
  [＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称，用于指定需要显示的接口。








缺省 :

无 






使用说明 :

显示该接口下的配置的 QinQ配置信息。如果show命令后不加接口名，则表现显示所有接口的QinQ配置信息。针对bras项目，子接口上配置any-other-VLAN QINQ类型标记，使用该命令能够显示对应的配置。子接口上配置QinQ any配置，使用该命令能够显示对应的配置。如果show命令后加父接口名，遍历该父接口的所有子接口进行显示。






范例 :

该命令执行及结果如下：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show interface-vlan qinq  interface: gei-0/1/0/1.1           exter-tpid: 0x8100, inter-tpid: 0x8100           inter-VLAN range:    1 - 200, exter-VLAN range:    1 - 3           inter-VLAN range:  200 - 201, exter-VLAN range:   11 - 3000接口配置了QinQ any配置，该命令执行及结果如下：ZXROSNG(config)#show interface-vlan qinq interface: smartgroup1.1           exter-tpid: 0x8100, inter-tpid: 0x8100           inter-VLAN range: any        , exter-VLAN range:    1 - 10 interface: smartgroup2.1           exter-tpid: 0x8100, inter-tpid: 0x8100           inter-VLAN range:    1 - 10  , exter-VLAN range: anyZXROSNG(config-vlan)#show interface-vlan qinq smartgroup3interface: smartgroup3.1exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range:    3000 - 3001, exter-VLAN range:    2000-2001interface: smartgroup3.2exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range:    4000 - 4001, exter-VLAN range:    4000-4001






相关命令 :

无 




## show interface-vlan 


show interface-vlan 




命令功能 :

该命令工作于除用户模式外的其它所有模式，作用为：显示所有子接口或者某个子接口下的VLAN 配置信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show interface-vlan 
  [＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称，用于指定需要显示的接口。








缺省 :

无 






使用说明 :

显示该接口下的配置的VLAN 配置信息。如果show命令后不加接口名，则表现显示所有接口的VLAN 配置信息。针对bras项目，子接口上配置any-other-VLAN类型标记，使用该命令能够显示对应的配置。如果配置了encapsulation untag，使用该命令显示对应的配置。子接口上配置NNI VLAN，使用该命令能够显示对应的配置。子接口上配置QinQ any配置，使用该命令能够显示对应的配置。如果show命令后加父接口名，遍历该父接口的所有子接口进行显示。






范例 :

该命令执行及结果如下：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show interface-vlaninterface: gei-0/1/0/1.1exter-tpid: 0x8100, inter-tpid: 0x8100untag: permittedVLAN range:    1 - 200VLAN range:  301 - 500interface: gei-0/1/0/1.2exter-tpid: 0x8100, inter-tpid: 0x8100VLAN ID: NNI 1000, leaf VLAN ID:2000interface: gei-0/1/0/1.3exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range:    1 - 200, exter-VLAN range:    1 - 3inter-VLAN range:  200 - 201, exter-VLAN range:   11 - 3000interface: smartgroup1.1exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range: any        , exter-VLAN range:    1 - 10interface: smartgroup2.1exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range:    1 - 10, exter-VLAN range: anyZXROSNG(config-vlan)#show interface-vlan smartgroup3interface: smartgroup3.1exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range:    3000 - 3001, exter-VLAN range:    2000-2001interface: smartgroup3.2exter-tpid: 0x8100, inter-tpid: 0x8100inter-VLAN range:    4000 - 4001, exter-VLAN range:    4000-4001






相关命令 :

show interface-vlan qinqshow interface-vlan dot1q




## show statistics 


show statistics 




命令功能 :

该命令工作于除用户模式外的其它所有模式，作用为：通过该命令，显示用户侧PVV链路的流量信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show statistics 
  ＜IfName 
＞ exvlan 
 ＜ExVlanId 
＞ [invlan 
 ＜InVlanId 
＞] 







命令参数解释 :



参数|描述
---|---
＜IfName＞|用户侧VCC子接口
＜ExVlanId＞|子接口支持的VLAN ID, 范围：1–4094
＜InVlanId＞|子接口支持的VLAN ID, 范围：1–4094








缺省 :

无 






使用说明 :

    本命令只支持M6000系列产品。子接口封装dot1q或者dot1q range时，show命令中只需要输入exvlan即可；     输入接口为父接口，提示错误信息表示父接口上不支持显示流量;






范例 :

显示电路上的流量信息：ZXROSNG#show statistics gei-0/1/0/1.1 exvlan 55In_Bytes:30                              E_Bytes:120                       In_Packets:60                            E_Packets:150                       In_Discards:90                           E_Discards:180






相关命令 :

无 




## show vlan count 


show vlan count 




命令功能 :

显示整机和各个单板的VLAN资源计数以及资源使用率。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show vlan count 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

用来显示系统和各块单板目前的VLAN资源计数，方便用户了解当前系统和单板VLAN资源的使用情况。 






范例 :

show vlan count Board-based subinterface VLAN Count limit:65472System-based subinterface VLAN Count limit:261888Total VLAN Count:40940Headers: All-VLAN-Count--All Types of Board-based VLAN count         Capacity--All Types of  Board-based VLAN capacityShelf-ID       Slot-ID        All-VLAN-Count         Capacity         Ratio(%)------------------------------------------------------------------------------0              1              40940                  65472            62%






相关命令 :

无 




## show vlan-conflict-interface 


show vlan-conflict-interface 




命令功能 :

该命令工作于除用户模式外的其它所有模式，作用为：通过该命令，查询与输入的VLAN range段相冲突的对应父接口的子接口列表。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show vlan-conflict-interface 
  ＜IfName 
＞ {dot1q 
 vlan-range 
 ＜ExVlanId 
＞|qinq 
 internal-vlan-range 
 ＜InVlanId 
＞ external-vlan-range 
 ＜ExVlanId 
＞} 







命令参数解释 :



参数|描述
---|---
＜IfName＞|接口名
dot1q|单层vlan类型
＜ExVlanId＞|双层vlan时，子接口支持的外层VLAN ID range段, 范围：1–4094
qinq|qinq类型
＜InVlanId＞|双层vlan时，子接口支持的内层VLAN ID range段, 范围：1–4094
＜ExVlanId＞|双层vlan时，子接口支持的外层VLAN ID range段, 范围：1–4094








缺省 :

无 






使用说明 :

输入接口名称如果是子接口，会显示与输入VLAN存在重叠的该子接口的所有的兄弟接口。输入接口名称如果是父接口，会显示与输入VLAN存在重叠的该物理口的所有的子接口。该命令有效率问题，不要频繁使用。另外，输入的接口名称，应该尽量保证该接口是VLAN支持的接口，并且保证该接口存在。





范例 :

ZXROSNG(config) show vlan-confict-interface gei-0/1/0/1.1 dot1q vlan-range 1-100 Conflict Interface Name : SUB-INTERFACE-NAME        --------------------------gei-0/1/0/1.1gei-0/1/0/1.3gei-0/1/0/1.5gei-0/1/0/1.7





相关命令 :

无 




## user-dynamic-vlan 


user-dynamic-vlan 




命令功能 :

创建子接口配置动态VLAN功能，使用no命令取消配置。 






命令模式 :

 VLAN子接口模式  






命令默认权限级别 :

15 






命令格式 :



user-dynamic-vlan 
  ＜dynamic-vlan-type 
＞

no user-dynamic-vlan 








命令参数解释 :



参数|描述
---|---
＜dynamic-vlan-type＞|动态VLAN类型,分为any-other-dot1q和any-other-qinq








缺省 :

无 






使用说明 :

如果子接口上已经存在静态VLAN配置，则不能执行此命令，即动静态VLAN不能同时存在一个子接口上。在配置了user-dynamic-vlan any-other-dot1q命令后，使用单层VLAN range命令配置当前子接口可以允许的动态VLAN范围，在配置了user-dynamic-vlan any-other-qinq命令后，使用双层 VLAN range 命令配置当前子接口的动态VLAN范围。子接口上删除动态VLAN标记后，VLAN range配置会自动关联删除。如果父接口绑入了VPLS/VPWS/VLSS实例，在接口的所有子接口不能配置动态vlan；如果子接口绑入了VPLS/VPWS/VLSS实例，该子接口不能配置动态vlan；如果子接口绑入了VPLS/VPWS/VLSS实例，并且该子接口配置了静态dot1q，如果在该子接口的兄弟接口配置动态qinq，则qinq外层vlan与dot1q的vlan不能有重叠。





范例 :

配置命令如下：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#user-dynamic-vlan any-other-dot1q通过show run命令查看：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan!<vlan>vlan-configuration  interface gei-0/1/0/1.1    user-dynamic-vlan any-other-dot1q  $$!</vlan>通过no命令删除动态VLAN标记：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#no user-dynamic-vlanZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan





相关命令 :

无 




## vlan-configuration 


vlan-configuration 




命令功能 :

该命令工作于全局配置模式下，用于进入VLAN模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



vlan-configuration 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于从全局配置模式进入VLAN模式。 






范例 :

ZXROSNG(config)#vlan-configuration ZXROSNG(config-vlan)#






相关命令 :

无 




## vlan-range-broadcast 


vlan-range-broadcast 




命令功能 :

为新创建的子接口配置是否支持VLAN range的ARP/ND广播功能。  






命令模式 :

 VLAN子接口模式  






命令默认权限级别 :

15 






命令格式 :



vlan-range-broadcast 
  {[single-layer 
] enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
single-layer|对于双层VLAN的情况，如果配置了single-layer选项，则只有外层VLAN起作用
enable|开启子接口VLAN range ARP/ND广播功能
disable|关闭子接口VLAN range ARP/ND广播功能








缺省 :

disable：不支持 






使用说明 :

子接口封装了range类型后才可以配置该命令。如果此子接口上没有封装VLAN或封装的VLAN类型不是range，则不能执行此命令。在配置了此命令时，如果子接口的VLAN个数超出产品设定的门限，则不允许开启此功能，目前是4k。最后一段VLAN range删除时，该开关自动修改为disable。single-layer表示发包只使用外层VLAN。





范例 :

打开vlan range 主动发包开关：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#vlan-range-broadcast enable查看配置结果信息：ZXROSNG(config-vlan-if-gei-0/1/0/1.1)#show running-config vlan!<vlan>vlan-configuration  interface gei-0/1/0/1.1    user-dynamic-vlan any-other-dot1q    encapsulation-dot1q range 1-2    vlan-range-broadcast enable  $$!</vlan>





相关命令 :

无 




# 二层交换配置命令 
interface :

interface (SwitchVLAN模式) 




命令功能 :

通过接口跳转到SwitchVLAN接口模式





命令模式 :

 SwitchVLAN模式  






命令默认权限级别 :

15 






命令格式 :


interface 
  ＜IfName 
＞






命令参数解释 :



参数|描述
---|---
＜IfName＞|接口名，支持物理口和smartgroup接口








缺省 :

无 






使用说明 :

通过接口跳转到SwitchVLAN接口模式，在该模式下可以对该接口进行相应的配置 






范例 :

ZXROSNG(config-swvlan)#interface gei-0/1/0/1ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode trunk ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport trunk vlan 100






相关命令 :

无 




## list 


list 




命令功能 :

VLAN的批量创建和删除 






命令模式 :

 SwitchVLAN模式  






命令默认权限级别 :

15 






命令格式 :


list 
  ＜vlan-list 
＞
no list 
  ＜vlan-list 
＞
				






命令参数解释 :



参数|描述
---|---
＜vlan-list＞|一个或多个VLAN，批量配置。有效范围2-4094。








缺省 :

无 






使用说明 :

进行VLAN的批量创建和删除。 






范例 :

批量创建VLAN 2到VLAN 100ZXROSNG(config-swvlan)#list 2-100批量删除VLAN 2到15ZXROSNG(config-swvlan)#no list 2-15





相关命令 :

show vlanvlan <vlan_id>




## name 


name 




命令功能 :

配置VLAN别名，使用no命令恢复VLAN别名为缺省值。 






命令模式 :

 SwitchVLAN-VLAN子模式  






命令默认权限级别 :

15 






命令格式 :



name 
  ＜vlan-name 
＞

no name 








命令参数解释 :



参数|描述
---|---
＜vlan-name＞|VLAN的别名。








缺省 :

VLAN 1的缺省别名为vlan0001；VLAN 100的缺省别名为vlan0100；以此类推。 






使用说明 :

配置VLAN别名不可以和其他VLAN重复，也不可以配置成其他所有VLAN的默认别名（即便该VLAN不存在）。name 后面只能输入字符串，字符串的第一个字符必须为字母（大写和小写都行），字符串中不能有逗号。






范例 :

将VLAN 2命名为zteZXROSNG(config-swvlan)#vlan 2ZXROSNG(config-swvlan-sub-2)#name zte将VLAN 2的别名从zte恢复到默认值ZXROSNG(config-swvlan)#vlan 2ZXROSNG(config-swvlan-sub-2)#no name





相关命令 :

show vlanvlan {<vlan_num>| name <vlan-name>}no vlan {<vlan_num>| name <vlan-name>}[no] list <vlan_list>




## show vlan id 


show vlan id 




命令功能 :

显示id指定的VLAN配置信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show vlan id 
  ＜vlan-id 
＞ 







命令参数解释 :



参数|描述
---|---
＜vlan-id＞|需要显示VLAN ID








缺省 :

无 






使用说明 :

显示配置的VLAN信息，参数id后的值为指定需要显示的具体VLAN。 






范例 :

显示VLAN 1的配置信息ZXROSNG(config-swvlan)#show vlan id 1VLAN     Name     PvidPorts           UntagPorts          TagPorts          ---------------------------------------------------------------1        vlan0001 smartgroup1-3                                             gei-0/1/0/1-47  






相关命令 :

[no] switchport access vlan[no] switchport trunk [native] vlan[no] switchport hybrid [native] vlan[no] switchport {pvid | tag | untag}




## show vlan name 


show vlan name 




命令功能 :

显示指定的VLAN信息，通过VLAN name指定具体VLAN。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show vlan name 
  ＜vlan-name 
＞ 







命令参数解释 :



参数|描述
---|---
＜vlan-name＞|需要显示的VLAN的别名








缺省 :

无 






使用说明 :

显示配置的VLAN信息，参数name后的字符串为指定需要显示的具体VLAN的name。 






范例 :

显示name为vlan0001的VLAN信息ZXROSNG(config-swvlan)#show vlan name vlan0001VLAN     Name     PvidPorts           UntagPorts          TagPorts          ----------------------------------------------------1        vlan0001 smartgroup1-3                                             gei-0/1/0/1-47 






相关命令 :

[no] switchport access vlan[no] switchport trunk [native] vlan[no] switchport hybrid [native] vlan[no] switchport {pvid | tag | untag}




## show vlan 


show vlan 




命令功能 :

显示已配置的VLAN信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show vlan 
  [{access 
|trunk 
|hybrid 
}] 







命令参数解释 :



参数|描述
---|---
access|显示VLAN下的access端口
trunk|显示VLAN下的trunk端口
hybrid|显示VLAN下的hybrid端口








缺省 :

显示已经配置的所有VLAN的信息 






使用说明 :

显示配置的VLAN信息，参数access、trunk和hybrid表示只显示对应模式的端口信息。 






范例 :

显示配置的VLAN中的access接口信息ZXROSNG(config-swvlan)#show vlan access VLAN     Name     PvidPorts           UntagPorts          TagPorts          -----------------------------------------------------------------1        vlan0001 smartgroup1-3                                             gei-0/1/0/3-47                          10       vlan0010                                         11       vlan0011                                         12       vlan0012  






相关命令 :

[no] switchport access vlan[no] switchport trunk [native] vlan[no] switchport hybrid [native] vlan[no] switchport {pvid | tag | untag}




## switchport access 


switchport access 




命令功能 :

将access端口加入到VLAN中，如果该VLAN不存在，则创建VLAN。使用no命令从VLAN中删除端口。 






命令模式 :

 SwitchVLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



switchport access 
 vlan 
 {＜vlan-id 
＞|＜vlan-name 
＞}

no switchport access 
 vlan 








命令参数解释 :



参数|描述
---|---
vlan|配置接口的VLAN。
＜vlan-id＞|具体VLAN ID，有效范围1-4094。
＜vlan-name＞|VLAN的别名。








缺省 :

二层端口缺省在VLAN 1中。 






使用说明 :

将access口加入或从指定VLAN移出，access模式的端口只能属于一个VLAN。接口配置了PVID后，其子接口上不允许配置untag，反之亦然。






范例 :

ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode access 将gei-0/1/0/1的PVID配置为VLAN 100ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport access vlan 100ZXROSNG(config-swvlan-if-gei-0/1/0/1)#show vlan id 100VLAN     Name     PvidPorts           UntagPorts          TagPorts          -----------------------------------------------------------------------100      vlan0100 gei-0/1/0/1 






相关命令 :

show vlan[no] switchport pvid default native-vlan 




## switchport hybrid native 


switchport hybrid native 




命令功能 :

配置hybrid端口的native VLAN，如果该VLAN不存在，则创建VLAN。使用no命令恢复缺省设置。 






命令模式 :

 SwitchVLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



switchport hybrid native 
 vlan 
 {＜vlan-id 
＞|＜vlan-name 
＞}

no switchport hybrid native 
 vlan 








命令参数解释 :



参数|描述
---|---
vlan|具体VLAN ID，有效范围1-4094。
＜vlan-id＞|具体VLAN ID，有效范围1-4094。
＜vlan-name＞|VLAN的别名。








缺省 :

缺省为VLAN 1。 






使用说明 :

执行该命令，端口必须为hybrid模式，否则提示出错。配置hybrid端口的Native VLAN，通过no命令恢复默认值。接口配置了PVID后，其子接口上不允许配置untag，反之亦然。






范例 :

ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode hybrid ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport hybrid native vlan 12ZXROSNG(config-swvlan-if-gei-0/1/0/1)#show vlan id 12VLAN     Name     PvidPorts           UntagPorts          TagPorts          ----------------------------------------------------------------------12       vlan0012 gei-0/1/0/1 






相关命令 :

[no] switchport pviddefault native-vlan




## switchport hybrid 


switchport hybrid 




命令功能 :

将hybrid端口加入到VLAN中，如果该VLAN不存在，则创建VLAN。使用no命令从VLAN中删除端口。 






命令模式 :

 SwitchVLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


switchport hybrid 
 vlan 
 ＜vlan-list 
＞ {tag 
|untag 
}
no switchport hybrid 
 vlan 
 ＜vlan-list 
＞
				






命令参数解释 :



参数|描述
---|---
vlan|配置接口的VLAN。
＜vlan-list＞|一个或多个VLAN，可批量配置，有效范围1-4094。
tag|标记为tag端口
untag|标记为untag端口








缺省 :

无 






使用说明 :

执行该命令，端口必须为hybrid模式，否则提示出错。配置hybrid端口的tag VLAN和untag VLAN成员。同一个接口下的VLAN不能既是untag VLAN又是tag VLAN，二选一。






范例 :

ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode hybrid ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport hybrid vlan 100-102 tag ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport hybrid vlan 10-15 untag 






相关命令 :

show vlan[no] switchport hybrid  vlan[no] switchport {tag | untag}[no] switchport mode {access | trunk | hybrid}




## switchport mode 


switchport mode 




命令功能 :

设置端口的VLAN链路模式，使用no命令恢复缺省模式。 






命令模式 :

 SwitchVLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



switchport mode 
  {access 
|trunk 
|hybrid 
}

no switchport mode 








命令参数解释 :



参数|描述
---|---
access|设置端口为access模式
trunk|设置端口为trunk模式
hybrid|设置端口为hybrid模式








缺省 :

二层端口默认模式为access。 






使用说明 :

当端口从trunk/hybrid模式被配置成access，或者通过no命令恢复到了默认值时，端口的tag、untag VLAN与端口的绑定关系自动删除。access端口只能属于一个VLAN。 






范例 :

ZXROSNG(config-swvlan)#interface gei-0/1/0/1将端口配置为trunk模式ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode trunk 将端口配置为access模式ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode access 将端口配置为hybrid模式ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode hybrid 将端口配置恢复成默认值access模式ZXROSNG(config-swvlan-if-gei-0/1/0/1)#no switchport mode 






相关命令 :

switchport tag trunk native vlan 




## switchport trunk native 


switchport trunk native 




命令功能 :

配置trunk端口的native VLAN，如果该VLAN不存在，则创建VLAN。使用no命令恢复缺省设置。 






命令模式 :

 SwitchVLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



switchport trunk native 
 vlan 
 {＜vlan-id 
＞|＜vlan-name 
＞}

no switchport trunk native 
 vlan 








命令参数解释 :



参数|描述
---|---
vlan|配置接口的VLAN。
＜vlan-id＞|具体VLAN ID，有效范围1-4094。
＜vlan-name＞|VLAN的别名。








缺省 :

缺省为VLAN 1。 






使用说明 :

执行该命令的端口模式必须为trunk。配置trunk端口的Native VLAN。通过no命令恢复成默认值。接口配置了PVID后，其子接口上不允许配置untag，反之亦然。 






范例 :

ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode trunk ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport trunk native vlan 10ZXROSNG(config-swvlan-if-gei-0/1/0/1)#show vlan id 10VLAN     Name     PvidPorts           UntagPorts          TagPorts          ----------------------------------------------------------------------10       vlan0010 gei-0/1/0/1   






相关命令 :

[no] switchport pviddefault native-vlan




## switchport trunk 


switchport trunk 




命令功能 :

将trunk端口加入到VLAN中，如果该VLAN不存在，则创建VLAN。使用no命令从VLAN中删除端口。 






命令模式 :

 SwitchVLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


switchport trunk 
 vlan 
 ＜vlan-list 
＞
no switchport trunk 
 vlan 
 ＜vlan-list 
＞
				






命令参数解释 :



参数|描述
---|---
vlan|配置接口的VLAN。
＜vlan-list＞|一个或多个VLAN，可批量配置，有效范围1-4094。








缺省 :

无 






使用说明 :

设置trunk端口的VLAN，trunk端口可以加入或移出多个VLAN。执行该命令的端口模式必须为trunk。 






范例 :

ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport mode trunk ZXROSNG(config-swvlan-if-gei-0/1/0/1)#switchport trunk vlan 10-12ZXROSNG(config-swvlan-if-gei-0/1/0/1)#no switchport trunk vlan 11-12






相关命令 :

[no] switchport tagdefault joined-vlan




## switchport 


switchport 




命令功能 :

VLAN端口的批量处理。 






命令模式 :

 SwitchVLAN-VLAN子模式  






命令默认权限级别 :

15 






命令格式 :


switchport 
  {pvid 
|tag 
|untag 
} ＜port-list 
＞
no switchport 
  {pvid 
|tag 
|untag 
} ＜port-list 
＞
				






命令参数解释 :



参数|描述
---|---
pvid|设置端口的PVID
tag|设置VLAN中端口为tag
untag|设置VLAN中端口为untag
＜port-list＞|配置端口，可以批量配置。








缺省 :

无 






使用说明 :

该命令在指定的VLAN上配置端口，可以批量配置。pvid配置对于所有端口有效，tag端口配置对于trunk/hybrid模式的端口有效，untag端口配置对于hybrid端口有效，模式不正确的情况提示用户相应出错信息。接口配置了PVID后，其子接口上不允许配置untag，反之亦然。






范例 :

ZXROSNG(config-swvlan)#vlan 100ZXROSNG(config-swvlan-sub)#switchport pvid gei-0/1/0/1ZXROSNG(config-swvlan-sub)#switchport tag gei-0/1/0/1      ZXROSNG(config-swvlan-sub)#switchport untag gei-0/1/0/2






相关命令 :

show vlan[no] switchport access vlan[no] switchport trunk [native] vlan[no] switchport hybrid [native] vlan




## switchvlan-configuration 


switchvlan-configuration 




命令功能 :

从全局配置模式进入SwitchVLAN模式 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



switchvlan-configuration 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于从全局配置模式进入SwitchVLAN模式，进行交换机VLAN相关命令的操作。 






范例 :

ZXROSNG(config)#switchvlan-configurationZXROSNG(config-swvlan)#





相关命令 :

无 




## vlan name 


vlan name 




命令功能 :

通过VLAN别名跳转到SwitchVLAN-VLAN子模式 






命令模式 :

 SwitchVLAN模式  






命令默认权限级别 :

15 






命令格式 :



vlan name 
  ＜vlan-name 
＞







命令参数解释 :



参数|描述
---|---
＜vlan-name＞|VLAN的别名。








缺省 :

无 






使用说明 :

通过指定的VLAN别名进入SwitchVLAN-VLAN子模式VLAN别名的VLAN必须存在，否则提示错误。






范例 :

ZXROSNG(config-swvlan)#show vlan VLAN     Name     PvidPorts           UntagPorts          TagPorts          -------------------------------------------------------------------------      100      zte                                              gei-0/1/0/1进入别名为zte的VLAN子模式下ZXROSNG(config-swvlan)#vlan name zteZXROSNG(config-swvlan-sub-100)#






相关命令 :

name <vlan_name>vlan <vlan_id>show vlan




## vlan 


vlan 




命令功能 :

创建单个VLAN，并进入子VLAN配置模式。使用no命令删除VLAN。 






命令模式 :

 SwitchVLAN模式  






命令默认权限级别 :

15 






命令格式 :


vlan 
  ＜vlan-id 
＞
no vlan 
  {＜vlan-id 
＞|name 
 ＜vlan-name 
＞}
				






命令参数解释 :



参数|描述
---|---
＜vlan-id＞|删除时指定的VLAN ID，有效范围为2-4094。








缺省 :

无 






使用说明 :

创建某个VLAN必须指定VLAN ID，即通过vlan <vlan_num>格式创建，创建后自动切换到SwitchVLAN-子VLAN模式。删除指定VLAN时，可以通过指定VLAN ID或VLAN别名。如果该VLAN为VLAN 1或者和其他模块有互斥检查不通过则提示不能删除。





范例 :

创建VLAN 100ZXROSNG(config-swvlan)#vlan 100ZXROSNG(config-swvlan-sub-100)#exit删除VLAN 100ZXROSNG(config-swvlan)#no vlan 100






相关命令 :

list 




# 接口基础配置命令 
## bandwidth 


bandwidth 




命令功能 :

该命令工作于接口配置模式下，用于设置接口能力带宽值，no bandwidth命令用于删除接口能力带宽值。 






命令模式 :

 eth接口模式  






命令默认权限级别 :

15 






命令格式 :



bandwidth 
  ＜1-1000000 
＞ [{mbps 
|gbps 
}]

no bandwidth 








命令参数解释 :



参数|描述
---|---
＜1-1000000＞|接口能力带宽值。取值范围：1-1000000。单位：mbps。
mbps|可选参数，数字量易用性使用
gbps|可选参数，数字量易用性使用








缺省 :

无 






使用说明 :

eth接口支持能力带宽配置。配置生效后，可以通过show  interface命令查看接口的能力带宽生效值。






范例 :

配置eth1接口的能力带宽值为10mbps，不带单位。命令如下：命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#bandwidth 10配置eth1接口的能力带宽值为10mbps。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#bandwidth 10 mbps配置eth1接口的能力带宽值为10gbps，不带单位。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#bandwidth 10000配置eth1接口的能力带宽值为10gbps。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#bandwidth 10 gbps删除eth1接口能力带宽值。命令如下：命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#no bandwidth






相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other






范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname






相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。






命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx接口模式:15,qx子接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other






范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname






相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 ATM子接口模式,ATM接口模式,atm_dslgroup接口模式,dsl接口模式,e1接口模式,eth_dslgroup子接口模式,eth_dslgroup接口模式,mte隧道接口模式,oh_tt接口模式,posgroup接口模式,pos子接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式  






命令默认权限级别 :

serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,oh_tt接口模式:15,eth_dslgroup子接口模式:15,e1接口模式:15,ulei子接口模式:15,vbui子接口模式:15,pos子接口模式:15,ulei接口模式:15,mte隧道接口模式:15,posgroup接口模式:15,ATM接口模式:15,ATM子接口模式:15,atm_dslgroup接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 10G以太接口模式,loopback接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,smartgroup接口模式:15,loopback接口模式:15,smartgroup子接口模式:15,以太接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 以太子接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,千兆以太接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 IPv6隧道接口模式,supervlan接口模式,te隧道接口模式  






命令默认权限级别 :

te隧道接口模式:15,IPv6隧道接口模式:15,supervlan接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 dialer接口模式,virtual_template子接口模式,virtual_template接口模式  






命令默认权限级别 :

virtual_template子接口模式:15,virtual_template接口模式:15,dialer接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 vbui接口模式  






命令默认权限级别 :

15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 multilink接口模式,pos接口模式,通道化ce1接口模式,通道化cpos_cep接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_cep接口模式:15,通道化cpos_e1接口模式:15,通道化ce1接口模式:15,multilink接口模式:15,pos接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 cip接口模式  






命令默认权限级别 :

15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth接口模式:15,eth子接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。






命令模式 :

 qx_eth接口模式  






命令默认权限级别 :

15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other






范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname






相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。no byname命令用于删除接口别名。物理接口名中有一系列表示物理位置的数字，如:fei-0/1/0/1，或者逻辑接口名的接口号比较大，不方便记忆，如te_tunnel64511，等等。此时，将接口别名设置为一个简单易记的字符串，可以方便用户进入接口模式对接口进行配置操作或者删除接口。





命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other.





范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname





相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi接口模式:15,bvi子接口模式:15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other






范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname






相关命令 :

无 




byname :

byname 




命令功能 :

该命令工作于接口配置模式下，用于设置接口别名。别名是接口的唯一标识，接口配置了别名后，可以通过别名进入接口模式，也可以通过别名删除接口。






命令模式 :

 celluar接口模式  






命令默认权限级别 :

15 






命令格式 :


byname 
  ＜byname 
＞

no byname 








命令参数解释 :



参数|描述
---|---
＜byname＞|接口别名。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置别名。可以通过show ip interface命令查看接口别名。别名是接口的唯一标识，不同接口不允许配置相同的别名。如果在接口上配置已经被别的接口使用了的别名，会提示：%Error 1220: The byname has existed,please input other






范例 :

配置gei-0/1/0/1接口的别名为ether1。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#byname ether1删除gei-0/1/0/1接口的别名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no byname






相关命令 :

无 




## control-plane-security 


control-plane-security 




命令功能 :

进入控制面安全命令配置模式 






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




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 IPsec接口模式  






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
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 ATM子接口模式,ATM接口模式,atm_dslgroup接口模式,dsl接口模式,e1接口模式,eth_dslgroup子接口模式,eth_dslgroup接口模式,mte隧道接口模式,oh_tt接口模式,posgroup接口模式,pos子接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式  






命令默认权限级别 :

posgroup接口模式:15,atm_dslgroup接口模式:15,mte隧道接口模式:15,serial接口模式:15,dsl接口模式:15,oh_tt接口模式:15,eth_dslgroup接口模式:15,e1接口模式:15,eth_dslgroup子接口模式:15,ulei子接口模式:15,vbui子接口模式:15,pos子接口模式:15,ulei接口模式:15,ATM子接口模式:15,ATM接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 10G以太接口模式,loopback接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,smartgroup接口模式:15,loopback接口模式:15,smartgroup子接口模式:15,以太接口模式:15,千兆以太接口模式:15,以太子接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 IPv6隧道接口模式,supervlan接口模式,te隧道接口模式  






命令默认权限级别 :

supervlan接口模式:15,te隧道接口模式:15,IPv6隧道接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 dialer接口模式,virtual_template子接口模式,virtual_template接口模式  






命令默认权限级别 :

dialer接口模式:15,virtual_template接口模式:15,virtual_template子接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 vbui接口模式  






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
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 multilink接口模式,pos接口模式,通道化ce1接口模式,通道化cpos_cep接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_cep接口模式:15,通道化cpos_e1接口模式:15,通道化ce1接口模式:15,multilink接口模式:15,pos接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 cip接口模式  






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
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 通道化cpos_e1子接口模式  






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
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。






范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description






相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth接口模式:15,eth子接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 gre隧道接口模式,三层VLAN接口模式  






命令默认权限级别 :

三层VLAN接口模式:15,gre隧道接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description





相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi接口模式:15,bvi子接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。






范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description






相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。






命令模式 :

 celluar接口模式,qx_eth接口模式  






命令默认权限级别 :

qx_eth接口模式:15,celluar接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。





范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description






相关命令 :

无 




description :

description 




命令功能 :

该命令工作于接口配置模式下，用于设置接口描述信息。no description命令用于删除接口描述信息。当接口上需要记录某些信息时，如接口的用途、接口上启用的业务等等，可以通过该命令将这些信息记录在接口的描述信息中。





命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx子接口模式:15,qx接口模式:15 






命令格式 :


description 
  ＜description 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description＞|接口描述信息。取值范围：配置范围为1-104位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。接口在缺省的情况下，没有配置描述信息。可以通过show interface description、show interface brief、show interface和show ip interface命令查看接口的描述信息。






范例 :

配置gei-0/1/0/1接口的描述信息为”this is an ether port”gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。”this is an ether port”为接口描述信息。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#description this is an ether port删除gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no description






相关命令 :

无 




## encapsulation 


encapsulation 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层封装协议。no encapsulation命令用于恢复接口缺省的二层封装协议。接口支持的二层封装协议类型包括PPP、HDLC、Frame-relay（帧中继）。PPP(Point to Point Protocol)，称为点对点协议，提供了一种标准的方式在点对点的链路上传输多种网络层协议的数据报。HDLC(High level Data Link Control)，称为高级数据链路控制，是一个在同步网上传输数据、面向位的数据链路层协议。Frame-relay帧中继，简称FR，是从X.25分组通信技术演变而来的一种通信方式。当接口上需要启用相应的二层协议时，则需要通过encapsulation命令配置接口的二层封装协议。





命令模式 :

 serial接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

serial接口模式:15,通道化cpos_e1接口模式:15,通道化ce1接口模式:15 






命令格式 :


encapsulation 
  {ppp 
|hdlc 
|frame-relay 
}

no encapsulation 








命令参数解释 :



参数|描述
---|---
ppp|和hdlc、frame-relay是三选一，若设置为ppp，表示接口封装类型为PPP封装。默认值：接口缺省为PPP封装。
hdlc|和ppp、frame-relay是三选一，若设置为hdlc，表示接口封装类型为HDLC封装。默认值：接口缺省为PPP封装。
frame-relay|和ppp、hdlc是三选一，若设置为frame-relay，表示接口封装类型为Frame-relay封装。默认值：接口缺省为PPP封装。








缺省 :

PPP封装 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。通道化接口和serial接口支持二层封装协议的配置。接口缺省为PPP封装。可以通过show interface命令查看接口当前的二层封装协议。通道化cpos_e1接口可以配置子接口。只有当接口配置为Frame-relay封装，才可以配置子接口。否则会提示：%Error 121017: The encapsulation of the father interface is not frame-relay protocol同样，当配置了子接口的情况下，不允许修改接口的封装类型，否则会提示：%Error 121101: The interface with child is not allowed to change its encapsulation





范例 :

配置cpos3_e1-0/1/0/1.2/1/1:2接口为HDLC封装。cpos3_e1-0/1/0/1.2/1/1:2表示设备上的通道化接口，其中”cpos3_e1-”表示接口类型为通道化后的CPOS_E1接口，”0/1/0/1.2/1/1:2”依次代表机框号、槽位号、子槽位号、接口号、复用路径au3或tug3、复用路径tug2、复用路径E1以及通道在E1中的编号。命令如下：ZXROSNG(config)#interface cpos3_e1-0/1/0/1.2/1/1:2ZXROSNG(config-if-cpos3_e1-0/1/0/1.2/1/1:2)#encapsulation hdlc恢复cpos3_e1-0/1/0/1.2/1/1:2接口的缺省二层封装。cpos3_e1-0/1/0/1.2/1/1:2表示设备上的通道化接口，其中”cpos3_e1-”表示接口类型为通道化后的CPOS_E1接口，”0/1/0/1.2/1/1:2”依次代表机框号、槽位号、子槽位号、接口号、复用路径au3或tug3、复用路径tug2、复用路径E1以及通道在E1中的编号。命令如下：ZXROSNG(config)#interface cpos3_e1-0/1/0/1.2/1/1:2ZXROSNG(config-if-cpos3_e1-0/1/0/1.2/1/1:2)#no encapsulation





相关命令 :

无 




## encapsulation 


encapsulation 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层封装协议。no encapsulation命令用于恢复接口缺省的二层封装协议。接口支持的二层封装协议类型包括PPP、HDLC、Frame-relay（帧中继）。同时，还支持将二层封装配置成单通模式：上行单通或者下行单通。PPP(Point to Point Protocol)，称为点对点协议，提供了一种标准的方式在点对点的链路上传输多种网络层协议的数据报。HDLC(High level Data Link Control)，称为高级数据链路控制，是一个在同步网上传输数据、面向位的数据链路层协议。Frame-relay帧中继，简称FR，是从X.25分组通信技术演变而来的一种通信方式。当接口上需要启用相应的二层协议时，则需要通过encapsulation命令配置接口的二层封装协议。对安全性方面有特殊的需求的网络，点对点通讯，需要支持单向的网络传输功能，单发或者单收。需要将接口配置为单通模式，表示接口只在单方向上传输报文。上行单通即为接口只发送报文，不接收报文，下行单通即为接口只接收报文，不发送报文。





命令模式 :

 pos接口模式  






命令默认权限级别 :

15 






命令格式 :


encapsulation 
  {ppp 
 [{rx 
|tx 
}]|hdlc 
 [{rx 
|tx 
}]|frame-relay 
 [{rx 
|tx 
}]}

no encapsulation 








命令参数解释 :



参数|描述
---|---
ppp|和hdlc、frame-relay是三选一，若设置为ppp，表示接口封装类型为PPP封装。默认值：接口缺省为PPP封装。
rx|和tx是二选一，若设置为rx，表示将接口设置为上行单通，只接收报文不发送报文。和tx共同组合为可选参数，如果不选择，表示将接口设置为双通模式，如果选择，表示将接口设置为单通模式。接口缺省为双通模式
tx|和rx是二选一，若设置为tx，表示将接口设置为下行单通，只发送报文不接收报文。和tx共同组合为可选参数，如果不选择，表示将接口设置为双通模式，如果选择，表示将接口设置为单通模式。接口缺省为双通模式。
hdlc|和ppp、frame-relay是三选一，若设置为hdlc，表示接口封装类型为HDLC封装。默认值：接口缺省为PPP封装。
rx|和tx是二选一，若设置为rx，表示将接口设置为上行单通，只接收报文不发送报文。和tx共同组合为可选参数，如果不选择，表示将接口设置为双通模式，如果选择，表示将接口设置为单通模式。接口缺省为双通模式
tx|和rx是二选一，若设置为tx，表示将接口设置为下行单通，只发送报文不接收报文。和tx共同组合为可选参数，如果不选择，表示将接口设置为双通模式，如果选择，表示将接口设置为单通模式。接口缺省为双通模式。
frame-relay|和ppp、hdlc是三选一，若设置为frame-relay，表示接口封装类型为Frame-relay封装。默认值：接口缺省为PPP封装。
rx|和tx是二选一，若设置为rx，表示将接口设置为上行单通，只接收报文不发送报文。和tx共同组合为可选参数，如果不选择，表示将接口设置为双通模式，如果选择，表示将接口设置为单通模式。接口缺省为双通模式
tx|和rx是二选一，若设置为tx，表示将接口设置为下行单通，只发送报文不接收报文。和tx共同组合为可选参数，如果不选择，表示将接口设置为双通模式，如果选择，表示将接口设置为单通模式。接口缺省为双通模式。








缺省 :

PPP封装 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。通道化接口和serial等接口支持二层封装协议的配置。接口缺省为PPP封装。可以通过show interface命令查看接口当前的二层封装协议。通道化cpos_e1接口可以配置子接口。只有当接口配置为Frame-relay封装，才可以配置子接口。否则会提示：%Error 121017: The encapsulation of the father interface is not frame-relay protocol同样，当配置了子接口的情况下，不允许修改接口的封装类型，否则会提示：%Error 121101: The interface with child is not allowed to change its encapsulation





范例 :

配置pos192-0/1/1/1接口为HDLC封装。pos192-0/1/1/1表示设备上的物理接口，其中”pos192-”表示接口类型为POS接口，”0/1/1/1” 依次代表机框号、槽位号、子槽位号和接口号。hdlc表示HDLC封装类型。命令如下：ZXROSNG(config)#interface pos192-0/1/1/1ZXROSNG(config-if-pos192-0/1/1/1)#encapsulation hdlc配置pos192-0/1/1/2接口为PPP封装上行单通。pos192-0/1/1/1表示设备上的物理接口，其中”pos192-”表示接口类型为POS接口，”0/1/1/1” 依次代表机框号、槽位号、子槽位号和接口号。ppp表示PPP封装类型。rx表示上行单通。命令如下：ZXROSNG(config)#interface pos192-0/1/1/2ZXROSNG(config-if-pos192-0/1/1/2)#encapsulation ppp rx恢复pos192-0/1/1/1接口的缺省二层封装。pos192-0/1/1/1表示设备上的物理接口，其中”pos192-”表示接口类型为POS接口，”0/1/1/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface pos192-0/1/1/1ZXROSNG(config-if-pos192-0/1/1/1)#no encapsulation





相关命令 :

无 




## encapsulation 


encapsulation 




命令功能 :

设置接口封装格式，使用no命令置封装格式为默认值 






命令模式 :

 e1接口模式  






命令默认权限级别 :

15 






命令格式 :



encapsulation 
  {ppp 
|tdm 
}

no encapsulation 








命令参数解释 :



参数|描述
---|---
ppp|PPP封装
tdm|TDM封装








缺省 :

按照产品管理上报的值为缺省值 






使用说明 :

本命令只支持CE1通道化接口配置 






范例 :

ZXROSNG(config)#interface ce1-0/1/0/1:1ZXROSNG(config-if-ce1-0/1/0/1:1)#encapsulation ppp






相关命令 :

无 




## ethernet-interface-range 


ethernet-interface-range 




命令功能 :

进入以太接口批量配置模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ethernet-interface-range 
  ＜port-list 
＞







命令参数解释 :



参数|描述
---|---
＜port-list＞|以太接口范围








缺省 :

无 






使用说明 :

进入以太接口批量配置模式，用于批量配置以太接口。 






范例 :

ZXROSNG(config)#ethernet-interface-range gei-0/1/0/1-3ZXROSNG(config–eth-if-range)#






相关命令 :

无 




## gateway interface 


gateway interface 




命令功能 :

该命令工作于接口配置模式下，用于将接口设置成网关接口。no gateway interface命令用于将接口设置成非网关接口。多个SR路由器通过HUB连接的组网中，如果路由器网关接口的IP地址误配，会导致接入的主机与正确的路由器之间正常通讯受到影响。需要对接口的IP地址做动态检测，如果网络中有地址冲突则配置的地址无效。接口配置成网关接口，网关接口的IP地址会进行ARP冲突检测，当检测通为可用后，地址状态才能设置为有效，否则网关地址为无效地址。





命令模式 :

 dsl接口模式,supervlan接口模式,vbui子接口模式  






命令默认权限级别 :

vbui子接口模式:15,dsl接口模式:15,supervlan接口模式:15 






命令格式 :


gateway interface 
 

no gateway interface 








命令参数解释 :


					无
				 






缺省 :

默认非网关接口 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口及其子接口、supervlan接口、vbui接口及其子接口和dsl接口支持网关接口的配置。接口缺省为非网关接口。网关地址ARP冲突检测未通过的情况下，通过show interface和show ip interface命令查看接口地址，会有” [INVALID]”标记当前地址为无效地址。接口设置为网关接口，必须在接口配置IP地址之前完成。如果接口配置了IP地址，再将接口设置为网关接口或将接口设置为非网关接口，会提示：%Error 121074: The interface has IP address只有三层接口才允许配置网关接口，如果设置二层接口为网关接口，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口为网关接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#gateway interface配置gei-0/1/0/1接口为非网关接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no gateway interface





相关命令 :

无 




## gateway interface 


gateway interface 




命令功能 :

该命令工作于接口配置模式下，用于将接口设置成网关接口。no gateway interface命令用于将接口设置成非网关接口。多个SR路由器通过HUB连接的组网中，如果路由器网关接口的IP地址误配，会导致接入的主机与正确的路由器之间正常通讯受到影响。需要对接口的IP地址做动态检测，如果网络中有地址冲突则配置的地址无效。接口配置成网关接口，网关接口的IP地址会进行ARP冲突检测，当检测通为可用后，地址状态才能设置为有效，否则网关地址为无效地址。





命令模式 :

 10G以太接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :


gateway interface 
 

no gateway interface 








命令参数解释 :


					无
				 






缺省 :

默认非网关接口 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口及其子接口、supervlan接口、vbui接口及其子接口和dsl接口支持网关接口的配置。接口缺省为非网关接口。网关地址ARP冲突检测未通过的情况下，通过show interface和show ip interface命令查看接口地址，会有” [INVALID]”标记当前地址为无效地址。接口设置为网关接口，必须在接口配置IP地址之前完成。如果接口配置了IP地址，再将接口设置为网关接口或将接口设置为非网关接口，会提示：%Error 121074: The interface has IP address只有三层接口才允许配置网关接口，如果设置二层接口为网关接口，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口为网关接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#gateway interface配置gei-0/1/0/1接口为非网关接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no gateway interface





相关命令 :

无 




## gateway interface 


gateway interface 




命令功能 :

该命令工作于接口配置模式下，用于将接口设置成网关接口。no gateway interface命令用于将接口设置成非网关接口。多个SR路由器通过HUB连接的组网中，如果路由器网关接口的IP地址误配，会导致接入的主机与正确的路由器之间正常通讯受到影响。需要对接口的IP地址做动态检测，如果网络中有地址冲突则配置的地址无效。接口配置成网关接口，网关接口的IP地址会进行ARP冲突检测，当检测通为可用后，地址状态才能设置为有效，否则网关地址为无效地址。





命令模式 :

 vbui接口模式  






命令默认权限级别 :

15 






命令格式 :


gateway interface 
 

no gateway interface 








命令参数解释 :


					无
				 






缺省 :

默认非网关接口 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口及其子接口、supervlan接口、vbui接口及其子接口和dsl接口支持网关接口的配置。接口缺省为非网关接口。网关地址ARP冲突检测未通过的情况下，通过show interface和show ip interface命令查看接口地址，会有” [INVALID]”标记当前地址为无效地址。接口设置为网关接口，必须在接口配置IP地址之前完成。如果接口配置了IP地址，再将接口设置为网关接口或将接口设置为非网关接口，会提示：%Error 121074: The interface has IP address只有三层接口才允许配置网关接口，如果设置二层接口为网关接口，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口为网关接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#gateway interface配置gei-0/1/0/1接口为非网关接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no gateway interface





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。





命令模式 :

 eth_dslgroup子接口模式,eth_dslgroup接口模式,supervlan接口模式  






命令默认权限级别 :

eth_dslgroup接口模式:15,eth_dslgroup子接口模式:15,supervlan接口模式:15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的MAC地址偏移为5。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address offset 5删除gei-0/1/0/1接口MAC地址偏移。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。






命令模式 :

 bvi接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.






范例 :

ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if-fei-0/1/0/1)#interface mac-address offset 5删除fei-0/1/0/1接口MAC地址偏移。fei-0/1/0/1表示设备上的物理接口，其中”fei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if-fei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。





命令模式 :

 smartgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的MAC地址偏移为5。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address offset 5删除gei-0/1/0/1接口MAC地址偏移。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。





命令模式 :

 10G以太接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太接口模式:15,千兆以太接口模式:15,10G以太接口模式:15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的MAC地址偏移为5。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address offset 5删除gei-0/1/0/1接口MAC地址偏移。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。





命令模式 :

 以太子接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的MAC地址偏移为5。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address offset 5删除gei-0/1/0/1接口MAC地址偏移。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。





命令模式 :

 dsl接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

ulei子接口模式:15,dsl接口模式:15,ulei接口模式:15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的MAC地址偏移为5。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address offset 5删除gei-0/1/0/1接口MAC地址偏移。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。





命令模式 :

 smartgroup子接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if-fei-0/1/0/1)#interface mac-address offset 5删除fei-0/1/0/1接口MAC地址偏移。fei-0/1/0/1表示设备上的物理接口，其中”fei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if-fei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。





命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的MAC地址偏移为5。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address offset 5删除gei-0/1/0/1接口MAC地址偏移。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题





命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx子接口模式:15,qx接口模式:15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address offset 5删除gei-0/1/0/1接口MAC地址偏移。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address offset 


interface mac-address offset 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址偏移。no interface mac-address offset命令用于删除接口的MAC地址偏移。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。当设备上接口的MAC地址冲突时，可以通过配置MAC地址偏移，解决这样的问题。





命令模式 :

 bvi子接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address offset 
  ＜offset-value 
＞

no interface mac-address offset 








命令参数解释 :



参数|描述
---|---
＜offset-value＞|接口的MAC地址偏移量。取值范围：系统启动时用户可以配置系统支持的MAC地址数量，该数量即为MAC地址偏移量的取值范围。默认值：无。








缺省 :

0 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。接口缺省没有MAC地址偏移，子接口继承父接口的MAC地址偏移。如果父接口没有配置MAC偏移，则子接口的MAC偏移以父接口MAC地址为基础进行偏移，如果父接口配置了MAC偏移，则子接口的MAC偏移以父接口未配置MAC地址偏移前的地址为基础进行偏移。可以通过show interface命令查看接口的MAC地址。可以通过show ip interface命令查看接口的MAC地址偏移。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址偏移，如果设置二层接口的MAC地址偏移，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的MAC地址偏移为5。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address offset 5删除gei-0/1/0/1接口MAC地址偏移。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address offset





相关命令 :

无 




## interface mac-address 


interface mac-address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址。no interface mac-address命令用于恢复接口缺省的MAC地址。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。其中，前三个字节是由IEEE的注册管理机构RA负责给不同厂家分配的代码(高位24位)，也称为“编制上唯一的标识符”（Organizationally Unique Identifier)，后三个字节(低位24位)由各厂家自行指派给生产的适配器接口，称为扩展标识符（唯一性）。一个地址块可以生成224个不同的地址。MAC地址实际上就是适配器地址或适配器标识符EUI-48。





命令模式 :

 eth_dslgroup接口模式,supervlan接口模式  






命令默认权限级别 :

eth_dslgroup接口模式:15,supervlan接口模式:15 






命令格式 :


interface mac-address 
  ＜mac-address 
＞

no interface mac-address 








命令参数解释 :



参数|描述
---|---
＜mac-address＞|接口的MAC地址，采用十六进制数表示，共六个字节（48位），每两个字节未一段，用’.’分隔，例如：0019.8407.230a








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。可以通过show interface命令查看接口的MAC地址。接口MAC地址缺省为系统的基MAC地址 。子接口在没有配置MAC地址偏移的情况下，继承父接口的MAC地址。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址，如果设置二层接口的MAC地址，会提示：%Error 94: The L2 interface does not support this command.





范例 :

ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address 2222.3333.4444恢复gei-0/1/0/1接口的缺省MAC地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address





相关命令 :

无 




## interface mac-address 


interface mac-address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址。no interface mac-address命令用于恢复接口缺省的MAC地址。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。其中，前三个字节是由IEEE的注册管理机构RA负责给不同厂家分配的代码(高位24位)，也称为“编制上唯一的标识符”（Organizationally Unique Identifier)，后三个字节(低位24位)由各厂家自行指派给生产的适配器接口，称为扩展标识符（唯一性）。一个地址块可以生成224个不同的地址。MAC地址实际上就是适配器地址或适配器标识符EUI-48。





命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address 
  ＜mac-address 
＞

no interface mac-address 








命令参数解释 :



参数|描述
---|---
＜mac-address＞|接口的MAC地址，采用十六进制数表示，共六个字节（48位），每两个字节未一段，用’.’分隔，例如：0019.8407.230a








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。可以通过show interface命令查看接口的MAC地址。接口MAC地址缺省为系统的基MAC地址 。子接口在没有配置MAC地址偏移的情况下，继承父接口的MAC地址。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址，如果设置二层接口的MAC地址，会提示：%Error 94: The L2 interface does not support this command.





范例 :

ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address 2222.3333.4444恢复gei-0/1/0/1接口的缺省MAC地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address





相关命令 :

无 




## interface mac-address 


interface mac-address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址。no interface mac-address命令用于恢复接口缺省的MAC地址。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。其中，前三个字节是由IEEE的注册管理机构RA负责给不同厂家分配的代码(高位24位)，也称为“编制上唯一的标识符”（Organizationally Unique Identifier)，后三个字节(低位24位)由各厂家自行指派给生产的适配器接口，称为扩展标识符（唯一性）。一个地址块可以生成224个不同的地址。MAC地址实际上就是适配器地址或适配器标识符EUI-48。





命令模式 :

 10G以太接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太接口模式:15,千兆以太接口模式:15,10G以太接口模式:15 






命令格式 :


interface mac-address 
  ＜mac-address 
＞

no interface mac-address 








命令参数解释 :



参数|描述
---|---
＜mac-address＞|接口的MAC地址，采用十六进制数表示，共六个字节（48位），每两个字节未一段，用’.’分隔，例如：0019.8407.230a








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。可以通过show interface命令查看接口的MAC地址。接口MAC地址缺省为系统的基MAC地址 。子接口在没有配置MAC地址偏移的情况下，继承父接口的MAC地址。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址，如果设置二层接口的MAC地址，会提示：%Error 94: The L2 interface does not support this command.





范例 :

ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address 2222.3333.4444恢复gei-0/1/0/1接口的缺省MAC地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address





相关命令 :

无 




## interface mac-address 


interface mac-address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址。no interface mac-address命令用于恢复接口缺省的MAC地址。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。其中，前三个字节是由IEEE的注册管理机构RA负责给不同厂家分配的代码(高位24位)，也称为“编制上唯一的标识符”（Organizationally Unique Identifier)，后三个字节(低位24位)由各厂家自行指派给生产的适配器接口，称为扩展标识符（唯一性）。一个地址块可以生成224个不同的地址。MAC地址实际上就是适配器地址或适配器标识符EUI-48。





命令模式 :

 dsl接口模式,ulei接口模式  






命令默认权限级别 :

ulei接口模式:15,dsl接口模式:15 






命令格式 :


interface mac-address 
  ＜mac-address 
＞

no interface mac-address 








命令参数解释 :



参数|描述
---|---
＜mac-address＞|接口的MAC地址，采用十六进制数表示，共六个字节（48位），每两个字节未一段，用’.’分隔，例如：0019.8407.230a








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。可以通过show interface命令查看接口的MAC地址。接口MAC地址缺省为系统的基MAC地址 。子接口在没有配置MAC地址偏移的情况下，继承父接口的MAC地址。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址，如果设置二层接口的MAC地址，会提示：%Error 94: The L2 interface does not support this command.





范例 :

ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address 2222.3333.4444恢复gei-0/1/0/1接口的缺省MAC地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address





相关命令 :

无 




## interface mac-address 


interface mac-address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址。no interface mac-address命令用于恢复接口缺省的MAC地址。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。其中，前三个字节是由IEEE的注册管理机构RA负责给不同厂家分配的代码(高位24位)，也称为“编制上唯一的标识符”（Organizationally Unique Identifier)，后三个字节(低位24位)由各厂家自行指派给生产的适配器接口，称为扩展标识符（唯一性）。一个地址块可以生成224个不同的地址。MAC地址实际上就是适配器地址或适配器标识符EUI-48。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth接口模式:15,eth子接口模式:15 






命令格式 :


interface mac-address 
  ＜mac-address 
＞

no interface mac-address 








命令参数解释 :



参数|描述
---|---
＜mac-address＞|接口的MAC地址，采用十六进制数表示，共六个字节（48位），每两个字节未一段，用’.’分隔，例如：0019.8407.230a








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。可以通过show interface命令查看接口的MAC地址。接口MAC地址缺省为系统的基MAC地址 。子接口在没有配置MAC地址偏移的情况下，继承父接口的MAC地址。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址，如果设置二层接口的MAC地址，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置eth1.1接口的MAC地址。命令如下：ZXROSNG(config)#interface eth1.1ZXROSNG(config-if-eth1.1)#interface mac-address 2222.3333.4444恢复eth1.1接口的缺省MAC地址。命令如下：ZXROSNG(config)#interface eth1.1ZXROSNG(config-if-eth1.1)#no interface mac-address






相关命令 :

无 




## interface mac-address 


interface mac-address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址。no interface mac-address命令用于恢复接口缺省的MAC地址。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。其中，前三个字节是由IEEE的注册管理机构RA负责给不同厂家分配的代码(高位24位)，也称为“编制上唯一的标识符”（Organizationally Unique Identifier)，后三个字节(低位24位)由各厂家自行指派给生产的适配器接口，称为扩展标识符（唯一性）。一个地址块可以生成224个不同的地址。MAC地址实际上就是适配器地址或适配器标识符EUI-48。






命令模式 :

 bvi接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address 
  ＜mac-address 
＞

no interface mac-address 








命令参数解释 :



参数|描述
---|---
＜mac-address＞|接口的MAC地址，采用十六进制数表示，共六个字节（48位），每两个字节未一段，用’.’分隔，例如：0019.8407.230a








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。可以通过show interface命令查看接口的MAC地址。接口MAC地址缺省为系统的基MAC地址 。子接口在没有配置MAC地址偏移的情况下，继承父接口的MAC地址。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址，如果设置二层接口的MAC地址，会提示：%Error 94: The L2 interface does not support this command.





范例 :

ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address 2222.3333.4444恢复gei-0/1/0/1接口的缺省MAC地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address





相关命令 :

无 




## interface mac-address 


interface mac-address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的MAC地址。no interface mac-address命令用于恢复接口缺省的MAC地址。MAC(Medium/Media Access Control)地址，用来表示互联网上每一个站点的标识符，采用十六进制数表示，共六个字节（48位）。其中，前三个字节是由IEEE的注册管理机构RA负责给不同厂家分配的代码(高位24位)，也称为“编制上唯一的标识符”（Organizationally Unique Identifier)，后三个字节(低位24位)由各厂家自行指派给生产的适配器接口，称为扩展标识符（唯一性）。一个地址块可以生成224个不同的地址。MAC地址实际上就是适配器地址或适配器标识符EUI-48。





命令模式 :

 smartgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


interface mac-address 
  ＜mac-address 
＞

no interface mac-address 








命令参数解释 :



参数|描述
---|---
＜mac-address＞|接口的MAC地址，采用十六进制数表示，共六个字节（48位），每两个字节未一段，用’.’分隔，例如：0019.8407.230a








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口支持MAC地址的配置。可以通过show interface命令查看接口的MAC地址。接口MAC地址缺省为系统的基MAC地址 。子接口在没有配置MAC地址偏移的情况下，继承父接口的MAC地址。接口的MAC地址和MAC地址偏移不能同时配置。如果配置了MAC地址，再配置MAC地址偏移，会提示：%Error 121165: The interface has configured mac-address.如果配置了MAC地址偏移，再配置MAC地址，会提示：%Error 121164: The interface has configured mac-address offset.只有三层接口才允许配置MAC地址，如果设置二层接口的MAC地址，会提示：%Error 94: The L2 interface does not support this command.





范例 :

ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#interface mac-address 2222.3333.4444恢复gei-0/1/0/1接口的缺省MAC地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no interface mac-address





相关命令 :

无 




## interface portlist 


interface portlist 




命令功能 :

该命令用于批量创建逻辑接口和子接口。no interface portlist命令可以批量删除用户定义的逻辑接口和子接口。






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


interface portlist 
  ＜portlist 
＞
no interface portlist 
  ＜portlist 
＞
				






命令参数解释 :



参数|描述
---|---
＜portlist＞|批量创建或删除的接口名。一个接口段用”-”表示，例如：fei-0/1/0/1的1号到100号子接口表示为” fei-0/1/0/1.1-100”，1号到64号smartgroup接口表示为”smartgroup1-64”；多个接口段之间用”,”隔开，例如：ulei-0/1/0/1的1号到20号、50号到60号子接口表为”ulei-0/1/0/1.1-20,ulei-0/1/0/1.50-60”。取值范围：最多可同时支持配置10个批量创建或删除的接口名段，包含的接口总数最多可达到4094个。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于全局配置模式下，需要先进入全局配置模式，才能使用该命令。该命令支持以太子接口、ULEI子接口、smartgroup接口及其子接口的批量创建和删除。当物理接口正在加载中或者已经离线，不允许批量创建或者删除物理接口的子接口，会提示：%Error 121152: The interface cannot be accessed now不允许批量删除物理接口，会提示%Error 121001: Removal of physical interfaces is not permitted父接口不存在的情况下，不允许批量创建子接口，会提示：%Error 1226: Please create the parent interface first.批量删除父接口时，会一并删除子接口。批量创建接口成功后，可以通过show interface <interface-name>查看接口的相关信息。





范例 :

批量创建gei-0/1/0/1.1到gei-0/1/0/1.20的接口。gei-0/1/0/1.1-20表示设备物理接口gei-0/1/0/1的1-20号子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号，”.1-20”表示子接口号段，即1号到20号的所有子接口。命令如下：ZXROSNG(config)#interface portlist gei-0/1/0/1.1-20批量创建smartgroup1到smartgroup64的接口。smartgroup1-64表示smartgroup1到smartgroup64的接口，因为smartgroup为逻辑接口，在设备上没有具体物理位置，”1-64”表示接口号段，即1号到64号的所有smartgroup接口。命令如下：ZXROSNG(config)#interface portlist smartgroup1-64批量创建smartgroup1到smartgroup64，以及smartgroup1.1到smartgroup1.20的接口。smartgroup1-64表示smartgroup1到smartgroup64的接口，因为smartgroup为逻辑接口，在设备上没有具体物理位置，”1-64”表示接口号段，即1号到64号的所有smartgroup接口。smartgroup1.1-20表示smartgroup1接口的1-20号子接口，因为smartgroup为逻辑接口，在设备上没有具体物理位置，”1.1-20”中第一个”1”表示接口号，”.1-20”表示子接口号段，即1号到20号的所有子接口。命令如下：ZXROSNG(config)#interface portlist smartgroup1-64,smartgroup1.1-20批量删除gei-0/1/0/1.1到gei-0/1/0/1.20的接口：gei-0/1/0/1.1-20表示设备物理接口gei-0/1/0/1的1-20号子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号，”.1-20”表示子接口号段，即1号到20号的所有子接口。命令如下：ZXROSNG(config)#no interface portlist gei-0/1/0/1.1-20批量删除smartgroup1到smartgroup64的接口：smartgroup1-64表示smartgroup1到smartgroup64的接口，因为smartgroup为逻辑接口，在设备上没有具体物理位置，”1-64”表示接口号段，即1号到64号的所有smartgroup接口。命令如下：ZXROSNG(config)#no interface portlist smartgroup1-64批量删除smartgroup1到smartgroup64，已及smartgroup1.1到smartgroup1.20的接口。smartgroup1-64表示smartgroup1到smartgroup64的接口，因为smartgroup为逻辑接口，在设备上没有具体物理位置，”1-64”表示接口号段，即1号到64号的所有smartgroup接口。smartgroup1.1-20表示smartgroup1接口的1-20号子接口，因为smartgroup为逻辑接口，在设备上没有具体物理位置，”1.1-20”中第一个”1”表示接口号，”.1-20”表示子接口号段，即1号到20号的所有子接口。命令如下：ZXROSNG(config)#no interface portlist smartgroup1-64,smartgroup1.1-20






相关命令 :

无 




interface :

interface (全局配置模式) 




命令功能 :

该命令用于进入到接口配置模式，也可以根据用户需要，创建并进入逻辑接口或者子接口。no interface命令用于删除用户定义的逻辑接口和子接口。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


interface 
  {byname 
 ＜interface-byname 
＞|＜interface-name 
＞}
no interface 
  {byname 
 ＜interface-byname 
＞|＜interface-name 
＞}
				






命令参数解释 :



参数|描述
---|---
＜interface-byname＞|接口别名，通过byname命令配置，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。默认值：无。
＜interface-name＞|接口名，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于全局配置模式下，需要先进入全局配置模式，才能使用。目前支持的接口类型有：以太接口、POS接口、ATM接口、通道化接口、串口、管理口等物理接口和smartgroup、multilink、posgroup、supervlan、loopback、virtual_template等逻辑接口，部分接口又支持子接口。物理接口的命名由接口类型和接口位置信息组成，例如：gei-0/1/0/1，其中”gei-”表示为千兆以太接口，”0/1/0/1”这几个数字分别表示接口所在的框、槽、子槽、接口编号，其中接口编号从1开始，其他编号都是从0开始。管理口作为特殊的物理接口，全局仅存在一个，命名为”mgmt_eth”。逻辑接口的命名由接口类型和接口编号组成，接口编号从1开始。例如1号loopback接口的接口名为”loopback1”。子接口的命名为父接口名和子端口号组成，例如：gei-0/1/0/1.1表示gei-0/1/0/1接口的1号子接口，smartgroup2.3表示smartgroup2接口的3号子接口。如果接口配置了别名，可以通过接口别名进入接口配置模式，也可以通过接口别名删除接口。如果当前接口正在加载中或者已经离线，不允许进入该接口的配置模式，会提示：%Error 121152: The interface cannot be accessed now不允许删除物理接口，如果命令删除物理接口，会提示%Error 121001: Removal of physical interfaces is not permitted父接口不存在的情况下，不允许创建子接口。如果命令创建，会提示：%Error 1226: Please create the parent interface first.删除父接口时，会一并删除子接口。例如：同时存在smartgroup1和smartgroup1.1这对父子接口，如果命令删除smartgroup1接口，会同时删除两个接口。创建接口成功后，可以通过show interface <interface-name>查看接口的相关信息。





范例 :

创建gei-0/1/0/1.1接口并进入接口配置模式。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1” 依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#设置gei-0/1/0/1.1接口的别名为ether1.1，并通过接口别名进入gei-0/1/0/1.1接口的配置模式。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1” 依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#byname ether1.1ZXROSNG(config-if-gei-0/1/0/1.1)#exitZXROSNG(config)#interface byname ether1.1ZXROSNG(config-if-gei-0/1/0/1.1)#删除gei-0/1/0/1.1接口。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1” 依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#no interface gei-0/1/0/1.1设置gei-0/1/0/1.1接口的别名为ether1.1，并通过接口别名删除gei-0/1/0/1.1接口。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1” 依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#byname ether1.1ZXROSNG(config-if-gei-0/1/0/1.1)#exitZXROSNG(config)#no interface byname ether1.1





相关命令 :

byname 




interface :

interface (CPS模式) 




命令功能 :

进入控制面安全接口配置模式 






命令模式 :

 CPS模式  






命令默认权限级别 :

15 






命令格式 :



interface 
  ＜interface-name 
＞







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#control-plane-security ZXROSNG(config-cps)#interface fei-0/1/0/1 ZXROSNG(config-cps-if-fei-0/1/0/1)#






相关命令 :

无 




ip address :

ip address 




命令功能 :

该命令工作于管理口配置模式下，用于设置管理口的IP地址。no ip address命令用于删除管理口的IP地址。管理口配置了IP地址后，则可以通过该IP地址登陆管理口，进行版本下载等操作。





命令模式 :

 管理口接口模式  






命令默认权限级别 :

15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于管理口配置模式下，需要先进入管理口配置模式，才能使用。管理口只能配置一个主地址，不支持配置辅地址，且配置主地址时，也不支持配置广播地址，管理口的广播地址缺省为255.255.255.255。系统在boot时会配置一个IP地址和子网掩码，该地址和掩码即为管理口缺省的IP地址。    可以通过show interface、show ip interface brief、show ip interface命令查看管理口的IP地址。





范例 :

配置管理口上的IP地址。mgmt_eth表示设备的管理口，192.168.5.250为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#ip addr 192.168.5.250 255.255.255.0配置管理口上的IP地址。mgmt_eth表示设备的管理口，192.168.5.250/24表示IP地址和掩码，其中”192.168.5.250”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#ip addr 192.168.5.250/24删除管理口上的IP地址。mgmt_eth表示设备的管理口，192.168.5.250为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ip address 192.168.5.250 255.255.255.0删除管理口上的IP地址。mgmt_eth表示设备的管理口，192.168.5.250/24表示IP地址和掩码，其中”192.168.5.250”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ip address 192.168.5.250/24删除管理口上的IP地址。mgmt_eth表示设备的管理口。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ip address





相关命令 :

show ip interface briefshow ip interface 




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 ATM子接口模式,ATM接口模式,atm_dslgroup接口模式,dialer接口模式,dsl接口模式,eth_dslgroup子接口模式,eth_dslgroup接口模式,posgroup接口模式,pos子接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式,virtual_template子接口模式  






命令默认权限级别 :

eth_dslgroup接口模式:15,dsl接口模式:15,serial接口模式:15,posgroup接口模式:15,atm_dslgroup接口模式:15,ATM接口模式:15,dialer接口模式:15,ATM子接口模式:15,ulei接口模式:15,pos子接口模式:15,vbui子接口模式:15,virtual_template子接口模式:15,ulei子接口模式:15,eth_dslgroup子接口模式:15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi子接口模式:15,bvi接口模式:15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。    IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。






范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address






相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 multilink接口模式,pos接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,通道化ce1接口模式:15,multilink接口模式:15,pos接口模式:15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 以太子接口模式,千兆以太接口模式  






命令默认权限级别 :

千兆以太接口模式:15,以太子接口模式:15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 10G以太接口模式,loopback接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式  






命令默认权限级别 :

以太接口模式:15,smartgroup子接口模式:15,smartgroup接口模式:15,10G以太接口模式:15,loopback接口模式:15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 virtual_template接口模式  






命令默认权限级别 :

15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 vbui接口模式  






命令默认权限级别 :

15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 IPv6隧道接口模式,supervlan接口模式,te隧道接口模式  






命令默认权限级别 :

supervlan接口模式:15,IPv6隧道接口模式:15,te隧道接口模式:15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。    IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth接口模式:15,eth子接口模式:15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置eth1接口上的IP主地址。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#ip address 1.1.1.1 255.255.255.0配置eth2接口上的IP主地址。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface eth2ZXROSNG(config-if-eth2)#ip address 2.2.2.2/24配置eth1接口上的IP辅地址。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#ip address 1.1.1.2 255.255.255.0 secondary配置eth2接口上的IP辅地址。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface eth2ZXROSNG(config-if-eth2)#ip address 2.2.2.4/24 secondary删除eth1接口上的IP地址。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#no ip address 1.1.1.2 255.255.255.0删除eth2接口上的IP地址。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface eth2ZXROSNG(config-if-eth2)#no ip address 2.2.2.2/24删除eth1接口上的所有IP地址。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#no ip address






相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。    IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。






范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address






相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。





命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx子接口模式:15,qx接口模式:15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。





范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address





相关命令 :

show ip interface briefshow ip interface




ip address :

ip address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP地址。no ip address命令用于删除接口的IP地址。IP地址是一种在Internet上的给主机编址的方式，也称为网际协议地址。IP地址是一个32位的二进制数，通常被分割为4个“8位二进制数”（也就是4个字节），用“点分十进制”表示成（a.b.c.d）的形式，其中，a,b,c,d都是0~255之间的十进制整数。IP地址分为A、B、C、D、E5类，分别适合不同容量的网络。A类IP地址是指，在IP地址的四段号码中，第一段号码为网络号码，剩下的三段号码为本地计算机的号码。如果用二进制表示IP地址的话，A类IP地址就由1字节的网络地址和3字节主机地址组成，网络地址的最高位必须是“0”。A类IP地址中网络的标识长度为8位，主机标识的长度为24位，A类网络地址数量较少，可以用于主机数达1600多万台的大型网络。A类IP地址 地址范围1.0.0.0到127.255.255.255。B类IP地址是指，在IP地址的四段号码中，前两段号码为网络号码。如果用二进制表示IP地址的话，B类IP地址就由2字节的网络地址和2字节主机地址组成，网络地址的最高位必须是“10”。B类IP地址中网络的标识长度为16位，主机标识的长度为16位，B类网络地址适用于中等规模的网络，每个网络所能容纳的计算机数为6万多台。B类IP地址地址范围128.0.0.0-191.255.255.255。C类IP地址是指，在IP地址的四段号码中，前三段号码为网络号码，剩下的一段号码为本地计算机的号码。如果用二进制表示IP地址的话，C类IP地址就由3字节的网络地址和1字节主机地址组成，网络地址的最高位必须是“110”。C类IP地址中网络的标识长度为24位，主机标识的长度为8位，C类网络地址数量较多，适用于小规模的局域网络，每个网络最多只能包含254台计算机。C类IP地址范围192.0.0.0-223.255.255.255。D类IP地址在历史上被叫做多播地址(multicast address)，即组播地址。在以太网中，多播地址命名了一组应该在这个网络中应用接收到一个分组的站点。多播地址的最高位必须是“1110”，范围从224.0.0.0到239.255.255.255。E类IP地址，以“1111”开始，为将来使用保留。其中240.0.0.0~255.255.255.254作为保留地址，255.255.255.255作为广播地址。常用的地址类型是B和C两类。该命令支持配置的为A、B、C三类地址。






命令模式 :

 mte隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip address 
  {＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞} [{＜ipv4-address 
＞|secondary 
}]
no ip address 
  [{＜ipv4-address 
＞ ＜ipv4-address-mask 
＞|＜ip-address/mask-length 
＞}]
				






命令参数解释 :



参数|描述
---|---
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ipv4-address-mask＞|IP子网掩码，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
＜ip-address/mask-length＞|IP地址/掩码长度。IP地址为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。掩码长度为整数，取值范围：1-32。默认值：无。
＜ipv4-address＞|IP地址，为十进制点分形式：x.x.x.x，其中每个x为0~255之间的十进制整数。默认值：无。
secondary|辅地址标识，表示配置的地址为辅地址。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。在删除接口IP地址时，既支持删除指定的IP地址，也支持删除当前接口所有的IP地址。可以通过show interface、show ip interface brief、show ip interface命令查看接口的IP地址。    IP地址分为主地址和辅地址，一个接口只能配置一个主地址，但可以配置多个辅地址。一个接口最多可以同时配置15个辅地址，如果配置超出该数量，会提示：%Error 121011: The number of addresses of this type comes to the limit接口在缺省的情况下，没有配置IP地址。用户如果要配置IP地址，必须先配置主地址，在没有主地址的情况下，不允许配置辅地址。如果在没有配置主地址的情况下，直接配置辅地址，会提示：%Error 121008: The interface has no primary address。同样，在配置了辅地址的情况下，不允许删除主地址。如果在配置了辅地址的情况下，直接删除主地址，会提示：%Error 121009: Must delete all secondary addresses first只有三层接口才允许配置IP地址，如果在二层接口上配置IP地址，会提示：%Error 94: The L2 interface does not support this command.接口的IP地址和地址借用(ip unnumbered)不能同时配置，如果接口已经配置了地址借用，再配置IP地址，会提示：%Error 1044: Must no ip unnumbered first.同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同的地址，或者同网段的地址。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的主IP地址冲突，会提示：%Error 121030: The IP x.x.x.x overlaps with xxx，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。如果是和辅IP地址冲突，会提示：%Error 121031: The IP x.x.x.x is assigned as a secondary address on xxx，同样，其中x.x.x.x表示冲突的网段，xxx表示冲突的地址所属接口。






范例 :

配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.1 255.255.255.0配置gei-0/1/0/1接口上的IP主地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，24为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.2/24配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.2为IP地址，255.255.255.0为掩码，secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 1.1.1.2 255.255.255.0 secondary配置gei-0/1/0/1接口上的IP辅地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。secondary为辅地址标识。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip address 2.2.2.4/24 secondary删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1.1.1.1为IP地址，255.255.255.0为掩码。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 1.1.1.2 255.255.255.0删除gei-0/1/0/1接口上的IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2.2.2.2/24表示IP地址和掩码，其中”2.2.2.2”为IP地址，”24”为掩码长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address 2.2.2.2/24删除gei-0/1/0/1接口上的所有IP地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip address






相关命令 :

show ip interface briefshow ip interface




## ip load-sharing 


ip load-sharing 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担策略，no ip load-sharing per-packet命令用于恢复接口缺省的负荷分担策略。当到达某一目的IP地址的数据流存在多个链路，并且这些链路的路由具有相同的优先级（等价路由），可以通过负荷分担使流量均衡分担到各个链路上。当接口上需要启用负荷分担功能时，则需要配置负荷分担策略。负荷分担的策略有逐流分担策略和逐包分担策略。逐流分担策略以流为单位，流量按照权重分担到各个链路上。逐包分担策略以报文为单位，轮询选择接口进行报文的负荷分担。





命令模式 :

 ATM子接口模式,ATM接口模式,dialer接口模式,dsl接口模式,gre隧道接口模式,posgroup接口模式,serial接口模式  






命令默认权限级别 :

serial接口模式:15,dsl接口模式:15,ATM子接口模式:15,dialer接口模式:15,ATM接口模式:15,posgroup接口模式:15,gre隧道接口模式:15 






命令格式 :


ip load-sharing 
  {per-destination 
|per-packet 
}

no ip load-sharing 
 per-packet 








命令参数解释 :



参数|描述
---|---
per-destination|和per-packet为二选一，表示负荷分担策略，选择per-destination表示将接口负荷分担策略设置成逐流负荷分担。
per-packet|和per-destination为二选一，表示负荷分担策略，选择per-packet表示将接口负荷分担策略设置成逐包负荷分担。no ip load-sharing per-packet命令只能选择per-packet，表示删除逐包负荷分担策略，恢复成缺省的逐流负荷分担。








缺省 :

缺省逐流分担策略 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担策略的配置。接口缺省为逐流分担策略。





范例 :

配置gei-0/1/0/1接口为逐流负荷分担。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip load-sharing per-destination配置gei-0/1/0/1接口为逐包负荷分担。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip load-sharing per-packet恢复gei-0/1/0/1接口的缺省负荷分担策略。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip load-sharing per-packet





相关命令 :

无 




## ip load-sharing 


ip load-sharing 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担策略，no ip load-sharing per-packet命令用于恢复接口缺省的负荷分担策略。当到达某一目的IP地址的数据流存在多个链路，并且这些链路的路由具有相同的优先级（等价路由），可以通过负荷分担使流量均衡分担到各个链路上。当接口上需要启用负荷分担功能时，则需要配置负荷分担策略。负荷分担的策略有逐流分担策略和逐包分担策略。逐流分担策略以流为单位，流量按照权重分担到各个链路上。逐包分担策略以报文为单位，轮询选择接口进行报文的负荷分担。






命令模式 :

 te隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip load-sharing 
  {per-destination 
|per-packet 
}

no ip load-sharing 
 per-packet 








命令参数解释 :



参数|描述
---|---
per-destination|和per-packet为二选一，表示负荷分担策略，选择per-destination表示将接口负荷分担策略设置成逐流负荷分担。
per-packet|和per-destination为二选一，表示负荷分担策略，选择per-packet表示将接口负荷分担策略设置成逐包负荷分担。no ip load-sharing per-packet命令只能选择per-packet，表示删除逐包负荷分担策略，恢复成缺省的逐流负荷分担。








缺省 :

缺省逐流分担策略 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担策略的配置。接口缺省为逐流分担策略。






范例 :

配置gei-0/1/0/1接口为逐流负荷分担。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip load-sharing per-destination配置gei-0/1/0/1接口为逐包负荷分担。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip load-sharing per-packet恢复gei-0/1/0/1接口的缺省负荷分担策略。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip load-sharing per-packet






相关命令 :

无 




## ip load-sharing 


ip load-sharing 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担策略，no ip load-sharing per-packet命令用于恢复接口缺省的负荷分担策略。当到达某一目的IP地址的数据流存在多个链路，并且这些链路的路由具有相同的优先级（等价路由），可以通过负荷分担使流量均衡分担到各个链路上。当接口上需要启用负荷分担功能时，则需要配置负荷分担策略。负荷分担的策略有逐流分担策略和逐包分担策略。逐流分担策略以流为单位，流量按照权重分担到各个链路上。逐包分担策略以报文为单位，轮询选择接口进行报文的负荷分担。






命令模式 :

 bvi子接口模式,bvi接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

bvi子接口模式:15,ulei子接口模式:15,ulei接口模式:15,bvi接口模式:15 






命令格式 :


ip load-sharing 
  {per-destination 
|per-packet 
}

no ip load-sharing 
 per-packet 








命令参数解释 :



参数|描述
---|---
per-destination|和per-packet为二选一，表示负荷分担策略，选择per-destination表示将接口负荷分担策略设置成逐流负荷分担。
per-packet|和per-destination为二选一，表示负荷分担策略，选择per-packet表示将接口负荷分担策略设置成逐包负荷分担。no ip load-sharing per-packet命令只能选择per-packet，表示删除逐包负荷分担策略，恢复成缺省的逐流负荷分担。








缺省 :

缺省逐流分担策略 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担策略的配置。接口缺省为逐流分担策略。






范例 :

配置gei-0/1/0/1接口为逐流负荷分担。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip load-sharing per-destination配置gei-0/1/0/1接口为逐包负荷分担。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip load-sharing per-packet恢复gei-0/1/0/1接口的缺省负荷分担策略。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip load-sharing per-packet






相关命令 :

无 




## ip load-sharing 


ip load-sharing 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担策略，no ip load-sharing per-packet命令用于恢复接口缺省的负荷分担策略。当到达某一目的IP地址的数据流存在多个链路，并且这些链路的路由具有相同的优先级（等价路由），可以通过负荷分担使流量均衡分担到各个链路上。当接口上需要启用负荷分担功能时，则需要配置负荷分担策略。负荷分担的策略有逐流分担策略和逐包分担策略。逐流分担策略以流为单位，流量按照权重分担到各个链路上。逐包分担策略以报文为单位，轮询选择接口进行报文的负荷分担。





命令模式 :

 10G以太接口模式,multilink接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,通道化ce1接口模式:15,smartgroup子接口模式:15,multilink接口模式:15,pos接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :


ip load-sharing 
  {per-destination 
|per-packet 
}

no ip load-sharing 
 per-packet 








命令参数解释 :



参数|描述
---|---
per-destination|和per-packet为二选一，表示负荷分担策略，选择per-destination表示将接口负荷分担策略设置成逐流负荷分担。
per-packet|和per-destination为二选一，表示负荷分担策略，选择per-packet表示将接口负荷分担策略设置成逐包负荷分担。no ip load-sharing per-packet命令只能选择per-packet，表示删除逐包负荷分担策略，恢复成缺省的逐流负荷分担。








缺省 :

缺省逐流分担策略 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担策略的配置。接口缺省为逐流分担策略。





范例 :

配置gei-0/1/0/1接口为逐流负荷分担。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip load-sharing per-destination配置gei-0/1/0/1接口为逐包负荷分担。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip load-sharing per-packet恢复gei-0/1/0/1接口的缺省负荷分担策略。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip load-sharing per-packet





相关命令 :

无 




## ip load-sharing 


ip load-sharing 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担策略，no ip load-sharing per-packet命令用于恢复接口缺省的负荷分担策略。当到达某一目的IP地址的数据流存在多个链路，并且这些链路的路由具有相同的优先级（等价路由），可以通过负荷分担使流量均衡分担到各个链路上。当接口上需要启用负荷分担功能时，则需要配置负荷分担策略。负荷分担的策略有逐流分担策略和逐包分担策略。逐流分担策略以流为单位，流量按照权重分担到各个链路上。逐包分担策略以报文为单位，轮询选择接口进行报文的负荷分担。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth接口模式:15,eth子接口模式:15 






命令格式 :


ip load-sharing 
  {per-destination 
|per-packet 
}

no ip load-sharing 
 per-packet 








命令参数解释 :



参数|描述
---|---
per-destination|和per-packet为二选一，表示负荷分担策略，选择per-destination表示将接口负荷分担策略设置成逐流负荷分担。
per-packet|和per-destination为二选一，表示负荷分担策略，选择per-packet表示将接口负荷分担策略设置成逐包负荷分担。no ip load-sharing per-packet命令只能选择per-packet，表示删除逐包负荷分担策略，恢复成缺省的逐流负荷分担。








缺省 :

缺省逐流分担策略 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担策略的配置。接口缺省为逐流分担策略。





范例 :

配置eth1接口为逐流负荷分担。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#ip load-sharing per-destination配置eth1接口为逐包负荷分担。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#ip load-sharing per-packet恢复eth1接口的缺省负荷分担策略。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#no ip load-sharing per-packet






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。





命令模式 :

 10G以太接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

千兆以太接口模式:15,10G以太接口模式:15,以太接口模式:15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为$#50397237#$~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip mtu 2000恢复gei-0/1/0/1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。





命令模式 :

 eth接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜68-9202 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜68-9202＞|接口的IP MTU值。配置范围为$#50397237#$~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置eth1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#ip mtu 2000恢复eth1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 pos接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

4470 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置pos-0/1/1/1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface pos-0/1/1/1ZXROSNG(config-if-pos-0/1/1/1)#ip mtu 2000恢复pos-0/1/1/1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface pos-0/1/1/1ZXROSNG(config-if-pos-0/1/1/1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 multilink接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397250#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置multilink1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface multilink1ZXROSNG(config-if-multilink1)#ip mtu 2000恢复multilink1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface multilink1ZXROSNG(config-if-multilink1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 ATM接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397249#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置atm-0/1/0/1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface atm-0/1/0/1ZXROSNG(config-if-atm-0/1/0/1)#ip mtu 2000恢复atm-0/1/0/1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface atm-0/1/0/1ZXROSNG(config-if-atm-0/1/0/1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 通道化ce1接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置ce1-0/1/0/1:1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface ce1-0/1/0/1:1ZXROSNG(config-if-ce1-0/1/0/1:1)#ip mtu 2000恢复ce1-0/1/0/1:1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface ce1-0/1/0/1:1ZXROSNG(config-if-ce1-0/1/0/1:1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 smartgroup子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为$#50397239#$~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置smartgroup1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface smartgroup1.1ZXROSNG(config-if-smartgroup1.1)#ip mtu 2000恢复smartgroup1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface smartgroup1.1ZXROSNG(config-if-smartgroup1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 以太子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为$#50397239#$~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gei-0/1/0/1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#ip mtu 2000恢复gei-0/1/0/1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 eth子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜68-9194 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜68-9194＞|接口的IP MTU值。配置范围为$#50397239#$~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置eth1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface eth1.1ZXROSNG(config-if-eth1.1)#ip mtu 2000恢复eth1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface eth1.1ZXROSNG(config-if-eth1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。





命令模式 :

 loopback接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置loopback1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface loopback1ZXROSNG(config-if-loopback1)#ip mtu 2000恢复loopback1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface loopback1ZXROSNG(config-if-loopback1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。





命令模式 :

 smartgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为$#50397237#$~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置smartgroup1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#ip mtu 2000恢复smartgroup1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

supervlan接口缺省为1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置supervlan1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#ip mtu 2000恢复supervlan1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 ATM子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397249#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置atm-0/1/0/1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface atm-0/1/0/1.1ZXROSNG(config-if-atm-0/1/0/1.1)#ip mtu 2000恢复atm-0/1/0/1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface atm-0/1/0/1.1ZXROSNG(config-if-atm-0/1/0/1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 virtual_template接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

当接口模式为PPP时，缺省值为1430；当接口模式为ps-core时，缺省值为1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置virtual_template1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface virtual_template1ZXROSNG(config-if-virtual_template1)#ip mtu 2000恢复virtual_template1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface virtual_template1ZXROSNG(config-if-virtual_template1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 IPv6隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置v6_tunnel1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#ip mtu 2000恢复v6_tunnel1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gre_tunnel1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#ip mtu 2000恢复gre_tunnel1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 te隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置te_tunnel1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#ip mtu 2000恢复te_tunnel1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 posgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

4470 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置posgroup1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if-posgroup1)#ip mtu 2000恢复posgroup1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if-posgroup1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 vbui接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置vbui1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface vbui1ZXROSNG(config-if-vbui1)#ip mtu 2000恢复vbui1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface vbui1ZXROSNG(config-if-vbui1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 ulei接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置ulei-0/1/0/1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1ZXROSNG(config-if-ulei-0/1/0/1)#ip mtu 2000恢复ulei-0/1/0/1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1ZXROSNG(config-if-ulei-0/1/0/1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 bvi接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置bvi1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#ip mtu 2000恢复bvi1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 bvi子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置bvi1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#ip mtu 2000恢复bvi1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为$#50397237#$~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置vlan接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface vlanZXROSNG(config-if-vlan)#ip mtu 2000恢复vlan接口缺省IP MTU。命令如下：ZXROSNG(config)#interface vlanZXROSNG(config-if-vlan)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 pos子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

4470 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置pos-0/1/1/1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface pos-0/1/1/1.1ZXROSNG(config-if-pos-0/1/1/1.1)#ip mtu 2000恢复pos-0/1/1/1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface pos-0/1/1/1.1ZXROSNG(config-if-pos-0/1/1/1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 vbui子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置vbui1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface vbui1.1ZXROSNG(config-if-vbui1.1)#ip mtu 2000恢复vbui1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface vbui1.1ZXROSNG(config-if-vbui1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 通道化cpos_e1接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置cpos3_e1-1/2/1/1.1/1/1:1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1)#ip mtu 2000恢复cpos3_e1-1/2/1/1.1/1/1:1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置cpos3_e1-1/2/1/1.1/1/1:1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1.1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1.1)#ip mtu 2000恢复cpos3_e1-1/2/1/1.1/1/1:1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1.1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 ulei子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置ulei-0/1/0/1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1.1ZXROSNG(config-if-ulei-0/1/0/1.1)#ip mtu 2000恢复ulei-0/1/0/1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1.1ZXROSNG(config-if-ulei-0/1/0/1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置ipsec_tunnel1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface ipsec_tunnel1ZXROSNG(config-if-ipsec_tunnel1)#ip mtu 2000恢复ipsec_tunnel1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface ipsec_tunnel1ZXROSNG(config-if-ipsec_tunnel1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 eth_dslgroup子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置eth_dslgroup1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface eth_dslgroup1.1ZXROSNG(config-if-eth_dslgroup1.1)#ip mtu 2000恢复eth_dslgroup1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface eth_dslgroup1.1ZXROSNG(config-if-eth_dslgroup1.1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 qx子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397251#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置qx1.1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface qx1.1ZXROSNG(config-if-qx1.1)#ip mtu 2000恢复qx1.1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface qx1.1ZXROSNG(config-if-qx1.1)#no ip mtu






相关命令 :

无。 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。 






命令模式 :

 qx接口模式  






命令默认权限级别 :

15 






命令格式 :



ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置qx1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface qx1ZXROSNG(config-if-qx1)#ip mtu 2000恢复qx1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface qx1ZXROSNG(config-if-qx1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 eth_dslgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置eth_dslgroup1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface eth_dslgroup1ZXROSNG(config-if-eth_dslgroup1)#ip mtu 2000恢复eth_dslgroup1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface eth_dslgroup1ZXROSNG(config-if-eth_dslgroup1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 atm_dslgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397249#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置atm_dslgroup1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface atm_dslgroup1ZXROSNG(config-if-atm_dslgroup1)#ip mtu 2000恢复atm_dslgroup1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface atm_dslgroup1ZXROSNG(config-if-atm_dslgroup1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 serial接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置serial-0/1/0/1接口的IP MTU为2000。命令如下：ZXROSNG(config)#interface serial-0/1/0/1ZXROSNG(config-if-serial-0/1/0/1)#ip mtu 2000恢复serial-0/1/0/1接口缺省IP MTU。命令如下：ZXROSNG(config)#interface serial-0/1/0/1ZXROSNG(config-if-serial-0/1/0/1)#no ip mtu






相关命令 :

无 




ip mtu :

ip mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IP协议最大传输单元，no ip mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。当报文大于IP MTU时，会将数据包丢弃。






命令模式 :

 dialer接口模式  






命令默认权限级别 :

15 






命令格式 :


ip mtu 
  ＜IP-MTU 
＞

no ip mtu 








命令参数解释 :



参数|描述
---|---
＜IP-MTU＞|接口的IP MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

4470 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface、show ip interface命令查看生效的IP MTU值。只有三层接口才允许配置IP MTU，如果在二层接口上配置IP MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

1. 配置接口的IP MTUZXROSNG(config)#interface dialer1ZXROSNG(config-if-dialer1)#ip mtu 15802. 删除接口的IP MTUZXROSNG(config)#interface dialer1ZXROSNG(config-if-dialer1)#no ip mtu





相关命令 :

无 




## ip unnumbered 


ip unnumbered 




命令功能 :

该命令工作于接口配置模式下，用于设置接口借用IP地址，no ip unnumbered命令用于解除借用关系。借用IP地址功能，最主要的目的就是节省宝贵的IP地址资源。一个接口如果没有IP地址就无法生成路由，也就无法转发报文。借用IP地址的实质就是：一个接口上没有配置IP地址，但是还想使用该接口，就向其它有IP地址的接口借一个IP地址过来，以使该接口能正常使用。如果被借用接口没有IP地址，则借用接口的IP地址为0.0.0.0。





命令模式 :

 dsl接口模式,pos子接口模式,te隧道接口模式  






命令默认权限级别 :

pos子接口模式:15,dsl接口模式:15,te隧道接口模式:15 






命令格式 :


ip unnumbered 
  ＜interface-name 
＞

no ip unnumbered 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|借用IP地址的接口的接口名，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。可以通过show ip interface brief命令查询当前设备上的接口。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。POS接口及其子接口、通道化接口、multilink接口、virtual_template接口、gre_tunnel接口、te_tunnel接口、ipsec_tunnel接口和dsl接口支持接口IP地址借用的配置。在缺省情况下，接口没有地址借用关系。借用IP地址，仅能借用接口的主IP地址，该借用关系对辅地址无效。配置借用IP地址生效后，可以通过show ip interface、show interface命令查看借用关系以及借用到的IP地址。只有三层接口才允许配置IP 地址借用，如果在二层接口上配置IP 地址借用，会提示：%Error 94: The L2 interface does not support this command.接口不能同时配置IP地址又借用其他接口的IP地址。当接口已经配置了IP地址，再配置借用IP地址时，会提示：%Error 121007: Current interface already has an IP address。当接口已经配置了借用IP地址，再配置IP地址时，会提示：%Error 1044: Must no ip unnumbered first.接口不能借用自己的IP地址，如果配置IP地址借用自身，会提示：%Error 121012: Cannot use self接口本身和被借用地址的接口必须同在公网路由或者在同一个私网路由中。否则配置IP地址借用，会提示：%Error 120607: Can not configure IP unnumbered interface which is not in the same VPN.IP地址借用关系不支持嵌套，例如：A接口借用B接口的IP地址，则C接口不能再借用A接口的IP地址。如果进行配置，会提示：%Error 121023: Interface xxx whose IP has already unnumbered another interface, does not support nesting，其中xxx即为上文所说的A接口。配置IP地址借用必须借用已经存在的接口，如果设置借用不存在的接口，会提示：%Error 121134: No such unnumbered interface





范例 :

配置te_tunnel1接口借用loopback1接口上的IP地址。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。loopback为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#ip unnumbered loopback1解除te_tunnel1接口的地址借用关系。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#no ip unnumbered





相关命令 :

无 




## ip unnumbered 


ip unnumbered 




命令功能 :

该命令工作于接口配置模式下，用于设置接口借用IP地址，no ip unnumbered命令用于解除借用关系。借用IP地址功能，最主要的目的就是节省宝贵的IP地址资源。一个接口如果没有IP地址就无法生成路由，也就无法转发报文。借用IP地址的实质就是：一个接口上没有配置IP地址，但是还想使用该接口，就向其它有IP地址的接口借一个IP地址过来，以使该接口能正常使用。如果被借用接口没有IP地址，则借用接口的IP地址为0.0.0.0。





命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


ip unnumbered 
  ＜interface-name 
＞

no ip unnumbered 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|借用IP地址的接口的接口名，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。可以通过show ip interface brief命令查询当前设备上的接口。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。POS接口及其子接口、通道化接口、multilink接口、virtual_template接口、gre_tunnel接口、te_tunnel接口、ipsec_tunnel接口和dsl接口支持接口IP地址借用的配置。在缺省情况下，接口没有地址借用关系。借用IP地址，仅能借用接口的主IP地址，该借用关系对辅地址无效。配置借用IP地址生效后，可以通过show ip interface、show interface命令查看借用关系以及借用到的IP地址。只有三层接口才允许配置IP 地址借用，如果在二层接口上配置IP 地址借用，会提示：%Error 94: The L2 interface does not support this command.接口不能同时配置IP地址又借用其他接口的IP地址。当接口已经配置了IP地址，再配置借用IP地址时，会提示：%Error 121007: Current interface already has an IP address。当接口已经配置了借用IP地址，再配置IP地址时，会提示：%Error 1044: Must no ip unnumbered first.接口不能借用自己的IP地址，如果配置IP地址借用自身，会提示：%Error 121012: Cannot use self接口本身和被借用地址的接口必须同在公网路由或者在同一个私网路由中。否则配置IP地址借用，会提示：%Error 120607: Can not configure IP unnumbered interface which is not in the same VPN.IP地址借用关系不支持嵌套，例如：A接口借用B接口的IP地址，则C接口不能再借用A接口的IP地址。如果进行配置，会提示：%Error 121023: Interface xxx whose IP has already unnumbered another interface, does not support nesting，其中xxx即为上文所说的A接口。配置IP地址借用必须借用已经存在的接口，如果设置借用不存在的接口，会提示：%Error 121134: No such unnumbered interface





范例 :

配置te_tunnel1接口借用loopback1接口上的IP地址。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。loopback为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#ip unnumbered loopback1解除te_tunnel1接口的地址借用关系。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#no ip unnumbered





相关命令 :

无 




## ip unnumbered 


ip unnumbered 




命令功能 :

该命令工作于接口配置模式下，用于设置接口借用IP地址，no ip unnumbered命令用于解除借用关系。借用IP地址功能，最主要的目的就是节省宝贵的IP地址资源。一个接口如果没有IP地址就无法生成路由，也就无法转发报文。借用IP地址的实质就是：一个接口上没有配置IP地址，但是还想使用该接口，就向其它有IP地址的接口借一个IP地址过来，以使该接口能正常使用。如果被借用接口没有IP地址，则借用接口的IP地址为0.0.0.0。





命令模式 :

 virtual_template接口模式  






命令默认权限级别 :

15 






命令格式 :


ip unnumbered 
  ＜interface-name 
＞

no ip unnumbered 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|借用IP地址的接口的接口名，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。可以通过show ip interface brief命令查询当前设备上的接口。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。POS接口及其子接口、通道化接口、multilink接口、virtual_template接口、gre_tunnel接口、te_tunnel接口、ipsec_tunnel接口和dsl接口支持接口IP地址借用的配置。在缺省情况下，接口没有地址借用关系。借用IP地址，仅能借用接口的主IP地址，该借用关系对辅地址无效。配置借用IP地址生效后，可以通过show ip interface、show interface命令查看借用关系以及借用到的IP地址。只有三层接口才允许配置IP 地址借用，如果在二层接口上配置IP 地址借用，会提示：%Error 94: The L2 interface does not support this command.接口不能同时配置IP地址又借用其他接口的IP地址。当接口已经配置了IP地址，再配置借用IP地址时，会提示：%Error 121007: Current interface already has an IP address。当接口已经配置了借用IP地址，再配置IP地址时，会提示：%Error 1044: Must no ip unnumbered first.接口不能借用自己的IP地址，如果配置IP地址借用自身，会提示：%Error 121012: Cannot use self接口本身和被借用地址的接口必须同在公网路由或者在同一个私网路由中。否则配置IP地址借用，会提示：%Error 120607: Can not configure IP unnumbered interface which is not in the same VPN.IP地址借用关系不支持嵌套，例如：A接口借用B接口的IP地址，则C接口不能再借用A接口的IP地址。如果进行配置，会提示：%Error 121023: Interface xxx whose IP has already unnumbered another interface, does not support nesting，其中xxx即为上文所说的A接口。配置IP地址借用必须借用已经存在的接口，如果设置借用不存在的接口，会提示：%Error 121134: No such unnumbered interface





范例 :

配置te_tunnel1接口借用loopback1接口上的IP地址。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。loopback为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#ip unnumbered loopback1解除te_tunnel1接口的地址借用关系。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#no ip unnumbered





相关命令 :

无 




## ip unnumbered 


ip unnumbered 




命令功能 :

该命令工作于接口配置模式下，用于设置接口借用IP地址，no ip unnumbered命令用于解除借用关系。借用IP地址功能，最主要的目的就是节省宝贵的IP地址资源。一个接口如果没有IP地址就无法生成路由，也就无法转发报文。借用IP地址的实质就是：一个接口上没有配置IP地址，但是还想使用该接口，就向其它有IP地址的接口借一个IP地址过来，以使该接口能正常使用。如果被借用接口没有IP地址，则借用接口的IP地址为0.0.0.0。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth接口模式:15,eth子接口模式:15 






命令格式 :


ip unnumbered 
  ＜interface-name 
＞

no ip unnumbered 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|借用IP地址的接口的接口名，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。可以通过show ip interface brief命令查询当前设备上的接口。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。POS接口及其子接口、通道化接口、multilink接口、virtual_template接口、gre_tunnel接口、te_tunnel接口、ipsec_tunnel接口和dsl接口支持接口IP地址借用的配置。在缺省情况下，接口没有地址借用关系。借用IP地址，仅能借用接口的主IP地址，该借用关系对辅地址无效。配置借用IP地址生效后，可以通过show ip interface、show interface命令查看借用关系以及借用到的IP地址。只有三层接口才允许配置IP 地址借用，如果在二层接口上配置IP 地址借用，会提示：%Error 94: The L2 interface does not support this command.接口不能同时配置IP地址又借用其他接口的IP地址。当接口已经配置了IP地址，再配置借用IP地址时，会提示：%Error 121007: Current interface already has an IP address。当接口已经配置了借用IP地址，再配置IP地址时，会提示：%Error 1044: Must no ip unnumbered first.接口不能借用自己的IP地址，如果配置IP地址借用自身，会提示：%Error 121012: Cannot use self接口本身和被借用地址的接口必须同在公网路由或者在同一个私网路由中。否则配置IP地址借用，会提示：%Error 120607: Can not configure IP unnumbered interface which is not in the same VPN.IP地址借用关系不支持嵌套，例如：A接口借用B接口的IP地址，则C接口不能再借用A接口的IP地址。如果进行配置，会提示：%Error 121023: Interface xxx whose IP has already unnumbered another interface, does not support nesting，其中xxx即为上文所说的A接口。配置IP地址借用必须借用已经存在的接口，如果设置借用不存在的接口，会提示：%Error 121134: No such unnumbered interface





范例 :

配置eth1接口借用loopback1接口上的IP地址。eth1为逻辑接口，在设备上没有具体物理位置，1表示接口编号。loopback为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#ip unnumbered loopback1解除eth1接口的地址借用关系。eth1为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#no ip unnumbered






相关命令 :

无 




## ip unnumbered 


ip unnumbered 




命令功能 :

该命令工作于接口配置模式下，用于设置接口借用IP地址，no ip unnumbered命令用于解除借用关系。借用IP地址功能，最主要的目的就是节省宝贵的IP地址资源。一个接口如果没有IP地址就无法生成路由，也就无法转发报文。借用IP地址的实质就是：一个接口上没有配置IP地址，但是还想使用该接口，就向其它有IP地址的接口借一个IP地址过来，以使该接口能正常使用。如果被借用接口没有IP地址，则借用接口的IP地址为0.0.0.0。






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip unnumbered 
  ＜interface-name 
＞

no ip unnumbered 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|借用IP地址的接口的接口名，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。可以通过show ip interface brief命令查询当前设备上的接口。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。POS接口及其子接口、通道化接口、multilink接口、virtual_template接口、gre_tunnel接口、te_tunnel接口、ipsec_tunnel接口和dsl接口支持接口IP地址借用的配置。在缺省情况下，接口没有地址借用关系。借用IP地址，仅能借用接口的主IP地址，该借用关系对辅地址无效。配置借用IP地址生效后，可以通过show ip interface、show interface命令查看借用关系以及借用到的IP地址。只有三层接口才允许配置IP 地址借用，如果在二层接口上配置IP 地址借用，会提示：%Error 94: The L2 interface does not support this command.接口不能同时配置IP地址又借用其他接口的IP地址。当接口已经配置了IP地址，再配置借用IP地址时，会提示：%Error 121007: Current interface already has an IP address。当接口已经配置了借用IP地址，再配置IP地址时，会提示：%Error 1044: Must no ip unnumbered first.接口不能借用自己的IP地址，如果配置IP地址借用自身，会提示：%Error 121012: Cannot use self接口本身和被借用地址的接口必须同在公网路由或者在同一个私网路由中。否则配置IP地址借用，会提示：%Error 120607: Can not configure IP unnumbered interface which is not in the same VPN.IP地址借用关系不支持嵌套，例如：A接口借用B接口的IP地址，则C接口不能再借用A接口的IP地址。如果进行配置，会提示：%Error 121023: Interface xxx whose IP has already unnumbered another interface, does not support nesting，其中xxx即为上文所说的A接口。配置IP地址借用必须借用已经存在的接口，如果设置借用不存在的接口，会提示：%Error 121134: No such unnumbered interface






范例 :

配置te_tunnel1接口借用loopback1接口上的IP地址。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。loopback为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#ip unnumbered loopback1解除te_tunnel1接口的地址借用关系。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#no ip unnumbered






相关命令 :

无 




## ip unnumbered 


ip unnumbered 




命令功能 :

该命令工作于接口配置模式下，用于设置接口借用IP地址，no ip unnumbered命令用于解除借用关系。借用IP地址功能，最主要的目的就是节省宝贵的IP地址资源。一个接口如果没有IP地址就无法生成路由，也就无法转发报文。借用IP地址的实质就是：一个接口上没有配置IP地址，但是还想使用该接口，就向其它有IP地址的接口借一个IP地址过来，以使该接口能正常使用。如果被借用接口没有IP地址，则借用接口的IP地址为0.0.0.0。





命令模式 :

 multilink接口模式,pos接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,通道化ce1接口模式:15,multilink接口模式:15,pos接口模式:15 






命令格式 :


ip unnumbered 
  ＜interface-name 
＞

no ip unnumbered 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|借用IP地址的接口的接口名，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。可以通过show ip interface brief命令查询当前设备上的接口。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。POS接口及其子接口、通道化接口、multilink接口、virtual_template接口、gre_tunnel接口、te_tunnel接口、ipsec_tunnel接口和dsl接口支持接口IP地址借用的配置。在缺省情况下，接口没有地址借用关系。借用IP地址，仅能借用接口的主IP地址，该借用关系对辅地址无效。配置借用IP地址生效后，可以通过show ip interface、show interface命令查看借用关系以及借用到的IP地址。只有三层接口才允许配置IP 地址借用，如果在二层接口上配置IP 地址借用，会提示：%Error 94: The L2 interface does not support this command.接口不能同时配置IP地址又借用其他接口的IP地址。当接口已经配置了IP地址，再配置借用IP地址时，会提示：%Error 121007: Current interface already has an IP address。当接口已经配置了借用IP地址，再配置IP地址时，会提示：%Error 1044: Must no ip unnumbered first.接口不能借用自己的IP地址，如果配置IP地址借用自身，会提示：%Error 121012: Cannot use self接口本身和被借用地址的接口必须同在公网路由或者在同一个私网路由中。否则配置IP地址借用，会提示：%Error 120607: Can not configure IP unnumbered interface which is not in the same VPN.IP地址借用关系不支持嵌套，例如：A接口借用B接口的IP地址，则C接口不能再借用A接口的IP地址。如果进行配置，会提示：%Error 121023: Interface xxx whose IP has already unnumbered another interface, does not support nesting，其中xxx即为上文所说的A接口。配置IP地址借用必须借用已经存在的接口，如果设置借用不存在的接口，会提示：%Error 121134: No such unnumbered interface





范例 :

配置te_tunnel1接口借用loopback1接口上的IP地址。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。loopback为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#ip unnumbered loopback1解除te_tunnel1接口的地址借用关系。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#no ip unnumbered





相关命令 :

无 




## ip unnumbered 


ip unnumbered 




命令功能 :

该命令工作于接口配置模式下，用于设置接口借用IP地址，no ip unnumbered命令用于解除借用关系。借用IP地址功能，最主要的目的就是节省宝贵的IP地址资源。一个接口如果没有IP地址就无法生成路由，也就无法转发报文。借用IP地址的实质就是：一个接口上没有配置IP地址，但是还想使用该接口，就向其它有IP地址的接口借一个IP地址过来，以使该接口能正常使用。如果被借用接口没有IP地址，则借用接口的IP地址为0.0.0.0。





命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip unnumbered 
  ＜interface-name 
＞

no ip unnumbered 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|借用IP地址的接口的接口名，用于唯一标识一个接口。取值范围：配置范围为1-31位的字符串。可以通过show ip interface brief命令查询当前设备上的接口。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。POS接口及其子接口、通道化接口、multilink接口、virtual_template接口、gre_tunnel接口、te_tunnel接口、ipsec_tunnel接口和dsl接口支持接口IP地址借用的配置。在缺省情况下，接口没有地址借用关系。借用IP地址，仅能借用接口的主IP地址，该借用关系对辅地址无效。配置借用IP地址生效后，可以通过show ip interface、show interface命令查看借用关系以及借用到的IP地址。只有三层接口才允许配置IP 地址借用，如果在二层接口上配置IP 地址借用，会提示：%Error 94: The L2 interface does not support this command.接口不能同时配置IP地址又借用其他接口的IP地址。当接口已经配置了IP地址，再配置借用IP地址时，会提示：%Error 121007: Current interface already has an IP address。当接口已经配置了借用IP地址，再配置IP地址时，会提示：%Error 1044: Must no ip unnumbered first.接口不能借用自己的IP地址，如果配置IP地址借用自身，会提示：%Error 121012: Cannot use self接口本身和被借用地址的接口必须同在公网路由或者在同一个私网路由中。否则配置IP地址借用，会提示：%Error 120607: Can not configure IP unnumbered interface which is not in the same VPN.IP地址借用关系不支持嵌套，例如：A接口借用B接口的IP地址，则C接口不能再借用A接口的IP地址。如果进行配置，会提示：%Error 121023: Interface xxx whose IP has already unnumbered another interface, does not support nesting，其中xxx即为上文所说的A接口。配置IP地址借用必须借用已经存在的接口，如果设置借用不存在的接口，会提示：%Error 121134: No such unnumbered interface





范例 :

配置te_tunnel1接口借用loopback1接口上的IP地址。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。loopback为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#ip unnumbered loopback1解除te_tunnel1接口的地址借用关系。te_tunnel为逻辑接口，在设备上没有具体物理位置，1表示接口编号。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#no ip unnumbered





相关命令 :

无 




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 ATM子接口模式,ATM接口模式,atm_dslgroup接口模式,dialer接口模式,dsl接口模式,eth_dslgroup子接口模式,eth_dslgroup接口模式,posgroup接口模式,pos子接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式,virtual_template子接口模式  






命令默认权限级别 :

serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,eth_dslgroup子接口模式:15,ulei子接口模式:15,virtual_template子接口模式:15,vbui子接口模式:15,pos子接口模式:15,ulei接口模式:15,ATM子接口模式:15,ATM接口模式:15,dialer接口模式:15,atm_dslgroup接口模式:15,posgroup接口模式:15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 IPv6隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将v6_tunnel接口绑定该VRF。v6_tunnel1表示设备上的逻辑接口ipv6隧道接口，其中"v6_tunnel"表示接口类型为IPV6隧道接口类型，"1"表示该接口在此类类型的接口中编号为1命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#ip vrf forwarding zte配置接口VRF解绑。命令如下：ZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#no ip vrf forwarding






相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 multilink接口模式,pos接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,通道化ce1接口模式:15,pos接口模式:15,multilink接口模式:15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 10G以太接口模式,loopback接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

loopback接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 vbui接口模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 virtual_template接口模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置gre_tunnel1接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将fei-0/1/0/1接口绑定该VRF。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exitZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#ip vrf forwarding zte配置gre_tunnel1接口VRF解绑。命令如下：ZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#no ip vrf forwarding






相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth接口模式:15,eth子接口模式:15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将eth1接口绑定该VRF。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#ip vrf forwarding zte配置接口VRF解绑。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#no ip vrf forwarding






相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding






范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding






相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx子接口模式:15,qx接口模式:15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi接口模式:15,bvi子接口模式:15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding






范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding






相关命令 :

ip vrfrdaddress-family




ip vrf forwarding :

ip vrf forwarding 




命令功能 :

该命令工作于接口配置模式下，用于将接口绑定到私网路由。no ip vrf forwarding命令用于删除这种绑定关系。路由转发实例(VPN Routing & Forwarding Instance，VRF)，每一个VRF可以看作虚拟的路由器（即上文所说的私网路由），好像是一台专用的PE设备。该虚拟路由器包括如下元素：一张独立的路由表，当然也包括了独立的地址空间；一组归属于这个VRF的接口的集合；一组只用于本VRF的路由协议。对于每个PE，可以维护一个或多个VRF，同时维护一个公网的路由表（也叫全局路由表），多个VRF实例相互分离独立。





命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf forwarding 
  ＜vrf-name 
＞

no ip vrf forwarding 








命令参数解释 :



参数|描述
---|---
＜vrf-name＞|接口绑定的VRF名称。可以通过show ip vrf brief命令查询系统当前所有的VRF。取值范围：配置范围为1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用该命令。在缺省情况下，接口不属于任何VRF，即属于全局路由。可以通过show ip interface命令查看接口的VRF绑定关系。只有三层接口才允许配置VRF绑定，如果在二层接口上配置VRF绑定，会提示：%Error 94: The L2 interface does not support this command.接口绑定的VRF必须已经存在，并且配置了RD（Route Distinguisher，路由区分符），否则会提示：%Error 8806: The VRF does not exist or does not have an RD.接口绑定的VRF必须使能了IPv4或者IPv6地址族，否则会提示：%Error 8826: IPv4 and IPv6 on this VRF are not enabled,enable IPv4 or IPv6 on this VRF first.接口绑定VRF必须在配置IPv4地址、IPv6地址、地址借用和被借用之前。否则会根据接口当前已有的配置，分别做如下提示：%Error 121074: The interface has IP address%Error 121075: The interface has IPv6 address%Error 121098: The interface has unnumbered or been unnumbered another interface接口绑定VRF后，不允许直接修改绑定关系，如果需要重新绑定别的VRF，必须先删除原有VRF绑定，再配置新的VRF绑定。如果直接绑定别的VRF，会提示：%Error 121072: The interface has configured VPN routing forwarding





范例 :

配置接口VRF绑定。首先，创建VRF，zte1为VRF名，然后配置RD（Route Distinguisher，路由标识符）并激活VRF的IPv4、IPv6地址族能力。最后将gei-0/1/0/1接口绑定该VRF。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#ip vrf zte1ZXROSNG(config-vrf-zte1)#rd 1:1ZXROSNG(config-vrf-zte1)#address-family ipv4ZXROSNG(config-vrf-zte1-af-ipv4)#exitZXROSNG(config-vrf-zte1)#address-family ipv6ZXROSNG(config-vrf-zte1-af-ipv6)#exit ZXROSNG(config-vrf-zte1)#exitZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ip vrf forwarding zte配置接口VRF解绑。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ip vrf forwarding





相关命令 :

ip vrfrdaddress-family




## ip-address network-segment conflict-check 


ip-address network-segment conflict-check 




命令功能 :

使能或者去使能接口IP地址网段冲突检查功能 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ip-address network-segment conflict-check 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能接口IP地址网段冲突检查功能
disable|去使能接口IP地址网段冲突检查功能








缺省 :

去使能接口IP地址网段冲突检查功能 






使用说明 :

使能接口IP地址网段冲突检查功能，不允许接口配置同网段IP地址。去使能接口IP地址网段冲突检查功能，允许接口配置同网段IP地址。当接口IP地址存在网段冲突时，不允许使能接口IP地址网段冲突检查功能，提示错误：%Error 121206: The interface IP/IPv6 address network segment conflict exists, please remove the conflicting address(es) first.






范例 :

使能接口IP地址网段冲突检查功能。命令如下：ZXROSNG(config)#ip-address network-segment conflict-check enableZXROSNG(config)#
去使能接口IP地址网段冲突检查功能。命令如下：ZXROSNG(config)#ip-address network-segment conflict-check disableZXROSNG(config)#






相关命令 :

无 




## ipv4 track 


ipv4 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv4协议关联检测对象。no ipv4 track命令用于删除接口IPv4协议与检测对象的关联关系。 






命令模式 :

 ATM子接口模式,ATM接口模式,IPv6隧道接口模式,dsl接口模式,gre隧道接口模式,posgroup接口模式,pos子接口模式,serial接口模式,supervlan接口模式,ulei子接口模式,ulei接口模式,virtual_template子接口模式,virtual_template接口模式  






命令默认权限级别 :

dsl接口模式:15,serial接口模式:15,gre隧道接口模式:15,IPv6隧道接口模式:15,ulei子接口模式:15,virtual_template子接口模式:15,pos子接口模式:15,ulei接口模式:15,virtual_template接口模式:15,ATM子接口模式:15,supervlan接口模式:15,ATM接口模式:15,posgroup接口模式:15 






命令格式 :



ipv4 track 
  [group 
] ＜track-name 
＞

no ipv4 track 








命令参数解释 :



参数|描述
---|---
group|IPv4协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。默认值：无。
＜track-name＞|接口关联的IPv4检测对象名称，长度为1~31个字符








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口IPv4协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个IPv4协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv4协议关联检测对象的情况下，如果需要配置其他的IPv4协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的IPv4协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4 track zte配置gei-0/1/0/2接口的IPv4协议关联检测组对象rosng。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv4 track rosng group删除gei-0/1/0/1接口的IPv4协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv4 track





相关命令 :

samgr 




## ipv4 track 


ipv4 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv4协议关联检测对象。no ipv4 track命令用于删除接口IPv4协议与检测对象的关联关系。 






命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :



ipv4 track 
  [group 
] ＜track-name 
＞

no ipv4 track 








命令参数解释 :



参数|描述
---|---
group|IPv4协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。默认值：无。
＜track-name＞|接口关联的IPv4检测对象名称，长度为1~31个字符








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口IPv4协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个IPv4协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv4协议关联检测对象的情况下，如果需要配置其他的IPv4协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的IPv4协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4 track zte配置gei-0/1/0/2接口的IPv4协议关联检测组对象rosng。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv4 track rosng group删除gei-0/1/0/1接口的IPv4协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv4 track





相关命令 :

samgr 




## ipv4 track 


ipv4 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv4协议关联检测对象。no ipv4 track命令用于删除接口IPv4协议与检测对象的关联关系。 






命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth接口模式:15,eth子接口模式:15 






命令格式 :



ipv4 track 
  [group 
] ＜track-name 
＞

no ipv4 track 








命令参数解释 :



参数|描述
---|---
group|IPv4协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。默认值：无。
＜track-name＞|接口关联的IPv4检测对象名称，长度为1~31个字符








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口IPv4协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个IPv4协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv4协议关联检测对象的情况下，如果需要配置其他的IPv4协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置eth1接口的IPv4协议关联检测对象zte。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#ipv4 track zte配置eth2接口的IPv4协议关联检测组对象rosng。命令如下：ZXROSNG(config)#interface eth2ZXROSNG(config-if-eth2)#ipv4 track rosng group删除eth1接口的IPv4协议关联检测对象。命令如下：ZXROSNG(config)#interface eth1ZXROSNG(config-if-eth1)#no ipv4 track






相关命令 :

samgr 




## ipv4 track 


ipv4 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv4协议关联检测对象。no ipv4 track命令用于删除接口IPv4协议与检测对象的关联关系。 






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :



ipv4 track 
  [group 
] ＜track-name 
＞

no ipv4 track 








命令参数解释 :



参数|描述
---|---
group|IPv4协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。
＜track-name＞|接口关联的IPv4检测对象名称，长度为1~31个字符








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口IPv4协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个IPv4协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv4协议关联检测对象的情况下，如果需要配置其他的IPv4协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group






范例 :

配置gei-0/1/0/1接口的IPv4协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4 track zte配置gei-0/1/0/2接口的IPv4协议关联检测组对象rosng。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv4 track rosng group删除gei-0/1/0/1接口的IPv4协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv4 track






相关命令 :

samgr 




## ipv4 track 


ipv4 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv4协议关联检测对象。no ipv4 track命令用于删除接口IPv4协议与检测对象的关联关系。 






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi接口模式:15,bvi子接口模式:15 






命令格式 :



ipv4 track 
  [group 
] ＜track-name 
＞

no ipv4 track 








命令参数解释 :



参数|描述
---|---
group|IPv4协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。
＜track-name＞|接口关联的IPv4检测对象名称，长度为1~31个字符








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口IPv4协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个IPv4协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv4协议关联检测对象的情况下，如果需要配置其他的IPv4协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的IPv4协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4 track zte配置gei-0/1/0/2接口的IPv4协议关联检测组对象rosng。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv4 track rosng group删除gei-0/1/0/1接口的IPv4协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv4 track






相关命令 :

samgr 




## ipv4 track 


ipv4 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv4协议关联检测对象。no ipv4 track命令用于删除接口IPv4协议与检测对象的关联关系。 






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



ipv4 track 
  [group 
] ＜track-name 
＞

no ipv4 track 








命令参数解释 :



参数|描述
---|---
group|IPv4协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。默认值：无。
＜track-name＞|接口关联的IPv4检测对象名称，长度为1~31个字符








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口IPv4协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个IPv4协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv4协议关联检测对象的情况下，如果需要配置其他的IPv4协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的IPv4协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4 track zte配置gei-0/1/0/2接口的IPv4协议关联检测组对象rosng。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv4 track rosng group删除gei-0/1/0/1接口的IPv4协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv4 track





相关命令 :

samgr 




## ipv4 track 


ipv4 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv4协议关联检测对象。no ipv4 track命令用于删除接口IPv4协议与检测对象的关联关系。 






命令模式 :

 10G以太接口模式,loopback接口模式,multilink接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,loopback接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,通道化ce1接口模式:15,pos接口模式:15,multilink接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :



ipv4 track 
  [group 
] ＜track-name 
＞

no ipv4 track 








命令参数解释 :



参数|描述
---|---
group|IPv4协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。默认值：无。
＜track-name＞|接口关联的IPv4检测对象名称，长度为1~31个字符








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口IPv4协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个IPv4协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv4协议关联检测对象的情况下，如果需要配置其他的IPv4协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的IPv4协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv4 track zte配置gei-0/1/0/2接口的IPv4协议关联检测组对象rosng。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv4 track rosng group删除gei-0/1/0/1接口的IPv4协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv4 track





相关命令 :

samgr 




ipv6 address :

ipv6 address 




命令功能 :

该命令工作于管理口配置模式下，用于设置管理口的IPv6地址。no ipv6 address命令用于删除管理口的IPv6地址。管理口配置了IPv6地址后，则可以通过该IPv6地址登陆管理口，进行版本下载等操作。





命令模式 :

 管理口接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞}]
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|IPv6地址，格式：X:X::X:X/<1-128>。X:X::X:X表示将要在接口上配置的地址，遵循RFC2373中的规定，以16位为一组，中间用“:”格开。<1-128>表示Ipv6地址的前缀长度。配置范围为1-128。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于管理口配置模式下，需要先进入管理口配置模式，才能使用。管理口只能配置一个linklocal和一个普通单播地址。管理口缺省没有IPv6地址可以通过show ipv6 interface brief、show ipv6 interface命令查看管理接口的IPv6地址。管理口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，管理口使能了IPv6功能后，如果删除配置的linklocal地址，会将管理口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除管理口所有的IPv6地址。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而单播地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置管理口上的linklocal地址。mgmt_eth表示设备的管理口，link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#ipv6 address link-local fe80::1配置管理口上的普通单播地址。mgmt_eth表示设备的管理口。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#ipv6 address 1::1/64删除管理口上的linklocal地址。mgmt_eth表示设备的管理口，link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ipv6 address link-local删除管理口上的普通单播地址。mgmt_eth表示设备的管理口。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ipv6 address 1::1/641::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。删除管理口上的所有IPv6地址。mgmt_eth表示设备的管理口。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ipv6 address





相关命令 :

show ipv6 interface briefshow ipv6 interface 



ipv6 address :

ipv6 address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6地址。no ipv6 address命令用于删除接口的IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。





命令模式 :

 10G以太接口模式,loopback接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式  






命令默认权限级别 :

loopback接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,smartgroup子接口模式:15,以太接口模式:15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address





相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6地址。no ipv6 address命令用于删除接口的IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。





命令模式 :

 multilink接口模式,pos接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,multilink接口模式:15,pos接口模式:15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address





相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6地址。no ipv6 address命令用于删除接口的IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。





命令模式 :

 以太子接口模式,千兆以太接口模式  






命令默认权限级别 :

千兆以太接口模式:15,以太子接口模式:15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address





相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6地址。no ipv6 address命令用于删除接口的IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。





命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address





相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6地址。no ipv6 address命令用于删除接口的IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth子接口模式:15,eth接口模式:15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address





相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6地址。no ipv6 address命令用于删除接口的IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。





命令模式 :

 dsl接口模式,eth_dslgroup子接口模式,eth_dslgroup接口模式,posgroup接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式,vbui接口模式,virtual_template接口模式  






命令默认权限级别 :

posgroup接口模式:15,ulei接口模式:15,vbui接口模式:15,virtual_template接口模式:15,vbui子接口模式:15,eth_dslgroup子接口模式:15,eth_dslgroup接口模式:15,serial接口模式:15,dsl接口模式:15,ulei子接口模式:15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|IPv6地址，格式：X:X::X:X/<1-128>。X:X::X:X表示将要在接口上配置的地址，遵循RFC2373第2.2节中的规定，以16位为一组，中间用“:”格开。<1-128>表示Ipv6地址的前缀长度。配置范围为1-128。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address





相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6地址。no ipv6 address命令用于删除接口的IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。





命令模式 :

 IPv6隧道接口模式,supervlan接口模式  






命令默认权限级别 :

supervlan接口模式:15,IPv6隧道接口模式:15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|IPv6地址，格式：X:X::X:X/<1-128>。X:X::X:X表示将要在接口上配置的地址，遵循RFC2373第2.2节中的规定，以16位为一组，中间用“:”格开。<1-128>表示Ipv6地址的前缀长度。配置范围为1-128。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address





相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6地址。no ipv6 address命令用于删除接口的IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。





命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.





范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address





相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi子接口模式:15,bvi接口模式:15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址。
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|IPv6地址，格式：X:X::X:X/<1-128>。X:X::X:X表示将要在接口上配置的地址，遵循RFC2373第2.2节中的规定，以16位为一组，中间用“:”格开。<1-128>表示Ipv6地址的前缀长度。配置范围为1-128。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。可以通过show ipv6 interface brief、show ipv6 interface命令查看接口的IPv6地址。接口在缺省的情况下，没有配置IPv6地址。以太物理接口及其子接口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6地址的配置。接口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，接口使能了IPv6功能后，如果删除配置的linklocal地址，会将接口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除当前接口所有的IPv6地址。只有三层接口才允许配置IPv6地址，如果在二层接口上配置IPv6地址，会提示：%Error 94: The L2 interface does not support this command.接口支持配置的IPv6地址类型包括linklocal地址、单播地址、泛播地址和eui-64地址。每个接口支持1个linklocal地址、15个单播地址、15个泛播地址和8个eui-64地址，如果配置超过数量限制，会提示：%Error 121011: The number of addresses of this type comes to the limit同一个私网路由(VRF)，或者公网路由中的不同接口，不允许配置相同网段的地址(不包含linklocal地址)。如果配置的IP地址与当前接口在同一个私网或者同在公网上的其他接口的IPv6地址冲突，会提示：%Error 121034: The interface xxx, x:x::x:x/xx is overlapping with 1::/64 on xxx，其中第一个xxx表示当前配置的接口，第二个xxx表示冲突地址所属接口，x:x::x:x/xx表示冲突的网段。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而非linklocal地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.






范例 :

配置gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address link-local fe80::1配置gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 1::1/64配置gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2::2/64为IPv6地址和前缀长度，其中”2::2”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 2:2::/64 eui-64配置gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的linklocal地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address link-local删除gei-0/1/0/1接口上的普通单播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 1::1/64删除gei-0/1/0/1接口上的eui-64地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。2:2::/64为IPv6地址和前缀长度，其中”2:2::”为地址，64为前缀长度。eui-64表示为eui-64地址类型。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 2:2::/64 eui-64删除gei-0/1/0/1接口上的泛播地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。3::3/64为IPv6地址和前缀长度，其中”3::3”为地址，64为前缀长度。anycast表示为泛播地址。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address 3::3/64 anycast删除gei-0/1/0/1接口上的所有IPv6地址。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 address






相关命令 :

show ipv6 interfaceshow ipv6 interface brief




ipv6 address :

ipv6 address 




命令功能 :

IPv6地址。IPv6指的是网络协议版本6。网络协议是指在国际互联网中普遍使用的通讯规程。IPv6是IETF设计的用于替代IPv4的下一代IP协议。IPv6提供128位的地址空间，IPv6所能提供的巨大的地址容量可以从以下几个方面来说明：    共有2128个不同的IPv6地址，也就是全球可分配地址数为340,282,366,920,938,463,463,374,607,431,768,211,456个。    若按土地面积分配，每平方厘米可获得2.2×1020个地址。IPv6地址耗尽的机会是很小的。在可预见的很长时期内，IPv6的128位地址长度形成的巨大的地址空间能够为所有可以想象出的网络设备提供一个全球唯一的地址。IPv6充足的地址空间将极大地满足那些伴随着网络智能设备的出现而对地址增长的需求，例如个人数据助理（PDA）、移动电话（Mobile Phone）、家庭网络接入设备（HAN）等。RFC中定义了三种IPv6地址类型：    单播：一个单接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。    组播：一组接口（一般属于不同节点）的标识符。送往一个组播地址的包将被传送至有该地址标识的所有接口上。    泛播：一组接口（一般属于不同节点）的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一（根据选路协议对于距离的计算方法选择“最近”的一个）。也称作泛播地址。IPv6地址长度4倍于IPv4地址，表达起来的复杂程度也是IPv4地址的4倍。IPv6地址的基本表达方式是X:X:X:X:X:X:X:X，其中X是一个4位十六进制整数（16位）。每一个数字包含4位，每个整数包含4个数字，每个地址包括8个整数，共计128位（4×4×8 =128）。某些IPv6地址中可能包含一长串的0。当出现这种情况时，标准中允许用“空隙”来表示这一长串的0。IPv6地址的基本表达方式可以简化为X:X::X:X，也就是说，地址2000:0:0:0:0:0:0:1可以被表示为2000::1，这两个冒号表示该地址可以扩展到一个完整的128位地址。






命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx接口模式:15,qx子接口模式:15 






命令格式 :


ipv6 address 
  {link-local 
 ＜ipv6-address 
＞|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
no ipv6 address 
  [{link-local 
|＜ipv6-address-mask 
＞ [{eui-64 
|anycast 
}]}
				






命令参数解释 :



参数|描述
---|---
link-local|linklocal地址标识，如果选择该标识，表示配置或者删除的地址为linklocal地址
＜ipv6-address＞|linklocal地址，地址格式：X:X::X:X。linklocal地址前缀为10，且前10位必须为1111111010。默认值：无。
＜ipv6-address-mask＞|IPv6地址，格式：X:X::X:X/<1-128>。X:X::X:X表示将要在接口上配置的地址，遵循RFC2373中的规定，以16位为一组，中间用“:”格开。<1-128>表示Ipv6地址的前缀长度。配置范围为1-128。默认值：无。
eui-64|和anycast为二选一，选择eui-64表示配置的地址为eui-64地址。为可选参数，如果不选择，表示配置的是普通单播地址。
anycast|和eui-64为二选一，选择anycast表示配置的地址为泛播地址。为可选参数，如果不选择，表示配置的是普通单播地址。








缺省 :

无 






使用说明 :

该命令工作于管理口配置模式下，需要先进入管理口配置模式，才能使用。管理口只能配置一个linklocal和一个普通单播地址。管理口缺省没有IPv6地址可以通过show ipv6 interface brief、show ipv6 interface命令查看管理接口的IPv6地址。管理口使能了IPv6功能后，如果没有配置linklocal地址，会自动生成一个linklocal地址。同样，管理口使能了IPv6功能后，如果删除配置的linklocal地址，会将管理口的linklocal地址恢复成自动生成的地址。在删除IPv6地址时，可以删除指定的IPv6地址，也可以删除管理口所有的IPv6地址。配置linklocal地址的前10位必须为1111111010，否则会提示：%Error 121154: Invalid IPv6 link-local address而单播地址的前10位必须不能为1111111010，否则会提示：%Error 1127: Invalid IPv6 address.






范例 :

配置管理口上的linklocal地址。mgmt_eth表示设备的管理口，link-local 表示地址类型为linklocal，fe80::1为地址。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#ipv6 address link-local fe80::1配置管理口上的普通单播地址。mgmt_eth表示设备的管理口。1::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#ipv6 address 1::1/64删除管理口上的linklocal地址。mgmt_eth表示设备的管理口，link-local 表示地址类型为linklocal。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ipv6 address link-local删除管理口上的普通单播地址。mgmt_eth表示设备的管理口。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ipv6 address 1::1/641::1/64为IPv6地址和前缀长度，其中”1::1”为地址，64为前缀长度。删除管理口上的所有IPv6地址。mgmt_eth表示设备的管理口。命令如下：ZXROSNG(config)#interface mgmt_ethZXROSNG(config-if-mgmt_eth)#no ipv6 address






相关命令 :

show ipv6 interface briefshow ipv6 interface 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。





命令模式 :

 10G以太接口模式,loopback接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式,管理口接口模式  






命令默认权限级别 :

管理口接口模式:15,loopback接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,smartgroup子接口模式:15,以太接口模式:15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。    只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable





相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。





命令模式 :

 multilink接口模式,pos接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,multilink接口模式:15,pos接口模式:15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。    只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable





相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。





命令模式 :

 以太子接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,千兆以太接口模式:15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。    只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable





相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。





命令模式 :

 eth子接口模式,eth接口模式  






命令默认权限级别 :

eth子接口模式:15,eth接口模式:15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。    只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable





相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。





命令模式 :

 dsl接口模式,eth_dslgroup子接口模式,eth_dslgroup接口模式,posgroup接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式,vbui接口模式,virtual_template接口模式  






命令默认权限级别 :

posgroup接口模式:15,ulei接口模式:15,vbui接口模式:15,virtual_template接口模式:15,vbui子接口模式:15,eth_dslgroup子接口模式:15,eth_dslgroup接口模式:15,serial接口模式:15,dsl接口模式:15,ulei子接口模式:15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable





相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。





命令模式 :

 virtual_template子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。    只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable





相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。





命令模式 :

 IPv6隧道接口模式,gre隧道接口模式,supervlan接口模式  






命令默认权限级别 :

supervlan接口模式:15,IPv6隧道接口模式:15,gre隧道接口模式:15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable





相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。





命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。    只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable





相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi接口模式:15,bvi子接口模式:15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable






相关命令 :

无 




## ipv6 enable 


ipv6 enable 




命令功能 :

该命令工作于接口配置模式下，用于使能接口IPv6协议功能。当接口上需要启用IPv6相关业务时，必须先使能IPv6协议功能。IPv6是由IETF设计的用来替代现行的IPv4协议的一种新的IP协议。IPv6是为了解决IPv4地址匮乏等问题，同时它还在许多方面提出了改进，例如路由方面、自动配置方面。






命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx子接口模式:15,qx接口模式:15 






命令格式 :


ipv6 enable 
 

no ipv6 enable 








命令参数解释 :


					无
				 






缺省 :

未使能





使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太物理接口及其子接口、管理口、POS接口及其子接口、通道化cpos_e1接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口及其子接口、vbui接口及其子接口、supervlan接口、serial接口、posgroup接口、multilink接口、loopback接口、virtual_template接口、gre_tunnel接口、v6_tunnel接口和dsl接口支持接口IPv6协议的使能和去使能配置。在缺省情况下，接口未使能IPv6协议功能配置成功后，可以通过show ipv6 interface brief和show ipv6 interface命令查看接口IPv6协议功能的使能情况。只有三层接口才允许配置IPv6 协议使能，如果在二层接口上配置IPv6 协议使能，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gei-0/1/0/1接口的IPv6 协议使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 enable配置gei-0/1/0/1接口的IPv6 协议去使能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 enable






相关命令 :

无 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 10G以太接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gei-0/1/0/1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 mtu 2000恢复gei-0/1/0/1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 eth接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜1280-9202 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜1280-9202＞|接口的IPV6 MTU值。配置范围为1280~$#50397247#$。单位：字节。








缺省 :

以太接口缺省为1500 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

1. 配置接口的IPv6 MTUZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if-fei-0/1/0/1)#ipv6 mtu 12802. 删除接口的IPv6 MTUZXROSNG(config)#interface fei-0/1/0/1ZXROSNG(config-if-fei-0/1/0/1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。






命令模式 :

 multilink接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397250#$。单位：字节。








缺省 :

1500 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置multilink1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface multilink1ZXROSNG(config-if-multilink1)#ipv6 mtu 2000恢复multilink1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface multilink1ZXROSNG(config-if-multilink1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。






命令模式 :

 pos接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397253#$。单位：字节。








缺省 :

4470 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置pos-0/1/1/1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface pos-0/1/1/1ZXROSNG(config-if-pos-0/1/1/1)#ipv6 mtu 2000恢复pos-0/1/1/1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface pos-0/1/1/1ZXROSNG(config-if-pos-0/1/1/1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。






命令模式 :

 smartgroup子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置smartgroup1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface smartgroup1.1ZXROSNG(config-if-smartgroup1.1)#ipv6 mtu 2000恢复smartgroup1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface smartgroup1.1ZXROSNG(config-if-smartgroup1.1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。






命令模式 :

 以太子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gei-0/1/0/1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#ipv6 mtu 2000恢复gei-0/1/0/1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。






命令模式 :

 eth子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜1280-9194 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜1280-9194＞|接口的IPV6 MTU值。配置范围为1280~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置eth1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface eth1.1ZXROSNG(config-if-eth1.1)#ipv6 mtu 2000恢复eth1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface eth1.1ZXROSNG(config-if-eth1.1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。






命令模式 :

 loopback接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置loopback1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface loopback1ZXROSNG(config-if-loopback1)#ipv6 mtu 2000恢复loopback1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface loopback1ZXROSNG(config-if-loopback1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。






命令模式 :

 smartgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

配置IPv6 MTU前需要先使能IPv6功能。该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置smartgroup1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#ipv6 mtu 2000恢复smartgroup1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置supervlan1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#ipv6 mtu 2000恢复supervlan1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 virtual_template接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397226#$。单位：字节。








缺省 :

当接口模式为PPP时，缺省值为1430；当接口模式为ps-core时，缺省值为1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置virtual_template1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface virtual_template1ZXROSNG(config-if-virtual_template1)#ipv6 mtu 2000恢复virtual_template1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface virtual_template1ZXROSNG(config-if-virtual_template1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 IPv6隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置v6_tunnel1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#ipv6 mtu 2000恢复v6_tunnel1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface v6_tunnel1ZXROSNG(config-if-v6_tunnel1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜1280-9600 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜1280-9600＞|接口的IPv6 MTU值，单位：字节








缺省 :

ipsec_tunnel接口缺省为1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

1. 配置接口的IPv6 MTUZXROSNG(config)#interface ipsec_tunnel1ZXROSNG(config-if-ipsec_tunnel1)#ipv6 mtu 45002. 删除接口的IPv6 MTUZXROSNG(config)#interface ipsec_tunnel1ZXROSNG(config-if-ipsec_tunnel1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gre_tunnel1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#ipv6 mtu 2000恢复gre_tunnel1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 posgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397253#$。单位：字节。








缺省 :

4470 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置posgroup1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if-posgroup1)#ipv6 mtu 2000恢复posgroup1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if-posgroup1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 vbui接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置vbui1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface vbui1ZXROSNG(config-if-vbui1)#ipv6 mtu 2000恢复vbui1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface vbui1ZXROSNG(config-if-vbui1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 ulei接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置ulei-0/1/0/1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1ZXROSNG(config-if-ulei-0/1/0/1)#ipv6 mtu 2000恢复ulei-0/1/0/1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1ZXROSNG(config-if-ulei-0/1/0/1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 bvi接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置bvi1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#ipv6 mtu 2000恢复bvi1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 bvi子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置bvi1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#ipv6 mtu 2000恢复bvi1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 vbui子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397226#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置vbui1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface vbui1.1ZXROSNG(config-if-vbui1.1)#ipv6 mtu 2000恢复vbui1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface vbui1.1ZXROSNG(config-if-vbui1.1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 通道化cpos_e1接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397253#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置cpos3_e1-1/2/1/1.1/1/1:1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1)#ipv6 mtu 2000恢复cpos3_e1-1/2/1/1.1/1/1:1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 ulei子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置ulei-0/1/0/1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1.1ZXROSNG(config-if-ulei-0/1/0/1.1)#ipv6 mtu 2000恢复ulei-0/1/0/1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1.1ZXROSNG(config-if-ulei-0/1/0/1.1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 eth_dslgroup子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397248#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置eth_dslgroup1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface eth_dslgroup1.1ZXROSNG(config-if-eth_dslgroup1.1)#ipv6 mtu 2000恢复eth_dslgroup1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface eth_dslgroup1.1ZXROSNG(config-if-eth_dslgroup1.1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 eth_dslgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置eth_dslgroup1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface eth_dslgroup1ZXROSNG(config-if-eth_dslgroup1)#ipv6 mtu 2000恢复eth_dslgroup1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface eth_dslgroup1ZXROSNG(config-if-eth_dslgroup1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 qx接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397247#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置qx1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface qx1ZXROSNG(config-if-qx1)#ipv6 mtu 2000恢复qx1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface qx1ZXROSNG(config-if-qx1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。






命令模式 :

 qx子接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397251#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置qx1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface qx1.1ZXROSNG(config-if-qx1.1)#ipv6 mtu 2000恢复qx1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface qx1.1ZXROSNG(config-if-qx1.1)#no ipv6 mtu






相关命令 :

ipv6 enable 




ipv6 mtu :

ipv6 mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议最大传输单元，no ipv6 mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送IPv6协议报文时，其报文长度必须不超过出接口的 IPv6 MTU。接口IPv6 MTU的配置会影响设备本地发包和转发包时IPv6协议报文的分片和重组。





命令模式 :

 serial接口模式  






命令默认权限级别 :

15 






命令格式 :


ipv6 mtu 
  ＜IPv6-MTU 
＞

no ipv6 mtu 








命令参数解释 :



参数|描述
---|---
＜IPv6-MTU＞|接口的IPv6 MTU值。配置范围为1280~$#50397253#$。单位：字节。








缺省 :

1500 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface和show ipv6 interface命令查看生效的IPv6 MTU值。只有三层接口才允许配置IPv6 MTU，如果在二层接口上配置IPv6 MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置serial-0/1/0/1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface serial-0/1/0/1ZXROSNG(config-if-serial-0/1/0/1)#ipv6 mtu 2000恢复serial-0/1/0/1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface serial-0/1/0/1ZXROSNG(config-if-serial-0/1/0/1)#no ipv6 mtu






相关命令 :

ipv6 enable 




## ipv6 track 


ipv6 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议关联检测对象。no ipv6 track命令用于删除接口IPv6协议与检测对象的关联关系。 






命令模式 :

 IPv6隧道接口模式,dsl接口模式,gre隧道接口模式,posgroup接口模式,serial接口模式,supervlan接口模式,ulei子接口模式,ulei接口模式,virtual_template接口模式  






命令默认权限级别 :

ulei接口模式:15,virtual_template接口模式:15,supervlan接口模式:15,ulei子接口模式:15,serial接口模式:15,dsl接口模式:15,posgroup接口模式:15,gre隧道接口模式:15,IPv6隧道接口模式:15 






命令格式 :



ipv6 track 
  [group 
] ＜track-name 
＞

no ipv6 track 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为检测组。选择group表示配置的检测对象为检测组，不选择group表示配置的检测对象不是检测组。
＜track-name＞|IPv6协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太接口及其子接口、POS接口、通道化CPOS接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、supervlan接口、multilink接口、posgroup接口、loopback接口、virtual_template接口、v6_tunnel接口和gre_tunnel接口支持接口IPv6协议关联检测对象的配置。在缺省情况下，接口没有IPv6协议关联检测对象。同一个接口仅允许配置一个IPv6协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv6协议关联检测对象的情况下，如果需要配置其他的IPv6协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的IPv6协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。zte为检测对象名。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 track zte配置gei-0/1/0/2接口的IPv6协议关联检测组对象。gei-0/1/0/2表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/2”依次代表机框号、槽位号、子槽位号和接口号。rosng为检测组对象名。group表示为检测组对象。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv6 track rosng group删除gei-0/1/0/1接口的IPv6协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 track





相关命令 :

samgr 




## ipv6 track 


ipv6 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议关联检测对象。no ipv6 track命令用于删除接口IPv6协议与检测对象的关联关系。SNG V1.00.30 R2版本开始支持






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi子接口模式:15,bvi接口模式:15 






命令格式 :


ipv6 track 
  [group 
] ＜track-name 
＞

no ipv6 track 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为检测组。选择group表示配置的检测对象为检测组，不选择group表示配置的检测对象不是检测组。
＜track-name＞|IPv6协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。默认值：无。








缺省 :

无





使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太接口及其子接口、POS接口、通道化CPOS接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、supervlan接口、multilink接口、posgroup接口、loopback接口、virtual_template接口、v6_tunnel接口和gre_tunnel接口支持接口IPv6协议关联检测对象的配置。在缺省情况下，接口没有IPv6协议关联检测对象。同一个接口仅允许配置一个IPv6协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv6协议关联检测对象的情况下，如果需要配置其他的IPv6协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group






范例 :

配置gei-0/1/0/1接口的IPv6协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。zte为检测对象名。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 track zte配置gei-0/1/0/2接口的IPv6协议关联检测组对象。gei-0/1/0/2表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/2”依次代表机框号、槽位号、子槽位号和接口号。rosng为检测组对象名。group表示为检测组对象。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv6 track rosng group删除gei-0/1/0/1接口的IPv6协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 track






相关命令 :

samgr 




## ipv6 track 


ipv6 track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口IPv6协议关联检测对象。no ipv6 track命令用于删除接口IPv6协议与检测对象的关联关系。 






命令模式 :

 10G以太接口模式,loopback接口模式,multilink接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,loopback接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,multilink接口模式:15,pos接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :



ipv6 track 
  [group 
] ＜track-name 
＞

no ipv6 track 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为检测组。选择group表示配置的检测对象为检测组，不选择group表示配置的检测对象不是检测组。
＜track-name＞|IPv6协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。以太接口及其子接口、POS接口、通道化CPOS接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、supervlan接口、multilink接口、posgroup接口、loopback接口、virtual_template接口、v6_tunnel接口和gre_tunnel接口支持接口IPv6协议关联检测对象的配置。在缺省情况下，接口没有IPv6协议关联检测对象。同一个接口仅允许配置一个IPv6协议关联检测对象，且不允许直接修改配置。接口已经配置了IPv6协议关联检测对象的情况下，如果需要配置其他的IPv6协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的IPv6协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。zte为检测对象名。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#ipv6 track zte配置gei-0/1/0/2接口的IPv6协议关联检测组对象。gei-0/1/0/2表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/2”依次代表机框号、槽位号、子槽位号和接口号。rosng为检测组对象名。group表示为检测组对象。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#ipv6 track rosng group删除gei-0/1/0/1接口的IPv6协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no ipv6 track





相关命令 :

samgr 




## load-sharing bandwidth 


load-sharing bandwidth 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担带宽，no load-sharing bandwidth命令用于恢复接口缺省的负荷分担带宽。当接口上需要启用负荷分担功能时，则需要配置负荷分担带宽。根据接口的负荷分担带宽可以计算接口的负荷分担比例，例如：设置接口fei-0/1/0/1负荷分担带宽为10000kbps，接口fei-0/1/0/2负荷分担带宽为20000kbps，则最终的分担比例为1:2。





命令模式 :

 ATM子接口模式,ATM接口模式,dialer接口模式,dsl接口模式,gre隧道接口模式,posgroup接口模式,serial接口模式  






命令默认权限级别 :

posgroup接口模式:15,gre隧道接口模式:15,serial接口模式:15,dsl接口模式:15,ATM子接口模式:15,dialer接口模式:15,ATM接口模式:15 






命令格式 :


load-sharing bandwidth 
  ＜1-4294967295 
＞ [{kbps 
|mbps 
|gbps 
}]

no load-sharing bandwidth 








命令参数解释 :



参数|描述
---|---
＜1-4294967295＞|负荷分担带宽。各个接口的负荷分担比例根据接口的负荷分担带宽比例计算，如设置接口fei-0/1/0/1负荷分担带宽为10000kbps，接口fei-0/1/0/2负荷分担带宽为20000kbps，则最终的分担比例为1:2取值范围：1-4294967295。接口负荷分担带宽的生效值为配置值和接口带宽两者中的较小值，如接口fei-0/1/0/1的接口带宽为100000kbps，配置负荷分担带宽为50000kbps，则接口负荷分担带宽生效值为50000kbps，如果修改负荷分担带宽配置为2000000kbps，则接口负荷分担带宽生效值为100000kbps默认值：接口的负荷分担带宽缺省与接口带宽相等。单位：kbps
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second








缺省 :

默认值为接口带宽 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担带宽的配置。接口的负荷分担带宽缺省与接口带宽相等。接口的负荷分担带宽生效值为接口带宽和负荷分担带宽配置值中的较小值。配置生效后，可以通过show ip interface命令查看接口的负荷分担带宽生效值。





范例 :

配置gei-0/1/0/1接口的负荷分担带宽为50000kpbs。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing bandwidth 50000恢复gei-0/1/0/1接口的缺省负荷分担带宽。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no load-sharing bandwidth





相关命令 :

无 




## load-sharing bandwidth 


load-sharing bandwidth 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担带宽，no load-sharing bandwidth命令用于恢复接口缺省的负荷分担带宽。当接口上需要启用负荷分担功能时，则需要配置负荷分担带宽。根据接口的负荷分担带宽可以计算接口的负荷分担比例，例如：设置接口fei-0/1/0/1负荷分担带宽为10000kbps，接口fei-0/1/0/2负荷分担带宽为20000kbps，则最终的分担比例为1:2。





命令模式 :

 te隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


load-sharing bandwidth 
  ＜1-4294967295 
＞ [{kbps 
|mbps 
|gbps 
}]

no load-sharing bandwidth 








命令参数解释 :



参数|描述
---|---
＜1-4294967295＞|负荷分担带宽。各个接口的负荷分担比例根据接口的负荷分担带宽比例计算，如设置接口fei-0/1/0/1负荷分担带宽为10000kbps，接口fei-0/1/0/2负荷分担带宽为20000kbps，则最终的分担比例为1:2取值范围：1-4294967295。接口负荷分担带宽的生效值为配置值和接口带宽两者中的较小值，如接口fei-0/1/0/1的接口带宽为100000kbps，配置负荷分担带宽为50000kbps，则接口负荷分担带宽生效值为50000kbps，如果修改负荷分担带宽配置为2000000kbps，则接口负荷分担带宽生效值为100000kbps默认值：接口的负荷分担带宽缺省与接口带宽相等。单位：kbps
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second








缺省 :

默认值为接口带宽 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担带宽的配置。接口的负荷分担带宽缺省与接口带宽相等。接口的负荷分担带宽生效值为接口带宽和负荷分担带宽配置值中的较小值。配置生效后，可以通过show ip interface命令查看接口的负荷分担带宽生效值。





范例 :

配置gei-0/1/0/1接口的负荷分担带宽为50000kpbs。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing bandwidth 50000恢复gei-0/1/0/1接口的缺省负荷分担带宽。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no load-sharing bandwidth





相关命令 :

无 




## load-sharing bandwidth 


load-sharing bandwidth 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担带宽，no load-sharing bandwidth命令用于恢复接口缺省的负荷分担带宽。当接口上需要启用负荷分担功能时，则需要配置负荷分担带宽。根据接口的负荷分担带宽可以计算接口的负荷分担比例，例如：设置接口fei-0/1/0/1负荷分担带宽为10000kbps，接口fei-0/1/0/2负荷分担带宽为20000kbps，则最终的分担比例为1:2。





命令模式 :

 bvi子接口模式,bvi接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

ulei接口模式:15,bvi接口模式:15,bvi子接口模式:15,ulei子接口模式:15 






命令格式 :


load-sharing bandwidth 
  ＜1-4294967295 
＞ [{kbps 
|mbps 
|gbps 
}]

no load-sharing bandwidth 








命令参数解释 :



参数|描述
---|---
＜1-4294967295＞|负荷分担带宽。各个接口的负荷分担比例根据接口的负荷分担带宽比例计算，如设置接口fei-0/1/0/1负荷分担带宽为10000kbps，接口fei-0/1/0/2负荷分担带宽为20000kbps，则最终的分担比例为1:2取值范围：1-4294967295。接口负荷分担带宽的生效值为配置值和接口带宽两者中的较小值，如接口fei-0/1/0/1的接口带宽为100000kbps，配置负荷分担带宽为50000kbps，则接口负荷分担带宽生效值为50000kbps，如果修改负荷分担带宽配置为2000000kbps，则接口负荷分担带宽生效值为100000kbps默认值：接口的负荷分担带宽缺省与接口带宽相等。单位：kbps
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second








缺省 :

默认值为接口带宽 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担带宽的配置。接口的负荷分担带宽缺省与接口带宽相等。接口的负荷分担带宽生效值为接口带宽和负荷分担带宽配置值中的较小值。配置生效后，可以通过show ip interface命令查看接口的负荷分担带宽生效值。





范例 :

配置gei-0/1/0/1接口的负荷分担带宽为50000kpbs。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing bandwidth 50000恢复gei-0/1/0/1接口的缺省负荷分担带宽。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no load-sharing bandwidth





相关命令 :

无 




## load-sharing bandwidth 


load-sharing bandwidth 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担带宽，no load-sharing bandwidth命令用于恢复接口缺省的负荷分担带宽。当接口上需要启用负荷分担功能时，则需要配置负荷分担带宽。根据接口的负荷分担带宽可以计算接口的负荷分担比例，例如：设置接口fei-0/1/0/1负荷分担带宽为10000kbps，接口fei-0/1/0/2负荷分担带宽为20000kbps，则最终的分担比例为1:2。





命令模式 :

 10G以太接口模式,multilink接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,通道化ce1接口模式:15,multilink接口模式:15,pos接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :


load-sharing bandwidth 
  ＜1-4294967295 
＞ [{kbps 
|mbps 
|gbps 
}]

no load-sharing bandwidth 








命令参数解释 :



参数|描述
---|---
＜1-4294967295＞|负荷分担带宽。各个接口的负荷分担比例根据接口的负荷分担带宽比例计算，如设置接口fei-0/1/0/1负荷分担带宽为10000kbps，接口fei-0/1/0/2负荷分担带宽为20000kbps，则最终的分担比例为1:2取值范围：1-4294967295。接口负荷分担带宽的生效值为配置值和接口带宽两者中的较小值，如接口fei-0/1/0/1的接口带宽为100000kbps，配置负荷分担带宽为50000kbps，则接口负荷分担带宽生效值为50000kbps，如果修改负荷分担带宽配置为2000000kbps，则接口负荷分担带宽生效值为100000kbps默认值：接口的负荷分担带宽缺省与接口带宽相等。单位：kbps
kbps|单位，Kilobits per second
mbps|单位，Megabits per second
gbps|单位，Gigabits per second








缺省 :

默认值为接口带宽 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担带宽的配置。接口的负荷分担带宽缺省与接口带宽相等。接口的负荷分担带宽生效值为接口带宽和负荷分担带宽配置值中的较小值。配置生效后，可以通过show ip interface命令查看接口的负荷分担带宽生效值。





范例 :

配置gei-0/1/0/1接口的负荷分担带宽为50000kpbs。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing bandwidth 50000恢复gei-0/1/0/1接口的缺省负荷分担带宽。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no load-sharing bandwidth





相关命令 :

无 




## load-sharing priority 


load-sharing priority 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担优先级，no load-sharing priority命令用于删除接口的负荷分担优先级。当接口上需要启用动态负荷分担功能时，则需要配置负荷分担优先级。接口的负荷分担优先级用于动态调整接口负荷分担权重。动态负荷分担的计算原则：流量尽可能多的从最高优先级链路走，最高优先级链路最大流量可达到：负荷分担带宽*负荷分担水线。





命令模式 :

 ATM子接口模式,ATM接口模式,dialer接口模式,dsl接口模式,gre隧道接口模式,posgroup接口模式,serial接口模式,te隧道接口模式  






命令默认权限级别 :

ATM子接口模式:15,dsl接口模式:15,serial接口模式:15,gre隧道接口模式:15,posgroup接口模式:15,te隧道接口模式:15,dialer接口模式:15,ATM接口模式:15 






命令格式 :


load-sharing priority 
  ＜1-7 
＞ [level 
 ＜50-95 
＞]

no load-sharing priority 








命令参数解释 :



参数|描述
---|---
＜1-7＞|负荷分担优先级。取值范围：1-7，1为最低，7为最高。默认值：接口在缺省情况下没有负荷分担优先级。
＜50-95＞|可选参数，负荷分担水线, 接口在动态负荷分担的情况下，最大可以负荷的流量和接口带宽的比率。若选择level <50-95>，则表示手动配置负荷分担优先级的水线，否则，表示负荷分担优先级的水线为缺省值。取值范围：50-95。默认值：90








缺省 :

无 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担优先级的配置。接口在缺省情况下，没有负荷分担优先级，即没有开启动态负荷分担的功能。负荷分担水线即为接口在动态负荷分担的情况下，最大可以负荷的流量和接口带宽的比率。缺省情况下，接口的负荷分担水线为90%，当然，这是在开启了接口的动态负荷分担功能的前提下，即配置了负荷分担优先级的情况下。





范例 :

配置gei-0/1/0/1接口的负荷分担优先级为3。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing priority 3配置gei-0/1/0/1接口的负荷分担优先级为3及水线为80。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing priority 3 level 80删除gei-0/1/0/1接口的负荷分担优先级。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no load-sharing priority





相关命令 :

无 




## load-sharing priority 


load-sharing priority 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担优先级，no load-sharing priority命令用于删除接口的负荷分担优先级。当接口上需要启用动态负荷分担功能时，则需要配置负荷分担优先级。接口的负荷分担优先级用于动态调整接口负荷分担权重。动态负荷分担的计算原则：流量尽可能多的从最高优先级链路走，最高优先级链路最大流量可达到：负荷分担带宽*负荷分担水线。






命令模式 :

 bvi子接口模式,bvi接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

ulei子接口模式:15,bvi子接口模式:15,bvi接口模式:15,ulei接口模式:15 






命令格式 :


load-sharing priority 
  ＜1-7 
＞ [level 
 ＜50-95 
＞]

no load-sharing priority 








命令参数解释 :



参数|描述
---|---
＜1-7＞|负荷分担优先级。取值范围：1-7，1为最低，7为最高。默认值：接口在缺省情况下没有负荷分担优先级。
＜50-95＞|可选参数，负荷分担水线, 接口在动态负荷分担的情况下，最大可以负荷的流量和接口带宽的比率。若选择level <50-95>，则表示手动配置负荷分担优先级的水线，否则，表示负荷分担优先级的水线为缺省值。取值范围：50-95。默认值：90








缺省 :

无 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担优先级的配置。接口在缺省情况下，没有负荷分担优先级，即没有开启动态负荷分担的功能。负荷分担水线即为接口在动态负荷分担的情况下，最大可以负荷的流量和接口带宽的比率。缺省情况下，接口的负荷分担水线为90%，当然，这是在开启了接口的动态负荷分担功能的前提下，即配置了负荷分担优先级的情况下。






范例 :

配置gei-0/1/0/1接口的负荷分担优先级为3。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing priority 3配置gei-0/1/0/1接口的负荷分担优先级为3及水线为80。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing priority 3 level 80删除gei-0/1/0/1接口的负荷分担优先级。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no load-sharing priority






相关命令 :

无 




## load-sharing priority 


load-sharing priority 




命令功能 :

该命令工作于接口配置模式下，用于设置接口的负荷分担优先级，no load-sharing priority命令用于删除接口的负荷分担优先级。当接口上需要启用动态负荷分担功能时，则需要配置负荷分担优先级。接口的负荷分担优先级用于动态调整接口负荷分担权重。动态负荷分担的计算原则：流量尽可能多的从最高优先级链路走，最高优先级链路最大流量可达到：负荷分担带宽*负荷分担水线。





命令模式 :

 10G以太接口模式,multilink接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,通道化ce1接口模式:15,smartgroup子接口模式:15,以太子接口模式:15,multilink接口模式:15,千兆以太接口模式:15,pos接口模式:15,以太接口模式:15 






命令格式 :


load-sharing priority 
  ＜1-7 
＞ [level 
 ＜50-95 
＞]

no load-sharing priority 








命令参数解释 :



参数|描述
---|---
＜1-7＞|负荷分担优先级。取值范围：1-7，1为最低，7为最高。默认值：接口在缺省情况下没有负荷分担优先级。
＜50-95＞|可选参数，负荷分担水线, 接口在动态负荷分担的情况下，最大可以负荷的流量和接口带宽的比率。若选择level <50-95>，则表示手动配置负荷分担优先级的水线，否则，表示负荷分担优先级的水线为缺省值。取值范围：50-95。默认值：90








缺省 :

无 






使用说明 :

ATM及其子接口、以太接口及其子接口、POS接口、通道化接口、dsl接口、serial接口、smartgroup接口及其子接口、multilink接口、posgroup接口、dialer接口、gre_tunnel接口和te_tunnel接口支持负荷分担优先级的配置。接口在缺省情况下，没有负荷分担优先级，即没有开启动态负荷分担的功能。负荷分担水线即为接口在动态负荷分担的情况下，最大可以负荷的流量和接口带宽的比率。缺省情况下，接口的负荷分担水线为90%，当然，这是在开启了接口的动态负荷分担功能的前提下，即配置了负荷分担优先级的情况下。





范例 :

配置gei-0/1/0/1接口的负荷分担优先级为3。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing priority 3配置gei-0/1/0/1接口的负荷分担优先级为3及水线为80。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#load-sharing priority 3 level 80删除gei-0/1/0/1接口的负荷分担优先级。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no load-sharing priority





相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 ATM子接口模式,ATM接口模式,dsl接口模式,posgroup接口模式,pos子接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式,vbui接口模式,virtual_template子接口模式,virtual_template接口模式  






命令默认权限级别 :

serial接口模式:15,posgroup接口模式:15,ulei子接口模式:15,dsl接口模式:15,pos子接口模式:15,vbui子接口模式:15,virtual_template子接口模式:15,ulei接口模式:15,ATM接口模式:15,ATM子接口模式:15,virtual_template接口模式:15,vbui接口模式:15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。





范例 :

使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable





相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。





范例 :

使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable





相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 multilink接口模式,pos接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化ce1接口模式:15,通道化cpos_e1接口模式:15,pos接口模式:15,multilink接口模式:15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。





范例 :

使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable





相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 以太子接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,千兆以太接口模式:15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。





范例 :

使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable





相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 IPv6隧道接口模式,gre隧道接口模式,supervlan接口模式,te隧道接口模式  






命令默认权限级别 :

supervlan接口模式:15,te隧道接口模式:15,gre隧道接口模式:15,IPv6隧道接口模式:15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。





范例 :

使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable





相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 10G以太接口模式,loopback接口模式,smartgroup子接口模式,smartgroup接口模式,以太接口模式  






命令默认权限级别 :

loopback接口模式:15,smartgroup接口模式:15,10G以太接口模式:15,smartgroup子接口模式:15,以太接口模式:15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。





范例 :

使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable





相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。






范例 :

gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable






相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi接口模式:15,bvi子接口模式:15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。






范例 :

gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable






相关命令 :

无 




## logging link-status 


logging link-status 




命令功能 :

该命令工作于接口配置模式下，用于使能接口的告警功能。使能了接口的告警功能，则系统会在接口状态DOWN时进行告警，并在接口状态UP后消除告警。






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


logging link-status 
  {disable 
|enable 
}






命令参数解释 :



参数|描述
---|---
disable|与enable为二选一，选择disable表示去使能接口的告警功能。
enable|与disable为二选一，选择enable表示使能接口的告警功能。








缺省 :

父接口缺省使能，子接口缺省去使能 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。父接口缺省使能告警功能，子接口缺省去使能告警功能。





范例 :

使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status enable去使能gei-0/1/0/1接口的告警功能。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# logging link-status disable





相关命令 :

无 




## mode 


mode 




命令功能 :

该命令工作于virtual_template接口配置模式下，用于配置virtual_template虚拟模板的工作模式。virtual_template虚拟模板接口，提供一个通用的服务。当接口配置成ppp模式，服务于MPPP、L2TP业务，用于动态接口的预配置。当接口配置成ps-core模式，服务于Xgw项目，用于配置PBR（Policy Based Routing策略路由）业务。






命令模式 :

 virtual_template接口模式  






命令默认权限级别 :

15 






命令格式 :


mode 
  {ppp 
|ps-core 
}

no mode 








命令参数解释 :



参数|描述
---|---
ppp|与ps-core为二选一，选择ppp表示virtual_template虚拟模板用于PPP协议。
ps-core|与ppp为二选一，选择ps-core表示virtual_template虚拟模板用于XGW项目绑定网元。








缺省 :

无 






使用说明 :

1.该命令工作于virtual_template接口配置模式下，需要先进入virtual_template接口配置模式，才能使用。2.virtual_template接口支持的工作模式有ppp和ps-core，分别用于不同的场景。ppp模式，表示虚拟模板用于PPP协议；ps-core模式，表示虚拟模板用于xGW项目绑定网元。3.由于不同的工作模式使用在不同的场景下，接口只能支持一个工作模式，且不支持进行模式的切换和删除，如果已经配置了工作模式，再进行修改或者删除，会提示：%Error 121022: This interface has configured mode already, and does not support to change it





范例 :

将virtual_template1接口配置成ppp模式。命令如下：ZXROSNG(config)#interface virtual_template1ZXROSNG(config-if-virtual_template1)#mode ppp将virtual_template2接口配置成ps-core模式。命令如下：ZXROSNG(config)#interface virtual_template2ZXROSNG(config-if-virtual_template2)#mode ps-core





相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 10G以太接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397247#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gei-0/1/0/1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#mpls mtu 2000恢复gei-0/1/0/1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

设置接口的MPLS协议最大传输单元，使用no命令恢复缺省配置 






命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx接口模式:15,qx子接口模式:15 






命令格式 :



mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。qx接口配置范围为68~$#50397247#$，qx子接口配置范围为68~$#50397251#$。单位：字节。








缺省 :

1550 






使用说明 :

no命令恢复缺省值。 






范例 :

配置qx1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface qx1ZXROSNG(config-if-qx1)#mpls mtu 2000恢复qx1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface qx1ZXROSNG(config-if-qx1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 pos接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

4520 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置pos-0/1/1/1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface pos-0/1/1/1ZXROSNG(config-if-pos-0/1/1/1)#mpls mtu 2000恢复pos-0/1/1/1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface pos-0/1/1/1ZXROSNG(config-if-pos-0/1/1/1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 multilink接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397250#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置multilink1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface multilink1ZXROSNG(config-if-multilink1)#mpls mtu 2000恢复multilink1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface multilink1ZXROSNG(config-if-multilink1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 ATM接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397249#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置atm-0/1/0/1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface atm-0/1/0/1ZXROSNG(config-if-atm-0/1/0/1)#mpls mtu 2000恢复atm-0/1/0/1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface atm-0/1/0/1ZXROSNG(config-if-atm-0/1/0/1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 通道化ce1接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置ce1-0/1/0/1:1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface ce1-0/1/0/1:1ZXROSNG(config-if-ce1-0/1/0/1:1)#mpls mtu 2000恢复ce1-0/1/0/1:1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface ce1-0/1/0/1:1ZXROSNG(config-if-ce1-0/1/0/1:1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 smartgroup子接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置smartgroup1.1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface smartgroup1.1ZXROSNG(config-if-smartgroup1.1)#mpls mtu 2000恢复smartgroup1.1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface smartgroup1.1ZXROSNG(config-if-smartgroup1.1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 以太子接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gei-0/1/0/1.1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#mpls mtu 2000恢复gei-0/1/0/1.1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 loopback接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置loopback1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface loopback1ZXROSNG(config-if-loopback1)#mpls mtu 2000恢复loopback1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface loopback1ZXROSNG(config-if-loopback1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 smartgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397247#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置smartgroup1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#mpls mtu 2000恢复smartgroup1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置supervlan1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#mpls mtu 2000恢复supervlan1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 ATM子接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397249#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置atm-0/1/0/1.1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface atm-0/1/0/1.1ZXROSNG(config-if-atm-0/1/0/1.1)#mpls mtu 2000恢复atm-0/1/0/1.1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface atm-0/1/0/1.1ZXROSNG(config-if-atm-0/1/0/1.1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 virtual_template接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

当接口模式为PPP时，缺省值为1480；当接口模式为ps-core时，缺省值为1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置virtual_template1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface virtual_template1ZXROSNG(config-if-virtual_template1)#mpls mtu 2000恢复virtual_template1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface virtual_template1ZXROSNG(config-if-virtual_template1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 posgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

4520 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置posgroup1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if-posgroup1)#mpls mtu 2000恢复posgroup1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if-posgroup1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 ulei接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397247#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置ulei-0/1/0/1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1ZXROSNG(config-if-ulei-0/1/0/1)#mpls mtu 2000恢复ulei-0/1/0/1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1ZXROSNG(config-if-ulei-0/1/0/1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 bvi接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397247#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置bvi1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#mpls mtu 2000恢复bvi1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 bvi子接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置bvi1.1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#mpls mtu 2000恢复bvi1.1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.





范例 :

配置vlan接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface vlanZXROSNG(config-if-vlan)#mpls mtu 2000恢复vlan接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface vlanZXROSNG(config-if-vlan)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 pos子接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

4520 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置pos-0/1/1/1.1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface pos-0/1/1/1.1ZXROSNG(config-if-pos-0/1/1/1.1)#mpls mtu 2000恢复pos-0/1/1/1.1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface pos-0/1/1/1.1ZXROSNG(config-if-pos-0/1/1/1.1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 通道化cpos_e1接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

1550 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置cpos3_e1-1/2/1/1.1/1/1:1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1)#mpls mtu 2000恢复cpos3_e1-1/2/1/1.1/1/1:1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

1550 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置cpos3_e1-1/2/1/1.1/1/1:1.1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1.1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1.1)#mpls mtu 2000恢复cpos3_e1-1/2/1/1.1/1/1:1.1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1.1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1.1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 ulei子接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397248#$。单位：字节。








缺省 :

1550 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置ulei-0/1/0/1.1接口的IPv6 MTU为2000。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1.1ZXROSNG(config-if-ulei-0/1/0/1.1)#ipv6 mtu 2000恢复ulei-0/1/0/1.1接口缺省IPv6 MTU。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1.1ZXROSNG(config-if-ulei-0/1/0/1.1)#no ipv6 mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 atm_dslgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397249#$。单位：字节。








缺省 :

1550 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置atm_dslgroup1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface atm_dslgroup1ZXROSNG(config-if-atm_dslgroup1)#mpls mtu 2000恢复atm_dslgroup1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface atm_dslgroup1ZXROSNG(config-if-atm_dslgroup1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 serial接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397253#$。单位：字节。








缺省 :

1550 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置serial-0/1/0/1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface serial-0/1/0/1ZXROSNG(config-if-serial-0/1/0/1)#mpls mtu 2000恢复serial-0/1/0/1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface serial-0/1/0/1ZXROSNG(config-if-serial-0/1/0/1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 te隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1550 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置te_tunnel1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#mpls mtu 2000恢复te_tunnel1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface te_tunnel1ZXROSNG(config-if-te_tunnel1)#no mpls mtu






相关命令 :

无 




mpls mtu :

mpls mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口MPLS层最大传输单元，no mpls mtu命令用于恢复接口缺省配置。MPLS(Multi-Protocol Label Switching 多协议标签交互)，独立于第二和第三层协议，诸如ATM 和IP。它提供了一种方式，将IP地址映射为简单的具有固定长度的标签，用于不同的包转发和包交换技术。它是现有路由和交换协议的接口，如IP、ATM、帧中继、资源预留协议（RSVP）、开放最短路径优先（OSPF）等等。在MPLS 中，数据传输发生在标签交换路径（LSP）上。LSP 是每一个沿着从源端到终端的路径上的结点的标签序列。现今使用着一些标签分发协议，如标签分发协议（LDP）、RSVP 或者建于路由协议之上的一些协议，如边界网关协议（BGP）及OSPF。因为固定长度标签被插入每一个包或信元的开始处，并且可被硬件用来在两个链接间快速交换包，所以使数据的快速交换成为可能。MPLS起源于IPv4，其核心技术可扩展到多种网络协议，包括IPX（Internet Packet Exchange）、Appletalk、DECnet、CLNP（Connectionless Network Protocol）等。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送MPLS 协议报文时，其报文长度必须不超过出接口的MPLS MTU。接口MPLS MTU的配置会影响设备本地发包和转发包时MPLS协议报文的分片和重组。





命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :


mpls mtu 
  ＜MPLS-MTU 
＞

no mpls mtu 








命令参数解释 :



参数|描述
---|---
＜MPLS-MTU＞|接口的MPLS MTU值。配置范围为68~$#50397226#$。单位：字节。








缺省 :

1550 






使用说明 :

命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。配置成功后，可以通过show interface命令查看生效的MPLS MTU值。只有三层接口才允许配置MPLS MTU，如果在二层接口上配置MPLS MTU，会提示：%Error 94: The L2 interface does not support this command.






范例 :

配置gre_tunnel1接口的MPLS MTU为2000。命令如下：ZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#mpls mtu 2000恢复gre_tunnel1接口缺省MPLS MTU。命令如下：ZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#no mpls mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 10G以太接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为$#50397236#$~$#50397226#$。单位：字节。








缺省 :

1600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置gei-0/1/0/1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#mtu 2000恢复gei-0/1/0/1接口缺省二层MTU。ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 pos接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1504~$#50397226#$。单位：字节。








缺省 :

4600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置pos192-0/1/1/1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface pos192-0/1/1/1ZXROSNG(config-if-pos192-0/1/1/1)#mtu 2000恢复pos192-0/1/1/1接口缺省二层MTU。ZXROSNG(config)#interface pos192-0/1/1/1ZXROSNG(config-if-pos192-0/1/1/1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 pos子接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1504~$#50397226#$。单位：字节。








缺省 :

4600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置pos192-0/1/1/1.1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface pos192-0/1/1/1.1ZXROSNG(config-if-pos192-0/1/1/1.1)#mtu 2000恢复pos192-0/1/1/1.1接口缺省二层MTU。ZXROSNG(config)#interface pos192-0/1/1/1.1ZXROSNG(config-if-pos192-0/1/1/1.1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 通道化cpos_e1接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1504~$#50397226#$。单位：字节。








缺省 :

1600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置cpos3_e1-1/2/1/1.1/1/1:1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1)#mtu 2000恢复cpos3_e1-1/2/1/1.1/1/1:1接口缺省二层MTU。ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1504~$#50397226#$。单位：字节。








缺省 :

1600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置cpos3_e1-1/2/1/1.1/1/1:1.1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1.1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1.1)#mtu 2000恢复cpos3_e1-1/2/1/1.1/1/1:1.1接口缺省二层MTU。ZXROSNG(config)#interface cpos3_e1-1/2/1/1.1/1/1:1.1ZXROSNG(config-if-cpos3_e1-1/2/1/1.1/1/1:1.1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 ATM接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1512~$#50397226#$。单位：字节。








缺省 :

1600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

接口的二层MTU值。配置范围为1512~$#50397226#$。单位：字节。






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 multilink接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1510~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置multilink1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface multilink1ZXROSNG(config-if-multilink1)#mtu 2000恢复multilink1接口缺省二层MTU。ZXROSNG(config)#interface multilink1ZXROSNG(config-if-multilink1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 通道化ce1接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1504~$#50397226#$。单位：字节。








缺省 :

1600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置ce1-0/1/0/1:1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface ce1-0/1/0/1:1ZXROSNG(config-if-ce1-0/1/0/1:1)#mtu 2000恢复ce1-0/1/0/1:1接口缺省二层MTU。ZXROSNG(config)#interface ce1-0/1/0/1:1ZXROSNG(config-if-ce1-0/1/0/1:1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 smartgroup子接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为$#50397238#$~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置smartgroup1.1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface smartgroup1.1ZXROSNG(config-if-smartgroup1.1)#mtu 2000恢复smartgroup1.1接口缺省二层MTU。ZXROSNG(config)#interface smartgroup1.1ZXROSNG(config-if-smartgroup1.1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 以太子接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为$#50397238#$~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置gei-0/1/0/1.1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#mtu 2000恢复gei-0/1/0/1.1接口缺省二层MTU。ZXROSNG(config)#interface gei-0/1/0/1.1ZXROSNG(config-if-gei-0/1/0/1.1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 smartgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为$#50397236#$~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置smartgroup1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#mtu 2000恢复smartgroup1接口缺省二层MTU。ZXROSNG(config)#interface smartgroup1ZXROSNG(config-if-smartgroup1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 supervlan接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1522~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置supervlan1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#mtu 2000恢复supervlan1接口缺省二层MTU。ZXROSNG(config)#interface supervlan1ZXROSNG(config-if-supervlan1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 ATM子接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1512~$#50397226#$。单位：字节。








缺省 :

1600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置atm-0/1/0/1.1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface atm-0/1/0/1.1ZXROSNG(config-if-atm-0/1/0/1.1)#mtu 2000恢复atm-0/1/0/1.1接口缺省二层MTU。ZXROSNG(config)#interface atm-0/1/0/1.1ZXROSNG(config-if-atm-0/1/0/1.1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 posgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1504~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置posgroup1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface posgroup1ZXROSNG(config-if-posgroup1)#mtu 2000恢复posgroup1接口缺省二层MTU。ZXROSNG(config)#interface posgroup1ZXROSNG(config-if-posgroup1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组





命令模式 :

 ulei接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1514~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置ulei-0/1/0/1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1ZXROSNG(config-if-ulei-0/1/0/1)#mtu 2000恢复ulei-0/1/0/1接口缺省二层MTU。ZXROSNG(config)#interface ulei-0/1/0/1ZXROSNG(config-if-ulei-0/1/0/1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组





命令模式 :

 bvi接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1514~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置bvi1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#mtu 2000恢复bvi1接口缺省二层MTU。ZXROSNG(config)#interface bvi1ZXROSNG(config-if-bvi1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组





命令模式 :

 bvi子接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1522~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置bvi1.1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#mtu 2000恢复bvi1.1接口缺省二层MTU。ZXROSNG(config)#interface bvi1.1ZXROSNG(config-if-bvi1.1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组





命令模式 :

 ulei子接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1522~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置ulei-0/1/0/1.1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface ulei-0/1/0/1.1ZXROSNG(config-if-ulei-0/1/0/1.1)#mtu 2000恢复ulei-0/1/0/1.1接口缺省二层MTU。ZXROSNG(config)#interface ulei-0/1/0/1.1ZXROSNG(config-if-ulei-0/1/0/1.1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组





命令模式 :

 eth_dslgroup子接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1522~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置eth_dslgroup1.1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface eth_dslgroup1.1ZXROSNG(config-if-eth_dslgroup1.1)#mtu 2000恢复eth_dslgroup1.1接口缺省二层MTU。ZXROSNG(config)#interface eth_dslgroup1.1ZXROSNG(config-if-eth_dslgroup1.1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。 






命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx子接口模式:15,qx接口模式:15 






命令格式 :



mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1514~$#50397226#$。单位：字节。








缺省 :

1600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置qx接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface qxZXROSNG(config-if-qx)#mtu 2000恢复qx接口缺省二层MTU。ZXROSNG(config)#interface qxZXROSNG(config-if-qx)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 eth_dslgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1514~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置eth_dslgroup1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface eth_dslgroup1ZXROSNG(config-if-eth_dslgroup1)#mtu 2000恢复eth_dslgroup1接口缺省二层MTU。ZXROSNG(config)#interface eth_dslgroup1ZXROSNG(config-if-eth_dslgroup1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 atm_dslgroup接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1512~$#50397226#$。单位：字节。








缺省 :

$#50397226#$ 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置atm_dslgroup1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface atm_dslgroup1ZXROSNG(config-if-atm_dslgroup1)#mtu 2000恢复atm_dslgroup1接口缺省二层MTU。ZXROSNG(config)#interface atm_dslgroup1ZXROSNG(config-if-atm_dslgroup1)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 serial接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1504~$#50397226#$。单位：字节。








缺省 :

1600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置serial-0/1/0/11接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface serial-0/1/0/11ZXROSNG(config-if-serial-0/1/0/11)#mtu 2000恢复serial-0/1/0/11接口缺省二层MTU。ZXROSNG(config)#interface serial-0/1/0/11ZXROSNG(config-if-serial-0/1/0/11)#no mtu






相关命令 :

无 




mtu :

mtu 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层最大传输单元，no mtu命令用于恢复接口缺省配置。最大传输单元(Maximum Transmission Unit，MTU)是指一种通信协议在某一层上面所能通过的最大数据报大小（以字节为单位）。路由器在对外发送链路层报文时，其报文长度必须不超过出接口的二层MTU。接口二层MTU的配置会影响设备本地发包和转发包时协议报文的分片和重组。





命令模式 :

 dialer接口模式  






命令默认权限级别 :

15 






命令格式 :


mtu 
  ＜MTU 
＞

no mtu 








命令参数解释 :



参数|描述
---|---
＜MTU＞|接口的二层MTU值。配置范围为1504~$#50397226#$。单位：字节。








缺省 :

4600 






使用说明 :

配置成功后，可以通过show interface命令查看生效的MTU值。 






范例 :

配置dialer1接口的二层MTU为2000。命令如下：ZXROSNG(config)#interface dialer1ZXROSNG(config-if-dialer1)#mtu 2000恢复dialer1接口缺省二层MTU。ZXROSNG(config)#interface dialer1ZXROSNG(config-if-dialer1)#no mtu






相关命令 :

无 




## multicast ecmp-cost 


multicast ecmp-cost 




命令功能 :

该命令工作于接口配置模式下，用于设置接口ECMP链路的组播带宽权重，no multicast ecmp-cost命令用于恢复接口缺省的ECMP链路的组播带宽权重。当接口上需要启用ECMP链路组播负荷分担功能时，需要配置ECMP链路的组播带宽权重。ECMP（Equal Cost Multipath等值多路径）：存在多条不同链路到达同一目的地址的网络环境中，如果使用传统的路由技术，发往该目的地址的数据包只能利用其中的一条链路，其它链路处于备份状态或无效状态，并且在动态路由环境下相互的切换需要一定时间，而等值多路径路由协议可以在该网络环境下同时使用多条链路，不仅增加了传输带宽，并且可以无时延无丢包地备份失效链路的数据传输。ECMP最大的特点是实现了等值情况下，多路径负载均衡和链路备份的目的，在静态路由和OSPF（Open Shortest Path First开放式最短路径优先）中基本上都支持ECMP功能。





命令模式 :

 dsl接口模式,e1接口模式,posgroup接口模式,pos子接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式,vbui接口模式,三层VLAN接口模式  






命令默认权限级别 :

vbui子接口模式:15,pos子接口模式:15,三层VLAN接口模式:15,ulei接口模式:15,vbui接口模式:15,ulei子接口模式:15,e1接口模式:15,serial接口模式:15,dsl接口模式:15,posgroup接口模式:15 






命令格式 :


multicast ecmp-cost 
  ＜multicast ecmp-cost 
＞

no multicast ecmp-cost 








命令参数解释 :



参数|描述
---|---
＜multicast ecmp-cost＞|ECMP链路的组播带宽权重。取值范围：1-8，1为最低，8为最高。默认值：接口缺省的ECMP链路的组播带宽权重为1。








缺省 :

1 






使用说明 :

以太接口及其子接口、POS接口及其子接口、通道化接口、e1接口、dsl接口、serial接口、ULEI接口及其子接口、sg接口及其子接口、vbui接口及其子接口、vlan接口、multilink接口、posgroup接口、loopback接口支持ECMP链路的组播带宽权重的配置。缺省情况下，接口的ECMP链路的组播带宽权重为1。





范例 :

配置gei-0/1/0/1接口的ECMP链路的组播带宽权重为3。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# multicast ecmp-cost 3恢复gei-0/1/0/1接口的缺省ECMP链路的组播带宽权重。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no multicast ecmp-cost





相关命令 :

无 




## multicast ecmp-cost 


multicast ecmp-cost 




命令功能 :

该命令工作于接口配置模式下，用于设置接口ECMP链路的组播带宽权重，no multicast ecmp-cost命令用于恢复接口缺省的ECMP链路的组播带宽权重。当接口上需要启用ECMP链路组播负荷分担功能时，需要配置ECMP链路的组播带宽权重。ECMP（Equal Cost Multipath等值多路径）：存在多条不同链路到达同一目的地址的网络环境中，如果使用传统的路由技术，发往该目的地址的数据包只能利用其中的一条链路，其它链路处于备份状态或无效状态，并且在动态路由环境下相互的切换需要一定时间，而等值多路径路由协议可以在该网络环境下同时使用多条链路，不仅增加了传输带宽，并且可以无时延无丢包地备份失效链路的数据传输。ECMP最大的特点是实现了等值情况下，多路径负载均衡和链路备份的目的，在静态路由和OSPF（Open Shortest Path First开放式最短路径优先）中基本上都支持ECMP功能。






命令模式 :

 supervlan接口模式,通道化cpos_e1子接口模式  






命令默认权限级别 :

通道化cpos_e1子接口模式:15,supervlan接口模式:15 






命令格式 :


multicast ecmp-cost 
  ＜multicast ecmp-cost 
＞

no multicast ecmp-cost 








命令参数解释 :



参数|描述
---|---
＜multicast ecmp-cost＞|ECMP链路的组播带宽权重。取值范围：1-8，1为最低，8为最高。默认值：接口缺省的ECMP链路的组播带宽权重为1。








缺省 :

1 






使用说明 :

以太接口及其子接口、POS接口及其子接口、通道化接口、e1接口、dsl接口、serial接口、ULEI接口及其子接口、sg接口及其子接口、vbui接口及其子接口、vlan接口、multilink接口、posgroup接口、loopback接口支持ECMP链路的组播带宽权重的配置。缺省情况下，接口的ECMP链路的组播带宽权重为1。






范例 :

配置gei-0/1/0/1接口的ECMP链路的组播带宽权重为3。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# multicast ecmp-cost 3恢复gei-0/1/0/1接口的缺省ECMP链路的组播带宽权重。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no multicast ecmp-cost






相关命令 :

无 




## multicast ecmp-cost 


multicast ecmp-cost 




命令功能 :

该命令工作于接口配置模式下，用于设置接口ECMP链路的组播带宽权重，no multicast ecmp-cost命令用于恢复接口缺省的ECMP链路的组播带宽权重。当接口上需要启用ECMP链路组播负荷分担功能时，需要配置ECMP链路的组播带宽权重。ECMP（Equal Cost Multipath等值多路径）：存在多条不同链路到达同一目的地址的网络环境中，如果使用传统的路由技术，发往该目的地址的数据包只能利用其中的一条链路，其它链路处于备份状态或无效状态，并且在动态路由环境下相互的切换需要一定时间，而等值多路径路由协议可以在该网络环境下同时使用多条链路，不仅增加了传输带宽，并且可以无时延无丢包地备份失效链路的数据传输。ECMP最大的特点是实现了等值情况下，多路径负载均衡和链路备份的目的，在静态路由和OSPF（Open Shortest Path First开放式最短路径优先）中基本上都支持ECMP功能。






命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi接口模式:15,bvi子接口模式:15 






命令格式 :


multicast ecmp-cost 
  ＜multicast ecmp-cost 
＞

no multicast ecmp-cost 








命令参数解释 :



参数|描述
---|---
＜multicast ecmp-cost＞|ECMP链路的组播带宽权重。取值范围：1-8，1为最低，8为最高。默认值：接口缺省的ECMP链路的组播带宽权重为1。








缺省 :

1 






使用说明 :

以太接口及其子接口、POS接口及其子接口、通道化接口、e1接口、dsl接口、serial接口、ULEI接口及其子接口、sg接口及其子接口、vbui接口及其子接口、vlan接口、multilink接口、posgroup接口、loopback接口支持ECMP链路的组播带宽权重的配置。缺省情况下，接口的ECMP链路的组播带宽权重为1。






范例 :

配置gei-0/1/0/1接口的ECMP链路的组播带宽权重为3。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# multicast ecmp-cost 3恢复gei-0/1/0/1接口的缺省ECMP链路的组播带宽权重。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no multicast ecmp-cost





相关命令 :

无 




## multicast ecmp-cost 


multicast ecmp-cost 




命令功能 :

该命令工作于接口配置模式下，用于设置接口ECMP链路的组播带宽权重，no multicast ecmp-cost命令用于恢复接口缺省的ECMP链路的组播带宽权重。当接口上需要启用ECMP链路组播负荷分担功能时，需要配置ECMP链路的组播带宽权重。ECMP（Equal Cost Multipath等值多路径）：存在多条不同链路到达同一目的地址的网络环境中，如果使用传统的路由技术，发往该目的地址的数据包只能利用其中的一条链路，其它链路处于备份状态或无效状态，并且在动态路由环境下相互的切换需要一定时间，而等值多路径路由协议可以在该网络环境下同时使用多条链路，不仅增加了传输带宽，并且可以无时延无丢包地备份失效链路的数据传输。ECMP最大的特点是实现了等值情况下，多路径负载均衡和链路备份的目的，在静态路由和OSPF（Open Shortest Path First开放式最短路径优先）中基本上都支持ECMP功能。





命令模式 :

 10G以太接口模式,loopback接口模式,multilink接口模式,pos接口模式,smartgroup子接口模式,smartgroup接口模式,以太子接口模式,以太接口模式,千兆以太接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,10G以太接口模式:15,smartgroup接口模式:15,loopback接口模式:15,以太子接口模式:15,smartgroup子接口模式:15,通道化ce1接口模式:15,multilink接口模式:15,pos接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :


multicast ecmp-cost 
  ＜multicast ecmp-cost 
＞

no multicast ecmp-cost 








命令参数解释 :



参数|描述
---|---
＜multicast ecmp-cost＞|ECMP链路的组播带宽权重。取值范围：1-8，1为最低，8为最高。默认值：接口缺省的ECMP链路的组播带宽权重为1。








缺省 :

1 






使用说明 :

以太接口及其子接口、POS接口及其子接口、通道化接口、e1接口、dsl接口、serial接口、ULEI接口及其子接口、sg接口及其子接口、vbui接口及其子接口、vlan接口、multilink接口、posgroup接口、loopback接口支持ECMP链路的组播带宽权重的配置。缺省情况下，接口的ECMP链路的组播带宽权重为1。





范例 :

配置gei-0/1/0/1接口的ECMP链路的组播带宽权重为3。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# multicast ecmp-cost 3恢复gei-0/1/0/1接口的缺省ECMP链路的组播带宽权重。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no multicast ecmp-cost





相关命令 :

无 




## port-limit untag 


port-limit untag 




命令功能 :

该命令工作于控制面安全接口配置模式下，用于设置接口的控制面安全参数，no port-limit untag命令用于恢复接口的控制面安全缺省配置。越来越多的网络攻击开始针对核心路由器，例如ICMP攻击、IP分片攻击、TCP攻击、DDOS攻击等等，使得路由器的安全性成为重要的技术参数。除了常见的DOS攻击之外，路由器也受到路由协议等控制平面的流量冲击，这些流量属于合法的流量，但是由于流量过大，或者路由器控制平面处理负荷过重而导致CPU瘫痪，致使路由器不可用。通过设置接口的控制面安全参数，防止路由器受到上述攻击，确保路由器稳定工作。接口上送控制面报文利用令牌桶（Token Bucket，TB）进行流量控制。令牌桶的原理：1.令牌以一定的速率放入桶中。2.每个令牌允许源发送一定数量的比特。3.发送一个包，流量调节器就要从桶中删除与包大小相等的令牌数。4.如果没有足够的令牌发送包，这个包就会等待直到有足够的令牌(在整形器的情况下)或者包被丢弃，也有可能被标记更低的DSCP(在策略者的情况下)。 5.桶有特定的容量，如果桶已经满了，新加入的令牌就会被丢弃。因此，在任何时候，源发送到网络上的最大突发数据量与桶的大小成比例。令牌桶允许突发，但是不能超过限制。接口的控制面安全参数包括CIR和CBS。CIR(Committed Information Rate，承诺信息速率)，设备按照这个速度向令牌桶中放置令牌，报文的流量只能是小于或者等于令牌生成的速度，如果流量超过该速率，则丢弃信息流或进行流控制。CBS(Committed Burst Size，承诺突发尺寸)，定义了令牌桶的容量，即每次突发所允许的最大流量尺寸。如果流量超过该尺寸，则丢弃信息流或进行流控制。





命令模式 :

 CPS接口模式  






命令默认权限级别 :

15 






命令格式 :


port-limit untag 
  {high 
 cir 
 ＜0-200000 
＞ [{pps 
|kpps 
}] cbs 
 {＜16-20000 
＞ [{kb 
|mb 
}]|default 
}|low 
 cir 
 ＜0-200000 
＞ [{pps 
|kpps 
}] cbs 
 {＜16-20000 
＞ [{kb 
|mb 
}]|default 
}}
no port-limit untag 
  {high 
 cir 
 cbs 
|low 
 cir 
 cbs 
}
				






命令参数解释 :



参数|描述
---|---
＜0-200000＞|承诺信息速率，令牌桶放置令牌的速率。单位：pps(包/秒)取值范围：0-200000默认值：高桶255pps，低桶745pps
pps|单位：Packets per second
kpps|单位：Kilopackets per second
＜16-20000＞|和default为二选一，承诺突发尺寸，令牌桶的容量。单位：KB取值范围：16-20000默认值：选择default表示为缺省情况，根据子卡类型进行适配。
kb|单位：Kilobyte
mb|单位：Megabyte
default|和16-20000为二选一，承诺突发尺寸，令牌桶的容量。选择default表示为缺省情况，根据子卡类型进行适配。
＜0-200000＞|承诺信息速率，令牌桶放置令牌的速率。单位：pps(包/秒)取值范围：0-200000默认值：高桶255pps，低桶745pps






No参数|描述
---|---
cir|约定信息速率
cbs|约定突发流量








缺省 :

高桶cir缺省值为255，低桶cir缺省值为745，高桶、低桶cbs缺省值都是0





使用说明 :

该命令工作于控制面安全接口配置模式下，需要先进入控制面安全接口配置模式，才能使用。配置成功后，可以通过show cps port-limit命令查看接口生效的控制面安全属性。物理接口、ULEI接口、smartgroup接口、eth_dslgroup接口、atm_dslgroup接口、multilink接口和posgroup接口支持接口的控制面安全参数配置。





范例 :

配置gei-0/1/0/1接口的高桶CIR为4000pps、CBS为200KB。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1” 依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1ZXROSNG(config-cps-if-gei-0/1/0/1)#port-limit untag high cir 4000 cbs 200配置gei-0/1/0/1接口的低桶CIR为2000pps、CBS为100KB。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1ZXROSNG(config-cps-if-gei-0/1/0/1)#port-limit untag low cir 2000 cbs 100恢复gei-0/1/0/1接口缺省的高桶CIR和CBS。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1ZXROSNG(config-cps-if-gei-0/1/0/1)#no port-limit untag high cir cbs恢复gei-0/1/0/1接口缺省的低桶CIR和CBS：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1ZXROSNG(config-cps-if-gei-0/1/0/1)#no port-limit untag low cir cbs





相关命令 :

无



## port-limit 


port-limit 




命令功能 :

该命令工作于控制面安全子接口配置模式下，用于设置子接口的控制面安全参数，no port-limit命令用于恢复子接口的控制面安全缺省配置。和port-limit untag命令的作用类似，该命令通过设置子接口的控制面安全参数，防止路由器受到攻击，确保路由器稳定工作，区别在于port-limit untag命令用于配置父接口，而本命令用于配置子接口。





命令模式 :

 CPS子接口模式  






命令默认权限级别 :

15 






命令格式 :


port-limit 
  {high 
 cir 
 ＜0-200000 
＞ [{pps 
|kpps 
}] cbs 
 {＜16-20000 
＞ [{kb 
|mb 
}]|default 
}|low 
 cir 
 ＜0-200000 
＞ [{pps 
|kpps 
}] cbs 
 {＜16-20000 
＞ [{kb 
|mb 
}]|default 
}}
no port-limit 
  {high 
 cir 
 cbs 
|low 
 cir 
 cbs 
}
				






命令参数解释 :



参数|描述
---|---
＜0-200000＞|承诺信息速率，令牌桶放置令牌的速率。单位：pps(包/秒)取值范围：0-200000默认值：高桶255pps，低桶745pps
pps|单位：Packets per second
kpps|单位：Kilopackets per second
＜16-20000＞|和default为二选一，承诺突发尺寸，令牌桶的容量。单位：KB取值范围：16-20000默认值：选择default表示为缺省情况，根据子卡类型进行适配。
kb|单位：Kilobyte
mb|单位：Megabyte
default|和16-20000为二选一，承诺突发尺寸，令牌桶的容量。选择default表示为缺省情况，根据子卡类型进行适配。






No参数|描述
---|---
cir|约定信息速率
cbs|约定突发流量








缺省 :

高桶cir缺省值为255，低桶cir缺省值为745，高桶、低桶cbs缺省值都是0





使用说明 :

本命令只支持子接口配置





范例 :

配置gei-0/1/0/1.1接口的高桶CIR为4000pps、CBS为200KB。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1” 依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1.1ZXROSNG(config-cps-if-gei-0/1/0/1.1)#port-limit high cir 4000 cbs 200配置gei-0/1/0/1.1接口的低桶CIR为4000pps、CBS为200KB。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1” 依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1.1ZXROSNG(config-cps-if-gei-0/1/0/1.1)#port-limit low cir 2000 cbs 100恢复gei-0/1/0/1.1接口缺省的高桶CIR和CBS。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1”依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1.1ZXROSNG(config-cps-if-gei-0/1/0/1.1)#no port-limit high cir cbs恢复gei-0/1/0/1.1接口缺省的低桶CIR和CBS。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1” 依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1.1ZXROSNG(config-cps-if-gei-0/1/0/1.1)#no port-limit low cir cbs





相关命令 :

show cps port-limit



## pw 


pw 




命令功能 :

该命令用于创建伪线。no pw命令可以删除伪线。伪线（Pseudo Wire）是在边缘路由器之间的一个点对点的连接。它的主要功能是仿效类似以太网的服务通过一个隐藏的核心 MPLS（Multi-Protocol Label Switching多协议标签交换）网络，通过封装到一个共同的 MPLS 格式中。伪线相当于MPLS网络中本地AC（Attachment Circuit，接入链路）到对端AC直接的一条直连通路，完成用户的二层数据透传。在VPLS（Virtual Private Lan Service，虚拟专用局域网业务）、VPWS（Virtual Pseudo Wire Service虚拟专用线路服务）的组网环境中，需要用到伪线。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


pw 
  ＜interface-name 
＞
no pw 
  ＜interface-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|PW实例名








缺省 :

无 






使用说明 :

该命令工作于全局配置模式下，需要先进入全局配置模式，才能使用。伪线名为pw+伪线号组成，例如：pw1、pw2。可以通过show pw命令查看系统当前所有的伪线。





范例 :

创建pw1伪线。伪线名称为”pw1”，其中1表示伪线号。命令如下：ZXROSNG(config)#pw pw1删除pw1伪线。伪线名称为”pw1”，其中1表示伪线号。命令如下：ZXROSNG(config)#no pw pw1





相关命令 :

无 




## revert interface 


revert interface 




命令功能 :

指定恢复接口默认值 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



revert interface 
  ＜interface-name 
＞







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名








缺省 :

无 






使用说明 :

指定恢复接口默认值会将接口相关的配置全部删除，所以在执行该命令时，会通过交互式的询问方式向用户确定是否进行恢复。提示如下：The operation will restore the interface configuration to the default. Continue? [yes/no]:无 






范例 :

指定恢复smartgroup1接口的默认值ZXROSNG(config)#revert interface smartgroup1ZXROSNG(config)#The operation will restore the interface configuration to the default. Continue? [yes/no]:yesZXROSNG(config)#






相关命令 :

无 




## show cps port-limit 


show cps port-limit 




命令功能 :

命令用于显示接口或者子接口控制面安全属性。接口的控制面安全属性包括高桶CIR、CBS和低桶CIR、CBS。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show cps port-limit 
 interface 
 ＜interface-name 
＞ 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口的控制面安全属性。可以通过show ip interfacebrief命令查询当前设备上的接口。取值范围： 配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

物理接口及其子接口、ULEI接口及其子接口、smartgroup接口及其子接口、eth_dslgroup接口、atm_dslgroup接口、multilink接口和posgroup接口支持显示接口的控制面安全属性。命令指定显示的接口如果不存在，会提示：%Info 85: No such interface(s)





范例 :

ZXROSNG(config)# show cps port-limit interface gei-0/1/0/1High cir(pps)   High cbs(KB)     Low cir(pps)   Low cbs(KB)4000            200            2000         100输出项名称    输出结果解释High cir(pps)    接口的高桶承诺信息速率，令牌桶放置令牌的速率。单位pps(包/秒)High cbs(KB)    接口的高桶承诺突发尺寸，令牌桶的容量。单位KBLow cir(pps)    接口的低桶承诺信息速率，令牌桶放置令牌的速率。单位pps(包/秒)Low cbs(KB)    接口的低桶承诺突发尺寸，令牌桶的容量。单位KB





相关命令 :

无



## show cps vlan-limit 


show cps vlan-limit 




命令功能 :

命令用于显示子接口基于VLAN的控制面安全属性。子接口基于VLAN的控制面安全属性包括高桶CIR、CBS和低桶CIR、CBS。





命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :


show cps vlan-limit 
 interface 
 ＜interface-name 
＞ 






命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口基于VLAN的控制面安全属性。可以通过show ip interfacebrief命令查询当前设备上的接口。取值范围： 配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

物理子接口、ULEI子接口、smartgroup子接口支持显示子接口基于VLAN的控制面安全属性。命令指定显示的接口如果不存在，会提示：%Info 85: No such interface(s)命令指定显示的接口不支持显示基于VLAN的控制面安全属性，会提示：%Info 121139: The interface does not support the configuration命令指定显示的接口没有基于VLAN的控制面安全限制，则无任何显示。





范例 :

ZXROSNG(config)# show cps vlan-limit interface gei-0/1/0/1.1High cir(pps)   High cbs(KB)     Low cir(pps)   Low cbs(KB)4000            200            2000         100输出项名称    输出结果解释High cir(pps)    子接口基于VLAN的高桶承诺信息速率，令牌桶放置令牌的速率。单位pps(包/秒)High cbs(KB)    子接口基于VLAN的高桶承诺突发尺寸，令牌桶的容量。单位KBLow cir(pps)    子接口基于VLAN的低桶承诺信息速率，令牌桶放置令牌的速率。单位pps(包/秒)Low cbs(KB)    子接口基于VLAN的低桶承诺突发尺寸，令牌桶的容量。单位KB





相关命令 :

无 




## show interface brief 


show interface brief 




命令功能 :

该命令用于显示系统所有二层接口的简要信息。接口的简要信息包括：接口名、光电属性、双工模式、带宽、管理状态、物理状态、协议状态和接口描述信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show interface brief 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令只显示二层接口的简要信息。 






范例 :

ZXROSNG(config)#show interface brief Interface     Portattribute  Mode  BW(Mbps)  Admin Phy   Prot  Description gei-0/1/0/1   electric   Duplex/full  100    down  down  down  ether1gei-0/1/0/2   electric   Duplex/full  100    down  down  down  ether2smartgroup1   N/A        N/A                 up    up    down  smartgroup2   N/A        N/A                 up    up    down输出项名称    输出结果解释Interface    接口名Portattribute    接口光电属性：electric表示电口，optical表示光口，pho&elec表示光电混合口，N/A表示无光电属性。Mode    接口双工模式：Duplex/full表示全双工模式，Duplex/half表示半双工模式，Duplex/auto表示自动协商模式，N/A表示无双工模式。BW(Mbps)    接口带宽，单位Mbps。Admin    接口管理状态：up表示接口管理状态up，down表示接口管理状态down。Phy    接口物理状态：up表示接口物理状态up，down表示接口物理状态down。Prot    接口协议状态：up表示接口协议状态up，down表示接口协议状态down。Description    接口描述信息，可以通过description命令进行配置，如果接口未配置描述信息，该项则为空。





相关命令 :

无 




## show interface description 


show interface description 




命令功能 :

该命令用于显示接口的描述信息，包括：接口名、光电属性、双工模式、带宽、管理状态、物理状态、协议状态和接口描述信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show interface description 
  [＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口的描述信息。可以通过show ip interfacebrief命令查询当前设备上的接口。取值范围： 配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令可以显示系统所有接口的描述信息，也可以显示指定接口的描述信息。指定显示的接口如果不存在，会提示：%Info 85: No such interface(s)





范例 :

ZXROSNG(config)#show interface descriptionInterface                       AdminStatus  PhyStatus  Protocol  Descriptiongei-0/1/0/1                      down         down       down     ether1gei-0/1/0/2                      down         down       down     ether2pos192-0/1/1/1                 down         down       down      pos192-0/1/1/2                 down         down       down      smartgroup1                    up           up         down      smartgroup2                    up           up         down输出项名称    输出结果解释Interface    接口名AdminStatus    接口管理状态：up表示接口管理状态up，down表示接口管理状态down。PhyStatus    接口物理状态：up表示接口物理状态up，down表示接口物理状态down。Protocol    接口协议状态：up表示接口协议状态up，down表示接口协议状态down。Description    接口描述信息，可以通过description命令进行配置，如果接口未配置描述信息，该项则为空。显示gei-0/1/0/1接口的描述信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#show interface description gei-0/1/0/1Interface                       AdminStatus  PhyStatus  Protocol  Descriptiongei-0/1/0/1                      down         down       down     ether1





相关命令 :

无 




## show interface 


show interface 




命令功能 :

该命令详细显示端口的各个统计信息，用于分析网络流量。接口的统计信息包括：接口名、接口状态、描述信息、硬件类型、MAC地址、IP地址、带宽、IP MTU、二层MTU、IPv6 MTU、MPLS MTU、保持时间、光电属性、环回方式、双工模式、协商模式、ARP信息以及接口的流量统计值。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show interface 
  [{＜interface-name 
＞|include 
 ＜regular-expression 
＞|exclude 
 ＜regular-expression 
＞}] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口的统计信息。可以通过show ip interfacebrief命令查询当前设备上的接口。取值范围： 配置范围为1-31位的字符串。默认值：无。
include|和exclude是二选一，若选择include，则表示显示接口名中包含指定字符或字符串的接口的IP协议简要信息，需要和参数<WORD>共同作用。
＜regular-expression＞|指定字符或字符串，需要和参数{include|exclude}共同作用，表示显示接口名中包含或不包含指定字符或字符串的接口的IP协议简要信息。取值范围：配置范围为1-31位的字符串。默认值：无。
exclude|和exclude是二选一，若选择exclude，则表示显示接口名中不包含指定字符或字符串的接口的IP协议简要信息，需要和参数<WORD>共同作用。
＜regular-expression＞|指定字符或字符串，需要和参数{include|exclude}共同作用，表示显示接口名中包含或不包含指定字符或字符串的接口的IP协议简要信息。取值范围：配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令支持显示系统所有接口的统计信息，同时也支持显示指定接口的统计信息。查询子接口、te_tunnel和vlan接口流量统计信息时，要确保接口统计开关已经开启，否则将不会有相关的流量统计信息。对于不支持接口流量统计功能的接口，使用show interface查询不到接口流量统计信息。不同的接口使用show interface查询到的计数项不同，显示的计数区域也不一样。比如以太接口流量统计信息显示分为HardWareCounters计数区和StreamCounters计数区，而子接口仅支持显示stream counter计数区。这取决于不同的接口采用不同的统计计数方法。可以使用clear statistics interface命令将当前查询到接口流量统计信息清零。命令指定显示的接口如果不存在，会提示：%Info 85: No such interface(s)





范例 :

ZXROSNG(config)#show interface gei-0/1/0/1gei-0/1/0/1 is administratively down, line protocol is down, detected status is RX-SF/TX-SF  Last line protocol up time :  2014-02-06 14:21:47   Description is is ether1  Hardware is Fast Ethernet, address is 0019.8407.2300  Internet address is 2.2.2.2/24  BW 100000 Kbps  IP MTU 1500 bytes  MTU 1600 bytes  MPLS MTU 1550 bytes  Holdtime is 120 sec(s)  The port is electric  The MDIMode of the port is reserved  Loopback cancel  Duplex full  Negotiation auto  ARP type ARP:  ARP Timeout 04:00:00   Last Clear Time : 2014-02-07 02:36:50  Last Refresh Time: 2014-02-07 08:31:00  120s input rate : 0Bps                 0Pps                 120s output rate: 0Bps                 0Pps                 Peak rate:                                                  input             0Bps                 peak time          N/A  output            0Bps                 peak time          N/A  Intf utilization: input 0%             output 0%            HardWareCounters:                                           In_Bytes          21420                In_Packets         21420  In_CRC_ERROR      21420                In_Unicasts        21420  In_Broadcasts     21420                In_Multicasts      21420  In_Undersize      21420                In_Oversize        21420  In_64B            21420                In_65_127B         21420  In_128_255B       21420                In_256_511B        21420  In_512_1023B      21420                In_1024_1518B      21420  In_1519_MaxB      21420                                     E_Bytes           21420                E_Packets          21420  E_CRC_ERROR       21420                E_Unicasts         21420  E_Broadcasts      21420                E_Multicasts       21420  E_Undersize       21420                E_Oversize         21420  E_64B             21420                E_65_127B          21420  E_128_255B        21420                E_256_511B         21420  E_512_1023B       21420                E_1024_1518B       21420  E_1519_MaxB       21420                                     StreamCounters  :                                           In_Bytes          20880                In_Packets         20880  In_Discards       20880                In_V4Bytes         20880  In_V4Pkts         20880                In_V6Bytes         20880  In_V6Pkts         20880                In_UpsendCar_Drop  20880  E_Bytes           20880                E_Packets          20880  E_Discards        20880                E_V4Bytes          20880  E_V4Pkts          20880                E_V6Bytes          20880  E_V6Pkts          20880                E_UpsendCar_Drop   20880输出项名称    输出结果解释gei-0/1/0/1    接口名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。is administratively down    接口管理状态和物理状态，如果接口的管理状态down，显示”is administratively down”，接口的管理状态up的情况下，如果物理状态down，显示”is down”，如果物理状态up，显示”is up”。line protocol is down    接口的协议状态，协议状态up，显示”line protocol is up”，协议状态down，显示”line protocol is down”。detected status   接口检测状态。Last line protocol up time   接口最近一次协议状态up时间，如果接口没有up过，显示”-”。Description    接口描述信息，可以通过description命令进行配置，如果接口未配置描述信息，则不显示。Hardware    接口的硬件类型，Fast Ethernet表示快速以太口、Packet Over SONET/SDH表示POS口、Management Ethernet表示以太管理口、Smartgroup表示smartgroup接口。address    接口的物理地址，即MAC地址。只有以太物理接口及其子接口、管理口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口会显示MAC地址，其他接口不会显示。Internet address    接口的IP主地址。如果当前接口没有IP地址，显示”Internet address is unassigned”。如果当前接口的IP地址为借用到的地址，则显示”Ip unnumbered xxx (using ip address:xx.xx.xx.xx/xx)”，其中”xxx”表示借用的接口，”xx.xx.xx.xx/xx”表示借用到的地址，如果没有借用到地址，显示为”0.0.0.0/0”。BW    接口带宽，单位Kbps。如果接口没有带宽，则不显示。IP MTU    接口IP协议最大传输单元，单位bytesMTU    接口二层最大传输单元，单位bytesIPV6 MTU    接口IPv6协议最大传输单元，单位bytes，只有使能的IPv6协议的接口才会显示。MPLS MTU    接口MPLS层最大传输单元，单位bytesHoldtime    接口保持时间，单位秒The port is electric    接口光电属性：electric表示电口，optical表示光口，unknow表示无光电属性。The MDIMode of the port is reserved    以太网接口(仅针对电口)的MDI(Media Dependant Interface)模式，”MDI”表示为平行网线模式、”MDI-X”为交叉网线模式、”auto”表示为自适应模式，”reserved”表示为保留模式。如果该以太网接口不支持MDI模式，则显示” not supported”。Loopback    接口环回方式，”cancel”表示接口无环回设置，”outer”表示接口为外环回，”inner”表示接口为内环回。Duplex    接口双工模式，”full”表示全双工模式，”half”表示半双工模式，”unknown”表示无双工模式。Negotiation    接口协商模式，”auto”表示为自协商模式，“force”表示未强制协商模式，”unknown”表示无协商模式。ARP Timeout    接口动态ARP（Address Resolution Protocol，地址解析协议）的老化时间。Last Clear Time    最近一次敲清除接口计数命令时记录下的系统时间。Last Refresh Time    最近一次项目侧上报接口计数时记录下的系统时间。120s input rate    接口入方向120s平均速率，以Bps和Pps为单位分别统计。Bps    接口120s平均字节速率(单位时间收到的字节数)Pps    接口120s平均包速率(单位时间收到的包数)120s output rate    接口出方向120s平均速率，以Bps和Pps为单位分别统计。Peak rate    接口120s平均速率峰值。input    接口入方向120s平均速率峰值，单位：Bpspeak time    记录接口入方向峰值出现的时间。output    接口出方向120s平均速率峰值，单位：Bpspeak time    记录接口入方向峰值出现的时间。Intfutilization    接口带宽利用率(接口120s平均速率/接口带宽BW值)。input    接口入方向带宽利用率。output    接口出方向带宽利用率。HardWareCounters    接口硬件计数，来源于BSP（Board Support Package，板级支持包）计数。In_Bytes    收到报文总字节数。。In_Packets    收到报文总数。In_CRC_ERROR    收到CRC（Cyclic Redundancy Check，循环冗余校验码）错误报文数。In_Unicasts    收到单播报文数。In_Broadcasts    收到广播报文数。In_Multicasts    收到组播报文数。In_Undersize    收到长度小于64字节的报文数。In_Oversize    收到长度大于Max字节的报文数。In_64B    收到长度为64字节的报文数。In_65_127B    收到长度为65~127字节的报文数。In_128_255B    收到长度为128~255字节的报文数。In_256_511B    收到长度为256~511字节的报文数。In_512_1023B    收到长度为512~1023字节的报文数。In_1024_1518B    收到长度为1024~1518字节的报文数。In_1519_MaxB    收到长度在1519~Max字节的报文数。E_Bytes    发送报文总字节数。E_Packets    发送报文总数。E_CRC_ERROR    发送CRC错误报文数。E_Unicasts    发送单播报文数。E_Broadcasts    发送广播报文数。E_Multicasts    发送组播报文数。E_Undersize    发送长度小于64字节的报文数。E_Oversize    发送长度大于Max字节的报文数。E_64B    发送长度为64字节的报文数。E_65_127B    发送长度为65~127字节的报文数。E_128_255B    发送长度为128~255字节的报文数。E_256_511B    发送长度为256~511字节的报文数。E_512_1023B    发送长度为512~1023字节的报文数。E_1024_1518B    发送长度为1024~1518字节的报文数。E_1519_MaxB    发送长度在1519~Max字节的报文数。StreamCounters    接口流计数，来源于微码芯片计数。In_Bytes    收到的报文总字节数。In_Packets    收到的报文总包数。In_Discards    接收丢包数。In_V4Bytes    接收自定义IPv4业务总字节数。In_V4Pkts    接收自定义IPv4业务总包数。In_V6Bytes    接收自定义IPv6业务总字节数。In_V6Pkts    接收自定义IPv6业务总包数。In_UpsendCar_Drop    接收上送car丢包数。E_Bytes    发送的报文总字节数。E_Packets    发送的报文总包数。E_Discards    发送丢包数。E_V4Bytes    发送自定义IPv4业务总字节数。E_V4Pkts    发送自定义IPv4业务总包数。E_V6Bytes    发送自定义IPv6业务总字节数。E_V6Pkts    发送自定义IPv6业务总包数。
E_UpsendCar_Drop    发送上送car丢包数。显示接口gei-0/1/0/1.1的统计信息。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1”依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#show interface gei-0/1/0/1.1gei-0/1/0/1.1 is down, line protocol is down, detected status is RX-SF/TX-SF  Last line protocol up time :  2014-02-06 14:21:47   Hardware is Fast Ethernet, address is 0019.8407.2300  Internet address is unassigned  BW 100000 Kbps  IP MTU 1500 bytes  MTU 1600 bytes  MPLS MTU 1550 bytes  ARP type ARP  ARP Timeout 04:00:00   Last Clear Time : 2014-02-07 02:45:51  Last Refresh Time: 2014-02-08 06:55:00  120s input rate : 0Bps                 0Pps                 120s output rate: 0Bps                 0Pps                 Peak rate:                                                  input             1Bps                 peak time          2014-02-07 02:46:40  output            1Bps                 peak time          2014-02-07 02:46:40  Intf utilization: input 0%             output 0%            StreamCounters  :                                           In_Bytes          101520               In_Packets         101520  In_Discards       101520               In_UpsendCar_Drop  101520  In_V4Bytes        101520               In_V4Pkts          101520  In_V6Bytes        101520               In_V6Pkts          101520  E_Bytes           101520               E_Packets          101520  E_Discards        101520               E_UpsendCar_Drop   101520  E_V4Bytes         101520               E_V4Pkts           101520  E_V6Bytes         101520               E_V6Pkts           101520输出项名称    输出结果解释gei-0/1/0/1.1    接口名。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1”依次代表机框号、槽位号、子槽位号、接口号和子接口号。is down    接口管理状态和物理状态，如果接口的管理状态down，显示”is administratively down”，接口的管理状态up的情况下，如果物理状态down，显示”is down”，如果物理状态up，显示”is up”。line protocol is down    接口的协议状态，协议状态up，显示”line protocol is up”，协议状态down，显示”line protocol is down”。detected status   接口检测状态。Last line protocol up time   接口最近一次协议状态up时间，如果接口没有up过，显示”-”。Description    接口描述信息，可以通过description命令进行配置，如果接口未配置描述信息，则不显示。Hardware    接口的硬件类型，Fast Ethernet表示快速以太口、Packet Over SONET/SDH表示POS口、Management Ethernet表示以太管理口、Smartgroup表示smartgroup接口。address    接口的物理地址，即MAC地址。只有以太物理接口及其子接口、管理口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口会显示MAC地址，其他接口不会显示。Internet address    接口的IP主地址。如果当前接口没有IP地址，显示”Internet address is unassigned”。如果当前接口的IP地址为借用到的地址，则显示”Ip unnumbered xxx (using ip address:xx.xx.xx.xx/xx)”，其中”xxx”表示借用的接口，”xx.xx.xx.xx/xx”表示借用到的地址，如果没有借用到地址，显示为”0.0.0.0/0”。BW    接口带宽，单位Kbps。如果接口没有带宽，则不显示。IP MTU    接口IP协议最大传输单元，单位bytesMTU    接口二层最大传输单元，单位bytesIPV6 MTU    接口IPv6协议最大传输单元，单位bytes，只有使能的IPv6协议的接口才会显示。MPLS MTU    接口MPLS层最大传输单元，单位bytesARP Timeout    接口动态ARP的老化时间。Last Clear Time    最近一次敲清接口计数命令时记录下的系统时间。Last Refresh Time    最近一次项目侧上报接口计数时记录下的系统时间。120s input rate    接口入方向120s平均速率，以Bps和Pps为单位分别统计。Bps    接口120s平均字节速率(单位时间收到的字节数)Pps    接口120s平均包速率(单位时间收到的包数)120s output rate    接口出方向120s平均速率，以Bps和Pps为单位分别统计。Peak rate    接口120s平均速率峰值。input    接口入方向120s平均速率峰值，单位：Bpspeak time    记录接口入方向峰值出现的时间。output    接口出方向120s平均速率峰值，单位：Bpspeak time    记录接口入方向峰值出现的时间。Intfutilization    接口带宽利用率(接口120s平均速率/接口带宽BW值)。input    接口入方向带宽利用率。output    接口出方向带宽利用率。StreamCounters    接口流计数，来源于微码芯片计数。In_Bytes    收到的报文总字节数。In_Packets    收到的报文总包数。In_Discards    接收丢包数。In_UpsendCar_Drop    接收上送car丢包数。In_V4Bytes    接收自定义IPv4业务总字节数。In_V4Pkts    接收自定义IPv4业务总包数。In_V6Bytes    接收自定义IPv6业务总字节数。In_V6Pkts    接收自定义IPv6业务总包数。E_Bytes    发送的报文总字节数。E_Packets    发送的报文总包数。E_Discards    发送丢包数。E_UpsendCar_Drop    发送上送car丢包数。E_V4Bytes    发送自定义IPv4业务总字节数。E_V4Pkts    发送自定义IPv4业务总包数。E_V6Bytes    发送自定义IPv6业务总字节数。E_V6Pkts    发送自定义IPv6业务总包数。






相关命令 :

无 




## show ip interface brief 


show ip interface brief 




命令功能 :

该命令用于显示接口的IP协议简要信息。接口的IP协议简要信息包括接口主IP地址、掩码、管理状态、物理状态和协议状态。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ip interface brief 
  [{＜interface-name 
＞|phy 
|include 
 ＜regular-expression 
＞|exclude 
 ＜regular-expression 
＞}] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口的IP协议简要信息。可以通过show ip interface brief命令查询当前设备上的接口。取值范围： 配置范围为1-31位的字符串。默认值：无。
phy|和{include|exclude} <WORD>是二选一，若选择phy，则表示显示所有物理接口的IP协议简要信息。
include|和exclude是二选一，若选择include，则表示显示接口名中包含指定字符或字符串的接口的IP协议简要信息，需要和参数<WORD>共同作用。
＜regular-expression＞|正则表达式，显示接口的过滤规则，长度为1~31个字符
exclude|和exclude是二选一，若选择exclude，则表示显示接口名中不包含指定字符或字符串的接口的IP协议简要信息，需要和参数<WORD>共同作用。
＜regular-expression＞|正则表达式，显示接口的过滤规则，长度为1~31个字符








缺省 :

无 






使用说明 :

无 






范例 :

显示所有三层接口的IP协议简要信息。命令如下：ZXROSNG(config)#show ip interface briefInterface                  IP-Address      Mask            Admin Phy  Prot gei-0/1/0/1                unassigned      unassigned      up    down downgei-0/1/0/2                unassigned      unassigned      down  down downpos192-0/1/1/1            unassigned      unassigned      down  down downpos192-0/1/1/1.1          unassigned      unassigned      down  down downpos192-0/1/1/1.2          unassigned      unassigned      down  down downpos192-0/1/1/2            unassigned      unassigned      down  down downmgmt_eth                192.168.5.250   255.255.255.0    up    up   upsmartgroup1              unassigned      unassigned      up    up   downsmartgroup2              unassigned      unassigned      up    up   downte_tunnel1                unassigned      unassigned      up    up   downte_tunnel2                unassigned      unassigned      up    up   down输出项名称    输出结果解释Interface    接口名IP-Address    接口主IP地址，为十进制点分形式：x.x.x.x，如果接口没有IP地址，显示”unassigned”。Mask     接口IP地址掩码，为十进制点分形式：x.x.x.x，如果接口没有IP地址，显示” unassigned”。Admin    接口管理状态，”up”表示接口管理状态up，”down”表示接口管理状态down。Phy    接口物理状态，”up”表示接口物理状态up，”down”表示接口物理状态down。Prot    接口协议状态，”up”表示接口协议状态up，”down”表示接口协议状态down。显示所有物理接口的IP协议简要信息。phy表示指定显示所有物理接口。命令如下：ZXROSNG(config)#show ip interface brief phyInterface                  IP-Address      Mask            Admin Phy  Prot gei-0/1/0/1                unassigned      unassigned      up    down downgei-0/1/0/2                unassigned      unassigned      down  down downpos192-0/1/1/1            unassigned      unassigned      down  down downpos192-0/1/1/2            unassigned      unassigned      down  down downmgmt_eth                192.168.5.250   255.255.255.0    up    up   up显示接口gei-0/1/0/1的IP协议简要信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#show ip interface brief gei-0/1/0/1Interface                  IP-Address      Mask            Admin Phy  Prot gei-0/1/0/1                unassigned      unassigned      up    down down显示接口名中包含字符串”gei”的接口的IP协议简要信息。include gei表示接口名中包含字符串”gei”。命令如下：ZXROSNG(config)#show ip interface brief include geiInterface                  IP-Address      Mask            Admin Phy  Prot gei-0/1/0/1                unassigned      unassigned      up    down downgei-0/1/0/2                unassigned      unassigned      down  down down显示接口名中不包含字符串”gei”的接口的IP协议简要信息。exclude gei表示接口名中不包含字符串”gei”。命令如下：ZXROSNG(config)#show ip interface brief exclude geiInterface                  IP-Address      Mask            Admin Phy  Prot pos192-0/1/1/1            unassigned      unassigned      down  down downpos192-0/1/1/1.1          unassigned      unassigned      down  down downpos192-0/1/1/1.2          unassigned      unassigned      down  down downpos192-0/1/1/2            unassigned      unassigned      down  down downmgmt_eth                192.168.5.250   255.255.255.0    up    up   upsmartgroup1              unassigned      unassigned      up    up   downsmartgroup2              unassigned      unassigned      up    up   downte_tunnel1                unassigned      unassigned      up    up   downte_tunnel2                unassigned      unassigned      up    up   down





相关命令 :

无 




## show ip interface 


show ip interface 




命令功能 :

该命令用于显示接口的IP协议信息。接口的IP协议简要信息包括接口管理状态、物理状态、协议状态、描述信息、VRF绑定关系、IP地址、地址借用关系、地址来源、接口别名、IP协议最大传输单元和MAC地址偏移。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ip interface 
  [＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口的IP协议简要信息。可以通过show ip interface brief命令查询当前设备上的接口。取值范围： 配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令支持显示系统所有接口的IP协议简要信息，同时也支持显示指定接口的IP协议简要信息。上述的接口都是指三层接口。命令指定显示的接口如果不存在，会提示：%Info 85: No such interface(s)命令指定显示的接口必须是三层接口，如果命令指定显示二层接口，会提示：%Info 121139: The interface does not support the configuration





范例 :

显示所有三层接口的IP协议信息。命令如下： ZXROSNG(config)#show ip interfacegei-0/1/0/1 AdminStatus is down, PhyStatus is down, line protocol is down  description is ether1   ip vrf forwarding a   Internet address is 2.2.2.2/24   Broadcast address is 255.255.255.255  Secondary address is 2.2.2.3/24   Address determined by setup command   byname ether1   Load-sharing bandwidth 100000 Kbps  IP MTU 1500 bytes  MAC address offset is 5gei-0/1/0/2 AdminStatus is down, PhyStatus is down, line protocol is down  description is ether2   Address determined by setup command   Load-sharing bandwidth 100000 Kbps  IP MTU 1500 bytespos192-0/1/1/1 AdminStatus is down, PhyStatus is down, line protocol is down  ip vrf forwarding a   IP unnumbered gei-0/1/0/1  (use ip address:2.2.2.2)   Address determined by IP unnumbered   Load-sharing bandwidth 9953280 Kbps  IP MTU 4470 bytespos192-0/1/1/1.1 AdminStatus is down, PhyStatus is down, line protocol is down  Address determined by setup command   Load-sharing bandwidth 9953280 Kbps  IP MTU 4470 bytespos192-0/1/1/1.2 AdminStatus is down, PhyStatus is down, line protocol is down  Address determined by setup command   Load-sharing bandwidth 9953280 Kbps  IP MTU 4470 bytespos192-0/1/1/2 AdminStatus is down, PhyStatus is down, line protocol is down  Address determined by setup command   Load-sharing bandwidth 9953280 Kbps  IP MTU 4470 bytesmgmt_eth AdminStatus is up, PhyStatus is up, line protocol is up  ip vrf forwarding mng   Internet address is 192.168.5.250/24   Broadcast address is 255.255.255.255  Address determined by NVRAM   IP MTU 1500 byteste_tunnel1 AdminStatus is up, PhyStatus is up, line protocol is up  Address determined by setup command   IP MTU 1500 byteste_tunnel2 AdminStatus is up, PhyStatus is up, line protocol is up  Address determined by setup command   IP MTU 1500 bytes输出项名称    输出结果解释gei-0/1/0/1    接口名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。AdminStatus is down    接口管理状态，”is up”表示接口管理状态up，”is down”表示接口管理状态down。PhyStatus is down    接口物理状态，”is up”表示接口物理状态up，”is down”表示接口物理状态down。line protocol is down    接口协议状态，”is up”表示接口协议状态up，”is down”表示接口协议状态down。description is ether1    接口描述信息，可以通过description命令进行配置，如果接口未配置描述信息，则不显示。ip vrf forwarding a    接口的VRF绑定关系，如果接口没有配置VRF绑定关系，则不显示。Internet address is 2.2.2.2/24    接口的主IP地址/掩码。IP地址为十进制点分形式：x.x.x.x，掩码长度为1-32的整数。如果接口没有IP地址，则不显示。Broadcast address is 255.255.255.255    接口的主IP地址/掩码。IP地址为十进制点分形式：x.x.x.x，掩码长度为1-32的整数。如果接口没有IP地址，则不显示。Secondary address is 2.2.2.3/24    接口的辅IP地址/掩码。IP地址为十进制点分形式：x.x.x.x，掩码长度为1-32的整数。如果接口没有辅IP地址，则不显示。如果接口有多条辅IP地址，则显示多条。IP unnumbered gei-0/1/0/1  (use ip address:2.2.2.2)    接口IP地址借用关系和借用到的IP地址。如果接口没有设置IP地址借用关系，则不显示。其中”gei-0/1/0/1”为借用IP地址的接口，括号内的部分为借用到的IP地址，IP地址为十进制点分形式：x.x.x.x。如果没有借用到地址，则不显示该部分内容。Address determined by setup command    IP地址源，接口缺省地址源为命令配置。“setup command”表示IP地址为命令配置的；”IP unnumbered”表示IP地址为地址借用的；”IPCP”表示IP地址为IPCP(IP Control Protocol，IP控制协议)动态分配的；”DHCP”表示IP地址为DHCP(Dynamic Host Configuration Protocol，动态主机配置协议)动态分配的；”GM”表示IP地址为GM(Group Management集群管理)动态分配的；”NVRAM”表示IP地址为保存在NVRAM中，即在系统boot时配置的，只有管理口使用缺省IP地址时，才会出现这种情况。byname ether1    接口别名，如果接口没有配置别名，则不显示。IP MTU 1500 bytes    接口IP协议最大传输单元，单位bytes。MAC address offset is 5    接口MAC地址偏移，如果没有MAC地址偏移，则不显示。显示接口gei-0/1/0/1的IP协议信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#show ip interface gei-0/1/0/1gei-0/1/0/1 AdminStatus is down, PhyStatus is down, line protocol is down, IPv4 protocol is down  description is ether1   ip vrf forwarding a   Internet address is 2.2.2.2/24   Broadcast address is 255.255.255.255  Secondary address is 2.2.2.3/24   Address determined by setup command   byname ether1   Load-sharing bandwidth 100000 Kbps  IP MTU 1500 bytes  MAC address offset is 5





相关命令 :

无 




## show ipv6 interface brief 


show ipv6 interface brief 




命令功能 :

该命令用于显示接口的IPv6协议简要信息。接口的IPv6协议简要信息包括接口是否使能IPv6、IPv6管理状态、IPv6协议状态和IPv6地址。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 interface brief 
  [{＜interface-name 
＞|phy 
|include 
 ＜regular-expression 
＞|exclude 
 ＜regular-expression 
＞}] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口的IPv6协议简要信息。可以通过show ip interface brief命令查询当前设备上的接口。取值范围： 配置范围为1-31位的字符串。默认值：无。
phy|和{include|exclude} <WORD>是二选一，若选择phy，则表示显示所有物理接口的IPv6协议简要信息。
include|和exclude是二选一，若选择include，则表示显示接口名中包含指定字符或字符串的接口的IPv6协议简要信息，需要和参数<WORD>共同作用。
＜regular-expression＞|指定字符或字符串，需要和参数{include|exclude}共同作用，表示显示接口名中包含或不包含指定字符或字符串的接口的IPv6协议简要信息。取值范围：配置范围为1-31位的字符串。默认值：无。
exclude|和exclude是二选一，若选择exclude，则表示显示接口名中不包含指定字符或字符串的接口的IPv6协议简要信息，需要和参数<WORD>共同作用。
＜regular-expression＞|指定字符或字符串，需要和参数{include|exclude}共同作用，表示显示接口名中包含或不包含指定字符或字符串的接口的IPv6协议简要信息。取值范围：配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令支持显示系统所有接口的IPv6协议简要信息，同时也支持显示所有物理接口、指定接口或者接口名中包含或者不包含指定字符串的接口的IPv6协议简要信息。上述的接口都是指支持IPv6协议的三层接口。命令指定显示的接口如果不存在，会提示：%Info 85: No such interface(s)命令指定显示的接口必须是三层接口，如果命令指定显示二层接口，会提示：%Info 121139: The interface does not support the configuration





范例 :

ZXROSNG(config)#show ipv6 interface briefgei-0/1/0/1                             [up/down]    fe80::219:84ff:fe07:2300   [tentative]    1::1/64   [tentative]    1::2/64   [ANY  tentative]    1:1::219:84ff:fe07:2300/64   [EUI  tentative]gei-0/1/0/2                             [down/down]    fe80::219:84ff:fe07:2300   [tentative]pos192-0/1/1/1                          [disable/down]  unassignedpos192-0/1/1/2                          [disable/down]  unassignedmgmt_eth                                [disable/down]  unassignedsmartgroup1                             [disable/down]  unassignedsmartgroup2                             [disable/down]  unassigned输出项名称    输出结果解释gei-0/1/0/1    接口名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。[up/down]    接口是否使能IPv6、IPv6管理状态和IPv6协议状态。“/”前面的部分表示使能IPv6和IPv6管理状态，如果未使能IPv6，则显示”disable”，如果使能IPv6，而IPv6管理状态为down，则显示”down”，如果使能IPv6，而IPv6管理状态为up，则显示”up”。”/”后面的部分表示IPv6协议状态。”up”表示接口IPv6协议状态up，”down” 表示接口IPv6协议状态down。unassigned    接口没有IPv6地址fe80::219:84ff:fe07:2300    接口的IPv6地址ANY    地址类型，ANY表示该IPv6地址为任播泛播地址，EUI表示该IPv6地址为eui64地址tentative    IPv6地址状态，tentative表示该IPv6地址是临时地址，还没完成重复地址检测，duplicated表示该IPv6地址是重复地址，链路上有其它节点采用了该地址。显示gei-0/1/0/1接口的IPv6协议简要信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#show ipv6 interface brief gei-0/1/0/1gei-0/1/0/1                             [up/down]    fe80::219:84ff:fe07:2300   [tentative]    1::1/64   [tentative]    1::2/64   [ANY  tentative]    1:1::219:84ff:fe07:2300/64   [EUI  tentative]显示所有物理接口的IPv6协议简要信息。phy表示指定显示所有物理接口。命令如下：ZXROSNG(config)#show ipv6 interface brief phygei-0/1/0/1                             [up/down]    fe80::219:84ff:fe07:2300   [tentative]    1::1/64   [tentative]    1::2/64   [ANY  tentative]    1:1::219:84ff:fe07:2300/64   [EUI  tentative]gei-0/1/0/2                             [down/down]    fe80::219:84ff:fe07:2300   [tentative]pos192-0/1/1/1                          [disable/down]  unassignedpos192-0/1/1/2                          [disable/down]  unassignedmgmt_eth                                [disable/down]  unassigned显示接口名中包含字符串”gei”的接口的IPv6协议简要信息。include gei表示接口名中包含字符串”gei”命令如下：ZXROSNG(config)#show ipv6 interface brief include geigei-0/1/0/1                             [up/down]    fe80::219:84ff:fe07:2300   [tentative]    1::1/64   [tentative]    1::2/64   [ANY  tentative]    1:1::219:84ff:fe07:2300/64   [EUI  tentative]gei-0/1/0/2                             [down/down]    fe80::219:84ff:fe07:2300   [tentative]显示接口名中不包含字符串”gei”的接口的IPv6协议简要信息。exclude gei表示接口名中不包含字符串”gei”。命令如下：ZXROSNG(config)#show ipv6 interface brief exclude geipos192-0/1/1/1                          [disable/down]  unassignedpos192-0/1/1/2                          [disable/down]  unassignedmgmt_eth                                [disable/down]  unassignedsmartgroup1                             [disable/down]  unassignedsmartgroup2                             [disable/down]  unassigned





相关命令 :

无 




## show ipv6 interface 


show ipv6 interface 




命令功能 :

该命令用于显示接口的IPv6协议信息。接口的IPv6协议信息包括接口的IPv6管理状态、IPv6协议状态、是否使能IPv6、硬件类型、物理地址、接口索引、接口带宽、IPv6协议最大传输单元和IPv6地址。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ipv6 interface 
  [＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口的IPv6协议信息。可以通过show ip interface brief命令查询当前设备上的接口。取值范围： 配置范围为1-31位的字符串。默认值：无。








缺省 :

无 






使用说明 :

该命令支持显示系统所有接口的IPv6协议信息，同时也支持显示指定接口的IPv6协议信息。上述的接口都是指支持IPv6协议的三层接口。命令指定显示的接口如果不存在，会提示：%Info 85: No such interface(s)命令指定显示的接口必须是三层接口，如果命令指定显示二层接口，会提示：%Info 121139: The interface does not support the configuration





范例 :

ZXROSNG(config)#show ipv6 interfaceInterface gei-0/1/0/1 is up, line protocol is down  IPv6 is enabled, Hardware is Fast Ethernet  Hardware address is 0019.8407.2300  Index 11   Bandwidth 100000 Kbps  IPv6 MTU 1500 bytes  inet6 fe80::219:84ff:fe07:2300/10   [tentative]  inet6 1::1/64   [tentative]  inet6 1::2/64   [ANY  tentative]  inet6 1:1::219:84ff:fe07:2300/64   [EUI  tentative]Interface gei-0/1/0/2 is down, line protocol is down  IPv6 is enabled, Hardware is Fast Ethernet  Hardware address is 0019.8407.2300  Index 12   Bandwidth 100000 Kbps  IPv6 MTU 1500 bytes  inet6 fe80::219:84ff:fe07:2300/10   [tentative]Interface pos192-0/1/1/1 is down, line protocol is down  IPv6 is disabled, Hardware is Packet Over SONET/SDH  Index 147   Bandwidth 9953280 Kbps  IPv6 address is unassignedInterface pos192-0/1/1/2 is down, line protocol is down  IPv6 is disabled, Hardware is Packet Over SONET/SDH  Index 148   Bandwidth 9953280 Kbps  IPv6 address is unassignedInterface mgmt_eth is up, line protocol is up  IPv6 is disabled, Hardware is Management Ethernet  Hardware address is 0019.8407.2300  Index 2   Bandwidth 1000000 Kbps  IPv6 address is unassignedInterface smartgroup1 is up, line protocol is down  IPv6 is disabled, Hardware is Smartgroup  Hardware address is 0019.8407.2300  Index 145   IPv6 address is unassignedInterface smartgroup2 is up, line protocol is down  IPv6 is disabled, Hardware is Smartgroup  Hardware address is 0019.8407.2300  Index 146   IPv6 address is unassigned输出项名称    输出结果解释gei-0/1/0/1    接口名。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。is up    接口的IPv6管理状态。”is up”表示接口的IPv6管理状态up，”is down”表示接口的IPv6管理状态down。line protocol is down    接口的IPv6协议状态。”is up”表示接口的IPv6协议状态up，”is down”表示接口的IPv6协议状态down。IPv6 is enabled    接口是否使能IPv6，”enabled”表示使能IPv6，”disables”表示未使能IPv6。Hardware    接口的硬件类型，Fast Ethernet表示快速以太口、Packet Over SONET/SDH表示POS口、Management Ethernet表示以太管理口、Smartgroup表示smartgroup接口。Hardware address    接口的物理地址，即MAC地址。只有以太物理接口及其子接口、管理口、smartgroup接口、supervlan接口、ulei接口、vlan接口、eth_dslgroup接口和dsl接口会显示MAC地址，其他接口不会显示。Index    接口索引Bandwidth    接口带宽，单位Kbps。IPv6 MTU    接口IPv6协议最大传输单元，单位bytes。inet6    接口IPv6地址。如果接口当前没有IPv6地址，则显示” IPv6 address is unassigned”ANY    地址类型，ANY表示该IPv6地址为任播泛播地址，EUI表示该IPv6地址为eui64地址tentative    IPv6地址状态，tentative表示该IPv6地址是临时地址，还没完成重复地址检测，duplicated表示该IPv6地址是重复地址，链路上有其它节点采用了该地址。显示gei-0/1/0/1接口的IPv6协议信息。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#show ipv6 interface gei-0/1/0/1Interface gei-0/1/0/1 is up, line protocol is down  IPv6 is enabled, Hardware is Fast Ethernet  Hardware address is 0019.8407.2300  Index 11   Bandwidth 100000 Kbps  IPv6 MTU 1500 bytes  inet6 fe80::219:84ff:fe07:2300/10   [tentative]  inet6 1::1/64   [tentative]  inet6 1::2/64   [ANY  tentative]  inet6 1:1::219:84ff:fe07:2300/64   [EUI  tentative]





相关命令 :

无 




## show logicinterface summary 


show logicinterface summary 




命令功能 :

该命令用于显示当前系统逻辑接口计数。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show logicinterface summary 
  [port 
 ＜parent-interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜parent-interface-name＞|接口名，用于唯一标识一个接口，指定命令显示该接口的子接口计数。可以通过show ip interfacebrief命令查询当前设备上的接口。当没有输入可选参数port <interface-name>，表示命令显示当前系统所有逻辑接口的计数，当输入可选参数port <interface-name>，表示命令显示指定接口的子接口计数。取值范围：配置范围为1-31位的字符串默认值：无








缺省 :

无 






使用说明 :

该命令支持显示系统所有逻辑接口计数，同时也支持显示指定接口的子接口计数。指定显示某接口的子接口计数时，如果当前接口不存在，会提示：%Info 85: No such interface(s)指定显示某接口的子接口计数时，如果当前接口没有子接口，会提示：%Info 121140: The interface does not have sub-interface(s)





范例 :

显示当前系统所有逻辑接口计数：ZXROSNG(config)#show logicinterface summary Logic-interface       Usedgei-0/1/0/1.*          3pos192-0/1/1/1.*      2null*                 1smartgroup*          2smartgroup1.*        3te_tunnel*            2subvlan*             1输出项名称    输出结果解释Logic-interface    逻辑接口名称Used    已使用个数gei-0/1/0/1.*    gei-0/1/0/1接口的所有子接口计数pos192-0/1/1/1.*    pos192-0/1/1/1接口的所有子接口计数null*    null接口计数，null接口为设备上电自动生成的接口，用于产生空洞路由，即不能转发数据包，也不能配置IP地址或配置其它链路层协议，任何送到该接口的网络数据报文都会被丢弃。smartgroup*    smartgroup接口计数smartgroup1.*    smartgroup1接口的所有子接口计数te_tunnel*    te_tunnel接口计数subvlan*    subvlan接口计数显示smartgroup1接口所有子接口的计数。smartgroup1为逻辑接口，没有具体的物理位置，smartgroup表示接口类型，1表示接口号。命令如下：ZXROSNG(config)#show logicinterface summary port smartgroup1Logic-interface       Usedsmartgroup1.*         3输出项名称    输出结果解释Logic-interface    逻辑接口名称Used    已使用个数smartgroup1.*    smartgroup1接口的所有子接口计数





相关命令 :

无 




## show pw 


show pw 




命令功能 :

命令用于显示当前系统的伪线。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pw 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

通过pw命令创建伪线后，可以通过本命令查询当前系统所有的伪线。 






范例 :

ZXROSNG(config)#show pwTotal number is 5.  pw1  pw2  pw3  pw4  pw5输出项名称    输出结果解释Total number    当前系统的伪线总数pw1    伪线名





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 dialer接口模式,virtual_template子接口模式,virtual_template接口模式  






命令默认权限级别 :

virtual_template子接口模式:15,virtual_template接口模式:15,dialer接口模式:15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。





命令模式 :

 bvi子接口模式,bvi接口模式  






命令默认权限级别 :

bvi子接口模式:15,bvi接口模式:15 






命令格式 :


shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。






范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown






相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。





命令模式 :

 qx子接口模式,qx接口模式  






命令默认权限级别 :

qx接口模式:15,qx子接口模式:15 






命令格式 :


shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。






范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown






相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 IPsec接口模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 ATM子接口模式,ATM接口模式,atm_dslgroup接口模式,dsl接口模式,e1接口模式,eth_dslgroup子接口模式,eth_dslgroup接口模式,mte隧道接口模式,oh_tt接口模式,posgroup接口模式,pos子接口模式,serial接口模式,ulei子接口模式,ulei接口模式,vbui子接口模式  






命令默认权限级别 :

posgroup接口模式:15,mte隧道接口模式:15,atm_dslgroup接口模式:15,serial接口模式:15,dsl接口模式:15,eth_dslgroup接口模式:15,oh_tt接口模式:15,eth_dslgroup子接口模式:15,e1接口模式:15,ulei子接口模式:15,vbui子接口模式:15,pos子接口模式:15,ulei接口模式:15,ATM子接口模式:15,ATM接口模式:15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 multilink接口模式,pos接口模式,通道化cpos_cep接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_cep接口模式:15,通道化cpos_e1接口模式:15,multilink接口模式:15,pos接口模式:15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 以太子接口模式,千兆以太接口模式  






命令默认权限级别 :

千兆以太接口模式:15,以太子接口模式:15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 IPv6隧道接口模式,supervlan接口模式,te隧道接口模式  






命令默认权限级别 :

IPv6隧道接口模式:15,te隧道接口模式:15,supervlan接口模式:15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 vbui接口模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 10G以太接口模式,loopback接口模式,smartgroup子接口模式,以太接口模式  






命令默认权限级别 :

loopback接口模式:15,10G以太接口模式:15,smartgroup子接口模式:15,以太接口模式:15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 smartgroup接口模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 cip接口模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 通道化ce1接口模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。






范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown






相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。





命令模式 :

 smartgroup接口批处理模式  






命令默认权限级别 :

15 






命令格式 :


shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。






范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown






相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 三层VLAN接口模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown





相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 celluar接口模式,qx_eth接口模式  






命令默认权限级别 :

qx_eth接口模式:15,celluar接口模式:15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。






范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown






相关命令 :

无 




shutdown :

shutdown 




命令功能 :

该命令工作于接口配置模式下，用于关闭接口，no shutdown命令用于启动接口。当接口处于关闭的状态下，所有接口功能都不能启用。 






命令模式 :

 以太接口批处理模式  






命令默认权限级别 :

15 






命令格式 :



shutdown 
 

no shutdown 








命令参数解释 :


					无
				 






缺省 :

物理口缺省关闭，子接口缺省打开，逻辑接口缺省打开。 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。关闭接口即接口的管理状态down，启动接口即接口的管理状态up。父接口的管理状态会关联到子接口，如果父接口的管理状态为down，无论子接口是开启还是关闭，其管理状态都是down的。而当父接口的管理状态为up，只有当子接口开启了，管理状态才能up。物理接口缺省关闭，子接口和逻辑接口缺省打开。配置成功后，可以通过show interface、show interface brief、show interface description、show ip interface brief、show ip interface等命令查看接口的管理状态。





范例 :

关闭gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#shutdown开启gei-0/1/0/1接口。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no shutdown






相关命令 :

无 




## smartgroup-interface-range 


smartgroup-interface-range 




命令功能 :

进入smartgroup接口批量配置模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



smartgroup-interface-range 
  ＜port-list 
＞







命令参数解释 :



参数|描述
---|---
＜port-list＞|smartgroup接口范围








缺省 :

无 






使用说明 :

进入smartgroup接口批量配置模式，用于批量配置smartgroup接口。 






范例 :

ZXROSNG(config)#ethernet-interface-range smartgroup1-3ZXROSNG(config–smartgroup-if-range)#






相关命令 :

无 




## switch attribute 


switch attribute 




命令功能 :

该命令工作于接口配置模式下，用于使能或去使能接口的二层属性。使能接口的二层属性，则将接口作为一个二层以太网接口使用，去使能接口的二层属性，则将接口作为一个三层以太网接口使用。






命令模式 :

 10G以太接口模式,smartgroup接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,以太接口模式:15,千兆以太接口模式:15,smartgroup接口模式:15 






命令格式 :


switch attribute 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|与disable为二选一，选择enable表示使能接口的二层属性，即将接口切换成二层接口。
disable|与enable为二选一，选择disable表示去使能接口的二层属性，即将接口切换成三层接口。








缺省 :

路由器以太接口、smartgroup接口、ulei接口缺省为三层属性 






使用说明 :

1.该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。2.二层接口可以通过show interface brief命令进行查看，三层接口可以通过show ip interface brief和show ip interface命令进行查看。3.以太接口、ULEI接口和smartgroup接口支持配置接口的二三层属性。4.路由器上的接口缺省都是三层接口。5.如果将二层接口切换成三层接口，会关联删除接口三层协议相关的配置。如果将三层接口切换成二层接口，会关联删除接口的二层协议相关的配置。所以在配置接口的二三层属性时，会通过交互式的询问方式向用户确定是否进行切换。提示如下：Would you change the L2/L3 attribute of the interface?[yes/no]:有些配置在二三层属性切换时不会直接关联删除，而需要用户手动进行删除，会在用户确定进行切换后，做出提示，根据配置的不同，提示信息也会有所不同。例如：当前接口配置了IP地址，而此时要将接口切换成二层接口，会提示：%Error 121174: Cannot do this operation, please remove IP address configuration first或者，当前接口配置了VRF绑定，而测试样将接口切换成二层接口，会提示：%Error 121176: Cannot do this operation, please remove IP VRF configuration first





范例 :

使能gei-0/1/0/1接口的二层属性。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# switch attribute enableWould you change the L2/L3 attribute of the interface?[yes/no]:yes去使能gei-0/1/0/1接口的二层属性。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# switch attribute disableWould you change the L2/L3 attribute of the interface?[yes/no]:yes





相关命令 :

无 




## switch attribute 


switch attribute 




命令功能 :

该命令工作于接口配置模式下，用于使能或去使能接口的二层属性。使能接口的二层属性，则将接口作为一个二层以太网接口使用，去使能接口的二层属性，则将接口作为一个三层以太网接口使用。






命令模式 :

 ulei接口模式  






命令默认权限级别 :

15 






命令格式 :


switch attribute 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|与disable为二选一，选择enable表示使能接口的二层属性，即将接口切换成二层接口。
disable|与enable为二选一，选择disable表示去使能接口的二层属性，即将接口切换成三层接口。








缺省 :

路由器以太接口、smartgroup接口、ulei接口缺省为三层属性 






使用说明 :

1.该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。2.二层接口可以通过show interface brief命令进行查看，三层接口可以通过show ip interface brief和show ip interface命令进行查看。3.以太接口、ULEI接口和smartgroup接口支持配置接口的二三层属性。4.路由器上的接口缺省都是三层接口。5.如果将二层接口切换成三层接口，会关联删除接口三层协议相关的配置。如果将三层接口切换成二层接口，会关联删除接口的二层协议相关的配置。所以在配置接口的二三层属性时，会通过交互式的询问方式向用户确定是否进行切换。提示如下：Would you change the L2/L3 attribute of the interface?[yes/no]:有些配置在二三层属性切换时不会直接关联删除，而需要用户手动进行删除，会在用户确定进行切换后，做出提示，根据配置的不同，提示信息也会有所不同。例如：当前接口配置了IP地址，而此时要将接口切换成二层接口，会提示：%Error 121174: Cannot do this operation, please remove IP address configuration first或者，当前接口配置了VRF绑定，而测试样将接口切换成二层接口，会提示：%Error 121176: Cannot do this operation, please remove IP VRF configuration first






范例 :

使能gei-0/1/0/1接口的二层属性。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# switch attribute enableWould you change the L2/L3 attribute of the interface?[yes/no]:yes
去使能gei-0/1/0/1接口的二层属性。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# switch attribute disableWould you change the L2/L3 attribute of the interface?[yes/no]:yes






相关命令 :

无 




## switch attribute 


switch attribute 




命令功能 :

该命令工作于接口配置模式下，用于使能或去使能接口的二层属性。使能接口的二层属性，则将接口作为一个二层以太网接口使用，去使能接口的二层属性，则将接口作为一个三层以太网接口使用。






命令模式 :

 bvi接口模式  






命令默认权限级别 :

15 






命令格式 :


switch attribute 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|与disable为二选一，选择enable表示使能接口的二层属性，即将接口切换成二层接口。
disable|与enable为二选一，选择disable表示去使能接口的二层属性，即将接口切换成三层接口。








缺省 :

路由器以太接口、smartgroup接口、ulei接口缺省为三层属性 






使用说明 :

1.该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。2.二层接口可以通过show interface brief命令进行查看，三层接口可以通过show ip interface brief和show ip interface命令进行查看。3.以太接口、ULEI接口和smartgroup接口支持配置接口的二三层属性。4.路由器上的接口缺省都是三层接口。5.如果将二层接口切换成三层接口，会关联删除接口三层协议相关的配置。如果将三层接口切换成二层接口，会关联删除接口的二层协议相关的配置。所以在配置接口的二三层属性时，会通过交互式的询问方式向用户确定是否进行切换。提示如下：Would you change the L2/L3 attribute of the interface?[yes/no]:有些配置在二三层属性切换时不会直接关联删除，而需要用户手动进行删除，会在用户确定进行切换后，做出提示，根据配置的不同，提示信息也会有所不同。例如：当前接口配置了IP地址，而此时要将接口切换成二层接口，会提示：%Error 121174: Cannot do this operation, please remove IP address configuration first或者，当前接口配置了VRF绑定，而测试样将接口切换成二层接口，会提示：%Error 121176: Cannot do this operation, please remove IP VRF configuration first





范例 :

使能gei-0/1/0/1接口的二层属性。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# switch attribute enableWould you change the L2/L3 attribute of the interface?[yes/no]:yes
去使能gei-0/1/0/1接口的二层属性。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)# switch attribute disableWould you change the L2/L3 attribute of the interface?[yes/no]:yes






相关命令 :

无 




## track trigger 


track trigger 




命令功能 :

配置检测关联关闭或阻塞接口对象。 






命令模式 :

 ATM接口模式,pos接口模式  






命令默认权限级别 :

ATM接口模式:15,pos接口模式:15 






命令格式 :



track trigger 
  [group 
] ＜track-name 
＞ {block 
|shutdown 
 [period 
 ＜10-600 
＞]}

no track trigger 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为track组
＜track-name＞|track对象名称，长度为1~31个字符
block|阻塞端口
shutdown|关闭端口
＜10-600＞|track trigger配置值








缺省 :

无 






使用说明 :

无 






范例 :

配置接口gei-0/1/0/1名称为"zte"的track对象关闭端口：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track trigger zte shutdownZXROSNG(config-if-gei-0/1/0/1)#no track trigger 配置接口gei-0/1/0/1名称为"zte"的track组对象阻塞端口：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track trigger zte group blockZXROSNG(config-if-gei-0/1/0/1)#no track trigger






相关命令 :

samgr 




## track trigger 


track trigger 




命令功能 :

配置检测关联关闭或阻塞接口对象。 






命令模式 :

 ATM子接口模式,ATM接口模式,pos子接口模式,pos接口模式,ulei子接口模式,ulei接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

pos接口模式:15,ulei子接口模式:15,通道化cpos_e1接口模式:15,pos子接口模式:15,ulei接口模式:15,ATM子接口模式:15,通道化ce1接口模式:15,ATM接口模式:15 






命令格式 :



track trigger 
  [group 
] ＜track-name 
＞ {block 
|shutdown 
}

no track trigger 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为track组
＜track-name＞|track对象名称，长度为1~31个字符
block|阻塞端口
shutdown|关闭端口








缺省 :

无 






使用说明 :

无 






范例 :

配置接口gei-0/1/0/1名称为"zte"的track对象关闭端口：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track trigger zte shutdownZXROSNG(config-if-gei-0/1/0/1)#no track trigger 配置接口gei-0/1/0/1名称为"zte"的track组对象阻塞端口：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track trigger zte group blockZXROSNG(config-if-gei-0/1/0/1)#no track trigger






相关命令 :

samgr 




## track trigger 


track trigger 




命令功能 :

配置检测关联关闭或阻塞接口对象。 






命令模式 :

 10G以太接口模式,以太子接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

以太子接口模式:15,千兆以太接口模式:15,以太接口模式:15,10G以太接口模式:15 






命令格式 :



track trigger 
  [group 
] ＜track-name 
＞ {block 
|shutdown 
}

no track trigger 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为track组
＜track-name＞|track对象名称，长度为1~31个字符
block|阻塞端口
shutdown|关闭端口








缺省 :

无 






使用说明 :

无 






范例 :

配置接口gei-0/1/0/1名称为"zte"的track对象关闭端口：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track trigger zte shutdownZXROSNG(config-if-gei-0/1/0/1)#no track trigger 配置接口gei-0/1/0/1名称为"zte"的track组对象阻塞端口：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track trigger zte group blockZXROSNG(config-if-gei-0/1/0/1)#no track trigger






相关命令 :

samgr 




track :

track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层协议关联检测对象。no track命令用于删除接口二层协议与检测对象的关联关系。 






命令模式 :

 ATM子接口模式,ATM接口模式,dsl接口模式,pos子接口模式,serial接口模式,ulei子接口模式,ulei接口模式  






命令默认权限级别 :

serial接口模式:15,dsl接口模式:15,ulei子接口模式:15,pos子接口模式:15,ulei接口模式:15,ATM子接口模式:15,ATM接口模式:15 






命令格式 :



track 
  [group 
] ＜track-name 
＞

no track 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为检测组。选择group表示配置的检测对象为检测组，不选择group表示配置的检测对象不是检测组。
＜track-name＞|二层协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口二层协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个二层协议关联检测对象，且不允许直接修改配置。接口已经配置了二层协议关联检测对象的情况下，如果需要配置其他的二层协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的二层协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。zte为检查对象名。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track zte配置gei-0/1/0/2接口的二层协议关联检测组对象rosng。gei-0/1/0/2表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/2”依次代表机框号、槽位号、子槽位号和接口号。rosng为检测组对象名。group表示为检测组对象。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#track rosng group删除gei-0/1/0/1接口的二层协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no track





相关命令 :

samgr 




track :

track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层协议关联检测对象。no track命令用于删除接口二层协议与检测对象的关联关系。 






命令模式 :

 10G以太接口模式,以太接口模式,千兆以太接口模式  






命令默认权限级别 :

10G以太接口模式:15,千兆以太接口模式:15,以太接口模式:15 






命令格式 :



track 
  [group 
] ＜track-name 
＞

no track 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为检测组。选择group表示配置的检测对象为检测组，不选择group表示配置的检测对象不是检测组。
＜track-name＞|二层协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口二层协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个二层协议关联检测对象，且不允许直接修改配置。接口已经配置了二层协议关联检测对象的情况下，如果需要配置其他的二层协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的二层协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。zte为检查对象名。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track zte配置gei-0/1/0/2接口的二层协议关联检测组对象rosng。gei-0/1/0/2表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/2”依次代表机框号、槽位号、子槽位号和接口号。rosng为检测组对象名。group表示为检测组对象。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#track rosng group删除gei-0/1/0/1接口的二层协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no track





相关命令 :

samgr 




track :

track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层协议关联检测对象。no track命令用于删除接口二层协议与检测对象的关联关系。 






命令模式 :

 通道化cpos_e1子接口模式  






命令默认权限级别 :

15 






命令格式 :



track 
  [group 
] ＜track-name 
＞

no track 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为检测组。选择group表示配置的检测对象为检测组，不选择group表示配置的检测对象不是检测组。
＜track-name＞|二层协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口二层协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个二层协议关联检测对象，且不允许直接修改配置。接口已经配置了二层协议关联检测对象的情况下，如果需要配置其他的二层协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group






范例 :

配置gei-0/1/0/1接口的二层协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。zte为检查对象名。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track zte配置gei-0/1/0/2接口的二层协议关联检测组对象rosng。gei-0/1/0/2表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/2”依次代表机框号、槽位号、子槽位号和接口号。rosng为检测组对象名。group表示为检测组对象。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#track rosng group删除gei-0/1/0/1接口的二层协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no track






相关命令 :

samgr 




track :

track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层协议关联检测对象。no track命令用于删除接口二层协议与检测对象的关联关系。 






命令模式 :

 pos接口模式,通道化ce1接口模式,通道化cpos_e1接口模式  






命令默认权限级别 :

通道化cpos_e1接口模式:15,通道化ce1接口模式:15,pos接口模式:15 






命令格式 :



track 
  [group 
] ＜track-name 
＞

no track 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为检测组。选择group表示配置的检测对象为检测组，不选择group表示配置的检测对象不是检测组。
＜track-name＞|二层协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口二层协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个二层协议关联检测对象，且不允许直接修改配置。接口已经配置了二层协议关联检测对象的情况下，如果需要配置其他的二层协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的二层协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。zte为检查对象名。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track zte配置gei-0/1/0/2接口的二层协议关联检测组对象rosng。gei-0/1/0/2表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/2”依次代表机框号、槽位号、子槽位号和接口号。rosng为检测组对象名。group表示为检测组对象。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#track rosng group删除gei-0/1/0/1接口的二层协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no track





相关命令 :

samgr 




track :

track 




命令功能 :

该命令工作于接口配置模式下，用于设置接口二层协议关联检测对象。no track命令用于删除接口二层协议与检测对象的关联关系。 






命令模式 :

 以太子接口模式  






命令默认权限级别 :

15 






命令格式 :



track 
  [group 
] ＜track-name 
＞

no track 








命令参数解释 :



参数|描述
---|---
group|可选参数，标识是否为检测组。选择group表示配置的检测对象为检测组，不选择group表示配置的检测对象不是检测组。
＜track-name＞|二层协议关联检测对象名称。可以通过show samgr brief命令查询当前设备所有的检测对象。取值范围：配置范围为1-31位的字符串。








缺省 :

无 






使用说明 :

该命令工作于接口配置模式下，需要先进入接口配置模式，才能使用。ATM接口及其子接口、以太接口及其子接口、POS接口及其子接口、通道化接口、dsl接口、serial接口、ULEI接口及其子接口、smartgroup接口及其子接口、virtual_template接口及其子接口、supervlan接口、VLAN接口、multilink接口、posgroup接口、loopback接口、v6_tunnel接口、gre_tunnel接口、te_tunnel接口和ipsec_tunnel接口支持接口二层协议关联检测对象的配置。在缺省情况下，接口没有IPv4协议关联检测对象。同一个接口仅允许配置一个二层协议关联检测对象，且不允许直接修改配置。接口已经配置了二层协议关联检测对象的情况下，如果需要配置其他的二层协议关联检测对象，需要先删除当前关联的检测对象，再重新配置。如果直接配置其他的检测对象，会提示：%Error 121130: The interface has configured track or track-group





范例 :

配置gei-0/1/0/1接口的二层协议关联检测对象zte。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。zte为检查对象名。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#track zte配置gei-0/1/0/2接口的二层协议关联检测组对象rosng。gei-0/1/0/2表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/2”依次代表机框号、槽位号、子槽位号和接口号。rosng为检测组对象名。group表示为检测组对象。命令如下：ZXROSNG(config)#interface gei-0/1/0/2ZXROSNG(config-if-gei-0/1/0/2)#track rosng group删除gei-0/1/0/1接口的二层协议关联检测对象。gei-0/1/0/1表示设备上的物理接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1”依次代表机框号、槽位号、子槽位号和接口号。命令如下：ZXROSNG(config)#interface gei-0/1/0/1ZXROSNG(config-if-gei-0/1/0/1)#no track





相关命令 :

samgr 




## vlan-limit 


vlan-limit 




命令功能 :

该命令工作于控制面安全子接口配置模式下，用于设置子接口基于VLAN的控制面安全参数，no vlan-limit命令用于删除子接口基于VLAN的控制面安全缺省配置。和port-limit命令的作用类似，该命令通过设置子接口的控制面安全参数，防止路由器受到攻击，确保路由器稳定工作，区别在于port-limit命令针对子接口，而本命令则是针对VLAN用户，用于防止针对接入VLAN的报文攻击。





命令模式 :

 CPS子接口模式  






命令默认权限级别 :

15 






命令格式 :


vlan-limit 
  {high 
 cir 
 ＜0-200000 
＞ [{pps 
|kpps 
}] cbs 
 {＜16-20000 
＞ [{kb 
|mb 
}]|default 
}|low 
 cir 
 ＜0-200000 
＞ [{pps 
|kpps 
}] cbs 
 {＜16-20000 
＞ [{kb 
|mb 
}]|default 
}}
no vlan-limit 
  {high 
 cir 
 cbs 
|low 
 cir 
 cbs 
}
				






命令参数解释 :



参数|描述
---|---
＜0-200000＞|承诺信息速率，令牌桶放置令牌的速率。单位：pps(包/秒)取值范围：0-200000默认值：无
pps|单位：Packets per second
kpps|单位：Kilopackets per second
＜16-20000＞|和default为二选一，承诺突发尺寸，令牌桶的容量。单位：KB取值范围：16-20000默认值：无
kb|单位：Kilobyte
mb|单位：Megabyte
default|和16-20000为二选一，承诺突发尺寸，令牌桶的容量。选择default表示根据子卡类型进行适配。






No参数|描述
---|---
cir|约定信息速率
cbs|约定突发流量








缺省 :

高桶cir缺省值为255，低桶cir缺省值为745，高桶、低桶cbs缺省值都是0





使用说明 :

该命令工作于控制面安全子接口配置模式下，需要先进入控制面安全子接口配置模式，才能使用。配置成功后，可以通过show cps vlan-limit命令查看子接口生效的基于VLAN的控制面安全属性。子接口基于VLAN的控制面安全没有缺省配置，当没有配置或者删除配置时，则表示没有基于VLAN的控制面安全限制。物理子接口、ULEI子接口、smartgroup子接口支持子接口的控制面安全参数配置。





范例 :

配置gei-0/1/0/1.1接口基于VLAN的高桶CIR为4000pps、CBS为200KB。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1”依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1.1ZXROSNG(config-cps-if-gei-0/1/0/1.1)#vlan-limit high cir 4000 cbs 200配置gei-0/1/0/1.1接口基于VLAN的低桶CIR为2000pps、CBS为100KB。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1”依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1.1ZXROSNG(config-cps-if-gei-0/1/0/1.1)#vlan-limit low cir 2000 cbs 100删除gei-0/1/0/1.1接口缺省基于VLAN的高桶CIR和CBS配置。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1”依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1.1ZXROSNG(config-cps-if-gei-0/1/0/1.1)#no vlan-limit high cir cbs删除gei-0/1/0/1.1接口缺省基于VLAN的低桶CIR和CBS配置。gei-0/1/0/1.1为设备物理接口gei-0/1/0/1的子接口，其中”gei-”表示接口类型为百兆以太接口，”0/1/0/1.1”依次代表机框号、槽位号、子槽位号、接口号和子接口号。命令如下：ZXROSNG(config)#control-plane-securityZXROSNG(config-cps)#interface gei-0/1/0/1.1ZXROSNG(config-cps-if-gei-0/1/0/1.1)#no vlan-limit low cir cbs





相关命令 :

show cps vlan-limit



# 接口性能统计配置命令 
## alarm-threshold 


alarm-threshold 




命令功能 :

该命令工作于接口性能统计配置模式下，用于开启或关闭当前设备所有支持且无门限配置接口的带宽利用率及错误包率告警功能。打开时，所有无门限配置接口根据性能参数进行告警逻辑判断，此时协议实体高门限的生效值为性能参数值；关闭后，所有无门限配置接口不再根据性能参数进行告警逻辑判断，此时协议实体高门限的生效值为100。 






命令模式 :

 接口性能统计模式  






命令默认权限级别 :

15 






命令格式 :



alarm-threshold 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|<作用> 开关开启，高门限值为性能参数值，系统根据性能参数值判断是否需要告警
disable|<作用>开关关闭，高门限值为100，此时不产生高门限告警








缺省 :

开关默认开启 






使用说明 :

无 






范例 :

开启所有支持接口的告警门限功能。 命令如下：ZXROSNG(config-intf-statistics)# alarm-thresholdenable关闭所有支持接口的告警门限功能。 命令如下：ZXROSNG(config-intf-statistics)# alarm-thresholddisable





相关命令 :

无 




## clear statistics interface 


clear statistics interface 




命令功能 :

该命令工作于特权模式下，用于清除系统缓存的接口流量统计累加值。需要查看从当前时刻开始接口的流量统计值时，可以使用该命令将之前缓存的接口流量统计值清零，接口流量重新从0开始统计。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear statistics interface 
  [＜interface-name 
＞]







命令参数解释 :



参数|描述
---|---
＜interface-name＞|<作用> 用于唯一标识一个接口，可以使用show ip in brief查询到当前设备上的接口<取值范围> 配置范围为1-32位的字符串若不输入接口名时，表示批量清除设备上所有支持流量统计功能的接口统计值<默认值> 无








缺省 :

无 






使用说明 :

使用该命令后，可以通过show interface查看接口下计数信息是否清零。每次在设备上使用该命令，都会记录下当前的系统时间，然后通过show interdace命令中的Last Clear Time可以查看到最后一次执行该命令时的系统时间。 






范例 :

清除fei-0/1/0/1的接口性能统计数据ZXROSNG#clear statistics interface fei-0/1/0/1 






相关命令 :

无 




interface :

interface (接口性能统计模式) 




命令功能 :

该命令用于进入接口性能统计接口配置模式。当需要对接口流量统计功能进行控制，如进行一分钟流量统计峰值功能、流量告警阈值配置、流量统计开关配置等相关配置时，必须先使用该命令进入接口性能统计配置模式。 






命令模式 :

 接口性能统计模式  






命令默认权限级别 :

15 






命令格式 :



interface 
  ＜interface-name 
＞







命令参数解释 :



参数|描述
---|---
＜interface-name＞|<作用> 用于唯一标识一个接口，可以使用show ip in brief查询到当前设备上的接口<取值范围> 配置范围为1-32位的字符串<默认值> 无








缺省 :

无 






使用说明 :

该命令工作于接口性能统计配置模式下，需要先进入接口性能统计配置模式，才能使用该命令。根据参数“接口名”来确定进入具体的接口性能统计配置模式。





范例 :

进入fei-0/1/0/1接口的接口性能统计接口配置模式ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1)#






相关命令 :

无 




## intf-statistics threshold 


intf-statistics threshold 




命令功能 :

该命令工作于接口性能统计物理接口配置模式下和接口性能统计物理子接口配置模式下。用于配置指定接口下指定计数器流量告警阈值。阈值分为高门限阈值和低门限阈值。当性能值超过所配置的告警阈值时就会产生越限告警。在高/低门限阈值范围内的则上报告警恢复。使用该命令后，可以实时监控接口上的流量变化。支持 no命令，执行no命令时恢复缺省门限配置。






命令模式 :

 接口性能统计pos接口模式,接口性能统计以太接口模式  






命令默认权限级别 :

接口性能统计pos接口模式:15,接口性能统计以太接口模式:15 






命令格式 :


intf-statistics threshold 
  {{input-utilization 
|output-utilization 
|input-fcsratio 
} low 
 ＜0-99 
＞ high 
 ＜1-100 
＞|input-fcserrors 
 low 
 ＜0-4294967294 
＞ high 
 ＜1-4294967295 
＞}
no intf-statistics threshold 
  [{input-utilization 
|output-utilization 
|input-fcserrors 
|input-fcsratio 
}]
				






命令参数解释 :



参数|描述
---|---
input-utilization|<作用> 接口入方向的带宽利用率，表示在120s内当前接口收到的实际流量速率和接口总速率的比值
output-utilization|<作用> 接口出方向的带宽利用率，表示120s内当前接口发送的实际流量速率和接口总速率的比值
input-fcsratio|<作用> 接口入方向的fcs错包率，表示在120s内当前接口收到的fcs错误包与接口收到的总包数的比值
＜0-99＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的低门限配置范围<取值范围> 输入值必须是在这个范围的整型数
＜1-100＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的高门限配置范围<取值范围> 输入值必须是在这个范围的整型数
input-fcserrors|<作用> 接口入方向的fcs错包数，表示10s内接口收到的fcs错误包数
＜0-4294967294＞|<作用>  告警类型input-fcserrors对应的低门限配置范围<取值范围> 输入值必须是在这个范围的整型数
＜1-4294967295＞|<作用>  告警类型input-fcserrors对应的高门限配置范围<取值范围> 输入值必须是在这个范围的整型数








缺省 :

无 






使用说明 :

该命令配置后，实际的生效值可以通过show intf-statistics threshold查看。当前接口流量统计值在阈值范围之外时，会有一次告警产生，后续只有再次回到阈值范围内时，会产生一次告警恢复。不会重复告警多次。配置命令时要保证低门限的配置值小于高门限的配置值。





范例 :

配置fei-0/1/0/1的入方向接口利用率告警阈值ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1)#intf-statistics threshold input-utilization low 20 high 80






相关命令 :

show intf-statistics threshold 




## intf-statistics threshold 


intf-statistics threshold 




命令功能 :

该命令工作于接口性能统计物理接口配置模式下和接口性能统计物理子接口配置模式下。用于配置指定接口下指定计数器流量告警阈值。阈值分为高门限阈值和低门限阈值。当性能值超过所配置的告警阈值时就会产生越限告警。在高/低门限阈值范围内的则上报告警恢复。使用该命令后，可以实时监控接口上的流量变化。 






命令模式 :

 接口性能统计ulei接口模式  






命令默认权限级别 :

15 






命令格式 :


intf-statistics threshold 
  {input-utilization 
|output-utilization 
} low 
 ＜0-99 
＞ high 
 ＜1-100 
＞
no intf-statistics threshold 
  [{input-utilization 
|output-utilization 
}]
				






命令参数解释 :



参数|描述
---|---
input-utilization|<作用> 接口入方向的带宽利用率，表示在120s内当前接口收到的实际流量速率和接口总速率的比值
output-utilization|<作用> 接口出方向的带宽利用率，表示120s内当前接口发送的实际流量速率和接口总速率的比值
＜0-99＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的低门限配置范围<取值范围> 输入值必须是在这个范围的整型数
＜1-100＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的高门限配置范围<取值范围> 输入值必须是在这个范围的整型数








缺省 :

无 






使用说明 :

该命令配置后，实际的生效值可以通过show intf-statistics threshold查看。当前接口流量统计值在阈值范围之外时，会有一次告警产生，后续只有再次回到阈值范围内时，会产生一次告警恢复。不会重复告警多次。配置命令时要保证低门限的配置值小于高门限的配置值。





范例 :

ZXROSNG(config)#intf-statistics ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1.1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1.1)# intf-statistics threshold input-utilization low 60 high 80





相关命令 :

subinterface intf-statistics thresholdshow intf-statistics threshold 




## intf-statistics threshold 


intf-statistics threshold 




命令功能 :

该命令工作于接口性能统计物理接口配置模式下和接口性能统计物理子接口配置模式下。用于配置指定接口下指定计数器流量告警阈值。阈值分为高门限阈值和低门限阈值。当性能值超过所配置的告警阈值时就会产生越限告警。在高/低门限阈值范围内的则上报告警恢复。使用该命令后，可以实时监控接口上的流量变化。 






命令模式 :

 接口性能统计物理子接口模式  






命令默认权限级别 :

15 






命令格式 :


intf-statistics threshold 
  {input-utilization 
|output-utilization 
} low 
 ＜0-99 
＞ high 
 ＜1-100 
＞
no intf-statistics threshold 
  [{input-utilization 
|output-utilization 
}]
				






命令参数解释 :



参数|描述
---|---
input-utilization|<作用> 接口入方向的带宽利用率，表示在120s内当前接口收到的实际流量速率和接口总速率的比值
output-utilization|<作用> 接口出方向的带宽利用率，表示120s内当前接口发送的实际流量速率和接口总速率的比值
＜0-99＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的低门限配置范围<取值范围> 输入值必须是在这个范围的整型数
＜1-100＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的高门限配置范围<取值范围> 输入值必须是在这个范围的整型数








缺省 :

无 






使用说明 :

该命令配置后，实际的生效值可以通过show intf-statistics threshold查看。当前接口流量统计值在阈值范围之外时，会有一次告警产生，后续只有再次回到阈值范围内时，会产生一次告警恢复。不会重复告警多次。配置命令时要保证低门限的配置值小于高门限的配置值。





范例 :

ZXROSNG(config)#intf-statistics ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1.1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1.1)# intf-statistics threshold input-utilization low 60 high 80





相关命令 :

subinterface intf-statistics thresholdshow intf-statistics threshold 




## intf-statistics 


intf-statistics 




命令功能 :

该命令用于进入接口性能统计配置模式。当需要对接口流量统计功能进行控制，如，进行一分钟流量统计峰值功能、流量告警阈值配置、流量统计开关配置等相关配置时，必须先使用该命令进入接口性能统计配置模式。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



intf-statistics 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令工作于全局配置模式下，需要先进入全局配置模式，才能使用该命令。 






范例 :

进入接口性能统计配置模式。命令如下：ZXROSNG(config)#intf-statisticsZXROSNG(config-intf-statistics)#





相关命令 :

无 




## one_minute_peak_value_clear 


one_minute_peak_value_clear 




命令功能 :

该命令工作于接口性能统计配置模式下。用于清除一分钟峰值性能值。系统以一定的周期上报流量统计值。开启一分钟峰值功能后，对15分钟内，各项性能参数最大值及时间点进行了记录，呈现给用户。关闭后，不再记录这些时刻及性能统计值。峰值处理中，分别记录了当前值和最大值。接口性能统计模块收到数据刷新并对当前值进行累加，当整分钟时刻到，将当前值和已存在的最大值进行比较，如果大于历史最大值，则当前值替换为15分钟峰值，否则不替换。直达15分钟末即16分钟时，将15分钟-16分钟中统计的流量作为15分钟-16分钟区间段的最大值。后续进入新的整分钟时刻，比如17分钟时，则将当前值和15分钟-16分钟区间段的最大值比较，取大值。依次类推……也就是每15分钟取一次最大值。接口流量是以一定的周期上报的，每次上报的都是差值，通过记录这个最大值和最大值出现的系统时间，可以实时观察接口流量统计的性能。使用此命令后，可以清除show one_minute_peak_value下显示的接口一分钟峰值。





命令模式 :

 接口性能统计模式  






命令默认权限级别 :

15 






命令格式 :


one_minute_peak_value_clear 
  [＜interface-name 
＞]






命令参数解释 :



参数|描述
---|---
＜interface-name＞|<作用> 用于唯一标识一个接口。可以使用show ip in brief查询到当前设备上的接口<取值范围> 配置范围为1-32位的字符串当前参数没有输入时，表示批量清除当前设备上所有以太接口的一分钟峰值。<默认值> 无








缺省 :

无 






使用说明 :

使用该命令后，可以通过show one_minute_peak_value查看当前接口一分钟峰值是否清0。目前仅支持以太接口的一分钟峰值统计功能。





范例 :

1.清除所有以太接口的性能一分钟峰值统计数据ZXROSNG(config-intf-statistics)#one_minute_peak_value_clear 2.清除fei-0/1/0/1接口的性能一分钟峰值统计数据ZXROSNG(config-intf-statistics)#one_minute_peak_value_clear fei-0/1/0/1






相关命令 :

one_minute_peak_valueshow one_minute_peak_value




## one_minute_peak_value 


one_minute_peak_value 




命令功能 :

该命令工作于接口性能统计配置模式下。用于开启或关闭一分钟峰值统计功能。系统以一定的周期上报流量统计值。开启一分钟峰值功能后，对15分钟内，各项性能参数最大值及时间点进行了记录，呈现给用户。关闭后，不再记录这些时刻及性能统计值。峰值处理中，分别记录了当前值和最大值。接口性能统计模块收到数据刷新并对当前值进行累加，当整分钟时刻到，将当前值和已存在的最大值进行比较，如果大于历史最大值，则当前值替换为15分钟峰值，否则不替换。直达15分钟末即16分钟时，将15分钟-16分钟中统计的流量作为15分钟-16分钟区间段的最大值。后续进入新的整分钟时刻，比如17分钟时，则将当前值和15分钟-16分钟区间段的最大值比较，取大值。依次类推……也就是每15分钟取一次最大值。接口流量是以一定的周期上报的，每次上报的都是差值，通过记录这个最大值和最大值出现的系统时间，可以实时观察接口流量统计的性能。





命令模式 :

 接口性能统计模式  






命令默认权限级别 :

15 






命令格式 :


one_minute_peak_value 
  {enable 
|disable 
} {＜interface-name 
＞|default 
}






命令参数解释 :



参数|描述
---|---
enable|<作用> 开关打开标记，开启接口一分钟峰值统计功能
disable|<作用> 开关关闭标记，关闭接口一分钟峰值统计功能
＜interface-name＞|<作用>用于唯一标识一个接口，可以使用show ip in brief查询到当前设备上的接口取值范围为1-32位的字符串。
default|<作用> 所有接口标记，表示开启或关闭所有以太接口的一分钟峰值统计功能<默认值> 无








缺省 :

所有以太接口的一分钟峰值性能统计功能默认关闭 






使用说明 :

该命令配置后，可以通过show one_minute_peak_value查看接口的一分钟峰值。目前仅支持以太接口的一分钟峰值统计功能。开启所有接口一分钟峰值功能然后再关闭指定接口的一分钟峰值功能，则最终指定接口的一分钟峰值功能是关闭的。关闭所有接口一分钟峰值功能然后再开启指定接口的一分钟峰值功能，则最终指定接口的一分钟峰值功能是开启的，其他以太接口的一分钟峰值功能是关闭的。开启指定接口一分钟峰值功能然后再关闭所有接口的一分钟峰值功能，则所有以太接口的一分钟峰值功能是关闭的。关闭指定接口一分钟峰值功能然后再开启所有接口的一分钟峰值功能，则所有接口的一分钟峰值功能是开启的。





范例 :

1.开启所有以太接口的一分钟峰值性能统计功能ZXROSNG(config-intf-statistics)#one_minute_peak_value enable default 2.关闭fei-0/1/0/1接口的一分钟峰值性能统计功能ZXROSNG(config-intf-statistics)#one_minute_peak_value disable fei-0/1/0/1






相关命令 :

one_minute_peak_value_clearshow one_minute_peak_value




## show bgp-policy-accounting status ip interface 


show bgp-policy-accounting status ip interface 




命令功能 :

查看指定接口下IPv4 BGP策略计数开关的配置情况。不指定接口名称则显示所有接口的IPv4 BGP策略计数开关配置情况。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bgp-policy-accounting status ip interface 
  [＜interface-name 
＞]







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

这一命令仅在自测时使用，尚未支持任何项目。 






范例 :

查询所有接口的IPv4 BGP策略计数开关配置情况：ZXROSNG(config)#show bgp-policy-accounting status ip interface     Interface                        Insrc    Indst    Outsrc   Outdst     smartgroup1                      enable   disable  disable  enable    gei-0/1/0/1                      enable   enable   enable   disableZXROSNG(config)#






相关命令 :

无 




## show bgp-policy-accounting status ipv6 interface 


show bgp-policy-accounting status ipv6 interface 




命令功能 :

查询指定接口下IPv6 BGP策略计数的开关配置情况。不带接口名则查询所有接口下IPv6 BGP策略计数开关的配置情况。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show bgp-policy-accounting status ipv6 interface 
  [＜interface-name 
＞]







命令参数解释 :



参数|描述
---|---
＜interface-name＞|接口名称








缺省 :

无 






使用说明 :

本命令仅在自测时使用，尚未支持任何项目。 






范例 :

ZXROSNG(config)#show bgp-policy-accounting status ipv6 interface                     Interface                        Insrc    Indst    Outsrc   Outdst     smartgroup1                      disable  enable   enable   disable    gei-0/1/0/1                      enable   enable   disable  enableZXROSNG(config)#






相关命令 :

无 




## show counter 


show counter 




命令功能 :

该命令用于查询以太接口部分计数项的性能统计值。支持单个以太接口的计数查询，同时也支持批量的以太接口计数查询。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show counter 
  {inbound 
|outbound 
} [＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
inbound|<作用> 表明查询的是接口入方向的性能统计值
outbound|<作用> 表明查询的是接口出方向的性能统计值
＜interface-name＞|<作用>用于唯一标识一个接口，可以使用show ip in brief查询到当前设备上的接口<取值范围> 配置范围为1-32位的字符串当前参数没有输入时，表示批量查询设备上所有以太接口统计值<默认值> 无








缺省 :

无 






使用说明 :

此命令中查询到接口性能统计值，和使用show interface查询到的值是一样的。只是该命令显示了以太接口几项比较典型的性能统计项，更加清晰明了。 






范例 :

1.显示fei-0/1/0/1的接口性能统计计数ZXROSNG(config)#show counter inbound fei-0/1/0/1Interface      Packets Bytes  Unicasts Multicasts Broadcasts Time(s) Bps   Pps fei-0/1/0/1    2       1     4        6          5          120     0     02.显示所有接口的性能统计计数ZXROSNG(config)#show counter inbound            Interface      Packets Bytes  Unicasts Multicasts Broadcasts Time(s) Bps   Pps fei-0/1/0/1    2       1     4        6          5          120     0     0fei-0/1/0/2    2       1     4        6          5          120     0     0fei-0/1/0/3    2       1     4        6          5          120     0     0fei-0/1/0/4    2       1     4        6          5          120     0     0fei-0/1/0/5    2       1     4        6          5          120     0     0






相关命令 :

无 




## show interface-performance 


show interface-performance 




命令功能 :

批量查询接口CRC计数，支持批量查询以太口CRC计数 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show interface-performance 
  {crc-error 
} [phy-interface-only 
] 







命令参数解释 :



参数|描述
---|---
crc-error|CRC错误码计数
phy-interface-only|只显示所有物理口的CRC计数信息








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show interface-performance crc-error Interface               In-CRC-err        E-CRC-errgei-0/1/0/1             278820            278820gei-0/1/0/2             278820            278820gei-0/1/0/3             278820            278820gei-0/1/0/4             278820            278820gei-0/1/0/5             278820            278820gei-0/1/0/6             278820            278820gei-0/1/0/7             278820            278820gei-0/1/0/8             278820            278820pos192-0/1/1/1          278820            N/Apos192-0/1/1/2          278820            N/Apos192-0/1/1/3          278820            N/Asmartgroup1             0                 0posgroup1               0                 N/A





相关命令 :

无 




## show intf-statistics threshold 


show intf-statistics threshold 




命令功能 :

该命令用于查询指定接口的门限告警阈值。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show intf-statistics threshold 
  ＜interface-name 
＞ {input-utilization 
|output-utilization 
|input-fcserrors 
|input-fcsratio 
} 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|<作用> 用于唯一标识一个接口，可以使用show ip in brief查询到当前设备上的接口<取值范围> 配置范围为1-32位的字符串<默认值> 无
input-utilization|<作用> 接口入方向的带宽利用率，表示在120s内当前接口收到的实际流量速率和接口总速率的比值<默认值> 低门限默认值为0,高门限默认值为100
output-utilization|<作用> 接口出方向的带宽利用率，表示120s内当前接口发送的实际流量速率和接口总速率的比值<默认值> 低门限默认值为0,高门限默认值为100
input-fcserrors|<作用> 接口入方向的fcs错包数，表示10s内接口收到的fcs错误包数<默认值> 低门限默认值为0,高门限默认值为1000000
input-fcsratio|<作用> 接口入方向的fcs错包率，表示在120s内当前接口收到的fcs错误包与接口收到的总包数的比值<默认值> 低门限默认值为0,高门限默认值为100








缺省 :

无 






使用说明 :

只有已经配置了接口门限告警阈值，才能查询到实际的阈值信息。对于没有配置的接口，查询的是接口门限告警阈值的默认值。 






范例 :

显示接口fei-0/1/0/1的入方向接口利用率告警阈值ZXROSNG(config)#show intf-statistics threshold fei-0/1/0/1 input-utilization -------------------------------------ThresholdType(Unit)   Thresholdvalue-------------------------------------low(%)                0high(%)               100






相关命令 :

无 




## show intf-statistics utilization 


show intf-statistics utilization 




命令功能 :

显示接口的带宽利用率及光功率 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show intf-statistics utilization 
  [phy-interface-only 
] 







命令参数解释 :



参数|描述
---|---
phy-interface-only|只显示所有物理口的带宽利用率及光功率








缺省 :

无 






使用说明 :

无 






范例 :

显示所有接口的带宽利用率及光功率ZXROSNG(config)#show intf-statistics utilization In(Bps)/Out(Bps):in speed/out speedIn(%)/Out(%):in utilization/out utilizationIn-error:in crc errorIn(dBm)/Out(dBm):in optical power/out optical powerInterface             In(Bps)    In(%)Out(Bps)    Out(%)In-error  In(dBm)Out(dBm)fei-0/1/0/1           0           0    0           0     15         N/A   N/A  fei-0/1/0/1.1       0           0    0           0     N/A        N/A   N/Afei-0/1/0/2           0           0    0           0     15         N/A   N/Afei-0/1/0/3           0           0    0           0     15         N/A   N/Afei-0/1/0/4           0           0    0           0     15         N/A   N/Afei-0/1/0/5           0           0    0           0     15         N/A   N/Afei-0/1/0/6           0           0    0           0     15         N/A   N/Apos192-0/1/1/1        0           0    0           0     40         N/A   N/Apos192-0/1/1/2        0           0    0           0     40         N/A   N/Apos192-0/1/1/3        0           0    0           0     40         N/A   N/A
smartgroup1           0           0    0           0     0          N/A   N/A  smartgroup1.1       0           0    0           0     N/A        N/A   N/A显示所有物理接口的带宽利用率及光功率ZXROSNG(config)#show intf-statistics utilization phy-interface-only In(Bps)/Out(Bps):in speed/out speedIn(%)/Out(%):in utilization/out utilizationIn-error:in crc errorIn(dBm)/Out(dBm):in optical power/out optical powerInterface             In(Bps)    In(%)Out(Bps)    Out(%)In-error  In(dBm)Out(dBm)fei-0/1/0/1           0           0    0           0     15         N/A   N/Afei-0/1/0/2           0           0    0           0     15         N/A   N/Afei-0/1/0/3           0           0    0           0     15         N/A   N/Afei-0/1/0/4           0           0    0           0     15         N/A   N/Afei-0/1/0/5           0           0    0           0     15         N/A   N/Afei-0/1/0/6           0           0    0           0     15         N/A   N/Apos192-0/1/1/1        0           0    0           0     40         N/A   N/Apos192-0/1/1/2        0           0    0           0     40         N/A   N/Apos192-0/1/1/3        0           0    0           0     40         N/A   N/A






相关命令 :

无 




## show one_minute_peak_value 


show one_minute_peak_value 




命令功能 :

该命令用于查询以太接口一分钟峰值性能统计值。支持单个以太接口的一分钟峰值查询，同时也支持批量的以太接口一分钟峰值查询。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show one_minute_peak_value 
  [＜interface-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜interface-name＞|<作用>用于唯一标识一个接口。可以使用show ip in brief查询到当前设备上的接口<取值范围> 配置范围为1-32位的字符串。当前参数没有输入时，表示批量查询设备上所有以太接口的一分钟峰值<默认值> 无








缺省 :

无 






使用说明 :

只有开启接口一分钟峰值功能，并且接口上数据时流量，才能使用该命令查看到接口一分钟峰值性能统计值。开启接口一分钟峰值功能后，假如接口流量还没上报上来，使用该命令则会返回：Interface hasn't received one minute peak statistic data yet.





范例 :

显示fei-0/1/0/1的一分钟峰值性能统计数据ZXROSNG(config)#show one_minute_peak_value fei-0/1/0/1--------------------------------------------------------
Interface Name: fei-0/1/0/1One Minute Peak Value                Appear TimeIn_Unicast     : 0                   2012-01-08 06:37:43 In_Multicasts  : 0                   2012-01-08 06:37:43 In_Broadcasts  : 0                   2012-01-08 06:37:43 In_Error       : 0                   2012-01-08 06:37:43 E_Unicast      : 0                   2012-01-08 06:37:43 E_Multicasts   : 0                   2012-01-08 06:37:43 E_Broadcasts   : 0                   2012-01-08 06:37:43 E_Error        : 0                   2012-01-08 06:37:43 --------------------------------------------------------






相关命令 :

无 




## subinterface intf-statistics threshold 


subinterface intf-statistics threshold 




命令功能 :

该命令工作于接口性能统计物理接口配置模式下。用于批量配置指定接口下所有子接口的流量告警阈值。接口流量告警阈值分为高门限阈值和低门限阈值。当性能值超过所配置的告警阈值时就会产生越限告警。在高/低门限范围内的上报告警恢复。 






命令模式 :

 接口性能统计ulei接口模式  






命令默认权限级别 :

15 






命令格式 :


subinterface intf-statistics threshold 
  {input-utilization 
|output-utilization 
} low 
 ＜0-99 
＞ high 
 ＜1-100 
＞
no subinterface intf-statistics threshold 
  [{input-utilization 
|output-utilization 
}]
				






命令参数解释 :



参数|描述
---|---
input-utilization|<作用> 接口入方向的带宽利用率，表示在120s内当前接口收到的实际流量速率和接口总速率的比值
output-utilization|<作用> 接口出方向的带宽利用率，表示120s内当前接口发送的实际流量速率和接口总速率的比值
＜0-99＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的低门限配置范围<取值范围> 输入值必须是在这个范围的整型数
＜1-100＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的高门限配置范围<取值范围> 输入值必须是在这个范围的整型数








缺省 :

无 






使用说明 :

该命令配置后，接口告警阈值实际的生效值可以通过show intf-statistics threshold查看。当前接口流量统计值在阈值范围之外时，会有一次告警产生，后续只有再次回到阈值范围内时，会产生一次告警恢复。不会重复告警多次。配置命令时要保证低门限的配置值小于高门限的配置值。假设某个子接口已配置intf-statistics threshold，此时再在对应的父接口下配置subinterface intf-statistics threshold，则子接口会继承这个新的告警阈值。假设某个父接口下已配置subinterface intf-statistics threshold，然后再在对应的子接口会配置intf-statistics threshold，则子接口的告警阈值以当前自身的配置为准。





范例 :

ZXROSNG(config)#intf-statistics ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1)# subinterface intf-statistics threshold input-utilization low 34 high 89






相关命令 :

intf-statistics threshold单个子接口的门限配置 




## subinterface intf-statistics threshold 


subinterface intf-statistics threshold 




命令功能 :

该命令工作于接口性能统计物理接口配置模式下。用于批量配置指定接口下所有子接口的流量告警阈值。接口流量告警阈值分为高门限阈值和低门限阈值。当性能值超过所配置的告警阈值时就会产生越限告警。在高/低门限范围内的上报告警恢复。 






命令模式 :

 接口性能统计pos接口模式,接口性能统计以太接口模式  






命令默认权限级别 :

接口性能统计以太接口模式:15,接口性能统计pos接口模式:15 






命令格式 :


subinterface intf-statistics threshold 
  {input-utilization 
|output-utilization 
} low 
 ＜0-99 
＞ high 
 ＜1-100 
＞
no subinterface intf-statistics threshold 
  [{input-utilization 
|output-utilization 
}]
				






命令参数解释 :



参数|描述
---|---
input-utilization|<作用> 接口入方向的带宽利用率，表示在120s内当前接口收到的实际流量速率和接口总速率的比值
output-utilization|<作用> 接口出方向的带宽利用率，表示120s内当前接口发送的实际流量速率和接口总速率的比值
＜0-99＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的低门限配置范围<取值范围> 输入值必须是在这个范围的整型数
＜1-100＞|<作用>  告警类型input-utilization 、ouput-utilization、input-fcsratio对应的高门限配置范围<取值范围> 输入值必须是在这个范围的整型数








缺省 :

无 






使用说明 :

该命令配置后，接口告警阈值实际的生效值可以通过show intf-statistics threshold查看。当前接口流量统计值在阈值范围之外时，会有一次告警产生，后续只有再次回到阈值范围内时，会产生一次告警恢复。不会重复告警多次。配置命令时要保证低门限的配置值小于高门限的配置值。假设某个子接口已配置intf-statistics threshold，此时再在对应的父接口下配置subinterface intf-statistics threshold，则子接口会继承这个新的告警阈值。假设某个父接口下已配置subinterface intf-statistics threshold，然后再在对应的子接口会配置intf-statistics threshold，则子接口的告警阈值以当前自身的配置为准。





范例 :

ZXROSNG(config)#intf-statistics ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1)# subinterface intf-statistics threshold input-utilization low 34 high 89






相关命令 :

intf-statistics threshold单个子接口的门限配置 




## subinterface traffic-statistics 


subinterface traffic-statistics 




命令功能 :

该命令工作于接口性能统计物理接口配置模式下或者接口性能统计逻辑接口配置模式下，用于批量开启或关闭父接口下所有子接口的全局开关。使用该命令开启开关后，系统按照一定的周期间隔上报子接口流量统计值。关闭开关后，停止上报子接口流量统计值。 






命令模式 :

 接口性能统计ATM接口模式,接口性能统计eth_dslgroup接口模式,接口性能统计ulei接口模式  






命令默认权限级别 :

接口性能统计eth_dslgroup接口模式:15,接口性能统计ATM接口模式:15,接口性能统计ulei接口模式:15 






命令格式 :



subinterface traffic-statistics 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|批量开启父接口下所有子接口的全局开关
disable|批量关闭父接口下所有子接口的全局开关








缺省 :

接口下所有子接口的性能统计功能默认去使能 






使用说明 :

系统以一定的周期上报流量统计值。当设备上有很多接口时，比如大量的子接口，此时如果允许芯片一直计数并上报，对CPU会造成严重的消耗及浪费。因此通过此开关关闭设备上指定接口下所有的子接口统计功能，不再上报计数。 使用该命令后可以通过show interface命令查看子接口是否有计数信息显示。subinterface traffic-statistics和指定子接口下的traffic-statistics命令之间取“或”的逻辑关系。即当父接口下全局子接口开关开启，而指定子接口开关关闭，则指定子接口开关实际是开启的；当父接口下全局子接口开关关闭，而指定子接口开关开启，则指定子接口开关实际是开启的。只有当父接口下全局子接口开关关闭，指定子接口开关也关闭，指定子接口开关才能关闭。开关默认关闭。





范例 :

使能fei-0/1/0/1接口下所有子接口的性能统计功能ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1)# subinterface traffic-statistics enable





相关命令 :

无 




## subinterface traffic-statistics 


subinterface traffic-statistics 




命令功能 :

该命令工作于接口性能统计物理接口配置模式下或者接口性能统计逻辑接口配置模式下，用于批量开启或关闭父接口下所有子接口的全局开关。使用该命令开启开关后，系统按照一定的周期间隔上报子接口流量统计值。关闭开关后，停止上报子接口流量统计值。 






命令模式 :

 接口性能统计smartgroup接口模式  






命令默认权限级别 :

15 






命令格式 :



subinterface traffic-statistics 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|<作用>开关开启，系统开始上报父接口下所有子接口流量统计值
disable|<作用>开关关闭，系统开始上报父接口下所有子接口流量统计值








缺省 :

接口下所有子接口的性能统计功能默认去使能 






使用说明 :

系统以一定的周期上报流量统计值。当设备上有很多接口时，比如大量的子接口，此时如果允许芯片一直计数并上报，对CPU会造成严重的消耗及浪费。因此通过此开关关闭设备上指定接口下所有的子接口统计功能，不再上报计数。 使用该命令后可以通过show interface命令查看子接口是否有计数信息显示。subinterface traffic-statistics和指定子接口下的traffic-statistics命令之间取“或”的逻辑关系。即当父接口下全局子接口开关开启，而指定子接口开关关闭，则指定子接口开关实际是开启的；当父接口下全局子接口开关关闭，而指定子接口开关开启，则指定子接口开关实际是开启的。只有当父接口下全局子接口开关关闭，指定子接口开关也关闭，指定子接口开关才能关闭。开关默认关闭。





范例 :

使能fei-0/1/0/1接口下所有子接口的性能统计功能ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1)# subinterface traffic-statistics enable





相关命令 :

无 




## subinterface traffic-statistics 


subinterface traffic-statistics 




命令功能 :

该命令工作于接口性能统计物理接口配置模式下或者接口性能统计逻辑接口配置模式下，用于批量开启或关闭父接口下所有子接口的全局开关。使用该命令开启开关后，系统按照一定的周期间隔上报子接口流量统计值。关闭开关后，停止上报子接口流量统计值。 






命令模式 :

 接口性能统计pos接口模式,接口性能统计以太接口模式,接口性能统计通道化cpos_e1接口模式  






命令默认权限级别 :

接口性能统计通道化cpos_e1接口模式:15,接口性能统计以太接口模式:15,接口性能统计pos接口模式:15 






命令格式 :



subinterface traffic-statistics 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|<作用>开关开启，系统开始上报父接口下所有子接口流量统计值
disable|<作用>开关关闭，系统开始上报父接口下所有子接口流量统计值








缺省 :

接口下所有子接口的性能统计功能默认去使能 






使用说明 :

系统以一定的周期上报流量统计值。当设备上有很多接口时，比如大量的子接口，此时如果允许芯片一直计数并上报，对CPU会造成严重的消耗及浪费。因此通过此开关关闭设备上指定接口下所有的子接口统计功能，不再上报计数。 使用该命令后可以通过show interface命令查看子接口是否有计数信息显示。subinterface traffic-statistics和指定子接口下的traffic-statistics命令之间取“或”的逻辑关系。即当父接口下全局子接口开关开启，而指定子接口开关关闭，则指定子接口开关实际是开启的；当父接口下全局子接口开关关闭，而指定子接口开关开启，则指定子接口开关实际是开启的。只有当父接口下全局子接口开关关闭，指定子接口开关也关闭，指定子接口开关才能关闭。开关默认关闭。





范例 :

使能fei-0/1/0/1接口下所有子接口的性能统计功能ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1ZXROSNG(config-intf-statistics-if-fei-0/1/0/1)# subinterface traffic-statistics enable





相关命令 :

无 




## traffic-statistics 


traffic-statistics 




命令功能 :

该命令工作于接口性能统计物理子接口配置模式下，用于开启或关闭指定子接口的流量统计开关。使用该命令开启开关后，系统按照一定的周期上报子接口流量统计值。关闭开关后，停止上报子接口流量统计值。 






命令模式 :

 接口性能统计物理子接口模式  






命令默认权限级别 :

15 






命令格式 :



traffic-statistics 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|<作用>开关开启，系统开始上报子接口流量统计值
disable|<作用>开关关闭，系统停止上报子接口流量统计值








缺省 :

接口的性能统计功能默认去使能 






使用说明 :

系统以一定的周期上报流量统计值。当系统有很多接口时，比如大量的子接口，此时如果允许芯片一直计数并上报，对CPU会造成严重的消耗及浪费。因此通过此开关关闭设备上指定子接口的接口统计功能，不再上报计数。使用该命令后可以通过show interface命令查看子接口是否有计数信息显示。subinterface traffic-statistics和指定子接口下的traffic-statistics命令之间取“或”的逻辑关系。即当父接口下全局子接口开关开启，而指定子接口开关关闭，则指定子接口开关实际是开启的；当父接口下全局子接口开关关闭，而指定子接口开关开启，则指定子接口开关实际是开启的。只有当父接口下全局子接口开关关闭，指定子接口开关也关闭，指定子接口开关才能关闭。开关默认关闭。





范例 :

使能物理接口fei-0/1/0/1.1接口的性能统计功能ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1.1ZXROSNG(config-intf-statistics-fei-0/1/0/1.1)#traffic-statistics enable






相关命令 :

无 




## traffic-statistics 


traffic-statistics 




命令功能 :

该命令工作于接口性能统计逻辑子接口配置模式下，用于开启或关闭指定子接口的流量统计开关。使用该命令开启开关后，系统按照一定的周期上报子接口流量统计值。关闭开关后，停止上报子接口流量统计值。 






命令模式 :

 接口性能统计逻辑子接口模式  






命令默认权限级别 :

15 






命令格式 :



traffic-statistics 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|<作用>开关开启，系统开始上报子接口流量统计值
disable|<作用>开关关闭，系统停止上报子接口流量统计值








缺省 :

接口的性能统计功能默认去使能 






使用说明 :

系统以一定的周期上报流量统计值。当系统有很多接口时，比如大量的子接口，此时如果允许芯片一直计数并上报，对CPU会造成严重的消耗及浪费。因此通过此开关关闭设备上指定子接口的接口统计功能，不再上报计数。使用该命令后可以通过show interface命令查看子接口是否有计数信息显示。subinterface traffic-statistics和指定子接口下的traffic-statistics命令之间取“或”的逻辑关系。即当父接口下全局子接口开关开启，而指定子接口开关关闭，则指定子接口开关实际是开启的；当父接口下全局子接口开关关闭，而指定子接口开关开启，则指定子接口开关实际是开启的。只有当父接口下全局子接口开关关闭，指定子接口开关也关闭，指定子接口开关才能关闭。开关默认关闭。





范例 :

使能物理接口fei-0/1/0/1.1接口的性能统计功能ZXROSNG(config-intf-statistics)#interface fei-0/1/0/1.1ZXROSNG(config-intf-statistics-fei-0/1/0/1.1)#traffic-statistics enable






相关命令 :

无 




## traffic-statistics 


traffic-statistics 




命令功能 :

该命令工作于接口性能统计te隧道接口配置模式下，用于开启或关闭指定的te_tunnnel接口流量统计开关。使用该命令开启开关后，系统按照一定的周期上报te_tunnnel接口流量统计值。关闭开关后停止上报te_tunnnel接口流量统计值。 






命令模式 :

 接口性能统计te隧道接口模式  






命令默认权限级别 :

15 






命令格式 :



traffic-statistics 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|<作用> 开关开启，系统开始上报te_tunnnel接口流量统计值
disable|<作用>开关关闭，系统停止上报te_tunnnel接口流量统计值








缺省 :

默认是去使能 






使用说明 :

系统以一定的周期上报流量统计值。当系统有很多te_tunnel接口时，如果允许芯片一直计数并上报，对CPU会造成严重的消耗及浪费。因此通过此开关关闭设备上指定te_tunnnel接口的接口统计功能，不再上报计数。使用该命令后可以通过show interface命令查看te_tunnnel接口是否有计数信息显示。开关默认关闭。





范例 :

ZXROSNG(config)#intf-statistics ZXROSNG(config-intf-statistics)#interface te_tunnel1ZXROSNG(config-intf-statistics-if-te_tunnel1)#traffic-statistics enable 






相关命令 :

无 




## traffic-statistics 


traffic-statistics 




命令功能 :

该命令工作于接口性能统计gre隧道接口配置模式下，用于开启或关闭指定的gre_tunnnel接口流量统计开关。使用该命令开启开关后，系统按照一定的周期上报gre_tunnnel接口流量统计值。关闭开关后停止上报gre_tunnnel接口流量统计值。 






命令模式 :

 接口性能统计gre隧道接口模式  






命令默认权限级别 :

15 






命令格式 :



traffic-statistics 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|<作用> 开关开启，系统开始上报gre_tunnnel接口流量统计值
disable|<作用>开关关闭，系统停止上报gre_tunnnel接口流量统计值








缺省 :

默认是去使能 






使用说明 :

系统以一定的周期上报流量统计值。当系统有很多gre_tunnel接口时，如果允许芯片一直计数并上报，对CPU会造成严重的消耗及浪费。因此通过此开关关闭设备上指定gre_tunnnel接口的接口统计功能，不再上报计数。使用该命令后可以通过show interface命令查看gre_tunnnel接口是否有计数信息显示。开关默认关闭。





范例 :

ZXROSNG(config)#intf-statistics ZXROSNG(config-intf-statistics)#interface gre_tunnel1ZXROSNG(config-intf-statistics-if-gre_tunnel1)#traffic-statistics enable 






相关命令 :

无 




## traffic-statistics 


traffic-statistics 




命令功能 :

该命令工作于接口性能统计配置模式下，用于开启或关闭当前设备所有支持流量统计功能的接口的全局开关。使用该命令开启开关后，系统按照一定的周期间隔上报接口流量统计值。关闭开关后，停止上报接口流量统计值。 






命令模式 :

 接口性能统计模式  






命令默认权限级别 :

15 






命令格式 :



traffic-statistics 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|<作用> 开关开启，系统开始上报接口流量统计值。
disable|<作用>开关关闭，系统停止上报接口流量统计值。








缺省 :

系统的接口性能统计功能默认使能 






使用说明 :

系统以一定的周期上报流量统计值。当设备上有很多接口时，比如大量的子接口，此时如果允许芯片一直计数并上报，对CPU会造成严重的消耗及浪费。因此通过此开关关闭设备上所有的接口统计功能，不再上报计数。使用该命令后可以通过show interface命令查看接口是否有计数信息显示。开关仅作用于支持show interface接口下StreamCounters区计数，对于HardWareCounters 计数区不起作用。





范例 :

开启所有接口的流量上报功能。 命令如下：ZXROSNG(config-intf-statistics)# traffic-statistics enable关闭所有接口的流量上报功能。命令如下：ZXROSNG(config-intf-statistics)# traffic-statistics disable





相关命令 :

无 




