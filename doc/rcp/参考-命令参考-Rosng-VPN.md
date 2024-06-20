# GRE配置命令 
## debug gre-tunnel interface 


debug gre-tunnel interface 




命令功能 :

打开指定GRE隧道的debug报文打印开关该命令工作于特权模式，用于开启GRE隧道的报文封装与解封装打印开关。该命令用于调试GRE隧道，检查GRE隧道的封装与解封装流程。用户开启该开关后，可以查看所有GRE隧道的报文封装与解封装信息，从而可以根据这些信息检查隧道的封装与解封装流程是否正确。





命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug gre-tunnel interface 
  ＜interface-name 
＞
no debug gre-tunnel interface 
  ＜interface-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|已创建的gre_tunnel接口








缺省 :

默认关闭该打印功能。 






使用说明 :

接口名必须是已经创建的GRE隧道接口，否则会提示命令错误，其它使用方法和debug gre-tunnel相同 






范例 :

ZXROSNG#debug gre-tunnel interface gre_tunnel1GRE tunnel interface debugging is onZXROSNG#no debug gre-tunnel interface gre_tunnel1GRE tunnel interface debugging is off





相关命令 :

terminal monitordebug gre-tunnelno debug gre-tunnel



## debug gre-tunnel 


debug gre-tunnel 




命令功能 :

该命令工作于特权模式，用于开启GRE隧道的报文封装与解封装打印开关。该命令用于调试GRE隧道，检查GRE隧道的封装与解封装流程。用户开启该开关后，可以查看所有GRE隧道的报文封装与解封装信息，从而可以根据这些信息检查隧道的封装与解封装流程是否正确。






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug gre-tunnel 
 

no debug gre-tunnel 








命令参数解释 :


					无
				 






缺省 :

关闭该调试功能 






使用说明 :

该命令需要伴随terminal monitor命令使用（参见命令terminal monitor），否则用户看不到隧道的封装与解封装打印信息。该打印开关状态可以通过命令show debug gre-tunnel查看（参见命令show debug gre-tunnel）。该命令开关默认为关闭，即默认不打印隧道封装与解封装信息。该命令开关打开后，会打印所有GRE隧道中报文的封装与解封装信息，包括keepalive报文，因此在GRE隧道数目较多时会打印大量的报文信息。建议用户在调试特定的GRE隧道时，用shutdown命令关闭其他不相关的GRE隧道接口以及用 no tunnel keepalive命令关闭隧道的keepalive开关（参见配置命令tunnel keepalive）。





范例 :

ZXROSNG#terminal monitorZXROSNG#debug gre-tunnel GRE tunnel debugging is onZXROSNG#no debug gre-tunnel GRE tunnel debugging is off在用户开启debug gre-tunnel开关后，如果有报文进出GRE隧道，可看到GRE隧道报文封装与解封装信息：ZXR10 MPU-0/20/0 2013-11-21 08:18:51 gre_tunnel1: GRE/IPv4 packet to be encapsulated: 10.1.1.1-->10.1.1.2 (len=100 ttl=255) ZXR10 MPU-0/20/0 2013-11-21 08:18:51 gre_tunnel1: GRE/IPv4 packet encapsulated: 1.1.1.1-->1.1.1.2 (len=124 ttl=255) !ZXR10 MPU-0/20/0 2013-11-21 08:18:51 gre_tunnel1: GRE/IPv4 packet to be decapsulated: 1.1.1.2-->1.1.1.1 (len=124 ttl=255) ZXR10 MPU-0/20/0 2013-11-21 08:18:51 gre_tunnel1: GRE/IPv4 packet decapsulated: 10.1.1.2-->10.1.1.1 (len=120 ttl=255)






相关命令 :

terminal monitor    show debug gre-tunnel



## gre-config 


gre-config 




命令功能 :

该命令工作于全局配置模式，用于进入GRE隧道配置模式。GRE全称为Generic Routing Encapsulation，是一种通用路由封装协议，实现一种协议报文在另一种网路中传输的机制，而这种传输通道称为tunnel。GRE隧道相关信息可参见RFC1701、RFC2784、RFC2890等文档。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


gre-config 
 






命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

拥有管理员权限的操作员通过该命令进入GRE隧道配置模式，之后才可以指定隧道接口名进入GRE隧道接口业务配置模式。此外，还可以在此模式下对隧道的全局开关进行控制，比如对keepalive-mode（参见配置命令tunnel keepalive-mode）的控制。 






范例 :

ZXROSNG(config)#gre-configZXROSNG(config-gre)#该模式下可通过指定隧道接口进入GRE隧道接口配置模式，如下所示：ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#





相关命令 :

configure terminalinterface gre_tunnel<tunnel no>



interface :

interface (GRE隧道模式) 




命令功能 :

该命令工作于GRE隧道配置模式，用于进入特定隧道的GRE隧道接口业务配置模式。执行成功后，可以在GRE隧道接口业务配置模式下对该隧道进行配置。 






命令模式 :

 GRE隧道模式  






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
＜interface-byname＞|用于标识GRE隧道的接口别名。取值范围：1-32位的字符串。默认值：无。
＜interface-name＞|用于标识GRE隧道的接口名称。取值范围：1-32位的字符串。默认值：无。








缺省 :

无 






使用说明 :

执行该命令前，需要提前创建相应的GRE隧道接口（参见全局配置模式下的配置命令interface），如果需要用到接口别名，需要在创建的GRE隧道接口中创建接口别名。可以通过show ip interface brief命令查询已经存在的GRE隧道接口。进入GRE隧道接口业务配置模式后，拥有管理员权限的操作员可以对隧道的模式，源地址和目的地址等信息进行配置，详细操作请参考隧道接口业务配置模式下的命令。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)byname tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#exitZXROSNG(config)#gre-tunnelZXROSNG(config-gre)#interface byname tunnel1





相关命令 :

gre-config 



## show debug gre-tunnel 


show debug gre-tunnel 




命令功能 :

该命令工作于任意模式下，用于查看GRE隧道debug开关是否开启。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug gre-tunnel 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于帮助用户查看GRE隧道的debug开关开启情况，在debug gre-tunnel开关默认关闭的情况下，执行该show命令后没有debug开关关闭的回显信息，只有在debug gre-tunnel开关开启时，才会有相应的回显信息。 






范例 :

ZXROSNG#show debug gre-tunnel ZXROSNG#ZXROSNG#debug gre-tunnel GRE tunnel debugging is onZXROSNG#show debug gre-tunnel GRE-TUNNEL:  GRE-tunnel packets debugging is on当用户执行show debug gre-tunnel命令后有回显提示GRE-tunnel packets debugging is on，说明GRE隧道的debug调试开关处于开启状态，否则处于关闭状态。






相关命令 :

debug gre-tunnelterminal monitor



## tunnel bfd 


tunnel bfd 




命令功能 :

该命令工作于GRE隧道接口业务模式，用于启用GRE隧道BFD（Bidirectional Forwarding Detection）检测机制。BFD是一套用来实现快速检测的国际标准协议，提供一种轻负荷、持续时间短的检测。该检测机制与keepalive保活机制的作用基本相同，都是用于检测隧道对端的状态，防止隧道流量断流。但是相对于keepalive保活机制而言，bfd检测机制能够提供更高的精度，实现更快速的流量切换。





命令模式 :

 GRE隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel bfd 
 

no tunnel bfd 








命令参数解释 :


					无
				 






缺省 :

隧道bfd功能未使能 






使用说明 :

BFD是一种双向检测机制，因此用户开启该检测功能时，需要在隧道两端同时打开该检测开关，否则该检测机制不生效。配置该命令前需要先通过tunnel mode命令配置隧道模式。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel mode ipZXROSNG(config-gre-if-gre_tunnel1)#tunnel bfdZXROSNG(config-gre-if-gre_tunnel1)#no tunnel bfd





相关命令 :

configure terminalinterface gre_tunnel<tunnel no>tunnel mode ip




## tunnel checksum 


tunnel checksum 




命令功能 :

该命令工作于GRE隧道接口业务模式，用于启用GRE隧道校验和选项。用户为GRE隧道设置了该选项后，隧道在对报文进行封装时，会设置GRE报文头中的C标志位为1，并且用报文的校验和填充GRE报文头中的checksum字段，在隧道对端会对报文进行校验和信息的验证，详细信息请参见rfc1701。





命令模式 :

 GRE隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel checksum 
 

no tunnel checksum 








命令参数解释 :


					无
				 






缺省 :

GRE隧道不使能checksum选项 






使用说明 :

隧道默认未开启校验和验证。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel checksumZXROSNG(config-gre-if-gre_tunnel1)#no tunnel checksum





相关命令 :

interface gre_tunnel<tunnel no>gre-config



## tunnel clear-dont-fragment-bit 


tunnel clear-dont-fragment-bit 




命令功能 :

该命令工作于GRE隧道接口业务模式，用于为xGW项目设置分片标识位。拥有管理员权限的操作员可以通过该命令清除GRE隧道的DF（Don’t Fragment）标记位，即支持经过该gre隧道封装后的报文进行分片。





命令模式 :

 GRE隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel clear-dont-fragment-bit 
 

no tunnel clear-dont-fragment-bit 








命令参数解释 :


					无
				 






缺省 :

gre隧道clearDFBit标示位为0 






使用说明 :

该配置命令只适用于xGW网元，配置作用于转发面，决定转发面在GRE封装后的分片行为，默认是GRE封装后不支持分片.可以通过该配置命令清除DF标记，支持GRE封装后的报文的分片功能。配置该命令前需要先通过tunnel mode命令配置隧道模式。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel mode ipZXROSNG(config-gre-if-gre_tunnel1)#tunnel clear-dont-fragment-bitZXROSNG(config-gre-if-gre_tunnel1)#no tunnel clear-dont-fragment-bit    





相关命令 :

interface gre_tunnel<tunnel no>gre-configtunnel mode ip



## tunnel destination 


tunnel destination 




命令功能 :

该命令工作于GRE隧道接口业务配置模式，用于为隧道配置目的地址。用户使用该命令为隧道指定隧道目的地址后，在隧道对报文进行封装时，隧道会将该地址作为封装后的IPv4或IPv6报文的目的地址。





命令模式 :

 GRE隧道接口业务模式  






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
ipv4|隧道封装模式为V4，外层为IPv4报文，目的地址为一个IPv4类型的地址，内层可以为IPv4或IPv6报文，GRE隧道为ipv4 over ipv4或者ipv6 over ipv4隧道
＜ipv4-address＞|隧道末端的地址
ipv6|隧道封装模式为V6，外层为IPv6报文，目的地址为一个IPv6类型的地址，内层可以为IPv4或IPv6报文，GRE隧道为ipv4 over ipv6或者ipv6 over ipv6隧道
＜ipv6-address＞|隧道末端的地址








缺省 :

隧道未配置目的地址 






使用说明 :

隧道目的地址配置支持IPv4和IPv6两种类型。通过本命令配置的目的地址类型必须与通过tunnel mode命令配置的隧道模式相同，即当隧道模式为ip时，只能配置IPv4类型的目的地址，否则会有错误提示，隧道模式为ipv6时，只能配置IPv6类型的目的地址。不同隧道的基本信息配置不能冲突，即通过tunnel source命令配置的源地址、通过tunnel destination命令配置的目的地址以及通过tunnel vrf命令配置的VRF，不同的GRE隧道对应的这三个配置不能完全一致，否则会有隧道冲突。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel mode ipZXROSNG(config-gre-if-gre_tunnel1)#tunnel destination ipv4 1.1.1.2ZXROSNG(config-gre-if-gre_tunnel1)#no tunnel destination





相关命令 :

interface gre_tunnel<tunnel no>gre-configtunnel mode ip



## tunnel dscp 


tunnel dscp 




命令功能 :

该命令工作于GRE隧道接口业务模式，用于启用GRE隧道DSCP（Differentiated Services Codepoint）设置的功能。DSCP由RFC2474定义，它重新命名了IPv4报头中TOS使用的1字节和IPv6报头中数据类（Traffic Class）1字节，新的名字称为DS字段（Differentiated Services Field）。该字段的作用没有变，仍然被QoS工具用来标记数据。不同的是IPP使用3比特，而DSCP使用6比特，最低2比特不用。RFC2474 定义最高3比特为级别／类别选择代码（ClassSelector Codepoints，CS），其意义和IPv4报头中IP优先级的定义是相同的，CS0 ～CS7的级别相等于IP优先级0 ～7。但它并没有定义第3到第5比特的具体含义以及使用规则。DSCP使用6比特，可以定义64个优先级（0－63）。





命令模式 :

 GRE隧道接口业务模式  






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

隧道未配置dscp，发包时优先级从内层报文继承。 






使用说明 :

1.在未配置隧道DSCP优先级时，隧道封装时默认从内层IP/IPv6头中继承DSCP值；2.未配置时，对于GRE隧道，如果内层为mpls标签报文，没有继承处理；从最外层标签exp中继承填入DSCP的高3bit；3.未配置时，对于GRE隧道，如果内层为isis封装报文，则不做继承；4.配置以后以配置值封装外层IP/IPv6报文的DSCP优先级，否则从内层继承IPP/DSCP/EXP优先级；对于GRE隧道，如果内层为mpls标签报文，从最外层标签exp中继承填入DSCP的高3bit；





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel dscp 60ZXROSNG(config-gre-if-gre_tunnel1)#no tunnel dscp





相关命令 :

interface gre_tunnel<tunnel no>gre-configtunnel mode ip



## tunnel keepalive 


tunnel keepalive 




命令功能 :

该命令工作与GRE隧道接口业务模式，用于启用隧道keepalive保活机制。由于隧道始端无法感知隧道末端的状态，因此如果隧道接收端由于某些原因导致隧道接口down，而隧道发送端并不能感受到这种变化而是照旧发送报文，就会造成报文像进入黑洞一样丢失。Keepalive保活机制就是用来解决这种问题的，它通过发送keepalive保活报文来检测隧道对端的状态，并对这种状态变化做出反应。






命令模式 :

 GRE隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel keepalive 
  [＜period 
＞ ＜retries 
＞]

no tunnel keepalive 








命令参数解释 :



参数|描述
---|---
＜period＞|用于设置keepalive报文的发送周期取值范围：1-32767，单位为秒默认值：10
＜retries＞|用于设置keepalive报文的尝试次数取值范围：1-255 默认值：3








缺省 :

GRE隧道保活功能未使能 






使用说明 :

配置该命令前需要先通过tunnel mode命令配置隧道模式。该命令设置后会影响本隧道接口的状态。如果超过设定的keepalive保活时间隧道本端还没有收到隧道对端的回应时，隧道本端接口会置down。隧道本端通过keepalive保活机制发现对端接口状态up后，会更新本端的隧道接口状态。启用keepalive机制后会产生周期性的报文流量，大量GRE隧道开启keepalive保活机制可能会对网元的性能造成一定的影响。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel mode ipZXROSNG(config-gre-if-gre_tunnel1)#tunnel keepalive 1 3ZXROSNG(config-gre-if-gre_tunnel1)#no tunnel keepalive





相关命令 :

interface gre_tunnel<tunnel no>gre-config



## tunnel keepalive-mode 


tunnel keepalive-mode 




命令功能 :

该命令工作于GRE隧道配置模式，用于转换keepalive报文的处理模式。默认情况下，keepalive报文是由控制面来进行收发处理的，并进行GRE隧道的状态切换。但是随着开启keepalive机制的隧道数目的增多，控制面需要处理大量的keepalive报文，可能会对控制面其他报文收发造成一定的影响。使用该命令切换keepalive报文的收发模式，由控制面收发转换为转发面收发，这样就能在增加keepalive隧道配置数目的同时，不影响控制面处理其他类型报文处理的能力。





命令模式 :

 GRE隧道模式  






命令默认权限级别 :

15 






命令格式 :


tunnel keepalive-mode 
  {centralized 
|distributed 
}






命令参数解释 :



参数|描述
---|---
centralized|与distributed模式二选一，该模式下，控制面负责处理keepalive报文并对隧道状态进行更新。
distributed|与centralized模式二选一，该模式下，转发面负责处理keepalive报文并将结果上送控制面，控制面负责隧道状态的更新。








缺省 :

默认为centralized，即主控进行keepalive报文的处理 






使用说明 :

Keepalive-mode转换为distributed后，控制面不再处理keepalive报文，交由转发面来处理。转发面会将keepalive报文的处理结果上送给控制面，控制面对相应的GRE隧道进行状态更新。该开关影响所有的GRE隧道，并非对单一隧道接口的控制。可以通过show running-config gre-tunnel命令查看GRE隧道的keepalive-mode模式。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#gre-configZXROSNG(config-gre)#tunnel keepalive-mode distributedZXROSNG(config-gre)#tunnel keepalive-mode centralized





相关命令 :

无 




## tunnel key 


tunnel key 




命令功能 :

该命令工作于GRE隧道接口业务模式，用于启用GRE隧道Key选项。用户为GRE隧道设置了key值后，GRE隧道在封装报文时会将该key值封装在GRE报文头的key选项中。报文到达隧道对端进行解封装时，对端需要对key值进行验证，如果隧道本端配置的key值与隧道对端配置的key值不匹配，报文会被丢弃，详细信息请参见rfc1701，rfc2890等。





命令模式 :

 GRE隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel key 
  ＜key-value 
＞

no tunnel key 








命令参数解释 :



参数|描述
---|---
＜key-value＞|用于为隧道设置的key选项值取值范围：0-4294967295的数字串默认值：未配置








缺省 :

GRE隧道不使能key选项 






使用说明 :

Key值的取值范围为0-4294967295，默认未设置key值。如果用户设置了key值，那么隧道两端的key值必须相同，否则会造成隧道通信失败。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel key 123ZXROSNG(config-gre-if-gre_tunnel1)#no tunnel key





相关命令 :

interface gre_tunnel<tunnel no>gre-config



## tunnel mode 


tunnel mode 




命令功能 :

该命令工作于GRE隧道接口业务配置模式，用于配置当前隧道的模式。隧道的封装模式主要分为GRE-IPv4以及GRE-IPv6两种。GRE-IPv4表示外层封装IPv4报文并在IPv4网络中传输，GRE-IPv6表示外层封装IPv6报文并在IPv6网络中传输。





命令模式 :

 GRE隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel mode 
  {ip 
|ipv6 
|ds-lite 
 {static 
|dynamic 
}}

no tunnel mode 








命令参数解释 :



参数|描述
---|---
ip|GRE over IPv4隧道模式
ipv6|GRE over IPv6隧道模式
static|隧道模式的一种，静态DS Lite隧道模式, 该模式在CGN场景中才能使用
dynamic|隧道模式的一种，动态DS Lite隧道模式, 该模式在CGN场景中才能使用








缺省 :

隧道模式未配置 






使用说明 :

用户在配置该命令前，如果隧道已经有源、目的地址等配置，该隧道模式的配置需要与源目的地址的类型相匹配，即如果隧道源目的地址配置为IPv4类型，隧道模式应该为ip，否则会有配置错误信息提示。该隧道模式的变更或取消时，会清除隧道的其它配置。例如隧道接口配置有源地址时，使用tunnel mode命令变更隧道模式或执行no tunnel mode命令会清除隧道原有的源地址配置信息。





范例 :

ZXROSNG(config)#gre-configZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel mode ipv6ZXROSNG(config-gre-if-gre_tunnel1)#no tunnel mode





相关命令 :

interface gre_tunnel<tunnel no>gre-config



## tunnel source interface 


tunnel source interface 




命令功能 :

该命令工作于GRE隧道接口业务模式，使用接口名为隧道配置源地址。该命令实现功能与tunnel source相同，不同的是tunnel source命令直接为隧道指定源地址，而本命令是通过为隧道指定源接口，通过从源接口上获取IPv4/IPv6地址，从而间接的为隧道指定源地址。在使用该命令为隧道指定源接口后，隧道的VRF值默认从该源接口上继承。





命令模式 :

 GRE隧道接口业务模式  






命令默认权限级别 :

15 






命令格式 :


tunnel source interface 
  ＜interface-name 
＞

no tunnel source interface 








命令参数解释 :



参数|描述
---|---
＜interface-name＞|用于设置隧道的源接口取值范围：1-32位的字符串。默认值：无。








缺省 :

隧道未配置源接口 






使用说明 :

配置该命令前需要先通过tunnel mode命令配置隧道模式。配置的接口必须是本地的物理接口或是通过interface命令创建的逻辑接口。如果用户通过tunnel source命令为隧道配置了源地址或通过tunnel vrf命令为隧道配置了VRF，就不能再执行tunnel source interface命令为隧道配置源接口。隧道从配置的源接口上获取到源地址与VRF值后，该隧道的源地址，目的地址以及VRF三者不能与其他隧道完全一致，否则会导致配置错误。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel mode ipZXROSNG(config-gre-if-gre_tunnel1)#tunnel source interface loopback1ZXROSNG(config-gre-if-gre_tunnel1)#no tunnel source interface





相关命令 :

configure terminalinterface gre_tunnel<tunnel no>tunnel mode ip




## tunnel source 


tunnel source 




命令功能 :

该命令工作于GRE隧道接口业务配置模式，用于为隧道配置源地址。用户使用该命令为隧道指定隧道源地址后，在隧道对报文进行封装时，隧道会将该地址作为封装后的IPv4报文或IPv6报文的源地址。





命令模式 :

 GRE隧道接口业务模式  






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
ipv4|隧道封装模式为V4，报文外层为IPv4报文，源地址为一个IPv4类型的地址，内层可以为IPv4或IPv6报文，GRE隧道为ipv4 over ipv4或者ipv6 over ipv4隧道
＜ipv4-address＞|隧道接口绑定的本地接口（可以是物理口也可是逻辑口）的地址
ipv6|隧道封装模式为V6，隧道报文外层为IPv6，源地址为一个IPv6类型的地址，内层可以为IPv4或IPv6报文，GRE隧道为ipv4 over ipv6或者ipv6 over ipv6隧道
＜ipv6-address＞|隧道接口绑定的本地接口（可以是物理口也可是逻辑口）的地址








缺省 :

隧道未配置源地址 






使用说明 :

隧道源地址配置支持ipv4和ipv6两种模式，通过本命令配置的源地址类型必须与通过tunnel mode命令配置的隧道模式相同，即当隧道模式为ip时，只能配置IPv4类型的源地址，否则会有错误提示，隧道模式为IPv6时，只能配置IPv6类型的源地址。不同隧道的基本信息配置不能重复，即通过tunnel source命令配置的源地址、通过tunnel destination命令配置的目的地址以及通过tunnel vrf命令配置的VRF，不同的GRE隧道对应的这三个配置不能完全一致，否则会有隧道冲突。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。该命令不能与tunnel source interface命令同时使用。如果用户通过tunnel source interface命令为隧道配置了接口，就无需再执行tunnel source命令为隧道配置源地址。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#gre-config ZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)#tunnel mode ipZXROSNG(config-gre-if-gre_tunnel1)#tunnel source ipv4 1.1.1.1ZXROSNG(config-gre-if-gre_tunnel1)#no tunnel source






相关命令 :

interface gre_tunnel<tunnel no>gre-configtunnel mode ip



## tunnel vrf 


tunnel vrf 




命令功能 :

该命令工作于GRE隧道接口业务模式，用于指定隧道绑定的VRF名称。本命令用于支持GRE隧道私网配置，实现GRE隧道对报文封装后的私网传输。当用户需要GRE隧道封装后的报文进入私网传输时，使用此命令。






命令模式 :

 GRE隧道接口业务模式  






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

GRE隧道不配置VPN实例 






使用说明 :

该命令配置的VRF值必须是先前通过ip vrf命令配置的vrf-name值。相关的VRF信息可以通过命令show ip vrf来查看。配置tunnel vrf时，与该隧道模式对应的该VRF的协议类型必须使能（参见ip vrf配置命令），即如果该隧道模式为ip，则该命令使用的VRF必须支持IPv4协议，而如果隧道模式为ipv6，则该命令使用的VRF必须支持IPv6协议，否则会发生配置错误。如果用户通过tunnel source interface命令为隧道配置了源接口，就不能再执行该命令为隧道配置VRF。用户使用tunnel mode命令变更隧道模式或使用no tunnel mode命令取消隧道模式时，该配置信息会自动被清除。





范例 :

ZXROSNG#configure terminalZXROSNG(config)#interface gre_tunnel1ZXROSNG(config-if-gre_tunnel1)#exitZXROSNG(config)#ip vrf sZXROSNG(config-vrf-s)#rd 100:100ZXROSNG(config-vrf-s)#address-family ipv4ZXROSNG(config-vrf-s)#!ZXROSNG(config)#gre-configZXROSNG(config-gre)#interface gre_tunnel1ZXROSNG(config-gre-if-gre_tunnel1)# tunnel vrf sZXROSNG(config-gre-if-gre_tunnel1)#no tunnel vrf





相关命令 :

interface gre_tunnel<tunnel no>gre-configip vrf <vrfname>rd <0-65535>:<0-4294967295>



# L2VPN配置命令 
## dldp 


dldp 




命令功能 :

二层协议透传控制，dldp协议报文可以透传。 






命令模式 :

 MAC-L2协议控制策略模式  






命令默认权限级别 :

15 






命令格式 :



dldp 
 tunnelled 


no dldp 








命令参数解释 :



参数|描述
---|---
tunnelled|使能透传








缺省 :

默认为不透传。 






使用说明 :

无 






范例 :

进入L2协议控制策略模式，使能dldp协议报文透传：ZXROSNG(config)#vpls zteZXROSNG(config-vpls-zte)#macZXROSNG(config-vpls-mac-zte)#l2protocol-control-policyZXROSNG(config-vpls-mac-l2protocolcontrolpolicy)#dldp tunnelledZXROSNG(config-vpls-mac-l2protocolcontrolpolicy)#





相关命令 :

l2protocol-control-policy 




## garp 


garp 




命令功能 :

二层协议透传控制，garp协议报文可以透传。 






命令模式 :

 MAC-L2协议控制策略模式  






命令默认权限级别 :

15 






命令格式 :



garp 
 tunnelled 


no garp 








命令参数解释 :



参数|描述
---|---
tunnelled|使能透传








缺省 :

默认为不透传。 






使用说明 :

无 






范例 :

进入L2协议控制策略模式，使能garp协议报文透传：ZXROSNG(config)#vpls zteZXROSNG(config-vpls-zte)#macZXROSNG(config-vpls-mac-zte)#l2protocol-control-policyZXROSNG(config-vpls-mac-l2protocolcontrolpolicy)#garp tunnelledZXROSNG(config-vpls-mac-l2protocolcontrolpolicy)#





相关命令 :

l2protocol-control-policy 




# L3VPN配置命令 
## address-family ipv4 


address-family ipv4 




命令功能 :

该命令用于激活公网VRF的IPv4地址族能力，并进入VRF-public-IPv4地址族模式。使用no命令去激活IPv4地址族能力。






命令模式 :

 VRF-public模式,VRF模式  






命令默认权限级别 :

VRF模式:15,VRF-public模式:15 






命令格式 :


address-family ipv4 
 

no address-family ipv4 








命令参数解释 :


					无
				 






缺省 :

公网VRF实例没有激活IPv4地址族的能力。 






使用说明 :

使用场景激活公网VRF的IPv4地址族能力注意事项1.必须激活至少一个地址族才能使公网VRF生效。该命令执行成功后进入VRF-public-IPv4地址族模式。






范例 :

配置公网VRF实例，激活IPv4地址族能力。ZXROSNG(config)#ip vrf-publicZXROSNG(config-public-vrf)address-family ipv4ZXROSNG(config-public-vrf-af-ipv4)#






相关命令 :

show ip vrf-public detail 




## address-family ipv6 


address-family ipv6 




命令功能 :

该命令用于激活公网VRF的IPv6地址族能力，并进入VRF-public-IPv6地址族模式。使用no命令去激活IPv6地址族能力。






命令模式 :

 VRF-public模式,VRF模式  






命令默认权限级别 :

VRF模式:15,VRF-public模式:15 






命令格式 :


address-family ipv6 
 

no address-family ipv6 








命令参数解释 :


					无
				 






缺省 :

公网VRF实例没有激活IPv6地址族的能力。 






使用说明 :

使用场景激活公网VRF的IPv6地址族能力注意事项3.必须激活至少一个地址族才能使公网VRF生效。该命令执行成功后进入VRF-public-IPv6地址族模式。






范例 :

配置公网VRF实例，激活IPv6地址族能力。ZXROSNG(config)#ip vrf-publicZXROSNG(config-public-vrf)address-family ipv6ZXROSNG(config-public-vrf-af-ipv6)#






相关命令 :

show ip vrf-public detail 




## arp generate-host-route 


arp generate-host-route 




命令功能 :

该命令工作于VRF模式，用于通知所有该VRF关联的接口上的ARP Vlink直连路由均允许生成主机路由。使用no命令恢复默认状态。 






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :



arp generate-host-route 
  [[route-map 
 ＜route-map-name 
＞]]

no arp generate-host-route 








命令参数解释 :



参数|描述
---|---
＜route-map-name＞|route-map名称取值范围:1–31个字符默认值:无








缺省 :

缺省状态该VRF关联的接口上的ARP均不允许生成主机路由。 






使用说明 :

（1）必须执行rd命令配置RD数据之后才可以配置该命令。（2）不带route-map-name参数时，对于所有该VRF关联的接口上的ARP Vlink直连路由，带route-map-name参数时，只有通过过滤的路由才允许生成主机路由。






范例 :

配置VRF实例zte，而且只有通过名为zte的route-map过滤的路由才可以生成主机路由。ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#arp generate-host-route route-map zte






相关命令 :

show ip vrf detail 




## clear l3vpn statistics 


clear l3vpn statistics 




命令功能 :

该命令用于配置指定的L3VPN类型所有业务或者具体某一业务实例持续累计的性能值清零。如果命令参数带有peer地址，该命令用于清除从指定PE邻居接收导入本地VRF的流量计数。 






命令模式 :

 特权模式  






命令默认权限级别 :

15 






命令格式 :



clear l3vpn statistics 
  [＜vrf-name 
＞ [peer 
 ＜ip-address 
＞]







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|指定清除统计信息的业务实例名称。取值范围：1-31位的字符串。默认值：无。
＜ip-address＞|IPv4地址，十进制点分形式








缺省 :

无 






使用说明 :

1.当需要对名为zte的L3VPN业务性能统计计数清零，使用以下命令：ZXROSNG#clear l3vpn statistics zteZXROSNG#2.当需要清除从10.1.1.1邻居收到导入本地名为zte的VRF路由的流量计数，使用以下命令：ZXROSNG#clear l3vpn statistics zte peer 10.1.1.1





范例 :

对名为zte的L3VPN业务性能统计计数清零：ZXROSNG#clear l3vpn statistics zteZXROSNG#






相关命令 :

VRF模式下的peer{<ip-address>} tunnel-policy <static-tunnel-policy-name> 




description :

description 




命令功能 :

该命令工作于VRF-public模式，用于配置公网VRF实例的描述信息。使用no命令可删除配置。






命令模式 :

 VRF-public模式,VRF模式  






命令默认权限级别 :

VRF模式:15,VRF-public模式:15 






命令格式 :


description 
  ＜description-of-vrf 
＞

no description 








命令参数解释 :



参数|描述
---|---
＜description-of-vrf＞|VRF实例的描述信息。取值范围：1~104位字符串，支持空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

使用场景配置公网VRF的描述信息。注意事项1.如果多次配置description命令，以最后一次的配置数据为准。2.缺省情况下，VRF实例没有配置描述信息。






范例 :

给公网VRF设置描述为“This public-vrf is create for test”：ZXROSNG(config)#ip vrf zteZXROSNG(config-public-vrf)#description This public-vrf is create for test






相关命令 :

show ip vrf-public detail 




## ds-mode 


ds-mode 




命令功能 :

该命令工作于VRF模式，用于控制MPLS（Multiprotocol Label Switching，多协议标记交换）标签的EXP和IP报文中ToS间的处理模式，缺省值为pipe模式。使用no命令恢复默认值。






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :


ds-mode 
  {uniform 
|pipe 
|short-pipe 
}

no ds-mode 








命令参数解释 :



参数|描述
---|---
uniform|和pipe、short-pipe是三选一，若设置为uniform，则表示：报文进入MPLS标签交换网，标签交换网认为其上游的IP路由网是可信的，标签中的EXP字段需要和IP报头中的ToS（Type of Service，服务类型）保持一致，即依据IP报头中的ToS字段生成标签中的EXP。报文出MPLS标签交换网，IP路由网认为标签交换网是可信的，IP报头中的ToS需要和标签中的EXP字段保持一致，即依据标签中的EXP修改IP报头中的ToS。用标签中的EXP字段作为QoS依据。
pipe|和uniform、short-pipe是三选一，若设置为pipe，则表示：报文进入MPLS标签交换网，标签交换网为上游的IP路由网提供透明的隧道服务，标签中的EXP字段固定，IP报头中的ToS保持不变。报文出MPLS标签交换网，标签交换网为下游的IP路由网提供透明的隧道服务，剥掉标签，IP报头中的ToS保持不变。用标签中的EXP字段作为QoS依据。
short-pipe|和uniform、pipe是三选一，为pipe模式的一个子模式，若设置为short-pipe，则表示：用IP报头中Pre字段作修改QoS依据。








缺省 :

缺省为pipe模式。 






使用说明 :

（1）必须执行rd命令配置RD数据之后才可以使用本命令配置。（2）在89项目中没有本命令。






范例 :

给名为zte的VRF配置ds-mode为uniform：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#ds-mode uniform 






相关命令 :

show ip vrf detail 




## equivalent-vni-label 


equivalent-vni-label 




命令功能 :

该命令工作于VRF模式，用于配置等价VNI标签。使用no命令删除该配置。 






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :


equivalent-vni-label 
  ＜L3 VNI-label 
＞
no equivalent-vni-label 
  ＜L3 VNI-label 
＞
				






命令参数解释 :



参数|描述
---|---
＜L3 VNI-label＞|EVPN三层等价VNI标签值。取值范围：1~16777215，无默认值。








缺省 :

无 






使用说明 :

（1）必须配置过RD配置该命令。（2）可配置的最多等价VNI标签个数由性能参数确定。






范例 :

在名称为zte的VRF下配置等价标签：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#equivalent-vni-label 10ZXROSNG(config-vrf-zte)#





相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn export-map 


evpn export-map 




命令功能 :

该命令用于将当前VPN实例的IPv4地址族与一条出方向的EVPN路由策略相关联。出方向路由映射可以过滤发布的路由信息以及为过滤的路由信息设置路由属性。使用no命取消当前VPN实例与出方向路由策略的关联。 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn export-map 
  ＜export-map-name 
＞

no evpn export-map 








命令参数解释 :



参数|描述
---|---
＜export-map-name＞|与VRF实例关联的出方向EVPN路由策略名称。取值范围：1-31位的字符串，不支持空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

（1）VPN实例的地址族只能与一条出方向的EVPN路由策略相关联，以最后关联的路由策略为准。（2）缺省情况下，系统没有为VPN实例IPv4地址族关联出方向的EVPN路由策略。





范例 :

1.当需要为名称是zte的VRF实例下的IPv4地址族配置一条出方向的EVPN路由策略时，使用以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)# address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#evpn export-map out_map





相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn export-map 


evpn export-map 




命令功能 :

该命令用于将当前VPN实例的IPv6地址族与一条出方向的EVPN路由策略相关联。出方向路由映射可以过滤发布的路由信息以及为过滤的路由信息设置路由属性。使用no命取消当前VPN实例与出方向路由策略的关联。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn export-map 
  ＜export-map-name 
＞

no evpn export-map 








命令参数解释 :



参数|描述
---|---
＜export-map-name＞|与VRF实例关联的出方向EVPN路由策略名称。取值范围：1-31位的字符串，不支持空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

（1）VPN实例的地址族只能与一条出方向的EVPN路由策略相关联，以最后关联的路由策略为准。（2）系统没有为VPN实例IPv6地址族关联出方向的EVPN路由策略。






范例 :

1.当需要为名称是zte的VRF实例下的IPv6地址族配置一条出方向的EVPN路由策略时，使用以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)# address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#evpn export-map out_map






相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn gw-ip inherit-nexthop 


evpn gw-ip inherit-nexthop 




命令功能 :

该命令控制VRF私网路由生成EVPN RT5G路由时，其NLRI的GW IP字段继承VRF私网路由的下一跳。 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn gw-ip inherit-nexthop 
  [[route-map 
 ＜route-map 
＞]]

no evpn gw-ip inherit-nexthop 








命令参数解释 :



参数|描述
---|---
＜route-map＞|route-map名称








缺省 :

无效 






使用说明 :

1.配置该命令后，如果VRF私网路由有原始下一跳，BGP会把VRF私网路由当做RT-5G向EVPN邻居发布，并且NLRI中的GW IP字段继承VRF私网路由的原始下一跳；2.VRF私网路由没有原始下一跳时，如果配置了evpn gw-ip命令，就使用evpn gw-ip配置的地址作为NLRI中的gw-ip字段，否则不会将该私网路由当作RT-5G路由向EVPN邻居发布。3.如果VRF私网路由有多个下一跳，则可以产生多条EVPN RT5G路由。4.如果配置了route-map，BGP只会将满足route-map条件的VRF私网路由当作EVPN RT-5G路由发布。






范例 :

当需要配置VRF私网路由生成EVPN RT5G路由时，其NLRI的GW IP字段继承VRF私网路由的下一跳时，使用以下命令:ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:2ZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#evpn gw-ip inherit-nexthop route-map rmp






相关命令 :

evpn gw-ip 




## evpn gw-ip inherit-nexthop 


evpn gw-ip inherit-nexthop 




命令功能 :

该命令控制VRF私网路由生成EVPN RT5G路由时，其NLRI的GW IP字段继承VRF私网路由的下一跳。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn gw-ip inherit-nexthop 
  [[route-map 
 ＜route-map 
＞]]

no evpn gw-ip inherit-nexthop 








命令参数解释 :



参数|描述
---|---
＜route-map＞|route-map名称








缺省 :

无效 






使用说明 :

1.配置该命令后，如果VRF私网路由有原始下一跳，BGP会把VRF私网路由当做RT-5G向EVPN邻居发布，并且NLRI中的GW IP字段继承VRF私网路由的原始下一跳；2.VRF私网路由没有原始下一跳时，如果配置了evpn gw-ip命令，就使用evpn gw-ip配置的地址作为NLRI中的gw-ip字段，否则不会将该私网路由当作RT-5G路由向EVPN邻居发布。3.如果VRF私网路由有多个下一跳，则可以产生多条EVPN RT5G路由。4.如果配置了route-map，BGP只会将满足route-map条件的VRF私网路由当作EVPN RT-5G路由发布。






范例 :

当需要配置VRF私网路由生成EVPN RT5G路由时，其NLRI的GW IP字段继承VRF私网路由的下一跳时，使用以下命令:ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:2ZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#evpn gw-ip inherit-nexthop route-map rmp






相关命令 :

evpn gw-ip 




## evpn gw-ip 


evpn gw-ip 




命令功能 :

配置EVPN的gateway IP地址，使用no命令删除配置。 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn gw-ip 
  ＜ip-address 
＞

no evpn gw-ip 








命令参数解释 :



参数|描述
---|---
＜ip-address＞|有效的IPv4地址，十进制点分形式








缺省 :

无 






使用说明 :

该命令与VRF模式下的vni-label互斥。 






范例 :

ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#evpn gw-ip 1.2.3.4





相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn gw-ip 


evpn gw-ip 




命令功能 :

配置EVPN的gateway IP地址，使用no命令删除配置。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn gw-ip 
  ＜ipv6-address 
＞

no evpn gw-ip 








命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|有效的IPv6地址，十六进制冒分形式








缺省 :

无 






使用说明 :

该命令和VRF模式下的vni-label命令互斥 






范例 :

ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#evpn gw-ip 1::1






相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn import-map 


evpn import-map 




命令功能 :

该命令用于将当前VPN实例的IPv4地址族与一条入方向的EVPN路由策略相关联。出方向路由映射可以过滤发布的路由信息以及为过滤的路由信息设置路由属性。使用no命取消当前VPN实例与入方向路由策略的关联。 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn import-map 
  ＜import-map-name 
＞

no evpn import-map 








命令参数解释 :



参数|描述
---|---
＜import-map-name＞|与VRF实例关联的入方向EVPN路由策略名称。取值范围：1-31位的字符串，不支持空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

（1）VPN实例的地址族只能与一条入方向的EVPN路由策略相关联，以最后关联的路由策略为准。（2）缺省情况下，系统没有为VPN实例IPv4地址族关联入方向的EVPN路由策略。





范例 :

1.当需要为名称是zte的VRF实例下的IPv4地址族配置一条入方向的EVPN路由策略时，使用以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)# address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#evpn import-map in_map





相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn import-map 


evpn import-map 




命令功能 :

该命令用于将当前VPN实例的IPv6地址族与一条入方向的EVPN路由策略相关联。入方向路由映射可以过滤发布的路由信息以及为过滤的路由信息设置路由属性。使用no命取消当前VPN实例与入方向路由策略的关联。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn import-map 
  ＜import-map-name 
＞

no evpn import-map 








命令参数解释 :



参数|描述
---|---
＜import-map-name＞|与VRF实例关联的入方向EVPN路由策略名称。取值范围：1-31位的字符串，不支持空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

（1）VPN实例的地址族只能与一条入方向的EVPN路由策略相关联，以最后关联的路由策略为准。（2）缺省情况下，系统没有为VPN实例IPv6地址族关联入方向的EVPN路由策略。






范例 :

1.当需要为名称是zte的VRF实例下的IPv6地址族配置一条入方向的EVPN路由策略时，使用以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)# address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#evpn import-map in_map






相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn rt-2 import-double-label 


evpn rt-2 import-double-label 




命令功能 :

该命令工作于VRF地址族模式，用于配置VRF是否导入携带双标签的EVPN RT-2类型路由。 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn rt-2 import-double-label 
  {enable 
|disable 
}

no evpn rt-2 import-double-label 








命令参数解释 :



参数|描述
---|---
enable|VRF导入带双标签的EVPN RT-2型路由
disable|VRF不导入带双标签的EVPN RT-2型路由








缺省 :

VRF导入带双标签的EVPN RT-2型路由 






使用说明 :

无 






范例 :

名称为zte的VRF控制不导入前缀为IPv4类型的EVPN双标签路由：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#evpn rt-2 import-double-label disable






相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn rt-2 import-double-label 


evpn rt-2 import-double-label 




命令功能 :

该命令工作于VRF地址族模式，用于配置VRF是否导入携带双标签的EVPN RT-2类型路由。使用no命令删除该配置。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn rt-2 import-double-label 
  {enable 
|disable 
}

no evpn rt-2 import-double-label 








命令参数解释 :



参数|描述
---|---
enable|VRF导入带双标签的EVPN RT-2型路由
disable|VRF不导入带双标签的EVPN RT-2型路由








缺省 :

VRF导入带双标签的EVPN RT-2型路由 






使用说明 :

无 






范例 :

名称为zte的VRF控制不导入前缀为IPv6类型的EVPN双标签路由：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#evpn rt-2 import-double-label disable






相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn rt-2 import-single-label 


evpn rt-2 import-single-label 




命令功能 :

该命令工作于VRF地址族模式，用于配置VRF是否导入携带单标签的EVPN RT-2类型路由。使用no命令删除该配置。 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn rt-2 import-single-label 
 

no evpn rt-2 import-single-label 








命令参数解释 :


					无
				 






缺省 :

默认VRF不导入带单标签的EVPN RT-2型路由。





使用说明 :

无 






范例 :

名称为zte的VRF使能导入前缀为IPv4类型的携带单标签的EVPN RT-2路由：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#evpn rt-2 import-single-label






相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn rt-2 import-single-label 


evpn rt-2 import-single-label 




命令功能 :

该命令工作于VRF地址族模式，用于配置VRF是否导入携带单标签的EVPN RT-2类型路由。使用no命令删除该配置。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



evpn rt-2 import-single-label 
 

no evpn rt-2 import-single-label 








命令参数解释 :


					无
				 






缺省 :

默认VRF不导入带单标签的EVPN RT-2型路由。





使用说明 :

无 






范例 :

名称为zte的VRF使能导入前缀为IPv6类型的携带单标签的EVPN RT-2路由：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#evpn rt-2 import-single-label






相关命令 :

show ip vrf detail [<vrf-name>] 




## evpn tunnel-encapsulation 


evpn tunnel-encapsulation 




命令功能 :

该命令工作于VRF模式，用于配置EVPN 隧道封装类型。使用no命令删除该配置。 






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :



evpn tunnel-encapsulation 
  {mpls 
|vxlan 
|vxlan-vni-symmetric 
|srv6 
|by-peer 
|by-peer-vni-symmetric 
}

no evpn tunnel-encapsulation 








命令参数解释 :



参数|描述
---|---
mpls|MPLS隧道封装
vxlan|VXLAN隧道封装，默认值。
vxlan-vni-symmetric|VNI对称的VXLAN隧道封装
srv6|SRv6隧道封装类型
by-peer|通过BGP邻居的配置设置EVPN路由的隧道封装属性类型。
by-peer-vni-symmetric|通过BGP邻居的配置设置EVPN路由的隧道封装属性类型，并且使能VNI对称功能。








缺省 :

VXLAN隧道封装 






使用说明 :

（1）    必须配置过RD配置该命令。 






范例 :

在名称为zte的VRF下配置EVPN路由为MPLS封装：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#evpn tunnel-encapsulation mplsZXROSNG(config-vrf-zte)#
在名称为zte的VRF下根据BGP邻居的配置设置EVPN路由的隧道封装属性类型：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#evpn tunnel-encapsulation by-peerZXROSNG(config-vrf-zte)#






相关命令 :

show ip vrf detail [<vrf-name>] 




## export map 


export map 




命令功能 :

该命令工作于VRF-IPv4地址族模式和VRF-IPv6地址族模式，用于将当前VPN实例的地址族与一条出方向的路由策略相关联。使用no命取消当前VPN实例与出方向路由策略的关联。当要求比采用扩展团体属性方式更精确地控制发布的VPN实例IPv4/IPv6地址族路由时，可以使用出方向路由映射。出方向路由映射可以过滤发布的路由信息以及为过滤的路由信息设置路由属性。





命令模式 :

 VRF-IPv4地址族模式,VRF-IPv6地址族模式  






命令默认权限级别 :

VRF-IPv4地址族模式:15,VRF-IPv6地址族模式:15 






命令格式 :


export map 
  ＜export-map-name 
＞

no export map 








命令参数解释 :



参数|描述
---|---
＜export-map-name＞|与VRF实例关联的出方向路由策略名称。取值范围：1~31位的字符串，不支持空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

（1）VPN实例的地址族只能与一条出方向的路由策略相关联，以最后关联的路由策略为准。（2）缺省情况下，系统没有为VPN实例相应地址族关联出方向的路由策略。





范例 :

将zte的IPv4地址族与出方向路由策略outmap相关联：ZXROSNG(config)#ip vrf zte ZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#export map outmapZXROSNG(config-vrf-zte-af-ipv4)#






相关命令 :

show ip vrf detail 




## gr 


gr 




命令功能 :

该命令工作于“全局配置模式”下，用于使能/去使能支撑模块路由、隧道转发表的GR功能。GR是Graceful Restart（优雅重启） 的简称。该命令用于GR主备倒换时。设备主备倒换后，新主启动，协议需要迅速重新建链交互协议报文，建链需要利用到达邻居的路由转发表和隧道转发表。因此，在主备倒换前，需要在主设备上使能GR命令，支撑会把路由转发表和隧道转发表备份到备板的数据库中，当协议建链需要用到路由转发表和隧道转发表时，直接从数据库中查询即可。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


gr 
  {enable 
|disable 
}






命令参数解释 :



参数|描述
---|---
enable|<作用> 使能支撑模块路由、隧道转发表GR功能<取值范围> 常量，固定为enable<默认值>  无
disable|<作用> 去使能支撑模块路由、隧道转发表GR功能<取值范围> 常量，固定为disable<默认值>  无








缺省 :

命令的默认使能、去使能状态可以使用性能参数控制。性能参数的编号为67240117，性能参数定制为1，表示设备启动后，GR默认是使能的；若性能参数定制为0，则GR默认是去使能的。 






使用说明 :

使用场景当用户需要使能/去使能支撑模块路由、隧道转发表的GR功能，可以执行该命令注意事项1、命令的默认使能、去使能状态可以使用性能参数控制。性能参数的编号为67240117，性能参数定制为1，表示设备启动后，GR默认是使能的，可以显式通过命令gr disable关掉，若性能参数定制为0，则GR默认是去使能的。性能参数的默认值定制为0。在去使能的状态下，可以显式通过命令gr enable 打开。2、GR功能打开后，主板会向备板同步路由转发表和隧道转发表，会占用一些的系统资源，占用情况视路由和隧道的数量来计量，不过一般可以忽略不计。





范例 :

使能GR功能：ZXROSNG(config)#gr ?  disable  Disable GR  enable   Enable GRZXROSNG(config)#gr enable去使能GR功能：ZXROSNG(config)#gr ?  disable  Disable GR  enable   Enable GRZXROSNG(config)#gr disable  查询GR使能状态(使能)：ZXROSNG(config)#show running-config lspm all    !<pss-lspm>gr enable!</pss-lspm>
查询GR使能状态(不使能)：ZXROSNG(config)#show running-config lspm all    !<pss-lspm>#gr disable!</pss-lspm>






相关命令 :

无。 




## import map 


import map 




命令功能 :

该命令工作于VRF-IPv4地址族模式和VRF-IPv6地址族模式，用于将当前VPN实例的地址族与一条入方向的路由策略相关联。使用no命令取消当前VPN实例与入方向路由策略的关联。当要求比采用扩展团体属性方式更精确地控制引入VPN实例路由时，可以采用入方向路由映射。入方向路由映射可以过滤引入的路由信息以及为过滤的路由信息设置路由属性。






命令模式 :

 VRF-IPv4地址族模式,VRF-IPv6地址族模式  






命令默认权限级别 :

VRF-IPv6地址族模式:15,VRF-IPv4地址族模式:15 






命令格式 :


import map 
  ＜import-map-name 
＞

no import map 








命令参数解释 :



参数|描述
---|---
＜import-map-name＞|与VRF实例关联的入方向的路由策略名称。取值范围：1~31位的字符串，不支持空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

（1）VPN实例的地址族只能与一条入方向的路由策略相关联，以最后关联的路由策略为准。（2）入方向路由映射没有缺省值，如果不配置，则允许所有Route Target属性匹配的路由加入VPN实例路由表。





范例 :

将zte的IPv4地址族与入方向的路由策略inmap相关联：ZXROSNG(config)#ip vrf zte ZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#import map inmapZXROSNG(config-vrf-zte-af-ipv4)#






相关命令 :

show ip vrf detail 




## import multicast-route 


import multicast-route 




命令功能 :

该命令工作于VRF-IPv4地址族模式，用于设置组播VPN专用的控制路由导入的Route Target。使用no命令删除配置。该命令工作的原理如下：拓扑结构：PE1----PE2PE1上某一VPN实例下配置组播导入Route target。PE1通过BGP协议向PE2通告相应的路由时会携带这一属性，PE2上的组播路由在向PE1通告前会查询是否有对应的组播导入Route Target，有的话则携带这一属性。当PE1从PE2接收组播路由时，会根据本地的组播导入Route Target和组播路由携带的组播导入Route Target决定这些路由是否可以导入对应的VRF路由表。






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :


import multicast-route 
 A.B.C.D:<0-65535> 


no import multicast-route 








命令参数解释 :



参数|描述
---|---
A.B.C.D:<0-65535>|控制组播VPN路由导入的Route Target。取值范围：冒号前的ip地址必须为有效单播地址。默认值：无。








缺省 :

无 






使用说明 :

（1）冒号前的IP地址必须为有效单播地址。（2）与单播Route Target不同，组播Route Target仅可以配置一个。






范例 :

给名称为zte的VPN的IPv4地址族设置组播VPN路由导入Route Target：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#import multicast-route 1.2.3.4:5ZXROSNG(config-vrf-zte-af-ipv4)#






相关命令 :

show ip vrf detail 




## import multicast-route 


import multicast-route 




命令功能 :

该命令工作于VRF-IPv6地址族模式，用于设置组播VPN专用的控制路由导入的Route Target。使用no命令删除配置。该命令工作的原理如下：拓扑结构：PE1----PE2 PE1上某一VPN实例下配置组播导入Route target。PE1通过BGP协议向PE2通告相应的路由时会携带这一属性，PE2上的组播路由在向PE1通告前会查询是否有对应的组播导入Route Target，有的话则携带这一属性。当PE1从PE2接收组播路由时，会根据本地的组播导入Route Target和组播路由携带的组播导入Route Target决定这些路由是否可以导入对应的VRF路由表。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :


import multicast-route 
 A.B.C.D:<0-65535> 


no import multicast-route 








命令参数解释 :



参数|描述
---|---
A.B.C.D:<0-65535>|控制组播VPN路由导入的Route Target。取值范围：冒号前的ip地址必须为有效单播地址。默认值：无。








缺省 :

无 






使用说明 :

（1）冒号前的IP地址必须为有效单播地址。（2）与单播Route Target不同，组播Route Target仅可以配置一个。






范例 :

给名称为zte的VPN的IPv6地址族设置组播VPN路由导入Route Target：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#import multicast-route 2.3.4.5:6ZXROSNG(config-vrf-zte-af-ipv6)#






相关命令 :

show ip vrf detail 




## ip frr 


ip frr 




命令功能 :

在VPN实例下存在多种路由协议生成的私网路由时，通过配置该命令使能私网协议路由间的IP FRR功能，以实现异种路由协议或同种协议间的路由保护，当主路径发生异常后能够快速切换，以保证报文顺畅转发。 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



ip frr 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能私网路由FRR功能
disable|不使能私网路由FRR功能








缺省 :

不使能私网路由FRR功能。 






使用说明 :

使用场景VPN实例下的多个CE接入到同一台PE上时，配置私网路由FRR特性，当PE去往CE主路由的下一跳不可达时，可以快速将流量切换到另一条PE与CE相连的链路上。






范例 :

需要配置私网路由的frr功能时，需要进行如下配置：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#ip frr enable






相关命令 :

ip frr-wtr 




## ip frr 


ip frr 




命令功能 :

在VPN实例下存在多种路由协议生成的私网路由时，通过配置该命令使能私网协议路由间的IP FRR功能，以实现异种路由协议或同种协议间的路由保护，当主路径发生异常后能够快速切换，以保证报文顺畅转发。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



ip frr 
  {enable 
|disable 
}







命令参数解释 :



参数|描述
---|---
enable|使能私网路由FRR功能
disable|不使能私网路由FRR功能








缺省 :

不使能私网路由FRR功能。 






使用说明 :

使用场景VPN实例下的多个CE接入到同一台PE上时，配置私网路由FRR特性，当PE去往CE主路由的下一跳不可达时，可以快速将流量切换到另一条PE与CE相连的链路上。






范例 :

需要配置私网路由的frr功能时，需要进行如下配置：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#ip frr enable






相关命令 :

ip frr-wtr 




## ip frr-wtr 


ip frr-wtr 




命令功能 :

该命令为VRF配置WTR（等待时间间隔），当网络故障消失后，需要将流量从备份路径切换回原有的主路径，回切流量时需要按照WTR时间延迟后再回切。 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



ip frr-wtr 
  [＜wtr 
＞]

no ip frr-wtr 








命令参数解释 :



参数|描述
---|---
＜wtr＞|等待时间间隔取值范围:1 ~ 12，单位为分钟默认值:5分钟








缺省 :

无 






使用说明 :

使用场景VPN实例下的多个CE接入到同一台PE上时，配置私网路由FRR特性，当PE去往CE主路由的下一跳不可达时，可以快速将流量切换到另一条PE与CE相连的链路上，当原有网络故障消失后，需要将流量从备份路径切换回原有的主路径，回切流量时可以按照配置的WTR时间延迟后再回切。注意事项：必须配置ip frr enable该功能才能生效。






范例 :

需要配置私网路由的frr 回切时间为7分钟，需要进行如下配置：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#ip frr-wtr 7





相关命令 :

ip frr {enable | disable} 




## ip frr-wtr 


ip frr-wtr 




命令功能 :

该命令为VRF配置WTR（等待时间间隔），当网络故障消失后，需要将流量从备份路径切换回原有的主路径，回切流量时需要按照WTR时间延迟后再回切。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



ip frr-wtr 
  [＜wtr 
＞]

no ip frr-wtr 








命令参数解释 :



参数|描述
---|---
＜wtr＞|等待时间间隔取值范围:1 ~ 12，单位为分钟默认值:5分钟








缺省 :

无 






使用说明 :

使用场景VPN实例下的多个CE接入到同一台PE上时，配置私网路由FRR特性，当PE去往CE主路由的下一跳不可达时，可以快速将流量切换到另一条PE与CE相连的链路上，当原有网络故障消失后，需要将流量从备份路径切换回原有的主路径，回切流量时可以按照配置的WTR时间延迟后再回切。注意事项：必须配置ip frr enable该功能才能生效。






范例 :

需要配置私网路由的frr 回切时间为7分钟，需要进行如下配置：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#ip frr-wtr 7






相关命令 :

ip frr {enable | disable} 




## ip rd-list trigger-delay 


ip rd-list trigger-delay 




命令功能 :

设置路由标识列表同步到应用的延迟时间。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ip rd-list trigger-delay 
  ＜delay-time 
＞

no ip rd-list trigger-delay 








命令参数解释 :



参数|描述
---|---
＜delay-time＞|延迟时间，范围0-30(单位：秒)








缺省 :

默认10秒。 






使用说明 :

1、应用协议（如BGP等）引用路由标识列表后，当路由标识列表创建、更新，会同步到对应的应用协议。同步会有一定延时，可以通过本命令调整延时时间。2、本配置针对所有路由标识列表实例生效。






范例 :

设置路由标识列表同步延迟时间为20秒：ZXROSNG(config)#ip rd-list trigger-delay 20






相关命令 :

show ip rd-list  




## ip rd-list 


ip rd-list 




命令功能 :

给BGP创建一个路由标识列表且控制对它的访问。使用no命令路由标识列表。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ip rd-list 
  {＜rd-list-number 
＞ {deny 
|permit 
} *({<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
})|＜rd-list-number 
＞ {deny 
|permit 
} ＜regular-expression 
＞}
no ip rd-list 
  {＜rd-list-number 
＞ [{deny 
|permit 
} {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}]|＜rd-list-number 
＞ [{deny 
|permit 
} ＜regular-expression 
＞]}
				






命令参数解释 :



参数|描述
---|---
＜rd-list-number＞|RD过滤器的编号，整数形式，取值范围是1～99。
deny|不允许对匹配条件进行访问。
permit|允许对匹配条件进行访问。
<0-65535>:<0-4294967295>|路由标识值，<aa>:<nnnn>类型，<aa>的取值范围：0-65535,<nnnn>的取值范围：0-4294967295。
A.B.C.D:<0-65535>|路由标识值，A.B.C.D : <aa>类型，A.B.C.D IP地址，十进制点分形式, <aa>的取值范围：0-65535。
<1-65535>.<0-65535>:<0-65535>|路由标识值，<aa>.<nn>:<kk>  <aa>的取值范围：1-65535,<nn>的取值范围：0-65535, <kk>的取值范围：0-65535。
＜rd-list-number＞|RD过滤器的编号，整数形式，取值范围是100～500。
deny|不允许对匹配条件进行访问。
permit|允许对匹配条件进行访问。
＜regular-expression＞|在路由标识表中使用正则表达式的自治系统。








缺省 :

无 






使用说明 :

配置重复值会过滤重复。 






范例 :

ZXROSNG(config)#ip rd-list 1 permit 1:1 1.2:3 1.2.3.4:5ZXROSNG(config)#show ip rd-list 1ip rd-list 1  permit  1:1  permit  1.2:3  permit  1.2.3.4:5






相关命令 :

show ip rd-list [<rd-list-number>] 




## ip vrf 


ip vrf 




命令功能 :

该命令工作于全局模式下，用于创建指定vpnid的VRF实例，执行成功后进入VRF模式。使用no命令删除指定的VRF实例。






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


ip vrf 
  ＜vrf-name 
＞ vpnid 
 ＜vpnid 
＞
no ip vrf 
  ＜vrf-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF实例名称，用于标识一个VRF实例。该名称只在本地有效，在某个接口与VPN绑定时用到该名称。取值范围：1~32位字符串，不包含空格，区分大小写。
＜vpnid＞|VRF实例的vpnid，可标识一个VRF实例。取值范围：1-$#117637121#$（目前XGW版本支持的最大值是4095，最大值可变化，由性能参数控制）；默认值：无。








缺省 :

无 






使用说明 :

（1）名称为“mng”的VRF在单板上电过程中自动生成，不能对此VRF的配置数据进行修改和删除。（2）此命令执行成功后即创建一个VRF实例，并进入VRF模式。（3）VRF实例创建成功后，需为该VRF配置RD（Route Distinguisher，路由标识符）。（4）VRF实例下支持IPv4地址族和IPv6地址族。配置ip vrf命令后，系统根据转发VPN路由的协议类型，运行命令address-family ipv4或者address-family ipv6激活相应的地址族能力，并在相应的地址族下进行VRF的相关配置。（5）xGW网元支持配置的VRF最大数目为4095个（可能发生变化，由性能参数控制）。（6）不同VRF的vpnid不同；（7）VRF的vpnid在指定后将不能修改，若要修改只能删除后重新配置。






范例 :

创建一个名为zte，vpnid为100的VPN：ZXROSNG(config)#ip vrf zte vpnid 100ZXROSNG(config-vrf-zte)#






相关命令 :

show ip vrfshow ip vrf briefshow ip vrf detail




## ip vrf-public 


ip vrf-public 




命令功能 :

在设备上配置公网VRF。使用no命令删除该VRF。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



ip vrf-public 
 

no ip vrf-public 








命令参数解释 :


					无
				 






缺省 :

无公网VRF。 






使用说明 :

使用场景Global-MVPN场景中，配置公网VRF参数。






范例 :

Global-MVPN场景中，需要配置公网VRF相关参数，需要如下配置：ZXROSNG(config)#ip vrf-publicZXROSNG(config-public-vrf)#






相关命令 :

show ip vrf-public detail 




## l3vpn-statistics 


l3vpn-statistics 




命令功能 :

该命令工作于全局配置模式，用于配置指定的L3VPN类型所有业务或者具体某一业务实例的统计状态。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



l3vpn-statistics 
  {enable 
|disable 
} [＜vrf-name 
＞]







命令参数解释 :



参数|描述
---|---
enable|和disable是二选一，若设置为enable，则表示开启L3VPN业务的性能统计功能。
disable|和enable是二选一，若设置为disable，则表示关闭L3VPN业务的性能统计功能。
＜vrf-name＞|用于指定配置的L3VPN业务实例名称。取值范围：1~32位的字符串，不包含空格，区分大小写。默认值：无。不指定L3VPN业务实例名称则表示配置L3VPN业务全局统计状态。








缺省 :

关闭L3VPN所有业务的性能统计功能。 






使用说明 :

（1）新创建的VPN实例默认继承全局统计状态。（2）配置全局统计状态后会使所有实例统计状态与全局状态一致。（3）具体业务实例的统计状态以全局配置和指定实例配置中最后配置的状态生效。






范例 :

开启名为zte的L3VPN业务的性能统计功能：ZXROSNG(config)#l3vpn-statistics enable zteZXROSNG(config)#






相关命令 :

show l3vpn-statistics status 




## maximum routes 


maximum routes 




命令功能 :

该命令工作于VRF-IPv4地址族模式和VRF-IPv6地址族模式，用于限制VRF实例地址族支持的最多路由数并给出相应的告警信息，超过最大路由数时关闭超限路由对应的协议连接，以避免PE设备因从CE和其他PE接收过多的路由而导致PE内存耗尽以及路由器崩溃。 






命令模式 :

 VRF-IPv4地址族模式,VRF-IPv6地址族模式  






命令默认权限级别 :

VRF-IPv6地址族模式:15,VRF-IPv4地址族模式:15 






命令格式 :



maximum routes 
  ＜maximum-number-of-routes 
＞ {＜warning-percent 
＞ [shutdown 
]|warning-only 
}

no maximum routes 








命令参数解释 :



参数|描述
---|---
＜maximum-number-of-routes＞|用于设置VRF路由表允许的路由上限。取值范围：1~4294967295。默认值：无。
＜warning-percent＞|此选项与warning-only是二选一，表示路由数目告警百分比，当VRF路由表中的路由数目与VRF路由表允许的最大路由数目的百分比第一次达到或者超过此参数值时，系统会给出告警提示。取值范围：1~100。
shutdown|此选项在warning-percent后是可选的，设置为在VRF路由表中路由总数达到或者超过上限时，关闭该路由来源的协议连接，目前只支持BGP协议。
warning-only|此选项与warning-percent是二选一，设置为此选项表示在VRF路由表中路由总数第一次达到或者超过上限时，系统给出一次告警提示，此后可以继续向VRF路由表中添加路由，系统不会再次给出告警提示。








缺省 :

允许路由的最大上限缺省为4294967295。 






使用说明 :

（1）配置为warning-percent（路由告警百分比）的情况下，在VRF路由表中路由条目数第一次达到或者超过告警百分比时，系统给出路由达到告警限额的提示，此后可以继续正常添加路由直到路由总数达到路由数目上限时，系统给出路由总数超限的告警提示；执行no命令取消路由表限制后，对于之前的超限的路由：     a.对于超限的静态路由，需要手动重新配置。    b.通过IGP路由协议从CE学到的路由，需要在PE上重启路由协议。    c.通过MP-IBGP学到的路由和从CE上学来的BGP路由，系统可以自动刷新。（2）配置为warning-only的情况下，在VRF路由表中路由总数第一次达到或者超过路由数目上限时给出告警提示，此后可以继续向VRF路由表中添加路由，系统不会再次给出告警提示。（3）不配置这一命令时VRF路由表的路由数目上限是4294967295。（4）同时配置了shutdown参数时，在VRF路由表的路由数目达到或超过最大路由数目时，若超限路由为BGP路由，则关闭该路由来源的BGP邻居连接。






范例 :

控制进入VRF的IPv6路由表的最大路由数目为1000条，并且在VRF路由表的路由数目达到最大路由数目的75%时发出告警，在VRF路由表的路由数目达到或超过最大路由数目时，关闭导致超限的路由协议连接，目前只支持BGP协议，命令应设置为：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#maximum routes 1000 75 shutdownZXROSNG(config-vrf-zte-af-ipv6)#






相关命令 :

show ip vrf detail 




## mpls label mode 


mpls label mode 




命令功能 :

该命令工作于VRF模式，用于设置VPN路由的私网标签分配方式。使用no命令删除配置。






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :


mpls label mode 
  [ipv6 
] {per-vrf 
|per-prefix 
}
no mpls label mode 
  [ipv6 
]
				






命令参数解释 :



参数|描述
---|---
ipv6|表示仅对IPv6地址族有效。
per-vrf|和per-prefix是二选一，若设置为per-vrf，则表示为每个VPN实例分配一个标签。
per-prefix|和per-vrf是二选一，若设置为per-prefix，则表示为每一条路由分配一个标签，全局模式下默认为per-prefix。








缺省 :

VRF配置模式下缺省时，默认继承全局模式下的配置。 






使用说明 :

（1）本命令在VRF模式下需要执行rd命令配置RD数据之后才可以配置。（2）本命令在全局模式下的配置对所有的VRF生效，在VRF模式下的配置仅对此VRF有效，VRF模式下的配置优先级高于全局模式下的配置。（3）全局模式下缺省时，默认为per-prefix；VRF模式下缺省时，默认使用全局模式下的配置。（4）携带可选参数ipv6表示仅对IPv6地址族有效，不携带可选参数ipv6表示仅对IPv4地址族有效。





范例 :

设置名称为zte的VPN私网标签分配方式为每VRF分配标签。ZXROSNG(config)#ip vrf zte ZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#mpls label mode per-vrfZXROSNG(config-vrf-zte)#






相关命令 :

show ip vrf detail 




## mpls label mode 


mpls label mode 




命令功能 :

该命令工作于全局配置模式，用于设置VPN路由的私网标签分配方式。使用no命令删除配置。






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


mpls label mode 
  [ipv6 
] {per-vrf 
|per-prefix 
}
no mpls label mode 
  [ipv6 
]
				






命令参数解释 :



参数|描述
---|---
ipv6|表示仅对IPv6地址族有效。
per-vrf|和per-prefix是二选一，若设置为per-vrf，则表示为每个VPN实例分配一个标签。
per-prefix|和per-vrf是二选一，若设置为per-prefix，则表示为每一条路由分配一个标签，全局模式下默认为per-prefix。








缺省 :

全局模式下缺省时，默认为每前缀分配标签；





使用说明 :

（1）本命令在全局模式下的配置对所有的VRF生效，在VRF模式下的配置仅对此VRF有效，VRF模式下的配置优先级高于全局模式下的配置。（2）全局模式下缺省时，默认为per-prefix；VRF模式下缺省时，默认使用全局模式下的配置。（3）携带可选参数ipv6表示仅对IPv6地址族有效，不携带可选参数ipv6表示仅对IPv4地址族有效。





范例 :

设置所有的VPN私网标签分配方式为每VRF分配标签。ZXROSNG(config)#mpls label mode per-vrf ZXROSNG(config)#






相关命令 :

show ip vrf detail 




## nat-type 


nat-type 




命令功能 :

该命令用于配置VRF是否对分发标签的流量做NAT转换。使用no命令恢复默认配置。






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :


nat-type 
  {inside 
|none 
}

no nat-type 








命令参数解释 :



参数|描述
---|---
inside|和none是二选一，若设置为inside，则表示对VRF中分发标签的流量做NAT转换。
none|和inside是二选一，若设置为none，表示对VRF中分发标签的流量不做NAT转换。








缺省 :

缺省为none，对VRF中分发标签的流量不做NAT转换。 






使用说明 :

必须执行rd命令配置RD数据之后才可以使用本命令配置。 






范例 :

设置对名为zte的VRF分发标签的流量做NAT处理：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)# nat-type insideZXROSNG(config-vrf-zte)#   





相关命令 :

show ip vrf detail 




## nd generate-host-route 


nd generate-host-route 




命令功能 :

该命令工作于VRF模式，用于通知所有该VRF关联的接口上的ND直连路由均允许生成主机路由。使用no命令恢复默认状态。 






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :



nd generate-host-route 
  [[route-map 
 ＜route-map-name 
＞]]

no nd generate-host-route 








命令参数解释 :



参数|描述
---|---
＜route-map-name＞|route-map名称取值范围:1–31个字符默认值:无








缺省 :

缺省状态该VRF关联的接口上的ARP均不允许生成主机路由。 






使用说明 :

（1）必须执行rd命令配置RD数据之后才可以配置该命令。（2）不带route-map-name参数时，对于所有该VRF关联的接口上的ARP Vlink直连路由，带route-map-name参数时，只有通过过滤的路由才允许生成主机路由。






范例 :

配置VRF实例zte，而且只有通过名为zte的route-map过滤的路由才可以生成主机路由。ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#nd generate-host-route route-map zte






相关命令 :

show ip vrf detail 




## peer &amp;lt;mid&amp;gt; tunnel-policy 


peer <mid> tunnel-policy 




命令功能 :

该命令工作于VRF-IPv4地址族模式，用于指定从PE邻居接收导入本地的VPN路由流量所走的外层隧道。使用no命令删除。






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :


peer  
 {＜ip-address 
＞} tunnel-policy 
  ＜static-tunnel-policy-name 
＞

no peer  
 {＜ip-address 
＞} tunnel-policy 








命令参数解释 :



参数|描述
---|---
＜ip-address＞|导入本地的VPN路由流量的源IP地址。取值范围：有效单播地址均可配置，一般是PE邻居地址。默认值：无。
＜static-tunnel-policy-name＞|取值含义：隧道策略名称。取值范围：1~63位的字符串，不包含空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

指定的隧道策略名称必须是已经存在的，如果不存在，可在全局模式下使用tunnel-policy命令创建。 






范例 :

指定从地址为1.2.3.4的PE邻居导入本地的VPN流量走名为abc的外层隧道：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#peer 1.2.3.4 tunnel-policy abc





相关命令 :

show ip vrf detail 




## peer &amp;lt;mid&amp;gt; tunnel-policy 


peer <mid> tunnel-policy 




命令功能 :

该命令工作于VRF-IPv6地址族模式，用于指定VPN路由流量所走的外层隧道，使用no命令删除； 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



peer  
 {＜ipv6-address 
＞} tunnel-policy 
  ＜static-tunnel-policy-name 
＞

no peer  
 {＜ipv6-address 
＞} tunnel-policy 








命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|邻居的IPv6地址， 十六进制冒分形式；
＜static-tunnel-policy-name＞|隧道策略名称，长度1-63个字符








缺省 :

无 






使用说明 :

只能指定已经存在的隧道策略，且邻居IPv6地址不能为IPv4地址映射的IPv6地址。 






范例 :

ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#peer 1::1 tunnel-policy abcdef





相关命令 :

show ip vrf detail 




## priority 


priority 




命令功能 :

该命令工作于VRF-IPv4地址族模式，用于设置VPN路由收敛优先级。使用no命令恢复VPN路由默认的收敛优先级。






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :


priority 
  ＜priority-of-convergence 
＞

no priority 








命令参数解释 :



参数|描述
---|---
＜priority-of-convergence＞|用于配置VPN路由收敛的优先级。取值范围：1~3；3为高优先级，2为中优先级（默认），1为低优先级。默认值：2。








缺省 :

默认VPN路由收敛优先级为中优先级。 






使用说明 :

配置值越大表示优先级越高。 






范例 :

给名为zte的VPN设置高路由收敛优先级：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#priority 3ZXROSNG(config-vrf-zte-af-ipv4)#






相关命令 :

show ip vrf detail 




## protection local-prefixes 


protection local-prefixes 




命令功能 :

该命令工作于VRF-IPv4地址族模式，用于打开同一个VRF的CE侧和PE侧路由形成FRR（Fast ReRoute，快速重路由）关系的开关。使用no命令恢复默认配置。






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :


protection local-prefixes 
 

no protection local-prefixes 








命令参数解释 :


					无
				 






缺省 :

默认同一个VRF的CE侧和PE侧路由形成FRR关系的开关是关闭的。 






使用说明 :

缺省情况下同一个VRF的CE侧和PE侧路由形成FRR关系的开关是关闭的。 






范例 :

打开名称为zte的VRF的CE侧和PE侧路由FRR关系的开关：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#protection local-prefixesZXROSNG(config-vrf-zte-af-ipv4)#






相关命令 :

show ip vrf detail 




## rd 


rd 




命令功能 :

该命令工作于VRF-public模式，用于为VPN实例配置RD（Route Distinguisher，路由标识符）。 






命令模式 :

 VRF-public模式,VRF模式  






命令默认权限级别 :

VRF模式:15,VRF-public模式:15 






命令格式 :



rd 
  {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}







命令参数解释 :



参数|描述
---|---
<0-65535>:<0-4294967295>|ASN_NN格式的路由标识符。取值范围：16位自治系统号:32位用户自定义数，例如：100:3。自治系统号的取值范围是0～65535；用户自定义数的取值范围是0～4294967295。默认值：无。
A.B.C.D:<0-65535>|IPADD_NN格式的路由标识符。取值范围：32位IP地址:16位用户自定义数，例如：192.168.155.20:1。IP地址的取值范围是0.0.0.0～255.255.255.255；用户自定义数的取值范围是0～65535。默认值：无。
<1-65535>.<0-65535>:<0-65535>|ASND_NN格式的路由标识符。取值范围：32位自治系统号:16位用户自定义数字，例如：100.3:1。32位自治系统号通常写成x.y的形式，即1～65535.0～65535；用户自定义数的取值范围是0～65535。默认值：无。








缺省 :

没有路由标识符。 






使用说明 :

（1）公网VRF的RD为0:0，不可更改。 






范例 :

公网VRF的RD固定为0:0：ZXROSNG(config)#ip vrf-publicZXROSNG(config-public-vrf)#rd 0:0





相关命令 :

show ip vrf-public detail  




## route-target 


route-target 




命令功能 :

该命令工作于VRF模式、VRF-IPv4地址族模式和VRF-IPv6地址族模式，用于创建一个或多个与VRF关联的Route Target扩展团体属性。使用no命令删除配置。通过Route Target可以控制VPN站点之间的路由发布。（1）当PE根据VPN实例IPv4/IPv6地址族向其他PE发送路由时，它将向发送的路由附加export Route Target。（2）当PE从其他PE接收路由时，它根据本地的import Route Target和接收的export Route Target决定这些路由是否可以被添加到相应的VPN实例IPv4/IPv6地址族中。（3）当PE根据VPN实例IPv4/IPv6地址族向其他PE发送L3EVPN路由时，它将向发送的路由附加evpn export Route Target。（4）当PE从其他PE接收L3EVPN路由时，它根据本地的evpn import Route Target和接收的evpn export Route Target决定这些路由是否可以被添加到相应的VPN实例IPv4/IPv6地址族中。






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :


route-target 
  [{both 
|export 
|import 
}] {<0-65535>:<0-4294967295> 
|<1-65535>.<0-65535>:<0-65535> 
|A.B.C.D:<0-65535> 
} [{vpn 
|evpn 
}]
no route-target 
  [{both 
|export 
|import 
}] [{<0-65535>:<0-4294967295> 
|<1-65535>.<0-65535>:<0-65535> 
|A.B.C.D:<0-65535> 
}]
				






命令参数解释 :



参数|描述
---|---
both|和export、import是三选一，若设置为both，则表示指定添加route-target扩展团体属性到VPN实例入方向和出方向的扩展团体属性列表中，等同于同时配置import和export。如果不指定关键字，则缺省值为both。
export|和both、import是三选一，若设置为export，则表示导出VRF路由携带route-target扩展团体属性。
import|和both、export是三选一，若设置为import，则表示根据route-target扩展团体属性导入路由到VRF。
<0-65535>:<0-4294967295>|ASN_NN格式的Route Target扩展团体属性。取值范围：16位自治系统号:32位用户自定义数，例如：100:3。自治系统号的取值范围是0～65535；用户自定义数的取值范围是0～4294967295。默认值：无。
<1-65535>.<0-65535>:<0-65535>|ASND_NN格式的Route Target扩展团体属性。取值范围：32位自治系统号:16位用户自定义数字，例如：100.3:1。32位自治系统号通常写成x.y的形式，即1～65535.0～65535；用户自定义数的取值范围是0～65535。默认值：无。
A.B.C.D:<0-65535>|IPADD_NN格式的Route Target扩展团体属性。取值范围：32位IP地址:16位用户自定义数，例如：192.168.155.20:1。IP地址的取值范围是0.0.0.0～255.255.255.255；用户自定义数的取值范围是0～65535。默认值：无。
vpn|表示route-target用于L3VPN路由的发布和接收
evpn|表示route-target用于L3EVPN路由的发布和接收








缺省 :

VRF没有相关的Route Target扩展团体属性。 






使用说明 :

（1）必须通过rd命令配置过RD数据之后才可以使用本命令配置。（2）VRF-IPv4地址族模式和VRF-IPv6地址族模式的Route Target配置分别在对应的地址族下生效。（3）VRF模式下的Route Target配置可以在IPv4地址族下生效，也可以在IPv6地址族下生效，VRF-IPv4地址族模式和VRF-IPv6地址族模式的配置优先级高于VRF模式下的配置，也就是当且仅当两种地址族模式下没有配置Route Target时才使用VRF模式下的配置。（4）同一个VRF的不同配置模式下入向和出向Route Target每种最多可以配置255个。（5）route-target如果不携带vpn或者evpn可选参数，表示同时用于L3VPN和L3EVPN路由的接收和发布。






范例 :

为VPN实例zte的入方向route-target列表添加3:3，出方向route-target列表添加4:4：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf)#rd 1:1ZXROSNG(config-vrf)#route-target import 3:3ZXROSNG(config-vrf)#route-target export 4:4（2）为VPN实例zte的入方向route-target列表添加1:1用于L3VPN路由接收，出方向route-target列表添加1:1用于L3EVPN路由发布：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf)#rd 1:1ZXROSNG(config-vrf)#route-target import 1:1 vpnZXROSNG(config-vrf)#route-target export 1:1 evpn






相关命令 :

show ip vrf detail 




## route-target 


route-target 




命令功能 :

该命令工作于VRF模式、VRF-IPv4地址族模式和VRF-IPv6地址族模式，用于创建一个或多个与VRF关联的Route Target扩展团体属性。使用no命令删除配置。通过Route Target可以控制VPN站点之间的路由发布。（1）当PE根据VPN实例IPv4/IPv6地址族向其他PE发送路由时，它将向发送的路由附加export Route Target。（2）当PE从其他PE接收路由时，它根据本地的import Route Target和接收的export Route Target决定这些路由是否可以被添加到相应的VPN实例IPv4/IPv6地址族中。（3）当PE根据VPN实例IPv4/IPv6地址族向其他PE发送L3EVPN路由时，它将向发送的路由附加evpn export Route Target。（4）当PE从其他PE接收L3EVPN路由时，它根据本地的evpn import Route Target和接收的evpn export Route Target决定这些路由是否可以被添加到相应的VPN实例IPv4/IPv6地址族中。






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :


route-target 
  [{both 
|export 
|import 
}] {<0-65535>:<0-4294967295> 
|<1-65535>.<0-65535>:<0-65535> 
|A.B.C.D:<0-65535> 
} [{vpn 
|evpn 
}]
no route-target 
  [{both 
|export 
|import 
}] [{<0-65535>:<0-4294967295> 
|<1-65535>.<0-65535>:<0-65535> 
|A.B.C.D:<0-65535> 
}]
				






命令参数解释 :



参数|描述
---|---
both|和export、import是三选一，若设置为both，则表示指定添加route-target扩展团体属性到VPN实例入方向和出方向的扩展团体属性列表中，等同于同时配置import和export。如果不指定关键字，则缺省值为both。
export|和both、import是三选一，若设置为export，则表示导出VRF路由携带route-target扩展团体属性。
import|和both、export是三选一，若设置为import，则表示根据route-target扩展团体属性导入路由到VRF。
<0-65535>:<0-4294967295>|ASN_NN格式的Route Target扩展团体属性。取值范围：16位自治系统号:32位用户自定义数，例如：100:3。自治系统号的取值范围是0～65535；用户自定义数的取值范围是0～4294967295。默认值：无。
<1-65535>.<0-65535>:<0-65535>|ASND_NN格式的Route Target扩展团体属性。取值范围：32位自治系统号:16位用户自定义数字，例如：100.3:1。32位自治系统号通常写成x.y的形式，即1～65535.0～65535；用户自定义数的取值范围是0～65535。默认值：无。
A.B.C.D:<0-65535>|IPADD_NN格式的Route Target扩展团体属性。取值范围：32位IP地址:16位用户自定义数，例如：192.168.155.20:1。IP地址的取值范围是0.0.0.0～255.255.255.255；用户自定义数的取值范围是0～65535。默认值：无。
vpn|表示route-target用于L3VPN路由的发布和接收
evpn|表示route-target用于L3EVPN路由的发布和接收








缺省 :

VRF没有相关的Route Target扩展团体属性。 






使用说明 :

（1）必须通过rd命令配置过RD数据之后才可以使用本命令配置。（2）VRF-IPv4地址族模式和VRF-IPv6地址族模式的Route Target配置分别在对应的地址族下生效。（3）VRF模式下的Route Target配置可以在IPv4地址族下生效，也可以在IPv6地址族下生效，VRF-IPv4地址族模式和VRF-IPv6地址族模式的配置优先级高于VRF模式下的配置，也就是当且仅当两种地址族模式下没有配置Route Target时才使用VRF模式下的配置。（4）同一个VRF的不同配置模式下入向和出向Route Target每种最多可以配置255个。（5）route-target如果不携带vpn或者evpn可选参数，表示同时用于L3VPN和L3EVPN路由的接收和发布。






范例 :

为VPN实例zte的入方向route-target列表添加3:3，出方向route-target列表添加4:4：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf)#rd 1:1ZXROSNG(config-vrf)#route-target import 3:3ZXROSNG(config-vrf)#route-target export 4:4（2）为VPN实例zte的入方向route-target列表添加1:1用于L3VPN路由接收，出方向route-target列表添加1:1用于L3EVPN路由发布：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf)#rd 1:1ZXROSNG(config-vrf)#route-target import 1:1 vpnZXROSNG(config-vrf)#route-target export 1:1 evpn






相关命令 :

show ip vrf detail 




## route-target 


route-target 




命令功能 :

该命令工作于VRF模式、VRF-IPv4地址族模式和VRF-IPv6地址族模式，用于创建一个或多个与VRF关联的Route Target扩展团体属性。使用no命令删除配置。通过Route Target可以控制VPN站点之间的路由发布。（1）当PE根据VPN实例IPv4/IPv6地址族向其他PE发送路由时，它将向发送的路由附加export Route Target。（2）当PE从其他PE接收路由时，它根据本地的import Route Target和接收的export Route Target决定这些路由是否可以被添加到相应的VPN实例IPv4/IPv6地址族中。（3）当PE根据VPN实例IPv4/IPv6地址族向其他PE发送L3EVPN路由时，它将向发送的路由附加evpn export Route Target。（4）当PE从其他PE接收L3EVPN路由时，它根据本地的evpn import Route Target和接收的evpn export Route Target决定这些路由是否可以被添加到相应的VPN实例IPv4/IPv6地址族中。






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :


route-target 
  [{both 
|export 
|import 
}] {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
} [{vpn 
|evpn 
}]
no route-target 
  [{both 
|export 
|import 
}] [{<0-65535>:<0-4294967295> 
|<1-65535>.<0-65535>:<0-65535> 
|A.B.C.D:<0-65535> 
}]
				






命令参数解释 :



参数|描述
---|---
both|和export、import是三选一，若设置为both，则表示指定添加route-target扩展团体属性到VPN实例入方向和出方向的扩展团体属性列表中，等同于同时配置import和export。如果不指定关键字，则缺省值为both。
export|和both、import是三选一，若设置为export，则表示导出VRF路由携带route-target扩展团体属性。
import|和both、export是三选一，若设置为import，则表示根据route-target扩展团体属性导入路由到VRF。
<0-65535>:<0-4294967295>|ASN_NN格式的Route Target扩展团体属性。取值范围：16位自治系统号:32位用户自定义数，例如：100:3。自治系统号的取值范围是0～65535；用户自定义数的取值范围是0～4294967295。默认值：无。
A.B.C.D:<0-65535>|IPADD_NN格式的Route Target扩展团体属性。取值范围：32位IP地址:16位用户自定义数，例如：192.168.155.20:1。IP地址的取值范围是0.0.0.0～255.255.255.255；用户自定义数的取值范围是0～65535。默认值：无。
<1-65535>.<0-65535>:<0-65535>|ASND_NN格式的Route Target扩展团体属性。取值范围：32位自治系统号:16位用户自定义数字，例如：100.3:1。32位自治系统号通常写成x.y的形式，即1～65535.0～65535；用户自定义数的取值范围是0～65535。默认值：无。
vpn|表示route-target用于L3VPN路由的发布和接收
evpn|表示route-target用于L3EVPN路由的发布和接收








缺省 :

VRF没有相关的Route Target扩展团体属性。 






使用说明 :

（1）必须通过rd命令配置过RD数据之后才可以使用本命令配置。（2）VRF-IPv4地址族模式和VRF-IPv6地址族模式的Route Target配置分别在对应的地址族下生效。（3）VRF模式下的Route Target配置可以在IPv4地址族下生效，也可以在IPv6地址族下生效，VRF-IPv4地址族模式和VRF-IPv6地址族模式的配置优先级高于VRF模式下的配置，也就是当且仅当两种地址族模式下没有配置Route Target时才使用VRF模式下的配置。（4）同一个VRF的不同配置模式下入向和出向Route Target每种最多可以配置255个。（5）route-target如果不携带vpn或者evpn可选参数，表示同时用于L3VPN和L3EVPN路由的接收和发布。






范例 :

为VPN实例zte的入方向route-target列表添加3:3，出方向route-target列表添加4:4：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf)#rd 1:1ZXROSNG(config-vrf)#route-target import 3:3ZXROSNG(config-vrf)#route-target export 4:4（2）为VPN实例zte的入方向route-target列表添加1:1用于L3VPN路由接收，出方向route-target列表添加1:1用于L3EVPN路由发布：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf)#rd 1:1ZXROSNG(config-vrf)#route-target import 1:1 vpnZXROSNG(config-vrf)#route-target export 1:1 evpn






相关命令 :

show ip vrf detail 




## show ip rd-list 


show ip rd-list 




命令功能 :

显示配置的RD条目 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show ip rd-list 
  [＜rd-list-number 
＞] 







命令参数解释 :



参数|描述
---|---
＜rd-list-number＞|RD过滤器的编号，整数形式，取值范围是1～500








缺省 :

无 






使用说明 :

当有ip rd-list配置时，能正确显示，无配置无显示。 






范例 :

ZXROSNG(config)#ip rd-list 1 permit 1:1ZXROSNG(config)#show ip rd-list 1 ip rd-list 1  permit  1:1ZXROSNG(config)#ip rd-list 100 permit :1ZXROSNG(config)#show ip rd-list 100ip rd-list 100  permit  :1






相关命令 :

ip rd-list {＜rd-list-number＞ {deny|permit} *({<0-65535>:<0-4294967295>|A.B.C.D:<0-65535>|<1-65535>.<0-65535>:<0-65535>})|＜rd-list-number＞ {deny|permit} ＜regular-expression＞} 




## show ip route vpn 


show ip route vpn 




命令功能 :

该命令工作于所有配置模式，主要用于显示VPN路由目的地址、下一跳以及VPN的RD（Route Distinguisher，路由标识符）等信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip route vpn 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令不显示mng、?_dcn等特殊VPN的路由信息。 






范例 :

ZXROSNG(config)#show ip route vpnRoutes of vpn:Dest                NextHop         Type ASN             Addr       Peer 0.0.0.0/0          0.0.0.0         2    0               0          0.0.0.0 192.168.100.0/24   192.168.100.252 2    0               0          0.0.0.0 192.168.100.252/32 192.168.100.252 2    0               0          0.0.0.0显示信息说明：Dest：目的地址；NextHop：下一跳；Type：RD格式的类型，<0-65535>:<0-4294967295>格式的类型值为0，A.B.C.D:<0-65535>格式的类型值为1，<1-65535>.<0-65535>:<0-65535>格式的类型值为2；ASN：RD的管理域值；Addr：RD的分配域值；Peer：BGP（Border Gateway Protocol，边界网关协议）邻居地址。






相关命令 :

无 




## show ip vrf brief 


show ip vrf brief 




命令功能 :

该命令工作于所有模式，功能等同于show ip vrf，用于简要显示VRF的相关配置信息，包括VRF名称、VRF对应的RD、VRF的地址族能力。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

除用户模式外的其他所有模式:15,用户模式:1 






命令格式 :



show ip vrf brief 
  [＜vrf-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|用于指定待查询简要信息的VRF名称。取值范围：1~32位字符串，不包含空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

如果不指定VPN实例名称，此命令将显示所有VRF实例的简要信息。 






范例 :

显示所有VRF的简要配置信息：ZXROSNG(config)#show ip vrf brief* Being deleted    Name                             Default RD            Protocols VRF ID    mng                              <not set>             ipv4,ipv6 16385    zte                              1:1                   ipv4      1    lhw                              <not set>                       2$#151060481: 0/  ;1/显示所有VRF的简要配置信息：ZXROSNG#show ip vrf brief* Being deleted    Name                             Default RD            Protocols VRF ID    mng                              <not set>             ipv4,ipv6 16385    vnfm                             <not set>             ipv4,ipv6 16387    zte                              1:1                   ipv4      1#$显示信息说明：Name：VRF名称；Default RD：VRF对应的路由标识符；Protocols：该VRF实例支持的地址族类型，根据VRF实例使能协议地址族不同，可能为下列取值： 未使能任何地址族（显示为空） 只使能IPv4地址族（显示为ipv4） 只使能IPv6地址族（显示为ipv6） 使能IPv4和IPv6地址族（显示为ipv4,ipv6）VRF ID：VRF的VPNID






相关命令 :

show ip vrf 




## show ip vrf detail 


show ip vrf detail 




命令功能 :

该命令工作于所有模式，用于显示VRF的详细配置信息。完成VRF实例的配置时，可用show ip vrf detail命令检查VRF实例的配置情况。






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :


show ip vrf detail 
  [＜vrf-name 
＞] 






命令参数解释 :



参数|描述
---|---
＜vrf-name＞|用于指定待查询详细信息的VRF名称。取值范围：1~32位的字符串，不包含空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

如果不指定VPN实例名称，此命令将显示所有VRF实例的详细信息。 






范例 :

显示名称为zte的VRF的详细配置信息：ZXROSNG#show ip vrf detail zteVRF zte (VRF Id = 1); default RD 2:2  Default VPNID: <not set>  Description: This is zte!  Nat-type: none  Ttl-mode: pipe  Ds-mode is pipe   Configed rate-limit policies as follows:    Rate-limit peer 1.0.0.1 mode aware 8-100-100-200Address family ipv4:  Export VPN route-target communities    1:1  Import VPN route-target communities    1:1  Import route-map: 123  Export route-map: abc  Route limit  100 , warning limit 80% (80)  Local prefix protection enabled  Next-hop host-only enabled  priority:  2  import multicast-route:  10.0.0.1:500  Configed static outlabel as follows:    20.0.0.2:100  Configed static tunnel as follows:    1.0.0.1:zte123Address family ipv6 not active.Mpls label mode:  ipv4 VRF label allocation mode: per-prefix  ipv6 VRF label allocation mode: per-prefix  per-vrf inlabel:  1010Interface:  loopback1显示信息说明：VRF Id：VRF实例标识号，配置VRF实例时系统分配的vpnid；Description:VRF实例的描述信息；Default VPNID:VRF对应global VPNID，RFC2685中定义；default RD:VRF的路由标识符；Nat-type：对分发标签流量的NAT转换类型；Ttl-mode:MPLS标签中的TTL域和IP头中的TTL域间的处理模式；Ds-mode:MPLS标签的优先级和IP报文中优先级的处理模式；Rate-limit:VRF限速策略配置；Address family ipv4:该VRF实例下的IPv4地址族信息；Address family ipv6:该VRF实例下的IPv6地址族信息；Export VPN route-target communities:出方向Route Target列表；Import VPN route-target communities:入方向Route Target列表；Import route-map:与VRF关联的导入路由策略；Export route-map:与VRF关联的导出路由策略；Route limit:VPN实例允许路由的最大路由数目；warning limit:当前VPN实例指定的最大路由数百分比，达到此百分比时会产生警告信息；Local prefix protection:VRF的CE侧和PE侧路由形成FRR关系的开关；Next-hop host-only：下一跳的迭代策略控制；priority:VPN路由收敛优先级；import multicast-route:组播VPN控制路由导入的策略；static outlabel:PE邻居的静态出标签；static tunnel:来自PE邻居的VPN路由流量所走的外层隧道策略；Mpls label mode:VPN路由的私网标签策略；per-vrf inlabel:标签分配模式为per-vrf时VPN路由使用的标签；Interface:与VRF绑定的接口。






相关命令 :

无 




## show ip vrf summary 


show ip vrf summary 




命令功能 :

该命令可工作于所有模式下，用于显示VRF的总数目（包括自动和手动配置的VRF）。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip vrf summary 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

显示当前设备上VRF总数目。ZXROSNG(config)#show ip vrf summary 2 VPN have been configured(MAX VPN:16385).显示信息说明：MAX VPN：设备允许的VRF最大个数。






相关命令 :

无 




## show ip vrf 


show ip vrf 




命令功能 :

该命令工作于所有模式，用于简要显示VRF的相关配置信息，包括VRF名称、VRF对应的RD、VRF的地址族能力。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip vrf 
  [＜vrf-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|用于指定待查询简要信息的VRF名称。取值范围：1~32位字符串，不包含空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

（1）如果不指定VPN实例名称，此命令将显示所有VRF实例的简要信息。 






范例 :

显示所有VRF的简要配置信息：ZXROSNG(config)#show ip vrf* Being deleted    Name                             Default RD            Protocols VRF ID    mng                              <not set>             ipv4,ipv6 16385    zte                              1:1                   ipv4      1    lhw                              <not set>                       2$#151060481: 0/  ;1/显示所有VRF的简要配置信息：ZXROSNG#show ip vrf* Being deleted    Name                             Default RD            Protocols VRF ID    mng                              <not set>             ipv4,ipv6 16385    vnfm                             <not set>             ipv4,ipv6 16387    zte                              1:1                   ipv4      1#$显示信息说明：Name：VRF名称；Default RD：VRF对应的路由标识符；Protocols：该VRF实例支持的地址族类型，根据VRF实例使能协议地址族不同，可能为下列取值： 未使能任何地址族（显示为空） 只使能IPv4地址族（显示为ipv4） 只使能IPv6地址族（显示为ipv6） 使能IPv4和IPv6地址族（显示为ipv4,ipv6）VRF ID:VRF的VPNID






相关命令 :

show ip vrf brief 




## show ip vrf-public detail 


show ip vrf-public detail 




命令功能 :

该命令工作于所有模式，用于显示公网VRF的详细配置信息。 






命令模式 :

 用户模式,除用户模式外的其他所有模式  






命令默认权限级别 :

用户模式:1,除用户模式外的其他所有模式:15 






命令格式 :



show ip vrf-public detail 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

使用场景用于显示公网VRF的详细配置信息。






范例 :

显示公网VRF的详细配置信息：ZXROSNG(config)#show ip vrf-public detailVRF Id = 0; default RD 0:0  Description: aaaSR mode is DT-static,SID is 1::2Address family ipv4:  Export VPN route-target communities    2:4  Import VPN route-target communities2:4SR mode is DT-static, SID is 1::3  Import multicast-route: 1.1.1.1:0Address family ipv6:  Export VPN route-target communities    3:4  Import VPN route-target communities3:4  SR mode is DX-static, as follows:    Interface: fei-0/20/0/1    Next hop: 100::1    SID: 1::4  Import multicast-route: 4.3.3.1:1





相关命令 :

无 




## show l3vpn-statistics status 


show l3vpn-statistics status 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于显示L3VPN业务实例的统计状态，如不指定实例名称则显示L3VPN全部业务实例的统计状态。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show l3vpn-statistics status 
  [＜vrf-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|用于指定待查询统计状态的L3VPN业务实例名称。取值范围：1~32位的字符串，不包含空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

如不指定实例名称则显示L3VPN全部业务实例的统计状态。 






范例 :

显示L3VPN全部业务实例的统计状态：ZXROSNG(config)#show l3vpn-statistics status ----------------------------------------L3vpn-service                    Status----------------------------------------zte                              enablelhw                              disableZXROSNG(config)#显示信息说明：L3vpn-service：L3VPN业务实例名称；Status：统计状态。






相关命令 :

无 




## show l3vpn-statistics 


show l3vpn-statistics 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于显示L3VPN具体某一业务实例的统计数据信息。如果命令参数带有peer地址，该命令用于显示从指定PE邻居接收导入本地VRF的流量计数。





命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :


show l3vpn-statistics 
 perfvalue 
 ＜vrf-name 
＞ [peer 
 ＜ip-address 
＞] 






命令参数解释 :



参数|描述
---|---
perfvalue|关键字，表示显示性能统计值。
＜vrf-name＞|用于指定待查询统计信息的业务实例名称。取值范围：1-31位的字符串。默认值：无。
＜ip-address＞|IPv4地址，十进制点分形式








缺省 :

无 






使用说明 :

使用本命令查看统计信息前建议先使用show l3vpn-statistics status命令查看统计开关状态是否为enable。 






范例 :

1.显示名为zte的L3VPN业务实例的统计信息：ZXROSNG#show l3vpn-statistics perfvalue zte Last Clear Time : 2014-01-17 08:22:30 Last Refresh Time:  2014-01-17 06:51:55 120s input rate : 0Bps                0pps                 120s output rate: 0Bps                0pps                 In_Bytes          0                   In_Packets          0 E_Bytes           0                   E_Packets           0ZXROSNG#显示信息说明：Last Clear Time:上次清除统计信息的时间；Last Refresh Time:上次刷新统计信息的时间；120s input rate:120秒入流量统计速率；120s output rate:120秒出流量统计速率；In_Bytes:收到字节数；In_Packets:收到报文数；E_Bytes:发送字节数；E_Packets:发送报文数。2.当需要显示从10.1.1.1邻居收到导入本地zte的路由流量计数，使用以下命令：ZXROSNG(config)#show l3vpn-statistics perfvalue zte peer 10.1.1.1Priority OutPkts              OutBytes             OutRates(Kbps)PBTS-0   123456               53021371392576       1958505087099PBTS-1   123456               53021371392576       4567851542123PBTS-2   123456               53021371392576       1958505087099PBTS-3   123456               53021371392576       7854219634123PBTS-4   123456               53021371392576       1958505087099PBTS-5   123456               53021371392576       7894561222223PBTS-6   123456               53021371392576       1958505087099PBTS-7   123456               53021371392576       7845122222123Total    987648               424170971140608      7834020348888显示信息说明：显示    描述Priority    优先级OutPkts           出向包数OutBytes    出向字节数OutRates    出向120s速率，单位Kbps





相关命令 :

clear l3vpn statistics 




## show mpls forwarding-table color-lsp 


show mpls forwarding-table color-lsp 




命令功能 :

显示 Color-LSP 的标签转发信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls forwarding-table color-lsp 
  [{＜ipv6-address 
＞ ＜dest-ipv6-mask-length 
＞|＜ipv4-address 
＞ ＜dest-ipv4-mask-length 
＞} ＜color 
＞] 







命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|IPv6 前缀
＜dest-ipv6-mask-length＞|IPv6掩码长度
＜ipv4-address＞|IPv4 前缀
＜dest-ipv4-mask-length＞|IPv4掩码长度
＜color＞|Color 的值，范围[1 -4294967295 ]








缺省 :

显示所有 Color-LSP的转发信息 






使用说明 :

使用场景用户需要查看COlor-lsp的转发信息，可以执行该命令。注意事项1、默认显示所有 Color-LSP 的转发信息。2、可以指定Prefix、掩码长度和Color显示指定的Color-LSP的转发信息。






范例 :

一，默认情况下，显示所有 Color-LSP的转发信息ZXROSNG#show mpls forwarding-table color-lsp  | detailPrefix              Local     Outgoing  Next Hop        Forwarding          M/Scolor               label     label                     info2.3.4.5/32/100      1001      200       11.2.3.4                            M2.3.4.5/32/100      1001      200       21.3.4.5                            M9.8.7.6/32/100      101       200       1.2.3.4         TE Tunnel[1]        M9::6/128/100        102       200       1.2.3.4         TE Tunnel[1]        M二、指定IPv4前缀、掩码、Color，显示指定的Color-path LSP的转发信息ZXROSNG#show mpls forwarding-table color-lsp   9.8.7.6 32 100  Prefix              Local     Outgoing  Next Hop        Forwarding          M/Scolor               label     label                     info9.8.7.6/32/100      101       200       1.2.3.4         TE Tunnel[1]        M三、指定IPv6前缀、掩码和Color，显示指定的Color-LSP的转发信息ZXROSNG#show mpls forwarding-table color-lsp 9::6 128 100Prefix              Local     Outgoing  Next Hop        Forwarding          M/Scolor               label     label                     info9::6/128/100        102       200       1.2.3.4         TE Tunnel[1]        M域信息说明：域：  说明Prefix color：此LSP的前缀和颜色Local label :  此LSP 条目的入标签Outgong label：此LSP条目的出标签Next  Hop ：此LSP条目的下一跳Forwarding info：此LSP的外层转发数据，若外层通过查路由转发，则此列显示为空；若能匹配到隧道，则显示隧道信息，如匹配到TE隧道，则显示为TE Tunnel[ID]，ID 为TE隧道的Tunnel-IDM/S：此LSP条目的出向是主还是备。






相关命令 :

无 




## show mpls forwarding-table static-lsp 


show mpls forwarding-table static-lsp 




命令功能 :

显示静态配置的MPLS转发表 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls forwarding-table static-lsp 
  [＜lspname 
＞] 







命令参数解释 :



参数|描述
---|---
＜lspname＞|静态LSP实例名








缺省 :

显示所有静态配置的lsp的转发信息 






使用说明 :

使用场景当用户需要查看静态MPLS的转发信息，可以执行该命令。注意事项1、默认显示所有静态配置的lsp的转发信息。2、指定static-lsp的名称，显示指定的static-lsp的转发信息。






范例 :

一，默认情况下，显示所有静态配置的lsp的转发信息ZXROSNG(config)#show mpls forwarding-table static-lspLocal Outgoing Prefix or Outgoing  Next Hop       M/Slabel label    Lspname   interface200   36987    slsp1  gei-0/1/0/5  3.6.1.2        M202   36987    slsp2  gei-0/1/0/8  3.8.1.2        M二、指定static-lsp的名称，显示固定一个静态配置的lsp 的转发信息ZXROSNG(config)#show mpls forwarding-table static-lsp slsp1Local  Outgoing Prefix or  Outgoing    NextHop    M/Slabel  label    Lspname    interface200    36987     slsp1     gei-0/1/0/1 53.6.1.2    M





相关命令 :

mpls static-lsp 




## show mpls forwarding-table summary 


show mpls forwarding-table summary 




命令功能 :

显示LDP  、SR 的IPv4和IPv6类型FEC 的数量统计数据。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls forwarding-table summary 
  [vrf 
 ＜vrf-name 
＞] 







命令参数解释 :



参数|描述
---|---
＜vrf-name＞|VRF名称，长度为1~32个字符。








缺省 :

无过滤参数时显示公网LDP和SR的IPv4和IPv6 类型FEC 的个数的统计数据。 






使用说明 :

使用场景当用户需要查看LDP和SR类型FEC个数统计数据，可以执行show mpls forwarding-table summary命令。注意事项1、默认显示公网LDP和SR的IPv4和IPv6类型fec数量统计数据。2、指定VRF 名称时，显示私网的LDP的IPv4和IPv6类型FEC数量统计数据。






范例 :

范例1：打印公网的LDP和SR的IPv4和IPv6类型FEC的数量统计数据ZXROSNG#show mpls forwarding-table summary Header: Origin: The origin of FECs        AF: Address Family        In-label: The number of normal in-labels        FEC: The number of all FECs        Single-Nh: The number of FECs having one next hop        FRR: The number of FECs having FRR        LDSH: The number of FECs having LDSHOrigin    AF    In-label  FEC       Single-Nh FRR       LDSHLDP       IPv4  1         4         0         1         0LDP       IPv6  1         4         1         0         0SR        IPv4  1         2         0         0         1SR        IPv6  1         2         1         0         0范例2：打印私网的LDP的IPv4和IPv6类型FEC的数量统计数据ZXROSNG#show mpls forwarding-table summary vrf zteHeader: Origin: The origin of FECs        AF: Address Family        In-label: The number of normal in-labels        FEC: The number of all FECs        Single-Nh: The number of FECs having one next hop        FRR: The number of FECs having FRR        LDSH: The number of FECs having LDSHOrigin    AF    In-label  FEC       Single-Nh FRR       LDSHLDP       IPv4  1         1         1         0         0LDP       IPv6  1         1         1         0         0域信息说明：域：  说明Origin:  统计FEC 的协议类型，目前只支持LDP；AF: 地址族类型；In-label：正常入标签（范围是[16-1048575]）的个数；FEC：FEC 的总个数；Single-Nh：存在一个下一跳的FEC的个数；FRR：存在FRR 的FEC的个数；LDSH：存在负荷分担的FEC 的个数






相关命令 :

mpls ldp instance 




## show mpls forwarding-table vpnv4-lsp 


show mpls forwarding-table vpnv4-lsp 




命令功能 :

支持显示BGP VPNV4  FIB表项内容转发表 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls forwarding-table vpnv4-lsp 
  [{<0-65535>:<0-4294967295> 
|<1-65535>.<0-65535>:<0-65535> 
|A.B.C.D:<0-65535> 
} [＜ipv4-address 
＞ {＜dest-ipv4-mask-length 
＞|＜ipv4-address-mask 
＞}]] 







命令参数解释 :



参数|描述
---|---
<0-65535>:<0-4294967295>|VPN Route Distinguisher
<1-65535>.<0-65535>:<0-65535>|VPN Route Distinguisher
A.B.C.D:<0-65535>|VPN Route Distinguisher
＜ipv4-address＞|Destination IPv4 prefix
＜dest-ipv4-mask-length＞|掩码长度
＜ipv4-address-mask＞|掩码








缺省 :

显示所有BGPVPNV4 lsp的转发信息。 






使用说明 :

使用场景当用户需要查看BGP VPNV4的lsp的转发信息，可以执行该命令。注意事项默认显示所有BGP VPNv4的LSP的转发信息，也可以指定 RD，显示此RD的所有LSP 的转发信息，也可以指定RD、Destination、掩码长度或掩码显示固定的BGP VPNv4 的LSP转发信息。






范例 :

一，默认情况下，显示所有BGP  VPNV4的lsp的转发信息ZXROSNG#show mpls forwarding-table vpnv4 Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface40000     50000     9.1.1.0/24[RD 0.0.0                     2.2.2.2         M                    .100:200]                                               40000     50001     9.1.1.0/24[RD 0.0.0                     2.2.2.3         S                    .100:200]                                               40001     50001     9.1.1.1/32[RD 0.0.0                     2.2.2.1         M                    .100:200]                                               40001     50002     9.1.1.1/32[RD 0.0.0                     2.2.2.2         M                    .100:200]                                               40001     50003     9.1.1.1/32[RD 0.0.0                     2.2.2.3         M                    .100:200]       二、指定rd，显示固定一个rd的BGP VPNV4 的lsp 的转发信息ZXROSNG#show mpls forwarding-table vpnv4 0.0.0.100:200Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface40000     50000     9.1.1.0/24[RD 0.0.0                     2.2.2.2         M                    .100:200]                                               40000     50001     9.1.1.0/24[RD 0.0.0                     2.2.2.3         S                    .100:200]                                               40001     50001     9.1.1.1/32[RD 0.0.0                     2.2.2.1         M                    .100:200]                                               40001     50002     9.1.1.1/32[RD 0.0.0                     2.2.2.2         M                    .100:200]                                               40001     50003     9.1.1.1/32[RD 0.0.0                     2.2.2.3         M三、指定rd、Destinatio、掩码长度或掩码显示固定的BGP VPNV4 的lsp转发信息 ZXROSNG#show mpls forwarding-table vpnv4 0.0.0.100:200 9.1.1.1 32Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface40001     50001     9.1.1.1/32[RD 0.0.0                     2.2.2.1         M                    .100:200]                                               40001     50002     9.1.1.1/32[RD 0.0.0                     2.2.2.2         M                    .100:200]                                               40001     50003     9.1.1.1/32[RD 0.0.0                     2.2.2.3         M                    .100:200]                                               40001     50004     9.1.1.1/32[RD 0.0.0                     2.2.2.4         M                    .100:200]                                               40001     50005     9.1.1.1/32[RD 0.0.0                     2.2.2.5         M                    .100:200]                                               40001     50006     9.1.1.1/32[RD 0.0.0                     2.2.2.6         M                    .100:200]  





相关命令 :

无 




## show mpls forwarding-table vpnv6-lsp 


show mpls forwarding-table vpnv6-lsp 




命令功能 :

支持显示BGP VPNv6  FIB表项内容转发表 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls forwarding-table vpnv6-lsp 
  [{<0-65535>:<0-4294967295> 
|<1-65535>.<0-65535>:<0-65535> 
|A.B.C.D:<0-65535> 
} [＜ipv6-address 
＞ ＜dest-ipv6-mask-length 
＞]] 







命令参数解释 :



参数|描述
---|---
<0-65535>:<0-4294967295>|VPN Route Distinguisher
<1-65535>.<0-65535>:<0-65535>|VPN Route Distinguisher
A.B.C.D:<0-65535>|VPN Route Distinguisher
＜ipv6-address＞|Destination IPv6 prefix
＜dest-ipv6-mask-length＞|掩码长度，范围[0-128]








缺省 :

显示所有BGP VPNv6 LSP的转发信息。 






使用说明 :

使用场景在V6类型L3VPN跨域场景配置完成后，在跨域节点使用此命令校验 BGP VPNv6 LSP的标签转发表注意事项默认显示所有BGP VPNv6的LSP的转发信息，也可以指定 RD，显示此RD的所有LSP 的转发信息，也可以指定RD、Destination、掩码长度或掩码显示固定的BGP VPNv6 的LSP转发信息






范例 :

一，默认情况下，显示所有BGP VPNv6的LSP的转发信息ZXROSNG#show mpls forwarding-table vpnv6                         Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface60000     70000     9:9:9::/96[RD 0.0.0                     3:1::1:1        M                    .100:200]                                               60000     70001     9:9:9::/96[RD 0.0.0                     3:1::1:2        S                    .100:200]                                               60001     70001     9:9:9::1/128[RD 0.0                     1:1::1:1        M                    .0.100:200]                                             60001     70002     9:9:9::1/128[RD 0.0                     1:1::1:2        M                    .0.100:200]                                             60001     70003     9:9:9::1/128[RD 0.0                     1:1::1:3        M                    .0.100:200]                                             60001     70004     9:9:9::1/128[RD 0.0                     1:1::1:4        M                    .0.100:200]                                             60001     70005     9:9:9::1/128[RD 0.0                     1:1::1:5        M                    .0.100:200]                                             60001     70006     9:9:9::1/128[RD 0.0                     1:1::1:6        M459412    530400    220:101:1::/64[RD 0                     10.10.10.10     M                    :0]                                                     459413    500673    220:102:1::/64[RD 0                     220.33.1.2      M                    :0]                                        二、指定RD，显示固定一个RD的BGP VPNv6 的LSP 的转发信息ZXROSNG#show mpls forwarding-table vpnv6 0.0.0.100:200Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface60000     70000     9:9:9::/96[RD 0.0.0                     3:1::1:1        M                    .100:200]                                               60000     70001     9:9:9::/96[RD 0.0.0                     3:1::1:2        S                    .100:200]                                               60001     70001     9:9:9::1/128[RD 0.0                     1:1::1:1        M                    .0.100:200]                                             60001     70002     9:9:9::1/128[RD 0.0                     1:1::1:2        M                    .0.100:200]                                             60001     70003     9:9:9::1/128[RD 0.0                     1:1::1:3        M                    .0.100:200]                                             60001     70004     9:9:9::1/128[RD 0.0                     1:1::1:4        M                    .0.100:200]                                             60001     70005     9:9:9::1/128[RD 0.0                     1:1::1:5        M                    .0.100:200]                                             60001     70006     9:9:9::1/128[RD 0.0                     1:1::1:6        M                    .0.100:200]                                             60001     70007     9:9:9::1/128[RD 0.0                     1:1::1:7        M                    .0.100:200]                                             60001     70008     9:9:9::1/128[RD 0.0                     1:1::1:8        M                    .0.100:200]                                             60001     70009     9:9:9::1/128[RD 0.0                     1:1::1:9        M                    .0.100:200]                                             60001     70010     9:9:9::1/128[RD 0.0                     1:1::1:10       M                    .0.100:200]                                             60001     70011     9:9:9::1/128[RD 0.0                     1:1::1:11       M三、指定RD、Destinatio、掩码长度或掩码显示固定的BGP VPNv6 的LSP转发信息 ZXROSNG#show mpls forwarding-table vpnv6 0.0.0.100:200 9:9:9::1 128Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface60001     70001     9:9:9::1/128[RD 0.0                     1:1::1:1        M                    .0.100:200]                                             60001     70002     9:9:9::1/128[RD 0.0                     1:1::1:2        M                    .0.100:200]                                             60001     70003     9:9:9::1/128[RD 0.0                     1:1::1:3        M                    .0.100:200]                                             60001     70004     9:9:9::1/128[RD 0.0                     1:1::1:4        M                    .0.100:200]                                             60001     70005     9:9:9::1/128[RD 0.0                     1:1::1:5        M                    .0.100:200]                                             60001     70006     9:9:9::1/128[RD 0.0                     1:1::1:6        M                    .0.100:200]                                             60001     70007     9:9:9::1/128[RD 0.0                     1:1::1:7        M                    .0.100:200]                                             60001     70008     9:9:9::1/128[RD 0.0                     1:1::1:8        M                    .0.100:200]                                             60001     70009     9:9:9::1/128[RD 0.0                     1:1::1:9        M                    .0.100:200]                                             60001     70010     9:9:9::1/128[RD 0.0                     1:1::1:10       M                    .0.100:200]                                             60001     70011     9:9:9::1/128[RD 0.0                     1:1::1:11       M                    .0.100:200]                                             60001     70012     9:9:9::1/128[RD 0.0                     1:1::1:12       M





相关命令 :

无 




## show mpls forwarding-table 


show mpls forwarding-table 




命令功能 :

显示MPLS转发表。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls forwarding-table 
  {[＜in-label 
＞]|[[vrf 
 ＜vrf-name 
＞] {[aii 
 ＜admini-instance-identifier 
＞]|[fa 
 ＜flexible-algorithm-id 
＞]} [{[＜ipv4-address 
＞ [{＜dest-ipv4-mask-length 
＞|＜ipv4-address-mask 
＞}] [detail 
]]|[＜ipv6-address 
＞ [＜dest-ipv6-mask-length 
＞]]}]]|[ipv4-lsp 
]|[ipv6-lsp 
]} 







命令参数解释 :



参数|描述
---|---
＜in-label＞|转发信息库的入标签，范围：16~1048575。
＜vrf-name＞|VRF名称，长度为1~32个字符。
＜admini-instance-identifier＞|网络切片管理实例标识。范围是[1-4294967295]
＜flexible-algorithm-id＞|网络切片算法ID。范围是[128-255]
＜ipv4-address＞|转发信息库中目的地址前缀。
＜dest-ipv4-mask-length＞|目的地址前缀的掩码长度
＜ipv4-address-mask＞|目的地址前缀的掩码。
detail|显示指定IPv4-LSP 详细转发信息（展开转发信息）的过滤器
＜ipv6-address＞|IPv6的目的地址
＜dest-ipv6-mask-length＞|IPv6目的地址前缀的掩码长度
ipv4-lsp|显示IPv4-LSP 转发信息的过滤器
ipv6-lsp|显示IPv6-LSP 转发信息的过滤器








缺省 :

无过滤参数时显示公网LDP、Segment-Routing、Static-LSP标签转发信息。 






使用说明 :

使用场景当用户需要查询MPLS转发表信息时，可以执行该命令。注意事项1、指定入标签时，显示此标签的LSP转发信息；2、指定IP地址和掩码（或掩码长度）时，显示此固定FEC的转发信息；3、指定IP地址无掩码（或掩码长度）时，最长匹配一个FEC，显示此FEC的转发信息；4、可以使用ipv4-lsp或ipv6-lsp参数只显示IPv4或IPv6类型的LSP转发信息；5、显示固定IPv4类型FEC的转发信息时，可使用detail 参数来显示FEC的展开转发信息。6、指定VRF 名称时，显示私网的标签转发信息。7、指定网络切片标识FA 或AII，可以打印指定网络切片内部的LSP转发信息。






范例 :

范例1：ZXROSNG(config-if)#show mpls forwarding-tableLocal    Outgoing   Prefix or         Outgoing       Next Hop        M/Slabel    label      Lspname           interface16384    Poptag      22.22.22.22/32   gei-0/1/0/1    1.1.1.2           M16385    Untagged    2.1.1.2/32       gei-0/1/0/2    2.1.1.2           M16386    Untagged    2.1.1.0/32       gei-0/1/0/2    2.1.1.2           M范例2：显示指定公网的IPv4-LSP的详细转发信息ZXROSNG#show mpls forwarding-table 70.70.1.101 detail Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interfaceImpNull   1296      70.70.1.101/32      gei-0/1/0/7.3       4.1.1.2         M      Label stack (Top -> Bottom):  {1296}     Outgoing interface: gei-0/1/0/7.3Direct next hop: 4.1.1.2范例3：显示指定私网的IPv4-LSP的详细转发信息ZXROSNG#show mpls forwarding-table vrf  zte 102.0.0.2 detail Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface205825    Poptag    102.0.0.2/32        gei-0/1/0/1         15.15.1.2       M      Label stack (Top -> Bottom):  {3}     Outgoing interface: gei-0/1/0/1    Direct hop: 15.15.1.2205825    205837    102.0.0.2/32                            104.0.0.2       S      Label stack (Top -> Bottom):  {205837|205848}     Outgoing interface: gei-0/1/0/8    Direct next hop: 15.15.6.2范例4：显示指定网络切片FA 算法为128的标签转发表信息ZXROSNG(config)#show mpls forwarding-table fa 128Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface900001    900001    1.1.1.9/32          fei-0/20/0/1        12.1.1.1        M900002    Untagged  2.2.2.9/32          loopback1           2.2.2.9         M900003    900003    3.3.3.9/32          fei-0/20/0/4        23.1.1.3        M900004    900004    4.4.4.9/32          fei-0/20/0/1        12.1.1.1        M范例5：显示指定网络切片AII为10的标签转发表信息ZXROSNG(config)#show mpls forwarding-table aii 10Local     Outgoing  Prefix or           Outgoing            Next Hop        M/Slabel     label     Lspname             interface900011    900011    1.1.11.9/32          fei-0/20/0/1        12.1.1.1        M900013    900013    3.3.13.9/32          fei-0/20/0/4        23.1.1.3        M900014    900014    4.4.14.9/32          fei-0/20/0/1        12.1.1.1        M域信息说明：1.列表中：域：  说明Local label :  此LSP 条目的入标签；Outgong label：此LSP条目的出标签；Prefix  or Lspname ：此LSP条目的前缀或静态LSP的名称；Outgong interface：此LSP条目的原始出接口；Next  Hop：此LSP条目的原始下一跳；M/S：此LSP条目的出向是主还是备。2.详细信息中：域：  说明Label stack (Top -> Bottom):   此LSP条目展开后的栈顶->栈底的标签栈，多个标签用|隔开；Outgoing interface:  此LSP条目展开后的实际出接口；Direct hop:   此LSP条目展开后的直连下一跳。






相关命令 :

mpls ldp instance 




## show mpls multicast forwarding-table mldp 


show mpls multicast forwarding-table mldp 




命令功能 :

显示MPLS MLDP转发表 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls multicast forwarding-table mldp 
  [{＜in-label 
＞|[vrf 
 ＜vrf-name 
＞] [＜root 
＞ [{tunnel-id 
 [＜tunnel-id 
＞]|ipv4-source 
 [＜source 
＞ ＜group 
＞]|ipv6-source 
 [＜source 
＞ ＜group 
＞]|ipv4-bidir 
 [＜rp 
＞ ＜group 
＞ ＜mask-length 
＞]|ipv6-bidir 
 [＜rp 
＞ ＜group 
＞ ＜mask-length 
＞]|vpnv4-source 
 [＜source 
＞ ＜group 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}]|vpnv6-source 
 [＜source 
＞ ＜group 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}]|vpnv4-bidir 
 [＜rp 
＞ ＜group 
＞ ＜mask-length 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}]|vpnv6-bidir 
 [＜rp 
＞ ＜group 
＞ ＜mask-length 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}]|rosen-mdt 
 [＜vpn-id 
＞ ＜mdt-number 
＞]|pub-recursive 
 [＜root 
＞ {tunnel-id 
 ＜tunnel-id 
＞|ipv4-source 
 ＜source 
＞ ＜group 
＞|ipv6-source 
 ＜source 
＞ ＜group 
＞|ipv4-bidir 
 ＜rp 
＞ ＜group 
＞ ＜mask-length 
＞|ipv6-bidir 
 ＜rp 
＞ ＜group 
＞ ＜mask-length 
＞|vpnv4-source 
 ＜source 
＞ ＜group 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|vpnv6-source 
 ＜source 
＞ ＜group 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|vpnv4-bidir 
 ＜rp 
＞ ＜group 
＞ ＜mask-length 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|vpnv6-bidir 
 ＜rp 
＞ ＜group 
＞ ＜mask-length 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|rosen-mdt 
 ＜vpn-id 
＞ ＜mdt-number 
＞}]|vpn-recursive 
 [{<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
} ＜root 
＞ {tunnel-id 
 ＜tunnel-id 
＞|ipv4-source 
 ＜source 
＞ ＜group 
＞|ipv6-source 
 ＜source 
＞ ＜group 
＞|ipv4-bidir 
 ＜rp 
＞ ＜group 
＞ ＜mask-length 
＞|ipv6-bidir 
 ＜rp 
＞ ＜group 
＞ ＜mask-length 
＞|vpnv4-source 
 ＜source 
＞ ＜group 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|vpnv6-source 
 ＜source 
＞ ＜group 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|vpnv4-bidir 
 ＜rp 
＞ ＜group 
＞ ＜mask-length 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|vpnv6-bidir 
 ＜rp 
＞ ＜group 
＞ ＜mask-length 
＞ {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
|<1-65535>.<0-65535>:<0-65535> 
}|rosen-mdt 
 ＜vnp-id 
＞ ＜mdt-number 
＞}]}]]}] 







命令参数解释 :



参数|描述
---|---
＜in-label＞|入标签，范围：16-1048575
＜vrf-name＞|VRF名称，长度为1~32个字符
＜root＞|隧道头结点的router-id
tunnel-id|Tunnel id 类型
＜tunnel-id＞|隧道的隧道ID，范围：[0-4294967295]
ipv4-source|IPv4 source 类型
＜source＞|源地址
＜group＞|组地址
ipv6-source|IPv6 source 类型
＜source＞|源地址
＜group＞|组地址
ipv4-bidir|IPv4 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
ipv6-bidir|IPv6 bidir 地址
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
vpnv4-source|VPNv4 source 类型
＜source＞|源地址
＜group＞|组地址
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv6-source|VPNv6 source 类型
＜source＞|源地址
＜group＞|组地址
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv4-bidir|VPNv4 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv6-bidir|VPNv6 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
rosen-mdt|Rosen mdt类型
＜vpn-id＞|全局VPN ID
＜mdt-number＞|MDT组播树编号
pub-recursive|Pub recursive 类型
＜root＞|隧道头结点的router-id
tunnel-id|Tunnel id 类型
＜tunnel-id＞|隧道的隧道ID，范围：[0-4294967295]
ipv4-source|IPv4 source 类型
＜source＞|源地址
＜group＞|组地址
ipv6-source|IPv6 source 类型
＜source＞|源地址
＜group＞|组地址
ipv4-bidir|IPv4 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
ipv6-bidir|IPv6 bidir 地址
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
vpnv4-source|VPNv4 source 类型
＜source＞|源地址
＜group＞|组地址
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv6-source|VPNv6 source 类型
＜source＞|源地址
＜group＞|组地址
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv4-bidir|VPNv4 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv6-bidir|VPNv6 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
rosen-mdt|Rosen mdt类型
＜vpn-id＞|全局VPN ID
＜mdt-number＞|MDT组播树编号
vpn-recursive|VPN recursiver 类型
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
＜root＞|隧道头结点的router-id
tunnel-id|Tunnel id 类型
＜tunnel-id＞|隧道的隧道ID，范围：[0-4294967295]
ipv4-source|IPv4 source 类型
＜source＞|源地址
＜group＞|组地址
ipv6-source|IPv6 source 类型
＜source＞|源地址
＜group＞|组地址
ipv4-bidir|IPv4 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
ipv6-bidir|IPv6 bidir 地址
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
vpnv4-source|VPNv4 source 类型
＜source＞|源地址
＜group＞|组地址
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv6-source|VPNv6 source 类型
＜source＞|源地址
＜group＞|组地址
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv4-bidir|VPNv4 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
vpnv6-bidir|VPNv6 bidir 类型
＜rp＞|Rp地址
＜group＞|组地址
＜mask-length＞|掩码长度
<0-65535>:<0-4294967295>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
A.B.C.D:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
<1-65535>.<0-65535>:<0-65535>|路由标识符，可以用AS号:NN或者IP地址：NN标识或者IP地址：AS号
rosen-mdt|Rosen mdt类型
＜vnp-id＞|全局VPN ID
＜mdt-number＞|MDT组播树编号








缺省 :

显示所有的MLDP转发表项 






使用说明 :

使用场景当用户需要查看MLDP转发表信息时，可以执行该命令。注意事项1、默认显示所有的MLDP转发表条目。2、输入入标签或MLDP FEC查看指定的MLDP转发表条目。






范例 :

一、显示入标签为4096的转发表项ZXROSNG#show mpls multicast forwarding-table mldp 4096Opaque-value type codes:  TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry       Next -hopLabel    Label    32.32.32.8/TI[1001]     4096     ----     4096                 ----32.32.32.8/TI[1001]     4096     1000     smartgroup2          3.3.3.9二、显示opaque value为tunnel-id类型的转发表项ZXROSNG#show mpls multicast forwarding-table mldp 32.32.32.8 tunnel-id 1001Opaque-value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    32.32.32.8/TI[1001]     11111    ----     [V]zteztezte         ----32.32.32.8/TI[1001]     11111    22222    gei-0/1/0/8       10.10.10.232.32.32.8/TI[1001]     11111    33333    gei-0/1/0/8       10.10.10.332.32.32.8/TI[1001]     11111    ----     [S]1000              ----三、 显示opaque value为ipv4-source类型的转发表项ZXROSNG#$ulticast forwarding-table mldp 20.20.20.8 ipv4-source 3.3.3.8 2.2.2.3Opaque-value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.8/4S[3.3.3.8,2 1234     ----     4096                 ----.2.2.3]20.20.20.8/4S[3.3.3.8,2 1234     1111     null1                3.3.3.9四、 显示opaque value为ipv6-source类型的转发表项ZXROSNG#$ulticast forwarding-table mldp 20.20.20.8 ipv6-source 3::8 2::3Opaque-value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.8/6S[3:0:0:0:0 1234     ----     4096                 ----:0:0:8,2:0:0:0:0:0:0:3]20.20.20.8/6S[3:0:0:0:0 1234     1111     null1                3.3.3.9:0:0:8,2:0:0:0:0:0:0:3]五、 显示opaque value为ipv4-bidir类型的转发表项ZXROSNG#$orwarding-table mldp 20.20.20.7 ipv4-bidir 1.1.1.2 2.2.2.3 24Opaque-value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.7/4B[1.1.1.2,2 1234     ----     4096                 ----.2.2.3,24]20.20.20.7/4B[1.1.1.2,2 1234     1111     null1                3.3.3.9.2.2.3,24]六、 显示opaque value为ipv6-bidir类型的转发表项ZXROSNG#$orwarding-table mldp 20.20.20.7 ipv6-bidir 1::2 2::3 24Opaque-value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.7/6B[1:0:0:0:0 1234     ----     4096                 ----:0:0:2,2:0:0:0:0:0:0:3,24]20.20.20.7/6B[1:0:0:0:0 1234     1111     null1                3.3.3.9:0:0:2,2:0:0:0:0:0:0:3,24]七、 显示opaque value为vpnv4-source类型的转发表项ZXROSNG#$orwarding-table mldp 20.20.20.8 vpnv4-source 1.1.1.2 2.2.2.3 1:2Opaque-value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.8/V4S[1.1.1.2, 1234     ----     4096                 ----2.2.2.3,1:2]20.20.20.8/V4S[1.1.1.2, 1234     1111     null1                3.3.3.92.2.2.3,1:2]八、 显示opaque value为vpnv6-source类型的转发表项ZXROSNG#$orwarding-table mldp 20.20.20.8 vpnv6-source 1::2 2::3 1:2Opaque-value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.8/V6S[1:0:0:0: 1234     ----     4096                 ----0:0:0:2,2:0:0:0:0:0:0:3,1:2]20.20.20.8/V6S[1:0:0:0: 1234     1111     null1                3.3.3.90:0:0:2,2:0:0:0:0:0:0:3,1:2]九、 显示opaque value为vpnv4-bidir类型的转发表项ZXROSNG#$orwarding-table mldp 20.20.20.8 vpnv4-bidir 1.1.1.2 2.2.2.3 24 1:2Opaque Value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.8/V4B[1.1.1.2, 1234     ----     4096                 ----2.2.2.3,24,1:2]20.20.20.8/V4B[1.1.1.2, 1234     1111     null1                3.3.3.92.2.2.3,24,1:2]十、显示opaque value为vpnv6-bidir类型的转发表项ZXROSNG#$orwarding-table mldp 20.20.20.8 vpnv6-bidir 1::2 2::3 128 1:2Opaque Value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.8/V6B[1:0:0:0: 1234     ----     4096                 ----0:0:0:2,2:0:0:0:0:0:0:3,128,1:2]20.20.20.8/V6B[1:0:0:0: 1234     1111     null1                3.3.3.90:0:0:2,2:0:0:0:0:0:0:3,128,1:2]十一、显示opaque value为rosen-mdt类型的转发表项ZXROSNG#show mpls multicast forwarding-table mldp 32.32.32.8 rosen-mdt 100：100 101Opaque Value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    32.32.32.8/RM[100:100,1 1234     ----     4096                 ----01]32.32.32.8/RM[100:100,1 1234     1111     null1                3.3.3.901]十二、显示opaque value为pub-recursive类型、内层opaque value为tunnel-id的转发表项ZXROSNG#show mpls multicast forwarding-table mldp 20.20.20.8 pub-recursiveOpaque Value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry       Next-hopLabel    Label   20.20.20.8/PR[5.5.5.9,T 1234     ----     4096                 ----I[1002]]20.20.20.8/PR[5.5.5.9,T 1234     1111     null1                3.3.3.9I[1002]]十三、显示opaque value为vpn-recursive类型、内层opaque value为tunnel-id的转发表项ZXROSNG#show mpls multicast forwarding-table mldp 20.20.20.8 vpn-recursiveOpaque Value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.8/VR[1.2.3.4:5 1234     ----     4096                 ----,7.7.7.3,TI[1002]]20.20.20.8/VR[1.2.3.4:5 1234     1111     null1                3.3.3.9,7.7.7.3,TI[1002]]十四、显示vrf name为zte下，opaque value为vpn-recursive类型、内层opaque value为tunnel-id的转发表项ZXROSNG#show mpls multicast forwarding-table mldp vrf zte 20.20.20.8 vpn-recursiveOpaque Value type codes: TI:  Tunnel Id,     RM:  Rosen Mdt     PR:  Pub Recursive, VR:  VPN Recursive4S:  IPv4 Source,   6S:  IPv6 Source   4B:  IPv4 Bidir,    6B:  IPv6 BidirV4S: VPNv4 Source,  V6S: VPNv6 Source  V4B: VPNv4 Bidir,   V6B: VPNv6 BidirOut-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDRoot/Opaque-value       Local    Outgoing Out-entry        Next-hopLabel    Label    20.20.20.8/VR[1.2.3.4:5 1234     ----     4096                 ----,7.7.7.3,TI[1002]]20.20.20.8/VR[1.2.3.4:5 1234     1111     null1                3.3.3.9,7.7.7.3,TI[1002]]域信息说明：域：  说明Root/Opaque-value： mLDP FEC的关键字。组播树的根和多种类型的透明值组合。Local Label：入标签。Outgoing Label：出标签。Out-entry：出向。目前支持四种类型：转发出接口、转组播公网路由转发、转组播私网路由转发时的VRF名称、组播分段时的Segment ID。Next-hop：下一跳。






相关命令 :

无 




## show mpls multicast forwarding-table mte dynamic-fec 


show mpls multicast forwarding-table mte dynamic-fec 




命令功能 :

显示动态MPLS MTE FEC转发表 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls multicast forwarding-table mte dynamic-fec 
 ingress-id 
 ＜ingress-lsr-id 
＞ ingress-tunnel-id 
 ＜dynamic-tunnel-id in ingress 
＞







命令参数解释 :



参数|描述
---|---
＜ingress-lsr-id＞|Ingress节点 LSR ID
＜dynamic-tunnel-id in ingress＞|头节点隧道Tunnel ID，范围1-4294967295








缺省 :

无 






使用说明 :

使用场景当用户需要查看动态MPLS MTE转发表信息，可以执行该命令。






范例 :

1. 显示Ingress ID 为9.1.1.3 ，Ingress Tunnel ID 为 3的转发表ZXROSNG#$orwarding-table mte dynamic-fec ingress-id 9.1.1.3 ingress-tunnel-id 3          Out-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDIngress-ID/Tunnel-ID/        Local Outgoing Out-entry          Next-hopLSP-ID                       Label Label9.1.1.3/3/1                  21206 ----     [G]                ----9.1.1.3/3/1                  21206 31030    spi-0/1/0/1        10.1.1.19.1.1.3/3/1                  21206 31034    gei-0/1/0/1        10.1.1.59.1.1.3/3/1                  21206 ----     [S]10102           ----9.1.1.3/3/2                  21207 ----     [G]                ----9.1.1.3/3/2                  21207 31035    spi-0/1/0/1        10.1.1.19.1.1.3/3/2                  21207 31036    spi-0/1/0/2        10.1.1.2域信息说明Ingress-ID/Tunnel-ID/ LSP-ID ：显示动态FEC时，依次为Ingress节点的 LSR ID，隧道头节点Tunnel ID和LSP  ID；静态FEC时，Ingress ID不存在，打印“—”。Tunnel ID 为静态Local Tunnel ID和静态 LSP ID 。Local Label ：FEC 的入标签，头节点FEC没有入标签，打印“--”。Out Label ： FEC 的出标签，当出向是导入IP组播路由表转发时，出标签为“--”。Out-entry ：FEC 的出口信息。可能的类型有FEC 的转发出接口，若有前导词(G)，表示导入组播公网路由表转发；若有前导词(V)表示导入组播私网路由表转发，接着打印私网VRF名称；若有前导词(S)，表示此出口为Segment类型的出向，接着打印Segment 的ID 。Next-hop ：FEC 出向信息的下一跳，若是IP组播路由转发和Segment 类型的出向，打印“--”。






相关命令 :

无 




## show mpls multicast forwarding-table mte static-fec 


show mpls multicast forwarding-table mte static-fec 




命令功能 :

显示静态MPLS MTE  FEC转发表 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls multicast forwarding-table mte static-fec 
 local-tunnel-id 
 ＜static-local-tunnel-id 
＞







命令参数解释 :



参数|描述
---|---
＜static-local-tunnel-id＞|静态MTE隧道本地Tunnel ID，范围1-4294967295








缺省 :

无 






使用说明 :

使用场景当用户需要查看静态MPLS MTE转发表信息，可以执行该命令指定MTE的local-tunnel-id查看。





范例 :

1. 打印static local tunnel ID 为1000 的转发表ZXROSNG#$ulticast forwarding-table mte  static-fec local-tunnel-id 1000Out-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDIngress-ID/Tunnel-ID/        Local Outgoing Out-entry          Next-hopLSP-ID                       Label Label--/1000/1                    ----  ----     [G]                ------/1000/1                    ----  31000    spi-0/1/0/1        10.1.1.1--/1000/1                    ----  31001    spi-0/1/0/2        10.1.1.2--/1000/2                    ----  ----     [V]zteztezte       ------/1000/2                    ----  31002    spi-0/1/0/1        10.1.1.1域信息说明Ingress-ID/Tunnel-Id/ LSP-ID ：显示动态FEC时，依次为Ingress节点的 LSR ID，隧道头节点Tunnel ID和LSP  ID；静态FEC时，Ingress Id不存在，打印“—”Tunnel ID 为静态Local Tunnel ID和静态 LSP ID Local Label ：FEC 的入标签，头节点FEC没有入标签，打印“--”Out Label ： FEC 的出标签，当出向是导入IP组播路由表转发时，出标签为“--”Out-entry ：FEC 的出口信息，可能的类型有FEC 的转发出接口，若有前导词(G)，表示导入组播公网路由表转发；若有前导词(V)表示导入组播私网路由表转发，接着打印私网VRF名称；若有前导词(S)，表示此出口为Segment类型的出向，接着打印Segment 的ID Next-hop ：FEC 出向信息的下一跳，若是IP组播路由转发和Segment 类型的出向，打印“--”






相关命令 :

无 




## show mpls multicast forwarding-table mte 


show mpls multicast forwarding-table mte 




命令功能 :

显示组播MPLS MTE转发表 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mpls multicast forwarding-table mte 
  [＜in-label 
＞] 







命令参数解释 :



参数|描述
---|---
＜in-label＞|入标签，范围：16-1048575








缺省 :

显示所有的组播MPLS MTE转发表项 






使用说明 :

使用场景当用户需要查看MPLS MTE转发表信息，可以执行该命令。注意事项1、默认显示所有MTE FEC转发表信息。2、输入入标签查询指定的MTE FEC转发表信息。






范例 :

1.  显示入标签为1048的转发表项：ZXROSNG#show mpls multicast forwarding-table mte 1048Out-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDIngress-ID/Tunnel-ID/        Local Outgoing Out-entry          Next-hopLSP-ID                       Label Label--26/1025                    1048   1031     xgei-0/20/0/1     3.3.3.9--26/1025                    1048   5031     smartgroup2       4.4.4.92. 显示所有MTE LSP 的转发表ZXROSNG#show mpls multicast forwarding-table mte Out-entry type codes: V: VRF Name  G: Global IP Forwarding S: P2MP Segment IDIngress-ID/Tunnel-ID/        Local Outgoing Out-entry          Next-hopLSP-ID                       Label Label--/1000/1                    ----  ----     [G]               ------/1000/1                    ----  31000    spi-0/1/0/1        10.1.1.19.1.1.1/1/3                  21202 ----     [G]                ----9.1.1.1/1/3                  21202 31014    gei-0/1/0/1        10.1.1.59.1.1.1/1/3                  21202 ----     [S)10100           ----域信息说明域   ：      描述Ingress-ID/Tunnel-ID/ LSP-ID ：显示的是动态FEC时，依次为Ingress节点的 LSR ID，隧道头节点Tunnel ID和LSP ID；显示静态FEC时，Ingress ID不存在，打印“—”，Tunnel ID 为静态Local Tunnel ID，然后是静态 LSP ID Local Label ：FEC 的入标签，头节点FEC没有入标签，打印“--”Out Label ： FEC 的出标签，当出向是导入IP组播路由表转发或Segment时，出标签为“--”Out-entry ：FEC 的出口信息，可能的类型有FEC 的转发出接口，若有前导词(G)，表示导入组播公网路由表转发；若有前导词(V)表示导入组播私网路由转发，接着打印私网VRF名称；若有前导词(S)，表示此出口为Segment类型的出向，接着打印Segment 的ID Next-hop ：FEC 出向信息的下一跳，若是转入IP组播路由转发或Segment 类型的出向，打印“--”






相关命令 :

无 




## srv6 end-dt-sid 


srv6 end-dt-sid 




命令功能 :

该命令用于配置公网VRF实例下DT类型的SRv6 SID，使用no命令删除该配置。 






命令模式 :

 VRF-public模式,VRF模式  






命令默认权限级别 :

VRF模式:15,VRF-public模式:15 






命令格式 :



srv6 end-dt-sid 
  {auto 
|static 
 ＜ipv6-address 
＞}

no srv6 end-dt-sid 








命令参数解释 :



参数|描述
---|---
auto|配置自动生成SID
static|配置生成静态SID
＜ipv6-address＞|SRv6 SID的偏移量








缺省 :

无 






使用说明 :

使用场景配置公网的SRv6 SID的分配方式。注意事项1.自动产生和静态配置的DT类型的SRv6 SID互斥。2.DT类型的SRv6 SID和DX类型的SRv6 SID互斥。3.静态的DT类型的SRv6 SID只能配置一个，配置新的静态的DT类型的SRv6 SID会自动覆盖原有的配置。4.当且仅当VRF-public-IPv4地址族模式或者VRF-public-IPv6地址族模式下没有配置Srv6 SID的分配方式时使用VRF-public模式下的配置。






范例 :

VRF-public模式下配置自动生成SRv6 DT SID，则输入以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-public-vrf)#srv6 end-dt-sid auto






相关命令 :

show ip vrf-public detail 




## srv6 end-dt-sid 


srv6 end-dt-sid 




命令功能 :

该命令用于配置VRF-public-IPv4地址族下DT类型的SRv6 SID，使用no命令删除该配置。 






命令模式 :

 VRF-IPv4地址族模式,VRF-public-IPv4地址族模式  






命令默认权限级别 :

VRF-IPv4地址族模式:15,VRF-public-IPv4地址族模式:15 






命令格式 :



srv6 end-dt-sid 
  {auto 
|static 
 ＜ipv6-address 
＞}

no srv6 end-dt-sid 








命令参数解释 :



参数|描述
---|---
auto|配置自动生成SID
static|配置生成静态SID
＜ipv6-address＞|SRv6 SID的偏移量








缺省 :

无 






使用说明 :

使用场景配置公网的SRv6 SID的分配方式注意事项1.自动产生和静态配置的DT类型的SRv6 SID互斥。2.DT类型的SRv6 SID和DX类型的SRv6 SID互斥。3.静态的DT类型的SRv6 SID只能配置一个，配置新的静态的DT类型的SRv6 SID会自动覆盖原有的配置。






范例 :

VRF-public-IPv4地址族模式下配置静态SRv6 DT SID ::20，则输入以下命令：ZXROSNG(config)#ip vrf-publicZXROSNG(config-public-vrf)#rd 1:1ZXROSNG(config-public-vrf)#address-family ipv4ZXROSNG(config-public-vrf-af-ipv4)#srv6 end-dt-sid static ::20






相关命令 :

show ip vrf-public detail 




## srv6 end-dt-sid 


srv6 end-dt-sid 




命令功能 :

该命令用于配置VRF-public-IPv6地址族下的DT类型的SRv6 SID，使用no命令删除该配置。 






命令模式 :

 VRF-IPv6地址族模式,VRF-public-IPv6地址族模式  






命令默认权限级别 :

VRF-IPv6地址族模式:15,VRF-public-IPv6地址族模式:15 






命令格式 :



srv6 end-dt-sid 
  {auto 
|static 
 ＜ipv6-address 
＞}

no srv6 end-dt-sid 








命令参数解释 :



参数|描述
---|---
auto|配置自动生成SID
static|配置生成静态SID
＜ipv6-address＞|SRv6 SID的偏移量








缺省 :

无 






使用说明 :

使用场景配置公网的SRv6 SID的分配方式。注意事项1.自动产生和静态配置的DT类型的SRv6 SID互斥。2.DT类型的SRv6 SID和DX类型的SRv6 SID互斥。3.静态的DT类型的SRv6 SID只能配置一个，配置新的静态的DT类型的SRv6 SID会自动覆盖原有的配置。






范例 :

VRF-public-IPv6地址族模式下配置静态SRv6 DT SID ::20，则输入以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-public-vrf)#address-family ipv6ZXROSNG(config-public-vrf-af-ipv6)#srv6 end-dt-sid static ::20






相关命令 :

show ip vrf-public detail 




## srv6 end-dx-sid auto 


srv6 end-dx-sid auto 




命令功能 :

该命令用于配置VRF-public-IPv6地址族下自动产生DX类型的SRv6 SID，使用no命令删除该配置。 






命令模式 :

 VRF-IPv4地址族模式,VRF-public-IPv4地址族模式  






命令默认权限级别 :

VRF-IPv4地址族模式:15,VRF-public-IPv4地址族模式:15 






命令格式 :



srv6 end-dx-sid auto 
 

no srv6 end-dx-sid auto 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

使用场景配置公网的SRv6 SID的分配方式。注意事项1.该命令和同一模式下srv6-end-dx static互斥。2.DX类型的SRv6 SID和DT类型的SRv6 SID互斥。3.对于公网路由，如果存在下一跳且下一跳非本地地址，那么发布公网路由时，会依据配置产生 DX类型的SRv6公网路由，SRv6公网路由出项信息会继承公网路由的下一跳和出接口；4.对于公网路由，如果不存在下一跳（如聚会路由）或下一跳为本地地址（如直连路由），那么发布公网路由时，不再依据配置产生DX类型的SRv6公网路由，只会产生DT类型的SRv6公网路由。






范例 :

VRF-public-IPv4地址族模式下自动产生DX类型的SRv6 SID，则输入以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-public-vrf)#rd 1:1ZXROSNG(config-public-vrf)#address-family ipv4ZXROSNG(config-public-vrf-af-ipv4)#srv6 end-dx-sid auto






相关命令 :

show ip vrf-public detail 




## srv6 end-dx-sid auto 


srv6 end-dx-sid auto 




命令功能 :

该命令用于配置VRF-public-IPv4地址族下自动产生DX类型的SRv6 SID，使用no命令删除该配置。 






命令模式 :

 VRF-IPv6地址族模式,VRF-public-IPv6地址族模式  






命令默认权限级别 :

VRF-IPv6地址族模式:15,VRF-public-IPv6地址族模式:15 






命令格式 :



srv6 end-dx-sid auto 
 

no srv6 end-dx-sid auto 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

使用场景配置公网的SRv6 SID的分配方式注意事项1.该命令和同一模式下srv6-end-dx static互斥。2.DX类型的SRv6 SID和DT类型的SRv6 SID互斥。3.对于公网路由，如果存在下一跳且下一跳非本地地址，那么发布公网路由时，会依据配置产生 DX类型的SRv6公网路由，SRv6公网路由出项信息会继承公网路由的下一跳和出接口。 4.对于公网路由，如果不存在下一跳（如聚会路由）或下一跳为本地地址（如直连路由），那么发布公网路由时，不再依据配置产生DX类型的SRv6公网路由，只会产生DT类型的SRv6公网路由。






范例 :

VRF-public-IPv6地址族模式下自动产生DX类型的SRv6 SID，则输入以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-public-vrf)#rd 1:1ZXROSNG(config-public-vrf)#address-family ipv6ZXROSNG(config-public-vrf-af-ipv6)#srv6 end-dx-sid auto






相关命令 :

show ip vrf-public detail 




## srv6 end-dx-sid static 


srv6 end-dx-sid static 




命令功能 :

该命令用于配置VRF-public-IPv4地址族下静态的DX类型的SRv6 SID,使用no命令删除该配置。 






命令模式 :

 VRF-IPv4地址族模式,VRF-public-IPv4地址族模式  






命令默认权限级别 :

VRF-IPv4地址族模式:15,VRF-public-IPv4地址族模式:15 






命令格式 :


srv6 end-dx-sid static 
  ＜interface-name 
＞ ＜ipv4-address 
＞ ＜ipv6-address 
＞
no srv6 end-dx-sid static 
  ＜interface-name 
＞ ＜ipv4-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|出接口名称
＜ipv4-address＞|下一跳的IPv4地址
＜ipv6-address＞|SRv6 SID的偏移量








缺省 :

无 






使用说明 :

使用场景配置公网的SRv6 SID的分配方式注意事项1.该命令和srv6 end-dx-sid auto互斥2.DX类型的SRv6 SID和DT类型的SRv6 SID互斥。3.DX类型的静态SRv6 SID可以配置多个。4.对于公网路由，如果存在下一跳且下一跳非本地地址，那么发布公网路由时，会依据配置产生DX类型的SRv6公网路由，SRv6公网路由出项信息会继承公网路由的下一跳和出接口； 5.对于公网路由，如果不存在下一跳（如聚合路由）或下一跳为本地地址（如直连路由），那么发布公网路由时，不再依据配置产生DX类型的SRv6公网路由，只会产生DT类型的SRv6公网路由.






范例 :

VRF-public-IPv4地址族模式下配置静态的DX类型的SRv6 SID的出接口为gei-0/20/0/1，下一跳为3.1.1.1，SRv6 SID为::2，则输入以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-public-vrf)#rd 1:1ZXROSNG(config-public-vrf)#address-family ipv4ZXROSNG(config-public-vrf-af-ipv4)#srv6 end-dx-sid static gei-0/20/0/1 3::1 ::2






相关命令 :

show ip vrf-public detail 




## srv6 end-dx-sid static 


srv6 end-dx-sid static 




命令功能 :

该命令用于配置VRF-public-IPv6地址族下静态的DX类型的SRv6 SID，使用no命令删除该配置。 






命令模式 :

 VRF-IPv6地址族模式,VRF-public-IPv6地址族模式  






命令默认权限级别 :

VRF-IPv6地址族模式:15,VRF-public-IPv6地址族模式:15 






命令格式 :


srv6 end-dx-sid static 
  ＜interface-name 
＞ ＜ipv6-address 
＞ ＜ipv6-address 
＞
no srv6 end-dx-sid static 
  ＜interface-name 
＞ ＜ipv6-address 
＞
				






命令参数解释 :



参数|描述
---|---
＜interface-name＞|出接口名称
＜ipv6-address＞|下一跳的IPv6地址
＜ipv6-address＞|SRv6 SID的偏移量








缺省 :

无 






使用说明 :

配置公网的SRv6 SID的分配方式。注意事项1该命令和同一模式下的srv6 end-dx-sid auto互斥。2.DX类型的SRv6 SID和DT类型的SRv6 SID互斥。3.3.DX类型的静态SRv6 SID可以配置多个。4.对于公网路由，如果存在下一跳且下一跳非本地地址，那么发布公网路由时，会依据配置产生 DX类型的SRv6公网路由，SRv6公网路由出项信息会继承公网路由的下一跳和出接口。 5.对于公网路由，如果不存在下一跳（如聚合路由）或下一跳为本地地址（如直连路由），那么发布公网路由时，不再依据配置产生DX类型的SRv6公网路由，只会产生DT类型的SRv6公网路由。






范例 :

VRF-public-IPv6地址族模式下配置静态的DX类型的SRv6 SID的出接口为gei-0/20/0/1，下一跳为3::1，SRv6 SID为::2，则输入以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-public-vrf)#rd 1:1ZXROSNG(config-public-vrf)#address-family ipv6ZXROSNG(config-public-vrf-af-ipv6)#srv6- end-dx-sid static gei-0/20/0/1 3::1 ::2






相关命令 :

show ip vrf-public detail 




## srv6 locator 


srv6 locator 




命令功能 :

该命令用于将当前VPN实例与SR模块的SRv6 locator通过名字相关联。使用no命取消当前VPN实例与SR模块的SRv6 locator的关联。 






命令模式 :

 VRF-public模式,VRF模式  






命令默认权限级别 :

VRF模式:15,VRF-public模式:15 






命令格式 :



srv6 locator 
  ＜name 
＞

no srv6 locator 








命令参数解释 :



参数|描述
---|---
＜name＞|与VRF实例关联的SR模块的SRv6 locator名称。字符串类型，长度1-31，不支持空格，区分大小写。








缺省 :

无 






使用说明 :

（1）配置该命令时不会检查对应的SRv6 locator名称是否存在。（2）一个VPN实例只能与SR模块的一个SRv6 locator名称相关联，以最后关联的SRv6 locator名称为准。（3）缺省情况下，VPN实例与SR模块的任何SRv6 locator没有关联。






范例 :

当需要为名称是zte的VRF实例关联一个SR模块的SRv6 locator，使用以下命令：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)# srv6 locator test






相关命令 :

show ip vrf detail [<vrf-name>] 




## static-inlabel 


static-inlabel 




命令功能 :

该命令工作于VRF模式，用于为VPN实例指定静态入标签值。MP_IBGP邻居发送的报文时会携带这一标签值，PE收到MP_IBGP邻居发过来的报文时根据这一标签值查找出接口，把报文发送到目的地。使用no命令删除配置。






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :


static-inlabel 
  ＜in-label-value 
＞

no static-inlabel 








命令参数解释 :



参数|描述
---|---
＜in-label-value＞|静态入标签的值。取值范围：最大取值范围是16~1048575，但实际可配置的范围可以动态变化，具体的生效范围可以通过对应show命令查看。默认值：无。








缺省 :

无 






使用说明 :

（1）必须通过rd命令配置过RD数据之后才可以使用本命令配置。（2）在通过mpls label mode命令将标签分配方式设置为per-vrf时，static-inlabel命令的配置值才有效。（3）不配置静态静态入标签时，VPN路由使用的入标签值由标签模块动态分配。





范例 :

配置名称为zte的VPN的静态入标签为123：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#static-inlabel 123ZXROSNG(config-vrf-zte)#






相关命令 :

show ip vrf detail 




## static-outlabel 


static-outlabel 




命令功能 :

该命令工作于VRF-IPv4地址族模式，为下一跳是远端PE的本地静态VPN路由设置outlabel（出标签）。使用no命令删除配置。






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :


static-outlabel 
  ＜ipv6-address 
＞ ＜out-label-value 
＞
no static-outlabel 
  {＜ipv6-address 
＞}
				






命令参数解释 :



参数|描述
---|---
＜ipv6-address＞|待指定outlabel（出标签）的IPv6地址。取值范围：有效单播地址均可配置，一般为PE邻居的地址。默认值：无。
＜out-label-value＞|取值含义：指定的静态outlabel（出标签）值。取值范围：16~1048575。








缺省 :

无 






使用说明 :

（1）此命令在静态VPN组网下使用，不同PE的静态outlabel（出标签值）可以相同也可以不同。（2）本端配置的outlabel（出标签值）必须和远端PE配置的inlabel（入标签值）一致。






范例 :

为远端PE（地址为100::1）配置静态outlabel（出标签）为25：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#static-outlabel 100::1 25ZXROSNG(config-vrf-zte-af-ipv6)#






相关命令 :

show ip vrf detail 




## static-outlabel 


static-outlabel 




命令功能 :

该命令工作于VRF-IPv4地址族模式，为下一跳是远端PE的本地静态VPN路由设置outlabel（出标签）。使用no命令删除配置。






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :


static-outlabel 
  ＜ip-address 
＞ ＜out-label-value 
＞
no static-outlabel 
  {＜ip-address 
＞}
				






命令参数解释 :



参数|描述
---|---
＜ip-address＞|待指定outlabel（出标签）的IP地址。取值范围：有效单播地址均可配置，一般为PE邻居的地址。默认值：无。
＜out-label-value＞|取值含义：指定的静态outlabel（出标签）值。取值范围：16~1048575。








缺省 :

无 






使用说明 :

（1）此命令在静态VPN组网下使用，不同PE的静态outlabel（出标签值）可以相同也可以不同。（2）本端配置的outlabel（出标签值）必须和远端PE配置的inlabel（入标签值）一致。





范例 :

为远端PE（地址为1.2.3.4）配置静态outlabel（出标签）为25：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#static-outlabel 1.2.3.4 25ZXROSNG(config-vrf-zte-af-ipv4)#






相关命令 :

show ip vrf detail 




## ttl-mode 


ttl-mode 




命令功能 :

该命令工作于VRF模式，用于控制MPLS标签中的TTL域和IP头中的TTL域间的处理模式，缺省情况下，MPLS对TTL的处理模式为uniform模式。使用no命令恢复默认值。






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :


ttl-mode 
  {uniform 
|pipe 
}

no ttl-mode 








命令参数解释 :



参数|描述
---|---
uniform|和pipe是二选一，若设置为uniform，则表示：报文进入MPLS标签交换网，标签交换网认为其上游的IP路由网是可信的，依据IP报头中的TTL字段生成标签中的TTL。报文出MPLS标签交换网，IP路由网认为标签交换网是可信的，依据标签中的TTL修改IP报头中的TTL。
pipe|和uniform是二选一，若设置为pipe，则表示：报文进入MPLS标签交换网，标签中的TTL设置为255。报文出MPLS标签交换网，IP报头中的TTL设置为255








缺省 :

缺省状态下为uniform模式。 






使用说明 :

（1）必须通过rd命令配置过RD数据之后才可以使用本命令配置。 






范例 :

给名称为zte的VRF配置TTL模式为uniform模式：ZXROSNG(config)#ip vrf zteZXROSNG(config)#rd 1:1ZXROSNG(config-vrf-zte)#ttl-mode uniformZXROSNG(config-vrf-zte)#






相关命令 :

show ip vrf detail 




## tunnel-policy 


tunnel-policy 




命令功能 :

该命令工作于VRF-IPv4地址族模式，用于指定从PE邻居接收导入本地的VPN路由流量所走的隧道策略。使用no命令删除。 






命令模式 :

 VRF-IPv6地址族模式  






命令默认权限级别 :

15 






命令格式 :



tunnel-policy 
  ＜tunnel-policy-name 
＞

no tunnel-policy 








命令参数解释 :



参数|描述
---|---
＜tunnel-policy-name＞|取值含义：隧道策略名称。取值范围：1~63位的字符串，不包含空格，区分大小写。默认值：无。








缺省 :

无 






使用说明 :

1.该命令和VRF-IPv4地址族模式下的命令peer tunnel-policy互斥2.该命令和VRF-IPv6地址族模式下的命令peer tunnel-policy互斥






范例 :

指定从地址为1.2.3.4的PE邻居导入本地的VPN流量走名为abc的外层隧道：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv4ZXROSNG(config-vrf-zte-af-ipv4)#tunnel-policy abc






相关命令 :

show ip vrf detailpeer <mid> tunnel-policy




## tunnel-policy 


tunnel-policy 




命令功能 :

该命令工作于VRF-IPv6地址族模式，用于指定VPN路由流量所走的隧道策略，使用no命令删除； 






命令模式 :

 VRF-IPv4地址族模式  






命令默认权限级别 :

15 






命令格式 :



tunnel-policy 
  ＜tunnel-policy-name 
＞

no tunnel-policy 








命令参数解释 :



参数|描述
---|---
＜tunnel-policy-name＞|隧道策略名称，长度1-63个字符








缺省 :

无 






使用说明 :

1.该命令和VRF-IPv4地址族模式下的命令peer tunnel-policy互斥2.该命令和VRF-IPv6地址族模式下的命令peer tunnel-policy互斥






范例 :

ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#address-family ipv6ZXROSNG(config-vrf-zte-af-ipv6)#tunnel-policy abcdef






相关命令 :

show ip vrf detailpeer <mid> tunnel-policy




## vni-label 


vni-label 




命令功能 :

该命令工作于VRF模式，用于配置EVPN 三层VNI标签。使用no命令删除该配置。 






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :



vni-label 
  ＜L3 VNI-label 
＞

no vni-label 








命令参数解释 :



参数|描述
---|---
＜L3 VNI-label＞|EVPN三层VNI标签值。取值范围：1~16777215，无默认值。








缺省 :

无 






使用说明 :

（1）    必须配置过RD配置该命令。（2）    该命令与VRF-IPv4地址族模式下的evpn gw-ip互斥。（3）    三层VNI标签值必须与二层VNI标签值不同。（4）    不同VRF下配置的三层VNI标签值必须不同。





范例 :

在名称为zte的VRF下配置EVPN三层VNI标签为123：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#rd 1:1ZXROSNG(config-vrf-zte)#vni-label 123ZXROSNG(config-vrf-zte)#





相关命令 :

show ip vrf detail [<vrf-name>] 




## vpn-id 


vpn-id 




命令功能 :

该命令工作于VRF模式，用于配置RFC2685协议中定义的虚拟专用网标识符。使用no命令删除配置。这一标识符主要用于在MIB中为VPN配置属性。






命令模式 :

 VRF模式  






命令默认权限级别 :

15 






命令格式 :


vpn-id 
  ＜vnp-id 
＞

no vpn-id 








命令参数解释 :



参数|描述
---|---
＜vnp-id＞|用于为VRF实例指定RFC2685中定义的global vpnid。取值范围：格式<3 bytes OUI:4 bytes VPN_Index>，冒号前后的字符只能是十六进制，冒号前为1~6个字符，冒号后为1~8个字符，冒号前和冒号后均为0字符时配置无效。默认值：无。








缺省 :

无 






使用说明 :

（1）无需配置RD便可配置。（2）冒号前和冒号后均为0字符时配置无效。（3）配置字符只能是十六进制，配置小写字母时会自动转换成大写字母生效。（4）同一个VRF实例可以配置多次vpn-id，以最后一次的配置为准。（5）不同VRF实例的vpn-id不可重复。






范例 :

给名称为zte的VPN设置全局vpnid为“123:abc”：ZXROSNG(config)#ip vrf zteZXROSNG(config-vrf-zte)#vpn-id 123:abcZXROSNG(config-vrf-zte)#






相关命令 :

show ip vrf detail 




## vrf reserved-vpnid-range 


vrf reserved-vpnid-range 




命令功能 :

配置VRF实例的保留VPN ID范围。 






命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :



vrf reserved-vpnid-range 
  ＜Minimum VPN ID value 
＞ ＜Maximum VPN ID value 
＞

no vrf reserved-vpnid-range 








命令参数解释 :



参数|描述
---|---
＜Minimum VPN ID value＞|保留VPN ID最小值,取值范围：1-$#117637121#$
＜Maximum VPN ID value＞|保留VPN ID最大值取值范围：1-$#117637121#$，








缺省 :

无 






使用说明 :

1. 在保留范围内的VPN ID不能分配给设备上创建的VRF实例。2. 设置的保留VPN ID范围必须和已经存在VRF实例的VPN ID不冲突。3. 上电的时候vrf reserved-vpnid-range命令先加载，后面加载的VRF实例如果VPN ID和保留VPN ID范围有冲突就不生效。






范例 :

配置VRF保留VPN ID范围为1000~2000:ZXROSNG(config)#vrf reserved-vpnid-range 1000 2000






相关命令 :

配置VRF保留VPN ID范围为1000~2000:ZXROSNG(config)#vrf reserved-vpnid-range 1000 2000




# MC-ELAM配置命令 
## bind smartgroup 


bind smartgroup 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置聚合组关联MC-ELAM实例及其协商模式。





命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :


bind smartgroup 
  ＜smartgroup-id 
＞ [mode 
 {auto 
|master 
|slave 
}]

no bind smartgroup 








命令参数解释 :



参数|描述
---|---
＜smartgroup-id＞|<作用> 需要关联的聚合组组号。<取值范围>最大值由项目性能参数设置，平台默认最大值为64，默认范围1–$#83951617#$。
auto|<作用>主备自动协商模式。
master|<作用>主用模式。
slave|<作用>备用模式。








缺省 :

主备自动协商模式 






使用说明 :

该命令用于配置聚合组关联MC-ELAM实例及其协商模式，可使用no命令配置MC-ELAM实例去关联聚合组。 






范例 :

主备自动协商模式ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#bind smartgroup 1或ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#bind smartgroup 1 mode auto主用模式ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#bind smartgroup 1  mode master备用模式ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#bind smartgroup 1 mode slaveno命令ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#no bind smartgroup





相关命令 :

无 




## destination 


destination 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置MC-ELAM实例的目的IP地址。 






命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :



destination 
  ＜ip-address 
＞







命令参数解释 :



参数|描述
---|---
＜ip-address＞|<作用>MC-ELAM实例的目的IP地址。








缺省 :

无 






使用说明 :

MC-ELAM实例对应的对端IP地址，设置成对端的LOOPBACK口地址。 






范例 :

ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#destination 1.1.1.2 






相关命令 :

无 




## detect-multiplier 


detect-multiplier 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置MC-ELAM实例的协议报文超时时间倍数。 






命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :



detect-multiplier 
  ＜detect-multiplier 
＞

no detect-multiplier 








命令参数解释 :



参数|描述
---|---
＜detect-multiplier＞|<作用> 配置MC-ELAM实例的协议报文超时时间倍数。<取值范围>超时时间倍数为3-180。<默认值>5。








缺省 :

5 






使用说明 :

该命令用于配置MC-ELAM实例的协议报文超时时间倍数，可使用no命令恢复成缺省超时时间倍数。 






范例 :

ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#detect-multiplier 6no命令ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#no detect-multiplier





相关命令 :

无 




## mc-elam 


mc-elam 




命令功能 :

该命令工作于MC-ELAM模式，用于创建指定的MC-ELAM实例，并从MC-ELAM模式进入MC-ELAM实例配置模式。 






命令模式 :

 MC-ELAM模式  






命令默认权限级别 :

15 






命令格式 :


mc-elam 
  ＜mcelam-instance-id 
＞
no mc-elam 
  ＜mcelam-instance-id 
＞
				






命令参数解释 :



参数|描述
---|---
＜mcelam-instance-id＞|<作用> 配置MC-ELAM实例号。








缺省 :

无 






使用说明 :

当实例不存在时创建并进入该实例，如果实例存在直接进入改实例，可使用no命令删除指定的MC-ELAM实例。 






范例 :

ZXROSNG(config-mc-elam-configuration)#mc-elam 1ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#no命令ZXROSNG(config-mc-elam-configuration)#no mc-elam 1





相关命令 :

无 




## mc-elam-configuration 


mc-elam-configuration 




命令功能 :

该命令工作于全局配置模式，用于进入MC-ELAM配置模式。





命令模式 :

 全局配置模式  






命令默认权限级别 :

15 






命令格式 :


mc-elam-configuration 
 






命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

该命令用于进入MC-ELAM配置模式。 






范例 :

ZXROSNG(config)#mc-elam-configuration ZXROSNG(config-mc-elam-configuration)#





相关命令 :

无 




## restore 


restore 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置MC-ELAM实例的回切模式及回切时间。





命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :


restore 
  {revertive 
 ＜revertive-time 
＞|immediately 
|non-revertive 
}

no restore 








命令参数解释 :



参数|描述
---|---
＜revertive-time＞|<作用> 配置MC-ELAM实例的回切模式，<holdoff-time>为回切等待时间。<取值范围>1~120。
immediately|<作用>配置MC-ELAM实例的立即回切模式。
non-revertive|<作用>配置MC-ELAM实例的不回切模式。








缺省 :

立即回切 






使用说明 :

该命令用于配置MC-ELAM实例的回切模式及回切时间，在配置revertive模式时才可以配置回切时间，可使用no命令恢复成缺省回切时间。 






范例 :

MC-ELAM实例的回切模式ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#restore revertive 30MC-ELAM实例的立即回切模式ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#restore immediatelyMC-ELAM实例的不回切模式ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#restore non-revertiveno命令恢复成立即回切模式ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#no restore





相关命令 :

无 




## show mc-elam 


show mc-elam 




命令功能 :

该命令工作于除用户模式外的其他所有模式，用于显示设备所有MC-ELAM实例的信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show mc-elam 
  {＜mcelam- instance-id 
＞|all 
|brief 
} 







命令参数解释 :



参数|描述
---|---
＜mcelam- instance-id＞|<作用>显示指定MC-LAM的实例信息。
all|<作用>显示MC-LAM的所有相关信息。
brief|<作用>只显示MC-LAM及关联的SG接口的主备用状态。








缺省 :

无 






使用说明 :

该命令用于显示设备所有MC-ELAM实例的信息。 






范例 :

ZXROSNG(config)#show mc-elam 1ZXROSNG(config)#show mc-elam allZXROSNG(config)#show mc-elam brief





相关命令 :

无 




## source 


source 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置MC-ELAM实例的源IP地址。 






命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :



source 
  ＜ip-address 
＞







命令参数解释 :



参数|描述
---|---
＜ip-address＞|<作用> 配置MC-ELAM实例的源IP地址。








缺省 :

无 






使用说明 :

该命令用于MC-ELAM实例的源IP地址，在配置时设为LOOPBACK口地址。 






范例 :

ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#source 1.1.1.1 






相关命令 :

无 




## system-mac 


system-mac 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置MC-ELAM实例的系统MAC。 






命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :



system-mac 
  ＜mac-address 
＞

no system-mac 








命令参数解释 :



参数|描述
---|---
＜mac-address＞|<作用>配置MC-ELAM实例系统MAC。<默认值>系统基MAC。








缺省 :

系统基MAC 






使用说明 :

该命令用于配置MC-ELAM实例的系统MAC，本端和对端的系统优先级相同的情况下，选择系统MAC优先级高的一端作为主的MC-ELAM。系统MAC的值越小代表优先级越高。可使用no命令恢复为缺省值。 






范例 :

ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#system-mac 0019.8407.2310no命令ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#no system-mac





相关命令 :

无 




## system-priority 


system-priority 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置MC-ELAM实例的系统优先级。 






命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :



system-priority 
  ＜system-priority 
＞

no system-priority 








命令参数解释 :



参数|描述
---|---
＜system-priority＞|<作用>配置MC-ELAM实例系统优先级。<取值范围>1~65535。<默认值>32768。








缺省 :

32768 






使用说明 :

配置了该命令后，根据本端和对端的系统优先级高的一端作为主的MC-ELAM。系统优先级的值越小代表优先级越高。 






范例 :

ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#system-priority 1no命令ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#no system-priority





相关命令 :

无 




## timeradvertise 


timeradvertise 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置MC-ELAM实例的协议报文发送周期。 






命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :



timeradvertise 
  ＜timer-advertise 
＞

no timeradvertise 








命令参数解释 :



参数|描述
---|---
＜timer-advertise＞|<作用>配置MC-ELAM实例的协议报文发送周期，单位100毫秒。<取值范围>5-100。<默认值>10。








缺省 :

10 






使用说明 :

该命令用于配置MC-ELAM实例的协议报文发送周期，可使用no命令恢复为默认发送周期。





范例 :

ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#timeradvertise 5no命令ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#no timeradvertise





相关命令 :

无 




track :

track 




命令功能 :

该命令工作于MC-ELAM实例模式，用于配置MC-ELAM实例与SAMGR的联动关系。 






命令模式 :

 MC-ELAM实例模式  






命令默认权限级别 :

15 






命令格式 :


track 
  ＜track-name 
＞ {link-type 
|peer-type 
|pw-type 
}
no track 
  ＜track-name 
＞
				






命令参数解释 :



参数|描述
---|---
＜track-name＞|<作用>指定跟踪的track对象名称。
link-type|<作用>按Link类型处理。
peer-type|<作用>按Peer类型处理。
pw-type|<作用>按公网pw类型处理。








缺省 :

无 






使用说明 :

该命令用于配置MC-ELAM实例与SAMGR的检测联动，link-type关注AC链路组，peer-type关注PE设备，pw-type关注公网pw。可使用no命令解除MC-ELAM实例与SAMGR的联动关系。 






范例 :

配置MC-ELAM实例与SAMGR的Link类型的联动ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#track 1 link-type配置MC-ELAM实例与SAMGR的Peer类型的联动ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#track 1 peer-type配置MC-ELAM实例与SAMGR的pw类型的联动ZXROSNG(config-mc-elam-configuration-mc-elam-instance)#track 1 pw-typeno命令ZXROSNG(config-lacp-member-if-gei-0/1/0/8)#no track 1





相关命令 :

无 




# PWE3显示命令 
## debug pwe3 all 


debug pwe3 all 




命令功能 :

打开或关闭PWE3所有调试信息 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug pwe3 all 
 

no debug pwe3 all 








命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

debug pwe3 all开启所有的调试信息no debug pwe3 all是关闭所有的调试信息






范例 :

ZXROSNG#debug pwe3 all All PWE3 debugging has been turned on






相关命令 :

无 




## debug pwe3 encode 


debug pwe3 encode 




命令功能 :

PWE3相关消息的编解码过程监视 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :



debug pwe3 encode 
 

no debug pwe3 encode 








命令参数解释 :


					无
				 






缺省 :

不监视编解码过程 






使用说明 :

debug pwe3 encode    打开对PWE3各种消息的编解码过程no debug pwe3 encode 关闭对PWE3各种消息的编解码过程






范例 :

ZXROSNG#debug pwe3 encode  PWE3 debugging encode is on






相关命令 :

无 




## debug pwe3 event 


debug pwe3 event 




命令功能 :

监视PWE3事件的调试信息，AC状态，Session状态。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug pwe3 event 
  [{fec128 
 peer 
 ＜ip-address 
＞ vcid 
 ＜vcid 
＞ pw-type 
 {ethernet 
 {raw 
|tagged 
}|ip 
|ppp 
|hdlc 
|fr 
 {port 
|dlci 
|dlci-old 
}|tdm 
 {aal1 
|aal2 
|satop 
 {e1 
|t1 
|e3 
|t3 
}|cesopsn 
 {basic 
|cas 
}|sonet-sdh 
 {cesom 
|ceop 
}}|atm 
 {port 
|vpc 
|vcc 
|vcc-group 
|vpc-group 
|sdu 
|pdu 
}}|fec129 
 peer 
 ＜ip-address 
＞ vpls-id 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
} pw-type 
 ethernet 
 {raw 
|tagged 
}}]
no debug pwe3 event 
  [{fec128 
 peer 
 ＜ip-address 
＞ vcid 
 ＜vcid 
＞ pw-type 
 {ethernet 
 {raw 
|tagged 
}|ip 
|ppp 
|hdlc 
|fr 
 {port 
|dlci 
|dlci-old 
}|tdm 
 {aal1 
|aal2 
|satop 
 {e1 
|t1 
|e3 
|t3 
}|cesopsn 
 {basic 
|cas 
}|sonet-sdh 
 {cesom 
|ceop 
}}|atm 
 {port 
|vpc 
|vcc 
|vcc-group 
|vpc-group 
|sdu 
|pdu 
}}|fec129 
 peer 
 ＜ip-address 
＞ vpls-id 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
} pw-type 
 ethernet 
 {raw 
|tagged 
}}]
				






命令参数解释 :



参数|描述
---|---
＜ip-address＞|PW对端的IP
＜vcid＞|PW标识ID
raw|PW类型：Ethernet
tagged|PW类型：Ethernet Tagged Mode
ip|PW类型：IP Layer2 Transport
ppp|PW类型：PPP
hdlc|PW类型：HDLC
port|PW类型： ATM transparent cell transport
dlci|PW类型：Frame Relay DLCI
dlci-old|PW类型：Frame Relay
aal1|PW类型：TDMoIP AAL1 Mode
aal2|PW类型：TDMoIP AAL2 Mode
e1|PW类型：SAToP E1
t1|PW类型：SAToP T1 (DS1)
e3|PW类型：SAToP E3
t3|PW类型：SAToP T3 (DS3)
basic|PW类型：CESoPSN basic mode
cas|PW类型：CESoPSN TDM with CAS
cesom|PW类型：SONET/SDH CESoM
ceop|PW类型：SONET/SDH CEoP
port|PW类型： ATM transparent cell transport
vpc|PW类型：  ATM one-to-one VPC cell mode
vcc|PW类型： ATM one-to-one VCC cell mode
vcc-group|PW类型： ATM n-to-one VCC cell transport
vpc-group|PW类型： ATM n-to-one VPC cell transport
sdu|PW类型： ATM transparent cell transport
pdu|PW类型： ATM AAL5 PDU VCC transport
＜ip-address＞|PW对端的IP
<0-65535>:<0-4294967295>|VPLS实例标识
A.B.C.D:<0-65535>|VPLS实例标识
raw|PW类型：Ethernet
tagged|PW类型：Ethernet Tagged Mode








缺省 :

不打开监视 






使用说明 :

（1）debug pwe3 event是对所有PW打开PWE3事件调试信息，比如AC状态，Session会话状态的变化，是基于全局的开关；也可以针对某个或者某些PW打开PWE3事件调试信息，是基于PW粒度的开关。目前支持最多打开16条PW，如debug pwe3 event fec128 peer 1.2.3.4 vcid 100 pw-type ethernet raw；本命令不同时支持打开全局和PW粒度的开关。（2）如果先打开了所有PW的PWE3事件调试信息，后又打开某个或者某些PW的PWE3事件调试信息，则提示用户要先关闭所有PW的PWE3事件调试信息，才可以打开的某个或者某些PW的PWE3事件调试信息。（3）如果先打开某个或者某些PW的PWE3事件调试信息，而后又开启所有PW的PWE3事件调试信息，则提示用户要先关闭所有已打开的基于PW粒度的PWE3事件调试信息，才可以开启所有PW的PWE3事件调试信息。（4）no debug pwe3 event 是对所有PW关闭对PWE3事件调试信息，也可以关闭某个PW已打开的PWE3事件调试信息，如no debug pwe3 event fec128 peer 1.2.3.4 vcid 100 pw-type ethernet raw。（5）如果打开的是某个或者某些PW的PWE3事件调试信息，执行no debug pwe3 event将关闭已打开的某个或者某些PW的PWE3事件调试信息。





范例 :

（1）ZXROSNG#debug pwe3 event    PWE3 debugging event is on（2）ZXROSNG#debug pwe3 event fec128 peer 100.100.1.2 vcid 100 pw-type ethernet raw     PWE3 debugging event is on（3）ZXROSNG#no debug pwe3 event    PWE3 debugging event is off（4）ZXROSNG#no debug pwe3 event fec128 peer 100.100.1.2 vcid 100 pw-type ethernet raw     PWE3 debugging event is off





相关命令 :

无 




## debug pwe3 signal 


debug pwe3 signal 




命令功能 :

监视PWE3信令交互信息，监视mapping消息、mapping withdraw消息等的收发情况。 






命令模式 :

 特权模式  






命令默认权限级别 :

2 






命令格式 :


debug pwe3 signal 
  [{fec128 
 peer 
 ＜ip-address 
＞ vcid 
 ＜vcid 
＞ pw-type 
 {ethernet 
 {raw 
|tagged 
}|ip 
|ppp 
|hdlc 
|fr 
 {port 
|dlci 
|dlci-old 
}|tdm 
 {aal1 
|aal2 
|satop 
 {e1 
|t1 
|e3 
|t3 
}|cesopsn 
 {basic 
|cas 
}|sonet-sdh 
 {cesom 
|ceop 
}}|atm 
 {port 
|vpc 
|vcc 
|vcc-group 
|vpc-group 
|sdu 
|pdu 
}}|fec129 
 peer 
 ＜ip-address 
＞ vpls-id 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
} pw-type 
 ethernet 
 {raw 
|tagged 
}}]
no debug pwe3 signal 
  [{fec128 
 peer 
 ＜ip-address 
＞ vcid 
 ＜vcid 
＞ pw-type 
 {ethernet 
 {raw 
|tagged 
}|ip 
|ppp 
|hdlc 
|fr 
 {port 
|dlci 
|dlci-old 
}|tdm 
 {aal1 
|aal2 
|satop 
 {e1 
|t1 
|e3 
|t3 
}|cesopsn 
 {basic 
|cas 
}|sonet-sdh 
 {cesom 
|ceop 
}}|atm 
 {port 
|vpc 
|vcc 
|vcc-group 
|vpc-group 
|sdu 
|pdu 
}}|fec129 
 peer 
 ＜ip-address 
＞ vpls-id 
 {<0-65535>:<0-4294967295> 
|A.B.C.D:<0-65535> 
} pw-type 
 ethernet 
 {raw 
|tagged 
}}]
				






命令参数解释 :



参数|描述
---|---
＜ip-address＞|PW对端的IP
＜vcid＞|PW标识ID
raw|PW类型：Ethernet
tagged|PW类型：Ethernet Tagged Mode
ip|PW类型：IP Layer2 Transport
ppp|PW类型：PPP
hdlc|PW类型：HDLC
port|PW类型：ATM transparent cell transport
dlci|PW类型：Frame Relay DLCI
dlci-old|PW类型：Frame Relay
aal1|PW类型：TDMoIP AAL1 Mode
aal2|PW类型：TDMoIP AAL2 Mode
e1|PW类型：SAToP E1
t1|PW类型：SAToP T1 (DS1)
e3|PW类型：SAToP E3
t3|PW类型：SAToP T3 (DS3)
basic|PW类型：CESoPSN basic mode
cas|PW类型：CESoPSN TDM with CAS
cesom|PW类型：SONET/SDH CESoM
ceop|PW类型：SONET/SDH CEoP
port|PW类型：ATM transparent cell transport
vpc|PW类型：  ATM one-to-one VPC cell mode
vcc|PW类型： ATM one-to-one VCC cell mode
vcc-group|PW类型： ATM n-to-one VCC cell transport
vpc-group|PW类型： ATM n-to-one VPC cell transport
sdu|PW类型： ATM transparent cell transport
pdu|PW类型： ATM AAL5 PDU VCC transport
＜ip-address＞|PW对端的IP
<0-65535>:<0-4294967295>|VPLS实例标识
A.B.C.D:<0-65535>|VPLS实例标识
raw|PW类型：Ethernet
tagged|PW类型：Ethernet Tagged Mode








缺省 :

不监视信令交互信息。 






使用说明 :

（1）debug pwe3 signal是对所有PW打开PWE3信令交互过程，是基于全局的开关；也可以针对某个或者某些PW打开PWE3信令交互过程，是基于PW粒度的开关。目前支持最多打开16条PW，如debug pwe3 signal fec128 peer 1.2.3.4 vcid 100 pw-type ethernet raw，本命令不支持同时打开基于全局和PW粒度的开关。（2）如果先打开了所有PW的PWE3信令交互过程，而后又打开某个或者某些PW的PWE3信令交互过程，则提示用户先要关闭已打开所有PW的PWE3信令交互过程，之后才可以打开某个或者某些PW的PWE3信令交互过程。（3）如果先打开某个或者某些PW的PWE3信令交互过程，而后又开启所有PW的PWE3信令交互过程，则提示用户先关闭基于某个或者某些PW的PWE3信令交互过程后，才可以开启所有PW的PWE3信令交互过程。（4）no debug pwe3 signal 是对所有PW关闭PWE3信令交互过程，也可以关闭某个已打开PW的PWE3信令交互过程，如no debug pwe3 signal fec128 peer 1.2.3.4 vcid 100 pw-type ethernet raw。（5）如果打开的是某个或者某些PW的PWE3信令交互过程，执行no debug pwe3 signal后将关闭已打开的某个或者某些PW的PWE3信令交互过程。





范例 :

（1）ZXROSNG#debug pwe3 signal    PWE3 debugging signal is on（2）ZXROSNG#debug pwe3 signal fec128 peer 100.100.1.2 vcid 100 pw-type ethernet raw     PWE3 debugging signal is on（3）ZXROSNG#no debug pwe3 signal   PWE3 debugging signal is off（4）ZXROSNG#no debug pwe3 signal fec128 peer 100.100.1.2 vcid 100 pw-type ethernet raw    PWE3 debugging signal is off





相关命令 :

无 




## show debug pwe3 


show debug pwe3 




命令功能 :

显示PWE3已经开启的监视项。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show debug pwe3 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

查看PWE3模块开启的监视项。 






范例 :

（1）开启某个（某些）PW的PWE3信令交互过程，其show debug pwe3结果：ZXROSNG(config)#show debug pwe3PWE3:PWE3 event debugging is onPWE3 encode debugging is on PWE3 signal debugging peer:1.2.3.4 ,vcid:100 ,pw_type:Ethernet is onPWE3 signal debugging peer:1.2.3.4 ,vcid:200 ,pw_type:VLAN is on ZXROSNG# （2）开启所有PW的PWE3信令交互过程，其show debug pwe3结果：ZXROSNG(config)#show debug pwe3PWE3:PWE3 event debugging is onPWE3 encode debugging is on PWE3 signal debugging is onZXROSNG#





相关命令 :

无 




## show pwe3 signal fec128 detail 


show pwe3 signal fec128 detail 




命令功能 :

显示fec128型PW的详细信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal fec128 detail 
  [{[peer 
 ＜ip-address 
＞] [vcid 
 ＜vcid 
＞] [pw-type 
 {ethernet 
 {raw 
|tagged 
}|ip 
|ppp 
|hdlc 
|fr 
 {port 
|dlci 
|dlci-old 
}|tdm 
 {aal1 
|aal2 
|satop 
 {e1 
|t1 
|e3 
|t3 
}|cesopsn 
 {basic 
|cas 
}|sonet-sdh 
 {cesom 
|ceop 
}}|atm 
 {port 
|vpc 
|vcc 
|vcc-group 
|vpc-group 
|sdu 
|pdu 
}}]|used-only 
|unuse-only 
 [{no-remote 
|no-config 
}]|service-type 
 {vpls 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]|vpws-evpn 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]|bridge-domain 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]|vpws 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]|mspw 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]}|local-label 
 ＜local-label 
＞|remote-label 
 ＜remote-label 
＞|pw-name 
 ＜PW name 
＞}] 







命令参数解释 :



参数|描述
---|---
＜ip-address＞|PW对端的IP
＜vcid＞|PW标识ID
raw|PW类型：Ethernet
tagged|PW类型：Ethernet Tagged Mode
ip|PW类型：IP Layer2 Transport
ppp|PW类型：PPP
hdlc|PW类型：HDLC
port|PW类型： ATM transparent cell transport
dlci|PW类型：Frame Relay DLCI
dlci-old|PW类型：Frame Relay
aal1|PW类型：TDMoIP AAL1 Mode
aal2|PW类型：TDMoIP AAL2 Mode
e1|PW类型：SAToP E1
t1|PW类型：SAToP T1 (DS1)
e3|PW类型：SAToP E3
t3|PW类型：SAToP T3 (DS3)
basic|PW类型：CESoPSN basic mode
cas|PW类型：CESoPSN TDM with CAS
cesom|PW类型：SONET/SDH CESoM
ceop|PW类型：SONET/SDH CEoP
port|PW类型： ATM transparent cell transport
vpc|PW类型：  ATM one-to-one VPC cell mode
vcc|PW类型： ATM one-to-one VCC cell mode
vcc-group|PW类型： ATM n-to-one VCC cell transport
vpc-group|PW类型： ATM n-to-one VPC cell transport
sdu|PW类型： ATM transparent cell transport
pdu|PW类型： ATM AAL5 PDU VCC transport
used-only|显示转发层面已经使用的PW
unuse-only|显示转发层面未使用的PW
no-remote|显示没有远端信息的PW
no-config|显示没有本地配置信息的PW
vpls|业务类型为VPLS
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
vpws-evpn|业务类型为VPWS EVPN
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
bridge-domain|业务类型为bridge-domain
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
vpws|业务类型为VPWS
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
mspw|业务类型为MSPW
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
＜local-label＞|本地标签
＜remote-label＞|远端标签
＜PW name＞|PW名称








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show pwe3 signal fec128 detail The detailed signal information of dynamic fec128 PWs or PW-segments:Some signal information are referred to as follows :    NON  - the LDP session is absent,   UP   - the LDP session is OPERATIONAL,    GR1  - the LDP session is reconnecting,    GR2  - the LDP session's remote mappings are recovering,   DOWN - not UP(or NON,or GR1,or GR2).PW entity    : < 2.2.2.2 , 21 , Ethernet >LSPs formed  : NO ( LDP session absent )        C-bits       : local        : NO         , remote     : ??                        negotiated   : ??        MTU          : local        : 1500       , remote     : ??                       negotiated   : ??        labels       : local        : 205927     , remote     : ??        signal       : Configured   : YES        , Received   : NO                       Negotiated   : NO         , Sent       : NO                       AC ready     : YES       oam status   : local        : PSN rcv(0),snd(0); AC rcv(0),snd(0); Error(0)               remote       : PSN rcv(?),snd(?); AC rcv(?),snd(?); Error(?)redundancy   : local        : ??         , remote     : ??                       negotiated   : ??        application  : service-type : bridge-domain , instance-id: 1         MAC-withdraw : received     : 0          , sent       : 0         local-VCCV   : CC-type      : CW|AL|TTL  , CV-type    : LSP       remote-VCCV  : CC-type      : ??         , CV-type    : ??        actual-VCCV  : CC-type      : ??         , CV-type    : ??        LDP session  : NON, please check it.attachment-circuit : ??local-description  : 21remote-description : ??local-flow-label   : --remote-flow-label  : ??actual-flow-label  : ??remote-vlan-id     : ??received-SPE-TLV   : ??   





相关命令 :

无 




## show pwe3 signal fec128 


show pwe3 signal fec128 




命令功能 :

查看FEC128型PW的信令状态 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal fec128 
  [{[peer 
 ＜ip-address 
＞] [vcid 
 ＜vcid 
＞] [pw-type 
 {ethernet 
 {raw 
|tagged 
}|ip 
|ppp 
|hdlc 
|fr 
 {port 
|dlci 
|dlci-old 
}|tdm 
 {aal1 
|aal2 
|satop 
 {e1 
|t1 
|e3 
|t3 
}|cesopsn 
 {basic 
|cas 
}|sonet-sdh 
 {cesom 
|ceop 
}}|atm 
 {port 
|vpc 
|vcc 
|vcc-group 
|vpc-group 
|sdu 
|pdu 
}}]|used-only 
|unuse-only 
 [{no-remote 
|no-config 
}]|service-type 
 {vpls 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]|vpws-evpn 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]|bridge-domain 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]|vpws 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]|mspw 
 [{id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞}]}|local-label 
 ＜local-label 
＞|remote-label 
 ＜remote-label 
＞|pw-name 
 ＜PW name 
＞}] 







命令参数解释 :



参数|描述
---|---
＜ip-address＞|PW对端的IP
＜vcid＞|PW标识ID
raw|PW类型：Ethernet
tagged|PW类型：Ethernet Tagged Mode
ip|PW类型：IP Layer2 Transport
ppp|PW类型：PPP
hdlc|PW类型：HDLC
port|PW类型： ATM transparent cell transport
dlci|PW类型：Frame Relay DLCI
dlci-old|PW类型：Frame Relay DLCI(Martini Mode)
aal1|PW类型：TDMoIP AAL1 Mode
aal2|PW类型：TDMoIP AAL2 Mode
e1|PW类型：SAToP E1
t1|PW类型：SAToP T1 (DS1)
e3|PW类型：SAToP E3
t3|PW类型：SAToP T3 (DS3)
basic|PW类型：CESoPSN basic mode
cas|PW类型：CESoPSN TDM with CAS
cesom|PW类型：SONET/SDH CESoM
ceop|PW类型：SONET/SDH CEoP
port|PW类型： ATM transparent cell transport
vpc|PW类型：  ATM one-to-one VPC cell mode
vcc|PW类型： ATM one-to-one VCC cell mode
vcc-group|PW类型： ATM n-to-one VCC cell transport
vpc-group|PW类型： ATM n-to-one VPC cell transport
sdu|PW类型： ATM transparent cell transport
pdu|PW类型： ATM AAL5 PDU VCC transport
used-only|显示转发层面已经使用的PW
unuse-only|显示转发层面未使用的PW
no-remote|显示没有远端信息的PW
no-config|显示没有本地配置信息的PW
vpls|业务类型为VPLS
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
vpws-evpn|业务类型为VPWS EVPN
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
bridge-domain|业务类型为bridge-domain
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
vpws|业务类型为VPWS
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
mspw|业务类型为MSPW
＜instance-id＞|MSPW实例ID，范围：1-$#67239950#$
＜instance-name＞|MSPW实例名称
＜local-label＞|本地标签
＜remote-label＞|远端标签
＜PW name＞|PW名称








缺省 :

无 






使用说明 :

1.    该命令在所有参数都缺省时表示显示fec128型PW的信令状态，主要显示PW的基本信息状态。2.    指定某一参数时，显示出符合此参数的fec128型PW的信令简要信息






范例 :

1. 显示所有fec128型PW信令状态的显示效果如下：ZXROSNG(config)#show pwe3 signal fec128The signal information of FEC 128 PWs in brief:Headers: Neighbourhood - neighbour's IP address, LDP state and related PW name;Service - PW encapsulation mode and service instance's type and index;Descriptions - remote description and local description;Labels - local label (in label) and remote label (out label)Codes  : L - Local configured; M - Mapping received; N - Negotiated;         S - mapping Sent; A - AC ready (VPWS) or service Attached (VPLS/MSPW);          C - Control word used;          Up    - PW signal procedures succeeded and both VC-LSPs formed;          Down  - PW not UP;         No    - session state is not UP;         Rd    - session state is UP;         G1    - session state is not UP and PW's remote label is staling;         G2    - session state is UP but PW's remote label is staling as beforeMarks  : ?unknown;.placeholder;^decimal vcid;$auto_;*ellipsis;NULL-empty string         BD bridge-domain-------------------------------------------------------------------------------Neighbourhood   VC-ID      Service    Descriptions               Labels  Status--------------- ---------- ---------- -------------------------- ------- ------2.2.2.2         21         Ethernet   ??                         205927    DOWNNo pw21         ^^^^^^^^^^ BD:1       21                         ??????? L...A.2.2.2.2         12         Ethernet   ??                         205926    DOWNNo pw12         ^^^^^^^^^^ MSPW:2     ??                         ??????? L...A.ZXROSNG(config)#2.显示pw-type为ethernet类型的PWZXROSNG#show pwe3 signal fec128 pw-type ethernet  raw The signal information of FEC 128 PWs in brief:Headers: Neighbourhood - neighbour's IP address, LDP state and related PW name;         Service - PW encapsulation mode and service instance's type and index;         Descriptions - remote description and local description;         Labels - local label (in label) and remote label (out label)Codes  : L - Local configured; M - Mapping received; N - Negotiated;         S - mapping Sent; A - AC ready (VPWS) or service Attached (VPLS/MSPW/ bridge-domain);          C - Control word used;          Up    - PW signal procedures succeeded and both VC-LSPs formed;          Down  - PW not UP;         No    - session state is not UP;         Rd    - session state is UP;         G1    - session state is not UP and PW's remote label is staling;         G2    - session state is UP but PW's remote label is staling as beforeMarks  : ?unknown;.placeholder;^decimal vcid;$auto_;*ellipsis;NULL-empty string         BD bridge-domain-------------------------------------------------------------------------------Neighbourhood   VC-ID      Service    Descriptions               Labels  Status--------------- ---------- ---------- -------------------------- ------- ------2.2.2.2         21         Ethernet   ??                         205927    DOWNNo pw21         ^^^^^^^^^^ BD:1       21                         ??????? L...A.2.2.2.2         12         Ethernet   ??                         205926    DOWNNo pw12         ^^^^^^^^^^ MSPW:2     ??                         ??????? L...A.





相关命令 :

show pwe3 signal fec128 detail等 




## show pwe3 signal fec129 detail 


show pwe3 signal fec129 detail 




命令功能 :

显示fec129型PW的详细信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal fec129 detail 
  [{used-only 
|unuse-only 
 [{no-remote 
|no-config 
}]|local-label 
 ＜local-label 
＞|remote-label 
 ＜remote-label 
＞|id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞|pw-name 
 ＜PW name 
＞}] 







命令参数解释 :



参数|描述
---|---
used-only|显示转发层面已经使用的PW
unuse-only|显示转发层面未使用的PW
no-remote|显示没有远端信息的PW
no-config|显示没有本地配置信息的PW
＜local-label＞|本地标签
＜remote-label＞|远端标签
＜instance-id＞|VPLS实例ID，范围：1-$#67239948#$
＜instance-name＞|VPLS实例名称
＜PW name＞|PW名称








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#show pwe3 signal fec129 detail The detailed signal information of dynamic fec129 PWs or PW-segments:Some signal information are referred to as follows :    NON  - the LDP session is absent,   UP   - the LDP session is OPERATIONAL,    GR1  - the LDP session is reconnecting,    GR2  - the LDP session's remote mappings are recovering,   DOWN - not UP(or NON,or GR1,or GR2).   PW entity    : < 100.100.1.2 , 0000006400000064 , Ethernet >LSPs formed  : YEStaii(1)      : local        : 64640102   , remote     : 64640102  saii(1)      : local        : 64640101   , remote     : 64640101  C-bits       : local        : NO         , remote     : NO                        negotiated   : NO        MTU          : local        : 1500       , remote     : 1500                     negotiated   : 1500      labels       : local        : 81922      , remote     : 81923     signal       : Configured   : YES        , Received   : YES                      Negotiated   : YES        , Sent       : YES                      AC ready     : YES       oam status   : local        : PSN rcv(?),snd(?); AC rcv(?),snd(?); Error(?)               remote       : PSN rcv(?),snd(?); AC rcv(?),snd(?); Error(?)redundancy   : local        : ??         , remote     : ??                       negotiated   : ??        application  : service-type : VPLS       , instance-id: 1         MAC-withdraw : received     : 0          , sent       : 0         local-VCCV   : CC-type      : NO         , CV-type    : NO        remote-VCCV  : CC-type      : NO         , CV-type    : NO        actual-VCCV  : CC-type      : NO         , CV-type    : NO        LDP session  : The LDP session's state is UP.attachment-circuit : ??local-description  : zteremote-description : ??ZXROSNG(config)#






相关命令 :

无 




## show pwe3 signal fec129 


show pwe3 signal fec129 




命令功能 :

查看FEC129型PW的信令状态。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal fec129 
  [{used-only 
|unuse-only 
 [{no-remote 
|no-config 
}]|local-label 
 ＜local-label 
＞|remote-label 
 ＜remote-label 
＞|id 
 ＜instance-id 
＞|name 
 ＜instance-name 
＞|pw-name 
 ＜PW name 
＞}] 







命令参数解释 :



参数|描述
---|---
used-only|显示转发层面已经使用的PW
unuse-only|显示转发层面未使用的PW
no-remote|显示没有远端信息的PW
no-config|显示没有本地配置信息的PW
＜local-label＞|本地标签
＜remote-label＞|远端标签
＜instance-id＞|VPLS实例ID，范围：1-$#67239948#$
＜instance-name＞|VPLS实例名称
＜PW name＞|PW名称








缺省 :

无 






使用说明 :

1.    该命令在所有参数都缺省时表示显示fec129型PW的信令状态，主要显示PW的基本信息状态。2.    指定某个参数时，显示符合此参数的所有fec129型PW的信令简要信息。






范例 :

1.显示所有fec129型PW的简要信令信息ZXROSNG(config)#show pwe3 signal fec129The signal information of FEC 129 PWs in brief:Headers: Neighbourhood - neighbour's IP address, LDP state and related PW name;Service - PW encapsulation mode and service instance's type and index;Labels - local label (in label) and remote label (out label)Codes  : L - Local configured; M - Mapping received; N - Negotiated;S - mapping Sent; A - AC ready (VPWS) or service Attached (VPLS/MSPW);C - Control word used;Up    - PW signal procedures succeeded and both VC-LSPs formed;Down  - PW not UP;No - session state is not UP;Rd - session state is UP;G1   - session state is not UP and PW's remote label is staling;G2   - session state is UP but PW's remote label is staling as beforeMarks  : ?unknown;.placeholder;^decimal vcid;$auto_;*ellipsis;NULL-empty string         BD bridge-domain-------------------------------------------------------------------------------Neighbourhood   AGI        Service    AIIs                       Labels  Status--------------- ---------- ---------- -------------------------- ------- ------100.100.1.2     00000064   ethernet   100.100.1.2     1684275458 81922       UPRd  $pw1      00000064   BD:1     100.100.1.1     1684275457 81923   LMNSA.ZXROSNG(config)#2.显示本地标签为81922的PW。ZXROSNG(config)#show pwe3 signal fec129 local-label 81922The signal information of FEC 129 PWs in brief:Headers: Neighbourhood - neighbour's IP address, LDP state and related PW name;Service - PW encapsulation mode and service instance's type and index;Labels - local label (in label) and remote label (out label)Codes  : L - Local configured; M - Mapping received; N - Negotiated;S - mapping Sent; A - AC ready (VPWS) or service Attached (VPLS/MSPW/bridge-domain);C - Control word used;Up    - PW signal procedures succeeded and both VC-LSPs formed;Down  - PW not UP;No - session state is not UP;Rd - session state is UP;G1   - session state is not UP and PW's remote label is staling;G2   - session state is UP but PW's remote label is staling as beforeMarks  : ?unknown;.placeholder;^decimal vcid;$auto_;*ellipsis;NULL-empty string         BD bridge-domain    -------------------------------------------------------------------------------Neighbourhood   AGI        Service    AIIs                       Labels  Status--------------- ---------- ---------- -------------------------- ------- ------100.100.1.2     00000064   ethernet   100.100.1.2     1684275458 81922       UPRd $pw1      00000064   BD:1     100.100.1.1     1684275457 81923   LMNSA.ZXROSNG(config)#





相关命令 :

show pwe3 signal fec129 detail 




## show pwe3 signal mspw 


show pwe3 signal mspw 




命令功能 :

查看各条MSPW的信令摘要信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal mspw 
  [{mspw-name 
 ＜mspw-name 
＞|used-only 
|unused-only 
 [{config-waiting 
|mapping-waiting 
}]|local-label 
 ＜local-label 
＞|remote-label 
 ＜remote-label 
＞|pw-type 
 {ethernet 
 {raw 
|tagged 
}|ip 
|ppp 
|hdlc 
|fr 
 {port 
|dlci 
|dlci-old 
}|tdm 
 {aal1 
|aal2 
|satop 
 {e1 
|t1 
|e3 
|t3 
}|cesopsn 
 {basic 
|cas 
}|sonet-sdh 
 {cesom 
|ceop 
}}|atm 
 {port 
|vpc 
|vcc 
|vcc-group 
|vpc-group 
|sdu 
|pdu 
}}}] [{more 
|detail 
}] 







命令参数解释 :



参数|描述
---|---
＜mspw-name＞|MSPW实例名称
used-only|显示转发层面已经使用的MSPW
unused-only|显示转发层面未使用的MSPW
config-waiting|显示配置不完整的MSPW
mapping-waiting|显示信令不完整的MSPW
＜local-label＞|显示某个本地标签对应的MSPW
＜remote-label＞|显示某个远端标签对应的MSPW
raw|PW类型：Ethernet
tagged|PW类型：Ethernet Tagged Mode
ip|PW类型：IP Layer2 Transport
ppp|PW类型：PPP
hdlc|PW类型：HDLC
port|PW类型：ATM transparent cell transport
dlci|PW类型：Frame Relay DLCI
dlci-old|PW类型：Frame Relay DLCI(Martini Mode)
aal1|PW类型：TDMoIP AAL1 Mode
aal2|PW类型：TDMoIP AAL2 Mode
e1|PW类型：SAToP E1
t1|PW类型：SAToP T1 (DS1)
e3|PW类型：SAToP E3
t3|PW类型：SAToP T3 (DS3)
basic|PW类型：CESoPSN basic mode
cas|PW类型：CESoPSN TDM with CAS
cesom|PW类型：SONET/SDH CESoM
ceop|PW类型：SONET/SDH CEoP
port|PW类型：ATM transparent cell transport
vpc|PW类型：ATM one-to-one VPC cell mode
vcc|PW类型：ATM one-to-one VCC cell mode
vcc-group|PW类型：ATM n-to-one VCC cell transport
vpc-group|PW类型：ATM n-to-one VPC cell transport
sdu|PW类型：ATM AAL5 SDU VCC transport
pdu|PW类型：ATM AAL5 PDU VCC transport
more|显示所有MSPW的一般信息
detail|显示所有MSPW的详细信息








缺省 :

无 






使用说明 :

1.    该命令在所有参数都缺省时表示显示所有MSPW的信令摘要信息。2.    该命令中除了detail、more参数显示格式不同外，其余的参数显示格式都相同。show pwe signal mspw detail命令显示所有MSPW信令状态的详细信息。3.   对于回显中的segment字段，如果没有本地配置这个参数或是目前获取不到，会呈现为“??”。





范例 :

1.显示所有MSPW信息ZXROSNG(config)#show pwe3 signal mspwThe brief signal information of PW switching point instances:Headers : id - PW switching point instance id, R - Received(for seg1 or seg2),PW-seg1-id - the VCID of the first PW segment,PW-seg2-id - the VCID of the second PW segment,used - signal procedures succeeded and transit-LSPs formedCodes   : ?unknown, *yes, .no-------------------------------------------------------------------------------PW-seg1-id R PW-seg2-id R pw-type   PW switching point instance name id    used---------- - ---------- - --------- -------------------------------- ----- ----40         * 100        * Ethernet  mspw_zte                         1     YESZXROSNG(config)#2. 显示所有MSPW信令更多的信息显示效果如下ZXROSNG(config)#show pwe3 signal mspw  detailThe detailed signal information of PW switching point instances:Some signal information are referred to as follows :NON  - the LDP session is absent,UP   - the LDP session is OPERATIONAL,GR1  - the LDP session is reconnecting,GR2  - the LDP session's remote mappings are recovering,DOWN - not UP(or NON,or GR1,or GR2).MSPW-ID     : 1MSPW-name   : mspw_ztePW-type     : EthernetLSPs formed : <100.100.1.1, 40>: YES  <100.100.1.1, 44>: YES  <100.100.1.3, 100>: YES  <100.100.1.3, 66>: YESPW segment1 : <100.100.1.1, 40> finish  : YES labels  : local     : 81920   , remote     : 81920 signal  : received  : YES     , negotiated : YES     , sent      : YES session : The LDP session's state is UP. local  status  : PSN : UP    ,AC : UP    , redundancy : ACTIVE    remote  status  : PSN : UP    , AC : UP  , redundancy : ACTIVE  PW backup-segment1 : <100.100.1.1, 44> finish  : YES labels  : local     : 81920   , remote     : 81920 signal  : received  : YES     , negotiated : YES     , sent      : YES session : The LDP session's state is UP. local  status  : PSN : UP    ,AC : UP    , redundancy : ACTIVE  remote  status  : PSN : UP    , AC : UP  , redundancy : ACTIVEPW segment2 : <100.100.1.3, 100> finish  : YES labels  : local     : 81921   , remote     : 81920 signal  : received  : YES     , negotiated : YES     , sent      : YES session : The LDP session's state is UP. local  status  : PSN : UP    ,AC : UP    , redundancy : ACTIVE  remote  status  : PSN : UP    , AC : UP  , redundancy : ACTIVEPW backup-segment2 : <100.100.1.3, 66> finish  : YES labels  : local     : 81921   , remote     : 81920 signal  : received  : YES     , negotiated : YES     , sent      : YES session : The LDP session's state is UP. local  status  : PSN : UP    ,AC : UP    , redundancy : ACTIVE     remote  status  : PSN : UP    , AC : UP  , redundancy : ACTIVERecieved interface parameters MTUs       :   segment1  : 1500      segment2  : 1500      backup-segment1  : 1500      backup-segment2  : 1500   C-bits     :  segment1  : 1         segment2  : 1         backup-segment1  : 1         backup-segment2  : 1   Remote-description  segment1  : gei-0/1/0/3  segment2  : gei-0/1/0/4  backup-segment1  : gei-0/1/0/4  backup-segment2  : gei-0/1/0/3 VCCV  CC-type   segment1 : ??   segment2 : ??   backup-segment1 : CW|AL|TTL    backup-segment2 : CW|AL|TTL  CV-type   segment1 : ??   segment2 : ??   backup-segment1 : LSP|BFD(0X4)   backup-segment2 : LSP|BFD(0X4)ZXROSNG(config)#域信息描述表：域               描述MSPW-ID               本地MSPW配置实例IDMSPW-name       本地MSPW配置实例名称PW-type               PW封装类型LSPs formed        PW是否形成LSPPW segment1       第一段PW的基本信息：PW唯一标识，PW本地配置                   基本信息，PW从远端接收的基本信息。                   <100.100.1.1, 40>                   PW唯一标识                   finish  : YES                   本地配置完成标识                   labels  : local     : 81920   ,                    remote     : 81920                   本地标签值和远端标签值                   signal  : received  : YES     ,                    negotiated : YES     , sent      :                    YES                   信令上是否接收到远端标签映射消息，是否协商成                   功，是否给对端发送过标签映射消息                   session : The LDP session's state is                   UP.                   该段PW对应的LDP会话所处的状态                   local  status  : PSN : UP    ,AC :                    UP    , redundancy : ACTIVE                      remote  status  : PSN : UP    , AC :                    UP  , redundancy : ACTIVE                     本地及远端PSN状态、AC状态以及冗余状态PW backup-         第一段PW的备份PW基本信息，细化字段同上segment1       PW segment2       第二段PW的基本信息，细化字段同上PW backup-         第二段PW的备份PW基本信息，细化字段同上segment2      Received           第一段PW、第二段PW、第一段备份PW、第二段备份interface          PW的远端接口参数信息，主要包括远端接口最大传输paramerters       单元，远端控制字，远端接口描述符，VCCV参数，                   具体显示条目见下：MTUs                MTUs : 显示各段PW的远端接口最大传输单元 C-bits             C-bits : 显示各段PW的远端控制字使能 Remote-des         Remote-description :显示各段PW的远端接口cription       描述符 VCCV               显示各段PW的远端CC和CV能力参数                    CC-type : 显示各段PW的远端CC能力参数                    CV-type : 显示各段PW的远端CV能力参数





相关命令 :

无 




## show pwe3 signal service-aware atm 


show pwe3 signal service-aware atm 




命令功能 :

显示PWE3信令的atm业务相关接口参数。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal service-aware atm 
  [{[peer 
 ＜ip-address 
＞],[vcid 
 ＜vcid 
＞],[pw-type 
 {port 
|vpc 
|vcc 
|vcc-group 
|vpc-group 
|sdu 
|pdu 
}]}] 







命令参数解释 :



参数|描述
---|---
＜ip-address＞|Peer IP地址
＜vcid＞|虚拟链路ID
port|ATM信元传输模式
vpc|ATM 1:1 VPC信元模式
vcc|ATM 1:1 VCC信元模式
vcc-group|ATM n:1 VCC信元模式
vpc-group|ATM n:1 VPC信元模式
sdu|ATM AAL5 SDU VCC传输模式
pdu|ATM AAL5 PDU VCC传输模式








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#ZXROSNG(config)# show pwe3 signal service-aware  frThe special information of dynamic PWs or PW-segments for ATM services:PW entity    : < 2.2.2.2 , 2446 , ATM_VCC1 >application  : service-type : MSPW       , instance-id: 301          local max ATM cells : 42remote max ATM cells: 42  local-description   : 1446remote-description  : 1446





相关命令 :

无 




## show pwe3 signal service-aware fr 


show pwe3 signal service-aware fr 




命令功能 :

显示PWE3信令的fr业务相关接口参数。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal service-aware fr 
  [{[peer 
 ＜ip-address 
＞],[vcid 
 ＜vcid 
＞],[pw-type 
 {port 
|dlci 
|dlci-old 
}]}] 







命令参数解释 :



参数|描述
---|---
＜ip-address＞|Peer IP地址
＜vcid＞|虚拟链路ID
port|帧中继端口模式
dlci|帧中继DLCI模式
dlci-old|帧中继DLCI martini模式








缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG(config)#ZXROSNG(config)# show pwe3 signal service-aware  frThe special information of dynamic PWs or PW-segments for FR services:PW entity    : < 2.2.2.2 , 2096 , DLCI(new) >application  : service-type : MSPW       , instance-id: 199          local DLCI length   : 4remote DLCI length  : 4local-description   : 1096remote-description  : 1096





相关命令 :

无 




## show pwe3 signal service-aware tdm 


show pwe3 signal service-aware tdm 




命令功能 :

显示PW上TDM业务的信令信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal service-aware tdm 
  [{[peer 
 ＜ip-address 
＞],[vcid 
 ＜vcid 
＞],[pw-type 
 {satop 
 {e1 
|t1 
|e3 
|t3 
}|cesopsn 
 {basic 
|cas 
}}]}] 







命令参数解释 :



参数|描述
---|---
＜ip-address＞|PW对端的IP
＜vcid＞|PW标识ID
e1|PW类型：SAToP E1
t1|PW类型：SAToP T1 (DS1)
e3|PW类型：SAToP E3
t3|PW类型：SAToP T3 (DS3)
basic|PW类型：CESoPSN basic mode
cas|PW类型：CESoPSN TDM with CAS








缺省 :

无 






使用说明 :

本命令是显示TDM业务的信令信息 






范例 :

ZXROSNG#show pwe3 signal service-aware tdm The special information of dynamic PWs or PW-segments for TDM services:PW entity    : < 1.1.1.1 , 100 , SAToP_E1 >application  : service-type : VPWS       , instance-id: 1              bits-rate    : local        : 32         , remote     : 32                        negotiated   : 32        payload bytes: local        : 256        , remote     : 256                      negotiated   : 256       local-description  : cip1remote-description : cip1local TDM Options  : R(1), D(1)remote TDM Options : R(1), D(1)






相关命令 :

show pwe3 signal fec128 




## show pwe3 signal statistics 


show pwe3 signal statistics 




命令功能 :

查看各种类型的PW的信令状态的统计信息。 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal statistics 
 







命令参数解释 :


					无
				 






缺省 :

所有参数都缺省时表示显示所有PW的信令状态 






使用说明 :

无 






范例 :

ZXROSNG#show pwe3 signal statistics The statistics of dynamic PWs or PW-segments:Headers : APP - application instance of PW, C-bit - the PWs using control word,          ether - the ethernet raw PWs, vlan - the ethernet tagged PWs,          others - the non-ethernet PWs,           used - signal procedures succeeded and VC-LSPs or transit-LSPs formedCodes   : ?application instance not configured; BD bridge-domain----+-----+------------------+------------------------+------------------------type|count| all dynamic PWs  |  the used dynamic PWs  | the unused dynamic PWs  of | of  +------------------+------------------------+------------------------APPs|APPs |total  used unused|C-bit ether  vlan others|C-bit ether  vlan others----+-----+-----+-----+------+-----+-----+-----+------+-----+-----+-----+------VPWS     0     0     0      0     0     0     0      0     0     0     0     0BD       1     1     0      1     0     0     0      0     0     1     0     0MSPW     2     3     0      3     0     0     0      0     0     3     0     0????     0     0     0      0     0     0     0      0     0     0     0     0SUM      3     4     0      4     0     0     0      0     0     4     0     0





相关命令 :

无 




## show pwe3 signal 


show pwe3 signal 




命令功能 :

显示所有PW的简要信息 






命令模式 :

 除用户模式外的其他所有模式  






命令默认权限级别 :

15 






命令格式 :



show pwe3 signal 
 







命令参数解释 :


					无
				 






缺省 :

无 






使用说明 :

无 






范例 :

ZXROSNG#show pwe3 signal The signal information of FEC 128/129 PWs in brief:Headers: Neighbourhood - neighbour's IP address, LDP state and related PW name;         AGI - attachment group identifier (FEC129 only);         Service - PW encapsulation mode and service instance's type and index;         AIIs - target AII and source AII (FEC129 only);         Descriptions - remote description and local description (FEC128 only);         Labels - local label (in label) and remote label (out label)Codes  : L - Local configured; M - Mapping received; N - Negotiated;         S - mapping Sent; A - AC ready (VPWS) or service Attached (VPLS/MSPW/ bridge-domain);          C - Control word used;         Up    - PW signal procedures succeeded and both VC-LSPs formed;          Down  - PW not UP;         No    - session state is not UP;         Rd    - session state is UP;         G1    - session state is not UP and PW's remote label is staling;         G2    - session state is UP but PW's remote label is staling as beforeMarks  : ?unknown;.placeholder;^decimal vcid;$auto_;*ellipsis;NULL-empty string         BD bridge-domain                -------------------------------------------------------------------------------Neighbourhood   AGI/VC-ID  Service    AIIs/Descriptions          Labels  Status--------------- ---------- ---------- -------------------------- ------- ------2.2.2.2         21         Ethernet   ??                         205927    DOWNNo pw21         ^^^^^^^^^^ BD:1       21                         ??????? L...A.





相关命令 :

无 




