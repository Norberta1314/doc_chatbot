# ZUF-77-01 移动性管理 
概述 : 
功能描述 : 
移动性管理功能用来控制MS在2/3G下的接入，以及跟踪MS当前的位置信息，即MS当前所在的RA、所在SGSN等信息。移动性管理功能主要通过附着、分离、路由区更新等流程来实现。这些流程保证了在MS移动的时候，相关网络实体中MS位置信息的及时更新。 
移动性管理通过记录不同的用户状态之间的切换，来表征用户不同的业务活动。 
2G接入下，用户状态包括IDLE、STANDBY和READY。 
3G接入下，用户状态包括PMM-DETACHED 、PMM-IDLE和PMM-CONNECTED。 
图1  2G接入下MS/网络侧状态转化图
2G接入下各用户状态说明参见下表。 
状态名称|说明
---|---
IDLE|MS没有附着在网上，MS与SGSN之间未建立MM上下文，网络不知道MS的位置信息。
STANDBY|MS已经附着在网上，MS与SGSN之间建立了MM上下文，MS的位置精确到RAI，该状态下MS可以被寻呼，但该状态下不能发送和接受数据。
READY|MS已经附着在网上，MS与SGSN之间建立了MM上下文，MS的位置精确到小区，该状态下MS可以接收和发送数据，不存在GPRS的寻呼，但其它业务的寻呼可通过SGSN下发。
图2  3G接入下MS/网络侧状态转化图
3G接入下各用户状态说明参见下表。 
状态名称|说明
---|---
PMM-DETACHED|MS没有附着在网上，MS与SGSN之间未建立MM上下文，网络不知道MS的位置信息。
PMM-IDLE|MS已经附着在网上，MS与SGSN之间建立了MM上下文，MS的位置精确到RAI，该状态下MS可以被寻呼，但该状态下不能发送和接受数据。
PMM-CONNECTED|MS已经附着在网上，MS与SGSN之间建立了MM上下文，SGSN中MS的位置精确到SAI，该状态下MS可以接收和发送数据，同样该状态下没有PS寻呼的概念。
功能特性简介 : 
为了应对各种场景下用户状态切换，以及位置变化，核心网提供了多种有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
附着|Gn/Gp SGSN网元附着流程是2/3G用户注册到PS域的基本过程，为后续用户进行PS域业务做好准备。在附着过程中，Gn/Gp SGSN可以对UE进行鉴权和认证，确定用户有使用PS业务的授权。同时还可以协商加密的算法和完整性保护算法，对用户的信令和数据进行加密和完整性保护。附着接受时网络侧分配给用户一个临时标识P-TMSI，避免用户的IMSI在空口频繁暴露，从而降低用户的IMSI被盗用/跟踪的风险。附着完成之后，用户可以进行PS域的业务（如短消息），用户可以在激活PDP后进行数据业务。|ZUF-77-01-001 Attach
分离|Gn/Gp SGSN网元分离流程是2/3G用户在PS域去注册的基本过程，用户分离后，所有的PS业务将不可用，网络侧无法感知到用户的位置。在分离完成后，SGSN应该删除用户所有的PDP，PS数据业务和其它PS业务都不可用。如果要进行PS的数据业务和其它的PS业务，那么用户必须再次发起附着。|ZUF-77-01-002 Detach
Purge|Purge功能指的是SGSN删除MM和PDP上下文（包括签约信息和鉴权集等），并通知HLR。当MS从网络分离后，SGSN可保留MS的信息（包括鉴权信息）一段时间。如果MS在这段时间内再次访问网络，MS无需访问HLR。|ZUF-77-01-003 Purge
RAT内路由区更新|Gn/Gp SGSN网元RAU流程是2/3G用户注册到PS域后，移动性管理中的一个基本流程，用于终端告知网络侧终端所在的位置，保证网络侧时刻知道用户最新的位置。在RAU过程中，Gn/Gp SGSN可以对MS进行重新鉴权和认证，同时还可以协商加密的算法和完整性保护算法，对用户的信令和数据进行保护。另外，支持在RAU流程完成时网络侧分配给用户一个临时标识P-TMSI。|ZUF-77-01-004 RAT内RA更新
RAT间路由区更新|根据网络类型，跨RAT路由区更新分为以下类型：3G和2G间RA更新4G和3G间RA更新4G和2G间RA更新在RAU过程中，Gn/Gp SGSN可以对MS进行重新鉴权和认证，同时还可以协商加密的算法和完整性保护算法，对用户的信令和数据进行保护。另外，支持在RAU流程完成时网络侧分配给用户一个临时标识P-TMSI。|ZUF-77-01-005 跨RAT RA更新
业务请求|Gn/Gp SGSN网元业务请求流程是3G用户在PS域从PMM-IDLE状态转变为PMM-CONNECTED状态，建立Iu连接过程，为后续用户进行PS域业务做建立无线连接的过程。如果业务请求的类型为数据类型，那么还需要为用户建立无线承载。在业务请求过程中，需要对UE进行鉴权和认证，确定用户身份的合法性。同时还要协商加密的算法和完整性保护算法，对用户的信令和数据进行保护业务请求完成之后，用户可以与网络侧进行信令交互，用户可以进行PS域的业务（如短消息），用户可以进行数据业务。|ZUF-77-01-006 业务请求
寻呼|Gn/Gp SGSN网元寻呼流程是2/3G用户在PS域有下行数据或者信令发送的时候，用户状态为PMM-IDLE或者STANDBY态时发生的流程。寻呼成功之后可以把用户状态迁移到PMM-CONNECTED或者READY状态，Gn/Gp SGSN知道用户所在的最新小区或者服务区。Iu接入时，UE使用寻呼类型的Service Request作为寻呼响应。Gb接入时，UE使用上行数据帧作为寻呼响应。寻呼完成之后，用户的状态为PMM-CONNECTED或者READY。|ZUF-77-01-007 寻呼
用户数据管理|当HLR上的用户数据发生变化，HLR发送插入用户数据（Insert Subscriber Data）消息给SGSN。SGSN处理用户数据变化，并发送插入用户数据响应（Insert Subscriber Data Ack）消息给HLR。|ZUF-77-01-008 用户数据管理
Suspend|若UE附着到2G网络并且支持DTM模式，当UE发起语音业务时，UE发送Suspend消息通知SGSN暂停其数据业务。当用户完成语音业务并返回PS域后，SGSN立即恢复该UE的数据业务。|ZUF-77-01-009 Suspend
## ZUF-77-01-001 Attach 
特性描述 : 
摘要描述应用场景客户收益实现原理遵循标准特性能力O&M相关 
描述 : 
定义
GnGp SGSN网元附着流程是2/3G用户注册到PS域的基本过程，为后续用户进行PS域业务做好准备。 
在附着过程中，GnGp SGSN可以对UE进行鉴权和认证，确定用户有使用PS业务的授权。同时还可以协商加密的算法和完整性保护算法，对用户的信令和数据进行加密和完整性保护。附着接受时网络侧分配给用户一个临时标识P-TMSI，避免用户的IMSI在空口频繁暴露，从而降低用户的IMSI被盗用/跟踪的风险。 
Gb接入时，GnGp SGSN可以对用户进行鉴权；可以通知BSS建立分组流上下文。 
Iu接入时，GnGp SGSN可以对用户进行鉴权，同时用户可以对网络侧鉴权，即GnGp SGSN与用户之间可以进行双向鉴权。 
附着完成之后，用户可以进行PS域的业务（如短消息），用户可以在激活PDP后进行数据业务。 
背景知识
GPRS网络架构图，如[图1]所示，其中包含了如下网元：
图1  GPRS架构图
各网元功能如下： 
TE/MT（Terminal Equipment/Mobile Terminal，终端设备/移动终端）：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS（Base Station System，基站系统）：GPRS/EDGE（2G）的无线接入网络，为终端的接入提供无线资源。
UTRAN（UMTS Terrestrial Radio Access Network，统一的陆地无线接入网络）：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
HLR（Home Location Register），归属位置寄存器）:永久存储用户签约数据。 
PDN（Packet Data Network，分组数据网）：为用户提供业务的网络。 
CGF（Charging Gateway Functionality，计费网关功能）：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS（Billing System，计费系统）：负责接收和处理从核心网发送过来的CDR文件。 
EIR（equipment identity register 设备标识寄存器）：负责检查UE设备。 
SGSN（Serving GPRS Support Node，服务GPRS支持节点）：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS
Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息； 
MSC/VLR（Mobile Switch Center/ Visitor Location Register，移动交互中心/拜访位置寄存器）：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMS GMSC/SMS IWMSC （Short Message Service Gateway MSC/ Short
Message Service Interworking MSC，短消息网管移动交换中心/短消息互通移动交换中心）：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL （Customised Applications for Mobile network Enhanced
Logic，移动网络定制应用增强逻辑服务器）：该功能实体主要对用户进行在线计费。 
应用场景 : 
GnGp SGSN网元附着流程是基本流程，用户要使用PS业务，必须先注册到PS网络，用户通过附着流程完成注册过程。常见场景包括： 
UE插入新的SIM/USIM卡之后，开机自动PS域附着。 
用户开机后，手动PS域附着。 
用户拔电池后，重新插入电池开机自动PS域附着。 
客户收益 : 
受益方|受益描述
---|---
运营商|支持合法的本地用户和漫游用户注册到运营商的PS网络上后，激活PDP上下文，使运营商可以为用户提供数据业务相关服务，如：邮件、网页浏览、流媒体等。
移动终端用户|为数据业务做好准备
实现原理 : 
涉及的网元
GnGp SGSN网元附着流程主要需要UE、BSS/RNC、SGSN、HLR、EIR（可选）、GGSN（可选）、CAMEL（可选）、MSC/VLR（可选）的共同配合，各网元在附着过程中具体功能为： 
UE：触发附着流程，完成安全功能，存储用户临时标识（P-TMSI）、移动性管理状态、用户安全参数等。 
BSS：对用户进行接入层安全功能，完成SGSN的选择，完成对用户无线资源管理功能，透传UE和SGSN之间的NAS层移动性管理消息。 
RNC：对用户进行接入层安全功能，完成SGSN的选择，完成对用户无线资源管理功能，透传UE和SGSN之间的NAS层移动性管理消息。 
SGSN：对用户进行接入控制和安全功能，完成用户临时标识（P-TMSI）的分配，完成HLR的选择。 
HLR：把用户的签约数据插入到SGSN，同时生成用户进行鉴权的鉴权向量，记录用户的位置信息，当发生用户的被叫业务的时候，能够从HLR中获取到用户注册的SGSN地址和号码。 
EIR：验证手机的合法性，是否处于黑名单或者灰名单列表中。 
GGSN：由SGSN触发，清除用户在该GGSN上遗留PDP上下文信息。 
CAMEL：控制附着流程是否可以继续执行。 
MSC/VLR：在联合附着过程中，通过PS域中转进行CS域的位置更新/注册，并维护IMSI和SGSN之间的对应关系。 
业务流程
附着流程如[图2]所示。
图2  附着流程
UE发送Attach Request消息到SGSN，携带附着类型、IMSI或者PTMSI+OldRAI、手机的网络能力、手机的无线接入能力、DRX、PTMSI
signature等参数。 
如果UE携带了PTMSI+OldRAI，SGSN判断RAI不是本局管理的，或者SGSN支持SGSN Pool时从PTMSI取出NRI，SGSN判断NRI不是本局分配的，SGSN根据Old
RAI或者NRI找到Old SGSN，向Old SGSN发送Identification Request消息。Old SGSN收到消息后，如果找到了用户则返回Identification
Response并携带IMSI，如果没有找到则返回Identification Response消息并携带失败原因值。 
如果SGSN没有从Old SGSN获取到IMSI，并且本SGSN也没有找到用户的IMSI，那么SGSN发送Identity
Request消息给UE，携带的Identity Type参数值为IMSI，获取UE的IMSI。UE返回Identity Response消息携带IMSI。 
SGSN发起Security Function流程。如果是UTRAN接入，还要发起到RNC的Security mode流程，进行加密和完整性保护的协商。如果网络中任何一处都找不到这个UE的MM上下文，那么鉴权则是强制的。Security
Function包括：从HLR获取鉴权向量、和UE进行鉴权消息交互、和RNC进行Security Mode过程。 
SGSN对UE进行检查，执行Identity Check过程。包括：从UE获取IMEI（如果鉴权流程没有获取到IMEISV）、到EIR进行IMEI校验。 同时如果SGSN存在UE的PDP上下文，那么发送Delete PDP Context Request到GGSN，GGSN返回Delete
PDP Context Response消息，SGSN删除UE的PDP上下文。 
如果是首次附着、SGSN发生了改变、执行了ADD（Automatic Device Detection）功能、IMEISV发生了改变、UE提供了一个IMSI，或者UE提供了一个不是指向SGSN有效MM上下文的old
P-TMSI/RAI，那么SGSN发送Update Location消息到HLR。 
HLR收到了Update Location消息，向Old SGSN发送Cancel Location消息，通知Old
SGSN用户到了其它SGSN，Old SGSN删除用户的PDP上下文和MM上下文。 
old SGSN回复Cancel Location ACK。若old SGSN中这个UE有正在进行的处理，那么old
SGSN要等这些进程完成之后才能删除MM和PDP上下文。 
如果在这个SGSN内存在激活的PDP上下文，则old SGSN向相关的GGSN（s）分别发送Delete PDP Context
Request删除这些上下文； 
GGSN（s）回复Delete PDP Context Response消息。 
HLR发送Insert Subscriber Data消息给new SGSN，插入用户的签约数据到SGSN。 
如果由于区域签约限制或是接入限制，不允许UE在这个RA内附着，则SGSN拒绝这个附着请求，回复Insert Subscriber
Data ACK； 
由于签约检查失败或是其他原因，SGSN拒绝附着请求，回复Insert Subscriber Data ACK； 
Iu接入时，如果网络支持网络共享的MOCN配置，但是UE不是一个支持网络共享的UE，这种情况下SGSN会通过发送Attach
Reject消息，同时在下行消息的AS层携带Redirection Indication参数给RNS，要求RNS发起redirection； 
所有检查通过，SGSN为这个UE创建一个MM上下文，并返回一个Insert Subscriber Data ACK消息。 
在旧的MM上下文删除并且新的MM上下文被创建后，HLR向SGSN返回Update Location Ack。如果Update
Location被HLR拒绝了，则SGSN会携带合理的原因拒绝这个附着请求。 
如果步骤1中附着类型为联合附着或者是IMSI附着完成的GPRS附着，则需要更新VLR，如果SGSN能够提供RAN节点到多CN节点的多区域连接功能，则VLR
number从RAI中获得；如果不能提供该功能，SGSN使用从IMSI得到的RAI以及hash value确定VLR number。SGSN根据用户当前的位置区找到了关联的MSC/VLR发送Update
Location消息到MSC/VLR. 
如果MSC/VLR发生了改变，MSC/VLR发送位置更消息到HLR； 
HLR向Old MSC/VLR发送Cancel Location消息，通知Old MSC/VLR用户到了其它MSC/VLR； 
Old MSC/VLR删除用户的MM上下文。Old VLR回复Cancel Location Ack消息。 
HLR插入用户签约数据到MSC/VLR，发送Insert Subscriber Data消息。 
MSC/VLR返回Insert Subscriber Data ACK消息 
HLR返回Update Location Ack给MSC/VLR。 
MSC/VLR返回Update Location Ack消息到SGSN携带VLR TMSI。 
Iu接入时，如果MSC/VLR返回位置更新失败或者SGSN无法获取MSC/VLR并且网络支持网络共享的MOCN配置，但是UE不是一个支持网络共享的UE，这种情况下SGSN会通过发送Attach
Reject消息同时在下行消息的AS层携带Redirection Indication参数Reject Cause Value为CS/PS
coordination required给RNS，要求RNS发起redirection； 
SGSN发送Attach Accept消息给UE，携带PTMSI、VLR TMSI（可选）、PTMSI Signature等参数。 
UE发现PTMSI或者VLR TMSI发生了变化，返回Attach Complete消息给SGSN，来确认已经收到了TMSI号码。 
如果分配了VLR TMSI给UE，SGSN发送TMSI Reallocation Complete消息到VLR，通知VLR，VLR
TMSI分配完成。 
在步骤8完成后，有一个CAMEL检查点C1： 
如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起CAMEL_GPRS_Attach and CAMEL_PS_Notification过程，返回”continue”，则流程继续，否则附着流程失败，发送Attach
Reject消息给UE； 
如果该用户签约了CAMEL，但是SGSN未配置Ge口，则检查CAMEL签约数据中的默认处理，如果是”continue”，则流程继续，否则附着流程失败，发送Attach
Reject消息给UE； 
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060 "General Packet Radio Service （GPRS）; Service
description; Stage 2". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service （GPRS）; Base
Station System （BSS） - Serving GPRS Support Node （SGSN）; BSS GPRS
Protocol （BSSGP）". 
3GPP TS 29.060: "General Packet Radio Service （GPRS）; GPRS
Tunnelling Protocol （GTP） across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part （MAP） specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
用户附着流程完成后，会在GnGp
SGSN中创建一个MM上下文，用于临时保存用户相关信息。 
O&M相关 : 
性能统计
性能计数器参见 [表2].
测量类型名称|性能计数器名称
---|---
SGSN附着测量（UMTS）|编号为C40576开头的所有计数器
SGSN路由区附着测量（UMTS）|编号为C40530开头的所有计数器
SGSN附着测量（GSM）|编号为C40575开头的所有计数器
SGSN路由区附着测量（GSM）|编号为C40531开头的所有计数器
话单与计费
SGSN附着的时候导致PDP去激活出S-CDR话单。 
特性配置 : 
摘要配置特性测试用例 
配置特性 : 
配置前提
本文以Iu口配置为例，给出了附着流程的基本配置。 
该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置就可以，比如SGSN的本局配置，与HLR的对接配置等。 
该配置的数据准备： 不同局间的交互需要提前协商下数据配置，如不同的RA对应不同的SGSN，SGSN根据MS带上来的信息能正确判断MS是否第一次附着或者是否以前曾在该SGSN附着过。通过信息交互以保证MS到SGSN的通信，SGSN之间，SGSN到GGSN之间的通信等。已经新增了本局信令点和本局配置。具体来说： 
SGSN里配置的是静态偶联，允许不同的RNC接入。 
SGSN里配置的RA包含MS所处的RA。 
所有的RA都能正确解析到对应的SGSN。 
不同RNC或SGSN之间的通信，在SGSN地址解析里有相应的配置。 
配置过程
M3UA连接建立过程
在EM客户端的配置页面的左侧命令树中，展开网元节点，选择CommonS_SIG_0节点。
使用命令[ADD ADJOFC]建立邻接局。
使用命令[ADD M3UASCTP]新增SCTP。
使用命令[ADD M3UAASP]新增ASP。
使用命令[ADD M3UAAS]新增AS。
使用命令[ADD M3UART]配置M3UA静态路由。
使用命令[ADD SIOLOCAS]新增SIO定位AS。
在EM客户端的配置页面的左侧命令树中，展开网元节点，选择NFS_MMESGSN_0节点。
使用命令[ADD RNC]建立RNC局。
使用命令[ADD ADJOFCIDCFG]添加局向属性。
使用命令[ADD IROAM]新增移动号码分析结果索引。
使用命令[ADD MDNAL]新增移动号码分析。
使用命令[ADD GTT]新增GT翻译选择子。
使用命令[ADD GT]新增GT翻译数据。
使用命令[ADD LAI]增加SGSN管理的LA。
使用命令[ADD RAI]增加SGSN管理的RA。
SGSN配置更新过程
在EM客户端的配置页面的左侧命令树中，选择网元节点，使用命令[SYNA]同步前后台数据。
跨局附着选择SGSN过程
使用本地地址解析配置在EM客户端的配置页面的左侧命令树中，展开网元节点，选择NFS_MMESGSN_0节点，使用命令ADD SGSNHOST增加新局SGSN地址解析。 
使用DNS地址解析配置使用命令SET DNS GLB设置DNS的全局参数。使用命令ADD DNS SERVER增加DNS地址。 
配置实例
M3UA连接建立过程.配置步骤配置说明ADD ADJOFC:OFFICEID=1,NETWORKNAME="RNC21",SPCMODE="TRIPLE_DEC",DPC="1.21.1",NET=1,SPTYPE="STEP",SSF="NATIONAL",SPCTYPE="24",AM="AM_SURE",PROT="CHINA",BANDFLAG="NO",SUBPROT="DEFAULT",RELATEOFFICEID1=0,RELATEOFFICEID2=0,RELATEOFFICEID3=0,RELATEOFFICEID4=0配置邻接局RNCADD SCTP:ID=21,NAME="RNC21",LOCPORT=10021,REMPORT=10021,VPNID1=0,LOCADDR1=40.1.136.248,REMADDR1=40.1.136.21,ROLE="CLT",PROTOCALTYPE="M3UA"ADD M3UASCTP:ASSOCID=21,SCTPPROTYPE="M3UA",OFFICEID=1增加RNC的SCTP配置ADD M3UAASP:ASPID=21,NAME="RNC21",ASSOCID=21增加ASP配置ADD M3UAAS:ASID=21,NAME="RNC21",EXISTCONTEXT="YES",PROTOCOL="M3UA",CONTEXTID=0,TAG="CLT",ASUPTYPE="SCCP",ASPID1=21增加AS配置ADD M3UART:ROUTEID=21,ALIAS="RNC21",ASID1=21M3UA静态路由配置ADD SIOLOCAS:DROUTEID=21,ALIAS="RNC21",DSTOFFICEID=21,SIO="SCCP",ROUTEID1=21SIO定位AS配置ADD RNC:RNCOFFID=1,MCC="460",MNC="03",RNC=111添加RNCADD ADJOFCIDCFG:OFCID=1,OFCTYPE="RNC"添加邻接局索引ADD IROAM:IDX=1,TP="HLR",RST="8613900018",NAME="HLR18"号码分析索引ADD MDNAL:DGT="46003",ENTR="DAS_IMSI_ROAM",RST=1,
NAME="HLR18"移动号码分析ADD GTT:PLAN="E.164",NATURE="INT",ID=1,NAME="HLR18"GT翻译选择子ADD GT:GT="8613900018",GTSL=1,OFCIDS=18-1ADD GT:GT="861390511",GTSL=1,OFCIDS=0-1GT翻译数据ADD LAI:NAME="1521",MCC="460",MNC="03",LAC="1521"ADD LAI:NAME="1522",MCC="460",MNC="03",LAC="1522"增加LA配置ADD RAI:NAME="152101",LAI="1521",RAC="01"ADD RAI:NAME="152201",LAI="1522",RAC="01"增加RA配置 
SGSN配置更新过程配置步骤配置说明SYNA:STYPE="CHG"同步前后台数据 
跨局附着选择SGSN过程配置步骤配置说明ADD SGSNHOST:NAME="rac0001.lac6101.mnc003.mcc460.gprs",
IPADDR="200.61.1.159"增加SGSN地址解析ADD DNS SERVER:ID=1,SERVERIPADDR=192.18.0.177,CLIENTIPADDR=40.1.136.1,VRFID=11增加DNS服务器地址，DNS解析时使用 
测试用例 : 
测试项目|GPRS附着
测试目的|验证SGSN对GPRS附着的处理
预置条件|系统运行正常，移动用户已在HLR中签约登记
测试过程|MS自动注册或手工搜索到网络（2/3G）后注册
通过准则|附着成功（从SGSN信令跟踪看有完整消息）
## ZUF-77-01-002 Detach 
特性描述 : 
摘要描述应用场景客户收益实现原理系统影响特性交互遵循标准特性能力O&M相关 
描述 : 
定义
Gn/Gp SGSN网元分离流程是2/3G用户在PS域去注册的基本过程，用户分离后，所有的PS业务将不可用，网络侧无法感知到用户的位置。
在分离完成后，SGSN应该删除用户所有的PDP，PS数据业务和其它PS业务都不可用。如果要进行PS的数据业务和其它的PS业务，那么用户必须再次发起附着。
背景知识
GPRS的网络架构如[图1]所示。
图1  GPRS架构图
包含了如下网元： 
TE/MT（Terminal Equipment/Mobile Terminal，终端设备/移动终端）：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS（Base Station System，基站系统）：GPRS/EDGE（2G）的无线接入网络，为终端的接入提供无线资源。 
UTRAN（UMTS Terrestrial Radio Access Network，统一的陆地无线接入网络）：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
HLR（Home Location Register，归属位置寄存器）:永久存储用户签约数据。 
PDN（Packet Data Network，分组数据网）：为用户提供业务的网络。 
CGF（Charging Gateway Functionality，计费网关功能）：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS（Billing System，计费系统）：负责接收和处理从核心网发送过来的CDR文件。 
EIR（Equipment Identity Register，设备标识寄存器）：负责检查UE设备。 
PSCN（Packet Switched Core Network，分组交换核心网）：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元： 
SGSN（Serving GPRS Support Node，服务GPRS支持节点）：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS
Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息。 
GGSN（Gateway GPRS Support Node，GPRS支持节点网关）：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
MSC/VLR（Mobile Switch Center/ Visitor Location Register，移动交互中心/拜访位置寄存器）：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMSGMSC/SMS IWMSC （Short Message Service Gateway MSC/ Short Message Service Interworking
MSC，短消息网管移动交换中心/短消息互通移动交换中心）：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL （Customised Applications for Mobile network Enhanced Logic，移动网络定制应用增强逻辑服务器）：该功能实体主要对用户进行在线计费。 
应用场景 : 
SGSN网元分离流程是基本流程，是用户在PS域去注册的基本流程。具体常见场景包括： 
手机关机。 
用户取消PS签约。 
用户使用完PS业务后，手动发起分离。 
SGSN主动发起分离。 
客户收益 : 
客户收益参见[表1]。
受益方|受益描述
---|---
运营商|用户分离后删除用户的PDP上下文资源和其它资源，可以把资源分配给其它用户。提高了运营商的网络用户接入成功率。
移动终端用户|终端用户删除PDP上下文和MM上下文，在PS域去注册，节省了使用PS业务带来的费用，节省电池电量消耗。
实现原理 : 
各网元作用
SGSN网元分离流程需要UE、BSS/RNC、SGSN、GGSN的共同配合，各网元在分离过程中具体功能包括： 
UE：触发PS域的去注册，完成UE的PDP上下文和MM上下文的删除。 
BSS：对用户建立的无线资源进行删除，透传UE和SGSN的NAS消息。 
RNC：对用户建立的无线承载资源进行释放，透传UE和SGSN的NAS相关消息。 
SGSN：可以作为分离的发起者和执行者，用户分离的时候释放用户的PDP资源，设置用户状态为分离状态；用户Gb接入时，可以对用户进行鉴权，可以通知BSS删除分组流上下文；用户Iu接入时，通知RNC删除无线承载，通知GGSN删除PDP上下文。 
GGSN：删除PDP上下文。 
HLR：可以作为分离流程的发起者。 
MSC/VLR：处理IMSI分离，GPRS分离时VLR删除与SGSN的关联，后续CS寻呼和位置更新不经过SGSN进行。 
业务流程
MS发起的分离流程
MS发起的分离流程如[图2]所示。
图2  MS发起分离流程
流程说明： 
SGSN收到了MS发送的Detach Request消息，携带Detach Type、PTMSI、PTMSI Signature、Switch
Off等参数。Detach Type用来说明支持是什么类型的分离，PTMSI Signature签名用来检查这条Detach Request消息的有效性，如果PTMSI
Signature无效或者不包含该参数，那么网络侧需要对MS进行鉴权。Switch off用来指出是否是关机造成的detach。 
如果分离类型为GRPS分离并且和这个MS相关的GGSN存在PDP上下文，那么SGSN发送Delete PDP Context
Request通知GGSN删除PDP上下文，SGSN收到了GGSN返回的Delete PDP Context Response消息后删除自己的PDP上下文。 
如果分离类型为IMSI detach并且用户建立了Gs口关联， SGSN发送IMSI Detach Indication消息到VLR。 
如果MS想保持IMSI附着执行GPRS分离的话， 则SGSN发送GPRS Detach Indication消息到VLR，VLR删除与SGSN的association，CS寻呼和位置更新不经过SGSN进行。 
如果Switch Off指示不是关机造成的detach，SGSN发送Detach Accept消息到MS。 
如果MS是GPRS detach，则3G接入的时候SGSN释放PS信令连接。 
HLR发起的分离流程
HLR发起的分离流程如[图3]所示。
图3  HLR发起的分离流程
流程说明： 
如果HLR想立即删除用户的MM和PDP上下文，HLR发送Cancel Location （IMSI, Cancellation
Type）消息到SGSN， Cancellation Type设置为Subscription Withdrawn. 
SGSN发送Detach Request （Detach Type） 给MS，Detach Type指出MS不需发起新的附着以及PDP上下文激活。 
如果用户存在PDP上下文，SGSN发送Delete PDP Context Request消息到GGSN，通知GGSN删除PDP上下文，GGSN返回给SGSN
Delete PDP Context Response消息，SGSN删除用户的PDP上下文。 
如果MS是IMSI和GPRS联合附着的话， SGSN发送GPRS Detach Indication消息到VLR。VLR删除与SGSN的association，CS寻呼和位置更新不经过SGSN进行。 
MS在step2后任意一个时间发送Detach Accept消息给SGSN。 
SGSN发送Cancel Location Ack消息到HLR，确认删除了MM和PDP上下文。 
在接收到Detach Accept消息后，如果Detach Type不请求MS发起一个新的附着，则3G接入的时候SGSN释放PS信令连接。 
SGSN发起的分离流程
SGSN发起的分离流程如[图4]所示。
图4  SGSN发起的分离流程
流程说明： 
SGSN发送Detach Request （Detach Type） to the MS. Detach Type 指出MS是否需要发起新的附着以及PDP上下文激活。 
如果用户存在PDP上下文，SGSN发送Delete PDP Context Request消息到GGSN，通知GGSN删除PDP上下文，GGSN返回给SGSN
Delete PDP Context Response消息，SGSN删除用户的PDP上下文。 
如果MS是IMSI和GPRS联合附着的话， SGSN发送GPRS Detach Indication消息到VLR。VLR删除与SGSN的association，CS寻呼和位置更新不经过SGSN进行。 
MS在step2后任意一个时间发送Detach Accept消息给SGSN。 
在接收到Detach Accept消息后，如果Detach Type不请求MS发起一个新的附着，则3G接入的时候SGSN释放PS信令连接。 
系统影响 : 
随着分离用户数的增加，系统资源占用会一直减小，CPU占用率会相应下降。 
特性交互 : 
由于分离流程是基本业务流程，用户分离后PS相关的业务都无法使用。 
特性交互参见[表2]。
业务|交互
---|---
分离与计费|用户分离后会产生M-CDR和S-CDR话单。
遵循标准 : 
本特性的遵循标准如下： 
3GPP TS 23.060 "General Packet Radio Service （GPRS）; Service
description; Stage 2". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service （GPRS）; Base
Station System （BSS） - Serving GPRS Support Node （SGSN）; BSS GPRS
Protocol （BSSGP）". 
3GPP TS 29.060: "General Packet Radio Service （GPRS）; GPRS
Tunnelling Protocol （GTP） across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part （MAP） specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
用户附着流程完成后，创建了一个MM上下文。用户分离后，能够保持用户的上下文一段时间，而不是立即删除。 
O&M相关 : 
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
SGSN分离测量|编号为C40579开头的所有计数器
CDRs and Billing
GSN分离的时候可以根据需要输出MCDR话单。 
特性配置 : 
摘要Gn/Gp SGSN网元分离流程配置测试用例 
#### Gn/Gp SGSN网元分离流程配置 
配置说明
该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置即可。 
配置前提
不同局间的交互需要提前协商数据配置，如不同的RA对应不同的SGSN。通过信息交互以保证MS到SGSN的通信，SGSN与SGSN之间，SGSN到GGSN之间的通信等。 
已经新增了本局信令点和本局配置。 
配置过程
SGSN里配置的是静态偶联，允许不同的RNC接入。 
SGSN里配置的RA包含MS所处的RA。 
所有的RA都能正确解析到对应的SGSN。 
不同RNC或SGSN之间的通信，在SGSN地址解析里有相应的配置。 
测试用例 : 
测试项目|GPRS附着用户发起正常分离
---|---
测试目的|验证网络侧能否正常处理用户发起的GPRS分离。
预置条件|系统运行正常，用户正常签约。
测试过程|CONNECTED状态用户发起GPRS分离（非关机）。
通过准则|网络侧返回Detatch acc消息
测试结果|无
## ZUF-77-01-003 Purge 
概述 : 
SGSN删除MM，PDP上下文和其他信息后，通知HLR。 
收益 : 
SGSN通知HLR已删除的分离MS的信息，这样HLR可及时获知MS信息并作出相应的标记。 
描述 : 
Purge功能指的是SGSN删除MM和PDP上下文（包括签约信息和鉴权集等），并通知HLR。当MS从网络分离后，SGSN可保留MS的信息（包括鉴权信息）一段时间。如果MS在这段时间内再次访问网络，MS无需访问HLR。  
## ZUF-77-01-004 RAT内RA更新 
特性描述 : 
摘要描述应用场景客户收益实现原理系统影响特性交互遵循标准特性能力O&M相关 
描述 : 
定义
Gn/Gp SGSN网元RAU流程是2/3G用户注册到PS域后，移动性管理中的一个基本流程，用于终端告知网络侧终端所在的位置，保证网络侧时刻知道用户最新的位置。 
在RAU过程中，Gn/Gp SGSN可以对MS进行鉴权和认证，确定用户有使用PS业务的授权。同时还可以协商加密的算法和完整性保护算法，对用户的信令和数据进行保护。RAU流程完成时网络侧分配给用户一个临时标识P-TMSI。 
Gb接入时，Gn/Gp SGSN可以对用户进行鉴权。 
Iu接入时，Gn/Gp SGSN可以对用户进行鉴权，同时用户可以对网络侧鉴权，即Gn/Gp
SGSN与用户之间可以进行双向鉴权。 
背景知识
GPRS网络架构图如[图1]所示。
图1  GPRS架构图
包含了如下网元： 
TE/MT（Terminal Equipment/Mobile Terminal，终端设备/移动终端）：为终端用户完成各种数据业务和其他业务的载体，负责存储MS相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS（Base Station System，基站系统）：GPRS/EDGE（2G）的无线接入网络，为终端的接入提供无线资源。 
UTRAN（UMTS Terrestrial Radio Access Network，统一的陆地无线接入网络）：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
HLR（Home Location Register，归属位置寄存器）:永久存储用户签约数据。 
PDN（Packet Data Network，分组数据网）：为用户提供业务的网络。 
CGF（Charging Gateway Functionality，计费网关功能）：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS（Billing System，计费系统）：负责接收和处理从核心网发送过来的CDR文件。 
EIR（Equipment Identity Register，设备标识寄存器）：负责检查MS设备。 
PSCN（Packet Switched Core Network，分组交换核心网）：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元： 
SGSN（Serving GPRS Support Node，服务GPRS支持节点）：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS
Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文；负责处理SGSN和MS之间的所有非接入层消息；负责收集用户话单信息。 
GGSN（Gateway GPRS Support Node，GPRS支持节点网关）：负责MS接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
MSC/VLR（Mobile Switch Center/ Visitor Location Register，移动交互中心/拜访位置寄存器）：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMSGMSC/SMS IWMSC （Short Message Service Gateway MSC/ Short Message Service Interworking
MSC，短消息网管移动交换中心/短消息互通移动交换中心）：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL （Customised Applications for Mobile network Enhanced Logic，移动网络定制应用增强逻辑服务器）：该功能实体主要对用户进行在线计费。 
应用场景 : 
SGSN网元RAU流程是基本流程，在用户移动过程中通过RAU流程完成用户位置信息在网络侧的更新。具体常见场景包括： 
用户驻留的RAI发生了改变，MS发起发起RAU流程。 
MS的接入方式发生了改变，MS发起RAU流程。 
MS的周期性RAU定时器超时，MS发起周期性的RAU流程。 
客户收益 : 
客户收益参见[表1]。
受益方|受益描述
---|---
运营商|提高用户满意度。
移动终端用户|用户移动后，无需重新注册，能继续使用PS业务。
实现原理 : 
涉及的网元
SGSN网元路由更新流程需要MS、BSS/RNC、SGSN、HLR（可选）、EIR（可选）、GGSN（可选）、CAMEL（可选）、MSC/VLR（可选）的共同配合，各网元在路由更新过程中具体功能包括： 
MS：触发RAU流程，完成安全功能，更新用户临时标识（P-TMSI）、移动性管理状态、用户安全参数等。 
BSS：对用户进行接入层安全功能，完成SGSN的选择，完成对用户无线资源管理功能，透传MS和SGSN之间的NAS层移动性管理消息。 
RNC：对用户进行接入层安全功能，完成SGSN的选择，完成对用户无线资源管理功能，透传MS和SGSN之间的NAS层移动性管理消息。 
SGSN：对用户进行接入控制和安全功能、位置信息更新、完成用户临时标识（P-TMSI）的分配。 
HLR：把用户的签约数据插入到SGSN，同时生成用户进行鉴权的鉴权向量，记录用户的位置信息，当发生用户的被叫业务的时候，能够从HLR中获取到用户注册的SGSN地址和号码。 
EIR：验证手机的合法性，是否处于黑名单或者灰名单列表中。 
GGSN：由SGSN触发，更新用户在该GGSN上PDP上下文信息。 
CAMEL：控制路由更新流程是否可以继续执行。 
MSC/VLR：通过PS域中转进行CS域的位置更新/注册，并维护IMSI和SGSN之间的对应关系。 
业务流程
SGSN间的RAU流程
SGSN间的RAU流程如[图2]所示。
图2  SGSN间的RAU流程
流程说明如下： 
MS发现RAI发生了改变或者周期性路由更新定时器超时，MS发送Routing Area Update Request
（包括P-TMSI、old RAI、 old PTMSI Signature、 Update Type、 MS Radio Access
Capability、 DRX parameters、MS Network Capability、additional PTMSI/RAI）消息到SGSN，其中Update
Type指出是普通RAU还是周期性RAU。 
SGSN执行鉴权和完整性保护流程，对MS进行鉴权同时和RNC协商完整性保护的算法和密钥。 
SGSN发现MS的RAI发生了改变，SGSN分配新的PTMSI给MS，发送Routing Area Update Accept（包括PTMSI、PTMSI
Signature）给MS。 
如果分配了新的PTMSI，MS返回Routing Area Update Complete消息给SGSN。 
步骤3后，对应图中的C1，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_Routing_Area_Update_Session、
CAMEL_PS_Notification和CAMEL_GPRS_Routing_Area_Update_Context三个检查流程。 
SGSN间的RAU流程
SGSN间的RAU流程如[图3]所示。
图3  SGSN间的RAU流程
 说明： 
本流程以Iu mode为例，Gb mode和本流程类似，只是没有基站与SGSN之间的data forward交互。 
流程说明如下： 
MS建立和RNC之间的RRC连接，MS发送Routing Area Update Request （包括PTMSI、old
RAI、old PTMSI Signature、Update Type、follow on request、MS Radio Access
Capability、DRX Parameters、MS Network Capability、additional P-TMSI/RAI）
消息到new SGSN。如果MS有后续的信令或者数据要发送并且是UMTS接入，MS设置follow-on。 
New SGSN通过Old RAI和old P-TMSI判断是局间RAU，new SGSN发送SGSN Context
Request （包括old PTMSI、old RAI、old PTMSI Signature） 消息到old SGSN来获取MS的MM和PDP上下文。Old
SGSN检查old PTMSI Signature ，返回new SGSN响应带合适原因值：签名不匹配，同时携带IMSI。New SGSN根据原因值决定执行鉴权流程，鉴权成功之后new
SGSN发送SGSN Context Request （包括IMSI、old RAI、MS Validated） 消息到old SGSN。old
SGSN判断鉴权成功，给new SGSN返回成功响应，消息中携带MS的MM和PDP上下文。 
如果MS在old SGSN处于PMM
CONNECTED状态,或者是局内RAU用户处于PMM-CONNECTED状态Iu连接发生改变，old SGSN发送SRNS Context
Request （包括IMSI）消息到old RNC来获取PDP上下文的序列号，在SGSN Context Response消息中带给new
SGSN。收到了该消息，RNC停止发送下行数据开始缓存下行数据，并且返回SRNS Context Response （包括IMSI、GTP
SNDs、GTP SNUs、PDCP SNUs） 消息给old SGSN。 
old SGSN返回SGSN Context Response （包括MM Context、PDP Context）消息给new
SGSN。 
new SGSN执行鉴权和完整性保护流程以及EIR检查。对MS进行鉴权以及和RNC协商完整性检查算法和密钥，并且对终端进行合法性检查。 
new SGSN发送SGSN Context Acknowledge消息到old SGSN。通知old SGSN new
SGSN 已经准备好接收PDP上下文的下行数据。 
对应图中的C1，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_PDP_Context_Disconnection和CAMEL_GPRS_Detach
and CAMEL_PS_Notification两个检查流程。 
如果MS在Old SGSN处于PMM CONNECTED状态，old SGSN发送SRNS Data Forward
Command （包括RAB ID、Transport Layer Address、Iu Transport Association）消息给RNC。RNC设置data-forwarding
定时器. 
对于每个RAB，RNC开始复制和隧道传输缓存的GTP数据到old SGSN。 
old SGSN隧道传输GTP报文到newSGSN。 
如果new SGSN成功创建了PDP，new SGSN发送Update PDP Context Request （包括new
SGSN Address、QoS Negotiated、Tunnel Endpoint Identifier、serving network
identity、CGI/SAI、RAT type、CGI/SAI/RAI change support indication、NRSN）
消息到每个PDP上下文关联的GGSN。 
new SGSN发送Update Location （包括SGSN Number、SGSN Address、IMSI、IMEISV）
消息到HLR更新用户的位置信息。如果支持ADD功能，那么应该携带IMEISV。 
HLR发送Cancel Location （包括IMSI、Cancellation Type）消息到old SGSN，
Cancellation Type设置为Update Procedure。old SGSN删除MM和PDP上下文。Old SGSN发送Iu
Release Command消息到RNC释放Iu连接。连接释放后old SGSN返回Cancel Location Ack （IMSI）消息给HLR。 
如果 data-forwarding 定时器超时、或者数据前传完成，则RNC返回Iu Release Complete消息给old
SGSN。 
在局间RAU过程中，HLR发送Insert Subscriber Data （包括IMSI、subscription
data）消息到new SGSN。new SGSN返回Insert Subscriber Data Ack （包括IMSI、SGSN
Area Restricted） 消息到HLR。 
如果由于区域签约限制或是接入限制，不允许MS在这个RA内注册，则SGSN拒绝这个RAU请求，回复Insert Subscriber
Data ACK。 
由于签约检查失败或是其他原因，SGSN拒绝RAU请求，回复Insert Subscriber Data ACK。 
网络支持网络共享的MOCN功能，但是MS不是一个支持网络共享的MS，这种情况下SGSN会通过发送RAU拒绝消息，同时在下行消息的AS层携带Redirection
Indication参数给RNS，要求RNS发起redirection。 
HLR发送Update Location Ack （包括IMSI、GPRS Subscriber Data）到new
SGSN。 
如果RAU是联合RAU、new SGSN发送Location Update Request （包括new LAI、IMSI、SGSN
Number、Location Update Type）消息到VLR。 
new VLR告知HLR用户的新的位置。HLR插入用户数据到new VLR，并且撤销和old VLR的关联: 
new VLR发送Update Location （包括new VLR） 消息到HLR。 
HLR发送Cancel Location （包括IMSI） 到old VLR，撤销和old VLR的关联。 
old VLR发送Cancel Location Ack （包括IMSI）消息给HLR。 
HLR发送Insert Subscriber Data （包括IMSI、subscriber data） 消息到new
VLR。 
new VLR发送Insert Subscriber Data Ack （包括IMSI）消息给HLR。 
HLR返回Update Location Ack （包括IMSI）消息到new VLR。 
new VLR分配新的TMSI返回Location Update Accept （包括VLR TMSI） 消息到new
SGSN。 
如果MSC/VLR返回位置更新失败或者SGSN无法获取MSC/VLR并且网络支持网络共享的MOCN功能，但是MS不是一个支持网络共享的MS，这种情况下SGSN会通过发送RAU拒绝消息，同时在下行消息的AS层携带Redirection
Indication参数Reject Cause Value为CS/PS coordination required给RNS，要求RNS发起redirection。 
对应图中的C2，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_Routing_Area_Update_Session
和 CAMEL_PS_Notification两个检查流程。 
new SGSN发送Routing Area Update Accept （包括PTMSI、VLR TMSI、PTMSI
Signature、IMS voice over PS Session Supported Indication）消息到MS。 
对应图中的C3，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_Routing_Area_Update_Context这一个检查流程。 
MS发现PTMSI或者TMSI被重新分配，发送Routing Area Update Complete消息到new SGSN。 
new SGSN发送TMSI Reallocation Complete消息到new VLR。 
SGSN内改变，从Iu接口切换到A/Gb接口流程
SGSN内改变，从Iu接口切换到A/Gb接口流程如[图4]所示。
图4  SGSN内改变，从Iu接口切换到A/Gb接口流程
流程说明如下： 
MS和RAN侧决定执行intersystem改变，并且新的Gb口消息将被用户使用，MS停止和网络侧的传输。 
MS发送Routing Area Update Request （包括old RAI、old PTMSI Signature、Update
Type） 消息到2G+3G SGSN。 
如果MS当前处于PMM CONNECTED 状态、the 2G+3G SGSN发送SRNS Context Request
（包括IMSI） 消息到 SRNS。收到该消息后，SRNS开始缓存下行数据，并且停止发送下行数据到MS。 
SRNS 返回SRNS Context Response （包括GTP SNDs、GTP SNUs、PDCP-SNDs、PDCP
SNUs） 消息。 
SGSN执行鉴权过程，对MS进行鉴权。 
如果MS处于PMM CONNECTED状态、the 2G+3G SGSN 发送SRNS Data Forward Command
（包括RAB ID、Transport Layer Address、Iu Transport Association） 消息到SRNS。通知SRNS前转数据到SGSN。 
如果SGSN之前建了DT， SGSN发送Update PDP Context Request（包括SGSN Address
and TEID、QoS Negotiated、RAT type）到建立了对应PDP的GGSN。GGSN更新了用户面的地址和TEID，返回Update
PDP Context Response给SGSN。 
对于SRNS Data Forward Command消息中的每个RAB，SRNS开始复制和隧道传输缓存的GTP报文到2G+3G
SGSN。 
2G+3G SGSN发送Iu Release Command消息到SRNS释放Iu连接。SRNS返回Iu Release
Complete 消息完成Iu释放。 
如果是联合RAU或者已经建立Gs口关联但是LAI发生了改变，the 2G+3G SGSN发送Location Update
Request （包括new LAI、IMSI、SGSN Number、Location Update Type） 消息到VLR。 
如果VLR发生了改变、new VLR通知HLR。HLR插入用户签约数据到new VLR。 
new VLR发送Update Location （包括new VLR） 消息到HLR。 
HLR发送sending Cancel Location （包括IMSI）消息到old VLR撤销和old VLR的关联。 
old VLR返回Cancel Location Ack （包括IMSI）消息到HLR。 
HLR发送Insert Subscriber Data （包括IMSI、subscriber data） 消息到new
VLR. 
new VLR返回Insert Subscriber Data Ack （包括IMSI）消息到HLR。 
HLR返回Update Location Ack （包括IMSI） 消息到new VLR. 
new VLR分配新的VLR TMSI 返回Location Update Accept （包括VLR TMSI）消息到2G+3G
SGSN。 
2G+3G SGSN发送Routing Area Update Accept （包括PTMSI、PTMSI Signature、Receive
N PDU Number （= converted PDCP SNU）） 消息到MS。 
对应图中的C1，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_Routing_Area_Update_Session、CAMEL_PS_Notification和CAMEL_GPRS_Routing_Area_Update_Context三个检查流程。 
如果分配了新的PTMSI，MS发送Routing Area Update Complete （包括Receive N
PDU Number） 消息到SGSN。 
如果重新分配了VLR TMSI，2G+3G SGSN发送TMSI Reallocation Complete消息到VLR。 
2G+3G SGSN 和BSS根据需要执行BSS Packet Flow Context过程。 
SGSN内改变，从A/Gb接口切换到Iu接口流程
SGSN内改变，从A/Gb接口切换到Iu接口流程如[图5]所示。
图5  SGSN内改变，从A/Gb接口切换到Iu接口流程
流程说明如下： 
MS和RAN侧决定执行intersystem改变，并且新的Iu口消息将被用户使用，MS停止和网络侧的传输。 
MS建立和RNC之间的RRC连接，发送Routing Area Update Request （包括PTMSI、Old
RA、Old PTMSI Signature、Update Type、CM）消息到2G+3G SGSN。 
SGSN执行鉴权和安全模式流程。对MS进行鉴权，同时和RNC协商完整性保护的算法和密钥。 
如果是联合RAU或者已经建立Gs口关联但是LAI发生了改变，the 2G+3G SGSN发送Location Update
Request （包括new LAI、IMSI、SGSN Number、Location Update Type） 消息到VLR。 
如果VLR发生了改变、new VLR通知HLR。HLR插入用户签约数据到new VLR: 
new VLR发送Update Location （包括new VLR） 消息到HLR。 
HLR发送sending Cancel Location （包括IMSI）消息到old VLR撤销和old VLR的关联。 
old VLR返回Cancel Location Ack （包括IMSI）消息到HLR。 
HLR发送Insert Subscriber Data （包括IMSI、subscriber data） 消息到new
VLR。 
new VLR返回Insert Subscriber Data Ack （包括IMSI）消息到HLR。 
HLR返回Update Location Ack （包括IMSI） 消息到new VLR. 
The new VLR allocates a new VLR TMSI and responds with Location
Update Accept （包括VLR TMSI） to the 2G+3G SGSN. VLR TMSI is optional
if the VLR has not changed. 
2G+3G SGSN发送Routing Area Update Accept （包括PTMSI、PTMSI Signature、IMS
voice over PS Session Supported Indication） 消息到MS。 
对应图中的C1，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_Routing_Area_Update_Session、CAMEL_PS_Notification和
CAMEL_GPRS_Routing_Area_Update_Context三个检查流程。 
如果重新分配了PTMSI，MS返回Routing Area Update Complete消息到SGSN。 
如果VLR分配了新的VLR TMSI，2G+3G SGSN发送TMSI Reallocation Complete消息到VLR。 
如果MS需要发送上行数据或者信令，MS发送Service Request （包括PTMSI、RAI、CKSN、Service
Type） message to the SGSN。Service Type 指出: Data或者Signalling. 
2G+3G SGSN发送RAB Assignment Request （包括RAB ID（s）、QoS Profile（s）、GTP
SNDs、GTP SNUs、PDCP SNUs） 消息到SRNS来重新建立RAB。如果支持DT，那么携带GGSN的用户面地址和TEID 
如果建立DT，SGSN发送Update PDP Context Request （包括RNC Address and TEID、QoS
Negotiated、RAT type）到对应的PDP归属的GGSN，携带RNC的用户面地址和TEID。 
SGSN和RNC之间的数据传输开始。 
SRNS和MS之间开始数据传输。 
SGSN间改变，从Iu接口切换到A/Gb接口流程
SGSN间改变，从Iu接口切换到A/Gb接口流程如[图6]所示。
图6  SGSN间改变，从Iu接口切换到A/Gb接口流程
流程说明如下： 
MS和RAN侧决定执行intersystem改变，并且新的Gb口消息将被用户使用，MS停止和网络侧的传输。 
MS发送Routing Area Update Request （包括old RAI、old PTMSI Signature、Update
Type、MS Network Capability） 消息到new 2G SGSN。 
new 2G SGSN发送SGSN Context Request （包括old RAI、TLLI、old PTMSI
Signature、New SGSN Address） 到old 3G SGSN获取MS的MM和PDP上下文。Old SGSN检查old
PTMSI Signature ，返回new SGSN响应带合适原因值。New SGSN根据原因值决定执行鉴权流程，鉴权成功之后new
SGSN发送SGSN Context Request （包括IMSI、old RAI、MS Validated） 消息到old SGSN。 
如果MS在old 3G-SGSN处于PMM CONNECTED状态,或者是局内RAU用户处于PMM-CONNECTED状态，old
3G-SGSN发送SRNS Context Request （包括IMSI）消息到old RNC来获取PDP上下文的序列号，在SGSN
Context Response消息中带给new 2G-SGSN。收到了该消息，RNC停止发送下行数据开始缓存下行数据，并且返回SRNS
Context Response （包括IMSI、GTP SNDs、GTP SNUs、PDCP SNUs） 消息给old 3G-SGSN。 
old 3G SGSN返回SGSN Context Response （包括MM Context、PDP Contexts）
消息到new 2G-SGSN。 
new 2G-SGSN执行鉴权流程，验证MS的合法性。如果SGSN Context Response 消息中没有携带IMEISV并且ADD功能在new
2G-SGSN支持，new 2G-SGSN从MS获取IMEISV。 
new 2G SGSN发送SGSN Context Acknowledge消息到old 3G SGSN。通知old 3G
SGSN new 2G SGSN已经准备好接收相应PDP上下文的数据包。 
对应图中的C1，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_PDP_Context_Disconnection和CAMEL_GPRS_Detach
and CAMEL_PS_Notification两个检查流程。 
如果MS处于PMM CONNECTED态，old 3G SGSN发送SRNS Data Forward Command
（包括RAB ID、Transport Layer Address、Iu Transport Association） 消息到SRNS。RNC启动data-forwarding定时器，指示对应的RAB开始复制和隧道传输缓存的数据到old
3G SGSN。 
old 3G SGSN通过隧道传输GTP数据包到new 2G SGSN。 
new 2G SGSN发送Update PDP Context Request （包括new SGSN Address、TEID、QoS
Negotiated、serving network identity、CGI/SAI、RAT type、CGI/SAI/RAI change
support indication、NRSN） 消息到每个PDP对应的GGSN。GGSN更新PDP上下文后返回Update PDP
Context Response （包括TEID、Prohibit Payload Compression、APN Restriction、CGI/SAI/RAI
change report required、BCM）消息。 
new 2G SGSN发送Update GPRS Location （包括SGSN Number、SGSN Address、IMSI、IMEISV）消息到HLR，如果支持ADD功能应该携带IMEISV。通知HLR用户的位置信息发生了改变。 
HLR发送Cancel Location （包括IMSI）消息到old 3G SGSN。old 3G SGSN返回Cancel
Location Ack （包括IMSI） 消息。old 3G SGSN删除MM and PDP上下文。 
如果MS old 3G SGSN在处于PMM CONNECTED态，old 3G SGSN发送Iu Release Command
消息到SRNS。当RNC data-forwarding定时器超时或者数据前传完成，SRNS返回Iu Release Complete消息。 
HLR发送Insert Subscriber Data （包括IMSI、Subscription Data）消息到new
2G SGSN。2G SGSN返回Insert Subscriber Data Ack （包括IMSI）消息到HLR。 
HLR返回Update GPRS Location Ack （包括IMSI、GPRS Subscriber Data）
消息到 new 2G SGSN。 
如果是联合RAU或者已经建立Gs口关联但是LAI发生了改变，2G SGSN发送Location Update Request
（包括new LAI、IMSI、SGSN Number、Location Update Type） 消息到VLR。 
如果VLR发生了改变、new VLR通知HLR。HLR插入用户签约数据到new VLR: 
new VLR发送Update Location （包括new VLR） 消息到HLR。 
HLR发送sending Cancel Location （包括IMSI）消息到old VLR撤销和old VLR的关联。 
old VLR返回Cancel Location Ack （包括IMSI）消息到HLR。 
HLR发送Insert Subscriber Data （包括IMSI、subscriber data） 消息到new
VLR. 
new VLR返回Insert Subscriber Data Ack （包括IMSI）消息到HLR。 
HLR返回Update Location Ack （包括IMSI） 消息到new VLR. 
new VLR分配新的VLR TMSI，返回Location Update Accept （包括VLR TMSI） 到2G
SGSN。 
对应图中的C2，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_Routing_Area_Update_Session
和 CAMEL_PS_Notification两个检查流程。 
new 2G SGSN发送Routing Area Update Accept （包括PTMSI、PTMSI Signature、Receive
N PDU Number （= converted PDCP SNU））消息给MS。 
对应图中的C3，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_Routing_Area_Update_Context这一个检查流程。 
如果分配新的PTMSI，MS返回Routing Area Update Complete （包括Receive N PDU
Number （= converted PDCP SND））消息到new 2G-SGSN。 
如果分配了新的VLR TMSI，new 2G SGSN发送TMSI Reallocation Complete消息到new
VLR 。 
2G SGSN和BSS根据需要执行BSS Packet Flow Context过程。 
SGSN间改变，从A/Gb接口切换到Iu接口流程
SGSN间改变，从A/Gb接口切换到Iu接口流程如[图7]所示。
图7  SGSN间改变，从A/Gb接口切换到Iu接口流程
l流程说明如下： 
MS和RAN侧决定执行intersystem改变，并且新的Iu口消息将被用户使用，MS停止和网络侧的传输。 
MS发送Routing Area Update Request （包括PTMSI、old RAI、old PTMSI
Signature、Update Type、CM、MS Network Capability）消息到new 3G SGSN。 
new 3G SGSN根据old RAI获取到old 2G SGSN地址，发送SGSN Context Request
（包括old RAI、old PTMSI、New SGSN Address） 消息到old 2G SGSN获取MS的MM和PDP上下文。Old
2G-SGSN检查old PTMSI Signature非法，返回new SGSN响应带合适原因值。New SGSN根据原因值决定执行鉴权流程，鉴权成功之后new
SGSN发送SGSN Context Request （包括old RAI、IMSI、MS Validated、New SGSN Address）
消息到old 2G-SGSN。 
old 2G SGSN 返回SGSN Context Response （包括MM Context、PDP Contexts）消息。 
new 3G-SGSN执行鉴权和安全模式流程。对MS进行鉴权同时和RNC协商完整性保护的算法和密钥。如果SGSN Context
Response消息中没有携带IMEISV同时new 3G-SGSN支持ADD功能，new 3G-SGSN向MS获取IMEISV。 
new 3G SGSN发送SGSN Context Acknowledge消息到old 2G SGSN。通知old 2G-SGSN
new 3G-SGSN已经准备好接收对应的PDP上下文的数据包。 
对应图中的C1，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_PDP_Context_Disconnection和CAMEL_GPRS_Detach
and CAMEL_PS_Notification两个检查流程。 
old 2G SGSN复制缓存的数据包通过隧道传输到new 3G-SGSN。 
new 3G SGSN发送Update PDP Context Request （包括new SGSN Address、TEID、QoS
Negotiated、serving network identity、CGI/SAI、RAT type、CGI/SAI/RAI change
support indication）消息到每个PDP上下文对应的GGSN。GGSN更新PDP上下文之后返回Update PDP Context
Response （包括TEID、Prohibit Payload Compression、APN Restriction、CGI/SAI/RAI
change report required） 消息。 
new 3G SGSN发送Update GPRS Location （包括SGSN Number、SGSN Address、IMSI、IMEISV）
消息到HLR，如果支持ADD功能携带IMEISV，通知HLR用户注册的SGSN发生了改变。 
HLR发送Cancel Location （包括IMSI、Cancellation Type）消息到old 2G SGSN。old
2G SGSN删除MM和 PDP上下文。old 2G SGSN返回Cancel Location Ack （包括IMSI）消息到HLR。 
HLR发送Insert Subscriber Data （包括IMSI、Subscription Data） 消息到new
3G SGSN。3G SGSN返回Insert Subscriber Data Ack （包括IMSI）消息给HLR。 
如果由于区域签约限制或是接入限制，不允许MS在这个RA内附着，则SGSN拒绝这个RAU请求，回复Insert Subscriber
Data ACK。 
由于签约检查失败或是其他原因，SGSN拒绝RAU请求，回复Insert Subscriber Data
ACK。 
网络支持网络共享的MOCN功能，但是MS不是一个支持网络共享的MS，这种情况下SGSN会通过发送RAU拒绝消息携带Redirection
Indication参数给RNS来发起redirection。 
HLR返回Update GPRS Location Ack （包括IMSI） 消息到new 3G SGSN. 
如果是联合RAU或者已经建立Gs口关联但是LAI发生了改变，3G SGSN发送Location Update Request
（包括new LAI、IMSI、SGSN Number、Location Update Type） 消息到VLR。 
如果VLR发生了改变、new VLR通知HLR。HLR插入用户签约数据到new VLR: 
new VLR发送Update Location （包括new VLR） 消息到HLR。 
HLR发送sending Cancel Location （包括IMSI）消息到old VLR撤销和old VLR的关联。 
old VLR返回Cancel Location Ack （包括IMSI）消息到HLR。 
HLR发送Insert Subscriber Data （包括IMSI、subscriber data） 消息到new
VLR. 
new VLR返回Insert Subscriber Data Ack （包括IMSI）消息到HLR。 
HLR返回Update Location Ack （包括IMSI） 消息到new VLR. 
new VLR分配新的TMSI后返回Location Update Accept （包括VLR TMSI）消息到3G
SGSN。 如果MSC/VLR返回位置更新失败或者SGSN无法获取MSC/VLR并且网络支持网络共享的MOCN配置，但是MS不是一个支持网络共享的MS，这种情况下SGSN会通过发送RAU拒绝消息，同时在下行消息的AS层携带Redirection
Indication参数Reject Cause Value为CS/PS coordination required给RNS，要求RNS发起redirection。 
对应图中的C2，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括： CAMEL_GPRS_Routing_Area_Update_Session
和 CAMEL_PS_Notification两个检查流程。 
new 3G SGSN发送Routing Area Update Accept （包括PTMSI、PTMSI signature）消息到MS。 
对应图中的C3，如果用户签约了CAMEL特性，需要执行CAMEL检查，包括：CAMEL_GPRS_Routing_Area_Update_Context这一个检查流程。 
如果分配了新的PTMSI，MS返回Routing Area Update Complete消息到SGSN。 
new 3G SGSN判断分配了新的VLR TMSI发送TMSI Reallocation Complete消息到new
VLR。 
如果MS需要发送上行数据或者信令，MS发送Service Request （包括PTMSI、RAI、CKSN、Service
Type） message to the SGSN。Service Type 指出: Data或者Signalling. 
3G SGSN发送RAB Assignment Request （包括RAB ID（s）、QoS Profile（s）、GTP
SNDs、GTP SNUs、PDCP SNUs） 消息到SRNS来建立RAB。如果支持DT，那么携带GGSN的用户面地址和TEID 
如果建立DT，SGSN发送Update PDP Context Request （包括RNC Address and TEID、QoS
Negotiated、RAT type）到对应的PDP归属的GGSN，携带RNC的用户面地址和TEID。 
系统影响 : 
局间路由更新到本局的用户数越多，系统资源占用越大。 
路由更新越频繁，系统CPU使用率越高。 
特性交互 : 
由于RAU流程是基本业务流程，在用户移动过程中通过RAU流程，保证用户一直处于注册状态并且网络侧用户的位置信息是最新的。保证后续所有PS业务及PDP相关流程可以正常进行。如果RAU失败，MS需要重新注册到网络才能继续进行PS相关业务。特性交互参见[表2]。
业务|交互
---|---
RAU和PDP更新|在路由更新的过程中会涉及到跨RAT改变或者SGSN改变，那么SGSN应该向GGSN发起PDP更新过程。
RAU和PDP去活|如果RAU过程失败，会导致用户的PDP删除，会出SCDR话单。
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060 "General Packet Radio Service （GPRS）; Service
description; Stage 2". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service （GPRS）; Base
Station System （BSS） - Serving GPRS Support Node （SGSN）; BSS GPRS
Protocol （BSSGP）". 
3GPP TS 29.060: "General Packet Radio Service （GPRS）; GPRS
Tunnelling Protocol （GTP） across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part （MAP） specification". 
3GPP TS 23.003: "Numbering、addressing and identification". 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
用户路由更新流程完成后，
Gn/Gp SGSN中如果没有用户的MM上下文会创建一个MM上下文，用于临时保存用户相关信息。 
O&M相关 : 
命令
相关命令参见[表3]。
功能|命令
---|---
新增邻接局|ADD ADJOFC
新增RNC局向附加属性|ADD RNC
新增ASP|ADD M3UAASP
新增AS|ADD M3UAAS
新增M3UA静态路由|ADD M3UART
新增SIO|ADD SIOLOCAS
新增移动号码分析结果索引|ADD IROAM
新增移动号码分析|ADD MDNAL
新增GT翻译选择子|ADD GTT
新增GT翻译数据|ADD GT
新增M3UA偶联|ADD M3UASCTP
新增位置区配置|ADD LAI
新增路由区配置|ADD RAI
新增RNC局向附加属性寻呼区域|ADD RNC PAGING AREA
设置Combo本局移动数据|SET COMBOCFG
增加SGSN地址解析|ADD SGSNHOST
设置DNS的全局配置|SET DNS GLB
增加DNS地址|ADD DNS SERVER
性能统计
SGSN路由区更新测量的设置依据： 
路由更新测量按测量对象分为SGSN路由更新测量和SGSN路由区更新测量，测量对象分别为SGSN和RA；两个测量类型中包含的计数器相同，测量触发点也一致。 
路由更新测量需要统计的包括请求次数、成功次数和失败次数，其中失败次数按拒绝消息携带的GMM Cause的取值进行分原因统计。 
路由更新测量按接入方式（GSM、UMTS）分别进行统计。 
路由更新测量按路由更新类型（包括普通RAU、周期性RAU、联合RAU以及IMSI附着的联合RAU）分别进行统计。 
路由更新测量按SGSN内和SGSN间分别进行统计。 
性能计数器参见[表4]。
测量类型名称|性能计数器名称
---|---
SGSN 路由更新测量（GSM）|编号为C40577开头的所有计数器。
SGSN 路由更新测量（UMTS）|编号为C40578开头的所有计数器。
业务观察/失败观察
失败的分原因统计，以SGSN内的RAU失败次数-UMTS为例，涵盖的失败原因参见[表5]。
GMM Cause取值|含义|计数器举例
---|---|---
2# IMSI unknown in HLR3# Illegal MS|非法用户|C405780003 由于非法用户导致的SGSN内的RAU失败次数-UMTS
6# Illegal ME|非法设备|C405780004 由于非法设备导致的SGSN内的RAU失败次数-UMTS
7# GPRS services not allowed|GPRS服务不允许|C405780005 由于GPRS服务不允许导致的SGSN内的RAU失败次数-UMTS
8# GPRS services and non-GPRS services not allowed|GPRS服务和非GPRS服务不允许|C405780006 由于GPRS服务和非GPRS服务不允许导致的SGSN内RAU失败次数-UMTS
9# MS identity cannot be derived by the network|网络无法获取IMSI|C405780007 由于网络无法获取MS ID导致SGSN内的路由更新失败次数_UMTS
10# Implicitly detached|隐式分离|C405780008 由于用户隐式分离导致的SGSN内的RAU失败次数-UMTS
11# PLMN not allowed|PLMN不允许|C405780009 由于PLMN不允许导致的SGSN内RAU失败次数-UMTS
12# Location Area not allowed|位置区不允许|C405780010 由于位置区不允许导致的SGSN内的RAU失败次数-UMTS
13# Roaming not allowed in this location area|漫游位置区不允许|C405780011 由于漫游位置区不允许导致的SGSN内的RAU失败次数-UMTS
14# GPRS services not allowed in this PLMN|GPRS服务在本PLMN不允许|C405780012 由于GPRS服务在本PLMN不允许导致的SGSN内的RAU失败次数-UMTS
15# No Suitable Cells In Location Area|本位置区没有合适的小区|C405780013 由于本位置区没有合适的小区导致的SGSN内的RAU失败次数-UMTS
17# Network failure|网络侧失败|C405780014 由于网络侧失败导致SGSN内的路由更新失败次数-UMTS
96# Invalid mandatory information|必选项错误|C405780015 由于必选项错误导致SGSN内的路由更新失败次数-UMTS
97# Message type non-existent or not implemented|消息类型不存在|C405780016 由于消息类型不存在导致SGSN内的路由更新失败次数-UMTS
98# Message not compatible with the protocol state|消息类型和协议不匹配|C405780017 由于消息类型和协议不匹配导致SGSN内的路由更新失败次数-UMTS
99# Information element non-existent or not implemented|信元错误|C405780018 由于信元错误导致的SGSN内RAU失败次数-UMTS
111# Protocol error、unspecified|协议错误或未指明|C405780019 由于未指定的协议错误导致的SGSN内RAU失败次数-UMTS
话单与计费
局间路由更新会在old SGSN产生MCDR，如果用户在路由更新前已经激活PDP上下文，则在路由更新后，old
SGSN会产生SCDR。 
路由更新失败的时候导致PDP去激活出S-CDR话单。 
特性配置 : 
摘要配置特性测试用例 
配置特性 : 
配置说明
该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置就可以。 
配置前提
不同局间的交互需要提前协商以下数据配置，如不同的RA对应不同的SGSN。通过信息交互以保证MS到SGSN的通信、SGSN与SGSN之间、SGSN到GGSN之间的通信。 
已经新增了本局信令点和本局配置。 
SGSN里已配置的是静态偶联，允许不同的RNC接入。 
SGSN里已配置的RA包含MS所处的RA。 
所有的RA都能正确解析到对应的SGSN。 
不同RNC或SGSN之间的通信，在SGSN地址解析里已有相应的配置。 
配置过程
M3UA连接建立过程
在EM客户端的配置页面的左侧命令树中，展开网元节点，选择CommonS_SIG_0节点。
使用[ADD ADJOFC]命令建立邻接局。
使用[ADD M3UAASP]命令新增ASP。
使用[ADD M3UAAS]命令新增AS。
使用[ADD M3UART]命令配置M3UA静态路由。
使用[ADD SIOLOCAS]命令新增SIO定位AS。
在EM客户端的配置页面的左侧命令树中，展开网元节点，选择NFS_MMESGSN_0节点。
使用命令[ADD RNC]建立RNC局。
使用命令[ADD ADJOFCIDCFG]添加局向属性。
使用[ADD IROAM]命令新增移动号码分析结果索引。
使用[ADD MDNAL]命令新增移动号码分析。
使用[ADD GTT]命令新增GT翻译选择子。
使用[ADD GT]命令新增GT翻译数据。
使用[ADD M3UASCTP]命令配置与RNC间的静态偶联。
使用[ADD M3UASCTP]命令配置与HLR间的动态偶联。
使用[ADD LAI]命令增加SGSN管理的LA。
使用[ADD RAI]命令增加SGSN管理的RA。
使用[ADD RNC PAGING AREA]命令新增RNC局向附加属性寻呼区域。
使用[SET COMBOCFG]命令配置本地移动数据。
SGSN配置更新过程
在EM客户端的配置页面的左侧命令树中，展开网元节点，选择NFS_MMESGSN_0节点。使用[SYNA]命令同步前后台数据。
跨局路由区更新选择SGSN过程
使用本地地址解析配置： 
使用[ADD SGSNHOST]命令增加新局SGSN地址解析。
使用[SET DNS GLB]命令设置DNS的全局配置。
使用[ADD DNS SERVER]命令增加DNS地址。
配置实例
多个SGSN与多个RNC相连，同时SGSN对应多个GGSN。 
步骤|命令|描述
---|---|---
1|ADD ADJOFC:OFFICEID=18,NETWORKNAME="HLR18",SPCMODE="TRIPLE_DEC",DPC="3.18.3",NET=1,SPTYPE="STEP",SPCTYPE="24",BANDFLAG="YES"|配置邻接局HLR。
2|ADD ADJOFC:OFFICEID=113,NETWORKNAME="RNC113",SPCMODE="TRIPLE_DEC",DPC="1.113.1",NET=1,SPTYPE="STEP",SPCTYPE="24",BANDFLAG="YES"ADD RNC|配置邻接局RNC。
3|ADD SCTP:ID=18,NAME="HLR18",LOCPORT=1520,REMPORT=6018,VPNID1=0,LOCADDR1=40.1.136.152,REMADDR1=40.1.136.181,ROLE="CLT",PROTOCALTYPE="M3UA"ADD M3UASCTP:ASSOCID=18,SCTPPROTYPE="M3UA",OFFICEID=18|配置与邻接局HLR的M3UA连接。
4|ADD M3UAASP:ASPID=18,NAME="HLR18",ASSOCID=18|增加ASP配置。
5|ADD M3UAAS:ASID=18,NAME="HLR18",EXISTCONTEXT="YES",PROTOCOL="M3UA",CONTEXTID=152,TAG="CLT",ASUPTYPE="SCCP",ASPID1=18|增加AS配置。
6|ADD M3UART:ROUTEID=18,ALIAS="HLR18",ASID1=18|M3UA静态路由配置。
7|ADD SIOLOCAS:DROUTEID=18,ALIAS="HLR18",DSTOFFICEID=18,SIO="SCCP",ROUTEID1=18|SIO定位AS配置。
8|ADD IROAM:IDX=1,TP="HLR",RST="8613900018",NAME="HLR18"|号码分析索引。
9|ADD MDNAL:DGT="46003",ENTR="DAS_IMSI_ROAM",RST=1,NAME="HLR18"|移动号码分析。
10|ADD GTT:PLAN="E.164",NATURE="INT",ID=1,NAME="HLR18"|GT翻译选择子。
11|ADD GT:GT="8613900018",GTSL=1,OFCIDS=18-1|GT翻译数据。
12|ADD M3UASCTP:MODULE=2,OFCID=113,ROLE="CLT",LOCADDR="IPv4"-0-"40.1.136.152",LOCPORT=1515,REMADDR="IPv4"-0-"40.1.136.113",REMPORT=1130,NAME="RNC113",ID=113|配置与邻接局RNC的M3UA连接。
13|ADD LAI:NAME="1521",MCC="460",MNC="03",LAC="1521"ADD LAI:NAME="1522",MCC="460",MNC="03",LAC="1522"|增加LA配置。
14|ADD RAI:NAME="152101",LAI="1521",RAC="01"ADD RAI:NAME="152201",LAI="1522",RAC="01"|增加RA配置。
15|ADD RNC PAGING AREA:RNCOFFID=113,LAI="1521"&"1522"|新增RNC局向附加属性寻呼区域。
16|SET COMBOCFG:MCC="460",MNC="03",GSNCODE="8613900060",IPV4APN="zte.com",SUPTYPE="ALL"|配置SGSN本局移动数据。
17|SYNA:STYPE="CHG"|同步前后台数据。
18|ADD SGSNHOST:NAME="rac0001.lac6101.mnc003.mcc460.gprs",IPADDR="200.61.1.159"|增加新局SGSN地址解析，本地解析时使用。
19|ADD DNS SERVER:ID=1,SERVERIPADDR=192.18.0.177,CLIENTIPADDR=40.1.136.1,VRFID=11|增加DNS服务器地址，DNS解析时使用。
测试用例 : 
测试项目|PMM-CONNECTED状态下的路由更新。
测试目的|验证网络侧能否正确处理PMM-CONNECTED状态下的跨路由更新请求。
预置条件|用户在HLR正常签约。用户附着并保持Iu连接，用户有激活的PDP上下文。
测试过程|用户在同一RNC内通过同一Iu连接发起路由更新。
通过准则|路由更新按照普通路由更新流程正常进行。
测试结果|—
## ZUF-77-01-005 跨RAT RA更新 
概述 : 
跨RAT路由区更新（包括互连路由区更新和位置区域更新）发生在SGSN之间。当手机在2G/3G网络和4G网络之间移动时，该流程用于通知SGSN新位置消息。 
收益 : 
当MS位置在RAT之间变化，该流程用于通知SGSN新位置信息。 
描述 : 
根据网络类型，跨RAT路由区更新分为以下类型： 
3G和2G间RA更新 
4G和3G间RA更新 
4G和2G间RA更新 
## ZUF-77-01-006 业务请求 
特性描述 : 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
应用限制 
特性交互 
遵循标准 
特性能力 
可获得性 
O&M相关 
描述 : 
定义
GnGp SGSN网元业务请求流程是3G用户在PS域从PMM-IDLE状态转变为PMM-CONNECTED状态，建立Iu连接过程，为后续用户进行PS域业务做建立无线连接的过程。如果业务请求的类型为数据类型，那么还需要为用户建立无线承载。 
在业务请求过程中，需要对UE进行鉴权和认证，确定用户身份的合法性。同时还要协商加密的算法和完整性保护算法，对用户的信令和数据进行保护。 
Iu接入时，GnGp SGSN对用户进行鉴权，同时用户需要对网络侧鉴权，进行双向鉴权。 
业务请求完成之后，用户可以与网络侧进行信令交互，用户可以进行PS域的业务（如短消息），用户可以进行数据业务。 
背景知识
GPRS网络架构图，如[图1]所示。
图1  GPRS架构图
其中包含了如下网元。 
TE/MT：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。 
UTRAN：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
HLR：永久存储用户签约数据。 
PDN：为用户提供业务的网络。 
CGF：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS：负责接收和处理从核心网发送过来的CDR文件。 
EIR：负责检查UE设备。 
PS CN（Packet Switched Core Network，分组交换核心网）：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元： 
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理上下文和分组数据协议上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息； 
GGSN：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务： 
MSC/VLR：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMSGMSC/SMS IWMSC：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL：该功能实体主要对用户进行在线计费。 
应用场景 : 
SGSN网元业务请求流程是3G业务基本流程，用户要使用PS的业务，必须有Iu连接，那么用户可以通过业务请求流程建立Iu连接。具体常见场景包括： 
处于PMM-IDLE状态的UE，需要进行PS业务，UE发起业务请求。 
处于PMM-IDLE状态的UE，网路侧收到了用户的下行数据包，网路侧发起寻呼，UE使用业务请求作为寻呼响应。 
处于PMM-IDLE状态的UE，触发网络侧分离、网络侧PDP去激活、网络侧激活、网络侧PDP修改、短消息业务，网络侧发起寻呼，UE使用业务请求作为寻呼响应。 
客户收益 : 
受益方|受益描述
---|---
运营商|支持Iu连接释放，可以节约运营商的PS网络资源，特别是无线资源，通过寻呼和业务请求，又可以使用户访问数据业务或其他业务不受影响，同时运营商也可以通过在业务请求过程中对用户进行鉴权，拒绝非法用户接入PS网络，避免用户非法使用网络资源。
移动终端用户|终端用户不掉网。
实现原理 : 
系统架构
无 
涉及的网元
网元名|作用
---|---
UE|RRC连接建立、和RNC之间的无线承载资源建立，完成业务请求流程的处理。
RNC|对用户建立无线承载资源，并通知UE建立无线承载，通知SGSN建立无线接入承载响应，透传UE和SGSN的NAS相关消息。
SGSN|对用户执行安全过程，对用户的无线资源进行管理，通知RNC建立无线承载及在建立单隧道情况下或QoS降低时，通知GGSN更新PDP上下文。
HLR|把用户的鉴权数据插入到SGSN，同时生成用户进行鉴权的鉴权向量。
协议栈
无 
本网元实现
无 
业务流程
MS Initiated Service Request Procedure
图2  MS Initiated Service Request Procedure
处于PMM-IDLE状态的UE，需要进行PS业务，UE发起业务请求。如果没有RRC连接，UE建立和RNC之间的RRC连接。 
UE发送Service Request (P-TMSI, RAI, CKSN, Service Type)消息到SGSN.
Service Type 指出业务请求的类型. Service Type有两种类型: Data 和Signalling。当Service
Type为Data的时候，UE可能会包含PDP上下文激活状态信息，说明哪个PDP上下文需要传输数据。在这种情况下，SGSN要执行鉴权流程。如果服务类型指示的是数据，一条信令连接在
MS 和 SGSN 之间被建立，而且激活PDP 上下文的资源也被分派。例如，为激活的PDP上下文建立起一条RAB。如果服务类型指示的是信令，为传送上层信息的信令链路在
MS 和 SGSN 之间被建立起来。例如，PDP上下文激活请求。则为激活PDP上下文的资源将不被分配。 
如果UE的状态为PMM-IDLE，SGSN发起鉴权和安全模式流程，协商鉴权参数和完整性保护算法和密钥。 
如果UE是PMM-CONNECTED状态并且业务请求类型为Data，SGSN应该向UE返回业务请求接受消息。如果是Data类型的业务请求消息，SGSN发送Radio
Access Bearer Assignment Request (NSAPIRAB ID(s), TEID(s), QoS Profile(s),
SGSN IP Address(es))消息给RNC来建立RAB。如果是建立DT，SGSN携带GGSN的用户面地址和TEID，而不是SGSN的IP地址以及TEID。SGSN还会用UE提供的PDP上下文激活信息去决定建立哪个RAB，哪个PDP需要删除。 
RNC发起和UE建立RB的流程。 
RNC向SGSN返回Radio Access Bearer Assignment Response (RAB ID(s),
TEID(s), QoS Profile(s), RNC IP Address(es)) 消息，此时IU接口的GTP隧道建立。 
如果RNC返回的Radio Access Bearer Assignment Response消息中说明请求的QoS不能被提供，则SGSN就会以不同的QoS重新发起一条Radio
Access Bearer Assignment Request消息 ，重建的次数和QoS值都由执行者决定。对于每个携带QoS重新建立的RAB，SGSN都会发起一个PDP
Context Modification procedure去通知MS以及GGSN给相应的PDP上下文分配新的协商QoS。如果在step4中SGSN建立了Direct
Tunnel，则SGSG会发起一个PDP Context Modification procedure给GGSN，向GGSN提供RNC的用户面地址以及下行数据的TEID。 
UE可以发送上行数据了。 
Network Initiated Service Request Procedure
图3  Network Initiated Service Request Procedure
SGSN收到了处于PMM-IDLE状态的用户的某个PDP上的下行数据。 
SGSN发送寻呼消息到RNC，RNC 发送寻呼消息到UE。 
当没有CS事务存在时，UE建立和RNC之间的RRC连接。 
UE发送Service Request (P TMSI, RAI, CKSN, Service Type)消息到SGSN.
Service Type 指出业务请求的类型为寻呼响应。这时SGSN会根据下行分组包判断是否要求建立RAB，如果下行的是PDU，则要建立；如果是信令消息（如请求PDP上下文激活或者是MT
SMS），则不需重建RAB。 
SGSN发起鉴权和安全模式流程，协商鉴权参数和完整性保护算法和密钥。 
如果PDP上下文的资源被重新建立，SGSN发送Radio Access Bearer Assignment Request
(NSAPIRAB ID(s), TEID(s), QoS Profile(s), SGSN IP Address(es))消息给RNC来建立RAB。如果是建立DT，SGSN携带GGSN的用户面地址和TEID。RNC发送Radio
Bearer Setup (RAB ID(s))到UE。UE返回Radio Bearer Setup Complete 消息给RNC，建立RB。
RNC发送 Radio Access Bearer Assignment Response (RAB ID(s), TEID(s),
RNC IP Address(es)) 消息到SGSN，通知SGSN Iu口的GTP隧道建立完成以及RNC和MS之间的RAB已经建立。如果RNC返回的Radio
Access Bearer Assignment Response消息中说明请求的QoS不能被提供，则SGSN就会携带不同的QoS重新发起一条Radio
Access Bearer Assignment Request消息 ，重建的次数和QoS值都由执行者决定。 
对于每个携带QoS重新建立的RAB，SGSN都会发起一个PDP Context Modification procedure去通知MS以及GGSN给相应的PDP上下文分配新的协商QoS。如果在第六步是建立单隧道，SGSN发起PDP
Context Modification过程到GGSN，告诉GGSN RNC的用户面地址和TEID。 
SGSN发送下行数据到UE。 
 说明： 
对于上述的业务请求流程，在23.060协议中有要求，traffic class为streaming or conversational的情况，RAB释放后是不允许通过业务请求来进行RAB重建的。UE可以通过发起PDP上下文修改或者重新激活两种方式恢复RAB。SGSN提供软件参数“是否支持会话或流媒体类业务rab重建”来控制RAB是否通过业务请求来进行RAB重建。 
系统影响 : 
随着业务请求数的增加，系统资源占用会一直增大。 
业务请求越频繁，系统CPU使用率越高。 
应用限制 : 
无 
特性交互 : 
由于业务请求流程是基本业务流程，3G PS业务得以使用的重要流程。如果业务请求流程失败，那么用户的一些PS业务将不能使用。 
业务|交互
---|---
寻呼和业务请求|寻呼响应会通过业务请求消息发送上来。
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060 "General Packet Radio Service (GPRS); Service
description; Stage 2". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service (GPRS); Base
Station System (BSS) - Serving GPRS Support Node (SGSN); BSS GPRS
Protocol (BSSGP)". 
3GPP TS 29.060: "General Packet Radio Service (GPRS); GPRS
Tunnelling Protocol (GTP) across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part (MAP) specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
用户业务请求流程完成后，更新用户的MM上下文，设置用户的状态和活动的时间。 
可获得性 : 
版本要求及变更记录
无 
License要求
无 
对其他网元的要求
无 
工程规划要求
无 
O&M相关 : 
命令
配置项无 
安全变量无 
定时器无 
软件参数新增软件参数参见表1。表1  新增软件参数软件参数ID软件参数名称786445SGSN是否支持会话或流媒体类业务rab重建0-否；1-是 
动态管理无 
性能统计
性能计数器参见[表2]。
测量类型名称|性能计数器名称
---|---
SGSN业务请求测量|编号为C40539开头的所有计数器
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
配置特性 
调整特性 
测试用例 
常见问题处理 
配置特性 : 
配置说明
无 
配置前提
该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置就可以。 
该配置的数据准备： 
不同局间的交互需要提前协商下数据配置，如不同的RA对应不同的SGSN。通过信息交互以保证MS到SGSN的通信，SGSN之间，SGSN到GGSN之间的通信等。已经新增了本局信令点和本局配置。具体来说： 
SGSN里配置的是静态偶联，允许不同的RNC接入。 
SGSN里配置的RA包含MS所处的RA。 
所有的RA都能正确解析到对应的SGSN。 
不同RNC或SGSN之间的通信，在SGSN地址解析里有相应的配置。 
配置过程
无 
配置实例
无 
调整特性 : 
无 
测试用例 : 
测试项目|数据类型的业务请求
测试目的|验证SGSN处理data类型业务请求
预置条件|前台与OMC网管运行正常
测试过程|用户激活1个PDP上下文，traffic class为traffic class为streaming或conversational。从RNC发起Iu释放请求。SGSN分组域安全变量参数中的支持会话或流媒体类业务rab重建设置为未选中。用户发起service request，请求类型为data。
通过准则|SGSN正常处理业务请求，Iu连接建立成功
测试结果|
常见问题处理 : 
无 
## ZUF-77-01-007 寻呼 
特性描述 : 
摘要描述应用场景客户收益实现原理系统影响应用限制特性交互遵循标准特性能力可获得性O&M相关 
描述 : 
定义
GnGp SGSN网元寻呼流程是2/3G用户在PS域有下行数据或者信令发送的时候，用户状态为PMM-IDLE或者STANDBY态时发生的流程。寻呼成功之后可以把用户状态迁移到PMM-CONNECTED或者READY状态，GnGP
SGSN知道用户所在的最新小区或者服务区。 
Iu接入时，UE使用寻呼类型的Service Request作为寻呼响应。 
Gb接入时，UE使用上行数据帧作为寻呼响应。 
寻呼完成之后，用户的状态为PMM-CONNECTED或者READY。 
背景知识
GPRS网络架构图,如图1所示，其中包含了如下网元： 
图1  GPRS架构图
TE/MT（Terminal Equipment/Mobile Terminal，终端设备/移动终端）：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS（Base Station System，基站系统）：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。 
UTRAN（UMTS Terrestrial Radio Access Network，统一的陆地无线接入网络）：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
HLR(Home Location Register，归属位置寄存器):永久存储用户签约数据。 
PDN(Packet
Data Network，分组数据网)：为用户提供业务的网络。 
CGF(Charging Gateway Functionality，计费网关功能)：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS（Billing System，计费系统）：负责接收和处理从核心网发送过来的CDR文件。 
EIR（equipment
identity register 设备标识寄存器）：负责检查UE设备。 
PS CN（Packet Switched Core
Network，分组交换核心网）：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元： 
SGSN(Serving
GPRS Support Node，服务GPRS支持节点)：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS
Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息； 
GGSN(Gateway GPRS Support Node，GPRS支持节点网关)：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务： 
MSC/VLR（Mobile Switch
Center/ Visitor Location Register，移动交互中心/拜访位置寄存器）：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMS GMSC/SMS IWMSC (Short Message Service Gateway MSC/ Short Message
Service Interworking MSC，短消息网管移动交换中心/短消息互通移动交换中心)：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL (Customised Applications for Mobile network Enhanced Logic，移动网络定制应用增强逻辑服务器)：该功能实体主要对用户进行在线计费。 
应用场景 : 
SGSN网元寻呼请求流程是2/3G业务基本流程，用于非连接态时通知UE进行状态迁移。具体常见场景包括： 
处于PMM-IDLE或者Standby状态的UE，有下行信令需要传输。 
处于PMM-IDLE或者Standby状态的UE，网路侧收到了用户的下行数据包，网路侧发起寻呼。 
客户收益 : 
受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的PS网络上后，对空闲态的用户如果有下行信令需要传输或网路侧收到了用户的下行数据包，则寻呼用户，寻呼成功后可以让用户继续使用业务，提高用户体验度。
移动终端用户|终端用户不可见。
实现原理 : 
系统架构
无 
涉及的网元
SGSN网元寻呼流程需要UE、BSS、RNC、SGSN、HLR、MSC/VLR（可选）的共同配合。 
网元|功能
---|---
UE（User Equipment，用户设备）|为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等，在寻呼过程中接收网络侧下发的寻呼消息，返回寻呼响应。
BSS（Base Station System，基站系统）|为终端的接入提供无线资源，对用户提供接入层安全功能。在寻呼过程中发送寻呼消息给终端。
RNC（Radio Network Controller，无线网络控制器）|为终端的Iu（无线接入网络和核心网的一种接口）接入提供无线资源。在寻呼过程中发送寻呼消息给终端。
SGSN(Serving GPRS Support Node，服务GPRS支持节点)|支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS MobilityManagement）上下文和分组数据协议（PDP，Packet Data Protocol）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。在寻呼过程中触发寻呼，发送寻呼消息给RAN，通过RAN发送给终端，处理终端返回的寻呼响应。
HLR（Home Location Register，归属位置寄存器）|负责存储用户的签约信息，包括用户签约的PS业务，签约的APN,Qos等参数。在寻呼过程中，把用户的鉴权数据插入到SGSN。
MSC/VLR|主要用户完成用户的CS域位置更新、注册以及语音业务的发起。在CS寻呼过程中，对于联合附着的用户通过PS域发送CS寻呼到MS。
协议栈
无 
本网元实现
无 
业务流程
Paging for GPRS Downlink Transfer (A/Gb mode)图2  Paging for GPRS Downlink Transfer (A/Gb mode)处于Standby状态的用户收到了下行的数据。SGSN发送BSSGP层的Paging Request （IMSI、P TMSI、Area、 Channel Needed、QoS、DRX Parameters） 消息到BSS。其中Area范围由SGSN根据配置的寻呼策略来确定。BSS需要IMSI用来计算MS寻呼组，P-TMSI是MS被寻呼的标识，Area指明了被寻呼的MS的路由区，Channel
Needed说明了是GPRS寻呼。QoS是为这个发起寻呼的PDP上下文协商过的QoS。DRX参数指明这个MS是否使用不连续的接收。BSS在用户上次驻留的路由区下的所有小区发送Paging Request（P TMSI、Channel Needed） 消息到UE。UE收到了寻呼消息，返回一个合法的上行LLC帧数据作为寻呼响应。响应的时候，MS修改MM状态为READY。收到了LLC 帧，BSS增加Cell ID后发送LLC帧到SGSN，SGSN把此帧作为寻呼响应，停止发送寻呼。 
PS Paging Initiated by SGSN (Iu mode) without RRC Connection
for CS图3  PS Paging Initiated by SGSN (Iu mode) without RRC Connection
for CS处于PMM-IDLE状态的用户收到了下行的数据或者信令。SGSN发送RANAP的Paging（IMSI、P TMSI、Area、CN Domain Indicator、DRX parameters）消息到用户上次驻留的路由区被管理的RNC。其中Area范围由SGSN根据配置的寻呼策略来确定。RNS需要用到IMSI来计算MS寻呼组，并且IMSI表示了被寻呼的MS。如果3G-SGSN分配了P-TMSI给MS，P-TMSI则需包含。Area指明了被寻呼的MS的路由区，CN
Domain Indicator指明PS域发起的寻呼消息。DRX Parameter指明了MS首选的DRX循环长度。RNS控制了MS是否建立RRC连接。在MS没有RRC连接情况下，将执行正常PCH寻呼。寻呼类型1在寻呼信道上传送，IMSI或P-TMSI识别MS。寻呼发起者用来指出是核心网还是UTRAN发起的寻呼。CN域ID用来指示本次寻呼消息是CS业务还是PS业务。在MS中寻呼请求触发了业务请求流程。 
PS Paging Initiated by 3G SGSN With RRC Connection for CS图4  PS Paging Initiated by 3G SGSN With RRC Connection for CS处于PMM-IDLE状态的用户收到了下行的数据或者信令。SGSN发送RANAP的Paging（IMSI、P TMSI、Area、CN Domain Indicator、DRX parameters） 消息到用户上次驻留的路由区被管理的RNC。其中Area范围由SGSN根据配置的寻呼策略来确定。RNS需要用到IMSI来计算MS寻呼组，并且IMSI表示了被寻呼的MS。如果3G-SGSN分配了P-TMSI给MS，P-TMSI则需包含，Area指明了被寻呼的MS的路由区，CN
Domain Indicator指明PS域发起的寻呼消息。DRX Parameter指明了MS首选的DRX循环长度。RNS判断MS是否建立RRC连接。在MS建立RRC连接情况下，寻呼类型2在建立的RRC连接上传送。CN域ID用来指示次寻呼消息是CS业务还是PS业务。在MS中寻呼请求触发了业务请求流程。 
CS Paging Initiated by SGSN 图5  CS Paging Initiated by SGSN 联合附着的用户处于非分离状态收到了MSC/VLR发送的CS寻呼。SGSN发送RANAP的Paging（IMSI、TMSI、Area、CN Domain Indicator、DRX parameters）消息到用户上次驻留的路由区被管理的RNC或者BSC。RNS/BSC需要用到IMSI来计算MS寻呼组，并且IMSI表示了被寻呼的MS。如果MSC/VLR分配了TMSI给MS，则寻呼消息包含TMSI，Area指明了被寻呼的MS的位置区。CN
Domain Indicator指明那个CS域发起的寻呼消息。DRX Parameter指明了MS首选的DRX循环长度。RNC/BSC发送CS寻呼消息给MS。 
系统影响 : 
随着寻呼请求数的增加，系统资源占用会一直增大。 
寻呼越频繁，系统CPU使用率越高。 
应用限制 : 
无 
特性交互 : 
由于寻呼流程是基本业务流程，3G PS业务得以使用的重要流程。如果寻呼流程失败，那么用户的一些PS业务将不能使用。 
业务|交互
---|---
寻呼和业务请求|寻呼响应会通过业务请求消息发送上来。
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060 "General Packet Radio Service
(GPRS); Service description; Stage 2". 
3GPP TS 24.008: "Mobile
Radio Interface Layer 3 specification; Core Network Protocols; Stage
3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service (GPRS); Base Station
System (BSS) - Serving GPRS Support Node (SGSN); BSS GPRS Protocol
(BSSGP)". 
3GPP TS 29.060: "General Packet Radio Service (GPRS);
GPRS Tunnelling Protocol (GTP) across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part (MAP) specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3; General
aspects". 
特性能力 : 
用户寻呼流程完成后，更新用户的MM上下文，更新用户的状态和活动的时间。 
SGSN支持1200万用户接入，支持1200万MM上下文。本文档中提供的指标值，是在一定条件下得出的，实际商用配置要依据实际话务模型和其它特定需求，协商确定。 
可获得性 : 
版本要求及变更记录
无 
License要求
无 
对其他网元的要求
无 
工程规划要求
无 
O&M相关 : 
命令
配置项无 
安全变量无 
定时器无 
软件参数无 
动态管理无 
性能统计
性能计数器参见[表3].
测量类型名称|性能计数器名称
---|---
SGSN寻呼测量|所有计数器标识由C40520开始
SGSN路由区寻呼测量|所有计数器标识由C40521开始
For the performance indexes, refer to [表4].
测量类型名称|性能指标名称
---|---
SGSN寻呼测量|二次或二次以上寻呼尝试次数
SGSN路由区寻呼测量|每路由区分组交换寻呼程序成功率（%）-UMTS每路由区分组交换寻呼程序成功率（%）-GSM
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
摘要GnGp SGSN网元寻呼流程配置特性调整特性测试用例常见问题处理 
#### GnGp SGSN网元寻呼流程配置特性 
配置说明
无 
配置前提
该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置就可以。 
该配置的数据准备。 
不同局间的交互需要提前协商下数据配置，如不同的RA对应不同的SGSN。通过信息交互以保证MS到SGSN的通信，SGSN之间，SGSN到GGSN之间的通信等。已经新增了本局信令点和本局配置。具体来说： 
SGSN里配置的是静态偶联，允许不同的RNC接入。 
SGSN里配置的RA包含MS所处的RA。 
所有的RA都能正确解析到对应的SGSN。 
不同RNC或SGSN之间的通信，在SGSN地址解析里有相应的配置。 
配置过程
使用命令[SET SGSN PAGING
POLICY]配置与寻呼策略。
配置实例
配置SGSN寻呼策略 
脚本命令|解释说明
---|---
SET SGSN PAGING POLICY:PGTIMES=3,PGINTERVAL=1,GBPTMSIPGAREA="RAI",IUPTMSIPGAREA="RAI", IMSIPAGING="NO",IMSIPGAREA="SGSN",OTHERITFPG="NO"|寻呼次数3，寻呼时间间隔1，Gb接入PTMSI寻呼区域为RAI，Iu接入PTMSI寻呼区域为RAI，不支持IMSI寻呼，PS域IMSI寻呼区域为SGSN，不支持在其它接口寻呼。
调整特性 : 
无 
测试用例 : 
测试项目|时间间隔寻呼
测试目的|根据配置的寻呼策略生效
预置条件|网管服务器正常，与前台连接正常
测试过程|SGSN寻呼策略为智能寻呼的时间间隔方式寻呼。触发对批量用户的寻呼，且寻呼失败,其中用户包括IU口和GB口用户。持续触发对这些用户的寻呼。
通过准则|检查SGSN能一直根据配置间隔对用户是否发起寻呼做控制。
测试结果|正常
常见问题处理 : 
无 
## ZUF-77-01-008 用户数据管理 
概述 : 
通过用户数据管理功能，HLR将用户数据插入到SGSN，并支持修改和删除保存在SGSN上的用户数据。 
收益 : 
该特性确保HLR和SGSN上的用户数据的一致性。 
描述 : 
当HLR上的用户数据发生变化，HLR发送插入用户数据（Insert Subscriber Data）消息给SGSN。SGSN处理用户数据变化，并发送插入用户数据响应（Insert Subscriber Data Ack）消息给HLR。 
## ZUF-77-01-009 Suspend 
概述 : 
在Gb接入模式下，SGSN支持暂停用户的数据业务。 
收益 : 
如果SGSN不支持DTM模式，当用户在CS域发起语音呼叫时，SGSN暂停该用户的数据业务。当用户完成语音呼叫并返回PS域后，SGSN立即恢复数据业务。 
描述 : 
UE附着到2G网络并且支持DTM模式。当UE发起语音业务，UE发送Suspend消息通知SGSN暂停其数据业务。  
当用户完成语音业务并返回PS域后，SGSN立即恢复该UE的数据业务。 
# 缩略语 
# 缩略语 
## BS 
Billing System计费系统
## BSS 
Base Station System基站系统
## CAMEL 
Customized Applications for Mobile Network Enhanced Logic移动网络增强逻辑的客户化应用
## CGF 
Charging
Gateway Function 计费网关功能
## CN 
Core Network核心网
## EDGE 
Enhanced Data rates for GSM EvolutionGSM用的增强型数据速率
EIR : 
Equipment Identity Register设备标识寄存器
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
## GMSC 
Gateway Mobile Switching Center网关移动交换中心
GPRS : 
General Packet Radio Service通用无线分组数据业务
HLR : 
Home Location Register归属位置寄存器
## IWMSC 
Interworking Mobile Switching Center网间移动交换中心
MSC : 
Mobile Switching Center移动交换中心
## MT 
Mobile Terminal移动终端
PDN : 
Packet Data Network分组数据网
PDP : 
Packet Data Protocol分组数据协议
## PS 
Packet Switched分组交换
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
SMS : 
Short Message Service短消息业务
## TE 
Terminal Equipment终端设备
UTRAN : 
UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
## VLR 
Visitor Location Register拜访位置寄存器
# ZUF-77-02 会话管理 
概述 : 
功能描述 : 
会话管理功能是UE与外部建立PDN连接，进行数据业务的基础。会话管理完成核心网络SGSN到GGSN之间的隧道建立、修改和释放的控制，完成SGSN和RNC/MS之间无线接入承载建立、修改和释放的控制。 
SGSN的会话管理功能包括：PDP上下文的激活、修改、去激活和保留等流程。 
功能特性简介 : 
会话管理功能详细的特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
PDP激活|当UE需要进行数据业务时，UE发起PDP激活流程。按PDP激活类型可分为：IPv4IPv6IPv4v6PDP上下文激活具体流程可参见3GPP 23.060协议9.2.2.1 PDP Context Activation Procedure章节。|ZUF-77-02-001 PDP激活
二次PDP激活|UE发起二次激活，建立和已经存在的PDP的地址和其他上下文信息相同，但是QoS不同的PDP。二次PDP上下文激活具体流程可参见3GPP 23.060协议9.2.2.1.1 Secondary PDP Context Activation Procedure章节。|ZUF-77-02-002 二次PDP上下文激活
网络侧发起PDP激活|GGSN收到用户的下行数据报文，GGSN检查没有报文PDP地址的PDP，向SGSN发起PDU通知请求，触发SGSN发起网络侧激活。网络侧请求PDP上下文激活具体流程可参见3GPP 23.060协议9.2.2.2 Network-Requested PDP Context Activation Procedure章节。|ZUF-77-02-003 网络侧发起PDP激活
PDP上下文修改|MS、SGSN、GGSN或RNC发起PDP更新过程，修改一个或几个PDP上下文中参数信息，可以修改的参数如下：QoSARP无线优先级PFIPDP地址（在GGSN发起PDP修改时）TFT（在MS或SGSN发起PDP修改时）PCO（在MS或SGSN发起PDP修改时）DTPDP上下文修改具体流程可参见3GPP 23.060协议9.2.3 Modification Procedures章节。|ZUF-77-02-004 PDP上下文修改
PDP去激活|MS、SGSN或GGSN发起PDP去激活功能，该过程可以去活一个PDP或相同PDP地址的多个PDP。PDP上下文去激活具体流程可参见3GPP 23.060 协议9.2.4 Deactivation Procedures章节。|ZUF-77-02-005 PDP去激活
PDP保留|当RAB释放时网络侧保留已经激活的PDP上下文，以便缩短RAB重建时间。PDP上下文保留具体流程可参见3GPP 23.060 协议9.2.5 Preservation Procedures章节。|ZUF-77-02-006 PDP上下文保留
Direct tunnel|DT就是指用户面数据报文直接在RNC和GGSN之间进行，不经过SGSN。建立DT的必要条件如下：RNC支持DT。GGSN支持DT。GGSN支持GTPV1。本地接入或拜访地接入。非CAMEL用户。另外，SGSN可以控制建立DT频次，可以根据IMEI\IMSI控制是否建立DT，这样可以减少DT带来的核心网信令风暴。DT具体流程可参见3GPP 23.060 协议15.6 Direct Tunnel Functionality章节。|ZUF-77-02-007 Direct tunnel
LBO控制|用户发生漫游时，如果为漫游用户选择归属地GGSN，会导致数据报文迂回，增加网络负担并增加时延，因此3GPP协议引入LBO，即SGSN为漫游用户选择拜访网络的GGSN。在用户签约许可拜访地接入且本地策略控制许可LBO时，SGSN为漫游用户选择拜访网络的GGSN，即许可LBO。用户签约PDP上下文中VPLMN Address Allowed参数为1，则标识该PDP上下文许可拜访地接入。SGSN上可以配置禁止LBO的漫游IMSI号段。参考3GPP 23.060 协议A.2 Selection Rules。|ZUF-77-02-008 LBO控制
## ZUF-77-02-001 PDP激活 
特性描述 : 
摘要描述应用场景客户收益实现原理系统影响应用限制特性交互遵循标准特性能力可获得性O&M相关 
描述 : 
定义
GnGp SGSN网元PDP激活流程是2/3G用户注册到PS网络上后，用户为访问数据业务需要通过PDP首次激活或二次激活过程激活PDP上下文。 
在PDP首次激活或二次激活过程中，GnGp SGSN为用户协商QoS，选择GGSN，通知GGSN建立PDP上下文。 
Gb接入时，GnGp SGSN可以对用户进行鉴权；可以通知BSS建立分组流上下文。 
Iu接入时，通知RNC建立无线承载，在RNC返回的QoS降低情况下或在建立单隧道情况下通知GGSN更新PDP上下文。 
PDP激活完成之后，用户可以通过PS网络访问数据业务和其他业务。 
背景知识
GPRS网络架构图如[图1]所示。
图1  GPRS架构图
其中包含了如下网元。 
TE/MT：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。 
UTRAN：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
HLR：永久存储用户签约数据。 
PDN：为用户提供业务的网络。 
CGF：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS：负责接收和处理从核心网发送过来的CDR文件。 
EIR：负责检查UE设备。 
PS CN（Packet Switched Core Network，分组交换核心网）：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元： 
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理上下文和分组数据协议上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息； 
GGSN：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务： 
MSC/VLR：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMSGMSC/SMS IWMSC：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL：该功能实体主要对用户进行在线计费。 
应用场景 : 
SGSN网元PDP激活流程是基本流程，用户因业务需求需要通过PS网络建立的承载访问数据业务和其他业务，必须通过PDP激活流程激活PDP上下文。具体常见场景包括： 
UE发起首次PDP激活。 
UE发起二次PDP激活。 
网络侧发起的首次激活。 
客户收益 : 
受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的PS网络上后，激活PDP上下文使运营商可以为用户提供各种数据业务和其他业务。
移动终端用户|终端用户不可见。
实现原理 : 
系统架构
无 
涉及的网元
SGSN网元PDP激活流程需要UE、BSS/RNC、SGSN、GGSN和CAMEL的共同配合： 
网元|功能
---|---
UE|为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等。在PDP激活过程中具体功能包括触发PDP建立，完成UEPDP上下文的建立。
BSS|为终端的接入提供无线资源，对用户提供接入层安全功能。在PDP激活过程中具体功能包括可以建立分组流上下文，透传UE和SGSN的NASPDP激活相关消息。
RNC|为终端的Iu（无线接入网络和核心网的一种接口）接入提供无线资源。在PDP激活过程中具体功能包括对用户建立无线承载资源，并通知UE建立无线承载，通知SGSN建立无线接入承载响应，透传UE和SGSN的NASPDP激活相关消息。
SGSN|支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS MobilityManagement）上下文和分组数据协议（PDP，Packet Data Protocol）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。在PDP激活过程中具体功能包括接收到UE的激活请求后，协商QoS，选择GGSN，为用户建立PDP相关信息，通知GGSN建立PDP上下文，用户Gb接入时，可以对用户进行鉴权，可以通知BSS建立分组流上下文；用户Iu接入时，通知RNC建立无线承载及在建立单隧道情况下或QoS降低时，通知GGSN更新PDP上下文。
GGSN|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。在PDP激活过程中具体功能包括负责UE接入PDN，分配用户IP地址，完成承载管理功能。
CAME|该功能实体主要对用户进行在线计费。在激活过程中主要控制激活流程是否可以继续，下发计费策略。
协议栈
无 
本网元实现
无 
业务流程
PDP Context Activation Procedure
图2  PDP Context Activation Procedure for A/Gb mode
图3  PDP Context Activation Procedure for Iu mode
手机发送激活请求消息携带NSAPI、TI、PDP类型、PDP地址、APN、请求的Qos到SGSN。 SGSN根据PDP地址是否携带判断手机申请的是静态地址还是动态地址，如果是动态地址激活，激活请求消息中不携带PDP地址。
如果SGSN决定可以在RNC和GGSN之间建立DT，SGSN在第4步的RAB指派请求消息中携带DT隧道的参数到RNC，并且在第6步的更新GGSN流程中，SGSN携带DT隧道下行数据接收的IP地址和TEID。 
A/Gb模式下，SGSN判断“Gb口激活PDP鉴权”设置为是，则SGSN对用户进行鉴权，否则不进行鉴权过程。 
SGSN发送Create PDP Context Request消息给GGSN，携带PDP类型，PDP地址，APN，协商的QoS，TEID，NSAPI信息；
   GGSN创建新的PDP上下文，申请Charging ID，返回Create PDP Context Response消息给SGSN，携带TEID，PDP地址，协商的QoS，Charging
ID，原因值等参数。 
在Iu接入模式需要执行RAB指派流程，其中SGSN判断满足建立单隧道条件，通知RNC GGSN用户面信息。 
A/Gb模式下，SGSN判断终端支持PFC，用户接入的NSE支持PFC并且PFI映射配置的PFI值为有效值，SGSN通知BSS执行分组流上下文过程。 
如果在RAB指派流程中，QoS参数被RNC降低或者支持建立DT，SGSN发送Update PDP Context Requset消息到GGSN，携带QoS、RNC用户面地址和TEIDU、DTI标记，GGSN在Update
PDP Context Reponse消息中确认是否接受QoS。 
SGSN插入GGSN地址到PDP上下文，SGSN发送激活接受消息给手机，携带PDP类型、PDP地址、TI、协商的QoS、无线传输优先级信息。SGSN可以开始转发上下行数据报文并且开始计费。 
在步骤1和步骤6完成后，有一个CAMEL检查点C1和C2： 
如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起 
C1：CAMEL_GPRS_PDP_Context_Establishment过程，返回”continue”，则流程继续，否则激活流程失败，发送激活拒绝消息给UE； 
C2：CAMEL_GPRS_PDP_Context_Establishment_Acknowledgement过程，返回”continue”，则流程继续，否则激活流程失败，发送激活拒绝消息给UE； 
如果该用户签约了CAMEL，但是SGSN未配置Ge口，则不发起 
C1：CAMEL_GPRS_PDP_Context_Establishment过程； 
C2：CAMEL_GPRS_PDP_Context_Establishment_Acknowledgement过程； 
Secondary PDP Context Activation Procedure
图4  Secondary PDP Context Activation Procedure for A/Gb mode
图5  Secondary PDP Context Activation Procedure for Iu mode
手机发送二次激活请求消息到SGSN，携带关联TI，NSAPI、TI、请求的QoS、TFT参数； 如果SGSN决定可以在RNC和GGSN之间建立DT，SGSN在第4步的RAB指派请求消息中携带DT隧道的参数到RNC，并且在第6步的更新GGSN流程中，SGSN携带DT隧道下行数据接收的IP地址和TEID； 
A/Gb 模式下，SGSN判断“Gb口激活PDP鉴权”设置为是，则SGSN对用户进行鉴权，否则不进行鉴权过程. 
SGSN使用二次激活请求消息中的Link TI校验TI是否合法，使用该TI的首次激活的PDP上下文中的GGSN地址被选择，SGSN发送Create
PDP Context Request消息到GGSN，携带协商的QoS、TEID、NSAPI、Primary NSAPI，TFT等参数；GGSN返回Create
PDP Context Response携带TEID、协商的QoS、Cause等参数。 
在Iu接入模式，SGSN发起RAB指派过程. 其中SGSN判断满足建立单隧道条件，通知RNC GGSN用户面信息。 
A/Gb模式下，SGSN判断终端支持PFC，用户接入的NSE支持PFC并且通过PFI映射配置的PFI值为有效值，SGSN通知BSS执行分组流上下文过程。 
如果在RAB指派流程中，QoS参数被RNC降低或者支持建立DT，SGSN发送Update PDP Context Requset消息到GGSN，携带QoS、RNC用户面地址和TEIDU、DTI标记，GGSN在Update
PDP Context Reponse消息中确认是否接受QoS。 
SGSN发送二次激活接受消息给手机，携带TI、协商的QoS、无线传输优先级信息。SGSN可以开始转发上下行数据报文并且开始计费。 
在步骤1和步骤6完成后，有一个CAMEL检查点C1和C2： 
如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起 
C1：CAMEL_GPRS_PDP_Context_Establishment过程，返回”continue”，则流程继续，否则激活流程失败，发送激活拒绝消息给UE； 
C2：CAMEL_GPRS_PDP_Context_Establishment_Acknowledgement过程，返回”continue”，则流程继续，否则激活流程失败，发送激活拒绝消息给UE； 
如果该用户签约了CAMEL，但是SGSN未配置Ge口，则不发起 
C1：CAMEL_GPRS_PDP_Context_Establishment过程； 
C2：CAMEL_GPRS_PDP_Context_Establishment_Acknowledgement过程； 
Network-Requested PDP Context Activation Procedure
图6  Successful Network-Requested PDP Context Activation Procedure
当GGSN收到了一个下行PDP分组数据报文，决定发起网络侧激活。GGSN保存发向该PDP地址的PDP分组数据。 
GGSN发送路由信息获取消息到HLR，如果HLR判断该请求可以接受，返回响应消息给GGSN携带用户的IMSI和SGSN地址以及终端不可达的原因。如果HLR判断该请求不接受，返回路由信息获取响应消息给GGSN，携带IMSI、MAP错误原因。 
如果HLR返回响应消息携带了SGSN地址并且不携带MNRG标记、不携带寻呼无响应标，GGSN发送PDU Notification
Request消息给SGSN携带IMSI、PDP类型、PDP地址、APN，SGSN返回PDU Notification Response消息给GGSN，通知GGSN该激活请求已经开始。 
SGSN发送Request PDP Context Activation消息给终端携带TI、PDP类型、PDP地址、APN参数，请求终端发起激活。 
终端发起PDP激活过程。 
系统影响 : 
随着PDP激活数的增加，系统资源占用会一直增大，CPU占用率会相应上升。 
应用限制 : 
无 
特性交互 : 
由于PDP激活流程是基本业务流程，是后续所有PDP相关流程的基础，如果无法使用，则其他PDP相关的业务都无法使用。 
业务|交互
---|---
PDP激活与鉴权|2G接入的时候在PDP激活流程中涉及到鉴权，鉴权失败则激活流程失败。
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060 "General Packet Radio Service (GPRS); Service
description; Stage 2". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service (GPRS); Base
Station System (BSS) - Serving GPRS Support Node (SGSN); BSS GPRS
Protocol (BSSGP)". 
3GPP TS 29.060: "General Packet Radio Service (GPRS); GPRS
Tunnelling Protocol (GTP) across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part (MAP) specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
首次或二次PDP激活流程完成后，激活了一个PDP上下文。 
SGSN支持1200万用户接入，支持2400万PDP上下文。本文档中提供的指标值，是在一定条件下得出的，实际商用配置要依据实际话务模型和其他特定需求，协商确定。 
可获得性 : 
版本要求及变更记录
无 
License 要求
无 
对其他网元的要求
无 
工程规划要求
无 
O&M相关 : 
命令
配置项无 
安全变量无 
定时器无 
软件参数无 
动态管理无 
性能统计
性能计数器参见 [表3].
测量类型名称|性能计数器名称
---|---
SGSN会话测量|所有计数器标识由C40507开始
性能指标参见 [表4].
测量类型名称|性能指标名称
---|---
SGSN会话测量|MS激活会话成功率（%）-UMTSMS激活会话成功率（%）-GSMMS激活会话成功率（去除用户原因）（%）-UMTSMS激活会话成功率（去除用户原因）（%）-GSM二次激活会话成功率（%）-UMTS二次激活会话成功率（%）-GSM激活PDP上下文时发起的DNS解析成功次数激活PDP上下文时发起的DNS解析成功率（%）由于流程冲突引起的PDP激活终止次数-UMTS由于流程冲突引起的PDP激活终止次数-GSMMS激活会话成功率（SGSN原因）（%）-UMTSMS激活会话成功率（SGSN原因）（%）-GSM
告警和通知
无 
业务观察/失败观察
无 
话单与计费
激活成功，开启SCDR话单。 
特性配置 : 
摘要GnGp SGSN网元PDP激活流程配置特性调整特性测试用例常见问题处理 
#### GnGp SGSN网元PDP激活流程配置特性 
配置说明
无 
配置前提
SGSN局基本配置已经完成，满足附着流程的要求。 
配置过程
使用命令[ADD GPRS APN] 配置APN，参数说明如下：
参数名称|含义|填写说明
---|---|---
APN名称|APN名称|字符类型，参数范围：1-82
IP地址|解析APN得到的IP地址|一般填写GGSN GTPC地址
计费模板标识|计费模板标识|标识范围：0～31
支持DT功能|支持DT功能|支持、不支持、根据签约
支持双栈功能|支持双栈功能|支持、不支持
使用命令[ADD APNCTPL]，配置计费模板，参数说明如下：
参数名称|含义|填写说明（建议值）
---|---|---
计费模板标识|计费模板标识|标识范围：0～31
计费方式|选择计费方式|时间计费、流量计费、时间和流量计费
计费流量门限|设置计费流量门限|单位：字节，取值范围：102400-4096000000
计费时间门限|设置计费时间门限|单位：分钟，取值范围：5-4320
最大部分话单数|最大部分话单数|单位：个，取值范围：1-9
无线承载释放时间|设置无线承载释放时间|单位：分钟，取值范围：30-4320
无活动PDP存在时长|设置无活动PDP存在时长|单位：分钟，取值范围：360-4294967295
用户别名|用户别名|单位：字符，取值范围：0～50
配置实例
配置APN解析Command ScriptDescriptionADD GPRS APN:APN="zte.com.mnc003.mcc460.gprs",IPADDR="200.85.1.159",CTPLID=1配置APN解析。 
配置APN计费模板Command ScriptDescriptionADD APNCTPL:TPLID=1,TYPE="TIMEFLOW",TIMELMT=30,FLOWLMT=10485762,MAXFRAG=5,RABTIMELMT=33,PDPTIMELMT=444,NAME="apnctrl1"配置APN计费模板。 
调整特性 : 
无 
测试用例 : 
测试项目|PDP 上下文激活
测试目的|验证移动用户可以使用动态 PDP 地址发起建立 PDP 上下文。
预置条件|网络中各网元系统、操作维护台以及到外部 PDN 网络的路由正常。用户分别通过2G、3G网络接入。用户在HLR中已签约GPRS业务，用户签约动态 PDP 地址
测试过程|用户发起GPRS附着。用户发起PDP 上下文激活，采用动态 PDP 地址。用户进行分组数据业务。
通过准则|用户GPRS附着成功。用户成功激活上下文，地址为 GGSN 或外部网络动态分配。分组数据业务正常。
测试结果|-
常见问题处理 : 
无 
## ZUF-77-02-002 二次PDP上下文激活 
概述 : 
ZXUN uMAC支持二次PDP上下文激活。在此激活过程中，MS的APN和请求的IP地址需与首次激活的PDP上下文中的一致。  
收益 : 
通过本特性，用户可以使用相同APN和IP地址建立多个PDP上下文。这些PDP上下文使用同样的信令信道，但使用不同的数据信道。本特性支持不同应用类型使用不同的QoS等级，从而节省了IP资源，系统可以分别控制不同质量要求的业务，以达到有效利用资源的目的。 
描述 : 
用户已激活一个PDP上下文用于传输数据，而另一个不同QoS等级的数据业务也要求使用同样的IP地址和APN进行数据传输。在此情况下，可执行二次PDP上下文激活。在二次激活成功后，SGSN间的两个PDP上下文共享同一个GTP信道用于信令传输。配置不同QoS等级的GTP数据信道可分别执行两个具有不同传输质量等级要求的业务，而且每个业务都是相互独立的。 
二次PDP上下文激活流程通过重用已激活PDP上下文的PDP地址和其他信息来激活其他具有不同QoS概要文件的PDP上下文，而无需进行APN选择和PDP地址协商。共享相同PDP地址和APN的多个PDP上下文通过唯一的TI和唯一的NSAPI进行区分。 
如果其他使用相同PDP地址和APN的已激活PDP上下文已有一个关联的话务流量模型（TFT），二次PDP上下文激活流程仍可执行而无需提供话务流量模型（TFT）。反之，则需要提供该模型。话务流量模型包含的属性指定了一个IP头域过滤器，用于将来自外部互连的分组数据网的数据包指向新激活的PDP上下文。 
## ZUF-77-02-003 网络侧发起PDP激活 
概述 : 
当外部网络需要接入MS时，SGSN在收到SGSN通知消息后，通知MS进行PDP上下文激活流程并建立数据传输链路。  
收益 : 
本特性支持外部网络主动接入用户，从而丰富了业务类型，例如PUSH业务。 
描述 : 
当GGSN从外部网络接收到需要传送给MS的数据时，需要使用网络侧业务。GGSN可接收SGSN位置管理消息，并将MS位置消息发送给SGSN。当GGSN发送PDU通知请求给SGSN时，SGSN可通知MS进行PDP上下文激活。当PDP上下文激活成功后，来自外网的数据就可传送给MS。关于网络侧发起PDP激活的流程，请参考3GPP
23.060和29.060协议。 
MS需要配置静态IP地址，GGSN应存储该信息在表中以便将静态IP地址映射到MS的IMSI。这样，GGSN可使用IMSI在HLR上查询SGSN的地址，并发送PDUT通知消息给该SGSN。在这种情况下，GGSN和HLR间的连接可能需要通过MAP
GSN功能进行转接。  
## ZUF-77-02-004 PDP上下文修改 
特性描述 : 
摘要术语描述应用场景客户收益实现原理系统影响应用限制特性交互遵循标准特性能力O&M相关 
术语 : 
术语|含义
---|---
GPRS|分组域的分组承载业务。
A/Gb模式|A/Gb模式指该子句或段落仅适用于在A/Gb模式中运行的系统或子系统，例如，根据无线接入网和核心网之间的A接口或Gb接口的使用，带有功能划分的系统或子系统。
Iu模式|Iu模式指该子句或段落仅适用于在Iu模式中运行的系统或子系统，例如，根据无线接入网和核心网之间的Iu-CS接口或Iu-PS接口的使用，带有功能划分的系统或子系统。
MS|该规范不区分MS和UE。
2G/3G|2G和3G前缀分别指支持A/Gb模式或Iu模式的系统或子系统，例如，2G SGSN是指当SGSN作为A/Gb模式下的MS时，SGSN的所有功能。
描述 : 
定义
GnGp SGSN网元PDP修改流程是2/3G用户注册到PS网络上后，由MS，SGSN，GGSN，RNC，HLR发起修改PDP过程，其中SGSN可以对已经激活PDP的QoS，直传隧道的使用进行修改，还可以配合完成PDP Address 或TFT的修改。
在PDP修改过程中，GnGp SGSN为用户协商QoS，通知GGSN更新PDP上下文，或通知UE修改PDP上下文；
Gb接入时，GnGp SGSN可以通知BSS建立分组流上下文；
Iu接入时，可以通知RNC修改无线承载，在RNC返回的QoS降低情况下或在建立单隧道情况下通知GGSN更新PDP上下文。
PDP修改完成之后，用户可以通过PS网络修改之后的PDP访问数据业务和其他业务。
背景知识
GPRS网络架构如[图1]所示。
图1  GPRS架构图
TE/MT：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。
BSS：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。 UTRAN：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。
HLR：永久存储用户签约数据。
PDN：为用户提供业务的网络。
CGF：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。
BS：负责接收和处理从核心网发送过来的CDR文件。
EIR：负责检查UE设备。
PSCN：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元：
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM）上下文和分组数据协议（PDP）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息；
GGSN：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务：
MSC/VLR：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。
SMS GMSC/SMS
IWMSC：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。
CAMEL：该功能实体主要对用户进行在线计费。
应用场景 : 
SGSN网元PDP修改流程是基本流程，用户原有激活PDP的QoS，直传隧道的使用，PDP Address，TFT不再满足业务需求，可以通过PS网络修改原有的PDP来访问数据业务和其他业务。具体常见场景包括：
SGSN发起PDP修改，可以修改QoS，直传隧道的使用。 
GGSN发起的PDP修改，可以修改QoS，TFT，PDP Address或直传隧道的使用。 
MS发起的PDP修改，可以修改QoS，TFT或直传隧道的使用。 
RNC发起Iu释放触发的PDP修改，可以修改QoS或直传隧道的使用。 
RNC发起RAB释放触发的PDP修改，可以修改QoS或直传隧道的使用。 
RNC发起的RAB修改，可以修改QoS或直传隧道的使用。 
HLR发起QoS修改，可以修改QoS或直传隧道的使用。 
客户收益 : 
受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的PS网络上激活了PDP后，运营商可以修改用户的PDP相关信息为用户提供各种数据业务和其他业务。
移动终端用户|终端用户因有业务需求而通知SGSN修改QoS或TFT。
实现原理 : 
涉及的网元
SGSN网元PDP修改流程需要UE、BSS/RNC、SGSN、GGSN、HLR的共同配合：
UE：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等。在PDP修改过程中具体功能包括触发PDP修改，完成UEPDP上下文的修改。 
BSS：为终端的接入提供无线资源，对用户提供接入层安全功能。在PDP修改过程中具体功能包括可以建立分组流上下文，透传UE和SGSN的NASPDP修改相关消息。 
RNC：为终端的Iu（无线接入网络和核心网的一种接口）接入提供无线资源。在PDP修改过程中具体功能包括对用户修改无线承载资源，并通知UE修改无线承载，通知SGSN修改无线接入承载响应，透传UE和SGSN的NASPDP修改相关消息。 
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。在PDP修改过程中具体功能包括接收到UE/GGSN/SGSN的修改PDP请求后，协商QoS，为用户修改PDP相关信息，通知GGSN更新PDP上下文，用户Gb接入时，可以通知BSS建立分组流上下文；用户Iu接入时，通知RNC修改无线承载及在建立单隧道情况下或QoS降低时，通知GGSN更新PDP上下文。 
GGSN：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。在PDP修改过程中具体功能包括触发PDP修改，完成PDP修改。 
HLR：永久存储用户签约数据。在PDP修改过程中具体功能包括修改用户签约数据的QoS。 
CAMEL：该功能实体主要对用户进行在线计费。在PDP修改过程中主要控制激活流程是否可以继续，下发计费策略。 
业务流程
SGSN发起的PDP修改流程
SGSN发起的PDP修改流程如[图2]和[图3]所示。
图2  Gb口SGSN发起的PDP修改流程
图3  Iu口SGSN发起的PDP修改流程
SGSN发送Update PDP Context Request （TEID，NSAPI，QoS Negotiated，DTI）消息到GGSN。如果DT（单隧道）SGSN在消息中携带RNC用户面地址和TEID以及DTI标记给GGSN。
GGSN保存协商的QoS，返回Update PDP Context Response（TEID，QoS Negotiated，Cause）消息给SGSN。
A/Gb模式下，SGSN判断通过PFI映射配置的PFI值为有效值，SGSN通知BSS执行分组流上下文过程。
在Iu模式下，SGSN发起RAB指派流程修改空口的承载参数。其中SGSN判断满足建立单隧道条件，通知RNCGGSN用户面信息。
在RAB修改流程中，如果RNC减低了QoS，SGSN通过发送Update PDP Context Request消息给GGSN，把新协商的QoS参数通知给GGSN。
如果GGSN接受新的QoS发送Update PDP Context
Response消息给SGSN。如果在第四步RAB修改过程中，SGSN建立了DT，那么在Update PDP Context Request消息中SGSN应该携带RNC的用户面地址、TEID和DTI。
SGSN发送Modify PDP Context Request（TI，QoS Negotiated, Radio Priority）消息给终端。
如果接受修改的QoS参数，终端接受该PDP修改流程。终端返回Modify PDP Context Accept消息给SGSN。
在步骤7后，有一个CAMEL检查点C1。如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起C1
CAMEL_GPRS_Change_Of_QoS过程，返回“continue”。
GGSN发起的PDP修改流程
GGSN发起的PDP修改流程如[图4]和[图5]所示。
图4  Gb口GGSN发起的PPD修改流程
图5  Iu口GGSN发起的PDP修改流程
GGSN发送Update PDP Context Request（TEID，NSAPI，PDP Address，QoS Requested，TFT）消息到SGSN。
QoS参数只是GGSN希望的QoS是多少。PDP地址作为可选项。TFT作为可选项可以作为增加、删除、修改该PDP上下文对应的TFT。
A/Gb模式下，SGSN判断通过PFI映射配置的PFI值为有效值，SGSN通知BSS执行分组流上下文过程。
在Iu模式，SGSN执行RAB指派流程修改空口的无线参数。其中SGSN判断满足建立单隧道条件，通知RNCGGSN用户面信息。
SGSN发送Modify PDP Context Request（TI，PDP Address，QoS Negotiated，Radio
Priority，TFT）消息到终端。
终端如果支持修改的QoS或者TFT，终端如果接受该修改流程返回Modify PDP Context Accept消息给SGSN。
SGSN如果接收到了终端返回的Modify PDP Context Accept消息，或者完成了RAB指派过程，发送Update
PDP Context Response（TEID，QoS Negotiated）消息到GGSN。
在步骤6后，有一个CAMEL检查点C1。如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起C1
CAMEL_GPRS_Change_Of_QoS过程，返回“continue”。
终端发起的PDP修改流程
终端发起的PDP修改流程如[图6]和[图7]所示。
图6  Gb口终端发起的PDP修改流程
图7  Iu口终端发起的PDP修改流程
终端发送PDP Context Request（TI，QoS Requested，TFT）消息到SGSN，用于修改QoS或者TFT，或者QoS和TFT。QoS指出终端希望的QoS参数，TFT指出终端希望修改该PDP对应的TFT参数。
SGSN发送Update PDP Context Request（TEID，NSAPI，QoS Negotiated，TFT，DTI）消息到GGSN。如果建立了DT，那么SGSN在该消息中携带RNC的用户面地址和TEID。
GGSN保存协商的QoS参数，修改或者删除PDP上下文对应的TFT，返回Update PDP Context Response（TEID，QoS Negotiated）消息给SGSN。
A/Gb模式下，SGSN判断通过PFI映射配置的PFI值为有效值，SGSN通知BSS执行分组流上下文过程。
Iu模式下，SGSN执行RAB指派过程修改空口的承载参数。如果不存在RAB，那么将通过RAB指派流程建立RAB。其中SGSN判断满足建立单隧道条件，通知RNCGGSN用户面信息。
如果在RAB指派或者修改流程中RNC降低了QoS参数，SGSN通过发送Update PDP Context Request消息给GGSN，携带最新的QoS参数。
GGSN确认接受了该QoS参数，返回Update PDP
Context Response消息给SGSN。如果在RAB指派或者修改过程中建立了DT，那么SGSN在Update PDP Context
Request消息中携带RNC的用户面地址和TEID，以及DTI。
SGSN发送Modify PDP Context Accept（TI，QoS Negotiated，Radio Priority）消息给终端。在步骤7后，有一个CAMEL检查点C1。如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起C1
CAMEL_GPRS_Change_Of_QoS过程，返回“continue”。
RNC触发的PDP修改流程
RNC触发的PDP修改流程如[图8]所示。
图8  Iu释放流程
RNC向SGSN发送Iu Release Request（Cause）消息。
如果释放RAB对应的PDP建立了单隧道，PDP上下文保留，SGSN向GGSN发送Update
PDP Context Request消息建立SGSN与GGSN的隧道，GGSN给SGSN回Update PDP Context Response消息。
如果PDP上下文的业务类型是流类或会话类，PDP上下文保留，SGSN将最大上下行比特率降为0，向GGSN发送Update PDP Context Request消息通知GGSN将最大上下行比特率降为0，GGSN给SGSN回Update PDP Context
Response消息。
如果PDP上下文的业务类型是交互类或背景类，PDP上下文不改变。
SGSN向RNC发送Iu Release Command（Cause）消息。
如果存在RRC连接，RAN发送Release RRC Connection message消息给终端。
终端发送Release RRC Connection Acknowledge message消息到RAN。
RNC向SGSN发送Iu Release Completion消息。
RAB释放触发的PDP修改流程
RAB释放触发的PDP修改流程如[图9]所示。
图9  RAB释放流程
RNC向SGSN发送RAB Release Request（RAB ID，Cause）消息。
如果释放RAB对应的PDP建立了单隧道，PDP上下文保留，SGSN向GGSN发送Update PDP
Context Request消息建立SGSN与GGSN的隧道，GGSN给SGSN回Update PDP Context Response消息。
如果PDP上下文的业务类型是流类或会话类，PDP上下文保留，SGSN将最大上下行比特率降为0，向SGSN发送Update PDP Context Request消息通知GGSN将最大上下行比特率降为0，GGSN给SGSN回Update PDP Context
Response消息。
如果PDP上下文的业务类型是交互类或背景类，PDP上下文不改变。
SGSN发送RAB Assignment Request（RAB ID，Cause）消息给RNC释放RAB。
如果Radio Bearer存在，那么Radio Bearer将会被释放。 
UTRAN发送RAB Assignment Response消息给SGSN。
RNC触发的RAB修改流程
RNC发起的RAB修改流程用于RAN修改已经建立的RAB的RAB参数，如[图10]所示。
图10  RAN发起的RAB修改流程
RAN发送RAB Modify Request（RAB ID，RAB Parameter Values）消息到SGSN。
SGSN如果接受该修改，则发起如[SGSN发起的PDP修改流程]描述的流程。
HLR触发的PDP修改流程
HLR触发的PDP修改流程如[图11]所示。
图11  HLR发起的PDP修改流程
HLR发送插入用户数据消息到SGSN。
SGSN更新用户新的签约数据，发送插入用户数据响应消息给HLR。
SGSN对于已经建立的PDP上下文进行检查，查看PDP上下文对应的签约PDP信息是否发生了变化。
对于新的或者没有使用的签约PDP上下文，SGSN除了保存之外不进行任何后续的处理。
对于已经使用的PDP上下文，SGSN检查QoS参数是否发生了改变，如果QoS发生了改变，SGSN发起PDP修改流程。
系统影响 : 
随着PDP修改数的增加，系统资源占用会一直增大，CPU占用率会相应上升。
应用限制 : 
无 
特性交互 : 
由于PDP修改流程是基本业务流程，是满足用户因业务需要而修改PDP的流程，如果无法使用，则用户某些业务需求无法满足。
业务|交互
---|---
PDP修改与计费|用户修改的时候需要如果满足条件出SCDR话单。
遵循标准 : 
3GPP TS 23.060 "General Packet Radio Service (GPRS); Service description;
Stage 2". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 25.413: "UTRAN Iu
Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet
Radio Service (GPRS); Base Station System (BSS) - Serving GPRS Support
Node (SGSN); BSS GPRS Protocol (BSSGP)". 
3GPP TS 29.060: "General
Packet Radio Service (GPRS); GPRS Tunnelling Protocol (GTP) across
the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application
Part (MAP) specification". 
3GPP TS 23.003: "Numbering, addressing
and identification" 
3GPP TS 24.007: "Mobile radio interface
signalling layer 3; General aspects". 
特性能力 : 
PDP修改流程完成后，PDP上下文数不变。
SGSN支持1200万用户接入，支持2400万PDP上下文，该PDP上下文可以是修改的PDP。本文中提供的指标值，是在一定条件下得出的，实际商用配置要依据实际话务模型和其他特定需求，协商确定。
O&M相关 : 
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
SGSN会话测量|C405070037 MS修改会话请求次数-UMTSC405070038 MS修改会话请求次数-GSMC405070039 MS修改会话成功次数-UMTSC405070040 MS修改会话成功次数-GSMC405070041 SGSN修改会话的请求次数-UMTSC405070042 SGSN修改会话的请求次数-GSMC405070043 SGSN修改会话的成功次数-UMTSC405070044 SGSN修改会话的成功次数-GSMC405070045 GGSN更新会话的请求次数-UMTSC405070046 GGSN更新会话的请求次数-GSMC405070047 GGSN更新会话的成功次数-UMTSC405070048 GGSN更新会话的成功次数-GSMC405070049 SGSN更新会话的请求次数-UMTSC405070050 SGSN更新会话的请求次数-GSMC405070051 SGSN更新会话的成功次数-UMTSC405070052 SGSN更新会话的成功次数-GSM
告警和通知
无 
业务观察/失败观察
无 
话单与计费
激活修改成功，如果达到最大碎片数，则输出SCDR话单。 
特性配置 : 
摘要配置特性测试用例常见问题处理 
配置特性 : 
配置前提
UE、BSS/RNC、SGSN、GGSN等各网元工作正常
SGSN网管服务器、客户端连接正常；服务器与OMP连接正常；SGSN已经配置好相关的本地配置。
用户已经激活成功。 
配置过程
无 
配置实例
无 
测试用例 : 
测试项目|MS发起的PDP上下文修改流程
测试目的|验证MS发起的PDP上下文修改流程
预置条件|网络中各网元系统、操作维护台以及到外部PDN网络的路由正常。用户分别通过2G、3G网络接入。用户在HLR中已签约GPRS业务。
测试过程|用户发起GPRS附着并激活PDP上下文。用户发起PDP上下文修改QoS和TFT。用户进行分组数据业务。
通过准则|用户GPRS附着及PDP上下文激活成功。用户成功修改QoS，GGSN的TFT被修改。可以用新的QoS进行分组数据传输。
测试项目|SGSN发起的PDP上下文修改流程
测试目的|验证SGSN发起的PDP上下文修改流程。
预置条件|网络中各网元系统、操作维护台以及到外部PDN网络的路由正常。用户分别通过2G、3G网络接入。用户在HLR中已签约GPRS业务。
测试过程|用户发起GPRS附着并激活PDP上下文。SGSN发起PDP上下文修改流程。用户进行分组数据业务。
通过准则|用户GPRS附着及PDP上下文激活成功。成功修改QoS。可以用新的QoS进行分组数据传输。
测试项目|GGSN发起的PDP上下文修改流程
测试目的|验证GGSN发起的PDP上下文修改流程。
预置条件|网络中各网元系统、操作维护台以及到外部PDN网络的路由正常。用户分别通过2G、3G网络接入。用户在HLR中已签约GPRS业务。
测试过程|用户发起GPRS附着并激活PDP上下文。触发GGSN发起的PDP上下文修改流程。用户进行分组数据业务。
通过准则|用户GPRS附着及PDP上下文激活成功。成功修改QoS。可以用新的QoS进行分组数据传输。
测试项目|Iu释放引起的PDP上下文修改。
测试目的|验证RNC发起的PDP上下文修改流程。
预置条件|网络中各网元系统、操作维护台以及到外部 PDN 网络的路由正常。用户通过3G网络接入。用户在HLR中已签约GPRS业务。
测试过程|用户发起GPRS附着并激活PDP上下文，traffic类型为streaming。RNC发起释放Iu。
通过准则|用户GPRS附着及PDP上下文激活成功。Iu成功释放，PMM状态为PMM-IDLE。SGSN和GGSN上的上下文MAX_BIT_RATE降为0。
常见问题处理 : 
无 
## ZUF-77-02-005 PDP去激活 
特性描述 : 
摘要术语描述应用场景客户收益实现原理系统影响应用限制特性交互遵循标准特性能力可获得性O&M相关 
术语 : 
术语|含义
---|---
GPRS|分组域的分组承载业务。
A/Gb模式|A/Gb模式指该子句或段落仅适用于在A/Gb模式中运行的系统或子系统，例如，根据无线接入网和核心网之间的A接口或Gb接口的使用，带有功能划分的系统或子系统。
Iu模式|Iu模式指该子句或段落仅适用于在Iu模式中运行的系统或子系统，例如，根据无线接入网和核心网之间的Iu-CS接口或Iu-PS接口的使用，带有功能划分的系统或子系统。
MS|该规范不区分MS和UE。
2G/3G|2G和3G前缀分别指支持A/Gb模式或Iu模式的系统或子系统，例如，2G SGSN是指当SGSN作为A/Gb模式下的MS时，SGSN的所有功能。
描述 : 
定义
GnGp SGSN网元PDP去活流程是由MS,SGSN或GGSN发起的PDP去活过程，用来去活用户的一个PDP，或者去活相同PDP地址的所有PDP。
在PDP去活过程中，GnGp SGSN通知GGSN删除PDP上下文，或通知UE删除PDP上下文；
Gb接入时，GnGp SGSN可以通知BSS删除分组流上下文；
Iu接入时，可以通知RNC释放无线承载；
PDP去活完成之后，用户不可以再通过PS网络去活的PDP访问数据业务和其他业务。
背景知识
GPRS网络架构图，如[图1]所示，其中包含了如下网元。
图1  GPRS架构图
TE/MT（Terminal Equipment/Mobile Terminal，终端设备/移动终端）：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS（Base Station System，基站系统）：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。
UTRAN（UMTS Terrestrial Radio Access Network，统一的陆地无线接入网络）：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
HLR(Home Location Register，归属位置寄存器):永久存储用户签约数据。 
PDN(Packet
Data Network，分组数据网)：为用户提供业务的网络。 
CGF(Charging Gateway Functionality，计费网关功能)：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS（Billing System，计费系统）：负责接收和处理从核心网发送过来的CDR文件。 
EIR（equipment
identity register 设备标识寄存器）：负责检查UE设备。 
PS CN（Packet Switched Core
Network，分组交换核心网）：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元： 
SGSN(Serving
GPRS Support Node，服务GPRS支持节点)：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS
Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息； 
GGSN(Gateway GPRS Support Node，GPRS支持节点网关)：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务： 
MSC/VLR（Mobile Switch
Center/ Visitor Location Register，移动交互中心/拜访位置寄存器）：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMS GMSC/SMS IWMSC (Short Message Service Gateway MSC/ Short Message
Service Interworking MSC，短消息网管移动交换中心/短消息互通移动交换中心)：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL (Customised Applications for Mobile network Enhanced Logic，移动网络定制应用增强逻辑服务器)：该功能实体主要对用户进行在线计费。 
应用场景 : 
SGSN网元PDP去活流程是基本流程，用户不再想要通过PS网络激活的PDP访问数据业务和其他业务，可以通过去激活流程删除PDP。具体常见场景包括：
以下流程可以去活一个PDP或相同PDP地址的所有PDP：
MS发起的PDP去激活；
SGSN发起的PDP去激活；
GGSN发起的PDP去激活；
客户收益 : 
受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的PS网络上激活了PDP后，使运营商可以去激活PDP不再为用户提供各种数据业务和其他业务。
移动终端用户|终端用户因不再需要通过激活的PDP访问业务而通知SGSN去激活PDP。
实现原理 : 
系统架构
无 
涉及的网元
SGSN网元PDP去活流程需要UE、BSS/RNC、SGSN、GGSN的共同配合： 
UE（User Equipment，用户设备）：为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等。在PDP去活过程中具体功能包括触发PDP去活，完成UE
PDP上下文的去活。
BSS（Base Station System，基站系统）：为终端的接入提供无线资源，对用户提供接入层安全功能。在PDP去活过程中具体功能包括可以删除分组流上下文，透传UE和SGSN的NAS
PDP去活相关消息。 
RNC（Radio Network Controller，无线网络控制器）：为终端的Iu（无线接入网络和核心网的一种接口）接入提供无线资源。在PDP去活过程中具体功能包括对用户释放无线承载资源，并通知UE释放无线承载，通知SGSN释放无线接入承载响应，透传UE和SGSN的NAS
PDP去活相关消息。 
SGSN(Serving GPRS Support Node，服务GPRS支持节点)：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS
Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。在PDP去活过程中具体功能包括接收到UE/GGSN/SGSN的去活PDP请求后，删除用户PDP相关信息，通知GGSN去活PDP上下文，用户Gb接入时，可以通知BSS删除分组流上下文；用户Iu接入时，通知RNC释放无线承载。 
GGSN(Gateway GPRS Support Node，GPRS支持节点网关)：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。在PDP去活过程中具体功能包括触发PDP去活，完成PDP去活。 
CAMEL (Customised Applications for Mobile network Enhanced Logic，移动网络定制应用增强逻辑服务器)：该功能实体主要对用户进行在线计费。在去活过程中主要对用户计费信息进行采集。 
协议栈
无 
本网元实现
无 
业务流程
终端发起的PDP去激活流程
终端在Gb接口和Iu接口发起的去活流程在[图2]和[图3]分别进行描述。
图2  Gb口终端发起的去活流程
图3  Iu口终端发起的去活流程
终端发送Deactivate PDP Context Request (TI, Teardown Ind) 消息到 SGSN.
A/Gb 模式下, SGSN判断“Gb口去活PDP鉴权”设置为是，则SGSN对用户进行鉴权，否则不进行鉴权过程.
SGSN发送Delete PDP Context Request(TEID, NSAPI, Teardown Ind)消息到到GGSN。如果终端发送的去活消息中携带了‘Teardown
Ind’，那么SGSN去活和当前PDP上下文使用的PDP地址相同的所有PDP，发送的Delete PDP Context Request消息中携带 ‘Teardown Ind’。GGSN删除相关的所有PDP，并且返回Delete PDP Context
Response (TEID)消息给SGSN。
SGSN返回Deactivate PDP Context Accept (TI) 消息给终端。
在Iu口，如果PDP上下文对应的RAB存在，SGSN在Iu接口发起RAB释放流程。 6) A/Gb模式下,SGSN判断PDP上下文的PFI值为有效值并且没有其他上下文使用该PFI，SGSN通知BSS执行分组流上下文过程。
在步骤1完成后，有一个CAMEL检查点C1： 
如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起 C1)	CAMEL_GPRS_PDP_Context_Disconnection.过程，返回”continue”；
SGSN发起的PDP去活流程如图3所示。
图4  SGSN发起的PDP去激活流程
SGSN发送 Delete PDP Context Request (TEID, NSAPI, Teardown Ind) 消息到 GGSN.。SGSN如果想去活使用该PDP地址的所有PDP上下文，SGSN发送Delete PDP
Context Request消息到GGSN携带‘Teardown Ind’指示。GGSN删除使用该PDP地址的所有PDP上下文，并且返回Delete
PDP Context Response (TEID) 消息到SGSN。 
SGSN发送Deactivate PDP Context Request (TI, Teardown Ind, Cause)消息给终端，如果携带了‘Teardown
Ind’那么终端去活使用该PDP地址的所有PDP上下文，并且返回Deactivate PDP Context Accept (TI)消息到SGSN。
在Iu接口，如果存在RAB那么SGSN发起RAB释放流程。
A/Gb模式下,SGSN判断PDP上下文的PFI值为有效值并且没有其他上下文使用该PFI，SGSN通知BSS执行分组流上下文过程。
在步骤1完成后，有一个CAMEL检查点C1： 
如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起 C1)	CAMEL_GPRS_PDP_Context_Disconnection.过程，返回”continue”；
图5   GGSN发起的PDP去活流程
GGSN发送Delete PDP Context Request (TEID, NSAPI, Teardown Ind)消息到SGSN，如果携带‘Teardown
Ind’那么使用该PDP地址的所有PDP上下文都去激活；
Deactivate PDP Context Request (TI, Teardown Ind, Cause)消息到终端，如果携带了如果携带‘Teardown
Ind’那么终端对使用该PDP地址的所有PDP上下文都去激活，终端返回Deactivate PDP Context Accept (TI)消息给SGSN；
SGSN发送Delete PDP Context Response (TEID) 消息到GGSN。 
在Iu接口，如果存在RAB那么SGSN发起RAB释放流程；
A/Gb模式下,SGSN判断PDP上下文的PFI值为有效值并且没有其他上下文使用该PFI，SGSN通知BSS执行分组流上下文过程。
在步骤1完成后，有一个CAMEL检查点C1： 
如果该用户签约了CAMEL，且SGSN存在Ge口配置，则发起 C1)	CAMEL_GPRS_PDP_Context_Disconnection.过程，返回”continue”；
系统影响 : 
随着PDP去激活数的增加，系统资源占用会减少，CPU占用率会相应下降。
应用限制 : 
无 
特性交互 : 
由于PDP去激活流程是基本业务流程，是满足用户不再访问业务需求的流程，如果无法使用，则用户不能停止基于某PDP的业务使用。
业务|交互
---|---
PDP去激活与计费|用户去激活的时候需要出SCDR话单。
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060 "General Packet Radio Service
(GPRS); Service description; Stage 2". 
3GPP TS 24.008: "Mobile
Radio Interface Layer 3 specification; Core Network Protocols; Stage
3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service (GPRS); Base Station
System (BSS) - Serving GPRS Support Node (SGSN); BSS GPRS Protocol
(BSSGP)". 
3GPP TS 29.060: "General Packet Radio Service (GPRS);
GPRS Tunnelling Protocol (GTP) across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part (MAP) specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3; General
aspects". 
特性能力 : 
PDP去活流程完成后，PDP上下文数相应减少。
SGSN支持1200万用户接入，支持2400万PDP上下文，该PDP上下文可以是被去活的PDP。本文档中提供的指标值，是在一定条件下得出的，实际商用配置要依据实际话务模型和其他特定需求，协商确定。
可获得性 : 
版本要求及变更记录
无 
License要求
无 
对其他网元的要求
无 
工程规划要求
无 
O&M相关 : 
命令
配置项无 
安全变量无 
定时器无 
软件参数无 
动态管理无 
性能统计
性能计数器参见[表4]。
测量类型名称|性能计数器名称
---|---
SGSN会话测量|C405070142 SGSN去激活会话请求次数-UMTSC405070143 SGSN去激活会话请求次数-GSMC405070144 SGSN去激活会话的成功次数-UMTSC405070145 SGSN去激活会话的成功次数-GSMC405070025 MS去激活会话的请求次数-UMTSC405070026 MS去激活会话的请求次数-GSMC405070027 MS去激活会话的成功次数-UMTSC405070028 MS去激活会话的成功次数-GSMC405070029 GGSN去激活会话的请求次数-UMTSC405070030 GGSN去激活会话的请求次数-GSMC405070031 GGSN去激活会话成功次数-UMTSC405070032 GGSN去激活会话成功次数-GSM
告警和通知
无 
业务观察/失败观察
无 
话单与计费
去激活成功，出SCDR话单。 
特性配置 : 
摘要配置特性调整特性测试用例常见问题处理 
配置特性 : 
配置说明
无 
配置前提
UE、BSS/RNC、SGSN、GGSN等各网元工作正常
SGSN网管服务器、客户端连接正常；服务器与OMP连接正常；SGSN已经配置好相关的本地配置；
用户已经激活成功； 
配置过程
无 
配置实例
无 
调整特性 : 
无 
测试用例 : 
测试项目|MS发起去活 PDP 上下文
测试目的|验证 MS 发起的 PDP 上下文去活流程正常
预置条件|网络中各网元系统、操作维护台以及到外部 PDN 网络的路由正常用户分别通过2G、3G网络接入用户在HLR中已签约GPRS业务
测试过程|用户发起GPRS附着并激活 PDP 上下文用户发起去活请求
通过准则|用户GPRS附着及PDP上下文激活成功PDP上下文去活成功
测试项目|SGSN 发起PDP 上下文去活
测试目的|验证 SGSN 发起的 PDP 上下文去活流程
预置条件|网络中各网元系统、操作维护台以及到外部 PDN 网络的路由正常用户分别通过2G、3G网络接入用户在HLR中已签约GPRS业务
测试过程|用户发起GPRS附着并激活 PDP 上下文SGSN 发起PDP 上下文去活
通过准则|用户GPRS附着及PDP上下文激活成功PDP上下文去活成功
常见问题处理 : 
无 
## ZUF-77-02-006 PDP上下文保留 
概述 : 
当RAB被释放后，被激活的PDP上下文仍保留在网络侧。 
收益 : 
本特性减少了RAB重建所需的时间。 
描述 : 
当RAB释放后，被激活的PDP上下文仍保留在网络侧，这样减少了重建RAB所需的时间。 
## ZUF-77-02-007 Direct tunnel 
特性描述 : 
摘要术语描述应用场景客户收益实现原理系统影响遵循标准特性能力可获得性O&M相关 
术语 : 
术语|含义
---|---
双隧道模式|指传统的GGSN与SGSN之间、SGSN与RAN之间用户面分别采用GTP隧道。
单隧道模式|指GGSN与RAN之间用户面分别采用一条GTP隧道。
描述 : 
定义
DT（Direct Tunnel，直传隧道）是基于网络扁平化以及控制面用户面分离提出的，与SAE演进架构方向趋向一致。实现DT后，用户面数据直接在RNC和GGSN之间传输，SGSN只负责PDP上下文的建立与删除，不负责用户面数据报文的转发。这样数据转发处理就减少了一个网元节点，减少了网络处理复杂度和时延，同时降低了网络成本，同时，SGSN在DT时，不建立用户面资源，节省了SGSN的部分投资。DT是Iu接入模式下的一个可选功能。DT框架如[图1]所示。
图1  DT框架
DT功能在PS域的RAN和GGSN间使用直传用户面隧道。在直传隧道功能下，SGSN为RAN提供GGSN TEID和用户面地址、为GGSN提供RAN
TEID和用户面地址。直传隧道功能不应用在Gb接入的情况。
实现DT之后，PS域用户面的协议栈如[图2]所示。
图2  PS域用户面协议栈
背景知识
当为PDP上下文指派的RAB被释放而PDP上下文保留时，GGSN和SGSN之间的GTP-U通道需要被建立，以便处理下行数据包，如[图3]所示。
图3  RAB被释放时建立GTP-U通道
应用场景 : 
满足如下任何一个条件的情况下都不能够采用DT： 
漫游：SGSN和GGSN归属不同PLMN。 
SGSN从HLR收到的用户签约信息中包含camel签约信息，即CAMEL用户，这是因为：如果直传隧道建立，由于SGSN对用户面传输不再可见，从SGSN进行流量上报是不可能的。由于Camel服务可以在PDP存在的任何时候开始流程上报，在签约数据中包含camel信息时应该禁止直传隧道。 
监测用户受控时。 
RNC不支持单隧道时（RNC连接局附加属性中配置）。 
GGSN不支持单隧道时（GGSN不支持 GTP v1或者根据APN确定）。 
非IU接入情况下。 
如果是从非DT转为DT，则还要判断PDP是否DT抑制次数达到了安全变量配置的值（0为不抑制；255标识总是抑制），如果是，则不再执行DT，并记录抑制次数；如果没有达到，则执行DT，复位累计的抑制次数。 
客户收益 : 
受益方|受益描述
---|---
运营商|节约用户面承载资源；提升用户感受，更有利于提升用户忠诚度和吸引新用户。
移动用户|减少数据报文时延，上网更流畅。
实现原理 : 
涉及的网元
功能涉及到SGSN和GGSN的配合。 
网元|功能
---|---
SGSN|具有DT能力的SGSN要有能力配置每个RNC和GGSN是否支持直接用户面连接。SGSN处理控制面信令并决策何时建立直接通道。
GGSN|在DT情况下，GGSN收到RNC的用户面ERROR INDICATION消息时，需要给SGSN发更新消息指示SGSN释放对应的RAB资源。
本网元实现
对于GGSN是否支持DT，可以通过多种方式： 
本地根据APN进行配置 
本地根据GGSN的IP地址配置 
根据APN前缀控制：在HLR中签约带DT前缀的APN，并在SGSN中配置DT前缀，DT前缀的APN则认为是支持DT的。 
对于RNC是否支持DT，通过RNC局向配置控制。 
业务流程
IU接入用户激活时建立单隧道功能
IU接入用户激活时建立单隧道功能流程如[图4]所示。该功能是指IU接入的用户在激活时，先将SGSN为DT情况下特殊分配的TEIDU带给GGSN，并在RAB指派完成后进行更新，将RNC的对应承载的用户面信息带给GGSN，并指示GGSN是DT。
图4  IU接入用户激活时建立单隧道功能流程图
IU接入用户二次激活时建立单隧道功能
IU接入用户二次激活时建立单隧道功能的流程如[图5]所示。该功能是指IU接入的用户二次激活时，先将SGSN为DT情况下特殊分配的TEIDU带给GGSN，并在RAB指派完成后进行更新，将RNC的对应承载的用户面信息带给GGSN，并指示GGSN是DT。
图5  IU接入用户二次激活时建立单隧道功能流程图
业务请求过程建立单隧道功能
业务请求过程建立单隧道功能的流程如[图6]所示。该功能是IU接入的用户发起DATA类型的Service Request时，建立DT。
图6  业务请求过程建立单隧道功能流程图
SGSN局内重定位过程建立单隧道功能
SGSN局内重定位过程建立单隧道功能的流程如[图7]所示。该功能是SRNC发起局内Serving RNS Relocation、Combined
Hard Handover and SRNS Relocation Procedure、Combined Cell / URA Update
and SRNS Relocation Procedure过程时，建立DT。
图7  SGSN局内重定位过程建立单隧道功能流程图
SGSN局间重定位过程新局建立单隧道功能
SGSN局间重定位过程新局建立单隧道功能的流程如[图8]所示。该功能是SRNC发起局间Serving RNS Relocation、Combined
Hard Handover and SRNS Relocation Procedure、Combined Cell / URA Update
and SRNS Relocation Procedure过程时，新SGSN建立DT，在13步中将RNC的用户面通知到GGSN。
图8  SGSN局间重定位过程新局建立单隧道功能流程图
RAB释放流程拆除单隧道功能
RAB释放流程拆除单隧道功能的流程如[图9]所示。该功能是RNC或SGSN发起RAB释放过程时，拆除DT，重新恢复SGSN与GGSN之间的用户面隧道。
图9  RAB释放流程拆除单隧道功能流程图
Iu释放流程拆除单隧道功能
Iu释放流程拆除单隧道功能的流程如[图10]所示。该功能是RNC或发起Iu释放过程时，拆除DT，重新恢复SGSN与GGSN之间的用户面隧道。
图10  Iu释放流程拆除单隧道功能流程图
SGSN实现局内重定位流程拆除单隧道功能
该功能是SRNC发起Serving RNS
Relocation、Combined Hard Handover and SRNS Relocation Procedure、Combined
Cell / URA Update and SRNS Relocation Procedure，SGSN决定拆除单隧道，建立双隧道。 
SGSN实现监测受控时拆除单隧道功能
该功能是监测服务器对用户布控时，触发SGSN拆除DT，重新建立SGSN与GGSN之间、SGSN与RNC之间的用户面隧道。 
SGSN实现DT情况下RAB释放流程删除PDP上下文功能
该功能是RNC接收到GGSN用户面发送过来的error
indication时，向SGSN发送RAB释放请求，携带原因值为GTP Resources Unavailable（263）。SGSN发现该PDP上下文处于DT状态，于是删除该PDP上下文。 
SGSN实现DT情况下GGSN收到RNC的ERROR INDICATION
SGSN实现DT情况下GGSN收到RNC的ERROR
INDICATION的功能流程如[图11]所示。该功能是SGSN接收到GGSN发起的PDP上下文更新过程，携带Direct Tunnel
Flags字段,并且EI标志位置1（即指示收到RNC的Error Indication），此时SGSN正处于DT状态，SGSN立即释放RAB并建立SGSN和GGSN之间的用户面隧道。
图11  SGSN实现DT情况下GGSN收到RNC的ERROR INDICATION的功能流程图
有开关控制Camel用户是否可以建立DT，此时其实是签约了Camel但是并不会与SCP交互的流程，所以也不需要控制DT。 
系统影响 : 
DT功能降低了SGSN用户面资源使用。 
DT功能增加了控制面的负荷，在Iu释放和RAB释放时增加了SGSN和GGSN之间信令交互，GGSN上的影响也需要考虑。 
DT功能对计费话单有影响：SGSN/GGSN会因为DT与非DT的切换而输出话单，增加话单的量，系统有开关控制是否输出DT话单；SGSN不能够根据时长和流量策略输出话单，可能会导致长话单（时长较长）的出现；DT情况下输出的话单中没有流量信息参数。 
遵循标准 : 
3GPP TS 23.060: "General Packet Radio Service (GPRS); Service
description; Stage 1". 
3GPP TS 29.060: "GPRS Tunnelling Protocol (GTP) across the
Gn and Gp interface". 
特性能力 : 
可以根据开关控制不输出DT话单或0流量的DT话单。 
可以控制非DT到DT切换的间隔次数，最大为255（表示从DT切换到非DT后不再能够重新DT），最小为0（表示不限制DT切换）。 
可获得性 : 
版本要求及变更记录
ZXUN uMAC具备V4.12.11版本及后续版本。 
对其他网元的要求
需要RNC支持Iu over IP功能。 
需要GGSN支持DT功能。 
GGSN开启DT功能对Radius功能有影响。SGSN发起的DT建链和拆链的更新请求会导致GGSN向Radius发送中间计费请求。大量的中间计费请求可能导致AAA服务器性能出现瓶颈。 
GGSN开启DT功能对OCS有影响，当OCS服务器下发了SGSN变化的trigger时，GGSN将向OCS发送CCRU消息，这将导致OCS服务器出现性能瓶颈。目前GGSN还没有开关关闭这种情况不发送CCRU。可通过OCS服务器不下发SGSN变化更新OCS的trigger来达到关闭这种CCRU的目的。 
O&M相关 : 
命令
配置项命令配置项参见表1。表1  命令配置项配置项命令RNC局向附加属性配置ADD RNCGPRS APN HOST配置ADD GPRS APNEPC APN HOST配置ADD EPC APNDNS解析类APN配置ADD DNSAPNCHGGPRS扩展APN配置ADD EXAPN支持DT的GGSN IP配置ADD DT IP签约APN DT前缀配置SET APN DT PREFIX 
软件参数新增软件参数参见表2。表2  新增软件参数软件参数ID软件参数名称786523DT话单控制786527DT切换频次786546CAMEL用户是否允许隧道直传 
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
SGSN DT测量|编号为C40559开头的所有计数器。
SGSN APN DT测量|编号为C40561开头的所有计数器。
SGSN RNC DT测量|编号为C40560开头的所有计数器。
性能指标参见[表4]。
测量类型名称|性能指标名称
---|---
SGSN DT测量KPI|SGSN携带DTI更新会话成功率（%）
SGSN APN DT测量KPI|每APN SGSN携带DTI更新会话成功率（%）
SGSN RNC DT测量KPI|每RNC SGSN携带DTI更新会话成功率（%）
话单与计费
DT建立时，出部分话单。类型为dT-Establishment , 需要携带dataVolumeGPRSUplink、dataVolumeGPRSDownlink字段。（收集DT建立之前的流量） 
DT释放时，出部分话单。类型为dT-Removal ， 此时不携带dataVolumeGPRSUplink、dataVolumeGPRSUplink字段。 
PDP正常去活时，若此时PDP处于DT状态，出正常关闭话单。 此时不携带Data Volume Uplink、Data
Volume Downlink字段。 
PDP异常去活时，若此时PDP处于DT状态，出异常关闭话单。 此时不携带Data Volume Uplink、Data
Volume Downlink字段。 
 说明： 
在DT情况下，由于用户面不存在，其他话单都不出。 
特性配置 : 
摘要Gn/Gp SGSN DT功能配置特性测试用例常见问题处理 
#### Gn/Gp SGSN DT功能配置特性 
配置前提
完成基本的网元数据配置。 
启用DT功能时，需要使RNC用户面网络与GGSN用户面网络互通。 
配置过程
打开支持DT的License控制。 
使用[ADD RNC]命令新增RNC配置，设置支持DT功能。
根据不同情况，选择执行如下操作。 
如果...|那么...
---|---
未启用APN扩展|使用ADD GPRS APN和ADD EPC APN命令设置解析配置。
使用DNS解析|使用ADD DNSAPNCHG命令进行DNS解析类APN配置。
（可选）如果启用了APN扩展，则使用[ADD EXAPN]命令进行APN扩展配置中的DT策略配置。
根据不同情况，选择执行如下操作。 
如果...|那么...
---|---
ADD EXAPN命令中设置的DT策略为“根据支持DT的GGSN IP配置决策”|使用ADD DT IP命令配置支持DT的GGSN IP。
ADD EXAPN命令中设置的DT策略不为“根据支持DT的GGSN IP配置决策”|无需操作，转至下一步
根据不同情况，选择执行如下操作。 
如果...|那么...
---|---
ADD GPRS APN和ADD EPC APN命令中的“支持DT功能”设置为“根据签约APN信息决策是否支持DT”|使用SET APN DT PREFIX命令进行签约APN DT前缀配置。
ADD GPRS APN和ADD EPC APN命令中的“支持DT功能”未设置为“根据签约APN信息决策是否支持DT”|无需操作，结束。
配置实例
APN本地解析，无APN扩展，DT策略直接设置为打开
 说明： 
DT功能的License开启不再说明。仅说明与DT参数相关的命令。 
SGSN配置关联的RNC(s)支持DT功能 
脚本命令|解释说明
---|---
ADD RNC:RNCOFFID=222,MCC="460",MNC="03",RNC=222,RAT="UTRAN",DTSPRT="YES",NAME="RNC222(DT)"|DTSPRT参数设置为YES，说明为此RNC支持DT。
如果APN格式为GPRS格式，进行GPRS APN解析配置 
脚本命令|解释说明
---|---
ADD GPRS APN:APN="\"zte.com.mnc003.mcc460.gprs",IPADDR="1.2.3.4",CTPLID=0,DTSPRT="YES"|DTSPRT参数设置为YES，表示此APN解析到的GGSN支持DT功能。
如果APN格式为EPC格式，进行EPC APN解析配置 
脚本命令|解释说明
---|---
ADD EPC APN:APN="zte.com.apn.epc.mnc003.mcc460.3gppnetwork.org",HOST="pgw",IPADDR="1.1.1.1",SERVICE="x-3gpp-pgw"&"x-3gpp-ggsn",PROTOCOL="x-gn"&"x-gp",DTSPRT="YES"|DTSPRT参数设置为YES”表示此APN解析到的GGSN支持DT功能。
APN为DNS解析，无APN扩展，DT策略根据APN签约信息决策
SGSN配置关联的RNC(s)支持DT功能 
脚本命令|解释说明
---|---
ADD RNC:RNCOFFID=222,MCC="460",MNC="03",RNC=222,RAT="UTRAN",DTSPRT="YES",NAME="RNC222(DT)"|DTSPRT：设置为YES，说明为此RNC支持DT。
DNS解析类APN配置 
脚本命令|解释说明
---|---
ADD DNSAPNCHG:APN="zte.com.mnc001.mcc460.gprs",DTSPRT="Subscription"|将DTSPRT参数设置为“根据签约APN信息决策是否支持DT”，说明此APN是否支持DT将根据用户的签约APN信息来决定。
配置签约APN DT前缀 
脚本命令|解释说明
---|---
SET APN DT PREFIX:CHECKCTX="YES",APNPERFIX="3gdt"|CHECKCTX：是否检查签约上下文，可以选YES和NO。如果不检查，SGSN接收到用户的签约数据时，则对签约PDP上下文保持原有的处理，且每个签约PDP上下文都是不支持DT的。如果检查，SGSN接收到用户的签约数据时，则对签约PDP上下文进行处理，根据是否包含DT前缀来确认是否支持DT。APNPERFIX：支持DT的APN前缀字符串，此参数由运营商决定。再对用户进行区别是否支持DT，支持DT的用户需要在HLR上签约一个包含此前缀的APN。
APN扩展，是否支持DT根据支持DT的GGSN IP配置决策
SGSN配置关联的RNC(s)支持DT功能 
脚本命令|解释说明
---|---
ADD RNC:RNCOFFID=222,MCC="460",MNC="03",RNC=222,RAT="UTRAN",DTSPRT="YES",NAME="RNC222(DT)"|DTSPRT：设置为YES，说明为此RNC支持DT。
配置扩展APN 
脚本命令|解释说明
---|---
ADD EXAPN:IMSI="460038800000001",EXUETYPE="For All",EXMODE="IMSI",EXBITS="3"-"9",APNCTRL="YES",DTCTRL="GGSNIP"|将DT策略选择为根据支持DT的GGSN IP配置决策。
配置支持DT的GGSN IP 
脚本命令|解释说明
---|---
ADD DT IP:IPADDR="131.1.30.159"|如果设置为“根据支持DT的GGSN IP配置决策”，用户IMSI为460038800000001通过扩展APN：hello.0038800.mnc003.mcc460.gprs解析的GGSN地址是131.1.30.159，则需要配置支持DT的GGSNIP配置中增加支持DT的GGSN IP地址，只有使用了扩展APN，才需要配置GGSN IP地址。 配置该地址后，则该扩展APN关联的GGSN支持DT。不配置该地址，则该扩展APN关联的GGSN不支持DT。
测试用例 : 
IU接入用户激活时建立单隧道功能
测试项目|IU接入用户激活时建立单隧道功能。
测试目的|SGSN实现IU接入用户激活时建立单隧道功能。
预置条件|Iu 方式接入。SGSN工作正常。SGSN支持DT功能。用户激活关联的RNC、GGSN支持DT功能。用户非CAMEL用户。用户不处于用户面监测受控状态。用户不处于漫游状态。
测试过程|模拟触发激活流程。测试PS上下行业务。
通过准则|SGSN 发送正确的create pdp context req 消息，该消息的所带用户面参数中地址是SGSN 用户面地址。GGSN 创建PDP上下文，返回正确的create pdp context rsp消息，其中带上GGSN分配的用户面地址和TEIDU。SGSN 向RNC发起RAB 指派过程，带的地址和隧道标识是GGSN 分配的用户面地址和GGSN TEIDU。RAB指派过程完成后，SGSN向GGSN 触发update 流程，需要至少检查TEIDU和DTI参数。TEIDU 是RNC 分配的用户面TEIDU。DTI IE必须带上，其中的DTI 标志正确。GGSN收到Update 请求后，更新控制面和用户面PDP上下文，回应正确的RSP消息。UPDATE流程完成之后，SGSN 向手机发送成功的Active pdp context accept消息，其他检查。GGSN 控制面和用户面PDP 上下文中的QOS 参数和更新前一致。GGSN PDP上下文中用户面GTP对端地址和TEIDU是RNC所分配而不是SGSN所分配。测试PS业务，单隧道业务通顺，大小报文无异常。以上流程中的信令跟踪解码要求正确。
测试结果|
DATA类型业务请求过程建立单隧道功能
测试项目|DATA类型业务请求过程建立单隧道功能。
测试目的|SGSN实现DATA类型业务请求过程建立单隧道功能。
预置条件|Iu 方式接入，没有DT链路。SGSN工作正常。SGSN支持DT功能。用户激活关联的RNC、GGSN支持DT功能。用户非CAMEL用户。用户不处于用户面监测受控状态。用户不处于漫游状态。
测试过程|模拟触发激活流程。测试PS上下行业务。
通过准则|用户发起DATA类型的Service Request。SGSN触发正确的RAB指派消息，该消息的所带用户面参数中，TEIDU 是 GGSN所分配的TEIDU，地址是GGSN用户面地址。RAB 指派过程完成后，SGSN 向GGSN 触发update 流程，需要至少检查TEIDU和DTI参数。TEIDU是RNC分配的用户面TEIDU。DTI IE必须带上，其中的DTI 标志正确。GGSN 收到Update 请求后，更新控制面和用户面PDP上下文，回应正确的RSP消息。UPDATE 流程完成之后，,其他检查：GGSN 控制面和用户面PDP 上下文中的QOS 参数和更新前一致。GGSN PDP上下文中用户面GTP对端地址和TEIDU是RNC所分配而不是SGSN所分配。SGSN用户面上下文在SGSN 收到该update  pdp context rsp 的成功消息后删除。 做PS 业务，创建的单隧道业务通顺，大小报文无异常，GGSN 数据跟踪显示正常。以上流程中的信令跟踪解码要求正确。
测试结果|
GGSN因DT情况下收到RNC的ERROR INDICATION而发起的更新过程
测试项目|GGSN因DT情况下收到RNC的ERROR INDICATION而发起的更新过程。
测试目的|SGSN实现GGSN因DT情况下收到RNC的ERROR INDICATION而发起的更新过程。
预置条件|Iu接入，已经建立了TD。RNC 用户面问题，向GGSN 触发Error Indication，造成GGSN向SGSN触发modify。
测试过程|Iu接入，已经建立了TD。RNC 用户面问题，向GGSN 触发Error Indication，造成GGSN向SGSN触发modify。
通过准则|SGSN收到GGSN发起PDP上下文修改消息Update PDP Context Request，且消息中携带DirectTunnel Flags字段,并且EI标志位置1。SGSN向GGSN发送Update PDP Context Response响应，响应消息中携带SGSN的用户面地址、TEID、Qos等信息。同时携带置0的DTI标记以告诉GGSN现在取消了DT。GGSN保存SGSN用户面地址、TEID。并在PDP上下文中取消DTI标记。表示取消了DT。并将上下文标记为有效，表示GGSN可以继续转发下行数据包。
测试结果|
局内重定位流程拆除单隧道功能
测试项目|局内重定位流程拆除单隧道功能。
测试目的|SGSN实现局内重定位流程拆除单隧道功能。
预置条件|Iu 方式接入，已经建立DT链接。SRNC 触发relocation 过程。
测试过程|Iu 方式接入，已经建立DT链接。SRNC 触发relocation 过程。
通过准则|SGSN向TRNC发送Relocation Request请求，向TRNC提供Qos、SGSN的用户面地址、TEID等信息。TRNC保存SGSN用户面地址、TEID。并建立RB承载。TRNC向SGSN返回Relocation RequestAck响应，消息中携带TRNC用户面地址、TEID。SGSN收到Relocation Request Ack响应，保存RNC用户面地址、TEID等RAB信息。向SRNC发送Relocation Command，继续重定位过程，直到收到 Relocation Complete消息。向GGSN发送Update PDP Context Request请求，请求消息中携带SGSN的用户面地址、TEID。同时携带DTI标记为0以告诉GGSN取消DT。将SGSN的用户面地址、TEID等信息更新到用户面，并在控制面、用户面PDP上下文中将DTI标记置0。此后GGSN向SGSN返回UpdatePDP Context Response消息。
测试结果|—
Iu释放流程拆除单隧道功能
测试项目|Iu释放流程拆除单隧道功能。
测试目的|SGSN实现Iu释放流程拆除单隧道功能。
预置条件|Iu 方式接入，已经建立DT链接。SGSN在老的Iu链接上，接收到RNC 的Iu 释放请求。
测试过程|Iu 方式接入，已经建立DT链接。SGSN在老的Iu链接上，接收到RNC 的Iu 释放请求。
通过准则|RNC向SGSN发起Iu Release Request消息。向RNC发起Iu释放COMMAND，收到RNC的Iu Release cmpletes时。向GGSN发送Update PDP Context Request消息，携带SGSN的用户面地址、TEID等参数，同时携带DTI标记置0以通知GGSN现在取消了DT。GGSN更新PDP上下文后，向SGSN回应Update PDP Context Response消息。确保SGSN和GGSN上下文和其他参数正确。
测试结果|
常见问题处理 : 
用户激活完成，通过检查发现只是普通激活，没有建立DT的双链路。SGSN在决策时判断用户是否满足以上条件，若满足以下任意一个条件，则判定对该用户不能使用DT；否则，判定该用户使用DT。漫游的情况下。SGSN的MM上下文中存储的签约信息中包含camel签约信息，即CAMEL用户。监测用户受控时。RNC或GGSN不支持单隧道时。非IU接入情况下。SGSN不支持DT。（包括SGSN不支持GTPV1时） 
已经DT用户激活建立了单隧道，但是业务不通。检查SGSN的环境是否为Iu over IP。在GGSN、PDN上的路由是否正确。 
## ZUF-77-02-008 LBO控制 
特性描述 : 
摘要术语描述应用场景客户收益系统影响遵循标准可获得性O&M相关 
术语 : 
术语|含义
---|---
MME池区|MME池区是指UE在其间移动不需要改变服务MME的区域。一个MME池区内有一个或多个对等的MME。MME池区是由多个TA汇聚。MME池区间可以有交迭。
SGW池区|SGW池区是指UE在其间移动不需要改变服务SGW的区域。一个SGW池区内有一个或多个对等的SGW。SGW池区是由多个TA汇聚。SGW池区间可以有交迭。
默认APN|默认APN是在签约数据中被标识为默认的APN，用于在附着过程中建立默认的PDN连接。
默认承载|默认承载是与分别在UE和PGW中用来匹配所有数据包的上、下行包过滤器相关的承载。
专用承载|专用承载是与分别在UE和PGW中用来匹配某些数据包的上、下行包过滤器相关的承载。
AMBR|AMBR是用来限制每个UE所有非GBR承载的汇聚最大bit rate的QOS项。
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载。
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载。
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载。
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程。
PDN连接|为UE与PDN之间存在的连接。
描述 : 
用户在运营商网络内部漫游或者运营商网络间漫游，使用LBO（Local Breakout，本地疏导）功能可以进行路由优化。因为用户平面不需要离开用户当前所在的区域，从而避免了路由迂回。
应用场景 : 
具体场景包括：要求SGSN支持基于IMSI号段支持LBO的局点。
客户收益 : 
收益者|收益描述
---|---
运营商|实现基于IMSI的LBO功能
系统影响 : 
本功能对SGSN的性能影响很小。 
遵循标准 : 
3GPP TS 23.060 
3GPP TS 23.401 
可获得性 : 
版本要求及变更记录
SGSN具备ZXUN-uMAC V7.19.12版本及后续版本。 
License要求
无 
对其他网元的要求
无 
O&M相关 : 
命令
相关命令配置项参见[表2]。
配置项|命令
---|---
SGSN IMSI号段LBO限制配置|ADD SGSN IMSI RESTRICT LBO
SET SGSN IMSI RESTRICT LBO|SGSN IMSI号段LBO限制配置
DEL SGSN IMSI RESTRICT LBO|SGSN IMSI号段LBO限制配置
SHOW SGSN IMSI RESTRICT LBO|SGSN IMSI号段LBO限制配置
性能统计
无 
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
摘要基于IMSI号段支持LBO功能配置特性调整特性 
#### 基于IMSI号段支持LBO功能配置特性 
配置前提
完成基本功能附着、激活流程的配置。 
配置过程
使用命令[ADD SGSN IMSI RESTRICT LBO]配置基于IMSI限制LBO。
配置实例
实例场景
SGSN本局PLMN为460-03，需要限制460010011
IMSI号段的漫游用户使用VPLMN的GGSN，即PLMN为460-03的GGSN。 
 说明： 
需确认本局其他PLMN中没有配置460-01，否则将按照归属地用户来处理。 
配置脚本
命令脚本|解释说明
---|---
ADD SGSN IMSI RESTRICT LBO:IMSI="460010011"|IMSI前缀为460010011的用户激活时，将不能按照APN.mnc003.mcc460.gprs的格式查找VPLMN的GGSN地址，而是按照APN.mnc001mcc460.gprs的格式查找HPLMN的GGSN地址。
调整特性 : 
可调整命令如下： 
调整命令|作用|重要参数填写说明
---|---|---
SET SGSN IMSI RESTRICT LBO|修改IMSI号段的别名|必须填写IMSI号段
# 缩略语 
# 缩略语 
## 2G 
The 2nd Generation Mobile Communications第二代移动通信
## 3G 
The 3rd Generation Mobile Communications第三代移动通信
## BS 
Billing System计费系统
## BSS 
Base Station System基站系统
## CAMEL 
Customized Applications for Mobile Network Enhanced Logic移动网络增强逻辑的客户化应用
## CDR 
Call Detail Record呼叫详细记录，即话单
## CGF 
Charging
Gateway Function 计费网关功能
## CN 
Core Network核心网
## CPU 
Central Processing Unit中央处理器
## CS 
Circuit Switched电路交换
## DT 
Direct Tunnel直传隧道
## DTI 
Digital Trunk Interface	数字中继接口板
## EDGE 
Enhanced Data rates for GSM EvolutionGSM用的增强型数据速率
EIR : 
Equipment Identity Register设备标识寄存器
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
## GMM 
GPRS Mobile ManagementGPRS 移动性管理
## GMSC 
Gateway Mobile Switching Center网关移动交换中心
GPRS : 
General Packet Radio Service通用无线分组数据业务
HLR : 
Home Location Register归属位置寄存器
IMSI : 
International Mobile Subscriber Identity国际移动用户标识
IP : 
Internet Protocol因特网协议
## IWMSC 
Interworking Mobile Switching Center网间移动交换中心
## LBO 
Local Breakout本地路由疏导
## MS 
Mobile Station移动台
MSC : 
Mobile Switching Center移动交换中心
## MT 
Mobile Terminal移动终端
NAS : 
Non-Access Stratum非接入层
## NSAPI 
Network-layer
Service Access Point Identifier网络层业务接入点标识
## OCS 
Online Charging System在线计费系统
## OMP 
Operation & maintenance Main Processor操作维护主处理板
PDN : 
Packet Data Network分组数据网
PDP : 
Packet Data Protocol分组数据协议
## PFI 
 Payload FCS Indicator净负荷FCS标识
PLMN : 
Public Land Mobile Network公共陆地移动网
## PS 
Packet Switched分组交换
QoS : 
Quality of Service服务质量
## RAB 
Radio Access Bearer无线接入承载
RAN : 
Radio Access Network无线接入网
RNC : 
Radio Network Controller无线网络控制器
## RRC 
Radio Resource Control无线资源控制
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
SMS : 
Short Message Service短消息业务
## TE 
Terminal Equipment终端设备
## TEID 
Tunnel Endpoint Identifier隧道端点标识
## TFT 
Traffic Flow Template话务流量模型
## TI 
Transparent Interface透明接口
UE : 
User Equipment用户设备
UTRAN : 
UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
## VLR 
Visitor Location Register拜访位置寄存器
# ZUF-77-03 切换 
概述 : 
功能描述 : 
在UE移动过程中，基站根据UE上报的测量报告，确定是否需要切换UE到目标小区或者目标基站。如果需要切换，当切换完成后，UE的信令面和用户面，将切换到目标基站，原有基站的用户信息将被释放，UE可在新的无线接入网中继续使用数据业务和其他业务。源基站可以是E-UTRAN，也可以是UTRAN；目的基站可以是E-UTRAN，也可以是UTRAN。 
根据目标基站和源基站接入方式的不同，切换可以区分如下场景： 
3G内切换，源基站和目标基站均为UTRAN。 
3G切换到LTE，源基站为UTRAN，目标基站为E-UTRAN。 
LTE切换到3G，源基站为E-UTRAN，目标基站为UTRAN。 
功能特性简介 : 
SGSN提供了不同的解决方案，解决不同的切换需求。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
3G内切换|切换发生在两个RNC之间。SGSN判断目标RNC是否归属本局管理，若不是则根据目标RNC信息，查询目标SGSN地址，并通知目标SGSN用户切入。切换流程完成之后，如果切换前后，用户所在RAI发生了改变，UE发起RAU流程。若切换前后SGSN变化，则在RAU流程中SGSN通知HLR用户注册的SGSN发生了改变。|ZUF-77-03-001 3G内切换
LTE到3G切换|SGSN网元跨RAT切换流程是用户从一种接入技术变成另一种接入技术时保证用户业务连续性的过程，目前仅涉及LTE与3G之间的切换。在跨RAT切换过程中，用户的无线连接无缝切换到目的无线接入网络。RAT切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。本特性涉及到从LTE接入，切换到3G接入。源MME根据目标RNC标识，查询目标SGSN地址，并通知目标SGSN用户切入。源MME负责将EPS安全上下文转化为UMTS安全上下文。目标SGSN可以在切换后的路由区更新流程中，根据本地配置决策是否重新鉴权，并重新生成UMTS安全上下文。|ZUF-77-03-002 LTE到3G切换
3G到LTE切换|SGSN网元跨RAT切换流程是用户从一种接入技术变成另一种接入技术时保证用户业务连续性的过程，目前仅涉及LTE与3G之间的切换。在跨RAT切换过程中，用户的无线连接无缝切换到目的无线接入网络。RAT切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。本特性涉及到从3G接入，切换到LTE接入。SGSN根据目标TAI，查询目标MME地址，并通知目标MME用户切入。目标SGSN不做安全上下文映射，直接将UMTS安全上下文传递给目标MME，由目标MME完成UMTS安全上下文到EPS安全上下文的映射。目标MME在切换后的跟踪区更新流程中，根据本地配置的策略，重新鉴权并生成本地EPS安全上下文。|ZUF-77-03-003 3G到LTE切换
## ZUF-77-03-001 3G内切换 
特性描述 : 
摘要描述应用场景客户收益实现原理系统影响应用限制特性交互遵循标准特性能力可获得性O&M相关 
描述 : 
定义
GnGp SGSN网元切换流程是3G用户注册到PS域后，在位置移动过程中携带业务的基本流程，保证用户在位置移动过程中数据传输不中断。
切换流程完成之后，如果SGSN发生了改变，UE发起RAU流程，在RAU流程中SGSN通知HLR用户注册的SGSN发生了改变。
背景知识
GPRS网络架构图,如图[图1]所示，其中包含了如下网元：
图1  GPRS架构图
TE/MT（Terminal Equipment/Mobile Terminal，终端设备/移动终端）：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS（Base Station System，基站系统）：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。
UTRAN（UMTS Terrestrial Radio Access Network，统一的陆地无线接入网络）：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
HLR(Home Location Register，归属位置寄存器):永久存储用户签约数据。 
PDN(Packet
Data Network，分组数据网)：为用户提供业务的网络。 
CGF(Charging Gateway Functionality，计费网关功能)：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS（Billing System，计费系统）：负责接收和处理从核心网发送过来的CDR文件。 
EIR（equipment
identity register 设备标识寄存器）：负责检查UE设备。 
PS CN（Packet Switched Core
Network，分组交换核心网）：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元： 
SGSN(Serving
GPRS Support Node，服务GPRS支持节点)：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS
Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息； 
GGSN(Gateway GPRS Support Node，GPRS支持节点网关)：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务： 
MSC/VLR（Mobile Switch
Center/ Visitor Location Register，移动交互中心/拜访位置寄存器）：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMS GMSC/SMS IWMSC (Short Message Service Gateway MSC/ Short Message
Service Interworking MSC，短消息网管移动交换中心/短消息互通移动交换中心)：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL (Customised Applications for Mobile network Enhanced Logic，移动网络定制应用增强逻辑服务器)：该功能实体主要对用户进行在线计费。 
应用场景 : 
SGSN网元切换流程是基本流程，在用户移动过程中通过切换流程完成携带数据业务的用户在两个RNC的移动。具体常见场景包括：
用户处于PMM-CONNECTED状态，用户在两个RNC之间移动。如下图所示：
在切换之前UE注册在old SGSN。源RNC充当服务RNC (SRNC)。
切换之后，UE注册在new SGSN。
UE在new SGSN处于PMM CONNECTED状态，目的RNC充当服务RNC。
客户收益 : 
受益方|受益描述
---|---
运营商|支持本地用户和合法漫游用户注册到运营商的PS网络上后，激活PDP上下文使运营商可以为用户提供各种数据业务和其他业务，在切换过程中用户的数据业务不中断，提高用户体验度
移动终端用户|终端用户不可见。
实现原理 : 
系统架构
无 
涉及的网元
SGSN网元切换流程需要UE、BSS/RNC、SGSN、HLR、GGSN的共同配合： 
网元|描述
---|---
UE（User Equipment，用户设备）|为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，比如UE/用户标识，移动性管理状态，用户安全参数等。在切换过程中具体功能包括RANMobility Information消息确认，RNC和UE进行RRC信令交换，完成无线信息交换，UE分配完成了RNTI并且UE发现RAI发生了改变，UE发起RAU流程。
RNC（Radio Network Controller，无线网络控制器）|为终端的Iu（无线接入网络和核心网的一种接口）接入提供无线资源。在切换过程中具体功能包括切换流程的发起和消息处理、对无线承载资源的建立和删除，前转下行数据包到新的SGSN。
SGSN(Serving GPRS Support Node，服务GPRS支持节点)|支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS MobilityManagement）上下文和分组数据协议（PDP，Packet Data Protocol）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。在切换过程中负责切换流程的信令处理，建立或者删除和RNC的无线承载，通知GGSN更新PDP上下文信息。
GGSN(Gateway GPRS Support Node，GPRS支持节点网关)|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。在切换过程中具体功能包括负责用户的PDP上下文更新，完成承载管理功能。
协议栈
无 
本网元实现
无 
业务流程
SRNS Relocation Procedure
图2  SRNS Relocation Procedure
源SRNC决定发起SRNS relocation.
source SRNC发送Relocation Required (Relocation Type, Cause, Source ID, Target
ID, Source RNC to target RNC transparent container) 消息到old SGSN。
old SGSN根据Target ID判断是局内还是局间SRNS relocation。如果是局间SRNS relocation，the
old SGSN根据Target ID找到 new SGSN的地址发送Forward Relocation
Request message (IMSI, Tunnel Endpoint Identifier Signalling, MM Context, PDP Context, Target
Identification, RAN transparent container, RANAP Cause, GCSI)消息到new SGSN。
new SGSN发送Relocation Request message (Permanent NASUE Identity, Cause, CN Domain Indicator,
Source-RNC to target RNC transparent container, RABs to be setup,
Service Handover related information) 消息到target RNC。New SGSN和target RNC执行RAB建立流程，对于在source RNC不存在的PDP上下文不建立RAB，如果new SGSN决定建立DT，那么RAB建立的时候携带GGSN的用户面地址和TEID。
在所有的RAB建立和资源分配完成后，target RNC发送Relocation Request
Acknowledge (RABs setup, RABs failed to setup)消息到new SGSN。
当target RNC和new SGSN资源分配完成后，new SGSN返回Forward Relocation Response message (Cause, RANAP Cause, and RAB Setup Information)消息到old SGSN。该消息指出target RNC已经准备好接收source SRNC收到的下行数据，资源分配已经完成。
old SGSN发送Relocation Command (RABs to be released, and RABs subject to data
forwarding)到source SRNC。
source SRNC根据QoS开始前转数据到target SRNC。 
source RNC设置data-forwarding定时器。当source SRNC准备好之后，source SRNC发送Relocation
Commit(SRNS Contexts)消息到target RNC，通知target RNC，source RNC开始执行切换。
当切换执行开始的时候target RNC发送Relocation Detect消息到new SGSN。Target RNC充当了SRNC的角色。
target SRNC 发送RAN Mobility Information给UE。
target SRNC收到了UE发送的RAN Mobility Information Confirm 消息，target RNC发送将发起Relocation Complete流程，发送Relocation
Complete消息到new SGSN，通知SGSN切换完成。
new SGSN发送Forward Relocation Complete消息给old SGSN，通知old SGSN切换完成。
new SGSN 发送Update PDP Context Request (new SGSN Address, SGSN Tunnel Endpoint
Identifier, QoS Negotiated, serving network identity, CGI/SAI, RAT type, CGI/SAI/RAI
change support indication, NRSN, DTI)消息到PDP对应的GGSN。如果建立DT，SGSN携带RNC的用户面地址和TEID。
GGSNs更新PDP上下文后返回Update PDP Context
Response (GGSN Tunnel Endpoint Identifier, Prohibit Payload Compression, APN Restriction, CGI/SAI/RAI change report required, BCM)消息到new SGSN。
收到Forward Relocation Complete消息之后，old SGSN发送Iu Release Command消息到source RNC，当source RNC中的data-forwarding定时器超时后source RNC返回Iu Release Complete消息给old SGSN。
UE分配完成了RNTI并且UE发现RAI发生了改变，UE发起Routeing Area Update流程。
Combined Hard Handover and SRNS Relocation Procedure
图3  Combined Hard Handover and SRNS Relocation Procedure
源SRNC决定发起SRNS relocation.
source SRNC发送Relocation Required (Relocation Type, Cause, Source ID, Target
ID, Source RNC to target RNC transparent container) 消息到old SGSN。
old SGSN根据Target ID判断是局内还是局间SRNS relocation。如果是局间SRNS relocation，the
old SGSN根据Target ID找到 new SGSN的地址发送Forward Relocation
Request message (IMSI, Tunnel Endpoint Identifier Signalling, MM Context, PDP Context, Target
Identification, RAN transparent container, RANAP Cause, GCSI)消息到new SGSN。
new SGSN发送Relocation Request message (Permanent NASUE Identity, Cause, CN Domain Indicator,
Source-RNC to target RNC transparent container, RABs to be setup,
Service Handover related information) 消息到target RNC。New SGSN和target RNC执行RAB建立流程，对于在source RNC不存在的PDP上下文不建立RAB，如果new SGSN决定建立DT，那么RAB建立的时候携带GGSN的用户面地址和TEID。
在所有的RAB建立和资源分配完成后，target RNC发送Relocation Request
Acknowledge (RABs setup, RABs failed to setup)消息到new SGSN。
当target RNC和new SGSN资源分配完成后，new SGSN返回Forward Relocation Response message (Cause, RANAP Cause, and RAB Setup Information)消息到old SGSN。该消息指出target RNC已经准备好接收source SRNC收到的下行数据，资源分配已经完成。
old SGSN发送Relocation Command (RABs to be released, and
RABs subject to data forwarding)到source SRNC。
source RNC设置data-forwarding定时器，source SRNC根据QoS开始前转数据到target SRNC。
RNC和UE进行RRC信令交换，完成无线信息交换；
源RNC通过Old SGSN、New SGSN发送SRNC Context信息到Target RNC；
当切换执行开始的时候target RNC发送Relocation Detect消息到new SGSN。Target RNC充当了SRNC的角色。
target SRNC收到了UE发送的RRC消息，target RNC发送将发起Relocation Complete流程，发送Relocation Complete消息到new SGSN，通知SGSN切换完成。
new SGSN发送Forward Relocation Complete消息给old SGSN，通知old SGSN切换完成。
new SGSN 发送Update PDP Context Request (new SGSN Address, SGSN Tunnel Endpoint
Identifier, QoS Negotiated, serving network identity, CGI/SAI, RAT type, CGI/SAI/RAI change support indication,
NRSN, DTI)消息到PDP对应的GGSN。如果建立DT，SGSN携带RNC的用户面地址和TEID。
GGSNs更新PDP上下文后返回Update PDP Context Response (GGSN Tunnel Endpoint Identifier,
Prohibit Payload Compression, APN Restriction, CGI/SAI/RAI change report required, BCM)消息到new SGSN。
收到Forward Relocation Complete消息之后，old SGSN发送Iu Release Command消息到source RNC，当source RNC中的data-forwarding定时器超时后source RNC返回Iu Release Complete消息给old SGSN。
UE分配完成了RNTI并且UE发现RAI发生了改变，UE发起Routeing Area Update流程。
系统影响 : 
随着同一时间里发生切换的用户数的增加，系统资源占用会一直增大。 
切换越频繁，系统CPU使用率越高。
应用限制 : 
无 
特性交互 : 
由于切换流程是3G业务基本流程，是用户进行数据业务时移动的重要流程，在用户移动过程中通过切换流程，保证数据业务的连续性。 
业务|交互
---|---
切换和PDP更新|在切换的过程中如果SGSN改变，那么SGSN应该向GGSN发起PDP更新过程。
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060 "General Packet Radio Service
(GPRS); Service description; Stage 2". 
3GPP TS 24.008: "Mobile
Radio Interface Layer 3 specification; Core Network Protocols; Stage
3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service (GPRS); Base Station
System (BSS) - Serving GPRS Support Node (SGSN); BSS GPRS Protocol
(BSSGP)". 
3GPP TS 29.060: "General Packet Radio Service (GPRS);
GPRS Tunnelling Protocol (GTP) across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part (MAP) specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3; General
aspects". 
特性能力 : 
用户切换流程完成后，如果是跨SGSN的切换，New SGSN创建了一个MM上下文和PDP上下文。
SGSN支持1200万用户接入，支持1200万MM上下文，2400万PDP上下文。本文档中提供的指标值，是在一定条件下得出的，实际商用配置要依据实际话务模型和其他特定需求，协商确定。
可获得性 : 
版本要求及变更记录
无 
License要求
无 
对其他网元的要求
无 
工程规划要求
无 
O&M相关 : 
命令
配置项无 
安全变量无 
定时器无 
软件参数无 
动态管理无 
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
SGSN重定位测量|编号为C4051100开头的所有计数器
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
摘要配置特性调整特性测试用例常见问题处理 
配置特性 : 
配置说明
无 
配置前提
该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置就可以。 
该配置的数据准备： 
不同局间的交互需要提前协商下数据配置，如不同的RA对应不同的SGSN。通过信息交互以保证MS到SGSN的通信，SGSN之间，SGSN到GGSN之间的通信等。已经新增了本局信令点和本局配置。具体来说：
SGSN里配置的是静态偶联，允许不同的RNC接入；
SGSN里配置的RA包含MS所处的RA；
所有的RA都能正确解析到对应的SGSN；
不同RNC或SGSN之间的通信，在SGSN地址解析里有相应的配置。
配置过程
在老SGSN中使用命令[ADD SGSNHOST]配置新老SGSN之间的连接。
使用命令[SYNA]同步前后台数据。
配置实例
调整特性 : 
可调整命令如下： 
调整命令|作用|重要参数填写说明
---|---|---
ADD SGSNHOST IPADDR:NAME="rac0001.lac1521.mnc003.mcc460.gprs",IPADDR="200.20.1.159"|增加逻辑名称解析的地址|逻辑名称、IP地址
测试用例 : 
测试项目|SRNS重定位过程成功
测试目的|验证SRNS重定位流程基本功能
预置条件|用户附着成功
测试过程|用户发起SRNS Relocation流程
通过准则|重定位流程成功信令跟踪正常
测试结果|重定位流程成功信令跟踪正常
常见问题处理 : 
无 
## ZUF-77-03-002 LTE到3G切换 
特性描述 : 
术语 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
应用限制 
特性交互 
遵循标准 
特性能力 
O&M相关 
术语 : 
术语|含义
---|---
MME池区|MME池区是指UE在其间移动不需要改变服务MME的区域。一个MME池区内有一个或多个对等的MME。MME池区是由多个TA汇聚。MME池区间可以有交迭。
SGW池区|SGW池区是指UE在其间移动不需要改变服务SGW的区域。一个SGW池区内有一个或多个对等的SGW。SGW池区是由多个TA汇聚。SGW池区间可以有交迭。
默认APN|默认APN是在签约数据中被标识为默认的APN，用于在附着过程中建立默认的PDN连接。
AMBR|AMBR是用来限制每个UE所有非GBR承载的汇聚最大bit rate的QoS项。
GBR承载|GBR承载是使用与GBR值相关的、在承载建立或修改时永久分配的专用网络资源的承载。
非GBR承载|非GBR承载是使用与GBR值无关的网络资源的承载。
链接承载标识|链接承载标识指示了与该承载资源相链接的默认承载。
流程处理标识|流程处理标识是UE在发起请求承载资源激活、修改、去活流程时动态分配的标识，用来区别网络侧发起流程和UE发起流程。
PDN连接|在UE和PDN间存在的联系，该联系中一个IPv4或一个IPv6地址，或者两者都有，代表一个UE；一个APN代表该PDN。
描述 : 
定义
MME网元跨RAT切换流程是用户从一种接入技术变成另一种接入技术时保证用户业务连续性的过程，目前仅涉及LTE与3G之间的切换。
在跨RAT切换过程中，用户的无线连接无缝切换到目的无线接入网络。
跨RAT切换流程完成之后，用户可以在新的无线接入网络中继续使用数据业务和其他业务。
背景知识
EPS网络架构图如[图1]所示。
图1  EPS架构图
UE：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成安全功能，完成承载管理功能。
E-UTRAN：可以提供更高的上下行速率，更低的传输延迟和更加可靠的无线传输。E-UTRAN中包含的网元是eNodeB，为终端的接入提供无线资源。
HSS：永久存储用户签约数据。
PDN：为用户提供业务的网络。
EPC：提供了更低的延迟，并允许更多的无线接入系统接入。包含了如下网元：
MME：控制面功能实体，临时存储用户数据的服务器，负责管理和存储UE相关信息，比如UE/用户 标识，移动性管理状态，用户安全参数等，为用户分配临时标识，当UE驻扎在该跟踪区域或者该网络时负责对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。 
Serving GW：用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。 
PDN GW：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个PDN
GW。在物理上，Serving GW和PDN GW可能合一。 
PCRF：该功能实体主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的QoS规则以及计费规则。该功能实体也可以控制接入网中承载的建立和释放。 
另外，EPS网络也能支持原来GERAN和UTRAN网络的接入。 
SGSN：临时存储用户数据的服务器，负责管理和存储UE相关信息，如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，完成用户安全功能，完成用户移动性管理功能和会话管理功能，处理SGSN和UE之间的所有非接入层消息。
UTRAN：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。
GERAN：GPRS/EDGE的无线接入网络，为终端的接入提供无线资源。
应用场景 : 
MME网元跨RAT（LTE与3G之间）切换流程是基本流程，通过跨RAT切换流程保证用户在不同RAT之间移动过程中数据业务和其他业务不中断。具体常见场景包括：
用户在有LTE信号的地方移动到UMTS信号的地方。 
用户在有UMTS信号的地方移动到LTE信号的地方。 
客户收益 : 
受益者|受益描述
---|---
运营商|支持跨RAT（LTE与3G之间）切换流程，可以保证用户在不同RAT之间移动过程中业务的连续性，保证用户的业务体验，可以极大的增强用户对EPS网络使用的满意度。
实现原理 : 
涉及的网元
MME网元跨RAT（LTE与3G之间）切换流程需要UE、eNodeB、MME、HSS、SGW、PGW、SGSN、UTRAN的共同配合。 
UE|为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，比如UE/用户标识、移动性管理状态、用户安全参数等。在切换过程中具体功能包括完成无线测量报告，完成RRC连接和RB连接的切换。
eNodeB|为终端的接入提供无线资源，对用户提供接入层安全功能。在切换过程中具体功能包括切换发起的决策，完成RRC连接和RB连接的切换。
MME|控制面功能实体，负责管理和存储UE相关信息，比如UE/用户标识、移动性管理状态、用户安全参数等。为用户分配临时标识，对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。在切换过程中具体功能包括完成SGSN的选择，完成非直接前转资源的建立，完成承载管理功能。
SGW|用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。在切换过程中具体功能包括管理和存储UE的承载信息，进行非直接前转数据的转发。
PGW|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。在切换过程中具体功能包括负责更新承载功能。
SGSN|临时存储用户数据的服务器，负责管理和存储UE相关信息，如UE/用户标识、移动性管理状态、用户安全参数等。为用户分配临时标识，完成用户安全功能，完成用户移动性管理功能和会话管理功能，处理SGSN和UE之间的所有非接入层消息。在切换过程中具体功能包括管理和存储UE的PDP/承载信息，进行非直接前转数据的转发。
UTRAN|第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。在切换过程中具体功能包括切换发起的决策，完成RRC连接和RB连接的切换。
业务流程
MME到Gn/Gp 3G SGSN的硬切换和SRNC重定位流程
图2  MME到Gn/Gp 3G SGSN的硬切换和SRNC重定位流程
流程说明如下： 
源eNodeB决定发起到UTRAN的切换的流程。
源eNodeB发送切换请求消息给源MME，请求在目标RNC和SGSN中建立资源。需要进行数据转发的承载由目标SGSN决定。
源MME发送前转重定位请求消息给目标SGSN。
目标SGSN发送重定位请求消息给目标RNC。包括Iu用户面在内的RAB必要资源分配完毕后，目标RNC向目标SGSN发送重定位请求确认消息。
目标RNC和目标SGSN间的转发资源分配完毕并且目标SGSN准备好了SRNS重定位，目标SGSN给源MME返回前转重定位响应消息。
如果“非直传前转”被使用了，源MME发送创建非直接数据前转隧道请求消息给SGW。
SGW返回创建非直接数据前转隧道响应消息给源MME。
源MME完成了切换准备，给源eNodeB发送切换命令消息。
源eNodeB对需要数据前转的承载，开始数据前转。 
源eNodeB通过HO from E-UTRAN Command消息向UE发送切换到目标的指令。
目标RNC检测到MS接入。 
当重定位执行触发消息被收到，目标RNC发送重定位检测消息给目标SGSN。
当MS完成了重新配置，MS发送RRC消息给服务的RNC。
当目的服务的RNC收到了从MS的RRC消息，目的服务的RNC发送重定位完成消息给目的SGSN。
目标SGSN收到重定位完成消息，如果是跨SGSN局的重定位，目标SGSN给源MME发送前转重定位完成消息。源MME设置一个定时器用于检测源eNodeB和源SGW的资源释放。
当收到了目的RNC的重定位完成消息，核心网将用户面从源RNC切换到目标SRNC。如果为SGSN间的重定位流程，或者SGSN内SRNS重定位流程，但是RNC和GGSN间建立直传隧道，目标侧SGSN向GGSN发送更新PDP上下文请求消息。GGSN返回更新PDP上下文响应消息。
MS完成重注册流程后，如果新的路由区标识和老路由区标识不同或者UE的TIN设置为“GUTI”，MS发起路由区更新流程。
当第15步设置的定时器超时，源MME通过源MME和目标SGSN采用GTPv1版本进行重定位信令交互，源MME推导出目标SGSN的版本是Gn/Gp SGSN，因此源MME发送删除回话请求消息给SGW，通知SGW删除会话资源，SGW返回删除回话响应消息。
当第15步设置的定时器超时，源MME发送释放资源消息给源eNodeB，通知源eNodeB删除用户资源，源eNodeB收到消息后检测到不再有数据需要前转时，释放用户资源。
Gn/Gp 3G SGSN到MME的硬切换和SRNC重定位流程
图3  Gn/Gp 3G SGSN到MME的硬切换和SRNC重定位流程
流程说明： 
源RNC决策发起到E-UTRAN的切换流程。 
源服务的RNC发送重定位请求消息给源SGSN。 
源SGSN根据Target ID判断是跨局的重定位，给目的MME发送前转重定位请求消息。 
从源SGSN来看，目的MME可以看做是一个目的SGSN，PGW可以看做是GGSN。 
目的MME发现Target ID为RNC ID，把Target RNC ID转换为Target eNodeB ID，转换规则可以根据运营商策略，配置Target
RNC ID和Target eNodeB ID的对应关系，也可以直接把RNC ID放在eNodeB ID的低位。 
MME选择一个目的SGW，按每PDN连接发送创建会话请求消息给SGW。 
目的SGW返回创建会话响应消息给目的MME。
目的MME给目的eNodeB发送切换请求消息，通知目的eNodeB进行切换资源准备。
目的eNodeB分配资源后，给目的MME回切换请求确认消息确认切换资源准备完成。
如果“非直接前转”被使用了并且SGW发生了切换，目的MME给S-GW发送创建非直接数据前转隧道请求消息通知S-GW创建非直接数据前转隧道.
S-GW回创建非直接数据前转隧道响应消息。
目的MME给源SGSN发送前转重定位响应消息。
源SGSN给源服务的RNC发送重定位命令消息。
根据QoS属性，源服务的RNC可能进行数据前转。
当源服务的RNC已经为切换准备好了，源RNC给MS发送RRC消息触发UE的切换。
在到E-UTRAN的切换过程中，不会有SRNC上下文的传输过程。如果源RNC触发了SRNC上下文的传输过程，MME忽略。
当UE成功的接入到了目的eNodeB，目的eNodeB发送切换通知消息给目的MME。
目的MME收到Handover Notify消息后，如果为局间的SRNS重定位，MME发送前转重定位完成消息通知源SGSN切换完成。
目的MME设置一个定时器用于非直接数据前转隧道资源的释放。
目的MME按每PDN连接发送修改承载请求消息给目的SGW。通知S-GWRAT间的切换已经完成，MME管理UE所有的承载上下文。
目的SGW按每PDN连接，给PGW发送修改承载请求消息，告知P-GW APN-AMBR值以及RAT Type发生改变（可以用于计费）。PGW返回修改承载响应消息给目的SGW。
目的SGW返回修改承载响应消息给目的MME，确认用户面切换成功。
当收到了前转重定位完成消息，源SGSN发送Iu释放命令消息给源RNC。源RNC的数据前转定时器超时以后，给源SGSN返回Iu释放完成消息。
如果跟踪区更新的条件满足，UE触发跟踪区更新过程。
目的MME计算UE-AMBR，如果需要修改UE-AMBR，或签约的APN-AMBR和映射得到的不同，目的MME发起签约QoS修改过程，将计算出的UE-AMBR和签约的APN-AMBR通知到eNodeB，S-GW和P-GW。
当第16步设置的定时器超时以后，MME释放非直接数据前转隧道资源。
系统影响 : 
随着用户跨RAT（LTE与3G之间）切换的增加，系统资源占用会增大，CPU占用率会相应上升。
应用限制 : 
无 
特性交互 : 
由于跨RAT（LTE与3G之间）切换流程是基本业务流程，能保证用户在不同RAT之间移动过程中，正在进行的数据业务和其他业务基本不中断，如果无法使用，则会严重影响到用户使用数据业务和其他业务的体验，增加用户对使用EPS网络的不满。
遵循标准 : 
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access". 
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for Evolved
Packet System (EPS); Stage 3". 
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network
(E-UTRAN); S1 Application Protocol (S1AP)". 
3GPP TS 29.274: "General Packet Radio Service (GPRS); Evolved
GPRS Tunnelling Protocol (eGTP) for EPS". 
3GPP TS 29.272: " Mobility Management Entity (MME) and Serving
GPRS Support Node (SGSN) related interfaces based on Diameter protocol". 
3GPP TS 23.203: "Policy and charging control architecture" 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
跨RAT（LTE与3G之间）切换流程是完成接入用户在不同RAT之间移动过程中保证业务连续性的过程，切换流程会把接入用户的资源，包括承载，切换到目的无线接入网络。
MME支持最大1500万用户接入，支持最大3000万承载。
O&M相关 : 
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
切换流程测量|编号为C4301100开头的所有计数器
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
配置特性 
测试用例 
常见问题处理 
配置特性 : 
配置前提
该功能属于基本功能，无需特别配置，只要保证基本配置及基本功能的数据配置就可以。 
SGSN和MME能够完成基本的ATTACH流程。 
SGSN与MME之间通讯正常。 
配置过程
在MME中执行命令[ADD EPCHOST]，新增对SGSN地址的解析配置。
执行命令[ADD EPCHOST]，在目标MME中增加选择SGW的配置。
配置实例
基本配置
命令脚本|解释说明
---|---
ADD EPCHOST:NAME="rnc00a9.rnc.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgsn",HOST="SGSN",IPADDR="10.10.11.1",PROTOCOL="x-gn"&"x-gp"|配置MME对于SGSN的解析，以便MME可以找到SGSN。
ADD EPCHOST:NAME="tac-lbXX.tac-hbXX.tac.epc.mncXXX.mccXXX.3gppnetwork.org",SERVICE="x-3gpp-sgw",HOST="XXX sgw",IPADDR="1.2.3.4",PROTOCOL="x-s11"|配置MME对于SGW的解析，以便MME可以找到SGW。
跨RAT切换时eNodeB和RNC之间的标识映射配置
命令脚本|解释说明
---|---
ADD ENB RNC:MCC="460",MNC="03",RNC=22,ENB=81|配置跨RAT切换时eNB和RNC之间的标识映射，用于实现MME与Gn/Gp SGSN间Inter RAT切换功能。
 说明： 
只存在RNC ID到eNodeB ID的映射，不存在eNodeB到RNC映射的场景。
跨RAT切换时TAI和RAI之间的映射配置
命令脚本|解释说明
---|---
ADD TAI RAI:MCC="460",MNC="03",LAC="8053",RAC="01",TAC="0022"|配置跨RAT切换时TAI和RAI之间的映射，用于实现MME与Gn/Gp SGSN间Inter RAT切换功能。
测试用例 : 
无 
常见问题处理 : 
无 
## ZUF-77-03-003 3G到LTE切换 
概述 : 
本特性允许用户可以在UMTS网络和LTE网络之间移动而无需使用PDP上下文，在移动过程中无数据中断，也减少了丢包。 
收益 : 
本特性便于运营商部署复杂网络（UMTS和LTE），并且在很大程度上改善了网络。 
描述 : 
在系统间切换过程中，间接前转可能请求将数据前转作为切换的一部分。MME可根据配置获知是否已申请间接前转。如果已申请，MME在SGW上分配数据前转路径用于间接前转。SGSN可根据配置获知是否已申请间接前转。如果已申请，SGSN在SGW上分配数据前转路径用于间接前转。间接前转的前提条件包括：UE处于ECM-CONNECTED或PDP-Connect状态，并且至少建立了一个PDP/EPS承载上下文。 
当网络决定进行切换时，系统间切换流程开始。根据UE、RNC或eNodeB上报的无线条件测量结果，网络决定进行从UTRAN Iu
模式到E-UTRAN的PS切换。 
# 缩略语 
# 缩略语 
APN : 
Access Point Name接入点名称
## BCM 
Basic Call Manager基本呼叫管理器
## CGI 
Cell Global Identification小区全球识别码
## CN 
Core Network核心网
## CPU 
Central Processing Unit中央处理器
## DT 
Direct Tunnel直传隧道
## DTI 
Digital Trunk Interface	数字中继接口板
E-UTRAN : 
Evolved Universal Terrestrial Radio Access Network演进的通用陆地无线接入网络
eNodeB : 
Evolved NodeB演进的NodeB
EPC : 
Evolved Packet Core演进的分组核心网
EPS : 
Evolved Packet System演进的分组系统
## GERAN 
GSM/EDGE Radio Access NetworkGSM/EDGE无线接入网
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
HLR : 
Home Location Register归属位置寄存器
HSS : 
Home Subscriber Server归属用户服务器
IMSI : 
International Mobile Subscriber Identity国际移动用户标识
LTE : 
Long Term Evolution长期演进
## MM 
Mobility Management移动性管理
MME : 
Mobility Management Entity移动管理实体
## MS 
Mobile Station移动台
NAS : 
Non-Access Stratum非接入层
## P-GW 
Packet Data Network Gateway分组数据网网关
PCRF : 
Policy and Charging Rules Function策略和计费规则功能
PDN : 
Packet Data Network分组数据网
PDP : 
Packet Data Protocol分组数据协议
PGW : 
PDN Gateway分组数据网网关
## PS 
Packet Switched分组交换
QoS : 
Quality of Service服务质量
## RA 
Routing Area路由区
## RAB 
Radio Access Bearer无线接入承载
## RAI 
Routing Area Identity路由区标识
RAN : 
Radio Access Network无线接入网
## RANAP 
Radio Access Network Application Protocol无线接入网应用协议
RAT : 
Radio Access Technology无线接入技术
## RAU 
Routing Area Update路由区更新
RNC : 
Radio Network Controller无线网络控制器
## RNTI 
Radio Network Temporary Identifier无线网络临时标识
## RRC 
Radio Resource Control无线资源控制
## S-GW 
Serving Gateway服务网关
## SAI 
Service Area Identity业务区域标识
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
SGW : 
Serving Gateway服务网关
## SRNC 
Serving Radio Network Controller服务无线网络控制器
## SRNS 
Serving RNS服务无线网络子系统
## TEID 
Tunnel Endpoint Identifier隧道端点标识
## TIN 
Terminating Intelligent Network终呼智能网
UE : 
User Equipment用户设备
## UMTS 
Universal Mobile Telecommunication System通用移动通讯系统
UTRAN : 
UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
# ZUF-77-04 安全管理 
概述 : 
功能描述 : 
在2G（GPRS）和3G（UMTS）网络中，为了防止非法用户接入，需要网络对用户进行认证，拒绝非法用户接入。	同时为了防止用户相关数据被窃听和篡改，需要对于用户的信令和承载进行完整性保护和加密。
安全管理可以解决如下诉求，提高网络安全性，提升用户体验。 
用户身份合法性校验，防止非法用户接入网络，或者防止用户接入非法网络 
终端设备合法性校验，拒绝非法设备接入网络 
用户号码保护，尽量减少用户IMSI、IMEI等信息在空口传递 
3G接入，空口用户数据完整性和私密性保护 
2G接入，用户信令或数据的私密性保护 
功能特性简介 : 
SGSN提供了不同的解决方案，解决不同的安全需求，详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
鉴权|在2G（GPRS）和3G（UMTS）网络中，为了防止非法用户接入，需要网络能够对用户进行认证，拒绝非法用户接入。	同时为了防止用户相关数据被窃听和篡改，需要对于用户的信令和承载进行完整性保护和加密。SGSN作为2G（GPRS）和3G（UMTS）网络的一部分，需要为用户提供以上安全功能。SGSN为2G/3G网络用户提供安全服务，执行对用户的鉴权，用户消息的完整性保护和加密，对用户IMEI合法性进行检查，以及为用户分配临时标识。运营商可以通过在本地用户和合法漫游用户接入到PS网络过程中对用户进行鉴权，拒绝非法用户接入PS网络，避免用户非法使用网络资源，并对后续用户的信令安全进行保护，防止用户相关数据被窃听和篡改等威胁到网络安全的行为。|ZUF-77-04-001 鉴权
二次鉴权|用户鉴权可保障合法用户的接入。在实际应用中，用户鉴权可能由于空中通道或MS等因素而失败。因此，二次鉴权可提高用户鉴权的成功率。本特性可保障合法用户接入的可靠性，提升客户满意度。|ZUF-77-04-002 二次鉴权
Gb口模式加密|在2G网络上，SGSN可加密Gb接口传输的信令和数据。本特性为Gb接口传输的信令和数据提供安全保护。|ZUF-77-04-003 Gb口模式加密
Iu口模式AS层安全模式过程|在3G网络，RNC为用户的AS层信令和数据完整性提供保护和加密功能。SGSN通知RNC使用的密钥、完整性保护算法和加密算法。为用户的AS层信令和数据完整性提供保护和加密功能。|ZUF-77-04-004 Iu口模式AS层安全模式过程
P-TMSI重分配|P-TMSI是分配给用户的分组域临时用户标识。P-TMSI可由网络侧进行分配。用户每次接入网络时都将获取不同的P-TMSI。本特性通过为用户分配P-TMSI和减少IMSI的直接使用，从而保护用户的身份。|ZUF-77-04-005 P-TMSI重分配
IMEI检查|SGSN提供IMEI检查功能。当用户进行附着或路由区更新（RAU）时，SGSN通过交换IMEI检查MD合法性，并通过基于E1或IP协议的接口（Gf接口）与EIR互连。本特性用于区别授权UE与未授权UE。UE身份验证能有效阻止未授权设备接入网络。系统可根据EIR提供的IMEI管理信息检查MS是否在黑名单中。如果MS未授权，系统拒绝为该MS提供业务。|ZUF-77-04-006 IMEI检查
ADD|SGSN支持自动设备检测（ADD）功能。SGSN可将国际移动设备识别码和软件版本号（IMEISV）发送给HSS以反映TE在硬件或软件上的变化。运营商可通过检查IMEI(SV)字段检测TE在硬件或软件上的变化，并可在为用户部署新业务的时候配置业务参数。|ZUF-77-04-007 ADD
## ZUF-77-04-001 鉴权 
特性描述 : 
摘要术语描述应用场景客户收益实现原理系统影响应用限制特性交互遵循标准特性能力 
术语 : 
术语|含义
---|---
GSM鉴权向量/鉴权三向量|包括RAND, SRES，Kc。
UMTS鉴权向量/鉴权五向量|包括RAND, XRES，CK，IK，AUTN。
GSM安全上下文|通过执行GSM AKA过程，在用户和服务网域建立，其包含Kc和CKSN等。
RAND|随机数，由HE/AuC 生成。
AUTN|鉴权令牌，用于用户对网络的鉴权。
XRES|期望的用户（USIM）响应，用于网络对用户的鉴权。
SRES|期望的用户（SIM）响应，用于网络对用户的鉴权。
Kc|GSM加密密钥。
UMTS安全上下文|通过执行UMTS AKA过程或从EUTRAN跨RAT切换到UTRAN或GERAN，在用户和服务网域建立，其包含CK，IK及KSI等。
描述 : 
定义
在2G（GPRS）和3G（UMTS）网络中，为了防止非法用户接入，需要网络能够对用户进行认证，拒绝非法用户接入。	同时为了防止用户相关数据被窃听和篡改，需要对于用户的信令和承载进行完整性保护和加密。 
SGSN作为2G（GPRS）和3G（UMTS）网络的一部分，需要为用户提供以上安全功能。 
背景知识
3GPP协议中定义了2G（GPRS）和3G（UMTS）网络如何为用户提供安全服务 
在2G网络中：SGSN对用户鉴权防止未经授权的接入。但GPRS网络存在一些安全隐患，如使用的128bit的密钥容易被破解，不支持数据的完整性保护，难以发现数据被篡改，用户无法对网络进行鉴权。 	用户与SGSN之间的NAS信令、承载进行加密，防止用户的信令和承载被监测或篡改。	SGSN为用户UE分配临时TLLI，使用TLLI标识用户，在信令中不携带IMSI，防止用户的IMSI被截获。 
在3G网络中：SGSN采用基于Milenage算法的AKA鉴权，实现了终端和网络间的双向认证，定义了强制的完整性保护和可选的加密保护，提供了更好的安全性保护。用户UE与RNC之间空口的信令、承载的进行完整性保护和加密，防止用户的信令和承载被监测或篡改。SGSN为用户UE分配临时P-TMSI，使用P-TMSI标识用户，在信令中不携带IMSI，防止用户的IMSI被截获。 
类别|2G|3G
---|---|---
鉴权算法|A3|AKA
鉴权向量|三元组RAND、SRES、Kc|五元组RAND, XRES, AUTN, CK, IK
密钥|Kc|CK、IK
用户临时标识|TTLI（等同于PTMSI）|PTMSI
支持卡类型|支持SIM/USIM卡|支持SIM/USIM卡
NAS完保|无完保|RNC完保
完保算法|无|UIA0（不完保）,UIA1, （Kasumi）,UIA2（SNOW 3G）
完保密钥|无|IK由SGSN在SMC消息发送给RNC
NAS加密|SGSN加密|RNC加密
加密算法|GEA0（不加密）,GEA1（R12后废弃，不推荐）,GEA2,GEA3,GEA4（128位加密算法,必须使用UMTS安全上下文,根据CK及IK生成）|UEA0（不加密）,UEA1, （Kasumi）,UEA2（SNOW 3G）
加密密钥|Kc/Kc128，Kc128由IK和CK生成|CK由SGSN在SMC消息发送给RNC
媒体报文加密|SGSN进行解密|RNC进行解密
是否启动鉴权|通过比较CKSN一致，可不启动鉴权。|KSI一致和PTMSI-signature校验成功可不启动鉴权
应用场景 : 
SGSN可以为2G/3G网络用户提供安全服务，执行对用户的鉴权，用户消息的完整性保护和加密，对用户IMEI合法性进行检查，以及为用户分配临时标识。 
用户鉴权
在2G/ 3G网络下，SGSN网元为用户提供鉴权服务，按照不同业务选择不同的鉴权策略。 
在设定通用鉴权策略基础上，如还需对某些用户提供更高的安全性，可再基于IMSI号段为其配置专门的鉴权策略。 
SGSN可按照下面的业务种类来选择鉴权策略2G网络3G网络附着业务类型附着业务类型路由更新业务类型路由更新业务类型业务请求业务类型业务请求业务类型Gb接入模式下的PDP激活业务类型局间切换后发起的路由更新业务类型Gb接入模式下的短信息始呼无Gb接入模式下的短信息终呼无 
2G/3G网络可选择的鉴权策略鉴权策略详细描述强制鉴权慎重使用该选项，该鉴权类型会导致对应业务类型流程每执行一次就触发一次鉴权，当用户业务类型流量较大时，会加重网络负担。强制不鉴权鉴于EPC网络非常强调网络安全和用户隐私保护，在商用局中不推荐使用“强制不鉴权”选项。系统判断SGSN检测到UE和SGSN之间没有安全环境或安全环境被破坏，则SGSN自动触发对UE鉴权，以建立新的安全环境，保障后续的信令消息在可靠的安全环境中传输。可以理解“系统判断”是在“需要”时鉴权，不“需要”时不鉴权。频次鉴权该鉴权类型是对“系统判断”类型的补充。是基于流程的，即流程每被执行N次，就触发一次鉴权。如果有一组用户执行同一个业务类型流程，那么发生在每个用户身上的鉴权概率是不均等的。 
3G网络消息完整性保护和加密
在3G网络下，如需支持对UE与RNC之间消息进行完整性保护和加密，需启动对用户鉴权后，按照下面方式对于完整性保护和加密算法设置，算法通知到RNC，由RNC完成完整性保护和加密。 
完整性保护算法|是否支持|级别
---|---|---
UIA2|支持|2（高）
UIA1|支持|1（中）
UIA0|支持（实际为不进行完保）|0（低）
完整性保护算法|是否支持|级别
---|---|---
UEA2|支持|2（高）
UEA1|支持|1（中）
UEA0|支持（实际为不进行加密）|0（低）
2G网络Gb口加密
在2G网络下，协议上不支持对消息完整性保护，只定义了Gb口消息加密。 
运营商可对不同的用户（IMEI不同）采用不同的加密算法，在同一个用户支持的多个加密算法中，还可能需要对算法设置不同的优先级。 
按照下面方式对于加密算法设置，加密由SGSN完成，在配置算法是否支持的同时，还可设置算法的优先级。 
完整性保护算法|是否支持|级别（可调整）
---|---|---
GEA3|支持|2（高）
GEA2|支持|1（中）
GEA1|支持|0（低）
IMEI检查
在2G和3G网络下，IMEI检查的作用是用于检查终端设备是否合法，目前一般情况并不启用。 
如需启用对用户进行IMEI检查，进行以下操作： 
“支持IMEI检查”开关打开 
“是否获取IMEI”开关选择为获取IMEISV 
如仅希望对某特定IMSI号段用户进行IMEI检查，进行以下操作： 
“支持IMEI检查”开关打开 
“是否获取IMEI”开关选择为获取IMEISV 
“支持基于IMSI号段IMEI检查”开关打开 
配置需要进行IMEI检查的IMSI号段 
用户分配临时标识
2G/3G网络时，SGSN需支持为用户分配临时标识（3G网络为PTMSI，2G网络为TLLI），2G或3G网络下，如SGSN采用POOL组网，为了给用户分配临时标识，SGSN需配置NRI，下面操作必须执行。
在本局移动数据管理中配置NRI长度 
在NRI管理中配置SGSN支持的NRI 
客户收益 : 
受益方|受益描述
---|---
运营商|运营商可以通过在本地用户和合法漫游用户接入到PS网络过程中对用户进行鉴权，拒绝非法用户接入PS网络，避免用户非法使用网络资源，并对后续用户的信令安全进行保护，防止用户相关数据被窃听和篡改等威胁到网络安全的行为。
移动终端用户|终端用户可以对接入的PS网络进行鉴权，避免使用到非法或损害用户利益的网络，终端用户还可以对信令和数据安全进行保护，防止用户相关数据被窃听和篡改等威胁到用户安全的行为。
实现原理 : 
系统架构
无 
涉及的网元
SGSN网元安全流程需要UE、RNC/BSS、SGSN、HLR和EIR的共同配合，各网元在安全功能中的作用包括： 
网元|作用
---|---
UE|对AS信令和数据进行安全保护（3G网络下）,或对LLC帧进行安全保护（2G网络下）或对网络进行鉴权。
BSS|传输用户和SGSN相关安全过程消息及LLC层加密帧
RNC|对用户提供接入层安全功能，对AS信令和数据进行安全保护。
SGSN|从HLR或老局SGSN获取到鉴权向量，对用户进行鉴权，配合完成IMEI检查。为用户分配临时标识，在UMTS和GSM之间互操作和系统间切换过程中，负责UMTS安全上下文和GSM安全上下文的转换；Iu接入下，在SMC过程或SRNS切换过程中通知RNC安全密钥和算法；Gb接入下，完成Gb加密协商，对LLC帧进行安全保护；
HLR|配置生成UE的鉴权数据，并提供给SGSN。
EIR|配置UE的IMEI数据，并检查UE的IMEI是否合法。
业务流程
用户鉴权
2G/3G网络附着业务鉴权图1  附着业务鉴权流程图流程说明：UE向SGSN发起附着业务。SGSN基于用户IMSI和当前附着业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权SGSN从HLR获得用户UE的鉴权数据。SGSN向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，SGSN再对用户UE进行鉴权。 
2G/3G 网络RAU业务鉴权图2  TAU业务鉴权流程图流程说明：UE向SGSN发起RAU业务。SGSN从老局SGSN获得用户的MM上下文和鉴权信息。SGSN基于用户IMSI和当前RAU业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权SGSN向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，SGSN再对用户UE进行鉴权。 
2G/3G 网络业务请求鉴权图3  业务请求鉴权流程图流程说明：UE向SGSN发起业务请求。SGSN基于用户IMSI和当前业务请求业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权SGSN向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，SGSN再对用户UE进行鉴权。 
2G网络Gb接入PDP激活鉴权图4  2G网络Gb接入PDP激活鉴权流程图流程说明：UE向SGSN发起业务请求。SGSN基于用户IMSI和当前业务请求业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权SGSN向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，SGSN再对用户UE进行鉴权。 
2G网络Gb接入短信始呼鉴权图5  2G网络Gb接入短信息始呼鉴权流程图流程说明：UE向SGSN发起短信起呼。SGSN基于用户IMSI和当前短信起呼业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权SGSN向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，SGSN再对用户UE进行鉴权。 
2G网络Gb接入短信终呼鉴权图6  2G网络Gb接入短信息终呼鉴权SGSN接收SMC短信中心发送的短信终呼。SGSN基于用户IMSI和当前短信终呼业务，调用配置获得鉴权策略，判断出是否需要鉴权，如需鉴权SGSN向用户UE发起鉴权请求，UE对网络鉴权完成后返回响应，SGSN再对用户UE进行鉴权。 
3G网络消息完整性保护和加密SMC流程图7  SMC流程图流程说明：SGSN完成对用户UE的鉴权后，向RNC发送 security mode command消息，该消息中包含密钥、完整性保护和加密算法。RNC接受完整性保护和加密的算法，向SGSN发送Security mode complete消息。 
NAS消息完整性保护机制图8  NAS层完整性保护机制流程说明：RNC发送下行NAS消息时，对NAS消息进行完整性保护，RNC将NAS下行序列号、方向位（下行）、承载标识、NAS消息、NAS信令的完整性保护密钥作为输入通过完整性保护算法获取MAC（message
authentication code）放在发送的消息中；RNC接收到上行NAS消息时，对NAS消息进行完整性检查，SGSN将NAS上行序列号、方向位（上行）、承载标识、NAS消息、NAS信令的完整性保护密钥作为输入通过完整性保护算法计算XMAC，并与接收的消息中的MAC进行比较，如果一致，则完整性检查成功。 
NAS消息加解密机制图9  NAS层加解密机制流程说明：RNC发送下行NAS消息时，对NAS消息进行加密，SGSN将NAS下行序列号、方向位（下行）、承载标识、NAS消息位长度、NAS信令的加密密钥作为输入通过加密算法计算密钥流，SGSN将获取的密钥流对NAS消息明文进行加密获取NAS消息密文。RNC接收到上行NAS消息时，对NAS消息进行解密，SGSN将NAS上行序列号、方向位（上行）、承载标识、NAS消息位长度、NAS信令的加密密钥作为输入通过加密算法计算密钥流，将其对接收的加密NAS消息进行解密获取NAS消息明文。 
2G网络Gb口加密XID协商流程图10  Gb加密协商流程图流程说明：SGSN完成对用户UE的鉴权后，向BSS发送 XID消息，该消息中包含加密密钥和加密算法。RNC接受加密算法后，向SGSN返回XID响应消息。 
Gb口消息加解密机制图11  Gb口消息加解密机制流程说明：SGSN发送下行LLC帧时，对LLC帧进行加密，SGSN将输入INPUT、方向位（下行）、加密密钥Kc通过加密算法计算输出OUTPUT，SGSN将获取的输出OUTPUT对LLC帧明文进行加密获取LLC帧密文。SGSN接收到上行LLC帧加密时，对LLC帧进行解密，SGSN将输入INPUT、方向位（上行）、加密密钥Kc通过加密算法计算输出OUTPUT，将其对接收的加密LLC帧进行解密获取LLC帧明文。 
IMEI检查
图12  IMEI检查流程图
流程说明： 
2G和3G网络下，IMEI检查的流程相同。
如果SGSN没有该用户的IMEI或IMEISV时， SGSN向用户UE发送Identity Request消息请求用户IMEI或IMEISV。 
用户UE给SGSN返回UE的IMEI或IMEISV，SGSN向EIR发送EIR Check Request消息。 
EIR网元检查UE的IMEI，将检查结果在EIR Check Respond消息中通知到SGSN，SGSN基于检查结果放行业务或拒绝业务。 
用户分配临时标识
图13  用户标识分配流程
流程说明： 
2G和3G网络下，用户分配临时标识的流程相同。 
用户UE向SGSN发起Attach或RAU请求。 
SGSN为用户UE分配P-TMSI或TLLI在Attach Accept或RAU Accept消息中携带。 
用户UE接受新的P-TMSI或TLLI，给SGSN返回Attach Complete或RAU Complete消息。 
系统影响 : 
鉴权策略的不同可能会导致SGSN与HLR之间信令增加，以及RNC/BSC和SGSN之间信令增加，故在设定鉴权策略时需注意对于Iu/Gb接口和Gr接口的影响。 
算法|系统性能影响
---|---
GEA1|性能下降7%
GEA2|性能下降4%
GEA3|性能下降2%
应用限制 : 
无 
特性交互 : 
由于安全流程是基本业务流程，是后续所有的流程的基础，如果选择需要进行安全流程却无法使用，则其他业务都无法使用。 
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060 "General Packet Radio Service （GPRS）; Service
description; Stage 2". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 33.102: "3G Security; Security architecture". 
3GPP TS 43.020: "Security related network functions". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service （GPRS）; Base
Station System （BSS） - Serving GPRS Support Node （SGSN）; BSS GPRS
Protocol （BSSGP）". 
3GPP TS 29.060: "General Packet Radio Service （GPRS）; GPRS
Tunnelling Protocol （GTP） across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part （MAP） specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
功能|能力
---|---
基于IMSI号段配置鉴权策略|最大可配置256×7个IMSI号段
基于IMSI号段进行IMEI检查|最大可配置1024个IMSI号段
特性配置 : 
摘要配置特性测试用例 
配置特性 : 
配置前提
MS、SGSN、GGSN、RNC、BSC等各网元工作正常。
SGSN网管服务器、客户端连接正常；服务器与OMP连接正常。
SGSN已经配置好相关的本地配置。 
配置过程
使用命令[SET SECURITY PARAMETER]设置SGSN安全参数。
使用命令[SET SOFTWARE PARAMETER]命令打开Gb口加密功能。
使用命令[SET GPRS ENCRYPTION]设置GPRS加密参数。
使用命令[SET ENCRYCTRL]设置UMTS AS加密控制参数。
使用命令[SET INTEGCTRL]设置UMTS AS完整性保护参数。
使用命令[ADD SGSN IMSI AUTH]命令增加基于IMSI以及IMSI range鉴权配置。
使用命令[SET SOFTWARE PARAMETER]打开基于IMSI的IMEI检查功能。
使用命令[ADD SGSN IMEI CHECK]增加基于IMSI的IMEI检查配置。
配置实例
配置用户接入鉴权配置步骤配置说明SET SECURITY PARAMETER: AUTHNUM=3配置SGSN获取鉴权向量组数为3组SET SECURITY PARAMETER:AUTHONATTACH="System
define"配置附着默认鉴权类型为系统判断ADD SGSN IMSI AUTH:IMSI="46000",IMSI="460000",SERVICETYPE="Attach",AUTHTYPE="Compelling_authentication"配置46000号段IMSI附着强制鉴权 
配置2G网络Gb接入PDP激活和短消息鉴权配置步骤配置说明SET SECURITY PARAMETER:AUTHONACTPDP="Compelling
authentication"配置对2G用户PDP激活进行强制鉴权SET SECURITY PARAMETER:AUTHSMSOUT="Compelling
authentication"配置对2G用户短消息呼出进行强制鉴权SET SECURITY PARAMETER:AUTHSMSIN="Compelling
authentication"配置对2G用户短消息呼入进行强制鉴权 
配置3G网络加密和完整性保护配置步骤配置说明SET ENCRYCTRL:ENCRYPTION="Support",ENCRYALGO="Support",ENCRYALGO1="Support",ENCRYALGO2="Support",ENCRYALGO3="Support"配置SGSN支持无加密算法、加密算法1、加密算法2、加密算法3SET ENCRYCTRL:ENCRYPTION="Support",ENCRYALGO="Support",ENCRYALGO1="Support",ENCRYALGO2="Support"配置SGSN支持完整性保护算法1和2 
配置2G网络Gb口加密某运营商要求对2G用户使用加密算法GEA1、GEA2、GEA3。配置步骤配置说明SET SOFTWARE PARAMETER:PARAID=589825,PARAVALUE=1配置SGSN支持LLC加密SET GPRS ENCRYPTION:GEA1="Support",GEA2="Support",GEA3="Support",PRIORGEA1="1",PRIORGEA2="2",PRIORGEA3="3"配置GPRS加密算法为支持GEA1、GEA2、GEA3某运营商要求对2G用户使用加密算法GEA1、GEA2、GEA3，对于IMEI中TAC为“46012345”的终端使用加密算法GEA3、GEA1，GEA3优先级最高。配置步骤配置说明SET SOFTWARE PARAMETER:PARAID=589825,PARAVALUE=1配置SGSN支持LLC加密SET GPRS ENCRYPTION:GEA1="Support",GEA2="Support",GEA3="Support",PRIORGEA1="1",PRIORGEA2="2",PRIORGEA3="3"配置GPRS加密算法为支持GEA1、GEA2、GEA3ADD TAC GEA:TAC="46012345",GEA1="ON",PRIORGEA1="2",GEA3="ON",PRIORGEA3="1"配置TAC为“46012345”终端支持GEA3、GEA1加密算法 
配置IMEI检查某运营商开启IMEI检查，需要对所有用户进行IMEI检查，向终端获取IMEI，在IMEI检查为黑名单时限制用户接入；如果IMEI获取失败，或IMEI检查流程失败，流程终止，限制用户接入。配置步骤配置说明SET SOFTWARE PARAMETER:PARAID=262150,PARAVALUE=1(2或者3)配置MME获取IMEISET SOFTWARE PARAMETER:PARAID=262181,PARAVALUE=1配置IMEI获取失败，限制用户接入某运营商开启IMEI检查，需要根据IMSI对部分号段的用户进行IMEI检查，4600100号段的用户进行IMEI检查，其他号段的用户不进行IMEI检查配置步骤配置说明SET SOFTWARE PARAMETER:PARAID=262150,PARAVALUE=1(2或者3)配置MME获取IMEISET SOFTWARE PARAMETER:PARAID=262232,PARAVALUE=1配置SGSN支持基于IMSI的IMEI检查功能ADD MME IMEI CHECK:IMSI="4600100"配置需要IMEI检查的IMSI号段 
配置PTMSI分配配置步骤配置说明SET COMBOCFG:NRILEN=6配置本局NRI长度为6SET FLEX NULLNRI:NRI=1配置NULL NRI值为1ADD FLEX NRI:NRI=11,NAME="NRI1"ADD FLEX NRI:NRI=12,NAME="NRI2"配置NRI1值为11、NRI2值为12SET COMBOCFG:FLEXEN="YES"配置本局支持Flex功能 
测试用例 : 
接入鉴权鉴权控制测试项目鉴权控制测试目的验证SGSN能正确处理用户接入时鉴权控制预置条件所有网元运行正常，OM维护正常。打开消息跟踪。SGSN配置获取3组鉴权向量，并对IMSI号段为4600010的用户设置附着强制鉴权。设置默认附着鉴权类型为系统判断。测试过程4600010号段用户和4600020号段用户分别多次附着到MME。检查网络侧用户信息和测试信令。通过准则SGSN对4600010号段的用户每次附着都进行鉴权，向HLR发送的鉴权消息中请求鉴权向量组数为3组。SGSN对4600020号段的用户除了初次附着鉴权后，后续局内PTMSI附着都不进行鉴权。消息跟踪能够跟踪到相应的消息，流程正确。 
Gb接入PDP激活鉴权测试项目Gb接入PDP激活鉴权测试目的验证SGN能正确处理2GPDP激活时鉴权控制预置条件所有网元运行正常，OM维护正常。用户已正常签约。打开消息跟踪。SGSN配置“Gb口激活PDP鉴权”为强制鉴权。测试过程用户开机发起附着并进行数据传输。检查网络侧用户信息和测试信令。通过准则在激活过程中SGSN对用户进行鉴权。鉴权成功后，用户PDP激活成功，数据业务正常。 
Gb接入短消息鉴权测试项目Gb接入短消息鉴权测试目的验证SGSN能正确处理2G短消息呼入、呼出鉴权控制预置条件所有网元运行正常，OM维护正常。2G用户已正常签约。打开消息跟踪。SGSN配置Gb口短消息呼入和呼出均为强制鉴权。测试过程用户接入后分别进行短消息呼入和呼出操作。检查网络侧用户信息和测试信令。通过准则呼入和呼出时，SGSN均对用户进行强制鉴权。消息跟踪能够跟踪到相应的消息，流程正确。 
3G网络加密和完整性保护测试项目加密和完整性保护测试目的验证SGSN能正确处理3G加密和完整性保护预置条件所有网元运行正常，OM维护正常。3G用户已正常签约。打开消息跟踪。SGSN配置UTMS加密和完整性保护算法1、2和3。MS支持加密算法2和完整性保护算法2。测试过程用户开机发起附着。检查网络侧用户信息和测试信令。通过准则SGSN发送Security Mode Command消息中选择的加密算法和完整性算法都为2。MS附着成功，业务流程正常。消息跟踪能够跟踪到相应的消息，流程正确。 
IMEI检查测试项目IMEI检查测试目的验证SGSN能正确处理IMEI检查预置条件所有网元运行正常，OM维护正常。用户签约IMEI为白名单。打开消息跟踪。SGSN开启获取用户IMEI。SGSN配置EIR，与EIR间链路正常。测试过程用户开机发起附着并进行数据。检查网络侧用户信息和测试信令。通过准则SGSN向MS获取IMEI，并发起IMEI检查流程。EIR返回IMEI检查结果为白名单，MME允许UE接入。MS附着成功，业务流程正常。消息跟踪能够跟踪到相应的消息，流程正确。 
PTMSI分配测试项目GUTI分配测试目的验证SGSN能正确处理PTMSI分配预置条件所有网元运行正常，OM维护正常。用户已正常签约。打开消息跟踪。MME在本局移动中配置支持Flex功能，且配置2个NRI，分别为11和12。测试过程用户多次进行附着。检查网络侧用户信息和测试信令。通过准则在不同的附着流程，MME发送的Attach Accept消息中分配的GUTI中既有NRI为11的PTMSI，也有NRI为12的PTMSI。MS附着成功，业务流程正常。消息跟踪能够跟踪到相应的消息，流程正确。 
## ZUF-77-04-002 二次鉴权 
概述 : 
用户鉴权可保障合法用户的接入。在实际应用中，用户鉴权可能由于空中通道或MS等因素而失败。因此，二次鉴权可提高用户鉴权的成功率。 
收益 : 
本特性可保障合法用户接入的可靠性，提升客户满意度。 
描述 : 
当首次鉴权失败后，SGSN选择另一组鉴权矢量来进行二次鉴权。由于用户可以再次进行鉴权，相对于通常的一次鉴权而言，鉴权成功率得到了提升。即使在没有合适设备（例如移动电话发生故障）或存在其他不利外部因素的情况下，本特性使用户仍可以更加容易地进行网络附着，提高了用户接入和业务的成功率。 
## ZUF-77-04-003 Gb口模式加密 
概述 : 
在2G网络上，SGSN可加密Gb接口传输的信令和数据。 
收益 : 
本特性为Gb接口传输的信令和数据提供安全保护。 
描述 : 
SGSN支持以下加密算法： 
GEA0（未加密） 
GEA1 
GEA2 
GEA3 
SGSN通过使用IMEI配置所支持的加密算法。SGSN也可配置算法优先级，并优先选择高优先级的算法。 
SGSN可基于MS获取加密算法和所支持算法之间的交集，并选择最终使用的算法。 
## ZUF-77-04-004 Iu口模式AS层安全模式过程 
概述 : 
在3G网络，RNC为用户的AS层信令和数据完整性提供保护和加密功能。 
收益 : 
为用户的AS层信令和数据完整性提供保护和加密功能。 
描述 : 
SGSN通知RNC使用的密钥、完整性保护算法和加密算法。SGSN提供如下可配置完整性保护算法：  
UIA1（Kasumi算法） 
UIA2（SNOW 3G算法） 
SGSN提供如下可配置加密算法： 
UEA0（未加密） 
UEA1（Kasumi算法） 
UEA2（SNOW 3G算法） 
## ZUF-77-04-005 P-TMSI重分配 
概述 : 
P-TMSI：分配给用户的分组域临时用户标识。本特性主要用于保护用户身份而不是直接暴露用户的IMSI。P-TMSI可由网络侧进行分配。用户每次接入网络时都将获取不同的P-TMSI。 
收益 : 
通过为用户分配P-TMSI和减少IMSI的直接使用，从而保护用户的身份。  
描述 : 
通过发送重分配P-TMSI的命令给MS，SGSN可在任意时间发起P-TMSI重分配流程。MS回送P-TMSI分配完成消息（P-TMSI
assignment completion）给SGSN。涉及到P-TMSI重分配的附着和路由更新流程只执行一次。 
## ZUF-77-04-006 IMEI检查 
概述 : 
本特性支持检查UE标识，从而对UE的合法性进行鉴权。 
收益 : 
本特性用于区别授权UE与未授权UE。UE身份验证能有效阻止未授权设备接入网络。系统可根据EIR提供的IMEI管理信息检查MS是否在黑名单中。如果MS未授权，系统拒绝为该MS提供业务。  
描述 : 
Check IMEI和Check IMEI Ack消息用于身份检查。Check
IMEI Ack消息用于回复Check IMEI消息。 
SGSN提供IMEI检查功能。当用户进行附着或路由区更新（RAU）时，SGSN通过交换IMEI检查MD合法性，并通过基于E1或IP协议的接口（即Gf接口）与EIR互连。 
在IMEI检查过程中，如果EIR回复该用户为灰名单或黑名单用户，SGSN生成告警通知以帮助运营商过滤灰名单或黑名单用户。运营商可配置是否生成告警。对于黑名单用户，运营商可拒绝其接入网络。对于灰名单用户，系统可将其视为被怀疑的黑名单用户进行跟踪。SGSN根据EIR检查结果决策是否拒绝用户接入处理详细参见下表。 
EIR检查结果|SGSN处理策略
---|---
EIR返回黑名单|拒绝
EIR返回未知设备|配置控制，默认拒绝
EIR返回灰名单|不拒绝
EIR超时无响应|配置控制，默认拒绝
EIR返回其他失败|配置控制，默认拒绝
获取EIR局向失败|配置控制，默认拒绝
当无法从MS获取IMEI (SV)时，如果SGSN支持Gf接口，SGSN可控制是否允许该MS接入网络。 
## ZUF-77-04-007 ADD 
概述 : 
SGSN支持自动设备检测（ADD）功能。SGSN可将国际移动设备识别码和软件版本号（IMEISV）发送给HSS以反映TE在硬件或软件上的变化。 
收益 : 
运营商可通过检查IMEI(SV)字段检测TE在硬件或软件上的变化，并可在为用户部署新业务的时候配置业务参数。 
描述 : 
SGSN发送IMEI(SV)给HSS，HSS发送IMEI（SV）给OTA服务器。当由于IMEI（SV）发生变化或者部署新业务需要重新配置TE时，OTA服务器通过OTA网关发送消息，用来为TE配置必要的参数。 
# ZUF-77-05 网元选择功能 
概述 : 
功能描述 : 
网元选择功能用于SGSN选择对端网元，提高了SGSN选择的灵活性，支持选择以下网元： 
GGSN 
PGW 
SGSN 
MME 
HLR 
MSC 
SMC 
CG 
功能特性简介 : 
针对不同的网元，核心网提供了多种有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
GGSN选择|PDP激活时，SGSN根据激活请求的APN选择一个可用的GGSN。SGSN选择GGSN的必要条件是：GGSN是有效的，SGSN通过节点管理确定GGSN的有效性。GGSN服务于所需承载的APN。当存在多个有效GGSN可用时，SGSN根据策略进行优选，优选策略有：负荷分担GGSN地址或地址段进行优选创建承载超时或失败时，可以重选GGSN，重选次数可配置。本特性提高SGSN选择GGSN的灵活性，便于运营商部署相应的Gn接口；提高Gn接口业务接入的稳定性，当一个GGSN发生故障，可通过其他GGSN进行业务接入。|ZUF-77-05-001 GGSN选择
PGW选择|当终端支持EPC，且EPC能力终端选择PGW开关打开时，则选择内置GGSN功能的PGW，以便终端在2G/3G和LTE网络之间进行切换。PGW选择的必要条件是：PGW有效，SGSN通过节点管理确定PGW的有效性。PGW服务于所需承载的APN。当符合必要条件的PGW有多个时，则可用通过如下条件组合进行优选：权重优先级PGW地址或地址段进行优选创建承载超时或失败时，可以重选PGW，重选次数可配置。该特性提高了PGW选择的灵活性。|ZUF-77-05-002 PGW选择
SGSN选择|SGSN选择功能是指选择一个可用的SGSN为UE服务。SGSN选择的必要条件是：用户位置在SGSN服务区。SGSN是有效的。当多个SGSN符合必要条件时，根据负荷分担进行选择。该特性提高了SSGN选择的灵活性。|ZUF-77-05-003 SGSN选择
MME选择|用户在3G网络和4G网络之间切换时，如果切换目标是eNodeB，则根据eNodeB或TAC选择目标MME。MME选择的必要条件是：用户位置在MME服务区。MME是有效的。当多个MME符合必要条件时，根据负荷分担进行选择。另外，MME和SGSN合一时，优选合一的MME。该特性实现了用户在3G网络和4G网络之间的切换。|ZUF-77-05-004 MME选择
HLR选择|SGSN选择用户的归属HLR，根据用户的IMSI决定用户归属HLR的七号信令局向。|ZUF-77-05-005 HLR选择
MSC选择|在联合附着或RAU过程中，SGSN选择一个MSC并进行注册。对于联合附着或RAU业务，SGSN可与多个MSC相连接。SGSN基于RAI映射获取LAI和LAI+IMSI，并且将LAI和LAI+IMSI与MSC局向相关联。该特性用于在PS业务通道实现CS寻呼，从而降低无线资源消耗。|ZUF-77-05-006 MSC选择
SMC选择|SGSN分析短消息的目标号码，并以此确定SMC的七号信令局向。本特性用于在PS域实现短信业务。|ZUF-55-05-007 SMC选择
CG选择|通常情况下SGSN只能连接一个CG，向其上报话单，实现本功能后，SGSN能够同时对接多个CG，实现CG间主备或负荷分担。本特性应用于SGSN的离线计费场景，SGSN可以根据用户所在位置区的PLMN，来选择使用哪个CG Profile来进行计费，这样可实现不同PLMN，采用不同CG进行不同的计费策略。本特性支持CG主备或负荷分担，提供系统在计费上的容灾能力；能够根据PLMN来选择不同CG，为运营商带来了更灵活的计费策略。|ZUF-77-05-009 CG选择
## ZUF-77-05-001 GGSN选择 
概述 : 
当SGSN与多个提供相同业务的GGSN连接时，SGSN可根据APN、位置信息和GGSN负荷分担等信息选择一个首选GGSN用于接入该业务。 
收益 : 
本特性提供以下收益： 
提高SGSN选择GGSN的灵活性，便于运营商部署相应的Gn接口。 
提高Gn接口业务接入的稳定性。当一个GGSN发生故障，可通过其他GGSN进行业务接入。 
描述 : 
对于APN，SGSN可提供多地址轮询功能。当DNS中的一个APN具有多个GGSN的IP地址时，SGSN可根据优先策略选择一个GGSN用于接入用户业务。 
SGSN总是在资源池中选择高优先级的GGSN。如果相同优先级的GGSN配置了权重，SGSN根据权重选择GGSN；如果没有配置权重，SGSN对这些GGSN进行轮选。优先级和选择模式可在操作台进行配置。 
SGSN可根据RAI或LAI配置GGSN的优先级和权重。这样SGSN可基于位置选择不同的首选GGSN。 
SGSN也可基于GGSN负荷分担原则选择GGSN。SSGN可根据GGSN的容量选择GGSN。当SGSN发送APN解析请求给DNS服务器时，DNS服务器会基于每个负荷分担策略返回一个GGSN地址。因此DNS会频繁的返回高优先级GGSN的地址。 
当PDP上下文已激活，SGSN根据发送激活请求的APN选择可用的GGSN. 
对于GGSN选择，对SGSN的要求如下： 
GGSN可用。SGSN通过节点管理确认GGSN是否可用。 
GGSN服务该APN。 
如果多个GGSN可用，SGSN根据以下策略进行最优选择。 
负荷分担 
根据GGSN地址或地址范围进行选择 
## ZUF-77-05-002 PGW选择 
概述 : 
SGSN支持根据UE提供的网络能力信息选择待激活的PGW。 
收益 : 
SGSN支持根据UE提供的网络能力信息选择待激活的PGW。 
描述 : 
ZXUN uMAC获取UE提供的网络能力信息。该信息指示该UE是否支持LTE以及是否能接入EPC核心网。 
SGSN获取HLR提供的如下用户信息： 
指示该UE是否支持LTE以及能否接入EPC核心网。 
PDN GW的IP地址。 
SGSN根据UE的能力和PGW的IP地址选择PGW。 
如果HLR/HSS上没有已签约PGW的IP地址，可从APN中获取PGW的地址，以及通过域名业务功能获取签约数据和附加信息。 
如果有多个PGW可供选择，SGSN根据以下因素选择PGW： 
PGW的可用性。PGW的可用性通过路径管理消息（Echo）和隧道管理消息（create PDP）进行检测。 
优先级和静态权重。可本地配置或从DNS获取优先级和静态权重。 
GGSN/PGW子网的优先级。从高优先级网络选取GGSN/PGW。 
当UE支持EPC并使能PGW功能，选择内置GGSN功能的PGW，以便UE能在2/3G和LTE网络间切换。  
PGW选择功能的要求如下： 
该PGW可用。SGSN通过节点管理确认PGW是否可用。 
该PGW服务APN。 
如果多个PGW可用，SGSN根据以下策略进行最优选择。 
权重 
优先级 
根据PGW地址或地址范围进行选择 
## ZUF-77-05-003 SGSN选择 
概述 : 
SGSN选择功能用于为UE选择一个可用的SGSN。 
收益 : 
本特性提高了SSGN选择的灵活性。 
描述 : 
SGSN选择功能用于为UE选择一个可用的SGSN。 
SGSN选择功能的要求如下： 
用户位于SGSN服务区。 
被选择的SGSN处于可用状态。 
如果有多个SGSN均满足要求，基于负荷分担进行选择。 
## ZUF-77-05-004 MME选择 
概述 : 
在3G网络和4G网络之间切换时，如果切换目标是eNodeB，系统根据eNodeB或TAC选择目标MME。 
收益 : 
本特性实现了3G网络和4G网络之间的切换。 
描述 : 
在3G网络和4G网络之间切换时，如果切换目标是eNodeB，系统根据eNodeB或TAC选择目标MME。 
MME选择特性的要求如下： 
用户位于MME服务区。 
被选择的MME处于可用状态。 
如果有多个MME均满足要求，基于负荷分担进行选择。 
## ZUF-77-05-005 HLR选择 
概述 : 
SGSN选择用户的归属HLR。 
收益 : 
本功能是一个基本功能。 
描述 : 
SGSN根据用户的IMSI决定用户归属HLR的七号信令局向。 
## ZUF-77-05-006 MSC选择 
概述 : 
在联合附着或RAU过程中，SGSN选择一个MSC并进行注册。 
收益 : 
本特性用于在PS业务通道实现CS寻呼，从而降低无线资源消耗。 
描述 : 
在联合附着或RAU过程中，SGSN选择一个MSC并进行注册。对于联合附着或RAU业务，SGSN可与多个MSC相连接。SGSN基于RAI映射获取LAI和LAI+IMSI，并且将LAI和LAI+IMSI与MSC局向相关联。 
## ZUF-55-05-007 SMC选择 
概述 : 
SGSN分析短消息的目标号码，并以此确定SMC的七号信令局向。 
收益 : 
本特性用于在PS域实现短信业务。 
描述 : 
SGSN分析短消息的目标号码，并以此确定SMC的七号信令局向。 
## ZUF-77-05-009 CG选择 
特性描述 : 
术语 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
应用限制 
特性交互 
遵循标准 
特性能力 
可获得性 
O&M相关 
术语 : 
无 
描述 : 
定义
本特性应用于SGSN的离线计费功能，通常情况下SGSN只能连接一个CG，向其上报话单，实现本功能后，SGSN能够同时连接多个CG，实现CG间主备或负荷分担，提高了SGSN在计费方面的稳定性与灵活性，组网架构如[图1]所示。
图1  支持CG异地容灾网络结构图
[图1]中描述了实现本功能后，SGSN与CG之间的关系图。
本功能SGSN最大支持连接16个CG，引入CG Profile概念，CG Profile为一组CG集合，最大支持2个CG，其中CG之间可以配置为主备或者负荷分担关系，CG属于某个CG Profile后，不能再归属于其他CG Profile。
SGSN可以根据用户所在位置区的PLMN，来选择使用哪个CG Profile来进行计费，这样可实现不同PLMN，采用不同CG进行不同的计费策略。SGSN本功能支持的能力情况如下：
最大支持16个CG，采用支持CG个数容量可配置的方式，默认值为2，支持2个CG，修改此配置需要重启OMP和SMP单板。
最大支持8个CG Proflie，每个CG Profile可配置两个CG，其中关系为主备或者负荷分担，负荷分担模式时，使用IMSI的后三位数值来选择CG。
CG Profile属性为“通用”的记录必须配置，但最多只有一条，在使用PLMN查找不到CG Profile时，均使用此CG Profile记录来发送话单。
运营商通过此功能，可以能够实现CG容灾，同时可对不同PLMN的用户采用不同的计费服务器来计费。
背景知识
GPRS网络架构图，如[图2]所示。
图2  GPRS架构图
网元|功能描述
---|---
TE/MT（Terminal Equipment/Mobile Terminal，终端设备/移动终端）|为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。
BSS（Base Station System，基站系统）|GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。
UTRAN（UMTS Terrestrial Radio Access Network，统一的陆地无线接入网络）|第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。
HLR(Home Location Register，归属位置寄存器)|永久存储用户签约数据。
PDN(Packet Data Network，分组数据网)|为用户提供业务的网络。
CGF(Charging Gateway Functionality，计费网关功能)|将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。
BS（Billing System，计费系统）|负责接收和处理从核心网发送过来的CDR文件。
EIR（equipment identity register 设备标识寄存器）|负责检查UE设备。
SGSN(Serving GPRS Support Node，服务GPRS支持节点)|支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS MobilityManagement）上下文和分组数据协议（PDP，Packet Data Protocol）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息。
GGSN(Gateway GPRS Support Node，GPRS支持节点网关)|负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。
MSC/VLR（Mobile Switch Center/ Visitor Location Register，移动交互中心/拜访位置寄存器）|通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。
SMS GMSC/SMS IWMSC (Short Message Service Gateway MSC/ ShortMessage Service Interworking MSC，短消息网管移动交换中心/短消息互通移动交换中心)|通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。
CAMEL (Customised Applications for Mobile network EnhancedLogic，移动网络定制应用增强逻辑服务器)|该功能实体主要对用户进行在线计费。
应用场景 : 
GPRS网络中，SGSN需要使用CG服务器对用户进行计费。
客户收益 : 
收益者|收益描述
---|---
运营商|支持CG主备或负荷分担，提供系统在计费上的容灾能力；能够根据PLMN来选择不同CG，为运营商带来了更灵活的计费策略。
移动终端用户|对终端用户不可见。
实现原理 : 
系统架构
无 
涉及的网元
本功能需要SGSN和CG共同完成。 
SGSN（Serving GPRS Support Node，服务GPRS支持节点）
支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS Mobility
Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。 
在本功能中，SGSN需要能够与多个CG同时建立GTP’连接，支持两个CG之间互为主备或负荷分担，某个CG故障时选择其他可用CG继续发送话单，同时支持3GPP
32.295协议规定的话单防重流程；另外可根据PLMN来选择不同的CG发送话单。 
CG（Charge Gateway，计费网关）
支持GTP’协议，接收来自SGSN的话单信息并上报给计费中心。 
在本功能中，SGSN需要能够支持3GPP
32.295协议规定的话单防重流程。 
协议栈
无 
本网元实现
无 
业务流程
主备/负荷分担CG
CG Profile为可包含两个CG，其中关系可为主备或者负荷分担，主备模式下正常情况一直使用主用CG，主用故障时使用备用，主用恢复后继续优先使用主用CG。
负荷分担模式下，两CG同时使用，通过IMSI号码后三位来判断选择哪个CG，达到负荷分担的效果。
例如： 
输入（IMSI后3位）|输出（CG服务器）
【0-499】|CG1
【500-999】|CG2
话单防重流程
在主备与负荷分担时，CG链路出现故障，按照3GPP 32.295协议规定有防重流程，防重流程由系统安全变量“话单防重功能”控制，如开关打开走防重流程，如关闭则话单存在缓存队列中等待故障CG恢复，新的话单选择可用CG发送
此安全变量“话单防重功能”开关，本功能建议一般情况下不打开。 
场景1：话单输出之前网元和CG的链路中断 
图3  话单输出之前网元和CG的链路中断
SGSN输出话单到CG1。
SGSN没有收到CG1的响应或者SGSN收到了CG1的响应带原因值资源不足。
SGSN把话单输出到CG2并且告诉CG2是复制话单，并且SGSN保存该话单的序列号。
CG2收到了该话单不输出话单到计费中心，返回响应给SGSN。
SGSN收到了CG1的Alive消息，返回确认给CG1。
SGSN发现有复制话单，发送空的话单携带序列号到CG1。
CG1返回Accept给SGSN。
SGSN知道CG1没有输出话单到计费中心。
SGSN通知CG2可以输出话单到计费中心。
CG2输出话单到计费中心，给SGSN返回成功响应。
场景2：话单输出之后网元和CG的链路中断 
图4  话单输出之后网元和CG的链路中断
SGSN输出话单到CG1；
SGSN没有收到CG1的响应或者SGSN收到了CG1的响应带原因值资源不足；
SGSN把话单输出到CG2并且告诉CG2是复制话单，并且SGSN保存该话单的序列号；
CG2收到了该话单不输出话单到计费中心，返回响应给SGSN；
SGSN收到了CG1的Alive消息，返回确认给CG1；
SGSN发现有复制话单，发送空的话单携带序列号到CG1；
CG1返回响应给SGSN，并告知该话单已经输出； 
SGSN通知CG2释放该复制话单；
CG2给SGSN返回成功响应。
根据PLMN选择CG
在发送话单时，SGSN使用用户当前所在的PLMN，根据CG Profile的配置，得到使用哪个CG Profile，然后再获取CG Profile中的CG。
PLMN与CG对应关系非必配置项，可以不配置。
如未配置，则SGSN会选择CG Profile属性为“通用”的记录，为防止出现某些用户话单获取不到需发给哪个CG，CG Profile属性为“通用”的记录必须配置，每次配置CG Profile时，第一条记录OMC限制一定配置为属性“通用”。
升级前准备
在版本升级时，不允许当前还有存盘的话单文件，如存在文件升级后这些文件可能无法发送到CG。
修改CG配置
删除CG服务器配置时，需将其对应的存盘话单文件发送完，否则这些文件在删除CG配置后将无法发送到CG。
另外在缓存队列中的话单，删除或修改CG配置后，这一部分的话单将丢失。
所以删除和修改CG配置请慎重操作。
系统影响 : 
本功能对系统无影响。 
应用限制 : 
无 
特性交互 : 
无 
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access". 
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for Evolved
Packet System (EPS); Stage 3". 
3GPP TS 32.295 : “Charging Data Record (CDR) transfer”. 
特性能力 : 
支持CG异地容灾功能对SGSN的特性能力无影响。
可获得性 : 
版本要求及变更记录
SGSN具备ZXUN-uMAC V4.12.10版本及后续版本。
License要求
无 
对其他网元的要求
本功能涉及SGSN与CG网元。
对于CG网元：需要能够支持3GPP 32.295协议规定的话单防重流程。
工程规划要求
O&M相关 : 
命令
无 
性能统计
无 
告警和通知
无 
业务观察/失败观察
无 
话单与计费
如果配置了主备CG或者负荷分担CG，主用的或者归属分担的CG发生链路故障，则新产生的话单可以发送的备用或者另外一个负荷分担的CG上。
特性配置 : 
配置特性 
调整特性 
测试用例 
常见问题处理 
配置特性 : 
配置说明
无 
配置前提
Ga接口的基本配置已经完成，基本的附着激活配置已经完成。 
配置过程
使用命令[SET CAPACITY]，修改CG容量。
如果默认CG容量无需修改，则这一步可以省略。如果修改了CG容量需要重启OMP和SMP。
使用命令[ADD CGCFG]，配置CG服务器。
使用命令[ADD CGPROFILE]，配置CG Profile。
使用命令[ADD CGPLMN]配置PLMN对应的CG Profile。
配置实例
实例场景
PLMN为46003的用户需要配置使用主备两个CG地址分别为40.1.136.30和40.1.136.31，
PLMN46002的用户使用负荷分担的两个CG地址分别为40.1.136.32和40.1.136.33。
配置脚本
步骤|说明
---|---
修改CG容量|将CG容量从2（默认值）修改为4SET CAPACITY:MAXCGNUM=4
配置CG服务器|增加CG1，CG1地址为40.1.136.30。ADD CGCFG:ID=1,CGADDR="40.1.136.30",CGPORT=3386增加CG2，CG2地址为40.1.136.31。ADD CGCFG:ID=2,CGADDR="40.1.136.31",CGPORT=3386增加CG3，CG3地址为40.1.136.32。ADD CGCFG:ID=3,CGADDR="40.1.136.32",CGPORT=3386增加CG4，CG4地址为40.1.136.33。ADD CGCFG:ID=4,CGADDR="40.1.136.33",CGPORT=3386
配置CG Profile|增加CG Profile1，CG1和CG2主备方式配置, 优先级1的为主，优先级为2的为备，优先级数值越低，优先级越高。ADD CGPROFILE:PROFILEID=1,CGSERVER="1"-"1"-"100"&"2"-"2"-"100"增加CG Profile2，CG3和CG4负荷分担方式配置，优先级相同，权重相同。ADD CGPROFILE:PROFILEID=2,‍CGSERVER="3"-"1"-"50"&"4"-"1"-"50"
配置CG PLMN|配置PLMN为46003的用户使用CG PROFILE1。ADD CGPLMN:PLMN="460"-"03",PROFILEID=1配置 PLMN为46002的用户使用CG PROFILE2。ADD CGPLMN:PLMN="460"-"02",PROFILEID=2
调整特性 : 
如需开启话单防重功能，如下软参设置为1，否则设置为0，默认取值0： 
65567：Prevent
Duplicated CDR 
测试用例 : 
无 
常见问题处理 : 
无 
# 缩略语 
# 缩略语 
## CG 
Charging Gateway计费网关
GPRS : 
General Packet Radio Service通用无线分组数据业务
IMSI : 
International Mobile Subscriber Identity国际移动用户标识
## OMC 
Operation & Maintenance Center操作维护中心
## OMP 
Operation & Maintenance Processor操作维护处理器
PLMN : 
Public Land Mobile Network公共陆地移动网
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
## SMP 
Signal Main Processor信令主处理模块
# ZUF-77-06 POOL 
概述 : 
功能描述 : 
SGSN POOL，是指多个SGSN核心网节点并行地共同服务于一组BSC/RNC所覆盖的无线区域，该服务区域即被称为一个POOL域（POOL Area）。移动终端在POOL域内移动时，不需要切换核心网节点。POOL功能在Iu口的技术实现也常常被称为Iu-Flex，在Gb口的技术实现被称为Gb-Flex。
SGSN POOL组网结构如[图1]所示。
图1  SGSN POOL组网结构
SGSN POOL主要功能包括： 
通过POOL内RAN节点的NNSF选择功能，保证POOL内各个SGSN的负载均衡及SGSN容灾。 
通过POOL内灵活的SGSN负荷卸载功能，减少SGSN升级/维护对在线用户的影响。 
采用SGSN POOL技术具有提高设备利用率、节省信令开销、减少局间切换以及提高网络性能等多方面的优势。POOL功能强化了网络性能，具体表现在： 
对于SGSN网元而言，多个SGSN节点之间的负荷分担成为可能。 
网络的可裁剪性、多网元间的负荷分担、漫游用户信令交互次数的减少。当用户在一个池区范围内漫游时，RAN节点总是尽可能的选择同一个SGSN节点，从HLR的角度而言，减少了SGSN与HLR之间的信令交互次数。 
功能特性简介 : 
针对SGSN POOL的应用特点和应用场景，核心网为满足容灾备份的要求，提供了多种有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
Flex|Flex支持Gb-Flex和Iu-Flex，支持多个SGSN组成POOL，用户在POOL内移动无需改变SGSN，同时POOL内SGSN之间具有相互容灾的能力。该特性应用于SGSN POOL组建和SGSN POOL运维的场景。该特性减少SGSN升级/维护等对在线用户的影响，提升用户体验；实现SGSN的容灾处理、负荷分担和平滑升级。|ZUF-77-06-001 SGSN POOL
负荷卸载|负荷卸载功能，可以在SGSN需要升级或处理能力降低时，将其注册的用户迁移到其他SGSN，避免用户下线。在某些情况下，运营商希望能从一个核心网节点有序地移除负荷（例如，进行定期维护或负荷卸载以避免过载），并且希望对终端用户影响最小和/或增加最少附加负荷到其他实体上。无需终端提供新功能，负荷卸载功能可迁移全部终端，提升用户体验。|ZUF-77-06-002 负荷卸载
优选COMBO节点|在COMBO局组网时，通过优选COMBO节点功能，用户在SGSN和MME下跨RAT移动，可以减少局间信令，降低业务时延，提高系统性能。用户进行附着、TAU/RAU或切换、RIM业务、SUSPEND业务时，RNC或eNodeB选择和老局同COMBO节点的SGSN或MME。|ZUF-77-06-003 优选COMBO节点
## ZUF-77-06-001 SGSN POOL 
特性描述 : 
术语 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
遵循标准 
特性能力 
O&M相关 
术语 : 
术语|含义
---|---
SGSN池区|SGSN池区是指UE在其间移动不需要改变服务SGSN的区域。一个SGSN池区内有一个或多个对等的SGSN。SGSN池区是由多个RA汇聚。SGSN池区间可以有交迭。
描述 : 
定义
SGSN POOL，是指多个SGSN核心网节点并行地共同服务于一组BSC/RNC所覆盖的无线区域，该服务区域即被称为一个POOL域（POOL Area）。移动终端在POOL域内移动时，不需要切换核心网节点。POOL功能在Iu口的技术实现也常常被称为Iu-Flex，在Gb口的技术实现被称为Gb-Flex。本文中，Iu-Flex和Gb-Flex也被合称为Iu/Gb-Flex。方便起见，本文也常用Flex功能指代POOL功能。
SGSN POOL组网结构如[图1]所示。
图1  SGSN POOL组网结构
采用SGSN POOL技术具有提高设备利用率、节省信令开销、减少局间切换以及提高网络性能等多方面的优势。
SGSN POOL主要功能包括：
通过POOL内RAN节点的NNSF选择功能，保证POOL内各个SGSN的负载均衡及SGSN容灾 
通过POOL内灵活的SGSN负荷卸载功能，减少SGSN升级/维护对在线用户的影响 
背景知识
GPRS网络架构
GPRS网络架构图，如[图2]所示。
图2  GPRS架构图
TE/MT（Terminal Equipment/Mobile Terminal，终端设备/移动终端）：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。 
BSS（Base Station System，基站系统）：GPRS/EDGE（2G）的无线接入网络，为终端的接入提供无线资源。 
UTRAN（UMTS Terrestrial Radio Access Network，统一的陆地无线接入网络）：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 说明：由于本文档是针对Iu/Gb-Flex在核心网PS域的描述，方便起见，BSS和UTRAN在本文中也被合称RAN。 
HLR（Home Location Register，归属位置寄存器）：永久存储用户签约数据。 
PDN（Packet Data Network，分组数据网）：为用户提供业务的网络。 
CGF（Charging Gateway Functionality，计费网关功能）：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。 
BS（Billing System，计费系统）：负责接收和处理从核心网发送过来的CDR文件。 
EIR（Equipment Identity Register，设备标识寄存器）：负责检查UE设备。 
PSCN（Packet Switched Core Network，分组交换核心网）：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元： 
SGSN（Serving GPRS Support Node，服务GPRS支持节点）：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS Mobility Management）上下文和分组数据协议（PDP，Packet Data Protocol）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息。 
GGSN（Gateway GPRS Support Node，GPRS支持节点网关）：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
MSC/VLR（Mobile Switch Center/ Visitor Location Register，移动交互中心/拜访位置寄存器）：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMSGMSC/SMS IWMSC Short Message Service Gateway MSC/ Short Message Service Interworking MSC，短消息网管移动交换中心/短消息互通移动交换中心）：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL（Customised Applications for Mobile network Enhanced Logic，移动网络定制应用增强逻辑服务器）：该功能实体主要对用户进行在线计费。 
POOL的引入
POOL功能引入之前，一个RAN节点只能对应于一个MSC Server或者SGSN节点，这导致系统本身有一些天然的缺陷。随着移动网络系统朝着松散的网络结构模式演进，系统在网络部署方面需要更为灵活多样的组网方式，因此引入Iu/Gb-Flex特性。
Iu/Gb-Flex功能是RAN支持一个RAN节点到多个SGSN节点的域内连接路由功能，SGSN在分配新P-TMSI给用户时，包含了本SGSN节点的标识NRI，用户通过RAN节点接入到SGSN时，RAN从P-TMSI/TLLI中分离出NRI，根据NRI将信令消息路由到正确的SGSN节点上。
POOL功能强化了网络性能，具体表现在： 
对于SGSN网元而言，多个SGSN节点之间的负荷分担成为可能。 
网络的可裁剪性、多网元间的负荷分担、漫游用户信令交互次数的减少。当用户在一个池区范围内漫游时，RAN节点总是尽可能的选择同一个SGSN节点，从HLR的角度而言，减少了SGSN与HLR之间的信令交互次数。 
SGSN POOL规模与NRI长度
一个SGSN POOL中可容纳的SGSN数目与NRI长度相关，NRI长度范围是1~10，去掉一个POOL内共用的NULL-NRI用于指示负荷重平衡，共剩余2N-1个NRI值可可分配个各个SGSN，每个SGSN至少一个，一个SGSN POOL内最多可部署（2N-1）个SGSN。
一般NRI长度（SGSN POOL规模大小）由运营商根据实际情况统一规划。
负荷卸载
出于网络维护的目的，比如降低某SGSN节点在POOL中业务负荷的权重或版本升级，可能需要将POOL中某个SGSN节点的用户迁移到POOL中其他的SGSN节点。为了尽可能不影响用户业务体验感受，需要引入负荷卸载功能。
具体实现的方法就是由SGSN为用户分配带NULL-NRI的P-TMSI和Non-broadcast RAI，以及很短的路由更新周期，使移动用户很快重新附着或执行RAU流程。随后RAN节点在分发用户信令报文时根据从用户P-TMSI中提取出来的NRI执行NNSF功能，选择POOL内其他SGSN，从而达到迁移用户的目的。
SGSN支持灵活多样的负荷卸载方式，主要包括：
指定卸载数量 
指定卸载比例 
指定RAN节点 
指定用户号段 
指定RAI 
指定POOL内其他SGSN接入 
运营商通过SGSN负荷卸载功能，可以在对某SGSN进行升级时，最大限度提升对用户的体验感受。
应用场景 : 
SGSN POOL组建
通常情况下，都是将一个无线连续覆盖区域组成一个SGSN POOL，如[图3]所示。SGSN1、SGSN2、SGSN3共同组成一个SGSN POOL，并同时为RAN节点（RNC1、RNC2、BSC1、BSC2）对应的无线区域（RA1、RA2、RA3、RA4）提供服务。
图3  POOL基本功能应用场景
SGSN POOL运维
SGSN POOL通过负荷卸载及可选的超容等手段，达到在尽量不影响用户的情况进行SGSN POOL扩容、升级改造及维护等目的。
SGSN POOL内SGSN新增SGSN POOL需要通过新增SGSN达到扩容的目的，此时SGSN POOL需要新增SGSN。新增的SGSN需要按POOL规划进行Flex相关配置参数。同时，基于负荷卸载功能，通过无线侧修改POOL内各SGSN权重或者由SGSN指定卸载到特定SGSN等手段，使得新上线的SGSN能够尽快接入新用户或者其他局在线用户，从而达到SGSN POOL内各SGSN尽快负载均衡的目的。如图4所示。图4  SGSN POOL内新增SGSN 
SGSN POOL内SGSN离线SGSN POOL内某SGSN需要进行软硬件升级/离线维护，为减少对驻留在该SGSN上的在线用户的影响，通过负荷卸载流程将该SGSN中的所有在线用户迁移到SGSN POOL中的其他SGSN中。如图5所示。图5  SGSN POOL内SGSN离线 
SGSN POOL内SGSN扩容（超容模式）超容对应场景如下：POOL内SGSN数目不增加，单SGSN持有的NRI数目未增加，单SGSN容量已达到极限（可分配的P-TMSI数目已达到极限，无法通过新增内部模块的方式来扩容），此时需要通过超容模式来扩容。超容模式的原理是通过压缩P-TMSI中重启计数占用的比特位，增加分配给用户的比特位，来达到单NRI可分配的P-TMSI数增加，这样对于单个SGSN而言，不需要增加NRI数目，即可达到扩容的目的。如图6所示。图6  SGSN POOL内SGSN扩容（超容模式） 
SGSN POOL内SGSN拨测为了验证SGSN POOL内所有SGSN均能正常工作，可使用一个测试用户在POOL内依次接入所有SGSN，并进行业务流程。通过“单用户指定SGSN卸载”功能可以方便快速的将测试用户从一个测试完毕的SGSN迁移到下一个待测试的SGSN。如图7所示。图7  SGSN POOL内SGSN拨测 
客户收益 : 
受益方|受益描述
---|---
运营商|容灾处理：当POOL内其中某个SGSN发生故障时，RAN节点可将用户业务发送到POOL中其他SGSN上处理。负荷分担：SGSN POOL功能对于SGSN网元而言，多个SGSN节点之间的负荷分担成为可能。当用户在一个池区范围内漫游时，RAN节点总是尽可能的选择同一个SGSN节点，从HLR的角度而言，减少了SGSN与HLR之间的信令交互次数。平滑升级：对某SGSN进行升级或扩容时，可通过负荷卸载功能，将在线用户在不影响业务的情况下搬迁到POOL内其他SGSN中，提升用户体验。
移动用户|减少SGSN升级/维护等对在线用户的影响，提升用户体验。
实现原理 : 
涉及的网元
BSC/RNCRAN节点BSC/RNC是无线接入网RAN的控制器，负责将用户的信令和数据传输到核心网SGSN。本功能中，RAN节点连接多个SGSN节点，收到NAS信令消息时，从用户报文中提取出NRI信息，当发现NRI为NULL-NRI时，执行NNSF功能，在POOL内选择其他SGSN，从而将用户迁移到其他SGSN。 
Gb模式BSC在MS接入阶段获取到用户的TMSI/P-TMSI（TLLI），从中提取出第23到N比特（根据POOL组网NRI长度配置，N的取值可以从22到14）得到NRI值。如果NRI没有配置对应的CN节点信息或者BSC获取不到NRI值，则根据负荷平衡，选取一个可用的CN点。 
Iu模式RNC在UE接入阶段从初始直传消息（RRC_initial_DT message）中获取到用户的“IDNNS”参数，并根据该参数选择CN点。如果IDNNS是从P-TMSI中获取的，则RAN从中获取NRI值选择一个CN点；如果CN点没有配置NRI或者RAN获取不到NRI值，则根据负荷平衡（load balancing），选取一个可用的CN点。如果IDNNS是从IMSI中获取的，IDNNS有一个从0 到999的(V) 值，RNC根据V值选择一个CN点。RAN节点总是尽可能的选择同一个SGSN节点，从而减少了SGSN与HLR之间的信令交互次数，减少局间切换的发生。 
SGSNPOOL组网时，SGSN需要完成如下几个功能：P-TMSI Allocation：SGSN在Attach/RAU Accept消息中或者P-TMSI Relocation消息中如果为MS分配了新的P-TMSI，则需要在P-TMSI中包含NRI字段。移动性管理：当MS进行局间Attach/RAU时，New SGSN需要通过NRI及RAI的组合查询到Old SGSN地址，并完成局间Attach/RAU过程。重定位过程：当MS进行局间重定位时，Source SGSN读取OMC的配置查询到Target SGSN地址。联合过程：SGSN在更新MSC/VLR时根据MS 的IMSI获取到V并根据V获取到对应的MSC号码，V＝(IMSI/10)%1000。CS寻呼：SGSN收到CS的寻呼后将Global CN-ID包含到寻呼消息中，以便RNC/BSS收到MS的寻呼响应后将其转交给正确的MSC/VLR。负荷重分配：OMC通过命令通知SGSN进行负荷重分配，SGSN收到后为正在接入的用户分配NULL-NRI（或POOL内其他SGSN的NRI）和Non-broadcast RAI，触发UE重新附着或RAU业务，使其分配到其他网元；或通知已经在线的用户分离后重新注册到CN，由RAN将用户分流到其他CN中。 
MSC与SGSN相关的MSC负荷卸载过程，实现原理关键是请求用户执行类型为IMSI Detach的网络侧分离过程，触发用户发起联合附着或联合路由更新。从而在下次联合附着或联合路由更新时，SGSN根据数据库的配置表选择到其他的MSC/VLR，进而SGSN连接到其他的MSC上。 
DNS ServerDNS Server提供基于NRI的域名解析，POOL内SGSN可使用NRI进行域名解析获取到POOL内其他SGSN地址信息，用于default SGSN查找POOL内其他SGSN。如果POOL内各SGSN使用网管本地配置，则不需要DNS Server增加额外NRI域名解析配置。 
业务流程
POOL功能基本流程
附着和RAU接入
正常的附着和RAU接入流程如[图8]所示。
图8  POOL内正常的负荷分担
MS/UE从RAN接入之后，向网络侧发送附着请求或RAU请求消息。
RAN接收到NAS信令消息或LLC帧时，根据MS/UE携带的NRI选择SGSN节点。如果选择失败，则在POOL内根据负荷均衡的原则执行NNSF功能，选择一个SGSN节点，向该SGSN节点转发附着或者RAU请求消息。
SGSN和MS/UE之间执行正常的安全管理功能。
SGSN判断该用户可以接入本局，为该用户分配正常的P-TMSI（携带本局NRI识别标志）和正常的RAI信息，并向MS/UE发送附着或RAU接受消息（携带P-TMSI、VLRTMSI, P-TMSI Signature, Radio Priority SMS)。
如果分配的P-TMSI发生改变，MS返回Attach Complete或RAU Complete消息给SGSN，包含收到的P-TMSI。
对于3G用户，附着/RAU流程结束后，发起Iu连接释放流程。
UE携带上一次SGSN为其分配的P-TMSI发起附着/RAU请求流程。
RAN节点收到UE的附着/RAU消息之后，从中提取NRI信息（为正常NRI信息），根据配置表，将该用户的附着/RAU请求消息转发到正确的SGSN节点。
SGSN主动负荷均衡
现网中，当SGSN启用FLEX功能时，有两种情形需要SGSN主动发起负荷均衡动作，如不做特殊处理，POOL内此SGSN的负荷将大于其他SGSN，导致负荷不均。这两种情形包括：
POOL外SGSN的NRI与POOL内某SGSN的相同。 
用户从不支持NNSF的BSC/RNC漫游进入支持NNSF的BSC/RNC。 
当出现以上两种情形时，SGSN在该用户的附着或RAU接受消息中分配含有Null-NRI的P-TMSI和Non-broadcast RAI给MS，同时分配很短的RAU更新周期时长。该功能由网管配置来控制。
用户重新附着或RAU后，BSC/RNC将按照负荷均匀的原则重新选择SGSN。
第一种情形的判断依据是： 
当SGSN接收到用户的附着或RAU请求 
当前用户所在的RAI支持FLEX。 
SGSN检查其中的Old RAI发现不属于池内RAI 
用户上报的P-TMSI的NRI属于本SGSN。 
第二种情形的判断依据是： 
当SGSN接收到用户的附着或RAU请求。 
之前用户就属于此SGSN且记录的BSC/RNC不支持NNSF。 
漫游后新的BSC/RNC支持NNSF 
漫游后用户所在的RAI支持FLEX。 
负荷卸载
SGSN前台接收到O&M发送的负荷卸载命令并处于SGSN负荷卸载状态后，业务前台将有序的将在线用户迁移到SGSN POOL中别的SGSN节点。一般在某SGSN负荷过重时，SGSN需要分离一部分用户，因此需要将用户业务迁移到其他SGSN上，对于用户是感知不到的。
系统支持通过人机界面发起负荷卸载的操作，负荷卸载分为三个阶段。 
在第一阶段接收到用户的Attach和RAU消息，则给用户分配含有Null-NRI（或者目标SGSN局的NRI）的P-TMSI和Non-broadcast RAI以及很短的RAU更新周期时长给MS，MS再次RAU后BSC/RNC重新选择SGSN。流程如[图9]所示。
图9  负荷卸载第一阶段
MS/UE从RAN接入之后，向网络侧发送附着请求或RAU请求消息。
RAN接收到NAS信令消息或LLC帧时，根据MS/UE携带的NRI正常选择SGSN节点。
SGSN和MS/UE之间执行正常的安全管理功能。
SGSN判断自己处于负荷卸载状态，决定要对当前用户进行负荷卸载，为该用户分配含有NULL-NRI（或者目标SGSN的NRI）的P-TMSI和Non-broadcast RAI信息，以及很短的RAU更新周期时长，向MS/UE发送附着或RAU接受消息（携带P-TMSI、VLRTMSI, P-TMSI Signature, Radio Priority SMS)。
第一阶段，SGSN控制用户负荷卸载处理如下： 
运营商通过配置打开SGSN负荷卸载优化，SGSN根据卸载步长设置令牌控制周期内的卸载门限，在控制周期内卸载数量超过此门限，SGSN不再进行卸载，直到下个控制周期开始。 
未开启负荷卸载优化，在此阶段，SGSN收到UE的附着、RAU请求消息后即对用户进行负荷卸载。 
MS/UE发现SGSN分配的P-TMSI发生改变，返回Attach Complete或RAU Complete消息给SGSN，其中包含收到的P-TMSI。
对于3G用户，附着/RAU流程结束后，发起Iu连接释放流程。
MS/UE的周期路由更新定时器很快超时，携带上一次SGSN为其分配的P-TMSI发起RAU请求流程。
RAN节点收到UE的RAU消息之后，从中提取NRI信息：
如果是NULL-NRI，在POOL内根据负荷均衡的原则执行NNSF功能，选择一个SGSN节点，向该SGSN节点转发RAU请求消息。 
如果是目标SGSN的NRI，则直接选择该SGSN节点，并向该SGSN节点转发RAU请求消息。 
负荷卸载状态持续一段时间之后（该时长由配置决定），进入第二阶段，具体流程如[图10]所示。
图10  负荷卸载第二阶段
第一阶段保护定时器超时，SGSN对连接态用户直接卸载触发分离；对IDLE态用户进行寻呼，建立连接后发起分离操作，并携带re-attach required标识，通知MS进行重新附着。
对需要分离的用户，如果存在激活的PDP，SGSN发起删除PDP上下文流程。
SGSN收到GGSN返回的删除PDP上下文响应。
SGSN收到用户返回的分离接受消息。
MS/UE继续发起附着请求消息，RAN节点根据正常的分发规则将MS/UE的消息分发给SGSN1。
SGSN和MS/UE之间执行正常的安全管理功能。
SGSN判断自己处于负荷状态，决定要对当前用户进行负荷卸载，为该用户分配含有NULL-NRI（或者目标SGSN的NRI）的P-TMSI和Non-broadcast RAI信息，以及很短的RAU更新周期时长，向MS/UE发送附着或RAU接受消息（携带P-TMSI、VLRTMSI、P-TMSI Signature、Radio Priority SMS)。
第二阶段，SGSN控制用户负荷卸载处理如下： 
运营商通过配置打开SGSN负荷卸载优化，SGSN根据卸载步长设置令牌控制周期内的卸载门限，在控制周期内，UE主动活动卸载和周期扫描卸载数量超过此门限，SGSN不再进行卸载，直到下个控制周期开始。 
未开启负荷卸载优化，在此阶段，SGSN收到UE的附着、RAU请求消息后即对用户进行负荷卸载，同时进行周期性扫描卸载。 
MS/UE发现SGSN分配的P-TMSI发生改变，返回Attach Complete或RAU Complete消息给SGSN，其中包含收到的P-TMSI。
对于3G用户，附着/RAU流程结束后，发起Iu连接释放流程。
MS/UE的周期路由更新定时器很快超时，携带上一次SGSN为其分配的P-TMSI发起RAU请求流程。
RAN节点收到UE的RAU消息之后，从中提取NRI信息。
如果是NULL-NRI，在POOL内根据负荷均衡的原则执行NNSF功能，选择一个SGSN节点，由此选择到另外一个SGSN节点SGSN2，向该SGSN节点转发RAU请求消息。 
如果是目标SGSN的NRI，则直接选择该SGSN节点，并向该SGSN节点转发RAU请求消息。 
第三阶段：第二阶段保护定时器超时后，系统回到正常状态。 
负荷卸载控制过程
负荷卸载控制过程如[图11]所示。
图11  负荷卸载控制过程
流程说明： 
启动负荷卸载优化，从OMM发起负荷卸载过程，SGSN启动令牌桶方式控制卸载速率， 以固定速率向桶内投放令牌。 
SGSN收到UE的附着、RAU或者周期性扫描卸载时，触发负荷卸载前，首先获取卸载令牌。 
UE活动卸载和扫描卸载时，在获取到卸载令牌后，MME对用户进行卸载。 
如果卸载时，未获取到卸载令牌，则不进行卸载。 
当卸载令牌控制周期结束后，清空剩余令牌，进入下个控制周期。 
POOL功能辅助流程
局间信令交互当MS进行局间Attach/RAU时（用户从POOL内移动到POOL外），default SGSN需要根据UE信令中提供的NRI及Old RAI信息的组合查询到Old SGSN地址，并转发ID或上下文请求完成局间Attach/RAU过程。流程如图12所示。图12  局间流程新SGSN根据Old RAI通过DNS解析获取到POOL内的缺省SGSN地址，向缺省SGSN发送MS/UE的ID Request或者SGSN Context Request请求消息。缺省SGSN收到ID Request消息或者SGSN Context Request消息，如果发现找不到该用户，并且本局支持Flex，那么缺省SGSN会根据NRI+RAI查找Old SGSN，把ID Request消息或者SGSN Context Request消息进行转发。老的SGSN收到ID Request消息或者SGSN Context Request消息，直接向新的SGSN发送ID Response或者SGSN Context Request消息。 
重定位过程当RNC需要进行重定位时，如果产生从POOL外到POOL内的SGSN局间重定位（如果已经在POOL内，则SGSN服务节点通常不需要切换）时，与Old RNC连接的Old SGSN根据Target RNC进行地址解析，会得到多个可用的SGSNIP地址（POOL内的Target RNC与多个SGSN相连）。这需要SGSN支持从多个SGSNIP地址中进行选择的功能。流程如图13所示。图13  重定位过程Source RNC向与其连接的Old SGSN发送Relocation Required消息。Old SGSN根据Target RNC可以解析到多个SGSNIP，从其中随机选择一个可用的SGSNIP。 
Gs口寻呼Gs口寻呼流程如图14所示。图14  Gs口寻呼MSC/VLR通过SGSN寻呼MS，如果MSC/VLR支持Flex，需要在寻呼消息中增加Global CNID。SGSN将Global CNID放在寻呼消息中，发送给RAN节点。RAN节点保存需要寻呼MS/UE的Global CNID信息并进行寻呼。RAN节点收到MS/UE终端寻呼响应。RAN节点根据保存的Global CNID信息直接给指定的MSC/VLR回寻呼响应。 
MSC负荷卸载当需要断开SGSN和当前连接的MSC的关联时，可通过MSC负荷卸载过程完成。第一阶段：在网络模式I下，当某个MSC进行负荷卸载时，提前通知SGSN修改Gs口IMSI hash配置表。在网管后台发送MSC负荷卸载请求时，后台已经将网管配置中已经将IMSI-LAI-VLR关系进行了重定向，使得正在进行负荷卸载的MSC不在该配置表中。 从而MS在下次联合路由更新或联合附着时，SGSN根据新的配置选择到其他的VLR，进而SGSN连接到其他的MSC上。第二阶段：第一阶段保护定时器超时后，SGSN请求剩下的在线且存在Gs口关联的UE执行类型为IMSI Detach的网络侧分离过程，触发MS发起联合路由更新。从而MS在下次联合路由更新时，SGSN根据新的配置选择到其他的VLR，进而SGSN连接到其他的MSC上。第三阶段：第二阶段保护定时器超时后，系统回到正常状态。 
业务请求为了加快负荷卸载执行过程，SGSN收到用户业务请求时，可在完成业务请求流程后发起分离操作，通知MS进行重新附着。接收到用户的附着消息后，则分配含有Null-NRI（或者目标SGSN的NRI）的P-TMSI和Non-broadcast RAI以及很短的RAU更新周期时长给MS，MS再次RAU后BSC/RNC重新选择SGSN。 
系统影响 : 
对系统，一般情况下，开启本功能对系统性能基本无影响。 
遵循标准 : 
3GPP TS 23.060: "General Packet Radio Service (GPRS); Service description; Stage 1". 
3GPP TS 23.236: "Intra-domain connection of Radio Access Network (RAN) nodes to multiple Core Network (CN) nodes (Release 6)". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification; Core Network Protocols; Stage 3". 
3GPP TS 25.331: "Radio Resource Control (RRC) Protocol Specification". 
特性能力 : 
基本特性能力
SGSN POOL功能基于开关控制。
一个SGSN最多可同时使用16个NRI。
用户容量
SGSN支持POOL功能时，支持的用户数容量会受到影响，这主要是由于支持POOL功能之后，P-TMSI中被划分出数个比特用作NRI，导致根据P-TMSI寻址用户的空间受到压缩。
当本局支持Flex功能时，按照下述公式进行容量合法检查： 
容量检查公式一（卸载寻址容量）： 
容量检查公式二（非超容）： 
容量检查公式三（超容）： 
其中： 
NUM_sgmp：控制面负荷分担中的USMP模块个数。 
MM_sgmp：license局容量配置中单USMP模块支持的MM上下文数。 
NUM_nri：普通NRI个数。 
NUM_(nri_bits)：NRI占用的比特数，或者叫NRI长度。 
Int(x)：表示对x值截取整数，省略小数部分。 
卸载所需时间
负荷卸载过程需要一定的时间才能完成。以SGSN单模块卸载10万用户、强制分离时长60分钟、扫描步长35（每秒卸载符合卸载条件的用户数目）为例：
如10万用户在卸载第一阶段期间，所有用户均已上报周期性RAU，则用户全部被卸载掉，卸载需要时长则为60分钟。 
如10万用户在卸载第一阶段期间，所有用户均未上报周期性RAU，则用户全部需要通过扫描来进行卸载，卸载共需要时长则为60分钟+48分钟（100000/35/60）。 
POOL的阶段性特征
POOL功能需要RAN节点的支持。由于技术发展的时间先后关系，存在着部分老的RAN节点不支持POOL，部分新的RAN节点支持POOL的情况。
分新的RAN节点支持POOL的情况。 为了验证开启POOL功能之后，系统的信令负荷实际提升指标，SGSN支持POOL功能的RAN节点和不支持POOL功能的RAN节点区分开来进行指标统计，如[图15]所示。
图15  SGSN 阶段POOL组网
O&M相关 : 
命令
配置项相关命令配置项参见表1。表1  命令配置项配置项命令本局移动数据SET COMBOCFGSHOW COMBOCFGNRI配置SET FLEXSHOW FLEXADD FLEX NRISET FLEX NRIDEL FLEX NRISHOW FLEX NRISET FLEX NULLNRIDEL FLEX NULLNRISHOW FLEX NULLNRIRNC局向附加属性配置ADD RNCSET RNCDEL RNCSHOW RNC网络业务实体配置ADD NSESET NSEDEL NSESHOW NSE路由区配置ADD RAISET RAIDEL RAISHOW RAIGs口MSC/VLR分担配置ADD MSCVLRSET MSCVLRDEL MSCVLRSHOW MSCVLRGPRS地址解析配置ADD SGSNHOSTSET SGSNHOSTDEL SGSNHOSTSHOW SGSNHOSTADD SGSNHOST IPADDRDEL SGSNHOST IPADDRSGSN卸载优化配置SET SGSN UNLOAD OPTSHOW SGSN UNLOAD OPT基于BSC/RNC的负荷卸载配置ADD UNLOADBSCRNCDEL UNLOADBSCRNCSHOW UNLOADBSCRNCDEL UNLOADBSCRNC ALL基于IMSI号段的负荷卸载配置ADD UNLOADNUMDEL UNLOADNUMDEL UNLOADNUM ALLSHOW UNLOADNUM基于RAI的负荷卸载配置ADD UNLOADRAIDEL UNLOADRAIDEL UNLOADRAI ALLSHOW UNLOADRAI基于MSISDN号段的负荷卸载配置ADD UNLOADMSISDNDEL UNLOADMSISDNDEL UNLOADMSISDN ALLSHOW UNLOADMSISDNSGSN卸载配置SET APPOINTSGSNSHOW APPOINTSGSNSGSN负荷卸载过程查询SHOW SGSN UNLOAD PROC 
软件参数新增软件参数参见表2。表2  新增软件参数软件参数ID软件参数名称65581支持NRI标识重复处理65582支持NNSF功能65583支持负荷卸载中数据业务65586支持指定IMSI/BSC/RNC/RAI部分卸载327797系统上电后强制鉴权时间（秒） 
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
SGSN POOL测量|C405440001 POOL内平均附着用户数-UMTS
C405440002 POOL内平均附着用户数-GSM|SGSN POOL测量
C405440003 POOL内平均激活用户数-UMTS|SGSN POOL测量
C405440004 POOL内平均激活用户数-GSM|SGSN POOL测量
C405440005 POOL内Gn/Gp口下行平均速率(KB/s)-UMTS|SGSN POOL测量
C405440006 POOL内Gn/Gp口下行平均速率(KB/s)-GSM|SGSN POOL测量
C405440007 POOL内Gn/Gp口上行平均速率(KB/s)-UMTS|SGSN POOL测量
C405440008 POOL内Gn/Gp口上行平均速率(KB/s)-GSM|SGSN POOL测量
告警和通知
新增告警/通知参见[表4]。
告警和通知
---
2114060324 取消SGSN负荷卸载通知
2114060326 SGSN负荷卸载成功结束通知
业务观察/失败观察
基于数量或者比例的负荷卸载
功能描述：根据组网需要，比如某SGSN减少单板或者退服，将某一SGSN单板上的用户全部卸载掉。 
操作描述：在设置flex配置中，配置需要卸载的指定比例或数量。执行命令SET FLEX:USRSTHD=1000,UNLOADNUM=50000;在动态管理中执行卸载类型为“按比例卸载SGSN”或“按数量卸载SGSN”的SGSN负荷卸载，使SGSN进入负荷卸载态。按比例卸载SGSN：执行命令EXEC UNLOAD:ACT="SGSN",MODULE=1&5,TYPE="BY_RATE";按数量卸载SGSN：执行命令EXEC UNLOAD:ACT="SGSN",MODULE=1&5,TYPE="BY_AMOUNT"; 说明：此命令执行过程中“MODULE”为可选项，如果有指定模块，则在指定模块下执行卸载，否则在全局范围内进行卸载。该选项只有卸载类型为指定数量卸载、指定比例卸载两种方式配置，其他卸载类型不可配置。 
基于RNC/BSC负荷卸载
功能描述： 
根据组网需要，比如配合进行割接，将某个BSC/RNC上的用户全部负荷卸载掉。
操作描述： 
设置需要卸载的BSC或者RNC。
按BSC（通过NSE体现）： 
执行命令[ADD UNLOADBSCRNC]:NSE =1000;
按RNC（通过RNC ID体现）： 
执行命令[ADD UNLOADBSCRNC]:RNC =255;
在动态管理中执行负荷卸载，使SGSN处于负荷卸载态。 
执行命令[EXEC UNLOAD]:ACT="SGSN",TYPE="BY_RNC_BSC";
 说明： 
如果软参“支持指定IMSI/BSC/RNC/RAI部分卸载”（软参号：65586
）为“支持”则表示还同时支持指定数量，即卸载指定BSC/RNC下一定数量的用户。
基于路由区负荷卸载配置
功能描述： 
根据组网需要，比如配合进行割接，将某个RA上的用户全部负荷卸载掉。
操作描述： 
设置需要卸载的RAI
执行命令[ADD UNLOADRAI]:RAI="123101";
在动态管理中执行负荷卸载，使SGSN处于负荷卸载态。
执行命令[EXEC UNLOAD]:ACT="SGSN",TYPE="BY_RAI";
如果软参“支持指定IMSI/BSC/RNC/RAI部分卸载”（软参号：65586
）为“支持”则表示还同时支持指定数量，即卸载指定RAI下一定数量的用户。
基于IMSI号段负荷卸载配置
功能描述： 
根据组网需要，将某个IMSI号段内的用户全部负荷卸载掉。
操作描述： 
设置需要卸载的IMSI号段：
执行命令[ADD UNLOADRAI]:IMSI="4600200117";
在动态管理中执行负荷卸载，使SGSN处于负荷卸载态： 
执行命令[EXEC UNLOAD]:ACT="SGSN",TYPE="BY_IMSI";
 说明： 
如果软参“支持指定IMSI/BSC/RNC/RAI部分卸载”（软参号：65586
）为“支持”则表示还同时支持指定数量，即卸载指定IMSI号段下一定数量的用户。
查询负荷卸载状态
功能描述： 
在执行负荷卸载过程中，可以执行该命令查看当前在线用户比例，已卸载用户数等信息，以及时了解卸载状态，判断是否可以手动停止卸载。 
操作描述： 
执行命令[SHOW UNLOADSTATE]
停止负荷卸载配置
功能描述： 
在负荷卸载过程中，通过查询负荷卸载情况决定可以结束负荷卸载时，可以使用该命令结束负荷卸载。 
操作描述： 
执行命令[CANCEL UNLOAD]
该命令可以停止以上所有类型的负荷卸载。 
特性配置 : 
摘要配置特性测试用例常见问题处理 
配置特性 : 
配置前提
在SGSN开启SGSN POOL功能之前，需要提前与运营商获取SGSN POOL相关的基础信息，包括：
NRI长度。 
分配给本SGSN的NRI数目及NRI值。 
SGSN POOL规划好的NULL NRI及分配给本SGSN的非广播路由区。 
归属于本SGSN POOL的RNC、BSC、RAI信息。 
如果CS开启了MSC POOL功能，并且SGSN与该MSC POOL中的MSC存在Gs口，需要获取每个MSC对应的IMSI V值段及关联的位置区。 
如果SGSN POOL相关域名解析在本地网管配置，还需要获取SGSN POOL内其他SGSN的IP地址、NRI、非广播路由区信息，基于NRI/RAI/RNCID进行SGSN POOL内其他SGSN域名解析配置。 
配置过程
SGSN POOL组建
根据运营商规划好的SGSN POOL数据，对SGSN POOL内的SGSN逐个进行POOL配置。
基础配置内容包括：本局移动数据Flex相关配置、Flex配置、NRI配置、NULL NRI配置、RNC局向附加属性Flex相关配置、网络业务实体Flex相关配置、路由区Flex相关配置。 
如果SGSN POOL域名解析在各SGSN本地网管配置，还包括：SGSN地址解析Flex相关配置。 
如果存在Gs口，而且MSC开启了POOL功能，还包括：MSC/VLR分担Flex相关配置。 
SGSN POOL内SGSN新增
新增SGSN的POOL相关配置，参见[SGSN POOL组建]。
SGSN POOL内新接入的SGSN可以通过负荷卸载接管SGSN POOL内其他SGSN的部分在线用户，这样可让SGSN POOL内SGSN尽快再次负荷均衡。
负荷重平衡主要处理过程如下： 
在SGSN POOL内其他SGSN设置指定SGSN卸载的NRI为本次新增的SGSN。
在SGSN POOL内其他SGSN进行负荷卸载操作，卸载部分用户到本次新增的SGSN中，可以通过指定IMSI号段、指定路由区、指定RNC/BSC、或指定比例等方式来达到卸载部分用户的目的，现场可根据实际情况灵活操作。
涉及的配置包括： 
指定SGSN卸载配置。 
指定部分用户卸载：Flex配置基于BSC/RNC的负荷卸载配置、基于IMSI号段的负荷卸载配置、基于RAI的负荷卸载配置、基于MSISDN号段的负荷卸载配置。 
请求负荷卸载命令。 
SGSN POOL内SGSN离线
SGSN POOL内某个SGSN需要离线维护时，需要先将该SGSN中在线用户通过负荷卸载迁移到其他SGSN中。该卸载过程不需要指定SGSN，需要卸载全部用户，通过分配给终端的NULL NRI，由RAN节点将卸载用户负荷均衡的分担到其他SGSN中。
涉及的配置包括：请求负荷卸载命令。 
对SGSN POOL内SGSN进行扩容。新增一种NRI配置模式，将单NRI可分配的PTMSI数扩容，可保证在NRI长度为7时，最多能支持100万附着用户。 
SGSN POOL内SGSN拨测
通过“单一指定用户卸载到指定SGSN”
功能可以方便快速的将测试用户从一个测试完毕的SGSN迁移到下一个待测试的SGSN。
涉及配置包括： 
指定SGSNNRI配置。 
软参“与POOL中SGSN的NRI重复处理”。 
基于IMSI号段的负荷卸载配置。 
OMM触发分离移动用户动态管理命令。 
OMM触发指定SGSN的PTMSI重分配动态管理命令。 
配置实例
SGSN POOL组建
数据规划： 
一个由3个SGSN节点SGSN1、SGSN2、SGSN3共同组成一个SGSN POOL，并同时为RAN节点（RNC1，RNC2，BSC1，BSC2）对应的无线区域（RA1、RA2、RA3、RA4）提供服务（其中RA1归属LA1,RA2归属LA2,RA3归属LA3,RA4归属LA4）,且SGSN1、SGSN2、SGSN3都和MSCServer1相连。 其余参数规划见下表。
SGSN节点|SGSN节点1|SGSN节点2|SGSN节点3
---|---|---|---
NRI 长度|3|3|3
NRI 长度|3|3|3
NULL NRI|5|5|5
LAI|LA1&LA2&LA3&LA4|LA1&LA2&LA3&LA4|LA1&LA2&LA3&LA4
RAI|RA1&RA2&RA3&RA4|RA1&RA2&RA3&RA4|RA1&RA2&RA3&RA4
BSC|BSC1&BSC2|BSC1&BSC2|BSC1&BSC2
RNC|RNC1&RNC2|RNC1&RNC2|RNC1&RNC2
NO-Broadcast RA|RA5|RA6|RA7
配置命令及过程： 
命令|描述
---|---
SET COMBOCFG:NRILEN=3|配置NRI长度，3个SGSN均需要配置。
ADD FLEX NRI:NRI=2,NAME=" SGSN1_NRI2"SET FLEX NULLNRI:NRI=5,NAME="NULLNRI"|配置SGSN1 NRI和NULL NRI值。
ADD FLEX NRI:NRI=3,NAME=" SGSN2_NRI3"SET FLEX NULLNRI:NRI=5,NAME="NULLNRI"|配置SGSN2 NRI和NULL NRI值。
ADD FLEX NRI:NRI=4,NAME=" SGSN3_NRI4"SET FLEX NULLNRI:NRI=5,NAME="NULLNRI"|配置SGSN3 NRI和NULL NRI值。
SET COMBOCFG:FLEXEN=YES|设置本局支持Flex，3个SGSN均需要配置。
ADD RNC:RNCOFFID=1,MCC="460",MNC="03",RNC=1,FLEX=YES,RAT=UTRAN,NAME="RNC1"ADD RNC:RNCOFFID=2,MCC="460",MNC="03",RNC=2,FLEX=YES,RAT=UTRAN,NAME="RNC2"|设置RNC局向支持Flex，3个SGSN均需要配置。
ADD NSE:NSEI=1,FLEX="YES",BEARMODE="IP",NSVCMODE="Static",NAME="BSC1"ADD NSE:NSEI=2,FLEX="YES",BEARMODE="IP",NSVCMODE="Static",NAME="BSC2"|设置BSC局向支持Flex，3个SGSN均需要配置。
ADD RAI:NAME="RAC5",LAI="LAC5",RAC="05",FLEX="YES",BROADCAST="YES"ADD RAI:NAME="RAC1",LAI="LAC1",RAC="01",FLEX="YES"ADD RAI:NAME="RAC2",LAI="LAC2",RAC="02",FLEX="YES"ADD RAI:NAME="RAC3",LAI="LAC3",RAC="03",FLEX="YES"ADD RAI:NAME="RAC4",LAI="LAC4",RAC="04",FLEX="YES"|设置SGSN1 NO-Broadcast RA以及关联的RA支持Flex。
ADD RAI:NAME="RAC6",LAI="LAC6",RAC="06",FLEX="YES",BROADCAST="YES"ADD RAI:NAME="RAC1",LAI="LAC1",RAC="01",FLEX="YES"ADD RAI:NAME="RAC2",LAI="LAC2",RAC="02",FLEX="YES"ADD RAI:NAME="RAC3",LAI="LAC3",RAC="03",FLEX="YES"ADD RAI:NAME="RAC4",LAI="LAC4",RAC="04",FLEX="YES"|设置SGSN2 NO-Broadcast RA以及关联的RA支持Flex。
ADD RAI:NAME="RAC7",LAI="LAC7",RAC="07",FLEX="YES",BROADCAST="YES"ADD RAI:NAME="RAC1",LAI="LAC1",RAC="01",FLEX="YES"ADD RAI:NAME="RAC2",LAI="LAC2",RAC="02",FLEX="YES"ADD RAI:NAME="RAC3",LAI="LAC3",RAC="03",FLEX="YES"ADD RAI:NAME="RAC4",LAI="LAC4",RAC="04",FLEX="YES"|设置SGSN3 NO-Broadcast RA以及关联的RA支持Flex。
ADD MSCVLR:NAME="LAC1",LAI="LAC1",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC2",LAI="LAC2",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC3",LAI="LAC3",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC4",LAI="LAC4",VLRCODE="8613999999999999"|设置SGSN1 MSC负荷分担。
ADD MSCVLR:NAME="LAC1",LAI="LAC1",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC2",LAI="LAC2",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC3",LAI="LAC3",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC4",LAI="LAC4",VLRCODE="8613999999999999"|设置SGSN2 MSC负荷分担。
ADD MSCVLR:NAME="LAC1",LAI="LAC1",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC2",LAI="LAC2",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC3",LAI="LAC3",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC4",LAI="LAC4",VLRCODE="8613999999999999"|设置SGSN3 MSC负荷分担。
ADD SGSNHOST:NAME="nri0003.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="BBB.BBB.BBB.BBB"ADD SGSNHOST:NAME="nri0004.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="CCC.CCC.CCC.CCC"|SGSN1配置路由区XXXX（RA1&RA2&RA3&RA4）解析到SGSN2（BBB.BBB.BBB.BBB）和SGSN3（CCC.CCC.CCC.CCC）。
ADD SGSNHOST:NAME="nri0002.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="AAA.AAA.AAA.AAA"ADD SGSNHOST:NAME="nri0004.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="CCC.CCC.CCC.CCC"|SGSN2配置路由区XXXX（RA1&RA2&RA3&RA4）解析到SGSN1（AAA.AAA.AAA.AAA）和SGSN3（CCC.CCC.CCC.CCC）。
ADD SGSNHOST:NAME="nri0002.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="AAA.AAA.AAA.AAA"ADD SGSNHOST:NAME="nri0003.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="BBB.BBB.BBB.BBB"|SGSN3配置路由区XXXX（RA1&RA2&RA3&RA4）解析到SGSN1（AAA.AAA.AAA.AAA）和SGSN2（BBB.BBB.BBB.BBB）。
SGSN POOL内SGSN新增
数据规划: 
一个由2个SGSN节点组成的SGSN POOL，并同时为RAN节点（RNC1，RNC2，BSC1，BSC2）对应的无线区域（RA1、RA2、RA3、RA4）提供服务（其中RA1归属LA1,RA2归属LA2,RA3归属LA3,RA4归属LA4）,现在需要在该POOL中新增一个SGSN3，其余参数规划见下表。
SGSN节点|SGSN节点1|SGSN节点2|SGSN节点3
---|---|---|---
NRI 长度|3|3|3
NRI 长度|3|3|3
NULL NRI|5|5|5
LAI|LA1&LA2&LA3&LA4|LA1&LA2&LA3&LA4|LA1&LA2&LA3&LA4
RAI|RA1&RA2&RA3&RA4|RA1&RA2&RA3&RA4|RA1&RA2&RA3&RA4
BSC|BSC1&BSC2|BSC1&BSC2|BSC1&BSC2
RNC|RNC1&RNC2|RNC1&RNC2|RNC1&RNC2
NO-Broadcast RA|RA5|RA6|RA7
配置命令及过程： 
命令|描述
---|---
SET COMBOCFG:NRILEN=3|配置NRI长度。
ADD FLEX NRI:NRI=4,NAME=" SGSN3_NRI4"SET FLEX NULLNRI:NRI=5,NAME="NULLNRI"|配置SGSN3 NRI和NULL NRI值。
SET COMBOCFG:FLEXEN=YES;|设置本局支持Flex。
ADD RNC:RNCOFFID=1,MCC="460",MNC="03",RNC=1,FLEX=YES,RAT=UTRAN,NAME="RNC1"ADD RNC:RNCOFFID=2,MCC="460",MNC="03",RNC=2,FLEX=YES,RAT=UTRAN,NAME="RNC2"|设置RNC局向支持Flex。
ADD NSE:NSEI=1,FLEX="YES",BEARMODE="IP",NSVCMODE="Static",NAME="BSC1"ADD NSE:NSEI=2,FLEX="YES",BEARMODE="IP",NSVCMODE="Static",NAME="BSC2"|设置BSC局向支持Flex。
ADD RAI:NAME="RAC7",LAI="LAC7",RAC="07",FLEX="YES",BROADCAST="YES"ADD RAI:NAME="RAC1",LAI="LAC1",RAC="01",FLEX="YES"ADD RAI:NAME="RAC2",LAI="LAC2",RAC="02",FLEX="YES"ADD RAII:NAME="RAC3",LAI="LAC3",RAC="03",FLEX="YES"ADD RAI:NAME="RAC4",LAI="LAC4",RAC="04",FLEX="YES"|设置SGSN3 NO-Broadcast RA以及关联的RA支持Flex。
ADD MSCVLR:NAME="LAC1",LAI="LAC1",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC2",LAI="LAC2",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC3",LAI="LAC3",VLRCODE="8613999999999999"ADD MSCVLR:NAME="LAC4",LAI="LAC4",VLRCODE="8613999999999999"|设置SGSN3 MSC负荷分担。
ADD SGSNHOST:NAME="nri0004.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="CCC.CCC.CCC.CCC"|SGSN1配置路由区XXXX （RA1&RA2&RA3&RA4）解析到SGSN3（CCC.CCC.CCC.CCC）。
ADD SGSNHOST:NAME="nri0004.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="CCC.CCC.CCC.CCC"|SGSN2配置路由区XXXX（RA1&RA2&RA3&RA4）解析到SGSN3（ CCC.CCC.CCC.CCC）。
ADD SGSNHOST:NAME="nri0002.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="AAA.AAA.AAA.AAA"ADD SGSNHOST:NAME="nri0003.racXXXX.lacXXXX.mnc003.mcc460.GPRS",IPADDR="BBB.BBB.BBB.BBB"|SGSN3配置路由区XXXX（RA1&RA2&RA3&RA4）解析到SGSN1（AAA.AAA.AAA.AAA）和SGSN2（ BBB.BBB.BBB.BBB）。
SET APPOINTSGSN:ISSPECNRI="YES",SPECNRI=4|SGSN1和SGSN2上配置，指定卸载到NRI为4的SGSN。
SET SOFTWARE PARAMETER:PARAID=65581,PARAVALUE=0|关闭“支持NRI标识重复处理”。
SET SOFTWARE PARAMETER:PARAID=65586,PARAVALUE=1|支持指定IMSI/BSC/RNC/RAI部分卸载。
ADD UNLOADBSCRNC:NSE=BSC1ADD UNLOADBSCRNC:NSE=BSC1ADD UNLOADBSCRNC:RNC=RNC1ADD UNLOADBSCRNC:RNC=RNC2|基于BSC/RNC的负荷卸载配置。
ADD UNLOADNUM:IMSI="46003"|基于IMSI号段的负荷卸载配置。
ADD UNLOADRAI:RAI="RA1"ADD UNLOADRAI:RAI="RA2"ADD UNLOADRAI:RAI="RA3"ADD UNLOADRAI:RAI="RA4"|基于RAI的负荷卸载配置。
ADD UNLOADMSISDN:MSISDN="8613675138"|基于MSISDN号段的负荷卸载配置。
EXEC UNLOAD:ACT="SGSN",TYPE="BY_RATE"|按比例卸载。
EXEC UNLOAD:ACT="SGSN",TYPE="BY_AMOUNT"|按数量卸载。
EXEC UNLOAD:ACT="SGSN",TYPE="BY_RNC_BSC"|基于BSC/RNC的负荷卸载配置。
EXEC UNLOAD:ACT="SGSN",TYPE="BY_RAI"|基于IMSI号段的负荷卸载配置。
EXEC UNLOAD:ACT="SGSN",TYPE="BY_IMSI"|基于RAI的负荷卸载配置。
EXEC UNLOAD:ACT="SGSN",TYPE="BY_MSISDN"|基于MSISDN号段的负荷卸载配置。
SGSN POOL内SGSN离线
数据规划: 
一个由3个SGSN节点SGSN1、SGSN2、SGSN3共同组成一个SGSN POOL，并同时为RAN节点（RNC1，RNC2，BSC1，BSC2）对应的无线区域（RA1、RA2、RA3、RA4）提供服务（其中RA1归属LA1,RA2归属LA2,RA3归属LA3,RA4归属LA4）,且SGSN1、SGSN2、SGSN3都和MSCServer1相连，现对SGSN3进行离线维护操作
配置命令及过程: 
命令|描述
---|---
SET FLEX:USRSTHD=0|设置卸载参数。
EXEC UNLOAD:ACT="SGSN",TYPE="BY_RATE"|按比例卸载。
SGSN POOL内SGSN扩容（超容模式）
数据规划： 
SGSN POOL网络计划使用7bit长度的NRI，有三个bit固定分配，实际一个POOL内可分配的NRI数目只有15个，一个SGSN目前来看只能有一个NRI，且要求单SGSN需要支持100万附着用户（需要200万MM上下文容量，按在线与不在线用户比为1:1进行上下文冗余预留，对应200万不冲突的PTMSI寻址），而目前SGSN在长度为7bit的单NRI情况下，最多支持可分配52万条不冲突的PTMSI寻址，需要扩容。 
配置命令及过程: 
命令|描述
---|---
SET COMBOCFG:NRILEN=7|设置为使用超容模式分配，NRI长度设置为规划值（nri length =7）。
ADD FLEX NRI:NRI=1,NAME="example"|配置NRI值为1，名字为example。
SET FLEX NULLNRI:NRI=0,NAME="example"|配置NULL NRI值为1，名字为example。
SET COMBOCFG:FLEXEN="ULTRA"|打开本局支持超容模式开关。
SET SOFTWARE PARAMETER:PARAID=327796,PARAVALUE=1|打开两个触发鉴权的软参（327796和327797软参）。
SET SOFTWARE PARAMETERPARAID=327797,PARAVALUE=6480|打开两个触发鉴权的软参（327796和327797软参）。
SGSN POOL内SGSN拨测
数据规划： 
一个由2个SGSN节点SGSN1（NRI=2）、SGSN2（NRI=3）共同组成一个SGSN POOL，启用“单用户指定SGSN卸载”功能验证SGSN POOL内所有SGSN是否均能正常工作，用户是否能快速的从SGSN1迁移到SGSN2。
配置命令及过程： 
命令|描述
SET APPOINTSGSN:ISSPECNRI="YES",SPECNRI=3|配置SGSN1支持指定SGSN卸载，且目标SGSN的NRI为3。
SET SOFTWARE PARAMETER:PARAID=65581,PARAVALUE=0|SGSN2关闭“支持NRI标识重复处理”。
SET SOFTWARE PARAMETER:PARAID=65586,PARAVALUE=1|支持指定IMSI/BSC/RNC/RAI部分卸载。
ADD UNLOADNUM:IMSI="460030000000001"|配置指定IMSI进行卸载。
DETACH USER:IMSI="460030000000001"|OMM分离用户，使用户快速分离。
测试用例 : 
SGSN POOL组建 
测试项目|SGSN POOL组网测试。
测试目的|验证SGSN POOL中MME负荷的平衡性。
预置条件|SGSN POOL组网配置正确。SGSN POOL与外围RAN、HLR、DNS等通讯正常。
测试过程|批量用户从同一个RAN上线。查询POOL中各个MME的用户数。查询用户分配的PTMSI。
通过准则|SGSN分配的PTMSI中包含NRI,且为网管配置的NRI。POOL内SGSN均有用户，且分布均匀。
测试结果|—
SGSN POOL内SGSN新增 
测试项目|SGSN POOL内SGSN新增。
测试目的|验证新增POOL内SGSN能否按照NRI配置规则分配P-TMSI。
预置条件|SGSN支持POOL功能。SGSN配置有至少多个有效的NRI（非NULL NRI）。SGSN至少配置有2个RNC， RNC1不支持Flex， RNC2支持Flex，两个RNC不能同时管理同一路由区。
测试过程|SGSN仅配置一个有效NRI。用户从RNC2发起IMSI附着。用户从RNC2发起P-TMSI附着。用户从RNC2发起RAU。
通过准则|用户附着，RAU成功。.每次给用户分配的P-TMSI中正确包含NRI值，NRI就是SGSN配置的NRI值。
测试结果|—
SGSN POOL内SGSN离线 
测试项目|SGSN POOL内SGSN离线。
测试目的|验证POOL内SGSN能否将所有用户卸载
预置条件|SGSN支持POOL功能。SGSN配置有至少多个有效的NRI（非NULL NRI）。SGSN至少配置有2个RNC， RNC1不支持Flex， RNC2支持Flex，两个RNC不能同时管理同一路由区。
测试过程|SGSN仅配置一个有效NRI。用户从RNC2发起IMSI附着。用户从RNC2发起P-TMSI附着。用户从RNC2发起RAU。
通过准则|用户附着，RAU成功。每次给用户分配的P-TMSI中正确包含NRI值，NRI就是SGSN配置的NRI值。
测试结果|—
SGSN POOL内SGSN扩容（超容模式） 
测试项目|SGSN POOL内SGSN扩容（超容模式）。
测试目的|验证开启超容模式业务正常。
预置条件|OMC和前台通信正常。规划了NRI值、NULL NRI 值、NRI长度。模块容量已规划。
测试过程|按规划SGSN配置启用超容模式。.根据提示重启整局验证基本业务。
通过准则|基本业务正常
测试结果|通过
SGSN POOL内SGSN拨测 
测试项目|SGSN POOL内SGSN拨测。
测试目的|验证POOL内SGSN是否是否能正常工作。
预置条件|SGSN1、SGSN2支持POOL功能，SGSN1支持NRI1,SGSN2支持NRI2。配置SGSN1支持指定SGSN卸载，NRI为NRI2。配置SGSN1支持IMSI负荷卸载。SGSN至少配置有2个RNC， RNC1不支持Flex， RNC2支持Flex，两个RNC不能同时管理同一路由区。
测试过程|用户从RNC2发起IMSI附着。执行基于IMSI负荷卸载执行detach type为re-attach required的分离。
通过准则|用户重新附着或RAU到本局，本局分配携带NRI2的PTMSI用户再次附着,RAN根据NRI选择目标SGSN，用户在目标SGSN附着完成。
测试结果|—
常见问题处理 : 
配置SGSN_POOL失败，主要原因是配置的SGSN参数不符合业务约束，比如配置的NRI的值不合业务要求，此时需要根据提示检查配置的参数是否符合要求。
## ZUF-77-06-002 负荷卸载 
概述 : 
通过负荷卸载功能，SGSN允许注册在一个SGSN上的UE移动到同一个池域中的其他SGSN上。 
收益 : 
在某些情况下，网络运营商希望能从一个核心网节点有序地移除负荷（例如，进行定期维护或负荷卸载以避免过载），并且希望对终端用户影响最小和/或增加最少附加负荷到其他实体上。无需终端提供新功能，负荷卸载功能可迁移全部终端。 
描述 : 
通过在SGSN执行相关O&M命令发起UE卸载。 
在第一阶段（两倍周期性路由区更新时长），进行路由区更新或附着的UE被迁移到同一个资源池中的其他核心网节点上。当核心网节点收到Routing
Area Update请求或Attach请求时，该节点返回Accept消息，携带新P-TMSI、null-NRI和non-broadcast
RAI。在PS域中，通过在Accept消息中将周期性路由区更新定时器时长设置为一个相当低的值（推荐设置为4秒）来触发新的路由区更新。由于存在null-NRI，在UE发送新的Routing Area Update消息给RAN节点之后不久，就被路由到新SGSN。 
在第二阶段，SGSN要求全体UE尝试建立PDP上下文以进行分离和再附着。当UE再次附着时，SGSN使用上述第一阶段描述的方法迁移UE. 
第三阶段包括扫描剩余UE，以及发起迁移操作将UE移动到其他SGSN上。由于要求UE在PS域进行分离和再附着，导致该UE被迁移。当连接到该资源池的BSC或RNC发起相应的O&M命令，要求该UE再次注册到同一个SGSN时，停止从该SGSN移出该UE。UE也可能由于在正在进行卸载操作的SGSN上进行注册而被停止移入一个池域。核心网节点需确认迁移操作不会造成网络过负荷。在多个SGSN同时进行卸荷时，BSC和RNC应能进行响应处理。可基于容量比例、RNC/BSC、IMSI范围和RAI使用Flex的负荷卸载功能。 
卸载过程中负荷卸载速率控制，通过打开SGSN负荷卸载优化，设置令牌控制周期，在控制周期内，UE主动活动卸载和周期扫描卸载数量超过门限，SGSN不再进行卸载，直到下个控制周期开始。 
## ZUF-77-06-003 优选COMBO节点 
特性描述 : 
术语 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
应用限制 
特性交互 
遵循标准 
特性能力 
可获得性 
O&M相关 
术语 : 
无 
描述 : 
定义
GnGp SGSN和MME采用COMBO局方式POOL组网，用户在SGSN和MME下跨RAT移动进行附着、TAU/RAU或切换、RIM业务、SUSPEND业务时，重新选择SGSN或MME时，尽量选择与原SGSN或MME处于同一COMBO节点的MME或SGSN，这样可以减少局间信令，降低业务时延，提高系统性能。
如图[图1]所示，用户首先附着在SGSN1下，当MS从RNC移动到eNodeB并发起TAU业务，此时eNodeB可以选择MME1或MME2，如选择到MME1，SGSN1和MME1为同一COMBO局，无需局间信令即可获得用户的上下文信息。
图1  SGSN/MME COMBO局POOL组网图
同样用户MS移动到eNodeB信号覆盖发起切换时，SGSN1选择目标网元，基于eNodeB ID进行DNS查询可得到MME1与MME2，此时SGSN1选择使用MME1则不需局间的GTP切换信令即可完成切换。
下表列举了不同的跨RAT业务场景下，不同的网元实现优选同一节点的具体方法： 
跨RAT业务场景|重选网元|优选方法
---|---|---
附着/RAU到SGSN|RNC/BSS|为MME规划和同一COMBO节点的SGSN的NRI相关联的MME Code，使得GUTI映射的P-TMSI中携带的NRI可以指向同节点的SGSN；
切换到SGSN|源MME|通过目标RNC ID的DNS解析SGSN地址时，优选与本网元相同的IP地址；
RIM到SGSN|源MME|判断目标RNC ID或CGI为本地配置，则直接转本节点SGSN下发；
SUSPEND到SGSN|BSS|为MME规划和同一COMBO节点的SGSN的NRI相关联的MME Code，使得GUTI映射的P-TMSI中携带同节点SGSN的NRI；
附着/TAU到MME|eNB|S1 SETUP RESPOND消息中携带同节点SGSN的LAI+NRI映射的GUMMEI，使得P-TMSI+RAI映射的GUTI中携带eNB已知的同节点的MMEID
切换到MME|源SGSN|通过目标RNC ID（映射eNB ID）的DNS解析MME地址时，优选与本网元相同的IP地址；
RIM到MME|源SGSN|判断目标eNB ID为本地配置，则直接转本节点MME下发；
背景知识
用户在2G/3G和LTE网络之间双向跨RAT移动时，UE需具有GUMMEI+MTMSI与PTMSI+RAI之间相互映射的能力，基于23.003协议映射的规则如下： 
MS从2G/3G移动到LTEMS在2G/3G网络附着后，SGSN为其分配PTMSI+RAI，此用户移动到LTE网络，MS需要基于之前的PTMSI+RAI映射得到GUMMEI+M-TMSI上报给MME，映射规则如下：eNodeB基于GUMMEI查找到MME发送消息，在新局MME中，MME采用以上反逻辑获得用户之前的PTMSI+RAI。 
MS从LTE移动到2G/3GMS在LTE网络附着后，MME为其分配GUMMEI+MTMSI，此用户移动到2G/3G网络，MS需要基于之前的GUMMEI+MTMSI映射得到PTMSI+RAI上报给SGSN，映射规则如下：RNC使用P-TMSI中的NRI查找到SGSN，在新局SGSN中，SGSN采用以上反逻辑获得用户之前的GUMMEI+MTMSI。 
应用场景 : 
SGSN MME融合POOL组网，即POOL内的所有节点，都是SGSN MME COMBO节点。 
客户收益 : 
受益方|受益描述
---|---
运营商|本功能可以减少SGSN与MME之间局间信令，提高系统性能。
移动用户|对终端用户不可见
实现原理 : 
系统架构
无 
涉及的网元
本功能需要SGSN和MME网元完成。 
MME：控制面功能实体，临时存储用户数据的服务器，负责管理和存储UE
相关信息，比如UE/用户 标识，移动性管理状态，用户安全参数等，为用户分配临时标识，当UE驻扎在该跟踪区域或者该网络时负责对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM，GPRS Mobility Management）上下文和分组数据协议（PDP，Packet
Data Protocol）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。在切换过程中负责切换流程的信令处理，建立或者删除和RNC的无线承载，通知GGSN更新PDP上下文信息。
本功能中，MME的功能为： 
在S1 SETUP RESPOND和MME CONFIGURATION UPDATE消息携带其同一COMBO节点的 SGSN中LAI+NRI映射的GUMMEI通知eNodeB。以便当用户从2G/3G移动到LTE时，eNodeB能够选择回到同一COMBO节点。 
4G3G切换业务，MME通过RNC ID进行DNS解析获得多个SGSN的IP地址，MME从中选择与本网元配置相同的IP地址。 
4G2/3G RIM业务，MME收到eNB DIRECT INFORMATION TRANSFER 消息，从中获得
RNC ID或CGI，判断其是否为本地配置。如为本地配置，则无需进行DNS解析直接转交本节点的SGSN处理，由本节点的SGSN，下发RIM消息到RNC/BSS。 
SGSN的功能为： 
3G4G切换业务，SGSN通过RNC ID（由eNB ID映射）进行DNS解析获得多个MME的IP地址，SGSN从中选择与本网元配置相同的IP地址。 
2/3G4G RIM业务，SGSN收到RIM消息中的目的地址为eNodeB ID和TAI，则检查eNodeB ID和TAI是否属于本地MME：如果属于本地MME，则无需进行DNS解析直接转交本节点的MME处理，由本节点的MME下发RIM消息到eNB。 
协议栈
无 
本网元实现
无 
业务流程
无 
系统影响 : 
本功能对系统能力无影响。 
应用限制 : 
无 
特性交互 : 
无 
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access
". 
3GPP TS 23.060: "General Packet Radio Service (GPRS); Service
description; Stage 2". 
3GPP TS 23.003: "Numbering, addressing and identification”. 
特性能力 : 
功能冲突
本功能如果与SGSN原有的“支持NRI标识重复处理”功能同时开启，则需要再同时开启“NRI标识重复优化”功能，增强对于NRI标识重复判断，避免将由MME
Code映射的NRI识别为池外与本局配置重复的NRI，而对用户发起卸载。 
组网要求
SGSN和MME混合组网下，应规划MME Group ID和LAC取值不同。 
SGSN需为POOL组网，同时NRI长度不大于8bit，如大于8bit则可能出现2个不同NRI映射后MME Code相同，无法区分。 
MME中MME Code映射为NRI后，此NRI在RNC配置上需指向其COMBO的SGSN。 
POOL内不同SGSN的NRI不能重复，由MME Code映射的NRI（MME Code的前Nbit，当NRI长度为N时）也要求与其他节点的SGSN的NRI不同，同时也与其他节点的MME
Code映射的NRI也不相同。 
可获得性 : 
版本要求及变更记录
无 
License要求
无 
对其他网元的要求
无 
工程规划要求
无 
O&M相关 : 
命令
配置项无 
安全变量无 
定时器无 
软件参数新增软件参数参见表3。表3  新增软件参数软件参数ID软件参数名称65600是否支持路由回Combo节点 
动态管理无 
性能统计
无 
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
配置特性 
调整特性 
测试用例 
常见问题处理 
配置特性 : 
配置说明
无 
配置前提
MME和eNodeB之间通讯正常。 
Combo局SGSN网元开启Pool功能。 
网络规划的MME Group ID和LAC不能有相同。 
本局其他GUMMEI配置的PLMN必须是在本局移动数据配置或本局其他HPLMN中已配置的PLMN。 
配置过程
网管打开软参是否支持路由回Combo节点(65600)
。
SGSN POOL配置及MME网元的基本配置。 
配置实例
COMBO局SGSN网元Pool组网： 
Combo网元1：PLMN=46000，MME
Group ID = 32768，MME Code = 4；SGSN的NRI长度为7bit，NRI取值为2，LAC = 0x0001、0x0002、0x0003；
Combo网元2：PLMN=46000，MME Group ID = 32768，MME Code = 6；SGSN的NRI长度为7bit，NRI取值为3，LAC
= 0x0001、0x0002、0x0003； 
网管打开功能控制软参 Command ScriptDescriptionSET SOFTWARE PARAMETER:PARAID=65600,PARAVALUE=12个网元均打开支持路由回Combo节点功能开关 
GUMMEI配置和NRI长度配置Command ScriptDescriptionSET COMBOCFG:MMEGROUPID=32768,MCC="460",MNC="00",MMECODE=4,
,FLEXEN="YES",NRILEN=7设置网元1的GUMMEI。设置网元1的SGSN Pool组网规划的NRI长度值为7SET COMBOCFG:MMEGROUPID=32768,MCC="460",MNC="00",MMECODE=6,
,FLEXEN="YES",NRILEN=7设置网元2的GUMMEI。设置网元2的SGSN Pool组网规划的NRI长度值为7 
设置的NRI值Command ScriptDescriptionADD FLEX NRI:NRI=2,NAME="SGSN1_NRI2"设置网元1的NRI值ADD FLEX NRI:NRI=3,NAME="SGSN1_NRI3"设置网元2的NRI值 
LAC配置Command ScriptDescriptionADD LAI:NAME="LAC01",MCC="460",MNC="00",LAC="0001"ADD LAI:NAME="LAC02",MCC="460",MNC="00",LAC="0002"ADD LAI:NAME="LAC03",MCC="460",MNC="00",LAC="0003"设置网元1和网元2的LAC配置。网络规划的MME Group ID和LAC不能有相同。 
调整特性 : 
无 
测试用例 : 
测试项目|MME支持多个GUMMEI
---|---
测试目的|验证Combo局的MME是否支持在S1Setup Response消息中携带多个GUMMEI
预置条件|1、MME和eNodeB间通讯正常；2、Combo局SGSN开启了Pool功能；3、网管配置了GUMMEI相关的配置；
测试过程|eNodeB接入到Combo局MME，发送S1Setup Request消息给MME；MME返回成功的S1 Setup Response消息，携带MME相关参数；
通过准则|检查S1 SetupResponse消息中携带的“Served GUMMEIs”中是否包括MME支持的GUMMEI以及根据SGSN配置的LAI+NRI映射的GUMMEI；检查S1 Setup Response消息中其他参数是否正确；
测试结果|无
测试项目|切换优选本Combo局
---|---
测试目的|验证切换优选本Combo局
预置条件|1、MME和eNodeB间通讯正常；2、Combo局SGSN开启了Pool功能；3、网管配置了GUMMEI相关的配置；
测试过程|1、LTE向UMTS切换，eNodeB发起切换，切往POOLSGSN下的RNC；
通过准则|1、MME选择本Combo局所在的SGSN进行切换处理
测试结果|无
常见问题处理 : 
新增一条本局其他GUMMEI配置，执行失败，提示“超过表最大容量”。 问题分析：本局其他GUMMEI配置最大只支持一条配置记录，如果已存在一条记录，只能在已有的记录上进行修改。 
功能控制开关打开，Combo局eNodeB接入时，MME在S1 Setup Response消息中只携带了MME支持的GUMMEI，未携带SGSN映射的GUMMEI。 
问题分析：Combo局MME携带SGSN映射的GUMMEI，前提条件是SGSN要开启Pool组网，检查SGSN是否开启了flex功能以及配置了NRI相关参数。
# ZUF-77-07 移动性限制 
概述 : 
功能描述 : 
由于用户业务特性或需求，或者运营商本地控制策略，需要针对用户接入进行限制，比如限制用户在某种接入类型（例如：WIFI接入、5G接入）下接入，或者限制用户在某个区域下接入。 
功能特性简介 : 
SGSN提供了多种接入限制策略，满足不同的接入限制需求。详细的解决方案特性见下表。 
方案特性|实现简述|特导链接
---|---|---
ARD限制|SGSN根据签约ARD信息和无线接入网类型决定是否接收用户的接入请求。2G用户可接入3G网络而仍可继续使用SIM卡和MSISDN/IMSI号码。运营商可灵活控制2G/3G接入权限。|ZUF-77-07-001 ARD限制
ODB限制|网络运营商或业务提供者通过异常处理程序调节用户接入业务（面向电路域和分组域），限制某些入局呼叫或出局呼叫或分组数据业务，或限制漫游。ODB可立即生效，并能终止正在进行的呼叫和限制后续呼叫或分组数据业务。凭借HLR中的ODB用户数据，本功能可拒绝欲注册用户的业务。|ZUF-77-07-002 ODB限制
Zone Code限制|SGSN支持按IMSI号段，将不同的区域限制代码配置为来自HLR的相同区域代码。SGSN提供默认的区域限制代码，对于没有区域限制代码配置的IMSI号段，SGSN设置默认配置。如果由于区号限制而拒绝用户接入，则可以配置故障原因。|ZUF-77-07-003 Zone Code限制
本地区域限制|SGSN支持基于IMSI/MSISDN号段进行区域限制。IMSI/MSISDN号段用于区别本地用户和其他PLMN的用户。SGSN可配置如下区域限制策略：IMSI/MSISDN号段LAI/RAI接入模式运营商可选择是否限制归属用户或漫游用户接入某些路由区。例如，限制只签约了2G漫游协议的漫游用户接入3G网络。|ZUF-77-07-004 本地区域限制
## ZUF-77-07-001 ARD限制 
概述 : 
在开始部署3G网络时，需要使用标志来区分2G用户和3G用户。运营商可控制2G用户和3G用户接入2G网络和3G网络的权限。 
收益 : 
运营商： 
运营商可灵活控制2G/3G接入权限。 
用户： 
2G用户可接入3G网络而仍可继续使用SIM卡和MSISDN/IMSI号码。另外，运营商可通过该特性控制3G用户接入2G网络的权限。 
SGSN应能根据从HLR获取的签约信息支持ARD控制。 
描述 : 
ARD信令流程如下： 
HLR添加ARD标签用于控制用户的接入权限，并管理ARD的签约信息。 
ARD信息通过扩展MAP ISD消息从HLR传送给VLR。 
SGSN根据ARD信息和无线接入网类型决定是否接收用户的接入请求。 
当SGSN根据ARD拒绝用户的接入请求时，SGSN须提供适当的释放原因。 
可从下表中选取ARD的值。 
结果|ARD含义|ARD值|无线接入网|场景
---|---|---|---|---
拒绝|GREAN允许/UTRAN不允许|01|3G UTRAN|2G用户接入3G网络
接受|GREAN允许/UTRAN允许|00|3G UTRAN|3G用户接入3G网络
接受|GREAN允许/UTRAN不允许|01|2G BSS|2G用户接入2G网络
接受|GREAN允许/UTRAN允许|00|2G BSS|3G用户接入2G网络
## ZUF-77-07-002 ODB限制 
概述 : 
本特性允许网络运营商或业务提供者通过异常处理程序调节用户接入业务（面向电路域和分组域），限制某些入局呼叫或出局呼叫或分组数据业务，或限制漫游。ODB可立即生效，并能终止正在进行的呼叫和限制后续呼叫或分组数据业务。 
收益 : 
凭借HLR中的ODB用户数据，本功能可拒绝欲注册用户的业务。 
描述 : 
业务提供者通过非标准接口与HLR的管理互动控制ODB应用。 
当漫游限制发生异常，通过激活呼叫限制补充业务，HLR以类似业务提供者的方式影响ODB。因此，SGSN也以相似的方式执行相关限制条件。值得注意的是没有使用密码。当MS位于其他PLMN而不是在归属PLMN或不在归属PLMN国家时，如果适用的话，HLR禁止该MS的漫游。 
除了确保后续呼叫限制，在应用ODB业务之前，HLR和SGSN须提供措施终止用户仍在进行的呼叫。 
如下列分类所述，业务提供者可能在任何时候激活本特性，能终止任何正在进行的呼叫（包括前转的呼叫），并通过下列限制分类限制后续呼叫： 
闭锁所有出局呼叫 
闭锁所有国际出局呼叫 
禁止所有除归属国PLMN外的国际出局呼叫 
闭锁所有区域间出局呼叫 
闭锁所有除归属国PLMN外的区域间出局呼叫 
闭锁所有除归属国PLMN外的国际出局呼叫以及闭锁所有区域间出局呼叫 
闭锁指定归属PLMN的移动始呼短消息—当移动台在其归属PLMN注册，并且属于下列任意一个或多个类型时： 
运营商决定的闭锁（类型1） 
运营商决定的闭锁（类型2） 
运营商决定的闭锁（类型3） 
运营商决定的闭锁（类型4） 
闭锁所有入局呼叫或移动终呼短消息 
闭锁所有面向分组的业务 
当用户在拜访PLMN漫游时，闭锁从归属PLMN内接入点接入的分组数据业务 
闭锁从拜访PLMN内接入点接入的分组数据业务 
## ZUF-77-07-003 Zone Code限制 
概述 : 
此功能允许根据不同的IMSI范围将不同的区域限制代码配置为来自HLR的相同区域代码。 
收益 : 
操作员可以将不同的区域限制代码配置为来自HLR的相同区域代码。 
描述 : 
Attach Request和Attach Accept的消息用于用户Attach，Attach Accept消息作为对附加Attach Request的回复发送。路由区域更新请求、路由区域更新接受和路由区域更新完成消息用于更新订阅的RA。 
基于不同的IMSI范围，可以在SGSN中配置从HLR到相同区域代码的不同区域限制代码。 
如果订阅者订阅区域代码，SGSN会根据不同的IMSI范围检查区域限制代码。SGSN提供默认的区域限制代码，对于没有区域限制代码配置的IMSI范围，SGSN设置默认配置。 
如果由于区号限制而拒绝订阅者，则可以配置故障原因。 
## ZUF-77-07-004 本地区域限制 
概述 : 
SGSN支持基于IMSI/MSISDN号段进行区域限制。IMSI/MSISDN号段用于区别本地用户和其他PLMN的用户。 
SGSN可配置如下区域限制策略： 
IMSI/MSISDN号段 
LAI/RAI 
接入模式 
IMSI/MSISDN号段策略用于限制号段范围，最多支持4096个IMSI/MSISDN号段。LAI/RAI策略用于限制IMSI/MSISDN号段的路由区。接入模式策略用于限制IMSI/MSISDN号段范围的2G接入或3G接入。 
SGSN发送3GPP 24.008协议所定义的原因码给用户用于区域限制。 
收益 : 
运营商可选择是否限制归属用户或漫游用户接入某些路由区。例如，限制只签约了2G漫游协议的漫游用户接入3G网络。 
描述 : 
SGSN可为基于IMSI/MSISDN号段分类的用户部署不同的路由区限制策略，并向不同的路由区发送不同的错误原因。IMSI/MSISDN号段可以是MCC+MNC或更详细的号码串。当MS来到禁止接入的路由区时（该MS的IMSI/MSISDN所在的IMSI/MSISDN号段禁止接入当前路由区），SGSN发送Attach Reject消息或Route Area Update Reject消息给MS，该消息携带配置的错误原因码。 
# ZUF-77-08 UE能力管理 
概述 : 
功能描述 : 
UE能力包括UE无线能力和UE网络能力。 
SGSN保存UE无线能力，并提供给RAN，避免RAN在从空闲态向连接态转换时向UE申请UE无线能力信息，节省空口资源。 
SGSN保存UE网络能力，并基于UE网络能力做差异化处理。 
功能特性简介 : 
针对用户的各种能力信息，核心网提供了多种有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
UE无线能力处理|终端在附着或RAU时，携带终端能力信息，SGSN保存这些信息，并且在切换过程中传递给新的目标局。UE的能力信息包括：MS无线接入能力、MS网络能力和UE网络能力。|ZUF-77-08-001 UE无线能力处理
UE核心网能力|UE的网络能力参数包括非无线能力参数，如GSM GPRS加密、UMTS鉴权和TI扩展能力。SGSN保存和处理UE的网络能力信息，并在UE移动时发送该信息给新的SGSN或MME。|ZUF-77-08-002 UE核心网能力
DRX参数处理|DRX参数用于指示MS是否使用DRX模式。MS应在附着过程中指示DRX参数。SGSN发送携带DRX参数的寻呼消息给BSS。BSS使用这些参数和IMSI计算正确的寻呼群。|ZUF-77-08-003 DRX参数处理
## ZUF-77-08-001 UE无线能力处理 
概述 : 
SGSN可保存和传送UE的无线能力信息。 
收益 : 
当UE移动到新MME/SGSN时，新MME/SGSN可通过该功能获取UE的无线能力信息。 
描述 : 
UE在附着或RAU流程中携带其能力信息。SGSN保存该信息，并在切换过程中发送给新的目标局。 
UE的能力信息包括：MS无线接入能力、MS网络能力和UE网络能力。 
## ZUF-77-08-002 UE核心网能力 
概述 : 
SGSN可处理和传输UE的网络能力信息。 
收益 : 
当UE移动到新的MME/SGSN时，新MME/SGSN可通过该功能获取UE的网络能力信息。 
描述 : 
UE的网络能力参数包括非无线能力参数，如GSM GPRS加密、UMTS鉴权和TI扩展能力。SGSN保存和处理UE的网络能力信息，并在UE移动时发送该信息给新的SGSN或MME。 
## ZUF-77-08-003 DRX参数处理 
概述 : 
DRX参数用于指示MS是否使用DRX模式。 
收益 : 
MS在附着过程中指示DRX参数，SGSN发送携带DRX参数的寻呼消息给BSS。BSS使用这些参数和IMSI计算正确的寻呼群。 
描述 : 
DRX参数用于指示MS是否使用DRX模式， 
MS应在附着过程中指示DRX参数。SGSN发送携带DRX参数的寻呼消息给BSS。BSS使用这些参数和IMSI计算正确的寻呼群。 
在A/Gb和Iu模式下，DRX参数为GERAN和UTRAN还有可能其他RAT（如E-UTRAN）携带有关DRX周期长度的信息。 
在A/Gb模式下，MS可能使用不连续接收（DRX）功能。如果使用DRX，MS应能指定其他DRX参数。这些参数指示网络发送寻呼请求（paging
request）或信道指派（channel assignment）消息给MS的时延。 
# ZUF-77-09 移动管理扩展功能 
概述 : 
功能描述 : 
扩展移动性管理，可以解决如下移动性诉求： 
向接入用户下发时区和网络信息 
一号多卡 
RAN间配置信息传递 
提高寻呼效率 
多PLMN支持 
功能特性简介 : 
SGSN提供了多种解决方案，满足不同的移动性管理扩展功能。具体特性如下。 
方案特性|实现简述|特导链接
---|---|---
RIM|RIM流程提供了一种RAN节点之间通过MME节点交互专有应用信息的通用机制。RAN节点应用信息封装在RIM容器(RIM container)中，MME能够将RAN信息通过接口消息从源RAN节点透传到目的RAN节点而无需解析。源/目的RAN节点包括：GERAN，UTRAN，E-UTRAN。|ZUF-77-09-001 RIM
智能寻呼|通过灵活寻呼策略，SGSN可适应各种网络情况，从而提高寻呼成功率。SGSN的智能寻呼策略包括寻呼次数、寻呼间隔、寻呼模式和寻呼范围等因素。寻呼模式包括：IMSI寻呼P-TMSI寻呼寻呼范围包括：全SGSN寻呼当前激活的RAI当前激活的BVC（仅适用于Gb接口接入模式）当前激活的LAI当前激活的多LAI|ZUF-77-09-002 智能寻呼
多PLMN|SGSN可配置有多个运营网络的国家码和网号。SGSN可接入这些已配置的网络，并进行相关业务。同时，用户的路由区信息能清晰指示用户接入的网络。根据该信息，系统可在位于不同接入网的设备上进行不同的接入控制和费率控制。同时，通过区域限制，SGSN可更好地进行用户管理。这些为多模式接入、统一核心网和多业务管理提供可行的管理策略。|ZUF-77-09-003 多PLMN
EPLMN|SGSN支持基于IMSI号段的EPLMN列表。SGSN可根据IMSI号段发送不同的EPLMN列表给不同的用户。最多可配置6个IMSI号段，每个IMSI号段最多可配置15个EPLMN。|ZUF-77-09-004 对等PLMN
多SIM|对于多SIM功能，用户有两种MSISDN：常用MSISDN和个人MSISDN。这两类MSISDN保存在HLR上。当HLR将用户数据插入SGSN的过程中，SGSN保存这两种MSISDN。SGSN为短信始呼业务使用常用MSISDN。SGSN通过专用消息格式向通过Gn接口向GGSN提供常用MSISDN和个人MSISDN。但是GGSN只提供常用MSISDN给Radius服务器或WAPGW。只有个人MSISDN被写入由SGSN和GGSN生成的话单中。计费中心将个人MSISDN映射到常用MSISDN，以便将处理过的话单发布给用户。另外，常用MSISDN和个人MSISDN之间的关系以及相关的用户信息可通过SGSN或GGSN的UME客户端查询。|ZUF-77-09-005 多SIM
Supper Charge|Supper Charge特性提供了一种机制，可在VLR和SGSN之间进行用户位置更新时减少移动相关的信令业务量。如果网络支持Supper Charge，当用户从一个网络实体漫游到另一个网络实体时，前一个网络实体仍保留该用户相关的签约信息。网络实体指的是MSC/VLR或SGSN。|ZUF-77-09-006 Supper Charge
IMEI检查增强|当在UE接入过程中检查IMEI时，MME发送携带有IMSI和MSISDN信息的IMEI检查请求（IMEI inspection request）给EIR，使EIR可检查IMEI和IMSI/MSISDN的绑定信息。|ZUF-77-09-008 IMEI检查增强
NITZ|NITZ为网络标识和时区总称，当终端注册到SGSN后，SGSN根据运营商策略向终端更新NI和/或TZ信息。|ZUF-77-09-008 NITZ
## ZUF-77-09-001 RIM 
特性描述 : 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
应用限制 
遵循标准 
可获得性 
O&M相关 
描述 : 
定义
RAN信息管理（RAN Information Relay，下面简称RIM）流程提供了一种RAN节点之间通过核心网的SGSN/MME节点交互专有应用信息的通用机制。 
RAN节点应用信息封装在“RIM容器”(RIM container)中，方便核心网（SGSN/MME）能够将RAN信息通过接口消息从源RAN节点透传到目的RAN节点而无需解析。源/目的RAN节点包括：GERAN，UTRAN，E-UTRAN。 
RIM流程涉及的接口包括：Gb(BSSGP)，Iu(RANAP)，S1(S1AP)，Gn(GTPv1)，S3(GTPv2)。 
RIM流程包括寻址、路由和转发三部分内容：寻址：用于标识RAN节点的地址，BSS的寻址标识是CGI（RAI+CI），RNC的寻址标识是Global RNC-Id，eNodeB的寻址标识是eNodeB
Identifier。 
路由：源RAN节点通过对应的接口发送消息到归属的SGSN/MME，同时携带源/目的RAN节点地址；SGSN/MME节点（本文一般也称作中间节点）基于目的RAN地址解析出RAN节点归属的SGSN/MME，并通过Gn/S3口GTP消息发送到对应的SGSN/MME；目的RAN节点归属的SGSN/MME根据目的地址找到正确的目的RAN节点并发送下去。 
转发：SGSN/MME在路由过程中需要在不同的接口协议之间进行转换，包括BSSGP，RANAP，GTP，S1AP，这一过程称为转发。 
本文中为了描述方便，源RAN节点归属的SGSN/MME，一般称作源侧中间节点（或者源侧SGSN/MME节点），目的RAN节点归属的SGSN/MME，一般称作目的侧中间节点（或者目的侧SGSN/MME节点）。 
如果源RAN节点和目的RAN节点归属同一个SGSN/MME（或者同一个Combo局中的SGSN和MME），那么源侧和目的侧的中间节点就是同一个中间节点，为了描述方便，有的时候也会描述为源侧中间节点和目的侧中间节点，具体情况可根据语境（描述时的上下文）判断。 
背景知识
GPRS网络架构图如[图1]所示。
图1  GPRS架构图
TE/MT：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。
BSS：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。
UTRAN：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。
HLR：永久存储用户签约数据。
PDN：为用户提供业务的网络。
CGF：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。
BS：负责接收和处理从核心网发送过来的CDR文件。
EIR：负责检查UE设备。
PSCN：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元：
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM）上下文和分组数据协议（PDP）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息。 
GGSN：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务。包含如下网元： 
MSC/VLR：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMSGMSC/SMS IWMSC：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL：该功能实体主要对用户进行在线计费。 
EPS网络架构图如[图2]所示。
图2  EPS架构图
UE：为终端用户完成各种数据业务和其他业务的载体，负责存储UE 相关信息，完成无线资源管理功能，完成移动性管理功能，完成安全功能，完成承载管理功能。 
E-UTRAN：可以提供更高的上下行速率，更低的传输延迟和更加可靠的无线传输。E-UTRAN中包含的网元是eNodeB(Evolved NodeB)，为终端的接入提供无线资源。 
HSS：永久存储用户签约数据。 
PDN：为用户提供业务的网络。 
EPC：提供了更低的延迟，并允许更多的无线接入系统接入。包含了如下网元：MME：控制面功能实体，临时存储用户数据的服务器，负责管理和存储UE 相关信息，比如UE/用户 标识，移动性管理状态，用户安全参数等，为用户分配临时标识，当UE驻扎在该跟踪区域或者该网络时负责对该用户进行鉴权，处理MME和UE之间的所有非接入层消息。Serving GW：用户面实体，负责用户面数据路由处理，终结处于空闲状态的UE（用户终端设备）的下行数据。管理和存储UE的承载（Bearer）信息，比如IP承载业务参数和网络内部路由信息等。PDN GW：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP和非3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个PDN
GW。 
PCRF：该功能实体主要根据业务信息和用户签约信息以及运营商的配置信息产生控制用户数据传递的QoS规则以及计费规则。该功能实体也可以控制接入网中承载的建立和释放。 
SGSN：临时存储用户数据的服务器，负责管理和存储UE相关信息，如UE/用户标识，移动性管理状态，用户安全参数等，为用户分配临时标识，完成用户安全功能，完成用户移动性管理功能和会话管理功能，处理SGSN和UE之间的所有非接入层消息。 
UTRAN：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。 
GERAN：GPRS/EDGE的无线接入网络，为终端的接入提供无线资源。 
应用场景 : 
RIM过程主要是应用于无线节点之间不支持切换，而又需要获取对端无线节点系统信息时一种辅助流程，比如NACC、SI3、MBMS data channel、SON
Transfer、UTRA SI（UTRA System Information）。
RIM功能主要服务于无线侧，核心网节点SGSN/MME作为中间路由节点需要支持RIM消息的路由和转发，且不关心其具体的无线侧的应用。 
SGSN/MME根据目的地址进行RIM消息的寻址、无状态路由及转发。 
RIM支持的无线节点包括：GERAN<->GERAN 
UTRAN<->UTRAN 
GERAN<->UTRAN 
GERAN<->E-UTRAN 
UTRAN<->E-UTRAN 
客户收益 : 
受益方|受益描述
---|---
运营商|优化无线资源，降低用户跨RAN移动带来的影响
移动终端用户|提升用户使用数据业务的体验
实现原理 : 
涉及的网元
RIM流程需要SGSN、MME、BSC、RNC、eNodeB共同配合。 
SGSN/MME：作为RIM流程的中间转发节点，主要负责RIM消息寻址、无状态路由及转发。 
BSC/RNC/eNodeB：作为RIM流程的源/目的RAN节点，将应用内容封装在RIM容器中，通过RIM流程，完成相关应用。 
业务流程
Gb口RIM流程图3  Gb口RIM流程Gb口RIM流程简要介绍如下：SGSN收到Gb口BSC发过来的BSSGP层的RIM消息，解析目的路由地址成功后，转换为对应接口的RIM消息后发往本局管理的目的RAN节点（比如：BSC、RNC，在Combo局还可能包含eNodeB），或者发往目的RAN节点归属的SGSN/MME。SGSN收到本局源RAN节点（比如：BSC、RNC，在Combo局还可能包含eNodeB）或者源中间节点SGSN/MME的RIM消息，解析目的路由地址为本局管理的CGI，转换为BSSGP层的RIM消息，发往目的BSC。BSSGP层的RIM消息包括：RAN-Information-Request、RAN-Information、RAN-Information-ACK、RAN-Information-ERROR、RAN-Information-APPLICATION-ERROR。透传的内容封装在RIM消息中的RIM Container中，对应RIM消息不同，其Contianer的内容也不一样，分别为：RAN-Information-Request RIM Container、RAN-Information RIM Container、RAN-Information-ACK RIM Container、RAN-Information-ERROR RIM Container、RAN-Information-APPLICATION-ERROR RIM Container。其他接口RIM中携带的RIM Container内容也是一样的。 
Iu口RIM流程图4  Iu口RIM流程Iu口RIM流程简要介绍如下：SGSN收到Iu口RNC发过来的RANAP层的RIM消息，解析目的路由地址成功后，转换为对应接口的RIM消息后发往本局管理的目的RAN节点（比如：BSC、RNC，在Combo局还可能包含eNodeB），或者发往目的RAN节点归属的SGSN/MME。SGSN收到本局源RAN节点（比如：BSC、RNC，在Combo局还可能包含eNodeB）或者源中间节点SGSN/MME的RIM消息，解析目的路由地址为本局管理的RNC-ID，转换为RANAP层的RIM消息，发往目的RNC。RANAP对应的RIM消息为DIRECT INFORMATION TRANSFER。 
S1口RIM流程图5  S1口RIM流程S1口RIM流程简要介绍如下：MME收到S1口eNodeB发过来的S1AP层的RIM消息，解析目的路由地址成功后，转换为对应接口的RIM消息后发往本局管理的目的RAN节点（比如：eNodeB，在Combo局还可能包含RNC或BSC），或者发往目的RAN节点归属的SGSN。MME收到本局源RAN节点（比如：eNodeB，在Combo局还可能包含RNC或BSC）或者源中间节点SGSN的RIM消息，解析目的路由地址为本局管理的eNodeB-ID，转换为S1AP层的RIM消息，发往目的eNodeB。S1AP层对应的RIM消息为：eNB DIRECT INFORMATION TRANSFER（eNB->MME），MME DIRECT INFORMATION TRANSFER（MME->eNB）。 
Gn口RIM流程图6  MME Gn口RIM流程MME Gn口RIM流程简要介绍如下：MME将S1口收到的RIM消息通过Gn口GTPv1的RIM消息发往SGSN。MME收到Gn口的GTPv1 RIM消息，解析目的路由地址为本局管理的RAN节点，转换为对应接口的RIM消息发往目的RAN节点。对应的GTPv1的RIM消息为RAN Information Relay。图7  SGSN Gn口RIM流程SGSN Gn口RIM流程简要介绍如下。SGSN将本局管理的RAN节点收到的RIM消息通过Gn口GTPv1的RIM消息发往目标侧的SGSN/MME。SGSN收到Gn口的GTPv1 RIM消息，解析目的路由地址为本局管理的RAN节点，转换为对应接口的RIM消息发往目的RAN节点。对应的GTPv1的RIM消息为RAN Information Relay。 
系统影响 : 
RIM消息在SGSN/MME内部是用户无关的消息，一般无法根据用户标识（比如，IMSI、TEID、PTMSI+RAI等）进行负荷分担，而是通过局向链路/随机/轮询等保证系统内部的负荷分担均衡。 
RIM消息属于SGSN/MME无状态转发的消息，当无线侧触发的RIM消息量比较大的时候，MME/SGSN转发这些消息会加重系统的负荷，目前SGSN/MME没有对这类消息进行负荷控制，外场如果开启RIM功能，需要先向无线侧了解RIM的话务模型（RIM功能主控在无线侧，SGSN/MME无法给出对应话务模型），并根据下述性能影响进行合理评估，下面是实验室稳定环境下的测试结果，实际情况不保证完全一样，话务模型供参考。 
根据本版本的实测结果，每模块每秒平均转发150条RIM消息，将会使CPU消耗增加1%，一般消息量与CPU消息呈线性比例关系。 
举例：SGSN有10个模块，根据无线话务模型及无线基站数量得出经由SGSN转发的RIM消息数（需要包括来回双向）约为10000条/秒，那么会使得SGSN的CPU平均消耗增加10000/10/150≈6.7%。 
业务流程影响：Gb口RIM流程在BVC链路建立时进行了协商，BSC或者SGSN支持RIM功能开关发生改变，无法立即生效，只有通过以后BSC或SGSN主动发起的信令BVC
Reset过程才能生效。
应用限制 : 
无 
遵循标准 : 
3GPP TS 23.003: "Numbering, addressing and identification". 
3GPP TS 23.060: "General Packet Radio Service (GPRS); Service
description; Stage 1". 
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 29.060: "General Packet Radio Service (GPRS); GPRS
Tunnelling Protocol(GTP) across the Gn and Gp Interface". 
3GPP TS 29.274: "3GPP Evolved Packet System; Evolved GPRS Tunnelling
Protocol (eGTP) for EPS; Stage 3". 
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network
(E-UTRAN); S1 Application Protocol (S1AP)". 
3GPP TS 48.018: "General Packet Radio Service (GPRS); Base
Station System (BSS) - Serving GPRS Support Node (SGSN); BSS GPRS
Protocol (BSSGP)". 
可获得性 : 
License要求
无 
对其他网元的要求
RIM流程需要BSC、RNC、eNodeB主导，SGSN/MME配合完成。 
其中，BSC需要支持Gb口的RIM消息的收发及解析，RNC需要支持Iu口的RIM消息的收发及解析，eNodeB需要支持S1口的RIM消息的收发及解析。 
O&M相关 : 
命令
配置项无 
安全变量无 
软件参数新增软件参数参见表2。表2  新增软件参数软件参数ID软件参数名称65569SGSN根据该变量判断是否需要支持基于标准的RIM消息中的eNB ID的解析，包括Gb口、Iu口。65617MME根据该变量判断是否需要支持基于标准的RIM消息中的RNC ID的解析，包括S1口。65619SGSN根据该变量判是否支持基于标准的RIM消息中的eNB ID构造FQDN，如果不支持将使用TAI构造。262283MME RIM流程在解析对端SGSN IP地址时，构造FQDN使用的方式。65542SGSN的RIM功能开关。 
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
RIM相关测量|编号为C40553开头的所有计数器
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
配置特性 
测试用例 
常见问题处理 
配置特性 : 
配置前提
MME或Combo局前后台连通，PPB板、后插卡等均已正常上电。网管客户端和服务器间能够正常通信。 
配置过程
SGSN解析配置 
执行命令[ADD SGSNHOST]，配置到局间BSC/RNC的解析。
 说明： 
如果ID为262279
的软件参数“新局SGSN获取老局SGSN地址时的域名格式”为EPS时，执行命令[ADD EPCHOST]进行配置解析，解析的逻辑名形式为racXXXX.lacYYYY.rac.epc.mncZZZ.mccWWW.3gppnetwork.org或rncXXXX.rnc.epc.mncZZZ.mccWWW.3gppnetwork.org。
执行命令[ADD EPCHOST]，配置到eNodeB的解析。
（可选）执行命令[ADD HOST SUBNET PRI]配置解析地址优先级，该命令可用于配置不同子网段的优先级。
MME解析配置 
执行命令[ADD EPCHOST]，增加到SGSN的解析。
 说明： 
如果ID为262283
的软件参数“MME RIM流程获取目标SGSN
IP时采用的域名格式”为PS时，执行命令[ADD SGSNHOST]进行解析配置，配置的逻辑名格式为racXXXX.lacYYYY.
mncZZZ.mccWWW.gprs或rncXXXX.mncZZZ.mccWWW.gprs。
配置实例
2G/3G到4G的RIM配置脚本说明SET SOFTWARE PARAMETER:PARAID=65542,PARAVALUE=1;配置Combo 1局SGSN开启RIM功能，默认该功能关闭。SET SOFTWARE PARAMETER:PARAID=65569,PARAVALUE=3;配置Combo 1局SGSN支持2G/3G到4G的RIM流程，默认不支持。SET SOFTWARE PARAMETER:PARAID=65619,PARAVALUE=1;配置Combo 1局到Combo 2局MME的局间解析使用eNB ID构造FQDN，默认使用TAI构造FQDN。ADD  EPCHOST:NAME="enb10025.enb.epc.mnc001.mcc460.3gppnetwork.org",SERVICE="x-3gpp-mme",HOST="combo2",IPADDR="192.168.100.2",PROTOCOL="x-gn"&"x-gp";在Combo 1局配置到Combo 2局MME的本地DNS解析。 
4G到2G/3G的RIM配置脚本说明SET SOFTWARE PARAMETER:PARAID=65617,PARAVALUE=1;配置Combo 1局MME支持RIM流程RNC ID的解析，默认不支持。SET SOFTWARE PARAMETER:PARAID=262283,PARAVALUE=1;配置Combo 1局MME RIM流程使用EPS格式解析获取对端SGSN地址，默认即使用EPS格式解析。本例中若该值没有改变，检查确认即可。SET SOFTWARE PARAMETER:PARAID=65542,PARAVALUE=1;配置Combo 2局SGSN开启RIM功能，默认该功能关闭。ADD  EPCHOST:NAME="rnc0059.rnc.epc.mnc003.mcc460.3gppnetwork.org",SERVICE="x-3gpp-sgsn",HOST="combo2",IPADDR="192.20.100.2",PROTOCOL="x-gn"&"x-gp";在Combo 1局配置到Combo 2局SGSN的本地DNS解析。 
测试用例 : 
无 
常见问题处理 : 
无 
## ZUF-77-09-002 智能寻呼 
概述 : 
SGSN支持向UE发起多次寻呼尝试，并可配置寻呼次数、寻呼间隔、寻呼模式和寻呼范围。  
收益 : 
通过灵活寻呼策略，SGSN可适应各种网络情况，从而提高寻呼成功率。 
描述 : 
SGSN的智能寻呼策略包括寻呼次数、寻呼间隔、寻呼模式和寻呼范围等因素。 
寻呼模式包括： 
IMSI寻呼 
P-TMSI寻呼 
寻呼范围包括： 
全SGSN寻呼 
当前激活的RAI 
当前激活的BVC（仅适用于Gb接口接入模式） 
当前激活的LAI 
当前激活的多LAI 
## ZUF-77-09-003 多PLMN 
概述 : 
一套SGSN设备可用于管理有不同网络标识（即MCC和MNC不同）的RNS系统和BSS系统，并提供一样的分组业务。 
收益 : 
运营商可使用一套SGSN设备管理具有不同网络标识的RNS/BSS接入，为用户量小且分散的跨国运营商提供便利。如果跨国运营商在两个相邻的小国运营网络，该运营商可使用一套SGSN设备提供分组业务，从而降低投资和运营成本。 
本特性也有利于2G和3G网络的混合运营。2G网络和3G网络的无线接入差别很大。2G和3G网络网号不同。两个网络可使用同一套分组核心网，为不同网号采用不同的操作和维护策略，为具有不同特性的两个网络提供最佳管理。  
描述 : 
SGSN可配置有多个运营网络的国家码和网号。SGSN可接入这些已配置的网络，并进行相关业务。同时，用户的路由区信息能清晰指示用户接入的网络。根据该信息，系统可在位于不同接入网的设备上进行不同的接入控制和费率控制。同时，通过区域限制，SGSN可更好地进行用户管理。这些为多模式接入、统一核心网和多业务管理提供可行的管理策略。 
## ZUF-77-09-004 对等PLMN 
概述 : 
SGSN支持基于IMSI号段的EPLMN列表。SGSN可根据IMSI号段发送不同的EPLMN列表给不同的用户。
收益 : 
运营商可向不同IMSI号段的用户发送不同EPLMN列表，从而使运营商，尤其是MVNO，可更加灵活地选择PLMN。 
描述 : 
在成功附着或路由区更新过程中，可基于3GPP协议通知移动终端等效PLMN信息。 
可基于IMSI号段在SGSN上配置等效PLMN。当移动用户附着到该SGSN或通过路由区更新到该SGSN时，可以选择相应的EPLMN列表，并将列表发送给用户设备。 
## ZUF-77-09-005 多SIM 
概述 : 
SGSN支持多SIM功能。如果该特性被使能，多个使用常用MSISDN的MS可被激活并同时使用PS业务。否则，只有一个使用常用MSISDN的MS可以被激活并使用PS业务，而禁止激活其他MS。 
收益 : 
运营商可为用户部署定制业务。例如，用户可以同时在不同设备上使用多个SIM卡，但是只使用一个MSISDN。一组用户也可作为一个家庭或公司团队共享一个MSISDN号码，并通过这个号码进行联系。在一些PS业务中，MSISDN发挥重要作用。例如： 
WAP门户：门户应用为每个MSISDN创建多个配置文件用于提供定制内容。 
应用（如号码簿，消息备份和MSN)：大部分应用使用MSISDN作为登录名。  
推送邮件：邮件服务器可将常用MSISDN的邮件推送给最后登录的移动台。 
描述 : 
对于多SIM功能，MS有两种MSISDN：常用MSISDN和个人MSISDN。这两类MSISDN保存在HLR上。当HLR将用户数据插入SGSN的过程中，SGSN保存这两种MSISDN。SGSN为短信始呼业务使用常用MSISDN。SGSN通过专用消息格式向通过Gn接口向GGSN提供常用MSISDN和个人MSISDN。但是GGSN只提供常用MSISDN给Radius服务器或WAPGW。 
只有个人MSISDN被写入由SGSN和GGSN生成的话单中。计费中心将个人MSISDN映射到常用MSISDN，以便将合并话单发布给客户。 
另外，常用MSISDN和个人MSISDN之间的关系以及相关的用户信息可通过SGSN或GGSN的OMM客户端查询。  
## ZUF-77-09-006 Supper Charge 
概述 : 
Supper Charge特性提供了一种机制，可在VLR和SGSN之间进行用户位置更新时减少移动相关的信令业务量。 
收益 : 
本特性减少移动相关的信令业务量和网络负荷。 
描述 : 
如果网络支持Supper Charge，当用户从一个网络实体漫游到另一个网络实体时，前一个网络实体仍保留该用户相关的签约信息。网络实体指的是MSC/VLR或SGSN。 
## ZUF-77-09-008 IMEI检查增强 
概述 : 
当系统在UE接入过程中检查IMEI的同时，还检查IMEI和IMSI/MSISDN的绑定信息。 
收益 : 
防止克隆卡用户使用其他终端接入网络。 
当用户使用已挂失的终端接入网络时，可拒绝该用户接入并锁定该用户。 
可追踪异常情况，例如IMEI相同但IMSI/MSISDN不同，从而增强网络和终端的安全性和规范性。 
描述 : 
当在UE接入过程中检查IMEI时，MME发送携带有IMSI和MSISDN信息的IMEI检查请求（IMEI
inspection request）给EIR，使EIR可检查IMEI和IMSI/MSISDN的绑定信息。 
## ZUF-77-09-008 NITZ 
特性描述 : 
特性描述 : 
术语 : 
术语|含义
---|---
NI|Networks Identify网络标识，由运营商自由定义配置。
TZ|Time Zone时区，是地球上的区域使用同一个时间定义。1884年在华盛顿召开国际经度会议时，为了克服时间上的混乱，规定将全球划分为24个时区。
MOCN|Multi-Operator Core Network多运营商网络共享，即一套无线网络可以同时连接到多个运营商的核心网节点，实现多家运营商共享同一套无线网络。
描述 : 
定义 : 
NITZ为网络标识和时区总称，当终端注册到PS域后，SGSN根据运营商策略向终端更新NITZ信息。
背景知识 : 
NITZ是一种用于自动配置本地的时间和日期的机制，同时也通过无线网向移动设备提供运营商信息。NITZ是PHASE
2+ RELEASE 96 的GSM中的可选功能，经常被用来自动更新移动电话的系统时钟。 
网络标识用于通知终端当前接入网络的运营商标识，当运营商开启网络共享时可能存在不同运营商需要配置不同的网络标识。 
MOCN网络共享架构如[图1]所示。
图1  MOCN网络共享架构
应用场景 : 
NITZ功能可使运营商在各种网络架构下为终端提供准确的网络标识和时区信息。 
向用户提供更新时区或网络标识服务：开启NITZ功能, 配置下发网络标识、时区、网络时间策略。 
开启网络共享功能时不同运营商下发不同网络标识：根据不同的PLMN配置不同的NI和时区信息。 
网络跨越多个时区时下发正确的时区：针对不同的RA配置不同的时区。 
客户收益 : 
受益方|受益描述
---|---
运营商|方便运维管理：使用MOCN/GWCN时可以根本不同的PLMN、RA灵活配置不同的网络标识和时区信息。
用户|提升用户体验：当用户在不同的运营商、不同的时区或夏令时变化时可以及时更新为更准确的信息。
实现原理 : 
系统架构 : 
本特性的网络架构图如[图2]所示。
图2  网络架构图
涉及的网元 : 
本功能由SGSN和UE配合完成，不涉及其它网元。
网元名称|网元作用
---|---
SGSN|SGSN根据运营商策略决策是否向终端更新NITZ信息及何种格式是否使用夏令时时间等。
UE|终端接收更新NITZ的后，可选的更新本地信息。
协议栈 : 
Gb口协议栈如[图3]所示。
图3  Gb口协议栈
Iu口协议栈如[图4]所示。
图4  Iu口协议栈
本网元实现 : 
当终端注册到PS域后，SGSN根据运营商策略向终端更新NITZ信息，具体策略如下。 
SGSN可以基于以下策略控制是否下发NITZ信息给UE： 
IMSI号段+业务种类 
全局开关+业务种类 
业务种类控制包括： 
终端附着位置更新业务请求 
用户首次接入SGSN 
网络标识改变 
NI可以根据如下策略设置： 
用户IMSI中的PLMN 
用户选择的PLMN 
全局设置 
TZ可以根据如下策略设置： 
根据RA设置 
全局设置 
业务流程 : 
用户附着流程成功后NITZ流程
用户附着流程成功后NITZ流程如[图5]所示。
图5  附着流程后NITZ流程
用户UE向SGSN发起Attach请求。 
SGSN完成Attach业务处理并向UE发送Attach Accept。 
如果Attach Accept中携带了新的P-TMSI，用户UE接受新的P-TMSI，给SGSN返回Attach Complete消息。 
SGSN根据运营商策略决策是否需要下发NITZ, 如果需要则通过GMM Information消息携带NI和/或TZ。 
路由区更新成功后NITZ流程
路由区更新成功后NITZ流程如[图6]所示。
图6  路由区更新后的NITZ流程
用户UE向SGSN发起RAU请求。 
SGSN完成RAU业务处理并向UE发送RAU Accept。 
如果RAU Accept中携带了新的P-TMSI，用户UE接受新的P-TMSI，给SGSN返回RAU Complete消息。 
SGSN根据运营商策略决策是否需要下发NITZ, 如果需要则通过GMM Information消息携带NI和/或TZ。 
业务请求流程成功后NITZ流程
业务请求流程成功后NITZ流程如[图7]所示。
图7  业务请求后的NITZ流程
用户UE向SGSN发起业务请求。 
SGSN完成业务请求处理。 
SGSN根据运营商策略决策是否需要下发NITZ，如果需要则通过GMM Information消息携带NI和/或TZ。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
业务|交互
---|---
MOCN功能|当MOCN和NITZ功能同时开启时，如果需要为不同的运营商下发不同的NI可通过“基于PLMN的NI配置”设置。
遵循标准 : 
标准名称|章节
---|---
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;Core Network Protocols; Stage 3".|4.7.12
3GPP TS 23.060 "General Packet Radio Service （GPRS）; Servicedescription; Stage 2".|-
特性能力 : 
名称|指标
---|---
基于PLMN的NI配置|最大可配置16个PLMN
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|5.17.10|首次发布。
License要求 : 
该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为SGSN支持NITZ功能（license ID：7044），此项目显示为支持，表示支持NITZ功能。 
对其他网元的要求 : 
UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
√|-|-|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
本特性无工程规划要求。 
O&M相关 : 
命令 : 
新增配置项参见[表1]。
配置项|命令
---|---
全局数据配置|SHOW NITZ
SET NITZ|全局数据配置
SGSN基于IMSI号段的NITZ发送策略配置|ADD SGSN IMSI NITZ
SET SGSN IMSI NITZ|SGSN基于IMSI号段的NITZ发送策略配置
DEL SGSN IMSI NITZ|SGSN基于IMSI号段的NITZ发送策略配置
SHOW SGSN IMSI NITZ|SGSN基于IMSI号段的NITZ发送策略配置
基于PLMN的NI配置|ADD PLMN NI
SET PLMN NI|基于PLMN的NI配置
DEL PLMN NI|基于PLMN的NI配置
SHOW PLMN NI|基于PLMN的NI配置
修改配置项参见[表2]。
配置项|命令|新增参数
---|---|---
路由区配置|ADD RAI|增加两个参数"是否使用全局时区"和"时区"
性能统计 : 
新增性能计数器参见[表3]。
性能计数器名称
---
C405910001 发送GMM INFORMATION消息次数
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
通过配置“全局数据配置”下的NITZ，可以使运营商支持更新手机运营商标识和时区信息功能。
通过配置“全局数据配置”下的NITZ和“基于PLMN的NI配置”，可以使运营商在开启网络共享功能时，根据不同的PLMN配置不同的NI和时区。
通过配置“全局数据配置”下的NITZ和“路由区配置”，可以使运营商网络跨越多个时区时，针对不同的RA配置不同的时区。
配置前提 : 
SGSN支持NITZ功能的License已开启。
配置过程 : 
配置“全局数据配置”中NITZ信息。
当有不同的PLMN,且对应不同的NI时，配置“基于PLMN的NI配置”。
当网络下有不同时区时，根据规划配置“路由区配置”，不同RA设置相应TZ。
配置NITZ下发策略。 
配置实例 : 
###### 实例场景1 
实例场景1：通过NITZ功能来更新手机运营商标识和时区信息。 
如运营商网络的网络长标识为operator_len，网络短标识为operator，时区为默认的全局时区。 
配置步骤： 
步骤|命令|说明
---|---|---
1|SET NITZ:IFSENDNI="YES",SCENENI="REGIST",IFSENDTZ="YES",SCENETZ="REGIST",SENDTM="NO",ADDCNY="NO",LNAME="operator_len",LNAMECODE="BIT7",SNAME="operator",SNAMECODE="BIT7"|设置NITZ下发条件为“终端首次登记到网络”，及网络长标识和短标识。
2|SET TIMEZONE:TIMEZONE=GMTE0800|设置本网元的全局时区
###### 实例场景2 
实例场景2：开启NITZ功能，并且需要开启网络共享功能时，SGSN需要配置多个PLMN对应不同的NI。 
如PLMN为46001网络标识为ChinaUnicom，PLMN为46000的网络标识为CMCC，时区为默认的全局时区。 
配置步骤： 
步骤|命令|说明
---|---|---
1|SET NITZ:IFSENDNI="YES",SCENENI="REGIST"&"NMCHG",IFSENDTZ="YES",SCENETZ="REGIST"&"NMCHG",SENDTM="NO",ADDCNY="NO",LNAME="operator_len",LNAMECODE="BIT7",SNAME="operator",SNAMECODE="BIT7"|设置NITZ下发条件为“终端首次登记到网络”和“网络标识改变”，及网络长标识和短标识。
2|ADD PLMN NI:PLMN="460"-"01",FULLNISTR="ChinaUnicom"|设置PLMN为46001的网络标识为ChinaUnicom。
3|ADD PLMN NI:PLMN="460"-"00",FULLNISTR="CMCC"|设置PLMN为46000的网络标识为CMCC。
4|SET TIMEZONE:TIMEZONE=GMTE0800|设置本网元的全局时区。
###### 实例场景3 
实例场景3：运营商开启NITZ功能，网络覆盖不同时区时。 
如运营商网络下RA1对应的时区为"GMT+08:00"，RA2对应的时区为"GMT+08:15"。 
配置步骤： 
步骤|命令|说明
---|---|---
1|ADD RAI:NAME="RA1",LAI="LA1",RAC="01",GLOBALTZ="NO",TIMEZONE="GMT+08:00";ADDRAI:NAME="RA2",LA2="LA2",RAC="02",GLOBALTZ="NO",TIMEZONE="GMT+08:15"|设置RA1的时区为"GMT+08:00",设置RA2的时区为"GMT+08:15"。
2|SET NITZ:IFSENDNI="YES",SCENENI="REGIST"&"TMZONECHG",IFSENDTZ="YES",SCENETZ="REGIST"&"TMZONECHG",SENDTM="NO",ADDCNY="NO",LNAME="operator_len",LNAMECODE="BIT7",SNAME="operator",SNAMECODE="BIT7"|设置NITZ下发条件为“终端首次登记到网络”和“时区改变”，及网络长标识和短标识。
调整特性 : 
本特性暂不涉及调整参数。 
测试用例 : 
测试项目|配置首次接入下发NITZ
---|---
测试目的|验证配置首次接入时下发NITZ，用户IMSI Attach成功后下发NIZT正确
预置条件|SGSN支持NITZ功能license打开
测试过程|配置“终端首次登记到网络”下发NITZ用户发起IMSI Attach
通过准则|用户Attach成功SGSN下发GMM INFOMATION消息携带正确NITZ
测试结果|–
测试项目|不同PLMN下发不同NI.
---|---
测试目的|验证从不同PLMN接入时，可以下发不同的NI
预置条件|SGSN支持NITZ功能license打开
测试过程|配置“终端首次登记到网络”和“网络标识改变”下发NITZ用户1从PLMN1发起IMSI Attach用户2从PLMN2发起IMSI Attach
通过准则|用户Attach成功用户1收到的NI为PLMN1对应的NI用户2收到的NI为PLMN2对应的NI
测试结果|–
测试项目|支持不同RA下配置不同TZ.
---|---
测试目的|验证用户在不同RA下移动时，如果时区改变可以通知终端更新时区
预置条件|SGSN支持NITZ功能license打开，RA1对应时区为TZ1, RA2对应时区为TZ2
测试过程|用户在RA1下发起IMSI Attach用户移动到RA2下并发起RAU
通过准则|用户Attach成功，SGSN下发的时区为TZ1用户RAU功能，SGSN下发的时区为TZ2
测试结果|–
常见问题处理 : 
无常见问题处理 
# 缩略语 
# 缩略语 
## BS 
Billing System计费系统
## BSS 
Base Station Subsystem基站子系统
## CAMEL 
Customized Applications for Mobile Network Enhanced Logic移动网络增强逻辑的客户化应用
## CGF 
Charging
Gateway Function 计费网关功能
## CN 
Core Network核心网
E-UTRAN : 
Evolved Universal Terrestrial Radio Access Network演进的通用陆地无线接入网络
EIR : 
Equipment Identity Register设备标识寄存器
EPC : 
Evolved Packet Core演进的分组核心网
## EPLMN 
Equivalent Public Land Mobile Network对等公用陆地移动网
## GERAN 
GSM/EDGE Radio Access NetworkGSM/EDGE无线接入网
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
## GMM 
GPRS Mobile ManagementGPRS 移动性管理
## GMSC 
Gateway Mobile Switching Center网关移动交换中心
HLR : 
Home Location Register归属位置寄存器
HSS : 
Home Subscriber Server归属用户服务器
## IWMSC 
Interworking Mobile Switching Center网间移动交换中心
MME : 
Mobility Management Entity移动管理实体
## MOCN 
Multi-Operator Core Network多运营商核心网
MSC : 
Mobile Switching Center移动交换中心
## MT 
Mobile Terminal移动终端
## NACC 
Network Assisted Cell Change网络辅助小区式切换
## NITZ 
Network Identity and Time Zone网络标志和时区
PCRF : 
Policy and Charging Rules Function策略和计费规则功能
PDN : 
Packet Data Network分组数据网
PDP : 
Packet Data Protocol分组数据协议
## PS 
Packet Switched分组交换
QoS : 
Quality of Service服务质量
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
## SI3 
System Information 3系统信息3
SMS : 
Short Message Service短消息业务
## TE 
Terminal Equipment终端设备
UE : 
User Equipment用户设备
UTRAN : 
UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
## VLR 
Visitor Location Register拜访位置寄存器
# ZUF-77-10 APN 
概述 : 
功能描述 : 
APN是用户通过手机上网时必须配置的一个参数，它决定了用户的手机通过哪种接入方式来访问网络，在骨干网中用来标识要使用的外部PDN网络。APN由以下两部分组成： 
网络标识：这部分必选，是由网络运营者分配给ISP（互联网服务提供商，Internet Service Provider）或公司的、与其固定Internet域名一样的一个标识。 
运营商标识：这部分可选，其形式为“xxx.yyy.gprs”（如MNC.MCC.gprs）或”xxx.yyy.3gppnetwork.org”（ MNC.MCC. 3gppnetwork.org），用于标识归属网络。 
功能特性简介 : 
针对APN的应用场景，核心网提供了可靠、有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
APN更正功能|APN更正功能指用户没有携带APN或者携带的APN不合法（无效的格式，或格式有效但是没有对应的GGSN）时，SGSN更正为其他APN。用户使用更正后的APN激活PDP上下文访问数据业务和其他业务。SGSN支持根据IMSI号段和PDP类型控制是否进行APN更正，配置APN更正方式、是否检查签约“*”及指定更正后的APN。APN更正方式有：SGSN配置的APNHLR签约的APNAPN模糊匹配|ZUF-77-10-001 APN更正功能
APN扩展|SGSN在进行GGSN选择时，根据配置的扩展方法对APN NI进行扩展。SGSN用扩展后的APN NI来构造APN获取服务的GGSN/PGW。SGSN根据以下依据确定是否进行扩展：用户号段（IMSI或MSISDN）APNAPN和用户号段是否漫游计费特性终端是否支持EPC能力扩展的信息包括：用户IMSI号码段用户MSISDN号码段计费特性计费特性和IMSI号码段计费特性和MSISDN号码段用户IMEI号码段|ZUF-77-10-002 APN扩展
APN转换|当用户携带的APN合法且是用户签约的APN时，SGSN支持根据MS的IMSI号段、PDP类型和MS请求的APN，将用户请求的合法APN转换为SGSN配置的APN，以灵活选择GGSN。转换后的APN对其他网元可见。|ZUF-77-10-003 APN转换
## ZUF-77-10-001 APN更正功能 
特性描述 : 
摘要术语描述应用场景客户收益实现原理系统影响应用限制遵循标准特性能力O&M相关 
术语 : 
无 
描述 : 
定义
APN更正功能包括4种：指定APN更正、更正为签约的第一个APN、APN模糊匹配和请求APN。 
指定APN更正：指用户发起激活PDP，对APN检查失败时，把用户使用的APN更正为指定的APN。如果开关指示不需要对指定APN检查是否有对应的签约上下文，将默认QoS作为PDP上下文的签约QoS，使用用户级别的签约计费特性。如果开关指示需要对指定APN检查是否有对应的签约上下文，则检查指定APN是否已签约。如果指定APN已签约，用户的签约信息取指定APN对应的签约上下文中的信息，如果指定APN已签约多个，SGSN取其中任意一个即可。如果指定APN没有签约，则激活PDP失败。指定APN和签约的APN必须完全一样才检查成功，用户签约的APN中有“*”不能作为检查成功的依据。 
更正为签约的第一个APN：指用户发起激活PDP，对APN检查失败时，把用户使用的APN更正为签约的第一个APN，如果第一个签约为“*”，则使用默认APN。签约的第一个APN指插入用户数据消息中的第一个签约APN（上下文ID最小的APN）。第一个签约APN有如下特性：如果所有APN签约数据发生变更，HLR将全部签约数据再次插入，SGSN还是取插入用户数据消息中的第一个签约APN。如果HLR单独插入一个新增的APN签约信息，则这个新增加的APN签约信息认为是最后一个。如果HLR单独插入一个修改的APN签约信息，则修改的APN签约数据替换原来的签约数据。如果HLR删除APN签约信息，则原插入用户数据消息中剩下的APN签约数据中靠前的APN签约数据为第一个签约APN。默认APN指每个IMSI号段配置的一个指定APN，如果没有指定APN，则取SGSN的全局的APN。 
APN模糊匹配：是指定APN更正方式和更正为签约的第一个APN方式的结合。用户发起激活PDP，对APN检查失败时，SGSN使用指定APN，如果指定的APN已签约，则用户使用的APN为指定APN。如果指定的APN没有签约，则把用户使用的APN更正为签约的第一个APN，如果第一个签约为“*”，则使用默认APN。APN模糊匹配必须有指定APN。 
请求APN：指用户发起激活PDP，对APN检查失败或根据APN查找GGSN失败时，检查用户请求的APN是否有签约。如果有签约，使用签约的该APN。如果请求的PDP
TYPE不在签约中，更正为签约的PDP TYPE，如果有多个签约PDP TYPE，则使用配置确定使用哪一个。如果激活请求消息中携带了PDP
地址，PDP地址检查失败，使用协商的PDP TYPE对应的签约PDP地址。如果请求的APN没有签约或用户没有携带请求的APN，则把用户使用的APN更正为签约的第一个APN，如果第一个签约为“*”，则使用默认APN。 
APN更正完成之后，用户使用更正后的APN激活PDP上下文访问数据业务和其他业务。对于漫入用户需做特殊处理，主要是基于本地SGSN运营商并不一定清楚漫入用户归属地所在SGSN默认使用的APN，因此对于漫入用户，APN更正使用第一个非“*”的APN，除非只有一个“*”无法进行更正时拒绝PDP激活。 
背景知识
GPRS网络架构图如[图1]所示。
图1  GPRS架构图
TE/MT：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。
BSS：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。
UTRAN：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。
HLR：永久存储用户签约数据。
PDN：为用户提供业务的网络。
CGF：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。
BS：负责接收和处理从核心网发送过来的CDR文件。
EIR：负责检查UE设备。
PSCN：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元：
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM）上下文和分组数据协议（PDP）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息。 
GGSN：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。 
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务。包含如下网元： 
MSC/VLR：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。 
SMSGMSC/SMS IWMSC：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。 
CAMEL：该功能实体主要对用户进行在线计费。 
应用场景 : 
GnGp SGSN网元APN更正功能，必须由运营商确认后才能使用。具体常见场景包括： 
UE携带了错误的APN。 
UE携带了非法的APN，比如以“rac”、“lac”、“sgsn”、“rnc”或“*”开头的APN。 
UE没有携带APN，且签约了多个PDP上下文。 
客户收益 : 
收益者|收益描述
---|---
运营商|支持GnGp SGSN网元APN更正功能后，可以提高用户激活PDP的成功率，提高用户使用数据业务和其他业务的成功率，从而提高用户对移动网络的使用满意度。
实现原理 : 
涉及的网元
GnGp SGSN网元APN更正功能由SGSN独立完成。 
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM）上下文和分组数据协议（PDP）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。在APN更正功能中具体功能是指用户首次激活过程中，在APN检查失败时，对用户使用的APN进行更正。 
业务流程
PDP上下文激活过程
图2  PDP上下文激活过程
UE发送激活PDP上下文请求消息给SGSN。 
SGSN进行APN检查，如果检查通过，则根据APN解析GGSN，给GGSN发送创建PDP上下文请求消息。 
SGSN检查APN失败，如果APN更正功能没有启用，则给UE直接回激活PDP上下文拒绝消息，如果APN更正功能启用了，流程执行第4-8步。 
APN更正方式为“指定APN更正”时，如果开关指示不需要对指定APN检查是否已签约，则使用的APN为指定APN，将默认QoS作为PDP上下文的签约QoS，使用用户级别的签约计费特性。 
如果开关指示需要对指定APN检查是否已签约，则进一步检查指定APN是否已签约。如果指定APN已签约，用户的签约信息取指定APN对应的签约上下文中的信息，如果指定APN已签约多个，SGSN取其中任意一个即可。如果指定APN没有签约，则激活PDP失败，SGSN给UE直接回激活PDP上下文拒绝消息。 
 说明： 
指定APN和签约的APN必须完全一样才检查成功，用户签约的APN中有“*”不能作为检查成功。 
APN更正方式为“签约的第一个APN”时，取签约的第一个APN，如果第一个签约为“*”，则使用默认APN。 
签约的第一个APN指插入用户数据消息中的第一个签约APN。默认APN指每个IMSI号段配置的一个指定APN，如果没有指定APN，则取SGSN的全局的APN。 
APN更正方式为“APN模糊匹配”时，先取指定APN。如果指定的APN已签约，则用户使用的APN为指定APN。如果指定的APN没有签约，则把用户使用的APN更正为签约的第一个APN，如果第一个签约为“*”，则使用默认APN。 
APN更正方式为“请求APN”时，先判断用户请求的APN是否有签约。如果有签约，使用签约的该APN。如果请求的PDP
TYPE不在签约中，更正为签约的PDP TYPE，如果有多个签约PDP TYPE，则使用配置确定使用哪一个。如果激活请求消息中携带了PDP
地址，PDP地址检查失败，使用协商的PDP TYPE对应的签约PDP地址。如果请求的APN没有签约或用户没有携带请求的APN，则把用户使用的APN更正为签约的第一个APN，如果第一个签约为“*”，则使用默认APN。 
对于漫入用户的特殊处理，主要是基于本地SGSN运营商并不一定清楚漫入用户归属地所在SGSN默认使用的APN，因此对于漫入用户，APN更正使用第一个非“*”的APN，除非只有一个“*”无法进行更正时拒绝PDP激活。
SGSN对APN更正以后，根据APN解析GGSN，给GGSN发送创建PDP上下文请求消息。 
系统影响 : 
GnGp SGSN网元APN更正功能，对CPU和内存等系统资源占用很小。 
应用限制 : 
无 
遵循标准 : 
3GPP TS 23.060 " General Packet Radio Service (GPRS) ; Service
description; Stage 2". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service (GPRS); Base
Station System (BSS) - Serving GPRS Support Node (SGSN); BSS GPRS
Protocol (BSSGP)". 
3GPP TS 29.060: "General Packet Radio Service (GPRS); GPRS
Tunnelling Protocol (GTP) across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part (MAP) specification". 
3GPP TS 23.003: "Numbering, addressing and identification" 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
APN更正功能最多支持1024个IMSI号段，每个IMSI号段的长度为1-15。 
O&M相关 : 
命令
无 
性能统计
无 
告警和通知
无 
业务观察/失败观察
无 
话单与计费
激活成功，开启SCDR话单。 
特性配置 : 
摘要配置特性测试用例常见问题处理 
配置特性 : 
配置前提
SGSN局基本配置已经完成，满足附着流程的要求。 
配置过程
执行命令[SET SOFTWARE PARAMETER]，配置软件参数“指定APN更正是否需要检查HLR签约信息”（软件参数ID为786483）。
执行命令[SET APNMOD POLICY]，配置APN更正功能。
执行命令[ADD APN MODIFICATION]，新增APN更正配置。
执行命令[SET SOFTWARE PARAMETER]，配置软件参数“是否支持漫入用户的APN更正优化”（软件参数ID为786490）。
配置实例
配置脚本|说明
---|---
SET SOFTWARE PARAMETER:PARAID=786483,PARAVALUE=1|配置指定APN更正是否需要检查HLR签约信息。
SET APNMOD POLICY:APNMODIFY="YES"|打开APN更正功能。
ADD APN MODIFICATION:IMSI="460300",MODIFYMODE="APNFuzzy Match",APN="apn1",PDPTYPE="IPv4"|新增APN更正配置。
测试用例 : 
无 
常见问题处理 : 
无 
## ZUF-77-10-002 APN扩展 
特性描述 : 
术语 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
应用限制 
特性交互 
遵循标准 
特性能力 
可获得性 
O&M相关 
术语 : 
术语|含义
---|---
APN扩展|在原APN上增加新的信息
APN转换|替换原APN中的信息。
APN更正|修改原APN中不正确的信息
描述 : 
定义
APN扩展：SGSN在使用APN进行GGSN/PGW选择时，对使用的APN（如果有APN更正或APN转换，则为更正后的APN或转换后的APN）根据配置的扩展方法对APN NI进行扩展。然后用扩展后的APN 获取服务的GGSN/PGW，所以扩展目的为了更准确地获取到本次服务的GGSN/PGW。 
背景知识
运营商在部署GGSN/PGW时，有可能需要考虑用户的号码和签约计费特性等，如不同计费特性在不同GGSN/PGW。在APN NI中扩展用户信息，可以为运营商提供更准确的GGSN/PGW选择策略，从而运营商可以更灵活的规划网络。 
应用场景 : 
场景一：基于IMSI扩展APN的场景当根据IMSI段来区分不同GGSN时，配置IMSI段的APN扩展。 
场景二：基于MSISDN扩展APN的场景当根据MSISDN段来区分不同GGSN时，配置MSISDN段的APN扩展。 
场景三：基于IMEI扩展APN的场景当根据IMEI段来区分不同GGSN时，配置IMEI段的APN扩展。 
场景四：基于计费特性扩展APN的场景当需要根据计费特性来区分不同GGSN，配置APN对应的计费特性扩展。 
场景五：基于IMSI号段和计费特性扩展APN的场景当需要根据IMSI号段和计费特性来区分不同GGSN时，则配置IMSI号段+计费特性的APN扩展。 
场景六：基于MSISDN号段和计费特性扩展APN的场景当需求根据MSISDN号段和计费特性来区分不同GGSN时，配置MSISDN号段+计费特性的APN扩展。 
客户收益 : 
收益方|受益描述
---|---
运营商|组网灵活，扩容方便
移动用户|无
实现原理 : 
系统架构
无 
涉及的网元
为本网元的功能，无网元间作用。 
协议栈
无 
本网元实现
SGSN根据如下信息确定是否对APN进行扩展： 
用户号段（IMSI或MSISDN） 
APN 
终端是否支持EPC能力 
是否漫游 
计费特性 
扩展的信息包括： 
用户IMSI号码段 
用户MSISDN号码段 
计费特性 
计费特性和IMSI号码段 
计费特性和MSISDN号码段 
用户IMEI号码段 
业务流程
PDP激活流程：SGSN在根据APN选择GGSN/PGW时，可以根据用户信息确定是否需对APN进行扩展，如根据CC标识的是否接入归属地省份GGSN/PGW，确定是否对用户进行APN扩展。如果需要，则对APN进行扩展后，使用扩展后的APN解析GGSN/PGW。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
本特性所遵循的标准为： 
协议|章节号及章节名称
---|---
3GPP TS 23.060: " General Packet Radio Service (GPRS); Servicedescription "|Stage 1
特性能力 : 
无。 
可获得性 : 
版本要求及变更记录
ZXUN-uMAC V4.12.11版本及后续版本。 
License要求
本特性无License控制。 
对其他网元的要求
需要在DNS上配置扩展后的APN对应的DNS数据。
工程规划要求
无 
O&M相关 : 
命令
配置项该特性不涉及配置项的变化。 
安全变量该特性不涉及安全变量的变化。 
定时器该特性不涉及定时器的变化。 
软参该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计
该特性不涉及性能统计的变化。 
告警和通知
该特性不涉及告警和通知消息的变化。 
业务观察/失败观察
该特性不涉及业务观察/失败观察的变化。 
话单与计费
该特性不涉及话单与计费的变化。 
特性配置 : 
配置特性 
调整特性 
测试用例 
常见问题处理 
配置特性 : 
配置说明
配置APN转换。 
配置前提
MME、SGSN或Combo（MME和SGSN合一成局）的网管客户端和服务器间能够正常通信。 
配置过程
SGSN的APN转换配置 
在命令终端使用[ADD CONVERT APN]命令，配置APN转换。
SGSN的APN扩展配置 
在命令终端使用[ADD EXAPN]命令，配置扩展APN。
配置实例
IMSI号码为8613700006001的用户在HLR中签约的APN为test.com，PDP
Type为IPv4，签约的第一个APN对应的计费特性为normal（普通计费）。
用户激活请求的APN是test.com，PDP
Type为IPv4，需要将激活请求的test.com转换成zte.com.normal.86137 
首先采用APN转换的配置将test.com转换成zte.com，再采用APN扩展的配置将zte.com根据计费特性+MSISDN进行扩展； 
配置步骤|解释说明|配置脚本
---|---|---
1|将软参中APN转换的控制开关打开。|SET SOFTWARE PARAMETER:PARAID=786537,PARAVALUE=1
2|在SGSN中配置APN转换。|ADD CONVERT APN:IMSI="460030000006001",REQPDPTYPE="IPv4",REQAPN="test.com",CNVTAPN="zte.com"
3|软参中设置根据计费特性的名称进行扩展，这个软参的默认值为0|SET SOFTWARE PARAMETER:PARAID=786485,PARAVALUE=0
4|软参中设置基于MSISDN进行扩展，这个软参的默认值为0|SET SOFTWARE PARAMETER:PARAID=786565,PARAVALUE=1
5|在SGSN中配置APN扩展。|ADD EXAPN:APN="zte.com",IMSI="8613700006001",EXUETYPE="For All",EXMODE="CHARGE+MSISDN",EXBITS=1-5,APNCTRL="NO"
调整特性 : 
无 
测试用例 : 
测试项目|基于MSISDN的APN扩展
测试目的|验证基于MSISDN的APN扩展功能是否实现。
预置条件|系统运行正常。设置安全变量“扩展APN的号码类型”为1（MSISDN）。配置APN+MSISDN的APN扩展，扩展模式是计费特性+MSISDN。
测试过程|使用配置号段MSISDN内的用户附着，使用APN激活。
通过准则|用户匹配到APN扩展中APN+MSISDN的记录，并且扩展方式是计费特性+MSISDN。
测试结果|无
常见问题处理 : 
无 
## ZUF-77-10-003 APN转换 
概述 : 
SGSN支持APN转换。当用户的PDP激活消息携带签约的APN时，SGSN使用其他APN替换该APN，并允许用户激活PDP上下文。 
收益 : 
本特性可避免由于核心网中的APN配置发生变化而无法接入PS网络和使用业务。 
通过本特性，运营商可提高PDP激活成功率的KPI指标而无需变更用户的配置文件。 
描述 : 
SGSN支持APN转换。本特性插入到PDP激活流程。 
SGSN基于IMSI号段和MS请求的APN选择新APN。SGSN使用新APN进行GGSN选择、话单生成和GTP消息填写等操作。 
当用户携带合法的签约APN，SGSN根据MS的IMSI号段、PDP类型以及MS请求的APN将该APN转换成SGSN配置的APN，从而可灵活进行GGSN选择。转换后的APN对其他NE是可见的。 
# 缩略语 
# 缩略语 
APN : 
Access Point Name接入点名称
## BS 
Billing System计费系统
## BSS 
Base Station Subsystem基站子系统
## CAMEL 
Customized Applications for Mobile Network Enhanced Logic移动网络增强逻辑的客户化应用
## CGF 
Charging
Gateway Function 计费网关功能
## CN 
Core Network核心网
DNS : 
Domain Name Server域名服务器
EIR : 
Equipment Identity Register设备标识寄存器
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
## GMM 
GPRS Mobile ManagementGPRS 移动性管理
## GMSC 
Gateway Mobile Switching Center网关移动交换中心
HLR : 
Home Location Register归属位置寄存器
IMEI : 
International Mobile Equipment Identity国际移动设备标识
## ISP 
Internet Service Provider因特网业务提供者
## IWMSC 
Interworking Mobile Switching Center网间移动交换中心
MSC : 
Mobile Switching Center移动交换中心
## MT 
Mobile Terminal移动终端
PDN : 
Packet Data Network分组数据网
PDP : 
Packet Data Protocol分组数据协议
## PS 
Packet Switched分组交换
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
SMS : 
Short Message Service短消息业务
## TE 
Terminal Equipment终端设备
UTRAN : 
UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
## VLR 
Visitor Location Register拜访位置寄存器
# ZUF-77-11 QoS 
概述 : 
功能描述 : 
QoS指在网络通信过程中，允许用户业务在丢包率、延迟、抖动和带宽等方面获得可预期的服务水平，为指定的网络通信提供更好的服务能力，是网络的一种安全机制，是用来解决网络延迟和阻塞等问题的一种技术。 
功能特性简介 : 
QoS功能详细的特性如下表： 
方案特性|实现简述|特导链接
---|---|---
QoS协商|移动网络中的各个网元SGSN、GGSN和RNC在整个QOS协商过程中，可以根据本身的资源状况，进行业务QoS参数的调整，即各个网元都可以修改使用的QoS，最后使用的QoS是各个网元协商的结果，是各个网元都能接受的QoS。SGSN支持R98、R99、R4、R5、R6、R7和R8版本QoS，既支持HSPA，也支持HSPA+。SGSN在QoS协商中起到主导角色，协商后的QoS由SGSN发送给手机。在如下流程中进行QoS协商：PDP激活PDP修改局内RAU局间RAU业务请求协商具体过程参见3GPP 23.060协议“9.2 PDP Context Activation, Modification, Deactivation, and Preservation Functions”章节。|ZUF-77-11-001 QoS协商
SGSN本地Qos策略|为灵活进行QoS控制，可以在SGSN上配置各种本地策略。SGSN本地QoS策略包括：按如下方式限制QoS上限：用户IMSI号段用户IMSI号段+接入方式（Iu接入或Gb接入）用户IMSI号段+接入的RNC ID基于IMSI号段的签约QoS的提升。自动识别UE的QoS能力。如果MS不接受网络侧协商出的QoS，MS会在PDP激活成功之后，立刻去激活该PDP，原因值指示为“QoS不接受”，当PDP上下文被再次激活，SGSN主动降低最大上下行速率到配置的区间。根据不同GGSN局向设置QoS版本适配。支持与RNC进行QoS协商。网络侧的ARP、THP参数和无线侧的ARP、THP参数可灵活映射。支持在下述流程中进行QoS重新协商：RAU流程切换流程业务请求流程|ZUF-77-11-002 SGSN本地Qos策略
DSCP映射|SGSN通过配置能力支持IP差别化服务（Diff-Serv）的QoS策略。SGSN可以分别为用户面和控制面设置独立的DSCP值。SGSN根据业务QoS参数设置用户面上下行数据报文的DSCP值。可以按如下维度进行映射：业务类别+ARP业务类别+MBR业务类别+GBR业务类别+传输时延SGSN可以为如下接口消息指定DSCP值。Gb下行层三信令Gb下行承载信令Gn接口的信令报文Ga接口ETSI LI1/ETSI LI2/ETSI LI3接口|ZUF-77-11-003 DSCP映射
R99/R98 QoS|SGSN支持R99/R98 QoS，并支持R99 QoS与R98/R97 QoS的相互转换。|ZUF-77-11-004 R99/R98 QoS
## ZUF-77-11-001 QoS协商 
特性描述 : 
术语 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
应用限制 
特性交互 
遵循标准 
特性能力 
可获得性 
O&M相关 
术语 : 
术语|含义
---|---
请求QoS|手机希望得到的QoS，UE/MS在激活PDP上下文请求或修改PDP上下文请求消息中携带。
签约QoS|能得到的QoS的上限，在HLR/HSS中签约确定。
默认QoS|在网管上配置的QoS。
协商QoS|最后协商使用的QoS，SGSN、GGSN、RNC都可以根据策略修改协商QoS的参数。
描述 : 
定义
QoS指在网络通信过程中，允许用户业务在丢包率、延迟、抖动和带宽等方面获得可预期的服务水平，为指定的网络通信提供更好的服务能力，是网络的一种安全机制，是用来解决网络延迟和阻塞等问题的一种技术。
移动网络，使用了两种典型的QoS确定机制：协商机制和PCC机制。
协商机制：移动网络中的各个网元SGSN、GGSN和RNC在整个QoS协商过程中，可以根据本身的资源状况，进行业务QoS参数的调整，即各个网元都可以修改使用的QoS，最后使用的QoS是各个网元协商的结果，是各个网元都能接受的QoS。SGSN起到主导角色，协商后的QoS由SGSN发送给手机。 
PCC机制：PCC即策略控制和计费，是由3GPP定义动态策略和计费控制技术方案，可实现2G/3G/LTE接入的统一策略控制，对QoS的策略控制是保障数据业务对网络资源的占用，在移动网络中只有一个网元（PCRF）具有QoS确定功能，其他网元不再具有QoS协商能力，要么接受确定的QoS，要么承载建立失败。 
Pre-R8之前的QoS确定机制，就是典型的协商机制，SGSN、GGSN、RNC都可以修改QoS。SGSN是控制面QoS协商的核心网元。
背景知识
QoS架构
3GPP对QoS提出了明确的要求，其核心和关键即在于“必须能满足端到端的QoS要求”。网络服务是一种端到端的业务，每一个端到端的业务都具有一定的QoS要求，以便网络为用户提供相应服务质量的保证。为实现一个特定的网络业务QoS，将在服务的源端和目的端建立一个清晰的特征和功能性定义的承载。
UMTS QoS采用分层的体系结构来为业务提供端到端的QoS保证。
图1  UMTS的QoS架构
在上述架构中，各个网元对QoS的处理如下：
网元名称|网元处理
---|---
TE+MT|根据上层业务，构造上层业务对UMTSQoS的要求，并通过请求QoS反馈给移动网络。
RAN（RNC）|对空口无线资源进行管理，根据业务优先级和用户优先级，对不同承载，进行不同的接纳控制、拥塞控制、负荷控制。可以参与QoS的协商。
CN EDGE NODE（SGSN）|SGSN对用户进行移动性管理和会话管理，是QoS协商的核心网元。
CN Gateway（GGSN）|分组域移动网络的网关，可参与QoS协商。如果部署了PCRF，则GGSN还可以根据PCRF的策略，更新QoS。
在上述架构中，从承载服务的角度包括无线接入承载服务和核心网承载服务： 
无线接入承载服务包括无线承载服务和RAN接入承载服务，其中无线承载服务包括了无线接口传输的所有方面，RAN接入承载服务和物理承载服务共同提供在UTRAN和CN之前的信息传输，RAN接入承载服务能够为具有不同QoS需求的分组业务提供不同的承载服务。 
核心网承载服务通过骨干网络服务来实现，骨干网络服务包括层1和层2的功能性，可以根据运营商的选择来实现核心网承载服务的QoS需求。 
QoS保障机制的作用
在3G系统中，通过QoS保证机制的支持（即服务质量的支持）可以实现业务的分级服务及用户的分类服务功能，即实现：
移动宽带网络需要对单个用户接入的不同的网络提供接入带宽管理，不同的业务可分配不同的资源以保证其所属业务级别的业务质量，同时使网络具有合理的资源利用率。 
不同的用户可签约不同的服务级别，提供不同的接入带宽，不同接入优先级，从而获得其所属类型的质量要求。 
QoS的四种承载业务类别及其应用和特征
根据业务对时延敏感性的不同，UMTS系统定义了四种承载业务类别：会话类、流类、交互类和背景类，典型业务应用和特征见下表。值得注意的一点，在各种应用业务与业务类别之间，不存在严格的一对一映射关系，如视频多媒体业务可以是会话类、流类，或者交互类。 
业务类别|会话类 Conversational class|流类 Streaming class|交互类 Interactive class|背景类 Background class
应用举例|语音、可视电话|视频流、音频流|网页浏览、位置服务|Email、FTP文件下载
主要特征|保证数据顺序关系;严格的低延时要求|保证数据顺序关系|请求应答模式;保证业务内容|数据没有时延要求;保证业务内容
注：GPRS基于分组交换，只提供”Best Effort” QoS，不保证比特率和时延等。GPRS接入网没有“连接”概念，所有用户流是混合的，不能提供QoS保证。
应用场景 : 
分组域业务主要包括语音、可视电话、视频点播（无交互）、音频点播、网页浏览、位置服务、Email、FTP文件下载等业务，其中语音、可视电话、视频点播（无交互）和音频点播等业务属于会话类或流类，此类业务一般要求保障型速率；网页浏览、位置服务、Email、FTP文件下载等业务属于交互类或背景类，此类业务一般不要求保障型速率。因此SGSNQoS保障机制主要应用于两类分组域业务：
保障速率的用户业务。 
非保障速率的用户业务。 
保障速率的用户业务
保障速率的用户业务一般是语音、可视电话、视频点播（无交互）和音频点播等业务，此类业务属于会话类或流类。 
资源充足时应用场景图如[图2]所示。
图2  资源充足时保障速率的用户业务应用场景
用户进行保障速率型业务（如语音、可视电话、视频点播（无交互）和音频点播等）时，在SGSN上进行PDP激活，UE将请求的QoS（包括Traffic class（会话类或流类）、MBR、GBR等）带给SGSN。
UE之前在网络附着时，HLR将用户签约的QoS信息下发给SGSN。
SGSN比较签约的QoS和请求的QoS，协商成功向GGSN申请创建一个PDP上下文，携带与签约协商的QoS（QoS negotiated 1）。
GGSN根据自身的资源情况进行QoS调整，将协商后的QoS（QoS negotiated 2）信息返回给SGSN。
SGSN下发协商后的QoS（包括Traffic class（会话类或流类）、MBR、GBR等）给RNC。
RNC根据QoS参数中的GBR大小，RNC会预留资源，保证这个RAB的最小带宽为GBR（最大带宽为MBR），为用户业务分配带宽。
资源紧张时应用场景图如下： 
图3  资源紧张时保障速率的用户业务应用场景
VIP用户进行保障速率型业务（如语音、可视电话、视频点播（无交互）和音频点播等），普通用户进行保障速率或非保障速率业务时，两用户分别在SGSN上进行PDP激活，两UE将请求的QoS分别带给SGSN。
两UE之前在网络附着时，HLR分别将两用户签约的QoS信息下发给SGSN，VIP用户签约ARP为1，普通用户签约ARP为2或3。
SGSN和GGSN对两用户的QoS协商后，SGSN分别下发两用户协商后的QoS。
RNC的无线资源是有限的，根据VIP用户QoS参数中的GBR大小，RNC判断资源池的资源不能满足GBR，则抢占其他普通用户RAB的预留资源，保证VIP用户这个RAB的最小带宽为GBR（最大带宽为MBR），为用户业务分配带宽。因VIP用户抢占了普通用户RAN的预留资源，RNC对普通用户的RAB指派失败。
非保障速率的用户业务
非保障速率的用户业务一般是网页浏览、位置服务、Email、FTP文件下载等业务，此类业务属于交互类或背景类。
资源充足应用场景图如下： 
图4  资源充足时非保障速率的用户业务应用场景
用户进行非保障速率型业务（如网页浏览、位置服务、Email、FTP文件下载等）时，在SGSN上进行PDP激活，UE将请求的QoS（包括Traffic class（交互类或背景类）、MBR等）带给SGSN。
UE之前在网络附着时，HLR将用户签约的QoS信息下发给SGSN。
SGSN比较签约的QoS和请求的QoS，协商成功向GGSN申请创建一个PDP上下文，携带与签约协商的QoS（QoS negotiated 1）。
GGSN根据自身的资源情况进行QoS调整，将协商后的QoS（QoS negotiated 2）信息返回给SGSN。
SGSN下发协商后的QoS（包括Traffic class（交互类或背景类）、MBR、GBR=0等）给RNC。
RNC根据基本优先级和MBR，配置了NBR（名义比特率，默认值32kbps），RNC也会预留资源，保证这个RAB的最小带宽为NBR（最大带宽为MBR），为用户业务分配带宽。
资源紧张时应用场景图如下：
图5  资源紧张时非保障速率的用户业务应用场景
VIP用户进行非保障速率型业务（如网页浏览、位置服务、Email、FTP文件下载等），普通用户进行保障速率或非保障速率业务时，两用户分别在SGSN上进行PDP激活，两UE将请求的QoS带给SGSN。
两UE之前在网络附着时，HLR分别将两用户签约的QoS信息下发给SGSN，VIP用户签约ARP为1，普通用户签约ARP为2或3。
SGSN和GGSN对两用户的QoS协商后，SGSN分别下发两用户协商后的QoS。
RNC的无线资源是有限的，根据VIP用户基本优先级和MBR，配置了NBR（名义比特率，默认值32kbps），RNC判断资源池的资源不能满足NBR，则抢占其他普通用户RAB的预留资源，保证VIP用户这个RAB的最小带宽为NBR（最大带宽为MBR），为用户业务分配带宽。因VIP用户抢占了普通用户RAN的预留资源，RNC对普通用户的RAB指派失败。
客户收益 : 
受益方|受益描述
---|---
运营商|提高运营成本效益，QoS机制为网络运营商提供了优化网络资源的有效手段，使得网络运营商能以最少量的网络资源满足更多终端用户的需求。获得新的收入增长点，QoS机制可使网络运营商提供更多增值业务，提高终端用户的满意度和忠诚度。
移动用户|用户可以享用优质的网络服务。QoS机制使终端用户使用复杂（通常其QoS需求较高）的应用成为可能，保证高端用户得到比低端用户更好的服务。
实现原理 : 
系统架构
无 
涉及的网元
SGSN网元QoS功能由UE、HLR、RNC、SGSN和GGSN配合完成。
网元名称|网元作用
---|---
UE|根据上层业务，构造上层业务对QoS的要求，并通过请求QoS反馈给SGSN。
HLR|负责存储用户签约的QoS，在HLR上配置有用户能得到的QoS的上限。
RNC|对空口无线资源进行管理，根据业务优先级和用户优先级，对不同承载，进行不同的接纳控制、拥塞控制、负荷控制，参与QoS的协商。
SGSN|SGSN对用户进行移动性管理和会话管理，是控制面QoS协商的核心网元。
GGSN|分组域移动网络的网关，参与QoS协商。如果部署了PCRF，则GGSN还可以根据PCRF的策略，更新QoS。
协议栈
无 
本网元实现
无 
业务流程
SGSN网元QoS功能涉及如下业务流程： 
PDP激活。
PDP修改。
局内RAU。
局间RAU。
业务请求。 
PDP激活
流程图如下： 
图6  PDP激活过程中QoS协商流程
流程描述： 
终端在网络附着时，HLR将用户签约的QoS（Sub QoS）信息插入用户数据（HLR里有用户的签约QoS Profile），下发给SGSN。
MS在发起PDP激活时，将请求的QoS（Req QoS）携带给SGSN，向SGSN申请激活一个PDP上下文，但也可以不给出QoS需求，SGSN直接使用默认的QoS。
SGSN对Req QoS进行参数合法性检查。如果Req QoS中有参数携带了保留值，则拒绝激活PDP上下文。
SGSN比较签约的QoS和请求的QoS，协商成功向GGSN申请创建一个PDP上下文，携带与签约协商的QoS（QoS negotiated 1）。
如果GGSN有足够的资源满足业务QoS的需求，向SGSN回送一个PDP上下文创建成功消息，一个GTP隧道将在GGSN和SGSN之间建立。GGSN会根据自身的资源情况进行QoS的调整，将协商后的QoS信息（QoS negotiated 2）返回给SGSN。
SGSN根据与GGSN协商的QoS（QoS negotiated 2）通知RNC进行RAB指派，由RNC去建立一个无线接入承载RAB。
RNC执行内部的接入控制和资源预留，创建RAB成功，并向SGSN返回RAB指派成功并携带QoS（QoS negotiated 3）。如果RNC没有足够的资源，则RAB创建失败向SGSN返回RAB指派失败并在原因值中指明请求的QoS不能提供。
SGSN根据RNC返回的结果降低QoS属性（QoS negotiated 3）并再次向GGSN发起上下文更新请求。
GGSN更新上下文成功，给SGSN返回Update PDP Context Response消息。
SGSN给终端发送Activate PDP Context Accept消息，携带QoS negotiated 3。
手机接受网络的协商结果，满足相关QoS（QoS negotiated 3）的手机到GGSN的PDP上下文建立完成。
说明：二次激活过程中QoS协商与一次激活过程一致。 
PDP修改
SGSN发起PDP修改
流程图如下： 
图7  SGSN发起PDP修改过程中QoS协商流程
流程描述： 
SGSN发送Update PDP Context Request (TEID, NSAPI, QoS Negotiated, DTI) 消息到GGSN。
GGSN保存协商的QoS，返回Update PDP Context Response (TEID, QoS Negotiated, Cause) 消息给SGSN。
SGSN发起RAB指派流程修改空口的承载参数。
RAB修改流程中，如果RNC减低了QoS，SGSN通过发送Update PDP Context Request 消息给GGSN，把新协商的QoS参数通知给GGSN。
GGSN接受新协商的QoS发送Update PDP Context Response消息给SGSN。
SGSN发送Modify PDP Context Request (TI, QoS Negotiated, Radio Priority)消息给终端。
SGSN发送Modify PDP Context Request (TI, QoS Negotiated, Radio Priority)消息给终端。
GGSN发起PDP修改
流程图如下： 
图8  GGSN发起PDP修改过程中QoS协商流程
流程描述： 
GGSN发送Update PDP Context Request (TEID, NSAPI, PDP Address, QoS Requested,TFT) 消息到SGSN，QoS参数是GGSN希望的QoS。
SGSN发起RAB指派流程修改空口的承载参数。RNC执行内部的接入控制和资源预留，创建RAB成功，并向SGSN返回RAB指派成功并携带协商的QoS。
SGSN发送Modify PDP Context Request (TI, PDP Address, QoS Negotiated, Radio
Priority, TFT)消息到终端。
终端支持修改的QoS参数，返回Modify PDP Context Accept消息给SGSN。
SGSN收到终端返回的Modify PDP Context Accept 消息，发送Update PDP Context Response
(TEID, QoS Negotiated)消息到GGSN。
终端发起PDP修改
流程图如下： 
图9  终端发起PDP修改过程中QoS协商流程
流程描述： 
终端发送Modify PDP Context Request (TI, QoS Requested, TFT)消息到SGSN，携带终端希望的QoS，用于修改QoS。
SGSN发送Update PDP Context Request (TEID, NSAPI, QoS Negotiated, TFT, DTI) 消息到GGSN。
GGSN保存协商的QoS，返回Update PDP Context Response (TEID, QoS Negotiated, Cause) 消息给SGSN。
SGSN发起RAB指派流程修改空口的承载参数。
RAB修改流程中，如果RNC减低了QoS，SGSN通过发送Update PDP Context Request 消息给GGSN，把新协商的QoS参数通知给GGSN。
GGSN接受新协商的QoS发送Update PDP Context Response消息给SGSN。
SGSN发送Modify PDP Context Accept (TI, QoS Negotiated, Radio Priority)消息给终端。
RNC触发PDP修改
流程图如下： 
图10  RNC触发PDP修改过程中QoS协商流程
流程描述： 
RNC向SGSN发送Iu Release Request (Cause)消息。
如果PDP上下文的业务类型是流类或会话类，PDP上下文保留，SGSN将最大上下行比特率降为0，SGSN发送Update PDP Context Request消息通知GGSN将最大上下行比特率降为0，GGSN给SGSN回Update PDP Context
Response消息。如果PDP上下文的业务类型是交互类或背景类，PDP上下文不改变。
SGSN向RNC发送Iu Release Command (Cause)。
如果存在RRC连接，RNC发送Release RRC Connection message 消息给终端。
终端发送Release RRC Connection Acknowledge message 消息到RNC。
RNC向SGSN发送Iu Release Completion消息。
RAB释放触发PDP修改
流程图如下： 
图11  RAB释放触发PDP修改过程中QoS协商流程
流程描述： 
RNC向SGSN发送RAB Release Request消息。
如果PDP上下文的业务类型是流类或会话类，PDP上下文保留，SGSN将最大上下行比特率降为0，SGSN发送Update PDP Context Request消息通知GGSN将最大上下行比特率降为0，GGSN给SGSN回Update PDP Context
Response消息。如果PDP上下文的业务类型是交互类或背景类，PDP上下文不改变。
SGSN发送RAB Assignment Request (For each RAB to be released: RAB ID, Cause)消息给RNC释放RAB。
如果Radio Bearer存在，那么Radio Bearer将会被释放。 
RNC发送RAB Assignment Response 消息给SGSN。
HLR触发PDP修改
流程图如下： 
图12  HLR触发PDP修改过程中QoS协商流程
流程描述： 
HLR发送插入用户数据消息到SGSN。
SGSN更新用户新的签约数据，发送插入用户数据响应消息给HLR。
SGSN对于已经建立的PDP上下文进行检查QoS参数是否发生了改变，如果QoS发生了改变，SGSN发起PDP修改流程。
局内RAU
2G间局内RAU和3G间局内RAU，RAT没有发生改变，不需要重协商QoS。
2G到3G局内RAU
2G到3G局内RAU，RAT发生改变，SGSN进行QoS重协商，并把新的协商QoS通知终端。
流程图如下： 
图13  2G到3G局内RAU过程中QoS协商流程
与QoS相关流程描述： 
上图第6步，2G+3G SGSN位置更新完成后，进行QoS重协商。
SGSN发送Routing Area Update Accept消息给终端，消息中携带协商的QoS。
终端接受协商的QoS参数，返回Routing Area Update Complete消息给SGSN。
3G到2G局内RAU
3G到2G局内RAU，RAT发生改变，SGSN进行QoS重协商，并把新的协商QoS通知终端。
流程图如下： 
图14  3G到2G局内RAU过程中QoS协商流程
与QoS相关流程描述： 
上图第6步，2G+3G SGSN通知SRNS前转数据到SGSN后，进行QoS重协商。
SGSN发送Update PDP Context Request消息给GGSN，消息中携带协商的QoS。
GGSN返回Update PDP Context Response给SGSN。
上图第11步，SGSN位置更新完成后，发送Routing Area Update Accept消息给终端，消息中携带协商的QoS。
终端接受协商的QoS参数，返回Routing Area Update Complete消息给SGSN。
局间RAU
局间2G接入RAU
局间2G接入的RAU，SGSN进行QoS重协商，并把新的协商QoS通知终端。
流程图如下： 
图15  局间2G接入RAU过程中QoS协商流程
与QoS相关流程描述： 
上图第9步，SGSN隧道GTP数据传输后，进行QoS重协商。
SGSN发送Update PDP Context Request消息给GGSN，消息中携带协商的QoS。
GGSN返回Update PDP Context Response给SGSN。
上图第18步，SGSN位置更新完成后，发送Routing Area Update Accept消息给终端，消息中携带协商的QoS。
终端接受协商的QoS参数，返回Routing Area Update Complete消息给SGSN。
局间3G接入RAU
局间3G接入的RAU，SGSN进行QoS重协商，并把新的协商QoS通知终端。
流程图如下： 
图16  局间3G接入RAU过程中QoS协商流程
与QoS相关流程描述： 
上图第7步，SGSN隧道GTP数据传输后，进行QoS重协商。
SGSN发送Update PDP Context Request消息给GGSN，消息中携带协商的QoS。
GGSN返回Update PDP Context Response给SGSN。
上图第15步，SGSN位置更新完成后，发送Routing Area Update Accept消息给终端，消息中携带协商的QoS。
终端接受协商的QoS参数，返回Routing Area Update Complete消息给SGSN。
入局切换后首个RAU
入局切换完成后，终端发现RAI发生了改变，终端发起RAU，RAU过程中进行QoS重协商并将协商后的QoS通知终端。
业务请求
2G到3G局内RAU后的首次业务请求
与QoS相关流程描述：
图3-8第10和11步，SGSN收到业务请求，发送RAB Assignment
Request (RAB ID(s), QoS Profile(s), GTP SNDs, GTP SNUs, PDCP SNUs) 消息到SRNS来重新建立RAB。
RNC执行内部的接入控制和资源预留，创建RAB成功，并向SGSN返回RAB指派成功并携带QoS。
SGSN进行QoS重协商。
图3-8第11a步，SGSN发送Update PDP Context Request消息给GGSN，消息中携带协商的QoS。
GGSN返回Update PDP Context Response给SGSN。
SGSN发送Modify PDP Context Request消息给终端，消息中携带协商的QoS。
终端接受修改的QoS参数，返回Modify PDP Context Accept 消息给SGSN。
局间3G接入RAU后的首次业务请求
与QoS相关流程描述： 
图3-11第19和20步，SGSN收到业务请求，发送RAB Assignment
Request (RAB ID(s), QoS Profile(s), GTP SNDs, GTP SNUs, PDCP SNUs) 消息到SRNS来重新建立RAB。
RNC执行内部的接入控制和资源预留，创建RAB成功，并向SGSN返回RAB指派成功并携带QoS。
SGSN进行QoS重协商。
图3-11第20a步，SGSN发送Update PDP Context
Request消息给GGSN，消息中携带协商的QoS。
GGSN返回Update PDP Context Response给SGSN。
SGSN发送Modify PDP Context Request消息给终端，消息中携带协商的QoS。
终端接受修改的QoS参数，返回Modify PDP Context Accept 消息给SGSN。
系统影响 : 
随着在线用户数的增加，系统资源占用会一直增大，CPU占用率会相应上升。
应用限制 : 
无 
特性交互 : 
业务|交互
---|---
基于IMSI和RNC限制QoS功能|SGSN根据用户的IMSI、接入方式、RNCID，对用户进行QoS限制，限制策略包括两种：强制使用默认QoS，则协商QoS使用SGSNIMSI号段QoS上限配置的QoS。协商QoS是终端请求QoS、签约QoS和SGSNIMSI号段QoS上限配置的QoS三者取小。
Smart QoS|SGSN收到终端发起去活，原因为QoS not accepted，用户再一次发起激活时，协商的QoS将根据配置的Smart QoS进行降级。降级原则为比前一次激活的QoS小一个级别。
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060: "General Packet Radio Service (GPRS) ; Service
description; Stage 2". 
3GPP TS 23.107: "Quality of Service (QoS) concept and architecture”. 
3GPP TS 23.203: “Policy and charging control architecture”. 
3GPP TS 24.008: "Mobile radio interface Layer 3 specification". 
特性能力 : 
特性|能力
---|---
QoS速率|最大支持256Mbps
可获得性 : 
版本要求及变更记录
无 
License要求
无 
对其他网元的要求
SGSN网元QoS功能由UE、HLR、RNC、SGSN和GGSN配合完成。
工程规划要求
无 
O&M相关 : 
命令
配置项 
安全变量 
定时器 
软件参数新增软件参数参见表6。表6  新增软件参数软件参数ID软件参数名称393234old SGSN R5签约QoS是否降为R99786464协商的R5 QoS是否自动降低为R99版本393236是否自动降低请求QoS版本786448是否降低协商QoS版本786449长度为R6 QoS最大长度的QoS速率限制设置786645是否将RAU时更新响应中的新QoS通知UE786468HLR修改QoS后重新协商QoS控制786484RNC不接受QoS时用户激活失败原因值786557QoS改变时是否出碎片话单786647是否接受更新PDP上下文响应中的QoS786449Gn口GTP消息指示是否支持QoS协商 
动态管理 
性能统计
无 
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
配置特性 
调整特性 
测试用例 
常见问题处理 
配置说明 : 
配置QoS协商。 
配置前提 : 
ZXUN uMAC跟RNC、HLR、GGSN之间链路通畅，HLR上已有用户签约数据和鉴权数据等信息。
配置过程 : 
配置[SET QOS DEFAULT]命令。
该命令用于配置SGSN本地默认的QoS参数。
配置[ADD QOS DSCP]命令。
该命令用于配置SGSN的Gn接口、Iu接口、Gb接口的用户面数据报文的DSCP值。 
配置[ADD QOS PFI]命令。
该命令用于新增MME和SGSN的QOS与PFI映射关系。 
配置[ADD QOS PIE]命令。
该命令用于增加用户级别与PIE参数配置，支持Iu接入和Gb接入两种方式，并且每种方式只能配置3类用户。 
配置[ADD QOS USERRATE]命令。
该命令用于增加用户级别与最大上下行速率配置。 
配置[ADD QOS USERRATE]命令。
该命令用于增加用户级别与最大上下行速率配置。 
配置[ADD THP]命令。
该命令用于THP配置。 
配置[ADD QOSTPL]命令。
该命令用于配置一个QoS模板，此模板定义了一组QoS参数的集合。 
配置[ADD QOS UPGRADE TPL]命令。
该命令用于定义一个QoS提升模板，作用为提升用户签约QoS数据中的上/下行MBR（Maximum
Bit Rate，最大比特率）。 
配置[ADD IMSI UPGRADE QOS]命令。
该命令用于SGSN支持根据用户的IMSI号段，提升用户签约QoS数据中的上/下行MBR。
配置[ADD GGSN SEGMENT QOS VERSION]命令。
该命令用于配置某个GGSN网元支持的最高QoS版本。
配置[ADD SMART QOS]命令。
该命令用于SGSN根据MS的可以接受的MBR的上限值来配置“最大上行链路比特率”与“最大下行链路比特率”，以保持Qos协商成功。 
配置[SET IMSI QOSLMT SPRT]命令。
该命令用于设置SGSN是否支持基于IMSI号段和接入类型控制QoS上限。
配置[ADD IMSI QOSLMT]命令。
该命令用于增加IMSI号段QoS上限配置。 
配置[SET IMSI QOSLMT DEFAULT]命令。
该命令用于缺省IMSI号段上限配置。 
配置[SET RAB QOS]命令。
该命令用于设置RAB指派流程QoS配置。 
配置[SET RAU QOS UE]命令。
该命令用于设置RAU流程QoS重协商和通知UE配置。 
通过[SET PACKET DOMAIN PARAMETER]命令，可以设置Gn口GTP消息指示是否支持QOS协商和提升
通过[SET SOFTWARE PARAMETER]命令，可以修改软参取值。
配置实例 : 
保障速率的用户业务
实例场景1：资源充足情况下，用户从RNC接入SGSN，发起会话类PDP激活。 
配置脚本|QoS参数取默认值配置，即可满足测试场景。
实例场景：资源紧张情况下，VIP用户和普通用户从RNC接入SGSN，VIP用户签约ARP为1，普通用户签约ARP为2。两类用户分别发起会话类PDP激活，普通用户资源被抢占，进行QoS重协商。
ZXUN uMAC跟RNC、HLR、GGSN之间链路通畅，HLR上已有用户签约数据和鉴权数据等信息。
步骤|解释说明|配置脚本
---|---|---
设置VIP用户的PIE配置。|用户级别为VIP用户，接入方式为IU接入，传输类型为会话类，设置可抢占其他呼叫，不允许被其他呼叫抢占，不允许排队。|ADD QOS PIE:USERCLASS=1,ACCTYPE="Iu Access",TRAFFICCLASS="ConversationalClass",QA="NO"
设置普通用户的PIE配置。|用户级别为普通用户，接入方式为IU接入，传输类型为会话类，设置不可抢占其他呼叫，允许被其他呼叫抢占，允许排队。|ADD QOS PIE:USERCLASS=2,ACCTYPE="Iu Access",TRAFFICCLASS="ConversationalClass",PC="NO",PV="YES"
设置RAB指派流程中QoS协商参数。|配置QoS重协商最大次数为5，最大上下行比特率降低跳数为30 （以上参数取值可以根据实际情况进行调整）。|SET RAB QOS:RENEGOMAX=5,MAXBITUHOP=30,MAXBITDHOP=30
实例场景2
资源紧张情况下，VIP用户和普通用户从RNC接入SGSN，VIP用户签约ARP为1，普通用户签约ARP为2。两类用户分别发起会话类PDP激活，普通用户资源被抢占，进行QoS重协商。
步骤|解释说明|配置脚本
---|---|---
设置VIP用户的PIE配置。|用户级别为VIP用户，接入方式为IU接入，传输类型为会话类，设置可抢占其他呼叫，不允许被其他呼叫抢占，不允许排队。|ADD QOS PIE:USERCLASS=1,ACCTYPE="Iu Access",TRAFFICCLASS="ConversationalClass",QA="NO"
设置普通用户的PIE配置。|用户级别为普通用户，接入方式为IU接入，传输类型为会话类，设置不可抢占其他呼叫，允许被其他呼叫抢占，允许排队。|ADD QOS PIE:USERCLASS=2,ACCTYPE="Iu Access",TRAFFICCLASS="ConversationalClass",PC="NO",PV="YES"
设置RAB指派流程中QoS协商参数。|配置QoS重协商最大次数为5，最大上下行比特率降低跳数为30 （以上参数取值可以根据实际情况进行调整）。|SET RAB QOS:RENEGOMAX=5,MAXBITUHOP=30,MAXBITDHOP=30
非保障速率的用户业务
实例场景1：资源充足情况下，用户从BSC接入SGSN，用户发起交互类PDP激活。 
配置脚本|QoS参数取默认值配置，即可满足测试场景。
实例场景2：资源紧张情况下，VIP用户和普通用户从BSC接入SGSN，VIP用户签约ARP为1，低端用户签约ARP为3。两用户分别发起交互类PDP激活，低端用户资源被抢占，进行QoS重协商。 
实例|解释说明|配置脚本
---|---|---
设置VIP用户的PIE配置。|用户级别为VIP用户，接入方式为Gb接入，传输类型为交互类，设置可抢占其他呼叫，不允许被其他呼叫抢占，允许排队|ADD QOS PIE:USERCLASS=1,ACCTYPE="Gb Access",TRAFFICCLASS="InteractiveClass",PC="YES"
设置低端用户的PIE配置。|用户级别为低端用户，接入方式为Gb接入，传输类型为交互类，设置不可抢占其他呼叫，允许被其他呼叫抢占，允许排队|ADD QOS PIE:USERCLASS=3,ACCTYPE="Gb Access",TRAFFICCLASS="InteractiveClass",PC="NO",PV="YES"
设置RAB指派流程中QoS协商参数。|配置QoS重协商最大次数为5，最大上下行比特率降低跳数为30 （以上参数取值可以根据实际情况进行调整）|SET RAB QOS:RENEGOMAX=5,MAXBITUHOP=30,MAXBITDHOP=30
调整特性 : 
无 
测试用例 : 
保障速率的用户业务
资源充足时用户进行保障速率业务 
测试项目|资源充足情况下，用户进行保障速率业务
测试目的|验证SGSN能够创建会话类或流类PDP
预置条件|SGSN、HLR、RNC等工作正常，RNC带宽资源充足。
测试过程|用户从RNC接入到SGSN。用户发起一个会话类PDP上下文激活流程。
通过准则|用户能够成功激活一个会话类PDP上下文。
测试结果|无
资源紧张时不同类别用户进行保障速率业务 
测试项目|资源紧张情况下，不同类别用户进行保障速率业务
测试目的|验证SGSN能够对不同用户进行分级服务
预置条件|SGSN、HLR、RNC等工作正常，RNC带宽资源有限。分别为VIP用户和普通用户增加PIE参数。配置RAB指派流程的QoS参数。
测试过程|VIP用户和普通用户从RNC接入到SGSN。VIP用户和普通用户分别发起一个会话类PDP上下文激活流程。
通过准则|VIP用户能够成功激活一个会话类PDP上下文。普通用户收到RNC返回的RAB指派失败，原因为请求的最大上/下比特率不可用，SGSN重新发起RAB指派请求。
测试结果|无
非保障速率的用户业务
资源充足时用户进行非保障速率业务 
测试项目|资源充足情况下，用户进行非保障速率业务
测试目的|验证SGSN能够创建交互类或背景类PDP
预置条件|1.SGSN、HLR、BSC等工作正常，BSC带宽资源充足。
测试过程|用户从BSC接入到SGSN。用户发起一个交互类PDP上下文激活流程。
通过准则|用户能够成功激活一个交互类PDP上下文。
测试结果|无
资源紧张情况下，不同类别用户进行非保障速率业务 
测试项目|资源紧张情况下，不同类别用户进行非保障速率业务
测试目的|验证SGSN能够对不同用户进行分级服务
预置条件|SGSN、HLR、BSC等工作正常，BSC带宽资源有限分别为VIP用户和低端用户增加PIE参数。配置RAB指派流程的QoS参数。
测试过程|VIP用户和低端用户从BSC接入到SGSN。VIP用户和低端用户分别发起一个交互类PDP上下文激活流程。
通过准则|VIP用户能够成功激活一个交互类PDP上下文。低端用户收到RNC返回的RAB指派失败，原因为请求的最大上/下比特率不可用，SGSN重新发起RAB指派请求。
测试结果|无
常见问题处理 : 
问题描述|解决方法
---|---
协商后的QoS参数没有达到预期效果|QoS协商的总体原则是选取较差/低的服务质量。对于大部分参数来说就是在协商过程中取小值，除了以下参数：Reliabilityclass、Precedence class、Delay class、Delivery order、Maximum SDU size、Transferdelay、Traffic handling priority、Traffic class
## ZUF-77-11-002 SGSN本地Qos策略 
概述 : 
SGSN配置本地QoS控制策略用于进行QoS灵活控制。 
收益 : 
SGSN可灵活控制QoS。 
描述 : 
可在SGSN上配置各种本地QoS策略以进行QoS灵活控制： 
根据以下条件限制QoS上限： 
用户的IMSI号段 
用户的IMSI号段+接入模式（Iu接入或Gb接入） 
用户的IMSI号段+接入RNC的ID 
基于IMSI号段进行的签约QoS提升 
自动标识UE的QoS能力：如果MS没有接受网络侧协商的QoS，当PDP上下文被激活后，MS立即去激活PDP上下文，原因为“QoS
not accepted”。当PDP上下文被再次激活，SGSN自动将最大上下行速率降低到配置的范围内。 
根据不同GGSN局向进行QoS版本适配设置 
与RNC进行QoS协商 
灵活进网络侧和无线侧ARP和THR参数映射 
在如下流程中进行QoS重协商： 
路由区更新 
切换 
业务请求 
## ZUF-77-11-003 DSCP映射 
概述 : 
SGSN通过配置能力支持IP差别化服务（Diff-Serv）的QoS策略。 
收益 : 
通过SGSN在IP报文的头域插入“Diff-Serv Code Point”，本特性有助于保证发送正确QoS设置到外部网络和通过外部网络传输正确的QoS设置。 
描述 : 
SGSN提供配置参数用于在GTP控制信令消息和O&M消息中进行DSCP设置。  
SGSN提供配置参数用于在Gb接口的DL-NAS和DL-IPNS消息中进行DSCP设置。 
SGSN提供配置参数用于为基于QoS和ARP的用户面数据前转配置进行DSCP配置。 
SGSN为控制面和用户面分别设置DSCP参数值。 
对于用户面，SGSN根据业务QoS参数设置上下行数据链路的DSCP值。 
SGSN根据以下维度进行映射： 
业务类型+ARP 
业务类型+ARP 
业务类型+GBR 
业务类型+传输延迟 
对于控制面，SGSN为以下接口消息指定DSCP值： 
Gb下行层3信令 
Gb下行承载信令 
Gn接口信令包 
Ga接口 
ETSI LI1/ETSI LI2/ETSI LI3接口 
如果某个接口消息未配置DSCP值，该接口消息的DSCP值为0。 
## ZUF-77-11-004 R99/R98 QoS 
概述 : 
本特性根据业务类型建立不同业务质量的数据链路用于传输业务数据。  
收益 : 
可根据不同业务请求合理分配资源和提供业务质量保证。运营商通过使用承载设备可提供更多定制化业务以吸引用户。  
描述 : 
SGSN提供如下QoS支持功能： 
从MS发送QoS请求给SGSN； 
根据网络资源情况进行资源接管和控制，并为实时业务如通话和流媒体预留资源，从而保证QoS； 
监控用户数据，与服务层协议（SLA）保持一致，并进行流监控功能； 
分配共享资源给承载业务，以进行资源管理； 
按照相应的承载QoS业务容量，标记和进行业务映射功能；  
支持R99和R98 QoS属性； 
SGSN支持R4、R5、R6和R7 QoS。 
# 缩略语 
# 缩略语 
## ARP 
Allocation and Retention Priority分配保持优先级
## BSC 
Base Station Controller基站控制器
## CPU 
Central Processing Unit中央处理器
## DSCP 
Differentiated Services Code Point差分服务编码点
## DTI 
Digital Trunk Interface	数字中继接口板
FTP : 
File Transfer Protocol文件传输协议
## GBR 
Guaranteed Bit Rate保证比特率
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
GPRS : 
General Packet Radio Service通用无线分组数据业务
GTP : 
GPRS Tunneling ProtocolGPRS隧道协议
HLR : 
Home Location Register归属位置寄存器
HSS : 
Home Subscriber Server归属用户服务器
IMSI : 
International Mobile Subscriber Identity国际移动用户标识
LTE : 
Long Term Evolution长期演进
## MBR 
Maximum Bit Rate最大比特率
## MT 
Mobile Terminal移动终端
## NSAPI 
Network-layer
Service Access Point Identifier网络层业务接入点标识
PCC : 
Policy and Charging Control计费和策略控制
PCRF : 
Policy and Charging Rules Function策略和计费规则功能
## PDCP 
Packet Data Convergence Protocol分组数据收敛协议
PDP : 
Packet Data Protocol分组数据协议
QoS : 
Quality of Service服务质量
## RAB 
Radio Access Bearer无线接入承载
## RAI 
Routing Area Identity路由区标识
RAN : 
Radio Access Network无线接入网
RAT : 
Radio Access Technology无线接入技术
## RAU 
Routing Area Update路由区更新
RNC : 
Radio Network Controller无线网络控制器
## RRC 
Radio Resource Control无线资源控制
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
## SRNS 
Serving RNS服务无线网络子系统
## TEID 
Tunnel Endpoint Identifier隧道端点标识
## TFT 
Traffic Flow Template话务流量模型
## THP 
Traffic Handling Priority 业务处理优先级
## TI 
Transparent Interface透明接口
UE : 
User Equipment用户设备
## UMTS 
Universal Mobile Telecommunication System通用移动通讯系统
UTRAN : 
UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
## VIP 
Very Important Person贵宾
# ZUF-77-12 计费 
概述 : 
功能描述 : 
作为电信运营商的核心竞争力之一，计费系统反映了运营商的营收状态。SGSN网元计费功能主要为离线计费。离线计费为在会话、移动性业务或短消息业务使用过程中，SGSN收集计费信息，触发离线计费话单。SGSN把离线话单上传到CGF，计费不会实时影响业务执行。 
GPRS共有5种类型的离线计费话单(CDR)，即S-CDR、M-CDR、G-CDR、S-SMO-CDR、S-SMT-CDR，这五种话单除G-CDR由GGSN产生外，其他四种均由SGSN产生：
S-CDR：SGSN生成的针对PDP的话单，反映了无线资源的使用情况。 
G-CDR：GGSN生成的针对PDP的话单，反映了对外部数据网资源的使用状况。 
M-CDR：移动性管理话单，反映了系统在移动管理上的开销，可以通过数据配置决定是否产生该话单。 
SMS-CDR：包括S-SMO-CDR（短消息起呼话单）和S-SMT-CDR（短消息终呼话单），用于记录短消息发送的计费信息。 
LCS-CDR：LCS话单，用于记录LCS的计费信息。 
对于同一次PDP过程产生两种类型的话单S-CDR和G-CDR，计费中心一般根据G-CDR计算最终费用向用户收费，S-CDR主要用于进行统计、账单核对和漫游结算。 
功能特性简介 : 
针对用户的各种CDR，核心网提供了多种有效的解决方案。详细的解决方案特性参见下表。 
方案特性|实现简述|特导链接
---|---|---
S-CDR话单|S-CDR是SGSN生成的针对PDP的话单，反映了无线资源的使用情况。话单生成机制和话单信息符合3GPP 32.251协议。另外，SGSN支持基于PLMN计费特性的选择。|ZUF-77-12-001 S-CDR话单
M-CDR话单|M-CDR是移动性管理话单，反映了系统在移动管理上的开销，可以通过数据配置决定是否产生该话单。话单生成机制和话单信息符合3GPP 32.251协议。|ZUF-77-12-002 M-CDR话单
SMS-CDR话单|S-SMO-CDR是短消息起呼话单，用于记录短消息始发的计费信息。S-SMT-CDR是短消息终呼话单，用于记录短消息终结的计费信息。|ZUF-77-12-003 SMS-CDR话单
LCS-CDR话单|SGSN支持产生LCS-MT-CDR，LCS-MO-CDR，LCS-NI-CDR话单。SGSN支持基于全局过滤LCS-MO-CDR话单、LCS-MT-CDR话单、LCS-NI-CDR话单。|ZUF-77-12-004 LCS-CDR话单
话单缓存|SGSN支持通过Ga口输出话单到CG，当SGSN和CG之间连接中断时，SGSN支持话单缓存功能，等连接恢复后将缓存话单发送给CG，并和CG配合避免话单重复。|ZUF-77-12-005 话单缓存
## ZUF-77-12-001 S-CDR话单 
特性描述 : 
描述 
应用场景 
客户收益 
实现原理 
系统影响 
特性交互 
遵循标准 
特性能力 
可获得性 
O&M相关 
描述 : 
定义
作为电信运营商的核心竞争力之一，计费系统在某种程度上决定了一个电信运营商的兴衰成败。SGSN网元计费功能包括离线计费和在线计费。 
离线计费：在会话、移动性业务或短消息业务使用过程中，SGSN收集计费信息，触发离线计费话单。SGSN把离线话单上传到CGF，计费不会实时影响业务执行。 
在线计费：实时计费模式，在会话、移动性业务或短消息业务使用过程中，SGSN使用CAMEL技术与gsmSCF交互，通过在线计费系统对账户、余额、还有对应的资费信息，进行批价处理，完成在线信用控制交互。CAMEL业务在无线分组域包括GPRS交互和短消息业务。 
本文重点描述SGSN离线计费功能。 
GPRS共有5种类型的离线计费话单(CDR)，即S-CDR、M-CDR、G-CDR、S-SMO-CDR、S-SMT-CDR，这五种话单除G-CDR由GGSN产生外，其他四种均由SGSN产生： 
S-CDR：SGSN生成的针对PDP的话单，反映了无线资源的使用情况。 
G-CDR：GGSN生成的针对PDP的话单，反映了对外部数据网资源的使用状况。 
M-CDR：移动性管理话单，反映了系统在移动管理上的开销，可以通过数据配置决定是否产生该话单。 
S-SMO-CDR：短消息起呼话单，用于记录短消息始发的计费信息。 
S-SMT-CDR：短消息终呼话单，用于记录短消息终结的计费信息。 
对于同一次PDP过程产生两种类型的话单S-CDR和G-CDR，计费中心一般根据G-CDR计算最终费用向用户收费，S-CDR主要用于进行统计、账单核对和漫游结算。 
背景知识
运营商对分组域业务提出的运营管理要求是：分组域网络能够对其所支持的多种复杂的数据业务进行有效和及时的计费。运营商对计费的需求主要表现在后付费管理和预付费管理两个方面，SGSN离线计费功能满足后付费管理需求，SGSN在线计费功能满足预付费管理需求。 
分组域计费功能网络架构如下：[图1]
图1  分组域计费功能网络架构
分组域计费架构涉及接口： 
计费接口|说明
---|---
Ga接口|离线计费接口，是SGSN/GGSN到CGF的接口，主要用于向CGF提供计费记录。Ga接口采用GTP＇协议，GTP＇基于UDP的协议。SGSN可以同时连接多个CG，多个CG之间主备或负荷分担。
Ge接口|在线计费接口，用于gsmSCF控制某个gprsSSF的GPRS Session、PDP context和短消息。
原始的话单记录CDR在SGSN产生，但是SGSN并不能长久保存话单记录，因为话单记录量太大，于是引入计费网关CG。SGSN可以同时连接多个CG，实现CG间主备或负荷分担，提高了SGSN在计费方面的稳定性与灵活性。组网图如[图2]所示。
图2  SGSN和CG组网图
SGSN最多支持连接32个CG，对多个CG按照PLMN分组，最多支持分8组，实现不同PLMN采用不同CG进行不同的计费策略；每组内CG之间主备或者负荷分担。 
应用场景 : 
运营商的网络在向用户提供服务的同时需要记录用户对网络资源的占用情况，计费从本质上说是根据用户对网络资源的使用情况按照一定的规则计算费用。由于各种业务对网络资源的占用状况不同，因此其计费策略也不同。离线计费的计费策略主要包括： 
针对PDP的时间计费、流量计费和时间+流量计费。 
移动性管理计费。 
短消息业务计费。 
时间计费
以时间为标准计费，即根据用户上网时长作为计费标准。时间门限根据运营商的需要设定。 
运营商一般使用S-CDR进行账单核对或漫游结算等，对本地用户和漫游归属地接入的用户来说，S-CDR一般用于账单核对；对漫游拜访地接入的用户来说，S-CDR一般用于漫游结算。 
本地用户产生时间计费S-CDR应用场景图如图3所示。图3  本地用户产生时间计费S-CDR计费流程：本地用户在SGSN上附着或局间RAU时，SGSN成功接收HLR下发的用户的计费特性。IP-CAN承载在SGSN上成功激活后S-CDR打开，SGSN开始收集MS相关的IP-CAN承载计费数据。当时间门限到达S-CDR关闭，SGSN把S-CDR上传到本地CGF。GGSN产生G-CDR也上传到本地CGF，由本地CGF采集预处理后，送至本地计费中心做后续处理。本地计费中心对计费数据进行处理产生最终的计费账单。 
漫游用户归属地接入产生时间计费S-CDR应用场景图如图4所示。图4  漫游用户归属地接入产生时间计费S-CDR计费流程：漫游用户在漫游地SGSN上附着或局间RAU时，漫游地SGSN成功接收HLR下发的用户的计费特性。IP-CAN承载在漫游地SGSN上成功激活后S-CDR打开，漫游地SGSN开始收集MS相关的IP-CAN承载计费数据。当时间门限到达S-CDR关闭，漫游地SGSN把S-CDR上传到漫游地CGF，漫游地CGF采集预处理后，送至漫游地计费中心做后续处理。归属地GGSN产生G-CDR上传到归属地CGF，由归属地CGF采集预处理后，送至归属地计费中心做后续处理。漫游地计费中心将S-CDR送至归属地计费中心，最终S-CDR和G-CDR都由归属地的计费中心进行处理产生最终的计费账单。 
漫游用户拜访地接入产生时间计费S-CDR应用场景图如图5所示。图5  漫游用户拜访地接入产生时间计费S-CDR计费流程：漫游用户在漫游地SGSN上附着或局间RAU时，漫游地SGSN成功接收HLR下发的用户的计费特性。IP-CAN承载在漫游地SGSN上成功激活后S-CDR打开，漫游地SGSN开始收集MS相关的IP-CAN承载计费数据。当时间门限到达S-CDR关闭，漫游地SGSN把S-CDR上传到漫游地CGF。漫游地GGSN产生G-CDR也上传到漫游地CGF，由漫游地CGF采集预处理后，送至漫游地计费中心做后续处理。漫游地计费中心对计费数据进行处理产生最终的计费账单。 
流量计费
以流量为标准计费，即根据用户上网所下载的数据量和上传的数据量作为计费标准。在GPRS中，上、下行流量具备不对称性，所以分别计费。流量门限根据运营商的需要设定。 
GPRS支持多种QoS轮廓，其QoS体现在5个方面，即延时、可靠性、优先级、平均吞吐量及峰值吞吐量，每个方面都有一些可选等级。对流量的描述采取列表的形式，按照每种QoS轮廓分别统计数据量。 
注意：不同用户、不同业务对QoS的要求不同，而无线环境又是时变的，网络能够提供的QoS随用户使用情况、信道质量因素等诸多原因而具备不确定性，因此一次会话过程中的QoS轮廓会变化，每次变化就在列表中增加一项。 
运营商出于网络利用率和收益的考虑，在一天内不同的时段可以设置不同的费率，比如一天中网络比较空闲的时段，为了刺激用户消费，可以设置低费率，因此一次会话过程中费率可能会变化，SGSN按照不同的费率分别统计数据量。 
运营商一般使用S-CDR进行账单核对或漫游结算等，对本地用户和漫游归属地接入的用户来说，S-CDR一般用于账单核对；对漫游拜访地接入的用户来说，S-CDR一般用于漫游结算。 
本地用户产生流量计费S-CDR应用场景图如图6所示。图6  本地用户产生流量计费S-CDR计费流程：本地用户在SGSN上附着或局间RAU时，SGSN成功接收HLR下发的用户的计费特性。IP-CAN承载在SGSN上成功激活后S-CDR打开，SGSN开始收集MS相关的IP-CAN承载计费数据。当流量门限到达S-CDR关闭，SGSN把S-CDR上传到本地CGF。GGSN产生G-CDR也上传到本地CGF，由本地CGF采集预处理后，送至本地计费中心做后续处理。本地计费中心对计费数据进行处理产生最终的计费账单。 
漫游用户归属地接入产生流量计费S-CDR应用场景图如下图7所示。图7  漫游用户归属地接入产生流量计费S-CDR计费流程：漫游用户在漫游地SGSN上附着或局间RAU时，漫游地SGSN成功接收HLR下发的用户的计费特性。IP-CAN承载在漫游地SGSN上成功激活后S-CDR打开，漫游地SGSN开始收集MS相关的IP-CAN承载计费数据。当流量门限到达S-CDR关闭，漫游地SGSN把S-CDR上传到漫游地CGF，漫游地CGF采集预处理后，送至漫游地计费中心做后续处理。归属地GGSN产生G-CDR上传到归属地CGF，由归属地CGF采集预处理后，送至归属地计费中心做后续处理。漫游地计费中心将S-CDR送至归属地计费中心，最终S-CDR和G-CDR都由归属地的计费中心进行处理产生最终的计费账单。 
漫游用户拜访地接入产生流量计费S-CDR应用场景图如图8所示。图8  漫游用户拜访地接入产生流量计费S-CDR计费流程：漫游用户在漫游地SGSN上附着或局间RAU时，漫游地SGSN成功接收HLR下发的用户的计费特性。IP-CAN承载在漫游地SGSN上成功激活后S-CDR打开，漫游地SGSN开始收集MS相关的IP-CAN承载计费数据。当流量门限到达S-CDR关闭，漫游地SGSN把S-CDR上传到漫游地CGF。漫游地GGSN产生G-CDR也上传到漫游地CGF，由漫游地CGF采集预处理后，送至漫游地计费中心做后续处理。漫游地计费中心对计费数据进行处理产生最终的计费账单。 
时间+流量计费
GPRS采用分组交换技术，意味24h实时在线，用户可以随时从Internet上获取所需信息，因此以流量为计费标准较符合GPRS的特性；以时间为计费标准显然限制了用户对GPRS的使用，GPRS的优越性得不到发挥。但仅仅已流量为计费标准，不利用运营商对用户提供多样的套餐和开展优惠打折活动，因此时间+流量的计费方式更适合运营商多样的计费需求，在现网比较常用。 
对本地用户和漫游用户，时间+流量的计费流程同上面两节描述，区别是当流量或时间门限到达S-CDR关闭，SGSN把S-CDR上传到CGF。 
针对以上三节，注： 
对于GPRS而言，通信过程用一次PDP上下文来描述。对于一次PDP上下文过程，同时存在S-CDR和G-CDR，而且由于数据通信持续时间长、包含的情况复杂，因此在GPRS业务节点（GSN）上一次会话会产生多个部分记录（Partial
Record），描述一次PDP上下文的多个记录需要一个标识符号来表示属于一次会话，这个标识符号就是Charging ID。Charging
ID在SGSN与GGSN之间建立PDP上下文的过程中确定下来，这样保证了一次会话S-CDR与G-CDR的关联性。 
移动性管理计费
手机移动可能引发位置更新、越区切换甚至越局切换，因此GPRS系统会在移动性管理上花费系统许多开销。M-CDR反映了系统在移动管理上的开销，GPRS的M-CDR中有一项Change
of Location，用于记录手机所经历的RAI，即一旦发生路由区域更新，就记录相应的RAI。 
当运营商需要为手机移动引发的位置更新和切换加收服务费用或收集与MS相关的移动性管理数据时，可以通过数据配置决定产生M-CDR。 
MS在SGSN上成功附着后M-CDR打开，SGSN开始收集与MS相关的移动性管理数据；当GPRS分离、SGSN改变、异常释放、时间门限到达、移动改变达到最大次数、网管强制或局内跨RAT流程等条件下M-CDR关闭，SGSN把M-CDR上传到CGF；CGF采集预处理后提交计费中心。 
短消息计费
当MS通过SGSN收发短消息时，运营商需要通过SGSN产生的短消息话单进行短消息计费。 
短消息话单包括S-SMO-CDR和S-SMT-CDR： 
MS通过SGSN发送一条短消息时在SGSN上产生S-SMO-CDR。 
MS通过SGSN接收一条短消息时在SGSN上产生S-SMT-CDR。 
客户收益 : 
受益方|受益描述
---|---
运营商|提供精准的原始计费数据和多样的计费策略（如：时间计费、流量计费、时间+流量计费等，同时体现QoS改变和费率改变），运营商据此对用户多种复杂的数据业务进行有效和及时计费，同时便于运营商设计计费方案，为用户提供各种优惠套餐，以此大幅提升用户忠诚度，增加网络运营收益。
移动用户|为用户提供精准的原始计费数据，保护业务用户的经济利益。用户通过优惠套餐选择，享受约定的优惠政策。
实现原理 : 
涉及的网元
SGSN网元离线计费功能由HLR、SGSN、CGF、计费中心、SMS-GMSC和SMSC配合完成。 
网元|功能
---|---
HLR|负责存储用户签约的计费特性，包括热计费、平率计费、预付费计费和普通计费。
SGSN|处理移动性管理、会话和短消息业务，SGSN从HLR接收用户的计费特性信息。在处理业务的过程中，SGSN打开各种CDR，满足一定话单关闭条件下关闭CDR，把CDR上传到CGF。
CGF|完成对于部分话单的第一级合并，减少了CGF与计费中心间的带宽要求，减轻了计费中心的处理负担。负责收集SGSN的计费数据；对计费数据进行较长时间的保存并进行合并分拣等预处理工作；并负责将收集到的计费数据送往计费中心。
计费中心 (Billing System)|负责对计费数据进行处理产生最终的计费账单，计费中心主要有以下功能：采集话单；根据话单计算出费用，进行话单的完全合并(第二级合并)，并进行话单正确性检查。
SMS-GMSC|负责短消息中心的短消息转发，根据HLR返回的路由信息，将短信转发到目的SGSN上。
SMSC|负责发送端的短消息业务接收，存储，转发投递到对应的短信网关SMS-GMSC上。
业务流程
SGSN网元计费功能涉及如下业务流程： 
SGSN产生S-CDR。 
SGSN产生M-CDR。 
SGSN产生SMS-CDR。 
SGSN产生S-CDR
流程图如[图9]所示。
图9  SGSN产生S-CDR
流程描述： 
用户在SGSN上附着或局间RAU时，SGSN成功接收HLR下发的用户的计费特性。 
MS向SGSN发送Activate PDP Context Request消息，请求激活PDP上下文；IP-CAN承载在SGSN上成功激活后S-CDR打开，SGSN开始收集MS相关的IP-CAN承载计费数据。 
话单关闭情况1：MS或SGSN发送Deactivate PDP Context Request消息，请求去活PDP上下文；SGSN去激活IP-CAN承载成功后关闭S-CDR关闭，把S-CDR上传到CGF。 
话单关闭情况2：MS发生了局间RAU，老局SGSN处理RAU完成后关闭S-CDR，把S-CDR上传到CGF。 
话单关闭情况3：SGSN发生了任意的异常释放，关闭S-CDR，把S-CDR上传到CGF。 
话单关闭情况4：MS的话单流量门限达到后，SGSN关闭S-CDR，把S-CDR上传到CGF。 
话单关闭情况5：MS的话单时间门限达到后，SGSN关闭S-CDR，把S-CDR上传到CGF。 
话单关闭情况6：MS的Qos改变次数或话单费率切换次数达到最大值，SGSN关闭S-CDR，把S-CDR上传到CGF。 
话单关闭情况7：网管发送强制输出话单消息给SGSN，SGSN关闭S-CDR，把S-CDR上传到CGF。 
话单关闭情况8：MS发生局内2/3G间的切换/RAU，SGSN切换完成/RAU完成后关闭S-CDR，把S-CDR上传到CGF。 
CGF收集S-CDR计费数据，对计费数据进行较长时间的保存并进行合并分拣等预处理工作。CGF将收集到的计费数据送往计费中心；计费中心对计费数据进行处理产生最终的计费账单。 
SGSN产生M-CDR
流程图如[图10]所示。
图10  SGSN产生M-CDR流程
流程描述： 
用户在SGSN上附着或局间RAU时，SGSN成功接收HLR下发的用户的计费特性。MS在SGSN上附着成功后M-CDR打开，SGSN开始收集MS相关的移动性管理数据。 
话单关闭情况1：MS或SGSN发送Detach Request消息，请求分离，SGSN分离用户成功后关闭M-CDR关闭，把M-CDR上传到CGF。 
话单关闭情况2：MS发生了局间RAU，老局SGSN处理RAU完成后关闭M-CDR，把M-CDR上传到CGF。 
话单关闭情况3：SGSN发生了任意的异常释放，关闭M-CDR，把M-CDR上传到CGF。 
话单关闭情况4：MS的话单时间门限达到后，SGSN关闭M-CDR，把M-CDR上传到CGF。 
话单关闭情况5：MS移动改变次数达到最大值，SGSN关闭M-CDR，把M-CDR上传到CGF。 
话单关闭情况6：网管发送强制输出话单消息给SGSN，SGSN关闭M-CDR，把M-CDR上传到CGF。 
话单关闭情况7：MS发生局内2/3G间的切换/RAU，SGSN切换完成/RAU完成后关闭M-CDR，把M-CDR上传到CGF。 
CGF收集M-CDR计费数据，对计费数据进行较长时间的保存并进行合并分拣等预处理工作。CGF将收集到的计费数据送往计费中心；计费中心对计费数据进行处理产生最终的计费账单。 
SGSN产生SMS-CDR
SGSN产生S-SMO-CDR流程图如图11所示。图11  SGSN产生S-SMO-CDR流程描述：始呼短消息发送成功后SGSN产生SMS-SMO-CDR话单，把SMS-SMO-CDR上传到CGF；CGF收集SMS-SMO-CDR计费数据，对计费数据进行较长时间的保存并进行合并分拣等预处理工作。CGF将收集到的计费数据送往计费中心；计费中心对计费数据进行处理产生最终的计费账单。 
SGSN产生S-SMT-CDR流程图如图12所示。图12  SGSN产生S-SMT-CDR流程流程描述：终呼短消息接收成功后SGSN产生SMS-SMT-CDR话单，把SMS-SMT-CDR上传到CGF；CGF收集SMS-SMT-CDR计费数据，对计费数据进行较长时间的保存并进行合并分拣等预处理工作。CGF将收集到的计费数据送往计费中心；计费中心对计费数据进行处理产生最终的计费账单。 
系统影响 : 
随着在线用户数的增加，系统资源占用会一直增大，CPU占用率会相应上升。 
特性交互 : 
业务|交互
---|---
DT功能|DT时SGSN输出的S-CDR无流量。
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060: " General Packet Radio Service (GPRS) ; Service
description; Stage 2". 
3GPP TS 32.251: " Charging management; Packet Switched (PS)
domain charging." 
3GPP TS 23.078: "Customised Applications for Mobile network
Enhanced Logic (CAMEL) Phase 3; Stage 2". 
特性能力 : 
特性|能力
---|---
话单处理能力|全局最大话单处理能力6000条/秒
多CG连接|SGSN最多支持连接32个CG
对其他网元的要求
SGSN网元计费功能由HLR、SGSN、CGF、计费中心、SMS-GMSC和SMSC配合完成。 
工程规划要求
SGSN连接多个CG，多个CG按照PLMN分组，每组内CG之间主备或者负荷分担，不同PLMN采用不同CG进行不同的计费策略。 
O&M相关 : 
命令
新增配置项参见表4。表4  新增配置项配置项命令Ga接口管理SET LOCAL GAINFOADD CGCFGADD CGPROFILEADD CGPLMNSET SINGLE ADDRSET CDR NODEID容量配置SET CAPACITYAPN计费模板配置ADD APNCTPLSET APNCTPL RATEADD GPRS APNADD DNSAPNCHGSET CDR TIME缺省计费特性配置SET CHGCHAR DEFAULT多网号用户计费特性配置ADD CHGCHAR PLMNCDR过滤配置SET CDRFLT分组域参数配置SET PACKET DOMAIN PARAMETERMCDR配置SET MCDR 
业务观察/失败观察
OMC控制出MCR使用命令REL MCDR输出某IMSI用户的MCDR。 
OMC控制出SCDR使用命令REL SCDR输出某IMSI用户的MCDR。 
保存MP缓存中的CDR使用命令SAVE CDR保存某SMP模块缓存中的CDR到A文件。 
发送CDR使用命令SEND CDR将积压话单传递给CG。 
停止发送CDR使用命令NO SEND CDR停止将积压话单传递给CG。 
特性配置 : 
GnGp SGSN网元计费功能配置特性 
调整特性 
测试用例 
#### GnGp SGSN网元计费功能配置特性 
配置说明
CG容量配置
使用命令[SET CAPACITY]配置全局容量规划中的CG服务器个数。
Ga接口配置
使用命令[SET LOCAL GAINFO]配置本地Ga接口相关信息。
使用命令[ADD CGCFG]配置CG服务器。
使用命令[ADD CGPROFILE]配置CG profile。
使用命令[ADD CGPLMN]配置某PLMN用户使用的CG
profile。
使用命令[SET SINGLE ADDR]配置本端单地址。
使用命令[SET CDR NODEID]配置话单NODE ID。
计费模板配置
使用命令[ADD APNCTPL]配置APN计费模板。
使用命令[SET APNCTPL RATE]，配置计费模板的费率时段。
使用命令[ADD GPRS APN]，配置APN对应的计费模板。
使用命令[ADD DNSAPNCHG]，配置DNS解析的APN对应的计费模板。
使用命令[SET CDR TIME]，配置Ga接口基本参数。
计费特性配置
使用命令[SET CHGCHAR DEFAULT]设置缺省计费特性。
使用命令[SET CHGCHAR PLMN]配置多网号计费特性。
话单过滤配置
使用命令[SET CDRFLT]设置CDR过滤。
根据APN过滤SCDR
使用命令[SET PACKET DOMAIN PARAMETER]设置是否支持根据APN过滤SCDR。
使用命令[ADD GPRS APN]设置本地解析的APN是否过滤SCDR。
使用命令[ADD DNSAPNCHG]配置DNS解析的APN是否过滤SCDR。
根据IMSI过滤CDR配置
使用命令[SET PACKET DOMAIN PARAMETER]设置是否支持根据IMSI过滤CDR。
使用命令[ADD IMSI CDR FILTER]设置按照IMSI号段过滤CDR。
MCDR出单配置
使用命令[SET MCDR]设置MCDR出单参数。
例如：SET MCDR:TIMELMT=360,MCLMT=4; 
配置前提
已获知和SGSN对接的CG数量和IP地址等详细信息。 
CG主备配置。 
配置过程
根据现场需要配置支持的CG个数； 
配置Ga接口； 
配置计费模板（可选，有系统默认的计费模板）。 
配置实例
时间计费
配置步骤|配置说明
---|---
SET CGCFG:ID=1,CGADDR="40.2.136.32",CGPORT=3386|配置使用的主CG服务器地址和端口号
ADD CGCFG:ID=2,CGADDR="40.2.136.33",CGPORT=3386|配置使用的备CG服务器地址和端口号
ADD CGPROFILE:PROFILEID=1,CGSERVER=1-1-500&2-1-500|配置CG PROFILE
SET SINGLE ADDR:LOCALADDR="192.20.118.3",VRF=51|配置本端与CG通信的地址
ADD APNCTPL:TPLID=1,TYPE="TIME",TIMELMT=5|配置计费模板(可选，系统默认就有计费模板0，使用时间流量计费模式)
ADD GPRS APN:APN="zte.com.mnc011.mcc460.gprs",CTPLID=1|配置APN对应的计费模板
流量计费
配置步骤|配置说明
---|---
SET CGCFG:ID=1,CGADDR="40.2.136.32",CGPORT=3386|配置使用的主CG服务器地址和端口号
ADD CGCFG:ID=2,CGADDR="40.2.136.33",CGPORT=3386|配置使用的备CG服务器地址和端口号
ADD CGPROFILE:PROFILEID=0,CGSERVER='1"-"1"-"500"&"2"-"1"-"500"|配置CG PROFILE
SET SINGLE ADDR:LOCALADDR="192.20.118.3",VRF=51|配置本端与CG通信的地址
ADD APNCTPL:TPLID=2,TYPE="FLOW",,TIMELMT=60,FLOWLMT=204800|配置计费模板(可选，系统默认就有计费模板0，使用时间流量计费模式)
ADD GPRS APN:APN="zte.com.mnc011.mcc460.gprs",CTPLID=2|配置APN对应的计费模板
时间+流量计费
配置步骤|配置说明
---|---
SET CGCFG:ID=1,CGADDR="40.2.136.32",CGPORT=3386|配置使用的主CG服务器地址和端口号
ADD CGCFG:ID=2,CGADDR="40.2.136.33",CGPORT=3386|配置使用的备CG服务器地址和端口号
ADD CGPROFILE:PROFILEID=0,CGSERVER="1"-"1"-"500"&"2"-"1"-"500"|配置CG PROFILE
SET SINGLE ADDR:LOCALADDR="192.20.118.3",VRF=51;|配置本端与CG通信的地址
ADD APNCTPL:TPLID=3,TYPE="TIMEFLOW",TIMELMT=5,FLOWLMT=204800;|配置计费模板(可选，系统默认就有计费模板0，使用时间流量计费模式)
ADD GPRS APN:APN="zte.com.mnc011.mcc460.gprs",IPADDR="0.0.0.0",CTPLID=3;|配置APN对应的计费模板
移动性管理计费
配置步骤|配置说明
---|---
SET CGCFG:ID=1,CGADDR="40.2.136.32",CGPORT=3386;|配置使用的主CG服务器地址和端口号
ADD CGCFG:ID=2,CGADDR="40.2.136.33",CGPORT=3386;|配置使用的备CG服务器地址和端口号
ADD CGPROFILE:PROFILEID=0,CGSERVER='1'-'1'-'500'&'2'-'1'-'500'|配置CG PROFILE
SET SINGLE ADDR:LOCALADDR="192.20.118.3",VRF=51|配置本端与CG通信的地址
短消息计费
配置步骤|配置说明
---|---
SET CGCFG:ID=1,CGADDR="40.2.136.32",CGPORT=3386|配置使用的主CG服务器地址和端口号
ADD CGCFG:ID=2,CGADDR="40.2.136.33",CGPORT=3386|配置使用的备CG服务器地址和端口号
ADD CGPROFILE:PROFILEID=0,CGSERVER='1'-'1'-'500'&'2'-'1'-'500'|配置CG PROFILE
SET SINGLE ADDR:LOCALADDR="192.20.118.3",VRF=51|配置本端与CG通信的地址
调整特性 : 
如需针对某PLMN用户使用特定的CG PROFILE，则按照配置说明一节进行配置。 
如需使用话单过滤功能，则按照配置说明中的对应章节进行配置。 
测试用例 : 
时间计费 
测试项目|时间计费
测试目的|能够按照时间门限产生SCDR
预置条件|Ga口链路通，已经配置好计费模板，且模板中是时间计费模式。
测试过程|用户附着，激活PDP。
通过准则|当PDP激活达到计费模板中配置的时间门限，则SGSN生成SCDR话单，并通过Ga口传递给CG。
流量计费 
测试项目|流量计费
测试目的|能够按照流量门限产生SCDR
预置条件|Ga口链路通，已经配置好计费模板，且模板中是流量计费模式。
测试过程|用户附着，激活PDP，有用户面数据。
通过准则|当用户面上下行流量和达到计费模板中配置的流量门限，则SGSN生成SCDR话单，并通过Ga口传递给CG。
时间+流量计费 
测试项目|时间+流量计费
测试目的|能够按照时间+流量门限产生SCDR
预置条件|Ga口链路通，已经配置好计费模板，且模板中是时间流量计费模式。
测试过程|用户附着，激活PDP，有用户面数据。
通过准则|当PDP激活达到计费模板中配置的时间门限或者上下行流量和达到计费模板中配置的流量门限，则SGSN生成SCDR话单，并通过Ga口传递给CG。
移动性管理计费 
测试项目|移动性管理计费
测试目的|能够产生MCDR
预置条件|Ga口链路通
测试过程|用户附着。用户发起局内RAU，从一个RAC到另外一个RAC。用户分离。
通过准则|当用户分离时SGSN生成MCDR，并记录两个RAC，MCDR通过Ga口传递给CG。
短消息计费 
测试项目|短消息计费
测试目的|能够产生SMSCDR
预置条件|Ga口链路通
测试过程|用户附着。发送和接收短信成功。
通过准则|SGSN生成SMS-SMO和SMS-SMT CDR，并通过Ga口传递给CG。
## ZUF-77-12-002 M-CDR话单 
概述 : 
M-CDR话单，即移动管理话单，显示系统在移动管理上的开销，并且该话单的生成取决于数据配置。SGSN根据各种条件为用户生成M-CDR话单。 
收益 : 
本特性用于数据业务计费。 
描述 : 
M-CDR话单显示系统在移动管理上的开销。该话单的生成取决于数据配置。M-CDR话单生成策略如下： 
移动变化话单 
时间阈值话单 
系统间变化话单 
NM mandatory CDR（网管强制话单） 
SGSN根据以下策略过滤M-CDR话单： 
基于PLMN 
基于全局配置 
## ZUF-77-12-003 SMS-CDR话单 
概述 : 
SGSN为PS域的短信始呼和终呼业务生成SMS-CDR话单。 
收益 : 
本特性用于短信业务计费。 
描述 : 
短信始呼话单（S-SMO-CDR）用于记录短信始呼的计费信息。短信终呼话单（S-SMT-CDR）用于记录短信终呼的计费信息。 
SGSN根据以下策略过滤S-SMO-CDR话单和S-SMT-CDR话单： 
基于PLMN 
基于全局配置 
## ZUF-77-12-004 LCS-CDR话单 
概述 : 
LCS-CDR指的是定位业务话单。 
收益 : 
本特性用于定位业务计费。 
描述 : 
SGSN支持生成LCS-MT-CDR话单、LCS-MO-CDR话单和LCS-NI-CDR话单。 
SGSN支持基于全局配置过滤LCS-MT-CDR话单、LCS-MO-CDR话单和LCS-NI-CDR话单。 
## ZUF-77-12-005 话单缓存 
概述 : 
ZXUN uMAC自动缓存由于链路故障而发送失败的用户话单。 
收益 : 
本特性可防止由于计费链路断开而造成的话单丢失，从而确保计费信息的准确性。 
描述 : 
话单可在线保存7天以上。话单存储能力可根据特定要求进行配置。  
# ZUF-77-13 会话管理扩展功能 
概述 : 
功能描述 : 
SGSN的会话管理功能，除了提供PDP上下文的激活、修改、去激活等基本功能外，还提供了扩展功能，包括：SGSN支持非活跃用户分离、长时间无流量释放RAB。 
功能特性简介 : 
会话管理扩展功能详细的特性如下表： 
方案特性|实现简述|特导链接
---|---|---
SGSN支持非活跃用户分离|SGSN支持对于长时间没有流量的用户进行PDP去激活，非活跃时长可基于APN配置。|ZUF-77-13-001 SGSN支持非活跃用户分离
长时间无流量释放RAB|SGSN支持对于长时间无流量的PDP，释放RAB，从而释放空口资源。无流量时长可基于APN配置。|ZUF-77-13-002 长时间无流量释放RAB
## ZUF-77-13-001 SGSN支持非活跃用户分离 
概述 : 
SGSN可检测已附着但长时间处于非活动状态的用户，或已被激活但长时间无数据传输的用户。对于这些用户，SGSN在网络侧发起去激活或分离操作。 
收益 : 
本特性提供以下收益： 
从SGSN移除非活动用户。 
降低网络负荷，保障网络有效运行。 
节省无线信道的带宽资源，使活动用户获得更多无线资源。 
描述 : 
通过配置，SGSN可确定非活动用户的时长参数。如果SGSN发现用户在定时器设置的周期内无数据传输，SGSN在网络侧发起去激活操作以删除用户的PDP上下文。时长参数可根据APN进行配置。当用户已附着到网络但在设置时长内未激活，网络侧发起分离流程将用户从GPRS网络移除，从而减少周期性路由更新以及避免不必要的信令（如路由更新）占用带宽资源。 
SGSN也可在PLMN配置基础上支持该特性。 
## ZUF-77-13-002 长时间无流量释放RAB 
概述 : 
当UE接入SGSN后长时间没有数据帧，SGSN可释放相关PDP的RAB，从而释放无线资源。 
收益 : 
本特性节省无线资源。 
描述 : 
当UE接入SGSN并激活后，该UE长时间没有数据帧。当时长超过设置的阈值时，SGSN释放RAB资源，从而释放无线资源。如果该RAB是UE唯一一个RAB，SGSN发起Iu释放，并释放Iu连接。 
# ZUF-77-14 语音与短信 
概述 : 
功能描述 : 
语音是短消息是最基础的通信功能。 
用户在GPRS网络接入时，语音一般由CS域提供。在EPS网络引入后，用户可同时在CS域和EPS域提供语音业务。当用户作为被叫，SGSN需配合HSS发起的T-ADS查询，便于对语音进行选择。
短消息 
用户在GPRS网络接入时，短消息可以经由CS域投递，也可以由PS域投递。由PS域投递时，SGSN与SMSC直连，SGSN透传UE和SMSC间短消息。
功能特性简介 : 
针对语音和短信的应用特点和应用场景，核心网为满足用户的可靠语音和短信的要求，提供了有效的解决方案。详细的解决方案特性如下表： 
方案特性|实现简述|特导链接
---|---|---
T-ADS功能|用户可同时注册在CS和PS域，当语音呼叫此用户时，HLR向SGSN发送PSI请求，请求用户上下文信息（是否支持VOPS，最近活动时间，所在的RAT类型），SGSN通过PSI响应返回以上信息，以便网络判断走CS语音还是PS语音。|ZUF-77-14-001 T-ADS功能
短消息|SGSN支持短消息业务。具体参见3GPP 23040协议。|ZUF-77-14-002 短信业务
## ZUF-77-14-001 T-ADS功能 
概述 : 
用户可同时在CS域和PS域注册。当用户有入呼时，HLR发送PSI请求给SGSN以获取用户信息（包括是否支持VoPS、最近活动时间和所在RAT类型）。SGSN发送携带用户信息的PSI响应，由网络决定是否提供CS域语音业务或PS域语音业务。 
收益 : 
通过本特性，网络可决定是否提供CS域语音业务或PS域语音业务，从而节省网络资源。 
描述 : 
用户可同时在CS域和PS域注册。当用户有入呼时，HLR发送PSI请求给SGSN以获取用户信息（包括是否支持VoPS、最近活动时间和所在RAT类型）。SGSN发送携带用户信息的PSI响应，由网络决定是否提供CS域语音业务或PS域语音业务。 
## ZUF-77-14-002 短信业务 
概述 : 
本特性使短消息可通过PS网络传输。 
收益 : 
通过本特性，短消息可在PS网络上传输，从而节省无线资源。 
描述 : 
SGSN支持短信业务。 
# ZUF-77-15 位置相关业务 
概述 : 
功能描述 : 
在移动网络中，用户位置信息包括RAI、CGI和地理位置信息等。SGSN从无线侧获得位置信息后可传递给核心网的其他网元。
与用户位置信息相关的应用包括： 
基于用户所在位置对用户采用不同的控制策略（比如计费策略、接入控制等）。 
通过用户所在位置为用户提供更好的服务（比如救援、导航、与位置相关的增值服务）。 
功能特性简介 : 
针对用户的应用需求，SGSN支持多种位置相关功能。详细的解决方案参见下表。 
方案特性|实现简述|特导链接
---|---|---
位置信息上报|由于某些业务（比如紧急呼叫、计费等）需要用户位置信息，GGSN指示SGSN上报位置信息。SGSN在进行附着/RAU/业务请求时，检测出用户所在的CGI/SAI或RAI发生变化时，则在Create PDP Context Request、Update PDP Request或MS Info Change Reporting Messages消息中携带新CGI/SAI/RAI给GGSN。位置信息上报功能参见3GPP 29060协议的“7.5B.1 MS Info Change Reporting Messages”章节。|ZUF-77-15-001 位置信息上报
Iu口小区位置信息上报|SGSN下发Location Report Control通知RNC，当用户所在SAI发生变化时，RNC上报Location Report通知SGSN。此功能将增加RNC和SGSN之间的信令负荷。Iu口小区位置上报功能参见3GPP 23060协议的“12.7.5 Location Reporting Procedure”章节。|ZUF-77-15-002 Iu口小区位置信息上报
Gb口小区信息上报|SGSN在消息中指示BSS，当用户所在小区发生变化时，BSS发送LLC空帧携带最新的小区通知SGSN，SGSN记录最新的小区。此功能将增加BSS和SGSN之间的信令负荷。Gb口小区更新功能参见3GPP 23060协议的"6.9.1.1 Cell Update Procedure章节。|ZUF-77-15-003 Gb口小区信息上报
LCS|SGSN支持定位业务。MS或网络侧获得MS当前所在的位置信息。定位类型可分为：UE起呼的立即定位（不支持周期性定位） UE终呼的立即定位延迟定位（不支持周期性定位）定位业务可参见3GPP 23.271协议的“9.1.6 Packet Switched Mobile Terminating Location Request(PS-MT-LR)”、“9.1.8 Mobile Terminating Deferred Location Request – UE available event”和“9.1.9 Deferred Location Request Procedure for the change of area event”章节。|ZUF-77-15-004 LCS
## ZUF-77-15-001 位置信息上报 
概述 : 
SGSN向GGSN上报用户位置信息。 
收益 : 
GGSN可获取用户位置信息。 
描述 : 
当某些业务如紧急呼叫、监测和计费等需要用户位置信息时，GGSN通知SGSN上报位置信息。当GGSN不再需要位置信息时，GGSN通知SGSN停止上报。 
当处理附着、RAU或业务请求时，发现用户所处位置的SAI或RAI发生变化，SGSN通过Create PDP Context Request消息、Update PDP Request消息或MS Info Change Reporting消息携带新SAI或RAI给GGSN。 
上报位置信息变化的粒度可分为： 
根据CGI/SAI的变化来上报 
根据RAI的变化来上报 
## ZUF-77-15-002 Iu口小区位置信息上报 
概述 : 
SGSN需要RNC向其上报用户SAI变化信息。 
收益 : 
在3G网络，SGSN可获取用户最新的SAI信息。 
描述 : 
通过本特性，RNC一发现用户SAI发生变化就向SGSN报告该信息。 
SGSN发送Location Report Control消息给RNC。当用户SAI发生变化，RNC发送Location Report消息给SGSN。 
本特性会显著增加RNC和SGSN之间的信令负荷。 
## ZUF-77-15-003 Gb口小区信息上报 
概述 : 
SGSN需要BSS向其上报用户小区变化信息。 
收益 : 
在2G网络，SGSN可获取用户最新的小区信息。 
描述 : 
通过本特性，BSS一发现用户小区发生变化就向SGSN报告该信息。 
SGSN向BSS发送消息，通知BSS如果发现用户小区发生变化，就向其发送携带有用户最新小区信息的LLC空帧。SGSN记录最新的小区信息。 
本特性会显著增加BSS和SGSN之间的信令负荷。 
## ZUF-77-15-004 LCS 
特性描述 : 
摘要术语描述应用场景客户收益实现原理系统影响遵循标准特性能力O&M相关 
术语 : 
术语|含义
---|---
LCS|定位业务，指定位到终端所在的地理位置，以及由此所关联的业务。
Lg|SGSN到GMLC之间的接口。
描述 : 
定义
LCS（定位业务）是一种提供移动用户位置信息的业务。提供的位置信息可以被网络内部使用，也可以被第三方使用。
LCS涉及的实体包括LCS服务方、LCS客户方、以及被定位的目标用户。 
背景知识
LCS业务的网络模型图如[图1]。
图1  LCS业务的网络模型图
应用场景 : 
该功能典型的应用包括： 
用于网络内部使用，如改善网络运行性能、网络维护、支持补充业务、支持移动智能业务等。用于商用的增值业务。如根据用户当前位置给予向导服务。 
用于紧急呼叫时确定起呼用户位置。 
用于经批准的安全部门跟踪用户位置。 
客户收益 : 
受益方|受益描述
---|---
运营商|支持LCS业务，吸引用户加入。
移动用户|适用LCS业务。
实现原理 : 
涉及的网元
LCS业务的实现需要HLR、GMLC、SGSN、RNC等的共同配合。
HLR主要是存储用户的LCS签约信息，同时把用户拜访的SGSN提供给GMLC。 
GMLC主要是发起用户的定位。 
SGSN主要是完成各种信令的处理，以及数据的传递。 
业务流程
UE被动的定位流程如[图2]所示。
图2  UE被动的定位流程图
流程说明： 
外部的LCS客户端发起定位请求，消息发送给R-GMLC。消息中包括MSISDN（或者IMSI或者UE假名）和LCS 的Qos。对于呼叫相关的定位，还包括被叫号码；会话相关的定位，包括APN-NI。消息中还需要带LCS的Service
ID，用于R-GMLC的客户端合法性检查。消息中有可能带H-GMLC的地址，如果没有，R-GMLC需要从网元PMD中读取。 
如果R-GMLC没有H-GMLC的地址，则发SEND_ROUTING_INFO_FOR_LCS到HSS要H-GMLC的地址；如果有H-GMLC的地址，则跳过此步骤。 
HSS返回SGSN的信息、H-GMLC的地址、IMSI/MSISDN、V-GMLC的地址、PPR的地址等信息。 
如果R-GMLC和H-GMLC属于不同的网元，则R-GMLC发送定位请求给H-GMLC。 
隐私检查。在H-GMLC完成，或者通知PPR完成。 
如果H-GMLC不知道用户的IMSI/MSISDN、V-GMLC的地址、SGSN的地址等，则发SEND_ROUTING_INFO_FOR_LCS到HSS；如果知道上述的信息，则跳过此步。 
HSS返回SGSN的信息、H-GMLC的地址、IMSI/MSISDN、V-GMLC的地址、PPR的地址等信息。 
如果H-GMLC不知道V-GMLC的地址，或者H-GMLC与V-GMLC相同，或者运营商的要求，H-GMLC无需发消息给V-GMLC；否则H-GMLC发定位请求给V-GMLC。 
被动定位过程。 
V-GMLC回复定位响应给H-GMLC。 
隐私检查。 
如果隐私检查判断需要通知信息，则H-GMLC发定位请求给V-GMLC，同时指明仅仅是通知。 
通知发送过程。 
V-GMLC回复定位响应给H-GMLC。 
H-GMLC回复定位响应给R-GMLC。 
R-GMLC回复定位响应给LCS客户端。 
普通的立即定位
普通的立即定位的流程如[图3]所示。
图3  普通的立即定位流程图
流程说明： 
LCS的客户端发起定位请求，GMLC发送Provide Subscriber Location消息给SGSN。消息携带IMSI、定位的类型、LCS的Qos、APN-NI等。 
SGSN收到此消息后，先鉴权接入的GMLC是否合法：其他PLNM的GMLC或者其他国家的GMLC，如果不支持，则回复错误。如果PSL消息指示了隐私相关的动作，SGSN需要读取隐私相关的动作。如果PSL消息没有隐私相关的动作，则SGSN需要根据用户的Profile来拦截LCS的客户端，如果在拦截之列，则回复错误响应给GMLC。否则，如果UE出于空闲态，在发起寻呼的流程以及安全流程。 
如果用户的隐私要求通知UE，SGSN发送LCS Location Notification Invoke给用户，消息中包含LCS客户端类型、LCS的名称等。SGSN可以无须等待LCS
Location Notification Return Result的响应消息，并行发起location request给RAN。 
UE判断和鉴权是否允许定位。如果不允许，SGSN回复错误的响应给GMLC。 
SGSN发送Location Request消息给RAN，消息中包括定位类型、QoS以及其他参数。 
RAN计算出UE的位置信息。 
RAN回复响应消息给SGSN，指明是否定位成功。如果不成功，携带失败原因。 
如果SGSN没有进行隐私检查过程，则回复定位的响应给GMLC，包括位置信息、生存期等信息。否则，在收到UE的隐私检查允许时，仅回复位置信息和计算方法给GMLC。如果UE的隐私检查拒绝，SGSN回复失败响应给GMLC。如果定位过程失败，但隐私检查通过，同时LCS客户端要求了当前或者最后的位置信息，则SGSN把此信息发送给GMLC。 
LCS客户端发起的UE可达的延迟定位
LCS客户端发起的UE可达的延迟定位的流程如[图4]所示。
图4  LCS客户端发起的UE可达的延迟定位的流程图
流程说明： 
LCS的客户端发起定位请求，指明是延迟定位，以及请求的事件等。 
GMLC之间的处理。同时H-GMLC分配一个LDR参考号，带给V-GMLC。 
V-GMLC发送Provide Subscriber Location request (deferred)消息给SGSN，消息中带有LDR参考号、请求的事件以及H-GMLC的地址等。 
如果SGSN不支持延迟定位中某些特殊事件，或者隐私检查失败，SGSN回复错误响应，带相应的错误原因。如果SGSN支持，回复不带位置信息的Provide
Subscriber Location ack给V-GMLC。同时计费。 
V-GMLC回复LCS Service Response给H-GMLC，指示请求是否被接受。 
H-GMLC回复LCS Service Response给R-GMLC，指示请求是否被接受。 
R-GMLC回复LCS Service Response给LCS客户端，指示请求是否被接受。 
UE发送Requested Event Detected消息给SGSN。 
SGSN从RAN得到位置信息，SGSN发送Subscriber Location Report消息。同时计费。 
如果没有得到位置信息，或者等待超时等某些原因失败。SGSN在Subscriber Location Report消息中带参考号、H-GMLC的地址，以及相应的原因。 
如果在等待的过程中，SGSN发现用户移动到其他的SGSN，SGSN立即发送Subscriber Location Report给V-GMLC，由V-GMLC或者H-GMLC向新的SGSN发起延迟定位请求。 
如果LCS要求的事件满足，SGSN发起被动的定位流程。如果发送了LCS Location Notification Invoke消息，定位请求的类型需要指明当前位置，同时忽略延迟定位事件类型。如果安全检查失败，SGSN在Subscriber Location Report消息中带参考号、H-GMLC的地址，以及相应的原因。 
V-GMLC回复响应给H-GMLC。 
H-GMLC回复响应给R-GMLC。 
R-GMLC回复响应给LCS客户端。 
LCS客户端发起UE可达的延迟周期性定位
此流程的周期性操作是在R-GMLC上完成，对于SGSN来说，与普通的被动延迟定位过程相同。 
LCS客户端发起的取消UE可达的延迟定位
LCS客户端发起的取消UE可达的延迟定位的流程如[图5]所示。
图5  LCS客户端发起的取消UE可达的延迟定位流程图
流程说明： 
LCS的客户端发起取消UE可达的延迟定位要求。 
R-GMLC发送LCS Cancell Service Request给H-GMLC。 
H-GMLC发送LCS Cancell Service Request给V-GMLC。 
V-GMLC发送Provide Subscriber Location消息给SGSN，通知取消UE可达的延迟定位要求。 
SGSN回复Provide Subscriber Location Ack给V-GMLC，消息不带位置信息。 
V-GMLC回复响应给H-GMLC。 
H-GMLC回复响应给R-GMLC。 
R-GMLC回复响应给LCS客户端。 
LCS客户端发起的UE位置事件的延迟定位
LCS客户端发起的UE位置事件的延迟定位的流程如[图6]所示。
图6  LCS客户端发起的UE位置事件的延迟定位流程图
流程说明： 
LCS的客户端发起定位请求，指明是延迟定位，以及请求的事件，指明区域以及用户离开或进入此区域等。 
GMLC之间的处理。同时H-GMLC分配一个LDR参考号，带给V-GMLC。 
V-GMLC发送Provide Subscriber Location request (deferred)消息给SGSN，消息中带有LDR参考号、请求的事件以及H-GMLC的地址等。 
SGSN判断用户是否支持此种定位，如果不支持，SGSN回复错误响应，带相应的错误原因。如果支持，用户处于空闲态时，需要寻呼、鉴权、安全性检查以及是否通知UE等操作。在隐私检查时，如果正在执行之前的延迟定位过程，UE可能会返回失败。 
SGSN发送LCS Area Event Invoke消息给UE，携带位置、LDR参考号以及H-GMLC的地址。 
UE成功处理后，UE发送响应给SGSN。 
SGSN回复响应给V-GMLC，指明成功或者失败。 
V-GMLC回复LCS Service Response给H-GMLC，指明成功或者失败。 
H-GMLC回复LCS Service Response给R-GMLC，指明成功或者失败。 
H-GMLC回复LCS Service Response给LCS客户端，指明成功或者失败。 
UE检测到位置事件发生。 
UE在发送LCS Area Event Report消息前，需要建立与SGSN的连接。消息中带LDR参考号、H-GMLC的地址以及是否需要通知验证过程指示。UE如果没有SGSN的响应，需要重发等操作。 
SGSN发送Subscriber Location Report给V-GMLC，消息中带参考号、H-GMLC的地址，以及相应的原因。 
V-GMLC回复响应给H-GMLC。 
如果UE发现漫游另外的PLMN等，通知H-GMLC，H-GMLC重新发起新的定位流程。 
LCS客户端发起的取消UE位置事件的延迟定位
LCS客户端发起的取消UE位置事件的延迟定位的流程如[图7]所示。
图7  LCS客户端发起的取消UE位置事件的延迟定位的流程图
流程说明： 
LCS的客户端发起取消UE位置事件的延迟定位要求。 
R-GMLC发送LCS Cancell Service Request给H-GMLC。 
H-GMLC发送LCS Cancell Service Request给V-GMLC。 
V-GMLC发送Provide Subscriber Location消息给SGSN，通知取消UE位置事件的延迟定位要求。 
SGSN发送LCS Area Event Cancellation给UE，消息中带LDR参考号以及H-GMLC的地址。 
UE回复LCS Area Event cancellation ack，消息中没有位置事件的信息；或者UE检测到位置事件发生，UE根据自身的策略主动取消位置事件上报，发送LCS
Area Event Report消息，消息中包括LDR参考号以及取消的指示和相应的错误。 
SGSN回复Provide Subscriber Location Ack给V-GMLC，消息不带位置信息。 
V-GMLC回复响应给H-GMLC。 
H-GMLC回复响应给R-GMLC。 
R-GMLC回复响应给LCS客户端。 
通知和验证过程
通知和验证过程的流程如[图8]所示。
图8  通知和验证过程流程图
流程说明： 
LCS的客户端发起通知和验证过程请求。 
GMLC发送Provide Subscriber Location消息给SGSN。消息指示notification only，并携带IMSI、定位的类型、LCS的Qos、APN-NI等。 
SGSN收到此消息后，进行隐私鉴权等。如果UE出于空闲态，在发起寻呼的流程。 
SGSN执行安全过程。 
SGSN发送通知消息给UE。 
UE通知用户，等待用户的允许或者拒绝。并通知SGSN，指明同意或者拒绝。如果用户拒绝，SGSN回复错误的响应给GMLC。 
SGSN回复Provide Subscriber Location Ack响应消息给GMCL。 
UE主动的定位
UE主动的定位的流程如[图9]所示。
图9  UE主动的定位流程图
流程说明： 
UE需要发起定位，如果处于空闲态，则发起Service Request流程，同时可能有安全检查的过程；如果用户处于连接态，则跳过此步。 
UE发送Service Invoke消息给SGSN。包括的定位类型：location estimate of the
UE, location estimate of the UE to be sent to an external LCS client,
location assistance data or broadcast assistance data message ciphering
keys。当UE选择location estimate of the UE to be sent to an external LCS
client时，需要携带LCS的ID，GMLC的地址（可选）。同时SGSN需要分配V-GMLC的地址。 
如果定位类型是current or last known location，SGSN判断如果已经保存了定位信息，则不再通知RAN；否则通知RAN。 
RAN定位用户。 
RAN返回位置信息Lcation Report。 
如果定位成功，SGSN发MAP Subscriber Location Report给V-GMLC，包含位置信息等。 
V-GMLC判断UE是否是location estimate of the UE to be sent to an external
LCS client的类型，如果外部的LCS客户端不可用，则回响应给SGSN；否则发消息给H-GMLC（从HLR得到H-GMLC的地址）。 
H-GMLC发消息给R-GMLC。 
R-GMLC发消息给LCS客户端。 
LCS客户端回复Location Information ack给R-GMLC，指明成功或者失败。 
R-GMLC回复Location Information ack给H-GMLC，指明成功或者失败。 
H-GMLC回复Location Information ack给V-GMLC，指明成功或者失败。 
V-GMLC回复MAP Subscriber Location Report Ack给SGSN，指明成功或者失败。 
SGSN回复Service Response给UE，指明成功或者失败。同时计费。 
系统影响 : 
对系统，一般情况下，LCS业务对SGSN系统基本无影响。只有在大话务量、并且存在大量用户定位的情况下，会增加MP的CPU负荷。对其他业务无影响。 
遵循标准 : 
标准名称
---
3GPP TS 23.271 Functional stage 2 description of Location Services(LCS)
3GPP TS 29.171 Location Services (LCS); LCS Application Protocol(LCS-AP) between the Mobile Management Entity (MME) and Evolved ServingMobile Location Centre (E-SMLC); SLs interface
3GPP TS 29.172 Location Services (LCS); Evolved Packet Core(EPC) LCS Protocol (ELP) between the Gateway Mobile Location Centre(GMLC) and the Mobile Management Entity (MME); SLg interface
3GPP TS 24.080 Mobile radio interface layer 3 supplementaryservices specification; Formats and coding
3GPP TS 29.002 Mobile Application Part (MAP) specification
3GPP TS 32.251 Telecommunication management; Charging management;Packet Switched (PS) domain charging
特性能力 : 
可以支持所有用户的定位。 
O&M相关 : 
命令
新增配置项参见[表3]。
配置项|命令
---|---
容量配置|SET CAPACITYSHOW CAPACITY
移动号码分析|ADD MDNALSET MDNALDEL MDNALSHOW MDNALSHOW MDN2REALM
SGSN GMLC配置|ADD GMLCSET GMLCDEL GMLCSHOW GMLC
SGSN VGML配置|ADD SGSN VGMLCSET SGSNVGMLCDEL SGSN VGMLCSHOW SGSN VGMLC
本局移动参数|SET COMBOCFGSHOW COMBOCFG
分组域参数配置|SET PACKET DOMAIN PARAMETERSHOW PACKET DOMAIN PARAMETER
GT翻译数据配置|ADD GTSET GTDEL GTSHOW GT
性能统计
性能计数器参见[表4]。
测量类型名称|性能计数器名称
---|---
LCS测量|编号为C43014开头的所有计数器
LCSAP消息测量|C432050001 定位请求消息发送次数C432050002 定位响应消息接收次数
SGSN LCS测量|编号为C40516开头的所有计数器
话单与计费
SGSN网元提供LCS计费功能。 
特性配置 : 
摘要配置特性测试用例常见问题处理 
配置特性 : 
配置前提
完成2G/3G业务基本配置，可以进行基本的PS业务。 
配置过程
设置license支持LCS功能。 
执行[ADD SGSN VGMLC]命令，增加SGSN VGMLC配置。
执行[SET CAPACITY]命令，修改容量规划配置。
执行[ADD GT]命令，配置GT翻译，指明局向。
执行[SET COMBOCFG]命令，在本局移动数据中配置LCS版本。
执行[ADD GMLC]命令，新增定位GMLC配置。
配置实例
配置脚本|配置说明
---|---
ADD SGSN VGMLC:VGMLCADDR=192.0.1.170,NAME="test1"|新增SGSN VGMLC
SET CAPACITY:BOARDTYPE=VMB,LCSNUM=2048,LCSSGSN=10000|设置容量规划
ADD GT:GT="86139810000",TRANS=1,OFFICEID1=81,SELECTEDNUM1=1,GTDI=0|GT翻译配置
SET COMBOCFG:LCSVER="R4"|本局移动数据配置
ADD GMLC:CC="88",NDC="139",ENABLE="YES",SELMODE="CC+NDC"|新增定位GMLC配置
测试用例 : 
测试项目|SGSN-MT LCS
---|---
测试目的|验证MT定位功能
预置条件|各网元运行正常。License开启支持LCS功能。创建性能统计测量任务：MME LCS测量、MME LCSAP消息测量、MME Diameter测量。
测试过程|2G用户已经附着、激活在网络，并保持ready态。SGSN收到GMLC发送来的PLR消息。
通过准则|SGSN发送PERFORM-LOCATION-REQUEST(BSSGP)消息给BSS，消息中包括定位类型、QoS等参数。定位成功，SGSN收到PERFORM-LOCATION-RESPONSE。SGSN回复PLA给GMLC，包括位置信息、生存期等信息。同时生成一张LCS-MT-CDR话单。信令跟踪、性能统计信息正确。
测试结果|无
测试项目|SGSN-延时定位-UE可及
---|---
测试目的|验证UE可及定位功能
预置条件|各网元运行正常。License开启支持LCS功能。创建性能统计测量任务：MME LCS测量、MME LCSAP消息测量、MME Diameter测量。
测试过程|SGSN收到V-GMLC发送来的PLR消息 (deferred) ，携带有LDR参考号、H-GMLC的地址等。
通过准则|SGSN回复不带位置信息的PLA给V-GMLC。探测到请求的事件，SGSN发送LOCATION REPORTING CONTROL消息给RAN。SGSN发送SLR消息,携带位置信息。检查LCS-MT-CDR所含信息正确。信令跟踪、性能统计信息正确。
测试结果|无
测试项目|SGSN-MO LCS
---|---
测试目的|验证MO定位功能
预置条件|各网元运行正常。License开启支持LCS功能。创建性能统计测量任务：MME LCS测量、MME LCSAP消息测量、MME Diameter测量。
测试过程|3G用户附着、激活成功后释放Iu链接，GMM状态为IDLE。用户发起业务请求。用户发送直传register消息给SGSN。
通过准则|业务请求流程成功，可能会有安全检查过程。SGSN向RAN发送LOCATION REPORTING CONTRO。收到RAN回应的Location Report后，SGSN向V-GMLC发送包含位置信息的MAP SubscriberLocation Report消息。定位成功，SGSN回复Service Response给UE。同时生成一张LCS-MO-CDR话单。信令跟踪、性能统计信息正确。
测试结果|无
常见问题处理 : 
网管中已经添加LCS配置，但无法做LCS业务。处理建议：检查是否打开License开关。 
从不支持LCS改为支持，每模块只能支持一个LCS用户。处理建议：不支持LCS功能时，容量设置每模块LCS用户为1。改为支持LCS时记得要修改容量的配置。 
MT定位失败。处理建议：MT定位时，SGSN会判断GMLC是否在允许列表中，不在将导致定位失败。 
容量受限，会导致2/3G用户附着失败处理建议：本局移动数据配置中“本局支持的LCS版本”的配置仅在SGSN环境中使用，MME无需此配置。COMBO环境中，对于MME开启了LCS功能，而当容量配置中SGSN的LCS用户数设置为1时，由于HLR会根据SGSN支持LCS能力下发LCS信息，但是由于容量受限，会导致2/3G用户附着失败。可以通过SET COMBOCFG:LCSVER="NO命令关闭SGSN的LCS能力，规避此现象。 
# 缩略语 
# 缩略语 
## CGI 
Cell Global Identification小区全球识别码
## GMLC 
Gateway for Mobile Location Center移动定位中心网关
HLR : 
Home Location Register归属位置寄存器
## LCS 
LoCation Services定位业务
## RAI 
Routing Area Identity路由区标识
RNC : 
Radio Network Controller无线网络控制器
## SAI 
Service Area Identity业务区域标识
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
# ZUF-77-16 增强功能 
概述 : 
功能描述 : 
因组网、用户业务或运营商本地控制的需要，SGSN对用户除了提供基本的接入管理、安全管理、移动性管理、会话管理，还提供了一些可选的增强功能。 
功能特性简介 : 
针对用户的应用特点和应用场景，核心网为满足用户的要求，提供了有效的解决方案。详细的解决方案特性如下。 
方案特性|实现简述|特导链接
---|---|---
支持MOCN|MOCN指无线接入网络共享，而核心网元不共享的一种网络共享方式。SGSN只支持3 G的MOCN功能。MOCN使得多个运营商共同出资建设共享的无线接入网络，分担网络建设成本，降低网络建设风险，提高建网速度。SGSN网元的MOCN功能包括在附着、RAU、局内切换以及局间切换业务流程中传递选择的PLMN标识，支持切换限制列表。SGSN支持MOCN功能参见3GPP 23.251协议。|ZUF-77-16-001 支持MOCN
支持PDP类型IPV6和双栈|SGSN支持UE地址为IPV4、IPv6和IPV4V6双栈。SGSN根据UE请求的PDP类型和签约的PDP类型进行协商。PDP类型协商参见3GPP 23.060协议的“9.2.1 Static and Dynamic PDP Addresses”章节。|ZUF-77-16-002 支持PDP类型IPV6和双栈
SGSN支持无线资源管理|无线资源管理指基于特定的用户进行上下文信息分配，并保持无线信道。SGSN支持基于IMSI号段配置RFSP索引。SGSN发送RFSP索引给RNC/BSC，RNC/BSC映射RFSP索引为相应的无线信道分配和管理策略。无线资源管理功能参见3GPP TS 23.401和TS 36.413协议。|ZUF-77-16-004 SGSN支持无线资源管理
## ZUF-77-16-001 支持MOCN 
特性描述 : 
摘要描述应用场景客户收益实现原理系统影响遵循标准特性能力可获得性O&M相关 
描述 : 
定义
3GPP R6引入的网络共享概念，是指不同运营商进行核心网共享或无线网络共享，主要是多个运营商共同出资建设共享的网络，这是为分担网络建设成本、降低风险而采取的一种建网模式。 
MOCN是指无线接入网络共享，核心网元不共享的一种网络共享方式，无线接入网络指RNC，即多个运营商共同出资建设共享的无线接入网络，分担网络建设成本，降低网络建设风险，提高建网速度。MOCN网络共享模式如[图1]所示。
图1  MOCN网络共享模式
Gn/Gp SGSN网元MOCN功能包括对NS-UE的接入、S-UE的接入、重定位过程中支持选择的PLMN标识和SNA信息维护传递。
3GPP R11引入了Gb口MOCN，目前ZXUN-uMAC仅支持根据用户IMSI判断是否需要Gb口重路由功能，用于解决不支持Gb接入MOCN功能的UE，无法接入到归属的核心网中。 
背景知识
协议上对网络共享给出了两种网络架构： 
MOCN：仅无线接入部分共享，核心网元不共享。 
GWCN：除了共享的无线网络，核心网也在运营商间共享。 
组网方式如[图2]所示。
图2  GWCN网络共享模式
经常与网络共享一起被提到的术语还有MVNO，主要是指没有无线频谱资源，但有经营权，可以通过租用方式向终端用户提供移动通信服务，能够发行自己的SIM卡的机构或组织，采用了核心网共享技术，其实，这也属于网络共享。 
对于Gb口MOCN的组网方式类似Iu口MOCN，只不过需要将无线接入网替换为BSC，SGSN和RAN之间的接口替换为Gb口。 
应用场景 : 
应用场景图如[图3]所示。
图3  3G无线接入网络共享
应用场景说明： 
运营商A和运营商B共享3G无线接入，运营商A拥有自己的核心网A和运营商B拥有自己的核心网B，且核心网中处理同一个RNC的CS域和PS域同属于一个运营商。 
网络共享需要兼容各种终端，包括S-UE（R6 UE）和NS-UE（Pre-R6 UE），这两种终端对于CN节点选择机制完全不同。S-UE和NS-UE对系统广播信息中的运营商信息采用不同的处理方式，如[图4]所示。
图4  网络共享兼容各种终端
NS-UE Iu接入过程
NS-UE Iu接入过程如[图5]所示。
图5  NS-UE接入过程
RNC通过系统信息（“System Information”）广播向UE发布某位置区中可用的网络信息（PLMN-id
List）。RNC在广播PLMN ID列表信息的同时，还需要广播Common PLMN-id，用于NS-UE进行网络选择。
NS-UE忽略系统信息广播中的PLMN ID列表，将Common PLMN和传统方式广播的网络作为候选列表执行网络选择，发起业务请求，但无法指示PLMN。 
在初始注册时，RNC将选择一个核心网（如核心网B）。
核心网分析IMSI并做相应检查，返回积极或消极的响应。
如果是积极响应，核心网B将返回一个TMSI/P-TMSI。
如果是消极响应，RNC将尝试其他核心网（如核心网A）。 
CS/PS协作即用户发起联合类型的附着，但Gs口更新失败，RNC需要重定向到其他核心网。 
S-UE Iu接入过程
S-UE Iu接入过程如[图6]所示。
图6  S-UE接入过程
RNC通过系统信息（“System Information”）广播向UE发布某位置区中可用的网络信息（PLMN-id
List）。RNC在广播PLMN ID列表信息的同时，还需要广播Common PLMN-id，用于NS-UE进行网络选择。
S-UE获取系统广播信息中的PLMN ID列表和传统方式广播的网络，将这些网络作为候选列表执行网络选择，Common
PLMN-id需要被排除在外。选择到可以接入的PLMN后，发起附着或路由更新请求并指示已选择的PLMN。 
RNC根据S-UE选择的PLMN直接定位所服务的运营商，从而将该消息路由到相应的CN节点（如核心网A）。 
核心网A确定UE被允许接入网络，返回一个TMSI/P-TMSI，方便RNC对后续消息的再次路由到本核心网。 
Gb接入重路由过程
Gb接入重路由过程如[图7]所示。
图7  Gb接入重路由过程
在UE初始注册时，BSC将选择一个核心网（如核心网B）。 
核心网分析IMSI并做相应检查，返回积极或消极的响应。
如果是积极响应，核心网B将返回一个TMSI/P-TMSI。
如果是消极响应，BSC将尝试其他核心网（如核心网A）。 
客户收益 : 
受益方|受益描述
---|---
运营商|Gn/Gp SGSN支持MOCN功能，可以为运营商提供更加灵活的网络建设方式，包括和其他运营商分担网络建设成本，降低网络建设风险，提高建网速度等。
移动用户|对终端用户不可见。
实现原理 : 
涉及的网元
Gn/Gp SGSN支持MOCN功能需要UE、RNC、Gn/Gp
SGSN共同完成。 
网元名称|网元作用
---|---
UE|S-UE负责携带Selected PLMN Identity。
RNC|通过系统信息广播向UE发布某位置区中可用的网络信息，对S-UE处理Selected PLMN Identity，对NS-UE进行重定向，处理SNAAccess Information信息。
SGSN|对S-UE处理Selected PLMN Identity，对NS-UE进行重定向，处理SNA Access Information信息。
业务流程
MOCN功能需要实现如下流程： 
NS-UE的接入。 
S-UE的接入。 
重定位过程中Selected PLMN Identity的处理。 
SNA信息维护过程。 
NS-UE的接入过程
NS-UE不支持网络共享，忽略广播消息中的PLMN ID列表。NS-UE将Common
PLMN和传统方式广播的网络作为候选列表进行网络选择，发起附着或路由更新请求，但无法指示PLMN。 
NS-UE的附着接入过程NS-UE的附着接入过程的流程如图8所示。图8  NS-UE的附着接入过程流程描述：UE读取共享RNC的广播信息。NS-UE忽略广播信息中的PLMN ID列表，将Common
PLMN和传统方式广播的网络作为候选列表进行网络选择，发起附着请求，但无法指示PLMN。RRC连接建立。
RNC收到UE的初始直传消息，透传初始直传消息中的附着请求NAS消息并携带已设置的“redirect attempt
flag”指示一起给SGSN A。“redirect attempt flag”指示SGSN对RNC响应“Reroute
Command”或“Reroute Complete”，并指示UE为NS-UE（因为RNC置位该标识，说明初始UE消息中没有携带任何selected
PLMN-ID）。RNC对CN节点的选择依赖于NRI（NRI有效）或随机选择。SGSN A收到携带“redirect attempt flag”指示的初始UE消息。“redirect
attempt flag”指示SGSN A将对RNC回应答消息“Reroute Command”或“Reroute
Complete”。SGSN A需要知道UE的IMSI，从老的SGSN或UE那里获得IMSI。拿IMSI比对核心网运营商的漫游协议，如果SGSN
A发现UE漫游不允许或UE漫游允许但CS/PS协作被要求，则附着流程被终止。CS/PS协作指用户发起联合类型的附着，但Gs口更新失败，需要重定向到其他SGSN。The signalling connection between RNC and SGSN A is released.
 SGSN A给RNC发送直传消息，携带“Reroute Command”信息，“Reroute Command”包含IMSI、拒绝原因码、附着拒绝消息和从UE收到的初始的附着请求消息。SGSN A和RNC之间的Iu连接被释放。RNC选择一个新的SGSN B，给新的SGSN B发送初始UE消息（包括附着请求消息），在初始UE消息中设置“redirect
attempt flag”，携带IMSI，防止SGSN B又一次需要从UE或老的MSC/SGSN那里获取IMSI，并且指示RNC已经执行了CS/PS域协作（如果RNC有这个能力）。SGSN B收到初始UE消息后开始附着过程处理。SGSN B根据漫游协议，允许该用户接入，对用户完成鉴权。SGSN B更新HLR，从HLR得到用户签约数据。The signalling connection between the RNC and the SGSN B is
released.  根据用户签约数据，漫游不允许。SGSN B给RNC发送直传消息，携带“Reroute Command”信息，“Reroute Command”包含拒绝原因码、附着拒绝消息和从UE收到的初始的附着请求消息。SGSN
B和RNC之间的Iu连接被释放。RNC选择一个新的SGSN C，给新的SGSN C发送初始UE消息（包括附着请求消息），在初始UE消息中设置“redirect
attempt flag”，携带IMSI。SGSN C开始附着过程处理。SGSN C根据漫游协议，允许该用户接入，对用户完成鉴权。SGSN C更新HLR，从HLR得到用户签约数据。用户签约数据允许漫游，SGSN C完成附着过程。SGSN C给RNC发送直传消息（包括附着接受消息），直传消息中设置“Reroute Complete”。RNC确认重定向完成，前转NAS消息（附着接受）消息给UE。附着接受消息被前转给UE，UE保存包含NRI的TMSI/P-TMSI信息，用于以后的信令消息传送。UE返回附着完成消息。 
NS-UE的路由更新接入过程NS-UE的路由更新接入过程的流程如图9所示。图9  NS-UE的路由更新接入过程流程说明：UE读取共享RNC的广播信息。NS-UE忽略广播信息中的PLMN ID列表，将Common
PLMN和传统方式广播的网络作为候选列表进行网络选择，发起路由更新请求，但无法指示PLMN。RRC连接建立。RNC收到UE的初始直传消息，透传初始直传消息中的路由更新请求NAS信息并携带已设置的“redirect attempt
flag”指示一起给SGSN A。“redirect attempt flag”指示SGSN对RNC响应“Reroute
Command”或“Reroute Complete”，并指示UE为NS-UE（因为RNC置位该标识，说明初始UE消息中没有携带任何selected
PLMN-ID）。RNC对CN节点的选择依赖于NRI（NRI有效）或随机选择。SGSN A收到携带“redirect attempt flag”指示的初始UE消息。“redirect
attempt flag”指示SGSN A将对RNC回应答消息“Reroute Command”或“Reroute
Complete”。The signalling connection between RNC and SGSN A is released.
SGSN A需要知道UE的IMSI，从老的SGSN或UE那里获得IMSI。拿IMSI比对核心网运营商的漫游协议，如果SGSN A发现UE漫游不允许或UE漫游允许但CS/PS协作被要求，则路由更新流程被终止。CS/PS协作指用户发起联合类型的附着，但Gs口更新失败，需要重定向到其他SGSN。SGSN A给RNC发送直传消息，携带“Reroute Command”信息，“Reroute Command”包含IMSI、拒绝原因码、路由更新拒绝消息和从UE收到的初始的路由更新请求消息。SGSN A和RNC之间的Iu连接被释放。RNC选择一个新的SGSN B，给新的SGSN B发送初始UE消息（包括路由更新请求消息），在初始UE消息中设置“redirect attempt flag”，携带IMSI，指示RNC已经执行了CS/PS域协作（如果RNC有这个能力）。SGSN B收到初始UE消息后开始处理路由更新过程处理。SGSN B根据漫游协议，允许该用户接入，对用户完成鉴权。SGSN B更新HLR，从HLR得到用户签约数据。The signalling connection between the RNC and the SGSN B is
released.  根据用户签约数据，漫游不允许。SGSN B给RNC发送直传消息，携带“Reroute Command”信息，“Reroute Command”包含拒绝原因码、路由更新拒绝消息和从UE收到的初始的路由更新请求消息。SGSN B和RNC之间的Iu连接被释放。RNC选择一个新的SGSN C，给新的SGSN C发送初始UE消息（包括路由更新请求消息），在初始UE消息中设置“redirect attempt flag”，携带IMSI。 SGSN C开始路由更新过程处理。SGSN C根据漫游协议，允许该用户接入，对用户完成鉴权。SGSN C更新HLR，从HLR得到用户签约数据。用户签约数据允许漫游，SGSN C完成路由更新过程。SGSN C给RNC发送直传消息（包括路由更新接受消息），直传消息中设置“Reroute Complete”。RNC确认重定向完成，前转NAS消息（路由更新接受）消息给UE。路由更新接受消息被前转给UE，UE保存包含NRI的TMSI/P-TMSI信息，用于以后的信令消息传送。UE返回路由更新完成消息。 
S-UE的接入过程
对于支持网络共享的终端接入，终端可以解码系统广播消息中的可用PLMN
ID列表，从中选择可以接入的PLMN，即S-UE可以自动选择服务的运营商（不同运营商网号不同），并发起附着或路由更新请求，RNC可以根据S-UE选择的PLMN直接定位所服务的运营商，从而将该消息路由到相应的CN节点。 
S-UE的附着接入过程S-UE的附着接入过程如图10所示。图10  S-UE的附着接入过程流程描述：S-UE读取共享无线网络的广播系统信息。S-UE解码共享网络信息，把可得到的PLMN ID列表作为PLMN选择的侯选。S-UE从可用的PLMN列表中完成网络选择。S-UE发送附着请求消息给网络，并将Selected PLMN Identity信息携带给RNC。RNC根据UE指示的Selected
PLMN Identity选择SGSN，发送附着请求消息给选择的SGSN。SGSN确定UE是否被允许接入网络。SGSN给UE发送附着接受或拒绝消息。如果附着接受，则附着接受消息中携带指定的TMSI/P-TMSI，方便RNC对后续消息的再次路由到本SGSN。 
S-UE的路由更新过程S-UE的路由更新过程如图11所示。图11  S-UE的路由更新过程流程说明：S-UE读取共享无线网络的广播系统信息。S-UE解码共享网络信息，把可得到的PLMN ID列表作为PLMN选择的侯选。S-UE从可用的PLMN列表中完成网络选择。S-UE发送路由更新请求消息给网络，并将Selected PLMN Identity信息携带给RNC。RNC根据UE指示的Selected
PLMN Identity选择SGSN，发送路由更新请求消息给选择的SGSN。SGSN确定UE是否被允许接入网络。SGSN给UE发送路由更新接受或拒绝消息。如果路由更新接受，则路由更新接受消息中携带指定的TMSI/P-TMSI，方便RNC对后续消息的再次路由到SGSN。 
重定位过程中支持Selected PLMN Identity
SGSN支持MOCN时，重定位过程中需要在Relocation
Request和Forward Relocation Request消息中携带Selected PLMN Identity信息。 
局内重定位过程中支持Selected PLMN Identity流程说明：SGSN收到Source RNC的Relocation Required消息。SGSN正常的处理局内重定位过程。SGSN给Target RNC发送Relocation Request消息，如果SGSN支持MOCN，并且在接入过程中收到了RNC携带过来的Selected
PLMN Identity信息，则把Selected PLMN Identity信息带给Target RNC。 
局间重定位过程中支持Selected PLMN Identity流程说明：老局SGSN收到Source RNC的Relocation Required消息。老局SGSN正常的处理局间重定位过程。老局SGSN给新局SGSN发送Forward Relocation Request消息，如果老局SGSN支持MOCN，并且在接入过程中收到了RNC携带过来的Selected
PLMN Identity信息，则把Selected PLMN Identity信息带给新局SGSN。新局SGSN收到Forward Relocation Request消息，给Target RNC发送Relocation
Request消息时，如果新局SGSN支持MOCN，并且Forward Relocation Request消息中携带了Selected
PLMN Identity信息，则把Selected PLMN Identity信息带给Target RNC。 
SNA信息维护过程
共享网络区（SNA）： 
共享网络区由运营商分配，在同一个PLMN内有效。共享网络区和位置区是多对多的关系：一个SNA可以包含一个或多个位置区LA，一个LA可以属于多个SNA。如[图12]所示。
图12  共享网络区
共享网络接入控制： 
共享网络接入控制由RNC执行，为实现基于SNA的共享网络接入控制，RNC需要知道位置区LA属于哪个或哪些SNA，RNC从CN获得关于本RNC下所有位置区LA在SNA中的归属关系以及用户在每个SNA的访问权限，并在需要的时候由CN告知RNC或者在RNC之间传递。这样RNC可以基于SNA控制每个用户对共享网络的访问权限。
SNA信息维护过程包括： 
给RNC下发全局信息过程这一信息通过和SGSN的Information Transfer过程来获取。给RNC下发全局信息过程如图13所示。图13  给RNC下发全局信息过程流程说明：SGSN或RNC重启或链路恢复后，SGSN检测到RNC局向可达，RESET过程成功后（收到或回送RESET ACK），如果SGSN支持MOCN和SNA， RNC也支持SNA ，则SGSN给RNC发送Information Transfer Indication消息，消息中携带PLMN列表，以及每个PLMN下的LAC和SNA对应关系列表。RNC收到后给SGSN返回Information Transfer Confirmation消息，RNC据此确定用户的接入限制范围（哪些LAC或者哪些PLMN）。 
给RNC下发用户SNA信息过程如果要实现指定用户的接入控制，SGSN还需要将用户可接入的SNA通知到RNC，这一信息在Common ID和Relocation Request中通知到RNC。用户SNA信息在接入过程（附着和路由更新）中通过Common ID消息带给RNC，在切换过程中通过Relocation Request消息带给RNC。附着过程中给RNC下发SNA信息的流程说明：SGSN收到RNC的初始UE消息（携带附着请求消息）。SGSN正常的处理附着过程。SGSN给RNC发送Common ID消息，如果SGSN支持MOCN和SNA， RNC也支持SNA，该用户也配置了SNA信息（根据用户的IMSI号段配置SNA信息），则把该用户配置的SNA信息下发给RNC。路由更新过程中给RNC下发SNA信息的流程说明：SGSN收到RNC的初始UE消息（携带路由更新请求消息）。SGSN正常的处理路由更新过程。SGSN给RNC发送Common ID消息，如果SGSN支持MOCN和SNA， RNC也支持SNA，该用户也配置了SNA信息（根据用户的IMSI号段配置SNA信息），则把该用户配置的SNA信息下发给RNC。局内重定位过程中给RNC下发SNA信息的流程说明：SGSN收到Source RNC的Relocation Required消息。SGSN正常的处理局内重定位过程。SGSN给Target RNC发送Relocation Request消息，如果SGSN支持MOCN和SNA，Target RNC也支持SNA，该用户也配置了SNA信息（根据用户的IMSI号段配置SNA信息），则把该用户配置的SNA信息下发给RNC。局间重定位过程中给RNC下发SNA信息的流程说明：新局SGSN收到Forward Relocation Request消息。新局SGSN正常的处理局间重定位过程。新局SGSN给Target RNC发送Relocation Request消息，如果新局SGSN支持MOCN和SNA，Target RNC也支持SNA，该用户也配置了SNA信息（根据用户的IMSI号段配置SNA信息），则把该用户配置的SNA信息下发给RNC 
Gb接入重路由过程
Gb接入附着过程如[图14]所示。
图14  Gb接入附着过程
流程说明： 
UE触发附着流程，发送LLC消息给BSC，携带foreign/random TLLI、Attach Request。 
BSC根据foreign/random TLLI选择SGSN Operator A，然后发送BSSGP UL-UNITDATA消息给该SGSN，携带foreign/random  TLLI、Attach Request以及redirect attempt flag。 
若在Operator A的核心网无法获取到该用户的IMSI，则触发Identify Request给UE，UE回复Identify Response，携带用户IMSI。 
若Operator A SGSN基于本地策略确定是否需要执行鉴权，若需要则执行鉴权认证流程。 
Operator A SGSN根据用户IMSI查询本地配置，决策该用户是否需要路由到其他SGSN。 
步骤5决策结果为需要将用户路由到其他SGSN，则Operator A SGSN拒绝附着请求，下发DL-UNITDATA给给BSC，其中携带收到的Attach Request、Attach Reject、IMSI、Redirection Indication以及Unconfirmed send state variable。 
BSC将步骤1中的TLLI暂时绑定到SGSN Operator B，然后发送BSSGP UL-UNITDATA消息给该SGSN，携带Attach Request、redirect attempt flag以及IMSI。 
Operator B SGSN接受Attach Request，下发BSSGP DL-UNITDATA给BSC，携带Attach Accept、redirection complete标记，Attach Accept包含新分配的TLLI。BSC将Attach Accept转发给UE。 
UE回复Attach Complete，确认新分配的TLLI。 
Gb接入路由区更新过程如[图15]所示。
图15  Gb接入路由区更新过程
流程说明： 
UE触发路由区更新流程，发送LLC消息给BSC，携带foreignTLLI、RAU Request。 
BSC根据foreign TLLI选择SGSN Operator A，然后发送BSSGP UL-UNITDATA消息给该SGSN，携带foreignTLLI、RAU Request以及redirect attempt flag。若UE从它局SGSN移动过来，则Operator A SGSN向老局SGSN请求用户信息。 
若Operator A SGSN基于本地策略确定是否需要执行鉴权，若需要则执行鉴权认证流程。 
Operator A SGSN根据用户IMSI查询本地配置，决策该用户是否需要路由到其他SGSN。 
步骤4决策结果为需要将用户路由到其他SGSN，则Operator A SGSN拒绝附着请求，下发DL-UNITDATA给给BSC，其中携带收到的RAU Request、RAU Reject、IMSI、Redirection Indication以及Unconfirmed send state variable。 
BSC将步骤1中的TLLI暂时绑定到SGSN Operator B，然后发送BSSGP UL-UNITDATA消息给该SGSN，携带RAU Request、redirect attempt flag以及IMSI。 
Operator B SGSN接受RAU Request，下发BSSGP DL-UNITDATA给BSC，携带RAU Accept、redirection complete标记，RAU Accept包含新分配的TLLI。BSC将RAU Accept转发给UE。 
UE回复RAU Complete，确认新分配的TLLI。 
系统影响 : 
SGSN支持MOCN功能，对SGSN的性能无影响。 
遵循标准 : 
本特性的参考资料清单如下： 
3GPP TS 23.060: " General Packet Radio Service (GPRS) ; Service
description; Stage 2". 
3GPP TS 23.251: " Network Sharing; Architecture and functional
description". 
3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification;
Core Network Protocols; Stage 3". 
3GPP TS 25.413: "UTRAN Iu Interface RANAP Signalling". 
3GPP TS 48.018: "General Packet Radio Service (GPRS); Base
Station System (BSS) - Serving GPRS Support Node (SGSN); BSS GPRS
Protocol (BSSGP)". 
3GPP TS 29.060: "General Packet Radio Service (GPRS); GPRS
Tunnelling Protocol (GTP) across the Gn and Gp Interface". 
3GPP TS 29.002: "Mobile Application Part (MAP) specification". 
3GPP TS 23.003: "Numbering, addressing and identification". 
3GPP TS 24.007: "Mobile radio interface signalling layer 3;
General aspects". 
特性能力 : 
特性|能力
---|---
多PLMN配置|最多支持16个PLMN。
共享网络区配置|最多支持256个共享网络区，一个共享网络区最多关联32个位置区，所有共享网络区关联的位置区对应的PLMN个数不超过8个。
共享网络群配置|最多支持22048个共享网络群，一个共享网络群最多支持8个共享网络区。
基于用户的共享网络区配置|最多支持基于256个用户IMSI号段配置共享网络区，每个IMSI号段最多支持8个共享网络群。
可获得性 : 
SGSN支持3G MOCN功能和Gb口支持Rerouting功能需要申请了License许可后，运营商才能获得该特性的服务。对应的License项目为： 
SGSN支持3G MOCN功能 
SGSN支持Gb口Rerouting 
O&M相关 : 
命令
新增配置项参见[表2]。
配置项|命令
---|---
设置本局移动数据|SET COMBOCFGSHOW COMBOCFG
RNC局向附加属性配置|ADD RNCSET RNCDEL RNCSHOW RNCADD RNC PAGING AREADELRNC PAGING AREASHOW RNC PAGING AREA
共享网络区配置|ADD SNASET SNADEL SNASHOW SNA
增加共享网络区的位置区|ADD SNA LAI
共享网络群配置|ADD SNGSET SNGDEL SNGSHOW SNG
基于用户的SNA接入信息配置|ADD IMSI SNASET IMSISNADEL IMSI SNASHOW IMSI SNA
SGSN与RNC对接配置|ADD OPCADD ADJOFCADD M3UASCTPADD RNC
SGSN支持多PLMN配置|ADD HPLMNCFGADD LAIADD RAIADD RNC
Gb口Rerouting策略配置|SET GB INTERFACE REROUTING POLICYSHOW GB INTERFACE REROUTING POLICY
IMSI号段Gb口Rerouting策略配置|ADD IMSI GB INTERFACE REROUTING POLICYDEL IMSI GB INTERFACE REROUTING POLICYSHOW IMSI GB INTERFACE REROUTING POLICY
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
SGSN RNC测量|C405580067 接收重定向指示尝试次数C405580068 发送重定向指示次数C405580069 发送重定向完成次数
SGSN NSE测量（GPRS）|C405400097 接收Gb口重定向指示尝试次数C405400098 发送Gb口重定向指示次数C405400099 发送Gb口重定向完成次数
特性配置 : 
摘要配置特性测试用例常见问题处理 
配置特性 : 
配置前提
MOCN组网要求支持网络共享的RNC与各SGSN互通。
SGSN与不同PLMN的RNC互通并支持多PLMN。
SGSN与GGSN、HLR服务器之间通讯正常。
确认CS侧是否开启SNA功能，如果开启，则SGSN不用开启SNA功能。如果未开启，则SGSN上配置SNA信息数据。
Gb口支持Rerouting时，需要支持网络共享的BSC与各SGSN之间能互通，SGSN与不同PLMN的BSC互通并支持多PLMN。 
配置过程
操作步骤： 
通过License控制SGSN支持3G MOCN功能和SGSN支持Gb口Rerouting功能。 
为支持SNA的RNC在附加属性中增加相关特性支持。 
配置SNA信息。 
配置Gb口Rerouting策略。 
在实际配置MOCN功能时，经常会碰到把支持MOCN功能的RNC/BSC接入到已有的SGSN上，支持MOCN功能的RNC/BSC和SGSN下已连接的RNC/BSC还可能属于不同的PLMN，因此补充下面两部分的内容： 
SGSN与RNC/BSC对接。 
SGSN支持多PLMN配置。 
配置实例
激活llicense配置本局支持MOCN。 
命令|说明
---|---
LOAD LICENSE|将SGSN支持3G MOCN功能和SGSN支持Gb口Rerouting功能的license上传至前台后执行该命令使之生效。
配置SNA信息。 
命令|说明
---|---
SET SUPPORT SNA:SNAFLAG="YES";|配置本局支持SNA。
SET RNC:RNCOFFID=1,SNAFLAG="YES",NAME="RNC1";|配置RNC1支持SNA。
SET RNCRNCOFFID=2,SNAFLAG="NO",NAME="RNC2";|配置RNC2不支持SNA。
ADD SNA:SNAID=1,SNAC="0001",LAI="lai1"&"lai2"&"lai3"&"lai4",NAME="sna1";|sna1与lai1、lai2、lai3、lai4对应。
ADD SNA:SNAID=2,SNAC="0002",LAI="lai3"&"lai4"&"lai5"&"lai6"&"lai7",NAME="sna2";|sna2与lai3、lai4、lai5、lai6、lai7对应。
ADD SNG:SNAGRPID=1,SNAID=1&2,NAME="46001";|配置共享网络群，包含SNA1和SNA2。
ADD IMSI SNA:IMSI="46001",SNAGRPID=1,NAME="46001";|配置46001关联共享网络群1。
配置Gb口Rerouting策略。 
命令|说明
---|---
SET GB INTERFACE REROUTING POLICY:SUPGBROUTING="YES",SUPIMSIGBREROUTING="YES",REJECTCAUSE="REJECTCAUSE_13";|配置本局支持Gb口Rerouting，支持根据IMSI号段控制Gb口Rerouting，同时配置拒绝原因值为11：PLMN not allowed。
ADD IMSI GB INTERFACE REROUTING POLICY:IMSI="46011";|新增IMSI号段Gb口Rerouting策略。
测试用例 : 
3G网络下由NS-UE发起流程附着到SGSN
测试项目|NS-UE用户从支持MOCN的RNC发起附着接入到SGSN
---|---
测试目的|验证SGSN在MOCN模式下，能对错误接入到3G网络的NS-UE用户进行重定向指示。
预置条件|PS网络中各网元系统及操作维护台运行正常。用户在HLR中已签约PS业务。SGSN完成本功能的相关配置。在SGSN上建立用户跟踪。
测试过程|用户附着到SGSN，其中该INITIAL UE MESSAGE消息携带了Redirect Attempt Flag标记。该用户不允许在SGSN的PLMN下接入。
通过准则|用户附着以原因值11（PLMN not allowed）被拒绝。SGSN给RNC发送拒绝接入的DIRECT TRANSFER消息，其中的NAS-PDU为Attach Reject，GMM Cause为层三拒绝原因值，RedirectionIndication中的initial NAS-PDU为INITIAL UE MESSAGE消息中的NAS-PDU，RedirectionIndication中的Reject Cause Value为对应的层三拒绝原因值，Redirection Indication中的PermanentNAS UE Identity为用户的IMSI。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|-
3G网络下S-UE发起流程附着到SGSN
测试项目|S-UE用户从支持MOCN的RNC发起附着接入到SGSN
---|---
测试目的|验证SGSN在MOCN模式下，能正常处理正确接入到3G网络的的S-UE用户。
预置条件|SGSN组网配置正确。SGSN与外围RNC、HLR、DNS等通讯正常。SGSN开启MOCN功能。对接的RNC支持MOCN功能。
测试过程|S-UE用户选择到了正确的PLMN，附着到其对应运营商的SGSN。该用户在该SGSN的PLMN下接入。
通过准则|用户附着成功。信令跟踪能正常跟踪上述业务流程。
测试结果|-
2G网络下NS-UE发起流程附着到SGSN
测试项目|NS-UE用户从支持MOCN的BSC发起附着接入到SGSN
---|---
测试目的|验证SGSN在MOCN模式下，能对错误接入到2G网络的NS-UE用户进行重定向指示。
预置条件|PS网络中各网元系统及操作维护台运行正常。SGSN与外围RNC、HLR、DNS等通讯正常。SGSN支持Gb口Rerouting功能license打开，配置本局支持Gb口Rerouting，支持根据IMSI号段控制Gb口Rerouting，同时配置拒绝原因值为11：PLMN not allowed。新增IMSI号段Gb口Rerouting策略，该用户IMSI处于该号段内。在SGSN上建立用户跟踪。
测试过程|用户在2G网络中附着到SGSN，其中UL-UNITDATA消息携带了Redirect Attempt Flag标记。
通过准则|用户附着以原因值11（PLMN not allowed）被拒绝。SGSN给BSC发送Attach Reject消息，其中DL-UNITDATA消息中携带Redirection Indication指示，拒绝原因值为11。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|-
2G网络下S-UE发起流程附着到SGSN
测试项目|S-UE用户从支持MOCN的BSC发起附着接入到SGSN
---|---
测试目的|验证SGSN在MOCN模式下，能正常处理正确接入到2G网络的S-UE用户。
预置条件|PS网络中各网元系统及操作维护台运行正常。SGSN与外围RNC、HLR、DNS等通讯正常。SGSN支持Gb口Rerouting功能license打开，配置本局支持Gb口Rerouting，支持根据IMSI号段控制Gb口Rerouting，同时配置拒绝原因值为11：PLMN not allowed。新增IMSI号段Gb口Rerouting策略，该用户IMSI不处于该号段内。在SGSN上建立用户跟踪。
测试过程|用户在2G网络中附着到SGSN，其中UL-UNITDATA消息携带了Redirect Attempt Flag标记。
通过准则|用户附着成功。SGSN给BSC发送Attach accept消息，其中DL-UNITDATA消息中携带Redirection Complete指示。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|-
常见问题处理 : 
问题描述|解决方法
---|---
NS-UE附着接入成功，但是直传消息中没有Redirect Complete的消息。|检查本局是否配置支持MOCN，如果支持，再检查下在INITIAL UE MESSAGE消息中是否带了RedirectAttempt Flag标识。
局内重定位过程中Relocation Request时，没有带Selected PLMN Identity信息给TargetRNC。|检查本局是否配置支持MOCN，如果支持，再检查下在INITIAL UE MESSAGE消息中是否带参数SelectedPLMN Identity信息。
局间重定位过程中Forward Relocation Request消息中，老局支持MOCN，而且在接入过程中收到了RNC携带过来的SelectedPLMN Identity信息，但是老局没有把Selected PLMN Identity信息带给新局SGSN。|检查下接收到的RNC携带过来的Selected PLMN Identity信息是否与本局配置或其他配置的PLMN一致，不一致的话，不会带Selected PLMN Identity信息给新局。
用户附着成功，但是没有SGSN没有下发SNA信息给RNC。|检查配置是否正确：本局支持MOCN功能、本局支持SNA功能、RNC支持SNA，配置了基于该用户IMSI号段的共享网络区。
## ZUF-77-16-002 支持PDP类型IPV6和双栈 
概述 : 
IPv6被认为是下一代互联网协议，以弥补IPv4地址的短缺。3GPP选择将IPv6作为一种分配给UE的地址类型。SGSN支持IPv6或IPv4v6 DS PDN激活请求，也支持通过GTP隧道传输的IPv6或IPv4v6类型的用户报文。 
收益 : 
从IPv4到IPv6的演进对于技术和市场发展而言是必不可少的。无论是当前还是未来，支持用户IPv6请求为运营商带来更多机遇。 
描述 : 
IPv6被认为是下一代互联网协议，以弥补IPv4地址的短缺。3GPP选择将IPv6作为一种分配给UE的地址类型。SGSN支持IPv6或IPv4v6 DS PDN激活请求，也支持通过GTP隧道传输的IPv6或IPv4v6用户报文。 
## ZUF-77-16-004 SGSN支持无线资源管理 
概述 : 
SGSN支持协同实现无线信道分配和维护。 
收益 : 
便于运营商灵活配置和维护无线资源。 
描述 : 
无线资源管理是指根据特定的用户信息分配和维护无线信道。 
支持在本地SGSN中基于IMSI段配置RFSP索引。 
SGSN向RNC或BSC发送RFSP索引，RNC或BSC将其映射为相应的无线信道分配和管理策略。 
# 缩略语 
# 缩略语 
## CS 
Circuit Switched电路交换
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
## GMM 
GPRS Mobile ManagementGPRS 移动性管理
HLR : 
Home Location Register归属位置寄存器
IMSI : 
International Mobile Subscriber Identity国际移动用户标识
## LA 
Location Area位置区
## MOCN 
Multi-Operator Core Network多运营商核心网
## P-TMSI 
Packet Temporary Packet Temporary Mobile Subscriber Identity分组临时移动用户标识
PLMN : 
Public Land Mobile Network公共陆地移动网
## PS 
Packet Switched分组交换
## RFSP 
RAT/Frequency Selection Priority无线/频率选择优先级
RNC : 
Radio Network Controller无线网络控制器
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
## SNA 
Shared Network Area共享网络区域
## TMSI 
Temporary Mobile Subscriber Identity临时移动用户识别码
# ZUF-77-17 逻辑接口 
概述 : 
功能描述 : 
SGSN在处理用户移动性管理业务、切换业务、PDP激活/修改/删除、定位业务、短消息业务、联合附着、事件暴露、话单上报等业务时，通过逻辑接口和其他网元进行交互。
SGSN和周边网元逻辑接口如[图1]所示。
图1  SGSN接口架构图
功能特性简介 : 
3GPP接口与协议定义了SGSN相关的逻辑接口，详细参见下表。
方案特性|实现简述|特导链接
---|---|---
Iu接口|Iu接口是SGSN和RNC之间的接口，用于交换信令信息和用户数据。|ZUF-77-17-001 Iu接口
Gb接口|Gb接口是SGSN和BSS之间的接口，用于交换信令信息和用户数据，建立SGSN与BSS之间连接以及SGSN和MS之间连接。|ZUF-77-17-002 Gb接口
Gn/Gp接口|Gn接口是SGSN之间或SGSN和GGSN之间的接口。当SGSN和其他SGSN或GGSN处于不同的PLMN时，Gn接口被称为Gp接口。Gn接口和Gp接口具有相同的功能和连接类型。|ZUF-77-17-003 Gn/Gp接口
Gr接口|Gr接口是SGSN与HLR之间的接口。通过支持Gr接口，SGSN可从HLR/AUC获取鉴权数据。HLR可通知SGSN用户数据的变化。|ZUF-77-17-004 Gr接口
Gs接口|Gs接口位于SGSN与MSC/VLR网元之间，进行联合附着或联合RAU更新，同时实现电路域通过SGSN对用户进行寻呼。|ZUF-77-17-005 Gs接口
Gd接口|SMS-GMSC和SMS-IWMSC通过Gd接口与SGSN相连接，使SGSN可以支持SMS。通过支持Gd接口，可在PS网络上实现SMS。|ZUF-77-17-006 Gd接口
Gf接口|通过支持Gf接口，SGSN协同EIR进行IMEI检查。|ZUF-77-17-007 Gf接口
Lg接口|SGSN和GMLC可通过Lg接口提供定位业务。|ZUF-77-17-009 Lg接口
Ga接口|SGSN可将话单通过Ga接口传送给CG，并且运营商可支持离线计费。|ZUF-77-17-010 Ga接口
## ZUF-77-17-001 Iu接口 
概述 : 
Iu接口是SGSN和RNC之间的接口。 
收益 : 
Iu接口实现了来自RNC的UMTS接入。 
描述 : 
Iu接口是SGSN和RNC之间的接口，用于交换信令信息和用户数据。  
Iu接口的控制面协议栈如[图1]所示。
图1  Iu接口的控制面协议栈
Iu接口的用户面协议栈如[图2]所示。
图2  Iu接口的用户面协议栈
Iu接口支持Iu Over IP模式。 
Iu接口支持HSPA接入和HSPA+接入。SGSN是否支持HSPA+取决于RNC配置。 
SGSN为Iu接口寻呼提供消息缓存功能。当用户的Iu接口在释放后又重新连接时，SGSN可缓存接收到的用户消息（例如POC业务的请求消息）。 
可以配置每个USUP所能缓存的最大下行报文数和每个PDP所能缓存的最大下行报文数。 
## ZUF-77-17-002 Gb接口 
概述 : 
Gb接口是SGSN和BSS之间的接口。 
收益 : 
Gb接口实现来自BSS的GPRS接入。 
描述 : 
Gb接口是SGSN和BSS之间的接口，用于交换信令信息和用户数据。Gb接口用于建立SGSN与BSS之间连接以及SGSN和MS之间连接。 
Gb接口的协议栈如[图1]所示。
图1  Gb接口的协议栈
Gb接口支持Gb Over IP模式。 
Gb接口可处理R98和R99的NAS层协议消息。 
Gb接口支持LLC层实现非确认模式下的用户信令和数据包传输。Gb接口支持LLC层的XID参数协商流程。 
Gb接口支持BSSGP层上的小区管理相关信令流程，包括BVC重置和BVC闭塞/解闭塞。详细信息请参考3GPP 48018协议第8章中的相关内容。 
Gb接口支持BSSGP层上的用户相关信令流程，包括RA-CAPABILITY和Radio Status。详细信息请参考3GPP 48018协议6.3节、7.2至7.5节的内容。 
Gb接口支持PFC流程，包括新建、修改和删除BSS PFC。详细信息请参考3GPP 48018协议8a节的内容。 
SGSN支持报文缓存功能用于Gb接口寻呼。在用户返回寻呼响应之前，Gb接口缓存SGSN接收到的用户消息（例如POC业务的请求消息）。 
## ZUF-77-17-003 Gn/Gp接口 
概述 : 
Gn接口是SGSN之间或SGSN和GGSN之间的接口。当SGSN和其他SGSN或GGSN处于不同的PLMN，Gn接口被称为Gp接口。Gn接口和Gp接口具有相同的功能和连接类型。 
收益 : 
通过支持Gn/Gp接口，运营商可为SGSN和GGSN选择不同的供应商，使网络部署更加灵活。 
描述 : 
Gn/Gp接口是SGSN的一个基本接口。Gn接口是SGSN之间或SGSN和GGSN之间的接口。当SGSN和其他SGSN或GGSN处于不同的PLMN，Gn接口被称为Gp接口。Gn接口和Gp接口具有相同的功能和连接类型。 
基于IP接口，Gn/Gp接口使用GTP协议。 
## ZUF-77-17-004 Gr接口 
概述 : 
Gr接口是SGSN与HLR之间的接口。 
收益 : 
通过支持Gr接口，运营商可为SGSN和HLR选择不同的供应商。 
描述 : 
Gr接口是SGSN与HLR之间的接口。通过支持Gr接口，SGSN可从HLR/AUC获取鉴权数据。HLR可通知SGSN用户数据的变化。本接口使用MAP协议。 
## ZUF-77-17-005 Gs接口 
特性描述 : 
摘要术语描述应用场景客户收益实现原理系统影响应用限制遵循标准可获得性O&M相关 
术语 : 
术语|含义
---|---
GPRS|分组域的分组承载业务。
A/Gb模式|A/Gb模式指该子句或段落仅适用于在A/Gb模式中运行的系统或子系统，例如，根据无线接入网和核心网之间的A接口或Gb接口的使用，带有功能划分的系统或子系统。
Iu模式|Iu模式指该子句或段落仅适用于在Iu模式中运行的系统或子系统，例如，根据无线接入网和核心网之间的Iu-CS接口或Iu-PS接口的使用，带有功能划分的系统或子系统。
MS|该规范不区分MS和UE。
2G/3G|2G和3G前缀分别指支持A/Gb模式或Iu模式的系统或子系统，例如，2G SGSN是指当SGSN作为A/Gb模式下的MS时，SGSN的所有功能。
Gs|SGSN与MSC/VLR网元之间的接口。
描述 : 
定义
Gs接口位于SGSN与MSC/VLR网元之间，用于完成Class A和Class B终端进行联合附着或联合RAU更新，同时可实现电路域通过SGSN对用户进行寻呼。用户联合附着或联合RAU接入SGSN，当其位置区发生改变时，SGSN可通过Gs接口发送消息通知MSC/VLR，从而在用户和CS域无交互的情况下，MSC/VLR能获知用户当前最新的位置信息。 
Gs接口遵循3GPP 29.018协议，使用BSSAP+协议消息，采用如[图1]所示协议栈。
图1  Gs接口协议栈
Gs接口支持联合位置更新、寻呼、GPRS去附着通知、IMSI去附着通知等业务，具体业务参见下表。 
业务名称|详细描述
---|---
Paging for non-GPRS services procedure|终端附着在GPRS网络中，需要对其进行非数据业务寻呼，VLR通过发送PAGING REQUEST消息到SGSN，SGSN在Gb或Iu口将寻呼下发到终端。
Location Update for non-GPRS services procedure|Location Update for non-GPRS services procedure：非数据业务的位置更新，SGSN发送LOCATION-UPDATE-REQUEST消息，通知VLR终端的最新LAI信息、SGSN号码，VLR可以在LOCATION-UPDATE-ACCEPT消息中对终端进行TMSI重分配，SGSN使用TMSI-REALLOCATION-COMPLETE消息来通知VLR重分配结果。SGSN在以下几种场景会触发非数据业务的位置更新业务：联合IMSI/GPRS附着IMSI已附着情况下的GPRS附着路由区/位置区联合更新
Non-GPRS alert procedure|VLR发送ALERT-REQUEST消息，向SGSN请求某用户是否激活中，SGSN接收此消息，如发现用户的IMSI在SGSN能被识别，返回ALERT-ACK消息。
Explicit IMSI detach from GPRS services procedure|当用户从GPRS去附着时，SGSN发送GPRS-DETACH-INDICATION通知VLR，此用户已退出GPRS网络。
Explicit IMSI detach from non-GPRS services procedure|SGSN接收到用户的IMSI去附着或IMSI/GPRS联合去附着时，向VLR发送IMSI-DETACH-INDICATION消息，VLR对此用户进行IMSI去附着，SGSN删除此用户与VLR的关联记录。
Implicit IMSI detach from non-GPRS services procedure|由于SGSN内部定时器超时，用户的GMM上下文已过期需隐式分离，SGSN发送IMSI-DETACH-INDICATION通知VLR，同时删除此用户与VLR的关联记录。
VLR failure procedure|VLR故障恢复后，发送RESET-INDICATION消息通知相关的SGSN，同时SGSN将与此VLR相关的用户记录中，VLR-Reliable标志置为无效，因为此时VLR可能已经没有用户相关的记录信息了。
SGSN failure procedure|SGSN故障恢复后，发送RESET-INDICATION消息通知所有相关的VLR，同时将用户与VLR的关联记录清空。
HLR failure|HLR从故障中恢复，发送消息通知到SGSN后，SGSN中对进行任意业务的用户，如此业务不触发与VLR的交互，则SGSN发出MS-ACTIVITY-INDICATION消息通知VLR，VLR收到后触发到HLR的位置更新，以更新HLR中此用户的相关信息。
MS Information procedure|VLR需要从用户获得某些特性的参数信息，通过发送消息到MS-INFORMATION-REQUEST消息到SGSN，SGSN如已保存需请求的参数信息，则直接发送MS-INFORMATION-RESPONSE返回给VLR，如没有则在Gb或Iu口发送IDENTITYREQUEST，向终端用户获取。
MM information procedure|VLR通过SGSN发送MM信息到终端用户，VLR发送BSSAP+-MM-INFORMATION-REQUEST到SGSN，SGSN透传此消息到终端用户。
Error Handling and Future Compatibility|协议定义了对于接口消息出现各种错误时处理原则，各种错误包括（消息过短、消息类型未知、缺少必选参数、消息元素未知、消息元素重复等）。
Gs接口支持的协议消息参见下表。 
消息名称
---
BSSAP+-ALERT-ACK
BSSAP+-ALERT-REJECT
BSSAP+-ALERT-REQUEST
BSSAP+-GPRS-DETACH-INDICATION
BSSAP+-IMSI-DETACH-ACK
BSSAP+-IMSI-DETACH-INDICATION
BSSAP+-LOCATION-UPDATE-ACCEPT
BSSAP+-LOCATION-UPDATE-REJECT
BSSAP+-LOCATION-UPDATE-REQUEST
BSSAP+-MM-INFORMATION-REQUEST
BSSAP+-MOBILE-STATUS
BSSAP+-MS-ACTIVITY-INDICATION
BSSAP+-MS-INFORMATION-REQUEST
BSSAP+-MS-INFORMATION-RESPONSE
BSSAP+-PAGING-REJECT
BSSAP+-PAGING-REQUEST
BSSAP+-RESET-ACK
BSSAP+-RESET-INDICATION
BSSAP+-MS-UNREACHABLE
BSSAP+-TMSI-REALLOCATION-COMPLETE
背景知识
GPRS网络架构如[图2]所示。
图2  GPRS架构图
TE/MT：为终端用户完成各种数据业务和其他业务的载体，负责存储UE相关信息，完成无线资源管理功能，完成移动性管理功能，完成会话管理功能。
BSS：GPRS/EDGE(2G)的无线接入网络，为终端的接入提供无线资源。
UTRAN：第三代移动通讯网络（3G）的无线接入网络，为终端的接入提供无线资源。
HLR：永久存储用户签约数据。
PDN：为用户提供业务的网络。
CGF：将从SGSN/GGSN发送过来的话单生成CDR文件，并前转给计费系统（BS）。
BS：负责接收和处理从核心网发送过来的CDR文件。
EIR：负责检查UE设备。
PSCN：提供了低延迟，并允许2/3G无线接入系统接入。包含了如下网元：
SGSN：支持Gb或Iu接入的GPRS，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM）上下文和分组数据协议（PDP）上下文；负责处理SGSN和UE之间的所有非接入层消息；负责收集用户话单信息。
GGSN：负责UE接入PDN的网关，分配用户IP地址，同时是3GPP接入系统的移动性锚点。用户在同一时刻能够接入多个GGSN。
另外，GPRS网络也能支持联合PS/CS业务，短消息，CAMEL业务： 
MSC/VLR：通过Gs口与SGSN连接，使得SGSN支持联合PS和CS业务。
SMSGMSC/SMS IWMSC：通过Gd口与SGSN连接，使得SGSN可以支持短消息的传输。
CAMEL：该功能实体主要对用户进行在线计费。
应用场景 : 
CS域与PS域共存，运营商启用联合附着、联合RAU的网络，需SGSN与MSC/VLR支持Gs接口功能。 
客户收益 : 
受益方|受益描述
---|---
运营商|通过Gs接口，实现联合附着、联合RAU，从而减少无线资源的使用，提高资源使用率。
移动用户|减少无线信号的交互，降低终端的耗电量提高待机时间。
实现原理 : 
涉及的网元
Gs接口涉及SGSN、MSC/VLR网元、BSS/RNC、终端。 
SGSN：支持Gb或Iu接入的GPRS节点，临时存储用户数据的服务器，负责管理和存储GPRS移动性管理（GMM）上下文和分组数据协议（PDP）上下文，负责处理SGSN和UE之间的所有非接入层消息，负责收集用户话单信息。在Gs接口中，SGSN负责通知MSC/VLR当前用户最新位置信息，在用户分离时通知MSC/VLR，并且接收MSC/VLR发送过来的寻呼消息，并通过RNC/BSC对用户进行寻呼。 
MSC/VLR：完成用户发起的位置更新、附着以及语音业务。在联合附着/RAU过程中，接收SGSN发送过来的位置更新，记录用户当前最新的位置信息，对用户寻呼时，向SGSN发送寻呼消息。 
RNC/BSC：需要支持联合附着或联合RAU。 
UE终端：需要终端支持PS模式与CS模式，对只支持单模式终端不能实现Gs口功能。 
业务流程
位置更新流程SGSN在以下三种情况，会触发到MSC/VLR的Gs口位置更新流程。联合IMSI/GPRS附着。已经IMSI附着的MS进行GPRS附着。联合RA/LA（路由区/位置区）更新。图3  位置更新流程SGSN收到RNC/BSC发送的附着或RAU消息，发现为以上3种情况，SGSN获取到用户所在的LAI，根据LAI和IMSI得到配置对应的MSC/VLR局向和VLR标识。向指定MSC/VLR发送Gs接口BSSAP+-LOCATION-UPDATE-REQUEST消息，携带SGSN标识、IMSI号码及用户最新位置信息等内容。MSC/VLR收到Gs口位置更新，记录最新的位置信息和SGSN标识，向SGSN返回BSSAP+-LOCATION-UPDATE-ACCEPT
消息，SGSN收到后与MSC/VLR的Gs连接建立成功。 
Gs口寻呼图4  Gs口寻呼某用户被呼叫，MSC/VLR发现此用户存在Gs口连接，对SGSN发送BSSAP+-PAGING-REQUEST（IMSI，VLR
TMSI，位置信息）消息。如果在SGSN未找到此用户的有效记录，给MSC/VLR直接返回BSSAP+-PAGING-REJECT拒绝消息。SGSN判断此用户有效，向RNC/BSC发送Paging消息，对用户进行寻呼。 
ALERT流程MSC/VLR通知此流程，要求一旦SGSN检查到某用户活动时，通知MSC/VLR。此流程VLR可以在任何时刻触发。图5  ALERT处理流程MSC/VLR需求获得某用户是否活动，发送BSSAP+-ALERT-REQUEST消息。SGSN收到消息后，记录用户信息返回BSSAP+-ALERT-ACK响应消息。此用户活动发起业务，SGSN检测到后如此业务不会触发与MSC/VLR之间的交互，SGSN发送BSSAP+-MS-ACTIVITY-INDICATION通知MSC/VLR。 
MS信息流程MSC/VLR通过MS信令流程，从SGSN获取用户的P-TMSI、IMEI、IMEISV或位置等信息。图6  MS 信息流程MSC/VLR需要获取用户的P-TMSI、IMEI、IMEISV或位置等信息，向SGSN发送BSSAP+-MS-INFORMATION-REQUEST消息。SGSN如果记录有被请求内容，直接提取在BSSAP+-MS-INFORMATION-RESPOND带给MSC/VLR。如果SGSN没有对应信息，则向终端发出Identity Request获取相应信息，得到响应后SGSN再发送给MSC/VLR。 
MM 信息流程图7  MM 信息流程SGSN接收一个来自MSC/VLR的BSSAP+-MM-INFORMATION-REQUEST消息。其中包括网络名、本地时间等信息。SGSN直接向BSC/RNC发送MM Information消息，转发这些信息给终端。 
分离流程GPRS分离流程图8  GPRS分离流程SGSN在以下三种情况会触发Gs口GPRS分离：收到终端发起的GPRS分离，SGSN触发网络侧分离，联合RA/LA更新被SGSN拒绝。SGSN向MSC/VLR发出BSSAP+-GPRS-DETACH-INDICATION消息。MSC/VLR返回BSSAP+-GPRS-DETACH-ACK响应消息，SGSN释放Gs口连接。IMSI分离流程图9  IMSI分离流程SGSN在以下三种情况会触发Gs口IMSI分离：收到终端发起的IMSI分离，SGSN内部定时器超时，触发隐式分离。SGSN向MSC/VLR发出BSSAP+-IMSI-DETACH-INDICATION消息。MSC/VLR返回BSSAP+-IMSI-DETACH-ACK响应消息，SGSN释放Gs口连接。 
SGSN故障恢复SGSN网元自身故障恢复后，向相连的MSC/VLR发出BSSAP+-RESET-INDICATION消息，同时将具有Gs口连接的用户的SGSN-Reset标志置为有效，同时启动T12-1定时器，定时器超时后，将SGSN-Reset标志置为无效。 
HLR故障恢复SGSN收到HLR故障恢复的RESET消息后，对具有Gs口连接的用户的NGAF标志置为有效。某用户触发业务，SGSN检测其NGAF标志有效，如此次业务不触发与MSC/VLR的交互，SGSN发送BSSAP+-MS-ACTIVITY-INDICATION通知MSC/VLR，并将其NGAF置为无效。 
VLR故障恢复SGSN收到VLR故障恢复的RESET消息后，将具有Gs口连接的用户的VLR-Reliable标志置为无效。收到用户的联合RA/LA更新或周期RAU，SGSN检查其VLR-Reliable标志为无效，触发Gs口位置更新，向VLR发送BSSAP+-LOCATION-UPDATE-REQUEST消息，重新建立Gs口连接。 
Gs负荷卸载在用户联合附着情况时，用户对应的MSC/VLR需要卸载用户，由SGSN来执行Gs负荷卸载，达到将用户迁移到其他MSC/VLR的目的。在SGSN启动Gs负荷卸载之前，修改用户位置区对应的VLR，后续SGSN收到用户的联合附着或联合RAU，选择新的VLR触发Gs口位置更新，用户在新的VLR登记，新的VLR为用户到HLR登记，HLR向用户老的VLR发送Cancel，这样用户从老的VLR中迁移到新的VLR。 
系统影响 : 
支持Gs接口，增加了与MSC/VLR之间的消息交互，收发共两条消息，对系统性能影响小于5%。 
应用限制 : 
无 
遵循标准 : 
3GPP TS 23.060: "General Packet Radio Service (GPRS); Service description;
Stage 1" 
3GPP TS 29.018: " General Packet Radio Service (GPRS);Serving
GPRS Support Node (SGSN) -Visitors Location Register (VLR) Gs interface
layer 3 specification " 
可获得性 : 
License要求
无 
对其他网元的要求
MSC/VLR支持Gs接口。 
终端、BSC/RNC支持联合RA/LA更新和联合附着。 
O&M相关 : 
命令
新增软件参数参见[表2]。
软件参数ID|软件参数名称
---|---
65575|支持Gs的IMSI寻呼
65576|支持Gs的HLR故障恢复
65577|支持位置更新请求携带IMEISV
65578|支持负荷卸载中周期RAU触发Gs位置更新
65579|支持POOL组网的Gs接口
65580|支持业务失败触发Gs口消息
性能统计
性能计数器参见[表3]。
测量类型名称|性能计数器名称
---|---
PS BSSAP+信令相关测量|编号为C40536开头的所有计数器
告警和通知
无 
业务观察/失败观察
无 
话单与计费
无 
特性配置 : 
摘要配置特性测试用例常见问题处理 
配置特性 : 
配置过程
执行命令[SET COMBOCFG]，配置SGSN支持Gs接口。
执行命令[ADD ADJOFC]，增加邻接局配置。
执行命令[ADD N7SSN]，增加邻接局子系统号配置。
执行命令[ADD SCTP]，增加SCTP偶联配置。
执行命令[ADD M3UASCTP]，增加M3UA偶联配置。
执行命令[ADD M3UAASP]，增加M3UA的ASP配置。
执行命令[ADD M3UAAS]，增加M3UA的AS配置。
执行命令[ADD M3UART]，增加M3UA的静态路由配置。
执行命令[ADD SIOLOCAS]，增加SIO定位AS。
执行命令[ADD GT]，增加翻译数据配置。
执行命令[ADD MSCVLR]，增加MSC负荷分担配置。
（可选）如果RAI归属MSC pool，则需要执行命令[ADD RAI]，配置RAI归属MSC
pool。
配置实例
配置脚本|说明
---|---
SET COMBOCFG:SUPTYPE="Gs"|设置SGSN支持Gs接口。
ADD ADJOFC:ID=818,NETWORKNAME="MSC818",SPCMODE="TRIPLE_DEC",DPC="1.181.1",NET=1,SPTYPE="SEP",SPCTYPE="24"|在邻接局配置中增加MSC邻接局，需要配置的参数包括：邻接局号、网络类别、信令点编码、信令点编码类型。
ADD N7SSN:OFFICEID=818,SSN="VLRA"|配置邻接局子系统号，不同厂商VLR用于Gs口的SSN不一样，需要与对端网元约定好。
ADD SCTP:ID=818,NAME="MSC818",LOCPORT=8818,REMPORT=8818,VPNID1=0,LOCADDR1=192.10.100.218,REMADDR1=192.10.100.213,ROLE="CLT",PROTOCALTYPE="M3UA"|配置SGSN和SCP之间的SCTP偶联，用来承载M3UA协议。需要配置的参数包括：SCTP标识、应用属性、本端IP、本端端口、对端IP、对端端口。其中应用属性、本端IP、本端端口、对端IP、对端端口需要和对端网元约定好。通常SGSN侧的应用属性是SCTP客户端，应用属性明确哪个网元发起SCTP的链路建立。
ADD M3UASCTP:ASSOCID=818,SCTPPROTYPE="M3UA",OFFICEID=818|配置M3UA偶联,  将M3UA偶联与邻接局相关联。
ADD M3UAASP:ASPID=818,NAME="MSC818",ASSOCID=818|配置M3UA的ASP，将ASP和偶联标识相关联。
ADD M3UAAS:ASID=81,NAME="MSC818",EXISTCONTEXT="YES",PROTOCOL="M3UA",CONTEXTID=818,TAG="CLT",ASPID1=818|配置M3UA的AS，将AS和ASP标识相关联。是否存在选路上下文、SGSN作为IPSP的客户端还是服务端，这两个参数需要和对端网元约定好。双方如果确定使用“存在选路上下文”，则需要进一步明确选路上下文的标识，SGSN和对端网元要保持该标识一致。对于IPSP客户端还是服务端，这个和偶联SCTP应用属性一致即可，如SGSN作为偶联SCTP的客户端，则这里选择IPSP客户端。根据Gs的协议栈，协议类型选择M3UA。
ADD M3UART:ROUTEID=81,ALIAS="MSC818",ASID1=81|配置M3UA的静态路由，和AS标识关联起来。
ADD SIOLOCAS:DROUTEID=81,ALIAS="MSC818",DSTOFFICEID=818,SIO="SCCP",ROUTEID1=81|配置SIO定位AS，将目标局向和静态路由关联起来。SIO指示语为SCCP。
ADD GT:GT="861390511",TRANS=1,OFFICEID1=0,SELECTEDNUM1=1|如果没有本局GT数据配置，需要增加配置；如果已经存在，则跳过本局GT数据配置。配置本局GT翻译数据，是为了SGSN处理邻接局的GT选路消息，能够根据目的GT号码在本局落地。信令点局向是SGSN本身，对应的邻接局为0。
ADD GT:GT="8613903010",TRANS=1,OFFICEID1=818,SELECTEDNUM1=1|信令点局向选择MSC/VLR邻接局号，这里是818。
ADD MSCVLR:NAME="MSC818",LAI="LAI09",VLRCODE="8613903010",VSTART=0,VEND=999|按照V值选择MSC，LAI09下的用户（V值从0-999）都选择VLR号码为8613903010的MSC818局。
测试用例 : 
非数据业务IMSI寻呼 
测试|说明
---|---
测试项目|非数据业务IMSI寻呼
测试目的|验证非数据业务IMSI寻呼是否正常
预置条件|移动台在SGSN中Gs关联状态为：Gs－Associated。
测试过程|软件参数“支持Gs的IMSI寻呼”设置为支持。SGSN收到BSSAP+-PAGING-REQUEST携带LAI、IMSI和VLR TMSI。BSSAP+-PAGING-REQUEST中携带的LAI和SGSN MM上下文中存储的不一致。
通过准则|SGSN使用IMSI进行寻呼，寻呼范围为整个SGSN。
测试结果|正常
Alert流程 
测试|说明
---|---
测试项目|Alert流程
测试目的|验证Alert流程是否正常
预置条件|用户签约为GPRS。确保无线网络环境正常工作。
测试过程|从VLR发送ALERT REQUEST消息到SGSN。确保ALERT REQUEST消息中指定的IMSI在SGSN中存在。分别执行Attach、RAU、Service Request等流程。
通过准则|如果用户当前活动存在Gs口流程交互，清除NGAF标志即可。如果用户当前活动不存在Gs口流程交互，SGSN就需要发送BSSAP+-MS-ACTIVITY-INDICATION到MSC/VLR，同时清除NGAF标志。
测试结果|正常
MS INFORMATION 
测试|说明
---|---
测试项目|MS INFORMATION
测试目的|验证MS INFORMATION流程是否正常
预置条件|用户签约为GPRS。确保无线网络环境正常工作。
测试过程|用户从Iu口或Gb口进行联合附着流程，建立关联。用户处于PMM－IDLE或Standby状态。从VLR发送MS INFORMATION REQUEST消息，请求类型为PTMSI。
通过准则|SGSN向VLR返回MS INFORMATION RESPONSE消息，携带PTMSI，检查MS INFORMATIONRESPONSE消息中的Mobile station state是否正确。
测试结果|正常
MM INFORMATION 
测试|说明
---|---
测试项目|MM INFORMATION
测试目的|验证MM INFORMATION流程是否正常
预置条件|用户签约为GPRS。确保无线网络环境正常工作。
测试过程|移动台进行联合附着流程，建立关联。从VLR发起同一IMSI的MM INFORMATION REQUEST消息。
通过准则|在Gb口收到GMM INFORMATION消息，其中的信息即为VLR发出的MM INFORMATION REQUEST消息中所带的信息。
测试结果|正常
GPRS分离 
测试|说明
---|---
测试项目|GPRS分离
测试目的|验证SGSN能够正确受理来自联合附着的移动台的显式GPRS业务分离请求
预置条件|用户签约为GPRS。确保无线网络环境正常工作。
测试过程|移动台进行联合附着过程,建立关联。MS发起的GPRS业务分离请求。
通过准则|SGSN向MSC/VLR发起分离流程，分离类型为“MS INITIATED IMSI DETACH FROM GPRSSERVICE”。该用户已从SGSN中分离，关联状态无效。MSC/VLR中该用户的关联状态无效。
测试结果|正常
IMSI分离 
测试|说明
---|---
测试项目|IMSI分离
测试目的|验证SGSN能够正确受理来自联合附着的移动台的显式GPRS业务分离请求
预置条件|用户签约为GPRS。确保无线网络环境正常工作。
测试过程|移动台进行联合附着过程，建立关联。MS发起的IMSI离请求。
通过准则|SGSN向MSC/VLR发起分离流程，分离类型为EXPLICIT MS INITIATED IMSI DETACH FROMNON-GPRS SERVICE。SGSN中该用户仍然附着，关联无效。
测试结果|正常
SGSN故障恢复 
测试|说明
---|---
测试项目|SGSN故障恢复
测试目的|验证SGSN复位过程是否对VLR发起正确的流程
预置条件|用户签约为GPRS。确保无线网络环境正常工作。
测试过程|移动台发起联合附着流程，建立关联。启动SGSN。检查结果。
通过准则|检查Gs口，SGSN发起复位过程。MSC/VLR将系统中关联的移动台的关联状态复位，将SGSN RELIABLE标志置为FALSE。
测试结果|正常
HLR故障恢复 
测试|说明
---|---
测试项目|HLR故障恢复
测试目的|验证HLR故障恢复流程是否正常
预置条件|移动台在SGSN中Gs关联状态为：Gs－Associated。
测试过程|软件参数“支持Gs的HLR故障恢复”设置为支持。HLR重启，SGSN收到MAP_RESET消息，MM上下文中对应的NGAF值为1。用户触发Attach、RAU、Service Request等MM流程。
通过准则|下列情况由于业务本身存Gs口交互，SGSN不会向VLR发送MS-ACTIVITY-INDICATION，NGAF值变成0。附着业务：Attach Type为combined GPRS/IMSI attach。路由更新：Rau Type为combined RA/LA updating或combined RA/LA updatingwith IMSI attach。下列情况业务本身不存在Gs口交互，SGSN向VLR发送MS-ACTIVITY-INDICATION，NGAF值变成0。路由更新：Periodic updating。业务请求：Service Type为Signalling或Data。
测试结果|正常
VLR故障恢复 
测试|说明
---|---
测试项目|VLR故障恢复
测试目的|验证VLR故障恢复功能是否正常
预置条件|用户签约为GPRS。确保无线网络环境正常工作。
测试过程|移动台进行联合附着流程，建立关联。启动VLR，向SGSN发送复位消息。检查结果。
通过准则|检查Gs口，SGSN收到VLR的RESET INDICATION消息。把该VLR相关的MM CONTEXT的Gs口状态设置为Gs-NULL。VLR RELIABLE设置为FALSE，并且向VLR返回RESET ACK消息。
测试结果|正常
常见问题处理 : 
用户联合附着失败 
通过用户信令跟踪，查看附着消息中附着类型，是否为联合附着。 
通过用户信令跟踪，查看Gs口的位置更新消息交互是否成功。 
用户联合RAU失败 
通过用户信令跟踪，查看RAU消息中附着类型，是否为联合RAU。 
通过用户信令跟踪，查看Gs口的位置更新消息交互是否成功。 
## ZUF-77-17-006 Gd接口 
概述 : 
SMS-GMSC和SMS-IWMSC通过Gd接口与SGSN相连接，使SGSN可以支持SMS。 
收益 : 
通过支持Gd接口，可在PS 网络上实现SMS。 
描述 : 
SMS-GMSC和SMS-IWMSC通过Gd接口与SGSN相连接，使SGSN可以支持SMS。通过支持Gd接口，可在PS网络上实现SMS。 
Gd接口使用MAP协议。 
## ZUF-77-17-007 Gf接口 
概述 : 
Gf接口是SGSN和EIR之间的接口。 
收益 : 
通过支持Gf接口，SGSN协同EIR进行IMEI检查，从而防止非法使用移动设备，如被盗的手机。 
描述 : 
Gf接口是SGSN和EIR之间的接口。通过支持Gf接口，SGSN可进行IMEI检查，并控制是否在IMEI Check消息的扩展IE中携带IMSI。 
SGSN通过基于E1或IP协议的接口与EIR互连。 
Gf接口的协议栈如下图所示： 
## ZUF-77-17-009 Lg接口 
概述 : 
Lg接口是SGSN（或MSC）和GMLC之间的接口。 
收益 : 
SGSN和GMLC可通过Lg接口提供定位业务。 
描述 : 
GMLC通过该接口将定位请求发送给需要定位的UE的当前服务SGSN（或MSC）。SGSN（或MSC）通过该接口将定位结果回复给GMLC。 
## ZUF-77-17-010 Ga接口 
概述 : 
Ga接口是SGSN和CG之间的接口。 
收益 : 
SGSN可将话单通过Ga接口传送给CG，并且运营商可支持离线计费。 
描述 : 
Ga接口是SGSN和CG之间的接口。SGSN可将话单通过Ga接口传送给CG，并且运营商可支持离线计费。 
# 缩略语 
# 缩略语 
## BS 
Billing System计费系统
## BSS 
Base Station Subsystem基站子系统
## CAMEL 
Customized Applications for Mobile Network Enhanced Logic移动网络增强逻辑的客户化应用
## CGF 
Charging
Gateway Function 计费网关功能
## CN 
Core Network核心网
EIR : 
Equipment Identity Register设备标识寄存器
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
## GMM 
GPRS Mobile ManagementGPRS 移动性管理
## GMSC 
Gateway Mobile Switching Center网关移动交换中心
HLR : 
Home Location Register归属位置寄存器
## IWMSC 
Interworking Mobile Switching Center网间移动交换中心
MSC : 
Mobile Switching Center移动交换中心
## MT 
Mobile Terminal移动终端
PDN : 
Packet Data Network分组数据网
PDP : 
Packet Data Protocol分组数据协议
## PS 
Packet Switched分组交换
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
SMS : 
Short Message Service短消息业务
## TE 
Terminal Equipment终端设备
UTRAN : 
UMTS Terrestrial Radio Access NetworkUMTS陆地无线接入网
## VLR 
Visitor Location Register拜访位置寄存器
# ZUF-77-18 拥塞及过负荷控制 
概述 : 
功能描述 : 
SGSN网络在实际运行中，由于批量用户集中涌入、频繁的跨RAT切换、无线或核心网网元重启、节假日集中爆发业务等导致大量用户集中注册到网络，使网络负荷迅速增高。由于网络中不同类型网元的处理能力和资源不同，往往会出现由某个网元故障或宕机导致全网瘫痪。为了保证整个EPC网络的正常运行，需要各网元配合，从源头上对业务和用户实施控制，保障整个网络正常运行。
过负荷控制功能通过限制本网元接入的业务量，降低本网元或者邻接网元的负荷，避免因负荷过高导致本网元或者邻接网元设备异常或崩溃。 
功能特性简介 : 
针对SGSN入向负荷控制和出向负荷控制的应用特点、接入方式和应用场景，核心网提供了可靠、有效的解决方案。详细的解决方案特性如下表：
方案特性|实现简述|特导链接
---|---|---
Iu接口过载控制|Iu接口过载控制是RNC或SGSN在自身负荷较高时，通知对端降低发给本端的业务量，避免因本网元负荷过高导致设备异常或崩溃。当SGSN处于过负荷情况时，发送overload消息通知RNC，RNC抑制UE发起的业务。当SGSN退出过负荷状态时，会停止发送overload消息给RNC，随后RNC正常接入业务。当RNC处于过负荷情况时，也会通过overload消息通知SGSN进行过负荷处理。在RNC退出过负荷状态时，停止向SGSN发送overload消息，随后SGSN正常向RNC发送消息。|ZUF-77-18-001 Iu接口过载控制
MAP接口拥塞控制|MAP接口拥塞控制是针对HLR能力来进行自动过负荷控制。SGSN支持ALC（auto load control）功能，在业务过负荷期间，SGSN根据到HLR的业务成功率，自动对使用到HLR的业务（附着、局间RAU等）进行控制，成功率高则允许更多的业务通过，反之就降低通过的业务数量。为了保护HLR，SGSN还可以限制到HLR的鉴权、位置更新等业务通过数量，避免对HLR造成冲击。|ZUF-77-18-002 MAP接口拥塞控制
无线拥塞控制|无线拥塞控制是指RAN/eNodeB侧检测小区负载状态，若小区发生拥塞现象，则上报SGSN/SGW，SGSN/SGW通知GGSN/PGW，最终由PCEF向PCRF申请特定的预定义规则，通过SGSN下发到RAN进行小区拥塞控制策略部署，达到预防或减轻小区拥塞现象的目的。|ZUF-77-18-003 无线拥塞控制
终端异常信令管控|异常信令管控是指网络侧感知到信令风暴时，采取一定的措施，减少要处理的信令，避免网络拥塞，化解信令风暴。SGSN异常信令管控是用户级操作，且针对三种终端信令，包括附着请求信令、业务请求信令和PDP激活请求信令。当用户单位时间内的信令数超过门限值时，用户将被加入信令黑名单，SGSN对其异常信令请求进行控制。|ZUF-77-18-004 终端异常信令管控
## ZUF-77-18-001 Iu接口过载控制 
特性描述 : 
特性描述 : 
术语 : 
术语|含义
---|---
过载控制|又称过负荷控制，限制接入的业务量，来降低本网元或者邻接网元的负荷，避免因负荷过高导致设备异常或崩溃。
描述 : 
定义 : 
Iu接口过载控制是RNC或SGSN在自身负荷较高时，通知对端降低发给本端的业务量，避免因本网元负荷过高导致设备异常或崩溃。
背景知识 : 
过载控制是保障网元安全运行的重要措施，在实际应用中，经常会出现因为某些特定的原因，导致用户短时间内暴发超过正常话务模型的业务量。这些原因包括：网元重启、传输网故障、用户大量移动、节假日以及特殊事件等。此时如果不进行过载控制，网元的处理能力、资源以及接口带宽都可能达到极限，最终导致网元崩溃，并形成雪崩效应使得整个网络瘫痪。 
根据过载发生的范围和控制的层次，过载控制分为以下几种： 
面向终端和应用的端到端过载控制。 
面向GSM\UMTS网络的网元间动态过载控制。 
针对单一网元的网元自身过载控制。 
网元间的动态过载控制
GSM\UMTS网络在实际运行中，有多种造成网络信令负荷增高的原因，例如：特定区域大批用户涌入引发的注册信令、频繁的跨RAT切换、无线或核心网网元重启造成的大量用户重新接入、节假日集中爆发的业务等。一旦出现过载，由于网络中不同类型的网元处理能力和资源各不相同，往往会出现由某个网元故障或宕机导致的全网瘫痪。因此为了保证整个GSM\UMTS网络的正常运行，就需要各网元配合，从源头上对业务和用户实施控制，来完成整个网络的过载控制。
网元自身的过载控制
SGSN是GSM\UMTS网络中的移动性管理网元，也是终端的控制面接入点，一旦遇到业务量突然增加的情况，SGSN将更加直接地受到冲击，自身资源（包括处理能力、内部资源、外部接口带宽等）将迅速耗尽。如果SGSN网元宕机，将会对整个GSM\UMTS网络造成巨大的影响。因此，SGSN网元需要保障自身正常运行的机制，实现自身的过载控制。 
为了防止出现以下情况影响整个系统，各个设备上都需要使用过载控制。 
在各个网元中，经常会出现因为某些原因，例如网元重启、对方网元不可达，用户大量移动等，导致用户短时间内暴发超过正常话务模型的业务量。此时，SGSN网元的处理器CPU资源、数据区资源、甚至接口或内部交换带宽都可能到达极限，从而导致系统崩溃。 
SGSN网元处理能力很强，突然涌现的业务，对自身可能影响不大，但周边MAP接口网元（HLR\EIR\SMS-IWMSC）可能会比较老旧，无法处理突发业务，也没有过载保护，从而导致系统崩溃，而周边MAP接口网元的宕机也会导致SGSN自身网元的业务无法进行。 
ZXUN uMAC网元（MME/SGSN）过载控制功能参见[表1]。
功能名称|功能概述
---|---
入向业务总量控制|控制单位时间内允许通过的业务总量，业务总量的计算为各个单项业务的加权叠加。
入向单项业务控制|控制单位时间内通过的各个单项业务量。
CPU过载控制|根据CPU拥塞情况对各类业务限制一定的通过率，保护CPU不会过载。
出向单项业务控制|对于本端发起的到其他网元的业务，比如到HSS、EIR、HLR、SMS-IWMSC，限制一定的业务量，保护对端网元不会被冲击。
信令过载控制|根据信令链路拥塞情况，保护信令链路。
网元过载控制|对于MME/SGSN网元，协议支持Iu、S1接口Overload消息。MME/SGSN发送Overload消息，通知对端网元本端的过载情况，对端就会控制发送的信令。对于Iu接口，SGSN和RNC可以互相通知，对于S1接口，只能MME通知eNodeB。
在业务量突然增加时，ZXUN uMAC为了保障自身工作正常，可通过以下方式控制本网元处理的业务量。
使用入向业务控制功能（包括总量和单项业务量）和CPU过载控制功能。 
通知RNC/eNodeB网元，本端业务已经过载，需要RNC/eNodeB网元控制接入到本端网元的业务量。 
如果周边网元，如HLR/HSS处理能力较弱，ZXUN uMAC为了保障周边网元安全，可通过以下方式控制输出到该网元的业务量。
使用出向单项业务控制功能和信令过载控制功能。 
接收RNC的过载通知，减少该RNC的业务量。 
应用场景 : 
当本SGSN负荷较高时，通过Iu接口过载控制，限制部分RNC发给本SGSN的业务，使SGSN的负荷稳定在一个正常的范围。负荷“削峰”，可以保证业务成功率，从而平滑地接入用户业务。 
Iu接口过载控制可以用于以下场景： 
遭遇突发业务场景ZXUN uMAC网元接入超过估算话务模型的业务量，CPU占用量陡增。例如，举办大型赛事，大量外地用户涌入。 
ZXUN uMAC设备升级场景在设备升级时，一般都需要整局重启。在重启后，本局的所有用户都会快速重新附着，导致单位时间内的用户附着数过高。 
客户收益 : 
受益方|受益描述
---|---
运营商|防止网元设备被突发大量业务冲击，在突发大话务的情况下，不会异常或者崩溃，提高网络的稳定性。
移动用户|网元设备被大量业务冲击造成网络瘫痪，移动用户无法接入网络， 通过Iu接口过载控制，限制RNC或SGSN发给对端的业务量，逐步放行，保证用户能平滑地接入网络。
实现原理 : 
系统架构 : 
Iu接口过载控制网络结构如[图1]所示。
图1  Iu接口过载控制网络结构
###### 涉及的网 
网元名称|网元作用
---|---
RNC|当本端RNC过载时，向SGSN发送Overload消息；收到SGSN的Overload消息，对发送对端的业务进行过载控制。
SGSN|当本端SGSN过载时，向RNC发送Overload消息；收到RNC的Overload消息，对发送对端的业务进行过载控制。
协议栈 : 
Iu接口协议栈如[图2]所示。
图2  Iu接口协议栈
本网元实现 : 
Iu接口过载控制包括SGSN过载处理和RNC过载处理。 
SGSN过载处理SGSN定时检测本端CPU负荷，如果CPU超过过负荷门限，则随机选择RNC发送Overload消息，支持发送消息的间隔时间可配置。 
RNC过载处理SGSN收到RNC的Overload消息时，开启TigOC、TinTC定时器，来维护对端RNC的过载step。图3  RNC过载step计算当RNC的过载step不为0时，SGSN对该RNC进行网元过载控制，减少发往该RNC的寻呼、切换消息。 
业务流程 : 
Iu接口过载控制业务流程如[图4]所示。
图4  Iu接口过载控制业务流程
当SGSN检测到本网元过载时，随机选择RNC发送Overload消息，RNC限制发往该SGSN的业务。 
当RNC检测到本网元过载时，向SGSN发送Overload消息，SGSN限制发往该RNC的业务。 
系统影响 : 
开启Iu接口过载控制功能时，RNC和SGSN在对方过载时，会拒绝部分发往对方的业务，导致部分业务失败。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准名称|章节
---|---
3GPP TS 25.413 UTRAN Iu interface Radio Access Network Application Part (RANAP) signalling|8.25.3
特性能力 : 
该特性不涉及规格指标。 
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 : 
该特性为ZXUN uMAC的基本特性，无需License支持。
对其他网元的要求 : 
UE|RNC|SGSN|HLR|MSC
---|---|---|---|---
-|√|√|-|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 : 
命令 : 
配置项参见表2。表2  新增配置项配置项命令过负荷基本参数配置SET OVERLOAD BASIC PARASHOW OVERLOAD BASIC PARASGSN通用过负荷参数配置SET OVERLOAD PARASHOW OVERLOAD PARASGSN通用业务控制配置SET SERVICE CONTROLSHOW SERVICE CONTROL 
安全变量该特性不涉及安全变量。 
软件参数该特性不涉及软参。 
动态管理该特性不涉及动态管理。 
性能统计 : 
新增性能计数器参见[表3]。
测量类型|描述
---|---
SGSN Iu/Gb口过负荷性能统计|编号为C40527开头的所有SGSN-Iu计数器
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
该配置过程实现Iu接口过载控制功能。 
配置前提 : 
SGSN和RNC基本业务正常。 
配置过程 : 
执行[SET OVERLOAD BASIC PARA]命令，配置过负荷基本参数。
执行[SET OVERLOAD PARA]命令，配置SGSN通用过负荷参数。
执行[SET SERVICE CONTROL]命令，配置SGSN通用业务控制。
配置实例 : 
场景说明 : 
SGSN网元CPU占用率过高，通知RNC Overload消息。 
RNC过载，通知SGSN Overload消息。 
 说明： 
SGSN和RNC可以互相通知Overload消息，但是只能配置SGSN的过载参数，无法配置RNC的过载参数。 
数据规划 : 
配置项|参数|取值
---|---|---
设置过负荷基本参数|业务控制周期(100ms)|10
评判周期/业务控制周期|设置过负荷基本参数|5
是否开启CPU拥塞控制|设置过负荷基本参数|是
拒绝/丢弃策略|设置过负荷基本参数|丢弃
CPU拥塞门限|设置过负荷基本参数|75
CPU高拥塞门限|设置过负荷基本参数|85
缓冲区大小|设置过负荷基本参数|5
设置SGSN通用过负荷参数|开始发送overload时的最小拥塞级别|低过载
每发送overload到RNC的报文间隔|设置SGSN通用过负荷参数|300
是否根据overload消息控制Iu口下行业务|设置SGSN通用过负荷参数|是
设置SGSN通用业务控制|高优先级业务|路由区更新、切换
每模块每秒保证通过业务数|设置SGSN通用业务控制|1000
每模块每秒通过附着业务个数|设置SGSN通用业务控制|100
附着业务权重|设置SGSN通用业务控制|10
每模块每秒通过业务请求业务个数|设置SGSN通用业务控制|100
业务请求业务权重|设置SGSN通用业务控制|6
拒绝/丢弃策略|设置SGSN通用业务控制|丢弃
配置步骤 : 
步骤|说明|命令
---|---|---
1|设置过负荷基本参数，启用过负荷控制|SET OVERLOAD BASIC PARA:CTRLTIMER=10,JUDGETIMER=5,CPUENABLE="YES",REJECT="Discard",THRESHOLD=75,HTHRESHOLD=85,BUFFER=5
2|设置SGSN通用过负荷参数，SGSN根据该配置发送Overload|SET OVERLOAD PARA:OLSLOWLEVEL="Slightly",OLSINTERVAL=300,OLIUDNCTRL="YES"
3|设置SGSN通用业务控制|SET SERVICE CONTROL:HPRISVRI="RAU"&"HO",SERVICENUMG=""-""-""-""-""-""-"1000"-"1000",ATTNUM=100,ATTWGT=10,SVRREQNUM=100,SVRREQWGT=6,REJECT="Discard"
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|验证SGSN过载，向RNC发送Overload消息
---|---
测试目的|SGSN在高负荷运行期间，通知RNC过载，RNC减少发给SGSN的业务消息。
预置条件|SGSN的CPU占用率过高。
测试过程|SGSN在高负荷运行期间向RNC发送Overload消息。
通过准则|检测到SGSN发出Overload消息，通知RNC过载。SGSN的业务量降低。
测试结果|–
测试项目|验证RNC过载，SGSN减少发送给RNC的业务消息
---|---
测试目的|SGSN收到RNC发送的Overload消息，减少发送给RNC的业务消息。
预置条件|RNC过载。
测试过程|SGSN收到RNC发送的Overload消息。
通过准则|检测到SGSN减少向RNC发送的业务消息。
测试结果|–
常见问题处理 : 
无。 
## ZUF-77-18-002 MAP接口拥塞控制 
特性描述 : 
特性描述 : 
术语 : 
无。 
描述 : 
定义 : 
拥塞和过负荷控制，是指当网络中因各种原因发生业务拥塞和网元过负荷时，对接入业务和用户实施的控制，以达到降低业务和整个网络的负荷，保证网元长期有效地正常运行的目的。 
MAP接口拥塞控制指SGSN和HLR\EIR\IWMSC\SMS-IWMSC网元进行业务处理过程中，对入向和出向业务进行负荷控制。 
背景知识 : 
拥塞和过负荷控制是网元运行安全保障的重要措施；在现网的实际应用中，经常会出现因为某些特定的原因导致用户短时间内暴发超过正常话务模型的业务。这些原因包括：网元重启、传输网故障、用户大量移动、节假日以及特殊事件等。此时，如果不进行拥塞控制，网元的处理能力、资源以及接口带宽都可能达到极限，最终导致网元崩溃，并形成雪崩效应使得整个网络瘫痪。 
根据拥塞和过负荷发生的范围和控制的层次，拥塞和过负荷控制分为： 
面向终端和应用的端到端拥塞控制。 
面向GSM\UMTS网络的网元间动态过负荷控制。 
针对单一网元的网元自身过负荷控制。 
网元间的动态过负荷控制
GSM\UMTS核心网在实际运行中，有多种造成GSM\UMTS网络信令负荷增高的原因，例如：特定区域大批用户涌入引发的注册信令、频繁的跨RAT切换、无线或核心网网元重启造成的大量用户重新接入、节假日集中爆发的业务等。一旦出现过负荷，由于网络中不同类型的网元处理能力和资源各不相同，往往会出现由某个网元故障或宕机导致的全网瘫痪。为了保证整个GSM\UMTS网络的正常运行，需要各网元配合，从源头上对业务和用户实施控制，来完成整个网络的过负荷控制。 
网元自身的过负荷控制
SGSN是GSM\UMTS网络中的移动性管理网元，也是终端的控制面接入点，一旦遭遇到业务量突发增加的情况，SGSN将更加直接的受到冲击，自身资源（包括处理能力、内部资源、外部接口带宽等）将迅速趋于耗尽。如果SGSN网元宕机，对整个SGSN网络的影响也十分巨大；因此，SGSN网元需要增加保障自身正常运行的机制，实现自身的过负荷控制。 
为了防止以下情况而引起突发业务冲击对整个系统的影响，各个设备上必须使用过负荷控制。 
在各个网元中，经常会出现因为某些原因（例如网元重启后、对方网元不可达，用户大量移动）导致用户短时间内暴发超过正常话务模型的业务请求次数。此时，SGSN网元的处理器CPU资源、数据区资源、甚至接口或内部交换带宽都可能达到极限能力，从而导致系统崩溃（例如CPU占用率长时间100%会导致自愈系统认为故障而复位），同时对外围网元也会造成冲击（例如，对HLR的冲击）。 
SGSN网元处理能力很强，突然涌现的业务对自身影响不大。周边MAP接口网元（HLR\EIR\SMS-IWMSC）由于比较老旧，无法处理突发业务，也没有过负荷保护，从而导致系统崩溃，而周边MAP接口网元的宕机会导致了SGSN网元自身的业务也无法进行。 
SGSN网元提供的过负荷控制功能参见[表1]。
功能名称|功能概述
---|---
入向业务总量控制|控制单位时间内允许通过的业务总量，业务总量的计算为各个单项业务的加权叠加。
入向单项业务控制|控制单位时间内通过的各个单项业务量。
CPU拥塞控制|在MP上根据CPU拥塞情况对各类业务限制一定的通过率，保护MP CPU不会冲高。
出向单向业务控制|对于本系统发起的到其他网元（比如HSS、EIR、HLR、SMS-IWMSC）的业务，限制一定的业务量，保护对方网元不会被冲击
信令拥塞控制|对于信令处理MP按照信令链路拥塞情况，保护信令链路
按网元拥塞控制|对于MME/SGSN，协议支持Iu、S1口overload消息，可以告知对方网元本局拥塞情况，接收overload消息的网元就会控制本方发送的信令。对于Iu口，SGSN和RNC可以互相通知；对于S1口，只有MME通知eNodeB。
应用场景 : 
###### 突发业务场景 
SGSN网元接入超过估算话务模型的业务量，CPU占用陡升。例如，举办大型赛事，大量外地用户涌入。uMAC SGSN网元可采用以下过负荷控制功能来保证自身和外部网元安全。 
入向业务总量控制功能 
入向业务单项控制功能 
CPU拥塞控制功能 
按网元拥塞控制功能 
 说明： 
建议开启“CPU拥塞控制功能”（该功能默认开启），CPU的过载门限为75%，高过载门限为85%。在过载拥塞时只对低优先级业务（默认为Attach、Service Request等）进行控制，在CPU高过载时对所有业务进行控制，包括高优先级业务（默认为RAU、HO）。 
如果持续出现过负荷告警，建议通过扩容来降低uMAC设备的负荷。 
###### 设备升级场景 
在SGSN设备升级时，一般都需要整局重启。重启后，本局的所有用户都会重新附着，导致单位时间内的用户附着数很高，对外部网元的冲击也会陡然增加。例如，终端重新附着，发送给HLR的位置更新请求单位时间内增加很多，造成HLR负荷上升。 
SGSN网元可采用以下过负荷控制功能来保证自身安全： 
入向业务总量控制功能 
入向业务单项控制功能 
CPU拥塞控制功能 
按网元拥塞控制功能 
 说明： 
建议除使用默认开启的“CPU拥塞控制功能”外，开启“入向单项业务控制功能”对Attach业务进行限制。 
限制的数值为1小时内所有用户接入的速率，即全部接入的用户数/MP模块数/3600。例如：本局有100万用户，16个模块，则需要限制Attach接入业务数为1000000/16/3600=17次。 
###### 邻接网元处理能力弱场景 
HLR/EIR/SMS-IWMSC等MAP接口网元是老的网元或未完成扩容，因此整体处理能力弱。在SGSN业务繁忙时，外部网元无法及时处理位置更新\短消息\设备识别等业务，甚至出现了宕机重启的情况。 
uMAC网元提供了如下功能来保护邻接网元： 
出向单项业务控制功能 
信令拥塞控制功能 
 说明： 
除了默认开启的“信令拥塞控制功能”外，还建议开启“出向单项业务控制功能”，对SGSN发出的业务进行控制。 
例如，评估HLR最多处理1000条/秒位置更新业务消息，则可以在出向单项业务控制功能中配置本局到该HLR局向最多发送1000条/秒位置更新业务消息。 
客户收益 : 
受益方|受益描述
---|---
运营商|防止设备在突发大话务情况下因大量业务冲击而发生异常或崩溃，同时不对周边网元（HLR/EIR/SMS-IWMSC等）造成冲击，提高网络的稳定性。
移动用户|防止在突发大话务情况下，引起移动用户长时间无法接入网络。
实现原理 : 
系统架构 : 
MAP接口拥塞控制的系统架构如[图1]所示（涉及红线标识的接口）。
图1  MAP接口拥塞控制的系统架构图
涉及的网元 : 
网元名称|网元作用
---|---
SGSN|接收HLR的过负荷通知，完成拥塞控制。接收EIR的过负荷通知，完成拥塞控制。接收SMS-IEMSC的过负荷通知，完成拥塞控制。完成SGSN过负荷控制。
HLR/HSS|通知SGSN，HLR/HSS设备发生拥塞。
SMS-IWMSC\SMS-GMSC|通知SGSN，SMS-IWMSC\SMS-GMSC网元设备发生拥塞。
协议栈 : 
SGSN与HLR之间的Gr接口协议栈如图2所示。 
SGSN与SMS-GMSC/SMS-IWMSC之间的Gd接口协议栈同Gr接口协议栈，如图2所示。 
图2  Gr接口协议栈
本网元实现 : 
SGSN过负荷控制功能如[图3]所示。
图3  过负荷控制功能
当SGSN发现自身CPU负荷过高，处理能力不足的情况下，可以有选择地拒绝来自UE以及GGSN、MSC、HLR等各项业务接入。当自身CPU负荷和业务负荷过高时，对HLR或SMS-GMSC\SMS-IWMSC消息量增加，造成老旧或处理能力弱的网元拥塞。 
SGSN在实施控制时，针对业务流程的首个消息实施控制，而对后续消息放行。在系统负荷允许的范围内通过尽量多的业务。用户业务被拒绝后，通过重新尝试，可以逐渐平滑的接入进来。 
对于HLR或SMS-GMSC\SMS-IWMSC网元，通过控制发送消息数量防止对端网元因负荷过高而拥塞。 
业务流程 : 
HLR网元过负荷控制由于网络故障引发大量UE重新附着，或者因节假日业务激增等原因，引发HLR短时间内突发大量的业务，发生过负荷。HLR发送过负荷后， SGSN发送给HLR的MAP对话会被拒绝丢弃，HLR会触发MAP-U-ABORT和MAP-P-ABORT过程，SGSN出现大量超时和对端失败。SGSN根据HLR的拥塞程度，减少到该HLR的消息数量，逐步缓解HLR的负荷，直到正常。 
SMS-GMSC\SMS-IWMSC网元过负荷控制由于网络故障或者因节假日短信业务激增等原因，引发SGSN短时间内突发大量短信业务，导致SMS-GMSC\SMS-IWMSC过负荷。SMS-GMSC\SMS-IWMSC发送过负荷后， SGSN发送给MAP对话会被拒绝丢弃，SMS-GMSC\SMS-IWMSC会触发MAP-U-ABORT和MAP-P-ABORT过程，SGSN出现大量超时和对端失败。SGSN根据SMS-GMSC\SMS-IWMSC的拥塞程度，减少到该SMS-GMSC\SMS-IWMSC的消息数量，逐步缓解SMS-GMSC\SMS-IEMSCIWMSC的负荷，直到正常。 
系统影响 : 
开启拥塞和过负荷控制功能后，当系统处于拥塞或过负荷的情况下，会采用简单有效的方法拒绝部分业务处理，从而降低系统负荷。拥塞控制功能本身对系统处理能力和资源消耗可以忽略。 
应用限制 : 
SGSN侧对UE尝试的业务实施持续的接入控制后，如果UE在短时间内多次发起尝试，会对网络处理能力和资源有少许消耗。 
SGSN对出向消息进行控制，会导致UE附着或者短消息会出现失败情况。UE不断尝试发起业务，会对网络处理能力和资源有少许消耗。但随着UE按比例逐渐恢复业务，SGSN网元的负荷会逐渐归于正常。 
特性交互 : 
相关特性|交互关系
---|---
紧急呼叫|紧急呼叫在拥塞控制中，具备最高优先级，作为最后被限制的业务。
遵循标准 : 
标准名称|章节
---|---
3GPP TS 23.401: “General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access”|4.3.7.1a GTP-C signalling based Load and Overload Control；4.3.7.4 MME control of overload4.3.7.5 PDN GW control of overload
3GPP TS 29.002: "Mobile Application Part (MAP) specification"|5.1.1 Overload control for MSC (outside MAP)5.1.2 Overload control for MAP entities
3GPP TS 25.413: "UTRAN Iu interface Radio Access Network Application Part (RANAP) signaling”|—
特性能力 : 
名称|指标
---|---
支持HLR过负荷控制的最大节点数|2048（个）
支持SMS-GMSC\IWMSC过负荷控制的最大节点数|2048（个）
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 : 
该特性为产品基本特性，无需License支持。 
对其他网元的要求 : 
UE|RNC|SGSN|HLR|SMS-GSMC\SMS-IWMSC
---|---|---|---|---
-|-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
该特性不涉及工程规划要求。 
O&M相关 : 
命令 : 
配置项新增配置项参见下表。配置项命令SGSN特定局向业务控制配置ADD SGSN OFFICE SERVICE MAXIMUMSET SGSN OFFICE SERVICE MAXIMUMDEL SGSN OFFICE SERVICE MAXIMUMSHOW SGSN OFFICE SERVICE MAXIMUM 
安全变量该特性不涉及安全变量。 
软件参数该特性不涉及软参。 
动态管理该特性不涉及动态管理。 
性能统计 : 
新增SGSN性能计数器参见下表。 
测量类型|描述
---|---
SGSN Gr/Gf口过负荷性能统计（40583）|编号为C40583开头的所有计数器。
SGSN Gd/Gs/Ge口过负荷性能统计（40584）|编号为C40584开头的所有计数器。
告警和通知 : 
该特性控制MAP口局向HLR\SMS-GMSC的消息数量，新增告警参见下表。 
告警码
---
2114584630 业务过负荷告警
业务观察/失败观察 : 
该特性不涉及业务观察/失败观察的变化。 
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
MAP接口拥塞控制功能默认关闭，SGSN支持根据局向配置到HLR和SMC的拥塞控制。 
配置前提 : 
已完成SGSN基本数据配置。 
配置过程 : 
根据本网元SGSN实际负荷以及邻接HLR/SMC网元负荷能力，执行[ADD SGSN OFFICE SERVICE MAXIMUM]命令，新增SGSN特定局向业务控制配置。
配置实例 : 
场景说明 : 
当HLR/EIR/SMS-IWMSC/SMS-GMSC网元整体处理能力弱，SGSN业务繁忙时，为防止对这些邻接网元产生冲击，SGSN上启用“MAP接口拥塞控制功能”。
数据规划 : 
配置项|参数名称|取值
---|---|---
新增SGSN特定局向业务控制配置|局向ID|1
每模块每秒到HLR鉴权最大数目|新增SGSN特定局向业务控制配置|100
每模块每秒到HLR位置更新最大数目|新增SGSN特定局向业务控制配置|200
每模块每秒到SMC短消息最大数目|新增SGSN特定局向业务控制配置|300
配置步骤 : 
步骤|说明|命令
---|---|---
1|新增SGSN特定局向业务控制配置|ADD SGSN OFFICE SERVICE MAXIMUM:ADJID=1,HLRAUTHNUM=100,HLRLUNUM=200,SMCSMSNUM=300
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|MAP接口信令拥塞控制
---|---
测试目的|测试MAP接口信令拥塞控制功能是否正常。
预置条件|SGSN网元完成基础配置，用户可以正常进行各项业务。
测试过程|在SGSN上配置特定局向的业务控制。示例如下：ADD SGSN OFFICE SERVICE MAXIMUM:ADJID=1,HLRAUTHNUM=100,HLRLUNUM=200,SMCSMSNUM=300
通过准则|SGSN上MP模块每秒发给HLR的最大鉴权数目为100，MP模块每秒发给HLR位置更新最大数目为200，MP模块每秒发给SMC短消息最大数目为300。
测试结果|消息数不超过业务控制配置值。
常见问题处理 : 
无。 
## ZUF-77-18-003 无线拥塞控制 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
无线拥塞控制是指RAN/eNodeB侧检测小区负载状态，若检测结果表明小区发生拥塞现象，则上报给SGSN/SGW转发到GGSN/PGW，最终由PCEF向PCRF申请用于无线侧拥塞控制的预定义规则，下发到RAN/eNodeB进行小区拥塞控制策略部署，达到预防或减轻小区拥塞现象的目的。
背景知识 : 
网络的吞吐量与通信子网负荷有着密切的关系。当通信子网负荷比较小时，网络的吞吐量随网络负荷的增加而线性增加。当网络负荷增加到某一值后，若网络吞吐量反而下降，则说明网络中出现了拥塞现象。 
应用场景 : 
无线拥塞控制可以部署在无线侧，检测小区内的负载状态，上报拥塞现象报告，并依据下发的拥塞控制策略，预防或减轻拥塞现象。 
无线侧RNC/eNodeB检测小区负载状态，若发生拥塞现象，则会在上行的IuPS/S1-U的GTP-U消息里携带一个特殊的字段，这个字段指示发生了拥塞。 
SGSN/SGW把对应的表示拥塞的字段转发给GGSN/PGW，由PCEF向PCRF申请特定的预定义规则。 
无线侧RNC/eNodeB根据PCRF分配的拥塞控制规则对小区拥塞现象进行预防或处理。 
客户收益 : 
受益方|受益描述
---|---
运营商|在小区部署无线拥塞控制功能，依据不同用户类型定制服务，能预防或减轻小区拥塞现象。
终端用户|享受更优质的网络服务体验。
实现原理 : 
涉及的网元 : 
网元名称|网元作用
---|---
RNC/eNodeB|检测小区负载拥塞，上报小区拥塞状态标识。
SGSN/SGW|依据协议决定是否透传GTP-U消息。
GGSN/PGW|申请特定的预定义拥塞控制规则。
PCRF|分配特定的预定义拥塞控制规则。
协议栈 : 
该特性涉及的接口协议栈如下图所示。 
图1  Iu口协议栈
本网元实现 : 
SGSN/SGW收到携带拥塞状态字段的GTP-U消息，依据协议29281中定义的GTP-U扩展头规则，决定是否透传该GTP-U消息到GGSN/PGW。 
在协议中定义了GTP-U的扩展头，GTP-U扩展头格式如[表1]所示。
字节|含义
---|---
1|扩展头长度。扩展头长度为可变的，但应该被定义为4字节的倍数，即：m+1=n×4（字节），其中n为扩展头长度值。
2-m|扩展头内容。
m+1|下一个扩展头类型。下一个扩展头类型的值指示了该特殊扩展头后是否存在新的扩展头，同时保存了新的扩展头类型值。如果不存在新的扩展头，则设置下一个扩展头类型的值为0。
扩展头类型值的第7、8比特位规定了接收者如何处理未知类型的扩展头，其含义如[表2]所示。
比特位8|比特位7|含义
---|---|---
0|0|不需要解析这个扩展头。中间节点应将其转发到任一接收端点。
0|1|不需要解析这个扩展头。中间节点应将该扩展头内容丢弃，不要将其转发到任一接收端点。每一个扩展头均应被独立处理。
1|0|扩展头需要被接收端点解析，但中间节点不需要解析。中间节点应将其完整的转发到接收端点。
1|1|扩展头类型需要被接收者（接收端点或中间节点）解析。
业务流程 : 
无线拥塞控制功能业务流程如下： 
RNC/eNodeB检测到小区出现负载拥塞，将小区拥塞状态标识封装到GTP-U消息的扩展头中，通过上行的IuPS/S1-U数据传输发送到SGSN/SGW。 
SGSN/SGW解码出GTP-U头中的“下一个扩展头类型”字段，其大小为1字节，根据该字段8、7比特位取值的含义，决定是否对GTP-U扩展头透传转发到GGSN/PGW。 
GGSN/PGW收到的GTP-U消息，若携带扩展头，且解析得到小区拥塞状态标识，由PCEF向PCRF申请用于无线侧拥塞控制的预定义规则。 
RNC/eNodeB部署下发的小区拥塞控制规则，预防或减轻小区拥塞现象。 
系统影响 : 
该特性不涉及对系统的影响。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
该特性不涉及与其他特性的交互。 
遵循标准 : 
标准名称
---
3GPP TS 29.281:"GTP-U Extension Header"
特性能力 : 
名称|指标
---|---
限制最大携带GTP-U扩展头数量|4
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
01|V7.18.10|首次发布。
License要求 : 
该特性为uMAC产品的基本特性，无需License支持。 
对其他网元的要求 : 
UE|eNodeB|SGSN|PGW|HSS
---|---|---|---|---
-|√|√|√|√
UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 : 
无。 
O&M相关 : 
命令 : 
配置项无新增配置项。 
安全变量无新增安全变量。 
软件参数软件参数ID软件参数名称393267SGSN支持Iu口GTP-U扩展头 
动态管理无新增动态管理。 
性能统计 : 
该特性不涉及计数器的变化。 
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
无线拥塞控制功能默认关闭，可根据实际情况决定是否开启该功能。 
完成该功能的配置，可以预防或减轻小区拥塞现象。 
配置前提 : 
MME/SGSN基础配置已经完成，网络环境可以正常运行。 
配置过程 : 
执行[SET SOFTWARE PARAMETER]命令，配置软件参数。
配置实例 : 
场景说明 : 
将无线拥塞控制功能配置为开启。 
数据规划 : 
配置名称|参数|取值
---|---|---
软件参数ID|PARAID|393267
软件参数值|PARAVALUE|1
配置步骤 : 
步骤|说明|操作
---|---|---
1|将“SGSN支持Iu口GTP-U扩展头”功能配置为开启|SET SOFTWARE PARAMETER:PARAID=393267, PARAVALUE=1;
调整特性 : 
无。 
测试用例 : 
测试项目|无线拥塞控制功能
---|---
测试目的|验证SGSN/SGW能够依据协议规则，透传GTP-U扩展头。
预置条件|无线拥塞控制功能开启。小区出现负载拥塞。
测试过程|RNC/eNodeB检测到小区负载拥塞，上报携带小区拥塞状态标识的GTP-U消息。抓包对比SGSN/SGW接收与转发的GTP-U消息中扩展头内容。
通过准则|SGSN/SGW透传的GTP-U消息携带的扩展头类型值的8、7比特位符合协议中规定的透传设定值。
测试结果|-
常见问题处理 : 
无。 
## ZUF-77-18-004 终端异常信令管控 
特性描述 : 
特性描述 : 
描述 : 
定义 : 
异常信令管控是指网络侧感知到信令风暴时，采取一定的措施，减少网络侧要处理的信令，避免网络拥塞，化解信令风暴。 
SGSN异常信令管控包含如下功能：
附着请求异常信令管控 
业务请求异常信令管控 
PDP激活请求异常信令管控 
背景知识 : 
引发信令风暴的原因有很多，主要包括如下原因： 
特殊事件：由于集会、节日、传输中断等导致短时间内大量用户发起业务，带来的信令冲击超过网络的处理能力。 
核心网的设备故障、重启或用户卸载等场景触发大量用户同时重新连接网络，触发信令风暴。 
终端问题：因下述原因，终端业务连续失败后，终端会不断重发信令请求，附着请求/业务请求/PDP激活请求频繁发生。当一定时间内信令请求数很多，即将超过网络信令资源的处理能力，就会触发信令风暴。终端APN或其他参数错误终端中毒终端恶意攻击网络传输中断区域限制业务服务器Down其他原因 
不同原因导致的信令风暴，其抑制手段也不同： 
特殊事件：SGSN启用智能过负荷控制，保证发生信令风暴时正常服务。 
设备故障：SGSN启用智能过负荷控制，保证发生信令风暴时正常服务。 
终端问题：SGSN对附着请求/业务请求/PDP激活请求信令进行信令黑名单控制，避免网络拥塞，化解信令风暴。 
应用场景 : 
本功能应用于包括但不限于以下原因导致的终端业务连续失败后，不断重发附着请求、业务请求、PDP激活请求，从而触发信令风暴的场景： 
终端APN或其他参数错误 
终端中毒 
终端恶意攻击网络 
传输中断 
区域限制 
业务服务器Down 
其他原因 
客户收益 : 
受益方|受益描述
---|---
运营商|确保网络设备安全运行：减轻网络信令压力，化解信令风暴，避免网络拥塞。提高用户满意度：保障用户使用数据业务和业务的成功率，从而提高用户满意度，增加收益。提升运营商KPI指标：抑制终端频繁发起信令请求导致的业务失败，提升了业务成功率。
移动用户|用户享受更稳定和更可靠的网络服务。
实现原理 : 
系统架构 : 
本特性的系统架构如[图1]所示。
图1  系统架构图
涉及的网元 : 
异常信令管控由SGSN和GGSN配合完成，具体参见[表1]。
网元|功能
---|---
SGSN|SGSN异常信令管控，具体包括附着请求异常信令管控、业务请求异常信令管控和PDP激活请求异常信令管控。SGSN在各信令的每个统计周期内统计各信令数，如果统计的信令数大于最大信令数，则SGSN将用户加入信令黑名单，并启动黑名单定时器。在信令黑名单定时器管理时间内，SGSN拒绝或丢弃信令；或SGSN建立FAKEAPN PDP，用户使用此PDP连接无法上网。信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。
GGSN|GGSN支持FAKE APN PDP激活，用户使用此PDP无法上网。
本网元实现 : 
附着请求异常信令管控SGSN在附着信令单位统计周期内统计附着信令数，如果统计的附着信令数大于最大信令数，则SGSN将用户加入附着信令黑名单，并启动附着黑名单定时器。在附着信令黑名单定时器管理时间内，UE不断发起附着，SGSN进行如下处理：拒绝接入请求。强制去附着。丢弃后续请求。附着信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
业务请求异常信令管控SGSN在业务请求信令单位统计周期内统计业务请求信令数，如果统计的业务请求信令数大于最大信令数，则SGSN将用户加入业务请求信令黑名单，并启动业务请求黑名单定时器。在业务请求信令黑名单定时器管理时间内，UE不断发起业务请求，SGSN进行如下处理：拒绝业务请求。强制去附着。丢弃后续请求。业务请求信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
PDP激活请求异常信令管控SGSN在PDP激活请求信令单位统计周期内统计附着信令数，如果统计的PDP激活请求信令数大于最大信令数，则SGSN将用户加入PDP激活请求信令黑名单，并启动PDP激活请求信令黑名单定时器。在PDP激活请求信令黑名单定时器管理时间内，UE不断发起PDP激活请求，SGSN进行如下处理：拒绝接入请求。建立Fake APN PDP。强制去附着。丢弃后续请求。PDP激活请求信令黑名单定时器超时后，用户从信令黑名单移除，可以正常上网。 
业务流程 : 
附着请求异常信令管控
附着请求异常信令管控流程如[图2]所示。
图2  附着请求异常信令管控流程
SGSN以UE为颗粒度，记录单位时间T1内产生的附着请求信令数，当单位时间信令数目没超过阈值N1时，SGSN按照正常流程处理用户信令，对单位时间信令数超过阈值N1的UE进行的异常信令进行控制，控制方法如下： 
SGSN将该用户加入黑名单，下发附着拒绝，拒绝原因可配置，并启动黑名单定时器TT1。 
TT1超时前如果继续收到附着请求，则进入步骤2。 
如果直到TT1超时仍未收到附着请求，则将用户从黑名单移除，正常处理后续消息。 
网络发起去附着（re-attach not required）。 
TT1超时前如果继续收到附着请求，则进入步骤3。 
如果直到TT1超时仍未收到附着请求，则将用户从黑名单移除，正常处理后续消息。 
SGSN丢弃该用户的信令，对这部分丢弃的信令单独统计。如果黑名单TT1超时时将用户从黑名单移除。 
业务请求异常信令管控
业务请求异常信令管控流程如[图3]所示。
图3  业务请求异常信令管控流程
SGSN以UE为颗粒度，记录单位时间T2内产生的业务请求信令数，当单位时间信令数目没超过阈值N2时，SGSN按照正常流程处理用户信令，对单位时间信令数超过阈值N2的UE进行的异常信令进行控制，控制方法如下： 
SGSN将该用户加入黑名单，业务请求拒绝，拒绝原因值可配置，并启动黑名单定时器TT2。 
TT2超时前如果继续收到业务请求，则进入步骤2。 
如果直到TT2超时仍未收到业务请求，则将用户从黑名单移除，正常处理后续消息。 
网络发起去附着（re-attach not required）。 
TT2超时前如果收到附着请求，则进入步骤3。 
如果直到TT2超时仍未收到附着请求，则将用户从黑名单移除，正常处理后续消息。 
SGSN丢弃该用户的信令，对这部分丢弃的信令单独统计。黑名单TT2超时时将用户从黑名单移除。 
PDP激活请求异常信令管控
PDP激活请求异常信令管控流程如[图4]所示。
图4  PDP激活请求异常信令管控流程
SGSN以UE为颗粒度，记录单位时间T3内产生的PDP激活请求信令数，当单位时间信令数目没超过阈值N3时，SGSN按照正常流程处理用户信令，对单位时间信令数超过阈值N3的UE进行的异常信令进行控制，控制方法如下： 
SGSN将该用户加入黑名单，并下发PDP激活拒绝，拒绝原因值可配置，并启动黑名单定时器TT3。 
TT3超时前如果继续收到PDP激活请求，则进入步骤2。 
如果直到TT3超时仍未收到PDP激活请求，则将用户从黑名单移除，正常处理后续消息。 
终端继续发起PDP激活请求信令时，SGSN以本地配置的Fake APN（能建立但是无法上网）让终端建立成功。 
如果直到TT3超时仍未收到PDP激活请求，则将用户从黑名单移除，终端再发起PDP激活请求时使用正常APN。 
如果本地未配置Fake APN或Fake APN PDP激活失败，则进入步骤3。 
TT3超时前如果继续收到PDP激活请求，则进入步骤3。 
网络发起去附着（re-attach not required）。 
TT3超时前如果收到附着请求，则进入步骤4。 
如果直到TT3超时仍未收到附着请求，则将用户从黑名单移除，正常处理后续消息。 
SGSN丢弃该用户的信令，对这部分丢弃的信令单独统计。黑名单TT3超时时将用户从黑名单移除。 
系统影响 : 
SGSN支持异常信令管控，减少了网络侧要处理的信令，异常信令管控的功效是提高系统处理性能。 
应用限制 : 
该特性不涉及应用限制。 
特性交互 : 
特性|交互
---|---
紧急呼叫|如果附着请求、业务请求或PDP激活请求信令进入黑名单，SGSN对紧急呼叫放行，允许信令黑名单用户拨打紧急呼叫。
遵循标准 : 
该特性不涉及标准协议。 
特性能力 : 
类型|能力
---|---
黑名单用户容量|数量等同于MM上下文配置容量。
可获得性 : 
版本要求及变更记录 : 
特性版本|发布版本|发布说明
---|---|---
V1.0|V7.19.13|首次发布。
License要求 : 
该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“SGSN支持信令风暴抑制”（license ID：7096），此项目显示为“支持”，表示SGSN支持异常信令管控功能。
对其他网元的要求 : 
GGSN需支持FAKE APN PDP激活，控制用户使用此PDP连接无法上网。 
工程规划要求 : 
Fake APN需要全网规划。 
O&M相关 : 
命令 : 
配置项表2  新增配置项配置项命令SGSN信令风暴抑制配置SET SGSN SIGSRESTRAIN FLAGSHOW SGSN SIGSRESTRAIN FLAGSET SGSN SIGSRESTRAINDEL SGSN SIGSRESTRAIN FAKE APNSHOW SGSN SIGSRESTRAIN 
动态管理在“动态管理”下增加“SGSN信令风暴抑制管理”，具体参见下表。功能命令查询单用户信令状态SHOW SGSN SUBSCRIBER SIGSTATUS用户移出信令黑名单MOVE SGSN SUBSCRIBER BLACK查询信令黑名单用户SHOW SGSN BLACK SUBSCRIBER 
性能统计 : 
测量类型|描述
---|---
SGSN信令风暴抑制流程测量|编号为C40595开头的所有计数器。
SGSN信令风暴抑制用户数测量|编号为C40596开头的所有计数器。
告警和通知 : 
该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 : 
该特性涉及的业务观察/失败观察，参见下表。 
失败原因码及名称|相关模块|波及业务|产生原因
---|---|---|---
161 信令风暴拒绝|EMM|附着/业务请求|附着信令风暴抑制，业务请求信令风暴抑制。
话单与计费 : 
该特性不涉及话单与计费的变化。 
特性配置 : 
特性配置 : 
配置说明 : 
通过配置信令风暴抑制功能，能够确保网络设备安全运行，减轻网络信令压力，化解信令风暴，避免网络拥塞。 
配置前提 : 
对于信令风暴抑制功能，根据经验，提供了各项门限的经验数据。但是各地网络均有其话务模型的独特性，需要预先评估各项黑名单门限预设值是否需要修改。 
要预先规划FAKE APN。 
配置过程 : 
执行命令[SET SGSN SIGSRESTRAIN FLAG]，打开“SGSN支持信令风暴抑制”功能开关。
执行命令[SET SGSN SIGSRESTRAIN]，根据全网规划配置Fake APN名称。
执行命令[ADD GPRS APN]，配置本地APN解析。Fake APN建议通过本地配置进行解析，而不是通过DNS进行解析。
（可选）执行命令[SET SGSN SIGSRESTRAIN]，根据各地实际话务模型，调整SGSN支持信令风暴抑制功能的各项门限值。
 说明： 
SGSN支持信令风暴抑制功能的门限默认值能够适应大多数地区的话务模型，如果运营范围内话务模型特殊，可以根据当地情况，酌情调整。 
配置实例 : 
###### 异常附着信令，引起信令风暴 
场景说明
在此场景下，如果大量异常终端反复发起附着请求，引起网络信令风暴，影响正常终端的附着，则需要进行对附着请求信令进行抑制，避免网络拥塞，化解信令风暴。 
数据规划
配置项|参数名称|取值
---|---|---
设置SGSN是否支持信令风暴抑制配置|SGSN支持信令风暴抑制|支持
设置SGSN信令风暴抑制配置|附着请求信令统计周期(秒)|720
附着请求最大信令数|设置SGSN信令风暴抑制配置|15
附着拒绝原因值|设置SGSN信令风暴抑制配置|7
附着请求黑名单定时器时长(秒)|设置SGSN信令风暴抑制配置|1200
配置步骤
步骤|说明|命令
---|---|---
1|启用SGSN支持信令风暴抑制。|SET SGSN SIGSRESTRAIN FLAG:FLAG="ON"
2|设置附着信令抑制策略。|SET SGSN SIGSRESTRAIN:ATTSTATISPERD=720,ATTMAXSIGNUM=15,ATTREJCAUSE=7,ATTBLACKLISTDUR=1200
###### 异常业务请求信令，引起信令风暴 
场景说明
在此场景下，如果大量异常终端反复发起业务请求，引起网络信令风暴，则需要进行对业务请求信令进行抑制，避免网络拥塞，化解信令风暴。 
数据规划
配置项|参数名称|取值
---|---|---
设置SGSN是否支持信令风暴抑制配置|SGSN支持信令风暴抑制|支持
设置SGSN信令风暴抑制配置|业务请求信令统计周期(秒)|720
业务请求最大信令数|设置SGSN信令风暴抑制配置|30
业务请求拒绝原因值|设置SGSN信令风暴抑制配置|7
业务请求黑名单定时器时长(秒)|设置SGSN信令风暴抑制配置|1200
配置步骤
步骤|说明|命令
---|---|---
1|启用SGSN支持信令风暴抑制。|SET SGSN SIGSRESTRAIN FLAG:FLAG="ON"
2|设置业务请求信令抑制策略。|SET SGSN SIGSRESTRAIN:SERVSTATISPERD=720,SERVMAXSIGNUM=30,SERVREJCAUSE=7,SERVBLACKLISTDUR=1200
###### 异常PDP请求信令，引起信令风暴 
场景说明
在此场景下，如果大量异常终端反复发起PDP请求，引起网络信令风暴，则需要进行对pdp激活信令进行抑制，避免网络拥塞，化解信令风暴。 
数据规划
配置项|参数名称|取值
---|---|---
设置SGSN是否支持信令风暴抑制配置|SGSN支持信令风暴抑制|支持
设置SGSN信令风暴抑制配置|PDP激活请求信令统计周期(秒)|720
PDP激活请求最大信令数|设置SGSN信令风暴抑制配置|10
PDP激活拒绝原因值|设置SGSN信令风暴抑制配置|31
PDP激活请求黑名单定时器时长(秒)|设置SGSN信令风暴抑制配置|1200
FAKE APN名称|设置SGSN信令风暴抑制配置|fake.apn.com
新增GPRS APN HOST配置|APN名称|fake.apn.com.mnc011.mcc460.gprs
IP地址|新增GPRS APN HOST配置|192.20.87.36
计费模板标识|新增GPRS APN HOST配置|5
支持DT功能|新增GPRS APN HOST配置|NO
支持终端双栈功能|新增GPRS APN HOST配置|NO
过滤S-CDR|新增GPRS APN HOST配置|NO
配置步骤
步骤|说明|命令
---|---|---
1|启用SGSN支持信令风暴抑制。|SET SGSN SIGSRESTRAIN FLAG:FLAG="ON"
2|设置业务请求信令抑制策略。|SET SGSN SIGSRESTRAIN:PDPSTATISPERD=720,PDPMAXSIGNUM=10,PDPREJCAUSE=31,PDPBLACKLISTDUR=1200,FAKEAPN="fake.apn.com"
3|设置fake apn的本地解析配置。|ADD GPRS APN:APN="fake.apn.com.mnc011.mcc460.gprs",IPADDR="192.20.87.36",CTPLID=5,DTSPRT="NO",DUALSTACKFLAG="NO",SCDRFLT="NO"
调整特性 : 
本特性不涉及调整特性。 
测试用例 : 
测试项目|附着请求信令风暴抑制
---|---
测试目的|测试附着请求信令风暴抑制功能。
预置条件|SGSN网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得SGSN网元信令风暴抑制功能的license授权，并更新了license。
测试过程|开启SGSN信令风暴抑制功能开关，根据全网规划，配置Fake APN。修改“附着请求最大信令数”参数为2，“附着请求黑名单定时器时长”参数为1200。打开信令跟踪。用户连续发起15次attach（15次附着请求在一个信令统计周期内）。等待20分钟后，查询用户黑名单状态。
通过准则|前两次attach成功。第三次attach失败，拒绝原因是“GPRS  service  not allowed”，使用动态管理命令查询，用户被加入信令黑名单。第四次attach时，网络侧发起detach(re-attach not required)流程。detach成功。第五次attach及后续attach时，用户消息被直接丢弃，不会触发后续流程。20分钟后，查询用户信令黑名单状态，用户已经从黑名单中移除。
测试结果|–
测试项目|业务请求信令风暴抑制
---|---
测试目的|测试业务请求信令风暴抑制功能。
预置条件|SGSN网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得SGSN网元信令风暴抑制功能的license授权，并更新了license。用户已经attach成功。
测试过程|开启信令风暴抑制功能开关，根据全网规划，配置Fake APN。修改“业务请求最大信令数”参数为2，“业务请求黑名单定时器时长”参数为1200。打开信令跟踪。用户连续发起4次业务请求（4次业务请求在一个信令统计周期内）。用户发起attach。等待20分钟后，查询用户黑名单状态。
通过准则|前两次业务请求成功。第三次业务请求失败，拒绝原因是“GPRS  service  not allowed”，使用动态管理命令查询，用户被加入信令黑名单。第四次业务请求时，网络侧发起detach(re-attach not required)流程。detach成功。用户attach时，用户消息被直接丢弃，不会触发后续流程。20分钟后，查询用户信令黑名单状态，用户已经从黑名单中移除。
测试结果|–
测试项目|PDP激活请求信令风暴抑制
---|---
测试目的|测试PDP激活请求信令风暴抑制功能。
预置条件|SGSN网元各项对接和业务配置完毕，用户可以正常进行各项业务。用户取得SGSN网元信令风暴抑制功能的license授权，并更新了license。用户已经attach成功。
测试过程|开启信令风暴抑制功能开关，根据全网规划，配置Fake APN。修改“PDP激活请求最大信令数”参数为2，“PDP激活请求黑名单定时器时长”参数为1200打开信令跟踪。用户连续发起5次PDP激活请求（5次PDP激活请求在一个信令统计周期内）。用户发起attach。等待20分钟后，查询用户黑名单状态。
通过准则|前两次PDP激活请求成功。第三次PDP激活请求失败，拒绝原因是“Activation rejected, unspecified”，使用动态管理命令查询，用户被加入信令黑名单。第四次PDP激活请求时，网络侧以fake apn让用户激活成功。第五次PDP激活请求时，网络侧发起detach(re-attach not required)流程。detach成功。用户attach时，用户消息被直接丢弃，不会触发后续流程。20分钟后，查询用户信令黑名单状态，用户已经从黑名单中移除。
测试结果|–
常见问题处理 : 
无 
# 缩略语 
# 缩略语 
EIR : 
Equipment Identity Register设备标识寄存器
eNodeB : 
Evolved NodeB演进的NodeB
GGSN : 
Gateway GPRS Support NodeGPRS网关支持节点
## GSM 
Global System for Mobile Communications全球移动通信系统
HLR : 
Home Location Register归属位置寄存器
## IWMSC 
Interworking Mobile Switching Center网间移动交换中心
PCEF : 
Policy and Charging Enforcement Function计费和策略控制实施功能
PCRF : 
Policy and Charging Rules Function策略和计费规则功能
PGW : 
PDN Gateway分组数据网网关
RAN : 
Radio Access Network无线接入网
RAT : 
Radio Access Technology无线接入技术
RNC : 
Radio Network Controller无线网络控制器
SGSN : 
Serving GPRS Support Node服务GPRS支持节点
SGW : 
Serving Gateway服务网关
## UMTS 
Universal Mobile Telecommunication System通用移动通讯系统
