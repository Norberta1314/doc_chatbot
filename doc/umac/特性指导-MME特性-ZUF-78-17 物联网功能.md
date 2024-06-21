概述 :功能描述 :移动物联网快速发展，在各行各业的应用越来越广泛，包括：金融、智慧城市、工业应用、农业、教育、医疗等领域。它具有广覆盖、大连接、低功耗、低成本的优势，解决了传统物联网存在的技术碎片化、覆盖不足的问题，极大提升了物联网的应用能力，获得了业内的广泛支持，将成为物联网主流技术。 
目前3GPP定义的移动物联网的主要技术： 
NB-IoT：窄带物联网技术，主要用于低功耗、高时延、深覆盖的物网设备的通信。 
eMTC：增强的物联网通信技术，主要用于高可靠、低时延的物和物之间的通信。 
3GPP定义的CIoT网络架构如[图1]所示：
图1  物联网架构

功能特性简介 :针对物联网的应用特点、接入方式和应用场景，核心网为满足物联网用户的要求，提供了可靠、有效的解决方案。详细的解决方案特性如下表： 
方案特性|实现简述|特导链接
---|---|---
NB-IoT接入|MME支持NB-IoT接入，并支持基于UE当前的RAT类型进行接入控制。|ZUF-78-17-001 NB-IoT接入
eMTC接入|传输上行和下行小包数据IP Data、Non-IP Data或短消息。完成S1-MME到S11-U面的小包数据IP Data、Non-IP Data转换传输。其他eMTC同普通LTE接入处理，业务流程同传统LTE网络。|ZUF-78-17-002 eMTC接入
物联网控制面EPS优化|适用于eMTC和NB-IoT。MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输小包数据。|ZUF-78-17-003 物联网控制面EPS优化
物联网用户面EPS优化|适用于eMTC和NB-IoT。UE在ECM-IDLE和ECM-CONNECTED态之间转换时，MME使用Suspend和Resume流程，代替了S1 Release和Service Request流程，大大减少了无线信令。|ZUF-78-17-004 物联网用户面EPS优化
海量接入|低复杂度、低功耗、低速率的物联网终端基于NB-IoT物联网技术接入EPC网络，核心网对物网用户进行优化存储。|ZUF-78-17-005 海量接入
节电智能|MME对不同用户、不同应用场景制定不同的节电策略，与UE协商节电参数，管理UE节电状态，通知SGW缓存下行数据，保证节电状态下的可靠数据传输等功能。包括PSM和eDRX两种节电技术，同时支持HLCom功能。|ZUF-78-17-006 节电智能
低移动性|为了减少海量接入的物联网设备对网络负荷能力造成的冲击，采用缩小设备的寻呼范围、减少对设备移动性管理操作等措施，提高移动网络的接入能力。制定不同TA List分配策略、寻呼策略、周期性TAU时长以及移动性限制策略，为网络资源的合理利用、终端节电和海量接入提供支撑。|ZUF-78-17-007 低移动性
深度覆盖|MME支持深度覆盖特性，通过对深度覆盖场景下的NB-IoT终端进行寻呼优化，保证系统使用尽可能少的资源尽快寻呼到NB-IoT终端，从而提升无线资源利用效率。|ZUF-78-17-008 深度覆盖
Non-IP EPS连接|物联网特有功能，特定的终端和应用可能采用例如6LowPAN、MQTT-SN等非IP的协议栈。MME和UE间通过控制面通道传输NAS数据包，MME和SAE-GW通过S11-U用户面通道传输小包数据，MME可以和SCEF、GW之间建立控制面通道传输Non-IP小包数据。|ZUF-78-17-009 Non-IP EPS连接
小包传输头压缩|头压缩（Header Compression）是减少无线与核心网之间的流量的一种技术。经过头压缩后，传输的报头字节数远远小于完整的报头，当频繁地传输比较小的数据包时，开启头压缩功能可以提高数据传输效率。|ZUF-78-17-010 头压缩
NAS速率控制|服务的PLMN的速率控制用于控制UE所有承载的上行报文速率及PGW/SCEF对UE的下行报文速率。APN的速率控制用于控制UE的某APN下承载的上行报文速率及PGW/SCEF对UE的下行报文速率。|ZUF-78-17-011 速率控制
DECOR专网|简称专网，用于为特定的用户提供特定的业务和功能，这类用户包括物联网用户、特定的企业用户或者独立行政区域用户等。支持DCN，可以通过DECOR/eDECOR技术把传统物联网终端迁移到专用核心网，构建专用的物联网核心网。|ZUF-78-17-012 DECOR
eDECOR专网|eDECOR是DECOR的演进，由UE协助进行专网选择。eDECOR使用UE携带的DCN-ID，通过RAN选择专网，从而减少了DECOR的重新定向路由的过程。|ZUF-78-17-013 eDECOR
CN辅助eNodeB参数|核心网辅助无线参数优化机制，可以减少MTC终端可能出现的频繁Connected/Idle之间状态转换所带来的信令开销，同时可以根据不同的MTC终端业务应用，提供差异化的状态转换策略，实现最优网络性能。|ZUF-78-17-014 CN辅助eNodeB参数
跨RAT移动|物联网NB-IoT终端可能会移出NB-IoT RAT覆盖区域，进入WB RAT区域；或者NB-IoT终端从WB RAT覆盖区域移动进入NB-IoT RAT覆盖区域。MME需要支持UE在空闲态下的跨RAT跨局移动，网络需要支持终端在空闲态下的跨RAT移动。|ZUF-78-17-015 NB跨RAT移动
无线覆盖增强限制|覆盖增强限制功能是指运营商不允许特定终端和无线使用深度覆盖，以达到减少终端的能量损耗。根据签约信息，对终端和eNodeB进行覆盖增强限制。根据UE's usage（终端指示）、签约信息、本地配置综合判断并对终端和eNodeB进行覆盖增强限制。|ZUF-78-17-016 覆盖增强限制
SCEF事件订阅上报|SCEF连接是指MME启动用户状态检测，检测到用户相应的订阅事件，直接与SCEF网元建立连接，将对应的用户移动状态事件上报给SCEF网元。|ZUF-78-17-017 SCEF连接
# ZUF-78-17-001 NB-IoT接入 
特性描述 :特性描述 :术语 :术语|含义
---|---
IoT|物联网，即物物相连的互联网，是互联网从人向物的延伸。物联网的核心和基础仍然是互联网，其用户端延伸和扩展到了任何物品与物品之间。物联网进行信息交换和通信，是基于特定的终端，如射频识别装置、红外感应器、全球定位系统、激光扫描器等，以有线或无线等接入手段，为企业和家庭用户提供机器到机器、机器到人的解决方案，满足用户对生产过程/家居生活监控、指挥调度、远程数据采集和测量、远程诊断等方面的信息化需求。国际电信联盟ITU在2005年《物联网》报告中将“物联网”定义为：一个无所不在的计算及通信网络，在任何时间、任何地方、任何人、任何物体之间都可以相互联结。
CIoT|蜂窝物联网，专指在移动网络上实现物联网。
NB-IoT|窄带物联网，是由3GPP定义的基于蜂窝网络的窄带物联网技术标准，是一种专为物联网设计的窄带射频技术，以广连接、低功耗、低成本、低移动和深覆盖为特点，可应用于GSM网络、UMTS网络和LTE网络中。
描述 :定义 :NB-IoT是由3GPP定义的基于蜂窝网络的窄带物联网技术标准，是一种专为物联网设计的窄带射频技术，以广连接、低功耗、低成本、低移动和深覆盖为特点。 
MME支持NB-IoT接入，并支持基于UE当前的RAT类型进行接入控制。 
背景知识 :物联网话务模型具有海量接入和业务突发性的特点。据咨询公司预测，2020年物联网终端将达到近300亿连接，是人网的5~6倍；年增值率达30%，增长速度是人终端的近10倍。 
MME对物联网终端支持海量接入，单网元将会达到亿级接入。当某类行业终端放号后，可能在某个时间集中突发性上线及收发数据，对网络集中处理性能有很高要求。因此，MME需要对物联网终端进行接入控制限制。 
应用场景 :场景1：HSS对NB-IoT接入进行控制场景描述：当UE的签约ARD为“NB-IoT Not Allowed”时，如果HSS需要对UE进行接入控制，则拒绝UE接入，返回失败的ULA消息，携带失败原因值：DIAMETER_ERROR_RAT_NOT_ALLOWED。MME根据此失败原因值，拒绝UE接入。 
场景2：MME根据签约ARD对NB-IoT接入进行控制场景描述：当UE的签约ARD为“NB-IoT Not Allowed”时，HSS不对UE进行接入控制，则HSS返回成功的ULA消息，其中携带UE的签约ARD。如果MME配置开启了ARD功能，则会限制UE接入。 
场景3：MME根据本地号段限制区域配置对NB-IoT接入进行控制场景描述：如果MME的“移动管理参数配置”中的以下任一参数设置为“支持”，那么MME需要根据“MME号段限制区域配置”对NB-IoT接入进行控制。“支持基于IMSI号段的TAI区域限制”“MME支持基于MSISDN号段的TAI区域限制”“MME支持基于IMEI的TAI区域限制” 
客户收益 :受益方|受益描述
---|---
运营商|运营商可以根据配置灵活控制是否允许NB-IoT受限用户接入。
物联网终端用户|不需要更换硬件，只需要升级软件就可以享受更多的服务。
实现原理 :系统架构 :NB-IoT接入所对应的组网架构如下图所示。 

涉及的网元 :网元名称|网元作用
---|---
NB-IoT UE|窄带物联网终端，发起接入物联网等流程，用NAS PDU发送和接收小包数据。
E-UTRAN|支持NB-IoT UE的接入，传递NAS PDU。
MME|支持NB-IoT UE的接入，并基于UE当前的RAT类型进行接入控制。
HSS|提供UE的签约数据。
协议栈 :
本网元实现 :当HSS对NB-IoT接入进行控制时：HSS在收到MME发送的ULR消息后，如果UE的签约ARD为“NB-IoT
Not Allowed”，则拒绝UE接入，返回失败的ULA消息。MME根据HSS返回的ULA中的失败原因值“DIAMETER_ERROR_RAT_NOT_ALLOWED”，限制UE接入，限制原因值可以通过“用户接入限制拒绝原因值配置”进行配置。
当HSS不对NB-IoT接入进行控制时：HSS在收到MME发送的ULR消息后，返回成功的ULA消息，其中携带UE的签约ARD。MME通过“移动管理参数配置”中的“MME支持LTE用户接入限制”参数控制是否开启ARD功能。当“MME支持LTE用户接入限制”参数设置为“支持”时，即表示开启ARD功能。如果UE的签约ARD为“NB-IoT Not Allowed”，则MME限制UE接入，限制原因值可以通过“移动管理参数配置”中的“LTE用户接入EUTRAN网络失败原因”参数配置。
MME根据号段和用户当前所在位置，检查本地配置策略，判断是否允许UE通过NB-IoT接入。“MME号段限制区域配置”中的“是否允许接入”参数增加了新的取值，需要根据UE的接入类型和配置来决定是否允许用户接入。
在NB-IoT用户号段能匹配到配置的情况下，只有当“是否允许接入”参数配置为“只允许NB-IoT接入”或“都允许接入”时，才允许用户接入。
业务流程 :NB-IoT的接入控制发生在附着流程中，如下图所示。 
流程描述如下： 
UE发送Attach Request消息，S1AP消息中携带的RAT类型为NB-IoT。 
MME收到Attach Request后，执行原有的鉴权和安全流程，包括通过分配GUTI以减少IMSI的暴露。 
MME进行位置更新和获取UE的签约数据。 
MME基于NB-IoT RAT类型进行接入控制，允许或拒绝UE接入。 
系统影响 :对于数量庞大的物联网设备终端，其话务模型可能只有公众网络智能手机类的终端的5%～10%甚至更低，因此从系统的CPU处理能力上来说，理应可以容纳10～20倍以上的终端接入。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :协议名称|章节
---|---
3GPP TS 23.720（Study on architecture enhancements for CellularInternet of Things）|6 Solutions
3GPP TS 29.272 （Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol）|7.3.31 Access-Restriction-Data
3GPP TS 23.401 （General Packet Radio Service (GPRS) enhancementsfor  Evolved Universal Terrestrial Radio Access Network (E-UTRAN)access）|5.3.2 Attach procedure
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :需要申请了“NB-IoT注册用户数”和“NB-IoT在线用户数”的License许可后，运营商才能获得NB-IoT用户接入核心网的服务。
对其他网元的要求 :UE|eNodeB（E-UTRAN）|SGW|PGW|HSS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项新增配置项参见表1。表1  新增配置项配置项命令物联网业务配置SET MME IOT CFGSHOW MME IOT CFGMME号段限制区域配置SET MME NUMSEG RESTRICT AREA POLICYSHOW MME NUMSEG RESTRICT AREA POLICY修改配置项参见表2。表2  修改配置项配置项命令新增参数MME号段限制区域配置ADD MME NUMSEG RESTRICT AREA“是否允许接入”参数中增加三个取值：只允许WB-EUTRAN接入、只允许NB-IoT接入、都允许接入。 
性能统计 :测量类型|描述
---|---
基于接入类型附着流程测量|编号为46501开头的所有计数器
基于接入类型跟踪区更新流程测量|编号为46502开头的所有计数器
基于接入类型业务请求流程测量|编号为46503开头的所有计数器
基于接入类型去附着流程测量|编号为46504开头的所有计数器
基于接入类型寻呼流程测量|编号为46505开头的所有计数器
基于接入类型EMM通用流程测量|编号为46506开头的所有计数器
基于接入类型承载激活流程测量|编号为46507开头的所有计数器
基于接入类型承载修改流程测量|编号为46508开头的所有计数器
基于接入类型承载去激活流程测量|编号为46509开头的所有计数器
基于接入类型UE请求承载资源流程测量|编号为46510开头的所有计数器
基于接入类型用户数测量|编号为46531开头的所有计数器
基于接入类型承载数测量|编号为46532开头的所有计数器
基于接入类型Diameter消息测量|编号为46541开头的所有计数器
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过NB-IoT接入控制的相关配置，实现MME对物联网终端基于RAT类型的接入控制。 
配置前提 :MME网元各项对接和业务配置完毕。 
配置过程 :执行命令[SET MME NUMSEG RESTRICT AREA POLICY]，配置移动管理参数，将“MME支持基于IMSI号段的TAI区域限制”、“MME支持基于MSISDN号段的TAI区域限制”、“MME支持基于IMEI的TAI区域限制”设置为“支持”。
执行命令[ADD MME RESTRICT AREA]，配置MME限制区域。
执行命令[ADD MME NUMSEG RESTRICT AREA]，配置MME号段限制区域。
配置实例 :配置MME对NB-IoT UE进行接入控制。 
限制IMSI号段为460021234的UE，在跟踪区标识为1的跟踪区中，只允许通过WB-EUTRAN接入。 
限制IMSI号段为460025678的UE，在跟踪区标识为1的跟踪区中，只允许通过NB-IoT接入。 
配置步骤|配置说明
---|---
SET MME NUMSEG RESTRICT AREA POLICY:MMESPTIMSISEGREST="YES"|配置移动管理参数“支持基于IMSI号段的TAI区域限制”为“支持”。
ADD MME RESTRICT AREA:AREAID=1,TAID=1,NAME="TA1"|配置MME限制区域，其中“限制区域标识”为1，“跟踪区标识”为1。跟踪区标识需要通过ADD TA命令预先配置。
ADD MME NUMSEG RESTRICT AREA:NUMSEG="460021234",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="WB_EUTRAN"|配置MME号段限制区域，其中需要限制的IMSI号段为460021234，该号段用户在“限制区域标识”为1的跟踪区中，只允许通过WB-EUTRAN接入。
ADD MME NUMSEG RESTRICT AREA:NUMSEG="460025678",NUMTYPE="IMSI",ISALLTA="NO",AREAID=1,ACCESS="NB_IOT"|配置MME号段限制区域，其中需要限制的IMSI号段为460025678，该号段用户在“限制区域标识”为1的跟踪区中，只允许通过NB-IoT接入。
测试用例 :##### MME支持根据UE签约数据控制NB-IoT接入 
测试项目|MME支持根据UE签约数据控制NB-IoT接入
测试目的|测试MME支持根据UE签约数据控制NB-IoT接入
预置条件|MME各项对接和业务配置完毕。取得NB-IoT注册用户数的license授权，并更新了license。取得NB-IoT在线用户数的license授权，并更新了license。取得MME支持物联网小包数据控制面传输优化功能的license授权，并更新了license。开启支持物联网小包数据控制面传输优化功能开关，对应命令为SET MME IOT CFG:CPSW="YES"。MME支持ARD功能开关打开，对应命令为SET MOBILE MANAGEMENT:SPTIMSITAIRST="YES"。UE在HSS签约为NB-IoT Not Allowed。
测试过程|物联网终端开机发起附着，使用控制面传输优化模式接入。MME给HSS发送的ULR消息中，携带的RAT Type为NB-IoT。HSS回复成功ULA消息，其中签约数据中携带NB-IoT Not Allowed。MME拒绝终端接入，拒绝原因为“移动管理参数配置”中的“LTE用户接入EUTRAN网络失败原因”参数配置的原因值，对应命令为SET MOBILE MANAGEMENT:LTEUSERACCESSCAUSE="Tracking Areanot allowed"。
通过准则|MME拒绝NB-IoT用户接入，拒绝原因为“移动管理参数配置”中的“LTE用户接入EUTRAN网络失败原因”参数配置的原因值。
测试结果|
##### MME支持根据IMSI和当前TA本地配置策略控制NB-IoT接入 
测试项目|MME支持根据IMSI和当前TA本地配置策略控制NB-IoT接入
测试目的|测试MME支持根据IMSI和当前TA本地配置策略控制NB-IoT接入
预置条件|MME各项对接和业务配置完毕。取得NB-IoT注册用户数的license授权，并更新了license。取得NB-IoT在线用户数的license授权，并更新了license。取得MME网元支持物联网小包数据控制面传输优化功能的license授权，并更新了license。开启支持物联网小包数据控制面传输优化功能开关，对应命令为SET MME IOT CFG:CPSW="YES"。移动管理参数“MME支持基于IMSI号段的TAI区域限制”、“MME支持基于MSISDN号段的TAI区域限制”、“MME支持基于IMEI的TAI区域限制”都设置为“支持”。配置MME限制区域。配置MME号段限制区域。
测试过程|物联网终端开机，从配置的被限制的TA发起附着，使用控制面传输优化模式接入。MME拒绝终端接入，拒绝原因为TA Not Allowed。
通过准则|MME拒绝NB-IoT用户接入，拒绝原因为TA Not Allowed。
测试结果|
常见问题处理 :无。 
# ZUF-78-17-002 eMTC接入 
特性描述 :特性描述 :术语 :术语|含义
---|---
IoT|物联网（Internet of Things），即物物相连的互联网，是互联网从人向物的延伸。物联网的核心和基础仍然是互联网，其用户端延伸和扩展到了任何物品与物品之间，进行信息交换和通信，是基于特定的终端，如射频识别装置、红外感应器、全球定位系统、激光扫描器等，以有线或无线等为接入手段，为企业和家庭客户提供机器到机器、机器到人的解决方案，满足客户对生产过程/家居生活监控、指挥调度、远程数据采集和测量、远程诊断等方面的信息化需求。国际电信联盟ITU在2005年物联网报告中将“物联网”定义为：一个无所不在的计算及通信网络，在任何时间、任何地方、任何人、任何物体之间都可以相互联结。
CIoT|蜂窝物联网，专指在移动网络上实现物联网。
描述 :定义 :eMTC是指增强的物联网通信，是基于LTE协议演进而来，主要用于高可靠、低时延的物和物之间的通信。
背景知识 :目前移动物联网的主要技术是3GPP定义的标准窄带物联网技术NB-IoT和非窄带物联网技术MTC，eMTC是增强的物联网通信技术。
eMTC主要用于高可靠、低时延的物和物之间的通信。在智能物流上，具有防盗、防调换、实时温度传感和可定位优势；在智能可穿戴设备中，可支持健康监测、视频业务、数据回传和定位；也可以用于智能充电桩和智能公交站牌等方面。 
eMTC是基于LTE协议演进而来，eMTC接入同普通的LTE接入，相对于NB-IoT，可用于中高速率、低时延的物网场景，因此具有同人网的业务特性；也可能传送小包数据，所以也具有物网小包数据传输的业务特性。 
eMTC大包数据传输同LTE网络，通过传统EPC网络S1-U用户面通道，在eNodeB和SGW间传输IP数据。数据传输架构如下图所示。 
图1  数据传输架构

eMTC小包数据可以通过用户面传输，也可以通过控制面传输，小包数据控制面传输架构如下图所示。 
图2  小包数据控制面传输架构图

MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SGW间通过S11-U用户面通道传输IP小包数据。小包数据传输类型也可以是NoN-IP数据。 
eMTC是基于LTE协议演进而来，与NB-IoT不同，eMTC接入同普通的LTE接入；eMTC移动性处理和数据传输同传统LTE网络，另外物联网小包数据控制面传输同NB-IoT；eMTC中高速率、低时延的物联网特性，MME映射为不同的承载QoS处理；对MME来说，没有引入新的网络处理技术。 
应用场景 :eMTC主要应用于中高速率、低时延的物联网场景，这类物联网设备终端发送和接收的可能是大包数据也可能是小包数据。MME针对eMTC的应用提供： 
普通LTE接入处理，通过传统EPC网络S1-U用户面通道传输大包数据。 
普通LTE接入处理，通过传统EPC网络S1-U用户面通道或控制面通道传输小包数据。 
支持eMTC终端移动性。 
提供特定QoS。 
数据传输（大包）
带音视频的物联网应用中，如智能可穿戴设备中的健康监测、视频业务等，往往都是大包数据传输。 
对于eMTC接入MME同普通LTE接入处理，数据传输也同LTE网络，通过传统EPC网络S1-U用户面通道，在eNodeB和SGW间传输IP数据。 
数据传输（小包）
小数据量信息传递的物联网应用中，如智能物流中的定位信息，可能是小包数据传输。 
eMTC接入MME同普通LTE接入处理，数据传输可以通过传统EPC网络S1-U用户面通道；也可以在MME和UE间通过控制面通道使用NAS消息传输小包数据，在MME和SGW间通过S11-U用户面通道传输IP小包数据。小包数据传输类型也可以是NoN-IP数据。 
 支持eMTC终端移动性
中高速的物联网应用中，物联网终端的可移动性是基本需求。eMTC接入MME同普通LTE接入处理，TAU、切换等移动性处理同传统LTE网络。 
提供特定QoS
eMTC中高速率、低时延的物联网特性，MME映射为不同的承载QoS。对于音视频或小数据量信息传递的物联网应用，推荐QCI=8的QoS。 
QCI|Resource Type|Priority|Packet Delay Budget|Packet Error LossRate|Example Services
---|---|---|---|---|---
8|-|8|300 ms|10-6|Video (Buffered Streaming)TCP-based (e.g., www, e-mail,chat, ftp, p2p file
客户收益 :受益方|受益描述
---|---
运营商|增加收入：未来物联网将成为运营商收入的主要来源，基于LTE网络的物联网技术eMTC为其提供重要的技术支撑。节约成本：复用已部署的LTE网络，无需重新建网；小包数据传输，可以和NB-IoT用户共用改造后的核心网。
物联网终端用户|丰富多样的物联网应用使得终端用户的生活更加便捷。
实现原理 :系统架构 :数据传输架构如下图所示。 
图3  数据传输架构图

小包数据控制面传输架构如下图所示。 
图4  小包数据控制面传输架构图

涉及的网元 :eMTC由UE、eNodeB、MME和SGW/PGW配合完成。 
网元名称|网元作用
---|---
UE|物联网终端，可以用NAS PDU发送和接收小包数据IP Data或NoN-IP Data；并携带S1释放辅助信息。
eNodeB|支持eMTC终端接入，传递NAS PDU；通过S1-U面传输数据。
MME|对用户进行接入控制和安全管理，完成SGW和PGW的选择和承载管理。传输上行和下行小包数据IP Data、NoN-IPData或短消息；完成S1-MME到S11-U面的小包数据IP Data、NoN-IP Data转换传输。
SGW/PGW|管理和存储UE的承载信息。负责将UE接入PDN，分配用户IP地址。通过S11-U面传输小包数据IP Data或NoN-IPData；通过S1-U面传输大包或小包数据。
协议栈 :eMTC控制面小包数据传输协议栈如下图所示。 
图5  eMTC控制面小包数据传输协议栈

本网元实现 :传输上行和下行小包数据IP Data、NoN-IP Data或短消息。 
完成S1-MME到S11-U面的小包数据IP Data、NoN-IP Data转换传输。 
其他eMTC同普通LTE接入处理，业务流程同传统LTE网络。 
业务流程 :eMTC同普通LTE接入处理，MME处理流程包括： 
普通LTE接入处理，通过传统EPC网络S1-U用户面通道传输大包数据。 
普通LTE接入处理，通过传统EPC网络S1-U用户面通道或控制面通道传输小包数据。 
支持eMTC终端移动性。 
提供特定QoS。 
数据传输（大包）
大包数据传输也同LTE网络，通过传统EPC网络S1-U用户面通道，在eNodeB和SAE-GW间传输IP数据。 
数据传输（小包）
小包数据可以通过传统EPC网络S1-U用户面通道传输，也可以通过控制面传输，这里详细描述控制面传输。 
小包数据控制面传输同NB，MME网元的小包数据传输流程包括： 
IP小包数据传输流程 
非IP小包数据传输流程 
IP小包数据传输流程
IP小包数据传输流程的附着流程如下图所示。 
图6  附着

流程描述： 
UE发送Attach Request消息，消息中指示： 
UE network capability参数包含“支持CP模式”的指示（“Control plane CIoT EPS
optimization supported”）。 

Additional update type的Preferred CIoT network behaviour 参数指示为“control
plane CIoT EPS optimization”。 

数据类型：IP and/or non-IP。 
UE在附着请求消息中会携带会话管理的PDN连接请求消息；如果是SMS方式，则不携带PDN连接请求消息。eNB向MME发送初始UE消息，携带接入类型为普通EPS接入。 
MME收到Attach Request，如果是CP模式且支持CP模式的开关打开，则允许UE接入；MME需要执行原有的鉴权和安全流程，包括通过分配GUTI以减少IMSI的暴露。CP模式下，只做NAS层的加密和完整性保护。 
MME进行位置更新和获取UE的签约数据，根据ARD数据检查UE是否允许接入，如果不允许则返回附着拒绝。
UE可以签约两个默认的APN，一个为IP类型，一个为Non-IP类型。MME根据UE请求的APN及类型或签约的APN以及IP/Non-IP类型指示，最终选择使用IP/Non-IP的APN。 
MME为UE创建PDN连接，向SGW发起创建会话请求消息，携带RAT Type指示为NB-IoT，消息中无NAS会话管理信令。 
IP Data：创建会话请求消息中携带IP的PDN类型，携带创建S11-U的指示，且在需要创建的承载上下文中携带S11-U
MME F-TEID。PGW根据附着请求中携带的PDN type分配了一个IP地址给UE。 
Non-IP Data：创建会话请求消息中携带Non-IP的PDN类型，PGW不分配IP地址给UE。 
SGW返回创建会话响应，创建的承载上下文中携带S11-U SGW F-TEID；如果是IP Data，消息还携带为UE分配的IP地址。 
MME记录SGW的S11-U的地址和S11-U SGW F-TEID，构建GTP-U隧道。MME通过下行NAS传输消息发送Attach
Accept消息给eNB，eNB通过RRC直传消息投递给UE，消息中不携带会话管理消息，如果是IP Data，消息还携带为UE分配的IP地址。另外Additional
update result的Negotiated CIoT network behaviour参数指示为“control-plane
CIoT EPS optimization”。 
UE通过RRC直传消息将Attach Complete消息投递给eNB，eNB通过上行NAS传输消息发送Attach
Complete给MME。 
RRC连接释放。 
控制面传输MO流程如下图所示。 
图7  控制面传输MO

流程描述： 
用户附着完成。UE发起的RRC连接建立，消息中携带有NAS PDU；NAS PDU中携带有EBI，用来标识同时携带的加密的上行数据；NAS
PDU用来携带小包数据IP Data。 
UE携带的释放辅助信息，可以帮助MME及时完成S1释放： 
如果携带释放信息，同时指示无需后继数据，则说明当前的上行数据已经是所有应用数据的最后一包，不需要应答或者是响应； 则MME可以在上行数据传输后立即释放S1连接。 
如果携带释放信息，同时指示需要后继数据，则说明当前的上行数据需要应答或者是响应，是所有应用数据的最后一次交互；则MME可以在收到下行数据并完成下行数据传输后立即释放S1连接。 
如果不携带释放信息，则MME不立即释放S1连接，处理UE和GW间的数据传输；直到收到释放信息，或者是eNB的S1释放为止。 
空闲态的场景，eNB通过Initial UE消息给MME，携带NAS PDU参数。Initial UE为控制面业务消息，并携带ESM
Data Transport参数。 
MME进行完整性检查和消息解密；如果S11-U尚未建立，则MME发送修改承载请求，重建S11-U；SGW返回修改承载响应；MME通过S11-U接口，将上行数据报文封装在GTP-U消息中，发送给SGW。根据UE释放指示的决策，如果MME需要释放，则立即释放S1连接；如果MME不需要释放S1连接，则等待GW的下行数据传递。 
小包数据抵达GW，则GW发送该数据给MME。 
MME根据SGW返回的S11-U地址和GTP-U的端口进行报文收发；MME从GTP-U消息中得到下行数据报文后，封装NAS传输消息ESM
Data Transport，对消息进行加密和完整性保护后，投递给eNB。根据UE释放指示的决策，如果MME需要在下行数据传递后释放S1连接，则发起S1释放。 
eNB发送Downlink Information Transfer（包括NAS消息）给UE，并且在RRC连接检测定时器到时释放RRC连接。如果MME根据释放指示的决策没有释放S1连接，且一定时间内没有NAS消息投递，则eNB发起S1释放。 
控制面传输MT流程如下图所示。 
图8  控制面传输MT

流程描述： 
用户附着完成。SGW收到下行数据报文，但发现没有S11-U承载，则缓存报文。SGW发送DDN消息给MME，消息中携带有EBI和ARP。 
（可选）当UE已注册且可达，MME发送寻呼消息给eNB。eNB寻呼UE；UE收到寻呼消息后，发起业务请求。eNB发送Initial
UE消息给MME。 
如果S11-U尚未建立，则MME发送修改承载请求，重建S11-U；SGW返回修改承载响应；MME根据SGW返回的S11-U地址和GTP-U的端口进行报文收发；MME从GTP-U消息中得到下行数据报文后，封装通用下行NAS投递消息ESM
Data Transport消息，对消息进行加密和完整性保护后，投递给eNB。eNB发送下行RRC消息携带NAS消息给UE。 
UE发送上行RRC消息携带NAS消息ESM Data Transport通过eNB给MME；MME进行完整性检查和消息解密。 
MME将上行数据报文通过S11-U发送给SGW；并根据消息中的释放辅助信息决策是否需要立即释放S1连接；如果MME根据释放指示的决策没有释放S1连接，且一定时间内没有NAS消息投递，则eNB发起S1释放。 
用户面传输
eNB和GW间使用S1-U面进行数据传送，和普通EPC网络数据传送一样。 
用户面小数据传输优化关键流程包括： 
SUSPEND 
RESUME 
SUSPEND流程如下图所示。 
图9  SUSPEND

流程描述： 
eNB使用新增的S1AP消息“UE Context Suspend Request”向MME发起挂起流程；UE进入IDLE态；MME为UE保留有S1AP上下文和承载上下文，包括MME和eNB的S1AP
ID，eNB的S1-U地址和TEID，SGW的地址和TEID等。 
MME发送Release Access Bearers Request消息，通知SGW释放S1-U连接。 
SGW释放eNB的相关信息，包括地址和下行的TEID等，返回Release Access Bearers Response消息；此后如果有下行报文，将触发DDN流程。 
MME收到释放接入承载响应后，向eNB发送“UE Context Suspend Response”消息。 
eNB发送RRC Connection Suspend消息。 
RESUME流程如下图所示。 
图10  RESUME>>

流程描述： 
Radnom Access。 
UE因上行业务或寻呼，引发连接恢复流程。 
eNB使用新增的S1AP消息“UE Context Resume Request”向MME发起恢复流程；UE进入CONNECT态。 
MME返回“UE Context Resume Response”消息给eNB，消息中携带为UE保存的S1AP上下文和承载上下文信息，包括MME和eNB的S1AP
ID，eNB的S1-U地址和TEID，SGW的地址和TEID等。 
如果步骤4中，MME携带了需要拒绝的承载列表，则eNB重新配置无线承载。 
上行数据此时可根据之前保存的SGW地址和TEID进行发送。 
MME发送Modify Bearer Request消息给SGW，消息中携带保存的eNB的S1-U地址和下行TEID；此时SGW可以发送下行报文给eNB。 
SGW向MME返回Modify Bearer Response消息，SGW的S1-U地址和上行TEID保持不变。 
非IP小包数据传输
非IP小包数据传输的附着流程与IP Data不同的是： 
UE发送Attach Request消息，消息中指示数据类型为non-IP。 
UE可以签约两个默认的APN，一个为IP类型，一个为Non-IP类型。MME根据UE请求的APN及类型和/或签约的APN以及Non-IP类型指示，最终选择使用Non-IP的APN。对于Non-IP
Data，MME根据签约中Non-IP的传输类型决定使用SGi传输方式。 
MME在创建会话请求消息中携带Non-IP的PDN类型，PGW不分配IP地址给UE。 
支持eMTC终端移动性
eMTC接入MME同普通LTE接入处理，TAU、切换等移动性处理同传统LTE网络。 
提供特定QoS
eMTC中高速率、低时延的物联网特性，MME映射为不同的承载QoS处理；eMTC接入MME同普通LTE接入处理，承载QoS流程的处理同传统LTE网络。 
系统影响 :物联网终端数量庞大，随着越来越多的eMTC终端接入系统，系统负荷越大。 
应用限制 :该特性基于3GPP R15 2018年3月份版本实现，与MME对接的周边网元支持eMTC接入时需要对齐到该协议版本。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: " General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|4.3.17节: Support for Machine Type Communications
3GPP TS 22.368: “Service requirements for Machine-Type Communications(MTC)”|全部
3GPP TS 29.272: “Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol”|7.3节：Information Elements
3GPP TS 24.301: “Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS)”|5.3.15节：CIoT EPS optimizations
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了“MME支持物联网小包数据控制面传输优化”和“MME支持物联网小包数据用户面传输优化”的License许可后，运营商才能获得物联网小包数据控制面和用户面传输优化特性的服务。 
需要申请“MME支持EPS注册态无PDN连接功能”的License许可后，运营商才能获得MME支持物联网用户仅使用短消息时不建PDN连接特性的服务。 
需要申请“MME支持Non-IP数据SGi口传输” 的License许可后，运营商才能获得MME支持物联网用户Non-IP数据通过SGi口传输 特性的服务。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :SGW/PGW升级通过S11-U面传输小包数据IP Data或NoN-IP Data。 
O&M相关 :命令 :配置项该特性不涉及命令的变化。 
软件参数 
软件参数ID|软件参数名称
---|---
262539|WB用户是否忽略CP模式
786850|是否只有NB用户支持用户面优化
262541|WB用户是否启用eDRX
262542|WB用户是否启用PSM
262551|寻呼增强时对WB用户寻呼的eNodeB个数保持最多7个
262536|WB的接入方式下EPS的附着和TAU是否支持SMS ONLY
786847|只有NB用户支持SMS IN MME功能
262540|Paging消息里WB用户是否携带UE_ID字段
262533|Context Req和Context Rsp消息是否携带RatType
262535|Sgi PDN情况下MME是否下发CP Only Indication给WB用户
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过eMTC的相关配置，实现MME对使用eMTC技术的用户的接入控制。 
配置前提 :MME网元与其他网元的对接和业务配置已完成。 
eMTC与NB-IoT的相关功能的基本配置是相同的，由于eMTC是WB类型的终端，MME侧对相应的特性增加了开关。 
启用eMTC时先参照NB-IoT功能的文档设置好基本的配置。 
启用物联网小包数据控制面传输优化功能时，需要规划好MME和SGW间的S11-U用户面地址，MME License需要开启MME支持物联网小包数据控制面传输优化。物联网相关业务开关中设置支持控制面优化。 
启用物联网小包数据用户面传输优化功能时，MME License需要开启MME支持物联网小包数据用户面传输优化。物联网相关业务开关中设置支持用户面优化。 
启用节电智能功能时，MME license需要开启MME支持PSM节电功能和MME支持eDRX节电功能。物联网相关业务开关中设置 支持PSM和支持eDRX；在节电配置中配置节电策略。 
启用低移动性功能时，MME license需要开启MME支持低移动性功能。物联网相关业务开关中设置支持低移动性(LM)。 
启用深度覆盖功能时，MME license需要开启MME支持物联网寻呼增强功能。 
启用Non-IP EPS连接功能时，MME license需要开启MME支持Non-IP。物联网相关业务开关中设置支持Non-IP数据SGi口传输。 
启用MME短消息功能时，MME需要支持S6d口，license需要开启MME支持SMS IN MME功能。物联网相关业务开关中设置支持物联网终端短消息优化。 
启用速率控制功能时，MME license需要开启MME支持速率控制。 
启用DECOR功能时，MME license需要开启MME支持DECOR。MME DECOR控制策略配置中设置MME支持DECOR。 
启用eDECOR功能时，MME license需要开启MME支持eDECOR。MME eDRCOR控制策略配置中设置MME支持eDRCOR。 
配置过程 :通过SET SOFTWARE PARAMETER:PARAID=262539,PARAVALUE=0;命令，允许WB用户接入时，MME支持CP模式。 
通过SET SOFTWARE PARAMETER:PARAID=786850,PARAVALUE=0;命令，允许允许WB用户接入时，MME支持UP模式。 
通过SET SOFTWARE PARAMETER:PARAID=262541,PARAVALUE=1;命令，打开WB用户接入时MME启用eDRX功能。 
通过SET SOFTWARE PARAMETER:PARAID=262542,PARAVALUE=1;命令，打开WB用户接入时MME启用PSM功能。 
通过SET SOFTWARE PARAMETER:PARAID=262551,PARAVALUE=1;命令，打开WB用户接入时MME支持寻呼增强功能。 
通过SET SOFTWARE PARAMETER:PARAID=262536,PARAVALUE=1;命令，打开WB接入EPS的附着和TAU时MME支持SMS ONLY功能。 
通过SET SOFTWARE PARAMETER:PARAID=786847,PARAVALUE=0;命令，允许WB用户支持SMS IN MME功能。 
通过SET SOFTWARE PARAMETER:PARAID=262540,PARAVALUE=1;命令，允许Paging消息里WB用户携带UE_ID字段。 
通过SET SOFTWARE PARAMETER:PARAID=262533,PARAVALUE=1;命令，允许Context Req和Context Rsp消息携带RatType字段。 
通过SET SOFTWARE PARAMETER:PARAID=262535,PARAVALUE=1;命令，允许SGi PDN情况下MME下发CP Only Indication给WB用户。 
配置实例 :配置eMTC接入时通过控制面通道使用NAS消息传输小包数据。 
MME需要打开“支持物联网小包数据控制面传输优化”功能开关，并配置MME S11-U的用户面地址，以及允许WB用户使用CP模式。
配置步骤|配置说明
---|---
SET MME IOT CFG:CPSW="YES";|打开MME“支持物联网小包数据控制面传输优化”功能开关。
SET MME GTPU IP:S11UIPADDR=192.20.66.210;|配置MME S11-U用户面地址。
SET SOFTWARE PARAMETER:PARAID=262539,PARAVALUE=0;|允许WB用户CP模式。
数据传输（大包）、支持eMTC终端移动性、提供特定QoS这三个场景，保证MME网元与其他网元的对接和业务配置完成即可，不需要额外配置。 
调整特性 :无 
测试用例 :测试项目|UE优选控制面的附着
---|---
测试目的|验证网络和终端同时支持控制面用户面方案情况下选择控制面附着
预置条件|网络中各网元系统及操作维护台运行正常。MME、SAE-GW同时支持CIOT控制面和用户面优化方案。CIOT UE同时支持CIOT控制面和用户面优化方案。在MME上建立S1、S6a、S5接口跟踪，单用户跟踪。
测试过程|UE发起附着流程。Attach request中携带的UE network capability指示UE同时支持“Control plane CIoT EPS optimization supported” 及“User plane CIoT EPS optimization supported”。Attach request中携带的Additional update type指示UE优选控制面附着。Attach request中PDN Type为IPv4。同时支持控制面和用户面的MME返回Attach accept消息，网络侧接受UE的控制面附着。
通过准则|检查UE attach request 中 UE Network Capability 的 Control-plane CIOT optimization is supported和User-plane CIOT optimization is supported同时置位。UE attach request 中Additional update type中bit 4,3 为01  control plane CIoT EPS optimization。
测试结果|UE attach成功。选择控制面附着。
测试项目|UE优选用户面的附着
---|---
测试目的|验证网络和终端同时支持控制面用户面方案情况下选择用户面附着
预置条件|网络中各网元系统及操作维护台运行正常。MME、SAE-GW同时支持CIoT控制面和用户面优化方案。CIoT UE同时支持CIoT控制面和用户面优化方案。在MME上建立S1、S6a、S5接口跟踪，单用户跟踪。
测试过程|UE发起附着流程。Attach request中携带的UE network capability指示UE同时支持“Control plane CIoT EPS optimization supported” 及“User plane CIoT EPS optimization supported” 。Attach request中携带的Additional update type指示UE优选用户面附着。Attach request中PDN Type为IPv4。同时支持控制面和用户面的MME返回Attach accept消息，网络侧接受UE的用户面附着。
通过准则|UE attach request 中 UE Network Capability 的 Control-plane CIOT optimization is supported和User plane CIOT optimization is supported同时置位。UE attach request 中Additional update type中bit 4,3 为10  User plane CIoT EPS optimization。Create Session Request消息中Indication字段中S11TF为0或不携带，Modify Bearer Request消息中Indication字段中S11TF为0或不携带。
测试结果|UE attach成功。选择用户面附着。
常见问题处理 :无。 
# ZUF-78-17-003 物联网控制面EPS优化 
特性描述 :特性描述 :描述 :定义 :物联网控制面EPS优化功能，适用eMTC，也适用NB-IoT。MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输小包数据。
背景知识 :NB-IoT小包数据传输架构
NB-IoT小包数据传输架构如下图所示，图中的C-SGN包括MME和SAE-GW。
NB-IoT应用于低吞吐量的物联网场景，因此这类物联网设备终端发送和接收的是小包数据。 
小包数据传输的方式有以下几种： 
方式一：通过传统EPC网络的S1-U用户面通道经由SAE-GW可以传输IP小包数据。 
但由于小包数据本身数据量小，为了节省无线网络承载资源，可在UE和MME之间使用控制面通道来传输小包数据。因此可以使用方式二。 
方式二：MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输IP小包数据。 
进一步考虑节省IP地址资源，可使用Non-IP方式传输小包数据。因此可使用方式三。 
方式三：MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输Non-IP小包数据。 
NB-IoT小包数据传输类型
IP数据IP小包数据可以通过现有的EPC网络S1-U用户面通道经由SAE-GW进行传输。考虑到网络需要传输的是小包数据，为了提高传输效率，MME和UE间也可以通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输小包数据，MME完成NAS到GTP-U的协议转换。 
Non-IP数据Non-IP数据是物联网特有的，特定的终端和应用可能采用例如6LowPAN、MQTT-SN等非IP的协议栈。对于Non-IP数据，MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输小包数据；也可以采用轻量化的架构，使得数据传输路径更短，MME可以和SCEF建立控制面通道传输Non-IP小包数据。 
SMSMME和SMSC/IWMSC建立控制面通道投递上下行短消息数据。 
本特性中仅介绍方式二。Non-IP相关的详细内容参见ZUF-78-17-009
Non-IP EPS连接
；SMS相关的详细内容参见ZUF-78-12 语音和短消息
。
应用场景 :物联网设备终端种类繁多，其中有相当一部分是低速率/低复杂度终端，如：各种定点探测设备（智能井盖、智能水表、智能电表、智能气表等）、环境监控设备（水质、水位监控）等。对于这类设备终端，网络侧在业务流程上进行优化，减少接口信令，加快小包数据传输。 
控制面EPS优化功能适用于上述低复杂度、非频发的小包数据传输场景。 
客户收益 :受益方|受益描述
---|---
运营商|使用控制面传输小包数据，MME不新增用户面进程，架构简单，部署方便。
物联网终端用户|不建立数据的无线承载，降低消耗。
实现原理 :系统架构 :控制面EPS优化的网络架构如下图所示。
MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输小包数据。
涉及网元 :网元名称|网元作用
---|---
NB-IoTUE|物联网终端，用NASPDU发送和接收小包数据（IP Data或Non-IP Data），并携带S1释放辅助信息。
E-UTRAN|支持NB-IoT终端接入，传递NAS PDU。通过S1-MME接口传输小包数据。
MME|传输上行和下行小包数据。完成S1-MME到S11-U面小包数据的转换传输。
SAE-GW|通过S11-U面传输小包数据。
协议栈 :NB-IoT控制面小包数据传输协议栈如下图所示。 
图1  NB-IoT控制面小包数据传输协议栈

本网元实现 :控制面小包数据传输优化的实现原理如下图所示。 
图2  控制面小包数据传输优化

传统的用户面数据传输，在UE IDLE态发起数据传输，流程复杂，信令开销远远大于数据包本身。优化如下： 
MME和UE间采用控制面通道，使用NAS信令传输小包数据，NAS信令小包数据通过空口RRC连接信令和S1初始化消息传输，MME和eNodeB间的S1接口信令可减少50%以上。 
MME和SAE-GW间通过S11-U用户面通道传输小包数据，MME通过控制面进程传输数据，极大简化了内部信令处理，提升了小包数据传输效率，完成NAS到GTP-U的协议转换。 
业务流程 :IP小包控制面传输流程包括：MO流程和MT流程。
控制面传输MO流程如下图所示。 
图3  控制面传输MO流程

控制面传输MO流程描述如下： 
UE附着完成后，UE发起RRC连接建立，消息中携带有NAS PDU。NAS
PDU中携带有EBI，用来标识同时携带的加密上行数据。NAS PDU用来携带小包数据IP Data。
UE携带的释放辅助信息，可以帮助MME及时完成S1释放。 
如果携带释放信息，同时指示无需后继数据，则说明当前的上行数据已经是所有应用数据的最后一包，不需要应答或者是响应，那么MME可以在上行数据传输后立即释放S1连接。 
如果携带释放信息，同时指示需要后继数据，则说明当前的上行数据需要应答或者是响应，是所有应用数据的最后一次交互，那么MME可以在收到下行数据并完成下行数据传输后立即释放S1连接。 
如果不携带释放信息，则MME不立即释放S1连接，处理UE和GW间的数据传输。直到收到释放信息，或者是eNodeB发起S1释放，MME才释放S1连接。 
空闲态的场景，eNodeB通过Initial UE消息发送该NAS PDU。该NAS消息为新增的Control Plane
Service Request消息，数据包携带在该消息的ESM Data Transport消息中。
MME进行完整性检查和消息解密。如果S11-U尚未建立，则MME发送修改承载请求，重建S11-U，SGW返回修改承载响应。MME通过S11-U接口，将上行数据报文封装在GTP-U消息中，发送给SGW。根据UE释放指示的决策，如果MME需要释放S1连接，则立即释放S1连接；如果MME不需要释放S1连接，则等待GW的下行数据传递。 
小包数据抵达GW，则GW发送该数据给MME。 
MME根据SGW返回的S11-U地址和GTP-U的端口进行报文收发。MME从GTP-U消息中得到下行数据报文后，封装NAS传输消息ESM
Data Transport，对消息进行加密和完整性保护后，投递给eNodeB。根据UE释放指示的决策，如果MME需要在下行数据传递后释放S1连接，则发起S1释放。 
eNodeB发送Downlink Information Transfer（包括NAS消息）给UE，并且在RRC连接检测定时器到时释放RRC连接。如果MME根据释放指示的决策没有释放S1连接，且一定时间内没有NAS消息投递，则eNodeB发起S1释放。 
控制面传输MT流程如下图所示。 
图4  控制面传输MT流程

控制面传输MT流程描述如下： 
UE附着完成。SGW收到下行数据报文，但发现没有S11-U承载，则缓存报文。SGW发送Downlink Data Notification消息给MME，消息中携带有EBI和ARP。
如果MME发现UE处于节电状态（PSM或者eDRX），无法响应寻呼，则计算用户能够建立无线承载的时间，通过Downlink
Data Notification响应消息通知SGW继续缓存报文，在UE可达前不要再下发Downlink Data Notification消息。
当UE已注册且可达，MME发送寻呼消息给eNodeB，eNodeB寻呼UE，UE收到寻呼消息后发起业务请求。eNodeB发送Initial
UE消息给MME。 
如果S11-U尚未建立，则MME发送修改承载请求，重建S11-U，SGW返回修改承载响应。MME根据SGW返回的S11-U地址和GTP-U的端口进行报文收发。MME从GTP-U消息中得到下行数据报文后，封装通用下行NAS投递消息ESM
Data Transport消息，对消息进行加密和完整性保护后，投递给eNodeB。eNodeB发送下行RRC消息携带NAS消息给UE。 
UE发送上行RRC消息携带NAS消息ESM Data Transport通过eNodeB给MME，MME进行完整性检查和消息解密。 
MME将上行数据报文通过S11-U发送给SGW，并根据消息中的释放辅助信息决策是否需要立即释放S1连接。如果MME根据释放指示的决策没有释放S1连接，且一定时间内没有NAS消息投递，则eNodeB发起S1释放。 
EDT（Early Data Transmission）数据流程如下图所示。 
图5  控制面优化MO EDT流程

EDT流程关键步骤描述如下，其他步骤同现有流程： 
步骤2： eNB收到UE的RRCEarlyDataRequest请求，在Initial UE message中携带 "EDT Session" indication给MME。 
步骤11： 
如果“Release assistance indication”指示没有预期的下行数据，第一包上行数据即完成数据传输且没有下行缓存数据。 
如果步骤2，eNB已指示"EDT Session" 并且“支持EDT”开关打开，MME处理如下：如果已有系统发送Service Accept（S1AP DL NAS TRANSPORT），则在S1AP DL NAS TRANSPORT中指示“End Indication”，指示：“no further data”，而不再发送S1AP UE Context Release Command。如果已有系统发送S1AP CONNECTION ESTABLISHMENT INDICATION，则在消息中指示“End Indication”，指示：“no further data”，而不再发送S1AP UE Context Release Command。如果已有系统没有发送S1AP DL NAS TRANSPORT和S1AP CONNECTION ESTABLISHMENT INDICATION，则MME为EDT功能发送S1AP CONNECTION ESTABLISHMENT INDICATION，在消息中指示“End Indication”，指示：“no further data”，不发送S1AP UE Context Release Command。 
如果“Release assistance indication”指示预期的下行数据，第一包上行数据加一包下行数据完成数据传送。 
如果步骤2，eNB已指示"EDT Session" 并且“支持EDT”开关打开，MME在S1AP DL NAS TRANSPORT消息中指示“End Indication”，指示：“no further data”，而不再发送S1AP UE Context Release Command。 
步骤12b：如果MME在S1AP消息中携带End Indication指示no further data，eNB可发送RRCEarlyDataComplete给UE。 
区分UE业务流程图如下图所示。 
图6  区分UE业务流程图

区分UE业务流程关键步骤描述如下： 
UE发起Attach业务流程，附着成功。 
SCC/AS向SCEF发送Update Request消息，携带CP（Communication-Pattern）参数。
SCS/AS使用该过程来添加、更改或删除UE的部分或全部CP参数集，例如： 
如果AS获知UE已经开始或停止了长时间的移动，则SCS/AS向SCEF提供相应的CP参数集以及有效时间。 
如果SCS/AS想与配置新CP参数集一起执行删除先前配置，则包含新CP参数集和取消的CP参数集标识。 
如果SCS/AS仅执行删除配置的CP参数集，则只需要携带删除的CP参数集标识。 
SCEF检查SCS/AS是否被授权向UE发送CP请求，过滤并根据运营商策略或配置选择用于添加/修改/删除的CP参数集。 
SCEF向HSS发送Update CP Parameter Request消息，以便为每个UE传递选定的CP参数集。消息中可能包含多个CP参数集。 
HSS检查更新CP参数请求消息，在UE的签约信息中存储CP参数集及其有效时间，以便在服务MME由于UE的移动性而改变时，将CP参数集转发给服务MME。 
HSS向SCEF返回Update CP Parameter Response消息。 
SCEF向SCC/AS返回Update Request消息。 
CP参数发生变化，HSS为每个UE发起Insert Subscriber Data Req过程，向MME发送具有相应有效期的CP参数集、SCEF参考ID和SCEF参考ID以进行删除。 
MME向HSS返回Insert Subscriber Data Ack，插入用户数据过程成功。 
在UE触发的业务流程中，在UE Information Transfer、Connection Establishment Indication、Downlink NAS Transport消息中，将终端Communication-Pattern信息通过UE Differentiation Information信元传递给eNodeB。 
无线侧根据终端的CP参数（传输周期、时间分布、传输模式、移动特点、节电要求），基站匹配不同的调度、DRX策略，优化资源。 
终端后续发起附着或者由于UE的移动性MME发生改变触发跨局TAU，MME向HSS发起位置更新过程。 
MME向HSS发送Update Location Request消息。 
HSS向MME返回Update Location Response消息，携带有效的CP参数集。 
eNodeB在第10步中通过过UE Differentiation Information信元接收终端Communication-Pattern信息，并进行资源调度与DRX策略操作。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :协议名称|章节
---|---
3GPP TS 23.720（Study on architecture enhancements for CellularInternet of Things）|6 Solutions
3GPP TS 23.401 （General Packet Radio Service (GPRS) enhancementsfor  Evolved Universal Terrestrial Radio Access Network (E-UTRAN)access）|4.10 Introduction of CIoT EPS Optimisations
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
##### LICENSE要求 
需要申请了“NB-IoT注册用户数”和“NB-IoT在线用户数”的License许可后，运营商才能获得NB-IoT用户接入核心网的服务。
需要申请了“MME支持物联网小包数据控制面传输优化”的License许可后，运营商才能获得物联网小包数据控制面传输优化特性的服务。
对其他网元的要求 :UE|eNodeB（E-UTRAN）|SGW|PGW|HSS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令MME GTPU地址配置SET MME GTPU IPSHOW MME GTPU IP表2  修改配置项配置项命令新增参数物联网业务配置SET MME IOT CFG支持控制面优化SHOW MME IOT CFG支持控制面优化VRF配置SET VRFCFGS11-U口VRF标识SHOW VRFCFGS11-U口VRF标识 
软件参数表3  新增软件参数软件参数ID软件参数名称262527NBIoT条件下ULR消息中RATType字段填写 
性能统计 :性能计数器名称
---
C430000150 EPS附着(CP)请求次数
C430000151 EPS附着(CP)成功次数
C430020056 控制面业务请求次数
C430020057 控制面业务请求成功次数
C432070008 从S11-U口发送的GTP-U数据包个数(个)
C432070010 从S11-U口发送的GTP-U数据包字节数(Byte)
C432070012 从S11-U口接收的GTP-U数据包个数(个)
C432070014 从S11-U口接收的GTP-U数据包字节数(Byte)
C432070016 S11-U口GTP上行包峰值速率(pps)
C432070017 S11-U口GTP下行包峰值速率(pps)
C432070018 S11-U口GTP上行字节峰值速率(KB/s)
C432070019 S11-U口GTP下行字节峰值速率(KB/s)
C432000084 Connection EstablishmentIndication消息发送次数
C432090002 接收ESM DATA Transport消息次数
C432090003 发送ESM DATA Transport消息次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置，可实现物联网小包数据控制面传输优化功能。 
通过该配置，可实现MME通过Subscription Based UE Differentiation Information信元向eNB传递NB IoT的数据传输周期、传输时间分布、数据传输模式、移动还是静止、节电要求等，基站可以通过这些信息，匹配不同的调度、DRX等策略。 
配置前提 :对于物联网小包数据控制面传输优化功能，需要规划好MME和SGW间的S11-U用户面地址。 
配置过程 :打开MME“支持物联网小包数据控制面传输优化”功能开关。
配置MME S11-U用户面地址。 
实现MME向无线传递Subscription Based UE Differentiation Information信元的功能。 
执行[SET MME IOT CFG]命令，MME开启支持NB-IoT网络UE differentiation功能。
执行[ADD SUPFEATURE]命令或者[SET SUPFEATURE]命令，配置Support Feature 2支持CP ，用于指示MME支持AESE communication patterns能力。
配置实例 :##### 配置MME使用物联网小包数据控制面传输 
MME需要打开“支持物联网小包数据控制面传输优化”功能开关，并配置MME S11-U的用户面地址。
配置步骤|配置说明
---|---
SET MME IOT CFG:CPSW="YES"|打开MME“支持物联网小包数据控制面传输优化”功能开关。
SET MME GTPU IP:S11UIPADDR=192.20.66.210|配置MME S11-U用户面地址。
##### 配置MME支持CP模式的UE differentiation功能 
MME需要打开“支持UE differentiation功能”功能开关，并配置Support Feature 2，支持 “Communication Pattern”。
配置步骤|配置说明
---|---
SET MME IOT CFG: SPRUEDIFFERENTIATION="ON"|打开MME“支持UE differentiation功能”功能开关。
ADD SUPFEATURE: FEATUREID=10,SUPFEATURE="NULL",SUPFEATURE2="CP"|增加Support Feature模板配置，基于用户的IMSI或用户所在HSS局向ID选择支持"Communication Pattern"功能的模板，支持"Communication Pattern"。
SET SUPFEATURE:FEATUREID=10,SUPFEATURE2="CP"|修改已有的Support Feature模板配置，改变现有Support Feature模板中的能力，支持"Communication Pattern"。
测试用例 :测试项目|MME支持物联网小包数据控制面传输优化
---|---
测试目的|测试MME支持物联网小包数据控制面传输优化。
预置条件|MME网元各项对接和业务配置完毕。用户取得MME网元支持物联网小包数据控制面传输优化功能的license授权，并更新了license。
测试过程|开启支持物联网小包数据控制面传输优化功能开关，并配置MMES11-U用户面地址。物联网终端开机发起附着，使用控制面传输优化模式接入。终端和应用服务器间传输用户数据。
通过准则|终端使用控制面传输优化模式接入到MME成功。终端和应用服务器间的用户数据使用控制面模式传输成功。
测试结果|-
测试项目|NB-IoT模式下，Attach流程下发UE differentiation参数
---|---
测试目的|测试NB-IoT Control Plane在附着过程中可以正确下发UE differentiation参数，上下文中用户签约UE differentiation信息正确。
预置条件|“支持UE differentiation功能”配置开关打开，配置Support Feature 支持CP。用户从NB-IOT接入。
测试过程|NB-IoT Control Plane在附着过程中，通过ULA获取到UE通信模式参数AESE-Communication-Pattern，并存储到用户上下文。MME通过attachaccept的DNT消息和ConnectionEstablishmentIndication消息下发ULA签约的SubscriptionBasedUEDifferentiationInformation给eNB。
通过准则|附着过程中MME向HSS发起位置更新流程，发送的ULR消息中支持Communication Pattern（CP）Feature，MME接收到成功的ULA消息后将CP模式参数存储到上下文中。MME通过attach accept的DNT消息和Connection Establishment Indication消息下发ULA签约的Subscription Based UE Differentiation Information给ENB。查询MME用户签约信息返回的“AESE-Communication-Pattern”是ULA签约的保存值。
测试结果|-
测试项目|NB-IoT模式下，IDR流程更新UE differentiation参数，TAU流程下发UE differentiation参数
---|---
测试目的|NB-IoT模式下，IDR流程更新UE differentiation参数，TAU流程正确下发UE differentiation参数。
预置条件|“支持UE differentiation功能”配置开关打开，配置Support Feature 支持CP。用户从NB-IOT接入。
测试过程|NB-IoT Control Plane用户发起附着，ULA下发签约信息中携带UE通信模式参数AESE-Communication-Pattern，存在单组CP参数，CP参数中SCEF-Reference-ID有效。附着成功后，HSS向MME发送IDR消息，签约信息中携带多组的UE通信模式参数AESE-Communication-Pattern发生变化，CP参数中SCEF-Reference-ID与附着时ULA下发的不一致。IDR成功后，用户发起局内TAU流程。
通过准则|MME通过TAU accept的DNT消息和Connection Establishment Indication消息下发IDR签约的Subscription Based UE Differentiation Information给eNB。Subscription Based UE Differentiation Information信元中携带对应的UE通信模式的参数。包括：PeriodicCommunicationIndicator、PeriodicTime、ScheduledCommunicationTime、DayofWeek、TimeofDayStart、TimeofDayEnd、Stationary、Indication、TrafficProfile、BatteryIndication。
测试结果|-
测试项目|用户签约信息变化时，IDR删除用户上下文中老的UE通信模式数据
---|---
测试目的|用户签约信息变化时，IDR删除用户上下文中老的UE通信模式数据。
预置条件|“支持UE differentiation功能”配置开关打开，配置Support Feature 支持CP。用户从NB-IOT接入。
测试过程|NB-IoT Control Plane用户携带SMSOnly发起CP模式附着，ULA下发签约信息中携带UE通信模式参数AESE-Communication-Pattern，存在多组CP参数，CP参数中SCEF-Reference-ID有效。SGS口更新成功。附着成功后，HSS向MME发送IDR消息，签约信息中携带UE通信模式参数AESE-Communication-Pattern，没有SCEF-Reference-ID，存在多个SCEF-ReferenceID-Deletion，其中一个SCEF-Reference-ID-for-Deletion有效与附着时ULA下发的一致。IDR成功后，eNB发起RetrieveUEInfomation请求。用户在CONNECTED状态下SGS口收发短消息。
通过准则|附着过程中MME向HSS发起位置更新流程，发送的ULR消息中支持Communication Pattern（CP）Feature，MME接收到成功的ULA消息后选取第一组CP模式参数存储到上下文中。MME通过attach accept的DNT消息和Connection Establishment Indication消息下发ULA签约的Subscription Based UE Differentiation Information给eNB。查询MME用户签约信息返回的“AESE-Communication-Pattern”是ULA签约的保存值。IDR流程判断上下文中的SCEF-Reference-ID和SCEF-Reference-ID-for-Deletion一致，删除用户上下文中老的UE通信模式数据。UEInfomationTransfer消息不会下发Subscription Based UE Differentiation Information给ENB。短消息的DNT消息不会下发Subscription Based UE Differentiation Information给ENB。查询MME用户签约信息不返回“AESE-Communication-Pattern”。
测试结果|-
常见问题处理 :无。 
# ZUF-78-17-004 物联网用户面EPS优化 
特性描述 :特性描述 :描述 :定义 :物联网用户面EPS优化功能，适用eMTC，也适用NB-IoT。UE在ECM-IDLE和ECM-CONNECTED态之间转换时，MME使用Suspend和Resume流程，代替了S1
Release和Service Request流程，大大减少了无线信令。 
应用场景 :物联网用户面EPS优化适用于低移动性、频繁的数据发送接收场景。 
物联网用户面优化的主要目的是：解决UE在IDLE态到CONNECT态转换时，业务请求过程中重建承载和上下文所带来的信令和资源消耗。 
物联网用户面优化可实现：当UE建立好承载和上下文，随后就可以使用挂起和恢复流程来替代原有的释放和重建流程。 
当使用挂起流程时： 
UE进入IDLE态，保存AS信息。 
eNodeB保存AS信息、S1AP连接以及承载上下文。 
MME保存S1AP连接以及承载上下文，进入IDLE态。 
随后恢复时： 
UE使用挂起时保存的AS信息进行恢复。 
eNodeB通知MME恢复。 
MME侧进入连接态。 
客户收益 :受益方|受益描述
---|---
运营商|用户在IDLE态和CONNECT态之间转换时，可减少无线信令消耗。
物联网终端用户|能快速恢复无线承载。
实现原理 :系统架构 :用户面EPS优化的网络架构如下图所示。

涉及的网元 :网元名称|网元作用
---|---
CIoTUE|物联网终端，用NASPDU发送和接收小包数据，并携带S1释放辅助信息。
E-UTRAN|支持NB-IoT终端接入，传递NAS PDU。通过S1-U面传输小包数据（IP Data）。
MME|支持物联网终端接入，辅助创建S1-U面。
SAE-GW|通过S1-U面传输小包数据（IP Data）。
协议栈 :NB-IoT用户面小包数据传输协议栈如下图所示。 
图1  NB-IoT用户面小包数据传输协议栈

本网元实现 :用户面小包数据传输优化的实现原理如下图所示。 
图2  用户面小包数据传输优化

MME利用为UE保留的S1AP上下文和承载上下文，快速恢复无线承载和网关承载，提升数据传输速度。 
业务流程 :IP小包数据用户面传输流程：eNodeB和SAE-GW间使用S1-U面进行数据传送，和普通EPC网络数据传送一样。
用户面小包数据传输优化关键流程包括：SUSPEND和RESUME。 
SUSPEND
SUSPEND流程如下图所示。 
图3  SUSPEND流程

SUSPEND流程描述如下： 
eNodeB使用新增的S1AP消息UE Context Suspend Request向MME发起挂起流程，UE进入IDLE态。MME为UE保留有S1AP上下文和承载上下文，包括MME和eNodeB的S1AP
ID，eNodeB的S1-U地址和TEID，SGW的地址和TEID等。
MME发送Release Access Bearers Request消息，通知SGW释放S1-U连接。 
SGW释放eNodeB的相关信息，包括地址和下行的TEID等，返回Release Access Bearers Response消息。此后如果有下行报文，将触发DDN流程。
MME收到释放接入承载响应后，向eNodeB发送UE Context Suspend Response消息。 
eNodeB发送RRC Connection Suspend消息。 
RESUME流程
RESUME流程如下图所示。 
图4  RESUME流程

RESUME流程描述如下： 
Random Access。 
UE因上行业务或寻呼，引发连接恢复流程。 
eNodeB使用新增的S1AP消息UE Context Resume Request向MME发起恢复流程，UE进入CONNECT态。 
MME返回UE Context Resume Response消息给eNodeB，消息中携带为UE保存的S1AP上下文和承载上下文信息，包括MME和eNodeB的S1AP
ID，eNodeB的S1-U地址和TEID，SGW的地址和TEID等。 
如果步骤4中，MME携带了需要拒绝的承载列表，则eNodeB重新配置无线承载。 
上行数据此时可根据之前保存的SGW地址和TEID进行发送。 
MME发送Modify Bearer Request消息给SGW，消息中携带保存的eNodeB的S1-U地址和下行TEID，此时SGW可以发送下行报文给eNodeB。 
SGW向MME返回Modify Bearer Response消息，SGW的S1-U地址和上行TEID保持不变。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :协议名称|章节
---|---
3GPP TS 23.720（Study on architecture enhancements for CellularInternet of Things）|6 Solutions
3GPP TS 23.401 （General Packet Radio Service (GPRS) enhancementsfor  Evolved Universal Terrestrial Radio Access Network (E-UTRAN)access）|4.11 User Plane CIoT EPS Optimization
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
##### LICENSE要求 
需要申请了“MME支持物联网小包数据用户面传输优化”的License许可后，运营商才能获得物联网小包数据用户面传输优化特性的服务。
对其他网元的要求 :UE|eNodeB（E-UTRAN）|SGW|PGW|HSS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  修改配置项配置项命令新增参数物联网业务配置SET MME IOT CFG支持用户面优化SHOW MME IOT CFG支持用户面优化 
软件参数表2  新增软件参数软件参数ID软件参数名称262527NBIoT条件下ULR消息中RATType字段填写 
性能统计 :性能计数器名称
---
C430000152 EPS附着(UP)请求次数
C430000153 EPS附着(UP)成功次数
C432000085 UE CONTEXT SUSPEND REQUEST消息接收次数
C432000086 UE CONTEXT SUSPEND RESPONSE消息发送次数
C432000087 UE CONTEXT RESUME REQUEST消息接收次数
C432000088 UE CONTEXT RESUME RESPONSE消息发送次数
C432000089 UE CONTEXT RESUME FAILURE消息发送次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过该配置，可实现物联网小包数据用户面传输优化功能。 
配置前提 :EPC各网元正常工作，用户可接入EPC核心网进行数据业务。 
配置过程 :打开MME“支持物联网小包数据用户面传输优化”功能开关。
打开MME“支持NB-IoT接入时采用S1-U承载进行数据传输”功能开关。
配置实例 :配置MME使用物联网小包数据用户面传输，支持物联网用户NB-IoT接入时采用S1-U承载进行数据传输。 
MME需要打开“支持物联网小包数据用户面传输优化”功能开关，打开“支持NB-IoT接入时采用S1-U承载进行数据传输”功能开关。
配置步骤|配置说明
---|---
SET MME IOT CFG:UPSW="YES";|打开MME“支持物联网小包数据用户面传输优化”功能开关。
SET MME IOT CFG:NBS1U="YES";|打开MME“支持NB-IoT接入时采用S1-U承载进行数据传输”功能开关。
测试用例 :测试项目|MME支持物联网小包数据用户面传输优化
---|---
测试目的|测试MME支持物联网小包数据用户面传输优化
预置条件|MME网元各项对接和业务配置完毕。用户取得MME网元支持物联网小包数据用户面传输优化功能的license授权，并更新了license。
测试过程|开启支持物联网小包数据用户面传输优化功能开关。物联网终端开机发起附着，使用用户面传输优化模式接入。终端和应用服务器间无用户数据传输，eNodeB发起S1上下文的Suspend流程。终端和应用服务器间有数据交互，触发了S1上下文的Resume流程。终端和应用服务器间传输用户数据。
通过准则|终端使用用户面传输优化模式接入到MME成功。eNodeB发起Suspend流程，MME保存S1上下文，并通知SGW释放S1用户面。用户触发Resume流程，MME恢复S1用户面。终端和应用服务器间的用户数据使用用户面模式传输成功。
测试结果|–
常见问题处理 :无。 
# ZUF-78-17-005 海量接入 
特性描述 :特性描述 :术语 :术语|含义
---|---
NB-IoT|窄带物联网，是由3GPP定义的基于蜂窝网络的窄带物联网技术标准，是一种专为物联网设计的窄带射频技术，以广连接、低功耗、低成本、低移动和深覆盖为特点，可应用于GSM网络、UMTS网络和LTE网络。
描述 :定义 :NB-IoT海量接入，是指低复杂度、低功耗、低速率的物联网终端基于NB-IoT物联网技术接入EPC网络，其数量为亿级单位，是智能手机终端的数十甚至上百倍。
背景知识 :预测2025年全球物联网连接数量达270亿个，来自市场研究公司MachinaResearch的最新数据如[图1]所示。
图1  NB-IoT在线用户数

2015年，全球物联网连接数量为60亿个。根据预期，到2025年这一数字将增至270亿个，中国将占据21%的全球物联网连接数。据预测2015-2025年10年间全球人口增长约10亿，相对人网的发展，物联网连接数是急剧增长的。 
在巨大的物联网连接总数中，移动物联网设备终端将会占据不少份额，因为电信运营商不仅是基础网络的拥有者，同时还拥有大量企业用户，最有望成为物联网产业的主导者，而网络连接数也终将取代用户数成为衡量运营商增长的全新指标。 
全球物联网连接数量及物联网收入在2015年-2025年之间将增长三倍，从而为电信运营商提供一个拓展新业务收入的机会，尤其是那些在企业IT服务领域具有经验的电信运营商，既是机会也是挑战，运营商首当其冲面临电信网络如何容纳数百亿物联网连接的问题。 
目前占据物联网市场主要的应用需求聚焦在海量接入、低速率、高时延应用，采用NB-IoT技术解决此类应用需求。但是数量庞大的NB-IoT物联网设备终端，如大量的水电表监测、水质/水位监测、井盖监测设备、烟雾报警等设备，其话务模型虽然小，可能只有公众网络智能手机类的终端的5%～10%甚至更低，个体上却存在和人网手机类终端一样的存储需求，而且其数量可能是人网终端的10~20倍，甚至更多，目前的2G、3G和4G系统存储容量受限，物网终端的接入和人网用户的接入无法完全隔离，容量上相互制约，满足不了海量的终端信息存储需求。 
另外，海量的物联网终端接入EPS网络后，如果发生物联网服务器故障、终端特殊应用、突发事件等，使得这些终端的业务在同一时间段内爆发，其业务量短时急剧增加，某类物网用户或某项应用挤占了大量的网络资源，影响了其他用户的正常业务，引发系统拥塞。目前的2G、3G和4G系统，不区分人和物以及不同的业务和应用，满足不了分级实施拥塞控制的需求。 
应用场景 :NB-IoT海量接入需要解决两类应用问题：
海量接入。 
特定业务和用户的拥塞。 
编号|应用|需求|解决策略
---|---|---|---
1|海量接入|容纳亿级物联网终端接入|海量存储优化
2|特定业务和用户的拥塞|不因某类用户或某项应用挤占大量的网络资源，而对其他用户的正常业务产生影响。|拥塞控制优化
##### 海量接入：海量存储优化 
场景描述
很多物联网终端设备其数量庞大，如智能路灯、智能垃圾桶、智能井盖、智能水表、智能电表、智能气表等。移动物联网首要解决海量终端接入的问题。 
场景分析
对于数量庞大的物联网设备终端，其话务模型虽然小，可能只有公众网络智能手机类的终端的5%～10%甚至更低，个体上却存在和人网手机类终端一样的存储需求，而且其数量可能是人网终端的10~20倍，甚至更多，如何容纳亿级终端接入，是核心网需要解决的关键问题；这类物联网设备终端的话务量很低，但用户信息需要长时间保存在MME上，因此MME要支持海量接入，关键要解决海量存储。 
海量存储优化
海量存储优化：基于用户分类/分组实现用户数据共享管理。 
MME依据物网终端和人网用户的业务特征不同，将物网终端用户和人网终端用户数据管理和存储隔离，实现用户数据的分类，对用户数据分类管理和存储，如[图2]所示。
图2  用户数据存储模型

用户数据的分类依据： 
用户终端特性。 
用户签约的业务特性。 
将同特性的用户数据，使用模板共享管理，业务层共享数据管理。如[图3]所示。
图3  用户数据管理模型

签约上下文共享存储：同一设备组签约数据共享，MME完成数据共享的分析，基于模板共享数据管理。 
用户上下文精简：设置独立的上下文，根据NB-IoT业务特性进行精简。设备能力共享存储。变长存储。 
MME通过共享数据管理和存储，大幅降低每用户数据的存储需求以及签约数据传输消耗，在同等硬件资源条件下，使得终端接入数大幅提升，满足海量接入需求。 
##### 特定业务和用户的拥塞：拥塞控制优化 
场景描述
海量的物联网终端接入EPS网络后，如果发生物联网服务器故障、终端特殊应用、突发事件等，使得这些终端的业务在同一时间段内爆发，其业务量短时急剧增加，引发系统拥塞。
场景分析
某类物网用户或某项应用挤占了大量的网络资源，影响了其他用户的正常业务，网络区分人与物，区分不同的业务和应用，分级实施拥塞控制，限制挤占了大量的网络资源的用户业务和应用。 
拥塞控制优化
拥塞控制优化：包括特定业务和用户的拥塞控制、业务接入优先级控制，基于终端类别和优先级的分级业务保障。 
MME实现智能化分级的拥塞控制和业务保障，在多个维度区分人与物以及不同的业务和应用，精细控制，保证不会因某类用户或某项应用挤占大量的网络资源，通过分级的拥塞控制，既保障了正常的业务通过量，又确保网络的负荷平衡。如[图4]所示。
图4  拥塞控制优化

智能化分级的多个维度如下： 
用户应用优先级，如：物联网应用、普通应用。 
用户签约优先级，如：签约了特定Group ID的用户。 
业务优先级，如：语音、MPS等。 
接入优先级，分高低优先级。 
业务流程优先级，如：附着、TAU、PDN连接。 
客户收益 :受益方|受益描述
---|---
运营商|增加收入：网络容纳亿级物联网终端接入，有助于运营商增加来自物联网的收入。提高系统可靠性：防止设备被突发的大量业务冲击，在突发大话务情况下，不会异常或者崩溃，提高网络的稳定性。
物联网终端用户|用户享受更稳定和更可靠的网络服务。
实现原理 :系统架构 :3GPP定义的NB-IoT网络架构如下图所示。
图5  NB-IoT网络架构图

涉及的网元 :NB-IoT由UE、CIoT-BS和MME配合完成。
网元名称|网元作用
---|---
UE|物联网终端，以NB-IoT方式接入网络。接收MME的拒绝消息，启动back-off timer，超时前不发起业务。
CIoT-BS|支持NB-IoT终端接入，传递NAS PDU。
MME|基于用户分类/分组实现用户数据共享管理，容纳亿级物联网终端接入。完成基于APN和MTC Group Identifier的拥塞控制；完成业务接入优先级控制。
本网元实现 :MME网元NB-IoT海量接入包括如下处理： 
海量存储优化 
特定业务和用户的拥塞基于APN的拥塞控制优化基于MTC用户的拥塞控制优化业务接入优先级控制（LAPI）优化 
海量存储优化
基于用户分类/分组实现用户数据共享管理，同业务特性用户群数据共享管理，大幅降低每用户数据的存储需求以及签约数据传输消耗；无业务流程。 
基于APN的拥塞控制优化
针对特定的APN，MME可控制用户发起业务，避免对APN对应的PGW POOL造成信令与承载冲击。
MME可基于下面四个条件判断是否拒绝业务： 
业务使用的APN在MME已建立承载数超过配置门限。 
业务使用的APN在MME建立承载速率超过配置门限。 
签约此APN的用户发送NAS MM信令速率超过门限。 
该APN对应的PGW指示APN拥塞，且在有效期内。 
MME在拒绝消息中携带Back-Off Timer，通知用户在一段时间内不再发起移动性管理或会话管理业务，减小发送到PGW的信令数及减少PGW承载资源占用。 
其中，满足条件1和条件2控制的会话管理类流程包括： 
附着 
PDN连接请求 
承载资源申请 
承载资源修改 
满足条件3控制的移动性管理类流程包括： 
附着 
TAU 
业务请求 
满足条件4控制的会话管理类流程包括： 
附着 
PDN连接请求 
基于MTC用户的拥塞控制优化
MME可控制签约了特定Group ID的用户，拒绝此类用户发起的业务；同时MME也可以控制签约了特定Group
ID与使用某APN或签约某特定APN的用户，拒绝此类用户发起业务，以便APN对应的PGW POOL保留资源提供给其他用户。 
MME在拒绝消息中携带BackOff Time，通知用户在一段时间内不再发起业务，以避免对MME网元造成冲击。 
MME接收到此类用户发起的业务，进行如下处理： 
MME中签约此Group ID的这类用户发送NAS信令速率超过门限；MME将限制相关的移动性管理与会话管理业务：附着TAU业务业务请求PDN连接请求承载资源申请承载资源修改 
MME中签约此Group ID与使用此APN的这类用户建立承载数超过门限；MME将限制签约了特性Group ID的用户不再发起此APN相关的会话管理业务：附着PDN连接请求承载资源申请承载资源修改 
MME中签约此Group ID与签约此APN的这类用户发送NAS信令速率超过门限；MME将限制签约此Group ID与签约此APN的用户不再发起移动性管理业务：附着TAU业务请求 
业务接入优先级控制（LAPI）优化
当系统拥塞时MME对于低优先接入的业务优先拒绝，或主动下线，并在一段时间内禁止进行低优先级接入业务，保障其他非低优先级接入的业务。 
系统影响 :开启拥塞控制后，当系统处于拥塞的情况下，会采用简单有效的方法拒绝部分业务处理，从而降低系统负荷；拥塞控制本身对系统处理能力和资源消耗可以忽略。 
应用限制 :如果UE不支持退避时间（Backoff Time）的处理，将会一定程度上弱化拥塞控制的效果；虽然MME可以对处于退避时间内的UE实施持续的接入控制，但是如果UE在短时间内多次发起尝试，还是对网络处理能力和资源有少许消耗。
特性交互 :无。 
遵循标准 :协议|章节号及章节名称
---|---
3GPP TS 23.720: " Study on architecture enhancements forCellular Internet of Things"|6节: Solutions
3GPP TS 23.401: “General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access”|4.3.7.4 MME control of overload
特性能力 :特性|能力
---|---
支持APN拥塞控制的最大APN个数|256（个）
可获得性 :License要求 :该特性需要申请了License “NB-IoT注册用户数”和“NB-IoT在线用户数”许可后，运营商才能获得NB-IoT海量接入的服务。 
该特性需要申请了License “MME支持基于APN拥塞控制功能”、“MME支持基于MTC用户拥塞控制功能”和“MME支持LAPI”许可后，运营商才能获得特定业务和用户的拥塞控制的服务。 
对其他网元的要求 :UE需要支持Back-off Timer和低优先级指示。 
SGW/PGW需要支持GTP-C过负荷控制功能。 
O&M相关 :命令 :新增配置项参见表2。表2  新增配置项配置项命令基于APN拥塞控制开关SET APN CONGESTION SWITCHSHOW APN CONGESTION SWITCHAPN拥塞控制策略配置ADD APN CONGESTION POLICYSET APN CONGESTION POLICYDEL APN CONGESTION POLICYSHOW APN CONGESTION POLICY基于MTC用户的MME网元拥塞控制开关SET MTCMME CONGESTION SWITCHSHOW MTCMME CONGESTION SWITCHMTC用户的MME网元拥塞控制策略配置ADD MTCMME CONGESTION POLICYSET MTCMME CONGESTION POLICYDEL MTCMME CONGESTION POLICYSHOW MTCMME CONGESTION POLICY基于MTC用户的APN拥塞控制开关SET MTCAPN CONGESTION SWITCHSHOW MTCAPN CONGESTION SWITCHMTC用户的APN拥塞控制策略配置ADD MTCAPN CONGESTION POLICYSET MTCAPN CONGESTION POLICYDEL MTCAPN CONGESTION POLICYSHOW MTCAPN CONGESTION POLICY 
软件参数新增软件参数参见表3。表3  新增软件参数软件参数ID软件参数名称262493TAU业务是否支持NAS拥塞控制262494业务请求是否支持NAS拥塞控制262495承载修改是否支持NAS拥塞控制262496已下发移动性管理BackOff Time再次接入拒绝携带原因262497已下发会话管理BackOff Time再次接入拒绝携带原因262498MME过负荷控制是否拒绝连接态262570控制面业务请求是否支持NAS拥塞控制 
性能统计 :该特性暂不涉及性能统计。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过NB-IoT海量接入特性的相关配置，实现MME对物联网终端的海量存储，支持海量物联网终端接入。
配置前提 :MME网元各项对接和业务配置完毕。
配置过程 :配置基于APN的拥塞控制过程。
使用[SET APN CONGESTION SWITCH]命令，开启基于APN拥塞控制功能。
使用[ADD APN CONGESTION POLICY]命令，配置基于APN拥塞控制策略。
配置基于MTC用户的MME网元拥塞控制功能过程。
使用[SET MTCMME CONGESTION SWITCH]命令，开启基于MTC用户的MME网元拥塞控制功能。
使用[ADD MTCMME CONGESTION POLICY]命令，配置基于MTC用户的MME网元拥塞控制策略。
配置基于MTC用户的APN拥塞控制功能。 
使用[SET MTCAPN CONGESTION SWITCH]命令，开启基于MTC用户的APN拥塞控制功能。
使用[ADD MTCAPN CONGESTION POLICY]命令，配置基于MTC用户的APN拥塞控制策略。
配置实例 :##### 配置基于APN的拥塞控制 
配置过程如下： 
步骤|命令|说明
---|---|---
1|SET APN CONGESTION SWITCH:ISSUPCONAPN="YES";|打开基于APN拥塞控制功能。
2|ADD APN CONGESTION POLICY:APN="pc1.auto.local.apn.epc.mnc011.mcc460.3gppnetwork.org",TYPE="BEARERNUM",MAXBEAR=20,MINDELAY=8,MAXDELAY=9,GUABEAR=10;|配置基于APN拥塞控制策略，APN名称为pc1.auto.local.apn.epc.mnc011.mcc460.3gppnetwork.org、拥塞控制类型为承载建立数、最大建立承载数为20、拒绝时携带的Back-offTimer最小取值为8秒、拒绝时携带的Back-off Timer最大取值为9秒、可保障建立承载数为10。
##### 配置基于MTC用户的MME网元拥塞控制功能 
配置过程如下： 
步骤|命令|说明
---|---|---
1|SET MTCMME CONGESTION SWITCH:ISSUPCONMTCMME="YES";|打开MTC用户的MME网元拥塞控制功能。
2|ADD MTCMME CONGESTION POLICY:MTCGRPID="460"-"02"-1,TYPE="NASMMRATE",MAXNASMM=100,GUANASMM=50,LOWMIN=60,LOWMAX=180;|配置MTC用户的MME网元拥塞控制策略，MTC组ID为"460"-"02"-1、拥塞控制类型为接收NASMM信令速率类型、最大接收NAS MM信令速率为100、可保障接收NASMM信令速率为50、统计周期默认为秒，也支持分钟，低优先级拒绝时携带的Back-off Timer最小取值为60秒、低优先级拒绝时携带的Back-off Timer最大取值为180秒。
##### 配置基于MTC用户的APN拥塞控制功能 
配置过程如下： 
步骤|命令|说明
---|---|---
1|SET MTCAPN CONGESTION SWITCH:ISSUPCONMTCAPN="YES";|打开基于MTC用户的APN拥塞控制功能。
2|ADD MTCAPN CONGESTION POLICY:MTCGRPID="460"-"02"-1,APN="pc1.auto.local.apn.epc.mnc011.mcc460.3gppnetwork.org",TYPE="BEARERNUM",MAXBEAR=100,GUABEAR=60,LOWMIN=60,LOWMAX=180;|配置基于MTC用户的APN拥塞控制策略，MTC组ID为"460"-"02"-1、APN名称为pc1.auto.local.apn.epc.mnc011.mcc460.3gppnetwork.org、拥塞控制类型为承载建立数、最大建立承载数为100、可保障建立承载数为60、统计周期默认为秒，也支持分钟，低优先级拒绝时携带的Back-offTimer最小取值为60秒、低优先级拒绝时携带的Back-off Timer最大取值为180秒。
测试用例 :MME支持物联网终端海量接入
测试项目|MME支持物联网终端海量接入
---|---
测试目的|测试MME支持物联网终端海量接入
预置条件|MME各项对接和业务配置完毕。已取得“MME支持物联网小包数据控制面传输优化”功能的license授权，并更新了license。用户取得MME支持“NB-IoT注册用户数”的license授权，并更新了license。
测试过程|开启支持物联网小包数据控制面传输优化功能开关，并配置MME S11-U用户面地址。500万个物联网终端开机发起附着，使用控制面传输优化模式接入。
通过准则|500万个终端使用控制面传输优化模式成功接入到MME。
测试结果|
MME支持针对物联网终端的基于APN的拥塞控制
测试项目|MME支持针对物联网终端的基于APN的拥塞控制
---|---
测试目的|测试MME支持针对物联网终端的基于APN的拥塞控制
预置条件|MME各项对接和业务配置完毕。已取得“MME支持基于APN拥塞控制功能”的license授权，并更新了license。MME打开支持按APN拥塞控制功能开关。MME配置APN1拥塞控制策略：拥塞控制类型配置为“承载建立数”，最大建立承载数配置为5，可保障建立承载数配置为3，配置Back-offTimer最小取值50秒和最大取值60秒。
测试过程|5个物联网终端开机附着，使用APN1建立5个承载。另外5个物联网终端用APN1发起附着流程。
通过准则|终端附着被拒绝，AttachReject消息中携带的拒绝原因为congestion，并且携带backofftime字段，取值是50秒到60秒之间的随机值。
测试结果|
MME支持针对物联网终端基于MTC用户的拥塞控制
测试项目|MME支持针对物联网终端基于MTC用户的拥塞控制
---|---
测试目的|测试MME支持针对物联网终端基于MTC用户的拥塞控制
预置条件|MME各项对接和业务配置完毕。已取得“MME支持基于MTC用户拥塞控制功能”和“MME支持LAPI”的license授权，并更新了license。MME打开“支持MTC用户的MME网元拥塞控制”功能开关。MME配置MTC用户的MME网元拥塞控制策略：配置GroupID1的拥塞控制类型为“接收NAS MM信令速率”，最大接收NASMM信令速率为50，可保障NAS MM信令速率为30，统计周期为秒。通知终端延时区间为20 s~40 s，拒绝比例为100%，低优先级拒绝时携带的Back-offTimer最小取值50秒和最大取值60秒。用户签约GroupID1支持拥塞控制。
测试过程|多个没有签约GroupID1的物联网终端同时开机，保证GroupID1的NAS MM信令速率大于30小于50。一个签约GroupID1支持拥塞控制的物联网终端开机发起附着流程。
通过准则|签约GroupID1支持拥塞控制的物联网终端附着被拒绝，AttachReject消息中携带的拒绝原因为congestion，并且携带backofftime字段，取值是50秒到60秒之间的随机值。
测试结果|
MME支持针对物联网终端业务接入优先级控制
测试项目|MME支持针对物联网终端业务接入优先级控制
---|---
测试目的|测试MME支持针对物联网终端业务接入优先级控制
预置条件|MME各项对接和业务配置完毕。已取得“MME支持基于APN拥塞控制功能”的license授权，并更新了license。MME打开支持按APN拥塞控制功能开关。MME配置APN1拥塞控制策略：拥塞控制类型配置为“承载建立数”，最大建立承载数配置为5，可保障建立承载数配置为3，配置Back-offTimer最小取值50秒和最大取值60秒。
测试过程|3个物联网终端开机附着，使用APN1建立3个承载。另外1个物联网终端用APN1发起附着流程，Attach Request消息携带Device Property字段为低优先级。
通过准则|附着流程失败，MME下发AttachReject消息，cause值为insufficient resources，并且携带backofftime字段，取值是50秒到60秒之间的随机值。
测试结果|
常见问题处理 :无。 
# ZUF-78-17-006 节电智能 
特性描述 :特性描述 :术语 :无。 
描述 :定义 :NB-IoT节电是为了应对LPWAN下终端超低功耗需求而引入的新功能，包括PSM和eDRX两种节电技术，同时衍生出节电时HLCom功能。
PSM：该模式通过类似关机（关闭无线接收单元）机制来达到节电目的，只是UE仍注册在网络中，恢复业务时不需要重新附着并重建PDN连接。 
eDRX：在现有DRX技术上进行扩展，通过大幅扩展休眠周期（从秒级到分钟、数十分钟甚至小时）达到节电目的。 
HLCom：节电时EPC缓存下行数据延时下发，保证数据可靠传输。 
DRX：无线接口包的数据流通常是突发性的，在没有数据传输时，可以通过DRX关闭UE的接收电路来降低功耗，从而提升电池使用时间。 
MME负责为不同用户，不同的物联网应用场景制定不同的节电策略；与UE协商节电参数；管理UE节电状态；通知SGW缓存下行数据，保证节电状态下的可靠数据传输等功能。
背景知识 :物联网终端面临节电的挑战
NB-IoT主要服务于移动物联网终端，参见[表1]。节电（低功耗）在环境监测、动物追踪等行业应用中属于关键需求，待机时间要求以年为单位甚至更高。
场景|应用举例|节电需求|目标
---|---|---|---
电池更换困难或无法更换|野生动物追踪恶劣环境下的环境监测|电池的使用寿命即传感器的生命周期。|超低功耗，待机时间超一般超过5年。
电池可更换|物流追踪资产监测|这类传感设备一般属于集团企业批量采购，如果频繁更换电池，会增加损耗及人力成本。|低功耗，待机时间以年为单位。
可持续供电|智能电表智能家电|低功耗不是主要需求，但持续节电同样也可以积少成多，降低成本。|无明确需求。
传统2/3/4G蜂窝网络主要服务于智能手机用户。终端在待机（IDLE态）状态下无线信号接收单元需要持续保持在开启状态以保证终端始终处于可寻呼状态，基于现有技术手机待机时间为几天，现有2/3/4G蜂窝网络无法满足窄带物联网终端的超低功耗需求。因此，针对窄带物联网网络，需要在节电技术上演进，满足超低功耗需求。 
节电关键技术
在网络传输层面的节电的主要手段包括：深度睡眠、减少不必要的信令消耗等。（定时关机会导致终端离线、无法灵活调整节电时间、上层应用可能会被同步关闭等缺陷，不推荐使用。） 
3GPP规范在R12、R13版本中陆续引入PSM、eDRX这两种节电技术，可将终端待机时间延长到5~10年。 
这两种技术是对深度睡眠及减少信令消耗两种节电手段的深入应用，包括： 
周期性深度睡眠：终端处于待机状态（ECM-IDLE态）时截取部分时间段进入节电状态，此时段内UE关闭无线接收单元，进入深度睡眠，从而达到省电目的。 
减少信令消耗：终端处于待机状态时需要通过周期性更新消息保持终端的在线状态，针对活跃度很低的物联网终端，可延长周期性时间，减少信令开销，达到省电目的。 
PSM节电技术
PSM节电技术的流程图如[图1]所示。
图1  PSM节电技术

在附着或TAU流程中UE和MME协商活跃定时器及周期性更新定时器时长，将UE进入IDLE态后时间分为两段：第一段为寻呼可达的活跃时间，第二段为剩余时间终端处于寻呼临时不可达的节电状态。
PSM节电技术具有如下特征： 
节电周期一般是以小时或天为单位。 
周期性更新时长越长，触发周期性TAU的频率越低，功耗越低。 
处于节电状态的时间越长，功耗越低，此时网络侧业务响应时间越长。 
eDRX节电技术
eDRX节电技术的流程图如[图2]所示。
图2  eDRX节电技术

在现有DRX技术上进行扩展，通过大幅扩展休眠周期（从秒级到分钟、数十分钟甚至小时）达到节电目的。
和PSM类似，在Attach/TAU流程中UE和MME协商eDRX Cycle和PTW时，UE进入IDLE态后的时间以eDRX Cycle为周期分割为若干时间段，在每一个eDRX Cycle周期内又分为两段：第一段为寻呼可达的PTW时长，第二段为剩余时间终端处于寻呼临时不可达的节电状态。
eDRX节电技术具有如下特征： 
节电周期一般是以分钟或数十分钟为单位。 
eDRX周期时长越长，处于节电状态的时间越长，功耗越低，此时网络侧业务响应时间越长。 
HLCom传输技术
通过PSM及eDRX两种节电技术可极大的延长终端待机时间，但也是有代价的：为保证节电，终端需要进入深度睡眠状态，此时终端会关闭无线收发单元，如果此时网络侧有下行数据投递给终端，会因为寻呼临时不可达而被丢弃。 
为避免下行数据因为寻呼临时不可达而被丢弃，需要通过额外的流程保证数据的可靠传输，为此，3GPP规范引入了HLCom功能。 
HLCom传输流程图如[图3]所示。
图3  HLCom传输技术
待机状态下，应用数据（网络命令）到达。 
MME监控终端状态，节电状态下通知SGW缓存。 
终端通过业务请求/TAU流程退出节电状态，并恢复用户面。 
承载恢复后，SGW向终端投递缓存报文，双向通信恢复。 
节电状态下收到下行数据报文，由于终端寻呼临时不可达，可通过HLCom技术，在节电状态下SGW与MME配合（MME管理终端状态，SGW缓存下行数据）完成下行数据缓存，并在UE可达后投递给UE，从而保证下行数据的可靠传输。
WUS节电技术
WUS技术是为能够防止接收器在持续检查信号过程中耗尽了电池，而采用了低功耗的过程，仅在检测到 WUS 时才唤醒设备，降低终端设备能耗。
图4  WUS节电技术

MME存储和向eNodeB传递WUS信息，具体如下： 
MME接收UE CAPABILITY INFO indication中UE无线寻呼信息中的WUS-Support指示，然后在寻呼消息中携带WUS-Support指示。 
MME在用户空闲态下寻呼时，将WUS-Support带给eNodeB，eNodeB通过WUS来指示寻呼，降低了盲检寻呼的复杂度，降低终端功耗。 
NB-IoT DRX节电技术
NB-IoT终端、基站支持NB-IoT UE Specific DRX参数，通过设置NB-IoT DRX来降低终端和功耗。 
终端可以在没有数据传输时，通过关闭UE的接收电路来降低功耗，提升电池使用时间。 
无线基站可以降低寻呼时延，从而降低终端功耗。 
NB DRX的时长在原来DRX基础上扩充了 512和1024， 分别对应5.12 S和10.24 S，可以更大程度的降低功耗。 
图5  NB-IoT DRX节电技术

NB-IoT DRX的基本机制是为处于RRC_CONNECTED态的UE配置一个DRX cycle。DRX cycle由以下两个组成： 
On Duration：在此时间内，UE侦听并接收PDCCH（激活期）。 
Opportunity for DRX：在此时间内，UE不接收下行信道的数据以节省功耗（休眠期）。 
应用场景 :##### 节电技术影响因素 
通信模式影响分析
NB-IoT物联网终端四大应用场景参见[表2]，通信模式比较规律，适用节电技术。其中，PSM适用节电周期较长（比如，应用通信频度按天、按小时）的应用，eDRX适用节电周期较短（比如，应用通信频度按半小时）的应用。
场景|应用举例|频度|对节电的要求
---|---|---|---
终端自动触发的异常报告|烟感告警、电量不足告警等|每几个月、每年等|无（无论是否节电状态，终端均可立即触发）
终端自动触发的周期性报告|智能抄表、智能环境监测、智能农业监测等|按天、按小时、按半小时等|根据频度不同，使用不同节电技术/参数
网络命令|功能开关、设备报告触发、请求测量等|按天、按小时、按半小时等|根据频度不同，使用不同节电技术/参数
软件升级/配置更新|软件补丁升级|半年|无
响应时延影响分析
在节电状态下网络侧主动发起的业务存在响应时延，该响应时延受网络侧协商的节电参数相关，该时长从数秒到数月不等。因此，节电状态下网络侧应用可容忍的响应时延也会影响节电技术的选择及参数设置。 
PSM一般节电周期较长，适用网络侧可容忍的响应时间较长的场景；eDRX节电周期较短，适用网络侧可容忍的响应时间较短的场景。 
响应时延流程如[图6]所示。
图6  响应时延流程

终端能力影响分析
终端选择节电技术有以下三种方式。 
只请求PSM、 
只请求eDRX。 
同时请求PSM及eDRX，网络侧是在终端请求的基础上进行协商。 
一般情况下由于终端不知道网络侧对节电技术支持能力，终端会同时请求PSM和eDRX，由网络侧根据应用场景进行选择合适的节电技术。 
网络应用感知影响分析
运营商可能无法感知所有物联网应用的通信模式，对于此类物联网应用，网络侧无法根据应用设置最合适的节电参数，但UE在请求使用节电功能时也会提供其建议的节电参数，此时网络侧可授权UE请求的节电参数。
##### NB-IoT节电特性应用场景 
基于节电技术影响因素分析，运营商可根据自身网络状况及业务发展需要，为不同用户，针对不同的物联网业务场景，提供灵活的节电策略。常见节电应用场景参见[表3]。
节电策略|应用场景
---|---
运营商感知应用|通信间隔|应用容忍的响应时延
---|---|---
PSM优先|是|超过2.9小时|无要求，或超过2.9小时
eDRX优先|是|低于2.9小时|低于2.9小时
PSM+eDRX|是|混合|混合
基于UE请求|否|N/A|N/A
##### 场景1，长通信间隔周期的节电策略：PSM优先 
场景描述
运营商能够获取此类物联网应用信息，通信间隔在2.9小时以上，对于节电状态下MT（网络侧触发）类应用时延响应要求也超过2.9小时或节电状态下不会触发网络命令。 
应用举例：水质监测，半天或一天周期上报一次水质信息。 
场景分析
该场景下，通信间隔较长，网络侧触发业务的响应时延宽松。节电周期可以设置长些，以保证最大程度的节电，PSM节电技术最适合本场景。在UE只请求eDRX节电技术时，网络侧无法准确设置节电参数，可以考虑以UE请求的为准。 
节电策略
根据场景分析，节电策略如下： 
基于APN识别此类业务。
启用PSM节电策略，周期性更新时长以本地配置优先并与通信间隔一致，活跃定时器时长推荐一次通信时长的2倍（用于重发）。
启用eDRX节电策略，eDRX Cycle周期以UE请求的优先。
当UE同时请求PSM及eDRX时，仅选择PSM。 
HLCom功能开启，以保证节电状态下的可靠传输。
##### 场景2，短通信间隔周期的节电策略：eDRX优先 
场景描述
运营商能够获取此类物联网应用信息，通信间隔在2.9小时以内，对于节电状态下MT（网络侧触发）类应用时延响应要求也超过2.9小时或节电状态下不会触发网络命令。 
应用举例：空气质量监测，小时或半小时周期上报一次空气质量信息。当空气质量较差时，检测中心可能会命令触发终端上报实时空气质量，响应时间要求在5分钟以内。 
场景分析
该场景下，通信间隔相对较短，网络侧触发业务的响应时延也有对应的要求。此时可考虑应用eDRX节电技术，在一个通信间隔周期内有多个eDRX周期，在保证节电的同时，缩短响应时延。在UE只请求PSM节电技术时，网络侧无法准确设置节电参数，可以考虑以UE请求的为准。 
节电策略
根据场景分析，节电策略如下： 
基于APN识别此类业务。 
启用eDRX节电策略，eDRX Cycle周期是通信间隔周期的一半或一半以内。 
启用PSM节电策略，活跃定时器时长及周期性TAU更新定时器时长以UE请求的优先。 
当UE同时请求PSM及eDRX时，仅选择eDRX。 
HLCom功能开启，以保证节电状态下的可靠传输。 
##### 场景3，混合通信间隔周期的节电策略：PSM+eDRX 
场景描述
运营商能够获取此类物联网应用信息，通信间隔由大小周期嵌套。 
应用举例：智能抄表，一个月采集一次，并集中在固定某一天分批分时间段（半小时）采集完成，每间隔半小时采集中心会通知采集失败用户重新尝试。 
场景分析
该场景下，适合同时使用PSM和eDRX，无通信要求的长周期时间段内，适用PSM；固定时段的短周期性存在通信时间段内适用eDRX。 
节电策略
根据场景分析，节电策略如下： 
基于APN识别此类业务。 
启用eDRX节电策略，eDRX Cycle周期是短通信间隔周期的一半或一半以内（保证有多个寻呼机会）。 
启用PSM节电策略，周期性TAU更新定时器时长与长通信周期间隔匹配；活跃定时器时长与短通信周期总时长匹配。 
当UE同时请求PSM及eDRX时，同时选择PSM和eDRX。 
HLCom功能开启，以保证节电状态下的可靠传输。 
##### 场景4，未知通信间隔周期的节电策略：UE请求优先 
场景描述
运营商无法获取此类物联网应用信息。 
应用举例：企业用户有多个物联网应用，并未申请不同种类应用使用不同APN，而是混合在运营商提供的一个缺省APN中使用。 
场景分析
该场景下尽量以UE请求的节电参数为准。 
节电策略
根据场景分析，节电策略如下： 
同时开启PSM及eDRX功能。 
PSM及eDRX节电参数策略UE优先。 
##### 场景5，UE与eNB支持WUS节电策略 
场景描述
NB-IoT用户、增强覆盖用户支持WUS时，eNB在小区配置时，可以使用WUS功能，减少寻呼监控相关的耗电量。
当在空闲模式下使用WUS时，适用以下选项： 
WUS用来指示UE应该监视MPDCCH或NPDCCH以在该小区中接收寻呼。 
对于没有配置扩展DRX的UE，WUS与一次寻呼机会（N＝1）相关联。 
对于配置了扩展DRX的UE，WUS可以关联到一个或多个寻呼时机（N≥PTW中的1)。 
如果UE检测到WUS，除非已经接收到寻呼消息，否则UE应监视后续寻呼时机（PO）。 
MME中的寻呼操作并不感知WUS在eNB中的使用。 
eNB处理WUS与寻呼时机（PO）之间的时序，UE可以期望在“配置的最大WUS时长”期间WUS重复发生，UE快速监测到WUS信号。 
场景分析
该场景下UE和eNB都要支持WUS功能，eNB在寻呼下发前先触发WUS信号，UE监测到后，开始监视寻呼消息，这样eNB在下发寻呼后，UE能够快速处理寻呼消息以及后续信令消息。 
节电策略
根据场景分析，WUS相比PO（paging occasion）序列短、终端监测时间短，从而有利于节电。终端只需检测有无WUS信号，从而决定是否读取PO和监测寻呼。 
##### 场景6，UE与eNB支持UE Specific DRX for NB-IOT节电策略 
场景描述
NB-IoT终端和无线基站通过支持UE Specific DRX可以降低寻呼时延，从而降低终端功耗。具体内容是：
无线基站进行广播时，携带是否支持UE Specific DRX的指示。 
在Attach和TAU流程中，终端和核心网协商确定UE Specific DRX for NB-IoT节电策略，MME将协商的结果携带给终端。 
MME在寻呼时，将UE Specific DRX for NB-IoT节电策略带给基站，基站用UE Specific DRX参数和小区的DRX参数比较取最小值，用于实际寻呼资源分配。终端同样用此策略计算接收寻呼的时机，从而降低寻呼时延，降低终端功耗。 
场景分析
R16支持了NB-IoT终端使用UE Specific DRX。适用于UE、无线基站、MME都支持UE Specific DRX for NB-IoT，UE与不同版本的MME之间的UE Specific DRX协商不生效的两个场景： 
当Pre-Rel-16MME接收到Rel-16UE发送的携带DRX参数IE的ATTACH REQUEST消息或者TAU REQUEST消息时，由于MME不能识别UE specific DRX for NB-IoT参数，网络不会使用收到的DRX参数进行寻呼。 
当Rel-16MME收到Pre-Rel-16UE发送的包含DRX参数IE的ATTACH REQUEST消息或TAU REQUEST消息时，MME不进行协商，MME寻呼不携带UE specific DRX for NB-IoT参数。 
节电策略
根据场景分析，使用UE Specific DRX for NB-IoT参数，终端可以在休眠期关闭接收电路降低功耗， 同时无线基站使用UE Specific DRX for NB-IoT参数进行寻呼，可以降低寻呼时延，从而降低终端功耗。 
客户收益 :受益方|受益描述
---|---
运营商|通过选择合理的寻呼策略，运营商能获得如下收益：节约投资成本：可在保证业务体验基础上降低负荷、节省网络资源。提升客户满意度：保障电池使用寿命，为客户节省投资并提升效率。
物联网终端客户|通过选择合理的寻呼策略，客户能获得如下收益：降低成本：降低设备采购成本及运维成本。享受定制的网络服务。
实现原理 :系统架构 :NB-IoT节电特性利用现有网元消息接口，新增节电参数字段达到终端节电目的，对系统架构无改变。
涉及的网元 :NB-IoT节电特性涉及PSM、eDRXHLCom、WUS、UE Specific DRX for NB-IoT子功能。
PSM节电功能需要MME、UE及HSS（可选）共同完成，各网元作用参见下表。表4  PSM节电功能的各网元作用网元名称网元作用MME在UE请求使用PSM时，为UE授权协商PSM节电参数，并监控UE节电状态。UE接受并使用MME下发的PSM节电参数。HSS签约周期性TAU更新时长，用于PSM周期性TAU更新参数协商时参考。 
eDRX节电功能需要MME、eNB和UE共同完成，各网元作用参见下表。表5  eDRX节电功能的各网元作用网元名称网元作用MME在UE请求使用eDRX时，为UE授权协商eDRX节电参数，并监控UE节电状态。在寻呼消息中将eDRX参数带给eNB，用于eNB计算寻呼时机。eNB寻呼时根据寻呼消息中的eDRX参数计算寻呼时机。UE接受并使用MME下发的eDRX节电参数。 
HLCom高时延功能需要SGW、MME和HSS（可选）共同完成，各网元作用参见下表。表6  HLCom高时延功能的各网元作用网元名称网元作用MME监控终端的节电状态，如果在节电状态下收到SGW的DDN请求通知SGW终端处于节电状态，需要缓存下行报文、缓存的最大时间及推荐缓存报文数。终端主动或寻呼触发退出节电状态并建立连接时，触发建立S1-U/S11-U用户面承载，用于SGW下发缓存下行报文。SGWSGW收到MME的DDN ACK消息中有缓存下行报文参数，触发下行报文缓存。SGW感知到用户面承载恢复后，将缓存的下行报文发送给终端。HSS签约建议缓存报文数，用于MME向SGW推荐最大缓存报文数协商时参考。 
WUS功能需要eNodeB、MME共同完成，各网元作用参见下表。表7  WUS功能的各网元作用网元名称网元作用MMEMME接收UE capability info indication中UE无线寻呼信息中的WUS-Support指示，然后在寻呼消息中携带WUS-Support指示。eNBeNodeB支持WUS信号的发送，通过WUS信号唤醒终端设备。 
UE Specific DRX for NB-IoT功能需要UE、NodeB、MME共同完成，各网元作用参见下表。表8  UE Specific DRX for NB-IoT功能的各网元作用网元名称网元作用UE附着以及发起TAU请求时，携带UE支持的UE Specific DRX for NB-IoT参数，同时接受并使用MME下发的UE Specific DRX for NB-IoT节电参数。终端使用此参数策略计算接收寻呼的时机。MME在UE发起请求使用UE Specific DRX for NB-IoT时，为UE授权协商UE Specific DRX for NB-IoT节电参数，并监控UE节电状态。eNBMME发起寻呼时，携带UE Specific DRX for NB-IoT，eNodeB支持使用UE Specific DRX和小区的DRX参数比较取最小值，用于实际寻呼资源分配。 
本网元实现 :MME提供了灵活的节电策略，支持从多维度区分不同应用场景配置节电策略，并提供丰富的操作维护工具进行节电状态观察。 
节电策略模板
节电特性涉及PSM、eDRX及HLCom，这三个功能互相存在关联，在使用时需要同时考虑，因此，在节电模板设置时进行了统一规划，包含四部分内容： 
公共部分：例如策略名称、PSM&eDRX互操作策略等。 
PSM独有策略参数。 
eDRX独有策略参数。 
HLCom独有策略参数。 
节电主要参数介绍参见下表。 
节电参数|作用域|功能描述
---|---|---
节电策略模板编号节电策略模板名称|公共|唯一识别节电策略模板。
UE同时请求PSM及eDRX时授权策略|公共|网络侧授权PSM及eDRX模式策略。
Active Time优先级|PSM|Active Time协商时优先级，包括：UE请求还是网络侧配置优先。
周期性更新时长优先级|PSM|周期性TAU时长协商优先级，包括：UE请求、MME本地配置还是HSS签约优先。
eDRX Cycle优先级|eDRX|eDRX Cycle协商时优先级，包括：UE请求还是网络侧配置优先。
PTW分配方式|eDRX|eDRX PTW协商时优先级，包括：UE请求优先、MME本地配置还是HSS签约优先。
SGW扩展缓存报文数推荐方式|HLCom|建议缓存报文数推荐策略，包括：不推荐、本地配置或HSS签约。
节电策略因子
运营商可以根据自身物联网业务状况，根据特定的因子配置自定义特定的节电策略。目前支持的策略因子包括：APN及IMSI号段。其中APN代表了某一类物联网业务场景，IMSI号段代表有特定节电需求的用户组/用户。运营商可以根据应用类型、用户类型或二者组合灵活选择/设置节电策略。
节电状态观察
网络中部署节电功能后，可根据需要监控节电功能的整体运行状态或某个特定设备的节电状态，MME提供了丰富的操作维护手段方便运维。 
包括： 
节电相关用户数统计。 
指定用户的节电相关签约参数、运行参数查看。 
业务流程 :PSM节电原理
PSM节电技术的流程如下图所示。 
图7  PSM节电技术

在附着或TAU流程中UE和MME协商活跃定时器及周期性更新定时器时长，将UE进入IDLE态后时间分为两段：第一段为寻呼可达的活跃时间，第二段为剩余时间终端处于寻呼临时不可达的节电状态。
eDRX节电原理
eDRX节电技术的流程图如下图所示。 
图8  eDRX节电技术

在现有DRX技术上进行扩展，通过大幅扩展休眠周期（从秒级到分钟、数十分钟甚至小时）达到节电目的。
和PSM类似，在Attach/TAU流程中UE和MME协商eDRX
Cycle和PTW时，UE进入IDLE态后的时间以eDRX Cycle为周期分割为若干时间段，在每一个eDRX Cycle周期内又分为两段：第一段为寻呼可达的PTW时长，第二段为剩余时间终端处于寻呼临时不可达的节电状态。
附着或TAU过程中的节电参数协商
节电参数协商流程如下图所示。 
图9  节电参数协商流程

流程说明： 
UE在Attach Request或者TAU Request消息中携带PSM及（或）eDRX参数，请求使用节电功能。 
如果签约了周期性TAU时长，在MME与HSS间位置更新或插入签约数据时，则会下发给MME。 
基于UE请求，MME获取节电策略，并结合UE请求参数、MME本地配置参数及HSS签约参数，协商出完整的节电参数并通过Attach
Accept或者TAU Accept消息下发给UE。 
UE激活MME下发的节电参数。 
节电状态下的高时延通信
高时延通信处理流程如下图所示。 
图10  节电状态下的高时延通信流程

流程说明： 
MME收到SGW的DDN消息，该UE处于节电状态。
MME为该UE启用高时延通信：MME获取高时延通信策略，结合MME本地配置参数及HSS签约参数，协商出高时延通信参数（最大缓存时间及可选的最大缓存报文数），并通过DDN
Ack消息通知给SGW。
 说明： 
对于PSM，MME分配的最大缓存时间超过当前时间到周期性更新定时器超时时间差；对于eDRX、MME分配的最大缓存时间超过当前时间到下一次寻呼时间窗达到时间。 
SGW收到DDN Ack消息，本地缓存下行报文，并启动最大缓存定时器。
对于PSM，UE通过周期性TAU触发UE退出节电状态，并通过TAU过程强制建立用户面承载；对于eDRX，MME在下一次寻呼时间窗达到时触发寻呼，并通过UE的业务请求流程建立用户面承载。
SGW检测到用户面承载恢复后立即下发缓存的下行数据包（一般是NC：Network Command）给UE，以此恢复双向数据传输。 
WUS节电原理
WUS处理流程如下图所示。 
图11  WUS处理流程

流程说明： 
如果UE由于“跨RAT TAU”或“UE无线能力更新”执行Attach过程或Tracking Area Update过程，MME向eNodeB发送Initial
Context Setup Request或UE Radio Capability Match Request消息时，则MME不携带任何UE无线能力信息。 
当eNB接收到从MME来的Initial Context Setup Request或UE Radio Capability
Match Request消息时，如果eNB还没有接收到从UE或MME来的UE的无线能力，则进行UE Capability Enquiry请求UE上传UE的无线能力信息。 
UE向eNB提供发送UE Capability Information的UE无线能力。 
eNB向MME返回Initial Context Setup Response或UE Radio Capability
Match Response消息。 
eNB在步骤2和步骤3中获取到UE请求无线能力后，则eNB通过UE Capability Info Indication消息将UE无线能力发送给MME，携带WUS-Support指示，MME存储UE无线能力，MME无需对内容解码，保存原始内容，以便后续进一步提供给eNB。 
当UE释放S1连接进入空闲态， 后续MME触发寻呼时，寻呼消息中携带UE寻呼无线能力信息，信息中包含WUS-Support指示。 
eNB收到寻呼消息后，触发WUS信号发送。UE检测到WUS信号后，启动在MPDCCH或NPDCCH上侦听寻呼消息。 
UE Specific DRX for NB-IoT节电处理流程
流程说明： 
UE发起附着/TAU请求，请求消息中携带DRX parameter in NB-S1 mode参数。 
MME在发送附着接受响应前进行NB DRX协商，根据UE携带的DRX parameter in NB-S1 mode参数和本地策略进行协商。 
MME在附着接受响应中将Negotiated DRX parameter in NB-S1 mode参数携带给UE，UE使用此参数控制设置DRX Cycle周期，进行节电控制。 
当UE释放S1连接进入空闲态， 后续MME触发寻呼时，寻呼消息中携带NB-IoT Paging DRX参数信息。 
MME向eNodeB下发寻呼消息。 
eNB收到寻呼消息后，使用NB-IoT Paging DRX和小区的DRX参数比较取最小值用于实际寻呼资源分配，终端采用同样的策略计算接收寻呼的时机。缩短寻呼时延，降低终端功耗。 
系统影响 :启用节电功能，对系统性能无影响。 
应用限制 :节电策略必须由UE触发PSM或eDRX由UE请求，MME授权协商；如果UE未请求，则MME不能为该UE授权节电功能。 
存在时延敏感应用的终端不能主动请求节电功能节电状态下终端寻呼临时不可达，需要在终端退出节电状态才能寻呼，导致MT业务高时延。对于存在时延敏感类应用（比如，语音）的终端不能主动请求使用节电功能，否则会导致应用延时严重，甚至失败，将严重影响业务体验。 
特性交互 :无。 
遵循标准 :协议|章节
---|---
3GPP TS23.682: " Architecture enhancements to facilitate communications withpacket data networks and applications "|4.5.4 UE Power Saving Mode4.5.7 High latency communication4.5.13 Extended idle mode DRX
3GPP TS23.401: "General Packet Radio Service (GPRS) enhancements for EvolvedUniversal Terrestrial Radio Access Network (E-UTRAN) access"|4.3.17.7 High latency communication4.3.22 UE Power Saving Mode5.3.2.1 E-UTRAN Initial Attach5.3.3.1 Tracking Area Update procedure with Serving GW change5.3.3.2 E-UTRAN Tracking Area Update without S GW Change5.3.4.1 UE triggered Service Request5.3.4.3 Network Triggered Service Request5.3.4B.3 Mobile Terminated Data Transport in Control PlaneCIoT EPS optimisation with P-GW connectivity5.3.5A Connection Resume procedure5.3.9.2 Insert Subscriber Data procedure5.4.1 Dedicated bearer activation5.4.2.1 PDN GW initiated bearer modification with bearer QoSupdate5.4.3 PDN GW initiated bearer modification without bearer QoSupdate5.7.2 MME5.10.2 UE requested PDN connectivity5.13a Extended Idle mode Discontinuous Reception (DRX)D.3.5 Routing Area UpdateD.3.6 Gn/Gp SGSN to MME Tracking Area Update
3GPP TS24.301: " Non-Access-Stratum (NAS) protocol for Evolved Packet System(EPS)"|5.3.11 Power saving mode5.3.12 Extended idle-mode DRX cycle5.3.13 Interaction between power saving mode and extended idlemode DRX cycle5.5.1.2.2 Attach procedure initiation5.5.3 Tracking area updating procedure (S1 mode only)
3GPP TS29.274: " Evolved General Packet Radio Service (GPRS) Tunnelling Protocolfor Control plane (GTPv2-C)"|7.3.6 ContextResponse
3GPP TS29.272: “Mobility Management Entity (MME) and Serving GPRS SupportNode (SGSN) related interfaces based on Diameter protocol”|5.2.1 Location Management Procedures5.2.2.1 Insert Subscriber Data5.2.2.2 Delete Subscriber Data
3GPP TS36.304:|7.3 Pagingin extended DRX
3GPP TS36.413: "Evolved Universal Terrestrial Access Network (E-UTRAN); S1Application Protocol (S1AP)"|8.5 Paging8.7.3 S1 Setup8.7.4 eNB Configuration Update
特性能力 :规格名称|规格指标
---|---
MME支持节电策略条目数（条）|4096
可获得性 :License要求 :该特性对应License文件中的包括： 
MME支持PSM节电功能 
MME支持eDRX节电功能 
MME支持物联网寻呼增强功能 
MME支持策略寻呼功能 
需要申请了License许可后，运营商才能获得该特性的服务。 
对其他网元的要求 :PSM由MME、UE、HSS配合完成。 
eDRX由MME、eNB、UE配合完成。 
HLCom由SGW、MME、HSS配合完成。 
工程规划要求 :节电策略可根据应用类型灵活设置，对工程规划无特殊要求。 
O&M相关 :命令 :新增命令配置项参见[表10]。
配置项|命令
---|---
物联网业务配置|SET MME IOT CFG
SHOW MME IOT CFG|物联网业务配置
节电策略模板配置|SET DEFAULT POWERSAVE POLICY
SHOW DEFAULT POWERSAVE POLICY|节电策略模板配置
ADD POWERSAVE POLICY|节电策略模板配置
SET POWERSAVE POLICY|节电策略模板配置
DEL POWERSAVE POLICY|节电策略模板配置
SHOW POWERSAVE POLICY|节电策略模板配置
节电策略因子配置|ADD POWERSAVE POLICY FACTOR
SET POWERSAVE POLICY FACTOR|节电策略因子配置
DEL POWERSAVE POLICY FACTOR|节电策略因子配置
SHOW POWERSAVE POLICY FACTOR|节电策略因子配置
移动号码分析|ADD MDNAL
SET MDNAL|移动号码分析
DEL MDNAL|移动号码分析
SHOW MDNAL|移动号码分析
SHOW MDN2REALM|移动号码分析
NB DRX策略配置|SET DEFAULT NBDRX POLICY
SHOW DEFAULT NBDRX POLICY|NB DRX策略配置
ADD NBDRX IMSISEG POLICY|NB DRX策略配置
SET NBDRX IMSISEG POLICY|NB DRX策略配置
DEL NBDRX IMSISEG POLICY|NB DRX策略配置
SHOW NBDRX IMSISEG POLICY|NB DRX策略配置
性能统计 :新增性能计数器参见[表11]。
性能计数器名称
---
C431000022 已激活PSM平均用户数
C431000023 已激活PSM最大用户数
C431000024 已激活eDRX平均用户数
C431000025 已激活eDRX最大用户数
C431000026 PSM节电状态平均用户数
C431000027 PSM节电状态最大用户数
C431000028 eDRX节电状态平均用户数
C431000029 eDRX节电状态最大用户数
C431000030 在SGW存有下行缓存的平均用户数
C431000031 在SGW存有下行缓存的最大用户数
特性配置 :特性配置 :配置说明 :MME提供了灵活的节电策略配置，运营商可以根据自身物联网业务状况，支持从多维度区分不同应用场景，根据APN及IMSI号段等策略因子自定义特定的节电策略。
配置前提 :MME license需要支持“MME支持PSM节电功能”、“MME支持eDRX节电功能”、“MME支持物联网寻呼增强功能”和“MME支持策略寻呼功能”。
配置过程 :MME仅使用默认节电策略时，配置过程如下：
通过[SET MME IOT CFG]命令，配置支持PSM、eDRX和HLCom功能。
通过[SET DEFAULT POWERSAVE POLICY]命令，配置缺省节电策略。
MME基于APN使用节电策略时，配置过程如下：
通过[SET MME IOT CFG]命令，配置支持PSM、eDRX和HLCom功能。
通过[ADD POWERSAVE POLICY]命令，配置节电策略模板。
通过[ADD POWERSAVE POLICY FACTOR]命令，配置节电策略因子。
MME基于IMSI使用节电策略时，配置过程如下：
通过[SET MME IOT CFG]命令，配置支持PSM、eDRX和HLCom功能。
通过[ADD POWERSAVE POLICY]命令，配置节电策略模板。
通过[ADD POWERSAVE POLICY FACTOR]命令，配置节电策略因子。
通过[ADD MDNAL]命令，配置IMSI号码分析。
MME仅使用默认NB DRX策略时，配置过程如下： 
通过[SET DEFAULT NBDRX POLICY]命令，配置支持NB DRX功能、缺省NB specific DRX策略配置。
MME基于号段的NB DRX策略时，配置过程如下： 
通过[SET DEFAULT NBDRX POLICY]命令，配置支持NB DRX功能、缺省NB specific DRX策略配置。
通过[ADD NBDRX IMSISEG POLICY]命令，配置基于号段的NB specific DRX策略配置。
配置实例 :##### 配置使用PSM节电策略 
运营商对于使用长通信间隔周期的物联网应用的终端，基于APN策略因子，配置使用PSM节电策略，活跃定时器时长和周期性TAU时长以本地配置的优先。如果终端同时请求了PSM和eDRX，则仅使用PSM策略。在UE非活跃时间，使用高时延通信功能，保证数据的可靠传输。
配置过程如下： 
步骤|命令|说明
---|---|---
1|SET MME IOT CFG:SUPPSM="YES",SUPHLCOM="YES"|打开PSM和HLCom功能。
2|ADD POWERSAVE POLICY:POLICYID=256,POLICYNAME="长通信间隔周期",AUTHPOLICY="PSM",PSMATPRIO="LOW"-"HIGH",PSMATVALUE=120,PSMT3412PRIO="LOW"-"HIGH"-"MEDIUM",PSMT3412=21600|对长通信间隔周期的应用，配置特定的节电策略模板。
3|ADD POWERSAVE POLICY FACTOR:FACTORAPN="apn1",POLICYID=256|配置基于APN策略因子获取节电策略。
##### 配置使用eDRX节电策略 
运营商对于使用短通信间隔周期的物联网应用的终端，基于APN策略因子，配置使用eDRX节电策略，eDRX
Cycle以本地配置的优先。如果终端同时请求了PSM和eDRX，则仅使用eDRX策略。在UE非活跃时间，使用高时延通信功能，保证数据的可靠传输。 
配置过程如下： 
步骤|命令|说明
---|---|---
1|SET MME IOT CFG:SUPEDRX="YES",SUPHLCOM="YES"|打开eDRX和HLCom功能。
2|ADD POWERSAVE POLICY:POLICYID=257,POLICYNAME="短通信间隔周期",AUTHPOLICY="EDRX",PSMATPRIO="LOW"-"HIGH",PSMATVALUE=120,PSMT3412PRIO="LOW"-"HIGH"-"MEDIUM",PSMT3412=21600|对短通信间隔周期的应用，配置特定的节电策略模板。
3|ADD POWERSAVE POLICY FACTOR:FACTORAPN="apn2",POLICYID=257|配置基于APN策略因子获取节电策略。
##### 配置使用NB DRX策略 
运营商对于小寻呼时延需求的终端，基于号段配置使用NB DRX策略，支持UE Specific DRX for NB-IOT协商和寻呼时携带此协商后的UE Specific DRX，无线基站在寻呼UE时可以降低时延。 
配置过程如下： 
步骤|命令|说明
---|---|---
1|SET DEFAULT NBDRX POLICY:NBDRXSWITCH="YES",NBDRXPERIOD="P32",NBDRXPOLICY="UE"|打开NB DRX功能，配置缺省NB-IoT UE Specific DRX周期值、缺省NB UE Specific DRX的协商策略。
2|ADD NBDRX IMSISEG POLICY:IMSI="46011",NBDRXPERIOD="P32",NBDRXPOLICY="UE"|配置基于号段的NB-IoT UE Specific DRX周期值、基于号段的NB UE Specific DRX的协商策略。
测试用例 :##### MME支持附着过程PSM参数协商 
测试项目|MME支持附着过程PSM参数协商
---|---
测试目的|测试MME支持附着过程PSM参数协商
预置条件|MME网元各项对接和业务配置完毕。用户取得MME支持PSM节电功能license授权，并更新了license。CIOT网络正常，CIoT终端可以正常接入该网络。CIOT网络支持PSM功能，已经正确配置了Active Timer值，设置UE请求的Active Time优先级高。CIoT终端支持PSM功能，支持在Attach Request消息中携带Active Timer。终端处于关机状态。
测试过程|终端开机。终端发送Attach Request (T3324 value)消息给MME。MME发送Attach Accept (T3324 value)消息给终端。
通过准则|Attach Request消息中携带T3324（Active Timer）定时器。Attach Accept消息中携带T3324（Active Timer）定时器，并且定时器的值和终端请求的T3324（ActiveTimer）值相同。
测试结果|–
##### 附着过程eDRX参数协商 
测试项目|附着过程eDRX参数协商
---|---
测试目的|测试MME支持附着过程eDRX参数协商
预置条件|MME网元各项对接和业务配置完毕。用户取得MME支持eDRX节电功能 授权，并更新了license。UE具备eDRX能力。MME支持eDRX，并配置了eDRX相关参数： eDRX Cycle优先级设置为本地配置优先级高，Paging TimeWindow length 为15.36 seconds；eDRX value为81.92seconds。
测试过程|UE发起4G附着。
通过准则|UE在 ATTACH REQUEST 中携带 Extended DRX parameters，其中 Paging TimeWindow为0， eDRX value为0100（61.44seconds）。MME在 ATTACH ACCEPT中携带确认后的 Extended DRX parameters，参数值 PagingTime Window为0101（15.36 seconds）， eDRX value为0101（81.92 seconds）。
测试结果|–
##### MME支持节电状态下的高时延通信 
测试项目|MME支持节电状态下的高时延通信
---|---
测试目的|测试eDRX处于非PTW时的下行数据缓存可以正常处理
预置条件|MME网元各项对接和业务配置完毕。用户取得MME支持eDRX节电功能 授权，并更新了license。UE具备eDRX能力。SGW支持eDRX。MME支持eDRX，并配置了eDRX相关参数： eDRX Cycle优先级设置为本地配置优先级高，Paging TimeWindow length 为15.36 seconds；eDRX value为81.92seconds。
测试过程|UE发起4G附着流程。eNodeB发起S1释放。UE处于非Paging Time Windows状态下，UE有下行数据报文。一段时间后，在非PTW时间内，UE主动发起Service Request流程。MME发送Modify Bearer Request消息给SGW。MME收到SGW返回的Modify Bearer Response消息。SGW发送缓存的下行数据给UE。
通过准则|SGW向MME发送 Downlink Data Notification消息。MME返回 Downlink Data Notification Acknowledge，携带DL BufferingDuration指示SGW缓存报文，在指示的时间内不再下发DDN。SGW缓存收到的下行数据，不发送Downlink Data Notification消息给MME。ServiceRequest流程结束后，SGW缓存的下行数据发送给UE。
测试结果|–
##### MME支持NB UE Specific DRX 
测试项目|NBIOT寻呼时，消息中携带MME协商后的NB-IoT Paging DRX字段
---|---
测试目的|测试MME支持NB用户寻呼时能携带协商后的NB-IoT Paging DRX字段。
预置条件|MME网元各项对接和业务配置完毕。MME支持NB功能。“支持NB UE specific DRX协商”功能开关打开。UE具备NB UE Specific DRX能力。MME支持NB UE Specific DRX，并配置了相关参数： NB-IOT UE Specific DRX周期、NB-IOT UE Specific DRX协商策略。
测试过程|UE发起4G附着流程。eNodeB发起S1释放。SGW发送下行数据报文给UE。
通过准则|Attach Accept消息中携带协商后的DRX parameter in NB-S1 mode IE。SGW向MME发送 Downlink Data Notification消息。MME给eNODEB发送PAGING消息，携带协商后的NB-IoT Paging DRX IE。MME返回 Downlink Data Notification Acknowledge。
测试结果|–
##### MME支持从UDM获取签约的PTW参数 
测试项目|MME支持从UDM获取签约的PTW参数。
测试目的|测试MME支持从UDM获取签约的PTW参数，并且签约的PTW优先级最高。
预置条件|MME网元各项对接和业务配置完毕。MME支持NB功能。MME支持用户签约PTW，签约PTW优先级为高、本地PTW优先级为中、UE请求优先级为低。
测试过程|UE发起附着，携带PTW参数，HSS签约PTW。
通过准则|Attach Accept消息中下发PTW参数，值为签约PTW。
测试结果|–
常见问题处理 :无。 
# ZUF-78-17-007 低移动性 
特性描述 :特性描述 :术语 :术语|含义
---|---
低移动性|移动性是指设备的物理位置发生改变的频度。物联网设备种类繁多，从设备的移动性角度进行分类，可以分为三类：低移动性的设备、一般移动性的设备和高移动性设备。比如各种定点探测设备、家庭电器设备等可归为低移动性设备。
描述 :定义 :MME支持对低移动性的物联网设备进行接入优化的功能。 
低移动性接入优化是指为了减少海量接入的物联网设备对网络的信令负荷能力造成冲击，通过采用缩小设备的寻呼范围、减少对设备移动性管理操作等措施，提高移动网络的接入能力。 
MME可以为低移动性的物联网设备制定不同TA List分配策略、寻呼策略、周期性TAU时长以及移动性限制策略，为网络资源的合理利用、终端节电和海量接入提供支撑。
背景知识 :NB-IoT设备的类型
NB-IoT设备的类型参见[表1]。
类型|应用举例|数据量|数据上报周期
---|---|---|---
自主异常报告业务类型|烟雾报警探测器、智能电表停电的通知等。|上行数据数据量极小（数十字节量级）|多以年、月为单位
自主周期报告业务类型|智能公用事业（煤气/水/电）测量报告、智能农业、智能环境等。|上行数据量较小（数百字节量级）|多以天、小时为单位
网络指令业务类型|设备（开启/关闭）时发送上行报告、请求抄表等。|下行数据量极小（数十字节量级）|多以天、小时为单位
软件更新业务类型|软件补丁/更新等。|上行/下行数据量较大（数千字节量级）|多以半年为单位
从[表1]中可以看出NB-IoT设备基本上是低移动性的设备。
NB-IoT的移动性管理
NB-IoT的终端个数是海量接入，在使用同一基站接入的情况下，NB-IoT可以比现有的无线接入技术提供更多的接入个数，接入个数可以达到现有接入个数的50~100倍，一个扇区能够支持5万个连接。 
在海量接入的情况下，如果MME使用和人网一样的移动性管理功能，系统会频繁地进行周期性握手，大范围寻呼等操作，对网络资源消耗很大，需要大量的网络设备，导致运营成本升高。同时NB-IoT终端也会因为移动性管理功能的复杂而增加成本。 
应用场景 :##### 通讯间隔长 
场景描述
自主异常报告业务类型的NB-IoT设备，如烟雾报警探测器、智能电表停电的通知等，对于上行数据数据量的需求极小（一般为数十字节量级），数据上报周期多以年、月为单位。 
场景分析
对于这类数据上报周期较长的NB-IoT设备，如果周期性TAU的时长比较短，则周期性TAU信令所占信令比例就非常高，会浪费无线侧和核心网侧的网络资源，也会增加终端的耗电量，所以要降低周期性TAU信令的占比。 
解决方法
考虑到不同周期性间隔的NB-IoT设备对周期性TAU的时长要求不同，有以下两种方式。 
通过在HSS的签约数据中设置终端的周期性TAU时长，MME将NB-IoT终端设备在HSS中签约的TAU时长下发给终端。 
MME也可以通过在本地根据终端设备的号码段配置不同的周期性TAU时长。 
##### 终端处于休眠态时，网络侧下发指令寻呼设备 
场景描述
网络指令业务类型的NB-IoT设备，如设备（开启/关闭）时发送上行报告，此类设备的下行数据量需求极小（一般为数十字节量级），周期多以天、小时为单位。当需要开启/关闭设备时，MME需要寻呼设备，触发设备进入连接态，以下达指令。 
场景分析
此类终端物理位置通常不会移动，且基本处于通讯休眠状态，网络侧下发指令时需要寻呼终端，通常情况下的寻呼范围一般是TA或TA
List，寻呼范围比较大，如果使用普通的寻呼策略对这类终端进行寻呼，则对无线网络资源浪费较大，且实际情况中通常会同时对同一类设备触发操作，瞬时寻呼量会非常大，所以需要考虑寻呼范围的合理性，以提升网络的接入能力。 
解决方法
缩小寻呼范围，缩小寻呼范围的策略如[图1]所示。
图1  精准寻呼

优化NB-IoT用户的TA List分配策略。TA List中只分配当前的TA，这样即使是按照TA Lsit寻呼，寻呼范围也比较小。 
单独配置NB-IoT用户的寻呼策略。设置一个比较小的寻呼范围。 
对NB-IoT用户只寻呼终端在最后信令中携带的eNodeB和CELL范围。MME发送给eNodeB的寻呼消息中携带小区信息。 
客户收益 :收益者|收益描述
---|---
运营商|节约成本：相同的投入成本下，系统可以容纳更多的终端接入。
终端用户|入网门槛低：简化移动性处理可以降低NB-IoT芯片复杂度，从而降低芯片成本。减少电量消耗，使终端电池使用时间更长。
实现原理 :系统架构 :3GPP定义的NB-IoT网络架构如下图所示。 
图2  NB-IoT网络架构

该架构是对EPS网络架构的优化，其特点是：简单、轻量化，去除了不必要的网络功能（例如：不支持动态PCC等），虽然从架构上C-SGN将原有的MME、SGW、PGW的功能进行了简化和整合，但实际上除了SGi口外，其他主要接口都是MME的接口，所以C-SGN的主要优化也是在MME实现，其优化主要体现在数据传输方面。
涉及的网元 :低移动性设备接入优化功能需要NB-IoT终端、MME、eNodeB和HSS共同完成，各网元作用参见下表。 
网元名称|网元作用
---|---
MME|支持接受HSS下发的周期性TAU时长，并下发给UE。支持根据IMSI本地控制周期性TAU时长。支持NB-IoT设备的TA List分配功能。支持NB-IoT设备的寻呼优化，包括接受UE的历史eNodeB和小区信息，并在寻呼消息中带给eNodeB。支持小区等位置信息上报
eNodeB|支持小区寻呼和小区位置上报。
NB-IoT终端|支持扩展周期性TAU时长，支持记录历史小区和eNodeB信息并在信令中带给MME。
HSS|支持周期性TAU时长的签约。
本网元实现 :MME保存并下发UE签约的周期性TAU时长，并可以根据本地策略进行控制；MME对NB-IoT终端采用不同的TAList分配策略，对NB-IoT终端采用不同的寻呼策略控制。 
业务流程 :Attach/TAU过程中的周期性TAU时长控制和TA
List分配流程
周期性TAU时长控制和TAList分配流程如下图所示。 
图3  业务流程

UE在发送给MME的Attach Request或者TAU Request消息中携带支持扩展TAU时长。 
（可选）如果NB-IoT终端在HSS上签约了周期性TAU时长，在位置更新或插入签约数据时，则HSS会将周期性TAU时长在Update
Location Answer消息中下发给MME。 
MME结合UE请求参数、本地配置数据及HSS下发的签约参数，确定周期性TAU时长参数；MME根据本地配置的NB-IoT的TA
List分配策略进行TA List分配，并通过Attach Accept或者TAU Accept消息下发给UE。 
寻呼策略选择流程
寻呼策略选择流程如下图所示。 
图4  寻呼策略选择流程

UE在RRC（Radio Resource Control）释放消息中将记录的历史eNodeB和CELL信息发送给eNodeB。 
eNodeB在UE CONTEXT RELEASE COMPLETE消息中将这些数据发送给MME，MME保存以供后续寻呼NB-IoT设备时使用。 
MME收到下行数据通知，发现UE处于IDLE状态，需要寻呼UE，MME判断UE为NB-IoT设备，则根据IMSI号码获得NB-IoT设备的寻呼策略，在之前记录的历史eNodeB和CELL范围时进行寻呼。 
eNodeB收到MME下发的寻呼请求消息，在推荐的小区范围内进行寻呼。 
系统影响 :启用低移动性设备接入优化功能可以提高系统的性能。 
应用限制 :该特性不涉及应用限制。 
特性交互 :本功能的周期性TAU时长控制部分与节电功能有交互，当终端指定启用节电功能时，则按照节电特性的原则来分配周期性TAU时长。 
遵循标准 :标准类别|标准名称|章节
---|---|---
3GPP|3GPP TS 22.368 Service requirements for Machine-Type Communications(MTC)|7.2.1 Low Mobility
3GPP TS 22.891 Feasibility Study on New Services and MarketsTechnology Enablers|3GPP|5.4.2 Low mobility devices
3GPP TS 23.401|3GPP|4.3.17 Support for Machine Type Communications (MTC)
3GPP TS 23.720|3GPP|5.4 Key Issue 4 - Support of efficient Paging area managementfor Cellular IoT
3GPP TS 23.888|3GPP|5.6 Key Issue - Low Mobility
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :需要申请以下License许可后，运营商才能获得该特性的服务。 
7102 MME支持低移动性功能 
7094 MME支持物联网寻呼增强功能 
对其他网元的要求 :UE|MME|eNodeB|SGW|HSS|SCEF
---|---|---|---|---|---
-|√|√|√|√|-
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表3  新增配置项配置项命令低移动性识别及控制策略SET LOWMOBILITY POLICY周期性TAU优化策略SET IMSI PERIODICTAU POLICYMME全局寻呼策略配置SET MME GLOBAL NBIOT PAGING POLICYMME寻呼策略配置SET MME NBIOT PAGING POLICYMME寻呼策略因子配置SET MME PAGING POLICY FACTOR物联网业务配置SET MME IOT CFG 
安全变量该特性不涉及安全变量的变化。 
定时器该特性不涉及定时器的变化。 
软参该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警和通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :根据NB-IoT终端低移动性的特点，配置更长的周期性TAU时长，可以节省无线网络和核心网络资源，节省终端寿命。 
终端通讯休眠态时网络侧下发寻呼消息，通过配置缩小寻呼范围，减小寻呼量，可以节省无线网络资源，减小对网络的冲击，提升网络的接入能力。 
配置前提 :确认相关的license已经开启。 
7102 MME支持低移动性功能 
7094 MME支持物联网寻呼增强功能 
配置过程 :##### 使用终端签约的TAU时长的配置过程 
通过[SET LOWMOBILITY
POLICY]命令，将参数默认周期性TAU时长控制策略设置为HSS签约（HSS）。
终端的签约周期性TAU时长要大于2秒。 
##### 根据号段配置不同的周期性TAU时长的配置过程 
通过[SET MME IOT CFG]命令，将参数低移动性识别开关设置为识别（YES）。
通过[ADD IMSI PERIODICTAU POLICY]命令中，配置IMSI号段的周期性TAU时长策略优先级和本地周期性TAU时长。
##### 缩小寻呼范围的配置过程 
通过[SET MME GLOBAL NBIOT
PAGING POLICY]命令，配置NB-IoT寻呼策略。
配置实例 :##### 实例1 
场景说明
通讯间隔长：根据HSS签约配置周期性TAU时长。 
配置步骤
根据规划，进行如下配置： 
说明|操作
---|---
通过命令SET LOWMOBILITY POLICY将参数默认周期性TAU时长控制策略设置为HSS签约（HSS）。|SET LOWMOBILITY POLICY:DEFAULTT3412PRIO="HSS";
##### 实例2 
场景说明
通讯间隔长：根据IMSI号段配置周期性TAU时长。 
配置步骤
假设配置的号段为46011，进行如下配置： 
说明|操作
---|---
通过SET MME IOT CFG命令，将参数低移动性识别开关设置为识别（YES）。通过命令ADD IMSI PERIODICTAU POLICY配置IMSI号段的周期性TAU时长策略优先级和本地周期性TAU时长。|SET MME IOT CFG:SUPLOWMOBILITY="YES";ADD IMSI PERIODICTAU POLICY: IMSI="46011",T3412PRIO="LOCAL",LOWMOBILITYT3412=5000;
##### 实例3 
场景说明
终端通讯休眠态时网络侧下发寻呼消息，缩小寻呼范围。 
配置步骤
根据规划，进行如下配置： 
说明|操作
---|---
通过SET MME GLOBAL NBIOT PAGING POLICY命令，将参数携带寻呼推荐小区信息设置为携带。|SET MME GLOBAL NBIOT PAGING POLICY:PAGECELL="YES";


测试用例 :



测试项目|MME根据签约的周期性TAU时长 配置周期性TAU时长
---|---
测试目的|测试MME支持根据签约信息配置周期性TAU时长
预置条件|MME打开7102 MME支持低移动性功能。HSS签约周期性TAU时长。配置全局周期性TAU时长。终端发起的附着流程不支持PSM。MME配置 默认周期性TAU时长控制策略为HSS签约。
测试过程|终端发起附着流程，Attach Request消息中携带支持扩展周期性TAU。
通过准则|AttachAccept消息中携带周期性TAU时长与签约的周期性TAU时长相同。




# ZUF-78-17-008 深度覆盖 
特性描述 :特性描述 :术语 :无 
描述 :定义 :ZXUN uMAC-MME支持深度覆盖特性，通过对深度覆盖场景下的NB-IoT终端进行寻呼优化，保证系统使用尽可能少的资源尽快寻呼到NB-IoT终端，从而提升无线资源利用效率。
NB-IoT终端由于自身特点需面对复杂环境下信号覆盖差异的问题，ZXUN uMAC-MME结合NB-IoT无线系统通过深度覆盖功能，可以保证地下车库、地下室、地下管道等信号难以到达的地方能够被信号覆盖。
背景知识 :现有寻呼技术在NB-IoT中面临的挑战
不同于人类聚居于城市、乡镇等相似的环境下，物联网应用形式多种多样，并且其终端所处环境的信号覆盖强弱也千差万别。典型的信号覆盖弱的物联网应用场景如下： 
寻呼是移动网络中网络侧触发联系终端的主要手段，对于人网（2/3/4G网络）而言，由于人类所处位置的相似性，可根据地理位置（比如与基站的远近）采用相似的信号强度进行寻呼。但对于物联网，相同区域不同位置下信号覆盖是千变万化的，如果仍采用人网类似的寻呼策略，对于深度覆盖下的物联网终端，极容易寻呼失败，影响业务开展。 
因此，NB-IoT无线系统在设计时提升了功率频谱密度，NB-IoT比LTE提升20dB增益，即覆盖能力提升100倍，很好实现广域覆盖，就算在地下车库、地下室、地下管道等信号难以到达的地方也能覆盖到。 
但深度覆盖（覆盖增强）是以增大无线发射功率为代价的，同一个区域内信号较好的位置上（比如地面）的NB-IoT终端并不需要覆盖增强，信号较差的位置上的NB-IoT终端可使用不同的覆盖增强级别。如果相同区域内针对所有NB-IoT终端采用相同的覆盖增强策略，对无线资源是极大的浪费，增大的运营商对于无线设备的CAPEX（Capital
Expenditure，资本性支出）投入。因此，需要找到一种方法，既要保证深度覆盖，也要降低无线的CAPEX。 
深度覆盖场景下的寻呼优化技术
考虑到深度覆盖场景下NB-IoT终端具备低移动或静止不动的特征，寻呼时可精准控制寻呼范围到小区级别，这样可在整个系统范围内节约无线资源。 
考虑到深度覆盖场景下NB-IoT终端位置的不同，其覆盖增强级别有差异，可针对不同终端采用不同的覆盖增强策略，这样可以保证每个终端都是采用最优的方式使用无线资源，从而降低整体的无线资源消耗。 
应用场景 :深覆盖特性主要适用于对地下车库、地下室、地下管道等信号难以到达之处的NB-IoT终端进行无线信号覆盖增强。典型应用场景有： 
智能停车中的地磁感应  
部署在地下管道内的水/电/气表  
分布在人烟稀少地带的环境监测设备  
分布在城市道路/小区中智能井盖  
客户收益 :受益方|受益描述
---|---
运营商|通过深度覆盖增强，运营商能获得如下收益：节约投资成本：扩大基站覆盖范围，减少投资及运维成本。提升客户满意度：通过覆盖增强实现广域覆盖，就算在地下车库、地下室、地下管道等信号难以到达的地方也能覆盖到。
物联网终端用户|降低成本：客户只需要部署支持覆盖增强的物联网终端就可接入网络，避免在高投资区域（比如，地下室、隧道灯）额外部署网络。享受定制的网络服务。
实现原理 :##### 系统构架 
深度覆盖特性利用现有网元消息接口，通过新增覆盖增强级别参数来完成深度覆盖下的寻呼优化，对系统架构无改变。
涉及的网元 :深度覆盖特性需要MME、eNB和UE共同完成。 
网元名称|网元作用
---|---
CIoT UE|物联网终端，用NAS PDU发送和接收小包数据IP Data、Non-IP Data或短消息，并携带S1释放辅助信息。
E-UTRAN|支持NB-IoT终端接入，传递NAS PDU。通过S1-U面传输小包数据IP Data。
MME|存储NB-IoT终端最近使用的覆盖增强级别。寻呼时携带覆盖增强。
eNodeB|基于覆盖增强级别实施寻呼。
UE|向网络侧提供当前使用的覆盖增强级别。
协议栈 :无 
本网元实现 :描述
MME负责保存eNodeB在S1释放消息中携带的覆盖增强级别CE
Level及历史位置信息，寻呼时基于这些信息进行寻呼优化。 
根据深度覆盖场景下NB-IoT终端的普遍特征（低移动性）及特定NB-IoT终端的特定位置特征（信号强弱），可从这两个维度进行寻呼优化。 
编号|名称|寻呼优化策略
---|---|---
1|低移动性终端的寻呼优化|基于小区的寻呼优化
2|不同信号覆盖下的寻呼优化|基于覆盖增强级别的寻呼优化
基于小区的寻呼优化
深度覆盖场景下NB-IoT终端可能用于抄表、环境监测等物联网应用，此类终端一般具备静止不动或低移动性特征。 
该场景下，由于NB-IoT终端基本不移动，如果仍沿用基于TA列表、TA、甚至eNB范围内的寻呼，存在寻呼资源的极大浪费。可以在现有的基于eNodeB精准寻呼基础上进一步缩小寻呼范围，实施基于小区的优化寻呼，从而降低无线的寻呼资源消耗。 
组网示意图如下图所示。 
图1  基于小区的寻呼优化

根据eNodeB上报信息，MME负责保存NB-IoT终端历史小区信息，并在寻呼过程中通过寻呼消息携带给eNodeB，以保证系统使用尽可能少的资源尽快寻呼到终端。 
基于覆盖增强级别的寻呼优化
深度覆盖场景下NB-IoT终端可能部署在楼宇、地下车库、地下室内或地下管道，其所处环境复杂，需要信号覆盖增强，但不同终端的覆盖增强级别要求不同。 
该场景下可对不同终端的覆盖增强级别CE Level进行针对性的寻呼优化，提高寻呼成功率的同时，保证了寻呼资源高效利用。 
 说明： 
CE Level（Coverage Enhancement Level，覆盖增强级别），从0到2，CE Level共三个等级，分别对应可对抗144dB、154dB、164dB的信号衰减。基站与NB-IoT终端之间会根据其所在的CE
Level来选择相对应的信息重发次数。 
组网示意图如下图所示。 
图2  基于覆盖增强的寻呼优化

MME负责保存UE最近一次接入时使用的覆盖增强级别CE Level，并应用在寻呼过程中，尽快寻呼到终端。虽然UE在IDLE态有可能改变其覆盖增强级别，但是上一次使用的覆盖增强级别有助于尽快找到当前的级别。 
同时，在寻呼无响应时，MME会尝试重发同时尝试调整寻呼范围，无线侧可据此调整覆盖增强级别CE Level，尽快寻呼到终端。 
业务流程 :基于小区的寻呼优化
基于小区的寻呼优化流程如下图所示。 
图3  基于小区的寻呼优化的流程

流程描述如下： 
UE在RRC释放消息中将记录的历史eNodeB信息和小区信息带给给eNodeB，eNodeB在UE CONTEXT RELEASE
COMPLETE中带给MME，MME将信息保存下来，以供后续寻呼使用。 
MME收到DDN（Downlink Data Notify，下行数据通知）或者其他信令消息时，发现UE处于IDLE态，需要寻呼UE。如果当前的寻呼策略是eNodeB范围内寻呼，而之前又有保存UE推荐的寻呼eNodeB和小区，则在UE推荐范围内寻呼。 
MME进行寻呼策略的选择。 
eNodeB收到寻呼请求，在推荐的小区范围内进行寻呼。 
基于覆盖增强的寻呼优化
基于覆盖增强的寻呼优化的流程图如下图所示。 
图4  基于覆盖增强的寻呼优化流程

流程描述如下： 
MME发送UE Context Release Command消息给eNodeB。 
eNodeB发送UE Context Release Complete或者UE Context Suspend Request消息（消息中携带小区列表和对应的覆盖增强级别CE
Level）给MME。MME保存覆盖增强级别信息。 
MME发起寻呼。MME在寻呼消息中携带覆盖增强级别信息CE Level和寻呼尝试信息给eNodeB。 
eNodeB以寻呼消息中的覆盖增强级别CE Level为基准，结合寻呼尝试信息微调（比如，根据当前寻呼尝试次数，按5dB->10dB->15db增大覆盖增强级别），以尽快寻呼到终端。 
系统影响 :启用深度覆盖功能，对系统性能无影响。 
应用限制 :无 
特性交互 :无 
遵循标准 :协议|章节
---|---
3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|4.3.27.1 Paging for Enhanced Coverage5.3.4.3 NetworkTriggered Service Request5.3.4A Connection Suspend procedure5.3.4B.3 Mobile Terminated Data Transport in Control Plane CIoTEPS optimisation with P-GW connectivity5.3.5 S1 release procedure
3GPP TS 36.300: "Evolved Universal Terrestrial Radio Access(E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN);Overall description; Stage 2"|23.7b Support of UEs in Enhanced Coverage23.13.2Paging optimisation for UEs in enhanced coverage
3GPP TS 36.413: " Evolved Universal Terrestrial Radio AccessNetwork(E-UTRAN); S1 Application Protocol (S1AP)"|8.5 Paging9.2.1.103 Assistance Data for Paging9.2.1.108 Assistance Data for CE capable Ues9.2.1.109 CellIdentifier and Coverage Enhancement Level9.2.1.110 Paging AttemptInformation
特性能力 :无 
可获得性 :版本要求及变更记录 :无 
##### LICENSE要求 
需要申请了“MME支持物联网寻呼增强功能”和“MME支持策略寻呼功能”的License许可后，运营商才能获得该特性的服务。
对其他网元的要求 :无 
工程规划要求 :无 
O&M相关 :命令 :配置项
新增配置项参见[表1]。
配置项|命令
---|---
MME全局寻呼策略配置|SET MME GLOBAL NBIOT PAGING POLICY
MME寻呼策略配置|ADD MME NBIOT PAGING POLICY
MME寻呼策略因子配置|ADD MME PAGING POLICY FACTOR
安全变量
无 
定时器
无 
软件参数
无 
动态管理
无 
性能统计 :该特性暂不涉及性能统计。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置深度覆盖功能（包括基于小区的寻呼优化和基于覆盖增强的寻呼优化），能够对深度覆盖场景下的NB-IoT终端进行寻呼优化，保证系统使用尽可能少的资源尽快寻呼到NB-IoT终端。 
配置前提 :已打开“MME支持物联网寻呼增强”功能License。
配置过程 :##### 使用基于小区的寻呼优化功能的配置过程 
使用命令[ADD MME NBIOT PAGING POLICY]，增加NB-IoT业务寻呼策略，携带寻呼推荐小区信息设置为携带。
使用命令[ADD MME PAGING POLICY FACTOR]，配置MME寻呼策略因子，寻呼策略类型设置为NB-IoT类型，策略编号为步骤1中设置的寻呼策略编号。
使用命令[ADD MDNAL]，配置IMSI号码分析，分析器入口设置为IMSI寻呼策略分析，号码分析结果索引为步骤2中设置的IMSI/MSISDN号段索引。
##### 使用覆盖增强的寻呼优化功能的配置过程 
使用命令[ADD MME NBIOT PAGING POLICY]，增加NB-IoT业务寻呼策略，其中：携带寻呼推荐小区信息设置为携带，携带寻呼覆盖增强级别设置为携带。
使用命令[ADD MME PAGING POLICY FACTOR]，配置MME寻呼策略因子，寻呼策略类型设置为NB-IoT，策略编号为步骤1中设置的寻呼策略编号。
使用命令[ADD MDNAL]，配置IMSI号码分析，分析器入口设置为IMSI寻呼策略分析，号码分析结果索引为步骤2中设置的IMSI/MSISDN号段索引。
配置实例 :##### 实例场景1–配置MME支持基于小区的寻呼优化 
涉及的配置信息参见下表。 
参数|取值|备注
---|---|---
寻呼策略编号|51|寻呼策略类型为NB-IoT
最近一次活动eNB寻呼次数|3|-
IMSI/MSISDN号段索引|1|即号码分析结果索引
被分析号码|4600201|-
配置命令如下： 
[ADD MME NBIOT PAGING POLICY]:ID=51,HISTORYENB=3,PAGECELL="YES";
[ADD MME PAGING POLICY FACTOR]:USERNUMIDX=1,PGPOLICY="NBIOT"-51;
[ADD MDNAL]:DGT="4600201",ENTR="DAS_IMSI_PGPOLICY",RST=1;
##### 实例场景2–配置MME支持基于覆盖增强的寻呼优化 
涉及的配置信息参见下表。 
参数|取值|备注
---|---|---
寻呼策略编号|52|寻呼策略类型为NB-IoT
最近一次活动eNB寻呼次数|3|-
IMSI/MSISDN号段索引|2|即号码分析结果索引
被分析号码|4600202|-
[ADD MME NBIOT PAGING POLICY]:ID=52,HISTORYENB=3,PAGECELL="YES",PAGECELEVEL="YES";
[ADD MME PAGING POLICY FACTOR]:USERNUMIDX=2,PGPOLICY="NBIOT"-52;
[ADD MDNAL]:DGT="4600202",ENTR="DAS_IMSI_PGPOLICY",RST=2;
测试用例 :测试项目|基于小区的寻呼优化
---|---
测试功能|测试MME支持基于小区的寻呼优化
预备条件|MME支持物联网寻呼增强功能License打开。MME配置NB-IoT业务寻呼策略，寻呼策略为eNodeB列表寻呼次数设置为2，打开“携带寻呼推荐小区信息”功能开关。MME配置寻呼策略因子，寻呼策略设置为NBIoT类型，并与上述寻呼策略相关联。MME配置IMSI号码分析，分析器入口为IMSI寻呼策略，与上面配置的寻呼策略因子相关联。
测试步骤|NB-IoT用户CP模式附着。基站释放S1链接。UE context release complete中携带eNB列表和小区列表。SGW发起DDN流程，触发MME发送寻呼消息。
预期结果|MME对所有eNB列表中的eNB进行寻呼，寻呼消息中携带小区列表字段与基站带上来的一致，并携带寻呼尝试信息。重发的寻呼消息携带的小区列表也和基站发送的UE context release complete消息中携带的一致。
项目名称|基于覆盖增强的寻呼优化
---|---
测试功能|测试MME支持基于覆盖增强的寻呼优化
预备条件|MME支持物联网寻呼增强功能License打开。MME配置NB-IoT业务寻呼策略，寻呼策略为eNB列表寻呼和TA列表寻呼，寻呼次数分别为2次和3次，打开“携带寻呼推荐小区信息”和“携带寻呼覆盖增强级别”功能开关。MME配置寻呼策略因子，寻呼策略设置为NBIoT类型，并与上述寻呼策略相关联。MME配置IMSI号码分析，分析器入口为IMSI寻呼策略，与上面配置的寻呼策略因子相关联。
测试步骤|NB-IoT用户CP模式附着。基站释放S1链接。UE context release complete中携带eNB列表、TA列表和小区列表，并含有寻呼cellid1的增强等级20dB。SGW发起DDN流程，触发MME发送寻呼消息。
预期结果|第1次寻呼带上cellid1和寻呼等级20dB，Paging Attempt Count为1，Intended Numberof Paging Attempts为5，Next Paging Area Scope字段为same。第2次寻呼带上cellid1和寻呼等级20dB，Paging Attempt Count为2，Intended Numberof Paging Attempts为5，Next Paging Area Scope字段为change。第3次寻呼带上cellid1和寻呼等级20dB，Paging Attempt Count为3，Intended Numberof Paging Attempts为5，Next Paging Area Scope字段为same。第4次寻呼带上cellid1和寻呼等级20dB，Paging Attempt Count为4，Intended Numberof Paging Attempts为5，Next Paging Area Scope字段为same。第5次寻呼带上cellid1和寻呼等级20dB，Paging Attempt Count为5，Intended Numberof Paging Attempts为5，且无Next Paging Area Scope字段。
常见问题处理 :无 
# ZUF-78-17-009 Non-IP EPS连接 
特性描述 :特性描述 :描述 :定义 :Non-IP数据是物联网特有的，特定的终端和应用可能采用例如6LowPAN、MQTT-SN等非IP的协议栈。对于Non-IP数据，MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输小包数据；也可以采用轻量化的架构，使得数据传输路径更短，MME可以和SCEF、GW之间建立控制面通道传输Non-IP小包数据。
背景知识 :对于大多数NB-IoT应用，发送的数据报告频率低、字节小，一般报告在20-200个字节之间，这样UDP/IP传输层协议栈的占用字节（IPv4：28字节；IPv6：48字节）占的数据报文比例很高，尤其是在有效负荷小于20字节的情况下，报文头甚至超过了数据，所以在这种情况下UE传输Non-IP数据可以大幅提升无线网络数据传输效率。
Non-IP数据传输有两种实现方式： 
通过SCEF传递Non-IP数据，无需建立用户面承载，属于Non-IP专属解决方案。需新建SCEF网元节点，并且MME需要开通并支持T6a接口。 
通过SGi进行UDP/IP封装，以隧道方式支持Non-IP小数据包传递。使用PGW功能传输IP及Non-IP数据，适用于IoT
UE与某个单独的AS之间协商并进行隧道加密的通信场景。网络侧需要给每个IoT UE都分配1个IP地址，MME/eNB需要支持提示UE禁用IP头压缩功能。当UE想要采用Non-IP的PDN连接来发送小数据包时，发送"Non-IP"标识给网络侧。 
 说明： 
本特导描述的是通过SGi隧道进行NON-IP的数据传输，不包括基于SCEF的Non-IP的数据传输。 
应用场景 :结合上文提到的non-IP的优势，non-IP可以实现以下内容： 
适用于低速率/低复杂度终端进行低复杂度、非频发的小包数据的传输场景。 
non-IP类数据传输到PGW后，PGW通过专用隧道发往物联网平台。 
通过SGi口接口传输non-IP数据可以使C-SGN统一数据出口， 便于未来面向NB-IoT类业务进行计费点选择和计费模式设计使用。 
客户收益 :受益方|受益描述
---|---
运营商|使用控制面传输小包数据，MME不新增用户面进程，架构简单，部署方便。通过SGi口接口传输non-IP数据可以使C-SGN统一数据出口，便于未来面向NB-IoT类业务进行计费点选择和计费模式设计使用。
物联网终端用户|不建立数据的无线承载，降低消耗。
实现原理 :系统架构 :支持NB-IoT的优化后的EPS网络架构如下图所示。 
图1  支持NB-IoT的优化后的EPS网络架构图

在SGi口进行Non-IP数据传输时，C-SGN和AS之间通过直传隧道进行数据传输，网络示意图如下图所示。 
图2  C-SGN和AS之间通过直传隧道进行数据传输

涉及的网元 :网元名称|网元作用
---|---
NB-IoT UE|物联网终端，用NAS PDU发送和接收小包数据（IP Data或Non-IP Data），并携 带S1释放辅助信息。
E-UTRAN|支持NB-IoT终端接入，传递NAS PDU。通过S1-MME接口传输小包数据。
MME|传输上行和下行小包数据。完成S1-MME到S11-U面小包数据的转换传输。
SAE-GW|通过S11-U面传输小包数据。
协议栈 :采用控制面优化方案时各网元的协议栈，其中Non-IP采用的是经由SGi隧道传输，如下图所示。 
图3  协议栈

该协议栈的特点： 
S1口进行简化，不支持承载和上下文相关流程，主要支持NAS传递即可。 
IP和非IP数据在UE和MME间，采用NAS传递。 
与PGW的接口不变，MME和SGW之间采用GTP-U传递用户面包文。 
本网元实现 :MME主要实现： 
附着过程中建立PDN类型为Non-IP的SGi传输。 
UE发起Non-IP小包数据传输。 
MME收到下行的小包数据，将小包数据投递给UE。  
业务流程 :附着流程
图4  附着流程

UE执行附着时，就指示当前是NB-IoT接入，同时指明当前是使用的CP（控制面优化）模式。 
MME执行鉴权和安全流程；随后用户数据的安全保障，就利用现有的安全保障机制。 
MME执行位置更新，获取签约数据。 
用户签约Non-IP数据，UE请求的APN的PDN类型为Non-IP，且签约的传输方式为SGi，则MME向GW发起创建会话请求，创建S11-U用户面。 
GW返回创建会话响应，携带S11-U地址；当前是Non-IP数据，不给UE分配IP地址。 
UE返回附着完成消息。 
局间能力协商
当UE发起局间TAU时，新的MME收到TAU后，会发起能力协商过程，在局间Context
Request消息中携带NB-IoT的RAT类型，以及新局支持NB-IoT的特性，包括： 
是否支持无PDN附着。 
是否支持SGi口传递Non-IP数据。 
是否支持SCEF传递Non-IP数据。 
老局MME收到局间上下文请求Context Request消息后进行协商判断： 
老局无承载，如果新局支持无PDN附着，则可以继续TAU流程；否则拒绝上下文请求，返回“Request Rejected”。 
老局只有Non-IP承载（区分SGi/SCEF），新局支持Non-IP（区分SGi/SCEF），则可以继续TAU流程；否则否则拒绝上下文请求，返回“Request
Rejected”。 
如果老局有多个承载，则根据新局的NB-IoT支持情况，返回新局支持的EPS承载上下文；如果新局不支持Non-IP，则老局不发送Non-IP相关的承载上下文。  
MO流程
图5  MO流程

UE发起的RRC连接建立消息中，携带有NAS PDU；NAS PDU中携带有EBI，用来标识同时携带的加密的上行数据。 
UE携带的释放辅助信息，可以帮助MME及时完成S1释放： 
如果携带释放信息，同时指示无需后继数据，则MME可以在上行数据传输后立即释放S1连接。 
如果携带释放信息，同时指示需要后继数据，则MME可以在收到下行数据后完成下行数据传输后立即释放S1连接。 
如果不携带释放信息，则MME不立即释放S1连接，处理UE和GW间的数据传输；直到收到释放信息，或者是eNB的S1释放为止。 
空闲态的场景，UE发起Control Plane Service Request，数据包携带在该消息的ESM Data
Transport消息中。 
MME进行完整性检查和消息解密，如果S11-U尚未建立，则MME发送修改承载请求，重建S11-U。 
S11-U建立完成，MME控制面进程在支持GTP-C协议栈的基础上，也同时支持GTP-U协议栈，MME通过S11-U接口，将上行数据报文封装在GTP-U消息中，发送给SGW。 
PGW通过SGi口采用隧道方式将Non-IP小数据包传递AS服务器。 
MT流程
图6  MT流程

SGW收到下行数据报文，但发现没有S11-U承载，则缓存报文。 
SGW发送DDN消息给MME，消息中携带有EBI和ARP。 
当UE已注册且可达，MME发送寻呼消息给eNB。 
UE收到寻呼消息后，发起控制面业务（Control Plane Service Request）请求流程。 
eNB发送Initial UE消息给MME。 
如果S11-U尚未建立，则MME发送修改承载请求，重建S11-U。 
S11U建立成功后，MME根据SGW返回的S11-U地址和GTP-U的端口进行报文收发；转到控制面进程处理。 
MME从GTP-U消息中得到下行数据报文后，封装通用下行NAS投递消息中，对消息进行加密和完保。 
MME通过ESM Data Transport消息将数据包投递给UE。 
UE的上行数据报文通过ESM Data Transport消息发给MME。 
MME进行完整性检查和消息解密，并MME将上行数据报文通过S11-U发送给SGW；并根据消息中的释放辅助信息决策是否需要立即释放S1连接。 
如果MME根据释放指示的决策没有释放S1连接，且一定时间内没有NAS消息投递，则eNB发起S1释放。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.720（Study on architecture enhancements for CellularInternet of Things）|6 Solutions
3GPP TS 23.401 （General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access）|4.10 Introduction of CIoT EPS Optimisations
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :需要申请了“NB-IoT注册用户数”和“NB-IoT在线用户数”的License许可后，运营商才能获得NB-IoT用户接入核心网的服务。 
需要申请了“MME支持物联网小包数据控制面传输优化”的License许可后，运营商才能获得物联网小包数据控制面传输优化特性的服务。 
对其他网元的要求 :UE|eNodeB（E-UTRAN）|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无。 
O&M相关 :命令 :命令|新增参数
---|---
SET MME IOT CFG|新增参数：支持Non-IP数据SGi口传输
ADD SUPFEATURE|新增参数：Non-IP PDN Type APNs
SET COMBOCFG|新增参数：MME缺省Non-IP APN
性能统计 :测量类型|计数器
---|---
基于APN的承载激活流程测量|C463000098 Non-IP PDN连接请求次数
C463000099 Non-IP PDN连接成功次数|基于APN的承载激活流程测量
特性配置 :特性配置 :配置说明 :MME支持Non-IP功能，UE可以建立到PGW的Non-IP类型的PDN连接，通过SGi口传输Non-IP的小包数据。 
配置前提 :对于Non-IP功能，需要： 
MME支持用户CP 模式接入 
MME支持Non-IP功能 
HSS支持Non-IP功能 
License支持Non-IP 
配置过程 :MME支持用户CP 模式接入。 
Non-IP功能开关打开。 
Support Feature支持Non-IP。 
配置实例 :##### 实例场景 
用户CP模式接入，MME支持Non-IP，终端请求建立Non-IP类型的PDN连接成功。 
MME和HSS对接时候的规划如下： 
Feature ID|Diameter局向|Diameter局向路由
---|---|---
1|1|1
配置步骤 :步骤|说明|操作
---|---|---
1|MME配置支持用户CP模式接入，Non-IP功能开关打开。|SET MME IOT CFG:CPSW="YES",SGNIPDNSW="YES";
2|SupportFeature支持Non-IP。|ADD SUPFEATURE:FEATUREID=1,SUPFEATURE2="NIPAPN";ADD DIAMADJ:ADJID=1,ADJROUTEID=1,SUPFEATUREID=1;ADD DIAMADJROUTE:ADJROUTEID=1,ROUTEGROUP=201-1-100,REALM="zte.com.cn",SUPFEATUREID=1;
测试用例 :测试项目|附着时请求APN类型为Non-IP
---|---
测试目的|附着时请求APN类型为Non-IP
预置条件|UE NB CP模式接入。license“MME支持Non-IP数据SGi口传输”设置为支持。MME物联网功能配置中“支持Non-IP数据SGi口传输”设置为支持。HSS局向关联的support feature支持NON-IP。签约默认NON-IP APN。签约Context ID的PDN类型为Non-IP签约addi Context ID的PDN类型为Non-IP。
测试过程|UE发起附着，请求PDN类型为Non-IP，未携带请求的APN。
通过准则|使用MME默认APN解析PGW。发送Create Session Request消息中携带PDN类型为Non-IP。MME发送激活默认承载请求给UE，携带PDN类型为Non-IP。附着成功。
测试结果|–
# ZUF-78-17-010 头压缩 
特性描述 :特性描述 :描述 :定义 :头压缩（Header Compression）是为了减少无线与核心网之间的流量的一种技术。经过头压缩后传输的报头字节数远远小于完整的报头，当要频繁地传输比较小的数据包，开启头压缩功能可以提高数据的传输效率。 
报文头压缩技术可以将报文头进行压缩，使得所需要传输的报文头字节数远远小于完整的报文头。在同一个报文中，相邻两个包之间有很多相同的域，这些相同的域可以不必每次都传输，不同域的变化也是有一定的规律，根据这些规律可以将其编码后进行发送，这样可以对报文头进行压缩，减少报文头的开销，从而减少无线与核心网之间的流量。 
背景知识 :在移动网络中的无线接入侧，最宝贵的是资源是无线资源，希望在有限的无线资源上，承载的业务越多越好。比如一个数据包的格式为：IP+UDP+RTP+Payload。如下图所示： 
图1  IP+UDP+RTP+Payload报文格式

如果采用的是IPv4，则报文头包括20个字节IPv4,8个字节UDP，12字节的RTP，共40个字节；如果采用IPv6，则40个字节的IPv6，12字节的RTP，共60个字节。通常情况下，Payload的有效长度为15~20个字节，因此采用IPv4，有66.7%~72.7%的无线资源浪费在报文头上；采用IPv6，有75%~80%的无线资源浪费在报文头上。 
IETF的规范中，主要的报文头压缩主要有四种：VJHC、IPHC、CRTP和ROHC。其中VJHC、IPHC以及CRTP在差错率高、延迟大的无线中均不能很好地工作，而ROHC可以解决这些问题，同时ROHC可以用于压缩RTP/UDP/IP、UDP/IP、ESP/IP报文，能够在无线中很好地工作，具有很强的健壮行和较高的压缩效率。
ROHC报文头域分类 
ROHC将报文头主要分类为静态域和动态域，更细致的可以划分为5类，具体见下表。 
分类|含义|RTP域|UDP域|IP域
---|---|---|---|---
可推导域|可以从其他域值推导得到的域，不需要做任何处理。|无|传送总长度字段信息。|传送总长度字段信息、首部检验和字段信息。
静态域|在整个生命周期都保持不变的域，一般会被传输一次。|传送P、X字段信息。|无|传送版本字段信息、标志字段信息。
静态已知域|该域的值为已知，不会被传输。|传送版本字段信息。|无|传送首部长度、保留位等字段信息。
静态定义域|用于定于一个流的域。|传送SSRC字段信息。|传送源和目的端口号字段信息。|传送源和目的IP地址字段信息。
变化域|其值在包与包之间会变化。|传送CC、M、载荷类型、SN、TS字段信息。|传送校验和字段信息。|传送TOS、IPID、TTL字段信息。
ROHC工作状态 
ROHC报文头压缩的压缩端和解压端在初始化时各自生成一个上下文。两者都有三种状态，初始化状态为最低状态，满足响应的条件后，转换为较高级的状态，当定时器超时或者上下文不同步时，便从高级状态转换为低级状态。工作在高级状态时，压缩效率是最高的。 
压缩端工作状态 
ROHC压缩端有三种状态：IR（Initialization and Refresh）、FO（First Order）和SO（Second Order）。三种状态的转换关系如下图所示。 
图2  ROHC压缩端有三种状态

影响状态之间转换的因素主要有以下几点：
原始报文头域的改变。在一个报文中，原始报文头中有些域突然出现了较大的变化，这会引起压缩段状态的下降，以同步压缩端和解压端的上下文。 
从解压端传送过来的正反馈信息（ACK），会引起压缩端状态的上升； 
从解压端传送过来的负反馈信息（NACK），会引起压缩端状态的下降； 
周期性的转变。 
解压端工作状态 
ROHC解压端有三种状态：NC（No Context）、SC（Static Context）和FC（Full Context）。三种状态的转换关系如下图所示。 
图3  ROHC解压端有三种状态

解压端开始，工作在NC状态，只要一旦进入到FC状态就很少回退到低状态。在NC状态下，只要成功解压一个包后，解压端就直接进入FC状态。在FC状态下，只有连续多次无法正确解压压缩包时，才会回退到SC状态，并且在SC状态下，一旦正确解压一个压缩包，就立即回到FC状态。在SC状态下，只有多次无法解压压缩端通过FC状态下发送过来的报文，才回退到NC状态。 
ROHC工作模式 
ROHC报文头压缩有三种工作模式：U模式（unidirectional，单向）、O模式（Bidirectional Optimistic，双向优化）和R模式（Bidirectional Reliable，双向可靠）。 
U模式 
U模式下，压缩端向解压端发送压缩包，而解压端不能向压缩端传输任何信息。当周期性的超时发生或者压缩报文的头域出现不规律变化时，压缩端的状态之间会进行转换。 
图4  U模式

U模式下解压端工作在NC状态，如果成功解压一个IR包，便会从NC状态转移到FC状态。 
在FC状态，如果发生多次解压失败，解压端会从FC状态转移到低级的状态，并且只能转移到SC状态。 
在SC状态，解压端成功解压更新包后，会再次回到FC状态，但是，如果解压端对多个更新包解压失败，便会转向NC状态。 
在NC状态，解压端仅接收IR类型的报文，其他类型的报文会被丢弃；在SC状态，仅接收IR类型、IR-DYN类型和UOR-2类型的报文；在FC状态下，任何类型的报文都可以接收。 
O模式 
O模式下存在反馈信道，解压端可以向压缩端发送错误请求（NACK和STATIC-NACK）、ACK（可以不发送），同时O模式下压缩端不使用定时器的机制。压缩端的状态转换如下图所示。 
图5  O模式

O模式下状态转换的解压端和U模式的解压端机制一致。但O模式下存在三种类型的反馈：ACK、NACK、STATIC-NACK，解压端在不同的状态下产生不同的反馈。ACK作为可选的反馈，如果解压端发送过一次ACK，后继都必须发送ACK。 
R模式 
R模式中反馈信道使用的次数更多，压缩端上下文和解压端上下文失步的概率远远小于U模式和O模式，其健壮性更强。压缩端由低级向高级状态的转换只有在接收到解压端发送的ACK后才转换，当需要进行更新或者收到NACK、STATIC-NACK反馈时，高级状态向低级状态转移。状态的转换见下图所示。 
图6  R模式

R模式的解压端只有携带7BIT或者8BIT的CRC报文（更新报文）时才能对上下文进行更新，而且只有在这种报文解压成功才会发ACK。 
在NC状态，若收到非IR报文时，发送STATIC-NACK反馈，如果IR报文CRC检验失败，则不发送反馈，等待新的IR报文；在SC状态，当CRC检验失败时，发送STATIC-NACK反馈；在FC状态，在CRC检验失败时，发送NACK反馈。 
应用场景 :物联网终端通过CP模式接入MME网络后，通过MME传输数据。MME和无线之间通过头压缩的方式，以节约无线的带宽。 
客户收益 :受益方|受益描述
---|---
运营商|增加无线的传输能力，在有限的带宽上传递更多的数据。提高用户的满意度。
终端|提高传输能力。
实现原理 :系统架构 :在ROHC中，压缩端和解压端之间会建立参考信息，存储中上下文中，双方各自维护一个上下文。两者的上下文在整个压缩过程中保持同步，压缩端定时向解压端发送更新包或者由解压端通知压缩端向解压端发送更新信息。 
压缩端和解压端通过CID（context identifier，上下文标识）来标识不同的上下文，而且压缩端和解压端的CID必须保持一致，当有多个上下文的时候，则需要多个CID。压缩端和解压端实现原理如下图所示。 
图7  压缩端和解压端实现原理图

当一个报文到来时，压缩端首先进入压缩初始化状态，将报文的分组报文头信息保存在压缩端相应的上下文中，同时将完整的报文头信息发给解压端。解压端在收到此报文头后，解压出原始报文头，并将报文头信息保存到解压端相应的上下文中。当压缩端确信解压端收到了所有的上下文信息后，便进入压缩状态，开始发送压缩报文。 
涉及的网元 :网元名称|网元作用
---|---
MME|MME的头压缩主要包括两个方面：压缩算法的协商。在附着、TAU、业务请求、PDN连接、激活承载、修改承载等业务流程中完成无线与MME之间的压缩算法的协商。数据压缩和解压缩。MME在DOWNLINK中完成数据的压缩，在UPLINK中完成数据的解压缩。
UE|协商头压缩的算法，根据算法对数据进行压缩和解压缩。
协议栈 :由于在报文传送过程中，仅需要链路层报文头就可以正确传送，像IP、UDP和RTP等在链路中不起作用。因此ROHC在TCP/IP协议栈中应该位于链路层和网络层之间。以RTP/UDP/IP报文为例，如下图所示： 
图8  协议栈

同时ROHC的框架是可以扩展的，不但可以压缩RTP/UDP/IP报文头，而且可以压缩UDP/IP，IP报文头。ROHC用一个域来标示该压缩包对应的原始包的类型，并称该域为profile。如果原始报文头的类型是RTP/UDP/IP，则对应的ROHC压缩称之为RTP profile；如果是UDP/IP，则为UDP profile；如果是IP，则为IP profile。 
业务流程 : 说明： 
本节只介绍头压缩相关的协商流程部分，所有流程均为EPC的标准流程，此处不对每条流程进行详细介绍。 
附着
附着流程如下图所示。 
图9  附着流程图

头压缩流程相关说明： 
在第1和第2步中，UE/eNB在附着请求中携带头压缩的相关信息给MME，信息为Header Compression Configuration。头压缩的信息包含在PDN连接的信息中，MME保留Header Compression Configuration。 
在第16步，MME根据自身支持的头压缩信息和UE/eNB带来的头压缩信息进行比较，协商出是否支持以及支持哪些Profile，在附着接受中把协商的结果带给UE/eNB。 
TAU流程
TAU流程如下图所示。 
图10  TAU流程

头压缩流程相关说明： 
第4步，如果新MME支持头压缩，在向老MME发送Context Request的时候带上支持头压缩的标识。 
第5步，老MME判断新MME支持头压缩，则把和UE协商的头压缩信息通过Context Response带给新的MME。 
第19步，新MME在TAU Accept消息中带上头压缩的信息。 
业务请求
业务请求流程如下图所示。 
图11  业务请求流程

头压缩流程相关说明： 
MME在第4步的时候，需要删除S11-U的相关信息，包括ROHC的上下文，但不包括Header Compression Configuration。 
PDN连接
UE请求PDN连接的流程如下图所示。 
图12  UE请求PDN连接

头压缩流程相关说明： 
第1步，UE/eNB在PDN请求中携带头压缩的相关信息给MME，信息为Header Compression Configuration。MME保留Header Compression Configuration。 
第7步，MME根据自身支持的头压缩信息和UE/eNB带来的头压缩信息进行比较，协商出是否支持，以及支持哪些Profile，在PDN接受中把协商的结果带给UE/eNB。 
切换过程
切换过程如下图所示。 
图13  切换流程

头压缩流程相关说明： 
第3步，源MME在向目标MME发送Forward Relocation Request的时候带上协商好的头压缩的信息。 
第25步，目标MME判断源MME带了头压缩信息，则保存下来，在TAU Accept消息中带上头压缩的信息。 
系统影响 :开通该特性需要占用一定的内存，占用的内存和支持的用户数相关。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401|General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access
3GPP TS 24.301|Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS)
3GPP TS 36.413:|S1 Application Protocol (S1AP)
IETF RFC 4995|The RObust Header Compression (ROHC) Framework
IETF RFC 4996|RObust Header Compression (ROHC): A Profile for TCP/IP (ROHC-TCP)
IETF RFC 3095|RObust Header Compression (RoHC): Framework and four profiles: RTP, UDP, ESP and uncompressed
IETF RFC 3843|RObust Header Compression (RoHC): A Compression Profile for IP
IETF RFC 4815:|RObust Header Compression (ROHC): Corrections and Clarifications to RFC 3095
IETF RFC 5225|RObust Header Compression (ROHC) Version 2: Profiles for RTP, UDP, IP, ESP and UDP Lite
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持物联网小包数据控制面传输优化”（license ID：7089），此项目显示为“支持”，表示ZXUN uMAC支持物联网小包数据控制面传输优化。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
有关|有关|无关|无关|无关
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :首先要了解到使用头压缩的用户数，用于配置头压缩的容量数据。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令MME头压缩配置SET MME HC FUNCIONSHOW MME HC FUNCIONSET MME HC ATTRIBUTESHOW MME HC ATTRIBUTE表2  修改配置项配置项命令新增参数容量配置SET CAPACITY新增配置参数RoHC上下文比例(%)，用于配置RoHC协商的上下文与承载上下文的比例。 
安全变量该特性不涉及安全变量的变化。 
软件参数表3  新增软件参数软件参数ID软件参数名称262574是否支持ROHC反馈机制 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过对头压缩的配置，实现头压缩的功能。 
配置前提 :已开启MME支持MME支持物联网小包数据控制面传输优化的license功能。 
MME配置已支持CP模式，开启CP模式命令为SET MME IOT CFG:CPSW="YES" 
配置过程 :头压缩功能配置过程如下： 
通过[SET MME HC FUNCION]命令，设置是否开启头压缩功能。
通过[SET MME HC ATTRIBUTE]命令，配置头压缩属性。
通过[SET CAPACITY]命令，支持头压缩的容量配置，配置的是RoHC协商的上下文与承载上下文的比例。
配置实例 :场景说明 :开启头压缩功能，配置maxid为100，支持的profile（UDP/IP、ESP/IP、IP、TCP/IP），配置容量比例为50%。 
配置步骤 :说明|操作
---|---
打开MME支持头压缩功能|SET MME HC FUNCION:HCFUNCTION="YES"
配置头压缩属性|SET MME HC ATTRIBUTE:HCMAXCID=100,HCPROFILE="UDP/IP"&"ESP/IP"&"IP"&"TCP/IP";
配置头压缩用户容量|SET CAPACITY:ROHCCAPIRATE=50;
调整特性 :无 
测试用例 :测试项目|MME支持IP头压缩功能
---|---
测试目的|MME能够对CP模式下的数据包中IP协议头部进行压缩与解压缩。
预置条件|终端支持头压缩功能，其中profile支持IP协议。MME配置支持CP模式。MME配置支持头压缩功能，其中支持的profile包括IP协议。
测试过程|终端发起CP附着，成功附着在网络上。上行ping 20个数据包。下行ping 20个数据包。
通过准则|经过终端压缩的20个数据包，MME能够正常解压缩，经过解压缩的数据包应该跟终端发的原始包码流一样，并把解压缩后的数据包发给SGW。对于下行的20个数据包，MME能够正确压缩，并发给终端。经过压缩数据IP头比正常的头要短。
测试结果|–
常见问题处理 :故障现象 :头压缩解压缩失败。 
##### 处理方法 
检查终端是否打开了头压缩功能。 
使用[SHOW MME HC FUNCION]命令，查看MME是否都打开了头压缩功能。如果不正确，使用[SET MME HC FUNCION]命令进行修改。
使用[SHOW MME HC ATTRIBUTE]命令，检查profile配置是否正确。如果不正确，使用[SET MME HC ATTRIBUTE]命令进行修改。
# ZUF-78-17-011 速率控制 
特性描述 :特性描述 :描述 :定义 :服务的PLMN的速率控制用于控制UE所有承载的上行报文速率及PGW/SCEF对UE的下行报文速率。
APN的速率控制用于控制UE的某APN下承载的上行报文速率及PGW/SCEF对UE的下行报文速率。
背景知识 :服务的PLMN的速率控制
MME对服务的PLMN的速率控制处理如下： 
MME为某用户分配报文上行与下行速率上限（所有承载），在业务流程中将报文速率值传递给UE与PGW或SCEF。 
UE在发送上行报文时，需控制不超过上行速率门限。 
PGW/SCEF在发送下行报文时，需控制不超过下行速率门限。 
由于UE的行为不可控，MME需要对用户需进行上行速率限制，如用户超过门限，将进行速率控制，报文丢弃。 
按照中国联通测试要求，MME对下行速率也可以进行限制。由内部变量控制，默认MME不对下行速率进行限制。 
服务的PLMN的速率控制仅作用于CP模式。 
APN的速率控制
APN的速率控制l是由PGW或SCEF进行控制： 
PGW或SCEF分配APN Rate Control的控制策略，并通过MME转发给UE，UE保存APN Rate Control的策略。 
UE在APN的承载中发送上行报文时，需控制报文数不超过APN的上行速率门限。 
由于UE的行为不可控，PGW/SCEF执行速率UE的上行报文的速率控制，超过部分的报文丢弃。 
MME处理的内容是透传APN
Rate Control字段。APN的速率控制信息包含在现有的PCO参数，MME将PCO字段透传给UE。 
APN的速率控制作用于CP模式和UP模式。 
应用场景 :NB-IoT物联网实现了控制面EPS优化功能，MME和UE间通过控制面通道使用NAS消息传输小包数据，MME和SAE-GW间通过S11-U用户面通道传输小包数据。这样就极易造成网络拥塞，为避免由于UE和AS服务器频繁发送报文对网络的冲击，终端和网络侧实现基于服务的PLMN的速率控制和APN的速率控制。
客户收益 :受益方|受益描述
---|---
运营商|实现控制面EPS优化功能后，MME和SAE-GW间通过S11-U用户面通道传输小包数据，支持速率控制，可以避免网络侧的拥塞。
物联网终端用户|有效的控制报文的发送，避免由于报文频繁对网络的冲击，从而降低消耗。
实现原理 :系统架构 :支持NB-IoT的优化后的EPS网络架构如下图所示。 
图1  系统架构图

涉及的网元 :网元名称|网元作用
---|---
NB-IoT UE|物联网终端，用NAS PDU发送和接收小包数据（IP Data或Non-IP Data），并携 带S1释放辅助信息。
E-UTRAN|支持NB-IoT终端接入，传递NAS PDU。通过S1-MME接口传输小包数据。
MME|传输上行和下行小包数据。完成S1-MME到S11-U面小包数据的转换传输。
SAE-GW|通过S11-U面传输小包数据。
协议栈 :采用控制面优化方案时各网元的协议栈如下图所示，其中Non-IP采用的是经由SGi隧道传输： 
图2  协议栈

本网元实现 :协议中定义每NB-IOT在6分钟时间内，上行与下行报文数量最少支持10个，最大上限为不限制。 
速率配置为0为不控制，该功能只有License，没有对应的软参，外场配置为0相当于关闭该功能。 
MME对服务的PLMN的速率控制实现内容如下： 
MME配置“全局用户报文速率”和“用户报文速率配置”，配置全局速率控制策略和具体用户速率控制策略。 
用户发起CP模式的附着业务，MME在向SGW/PGW发送的Create Session Request消息时，将下行Serving
PLMN Rate携带给PGW. 
在创建会话成功后，MME向UE发起激活默认承载请求，将上行Serving PLMN Rate携带给UE. 
MME对APN的速率控制实现内容如下： 
APN Rate Control相关信息都包含在PCO里，MME只是透传。 
在PDN连接时，UE会在PCO里携带标志，指示UE支持APN Rate Control。 
PGW会下发APN Rate Control值，包含在PCO里，由MME透传给UE。实现UE的APN Rate Control。  
业务流程 :附着流程
附着流程如下图所示。 
图3  附着流程

UE发起附着业务，就指示当前是NB-IoT接入，同时指明当前是使用的CP（控制面优化）模式。 
MME判断数据传输方式为CP，根据用户IMSI查表获得对应的Serving PLMN Rate配置，如查找不到记录或配置为不限制，则读取全局的Serving
PLMN Rate，获取配置完成后，MME在向SGW/PGW发送的Create Session Request消息中携带下行Serving
PLMN Rate。 
PGW返回Create Session Response，其中携带APN Rate信息。 
MME向UE发起激活默认承载请求，其中携带上行Serving PLMN Rate控制信息和APN Rate控制信息。 
局间TAU业务
局间TAU业务流程如下图所示。 
图4  局间TAU业务流程

UE发起局间TAU业务请求。 
新局MME向老局MME要用户上下文信息，发送Context Request消息。 
老局MME返回Context Respond消息，其中携带Serving PLMN Rate。 
新局 MME以基于老局MME的Serving PLMN Rate来控制上行报文速率，如老局响应消息中未携带，则不限制。（由于UE侧的速率控制参数无法修改，没有采用新局本地配置） 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :协议名|章节
---|---
23.401.e00|4.7.7 Support of rate control of user data using CIoT EPS optimisation
24.301.e01|ESM NAS消息中支持携带Extended protocol configuration options与 ServingPLMN rate control字段
29.128.d10|MME与SCEF间消息支持携带Extended protocol configuration options与 ServingPLMN rate control字段
29.274.e00|MME与SGW间GTP消息支持携带Extended protocol configuration options与 ServingPLMN rate control字段
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要开启License，对应的License项目为“MME支持包速率控制功能”（license ID：7111），此项目显示为“支持”，表示支持该功能。
对其他网元的要求 :UE|eNodeB (E-UTRAN)|SGW|PGW|HSS
---|---|---|---|---
-|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :配置项|命令
---|---
全局用户报文速率配置|SET NBIOT DATARATE
SHOW NBIOT DATARATE|全局用户报文速率配置
基于IMSI号段用户报文速率配置|ADD IMSI NBIOT DATARATE
SET IMSI NBIOT DATARATE|基于IMSI号段用户报文速率配置
DEL IMSI NBIOT DATARATE|基于IMSI号段用户报文速率配置
SHOW IMSI NBIOT DATARATE|基于IMSI号段用户报文速率配置
性能统计 :性能计数器名称
---
C432080008 拥塞控制丢弃ESM DATA Transport消息次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :虽然窄带物联网终端的数据传输速率极低，但物联网终端的量特别巨大，为避免网络拥塞，需要对物联网终端进行速率控制。 
速率控制包括针对拜访网络的“Serving PLMN Rate Control”及针对归属网络的“APN Rate Control”这两种控制方式，其中“APN
Rate Control”对MME不可见，“Serving PLMN Rate Control”由MME控制。 
服务PLMN速率控制参数由MME设置，包括上行控制速率及下行控制速率，并通过NAS接口及S11接口消息分别通知到UE及PGW，UE执行上行速率控制，PGW执行下行速率控制。 
配置前提 :对于速率控制功能，需要： 
MME支持用户CP 模式接入。 
MME支持速率控制。 
配置过程 :设置License：MME支持包速率控制功能设置为支持。 
支持用户CP模式接入：MME物联网相关业务功能开关（[SET MME IOT CFG]）中设置为支持。
基于IMSI的速率控制：新增基于IMSI号段用户报文速率（[ADD IMSI NBIOT DATARATE]）。
配置实例 :##### 实例场景 
配置对460119990023XXX号段进行速率控制，6分钟内只能发10个CP
SR（携带ESM Data Transport）。 
配置步骤 :步骤|说明|操作
---|---|---
1|license设置为支持。|该功能license设置为支持。
2|支持用户CP模式接入。|SET MME IOT CFG:CPSW="YES";
3|配置速率控制。|ADD IMSI NBIOT DATARATE:IMSI="460119990023",UPNASDATARATE=10,DOWNNASDATARATE=10;
测试用例 :测试项目|MME速率控制
测试目的|MME速率控制
预置条件|License支持速率控制。MME支持用户CP模式接入。
测试过程|MME配置Serving PLMN Rate Control，配置上下行限制速率。用户在6分钟内发送的报文已达到限制门限。用户发起CP SR携带ESM Data Transport。用户持续以CP SR发送报文，直到超过6分钟周期。
通过准则|1.6分钟内，MME丢弃CP SR中的ESM Data Transport消息，正常处理CP SR流程。超过6分钟后，MME正常转发ESM Data Transport消息。
测试结果|–
测试项目|APN速率控制
测试目的|APN速率控制
预置条件|License支持速率控制。MME支持用户CP模式接入。
测试过程|MME收到Create Session Response消息携带PCO，包含APN速率控制和包大小控制。
通过准则|MME发送Activate Default EPS Bearer Context Request消息中携带PCO，APN速率值和Create Session Response消息中一致。
测试结果|–
# ZUF-78-17-012 DECOR 
特性描述 :特性描述 :术语 :术语|含义
---|---
DCN|Dedicated Core Network，专用核心网
DECOR|即DCN，Dedicated Core Network，专用核心网
描述 :定义 :DECOR/eDECOR即专用核心网（以下简称专网），专网用于为特定的用户提供特定的业务和功能，这类用户包括物联网用户、特定的企业用户或者独立行政区域用户等。 
ZXUN uMAC支持DCN（Dedicated Core Network）功能，对于传统的物联网业务，可以通过DECOR/eDECOR技术把传统物联网终端迁移到专用核心网，构建专用的物联网核心网。
现网部署时，核心网可能会存在多个NB-IoT的DCN（Dedicated Core Network）。根据TSG RAN侧TS23.236的协议规范，NB-IoT
DCN可能会同时连接到E-UTRAN和NB-IoT的RAN节点，可以根据用户类型采取两种不同方案为其选择合适的DCN。 
第一种是重定向方案，参考TR23.707协议中的DECOR功能。 
第二种是UE辅助方案，参考TR23.711协议中的eDECOR功能。 
本特性用于介绍DECOR功能。 
背景知识 :物联网终端区别于人网终端，具有海量接入、低功耗等特性，具有专网服务的需求，在物联网应用快速发展的背景下，为物联网用户提供专网服务的需求越来越迫切。 
应用场景 :特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了DCN专网，MME通过DECOR技术支持将用户重定向到其所属的DCN网络下的MME下，完成附着、TAU、切换等。
客户收益 :受益方|受益描述
---|---
运营商|运营商可以根据接入网络的用户特性，将用户重定向到所属的DCN网络下的MME接入，灵活地为用户提供特定的特性和功能。
终端用户|该特性对终端用户不可见。
实现原理 :系统架构 :DCN组网架构如[图1]所示。
图1  DCN组网架构

涉及的网元 :网元名称|网元作用
---|---
UE|触发附着流程、跟踪区更新流程，完成安全功能，完成承载管理功能。
eNodeB|对用户进行接入层安全功能，完成MME的选择以及REROUTE功能，完成对用户无线资源管理功能。
MME|对用户进行接入控制和安全功能，完成MME的选择及是否REROUTE的判断，完成SGW和PGW的选择，完成用户临时标识的分配，完成TA List的分配，完成MME或SGSN的选择，完成HSS的选择，完成承载管理功能。
HSS|把用户签约数据提供给MME，存储用户目前所接入的MME信息。
本网元实现 :MME判断用户接入流程是否为专网用户接入流程，是否需要获取UE Usage
Type和MMEGI，判断流程参见[图2]。
图2  MME支持DECOR

MME获取UE Usage Type的方式有如下两种。 
向老局获取在局间Attach/TAU流程中，如果“UE Usage Type”参数可用，则老局MME/SGSN在Identification
Response message/Context Response message消息中携带“UE Usage Type”参数。 
向HSS获取若MME需要获取UE Usage Type，并且没有从老局MME/SGSN中获取到UE Usage
Typ，则MME发送Authentication Information Request message消息给HSS，此消息中设置“Send
UE Usage Type”标识位为有效。如果需要获取鉴权向量集，则同时携带鉴权向量集类型和请求的数目。如果不需要获取鉴权向量集，则只设置“Send
UE Usage Type”标识位为有效。HSS在Authentication Information Answer message消息中返回“UE
Usage Type”参数，同时可能携带请求的鉴权向量集，MME保存“UE Usage Type”参数。如果“UE Usage
Type”获取失败，则认为不是专用用户，按普通用户流程处理。 
MME获取到“UE Usage Type”后，基于本地的配置数据或者通过向DNS查询来获取MMEGI，再判断是否需要进行重定向，业务流程参见[图3]。
图3  是否执行重定向流程

如果第一个新局MME决策不需要发送重定向NAS消息（本局就是为UE服务的专网MME），则正常处理Attach/TAU流程。 
如果第一个新局MME决策需要发送重定向NAS消息到专网MME，第一个新局MME将执行“NAS Message Redirection
Procedure（NAS消息的重定向流程）”。在TAU流程中，如果存在老局MME/SGSN，则第一个新局MME发送Context
Acknowledge Message消息并携带失败原因（Service denied），老局MME/SGSN会按照没有收到Context
Request消息的情况，后续正常处理第二个新局的“NAS Message Redirection Procedure（NAS消息的重定向流程）”，Attach流程结束，用户上下文保持为原样（即对于新接入用户，删除其上下文。对于老用户，保留其上下文），释放S1AP。 
如果第一个新局MME决策需要拒绝NAS消息，则MME根据SET DECOR CONTROL POLICY命令中配置的参数“MME是否拒绝专网用户接入”，正常处理Attach/TAU流程或发送Attach/TAU拒绝消息，携带合适的Cause和backoff timer，避免UE立即重新触发Attach/TAU。 
 说明： 
连接态下（如切换）的TAU不应该执行NAS message重定向。 
业务流程 :NAS消息的重定向流程
图4  NAS Message Redirection Procedure：

第一个新局MME发送Reroute NAS Message Request消息（其中携带的参数包括original RAN
message、reroute parameters、Additional GUTI/P-TMSI、UE Usage Type和optionally
the IMSI)给eNodeB。其中Reroute parameter是DCN对应于UE Usage Type中的MMEGI，MME使用DNS查询确定DCN对应的MMEGI。如果UE提供了可用的Additional
GUTI，则携带Additional GUTI参数。如果UE Usage Type可用，则携带UE Usage Type参数。原RAN
message是来自eNodeB的完整的PDU，包括原NAS Request message和所有的RAN
IEs。
eNodeB基于MMEGI和Additional GUTI选择第二个新局MME。如果Additional GUTI标识了由MMEGI表示的有效节点集内的一个MME，则eNodeB选择该MME。否则eNodeB选择一个对应MMEGI的MME。如果MMEGI标识的有效节点集内没有有效的MME，则eNodeB从默认DCN中选择一个MME或者基于运营商的配置数据选择发送Reroute
Request消息的MME。 
eNodeB发送Initial UE Message给选择的第二个新局MME，Initial UE message中包括NAS
Request message和来自第一个新局MME的MMEGI、UE Usage Type和IMSI。MMEGI标识了该NAS message是重定向过来的消息，第二个新局MME不应该reroute
the NAS message。第二个新局MME使用UE Usage Type选择SGW和PGW。 
Attach/TAU流程
图5  Attach/TAU流程

用户发起Attach/TAU流程。如果DCN-ID可用，则UE会在请求消息中提供DCN-ID，此DCN-ID是PLMN确定的DCN-ID或默认标准的DCN-ID。eNodeB根据DCN-ID选择一个DCN和该DCN内的一个服务的MME。
eNodeB将DCN-ID在初始请求消息中带给MME。如果UE提供GUTI等信息指示了一个节点MME，eNodeB根据UE
GUTI等信息选择服务节点MME优先于根据DCN-ID选择服务节点MME。
如果UE使用GUTI标识且MME发生了改变，则在Attach流程中，如果“UE Usage Type”参数可用，老局MME/SGSN在Identification
Response message中携带“UE Usage Type”参数。在TAU流程中，老局MME/SGSN在Context Response
Message中携带“UE Usage Type”参数。 
如果第一个新局MME已经获取到了“UE Usage Type”参数，或者基于本地配置数据和UE上下文，MME确定是否需要为该用户提供服务。 
如果第一个新局MME没有从eNodeB获取到MMEGI，不能确定是否为该用户提供服务，MME发送Authentication
Information Request Message给HSS，请求消息中设置”Send UE Usage Type”标识位有效，也可以同时携带一个或多个鉴权向量。如果“UE
Usage Type”参数可用，HSS在Authentication Information Answer Message中返回“UE
Usage Type”参数，同时携带请求的鉴权向量。 
如果第一个新局MME已经获取到了“UE Usage Type”参数，或者基于本地配置数据和UE上下文，MME确定是否需要为该用户提供服务。 
如果第一个新局MME没有从eNodeB获取到MMEGI，不能确定是否为该用户提供服务，MME发送Authentication
Information Request Message给HSS，请求消息中设置”Send UE Usage Type”标识位有效，也可以同时携带一个或多个鉴权向量。 
如果“UE Usage Type”参数可用，HSS在Authentication Information Answer
Message中返回“UE Usage Type”参数，同时携带请求的鉴权向量。 
如果第一个新局MME决策发送重定向NAS消息到专网MME，第一个新局MME将执行“NAS
Message Redirection Procedure”。在TAU流程中，如果存在老局MME/SGSN，则第一个新局MME发送Context
Acknowledge Message并携带失败原因。老局MME/SGSN按照没有收到Context Request消息的情况，后续正常处理第二个新局MME的Context
Request。
如果第一个新局MME决策不需要重定向NAS消息（本局就是为UE服务的专网MME），则正常处理Attach/TAU流程。如果DCN-ID可用，MME发送Attach/TAU
Accept消息携带DCN-ID。如果服务PLMN的DCN-ID改变，UE更新存储的DCN-ID参数。 
如果第一个新局MME决策需要拒绝NAS消息（本局不是为UE服务的专网MME，且MME不支持NAS重定向），则MME根据SET DECOR CONTROL POLICY命令中配置的参数“MME是否拒绝专网用户接入”来正常处理Attach/TAU流程或发送Attach/TAU拒绝消息，携带合适的Cause和backoff
timer，避免UE立即重新触发Attach/TAU。 
第二个新局MME收到eNodeB发送的Rerouted NAS message（Attach/TAU请求），消息中携带MMEGI。 
MME执行Attach/TAU流程处理。或者根据本地的配置数据，MME发送Attach/TAU拒绝消息，携带合适的Cause和backoff
timer。 
同样，在Attach流程中，如果“UE Usage Type”参数可用，老局MME/SGSN在Identification
Response message中携带“UE Usage Type”参数。在TAU流程中，老局MME/SGSN在Context Response
message中携带“UE Usage Type”参数。 
如果在NAS Message Redirection Procedure中，第二个新局MME从第一个新局MME获得了IMSI，则第二个新局MME不需要从UE获取IMSI。 
如果DCN-ID可用，MME发送Attach/TAU Accept消息，其中携带DCN-ID。如果服务PLMN的DCN-ID改变，UE更新存储的DCN-ID参数。由于来自eNodeB的Initial
UE message/UL-Unitdata message包括MMEGI，第二个新局MME不应该发送reroute the NAS
message消息到另一个MME。 
Handover流程
当切换过程中MME改变，如果UE Usage
Type可用，从源MME发送到目标MME的Forward Relocation Request message消息中携带UE Usage
Type。适用S1-based handover和E-UTRAN to UTRAN Iu mode Inter RAT handover切换流程。 
当UE从DCN未使用区域切换到支持DCN的区域并且MME改变时，Target MME在切换后的TAU流程中从HSS获取UE
Usage Type。如果Target MME确定SGW不支持该UE Usage Type，Target MME触发SGW改变的切换流程。如果Target
MME不服务于此UE Usage Type，切换流程成功执行完成，Target MME使用GUTI重分配流程将UE重定向到服务的DCN。 
初始Dedicated Core Network重选流程
部署DCN后，该流程用于如下两种情况： 
HSS更新UE服务节点的UE Usage Type签约信息。该过程可能导致UE的服务节点改变。 
切换后Target MME重定向UE的服务DCN，此时MME触发UE服务节点的改变。图6  初始Dedicated Core Network重选流程HSS发送Insert Subscriber Data Request Message（携带IMSI, Subscription Data）给MME，签约数据包括UE
Usage Type参数。MME更新存储的签约数据，回复Insert Subscriber Data Answer (IMSI) Message给HSS。如果MME能继续服务该UE，则此流程结束。如果MME决策将UE重定向到另外一个MME，或者MME判断DCN-ID需要立即更新，并且UE为空闲态，则MME寻呼UE，或者MME一直等到用户激活后再继续后续流程。如果MME决策将UE重定向到另外一个MME，则执行步骤4-7或步骤8。如果UE已经处于连接态或UE通过Initiating data transfer进入连接态时，执行步骤4-7。UE处于空闲态，执行步骤8。如果MME决策仅更新UE的DCN-ID时，执行步骤4-5。UE通过寻呼或uplink data触发NAS连接建立，或者UE通过TAU请求触发NAS连接建立。当一个NAS连接已经存在，或者Initiating data transfer的NAS连接已经存在，MME触发GUTI
Reallocation过程。如果DCN-ID可用且MME决策UE应该被更新一个新的DCN-ID，则GUTI Reallocation
Command中包含新的DCN-ID。MME释放无线资源且UE进入空闲模式。如果大量的UE需要卸载，则MME不应该立即释放所有UE的无限资源，避免忽然的UE重定向使核心网节点过载，MME应等到UE去活才释放。Non-broadcast TAI会触发UE立即发起TAU。如果新的DCN-ID可用，UE会将新的DCN-ID发给eNodeB。UE发起TAU。MME收到TAU Request message，如果由于MME不服务于此UE Usage Type，则此MME触发NAS
Message redirection procedure。后续执行TAU处理。 
HSS删除用户的UE Usage Type签约数据
HSS删除用户的UE Usage Type签约数据如下图所示。 
图7  HSS删除用户的UE Usage Type签约数据流程图

用户修改了签约数据，HSS向MME发送了Delete Subscriber Data Request消息，通知MME删除掉用户UE Usage Type签约数据。MME收到的Delete Subscriber Data Request消息，消息中DSR Flags AVP中包含指示用户删除的UE Usage Type Withdrawal AVP，MME删除用户的UE Usage Type。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: General Packet Radio Service (GPRS) enhancementsforEvolved Universal Terrestrial Radio Access Network (E-UTRAN) access|4.3.25
3GPP TS 36.413: Evolved Universal Terrestrial Radio AccessNetwork(E-UTRAN);S1 Application Protocol (S1AP)|8.6.2.18.6.2.59.2.3.45
3GPP TS 29.274: Evolved General Packet Radio Service (GPRS)Tunnelling Protocol for Control plane (GTPv2-C)|7.3.17.3.67.3.9
3GPP TS 29.272: Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol|5.2.1.15.2.2.15.2.37.3.27.3.2017.3.202
3GPP TS 24.301: Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS)|8.2.1.18.2.1.158.2.16.18.2.26.1
3GPP TS 23.885: Technical Specification Group Services andSystem Aspects;Feasibility Study of Single Radio Voice Call Continuity(SRVCC) from UTRAN/GERAN to E-UTRAN/HSPA|-
3GPP TS 29.280: Technical Specification Group Core Networkand Terminals;Evolved Packet System (EPS);3GPP Sv interface (MME toMSC, and SGSN to MSC) for SRVCC|-
3GPP TS 29.303: Technical Specification Group Core Networkand Terminals Domain Name System Procedures|-
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License为7106 MME支持DECOR，此项目显示为“支持”，表示ZXUN uMAC支持DECOR功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项 
配置项|命令
---|---
DECOR控制策略配置|SET DECOR CONTROL POLICY
SHOW DECOR CONTROL POLICY|DECOR控制策略配置
DECOR/eDECOR公共控制策略配置|SET DECOR EDECOR CTRL POLICY
SHOW DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
ADD IMSI DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
SET IMSI DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
DEL IMSI DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
SHOW IMSI DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
专网MME权重配置|ADD DCN MME WEIGHT
SET DCN MME WEIGHT|专网MME权重配置
DEL DCN MME WEIGHT|专网MME权重配置
SHOW DCN MME WEIGHT|专网MME权重配置
MMEGI解析配置|ADD MMEGI RESOLVE
SET MMEGI RESOLVE|MMEGI解析配置
DEL MMEGI RESOLVE|MMEGI解析配置
SHOW MMEGI RESOLVE|MMEGI解析配置
非广播跟踪区配置|ADD NONBCTA
DEL NONBCTA|非广播跟踪区配置
SHOW NONBCTA|非广播跟踪区配置
配置项|命令|新增参数
---|---|---
EPCAPN HOST配置|ADD EPC APN|“用户使用类型”参数中增加专网用户使用类型，可多选。
SET EPC APN|EPCAPN HOST配置|“用户使用类型”参数中增加专网用户使用类型，可多选。
PGW解析配置|ADD EPC PGW|“用户使用类型”参数中增加专网用户使用类型，可多选。
SET EPC PGW|PGW解析配置|“用户使用类型”参数中增加专网用户使用类型，可多选。
EPC地址解析配置|ADD EPCHOST|“用户使用类型”参数中增加专网用户使用类型，可多选。
SET EPCHOST|EPC地址解析配置|“用户使用类型”参数中增加专网用户使用类型，可多选。
性能统计 :性能计数器名称
---
C432000083 Reroute NAS Request消息发送次数
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过DECOR的相关配置，实现MME的DECOR REROUTE接入控制。 
配置前提 :MME网元与其他网元的对接和业务配置已完成。 
确认License 7106 MME支持DECOR为支持。 
配置过程 :通过[SET DECOR CONTROL POLICY]命令，设置DECOR控制策略。
通过[SET DECOR EDECOR CTRL POLICY]命令，设置DECOR/eDECOR公共控制策略。
通过[ADD DNS SERVER]命令，新增DNS服务器配置。
通过[ADD DNS SRVGRP]命令，新增DNS服务器组配置。
通过[ADD DNS PROFILE]命令，新增DNS Profile配置。
通过[SET SOFTWARE PARAMETER]命令，设置软参“MME地址解析优先级控制”为1。
通过[ADD MMEGI RESOLVE]命令，新增MMEGI解析配置。
配置实例 :在GUTI不属于本地MME的情况下，完成GUTI附着及局间TAU流程，详细配置过程参见下表。 
配置步骤|配置说明
---|---
SET DECOR CONTROL POLICY:MMESUPDECOR="YES",MINDELAY=10,MAXDELAY=20;|设置DECOR控制策略：MME支持DECOR功能，设置Back-off Timer的最小值为10s，最大值为20s。
SET DECOR EDECOR CTRL POLICY:USERDEFDCNSUP="SUPDECOR";|设置DECOR/eDECOR公共控制策略：将用户默认专网支持参数设置为SUPDECOR。
ADD DNS SERVER:ID=1,SERVERIPADDR="192.20.32.172",CLIENTIPADDR="192.20.152.1",VRFID=51;|新增DNS服务器配置：设置DNS服务器编号1，设置DNS服务器IP地址192.20.32.172，DNS客户端IP地址192.20.152.1，VRFID为51。
ADD DNS SRVGRP:ID=1,SVRLST=1-0;|新增DNS服务器组配置：设置DNS服务器组号1，DNS服务器列表为1-0。
ADD DNS PROFILE:TYPE="LTE",SVRGRPLST=1-0;|新增DNS Profile配置：设置DNS Profile类型为LTE，DNS服务器列表为1-0。
SET SOFTWARE PARAMETER:PARAID=65593,PARAVALUE=1;|设置软参“MME地址解析优先级控制”为1。
ADD MMEGI RESOLVE:LGCNAME="tac-lb01.tac-hb61.tac.epc.mnc011.mcc460.3gppnetwork.org",UEUSAGETYPE=130,MMEGI=32840;|新增MMEGI解析配置：设置逻辑名称tac-lb01.tac-hb61.tac.epc.mnc011.mcc460.3gppnetwork.org，用户使用类型130，MMEGroup ID=32840;
测试用例 :测试项目|专网用户GUTI附着，GUTI不属于本地
---|---
测试目的|验证MME能实现DECOR REROUTE接入功能
预置条件|LTE网络内的所有网元运行正常用户在HSS开户，并签约LTE业务，且支持专网接入新局MME支持DECOR的license打开新局MME支持DECOR的开关打开新局配置用户默认支持DECOR
测试过程|本地用户在老局IMSI非专网接入成功。用户在新局发起局间GUTI附着，Initial UEMessage中不包括MMEGI。用户发起ID请求，老局回复的ID response中携带IMSI，未携带UE usage typeMME向HSS获取UE usage type成功。实现NAS Message Redirection Procedure功能，用户成功通过REROUTE接入到新局MME
通过准则|新局局间GUTI附着过程中，新局根据老局返回的IMSI判断用户是专网用户因老局未返回UE Usage Type，MME向HSS发起AIR获取鉴权向量，AIR消息中设置"Send UE Usage Type" flag有效，AIA消息中携带“UE Usage Type”参数根据TA-FQDN和UE Usage Typ解析到MMEGI后，用户专网接入成功
测试结果|-
测试项目|专网用户局间TAU，通过context response获取UEusage type失败，向HSS获取成功
---|---
测试目的|验证MME能实现专网局间TAU功能
预置条件|LTE网络内的所有网元运行正常用户在HSS开户，并签约LTE业务，且支持专网接入新局MME支持DECOR的license打开新局MME支持DECOR的开关打开新局配置用户默认支持DECOR
测试过程|本地用户在老局IMSI专网接入成功用户在新局发起局间TAU，Initial UE Message中不包括MMEGI用户发起Context Request，老局回复的Context response消息中携带IMSI,未携带UE Usage Type。向HSS获取UE Usage Type成功实现专网局间TAU功能
通过准则|新局局间TAU过程中，根据老局返回的IMSI判断用户是专网用户因老局未返回UE Usage Type，MME向HSS发起AIR获取鉴权向量集的同时携带AIR-Flags，其中“Send UE Usage Type“的标识为1根据获取到的“UE Usage Type”和TA-FQDN解析到MMEGI用户局间TAU成功
测试结果|-
# ZUF-78-17-013 eDECOR 
特性描述 :特性描述 :术语 :术语|含义
---|---
DCN|Dedicated Core Network，专用核心网
eDECOR|Enhancements of Dedicated Core Network，增强的专用核心网。eDECOR是Decor的演进，由UE协助进行专网选择，eDECOR使用UE携带的DCN-ID，通过RAN选择专网，从而减少了DECOR的重新定向路由的过程。
描述 :定义 :DECOR/eDECOR即专用核心网（以下简称专网），专网用于为特定的用户提供特定的业务和功能，这类用户包括物联网用户、特定的企业用户或者独立行政区域用户等。 
ZXUN uMAC支持DCN（Dedicated Core Network）功能，对于传统的物联网业务，可以通过DECOR/eDECOR技术把传统物联网终端迁移到专用核心网，构建专用的物联网核心网。
现网部署时，核心网可能会存在多个NB-IoT的DCN（Dedicated Core Network）。根据TSG RAN侧TS23.236的协议规范，NB-IoT
DCN可能会同时连接到E-UTRAN和NB-IoT的RAN节点，可以根据用户类型采取两种不同方案为其选择合适的DCN。 
第一种是重定向方案，参考TR23.707协议中的DECOR功能。 
第二种是UE辅助方案，参考TR23.711协议中的eDECOR功能。 
本特性用于介绍eDECOR功能。 
背景知识 :物联网终端区别于人网终端，具有海量接入、低功耗等特性，具有专网服务的需求，在物联网应用快速发展的背景下，为物联网用户提供专网服务的需求越来越迫切。 
应用场景 :特定用户（物联网用户、特定的企业用户或者独立行政区域用户等）接入网络进行业务（附着、TAU、切换等）时，如果运营商部署了DCN专网且UE存储了默认DCN标识、按PLMN存储了DCN标识，UE提供DCN标识给eNodeB，eNodeB根据DCN标识为用户选择专网MME，减少信令改向，MME及时识别DCN标识改变并通知UE更新。
客户收益 :受益方|受益描述
---|---
运营商|运营商可以根据接入网络的用户特性，将用户重定向到所属的DCN网络下的MME接入，灵活地为用户提供特定的特性和功能。
终端用户|该特性对终端用户不可见。
实现原理 :系统架构 :多个DCN可以共享同一个RAN，不同用户可通过RAN路由至对应的DCN。多个DCN可以组成DCN
POOL，如物联网DCN，因为一个MME容纳不了海量终端，需要多个MME。 
DCN组网架构如[图1]所示。
图1  DCN组网架构

涉及的网元 :网元名称|网元作用
---|---
UE|触发附着流程、跟踪区更新流程，完成安全功能，完成承载管理功能
eNodeB|对用户进行接入层安全功能，完成MME的选择以及REROUTE功能，完成对用户无线资源管理功能。
MME|对用户进行接入控制和安全功能，完成MME的选择及是否REROUTE的判断，完成SGW和PGW的选择，完成用户临时标识的分配，完成TAList的分配，完成MME或SGSN的选择，完成HSS的选择，完成承载管理功能
HSS|把用户签约数据提供给MME，存储用户目前所接入的MME信息
本网元实现 :MME判断用户接入流程是否为专网用户接入流程，是否需要获取UE Usage
Type和MMEGI，判断流程参见[图2]。
图2  eDecor流程

MME获取UE Usage Type的方式有如下两种。 
向老局获取在局间Attach/TAU流程中，如果“UE Usage Type”参数可用，则老局MME/SGSN在Identification
Response message/Context Response message消息中携带“UE Usage Type”参数。 
向HSS获取若MME需要获取UE Usage Type，并且没有从老局MME/SGSN中获取到UE Usage
Typ，则MME发送Authentication Information Request message消息给HSS，此消息中设置“Send
UE Usage Type”标识位为有效。如果需要获取鉴权向量集，则同时携带鉴权向量集类型和请求的数目。如果不需要获取鉴权向量集，则只设置“Send
UE Usage Type”标识位为有效。HSS在Authentication Information Answer message消息中返回“UE
Usage Type”参数，同时可能携带请求的鉴权向量集，MME保存“UE Usage Type”参数。如果“UE Usage
Type”获取失败，则认为不是专用用户，按普通用户流程处理。 
新的MME交换局处理： 
第二个新局MME收到eNodeB发送的Initial UE Message（Attach/TAU请求），消息中携带MMEGI，则MME执行完成Attach/TAU流程处理；或者根据配置MME发送Attach/TAU拒绝消息，携带合适的Cause（No
Suitable Cells In tracking area）和backoff timer。 
在Attach流程中，如果“UE Usage Type”参数可用，老局MME/SGSN在Identification
Response Message中携带“UE Usage Type”参数；在TAU流程中，老局MME/SGSN在Context Response
Message中携带“UE Usage Type”参数。 
如果SET EDECOR CONTROL POLICY中的参数“MME是否支持eDECOR”开关打开，表示UE支持eDECOR，MME根据ADD DCN IDENTITY命令的配置结果获取到DCN-ID，MME发送Attach/TAU Accept消息中携带DCN-ID；如果服务PLMN的DCN-ID改变，UE更新存储的DCN-ID参数。 
由于来自eNodeB的Initial UE message包括MMEGI，第二个新局MME不应该发送Reroute the
NAS Message消息到另一个MME，可直接拒绝。 
 说明： 
连接态下（如切换）的TAU不应该执行NAS message重定向。 
业务流程 :Attach/TAU流程
图3  Attach/TAU流程

用户发起Attach/TAU流程。如果DCN-ID可用，则UE会在请求消息中提供DCN-ID，此DCN-ID是PLMN确定的DCN-ID或默认标准的DCN-ID。eNodeB根据DCN-ID选择一个DCN和该DCN内的一个服务的MME。
eNodeB将DCN-ID在初始请求消息中带给MME。如果UE提供GUTI等信息指示了一个节点MME，eNodeB根据UE
GUTI等信息选择服务节点MME优先于根据DCN-ID选择服务节点MME。
如果UE使用GUTI标识且MME发生了改变，则在Attach流程中，如果“UE Usage Type”参数可用，老局MME/SGSN在Identification
Response message中携带“UE Usage Type”参数。在TAU流程中，老局MME/SGSN在Context Response
Message中携带“UE Usage Type”参数。 
如果第一个新局MME已经获取到了“UE Usage Type”参数，或者基于本地配置数据和UE上下文，MME确定是否需要为该用户提供服务。 
如果第一个新局MME没有从eNodeB获取到MMEGI，不能确定是否为该用户提供服务，MME发送Authentication
Information Request Message给HSS，请求消息中设置”Send UE Usage Type”标识位有效，也可以同时携带一个或多个鉴权向量。如果“UE
Usage Type”参数可用，HSS在Authentication Information Answer Message中返回“UE
Usage Type”参数，同时携带请求的鉴权向量。 
如果第一个新局MME已经获取到了“UE Usage Type”参数，或者基于本地配置数据和UE上下文，MME确定是否需要为该用户提供服务。 
如果第一个新局MME没有从eNodeB获取到MMEGI，不能确定是否为该用户提供服务，MME发送Authentication
Information Request Message给HSS，请求消息中设置”Send UE Usage Type”标识位有效，也可以同时携带一个或多个鉴权向量。 
如果“UE Usage Type”参数可用，HSS在Authentication Information Answer
Message中返回“UE Usage Type”参数，同时携带请求的鉴权向量。 
如果第一个新局MME决策发送重定向NAS消息到专网MME，第一个新局MME将执行“NAS
Message Redirection Procedure”。在TAU流程中，如果存在老局MME/SGSN，则第一个新局MME发送Context
Acknowledge Message并携带失败原因。老局MME/SGSN按照没有收到Context Request消息的情况，后续正常处理第二个新局MME的Context
Request。
如果第一个新局MME决策不需要重定向NAS消息（本局就是为UE服务的专网MME），则正常处理Attach/TAU流程。如果DCN-ID可用，MME发送Attach/TAU
Accept消息携带DCN-ID。如果服务PLMN的DCN-ID改变，UE更新存储的DCN-ID参数。 
如果第一个新局MME决策需要拒绝NAS消息（本局不是为UE服务的专网MME，且MME不支持NAS重定向），则MME根据SET DECOR CONTROL POLICY命令中配置的参数“MME是否拒绝专网用户接入”来正常处理Attach/TAU流程或发送Attach/TAU拒绝消息，携带合适的Cause和backoff
timer，避免UE立即重新触发Attach/TAU。 
第二个新局MME收到eNodeB发送的Rerouted NAS message（Attach/TAU请求），消息中携带MMEGI。 
MME执行Attach/TAU流程处理。或者根据本地的配置数据，MME发送Attach/TAU拒绝消息，携带合适的Cause和backoff
timer。 
同样，在Attach流程中，如果“UE Usage Type”参数可用，老局MME/SGSN在Identification
Response message中携带“UE Usage Type”参数。在TAU流程中，老局MME/SGSN在Context Response
message中携带“UE Usage Type”参数。 
如果在NAS Message Redirection Procedure中，第二个新局MME从第一个新局MME获得了IMSI，则第二个新局MME不需要从UE获取IMSI。 
如果DCN-ID可用，MME发送Attach/TAU Accept消息，其中携带DCN-ID。如果服务PLMN的DCN-ID改变，UE更新存储的DCN-ID参数。由于来自eNodeB的Initial
UE message/UL-Unitdata message包括MMEGI，第二个新局MME不应该发送reroute the NAS
message消息到另一个MME。 
Handover流程
当切换过程中MME改变，如果UE Usage
Type可用，从源MME发送到目标MME的Forward Relocation Request message消息中携带UE Usage
Type。适用S1-based handover和E-UTRAN to UTRAN Iu mode Inter RAT handover切换流程。 
当UE从DCN未使用区域切换到支持DCN的区域并且MME改变时，Target MME在切换后的TAU流程中从HSS获取UE
Usage Type。如果Target MME确定SGW不支持该UE Usage Type，Target MME触发SGW改变的切换流程。如果Target
MME不服务于此UE Usage Type，切换流程成功执行完成，Target MME使用GUTI重分配流程将UE重定向到服务的DCN。 
初始Dedicated Core Network重选流程
部署DCN后，该流程用于如下两种情况： 
HSS更新UE服务节点的UE Usage Type签约信息。该过程可能导致UE的服务节点改变。 
切换后Target MME重定向UE的服务DCN，此时MME触发UE服务节点的改变。图4  初始Dedicated Core Network重选流程HSS发送Insert Subscriber Data Request Message（携带IMSI, Subscription Data）给MME，签约数据包括UE
Usage Type参数。MME更新存储的签约数据，回复Insert Subscriber Data Answer (IMSI) Message给HSS。如果MME能继续服务该UE，则此流程结束。如果MME决策将UE重定向到另外一个MME，或者MME判断DCN-ID需要立即更新，并且UE为空闲态，则MME寻呼UE，或者MME一直等到用户激活后再继续后续流程。如果MME决策将UE重定向到另外一个MME，则执行步骤4-7或步骤8。如果UE已经处于连接态或UE通过Initiating data transfer进入连接态时，执行步骤4-7。UE处于空闲态，执行步骤8。如果MME决策仅更新UE的DCN-ID时，执行步骤4-5。UE通过寻呼或uplink data触发NAS连接建立，或者UE通过TAU请求触发NAS连接建立。当一个NAS连接已经存在，或者Initiating data transfer的NAS连接已经存在，MME触发GUTI
Reallocation过程。如果DCN-ID可用且MME决策UE应该被更新一个新的DCN-ID，则GUTI Reallocation
Command中包含新的DCN-ID。MME释放无线资源且UE进入空闲模式。如果大量的UE需要卸载，则MME不应该立即释放所有UE的无限资源，避免忽然的UE重定向使核心网节点过载，MME应等到UE去活才释放。Non-broadcast TAI会触发UE立即发起TAU。如果新的DCN-ID可用，UE会将新的DCN-ID发给eNodeB。UE发起TAU。MME收到TAU Request message，如果由于MME不服务于此UE Usage Type，则此MME触发NAS
Message redirection procedure。后续执行TAU处理。 
HSS删除用户的UE Usage Type签约数据
HSS删除用户的UE Usage Type签约数据如下图所示。 
图5  HSS删除用户的UE Usage Type签约数据流程图

用户修改了签约数据，HSS向MME发送了Delete Subscriber Data Request消息，通知MME删除掉用户UE Usage Type签约数据。MME收到的Delete Subscriber Data Request消息，消息中DSR Flags AVP中包含指示用户删除的UE Usage Type Withdrawal AVP，MME删除用户的UE Usage Type。 
系统影响 :该特性不涉及对系统的影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: General Packet Radio Service (GPRS) enhancementsforEvolved Universal Terrestrial Radio Access Network (E-UTRAN) access|4.3.25
3GPP TS 36.413: Evolved Universal Terrestrial Radio AccessNetwork(E-UTRAN);S1 Application Protocol (S1AP)|8.6.2.18.6.2.59.2.3.45
3GPP TS 29.274: Evolved General Packet Radio Service (GPRS)Tunnelling Protocol for Control plane (GTPv2-C)|7.3.17.3.67.3.9
3GPP TS 29.272: Mobility Management Entity (MME) and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol|5.2.1.15.2.2.15.2.37.3.27.3.2017.3.202
3GPP TS 24.301: Non-Access-Stratum (NAS) protocol for EvolvedPacket System (EPS)|8.2.1.18.2.1.158.2.16.18.2.26.1
3GPP TS 23.885: Technical Specification Group Services andSystem Aspects;Feasibility Study of Single Radio Voice Call Continuity(SRVCC) from UTRAN/GERAN to E-UTRAN/HSPA|-
3GPP TS 29.280: Technical Specification Group Core Networkand Terminals;Evolved Packet System (EPS);3GPP Sv interface (MME toMSC, and SGSN to MSC) for SRVCC|-
3GPP TS 29.303: Technical Specification Group Core Networkand Terminals Domain Name System Procedures|-
特性能力 :该特性不涉及规格指标。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License为7107 MME支持eDECOR，项目显示为“支持”，表示支持eDECOR功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项 
配置项|命令
---|---
eDECOR控制策略配置|SET EDECOR CONTROL POLICY
SHOW EDECOR CONTROL POLICY|eDECOR控制策略配置
DECOR/eDECOR公共控制策略配置|SET DECOR EDECOR CTRL POLICY
SHOW DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
ADD IMSI DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
SET IMSI DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
DEL IMSI DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
SHOW IMSI DECOR EDECOR CTRL POLICY|DECOR/eDECOR公共控制策略配置
专网MME权重配置|ADD DCN MME WEIGHT
SET DCN MME WEIGHT|专网MME权重配置
DEL DCN MME WEIGHT|专网MME权重配置
SHOW DCN MME WEIGHT|专网MME权重配置
MMEGI解析配置|ADD MMEGI RESOLVE
SET MMEGI RESOLVE|MMEGI解析配置
DEL MMEGI RESOLVE|MMEGI解析配置
SHOW MMEGI RESOLVE|MMEGI解析配置
非广播跟踪区配置|ADD NONBCTA
DEL NONBCTA|非广播跟踪区配置
SHOW NONBCTA|非广播跟踪区配置
配置项|命令|新增参数
---|---|---
EPCAPN HOST配置|ADD EPC APN|“用户使用类型”参数中增加专网用户使用类型，可多选。
SET EPC APN|EPCAPN HOST配置|“用户使用类型”参数中增加专网用户使用类型，可多选。
PGW解析配置|ADD EPC PGW|“用户使用类型”参数中增加专网用户使用类型，可多选。
SET EPC PGW|PGW解析配置|“用户使用类型”参数中增加专网用户使用类型，可多选。
EPC地址解析配置|ADD EPCHOST|“用户使用类型”参数中增加专网用户使用类型，可多选。
SET EPCHOST|EPC地址解析配置|“用户使用类型”参数中增加专网用户使用类型，可多选。
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过eDECOR的相关配置，实现MME的eDECOR专网用户接入控制。 
配置前提 :MME网元与其他网元的对接和业务配置已完成。 
确认License 7107 MME支持eDECOR为支持。 
配置过程 :通过[SET EDECOR CONTROL POLICY]命令，设置eDECOR控制策略。
通过[SET DECOR EDECOR CTRL POLICY]命令，设置DECOR/eDECOR公共控制策略。
通过[ADD DCN IDENTITY]命令，新增DCN-ID配置。配置PLMN+UE
Usage Type关联DCN-ID
配置实例 :配置步骤|配置说明
---|---
SET EDECOR CONTROL POLICY:MMESUPEDECOR="YES";|设置eDECOR控制策略：MME支持eDECOR；
SET DECOR EDECOR CTRL POLICY:USERDEFDCNSUP="SUPEDECOR";|设置DECOR/eDECOR公共控制策略：用户默认专网支持设置为SUPEDECOR；
ADD DCN IDENTITY:PLMN="460"-"11",UEUSAGETYPE=129,DCNID=291;|新增DCN-ID配置：PLMN="460"-"11"；用户使用类型为129；DCN标识为291；
测试用例 :测试项目|专网用户eDECOR附着，不用获取鉴权向量，向HSS获取UE Usage Type成功
---|---
测试目的|验证MME能实现eDECOR接入功能
预置条件|LTE网络内的所有网元运行正常用户在HSS开户，并签约LTE业务，且支持专网接入新局MME支持eDECOR的License打开新局MME支持eDECOR的开关打开新局配置用户默认支持eDECOR
测试过程|本地用户在老局IMSI非专网接入成功本局存在上下文的用户，上下文中不存在“UE Usage Type”，再次GUTI附着，不需要获取鉴权向量HSS返回的AIA携带“UE Usage Type”（128-255），向HSS获取UE UsageType成功
通过准则|GUTI附着过程中，判断是用户支持eDECOR，用户发起AIR未携带鉴权向量请求、携带AIR-Flags，其中“Send UE Usage Type“标识位为1。用户根据HSS返回的UE Usage Type本地解析到DCN-IDAttach Accept中携带DCN-ID
测试结果|-
测试项目|专网用户eDECOR局间TAU，通过context response获取UE UsageType失败，向HSS获取成功
---|---
测试目的|验证MME能实现eDECOR局间TAU功能
预置条件|LTE网络内的所有网元运行正常用户在HSS开户，并签约LTE业务，且支持专网接入新局MME支持eDECOR的license打开新局MME支持eDECOR的开关打开新局配置用户默认支持eDECOR
测试过程|本地用户在老局IMSI专网接入成功用户在新局发起局间TAU用户发起Context Request，老局回复的Context Response中携带IMSI，未携带UE UsageType向HSS获取UE UsageType成功实现eDECOR局间TAU功能
通过准则|新局局间TAU过程中，根据老局返回的IMSI判断用户支持eDECOR因老局未返回UE Usage Type，MME向HSS发起AIR获取鉴权向量的同时携带AIR-Flags，其中“Send UE Usage Type“标识位为1并根据获取到的“UE Usage Type”本地解析到DCN-IDTAU Accept消息中中携带DCN-ID
测试结果|-
# ZUF-78-17-014 CN辅助eNodeB参数 
特性描述 :特性描述 :术语 :术语|含义
---|---
CN|核心网，为用户提供连接、对用户进行管理、完成业务承载，提供到外部网络的接口。
MTC|机器类通信，通过蜂窝网络进行数据传输的机器与机器（Machine to Machine，M2M）通信。
RRC|无线资源控制，实现终端和RNC之间的无线连接。
描述 :定义 :核心网辅助无线参数优化机制，可以减少MTC终端可能出现的频繁Connected/Idle之间状态转换所带来的信令开销，同时可以根据不同的MTC终端业务应用，提供差异化的状态转换策略，实现最优网络性能。
背景知识 :NB-IoT物联网具有海量接入的特性，基于NB-IoT物联网技术接入EPC网络的MTC终端，其数量为亿级单位，是智能手机终端的数十甚至上百倍。如此海量的终端，在与无线建立RRC连接时，会占用大量的无线空口资源，导致无线资源紧张。海量接入的MTC终端同时会对网络信令负荷造成冲击，需要在无线侧减少终端的状态切换，从而减少网络对MTC终端的寻呼开销以及移动性管理过程，降低信令负荷。 
引入的核心网辅助无线参数优化机制，可以减少MTC终端可能出现频繁Connected/Idle之间状态转换所带来的信令开销。 
应用场景 :核心网辅助无线参数优化机制：MME根据运营商策略，提供终端签约信息或统计信息给eNodeB，eNodeB根据该信息来优化设置MTC终端Inactive
Timer定时器时长，减少无线侧终端的状态转换，降低信令负荷。 
可为运营商提供差异化的状态转换策略，包括： 
基于IMSI和APN的优先策略。 
基于IMSI的优先策略。 
基于APN的优先策略。 
客户收益 :受益方|受益描述
---|---
运营商|降低信令开销，实现最优网络性能。
终端用户|对终端用户不可见。
实现原理 :系统架构 :图1  系统架构图

涉及的网元 :本功能由MME、HSS、eNodeB配合完成，不涉及其它网元。 
网元名称|网元作用
---|---
MME|根据运营商策略计算出用户的行为信息，并下发给eNodeB。
eNodeB|根据MME下发的用户行为，设置MTC终端Inactive Timer定时器时长，来决定MTC终端在没有数据传输时，何时释放该MTC终端的RRC连接。
HSS|向MME下发用户的Communication Pattern（CP）参数。
协议栈 :图2  Diameter消息

图3  S1AP消息

本网元实现 :当终端注册到PS域后，MME根据运营商策略向eNodeB下发用户行为信息，具体参见[业务流程]。
该机制实现的功能是：由核心网MME根据MTC终端的签约或统计信息，将MTC终端的Expected
UE Behaviour相关信息告知eNodeB，eNodeB根据该信息来优化、设置MTC终端RRC连接释放定时器时长，从而决定MTC终端在没有数据传输时，何时释放该MTC终端的RRC连接。 
图4  核心网辅助无线参数优化机制

业务流程 :Attach流程
图5  Attach流程

UE向MME发起Attach请求。 
MME根据运营商策略，通过Initial Context Setup Request消息给eNodeB下发Expected
UE Behaviour，包含用户Expected Activity Period、Expected Idle Period、Expected
HO Interval以及Source of UE Activity Behaviour Information。 
Source
of UE Activity Behaviour Information：来源于HSS下发的签约信息或MME内部统计的信息。 
TAU流程
图6  TAU流程

UE向MME发起TAU请求。 
MME根据运营商策略，通过Initial Context Setup Request消息给eNodeB下发Expected
UE Behaviour，包含用户Expected Activity Period、Expected Idle Period、Expected
HO Interval以及Source of UE Activity Behaviour Information。 
Source
of UE Activity Behaviour Information：来源于HSS下发的签约信息或MME内部统计的信息。 
Service Request流程
图7  Service Request流程

UE向MME发起Service Request请求。 
MME根据运营商策略，通过Initial Context Setup Request消息给eNodeB下发Expected
UE Behaviour，包含用户Expected Activity Period、Expected Idle Period、Expected
HO Interval以及Source of UE Activity Behaviour Information。 
Source
of UE Activity Behaviour Information：来源于HSS下发的签约信息或MME内部统计的信息。 
HO流程
图8  HO流程

UE向MME发起切换流程。 
MME根据运营商策略，通过Handover Request消息给eNodeB下发Expected UE Behaviour，包含用户Expected
Activity Period、Expected Idle Period、Expected HO Interval以及Source
of UE Activity Behaviour Information。 
Source of UE Activity
Behaviour Information：来源于HSS下发的签约信息或MME内部统计的信息。 
系统影响 :该特性不涉及系统影响。 
应用限制 :该特性不涉及应用限制。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401（General Packet Radio Service (GPRS) enhancementsfor Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access）|4.3.21
3GPP TS 29.272（Mobility Management Entity (MME)and ServingGPRS Support Node (SGSN) related interfaces based on Diameter protocol）|7.3.193
3GPP TS 36.413（S1 Application Protocol (S1AP)）|8.3.1、8.4.2
特性能力 :名称|指标
---|---
基于IMSI和APN的策略|8192（个）
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要开启License，对应的License项目为“MME支持CN辅助无线参数优化功能”（license ID：7105），此项目显示为“支持”，表示MME支持CN辅助无线参数优化功能。
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|-|-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令基于IMSI号段的CN辅助无线参数统计配置ADD CN ASS RAN PARA STATSSHOW CN ASS RAN PARA STATS表2  修改配置项配置项命令新增参数物联网业务配置SET MME IOT CFGMME是否支持CN辅助无线参数优化功能 
动态管理表3  新增动态管理动态管理项命令查询MTC用户动态信息SHOW MTC USER DYNAMIC INFO表4  修改动态管理动态管理项命令新增参数查询MME用户签约信息SHOW MMEUSERSUBAESE-Communication-Pattern 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过配置基于IMSI和APN的策略，可以为不同用户提供差异化的配置策略。 
配置前提 :MME支持CN辅助无线参数优化功能对应的License项为“支持”。 
SET MME IOT CFG命令中的“MME是否支持CN辅助无线参数优化功能”参数设置为“支持”。 
配置过程 :执行命令[ADD CN ASS RAN PARA STATS]，配置基于IMSI和APN、APN、IMSI的策略。
配置实例 :实例场景1：针对IMSI号段为46001以及APN为zte的终端，运营商希望eNodeB能够根据核心网通知的MTC终端的Expected
UE Behaviour相关信息，设置MTC终端RRC连接释放定时器时长，来实现最优网络性能，MTC终端的Expected UE Behaviour信息来源于HSS下发的签约信息。 
命令脚本|解释说明
---|---
ADD CN ASS RAN PARA STATS:IMSI="46001",APN="zte",MMEASSRANPARAPLCY="SUBFIRST";|对于IMSI号段为46001以及APN为zte的终端，设置核心网下发的Expected UE Behaviour信息为签约优先。
调整特性 :本特性暂不涉及调整参数。 
测试用例 :测试项目|Attach流程中给eNodeB下发Expected UE Behaviour信息
---|---
测试目的|验证基于IMSI和APN给eNodeB下发Expected UE Behaviour信息
预置条件|MME支持CN辅助无线参数优化功能对应的License项为“支持”。SET MME IOT CFG命令中的“MME是否支持CN辅助无线参数优化功能”参数设置为“支持”。
测试过程|配置基于IMSI和APN的下发策略为签约优先/统计优先。用户发起IMSI Attach流程。
通过准则|用户Attach成功。MME给eNodeB下发Expected UE Behaviour信息，信息来源于HSS签约信息/MME内部用户统计行为。
测试结果|–
常见问题处理 :无。 
# ZUF-78-17-015 NB跨RAT移动 
特性描述 :特性描述 :描述 :定义 :跨RAT移动是指UE在空闲态跨RAT移动到NB-IoT或移动出NB-IoT时，MME不分离UE，支持UE移动。
背景知识 :由于网络覆盖的问题，物联网NB-IoT终端可能会移动出NB-IoT RAT覆盖区域，进入WB RAT覆盖区域；或者NB-IoT终端从WB RAT覆盖区域移动进入NB-IoT RAT覆盖区域。MME需要支持UE在空闲态下的跨RAT跨局移动，网络需要支持终端在空闲态下的跨RAT移动。 
应用场景 :UE在空闲态跨RAT移动到NB-IoT覆盖区域NB-IoT终端在空闲态下，从WB RAT覆盖区域移动进入NB-IoT RAT覆盖区域，MME提供NB-IoT RAT的TAI list（包括小区），根据UE的签约对每PDN连接进行处理：保持PDN连接。发起PDN去连接，携带重激活请求。发起PDN去连接，不携带重激活请求。 
UE在空闲态跨RAT移动出NB-IoT覆盖区域NB-IoT终端在空闲态下，移动出NB-IoT RAT覆盖区域，进入WB RAT覆盖区域，MME提供WB RAT的TAI list（包括小区），根据UE的签约对每PDN连接进行处理，处理同UE在空闲态跨RAT移动到NB-IoT覆盖区域。 
客户收益 :受益方|受益描述
---|---
运营商|提升用户满意度，满足物联网NB-IoT终端的移动性需求。
物联网终端用户|享受更加优质的网络服务。
实现原理 :系统架构 :物联网NB-IoT终端，在NB-IoT RAT覆盖区域接入NB-IoT RAT，NB-IoT接入网络架构如下图所示。
图1  NB-IoT接入网络架构

NB-IoT终端移动出NB-IoT RAT覆盖区域，接入WB RAT，WB接入网络架构如下图所示。
图2  WB接入网络架构

涉及的网元 :网元名称|网元作用
---|---
UE|物联网终端，在NB-IoT RAT覆盖区域接入NB RAT；移动出NB-IoT RAT覆盖区域，接入WB RAT。
eNodeB|支持NB-IoT终端接入，NB-IoT RAT提供NB-IoT接入方式；WB RAT提供WB接入方式。
MME|NB-IoT终端空闲态下从NB-IoT移入或移出时，MME提供UE所驻留的RAT-type（WB-E-UTRAN or NB-IoT）的TAI list（包括小区），并根据UE的签约对每PDN连接进行处理。
HSS|为NB-IoT终端提供每APN签约的PDN-Connection-Continuity AVP。
本网元实现 :NB-IoT终端空闲态下从NB-IoT移入或移出时，MME提供UE所驻留的RAT-type（WB-E-UTRAN or NB-IoT）的TAI list（包括小区），并根据UE的签约对每PDN连接进行处理。 
业务流程 :UE跨RAT移动，MME处理流程
UE跨RAT移动，MME处理流程包括： 
UE在空闲态跨RAT移动到NB-IoT覆盖区域。 
UE在空闲态跨RAT移出NB-IoT覆盖区域。 
UE在空闲态跨RAT移动到NB-IoT覆盖区域
NB-IoT终端在空闲态下，从WB RAT覆盖区域移动进入NB-IoT RAT覆盖区域，MME提供NB-IoT RAT的TAI list（包括小区）。 
涉及如下流程： 
Tracking Area Update procedure with SGW change 
E-UTRAN Tracking Area Update without SGW Change 
Gn/Gp SGSN to MME Tracking Area Update 
在如上3个TAU流程处理中，如果MME识别RAT type已改变，则MME检测UE每APN签约的PDN-Connection-Continuity AVP： 
MAINTAIN-PDN-CONNECTION (0)：保持PDN连接。 
DISCONNECT-PDN-CONNECTION-WITH-REACTIVATION-REQUEST (1)：发起PDN去连接，携带重激活请求，MME在TAU流程完成后且在S1/RRC接口连接释放前，触发PDN Connection Deactivation procedure，携带ESM cause：#39, "reactivation requested"，对专有承载则携带ESM cause：#37 "EPS QoS not accepted"。 
DISCONNECT-PDN-CONNECTION-WITHOUT-REACTIVATION-REQUEST (2)：发起PDN去连接，不携带重激活请求，MME在TAU流程完成后且在S1/RRC接口连接释放前，触发PDN Connection Deactivation procedure，携带ESM cause：#66 "Requested APN not supported in current RAT and PLMN combination"，对专有承载则携带ESM cause：#37 "EPS QoS not accepted"。 
如果UE所有的PDN都去连接了，且UE不支持"attach without PDN connectivity"，则MME应该detach UE，并指示reattach。 
UE在空闲态跨RAT移动出NB-IoT覆盖区域 
NB-IoT终端在空闲态下，移动出NB-IoT RAT覆盖区域，进入WB RAT覆盖区域，MME提供WB RAT的TAI list（包括小区），根据UE的签约对每PDN连接进行处理，处理同UE在空闲态跨RAT移动到NB-IoT覆盖区域描述。 
系统影响 :本特性仅涉及业务流程的正常处理，对系统几乎无影响。 
应用限制 :该特性基于3GPP R15 2018年9月份版本实现，与MME对接的周边网元支持NB跨RAT移动时需要对齐到该协议版本。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: " General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|4.3.5.1 General4.3.5.3 Tracking Area list management5.3.3.1 Tracking Area Update procedure with Serving GW change5.3.3.2 E-UTRAN Tracking Area Update without SGW Change5.7.1 HSS5.7.2 MMED.3.6 Gn/Gp SGSN to MME Tracking Area Update
3GPP TS 29.272: “Mobility Management Entity (MME) and Serving GPRS Support Node (SGSN) related interfaces based on Diameter protocol”|7.3.214 PDN-Connection-Continuity
特性能力 :支持本地配置2048条IMSI+APN获取“PDN连接连续性”的数据。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|7.19.13|首次发布。
License要求 :该特性需要申请了“MME支持NB跨RAT空闲态移动”的License许可后，运营商才能获得NB跨RAT移动特性的服务。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
-|√|-|-|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :HSS为NB-IoT终端提供每APN签约的PDN-Connection-Continuity AVP。 
一般要求NB-IoT的拥塞门限低于WB的拥塞门限设置。 
O&M相关 :命令 :配置项配置项命令NB跨RAT移动策略SET NB RAT POLICYSHOW NB RAT POLICYNB跨RAT移动配置ADD NB RATSET NB RATDEL NB RATSHOW NB RAT 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软参的变化。 
动态管理该特性不涉及动态管理的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :MME根据UE的号段策略、APN策略、默认策略和HSS签约信息来决策NB跨RAT后的PDN连续性策略，PDN连续性策略共有三种：保留PDN连接、PDN去连接携带Reactive指示、PDN去连接未携带Reactive指示。 
策略配置中，有本功能的开关、优先级配置和全局默认策略。其中，优先级配置的规则如下： 
本地配置优先原则: 获得本地配置（号段/APN）中的PDN连续性策略，取不到则从HSS 签约获取，如果再取不到则会取全局默认策略。 
HSS签约优先原则: 先从HSS获取签约中的PDN连续性策略, 取不到则从本地配置（号段/APN）获取，如果再取不到则会取全局默认策略。 
本地配置中，优先级： 同时配置IMSI+APN > 仅配置APN > 仅配置IMSI。 
配置前提 :MME已开启支持NB跨RAT空闲态移动的License功能。 
配置过程 :使用[SET NB RAT POLICY]命令，打开支持NB跨RAT空闲态移动开关，设置签约和本地配置的优先级，以及全局默认PDN连续性策略。
使用[ADD NB RAT]命令，新增基于号段和APN本地配置的PDN连续性策略。
配置实例 :##### HSS签约优先，有本地配置和全局默认策略 
场景说明
设置HSS签约优先，HSS签约优先原则: 先从HSS获取签约中的PDN连续性策略, 取不到则从本地配置（号段/APN）获取，如果再取不到则会取全局默认策略。 
数据规划
打开NB跨RAT空闲态移动开关，设置为HSS签约优先，全局默认策略为保留PDN连接策略。 
本地配置部分号段为“PDN去连接携带Reactive指示”策略 
本地配置部分APN为“PDN去连接未携带Reactive指示”策略。 
配置步骤
步骤|说明|操作
---|---|---
1|打开NB跨RAT空闲态移动开关，设置为HSS签约优先，全局默认配置为保留PDN连接策略。|SET NB RAT POLICY:SUPNBRATIDLEMV="YES",PDNPRIORITY="SSHSUBSCRIPT",DEFPDNCONTINUNITY="PDNCONN";
2|本地配置部分号段为“PDN去连接携带Reactive指示”策略|ADD NB RAT:IMSI="4601199",PDNCONTINUNITY="PDNDISCONNWITHREA";
3|本地配置部分APN为“PDN去连接未携带Reactive指示”策略|ADD NB RAT:APN="pc3.auto.local",PDNCONTINUNITY="PDNDISCONNWITHNOREA";
4|传送配置|SYNA;
##### 本地配置优先，有本地配置和全局默认策略 
场景说明
设置本地配置优先，本地配置优先原则: 获得本地配置（号段/APN）中的PDN连续性策略，取不到则从HSS 签约获取，如果再取不到则会取全局默认策略。 
数据规划
打开NB跨RAT空闲态移动开关，设置为本地配置优先，全局默认策略为保留PDN连接策略。 
本地配置部分号段和APN为“PDN去连接携带Reactive指示”策略 
配置步骤
步骤|说明|操作
---|---|---
1|打开NB跨RAT空闲态移动开关，设置为本地配置优先，全局默认策略为保留PDN连接策略。|SET NB RAT POLICY:SUPNBRATIDLEMV="YES",PDNPRIORITY="LOCAL",DEFPDNCONTINUNITY="PDNCONN";
2|本地配置部分号段和APN为“PDN去连接携带Reactive指示”策略。|ADD NB RAT:IMSI="460119",APN="pc3.auto.local",PDNCONTINUNITY="PDNDISCONNWITHREA";
3|传送配置。|SYNA;
调整特性 :该特性不涉及调整特性。 
测试用例 :测试项目|MME支持NB-IoT跨RAT空闲态移动性
---|---
测试目的|验证本地优先。
预置条件|1.发生跨RAT TAU流程 （UE在空闲态跨RAT移动到NB-IoT或移动出NB-IoT）。2.MME支持NB跨RAT空闲态移动功能。
测试过程|1.使用SET NB RAT POLICY命令，打开NB-IoT跨RAT空闲态移动开关，配置优先级及默认PDN连续性策略。2.使用ADD NB RAT命令，新增基于号段和APN配置的PDN连续性策略。3.使用SYNA命令，同步数据。
通过准则|终端在空闲态能正常跨RAT移动到NB-IoT或移出NB-IoT网络。
测试结果|–
常见问题处理 :无 
# ZUF-78-17-016 覆盖增强限制 
特性描述 :特性描述 :描述 :定义 :覆盖增强限制功能是指运营商不允许特定终端和无线使用深度覆盖，以达到减少终端的能量损耗。 
通过以下两种方式对终端进行限制： 
终端支持覆盖增强限制功能。MME根据终端的签约信息，可以对终端和eNodeB进行覆盖增强限制。 
CE Mode B的终端，根据UE's usage（终端的指示参数）、在HSS中的签约信息，以及在MME上的配置，来通知eNodeB限制使用CE ModeB的模式。 
背景知识 :物联网终端面对复杂环境下信号覆盖差异问题时，系统通过深度覆盖功能，以便保证地下车库、地下室、地下管道等信号难以到达的地方的信号覆盖，但对于某些终端不需要使用深度覆盖，网络可以关闭使用覆盖增强以减少能量的损耗。比如：某些终端只有上行数据要求时，则可以使用覆盖增强限制功能。 
应用场景 :当某些终端不需要使用深度覆盖，网络可以关闭使用覆盖增强以减少能量的损耗。 
客户收益 :受益方|受益描述
---|---
运营商|通过覆盖增强限制功能，运营商能获得如下收益：节约投资成本 提高用户满意度提高运营成本效益获得新的收入增长点提升无线频谱利用率
移动用户|提升终端用户体验用户享受更稳定和更可靠的网络服务
实现原理 :系统架构 :本特性利用现有网元消息接口，在现有的接口消息中新增参数字段达到目的，对系统架构无改变。 
涉及的网元 :网元名称|网元作用
---|---
MME|接受并保存UE带上的参数并保存。接受HSS的签约信息。通知UE和eNodeB。
eNodeB|接受并使用MME下发的限制参数。
HSS|把用户的限制增强的签约带给MME。
UE|把终端的能力带给MME。
本网元实现 :以下为覆盖增强限制特性涉及的功能点： 
终端能够正常接入系统，在附着和TAU时，把支持覆盖限制的情况以及CE ModeB的模式带给MME。 
MME从HSS得到用户的覆盖增强限制签约信息。 
决策出限制覆盖增强，通知给UE和eNodeB。 
业务流程 :附着过程
附着过程如下图所示。 
图1  附着过程

流程说明： 
UE发起附着，通过eNodeB发附着请求给MME，消息中带上支持覆盖增强限制指示。 
MME发Update Location Request消息给HSS，以期获得UE的签约信息。 
HSS返回用户的签约信息，指示UE签约了覆盖增强限制功能。 
MME在附着接受消息指示UE和eNodeB启动覆盖增强限制功能。 
TAU过程
TAU过程如下图所示。 
图2  TAU过程

流程说明 
UE发起TAU，通过eNodeB发附着请求给MME，消息中带上支持覆盖增强限制指示。 
MME发Update Location Request消息给HSS，以期获得UE的签约信息。 
HSS返回用户的签约信息，指示UE签约了覆盖增强限制功能。 
MME在TAU接受消息指示UE和eNodeB启动覆盖增强限制功能。 
系统影响 :该特性不涉及对系统的影响 
应用限制 :该特性不涉及应用限制 
特性交互 :该特性不涉及与其他特性的交互 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: "GPRS enhancements for E-UTRAN access "|5.3.2节: Attach procedure5.3.3节: Tracking Area Update procedures
3GPP TS 36.413: "Evolved Universal Terrestrial Access Network (E-UTRAN); S1 Application Protocol (S1AP)".|全部
特性能力 :该特性不涉及规格指标 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要申请了“MME支持覆盖增强限制功能”的License许可后，运营商才能获得向MME支持覆盖增强限制功能。 
对其他网元的要求 :UE|eNodeB|SGW|PGW|HSS
---|---|---|---|---
|√|-|-|√
覆盖增强限制特性需要HSS、UE和eNodeB配合完成。 
其中，HSS需要具备把用户签约的覆盖增强限制带给MME；UE把支持覆盖增强限制的指示带给MME，并根据MME的指示限制覆盖增强；eNodeB根据MME的指示限制覆盖增强和CE Mode B。 
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :无 
O&M相关 :命令 :配置项表1  新增配置项配置项命令无线覆盖增强与CE mode B控制开关SET ECOVRESTRIC CTRLSHOW ECOVRESTRIC CTRL无线覆盖增强与CE mode B控制策略配置SET DEFAULT ECOVRESTRICSHOW DEFAULT ECOVRESTRICADD PLMN ECOVRESTRICSET PLMN ECOVRESTRICDEL PLMN ECOVRESTRICSHOW PLMN ECOVRESTRIC 
安全变量该特性不涉及安全变量的变化。 
软件参数该特性不涉及软参的变化。 
动态管理查询用户签约数据命令SHOW MMEUSERSUB，能够查到签约的扩展ARD（Enhanced Coverage Not Allowed）。查询用户动态信息命令SHOW MMEUSERDYN，能够查到UE是否支持CE Mode B（UE network capability中的RestrictEC）。 
性能统计 :该特性不涉及性能统计的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :覆盖增强特性主要包括了覆盖增强限制控制、Voice centric方式的CE mode B控制、Data centric的方式CE mode B控制。 
覆盖增强限制控制UE在附着和TAU时，在消息中指示支持覆盖增强限制功能，MME根据HSS的签约和本地策略（根据PLMN配置），指示UE和eNB是否需要限制覆盖增强。 
Voice centric方式的CE mode B控制在附着请求和TAU请求中，如果eNB通知MME  UE支持CE mode B，并且UE's usage 设置为"voice centric"，MME需要通知eNB 的CE mode B需要限制。 
Data centric方式的CE mode B控制在附着请求和TAU请求中，如果UE支持CE mode B，并且UE's usage 设置为"data centric"，对于本地用户，MME需要根据用户的签约信息来通知eNB是否需要限制UE的CE mode B；对于漫游用户，MME需要结合HSS的签约和本地策略来通知eNB是否需要限制UE的CE mode B。 
配置前提 :MME支持覆盖增强限制功能的License项已支持。 
配置过程 :##### 覆盖增强限制配置过程 
打开覆盖增强限制功能开关。 
配置覆盖增强限制默认本地策略与优先级。 
配置基于PLMN覆盖增强限制本地策略与优先级。 
##### CE mode B 限制配置过程 
打开CE mode B控制功能开关。 
配置CE mode B限制默认本地策略与优先级。 
配置基于PLMN的CE mode B限制本地策略与优先级。 
配置实例 :##### 实例 1 
场景说明
MME配置支持覆盖增强限制功能，默认策略优先级为本地优先，本地控制策略为不限制。增加46011 PLMN控制策略，优先级为HSS签约优先，本地控制策略为限制。 
配置步骤
根据规划，进行如下配置： 
说明|操作
---|---
配置MME支持覆盖增强限制。|SET ECOVRESTRIC CTRL:ENHCOVCTRL="YES";
配置MME支持覆盖增强限制默认策略，优先级为本地优先，本地限制策略为不限制。|SET DEFAULT ECOVRESTRIC:ENHCOVPRIORITY="LOCAL",ENHCOVLOCALPOLICY="NO";
配置基于PLMN的覆盖增强限制策略，优先级为HSS签约优先，本地限制策略为限制。|ADD PLMN ECOVRESTRIC:PLMN="460"-"11",ENHCOVPRIORITY="HSSSUBSCRIPT",ENHCOVLOCALPOLICY="YES";
##### 实例 2 
场景说明
MME配置支持CE Mode B限制功能，CE Mode B限制默认策略优先级为本地优先，本地控制策略为不限制。增加46011 PLMN控制的CE Mode B限制策略，优先级为HSS签约优先，本地控制策略为限制。 
配置步骤
根据规划，进行如下配置： 
说明|操作
---|---
配置MME支持CE Mode B限制。|SET ECOVRESTRIC CTRL:CEMODEBCTRL="YES";
配置MME支持CE Mode B限制默认策略，优先级为本地优先，本地限制策略为不限制。|SET DEFAULT ECOVRESTRIC:CEMODEBPRIORITY="LOCAL",CEMODEBLOCALPOLICY="NO";
配置基于PLMN的CE Mode B限制策略，优先级为HSS签约优先，本地限制策略为限制。|ADD PLMN ECOVRESTRIC:PLMN="460"-"11",CEMODEBPRIORITY="HSSSUBSCRIPT",CEMODEBLOCALPOLICY="YES";
调整特性 :无。 
测试用例 :测试项目|MME支持覆盖增强限制
---|---
测试目的|MME能够根据本地配置、签约来决策是否增强覆盖限制。
预置条件|MME支持覆盖增强限制功能开关打开。配置默认覆盖增强限制策略优先级为本地优先，默认本地限制策略为限制。配置基于PLMN（46011）的覆盖增强限制策略，优先级为HSS签约优先，本地限制策略为不限制。46011XXXXXXXXXX的用户签约的覆盖增强限制为“不限制”。
测试过程|号段46011的用户发起正常的附着流程。非号段46011的用户发起正常的附着流程。
通过准则|46011的用户，在attach accept中携带覆盖增强限制为"不限制"，在initial context setup request不填写限制参数。非46011的用户，在attach accept中携带覆盖增强限制为"限制"，在initial context setup request填写限制参数。
测试结果|–
测试项目|MME支持CE mode B限制
---|---
测试目的|Voice centric方式的CE mode B控制。
预置条件|MME支持CE mode B限制功能开关打开。配置默认CE mode B限制策略优先级为本地优先，默认本地限制策略为限制。配置基于PLMN（46011）的CE mode B限制策略，优先级为HSS签约优先，本地限制策略为不限制。46011XXXXXXXXXX的用户签约的CE mode B限制为“不限制”。
测试过程|46011用户UE发起附着，请求中带CE mode B，并且UE's usage 设置为"voice centric"。非46011用户UE发起附着，请求中带CE mode B，并且UE's usage 设置为"voice centric"
通过准则|46011的用户、非46011的用户在消息INITIAL CONTEXT SETUP REQUEST中携带CE mode B限制的参数。
测试结果|–
测试项目|MME支持CE mode B限制
---|---
测试目的|Data centric方式的CE mode B控制。
预置条件|MME支持CE mode B限制功能开关打开。配置默认CE mode B限制策略优先级为本地优先，默认本地限制策略为限制。配置基于PLMN（46011）的CE mode B限制策略，优先级为HSS签约优先，本地限制策略为不限制。46011XXXXXXXXXX的用户签约的CE mode B限制为“不限制”。
测试过程|46011用户UE发起附着，请求中带CE mode B，并且UE's usage 设置为"data centric"，签约覆盖增强的ARD，签约不限制。非46011用户UE发起附着，请求中带CE mode B，并且UE's usage 设置为"data centric"，签约覆盖增强的ARD，签约不限制。
通过准则|46011的用户在消息INITIAL CONTEXT SETUP REQUEST中不携带CE mode B限制的参数。非46011的用户在消息INITIAL CONTEXT SETUP REQUEST中携带CE mode B限制的参数。
测试结果|–
常见问题处理 :无。 
# ZUF-78-17-017 SCEF连接 
特性描述 :特性描述 :术语 :术语|含义
---|---
能力开放|传统的移动运营商和第三方业务提供商合作，双方可以签订能力开放业务合作协议，由运营商提供网络能力开放功能，第三方借助开放的网络能力接入网络，便捷地使用移动网络的某些基础业务和能力，运营商基于业务合作协议，对第三方执行能力开放接入鉴权及能力使用授权，并提供网络能力开放业务。
描述 :定义 :SCEF连接是指MME启动用户状态检测，检测到用户相应的订阅事件，直接与SCEF网元建立连接，发送对应的用户移动状态事件上报给SCEF网元。
背景知识 :为满足网络能力开放应用场景需求，尤其是物联网应用需求，在移动网络中引入网络能力开放平台和业务能力开放功能（SCEF），实现第三方应用的认证授权、计费和与网络侧网元的信息交互、信息隐藏以及封装调用。通过SCEF，能够安全地向第三方开放服务与网络能力。即SCEF是基于电信网络，面向合作方业务平台开放移动网络能力的设备。 
应用场景 :物联网终端往往有事件监控的需求，例如： 
对处于节电状态的物联网终端下发数据，需要监控其移动连接状态。 
跟踪终端位置，做业务应用的场景（如摩拜单车），需要监控其位置信息。 
第三方应用需要进行终端状态维护，如无线传感器维护（故障事件上报），需要监控其通信状态。 
因此MME支持如下用户能力开放事件监控： 
移动连接状态：包括失去连接订阅/上报、终端可及订阅/上报和DDN失败后可达订阅/上报 
物联网终端尤其是低移动的NB终端，常处于节电状态。当第三方应用需要和终端交互，下发数据时，需要通过能力开放平台和SCEF先订阅终端UE的失去连接状态；如果MME通知SCEF UE失去连接，后续应用继续订阅UE是否可达的状态；或者第三方应用先下发下行用户数据失败，再通过能力开放平台和SCEF订阅终端UE DDN失败后可达状态。 
SCEF通过HSS向MME下发终端失去连接订阅请求，MME检测到UE失去连接，向SCEF发送终端失去连接上报。SCEF通过能力开放平台通知第三方应用，用户失去连接，此时第三方应用不再下发用户数据。 
SCEF通过HSS向MME下发终端可及订阅请求，MME检测到终端UE可达时，向SCEF发送终端可及上报。SCEF通过能力开放平台通知第三方应用，用户可达，可以下发下行数据了。 
SCEF通过HSS向MME下发终端可及订阅请求，MME检测到终端DDN失败后状态变为可达时，向SCEF发送DDN失败后可达上报。SCEF通过能力开放平台通知第三方应用终端DDN失败后可达。 
位置信息：位置订阅/上报 
物网和人网的终端都要位置跟踪的需求，如移动单车，学生携带的终端等。当第三方应用需要获得终端的位置信息时，需要通过能力开放平台和SCEF订阅终端UE的位置。SCEF通过HSS向MME下发终端可及订阅请求，MME检测到UE位置改变时，向SCEF发送位置上报。SCEF通过能力开放平台通知第三方应用用户位置。 
通信状态：通信失败订阅/上报 
第三方应用需要进行终端状态维护，如无线传感器维护（故障事件上报）等，通过能力开放平台和SCEF先订阅终端UE通信失败。SCEF通过HSS向MME下发终端可及订阅请求，MME检测到和无线及终端通信失败时，向SCEF发送位置上报。SCEF通过能力开放平台通知第三方应用用户通信失败。 
客户收益 :受益方|受益描述
---|---
运营商|与第三方业务提供商进行能力开放业务合作，增加营收，打造共赢的局面。提升用户满意度，满足物联网终端的多样需求。
移动用户|享受更加优质的网络服务。
实现原理 :系统架构 :SCEF通过向3GPP网元订阅能力开放事件，获得相应的能力开放信息。3GPP网络架构如下图所示。 
图1  能力开放3GPP网络架构

涉及的网元 :网元名称|网元作用
---|---
UE|物联网终端或人网终端，通过eNodeB接入网络。
eNodeB|支持NB-IoT终端接入，NB-IoT RAT提供NB-IoT接入方式；WB RAT提供WB接入方式。
MME|SCEF通过HSS向MME订阅如下用户状态信息，MME检测到上面相应的订阅事件，发送对应的事件报告给SCEF。MME和SCEF间建立Diameter链路连接和会话。
HSS|HSS接收SCEF的用户状态事件订阅，根据订阅的事件类型，或者本地启动事件监测，检测到相应的订阅事件，发送对应的事件报告给SCEF。或者通知MME用户状态事件订阅。HSS和SCEF间建立Diameter链路连接和会话。
SCEF|第三方应用通过能力开放平台和SCEF订阅终端UE移动状态信息。SCEF网元通过HSS向MME订阅用户移动状态信息，MME启动用户状态检测，检测到用户相应的订阅事件，就发送对应的用户移动状态事件上报给SCEF。SCEF通过能力开放平台上报第三方应用。
协议栈 :其中MME和SCEF之间是T6a接口，Diameter协议栈。 
图2  T6a接口协议栈

本网元实现 :SCEF通过HSS向MME订阅如下用户状态信息，MME检测到上面相应的订阅事件，发送对应的事件报告给SCEF。MME和SCEF间建立Diameter链路连接和会话。 
MME支持如下SCEF用户移动状态订阅和上报： 
失去连接订阅/上报 
终端可及订阅/上报 
位置订阅/上报 
通信失败订阅/上报 
DDN失败后可达订阅/上报 
##### 公共订阅/上报流程 
订阅流程
订阅业务流程如下图所示。 
SCS/AS发送Monitoring Request给SCEF，消息中包含：External Identifier(s)或MSISDN(s)或External Group ID、SCS/AS Identifier、SCS/AS Reference ID、Monitoring Type、Maximum Number of Reports、Monitoring Duration、Monitoring Destination Address、SCS/AS Reference ID for Deletion、Group Reporting Guard Time。 
如果SCS/AS想订阅一组用户的事件监控，则Monitoring Request消息中携带External Group Identifier and Group Reporting Guard Time。如果External Group Identifier有效，则SCEF应忽略参数External Identifier(s)和MSISDN(s)。 
SCEF同时收到SCS/AS的多个Monitoring Requests，SCEF根据本地优先级策略进行处理，包括过负荷情况下的处理优先级。 
SCS/AS和SCEF间采用API接口。 
SCEF收到Monitoring Request，保存参数SCS/AS Reference ID、SCS/AS Identifier、Monitoring Destination Address、Monitoring Duration、Maximum Number of Reports and Group Reporting Guard Time。SCEF分配SCEF Reference ID，用于关联SCEF上下文信息、关联事件监控上报或特定事件监控删除。 
基于运营商的策略（SCEF本地控制策略），如果SCS/AS没有被授权执行此事件监控，或SLA控制，或Monitoring Request消息检测不合法，或SCS/AS已超过了配额或订阅率，则SCEF执行步骤9，发送Monitoring Response给SCS/AS，携带失败原因。 
如果SCEF收到SCS/AS Reference ID for Deletion，SCEF检索到关联的SCEF Reference ID，删除对应的事件监控。 
Group Reporting Guard Time是可选参数，指示当Group Reporting Guard Time超时时，SCEF将组内用户的所有事件监控上报集合打包发送给SCS/AS。 
SCEF发送Monitoring Request给HSS订阅在HSS和MME上指定的事件监控，消息中携带参数包括：External Identifier或MSISDN或External Group Identifier、SCEF ID、SCEF Reference ID、Monitoring Type、Maximum Number of Reports、Monitoring Duration、SCEF Reference ID for Deletion、Chargeable Party Identifier、Group Reporting Guard Time。 
如果External Group Identifier有效，则SCEF应忽略参数External Identifier(s)和MSISDN(s)。对一次性的UE漫游状态事件监控，SCEF不指示Group Reporting Guard Time。 
HSS收到Monitoring Request，检查用户标识External Identifier或MSISDN或External Group Identifier标识的数据在HSS是否存在，如果不存在，则HSS执行步骤8，发送Monitoring Response给SCEF，携带失败原因DIAMETER_ERROR_USER_UNKNOWN。 
HSS检查SCEF是否有权限请求的事件监控，如果没有权限，则HSS执行步骤8，发送Monitoring Response给SCEF，携带失败原因DIAMETER_ERROR_UNAUTHORIZED_REQUESTING_ENTITY。 
HSS检查UE是否授权了请求的监控事件，如果没有权限，则HSS执行步骤8，发送Monitoring Response给SCEF，携带失败原因DIAMETER_ERROR_UNAUTHORIZED_SERVICE。 
HSS检查服务MME是否支持请求的监控事件或组监控事件、或监控事件参数在运营商允可范围、或需要删除的监控事件有效，检查失败HSS执行步骤8，发送Monitoring Response给SCEF，携带失败原因。HSS还可以鉴权收费方确定的收费方标识。 
HSS保存参数SCEF Reference ID、SCEF ID、Maximum Number of Reports、Monitoring Duration和SCEF Reference ID for Deletion。对于UE组事件监控，HSS为组内每个UE保存这些参数。 
当Group Reporting Guard Time超时时，HSS将组内用户的所有事件监控上报集合打包发送给SCEF。 
一个用户可以在HSS签约一个或多个External Group Identifier，External Group Identifier中的Local Identifier用于获取一个IMSI-Group Identifier。当External Group Identifier用于通信模式设置、事件监控或删除时，HSS解析External Group Identifier到一个IMSI-Group Identifier。 
4a. 对于UE组事件监控，HSS立即发送Monitoring Response (SCEF Reference ID、Cause) 给SCEF确认接受UE组事件监控，然后开始组内各UE的事件监控处理。HSS删除SCEF Reference ID for Deletion指示的事件监控。 
4b. SCEF给SCS/AS回复Monitoring Response，指示组事件监控处理中。 
HSS检查通过，发送Insert Subscriber Data Request给MME，消息中携带参数包括：Monitoring Type、SCEF ID、SCEF Reference ID、Maximum Number of Reports、Monitoring Duration、SCEF Reference ID for Deletion、Chargeable Party Identifier。 
对于UE组事件监控，HSS对组内每个UE发送一条Insert Subscriber Data Request到服务于UE组的所有MME，每条消息中携带External ID 或MSISDN。 
MME检查请求，检查Monitoring Type是否支持（包括漫游非漫游情况），检查需要删除的监控事件是否有效，如果检查失败HSS执行步骤7，发送Insert Subscriber Data Answer，携带失败原因。过负荷或SLA控制也可能导致失败，后续处理一样。 
MME检查成功，保存收到的参数，开始检测订阅的监控事件。 
如果MME收到SCEF Reference ID for Deletion，则MME检索到关联的监控事件，删除对应的事件监控。 
MME改变时，老局MME需要把事件监控参数作为上下文信息的一部分，传送给新局MME/SGSN。 
MME处理成功，发送Insert Subscriber Data Answer给HSS.如果在发送Insert Subscriber Data Answer 时MME检测到请求的监控事件可用，则在Answer 中携带Monitoring Event Report。 
对单个UE的事件监控，HSS发送Monitoring Response给SCEF确认接受事件监控请求和监控事件删除指示，消息携带参数(SCEF Reference ID、Cause)。如果在发送Monitoring Response时HSS检测到请求的监控事件可用，则在Monitoring Response中携带Monitoring Event Report。 
如果是一次性的事件监控并且Insert Subs  criber Data Answer中包含Monitoring Event Report，则HSS删除UE相关的事件监控订阅，对于UE组则删除组内单个UE相关的事件监控订阅。 
UE组事件监控，如果HSS在4a步已发送Monitoring Response，Group Reporting Guard Time有效，则在Group Reporting Guard Time时间内HSS累计多个UE Monitoring Response，当Group Reporting Guard Time超时时，HSS发送Monitoring Indication，携带多个Monitoring Response，由于消息最大长度的限制，Monitoring Indications可以分为多个消息发送，因此消息中会指示是UE组的中间的消息或最后一个消息。如果UE组内有成员的事件监控失败，则HSS在相应的Monitoring Response中携带UE identity和Cause。 
UE移动到新局，HSS要判断是否新局MME支持请求的事件监控。 
对单个UE，SCEF发送Monitoring Response给SCS/AS，携带参数(SCS/AS Reference ID、Cause)。如果Monitoring Event Report存在，则Monitoring Event Report包含在Monitoring Response中。 
对一次性的单个UE的事件监控并且Monitoring Response中包含Monitoring Event Report，则SCEF删除UE相关的事件监控订阅。 
对UE组事件监控，SCEF收到HSS的Monitor Indication且指示最后一个消息时，发送Monitor Indication给SCS/AS。或者Group Reporting Guard Time有效，在Group Reporting Guard Time时间内SCEF累计多个UE Monitoring Response，当Group Reporting Guard Time超时时，SCEF发送Monitoring Indication，携带多个Monitoring Response。 
如果HSS检测serving MME不支持请求的监控事件，如UE移动引发，则通知SCEF挂起UE事件监控订阅。SCEF认为网络暂时不能订阅UE事件监控，如下情况导致：由于UE移动UE的MME发生改变，并且新局MME支持挂起的监控事件，HSS应该在订阅新局MME订阅事件监控，并通知SCEF恢复挂起的监控事件。当监控事件被挂起后，Monitoring Duration截止到期，HSS和SCEF应各自删除挂起的监控事件。 
上报流程
上报流程如下图所示。 
MME (1a)或HSS (1b)检测到一个订阅的监控事件。 
MME与SCEF交互。 

MME发送Monitoring Indication给SCEF，消息携带参数SCEF Reference ID、Monitoring Event Report、User Identity。如果是一次性事件监控请求，则MME发送Monitoring Indication的同时删除此监控事件订阅；如果该监控事件Maximum Number of Reports有效，则MME对Maximum Number of Reports-1；如果监控事件订阅包括用户标识User Identity，则MME发送Monitoring Indication包括User Identity。 
HSS发送Monitoring Indication给SCEF，消息携带参数SCEF Reference ID and Monitoring Event Report。如果是一次性事件监控请求，则HSS发送Monitoring Indication的同时删除此单用户或此用户组的监控事件订阅。如果该监控事件Maximum Number of Reports有效，则HSS对Maximum Number of Reports-1。如果Group Reporting Guard Time有效，则HSS在Group Reporting Guard Time内收集组内UE的监控事件，当Group Reporting Guard Time超时时，HSS发送Monitoring Indication给SCEF，消息携带参数SCEF Reference ID、Monitoring Event Report Set、External Group ID、External ID(s)或MSISDN(s)。 
UE组事件监控订阅，由于消息尺寸限制，HSS可以将收集的组监控事件报告拆分成多个Monitoring indication消息。 
SCEF使用SCEF Reference ID获得关联的SCS/AS Reference ID连同Monitoring Destination Address，如果Monitoring Destination Address无效，则使用之前发送订阅请求的SCS/AS地址作为目的地址，发送Monitoring Indication给SCS/AS，消息携带参数(SCS/AS Reference ID、External ID或MSISDN、Monitoring Information)。如果SCS/AS Reference ID是为组事件监控订阅分配，SCEF发送Monitoring Indication 给SCS/AS，消息携带参数(SCS/AS Reference ID、External Group Identifier、External ID(s)或MSISDN(s)、Monitoring Information)，其中External ID(s)或MSISDN(s)来自Monitoring Event reporting。如果Group Reporting Guard Time有效且来自事件监控订阅，SCEF在Group Reporting Guard Time内收集组内UE的监控事件，当Group Reporting Guard Time超时时，SCEF发送Monitoring Indication给SCS/AS。 
当单UE的监控订阅请求的事件报告达到maximum number of reports，SCEF请求HSS（通过HSS订阅）或MME（直接在MME订阅）删除相应的监控事件订阅。 如果通过HSS进行一次性事件监控订阅，MME上报监控事件报告给HSS，则SCEF请求HSS删除相关的事件监控订阅，HSS通知MME删除关联的事件监控订阅。 
##### 失去连接订阅/上报流程 
3GPP网络检测到UE信令或用户面不可达，MME判断移动可达定时器超时则认为UE失去连接。 
SCS/AS可以提供一个Maximum Detection Time，指示SCS/AS和UE无通信的最大周期时间，在此周期时间后SCS/AS被通知UE不可达。 
由于失去连接的Maximum Detection Time确定了周期性更新定时器的数量级，因此网络侧应该确保这个Maximum Detection Time，从而UE的周期TAU/RAU时长保持高于UE节电和网络的信令负荷管理的下限值。所以受UE电池的限制，Maximum Detection Time不应该是一个小的时间（如仅几分钟的粒度）。即使没有UE电池的限制，由于此特性信令成本，失去连接的Maximum Detection Time为几分钟的粒度也仅适用于数量有限的UE。 
订阅流程
SCS/AS设置Monitoring Type为"Loss of Connectivity"，可选的添加Maximum Detection Time，然后发送Monitoring Request给SCEF。 
SCEF处理同公共订阅流程步骤2和步骤3。 
HSS处理同公共订阅流程步骤4。此外，Maximum Detection Time有效，则HSS检查Maximum Detection Time是否在运用商规定的范围，如果可接受则HSS使用Maximum Detection Time设置用户签约周期性RAU/TAU时长。如果Maximum Detection Time不可接受、则HSS拒绝Monitoring Request。如果之前同一用户被另一个SCEF Reference ID标识另一个Monitoring Request设定了签约周期性RAU/TAU时长，则根据运营商的策略，HSS可以拒绝Monitoring Request携带失败原因，或接受Monitoring Request。如果HSS接受这个Monitoring Request，则他应取消先前接受的Monitoring Request。 
因为移动可达定时器的值大于周期性RAU/TAU时长（默认4分钟），所以HSS可以设置签约周期性RAU/TAU时长小于Maximum Detection Time。 
HSS处理同公共订阅流程步骤5。此外HSS包括签约周期性RAU/TAU时长 (如果时长改变)。 
MME处理同公共订阅流程步骤6。如果MME从HSS收到签约周期性TAU时长，MME分配为UE分配此周期性TAU时长。MME开始检测移动可达定时器时长是否到达。 
其他同公共订阅流程步骤7-9的处理。 
上报流程
同公共上报流程步骤1a，当mobile reachability timer超时，MME检测到“失去连接”事件。 
同公共上报流程步骤2a。 
同公共上报流程步骤3。 
##### 终端可及订阅/上报业务流程 
“终端可及”指示当UE因短消息或下行数据变为可达，当UE状态变为是ECM_CONNECTED（UE使用PSM或eDRX）或UE因为寻呼变可达（UE使用eDRX）。此监控事件支持短消息可达和数据可达。短消息可达仅用于一次性Monitoring Request。SCS/AS可以再发给SCEF的Monitoring Event configuration request中包含如下参数： 
可达类型"Reachability for SMS"或"Reachability for Data"或both。 
“Maximum Latency”可选，指示下行数据传送可接受的最大延迟。此参数用于设置UE的周期性TAU/RAU时长，作为其最大周期，Maximum Latency之后UE已再次连接到网络变为可达。运营商确定可以去活PSM的Maximum Latency下限值。 
“Maximum Response Time”可选，指示UE保持可达允许SCS/AS可靠的传输所需的下行数据的时间。此参数用于设置UE的Active Time。当UE使用eDRX时，Maximum Response Time用于确定在下次寻呼发生之前，此监控事件应该多早上报给SCS/AS。 
“Suggested number of downlink packets”可选，指示当UE不可达时SGW应该缓存的下行包数。 
由于Maximum Latency确定了周期性更新定时器的数量级，因此网络侧应该确保这个Maximum Latency，从而UE的周期TAU/RAU时长保持高于UE节电和网络的信令负荷管理的下限值。所以受UE电池的限制，Maximum Latency不应该是一个小的时间（如仅几分钟的粒度）。即使没有UE电池的限制，由于此特性信令成本， Maximum Latency为几分钟的粒度也仅适用于数量有限的UE。Maximum Latency取值范围是1分钟到多小时。 
订阅流程
SCS/AS设置Monitoring Type为"UE Reachability"，并包括Reachability Type、optionally Maximum Latency和optionally Maximum Response Time，发送Monitoring Request给SCEF。 
SCEF处理同公共订阅流程步骤2。此外，Maximum Latency和Maximum Response Time有效，SCEF检查Maximum Latency和Maximum Response Time是否在运用商规定的范围，如果不在运营商可接受范围，则SCEF执行订阅流程步骤9拒绝Monitoring Request携带失败原因。 
可达类型是"Reachability for SMS"，SCEF向HSS订阅，同公共订阅流程步骤3，当HSS获知UE可达时通知SCEF。HSS执行UE Reachability Notification Request流程获取UE激活通知，该流程在TS 23.401描述。 
可达类型是" Reachability for Data "，SCEF执行公共订阅流程步骤3。此外SCEF通知HSS Maximum Latency和Maximum Response Time。 
HSS执行公共订阅流程步骤4。此外，如果请求被接受且Maximum Latency有效，则HSS设置签约的周期性RAU/TAU定时器时长为Maximum Latency。如果请求的Maximum Latency时长不可接受，则HSS拒绝Monitoring Request。如果之前同一用户被另一个SCEF Reference ID标识另一个Monitoring Request设定了签约周期性RAU/TAU时长，则根据运营商的策略，HSS可以执行订阅流程步骤8拒绝Monitoring Request携带失败原因，或接受Monitoring Request。如果HSS接受这个Monitoring Request，则他应取消先前接受的Monitoring Request。 
HSS执行公共订阅流程步骤5。此外，HSS包括签约周期性RAU/TAU时长 (如果时长改变)、Maximum Response Time（如果有效）。 
MME处理同公共订阅流程步骤6，并且开始检测UE是否进入连接态。在后续的每个TAU流程中，MME使用签约的周期性TAU定时器。 
其他同公共订阅流程步骤7-9的处理。 
上报流程
处理同公共上报流程步骤1a和步骤1b，当UE变为连接态（UE使用PSM或eDRX），或当UE变为寻呼可达（UE使用eDRX），MME检测到“终端可及”事件。 
如果Maximum Response Time有效，则MME保持UE相应的S1-U连接时长少于PSM Active Timer，至少是Maximum Response Time。如果UE使用eDRX，则MME决策在下一次寻呼发生前，何时报告“终端可及”事件时要考虑Maximum Response Time。 
处理同公共上报流程步骤2a和步骤2b。 
处理同公共上报流程步骤3。 
##### 位置订阅/上报业务流程 
“位置上报”监控事件允许SCS/AS请求获取UE当前位置或最近一次获知位置。支持的位置精度可以使CGI/ECGI级、eNodeB级或TA/RA级。最近一次获知的位置监控仅支持一次性上报。目前的位置监控支持一次或持续的位置上报。对持续的位置上报，MME每次检测到UE位置改变即上报一次请求精度的位置上报。 
由于信令负荷潜在增加，推荐小区级的当前位置的持续监控仅应用于有限数量的用户。 
订阅流程 
SCS/AS设置Monitoring Type为"Location Reporting"，并且添加Location Type和可选精度，然后发送Monitoring Request给SCEF。 
Location Type指示请求“Current Location”或“Last Known Location”。Accuracy参数指示请求位置信息的期望精度。 
Accuracy可能是cell level (CGI/ECGI)、eNodeB级、TA/RA级或其他格式，例如街道、地区等。 
SCEF处理同公共订阅流程步骤2。 
Accuracy有效，SCEF根据运营商的配置映射Accuracy到可允许的精度cell level (CGI/ECGI)、eNodeB级、TA/RA级。Accuracy无效，SCEF根据运营商配置设置精度。SCEF发送Monitoring Request给HSS，同公共订阅流程步骤3，携带Location Type 和Accuracy。 
HSS处理同公共订阅流程步骤4。 
依据Location Type，HSS设置"Current Location Request"同TS 29.272协议，发送Insert Subscriber Data Request给MME，同公共订阅流程步骤5，携带Accuracy。 
MME处理同公共订阅流程步骤6，根据请求的Accuracy获取位置信息。除了一次性请求，MME依据Accuracy开始检测cell/TA/eNodeB改变。 
同公共订阅流程步骤7-9的处理，包括当前或最近一次位置上报。SCEF映射eNodeB-ID/cell-ID/TAI为地理位置，然后上报SCS/AS。 
上报流程
处理同公共上报流程步骤1a，MME检测到要求精度的UE位置改变。 
处理同公共上报流程步骤2a。 
处理同公共上报流程步骤3。SCEF映射cell level (CGI/ECGI)、eNodeB、TA为地理位置，上报SCS/AS。 
##### 通信失败订阅/上报业务流程 
“通信失败”监控事件允许SCS/AS被通知RAN/NAS释放原因码（TS 23.401）标识的通信失败事件。 
订阅流程
SCS/AS设置Monitoring Type为"Communication Failure"，然后发送Monitoring Request给SCEF。 
SCEF处理同公共订阅流程步骤2。 
SCEF处理同公共订阅流程步骤3。 
HSS处理同公共订阅流程步骤4。 
HSS处理同公共订阅流程步骤5。 
MME处理同公共订阅流程步骤6并且开始检测通信失败事件。 
其他同公共订阅流程步骤7-9的处理。 
上报流程
处理同公共上报流程步骤1a，MME检测到RAN或NAS失败事件。 
处理同公共上报流程步骤2a。 
处理同公共上报流程步骤3。基于运营商的配置，SCEF上报收到的failure cause code(s) as-is或失败原因。 
##### DDN失败后可达订阅/上报业务流程 
“DDN失败后可达”监控事件允许SCS/AS被通知在DDN失败后UE可达。 
订阅流程
1. SCS/AS设置Monitoring Type为"Availability after DDN Failure"，然后发送Monitoring Request给SCEF。 
2. SCEF处理同公共订阅流程步骤2。 
3. SCEF处理同公共订阅流程步骤3，此外不需要考虑Max Number of Reports，此事件上报后，SCS/AS即刻删除它。 
4. 其他处理同公共订阅流程步骤4-5处理。 
5. MME处理处理同公共订阅流程步骤6并且开始检测DDN失败后可达事件。 
6. 其他处理同公共订阅流程步骤7-9的处理。 
上报流程
处理同公共上报流程步骤1a，MME检测到DDN失败后UE可达。 
处理同公共上报流程步骤2a。 
处理同公共上报流程步骤3。 
系统影响 :能力开放存在集中订阅的场景，如某区域的所有终端位置订阅，对MME网元系统性能影响较大。为了避免对现网网元的冲击： 
对批量集中订阅，需要各网元逐级进行限速，如：SCEF限速发送订阅事件到HSS，HSS限速发送订阅事件到MME。 
多个应用平台同时或先后对同一个UE进行同一事件订阅，SCEF具备整合能力，如果订阅内容一致，避免多次在南向给3GPP网元下发订阅，不增加3GPP网元信令负荷；如果订阅内容有不同，才更新南向网元订阅。 
MME网元启动CPU过负荷控制。 
应用限制 :该特性基于3GPP R15 2018年9月份版本实现，与MME对接的周边网元支持能力开放时需要对齐到该协议版本。 
特性交互 :该特性不涉及与其他特性的交互。 
遵循标准 :标准名称|章节
---|---
3GPP TS 23.401: " General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access"|4.3.26 Support for Monitoring Events5.3.2.1 E-UTRAN Initial Attach5.3.3 Tracking Area Update procedures5.3.4 Service Request procedures5.3.4B Data Transport in Control Plane CIoT EPS Optimisation5.7.1 HSS5.7.2 MME
3GPP TS 23.682: Architecture enhancements to facilitate communications with packet data networks and applications|4.2 Architectural Reference Model4.3.3.6 T6a/T6b Reference Point Requirements4.3.3.7 S6t Reference Point Requirements5.6 Monitoring Procedures
3GPP TS 29274: Evolved General Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C)|8.120 Monitoring Event Information
特性能力 :MME最大支持1024个SCEF邻接局。 
可获得性 :版本要求及变更记录 :特性版本|发布版本|发布说明
---|---|---
01|V7.19.13|首次发布。
License要求 :该特性需要申请了License许可后，运营商才能获得该特性的服务。 
该特性需要申请了“MME支持事件监控”的License许可后，运营商才能获得向MME订阅用户状态的服务。 
对其他网元的要求 :UE|eNodeB|MME|HSS|SCEF
---|---|---|---|---
√|√|√|√|√
 说明： 
表中“√”表示本功能对网元有要求，“-”表示本功能对网元无要求。 
工程规划要求 :现网部署SCEF网元，和能力开放平台API接口连接，和HSS/MME网元建立Diameter链路。 
O&M相关 :命令 :配置项表1  新增配置项配置项命令MME事件监控策略配置SET MMEEVMONIPOLYSHOW MMEEVMONIPOLYDiameter SCEF配置ADD DIASCEFSET DIASCEFDEL DIASCEFSHOW DIASCEF 
安全变量该特性不涉及安全变量的变化。 
软件参数·该特性不涉及软件参数的变化。 
性能统计 :该特性不涉及计数器的变化。 
告警和通知 :该特性不涉及告警/通知消息的变化。 
业务观察/失败观察 :该特性不涉及业务观察/失败观察的变化。 
话单与计费 :该特性不涉及话单与计费的变化。 
特性配置 :特性配置 :配置说明 :通过SCEF连接特性相关配置，实现MME与SCEF网元的对接，支持对SCEF网元订阅的事件进行监控上报。 
配置前提 :MME已和HSS等网元对接，HSS能够将SCEF订阅的事件下发给MME。 
配置过程 :MME支持事件监控及解除事件监控。 
配置实例 :场景说明 :MME支持和SCEF对接。 
数据规划 :网元|地址|端口|主机名|域名
---|---|---|---|---
MME|192.10.100.75|48901|MME主机名|MME域名
SCEF|192.10.61.1|48901|SCEF-3601.ZTE.COM.CN|ZTE.COM.CN
配置步骤 :步骤|操作|说明
---|---|---
1|SET MMEEVMONIPOLY:MMESUPMONIEV="YES",MMESUPDELMONIEV="YES";|功能开关设置为支持。
2|配置与SCEF网元对接的Diameter偶联ADD SCTP:ID=3801,NAME="OFC2_SCEF_1",LOCPORT=48901,REMPORT=48901,LOCADDR1="192.10.100.75",REMADDR1="192.10.61.1",PROTOCALTYPE=DIAMETER配置与SCEF网元对接的Diameter连接ADD DIAMCONN:ADJNAME="SCEF-3601.ZTE.COM.CN",ADJDOMAIN="ZTE.COM.CN",SCTPID=3801配置与SCEF网元对接的Diameter链路组ADD DIAMLINKGROUP:LINKGRPID=801,SCTPLINKID=3801,PARTAKEMODE="PARTAKE"配置与SCEF网元对接的Diameter路由ADD DIAMROUTE:ROUTEID=801,LINKGRPID=801,ABILITY="T6a"配置与SCEF网元对接的Diameter路由组ADD DIAMROUTEGROUP:ROUTEGRPID=801,ROUTEID=801配置与SCEF网元对接的Diameter局向路由ADD DIAMADJROUTE:ADJROUTEID=801,ROUTEGROUP=801-1-100,REALM="ZTE.COM.CN",HOSTNAME="SCEF-3601.ZTE.COM.CN"配置与SCEF网元对接的Diameter局向ADD DIAMADJ:ADJID=801,ADJROUTEID=801配置与SCEF网元对接的SCEF配置ADD DIASCEF:SCEFNAME="SCEF-3601.ZTE.COM.CN",ADJOFFICEID=801|MME与SCEF对接。
3|SYNA|传表，将配置数据传送到前台。
调整特性 :本特性不涉及调整特性。 
测试用例 :测试项目|UE可达事件上报
---|---
测试目的|UE可达事件上报。
预置条件|MME设置支持事件监控。MME与SCEF对接成功，局向正常。
测试过程|用户附着成功。eNB释放S1连接。SCEF通过HSS订阅UE可达事件。UE发起业务请求流程。
通过准则|业务请求过程中MME发送UE可达事件给SCEF。
测试结果|–
常见问题处理 :SCEF通过HSS订阅监控事件，MME收到对应事件后没有触发，原因可能是监控周期已经过期。 
 缩略语 
 缩略语 
3GPP :3rd Generation Partnership Project第三代合作伙伴计划
# AIA 
Authentication-Information-Answer鉴权信息检索响应
# AIR 
Authentication-Information-Request鉴权信息检索请求
APN :Access Point Network接入点网络
# ARD 
Access Restriction Data	接入限制数据
# ARP 
Allocation and Retention Priority分配保持优先级
# AS 
Access Stratum接入层
# BS 
Base Station基站
# C-SGN 
CIoT Serving Gateway Node蜂窝物联网服务网关节点
# CIoT 
Cellular Internet of Things蜂窝物联网
# CN 
Core Network核心网
# CP 
Communication Pattern通信模式
# CRTP 
Compressing IP/UDP/RTP Headers头部压缩技术
# DDN 
Downlink Data Notification下行数据通知
DNS :Domain Name Server域名服务器
# DRX 
Discontinuous Reception 不连续接收
E-UTRAN :Evolved Universal Terrestrial Radio Access Network演进的通用陆地无线接入网络
# EBI 
EPS Bearer IDEPS承载标识
# eDRX 
extended Idle Mode DRX演进的DRX
# eMTC 
Enhanced Machine Type Communication增强机器类通信
# eNB 
Evolved Node B演进型基站
eNodeB :Evolved NodeB演进的NodeB
EPC :Evolved Packet Core演进的分组核心网
EPS :Evolved Packet System演进的分组系统
# ESM 
EPS Session ManagementEPS会话管理
FQDN :Fully Qualified Domain Name全称域名
# GSM 
Global System for Mobile Communications全球移动通信系统
GUTI :Globally Unique Temporary Identity全球唯一临时标识
# GW 
GateWay网关
# HLCom 
High Latency Communication高时延通讯
HSS :Home Subscriber Server归属用户服务器
IMSI :International Mobile Subscriber Identity国际移动用户标识
# IPHC 
Internet Protocol Header CompressionIP头压缩
# IWMSC 
Interworking Mobile Switching Center网间移动交换中心
# LPWAN 
Low-Power Wide-Area Network低功耗广域网
LTE :Long Term Evolution长期演进
# MM 
Mobility Management移动性管理
MME :Mobility Management Entity移动管理实体
# MO 
Mobile Originated移动台发起
# MPDCCH 
MTC Physical Downlink Control Channel机器类型通信物理下行控制信道
# MPS 
Multimedia Priority Service多媒体优先业务
# MT 
Mobile Terminated移动台终止
# MTC 
Machine Type Communication机器类型通信
NAS :Non-Access Stratum非接入层
# NB-IoT 
Narrow Band Internet of Things窄带物联网
# NPDCCH 
Narrowband Physical Downlink Control Channel窄带物理下行控制信道
PDN :Packet Data Network分组数据网
PDU :Packet Data Unit分组数据单元
PGW :PDN Gateway分组数据网网关
PLMN :Public Land Mobile Network公共陆地移动网
# PSM 
Power Saving Mode节电模式
# PTW 
Paging Time Window寻呼时间窗
RAT :Radio Access Technology无线接入技术
# ROHC 
Robust Header Compression健壮性头压缩
# RRC 
Radio Resource Control无线资源控制
# S1AP 
S1 Application ProtocolS1应用协议
# SAE 
System Architecture Evolution系统架构演进
# SCEF 
Service Capability Exposure Function服务能力开放功能（平台）
SGSN :Serving GPRS Support Node服务GPRS支持节点
SGW :Serving Gateway服务网关
# SMSC 
Short Message Service Center短消息中心
TA :Tracking Area跟踪区域
TAU :Tracking Area Update跟踪区域更新
# TEID 
Tunnel Endpoint Identifier隧道端点标识
UE :User Equipment用户设备
# UMTS 
Universal Mobile Telecommunication System通用移动通讯系统
# VJHC 
Van Jacobson’s Header Compression范•雅各布森头压缩
# WB 
Wideband 宽频带/宽带
# WUS 
Wake Up Signal唤醒信号
