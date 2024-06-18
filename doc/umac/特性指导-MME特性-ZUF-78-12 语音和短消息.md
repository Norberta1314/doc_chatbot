# 概述 
## 功能描述 
### LTE语音 
LTE语音解决方案主要包括两个。 
CSFB（Circuit Switched Fall Back）：LTE网络只提供数据业务，当UE发起或者接收语音呼叫时，回落到CS域进行处理。运营商无需部署IMS，只需要升级MSC就可以支持。这是一种快速提供业务的方案，但缺点是呼叫接续速度慢。CSFB适合作为IMS部署之前的过渡方案，另外还可以用来解决LTE手机漫游场景的语音呼叫问题，即在拜访地网络没有部署IMS，或者IMS漫游协议尚未应用的情况下，CSFB可以为漫入的LTE用户提供语音业务。UE从E-UTRAN回落到UTRAN/GERAN的CSFB网络架构如下图所示。UE从E-UTRAN回落到CDMA 1xRTT的CSFB网络架构如下图所示。LTE部署的初期，LTE只处理数据业务，语音业务回落到CS域处理。CSFB作为部署IMS前的过渡方案，可以快速实现网络部署并提供语音业务，但是接续速度慢。CSFB快速回落方案，可以在2s内回落。 
VoLTE（Voice over Long Term Evolution）+SRVCC（Single Radio Voice Call Continuity）：通过LTE网络中的IMS域提供高清晰的语音服务。IMS由于支持多种接入和丰富的多媒体业务，成为全IP时代的核心网标准架构。经历了多年的发展成熟后，如今IMS已经跨越裂谷，成为固定话音领域、PSTN网络改造的主流选择，而且也被3GPP、GSMA确定为移动语音的标准架构。在LTE网络部署不完全时，通过SRVCC解决语音控制和UE移动到CS网络切换时的语音连续性问题。SRVCC的实现过程实质上就是一个切换过程，在LTE网络中终端是通过IMS来实现语音功能的，当终端离开LTE网络后，则通过MSC server切换到2G/3G 网络中从而实现在2G/3G网络中的语音功能。UE通过LTE网络接入IMS。UE从E-UTRAN切换到UTRAN/GERAN的SRVCC网络架构如下图所示。UE从E-UTRAN切换到CDMA 1xRTT的SRVCC网络架构如下图所示。在LTE覆盖区内提供基于IP的高清晰语音和视频业务，在LTE覆盖区外仍通过CS域提供语音业务。SRVCC实现LTE网络中的IMS域语音到2G/3G网络中的CS域语音的无缝切换。为了减少SRVCC切换时长，使用户获得更好的通话体验，协议还定义了eSRVCC。eSRVCC相比于SRVCC，媒体切换点改为更靠近本端的设备。具体方案就是增加ATCF/ATGW功能实体作为媒体锚定点，无论是切换前还是切换后的会话消息都要经过ATCF/ATGW转发。后续在发生eSRVCC切换时，只需要创建UE与ATGW之间的承载通道，对端设备与ATGW之间的媒体流还是通过原承载通道传输。这样其创建新承载通道的消息交互路径明显短于SRVCC方案，减少了切换时长。 
### LTE短消息 
LTE短消息解决方案主要包括三个。 
SMS over SGs：基于SGs接口的短消息业务，即短消息业务由CS域直连短消息中心，MME完成SGs和NAS接口的短消息传递。 
SMS over SGd：基于SGd接口的短消息业务，即MME与SMSC直连，MME透传UE和SMSC间短消息。 
SMS over IP：由IMS提供短消息服务，EPS提供IP承载。 
## 功能特性简介 
针对语音和短信的应用特点和应用场景，核心网为满足用户的可靠语音和短信的要求，提供了有效的解决方案。详细的解决方案特性如下表： 
方案特性|实现简述|特导链接
---|---|---
VOLTE能力管理|MME在附着/TAU业务中，通知HSS和UE，UE是否能够使用IMS VoPS。IMS VoPS是否支持由MME基于以下几个元素得到：UE上报的Voice domain preference and UE's usage setting取值UE所在的TAIUE的IMSIUE的IMSI和所在的TAIUE是否签约VoLTEUE是否签约STN-SRUE的SRVCC能力UE的IMEI和SRVCC能力具体描述参见3GPP 23.401协议的“4.3.5.8 IMS voice over PS Session Supported Indication”、“4.3.5.8A Homogenous Support of IMS Voice over PS Sessions Indication”和“4.3.5.9 Voice domain preference and UE's usage setting”章节。|ZUF-78-12-001 VOLTE能力管理
T-ADS|用户可同时注册在CS和LTE域，当语音呼叫此用户时，HSS向MME发送IDR消息，请求用户上下文信息（是否支持VOLTE，最近活动时间，所在的RAT类型），MME通过IDA响应返回以上信息，以便网络判断走CS语音还是LTE语音。|ZUF-78-12-002 T-ADS
LTE IMS紧急会话支持|在EPC网络中，运营商通过IMS网络为用户提供语音业务。EPC网络与IMS网络建立紧急会话，可以给用户提供紧急呼叫业务。为了给紧急呼叫提供端到端的保障，EPC网络需要为IMS紧急会话提供紧急承载，且保证紧急承载的优先级和QoS。按用户合法性分类，MME支持的紧急呼叫如下：仅完全合法有效用户可以紧急呼叫仅鉴权合法用户（可能位置被限制）可以紧急呼叫具有IMSI的用户（可能鉴权失败、位置被限制）可以紧急呼叫任意用户（可能不具有IMSI、鉴权失败、位置被限制）可以紧急呼叫。MME支持紧急会话的SRVCC切换和紧急CSFB回落。IMS紧急会话的具体描述参见3GPP 23.401协议的“4.3.12 IMS Emergency Session Support”章节。|ZUF-78-12-003 LTE IMS紧急会话支持
CSFB|CSFB（CS Fallback）指CS语音回落。在LTE和2G/3G网络共同覆盖的区域，对于不支持IMS业务的终端，可以回落到2G/3G网络使用CS域进行语音业务，同时保持数据业务连续性的功能。MME需要与MSC/VLR之间使用SGs口连接，完成用户在CS域的位置更新、注册、寻呼和短消息业务。MME支持紧急呼叫的CS语音回落。MME支持基于TA和IMSI号段来配置是否支持CSFB功能，也可以基于TA来配置是否支持CSFB功能。CSFB的具体业务流程参见3GPP 23.272协议。|ZUF-78-12-004 CSFB
SRVCC|SRVCC（Single Radio Voice Call Continuity）是3GPP提出的一种VoLTE语音业务连续性方案，主要是为了解决当单射频UE在LTE网络和2G/3G CS网络之间移动时，如何保证语音呼叫连续性的问题，即保证单射频UE在IMS控制的VoIP语音和CS域语音之间的平滑切换。MME支持紧急呼叫的语音连续性。MME支持从HSS获得CS呼叫中使用的A-MSISDN（Additional-MSISDN，附加MSISDN）。在SRVCC切换中，MME将A-MSISDN作为C-MSISDN号码在信令中携带给MSC，MSC通过C-MSISDN找到语音会话并将会话从IMS迁移到CS域中。SRVCC的具体业务流程参见3GPP 23.216协议，3GPP 23.003协议的“18.7 Correlation MSISDN”和“18.9 Additional MSISDN”章节，3GPP 29.272的“7.3.157 A-MSISDN”章节。|ZUF-78-12-005 SRVCC
eSRVCC|eSRVCC是基于SIP的SRVCC的增强改进方案。相对于SRVCC切换，eSRVCC切换在IMS网络新增ATCF/ATGW逻辑网元。ATCF在SRVCC语音切换时锚定媒体流，因而媒体的切换不需要通过对端的IMS UE的参与，避免因为IMS信令路径过长引起SRVCC切换时的语音中断和时延。|ZUF-78-12-005 SRVCCZUF-78-12-006 eSRVCC
e1xCSFB|e1xCSFB指1xCS语音回落，用于在LTE和CDMA2000网络共同覆盖的区域对于不支持IMS业务的终端回落到CDMA2000网络使用1xCS进行语音业务，同时保持数据业务连续性的功能。为完成e1xCSFB业务，MME通过IWS与MSCe/VLR之间互通，完成用户在1xCS域注册、去注册、语音和短消息业务。e1xCSFB具体业务流程参见3GPP 23.272协议。|ZUF-78-12-007 e1xCSFB
VoLTE保障信令流程|VoLTE保障信令流程指在网络侧流程和UE、无线侧流程冲突时，保障业务正确的处理流程。VoLTE专有承载是通过网络侧建立或修改流程来完成的，使得网络侧流程和UE、无线侧流程并发冲突的概率增加。当MME发现网络侧发起的专有承载操作和UE、无线侧发起的业务流程冲突时：如果SGW不改变，则MME缓存专有承载操作，等UE或无线侧的业务流程完成后，继续执行专有承载操作。如果SGW发生改变，则MME直接给SGW返回失败，携带特殊原因。PGW延时后重新触发专有承载操作。|ZUF-78-12-008 VoLTE保障信令流程
VoLTE容灾之MME故障控制|MME故障时，为了触发用户业务恢复，使得用户可以尽快作语音被叫，MME支持以下功能：Pool内全部MME之间支持在线用户IMSI和TA list信息备份。收到SGW发送的DDN消息后，备用MME以IMSI方式寻呼用户，触发用户重新附着。具体描述参见3GPP 23.007协议的“14.1 Restart of the MME”章节。|ZUF-78-12-009 VoLTE容灾之MME故障控制
VoLTE容灾之SGW故障控制|MME支持SGW故障时触发用户业务恢复，使得用户可以尽快作语音被叫。MME发现SGW故障的方式有：支持通过Echo消息或者Recovery信元检测SGW故障。支持根据PGW的指示检测SGW故障。MME在发现SGW故障后，触发用户业务恢复的方式有：针对故障设备上的用户，采用SGW Relocation或指示用户重新附着的方式进行业务恢复。用户主动触发Service Request或TAU时，采用SGW Relocation或指示用户重新附着的方式进行业务恢复。用户恢复速率可控制。具体描述参见3GPP 23.007协议的“14.1A.1 SGW Failure”章节。|ZUF-78-12-010 VoLTE容灾之SGW故障控制
VoLTE容灾之PGW故障控制|MME支持PGW故障时触发用户业务恢复，使得用户可以尽快作语音被叫。MME通过SGW发送的PGW Restart Notification消息感知PGW故障。检测到PGW故障后，针对故障设备上的用户，MME支持如下方式恢复业务：若所有PDN连接对应的PGW均故障，则MME通过发送分离请求、IMSI寻呼、业务请求或TAU拒绝消息指示用户重新附着。若仅IMS PDN连接对应的PGW故障，则MME指示用户重建IMS PDN连接。用户恢复速率可控制。具体描述参见3GPP 23.007协议的“14.3 Partial Failure Handling at MME”章节。|ZUF-78-12-011 VoLTE容灾之PGW故障控制
VoLTE容灾之P-CSCF故障|MME支持P-CSCF故障时，触发用户业务恢复，使得用户可以尽快作语音被叫。MME根据HSS的P-CSCF恢复指示，触发UE的IMS PDN重建。在PDN重建过程中，由PGW为UE分配新的P-CSCF地址。具体描述参见3GPP TS 23.380协议的“5.1.2 Network recovery information flow - Update PDP context / Bearer”章节。|ZUF-78-12-012 VoLTE容灾之P-CSCF故障控制
VoLTE故障定位手段增强|为增强对VoLTE、SRVCC等语音业务服务质量的监控，提供了如下手段：提供以QCI为对象的承载激活、修改、去激活、TAU、业务请求、切换、S1释放、Erab释放等流程测量。提供以APN为对象的承载激活、修改、去激活流程测量。提供以QCI为对象的承载激活、修改、切换、TAU、业务请求等分网元测量。提供以QCI为对象的承载数量、承载建立和删除数量的测量。提供以QCI、TA、APN、域等组合对象的承载激活、修改、去激活流程测量和承载激活、修改分网元测量。针对VoLTE和SRVCC过程中各种失败分开统计。|ZUF-78-12-013 VoLTE故障定位手段增强
内嵌IWS功能|MME支持内嵌IWS功能，实现MME和3GPP2 MSC的互通。通过IWS功能，LTE网络下的UE可以和3GPP2 MSC进行交互，完成各种业务，主要包括：位置更新业务语音起呼、终呼短消息起呼、终呼SRVCC切换|ZUF-78-12-014 内嵌IWS功能
CSFB语音容灾之MME故障控制|当MSC/VLR发现用户注册所在的MME故障（SGs口链路故障）时，选择MME Pool中的其他MME发送CSFB的终呼，携带LAC和CS restoration indicator标识。MME收到MSC的寻呼消息，MME在LAC范围内可对用户进行寻呼，触发UE重新联合附着，完成MSC注册，CSFB业务恢复。具体描述参见3GPP 23.007协议的“26 Mobile terminated CS service delivery via an alternative MME in MME pool”章节。|ZUF-78-12-015 CSFB语音容灾之MME故障控制
CSFB语音容灾之MSC/VLR故障控制|MME支持MSC/VLR故障时的三种恢复方式，包括：被动恢复：故障时UE的CS语音被叫业务时，备份MSC/VLR向MME下发无LAI寻呼。MME触发UE的IMSI重新附着，完成MSC注册，CSFB业务恢复。主动恢复：MME能够自动监控SGs接口异常。一旦发现SGs接口异常，能够触发异常SGs接口上注册的UE重新注册到正常SGs接口的MSC/VLR上，恢复CSFB被叫业务。人工恢复：当发现某个MSC故障，或者需要升级维护时，需要对该MSC上注册的UE进行卸载/迁移。MME能够提供网管动态管理命令，触发注册在该MSC的UE重新发起IMSI附着。具体描述参见3GPP 23.007协议的“4.2.10 MME associations”章节。|ZUF-78-12-016 CSFB语音容灾之MSC/VLR故障控制
SMS over SGs|MME支持基于SGs口的短消息业务，即短消息业务由CS域直连短消息中心，MME完成LTE网络和CS网络间的短消息传递。MME可以基于IMSI或APN控制SGs口短消息。具体描述参见3GPP 23.272协议的“8.2 Short Message Service (SMS)”章节。|ZUF-78-12-017 SMS over SGs
SMS over SGd|MME支持基于SGd口的短消息业务，即短消息业务由MME通过SGd口直连短消息中心，UE和MME之间仍然通过EPS NAS信令投递短消息。具体描述参见3GPP 23.272 Annex C。|ZUF-78-12-018 SMS over SGd
SMS over IP|MME支持SMS over IP，即由IMS提供短消息服务，EPS提供IP承载。具体描述参见3GPP 23.204协议。|ZUF-78-12-019 SMS over IP
# ZUF-78-12-001 VOLTE能力管理 
## 特性描述 
## 特性描述 
### 术语 
术语|含义
---|---
支持IMS的同向性指示|该信元表示是否服务节点（MME或SGSN，或MME/SGSN组合）中的所有跟踪区或路由区都支持“IMS语音能力”。如果其值为“支持”，表示所有跟踪区或路由区都支持“IMS语音能力”；如果其值为“不支持”，则表示任何跟踪区或路由区都不支持“IMS语音能力”。
### 描述 
##### 定义 
VoLTE是基于IMS网络的LTE语音解决方案，即在LTE覆盖区域内提供基于IP的高清晰语音业务。VoLTE是一种IP数据传输技术，无需2G/3G网，全部业务承载于4G网络上，可实现数据与语音业务在同一网络下的统一。换言之，4G网络下不仅仅提供高速率的数据业务，同时还提供高质量的音视频通话，音视频通话需要VoLTE技术来实现。部署VoLTE意味着运营商开启了移动宽带语音演进之路。
##### 背景知识 
LTE语音解决方案演进
LTE语音解决方案演进过程如下图所示。 
[]images/ZUF-78-12-001%20-%E8%83%8C%E6%99%AF%E7%9F%A5%E8%AF%861.jpg)SvLTE（Simultaneous Voice and LTE），即双待手机方式。手机同时工作在LTE网络和CS网络，LTE网络提供数据业务，CS网络提供语音业务。该方案是纯粹基于手机的方案，对网络无特别要求，不需要部署IMS，缺点是手机成本高、耗电高。目前已经有CDMA1x和LTE的双待手机，因此该方案被一些CDMA运营商采用作为IMS部署前的过渡方案。 
CSFB（Circuit Switched Fall Back），LTE网络只提供数据业务，当UE发起或者接收语音呼叫时，回落到CS域进行处理。运营商无需部署IMS，只需要升级MSC就可以支持。这是一种快速提供业务的方案，但缺点是呼叫接续速度慢。CSFB适合作为IMS部署之前的过渡方案，另外还可以用来解决LTE手机漫游场景的语音呼叫问题，即在拜访地网络没有部署IMS，或者IMS漫游协议尚未应用的情况下，CSFB可以为漫入的LTE用户提供语音业务。 
SRVCC（Single Radio Voice Call Continuity），解决语音控制和UE移动到CS网络切换时的语音连续性问题。该方案为基于IMS的VoIP呼叫解决方案，利用IMS核心网络提供LTE
VoIP语音业务的路由、控制和业务触发，并提供LTE向2G/3G切换时的语音连续性保证。SRVCC的实现过程实质上就是一个切换过程，在LTE网络中终端是通过IMS来实现语音功能的，当终端离开LTE网络后，则通过MSC
server切换到2G/3G 网络中从而实现在2G/3G网络中的语音功能。 
VoLTE（Voice over Long Term Evolution），通过LTE网络中的IMS域提供高清晰的语音服务。IMS由于支持多种接入和丰富的多媒体业务，成为全IP时代的核心网标准架构。经历了多年的发展成熟后，如今IMS已经跨越裂谷，成为固定话音领域、PSTN网络改造的主流选择，而且也被3GPP、GSMA确定为移动语音的标准架构。 
LTE语音解决方案（CSFB）
UE从E-UTRAN回落到UTRAN/GERAN的CSFB网络架构如下图所示。 
[]images/ZUF-78-12-001%20-%E8%83%8C%E6%99%AF%E7%9F%A5%E8%AF%862.png)UE从E-UTRAN回落到CDMA 1xRTT的CSFB网络架构如下图所示。 
[]images/ZUF-78-12-001%20-%E8%83%8C%E6%99%AF%E7%9F%A5%E8%AF%863.png)LTE部署的初期，LTE只处理数据业务，语音业务回落到CS域处理。CSFB作为部署IMS前的过渡方案，可以快速实现网络部署并提供语音业务，但是接续速度慢。CSFB快速回落方案，可以在2
s内回落。 
LTE语音解决方案（SRVCC）
UE从E-UTRAN切换到UTRAN/GERAN的SRVCC网络架构如下图所示。 
[]images/ZUF-78-12-001%20-%E8%83%8C%E6%99%AF%E7%9F%A5%E8%AF%864.png)UE从E-UTRAN切换到CDMA 1xRTT的SRVCC网络架构如下图所示。 
[]images/ZUF-78-12-001%20-%E8%83%8C%E6%99%AF%E7%9F%A5%E8%AF%865.png)在LTE覆盖区内提供基于IP的高清晰语音和视频业务，在LTE覆盖区外仍通过CS域提供语音业务。 
SRVCC实现LTE网络中的IMS域语音到2G/3G网络中的CS域语音的无缝切换。 
LTE语音解决方案（eSRVCC）
eSRVCC方案相对于SRVCC方案的增强在于减少了切换时长（切换时长小于300
ms），使用户获得更好的通话体验。 
SRVCC和eSRVCC对比如下图所示。 
[]images/ZUF-78-12-001%20-%E8%83%8C%E6%99%AF%E7%9F%A5%E8%AF%866.png)SRVCC：媒体的切换点是对端网络设备（如对端UE），影响切换时长的主要因素是会话切换后需要在IMS网络中创建新的承载。 
eSRVCC：相比于SRVCC，媒体切换点改为更靠近本端的设备。具体方案就是增加ATCF/ATGW功能实体作为媒体锚定点，无论是切换前还是切换后的会话消息都要经过ATCF/ATGW转发。后续在发生eSRVCC切换时，只需要创建UE与ATGW之间的承载通道，对端设备与ATGW之间的媒体流还是通过原承载通道传输。这样其创建新承载通道的消息交互路径明显短于SRVCC方案，减少了切换时长。 
LTE语音解决方案（CSFB与SRVCC对比）
解决方案|优点|缺点
---|---|---
CSFB|不引入IMS，重用现有的CS网络。终端产业链较成熟。3GPP标准化。|现网需要改造。呼叫接续时间增加。语音通话期间，不能体验LTE高速数据业务。
SRVCC|丰富的多媒体业务体验。高清语音和视频编解码明显提升用户感受。VoLTE引入高清编解码技术，改变了多年不变的语音编码，新的语音编码至少能够达到7000Hz以上，可以给用户提供更加高水平的语音质量。接续时间百毫秒级。提升频谱利用率，降低网络成本。3GPP标准化。|需要建设IMS。终端产业链待成熟。
### 应用场景 
##### VoLTE业务 
VoLTE用于EPS网络覆盖区域下的用户接入IMS域进行语音或视频通话，其中语音业务承载于EPS网络上。按照业务使用场景分类，包括如下几类。 
4G用户间的语音通话 
4G用户间的视频通话 
4G用户与2G/3G网络用户间的语音通话 
4G用户间的语音通话
该场景的实现过程如[图1](ZUF-78-12-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842495__G%E7%94%A8%E6%88%B7%E9%97%B4%E7%9A%84%E8%AF%AD%E9%9F%B3%E9%80%9A%E8%AF%9D-D8978A54)所示。
图1  4G用户间的语音通话
[]images/ZUF-78-12-001%20-%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF1.png)
主被叫LTE用户已注册到IMS网络，LTE用户通过LTE网络发起呼叫，被叫域选为LTE网络，被叫应答，主被叫进入语音通话。 
4G用户间的视频通话
该场景的实现过程如[图1](ZUF-78-12-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842495__G%E7%94%A8%E6%88%B7%E9%97%B4%E7%9A%84%E8%AF%AD%E9%9F%B3%E9%80%9A%E8%AF%9D-D8978A54)所示。
主被叫LTE用户已注册到IMS网络，LTE用户通过LTE网络发起呼叫，被叫域选为LTE网络，被叫应答，主被叫进入视频通话。 
4G用户与2G/3G网络用户间的语音通话
4G用户与2G/3G网络用户间的语音通话包括两种：LTE用户呼叫CS用户和CS用户呼叫LTE用户。 
LTE用户呼叫CS用户的实现过程如下图所示。 
[]images/ZUF-78-12-001%20-%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF2.png)主叫LTE用户已注册到IMS网络，被叫2G/3G用户已注册到CS网络，被叫承载在CS域建立，被叫应答，主被叫进入语音通话。 
CS用户呼叫LTE用户的实现过程如下图所示。 
[]images/ZUF-78-12-001%20-%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF3.png)主叫2G/3G用户已注册到CS网络，被叫LTE用户已注册到IMS网络，主叫承载在CS域建立，被叫应答，主被叫进入语音通话。 
总结
MME网元在VoLTE业务中提供如下特性： 
VoLTE能力管理MME在附着和TAU流程中指示UE IMS语音能力，UE会根据该指示决策是否发起IMS业务。MME决策IMS语音能力的策略包括：UE语音能力、无线语音能力、运营商策略、用户签约能力。如果UE语音能力、无线语音能力、运营商策略以及用户签约能力四者有其一不支持IMS VoPS，则MME通知UE不支持IMS VoPS；如果这四者都支持IMS
VoPS，则MME通知UE支持IMS VoPS。另外，苹果iWatch，在注册时，携带联合附着/TAU，但实际没有2G/3G能力，不携带SRVCC能力指示，此时要求可以携带支持IMS VoPS给终端。 
T-ADS问询被叫域问询。主被叫LTE用户都注册到IMS网络，被叫用户会在2G/3G网络和4G网络间来回驻留，主叫呼叫LTE用户时IMS需要向HSS/HLR发起被叫域问询，HSS/HLR同时向MME和SGSN发起被叫域问询，确定当前被叫用户所在域。MME上报HSS的关于支持IMS的同向性指示，UE当前位置是否支持IMS语音、最近接入时间和接入类型。 
有QoS保障的VoLTE业务一般运营商对VoLTE QoS的要求如下：QCI=1：语音承载。QCI=2：视频承载。QCI=5：SIP/SDP传输IMS信令的承载。QCI=8/9：一般上网业务承载。QCI等级资源类型优先级数据包时延预算数据包丢失率典型业务1GBR2100 ms10-2会话语音2GBR4150 ms10-3会话视频（直播流媒体）5Non-GBR1100 ms10-6IMS信令8Non-GBR8300 ms10-6视频（缓冲流媒体）基于TCP的业务99 
##### 漫游用户VoLTE业务 
如果运营商对漫游用户接入采用Local Breakout方式，即用户漫游到了拜访地，选择了拜访地的SGW和PGW，接入拜访地的网络，如下图所示。 
[]images/ZUF-78-12-001%20-%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF4.png)漫游用户在拜访地进行VoLTE语音/视频呼叫。后续漫游用户回到了归属地，用户再进行VoLTE语音/视频呼叫，由于PGW是锚定点，MME会将用户接入本地的SGW和原拜访地的PGW，SGW和PGW之间拉远了，造成承载资源的浪费，特别是对VoLTE业务加大了语音的时延。 
为了解决语音时延问题，对于本地用户，MME如果发现用户的SGW改变且用户已处于“空闲态”有一段时间，则对该用户重建IMS PDN连接，重建时PGW就近重选，保证用户接入到本地合一或拓扑最近的SGW和PGW。 
### 客户收益 
受益方|受益描述
---|---
运营商|提升无线频谱利用率、降低网络成本。
移动用户|提升用户体验，VoLTE的体验明显优于传统CS语音。
### 实现原理 
##### 涉及的网元 
网元名称|网元作用
---|---
UE|支持E-UTRAN/GERAN/UTRAN接入；支持将自身的VoLTE能力通过NAS信令传递给MME。
eNodeB|传递UE的NAS信令。
MME|能够建立用于VoLTE的IMS信令承载、视频承载和语音承载；支持将MME自身的VoLTE能力通知HSS。
HSS|向MME请求用户最新的位置更新信息，将得到的网络信息发送给IMS。
SGW|SGW通知MME建立语音和视频专有承载。
PGW|PGW通过SGW通知MME建立语音和视频专有承载。
PCRF|IMS向PCRF发起承载建立请求，PCRF向PGW提供授权的QoS策略；IMS视频语音使用audio:QCI=1、video:QCI=2的承载，SIP/SDP传输IMS信令使用QCI=5的承载。
CS网元|2G/3G用户和4G用户间进行语音通话时，CS网元负责2G/3G用户语音信令和承载的建立和处理。
IMS网元|IMS网络向融合HSS（即HSS和HLR合一设置）获取被叫网络信息，负责将呼叫路由到被叫网络和被叫用户；触发PCRF发起专有承载建立；打通主被叫间的语音信令和承载。
##### 业务流程 
注册流程
用户要进行VoLTE语音/视频呼叫时，需要先进行VoLTE注册。 
附着流程是用户注册到EPS网络上的流程，是用户开机后的第一个过程，是后续所有流程的基础。在附着过程中，MME会为用户建立一个默认承载，也可以对用户进行鉴权（用户首次附着到EPS网络上必须鉴权）。如果IMS业务APN和数据业务APN采用独立的APN，那么附着流程完成之后，EPC网络就建立了数据业务APN默认承载，用户可以通过EPS网络访问数据业务。UE再发起PDN连接请求，MME为其建立IMS
APN默认承载，用于传输IMS信令。后续语音呼叫过程中，MME为其建立IMS APN专有承载，用于传输语音和视频。 
在此流程中MME有如下处理： 
UE在Attach Request消息中携带VoLTE关键信元：UE's usage setting和Voice domain
preference。 
UE's usage setting包括以下两种取值：Voice centric：表示UE支持IMS语音业务，或CSFB语音业务，或两者都支持。支持voice centric的终端必须保证语音业务可用。如果支持voice
centric的终端在LTE网络中无法获得语音业务（即IMS语音业务和CSFB语音业务都不可用）时，终端必须去使能E-UTRAN能力，重选回GERAN或UTRAN网络。Data centric：data centric的终端即使无法在E-UTRAN网络获得语音业务的情况下，仍可以继续驻留在E-UTRAN网络中。 
Voice domain preference包括以下四种取值：0：CS Voice only，即仅支持CSFB语音业务。1：IMS PS Voice only，即仅支持IMS VoPS语音业务。2：CS voice preferred, IMS PS Voice as secondary，即优选CSFB语音业务，次选IMS
VoPS语音业务。3：IMS PS voice preferred, CS Voice as secondary，即优选IMS VoPS语音业务，次选CSFB语音业务。 
若用户为语音中心用户，则MME根据用户语音偏好以及本地配置，决策是否允许用户接入。若不允许，则拒绝附着流程，拒绝原因值取本地配置的NAS原因值。 
MME向HSS发送Update Location Request消息，消息中携带homogeneous-support-of-ims-voice-over-ps-sessions用于指示EPC网络是否支持IMS语音业务。具体参见[T-ADS](ZUF-78-12-001-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__T-ADS-D89CC13D)。
HSS向MME返回Update Location Ack消息，返回用户签约的数据APN和IMS APN以及签约的SRVCC能力（STN-SR）。 
MME向SGW/PGW发送Create Session Request消息，消息中携带数据APN，请求建立数据APN默认承载。 
SGW/PGW返回Create Session Response消息，其中携带QCI（8或9），指示建立数据APN默认承载已完成。 
MME向UE返回Attach Accept消息，消息中携带EPS network feature support信元，指示是否支持IMS
voice over PS Session，该信元由UE语音能力、无线语音能力、运营商策略以及用户签约能力共同决定。 
UE语音能力：是指UE是否支持IMS VoPS，MME根据UE在Attach请求中携带的Voice domain preference和UE's
usage setting，并结合“基于UE的语音参数策略配置”确定。 
无线语音能力：是指无线侧是否支持IMS VoPS，MME基于TA粒度确定无线侧是否支持，通过该TA关联的“基于TA的语音参数策略模板配置”确定。 
运营商策略：是指用户归属的运营商（即PLMN）是否支持IMS VoPS，使用“基于IMSI的语音参数策略配置”确定。 
用户签约能力：是指根据用户签约信息判断是否支持IMS VoPS，由UE签约IMS APN、UE签约SRVCC能力（签约STN-SR）和UE支持SRVCC能力三者确定。其中，无线语音能力和运营商策略属于网络支持的语音能力，可以分开确定，也可以合一确定。• 当需要针对特定用户在特定区域采用特定的语音能力时，使用“基于IMSI和TA的语音参数策略配置”确定。• 当无需针对特定用户在特定区域采用特定的语音能力时，无线语音能力使用“基于TA的语音参数策略配置”确定，运营商策略使用“基于IMSI的语音参数策略配置”确定。网络支持的语音能力，优先根据“基于IMSI和TA的语音参数策略配置”确定；若获取不到再根据“基于IMSI的语音参数策略配置”和“基于TA的语音参数策略配置”确定。 
如果UE语音能力、无线语音能力、运营商策略以及用户签约能力四者有其一不支持IMS VoPS，则MME通知UE不支持IMS
VoPS；如果这四者都支持IMS VoPS，则MME通知UE支持IMS VoPS。 
 说明： 
对于一些特殊的iWatch，UE没有MS Network Capability，又没有SRVCC能力，又是Voice Center，则可以通过全局开关或IMEI号段控制在决策VoIMS能力时不考虑UE的SRVCC能力。 
UE根据IMS voice over PS Session指示发起PDN连接请求，消息中携带IMS APN、Protocol
configuration options指示请求P-CSCF IPv4或IPv6地址。 
MME向SGW/PGW发送Create Session Request消息，消息中携带IMS APN（QCI=5），请求建立IMS
APN默认承载，用于传输IMS信令。 
PGW收到Create Session Request消息后，发起IP-CAN会话建立流程，即PGW向PCRF发送信用控制请求（CCR）消息，获取UE的PCC规则。 
PCRF根据SPR的签约信息、PGW上报的网络信息和PCRF的本地配置信息进行策略决策，对IMS APN的PDN连接请求进行EPS默认承载的QoS授权，并使用信用控制应答（CCA）消息下发授权的QoS信息给PGW。CCA消息里携带Default-EPS-Bearer-QoS
AVP，其QCI设置为5。 
SGW/PGW向MME返回Create Session Response消息，消息中携带关键信元PCO和QCI（QCI=5），指示建立IMS信令默认承载已完成，其中PCO包含P-CSCF的地址。 
MME发送Activate default EPS bearer context request消息给UE，通知UE激活默认承载，消息中携带Protocol
configuration options指示已分配的P-CSCF的地址。 
IMS信令承载建立后，UE发起到IMS的注册。 
LTE用户呼叫LTE用户语音流程
在此流程中MME有如下处理： 
IMS向HSS发送消息，请求获取被叫用户的T-ADS信息。 
HSS发送Insert Subscriber Data Request消息，向MME查询被叫用户的T-ADS信息。消息中携带t-ads-data-request=1，指示请求被叫域选数据。 
被叫MME返回Insert Subscriber Data Answer消息，携带查询的结果： 
ims-voice-over-ps-session-supported，指示EPC网络是否支持IMS语音业务。 
last-ue-activity-time，指示被叫用户最后一次激活时间。 
rat-type:E-UTRAN，指示用户当前附着网络类型。 
HSS向IMS发送响应消息，携带MME返回的被叫T-ADS信息。 
IMS判断当前域选到LTE网络即被叫路由到IMS，继续接续被叫，下发数据报文。如果用户处于空闲态，SGW/PGW收到下行数据报文，但是对应的承载的S1-U资源被释放，SGW缓存下行数据报文，发送下行数据通知DDN消息给MME。 
MME回确认消息给SGW，MME根据下行数据通知消息中携带的Paging and Service Information，找到对应承载的APN（IMS
APN）和QCI（5），再匹配本地配置的寻呼策略下发寻呼。 
MME寻呼到用户后，用户发起业务请求，激活已有的承载。 
被叫用户振铃，IMS已获得主叫会话信息，当前呼叫的媒体类型为audio，通知PCRF建立被叫专有承载。 
PCRF根据认证/授权请求消息携带的媒体类型和媒体描述信息做策略决策，提供授权的QoS，并通过重新认证/授权请求RAR消息将QoS（QCI=1/ARP/GBR/MBR）和PCC规则发送至PGW。 
PGW通过SGW向MME发送Create Bearer Request消息（QCI=1），指示被叫MME建立专有承载。 
被叫MME收到Create Bearer Request消息后，向被叫UE发送Activate dedicated EPS
bearer context request消息，用于请求激活一个专有EPS承载上下文。 
被叫专有承载建立完成，IMS通知PCRF建立主叫专有承载。 
主叫专有承载建立过程同被叫专有承载建立步骤9~步骤12。 
LTE用户呼叫LTE用户视频流程
在此流程中MME有如下处理： 
IMS向HSS发送消息，请求获取被叫用户的T-ADS信息。 
HSS发送Insert Subscriber Data Request消息，向MME查询被叫用户的T-ADS信息。消息中携带t-ads-data-request=1，指示请求被叫域选数据。 
被叫MME返回Insert Subscriber Data Answer消息，携带查询的结果： 
ims-voice-over-ps-session-supported，指示EPC网络是否支持IMS语音业务。 
last-ue-activity-time，指示被叫用户最后一次激活时间。 
rat-type:eutran，指示用户当前附着网络类型。 
HSS向IMS发送响应消息，携带MME返回的被叫T-ADS信息。 
IMS判断当前域选到LTE网络即被叫路由到IMS，继续接续被叫，下发数据报文。如果用户处于空闲态，SGW/PGW收到下行数据报文，但是对应的承载的S1-U资源被释放，SGW缓存下行数据报文，发送下行数据通知DDN消息给MME。 
MME回确认消息给SGW，MME根据下行数据通知消息中携带的Paging and Service Information，找到对应承载的APN（IMS
APN）和QCI（5），再匹配本地配置的寻呼策略下发寻呼。 
MME寻呼到用户后，用户发起业务请求，激活已有的承载。 
被叫用户振铃，IMS已经获得主叫会话信息，当前呼叫的媒体类型为audio和video，通知PCRF建立被叫专有承载。 
PCRF根据认证/授权请求消息携带的媒体类型和媒体描述信息做策略决策，提供授权的QoS，并通过重新认证/授权请求消息RAR消息将QoS（QCI=1，QCI=2/ARP/GBR/MBR）和PCC规则发送至PGW，其中QCI=1表示承载的语音媒体，QCI=2表示承载的视频媒体。 
PGW通过SGW向MME发送Create Bearer Request消息（QCI=1和QCI=2），指示被叫MME建立专有承载。 
被叫MME收到Create Bearer Request消息后，向被叫UE发送Activate dedicated EPS
bearer context request消息，用于请求激活一个专有EPS承载上下文。 
被叫专有承载建立完成，IMS通知PCRF建立主叫专有承载。 
主叫专有承载建立过程同被叫专有承载建立步骤9~步骤12。 
LTE用户呼叫LTE用户视频回落语音流程
在此流程中MME有如下处理： 
LTE用户与LTE用户在EPC网络下进行视频通话，主叫用户触发切换语音流程。 
IMS通知PCRF删除被叫视频承载。 
PCRF请求PGW删除被叫视频承载video：QCI=2。 
PGW通过SGW向MME发送 Delete Bearer Request消息，指示被叫MME删除视频承载。 
被叫MME收到Delete Bearer Request消息后，向被叫UE发送Deactivate EPS Bearer
Context Request消息，用于请求删除一个EPS承载上下文。 
主叫视频承载删除过程同被叫视频承载删除步骤3~步骤5。 
LTE用户呼叫CS用户流程
在此流程中MME有如下处理： 
主叫LTE用户已注册到IMS网络，被叫2G/3G用户已注册到CS网络。 
被叫承载在CS域建立。 
主叫IMS收到被叫用户回复的响应消息后通知PCRF建立主叫专有承载。 
PCRF要控制PGW建立承载，则发RAR消息给PGW。 
PGW通过SGW向MME发送Create Bearer Request消息（QCI=1），指示主叫MME建立专有承载。 
主叫MME收到Create Bearer Request消息后，向主叫UE发送Activate dedicated EPS
bearer context request消息，用于请求激活一个专有EPS承载上下文。 
被叫应答，主被叫进入语音通话。 
CS用户呼叫LTE用户流程
在此流程中MME有如下处理： 
主叫2G/3G用户已注册到CS网络，被叫LTE用户已注册到IMS网络。 
主叫承载在CS域建立。 
被叫IMS收到被叫用户回复的响应消息后通知PCRF建立被叫专有承载。 
PCRF要控制PGW建立承载，则发RAR消息给PGW。 
PGW通过SGW向MME发送Create Bearer Request消息（QCI=1），指示被叫MME建立专有承载。 
被叫MME收到Create Bearer Request消息后，向被叫UE发送Activate dedicated EPS
bearer context request消息，用于请求激活一个专有EPS承载上下文。 
被叫应答，主被叫进入语音通话。 
用户挂机释放流程
在此流程中MME有如下处理： 
用户挂机。 
IMS通知PCRF删除被叫承载。 
PCRF请求PGW删除被叫专有承载（语音承载QCI=1，视频承载QCI=2）。 
PGW通过SGW向MME发送 Delete Bearer Request消息，指示被叫MME删除专有承载。 
被叫MME收到 Delete Bearer Request消息后，向被叫UE发送Deactivate EPS Bearer
Context Request消息，用于请求删除一个EPS承载上下文。 
主叫专有承载删除过程同被叫专有承载删除步骤3~步骤5。 
VoLTE能力管理
MME在附着和TAU流程中给UE下发是否支持IMS
voice over PS Session 的指示（即IMS voice over PS Session Supported Indication），UE根据该指示决策是否发起IMS业务。该指示的决策过程如下： 
UE在Attach Request/TAU Request消息中携带VoLTE关键信元：SRVCC能力和Voice domain
preference and UE's usage setting。 
UE's usage setting指示Voice centric或Data centric：Voice centric：表示UE支持IMS语音业务，或CSFB语音业务，或两者都支持。voice centric的终端必须保证语音业务可用。如voice
centric的终端在LTE网络中无法获得voice业务（即IMS voice和CSFB都不可用）时，终端必须去使能E-UTRAN能力，重选回GERAN或UTRAN网络。Data centric：data centric的终端即使在E-UTRAN网络获得语音业务，仍可以继续驻留在E-UTRAN网络中。 
Voice domain preference指示，0：CS Voice only；1：IMS PS Voice only；2：CS
voice preferred, IMS PS Voice as secondary；3：IMS PS voice preferred,
CS Voice as secondary。 
MME向HSS获取签约信息，包括IMS APN和签约的SRVCC能力（STN-SR）。 
MME向UE返回Attach Accept/TAU Accept，消息中携带EPS network feature support信元，指示是否支持IMS
voice over PS Session，该信元由UE语音能力、无线语音能力、运营商策略和用户签约能力共同决定。 
UE语音能力：是指UE是否支持IMS VoPS，MME根据UE在Attach请求中携带的Voice domain preference
and UE's usage setting，并结合“基于UE的语音参数策略配置”确定。 
无线语音能力：是指无线侧是否支持IMS VoPS，MME基于TA粒度确定无线侧是否支持，通过该TA关联的“基于TA的语音参数策略模板配置”确定。 
运营商策略：是指根据用户IMSI号段配置是否支持IMS VoPS，通过“基于IMSI的语音参数策略配置”确定。 
用户签约能力：是指根据用户签约信息判断是否支持IMS VoPS，由UE签约IMS APN、UE签约SRVCC能力（签约STN-SR）和UE支持SRVCC能力三者确定。其中，无线语音能力和运营商策略属于网络支持的语音能力，可以分开确定，也可以合一确定。• 当需要针对特定用户在特定区域采用特定的语音能力时，使用“基于IMSI和TA的语音参数策略配置”确定。• 当无需针对特定用户在特定区域采用特定的语音能力时，无线语音能力使用“基于TA的语音参数策略配置”确定，运营商策略使用“基于IMSI的语音参数策略配置”确定。网络支持的语音能力，优先根据“基于IMSI和TA的语音参数策略配置”确定；若获取不到再根据“基于IMSI的语音参数策略配置”和“基于TA的语音参数策略配置”确定。 
如果UE语音能力、无线语音能力、运营商策略以及用户签约能力四者有其一不支持IMS VoPS，则MME通知UE不支持IMS
VoPS；如果这四者都支持IMS VoPS，则MME通知UE支持IMS VoPS。 
T-ADS
主被叫LTE用户都注册到IMS网络，被叫用户会在2G/3G网络和4G网络间来回驻留。因此主叫呼叫LTE用户时，需求决策当前被叫用户所在域：如果用户当前在2G/3G网络，SGSN不支持IMS语音，则被叫域选CS网络；如果用户当前在4G网络，EPC网络支持IMS语音，则被叫域选LTE网络，被叫路由到IMS。 
如果UE在MME和SGSN上都是注册状态，当呼叫请求到来时，IMS需要向HSS/HLR发起T-ADS问询，HSS/HLR同时向MME和SGSN发起T-ADS问询，查询UE当前位置是否支持IMS语音、最近接入时间和接入类型。 
T-ADS被叫接入域选择的实现过程如下图所示。 
[]images/ZUF-78-12-001%20-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%861.png)IMS查询HSS获取用户最近一次接入的网络是否支持IMS：当前PS域支持IMS则被叫路由到IMS，否则路由到CS。 
T-ADS上报：
MME上报HSS是否支持T-ADS Data Retrieval，由软件参数控制（262305
 支持T-ADS基本查询功能）。
MME上报给HSS的关于支持IMS的同向性指示（即Homogenous
Support of IMS Voice over PS Sessions Indication），可上报“都支持”、“都不支持”、“部分支持/未知”，用于减少HSS查询用户当前服务节点的次数。MME可通过ULR和NOR上报给HSS，如下图所示。 
[]images/ZUF-78-12-001%20-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%862.png)[]images/ZUF-78-12-001%20-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%863.png)MME向HSS发送Update Location Request/Notify
Request消息，消息中携带Homogenous Support of IMS Voice over PS Sessions Indication信元，指示是否支持IMS
voice over PS Session。该信元由无线语音能力或UE语音能力、运营商策略和用户签约能力共同决定。 
软件参数“MME根据TA能力上报Homogeneous
Support Of IMS VoPS字段”（ID：262371）的取值不同，MME就会根据不同的策略判断并通知HSS是否支持IMS
VoPS。 
该软件参数值设置为1（即支持）：如果无线语音能力、运营商策略和用户签约能力三者有其一不支持IMS VoPS，那么MME通知HSS不支持IMS
VoPS；如果三者都支持IMS VoPS，那么MME通知HSS支持IMS VoPS。 
该软件参数值设置为0（即不支持）：如果UE语音能力、运营商策略和用户签约能力三者有其一不支持IMS VoPS，那么MME通知HSS不支持IMS
VoPS；如果三者都支持IMS VoPS，那么MME通知HSS支持IMS VoPS。 
T-ADS查询：
如果UE只在MME上注册（即单注册），那么HSS根据MME上报给HSS的T-ADS信息进行决策，参见下表。 
如果|那么
---|---
是否支持T-ADS Data Retrieval|Homogenous Support of IMS Voice over PS Sessions Indication|是否向MME发起T-ADS查询
否|Supported/Not Supported/Unknown|否
是|Supported|否
是|Not Supported|否
是|Unknown|是
如果UE在MME和SGSN上都是注册状态（即双注册），并且MME支持T-ADS Data Retrieval，向HSS上报T-ADS信息，那么HSS进行如下决策，参见下表。 
如果|那么
---|---
SGSN上报的Homogenous Support of IMS Voice over PS SessionsIndication|MME上报的Homogenous Support of IMS Voice over PS Sessions Indication|是否向SGSN和MME同时发起T-ADS查询
Not Supported|Not Supported|否
Not Supported|Supported|是
Not Supported|Unknown|是
Unknown|Supported|是
None|Not Supported|是
None|None|是
HSS与MME之间的T-ADS查询流程如下图所示。 
[]images/ZUF-78-12-001%20-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%864.png)HLR与SGSN之间的T-ADS查询流程如下图所示。 
[]images/ZUF-78-12-001%20-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%865.png)对于以上两个T-ADS查询流程，说明如下： 
HSS/HLR通过Insert Subscriber Data Request消息，向MME查询被叫用户的T-ADS信息。HSS/HLR通过PSI
Req消息，向SGSN查询被叫用户的T-ADS信息。 
被叫MME返回Insert Subscriber Data Answer消息，携带查询的结果：EPC网络是否支持IMS语音业务、被叫用户最后一次激活时间和用户当前附着网络类型（E-UTRAN）。被叫SGSN返回PSI
Ack消息，携带查询结果：GPRS网络是否支持IMS语音业务、被叫用户最后一次激活时间和用户当前附着网络类型（UTRAN或GERAN）。 
如果EPC网络支持IMS语音业务，HSS/HLR需要比较被叫用户在2G/3G网络和4G网络最后一次激活的时间，找到最近一次激活的网络确定被叫域选网络。如果用户最近一次激活的网络是4G网络，则被叫域选LTE网络；如果用户最近一次激活的网络是2G/3G网络，则被叫域选CS网络。HSS/HLR再将选择的被叫域通知IMS。 
如果EPC网络不支持IMS语音业务，则被叫域选CS网络。HSS/HLR再将选择的被叫域通知IMS。UE在MME和SGSN上都是注册状态（即双注册）时，IMS需要向HLR和HSS同时发起T-ADS问询，呼叫时延较大。可通过单域注册机制保证UE只附着在MME或SGSN下，其中一方的附着请求将触发另外一方的分离流程。  
VoLTE容灾
语音容灾，是指IMS/EPC/CS网络中，网元设备出现故障后，能够保证语音业务及时接管和恢复的功能。 
对于VoLTE业务，EPC网络作为VoLTE业务的承载提供者，需要在网元设备出现故障后，能够及时进行EPS承载的重建，以保证VoLTE业务及时恢复。 
SRVCC
SRVCC（Single Radio Voice Call Continuity）是3GPP提出的一种VoLTE语音业务连续性方案，主要是为了解决当单射频UE
在LTE网络和2/3G CS 网络之间移动时，如何保证语音呼叫连续性的问题，即保证单射频UE 在IMS 控制的VoIP 语音和CS
域语音之间的平滑切换。 
SGW改变重建IMS PDN连接
某些运营商对国内漫游用户采用的是Local
Breakout方式，即用户漫游到外省时，在外省建立的PDN连接，选择了拜访地的PGW。由于PGW是锚定点，用户从外省回到归属地后，还是会接入拜访地的PGW，而接入的SGW是本地的，SGW和PGW之间拉远了，造成承载资源的浪费，特别是对VoLTE业务造成了语音的时延。 
MME对本网用户，发现SGW改变，对处于“空闲态”一段时间的用户重建IMS PDN连接（PGW就近重选）。 
VoLTE保障信令流程
VoLTE保障信令流程是指在网络侧流程和UE或无线侧流程冲突时,保障业务正确的处理流程。 
VoLTE专有承载都是通过网络侧建立或修改流程来完成的，使得网络侧流程和终端侧或无线侧流程并发冲突概率增加。 
当MME发现网络侧发起的专有承载操作和UE或无线发起的业务流程冲突时，如果判断SGW不改变，则缓存专有承载操作，等UE或无线侧的业务流程完成后，继续执行专有承载操作；如果判断SGW发生改变，则直接给SGW回失败，并携带特殊原因，PGW延时后重新触发专有承载操作。 
### 系统影响 
网络中的VoLTE用户数以及用户语音业务的话务模型，决定了MME开启VoLTE功能后，MME实际上增加的负荷。 
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
该特性不涉及与其他特性的交互。 
### 遵循标准 
标准名称|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".|5.3.2 Attach procedure
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3".|-
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS".|-
3GPP TS 23.003: "Numbering, addressing and identification"|-
### 特性能力 
名称|指标
---|---
基于TA的语音参数策略模板配置|最多支持配置255个基于TA的语音参数策略模板。
基于IMSI的语音参数策略配置|最多支持配置8192个IMSI号段。
基于IMSI和TA的语音参数策略配置|最多支持配置2048个基于IMSI和TA的语音参数策略。
### 可获得性 
##### License要求 
该特性为ZXUN uMAC的基本特性，无需License支持。
##### 对其他网元的要求 
要求参与VoLTE的各网元功能，均依据3GPP协议规定。 
##### 工程规划要求 
EPC网络中，MME、SGW、PGW均采用POOL的方式实现负荷分担和网元间的冗余备份。 
### O&M相关 
##### 命令 
配置项表1  新增配置项配置项命令基于UE的语音参数策略配置SET DEFAULT VOICESET POLICYSHOW DEFAULT VOICESET POLICYADD UE VOICE POLICYSET UE VOICE POLICYDEL UE VOICE POLICYSHOW UE VOICE POLICY基于TA的语音参数策略模板配置SET DEFAULT TA VOICE POLICYSHOW DEFAULT TA VOICE POLICYADD TA VOICESET POLICY TEMPLATESET TA VOICESET POLICY TEMPLATEDEL TA VOICESET POLICY TEMPLATESHOW TA VOICESET POLICY TEMPLATE基于IMSI的语音参数策略配置SET DEFAULT IMSI VOICE POLICYSHOW DEFAULT IMSI VOICE POLICYADD IMSI VOICE POLICYSET IMSI VOICE POLICYDEL IMSI VOICE POLICYSHOW IMSI VOICE POLICY基于IMSI和TA的语音参数策略模板配置ADD IMSI TA VOICE POLICYSET IMSI TA VOICE POLICYDEL IMSI TA VOICE POLICYSHOW IMSI TA VOICE POLICY基于IMEI的语音参数策略配置SET DEFAULT IMEI VOICE POLICYSHOW DEFAULT IMEI VOICE POLICYADD IMEI VOICE POLICYSET IMEI VOICE POLICYDEL IMEI VOICE POLICYSHOW IMEI VOICE POLICYMME寻呼策略因子配置ADD MME PAGING POLICY FACTORSET MME PAGING POLICY FACTORDEL MME PAGING POLICY FACTORSHOW MME PAGING POLICY FACTORDiameter局向配置ADD DIAMADJSET DIAMADJDEL DIAMADJSHOW DIAMADJIMS APN配置ADD IMS APNDEL IMS APNSHOW IMS APNADD PLMN IMS APNDEL PLMN IMS APNSHOW PLMN IMS APN默认承载重建策略配置SET DEFAULT BEARER REBUILDSHOW DEFAULT BEARER REBUILD需重建默认承载的APN配置ADD REBUILD BEARER APNDEL REBUILD BEARER APNSHOW REBUILD BEARER APN语音中心用户限制模板配置ADD VC USER RESTRICT POLICY PROFILESET VC USER RESTRICT POLICY PROFILEDEL VC USER RESTRICT POLICY PROFILESHOW VC USER RESTRICT POLICY PROFILE语音中心用户限制策略配置SET VC USER RESTRICT POLICYSHOW VC USER RESTRICT POLICY 
安全变量表2  修改配置项安全变量命令MME支持基于PS会话IMS语音SET PACKET DOMAIN PARAMETER 
软件参数表3  新增软件参数软件参数ID软件参数名称262371MME根据TA能力上报Homogeneous Support Of IMS VoPS字段262411支持NOR携带Homogeneous Support of IMS Voice Over PS Sessions262305支持T-ADS基本查询功能262501获取签约数据的ULR携带Homogeneous Support of IMS Voice Over PS Sessions262340扣压Homogeneous Support Of IMS Voice Over PS Sessions字段262379IMSVoPS能力变化时更新HSS262307IDA无条件上报T-ADS信息262293默认HSS局向路由协议版本号 
##### 性能统计 
测量类型|描述
---|---
基于APN的承载激活流程测量|编号为C46300开头的所有计数器
基于APN的承载修改流程测量|编号为C46301开头的所有计数器
基于APN承载的去激活流程测量|编号为C46302开头的所有计数器
基于QCI的承载激活流程测量|编号为C46411开头的所有计数器
基于QCI的承载修改流程测量|编号为C46412开头的所有计数器
基于QCI的承载去激活流程测量|编号为C46413开头的所有计数器
基于QCI的切换流程测量|编号为C46414开头的所有计数器
基于QCI的跟踪区更新流程测量|编号为C46415开头的所有计数器
基于QCI的业务请求流程测量|编号为C46416开头的所有计数器
基于QCI的eNB发起的S1释放流程测量|编号为C46427开头的所有计数器
基于QCI的MME发起的S1释放流程测量|编号为C46428开头的所有计数器
基于QCI的eNB发起的E-RAB释放流程测量|编号为C46429开头的所有计数器
基于QCI的MME发起的E-RAB释放流程测量|编号为C46430开头的所有计数器
基于QCI的承载激活分网元测量|编号为C46417开头的所有计数器
基于QCI的承载修改分网元测量|编号为C46418开头的所有计数器
基于QCI的切换分网元测量|编号为C46420开头的所有计数器
基于QCI的跟踪区更新分网元测量|编号为C46421开头的所有计数器
基于QCI的业务请求分网元测量|编号为C46422开头的所有计数器
基于QCI的承载数量测量|编号为C46431开头的所有计数器
基于QCI的创建承载数量测量|编号为C46432开头的所有计数器
基于QCI的删除承载数量测量|编号为C46433开头的所有计数器
承载激活流程组合条件测量|编号为C47011开头的所有计数器
承载修改流程组合条件测量|编号为C47012开头的所有计数器
承载去激活流程组合条件测量|编号为C47013开头的所有计数器
承载激活分网元组合条件测量|编号为C47014开头的所有计数器
承载修改分网元组合条件测量|编号为C47015开头的所有计数器
性能计数器名称
---
C430090008 默认承载去激活请求次数(重建PDN连接原因)
C430030015 MME发起的EPS去附着请求次数(删除最后一个PDN)
##### 告警和通知 
该特性不涉及告警/通知消息的变化。 
##### 业务观察/失败观察 
该特性不涉及业务观察/失败观察的变化。 
##### 话单与计费 
该特性不涉及话单与计费的变化。 
## 特性配置 
## 特性配置 
### 配置说明 
通过配置，可实现4G用户之间的语音通话和视频通话、4G用户和2G/3G用户之间的语音通话。 
### 配置前提 
MME基础配置已经完成，即用户可以在MME附着并建立语音承载。 
### 配置过程 
配置IMS语音指示、T-ADS和相关软件参数。 
配置IMS APN。 
配置语音寻呼策略。 
配置默认承载重建。 
配置语音中心用户限制策略。 
### 配置实例 
#### 摘要 
本节以实现4G用户之间的语音通话/视频通话为例进行配置。 
对于4G用户与2G/3G用户之间的语音通话： 
LTE用户呼叫CS用户时，不需要配置MME寻呼策略因子。 
CS用户呼叫LTE用户时，配置同4G用户之间的语音通话。 
4G用户间语音通话的第一步是主被叫用户注册到IMS网络，因此先进行IMS语音指示配置；第二步确定被叫域，进行T-ADS配置。 
##### IMS语音能力指示配置 
终端IMS语音能力指示是在用户附着接入EPC网络的过程完成的。MME通过5个方面进行综合判断，即本局IMS语音能力、终端语音能力、TA语音能力、基于IMSI语音能力和用户IMS语音能力签约。当MME判断该5个条件的IMS语音能力均为支持时，那么MME指示终端IMS语音能力为支持；否则，指示为不支持。 
MME全局IMS语音能力配置
“MME支持基于PS会话IMS语音”安全变量配置是全局控制总开关。 
如果配置为支持，配置命令为SET PACKET DOMAIN PARAMETER:MMEIMSVOPS="YES"。 
如果配置为不支持，配置命令为SET PACKET DOMAIN PARAMETER:MMEIMSVOPS="NO"，那么MME在Attach Accept/TAU Accept消息中指示终端IMS语音能力为不支持，不需要再考虑任何其他IMS的相关配置。 
MME根据终端语音策略获取IMS语音能力配置
UE在Attach Request/TAU Request消息中携带的UE's usage setting、Voice
domain preference参数分别对应命令中的“UE使用设置”、“E-UTRAN语音优先策略参数”，MME针对不同的“UE使用设置”和“E-UTRAN语音优先策略”的参数组合，配置不同的策略。
MME根据UE's usage setting和Voice domain preference，在“基于UE的语音参数策略配置”记录中进行匹配查找，先匹配通过[ADD UE VOICE POLICY](../../MMESGSN\zh-CN\mml\1261635.html)命令配置的记录，如未匹配到，就使用通过[SET DEFAULT VOICESET POLICY](../../MMESGSN\zh-CN\mml\1261632.html)命令配置的缺省策略。
如果网络无特殊要求，可以直接使用[SET DEFAULT VOICESET POLICY](../../MMESGSN\zh-CN\mml\1261632.html)命令配置的缺省策略；如果网络需要针对特定的UE's usage setting和Voice domain preference的组合来配置特定的策略，则使用[ADD UE VOICE POLICY](../../MMESGSN\zh-CN\mml\1261635.html)命令进行配置。
配置实例
现有如下三种不同语音能力的终端： 
UE1的语音能力为Voice centric和IMS PS Voice only，规划需要支持IMS语音。 
UE2的语音能力为Voice centric和IMS PS voice preferred, CS Voice as
secondary，规划需要支持IMS语音。 
UE3的语音能力为Data centric和CS Voice only，规划不支持IMS语音。 
配置脚本
配置语音能力为Data centric和CS Voice only的终端不支持IMS语音，UE3使用该语音策略。 
[ADD UE VOICE POLICY](../../MMESGSN\zh-CN\mml\1261635.html):USAGESET="DATA",VOICEPREFER="CSVOICE",IMSVOPS="NOSPRT"
配置默认语音策略为支持IMS语音，UE1和UE2使用该语音策略。 
[SET DEFAULT
VOICESET POLICY](../../MMESGSN\zh-CN\mml\1261632.html):IMSVOPS="SPRT"
MME基于TA的语音能力配置
TA语音参数策略是配置TA的语音能力，需要根据现网TA的实际语音能力来进行配置。通过配置TA关联语音策略模板来配置语音能力；如果TA中未关联语音策略模板，那么使用本配置中的默认语音策略。 
配置实例
现有如下三个TA： 
TA1的TAID为1，规划支持IMS语音。 
TA2的TAID为2，规划支持IMS语音。 
TA3的TAID为3，规划不支持IMS语音。 
配置脚本
配置语音策略模板1，配置该模板不支持IMS语音。 
[ADD TA VOICESET POLICY
TEMPLATE](../../MMESGSN\zh-CN\mml\1261768.html):POLICYID=1,DFTIMSVOPS="NOSPRT"
配置默认语音策略支持IMS语音。 
[SET DEFAULT TA VOICE POLICY](../../MMESGSN\zh-CN\mml\1261892.html):IMSVOPS="SPRT"
配置TA1引用语音策略模板0，表示TA1使用默认语音策略。 
[SET TA](../../MMESGSN\zh-CN\mml\1262204.html):TAID=1,POLICYID=0
配置TA2引用语音策略模板0，表示TA2使用默认语音策略。 
[SET TA](../../MMESGSN\zh-CN\mml\1262204.html):TAID=2,POLICYID=0
配置TA3引用语音策略模板1，表示TA3使用语音策略模板1中的语音策略。 
[SET TA](../../MMESGSN\zh-CN\mml\1262204.html):TAID=3,POLICYID=1
MME基于IMSI的语音能力配置
IMSI语音策略是基于IMSI号段来选择语音策略，主要是针对漫游用户。运营商可以通过该配置来灵活设置漫游用户的VoLTE业务的使用。如果未配置基于IMSI的语音策略，那么使用本配置中的默认语音策略。 
配置实例
现有如下三种IMSI号段的用户： 
IMSI号段为46001的用户，规划支持IMS语音。 
IMSI号段为46013的用户，规划支持IMS语音。 
IMSI号段为45400的用户，规划不支持IMS语音。 
配置脚本
配置IMSI号段为45400的用户的语音策略为不支持IMS语音。 
[ADD IMSI VOICE
POLICY](../../MMESGSN\zh-CN\mml\1261950.html):IMSI="45400",IMSVOPS="NO"
配置默认语音策略支持IMS语音，不进行用户的IMS APN和STN-SR签约检查，也不进行MME支持SRVCC能力的检查，IMSI号段为46001和46013的用户使用该语音策略。 
[SET DEFAULT IMSI VOICE POLICY](../../MMESGSN\zh-CN\mml\1261955.html):IMSVOPS="SPRT"
 说明： 
如果要进行用户的IMS APN和STN-SR签约检查，或MME支持SRVCC能力的检查，请参考“[MME根据用户签约和SRVCC能力获取IMS语音能力配置](ZUF-78-12-001-14-%E7%89%B9%E6%80%A7%E9%85%8D%E7%BD%AE.html#T_20175108424919__MME%E6%A0%B9%E6%8D%AE%E7%94%A8%E6%88%B7%E7%AD%BE%E7%BA%A6%E5%92%8CSRVCC%E8%83%BD%E5%8A%9B%E8%8E%B7%E5%8F%96IMS%E8%AF%AD%E9%9F%B3%E8%83%BD%E5%8A%9B%E9%85%8D%E7%BD%AE-D92DB300)”
。
MME基于IMSI和TA的语音能力配置 
IMSI和TA语音策略是同时基于IMSI号段和“语音参数策略区域编号”来选择语音策略。其中，TA语音参数策略区域编号是配置TA的语音能力，需要根据现网TA的实际语音能力来进行配置。通过配置TA关联语音参数策略区域编号来配置语音能力。 
配置实例
现有如下二种场景： 
TA1的TAID为1，IMSI号段为46001的用户，规划支持IMS语音。 
TA2的TAID为2，IMSI号段为45400的用户，规划不支持IMS语音。 
配置脚本
配置语音参数策略区域编号1，IMSI号段为46001的用户，语音策略为支持IMS语音。 
[ADD IMSI TA VOICE POLICY](../../MMESGSN\zh-CN\mml\1262664.html):IMSI="46001",VOICEPLYAREAID=1,IMSVOPS="YES"
配置语音参数策略区域编号2，IMSI号段为45400的用户，语音策略为不支持IMS语音。 
[ADD IMSI TA VOICE POLICY](../../MMESGSN\zh-CN\mml\1262664.html):IMSI="45400",VOICEPLYAREAID=2,IMSVOPS="NO"
配置TA1引用语音参数策略区域编号1。 
[SET TA](../../MMESGSN\zh-CN\mml\1262204.html):TAID=1,VOICEPLYAREAID=1
配置TA2引用语音参数策略区域编号2。 
[SET TA](../../MMESGSN\zh-CN\mml\1262204.html):TAID=2,VOICEPLYAREAID=2
MME根据用户签约和SRVCC能力获取IMS语音能力配置
基于用户签约下发终端IMS语音能力主要是检查用户的IMS APN、STN-SR的签约以及终端SRVCC能力和MME支持SRVCC能力。如果运营商决策不需要根据用户签约和SRVCC能力，可以忽略此配置步骤。 
配置IMEI号段为50001的用户的语音策略为“不根据SRVCC能力决策IMS VoPS能力” 
[ADD IMEI VOICE POLICY](../../MMESGSN\zh-CN\mml\1263242.html):IMEI="50001",IFVOPSBASEDSRVCCCAPA="NOT_BASE_ON_SRVCC"
配置默认语音策略为“根据SRVCC能力决策IMS VoPS能力”，非50001的IMEI号段用户使用该语音策略。 
[SET DEFAULT IMEI VOICE POLICY](../../MMESGSN\zh-CN\mml\1263239.html):IFVOPSBASEDSRVCCCAPA="BASE_ON_SRVCC"
 说明： 
该配置默认语音策略为“不根据SRVCC能力决策IMS VoPS能力”。如果配置为“根据SRVCC能力决策IMS VoPS能力”，MME会检查终端SRVCC能力和MME支持SRVCC功能的License。当终端不支持SRVCC或者MME不支持SRVCC时，MME给终端指示IMS语音能力为不支持，终端无法使用IMS语音业务。考虑苹果手表终端应用场景，配置为“根据SRVCC能力和2G3G能力决策IMS VoPS能力”，MME会检查终端SRVCC能力和MS Network Capability能力。当终端不支持SRVCC也没携带MS Network Capability，且为Voice centric，MME给终端指示IMS语音能力为支持，终端可以使用IMS语音业务。 
配置IMSI号段为46001的语音策略为“不支持根据IMS APN签约决策IMS VoPS能力” 
[ADD IMSI VOICE POLICY](../../MMESGSN\zh-CN\mml\1261950.html):IMSI="46001",IMSAPNCHK="NO"
配置默认语音策略为“支持根据IMS APN签约决策IMS VoPS能力”，非46001的IMSI号段用户使用该语音策略。 
[SET DEFAULT IMSI VOICE POLICY](../../MMESGSN\zh-CN\mml\1261955.html):IMSAPNCHK="YES"
 说明： 
该配置默认语音策略为“不支持根据IMS APN签约决策IMS VoPS能力”。如果配置为“支持根据IMS APN签约决策IMS VoPS能力”，MME会检查用户是否签约IMS APN，如果用户未签约IMS APN，MME指示终端IMS语音不支持。 
配置通用IMS APN，MME根据该配置检查用户签约的APN中是否包含名称为ims的APN，如果包含该APN，说明用户有使用IMS语音的权限。 
[ADD IMS APN](../../MMESGSN\zh-CN\mml\1261784.html):APNNAME="ims"
配置IMSI号段为46001的语音策略为“不支持根据STN-SR签约决策IMS VoPS能力” 
[SET DEFAULT IMSI VOICE POLICY](../../MMESGSN\zh-CN\mml\1261955.html):IMSI="46001",STNSRCHK="NO"
配置默认语音策略为“支持根据STN-SR签约决策IMS VoPS能力”，非46001的IMSI号段用户使用该语音策略。 
[SET DEFAULT IMSI VOICE POLICY](../../MMESGSN\zh-CN\mml\1261955.html):STNSRCHK="YES"
 说明： 
该配置默认语音策略为“不支持根据STN-SR签约决策IMS VoPS能力”。如果配置为“支持根据STN-SR签约决策IMS VoPS能力”，MME会检查用户是否签约STN-SR，如果用户未签约STN-SR，MME指示终端IMS语音不支持。 
##### T-ADS配置 
T-ADS被叫域选择过程中，MME收到T-ADS查询后，需要将用户的IMS
Voice over PS SessionsSupported（IMS语音支持能力）、Last UE Activity Time（用户的最后活动时间）、RAT
Type（当前的无线接入类型）信息在IDA消息中携带给HSS。 
本节介绍如何配置MME的T-ADS域选功能，使LTE用户在被叫时能够选择一个合适的网络接入，并接通呼叫。 
配置实例
MME开启T-ADS域选功能。 
配置脚本
配置MME支持T-ADS查询功能。 
设置软件参数“支持T-ADS基本查询功能”（ID：262305）的取值为1，用于MME向HSS指示本网元支持T-ADS查询功能。
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262305,PARAVALUE=1
配置HSS局向Diameter协议支持R9。 
MME上报HSS的IMS语音同向性指示信元需要R9及以上协议版本的Diameter消息才能携带。如果配置为支持R8协议版本，Diameter消息中不会携带该信元，那么每次VoLTE呼叫都需要HSS执行T-ADS查询流程。 
[SET DIAMADJ](../../MMESGSN\zh-CN\mml\1262151.html):ADJID=1,PROVERSION="R9"
（可选）配置根据TA能力上报IMS语音同向性指示，对应软件参数“MME根据TA能力上报Homogeneous Support
Of IMS VoPS字段”（ID：262371）。
该软件参数用于配置MME上报HSS的IMS语音同向性信元的取值选取方式。 
当软件参数取值为0时，信元取值由UE语音能力、运营商策略以及用户签约能力决定。 
当软件参数取值为1时，信元取值由无线语音能力、运营商策略以及用户签约能力决定。 
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262371,PARAVALUE=0
配置支持IMS语音能力变化时通知HSS，对应软件参数“IMSVoPS能力变化时更新HSS”（ID：262379）。
该软件参数用于配置当IMS语音能力变更时，MME是否将变更后的IMS语音能力及时通知给HSS。 
典型应用场景： 
终端IMS语音能力变更。 
用户从支持IMS语音的TA移动到不支持IMS语音的TA或者相反。 
网络侧配置变更导致IMS语音能力发生变化。 
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262379,PARAVALUE=1
配置支持NOR消息携带IMS语音同向性指示，对应于软件参数“支持NOR携带Homogeneous Support
of IMS Voice Over PS Sessions”（ID：262411）。
该软件参数配置用于当IMS语音能力变更时，MME是否可以通过NOR消息将变更后的IMS语音能力携带给HSS。该软件参数的使用前提是打开软件参数262379，且HSS局向的Diameter协议版本支持R10及以上版本。 
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262411,PARAVALUE=1
（可选）配置TALIST分配策略。 
该命令配置是将具有相同IMS语音能力的TA分配到一个TALIST中，目的是防止用户在一个TALIST中的TA移动，源TA和目的TA的IMS语音能力不一致时，不能及时通知HSS的问题。如果全网TA支持IMS语音，可以忽略此配置。 
[SET TALIST ASSIGN POLICY](../../MMESGSN\zh-CN\mml\1266006.html):SAMEIMSVOPS="YES"
配置MME支持用户状态查询，对应软件参数“是否支持查询用户状态和位置”（ID：262312）。
该软件参数配置实际上与T-ADS域选功能没有关系。但是ZTE IMS网元查询被叫T-ADS的时候会同时查询用户状态信息，确认用户当前是否驻留在EPC网络。MME收到HSS的用户状态查询请求时，会将用户当前的状态IDLE或Connect在IDA消息中携带给HSS。 
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262312,PARAVALUE=1
##### 语音寻呼配置 
语音寻呼配置目的是将VoLTE语音寻呼和普通数据业务的智能寻呼策略区分开，通过VoLTE语音寻呼策略的优化配置，提高VoLTE语音寻呼的寻呼成功率，减少寻呼时长。VoLTE语音寻呼策略的配置可以通过QCI、IMS
APN、PPI等信息来进行配置。 
配置实例
现有一种寻呼策略：GUTI在TALIST中寻呼,寻呼时长50ms，寻呼优先级1。 
现有四种方式获取寻呼策略： 
根据QCI=1获取VoLTE语音寻呼策略。 
根据QCI=5获取VoLTE语音寻呼策略。 
根据PPI=1获取VoLTE语音寻呼策略。 
根据IMS APN=ims获取VoLTE语音寻呼策略。 
配置脚本
配置VoLTE语音寻呼策略，寻呼方式为GUTI在TALIST寻呼，寻呼时长50ms，寻呼优先级1。 
[ADD
MME PS PAGING POLICY](../../MMESGSN\zh-CN\mml\1260689.html):ID=51,PAGEPOLICY="GUTITALIST"-50-"PRIO_0"
配置QCI=1的寻呼策略因子，引用步骤1中的寻呼策略ID。MME根据语音业务下行专有承载建立请求消息的QCI来选择该寻呼策略。 
[ADD MME PAGING POLICY FACTOR](../../MMESGSN\zh-CN\mml\1260704.html):QCI=1,PGPOLICY="PS"-51
配置QCI=5的寻呼策略因子，引用步骤1中的寻呼策略ID。MME根据语音业务DDN消息中携带的EBI获取承载的QCI，再根据该QCI来选择该寻呼策略。 
[ADD MME PAGING POLICY FACTOR](../../MMESGSN\zh-CN\mml\1260704.html):QCI=5,PGPOLICY="PS"-51
配置PPI=1的寻呼策略因子，引用步骤1中的寻呼策略ID。MME根据语音业务DDN消息中携带的PPI来选择该寻呼策略。 
[ADD MME PAGING POLICY FACTOR](../../MMESGSN\zh-CN\mml\1260704.html):QCI=0,PPI=1,PGPOLICY="PS"-51
配置IMS APN的寻呼策略因子，引用步骤1中的寻呼策略ID。 
[ADD MME PAGING
POLICY FACTOR](../../MMESGSN\zh-CN\mml\1260704.html):QCI=0,APNNI="ims",PPI=0,PGPOLICY="PS"-51
##### 基于TA的语音中心用户限制策略配置 
基于TA的语音中心用户限制策略配置目的是以TA为单位，针对用户的语音能力，对用户接入进行限制。 
配置实例
TA1的TAID为1。 
限制语音能力为CS Voice Only的用户接入，拒绝原因值为Illegal UE。 
限制语音能力为IMS PS Voice Only的用户接入，拒绝原因值为Illegal UE。 
限制语音能力为CS Voice Prefer的用户接入，拒绝原因值为EPS services and non-EPS services not allowed。 
限制语音能力为IMS PS Voice Prefer的用户接入，拒绝原因值为Illegal ME。 
配置脚本
设置当前MME支持语音中心用户限制功能。 
[SET VC USER RESTRICT POLICY](../../MMESGSN\zh-CN\mml\1269766.html):IVCUSERLIMIT=”YES“
新建限制策略模板。 
[ADD VC USER RESTRICT POLICY PROFILE](../../MMESGSN\zh-CN\mml\1269762.html):POLICYID=1,CSVOICEONLYPOLICY="NO"-"NO"-"REJECTCAUSE_3",IMSPSVOICEONLYPOLICY="NO"-"NO"-"REJECTCAUSE_3",IMSPSVOICEVPREPOLICY="NO"-"NO"-"REJECTCAUSE_6",CSVOICEVPREPOLICY="NO"-"NO"-"REJECTCAUSE_8"
将新建的策略模板与TA进行关联。 
[SET TA](../../MMESGSN\zh-CN\mml\1262204.html):TAID=1,VCUSERLIMITPLYID=1
### 测试用例 
##### 4G用户间的语音通话 
测试项目|4G用户呼叫4G用户，通话正常
测试目的|验证呼叫建立成功，通话正常
预置条件|主被叫用户已注册到EPC网络。主被叫用户、无线和运营商都支持IMS语音。主被叫用户已建立语音信令默认承载（QCI=5）。主被叫用户已注册到IMS网络。主被叫最近接入的网络是LTE网络。
测试过程|主叫用户发起语音呼叫请求。在网络侧查询用户的信息。
通过准则|主被叫用户通话是否正常。主被叫语音专有承载是否建立成功（QCI=1）。被叫域是否选LTE网络，被叫是否路由到IMS。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|–
##### 4G用户间的视频通话 
测试项目|4G用户视频呼叫4G用户，视频通话正常
测试目的|验证呼叫建立成功，视频通话正常
预置条件|主被叫用户已注册到EPC网络。主被叫用户、无线和运营商都支持IMS语音。主被叫用户已建立语音信令默认承载。主被叫用户已注册到IMS网络。主被叫最近接入的网络是LTE网络。
测试过程|主叫用户发起视频呼叫请求。在网络侧查询用户的信息。
通过准则|主被叫用户视频通话是否正常。主被叫语音专有承载是否建立成功（QCI=1）。主被叫视频专有承载是否建立成功（QCI=2）。被叫域是否选LTE网络，被叫是否路由到IMS。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|–
##### 4G用户与2G/3G网络用户间的语音通话 
测试项目|4G用户呼叫2G/3G用户，通话正常
测试目的|验证呼叫建立成功，通话正常
预置条件|主叫用户已注册到EPC网络。主叫用户、无线和运营商都支持IMS语音。主叫用户已建立语音信令默认承载。主叫用户已注册到IMS网络。被叫用户已注册到CS网络。主叫最近接入的网络是LTE网络。
测试过程|主叫用户发起语音呼叫请求。在网络侧查询主叫用户的信息。
通过准则|主被叫用户通话是否正常。主叫语音专有承载是否建立成功（QCI=1）。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|–
测试项目|2G/3G用户呼叫4G用户，通话正常
测试目的|验证呼叫建立成功，通话正常
预置条件|被叫用户已注册到EPC网络。被叫用户、无线和运营商都支持IMS语音。被叫用户已建立语音信令默认承载。被叫用户已注册到IMS网络。主叫用户已注册到CS网络。被叫最近接入的网络是LTE网络。
测试过程|主叫用户发起语音呼叫请求。在网络侧查询被叫用户的信息。
通过准则|主被叫用户通话是否正常。被叫语音专有承载是否建立成功（QCI=1）。被叫域是否选LTE网络，被叫是否路由到IMS。消息跟踪是否能够跟踪到相应的消息，流程是否正确。
测试结果|–
##### 基于TA的语音用户限制 
测试项目|基于TA的语音用户限制接入
测试目的|验证TA范围内，特定语音能力的用户限制接入MME
预置条件|MME限制语音中心用户的功能开关打开。用户的语音能力对于的限制模板已配置，并且已和接入的TA进行关联。
测试过程|用户发起Attach流程。
通过准则|Attach流程被拒绝。Attach Reject消息中携带的原因值跟配置的原因值是一致的。
测试结果|–
### 常见问题处理 
无。 
# ZUF-78-12-002 T-ADS 
## 概述 
T-ADS表示随机接入域选择数据的检索。利用T-ADS，IMS的SCC-AS可以获得信息以决定IMS语音业务将选择哪个承载PS/CS。
## 收益 
支持IMS Voice over PS Sessions服务。 
## 描述 
开关打开时，MME可能会在UE当前注册的所有服务节点中携带支持T-ADS Data Retrieve和IMS Voice over PS Sessions的同构支持的指示，也可能会应答HSS发送的T-ADS Data Request消息。 
用户可同时注册在CS和LTE域，当语音呼叫此用户时，HSS向MME发送IDR消息，请求用户上下文信息（是否支持VOLTE，最近活动时间，所在的RAT类型），MME通过IDA响应返回以上信息，以便网络判断走CS语音还是LTE语音。 
# ZUF-78-12-003 LTE IMS紧急会话支持 
## 特性描述 
## 特性描述 
### 术语 
术语|含义
---|---
紧急呼叫|所谓紧急呼叫是指用户拨打报警或求救号码。这些号码的紧急性使各国都规定这些号码可以使用任何当时可用的网络。
紧急承载|为紧急呼叫而建立的EPS承载。
紧急附着|紧急呼叫触发的附着。
紧急PDN连接|为紧急呼叫而建立的PDN连接。
### 描述 
##### 定义 
紧急呼叫是各国家都要求的电信网络的基本功能，且是语音业务；电信网络可以通过终端信令中带紧急标识或用户拨打紧急号码两种途径被识别出。 
在纯4G网络中，VoLTE的语音业务就是IMS语音呼叫，所以纯4G网络中的紧急呼叫就是指基于EPS承载的IMS紧急呼叫。 
MME在IMS紧急呼叫中的主要作用就是下发紧急呼叫号码列表、识别紧急呼叫并控制紧急承载的建立。 
##### 背景知识 
紧急呼叫是在2/3G网络语音呼叫时就存在的业务，2/3G和4G的语音呼叫存在差异，紧急呼叫上也存在差异，差异分析参见下表。 
项目|4G网络|2/3G网络
---|---|---
紧急呼叫控制|紧急呼叫业务控制在IMS网络|紧急呼叫控制在MSC
紧急呼叫承载|紧急呼叫是基于EPS承载|紧急呼叫是基于电路域承载
参与网元|UE\eNodeB\MME\SGW\PGW\PCRF\IMS\PSAP|UE\RNC\MSC\MGW\PSAP
为保障紧急呼叫的成功，需要在紧急呼叫的呼叫信令发送前建立EPS紧急承载，避免紧急呼叫信令的丢失和减少时延；同时为保障紧急呼叫语音数据包不丢失且时延小，需要为紧急呼叫建立语音EPS紧急承载。 
EPS紧急承载只能够用于紧急呼叫，不能够被其他业务使用。 
4G网络紧急呼叫承载示意图如下图所示。 
图1  紧急呼叫承载示意图
[]images/ZUF-78-12-003-%E7%B4%A7%E6%80%A5%E5%91%BC%E5%8F%AB-%E6%8F%8F%E8%BF%B0.png)
### 应用场景 
移动网络中从合法性来说可以将用户分为四类：完全合法有效用户、合法但是位置区无效的用户、有卡但不合法的用户和无卡用户。这四种用户紧急呼叫支持情况如[表2](ZUF-78-12-003-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842495__%E5%9B%9B%E7%A7%8D%E7%94%A8%E6%88%B7%E7%9A%84%E7%B4%A7%E6%80%A5%E5%91%BC%E5%8F%AB%E6%94%AF%E6%8C%81%E6%83%85%E5%86%B5-C4254481)所示。
用户类型|网络仅支持完全合法用户紧急呼叫|网络支持完全合法用户和合法但位置无效用户紧急呼叫|网络支持所有有卡用户紧急呼叫|网络支持所有用户的紧急呼叫
---|---|---|---|---
完全合法有效用户|可以进行紧急呼叫|可以进行紧急呼叫|可以进行紧急呼叫|可以进行紧急呼叫
合法但位置无效用户|不可以进行紧急呼叫|可以进行紧急呼叫|可以进行紧急呼叫|可以进行紧急呼叫
有卡但不合法用户|不可以进行紧急呼叫|不可以进行紧急呼叫|可以进行紧急呼叫|可以进行紧急呼叫
无卡用户|不可以进行紧急呼叫|不可以进行紧急呼叫|不可以进行紧急呼叫|可以进行紧急呼叫
MME根据运营商需求确定为哪些用户提供紧急呼叫业务。 
### 客户收益 
受益方|受益描述
---|---
运营商|符合国家要求：4G网络下支持为用户提供紧急呼叫功能，符合国家法律要求。
移动用户|用户享受更稳定和更可靠的网络服务：在4G网络下可进行紧急呼叫，确保生命财产安全。
### 实现原理 
##### 系统架构 
基于EPS的IMS紧急呼叫组网图如[图2](ZUF-78-12-003-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E5%9F%BA%E4%BA%8EEPS%E7%9A%84IMS%E7%B4%A7%E6%80%A5%E5%91%BC%E5%8F%AB%E7%BB%84%E7%BD%91%E5%9B%BE-C42554FD)所示。
图2  基于EPS的IMS紧急呼叫组网图
[]images/ZUF-78-12-003-%E7%B4%A7%E6%80%A5%E5%91%BC%E5%8F%AB-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%861.png)
##### 涉及的网元 
本功能需要UE、eNodeB、MME、PGW、SGW、PCRF、IMS等网元共同协作完成。 
网元名称|网元作用
---|---
UE|识别紧急呼叫，并能触发紧急呼叫。
eNodeB|为紧急呼叫提供高优先级高质量承载。
MME|识别紧急呼叫，并建立紧急承载。
PGW|识别紧急承载，保证紧急承载的高优先级。
SGW|识别紧急承载，保证紧急承载的高优先级。
PCRF|识别紧急呼叫业务，并且提供紧急业务的QoS和规则控制。
IMS|识别IMS紧急呼叫。进行紧急附着处理。路由紧急呼叫到紧急呼叫中心。
##### 业务流程 
紧急承载建立触发有两种场景： 
用户拨打紧急呼叫键，终端识别出用户是发起紧急呼叫，而当前没有附着在网络中，选择了LTE网络，则向LTE网络发起紧急附着及紧急PDN连接建立请求。MME识别紧急附着，系统支持该用户的紧急呼叫，则为用户建立紧急PDN连接，在紧急PDN连接建立后，终端通过紧急PDN的默认承载发起IMS紧急呼叫。 
用户拨打紧急呼叫键或紧急呼叫号码，终端识别出用户是发起紧急呼叫，终端已经附着在LTE网络，终端发起紧急PDN连接建立请求。MME识别是紧急PDN连接建立，则为用户建立紧急PDN连接，在紧急PDN连接建立后，终端通过紧急PDN的默认承载发起IMS紧急呼叫。 
紧急附着
紧急附着流程如下图所示。 
图3  紧急附着流程
[]images/ZUF-78-12-003-%E7%B4%A7%E6%80%A5%E5%91%BC%E5%8F%AB-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%862.png)
紧急附着流程说明如下： 
UE发起附着，其中附着类型为EPS emergency attach。 
对于合法用户，除了PDN连接建立时使用配置的紧急数据中的APN和QoS等处理外，其他处理都和非紧急呼叫相同。 
如果用户非法，MME根据运营商要求确定是否建立紧急承载。MME不进行到HSS的位置更新流程。 
无论是否紧急附着，都在Attach Accept中携带TAI对应的紧急呼叫号码列表。 
紧急PDN连接请求
紧急PDN连接请求流程如下图所示。 
图4  紧急PDN连接请求流程
[]images/ZUF-78-12-003-%E7%B4%A7%E6%80%A5%E5%91%BC%E5%8F%AB-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%863.png)
紧急PDN连接请求流程说明如下： 
UE发送PDN连接请求，请求类型是紧急。 
MME忽略请求中的APN，根据TAI解析获得SGW地址，再根据当前所在位置对应的PLMNID获取本地配置的紧急业务数据，根据配置的紧急数据进行处理。 
其他处理同非紧急PDN连接处理。 
### 系统影响 
该特性不涉及对系统的影响。 
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
相关特性|交互关系
---|---
CSFB|终端指示紧急呼叫回落到CS时，MME能够指示eNodeB是紧急呼叫的回落，并执行回落CS流程。
SRVCC|正在进行紧急呼叫时，如果用户发生4G到2/3G网络切换，能够执行SRVCC。
LCS|紧急呼叫时根据运营商要求主动触发紧急定位。
移动性限制|当用户移动到受限区域发起紧急呼叫时，MME能够根据运营商要求确定是否建立紧急承载；当用户在紧急呼叫过程中移动到受限区域时，MME能够根据运营商要求确定是否释放紧急承载。
QoS|为紧急呼叫提供运营商要求的QoS保障。
### 遵循标准 
标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".
3GPP TS 24.301: " Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS)".
### 特性能力 
规格名称|规格指标
---|---
紧急呼叫数据|MME支持为每个PLMN配置一套用于紧急呼叫数据，MME最大支持17个PLMN。
紧急呼叫号码列表|MME最大可配置50个紧急号码列表，每个列表中最大可包含10个号码，不同的TA关联不同的紧急号码列表。
### 可获得性 
##### License要求 
该特性为MME的基本特性，无需License支持。 
##### 对其他网元的要求 
紧急呼叫业务特性需要UE、eNodeB、SGW、PGW、PCRF以及IMS网元配合完成。 
##### 工程规划要求 
为紧急呼叫分配一个独立APN，该APN不被其他业务使用。 
为紧急呼叫确定一个ARP，该ARP不能够被其他业务使用。 
### O&M相关 
##### 命令 
配置项|命令
---|---
紧急呼叫配置-控制开关配置|SET EMERGENCYCFG
SHOW EMERGENCYCFG|紧急呼叫配置-控制开关配置
紧急呼叫配置-紧急数据配置|ADD EMERGDATA
SET EMERGDATA|紧急呼叫配置-紧急数据配置
DEL EMERGDATA|紧急呼叫配置-紧急数据配置
SHOW EMERGDATA|紧急呼叫配置-紧急数据配置
紧急呼叫配置-紧急号码列表配置|ADD EMERGNUMLIST
SET EMERGNUMLIST|紧急呼叫配置-紧急号码列表配置
DEL EMERGNUMLIST|紧急呼叫配置-紧急号码列表配置
SHOW EMERGNUMLIST|紧急呼叫配置-紧急号码列表配置
配置项|命令|修改的参数
---|---|---
跟踪区配置|ADD TA|紧急号码列表ID
SET TA|跟踪区配置|紧急号码列表ID
DEL TA|跟踪区配置|紧急号码列表ID
SHOW TA|跟踪区配置|紧急号码列表ID
##### 性能统计 
该特性不涉及计数器的变化。 
##### 告警和通知 
该特性不涉及告警/通知消息的变化。 
##### 业务观察/失败观察 
失败原因码及名称|处理建议
---|---
失败观察中上报“Get Emergency Data Fail”|检查“紧急呼叫配置-紧急数据配置”中是否配置了用户所在TA归属PLMN对应的紧急数据。
##### 话单与计费 
该特性不涉及话单与计费的变化。 
## 特性配置 
## 特性配置 
### 配置说明 
MME紧急呼叫功能配置，可以在MME网元实现对紧急呼叫的控制，可以基于PLMN控制是否支持紧急呼叫，可以基于TA确定携带的紧急呼叫号码列表。 
### 配置前提 
局运行正常，用户普通附着和建立PDN正常。 
### 配置过程 
执行[SET EMERGENCYCFG](../../MMESGSN\zh-CN\mml\1261660.html)命令，开启紧急呼叫功能。
执行[ADD EMERGDATA](None)命令，配置紧急APN和紧急业务相关签约数据。
执行[ADD EMERGNUMLIST](../../MMESGSN\zh-CN\mml\1261668.html)命令，增加紧急呼叫号码列表。
执行[ADD TA](../../MMESGSN\zh-CN\mml\1262200.html)命令，增加TA关联的紧急号码列表。
### 配置实例 
##### 网络支持所有用户进行紧急呼叫 
实例场景：允许所有用户进行紧急呼叫，包括“完全合法有效用户”、“合法但位置无效用户”、“有卡但不合法用户”、“无卡用户”四类用户。
配置脚本如下： 
设置紧急呼叫开关。 
命令脚本|说明
---|---
SET EMERGENCYCFG:POLICY="SPFLAG"&"SPNOCARDUSER"&"ATTACHAUTH"&"PAUTHFAIL"&"PLIMITUSER";|打开紧急呼叫开关，设置允许“完全合法有效用户”、“合法但位置无效用户”、“有卡但不合法用户”、“无卡用户”四类用户进行紧急呼叫。
配置紧急数据。 
命令脚本|说明
---|---
ADD EMERGDATA:PLMN="460"-"01",APN="emergency",APNAMBR4UL="256Mbps",APNAMBR4DL="256 Mbps",QCI=8,PRIOLEVEL="PRIO14",PC="NO",PV="NO",IPADDR="192.20.102.196"|配置紧急APN和紧急业务相关数据，包括ARP、QCI、PGW地址等。
配置紧急号码列表。 
命令脚本|说明
---|---
ADD EMERGNUMLIST:LISTID=1,NUMBER="110",TYPE="PC"|配置报警中心紧急号码为110。
引用紧急号码列表。 
命令脚本|说明
---|---
SET TA:TAID=1,LISTID=1|在TA编号为1的TA中引用紧急号码列表。
##### 网络支持所有有卡用户紧急呼叫 
实例场景：允许“完全合法有效用户”、“合法但位置无效用户”、“有卡但不合法用户”进行紧急呼叫。
配置脚本如下： 
设置紧急呼叫开关。 
命令脚本|说明
---|---
SET EMERGENCYCFG:POLICY="SPFLAG"&"ATTACHAUTH"&"PAUTHFAIL"&"PLIMITUSER"|打开紧急呼叫开关，设置允许“完全合法有效用户”、“合法但位置无效用户”、“有卡但不合法用户”进行紧急呼叫。
配置紧急数据。 
命令脚本|说明
---|---
ADD EMERGDATA:PLMN="460"-"01",APN="emergency",APNAMBR4UL="256Mbps",APNAMBR4DL="256 Mbps",QCI=8,PRIOLEVEL="PRIO14",PC="NO",PV="NO",IPADDR="192.20.102.196"|配置紧急APN和紧急业务相关数据，包括ARP、QCI、PGW地址等。
配置紧急号码列表。 
命令脚本|说明
---|---
ADD EMERGNUMLIST:LISTID=1,NUMBER="110",TYPE="PC"|配置报警中心紧急号码为110。
引用紧急号码列表。 
命令脚本|说明
---|---
SET TA:TAID=1,LISTID=1|在TA编号为1的TA中引用紧急号码列表。
##### 网络支持完全合法用户和合法但位置无效用户紧急呼叫 
实例场景：允许“完全合法有效用户”、“合法但位置无效用户”进行紧急呼叫。
配置脚本如下： 
设置紧急呼叫开关。 
命令脚本|说明
---|---
SET EMERGENCYCFG:POLICY="SPFLAG"&"ATTACHAUTH"&"PLIMITUSER"|设置允许“完全合法有效用户”、“合法但位置无效用户”进行紧急呼叫。
配置紧急数据。 
命令脚本|说明
---|---
ADD EMERGDATA:PLMN="460"-"01",APN="emergency",APNAMBR4UL="256Mbps",APNAMBR4DL="256 Mbps",QCI=8,PRIOLEVEL="PRIO14",PC="NO",PV="NO",IPADDR="192.20.102.196"|配置紧急APN和紧急业务相关数据，包括ARP、QCI、PGW地址等。
配置紧急号码列表。 
命令脚本|说明
---|---
ADD EMERGNUMLIST:LISTID=1,NUMBER="110",TYPE="PC"|配置报警中心紧急号码为110。
引用紧急号码列表。 
命令脚本|说明
---|---
SET TA:TAID=1,LISTID=1|在TA编号为1的TA中引用紧急号码列表。
##### 网络仅支持完全合法用户紧急呼叫 
实例场景：允许“完全合法有效用户”进行紧急呼叫。
配置脚本如下： 
设置紧急呼叫开关。 
命令脚本|说明
---|---
SET EMERGENCYCFG:POLICY="SPFLAG"&"ATTACHAUTH"|设置允许“完全合法有效用户”进行紧急呼叫。
配置紧急数据。 
命令脚本|说明
---|---
ADD EMERGDATA:PLMN="460"-"01",APN="emergency",APNAMBR4UL="256Mbps",APNAMBR4DL="256 Mbps",QCI=8,PRIOLEVEL="PRIO14",PC="NO",PV="NO",IPADDR="192.20.102.196"|配置紧急APN和紧急业务相关数据，包括ARP、QCI、PGW地址等。
配置紧急号码列表。 
命令脚本|说明
---|---
ADD EMERGNUMLIST:LISTID=1,NUMBER="110",TYPE="PC"|配置报警中心紧急号码为110。
引用紧急号码列表。 
命令脚本|说明
---|---
SET TA:TAID=1,LISTID=1|在TA编号为1的TA中引用紧急号码列表。
### 测试用例 
##### 完全合法有效用户紧急呼叫 
测试项目|完全合法有效用户紧急呼叫
测试目的|测试完全合法有效用户紧急呼叫业务正常
预置条件|用户普通IMS语音业务正常
测试过程|用户普通附着后，激活紧急PDN。用户发起IMS紧急呼叫。
通过准则|IMS紧急呼叫正常
测试结果|–
##### 无卡用户紧急呼叫 
测试项目|无卡用户紧急呼叫
测试目的|无卡用户建立紧急呼叫正常
预置条件|手机不插USIM卡
测试过程|用户紧急附着，建立紧急承载。用户发起IMS紧急呼叫。
通过准则|IMS紧急呼叫正常
测试结果|–
##### 未鉴权用户紧急呼叫 
测试项目|未鉴权用户紧急呼叫
测试目的|未鉴权用户建立紧急呼叫正常
预置条件|用户在MME鉴权失败
测试过程|用户紧急附着，鉴权失败，MME放行后建立紧急承载。用户发起IMS紧急呼叫。
通过准则|IMS紧急呼叫正常
测试结果|–
### 常见问题处理 
无。 
# ZUF-78-12-004 CSFB 
## 特性描述 
## 特性描述 
### 描述 
##### 定义 
CSFB是指CS语音回落，用于在LTE和2G/3G网络共同覆盖的区域内，对于不支持IMS业务的终端回落到2G/3G网络使用CS域进行语音业务，同时保持数据业务连续性的功能。
为实现CSFB业务，MME需要与MSC/VLR之间使用SGs口连接，完成用户在CS域的位置更新、注册、寻呼和短消息业务。
##### 背景知识 
VoLTE即基于LTE承载的IMS语音。对运营商而言，部署VoLTE意味着开启了向移动宽带语音演进之路。从长远来看，这将给运营商带来两方面的价值，一方面是提升无线频谱利用率、降低网络成本。另一方面是提升用户体验，VoLTE的体验明显优于传统CS语音。
但是，由于现阶段LTE覆盖比较有限，运营商需要利用传统CS覆盖的广度和深度来提供无缝的语音业务，即LTE与CS的互操作，其中有两个主要技术点： 
LTE用户漫游到CS域后的业务提供方式，有两种可选方案，一种是完全由MSC处理语音业务，即CSFB；另一种是通过MSC接入IMS域以提供语音业务，就是ICS架构。 
通话中的LTE到CS的切换，3GPP为此定义了SRVCC技术。 
第一个技术点即CSFB，即本文档主要描述的内容。 
第二个技术点即为SRVCC，参见ZUF-78-12-005 SRVCC
。
### 应用场景 
CSFB的应用场景要求LTE网络与2/3G网络相同覆盖。MME与MSC间使用的SGs口（承载于SCTP偶联上）相连。
MME与MSC之间的组网，有多种形式。根据MME是否与UE回落后的服务MSC相连，分为Proxy方式和直连方式；这两种方式从MSC升级方式、MSC选择方式、回落时延等方面都有较大的差别，具体比较参见[表1](ZUF-78-12-004-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842495__MME-MSC%E7%BB%84%E7%BD%91%E7%9B%B4%E8%BF%9E%E6%96%B9%E5%BC%8F%E6%AF%94%E8%BE%83-D9528633)。
组网方式|MSC升级方式|MSC选择方式|回落时延
---|---|---|---
Proxy MSC方式|无需全网MSC升级，只需要新增一对支持CSFB的MSC。|SGs口位置更新时选择ProxyMSC，UE位置变化无需发起SGs口位置更新。.|回落后UE需要向MSC发起位置更新，回落时延大。
直连组网方式|需要全网MSC升级支持CSFB。|SGs口位置更新时选择和TA同覆盖的LA的MSC，LAI变化时UE需要发起SGs口位置更新。|回落后UE无需向MSC发起位置更新，回落时延小。
Proxy MSC负荷分担组网方式图1  ZUF-78-12-004-Proxy MSC负荷分担组网图 
直连组网方式图2  ZUF-78-12-004-直连组网方式组网图 
MSC的容灾方式，分为无容灾、主备和负荷分担三种，在主备和负荷分担方式时，MME需要打开65579
 （支持POOL组网的Gs接口）功能开关。
MSC容灾方式|LAI归属及备份方式|MSC选择方式
---|---|---
无容灾方式|一个LAI归属一个MSC。|LAI归属的MSC状态正常，MME选择此MSC；如此MSC宕机，MME无MSC可选；
主备方式|一个LAI归属一个主用MSC；一个MSC宕机，可由备用MSC接管。|LAI归属的主用MSC状态正常，MME选择主用MSC；主用MSC宕机，MME选择备用MSC。
负荷分担方式|一个LAI归属POOL内的所有MSC，其中MSC可具有不同的能力，分配的用户数不同；MSC宕机，可由POOL内其他MSC接管。|MME根据LAI归属的POOL内各个MSC的权重选择MSC；一旦有MSC宕机，MME将在可用的MSC中按权重选择。
下面列举了三种常见的组网形式： 
无容灾方式图3  ZUF-78-12-004-无容灾方式组网图 
主备组网方式图4  ZUF-78-12-004-主备组网方式组网图 
负荷分担方式（MSC POOL 组网）负荷分担的MSC基于各自的处理能力，分配不同数量的用户。图5  ZUF-56–12–004–负荷分担方式组网图 
另一方面，如果LTE用户归属于不同的2/3G网络，在回落时，处于同一区域的UE，需要选择各自归属的2/3G网络；MME根据UE的NRI、IMSI，选择其归属的MSC网络。而归属的MSC网络，其组网也可能是上述的三种模式中的一种。以负荷分担方式为例：
图6  ZUF-78-12-004-多PLMN直连负荷分担方式组网图
[]images/ZUF-78-12-004-%E5%A4%9APLMN%E7%9B%B4%E8%BF%9E%E8%B4%9F%E8%8D%B7%E5%88%86%E6%8B%85%E6%96%B9%E5%BC%8F%E7%BB%84%E7%BD%91%E5%9B%BE.png)
### 客户收益 
收益者|收益描述
---|---
运营商|通过CSFB功能，让LTE网络的用户回落到2/3G完成语音业务。
移动用户|用户在LTE网络进行高速数据业务，同时可拨打或接听语音呼叫。
### 实现原理 
##### 各网元作用 
EPS网络中CSFB组网如下：
图7  ZUF-78-12-004-CSFB组网图
[]images/ZUF-78-12-004-CSFB%E7%BB%84%E7%BD%91%E5%9B%BE.png)
##### 涉及的网元 
CSFB功能涉及eNodeB、MME、MSC/VLR和HSS网元。
网元|作用
---|---
eNodeB|为UE终端提供无线资源，完成对用户的寻呼，以及指示UE终端选择回到CS域中的小区。
MME|完成用户的注册、承载建立和用户的位置更新，当UE终端进行联合附着或联合TAU业务时，发送位置更新消息通知MSC/VLR，并将MSC/VLR分配的TMSI透传给UE终端。
MSC/VLR|接收MME发送的位置更新消息，完成用户在CS域位置更新、注册以及发起对UE的语音终呼和短消息业务。
HSS|主要完成用户的签约数据插入和管理。
##### 本网元实现 
VLR局向选择流程： 
根据用户的IMSI号段和TAI选择MSC POOL，如[图8](ZUF-78-12-004-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__ZUF-78-12-004-VLR%E5%B1%80%E5%90%91%E9%80%89%E6%8B%A9%E6%B5%81%E7%A8%8B1-DA21FD2C)所示，选中MSC POOL1：
图8  ZUF-78-12-004-VLR局向选择流程 1
[]images/ZUF-78-12-004-VLR%E5%B1%80%E5%90%91%E9%80%89%E6%8B%A9%E6%B5%81%E7%A8%8B%201.png)
在同一个POOL内，根据优先级顺序，选择最高优先级的一组VLR，如[图9](ZUF-78-12-004-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__ZUF-78-12-004-VLR%E5%B1%80%E5%90%91%E9%80%89%E6%8B%A9%E6%B5%81%E7%A8%8B2-DA2235F6)所示，选中VLR11和VLR12：
图9  ZUF-78-12-004-VLR局向选择流程 2
[]images/ZUF-78-12-004-VLR%E5%B1%80%E5%90%91%E9%80%89%E6%8B%A9%E6%B5%81%E7%A8%8B%202.png)
在该优先级的这一组VLR中，按下面的顺序进行VLR选择： 
UE携带NRI对应的VLR。 
IMSI后三位值归属的VLR。 
MM上下文保存的VLR。 
如果上述VLR均不可用，则在可用VLR中，根据权重选择。 
如果该优先级中没有可用的VLR，回到第二步，选择下一优先级的一组VLR，依次类推，如[图10](ZUF-78-12-004-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__ZUF-78-12-004-VLR%E5%B1%80%E5%90%91%E9%80%89%E6%8B%A9%E6%B5%81%E7%A8%8B3-DA227B4A)所示，选中VLR11和VLR12：
图10  ZUF-78-12-004-VLR局向选择流程 3
[]images/ZUF-78-12-004-VLR%E5%B1%80%E5%90%91%E9%80%89%E6%8B%A9%E6%B5%81%E7%A8%8B%203.png)
##### 业务流程 
联合附着
图11  ZUF-78-12-004-联合附着流程
[]images/ZUF-78-12-004-%E8%81%94%E5%90%88%E9%99%84%E7%9D%80%E6%B5%81%E7%A8%8B.png)
UE通过eNodeB发送联合附着消息到MME。 
MME根据3GPP 23.401协议的附着流程继续附着流程，直到接收SGW创建会话响应。
MME根据消息中TAI，以及用户的IMSI，查询本地配置，获取映射的LAI，基于LAI得到LAI归属的MSC POOL，再根据POOL内各个MSC/VLR的优先级和权重以及NRI、IMSI得到MSC/VLR局向ID。
MME确定MSC局向ID后，按照路由组——路由——链路的层级关系，选择可用的SGs链路，向此局向发送位置更新消息。 
MME和MSC/VLR建立SGs接口关联。 
MSC/VLR完成CS域的位置更新流程。 
MSC/VLR发送位置更新响应消息给MME，携带位置更新结果以及为用户分配的TMSI。 
MME继续完成后续的附着流程。 
联合TAU
图12  ZUF-78-12-004-联合TAU流程
[]images/ZUF-78-12-004-%E8%81%94%E5%90%88TAU%E6%B5%81%E7%A8%8B.png)
UE识别判断需要执行TAU流程。 
UE通过eNodeB发送联合TAU消息到MME。 
MME根据3GPP 23.401协议进行TAU业务处理，从Old MME获得用户的上下文，在新的SGW完成承载建立。 
MME根据消息中TAI，以及用户的IMSI，查询本地配置，获取映射的LAI，基于LAI得到LAI归属的MSC POOL，最后再根据POOL内各个MSC/VLR的优先级和权重以及NRI、IMSI，得到MSC/VLR局向ID。MME确定MSC局向ID后，按照路由组——路由——链路的层级关系，选择可用的SGs链路，向此局向发送位置更新消息，如MSC局向发送变化，MME与新的MSC建立SGs关联。 
MSC/VLR完成CS域的位置更新流程。 
MSC/VLR发送位置更新响应消息给MME，携带位置更新结果以及为用户分配的TMSI。 
MME向UE返回TAU Accept消息。 
UE向MME返回TAU Complete。 
分离流程
UE发起的分离过程
图13  ZUF-78-12-004-UE发起的分离流程
[]images/ZUF-78-12-004-UE%E5%8F%91%E8%B5%B7%E7%9A%84%E5%88%86%E7%A6%BB%E6%B5%81%E7%A8%8B.png)
MME收到了UE发送的Detach Request (Detach Type) 消息，Detach Type 指出执行分离类型为IMSI
Detach 或者combined EPS and IMSI Detach。 
Step2到Step10参见 3GPP23.401的UE发起的分离过程。 
MME发送IMSI Detach Indication (IMSI) 消息到MSC/VLR。 
MME和MSC/VLR删除SGs关联。 
MME向UE发送Detach Accept消息。 
MME继续后续的分离流程。 
MME发起的分离过程
图14  ZUF-78-12-004-MME发起的分离流程
[]images/ZUF-78-12-004-MME%E5%8F%91%E8%B5%B7%E7%9A%84%E5%88%86%E7%A6%BB%E6%B5%81%E7%A8%8B.png)
MME执行网络侧发起的Detach procedure，参见TS23.401协议。 
MME发送IMSI Detach Indication (IMSI) 消息到VLR。 
MME和MSC/VLR删除用户的SGs口关联。 
HSS发起的分离过程
图15  ZUF-78-12-004-HSS发起的分离流程
[]images/ZUF-78-12-004-HSS%E5%8F%91%E8%B5%B7%E7%9A%84%E5%88%86%E7%A6%BB%E6%B5%81%E7%A8%8B.png)
MME执行HSS发起的Detach procedure，参见TS23.401协议。 
MME在向UE发送了Detach Request之后，如果建立SGs口关联MME发送IMSI Detach Indication
(IMSI) 消息到VLR。 
MME和MSC/VLR删除用户的SGs口关联。 
UE作为主叫流程
UE的主叫流程按照用户的状态可分为以下部分。 
连接态基于HO的主叫过程
图16  ZUF-78-12-004-基于HO的MO-CALL流程
[]images/ZUF-78-12-004-%E5%9F%BA%E4%BA%8EHO%E7%9A%84MO-CALL%E6%B5%81%E7%A8%8B.png)
MME收到了UE发送的Extended Service Request，Service Type指示为MO-CSFB，通知MME
UE希望进行CSFB，MME执行UE发起的Extended Service Request功能需求。MME收到Extended Service Request消息后，如果该VLR局向配置“支持发送MO CSFB Indication消息”，MME向MSC发送MO CSFB Indication消息。 
MME发送S1‑AP Request message（UE CONTEXT MODIFICATION REQUEST消息，携带CS
Fallback Indicator)到eNodeB包含CSFB指示，eNodeB收到此消息后，指示UE接入到UTRAN/GREAN中。 
UE支持数据业务的切换，通过eNodeB向MME发送Handover Required消息，MME执行PS Handover流程。 
UE从BSC或RNC发送Cm Service Request消息到MSC。 
CS域呼叫建立。 
MME继续完成PS Handover流程。 
连接态基于非HO的主叫过程
图17  ZUF-78-12-004-基于非HO的MO-CALL流程
[]images/ZUF-78-12-004-%E5%9F%BA%E4%BA%8E%E9%9D%9EHO%E7%9A%84MO-CALL%E6%B5%81%E7%A8%8B.png)
MME收到了UE发送的Extended Service Request，Service Type指示为MO-CSFB，通知MME
UE希望进行CSFB，MME执行UE发起的Extended Service Request功能需求。MME收到Extended Service Request消息后，如果该VLR局向配置“支持发送MO CSFB Indication消息”，MME向MSC发送MO CSFB Indication消息。 
MME发送S1‑AP Request message（INITIAL CONTEXT SETUP REQUEST或者UE
CONTEXT MODIFICATION REQUEST消息，携带CS Fallback Indicator)到eNodeB包含CSFB指示。eNodeB收到此消息后，指示UE接入到UTRAN/GREAN中。 
MME收到eNodeb发送的UE Context Release Request (Cause)，Cause指出UE的PS业务不可用（UE
Not Available For PS Service）。 
MME释放S1口的UE 上下文，释放S1AP连接。 
UE在CS域进行位置更新或者进行联合位置更新。 
UE发起挂起流程。 
MME收到了SGSN发送Suspend Request消息。 
MME发送Suspend Notification消息给S-GW，通知S-GW丢弃收到的下行报文。 
UE在CS域进行呼叫业务。 
非连接态的主叫过程
非连接态的主叫过程参考[连接态基于HO的被叫过程](ZUF-78-12-004-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E8%BF%9E%E6%8E%A5%E6%80%81%E5%9F%BA%E4%BA%8EHO%E7%9A%84%E8%A2%AB%E5%8F%AB%E8%BF%87%E7%A8%8B-DC41C020)和[连接态基于非HO的被叫过程](ZUF-78-12-004-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E8%BF%9E%E6%8E%A5%E6%80%81%E5%9F%BA%E4%BA%8E%E9%9D%9EHO%E7%9A%84%E8%A2%AB%E5%8F%AB%E8%BF%87%E7%A8%8B-DC41C401)连接态的过程，仅仅需要使用S1-AP Initial UE Context Request
and Response来代替S1-AP UE Context Modification Request and Response即可。
UE作为被叫流程
连接态基于HO的被叫过程
图18  ZUF-78-12-004-基于HO的被叫流程
[]images/ZUF-78-12-004-%E5%9F%BA%E4%BA%8EHO%E7%9A%84%E8%A2%AB%E5%8F%AB%E6%B5%81%E7%A8%8B.png)
MME收到了MSC通过SGs口发送Paging Request (IMSI, VLR TMSI, Location Information)消息，发送CS业务通知消息到UE；MME通过SGs口发送Service
Request消息给MSC，通知MSC停止发送寻呼。 
MME收到了UE发送的Extended Service Request消息，Service Type指示为MT-CSFB并且携带
CS Fallback Response为成功，MME执行UE发起的Extended Service Request流程，如果是拒绝，那么MME通过SGs口发送CS
寻呼拒绝消息给MSC，通知MSC CSFB业务失败，流程结束。 
MME发送UE CONTEXT MODIFICATION REQUEST (携带CS Fallback Indicator)
到eNodeB，eNodeB收到此消息后，指示UE接入到UTRAN/GREAN中。 
UE支持数据业务的切换，通过eNodeB向MME发送Handover Required消息，MME执行PS Handover流程。 
用户返回寻呼响应到MSC/VLR。 
用户在CS域进行呼叫业务。 
用户继续后续的HO流程。 
连接态基于非HO的被叫过程
图19  ZUF-78-12-004-连接态基于非HO的被叫过程
[]images/ZUF-78-12-004-%E8%BF%9E%E6%8E%A5%E6%80%81%E5%9F%BA%E4%BA%8E%E9%9D%9EHO%E7%9A%84%E8%A2%AB%E5%8F%AB%E8%BF%87%E7%A8%8B.png)
MME收到了MSC通过SGs口发送Paging Request (IMSI, VLR TMSI, Location Information)消息，发送CS业务通知消息到UE；MME通过SGs口发送Service
Request消息给MSC，通知MSC停止发寻呼。 
MME收到了UE发送的Extended Service Request消息，Service Type指示为MT-CSFB并且
携带 CS Fallback Response为成功，MME执行UE发起的Extended Service Request流程，如果是拒绝，那么MME通过SGs口发送CS
寻呼拒绝消息给MSC，通知MSC CSFB业务失败，流程结束。 
MME发送UE CONTEXT MODIFICATION REQUEST (携带CS Fallback Indicator)到eNodeB，eNodeB收到此消息后，指示UE接入到UTRAN/GREAN中。 
后续流程同基于非HO的主叫过程。 
非连接态的被叫过程
寻呼的过程如[图20](ZUF-78-12-004-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__ZUF-78-12-004-%E9%9D%9E%E8%BF%9E%E6%8E%A5%E6%80%81%E7%9A%84%E8%A2%AB%E5%8F%AB%E8%BF%87%E7%A8%8B-DA27CF51)所示。
图20  ZUF-78-12-004-非连接态的被叫过程
[]images/ZUF-78-12-004-%E9%9D%9E%E8%BF%9E%E6%8E%A5%E6%80%81%E7%9A%84%E8%A2%AB%E5%8F%AB%E8%BF%87%E7%A8%8B.png)
GMSC收到IAM消息。
GMSC通过SRI从HSS得到MSC/VLR的地址。
GMSC发送IAM消息到MSC/VLR。 
MSC/VLR向MME发送寻呼消息。 
MME向eNodeB寻呼用户。 
eNodeB寻呼UE。 
MME收到了UE发起的业务请求，为用户建立S1信令连接。 
Idle状态下的MO-SMS
图21  ZUF-78-12-004-Idle状态下的MO-SMS
[]images/ZUF-78-12-004-Idle%E7%8A%B6%E6%80%81%E4%B8%8B%E7%9A%84MO-SMS.png)
UE联合附着。 
MME收到了UE发起的业务请求，为用户建立S1信令连接。 
MME收到了UE构造SMS的UPLINK NAS TRANSPORT消息。
MME通过SGs口发送Uplink Unit data消息到MSC/VLR并携带短消息内容。为了MSC产生计费话单，在消息中携带IMEISV、time zone、Mobile
Station Classmark2、current TAI和E‑CGI 等内容。
MSC将短消息投递给短消息中心。 
MME收到了MSC/VLR发送Downlink Unit data消息到作为收到SMS的确认。 
MME发送DOWNLINK NAS TRANSPORT消息到UE。 
短消息中心返回投递报告。 
MME收到 MSC/VLR发送Downlink Unit data消息表示已经把SMS发送成功。 
MME把从MSC/VLR收到的消息通过DOWNLINK NAS TRANSPORT消息发送到UE。 
MME收到了UE作为确认投递结果的UPLINK NAS TRANSPORT消息。 
MME转发Uplink Unit data消息到MSC/VLR。 
MSC/VLR通知MME没有后续消息要被传输，发送Release Request消息到MME。 
Idle状态下的MT-SMS
图22  ZUF-78-12-004-Idle状态下的MT-SMS流程
[]images/ZUF-78-12-004-Idle%E7%8A%B6%E6%80%81%E4%B8%8B%E7%9A%84MT-SMS%E6%B5%81%E7%A8%8B.png)
UE联合附着。 
短消息中心下发短消息。 
SMS-GMSC查询HLR/HSS获取MSC/VLR地址。
SMS-GMSC将短消息投递给MSC/VLR。 
MME收到MSC/VLR发送Paging (IMSI, VLR TMSI, Location Information,
SMS indicator) 消息。 
MME在S1接口发送寻呼消息，发起对UE的寻呼。 
eNodeB寻呼用户。 
MME收到了UE发送Service Request消息。MME发送Initial Context Setup Request
消息到eNodeB 建立无线承载，处理业务请求。 
业务请求流程成功之后，MME发送Service Request消息到MSC，为了让MSC产生计费话单的需要，MME在消息中携带IMEISV、time
zone、the Mobile Station Classmark2、current TAI和E‑CGI。 
MME收到了MSC/VLR发送的Downlink Unit data消息，携带MT-SMS内容；MME发送DOWNLINK
NAS TRANSPORT消息到eNodeB，携带短消息内容，eNodeB发送给UE。 
MME收到了UE通过UPLINK NAS TRANSPORT发送的确认消息，通过SGs口发送Uplink Unit data消息到MSC/VLR。 
MME收到UE通过UPLINK NAS TRANSPORT消息发送MT-SMS接收报告， MME通过Uplink Unit
data 转发接收报告到MSC/VLR。 
MSC/VLR将接收报告通过SMS-GMSC发送给短消息中心。 
MME收到了MSC/VLR发送的Downlink Unit data消息，作为收到SMS的接收报告的确认，通过DOWNLINK
NAS TRANSPORT消息传输到UE。 
MME收到MSC发送Release Request消息，指示没有消息需要发送了。 
### 系统影响 
UE由于需要进行CS语音业务而触发的CS域回落，会同时伴随有跨RAT的更新和切换；一定程度上会增加UE的业务负荷。UE原有的话务模型需要做相应的增加。
MSC/VLR通过MME寻呼用户，对MME的负荷有一定的影响。
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
该特性不涉及与其他特性的交互。 
### 遵循标准 
标准类别|标准名称|章节
---|---|---
3GPP|3GPP TS 23.401|General Packet Radio Service (GPRS) enhancements for EvolvedUniversal Terrestrial Radio Access Network (E-UTRAN) access .
3GPP|3GPP TS 23.272|Circuit Switched (CS) fallback in Evolved Packet System (EPS).
3GPP|3GPP TS 29.118|Mobility Management Entity (MME) –Visitor Location Register(VLR) SGs interface specification .
3GPP|3GPPTS36.413|S1 Application Protocol (S1AP).
3GPP|3GPPTS24.301|Non-Access-Stratum (NAS) protocol for Evolved Packet System(EPS); Stage 3.
### 特性能力 
规格|指标
---|---
MSC POOL|系统最大支持1024个MSC POOL，每个POOL最大支持32个MSC/VLR局向。
SGs局向路由组|系统最大支持255个SGs局向路由组，一个SGs局向路由组中最多配置8个SGs路由，其中路由可配置为N+M主备或负荷分担关系。一个MSC/VLR局向最多有4个SGs局向路由组，其中第一个为主用局向路由，其他为备份局向路由，优先级依次递减。
SGs局向路由|一个SGs局向路由中最多配置8个SGs连接，其中路由可配置为N+M主备或负荷分担关系。
SGs连接|系统最大支持2047个SGs连接。
### 可获得性 
##### 版本要求及变更记录 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
##### License要求 
该特性为ZXUN uMAC的基本特性，无需License支持。
##### 工程规划要求 
MSC/VLR组网规划：需要规划好MSC/VLR的组网形式，包括负荷分担、主备等。 
跟踪区和位置区规划：需要根据组网和无线覆盖，规划好TA和LA的对应关系，以及MSC/VLR对LA的管辖关系。 
SGs口对接参数规划：需要规划好对接的SCTP偶联相关参数，包括偶联地址、端口号等。需要规划好SGs口使用的VLR Name和MME Name。 
##### 对其他网元的要求 
UE|MME|eNodeB|MSC
---|---|---|---
-|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
需要eNodeB支持CSFB功能、MSC支持SGs接口功能。 
### O&M相关 
##### 命令 
配置项表2  新增配置项配置项命令SGs口开关配置SET SGSFLAGSGs偶联配置ADD SCTPSGs连接配置ADD SGSCONNSGs路由配置ADD SGS ROUTESGs路由组配置ADD SGS ROUTE GROUPSGs局向路由组配置ADD SGS OFFICE ROUTE GROUPSGs口VLR局向配置ADD VLROFFICESGs口VLR POOL配置ADD VLRPOOLVLR POOL NRI长度配置ADD POOLNRL LENPOOL内VLR NRI值配置ADD POOL VRLNRI位置区配置ADD LAI跟踪区配置ADD TA基于IMSI和TAI映射LAI配置ADD IMSITAITOLAI移动号码分析ADD MDNALSGs口选择VLR POOL配置ADD LAIVLRPOOLGs口MSC/VLR分担配置ADD MSCVLR 
安全变量该特性不涉及安全变量的变化。 
定时器该特性不涉及定时器的变化。 
软参表3  新增软件参数软件参数ID软件参数名称786860当配置为VLR Pool时，MME根据IMSI选择VLR的方式262368支持对等PLMN列表包含LAI的PLMN262387是否支持VLR局向状态告警上报65678支持根据NRI选择VLR262433接收SGs寻呼是否更新VLR局向号262439清除SGS口是否通知VLR262263TAU(Combined TA/LA updating类型)流程中是否更新VLR262273TAU失败时通知VLR的分离类型262332IMSI改变是否清除VLR信息262378SUSPEND态联合TAU强制更新VLR262401VLR重启后MME触发IMSI分离需要通知VLR524296支持根据VLR查找NSE接口优化 
动态管理该特性不涉及动态管理的变化。 
##### 性能统计 
CSFB消息测量
CSFB测量，用于测量CSFB回落的请求次数以及不同回落方式下的回落的成功率和建立时长，同时还包括发送和接收SMS的请求和成功次数测量 
测量类型|描述
---|---
CSFB测量|编号为43015开头的所有计数器
性能计数器名称
---
C432080003 CSFB MO试呼次数
C432080004 CSFB MT试呼次数
C432080005 CSFB紧急呼叫试呼次数
C432080006 CSFB 寻呼次数
C432080007 CSFB 电路域服务通知次数
MME SGs口相关测量
SGs口消息测量，用于测量发送和接收的各种SGs口消息的数目。 
测量类型|描述
---|---
SGs口消息测量|编号为43203开头的所有计数器
SGs接口负荷控制测量|编号为43303开头的所有计数器
MME SGs口VLR局向测量
用于SGs口VLR局向相关测量。 
测量类型|描述
---|---
联合附着分VLR局向测量|编号为46100开头的所有计数器
联合跟踪区更新分VLR局向测量|编号为46101开头的所有计数器
SGs口寻呼分VLR局向测量|编号为46102开头的所有计数器
基于VLR局向用户数测量|编号为46104开头的所有计数器
##### 告警和通知 
告警和通知
---
2114322676 SGs口VLR局向不可达
2114322675 SGs路由组不可用
##### 业务观察/失败观察 
该特性不涉及业务观察/失败观察的变化。 
##### 话单与计费 
该特性不涉及话单与计费的变化。 
## 特性配置 
## 特性配置 
### 配置说明 
本节用于描述如何配置CSFB。
### 配置前提 
eNodeB和MSC支持CSFB功能。 
MME License支持CSFB功能。 
### 配置过程 
使用命令[SET SGSFLAG](../../MMESGSN\zh-CN\mml\1260253.html)设置支持SGs口。
使用命令[ADD SCTP](../../Commons_SIG\zh-cn\mml\1251000.html)配置SGs口偶联。
使用命令[ADD SGSCONN](../../MMESGSN\zh-CN\mml\1262118.html)配置SGs口连接。
使用命令[ADD SGS ROUTE](../../MMESGSN\zh-CN\mml\1262173.html)配置SGs口路由
使用命令[ADD SGS ROUTE GROUP](../../MMESGSN\zh-CN\mml\1262169.html)配置SGs口路由组。
使用命令[ADD SGS OFFICE ROUTE GROUP](../../MMESGSN\zh-CN\mml\1262165.html)配置SGs局向路由组。
使用命令[ADD VLROFFICE](../../MMESGSN\zh-CN\mml\1261261.html)配置VLR局向。
使用命令[ADD VLRPOOL](../../MMESGSN\zh-CN\mml\1261267.html)配置SGS口VLRPOOL。
使用命令[ADD POOLNRL LEN](../../MMESGSN\zh-CN\mml\1261835.html)配置VLR POOL NRI的长度
使用命令[ADD POOL VRLNRI](../../MMESGSN\zh-CN\mml\1261840.html)配置POOL内VLR NRI值
使用命令[ADD LAI](../../MMESGSN\zh-CN\mml\1262230.html)配置位置区。
使用命令[ADD TA](../../MMESGSN\zh-CN\mml\1262200.html)配置跟踪区。
使用命令[ADD MSCVLR](../../MMESGSN\zh-CN\mml\1262250.html)配置VLR分担。
使用命令[ADD IMSITAITOLAI](../../MMESGSN\zh-CN\mml\1261756.html)配置IMSI和TA映射LAI配置。
使用命令[ADD MDNAL](../../MMESGSN\zh-CN\mml\1261015.html)配置移动号码分析。
使用命令[ADD LAIVLRPOOL](../../MMESGSN\zh-CN\mml\1261272.html)配置SGS选择VLRPOOL配置。
### 配置实例 
##### 无容灾方式组网 
实例场景1: 某局点采用无容灾组网方式
某局点采用Proxy MSC的方式进行负荷分担组网，组网如[图1](ZUF-78-12-004-14-%E7%89%B9%E6%80%A7%E9%85%8D%E7%BD%AE.html#T_20175108424919__ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E9%87%87%E7%94%A8%E6%97%A0%E5%AE%B9%E7%81%BE%E7%BB%84%E7%BD%91%E6%96%B9%E5%BC%8F-DAD053FF)所示。
图1  ZUF-78-12-004-某局点采用无容灾组网方式
[]images/ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E9%87%87%E7%94%A8%E6%97%A0%E5%AE%B9%E7%81%BE%E7%BB%84%E7%BD%91%E6%96%B9%E5%BC%8F.png)
配置说明
数据规划配置请参考下表。 
参数|MME1|MSC1|MSC2
---|---|---|---
偶联IP|131.1.17.159|SCTP1：40.40.1.1|SCTP2：40.40.2.1
偶联端口号|6001|6001|6001
LAI|46001-0110|46001-0110|46001-0110
TAI|46001-0110|-|-
VLRPOOL|-|POOL1级别1|POOL1级别1
配置步骤
步骤|解释说明|命令脚本
---|---|---
1|设置MME支持SGs口。|SET SGSFLAG:SGSFLAG="YES"
2|增加SGs偶联。|增加MME与MSC1之间的SGs偶联连接SCTP1。ADD SCTP:ID=110,NAME="MSCSCTP110",LOCPORT=6001,REMPORT=6001,VPNID1=2,LOCADDR1="131.1.17.159",REMADDR1="40.40.1.1",ROLE="CLT",PROTOCALTYPE="SGS"增加MME与MSC2之间的SGs偶联连接SCTP2。ADD SCTP:ID=120,NAME="MSCSCTP120",LOCPORT=6001,REMPORT=6001,VPNID1=2,LOCADDR1="131.1.17.159",REMADDR1="40.40.2.1",ROLE="CLT",PROTOCALTYPE="SGS"
3|增加SGs连接。|增加到MSC1的SGs连接110。ADD SGSCONN:ID=110,SCTPID=110,NAME="sgslink110"增加到MSC2的SGs连接120。ADD SGSCONN:ID=120,SCTPID=120,NAME="sgslink120"
4|增加SGs路由配置。|增加到MSC1的SGs路由配置，包括SGs连接110。ADD SGS ROUTE:ROUTEID=110,PARTAKEMODE="PARTAKE",CONNECTION=110增加到MSC2的SGs路由配置 ，包括SGs连接120。ADD SGS ROUTE:ROUTEID=120,PARTAKEMODE="PARTAKE",CONNECTION=120
5|增加SGs路由组配置。|增加到MSC1的SGs路由组配置。ADD SGS ROUTE GROUP:ROUTEGRPID=110,PARTAKEMODE="PARTAKE",ROUTE=110增加到MSC2的SGs路由组配置。ADD SGS ROUTE GROUP:ROUTEGRPID=120,PARTAKEMODE="PARTAKE",ROUTE=120
6|增加SGs局向路由组配置。|增加到MSC1局向的SGs路由组配置。ADD SGS OFFICE ROUTE GROUP:OFFICEID=110,ROUTEGRPID=110,NAME="PROXYMSC1"增加到MSC2局向的SGs路由组配置。ADD SGS OFFICE ROUTE GROUP:OFFICEID=120,ROUTEGRPID=120,NAME="PROXYMSC2"
7|增加SGs VLR局向配置。|增加到MSC1局向。ADD VLROFFICE:VLROFFICEID=110,VLRNAME="proxymsc1.msc.mnc001.mcc460.3gppnetwork.org"增加到MSC2局向。ADD VLROFFICE:VLROFFICEID=120,VLRNAME="proxymsc2.msc.mnc001.mcc460.3gppnetwork.org"
8|增加VLR Pool配置。|增加到MSC1到POOL1，权重为50。ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=110,VLRLEVEL="LEVEL_1",VLRWEIGHT=50增加到MSC2到POOL1，权重为50。ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=120,VLRLEVEL="LEVEL_1",VLRWEIGHT=50
9|位置区配置。|新增一个位置区。ADD LAI:NAME="lai110",MCC="460",MNC="01",LAC="0110"
10|跟踪区配置。|新增一个跟踪区，以及对应的位置区。ADD TA:TAID=110,GRPID=1,MCC="460",MNC="01",TAC="0110",LAI="lai110",NAME="ta110"
11|添加SGs口选择VLRPOOL配置。|配置LAI对应的VLRPOOL。ADD LAIVLRPOOL:LAINAME="lai110",VLRPOOLID=1
##### 主备组网方式 
实例场景2: 某局点采用主备组网方式
某局点采用主备组网方式，组网如[图2](ZUF-78-12-004-14-%E7%89%B9%E6%80%A7%E9%85%8D%E7%BD%AE.html#T_20175108424919__ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E9%87%87%E7%94%A8%E4%B8%BB%E5%A4%87%E7%BB%84%E7%BD%91%E6%96%B9%E5%BC%8F-DAD06A6F)所示。
图2  ZUF-78-12-004-某局点采用主备组网方式
[]images/ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E9%87%87%E7%94%A8%E4%B8%BB%E5%A4%87%E7%BB%84%E7%BD%91%E6%96%B9%E5%BC%8F.png)
MME1和MSC1/standby MSC1直连，MSC1故障后，选择standby MSC1。 
配置说明
数据规划配置请参考下表。 
参数|MME1|MSC1|Standby MSC1
---|---|---|---
偶联IP|131.1.17.159|SCTP1：40.40.1.1|SCTP2：40.40.3.1
偶联端口号|6001|6001|6001
LAI|46001-0110|46001-0110|46001-0110
TAI|46001-0110|-|-
VLRPOOL|-|POOL1级别1|POOL1级别2
配置步骤
步骤|解释说明|命令脚本
---|---|---
1|设置MME支持SGs口。|SET SGSFLAG:SGSFLAG="YES"
2|增加SGs偶联。|增加MME与MSC1之间的SGs偶联连接SCTP1。ADD SCTP:ID=110,NAME="MSCSCTP110",LOCPORT=6001,REMPORT=6001,VPNID1=2,LOCADDR1="131.1.17.159",REMADDR1="40.40.1.1",ROLE="CLT",PROTOCALTYPE="SGS"增加MME与MSC2之间的SGs偶联连接SCTP2。ADD SCTP:ID=130,NAME="MSCSCTP130",LOCPORT=6001,REMPORT=6001,VPNID1=2,LOCADDR1="131.1.17.159",REMADDR1="40.40.3.1",ROLE="CLT",PROTOCALTYPE="SGS"
3|增加SGs连接。|增加到MSC1的SGs连接110。ADD SGSCONN:ID=110,SCTPID=110,NAME="sgslink110"增加到Standby MSC1的SGs路由配置，包括SGs连接130。ADD SGSCONN:ID=130,SCTPID=130,NAME="sgslink130"
4|增加SGs路由配置。|增加到MSC1的SGs路由配置，包括SGs连接110。ADD SGS ROUTE:ROUTEID=110,PARTAKEMODE="PARTAKE",CONNECTION=110增加到MSC2的SGs路由配置 ，包括SGs连接120。ADD SGS ROUTE:ROUTEID=130,PARTAKEMODE="PARTAKE",CONNECTION=130&131
5|增加SGs路由组配置。|增加到MSC1的SGs路由组配置。ADD SGS ROUTE GROUP:ROUTEGRPID=110,PARTAKEMODE="PARTAKE",ROUTE=110增加到Standby MSC1的SGs路由组配置。ADD SGS ROUTE GROUP:ROUTEGRPID=130,PARTAKEMODE="PARTAKE",ROUTE=130
6|增加SGs局向路由组配置。|增加到MSC1局向的SGs路由组配置。ADD SGS OFFICE ROUTE GROUP:OFFICEID=110,ROUTEGRPID=110,NAME="MSC1"增加到Standby MSC1局向的SGs路由组配置。ADD SGS OFFICE ROUTEGROUP:OFFICEID=130,ROUTEGRPID=120,NAME="STANDBYMSC"
7|增加SGs VLR局向配置。|增加到MSC1局向。ADD VLROFFICE:VLROFFICEID=110,VLRNAME="msc1.msc.mnc001.mcc460.3gppnetwork.org"增加到Standby MSC1局向。ADD VLROFFICE:VLROFFICEID=130,VLRNAME="standbymsc.msc.mnc001.mcc460.3gppnetwork.org";
8|增加VLR Pool配置。|增加到MSC1到POOL1级别1，权重为50。ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=110,VLRLEVEL="LEVEL_1",VLRWEIGHT=50增加到Standby MSC1到POOL1级别2，权重为50。ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=130,VLRLEVEL="LEVEL_2",VLRWEIGHT=50
9|位置区配置。|新增一个位置区。ADD LAI:NAME="lai110",MCC="460",MNC="01",LAC="0110"
10|跟踪区配置。|新增一个跟踪区，以及对应的位置区。ADD TA:TAID=110,GRPID=1,MCC="460",MNC="01",TAC="0110",LAI="lai110",NAME="ta110"
11|添加SGs口选择VLR Pool配置。|配置LAI对应的VLR Pool。ADD LAIVLRPOOL:LAINAME="lai110",VLRPOOLID=1
##### 负荷分担组网方式 
实例场景3: 某局点采用负荷分担组网方式
某局点采用负荷分担组网方式，组网如[图3](ZUF-78-12-004-14-%E7%89%B9%E6%80%A7%E9%85%8D%E7%BD%AE.html#T_20175108424919__ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E9%87%87%E7%94%A8%E8%B4%9F%E8%8D%B7%E5%88%86%E6%8B%85%E7%BB%84%E7%BD%91%E6%96%B9%E5%BC%8F-DAD09310)所示。
图3  ZUF-78-12-004-某局点采用负荷分担组网方式
[]images/ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E9%87%87%E7%94%A8%E8%B4%9F%E8%8D%B7%E5%88%86%E6%8B%85%E7%BB%84%E7%BD%91%E6%96%B9%E5%BC%8F.png)MME1和MSC1/MSC2直连，MSC1/MSC2进行负荷分担。 
配置说明
数据规划配置请参考下表。 
参数|MME1|MSC1|MSC2
---|---|---|---
偶联IP|131.1.17.159|SCTP1：40.40.1.1|SCTP2：40.40.2.1
偶联端口号|6001|6001|6001
LAI|46001-0110|46001-0110|46001-0110
TAI|46001-0110|-|-
VLR Pool|-|POOL1级别1|POOL1级别1
配置步骤
步骤|解释说明|命令脚本
---|---|---
1|设置MME支持SGs口。|SET SGSFLAG:SGSFLAG="YES"
2|增加SGs偶联。|增加MME与MSC1之间的SGs偶联连接SCTP1。ADD SCTP:ID=110,NAME="MSCSCTP110",LOCPORT=6001,REMPORT=6001,VPNID1=2,LOCADDR1="131.1.17.159",REMADDR1="40.40.1.1",ROLE="CLT",PROTOCALTYPE="SGS"增加MME与MSC2之间的SGs偶联连接SCTP2。ADD SCTP:ID=120,NAME="MSCSCTP120",LOCPORT=6001,REMPORT=6001,VPNID1=2,LOCADDR1="131.1.17.159",REMADDR1="40.40.2.1",ROLE="CLT",PROTOCALTYPE="SGS"
3|增加SGs连接。|增加到MSC1的SGs连接110。ADD SGSCONN:ID=110,SCTPID=110,NAME="sgslink110"增加到MSC2的SGs连接120。ADD SGSCONN:ID=120,SCTPID=120,NAME="sgslink120"
4|增加SGs路由配置。|增加到MSC1的SGs路由配置。ADD SGS ROUTE:ROUTEID=110,PARTAKEMODE="PARTAKE",CONNECTION=110增加到MSC2的SGs路由配置。ADD SGS ROUTE:ROUTEID=120,PARTAKEMODE="PARTAKE",CONNECTION=120
5|增加SGs路由组配置。|增加到MSC1的SGs路由组配置。ADD SGS ROUTE GROUP:ROUTEGRPID=110,PARTAKEMODE="PARTAKE",ROUTE=110增加到MSC2的SGs路由组配置。ADD SGS ROUTE GROUP:ROUTEGRPID=120,PARTAKEMODE="PARTAKE",ROUTE=120
6|增加SGs局向路由组配置。|增加到MSC1局向的SGs路由组配置。ADD SGS OFFICE ROUTE GROUP:OFFICEID=110,ROUTEGRPID=110,NAME="MSC1"增加到MSC2局向的SGs路由组配置。ADD SGS OFFICE ROUTE GROUP:OFFICEID=120,ROUTEGRPID=120,NAME="MSC2"
7|增加SGs VLR局向配置。|增加到MSC1局向。ADD VLROFFICE:VLROFFICEID=110,VLRNAME="msc1.msc.mnc001.mcc460.3gppnetwork.org"增加到MSC2局向。ADD VLROFFICE:VLROFFICEID=120,VLRNAME="msc2.msc.mnc001.mcc460.3gppnetwork.org"
8|增加VLR Pool配置。|增加到MSC1到POOL1级别1，权重为50。ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=110,VLRLEVEL="LEVEL_1",VLRWEIGHT=50增加到MSC2到POOL1级别1，权重为50。ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=120,VLRLEVEL="LEVEL_1",VLRWEIGHT=50
9|位置区配置。|新增一个位置区。ADD LAI:NAME="lai110",MCC="460",MNC="01",LAC="0110"
10|跟踪区配置。|新增一个跟踪区，以及对应的位置区。ADD TA:TAID=110,GRPID=1,MCC="460",MNC="01",TAC="0110",LAI="lai110",NAME="ta110"
11|添加SGS口选择VLR Pool配置。|配置LAI对应的VLR Pool。ADD LAIVLRPOOL:LAINAME="lai110",VLRPOOLID=1
##### 多PLMN直连负荷分担组网方式 
实例场景4: 某局点采用多PLMN直连负荷分担组网
某局点采用直连多PLMN负荷分担组网方式，组网如[图4](ZUF-78-12-004-14-%E7%89%B9%E6%80%A7%E9%85%8D%E7%BD%AE.html#T_20175108424919__ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E9%87%87%E7%94%A8%E5%A4%9APLMN%E7%9B%B4%E8%BF%9E%E8%B4%9F%E8%8D%B7%E5%88%86%E6%8B%85%E7%BB%84%E7%BD%91-DAD0B44C)所示。
图4  ZUF-78-12-004-某局点采用多PLMN直连负荷分担组网
[]images/ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E9%87%87%E7%94%A8%E5%A4%9APLMN%E7%9B%B4%E8%BF%9E%E8%B4%9F%E8%8D%B7%E5%88%86%E6%8B%85%E7%BB%84%E7%BD%91.png)
配置说明
数据规划配置请参考下表。 
参数|MSC1|MSC2|MSCa|MSCb
---|---|---|---|---
MSC Pool|POOL1|POOL1|POOL2|POOL2
PLMN|46001|46001|46001|46001
LAI|46001-0110|46001-0110|46002-0120|46002-0120
按照[配置步骤](ZUF-78-12-004-14-%E7%89%B9%E6%80%A7%E9%85%8D%E7%BD%AE.html#T_20175108424919__%E9%85%8D%E7%BD%AE%E6%AD%A5%E9%AA%A4-DAC82274)中的1-8配置好POOL1和MSC1/2、POOL2和MSCa/b之间的关系。
配置步骤
步骤|解释说明|命令脚本
---|---|---
1|位置区配置。|新增PLMN1的位置区。ADD LAI:NAME="lai110",MCC="460",MNC="01",LAC="0110"新增PLMN2的位置区。ADD LAI:NAME="lai120",MCC="460",MNC="02",LAC="0120"
2|跟踪区配置。|新增一个跟踪区。ADD TA:TAID=110,GRPID=1,MCC="460",MNC="01",TAC="0110"
3|添加基于IMSI和TAI映射LAI配置。|添加基于IMSI和TAI映射LAI配置。ADD IMSITAITOLAI:IDX=110,TAIID=110,LAINAME="lai110"添加基于IMSI和TAI映射LAI配置。ADD IMSITAITOLAI:IDX=120,TAIID=110,LAINAME="lai120"
4|添加移动号码分析。|添加PLMN1移动号码分析。ADD MDNAL:DGT="46001",ENTR="DAS_IMSI_LAI",RST=110添加PLMN2移动号码分析。ADD MDNAL:DGT="46002",ENTR="DAS_IMSI_LAI",RST=120
5|添加SGS口选择VLR Pool配置。|配置LAI110对应的VLR Pool。ADD LAIVLRPOOL:LAINAME="lai110",VLRPOOLID=1配置LAI120对应的VLR Pool。ADD LAIVLRPOOL:LAINAME="lai120",VLRPOOLID=2
##### 根据NRI选择VLR 
实例场景3: 某局点支持NRI选择VLR
某局点采用组网如[图5](ZUF-78-12-004-14-%E7%89%B9%E6%80%A7%E9%85%8D%E7%BD%AE.html#T_20175108424919__ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E6%94%AF%E6%8C%81NRI%E9%80%89%E6%8B%A9VLR-DAD125C9)所示。
图5  ZUF-78-12-004-某局点支持NRI选择VLR
[]images/ZUF-78-12-004-%E6%9F%90%E5%B1%80%E7%82%B9%E6%94%AF%E6%8C%81NRI%E9%80%89%E6%8B%A9VLR.png)MME1和MSC1/MSC2直连，MME1支持根据NRI选择VLR时，选择MSC1还是MSC2是由用户带上来的NRI决定。 
配置说明
数据规划配置请参考下表。 
参数|MME1|MSC1|Standby MSC1
---|---|---|---
偶联IP|131.1.17.159|SCTP1：40.40.1.1|SCTP2：40.40.3.1
偶联端口号|6001|6001|6001
LAI|46001-0110|46001-0110|46001-0110
TAI|46001-0110|-|-
VLR Pool|-|POOL1级别1|POOL1级别2
参数|POOL1|MSC1|MSC2
---|---|---|---
POOL1的NRI长度|5|-|-
POOL1内VLR NRI值|-|1,2,3,4,5|27,28,29,30,31
配置步骤
步骤|解释说明|命令脚本
---|---|---
1|设置MME支持SGs口.|SET SGSFLAG:SGSFLAG="YES";
2|设置MME支持根据NRI选择VLR。|SET SOFTWARE PARAMETER:PARAID=65678,PARAVALUE=1
3|增加SGs偶联。|增加MME与MSC1之间的SGs偶联连接SCTP1。ADD SCTP:ID=110,NAME="MSCSCTP110",LOCPORT=6001,REMPORT=6001,VPNID1=2,LOCADDR1="131.1.17.159",REMADDR1="40.40.1.1",ROLE="CLT",PROTOCALTYPE="SGS"增加MME与MSC2之间的SGs偶联连接SCTP2。ADD SCTP:ID=120,NAME="MSCSCTP120",LOCPORT=6001,REMPORT=6001,VPNID1=2,LOCADDR1="131.1.17.159",REMADDR1="40.40.2.1",ROLE="CLT",PROTOCALTYPE="SGS"
4|增加SGs连接。|增加到MSC1的SGs连接110。ADD SGSCONN:ID=110,SCTPID=110,NAME="sgslink110"增加到MSC2的SGs连接120。ADD SGSCONN:ID=120,SCTPID=120,NAME="sgslink120"
5|增加SGs路由配置。|增加到MSC1的SGs路由配置。ADD SGS ROUTE:ROUTEID=110,PARTAKEMODE="PARTAKE",CONNECTION=110增加到MSC2的SGs路由配置。ADD SGS ROUTE:ROUTEID=120,PARTAKEMODE="PARTAKE",CONNECTION=120
6|增加SGs路由组配置。|增加到MSC1的SGs路由组配置。ADD SGS ROUTE GROUP:ROUTEGRPID=110,PARTAKEMODE="PARTAKE",ROUTE=110增加到MSC2的SGs路由组配置。ADD SGS ROUTE GROUP:ROUTEGRPID=120,PARTAKEMODE="PARTAKE",ROUTE=120
7|增加SGs局向路由组配置。|增加到MSC1局向的SGs路由组配置。ADD SGS OFFICE ROUTE GROUP:OFFICEID=110,ROUTEGRPID=110,NAME="MSC1"增加到MSC2局向的SGs路由组配置。ADD SGS OFFICE ROUTE GROUP:OFFICEID=120,ROUTEGRPID=120,NAME="MSC2"
8|增加SGs VLR局向配置。|增加到MSC1局向。ADD VLROFFICE:VLROFFICEID=110,VLRNAME="msc1.msc.mnc001.mcc460.3gppnetwork.org"增加到MSC2局向。ADD VLROFFICE:VLROFFICEID=120,VLRNAME="msc2.msc.mnc001.mcc460.3gppnetwork.org"
9|增加VLR Pool配置。|增加到MSC1到POOL1级别1，权重为50。ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=110,VLRLEVEL="LEVEL_1",VLRWEIGHT=50增加到MSC2到POOL1级别1，权重为50。ADD VLRPOOL:VLRPOOLID=1,VLROFFICEID=120,VLRLEVEL="LEVEL_1",VLRWEIGHT=50
10|VLR Pool NRI的长度配置。|增加POOL1的NRI长度，长度为5。ADD POOLNRL LEN:VLRPOOLID=1,NRILENGTH=5
11|POOL内VLR NRI值的配置。|增加POOL内VLR局为110的NRI值1，2，3，4，5。ADD POOL VRLNRI:VLRPOOLID=1,VLROFFICEID=110,NRI=1&2&3&4&5增加POOL内VLR局为120的NRI值27，28，29，30，31。ADD POOLVRLNRI:VLRPOOLID=1,VLROFFICEID=120,NRI=27&28&29&30&31
12|位置区配置。|新增一个位置区。ADD LAI:NAME="lai110",MCC="460",MNC="01",LAC="0110"
13|跟踪区配置。|新增一个跟踪区，以及对应的位置区。ADD TA:TAID=110,GRPID=1,MCC="460",MNC="01",TAC="0110",LAI="lai110",NAME="ta110"
14|添加SGS口选择VLR Pool配置。|配置LAI对应的VLR Pool。ADD LAIVLRPOOL:LAINAME="lai110",VLRPOOLID=1
### 测试用例 
测试项目|CSFB功能
测试目的|验证Proxy MSC负荷分担组网方式业务正常。
预置条件|按照ProxyMSC负荷分担组网方式描述配置好环境。
测试过程|用户联合附着后发起语音业务，去附着。断开到用户附着到的Proxy MSC的连接。用户重新联合附着。
通过准则|用户首次联合附着和回落正常。用户第二次重新附着，选择正常Proxy MSC进行业务。
测试项目|CSFB功能
测试目的|验证直连MSCN+1主备组网方式业务正常。
预置条件|按照直连MSCN+1主备组网方式描述配置好环境。
测试过程|用户联合附着后发起语音业务，去附着。断开到MSC1和MSC2的连接。用户重新联合附着。
通过准则|用户首次联合附着和回落正常。用户第二次重新附着，选择正常Standby MSC进行业务。
测试项目|CSFB功能
测试目的|验证直连MSCPOOL组网方式业务正常。
预置条件|按照直连MSCPOOL组网方式描述配置好环境。
测试过程|用户联合附着后发起语音业务，去附着。断开到用户附着到的MSC的连接。用户重新联合附着。
通过准则|用户首次联合附着和回落正常。用户第二次重新附着，选择正常 MSC进行业务。
测试项目|CSFB功能
测试目的|验证多PLMN直连MSC POOL组网业务正常。
预置条件|按照直连MSCN+1主备组网方式描述配置好环境。
测试过程|不同PLMN用户联合附着后发起语音业务，去附着。
通过准则|联合附着时，MME为不同PLMN的用户选择不同的POOL。用户联合附着和回落正常。
测试项目|CSFB功能
测试目的|验证根据NRI选择VLR业务正常。
预置条件|按照组网方式描述配置好环境。
测试过程|用户带上不同的NRI联合附着后发起语音业务，去附着。
通过准则|联合附着时，MME为携带不同NRI的用户选择不同的VLR。用户联合附着和回落正常。
# ZUF-78-12-005 SRVCC 
## 特性描述 
## 特性描述 
### 描述 
##### 定义 
SRVCC是3GPP提出的一种VoLTE语音业务连续性方案，主要是为了解决当单射频UE在LTE网络和2G/3G CS网络之间移动时，如何保证语音呼叫连续性的问题，即保证单射频UE
在IMS 控制的VoIP 语音和CS 域语音之间的平滑切换。
eSRVCC主要是指基于SIP的SRVCC增强改进方案；相对于SRVCC切换，eSRVCC切换在IMS网络新增ATCF/ATGW逻辑网元，ATCF在SRVCC语音切换时锚定媒体流，因而媒体的切换不需要通过对端的IMS
UE参与，避免因为IMS信令路径过长引起的SRVCC切换时的语音中断和时延。
##### 背景知识 
VoLTE即基于LTE承载的IMS语音。对运营商而言，部署VoLTE意味着开启了向移动宽带语音演进之路。从长远来看，这将给运营商带来两方面的价值，一是提升无线频谱利用率、降低网络成本。另一个价值就是提升用户体验，VoLTE的体验明显优于传统CS语音。 
但是，由于现阶段LTE覆盖比较有限，运营商需要利用传统CS覆盖的广度和深度来提供无缝的语音业务；而通话中的VoLTE到CS的切换，就是SRVCC技术。SRVCC针对支持LTE和GERAN/UTRAN双模单待方式的终端，通过将话路由LTE
切换到GERAN/UTRAN的方式，保证了通话过程中的语音连续性。 
SRVCC切换中的语音中断和时延，主要取决于语音媒体切换时远端更新带来的时延。而eSRVCC正是针对这一问题提出的基于SIP的改进方案；相对于SRVCC切换，eSRVCC切换在IMS网络新增ATCF/ATGW逻辑网元，ATCF在SRVCC语音切换时锚定媒体流，因而媒体的切换不需要通过对端的IMS
UE参与，从而避免了因为IMS信令路径过长引起的SRVCC切换时的语音中断和时延。 
### 应用场景 
##### SRVCC的主要应用场景 
网络开展了VoLTE业务，但是LTE网络无法达到全覆盖，在没有LTE覆盖的区域，需要将语音切换到CS域，以保证用户语音业务连续性。 
##### eSRVCC的主要应用场景 
当SRVCC的切换中断时间超过合理范围（如3GPP
TS22.278要求的300ms），网络需要部署ATCF和ATGW网元，将用户的媒体流锚定在ATCF/ATGW，避免切换时需要UE参与媒体修改而带来的中断时延。 
##### 特定CS域业务引发的SRVCC 
用户在VoLTE语音业务进行中，需要通过SRVCC的方式回落到CS域，完成如定位、补充业务设置等CS域业务；为了保证CS域业务正常实现，SRVCC切换的目标MSC需要选择SGs口关联的MSC。 
### 客户收益 
受益方|受益描述
---|---
运营商|支持SRVCC切换流程，可以保证用户在移动过程中语音业务的连续性，保证用户的业务体验，提升用户对LTE网络使用的满意度。
移动用户|LTE网络信号不佳时，仍可享受语音通话不受影响。
### 实现原理 
##### 系统架构 
EPS网络E-UTRAN与GERAN/UTRAN间SRVCC切换架构如[图1](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__fig_-1354-28143679)所示。
图1  EPS网络E-UTRAN与GERAN/UTRAN间SRVCC切换架构图
[]images/ZUF-78-12-005%20EPS%20E-UTAN%E4%B8%8EGERANUTRAN%E9%97%B4SRVCC%E5%88%87%E6%8D%A2%E6%9E%B6%E6%9E%84%E5%9B%BE.png)
SRVCC功能需要UE、eNodeB、MME、MSC-Server、HSS、SGW、PGW、PCRF、DNS Server的共同配合，在SRVCC功能中各网元的主要作用如下： 
网元|作用
---|---
UE|支持E-UTRAN/GERAN/UTRAN接入；支持将自身的SRVCC能力通过NAS信令传递给MME。
eNodeB|能够识别该用户是否可以进行SRVCC切换及是否携带了语音承载，并能够据此选择合适的邻居小区列表；SRVCC切换时能够告知MME本次切换为一个SRVCC切换。
MME|能够分离出语音承载用于PS–CS切换；非语音承载可进行PS-PS切换、挂起或局间传递；MME基于本地配置或者DNS Server选择MSC Server。
MSC Server|通过Sv口与MME连接，能够处理MME发起的SRVCC的呼叫切换。在SRVCC切换过程中完成用户语音业务到IMS域的切换。
HSS|基于S6a口将SRVCC相关参数（STN-SR、C-MSISDN、ICS-Flags等）通过ULA或者IDR消息下发给MME。
PCRF|IMS语音使用QCI=1的承载。
DNS Server|MME基于RAI/RNCID进行MSCServer域名解析时，可选的使用的DNS Server进行域名解析。（另一种域名解析方法是使用MME本地网管配置）
eSRVCC的商用部署如[图2](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__ESRVCC%E5%95%86%E7%94%A8%E9%83%A8%E7%BD%B2%E5%9B%BE-D9A5CC73)所示。
图2  eSRVCC商用部署图
[]images/ZUF-78-12-005%20eSRVCC%E5%95%86%E7%94%A8%E9%83%A8%E7%BD%B2%E5%9B%BE.png)
eSRVCC新增了ATCF、ATGW网元，主要网元涉及的功能为： 
网元|作用
---|---
MME|负责向HSS上报UE的SRVCC能力，接收HSS下发的STN-SR，并在PSto CS请求消息中带给MSC Server。
UE|向MME上报SRVCC能力。
HSS|负责保存UE的SRVCC能力供SCCAS查询，负责保存UE的STN-SR信息供SCC AS修改。
SCC AS|关联ATCF和远端的呼叫分支，更新HSS保存的STN-SR，提供C-MSISDN和ATU-STI等呼叫建立信息，根据UE的SRVCC能力和签约信息决策是否执行eSRVCC等。
ATCF|分配STN-SR号码并通过第三方注册通知到SCCAS，进入SIP会话，锚定控制面在ATGW，完成到CS媒体的接入转移和更新等。
ATGW|受控ATCF完成呼叫中的媒体面功能。
##### 业务流程 
SRVCC业务流程介绍主要包含： 
为切换辅助的业务流程，比如Attach/TAU时SRVCC能力协商、MME向eNodeB传递“UE是否可以进行SRVCC切换指示”等。
切换相关的业务流程，比如下面的几种切换场景等。 
SRVCC的E-UTRAN附着流程
Attach和TAU流程与EPC中的流程保持一致。 
对于SRVCC有如下额外处理： 
Attach Request和Tracking Area Update消息中的“MS Network Capability”信元包含有UE的SRVCC capability indication；MME需要保存这一信息。
Attach Request和非周期性的Tracking Area Update消息中同时包含有GERAN MS Classmark3、MS
Classmark2以及Supported Codecs信元。MME需要保存这些信息。 
HSS发给MME的签约信息中包含有SRVCC STN-SR和C-MSISDN；如果有SRVCC STN-SR is present则说明用户已经签约SRVCC业务。如果拜访网络不支持SRVCC，HSS将不携带这些信息。 
MME在S1 AP的Initial Context Setup Request消息中携带“SRVCC operation
possible”指示，表明UE和MME都具备SRVCC能力。
SRVCC的Service Request流程
业务请求流程与EPC中的流程保持一致。 
MME在S1 AP的Initial Context
Setup Request消息中携带“SRVCC operation possible”指示，表明UE和MME都具备SRVCC能力。
SRVCC PS Handover流程
PS-PS切换流程与EPC中的流程保持一致。 
对于SRVCC有如下额外处理： 
MS Classmark 2、MS Classmark 3、STN-SR、C-MSISDN、ICS Indicator以及Supported
Codec信元需要由源MME发送到目标MME/SGSN。 
目标MME在S1-AP的Handover Request消息中携带"SRVCC operation possible"指示，表明UE和目标MME都具备SRVCC能力。 
从E-UTRAN发起的SRVCC的呼叫流程
从E-UTRAN到GERAN/UTRAN的SRVCC切换流程，根据终端和目标侧RAN的能力，可分为下面三个触发场景： 
场景一：从E-UTRAN到GERAN的SRVCC切换，不支持DTM。流程如[图3](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E4%BB%8EE-UTRAN%E5%88%B0GERAN%E7%9A%84SRVCC%E5%88%87%E6%8D%A2%E4%B8%8D%E6%94%AF%E6%8C%81DTM-D9A884A4)所示。
图3  从E-UTRAN到GERAN的SRVCC切换，不支持DTM
[]images/ZUF-78-12-005%20SRVCC%20from%20E-UTRAN%20to%20GERAN%20without%20DTM%20support.png)
该流程要求eNB能够决策出目标为GERAN且不支持DTM或者UE不支持DTM。流程说明： 
UE发送测量报告给 E-UTRAN。 
基于UE的测量报告，源E-UTRAN决定触发到GERAN的SRVCC切换。 
源E-UTRAN发送Handover Required（Target ID, generic Source to Target
Transparent Container, SRVCC HO Indication）消息到源MME，其中SRVCC HO indication表明目标侧只有CS能力，当前的SRVCC切换只到CS域。消息中携带目标小区UE的PS业务不可用指示。 
基于语音承载关联的QCI (QCI 1)以及SRVCC HO indication，源MME从非语音承载中分离出语音承载，发起到MSC
Server的PS-CS切换流程。 
MME发送SRVCC PS to CS Request (IMSI, Target ID, STN-SR, C MSISDN,
generic Source to Target Transparent Container, MM Context)消息到MSC
Server。 其中MM Context包含有安全相关信息。 
MSC Server发送Prepare Handover Request消息到目标MSC，进行CS域的局间切换。 
目标MSC通过与目标BSS间的Handover Request/ Acknowledge消息执行目标侧的资源分配。 
目标MSC发送Prepare Handover Response 消息到MSC Server。 
MSC Server的MGW和MSC之间建立电路连接。 
MSC Server使用STN-SR发起会话转接。 
远端被更新为CS呼叫分支的SDP后，下行的VoIP报文将切换至CS呼叫分支。 
源侧的IMS呼叫分支被释放。 
MSC Server发送SRVCC PS to CS Response (Target to Source Transparent
Container) 消息到源MME。 
源MME发送Handover Command (Target to Source Transparent Container)消息到源E-UTRAN。 
源E-UTRAN发送Handover from E-UTRAN Command消息给UE。 
UE转向GERAN。 
Handover Detection在目标BSS发生。 
UE发起Suspend流程。目标SGSN发送Suspend Notification消息到源MME。MME返回Suspend
Acknowledge消息。 
目标BSS发送 Handover Complete消息到目标MSC。 
目标MSC发送SES (Handover Complete) 消息到MSC Server，语音电路打通接通。 
MSC Server收到应答消息，呼叫建立完成。 
MSC Server发送SRVCC PS to CS Complete Notification消息到源MME，通知UE抵达目标侧。源MME回复SRVCC
PS to CS Complete Acknowledge消息。 
MME去活语音使用的承载及其他GBR承载。 
MME向S-GW发送Suspend Notification消息，保留并挂起non-GBR承载。S-GW释放S1-U承载，向P-GW发送Suspend
Notification消息；MME在UE上下文中保存UE的挂起状态。所有保留的non-GBR承载在S-GW和P-GW中被标识为挂起状态。
P-GW将丢已经挂起的用户的数据报文。 
如果需要更新HLR，MSC Sever执行TMSI重分配流程。 
如果TMSI重分配成功， MSC Server执行MAP的Update Location。 
对于紧急呼叫，切换完成后，源MME或MSC Server会向GMLC发送Subscriber Location Report消息，携带MSC
Server的标识。 
场景二：从E-UTRAN到GERAN的SRVCC切换支持DTM但不支持DTM HO；从E-UTRAN到UTRAN的SRVCC切换不支持PS
HO。 
该流程与[图3](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E4%BB%8EE-UTRAN%E5%88%B0GERAN%E7%9A%84SRVCC%E5%88%87%E6%8D%A2%E4%B8%8D%E6%94%AF%E6%8C%81DTM-D9A884A4)所描述的十分类似，所不同的是Suspend流程（[图3](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E4%BB%8EE-UTRAN%E5%88%B0GERAN%E7%9A%84SRVCC%E5%88%87%E6%8D%A2%E4%B8%8D%E6%94%AF%E6%8C%81DTM-D9A884A4)中的第18步和第22a步）无需执行，MME仅去活语音承载，设置PS-to-CS handover indicator。该场景需要eNB能够检测出目标网络是GERAN支持DTM但不支持
DTM HO或是UTRAN (HSPA)网络不支持 PS HO。在[图3](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E4%BB%8EE-UTRAN%E5%88%B0GERAN%E7%9A%84SRVCC%E5%88%87%E6%8D%A2%E4%B8%8D%E6%94%AF%E6%8C%81DTM-D9A884A4)的流程结束后，UE执行RAU流程，保留的PS资源将被重建。
场景三：从E-UTRAN到UTRAN的SRVCC切换支持PS
HO；从E-UTRAN到GERAN的SRVCC切换支持DTM HO。流程如[图4](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E4%BB%8EE-UTRAN%E5%88%B0UTRAN%E7%9A%84SRVCC%E5%88%87%E6%8D%A2%E6%94%AF%E6%8C%81PSHO%E4%BB%8EE-UTRA-D9A92D24)所示。
图4  从E-UTRAN到UTRAN的SRVCC切换支持PS HO；从E-UTRAN到GERAN的SRVCC切换支持DTM HO
[]images/ZUF-78-12-005%20SRVCC%20from%20E-UTRAN%20to%20UTRAN%20with%20PS%20HO.png)
流程说明： 
UE 发送测量报告给E-UTRAN。 
基于UE的测量报告，源E-UTRAN决定出发到UTRAN的SRVCC切换。 
如果目标为UTRAN，源E-UTRAN发送Handover Required（Target ID, generic Source
to Target Transparent Container, SRVCC HO indication）消息给源MME。其中SRVCC
HO indication指示为CS+PS HO。 
根据语音承载的QCI（QCI 1）以及SRVCC HO Indication，源MME分离语音承载和其他PS承载，分别向MSC和SGSN发起切换。 
按下列步骤执行： 
源MME对语音承载发起PS-CS handover流程，发送SRVCC PS to CS Request (IMSI,
Target ID, STN-SR, C MSISDN, Source to Target Transparent Container,
MM Context) 消息给MSC Server。其中MM Context包括安全相关信息。其中MSC enhanced for
SRVCC的选择。 
MSC Server发送Prepare Handover Request消息到目标MSC，进行CS域的局间切换。 
目标MSC发送Relocation Request消息到目标RNS， 请求CS切换的资源分配。 
与上一步并行处理的是，源MME发起PS承载的切换，按下列步骤执行： 
源MME发送Forward Relocation Request (generic Source to Target
Transparent Container, MM Context, PDP Contexts) 消息给目标SGSN。PDP Contexts包含有除了语音承载外的所有承载信息。 
目标SGSN发送Relocation Request (Source to Target Transparent Container)
消息给目前 RNS，请求PS切换的资源分配。 
目标RNS收到CS relocation和PS relocation后，分配相应的CS和PS资源，按下列步骤执行： 
目标RNS 回复Relocation Request Acknowledge (Target to Source Transparent
Container) 消息给目标SGSN。 
目标SGSN 发送Forward Relocation Response (Target to Source Transparent
Container) 消息给源 MME。 
与上一步并行处理的是： 
目标RNS回复Relocation Request Acknowledge (Target to Source Transparent
Container) message 给目标MSC。 
目标MSC发送Prepare Handover Response (Target to Source Transparent
Container) 消息给MSC Server。 
MSC Server的MGW和MSC之间建立电路连接。 
MSC Server使用STN-SR发起会话转接。 
远端被更新为CS呼叫分支的SDP后，下行的VoIP报文将切换至CS呼叫分支。 
源侧的IMS呼叫分支被释放。 
MSC Server发送SRVCC PS to CS Response (Target to Source Transparent
Container) 消息到源MME。 
源MME同步两个准备重定向，发送Handover Command (Target to Source Transparent
Container)消息到源E-UTRAN。 
源E-UTRAN发送Handover from E-UTRAN Command消息给UE。 
UE转向目标GERAN/UTRAN小区。 
Handover Detection在目标RNC发生。 
CS切换完成，执行下列步骤： 
目标RNS发送Relocation Complete消息到目标MSC。 
目标MSC发送SES (Handover Complete) 消息到MSC Server，语音电路打通接通。 
MSC Server收到应答消息，呼叫建立完成。 
MSC Server发送SRVCC PS to CS Complete Notification消息到源MME，通知UE抵达目标侧。源MME回复SRVCC
PS to CS Complete Acknowledge消息。 
MME去活语音使用的承载，向S-GW/P-GW发送Delete Bearer Command消息，携带PS-to-CS
handover indicator。 
如果需要更新HLR，MSC Sever执行TMSI重分配流程。 
如果TMSI重分配成功， MSC Server执行MAP的Update Location。 
与上一步并行的是，PS切换完成，执行下列步骤： 
目标RNS发送Relocation Complete消息到目标SGSN。 
目标SGSN发送Forward Relocation Complete消息到源MME。完成第17e步骤后，源MME向目标SGNS回复Forward
Relocation Complete Acknowledge消息。 
目标SGSN更新承载。 
MME发送Delete Session Request到SGW。 
源MME发送Release Resources消息到源eNodeB。源eNodeB释放UE的相关资源。 
对于紧急呼叫，切换完成后，源MME或MSC Server会向GMLC发送Subscriber Location Report消息，携带MSC
Server的标识。 
上述三个场景中，MME中相关的语音承载及非语音承载由于SRVCC切换可能会删除或重建，介绍如下： 
MME中的语音承载：基于SRVCC切换至CS域后由CS域维护（EPS域的语音承载在IMS语音切换至CS域后释放），并在语音结束后由CS域负责释放对应语音链路。 
MME中的非IMS语音承载：在第一个场景中，对于GBR承载立即释放，对于非GBR承载，在IMS语音结束前在EPS域中挂起，在IMS语音结束后由UE重选网络（EPS域或者PS域），并在对应网络中恢复(resume)这些挂起(suspend)的承载。在第二个场景中：在SRVCC切换后，所有非语音承载通过PS域的RAU流程传递到PS域中，并在PS域恢复。在第三个场景中：在SRVCC切换过程中，所有非语音承载通过PS域HO流程传递到PS域中，并在PS域恢复。 
MSC enhanced for SRVCC的选择
为了满足IMS通话状态下，UE回落到CS域完成特定CS业务而触发SRVCC的功能要求，MME在选择SRVCC时，优先选择UE在联合附着或联合TAU时注册的同时具备CSFB和SRVCC业务处理能力的MSC/VLR。 
普通的SRVCC流程中，MME根据切换请求消息中的Target ID构造FQDN，进行DNS查询或者本地地址解析，并根据查询或解析返回的结果，按权重和优先级，选择MSC
Server的IP地址，发送Sv口消息。 
如果根据Target ID获取MSC Server地址失败，还可使用本地配置的缺省MSC Server。 
eSRVCC的ATCF选择流程
eSRVCC的ATCF选择流程如[图5](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__ESRVCC%E7%9A%84ATCF%E9%80%89%E6%8B%A9%E6%B5%81%E7%A8%8B-D9A9E233)所示。
图5  eSRVCC的ATCF选择流程
[]images/ZUF-78-12-005%20eSRVCC%E7%9A%84ATCF%E9%80%89%E6%8B%A9%E6%B5%81%E7%A8%8B.png)
流程说明： 
用户EPS附着。 
MME发起位置更新，在ULR消息中携带UE SRVCC capability，发送给HSS，HSS储存该字段。 
UE通过ATCF向归属网络发起注册。 
ATCF分配STN-SR，转发SIP注册消息。 
CSCF发送第三方注册消息到SCC AS，携带STN-SR。 
SCC AS查询UE的SRVCC能力。 
SCC AS更新HSS保存的STN-SR为当前ATCF分配的STN-SR。 
HSS发送插入用户数据请求，其中携带STN-SR号码。 
SCC AS向ATCF通知UE的SRVCC能力等相关信息。 
### 系统影响 
SRVCC切换由eNodeB控制发起的，是否需要进行SRVCC切换，主要取决于LTE无线信号覆盖及质量；SRVCC切换并不引发其他MME的业务流程。 
网络中支持VoLTE和SRVCC的用户数以及用户语音业务的话务模型，决定了MME开启SRVCC功能后，MME实际上的负荷增加。如果网络中开通了SRVCC业务，需要在配置计算时，输入相关的SRVCC话务模型数据，以便得到准确的结果。 
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
业务|交互
---|---
SRVCC HO与PS-PSHO|在不支持SRVCC功能前，所有承载均向UTRANPS域切换，语音承载可能会重建失败。支持SRVCC功能后，对应SRVCC from E-UTRAN to UTRANwith PS HO or GERAN with DTM HO support流程，语音承载向CS域切换，非语音承载向PS域切换。
IMS语音|SRVCC切换是为IMS语音服务的，因此，MME支持IMS语音是SRVCC切换的前提条件。
### 遵循标准 
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
3GPP TS 23.216: " Single Radio Voice Call Continuity (SRVCC)". 
3GPP TR 23.856: " Single Radio Voice Call Continuity (SRVCC)
enhancements ". 
### 特性能力 
MME并不特别限定支持对接的MSC数目。 
### 可获得性 
##### License要求 
License ID|License控制值|License描述
---|---|---
7014|ON|MME支持SRVCC功能
##### 对其他网元的要求 
UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
##### 工程规划要求 
MME与MSC间使用的Sv口（承载于UDP）相连。MME根据切换请求消息中的Target
ID构造FQDN来解析目标MSC的地址。 
常见的MME与MSC的组网场景包括以下两种： 
组网方式|MSC升级方式|Sv口MSC解析方式|切换方式
---|---|---|---
Proxy MSC组网|避免全网MSC升级，只需要新增一对支持SRVCC的MSC。|通过TargetID构造FQDN解析的方式，DNS解析到Proxy MSC。|切换后，由ProxyMSC再次发起CS域的局向切换，切换到UE在CS域相连的MSC。
直连组网方式|需要全网MSC升级支持SRVCC。|通过TargetID构造FQDN解析的方式，DNS解析到UE在CS域相连的MSC。|直接切换到UE在CS域相连的MSC。
Target ID构造的FQDN，有以下几种格式： 
使用RNC ID：rnc<RNC>.rnc.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org 
使用RAI：Target ID中包含有RAC：rac<RAC>.lac<LAC>.rac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.orgTarget ID中不包含有RAC：rac00FF.lac<LAC>.rac.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org 
### O&M相关 
##### 命令 
配置项命令配置项参见表1。表1  新增配置项配置项命令IMS 语音参数配置SET PACKET DOMAIN PARAMETERADD IMS APNADD PLMN IMS APNADD UE VOICE POLICYSET DEFAULT VOICESET POLICYMME支持MSC Server域名解析ADD EPCHOST配置Sv接口支持VRFSET VRFCFGSv接口信令地址配置SHOW MME SX GTPC基于PLMN的缺省SRVCC增强MSC Server配置ADD PLMN DFTMSCS全局缺省SRVCC增强MSC Server配置SET GLOBAL DFTMSCSSRVCC优选SGS口注册的MSC配置ADD VLROFFICE 
安全变量新增安全变量参见表2。表2  新增安全变量安全变量命令MME支持基于PS会话IMS语音SET PACKET DOMAIN PARAMETER 
软件参数新增软件参数参见表3。表3  软件参数软参ID软参名称65562MSC Server IP地址获取方式65642MME支持缺省SRVCC增强MSC Server262385按SRVCC能力优选SGs口MSC262386根据SGs口注册的MSC选择Sv口MSC262405MME通过权重和优先级选择MSC 
##### 性能统计 
新增性能计数器参见[表4](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_20175108424914__%E6%96%B0%E5%A2%9E%E6%80%A7%E8%83%BD%E8%AE%A1%E6%95%B0%E5%99%A8-D9B9BE3F)。
测量类型|描述
---|---
SRVCC流程测量|编号为C43020开头的所有计数器
GTPv2消息测量|编号为C43201开头的所有计数器
##### 告警和通知 
新增告警和通知参见[表5](ZUF-78-12-005-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_20175108424914__%E5%91%8A%E8%AD%A6%E5%92%8C%E9%80%9A%E7%9F%A5AlarmsAndNotifications-24EE20FD)。
告警和通知
---
2114060406 MME上报MSC Server不可达
##### 业务观察/失败观察 
该特性不涉及业务观察/失败观察的变化。 
##### 话单与计费 
该特性不涉及话单与计费的变化。 
## 特性配置 
## 特性配置 
### 配置说明 
配置MME支持SRVCC功能。 
### 配置前提 
配置数据|说明
---|---
IMS语音参数配置核查|检查安全变量“MME支持基于PS会话IMS语音”设置为“支持”。检查需要支持SRVCC切换的PLMN没有在“MME不支持IMS VoPS的PLMN”中配置。检查“语音参数策略配置”中的“缺省语音参数策略配置””为“支持IMS VoPS”。
SRVCC功能License|MME网元支持SRVCC功能，MME需要制作支持SRVCC功能的License文件。
MSC Server域名解析|需要向运营商获取MSC Server域名解析规划数据，用于SRVCC切换的RAI(s)或者RNCID(s)及对应的MSCServer的IP地址（或列表）。其中，基于RNCID域名解析只能用于MSC Server侧UTRAN接入时有效，MSCServer侧GERAN接入时只能基于RAI域名解析。IPv4及IPv6类型的MSC Server地址均支持。MME对MSC Server域名解析可以在MME的本地网管上配置，也可以配置在DNS Server上，这取决于运营商的规划。如果配置在本地网管上，则需要用到本项配置。如果配置在DNS Server上，则需要向运营商获取网络DNS Server地址信息。
MSC Server域名解析类型开关控制|在MSC Server侧使用UTRAN接入时，使用RAI(s)或者RNCID(s)，二选一即可，这个取决于运营商规划，基于3GPP协议，推荐使用RAI进行MSCServer域名解析。在MSV Server侧使用GERAN接入时，MME总是使用RAI进行MSC Server域名解析，不受本开关控制。该开关默认值即为使用RAI域名解析，默认可以不修改。
DNS Server地址配置|如果MSC Server域名解析基于DNS Server解析，则MME需要配置DNS Server地址。IPv4及IPv6类型的DNS Server地址均支持。对应的MSC Server域名解析不需要在MME本地网管配置，需要在DNS Server上配置。
Sv口VRF配置|MME与MSC Server之间是否使用VRF，这取决于运营商的规划。如果存在VRF，则需要使用本配置，VRF值需要向运营商获取。
MME是否支持缺省SRVCC增强MSCServer|MME在找不到SRVCC增强MSCServer时，是否选择缺省SRVCC增强MSC Server。
### 配置过程 
支持支持SRVCC功能的License文件，并加载到MME网管。 
根据运营商的规划，配置MSC Server侧UTRAN接入时域名解析类型控制开关（基于RNCID还是RAI进行MSC
Server域名解析）。 
 说明： 
MSC Server侧GERAN接入，MME总是使用RAI进行MSC Server域名解析。 
该控制开关默认为使用RAI，3GPP规范也是要求使用RAI，因此，若运营商无特备要求，本配置项使用默认值，无需配置。 
若运营商要求使用MME本地网管配置进行MSC Server域名解析，则在MME网管配置MSC Server在Sv口的域名解析，否则本步骤不需要，而是采用步骤4的方式。 
若运营商要求使用DNS Server进行MSC Server域名解析配置，则在MME网管配置DNS Server地址（该配置方式需要在DNS
Server上配置MSC Server的域名解析），否则本步骤不需要，而是采用步骤3的方式。 
若运营商已在MME与MSC Server间的的Sv口规划了VRF，则在MME网管中配置Sv口VRF。 
在MME网管中进行到DNS Server（如果有）及MSC Server的IP路由配置，以保证MME与DNS Server（如果有）及MSC
Server间路由可达。 
如果要开启默认MSC Server功能，则配置软参“MME支持缺省SRVCC增强MSC Server”为支持，并通过“全局缺省SRVCC增强MSC Server配置”配置缺省MSC Server。
如果需要开启SRVCC流程优选SGs口注册MSC/VLR的功能，需要在“SGs接口VLR局向配置”中配置VLR局向支持SRVCC能力和Sv接口标识。同时需要配置软参“按SRVCC能力优选SGs口MSC”为支持；配置软参“根据SGs口注册的MSC选择Sv口MSC”为非0。
### 配置实例 
##### 配置SRVCC业务 
在SRVCC业务配置之前，应当完成相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
MME支持基于PS会话IMS语音|是|MME支持基于PS会话IMS语音
支持IMS VoPS的PLMN|460 02|支持IMS VoPS的PLMN
Sv IPv4信令地址|200.51.1.159|Sv IPv4信令地址
MSC Server域名解析类型|使用RAI进行域名解析|MSC Server域名解析类型
使用RAI解析MSC Server|RAC|3
LAC|使用RAI解析MSC Server|1
MNC|使用RAI解析MSC Server|2
MCC|使用RAI解析MSC Server|460
MSC Server IP|使用RAI解析MSC Server|192.20.100.29
PLMN46002对应的缺省SRVCC增强MSCServer IP地址|192.100.11.13|PLMN46002对应的缺省SRVCC增强MSCServer IP地址
全局缺省SRVCC增强MSCServer IP地址|192.100.11.14|全局缺省SRVCC增强MSCServer IP地址
根据规划，进行如下配置。 
配置IMS语音参数。 
配置MME支持IMS语音功能开关，设置分组域参数“MME支持基于PS会话IMS语音”为“是”，命令如下：
[SET PACKET DOMAIN PARAMETER](../../MMESGSN\zh-CN\mml\1268017.html):MMEIIMSVOPS="YES"
新增IMS PAN配置，命令如下： 
[ADD IMS APN](../../MMESGSN\zh-CN\mml\1261784.html):APNNAME="apnims"
新增基于PLMN的IMS APN配置，命令如下： 
[ADD PLMN IMS APN](../../MMESGSN\zh-CN\mml\1261912.html):APNNAME="apnims",PLMN="460"-"02"
配置MME的Sv信令地址，命令如下。 
[SET MME SX GTPC](../../MMESGSN\zh-CN\mml\1260641.html):IIPADDR="200.51.1.159"
配置MSC Server域名解析类型控制开关，设置软件参数“MSC Server IP地址获 取方式”为RAI解析，命令如下:
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAIID=65562,PARAVALUE=1
配置MSC Server域名解析，命令如下： 
[ADD EPCHOST](../../MMESGSN\zh-CN\mml\1261552.html):NAME="rac0003.lac0001.rac.epc.mnc002.mcc460.3gppnetwork.org",SERVIICE="x-3gpp-msc",HOST="MSC",IIPADDR="192.20.100.29",PROTOCOL="x-sv"
配置MME支持缺省SRVCC增强MSC Server。 
配置MME支持缺省SRVCC增强MSC Server控制开关，设置软参“MME支持缺省SRVCC增强MSC Server”为支持，命令如下：
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAIID=65642,PARAVALUE=1
配置基于PLMN的缺省SRVCC增强MSC Server，命令如下： 
[ADD PLMN
DFTMSCS](../../MMESGSN\zh-CN\mml\1261720.html):PLMN="460"-"02",MSCSIIP="192.100.11.13"
配置全局缺省SRVCC增强MSC Server，命令如下： 
[SET GLOBAL DFTMSCS](../../MMESGSN\zh-CN\mml\1261717.html):MSCSIIP="192.100.11.14"
##### 配置eSRVCC业务 
在eSRVCC业务配置之前，应当完成SRVCC业务调试，并完成相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
HSS的Diameter局向号|27
协议版本号|R10
根据规划，进行如下配置。 
设置HSS局向的协议版本号为R10，命令如下： 
[SET DIAMADJ](../../MMESGSN\zh-CN\mml\1262151.html):ADJJIID=27,PROVERSIION="R10"
（可选）设置软件参数“默认HSS局向路由协议版本号”为R10，命令如下：
[SET
SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAIID=262293,PARAVALUE=2
##### 配置SRVCC优选SGs口注册的MSC 
在配置之前，应当完成用户联合附着和SRVCC业务调试，并完成相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
按SRVCC能力优选SGs口MSC|支持
根据SGs口注册的MSC选择Sv口MSC|1（使用配置的Sv口名称进行S-NAPTR查询，优先DNS）
MSC/VLR局向号|1
MSC/VLR局向ATTR|VLR_SRVCC
MSC/VLR在Sv口使用的名称|rac00FF.lac0001.rac.epc.mnc001.mcc460.3gppnetwork.org（ mcc460-mnc01-lac0x0001为该MSC管辖的LAI）
根据规划，进行如下配置。 
1. 设置MME支持按SRVCC能力优选SGs口MSC，命令如下： 
[SET SOFTWARE
PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262385,PARAVALUE=1
配置用户联合附着MSC/VLR局向属性支持SRVCC以及Sv口使用的名称，命令如下： 
[SET
VLROFFICE](../../MMESGSN\zh-CN\mml\1261262.html):VLROFFICEID=1,ATTR="VLR_SRVCC",SVHNAME="rac00FF.lac0001.rac.epc.mnc001.mcc460.3gppnetwork.org"
配置Sv口MSC地址的查询方式，命令如下： 
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262386,PARAVALUE=1
### 调整特性 
MME网元支持SRVCC功能相关配置一般均需要运营商统一规划，不能随意调整。 
### 测试用例 
测试项目|SRVCC fromE-UTRAN to UTRAN with PS HO
---|---
测试目的|验证MME支持SRVCC功能。
预置条件|MME支持SRVCC。网管配置使用RNC ID解析MSC。使用本地解析MSC地址。
测试过程|UE发起附着，在IMS注册成功。UE发起IMS语音呼叫。UE移动到CS信号覆盖范围，LTE信号减弱，触发SRVCC流程。
通过准则|SRVCC流程正常，MME处理流程正确。UE语音业务切换到CS域正常，语音业务没有中断。
测试结果|—
### 常见问题处理 
信令跟踪看到了MME发给MSC的SRVCC PS to CS Request消息，但是MSC未收到，ping MSC地址也是通的。 
问题分析：物理层是通的，但是业务层不同，应该是Sv口的VRF未配置，使用[SET VRFCFG](../../MMESGSN\zh-CN\mml\1260250.html)命令配置Sv口的VRF。
# ZUF-78-12-006 eSRVCC 
eSRVCC是一种基于SIP的SRVCC增强和改善方案。与SRVCC切换相比，eSRVCC切换涉及到一个新的逻辑网元，ATCF/ATGW。该网元位于IMS网络。ATCF将媒体流锚定到SRVCC语音切换流程，因此媒体切换不涉及到远程IMS UE。这就避免了在SRVCC切换过程中由于IMS信令路径过长而导致语音中断和延迟。
# ZUF-78-12-007 e1xCSFB 
## 特性描述 
## 特性描述 
### 描述 
##### 定义 
对于支持1xRTT和E-UTRAN的双模终端，网络可为终端提供从LTE网络回落到1xRTT网络，完成语音起呼或终呼的业务。这样在LTE网络无法提供VoLTE能力的区域，可利用原有1xRTT网络资源，完成语音呼叫；也可以为LTE网络下的终端提供收发1xRTT短信的能力。
##### 背景知识 
在3GPP 23.272-c00协议中，定义的1xCSFB相关业务参见下表。
业务|详细描述
---|---
CS注册/去注册|终端通过MME、IWS网元完成到1xRTT的注册和去注册。
1xCSFB语音起呼|终端从E-UTRAN回落到1xRTT之后，在1xRTT下发起语音起呼。
1xCSFB语音终呼|终端接收到CS寻呼消息，从E-UTRAN回落到1xRTT之后，在1xRTT下发起语音终呼响应。
e1xCSFB语音起呼|终端在从E-UTRAN回落到1xRTT之前，通过MME、IWS网元将语音起呼消息发送到1xRTT核心网，完成在1xRTT的语音接续后，再回落到1xRTT。
e1xCSFB语音终呼|终端接收到CS寻呼消息，从E-UTRAN回落到1xRTT之前，通过MME、IWS网元将语音终呼响应发送到1xRTT核心网，完成在1xRTT的语音接续后，再回落到1xRTT。
CS短信起呼|终端通过MME、IWS网元将短信发送到1xRTT短信中心。
CS短信终呼|1xRTT短信中心下发短信，通过IWS、MME网元将短信发送到终端。
由UE决策执行1xCSFB语音起呼/终呼还是 e1xCSFB语音起呼/终呼。
### 应用场景 
#### 摘要 
1xCSFB功能的配置主要在于IWS网元的选择，MME基于用户消息中的CELLID来选择IWS，MME与IWS之间的组网分为无容灾、主备和负荷分担三种方式。
组网方式|IWS选择
---|---
无容灾方式|一个CELLID选择一个IWS。
主备方式|一个CELLID选择一对主用IWS，主用IWS宕机，可由备用IWS接管。
负荷分担方式|一个CELLID选择多个IWS，其中IWS可具有不同的能力，MME基于IWS能力分配用户。当其中一个IWS宕机时，可由其他IWS接管。
##### 无容灾方式 
无容灾方式组网如下图所示。 
图1  无容灾方式组网
[]images/ZUF-78-12-007-%E6%97%A0%E5%AE%B9%E7%81%BE%E6%96%B9%E5%BC%8F.png)
一个CELLID配置对应一个IWS网元。 
MME从S1口接收到UL S1 CDMA2000 Tunneling消息，根据其中的CELLID查找配置得到某个IWS网元的IP地址，据此IP地址向IWS网元发送S102消息。如果此IWS网元故障，则无法发送S102消息。 
##### 主备方式 
主备方式组网如下图所示。 
图2  主备方式组网
[]images/ZUF-78-12-007-%E4%B8%BB%E5%A4%87%E6%96%B9%E5%BC%8F.png)
一个CELLID配置对应两个IWS网元，两个IWS网元的关系为主备。 
MME从S1口接收到UL S1
CDMA2000 Tunneling消息，根据其中的CELLID查找配置得到两个IWS网元： 
如果此时主用IWS网元正常，则选择主用IWS网元的IP地址，向主用IWS网元发送S102消息。 
如果此时主用IWS网元故障，则选择备用IWS网元的IP地址，向备用IWS网元发送S102消息。 
如果此时主用和备用IWS网元均故障，则无法发送S102消息。 
##### 负荷分担方式 
负荷分担方式组网如下图所示。 
图3  负荷分担方式组网
[]images/ZUF-78-12-007-%E8%B4%9F%E8%8D%B7%E5%88%86%E6%8B%85%E6%96%B9%E5%BC%8F.png)
一个CELLID配置对应多个IWS网元，多个IWS网元的关系为负荷分担，每个IWS网元可具有不同权重。 
MME从S1口接收到UL S1 CDMA2000 Tunneling消息，根据其中的CELLID查找配置得到多个IWS网元。在其中可用的IWS网元中，基于权重选择到一个IWS网元，获得此IWS网元的IP地址，向此IWS网元发送S102消息；如果所有IWS网元都不可用，则无法发送S102消息。 
### 客户收益 
受益方|受益描述
---|---
运营商|在LTE网络无法提供VoLTE能力的区域，利用原有1xRTT网络资源，为用户提供语音/短信服务。
移动用户|在LTE网络下完成语音/短信业务。
### 实现原理 
##### 系统架构 
在3GPP 23.272-c00协议中，为e1xCSFB功能，定义了1xRTT 核心网与LTE核心网互操作的参考模型，如下图所示。
图4  1xRTT 核心网与LTE核心网互操作的参考模型
[]images/ZUF-78-12-007-1xRTT%20%E6%A0%B8%E5%BF%83%E7%BD%91%E4%B8%8ELTE%E6%A0%B8%E5%BF%83%E7%BD%91%E4%BA%92%E6%93%8D%E4%BD%9C%E7%9A%84%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B.png)
如[图4](ZUF-78-12-007-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__xRTT%E6%A0%B8%E5%BF%83%E7%BD%91%E4%B8%8ELTE%E6%A0%B8%E5%BF%83%E7%BD%91%E4%BA%92%E6%93%8D%E4%BD%9C%E7%9A%84%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B-DE442405)所示， MME通过IWS网元完成与1xRTTMSC的互通，MME与IWS之间使用S102接口。
##### 涉及的网元 
e1xCSFB功能需要UE、eNodeB、MME、IWS、BSC和MSC共同完成。
网元名称|网元作用
---|---
UE|需要支持1xRTT和E-UTRAN双模，在E-UTRAN下发起回落到1xRTT的语音呼叫。
eNodeB|通知UE回落到1xRTT。接收DOWNLINK S1 1XRTT TUNNELING消息，提取其中封装的1xRTT层3信令透传给UE。从UE接收1xRTT层3信令，并封装在UPLINK S1 1XRTT TUNNELING消息中发送给MME。
MME|接收UPLINK S1 1XRTT TUNNELING消息，提取其中内容并封装在S102消息中发送给IWS。接收IWS下发的S102消息，提取其中内容并封装在DOWNLINK S1 1XRTT TUNNELING消息中发送给eNodeB。记录用户选择的IWS的IP地址。
IWS|接收MME发送的S102消息，提取其中1xRTT层3信令，转换为A1消息发送给MSC。从MSC接收A1消息，构造1xRTT层3信令，封装在S102消息中发送给MME。记录用户所在的MME的IP地址。
MSC|MSC按照标准的1xRTT信令流程处理，但不进行承载资源协商。
BSC|按照标准的1xRTT信令流程处理，接收UE的语音起呼/终呼接入，切换接入，短信接收和下发。
##### 协议栈 
MME与IWS之间采用S102接口，S102接口的协议栈如下图所示。 
图5  S102接口协议栈
[]images/ZUF-78-12-007-S102%E6%8E%A5%E5%8F%A3%E5%8D%8F%E8%AE%AE%E6%A0%88.png)
如[图5](ZUF-78-12-007-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__S102%E6%8E%A5%E5%8F%A3%E5%8D%8F%E8%AE%AE%E6%A0%88-DE4A88CB)所示，S102接口采用IP物理连接，S102接口消息承载在UDP协议上。
##### 本网元实现 
本节介绍普通型1xCSFB起呼和增强型1xCSFB起呼的实现过程。 
普通型1xCSFB语音起呼
[]images/ZUF-78-12-007-%E6%99%AE%E9%80%9A%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E8%B5%B7%E5%91%BC.png)实现过程描述如下： 
UE尝试发起语音起呼，UE发送Extended Service Request消息通知到MME，其中指示用户进行1xCSFB。 
MME发送UE Initial Context Setup Request到eNodeB，指示为CSFB回落，eNodeB通知UE回落到CS域。 
UE回落到1xRTT后发起语音呼叫，完成呼叫业务。 
增强型1xCSFB语音起呼
[]images/ZUF-78-12-007-%E5%A2%9E%E5%BC%BA%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E8%B5%B7%E5%91%BC%20.png)实现过程描述如下： 
UE尝试发起语音起呼，UE发送Extended Service Request消息通知到MME，其中指示用户进行e1xCSFB。 
MME发送UE Initial Context Setup Request到eNodeB，指示为CSFB回落，eNodeB通知UE回落到CS域。 
UE构造1xRTT的语音起呼消息，通过eNodeB发送给MME网元。 
MME将此语音起呼消息转发给IWS。 
IWS构造标准的A1接口CM Service Request消息，MSC与IWS交互完成语音呼叫建立的信令流程，IWS构造Handoff
Required消息发送到MSC，触发切换流程，MSC下发Handoff Command到IWS。 
IWS收到Handoff Command消息，转换为1xRTT的切换命令消息发送给MME。 
MME将切换命令透传到UE，通知UE执行切换。 
UE切换到1xRTT网络，在1xRTT网络下进行语音业务。 
##### 业务流程 
通过LTE完成到1xRTT的登记/去登记
通过LTE完成到1xRTT的登记/去登记流程如下图所示。 
图6  通过LTE完成到1xRTT的注册/去注册
[]images/ZUF-78-12-007-%E9%80%9A%E8%BF%87LTE%E5%AE%8C%E6%88%90%E5%88%B01xRTT%E7%9A%84%E6%B3%A8%E5%86%8C%20%E5%8E%BB%E6%B3%A8%E5%86%8C.png)
流程描述如下： 
UE附着在LTE网络中。 
UE发起到1xRTT网络的登记。 
如果用户处于IDLE态，UE先发送Service Request完成S1连接的建立。 
1xRTT登记消息的传递。 
建立S1连接后，UE通过eNodeB上报UL S1 1XRTT Tunneling消息，其中封装1xRTT登记消息。 
MME提取其中的Cell ID，通过查询配置获得对应的S102局向 IP地址，发送A21-1x Air Interface
Signaling消息。 
IWS返回A21-1x Air Ack消息，表明已收到A21-1x Air Interface Signaling消息。 
IWS发送消息到MSC，MSC完成对UE的登记。 
1xRTT登记响应消息的传递。 
IWS从MSC收到登记接受消息，IWS构造登记响应封装在A21-1x Air Interface Signaling消息中，发送给MME。 
MME通过eNodeB将登记响应发送到UE。 
MME向IWS发送A21-1x Air Ack消息，表面已收到A21-1x Air Interface Signaling消息。 
普通型1xCSFB语音起呼流程
普通型1xCSFB语音起呼流程如下图所示。 
图7  普通型1xCSFB语音起呼流程
[]images/ZUF-78-12-007-%E6%99%AE%E9%80%9A%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E8%B5%B7%E5%91%BC%E6%B5%81%E7%A8%8B.png)
流程描述如下： 
UE附着在LTE网络和1xRTT网络中。 
用户发起Extended Service Request消息，其中指示1xCSFB回落。 
MME下发UE Context Modification Request通知eNodeB，由eNodeB通知用户回落到1x
RTT。eNodeB返回UE Context Modification Respond消息，指示UE已接受回落请求。 
UE回落后，eNodeB发送UE Context Release Request消息，其中携带原因值“CS Fallback
to 1xRTT”。
MME检测到原因为“CS Fallback to 1xRTT”，挂起Non-GBR承载，发送Suspend
Notification通知SGW。
SGW返回Suspend Ack响应，指示承载已挂起。 
MME发送UE Context Release Command，通知eNodeB释放S1连接。eNodeB返回UE Context
Release Complete，指示S1连接已释放完成。 
UE在1xRTT网络下发起语音起呼，建立语音呼叫。 
普通型1xCSFB语音终呼
普通型1xCSFB语音终呼流程如下图所示。 
图8  普通型1xCSFB语音终呼流程
[]images/ZUF-78-12-007-%E6%99%AE%E9%80%9A%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E7%BB%88%E5%91%BC%E6%B5%81%E7%A8%8B.png)
流程描述如下： 
UE附着在LTE网络和1xRTT网络中。 
MSC向IWS发起对用户的语音寻呼。 
IWS封装此寻呼消息在A21-1x Air Interface Signaling消息中，通知到MME。 
MME返回A21-1x Ack指示，已接收到A21-1x Air Interface Signaling消息。 
如果用户处于IDLE态，MME先对用户寻呼，寻呼成功，下发DL S1 1XRTT Tunnelling消息，其中封装1xRTT的语音寻呼消息。 
如果用户处于连接态，则直接下发DL S1 1XRTT Tunnelling消息 
用户发起Extended Service Request消息，其中指示1xCSFB回落。 
MME下发UE Context Modification Request通知eNodeB，由eNodeB通知用户回落到1x
RTT。eNodeB返回UE Context Modification Respond消息，指示UE已接受回落请求。 
UE回落后，eNodeB发送UE Context Release Request消息，其中携带原因值“CS Fallback
to 1xRTT”。 
MME检测到原因为“CS Fallback to 1xRTT”，挂起Non-GBR承载，发送Suspend Notification通知SGW。 
SGW返回Suspend Ack响应，指示承载已挂起。 
MME发送UE Context Release Command，通知eNodeB释放S1连接。eNodeB返回UE Context
Release Complete，指示S1连接已释放完成。 
UE在1xRTT网络发送寻呼响应，建立语音呼叫。 
增强型1xCSFB语音起呼
增强型1xCSFB语音起呼流程如下图所示。 
图9  增强型1xCSFB语音起呼流程
[]images/ZUF-78-12-007-%E5%A2%9E%E5%BC%BA%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E8%B5%B7%E5%91%BC%E6%B5%81%E7%A8%8B.png)
流程描述如下： 
UE附着在LTE网络和1xRTT网络中。 
用户发起Extended Service Request消息，其中指示1xCSFB回落。 
MME下发UE Context Modification Request通知eNodeB，由eNodeB通知用户回落到1x
RTT。eNodeB返回UE Context Modification Respond消息，指示UE已接受回落请求。 
UE支持增强型1xCSFB，构造1xRTT语音起呼消息并通过eNodeB上报给MME。 
MME将1xRTT语音起呼消息封装在A21-1x Air Interface Signaling消息中发送给IWS。 
IWS返回A21-1x Air Ack，指示已接收到A21-1x Air Interface Signaling消息。 
IWS与MSC交互完成语音接续流程，IWS触发切换流程。 
IWS从MSC接收到切换命令后，封装在A21-1x Air Interface Signaling消息中发送给MME。 
MME返回A21-1x Air Ack，指示已接收到A21-1x Air Interface Signaling消息。 
MME通过S1信令将切换命令下发给eNodeB。 
eNodeB通知UE开始切换。 
如果UE不支持PS业务优化切换到1xRTT，eNodeB发送UE Context Release Request消息，其中携带原因值“CS
Fallback to 1xRTT”。 
MME检测到原因为“CS Fallback to 1xRTT”，挂起Non-GBR承载，发送Suspend Notification通知SGW。 
SGW返回Suspend Ack响应，指示承载已挂起。 
MME发送UE Context Release Command，通知eNodeB释放S1连接。eNodeB返回UE Context
Release Complete，指示S1连接已释放完成。 
UE在1xRTT下进行语音呼叫。 
如果UE支持PS业务优化切换，将PS业务切换到1xRTT网络。 
增强型1xCSFB语音终呼
图10  增强型1xCSFB语音终呼
[]images/ZUF-78-12-007-%E5%A2%9E%E5%BC%BA%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E7%BB%88%E5%91%BC%E6%B5%81%E7%A8%8B.png)
流程描述如下： 
UE附着在LTE网络和1xRTT网络中。 
MSC向IWS发起对用户的语音寻呼。 
IWS将此寻呼消息封装在A21-1xAir Interface Signaling消息中通知到MME。 
MME返回A21-1x Ack，指示已接收到A21-1xAir Interface Signaling消息。 
如果用户处于IDLE态，MME先对用户寻呼，寻呼成功后，再下发DL S1 1XRTT Tunnelling消息，其中封装1xRTT的语音寻呼消息。 
如果用户处于连接态则直接下发DL S1 1XRTT Tunnelling消息。 
用户发起Extended Service Request消息，其中指示1xCSFB回落。 
MME下发UE Context Modification Request通知eNodeB，由eNodeB通知用户回落到1x
RTT。eNodeB返回UE Context Modification Respond消息，指示UE已接受回落请求。 
UE支持增强型CSFB，先构造1xRTT语音起呼消息通过eNodeB上报给MME。 
MME将1xRTT语音起呼消息封装在A21-1xAir Interface Signaling消息中发送给IWS。 
IWS返回A21-1xAir Ack，指示已接收到A21-1xAir Interface Signaling消息。 
IWS与MSC交互完成语音接续流程，IWS触发切换流程。 
IWS从MSC接收到切换命令后，封装在A21-1xAir Interface Signaling消息中发送给MME。 
MME返回A21-1xAir Ack，指示已接收到A21-1xAir Interface Signaling消息。 
MME将通过S1信令将切换命令下发给eNodeB。 
eNodeB通知UE开始切换。 
如果UE不支持PS业务优化切换到1xRTT，eNodeB发送UE Context Release Request消息，其中携带原因值“CS
Fallback to 1xRTT”。 
MME检测到原因为“CS Fallback to 1xRTT”，挂起Non-GBR承载，发送Suspend Notification通知SGW。 
SGW返回Suspend Ack响应，指示承载已挂起。 
MME发送UE Context Release Command，通知eNodeB释放S1连接。eNodeB返回UE Context
Release Complete，指示S1连接已释放完成。 
UE在1xRTT下进行语音呼叫。 
如果UE支持PS业务优化切换，将PS业务切换到1xRTT网络。 
短信起呼
短信起呼流程如下图所示。 
图11  短信起呼
[]images/ZUF-78-12-007-%E7%9F%AD%E4%BF%A1%E8%B5%B7%E5%91%BC.png)
流程描述如下： 
UE附着在LTE网络和1xRTT网络中。 
UE发出短信，如果UE当前为IDLE态，先建立S1连接。 
eNodeB向MME发送UL S1 1xRTT Tunneling消息，其中封装1xRTT短信信令。 
MME将1xRTT短信信令封装在A21-1xAir Interface Signaling消息中发送给IWS。 
IWS返回A21-1x Ack，指示已接收到A21-1xAir Interface Signaling消息。 
IWS构造ADDS Transfer消息发送给MSC。 
MSC返回ADDS Page消息。 
IWS构造短信下行信令，并将其封装在A21-1xAir Interface Signaling消息中发送给IWS。 
MME将短信下行信令封装在DL S1 1xRTT Tunneling消息中发送给eNodeB，eNodeB通知到UE。 
MME返回A21-1x Ack，指示已接收到A21-1xAir Interface Signaling消息。 
IWS构造ADDS Page Ack消息发送给MSC。 
短信终呼
短信终呼流程如下图所示。 
图12  短信终呼
[]images/ZUF-78-12-007-%E7%9F%AD%E4%BF%A1%E7%BB%88%E5%91%BC.png)
流程描述如下： 
UE附着在LTE网络和1xRTT网络中。 
MSC下发短信，向IWS发送ADDS Page消息。 
IWS将短信下行信令封装在A21-1xAir Interface Signaling消息中发送给MME。 
MME返回A21-1x Ack，指示已接收到A21-1xAir Interface Signaling消息。 
IWS构造ADDS Page Ack消息发送给MSC。 
如果UE处于IDLE态，MME对用户寻呼建立S1连接。 
UE处于连接态后，MME将短信下行信令封装在DL S1 1xRTT Tunneling消息中发送给eNodeB，eNodeB通知到UE。 
UE在接收到短信后返回层3响应，通过eNodeB向MME发送UL S1 1xRTT Tunneling，其中封装1xRTT短信上行信令。 
MME将1xRTT短信信令封装在A21-1xAir Interface Signaling消息中发送给IWS。 
IWS返回A21-1x Ack，指示已接收到A21-1xAir Interface Signaling消息。 
IWS构造ADDS Transfer消息发送给MSC。 
### 系统影响 
本功能对于系统性能的影响取决于1xCSFB相关业务的发生频率，相关业务包括：
1xRTT登记和去登记业务。 
普通型1xCSFB起呼。 
普通型1xCSFB终呼。 
增强型1xCSFB起呼。 
增强型1xCSFB终呼。 
1xRTT短信起呼。 
1xRTT短信终呼。 
如果开通1xCSFB业务，需提供业务发生频率来评估对系统的影响。 
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
该特性不涉及与其他特性的交互。 
### 遵循标准 
标准名称
---
3GPP TS 23.272 Circuit Switched (CS) fallback in Evolved PacketSystem (EPS)
3GPP TS 29.277 Optimized Handover Procedures andProtocol between EUTRAN access and non-3GPP accesses (S102)
3GPP TS 36.413 Evolved Universal Terrestrial AccessNetwork (E-UTRAN); S1 Application Protocol (S1AP)
3GPP2 A.S0008-D Interoperability Specification (IOS) for HighRate Packet Data (HRPD) Radio Access Network Interfaces with SessionControl in the Access Network
### 特性能力 
名称|指标
---|---
CELLID个数|最多可配置65534个CELLID。
IWS组|最多可配置1024个IWS组。
IWS局向|最多可配置1024个IWS局向。
### 可获得性 
##### 版本要求及变更记录 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
##### License要求 
该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持S102接口”（license ID：7037），此项目显示为“支持”，表示ZXUN uMAC支持S102接口功能。
##### 对其他网元的要求 
UE|eNodeB|MME|IWS|MSC|BSC
---|---|---|---|---|---
√|√|√|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
##### 工程规划要求 
需获知邻接IWS网元的IP地址，MME与IWS之间采用UDP协议，端口号不需配置，使用固定的23272端口。 
需规划CELLID与IWS网元的对应关系，CELLID在UL S1 1XRTT Tunneling消息的1xRTT Sector
ID字段中携带。 
需规划IWS网元间组网模式，无容灾、主备还是负荷分担方式，负荷分担时确定各个IWS网元的分担比例。 
### O&M相关 
##### 命令 
配置项表3  新增配置项配置项命令S102本地地址配置SET S102 LOCALADDRSHOW S102 LOCALADDRIWS局向配置ADD IWSOFFSET IWSOFFDEL IWSOFFSHOW IWSOFFIWS局向组配置ADD IWSOFFGRPSET IWSOFFGRPADD IWSOFFGRP OFFICEDEL IWSOFFGRP OFFICEDEL IWSOFFGRPSHOW IWSOFFGRP基于CELLID选择IWS网元配置SET DEFAULT IWSCELLIDSHOW DEFAULT IWSCELLIDADD IWSCELLIDSET IWSCELLIDDEL IWSCELLIDSHOW IWSCELLID 
软件参数表4  新增软件参数软件参数ID软件参数名称262390S102消息重发次数262391发送失败次数导致链路故障262392发送失败时间导致链路故障262393S102局向故障恢复尝试间隔262395GTP消息是否携带S102地址 
##### 性能统计 
测量类型|描述
---|---
基于IWS局向MME S102接口消息测量|编号为43019开头的所有计数器
##### 告警和通知 
告警和通知
---
2114322442 S102局向不可用
##### 业务观察/失败观察 
该特性不涉及业务观察/失败观察的变化。 
##### 话单与计费 
该特性不涉及话单与计费的变化。 
## 特性配置 
## 特性配置 
### 配置说明 
通过配置实现e1xCSFB功能。 
### 配置前提 
MME License支持S102接口。 
按照组网规划，获知MME的S102接口的IP地址。 
按照组网规划，获知各个IWS网元的IP地址。 
按照组网规划，获知各个CELLID对应的IWS网元。 
### 配置过程 
执行命令[SET S102 LOCALADDR](None)，配置S102接口本地地址。
执行命令[ADD IWSOFF](None)，配置IWS局向。
执行命令[ADD IWSOFFGRP](None)，配置IWS局向组。
执行命令[SET DEFAULT IWSCELLID](None)，配置CELLID对应的默认IWS局向组。
执行命令[ADD IWSCELLID](None)，配置各个CELLID分别对应的IWS局向组。
### 配置实例 
##### 无容灾方式组网 
实例场景：某局点IWS采用无容灾方式组网
某局点IWS采用无容灾方式组网，如下图所示。 
[]images/ZUF-78-12-007-%E6%9F%90%E5%B1%80%E7%82%B9IWS%E9%87%87%E7%94%A8%E6%97%A0%E5%AE%B9%E7%81%BE%E6%96%B9%E5%BC%8F%E7%BB%84%E7%BD%91.png)数据规划
参数项|MME1|IWS1|IWS2
---|---|---|---
IP地址|131.1.17.159|40.40.1.1|40.40.2.1
CELLID|-|460-01-0001|其他CELLID
配置脚本
设置MME的S102接口本地地址。 
[SET S102 LOCALADDR](None):IPADDR="131.1.17.159"
配置IWS1局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=1,IP="40.40.1.1"
配置IWS2局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=2,IP="40.40.2.1"
配置IWS局向组1。 
[ADD IWSOFFGRP](None):GRPID=1,OFFICE=1-1-100
配置IWS局向组2。 
[ADD IWSOFFGRP](None):GRPID=2,OFFICE=2-1-100
配置CELLID1对应的IWS局向组。 
[ADD IWSCELLID](None):CELLID=460-01-0001,GRPID=1
配置CELLID对应的默认IWS局向组。 
[SET DEFAULT IWSCELLID](None):GRPID=2
##### 主备方式组网 
实例场景：某局点IWS采用主备方式组网
某局点IWS采用主备方式组网，如下图所示。 
[]images/ZUF-78-12-007-%E6%9F%90%E5%B1%80%E7%82%B9IWS%E9%87%87%E7%94%A8%E4%B8%BB%E5%A4%87%E6%96%B9%E5%BC%8F%E7%BB%84%E7%BD%91.png)数据规划
参数项|MME1|IWS1|备用IWS1|IWS2|备用IWS2
---|---|---|---|---|---
IP地址|131.1.17.159|40.40.1.1|40.40.1.2|40.40.2.1|40.40.2.2
CELLID|-|460-01-0001|460-01-0001|其他CELLID|其他CELLID
配置脚本
设置MME的S102接口本地地址。 
[SET S102 LOCALADDR](None):IPADDR="131.1.17.159"
配置IWS1局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=1,IP="40.40.1.1"
配置备用IWS1局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=2,IP="40.40.1.2"
配置IWS2局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=3,IP="40.40.2.1"
配置备用IWS2局向IP地址。 
[ADD IWSOFF](None):OFFICEID=4,IP="40.40.2.2"
配置IWS局向组1。 
[ADD IWSOFFGRP](None):GRPID=1,OFFICE=1-1-100
&2-2-100
配置IWS局向组2。 
[ADD IWSOFFGRP](None):GRPID=2,OFFICE=3-1-100
&4-2-100
配置CELLID1对应的IWS局向组。 
[ADD IWSCELLID](None):CELLID=460-01-0001,GRPID=1
配置其他CELLID对应的默认IWS局向组。 
[SET DEFAULT IWSCELLID](None):GRPID=2
##### 负荷分担方式组网 
实例场景：某局点IWS采用负荷分担方式组网
某局点IWS采用负荷分担方式组网，如下图所示。 
[]images/ZUF-78-12-007-%E6%9F%90%E5%B1%80%E7%82%B9IWS%E9%87%87%E7%94%A8%E8%B4%9F%E8%8D%B7%E5%88%86%E6%8B%85%E6%96%B9%E5%BC%8F%E7%BB%84%E7%BD%91.png)数据规划
参数项|MME1|IWS1|IWS2|IWS3|IWS4|IWS5|IWS6
---|---|---|---|---|---|---|---
IP地址|131.1.17.159|40.40.1.1|40.40.1.2|40.40.1.3|40.40.2.1|40.40.2.2|40.40.2.3
CELLID|-|460-01-0001|460-01-0001|460-01-0001|其他CELLID|其他CELLID|其他CELLID
配置脚本
设置MME的S102接口本地地址。 
[SET S102 LOCALADDR](None):IPADDR="131.1.17.159"
配置IWS1局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=1,IP="40.40.1.1"
配置IWS2局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=2,IP="40.40.1.2"
配置IWS3局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=3,IP="40.40.1.3"
配置IWS4局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=4,IP="40.40.2.1"
配置IWS5局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=5,IP="40.40.2.2"
配置IWS6局向的IP地址。 
[ADD IWSOFF](None):OFFICEID=6,IP="40.40.2.3"
配置IWS局向组1。 
[ADD IWSOFFGRP](None):GRPID=1,OFFICE=1-1-100
&2-1-100&3-1-100
配置IWS局向组2。 
[ADD IWSOFFGRP](None):GRPID=2,OFFICE=4-1-100
&5-1-100&6-1-100
配置CELLID1对应的IWS局向组。 
[ADD IWSCELLID](None):CELLID=460-01-0001,GRPID=1
配置其他CELLID对应的默认IWS局向组。 
[SET DEFAULT IWSCELLID](None):GRPID=2
### 测试用例 
##### 验证IWS无容灾组网方式的业务正常 
测试项目|1xCSFB功能
---|---
测试目的|验证IWS无容灾组网方式的业务正常。
预置条件|按照无容灾组网方式的实例配置，完成数据配置。
测试过程|用户附着在LTE。用户发起到1xRTT网络注册。用户发起语音起呼，进行增强型1xCSFB回落。
通过准则|用户成功注册到1xRTT网络，根据CELLID选择正确的IWS网元。用户语音起呼成功。
测试结果|–
##### 验证IWS主备组网方式的业务正常 
测试项目|1xCSFB功能
---|---
测试目的|验证IWS主备组网方式的业务正常。
预置条件|按照主备组网方式的实例配置，完成数据配置。
测试过程|用户附着在LTE。CELLID对应的主用IWS故障用户发起到1xRTT网络注册用户发起语音起呼，进行增强型1xCSFB回落。
通过准则|用户成功注册到1xRTT网络，根据CELLID选择正确的备用IWS网元。用户语音起呼成功
测试结果|–
##### 验证IWS负荷分担组网方式的业务正常 
测试项目|1xCSFB功能
---|---
测试目的|验证IWS负荷分担组网方式的业务正常。
预置条件|按照负荷分担组网方式的实例配置，完成数据配置。
测试过程|用户附着在LTE。用户发起到1xRTT网络注册。用户发起语音起呼，进行增强型1xCSFB回落。
通过准则|用户成功注册到1xRTT网络，根据CELLID选择正确的IWS网元。用户语音起呼成功。
测试结果|–
### 常见问题处理 
无。 
# ZUF-78-12-008 VoLTE保障信令流程 
## 概述 
VoLTE保障信令流程是指在语音相关流程和UE或无线侧触发的流程冲突时，MME保障语音相关流程顺利完成。 
在语音相关流程和切换、TAU、业务请求流程冲突时，MME可以缓存或通知GW缓存语音相关消息，待切换、TAU、业务请求流程完成后，再处理语音相关流程，从而尽可能地保障语音流程顺利完成。 
MME对语音业务可设置特定的寻呼策略。 
## 客户收益 
在语音相关流程和UE或无线侧触发的流程冲突时，MME尽可能保障语音相关流程成功，提升用户体验。 
## 说明 
当MME检测到网络发起的VoLTE专用承载相关流程与UE或无线网络发起的流程冲突时，MME缓存网络发起的VoLTE专用承载相关流程消息，在UE或无线网络发起的流程完成后，MME再重新处理网络发起的VoLTE专用承载相关流程消息，或向GW返回携带具体原因的故障响应。GW则会缓存网络发起的VoLTE专用承载相关流程消息，在UE或无线网络发起的流程完成后，GW继续处理网络发起的VoLTE专用承载相关流程。 
MME对语音业务可设置特定的寻呼策略。 
# ZUF-78-12-009 VoLTE容灾之MME故障控制 
## 特性描述 
## 特性描述 
### 描述 
##### 定义 
语音容灾，是指IMS/EPC/CS网络中，网元设备出现故障后，能够保证语音业务及时接管和恢复的功能。 
对于VoLTE业务，EPC网络作为VoLTE业务的承载提供者，需要在网元设备出现故障后，能够及时进行EPS承载的重建，以保证VoLTE业务及时恢复。  
对于CSFB业务，MME需要能够在MME故障或MSC故障后，能够及时恢复和MSC的SGs连接，以保证CSFB业务及时恢复。 
##### 背景知识 
VoLTE业务容灾恢复
EPC网络中，MME、SGW、PGW均采用POOL的方式实现了负荷分担和网元间的冗余备份。只要UE重新选择可用的MME、SGW和PGW，重建EPS承载，就可以实现EPC网元的容灾业务恢复。 
VoLTE是基于LTE承载的IMS语音业务，为了保证VoLTE业务的可靠性，对EPC网络的可靠性有更高的要求。特别是对于VoLTE终呼业务来说，需要保持UE实时在线并始终有可用的EPS承载。所以这就需要在EPC网元发生故障后，能够尽快的重建EPS承载，完成业务恢复。 
由于IMS网络中UE的P-CSCF的发现过程是在UE创建PDN连接时，由PGW通过PCO参数将可用的P-CSCF下发给UE的，所以在P-CSCF故障后需指示UE重建PDN连接完成P-CSCF的容灾恢复。 
在EPC/IMS网络中主要网元故障后，VoLTE业务的恢复方式参见下表。 
故障类型|VoLTE主叫业务恢复方式|VoLTE被叫业务恢复方式
---|---|---
MME故障|MME故障后，UE的上行业务触发eNB重选可用的MME，UE在新MME重新附着并重建EPS承载，继而在IMS重新注册，VoLTE业务恢复。|MME故障后，UE的下行业务触发SGW重选可用的MME，触发UE重新附着并重建EPS承载，继而在IMS重新注册，VoLTE业务恢复。
SGW故障|SGW故障后，UE的上行业务触发MME指示UE恢复。恢复时，MME重选可用的SGW，重建EPS承载，继而实现UE在IMS重新注册，VoLTE业务恢复。|SGW故障后，UE的下行业务触发PGW通过可用的SGW通知MME触发UE恢复。同时MME感知SGW故障后扫描故障SGW中的UE，依次触发UE恢复。恢复时，MME重选可用的SGW，重建EPS承载，继而实现UE在IMS重新注册，VoLTE业务恢复。
PGW故障|PGW故障后，UE的上行业务触发MME指示UE恢复。恢复时，MME重选可用的PGW，重建EPS承载，继而实现UE在IMS重新注册，VoLTE业务恢复。|PGW故障后，MME扫描故障PGW中的UE，依次触发UE恢复。恢复时，MME重选可用的PGW，重建EPS承载，继而实现UE在IMS重新注册，VoLTE业务恢复。
P-CSCF故障|P-CSCF故障后，UE重新选择新的P-CSCF进行IMS注册，VoLTE业务恢复。|P-CSCF故障后，S-CSCF通知HSS，HSS向MME下发指示，MME触发UE恢复。恢复时，MME重建IMSPDN连接，UE从PGW获取新的P-CSCF地址进行IMS注册，VoLTE业务恢复。
CSFB业务容灾恢复
对于CSFB业务，如果SGs口出现故障或者MSC宕机，导致UE在重新附着、联合TAU之前，无法做被叫，此时需要能快速恢复SGs口连接从而恢复CSFB的被叫业务。 
在网络中主要网元故障后，CSFB业务的恢复方式参见下表。 
故障类型|CSFB主叫业务恢复方式|CSFB被叫业务恢复方式
---|---|---
MME故障|MME故障后，UE的上行业务触发eNB重选可用的MME，UE在新MME重新联合附着，完成在MSC注册，CSFB业务恢复。|MME故障后，UE的CS语音被叫业务会触发MSC/VLR在MME POOL中重选可用的MME下发寻呼。MME触发UE重新联合附着，完成在MSC注册，CSFB业务恢复。
MSC故障（包括SGs口故障）|MSC故障（包括SGs口故障）后，UE的上行业务触发MME选择正常SGs接口的MSC，UE在新MSC重新注册，CSFB业务恢复。|MSC故障（包括SGs口故障）后，UE的CS语音被叫业务会触发备份MSC/VLR向MME下发无LAI寻呼。MME触发UE的IMSI重新附着，完成在MSC注册，CSFB业务恢复。同时，MME自动监控SGs接口，一旦发现SGs接口异常，触发异常SGs接口上注册的UE重新注册到正常SGs接口的MSC上，CSFB业务恢复。
### 应用场景 
##### MME故障后的业务恢复 
MME发生故障或重启，该MME上的UE有下行的数据报文（例如：VoLTE业务终呼信令），SGW能够立即为UE重新选择可用的MME，通过新MME触发UE重新附着，完成EPS承载重建。 
MME发生故障或重启，该MME上的UE有CSFB的终呼业务，MSC/VLR能够立即选择其它可用MME下发寻呼，通过新MME触发UE重新联合附着，完成MSC注册和SGs连接恢复。 
##### SGW故障后的业务恢复 
SGW发生故障或重启，UE的下行业务触发PGW通过可用的SGW通知MME触发UE恢复。同时MME感知SGW故障后扫描故障SGW中的UE，依次触发UE恢复。恢复时，MME可选择触发UE重新附着或者触发UE重新选择SGW，完成EPS承载重建。 
##### PGW故障后的业务恢复 
PGW发生故障或重启，MME针对该PGW上的用户，主动触发UE重新附着或重建IMS
PDN连接，完成EPS承载重建。 
##### P-CSCF故障后的业务恢复 
P-CSCF发生故障或重启，P-CSCF采用基于HSS的方式恢复。MME根据HSS的指示，重建UE的IMS
PDN连接。UE从PGW获取新的P-CSCF地址后，进行IMS注册，完成IMS业务恢复。 
##### MSC故障后的CSFB业务恢复 
MSC发生故障或重启，UE的CS语音被叫业务由备份MSC/VLR向MME下发无LAI寻呼，触发UE的IMSI重新附着。同时MME发现MSC发生故障或重启后，扫描故障MSC中的UE，依次触发UE发起IMSI附着，注册到正常的MSC上，完成CSFB业务恢复。 
##### MSC/VLR手动卸载 
当发现某个MSC故障或者需要升级维护时，需要对该MSC上注册的UE进行迁移。MME提供网管动态管理命令，触发注册在该MSC的UE重新发起IMSI附着。 
### 客户收益 
受益方|受益描述
---|---
运营商|提高系统的可靠性和安全性。在部署了VoLTE的网络中，提高VoLTE业务的可靠性，大幅减少因网络故障对VoLTE业务的影响。
移动用户|网络故障后，VoLTE业务不受影响。
### 实现原理 
##### 涉及的网元 
语音容灾功能需要UE、MME、SGW、PGW、HSS、MSC/VLR的共同配合，各网元的主要作用参见下表。 
网元|作用
---|---
UE|接受MME的指示，重新附着、重选SGW或重建IMS PDN连接。
MME|SGW/PGW故障或重启后，MME能够主动触发UE重新附着、重选SGW或重建IMS PDN连接。其他MME故障或重启后，作为新选择的MME能够接受SGW的指示触发UE重新附着；能备份特定MME的UE动态位置信息，以便在寻呼用户时有效控制寻呼范围，
SGW|MME故障或重启后，能够保持PDN连接和承载上下文。在收到下行的数据报文时，可以立即选择一个可用的MME，发送PGWDownlink Triggering Notification消息给MME触发UE恢复。
PGW|SGW故障或重启后，能够保持PDN连接和承载上下文。在收到下行的数据报文时，可以通过其他可用的SGW，发送DownlinkData Notification消息给MME触发UE恢复。
HSS|P-CSCF故障后，能够接收S-CSCF的指示，通知MME触发UE恢复。
MSC/VLR|MME故障或重启后，能够在MME POOL中选择一个MME进行被叫业务。MSC/VLR故障或重启后，作为备用MSC/VLR能够下发无LAI寻呼。
##### 业务流程 
MME故障后的业务恢复
容灾数据备份当UE在MME上的位置信息发生变化时，MME将UE的位置信息备份到POOL内的特定MME。一旦某个MME发生故障，POOL内的其他MME可以从该MME的备份节点获取该MME上用户的位置信息。 
EPS业务恢复当SGW检测到MME故障或重启后，SGW需要保持PDN连接和承载上下文。一旦收到下行的数据报文时，SGW立即选择一个可用的备份MME，发送Downlink
Data Notification消息给MME。 备份MME收到消息后，根据消息中的IMSI以及备份的位置信息寻呼UE，触发UE重新附着，完成EPS承载重建。 
CSFB业务恢复MME故障后，当UE有CSFB被叫业务时，MSC/VLR在MME POOL中重选可用的MME下发寻呼，并在寻呼消息中携带CS业务恢复指示。MME收到寻呼消息后，尽管当前没有UE的上下文信息，但是判断寻呼消息中携带有CS业务恢复指示，则采用IMSI寻呼的方式，触发UE重新联合附着，完成业务恢复。IMSI寻呼时，MME可以利用寻呼消息中的LAC信息，或者是从故障MME的备份节点获取用户的位置信息来控制寻呼范围，从而避免全网寻呼。 
SGW故障后的业务恢复
当PGW检测到SGW故障或重启后，PGW需要保持PDN连接和承载上下文。一旦收到下行的数据报文时，PGW通过其他可用的SGW，发送Downlink
Data Notification消息给MME。MME触发UE发起业务请求，MME收到业务请求后重新选择可用的SGW，重建EPS承载。 
同时，当MME通过Echo消息或者Recovery信元检测到SGW故障或重启后，MME扫描该SGW上的用户，依次触发UE采用重选SGW或者重新附着的方式进行恢复，完成EPS承载重建。 
PGW故障后的业务恢复
当MME通过SGW发送的PGW Restart Notification消息感知到PGW故障或重启后，MME针对该PGW上的用户进行如下处理： 
如果UE的所有PDN连接对应的PGW均故障，则MME触发UE重新附着，重建EPS承载。 
如果UE仅IMS PDN连接对应的PGW故障，则MME触发UE重建IMS PDN连接。 
P-CSCF故障后的业务恢复
当S-CSCF发现P-CSCF故障或重启，终呼无法投递时，S-CSCF通知HSS，HSS向MME下发IDR消息，指示MME进行P-CSCF恢复。MME收到P-CSCF恢复指示后，指示UE重建IMS
PDN连接，在PDN重建过程中，UE从PGW获取到新的P-CSCF地址后，进行IMS注册。  
MSC故障后的CSFB业务恢复
被叫业务触发的恢复MSC发生故障或重启后，UE的CS语音被叫业务由备份MSC/VLR接管，备份MSC/VLR向MME下发无LAI寻呼。MME收到无LAI寻呼后，向UE发送IMSI
Detach消息，触发UE发起IMSI重新附着，完成可用MSC的重选和SGs口的重新注册。 
上行业务触发的恢复MSC发生故障或重启后，当UE发起TAU（包括周期性TAU）时，MME重选可用的MSC/VLR完成SGs口注册。当UE发起业务请求、扩展业务请求、SGs口短信起呼时，MME向UE发送IMSI
Detach，触发UE发起IMSI重新附着，完成可用MSC的重选和SGs口的重新注册。 
MME主动快速恢复MME接收到MSC/VLR的RESET消息，或者是检测到与MSC/VLR的链路全部中断，则主动触发该MSC/VLR的用户恢复。MME扫描故障MSC/VLR的UE，依次向UE发送IMSI
Detach消息，触发UE发起IMSI重新附着，完成可用MSC/VLR的重选和SGs口的重新注册。 小心！为了避免链路瞬断造成的误判，需要通过网管配置合理的局向状态不可达时长。只有当局向状态进入不可达的时长达到配置的阈值，才需要触发恢复。 
MSC/VLR手动卸载当人工发现某个MSC/VLR故障，或者某个MSC/VLR需要升级维护时，MME通过动态管理命令，对该MSC/VLR上注册的UE进行卸载。一旦命令被执行，MME扫描该MSC/VLR上的UE，依次向UE发送IMSI
Detach消息，触发UE发起IMSI重新附着，完成MSC/VLR重选。 说明：如果不希望UE重选时选择原来的MSC/VLR，可在MSC/VLR选择策略相关配置中，将该MSC/VLR权重暂时调整为0。  
### 系统影响 
##### 容灾恢复中 
一旦有一个网元发生故障或重启，该网元上的所有用户都有待恢复。这些用户的恢复过程，对POOL内的其他网元，带来了额外的业务负荷，所以POOL内的网元都需要有适当的冗余（一般情况下冗余1/N，N为POOL内节点数目），来保证容灾的业务接管。 
为了防止短时间内大量用户恢复造成的业务激增，需要MME在扫描恢复时，合理地控制单位时间内恢复的用户数目，既要避免对同时处理的正常业务造成过大的影响，也要避免恢复时间过长。 
按每秒每模块最快恢复40个用户、每模块5万用户需要恢复来计算，全部恢复需要约21分钟，触发恢复的业务负担增加不超过3%。 
##### 容灾准备中 
为了满足MME故障恢复时寻呼负荷的控制，POOL内的MME间需要实时的进行用户动态位置信息的备份，这将会增加一定的MME局间信令和业务负荷，但不超过1%。 
##### MME在无用户注册信息时的寻呼 
MME POOL组网中，如果用户所在的MME宕机，则MSC/VLR在MME
POOL中重选可用的MME下发寻呼。MME收到寻呼消息后，尽管当前没有UE的上下文信息，但是判断寻呼消息中携带有CS业务恢复指示，则采用IMSI寻呼的方式。IMSI寻呼时，MME可以利用寻呼消息中的LAC信息，或者是从故障MME的备份节点获取用户的位置信息来控制寻呼范围，而避免全网寻呼。 
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
业务|交互
---|---
本地资源回收|采用容灾业务恢复后，无需再使用本地资源回收。本地资源回收，是指SGW/PGW故障后，MME将相关的会话上下文资源予以回收，而不通知UE恢复业务。
### 遵循标准 
标准名称
---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS); Stage 3".
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network(E-UTRAN); S1 Application Protocol (S1AP)".
3GPP TS 29.274: "General Packet Radio Service (GPRS); EvolvedGPRS Tunnelling Protocol (eGTP) for EPS".
3GPP TS 29.272: " Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol".
3GPP TS 23.007: "Restoration procedures".
### 特性能力 
MME主动触发的UE恢复流程，最大支持每秒每模块100个用户。 
MME间的备份关系可支持链式备份和集中备份。 
### 可获得性 
##### 版本要求及变更记录 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
##### License要求 
该特性需要申请了下表中的License许可后，运营商才能获得该特性的服务。 
License ID|License控制值|License描述
---|---|---
7049|支持|MME支持MME容灾故障恢复功能
7058|支持|MME支持SGW容灾故障恢复功能
7059|支持|MME支持PGW容灾故障恢复功能
7052|支持|MME支持P-CSCF恢复功能
7056|支持|MME支持SGs口主动恢复
##### 对其他网元的要求 
需要SGW支持容灾故障恢复的相关功能，支持3GPP TS 23.007中描述的“网络侧触发的业务恢复”功能。 
需要PGW支持容灾故障恢复的相关功能，支持3GPP TS 23.007中描述的“网络侧触发的业务恢复”功能。 
需要MSC/VLR支持容灾故障恢复的相关功能，支持3GPP
TS 23.007中描述的“网络侧触发的业务恢复”功能。 
需要HSS支持3GPP TS 23.380中描述的“P-CSCF恢复”功能。 
由于POOL内MME间传递UE动态位置信息备份的接口是私有接口，所以要求POOL内的MME由同一厂家提供。 
UE|eNodeB|SGW|PGW|HSS
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
##### 工程规划要求 
语音容灾对组网无特殊要求。 
MME间采用S10接口的GTP-C地址进行通信以实现UE的动态位置信息备份。 
### O&M相关 
##### 命令 
配置项表2  新增配置项配置项命令容灾恢复配置SET SERVRSTOCFGSHOW SERVRSTOCFGADD POOLBAKMMECFGSET POOLBAKMMECFGDEL POOLBAKMMECFGSHOW POOLBAKMMECFG表3  修改配置项配置项命令修改的参数Support Feature管理ADD SUPFEATURESupport Feature 2SET SUPFEATURESupport Feature 2SHOW GLOBAL SUPFEATURESupport Feature 2SGs口VLR局向配置ADD VLROFFICE局向属性SET VLROFFICE局向属性SHOW VLROFFICE局向属性 
软件参数表4  新增软件参数软件参数ID软件参数名称786732支持MME容灾的未知备份节点的备份数据查询786733查询他局备份数据等待时间262446支持SMS Only用户的SGs口主动恢复 
动态管理查询备份用户信息在备份MME上，通过SHOW BAKDATAPOOL命令，可根据UE的IMSI，查询备份的动态位置信息，命令示例如下： SHOW BAKDATAPOOL:IMSI="460119990022003";查询结果示例如下：Result	
---------
Success	
---------
1 Record(s)

Tracking Area	
----------------
460-11-8801	
460-11-8803	
460-11-8802	
----------------
3 Record(s)备份数据手动清空在备用MME上，通过CLEAR BAKDATA命令，可将所有备份的动态位置信息清除掉。备份数据手动同步在主用MME上，通过SYN BAKDATA命令，可将所有用户的动态位置信息同步给备份MME。取消备份数据同步在主用MME上，通过CANCEL BAKDATA SYN命令，可取消正在进行的备份数据手动同步命令。 VLR局向手动恢复当需要迁移某个或多个VLR局向的用户时，通过RESTORE VLR命令可进行VLR局向手动恢复。取消VLR局向手动恢复当需要终止正在执行的VLR局向手动恢复命令时，通过CANCEL
RESTORE VLR命令，可取消VLR局向手动恢复。 
##### 性能统计 
该特性不涉及计数器的变化。 
##### 告警和通知 
该特性不涉及告警/通知消息的变化。 
##### 业务观察/失败观察 
该特性不涉及业务观察/失败观察的变化。 
##### 话单与计费 
该特性不涉及话单与计费的变化。 
## 特性配置 
## 特性配置 
### 配置说明 
通过配置实现语音容灾功能。 
### 配置前提 
MME基础配置已经完成，即用户可以在MME附着并且该用户的语音承载已建立。 
容灾相关License功能项已经设置为支持，包括：MME支持MME容灾故障恢复功能、MME支持SGW容灾故障恢复功能、MME支持PGW容灾故障恢复功能、MME支持P-CSCF恢复功能、MME支持SGs口主动恢复。 
需要规划POOL内MME间的动态位置信息备份关系。比如POOL内有四个MME：MME1、MME2、MME3、MME4，链式备份的备份关系为MME1的备份为MME2、MME2的备份为MME3、MME3的备份为MME4、MME4的备份为MME1。 
需要配置与MME对接的VLR POOL以及POOL内各个VLR的权重和优先级，以便MME进行VLR选择。 
### 配置过程 
执行命令[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)，分别开启支持SGW容灾恢复、支持PGW容灾恢复、支持MME容灾恢复、支持P-CSCF容灾恢复、支持PGW触发的SGW恢复的开关。
对于已经配置Feature ID的HSS局向，执行命令[SET SUPFEATURE](../../MMESGSN\zh-CN\mml\1262601.html)，配置支持P-CSCF Restoration能力。
执行命令[SET VLROFFICE](../../MMESGSN\zh-CN\mml\1261262.html)，配置VLR局向支持故障后的主动恢复的开关。
执行命令[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)，配置合理的容灾恢复速率和GW容灾寻呼范围。
执行命令[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)，配置合理的采用SGW重选方式的故障恢复时长。
执行命令[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)，配置本MME的备份节点IP。
执行命令[ADD POOLBAKMMECFG](../../MMESGSN\zh-CN\mml\1260774.html)，配置POOL内其它MME的IP及其备份节点IP。
执行命令[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)，配置合理的动态位置信息备份速率。
执行命令[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html)，根据需要开启“支持MME容灾的未知备份节点的备份数据查询”功能，并设置合理的“查询他局备份数据等待时间”。
执行命令[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)，配置合理的备份数据老化时长。
执行命令[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)，配置合理的VLR局向故障恢复检测时长。
执行命令[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html)，开启“支持SMS Only用户的SGs口主动恢复”功能。
### 配置实例 
##### MME容灾配置 
在MME容灾配置之前，应当完成相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
支持MME容灾恢复|支持
备份MME的IP地址|10.10.10.10（本局IP地址为10.10.10.13）
POOL内其他MME的备份关系|主用节点：10.10.10.10，备份节点：10.10.10.11；主用节点：10.10.10.11，备份节点：10.10.10.12；主用节点：10.10.10.12，备份节点：10.10.10.13；
数据备份消息发送频率|1000毫秒
数据备份消息包大小（KB）|4KB
支持MME容灾的未知备份节点的备份数据查询|支持
查询他局备份数据等待时间|3秒
根据规划，进行如下配置。 
配置MME容灾恢复参数：设置支持MME容灾恢复功能，设置备份MME的IP地址为10.10.10.10，设置数据备份消息发送频率为1000毫秒，数据备份消息包大小为4KB，命令如下： 
[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html):MMERSTOFLAG="YES",BAKMMEIP="10.10.10.10",BAKRATE=1000,BAKSIZE=4
配置POOL内MME间备份关系，命令如下： 
[ADD POOLBAKMMECFG](../../MMESGSN\zh-CN\mml\1260774.html):MMEIP="10.10.10.10",BAKMMEIP="10.10.10.11",NAME="MME1"
[ADD POOLBAKMMECFG](../../MMESGSN\zh-CN\mml\1260774.html):MMEIP="10.10.10.11",BAKMMEIP="10.10.10.12",NAME="MME2"
[ADD POOLBAKMMECFG](../../MMESGSN\zh-CN\mml\1260774.html):MMEIP="10.10.10.12",BAKMMEIP="10.10.10.13",NAME="MME3"
配置未知备份节点的相关软件参数，命令如下： 
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=786732,PARAVALUE=1
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=786733,PARAVALUE=3
##### SGW容灾配置 
在SGW容灾配置之前，应当完成相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
支持SGW容灾恢复|支持
支持PGW触发的SGW恢复|支持
容灾恢复扫描速率|每模块每百毫秒40个用户
容灾业务恢复速率|每模块每百毫秒5个用户
GW容灾恢复时IMSI寻呼范围|TA List
采用SGW重选方式的故障恢复时长|10分钟
根据规划，进行如下配置。 
[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html):SGWRSTOFLAG="YES",PGWTRIGSGWRSTO="YES",RSTOSCANRATE=40,RSTORATE=5,GWRSTOPGAREA="TALIST",SGWRELOCTIME=10
##### PGW容灾配置 
在PGW容灾配置之前，应当完成相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
支持PGW容灾恢复|支持
容灾恢复扫描速率|每模块每百毫秒40个用户
容灾业务恢复速率|每模块每百毫秒5个用户
GW容灾恢复时IMSI寻呼范围|TA List
IMS APN NI|IMS
根据规划，进行如下配置。 
配置PGW容灾恢复参数，命令如下： 
[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html):PGWRSTOFLAG="YES",RSTOSCANRATE=40,RSTORATE=5,GWRSTOPGAREA="TAList"
配置IMS APN NI，命令如下： 
[ADD IMS APN](../../MMESGSN\zh-CN\mml\1261784.html):APNNAME="IMS"
##### P-CSCF容灾配置 
在P-CSCF容灾配置之前，应当完成相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
支持P-CSCF容灾恢复|支持
HSS局向支持P-CSCF Restoration能力|支持
根据规划，分两种情况进行如下配置。 
已配置Feature ID（值为1）的HSS开启P-CSCF Restoration的场景打开支持P-CSCF容灾恢复功能开关，命令如下：SET SERVRSTOCFG: PCSCFRSTOFLAG="YES"打开HSS局向支持P-CSCF Restoration能力开关，命令如下：SET SUPFEATURE:FEATUREID=1,SUPFEATURE2="PCSCF" 
未配置Feature ID的HSS开启P-CSCF Restoration的场景打开支持P-CSCF容灾恢复功能开关，命令如下：SET SERVRSTOCFG: PCSCFRSTOFLAG="YES"新增Support Feature配置，支持P-CSCF Restoration，命令如下：ADD SUPFEATURE:FEATUREID=1,SUPFEATURE="TRACE"&"TADS"&"STALOC",SUPFEATURE2="PCSCF" 说明：注意要把全局支持的Support Feature配置进去，可以使用SHOW GLOBAL SUPFEATURE命令查询全局支持的Support Feature。HSS的Diameter邻接局向（ID为1）配置引用Support Feature配置中的Feature ID参数，命令如下：SET DIAMADJ:ADJID=1,SUPFEATUREID=1 
##### SGs口快速恢复配置 
在SGs口快速恢复配置之前，应当完成VLR局向和VLR POOL的相关配置，并完成SGs口快速恢复相关数据规划，数据规划示例参见下表。 
参数名称|取值举例
---|---
VLR局向标识|1、2、3
VLR局向属性|支持故障后主动恢复
容灾恢复扫描速率|每模块每百毫秒40个用户
容灾业务恢复速率|每模块每百毫秒5个用户
VLR局向故障恢复检测时长|2分钟
支持SMS Only用户的SGs口主动恢复|支持
根据规划，进行如下配置。 
开启VLR POOL内各个VLR局向支持故障后的主动恢复的开关，命令如下： 
[SET VLROFFICE](../../MMESGSN\zh-CN\mml\1261262.html):VLROFFICEID=1,ATTR="ASSRES"
[SET VLROFFICE](../../MMESGSN\zh-CN\mml\1261262.html):VLROFFICEID=2,ATTR="ASSRES"
[SET VLROFFICE](../../MMESGSN\zh-CN\mml\1261262.html):VLROFFICEID=3,ATTR="ASSRES"
配置SGs口快速恢复参数，命令如下： 
[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html):RSTOSCANRATE=40,RSTORATE=5,VLRDETCTIME=2
配置支持SMS Only用户SGs口主动恢复，命令如下： 
[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262446,PARAVALUE=1
### 调整特性 
POOL内MME间备份关系调整：当因为POOL内增加或减少MME节点等原因，导致需要调整POOL内MME间备份关系，可参考配置流程中的步骤6和步骤7予以调整。 
备份速率调整：一般无需特别调整备份速率，如需调整可参考配置流程中的步骤8。 
恢复速率调整：一般无需特别调整恢复速率，特殊情况下，可根据系统的负荷情况加快或减慢恢复速率，调整方法可参考配置流程中的步骤4。 
采用SGW重选方式的故障恢复时长调整：需要根据PGW发现SGW故障后，保留PDN连接的时间来调整，保证采用SGW重选方式的故障恢复时，PGW仍保留有原PDN连接。 
### 测试用例 
##### MME容灾恢复 
测试项目|MME容灾恢复
---|---
测试目的|测试MME收到SGW发送的DDN消息后，能够触发用户重新附着。
预置条件|EPC网络中各网元运行正常。POOL内有三个MME网元。
测试过程|用户附着后，处于IDLE态。用户附着的MME故障。网络侧有下行数据报文。
通过准则|用户附着成功，能够在备份的MME上查询到该用户的备份数据。新的MME收到SGW发送的DDN消息后，获取用户的位置信息，寻呼用户。用户重新附着成功。
测试结果|—
##### SGW容灾恢复-MME发起的重新附着 
测试项目|SGW容灾恢复-MME发起的重新附着
---|---
测试目的|测试SGW故障后MME能够主动触发用户重新附着。
预置条件|EPC网络中各网元运行正常。采用SGW重选方式的故障恢复时长设置为0分钟。
测试过程|用户附着后，处于IDLE态。用户所在的SGW故障。
通过准则|用户附着成功。一段时间后，MME寻呼用户。用户重新附着成功。
测试结果|—
##### SGW容灾恢复-MME发起的重选SGW 
测试项目|SGW容灾恢复-MME发起的重选SGW
---|---
测试目的|测试SGW故障后MME能够主动触发用户重选SGW。
预置条件|EPC网络中各网元运行正常。采用SGW重选方式的故障恢复时长设置为2分钟。
测试过程|用户附着后，处于IDLE态。用户所在的SGW故障。
通过准则|用户附着成功。SGW故障，2分钟内用户都会重选SGW 。
测试结果|—
##### SGW容灾恢复- PGW触发的恢复 
测试项目|SGW容灾恢复- PGW触发的恢复
---|---
测试目的|测试SGW故障后PGW主动触发恢复。
预置条件|EPC网络中各网元运行正常。支持PGW触发的SGW恢复的开关。
测试过程|用户附着后，处于IDLE态。PGW重选一个正常的SGW，MME收到SGW发送的PGW Downlink Triggering Notification消息，消息中携带此用户的IMSI。
通过准则|MME返回成功的PGW Downlink Triggering Answer消息，不携带MMEID。用户处于IDLE态，MME寻呼UE。MME收到UE的业务请求后，重选SGW。
测试结果|—
##### PGW容灾恢复 
测试项目|PGW容灾恢复
---|---
测试目的|测试用户仅IMS PDN连接对应的PGW故障后，MME能够触发用户重建IMS PDN连接。
预置条件|EPC网络中各网元运行正常。
测试过程|用户附着时创建数据PDN连接，再创建IMS PDN连接。用户IMS PDN连接对应的PGW故障。
通过准则|用户附着成功，建立两个PDN连接。一段时间后，MME指示UE重建IMS PDN连接。用户重建IMS PDN连接成功。
测试结果|—
##### P-CSCF容灾恢复 
测试项目|P-CSCF容灾恢复
---|---
测试目的|测试MME根据HSS的IDR指示，重建IMS PDN，进行P-CSCF恢复。
预置条件|EPC网络中各网元运行正常。MME的License中支持P-CSCF容灾恢复。支持P-CSCF容灾恢复的开关打开。HSS局向关联的Feature ID配置支持P-CSCF Restoration能力。MME支持Feature协商。
测试过程|用户附着时，HSS返回的ULA消息指示支持P-CSCF恢复。用户建立普通PDN，再建立一个IMS PDN，并建立专有承载。用户处于连接态，收到HSS发送的IDR消息中携带P-CSCF恢复flag。
通过准则|MME收到IDR后，返回成功的IDA，发起IMS PDN去连接，携带NAS原因值为“reactivation requested”，同时通知SGW删除会话。
测试结果|—
##### SGs口主动恢复 
测试项目|SGs口主动恢复
---|---
测试目的|测试VLR故障时，能触发SGs口的主动恢复。
预置条件|MME的License中支持SGs口主动恢复。SGs口的VLR局向支持故障后的主动恢复。VLR局向都可达。VLR局向故障恢复检测时长为2分钟。容灾业务扫描速率为40/100ms。容灾业务恢复速率为5/100ms。
测试过程|用户在VLR上联合附着，处于连接态。VLR不可达时间达到阈值2分钟。MME发送IMSI Detach消息后，收到UE发出的Detach Accept消息和联合TAU消息。
通过准则|VLR不可达两分钟后直接进行IMSI Detach，并清除SGs状态。MME收到Detach Accept后，不主动释放S1连接，收到联合TAU后，重选VLR发起位置更新。
测试结果|—
### 常见问题处理 
无。 
# ZUF-78-12-010 VoLTE容灾之SGW故障控制 
在EPC网络，SGW通过资源池进行容灾。一旦UE重附着，eNodeB重选一个可用MME，MME选择可用SGW和PGW。当EPC网元容灾后，可通过这种方式恢复业务。对于VoLTE业务，UE需实时在线以进行语音终呼，因此SGW需能够在故障发生后触发UE进行重附着。 
当SGW怠机，UE的上行业务触发MME指示UE恢复。在恢复过程中，MME重新选择可用SGW并重建EPS承载。UE重新注册在IMS上。VoLTE业务恢复正常。 
# ZUF-78-12-011 VoLTE容灾之PGW故障控制 
在EPC网络，PGW通过资源池进行容灾。一旦UE重附着，eNodeB重选一个可用MME，MME选择可用SGW和PGW。当EPC网元容灾后，可通过这种方式恢复业务。对于VoLTE业务，UE需实时在线以进行语音终呼，因此PGW需能在故障发生后触发UE进行重附着。 
当SGW怠机，UE的上行业务触发MME指示UE恢复。在恢复过程中，MME重新选择可用PGW并重建EPS承载。UE重新注册在IMS上。VoLTE业务恢复正常。 
# ZUF-78-12-012 VoLTE容灾之P-CSCF故障控制 
如果P-CSCF部署在资源池中，当UE重建IMS PDN连接时，PGW能重选可用P-CSCF。这样当P-CSCF发生故障时，业务仍可恢复。对于VoLTE业务，为保障用户能始终接收到语音呼叫，UE应保持在线状态。因此，如果P-CSCF发生故障，UE可被立即触发以重建IMS
PDN连接。 
如果P-CSCF怠机，UE重选新P-CSCF以注册到IMS。VoLTE业务恢复正常。 
# ZUF-78-12-013 VoLTE故障定位手段增强 
## 概述 
本特性为语音呼叫提供性能统计，包括VoLTE和SRVCC。 
## 收益 
本特性可用于监控VoLTE质量。 
## 描述 
为增强对VoLTE和SRVCC的质量监控，提供以下手段： 
以QCI为目标的流程测量，包括承载激活、修改和去激活、TAU、业务请求、切换、S1释放和ERAB释放等。 
以APN为目标的流程测量，包括承载激活、修改和去激活。 
以QCI为目标并用于不同网元的流程测量，包括承载激活和修改，TAU、业务请求和切换等。 
以QCI为目标的测量，包括承载数量、建立承载数量和删除承载数量。 
以OCI、TA、APN和域组合为目标以及用于各种网元的测量，包括承载激活、修改和去激活。 
用于VoLTE和SRVCC流程的失败统计。 
# ZUF-78-12-014 内嵌IWS功能 
## 特性描述 
## 特性描述 
### 术语 
术语|含义
---|---
CDMA 1xRTT|CDMA 1xRTT是CDMA的第一阶段，支持最高153.6kbps数据速率。CDMA 1xRTT可以提供语音业务和数据业务。
1xCSFB|CDMA 1xRTT CSFB（简称1xCSFB）是基础的CS fallback to1xRTT功能。当UE需要回落到CDMA 1xRTT网络进行语音业务时，eNodeB将UE重定向到CDMA 1xRTT网络。
e1xCSFB|CDMA 1xRTT eCSFB（简称e1xCSFB）是增强的CS fallback to1xRTT功能。当UE需要回落到CDMA 1xRTT网络进行语音业务时，eNodeB先通过MME的S102接口向目标IWS请求分配目标CDMA空口资源，建立A1/A2链路，向UE下发切换请求（切换请求携带目标侧分配的CDMA空口资源）。UE根据eNodeB的指示从LTE网络切换到1xRTT网络，完成1xRTT网络的接入。相对CDMA 1xRTT CSFB，CDMA 1xRTT eCSFB的切换时延更短，用户体验较好。
S102接口|在CDMA 1xRTT CSFB特性中，最主要的接口是S102接口，是MME和IWS之间的接口，主要用来处理EPS和CDMA网络之间的移动性管理和语音、短消息业务、寻呼流程。
### 描述 
##### 定义 
对于支持1xRTT和E-UTRAN的双模终端，网络可为终端提供e1xCSFB、E-UTRAN to
1xRTT的SRVCC和E-UTRAN to 1xRTT的PS业务。
e1xCSFB从LTE网络回落到CDMA 2000网络，完成语音起呼或终呼的业务，这样在LTE网络无法提供VoLTE能力的区域，利用原有CDAM
2000网络资源，完成语音呼叫。 
E-UTRAN to 1xRTT的SRVCC用户在LTE网络下进行VoLTE语音呼叫，用户移动进入1xRTT覆盖区域，语音切换到1xRTT网络。 
以上2个功能均需要IWS网元，实现1xRTT网络与E-UTRAN之间的互操作。
CDMA 1xRTT CSFB语音业务，是一种在不引入IMS的情况下，利用现有的1xRTT网络实现语音通话的一种语音解决方案。该方案在用户发起语音业务时，由EPS网络指示用户回落到目标1xRTT网络之后，再发起语音呼叫。  
### 应用场景 
在LTE做热点覆盖的初期，由于LTE中不存在CS域的概念，为了保证UE能够进行语音业务并且能够享受到LTE的PS业务引入了CDMA
1xRTT CSFB业务，在进行语音业务的时候保证UE回落到目标1xRTT网络。 
### 客户收益 
收益者|收益描述
---|---
运营商|CDMA 1xRTT CSFB语音方案满足在部署LTE初期就提供语音服务但同时又不愿意过早部署IMS的运营商的需求。最大化利用现有1xRTT网络的覆盖和业务质量等资源，保护运营商的投资利益最大化。
终端用户|终端用户可以使用一个终端享用LTE高速数据业务和1xRTT成熟语音业务。
### 实现原理 
##### 系统架构 
IWS是实现是1xRTT网络与E-UTRAN互操作功能的中间逻辑实体。 
CDMA网络内的IWS设备通过S102接口和EPS网络的MME通讯。为了支持CDMA 1xRTT CSFB语音业务，MME需要和IWS网元之间收发1xRTT封装消息，虚线上方为CDMA网络，虚线下方为EPS网络，如[图1](ZUF-78-12-014-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84-DD5FBCE0)所示。
图1  系统架构
[]images/ZUF-78-12-014-%E7%BB%84%E7%BD%91%E5%9B%BE.png)
IWS可以作为独立网元，也可作为MME的一个内嵌功能。 
独立设置IWS为独立网元，但其往往放置于核心网机房而集中设置。IWS和MME一般呈现的是一对多的组网关系；IWS和MSCe一般呈现的是一对一或者多对一的组网关系。 
内嵌MMEIWS同MME一起放置于核心网机房。IWS和MSCe一般呈现的是一对一或者多对一的组网关系。 
IWS可以连接一个或多个MME，向MME发送消息时使用保存的MME IP地址，不需要选择MME，IWS连接一个或多个MME时，IWS无配置差异。 
IWS基于用户消息中CELLID来选择MSC，IWS与MSC之间的组网分为无容灾、主备和负荷分担三种方式，参见[表1](ZUF-78-12-014-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__MME-MSC%E7%BB%84%E7%BD%91MSC%E5%AE%B9%E7%81%BE%E6%96%B9%E5%BC%8F%E6%AF%94%E8%BE%83-DD5FC2B9)。
组网方式|IWS选择
---|---
无容灾方式|一个CELLID选择一个MSC；
主备方式|一个CELLID选择一对主用MSC；一个MSC宕机，可由备用MSC接管；
负荷分担方式|一个CELLID选择多个MSC，其中MSC可具有不同的能力，IWS基于MSC能力分配用户；MSC宕机时，可由其他MSC接管；
无容灾方式图2  无容灾方式 
主备组网方式图3  主备组网方式 
负荷分担方式图4  负荷分担方式 
负荷分担方式 
##### 各网元作用 
网元名称|网元作用
---|---
UE|需要支持1xRTT和E-UTRAN双模，在E-UTRAN下发起回落到1xRTT的语音呼叫。
eNodeB|eNodeB支持DOWNLINK S1 CDMA2000 TUNNELING和UPLINK S1 CDMA2000 TUNNELING消息，eNodeB支持通知UE进行1xCSFB回落。
MME|接收UPLINKS1 CDMA2000 TUNNELING消息，提取其中内容封装在S102消息中发送给IWS。接收IWS下发的S102消息，提取其中内容封装在DOWNLINKS1 CDMA2000 TUNNELING消息中发送给IWS。记录用户选择的IWS的IP地址。
IWS|接收MME发送的S102消息，提取其中1xRTT层3信令，转换为A1消息发送给MSC从MSC接收A1消息，构造1xRTT层3信令，封装在S102消息中发送给MME。记录用户所在的MME的IP地址。
MSC|MSC按照标准的CDMA2000信令流程处理，但不进行承载资源协商，
##### 协议栈 
IWS一方面使用S102接口和MME通信，作为信令隧道终点，接收来自UE的或向UE发送封装的3GPP2
1xRTT信令消息；另一方面，使用A1接口，模拟1x BSC与MSC对接。 
IWS的协议栈如[图5](ZUF-78-12-014-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842497__IWS%E7%9A%84%E5%8D%8F%E8%AE%AE%E6%A0%88-DD3C7F25)所示。
图5  IWS的协议栈
[]images/ZUF-78-12-014-IWS%E7%9A%84%E5%8D%8F%E8%AE%AE%E6%A0%88.png)
IWS网元相关的协议参见下表。 
协议|作用
---|---
IP|IWS与MME之间使用IP物理连接方式。
UDP|IWS与MME之间使用UDP协议传输，采用固定端口23272
S102|IWS与MME之间的S102接口协议，遵循3GPP29.277协议。
GCSNA|IWS与UE之间的协议，用于封装1x层3空口信令，替代原1xRTT空中接口作用，遵循3GPP2C.S0097协议。
1X Layer3|IWS与UE之间的协议，等同于原1xRTT的层3空口信令，遵循3GPP2C.S0005协议
##### 本网元实现 
IWS的功能
消息翻译1x空口信令消息和IOS A1/A1p消息间的翻译，其中IOS A1/A1p消息是与MSC之间收发，1x空口信令消息是通过与MME之间的S102接口收发。 
MME地址存储保存用户所在MME的IP地址，用于发送下行消息时查找MME。 
MSC选择基于消息中CELLID，为用户选择MSC。 
增强型1xCSFB语音起呼
用户尝试语音起呼，UE发送Extended Service Request消息通知到MME，其中指示用户进行1xCSFB。 
MME发送Ue Init Context Setup Request到eNodeB，指示为CSFB回落，eNodeB通知UE回落到CS域。 
UE构造1xRTT的语音起呼消息，通过eNodeB发送给MME网元。 
MME将此语音起呼消息转发给IWS。 
IWS构造标准的A1接口Cm Service Request，MSC与IWS交互完成语音呼叫建立的信令流程，IWS构造Handoff
Required消息发送到MSC，触发切换流程，MSC下发Handoff Command到IWS。 
IWS收到Handoff Command消息，转换为1xRTT的切换命令消息发送给MME。 
MME将切换命令透传到UE，通知UE执行切换。UE切换到1xRTT网络，在1xRTT网络下进行语音业务。 
E-UTRAN to 1xRTT SRVCC业务
用户在LTE网络下进行语音呼叫，移动进入1xRTT网络，UE构造1xRTT信令通过eNodeB发送给MME。 
MME将1xRTT信令通过S102接口转发给IWS。 
IWS构造A1口语音起呼消息发送到MSC，与MSC交互完成语音呼叫建立的信令流程，IWS触发切换请求通知MSC，MSC下发切换命令到IWS。 
IWS将切换命令消息通过S102接口发送到MME。 
MME将切换命令通过eNodeB透传给UE。 
UE执行切换，从E-UTRAN切换到1xRTT网络，继续在1xRTT网络下进行语音业务。 
##### 业务流程 
通过LTE完成到CDMA2000的登记/去登记
图6  通过LTE完成到CDMA2000网络的登记/去登记
[]images/ZUF-78-12-014-%E9%80%9A%E8%BF%87LTE%E5%AE%8C%E6%88%90%E5%88%B0CDMA%E7%9A%84%E7%99%BB%E8%AE%B0.png)
UE附着在LTE网络中。 
UE发起到CDMA2000网络的登记。 
如用户处于IDLE，UE先发送Service Request完成S1连接的建立。 
建立S1连接后。 
UE通过eNodeB上报UL S1 CDMA2000 Tunneling消息，其中封装1x登记消息。 
MME提取其中的Cell ID，查表获得对应的S102局向 IP地址，发送A21-1xAir Interface Signaling消息。 
IWS返回A21-1x Air Ack消息，表面之前A21消息已收到。 
IWS构造A1口Location Update Request消息发送消息到MSC。 
MSC完成对UE的登记，返回Location Update Accept响应消息。 
IWS从MSC收到登记接受。 
MME通过eNodeB将登记响应发送到UE。 
MME向IWS发送A21-1x Air Ack消息，表面之前A21消息已收到。 
IWS完成登记流程，触发释放A1口流程，向MSC发送Clear Request消息。 
MSC返回Clear Command消息。 
IWS返回Clear Complete消息。 
普通型1xCSFB语音起呼
图7  普通型1xCSFB语音起呼
[]images/ZUF-78-12-014-%E6%99%AE%E9%80%9A%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E7%BB%88%E5%91%BC.png)
UE附着在LTE网络和1xRTT网络中。 
MSC向IWS发起对用户的语音寻呼。 
IWS封装此寻呼消息在A21-1xAir Interface Signaling消息中通知到MME。 
MME返回A21-1x Ack指示之前A21消息已接收到。 
如用户处于IDLE态，MME对用户寻呼 
寻呼成功用户后，再下发DL S1 CDMA2000 Tunnelling消息，其中封装1xRTT的语音寻呼消息。如用户处于连接态则直接下发。 
用户发起回落流程。 
UE在1xRTT网络发送寻呼响应，建立语音呼叫。 
普通型1xCSFB语音终呼
图8  普通型1xCSFB语音终呼
[]images/ZUF-78-12-014-%E6%99%AE%E9%80%9A%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E7%BB%88%E5%91%BC(%E9%87%8D%E7%94%A81).png)
UE附着在LTE网络和1xRTT网络中。 
MSC向IWS发起对用户的语音寻呼。 
IWS封装此寻呼消息在A21-1xAir Interface Signaling消息中通知到MME。 
MME返回A21-1x Ack指示之前A21消息已接收到。 
如用户处于IDLE态，MME对用户寻呼。 
寻呼成功用户后，再下发DL S1 CDMA2000 Tunnelling消息，其中封装1xRTT的语音寻呼消息。如用户处于连接态则直接下发。 
用户发起回落流程。 
UE在1xRTT网络发送寻呼响应，建立语音呼叫。 
增强型1xCSFB语音起呼
图9  增强型1xCSFB语音起呼
[]images/ZUF-78-12-014-%E5%A2%9E%E5%BC%BA%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E8%B5%B7%E5%91%BC.png)
UE附着在LTE网络和1xRTT网络中。 
用户发起Extended Service Request消息，其中指示1xCSFB回落。 
MME下发UE Context Modification Request通知eNodeB，由eNodeB通知用户回落到1x
RTT。eNodeB返回UE Context Modification Respond消息，指示UE已接受回落请求。 
UE支持增强型CSFB，先构造1xRTT语音起呼消息通过eNodeB上报给MME。 
MME将1xRTT语音起呼消息封装在A21-1xAir Interface Signaling消息中发送给IWS。 
IWS返回A21-1xAir Ack指示之前A21消息已接收到。 
IWS构造Cm Service Request消息发送给MSC。 
MSC检查用户合法性后，对用户向IWS下发Assign Request消息。 
IWS直接返回Assign Complete消息。 
IWS构造Handoff Required消息发送给MSC，触发切换流程。 
MSC查找到目标BSC完成交互后，向IWS下发Handoff Command消息。 
IWS将切换命令封装在A21-1x Air Interface Signaling消息中发送给MME。 
MME返回A21-1xAir Ack指示之前A21消息已接收到。 
MME通过S1信令将切换命令下发给eNodeB。 
eNodeB通知UE开始切换。 
UE进入1xRTT下继续进行语音呼叫。 
增强型1xCSFB语音终呼
图10  增强型1xCSFB语音终呼
[]images/ZUF-78-12-014-%E5%A2%9E%E5%BC%BA%E5%9E%8B1xCSFB%E8%AF%AD%E9%9F%B3%E7%BB%88%E5%91%BC.png)
UE附着在LTE网络和1xRTT网络中。 
MSC向IWS发起对用户的语音寻呼。 
IWS封装此寻呼消息在A21-1xAir Interface Signaling消息中通知到MME。 
MME返回A21-1x Ack指示之前A21消息已接收到。 
如用户处于IDLE态，MME对用户寻呼。 
寻呼成功用户后，再下发DL S1 CDMA2000 Tunnelling消息，其中封装1xRTT的语音寻呼消息。如用户处于连接态则直接下发。 
用户发起Extended Service Request消息，其中指示1xCSFB回落。 
MME下发UE Context Modification Request通知eNodeB，由eNodeB通知用户回落到1x
RTT。eNodeB返回UE Context Modification Respond消息，指示UE已接受回落请求。 
UE支持增强型CSFB，先构造1xRTT语音起呼消息通过eNodeB上报给MME。 
MME将1xRTT语音起呼消息封装在A21-1xAir Interface Signaling消息中发送给IWS。 
IWS返回A21-1xAir Ack指示之前A21消息已接收到。 
IWS构造Cm Service Request消息发送给MSC。 
MSC检查用户合法性后，对用户向IWS下发Assign Request消息。 
IWS直接返回Assign Complete消息。 
IWS构造Handoff Required消息发送给MSC，触发切换流程。 
MSC查找到目标BSC完成交互后，向IWS下发Handoff Command消息。 
IWS将切换命令封装在A21-1x Air Interface Signaling消息中发送给MME。 
MME返回A21-1xAir Ack指示之前A21消息已接收到。 
MME通过S1信令将切换命令下发给eNodeB。 
eNodeB通知UE开始切换。 
UE进入1xRTT下继续进行语音呼叫。 
短信起呼
图11  短信起呼
[]images/ZUF-78-12-014-%E7%9F%AD%E4%BF%A1%E8%B5%B7%E5%91%BC.png)
UE附着在LTE网络和1xRTT网络中。 
UE发出短信，如UE当前为IDLE态，先建立S1连接。 
eNodeB向MME发送UL S1 CDMA2000 Tunneling，其中封装1xRTT短信信令。 
MME将1xRTT短信信令封装在A21-1xAir Interface Signaling消息中发送给IWS。 
IWS返回A21-1x Ack指示之前A21消息已接收到。 
IWS构造ADDS Transfer消息发送给MSC。 
MSC返回ADDS Page消息。 
IWS将构造短信下行信令封装在A21-1xAir Interface Signaling消息中发送给IWS。 
MME将短信下行信令封装在DL S1 CDMA2000 Tunneling消息中发送给eNodeB，eNodeB通知到UE。 
MME返回A21-1x Ack指示之前A21消息已接收到。 
IWS构造ADDS Page Ack消息发送给MSC。 
短信终呼
图12  短信终呼
[]images/ZUF-78-12-014-%E7%9F%AD%E4%BF%A1%E7%BB%88%E5%91%BC.png)
UE附着在LTE网络和1xRTT网络中。 
MSC下发短信，向IWS发送Adds Page消息。 
IWS将短信下行信令封装在A21-1xAir Interface Signaling消息中发送给MME。 
MME返回A21-1x Ack指示之前A21消息已接收到。 
IWS构造ADDS Page Ack消息发送给MSC。 
如UE处于IDLE态，MME对用户寻呼建立S1连接。 
UE处于连接态后，MME将短信下行信令封装在DL S1 CDMA2000 Tunneling消息中发送给eNodeB，eNodeB通知到UE。 
UE对接收到短信后返回层3响应，通过eNodeB向MME发送UL S1 CDMA2000 Tunneling，其中封装1xRTT短信上行信令。 
MME将1xRTT短信信令封装在A21-1xAir Interface Signaling消息中发送给IWS。 
IWS返回A21-1x Ack指示之前A21消息已接收到。 
IWS构造ADDS Transfer消息发送给MSC。 
E-UTRAN to 1xRTT的SRVCC
图13  E-UTRAN to 1xRTT SRVCC业务[]images/ZUF-78-12-014-E-UTRAN%20to%201xRTT%20SRVCC%E4%B8%9A%E5%8A%A1.png)
UE在LTE网络下进行VoLTE语音呼叫。 
用户判断需要语音SRVCC切换到1xRTT网络。 
UE构造1xRTT语音起呼消息通过eNodeB上报给MME。 
MME将1xRTT语音起呼消息封装在A21-1xAir Interface Signaling消息中发送给IWS。 
IWS返回A21-1xAir Ack指示之前A21消息已接收到。 
IWS构造Cm Service Request消息发送给MSC。 
MSC检查用户合法性后，对用户向IWS下发Assign Request消息。 
IWS直接返回Assign Complete消息。 
IWS构造Handoff Required消息发送给MSC，触发切换流程。 
MSC查找到目标BSC完成交互后，向IWS下发Handoff Command消息。 
IWS将切换命令封装在A21-1x Air Interface Signaling消息中发送给MME。 
MME返回A21-1xAir Ack指示之前A21消息已接收到。 
MME通过S1信令将切换命令下发给eNodeB。 
eNodeB通知UE开始切换。 
UE进入1xRTT下继续进行语音呼叫。 
### 系统影响 
IWS与MME合设成局时，对于MME内存占用取决于License配置的每个模块支持IWS用户数、每个模块IWS相关数据区容量。对于每个模块将新增占用大约25M内存。 
License支持IWS用户数|50000
S102数据区容量|2000
GCSNA数据区容量|1000
A1P数据区容量|5000
IWS与MME合设成局时，发生IWS相关的业务，将会占用系统CPU，占用CPU的比例取决于发生IWS业务的频率。 
### 应用限制 
只能应用于LTE网络和1xRTT网络间互操作，不能应用于LTE网络与GSM/UMTS网络间互操作。 
### 特性交互 
该特性不涉及与其他特性的交互。 
### 遵循标准 
标准类别|标准名称
---|---
3GPP TS 23.216|Single Radio Voice Call Continuity (SRVCC)
3GPP TS 23.272|Circuit Switched (CS) fallback in Evolved Packet System (EPS)、
3GPPTS29.277|Optimized Handover Procedures and Protocol between EUTRAN accessand non-3GPP accesses (S102)
3GPP2 A.S0008-D|Interoperability Specification (IOS) for High Rate Packet Data(HRPD) Radio Access Network Interfaces with Session Control in theAccess Network.
3GPP2 A.S0005-D|Upper Layer (Layer 3) Signaling Standard for cdma2000 SpreadSpectrum Systems
3GPP2 A.S0013-C|Interoperability Specification (IOS) for cdma2000 Access NetworkInterfaces — Part 3 Features
3GPP2 A.S0014-C|Interoperability Specification (IOS) for cdma2000 Access NetworkInterfaces — Part 4 Features
### 特性能力 
规格|指标
---|---
CELLID个数|最多可配置65534个CELLID
MSC组|最多可配置512个MSC组
MSC局向|最多可配置1024个MSC局向
### 可获得性 
##### 版本要求及变更记录 
特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
##### License要求 
该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性对应License文件中的项目为7037 MME支持S102接口。此项目显示为支持，表示ZXUN uMAC支持该特性。
##### 对其他网元的要求 
UE|MME|eNodeB|IWS|MSC
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
### O&M相关 
##### 命令 
配置项表2  新增配置项配置项命令S102本地地址配置SET S102 LOCALADDRSHOW S102 LOCALADDRIWS局向配置ADD IWSOFFSET IWSOFFDEL IWSOFFSHOW IWSOFFIWS局向组配置ADD IWSOFFGRPSET IWSOFFGRPADD IWSOFFGRP OFFICEDEL IWSOFFGRP OFFICEDEL IWSOFFGRPSHOW IWSOFFGRP基于CELLID选择IWS网元配置SET DEFAULT IWSCELLIDSHOW DEFAULT IWSCELLIDADD IWSCELLIDSET IWSCELLIDDEL IWSCELLIDSHOW IWSCELLID 
安全变量该特性不涉及安全变量的变化。 
定时器该特性不涉及定时器的变化。 
软参该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
##### 性能统计 
该特性不涉及计数器的变化。 
##### 告警和通知 
该特性不涉及告警和通知消息的变化。 
##### 业务观察/失败观察 
该特性不涉及业务观察/失败观察的变化。 
##### 话单与计费 
该特性不涉及话单与计费的变化。 
## 特性配置 
## 特性配置 
### 配置说明 
本节介绍如何配置IWS特性。 
### 配置前提 
需获知邻接MSC网元的点码、IP地址和端口号，MME与IWS之间采用SCTP协议。 
需规划CELLID与MSC网元的对应关系，CELLID在S102的A21-1xAir Interface Signaling消息Reference
Cell ID字段中携带。 
需规划MSC网元间组网模式，无容灾、主备还是负荷分担关系，负荷分担时确定各个MSC网元的分担比例。 
确认该特性对应License7037 MME支持S102接口为支持。 
### 配置过程 
设置MME的S102接口本地地址。 
在命令终端使用[SET S102 LOCALADDR](None)命令。
配置IWS1局向IP地址。 
在命令终端使用[ADD IWSOFF](None)命令。
配置IWS局向组。 
在命令终端使用[ADD IWSOFFGRP](None)命令。
配置CELLID对应默认IWS局向组。 
在命令终端使用[SET DEFAULT IWSCELLID](None)命令。
### 配置实例 
##### 配置IWS与MME互通 
场景说明
配置MME支持S102口，与IWS互通。 
数据规划
项目|MME1|IWS1
---|---|---
IP地址|131.1.17.159|40.40.1.1
配置步骤
配置步骤|解释说明|配置脚本
---|---|---
1|设置MME的S102接口本地地址|SET S102 LOCALADDR:IPADDR="131.1.17.159"
2|配置IWS1局向IP地址|ADD IWSOFF:OFFICEID=1,IP="40.40.1.1"
3|配置IWS局向组1|ADD IWSOFFGRP:GRPID=1,OFFICE=1-1-100
4|配置CELLID对应默认IWS局向组|SET DEFAULT IWSCELLID:GRPID=1
##### 配置IWS与MSC互通 
场景说明
配置IWS与MSC互通。 
数据规划
项目|IWS1|MSC1
---|---|---
与MME互通的IP地址|40.40.1.1|-
与MSC互通的IP地址|40.40.1.2|40.40.1.3
与MSC互通M3ua端口号|1000|1000
A口协议版本|IOS5.0|IOS5.0
CELLID|460-01-0001|-
7号信令点码|11-11-11|22-22-22
 说明： 
此时的CELLID为IWS在起呼消息中，上报给MSC的小区。 
配置步骤
配置步骤|解释说明|配置脚本
---|---|---
1|设置IWS网元属性|SET IWSCFG:IWSID=1,S102DATANUM=1000,GCSNADATANUM=1000,A1PDATANUM=1000
2|设置IWS的S102接口本地地址|SET IWSLOCALIP:IPADDR="40.40.1.1"
3|置本局7号信令点码|ADD OPC:NET=1,NETWORKNAME="IWS",OPC24="11.11.11"ADD LOFC:NET=1,SPTYPE="STEP",INVALIDNANUM=0
4|增加邻接MSC 7号信令局向|ADD ADJOFC:OFFICEID=100,NETWORKNAME="msc",SPCMODE="TRIPLE_DEC",DPC="22.22.22",NET=1,SPTYPE="STEP",SPCTYPE="24",PROT="ANSI"ADD ADJOFCIDCFG:OFCID=100,OFCTYPE="MSCSERVER"
5|增加MSC局向属性|ADD MSCECFG:OFCID=100,IOSVER="IOS5_0",MARKETID=100,SWITCHNUMBER=100,CELLID=1
6|增加MSC局向组|ADD MSCGROUP:MSCGRPID=100,MSCOFC=100-1-100
7|配置默认MSC局向组|SET DEFAULT MSCGROUP:MSCGRPID=100
# ZUF-78-12-015 CSFB语音容灾之MME故障控制 
## 特性描述 
## 特性描述 
### 描述 
##### 定义 
CSFB容灾，是指EPC/CS网络中，网元设备出现故障后，能够保证语音业务及时接管和恢复的功能。
对于CSFB业务，MME需要能够在MME故障或MSC故障后，能够及时恢复和MSC的SGs连接，以保证CSFB业务及时恢复。
##### 背景知识 
对于CSFB业务，如果SGs口出现故障或者MSC宕机，导致UE在重新附着、联合TAU之前，无法做被叫，此时需要能快速恢复SGs口从而恢复CSFB的被叫业务。
故障网元与CSFB主被叫业务的恢复方式参见[表1](ZUF-78-12-015-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#T_2017510842494__%E6%95%85%E9%9A%9C%E7%BD%91%E5%85%83%E4%B8%8ECSFB%E4%B8%BB%E8%A2%AB%E5%8F%AB%E4%B8%9A%E5%8A%A1%E7%9A%84%E6%81%A2%E5%A4%8D%E6%96%B9%E5%BC%8F-37F2353C)。
故障网元|CSFB主叫业务恢复方式|CSFB被叫业务恢复方式
---|---|---
MME故障|故障出现后，UE的上行业务触发eNB重选可用的MME，UE在新MME上重新联合附着，完成MSC注册，从而恢复CSFB业务。|UE在CS语音中处于被叫业务。故障出现后，此时MSC/VLR在MME POOL中重选可用的MME来下发寻呼，新的MME触发UE重新联合附着，完成MSC注册，从而恢复CSFB业务。
MSC故障（包括SGs口故障）|故障出现后，UE的上行业务触发MME选择正常SGs接口的MSC来重新注册，从而恢复CSFB业务。|UE在CS语音中处于被叫业务。故障出现后，此时备用MSC/VLR向MME下发无LAI寻呼。MME触发UE使用IMSI进行重新附着，完成MSC注册，从而恢复CSFB业务。同时，MME自动监控SGs接口，一旦发现SGs接口异常，异常SGs接口上注册的UE则重新注册到正常SGs接口的MSC上，从而恢复CSFB业务。
### 应用场景 
##### MME故障后的业务恢复 
MME发生故障或重启；该MME上的UE有CSFB的终呼业务，MSC/VLR能够立即选择其它可用MME下发寻呼；通过这个新选择的MME触发UE重新联合附着，完成MSC注册和SGs连接恢复。 
##### MSC故障后的CSFB业务恢复 
MSC发生故障或重启，故障后UE的CS语音被叫业务由备份MSC/VLR接管，并向MME下发无LAI寻呼，触发UE的IMSI重新附着。 
同时MME发现MSC发生故障或重启后，扫描故障MSC的UE，依次触发UE发起IMSI附着，注册到正常的MSC上，完成CSFB业务恢复。 
##### MSC/VLR手动卸载 
当发现某个MSC故障、或者需要升级维护时，需要对该MSC上注册的UE进行迁移；MME提供网管动态管理命令，触发注册在该MSC的UE重新发起IMSI附着。 
### 客户收益 
受益方|受益描述
---|---
运营商|提示系统的可靠性和安全性，特别是部署了VoLTE，提高VoLTE业务的可靠性，大幅减少因网络故障对VoLTE业务的影响。
移动用户|网络故障后，VoLTE业务不受影响。
### 实现原理 
##### 涉及的网元 
CSFB容灾功能需要UE、MME、MSC的共同配合，在CSFB容灾功能中各网元的主要作用参见[表2](ZUF-78-12-015-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#z1a997d06b1104334919f97930142da0b__b756a6b2-1042-48a8-beff-9bc2c9f0632a)。
网元|功能
---|---
UE|接受MME的指示，重新附着或者重新IMSI附着。
MME|MSC故障或重启后，能够主动触发UE重新IMSI附着。其他MME故障或重启后，作为新选择的MME能够接受MSC的寻呼消息，触发UE重新附着。
MSC/VLR|MME故障或重启后，能够在MME POOL中选择一个MME做被叫业务。MSC/VLR故障或重启后，作为备用MSC/VLR能够下发无LAI寻呼。
##### 业务流程 
MME出现故障后的CSFB业务恢复
MME出现故障后的CSFB业务恢复的流程如[图1](ZUF-78-12-015-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#z1a997d06b1104334919f97930142da0b__af97e37c-ab29-460f-aae8-0543747fd35e)所示。
图1  MME出现故障后的CSFB业务恢复的流程图
[]images/1587871055195.png)
流程说明如下： 
UE联合附着。 
UE所在的MME发生故障。当UE有CSFB被叫业务时，MSC/VLR在MME POOL中重选可用的MME下发寻呼，并在寻呼消息中携带CS业务恢复指示。 
MME收到寻呼消息后，尽管当前没有UE的上下文信息，但是判断寻呼消息中携带有CS业务恢复指示，则采用IMSI寻呼的方式，触发UE重新联合附着；IMSI寻呼时，MME利用寻呼消息中的LAC信息，获取用户的位置信息来控制寻呼范围，而避免全网寻呼。 
UE重新附着到新的MME。 
MME向MSC/VLR发起位置更新请求。 
MSC/VLR完成CS域的注册。 
MSC/VLR返回位置更新响应。 
MME返回联合附着接受。 
UE返回附着完成，至此UE业务恢复。 
此后该UE的终呼业务可被正常处理。 
MSC出现故障后被叫业务触发恢复
MSC出现故障后被叫业务触发恢复的流程如[图2](ZUF-78-12-015-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#z1a997d06b1104334919f97930142da0b__00166350-2be8-43c4-9cf6-f4794d12439c)所示。
图2  MSC出现故障后被叫业务触发恢复的流程图
[]images/1587871056155.png)
流程说明如下： 
UE联合附着。 
UE当前所在的MSC发生故障或重启。UE的CS语音被叫业务由备份MSC/VLR接管，备份MSC/VLR向MME下发寻呼，寻呼消息中不携带LAI。 
MME收到无LAI寻呼后，向UE发送IMSI Detach，触发UE发起IMSI重新附着。 
UE发起联合TAU更新，指示需要进行IMSI附着。 
MME重新选择可用MSC，发起SGs口的重新注册。 
MSC/VLR完成CS域的注册。 
MSC/VLR返回位置更新响应。 
MME返回联合TAU接受。 
UE返回TAU完成；至此UE业务恢复。 
此后该UE的终呼业务可被正常处理。 
MSC出现故障后上行业务触发恢复
MSC出现故障后上行业务触发的恢复的流程如[图3](ZUF-78-12-015-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#z1a997d06b1104334919f97930142da0b__60c2bc27-44ed-4fcd-acee-a07ebfc73cea)所示。
图3  MSC出现故障后上行业务触发恢复的流程图
[]images/CSFB%E5%AE%B9%E7%81%BE%E7%89%B9%E6%80%A7--MSC%E5%87%BA%E7%8E%B0%E6%95%85%E9%9A%9C%E5%90%8E%E4%B8%8A%E8%A1%8C%E4%B8%9A%E5%8A%A1%E8%A7%A6%E5%8F%91%E7%9A%84%E6%81%A2%E5%A4%8D.png)
流程说明如下： 
UE联合附着。 
UE发起TAU（包括周期性TAU）。 
MME判断UE当前所在的MSC发生故障或重启。 
MME重新选择可用MSC，发起SGs口的重新注册。 
MSC/VLR完成CS域的注册。 
MSC/VLR返回位置更新响应。 
MME返回TAU接受。 
UE返回TAU完成，至此UE业务恢复。 
此后该UE的终呼业务可被正常处理。 
MSC出现故障后MME主动快速恢复
MSC出现故障后MME主动快速恢复的流程如[图4](ZUF-78-12-015-1-%E7%89%B9%E6%80%A7%E6%8F%8F%E8%BF%B0.html#z1a997d06b1104334919f97930142da0b__618fce7f-93e7-454e-92d8-a03903f29cc0)所示。
图4  MSC出现故障后MME主动快速恢复的流程图
[]images/CSFB%E5%AE%B9%E7%81%BE%E7%89%B9%E6%80%A7--MSC%E5%87%BA%E7%8E%B0%E6%95%85%E9%9A%9C%E5%90%8EMME%E4%B8%BB%E5%8A%A8%E5%BF%AB%E9%80%9F%E6%81%A2%E5%A4%8D.png)
流程说明如下： 
UE联合附着。 
MME接收到MSC/VLR的RESET消息，或者是检测到与MSC/VLR的链路全部中断。 
为了避免链路瞬断造成的误判，需要通过网管配置合理的局向状态不可达时间。只有当局向状态进入不可达的时间达到配置的阈值，才需要触发恢复。 
MME扫描故障MSC/VLR的UE，依次向UE发送IMSI Detach，触发UE发起IMSI重新附着。 
UE发起联合TAU更新，指示需要进行IMSI附着。 
MME重新选择可用MSC，发起SGs口的重新注册。 
MSC/VLR完成CS域的注册。 
MSC/VLR返回位置更新响应。 
MME返回联合TAU接受。 
UE返回TAU完成；至此UE业务恢复。 
MSC出现故障后MSC/VLR手动卸载
当人工发现某个MSC/VLR故障，或者某个MSC/VLR需要升级维护时，MME通过动态管理命令，指定该MSC/VLR，对该MSC/VLR上注册的UE进行卸载。一旦命令被执行，MME扫描该MSC/VLR的UE，依次向UE发送IMSI Detach，触发UE发起IMSI重新附着，完成MSC/VLR重选。 
如果不希望UE重选时选择原来的MSC/VLR，可在MSC/VLR选择策略相关配置中，将该MSC/VLR权重暂时调整为0。 
### 系统影响 
##### 容灾恢复中 
一旦有一个网元发生故障或重启，该网元上的所有用户都有待恢复。这些用户的恢复过程，对POOL内的其他网元，带来了额外的业务负荷。所以POOL内的网元都需要有适当的冗余（一般情况下冗余1/N，N为POOL内节点数目），来保证容灾的业务接管。 
为了防止短时间内大量用户恢复造成的业务激增，需要MME在扫描恢复时，合理的控制单位时间内恢复的用户数目，既要避免对同时处理的正常业务造成过大的影响，也要避免恢复时间过长。 
按每秒每模块最快恢复40个用户、每模块5万用户需要恢复来计算，全部恢复需要约21分钟。触发恢复的业务负担增加不超过3%。 
##### MME无用户的寻呼 
MME POOL组网，用户所在的MME宕机，其他MME收到MSC
Server的寻呼请求，此MME需要根据寻呼中的LAI进行寻呼从而避免使用全局对系统的影响。 
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
该特性不涉及与其他特性的交互。 
### 遵循标准 
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements
for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access" 
3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for Evolved
Packet System (EPS); Stage 3" 
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network
(E-UTRAN); S1 Application Protocol (S1AP)" 
3GPP TS 23.007: "Restoration procedures" 
### 特性能力 
MME主动触发的UE恢复流程，最大支持每秒每模块100个用户。 
MME间的备份关系可支持链式备份和集中备份。 
### 可获得性 
##### License要求 
License ID|License控制值|License描述
---|---|---
7056|ON|MME支持SGs口主动恢复。
##### 对其他网元的要求 
需要MSC/VLR支持容灾故障恢复的相关功能，支持3GPP TS
23.007中描述的“网络侧触发的业务恢复”功能。
##### 组网要求 
CSFB容灾对组网无特殊要求。 
### O&M相关 
##### 命令 
配置项与CSFB容灾相关的配置项参见表3。表3  配置项配置项命令配置容灾恢复速率SET SERVRSTOCFG修改SGs口VLR局向配置SET VLROFFICE 
软件参数与CSFB容灾相关的软参参见表4。表4  软参软参ID软参名称262446支持SMS Only用户的SGs口主动恢复262372支持业务请求时VLR不可靠触发IMSI分离262373支持短信起呼时VLR不可靠触发IMSI分离262374支持扩展业务请求时VLR不可靠触发IMSI分离 
##### 业务观察/失败观察 
VLR局向手动恢复
当需要迁移某个或多个VLR局向的用户时，使用VLR局向手动恢复命令，具体命令如下： 
[RESTORE
VLR](../../MMESGSN\zh-CN\mml\1269623.html):VLROFFICEID=1&2;
取消VLR局向手动恢复
当需要终止正在执行的VLR局向手动恢复命令时，使用取消VLR局向手动恢复，具体命令如下： 
[CANCEL
RESTORE VLR](../../MMESGSN\zh-CN\mml\1269624.html):VLROFFICEID=1;
## 特性配置 
## 特性配置 
### 配置说明 
为了保证语音业务及时接管和恢复的功能，需要对CSFB容灾进行配置。 
### 配置前提 
需要完成MME基础配置。 
### 配置过程 
MME网元支持CSFB容灾功能主要包括如下几个配置步骤： 
将制作的MME支持SGs口主动恢复的license文件，加载到MME网管。 
使用[SET VLROFFICE](../../MMESGSN\zh-CN\mml\1261262.html)命令，开启VLR局向支持故障后的能主动恢复。
使用[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)命令，配置合理的容灾恢复速率。
使用[SET SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)命令，配置合理的VLR局向故障恢复检测时长。
使用[SET SOFTWARE PARAMETER](../../MMESGSN\zh-CN\mml\1268001.html):PARAID=262446,PARAVALUE=1命令，开启支持SMS
Only用户的SGs口主动恢复功能。
配置MME支持上行业务触发的恢复，包括： 
使用SET SOFTWARE PARAMETER:PARAID=262372,PARAVALUE=1命令，开启支持业务请求时VLR不可靠触发IMSI分离。 
使用SET SOFTWARE PARAMETER:PARAID=262373,PARAVALUE=1命令，开启支持短信起呼时VLR不可靠触发IMSI分离。 
使用SET SOFTWARE PARAMETER:PARAID=262374,PARAVALUE=3命令，开启支持扩展业务请求时VLR不可靠触发IMSI分离。 
### 配置实例 
MME POOL组网，POOL内有二个MME： 
MME1对接VLR1局向，支持无LAC寻呼。 
MME2对接VLR1局向。 
VLR1局向支持CSRI。 
配置MME故障后CSFB业务恢复。 
MME故障后CSFB业务恢复需要MME POOL组网，并且VLR局向的配置，而且该VLR支持MME容灾功能。 
以MME POOL的MME1进行配置说明。 
步骤|命令|说明
---|---|---
1|SET VLROFFICE:VLROFFICEID=1,ATTR="CS"|配置VLR1局向支持CSRI功能。
2|SET SOFTWARE PARAMETER:PARAID=65683,PARAVALUE=1|当MME收到VLR1的寻呼消息携带CSRI信元，且MME找不到用户时，进行全网IMSI寻呼用户。
配置MSC故障后CSFB业务恢复。 
配置被叫业务触发的恢复。 
步骤|命令|说明
---|---|---
1|SET VLROFFICE:VLROFFICEID=1,ATTR="NO_LAI"|配置VLR1局向支持无LAC寻呼。
配置上行业务触发的恢复。 
MSC/VLR故障后，终端发起业务请求、SGs短信和扩展业务请求触发恢复。 
步骤|命令|说明
---|---|---
1|SET SOFTWARE PARAMETER:PARAID=262372,PARAVALUE=1|配置MME支持业务请求触发SGs口恢复。
2|SET SOFTWARE PARAMETER:PARAID=262373,PARAVALUE=1|配置MME支持短信业务触发SGs口恢复。
3|SET SOFTWARE PARAMETER:PARAID=262374,PARAVALUE=3|配置MME支持扩展业务请求触发SGs口恢复。
配置MME主动快速恢复。 
在SGs口快速恢复配置之前，应当完成VLR局向和VLR POOL的相关配置。 
步骤|命令|说明
---|---|---
1|SHOW LICENSE|MME支持SGs快速恢复License配置。查询LicesneID为7056的取值是否为支持。如果为否，需购买该功能的License并重新加载，否则该功能不可用。
2|SET VLROFFICE:VLROFFICEID=1,ATTR="ASSRES"|配置VLR1局向支持SGs快速恢复。当MME检测到VLR1局向不可达的时间达到配置的时间阈值或者MME收到VLR1局向VLRReset消息时，判断VLR1局向故障，主动触发联合附着到VLR1的用户进行SGs恢复。
3|SET VLROFFICE:VLROFFICEID=2,ATTR="ASSRES"|配置VLR2局向支持SGs快速恢复。
4|SET VLROFFICE:VLROFFICEID=3,ATTR="ASSRES"|配置VLR3局向支持SGs快速恢复。
5|SET SERVRSTOCFG:RSTOSCANRATE=40,RSTORATE=5,VLRDETCTIME=2|配置SGs快速恢复相关参数，包括：设置容灾恢复扫描速率为40。设置容灾业务恢复速率为5。设置VLR局向故障恢复检测时长为2。参数的具体取值可以根据实际情况进行调整。
6|SET SOFTWARE PARAMETER:PARAID=262446,PARAVALUE=1|配置SMS only的用户支持SGs快速恢复。如果该软参关闭，对于附加更新类型为SMS only的用户，MME不会主动触发用户进行SGs恢复。
手动卸载MSC/VLR。 
MSC/VLR手动卸载是通过动态命令执行卸载VLR的用户触发SGs恢复。 
命令|说明
---|---
RESTORE VLR:VLROFFICEID=1&2|当需要迁移某个或多个VLR局向的用户时，使用VLR局向手动恢复命令。
CANCEL RESTORE VLR :VLROFFICEID=1|当需要终止正在执行的VLR局向手动恢复命令时，使用取消VLR局向手动恢复。
### 调整特性 
恢复速率调整，一般无需特别调整恢复速率，特殊情况下，可根据系统的负荷情况加快或减慢恢复速率，配置命令为[SET
SERVRSTOCFG](../../MMESGSN\zh-CN\mml\1260771.html)。
### 测试用例 
测试项目|SGs口主动恢复
测试目的|测试VLR故障时，能触发SGs口的主动恢复。
预置条件|license中MME支持SGs口主动恢复。SGs口的VLR局向支持故障后的主动恢复。VLR局向都可达。VLR局向故障恢复检测时长为2分钟。容灾业务扫描速率为40/100ms。容灾业务恢复速率为5/100ms。
测试过程|用户在VLR上联合附着，处于连接态。VLR不可达时间达到阈值2分钟。MME发送IMSI detach后，收到UE发出的detach accept后和联合TAU。
通过准则|VLR不可达两分钟后直接进行IMSI detach，并清除SGs状态。收到detach accept后，不主动释放S1连接，收到联合TAU后，重选VLR发起位置更新。
测试结果|—
# ZUF-78-12-016 CSFB语音容灾之MSC/VLR故障控制 
MSC发生故障或重启。当故障发生后，备用MSC/VLR接管UE的CS语音终呼业务，并向MME发送non-LAI paging消息，触发UE进行IMSI重附着。 
同时，当MME检测到MSC发生故障或重启时，MME扫描断链MSC的UE，触发UE依次发起IMSI附着和在正常运行的MSC上注册，以恢复CSFB业务。 
# ZUF-78-12-017 SMS over SGs 
## 概述 
MME在LTE网络和CS网络间投递短消息。 
## 收益 
在LTE网络和CS网络间传递短消息，节约网络资源。 
## 描述 
MME支持基于SGs口的短消息业务，即短消息业务由CS域直连短消息中心，MME完成LTE网络和CS网络间的短消息传递。 
MME可以基于以下因素控制SGs口短消息： 
IMSI 
APN 
# ZUF-78-12-018 SMS over SGd 
## 概述 
基于MME的短信机制指短消息业务由MME实现。当UE请求短消息业务时，基于MME的短信机制通过
SGd接口连接的MME与SMC之间的EPS NAS信令下发SMS业务。 SGd接口是基于Diameter/SCTP/IP协议的。并且，MME支持UE在不使用PDN连接的情况下只使用SMS业务请求和附着业务。 
## 收益 
基于MME的短信架构选项通过E-UTRAN支持EPS中SMS业务，无需部署
3GPP MSC。 
## 说明 
MME注册到HSS中获取短消息用户数据并给HSS提供MME标识，用于MT-SMS（终呼短消息）下发。MME验证是否允许用户获取短消息业务。 
当UE只需要短消息业务时，MME支持不建立PDN连接的EMM附着。MME将与UE协商不具备PDN连接能力的附着。MME将允许UE在没有默认PDN连接的情况下保持附着。无论UE在什么时候请求EPS业务，MME都建立PDN连接。 
UE和MME之间仍然通过EPS
NAS信令投递短消息。而在MME和SMC之间，短消息的投递是通过基于Diameter/SCTP/IP协议的SGd接口，而不是通过SGs接口。 
在基于MME的短信机制中，MME不会向VLR进行任何注册。 
# ZUF-78-12-019 SMS over IP 
## 概述 
MME为IMS提供IP承载完成短消息传递.。 
## 收益 
在LTE网络传递短消息。 
## 描述 
SMS over IP是由IMS提供短消息服务，EPS提供IP承载。 
# ZUF-78-12-020 公共告警系统/小区广播服务 
## 特性描述 
### 描述 
#### 定义 
公共告警系统PWS，用于在地震、海啸、恐怖事件等灾难或紧急事件发生时，通过广播、网络、电视等各种通讯技术，向公众及时传递告警信息，提醒公众避险。
小区广播服务CBS，是公共告警系统通过移动网络传递告警信息时采用的一种方式。公共告警系统生成告警信息后，发送到核心网的CBC。MME接收来自小区广播中心下发的告警信息，并广播给指定的eNodeB。eNodeB向移动终端广播告警信息。当终端收到告警信息时，信息自动弹出并播放特定的告警音，以便用户快速及时的获知告警信息，及时避险。
#### 背景知识 
公共安全已成为世界各国经济社会正常发展和国家管理正常运行的重要保障。为了避免人类在遇到地震、海啸等突发重大自然灾害或者恐怖事件等人为灾难中遇到的伤害，各国政府都在对PWS进行研究。PWS包含多种类型，例如：
地震海啸预警系统ETWS， 专门用于对地震和海啸进行预警，目前主要使用国家是日本。 
商用移动预警系统CMAS，又名WEA（Wireless Emergency Alert，无线紧急预警）。这个告警系统是FCC定义的，目前在大多数国家使用，例如美国、巴西、智利等。3GPP定义的CMAS架构如图1所示：图1  CMAS Reference Architecture 
### 应用场景 
政府机构探测到地震、海啸、恐怖事件等灾难或紧急事件发生时，启用小区广播服务，通过移动网络及时广播公共告警信息给终端用户，用于避险。 
### 客户收益 
受益方|受益描述
---|---
运营商|当地震、海啸、恐怖事件等发生时，快速广播公共告警信息给移动用户。
移动用户|能够快速获取地震、海啸、恐怖事件等告警信息，及时避险。
### 实现原理 
#### 系统架构 
3GPP定义的4G PWS网络架构如[图1](#T_2017510842497__775c6b99-e216-4def-bd84-509ba7faa003)所示：
图1  4G PWS架构
[]images/1651804862470.png)
#### 涉及的网元 
网元名称|网元作用
---|---
UE|接收移动网络下发的告警消息，并显示给用户。
eNodeB|接收MME发送的告警消息，选择待广播的小区列表，向选定的小区广播告警消息。支持PWS重启/故障指示流程，向MME发送PWS重启/故障指示消息。
CBC|选择MME列表，向选定的MME发送告警消息。接收MME转发的PWS重启/故障指示消息。
CBE|小区广播设备。
#### 协议栈 
该特性涉及的接口协议栈参见下表。 
接口|协议栈信息参考
---|---
S1|ZUF-78-16-001 S1-MME
SBc|ZUF-78-16-017 SBc
#### 本网元实现 
告警消息发送/取消流程：MME接收CBC发送的告警发送/告警取消消息，选择合适的eNodeB并转发给选中的eNodeB。 
PWS重启/故障指示流程：MME接收eNodeB发送的PWS重启/故障指示消息，转发给CBC。 
#### 业务流程 
告警消息发送流程
告警消息发送流程如[图2](#T_2017510842497__98e5a360-9afd-4ad8-9199-9f0af5314ead)所示。
图2  告警消息发送流程
[]images/1651904979189.png)
流程说明如下： 
UE执行网络注册和安全流程。 
CBE向CBC发送Emergency Broadcast Request消息（包括：告警类型、告警消息、广播域、广播周期等）。 
CBC对消息进行鉴权，根据广播区域确定需要发送的MME，向MME发送Write-Replace Warning Request消息，消息中携带要广播的告警消息以及Message Identifier、Serial Number、List of TAIs、Warning Area List、Send Write-Replace-Warning-Indication、Global eNB ID等参数。 
MME向CBC发送Write-Replace Warning Confirm消息，指示MME已经开始向eNodeB广播告警消息。消息中还可以携带Unknown Tracking Area List参数，用于标识MME未知且告警请求无法发送的跟踪区。 
CBC向CBE发送确认消息。 
MME根据Write-Replace Warning Request消息中的List of TAIs和Global eNB ID确定需要转发的eNodeB，然后向选定的eNodeB转发Write-Replace Warning Request消息。如果CBC消息中携带了Global eNB ID，则MME向Global eNB ID指示的eNodeB转发该消息；如果未携带Global eNB ID，携带了List of TAIs，则MME根据List of TAIs确定需要转发的eNodeB；如果Global eNB ID和List of TAIs均未携带，则MME向所有连接的eNodeB转发该消息。 
eNodeB根据告警消息中的Message identifier和Serial Number检测是否重复消息，如果检测到重复消息，则只对第一个收到的消息进行小区广播。eNodeB根据消息中的Warning Area List参数确定待广播的小区区域。eNodeB向MME返回Write-Replace Warning Response消息。 
UE通过声音、震动或者其他方式向用户告警。 
（可选）如果MME接收的Write-Replace Warning Request消息中携带了Send Write-Replace-Warning-Indication参数，并且MME支持该参数，则MME将eNodeB在Write-Replace Warning Response消息中携带的Broadcast Completed Area List转发到CBC。MME可以聚合从eNodeB接收的Broadcast Completed Area List后转发到CBC。 
告警消息取消流程
告警消息取消流程如[图3](#T_2017510842497__1f4ec577-db75-4b5a-abc4-418f1decbeec)所示。
图3  告警消息取消流程
[]images/1651905062972.png)
流程说明如下： 
CBE向CBC发送Stop Emergency Broadcast Request消息（包括：Message Identifier和Serial Number）。 
CBC对消息进行鉴权，确定需要发送的MME，向MME发送Stop Warning Request消息，消息中携带Message Identifier、Serial Number、List of TAIs、Warning Area List、Send Stop Warning Indication等参数。 
MME向CBC发送Stop Warning Confirm消息，指示MME已经开始向eNodeB发送Kill Request消息。 
CBC向CBE发送确认消息。 
MME根据Stop Warning Request message消息中的List of TAIs参数确定需要转发的eNodeB，然后向选定的eNodeB转发Kill Request消息。如果未携带List of TAIs参数，则MME向所有连接的eNodeB转发Kill Request消息。 
eNodeB收到Kill Request消息后，停止广播由Message identifier和Serial Number标识的告警消息。eNodeB向MME返回Kill Response消息。 
（可选）如果MME接收的Kill Response消息中携带了Broadcast Cancelled Area List参数，并且MME支持该参数，则MME将eNodeB在Kill Response消息中携带的Broadcast Cancelled Area List转发到CBC。MME可以聚合从eNodeB接收的Broadcast Cancelled Area List后转发到CBC。 
PWS重启指示流程
PWS重启指示流程如[图4](#T_2017510842497__4f01561a-00a6-4a22-99f7-2f5fb7c5ec28)所示。
图4  PWS重启指示流程
[]images/1651908410879.png)
流程说明如下： 
eNodeB发现部分小区或所有小区需要CBC重新下发告警信息时，向MME发送PWS Restart Indication消息。 
MME收到PWS Restart Indication消息后，转发给CBC。如果MME连接多个CBC，则MME应将PWS restart Indication消息转发给所有CBC。 
PWS故障指示流程
PWS故障指示流程如[图5](#T_2017510842497__41e60ab0-617d-44ae-8970-23922eecc281)所示。
图5  PWS故障指示流程
[]images/1651908424441.png)
流程说明如下： 
eNodeB发现一个或多个小区下PWS操作失败时，向MME发送PWS Failure Indication消息。 
MME收到PWS Failure Indication消息后，转发给CBC。如果MME连接多个CBC，则MME应将PWS Failure Indication消息转发给所有CBC。 
### 系统影响 
MME需要非常快速的向eNodeB广播告警消息，因此，CPU会有瞬间的波动。 
### 应用限制 
该特性不涉及应用限制。 
### 特性交互 
该特性不涉及与其他特性的交互。 
### 遵循标准 
标准名称|章节
---|---
3GPP 22.268（Public Warning System (PWS) requirements）|所有章节
3GPP 23.041（Technical realization of Cell Broadcast Service (CBS)）|所有章节
3GPP 29.168（Cell Broadcast Center interfaces with the Evolved Packet Core）|所有章节
### 特性能力 
名称|指标
---|---
CBC局向最大个数|32（个）
每个CBC局向支持的最大偶联个数|4（个）
### 可获得性 
#### 版本要求及变更记录 
特性版本|发布版本|发布说明
---|---|---
01|V7.22.10|首次发布。
#### License要求 
该特性需要申请License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为MME支持PWS功能（license ID：uMAC_MME_7140），此项目显示为“支持”，表示MME支持PWS功能。
#### 对其他网元的要求 
UE|eNodeB|CBC
---|---|---
√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
#### 工程规划要求 
工程规划上，需要部署CBC。 
## 特性配置 
### 配置说明 
通过增加SCTP偶联与CBC局向配置，实现MME与CBC互通。 
### 配置前提 
MME和CBC的地址、路由等均已配置完毕，业务地址能够互通。 
已加载MME支持PWS功能的License。 
### 配置过程 
执行[ADD SCTP](../../Commons_SIG\zh-cn\mml\1251000.html)命令，根据业务规划添加偶联，应用协议类型为SBCAP。
执行[ADD SCTPIDCFG](../../MMESGSN\zh-CN\mml\1260413.html)命令添加偶联索引，偶联协议类型为SBCAP。
执行[ADD CBC OFFICE](../../MMESGSN\zh-CN\mml\1269717.html)命令，根据业务规划增加CBC局向。
### 配置实例 
#### 场景说明 
通过增加SCTP偶联与CBC局向配置，实现MME与CBC互通。 
#### 数据规划 
配置名称|参数项|取值
---|---|---
SCTP偶联配置|SCTP标识|100
本端端口|SCTP偶联配置|40101
对端端口|SCTP偶联配置|40101
本端IP地址1|SCTP偶联配置|192.10.100.22
对端IP地址1|SCTP偶联配置|192.10.53.1
应用协议类型|SCTP偶联配置|SBCAP
偶联索引配置|偶联ID|100
偶联协议类型|偶联索引配置|SBCAP
CBC局向配置|CBC标识|1
SCTP连接标识|CBC局向配置|100
#### 配置步骤 
步骤|配置说明|配置脚本
---|---|---
1|配置MME和CBC通信的偶联，IP地址、端口号，应用属性按照业务规划配置|ADD SCTP:ID=100,LOCPORT=40101,REMPORT=40101,LOCADDR1="192.10.100.22",REMADDR1="192.10.53.1",PROTOCALTYPE=SBCAP
2|配置偶联索引|ADD SCTPIDCFG:SCTPID=100,TYPE=SBCAP
3|配置CBC局向|ADD CBC OFFICE:CBCID=1,SCTPID="100"
### 调整特性 
本特性不涉及调整特性。 
### 测试用例 
测试项目|开始告警
---|---
测试目的|测试PWS功能的告警消息发送流程。
预置条件|MME各项对接和业务配置完毕。已加载MME支持PWS功能的License。MME和CBC对接成功。eNodeB支持ETWS或CMAS。
测试过程|CBC收到CBE发送的紧急信息，发送Write-Replace Warning Request消息给MME。MME向CBC返回响应，并根据消息中的eNodeB或TAI列表确定需要转发的eNodeB。MME收到各eNodeB的响应，记录日志信息，并根据CBC消息中的指示确定是否向CBC发送指示消息。
通过准则|开始告警流程成功。
测试结果|–
测试项目|停止告警
---|---
测试目的|测试PWS功能的告警消息取消流程。
预置条件|MME各项对接和业务配置完毕。已加载MME支持PWS功能的License。MME和CBC对接成功。eNodeB支持ETWS或CMAS。
测试过程|CBC给MME发告警停止请求。如果请求中带了TAList，那么MME查找TAList对应的eNodeB，给CBC回响应，并给eNodeB发Kill消息。如果请求中没有带TAList，那么MME给本局所有eNodeB发Kill。MME收到eNodeB响应时，根据消息中的Serial Number查找到数据区确定是需要给CBC回响应的，则给CBC回确认消息。
通过准则|结束告警流程成功。
测试结果|–
测试项目|eNodeB重启
---|---
测试目的|测试PWS功能的eNodeB重启流程
预置条件|MME各项对接和业务配置完毕。已加载MME支持PWS功能的License。MME和CBC对接成功。eNodeB支持ETWS或CMAS。
测试过程|eNodeB发现部分小区或所有小区需要CBC重新下发告警信息时，给MME发重启指示。MME将消息转发给CBC。如果MME连接多个CBC局向，则将消息发送到各局向。
通过准则|eNodeB重启流程成功。
测试结果|–
### 常见问题处理 
无。 
 缩略语 
 缩略语 
# 1xCSFB 
1x Circuit Switched Fallback1x电路交换回落
# 1xRTT 
1x Radio Transmission Technology1x无线传输技术
# 3GPP 
3rd Generation Partnership Project第三代合作伙伴计划
# ATCF 
Access Transfer Control Function接入转换控制功能
# ATGW 
Access Transfer Gateway接入转换网关
# BSC 
Base Station Controller基站控制器
# CDMA 
Code Division Multiple Access码分多址
# CS 
Circuit Switched电路交换
# CSFB 
Circuit Switched Fallback电路域回落
# DDN 
Downlink Data Notification下行数据通知
# E-UTRAN 
Evolved Universal Terrestrial Radio Access Network演进的通用陆地无线接入网络
# e1xCSFB 
Evolved 1x Circuit Switched Fallback演进的1x电路交换回落
# eNodeB 
Evolved NodeB演进的NodeB
# EPC 
Evolved Packet Core演进的分组核心网
# EPS 
Evolved Packet System演进的分组系统
# eSRVCC 
enhanced SRVCC增强SRVCC
# GMSC 
Gateway Mobile-service Switching Center网关移动业务交换中心
# HLR 
Home Location Register归属位置寄存器
# HSS 
Home Subscriber Server归属用户服务器
# IAM 
Initial Address Message初始地址消息
# ICS 
IMS Centralized ServiceIMS集中式业务提供
# IDA 
Insert-Subscriber-Data- Answer插入用户数据响应
# IDR 
Insert-Subscriber-Data-Request插入用户数据请求
# IMEISV 
International Mobile Equipment Identity and Software Version number国际移动设备识别码和软件版本号
# IMS 
IP Multimedia SubsystemIP多媒体子系统
# IMSI 
International Mobile Subscriber Identity国际移动用户标识
# IWS 
Interworking Solution互操作解决方案
# LA 
Location Area位置区
# LAI 
Location Area Identity位置区标识
# LTE 
Long Term Evolution长期演进
# MME 
Mobility Management Entity移动管理实体
# MSC 
Mobile Switching Center移动交换中心
# NRI 
Network Resource Identifier网络资源标识
# PLMN 
Public Land Mobile Network公共陆地移动网
# RAT 
Radio Access Technology无线接入技术
# SCTP 
Stream Control Transmission Protocol流控制传输协议
# SGW 
Serving Gateway服务网关
# SIP 
Simple Internet Protocol简单IP协议
# SMS 
Short Message Service短消息业务
# SRI 
Send Routing Information发送路由信息
# SRVCC 
Single Radio Voice Call Continuity单射频语音呼叫连续性
# T-ADS 
Terminating Access Domain Selection终结接入域选择
# TA 
Tracking Area跟踪区域
# TAI 
Tracking Area Identity跟踪区标识
# TAU 
Tracking Area Update跟踪区域更新
# TMSI 
Temporary Mobile Subscriber Identity临时移动用户识别码
# UDP 
User Datagram Protocol用户数据报协议
# UE 
User Equipment用户设备
# VLR 
Visitor Location Register拜访位置寄存器
# VoLTE 
Voice over LTELTE语音
