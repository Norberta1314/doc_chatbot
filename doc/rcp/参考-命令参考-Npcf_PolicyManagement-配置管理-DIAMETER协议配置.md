 DIAMETER协议配置 
背景知识 : 
 
Diameter体系架构
Diameter协议采用了一种新的协议定义模式：首先推出一个轻量的、易于实施的基础协议，旨在提供一个AAA框架，其中包括实现AAA功能最基本的要求。然后针对不同的网络情况和业务需求，分别制定相应的应用扩展。
Diameter协议族包括基础协议（Diameter Base Protocol）和各种应用协议。基础协议由IETF制订，提供了作为一个AAA协议的最低需求，是Diameter网络节点都必须实现的功能，包括节点间能力的协商、Diameter消息的接收及转发、计费信息的实时传输等。应用协议则充分利用基础协议提供的消息传送机制，规范相关节点的功能以及其特有的消息内容，来实现应用业务的AAA。基础协议可以作为一个计费协议单独使用，但一般情况下需与某个应用一起使用。3GPP在Diameter基础协议上制订Cx、Dx、Sh接口应用扩展协议来完成用户数据管理、路由、移动性管理以及鉴权等功能。
 
 
Diameter传输协议
Diameter 基本协议运行在TCP 或SCTP传输协议上。SCTP与TCP相同点是：
提供面向连接的传输服务。
提供可靠的传输，保证数据按顺序到达，并且没有丢失或重复。
是全双工的。
应用窗口机制以提供流控。
SCTP还提供一些TCP不具备的能力：
SCTP 提供两端点之间的多数据流传送。每个数据流内，消息都会按序到达，并且没有丢失和重复。
SCTP是面向消息的；即SCTP 负责维护消息分界并分发完整消息（PDU）,而TCP 则是面向比特的。
SCTP使用多宿主主机的概念。一个多宿主主机是拥有多个IP接口的主机。在初始化时，SCTP两端交换它们的IP接口地址列表。一个要求重传的SCTP消息可以被发送到备选的IP地址，这样可以在发生网络失败时，提高SCTP会话复原的能力。而TCP会话在每个端点只能处理单个IP地址。
Diameter 协议必须能够在可以提供重传策略的传输层上运行，以使其能够在对等端不可达时，有效地转换另一个主机。与RADIUS相反，Diameter
协议要求代理链上的每一个节点都应在“ 传输层”对请求或响应进行确认。由于Diameter 运行在提供可靠传输的SCTP上，代理链上的每个节点都有责任对没有确认的消息进行重传。
Diameter节点可以从一个源端口上初始化连接，该端口可以不是其声明接受连接请求的端口，同时Diameter节点必须时刻准备在端口3868上接收连接。一个特定的Diameter对等端状态机的实例不允许使用多个传输连接与一个已知的对等端通信，除非该对等端出现多个实例，这种情况下，允许每个进程一个连接。
当一个对等端不存在与之相关的传输连接时，应当定期进行连接尝试。该行为通过Tc定时器控制，建议该值为30秒。该规则还有特定的例外，比如一个对等端已经结束了传输连接，表明其不希望通信等等。
当连接一个对等端，且定义了零个或多个传输时，应首先尝试使用SCTP，然后是TCP。
 
 
功能描述 : 
该功能模块用于配置Diameter协议栈相关数据，包含以下内容： 
Diameter协议提供可靠的传输，当一个对等端不存在与之相关的传输连接时，应当定期进行连接尝试。该行为通过Tc定时器控制，建议该值为30秒，对该Tc定时器提供了配置命令，即在“DIAMETER协议基本配置”中配置Tc定时器值，该置系统默认为30秒。 
Diameter本协议运行在TCP或SCTP传输协议上。 
 
如果选择TCP，则需要在“TCP/UDP连接配置”中配置TCP协议相关数据。 
 
如果选择SCTP，则需要在“DIAMETER偶联配置”中配置SCTP协议相关数据。 
 
主要是配置IP地址，端口号，以及链路规划所在的CMP模块号。 
根据Diameter链路规划，配置diameter链路，即在“DIAMETER信令链路配置”中配置diameter链路相关数据，主要是本端和对端的主机名和域名，以及该条链路上承载的各种应用，如Cx\Dx\Sh\Dh等,其中一条diameter链路对应一条TCP或者SCTP链路。 
如果需要路由转发，则需要在“DIAMETER信令路由配置”中配置diameter路由相关数据。 
# DIAMETER协议基本配置 
# DIAMETER协议基本配置 
背景知识 : 
Diameter协议是用于认证、授权、计费的协议，主要应用于IP多媒体子系统、演进的分组核心网等系统。 
Diameter对等端是指一个Diameter节点，该节点和另一个特定的Diameter节点有一个直接的传输连接。 
功能描述 : 
该配置提供了本网元的Diameter协议正常建链需要的产品名称、厂商、心跳检测时长，Diameter的最大连接数和最大路由数，消息重发间隔。 
本配置为Diameter协议全局性配置。该配置不可删除。 
## SET DIM GLOBAL 
## SET DIM GLOBAL 
命令功能 : 
该命令用于修改Diameter协议基本配置。 
当需要重新配置产品名称、厂商、心跳检测时长、支持的最大连接数、支持的最大路由数、消息重发间隔参数时，使用该命令。 
注意事项 : 
 
Diameter协议基本配置全局唯一。 
 
若修改Diameter协议基本配置中支持的最大连接数、支持的最大路由数，需要执行命令RESET SYSTEM重启整个网元才能生效。
修改时，某些参数不输入，该参数将保持最近一次的配置内容。
 
 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
PRODUCTNAME|产品名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：该参数用于指定产品名称。建议使用能够表明本产品网元的名称，例如RCP。本网元发送CER（能力交换请求，Capabilities-Exchange-Req）消息到对等端时，在Product-Name AVP中填写该值。本网元发送CEA（能力交换应答，Capabilities-Exchange-Answer）消息到对等端时，在Product-Name AVP中填写该值。数据来源：本端规划。配置原则：由本端规划的1~127长度的FQDN字符串。
VENDORID|运营商标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|参数作用：该参数用于指定本网元的厂商ID。本网元发送CER（Capabilities-Exchange-Req，能力交换请求）消息到对等端时，在Vendor-Id AVP中填写该值。本网元发送CEA（Capabilities-Exchange-Answer，能力交换应答）消息到对等端时，在Vendor-Id AVP中填写该值。数据来源：本端规划。配置原则：配置为协议规定的厂商ID号，常用的有：10415：3GPP3902：ZTE推荐填写10415。
MAXCONN|支持的最大连接数|参数可选性:任选参数；参数类型:整数；参数范围为:32~2048。|参数作用：本参数用于指定Diameter连接数据的全局容量上限。当本网元和对端网元需要建立Diameter链路（ADD DIM RCPLINK）时，配置本参数。数据来源：本端规划。配置原则：根据网元所需要建立的最大Diameter链路数进行设置。修改本参数需要通过RESET SYSTEM命令重启本网元才能生效。
MAXROUTE|支持的最大路由数|参数可选性:任选参数；参数类型:整数；参数范围为:64~8192。|参数作用：用于指定Diameter路由数的全局容量上限。当本网元需要向对端网元发送Diameter消息时，配置本参数。具体的路由数包括ADD DIM ROUTE命令所配置的路由条数和根据Diameter链路自动生成的路由条数。数据来源：：本端规划。配置原则：根据网元规划需要建立的最大Diameter路由条数进行设置。修改本参数需要通过RESET SYSTEM命令重启本网元才能生效。
ACTIVETIME|消息重发间隔（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|参数作用：用于指定本网元未收到Diameter响应消息时，重发Diameter请求消息的时间间隔。不包括Diameter基本消息CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）、DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）、DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）。数据来源：本端规划。配置原则：建议使用默认值7秒。
RESENDTIMES|消息重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:0~5。|参数作用：用于指定消息重发的次数。消息重发次数是同一个消息重发的最大次数。当本节点发送请求消息时设置消息重发定时器，定时器到时如果没有接收到响应，则本节点重新选择一条链路发送该消息。数据来源：本端规划。配置原则：建议使用默认值0次，也就是不进行重发。
BUSYCYCLE|忙检测周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~60。|参数作用：用于指定对等端忙的检测周期。本端收到某条链路上回复的原因为DIAMETER_TOO_BUSY的应答消息后，在一段时间内本端不使用此链路发送消息。其中“在一段时间内”的时间长度可配置。数据来源：运营商规划。配置原则：根据网元所在当地的网络情况配置。推荐使用默认值10秒。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
PRODUCTNAME|产品名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：该参数用于指定产品名称。建议使用能够表明本产品网元的名称，例如RCP。本网元发送CER（能力交换请求，Capabilities-Exchange-Req）消息到对等端时，在Product-Name AVP中填写该值。本网元发送CEA（能力交换应答，Capabilities-Exchange-Answer）消息到对等端时，在Product-Name AVP中填写该值。数据来源：本端规划。配置原则：由本端规划的1~127长度的FQDN字符串。
VENDORID|运营商标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|参数作用：该参数用于指定本网元的厂商ID。本网元发送CER（Capabilities-Exchange-Req，能力交换请求）消息到对等端时，在Vendor-Id AVP中填写该值。本网元发送CEA（Capabilities-Exchange-Answer，能力交换应答）消息到对等端时，在Vendor-Id AVP中填写该值。数据来源：本端规划。配置原则：配置为协议规定的厂商ID号，常用的有：10415：3GPP3902：ZTE推荐填写10415。
MAXCONN|支持的最大连接数|参数可选性:任选参数；参数类型:整数；参数范围为:32~2048。|参数作用：本参数用于指定Diameter连接数据的全局容量上限。当本网元和对端网元需要建立Diameter链路（ADD DIM RCPLINK）时，配置本参数。数据来源：本端规划。配置原则：根据网元所需要建立的最大Diameter链路数进行设置。修改本参数需要通过RESET SYSTEM命令重启本网元才能生效。
MAXROUTE|支持的最大路由数|参数可选性:任选参数；参数类型:整数；参数范围为:64~8192。|参数作用：用于指定Diameter路由数的全局容量上限。当本网元需要向对端网元发送Diameter消息时，配置本参数。具体的路由数包括ADD DIM ROUTE命令所配置的路由条数和根据Diameter链路自动生成的路由条数。数据来源：：本端规划。配置原则：根据网元规划需要建立的最大Diameter路由条数进行设置。修改本参数需要通过RESET SYSTEM命令重启本网元才能生效。
ACTIVETIME|消息重发间隔（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|参数作用：用于指定本网元未收到Diameter响应消息时，重发Diameter请求消息的时间间隔。不包括Diameter基本消息CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）、DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）、DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）。数据来源：本端规划。配置原则：建议使用默认值7秒。
RESENDTIMES|消息重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:0~5。|参数作用：用于指定消息重发的次数。消息重发次数是同一个消息重发的最大次数。当本节点发送请求消息时设置消息重发定时器，定时器到时如果没有接收到响应，则本节点重新选择一条链路发送该消息。数据来源：本端规划。配置原则：建议使用默认值0次，也就是不进行重发。
BUSYCYCLE|忙检测周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~60。|参数作用：用于指定对等端忙的检测周期。本端收到某条链路上回复的原因为DIAMETER_TOO_BUSY的应答消息后，在一段时间内本端不使用此链路发送消息。其中“在一段时间内”的时间长度可配置。数据来源：运营商规划。配置原则：根据网元所在当地的网络情况配置。推荐使用默认值10秒。
HINT|命令提示信息|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于表示该命令执行时的提示信息。数据来源：本端规划。配置原则：固定设置为“修改支持的最大连接数或路由数，需要重启整个系统才能生效。”。
命令举例 : 
修改Diameter协议基本配置：产品名称为A，运营商标识为1，心跳检测时长（秒）5；支持的最大连接数为64，支持的最大路由数为256。 
SET DIM GLOBAL:PRODUCTNAME="A",VENDORID=1,TC=5,MAXCONN=64,MAXROUTE=256; 
相关命令 : 
[查询DIAMETER协议基本配置]
## SHOW DIM GLOBAL 
## SHOW DIM GLOBAL 
命令功能 : 
该命令用于查询Diameter协议基本配置。 
当需要查看Diameter协议栈的基本参数时，使用该命令进行查询。查询成功后，可显示产品名称、厂商、心跳检测时长、支持的最大连接数、支持的最大路由数、消息重发间隔。 
注意事项 : 
不需要输入参数，默认查询所有配置。 
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
PRODUCTNAME|产品名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~128个字符。|参数作用：该参数用于指定产品名称。建议使用能够表明本产品网元的名称，例如RCP。本网元发送CER（能力交换请求，Capabilities-Exchange-Req）消息到对等端时，在Product-Name AVP中填写该值。本网元发送CEA（能力交换应答，Capabilities-Exchange-Answer）消息到对等端时，在Product-Name AVP中填写该值。数据来源：本端规划。配置原则：由本端规划的1~127长度的FQDN字符串。
VENDORID|运营商标识|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|参数作用：该参数用于指定本网元的厂商ID。本网元发送CER（Capabilities-Exchange-Req，能力交换请求）消息到对等端时，在Vendor-Id AVP中填写该值。本网元发送CEA（Capabilities-Exchange-Answer，能力交换应答）消息到对等端时，在Vendor-Id AVP中填写该值。数据来源：本端规划。配置原则：配置为协议规定的厂商ID号，常用的有：10415：3GPP3902：ZTE推荐填写10415。
MAXCONN|支持的最大连接数|参数可选性:任选参数；参数类型:整数；参数范围为:32~2048。|参数作用：本参数用于指定Diameter连接数据的全局容量上限。当本网元和对端网元需要建立Diameter链路（ADD DIM RCPLINK）时，配置本参数。数据来源：本端规划。配置原则：根据网元所需要建立的最大Diameter链路数进行设置。修改本参数需要通过RESET SYSTEM命令重启本网元才能生效。
MAXROUTE|支持的最大路由数|参数可选性:任选参数；参数类型:整数；参数范围为:64~8192。|参数作用：用于指定Diameter路由数的全局容量上限。当本网元需要向对端网元发送Diameter消息时，配置本参数。具体的路由数包括ADD DIM ROUTE命令所配置的路由条数和根据Diameter链路自动生成的路由条数。数据来源：：本端规划。配置原则：根据网元规划需要建立的最大Diameter路由条数进行设置。修改本参数需要通过RESET SYSTEM命令重启本网元才能生效。
ACTIVETIME|消息重发间隔（秒）|参数可选性:任选参数；参数类型:整数；参数范围为:1~20。|参数作用：用于指定本网元未收到Diameter响应消息时，重发Diameter请求消息的时间间隔。不包括Diameter基本消息CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）、DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）、DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）。数据来源：本端规划。配置原则：建议使用默认值7秒。
RESENDTIMES|消息重发次数|参数可选性:任选参数；参数类型:整数；参数范围为:0~5。|参数作用：用于指定消息重发的次数。消息重发次数是同一个消息重发的最大次数。当本节点发送请求消息时设置消息重发定时器，定时器到时如果没有接收到响应，则本节点重新选择一条链路发送该消息。数据来源：本端规划。配置原则：建议使用默认值0次，也就是不进行重发。
BUSYCYCLE|忙检测周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:1~60。|参数作用：用于指定对等端忙的检测周期。本端收到某条链路上回复的原因为DIAMETER_TOO_BUSY的应答消息后，在一段时间内本端不使用此链路发送消息。其中“在一段时间内”的时间长度可配置。数据来源：运营商规划。配置原则：根据网元所在当地的网络情况配置。推荐使用默认值10秒。
命令举例 : 
查询Diameter协议基本配置。 
SHOW DIM GLOBAL; 
`
命令 (No.1): SHOW DIM GLOBAL
操作维护       产品名称 运营商标识 心跳检测时长（秒） 支持的最大连接数 支持的最大路由数 消息重发间隔（秒） 消息重发次数 忙检测周期(秒) 
---------------------------------------------------------------------------------------------------------------------------------------
修改           ZTE      10415      30                 1024             4096             7                  0            10             
---------------------------------------------------------------------------------------------------------------------------------------
记录数：1
命令执行成功（耗时 0.023 秒）。
` 
相关命令 : 
[修改DIAMETER协议基本配置]
# DIAMETER链路闭塞配置 
# DIAMETER链路闭塞配置 
背景知识 : 
当网元因升级或者容灾倒换不提供服务时，可以通过此命令一键闭塞所有的Diameter链路。当本网元重新恢复提供服务时，可以通过此命令一键解闭塞所有的Diameter链路。 
功能描述 : 
该配置用于控制本网元是否允许建立Diameter链路。 
当本网元需要关闭对外所有的Diameter链路时，可以使用该命令闭塞所有的Diameter链路。闭塞后本网元所有的Diameter链路将会关闭，不收发任何Diameter消息。 
在Diameter链路闭塞之后，如果本网元想要再重新提供Diameter链路功能，则可以修改此配置解闭塞Diameter链路。 
## SET DIAMLINKBLOCK 
## SET DIAMLINKBLOCK 
命令功能 : 
该命令用于修改Diameter链路闭塞状态。 
当网元进行升级或者容灾倒换不再对外提供服务时，可以通过此命令一键闭塞所有的Diameter链路。 
当本网元重新恢复提供服务时，可以通过此命令一键解闭塞所有的Diameter链路。 
注意事项 : 
无
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BLOCKFLAG|人工闭塞标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置Diameter链路状态。数据来源：与对端协商规划。配置原则：闭塞：表示设置Diameter链路状态为闭塞状态。解闭塞：表示设置Diameter链路状态为解闭塞状态。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
BLOCKFLAG|人工闭塞标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置Diameter链路状态。数据来源：与对端协商规划。配置原则：闭塞：表示设置Diameter链路状态为闭塞状态。解闭塞：表示设置Diameter链路状态为解闭塞状态。
命令举例 : 
闭塞Diameter链路。 
SET DIAMLINKBLOCK:BLOCKFLAG="BLOCKED"; 
## SHOW DIAMLINKBLOCK 
## SHOW DIAMLINKBLOCK 
命令功能 : 
该命令用于查询Diameter链路闭塞状态。 
注意事项 : 
无
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
BLOCKFLAG|人工闭塞标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于设置Diameter链路状态。数据来源：与对端协商规划。配置原则：闭塞：表示设置Diameter链路状态为闭塞状态。解闭塞：表示设置Diameter链路状态为解闭塞状态。
命令举例 : 
查询Diameter链路闭塞状态。 
SHOW DIAMLINKBLOCK; 
# DIAMETER链路配置 
# DIAMETER链路配置 
背景知识 : 
Diameter链路运行于SCTP偶联上。Diameter客户端、代理和服务器必须都支持SCTP偶联。 
Diameter对等端是指一个Diameter节点，该节点和另一个特定的Diameter节点有一个直接的传输连接。 
功能描述 : 
Diameter链路配置通过本端主机名称、本端域名、对端主机名称、对端域名、承载协议类型、SCTP承载链路创建一条Diameter链路，并设置该Diameter链路的心跳检测参数。 
当网元之间采用Diameter协议对接设备时，需要使用Diameter链路配置来配置设备间的链路，并确定承载协议类型和关联哪条承载链路。若配置错误，将导致链路不能正常收发Diameter消息。 
本配置依赖于SCTP承载配置，需首先配置好SCTP承载。 
## ADD DIM RCPLINK 
## ADD DIM RCPLINK 
命令功能 : 
该命令用于增加Diameter链路。 
当网元之间采用Diameter协议对接设备时，需要使用Diameter链路配置来配置设备间的链路。 
配置成功后，Diameter协议栈将根据该配置进行Diameter链路建链。Diameter建链成功后，可以在这条链路上进行发送、接收Diameter消息。 
注意事项 : 
配置Diameter链路之前，如果该Diameter链路配置的承载协议类型为SCTP，需要先使用[ADD SCTP]命令配置SCTP承载链路。
本配置支持的Diameter链路条数和动态链路生成的Diameter链路条数的总数为[修改DIAMETER协议基本配置]命令配置的本网元支持的最大链路数。
可通过[SHOW DIMLNKSTAT]命令，查看链路状态是否为建链成功。
同一个承载链路编号，只能关联一条Diameter链路。 
配置Diameter链路之前需要根据对端提供的功能来确定邻接局类型的取值，详见“邻接局类型”参数说明。此字段只能在本命令中设置，通过[修改DIAMETER链路]命令无法修改。
链路名称具有唯一性，不同链路的名称不可以相同。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于唯一标识一条Diameter链路。当需要使用该链路时，需要使用该参数关联到本条Diameter链路配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALHOSTNAME|本端主机名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定该Diameter信令链路的本端主机名，与已配置的本局主机名一致。本局主机名可通过执行查询本局命令查询。本端主机名称在处理基本Diameter消息、动态生成路由、通过上行请求消息查找路由等场景使用。本端主机名称在RCP处理Diameter消息使用，使用本端主机名称填写Origin-Host AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
LOCALREALM|本端域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的本端域名，与已配置的本局域名一致。本局主机名可通过执行查询本局命令查询。本端域名称在RCP处理基本Diameter消息、动态生成路由等场景使用。本端Diameter模块使用，使用本端域名填写Origin-Realm AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTHOSTNAME|对端主机名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端主机名。对端主机名称在RCP处理基本Diameter消息使用，主要包括以下几种情况：本端Diameter模块接收到DWR（Device-Watchdog-Request，设备监控请求）消息时，对比DWR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到DWA（Device-Watchdog-Answer，设备监控应答消息）消息时，对比DWA消息中的Origin-Host AV与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到CER（Capabilities-Exchange-Req，能力交换请求）消息时，对比CER消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到CEA（Capabilities-Exchange-Answer，能力交换应答）消息时，对比CEA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPR（Disconnect-Peer-Request，拆除对等端连接请求）消息时，对比DPR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息时，对比DPA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTREALM|对端域名|参数可选性:必选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端域名。对端域名在Diameter生成域路由、发送下行请求消息查找路由等场景使用。本端Diameter模块生成域路由是指根据链路的对端域名，动态生成一条路由，用以发送下行请求消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
ADJTYPE|邻接局类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。默认值:DRA。|参数作用：本参数用于配置对端邻接局的类型。数据来源：对端网元的类型。配置原则：DRA：表示链路对端的网元为DRA，此链路上默认支持收发所有接口的消息。PCEF：表示链路对端的网元为PCEF，此链路上默认支持收发Gx接口的消息。SPR：表示链路对端的网元为SPR，此链路上默认支持收发Sp和Sp'接口的消息。AF：表示链路对端的网元为AF，此链路上默认支持收发Rx接口的消息。OCS：表示链路对端的网元为OCS，此链路上默认支持收发Sy接口的消息。TDF：表示链路对端的网元为TDF，此链路上默认支持收发Sd接口的消息。PCRF：表示此链路为容灾使用的Diameter链路，此链路上默认支持收发所有接口的消息。
CONNID|SCTP承载链路|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于指定Diameter链路关联承载链路。数据来源：本端规划。配置原则：若承载协议类型为SCTP，该参数引用ADD DIMSCTP命令中配置的SCTP标识ID。
PROTOCOL|承载协议类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于指定Diameter链路关联承载链路类型。数据来源：本端规划。配置原则：当承载协议类型为SCTP时，则SCTP承载链路的标识为ADD DIMSCTP命令中配置的SCTP承载链路的SCTP标识。
NAME|链路名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~32个字符。|参数作用：本参数用于配置Diameter链路的名称。数据来源：本端规划。配置原则：不同链路的名称不可重复。
HEARTBEAT|是否进行心跳检测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:YES。|参数作用：本参数用于配置该链路是否需要进行心跳检测。数据来源：本端规划。配置原则：如果配置为“是”，则本端Diameter模块正常发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息给Diameter对等端。如果该参数配置为“否”，则本端Diameter模块不发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息。
HEARTBEATCYCLE|心跳检测周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~360。默认值:30。|参数作用：心跳检测周期指本端向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息的间隔时长。本端和对等端之间的Diameter动态连接链路上没有流量交互时，本网元向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息，用于检测该Diameter链路是否正常。数据来源：本端规划。配置原则：建议使用默认值30s。
HEARTBEATTIMES|心跳检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。默认值:3。|参数作用：该链路对等端未回复心跳检测DWR（Device-Watchdog-Request，设备监控请求）消息时，本网元重复发送DWR（Device-Watchdog-Request，设备监控请求）心跳检测的次数。如果DWR（Device-Watchdog-Request，设备监控请求）心跳消息发送超过该次数，对等端仍没有回复，则该Diameter链路会主动断链。数据来源：本端规划。配置原则：建议使用默认值3次。
TLSENABLED|是否支持TLS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NO。|参数作用：使用该Diameter链路与对等端通信时，是否使用TLS（Transport Layer Security，传输层安全）协议。数据来源：与对端网元协商规划。配置原则：建议关闭。
PPID|偶联负荷协议标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:ANY。|参数作用：本参数在“承载协议类型”选择SCTP承载链路时有效，用于标识Diameter链路要求偶联支持的负荷协议类型。数据来源：与对端网元协商规划。配置原则：若偶联负荷协议标识为“任意”（值为0），兼容旧协议。若偶联负荷协议标识为“SCTP数据块”（值为46），表示用于传输SCTP数据块。若偶联负荷协议标识为“DTLS/SCTP数据块”（值为47），表示用于传输DTLS加密的SCTP数据块。建议使用默认值0。
BLOCKFLAG|人工闭塞标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:UNBLOCK。|参数作用：此参数用于标识Diameter链路人工闭塞或解闭塞的操作。数据来源：与对端网元协商规划。配置原则：此参数值为闭塞，则人工中断链路。此参数值为解闭塞，则链路正常建链。建议使用默认值解闭塞。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于唯一标识一条Diameter链路。当需要使用该链路时，需要使用该参数关联到本条Diameter链路配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALHOSTNAME|本端主机名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定该Diameter信令链路的本端主机名，与已配置的本局主机名一致。本局主机名可通过执行查询本局命令查询。本端主机名称在处理基本Diameter消息、动态生成路由、通过上行请求消息查找路由等场景使用。本端主机名称在RCP处理Diameter消息使用，使用本端主机名称填写Origin-Host AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
LOCALREALM|本端域名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的本端域名，与已配置的本局域名一致。本局主机名可通过执行查询本局命令查询。本端域名称在RCP处理基本Diameter消息、动态生成路由等场景使用。本端Diameter模块使用，使用本端域名填写Origin-Realm AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTHOSTNAME|对端主机名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端主机名。对端主机名称在RCP处理基本Diameter消息使用，主要包括以下几种情况：本端Diameter模块接收到DWR（Device-Watchdog-Request，设备监控请求）消息时，对比DWR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到DWA（Device-Watchdog-Answer，设备监控应答消息）消息时，对比DWA消息中的Origin-Host AV与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到CER（Capabilities-Exchange-Req，能力交换请求）消息时，对比CER消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到CEA（Capabilities-Exchange-Answer，能力交换应答）消息时，对比CEA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPR（Disconnect-Peer-Request，拆除对等端连接请求）消息时，对比DPR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息时，对比DPA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTREALM|对端域名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端域名。对端域名在Diameter生成域路由、发送下行请求消息查找路由等场景使用。本端Diameter模块生成域路由是指根据链路的对端域名，动态生成一条路由，用以发送下行请求消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
CONNID|SCTP承载链路|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于指定Diameter链路关联承载链路。数据来源：本端规划。配置原则：若承载协议类型为SCTP，该参数引用ADD DIMSCTP命令中配置的SCTP标识ID。
PROTOCOL|承载协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于指定Diameter链路关联承载链路类型。数据来源：本端规划。配置原则：当承载协议类型为SCTP时，则SCTP承载链路的标识为ADD DIMSCTP命令中配置的SCTP承载链路的SCTP标识。
NAME|链路名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~32个字符。|参数作用：本参数用于配置Diameter链路的名称。数据来源：本端规划。配置原则：不同链路的名称不可重复。
HEARTBEAT|是否进行心跳检测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置该链路是否需要进行心跳检测。数据来源：本端规划。配置原则：如果配置为“是”，则本端Diameter模块正常发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息给Diameter对等端。如果该参数配置为“否”，则本端Diameter模块不发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息。
HEARTBEATCYCLE|心跳检测周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~360。|参数作用：心跳检测周期指本端向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息的间隔时长。本端和对等端之间的Diameter动态连接链路上没有流量交互时，本网元向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息，用于检测该Diameter链路是否正常。数据来源：本端规划。配置原则：建议使用默认值30s。
HEARTBEATTIMES|心跳检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|参数作用：该链路对等端未回复心跳检测DWR（Device-Watchdog-Request，设备监控请求）消息时，本网元重复发送DWR（Device-Watchdog-Request，设备监控请求）心跳检测的次数。如果DWR（Device-Watchdog-Request，设备监控请求）心跳消息发送超过该次数，对等端仍没有回复，则该Diameter链路会主动断链。数据来源：本端规划。配置原则：建议使用默认值3次。
TLSENABLED|是否支持TLS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：使用该Diameter链路与对等端通信时，是否使用TLS（Transport Layer Security，传输层安全）协议。数据来源：与对端网元协商规划。配置原则：建议关闭。
PPID|偶联负荷协议标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数在“承载协议类型”选择SCTP承载链路时有效，用于标识Diameter链路要求偶联支持的负荷协议类型。数据来源：与对端网元协商规划。配置原则：若偶联负荷协议标识为“任意”（值为0），兼容旧协议。若偶联负荷协议标识为“SCTP数据块”（值为46），表示用于传输SCTP数据块。若偶联负荷协议标识为“DTLS/SCTP数据块”（值为47），表示用于传输DTLS加密的SCTP数据块。建议使用默认值0。
ADJTYPE|邻接局类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置对端邻接局的类型。数据来源：对端网元的类型。配置原则：DRA：表示链路对端的网元为DRA，此链路上默认支持收发所有接口的消息。PCEF：表示链路对端的网元为PCEF，此链路上默认支持收发Gx接口的消息。SPR：表示链路对端的网元为SPR，此链路上默认支持收发Sp和Sp'接口的消息。AF：表示链路对端的网元为AF，此链路上默认支持收发Rx接口的消息。OCS：表示链路对端的网元为OCS，此链路上默认支持收发Sy接口的消息。TDF：表示链路对端的网元为TDF，此链路上默认支持收发Sd接口的消息。PCRF：表示此链路为容灾使用的Diameter链路，此链路上默认支持收发所有接口的消息。
BLOCKFLAG|人工闭塞标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：此参数用于标识Diameter链路人工闭塞或解闭塞的操作。数据来源：与对端网元协商规划。配置原则：此参数值为闭塞，则人工中断链路。此参数值为解闭塞，则链路正常建链。建议使用默认值解闭塞。
命令举例 : 
增加Diameter链路：增加RCP与PGW之间的链路，链路号为1，本端主机名称为X.B.C，本端域名为B.C，对端主机名称为Y.B.C，对端域名为B.C，邻接局类型为PCEF，SCTP承载节点ID为1，承载协议类型为SCTP，链路名称为A。 
ADD DIM RCPLINK:LINKNO=1,LOCALHOSTNAME="X.B.C",LOCALREALM="B.C",DSTHOSTNAME="Y.B.C",DSTREALM="B.C",ADJTYPE="PCEF",CONNID=1,PROTOCOL="SCTP",NAME="A" 
相关命令 : 
[修改DIAMETER链路]
[删除DIAMETER链路]
[查询DIAMETER链路]
## SET DIM RCPLINK 
## SET DIM RCPLINK 
命令功能 : 
该命令用于修改Diameter链路。 
当维护人员根据实际需求，需要修改已有Diameter链路的部分参数时，使用该命令设置Diameter链路。 
当修改了本端主机名称、本端域名、对端主机名称、对端域名、SCTP承载链路、承载协议类型、是否支持TLS后，Diameter协议栈将根据该配置对该Diameter链路重新建链。 
注意事项 : 
修改偶联配置前需要确定修改后的目的实体数据同步（比如IP地址）已经完成，否则会导致在该条链路上的所有消息都失败。 
使用该命令修改Diameter链路的配置信息，必须是已使用[增加DIAMETER链路]新增的链路。
链路号为已经配置成功的Diameter链路号。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于唯一标识一条Diameter链路。当需要使用该链路时，需要使用该参数关联到本条Diameter链路配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALHOSTNAME|本端主机名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定该Diameter信令链路的本端主机名，与已配置的本局主机名一致。本局主机名可通过执行查询本局命令查询。本端主机名称在处理基本Diameter消息、动态生成路由、通过上行请求消息查找路由等场景使用。本端主机名称在RCP处理Diameter消息使用，使用本端主机名称填写Origin-Host AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
LOCALREALM|本端域名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的本端域名，与已配置的本局域名一致。本局主机名可通过执行查询本局命令查询。本端域名称在RCP处理基本Diameter消息、动态生成路由等场景使用。本端Diameter模块使用，使用本端域名填写Origin-Realm AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTHOSTNAME|对端主机名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端主机名。对端主机名称在RCP处理基本Diameter消息使用，主要包括以下几种情况：本端Diameter模块接收到DWR（Device-Watchdog-Request，设备监控请求）消息时，对比DWR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到DWA（Device-Watchdog-Answer，设备监控应答消息）消息时，对比DWA消息中的Origin-Host AV与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到CER（Capabilities-Exchange-Req，能力交换请求）消息时，对比CER消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到CEA（Capabilities-Exchange-Answer，能力交换应答）消息时，对比CEA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPR（Disconnect-Peer-Request，拆除对等端连接请求）消息时，对比DPR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息时，对比DPA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTREALM|对端域名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端域名。对端域名在Diameter生成域路由、发送下行请求消息查找路由等场景使用。本端Diameter模块生成域路由是指根据链路的对端域名，动态生成一条路由，用以发送下行请求消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
CONNID|SCTP承载链路|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于指定Diameter链路关联承载链路。数据来源：本端规划。配置原则：若承载协议类型为SCTP，该参数引用ADD DIMSCTP命令中配置的SCTP标识ID。
PROTOCOL|承载协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于指定Diameter链路关联承载链路类型。数据来源：本端规划。配置原则：当承载协议类型为SCTP时，则SCTP承载链路的标识为ADD DIMSCTP命令中配置的SCTP承载链路的SCTP标识。
NAME|链路名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~32个字符。|参数作用：本参数用于配置Diameter链路的名称。数据来源：本端规划。配置原则：不同链路的名称不可重复。
HEARTBEAT|是否进行心跳检测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置该链路是否需要进行心跳检测。数据来源：本端规划。配置原则：如果配置为“是”，则本端Diameter模块正常发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息给Diameter对等端。如果该参数配置为“否”，则本端Diameter模块不发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息。
HEARTBEATCYCLE|心跳检测周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~360。|参数作用：心跳检测周期指本端向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息的间隔时长。本端和对等端之间的Diameter动态连接链路上没有流量交互时，本网元向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息，用于检测该Diameter链路是否正常。数据来源：本端规划。配置原则：建议使用默认值30s。
HEARTBEATTIMES|心跳检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|参数作用：该链路对等端未回复心跳检测DWR（Device-Watchdog-Request，设备监控请求）消息时，本网元重复发送DWR（Device-Watchdog-Request，设备监控请求）心跳检测的次数。如果DWR（Device-Watchdog-Request，设备监控请求）心跳消息发送超过该次数，对等端仍没有回复，则该Diameter链路会主动断链。数据来源：本端规划。配置原则：建议使用默认值3次。
TLSENABLED|是否支持TLS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：使用该Diameter链路与对等端通信时，是否使用TLS（Transport Layer Security，传输层安全）协议。数据来源：与对端网元协商规划。配置原则：建议关闭。
PPID|偶联负荷协议标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数在“承载协议类型”选择SCTP承载链路时有效，用于标识Diameter链路要求偶联支持的负荷协议类型。数据来源：与对端网元协商规划。配置原则：若偶联负荷协议标识为“任意”（值为0），兼容旧协议。若偶联负荷协议标识为“SCTP数据块”（值为46），表示用于传输SCTP数据块。若偶联负荷协议标识为“DTLS/SCTP数据块”（值为47），表示用于传输DTLS加密的SCTP数据块。建议使用默认值0。
BLOCKFLAG|人工闭塞标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：此参数用于标识Diameter链路人工闭塞或解闭塞的操作。数据来源：与对端网元协商规划。配置原则：此参数值为闭塞，则人工中断链路。此参数值为解闭塞，则链路正常建链。建议使用默认值解闭塞。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于唯一标识一条Diameter链路。当需要使用该链路时，需要使用该参数关联到本条Diameter链路配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALHOSTNAME|本端主机名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定该Diameter信令链路的本端主机名，与已配置的本局主机名一致。本局主机名可通过执行查询本局命令查询。本端主机名称在处理基本Diameter消息、动态生成路由、通过上行请求消息查找路由等场景使用。本端主机名称在RCP处理Diameter消息使用，使用本端主机名称填写Origin-Host AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
LOCALREALM|本端域名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的本端域名，与已配置的本局域名一致。本局主机名可通过执行查询本局命令查询。本端域名称在RCP处理基本Diameter消息、动态生成路由等场景使用。本端Diameter模块使用，使用本端域名填写Origin-Realm AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTHOSTNAME|对端主机名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端主机名。对端主机名称在RCP处理基本Diameter消息使用，主要包括以下几种情况：本端Diameter模块接收到DWR（Device-Watchdog-Request，设备监控请求）消息时，对比DWR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到DWA（Device-Watchdog-Answer，设备监控应答消息）消息时，对比DWA消息中的Origin-Host AV与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到CER（Capabilities-Exchange-Req，能力交换请求）消息时，对比CER消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到CEA（Capabilities-Exchange-Answer，能力交换应答）消息时，对比CEA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPR（Disconnect-Peer-Request，拆除对等端连接请求）消息时，对比DPR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息时，对比DPA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTREALM|对端域名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端域名。对端域名在Diameter生成域路由、发送下行请求消息查找路由等场景使用。本端Diameter模块生成域路由是指根据链路的对端域名，动态生成一条路由，用以发送下行请求消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
CONNID|SCTP承载链路|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于指定Diameter链路关联承载链路。数据来源：本端规划。配置原则：若承载协议类型为SCTP，该参数引用ADD DIMSCTP命令中配置的SCTP标识ID。
PROTOCOL|承载协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于指定Diameter链路关联承载链路类型。数据来源：本端规划。配置原则：当承载协议类型为SCTP时，则SCTP承载链路的标识为ADD DIMSCTP命令中配置的SCTP承载链路的SCTP标识。
NAME|链路名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~32个字符。|参数作用：本参数用于配置Diameter链路的名称。数据来源：本端规划。配置原则：不同链路的名称不可重复。
HEARTBEAT|是否进行心跳检测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置该链路是否需要进行心跳检测。数据来源：本端规划。配置原则：如果配置为“是”，则本端Diameter模块正常发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息给Diameter对等端。如果该参数配置为“否”，则本端Diameter模块不发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息。
HEARTBEATCYCLE|心跳检测周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~360。|参数作用：心跳检测周期指本端向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息的间隔时长。本端和对等端之间的Diameter动态连接链路上没有流量交互时，本网元向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息，用于检测该Diameter链路是否正常。数据来源：本端规划。配置原则：建议使用默认值30s。
HEARTBEATTIMES|心跳检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|参数作用：该链路对等端未回复心跳检测DWR（Device-Watchdog-Request，设备监控请求）消息时，本网元重复发送DWR（Device-Watchdog-Request，设备监控请求）心跳检测的次数。如果DWR（Device-Watchdog-Request，设备监控请求）心跳消息发送超过该次数，对等端仍没有回复，则该Diameter链路会主动断链。数据来源：本端规划。配置原则：建议使用默认值3次。
TLSENABLED|是否支持TLS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：使用该Diameter链路与对等端通信时，是否使用TLS（Transport Layer Security，传输层安全）协议。数据来源：与对端网元协商规划。配置原则：建议关闭。
PPID|偶联负荷协议标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数在“承载协议类型”选择SCTP承载链路时有效，用于标识Diameter链路要求偶联支持的负荷协议类型。数据来源：与对端网元协商规划。配置原则：若偶联负荷协议标识为“任意”（值为0），兼容旧协议。若偶联负荷协议标识为“SCTP数据块”（值为46），表示用于传输SCTP数据块。若偶联负荷协议标识为“DTLS/SCTP数据块”（值为47），表示用于传输DTLS加密的SCTP数据块。建议使用默认值0。
BLOCKFLAG|人工闭塞标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：此参数用于标识Diameter链路人工闭塞或解闭塞的操作。数据来源：与对端网元协商规划。配置原则：此参数值为闭塞，则人工中断链路。此参数值为解闭塞，则链路正常建链。建议使用默认值解闭塞。
命令举例 : 
修改Diameter链路：链路号为1，本端主机名称为X.B.C，本端域名为B.C，对端主机名称为Y.B.C，对端域名为B.C，SCTP承载节点ID为1，承载协议类型为SCTP，链路名称为A。 
 SET DIM RCPLINK:LINKNO=1,LOCALHOSTNAME="X.B.C",LOCALREALM="B.C",DSTHOSTNAME="Y.B.C",DSTREALM="B.C",CONNID=1,PROTOCOL="SCTP",NAME="A"; 
相关命令 : 
[增加DIAMETER链路]
[删除DIAMETER链路]
[查询DIAMETER链路]
## DEL DIM RCPLINK 
## DEL DIM RCPLINK 
命令功能 : 
该命令用于删除Diameter链路。 
当维护人员客户根据实际需求，不再使用已有Diameter链路时，使用该命令删除该Diameter链路。 
当删除了某条Diameter链路后，该链路中断，将无法接收、发送Diameter消息。 
注意事项 : 
删除链路配置前需要先确定不再需要该条链路，否则会导致在该条链路上的所有消息都失败。 
删除Diameter链路前，需要先删除Diameter路由配置，[ADD DIMROUTE]命令增加的链路号为被删除链路的Diameter路由。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于指定需要删除的Diameter链路号。数据来源：与对端网元协商规划。配置原则：输入需要删除的链路号。
命令举例 : 
删除Diameter链路：链路号为1。 
DEL DIM RCPLINK:LINKNO=1;  
相关命令 : 
[增加DIAMETER链路]
[修改DIAMETER链路]
[查询DIAMETER链路]
## SHOW DIM RCPLINK 
## SHOW DIM RCPLINK 
命令功能 : 
该命令用于查询Diameter链路。 
当需要查询已经配置的Diameter链路时，使用该命令查询全部或者部分Diameter链路。 
注意事项 : 
不输入参数默认查询所有配置。输入链路号和链路名称，则查询指定条件的链路配置。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于指定需要查询的起始链路号。数据来源：根据查询需求决定。配置原则：输入需要查询的起始链路号。
END|结束链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于指定需要查询的结束链路号。数据来源：根据查询需求决定。配置原则：输入需要查询的结束链路号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于唯一标识一条Diameter链路。当需要使用该链路时，需要使用该参数关联到本条Diameter链路配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALHOSTNAME|本端主机名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定该Diameter信令链路的本端主机名，与已配置的本局主机名一致。本局主机名可通过执行查询本局命令查询。本端主机名称在处理基本Diameter消息、动态生成路由、通过上行请求消息查找路由等场景使用。本端主机名称在RCP处理Diameter消息使用，使用本端主机名称填写Origin-Host AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
LOCALREALM|本端域名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的本端域名，与已配置的本局域名一致。本局主机名可通过执行查询本局命令查询。本端域名称在RCP处理基本Diameter消息、动态生成路由等场景使用。本端Diameter模块使用，使用本端域名填写Origin-Realm AVP，主要包括以下几种情况：RCP发送CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。RCP发送DWR（Device-Watchdog-Request，设备监控请求）/DWA（Device-Watchdog-Answer，设备监控应答消息）消息。RCP发送DPR（Disconnect-Peer-Request，拆除对等端连接请求）/DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTHOSTNAME|对端主机名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端主机名。对端主机名称在RCP处理基本Diameter消息使用，主要包括以下几种情况：本端Diameter模块接收到DWR（Device-Watchdog-Request，设备监控请求）消息时，对比DWR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到DWA（Device-Watchdog-Answer，设备监控应答消息）消息时，对比DWA消息中的Origin-Host AV与对端主机名称是否相同。如果不同会给对端发送断链消息，Diameter链路断链。本端Diameter模块收到CER（Capabilities-Exchange-Req，能力交换请求）消息时，对比CER消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到CEA（Capabilities-Exchange-Answer，能力交换应答）消息时，对比CEA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPR（Disconnect-Peer-Request，拆除对等端连接请求）消息时，对比DPR消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。本端Diameter模块收到DPA（Disconnect-Peer-Answer，拆除对等端连接应答）消息时，对比DPA消息中的Origin-Host AVP与对端主机名称是否相同。如果不同，RCP和对端网元建链失败。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
DSTREALM|对端域名|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：本参数用于指定Diameter信令链路的对端域名。对端域名在Diameter生成域路由、发送下行请求消息查找路由等场景使用。本端Diameter模块生成域路由是指根据链路的对端域名，动态生成一条路由，用以发送下行请求消息。数据来源：运营商规划。配置原则：由运营商规划的1~127长度的FQDN字符串。
CONNID|SCTP承载链路|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：本参数用于指定Diameter链路关联承载链路。数据来源：本端规划。配置原则：若承载协议类型为SCTP，该参数引用ADD DIMSCTP命令中配置的SCTP标识ID。
PROTOCOL|承载协议类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于指定Diameter链路关联承载链路类型。数据来源：本端规划。配置原则：当承载协议类型为SCTP时，则SCTP承载链路的标识为ADD DIMSCTP命令中配置的SCTP承载链路的SCTP标识。
NAME|链路名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~32个字符。|参数作用：本参数用于配置Diameter链路的名称。数据来源：本端规划。配置原则：不同链路的名称不可重复。
HEARTBEAT|是否进行心跳检测|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置该链路是否需要进行心跳检测。数据来源：本端规划。配置原则：如果配置为“是”，则本端Diameter模块正常发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息给Diameter对等端。如果该参数配置为“否”，则本端Diameter模块不发送DWR（Device-Watchdog-Request，设备监控请求）心跳消息。
HEARTBEATCYCLE|心跳检测周期(秒)|参数可选性:任选参数；参数类型:整数；参数范围为:10~360。|参数作用：心跳检测周期指本端向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息的间隔时长。本端和对等端之间的Diameter动态连接链路上没有流量交互时，本网元向对等端周期性发送DWR（Device-Watchdog-Request，设备监控请求）消息，用于检测该Diameter链路是否正常。数据来源：本端规划。配置原则：建议使用默认值30s。
HEARTBEATTIMES|心跳检测次数|参数可选性:任选参数；参数类型:整数；参数范围为:1~100。|参数作用：该链路对等端未回复心跳检测DWR（Device-Watchdog-Request，设备监控请求）消息时，本网元重复发送DWR（Device-Watchdog-Request，设备监控请求）心跳检测的次数。如果DWR（Device-Watchdog-Request，设备监控请求）心跳消息发送超过该次数，对等端仍没有回复，则该Diameter链路会主动断链。数据来源：本端规划。配置原则：建议使用默认值3次。
TLSENABLED|是否支持TLS|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：使用该Diameter链路与对等端通信时，是否使用TLS（Transport Layer Security，传输层安全）协议。数据来源：与对端网元协商规划。配置原则：建议关闭。
PPID|偶联负荷协议标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数在“承载协议类型”选择SCTP承载链路时有效，用于标识Diameter链路要求偶联支持的负荷协议类型。数据来源：与对端网元协商规划。配置原则：若偶联负荷协议标识为“任意”（值为0），兼容旧协议。若偶联负荷协议标识为“SCTP数据块”（值为46），表示用于传输SCTP数据块。若偶联负荷协议标识为“DTLS/SCTP数据块”（值为47），表示用于传输DTLS加密的SCTP数据块。建议使用默认值0。
ADJTYPE|邻接局类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：本参数用于配置对端邻接局的类型。数据来源：对端网元的类型。配置原则：DRA：表示链路对端的网元为DRA，此链路上默认支持收发所有接口的消息。PCEF：表示链路对端的网元为PCEF，此链路上默认支持收发Gx接口的消息。SPR：表示链路对端的网元为SPR，此链路上默认支持收发Sp和Sp'接口的消息。AF：表示链路对端的网元为AF，此链路上默认支持收发Rx接口的消息。OCS：表示链路对端的网元为OCS，此链路上默认支持收发Sy接口的消息。TDF：表示链路对端的网元为TDF，此链路上默认支持收发Sd接口的消息。PCRF：表示此链路为容灾使用的Diameter链路，此链路上默认支持收发所有接口的消息。
BLOCKFLAG|人工闭塞标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：此参数用于标识Diameter链路人工闭塞或解闭塞的操作。数据来源：与对端网元协商规划。配置原则：此参数值为闭塞，则人工中断链路。此参数值为解闭塞，则链路正常建链。建议使用默认值解闭塞。
命令举例 : 
查询Diameter链路：链路号为1。 
SHOW DIM RCPLINK:BEGIN=1,END=1; 
`
命令 (No.1): SHOW DIM RCPLINK:BEGIN=1,END=1;
操作维护         链路号   本端主机名称          本端域名          对端主机名称           对端域名          SCTP承载链路       承载协议类型   链路名称   是否进行心跳检测   心跳检测周期(秒)   心跳检测次数   是否支持TLS
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1        rcp.hatt.zte.com.cn   hatt.zte.com.cn   pcef.hatt.zte.com.cn   hatt.zte.com.cn   1                  SCTP           to pcef    是                 30                 3              否
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.024 秒）。
` 
查询Diameter链路：链路号为1到10之间。 
SHOW DIM RCPLINK:BEGIN=1,END=1; 
`
(No.1) : SHOW DIM RCPLINK:BEGIN=1,END=10
-----------------Npcf_PolicyManagement_0----------------
操作维护       链路号 本端主机名称        本端域名        对端主机名称          对端域名        SCTP承载链路     承载协议类型 链路名称 是否进行心跳检测 心跳检测周期(秒) 心跳检测次数 是否支持TLS 偶联负荷协议标识 邻接局类型 人工闭塞标识 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除 1      rcp.hatt.zte.com.cn hatt.zte.com.cn pcef.hatt.zte.com.cn  hatt.zte.com.cn 1                SCTP         to pcef  是               30               3            否          任意             PCEF       解闭塞       
复制 修改 删除 2      rcp.hatt.zte.com.cn hatt.zte.com.cn spr.hatt.zte.com.cn   hatt.zte.com.cn 2                SCTP         to spr   是               30               3            否          任意             SPR        解闭塞       
复制 修改 删除 3      rcp.hatt.zte.com.cn hatt.zte.com.cn af.hatt.zte.com.cn    hatt.zte.com.cn 3                SCTP         to af    是               30               3            否          任意             AF         解闭塞       
复制 修改 删除 4      rcp.hatt.zte.com.cn hatt.zte.com.cn spcef.hatt.zte.com.cn hatt.zte.com.cn 4                SCTP         to spcef 是               30               3            否          任意             PCEF       解闭塞       
复制 修改 删除 5      rcp.hatt.zte.com.cn hatt.zte.com.cn bpcef.hatt.zte.com.cn hatt.zte.com.cn 5                SCTP         to bpcef 是               30               3            否          任意             PCEF       解闭塞       
复制 修改 删除 8      rcp.hatt.zte.com.cn hatt.zte.com.cn ocs.hatt.zte.com.cn   hatt.zte.com.cn 10               SCTP         to ocs   是               30               3            否          任意             OCS        解闭塞       
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数：6
执行成功开始时间:2021-09-28 16:45:28 耗时: 0.628 秒
` 
相关命令 : 
[增加DIAMETER链路]
[修改DIAMETER链路]
[删除DIAMETER链路]
# DIAMETER链路一般能力配置 
# DIAMETER链路一般能力配置 
背景知识 : 
Diameter对等端是指一个Diameter节点。Diameter本端和Diameter对等端之间可以直接进行传输连接。 
两个Diameter对等端建立传输连接时，必须交换能力交换消息。能力交换消息包括了对等端的标识和能力，如：协议版本号、支持的Diameter应用、安全机制等。 
Diameter一般能力是指CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息的Supported-Vendor-Id AVP、Auth-Application-Id AVP、Inband-Security-Id AVP、Acct-Application-Id AVP所填写的能力值。 
功能描述 : 
Diameter建链时需要使用Diameter链路一般能力配置填写发送给Diameter对等端的CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。 
本端收到来自Diameter对等端的CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息后，需要使用Diameter链路一般能力配置进行能力交换。 
设置与对端能力协商中的以下AVP值，如果不配置，会影响RCP和对端网元建立Diameter链路。 
 
Supported-Vendor-Id（支持厂商）。
 
 
Auth-Application-Id（认证应用能力）。
Auth-Application-Id在Diameter信令链路配置完成后自动生成相应配置，一般不需要配置。如果需要配置，需与对端网元协商后配置成相同的值。
 
 
Inband-Security-Id（安全）。
 
 
Acct-Application-Id（计费应用）。
 
 
## ADD DIM LINKCOMMON 
## ADD DIM LINKCOMMON 
命令功能 : 
该命令用于增加Diameter链路一般能力配置。当RCP网元需要Diameter静态建链时，使用该命令配置本端支持的一般能力。命令执行成功后，RCP可使用所配置的Diameter链路一般能力，在Diameter静态建链时进行能力交换。 
注意事项 : 
 
该命令对使用ADD DIM RCPLINK配置的Diameter链路进行一般能力配置。 
 
RCP系统默认为ADD DIM RCPLINK配置的每条Diameter链路配置Diameter链路一般能力。如果不使用默认配置，需进行手动配置，否则会影响RCP和对端网元建立Diameter链路。 
 
每条Diameter链路只能配置一条Diameter链路一般能力配置。 
 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
VENDOR1|支持厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR2|支持厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR3|支持厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR4|支持厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR5|支持厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR6|支持厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR7|支持厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR8|支持厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR9|支持厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR10|支持厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
AUTHAPP1|认证应用能力ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号1为0。
AUTHAPP2|认证应用能力ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号2为0。
AUTHAPP3|认证应用能力ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号3为0。
AUTHAPP4|认证应用能力ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号4为0。
AUTHAPP5|认证应用能力ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号5为0。
AUTHAPP6|认证应用能力ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号6为0。
AUTHAPP7|认证应用能力ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号7为0。
AUTHAPP8|认证应用能力ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号8为0。
AUTHAPP9|认证应用能力ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号9为0。
AUTHAPP10|认证应用能力ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号10为0。
INBANDSECU1|安全ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号1为0。
INBANDSECU2|安全ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号2为0。
INBANDSECU3|安全ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号3为0。
INBANDSECU4|安全ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号4为0。
INBANDSECU5|安全ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号5为0。
INBANDSECU6|安全ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号6为0。
INBANDSECU7|安全ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号7为0。
INBANDSECU8|安全ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号8为0。
INBANDSECU9|安全ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号9为0。
INBANDSECU10|安全ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号10为0。
ACCTAPP1|计费应用ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号1为0。
ACCTAPP2|计费应用ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号2为0。
ACCTAPP3|计费应用ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号3为0。
ACCTAPP4|计费应用ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号4为0。
ACCTAPP5|计费应用ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号5为0。
ACCTAPP6|计费应用ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号6为0。
ACCTAPP7|计费应用ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号7为0。
ACCTAPP8|计费应用ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号8为0。
ACCTAPP9|计费应用ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号9为0。
ACCTAPP10|计费应用ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号10为0。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
VENDOR1|支持厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR2|支持厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR3|支持厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR4|支持厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR5|支持厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR6|支持厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR7|支持厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR8|支持厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR9|支持厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR10|支持厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
AUTHAPP1|认证应用能力ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号1为0。
AUTHAPP2|认证应用能力ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号2为0。
AUTHAPP3|认证应用能力ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号3为0。
AUTHAPP4|认证应用能力ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号4为0。
AUTHAPP5|认证应用能力ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号5为0。
AUTHAPP6|认证应用能力ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号6为0。
AUTHAPP7|认证应用能力ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号7为0。
AUTHAPP8|认证应用能力ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号8为0。
AUTHAPP9|认证应用能力ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号9为0。
AUTHAPP10|认证应用能力ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号10为0。
INBANDSECU1|安全ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号1为0。
INBANDSECU2|安全ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号2为0。
INBANDSECU3|安全ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号3为0。
INBANDSECU4|安全ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号4为0。
INBANDSECU5|安全ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号5为0。
INBANDSECU6|安全ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号6为0。
INBANDSECU7|安全ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号7为0。
INBANDSECU8|安全ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号8为0。
INBANDSECU9|安全ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号9为0。
INBANDSECU10|安全ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号10为0。
ACCTAPP1|计费应用ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号1为0。
ACCTAPP2|计费应用ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号2为0。
ACCTAPP3|计费应用ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号3为0。
ACCTAPP4|计费应用ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号4为0。
ACCTAPP5|计费应用ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号5为0。
ACCTAPP6|计费应用ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号6为0。
ACCTAPP7|计费应用ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号7为0。
ACCTAPP8|计费应用ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号8为0。
ACCTAPP9|计费应用ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号9为0。
ACCTAPP10|计费应用ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号10为0。
命令举例 : 
增加Diameter链路一般能力，链路号为1，支持厂商ID为10415。 
ADD DIM LINKCOMMON:LINKNO=1,VENDOR1=10415; 
相关命令 : 
[修改DIAMETER链路一般能力]
[删除DIAMETER链路一般能力]
[查询DIAMETER链路一般能力]
## SET DIM LINKCOMMON 
## SET DIM LINKCOMMON 
命令功能 : 
该命令用于修改Diameter链路一般能力配置。当需要重新配置Diameter链路的支持厂商ID、支持认证应用、支持安全、支持计费应用时，使用该命令。命令执行成功后，RCP系统将使用修改后的配置重新发起该Diameter链路的建链。 
注意事项 : 
链路建立成功后，一般情况下不能修改Diameter链路的一般能力配置，否则会影响RCP网元和对端建立的Diameter链路状态。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
VENDOR1|支持厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR2|支持厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR3|支持厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR4|支持厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR5|支持厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR6|支持厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR7|支持厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR8|支持厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR9|支持厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR10|支持厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
AUTHAPP1|认证应用能力ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号1为0。
AUTHAPP2|认证应用能力ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号2为0。
AUTHAPP3|认证应用能力ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号3为0。
AUTHAPP4|认证应用能力ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号4为0。
AUTHAPP5|认证应用能力ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号5为0。
AUTHAPP6|认证应用能力ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号6为0。
AUTHAPP7|认证应用能力ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号7为0。
AUTHAPP8|认证应用能力ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号8为0。
AUTHAPP9|认证应用能力ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号9为0。
AUTHAPP10|认证应用能力ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号10为0。
INBANDSECU1|安全ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号1为0。
INBANDSECU2|安全ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号2为0。
INBANDSECU3|安全ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号3为0。
INBANDSECU4|安全ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号4为0。
INBANDSECU5|安全ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号5为0。
INBANDSECU6|安全ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号6为0。
INBANDSECU7|安全ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号7为0。
INBANDSECU8|安全ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号7为0。
INBANDSECU9|安全ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号9为0。
INBANDSECU10|安全ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号10为0。
ACCTAPP1|计费应用ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号1为0。
ACCTAPP2|计费应用ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号2为0。
ACCTAPP3|计费应用ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号3为0。
ACCTAPP4|计费应用ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号4为0。
ACCTAPP5|计费应用ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号5为0。
ACCTAPP6|计费应用ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号6为0。
ACCTAPP7|计费应用ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号7为0。
ACCTAPP8|计费应用ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号8为0。
ACCTAPP9|计费应用ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号9为0。
ACCTAPP10|计费应用ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号10为0。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
VENDOR1|支持厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR2|支持厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR3|支持厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR4|支持厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR5|支持厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR6|支持厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR7|支持厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR8|支持厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR9|支持厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR10|支持厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
AUTHAPP1|认证应用能力ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号1为0。
AUTHAPP2|认证应用能力ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号2为0。
AUTHAPP3|认证应用能力ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号3为0。
AUTHAPP4|认证应用能力ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号4为0。
AUTHAPP5|认证应用能力ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号5为0。
AUTHAPP6|认证应用能力ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号6为0。
AUTHAPP7|认证应用能力ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号7为0。
AUTHAPP8|认证应用能力ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号8为0。
AUTHAPP9|认证应用能力ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号9为0。
AUTHAPP10|认证应用能力ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号10为0。
INBANDSECU1|安全ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号1为0。
INBANDSECU2|安全ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号2为0。
INBANDSECU3|安全ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号3为0。
INBANDSECU4|安全ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号4为0。
INBANDSECU5|安全ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号5为0。
INBANDSECU6|安全ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号6为0。
INBANDSECU7|安全ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号7为0。
INBANDSECU8|安全ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号7为0。
INBANDSECU9|安全ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号9为0。
INBANDSECU10|安全ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号10为0。
ACCTAPP1|计费应用ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号1为0。
ACCTAPP2|计费应用ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号2为0。
ACCTAPP3|计费应用ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号3为0。
ACCTAPP4|计费应用ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号4为0。
ACCTAPP5|计费应用ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号5为0。
ACCTAPP6|计费应用ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号6为0。
ACCTAPP7|计费应用ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号7为0。
ACCTAPP8|计费应用ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号8为0。
ACCTAPP9|计费应用ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号9为0。
ACCTAPP10|计费应用ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号10为0。
命令举例 : 
修改Diameter链路一般能力，链路号为1，支持厂商ID为10415。 
SET DIM LINKCOMMON:LINKNO=1,VENDOR1=10415; 
相关命令 : 
[增加DIAMETER链路一般能力]
[删除DIAMETER链路一般能力]
[查询DIAMETER链路一般能力]
## DEL DIM LINKCOMMON 
## DEL DIM LINKCOMMON 
命令功能 : 
该命令用于删除Diameter链路一般能力配置。当RCP网元不支持该Diameter链路配置的厂商ID、认证应用、安全或计费应用一般能力时，使用该命令进行删除。命令执行成功后，RCP系统将默认为该Diameter链路的一般能力配置的所有参数值均为0。 
注意事项 : 
链路建立成功后，一般情况下不能删除Diameter链路的一般能力配置，否则会影响RCP网元和对端建立的Diameter链路状态。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
命令举例 : 
删除Diameter链路一般能力，链路号1。 
DEL DIM LINKCOMMON:LINKNO=1; 
相关命令 : 
[增加DIAMETER链路一般能力]
[修改DIAMETER链路一般能力]
[查询DIAMETER链路一般能力]
## SHOW DIM LINKCOMMON 
## SHOW DIM LINKCOMMON 
命令功能 : 
该命令用于查询Diameter链路一般能力配置。 
当需要查看已经配置的Diameter链路一般能力配置时，使用该命令进行查询。查询成功后，可显示该Diameter链路的支持厂商ID、支持认证应用、支持安全、支持计费应用。 
注意事项 : 
不输入参数默认查询所有配置。输入起始链路编号和结束链路编号，查询指定编号范围内的所有配置。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：查询时设置的起始链路号。数据来源：本端规划。配置原则：该参数可通过SHOW DIM RCPLINK查询结果中的链路号LINKNO来设置查询的起始链路号。
END|结束链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：查询时设置的结束链路号。数据来源：本端规划。配置原则：该参数可通过SHOW DIM RCPLINK查询结果的链路号LINKNO来设置查询的结束链路号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
VENDOR1|支持厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR2|支持厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR3|支持厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR4|支持厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR5|支持厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR6|支持厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR7|支持厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR8|支持厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR9|支持厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
VENDOR10|支持厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Supported-Vendor-Id AVP。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0。协议规定中常用厂商标识：3902：ZTE。10415：3GPP。
AUTHAPP1|认证应用能力ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号1为0。
AUTHAPP2|认证应用能力ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号2为0。
AUTHAPP3|认证应用能力ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号3为0。
AUTHAPP4|认证应用能力ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号4为0。
AUTHAPP5|认证应用能力ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号5为0。
AUTHAPP6|认证应用能力ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号6为0。
AUTHAPP7|认证应用能力ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号7为0。
AUTHAPP8|认证应用能力ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号8为0。
AUTHAPP9|认证应用能力ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号9为0。
AUTHAPP10|认证应用能力ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Auth-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对认证、授权的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持认证应用编号不能重复。RCP系统默认生成的支持认证应用编号10为0。
INBANDSECU1|安全ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号1为0。
INBANDSECU2|安全ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号2为0。
INBANDSECU3|安全ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号3为0。
INBANDSECU4|安全ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号4为0。
INBANDSECU5|安全ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号5为0。
INBANDSECU6|安全ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号6为0。
INBANDSECU7|安全ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号7为0。
INBANDSECU8|安全ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号8为0。
INBANDSECU9|安全ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号9为0。
INBANDSECU10|安全ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Inband-Security-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对安全的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个安全编号不能重复。RCP系统默认生成的支持安全编号10为0。
ACCTAPP1|计费应用ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号1为0。
ACCTAPP2|计费应用ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号2为0。
ACCTAPP3|计费应用ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号3为0。
ACCTAPP4|计费应用ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号4为0。
ACCTAPP5|计费应用ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号5为0。
ACCTAPP6|计费应用ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号6为0。
ACCTAPP7|计费应用ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号7为0。
ACCTAPP8|计费应用ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号8为0。
ACCTAPP9|计费应用ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号9为0。
ACCTAPP10|计费应用ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Acct-Application-Id AVP。本端Diameter模块与对等端进行能力交换，将本端对计费的支持告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个支持计费应用编号不能重复。RCP系统默认生成的支持计费应用编号10为0。
命令举例 : 
查询Diameter链路一般能力，链路号为1。 
SHOW DIM LINKCOMMON:BEGIN=1,END=1; 
`
命令 (No.1): SHOW DIM LINKCOMMON:BEGIN=1,END=1;
操作维护         链路号   支持厂商ID1   支持厂商ID2   支持厂商ID3   支持厂商ID4   支持厂商ID5   支持厂商ID6   支持厂商ID7   支持厂商ID8   支持厂商ID9   支持厂商ID10   认证应用能力ID1   认证应用能力ID2   认证应用能力ID3   认证应用能力ID4   认证应用能力ID5   认证应用能力ID6   认证应用能力ID7   认证应用能力ID8   认证应用能力ID9   认证应用能力ID10   安全ID1      安全ID2      安全ID3      安全ID4      安全ID5      安全ID6      安全ID7      安全ID8      安全ID9      安全ID10     计费应用ID1   计费应用ID2   计费应用ID3   计费应用ID4   计费应用ID5   计费应用ID6   计费应用ID7   计费应用ID8   计费应用ID9   计费应用ID10
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1        0             0             0             0             0             0             0             0             0             0              3                 4                 0                 0                 0                 0                 0                 0                 0                 0                  0            0            0            0            0            0            0            0            0            0            3             0             0             0             0             0             0             0             0             0
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.023 秒）。
` 
相关命令 : 
[增加DIAMETER链路一般能力]
[修改DIAMETER链路一般能力]
[删除DIAMETER链路一般能力]
# DIAMETER链路特殊能力配置 
# DIAMETER链路特殊能力配置 
背景知识 : 
Diameter对等端是指一个Diameter节点，Diameter本端和Diameter对等端之间可以直接进行传输连接。 
两个Diameter对等端建立传输连接时，必须交换能力交换消息。能力交换消息包括了对等端的标识和能力（协议版本号、支持的Diameter应用、安全机制等）。 
Diameter特殊能力是指CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息的Vendor-Specific-Application-Id AVP填写的能力值。 
CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息的具体内容，可参考RFC3588的5.3.1节、5.3.2节。 
功能描述 : 
该配置提供了本网元的Diameter静态建链需要的特殊能力。 
特殊能力配置中填写的Vendor-Id和Application-Id会被封装成Vendor-Specific-Application-Id这个组合AVP，Diameter建链时需要使用Diameter链路特殊能力配置填写发送给Diameter对等端的CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息。 
本端收到来自Diameter对等端的CER（Capabilities-Exchange-Req，能力交换请求）/CEA（Capabilities-Exchange-Answer，能力交换应答）消息后，需要使用Diameter链路特殊能力配置进行能力交换。 
如果不配置，会影响RCP和对端网元建立Diameter链路。 
## ADD DIM LINKSPECIFIC 
## ADD DIM LINKSPECIFIC 
命令功能 : 
该命令用于增加Diameter链路特殊能力配置。当RCP网元需要Diameter静态建链时，使用该命令配置本端支持的特殊能力。配置成功后，RCP可使用所配置的Diameter链路特殊能力在Diameter静态建链时进行能力交换。 
注意事项 : 
 
该命令对ADD DIM RCPLINK配置的Diameter链路进行特殊能力配置。 
 
RCP系统默认为ADD DIM RCPLINK配置的每条Diameter链路配置Diameter链路特殊能力为0，根据维护人员需求，需要进行手工配置其他特殊能力值。 
 
每条Diameter链路只能配置十条Diameter链路特殊能力配置。 
 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
SPINDEX|特殊能力索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~10。|参数作用：该参数为Diameter链路关联的特殊能力的索引。数据来源：与对端协商。配置原则：同一个链路号的十条Diameter链路特殊能力需要配置不同的特殊能力索引。
VENDOR1|厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR2|厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR3|厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR4|厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR5|厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR6|厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR7|厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR8|厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR9|厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR10|厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
AUTHAPP|支持鉴权应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Auth-Application-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的认证、授权告知Diameter链路的另一端。数据来源：与对端协商。配置原则：常用鉴权应用标识：16777231：SP接口。16777232：Sp'接口。16777236：Rx接口。16777238：Gx接口。16777302：Sy接口。16777303：Sd接口。
ACCTAPP|支持计费应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Acct-Application-Id AVP）。本端DIAMETER模块与对等端进行能力交换，将本端支持的计费应用告知DIAMETER链路的另一端。数据来源：与对端协商。配置原则：RCP系统默认生成的支持计费应用编号为0。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
SPINDEX|特殊能力索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|参数作用：该参数为Diameter链路关联的特殊能力的索引。数据来源：与对端协商。配置原则：同一个链路号的十条Diameter链路特殊能力需要配置不同的特殊能力索引。
VENDOR1|厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR2|厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR3|厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR4|厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR5|厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR6|厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR7|厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR8|厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR9|厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR10|厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
AUTHAPP|支持鉴权应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Auth-Application-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的认证、授权告知Diameter链路的另一端。数据来源：与对端协商。配置原则：常用鉴权应用标识：16777231：SP接口。16777232：Sp'接口。16777236：Rx接口。16777238：Gx接口。16777302：Sy接口。16777303：Sd接口。
ACCTAPP|支持计费应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Acct-Application-Id AVP）。本端DIAMETER模块与对等端进行能力交换，将本端支持的计费应用告知DIAMETER链路的另一端。数据来源：与对端协商。配置原则：RCP系统默认生成的支持计费应用编号为0。
命令举例 : 
创建链路号为1，特殊能力索引号为1，厂商ID为10415，鉴权应用ID为16777238的链路特殊能力。 
ADD DIM LINKSPECIFIC:LINKNO=1,SPINDEX=1,VENDOR1=10415,AUTHAPP=16777238; 
相关命令 : 
[修改DIAMETER链路特殊能力]
[删除DIAMETER链路特殊能力]
[查询DIAMETER链路特殊能力]
## SET DIM LINKSPECIFIC 
## SET DIM LINKSPECIFIC 
命令功能 : 
该命令用于修改Diameter链路特殊能力配置。当需要重新配置Diameter链路的厂商ID、支持鉴权应用编号、支持计费应用编号时，使用该命令。命令执行成功后，RCP系统将使用修改后的配置重新发起该Diameter链路的建链。 
注意事项 : 
链路建立成功后，一般情况下不能修改Diameter链路的特殊能力配置，否则会影响RCP网元和对端建立的Diameter链路状态。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
SPINDEX|特殊能力索引|参数可选性:必选参数；参数类型:整数；参数范围为:1~10。|参数作用：该参数为Diameter链路关联的特殊能力的索引。数据来源：与对端协商。配置原则：同一个链路号的十条Diameter链路特殊能力需要配置不同的特殊能力索引。
VENDOR1|厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR2|厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR3|厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR4|厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR5|厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR6|厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR7|厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR8|厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR9|厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR10|厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP(Vendor-Id AVP)。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
AUTHAPP|支持鉴权应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Auth-Application-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的认证、授权告知Diameter链路的另一端。数据来源：与对端协商。配置原则：常用鉴权应用标识：16777231：SP接口。16777232：Sp'接口。16777236：Rx接口。16777238：Gx接口。16777302：Sy接口。16777303：Sd接口。
ACCTAPP|支持计费应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Acct-Application-Id AVP）。本端DIAMETER模块与对等端进行能力交换，将本端支持的计费应用告知DIAMETER链路的另一端。数据来源：与对端协商。配置原则：RCP系统默认生成的支持计费应用编号为0。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
SPINDEX|特殊能力索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|参数作用：该参数为Diameter链路关联的特殊能力的索引。数据来源：与对端协商。配置原则：同一个链路号的十条Diameter链路特殊能力需要配置不同的特殊能力索引。
VENDOR1|厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR2|厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR3|厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR4|厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR5|厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR6|厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR7|厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR8|厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR9|厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR10|厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP(Vendor-Id AVP)。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
AUTHAPP|支持鉴权应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Auth-Application-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的认证、授权告知Diameter链路的另一端。数据来源：与对端协商。配置原则：常用鉴权应用标识：16777231：SP接口。16777232：Sp'接口。16777236：Rx接口。16777238：Gx接口。16777302：Sy接口。16777303：Sd接口。
ACCTAPP|支持计费应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Acct-Application-Id AVP）。本端DIAMETER模块与对等端进行能力交换，将本端支持的计费应用告知DIAMETER链路的另一端。数据来源：与对端协商。配置原则：RCP系统默认生成的支持计费应用编号为0。
命令举例 : 
修改链路号为1，特殊能力索引号为1，厂商ID为10415，鉴权应用ID为16777238链路特殊能力。 
SET DIM LINKSPECIFIC:LINKNO=1,SPINDEX=1,VENDOR1=10415,AUTHAPP=16777238; 
相关命令 : 
[增加DIAMETER链路特殊能力]
[删除DIAMETER链路特殊能力]
[查询DIAMETER链路特殊能力]
## DEL DIM LINKSPECIFIC 
## DEL DIM LINKSPECIFIC 
命令功能 : 
该命令用于删除Diameter链路特殊能力配置。当RCP网元不支持该Diameter链路配置的厂商ID、认证应用、安全或计费应用特殊能力时，使用该命令进行删除。命令执行成功后，RCP系统将默认为该Diameter链路的该条特殊能力的所有参数值均为0。删除后会影响RCP和对端网元建立的Diameter链路。 
注意事项 : 
链路建立成功后，一般情况下不能删除Diameter链路的特殊能力配置，否则会影响RCP网元和对端建立的Diameter链路状态。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
SPINDEX|特殊能力索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|参数作用：该参数为Diameter链路关联的特殊能力的索引。数据来源：与对端协商。配置原则：同一个链路号的十条Diameter链路特殊能力需要配置不同的特殊能力索引。
命令举例 : 
删除链路号为1，特殊能力索引号为1的特殊能力。 
DEL DIM LINKSPECIFIC:LINKNO=1,SPINDEX=1; 
相关命令 : 
[增加DIAMETER链路特殊能力]
[修改DIAMETER链路特殊能力]
[查询DIAMETER链路特殊能力]
## SHOW DIM LINKSPECIFIC 
## SHOW DIM LINKSPECIFIC 
命令功能 : 
该命令用于查询Diameter链路特殊能力配置。 
当需要查看已经配置的Diameter链路特殊能力配置时，使用该命令进行查询。查询成功后，可显示该Diameter链路的厂商ID、支持鉴权应用编号、支持计费应用编号。 
注意事项 : 
不输入参数默认查询所有配置。输入链路号和特殊能力索引，查询指定链路号和特殊能力索引的配置。仅输入链路号，查询该链路号的所有Diameter链路特殊能力配置。仅输入特殊能力索引，查询该特殊能力索引的所有Diameter链路特殊能力配置。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
SPINDEX|特殊能力索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|参数作用：该参数为Diameter链路关联的特殊能力的索引。数据来源：与对端协商。配置原则：同一个链路号的十条Diameter链路特殊能力需要配置不同的特殊能力索引。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LINKNO|链路号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于指定与对端网元对接的Diameter信令链路编号。数据来源：本端规划。配置原则：该参数引用SHOW DIM RCPLINK查询结果的链路号LINKNO。
SPINDEX|特殊能力索引|参数可选性:任选参数；参数类型:整数；参数范围为:1~10。|参数作用：该参数为Diameter链路关联的特殊能力的索引。数据来源：与对端协商。配置原则：同一个链路号的十条Diameter链路特殊能力需要配置不同的特殊能力索引。
VENDOR1|厂商ID1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID1为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR2|厂商ID2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID2为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR3|厂商ID3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID3为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR4|厂商ID4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID4为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR5|厂商ID5|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID5为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR6|厂商ID6|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID6为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR7|厂商ID7|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID7为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR8|厂商ID8|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID8为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR9|厂商ID9|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID9为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
VENDOR10|厂商ID10|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Vendor-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的厂商标识告知Diameter链路的另一端。数据来源：与对端协商。配置原则：同一Diameter链路引用的10个厂商ID不能重复。RCP系统默认生成的厂商ID10为0，0为无效值不下发。配置为协议所规定的厂商ID号，常用的有：3902：ZTE10415：3GPP
AUTHAPP|支持鉴权应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Auth-Application-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的认证、授权告知Diameter链路的另一端。数据来源：与对端协商。配置原则：常用鉴权应用标识：16777231：SP接口。16777232：Sp'接口。16777236：Rx接口。16777238：Gx接口。16777302：Sy接口。16777303：Sd接口。
ACCTAPP|支持计费应用编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|参数作用：该参数用于填写Vendor-Specific-Application-Id AVP的子AVP（Acct-Application-Id AVP）。本端Diameter模块与对等端进行能力交换，将本端支持的计费应用告知Diameter链路的另一端。数据来源：与对端协商。配置原则：RCP系统默认生成的支持计费应用编号为0。
命令举例 : 
查询链路号为1，特殊能力索引号为1的特殊能力命令。 
`
命令 (No.1): SHOW DIM LINKSPECIFIC:LINKNO=1,SPINDEX=1;
操作维护         链路号   特殊能力索引   厂商ID1      厂商ID2      厂商ID3      厂商ID4      厂商ID5      厂商ID6      厂商ID7      厂商ID8      厂商ID9      厂商ID10     支持鉴权应用编号   支持计费应用编号
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1        1              10415        0            0            0            0            0            0            0            0            0            16777231           0
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.032 秒）。
` 
相关命令 : 
[增加DIAMETER链路特殊能力]
[修改DIAMETER链路特殊能力]
[删除DIAMETER链路特殊能力]
# DIAMETER 路由配置 
# DIAMETER 路由配置 
背景知识 : 
DIAMETER协议是用于认证、授权、计费的协议，主要应用于IP多媒体子系统、演进的分组核心网等系统。 
DIAMETER对等端是指一个DIAMETER节点，该节点和另一个特定的DIAMETER节点间有一个直接的传输连接。 
功能描述 : 
DIAMETER路由功能是对本网元发送的DIAMETER消息或者从上一跳对等端接收到的DIAMETER消息进行分析，决定按以下哪种方式处理该消息： 
 
针对本网元发送的请求消息进行路由分析，决定本地动作及下一跳选路。 
 
针对本网元从上一跳对端接收的请求消息进行路由分析，决定本地动作以及下一跳选路。 
 
DIAMETER路由配置用于配置一条DIAMETER路由。当本端DIAMETER模块需要发送RCP网元的DIAMETER消息，或者发送从上一跳对等端接收到的DIAMETER消息时，需要配置DIAMETER路由。如果不配置，RCP发送的DIAMETER消息或者从上一跳对等端接收到的DIAMETER消息将无法发送到对端网元。 
## ADD DIM ROUTE 
## ADD DIM ROUTE 
命令功能 : 
该命令用于增加DIAMETER路由。当本网元需要发送DIAMETER消息或者从上一跳对等端接收到DIAMETER消息时，执行该命令增加新的DIAMETER路由。配置成功后，按照配置要求，本端DIAMETER模块进行路由分析，决定本地动作及下一跳选路。 
注意事项 : 
支持应用、目的URI、本地动作、链路号、路由优先级为一条链路的五元组。这五项完全相同的路由只能配置一条。 
配置DIAMETER路由之前，需要先使用[增加DIAMETER链路]命令配置DIAMETER链路。
如果需要配置组号，则在配置DIAMETER路由之前，需要先使用[增加DIAMETER路由组属性]命令配置该DIAMETER路由所属的路由组号以及组属性。需要明确，新增路由组属性是否为主备模式。当为主备模式时，本条DIAMETER路由由该命令的“路由主用标识”参数决定为主用还是备用。
如果需要增加附加条件，则在配置DIAMETER路由之前，需要先使用[增加DIAMETER路由条件]配置DIAMETER路由条件。当路由组编号为0时，此路由不归属于任一路由组，多条路由即使支持应用、目的URI、优先级都一致也无法在多路由中实现负荷分担。
系统最多支持配置的DIAMETER路由条数和系统根据DIAMETER链路自动生成的DIAMETER路由条数的总数，最大为[修改DIAMETER协议基本配置]命令配置的支持的最大路由数。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ROUTENO|路由编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~32767。|参数作用：该参数用于唯一标识一条DIAMETER路由。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALPROCESSID|本地动作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:RELAY。|参数作用：当DIAMETER模块收到DIAMETER消息，判断为本网元发出的DIAMETER消息或者是来自上一跳对等端的DIAMETER消息时，通过该参数来确定此消息的处理方式。数据来源：本端规划。配置原则：具体处理方式支持一种：RELAY。DIAMETER消息直接发往下一跳的服务器，且不修改消息中任何与路由无关的属性。
MASTERLINKNO|主用链路|参数可选性:必选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于指定信令路由关联的信令链路的编号。数据来源：本端规划。配置原则：该参数引用“新增DIAMETER信令链路”的信令链路编号LINKNO，参见查询DIAMETER链路。
ROUTEPRIORITY|路由优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:LOW。|参数作用：该参数用于指定路由的优先级，当存在多条路由时，将依据优先级从高到低进行选路。数据来源：本端规划。配置原则：可配置的优先级有以下三种：低（LOW）：此路由优先级低。中（MID）：此路由优先级高于低优先级路由，低于高优先级路由。高（HIGH）：此路由优先级高。
ROUTEAPPID|支持应用|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定该DIAMETER路由支持的应用。数据来源：本端规划。配置原则：可选的应用有以下7种：COMMON：Diameter在线计费协议/离线计费协议。E4/Sp：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的签约消息的交互。Sp'：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的用量消息的交互。RX：用于RCP和AF（Application Function，应用服务）的消息交互。Gx：用于RCP和PCEF（Policy and Charging Enforcement Function，策略与计费执行功能）的消息交互。Sy：用于RCP和OCS（Online Charging System，在线计费系统）的消息交互。Sd：用于RCP和TDF（Traffic Detection Function）的消息交互。
DESTURI|目的URI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：该参数配置DIAMETER路由的目的URI。该参数为本路由的关键字。本端DIMAETER模块进行路由分析时，获取码流中Destination-Host AVP（若没有，则取Destination-Realm AVP）的内容，根据目的URI操作属性确定的匹配方式，与该参数进行匹配。如果二者匹配，则选用本路由，否则不能使用本路由。数据来源：本端规划。配置原则：要求目的URI必须符合FQDN格式要求。
DESTURIOPTYPE|目的URI操作属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:LMFR。|参数作用：该参数用于明确目的URI与码流中的Destination-Host AVP（或Destination-Realm AVP）内容以哪种方式进行匹配。数据来源：本端规划。配置原则：可选的目的URI操作属性有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从右到左包含了该参数配置的目的URI的全部字符，当与多个配置目的URI相匹配的时候，选择配置目的URI最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的目的URI完全相同。一般选择从右往左最长匹配。也可根据实际需求选择全匹配。
SPECFLAG|特殊属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:COMM。|参数作用：该参数用于标识该DIAMETER路由是否优先处理，以及条件满足但处理失败后的处理方式。数据来源：本端规划。配置原则：有以下三种属性：普通路由（COMM）。普通路由主要和下面两种路由选择方式区分开，一般情况下都配成普通路由。优先比较本路由，条件满足，链路不通时失败（RETURN）。链路不通时失败指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，不进行继续分析以获取其它路由。优先比较本路由，条件满足，链路不通时继续（CONTINUE）。链路不通时继续指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，进行继续分析以获取其它路由。
ROUTEGROUPNO|路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|参数作用：该参数用于标识该DIAMETER路由归属于哪个路由组。数据来源：本端规划。配置原则：如果不归属于任何路由组，配置为0。或者直接使用默认配置。如果归属于某路由组，则路由组编号需要通过 增加DIAMETER路由组属性命令在DIAMETER路由组属性配置中提前配置。
MASTERFLAG|路由主用标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:MASTER。|参数作用：该参数用于指示该DIAMETER路由为主用路由还是备用路由。数据来源：本端规划。配置原则：只有路由组编号为非0的有效值，且该路由组的路由组属性配置为“主备模式”时，本配置才有效。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。该参数的选项有以下两种：主用（MASTER）：在一个路由组中此路由可用时，将被优先使用。备用（SLAVE）：在一个路由组中仅当所有主用路由不可用时，使用此路由。
OTHCONDNO1|附加条件1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|参数作用：本参数用于增加附加条件1，当根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中已配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO2|附加条件2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|参数作用：本参数用于增加附加条件2，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO3|附加条件3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|参数作用：本参数用于增加附加条件3，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO4|附加条件4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|参数作用：本参数用于增加附加条件4，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
PEERHOSTNAME|动态对等端主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~127个字符。|参数作用：该参数用于指示该DIAMETER路由使用动态链路时，需要的动态对等端主机名。数据来源：本端规划。配置原则：该动态对等端主机名是和RCP网元建立动态链路的对等端主机名。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~9。默认值:0。|参数作用：该参数用于指示该DIAMETER路由所占的权重。只有路由组编号有效，组内有多条路由，且路由组属性为负荷分担的情况下，才使用该参数。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。本端DIAMETER模块在选路时，当权重大于0，则继续使用该路由；否则，使用该路由组的下一条路由。数据来源：本端规划。配置原则：权重值为0时，表示路由为轮选。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ROUTENO|路由编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32767。|参数作用：该参数用于唯一标识一条DIAMETER路由。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALPROCESSID|本地动作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：当DIAMETER模块收到DIAMETER消息，判断为本网元发出的DIAMETER消息或者是来自上一跳对等端的DIAMETER消息时，通过该参数来确定此消息的处理方式。数据来源：本端规划。配置原则：具体处理方式支持一种：RELAY。DIAMETER消息直接发往下一跳的服务器，且不修改消息中任何与路由无关的属性。
MASTERLINKNO|主用链路|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于指定信令路由关联的信令链路的编号。数据来源：本端规划。配置原则：该参数引用“新增DIAMETER信令链路”的信令链路编号LINKNO，参见查询DIAMETER链路。
ROUTEPRIORITY|路由优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定路由的优先级，当存在多条路由时，将依据优先级从高到低进行选路。数据来源：本端规划。配置原则：可配置的优先级有以下三种：低（LOW）：此路由优先级低。中（MID）：此路由优先级高于低优先级路由，低于高优先级路由。高（HIGH）：此路由优先级高。
ROUTEAPPID|支持应用|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定该DIAMETER路由支持的应用。数据来源：本端规划。配置原则：可选的应用有以下7种：COMMON：Diameter在线计费协议/离线计费协议。E4/Sp：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的签约消息的交互。Sp'：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的用量消息的交互。RX：用于RCP和AF（Application Function，应用服务）的消息交互。Gx：用于RCP和PCEF（Policy and Charging Enforcement Function，策略与计费执行功能）的消息交互。Sy：用于RCP和OCS（Online Charging System，在线计费系统）的消息交互。Sd：用于RCP和TDF（Traffic Detection Function）的消息交互。
DESTURI|目的URI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：该参数配置DIAMETER路由的目的URI。该参数为本路由的关键字。本端DIMAETER模块进行路由分析时，获取码流中Destination-Host AVP（若没有，则取Destination-Realm AVP）的内容，根据目的URI操作属性确定的匹配方式，与该参数进行匹配。如果二者匹配，则选用本路由，否则不能使用本路由。数据来源：本端规划。配置原则：要求目的URI必须符合FQDN格式要求。
DESTURIOPTYPE|目的URI操作属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于明确目的URI与码流中的Destination-Host AVP（或Destination-Realm AVP）内容以哪种方式进行匹配。数据来源：本端规划。配置原则：可选的目的URI操作属性有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从右到左包含了该参数配置的目的URI的全部字符，当与多个配置目的URI相匹配的时候，选择配置目的URI最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的目的URI完全相同。一般选择从右往左最长匹配。也可根据实际需求选择全匹配。
SPECFLAG|特殊属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于标识该DIAMETER路由是否优先处理，以及条件满足但处理失败后的处理方式。数据来源：本端规划。配置原则：有以下三种属性：普通路由（COMM）。普通路由主要和下面两种路由选择方式区分开，一般情况下都配成普通路由。优先比较本路由，条件满足，链路不通时失败（RETURN）。链路不通时失败指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，不进行继续分析以获取其它路由。优先比较本路由，条件满足，链路不通时继续（CONTINUE）。链路不通时继续指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，进行继续分析以获取其它路由。
ROUTEGROUPNO|路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于标识该DIAMETER路由归属于哪个路由组。数据来源：本端规划。配置原则：如果不归属于任何路由组，配置为0。或者直接使用默认配置。如果归属于某路由组，则路由组编号需要通过 增加DIAMETER路由组属性命令在DIAMETER路由组属性配置中提前配置。
MASTERFLAG|路由主用标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指示该DIAMETER路由为主用路由还是备用路由。数据来源：本端规划。配置原则：只有路由组编号为非0的有效值，且该路由组的路由组属性配置为“主备模式”时，本配置才有效。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。该参数的选项有以下两种：主用（MASTER）：在一个路由组中此路由可用时，将被优先使用。备用（SLAVE）：在一个路由组中仅当所有主用路由不可用时，使用此路由。
OTHCONDNO1|附加条件1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件1，当根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中已配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO2|附加条件2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件2，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO3|附加条件3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件3，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO4|附加条件4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件4，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
PEERHOSTNAME|动态对等端主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~127个字符。|参数作用：该参数用于指示该DIAMETER路由使用动态链路时，需要的动态对等端主机名。数据来源：本端规划。配置原则：该动态对等端主机名是和RCP网元建立动态链路的对等端主机名。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~9。|参数作用：该参数用于指示该DIAMETER路由所占的权重。只有路由组编号有效，组内有多条路由，且路由组属性为负荷分担的情况下，才使用该参数。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。本端DIAMETER模块在选路时，当权重大于0，则继续使用该路由；否则，使用该路由组的下一条路由。数据来源：本端规划。配置原则：权重值为0时，表示路由为轮选。
命令举例 : 
增加DIAMETER路由：路由编号为1，本地动作为中继处理（RELAY），链路号为1，路由优先级为高（HIGH），支持应用为Gx，目的URI为rcp.zte.com.cn，路由组编号为1，动态对等端主机名为1，权重为1。 
ADD DIM ROUTE:ROUTENO=1,LOCALPROCESSID="RELAY",MASTERLINKNO=1,ROUTEPRIORITY="HIGH",ROUTEAPPID="Gx",DESTURI="rcp.zte.com.cn",ROUTEGROUPNO=1,PEERHOSTNAME="1",WEIGHT=1; 
相关命令 : 
[修改DIAMETER路由]
[删除DIAMETER路由]
[查询DIAMETER路由]
## SET DIM ROUTE 
## SET DIM ROUTE 
命令功能 : 
该命令用于修改DIAMETER路由。当本网元需要发送DIAMETER消息或者从上一跳对等端接收到DIAMETER消息，需要修改已有的DIAMETER路由时，使用该命令。修改路由后，可能会影响原有RCP网元的DIAMETER消息发送。 
注意事项 : 
一般情况下，不能修改DIAMETER路由配置，否则会影响RCP发送的DIAMETER消息或从上一跳对等端接收到的DIAMETER消息的发送。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ROUTENO|路由编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~32767。|参数作用：该参数用于唯一标识一条DIAMETER路由。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALPROCESSID|本地动作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：当DIAMETER模块收到DIAMETER消息，判断为本网元发出的DIAMETER消息或者是来自上一跳对等端的DIAMETER消息时，通过该参数来确定此消息的处理方式。数据来源：本端规划。配置原则：具体处理方式支持一种：RELAY。DIAMETER消息直接发往下一跳的服务器，且不修改消息中任何与路由无关的属性。
MASTERLINKNO|主用链路|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于指定信令路由关联的信令链路的编号。数据来源：本端规划。配置原则：该参数引用“新增DIAMETER信令链路”的信令链路编号LINKNO，参见查询DIAMETER链路。
ROUTEPRIORITY|路由优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定路由的优先级，当存在多条路由时，将依据优先级从高到低进行选路。数据来源：本端规划。配置原则：可配置的优先级有以下三种：低（LOW）：此路由优先级低。中（MID）：此路由优先级高于低优先级路由，低于高优先级路由。高（HIGH）：此路由优先级高。
ROUTEAPPID|支持应用|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定该DIAMETER路由支持的应用。数据来源：本端规划。配置原则：可选的应用有以下7种：COMMON：Diameter在线计费协议/离线计费协议。E4/Sp：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的签约消息的交互。Sp'：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的用量消息的交互。RX：用于RCP和AF（Application Function，应用服务）的消息交互。Gx：用于RCP和PCEF（Policy and Charging Enforcement Function，策略与计费执行功能）的消息交互。Sy：用于RCP和OCS（Online Charging System，在线计费系统）的消息交互。Sd：用于RCP和TDF（Traffic Detection Function）的消息交互。
DESTURI|目的URI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：该参数配置DIAMETER路由的目的URI。该参数为本路由的关键字。本端DIMAETER模块进行路由分析时，获取码流中Destination-Host AVP（若没有，则取Destination-Realm AVP）的内容，根据目的URI操作属性确定的匹配方式，与该参数进行匹配。如果二者匹配，则选用本路由，否则不能使用本路由。数据来源：本端规划。配置原则：要求目的URI必须符合FQDN格式要求。
DESTURIOPTYPE|目的URI操作属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于明确目的URI与码流中的Destination-Host AVP（或Destination-Realm AVP）内容以哪种方式进行匹配。数据来源：本端规划。配置原则：可选的目的URI操作属性有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从右到左包含了该参数配置的目的URI的全部字符，当与多个配置目的URI相匹配的时候，选择配置目的URI最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的目的URI完全相同。一般选择从右往左最长匹配。也可根据实际需求选择全匹配。
SPECFLAG|特殊属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于标识该DIAMETER路由是否优先处理，以及条件满足但处理失败后的处理方式。数据来源：本端规划。配置原则：有以下三种属性：普通路由（COMM）。普通路由主要和下面两种路由选择方式区分开，一般情况下都配成普通路由。优先比较本路由，条件满足，链路不通时失败（RETURN）。链路不通时失败指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，不进行继续分析以获取其它路由。优先比较本路由，条件满足，链路不通时继续（CONTINUE）。链路不通时继续指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，进行继续分析以获取其它路由。
ROUTEGROUPNO|路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于标识该DIAMETER路由归属于哪个路由组。数据来源：本端规划。配置原则：如果不归属于任何路由组，配置为0。或者直接使用默认配置。如果归属于某路由组，则路由组编号需要通过 增加DIAMETER路由组属性命令在DIAMETER路由组属性配置中提前配置。
MASTERFLAG|路由主用标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指示该DIAMETER路由为主用路由还是备用路由。数据来源：本端规划。配置原则：只有路由组编号为非0的有效值，且该路由组的路由组属性配置为“主备模式”时，本配置才有效。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。该参数的选项有以下两种：主用（MASTER）：在一个路由组中此路由可用时，将被优先使用。备用（SLAVE）：在一个路由组中仅当所有主用路由不可用时，使用此路由。
OTHCONDNO1|附加条件1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件1，当根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中已配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO2|附加条件2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件2，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO3|附加条件3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件3，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO4|附加条件4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件4，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
PEERHOSTNAME|动态对等端主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~127个字符。|参数作用：该参数用于指示该DIAMETER路由使用动态链路时，需要的动态对等端主机名。数据来源：本端规划。配置原则：该动态对等端主机名是和RCP网元建立动态链路的对等端主机名。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~9。|参数作用：该参数用于指示该DIAMETER路由所占的权重。只有路由组编号有效，组内有多条路由，且路由组属性为负荷分担的情况下，才使用该参数。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。本端DIAMETER模块在选路时，当权重大于0，则继续使用该路由；否则，使用该路由组的下一条路由。数据来源：本端规划。配置原则：权重值为0时，表示路由为轮选。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ROUTENO|路由编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32767。|参数作用：该参数用于唯一标识一条DIAMETER路由。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALPROCESSID|本地动作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：当DIAMETER模块收到DIAMETER消息，判断为本网元发出的DIAMETER消息或者是来自上一跳对等端的DIAMETER消息时，通过该参数来确定此消息的处理方式。数据来源：本端规划。配置原则：具体处理方式支持一种：RELAY。DIAMETER消息直接发往下一跳的服务器，且不修改消息中任何与路由无关的属性。
MASTERLINKNO|主用链路|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于指定信令路由关联的信令链路的编号。数据来源：本端规划。配置原则：该参数引用“新增DIAMETER信令链路”的信令链路编号LINKNO，参见查询DIAMETER链路。
ROUTEPRIORITY|路由优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定路由的优先级，当存在多条路由时，将依据优先级从高到低进行选路。数据来源：本端规划。配置原则：可配置的优先级有以下三种：低（LOW）：此路由优先级低。中（MID）：此路由优先级高于低优先级路由，低于高优先级路由。高（HIGH）：此路由优先级高。
ROUTEAPPID|支持应用|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定该DIAMETER路由支持的应用。数据来源：本端规划。配置原则：可选的应用有以下7种：COMMON：Diameter在线计费协议/离线计费协议。E4/Sp：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的签约消息的交互。Sp'：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的用量消息的交互。RX：用于RCP和AF（Application Function，应用服务）的消息交互。Gx：用于RCP和PCEF（Policy and Charging Enforcement Function，策略与计费执行功能）的消息交互。Sy：用于RCP和OCS（Online Charging System，在线计费系统）的消息交互。Sd：用于RCP和TDF（Traffic Detection Function）的消息交互。
DESTURI|目的URI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：该参数配置DIAMETER路由的目的URI。该参数为本路由的关键字。本端DIMAETER模块进行路由分析时，获取码流中Destination-Host AVP（若没有，则取Destination-Realm AVP）的内容，根据目的URI操作属性确定的匹配方式，与该参数进行匹配。如果二者匹配，则选用本路由，否则不能使用本路由。数据来源：本端规划。配置原则：要求目的URI必须符合FQDN格式要求。
DESTURIOPTYPE|目的URI操作属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于明确目的URI与码流中的Destination-Host AVP（或Destination-Realm AVP）内容以哪种方式进行匹配。数据来源：本端规划。配置原则：可选的目的URI操作属性有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从右到左包含了该参数配置的目的URI的全部字符，当与多个配置目的URI相匹配的时候，选择配置目的URI最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的目的URI完全相同。一般选择从右往左最长匹配。也可根据实际需求选择全匹配。
SPECFLAG|特殊属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于标识该DIAMETER路由是否优先处理，以及条件满足但处理失败后的处理方式。数据来源：本端规划。配置原则：有以下三种属性：普通路由（COMM）。普通路由主要和下面两种路由选择方式区分开，一般情况下都配成普通路由。优先比较本路由，条件满足，链路不通时失败（RETURN）。链路不通时失败指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，不进行继续分析以获取其它路由。优先比较本路由，条件满足，链路不通时继续（CONTINUE）。链路不通时继续指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，进行继续分析以获取其它路由。
ROUTEGROUPNO|路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于标识该DIAMETER路由归属于哪个路由组。数据来源：本端规划。配置原则：如果不归属于任何路由组，配置为0。或者直接使用默认配置。如果归属于某路由组，则路由组编号需要通过 增加DIAMETER路由组属性命令在DIAMETER路由组属性配置中提前配置。
MASTERFLAG|路由主用标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指示该DIAMETER路由为主用路由还是备用路由。数据来源：本端规划。配置原则：只有路由组编号为非0的有效值，且该路由组的路由组属性配置为“主备模式”时，本配置才有效。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。该参数的选项有以下两种：主用（MASTER）：在一个路由组中此路由可用时，将被优先使用。备用（SLAVE）：在一个路由组中仅当所有主用路由不可用时，使用此路由。
OTHCONDNO1|附加条件1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件1，当根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中已配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO2|附加条件2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件2，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO3|附加条件3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件3，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO4|附加条件4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件4，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
PEERHOSTNAME|动态对等端主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~127个字符。|参数作用：该参数用于指示该DIAMETER路由使用动态链路时，需要的动态对等端主机名。数据来源：本端规划。配置原则：该动态对等端主机名是和RCP网元建立动态链路的对等端主机名。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~9。|参数作用：该参数用于指示该DIAMETER路由所占的权重。只有路由组编号有效，组内有多条路由，且路由组属性为负荷分担的情况下，才使用该参数。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。本端DIAMETER模块在选路时，当权重大于0，则继续使用该路由；否则，使用该路由组的下一条路由。数据来源：本端规划。配置原则：权重值为0时，表示路由为轮选。
命令举例 : 
修改DIAMETER路由：路由编号为1，主用链路为1，支持应用为Gx，目的URI为：rcp.zte.com.cn，路由组编号为1，对端主机名为1，权重为1。 
SET DIM ROUTE:ROUTENO=1,MASTERLINKNO=1,ROUTEPRIORITY="HIGH",ROUTEAPPID="Gx",DESTURI="rcp.zte.com.cn",ROUTEGROUPNO=1,PEERHOSTNAME="1",WEIGHT=1; 
相关命令 : 
[增加DIAMETER路由]
[删除DIAMETER路由]
[查询DIAMETER路由]
## DEL DIM ROUTE 
## DEL DIM ROUTE 
命令功能 : 
该命令用于删除DIAMETER路由。当不再使用该DIAMETER路由时，使用该命令。删除路由后，有可能造成无法发送DIAMETER消息。 
注意事项 : 
一般情况下，不能删除DIAMETER路由配置，否则会使RCP网元发送的DIAMETER消息或从上一跳对等端接收到的DIAMETER消息无法发送。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ROUTENO|路由编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~32767。|参数作用：该参数用于唯一标识一条DIAMETER路由。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
命令举例 : 
删除DIAMETER路由：路由编号为1。 
DEL DIM ROUTE:ROUTENO=1; 
相关命令 : 
[增加DIAMETER路由]
[修改DIAMETER路由]
[查询DIAMETER路由]
## SHOW DIM ROUTE 
## SHOW DIM ROUTE 
命令功能 : 
该命令用于查询DIAMETER路由。通过该命令，可以获取路由编号、本地动作、支持的应用、路由优先级等信息。 
注意事项 : 
 
不输入参数默认查询所有配置。
 
 
输入起始分析编号和结束分析编号，查询指定编号范围内的所有配置。
 
 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始路由编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32767。|参数作用：该参数用于查询时标识一条DIAMETER路由的起始编号。数据来源：本端规划。配置原则：编号在允许取值范围内即可，需要小于等于结束路由编号。
END|结束路由编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32767。|参数作用：该参数用于查询时标识一条DIAMETER路由的结束编号。数据来源：本端规划。配置原则：编号在允许取值范围内即可，需要大于等于起始路由编号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ROUTENO|路由编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~32767。|参数作用：该参数用于唯一标识一条DIAMETER路由。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
LOCALPROCESSID|本地动作|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：当DIAMETER模块收到DIAMETER消息，判断为本网元发出的DIAMETER消息或者是来自上一跳对等端的DIAMETER消息时，通过该参数来确定此消息的处理方式。数据来源：本端规划。配置原则：具体处理方式支持一种：RELAY。DIAMETER消息直接发往下一跳的服务器，且不修改消息中任何与路由无关的属性。
MASTERLINKNO|主用链路|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于指定信令路由关联的信令链路的编号。数据来源：本端规划。配置原则：该参数引用“新增DIAMETER信令链路”的信令链路编号LINKNO，参见查询DIAMETER链路。
ROUTEPRIORITY|路由优先级|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定路由的优先级，当存在多条路由时，将依据优先级从高到低进行选路。数据来源：本端规划。配置原则：可配置的优先级有以下三种：低（LOW）：此路由优先级低。中（MID）：此路由优先级高于低优先级路由，低于高优先级路由。高（HIGH）：此路由优先级高。
ROUTEAPPID|支持应用|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定该DIAMETER路由支持的应用。数据来源：本端规划。配置原则：可选的应用有以下7种：COMMON：Diameter在线计费协议/离线计费协议。E4/Sp：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的签约消息的交互。Sp'：用于RCP和SPR（Subsciption Profile Repository，用户签约服务）的用量消息的交互。RX：用于RCP和AF（Application Function，应用服务）的消息交互。Gx：用于RCP和PCEF（Policy and Charging Enforcement Function，策略与计费执行功能）的消息交互。Sy：用于RCP和OCS（Online Charging System，在线计费系统）的消息交互。Sd：用于RCP和TDF（Traffic Detection Function）的消息交互。
DESTURI|目的URI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|参数作用：该参数配置DIAMETER路由的目的URI。该参数为本路由的关键字。本端DIMAETER模块进行路由分析时，获取码流中Destination-Host AVP（若没有，则取Destination-Realm AVP）的内容，根据目的URI操作属性确定的匹配方式，与该参数进行匹配。如果二者匹配，则选用本路由，否则不能使用本路由。数据来源：本端规划。配置原则：要求目的URI必须符合FQDN格式要求。
DESTURIOPTYPE|目的URI操作属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于明确目的URI与码流中的Destination-Host AVP（或Destination-Realm AVP）内容以哪种方式进行匹配。数据来源：本端规划。配置原则：可选的目的URI操作属性有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从右到左包含了该参数配置的目的URI的全部字符，当与多个配置目的URI相匹配的时候，选择配置目的URI最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的目的URI完全相同。一般选择从右往左最长匹配。也可根据实际需求选择全匹配。
SPECFLAG|特殊属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于标识该DIAMETER路由是否优先处理，以及条件满足但处理失败后的处理方式。数据来源：本端规划。配置原则：有以下三种属性：普通路由（COMM）。普通路由主要和下面两种路由选择方式区分开，一般情况下都配成普通路由。优先比较本路由，条件满足，链路不通时失败（RETURN）。链路不通时失败指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，不进行继续分析以获取其它路由。优先比较本路由，条件满足，链路不通时继续（CONTINUE）。链路不通时继续指本端DIAMETER模块分析出来的路由，如果该路由的链路不通，进行继续分析以获取其它路由。
ROUTEGROUPNO|路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：该参数用于标识该DIAMETER路由归属于哪个路由组。数据来源：本端规划。配置原则：如果不归属于任何路由组，配置为0。或者直接使用默认配置。如果归属于某路由组，则路由组编号需要通过 增加DIAMETER路由组属性命令在DIAMETER路由组属性配置中提前配置。
MASTERFLAG|路由主用标识|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指示该DIAMETER路由为主用路由还是备用路由。数据来源：本端规划。配置原则：只有路由组编号为非0的有效值，且该路由组的路由组属性配置为“主备模式”时，本配置才有效。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。该参数的选项有以下两种：主用（MASTER）：在一个路由组中此路由可用时，将被优先使用。备用（SLAVE）：在一个路由组中仅当所有主用路由不可用时，使用此路由。
OTHCONDNO1|附加条件1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件1，当根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中已配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO2|附加条件2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件2，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO3|附加条件3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件3，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
OTHCONDNO4|附加条件4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|参数作用：本参数用于增加附加条件4，根据该DIAMETER路由的其他配置已经匹配到本条路由时，再使用附加条件继续判断是否使用该DIAMETER路由。数据来源：本端规划。配置原则：引用增加DIAMETER路由条件命令中配置的条件编号，目前只支持源主机名匹配。只支持匹配一条源主机名。默认值为0，表示无附加条件编号。
PEERHOSTNAME|动态对等端主机名|参数可选性:任选参数；参数类型:字符型；参数范围为:0~127个字符。|参数作用：该参数用于指示该DIAMETER路由使用动态链路时，需要的动态对等端主机名。数据来源：本端规划。配置原则：该动态对等端主机名是和RCP网元建立动态链路的对等端主机名。
WEIGHT|权重|参数可选性:任选参数；参数类型:整数；参数范围为:0~9。|参数作用：该参数用于指示该DIAMETER路由所占的权重。只有路由组编号有效，组内有多条路由，且路由组属性为负荷分担的情况下，才使用该参数。执行查询DIAMETER路由组属性命令，可以查询该路由组的“路由组属性”参数配置值。本端DIAMETER模块在选路时，当权重大于0，则继续使用该路由；否则，使用该路由组的下一条路由。数据来源：本端规划。配置原则：权重值为0时，表示路由为轮选。
命令举例 : 
查询DIAMETER路由编号为1。 
SHOW DIM ROUTE:BEGIN=1,END=1; 
`
命令 (No.1): SHOW DIM ROUTE:BEGIN=1,END=1;
操作维护         路由编号   本地动作   主用链路   路由优先级   支持应用   目的URI               目的URI操作属性    特殊属性                                   路由组编号   路由主用标识   附加条件1   附加条件2   附加条件3   附加条件4   动态对等端主机名   权重
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
复制 修改 删除   1          本地处理   1          低           Gx         rcp.hatt.zte.com.cn   从右往左最长匹配   普通路由                                   0            主用           0           0           0           0                              0
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.059 秒）。
` 
相关命令 : 
[增加DIAMETER路由]
[修改DIAMETER路由]
[删除DIAMETER路由]
# DIAMETER 路由条件配置 
# DIAMETER 路由条件配置 
背景知识 : 
路由条件配置是DIAMETER路由配置（[增加DIAMETER路由]命令）的附加条件。通过配置附加条件，以满足仅通过现有DIAMETER路由配置无法选路的情况。
DIAMETER路由是指对本网元发送的DIAMETER消息或者从上一跳对等端接收到的DIAMETER消息进行分析，决定按以下哪种方式处理该消息。 
 
针对本网元发送的请求消息进行路由分析，决定本地动作及下一跳选路。 
 
针对本网元从上一跳对端接收的请求消息进行路由分析，决定本地动作以及下一跳选路。 
 
功能描述 : 
该功能用于配置DIAMETER路由条件。当本网元使用现有DIAMETER路由配置来选路，但无法满足要求时，需要配置并关联此处配置的DIAMETER路由条件配置。 
目前，DIAMETER路由条件配置只支持源主机名的匹配。当需要通过源主机名的匹配来选择DIAMETER路由时，可通过该命令实现。 
一般情况下，不需要配置DIAMETER路由条件。 
## ADD DIM ROUTECOND 
## ADD DIM ROUTECOND 
命令功能 : 
该命令用于增加DIAMETER路由条件。当本网元使用现有DIAMETER路由配置来选路，但无法满足要求时，可以使用该命令增加新的DIAMETER路由条件。配置成功后，在DIAMETER路由配置（[增加DIAMETER路由]命令）的附加条件中可以关联该DIAMETER路由条件，作为本网元选择DIAMETER路由的条件之一。
注意事项 : 
目前，DIAMETER路由条件配置只支持条件类型为源主机名（LOCAL）的配置。当DIAMETER路由配置（[增加DIAMETER路由]命令）的附加条件为多个时，系统一旦成功获取一个源主机名，便不再匹配其他的附加条件。
该命令需要在DIAMETER路由配置的附加条件中关联，才会生效。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
CONDNO|条件编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由条件配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
CONDNAME|条件名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由条件配置。用户可根据本路由条件配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：不同条件的名称不可重复。
CONDTYPE|条件类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:ORIGIN。|参数作用：该参数用于描述匹配路由的条件类型。数据来源：本端规划。配置原则：目前支持的条件类型为：源主机名（ORIGIN）。
CONDOPTYPE|条件匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:AM。|参数作用：当该DIAMETER路由条件被DIAMETER路由配置（增加DIAMETER路由命令）关联时，该参数用于明确条件值与本网元发送的DIAMETER消息中的Origin-Host AVP内容以哪种方式进行匹配。数据来源：本端规划。配置原则：该参数的选项有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从最右到左包含了配置的条件值的全部字符，当与多个条件值相匹配的时候，选择条件值最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的条件值完全相同。默认为全匹配。
CONDITION|条件值|参数可选性:必选参数；参数类型:字符型；参数范围为:1~255个字符。|参数作用：该参数用于指定用来匹配的数据值。数据来源：本端规划。配置原则：当条件类型为“源主机名（LOCAL）”时，该参数内容为源主机的主机名。例如：条件值为“rcp.zte.com.cn”，条件类型为“源主机名”，条件匹配类型为“全匹配”，那么该条件的实际匹配动作就是：全匹配源主机名为rcp.zte.com.cn的主机。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
CONDNO|条件编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由条件配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
CONDNAME|条件名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由条件配置。用户可根据本路由条件配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：不同条件的名称不可重复。
CONDTYPE|条件类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于描述匹配路由的条件类型。数据来源：本端规划。配置原则：目前支持的条件类型为：源主机名（ORIGIN）。
CONDOPTYPE|条件匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：当该DIAMETER路由条件被DIAMETER路由配置（增加DIAMETER路由命令）关联时，该参数用于明确条件值与本网元发送的DIAMETER消息中的Origin-Host AVP内容以哪种方式进行匹配。数据来源：本端规划。配置原则：该参数的选项有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从最右到左包含了配置的条件值的全部字符，当与多个条件值相匹配的时候，选择条件值最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的条件值完全相同。默认为全匹配。
CONDITION|条件值|参数可选性:任选参数；参数类型:字符型；参数范围为:1~255个字符。|参数作用：该参数用于指定用来匹配的数据值。数据来源：本端规划。配置原则：当条件类型为“源主机名（LOCAL）”时，该参数内容为源主机的主机名。例如：条件值为“rcp.zte.com.cn”，条件类型为“源主机名”，条件匹配类型为“全匹配”，那么该条件的实际匹配动作就是：全匹配源主机名为rcp.zte.com.cn的主机。
命令举例 : 
增加DIAMETER路由条件：条件编号为1，条件名称为1，条件值为"rcp.zte.com.cn",匹配类型为LMFR。 
ADD DIM ROUTECOND:CONDNO=1,CONDNAME="1",CONDOPTYPE="LMFR",CONDITION="rcp.zte.com.cn"; 
相关命令 : 
[修改DIAMETER路由条件]
[删除DIAMETER路由条件]
[查询DIAMETER路由条件]
## SET DIM ROUTECOND 
## SET DIM ROUTECOND 
命令功能 : 
该命令用于修改DIAMETER路由条件。当本网元使用现有DIAMETER路由配置来选路，但无法满足要求时，需要使用该命令修改已有DIAMETER路由条件配置，作为本网元选择DIAMETER路由的条件之一。修改路由条件后，可能会影响原有RCP的DIAMETER消息的发送。 
注意事项 : 
一般情况下，不能修改DIAMETER路由条件配置，否则会影响RCP发送的DIAMETER消息或从上一跳对等端接收到的DIAMETER消息的发送。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
CONDNO|条件编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由条件配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
CONDNAME|条件名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由条件配置。用户可根据本路由条件配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：不同条件的名称不可重复。
CONDTYPE|条件类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于描述匹配路由的条件类型。数据来源：本端规划。配置原则：目前支持的条件类型为：源主机名（ORIGIN）。
CONDOPTYPE|条件匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：当该DIAMETER路由条件被DIAMETER路由配置（增加DIAMETER路由命令）关联时，该参数用于明确条件值与本网元发送的DIAMETER消息中的Origin-Host AVP内容以哪种方式进行匹配。数据来源：本端规划。配置原则：该参数的选项有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从最右到左包含了配置的条件值的全部字符，当与多个条件值相匹配的时候，选择条件值最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的条件值完全相同。默认为全匹配。
CONDITION|条件值|参数可选性:任选参数；参数类型:字符型；参数范围为:1~255个字符。|参数作用：该参数用于指定用来匹配的数据值。数据来源：本端规划。配置原则：当条件类型为“源主机名（LOCAL）”时，该参数内容为源主机的主机名。例如：条件值为“rcp.zte.com.cn”，条件类型为“源主机名”，条件匹配类型为“全匹配”，那么该条件的实际匹配动作就是：全匹配源主机名为rcp.zte.com.cn的主机。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
CONDNO|条件编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由条件配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
CONDNAME|条件名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由条件配置。用户可根据本路由条件配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：不同条件的名称不可重复。
CONDTYPE|条件类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于描述匹配路由的条件类型。数据来源：本端规划。配置原则：目前支持的条件类型为：源主机名（ORIGIN）。
CONDOPTYPE|条件匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：当该DIAMETER路由条件被DIAMETER路由配置（增加DIAMETER路由命令）关联时，该参数用于明确条件值与本网元发送的DIAMETER消息中的Origin-Host AVP内容以哪种方式进行匹配。数据来源：本端规划。配置原则：该参数的选项有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从最右到左包含了配置的条件值的全部字符，当与多个条件值相匹配的时候，选择条件值最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的条件值完全相同。默认为全匹配。
CONDITION|条件值|参数可选性:任选参数；参数类型:字符型；参数范围为:1~255个字符。|参数作用：该参数用于指定用来匹配的数据值。数据来源：本端规划。配置原则：当条件类型为“源主机名（LOCAL）”时，该参数内容为源主机的主机名。例如：条件值为“rcp.zte.com.cn”，条件类型为“源主机名”，条件匹配类型为“全匹配”，那么该条件的实际匹配动作就是：全匹配源主机名为rcp.zte.com.cn的主机。
命令举例 : 
修改DIAMETER路由条件：条件编号为1，条件名称为1，条件值为"rcp.zte.com.cn"，匹配类型为LMFR。 
SET DIM ROUTECOND:CONDNO=1,CONDNAME="1",CONDOPTYPE="LMFR",CONDITION="rcp.zte.com.cn"; 
相关命令 : 
[增加DIAMETER路由条件]
[删除DIAMETER路由条件]
[查询DIAMETER路由条件]
## DEL DIM ROUTECOND 
## DEL DIM ROUTECOND 
命令功能 : 
该命令用于删除DIAMETER路由条件。当不需要使用该附加条件作为路由配置的分析条件，使用该命令。删除后，可能影响原路由的分析结果。 
注意事项 : 
一般情况下，不能删除DIAMETER路由条件配置，否则会使RCP网元发送的DIAMETER消息或从上一跳对等端接收到的DIAMETER消息无法发送。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
CONDNO|条件编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由条件配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
命令举例 : 
删除DIAMETER路由条件：条件编号为1。 
DEL DIM ROUTECOND:CONDNO=1; 
相关命令 : 
[增加DIAMETER路由条件]
[修改DIAMETER路由条件]
[查询DIAMETER路由条件]
## SHOW DIM ROUTECOND 
## SHOW DIM ROUTECOND 
命令功能 : 
该命令用于查询DIAMETER路由条件。当需要查询已有的DIAMETER路由条件配置时，使用该命令。 
注意事项 : 
查询DIAMETER路由条件。 
 
若不输入参数，则默认查询所有配置。 
 
若输入条件编号，则查询满足条件编号的配置。 
 
若输入条件名称，则查询满足条件名称的配置。 
 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始条件编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于标识查询的DIAMETER路由条件配置的起始条件编号。数据来源：本端规划。配置原则：编号在允许取值范围内即可，需要小于等于结束条件编号。
END|结束条件编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于标识查询的DIAMETER路由条件配置的结束条件编号。数据来源：本端规划。配置原则：编号在允许取值范围内即可，需要大于等于起始条件编号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
CONDNO|条件编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由条件配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
CONDNAME|条件名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由条件配置。用户可根据本路由条件配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：不同条件的名称不可重复。
CONDTYPE|条件类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于描述匹配路由的条件类型。数据来源：本端规划。配置原则：目前支持的条件类型为：源主机名（ORIGIN）。
CONDOPTYPE|条件匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：当该DIAMETER路由条件被DIAMETER路由配置（增加DIAMETER路由命令）关联时，该参数用于明确条件值与本网元发送的DIAMETER消息中的Origin-Host AVP内容以哪种方式进行匹配。数据来源：本端规划。配置原则：该参数的选项有以下两种：从右往左最长匹配（LMFR）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容从最右到左包含了配置的条件值的全部字符，当与多个条件值相匹配的时候，选择条件值最长的那个条目。全匹配（AM）：码流中的Destination-Host AVP（或Destination-Realm AVP）内容与配置的条件值完全相同。默认为全匹配。
CONDITION|条件值|参数可选性:任选参数；参数类型:字符型；参数范围为:1~255个字符。|参数作用：该参数用于指定用来匹配的数据值。数据来源：本端规划。配置原则：当条件类型为“源主机名（LOCAL）”时，该参数内容为源主机的主机名。例如：条件值为“rcp.zte.com.cn”，条件类型为“源主机名”，条件匹配类型为“全匹配”，那么该条件的实际匹配动作就是：全匹配源主机名为rcp.zte.com.cn的主机。
命令举例 : 
查询DIAMETER路由条件编号为1。 
SHOW DIM ROUTECOND:BEGIN=1,END=1; 
`
命令 (No.1): SHOW DIM ROUTECOND:BEGIN=1,END=1;
操作维护         条件编号   条件名称   条件类型   条件匹配类型       条件值
---------------------------------------------------------------------------
复制 修改 删除   1          test       源主机名   全匹配             rcp.zte.com.cn
---------------------------------------------------------------------------
记录数 1
命令执行成功（耗时 0.021 秒）。
` 
相关命令 : 
[增加DIAMETER路由条件]
[修改DIAMETER路由条件]
[删除DIAMETER路由条件]
# DIAMETER路由组属性配置 
# DIAMETER路由组属性配置 
背景知识 : 
DIAMETER路由是指对本网元发送的DIAMETER消息或者从上一跳对等端接收到的DIAMETER消息进行分析，决定按以下哪种方式处理该消息。 
 
针对本网元发送的请求消息进行路由分析，决定本地动作及下一跳选路。 
 
针对本网元从上一跳对端接收的请求消息进行路由分析，决定本地动作以及下一跳选路。 
 
DIAMETER路由组属性配置指定了同一路由组中各个DIAMETER路由之间的处理模式。 
功能描述 : 
该功能用于配置DIAMETER路由组属性。当属于同一个路由组的DIAMETER路由之间以负荷分担或者主备模式方式进行处理时，各个DIAMETER路由需要关联一个DIAMETER路由组属性配置，表示该DIAMETER路由属于该DIAMETER路由组，并由该路由组属性配置指定路由间具体的处理模式。 
如果不配置DIAMETER路由组属性，就不能以负荷分担或主备模式来使用一组路由。 
## ADD DIM ROUTEGRPPTY 
## ADD DIM ROUTEGRPPTY 
命令功能 : 
该命令用于增加DIAMETER路由组属性。当需要以负荷分担或主备模式来使用一组路由时，使用该命令，为这组路由配置属性。 
通过在DIAMETER路由配置（[增加DIAMETER路由]命令）的“路由组编号”中关联该配置。RCP进行选路时，可以采用负荷分担或者主备方式选择该路由组中的路由。
注意事项 : 
在DIAMETER路由配置[增加DIAMETER路由]的“路由组编号”中关联该配置，该配置才会生效，表示该路由归属于路由组。
同一个DIAMETER路由，只能关联一个DIAMETER路由组属性配置，表示该DIAMETER路由属于该DIAMETER路由组。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
GROUPNO|路由组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由组属性配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
GROUPNAME|路由组名称|参数可选性:必选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由组属性。维护人员可根据本路由组属性配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：路由组名称具有唯一性，不同路由组名称不可以相同。
GROUPPTY|路由组属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:LOADBALANCE。|参数作用：该参数用于指定关联该DIAMETER路由组属性配置的DIAMETER路由之间的关系。数据来源：本端规划。配置原则：该参数的选项有以下两种：负荷分担（LOADBALANCE）：采用负荷分担方式时，可以通过增加DIAMETER路由命令配置路由组中各路由的权重。RCP进行路由分析时，根据权重配置在各路由之间实现负荷分担。主备模式（BACKUP）：采用主备模式时，可以通过增加DIAMETER路由命令配置路由组中的路由为主用路由或备用路由。RCP进行路由分析时，优先选择主用路由。当主用路由发生故障时，RCP才会选择备用路由。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
GROUPNO|路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由组属性配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
GROUPNAME|路由组名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由组属性。维护人员可根据本路由组属性配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：路由组名称具有唯一性，不同路由组名称不可以相同。
GROUPPTY|路由组属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定关联该DIAMETER路由组属性配置的DIAMETER路由之间的关系。数据来源：本端规划。配置原则：该参数的选项有以下两种：负荷分担（LOADBALANCE）：采用负荷分担方式时，可以通过增加DIAMETER路由命令配置路由组中各路由的权重。RCP进行路由分析时，根据权重配置在各路由之间实现负荷分担。主备模式（BACKUP）：采用主备模式时，可以通过增加DIAMETER路由命令配置路由组中的路由为主用路由或备用路由。RCP进行路由分析时，优先选择主用路由。当主用路由发生故障时，RCP才会选择备用路由。
命令举例 : 
增加DIAMETER路由组属性：路由组编号为1，路由组名称为1，组属性为"BACKUP"。 
ADD DIM ROUTEGRPPTY:GROUPNO=1,GROUPNAME="1",GROUPPTY="BACKUP"; 
## SET DIM ROUTEGRPPTY 
## SET DIM ROUTEGRPPTY 
命令功能 : 
该命令用于修改DIAMETER路由组属性。当RCP需要修改已有的DIAMETER路由组属性时，使用该命令。 
修改成功后，通过该路由组编号关联的DIAMETER路由，RCP将按照新配置的路由组属性进行路由分析，可能会影响原有RCP网元的DIAMETER消息发送。 
注意事项 : 
修改路由组属性时，先执行[查询DIAMETER路由]命令查询关联到本条路由组编号的所有路由,根据情况需要决定是否需要修改，如果需要将路由组属性从主备模式却换为负荷分担，请查看路由配置中的权重（Weight）设置是否合适，如果需要从负荷分担切换为主备模式，请查看路由配置中路由主用标识（Master Route）设置是否合适，之后再进行路由组属性的切换，会影响本端DIAMETER模块路由分析结果，从而影响RCP消息的发送。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
GROUPNO|路由组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由组属性配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
GROUPNAME|路由组名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由组属性。维护人员可根据本路由组属性配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：路由组名称具有唯一性，不同路由组名称不可以相同。
GROUPPTY|路由组属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定关联该DIAMETER路由组属性配置的DIAMETER路由之间的关系。数据来源：本端规划。配置原则：该参数的选项有以下两种：负荷分担（LOADBALANCE）：采用负荷分担方式时，可以通过增加DIAMETER路由命令配置路由组中各路由的权重。RCP进行路由分析时，根据权重配置在各路由之间实现负荷分担。主备模式（BACKUP）：采用主备模式时，可以通过增加DIAMETER路由命令配置路由组中的路由为主用路由或备用路由。RCP进行路由分析时，优先选择主用路由。当主用路由发生故障时，RCP才会选择备用路由。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
GROUPNO|路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由组属性配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
GROUPNAME|路由组名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由组属性。维护人员可根据本路由组属性配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：路由组名称具有唯一性，不同路由组名称不可以相同。
GROUPPTY|路由组属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定关联该DIAMETER路由组属性配置的DIAMETER路由之间的关系。数据来源：本端规划。配置原则：该参数的选项有以下两种：负荷分担（LOADBALANCE）：采用负荷分担方式时，可以通过增加DIAMETER路由命令配置路由组中各路由的权重。RCP进行路由分析时，根据权重配置在各路由之间实现负荷分担。主备模式（BACKUP）：采用主备模式时，可以通过增加DIAMETER路由命令配置路由组中的路由为主用路由或备用路由。RCP进行路由分析时，优先选择主用路由。当主用路由发生故障时，RCP才会选择备用路由。
命令举例 : 
修改DIAMETER路由组属性：路由组编号为1，路由组名称为1，组属性为"BACKUP"。 
SET DIM ROUTEGRPPTY:GROUPNO=1,GROUPNAME="1",GROUPPTY="BACKUP"; 
## DEL DIM ROUTEGRPPTY 
## DEL DIM ROUTEGRPPTY 
命令功能 : 
该命令用于删除DIAMETER路由组属性。当该路由组编号关联的DIAMETER路由不需要使用该组属性进行路由分析时，使用该命令删除路由组属性。 
删除成功后，将不能在DIAMETER路由中关联该DIAMETER路由组，可能会影响原有RCP网元的DIAMETER消息发送。 
注意事项 : 
删除路由组信息时，先执行[查询DIAMETER路由]命令查看“路由组编号”参数中是否关联本条路由组编号信息。若存在关联，则需要修改路由项关联到其它路由组，或者删除关联到该路由组的无效路由项。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
GROUPNO|路由组编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由组属性配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
命令举例 : 
删除DIAMETER路由组属性：路由组编号为1。 
DEL DIM ROUTEGRPPTY:GROUPNO=1; 
## SHOW DIM ROUTEGRPPTY 
## SHOW DIM ROUTEGRPPTY 
命令功能 : 
该命令用于查询DIAMETER路由组属性。当需要了解当前配置的DIAMETER路由组属性时，使用该命令。 
注意事项 : 
 
若不输入参数，则默认查询所有配置。 
 
若输入路由组编号和路由组属性名称，则查询指定条件的配置信息。 
 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于标识DIAMETER路由组属性配置的起始路由组编号。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，需要小于等于结束路由编号。
END|结束路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于标识DIAMETER路由组属性配置的结束路由组编号。数据来源：本端规划。配置原则：编号在允许取值范围内即可，需要大于等于起始路由组编号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
GROUPNO|路由组编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|参数作用：该参数用于唯一标识一条DIAMETER路由组属性配置。数据来源：本端规划。配置原则：编号范围在允许取值范围内即可，且全局唯一。
GROUPNAME|路由组名称|参数可选性:任选参数；参数类型:字符型；参数范围为:1~256个字符。|参数作用：该参数用于描述DIAMETER路由组属性。维护人员可根据本路由组属性配置的用途，为该配置添加描述，便于理解和识别。数据来源：本端规划。配置原则：路由组名称具有唯一性，不同路由组名称不可以相同。
GROUPPTY|路由组属性|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|参数作用：该参数用于指定关联该DIAMETER路由组属性配置的DIAMETER路由之间的关系。数据来源：本端规划。配置原则：该参数的选项有以下两种：负荷分担（LOADBALANCE）：采用负荷分担方式时，可以通过增加DIAMETER路由命令配置路由组中各路由的权重。RCP进行路由分析时，根据权重配置在各路由之间实现负荷分担。主备模式（BACKUP）：采用主备模式时，可以通过增加DIAMETER路由命令配置路由组中的路由为主用路由或备用路由。RCP进行路由分析时，优先选择主用路由。当主用路由发生故障时，RCP才会选择备用路由。
命令举例 : 
查询DIAMETER路由组属性。 
SHOW DIM ROUTEGRPPTY:BEGIN=1,END=1; 
`
命令 (No.1): SHOW DIM ROUTEGRPPTY:BEGIN=1,END=1;
操作维护         路由组编号   路由组名称   路由组属性
-----------------------------------------------------
复制 修改 删除   1            Group1       负荷分担
-----------------------------------------------------
记录数 1
命令执行成功（耗时 0.022 秒）。
` 
# DIAMETER AVP码父节点配置 
# DIAMETER AVP码父节点配置 
背景知识 : 
DIAMETER AVP码父节点配置包括：新增、修改、删除及查询DIAMETER AVP码父节点配置的相关命令及配置参数说明。 
功能描述 : 
DIM信令可编辑的使用场景往往是后验型使用场景，即两个网元的设备厂商在进行DIM信令交互时，发现交互信令不符合规范或双方理解不一致才会启用编辑功能。启用DIM信令可编辑功能时，试验码流已产生，为了避免后续类似处理流程失败，可考虑通过对特定消息内容进行DIM信令可编辑。 
DIM信令可编辑是指在外场对接时由于双方对DIM相关协议理解不一致时，能够在不重新制作版本前提下，通过修改信令码流，达到双方都能处理得目的，从而能顺利进行对接测试。DIM信令可编辑功能针对DIM消息码流AVP部分进行编辑，能够增加可选AVP、修改AVP值、删除可选AVP。 
若需要根据AVP码作为匹配条件进行信令编辑且待匹配的AVP是组合AVP的子节点，则配置该AVP的父节点信息。 
## ADD DIM FATHERAVP 
## ADD DIM FATHERAVP 
命令功能 : 
该命令用于增加DIAMETER AVP码父节点。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|DIAMETER AVP码父节点的编号，必须唯一。
AVPLAYERNO|AVP所在层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。默认值:1。|AVP所在层号, 该AVP在消息中的层数。
DIMAVPCODE|AVP码|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|AVP码，协议规定的AVP码。
VENDORID|AVP厂商标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|AVP厂商编号，协议规定或自定义厂商编号。
NEXTLAYERNUM|与下一层设定AVP层差|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。默认值:1。|与下一层设定AVP层差。
VENDORIDMATCHFLAG|厂商标识匹配标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NONEED。|厂商编号匹配标志，包括：需要匹配，不需要匹配。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|DIAMETER AVP码父节点的编号，必须唯一。
AVPLAYERNO|AVP所在层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|AVP所在层号, 该AVP在消息中的层数。
DIMAVPCODE|AVP码|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|AVP码，协议规定的AVP码。
VENDORID|AVP厂商标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|AVP厂商编号，协议规定或自定义厂商编号。
NEXTLAYERNUM|与下一层设定AVP层差|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|与下一层设定AVP层差。
VENDORIDMATCHFLAG|厂商标识匹配标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|厂商编号匹配标志，包括：需要匹配，不需要匹配。
命令举例 : 
增加一个父节点编号为1、AVP码为630的父节点配置的命令：
ADD DIM FATHERAVP:ID=1,DIMAVPCODE=630,VENDORID=10415,NEXTLAYERNUM=1,VENDORIDMATCHFLAG="NEED"; 
相关命令 : 
[修改DIAMETER AVP码父节点]
[删除DIAMETER AVP码父节点]
[查询DIAMETER AVP码父节点]
## SET DIM FATHERAVP 
## SET DIM FATHERAVP 
命令功能 : 
该命令用于修改DIAMETER AVP码父节点。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|DIAMETER AVP码父节点的编号，必须唯一。
AVPLAYERNO|AVP所在层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|AVP所在层号, 该AVP在消息中的层数。
DIMAVPCODE|AVP码|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|AVP码，协议规定的AVP码。
VENDORID|AVP厂商标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|AVP厂商编号，协议规定或自定义厂商编号。
NEXTLAYERNUM|与下一层设定AVP层差|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|与下一层设定AVP层差。
VENDORIDMATCHFLAG|厂商标识匹配标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|厂商编号匹配标志，包括：需要匹配，不需要匹配。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|DIAMETER AVP码父节点的编号，必须唯一。
AVPLAYERNO|AVP所在层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|AVP所在层号, 该AVP在消息中的层数。
DIMAVPCODE|AVP码|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|AVP码，协议规定的AVP码。
VENDORID|AVP厂商标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|AVP厂商编号，协议规定或自定义厂商编号。
NEXTLAYERNUM|与下一层设定AVP层差|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|与下一层设定AVP层差。
VENDORIDMATCHFLAG|厂商标识匹配标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|厂商编号匹配标志，包括：需要匹配，不需要匹配。
命令举例 : 
修改父节点编号为1、厂商标识修改为“不需要匹配”的命令：
SET DIM FATHERAVP:ID=1,VENDORIDMATCHFLAG="NONEED"; 
相关命令 : 
[增加DIAMETER AVP码父节点]
[删除DIAMETER AVP码父节点]
[查询DIAMETER AVP码父节点]
## DEL DIM FATHERAVP 
## DEL DIM FATHERAVP 
命令功能 : 
该命令用于删除DIAMETER AVP码父节点。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|DIAMETER AVP码父节点的编号，必须唯一。
命令举例 : 
删除父节点编号为1的父节点配置的命令：
DEL DIM FATHERAVP:ID=1; 
相关命令 : 
[增加DIAMETER AVP码父节点]
[修改DIAMETER AVP码父节点]
[查询DIAMETER AVP码父节点]
## SHOW DIM FATHERAVP 
## SHOW DIM FATHERAVP 
命令功能 : 
该命令用于查询DIAMETER AVP码父节点。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|查询时设置的起始编号。
END|结束编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|查询时设置的结束编号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|DIAMETER AVP码父节点的编号，必须唯一。
AVPLAYERNO|AVP所在层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|AVP所在层号, 该AVP在消息中的层数。
DIMAVPCODE|AVP码|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|AVP码，协议规定的AVP码。
VENDORID|AVP厂商标识|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|AVP厂商编号，协议规定或自定义厂商编号。
NEXTLAYERNUM|与下一层设定AVP层差|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|与下一层设定AVP层差。
VENDORIDMATCHFLAG|厂商标识匹配标志|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|厂商编号匹配标志，包括：需要匹配，不需要匹配。
命令举例 : 
显示父节点编号为1的配置信息的命令：
SHOW DIM FATHERAVP:BEGIN=1,END=1; 
相关命令 : 
[增加DIAMETER AVP码父节点]
[修改DIAMETER AVP码父节点]
[删除DIAMETER AVP码父节点]
# DIAMETER AVP码匹配方法配置 
# DIAMETER AVP码匹配方法配置 
背景知识 : 
DIAMETER AVP码匹配方法配置包括：新增、修改、删除及查询DIAMETER AVP码匹配方法配置的相关命令及配置参数说明。 
功能描述 : 
DIM信令可编辑的使用场景往往是后验型使用场景，即两个网元的设备厂商在进行DIM信令交互时，发现交互信令不符合规范或双方理解不一致才会启用编辑功能。启用DIM信令可编辑功能时，试验码流已产生，为了避免后续类似处理流程失败，可考虑通过对特定消息内容进行DIM信令可编辑。 
DIM信令可编辑是指在外场对接时由于双方对DIM相关协议理解不一致时，能够在不重新制作版本前提下，通过修改信令码流，达到双方都能处理得目的，从而能顺利进行对接测试。DIM信令可编辑功能针对DIM消息码流AVP部分进行编辑，能够增加可选AVP、修改AVP值、删除可选AVP。 
若需要根据AVP码作为匹配条件进行信令编辑，则配置该AVP码匹配方法；若该AVP存在父节点信息，则引用已配置该AVP的父节点ID。 
## ADD DIM AVPCODEMATCH 
## ADD DIM AVPCODEMATCH 
命令功能 : 
该命令用于增加DIAMETER AVP码匹配方法。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP码匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BOTH。|匹配模式，指定层级和组合关系都匹配。
AVPCODE|待编辑的AVP码|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|待编辑的AVP码，协议规定的AVP码。
VENDORIDFLG|厂商编号匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:NONEED。|厂商编号匹配标记，包括：需要匹配，不需要匹配。
VENDORID|厂商编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|厂商编号，协议规定或自定义厂商编号。
AVPLAYER|AVP层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。默认值:1。|AVP层号，该AVP在消息中的层数。
FATHERAVPID1|父AVP编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|父AVP编号1，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID2|父AVP编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|父AVP编号2，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID3|父AVP编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|父AVP编号3，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID4|父AVP编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。默认值:0。|父AVP编号4，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP码匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|匹配模式，指定层级和组合关系都匹配。
AVPCODE|待编辑的AVP码|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|待编辑的AVP码，协议规定的AVP码。
VENDORIDFLG|厂商编号匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|厂商编号匹配标记，包括：需要匹配，不需要匹配。
VENDORID|厂商编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|厂商编号，协议规定或自定义厂商编号。
AVPLAYER|AVP层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|AVP层号，该AVP在消息中的层数。
FATHERAVPID1|父AVP编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号1，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID2|父AVP编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号2，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID3|父AVP编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号3，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID4|父AVP编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号4，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
命令举例 : 
增加一个AVP码匹配方法编号为1、AVP码为628的匹配方法的命令：
ADD DIM AVPCODEMATCH:ID=1,AVPCODE=628,VENDORIDFLG="NEED",VENDORID=10415,FATHERAVPID1=1; 
相关命令 : 
[修改DIAMETER AVP码匹配方法]
[删除DIAMETER AVP码匹配方法]
[查询DIAMETER AVP码匹配方法]
## SET DIM AVPCODEMATCH 
## SET DIM AVPCODEMATCH 
命令功能 : 
该命令用于修改DIAMETER AVP码匹配方法。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP码匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|匹配模式，指定层级和组合关系都匹配。
AVPCODE|待编辑的AVP码|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|待编辑的AVP码，协议规定的AVP码。
VENDORIDFLG|厂商编号匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|厂商编号匹配标记，包括：需要匹配，不需要匹配。
VENDORID|厂商编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|厂商编号，协议规定或自定义厂商编号。
AVPLAYER|AVP层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|AVP层号，该AVP在消息中的层数。
FATHERAVPID1|父AVP编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号1，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID2|父AVP编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号2，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID3|父AVP编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号3，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID4|父AVP编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号4，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP码匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|匹配模式，指定层级和组合关系都匹配。
AVPCODE|待编辑的AVP码|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|待编辑的AVP码，协议规定的AVP码。
VENDORIDFLG|厂商编号匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|厂商编号匹配标记，包括：需要匹配，不需要匹配。
VENDORID|厂商编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|厂商编号，协议规定或自定义厂商编号。
AVPLAYER|AVP层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|AVP层号，该AVP在消息中的层数。
FATHERAVPID1|父AVP编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号1，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID2|父AVP编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号2，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID3|父AVP编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号3，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID4|父AVP编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号4，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
命令举例 : 
修改AVP码匹配方法编号为1、厂商标识为“不需要匹配”的命令：
SET DIM AVPCODEMATCH:ID=1,VENDORIDFLG="NONEED"; 
相关命令 : 
[增加DIAMETER AVP码匹配方法]
[删除DIAMETER AVP码匹配方法]
[查询DIAMETER AVP码匹配方法]
## DEL DIM AVPCODEMATCH 
## DEL DIM AVPCODEMATCH 
命令功能 : 
该命令用于删除DIAMETER AVP码匹配方法。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP码匹配方法的编号，必须唯一。
命令举例 : 
删除AVP码匹配方法编号为1的匹配方法的命令：
DEL DIM AVPCODEMATCH:ID=1; 
相关命令 : 
[增加DIAMETER AVP码匹配方法]
[修改DIAMETER AVP码匹配方法]
[查询DIAMETER AVP码匹配方法]
## SHOW DIM AVPCODEMATCH 
## SHOW DIM AVPCODEMATCH 
命令功能 : 
该命令用于查询DIAMETER AVP码匹配方法。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|查询时设置的起始匹配方法编号。
END|结束匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|查询时设置的结束匹配方法编号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP码匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|匹配模式，指定层级和组合关系都匹配。
AVPCODE|待编辑的AVP码|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|待编辑的AVP码，协议规定的AVP码。
VENDORIDFLG|厂商编号匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|厂商编号匹配标记，包括：需要匹配，不需要匹配。
VENDORID|厂商编号|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|厂商编号，协议规定或自定义厂商编号。
AVPLAYER|AVP层号|参数可选性:任选参数；参数类型:整数；参数范围为:1~4。|AVP层号，该AVP在消息中的层数。
FATHERAVPID1|父AVP编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号1，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID2|父AVP编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号2，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID3|父AVP编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号3，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
FATHERAVPID4|父AVP编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~4294967295。|父AVP编号4，引用已配置父节点编号，需要在增加DIAMETER AVP码父节点配置。
命令举例 : 
查询AVP码匹配方法编号为1的配置信息的命令：
SHOW DIM AVPCODEMATCH:BEGIN=1,END=1; 
相关命令 : 
[增加DIAMETER AVP码匹配方法]
[修改DIAMETER AVP码匹配方法]
[删除DIAMETER AVP码匹配方法]
# DIAMETER AVP值特征码流匹配方法配置 
# DIAMETER AVP值特征码流匹配方法配置 
背景知识 : 
DIAMETER AVP值特征码流匹配方法配置包括：新增、修改、删除及查询DIAMETER AVP值特征码流匹配方法配置的相关命令及配置参数说明。 
功能描述 : 
DIM信令可编辑的使用场景往往是后验型使用场景，即两个网元的设备厂商在进行DIM信令交互时，发现交互信令不符合规范或双方理解不一致才会启用编辑功能。启用DIM信令可编辑功能时，试验码流已产生，为了避免后续类似处理流程失败，可考虑通过对特定消息内容进行DIM信令可编辑。 
DIM信令可编辑是指在外场对接时由于双方对DIM相关协议理解不一致时，能够在不重新制作版本前提下，通过修改信令码流，达到双方都能处理得目的，从而能顺利进行对接测试。DIM信令可编辑功能针对DIM消息码流AVP部分进行编辑，能够增加可选AVP、修改AVP值、删除可选AVP。 
若需要根据AVP值码流作为匹配条件进行信令编辑，则配置该AVP值特征码流匹配方法。 
## ADD DIM AVPVALUEMATCH 
## ADD DIM AVPVALUEMATCH 
命令功能 : 
该命令用于增加DIAMETER AVP值特征码流匹配方法。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP值特征码流匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:CM。|匹配模式包括：完全匹配，模糊匹配。
AVPCODE|码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|待匹配的AVP内容码流，为二进制码流格式。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP值特征码流匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|匹配模式包括：完全匹配，模糊匹配。
AVPCODE|码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|待匹配的AVP内容码流，为二进制码流格式。
命令举例 : 
增加一个AVP值特征码流匹配方法编号为1、匹配码流为输入的匹配方法的命令：
ADD DIM AVPVALUEMATCH:ID=1,AVPCODE="00000022"; 
相关命令 : 
[修改DIAMETER AVP值特征码流匹配方法]
[删除DIAMETER AVP值特征码流匹配方法]
[查询DIAMETER AVP值特征码流匹配方法]
## SET DIM AVPVALUEMATCH 
## SET DIM AVPVALUEMATCH 
命令功能 : 
该命令用于修改DIAMETER AVP值特征码流匹配方法。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP值特征码流匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|匹配模式包括：完全匹配，模糊匹配。
AVPCODE|码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|待匹配的AVP内容码流，为二进制码流格式。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP值特征码流匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|匹配模式包括：完全匹配，模糊匹配。
AVPCODE|码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|待匹配的AVP内容码流，为二进制码流格式。
命令举例 : 
修改AVP值特征码流匹配方法编号为1、匹配类型为“模糊匹配”的命令：
SET DIM AVPVALUEMATCH:ID=1,MATCHTYPE="BM"; 
相关命令 : 
[增加DIAMETER AVP值特征码流匹配方法]
[删除DIAMETER AVP值特征码流匹配方法]
[查询DIAMETER AVP值特征码流匹配方法]
## DEL DIM AVPVALUEMATCH 
## DEL DIM AVPVALUEMATCH 
命令功能 : 
该命令用于删除DIAMETER AVP值特征码流匹配方法。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP值特征码流匹配方法的编号，必须唯一。
命令举例 : 
删除AVP值特征码流匹配方法编号为1的匹配方法的命令：
DEL DIM AVPVALUEMATCH:ID=1; 
相关命令 : 
[增加DIAMETER AVP值特征码流匹配方法]
[修改DIAMETER AVP值特征码流匹配方法]
[查询DIAMETER AVP值特征码流匹配方法]
## SHOW DIM AVPVALUEMATCH 
## SHOW DIM AVPVALUEMATCH 
命令功能 : 
该命令用于查询DIAMETER AVP值特征码流匹配方法。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|查询时设置的起始匹配方法编号。
END|结束匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|查询时设置的结束匹配方法编号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
ID|匹配方法编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER AVP值特征码流匹配方法的编号，必须唯一。
MATCHTYPE|匹配类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|匹配模式包括：完全匹配，模糊匹配。
AVPCODE|码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~255个字符。|待匹配的AVP内容码流，为二进制码流格式。
命令举例 : 
查询AVP值特征码流匹配方法编号为1的配置信息的命令：
SHOW DIM AVPVALUEMATCH:BEGIN=1,END=1; 
相关命令 : 
[增加DIAMETER AVP值特征码流匹配方法]
[修改DIAMETER AVP值特征码流匹配方法]
[删除DIAMETER AVP值特征码流匹配方法]
# DIAMETER信令可编辑动作配置 
# DIAMETER信令可编辑动作配置 
背景知识 : 
DIM信令可编辑的使用场景往往是后验型使用场景，即两个网元的设备厂商在进行DIM信令交互时，发现交互信令不符合规范或双方理解不一致才会启用编辑功能。启用DIM信令可编辑功能时，试验码流已产生，为了避免后续类似处理流程失败，可考虑通过对特定消息内容进行DIM信令可编辑。
功能描述 : 
DIM信令可编辑是指在外场对接时由于双方对DIM相关协议理解不一致时，能够在不重新制作版本前提下，通过修改信令码流，达到双方都能处理得目的，从而能顺利进行对接测试。DIM信令可编辑功能针对DIM消息码流AVP部分进行编辑，能够增加可选AVP、修改AVP值、删除可选AVP。
## 配置流程说明 
 
增加信令编辑的策略配置，同一个策略引用已配置好的编辑动作进行编辑。 
 
## ADD DIM EDITACT 
## ADD DIM EDITACT 
命令功能 : 
该命令用于增加DIAMETER信令可编辑动作。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|动作编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER信令可编辑动作的编号，必须唯一。
OPWAY|操作方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:MODAVPVALUE。|编辑动作操作方式，包括：修改AVP值，增加AVP，删除AVP。
DIRECTION|码流方向匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BOTH。|码流方向匹配，包括：双向，入局，出局。
CMDCODE|消息码匹配|参数可选性:必选参数；参数类型:整数；参数范围为:1~4294967295。|消息码匹配。
MSGTYPE|消息类型匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BOTH。|消息类型匹配，包括：请求和响应，请求，响应。
METHODTYPE1|AVP相关匹配方法类型编号1|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。默认值:NONE。|AVP相关匹配方法类型编号1，包括AVP码匹配方法和AVP值特征码流匹配方法，具体配置要求参考特性指导说明书。
METHOD1|AVP相关匹配方法编号1|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|AVP相关匹配方法编号1，如果AVP码匹配方法，需要在增加DIAMETER AVP码匹配方法中提前配置好。如果AVP值特征码流匹配方法，需要在增加DIAMETER AVP值特征码流匹配方法中提前配置好。
METHODTYPE2|AVP相关匹配方法类型编号2|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。默认值:NONE。|AVP相关匹配方法类型编号2，参考AVP相关匹配方法类型编号1。
METHOD2|AVP相关匹配方法编号2|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|AVP相关匹配方法编号2，参考AVP相关匹配方法编号1。
METHODTYPE3|AVP相关匹配方法类型编号3|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。默认值:NONE。|AVP相关匹配方法类型编号3，参考AVP相关匹配方法编号1。
METHOD3|AVP相关匹配方法编号3|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|AVP相关匹配方法编号3，参考AVP相关匹配方法编号1。
METHODTYPE4|AVP相关匹配方法类型编号4|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。默认值:NONE。|AVP相关匹配方法类型编号4，参考AVP相关匹配方法编号1。
METHOD4|AVP相关匹配方法编号4|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|AVP相关匹配方法编号4，参考AVP相关匹配方法编号1。
REPMETHOD|AVP替换方法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:BIN。|AVP替换方法，指二进制码流替换方法。
AVPINFO|AVP替换码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~2046个字符。|AVP替换码流。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|动作编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER信令可编辑动作的编号，必须唯一。
OPWAY|操作方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编辑动作操作方式，包括：修改AVP值，增加AVP，删除AVP。
DIRECTION|码流方向匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|码流方向匹配，包括：双向，入局，出局。
CMDCODE|消息码匹配|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|消息码匹配。
MSGTYPE|消息类型匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|消息类型匹配，包括：请求和响应，请求，响应。
METHODTYPE1|AVP相关匹配方法类型编号1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号1，包括AVP码匹配方法和AVP值特征码流匹配方法，具体配置要求参考特性指导说明书。
METHOD1|AVP相关匹配方法编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号1，如果AVP码匹配方法，需要在增加DIAMETER AVP码匹配方法中提前配置好。如果AVP值特征码流匹配方法，需要在增加DIAMETER AVP值特征码流匹配方法中提前配置好。
METHODTYPE2|AVP相关匹配方法类型编号2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号2，参考AVP相关匹配方法类型编号1。
METHOD2|AVP相关匹配方法编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号2，参考AVP相关匹配方法编号1。
METHODTYPE3|AVP相关匹配方法类型编号3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号3，参考AVP相关匹配方法编号1。
METHOD3|AVP相关匹配方法编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号3，参考AVP相关匹配方法编号1。
METHODTYPE4|AVP相关匹配方法类型编号4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号4，参考AVP相关匹配方法编号1。
METHOD4|AVP相关匹配方法编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号4，参考AVP相关匹配方法编号1。
REPMETHOD|AVP替换方法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP替换方法，指二进制码流替换方法。
AVPINFO|AVP替换码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~2046个字符。|AVP替换码流。
命令举例 : 
增加一个编辑动作编号为1，匹配动作为修改AVP值的匹配方法的命令：
ADD DIM EDITACT:NO=1,OPWAY="MODAVPVALUE",CMDCODE=316,METHODTYPE1="ACP",METHOD1=1,METHODTYPE2="AVRM",METHOD2=1,AVPINFO="000001c8"; 
相关命令 : 
[修改DIAMETER信令可编辑动作]
[删除DIAMETER信令可编辑动作]
[查询DIAMETER信令可编辑动作]
## SET DIM EDITACT 
## SET DIM EDITACT 
命令功能 : 
该命令用于修改DIAMETER信令可编辑动作。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|动作编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER信令可编辑动作的编号，必须唯一。
OPWAY|操作方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编辑动作操作方式，包括：修改AVP值，增加AVP，删除AVP。
DIRECTION|码流方向匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|码流方向匹配，包括：双向，入局，出局。
CMDCODE|消息码匹配|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|消息码匹配。
MSGTYPE|消息类型匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|消息类型匹配，包括：请求和响应，请求，响应。
METHODTYPE1|AVP相关匹配方法类型编号1|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号1，包括AVP码匹配方法和AVP值特征码流匹配方法，具体配置要求参考特性指导说明书。
METHOD1|AVP相关匹配方法编号1|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号1，如果AVP码匹配方法，需要在增加DIAMETER AVP码匹配方法中提前配置好。如果AVP值特征码流匹配方法，需要在增加DIAMETER AVP值特征码流匹配方法中提前配置好。
METHODTYPE2|AVP相关匹配方法类型编号2|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号2，参考AVP相关匹配方法类型编号1。
METHOD2|AVP相关匹配方法编号2|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号2，参考AVP相关匹配方法编号1。
METHODTYPE3|AVP相关匹配方法类型编号3|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号3，参考AVP相关匹配方法编号1。
METHOD3|AVP相关匹配方法编号3|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号3，参考AVP相关匹配方法编号1。
METHODTYPE4|AVP相关匹配方法类型编号4|参数可选性:特殊任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号4，参考AVP相关匹配方法编号1。
METHOD4|AVP相关匹配方法编号4|参数可选性:特殊任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号4，参考AVP相关匹配方法编号1。
REPMETHOD|AVP替换方法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP替换方法，指二进制码流替换方法。
AVPINFO|AVP替换码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~2046个字符。|AVP替换码流。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|动作编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER信令可编辑动作的编号，必须唯一。
OPWAY|操作方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编辑动作操作方式，包括：修改AVP值，增加AVP，删除AVP。
DIRECTION|码流方向匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|码流方向匹配，包括：双向，入局，出局。
CMDCODE|消息码匹配|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|消息码匹配。
MSGTYPE|消息类型匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|消息类型匹配，包括：请求和响应，请求，响应。
METHODTYPE1|AVP相关匹配方法类型编号1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号1，包括AVP码匹配方法和AVP值特征码流匹配方法，具体配置要求参考特性指导说明书。
METHOD1|AVP相关匹配方法编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号1，如果AVP码匹配方法，需要在增加DIAMETER AVP码匹配方法中提前配置好。如果AVP值特征码流匹配方法，需要在增加DIAMETER AVP值特征码流匹配方法中提前配置好。
METHODTYPE2|AVP相关匹配方法类型编号2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号2，参考AVP相关匹配方法类型编号1。
METHOD2|AVP相关匹配方法编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号2，参考AVP相关匹配方法编号1。
METHODTYPE3|AVP相关匹配方法类型编号3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号3，参考AVP相关匹配方法编号1。
METHOD3|AVP相关匹配方法编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号3，参考AVP相关匹配方法编号1。
METHODTYPE4|AVP相关匹配方法类型编号4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号4，参考AVP相关匹配方法编号1。
METHOD4|AVP相关匹配方法编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号4，参考AVP相关匹配方法编号1。
REPMETHOD|AVP替换方法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP替换方法，指二进制码流替换方法。
AVPINFO|AVP替换码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~2046个字符。|AVP替换码流。
命令举例 : 
修改编辑动作编号为1、方向为入向的命令：
SET DIM EDITACT:NO=1,DIRECTION="IN"; 
相关命令 : 
[增加DIAMETER信令可编辑动作]
[删除DIAMETER信令可编辑动作]
[查询DIAMETER信令可编辑动作]
## DEL DIM EDITACT 
## DEL DIM EDITACT 
命令功能 : 
该命令用于删除DIAMETER信令可编辑动作。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|动作编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER信令可编辑动作的编号，必须唯一。
命令举例 : 
删除编辑动作编号为1的匹配方法的命令：
DEL DIM EDITACT:NO=1; 
相关命令 : 
[增加DIAMETER信令可编辑动作]
[修改DIAMETER信令可编辑动作]
[查询DIAMETER信令可编辑动作]
## SHOW DIM EDITACT 
## SHOW DIM EDITACT 
命令功能 : 
该命令用于查询DIAMETER信令可编辑动作。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始动作编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|查询时设置的起始动作编号。
END|结束动作编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|查询时设置的结束动作编号。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|动作编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~65535。|DIAMETER信令可编辑动作的编号，必须唯一。
OPWAY|操作方式|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|编辑动作操作方式，包括：修改AVP值，增加AVP，删除AVP。
DIRECTION|码流方向匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|码流方向匹配，包括：双向，入局，出局。
CMDCODE|消息码匹配|参数可选性:任选参数；参数类型:整数；参数范围为:1~4294967295。|消息码匹配。
MSGTYPE|消息类型匹配|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|消息类型匹配，包括：请求和响应，请求，响应。
METHODTYPE1|AVP相关匹配方法类型编号1|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号1，包括AVP码匹配方法和AVP值特征码流匹配方法，具体配置要求参考特性指导说明书。
METHOD1|AVP相关匹配方法编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号1，如果AVP码匹配方法，需要在增加DIAMETER AVP码匹配方法中提前配置好。如果AVP值特征码流匹配方法，需要在增加DIAMETER AVP值特征码流匹配方法中提前配置好。
METHODTYPE2|AVP相关匹配方法类型编号2|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号2，参考AVP相关匹配方法类型编号1。
METHOD2|AVP相关匹配方法编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号2，参考AVP相关匹配方法编号1。
METHODTYPE3|AVP相关匹配方法类型编号3|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号3，参考AVP相关匹配方法编号1。
METHOD3|AVP相关匹配方法编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号3，参考AVP相关匹配方法编号1。
METHODTYPE4|AVP相关匹配方法类型编号4|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP相关匹配方法类型编号4，参考AVP相关匹配方法编号1。
METHOD4|AVP相关匹配方法编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|AVP相关匹配方法编号4，参考AVP相关匹配方法编号1。
REPMETHOD|AVP替换方法|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|AVP替换方法，指二进制码流替换方法。
AVPINFO|AVP替换码流|参数可选性:任选参数；参数类型:字符型；参数范围为:0~2046个字符。|AVP替换码流。
命令举例 : 
查询编辑动作编号为1的配置信息的命令：
SHOW DIM EDITACT:BEGIN=1,END=1; 
相关命令 : 
[增加DIAMETER信令可编辑动作]
[修改DIAMETER信令可编辑动作]
[删除DIAMETER信令可编辑动作]
# DIAMETER信令可编辑策略配置 
# DIAMETER信令可编辑策略配置 
背景知识 : 
DIAMETER信令可编辑动作配置包括：新增、修改、删除及查询DIAMETER信令可编辑动作配置的相关命令及配置参数说明。 
功能描述 : 
DIM信令可编辑的使用场景往往是后验型使用场景，即两个网元的设备厂商在进行DIM信令交互时，发现交互信令不符合规范或双方理解不一致才会启用编辑功能。启用DIM信令可编辑功能时，试验码流已产生，为了避免后续类似处理流程失败，可考虑通过对特定消息内容进行DIM信令可编辑。 
DIM信令可编辑是指在外场对接时由于双方对DIM相关协议理解不一致时，能够在不重新制作版本前提下，通过修改信令码流，达到双方都能处理得目的，从而能顺利进行对接测试。DIM信令可编辑功能针对DIM消息码流AVP部分进行编辑，能够增加可选AVP、修改AVP值、删除可选AVP。 
增加信令编辑的动作配置，包括增加可选AVP、修改AVP值、删除可选AVP。可以根据AVP码匹配方法和AVP值码流匹配方法进行匹配后执行编辑动作。 
## ADD DIM EDITPLC 
## ADD DIM EDITPLC 
命令功能 : 
该命令用于增加DIAMETER信令可编辑策略。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~64。|策略编号
APPID|应用ID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:Gx。|应用ID，与待编辑消息头部中的应用ID一致
URI|待匹配的URI|参数可选性:必选参数；参数类型:字符型；参数范围为:1~127个字符。|待编辑的匹配URI
SWTICH|信令可编辑开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。默认值:OFF。|信令可编辑开关
ACTNO1|动作编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号1，引用已配置好的编辑动作
ACTNO2|动作编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号2，引用已配置好的编辑动作
ACTNO3|动作编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号3，引用已配置好的编辑动作
ACTNO4|动作编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号4，引用已配置好的编辑动作
ACTNO5|动作编号5|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号5，引用已配置好的编辑动作
ACTNO6|动作编号6|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号6，引用已配置好的编辑动作
ACTNO7|动作编号7|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号7，引用已配置好的编辑动作
ACTNO8|动作编号8|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号8，引用已配置好的编辑动作
ACTNO9|动作编号9|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号9，引用已配置好的编辑动作
ACTNO10|动作编号10|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。默认值:0。|动作编号10，引用已配置好的编辑动作
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~64。|策略编号
APPID|应用ID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|应用ID，与待编辑消息头部中的应用ID一致
URI|待匹配的URI|参数可选性:任选参数；参数类型:字符型；参数范围为:0~127个字符。|待编辑的匹配URI
SWTICH|信令可编辑开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|信令可编辑开关
ACTNO1|动作编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号1，引用已配置好的编辑动作
ACTNO2|动作编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号2，引用已配置好的编辑动作
ACTNO3|动作编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号3，引用已配置好的编辑动作
ACTNO4|动作编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号4，引用已配置好的编辑动作
ACTNO5|动作编号5|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号5，引用已配置好的编辑动作
ACTNO6|动作编号6|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号6，引用已配置好的编辑动作
ACTNO7|动作编号7|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号7，引用已配置好的编辑动作
ACTNO8|动作编号8|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号8，引用已配置好的编辑动作
ACTNO9|动作编号9|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号9，引用已配置好的编辑动作
ACTNO10|动作编号10|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号10，引用已配置好的编辑动作
命令举例 : 
增加一个编辑策略编号为1，到PCRF局向的策略编辑的命令：
ADD DIM EDITPLC:NO=1,APPID="RX",URI="pcrf.zte.com.cn",SWTICH="ON",ACTNO1=1; 
相关命令 : 
[修改DIAMETER信令可编辑策略]
[删除DIAMETER信令可编辑策略]
[查询DIAMETER信令可编辑策略]
## SET DIM EDITPLC 
## SET DIM EDITPLC 
命令功能 : 
该命令用于修改DIAMETER信令可编辑策略。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~64。|策略编号
SWTICH|信令可编辑开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|信令可编辑开关
ACTNO1|动作编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号1，引用已配置好的编辑动作
ACTNO2|动作编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号2，引用已配置好的编辑动作
ACTNO3|动作编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号3，引用已配置好的编辑动作
ACTNO4|动作编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号4，引用已配置好的编辑动作
ACTNO5|动作编号5|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号5，引用已配置好的编辑动作
ACTNO6|动作编号6|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号6，引用已配置好的编辑动作
ACTNO7|动作编号7|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号7，引用已配置好的编辑动作
ACTNO8|动作编号8|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号8，引用已配置好的编辑动作
ACTNO9|动作编号9|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号9，引用已配置好的编辑动作
ACTNO10|动作编号10|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号10，引用已配置好的编辑动作
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~64。|策略编号
APPID|应用ID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|应用ID，与待编辑消息头部中的应用ID一致
URI|待匹配的URI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|待编辑的匹配URI
SWTICH|信令可编辑开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|信令可编辑开关
ACTNO1|动作编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号1，引用已配置好的编辑动作
ACTNO2|动作编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号2，引用已配置好的编辑动作
ACTNO3|动作编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号3，引用已配置好的编辑动作
ACTNO4|动作编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号4，引用已配置好的编辑动作
ACTNO5|动作编号5|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号5，引用已配置好的编辑动作
ACTNO6|动作编号6|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号6，引用已配置好的编辑动作
ACTNO7|动作编号7|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号7，引用已配置好的编辑动作
ACTNO8|动作编号8|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号8，引用已配置好的编辑动作
ACTNO9|动作编号9|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号9，引用已配置好的编辑动作
ACTNO10|动作编号10|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号10，引用已配置好的编辑动作
命令举例 : 
修改编辑策略编号为1、策略开关为关闭的命令：
SET DIM EDITPLC:NO=1,SWTICH="OFF"; 
相关命令 : 
[增加DIAMETER信令可编辑策略]
[删除DIAMETER信令可编辑策略]
[查询DIAMETER信令可编辑策略]
## DEL DIM EDITPLC 
## DEL DIM EDITPLC 
命令功能 : 
该命令用于删除DIAMETER信令可编辑策略。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|策略编号|参数可选性:必选参数；参数类型:整数；参数范围为:1~64。|策略编号
命令举例 : 
删除编辑策略编号为1的匹配方法的命令：
DEL DIM EDITPLC:NO=1; 
相关命令 : 
[增加DIAMETER信令可编辑策略]
[修改DIAMETER信令可编辑策略]
[查询DIAMETER信令可编辑策略]
## SHOW DIM EDITPLC 
## SHOW DIM EDITPLC 
命令功能 : 
该命令用于查询DIAMETER信令可编辑策略。
注意事项 : 
无。
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
BEGIN|起始策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~64。|起始策略编号
END|结束策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~64。|结束策略编号
APPID|应用ID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|应用ID，与待编辑消息头部中的应用ID一致
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
NO|策略编号|参数可选性:任选参数；参数类型:整数；参数范围为:1~64。|策略编号
APPID|应用ID|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|应用ID，与待编辑消息头部中的应用ID一致
URI|待匹配的URI|参数可选性:任选参数；参数类型:字符型；参数范围为:1~127个字符。|待编辑的匹配URI
SWTICH|信令可编辑开关|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|信令可编辑开关
ACTNO1|动作编号1|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号1，引用已配置好的编辑动作
ACTNO2|动作编号2|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号2，引用已配置好的编辑动作
ACTNO3|动作编号3|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号3，引用已配置好的编辑动作
ACTNO4|动作编号4|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号4，引用已配置好的编辑动作
ACTNO5|动作编号5|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号5，引用已配置好的编辑动作
ACTNO6|动作编号6|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号6，引用已配置好的编辑动作
ACTNO7|动作编号7|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号7，引用已配置好的编辑动作
ACTNO8|动作编号8|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号8，引用已配置好的编辑动作
ACTNO9|动作编号9|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号9，引用已配置好的编辑动作
ACTNO10|动作编号10|参数可选性:任选参数；参数类型:整数；参数范围为:0~65535。|动作编号10，引用已配置好的编辑动作
命令举例 : 
显示编辑策略编号为1的配置信息的命令：
SHOW DIM EDITPLC:BEGIN=1,END=1; 
相关命令 : 
[增加DIAMETER信令可编辑策略]
[修改DIAMETER信令可编辑策略]
[删除DIAMETER信令可编辑策略]
# DIAMETER告警门限配置 
# DIAMETER告警门限配置 
背景知识 : 
RCP网元的重要功能之一是实现与邻接网元的Diameter消息交互。各项资源（路由、链路和承载）配置与Diameter的消息链路配置相关；数据区保障Diameter消息能够有序的收发。当出现数据区和各项资源（路由、链路和承载）占用率过大时，上报告警有助于及时发现问题并解决问题。不同系统对数据区和各项资源（路由、链路和承载）的各级使用率告警阈值设置的需求不同。 
功能描述 : 
Diameter告警门限配置用于提供一种告警上报和告警恢复机制： 
 
当Diameter模块中的数据区和各项资源（路由、链路和承载）使用率大于等于系统配置的各级使用率告警阈值时，RCP会上报相应的告警。
 
 
当Diameter模块中的数据区和各项资源（路由、链路和承载）使用率低于下个级别告警门限时，恢复本级别的告警，上报下个级别的告警；使用率低于“告警恢复门限”时，该类型告警恢复。
 
 
## SET DIMTHRESH 
## SET DIMTHRESH 
命令功能 : 
该命令用于修改Diameter告警门限配置。在部署RCP网元的时候可以综合系统容量和性能要求执行该命令，设定数据区和各项资源（路由、链路和承载）的各级使用率告警阈值。 
注意事项 : 
无。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LOADTYPE|负荷类型|参数可选性:必选参数；参数类型:枚举。参见枚举定义。|该参数用于设置告警门限的负荷类型：数据区、路由、链路和承载。DATA：数据区，Diameter消息收发过程中使用。ROUTE：路由，根据Diameter消息可匹配的特定通路。LINK：链路，传递Diameter消息的Diameter链路。BEARER：承载，运行Diameter消息的偶联。
OTH1|1级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到一级告警的阈值。数据区一级告警阈值的默认值是70；路由、链路和承载一级告警阈值的默认值是100。
OTH2|2级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到二级告警的阈值。数据区二级告警阈值的默认值是60；路由、链路和承载二级告警阈值的默认值是85。2级告警门限值必须小于1级告警门限值。
OTH3|3级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到三级告警的阈值。数据区三级告警阈值的默认值是55；路由、链路和承载三级告警阈值的默认值是75。3级告警门限值必须小于2级告警门限值。
OTH4|4级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到四级告警的阈值。数据区四级告警阈值的默认值是50；路由、链路和承载四级告警阈值的默认值是70。4级告警门限值必须小于3级告警门限值。
DTH|告警恢复门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置恢复告警的阈值。数据区告警恢复的默认值是45；路由、链路和承载告警恢复的默认值是65。告警恢复门限值必须小于4级告警门限值。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LOADTYPE|负荷类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置告警门限的负荷类型：数据区、路由、链路和承载。DATA：数据区，Diameter消息收发过程中使用。ROUTE：路由，根据Diameter消息可匹配的特定通路。LINK：链路，传递Diameter消息的Diameter链路。BEARER：承载，运行Diameter消息的偶联。
OTH1|1级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到一级告警的阈值。数据区一级告警阈值的默认值是70；路由、链路和承载一级告警阈值的默认值是100。
OTH2|2级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到二级告警的阈值。数据区二级告警阈值的默认值是60；路由、链路和承载二级告警阈值的默认值是85。2级告警门限值必须小于1级告警门限值。
OTH3|3级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到三级告警的阈值。数据区三级告警阈值的默认值是55；路由、链路和承载三级告警阈值的默认值是75。3级告警门限值必须小于2级告警门限值。
OTH4|4级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到四级告警的阈值。数据区四级告警阈值的默认值是50；路由、链路和承载四级告警阈值的默认值是70。4级告警门限值必须小于3级告警门限值。
DTH|告警恢复门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置恢复告警的阈值。数据区告警恢复的默认值是45；路由、链路和承载告警恢复的默认值是65。告警恢复门限值必须小于4级告警门限值。
命令举例 : 
修改Diameter告警门限配置：负荷类型为“数据区”，1级告警门限为“90”： 
SET DIMTHRESH:LOADTYPE="DATA",OTH1=90 
## SHOW DIMTHRESH 
## SHOW DIMTHRESH 
命令功能 : 
该命令用于查询Diameter告警门限配置，可查询数据区和各项资源（路由、链路和承载）的各级使用率告警阈值配置。 
注意事项 : 
无。 
输入参数说明 : 
标识|名称|类型|说明
---|---|---|---
LOADTYPE|负荷类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置告警门限的负荷类型：数据区、路由、链路和承载。DATA：数据区，Diameter消息收发过程中使用。ROUTE：路由，根据Diameter消息可匹配的特定通路。LINK：链路，传递Diameter消息的Diameter链路。BEARER：承载，运行Diameter消息的偶联。
输出参数说明 : 
标识|名称|类型|说明
---|---|---|---
LOADTYPE|负荷类型|参数可选性:任选参数；参数类型:枚举。参见枚举定义。|该参数用于设置告警门限的负荷类型：数据区、路由、链路和承载。DATA：数据区，Diameter消息收发过程中使用。ROUTE：路由，根据Diameter消息可匹配的特定通路。LINK：链路，传递Diameter消息的Diameter链路。BEARER：承载，运行Diameter消息的偶联。
OTH1|1级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到一级告警的阈值。数据区一级告警阈值的默认值是70；路由、链路和承载一级告警阈值的默认值是100。
OTH2|2级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到二级告警的阈值。数据区二级告警阈值的默认值是60；路由、链路和承载二级告警阈值的默认值是85。2级告警门限值必须小于1级告警门限值。
OTH3|3级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到三级告警的阈值。数据区三级告警阈值的默认值是55；路由、链路和承载三级告警阈值的默认值是75。3级告警门限值必须小于2级告警门限值。
OTH4|4级告警门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置负荷达到四级告警的阈值。数据区四级告警阈值的默认值是50；路由、链路和承载四级告警阈值的默认值是70。4级告警门限值必须小于3级告警门限值。
DTH|告警恢复门限（%）|参数可选性:任选参数；参数类型:整数；参数范围为:0~100。|该参数用于设置恢复告警的阈值。数据区告警恢复的默认值是45；路由、链路和承载告警恢复的默认值是65。告警恢复门限值必须小于4级告警门限值。
命令举例 : 
查询Diameter告警门限的命令： 
SHOW DIMTHRESH; 
